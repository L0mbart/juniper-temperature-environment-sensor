import paramiko
import re
import pandas as pd
from datetime import datetime
import os

# SSH connection configuration
hostname = 'IP_ADDRESS'
port = 22
username = 'USERNAME'
password = 'PASSWORD'

# Function to run a command on the Juniper device and get the output
def run_command():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, port, username, password)
    
    stdin, stdout, stderr = client.exec_command("show chassis environment | no-more")
    output = stdout.read().decode()
    client.close()
    return output

# Regular expression pattern to capture temperature in Celsius
pattern = r'\s+OK\s+(\d+)\s+degrees\s+C\s+/\s+\d+\s+degrees\s+F'

# Function to process each line of the output
def process_line(line):
    match = re.search(pattern, line)
    if match:
        temp_celsius = match.group(1)
        # Remove the text before the temperature and add a tab before the temperature
        cleaned_line = re.sub(pattern, '', line).strip() + '\t' + temp_celsius
        return cleaned_line
    return line

# Function to process the output into a dictionary
def parse_output(output):
    sensor_data = {}
    lines = output.splitlines()
    for line in lines:
        cleaned_line = process_line(line)
        parts = cleaned_line.split('\t')
        if len(parts) == 2:
            sensor_name = parts[0].strip()
            temperature = parts[1].strip()
            sensor_data[sensor_name] = temperature
    return sensor_data

# Function to save data into an Excel file
def save_to_excel(sensor_data, file_path):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Check if the Excel file already exists
    if os.path.exists(file_path):
        df = pd.read_excel(file_path, index_col=0)
    else:
        # Initialize an empty DataFrame if the file doesn't exist
        df = pd.DataFrame()

    # Create a new DataFrame for the current data
    new_data = pd.DataFrame(sensor_data, index=[timestamp])

    # Combine the new DataFrame with the existing one
    if df.empty:
        df = new_data
    else:
        df = pd.concat([df, new_data])

    # Set the format of the DataFrame so that timestamps are rows and sensors are columns
    df.index.name = 'Timestamp'
    
    # Save the DataFrame to an Excel file
    df.to_excel(file_path)
    print(f"Data successfully saved to {file_path}")

# Path to the Excel file
today = datetime.now().strftime("%Y-%m-%d")
folder_path = "/home/myproject/"
excel_file_path = os.path.join(folder_path, f"{today}_juniper_chassis_env.xlsx")

# Run the functions
output = run_command()
sensor_data = parse_output(output)
save_to_excel(sensor_data, excel_file_path)
