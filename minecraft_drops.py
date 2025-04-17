from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd
import time
import re

# Setup Chrome driver path
service = Service("/Users/jay/Desktop/chromedriver")  # <-- change path if needed

# Launch browser
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # don't open a visible window
driver = webdriver.Chrome(service=service, options=options)

# Load the page and wait
url = "https://minecraft.wiki/w/Drops#Mob_drops"
driver.get(url)
time.sleep(5)  # wait for JavaScript to finish loading

# Get full HTML and parse
soup = BeautifulSoup(driver.page_source, "lxml")
driver.quit()

# Find all tables
tables = soup.find_all("table", {"class": "wikitable"})
print(f"Found {len(tables)} tables.")

# Preview the first few tables
for i, table in enumerate(tables[1:4]):
    df = pd.read_html(str(table))[0]
    print(f"\n--- Table {i} ---")
    print(df.head())

# Convert to DataFrames and clean
def clean_mob_name(name):
    """Clean mob names from wiki formatting"""
    return re.sub(r'\[.*?\]|\u200b|edit', '', name).strip()

# Assuming tables 1-3 are passive, neutral, hostile (verify this)
passive_df = pd.read_html(str(tables[1]))[0]
neutral_df = pd.read_html(str(tables[2]))[0]
hostile_df = pd.read_html(str(tables[3]))[0]

# Clean mob names
for df in [passive_df, neutral_df, hostile_df]:
    if 'Mob' in df.columns:
        df['Mob'] = df['Mob'].apply(clean_mob_name)

# Save to CSV
passive_df.to_csv("passive_mobs.csv", index=False)
neutral_df.to_csv("neutral_mobs.csv", index=False)
hostile_df.to_csv("hostile_mobs.csv", index=False)

print("Data saved to CSV files!")


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd
import time
import re

# Setup Chrome driver
service = Service("/Users/jay/Desktop/chromedriver")  # Update path if needed
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(service=service, options=options)

# Load the Mob page
url = "https://minecraft.wiki/w/Mob#Damage_dealt_by_mobs"
driver.get(url)
time.sleep(5)

# Get the page source and parse
soup = BeautifulSoup(driver.page_source, "lxml")
driver.quit()

# ✅ Find the damage table using the 'data-description' attribute
damage_table_tag = soup.find("table", attrs={"data-description": "Mob damage by difficulty"})

# Read it into a pandas DataFrame
damage_df = pd.read_html(str(damage_table_tag))[0]

# Flatten columns if multi-level
if isinstance(damage_df.columns, pd.MultiIndex):
    damage_df.columns = [' '.join(col).strip() for col in damage_df.columns]

# Confirm column names
print("Columns:", damage_df.columns)

# Clean mob names
damage_df["Mob Mob"] = damage_df["Mob Mob"].astype(str).str.replace(r'\[.*?\]|\u200b|edit', '', regex=True).str.strip()

# Save to CSV
damage_df.to_csv("mob_damage.csv", index=False)
print("✅ Mob damage data saved to mob_damage.csv")

