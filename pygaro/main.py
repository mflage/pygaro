# -*- coding: utf-8 -*-
import requests

from .const import (
    RFID_ENDPOINT,
    DEFAULT_PORT,
    METHOD_GET,
    METHOD_POST,
)


class Garo:

    def __init__(self, host, port = DEFAULT_PORT):
        self._host = host
        self._port = port
    
    def list_rfids(self):

        r = requests.get(RFID_ENDPOINT.format(host=self._host,
                                              port=self._port))

        if r.status_code == 200:
            return r.json()

    def add_rfid(self, tag, description):

        data = {}
        data["serialnumber"] = -1
        data["reference"] = description
        data["seqNr"] = -1
        data["rfid"] = "{:x}".format(tag)

        r = requests.post(BASE_URL)
        # data["validFrom"]
        # data["validTo"]

        pass

    def delete_rfid(self, tag):
        pass

    def _send_request(self, endpoint, params=None, method=METHOD_GET):
        pass
    
                      
