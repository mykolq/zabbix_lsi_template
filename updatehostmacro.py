#!/usr/bin/python3

import sys,json,ast,re,base64,argparse,ssl
from pyzabbix import ZabbixAPI
import traceback
import subprocess

#this is for debug. If you need to debug delete next line and line with three odrinary qoutes after import logging
''' this is for debug request to zabbix api
import logging
'''


# Below we replacing argparse errors
class ArgumentParserError(Exception): pass

class ThrowingArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        raise ArgumentParserError(message)
		


parser = ThrowingArgumentParser()

parser.add_argument('--zbxurl', help = "URL to the zabbix server (example: https://monitor.example.com/zabbix)", dest = "zbxurl", required = True)
parser.add_argument('--zbxuser', help = "Zabbix api writer user", dest = "apiuser", required = True)
parser.add_argument('--zbxpass', help = "Zabbix api writer password", dest = "apipass", required = True)
parser.add_argument('--host', help = "DNS name of host", dest = "host", required = True)
parser.add_argument('--macroname', help = "Name of macro", dest = "macro_name", required = True)
parser.add_argument('--macrovalue', help = "Macro value", dest = "macro_value", required = True)
parser.add_argument('--valuetype', help = "Type of value for macro. Now needed if you need to set json in macro", dest = "value_type")

try:
	args = parser.parse_args()
	zbxurl = args.zbxurl
	apiuser = args.apiuser
	apipass = args.apipass
	host = args.host
	macro_name = "{{${}}}".format(args.macro_name)
	macro_value = args.macro_value
	
	if args.value_type is not None:
		value_type = args.value_type
		if value_type == 'JSON':
			macro_value = re.sub(r'"','\"',macro_value)
		else:
			macro_value = macro_value
	
	#this is for debug. If you need to debug delete next line and line with three odrinary qoutes after log.setLevel
	'''
	stream = logging.StreamHandler(sys.stdout)
	stream.setLevel(logging.DEBUG)
	log = logging.getLogger('pyzabbix')
	log.addHandler(stream)
	log.setLevel(logging.DEBUG)
	'''

	
	zabbix = ZabbixAPI(zbxurl, user = apiuser, password = apipass)
	zabbix.session.verify = False
	
	hid=zabbix.host.get(search={'host': host})[0]['hostid']
	macros=zabbix.usermacro.get(hostids=hid, output=['value'], filter={'macro':macro_name})
	if len(macros)==0:
		zabbix.usermacro.create(hostid=hid,macro=macro_name,value=macro_value)
	else:
		zabbix.usermacro.update(hostmacroid=macros[0]['hostmacroid'],value=macro_value)
	
except Exception as ex:
	err = "Exception: {}\nTrace:".format(ex, traceback.format_exc())
	print (err)
	sys.exit(0)	




