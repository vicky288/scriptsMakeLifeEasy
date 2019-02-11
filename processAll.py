import myconfig
import datetime
import urllib2
import zipfile
import csv
import os
from shutil import copyfile

def downloadFileUsingURL(url, destFileName):
	dateString = datetime.date.today()
	#Download content
	resp = urllib2.urlopen(url)
	data = resp.read()
	# Write binary data to file
	fileHandle = open(destFileName, 'wb')
	fileHandle.write(data)
	fileHandle.close()


def unzipFile(zipfileName, destDir):
	zipHandle = zipfile.ZipFile(zipfileName, 'r')
	zipHandle.extractall(destDir)
	zipHandle.close()


def downloadAndExtractZip(url,destFolder,zipFileName):
	try:  
	    os.mkdir(destFolder)
	except OSError:  
	    print ("Folder Exists")
	else:  
	    print ("Successfully created the directory")
	destZipFilePath = destFolder + "/" + zipFileName
	downloadFileUsingURL(url,destZipFilePath)
	unzipFile(destZipFilePath, destFolder)


def extractFieldFromCSV(folderPath, csvFileName, newTextFileName, fieldNum):
	destTextFilePath = folderPath + "/" + newTextFileName
	csvFilePath = folderPath + "/" + csvFileName
	fileHndl = open(destTextFilePath, "w")
	with open(csvFilePath) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		line_count = 0
	  	for row in csv_reader:
	    		fileHndl.write(row[fieldNum-1]+"\n")
	fileHndl.close()


def copyToTopSites(folderName, fileName):
	dest = myconfig.topSites + "/" + fileName
	src = folderName + "/" + fileName
	copyfile(src, dest)

def main():
	"""Downlaod and Extract Alexa zip"""
	#downloadAndExtractZip(myconfig.alexaUrl,myconfig.alexaFolder,myconfig.alexaZipFile)
	"""Extract 1m domain names to a txt file"""
	#extractFieldFromCSV(myconfig.alexaFolder, myconfig.alexa1mcsv, myconfig.alexa1mtxt, 2)


	"""Downlaod and Extract Cisco Umbrella zip"""
	#downloadAndExtractZip(myconfig.ciscoUrl,myconfig.ciscoFolder,myconfig.ciscoZipFile)
	"""Extract 1m domain names to a txt file"""
	#extractFieldFromCSV(myconfig.ciscoFolder, myconfig.cisco1mcsv, myconfig.cisco1mtxt, 2)


	"""Downlaod Majestic csv"""
	try:  
	    os.mkdir(myconfig.majesticFolder)
	except OSError:  
	    print ("Folder Exists")
	else:  
	    print ("Successfully created the directory")
	majesticFile = myconfig.majesticFolder + "/" +myconfig.majestic1mcsv
	#downloadFileUsingURL(myconfig.majesticUrl,majesticFile)
	"""Extract 1m domain names to a txt file"""
	#extractFieldFromCSV(myconfig.majesticFolder, myconfig.majestic1mcsv, myconfig.majestic1mtxt, 3)



	"""Copy Files to TopSites location of DGA"""
	copyToTopSites(myconfig.alexaFolder, myconfig.alexa1mtxt)
	copyToTopSites(myconfig.ciscoFolder, myconfig.cisco1mtxt)
	copyToTopSites(myconfig.majesticFolder, myconfig.majestic1mtxt)



main()





























