import logging
from socket import gaierror
from paramiko import AuthenticationException
from asyncssh import PermissionDenied
from core.ssh_client import open_connection, enter_command

logger = logging.getLogger(__name__)

async def get_info(ip: str, user: str, secret: str, port: int = 22):
    try:
        neofetch_output = await enter_command((ip, user, secret, port), 'neofetch')
        df_output = await enter_command((ip, user, secret, port), 'df -h')
    except PermissionDenied:
        return {
            'status': False,
            'error': '❌ Неверный логин или пароль'
        }
    except gaierror:
        return {
            'status': False,
            'error': '❌ Неверный IP адрес'
        }
    except Exception as err:
        logger.exception(err)
        return {
            'status': False,
            'error': '❌ Не удалось получить информацию о сервере'
        }

    os = neofetch_output.partition('OS')[2].split('[0m')[3]
    host = neofetch_output.partition('Host')[2].split('[0m')[3]
    kernel = neofetch_output.partition('Kernel')[2].split('[0m')[3]
    uptime = neofetch_output.partition('Uptime')[2].split('[0m')[3]
    packages = neofetch_output.partition('Packages')[2].split('[0m')[3]
    shell = neofetch_output.partition('Shell')[2].split('[0m')[3]
    cpu = neofetch_output.partition('CPU')[2].split('[0m')[3]
    memory = neofetch_output.partition('Memory')[2].split('[0m')[3]
    disks = [
        df_output.split('\n')[0]
    ]
    for disk in df_output.split('\n'):
        if disk.startswith('/dev/'):
            disks.append(disk)
    return {
        'status': True,
        'os': os,
        'host': host,
        'kernel': kernel,
        'uptime': uptime,
        'packages': packages,
        'shell': shell,
        'cpu': cpu,
        'memory': memory,
        'disks': disks
    }