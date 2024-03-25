# zabbix_lsi_template for agent 2 module
## Description

This template is for discovering and monitoring LSI based (Avago, Broadcom, Perc, Lenovo) storage controllers by using json outputs of storcli64 and perccli64 tool, preproccessed with agent 2 module.
Now it works only with zabbix 6.4 and higher

## Main features

* Discovery of controllers, logical discs, physical discs, batteries (bbu and cv)
* Monitoring controllers, logical, physical discs, batteries
* Useful with OS, where storcli64 and perccli64 works
* Overrides for reducing non supported items
* Comfortable changing of time intervals by macroses.
* Can get info about controllers, logical discs, physical discs, batteries by one master metric (if it is possible)

## Installation

### Zabbix server

* Import template
* Create and configure global or template macroses:
  * {$ADAP_DISCOVERY_PERIOD} - adapters discovery period. I think you can set it nearly 1d (daily)
  * {$ADAP_HISTORY_PERIOD} - period of saving history for adapters data. For example 30d
  * {$ADAP_REQUEST_PERIOD} - period of requesting storage adapters data ( adapter,battery state, etc). 1h
  * {$LD_DISCOVERY_PERIOD} - logical discs discovery period. 6h
  * {$LD_HISTORY_PERIOD} - period of saving history for logical discs data. 30d
  * {$LD_REQUEST_PERIOD} - period of requesting logical discs data. 5m
  * {$PD_DISCOVERY_PERIOD} - physical discs discovery period. 30m
  * {$PD_HISTORY_PERIOD} - period of saving history for physical discs data. 30d
  * {$PD_REQUEST_PERIOD} - period of requesting physical discs data. 5m
   * {$ADAP_THROTTLING_HB_PERIOD} - period of heartbit for throttling for adapter data
   * {$LD_THROTTLING_HB_PERIOD} - period of heartbit for throttling for logical discs data
   * {$PD_THROTTLING_HB_PERIOD} - period of heartbit for throttling for physical discs data.

*For automating changes of template macro you have to do instructions below or doing something like that by yourself:
  * Create user for API. This user must have write access for changing settings of servers, monitoring by this template.
  * Install pyzabbix module for you default python version (Something like pip install pyzabbix)
  * Copy updatehostmacro.py script to your zabbix external script folder
  * Than you have to create macroses (i use global) for login and password of this user. Create macros for zabbix server URL.
  For example: {$ZBX_API_WRITER_USER}, {$ZBX_API_WRITER_PASSWORD}, {$ZBX_URL}. Zabbix url macros must equal something like that: http://zabbix_server_address/zabbix
  * Create script 'Update hostmacro' (Administration-Scripts) with command (check your file path) 
  /usr/bin/python3 /zabbixexternalscripts/updatehostmacro.py "--zbxurl" "{$ZBX_URL}" "--zbxuser" "{$ZBX_API_WRITER_USER}" "--zbxpass" '{$ZBX_API_WRITER_PASSWORD}' "--host" "{HOST.HOST}" "--macroname" "{EVENT.TAGS.MACRONAME}" "--macrovalue" '{EVENT.TAGS.MACROVALUE}'  "--valuetype" "{EVENT.TAGS.VALUETYPE}"
  * Create action with name like "Change macro value on host" and condition "Value of tag ACTION equals Change macro value on host"
  * Add step for execution 'Update hostmacro' script
  
  
### Agent servers

Just use module from here https://github.com/mykolq/zabbix_agent2_plugins/tree/main/lsi 