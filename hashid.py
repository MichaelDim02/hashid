import colorama
from colorama import Fore, Back, Style
import argparse
import sqlite3

def banner():
    print("\n--hash Hash")

def list_():
    conn = sqlite3.connect("files/hashes")
    cur = conn.cursor()
    cur.execute("SELECT * FROM hashes")
    print("\nHoundsniff supports:\n")
    for row in cur.fetchall():
        print(row[0])
    print("Wordpress hash\nMD5 crypt(3)\nSHA256 crypt(3)\nSHA512 crypt(3)")
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
print("Houndsniff - Hash Identification Program - Version 0.4\nBy MCD")

def extract(hash):
    length = len(hash.strip())
    charset = "a"
    found = False

    #### DEFINITE GUESS #### These if statements are for hashes with definite identifialbe characteristics
    if hash.startswith("$P$"):
        print("\n"+Style.BRIGHT + Fore.RED + "["+Fore.WHITE+"1"+Style.BRIGHT + Fore.RED + "] "+Fore.WHITE+str("Wordpress hash")+"\n")
        found = True
    elif hash.startswith("$1$"):
        print("\n"+Style.BRIGHT + Fore.RED + "["+Fore.WHITE+"1"+Style.BRIGHT + Fore.RED + "] "+Fore.WHITE+str("MD5 crypt(3)")+"\n")
        found = True
    elif hash.startswith("$5$"):
        print("\n"+Style.BRIGHT + Fore.RED + "["+Fore.WHITE+"1"+Style.BRIGHT + Fore.RED + "] "+Fore.WHITE+str("SHA256 crypt(3)")+"\n")
        found = True
    elif hash.startswith("$6$"):
        print("\n"+Style.BRIGHT + Fore.RED + "["+Fore.WHITE+"1"+Style.BRIGHT + Fore.RED + "] "+Fore.WHITE+str("SHA512 crypt(3)")+"\n")
        found = True
    ### END ###
    elif "$" in hash:
        charset = "b"
    elif "/" in hash:
        charset = "c"
    elif hash[:3] == "0x0":
        charset = "d"
    if not found:
        search(length, charset)

def about():
    print("Houndsniff's not a sniffing tool! ;)")
    print("It is a hash identification & recognition program")
    print("Version 0.4")
    print("Written by MCD")
    print("\nHow it works:")
    print("Houndsniff uses an sqlite database with hashes")
    print("and their characteristics and compares them to")
    print("the characteristics of the given hash. The hases")
    print("are listed by their popularity, which is determined")
    print("by its google results in relation to other hashes")
    print("with the same characteristics.\n\nUse --list to get a list of the supported hashes\n")
    print("If the hash starts with dollarsign ($) make sure you put it between single quote marks :)")

parser = argparse.ArgumentParser()
parser.add_argument("--hash", help="Hash")
parser.add_argument("--about", action="store_true")
parser.add_argument("--list", action="store_true")
args = parser.parse_args()
hash = args.hash

if args.hash:
    extract(hash)
elif args.about:
    about()
elif args.list:
    list_()
else:
    banner()


