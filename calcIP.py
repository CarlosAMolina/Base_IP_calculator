def str2list(STRing):    # each element separed by dot
    parts = STRing.split('.')    # parts=['0','1','2','3']
    List = []
    List.append(int(parts[0]))
    List.append(int(parts[1]))
    List.append(int(parts[2]))
    List.append(int(parts[3]))
    return List        #  list=[0,1,10,11], int elements

def listInt2Bin(listInt):
    listBin = []
    listBin.append(bin(listInt[0]))
    listBin.append(bin(listInt[1]))
    listBin.append(bin(listInt[2]))
    listBin.append(bin(listInt[3]))
    return listBin        #  listBin=[0,1,10,11]

def ipANDmac(ip, mac):    # AND operator at each bit of int elements of lists 
    ipAndMac = []
    ipAndMac.append(ip[0]&mac[0])
    ipAndMac.append(ip[1]&mac[1])
    ipAndMac.append(ip[2]&mac[2])
    ipAndMac.append(ip[3]&mac[3])
    return ipAndMac

def list2string(List):
    return '%s.%s.%s.%s' %(List[0],List[1],List[2],List[3])

def bits4hostsInAPart(macPart):    #mac=part0.part1.part2.part3, each part = 8bits
    hostsBits = 0
    multi = 1    # searchs 0's at masc
    while (len(bin(multi))-2)<=8:    # bin(multi)='0b..'
        if macPart&multi==0:
            hostsBits += 1
        else:
            return hostsBits
        multi = multi << 1
    return hostsBits

def bits4hosts(macList):     #mac=part0.part1.part2.part3, each part = 8bits
    macPart = 3
    hostsBits = bits4hostsInAPart(macList[macPart])
    while hostsBits%8 == 0 and macPart>0:
        macPart -= 1
        hostsBits += bits4hostsInAPart(macList[macPart])
    return hostsBits

import sys
while (1):
    sintaxisOK = False
    while sintaxisOK == False:
        ipMasc = raw_input('Escriba ip/mascara (ejm 192.168.1.5/255.255.255.0): ')
        try:
            ip = ipMasc.split('/')[0]    # ip = '0.1.2.3'
            mac = ipMasc.split('/')[1]    # mac = 24
            sintaxisOK = True
        except:
            print 'sintaxis incorrecta'
    ipList = str2list(ip)
    macList = str2list(mac)
    ipBin = listInt2Bin(ipList)
    macBin = listInt2Bin(macList)
    ipBaseList = ipANDmac(ipList,macList)
    ipBase = list2string(ipBaseList)
    bits4Hosts = bits4hosts(macList)
    masc = 32-bits4Hosts
    print 'ip_base/masc: '+ str(ipBase) +'/'+str(masc)
