import csv
import copy
import ipaddress

txtfile = open("plantilla.txt", "r")
file_data = txtfile.read().split('\n')

with open('db.csv', newline='', encoding='utf-8') as csvfile:
  spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
  for i, row in enumerate(spamreader):
    if i > 0:
      # create new txt file
      #result_txt = open("data"+str(i)+".txt", "a+")
      CVindex = row[0].index('G', 0)
      CV = row[0][:CVindex]
      result_txt = open(CV+".txt", "a+")
      new_file = copy.deepcopy(file_data)
      # get row as list split by comma 
      row = ''.join(row).split(',')
      # get olt
      olt = row[2].strip() + '-' + row[1]
      index = new_file[5].index('XXX') 
      # modify OLT data
      new_file[5] = new_file[5][:index] + olt
      x = row[3].strip()
      ip_lan_network_id = ipaddress.ip_address(x) 
      ip_lan_excluded1 = ipaddress.ip_address(x) + 254
      ip_lan_excluded2 = ipaddress.ip_address(x) + 1
      ip_lan_excluded3 = ipaddress.ip_address(x) + 128
      indexlan = new_file[80].index('10.22.X.')
      new_file[80] = new_file[80][:indexlan] + str(ipaddress.IPv4Address(ip_lan_excluded1))
      new_file[81] = new_file[81][:indexlan] + str(ipaddress.IPv4Address(ip_lan_excluded2)) + ' '+ str(ipaddress.IPv4Address(ip_lan_excluded3))
      networkid = new_file[84].index('10.22.X.0')
      new_file[84] = new_file[84][:networkid] + str(ipaddress.IPv4Address(ip_lan_network_id)) + ' 255.255.255.0'
      defaultrouter = new_file[85].index('10.22')
      new_file[85] = new_file[85][:defaultrouter] + str(ipaddress.IPv4Address(ip_lan_excluded2))
      wanipEx = row[4].strip()
      wanipASR = ipaddress.ip_address(wanipEx) + 1
      wanip921 = ipaddress.ip_address(wanipEx) + 2
      ipindex = new_file[160].index('172.2')
      new_file[160] = new_file[160][:ipindex] + str(ipaddress.IPv4Address(wanip921))+ ' 255.255.255.252'
      ipv6wan = row[6].strip()
      ipv6index = new_file[161].index('2801:')
      new_file[161] = new_file[161][:ipv6index] + ipv6wan + '2/126'
      lanindex = new_file[167].index('10.XX')
      new_file[167] = new_file[167][:lanindex] + str(ipaddress.IPv4Address(ip_lan_excluded2)) + ' 255.255.255.0'
      ipv6lan = row[5].strip()
      ipv6lan_index = new_file[168].index('2801:')
      new_file[168] = new_file[168][:ipv6lan_index] + ipv6lan + '1/64'
      iproute = new_file[172].index('172.')
      new_file[172] = new_file[172][:iproute] + str(ipaddress.IPv4Address(wanipASR)) + ' name DEFAULT_SERVICIO-1_INTERNET'
      iproutev6 = new_file[173].index('2801')
      new_file[173] = new_file[173][:iproutev6] + ipv6wan + '1 name DEFAULT_SERVICIO-1_INTERNET'
      ntp = new_file[203].index('172.')
      new_file[203] = new_file[203][:ntp] + str(ipaddress.IPv4Address(wanipASR))
      print (CV,'Script listo')
      
      result_txt.writelines([l + '\n' for l in new_file])
      result_txt.close()