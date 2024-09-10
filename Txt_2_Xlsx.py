import pandas as pd
import re

def parse_log_line(line):
    # Regular expression to extract timestamp, category, and message
    match = re.match(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3}) - (\w+) - (.*)', line)
    if match:
        timestamp, category, message = match.groups()
        return timestamp, category, message
    return None, None, None

def log_to_dataframe(log_file_path):
    data = {'Timestamp': [], 'Category': [], 'Message': []}
    
    with open(log_file_path, 'r') as file:
        for line in file:
            timestamp, category, message = parse_log_line(line.strip())
            if timestamp:
                data['Timestamp'].append(timestamp)
                data['Category'].append(category)
                data['Message'].append(message)
    
    return pd.DataFrame(data)

def save_to_excel(dataframe, excel_file_path):
    with pd.ExcelWriter(excel_file_path, engine='xlsxwriter') as writer:
        dataframe.to_excel(writer, index=False, sheet_name='Logs')

# Path to the input text file and output Excel file
log_file_path = '/home/atre/spacemouseTeleoperation/src/doosan-robot/dsr_example/py/scripts/spaceMouse/collectedData.txt'  # Change this to your log file path
excel_file_path = '/home/atre/spacemouseTeleoperation/src/doosan-robot/dsr_example/py/scripts/spaceMouse/outputfile.xlsx'  # Change this to your desired output file path

# Convert log file to DataFrame and save to Excel
df = log_to_dataframe(log_file_path)
save_to_excel(df, excel_file_path)

print(f"Data has been successfully written to {excel_file_path}")
