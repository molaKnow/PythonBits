import subprocess, os, threading
def checkLength(fileCount):
	print "...checking..."
	if fileCount % 12 != 0: #12 is unique to the number of slides per scanning plate
		subprocess.Popen(['open', "/Applications/Epson Software/EPSON Scan.app"])

def CheckApp():
	path, dirs, files = os.walk("/Users/michaelmolyneaux/Desktop/BB Slides/BB Slides 80-81").next()
	fileCount = len(files)
	if fileCount <= 60: #shuts the app down after every scan, so you do have to self-increment	
		threading.Timer(8.0, CheckApp).start()
		checkLength(fileCount)
	else: 
		print "All files in folder"




CheckApp()
