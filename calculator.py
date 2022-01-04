from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtUiTools import QUiLoader
from math import *



class Calculator (QMainWindow):
    def __init__(self):
        super().__init__()
        loader=QUiLoader()
        self.app=loader.load("design.ui")
        self.app.show()
        self.result=0
        self.opration=""

        self.app.b0.clicked.connect(self.zero)
        self.app.b1.clicked.connect(self.one)
        self.app.b2.clicked.connect(self.two)
        self.app.b3.clicked.connect(self.three)
        self.app.b4.clicked.connect(self.four)
        self.app.b5.clicked.connect(self.five)
        self.app.b6.clicked.connect(self.six)
        self.app.b7.clicked.connect(self.seven)
        self.app.b8.clicked.connect(self.eight)
        self.app.b9.clicked.connect(self.nine)
        self.app.b_sum.clicked.connect(self.add)
        self.app.b_sub.clicked.connect(self.sub)
        self.app.b_m.clicked.connect(self.mul)
        self.app.b_d.clicked.connect(self.div)
        self.app.b_sin.clicked.connect(self.sin_t)
        self.app.b_cos.clicked.connect(self.cos_t)
        self.app.b_tan.clicked.connect(self.tan_t)
        self.app.b_cot.clicked.connect(self.cot_t)
        self.app.b_log.clicked.connect(self.log_n)
        self.app.b_sqrt.clicked.connect(self.sqrt_n)
        self.app.b_dot.clicked.connect(self.dot)
        self.app.b_pm.clicked.connect(self.plus_minus)
        self.app.b_p.clicked.connect(self.percentage)
        self.app.b_e.clicked.connect(self.equal)
        self.app.b_ac.clicked.connect(self.reset)

    def zero(self):
        self.app.line_edit.setText(self.app.line_edit.text() + "0")
    def one(self):
        self.app.line_edit.setText(self.app.line_edit.text() + "1")
    def two(self):
        self.app.line_edit.setText(self.app.line_edit.text() + "2")
    def three(self):
        self.app.line_edit.setText(self.app.line_edit.text() + "3")
    def four(self):
        self.app.line_edit.setText(self.app.line_edit.text() + "4")
    def five(self):
        self.app.line_edit.setText(self.app.line_edit.text() + "5")
    def six(self):
        self.app.line_edit.setText(self.app.line_edit.text() + "6")
    def seven(self):
        self.app.line_edit.setText(self.app.line_edit.text() + "7")
    def eight(self):
        self.app.line_edit.setText(self.app.line_edit.text() + "8")
    def nine(self):
        self.app.line_edit.setText(self.app.line_edit.text() + "9")

    def add(self):
        try:
            self.result=float(self.app.line_edit.text())
            self.app.line_edit.setText("")
            self.opration="+"
        except:
            self.app.line_edit.setText(":(")
            self.result = 0
        
    def sub(self):
        try:
            self.result=float(self.app.line_edit.text())
            self.app.line_edit.setText("")
            self.opration="-"
        except:
            self.app.line_edit.setText(":(")
            self.result = 0
       
    def mul(self):
        try:
            self.result=float(self.app.line_edit.text())
            self.app.line_edit.setText("")
            self.opration="*"
        except:
            self.app.line_edit.setText(":(")
            self.result = 0
        
    def div(self):
        try:
            self.result=float(self.app.line_edit.text())
            self.app.line_edit.setText("")
            self.opration="/"
        except:
            self.app.line_edit.setText(":(")
            self.result = 0
        
    def sin_t(self):
        self.result = float(self.app.line_edit.text())
        self.result = self.result/360 *2 * pi
        self.result = round(sin(self.result),5)
        self.app.line_edit.setText(str(self.result))
        self.oparation = 'sin'
        self.step += 1

    def cos_t(self):
        self.result = float(self.app.line_edit.text())
        self.result = self.result/360 *2 * pi
        self.result = round(cos(self.result),5)
        self.app.line_edit.setText(str(self.result))
        self.oparation = 'cos'
        self.step += 1

    def tan_t(self):
        self.result = float(self.app.line_edit.text())
        self.result = self.result/360 *2 * pi
        self.result = round(tan(self.result),5)
        self.app.line_edit.setText(str(self.result))
        self.oparation = 'tan'
        self.step += 1
           
    def cot_t(self):
        self.result=float(self.app.line_edit.text())
        self.result=self.result/360 *2 * pi
        self.result=round(atan(self.result),5)
        self.app.line_edit.setText(str(self.result))
        self.oparation = 'cot'
        self.step += 1
        
    def log_n(self):
        self.app.line_edit.setText(str(log10(float(self.app.line_edit.text()))))

    def sqrt_n(self):
        self.app.line_edit.setText(str(sqrt(float(self.app.line_edit.text()))))

    def dot(self):
        if '.' not in self.app.line_edit.text():
            self.app.line_edit.setText(self.app.line_edit.text() + '.')
    
    def plus_minus(self):
        self.num2=float(self.app.line_edit.text())
        self.num2 *=-1
        self.app.line_edit.setText(str(self.num2))

    def percentage(self):
        self.app.line_edit.setText(str(float(self.app.line_edit.text())/100))

    def equal(self):
        self.num2 = float(self.app.line_edit.text())
        if self.opration == "+":
            self.result +=self.num2
            self.app.line_edit.setText(str(self.result))
            self.opration= ""
            self.result=0
        elif self.opration == "-":
            self.result -=self.num2
            self.app.line_edit.setText(str(self.result))
            self.opration= ""
            self.result=0
        elif self.opration == "*":
            self.result *= self.num2
            self.app.line_edit.setText(str(self.result))
            self.opration= ""
            self.result=0
        elif self.opration == "/":
            try:
                self.result /= self.num2
                self.app.line_edit.setText(str(self.result))
                self.opration= ""
                self.result=0
            except:
                self.app.line_edit.setText(":(")
                self.opration= ""
                self.result=0
        else:
            self.result = self.num2

    def reset(self):
       self.app.line_edit.setText("")
       self.result=0
       self.opration=""



if __name__ == "__main__":
    my_app=QApplication()
    main_window=Calculator()
    my_app.exec()