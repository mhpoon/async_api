"""
Base ashnc HTTP client. All services use this module to make HTTP GET requests.
"""

import logging
import aiohttp

from config import REQUEST_TIMEOUT

logger = logging.getLogger(__name__)


class APIError(Exception):
    """
    Raise when API request fails.
    """

    def __init__(self, url: str, status: int, message: str):
        self.url = url
        self.status = status
        self.message = message 
        super().__init__(f"API error {status} for {url}: {message}")

    
async def get(
    session: aiohttp.ClientSession,
    url: str,
    params: dict,
) -> dict:
    """
    Make an async HTTP GET request and return the JSON response. 
    
    Args:
        session: The aiohttp ClientSession to use for the request.
        url: The url for HTTP request
        params: The query parameters to include in the request. 
    
    Returns:
        The JSON response as a dictionary. 
    
    Raises:
        APIError: If the response status is not 200. 
        asyncio.TimeoutError: If the request exceeds REQUEST_TIMEOUT seconds.
    """
    timeout = aiohttp.ClientTimeout(total=REQUEST_TIMEOUT)

    logger.debug(f"GET {url} params={params}")

    async with session.get(url, params=params, timeout=timeout) as resp:
        if resp.status != 200:
            text = await resp.text()
            logger.error(f"API error {resp.status} for {url}: {text}")
            raise APIError(url=url, status=resp.status, message=text)
        
        data = await resp.json()
        logger.debug(f"Response from {url} : {data}")
        return data
    









