[![Hits-of-Code](https://hitsofcode.com/github/l0mbart/juniper-temperature-environment-sensor?branch=main)](https://hitsofcode.com/github/l0mbart/juniper-temperature-environment-sensor/view?branch=main)
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FL0mbart%2Fjuniper-temperature-environment-sensor&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com) 

# Juniper Temperature Data Logger

This is a Python script that retrieves temperature data that isn't monitored by NMS systems like Observium, Zabbix, PRTG, etc., from Juniper devices and logs it to an Excel file. The script connects to the Juniper device via SSH, parses the output to extract temperature data, and saves it to an Excel file with a timestamp every 15 minutes.

## Requirements

Before running the script, you need to install the following packages:

- `paramiko` for SSH communication
- `pandas` for managing data and writing to Excel files
- `openpyxl` for writing to Excel files

You can install these packages using `pip`:

```bash
pip install paramiko pandas openpyxl
```
## How to Use
Configure the Script
Open the juniper_chassis_env.py file and update the following configuration parameters:

```
hostname = 'replace_with_juniper_device_IP'
port = 22 # change this if needed
username = 'juniper_device_username'
password = 'juniper_device_password'
```
Replace the IP, username, password, and port with your Juniper device's details.

## Run the Script
Execute the script with Python:
```
python juniper_chassis_env.py
```

The script will connect to the Juniper device, retrieve temperature data, and save it to an Excel file in the myproject directory. The file will be named in the format YYYY-MM-DD_juniper_chassis_env.xlsx, where YYYY-MM-DD is the current date.

## File Structure
juniper_chassis_env.py - The main script that handles data retrieval and logging.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
paramiko for SSH communication
pandas for managing data and writing to Excel files
openpyxl for writing to Excel files
crontab - Contains the configuration for running the script at regular intervals.

iseng2.id
