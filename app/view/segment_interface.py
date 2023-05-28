from qfluentwidgets import TextEdit, PushButton
from .gallery_interface import GalleryInterface
from ..common.translator import Translator
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtCore import Qt
from ..utils.nlp import printsegment

class SegmentInterface(GalleryInterface):
    """ Segment interface """

    def __init__(self, parent=None):
        t = Translator()
        super().__init__(
            title=t.segment,
            subtitle="The text you provide will be segment",
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

        segmentButton = PushButton(self.tr('Do segment'))
        segmentButton.clicked.connect(lambda: textEdit2.setText(printsegment(textEdit.toPlainText())))
        self.vBoxLayout.addWidget(segmentButton,0,Qt.AlignCenter)

        textEdit2.setPlaceholderText(
            "The result will be shown in here"
        )
        textEdit2.setFixedHeight(200)
        textEdit2.setDisabled(True)
        self.addExampleCard(
            widget=textEdit2,
            stretch=1
        )