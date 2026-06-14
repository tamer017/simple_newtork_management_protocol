# Simple Network Management Protocol (SNMP) Implementation

> **Python implementation of SNMPv2c manager and agent with MIB parsing, OID traversal, GET/GETNEXT/GETBULK/SET operations, and trap listener for network device monitoring.**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![pysnmp](https://img.shields.io/badge/pysnmp-4.4+-blue.svg)](https://pysnmp.readthedocs.io/)
[![Protocol](https://img.shields.io/badge/Protocol-SNMPv2c-green.svg)]()

---

## Overview

This project implements a complete **SNMP (Simple Network Management Protocol) toolkit** covering both the manager and agent sides of network device monitoring. SNMP is the industry-standard protocol for monitoring and managing network infrastructure (routers, switches, servers, printers).

---

## SNMP Architecture

```
┌─────────────────┐         ┌─────────────────┐
│   SNMP Manager    │         │   SNMP Agent      │
│  (this project)   │         │  (network device) │
│                   │         │                   │
│  GET/GETNEXT      │───UDP──►│  MIB-II           │
│  GETBULK/SET      │◄─UDP───│  OID Tree          │
│  Trap Listener    │         │  Trap Generator   │
└─────────────────┘         └─────────────────┘
          Port 161 (queries)    Port 162 (traps)
```

---

## SNMP Operations Implemented

### GET — Retrieve Single OID Value
```python
from pysnmp.hlapi import *

def snmp_get(host, community, oid):
    iterator = getCmd(
        SnmpEngine(),
        CommunityData(community, mpModel=1),  # SNMPv2c
        UdpTransportTarget((host, 161)),
        ContextData(),
        ObjectType(ObjectIdentity(oid))
    )
    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
    if not errorIndication and not errorStatus:
        for varBind in varBinds:
            return str(varBind[1])

# Example: get system description
desc = snmp_get('192.168.1.1', 'public', '1.3.6.1.2.1.1.1.0')
print(f'sysDescr: {desc}')
```

### GETNEXT — OID Tree Walk
```python
def snmp_walk(host, community, oid_base):
    """Walk the entire OID subtree"""
    for errorIndication, errorStatus, errorIndex, varBinds in nextCmd(
        SnmpEngine(),
        CommunityData(community),
        UdpTransportTarget((host, 161)),
        ContextData(),
        ObjectType(ObjectIdentity(oid_base)),
        lexicographicMode=False  # stop at subtree boundary
    ):
        for varBind in varBinds:
            print(f'{varBind[0]} = {varBind[1]}')
```

### GETBULK — Efficient Bulk Retrieval
```python
# Retrieve up to 25 OIDs in a single UDP packet
bulkCmd(..., maxRepetitions=25, nonRepeaters=0)
```

### SET — Modify Device Configuration
```python
# Set interface description
snmp_set('192.168.1.1', 'private',
         '1.3.6.1.2.1.2.2.1.2.1',
         OctetString('WAN Link to ISP'))
```

### Trap Listener
```python
# Async trap receiver on UDP/162
def trap_callback(snmpEngine, stateReference, contextEngineId,
                  contextName, varBinds, cbCtx):
    for name, val in varBinds:
        print(f'Trap OID: {name}, Value: {val}')
```

---

## Common OIDs Monitored

| OID | MIB Object | Description |
|---|---|---|
| `1.3.6.1.2.1.1.1.0` | sysDescr | Device description |
| `1.3.6.1.2.1.1.5.0` | sysName | Device hostname |
| `1.3.6.1.2.1.2.2.1.10.x` | ifInOctets | Interface input bytes |
| `1.3.6.1.2.1.2.2.1.16.x` | ifOutOctets | Interface output bytes |
| `1.3.6.1.2.1.25.3.3.1.2.x` | hrProcessorLoad | CPU utilization % |
| `1.3.6.1.2.1.25.2.3.1.6.x` | hrStorageUsed | Memory/disk used |

---

## Installation

```bash
git clone https://github.com/tamer017/simple_newtork_management_protocol.git
cd simple_newtork_management_protocol
pip install pysnmp
python snmp_manager.py
```

---

## Skills & Concepts

`SNMP` `SNMPv2c` `Network Management` `MIB` `OID` `UDP` `pysnmp` `GET/SET Operations` `Trap Listener` `Network Monitoring` `Infrastructure Automation`

---

## Author

**Ahmed Tamer Assy** — [GitHub](https://github.com/tamer017) | Machine Learning Researcher @ Volkswagen AG
