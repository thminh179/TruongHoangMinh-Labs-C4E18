from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin123@ds035593.mlab.com:35593/minhth-c4e18-lab"

#1. Connect to database
client = MongoClient(mongo_uri)

#2. Get database
db = client.get_default_database()

#3. Create Collection
games = db['games']
films = db['films']

# #4. Create Document
# new_game = {
#     "title": "PES",
#     "description": "Pro Evolution Soccer"
# }
# new_film = {
#     "title": "Better Call Saul",
#     "description": "Breaking Bad spin-off"
# }

# #5. Insert Document into Collection
# games.insert_one(new_game)
# films.insert_one(new_film)

all_game = games.find()
for game in all_game:
    print(game)