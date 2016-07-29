import psutil
Pname = 'GoogleSearch.py'
for proc in psutil.process_iter():
	proclist =  proc.name
	print proclist

