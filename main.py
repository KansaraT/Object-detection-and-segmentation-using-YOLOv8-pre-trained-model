from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n-seg.pt")  # load a pretrained model (recommended for training)

# Use the model
results = model("https://ultralytics.com/images/bus.jpg")  # predict on an image