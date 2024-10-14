from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QTableWidget, QTableWidgetItem, QAbstractItemView

class estacionGas:
    def setup_ui(self, MainWindow):
        MainWindow.setWindowTitle("Sistema de Gestión de Gasolinera")
        MainWindow.setGeometry(100, 100, 600, 400)

        # Widgets principales
        self.central_widget = QWidget(MainWindow)
        self.layout = QVBoxLayout(self.central_widget)

        # Formulario de venta de combustible
        self.type_label = QLabel("Tipo de Combustible:")
        self.type_combo = QComboBox()
        self.type_combo.addItems(["Gasolina Súper", "Gasolina Regular", "Diesel"])

        self.total_label = QLabel("Total a Pagar: $")
        self.total_input = QLineEdit()
        self.total_input.setPlaceholderText("Introduce el monto total en dólares")

        self.gallons_label = QLabel("Galones: 0.00")
        self.calculate_button = QPushButton("Calcular Galones")
        self.calculate_button.clicked.connect(self.calculate_gallons)  # Conectar botón al cálculo de galones

        self.sell_button = QPushButton("Confirmar Venta")
        self.sell_button.clicked.connect(self.confirm_sale)  # Conectar botón a método de confirmación

        # Tabla para mostrar ventas
        self.sales_table = QTableWidget(0, 3)
        self.sales_table.setHorizontalHeaderLabels(["Tipo", "Galones", "Total ($)"])
        self.sales_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)  # Desactivar la edición
        self.sales_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)  # Seleccionar toda la fila

        # Agregar widgets al layout
        self.layout.addWidget(self.type_label)
        self.layout.addWidget(self.type_combo)
        self.layout.addWidget(self.total_label)
        self.layout.addWidget(self.total_input)
        self.layout.addWidget(self.calculate_button)
        self.layout.addWidget(self.gallons_label)
        self.layout.addWidget(self.sell_button)
        self.layout.addWidget(self.sales_table)

        MainWindow.setCentralWidget(self.central_widget)

    def calculate_gallons(self):
        # Precios por galón de cada tipo de combustible en El Salvador
        prices = {
            "Gasolina Súper": 3.77,  # Precio por galón de gasolina súper
            "Gasolina Regular": 3.73,  # Precio por galón de gasolina regular
            "Diesel": 3.46     # Precio por galón de diésel
        }

        try:
            # Obtener el monto total ingresado
            total = float(self.total_input.text())
            # Obtener el tipo de combustible seleccionado
            fuel_type = self.type_combo.currentText()
            # Obtener el precio del combustible por galón
            price_per_gallon = prices[fuel_type]

            # Calcular galones usando lambda
            gallons = (lambda total, price: total / price)(total, price_per_gallon)
            # Actualizar etiqueta de galones
            self.gallons_label.setText(f"Galones: {gallons:.2f}")
        except ValueError:
            self.gallons_label.setText("Por favor, ingresa un monto válido.")

    def confirm_sale(self):
        try:
            fuel_type = self.type_combo.currentText()
            gallons = float(self.gallons_label.text().split(": ")[1])
            total = float(self.total_input.text())

            # Insertar nueva fila en la tabla de ventas
            row_position = self.sales_table.rowCount()
            self.sales_table.insertRow(row_position)
            self.sales_table.setItem(row_position, 0, QTableWidgetItem(fuel_type))
            self.sales_table.setItem(row_position, 1, QTableWidgetItem(f"{gallons:.2f}"))
            self.sales_table.setItem(row_position, 2, QTableWidgetItem(f"${total:.2f}"))

            # Limpiar campos de entrada
            self.total_input.clear()
            self.gallons_label.setText("Galones: 0.00")
        except ValueError:
            self.gallons_label.setText("Error en la confirmación de venta.")
