# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(621, 351)
        MainWindow.setMinimumSize(QtCore.QSize(621, 351))
        MainWindow.setMaximumSize(QtCore.QSize(621, 351))
        MainWindow.setStyleSheet("border-top-color: rgb(97, 179, 255);\n"
"background-color: rgb(49, 49, 49);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("border-top-color: rgb(97, 179, 255);\n"
"background-color: rgb(49, 49, 49);")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(60, 20, 91, 31))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.inicial = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setItalic(False)
        self.inicial.setFont(font)
        self.inicial.setStyleSheet("\n"
"color: rgb(1, 255, 1);")
        self.inicial.setDecimals(1)
        self.inicial.setMaximum(100000.0)
        self.inicial.setSingleStep(1.0)
        self.inicial.setObjectName("inicial")
        self.horizontalLayout_6.addWidget(self.inicial, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(20, 20, 41, 31))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setKerning(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2, 0, QtCore.Qt.AlignRight)
        self.horizontalLayoutWidget_8 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(20, 80, 41, 31))
        self.horizontalLayoutWidget_8.setObjectName("horizontalLayoutWidget_8")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setKerning(False)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_9.addWidget(self.label_3, 0, QtCore.Qt.AlignRight)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(480, 20, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.verticalLayoutWidget_2.setFont(font)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Calcular = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Calcular.sizePolicy().hasHeightForWidth())
        self.Calcular.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setKerning(False)
        self.Calcular.setFont(font)
        self.Calcular.setStyleSheet("background-color: rgb(0, 85, 255);")
        self.Calcular.setObjectName("Calcular")
        self.verticalLayout_2.addWidget(self.Calcular)
        self.horizontalLayoutWidget_11 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_11.setGeometry(QtCore.QRect(20, 50, 41, 31))
        self.horizontalLayoutWidget_11.setObjectName("horizontalLayoutWidget_11")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_11)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_11)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setKerning(False)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_12.addWidget(self.label_5, 0, QtCore.Qt.AlignRight)
        self.horizontalLayoutWidget_12 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_12.setGeometry(QtCore.QRect(20, 170, 41, 31))
        self.horizontalLayoutWidget_12.setObjectName("horizontalLayoutWidget_12")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_12)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_12)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setKerning(False)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_13.addWidget(self.label_6, 0, QtCore.Qt.AlignRight)
        self.horizontalLayoutWidget_9 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_9.setGeometry(QtCore.QRect(60, 80, 91, 31))
        self.horizontalLayoutWidget_9.setObjectName("horizontalLayoutWidget_9")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.volumen = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget_9)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setItalic(False)
        self.volumen.setFont(font)
        self.volumen.setStyleSheet("\n"
"color: rgb(1, 255, 1);")
        self.volumen.setDecimals(1)
        self.volumen.setMaximum(100000.0)
        self.volumen.setSingleStep(1000000.0)
        self.volumen.setObjectName("volumen")
        self.horizontalLayout_10.addWidget(self.volumen, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayoutWidget_10 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_10.setGeometry(QtCore.QRect(60, 50, 91, 31))
        self.horizontalLayoutWidget_10.setObjectName("horizontalLayoutWidget_10")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_10)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.ingreso = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget_10)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setItalic(False)
        self.ingreso.setFont(font)
        self.ingreso.setStyleSheet("\n"
"color: rgb(1, 255, 1);")
        self.ingreso.setDecimals(1)
        self.ingreso.setMaximum(100000.0)
        self.ingreso.setObjectName("ingreso")
        self.horizontalLayout_11.addWidget(self.ingreso, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(60, 110, 91, 31))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.caudal = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setItalic(False)
        self.caudal.setFont(font)
        self.caudal.setStyleSheet("\n"
"color: rgb(1, 255, 1);")
        self.caudal.setDecimals(1)
        self.caudal.setMaximum(100000.0)
        self.caudal.setSingleStep(1.0)
        self.caudal.setObjectName("caudal")
        self.horizontalLayout_7.addWidget(self.caudal, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayoutWidget_13 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_13.setGeometry(QtCore.QRect(60, 170, 91, 31))
        self.horizontalLayoutWidget_13.setObjectName("horizontalLayoutWidget_13")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_13)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.profundidad = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget_13)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setItalic(False)
        self.profundidad.setFont(font)
        self.profundidad.setStyleSheet("\n"
"color: rgb(1, 255, 1);")
        self.profundidad.setDecimals(1)
        self.profundidad.setMaximum(100000.0)
        self.profundidad.setSingleStep(1.0)
        self.profundidad.setObjectName("profundidad")
        self.horizontalLayout_14.addWidget(self.profundidad, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(20, 110, 41, 31))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setKerning(False)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_8.addWidget(self.label_7, 0, QtCore.Qt.AlignRight)
        self.resultado = QtWidgets.QTextEdit(self.centralwidget)
        self.resultado.setGeometry(QtCore.QRect(250, 60, 341, 271))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        self.resultado.setFont(font)
        self.resultado.setStyleSheet("\n"
"color: rgb(1, 255, 1);")
        self.resultado.setObjectName("resultado")
        self.horizontalLayoutWidget_18 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_18.setGeometry(QtCore.QRect(20, 140, 41, 31))
        self.horizontalLayoutWidget_18.setObjectName("horizontalLayoutWidget_18")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_18)
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget_18)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setKerning(False)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_19.addWidget(self.label_9, 0, QtCore.Qt.AlignRight)
        self.horizontalLayoutWidget_19 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_19.setGeometry(QtCore.QRect(60, 140, 91, 31))
        self.horizontalLayoutWidget_19.setObjectName("horizontalLayoutWidget_19")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_19)
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.sedimentacion = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget_19)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setItalic(False)
        self.sedimentacion.setFont(font)
        self.sedimentacion.setStyleSheet("\n"
"color: rgb(1, 255, 1);")
        self.sedimentacion.setDecimals(1)
        self.sedimentacion.setMaximum(100000.0)
        self.sedimentacion.setSingleStep(1.0)
        self.sedimentacion.setObjectName("sedimentacion")
        self.horizontalLayout_20.addWidget(self.sedimentacion, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayoutWidget_20 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_20.setGeometry(QtCore.QRect(20, 230, 41, 31))
        self.horizontalLayoutWidget_20.setObjectName("horizontalLayoutWidget_20")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_20)
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget_20)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_21.addWidget(self.label_10, 0, QtCore.Qt.AlignRight)
        self.horizontalLayoutWidget_21 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_21.setGeometry(QtCore.QRect(60, 230, 91, 31))
        self.horizontalLayoutWidget_21.setObjectName("horizontalLayoutWidget_21")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_21)
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.t = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget_21)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setItalic(False)
        self.t.setFont(font)
        self.t.setStyleSheet("\n"
"color: rgb(1, 255, 1);")
        self.t.setDecimals(1)
        self.t.setMaximum(100000.0)
        self.t.setSingleStep(1.0)
        self.t.setObjectName("t")
        self.horizontalLayout_22.addWidget(self.t, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayoutWidget_22 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_22.setGeometry(QtCore.QRect(150, 20, 81, 31))
        self.horizontalLayoutWidget_22.setObjectName("horizontalLayoutWidget_22")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_22)
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.cb_p = QtWidgets.QComboBox(self.horizontalLayoutWidget_22)
        self.cb_p.setStyleSheet("background-color: rgb(136, 136, 136);\n"
"color: rgb(34, 63, 255);\n"
"selection-background-color: rgb(206, 206, 206);")
        self.cb_p.setObjectName("cb_p")
        self.horizontalLayout_23.addWidget(self.cb_p)
        self.horizontalLayoutWidget_23 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_23.setGeometry(QtCore.QRect(150, 50, 81, 31))
        self.horizontalLayoutWidget_23.setObjectName("horizontalLayoutWidget_23")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_23)
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.cb_le = QtWidgets.QComboBox(self.horizontalLayoutWidget_23)
        self.cb_le.setStyleSheet("background-color: rgb(136, 136, 136);\n"
"color: rgb(34, 63, 255);\n"
"selection-background-color: rgb(206, 206, 206);")
        self.cb_le.setObjectName("cb_le")
        self.horizontalLayout_24.addWidget(self.cb_le)
        self.horizontalLayoutWidget_24 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_24.setGeometry(QtCore.QRect(150, 80, 81, 31))
        self.horizontalLayoutWidget_24.setObjectName("horizontalLayoutWidget_24")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_24)
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.cb_v = QtWidgets.QComboBox(self.horizontalLayoutWidget_24)
        self.cb_v.setStyleSheet("background-color: rgb(136, 136, 136);\n"
"color: rgb(34, 63, 255);\n"
"selection-background-color: rgb(206, 206, 206);")
        self.cb_v.setObjectName("cb_v")
        self.horizontalLayout_25.addWidget(self.cb_v)
        self.horizontalLayoutWidget_25 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_25.setGeometry(QtCore.QRect(150, 110, 81, 31))
        self.horizontalLayoutWidget_25.setObjectName("horizontalLayoutWidget_25")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_25)
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.cb_qs = QtWidgets.QComboBox(self.horizontalLayoutWidget_25)
        self.cb_qs.setStyleSheet("background-color: rgb(136, 136, 136);\n"
"color: rgb(34, 63, 255);\n"
"selection-background-color: rgb(206, 206, 206);")
        self.cb_qs.setObjectName("cb_qs")
        self.horizontalLayout_26.addWidget(self.cb_qs)
        self.horizontalLayoutWidget_26 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_26.setGeometry(QtCore.QRect(150, 140, 81, 31))
        self.horizontalLayoutWidget_26.setObjectName("horizontalLayoutWidget_26")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_26)
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.cb_sr = QtWidgets.QComboBox(self.horizontalLayoutWidget_26)
        self.cb_sr.setStyleSheet("background-color: rgb(136, 136, 136);\n"
"color: rgb(34, 63, 255);\n"
"selection-background-color: rgb(206, 206, 206);")
        self.cb_sr.setObjectName("cb_sr")
        self.horizontalLayout_27.addWidget(self.cb_sr)
        self.horizontalLayoutWidget_27 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_27.setGeometry(QtCore.QRect(150, 170, 81, 31))
        self.horizontalLayoutWidget_27.setObjectName("horizontalLayoutWidget_27")
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_27)
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.cb_ad = QtWidgets.QComboBox(self.horizontalLayoutWidget_27)
        self.cb_ad.setStyleSheet("background-color: rgb(136, 136, 136);\n"
"color: rgb(34, 63, 255);\n"
"selection-background-color: rgb(206, 206, 206);")
        self.cb_ad.setObjectName("cb_ad")
        self.horizontalLayout_28.addWidget(self.cb_ad)
        self.horizontalLayoutWidget_28 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_28.setGeometry(QtCore.QRect(150, 230, 81, 31))
        self.horizontalLayoutWidget_28.setObjectName("horizontalLayoutWidget_28")
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_28)
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.cb_t = QtWidgets.QComboBox(self.horizontalLayoutWidget_28)
        self.cb_t.setStyleSheet("background-color: rgb(136, 136, 136);\n"
"color: rgb(34, 63, 255);\n"
"selection-background-color: rgb(206, 206, 206);")
        self.cb_t.setObjectName("cb_t")
        self.horizontalLayout_29.addWidget(self.cb_t)
        self.horizontalLayoutWidget_14 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_14.setGeometry(QtCore.QRect(20, 200, 41, 31))
        self.horizontalLayoutWidget_14.setObjectName("horizontalLayoutWidget_14")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_14)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_14)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setKerning(False)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_15.addWidget(self.label_4, 0, QtCore.Qt.AlignRight)
        self.horizontalLayoutWidget_15 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_15.setGeometry(QtCore.QRect(60, 200, 91, 31))
        self.horizontalLayoutWidget_15.setObjectName("horizontalLayoutWidget_15")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_15)
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.tw = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget_15)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setItalic(False)
        self.tw.setFont(font)
        self.tw.setStyleSheet("\n"
"color: rgb(1, 255, 1);")
        self.tw.setDecimals(1)
        self.tw.setMaximum(100000.0)
        self.tw.setSingleStep(1.0)
        self.tw.setObjectName("tw")
        self.horizontalLayout_16.addWidget(self.tw, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayoutWidget_29 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_29.setGeometry(QtCore.QRect(150, 200, 81, 31))
        self.horizontalLayoutWidget_29.setObjectName("horizontalLayoutWidget_29")
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_29)
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.cb_tw = QtWidgets.QComboBox(self.horizontalLayoutWidget_29)
        self.cb_tw.setStyleSheet("background-color: rgb(136, 136, 136);\n"
"color: rgb(34, 63, 255);\n"
"selection-background-color: rgb(206, 206, 206);")
        self.cb_tw.setObjectName("cb_tw")
        self.horizontalLayout_30.addWidget(self.cb_tw)
        self.horizontalLayoutWidget_30 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_30.setGeometry(QtCore.QRect(60, 300, 171, 31))
        self.horizontalLayoutWidget_30.setObjectName("horizontalLayoutWidget_30")
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_30)
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.cb_modelo = QtWidgets.QComboBox(self.horizontalLayoutWidget_30)
        self.cb_modelo.setStyleSheet("background-color: rgb(203, 203, 203);\n"
"selection-background-color: rgb(130, 186, 255);")
        self.cb_modelo.setObjectName("cb_modelo")
        self.horizontalLayout_31.addWidget(self.cb_modelo)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Marina"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">P</span><span style=\" color:#ffffff; vertical-align:sub;\">(0)</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">V</span></p></body></html>"))
        self.Calcular.setText(_translate("MainWindow", "Report"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">L</span><span style=\" color:#ffffff; vertical-align:sub;\">e</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">ad</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Q</span><span style=\" color:#ffffff; vertical-align:sub;\">s</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">sr</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:400; color:#ffffff;\">t</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">t</span><span style=\" color:#ffffff; vertical-align:sub;\">w</span></p></body></html>"))

