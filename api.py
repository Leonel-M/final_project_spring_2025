#  Code base of https://fastapi.tiangolo.com/tutorial/first-steps/
from fastapi import FastAPI
import json
import httpx
"""
The HTTPX library is required to connect correctly and asynchronously with external sites.
https://stackoverflow.com/questions/63872924/how-can-i-send-an-http-request-from-my-fastapi-app-to-another-site-api?utm_source=chatgpt.com
"""

async def fetch_data(client, url):
    """
    :param client:
    :param url: Platzi API
    :return: Server data in JSON format
    """
    response = await client.get(url)
    return response.json()  # https://fakeapi.platzi.com/ has e-commerce data in JSON format

def save_json(data,filename):
    """
    :param data: Server data
    :param filename: Document location
    :return:
    """
    # https://www.geeksforgeeks.org/reading-and-writing-json-to-a-file-in-python/
    with open(filename, 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4 )

app = FastAPI()

@app.get("/")
async def get_data():
    api_products = 'https://api.escuelajs.co/api/v1/products'
    api_locations = 'https://api.escuelajs.co/api/v1/locations'

    async with httpx.AsyncClient() as client:  # Async requests https://www.python-httpx.org/async/

        products = await fetch_data(client,api_products)
        locations = await fetch_data(client,api_locations)

        save_json(products, 'data/products.json')
        save_json(locations, 'data/locations.json')
    return {
        'message': 'Data saved successfully',
        'products_count': len(products),
        'locations_count': len(locations)
    }