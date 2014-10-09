import ConfigParser, os, csv, datetime

import dropbox
import requests

headers = ['user_id', 'name', 'session_count', 'created_at', 'email', 'last_request_at']

config = ConfigParser.ConfigParser()
config.read('main.cfg')

dbx={}
dbx['app_key']=config.get('Dropbox', 'app_key')
dbx['access_token']=config.get('Dropbox', 'access_token')

intercom = {}
intercom['app_key']=config.get('Intercom', 'app_key')
intercom['app_id']=config.get('Intercom', 'app_id')

for segment in config.items('IntercomSegments'):
	segment_name=segment[0]
	segment_id=segment[1]
	users = []
	r=requests.get('https://api.intercom.io/users',
		params={'segment_id': segment_id, 'per_page': 50},
		auth=(intercom['app_id'], intercom['app_key']),
		headers={'Accept':'application/json', 'User-Agent': 'Intercom Folder API App'}).json()
	users+=r['users']
	for i in range(2, r['pages']['total_pages'] + 1):
		r=requests.get('https://api.intercom.io/users',
			params={'segment_id': segment_id, 'per_page': 50, 'page': i},
			auth=(intercom['app_id'], intercom['app_key']),
			headers={'Accept':'application/json', 'User-Agent': 'Intercom Folder API App'}).json()
		users+=r['users']
	f=open(segment_name+'.csv', 'wb')
	writer=csv.writer(f)
	writer.writerow(headers)
	for user in users:
		row=[]
		for header in headers:
			row.append(str(user[header]))
		writer.writerow(row)
	dbx_client = dropbox.client.DropboxClient(dbx['access_token'])
	f.close()
	f=open(segment_name+'.csv', 'rb')
	response = dbx_client.put_file(segment_name+'/'+datetime.datetime.now().strftime('%Y-%m-%d')+'.csv', f, True)
	print "Uploaded: ", response
	f.close()
	os.remove(segment_name+'.csv')
