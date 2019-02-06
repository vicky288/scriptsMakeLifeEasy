"""
Created this script to process more than 200 attack pcaps.
It will list the Servlet URIs and corresponding pcaps in sorted order.
"""
import subprocess;
import glob
print "-------------------------------"
path = './*.pcap'
files = glob.glob(path)
file_uri = {}
uri_file_list = []
for file in files:
	batcmd = "tshark -r "+file+" -Y http.request -T fields -e http.request.uri"
	uris = subprocess.check_output(batcmd, shell=True)

	#Find 2nd URI - Servelet Part
	uri_list = uris.split('\n')
	secondURI = uri_list[1]
	uri_list = secondURI.split('/')
	uriString = uri_list[1]
	finalURIParts = uriString.split('?')
	finalURI = finalURIParts[0]

	#Get the File name
	filename_parts = file.split('/')
	filename = filename_parts[1]

	#Add url:file entry	
	uri_file = finalURI + ':' + filename
	uri_file_list.append(uri_file)


uri_file_list.sort()
file_handle = open("list.txt","w")
for uri_file in uri_file_list:
	file_handle.write(uri_file+"\n")
	

