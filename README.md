# Minecraft mob data analysis

A project that scrapes Minecraft mob data and analyzes their behaviors.

# Files

# Code files
- `minecraft_drops.py` - Python script that scrapes:
  - Mob drop rates
  - Mob health points
  - Damage values
  - Spawn conditions
- `BLOG.ipynb` - Jupyter Notebook containing:
  - Data cleaning steps
  - Visualization of mob statistics
  - Comparative analysis

# Data Files
- `passive_mobs.csv` - Peaceful mobs (cows, pigs, sheep)
- `neutral_mobs.csv` - Mobs that attack when provoked (endermen, spiders)
- `hostile_mobs.csv` - Always aggressive mobs (zombies, creepers)
- `mob_damage.csv` - Damage values and attack patterns

# Setup Instructions

1. Install requirements:
```bash
pip install requests beautifulsoup4 pandas matplotlib jupyter

2. Run the scraper:
python minecraft_drops.py

3. Launch the analysis notebook
jupyter notebook BLOG.ipynb
