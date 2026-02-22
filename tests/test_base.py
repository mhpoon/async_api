"""
Unit test for base.py in services
"""

import pytest
import asyncio
import aiohttp
from aioresponses import aioresponses

from services.base import get, APIError


# Fixtures 

@pytest.fixture
async def session():
    """
    Shared aiohttp ClientSession for each test.
    """
    async with aiohttp.ClientSession() as s:
        yield s


BASE_URL = "https://test.com/api"

# Success Cases 
@pytest.mark.asyncio
async def test_get_returns_json(session):
    """
    A 200 response should return the parsed JSON body as a dict.
    """
    mock_response = {"result": "ok", "value": 17}

    with aioresponses() as mock:
        mock.get(BASE_URL, payload=mock_response, status=200)
        result = await get(session, BASE_URL, params={})

    assert result == mock_response


@pytest.mark.asyncio
async def test_get_passes_params(session):
    """
    Query params should be include in the request.
    """
    params = {"address": "123 Seaseme St", "format": "json"}

    with aioresponses() as mock:
        mock.get(BASE_URL, payload={"result": "ok"}, status=200)
        await get(session, BASE_URL, params=params)

    # aioresponse captures the requests made 
    mock.assert_called_once()


# Error 
    
@pytest.mark.asyncio
async def test_get_raises_api_error_on_non_200(session):
    """
    Raise APIError when response is not 200
    """
    status_code = 404

    with aioresponses() as mock:
        mock.get(BASE_URL, body="Not Found", status=status_code)

        with pytest.raises(APIError) as exec_info:
            await get(session, BASE_URL, params={})

    assert exec_info.value.status == status_code
    assert exec_info.value.url == BASE_URL


@pytest.mark.asyncio
async def tset_api_error_contains_message(session):
    """
    APIError should carry the response body in the message.
    """    
    status_code = 503
    error_body = "Service Unavailable"

    with aioresponses() as mock:
        mock.get(BASE_URL, body=error_body, status=status_code)

        with pytest.raises(APIError) as exec_info:
            await get(session, BASE_URL, params={})

        assert exec_info.value.message == error_body
        assert exec_info.value.status == status_code


@pytest.mark.asyncio
async def test_get_raises_timeout(session):
    """
    Raise asyncio.TimeoutError when request exceeds the timeout
    """
    with aioresponses() as mock:
        mock.get(BASE_URL, exception=asyncio.TimeoutError())

        with pytest.raises(asyncio.TimeoutError):
            await get(session, BASE_URL, params={})


@pytest.mark.asyncio
async def test_get_raises_on_connection_error(session):
    """
    Raise aiohttp.ClientconnectionError
    """
    with aioresponses() as mock:
        mock.get(BASE_URL, exception=aiohttp.ClientConnectionError())

        with pytest.raises(aiohttp.ClientConnectionError):
            await get(session, BASE_URL, params={})
