
import os
import csv
import xml.etree.ElementTree as ET
from tqdm import tqdm
import pandas as pd

#XML parsing
def find_information(xml_file_path, *target_elements):
    try:
        # Parse the XML file
        with open(xml_file_path, 'rb') as file:
            tree = ET.parse(file)

        root = tree.getroot()

        # Initialize variables to store information
        info = [None] * len(target_elements)

        # Search for each target element
        for i, target_element in enumerate(target_elements):
            for element in root.iter(target_element):
                info[i] = element.text

        # Return "NaN" for missing values
        return tuple(val if val is not None else "NaN" for val in info)

    except ET.ParseError:
        # Handle the case where the XML file is not well-formed
        print(f"Error parsing XML file: {xml_file_path}")
        return tuple("NaN" for _ in target_elements)

    except Exception as e:
        # Handle other exceptions
        print(f"Error processing XML file {xml_file_path}: {str(e)}")
        return tuple("NaN" for _ in target_elements)

def process_folders(root_folder, output_csv_path, *target_elements):
    # Open the CSV file for writing
    with open(output_csv_path, 'w', newline='', encoding='utf-8') as csv_file:
        # Create a CSV writer object
        csv_writer = csv.writer(csv_file)

        # Write headers to the CSV file
        csv_headers = ['NCT number'] + [f'Target Element {i}' for i in range(1, len(target_elements) + 1)]
        csv_writer.writerow(csv_headers)

        # Iterate through all folders in the root folder
        for folder_name in os.listdir(root_folder):
            folder_path = os.path.join(root_folder, folder_name)

            # Check if the item in the root folder is a directory
            if os.path.isdir(folder_path):
                # Call the function to process XML files in the current folder
                process_folder(folder_path, csv_writer, *target_elements)

def process_folder(folder_path, csv_writer, *target_elements):
    # Get the list of XML files in the specified folder
    xml_files = [filename for filename in os.listdir(folder_path) if filename.endswith(".xml")]

    # Use tqdm to create a progress bar for file-by-file progress
    with tqdm(total=len(xml_files), desc=f"Processing XML files in {os.path.basename(folder_path)}") as pbar:
        # Iterate through all files in the specified folder
        for filename in xml_files:
            # Extract NCT number from the XML file name
            nct_number = os.path.splitext(filename)[0]

            # Construct the full path to the XML file
            xml_file_path = os.path.join(folder_path, filename)

            # Call the function to find information in the current XML file
            info = find_information(xml_file_path, *target_elements)

            # Write the results to the CSV file
            csv_writer.writerow([nct_number] + list(info))

            # Update the tqdm progress bar for the current file
            pbar.update()


root_folder = r'F:\...\AllPublicXML'
output_csv_path = 'df_xml_parsed_final.csv'
target_elements = [
    'sharing_ipd',
    'ipd_description',
    'ipd_access_criteria',
    'ipd_time_frame',
    'condition',
    'study_type',
    'primary_purpose',
    'start_date',
    'study_first_posted',
    'last_update_posted',
    'overall_status',
    'verification_date',
    'country'

]

# Call the function to process all folders and their XML files
process_folders(root_folder, output_csv_path, *target_elements)

#Rename the columns as they are Target Element list
df_f = pd.read_csv(r'G:\.....\df_xml_parsed_final.csv')
df_f.describe()
# Rename columns
new_column_names = {
    'Target Element 1': 'IPD Check',
    'Target Element 2': 'IPD Description',
    'Target Element 3': 'IPD Access Criteria',
    'Target Element 4': 'IPD Time Frame',
    'Target Element 5': 'Condition',
    'Target Element 6': 'Study Type',
    'Target Element 7': 'Primary Purpose',
    'Target Element 8': 'Start Date',
    'Target Element 9': 'Study First Posted',
    'Target Element 10':'Last Update Posted',
    'Target Element 11':'Overall Status',
    'Target Element 12':'Verification Date',
    'Target Element 13':'Country'}
df_f.rename(columns=new_column_names, inplace=True)

df_f.to_csv(r'F:\.....\Clinicaltrials.csv', index=False)

