class Inventory:
    def __init__(self):
        self.fuels = {
            "Gasolina Súper": 264.17,  # Galones iniciales (1000 litros convertidos a galones)
            "Gasolina Regular": 264.17,  # Galones iniciales (1000 litros convertidos a galones)
            "Diesel": 264.17  # Galones iniciales (1000 litros convertidos a galones)
        }

    # Método para actualizar el inventario en galones
    def update_inventory(self, fuel_type, gallons_sold):
        if fuel_type not in self.fuels:
            raise ValueError(f"El tipo de combustible '{fuel_type}' no es válido.")
        
        if gallons_sold < 0:
            raise ValueError("Los galones vendidos no pueden ser negativos.")
        
        if self.fuels[fuel_type] < gallons_sold:
            raise ValueError(f"No hay suficiente {fuel_type}. Disponible: {self.fuels[fuel_type]:.2f} galones.")
        
        self.fuels[fuel_type] -= gallons_sold

    # Método para agregar combustible en galones
    def add_fuel(self, fuel_type, gallons):
        if fuel_type not in self.fuels:
            raise ValueError(f"El tipo de combustible '{fuel_type}' no es válido.")
        
        if gallons < 0:
            raise ValueError("Los galones agregados no pueden ser negativos.")
        
        self.fuels[fuel_type] += gallons

    # Método para obtener el inventario en galones
    def get_inventory(self):
        return self.fuels


class Sales:
    def __init__(self):
        self.sales = []

    # Método para registrar una venta en galones
    def record_sale(self, fuel_type, gallons, total):
        if gallons < 0 or total < 0:
            raise ValueError("Los galones vendidos y el total no pueden ser negativos.")
        
        self.sales.append({
            "fuel_type": fuel_type,
            "gallons": gallons,
            "total": total
        })

    # Método para obtener todas las ventas
    def get_sales(self):
        return self.sales

    # Método para obtener los ingresos totales
    def get_total_income(self):
        return sum(sale['total'] for sale in self.sales)

