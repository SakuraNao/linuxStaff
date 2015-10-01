import sys
from datetime import datetime
from imgurpython import ImgurClient
from auth import authenticate
import pyperclip


argvs = sys.argv 
# If you already have an access/refresh pair in hand
client_id = ''
client_secret = ''
access_token = ''
refresh_token = ''

# Note since access tokens expire after an hour, only the refresh token is required (library handles autorefresh)
client = ImgurClient(client_id, client_secret, access_token, refresh_token)

path = argvs[1]
album = None # You can also enter an album ID here
name = None
title = None
description = None

def upload(client):
	config = {
		'album': album,
		'name':  name,
		'title': title,
		'description': description
	}


	image = client.upload_from_path(path, config=config, anon=False)
	return image

if __name__ == "__main__":
	

# Note since access tokens expire after an hour, only the refresh token is required (library handles autorefresh)
	#client = ImgurClient(client_id, client_secret, access_token, refresh_token)
#	client = authenticate()
	image = upload(client)
#	items = client.gallery(section='top', sort='time', page=3, window='week', show_viral=False)
#	print(image['link'])
	imageLink = '[img]' + image['link'] + '[/img]'
#	pyperclip.copy(image['link'])
	pyperclip.copy(imageLink)
