import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QHBoxLayout
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model

# Load the model
model = load_model('../model/traffic_classifier.h5')

# Dictionary to label all traffic signs classes
classes = {1: 'Speed limit (20km/h)', 2: 'Speed limit (30km/h)', 3: 'Speed limit (50km/h)', 
            4: 'Speed limit (60km/h)', 5: 'Speed limit (70km/h)', 6: 'Speed limit (80km/h)', 
            7: 'End of speed limit (80km/h)', 8: 'Speed limit (100km/h)', 9: 'Speed limit (120km/h)', 
            10: 'No passing', 11: 'No passing veh over 3.5 tons', 12: 'Right-of-way at intersection', 
            13: 'Priority road', 14: 'Yield', 15: 'Stop', 16: 'No vehicles', 17: 'Veh > 3.5 tons prohibited', 
            18: 'No entry', 19: 'General caution', 20: 'Dangerous curve left', 21: 'Dangerous curve right', 
            22: 'Double curve', 23: 'Bumpy road', 24: 'Slippery road', 25: 'Road narrows on the right', 
            26: 'Road work', 27: 'Traffic signals', 28: 'Pedestrians', 29: 'Children crossing', 
            30: 'Bicycles crossing', 31: 'Beware of ice/snow', 32: 'Wild animals crossing', 
            33: 'End speed + passing limits', 34: 'Turn right ahead', 35: 'Turn left ahead', 
            36: 'Ahead only', 37: 'Go straight or right', 38: 'Go straight or left', 
            39: 'Keep right', 40: 'Keep left', 41: 'Roundabout mandatory', 
            42: 'End of no passing', 43: 'End no passing veh > 3.5 tons'}

class TrafficSignClassifier(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the layout
        self.layout = QVBoxLayout()
        self.image_layout = QHBoxLayout()

        # Create widgets
        self.label = QLabel("Upload an image to classify")
        self.label.setFont(QFont("Arial", 16, QFont.Bold))
        self.label.setAlignment(Qt.AlignCenter)
        self.image_label = QLabel()
        self.upload_button = QPushButton("Upload Image")
        self.upload_button.setStyleSheet("background-color: #4CAF50; color: white; font-weight: bold;")
        self.classify_button = QPushButton("Classify Image")
        self.classify_button.setStyleSheet("background-color: #f44336; color: white; font-weight: bold;")
        self.classify_button.setEnabled(False)

        # Set style
        self.setStyleSheet("background-color: #f0f0f0;")
        self.image_label.setStyleSheet("border: 2px solid #ddd;")
        
        # Add widgets to layout
        self.image_layout.addWidget(self.image_label)
        self.image_layout.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label)
        self.layout.addLayout(self.image_layout)
        self.layout.addWidget(self.upload_button)
        self.layout.addWidget(self.classify_button)

        # Set layout
        self.setLayout(self.layout)

        # Connect buttons
        self.upload_button.clicked.connect(self.upload_image)
        self.classify_button.clicked.connect(self.classify_image)

    def upload_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Images (*.png *.jpg *.bmp)")
        if file_path:
            self.file_path = file_path
            pixmap = QPixmap(file_path)
            self.image_label.setPixmap(pixmap.scaled(400, 400, Qt.KeepAspectRatio))
            self.classify_button.setEnabled(True)

    def classify_image(self):
        image = Image.open(self.file_path)
        image = image.resize((30, 30))
        image = np.expand_dims(image, axis=0)
        image = np.array(image)
        predictions = model.predict(image)
        pred_class = np.argmax(predictions, axis=-1)[0]
        confidence = np.max(predictions) * 100
        sign = classes[pred_class + 1]
        self.label.setText(f"Prediction: {sign}\nConfidence: {confidence:.2f}%")

    def closeEvent(self, event):
        """Handle the window close event."""
        sys.exit(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TrafficSignClassifier()
    window.setWindowTitle('Traffic Sign Classification')
    window.resize(800, 600)
    window.setStyleSheet("font-family: Arial;")
    window.show()
    sys.exit(app.exec_())
