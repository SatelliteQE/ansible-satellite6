def ansible_setup():
	with open("ansible_runner/inventory/hosts", "w") as file:
		# This is something that needs to be discussed if we want users to specify hosts at runtime
		for host in env['hosts']:
			file.write(host + '\n')


def ansible_cleanup():
	with open("ansible_runner/inventory/hosts", "w") as file:
		file.write("# Hostnames will be added here\n")
