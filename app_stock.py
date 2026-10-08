import sys
import pandas as pd
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTabWidget, QWidget, 
                             QVBoxLayout, QTableWidget, QTableWidgetItem, 
                             QPushButton, QHBoxLayout, QLabel, QLineEdit, QHeaderView, QInputDialog, QMessageBox)
from PyQt5.QtCore import Qt

class StockApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Control de Stock Semanal - Distribuidora")
        self.setGeometry(100, 100, 950, 700)

        # Todos los productos completos organizados por proveedor / categoría
        self.datos_stock = {
            "Quesos y Embutidos": [
                ["Manteca Alternativa x 100g Glucelat", "160", ""],
                ["Manteca Alternativa x 200g Glucelat", "86", ""],
                ["Cremoso X Salut", "0", ""],
                ["Barra Las 3 Niñas", "13", ""],
                ["Barra Sagrada", "14", ""],
                ["Cremoso Sagrada", "18", "07/09"],
                ["Cremoso Corbai", "0", ""],
                ["Cremoso Lactear", "16", ""],
                ["Roquefort Quesera", "6", ""],
                ["Muzzarella Muelle", "19", ""],
                ["Muzza Norte", "0", ""],
                ["Cheddar Tonadita Fetas", "18", ""],
                ["Cheddar Tonadita Líquido", "7", ""],
                ["Cremoso Punta", "50", ""],
                ["Barra Punta", "11", ""],
                ["Barra Tonutti", "15", ""],
                ["Roque Emperador", "5", ""],
                ["Muzzarella Barraza", "34", ""],
                ["Barra Manjar Blanco", "10", ""],
                ["Cremoso Barraza", "4", "05/10"],
                ["Sardo Fresco", "37", "05/10"],
                ["Sardo Negro Melincue", "0", ""],
                ["Cremoso Mediterráneo x 4kg", "6", ""],
                ["Cremoso Mediterráneo x 2kg", "32", "30/09 - 19/10"],
                ["Muzza Mediterránea", "0", ""],
                ["Muzza Aurora", "10", "02/09"],
                ["Regianito Noalsa", "1/2", ""],
                ["Sardo Los Toldos", "0", ""],
                ["Romanito Migue", "4", ""],
                ["Bocha Calchaquí", "1", ""],
                ["Cañón Calchaquí", "0", ""],
                ["Salamín 42 x Unidad Fino", "70", ""],
                ["Salamín 42 x Unidad Grueso", "32", "07/08"],
                ["Lomito Ahumado c/ Hierbas y Romero", "0", ""],
                ["Romanito Miguel", "5", ""]
            ],
            "González": [
                ["Bolón Don Jorge", "18", ""],
                ["Salchichón Primavera", "5", ""],
                ["Salchichón Primavera con Jamón", "0", ""],
                ["Paleta Rimini", "9", ""],
                ["Cocidito González con Cuero", "25", ""],
                ["Muelle Agustín", "0", ""],
                ["Paleta Orfebre", "24", ""],
                ["Paleta 42", "0", ""],
                ["Port Salud", "0", ""],
                ["Holanda", "5", ""]
            ],
            "Nonna Pia": [
                ["Provoleta Tradicional Pintada", "0", ""],
                ["Queso de Campo Mixta", "40", ""],
                ["Provoleta con Cazuela", "50", ""],
                ["Provoleta sin Cazuela x Unidad", "0", ""],
                ["Provoleta Fraccionada x 4u", "38", ""]
            ],
            "La Serenísima": [
                ["Manteca 100g", "35", ""],
                ["Manteca 200g", "50", ""],
                ["Dulce de Leche Clásico x 400g", "18", ""],
                ["Dulce de Leche Repostero 400g", "23", "30/10"],
                ["Dulce de Leche Colonial x 400g", "20", "02/27"],
                ["Dulce de Leche Clásico x 250g", "1", ""],
                ["Dulce de Leche Colonial x 250g", "18", "15/11"],
                ["Crema 200cc", "0", ""],
                ["Crema 330 Batir", "0", ""],
                ["Crema 330 Cocinar", "0", ""],
                ["Crema 520 Cocinar", "0", ""],
                ["Crema 520 Batir", "0", ""],
                ["Finlandia Light x 290g", "7", ""],
                ["Finlandia Clásico x 290g", "0", ""],
                ["Finlandia Red Calorías x 290g", "0", ""],
                ["Finlandia Light x 180g", "7", ""],
                ["Finlandia Clásico x 180g", "6", ""],
                ["Finlandia Red Calorías x 180g", "6", ""],
                ["Queso Rallado 35g", "80", ""],
                ["Queso Rallado 70g", "25", "11/10"],
                ["Leche Larga Vida LS Entera", "8", ""],
                ["Leche Larga Vida LS Descremada", "7", ""]
            ],
            "Tapamanía": [
                ["Tapas Empanadas Freír x 330g", "45", ""],
                ["Tapas Empanadas Criolla x 330g", "80", ""],
                ["Tapas Empanadas Horno x 330g", "45", ""],
                ["Tapas Pascualina Criolla x 400g", "5", ""],
                ["Tapas Pascualina Horno x 400g", "10", ""],
                ["Tapas Empanadas Súper Horno x 500g", "32", ""],
                ["Tapas Empanadas Súper Criolla x 500g", "36", ""],
                ["Tapas Empanadas Súper Tubo x 2kg Horno", "14", ""],
                ["Tapas Empanadas Súper Tubo x 2kg Criolla", "20", ""],
                ["Ravioles Blíster Pollo y Verdura x 500g", "0", "Cambio: 1"],
                ["Ravioles Blíster Jamón y Ricota x 500g", "13", "Cambio: 5"],
                ["Ravioles Blíster Verdura x 500g", "8", "Cambio: 3"],
                ["Ravioles Blíster 4 Quesos x 500g", "25", ""],
                ["Ravioles Bolsa Verdura x 1kg", "8", ""],
                ["Ravioles Bolsa Pollo y Verdura x 1kg", "15", ""],
                ["Ravioles Bolsa 4 Quesos x 1kg", "25", ""],
                ["Ravioles Bolsa Ricota y Jamón x 1kg", "15", ""],
                ["Ñoquis Blíster x 500g", "6", ""],
                ["Ñoquis Bolsa x 1kg", "11", ""]
            ],
            "Pan Baires Pan": [
                ["Multicereal", "29", "16/10"],
                ["Salvado", "27", "18/10"],
                ["Blanco", "17", "16/10"],
                ["Hamburguesa", "25", "25/09"]
            ]
        }

        self.tablas = {}
        self.initUI()

    def initUI(self):
        main_widget = QWidget()
        layout = QVBoxLayout(main_widget)

        # Encabezado superior
        top_layout = QHBoxLayout()
        lbl_titulo = QLabel("📋 Control de Stock - Carga Lunes")
        lbl_titulo.setStyleSheet("font-size: 18px; font-weight: bold; color: #2C3E50;")
        top_layout.addWidget(lbl_titulo)
        top_layout.addStretch()

        btn_agregar = QPushButton("➕ Agregar Producto")
        btn_agregar.setStyleSheet("background-color: #2980B9; color: white; font-weight: bold; padding: 8px 12px; border-radius: 4px;")
        btn_agregar.clicked.connect(self.agregar_producto)
        top_layout.addWidget(btn_agregar)

        btn_guardar = QPushButton("💾 Guardar en Excel")
        btn_guardar.setStyleSheet("background-color: #27AE60; color: white; font-weight: bold; padding: 8px 15px; border-radius: 4px;")
        btn_guardar.clicked.connect(self.guardar_excel)
        top_layout.addWidget(btn_guardar)

        layout.addLayout(top_layout)

        # Buscador de productos rápido
        search_layout = QHBoxLayout()
        lbl_buscar = QLabel("🔍 Buscar Producto:")
        lbl_buscar.setStyleSheet("font-weight: bold;")
        self.txt_buscar = QLineEdit()
        self.txt_buscar.setPlaceholderText("Escribe para filtrar productos...")
        self.txt_buscar.textChanged.connect(self.filtrar_productos)
        search_layout.addWidget(lbl_buscar)
        search_layout.addWidget(self.txt_buscar)
        layout.addLayout(search_layout)

        # Pestañas por Proveedor / Marca
        self.tabs = QTabWidget()
        for proveedor, productos in self.datos_stock.items():
            tab = QWidget()
            tab_layout = QVBoxLayout(tab)
            
            tabla = QTableWidget()
            tabla.setColumnCount(3)
            tabla.setHorizontalHeaderLabels(["Producto", "Cantidad", "Vencimiento / Notas"])
            tabla.setRowCount(len(productos))
            
            for row_idx, fila in enumerate(productos):
                for col_idx, valor in enumerate(fila):
                    item = QTableWidgetItem(valor)
                    if col_idx == 1:
                        item.setTextAlignment(Qt.AlignCenter)
                    tabla.setItem(row_idx, col_idx, item)

            tabla.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
            tabla.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
            tabla.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
            tabla.setShowGrid(True)
            
            tab_layout.addWidget(tabla)
            self.tabs.addTab(tab, proveedor)
            self.tablas[proveedor] = tabla

        layout.addWidget(self.tabs)
        self.setCentralWidget(main_widget)

    def filtrar_productos(self, texto):
        texto = texto.lower().strip()
        for proveedor, tabla in self.tablas.items():
            for row in range(tabla.rowCount()):
                item_prod = tabla.item(row, 0)
                if item_prod:
                    nombre_prod = item_prod.text().lower()
                    match = texto in nombre_prod
                    tabla.setRowHidden(row, not match)

    def agregar_producto(self):
        pestaña_actual = self.tabs.tabText(self.tabs.currentIndex())
        tabla = self.tablas[pestaña_actual]
        
        prod_nombre, ok = QInputDialog.getText(self, "Nuevo Producto", f"Nombre del producto para {pestaña_actual}:")
        if ok and prod_nombre.strip():
            row_pos = tabla.rowCount()
            tabla.insertRow(row_pos)
            tabla.setItem(row_pos, 0, QTableWidgetItem(prod_nombre.strip()))
            
            item_cant = QTableWidgetItem("0")
            item_cant.setTextAlignment(Qt.AlignCenter)
            tabla.setItem(row_pos, 1, item_cant)
            
            tabla.setItem(row_pos, 2, QTableWidgetItem(""))
            QMessageBox.information(self, "Éxito", f"Producto '{prod_nombre}' agregado en {pestaña_actual}.")

    def guardar_excel(self):
        try:
            with pd.ExcelWriter("Stock_Actualizado_Lunes.xlsx") as writer:
                for proveedor, tabla in self.tablas.items():
                    filas = []
                    for row in range(tabla.rowCount()):
                        prod = tabla.item(row, 0).text() if tabla.item(row, 0) else ""
                        cant = tabla.item(row, 1).text() if tabla.item(row, 1) else ""
                        notas = tabla.item(row, 2).text() if tabla.item(row, 2) else ""
                        filas.append([prod, cant, notas])
                    
                    df = pd.DataFrame(filas, columns=["Producto", "Cantidad", "Vencimiento / Notas"])
                    df.to_excel(writer, sheet_name=proveedor[:31], index=False)
            QMessageBox.information(self, "Guardado", "¡Stock guardado con éxito en 'Stock_Actualizado_Lunes.xlsx'!")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo guardar el archivo: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StockApp()
    window.show()
    sys.exit(app.exec_())