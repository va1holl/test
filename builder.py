import random, pathlib
from datetime import date
import themes, sections

DIST = pathlib.Path(__file__).parent / "dist"
DIST.mkdir(exist_ok=True)

def build_site():
    cfg = themes.pick()

    html = build_html(cfg)
    css = build_css(cfg)

    (DIST / "index.html").write_text(html, encoding="utf-8")
    (DIST / "styles.css").write_text(css, encoding="utf-8")

    print(f"Тема: {cfg['palette']['name']} | Шрифт: {cfg['font'][0]}")

def build_html(cfg):
    blocks = [sections.hero(cfg), sections.features(cfg), sections.contacts(cfg)]
    random.shuffle(blocks)
    return f"""<!doctype html>
            <html lang="en">
            <head>
              <meta charset="utf-8">
              <meta name="viewport" content="width=device-width, initial-scale=1">
              <title>Static Site</title>
              <link rel="stylesheet" href="styles.css">
            </head>
            <body>
              <header><div class="container"><span class="brand">StaticGen</span></div></header>
              {''.join(blocks)}
              <footer><div class="container">&copy; {date.today().year} StaticGen</div></footer>
            </body>
            </html>"""

def build_css(cfg):
    p = cfg["palette"]
    font_name, font_stack = cfg["font"]
    return f"""
            :root {{
              --bg: {p['bg']}; --text: {p['text']}; --muted: {p['muted']};
              --primary: {p['primary']}; --accent: {p['accent']};
            }}
            body {{
              margin:0; background:var(--bg); color:var(--text);
              font-family:{font_stack}; line-height:1.5;
            }}
            .container {{ max-width:900px; margin:0 auto; padding:20px; }}
            header,footer {{ padding:10px 0; border-bottom:1px solid var(--muted); }}
            footer {{ border-top:1px solid var(--muted); font-size:14px; opacity:.7; }}
            .btn {{
              background:var(--primary); color:#fff; padding:10px 16px; border-radius:8px;
              display:inline-block; text-decoration:none;
            }}
            .features {{ display:grid; gap:16px; grid-template-columns:repeat(auto-fit,minmax(200px,1fr)); }}
            .card {{ background:var(--muted); padding:16px; border-radius:8px; }}
            @media (max-width:600px) {{
              .features {{ grid-template-columns:1fr; }}
            }}
            """
