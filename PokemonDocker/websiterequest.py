import requests

def search_pokemon(pokemon_name):
    # Make a GET request to the PokeAPI with the specified Pokemon name
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}'
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the response content to a dictionary
        pokemon_data = response.json()

        # Extract the desired information from the Pokemon data
        name = pokemon_data['name']
        pokemon_id = pokemon_data['id']
        types = [type_data['type']['name'] for type_data in pokemon_data['types']]
        abilities = [ability_data['ability']['name'] for ability_data in pokemon_data['abilities']]
        # Additional information can be extracted as needed

        # Print the extracted information
        print(f"Name: {name}")
        print(f"ID: {pokemon_id}")
        print(f"Types: {', '.join(types)}")
        print(f"Abilities: {', '.join(abilities)}")
        # Additional information can be printed as needed
    else:
        print("Error! Pokemon not found.")

# Prompt the user for a Pokemon name to search for
pokemon_name = 'pikachu'#input("Enter Pokemon name: ")

# Call the search_pokemon function with the user input
search_pokemon(pokemon_name)
