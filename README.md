# Minecraft mob data analysis

This project combines data science with Minecraft by scraping and analyzing mob data from Minecraft Wiki. It focuses on mob drops and damage statistics to uncover new findings in mob values. 

# Files

# Code files
- `minecraft_drops.py` - Python script that scrapes:
  - Mob drop rates
  - Mob health points
  - Damage values
  - Spawn conditions
- `BLOG.ipynb` - Jupyter Notebook containing:
  - Data overview
  - Methodology
  - Visualization & Analysis
  - Limitations
  - Applications

# Data Files
- `passive_mobs.csv` - Peaceful mobs (cows, pigs, sheep)
- `neutral_mobs.csv` - Mobs that attack when provoked (endermen, spiders)
- `hostile_mobs.csv` - Aggressive mobs (zombies, creepers)
- `mob_damage.csv` - Damage values and attacks

# Requirements
To run this project, you will need:
- Python
- Chrome browser & ChromeDriver

# Setup Instructions

1. Install requirements:
pip install requests beautifulsoup4 pandas matplotlib jupyter

2. Run the scraper:
python minecraft_drops.py

3. Launch the analysis notebook
jupyter notebook BLOG.ipynb