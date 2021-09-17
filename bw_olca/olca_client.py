from datetime import datetime

import requests
from dateutil import parser

from bw_olca.exchange_types import ExchangeType


class OLCAClient(object):
    def __init__(self, url: str = "http://localhost", port: int = 8080):
        self.url = "{}:{}".format(url, port)
        self.next_id = 1

    def get_olca_database_by_type(self, exchange_types: ExchangeType, verbose=False):
        """
        Performs requests for the types specified in exchange_types and returns the
        results
        This works for the database that is currently being published by the
        OpenLCA software.
        For details on how to set up the OpenLCA Server refer to the README.
        """

        # This uses the brightway convention as keys if they are available
        results = {}

        for exchange_type in exchange_types:
            if verbose:
                print(exchange_type)

            tmp_results = []

            params = {"@type": exchange_type.value["olca"]}

            # For performance reasons, all descriptors are pulled first and then the
            # individual datasets are pulled separately.

            descriptors, error = self.post(method="get/descriptors", params=params)
            self.post(method="", params=params)
            for descriptor in descriptors:
                params = {
                    "@id": descriptor["@id"],
                    "@type": exchange_type.value["olca"],
                }
                res, error = self.post(method="get/model", params=params)

                # Before adding results, make sure that the last changed date is in
                # python datetime format.
                if "lastChange" in res.keys():
                    if isinstance(res["lastChange"], str):
                        res["lastChange"] = parser.parse(res["lastChange"])
                    elif not isinstance(res["lastChange"], datetime):
                        res["lastChange"] = parser.parse("1970-1-1T00:00:00.0+00:00")
                else:
                    # If no lastChange is recorded, use a dummy value instead
                    res["lastChange"] = parser.parse("1970-1-1T00:00:00.0+00:00")

                tmp_results.append(res)

            # Sort the temp_results list by last changed dates to make sure, the
            # most recent changed exchange is at the top. This is needed so that
            # brightway can easily check if it's cache is still up-to-date.
            tmp_results = sorted(
                tmp_results, key=lambda k: k["lastChange"], reverse=True
            )

            # Store the resulting sorted list using the brightway names
            key = exchange_type.value["bw"]
            if not key:
                print(
                    "Warning: brightway key for "
                    + exchange_type
                    + " not specified, using olca key instead."
                )
                key = exchange_type.value["olca"]

            results[key] = tmp_results

        return results

    def post(self, method, params):
        """
        Performs a request with the given parameters.
        It returns a tuple (result, error).
        """
        req = {"jsonrpc": "2.0", "id": self.next_id, "method": method, "params": params}
        self.next_id += 1
        resp = requests.post(self.url, json=req).json()  # type: dict
        err = resp.get("error")  # type: dict
        if err is not None:
            err_msg = "%i: %s" % (err.get("code"), err.get("message"))
            return None, err_msg
        result = resp.get("result")
        if result is None:
            err_msg = "No error and no result: invalid JSON-RPC response"
            return None, err_msg
        return result, None
