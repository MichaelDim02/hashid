import colorama
from colorama import Fore, Back, Style
import argparse
import sqlite3

def banner():
	print("--hash Hash")

def search(length, chars):
	conn = sqlite3.connect("files/hashes")
	cur = conn.cursor()
	cur.execute("SELECT * FROM hashes WHERE length = ? AND charset = ? ORDER BY popularity DESC", (length, chars))
	print(Style.BRIGHT + Fore.RED + "Possible Hashes:\n")
	count = 1
	for row in cur.fetchall():
		print("["+Fore.WHITE+str(count)+Style.BRIGHT + Fore.RED + "] "+Fore.WHITE+str(row[0]))
		count = count + 1

print("HASHID - Identify the hash!\nBy MihaelDim02")

def extract(hash):
	length = len(hash.strip())
	search(length, "a")

parser = argparse.ArgumentParser()
parser.add_argument("--hash", help="Hash")
args = parser.parse_args()
hash = args.hash

if args.hash:
	extract(hash)
else:
	banner()
