import pandas as pd
import pdb

df1 = pd.read_excel('netflix_tmdb_dataset_movie_v1.xlsx')
df2 = pd.read_excel('netflix_tmdb_dataset_v1.xlsx')

result = pd.concat([df1,df2],ignore_index=True)
# result.to_excel('combined_data.xlsx',index = False)


genre_dict = [{"id": 28,"name": "Action"},{"id": 12,"name": "Adventure"},{"id": 16,"name": "Animation"},
{"id": 35,"name": "Comedy"},{"id": 80,"name": "Crime"},
{"id": 99,"name": "Documentary"},{"id": 18, "name": "Drama"},{"id": 10751,"name": "Family"},
{"id": 14,"name": "Fantasy"},{"id": 36,"name": "History"},{"id": 27,"name": "Horror"},
{"id": 10402,"name": "Music"},{"id": 9648,    "name": "Mystery"},{"id": 10749,"name": "Romance"},
{"id": 878,"name": "Science Fiction"},{"id": 10770,"name": "TV Movie"},
{"id": 53,"name": "Thriller"},{"id": 10752,"name": "War"},{"id": 37,"name": "Western"}]

final_genre_dict = {}

for test_dict in genre_dict:
	genre_id = test_dict['id']
	genre_name = test_dict['name']

	final_genre_dict[genre_id] =genre_name 



pd.set_trace()

print(final_genre_dict)
print(len(final_genre_dict))