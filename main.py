# Step 3.1: Fetch HTML Content
# Please be careful to follow instructions on how to run the program; 
# the Run menu or right-click > Run options do not work in the simulated environment. 
# Ensure you have run the terminal command to install the correct libraries using pip.
# You must use the terminal window as directed in Step 3.
import requests
from bs4 import BeautifulSoup

# Fetch the webpage content
url = "http://127.0.0.1:5500/baseball_stats.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Print the HTML content to inspect
print(soup.prettify())

# Step 3.2: Extract the Required Data
# Create the beautifulsoup object (already done above)
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3.2: Extract the Required Data
table_body = soup.find('tbody')
rows = table_body.find_all('tr')

games_data = []

for row in rows:
    cells = row.find_all('td')
    if len(cells) >= 7:  # Ensure the row has all 7 data columns
        game_info = {
            "GameID": cells[0].text.strip(),
            "Team 1": cells[1].text.strip(),
            "Team 2": cells[2].text.strip(),
            "Expected Runs (Team 1)": cells[3].text.strip(),
            "Expected Runs (Team 2)": cells[4].text.strip(),
            "Over/Under": cells[5].text.strip(),
            "Moneyline Favorite": cells[6].text.strip()
        }
        games_data.append(game_info)

# Print the extracted data to check it
print(games_data)


# Step 4.1: Convert to a DataFrame
# Import pandas
import pandas as pd

# Convert the game data into a pandas DataFrame
df = pd.DataFrame(games_data)

# Inspect the DataFrame
print(df.info())

# Save and print the shaped data
print(df)

# Step 5.1: Save to a CSV File
# Save the DataFrame to a CSV file named sports_statistics.csv
df.to_csv('sports_statistics.csv', index=False)