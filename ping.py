import os


def ping(hostname):
	response = os.system("ping -c 1 -w " + \
		str(2) + " " + hostname + " > /dev/null 2>&1")
	ping = 1 if response == 0 else 0
	result={
		"hostname":hostname,
		"is_ping_has_reply":ping,
	}
	return result





a = ping("114.114.114.114")


print(a)