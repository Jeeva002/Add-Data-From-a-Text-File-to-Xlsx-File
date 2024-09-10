# Add-Data-From-a-Text-File-to-Xlsx-File

This script is designed to convert log files into an Excel spreadsheet. It reads a log file with a specific format, parses the entries, and saves the results into an Excel file for easy analysis.

Requirements
Python 3.x
pandas library
xlsxwriter library
You can install the required libraries using pip:



pip install pandas xlsxwriter

Script Overview

parse_log_line(line): Extracts timestamp, category, and message from a single log line using regular expressions.
log_to_dataframe(log_file_path): Reads the log file, parses each line, and creates a DataFrame.
save_to_excel(dataframe, excel_file_path): Saves the DataFrame to an Excel file.

How to Use
1)Set File Paths

Update the file paths for the input log file and the output Excel file in the script

2)Run the Script

Execute the script using Python

python Txt_2_Xlsx.py


Check the Output

After running the script, the data will be written to the specified Excel file. You can open it with any spreadsheet application to view and analyze the log entries.

Regular Expressions
This script uses Python's re module to parse log lines. For more information on regular expressions and how they work, you can refer to 
https://www.w3schools.com/python/python_regex.asp this tutorial on the re module.

Example Log Line Format
The script expects log lines to be in the following format:

YYYY-MM-DD HH:MM:SS.mmm - CATEGORY - Message content

For example:

2024-09-10 15:42:30.123 - INFO - This is a sample log message.
