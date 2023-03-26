import json

# steamdb was too large to upload to github, so I put the cleaned genre_data.json file in the repo instead
with open('steamdb.json', 'r', encoding='iso-8859-1') as f:
    data = json.load(f)

genre_data = []
for game in data:
    if 'genres' in game:
        genre_data.append({'genres': game['genres']})

with open('genre_data.json', 'w') as f:
    json.dump(genre_data, f)
