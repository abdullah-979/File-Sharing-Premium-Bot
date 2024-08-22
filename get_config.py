import aiohttp
import os
import logging

logging.basicConfig(level=logging.ERROR)
LOGGER = logging.getLogger(__name__)

CONFIG_FILE_URL = os.environ.get('CONFIG_FILE_URL')

if CONFIG_FILE_URL:
    try:
        with aiohttp.ClientSession() as session:
            res = session.get(CONFIG_FILE_URL)
            res.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)

            content = res.read()
            with open('config.py', 'wb') as f:
                f.write(content)
    except Exception as e:
        LOGGER.error(f"Error downloading CONFIG_FILE_URL: {e}")
else:
    LOGGER.error("CONFIG_FILE_URL is missing or empty")
