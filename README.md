# ATP Tennis Analysis

Python-based tennis analytics project that scrapes ATP player and match data from public tennis statistics websites for analysis and visualization.

## Goals

- Scrape player profile links
- Extract player statistics
- Build structured datasets
- Analyze ATP performance trends
- Explore machine learning applications in tennis analytics
- Visualize data
- insights based on the following factors:
  - temperature [ does the temperature affect the player's performance ], 
  - wins leading up to the match [ momentum ],
  - loss leading up to the match [ momentum ] 
  - wins on that surface in that year [ specialization on surface ]
  - average player beaten ranks [ did they face tough competition ]
  - respective players win streak [ do they get tired ]
  - Distance travelled from tournement to tournement [ does travelling, making them tired, affect their performance]
  - size of team [ does the size of the team affect the player's performance 
  - age of player [ does the age of the player affect the player's performance]
  - ball used ( traits " fast " , "slow" )
  - home crowd advantage
  - ``

## Tech Stack

- Python
- BeautifulSoup
- Requests
- Pandas
- SQLite

## Project Structure

- `scraper.py` → web scraping logic
- `parser.py` → data cleaning/parsing
- `database.py` → database storage
- `notebooks/` → experimentation and analysis

## Data URLS and Sources Apps Used
- https://www.tennisabstract.com/
- https://streamlit.io/#install
- 