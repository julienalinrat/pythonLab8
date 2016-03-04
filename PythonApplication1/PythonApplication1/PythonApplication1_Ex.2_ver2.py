import sys
from PySide.QtCore import*
from PySide.QtGui import*


'''
class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
       
        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0,127,0))

        p.drawEllipse(10.0, 20.0, 80.0, 60.0)
        p.drawEllipse(90.0, 20.0, 80.0, 60.0)
        p.drawEllipse(170.0, 20.0, 80.0, 60.0)
        p.drawEllipse(250.0, 20.0, 80.0, 60.0)
        p.drawEllipse(330.0, 20.0, 80.0, 60.0)

        p.setBrush(QColor(50,50,50))

        p.drawEllipse(340,30,20,20)
        p.drawEllipse(380,30,20,20)

        p.setBrush(QColor(127,0,0))

        p.drawEllipse(360,40,20,20)

        p.setBrush(QColor(0,0,127))
        p.drawPolygon([QPoint(360,70),QPoint(370,60),QPoint(365,60),])


def main():
    app = QApplication(sys.argv)
    w = Simple_drawing_window()
    w.show()
    return app.exec_()



if (__name__ == "__main__"):
    sys.exit(main())
    '''

import PySide.QtCore as QtCore

class W(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.resize(400,400)
        self.myIsMousePressing = False
        self.p = QPainter(self)
        self.autoFillBackground()
        self.x = 0
        self.y = 0
        self.r = dict()#{(x,Y,49, 49):rect}
        self.penColor = 1
    def mousePressEvent(self, event):
        self.myIsMousePressing = True
    def mouseReleaseEvent(self, event):
        self.myIsMousePressing = False
    def myTimeOut(self):
        if self.myIsMousePressing:
            pos = self.mapFromGlobal(QCursor.pos())
            self.x = pos.x()/50
            self.y = pos.y()/50
            self.r[(self.x*50, self.y*50, 10, 10)] = self.penColor
    def paintEvent(self, event):
        self.p.begin(self)
        for k in self.r.keys():
            if self.r[k] == 1:
                self.p.setPen(QtCore.Qt.black)
                self.p.setBrush(QtCore.Qt.black)
            else:
                self.p.setPen(QtCore.Qt.white)
                self.p.setBrush(QtCore.Qt.white)
            self.p.drawRect(*k)
        self.p.end()
        self.update()

class MyWidget(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setMinimumSize(400, 400)
        self.initMenu()
        self.w = W()
        self.setCentralWidget(self.w)
        self.t = QTimer(self.w)
        self.t.timeout.connect(self.w.myTimeOut)
        self.t.start(1)

    def initMenu(self):
        self.fileMenu = self.menuBar().addMenu("&File")
        self.editMenu = self.menuBar().addMenu("&Edit")
        self.helpMenu = self.menuBar().addMenu("&Help")

        self.fileMenuAction = QAction("&New", self)
        self.editMenuAction1 = QAction("&Black", self)
        self.editMenuAction2 = QAction("&White", self)
        self.helpMenuAction = QAction("&About", self)

        actGroup = QActionGroup(self)
        actGroup.addAction(self.editMenuAction1)
        actGroup.addAction(self.editMenuAction2)

        self.editMenuAction1.setCheckable(True)
        self.editMenuAction2.setCheckable(True)
        self.editMenuAction1.setChecked(True)

        self.fileMenu.addAction(self.fileMenuAction)
        self.editMenu.addAction(self.editMenuAction1)
        self.editMenu.addAction(self.editMenuAction2)
        self.helpMenu.addAction(self.helpMenuAction)

        self.editMenuAction1.triggered.connect(self.action1)
        self.editMenuAction2.triggered.connect(self.action2)

    def action1(self):
        self.w.penColor = 1

    def action2(self):
        self.w.penColor = 2

app = QApplication([])
mainWin = MyWidget()
mainWin.show()
app.exec_()