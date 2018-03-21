import paramiko

server = '172.20.10.9'
username = 'magdz'
password = '1234'
port = 8888

cmd_to_execute = 'cd Github/BulletinBoard && python start.py'


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(server, username=username, password=password, port=port)
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd_to_execute, get_pty=True)

for line in iter(lambda: ssh_stdout.readline(2048), ""):
    print(line)
