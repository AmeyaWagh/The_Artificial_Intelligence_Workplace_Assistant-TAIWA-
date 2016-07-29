# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sample.ui'
#
# Created: Sun Feb 21 19:19:03 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

def extract_text(filepath):
    fp = open(filepath)
    _myText = fp.readlines()
    myText = ''.join( Text for Text in _myText)
    count = sum(1 for line in _myText)
    max_len = max(len(line) for line in _myText)
    return myText , count , max_len

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form, Title,Text,no_of_lines,max_len):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(500+max_len, no_of_lines*15+100)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(110, 10, 192, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(70,70, 400+max_len, no_of_lines*15+20))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(Form,Title,Text)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form,Title,Text):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", Title, None))
        self.label_2.setText(_translate("Form", Text, None))


if __name__ == "__main__":
    import sys
    mytext,count,max_len = extract_text('textnote.txt')
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form,"Project TAIWA",mytext,count,max_len)
    Form.show()
    sys.exit(app.exec_())
    

