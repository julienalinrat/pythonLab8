import sys
from PySide.QtCore import*
from PySide.QtGui import*



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