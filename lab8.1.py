import requests
import random


# 1.1: GET Request (эта облость кода реквестит get запрос к json Api
post_id = 1 
response = requests.get(f"https://jsonplaceholder.typicode.com/todos/{post_id}")

if response.status_code >= 400: # если статус рекуеста больше или равно 400 то означает то что что то пошло не так, ошибки могут быть по типу 404 то есть NOT FOUNG
    print(f"Error: {response.status_code} - {response.text}")
else:
    print("Response content:") # в противном случае если он находит и нет никаких проблем то он выводит ответ 
    print(response.json())

# 1.2 1.3: тут мы создаем класс todo в котором есть userId, id и тд чтобы в дальнейшем дать значение 
class ToDo:
    def __init__(self, userId, id, title, completed):
        self.userId = userId
        self.id = id
        self.title = title
        self.completed = completed


new_todo = ToDo(userId=1, id=post_id, title="Sample Title", completed=False) #Создается новый объект ToDo с заданными параметрами (userId, id, title, completed). Этот объект представляет собой задачу, которая будет отправлена на сервер.

# 1.4: POST Request Создается словарь new_todo_payload, который содержит данные о задаче (new_todo). Эти данные будут использованы в теле POST-запроса для создания новой задачи на сервере. 
new_todo_payload = {
    "userId": new_todo.userId,
    "id": new_todo.id,
    "title": new_todo.title,
    "completed": new_todo.completed
}

post_response = requests.post("https://jsonplaceholder.typicode.com/todos", json=new_todo_payload) # делаем post запрос

if post_response.status_code >= 400: # как и ранее если запрос пост прошел успешно то он выводится, если нет то показывается ошибка которая случилась
    print(f"Error: {post_response.status_code} - {post_response.text}")
else:
    print("Post Response content:")
    print(post_response.json())

# 1.5: 
new_todo.title = "Updated Title"

# 1.6: тут происходит запрос put, то есть обновление 
put_payload = {
    "userId": new_todo.userId,
    "id": new_todo.id,
    "title": new_todo.title,
    "completed": new_todo.completed
}

chosen_id = 2  #Этот идентификатор то есть в этом случае 2 будет использоваться для указания ресурса, по которому он обновит на сервере
put_response = requests.put(f"https://jsonplaceholder.typicode.com/todos/{chosen_id}", json=put_payload) # запрос put где учитывается chosen_id 

if put_response.status_code >= 400:
    print(f"Error: {put_response.status_code} - {put_response.text}")
else:
    print("Put Response content:")
    print(put_response.json())


                    #Task 2
                    
# Task 2.1:  тут запрос на рандомного персонажа с рика и морти, тут запрос гет и ссылка URL  через который мы получаем информацию
random_character_id = random.randint(1, 826)
character_response = requests.get(f"https://rickandmortyapi.com/api/character/{random_character_id}")

if character_response.status_code == 200: # 200 это озночает что он нашел то что мы искалии выводит, в противном случае он выведет ошибку то что не нашел или такого не существует 
    random_character_data = character_response.json()
    print("Random Character JSON response:")
    print(random_character_data)
else:
    print(f"Failed to fetch character with ID: {random_character_id}")

# Task 2.2: тут дата будет выходит в виде ключей которые мы указали выше 
if random_character_data:
    print("Keys in the JSON structure:")
    print(random_character_data.keys())

# Task 2.3: Save to File тут мы сохраняем результат в файл
if random_character_data:
    with open(f"info_character_{random_character_id}.json", "w") as file:
        file.write(str(random_character_data))

# Task 2.4: тут мы получаем лист епизодов 
if random_character_data:
    episode_urls = random_character_data.get("episode", [])
    episode_ids = [url.split("/")[-1] for url in episode_urls]
    with open(f"all_episodes_with_character_{random_character_id}.txt", "a") as file:
        for episode_id in episode_ids:
            file.write(f"https://rickandmortyapi.com/api/episode/{episode_id}\n")

# Task 2.5: Episode Response Structure тыт мы просим через запрос гет получить информацию именно про первый эпизод рика и морти
episode_1_response = requests.get("https://rickandmortyapi.com/api/episode/1")
if episode_1_response.status_code == 200:
    episode_1_data = episode_1_response.json()
    print("Episode 1 Response Structure:")
    print(episode_1_data)
else:
    print("Failed to fetch episode 1 data")

# Task 2.6: создаем класс эпизоды и библиоетку где входит название эпизода, ссылки и тд
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

# Task 2.7: Episode Data Retrieval
episodes_data = [] # пустой список в котором будут содержаться объекты классы episode 
for episode_id in episode_ids:
    episode_response = requests.get(f"https://rickandmortyapi.com/api/episode/{episode_id}") #выполняется запрос API для каждого идентификатора эпизода в списке episode_ids
    if episode_response.status_code == 200:
        episode_data = episode_response.json()
        episode = Episode(
            id=episode_data['id'],
            name=episode_data['name'],
            air_date=episode_data['air_date'],
            episode=episode_data['episode'],
            characters=episode_data['characters'],
            url=episode_data['url']
        )
        episodes_data.append(episode)
    else:
        print(f"Failed to fetch episode with ID: {episode_id}")

# Task 2.8: метод для ввывода 
for episode in episodes_data:
    print(episode.get_episode_info())

# Task 2.9: 
character_1_response = requests.get("https://rickandmortyapi.com/api/character/1")
if character_1_response.status_code == 200:
    character_1_data = character_1_response.json()
    print("Character 1 Response Structure:")
    print(character_1_data)
else:
    print("Failed to fetch character 1 data")

# Task 2.10: тут создается класс character который будет описывать какого либо персонажа с эпизоды с такими характеристиками как имя генден и тд
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

# Task 2.11: 
if character_1_data:
    character_1 = Character(
        id=character_1_data['id'],
        name=character_1_data['name'],
        status=character_1_data['status'],
        species=character_1_data['species'],
        gender=character_1_data['gender'],
        origin=character_1_data['origin'],
        location=character_1_data['location'],
        image=character_1_data['image'],
        episode_urls=character_1_data['episode']
    )

# Task 2.12: вывод информации про персонажа 
if character_1:
    print(character_1.get_character_info())
