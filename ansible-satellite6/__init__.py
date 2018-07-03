"""A set of tasks for automating interactions with Satellite servers.

Some commands may require modifications of envvars file.
"""

import ansible_runner

from ansible_satellite6.utils import ansible_setup, ansible_cleanup

PLAYBOOK_DIR = "ansible_runner/"


def partition_disk():
	"""Re-partitions disk to increase the size of /root to handle
	synchronization of larger repositories.

	"""
	ansible_setup()
	ansible_runner.interface.run(
		private_data_dir=PLAYBOOK_DIR,
		playbook="partition_disk.yml"
	)
	ansible_cleanup()
