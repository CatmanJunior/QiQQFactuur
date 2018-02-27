import PyPDF2, os
import csv
# import urllib2, urllib

pdfList = []

reader = csv.reader(open('Book1.csv', 'r'))

debit = []

for line in reader:
	debit.append(line)

# print (debit)





class Voip:
	def __init__(self, name, price, spec):
		self.name = name
		self.price = price
		self.spec = spec
		self.getID()
		# self.id = 0

	def printvoip(self):
		print("Naam: " + self.name)
		print("Kosten " + self.price)
		print("Specificatienummer: " + self.spec)
		print("ID: " + str(self.id))
		print()

	def getID(self):
		for line in debit:
			# print(line[0])
			if line[0] == self.name:
				self.id = line[1]

	# def postPhp(self):
		
	# 	mydata=[('id',self.name),('cost',self.price), ('spec', self.spec)]    #The first is the var name the second is the value
	# 	mydata=urllib.urlencode(mydata)
	# 	path='http://localhost/new.php'    #the url you want to POST to
	# 	req=urllib2.Request(path, mydata)
	# 	req.add_header("Content-type", "application/x-www-form-urlencoded")
	# 	page=urllib2.urlopen(req).read()
	# 	print (page)

voiplist = []

for filename in os.listdir('.'):
	if filename.endswith('.pdf'):
		pdfList.append(filename)

for file in pdfList:
	pdfFile = open (file, 'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFile)
	page = pdfReader.getPage(0)
	text = page.extractText()
	name = text[:text.find ('\n')]
	line = text.find("Gesprekskostenindeafgelopenperiode")
	lineb = text.find('\n', line+3) + 1
	linec = text.find('EUR', lineb+3)
	price = text[lineb:linec]
	#print(page.extractText())

	line = text.find("Specificatienummer")
	lineb = text.find('\n', line+3) + 1
	linec = text.find('\n', lineb+3)
	spec = text[linec-7:linec]

	nv = Voip(name, price, spec)
	voiplist.append(nv)




for v in voiplist:
	v.printvoip()



