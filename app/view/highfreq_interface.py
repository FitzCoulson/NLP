from qfluentwidgets import TextEdit, PushButton,TableWidget
from .gallery_interface import GalleryInterface
from ..common.translator import Translator
from PyQt5.QtWidgets import QHBoxLayout,QTableWidgetItem
from PyQt5.QtCore import Qt
from ..utils.nlp import print_high_freq

class HighFrequencyInterface(GalleryInterface):
    """ Stop word interface """

    def __init__(self, parent=None):
        t = Translator()
        super().__init__(
            title=t.highfrequency,
            subtitle="The text you provide will be extracted high frequency words",
            parent=parent
        )

        # text receiver
        textEdit = TextEdit(self)

        table = TableWidget(self)
        tablecontent=[]
        textEdit.setPlaceholderText(
            "Please input the text to be processed"
        )
        textEdit.setFixedHeight(200)
        self.addExampleCard(
            widget=textEdit,
            stretch=1
        )

        highferqButton = PushButton(self.tr('Extract High Frequency Words'))
        highferqButton.clicked.connect(lambda: showresult(tablecontent))
        self.vBoxLayout.addWidget(highferqButton,0,Qt.AlignCenter)

        table.verticalHeader().hide()
        table.setColumnCount(2)
        table.setRowCount(5)
        table.setHorizontalHeaderLabels(
            [self.tr('High Frequency Word'),self.tr('Count')]
        )
        table.resizeColumnsToContents()
        table.setFixedSize(220,200)
        self.addExampleCard(
            table,
            stretch=1
        )

        def showresult(tablecontent):
            _,dict=print_high_freq(textEdit.toPlainText())
            content=[]
            for k,v in dict:
                content.append([k,v])
            tablecontent+=content
            for i, word in enumerate(tablecontent):
                for j in range(2):
                    table.setItem(i, j, QTableWidgetItem(str(word[j])))

