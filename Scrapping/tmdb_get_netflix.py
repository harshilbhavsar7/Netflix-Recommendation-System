import requests
import pdb
import pandas as pd

# url = "https://api.themoviedb.org/3/discover/movie?api_key=deb585dfabf43c69bd9e46ba9b30b099&with_networks=213"
url = "https://api.themoviedb.org/3/discover/tv?api_key=deb585dfabf43c69bd9e46ba9b30b099&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&with_watch_providers=Netflix&watch_region=CA&with_watch_monetization_types=flatrate"



payload={}
headers = {}


response = requests.request("GET", url, headers=headers, data=payload)


total_pages = response.json()['total_pages']

final_data_dict = {}
final_list=[]
for i in range(1,total_pages+1):
	url = url + "&page={}".format(i)
	response = requests.request("GET", url, headers=headers, data=payload)
	for itm in response.json()['results']:
		final_list.append(itm)
	# loop_dict = {}
	# for j,itm in enumerate(response.json()['results']):
	# 	try:
	# 		loop_dict.clear()
	# 		# pdb.set_trace()
	# 		if itm['backdrop_path']:
	# 			loop_dict['backdrop_path']=itm['backdrop_path']
	# 		if itm['first_air_date']:		
	# 			loop_dict['first_air_date']=itm['first_air_date']
	# 		if itm['genre_ids']:
	# 			loop_dict['genre_ids']=itm['genre_ids']
	# 		if itm['id']:
	# 			loop_dict['id']=itm['id']
	# 		if itm['name']:
	# 			loop_dict['name']=itm['name']
	# 		if itm['origin_country']:
	# 			loop_dict['origin_country']=itm['origin_country']
	# 		if itm['original_language']:
	# 			loop_dict['original_language']=itm['original_language']
	# 		if itm['original_name']:
	# 			loop_dict['original_name']=itm['original_name']
	# 		if itm['overview']:
	# 			loop_dict['overview']=itm['overview']
	# 		if itm['popularity']:
	# 			loop_dict['popularity']=itm['popularity']
	# 		if itm['poster_path']:
	# 			loop_dict['poster_path']=itm['poster_path']
	# 		if itm['vote_average']:
	# 			loop_dict['vote_average']=itm['vote_average']
	# 		if itm['vote_count']:
	# 			loop_dict['vote_count']=itm['vote_count']
	# 		final_data_dict[j] = loop_dict
	# 	except Exception as e:
	# 		print(i,j,e)
			

print(final_list)
# pdb.set_trace()
# final_data = pd.DataFrame.from_dict(final_data_dict,orient='index',
#                        columns=['backdrop_path''first_air_date','genre_ids','id','name',
#                        'origin_country','original_language','original_name','overview',
#                        'popularity','poster_path','vote_average','vote_count'])


final_data = pd.json_normalize(final_list)


final_data.to_excel('netflix_tmdb_dataset_movie_v1.xlsx',index = False)