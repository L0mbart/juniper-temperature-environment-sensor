# Nama file: juniper_graph_env.py

import os
import pandas as pd
import plotly.graph_objs as go
import plotly.io as pio

def test_plotly_graph_creation():
    # Path ke file Excel dan file output
    file_path = "/home/myproject/2024-09-03_juniper_chassis_env.xlsx"
    output_file = "/home/myproject/sensor_temperature_graph_2024-09-03.html"

    # Pastikan file Excel ada
    assert os.path.exists(file_path), "File Excel tidak ditemukan."

    # Jalankan kode utama (copy-paste dari script)
    df = pd.read_excel(file_path, index_col=0)
    
    fig = go.Figure()
    for sensor_name in df.columns:
        fig.add_trace(go.Scatter(x=df.index, y=df[sensor_name], mode='lines', name=sensor_name))

    fig.update_layout(
        title="Sensor Temperature Over Time",
        xaxis_title="Timestamp",
        yaxis_title="Temperature (°C)",
        legend_title="Sensor",
        template="plotly_dark"
    )
    
    # Simpan grafik sebagai file HTML
    pio.write_html(fig, file=output_file)

    # Cek apakah file HTML sudah terbentuk
    assert os.path.exists(output_file), "File grafik HTML tidak berhasil dibuat."

    # Baca file HTML untuk memastikan grafik terbentuk dengan benar
    with open(output_file, 'r') as f:
        html_content = f.read()

    # Pastikan file HTML berisi data Plotly
    assert "plotly" in html_content, "File HTML tidak berisi grafik Plotly."
