from pyqttest_form import Ui_MainWindow

import numpy as np
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import QMainWindow,QApplication
import sys
from PyQt5.QtWidgets import QMessageBox

class Figure_Canvas(FigureCanvas):   # 通过继承FigureCanvas类，使得该类既是一个PyQt5的Qwidget，又是一个matplotlib的FigureCanvas，这是连接pyqt5与matplot                                          lib的关键

    def __init__(self, parent=None, width=11, height=5, dpi=100):
        fig = Figure(figsize=(width, height), dpi=100)  # 创建一个Figure，注意：该Figure为matplotlib下的figure，不是matplotlib.pyplot下面的figure

        FigureCanvas.__init__(self, fig) # 初始化父类
        self.setParent(parent)

        self.axes = fig.add_subplot(111) # 调用figure下面的add_subplot方法，类似于matplotlib.pyplot下面的subplot方法

    def test(self):
        x = [1,2,3,4,5,6,7,8,9]
        y = [23,21,32,13,3,132,13,3,1]
        self.axes.plot(x, y)



class MyMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
        def __init__(self, parent=None):    
                super(MyMainWindow, self).__init__(parent)
                self.setupUi(self)
                self.update_canvas()
                self.update_list()
                self.pushButton.clicked.connect(self.on_click)
        def update_canvas(self):
            dr = Figure_Canvas()
            dr.test()  # 画图
            graphicscene = QtWidgets.QGraphicsScene()  # 第三步，创建一个QGraphicsScene，因为加载的图形（FigureCanvas）不能直接放到graphicview控件中，必须先放到graphicScene，然后再把graphicscene放到graphicview中
            graphicscene.addWidget(dr)  # 第四步，把图形放到QGraphicsScene中，注意：图形是作为一个QWidget放到QGraphicsScene中的
            self.graphicsView.setScene(graphicscene)  # 第五步，把QGraphicsScene放入QGraphicsView
            self.graphicsView.show()  # 最后，调用show方法呈现图形！Voila!!

        def update_list(self):
            self.listWidget.addItem('fuck')

        def on_click(self):
            QMessageBox.about(self,"fuck","fuck")

        def closeEvent(self, event):

            reply = QMessageBox.question(self, 'Message',
                "Are you sure to quit?", QMessageBox.Yes | 
                QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()        


            
#主程式，生成一個視窗例項並執行。
if __name__=="__main__":  
        app = QtWidgets.QApplication(sys.argv)  
        myWin = MyMainWindow()  

        myWin.show()  
        app.exec_()