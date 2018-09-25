import __future__
import sys 
import urllib.request
import json

#take command line params
mta_key = sys.argv[1]
# 85d30156-ce9e-4913-85c1-1cadcd0a5d2f
bus_line = sys.argv[2]

#Grab data
api = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=' + mta_key + '&VehicleMonitoringDetailLevel=calls&LineRef=' + bus_line
j = urllib.request.urlopen(api) 
j = j.read().decode()
data = json.loads(j)

#Read location info and output
bus = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
bus_loc = data ['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
print ("Bus Line: ", bus_line)
print ("Number of Active Buses: ", (len(bus)))
for i in range(len(bus)):
    print ("The Bus %s is at Latitude  %s and Longitude %s" %(i+1, bus_loc[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude'], bus_loc[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']))
