import sys
import operator
import spotipy
import spotipy.util as util
import webbrowser as wb

#open files emotions.txt
#assign file to data

if len(sys.argv) > 1:
	username = sys.argv[1]
else:
	print("Usage: %s username" % (sys.argv[0],))
	sys.exit()

scope = 'user-top-read'
#add client secret and client user and redirect uri localhost:8888
token = util.prompt_for_user_token(username, scope, client_id='ea5e894128dd4d598c1ac326ada95b90', client_secret='7e9b908b1e1148f69ba12730c337f5be', redirect_uri ='http://localhost:8888')

if token:
	sp = spotipy.Spotify(auth=token)
	sp.trace = False
	ranges = ['short_term', 'medium_term', 'long_term']
	for range in ranges:
		print("range:", range)
	results = sp.current_user_top_tracks(time_range=range, limit=50)
	ids=[]
	previewUrls={}
	for i,item in enumerate(results['items']):
		
		ids.append(item['id'])
		previewUrls[item['id']]=item['preview_url']	

	valences={}
	analysis = sp.audio_features(ids)
	for item in analysis:
		valences[item['valence']]=item['id']
	maximum = (max(valences.iteritems()))
	happyId = maximum[1]
	minimum = (min(valences.iteritems()))
	sadId = minimum[1]

	f = open("emotion.txt", "r")
	content = f.read()	

	if content == 'HAPPY':
		wb.open_new_tab(previewUrls.get(happyId))
	if content == 'SAD':
		wb.open_new_tab(previewUrls.get(sadId))
		

else:
	print("Can't get token for", username)
