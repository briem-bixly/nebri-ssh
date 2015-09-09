# Nebri SSH

This app is intended for use with a Nebri instance. Visit https://nebrios.com to sign up for free!

<h2>Setup</h2>
This app requires very little in terms of setup. Please ensure that all files are placed in the correct places over SFTP. `nebri_ssh.py` should be copied to /libraries.
<strong>NOTE</strong>: A copy of the private ssh key that will be used to connect to any servers should also be uploaded to your instance. This file should be copied to /workspace.

<h2>Requirements</h2>
This app requires the use of sshtunnel. SSH into your Nebri instance and install via pip:
```
pip install sshtunnel
```

<h2>Examples</h2>
```
from nebri_ssh import setup_ssh
server = setup_ssh('remote_ip', 'remote_port', 'username', 'ssh_file_name', ('remote_bind_ip', 'remote_bind_port'))
server.start()
# do stuff
server.close()
```
- remote ip is the ip address of the server you want to ssh to
- remote port is the port to connect to, <strong>NOTE</strong>: this should usually be port 22
- username is the user to connect to the server as
- ssh file name should be just the file name of your private ssh key, no path is needed
- remote bind ip and remote bind port should be a tuple. they should point to the port you want to tunnel to
-   for example, if you want to ssh tunnel to a MySQL instance, your ip should be the server ip with a port of 3306
