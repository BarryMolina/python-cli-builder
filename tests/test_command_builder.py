from unittest.mock import patch
from python_cli_builder.command import Command

def test_command_builder():
	command = Command('docker compose --profile')
	command.add('up')
	assert command.args == ['docker', 'compose', '--profile', 'up']

def test_command_builder_add_list():
	command = Command('docker compose --profile')
	command.add(['up', 'down'])
	assert command.args == ['docker', 'compose', '--profile', 'up', 'down']

def test_command_builder_run():
	with patch('subprocess.run') as mock_run:
		command = Command('docker compose --profile')
		command.add(['up', 'down'])
		command.run()
		mock_run.assert_called_once_with(['docker', 'compose', '--profile', 'up', 'down'])
