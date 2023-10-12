import ipaddress
import asyncio
from typing import Dict
from api.https import AsyncHTTPClient, HTTPClient
from endpoints import Endpoints
from ext import errors


class IpGeolocationClient:
    def __init__(self, api_key: str):
        self._api_key = api_key
        self._current_ip = None     # Saved for time optimization
        self._validate_key()

    def _validate_key(self):
        # Test request
        url = Endpoints.GEOLOCATION % (self._api_key, "8.8.8.8")  # Google DNS
        resp = HTTPClient.get(url)
        bad_key = resp.get("message", None)

        if bad_key is None:
            pass
        else:
            raise errors.InvalidAPIKey(f"Provided API key \"{self._api_key}\" is not valid.")

    async def get_ip_info(self, ipaddr: str = None) -> str | Dict:
        """
        Get IP information from either a specified IP (v4 or V6) or current machine's IP.
        :param ipaddr: Ip address to look up
        :return:
        """
        # TODO: Figure out how to
        if ipaddr is None:
            if self._current_ip is None:
                ipaddr = await self._get_public_ip(True)
            else:
                ipaddr = await self._get_public_ip()

        if not self._check_ip(ipaddr):
            raise errors.NotAValidIP(f"{ipaddr} is not a valid IP address")

        url = Endpoints.GEOLOCATION % (self._api_key, ipaddr)

        return await self._send_request(url)

    @staticmethod
    async def _send_request(url, *args, **kwargs):
        info = await AsyncHTTPClient.get(url, *args, **kwargs)
        msg = info.get("message", None)
        if msg:
            return msg
        return info

    @staticmethod
    def _check_ip(ip):
        try:
            ipaddress.ip_address(ip)
            return True
        except ValueError:
            return False

    async def _get_public_ip(self, override: bool = False):
        response = await AsyncHTTPClient.get("https://api64.ipify.org?format=json")
        ipaddr = response.get('ip')

        if override or self._current_ip is None:
            self._current_ip = ipaddr

        return ipaddr

    async def get_timezone(self, timezone: str) -> str | Dict:
        """
        Get the timezone information
        :param timezone: Example: America/Los_Angeles
        :return: Dict
        """
        url = Endpoints.TIMEZONE % (self._api_key, timezone)
        return await self._send_request(url)

    async def get_user_agent(self) -> str | Dict:
        """
        Get the current machine's useragent
        :return:
        """
        url = Endpoints.USERAGENT % (self._api_key,)
        return await self._send_request(url)

    async def get_solar_from_location(self, location: str) -> str | Dict:
        """
        Get the current information about sunset, sunrise, and other time information from a location.
        :param location: Example: New York, US
        :return:
        """
        url = Endpoints.ASTRO_GENERAL % (self._api_key, location)
        return await self._send_request(url)

    async def get_solar_from_coordinates(self, lat: float | int, long: float | int) -> str | Dict:
        """
        Get the current information about sunset, sunrise, and other time information from a lat and long coord.
        :param lat:
        :param long:
        :return:
        """
        url = Endpoints.ASTRO_COORDS % (self._api_key, lat, long)
        return await self._send_request(url)

    async def get_solar_from_ip(self, ipaddr: str = None):
        if ipaddr is None:
            if self._current_ip is None:
                ipaddr = await self._get_public_ip(True)
            else:
                ipaddr = await self._get_public_ip()

        if not self._check_ip(ipaddr):
            raise errors.NotAValidIP(f"{ipaddr} is not a valid IP address")

        url = Endpoints.ASTRO_IP % (self._api_key, ipaddr)
        return await self._send_request(url)
