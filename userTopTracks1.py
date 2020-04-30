import sys

import spotipy
import spotipy.util as util

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

scope = 'user-top-read'
token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    ranges = ['short_term', 'medium_term', 'long_term']
    for range in ranges:
        print("range:", range)
        results = sp.current_user_top_tracks(time_range=range, limit=50)
	ids=[]
	previewUrls={}
        for i, item in enumerate(results['items']):
           #print(i, item['name'])
            ids.append(results['id'])
	    previewUrls[results['id']]=results['preview_url']	
        
	valences={}
	analysis = sp.audio_features(ids)
	for valence in analysis:
		valences[analysis['id']]=analysis['valence']
	maximum = (max(analysis['valence']))
	happyId = maximum[1]
	minimum = (min(analysis['valence']))
	sadId = minimum[1]

	#if file == happy
	#	webbrowser open preview url
	#	previewUrls.get(happyId)
	#if file == sad
	#	same as above
	
else:
    print("Can't get token for", username)
