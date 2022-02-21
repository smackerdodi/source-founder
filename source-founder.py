import concurrent.futures
import requests
import threading
import sys
import time
from colorama import Fore, Style
from urllib.parse import urlparse
extensions = ["zip","bak","tar","gizp","rar","7z","iso","bz2","gz","apk","cab","jar","bzip2","deb","ace"]
inputfile=sys.argv[1]
outputfile=sys.argv[2]
output=open(outputfile, "a")
with open(inputfile, "r") as f:
	inputurl = [line.rstrip() for line in f]
threadLocal = threading.local()
count = len(inputurl)
print("number of urls = " + str(count))
def get_session():
    if not hasattr(threadLocal, "session"):
        threadLocal.session = requests.Session()
    return threadLocal.session
def check_sub(url):
	try :
		session=get_session()
		subd = urlparse(url.strip()).netloc
		url2 = url.strip() + "/" + subd
		for ext in extensions :
			url3 = url2 + "." + ext
			res=session.get(url3, timeout=1, allow_redirects=False)
			if str(res.status_code)[0] == "3":
				res3=url3 + " : " + str(res.status_code)
				print(Style.BRIGHT + Fore.WHITE + (url3)+ " : " + Fore.BLUE + str(res.status_code))
				output.write(res3 +"\n")
			elif str(res.status_code)[0] == "2":
				res2=url3 + " : " + str(res.status_code) + " : " + res.headers['Content-Length']
				print(Style.BRIGHT + Fore.GREEN + (url3)+ " : " + str(res.status_code) + " : " + res.headers['Content-Length'] + " bytes")
				output.write(res2 +"\n")
			elif str(res.status_code)[0] == "4":
				res4=url3 + " : " + str(res.status_code) 
				print(Style.BRIGHT + Fore.WHITE + (url3)+ " : " + Fore.YELLOW + str(res.status_code))
				output.write(res4 +"\n")
			elif str(res.status_code)[0] == "5":
				res5=url3 + " : " + str(res.status_code) 
				print(Style.BRIGHT + Fore.WHITE + (url3)+ " : " + Fore.RED + str(res.status_code))
				output.write(res5 +"\n")
			else :
				res6=url3 + " : " + str(res.status_code)
				print(Style.BRIGHT + Fore.WHITE + (url3)+ " : " + Fore.RED + str(res.status_code))
				output.write(res6 +"\n")
	except:
		print(Style.BRIGHT + Fore.WHITE + (url3)+ " : " + Fore.RED+ " : is unreachable")
def itterate_url(inputurl):
	url=inputurl
	check_sub(url)
	
if __name__ == "__main__":
	start_time = time.time()
	with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
       		executor.map(itterate_url, inputurl)
	duration = time.time() - start_time
	print("finished in : " + str(duration) + "  sec")
