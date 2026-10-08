import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Control de Stock", page_icon="📦", layout="wide")

st.title("📦 Control de Stock - Carga Lunes")
st.caption(f"Fecha de actualización: {datetime.now().strftime('%d/%m/%Y')}")

# Inventario completo cargado por categoría
datos_stock = {
    "Quesos y Embutidos": [
        ["Manteca Alternativa x 100g Glucelat", 160, ""],
        ["Manteca Alternativa x 200g Glucelat", 86, ""],
        ["Cremoso X Salut", 0, ""],
        ["Barra Las 3 Niñas", 13, ""],
        ["Barra Sagrada", 14, ""],
        ["Cremoso Sagrada", 18, "07/09"],
        ["Cremoso Corbai", 0, ""],
        ["Cremoso Lactear", 16, ""],
        ["Roquefort Quesera", 6, ""],
        ["Muzzarella Muelle", 19, ""],
        ["Muzza Norte", 0, ""],
        ["Cheddar Tonadita Fetas", 18, ""],
        ["Cheddar Tonadita Líquido", 7, ""],
        ["Cremoso Punta", 50, ""],
        ["Barra Punta", 11, ""],
        ["Barra Tonutti", 15, ""],
        ["Roque Emperador", 5, ""],
        ["Muzzarella Barraza", 34, ""],
        ["Barra Manjar Blanco", 10, ""],
        ["Cremoso Barraza", 4, "05/10"],
        ["Sardo Fresco", 37, "05/10"],
        ["Sardo Negro Melincue", 0, ""],
        ["Cremoso Mediterráneo x 4kg", 6, ""],
        ["Cremoso Mediterráneo x 2kg", 32, "30/09 - 19/10"],
        ["Muzza Mediterránea", 0, ""],
        ["Muzza Aurora", 10, "02/09"],
        ["Regianito Noalsa", "1/2", ""],
        ["Sardo Los Toldos", 0, ""],
        ["Romanito Migue", 4, ""],
        ["Bocha Calchaquí", 1, ""],
        ["Cañón Calchaquí", 0, ""],
        ["Salamín 42 x Unidad Fino", 70, ""],
        ["Salamín 42 x Unidad Grueso", 32, "07/08"],
        ["Lomito Ahumado c/ Hierbas y Romero", 0, ""],
        ["Romanito Miguel", 5, ""]
    ],
    "González": [
        ["Bolón Don Jorge", 18, ""],
        ["Salchichón Primavera", 5, ""],
        ["Salchichón Primavera con Jamón", 0, ""],
        ["Paleta Rimini", 9, ""],
        ["Cocidito González con Cuero", 25, ""],
        ["Muelle Agustín", 0, ""],
        ["Paleta Orfebre", 24, ""],
        ["Paleta 42", 0, ""],
        ["Port Salud", 0, ""],
        ["Holanda", 5, ""]
    ],
    "Nonna Pia": [
        ["Provoleta Tradicional Pintada", 0, ""],
        ["Queso de Campo Mixta", 40, ""],
        ["Provoleta con Cazuela", 50, ""],
        ["Provoleta sin Cazuela x Unidad", 0, ""],
        ["Provoleta Fraccionada x 4u", 38, ""]
    ],
    "La Serenísima": [
        ["Manteca 100g", 35, ""],
        ["Manteca 200g", 50, ""],
        ["Dulce de Leche Clásico x 400g", 18, ""],
        ["Dulce de Leche Repostero 400g", 23, "30/10"],
        ["Dulce de Leche Colonial x 400g", 20, "02/27"],
        ["Dulce de Leche Clásico x 250g", 1, ""],
        ["Dulce de Leche Colonial x 250g", 18, "15/11"],
        ["Crema 200cc", 0, ""],
        ["Crema 330 Batir", 0, ""],
        ["Crema 330 Cocinar", 0, ""],
        ["Crema 520 Cocinar", 0, ""],
        ["Crema 520 Batir", 0, ""],
        ["Finlandia Light x 290g", 7, ""],
        ["Finlandia Clásico x 290g", 0, ""],
        ["Finlandia Red Calorías x 290g", 0, ""],
        ["Finlandia Light x 180g", 7, ""],
        ["Finlandia Clásico x 180g", 6, ""],
        ["Finlandia Red Calorías x 180g", 6, ""],
        ["Queso Rallado 35g", 80, ""],
        ["Queso Rallado 70g", 25, "11/10"],
        ["Leche Larga Vida LS Entera", 8, ""],
        ["Leche Larga Vida LS Descremada", 7, ""]
    ],
    "Tapamanía": [
        ["Tapas Empanadas Freír x 330g", 45, ""],
        ["Tapas Empanadas Criolla x 330g", 80, ""],
        ["Tapas Empanadas Horno x 330g", 45, ""],
        ["Tapas Pascualina Criolla x 400g", 5, ""],
        ["Tapas Pascualina Horno x 400g", 10, ""],
        ["Tapas Empanadas Súper Horno x 500g", 32, ""],
        ["Tapas Empanadas Súper Criolla x 500g", 36, ""],
        ["Tapas Empanadas Súper Tubo x 2kg Horno", 14, ""],
        ["Tapas Empanadas Súper Tubo x 2kg Criolla", 20, ""],
        ["Ravioles Blíster Pollo y Verdura x 500g", 0, "Cambio: 1"],
        ["Ravioles Blíster Jamón y Ricota x 500g", 13, "Cambio: 5"],
        ["Ravioles Blíster Verdura x 500g", 8, "Cambio: 3"],
        ["Ravioles Blíster 4 Quesos x 500g", 25, ""],
        ["Ravioles Bolsa Verdura x 1kg", 8, ""],
        ["Ravioles Bolsa Pollo y Verdura x 1kg", 15, ""],
        ["Ravioles Bolsa 4 Quesos x 1kg", 25, ""],
        ["Ravioles Bolsa Ricota y Jamón x 1kg", 15, ""],
        ["Ñoquis Blíster x 500g", 6, ""],
        ["Ñoquis Bolsa x 1kg", 11, ""]
    ],
    "Pan Baires Pan": [
        ["Multicereal", 29, "16/10"],
        ["Salvado", 27, "18/10"],
        ["Blanco", 17, "16/10"],
        ["Hamburguesa", 25, "25/09"]
    ]
}

# Buscador rápido
busqueda = st.text_input("🔍 Buscar producto rápido:", placeholder="Escribe 'barra', 'manteca', 'ravioles'...")

proveedores = list(datos_stock.keys())
tabs = st.tabs(proveedores)

for idx, prov in enumerate(proveedores):
    with tabs[idx]:
        df = pd.DataFrame(datos_stock[prov], columns=["Producto", "Cantidad", "Vencimiento / Notas"])
        
        if busqueda:
            df = df[df["Producto"].str.contains(busqueda, case=False, na=False)]
            
        st.data_editor(
            df,
            key=f"editor_{prov}",
            num_rows="dynamic",
            use_container_width=True
        )