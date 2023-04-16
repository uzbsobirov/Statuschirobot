from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool

from data import config


class Database:
    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME,
        )

    async def execute(
            self,
            command,
            *args,
            fetch: bool = False,
            fetchval: bool = False,
            fetchrow: bool = False,
            execute: bool = False,
    ):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    async def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
        id SERIAL PRIMARY KEY,
        full_name VARCHAR(255) NOT NULL,
        username varchar(255) NULL,
        user_id BIGINT NOT NULL UNIQUE,
        text_place TEXT,
        text_shrift TEXT,
        text_size INTEGER,
        text_color TEXT
        );
        """
        await self.execute(sql, execute=True)

    async def create_table_sponsor(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Sponsor (
        id SERIAL PRIMARY KEY,
        channel TEXT NULL UNIQUE
        );
        """
        await self.execute(sql, execute=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join(
            [f"{item} = ${num}" for num, item in enumerate(parameters.keys(), start=1)]
        )
        return sql, tuple(parameters.values())

    async def add_user(self, full_name: str, username: str, user_id: int, text_place: str, text_shrift: str, text_size: int, text_color: str):
        sql = "INSERT INTO users (full_name, username, user_id, text_place, text_shrift, text_size, text_color) VALUES($1, $2, $3, $4, $5, $6, $7) returning *"
        return await self.execute(sql, full_name, username, user_id, text_place, text_shrift, text_size, text_color, fetchrow=True)

    async def add_channel(self, channel):
        sql = "INSERT INTO Sponsor (channel) VALUES($1) returning *"
        return await self.execute(sql, channel, fetchrow=True)

    async def select_all_users(self):
        sql = "SELECT * FROM Users"
        return await self.execute(sql, fetch=True)

    async def select_one_user(self, user_id):
        sql = "SELECT * FROM Users WHERE user_id=$1"
        return await self.execute(sql, user_id, fetch=True)


    async def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def count_users(self):
        sql = "SELECT COUNT(*) FROM Users"
        return await self.execute(sql, fetchval=True)

    async def select_row_panel(self):
        sql = "SELECT * FROM Sponsor"
        return await self.execute(sql, fetch=True)

    async def update_user_issubs(self, issubs, user_id):
        sql = "UPDATE Users SET issubs=$1 WHERE user_id=$2"
        return await self.execute(sql, issubs, user_id, execute=True)

    async def update_text_shrift(self, text_shrift, user_id):
        sql = "UPDATE Users SET text_shrift=$1 WHERE user_id=$2"
        return await self.execute(sql, text_shrift, user_id, execute=True)

    async def update_text_size(self, text_size, user_id):
        sql = "UPDATE Users SET text_size=$1 WHERE user_id=$2"
        return await self.execute(sql, text_size, user_id, execute=True)

    async def update_text_color(self, text_color, user_id):
        sql = "UPDATE Users SET text_color=$1 WHERE user_id=$2"
        return await self.execute(sql, text_color, user_id, execute=True)

    async def update_text_place(self, text_place, user_id):
        sql = "UPDATE Users SET text_place=$1 WHERE user_id=$2"
        return await self.execute(sql, text_place, user_id, execute=True)

    async def delete_user(self, user_id):
        sql = "DELETE FROM Users WHERE user_id=$1"
        await self.execute(sql, user_id, execute=True)

    async def delete_sponsor_channel(self, channel):
        sql = "DELETE FROM Sponsor WHERE channel=$1"
        await self.execute(sql, channel, execute=True)


    async def drop_courses(self):
        await self.execute("DROP TABLE Courses", execute=True)