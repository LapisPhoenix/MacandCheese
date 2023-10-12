import aiohttp
import requests
from typing import Dict, Optional


class AsyncHTTPClient:
    """
    A handler for sending Asynchronous requests
    """

    @staticmethod
    async def get(endpoint: str, params: Optional[Dict] = None, headers: Optional[Dict] = None) -> Dict:
        """
        Get data from an endpoint.
        :param endpoint: Endpoint URL
        :param params: Optional Endpoint Parameters
        :param headers: Optional Endpoint Headers
        :return: Dictionary
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(
                url=endpoint, headers=headers, params=params
            ) as response:
                return await response.json()

    @staticmethod
    async def post(
        endpoint: str,
        data: Optional[Dict] = None,
        params: Optional[Dict] = None,
        headers: Optional[Dict] = None,
    ) -> Dict:
        """
        Post data to an endpoint.
        :param endpoint: Endpoint URL
        :param data: Optional Endpoint Data
        :param params: Optional Endpoint Parameters
        :param headers: Optional Endpoint Headers
        :return: Dictionary
        """
        async with aiohttp.ClientSession() as session:
            async with session.post(url=endpoint, data=data, params=params, headers=headers) as request:
                return await request.json()


class HTTPClient:
    @staticmethod
    def get(endpoint: str, params: Optional[Dict] = None, headers: Optional[Dict] = None) -> Dict:
        """
        Get data from an endpoint.
        :param endpoint: Endpoint URL
        :param params: Optional Endpoint Parameters
        :param headers: Optional Endpoint Headers
        :return: Dictionary
        """
        request = requests.get(url=endpoint, params=params, headers=headers)
        return request.json()

    @staticmethod
    def post(
        endpoint: str,
        data: Optional[Dict] = None,
        params: Optional[Dict] = None,
        headers: Optional[Dict] = None,
    ) -> Dict:
        """
        Post data to an endpoint.
        :param endpoint: Endpoint URL
        :param data: Optional Endpoint Data
        :param params: Optional Endpoint Parameters
        :param headers: Optional Endpoint Headers
        :return: Dictionary
        """
        request = requests.post(url=endpoint, params=params, headers=headers, data=data)
        return request.json()
