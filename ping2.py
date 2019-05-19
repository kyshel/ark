import platform    # For getting the operating system name
import subprocess  # For executing a shell command

def ping(host):
	"""
	Returns True if host (str) responds to a ping request.
	Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
	"""

	# Option for the number of packets as a function of
	number = '-n' if platform.system().lower()=='windows' else '-c'
	try:
	 	TIMEOUT_PING
	except NameError:
	 	TIMEOUT_PING = 2

	# Building the command. Ex: "ping -c 1 google.com"
	command = ['ping', number, '1', '-w', str(TIMEOUT_PING) , host]

	return subprocess.call(command) == 0