import urllib
import datetime
import os

print "********************************************"
print "*                                          *"
print "*            Drag N Drop Updater           *"
print "*                                          *"
#print "*           Press enter to update          *"
print "********************************************"

#gives log time stamp
open("log.txt", 'a').write(datetime.datetime.now().ctime())

#this functions downloads new files
def download():
	outf = open('log.txt', 'a')
	print outf
	error = "  Error: Unable to download file"
	count = 0

	print "Downloading new files"

	RogueKiller32 = urllib.URLopener()
	print "  Downloading RogueKiller32"
	try:
		RogueKiller32.retrieve("http://download.adlice.com/RogueKiller/RogueKiller.exe", "RogueKiller32.exe")
		print "  Done"
		outf.write('\nRogueKiller32 downloaded\n')
	except:
		print error
		count = count + 1
		outf.write('\nRogueKiller32 failed to download\n')
		pass

	RogueKiller64 = urllib.URLopener()
	print "  Downloading RogueKiller64"
	try:
		RogueKiller64.retrieve("http://download.adlice.com/RogueKiller/RogueKillerX64.exe", "RogueKillerX64.exe")
		print "  Done"
		outf.write('RogueKillerX64 downloaded\n')
	except:
		print error
		count = count + 1
		outf.write('RogueKillerX64 failed to download\n')
		pass

	AdwareCleaner = urllib.URLopener()
	print "  Downloading AdwareCleaner"
	try:
		AdwareCleaner.retrieve("http://download.bleepingcomputer.com/dl/8360ae6d977500acedc6c71011d72081/569002db/windows/security/security-utilities/a/adwcleaner/AdwCleaner.exe", "AdwareCleaner.exe")
		print "  Done"
		outf.write('AdwareCleaner downloaded\n')
	except:
		print error
		count = count + 1
		outf.write('AdwareCleaner failed to download\n')
		pass

	NiniteMalSuper = urllib.URLopener()
	print "  Downloading Ninite Installer for Malwarebytes and Super Anti Spyware"
	try:
		NiniteMalSuper.retrieve("https://ninite.com/malwarebytes-super/ninite.exe", "Ninite MalwareBytes Super.exe")
		print "  Done"
		outf.write('NiniteMalSuper downloaded\n')
	except:
		print error
		count = count + 1
		outf.write('NiniteMalSuper failed to download\n')
		pass

	NiniteEssentials = urllib.URLopener()
	print "  Downloading Ninite Installer for Security Essentials"
	try:
		NiniteEssentials.retrieve("https://ninite.com/essentials/ninite.exe", "Ninite Security Essentials.exe")
		print "  Done"
		outf.write('NiniteEssentials downloaded\n')
	except:
		print error
		count = count + 1
		outf.write('NiniteEssentials failed to download\n')
		pass

	NiniteTeam = urllib.URLopener()
	print "  Downloading Ninite Installer for TeamViewer"
	try:
		NiniteTeam.retrieve("https://ninite.com/teamviewer/ninite.exe", "Ninite TeamViewer.exe")
		print "  Done"
		outf.write('NiniteTeam downloaded\n')
	except:
		print error
		count = count + 1
		outf.write('NiniteTeam failed to download\n')
		pass

	#ccleaner = urllib.URLopener()
	#print "  Downloading CCleaner"
	#try:
	#	ccleaner.retrieve("http://files.downloadnow.com/s/software/14/49/30/77/ccsetup513.exe?token=1451967159_d30ecc05e3454eb4bb3f6379984aca1b&fileName=ccsetup513.exe", "CCleaner.exe")
	#	print "  Done"
	#	outf.write('CCleaner downloaded\n')
	#except:
	#	print error
	#	count = count + 1
	#	outf.write('CCleaner failed to download\n')
	#	pass

	poweliks = urllib.URLopener()
	print "  Downloading ESETPoweliksCleaner.exe"
	try:
		poweliks.retrieve("http://download.eset.com/special/ESETPoweliksCleaner.exe", "ESETPoweliksCleaner.exe")
		print "  Done"
		outf.write('ESETPoweliksCleaner downloaded\n')
	except:
		print error
		count = count + 1
		outf.write('ESETPoweliksCleaner failed to download\n')
		pass

	eset = urllib.URLopener()
	print "  Downloading ESET Smart Installer"
	try:
		eset.retrieve("http://download.eset.com/special/eos/esetsmartinstaller_enu.exe", "ESET Smart Installer.exe")
		print "  Done"
		outf.write('esetsmartinstaller_enu downloaded\n')
	except:
		print error
		count = count + 1
		outf.write('esetsmartinstaller_enu failed to download\n')
		pass

	print "  "
	print "Files downloaded"
	print str(count) + " file(s) failed to download because u ar an feggit"
	outf.write(str(count) + ' file(s) failed to download\n')

#raw_input()

print " "

download()

outf = open('log.txt', 'a')
outf.write("-------------------------------------------------------------\n")

print " "
print "Drag N Drop has been successfully updated. log.txt has been updated."

print " "
print "********************************************"
print "*            Coded By Max Spehr            *"
print "*               Need A Nerd                *"
print "*                                          *"
print "*           Press Enter to Quit            *"
print "********************************************"

raw_input()
