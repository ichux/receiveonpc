import os

from flask import Flask, redirect, render_template, request, url_for
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {"mp4", "avi", "mov", "mkv"}

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return redirect(request.url)

    file = request.files["file"]
    if file.filename == "":
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        return redirect(url_for("uploaded_file", filename=filename))
    else:
        return "Invalid file format. Allowed formats: mp4, avi, mov, mkv"


@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return f"File {filename} has been uploaded successfully."
