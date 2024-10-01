# Nama file: juniper_graph_env.py 

import os
import pandas as pd
import plotly.graph_objs as go
import plotly.io as pio
from datetime import datetime

# Ambil tanggal saat ini
current_date = datetime.now().strftime("%Y-%m-%d")

# Path ke file Excel dan file output
file_path = f"/home/noc/myproject/{current_date}_juniper_chassis_env.xlsx"
output_file = f"/home/noc/myproject/sensor_temperature_graph_{current_date}.html"

# Pastikan file Excel ada
if not os.path.exists(file_path):
    raise FileNotFoundError("File Excel tidak ditemukan.")

# Jalankan kode utama
df = pd.read_excel(file_path, index_col=0)

fig = go.Figure()
for sensor_name in df.columns:
    fig.add_trace(go.Scatter(x=df.index, y=df[sensor_name], mode='lines', name=sensor_name))

fig.update_layout(
    title="Sensor Temperature Over Time",
    xaxis_title="Timestamp",
    yaxis_title="Temperature (Â°C)",
    legend_title="Sensor",
    template="plotly_dark"
)

# Simpan grafik sebagai file HTML
pio.write_html(fig, file=output_file)

# Cek apakah file HTML sudah terbentuk
if not os.path.exists(output_file):
    raise FileNotFoundError("File grafik HTML tidak berhasil dibuat.")

print(f"Grafik berhasil disimpan di {output_file}")
