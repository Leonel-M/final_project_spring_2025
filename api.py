#  Code base of https://fastapi.tiangolo.com/tutorial/first-steps/

from fastapi import FastAPI
import json
import httpx
"""
The HTTPX library is required to connect correctly and asynchronously with external sites.
https://stackoverflow.com/questions/63872924/how-can-i-send-an-http-request-from-my-fastapi-app-to-another-site-api?utm_source=chatgpt.com
"""

app = FastAPI()


@app.get("/")
async def get_data():
    api_products = 'https://api.escuelajs.co/api/v1/products'
    async with httpx.AsyncClient() as client:  # Async requests https://www.python-httpx.org/async/
        products_response = await client.get(api_products)
        products = products_response.json()  # https://fakeapi.platzi.com/ has e-commerce data in JSON format

    api_locations = 'https://api.escuelajs.co/api/v1/locations'
    async with httpx.AsyncClient() as client:
        locations_response = await client.get(api_locations)
        locations = locations_response.json()

# https://www.geeksforgeeks.org/reading-and-writing-json-to-a-file-in-python/
    with open('data/products.json', 'w', encoding='utf-8') as outfile:
        json.dump(products, outfile, ensure_ascii=False, indent=4 )
    with open('data/locations.json', 'w', encoding='utf-8') as outfile:
        json.dump(locations, outfile, ensure_ascii=False, indent=4 )

    return