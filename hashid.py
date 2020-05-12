import colorama
from colorama import Fore, Back, Style
import argparse
import sqlite3

def banner():
    print("\n--hash Hash")

def search(length, chars):
    conn = sqlite3.connect("files/hashes")
    cur = conn.cursor()
    cur.execute("SELECT * FROM hashes WHERE length = ? AND charset = ? ORDER BY popularity DESC", (length, chars))
    print("\n" + Style.BRIGHT + Fore.RED + "Possible Hashes:\n")
    count = 1
    for row in cur.fetchall():
        print(Style.BRIGHT + Fore.RED + "["+Fore.WHITE+str(count)+Style.BRIGHT + Fore.RED + "] "+Fore.WHITE+str(row[0]))       
        count = count + 1
    print(" ")
print("          __")
print("(\,------'()'--o  Sniff..")
print(" l_ )  _   /-''    Sniff...")
print("  /_)_) /_)_)\n")
####https://www.asciiart.eu/animals/dogs
print("Houndsniff - Hash Identification Program - Version 0.2\nBy MCD")

def extract(hash):
    length = len(hash.strip())
    charset = "a"
    if hash.startswith("$P$"):
        print("\n"+Style.BRIGHT + Fore.RED + "["+Fore.WHITE+"1"+Style.BRIGHT + Fore.RED + "] "+Fore.WHITE+str("Wordpress hash")+"\n")
        found = True
    elif "$" in hash:
        charset = "b"
    elif "/" in hash:
        charset = "c"
    elif hash[:3] == "0x0":
        charset = "d"
    if not found:
        search(length, charset)

parser = argparse.ArgumentParser()
parser.add_argument("--hash", help="Hash")
args = parser.parse_args()
hash = args.hash

if args.hash:
    extract(hash)
else:
    banner()
