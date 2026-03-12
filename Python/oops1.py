class intrest:
	def __init__(self,p,t,r):
		self.p=p
		self.t=t
		self.r=r
	def show(self):
	    print("Principal:",self.p)
	    print("Time:",self.t)
	    print("Rate:",self.r)
	def si(self):
	    return (self.p*self.t*self.r)/100
print("Enter p and t and r")
p=float(input())
t=float(input())
r=float(input())    
s=intrest(p,t,r)
s.show()
print("Simple intrest:",s.si())
	        	