# coding: utf8

import unittest




import json


class tst():

    def getListElement(self, sJson, nIndex ):
        jsonFile = json.loads(sJson)

        if isinstance(jsonFile, list):
            if (nIndex<len(jsonFile)):
                return json.dumps(jsonFile[nIndex])

        return "{}"

    def getValue(self, sJson, sKey ):
        jsonFile = json.loads(sJson)
        ret = ""
        if sKey in jsonFile:
            val = jsonFile[sKey]

            if (isinstance( val, dict) 
                or isinstance( val, list)):
                ret = json.dumps(val)
            else:
                ret = val
        else:
            self.DEBUG.add_message("Error: Key not found.")

        if isinstance(ret, str):
            ret = ret.encode("ascii", "xmlcharrefreplace")

        return ret


################################################################################


class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        pass

    def test_getValue_str(self):
        dummy = tst()
        inText = '{"siteCurrentPowerFlow":{"updateRefreshRate":3,"unit":"kW","connections":[{"from":"STORAGE","to":"Load"},{"from":"GRID","to":"Load"}],"GRID":{"status":"Active","currentPower":0.01},"LOAD":{"status":"Active","currentPower":1.37},"PV":{"status":"Idle","currentPower":0.0},"STORAGE":{"status":"Discharging","currentPower":1.36,"chargeLevel":38,"critical":false}}}'
        ret = dummy.getValue(inText, "siteCurrentPowerFlow")
        res = '{"LOAD": {"status": "Active", "currentPower": 1.37}, "PV": {"status": "Idle", "currentPower": 0.0}, "STORAGE": {"status": "Discharging", "critical": false, "chargeLevel": 38, "currentPower": 1.36}, "connections": [{"to": "Load", "from": "STORAGE"}, {"to": "Load", "from": "GRID"}], "GRID": {"status": "Active", "currentPower": 0.01}, "updateRefreshRate": 3, "unit": "kW"}'
        self.assertEqual(ret, res)

    def test_getValue_int(self):
        dummy = tst()
        ret = '{"LOAD": {"status": "Active", "currentPower": 1.37}, "PV": {"status": "Idle", "currentPower": 0.0}, "STORAGE": {"status": "Discharging", "critical": false, "chargeLevel": 38, "currentPower": 1.36}, "connections": [{"to": "Load", "from": "STORAGE"}, {"to": "Load", "from": "GRID"}], "GRID": {"status": "Active", "currentPower": 0.01}, "updateRefreshRate": 3, "unit": "kW"}'
        ret = dummy.getValue(ret, "updateRefreshRate")
        self.assertEqual(ret, 3)


if __name__ == '__main__':
    unittest.main()
