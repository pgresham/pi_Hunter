from pexpect import pxssh
from os import system
import ipaddress 

system('clear')
print('    ppppp   ii      HH    HH  UU    UU   NN    NN  TTTTTTTT  EEEEEEEE  RRRRR\n   p   p            HH    HH  UU    UU   NNN   NN     TT     EE        RR   RR\n  ppppp   ii        HH    HH  UU    UU   NN N  NN     TT     EE        RR   RR\n p       ii         HHHHHHHH  UU    UU   NN  N NN     TT     EEEEEE    RRRRRRR\np      ii           HH    HH  UUU  UUU   NN   NNN     TT     EE        RR  RR\n                    HH    HH   UU  UU    NN    NN     TT     EE        RR   RR\n                    HH    HH   UUUUUU    NN     N     TT     EEEEEEEE  RR    RR\n\n')
print(79*'-'+'\nThis tool scans an IP block for any Raspberry pi running SSH with default creds\n'+79*'-')
m = -1
print('\n4. IPv4 Addressing\n\n6. IPv6 Addressing\n\n0. Exit')
while(m!=0):
	
	while m != 4 and m != 6 and m != 0:
		try:
			m = int(input(':'))
		except:
			print('try again')
	
			
	if m == 0:
		break	
	
	if m == 4:
		catch = 0
		while catch ==0:
			try:
				u = ipaddress.IPv4Address(str(input('Enter start IPv4 Address: ')).strip())
				v = ipaddress.IPv4Address(str(input('Enter end IPv4 Address: ')).strip())
				if int(v) > int(u):
					catch =1
				else:
					print('try again')
			except:
				print('try again')
		found = []

		system('clear')
		print('    ppppp   ii      HH    HH  UU    UU   NN    NN  TTTTTTTT  EEEEEEEE  RRRRR\n   p   p            HH    HH  UU    UU   NNN   NN     TT     EE        RR   RR\n  ppppp   ii        HH    HH  UU    UU   NN N  NN     TT     EE        RR   RR\n p       ii         HHHHHHHH  UU    UU   NN  N NN     TT     EEEEEE    RRRRRRR\np      ii           HH    HH  UUU  UUU   NN   NNN     TT     EE        RR  RR\n                    HH    HH   UU  UU    NN    NN     TT     EE        RR   RR\n                    HH    HH   UUUUUU    NN     N     TT     EEEEEEEE  RR    RR\n')
		print(79*'-')
		print('Scanning from '+str(u)+' to '+str(v))
		print(79*'-')
		print('\nTrying SSH '+str(u)+'...')
		for i in range(int(u),int(v)):
			try:
				s = pxssh.pxssh()
				
				s.login(str(ipaddress.IPv4Address(i)), 'pi', 'raspberry', sync_multiplier=5) #Multiplier may have to be adjusted
				print('(+) Default Pi Found At'+str(ipaddress.IPv4Address(i)))
				found.append(str(ipaddress.IPv4Address(i)))
				s.logout()
			except:
				system('clear')
				print('    ppppp   ii      HH    HH  UU    UU   NN    NN  TTTTTTTT  EEEEEEEE  RRRRR\n   p   p            HH    HH  UU    UU   NNN   NN     TT     EE        RR   RR\n  ppppp   ii        HH    HH  UU    UU   NN N  NN     TT     EE        RR   RR\n p       ii         HHHHHHHH  UU    UU   NN  N NN     TT     EEEEEE    RRRRRRR\np      ii           HH    HH  UUU  UUU   NN   NNN     TT     EE        RR  RR\n                    HH    HH   UU  UU    NN    NN     TT     EE        RR   RR\n                    HH    HH   UUUUUU    NN     N     TT     EEEEEEEE  RR    RR\n')
				print(79*'-')
				print('Scanning from '+str(u)+' to '+str(v))
				print(79*'-')
				print('\nTrying SSH '+str(ipaddress.IPv4Address((i))))
				print('Trying SSH '+str(ipaddress.IPv4Address((i+1)))+'...\n')
				for element in found:
					print('\n\n(+) Default Pi Found At '+element)
 			
	elif m == 6:
		catch = 0
		while catch ==0:
			try:
				u = ipaddress.IPv6Address(str(input('Enter start IPv6 Address: ')).strip())
				v = ipaddress.IPv6Address(str(input('Enter end IPv6 Address: ')).strip())
				if int(v) > int(u):
					catch =1
				else:
					print('try again')
			except:
				print('try again')
		found = []

		system('clear')
		print('    ppppp   ii      HH    HH  UU    UU   NN    NN  TTTTTTTT  EEEEEEEE  RRRRR\n   p   p            HH    HH  UU    UU   NNN   NN     TT     EE        RR   RR\n  ppppp   ii        HH    HH  UU    UU   NN N  NN     TT     EE        RR   RR\n p       ii         HHHHHHHH  UU    UU   NN  N NN     TT     EEEEEE    RRRRRRR\np      ii           HH    HH  UUU  UUU   NN   NNN     TT     EE        RR  RR\n                    HH    HH   UU  UU    NN    NN     TT     EE        RR   RR\n                    HH    HH   UUUUUU    NN     N     TT     EEEEEEEE  RR    RR\n')
		print('Scanning from '+str(u)+' to '+str(v))
		print('\nTrying SSH '+str(u)+'...')
		for i in range(int(u),int(v)):
			try:
				s = pxssh.pxssh()
				s.login(str(ipaddress.IPv6Address(i)), 'pi', 'raspberry',sync_multiplier=5) #Multiplier may have to be adjusted
				print('\n(+) Default Pi Found At '+str(ipaddress.IPv6Address(i)))
				found.append(str(ipaddress.IPv6Address(i)))
				s.logout()
			except:
				system('clear')
				print('    ppppp   ii      HH    HH  UU    UU   NN    NN  TTTTTTTT  EEEEEEEE  RRRRR\n   p   p            HH    HH  UU    UU   NNN   NN     TT     EE        RR   RR\n  ppppp   ii        HH    HH  UU    UU   NN N  NN     TT     EE        RR   RR\n p       ii         HHHHHHHH  UU    UU   NN  N NN     TT     EEEEEE    RRRRRRR\np      ii           HH    HH  UUU  UUU   NN   NNN     TT     EE        RR  RR\n                    HH    HH   UU  UU    NN    NN     TT     EE        RR   RR\n                    HH    HH   UUUUUU    NN     N     TT     EEEEEEEE  RR    RR\n')
				print(79*'-')
				print('Scanning from '+str(u)+' to '+str(v))
				print(79*'-')
				print('\nTrying SSH '+str(ipaddress.IPv6Address((i))))
				print('Trying SSH '+str(ipaddress.IPv6Address((i+1)))+'...')
				for element in found:
					print('(+) Default Pi Found At '+element)

	m = -1
	print('\nDone.\n\n4. IPv4 Addressing\n\n6. IPv6 Addressing\n\n0. Exit')
