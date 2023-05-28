from qfluentwidgets import TextEdit, PushButton
from .gallery_interface import GalleryInterface
from ..common.translator import Translator
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtCore import Qt
from ..utils.nlp import print_clean_stopword

class StopWordInterface(GalleryInterface):
    """ Stop word interface """

    def __init__(self, parent=None):
        t = Translator()
        super().__init__(
            title=t.stopword,
            subtitle="The text you provide will be removed the stop word",
            parent=parent
        )

        # text receiver
        textEdit = TextEdit(self)
        textEdit2 = TextEdit(self)
        textEdit.setPlaceholderText(
            "Please input the text to be processed"
        )
        textEdit.setFixedHeight(200)
        self.addExampleCard(
            widget=textEdit,
            stretch=1
        )

        stopwordButton = PushButton(self.tr('Remove the stop word'))
        stopwordButton.clicked.connect(lambda: textEdit2.setText(print_clean_stopword(textEdit.toPlainText())))
        self.vBoxLayout.addWidget(stopwordButton,0,Qt.AlignCenter)

        textEdit2.setPlaceholderText(
            "The result will be shown in here"
        )
        textEdit2.setFixedHeight(200)
        textEdit2.setDisabled(True)
        self.addExampleCard(
            widget=textEdit2,
            stretch=1
        )