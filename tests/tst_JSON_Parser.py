# coding: utf8

import unittest
import json

################################
# get the code
with open('framework_helper.py', 'r') as f1, open('../src/11087_JSON_Parser (11087).py', 'r') as f2:
    framework_code = f1.read()
    debug_code = f2.read()

exec (framework_code + debug_code)


################################
# unit tests
class JsonTests(unittest.TestCase):

    def setUp(self):
        self.dummy = JSON_Parser_11087_11087(0)
        self.dummy.on_init()

    def tearDown(self):
        pass

    def test_error_json(self):
        in_json = '{"test":1, "dummy":2 "go": 3}'
        self.dummy.debug_input_value[self.dummy.PIN_I_SJSON] = in_json
        self.dummy.debug_input_value[self.dummy.PIN_I_SKEY] = "go"
        self.dummy.debug_input_value[self.dummy.PIN_I_NIDX] = -1

        self.dummy.on_input_value(self.dummy.PIN_I_SKEY, "go")

        self.assertTrue(True)

    def test_getValue_str(self):
        in_text = '{"siteCurrentPowerFlow":{"updateRefreshRate":3,"unit":"kW","connections":[{"from":"STORAGE",' \
                  '"to":"Load"},{"from":"GRID","to":"Load"}],"GRID":{"status":"Active","currentPower":0.01},' \
                  '"LOAD":{"status":"Active","currentPower":1.37},"PV":{"status":"Idle","currentPower":0.0},' \
                  '"STORAGE":{"status":"Discharging","currentPower":1.36,"chargeLevel":38,"critical":false}}} '

        ok, ret = self.dummy.get_value(in_text, "siteCurrentPowerFlow")
        res = '{"LOAD": {"status": "Active", "currentPower": 1.37}, "PV": {"status": "Idle", "currentPower": 0.0}, ' \
              '"STORAGE": {"status": "Discharging", "critical": false, "chargeLevel": 38, "currentPower": 1.36}, ' \
              '"connections": [{"to": "Load", "from": "STORAGE"}, {"to": "Load", "from": "GRID"}], "GRID": {"status": ' \
              '"Active", "currentPower": 0.01}, "updateRefreshRate": 3, "unit": "kW"} '
        self.assertTrue(ok)
        self.assertEqual(json.loads(ret), json.loads(res))

    def test_getValue_int(self):
        ret = '{"LOAD": {"status": "Active", "currentPower": 1.37}, "PV": {"status": "Idle", "currentPower": 0.0}, ' \
              '"STORAGE": {"status": "Discharging", "critical": false, "chargeLevel": 38, "currentPower": 1.36}, ' \
              '"connections": [{"to": "Load", "from": "STORAGE"}, {"to": "Load", "from": "GRID"}], "GRID": {"status": ' \
              '"Active", "currentPower": 0.01}, "updateRefreshRate": 3, "unit": "kW"} '
        ok, ret = self.dummy.get_value(ret, "updateRefreshRate")
        self.assertTrue(ok)
        self.assertEqual(ret, 3)

    def test_index(self):
        ret = '["LOAD", "Active", "PV"]'
        self.dummy.debug_input_value[self.dummy.PIN_I_SJSON] = ret
        self.dummy.debug_input_value[self.dummy.PIN_I_SKEY] = str()
        self.dummy.debug_input_value[self.dummy.PIN_I_NIDX] = 1

        self.dummy.on_input_value(self.dummy.PIN_I_NIDX, 1)

        ret = self.dummy.debug_output_value[self.dummy.PIN_O_SVALUE]
        self.assertEqual(ret, 'Active')

        ret = '[["LOAD", "Active", "PV"], [1, 2, 3]]'
        self.dummy.debug_input_value[self.dummy.PIN_I_SJSON] = ret

        self.dummy.on_input_value(self.dummy.PIN_I_NIDX, 1)

        ret = self.dummy.debug_output_value[self.dummy.PIN_O_SVALUE]
        self.assertEqual(ret, "[1, 2, 3]")

    def test_key(self):
        ret = '{"LOAD": {"status": "Active", "currentPower": 1.37}, "PV": {"status": "Idle", "currentPower": 0.0}, ' \
              '"STORAGE": {"status": "Discharging", "critical": false, "chargeLevel": 38, "currentPower": 1.36}, ' \
              '"connections": [{"to": "Load", "from": "STORAGE"}, {"to": "Load", "from": "GRID"}], "GRID": {"status": ' \
              '"Active", "currentPower": 0.01}, "updateRefreshRate": 3, "unit": "kW"} '

        self.dummy.debug_input_value[self.dummy.PIN_I_SJSON] = ret
        self.dummy.debug_input_value[self.dummy.PIN_I_SKEY] = "updateRefreshRate"
        self.dummy.debug_input_value[self.dummy.PIN_I_NIDX] = -1

        self.dummy.on_input_value(self.dummy.PIN_I_NIDX, -1)

        ret = self.dummy.debug_output_value[self.dummy.PIN_O_SVALUE]
        self.assertEqual(ret, "3")

        ret = self.dummy.debug_output_value[self.dummy.PIN_O_FVALUE]
        self.assertEqual(ret, 3)

    def test_kaskade(self):
        ret = '{"1": "a", "2":[{"2.1": "b.1", "2.2": "b.2"}, {"2.3": "b.3"}]}'
        self.dummy.debug_input_value[self.dummy.PIN_I_SJSON] = ret
        self.dummy.debug_input_value[self.dummy.PIN_I_NIDX] = -1
        self.dummy.debug_input_value[self.dummy.PIN_I_SKEY] = "2"

        self.dummy.on_input_value(self.dummy.PIN_I_SKEY, "2")
        ret = self.dummy.debug_output_value[self.dummy.PIN_O_SVALUE]
        self.assertEqual(json.loads('[{"2.1": "b.1", "2.2": "b.2"}, {"2.3": "b.3"}]'), json.loads(ret))

        self.dummy.debug_input_value[self.dummy.PIN_I_SJSON] = ret
        self.dummy.debug_input_value[self.dummy.PIN_I_NIDX] = 0
        self.dummy.on_input_value(self.dummy.PIN_I_NIDX, 0)
        ret = self.dummy.debug_output_value[self.dummy.PIN_O_SVALUE]
        self.assertEqual(json.loads('{"2.1": "b.1", "2.2": "b.2"}'), json.loads(ret))

        self.dummy.debug_input_value[self.dummy.PIN_I_SJSON] = ret
        self.dummy.debug_input_value[self.dummy.PIN_I_NIDX] = -1
        self.dummy.debug_input_value[self.dummy.PIN_I_SKEY] = "2.2"
        self.dummy.on_input_value(self.dummy.PIN_I_SKEY, "2.2")
        ret = self.dummy.debug_output_value[self.dummy.PIN_O_SVALUE]

        self.assertEqual("b.2", ret)

    def test_unicode(self):
        in_val = u'{"2.1": "Äö", "2.2": "b.2"}'

        ok, ret = self.dummy.get_value(in_val, "2.1")
        res = '&#196;&#246;'
        self.assertTrue(ok)
        self.assertEqual(ret, res)
        ok, ret = self.dummy.get_value(in_val, u"2.1")
        self.assertTrue(ok)
        self.assertEqual(ret, res)
        ok, ret = self.dummy.get_value(in_val, u"2.2")
        self.assertTrue(ok)
        self.assertEqual(ret, "b.2")


if __name__ == '__main__':
    unittest.main()
