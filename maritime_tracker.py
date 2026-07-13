import pandas as pd
from datetime import datetime
import os

def generate_maritime_poc_data():
    # Proof of Concept (PoC) dataset representing live tracking parameters 
    # for the Eastern Maritime Corridor (EMC)
    corridor_vessels = [
        {"Vessel_Name": "Kapitan Maslov", "IMO_Number": "9130145", "Current_Status": "In Transit", "Origin_Port": "Chennai (IN)", "Destination_Port": "Vladivostok (RU)", "Est_Arrival": "2026-07-28"},
        {"Vessel_Name": "FESCO Moneron", "IMO_Number": "9274355", "Current_Status": "Loading", "Origin_Port": "Mumbai (IN)", "Destination_Port": "Vladivostok (RU)", "Est_Arrival": "2026-08-05"},
        {"Vessel_Name": "Vladivostok Express", "IMO_Number": "9742156", "Current_Status": "Arrived", "Origin_Port": "Chennai (IN)", "Destination_Port": "Vladivostok (RU)", "Est_Arrival": "2026-07-12"}
    ]
    
    df = pd.DataFrame(corridor_vessels)
    return df

def generate_markdown_report(df):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    markdown_content = "## ⚓ Chennai-Vladivostok Eastern Maritime Corridor (EMC) Tracker\n\n"
    markdown_content += "**Automated Daily Operational Report — Daytraa Business Solutions**\n\n"
    markdown_content += f"*System Status: Active PoC | Last Automated Scan: {timestamp} IST*\n\n"
    markdown_content += "### Live Vessel Positioning\n\n"
    markdown_content += df.to_markdown(index=False)
    markdown_content += "\n\n---\n*This intelligence agent is deployed via GitHub Actions for continuous macro-economic supply chain monitoring.*"
    
    with open("README.md", "w") as f:
        f.write(markdown_content)

if __name__ == "__main__":
    freight_data = generate_maritime_poc_data()
    generate_markdown_report(freight_data)
