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

def detect_shrift(shrift):
    if shrift == 'shrift1':
        new_shrift = "1-shrift"
        return new_shrift
    elif shrift == 'shrift2':
        new_shrift = "2-shrift"
        return new_shrift
    elif shrift == 'shrift3':
        new_shrift = "3-shrift"
        return new_shrift
    elif shrift == 'shrift4':
        new_shrift = "4-shrift"
        return new_shrift
    elif shrift == 'shrift5':
        new_shrift = "5-shrift"
        return new_shrift

def detect_shrift_ttf(ttf):
    if ttf == 'shrift1':
        ttf = "media/OpenSans.ttf"
        return ttf
    elif ttf == 'shrift2':
        ttf = "media/allura.otf"
        return ttf
    elif ttf == 'shrift3':
        ttf = "media/ostrich.otf"
        return ttf
    elif ttf == 'shrift4':
        ttf = "media/Quicksand-Light.otf"
        return ttf
    elif ttf == 'shrift5':
        ttf = "media/Quicksand_Dash.otf"
        return ttf

def detect_place(place, x, y, text_size):
    if place == 'left':
        x = ((x.width - text_size[2]) / 2) - text_size[0]
        y = (y.height - text_size[2]) / 2 - text_size[0]
        return x, y
    elif place == 'bottom_center':
        x = x.width / 2
        y = y.height - text_size[0]
        return x, y
    elif place == 'center':
        x = x.width / 2 - text_size[3]
        y = y.height / 2 - text_size[1]
        return x, y
    elif place == 'top_center':
        x = (x.width / 2) - text_size[0]
        y = (y.height / 2) - text_size[2]
        return x, y
    elif place == 'right':
        x = x.width - text_size[2]
        y = (y.height / 2) - text_size[1]
        return x, y