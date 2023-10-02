# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
    QLineEdit, QProgressBar, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import rc_resources

class Ui_Window(object):
    def setupUi(self, Window):
        if not Window.objectName():
            Window.setObjectName(u"Window")
        Window.resize(490, 200)
        Window.setMaximumSize(QSize(16777215, 200))
        icon = QIcon()
        icon.addFile(u":/icons/icons/ytd.ico", QSize(), QIcon.Normal, QIcon.Off)
        Window.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(Window)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Window)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(Window)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.lineEditURL = QLineEdit(Window)
        self.lineEditURL.setObjectName(u"lineEditURL")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEditURL)

        self.label_3 = QLabel(Window)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEditDir = QLineEdit(Window)
        self.lineEditDir.setObjectName(u"lineEditDir")
        self.lineEditDir.setReadOnly(True)

        self.horizontalLayout.addWidget(self.lineEditDir)

        self.pushButtonBrowse = QPushButton(Window)
        self.pushButtonBrowse.setObjectName(u"pushButtonBrowse")

        self.horizontalLayout.addWidget(self.pushButtonBrowse)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout)


        self.verticalLayout.addLayout(self.formLayout)

        self.progressBar = QProgressBar(Window)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.verticalLayout.addWidget(self.progressBar)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButtonDownloadVideo = QPushButton(Window)
        self.pushButtonDownloadVideo.setObjectName(u"pushButtonDownloadVideo")

        self.horizontalLayout_2.addWidget(self.pushButtonDownloadVideo)

        self.pushButtonDownloadAudio = QPushButton(Window)
        self.pushButtonDownloadAudio.setObjectName(u"pushButtonDownloadAudio")

        self.horizontalLayout_2.addWidget(self.pushButtonDownloadAudio)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Window)

        QMetaObject.connectSlotsByName(Window)
    # setupUi

    def retranslateUi(self, Window):
        Window.setWindowTitle(QCoreApplication.translate("Window", u"YouTube Downloader - By Filipe C. F.", None))
        self.label.setText(QCoreApplication.translate("Window", u"YouTube Downloader", None))
        self.label_2.setText(QCoreApplication.translate("Window", u"Video URL", None))
        self.label_3.setText(QCoreApplication.translate("Window", u"Output Folder", None))
        self.lineEditDir.setText(QCoreApplication.translate("Window", u".", None))
        self.pushButtonBrowse.setText(QCoreApplication.translate("Window", u"Browse", None))
        self.pushButtonDownloadVideo.setText(QCoreApplication.translate("Window", u"Download Video", None))
        self.pushButtonDownloadAudio.setText(QCoreApplication.translate("Window", u"Download Audio", None))
    # retranslateUi

