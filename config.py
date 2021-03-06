SSLKeyPath=  'keys/tophat.key'

SSLCertPath= 'keys/tophat.crt'

SSLCAPath = 'keys/ca.crt'		

Port=8880

Interface='0.0.0.0'

User='tophat'

Group='tophat'

Threads=6

PIDFile = 'tophat.pid'
#EncryptionMethod=SSLEncryption

LogFile='/var/log/tophat/tophat.log'

DBDriver='MySQL'

MySQLHost='localhost'

MySQLUser='tophat'

MySQLPass='password'

MySQLDatabase='tophat'

resources = [
	('/apitokens/', "Apitokens"),
	('/users/', "Users"),
	('/jsontest/', "Jsontest"),
	('/', 'Version'),
	('/version/', "Version"),
	('/games/', "Games"),
	('/kills/', "Kills"),
	('/players/', "Players"),
	('/alive/', "Alive"),
	('/teamscore/', "TeamScore"),
	('/teams/', "Teams")
]
from Networking.Protocols.Cherrypy import Protocol

Version='0.1.2'
GameVersion='0.1'
ServerTitle='TopHat QRzar Testing Server'

try:
	from local_config import * 
except ImportError:
	pass
