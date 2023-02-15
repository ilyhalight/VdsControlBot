import logging
import asyncssh

logger = logging.getLogger(__name__)


async def open_connection(host: str, user: str, secret: str, port: int = 22):
    conn, client = await asyncssh.create_connection(asyncssh.SSHClient, host = host, port = port, username = user, password = secret, known_hosts=None)
    return conn, client

async def enter_command(data: list, command: str):
    conn, client = await open_connection(*data)
    async with conn:
        result = await conn.run(command)
        data = result.stdout + result.stderr
        return data