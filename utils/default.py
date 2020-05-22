import json
import time
import aiohttp
import inspect
import discord

from collections import namedtuple

def get(file):
    try:
        with open(file, encoding='utf8') as data:
            return json.load(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
    except AttributeError:
        raise AttributeError("Unknown argument")
    except FileNotFoundError:
        raise FileNotFoundError("JSON file wasn't found")

def date(target, clock=True):
    if clock is False:
        return target.strftime("%d %B %Y")
    return target.strftime("%d %B %Y, %H:%M")

async def request(url, *, headers=None, payload=None, method='GET', attr='json', force_content_type_json=False):
    # Make sure our User Agent is what's set, and ensure it's sent even if no headers are passed
    if headers is None:
        headers = {}

    config = get("config.json")

    headers['User-Agent'] = config.user_agent

    for i in range(5):
        try:
            # Create the session with our headers
            async with aiohttp.ClientSession(headers=headers) as session:
                # Make the request, based on the method, url, and paramaters given
                async with session.request(method, url, params=payload) as response:
                    # If the request wasn't successful, re-attempt
                    if response.status != 200:
                        continue

                    try:
                        # Get the attribute requested
                        return_value = getattr(response, attr)
                        # Next check if this can be called
                        if callable(return_value):
                            # This is use for json; it checks the mimetype instead of checking if the actual data
                            # This causes some places with different mimetypes to fail, even if it's valid json
                            # This check allows us to force the content_type to use whatever content type is given
                            if force_content_type_json:
                                return_value = return_value(content_type=response.headers['content-type'])
                            else:
                                return_value = return_value()
                        # If this is awaitable, await it
                        if inspect.isawaitable(return_value):
                            return_value = await return_value

                        # Then return it
                        return return_value
                    except AttributeError:
                        # If an invalid attribute was requested, return None
                        return None
        # If an error was hit other than the one we want to catch, try again
        except:
            continue