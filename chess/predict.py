import cv2

def predict_and_draw(img_array, model):
    if img_array is None:
        raise ValueError("Input image array is None")
    img_rgb = cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB)
    results = model(img_rgb)
    df = results.pandas().xyxy[0]
    print(df) 
    board_matrix = [['.' for _ in range(8)] for _ in range(8)]
    img_size = img_array.shape[0]
    square_size = img_size // 8
    class_names = model.names
    for index, row in df.iterrows():
        x1, y1, x2, y2, conf, cls = row['xmin'], row['ymin'], row['xmax'], row['ymax'], row['confidence'], row['class']
        if conf > 0.8 and class_names[int(cls)] != "board":
            center_x = (x1 + x2) / 2
            center_y = (y1 + y2) / 2
            grid_x = int(center_x // square_size)
            grid_y = int(center_y // square_size)
            grid_x = min(max(grid_x, 0), 7)
            grid_y = min(max(grid_y, 0), 7)
            piece_symbol = class_names[int(cls)][0]
            board_matrix[grid_y][grid_x] = piece_symbol
    print(board_matrix)
    return board_matrix
