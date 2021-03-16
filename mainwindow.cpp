#if defined(WIN32) || defined(_WIN32) || defined(__WIN32) && !defined(__CYGWIN__)
    #include <windows.h>
#else

#endif

#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QString>
#include <QAction>
#include <cstring>

QString TCHARToString(const TCHAR* ptsz);

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    Setup_Serial(9600);
    Scan_Serial_Port();

    QObject::connect(port, SIGNAL(readyRead()), this, SLOT(text_Reading()));
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::Setup_Serial(int baudrate){
    port = new QSerialPort();
    port->setBaudRate(baudrate);
    port->setDataBits(QSerialPort::Data8);
    port->setParity(QSerialPort::NoParity);
    port->setStopBits(QSerialPort::OneStop);
    port->setFlowControl(QSerialPort::NoFlowControl);
}

void MainWindow::text_Reading(){
    QByteArray read_Data;
    read_Data = port->readAll();

    ui->label->setText(read_Data);
    ui->label->show();

    qDebug() << read_Data.length();
}

void MainWindow::on_pushButton_clicked()
{
    QByteArray send_Data;
    send_Data = ui->textEdit->toPlainText().toUtf8();
    port->write(send_Data.data());
}

void MainWindow::on_serial_Button_clicked()//시리얼 포트 확인 버튼
{
    port->setPortName(ui->comboBox->currentText());

    if(!port->open(QIODevice::ReadWrite)){
        qDebug() << "\n Serial port open Error \n";
        ui->label->setText("Serial port Error");
    }
    else{
        ui->label->setText("Connet!");
    }
}


/**
 * @brief 사용가능한 시리얼 포트 검색
 * @param ui
 */
void MainWindow::Scan_Serial_Port(){
    HKEY hKey; // Windows 레지스트리 접근
    RegOpenKey(HKEY_LOCAL_MACHINE, TEXT("HARDWARE\\DEVICEMAP\\SERIALCOMM"), &hKey);

    TCHAR szData[20], szName[100];
    DWORD index = 0, dwSize=100, dwSize2 = 20, dwType = REG_SZ;
    memset(szData, 0x00, sizeof(szData));
    memset(szName, 0x00, sizeof(szName));

    while (ERROR_SUCCESS == RegEnumValue(hKey, index, szName, &dwSize, NULL, NULL, NULL, NULL)){
       index++;

       RegQueryValueEx(hKey, szName, NULL, &dwType, (LPBYTE)szData, &dwSize2);
       QString tem = TCHARToString(szData);
       ui->comboBox->addItem(tem);

       memset(szData, 0x00, sizeof(szData));  //초기화
       memset(szName, 0x00, sizeof(szName));
       dwSize = 100;
       dwSize2 = 20;
   }

   RegCloseKey(hKey);
}

QString TCHARToString(const TCHAR* ptsz){
     int len = wcslen((wchar_t*)ptsz);
     char* psz = new char[2*len + 1];
     wcstombs(psz, (wchar_t*)ptsz, 2*len + 1);
     QString s = psz;
     delete [] psz;
     return s;
}
