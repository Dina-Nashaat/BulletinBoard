import json
import paramiko


system_properties = json.load(open('system.properties'))

hostname = system_properties["server"]["host"]
username = system_properties["server"]["username"]
password = system_properties["server"]["password"]
port     = system_properties["server"]["port"]

cmd_to_execute = 'cd Github/BulletinBoard && python start.py'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname, username=username, password=password, port=port)
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd_to_execute, get_pty=True)


hostname = system_properties["reader0"]["host"]
username = system_properties["reader0"]["username"]
password = system_properties["reader0"]["password"]
port = system_properties["reader0"]["port"]

cmd_to_execute = ' cd /home/dina/Documents/BulletinBoard && python start2.py'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname, username=username, password=password, port=port)
ssh_stdin, ssh_stdout2, ssh_stderr = ssh.exec_command(cmd_to_execute, get_pty=True)

for line in iter(lambda: ssh_stdout.readline(2048), ""):
    print(line)
