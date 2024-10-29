import requests
import json
import os
from rich.prompt import Prompt
import pyeuropeana.apis as apis


def fetch_pokemon(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None


def search_europeana(pokemon_name, api_key):
    result = apis.search(
        query=pokemon_name,
        qf='(skos_concept:"http://data.europeana.eu/concept/base/48" AND TYPE:IMAGE)',
        reusability='open AND permission',
        media=True,
        thumbnail=True,
        landingpage=True,
        colourpalette='#0000FF',
        theme='photography',
        sort='europeana_id',
        profile='rich',
        rows=5,
        wskey=api_key
    )
    return result


def save_combined_data(pokemon_data, europeana_data, filename):
    combined_data = {
        "pokemon": pokemon_data,
        "europeana": europeana_data
    }
    with open(filename, 'w') as json_file:
        json.dump(combined_data, json_file, indent=4)
        print(f"Combined data saved to {filename}")


def delete_europeana_api_key():
    if 'EUROPEANA_API_KEY' in os.environ:
        del os.environ['EUROPEANA_API_KEY']
        print("Europeana API key has been deleted from environment variables.")
    else:
        print("No Europeana API key found in environment variables.")


def main():
    europeana_key = os.getenv('EUROPEANA_API_KEY')
    if not europeana_key:
        europeana_key = Prompt.ask("Please enter your Europeana API key")
    pokemon_name = Prompt.ask("Please enter the name of a Pokémon to search for (e.g., Pikachu)")
    
    pokemon_data = fetch_pokemon(pokemon_name) 
    if pokemon_data:
        pokemon_info = {
            "name": pokemon_data.get("name").capitalize(),
            "height": pokemon_data.get("height"),
            "weight": pokemon_data.get("weight"),
            "types": [type_info['type']['name'] for type_info in pokemon_data['types']]
        }
    else:
        print("Pokémon not found in PokeAPI.")
        pokemon_info = None

    europeana_data = search_europeana(pokemon_name, europeana_key)
    if pokemon_info and europeana_data:
        europeana_data.pop('api_key', None)
        save_combined_data(pokemon_info, europeana_data, f"{pokemon_info['name']}_combined_data.json")
    else:
        print("Could not save data as Pokémon data was not found or Europeana search failed.")


delete_europeana_api_key()
if __name__ == "__main__":
    main()
