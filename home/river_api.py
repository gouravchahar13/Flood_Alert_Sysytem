import asyncio
import requests

async def river():
    url = "https://indonesia-jakarta-water-level-monitoring-data.p.rapidapi.com/tinggi_pintu_air_jakarta"

    headers = {
        "X-RapidAPI-Key": "4a1a56f92dmshb5aedf64a947abfp1f1a18jsnf46627b6bf76",
        "X-RapidAPI-Host": "indonesia-jakarta-water-level-monitoring-data.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    return(response.json())
