# -*- coding: utf-8 -*-
import requests

from .const import (
    ENDPOINT_RFID,
    DEFAULT_PORT,
    METHOD_GET,
    METHOD_POST,
    METHOD_DELETE,
    HTTP_OK,
)


class Garo:

    def __init__(self, host, port=DEFAULT_PORT):
        self._base_url = "http://{host}:{port}".format(host=host,
                                                       port=port)

    def _send_request(self, endpoint, params=None, method=METHOD_GET):

        url = '{url}/{endpoint}'.format(
            url=self._base_url,
            endpoint=endpoint)

        if method == METHOD_GET:
            r = requests.get(url, json=params)
        elif method == METHOD_POST:
            r = requests.post(url, json=params)
        elif method == METHOD_DELETE:
            r = requests.delete(url)
        else:
            return False

        if r.status_code == HTTP_OK:
            return r.json()
        else:
            return False

    def list_rfids(self):
        return self._send_request(ENDPOINT_RFID)

    def add_rfid(self, tag, description):
        """method that will add a new tag to the charger

        :param str tag: tag in decimal format (will be converted to
        hex upon submission)

        :param str description: description of the tag

        """

        data = {}
        data["serialnumber"] = -1
        data["reference"] = description
        data["seqNr"] = -1
        data["rfid"] = "{:x}".format(tag)

        self._send_request(ENDPOINT_RFID, data, METHOD_POST)

    def delete_rfid(self, tag):
        _tag_to_hex = "{:x}".format(tag)

        rfids = self.list_rfids()

        for rfid in rfids:
            if rfid["rfid"] == _tag_to_hex:
                _endpoint_url = "{base_endpoint}/{seqnr}".format(base_endpoint=ENDPOINT_RFID,
                                                                 seqnr=rfid["seqNr"])

                self._send_request(_endpoint_url, None, METHOD_DELETE)

    def edit_rfid(self, tag, descripton):
        pass
