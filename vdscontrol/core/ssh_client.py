import paramiko
import logging

logger = logging.getLogger(__name__)

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


def open_connection(host, user, secret, port = 22):
    client.connect(hostname=host, username=user, password=secret, port=port)

def check_connection():
    if client.get_transport().is_active() == True:
        logger.debug('Connection is active')
        return True
    else:
        logger.debug('Connection is not active')
        return False

def enter_command(command):
    stdin, stdout, stderr = client.exec_command(command)
    data = stdout.read() + stderr.read()
    return data.decode()

def close_connection():
    client.close()