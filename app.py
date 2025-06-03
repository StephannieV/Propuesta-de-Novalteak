import pandas as pd
import os

# Crear un directorio relativo (en el directorio actual del script)
output_dir = "csv_datos_canada"
os.makedirs(output_dir, exist_ok=True)

# Datos preparados para cada categoría
datos = {
    "inclusion_sector_verde": {
        "Variables": [
            "Inversión gubernamental (USD)",
            "Tasa de crecimiento proyectada (2025-2029)",
            "Crecimiento previo (2020-2024)"
        ],
        "Valores": [
            903.5,
            "3.2%",
            "5.8%"
        ]
    },
    "importacion_madera": {
        "Variables": [
            "Reducción de envíos 2021-2023 (millones m³)",
            "Producción en marzo 2024 (millones m³)",
            "Importaciones desde EE.UU. en 2024 (millones m³)"
        ],

