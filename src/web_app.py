from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template(
        "setup_index.html"
    )

if __name__ == "__main__":
    app.run(debug=True, port=6060)