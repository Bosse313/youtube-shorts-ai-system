from flask import Flask, jsonify, request, send_from_directory
from pathlib import Path

from backend.trending_analyzer import find_trend, get_trends
from backend.video_generator import generate_video_plan

ROOT_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = ROOT_DIR / "frontend"

app = Flask(__name__, static_folder=str(FRONTEND_DIR), static_url_path="")

state = {
    "generated": [],
    "last_selected": None,
}


@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")


@app.route("/workflow3d")
def workflow3d():
    return send_from_directory(app.static_folder, "workflow3d.html")


@app.route("/api/health")
def health():
    return jsonify({"status": "ok", "message": "YouTube Shorts AI System aktiv"})


@app.route("/api/trends")
def trends():
    return jsonify({"trends": get_trends()})


@app.route("/api/workflow")
def workflow():
    return jsonify({
        "generated": state["generated"],
        "last_selected": state["last_selected"],
    })


@app.route("/api/generate", methods=["POST"])
def generate():
    payload = request.get_json(silent=True) or {}
    trend_id = payload.get("trend_id")
    trend = find_trend(trend_id) if trend_id else get_trends()[0]

    video = generate_video_plan(trend)
    video["approved"] = False
    video["status"] = "queued"

    state["generated"].append(video)
    state["last_selected"] = video

    return jsonify({"ok": True, "video": video})


@app.route("/api/approve", methods=["POST"])
def approve():
    payload = request.get_json(silent=True) or {}
    video_id = payload.get("video_id")

    for video in state["generated"]:
        if video["id"] == video_id:
            video["approved"] = True
            video["status"] = "approved_for_upload"
            state["last_selected"] = video
            return jsonify({"ok": True, "video": video})

    return jsonify({"ok": False, "message": "Video nicht gefunden"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
