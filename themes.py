import random

PALETTES = [
    {"name":"light","bg":"#ffffff","text":"#222","muted":"#f3f4f6","primary":"#2563eb","accent":"#0ea5e9"},
    {"name":"dark","bg":"#111827","text":"#f9fafb","muted":"#1f2937","primary":"#a78bfa","accent":"#f472b6"},
]
FONTS = [
    ("sans","Arial, Helvetica, sans-serif"),
    ("serif","Georgia, 'Times New Roman', serif")
]

def pick():
    return {
        "palette": random.choice(PALETTES),
        "font": random.choice(FONTS)
    }
