# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sticky notes.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Defaults.UI_Defaults import *


class stickyNotesUI(object):

    def __init__(self):
        self.MainWindow_Dialog = QtWidgets.QMainWindow()
        self.setupUi(self.MainWindow_Dialog)
        self.MainWindow_Dialog.setGeometry(0, 50, 500, 1032)


    def setupUi(self, MainWindow):
        MainWindow.setObjectName(DFLT_MAINWINDOW_OBJ_NAME)
        MainWindow.resize(500, 1032)
        MainWindow.setMinimumSize(QtCore.QSize(500, 125))
        MainWindow.setMaximumSize(QtCore.QSize(500, 1032))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(MAINWINDOW_DFLT_STYLESHEET)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName(DFLT_CENTRALWIDGET_OBJ_NAME)

        #Definition for all font labels
        self.label_font = QtGui.QFont("OCR A Extended", italic = True)
        self.label_font.setPointSize(11)

        #Definition for lblNote_1
        self.lblNote_1 = QtWidgets.QLabel(self.centralwidget)
        self.lblNote_1.setEnabled(True)
        self.lblNote_1.setFont(self.label_font)
        self.lblNote_1.setGeometry(QtCore.QRect(0, 0, 489, 33))
        self.lblNote_1.setMaximumSize(QtCore.QSize(500, 33))
        self.lblNote_1.setObjectName(DFLT_LBLNOTE_1_OBJ_NAME)
        self.lblNote_1.setStyleSheet(LBLNOTE_1_DFLT_STYLESHEET)
        self.lblNote_1.setTextFormat(QtCore.Qt.AutoText)

        #Definition for lblNote_2
        self.lblNote_2 = QtWidgets.QLabel(self.centralwidget)
        self.lblNote_2.setEnabled(True)
        self.lblNote_2.setFont(self.label_font)
        self.lblNote_2.setGeometry(QtCore.QRect(0, 33, 489, 33))
        self.lblNote_2.setMaximumSize(QtCore.QSize(500, 33))
        self.lblNote_2.setObjectName(DFLT_LBLNOTE_2_OBJ_NAME)
        self.lblNote_2.setStyleSheet(LBLNOTE_2_DFLT_STYLESHEET)
        self.lblNote_2.setTextFormat(QtCore.Qt.AutoText)

        #Definition for lblNote_3
        self.lblNote_3 = QtWidgets.QLabel(self.centralwidget)
        self.lblNote_3.setEnabled(True)
        self.lblNote_3.setFont(self.label_font)
        self.lblNote_3.setGeometry(QtCore.QRect(0, 66, 489, 32))
        self.lblNote_3.setMaximumSize(QtCore.QSize(500, 33))
        self.lblNote_3.setObjectName(DFLT_LBLNOTE_3_OBJ_NAME)
        self.lblNote_3.setStyleSheet(LBLNOTE_3_DFLT_STYLESHEET)
        self.lblNote_3.setTextFormat(QtCore.Qt.AutoText)

        #Definition for lblNote_4
        self.lblNote_4 = QtWidgets.QLabel(self.centralwidget)
        self.lblNote_4.setEnabled(True)
        self.lblNote_4.setFont(self.label_font)
        self.lblNote_4.setGeometry(QtCore.QRect(0, 98, 489, 33))
        self.lblNote_4.setMaximumSize(QtCore.QSize(500, 33))
        self.lblNote_4.setObjectName(DFLT_LBLNOTE_4_OBJ_NAME)
        self.lblNote_4.setStyleSheet(LBLNOTE_4_DFLT_STYLESHEET)
        self.lblNote_4.setTextFormat(QtCore.Qt.AutoText)

        #Definition for lblNote_5
        self.lblNote_5 = QtWidgets.QLabel(self.centralwidget)
        self.lblNote_5.setEnabled(True)
        self.lblNote_5.setFont(self.label_font)
        self.lblNote_5.setGeometry(QtCore.QRect(0, 131, 489, 33))
        self.lblNote_5.setMaximumSize(QtCore.QSize(500, 33))
        self.lblNote_5.setObjectName(DFLT_LBLNOTE_5_OBJ_NAME)
        self.lblNote_5.setStyleSheet(LBLNOTE_5_DFLT_STYLESHEET)
        self.lblNote_5.setTextFormat(QtCore.Qt.AutoText)

        #Definition for lblNote_6
        self.lblNote_6 = QtWidgets.QLabel(self.centralwidget)
        self.lblNote_6.setEnabled(True)
        self.lblNote_6.setFont(self.label_font)
        self.lblNote_6.setGeometry(QtCore.QRect(0, 164, 489, 33))
        self.lblNote_6.setMaximumSize(QtCore.QSize(500, 33))
        self.lblNote_6.setObjectName(DFLT_LBLNOTE_6_OBJ_NAME)
        self.lblNote_6.setStyleSheet(LBLNOTE_6_DFLT_STYLESHEET)
        self.lblNote_6.setTextFormat(QtCore.Qt.AutoText)

        #Definition for lblNote_7
        self.lblNote_7 = QtWidgets.QLabel(self.centralwidget)
        self.lblNote_7.setEnabled(True)
        self.lblNote_7.setFont(self.label_font)
        self.lblNote_7.setGeometry(QtCore.QRect(0, 197, 489, 33))
        self.lblNote_7.setMaximumSize(QtCore.QSize(500, 33))
        self.lblNote_7.setObjectName(DFLT_LBLNOTE_7_OBJ_NAME)
        self.lblNote_7.setStyleSheet(LBLNOTE_7_DFLT_STYLESHEET)
        self.lblNote_7.setTextFormat(QtCore.Qt.AutoText)

        #Definition for lblNote_8
        self.lblNote_8 = QtWidgets.QLabel(self.centralwidget)
        self.lblNote_8.setEnabled(True)
        self.lblNote_8.setFont(self.label_font)
        self.lblNote_8.setGeometry(QtCore.QRect(0, 230, 489, 33))
        self.lblNote_8.setMaximumSize(QtCore.QSize(500, 33))
        self.lblNote_8.setObjectName(DFLT_LBLNOTE_8_OBJ_NAME)
        self.lblNote_8.setStyleSheet(LBLNOTE_8_DFLT_STYLESHEET)
        self.lblNote_8.setTextFormat(QtCore.Qt.AutoText)

        #Definition for lblNote_9
        self.lblNote_9 = QtWidgets.QLabel(self.centralwidget)
        self.lblNote_9.setEnabled(True)
        self.lblNote_9.setFont(self.label_font)
        self.lblNote_9.setGeometry(QtCore.QRect(0, 263, 489, 32))
        self.lblNote_9.setMaximumSize(QtCore.QSize(500, 33))
        self.lblNote_9.setObjectName(DFLT_LBLNOTE_9_OBJ_NAME)
        self.lblNote_9.setStyleSheet(LBLNOTE_9_DFLT_STYLESHEET)
        self.lblNote_9.setTextFormat(QtCore.Qt.AutoText)

        #Definition for lblNote__10
        self.lblNote__10 = QtWidgets.QLabel(self.centralwidget)
        self.lblNote__10.setEnabled(True)
        self.lblNote__10.setFont(self.label_font)
        self.lblNote__10.setGeometry(QtCore.QRect(0, 295, 489, 33))
        self.lblNote__10.setMaximumSize(QtCore.QSize(500, 33))
        self.lblNote__10.setObjectName(DFLT_LBLNOTE__10_OBJ_NAME)
        self.lblNote__10.setStyleSheet(LBLNOTE__10_DFLT_STYLESHEET)
        self.lblNote__10.setTextFormat(QtCore.Qt.AutoText)

        #Definition for lblNote__11
        self.lblNote__11 = QtWidgets.QLabel(self.centralwidget)
        self.lblNote__11.setEnabled(True)
        self.lblNote__11.setFont(self.label_font)
        self.lblNote__11.setGeometry(QtCore.QRect(0, 328, 489, 33))
        self.lblNote__11.setMaximumSize(QtCore.QSize(500, 33))
        self.lblNote__11.setObjectName(DFLT_LBLNOTE__11_OBJ_NAME)
        self.lblNote__11.setStyleSheet(LBLNOTE__11_DFLT_STYLESHEET)
        self.lblNote__11.setTextFormat(QtCore.Qt.AutoText)

        #Definition for lblNote__12
        self.lblNote__12 = QtWidgets.QLabel(self.centralwidget)
        self.lblNote__12.setEnabled(True)
        self.lblNote__12.setFont(self.label_font)
        self.lblNote__12.setGeometry(QtCore.QRect(0, 361, 489, 33))
        self.lblNote__12.setMaximumSize(QtCore.QSize(500, 33))
        self.lblNote__12.setObjectName(DFLT_LBLNOTE__12_OBJ_NAME)
        self.lblNote__12.setStyleSheet(LBLNOTE__12_DFLT_STYLESHEET)
        self.lblNote__12.setTextFormat(QtCore.Qt.AutoText)

        #Definition for lblNote__13
        self.lblNote__13 = QtWidgets.QLabel(self.centralwidget)
        self.lblNote__13.setEnabled(True)
        self.lblNote__13.setFont(self.label_font)
        self.lblNote__13.setGeometry(QtCore.QRect(0, 394, 489, 33))
        self.lblNote__13.setMaximumSize(QtCore.QSize(500, 33))
        self.lblNote__13.setObjectName(DFLT_LBLNOTE__13_OBJ_NAME)
        self.lblNote__13.setStyleSheet(LBLNOTE__13_DFLT_STYLESHEET)
        self.lblNote__13.setTextFormat(QtCore.Qt.AutoText)

        #Definition for lblNote__14
        self.lblNote__14 = QtWidgets.QLabel(self.centralwidget)
        self.lblNote__14.setEnabled(True)
        self.lblNote__14.setFont(self.label_font)
        self.lblNote__14.setGeometry(QtCore.QRect(0, 427, 489, 33))
        self.lblNote__14.setMaximumSize(QtCore.QSize(500, 33))
        self.lblNote__14.setObjectName(DFLT_LBLNOTE__14_OBJ_NAME)
        self.lblNote__14.setStyleSheet(LBLNOTE__14_DFLT_STYLESHEET)
        self.lblNote__14.setTextFormat(QtCore.Qt.AutoText)

        #Definition for lblNote__15
        self.lblNote__15 = QtWidgets.QLabel(self.centralwidget)
        self.lblNote__15.setEnabled(True)
        self.lblNote__15.setFont(self.label_font)
        self.lblNote__15.setGeometry(QtCore.QRect(0, 460, 489, 32))
        self.lblNote__15.setMaximumSize(QtCore.QSize(500, 33))
        self.lblNote__15.setObjectName(DFLT_LBLNOTE__15_OBJ_NAME)
        self.lblNote__15.setStyleSheet(LBLNOTE__15_DFLT_STYLESHEET)
        self.lblNote__15.setTextFormat(QtCore.Qt.AutoText)

        #Definition for lblNote__16
        self.lblNote__16 = QtWidgets.QLabel(self.centralwidget)
        self.lblNote__16.setEnabled(True)
        self.lblNote__16.setFont(self.label_font)
        self.lblNote__16.setGeometry(QtCore.QRect(0, 492, 489, 33))
        self.lblNote__16.setMaximumSize(QtCore.QSize(500, 33))
        self.lblNote__16.setObjectName(DFLT_LBLNOTE__16_OBJ_NAME)
        self.lblNote__16.setStyleSheet(LBLNOTE__16_DFLT_STYLESHEET)
        self.lblNote__16.setTextFormat(QtCore.Qt.AutoText)

        #Definition for lblNote__17
        self.lblNote__17 = QtWidgets.QLabel(self.centralwidget)
        self.lblNote__17.setEnabled(True)
        self.lblNote__17.setFont(self.label_font)
        self.lblNote__17.setGeometry(QtCore.QRect(0, 525, 489, 33))
        self.lblNote__17.setMaximumSize(QtCore.QSize(500, 33))
        self.lblNote__17.setObjectName(DFLT_LBLNOTE__17_OBJ_NAME)
        self.lblNote__17.setStyleSheet(LBLNOTE__17_DFLT_STYLESHEET)
        self.lblNote__17.setTextFormat(QtCore.Qt.AutoText)

        #Definition for lblNote__18
        self.lblNote__18 = QtWidgets.QLabel(self.centralwidget)
        self.lblNote__18.setEnabled(True)
        self.lblNote__18.setFont(self.label_font)
        self.lblNote__18.setGeometry(QtCore.QRect(0, 558, 489, 33))
        self.lblNote__18.setMaximumSize(QtCore.QSize(500, 33))
        self.lblNote__18.setObjectName(DFLT_LBLNOTE__18_OBJ_NAME)
        self.lblNote__18.setStyleSheet(LBLNOTE__18_DFLT_STYLESHEET)
        self.lblNote__18.setTextFormat(QtCore.Qt.AutoText)

        #Definition for lblNote__19
        self.lblNote__19 = QtWidgets.QLabel(self.centralwidget)
        self.lblNote__19.setEnabled(True)
        self.lblNote__19.setFont(self.label_font)
        self.lblNote__19.setGeometry(QtCore.QRect(0, 591, 489, 33))
        self.lblNote__19.setMaximumSize(QtCore.QSize(500, 33))
        self.lblNote__19.setObjectName(DFLT_LBLNOTE__19_OBJ_NAME)
        self.lblNote__19.setStyleSheet(LBLNOTE__19_DFLT_STYLESHEET)
        self.lblNote__19.setTextFormat(QtCore.Qt.AutoText)

        #Definition for lblNote__20
        self.lblNote__20 = QtWidgets.QLabel(self.centralwidget)
        self.lblNote__20.setEnabled(True)
        self.lblNote__20.setFont(self.label_font)
        self.lblNote__20.setGeometry(QtCore.QRect(0, 624, 489, 33))
        self.lblNote__20.setMaximumSize(QtCore.QSize(500, 33))
        self.lblNote__20.setObjectName(DFLT_LBLNOTE__20_OBJ_NAME)
        self.lblNote__20.setStyleSheet(LBLNOTE__20_DFLT_STYLESHEET)
        self.lblNote__20.setTextFormat(QtCore.Qt.AutoText)

        #Definition for lblNote__21
        self.lblNote__21 = QtWidgets.QLabel(self.centralwidget)
        self.lblNote__21.setEnabled(True)
        self.lblNote__21.setFont(self.label_font)
        self.lblNote__21.setGeometry(QtCore.QRect(0, 657, 489, 32))
        self.lblNote__21.setMaximumSize(QtCore.QSize(500, 33))
        self.lblNote__21.setObjectName(DFLT_LBLNOTE__21_OBJ_NAME)
        self.lblNote__21.setStyleSheet(LBLNOTE__21_DFLT_STYLESHEET)
        self.lblNote__21.setTextFormat(QtCore.Qt.AutoText)

        #Definition for lblNote__22
        self.lblNote__22 = QtWidgets.QLabel(self.centralwidget)
        self.lblNote__22.setEnabled(True)
        self.lblNote__22.setFont(self.label_font)
        self.lblNote__22.setGeometry(QtCore.QRect(0, 689, 489, 33))
        self.lblNote__22.setMaximumSize(QtCore.QSize(500, 33))
        self.lblNote__22.setObjectName(DFLT_LBLNOTE__22_OBJ_NAME)
        self.lblNote__22.setStyleSheet(LBLNOTE__22_DFLT_STYLESHEET)
        self.lblNote__22.setTextFormat(QtCore.Qt.AutoText)

        #Definition for lblNote__23
        self.lblNote__23 = QtWidgets.QLabel(self.centralwidget)
        self.lblNote__23.setEnabled(True)
        self.lblNote__23.setFont(self.label_font)
        self.lblNote__23.setGeometry(QtCore.QRect(0, 722, 489, 33))
        self.lblNote__23.setMaximumSize(QtCore.QSize(500, 33))
        self.lblNote__23.setObjectName(DFLT_LBLNOTE__23_OBJ_NAME)
        self.lblNote__23.setStyleSheet(LBLNOTE__23_DFLT_STYLESHEET)
        self.lblNote__23.setTextFormat(QtCore.Qt.AutoText)

        #Definition for lblNote__24
        self.lblNote__24 = QtWidgets.QLabel(self.centralwidget)
        self.lblNote__24.setEnabled(True)
        self.lblNote__24.setFont(self.label_font)
        self.lblNote__24.setGeometry(QtCore.QRect(0, 755, 489, 33))
        self.lblNote__24.setMaximumSize(QtCore.QSize(500, 33))
        self.lblNote__24.setObjectName(DFLT_LBLNOTE__24_OBJ_NAME)
        self.lblNote__24.setStyleSheet(LBLNOTE__24_DFLT_STYLESHEET)
        self.lblNote__24.setTextFormat(QtCore.Qt.AutoText)

        #Definition for lblNote__25
        self.lblNote__25 = QtWidgets.QLabel(self.centralwidget)
        self.lblNote__25.setEnabled(True)
        self.lblNote__25.setFont(self.label_font)
        self.lblNote__25.setGeometry(QtCore.QRect(0, 788, 489, 33))
        self.lblNote__25.setMaximumSize(QtCore.QSize(500, 33))
        self.lblNote__25.setObjectName(DFLT_LBLNOTE__25_OBJ_NAME)
        self.lblNote__25.setStyleSheet(LBLNOTE__25_DFLT_STYLESHEET)
        self.lblNote__25.setTextFormat(QtCore.Qt.AutoText)

        #Definition for lblNote__26
        self.lblNote__26 = QtWidgets.QLabel(self.centralwidget)
        self.lblNote__26.setEnabled(True)
        self.lblNote__26.setFont(self.label_font)
        self.lblNote__26.setGeometry(QtCore.QRect(0, 821, 489, 33))
        self.lblNote__26.setMaximumSize(QtCore.QSize(500, 33))
        self.lblNote__26.setObjectName(DFLT_LBLNOTE__26_OBJ_NAME)
        self.lblNote__26.setStyleSheet(LBLNOTE__26_DFLT_STYLESHEET)
        self.lblNote__26.setTextFormat(QtCore.Qt.AutoText)

        #Definition for lblNote__27
        self.lblNote__27 = QtWidgets.QLabel(self.centralwidget)
        self.lblNote__27.setEnabled(True)
        self.lblNote__27.setFont(self.label_font)
        self.lblNote__27.setGeometry(QtCore.QRect(0, 854, 489, 32))
        self.lblNote__27.setMaximumSize(QtCore.QSize(500, 33))
        self.lblNote__27.setObjectName(DFLT_LBLNOTE__27_OBJ_NAME)
        self.lblNote__27.setStyleSheet(LBLNOTE__27_DFLT_STYLESHEET)
        self.lblNote__27.setTextFormat(QtCore.Qt.AutoText)

        #Definition for lblNote__28
        self.lblNote__28 = QtWidgets.QLabel(self.centralwidget)
        self.lblNote__28.setEnabled(True)
        self.lblNote__28.setFont(self.label_font)
        self.lblNote__28.setGeometry(QtCore.QRect(0, 886, 489, 33))
        self.lblNote__28.setMaximumSize(QtCore.QSize(500, 33))
        self.lblNote__28.setObjectName(DFLT_LBLNOTE__28_OBJ_NAME)
        self.lblNote__28.setStyleSheet(LBLNOTE__28_DFLT_STYLESHEET)
        self.lblNote__28.setTextFormat(QtCore.Qt.AutoText)

        #Definition for lblNote__29
        self.lblNote__29 = QtWidgets.QLabel(self.centralwidget)
        self.lblNote__29.setEnabled(True)
        self.lblNote__29.setFont(self.label_font)
        self.lblNote__29.setGeometry(QtCore.QRect(0, 919, 489, 33))
        self.lblNote__29.setMaximumSize(QtCore.QSize(500, 33))
        self.lblNote__29.setObjectName(DFLT_LBLNOTE__29_OBJ_NAME)
        self.lblNote__29.setStyleSheet(LBLNOTE__29_DFLT_STYLESHEET)
        self.lblNote__29.setTextFormat(QtCore.Qt.AutoText)

        #Definition for lblNote__30
        self.lblNote__30 = QtWidgets.QLabel(self.centralwidget)
        self.lblNote__30.setEnabled(True)
        self.lblNote__30.setFont(self.label_font)
        self.lblNote__30.setGeometry(QtCore.QRect(0, 952, 489, 33))
        self.lblNote__30.setMaximumSize(QtCore.QSize(500, 33))
        self.lblNote__30.setObjectName(DFLT_LBLNOTE__30_OBJ_NAME)
        self.lblNote__30.setStyleSheet(LBLNOTE__30_DFLT_STYLESHEET)
        self.lblNote__30.setTextFormat(QtCore.Qt.AutoText)

        #Definition for pshBtnAdd
        self.pshBtnAdd = QtWidgets.QPushButton(self.centralwidget)
        self.pshBtnAdd.setGeometry(QtCore.QRect(450, 990, 51, 40))
        self.pshBtnAdd.setStyleSheet(PSHBTNADD_DFLT_STYLESHEET)
        self.pshBtnAdd.setAutoDefault(False)
        self.pshBtnAdd.setDefault(False)
        self.pshBtnAdd.setFlat(True)
        self.pshBtnAdd.setObjectName(DFLT_PSHBTNADD_OBJ_NAME)

        #Definition for pshBtnViewHTML
        self.pshBtnViewHTML = QtWidgets.QPushButton(self.centralwidget)
        self.pshBtnViewHTML.setGeometry(QtCore.QRect(400, 990, 51, 40))
        self.pshBtnViewHTML.setStyleSheet(PSHBTNVIEWHTML_DFLT_STYLESHEET)
        self.pshBtnViewHTML.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/convert_to_HTML_Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pshBtnViewHTML.setIcon(icon)
        self.pshBtnViewHTML.setIconSize(QtCore.QSize(40, 40))
        self.pshBtnViewHTML.setCheckable(True)
        self.pshBtnViewHTML.setAutoDefault(False)
        self.pshBtnViewHTML.setDefault(False)
        self.pshBtnViewHTML.setFlat(True)
        self.pshBtnViewHTML.setObjectName(DFLT_PSHBTNVIEWHTML_OBJ_NAME)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sticky Notes"))
        self.lblNote_1.setText(_translate("MainWindow", DFLT_LABEL_TEXT))
        self.lblNote_2.setText(_translate("MainWindow", DFLT_LABEL_TEXT))
        self.lblNote_3.setText(_translate("MainWindow", DFLT_LABEL_TEXT))
        self.lblNote_4.setText(_translate("MainWindow", DFLT_LABEL_TEXT))
        self.lblNote_5.setText(_translate("MainWindow", DFLT_LABEL_TEXT))
        self.lblNote_6.setText(_translate("MainWindow", DFLT_LABEL_TEXT))
        self.lblNote_7.setText(_translate("MainWindow", DFLT_LABEL_TEXT))
        self.lblNote_8.setText(_translate("MainWindow", DFLT_LABEL_TEXT))
        self.lblNote_9.setText(_translate("MainWindow", DFLT_LABEL_TEXT))
        self.lblNote__10.setText(_translate("MainWindow", DFLT_LABEL_TEXT))
        self.lblNote__11.setText(_translate("MainWindow", DFLT_LABEL_TEXT))
        self.lblNote__12.setText(_translate("MainWindow", DFLT_LABEL_TEXT))
        self.lblNote__13.setText(_translate("MainWindow", DFLT_LABEL_TEXT))
        self.lblNote__14.setText(_translate("MainWindow", DFLT_LABEL_TEXT))
        self.lblNote__15.setText(_translate("MainWindow", DFLT_LABEL_TEXT))
        self.lblNote__16.setText(_translate("MainWindow", DFLT_LABEL_TEXT))
        self.lblNote__17.setText(_translate("MainWindow", DFLT_LABEL_TEXT))
        self.lblNote__18.setText(_translate("MainWindow", DFLT_LABEL_TEXT))
        self.lblNote__19.setText(_translate("MainWindow", DFLT_LABEL_TEXT))
        self.lblNote__20.setText(_translate("MainWindow", DFLT_LABEL_TEXT))
        self.lblNote__21.setText(_translate("MainWindow", DFLT_LABEL_TEXT))
        self.lblNote__22.setText(_translate("MainWindow", DFLT_LABEL_TEXT))
        self.lblNote__23.setText(_translate("MainWindow", DFLT_LABEL_TEXT))
        self.lblNote__24.setText(_translate("MainWindow", DFLT_LABEL_TEXT))
        self.lblNote__25.setText(_translate("MainWindow", DFLT_LABEL_TEXT))
        self.lblNote__26.setText(_translate("MainWindow", DFLT_LABEL_TEXT))
        self.lblNote__27.setText(_translate("MainWindow", DFLT_LABEL_TEXT))
        self.lblNote__28.setText(_translate("MainWindow", DFLT_LABEL_TEXT))
        self.lblNote__29.setText(_translate("MainWindow", DFLT_LABEL_TEXT))
        self.lblNote__30.setText(_translate("MainWindow", DFLT_LABEL_TEXT))
        self.pshBtnAdd.setText(_translate("MainWindow", "+"))


    @property
    def notesLabelsLst(self):
        """
        This is the list of all the possible note labels, and this is what's used when working with the notes
        """
        self._notesLst = [
            self.lblNote_1,
            self.lblNote_2,
            self.lblNote_3,
            self.lblNote_4,
            self.lblNote_5,
            self.lblNote_6,
            self.lblNote_7,
            self.lblNote_8,
            self.lblNote_9,
            self.lblNote__10,
            self.lblNote__11,
            self.lblNote__12,
            self.lblNote__13,
            self.lblNote__14,
            self.lblNote__15,
            self.lblNote__16,
            self.lblNote__17,
            self.lblNote__18,
            self.lblNote__19,
            self.lblNote__20,
            self.lblNote__21,
            self.lblNote__22,
            self.lblNote__23,
            self.lblNote__24,
            self.lblNote__25,
            self.lblNote__26,
            self.lblNote__27,
            self.lblNote__28,
            self.lblNote__29,
            self.lblNote__30
            ]
        return self._notesLst


    @property
    def MAX_LABEL_COUNT(self):
        """
        <Insert Documentation>
        """
        return 30


    def show(self):
        self.MainWindow_Dialog.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ex = stickyNotesUI()
    ex.show()
    sys.exit()
    sys.exit(app.exec_())
