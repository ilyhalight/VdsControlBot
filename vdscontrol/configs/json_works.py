import json
import logging
import aiofiles

logger = logging.getLogger(__name__)

async def read_json():
    async with aiofiles.open('./configs/vds.json', 'r', encoding='utf-8') as f:
        return json.loads(await f.read())

async def write_json(data):
    try:
        current_data = await read_json()
        current_data.append(data)
    except FileNotFoundError as e:
        current_data = []
        current_data.append(data)
        logger.error(e)
    except json.decoder.JSONDecodeError as e:
        current_data = []
        current_data.append(data)
        logger.error(e)
    except AttributeError as e:
        current_data = []
        current_data.append(data)
        logger.error(e)
    except Exception as e:
        logger.exception(e)
    async with aiofiles.open('./configs/vds.json', 'w', encoding='utf-8') as f:
        await f.write(json.dumps(current_data))

async def remove_json(name):
    try:
        current_data = await read_json()
        for server in current_data:
            if server['name'] == name:
                current_data.remove(server)
                break
    except Exception as e:
        logger.exception(e)
    async with aiofiles.open('./configs/vds.json', 'w', encoding='utf-8') as f:
        await f.write(json.dumps(current_data))