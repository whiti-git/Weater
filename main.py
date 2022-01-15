import requests
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

app = QApplication([])
app.setStyle('Fusion')
main = QVBoxLayout()
inp = QLineEdit()
button = QPushButton('GET')
desc = QLabel('SUMMARY')
temp = QLabel('TEMPERATURE')
clouds = QLabel('CLOUDS')
wind = QLabel('WIND SPEED')
press = QLabel("PRESSURE")
main.addWidget(inp)
main.addWidget(button)
main.addWidget(desc, alignment=Qt.AlignLeft)
main.addWidget(temp, alignment=Qt.AlignLeft)
main.addWidget(clouds, alignment=Qt.AlignLeft)
main.addWidget(wind, alignment=Qt.AlignLeft)
main.addWidget(press, alignment=Qt.AlignLeft)
win = QWidget()
win.setWindowTitle('Weather')
win.setLayout(main)
win.show()


def get(city):
    try:
        api = requests.get(
            'https://api.openweathermap.org/data/2.5/weather?q={}&appid=7a169433eebcace064229e4fc6a493b8'.format(city))
        if api.status_code == 401:
            pass
        else:
            data = api.json()
            pars(data)
    except:
        pass


def click():
    get(inp.text())


def pars(data):
    desc.setText('SUMMARY:    ' + data['weather'][0]['description'])
    temp.setText('TEMPERATURE:    ' + str(int(data['main']['temp']-273)))
    press.setText('PRESSURE:    ' + str(data['main']['pressure']))
    wind.setText('WIND SPEED:    ' + str(data['wind']['speed']))
    clouds.setText('CLOUDS:    ' + str(data['clouds']['all']) + '%')


if __name__ == '__main__':
    button.clicked.connect(click)
    app.exec_()
