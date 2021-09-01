import os, shutil, uuid, yaml, logging, aiohttp, json, urllib, hashlib, datetime, asyncio, base64, re, zipfile, tempfile, time
from urllib.parse import urlparse


async def fetch_post(url, body):
    p = urlparse(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Referer': f'{p.scheme}//{p.netloc}'
    }
    connector = aiohttp.TCPConnector(verify_ssl=False)
    async with aiohttp.ClientSession(headers=headers, connector=connector) as session:
        async with session.post(url, data=json.dumps(body)) as resp:
            response = await resp.json()
            return response