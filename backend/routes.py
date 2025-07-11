from flask import Blueprint, request, jsonify
import boto3
import os
from backend.db import get_db_connection
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
from datetime import datetime
from prometheus_client import Counter


load_dotenv()

s3 = boto3.client(
    "s3",
    region_name=os.getenv("AWS_REGION", "us-east-1"),
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
)

routes = Blueprint("routes", __name__)

upload_counter = Counter(
    "file_upload_total",
    "Total number of uploaded files",
    ["status"]
)

@routes.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    filename = secure_filename(file.filename)

    try:
        # Upload to S3
        s3.upload_fileobj(
            file,
            os.getenv("S3_BUCKET_NAME"),
            filename,
            ExtraArgs={"ACL": "private"}
        )

        # Record to DB with timestamp
        timestamp = datetime.utcnow().isoformat()
        conn = get_db_connection()
        conn.execute(
            "INSERT INTO uploads (filename, status, uploaded_at) VALUES (?, ?, ?)",
            (filename, "uploaded", timestamp)
        )
        conn.commit()
        conn.close()

        # Increment Prometheus metric
        upload_counter.labels(status="success").inc()

        return jsonify({
            "message": "File uploaded successfully",
            "filename": filename
        }), 200

    except Exception as e:
        upload_counter.labels(status="failure").inc()
        return jsonify({"error": str(e)}), 500

@routes.route("/uploads", methods=["GET"])
def get_uploaded_files():
    try:
        conn = get_db_connection()
        uploads = conn.execute("SELECT id, filename, status, uploaded_at FROM uploads ORDER BY uploaded_at DESC").fetchall()
        conn.close()

        results = [dict(row) for row in uploads]
        return jsonify(results), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@routes.route("/", methods=["GET"])
def health_check():
    return jsonify({"message": "Ingestion backend running ✅"}), 200

