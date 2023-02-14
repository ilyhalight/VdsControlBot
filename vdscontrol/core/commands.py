from paramiko import AuthenticationException
from core.ssh_client import open_connection, check_connection, enter_command, close_connection

def get_info(ip: str, user: str, secret: str, port: int = 22):
    try:
        open_connection(ip, user, secret, port)
    except AuthenticationException:
        return {
            'status': False,
            'error': '❌ Неверный логин или пароль'
        }
    if not check_connection():
        return {
            'status': False,
            'error': '❌ Не удалось подключиться к серверу'
        }
    neofetch_output = enter_command('neofetch')
    df_output = enter_command('df -h')
    close_connection()
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