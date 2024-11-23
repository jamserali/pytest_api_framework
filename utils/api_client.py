import requests

from utils.logger import logger


class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    # def log_request(self, method, url, **kwargs):
    #     """Log request details"""
    #     logger.debug(f"Request: {method} -> {url}")
    #     if kwargs.get('headers'):
    #         logger.debug(f"Headers: {kwargs['headers']}")
    #     if kwargs.get('params'):
    #         logger.debug(f"Params: {kwargs['params']}")
    #     if kwargs.get('json'):
    #         logger.debug(f"Json: {kwargs['json']}")
    #     if kwargs.get('data'):
    #         logger.debug(f"Data: {kwargs['data']}")

    # def log_request(self, method, url, **kwargs):
    #     """Log request details"""
    #     logger.debug(f"Request: {method} -> {url}")
    #
    #     match kwargs:
    #         case {'headers': headers} if headers:
    #             logger.debug(f"Headers: {headers}")
    #         case {'params': params} if params:
    #             logger.debug(f"Params: {params}")
    #         case {'json': json_data} if json_data:
    #             logger.debug(f"Json: {json_data}")
    #         case {'data': data} if data:
    #             logger.debug(f"Data: {data}")

    # def log_response(self, response):
    #     """log response details"""
    #     logger.debug(f"Response: {response.status_code}")
    #     # logger.debug(f"Response Body: {response.text}")

    def log_request(self, method, url, **kwargs):
        logger.debug("Request: %s %s with params: %s", method, url, kwargs.get('params', {}))

    def log_response(self, response):
        logger.debug("Response: %s", response.text)

    def get(self, endpoint, params=None, headers=None):
        """ Make a get request """
        url = f"{self.base_url}{endpoint}"
        self.log_request("GET", url, params=params, headers=headers)
        response = requests.get(url, params=params, headers=headers)
        # self.log_response(response)
        return response

    def post(self, endpoint, data=None, json=None, headers=None):
        """ Make a post request """
        url = f"{self.base_url}{endpoint}"
        self.log_request("POST", url, endpoint=endpoint, data=data, json=json, headers=headers)
        response = requests.post(url, data=data, json=json, headers=headers)
        self.log_response(response)
        return response

    def put(self, endpoint, data=None, json=None, headers=None):
        """ Make a put request """
        url = f"{self.base_url}{endpoint}"
        self.log_request("PUT", url, endpoint=endpoint, data=data, json=json, headers=headers)
        response = requests.put(url, data=data, json=json, headers=headers)
        self.log_response(response)
        return response

    def delete(self, endpoint, headers=None):
        url = f"{self.base_url}{endpoint}"
        self.log_request("PUT", url, endpoint=endpoint,  headers=headers)
        response = requests.delete(url, headers=headers)
        self.log_response(response)
        return response
