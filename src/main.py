# Author: Filipe Chagas Ferraz
# Date: 02-10-2023
# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
from qt_material import apply_stylesheet
from pytube import YouTube
from moviepy.editor import *
import os

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_window import Ui_Window

def msgbox(title: str, msg: str, description: str = None):
    """
    Display a message box
    """
    msgBox = QMessageBox()
    msgBox.setWindowTitle(title)
    msgBox.setText(msg)
    if description is not None:
        msgBox.setInformativeText(description)
    msgBox.exec()

class Window(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Window()
        self.ui.setupUi(self)

        #Set the 'Downloads' directory as default output directory
        self.ui.lineEditDir.setText(os.path.join(os.path.expanduser('~'), 'Downloads'))

        #Connections
        self.ui.pushButtonDownloadVideo.clicked.connect(self._download_video_clicked)
        self.ui.pushButtonDownloadAudio.clicked.connect(self._download_audio_clicked)
        self.ui.pushButtonBrowse.clicked.connect(self._browse_clicked)

    def _browse_clicked(self):
        self.ui.lineEditDir.setText(QFileDialog.getExistingDirectory())

    def _download_video_clicked(self):
        def progress(stream, chunk, bytes_remaining):
            #Update progress bar
            size = stream.filesize
            p = int((float(size-bytes_remaining)/float(size))*100)
            self.ui.progressBar.setValue(p)

        try:
            #Download video
            youtubeObject = YouTube(self.ui.lineEditURL.text(), on_progress_callback=progress)
            youtubeObject = youtubeObject.streams.get_highest_resolution()
            youtubeObject.download(output_path=self.ui.lineEditDir.text())

            msgbox('Success!', 'Download is completed successfully')
            self.close()
        except Exception as ex:
            msgbox('Error', str(ex))
            self.ui.progressBar.setValue(0)

    def _download_audio_clicked(self):
        def progress(stream, chunk, bytes_remaining):
            #Update progress bar
            size = stream.filesize
            p = int((float(size-bytes_remaining)/float(size))*100)
            self.ui.progressBar.setValue(p)

        try:
            #Download Video
            youtubeObject = YouTube(self.ui.lineEditURL.text(), on_progress_callback=progress)
            youtubeObject = youtubeObject.streams.get_highest_resolution()
            outfile = youtubeObject.download(output_path=self.ui.lineEditDir.text())

            #Convert to MP3
            video = VideoFileClip(outfile)
            video.audio.write_audiofile(outfile.split('.')[0] + '.mp3')

            msgbox('Success!', 'Download is completed successfully')
            self.close()
        except Exception as ex:
            msgbox('Error', str(ex))
            self.ui.progressBar.setValue(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_purple.xml')
    window = Window()
    window.show()
    sys.exit(app.exec())
