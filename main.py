from builder import build_site
import webbrowser, pathlib

if __name__ == "__main__":
    build_site()
    index_path = pathlib.Path(__file__).parent / "dist" / "index.html"
    webbrowser.open(index_path.as_uri())