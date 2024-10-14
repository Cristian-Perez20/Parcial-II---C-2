from PyQt6.QtWidgets import QApplication, QMainWindow
import sys
from EstacionGAS import estacionGas  # Asegúrate de que el archivo se llame EstacionGAS.py

class GasStationApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = estacionGas()  # Cargamos la interfaz
        self.ui.setup_ui(self)  # Configuramos la interfaz

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GasStationApp()
    window.show()
    sys.exit(app.exec())
