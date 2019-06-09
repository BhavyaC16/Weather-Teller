from apikey import key
import urllib.request


k = key()

# function to get weather response
def weather_response(location, API_key = k):
	""" The weather_response function is used to extract the weather response forecast from the web-service into the program. It converts the JSON Data into a string for further processing"""
	url = "http://api.openweathermap.org/data/2.5/forecast?q=" + location + "&APPID=" + API_key
	webpage = urllib.request.urlopen(url)
	json = str(webpage.read())
	json = json[1:]
	#print(json)
	return json

# function to check for valid response
def has_error(location,json):
	""" The has_error function checks whether the location passed as a query to the web-service is the same as the location for which the forecast has been displayed."""
	i1 = json.find('name')                                                          
	i2 = i1 + 7
	i3 = json.find('"',i2)                                                                  
	if json[i2:i3] != location:
		return True

# function to get attributes on nth day
import datetime
def get_temperature (json, n=0, t="03:00:00"):
	""" The get_temperature function takes the json string, nth day from today, and the time as formal parameters and returns the forecasted temperature of the required date and time."""
	D = datetime.date.today() + datetime.timedelta(days=n) #adds n days to the current date
	Date = datetime.date.isoformat(D) #converts the date to the required format
	if(t=='00:00:00' or t=='03:00:00' or t=='06:00:00' or t=='09:00:00' or t=='12:00:00' or t=='15:00:00' or t=='18:00:00' or t=='21:00:00'):
		date_and_time = Date + ' ' + t
		i1 = json.find(date_and_time)
		i2 = json.rfind('temp"',0,i1)
		i3 = json.find(',',i2)
		temp = float(json[i2+6:i3])
		return temp    #returns the temperature of the required date and time
	else:
		message = 'Invalid Time Input'
		return message
def get_humidity(json, n=0, t="03:00:00"):
	""" The get_humidity function takes the json string, nth day from today, and the time as formal parameters and returns the forecasted humidity of the required date and time."""

	D = datetime.date.today() + datetime.timedelta(days=n) #adds n days to the current date
	Date = datetime.date.isoformat(D) #converts the date to the required format
	if t=='00:00:00' or t=='03:00:00' or t=='06:00:00' or t=='09:00:00' or t=='12:00:00' or t=='15:00:00' or t=='18:00:00' or t=='21:00:00':  
		date_and_time = Date + ' ' + t
		i1 = json.find(date_and_time)
		i2 = json.rfind('humidity"',0,i1)
		i3 = json.find(',',i2)
		humidity = float(json[i2+10:i3])
		return humidity  #returns the  of the required date and time
	else:
		message = 'Invalid Time Input'
		return message

def get_pressure(json, n=0, t="03:00:00"):
	""" The get_pressure function takes the json string, nth day from today, and the time as formal parameters and returns the forecasted pressure of the required date and time."""
	D = datetime.date.today() + datetime.timedelta(days=n) #adds n days to the
	Date = datetime.date.isoformat(D) #converts the date to the required format
	if t=='00:00:00' or t=='03:00:00' or t=='06:00:00' or t=='09:00:00' or t=='12:00:00' or t=='15:00:00' or t=='18:00:00' or t=='21:00:00': 
		date_and_time = Date + ' ' + t
		i1 = json.find(date_and_time)
		i2 = json.rfind('pressure"',0,i1)
		i3 = json.find(',',i2)
		pressure =  float(json[i2+10:i3])
		return pressure   #returns the pressure of the required date and time
	else:
		message = 'Invalid Time Input'
		return message

def get_wind(json, n=0, t="3:00:00"):
	""" The get_wind function takes the json string, nth day from today, and the time as formal parameters and returns the forecasted wind speed for the required date and time."""

	D = datetime.date.today() + datetime.timedelta(days=n)    #adds n days to the current date
	Date = datetime.date.isoformat(D)    #converts the date to the required format
	if t=='00:00:00' or t=='03:00:00' or t=='06:00:00' or t=='09:00:00' or t=='12:00:00' or t=='15:00:00' or t=='18:00:00' or t=='21:00:00':        
		date_and_time = Date + ' ' + t
		i1 = json.find(date_and_time)
		i2 = json.rfind('speed"',0,i1)
		i3 = json.find(',',i2)
		wind_speed = float(json[i2+7:i3])
		return wind_speed   #returns the wind speed of the required date and time
	else:
		message = 'Invalid Time Input'
		return message

def get_sealevel(json, n=0, t="03:00:00"):
	""" The get_sealevel function takes the json string, nth day from today, and the time as formal parameters and returns the forecasted sea level for the required date and time."""

	D = datetime.date.today() + datetime.timedelta(days=n) #adds n days to the current date
	Date = datetime.date.isoformat(D)     #converts the date to the required format
	if t=='00:00:00' or t=='03:00:00' or t=='06:00:00' or t=='09:00:00' or t=='12:00:00' or t=='15:00:00' or t=='18:00:00' or t=='21:00:00':        
		date_and_time = Date + ' ' + t
		i1 = json.find(date_and_time)
		i2 = json.rfind('sea_level"',0,i1)
		i3 = json.find(',',i2)
		sea_level = float(json[i2+11:i3])
		return sea_level   #returns the sealevel of the required date and time
	else:
		message = 'Invalid Time Input'
		return message
		
weather_response("singapore")
