import os
import shutil
from pathlib import Path
from ultralytics import YOLO

path = Path('../runs/detect/train7/weights/best.pt')


def predict_image(image, image_name):
    model = YOLO(path)
    # Add a project name because model saves default path for saving objects underhood
    model.predict([image], save=True, project='./runs/detect/temp', name='', line_thickness=1)

    # Rename image0.jpg file from default models root path /runs/detect/predict
    output_dir = Path("./runs/detect/temp/predict")
    old_name = os.path.join(output_dir, "image0.jpg")
    new_name = os.path.join(output_dir, f"{image_name}")
    os.rename(old_name, new_name)

    new_folder = Path("./static/uploads")
    new_path = os.path.join(new_folder, f"{image_name}")
    shutil.move(new_name, new_path)
    shutil.rmtree(output_dir)
