import requests
import random


def print_response(response, label):
    if response.status_code == 200:
        print(label)
        print(response.json())
    else:
        print(f"Error: {response.status_code} - {response.text}")

def get_api_data(url):
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None


def save_to_file(data, filename):
    with open(filename, "w") as file:
        file.write(str(data))


post_id = 1 
response = requests.get(f"https://jsonplaceholder.typicode.com/todos/{post_id}")
print_response(response, "Response content:")


class ToDo:
    def __init__(self, userId, id, title, completed):
        self.userId = userId
        self.id = id
        self.title = title
        self.completed = completed


new_todo = ToDo(userId=1, id=post_id, title="Sample Title", completed=False)


post_response = requests.post("https://jsonplaceholder.typicode.com/todos", json=new_todo.__dict__)
print_response(post_response, "Post Response content:")


new_todo.title = "Updated Title"


put_payload = new_todo.__dict__
chosen_id = 1  
put_response = requests.put(f"https://jsonplaceholder.typicode.com/todos/{chosen_id}", json=put_payload)
print_response(put_response, "Put Response content:")


random_character_id = random.randint(1, 826)
character_data = get_api_data(f"https://rickandmortyapi.com/api/character/{random_character_id}")
print_response(character_data, "Random Character JSON response:")


if character_data:
    print("Keys in the JSON structure:")
    print(character_data.keys())


if character_data:
    save_to_file(character_data, f"info_character_{random_character_id}.json")


if character_data:
    episode_urls = character_data.get("episode", [])
    episode_ids = [url.split("/")[-1] for url in episode_urls]
    save_to_file(episode_ids, f"all_episodes_with_character_{random_character_id}.txt")


episode_1_data = get_api_data("https://rickandmortyapi.com/api/episode/1")
print_response(episode_1_data, "Episode 1 Response Structure:")


class Episode:
    def __init__(self, id, name, air_date, episode, characters, url):
        self.id = id
        self.name = name
        self.air_date = air_date
        self.episode = episode
        self.characters = characters
        self.url = url

    def get_episode_info(self):
        return f"Episode {self.episode}: {self.name} - Air date: {self.air_date}"


episodes_data = [get_api_data(f"https://rickandmortyapi.com/api/episode/{episode_id}") for episode_id in episode_ids]


for episode_data in episodes_data:
    episode = Episode(**episode_data)
    print(episode.get_episode_info())


character_1_data = get_api_data("https://rickandmortyapi.com/api/character/1")
print_response(character_1_data, "Character 1 Response Structure:")


class Character:
    def __init__(self, id, name, status, species, gender, origin, location, image, episode_urls):
        self.id = id
        self.name = name
        self.status = status
        self.species = species
        self.gender = gender
        self.origin = origin
        self.location = location
        self.image = image
        self.episode_urls = episode_urls

    def get_character_info(self):
        return f"{self.name} - {self.status} - Species: {self.species} - Gender: {self.gender}"


character_1 = Character(**character_1_data)


if character_1:
    print(character_1.get_character_info())