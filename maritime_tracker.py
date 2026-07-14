from datetime import datetime

def generate_maritime_poc_data():
    return [
        {"Vessel_Name": "Kapitan Maslov", "IMO_Number": "9130145", "Current_Status": "In Transit", "Origin_Port": "Chennai (IN)", "Destination_Port": "Vladivostok (RU)", "Est_Arrival": "2026-07-28"},
        {"Vessel_Name": "FESCO Moneron", "IMO_Number": "9274355", "Current_Status": "Loading", "Origin_Port": "Mumbai (IN)", "Destination_Port": "Vladivostok (RU)", "Est_Arrival": "2026-08-05"},
        {"Vessel_Name": "Vladivostok Express", "IMO_Number": "9742156", "Current_Status": "Arrived", "Origin_Port": "Chennai (IN)", "Destination_Port": "Vladivostok (RU)", "Est_Arrival": "2026-07-12"}
    ]

def generate_markdown_report(data):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Build Markdown header
    markdown_content = "## ⚓ Chennai-Vladivostok Eastern Maritime Corridor (EMC) Tracker\n\n"
    markdown_content += "**Automated Daily Operational Report — Daytraa Business Solutions**\n\n"
    markdown_content += f"*System Status: Active PoC | Last Automated Scan: {timestamp} IST*\n\n"
    markdown_content += "### Live Vessel Positioning\n\n"
    
    # Build Native Markdown Table
    markdown_content += "| Vessel Name | IMO Number | Current Status | Origin Port | Destination Port | Est Arrival |\n"
    markdown_content += "| :--- | :--- | :--- | :--- | :--- | :--- |\n"
    
    for row in data:
        markdown_content += f"| {row['Vessel_Name']} | {row['IMO_Number']} | {row['Current_Status']} | {row['Origin_Port']} | {row['Destination_Port']} | {row['Est_Arrival']} |\n"
        
    markdown_content += "\n\n---\n*This intelligence agent is deployed via GitHub Actions for continuous macro-economic supply chain monitoring.*"
    
    with open("README.md", "w") as f:
        f.write(markdown_content)

if __name__ == "__main__":
    freight_data = generate_maritime_poc_data()
    generate_markdown_report(freight_data)
