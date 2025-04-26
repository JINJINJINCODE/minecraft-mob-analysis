import re
import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def setup_driver(chromedriver_path="/Users/jay/Desktop/chromedriver"):
    """Setup and return a Chrome webdriver"""
    service = Service(chromedriver_path)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    return webdriver.Chrome(service=service, options=options)

def get_soup_from_url(url, wait_time=5):
    """Get BeautifulSoup object from a URL"""
    driver = setup_driver()
    driver.get(url)
    time.sleep(wait_time)
    soup = BeautifulSoup(driver.page_source, "lxml")
    driver.quit()
    return soup

def clean_mob_name(name):
    """Clean mob names from wiki formatting"""
    return re.sub(r'\[.*?\]|\u200b|edit', '', str(name)).strip()

def scrape_mob_drops():
    """Scrape mob drops data from Minecraft Wiki"""
    print("Scraping mob drops data...")
    url = "https://minecraft.wiki/w/Drops#Mob_drops"
    soup = get_soup_from_url(url)
    
    # Find all tables
    tables = soup.find_all("table", {"class": "wikitable"})
    print(f"Found {len(tables)} tables.")
    
    # Preview the first few tables (for debugging)
    for i, table in enumerate(tables[1:4]):
        df = pd.read_html(str(table))[0]
        print(f"\n--- Table {i} ---")
        print(df.head())
    
    # Extract and clean data
    passive_df = pd.read_html(str(tables[1]))[0]
    neutral_df = pd.read_html(str(tables[2]))[0]
    hostile_df = pd.read_html(str(tables[3]))[0]
    
    # Clean mob names in all dataframes
    for df in [passive_df, neutral_df, hostile_df]:
        if 'Mob' in df.columns:
            df['Mob'] = df['Mob'].apply(clean_mob_name)
    
    # Save to CSV
    passive_df.to_csv("passive_mobs.csv", index=False)
    neutral_df.to_csv("neutral_mobs.csv", index=False)
    hostile_df.to_csv("hostile_mobs.csv", index=False)
    print("Mob drops data saved to CSV files")

def scrape_mob_damage():
    """Scrape mob damage data from Minecraft Wiki"""
    print("Scraping mob damage data...")
    url = "https://minecraft.wiki/w/Mob#Damage_dealt_by_mobs"
    soup = get_soup_from_url(url)
    
    # Find the damage table using the 'data-description' attribute
    damage_table_tag = soup.find("table", attrs={"data-description": "Mob damage by difficulty"})
    
    # Read it into a pandas dataframe
    damage_df = pd.read_html(str(damage_table_tag))[0]
    
    # Flatten columns if multi-level
    if isinstance(damage_df.columns, pd.MultiIndex):
        damage_df.columns = [' '.join(col).strip() for col in damage_df.columns]
    
    print("Columns:", damage_df.columns)
    
    # Clean mob names
    damage_df["Mob Mob"] = damage_df["Mob Mob"].apply(clean_mob_name)
    
    # Save to CSV
    damage_df.to_csv("mob_damage.csv", index=False)
    print("Mob damage data saved to CSV file")

def main():
    # Scrape both datasets
    scrape_mob_drops()
    scrape_mob_damage()
    print("All data saved :)")

if __name__ == "__main__":
    main()