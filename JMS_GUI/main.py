from QT_Form import *

if __name__=="__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    ui.signals()
    Form.show()
    sys.exit(app.exec_())
