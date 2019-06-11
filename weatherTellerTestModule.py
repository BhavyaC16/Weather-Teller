# AUTHOR: BHAVYA CHOPRA 


""" This module is used to test the functions of the module a1.py by the method of unittesting, which is testing of a unit of code in isolation"""

import unittest
from a1 import weather_response
from a1 import has_error
from a1 import get_temperature 
from a1 import get_humidity
from a1 import get_pressure
from a1 import get_wind
from a1 import get_sealevel

# TEST cases should cover the different boundary cases.

string1 = weather_response("Delhi","cd05d8c81889d20eed43fed129efec2b")          #string1 stores the weather forecast of Delhi returned by the web-service in string format 
string2 = weather_response("Paris","cd05d8c81889d20eed43fed129efec2b")          #string2 stores the weather forecast of Paris returned by the web-service in string format
string3 = weather_response("Jaipur","cd05d8c81889d20eed43fed129efec2b")         #string3 stores the weather forecast of Jaipur returned by the web-service in string format
string4 = weather_response("Hyderabad","cd05d8c81889d20eed43fed129efec2b")      #string4 stores the weather forecast of Hyderabad returned by the web-service in string format
string5 = weather_response("Singapore","cd05d8c81889d20eed43fed129efec2b")      #string5 stores the weather forecast of Singapore returned by the web-service in string format

class testpoint(unittest.TestCase):


	def test_has_error(self):
		self.assertTrue(has_error("Delhi",string1))
		self.assertTrue(has_error("Paris",string2))
		self.assertTrue(has_error("Jaipur",string3))
		self.assertTrue(has_error("Hyderabad",string4))
		self.assertTrue(has_error("Singapore",string5))        
                

	def test_get_temperature(self):
		""" test_get_temperature tests the get_temperature function of the module a1.py using 5 different test cases.
		The parameter 'delta=5' of the assertAlmostEqual function allows a variation of plus or minus 5 percent in the returned 		output and the expected output"""
		self.assertAlmostEqual(get_temperature(string1,2,"21:00:00"),296.97,delta=5)
		self.assertAlmostEqual(get_temperature(string2,3,"00:00:00"),292.33,delta=5)
		self.assertAlmostEqual(get_temperature(string3,1,"03:00:00"),297.51,delta=5)
		self.assertAlmostEqual(get_temperature(string4,4,"09:00:00"),303.628,delta=5)
		self.assertAlmostEqual(get_temperature(string5,0,"21:00:00"),301.278,delta=5)



	def test_get_humidity(self):
		""" test_get_humidity tests the get_humidity function of the module a1.py using 5 different test cases.
		The parameter 'delta=5' of the assertAlmostEqual function allows a variation of plus or minus 5 percent in the returned 		output and the expected output"""        
		self.assertAlmostEqual(get_humidity(string1,0,"21:00:00"),92,delta=5)
		self.assertAlmostEqual(get_humidity(string2,4,"09:00:00"),71,delta=5)
		self.assertAlmostEqual(get_humidity(string3,3,"06:00:00"),84,delta=5)
		self.assertAlmostEqual(get_humidity(string4,1,"03:00:00"),60,delta=5)
		self.assertAlmostEqual(get_humidity(string5,2,"00:00:00"),100,delta=5)


	def test_get_pressure(self):
		""" test_get_pressure tests the get_pressure function of the module a1.py using 5 different test cases.
		The parameter 'delta=5' of the assertAlmostEqual function allows a variation of plus or minus 5 percent in the returned 		output and the expected output"""
		self.assertAlmostEqual(get_pressure(string1,2,"12:00:00"),992.16,delta=5)
		self.assertAlmostEqual(get_pressure(string2,0,"21:00:00"),1022.39,delta=5)
		self.assertAlmostEqual(get_pressure(string3,3,"18:00:00"),972.42,delta=5)
		self.assertAlmostEqual(get_pressure(string4,1,"00:00:00"),963.49,delta=5)
		self.assertAlmostEqual(get_pressure(string5,4,"03:00:00"),1023.84,delta=5)

     
	def test_get_wind(self):
		""" test_get_wind tests the get_wind function of the module a1.py using 5 different test cases. 
		The parameter 'delta=5' of the assertAlmostEqual function allows a variation of plus or minus 5 percent in the returned 		output and the expected output"""   
		self.assertAlmostEqual(get_wind(string1,3,"21:00:00"),1.31,delta=5)
		self.assertAlmostEqual(get_wind(string2,1,"15:00:00"),3.02,delta=5)
		self.assertAlmostEqual(get_wind(string3,0,"18:00:00"),1.62,delta=5)
		self.assertAlmostEqual(get_wind(string4,4,"06:00:00"),0.27,delta=5)
		self.assertAlmostEqual(get_wind(string5,2,"06:00:00"),5.56,delta=5)


	def test_get_sealevel(self):
		""" test_get_sealevel tests the get_sealevel function of the module a1.py using 5 different test cases. 
		The parameter 'delta=5' of the assertAlmostEqual function allows a variation of plus or minus 5 percent in the returned 		output and the expected output"""
		self.assertAlmostEqual(get_sealevel(string1,1,"09:00:00"),1018.25,delta=5)
		self.assertAlmostEqual(get_sealevel(string2,3,"18:00:00"),1027.84,delta=5)
		self.assertAlmostEqual(get_sealevel(string3,2,"21:00:00"),1018.66,delta=5)
		self.assertAlmostEqual(get_sealevel(string4,4,"09:00:00"),1020.12,delta=5)
		self.assertAlmostEqual(get_sealevel(string5,0,"18:00:00"),1025.33,delta=5)

if __name__=='__main__':
        unittest.main()
