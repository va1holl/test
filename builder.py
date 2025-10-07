import random, pathlib
from datetime import date
import themes, sections

DIST = pathlib.Path(__file__).parent / "dist"
DIST.mkdir(exist_ok=True)

def build_site():
    """
    Generate the static website files.

    - Picks a random theme configuration using `themes.pick()`.
    - Builds the HTML and CSS using helper functions.
    - Writes the generated files (`index.html`, `styles.css`) into the `dist` directory.
    - Prints the chosen theme name and font for reference.
    """
    cfg = themes.pick()

    html = build_html(cfg)
    css = build_css(cfg)

    (DIST / "index.html").write_text(html, encoding="utf-8")
    (DIST / "styles.css").write_text(css, encoding="utf-8")

    print(f"Theme: {cfg['palette']['name']} | Font: {cfg['font'][0]}")

def build_html(cfg):
    """
    Construct the full HTML content for the static website.

    Args:
        cfg (dict): The configuration dictionary containing theme, font, and color palette data.

    Returns:
        str: Complete HTML markup for the page.

    Description:
        - Calls section-building functions from `sections` (hero, features, contacts, quotes, pricing, gallery).
        - Randomizes their order to make each build unique.
        - Wraps them inside a complete HTML structure with header and footer.
    """

    blocks = [
        sections.hero(cfg),
        sections.features(cfg),
        sections.contacts(cfg),
        sections.quotes(cfg),
        sections.pricing(cfg),
        sections.gallery(cfg),
        sections.faq(cfg)
    ]

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
              <header><div class="container"><h1 class="brand">StaticGen</h1></div></header>
              {''.join(blocks)}
              <footer><div class="container">&copy; {date.today().year} StaticGen</div></footer>
            </body>
            </html>"""

def build_css(cfg):
    """
    Generate the CSS stylesheet for the website.

    Args:
        cfg (dict): Theme configuration containing palette colors and font definitions.

    Returns:
        str: The CSS string with all color variables, layout styles, and responsive rules.

    Description:
        - Defines CSS variables based on the selected theme palette.
        - Applies consistent typography and layout.
        - Includes grid layout for feature cards and responsive design for small screens.
        - Adds style definitions for all section classes (hero, gallery, pricing, etc.).
        - Adds randomized stylistic variation for border radius and shadow intensity.
    """
    import random

    p = cfg["palette"]
    font_name, font_stack = cfg["font"]

    radius = random.choice(["6px", "8px", "12px", "16px"])
    shadow = random.choice([
        "0 2px 6px rgba(0,0,0,.1)",
        "0 4px 12px rgba(0,0,0,.15)",
        "0 6px 20px rgba(0,0,0,.25)"
    ])

    return f"""
    :root {{
      --bg: {p['bg']}; 
      --text: {p['text']}; 
      --muted: {p['muted']};
      --primary: {p['primary']}; 
      --accent: {p['accent']};
      --radius: {radius};
      --shadow: {shadow};
    }}

    body {{
      margin: 0;
      background: var(--bg);
      color: var(--text);
      font-family: {font_stack};
      line-height: 1.5;
    }}

    .container {{
      max-width: 900px;
      margin: 0 auto;
      padding: 20px;
    }}

    header {{
      padding: 10px 0;
      border-bottom: 1px solid var(--muted);
    }}

    footer {{
      border-top: 1px solid var(--muted);
      font-size: 14px;
      opacity: .7;
      padding: 10px 0;
    }}

    .btn {{
      background: var(--primary);
      color: #fff;
      padding: 10px 16px;
      border-radius: var(--radius);
      display: inline-block;
      text-decoration: none;
      box-shadow: var(--shadow);
      transition: transform .2s ease;
    }}

    .btn:hover {{
      transform: translateY(-2px);
    }}

    .card {{
      background: var(--muted);
      padding: 16px;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
    }}

    .grid {{
      display: grid;
      gap: 16px;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    }}

    .features, .pricing, .stats {{
      display: grid;
      gap: 20px;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      margin-top: 20px;
    }}

    .gallery {{
      display: grid;
      gap: 12px;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    }}

    .gallery img {{
      width: 100%;
      height: auto;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
    }}

    .hero {{
      text-align: center;
      padding: 60px 20px;
      background: var(--accent);
      color: #fff;
      border-radius: var(--radius);
    }}

    .pricing .card.highlight {{
      outline: 2px solid var(--accent);
      transform: translateY(-2px);
    }}

    .faq {{
      margin-top: 30px;
    }}

    .faq details {{
      background: var(--muted);
      border-radius: var(--radius);
      padding: 10px 14px;
      margin-bottom: 8px;
      box-shadow: var(--shadow);
    }}

    .stats .card h3 {{
      font-size: 2em;
      margin-bottom: 8px;
    }}

    .cta {{
      text-align: center;
      padding: 40px 20px;
      background: var(--primary);
      color: #fff;
      border-radius: var(--radius);
    }}

    @media (max-width:600px) {{
      .features, .pricing, .gallery, .stats {{
        grid-template-columns: 1fr;
      }}
    }}
    """
