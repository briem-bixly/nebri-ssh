from sshtunnel import SSHTunnelForwarder


def setup_ssh(ip, port, username, ssh_file, remote_address):
    """
    :param ip: this is the ip address of the ssh server to connect to
    :param port: this is the port of the ssh server to connect to. default is 22
    :param username: the user that you will be authenticated as
    :param ssh_file: the filename of the ssh private key that will used to authenticate
    :param remote_address: a tuple of the remote ip (string) and port (int) to bind to
    :return: returns a server object
    """
    return SSHTunnelForwarder(
        (ip, port),
        ssh_username=username,
        ssh_private_key=ssh_file,
        remote_bind_address=remote_address
    )
