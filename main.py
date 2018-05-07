import requests
import bs4
import csv



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

	def displayPricingAsList(self):
		if len(self.Datapoints) == 0:
			self.updateDatapoints()
		else:
			for val in self.Datapoints:
				print val





if __name__ == '__main__':
	a = spinxAPI()
	a.displayPricingAsList()

