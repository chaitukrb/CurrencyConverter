class Convert:
	def cal(self, a,b,k=1):
		try:
			from __init__ import data
			a=a.upper()
			b=b.upper()
			if(a!='india' and b!='india'):
				x=data[a][1]
				y=data[b][1]
				return str((x/y))+' '+data[b][0]+'s',1
			else:
				if(a=='india'):
					return str(1/data[b][1])+' '+data[b][0]+'s',1
				else:
					return str(data[a][1])+' '+data[a][0]+'s',1
		except ConnectionError:
			return('Error:please check your Internet Connection!',0)
		except KeyError:
			return('Sorry,the data for your request is not available!',0)
		except:
			return('Sorry,problem in the source for the application!',0)