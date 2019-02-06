import os;
import glob
print "-------------------------------"
path = './*.pcap'
files = glob.glob(path)
for file in files:
	os.system("tshark -r "+file+" -Y http.request -T fields -e http.request.uri > results.txt")
