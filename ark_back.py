import logging
from pprint import pprint, pformat
from time import localtime, strftime
import platform    
import subprocess  
import os




FILENAME_LOGGING='check.log'

logging.basicConfig(
	level=logging.INFO,
	# format='%(asctime)s %(name)-1s %(levelname)-3s %(message)s',
	# format='%(levelname)-3s %(message)s',
	format='%(levelname)-3s [%(filename)s:%(lineno)d] %(message)s',
	datefmt='%y-%m-%d %H:%M:%S',
	handlers=[
	logging.FileHandler(FILENAME_LOGGING),
	logging.StreamHandler()
	]
)

def log(var,type=1,var_name=">"): # 0 debug, 1 info
	logging.info(str(var_name)+': %s',pformat(var) )\
		if type == 1 else logging.debug(str(var_name)+': %s',pformat(var))



class Worker:

	def ping(self,args = None):
		if not args:
			return {'example': '/do/ping?ip=8.8.8.8' }
		var_dump(args)
		ip = str(args.get('ip'))
		return ping(ip)

	def get_weather(self,args = None):
		return 'sunny'







def do(action,args = None):
	valid_actions = [func for func in dir(Worker) \
		if callable(getattr(Worker, func)) and not func.startswith("__")]
	if action in valid_actions:
		tom = Worker()
		res = getattr(tom, action)(args)
		# res = globals()[action](args)
	else:
		log('no')
		res = {'valid_actions': valid_actions}
	return res













def ping(host):
	try:
	 	TIMEOUT_PING
	except NameError:
	 	TIMEOUT_PING = 2

	timeout = TIMEOUT_PING * 1000 if platform.system().lower()=='windows' else  TIMEOUT_PING
	number = '-n' if platform.system().lower() == 'windows' else '-c'
	devnull = open(os.devnull, 'w')

	command = ['ping', number, '1', '-w', str(timeout) , host]
	return subprocess.call(command,stdout=devnull, stderr=subprocess.STDOUT) == 0





def get_weather(args):
	return 'sunny'




def get_time_now():
	return strftime("%Y-%m-%d %H:%M:%S", localtime())


def var_dump(var,var_name = ''):
	a='>>>Value:\n{0}\n<<<< \n>>>Type:\n{1}\n<<< \n>>>Dir:\n{2}\n<<< '.format(
		var,
		type(var),
		dir(var),
		)
	print(a)

	return a


