from gensim.models import word2vec

json_file_path = 'data/test_user.json'

model = word2vec.Word2Vec.load('data/wiki.model')

atmosphere_vec = model.wv['']
past_trip_you_liked_vec = model.wv['']
hobby_vec = model.wv['']

with open(json_file_path, 'r') as f:
	data_list = f.read()
	

