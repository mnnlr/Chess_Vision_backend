# Chess Vision Backend

This project provides a backend service for detecting chess pieces and generating FEN strings from chessboard images using a YOLOv7 object detection model. The service is built with Flask and relies on a pretrained YOLOv7 model for piece detection.

## Project Structure

- **`chess/`**: Contains the core logic of the application.
  - **`fenstring.py`**: Contains functions for converting board matrix to FEN string.
  - **`board.py`**: Contains functions for detecting and cropping the chessboard from an image.
  - **`predict.py`**: Contains functions for predicting chess pieces and drawing results.
- **`models/`**: Contains the pretrained YOLOv7 model file.
  - **`best.pt`**: The pretrained YOLOv7 model for chess piece detection.
- **`app.py`**: The main Flask application file that runs the backend service.

## Prerequisites

Ensure you have the following installed:

- Python 3.x
- Flask
- OpenCV
- PyTorch
- Other dependencies listed in `requirements.txt`

## Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Install required Python packages:**

   Create a virtual environment (optional but recommended) and install the dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Download the YOLOv7 model:**

   Ensure that the `best.pt` file is located in the `models/` directory. If you don't have the model file, download it from your source and place it in the `models/` folder.

## Running the Application

To start the Flask application, use one of the following commands:

- **Using Flask CLI:**

  ```bash
  flask run
  ```

  Ensure you have set the `FLASK_APP` environment variable to `app.py`:

  ```bash
  export FLASK_APP=app.py  # On Windows, use `set FLASK_APP=app.py`
  ```

- **Directly with Python:**

  ```bash
  python app.py
  ```

By default, the application will run on `http://127.0.0.1:5000`.

## Testing the Application

You can test the `/fen-string` route using Postman:

1. **Open Postman.**
2. **Set the request type to POST.**
3. **Enter the URL:** `http://127.0.0.1:5000/fen-string`
4. **Select the "Body" tab and choose "form-data".**
5. **Add a key named `image` with the type set to "File".**
6. **Choose an image file of a chessboard to upload.**
7. **Send the request.**

The server will respond with a JSON object containing the FEN string representation of the chessboard.

