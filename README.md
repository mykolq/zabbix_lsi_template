# zabbix_lsi_template
## Description

This template is for discovering and monitoring LSI (Avago, Broadcom) storage controllers by using json outputs of storcli tool.
Now it works only with zabbix 4.2

## Main features

* Discovery of controllers, logical discs, physical discs, batteries (bbu an cv) without scripts on servers side (it uses parsing of json
and java scripts on zabbix side)
* Monitoring controllers, logical, physical discs, batteries
* Useful with OS, where storcli works
* Comfortable changing of time intervals by macroses.

## Plans
* Test template with not only Windows and write instruction for other platforms
* Make lld discovery for controllers with javascript (dell servers have some different json paths in storcli outputs).

## Installation

### Zabbix server

* Import template
* Create and configure global macroses:
  * {$ADAP_DISCOVERY_PERIOD} - adapters discovery period. I think you can set it nearly 1d (daily)
  * {$ADAP_HISTORY_PERIOD} - period of saving history for adapters data. For example 30d
  * {$ADAP_REQUEST_PERIOD} - period of requesting storage adapters data ( adapter,battery state, etc). 1h
  * {$INTERNAL_ITEMS_HISTORY_PEIOD} - period of source data for parsing items by json path. Usually 0, but for 
  debugging you can set it higher
  * {$LD_DISCOVERY_PERIOD} - logical discs discovery period. 6h
  * {$LD_HISTORY_PERIOD} - period of saving history for logical discs data. 30d
  * {$LD_REQUEST_PERIOD} - period of requesting logical discs data. 5m
  * {$PD_DISCOVERY_PERIOD} - physical discs discovery period. 30m
  * {$PD_HISTORY_PERIOD} - period of saving history for physical discs data. 30d
  * {$PD_REQUEST_PERIOD} - period of requesting physical discs data. 5m
 * Set template macroses:
   * {$ADAP_THROTTLING_HB_PERIOD} - period of heartbit for throttling for adapter data
   * {$LD_THROTTLING_HB_PERIOD} - period of heartbit for throttling for logical discs data
   * {$PD_THROTTLING_HB_PERIOD} - period of heartbit for throttling for physical discs data.
  
  ### Windows
  
  * Copy storcli utility (you can use version in archive avago.7z) in place where you store things like this
  * Copy lsi_win.conf in zabbix_agent configs folder
  * Edit storcli paths in lsi_win.conf.
  
