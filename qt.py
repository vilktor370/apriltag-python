import cv2
from PySide6 import QtWidgets, QtGui
import numpy as np

def arrayToImg(cvImg):
    """
    numpy array to QImage

    Args:
        cvImg (numpy array): _description_
    """
    height, width, channel = cvImg.shape
    bytesPerLine = 3 * width
    qImg = QtGui.QImage(cvImg.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
    return qImg


class PhotoViewer(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(PhotoViewer, self).__init__(parent)
        # Create a label to display the image
        self.label = QtWidgets.QLabel(self)
        self.label.setFixedSize(400, 400)
        # Create a push button to go to the next image
        self.next_button = QtWidgets.QPushButton('Next', self)
        self.next_button.clicked.connect(self.show_next_image)
        # Create a push button to select the image path
        self.select_path_button = QtWidgets.QPushButton('Select Path', self)
        self.select_path_button.clicked.connect(self.select_path)
        # Create a push button for selecting a region of the image
        self.select_region_button = QtWidgets.QPushButton('Select Region', self)
        self.select_region_button.clicked.connect(self.select_region)
        # Create a line edit for entering the value to set the selected region to
        self.region_value_edit = QtWidgets.QLineEdit(self)
        # Create a push button for setting the selected region to the entered value
        self.set_region_button = QtWidgets.QPushButton('Set', self)
        self.set_region_button.clicked.connect(self.set_region)
        # Create a vertical layout to add the widgets to
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.next_button)
        self.layout.addWidget(self.select_path_button)
        self.layout.addWidget(self.select_region_button)
        
        hbox = QtWidgets.QHBoxLayout(self)
        hbox.addWidget(self.region_value_edit)
        hbox.addWidget(self.set_region_button)
        self.layout.addLayout(hbox)
        # Set the initial image path and image
        self.image_path = '.'
        self.current_image = 0
        self.image_data = None
        self.show_next_image()
        
        
    def select_path(self):
        # Get the selected path from the user
        # selected_path = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Image Path')
        selected_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Select Image', '', 'Image files (*.png *.jpeg *.jpg)')

        # Update the image path and show the first image in the new path
        if selected_path:
            self.image_path = selected_path
            self.current_image = 0
            self.show_next_image()

    def show_next_image(self):
        # Get the list of images in the current directory
        # image_files = [f for f in os.listdir(self.image_path) if (f.endswith('.jpg') or f.endswith('.png') or f.endswith('.jpeg'))]
        image_files = self.image_path
        print(image_files)
        # Check if there are any images
        if not image_files:
            self.label.setText('No images found')
            return
        # Show the next image
        self.current_image = (self.current_image + 1) % len(image_files)
        # image = QtGui.QPixmap(os.path.join(self.image_path, image_files[self.current_image]))
        image = QtGui.QPixmap(image_files)
        image = image.scaled(400, 400)
        self.label.setPixmap(image)
        
        
    def select_region(self):
        qimage = self.label.pixmap().toImage()
        img_bytes = qimage.constBits()[:]
        print(img_bytes)
        img = np.frombuffer(img_bytes, np.uint8, qimage.width(), qimage.height())
        x, y, w, h = cv2.selectROI(img)

        # Crop the image to the selected ROI
        cropped_image = img[y:y+h, x:x+w]
        
        # Convert the NumPy array to a QImage
        qimage = arrayToImg(cropped_image)

        # Create a QPixmap from the QImage
        pixmap = QtGui.QPixmap.fromImage(qimage)
        
        self.label.setPixmap(pixmap)

    
    def set_region(self, region):
        pass

if __name__ == '__main__':
    # Create the Qt Application
    app = QtWidgets.QApplication([])
    # Create and show the photo viewer
    viewer = PhotoViewer()
    viewer.show()
    # Run the main Qt loop
    app.exec_()
