import time
import requests
import csv
from bs4 import BeautifulSoup
from rich.console import Console
from rich.table import Table


headers = {
    'User-Agent': 'UIUC-IS310-WebScrape-Assignment/1.0 (itsoctane@proton.me)',
    'Accept-Encoding': 'gzip'
}
cs_major_csv = 'CS_Major.csv'
console = Console()

def scrape_tournament_data():
    url = "https://en.wikipedia.org/wiki/Counter-Strike_Major_Championships"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table', {'class': 'wikitable'})
        data = []

        for row in table.find_all('tr')[1:]:  # Skip the header row
            columns = row.find_all('td')
            if len(columns) > 0:
                tournament = columns[0].get_text(strip=True)
                date = columns[1].get_text(strip=True)
                organizer = columns[2].get_text(strip=True)
                host_city = columns[3].get_text(strip=True)
                winners = columns[4].get_text(strip=True)
                finals_result = columns[5].get_text(strip=True)

                data.append((tournament, date, organizer, host_city, winners, finals_result))
                time.sleep(2)
        return data
    else:
        print(f'Error fetching the page: {response.status_code}')
        return []

def write_to_csv(data):
    with open(cs_major_csv, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Tournament', 'Date', 'Organizer', 'Host City', 'Winners', 'Finals Result'])
        writer.writerows(data)

def scrape_html_related_data():
    console.print("Performing HTML-related requests...")

def display_data(data):
    table = Table(title="Counter-Strike Major Championships")
    table.add_column("Tournament", style="cyan")
    table.add_column("Date", style="magenta")
    table.add_column("Organizer", style="yellow")
    table.add_column("Host City", style="green")
    table.add_column("Winners", style="blue")
    table.add_column("Finals Result", style="bright_red")

    for entry in data:
        table.add_row(*entry)

    console.print(table)

# Main execution
tournament_data = scrape_tournament_data()
if tournament_data:
    write_to_csv(tournament_data)
    display_data(tournament_data)

scrape_html_related_data()
