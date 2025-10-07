import random

PALETTES = [
    {
        "name": "light",
        "bg": "#ffffff",
        "text": "#222222",
        "muted": "#f3f4f6",
        "primary": "#2563eb",
        "accent": "#0ea5e9",
    },
    {
        "name": "dark",
        "bg": "#111827",
        "text": "#f9fafb",
        "muted": "#1f2937",
        "primary": "#a78bfa",
        "accent": "#f472b6",
    },
    {
        "name": "forest",
        "bg": "#f0fdf4",
        "text": "#064e3b",
        "muted": "#d1fae5",
        "primary": "#065f46",
        "accent": "#10b981",
    },
    {
        "name": "rose",
        "bg": "#fff1f2",
        "text": "#4c0519",
        "muted": "#ffe4e6",
        "primary": "#db2777",
        "accent": "#f43f5e",
    },
    {
        "name": "solar",
        "bg": "#fefce8",
        "text": "#78350f",
        "muted": "#fef3c7",
        "primary": "#d97706",
        "accent": "#f59e0b",
    },
    {
        "name": "midnight",
        "bg": "#0f172a",
        "text": "#e2e8f0",
        "muted": "#1e293b",
        "primary": "#3b82f6",
        "accent": "#60a5fa",
    },
    {
        "name": "lavender",
        "bg": "#faf5ff",
        "text": "#4a044e",
        "muted": "#f3e8ff",
        "primary": "#9333ea",
        "accent": "#c084fc",
    },
    {
        "name": "aqua",
        "bg": "#ecfeff",
        "text": "#042f2e",
        "muted": "#cffafe",
        "primary": "#06b6d4",
        "accent": "#22d3ee",
    },
]
FONTS = [
    ("sans", "Inter, Arial, Helvetica, sans-serif"),
    ("serif", "Georgia, 'Times New Roman', serif"),
    ("mono", "'Fira Code', 'Courier New', monospace"),
    ("rounded", "'Nunito', 'Quicksand', sans-serif"),
    ("modern", "'Poppins', 'Segoe UI', sans-serif"),
    ("slab", "'Roboto Slab', 'Times New Roman', serif"),
]

def pick():
    """
    Pick a random visual theme configuration.
    :return: dict : {
                        "palette": dict with colors keys,
                        "font": tuple(name, css_font_family)
                    }
    """
    return {
        "palette": random.choice(PALETTES),
        "font": random.choice(FONTS)
    }
