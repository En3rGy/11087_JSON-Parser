# coding: UTF-8
import json

##!!!!##################################################################################################
#### Own written code can be placed above this commentblock . Do not change or delete commentblock! ####
########################################################################################################
##** Code created by generator - DO NOT CHANGE! **##

class JSON_Parser_11087_11087(hsl20_4.BaseModule):

    def __init__(self, homeserver_context):
        hsl20_4.BaseModule.__init__(self, homeserver_context, "hsl20_4_json")
        self.FRAMEWORK = self._get_framework()
        self.LOGGER = self._get_logger(hsl20_4.LOGGING_NONE,())
        self.PIN_I_SJSON=1
        self.PIN_I_SKEY=2
        self.PIN_I_NIDX=3
        self.PIN_O_SVALUE=1
        self.PIN_O_FVALUE=2

########################################################################################################
#### Own written code can be placed after this commentblock . Do not change or delete commentblock! ####
###################################################################################################!!!##

    def get_list_element(self, s_json, n_index):
        json_file = json.loads(s_json)

        if isinstance(json_file, list):
            if n_index < len(json_file):
                val = json_file[n_index]
                if isinstance(val, unicode):
                    return True, val.encode("ascii", "xmlcharrefreplace")
                else:
                    return True, json.dumps(val)

        return False, "{}"

    def get_value(self, json_file, key):
        """

        :param json_file:
        :type json_file: unicode or non-unicode string
        :param key:
        :type key: non-unicode string
        :return:
        """
        try:
            json_file = json.loads(json_file)
        except ValueError as e:
            self.DEBUG.add_message('In get_value:129, "{}" with \n{}'.format(e.message, json_file))
            return False, str()

        if not isinstance(key, unicode):
            key = key.decode('utf-8')

        ret = ""
        if key in json_file:
            val = json_file[key]

            if isinstance(val, dict) or isinstance(val, list):
                ret = json.dumps(val)
            else:
                ret = val

            if isinstance(ret, unicode):
                ret = ret.encode("ascii", "xmlcharrefreplace")

        else:
            self.DEBUG.add_message("Error: Key not found.")
            return False, ""

        return True, ret

    def on_init(self):
        self.DEBUG = self.FRAMEWORK.create_debug_section()

    def on_input_value(self, index, value):
        s_json = self._get_input_value(self.PIN_I_SJSON)
        if s_json == str():
            self.DEBUG.add_message("No json data set.")
            return

        s_key = self._get_input_value(self.PIN_I_SKEY)
        n_idx = self._get_input_value(self.PIN_I_NIDX)

        if s_key == str() and n_idx < 0:
            self.DEBUG.add_message("No key of index set.")
            return

        val = ""

        self.DEBUG.set_value("Json", str(s_json))
        self.DEBUG.set_value("Index", str(n_idx))
        self.DEBUG.set_value("Key", str(s_key))

        if n_idx >= 0:
            self.DEBUG.add_message("Index requested")
            ok, val = self.get_list_element(s_json, n_idx)
        else:
            self.DEBUG.add_message("Value requested")
            ok, val = self.get_value(s_json, s_key)

        if not ok:
            return

        # handle unicode representation
        if isinstance(val, str):
            val = val.replace("u'", '"')
            val = val.replace("'", '"')
            val = val.replace(": False", ': false')
            val = val.replace(": True", ': true')
        try:
            self._set_output_value(self.PIN_O_FVALUE, float(val))
        except:
            pass

        self._set_output_value(self.PIN_O_SVALUE, str(val).encode("ascii", "xmlcharrefreplace"))
