# Mac and Cheese
Mac and Cheese is a Python package that serves as a convenient wrapper for the IPGeolocation API. It simplifies the process of obtaining various information about IP addresses, time zones, user agents, and solar-related data.

## Installation

To install Mac and Cheese, you can use **pip**:
```bash
pip install macandcheese
```

## Usage
Here's a simple example demonstrating how to use the Mac and Cheese package to get information about a specific IP address:
```python
import asyncio
from macandcheese import IpGeolocationClient

async def main():
    # Replace 'your_api_key' with your actual IPGeolocation API key
    api_key = 'your_api_key'
    
    # Create an instance of the IpGeolocationClient
    client = IpGeolocationClient(api_key)
    
    # Specify the IP address you want to look up (optional, defaults to the current machine's IP)
    ip_address = '8.8.8.8'
    
    try:
        # Get information about the specified IP address
        result = await client.get_ip_info(ip_address)
        print(result)
    except Exception as e:
        print(f"Error: {e}")

# Run the event loop
asyncio.run(main())
```
In this example, we create an IpGeolocationClient instance with the provided API key and then use it to retrieve information about the specified IP address (in this case, '8.8.8.8'). The result is printed to the console.

## Documentation
IpGeolocationClient Class
__init__(self, api_key: str)

    Initializes the IpGeolocationClient with the provided API key.
    Raises an errors.InvalidAPIKey exception if the API key is not valid.

get_ip_info(self, ipaddr: str = None) -> str | Dict

    Retrieves information about the specified IP address.
    If ipaddr is not provided, it defaults to the current machine's IP.
    Returns a dictionary containing IP information.

get_timezone(self, timezone: str) -> str | Dict

    Retrieves information about the specified timezone.
    Returns a dictionary containing timezone information.

get_user_agent(self) -> str | Dict

    Retrieves the user agent of the current machine.
    Returns a dictionary containing user agent information.

get_solar_from_location(self, location: str) -> str | Dict

    Retrieves information about sunset, sunrise, and other time-related data for a given location.
    Returns a dictionary containing solar information.

get_solar_from_coordinates(self, lat: float | int, long: float | int) -> str | Dict

    Retrieves information about sunset, sunrise, and other time-related data for a given latitude and longitude.
    Returns a dictionary containing solar information.

get_solar_from_ip(self, ipaddr: str = None) -> str | Dict

    Retrieves information about sunset, sunrise, and other time-related data for the specified IP address.
    If ipaddr is not provided, it defaults to the current machine's IP.
    Returns a dictionary containing solar information.

# License
This project is licensed under the MIT License - see the __LICENSE__ file for details.
