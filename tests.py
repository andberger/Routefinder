import unittest
import routefinder as rf

class TestRouteFinder(unittest.TestCase):

	def test_copenhagen(self):
		problem = rf.Problem()
		problem.initState = (10,70)
		problem.goalState = (55,55)
		problem.datapath = "data/copenhagencity.txt"
		route = rf.AStar(problem)

		self.assertEqual("Vestervoldgade", route[0][0])
		self.assertEqual("Studiestraede", route[0][1])
		self.assertEqual("Studiestraede", route[0][2])
		self.assertEqual("Noerregade", route[0][3])
		self.assertEqual("Vestergade", route[0][4])
		self.assertEqual(130.7135762879351, route[1])

	def test_manhattan(self):
		problem = rf.Problem()
		problem.initState = (0,0)
		problem.goalState = (9,9)
		problem.datapath = "data/manhattan.txt"
		route = rf.AStar(problem)

		self.assertTrue("0" in route[0][0])
		self.assertTrue("1" in route[0][1])
		self.assertTrue("1" in route[0][2])
		self.assertTrue("2" in route[0][3])
		self.assertTrue("2" in route[0][4])
		self.assertTrue("3" in route[0][5])
		self.assertTrue("3" in route[0][6])
		self.assertTrue("4" in route[0][7])
		self.assertTrue("4" in route[0][8])
		self.assertTrue("5" in route[0][9])
		self.assertTrue("5" in route[0][10])
		self.assertTrue("6" in route[0][11])
		self.assertTrue("6" in route[0][12])
		self.assertTrue("7" in route[0][13])
		self.assertTrue("7" in route[0][14])
		self.assertTrue("8" in route[0][15])
		self.assertTrue("8" in route[0][16])
		self.assertTrue("9" in route[0][17])
		self.assertEqual(18.0, route[1])

if __name__ == '__main__':
    unittest.main()
