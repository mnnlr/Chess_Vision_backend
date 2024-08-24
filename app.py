import torch
from chess.board import detect_and_crop_chessboard
from chess.predict import predict_and_draw
from chess.fenstring import board_to_fen
from flask import Flask, request, jsonify
from PIL import Image
import numpy as np 
import cv2
import io

app = Flask(__name__)

model = torch.hub.load('WongKinYiu/yolov7', 'custom', './models/best.pt', force_reload=True)
print("Model loaded successfully!")

@app.route('/fen-string', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image part in the request"}), 400
    file = request.files['image']
    if file.filename == '':
        return jsonify({"error": "No image selected for uploading"}), 400
    try:
        image_bytes = file.read()
        image_np = np.frombuffer(image_bytes, np.uint8)
        print(image_np)
        image = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
        print(image)
        if image is None:
            return jsonify({"error": "Failed to decode the image. Ensure it is a valid image file."}), 400
        cv2.imwrite('temp_uploaded_image.jpg', image)
        print("written success full")
        cropped_chessboard = detect_and_crop_chessboard(image)
        print("chessboard cropped succesfully")
        board_matrix= predict_and_draw(cropped_chessboard, model)
        print("matrix returned successfully")
        fen_string = board_to_fen(board_matrix)
        print("fen returnded")
        return jsonify({
            "message": "Image successfully uploaded and processed",
            "fen": fen_string
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
