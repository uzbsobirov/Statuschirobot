from loader import dp, bot, db, db_json
from states.makestatus import Status

from aiogram import types
from aiogram.dispatcher import FSMContext
from PIL import Image, ImageDraw, ImageFont

@dp.message_handler(text="📝 Rasmga Status Tayorlash ✍️", state='*')
async def make_status(message: types.Message, state: FSMContext):
    text = "<b>Rasm yuboring...</b>\n\n" \
           "<i>Chiroyli va pechatsiz rasmlarni <b>@page_ea7</b> kanalidan olishingiz mumkin😉</i>"
    await message.answer(text=text)
    await Status.image.set()

@dp.message_handler(state=Status.image, content_types=types.ContentType.PHOTO)
async def state_image(message: types.Message, state: FSMContext):
    file_id = message.photo[-1].file_id
    await state.update_data(
        {'file_id': file_id}
    )
    text = "Rasm saqlandi✅\n\n<i>Endi rasm uchun status yuboring...</i>\n\n"
    await message.answer(text=text)
    await Status.text.set()

@dp.message_handler(state=Status.text)
async def state_status(message: types.Message, state: FSMContext):
    user_id = message.from_user.id

    datas = await db.select_one_user(user_id=user_id)
    text_shrift = datas[0][5]
    text_size = datas[0][6]
    text_color = datas[0][7]
    text_place = datas[0][4]

    """
    36 == 25%
    48 == 50%
    60 == 75%
    72 == 100%
    """

    get_me = await bot.get_me()
    data = await state.get_data()

    file_id = data.get('file_id')
    photo_info = await bot.get_file(file_id)
    file_path = photo_info['file_path']
    await bot.download_file(file_path, "image.jpg")
    status = message.text

    path_photo = 'C:/Users/Servis/Documents/Programming/Bot/Statuschirobot/image.jpg'
    img = Image.open(path_photo)
    draw = ImageDraw.Draw(img)
    if text_shrift == 'shrift1':
        font = ImageFont.truetype("media/OpenSans.ttf", text_size)
        text_size = draw.textbbox((100, 100), status, font=font)

        x = (img.width - text_size[2]) / 2
        y = (img.height - text_size[2]) / 2

        draw.text((x, y), status, font=font, fill=text_color)
        img.save("media/results.jpg")
        with open(file='media/results.jpg', mode='rb') as photo:
            caption = f"📝<code>{status}</code>\n\n✅<b> @{get_me.username} orqali taqdim etildi!</b>"
            await message.answer_photo(photo=photo, caption=caption)
            await state.finish()

    elif text_shrift == 'shrift2':
        font = ImageFont.truetype("media/allura.otf", text_size)
        text_size = draw.textbbox((100, 100), status, font=font)

        x = (img.width - text_size[2]) / 2
        y = (img.height - text_size[2]) / 2

        draw.text((x, y), status, font=font, fill=text_color)
        img.save("media/results.jpg")
        with open(file='media/results.jpg', mode='rb') as photo:
            caption = f"📝<code>{status}</code>\n\n✅<b> @{get_me.username} orqali taqdim etildi!</b>"
            await message.answer_photo(photo=photo, caption=caption)
            await state.finish()