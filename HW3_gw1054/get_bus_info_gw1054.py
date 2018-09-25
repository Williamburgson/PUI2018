import __future__
import json
import urllib.request
import sys
import csv

mta_key = sys.argv[1]
bus_line = sys.argv[2]
filename = sys.argv[3]

api = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=' + mta_key + '&VehicleMonitoringDetailLevel=calls&LineRef=' + bus_line
j = urllib.request.urlopen(api)
j = j.read().decode()
data = json.loads(j)

bus = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
fout = open(filename, 'w')
fout.write('Latitude,Longtitude,Stop Name,Stop Status\n')
for i in range(0, len(bus)):
    output = ''
    output += str(bus[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude'])
    output += ','
    output += str(bus[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])
    output += ','
    try: bus_stop = bus_stop = bus[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
    except LookupError: bus_stop = 'N/A'
    try: bus_status = bus[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
    except LookupError: bus_status = 'N/A'
    output += bus_stop + ',' + bus_status + '\n'
    fout.write(output)

