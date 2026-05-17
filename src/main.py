from scraper import get_match_links
import pandas as pd

#creating a dictionary
url = "https://www.tennisabstract.com/charting/"

matches = get_match_links(url)

print(f"Found {len(matches)} matches\n")

for match in matches[:20]:
    print(match["match_name"])
    print(match["link"])
    print()

#creating a dataframe
df_matches = pd.DataFrame(matches)
print(df_matches.head(2))