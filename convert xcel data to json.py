import pandas as pd
import json

def excel_to_json_all_sheets():
    excel_path = r"C:\Users\Tanvir Tocky\Desktop\practice.xlsx"
    output_folder = r"C:\Users\Tanvir Tocky\Desktop"

    xls = pd.ExcelFile(excel_path)

    for sheet_name in xls.sheet_names:
        df = pd.read_excel(excel_path, sheet_name=sheet_name)
        json_path = f"{output_folder}\\{sheet_name}.json"
        df.to_json(json_path, orient="records", indent=4)
        print(f"✅ Saved '{sheet_name}' as JSON at: {json_path}")

# Run the function
excel_to_json_all_sheets()

