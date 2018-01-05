import requests
import bs4
import csv


def grabSite(url):
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	return requests.get(url, headers=headers)

class spinxAPI(object):
	#placeholder bot class - will eventually merge a ton of stuff into this
	def __init__(self, defaultStore=None):
		self.updateDatapoints()

	def updateDatapoints(self):
		self.Datapoints = []
		self.Data = {}
		res = requests.get('http://zingon-data.com/spinx/prices.csv')
		decoded_content = res.content.decode('utf-8')
		cr = csv.reader(decoded_content.splitlines(), delimiter=',')
		my_list = list(cr)
		for row in my_list:
			newVal = []
			for val in row:
				if len(val.strip()) > 2:
					newVal.append(val.strip())
			if len(newVal) > 1:
				self.Datapoints.append(newVal)
		for val in self.Datapoints:
			self.Data[val[0]] = {}
		for val in self.Datapoints:
			self.Data[val[0]][val[2]] = val[3]

	def displayPricing(self):
		if len(self.Datapoints) == 0:
			self.updateDatapoints()
		else:
			for val in self.Datapoints:
				print val

	def printData(self):
		print self.Data




if __name__ == '__main__':
	a = spinxAPI()
	a.printData()

