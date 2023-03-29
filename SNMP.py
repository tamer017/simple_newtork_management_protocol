from pysnmp.hlapi import *


# SNMP GET operation
def GET(ip_address, community_string, port_number, OID):
    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
            CommunityData(community_string),
            UdpTransportTarget((ip_address, port_number)),
            ContextData(),
            ObjectType(ObjectIdentity(OID+".0"))
            )
    )
    if errorIndication:
        return errorIndication
    elif errorStatus:
        return '%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?')
    else:
        for varBind in varBinds:
            return ' = '.join([x.prettyPrint() for x in varBind])

# SNMP SET operation
def SET(ip_address, community_string, port_number, OID,Value):
    errorIndication, errorStatus, errorIndex, varBinds = next(
        setCmd(SnmpEngine(),
            CommunityData(community_string),
            UdpTransportTarget((ip_address, port_number)),
            ContextData(),
            ObjectType(ObjectIdentity(OID+".0"),Value)
            )
    )
    if errorIndication:
        return errorIndication
    elif errorStatus:
        return '%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?')
    else:
        for varBind in varBinds:
            return ' = '.join([x.prettyPrint() for x in varBind])
            

# SNMP GETNEXT operation
def GETNEXT(ip_address, community_string, port_number, OID):
    errorIndication, errorStatus, errorIndex, varBinds = next(
        nextCmd(
            SnmpEngine(),
            CommunityData(community_string),
            UdpTransportTarget((ip_address, port_number)),
            ContextData(),
            ObjectType(ObjectIdentity(OID+".0"))
    ))
    if errorIndication:
        return errorIndication
    elif errorStatus:
        return '%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?')
    else:
        for varBind in varBinds:
            return ' = '.join([x.prettyPrint() for x in varBind])
# ip_address = '127.0.0.1'
# community_string = 'Tamer'
# port_number = 161
# OID = "1.3.6.1.2.1.1.5"
# Value = "LAPTOP-QAOOUQTU"
# # GETNEXT(ip_address, community_string, port_number, OID)
# GET(ip_address, community_string, port_number, OID)
# # SET(ip_address, community_string, port_number, OID,Value)

