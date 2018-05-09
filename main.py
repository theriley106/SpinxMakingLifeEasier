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
				print val[0]

	def DB(self):
		DB = []
		for key, val in self.Data.items():
			if str(key) != '9128':
				info = {}
				info["Number"] = key
				info["Options"] = []
				for e, z in self.Data[key].items():
					info["Options"].append({"Name": e, "Price": float(z)})
				DB.append(info)
				info["Price"] = "Error"
				for val in info["Options"]:
					if val['Name'] == 'Unleaded 87':
						info["Price"] = val["Price"]
		return DB



if __name__ == '__main__':
	a = spinxAPI()
	print a.DB()

