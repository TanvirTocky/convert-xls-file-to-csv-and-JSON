import pandas as pd

def excel_to_csv_all_sheets():
    excel_path = r"C:\Users\Tanvir Tocky\Desktop\practice.xlsx"
    output_folder = r"C:\Users\Tanvir Tocky\Desktop"

    # Load the Excel file
    xls = pd.ExcelFile(excel_path)

    # Loop through each sheet and save as CSV
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(excel_path, sheet_name=sheet_name)
        csv_path = f"{output_folder}\\{sheet_name}.csv"
        df.to_csv(csv_path, index=False)
        print(f"Saved '{sheet_name}' as CSV at: {csv_path}")

# Run the function
excel_to_csv_all_sheets()
