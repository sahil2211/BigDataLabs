from rtree import index
import math
import time
import sys

minimumx = 0
minimumy = 0
maximumx = 0 
maximumy = 0


class Point:
	def __init__(self,x,y):
		self.x = x
		self.y = y

class Polygon:
	def __init__(self,points):
		self.points = points
		self.nvert = len(points)
		
		global minimumx 
                global minimumy 
                global maximumx 
                global maximumy 
		
		
		minx = maxx = points[0].x
		miny = maxy = points[0].y
		for i in range(1,self.nvert):
			minx = min(minx,points[i].x)
			miny = min(miny,points[i].y)
			maxx = max(maxx,points[i].x)
			maxy = max(maxy,points[i].y)
		
		minimumx = minx
		minimumy = miny
		maximumx = maxx
		maximumy = maxy
		self.bound = (minx,miny,maxx,maxy)


	def contains(self,pt):
		firstX = self.points[0].x
		firstY = self.points[0].y
		testx = pt.x
		testy = pt.y
		c = False
		j = 0
		i = 1
		nvert = self.nvert
		while (i < nvert) :
			vi = self.points[i]
			vj = self.points[j]

			if(((vi.y > testy) != (vj.y > testy)) and (testx < (vj.x - vi.x) * (testy - vi.y) / (vj.y - vi.y) + vi.x)):
				c = not(c)

			if(vi.x == firstX and vi.y == firstY):
				i = i + 1
				if (i < nvert):
					vi = self.points[i];
					firstX = vi.x;
					firstY = vi.y;
			j = i
			i = i + 1
		return c

	def bounds(self):
		return self.bound
'''def parseInput():
        j = 0
        for line in sys.stdin:
                line = line.strip()
                values = line.split(',')
                #if values[0]=='"Date/Time"': continue
                if values[0]=="Pickup_latitude": continue
                if values[2]=="latitude": continue
                yield values
'''
def simplePolygonTest():
	print("Point in polygon test")
	# Create a simple polygon
	JFK = Polygon([Point(40.6188,-73.7712),Point(40.6233,-73.7674),Point(40.6248,-73.7681),Point(40.6281,-73.7681),Point(40.6356,-73.7472),Point(40.6422,-73.7468),Point(40.6469,-73.7534),
	Point(40.6460,-73.7544),Point(40.6589,-73.7745),Point(40.6628,-73.7858),Point(40.6634,-73.7891),Point(40.6655,-73.7903),Point(40.6658,-73.8021),Point(40.6632,-73.8146),Point(40.6638,-73.8210),Point(40.6621,-73.8244),Point(40.6546,-73.8248),
	Point(40.6469,-73.8212),Point(40.6302,-73.7848),Point(40.6223,-73.7899),Point(40.6203,-73.7831),Point(40.6274,-73.7782),Point(40.6235,-73.7731),Point(40.6193,-73.7738),Point(40.6188,-73.7712)])

	LGA = Polygon([Point(40.7662,-73.8888),Point(40.7736,-73.8898),Point(40.7751,-73.8843),Point(40.7808,-73.8852),Point(40.7812,-73.8795),Point(40.7842,-73.8788),Point(40.7827,-73.8751),
	Point(40.7864,-73.8711),Point(40.788,-73.8673),Point(40.7832,-73.868),Point(40.7808,-73.8716),Point(40.773,-73.8534),Point(40.7697,-73.8557),Point(40.7673,-73.8505),Point(40.7645,-73.85),Point(40.7637,-73.8529),
        Point(40.7676,-73.856),Point(40.7659,-73.8594),Point(40.7654,-73.8625),Point(40.7693,-73.8672),Point(40.7714,-73.8732),Point(40.7697,-73.8871),Point(40.7665,-73.8866),Point(40.7662,-73.8888)])

	List_points=[]
	JFKcount=0
	LGAcount=0
	with open("taxigreen(06-15)_table.csv") as f:
                for line in f:
			line=line.strip()
			values=line.split(",")
			if values[0]=="Pickup_latitude" or values[0]=="latitude":
					continue
                        dropoff_latitude=float(values[2])
                        dropoff_longitude=float(values[3])
                        pt1=Point(dropoff_latitude,dropoff_longitude)
                        List_points.append(pt1)

	start_time = time.clock()
	for i1 in range(0,len(List_points)):
		if JFK.contains(List_points[i1]):
			JFKcount=JFKcount+1
			
	JFK_time = (time.clock() - start_time)
	start_time = time.clock()
	for i1 in range(0,len(List_points)):
		if LGA.contains(List_points[i1]):
			LGAcount = LGAcount+1
			
	LGA_time =(time.clock() - start_time)

	print("query time for jfk is %f seconds" %(JFK_time))
	print("Total points in the polygon of JFK is %d " % (JFKcount))
	print("query time for LGA is %f seconds" %(LGA_time))
	print("Total points in the polygon of LGA is %d" %(LGAcount))

def simpleRTree():
        i=1
	idx = index.Index()

        JFK = Polygon([Point(40.6188,-73.7712),Point(40.6233,-73.7674),Point(40.6248,-73.7681),Point(40.6281,-73.7681),Point(40.6356,-73.7472),Point(40.6422,-73.7468),Point(40.6469,-73.7534),
	Point(40.6460,-73.7544),Point(40.6589,-73.7745),Point(40.6628,-73.7858),Point(40.6634,-73.7891),Point(40.6655,-73.7903),Point(40.6658,-73.8021),Point(40.6632,-73.8146),Point(40.6638,-73.8210),Point(40.6621,-73.8244),Point(40.6546,-73.8248),
	Point(40.6469,-73.8212),Point(40.6302,-73.7848),Point(40.6223,-73.7899),Point(40.6203,-73.7831),Point(40.6274,-73.7782),Point(40.6235,-73.7731),Point(40.6193,-73.7738),Point(40.6188,-73.7712)])

	
	with open("taxigreen(06-15)_table.csv") as f:
                for line in f:
			line=line.strip()
			values=line.split(",")
			if values[0]=="Pickup_latitude" or values[0]=="latitude":
					continue
                        dropoff_latitude=float(values[2])
                        dropoff_longitude=float(values[3])
                        pt1=Point((dropoff_latitude),(dropoff_longitude))
                        idx.insert(i,(pt1.x,pt1.y,pt1.x,pt1.y))
                        i=i+1
                        #print(i)

	leftBottom = Point(minimumx,minimumy)
	rightTop = Point(maximumx,maximumy)
	start_time = time.clock()
	results = list(idx.intersection(((leftBottom.x),(leftBottom.y),(rightTop.x),(rightTop.y))))
	JFK_time=(time.clock() - start_time)

	print("JFK Query result ")
	#print((results))
	print("query time for jfk is %f seconds " %(JFK_time))
	print("Total points in the polygon of JFK is %d " % (len(results)))

        LGA = Polygon([Point(40.7662,-73.8888),Point(40.7736,-73.8898),Point(40.7751,-73.8843),Point(40.7808,-73.8852),Point(40.7812,-73.8795),Point(40.7842,-73.8788),Point(40.7827,-73.8751),
	Point(40.7864,-73.8711),Point(40.788,-73.8673),Point(40.7832,-73.868),Point(40.7808,-73.8716),Point(40.773,-73.8534),Point(40.7697,-73.8557),Point(40.7673,-73.8505),Point(40.7645,-73.85),Point(40.7637,-73.8529),
        Point(40.7676,-73.856),Point(40.7659,-73.8594),Point(40.7654,-73.8625),Point(40.7693,-73.8672),Point(40.7714,-73.8732),Point(40.7697,-73.8871),Point(40.7665,-73.8866),Point(40.7662,-73.8888)])
	
	leftBottom = Point(minimumx,minimumy)
	rightTop = Point(maximumx,maximumy)
	start_time = time.clock()
	results = list(idx.intersection(((leftBottom.x),(leftBottom.y),(rightTop.x),(rightTop.y))))
	LGA_time =(time.clock() - start_time)

	print("LGA Query result ")
	#print((results))
	print("query time for LGA is %f seconds" %(LGA_time))
	print("Total points in the polygon of LGA is %d" %(len(results)))



simplePolygonTest()
#sys.stdin = sys.__stdin__
simpleRTree()

