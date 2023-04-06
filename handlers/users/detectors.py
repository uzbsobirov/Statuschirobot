def detect_color(color):
    if color == 'white':
        new_color = "⚪️ Oq"
        return new_color
    elif color == 'green':
        new_color = "🟢 Yashil"
        return new_color
    elif color == 'black':
        new_color = "⚫️ Qora"
        return new_color
    elif color == 'yellow':
        new_color = "🟡 Sariq"
        return new_color
    elif color == 'blue':
        new_color = "🔵 Ko'k"
        return new_color
    elif color == 'purple':
        new_color = "🟣 Pushti"
        return new_color

def detect_size(size):
    if size == 25:
        new_size = "25%"
        return new_size
    elif size == 50:
        new_size = "50%"
        return new_size
    elif size == 75:
        new_size = "75%"
        return new_size
    elif size == 100:
        new_size = "100%"
        return new_size
