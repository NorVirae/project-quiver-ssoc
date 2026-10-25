from pathlib import Path
from flask import Flask, send_from_directory

DIST = Path(__file__).parent / "dist"
app = Flask(__name__)


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve(path):
    path = path.rstrip("/")
    target = DIST / path

    if path == "":
        return send_from_directory(DIST, "index.html")
    if target.is_dir():
        return send_from_directory(DIST, f"{path}/index.html")
    if target.is_file():
        return send_from_directory(DIST, path)

    if (DIST / "404.html").exists():
        return send_from_directory(DIST, "404.html"), 404
    return "Not found", 404