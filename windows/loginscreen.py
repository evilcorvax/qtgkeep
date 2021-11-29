import PyQt5
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage, QPalette, QLinearGradient, QColor
from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QFrame, QLabel, QLineEdit, QPushButton

from utils.gkeep import GKeepNotes


class LoginScreen(QMainWindow):

    def check_auth(self):
        self.web_connector = GKeepNotes(self.login_text_input.text(), self.password_text_input.text())
        print(self.web_connector.get_all_notes())

    def __init__(self):
        super().__init__()

        # print(web_connector.get_all_notes())

        main_widget = QWidget()

        main_layout = QHBoxLayout()
        center_layout = QVBoxLayout()

        frame = QFrame()
        frame.setStyleSheet("QFrame "
                            "{"
                            "background-color: white;"
                            "border-radius: 30px;"
                            "height: 1000px;"
                            "width: 1000px;"
                            "}")

        logo_label = QLabel()
        logo_label.setPixmap(
            QPixmap.fromImage(QImage("resources/gkeep.png")))
        # logo_label.setFixedSize(64, 64)

        self.login_text_input = QLineEdit()
        self.password_text_input = QLineEdit()

        login_button = QPushButton("Login")

        self.login_text_input.setStyleSheet("QLineEdit "
                                       "{"
                                       "border: 1px solid #282830;"
                                       "color: black;"
                                       "font-size: 15px;"
                                       "height:17px;"
                                       "width:400px;"
                                       "margin-left:20px;"
                                       "margin-right:20px;"
                                       "border-radius:10px;"
                                       "padding:5px;"
                                       "}")
        self.password_text_input.setStyleSheet("QLineEdit "
                                          "{"
                                          "border: 1px solid #282830;"
                                          "color: black;"
                                          "font-size: 15px;"
                                          "height:17px;"
                                          "width:400px;"
                                          "margin-left:20px;"
                                          "margin-right:20px;"
                                          "border-radius:10px;"
                                          "padding:5px;"
                                          "}")
        login_button.setStyleSheet("QPushButton "
                                   "{"
                                   "color: white;"
                                   "background-color: black;"
                                   "margin-bottom:20px;"
                                   "margin-top:20px;"
                                   "border:none;"
                                   "height:20px;"
                                   "width:100px;"
                                   "padding:5px;"
                                   "border-radius: 10px;"
                                   "}"
                                   "QPushButton:hover"
                                   "{"
                                   "background-color:#47B0D0;"
                                   "}")
        login_button.setFixedSize(128, 75)

        button_container = QVBoxLayout()
        button_container.addWidget(login_button)
        button_container.setAlignment(Qt.AlignHCenter)

        center_layout.addWidget(logo_label)
        center_layout.addWidget(self.login_text_input)
        center_layout.addWidget(self.password_text_input)
        center_layout.addLayout(button_container)
        center_layout.addWidget(login_button)

        self.showMaximized()
        background_gradient = QLinearGradient(0, 0, 0, self.height())
        background_gradient.setColorAt(0, QColor("#FF512F"))
        background_gradient.setColorAt(1, QColor("#DD2476"))

        back_pallete = QPalette()
        back_pallete.setBrush(QPalette.Background, background_gradient)

        self.setPalette(back_pallete)

        frame.setLayout(center_layout)
        frame.setFixedSize(500, 400)
        center_layout.setAlignment(Qt.AlignCenter)
        logo_label.setAlignment(Qt.AlignCenter)

        main_layout.addWidget(frame)

        main_widget.setLayout(main_layout)

        self.setCentralWidget(main_widget)

        login_button.clicked.connect(self.check_auth)

        self.show()

