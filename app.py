import pandas as pd
import os
import tempfile

# Crear un directorio temporal seguro para guardar los archivos CSV
output_dir = tempfile.mkdtemp()

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
        "Valores": [
            7.5,
            4.8,
            28.1
        ]
    },
    "industria_mueble_valor": {
        "Año": [2024, 2025, 2029],
        "Valor (USD mil millones)": [17.81, 20.08, 23.62]
    },
    "muebles_lujo_sostenibles": {
        "Variable": ["Crecimiento e-commerce durante pandemia", "CAGR proyectada (2025-2034)"],
        "Valor": ["191%", "4.90%"]
    },
    "ecommerce_muebles_personalizados": {
        "Variable": ["Proporción en tienda 2025", "Proporción en línea 2025", "Crecimiento durante pandemia"],
        "Valor": ["69%", "31%", "191%"]
    },
    "ventas_madera_tropical": {
        "Variable": [
            "Crecimiento mercado productos madera (2025-2029)",
            "Valor mercado muebles lujo 2030 (USD millones)",
            "CAGR muebles lujo (2025-2030)"
        ],
        "Valor": ["1.22%", 797.4, "4.5%"]
    },
    "penetracion_zonas": {
        "Variable": [
            "Ranking exportador mundial",
            "Proyección ingresos mercado 2030 (USD millones)",
            "CAGR (2023-2030)"
        ],
        "Valor": ["5to", 40568.0, "6%"]
    },
    "penetracion_aplicacion_final": {
        "Sector": ["Residencial", "Exterior", "Comercial"],
        "Valor proyectado (USD millones)": [26160, 211.82, None],
        "Notas": [
            "CAGR 2025-2030: 5.43%",
            None,
            "Impulsado por demanda de oficinas y sector comercial"
        ]
    },
    "ventas_por_necesidad_cliente": {
        "Segmento": ["Lujo", "General madera", "General Canadá"],
        "Valor 2025 (USD mil millones)": [25.28, 120.15, None],
        "Valor 2032-2033 (USD mil millones)": [37.34, 176.30, 23.62],
        "CAGR estimada": [None, "4.91%", "3.95%"]
    }
}


