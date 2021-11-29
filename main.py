import sys

from PyQt6.QtWidgets import QApplication

from windows.loginscreen import LoginScreen


def main():
    app = QApplication(sys.argv)
    login_screen = LoginScreen()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
