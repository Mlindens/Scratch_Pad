# Importing necessary modules: sys for system-specific parameters and functions, 
# QApplication from PySide6 for creating the application object
import sys
from PySide6.QtWidgets import QApplication

# Importing the MainWindow class from the mainwindow file
from mainwindow import MainWindow

# Initializing the QApplication object with command line arguments
app = QApplication(sys.argv)

# Creating an object of MainWindow class
w = MainWindow(app)

# Making the window visible
w.show()

# Starting the application's event loop
app.exec()
