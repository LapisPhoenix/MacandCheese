# Endpoints for the ipgelocation api
# Note: Some endpoints may go unused
# ! IMPORTANT: ALL ENDPOINTS REQUIRE API KEY
# If I missed an endpoint, open an issue and let me know!

class Endpoints:
    GEOLOCATION       = "https://api.ipgeolocation.io/ipgeo?apiKey=%s&ip=%s"
    TIMEZONE          = "https://api.ipgeolocation.io/timezone?apiKey=%s&tz=%s"
    USERAGENT         = "https://api.ipgeolocation.io/user-agent?apiKey=%s"

    ASTRO_GENERAL     = "https://api.ipgeolocation.io/astronomy?apiKey=%s&location=%s"
    ASTRO_COORDS      = "https://api.ipgeolocation.io/astronomy?apiKey=%s&lat=%s&long=%s"
    ASTRO_IP          = "https://api.ipgeolocation.io/astronomy?apiKey=%s&ip=%s"
    ASTRO_COORDS_DATE = "https://api.ipgeolocation.io/astronomy?apiKey=%s&lat=%s&long=%s&date=%s"
    ASTRO_IP_DATE     = "https://api.ipgeolocation.io/astronomy?apiKey=API_KEY&ip=%s&date=%s"
