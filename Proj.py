import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from Projw import Ui_MainWindow
from FileManager import FileManager
class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.fileManager = FileManager()
        self.fileType.addItem("文本文档",0)
        self.fileType.addItem("Excel表格",1)
        self.fileType.currentIndexChanged.connect(lambda: self.on_filetype_changed())

    def on_filetype_changed(self):
        self.fileManager.set_file_type(self.fileType.currentIndex())
        suffix = self.fileManager.get_file_suffix()
        print(suffix)
        self.suffixLabel.setText(suffix)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())