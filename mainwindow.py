# Importing necessary modules from PySide6 for GUI
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox

# Importing the UI design for the main window
from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    MainWindow class that creates the main window for the app and sets up UI. Inherits QMainWindow and the
    Ui_MainWindow from the ui_mainwindow file. Also handles the actions triggered by the user in the UI.
    """
    def __init__(self, app):
        """
        Initializes MainWindow class.

        Args:
            app (QApplication): The application object, needed to handle the quit action.
        """
        super().__init__()
        # Setting up the UI
        self.setupUi(self)
        # Setting the window title
        self.setWindowTitle("Scratch pad")
        # Storing the application object for later use
        self.app = app

        # Connecting menu action signals to the slot methods
        self.actionQuit.triggered.connect(self.quit)
        self.actionCut.triggered.connect(self.cut)
        self.actionCopy.triggered.connect(self.copy)
        self.actionPaste.triggered.connect(self.paste)
        self.actionUndo.triggered.connect(self.undo)
        self.actionRedo.triggered.connect(self.redo)
        self.actionAbout.triggered.connect(self.about)
        self.actionAboutQt.triggered.connect(self.aboutqt)

    def quit(self):
        """
        Handles the action when 'Quit' is clicked in the application.
        Quits the application.
        """
        self.app.quit()

    def copy(self):
        """
        Handles the action when 'Copy' is clicked in the application.
        Copies the selected text in the textEdit widget.
        """
        self.textEdit.copy()

    def cut(self):
        """
        Handles the action when 'Cut' is clicked in the application.
        Cuts the selected text in the textEdit widget.
        """
        self.textEdit.cut()

    def paste(self):
        """
        Handles the action when 'Paste' is clicked in the application.
        Pastes the copied text into the textEdit widget at the cursor's position.
        """
        self.textEdit.paste()

    def undo(self):
        """
        Handles the action when 'Undo' is clicked in the application.
        Undoes the last text operation in the textEdit widget.
        """
        self.textEdit.undo()

    def redo(self):
        """
        Handles the action when 'Redo' is clicked in the application.
        Redoes the last text operation in the textEdit widget.
        """
        self.textEdit.redo()

    def about(self):
        """
        Handles the action when 'About' is clicked in the application.
        Shows a message box with information about the application.
        """
        QMessageBox.information(self, "Scratch pad", "Simple scratch pad using Qt Designer")

    def aboutqt(self):
        """
        Handles the action when 'About Qt' is clicked in the application.
        Shows a message box with information about the Qt framework.
        """
        QApplication.aboutQt()
