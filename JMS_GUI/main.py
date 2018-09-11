from JMS_GUI import *

if __name__=="__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    ui.BG_label.setStyleSheet("background-image: url(./img/BG_IMG.png);")
    Form.show()
    sys.exit(app.exec_())
