import csv, json
import requests
import webbrowser
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager


def getwebidFromPi(wordlist):
	url = 'https://128.2.109.159/piwebapi/dataservers/s0-MYhSMORGkyGTe9bdohw0AV0lOLTYyTlBVMkJWTDIw/points?namefilter=*'
	url += 'phipps*'
	for i in wordlist:
		url += i + '*'
	content = requests.get(url, auth=('CMU_Students', 'WorkHard!ChangeWorld'), verify=False)
	raw = json.loads(content.text)
	webid = raw['Items'][0]['WebId']
	# print(webid)
	return webid

def getrawFromPi(url):
    content = requests.get(url, auth=('CMU_Students', 'WorkHard!ChangeWorld'), verify=False)
    raw = json.loads(content.text)
    return raw

def queryData(webid, name, starttime, endtime, interval):
	filename = name + '.csv'
	url = 'https://128.2.109.159/piwebapi/streams/' + webid + '/interpolated?starttime=%s&endtime=%s&interval=%s'%(starttime, endtime, interval)
	raw = getrawFromPi(url)
	dataItems = raw['Items']
	formedTimeSeries = []
	for dataItem in dataItems:
		if dataItem['Good']:
			formedTimeSeries.append([dataItem['Timestamp'], dataItem['Value']])
		else:
			formedTimeSeries.append([dataItem['Timestamp'], None])
	with open(filename, 'w') as csv_file:
		wr = csv.writer(csv_file)
		for row in formedTimeSeries:
			wr.writerow(row)

def download(keywords, key):
	starttime = '2017-10-01T00:00:00Z'
	endtime = '2019-10-01T00:00:00Z'
	interval = '10m'

	var = key
	wordlist = keywords
	ix = wordlist.index(key)
	for i in range(2):
		new = var + str(i*2+2) 
		wordlist[ix] = new
		print("!!!!",wordlist)
		webid = getwebidFromPi(wordlist)
		name = '_'.join(wordlist)
		queryData(webid, name, starttime, endtime, interval)
	return  None

# download(['204','VAV-','temp'], 'VAV-')

starttime = '2017-10-01T00:00:00Z'
endtime = '2019-10-01T00:00:00Z'
interval = '10m'


############### AHU

# webid = 'P0-MYhSMORGkyGTe9bdohw0AVTgAAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19BSFUtMSBPQVQgTU9OSVRPUl9PQSBIVU1JRElUWSBBVi5QUkVTRU5UX1ZBTFVF'
# name = 'outdoorair_humidity'

# webid = 'P0-MYhSMORGkyGTe9bdohw0AUjgAAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19BSFUtMSBPQVQgTU9OSVRPUl9PVVRTSURFIEFJUiBURU1QRVJBVFVSRS5QUkVTRU5UX1ZBTFVF'
# name = 'outdoorair_temp'

############### wather station

# webid = 'P0-MYhSMORGkyGTe9bdohw0AVSsAAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19XRUFUSEVSX1NPTEFSX1JBRElBVElPTl9BVi5QUkVTRU5UX1ZBTFVF'
# name = 'solar_radiation'

# webid = 'P0-MYhSMORGkyGTe9bdohw0AVysAAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19XRUFUSEVSX1dJTkRfU1BFRURfQVYuUFJFU0VOVF9WQUxVRQ'
# name = 'wind_speed'

# webid = 'P0-MYhSMORGkyGTe9bdohw0AUysAAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19XRUFUSEVSX1dJTkRfRElSRUNUSU9OX0FWLlBSRVNFTlRfVkFMVUU'
# name = 'wind_direction'

# webid = 'P0-MYhSMORGkyGTe9bdohw0AWCsAAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19XRUFUSEVSX09BX0hVTUlESVRZLlBSRVNFTlRfVkFMVUU'
# name = 'outsideair_humidity'

# webid = 'P0-MYhSMORGkyGTe9bdohw0AVisAAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19XRUFUSEVSX09BX1RFTVBFUkFUVVJFLlBSRVNFTlRfVkFMVUU'
# name = 'outsideair_temp'

# webid = 'P0-MYhSMORGkyGTe9bdohw0AWisAAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19XRUFUSEVSX09BX0RFV1BPSU5ULlBSRVNFTlRfVkFMVUU'
# name = 'outsideair_dewpoint'

# webid = 'P0-MYhSMORGkyGTe9bdohw0AWSsAAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19XRUFUSEVSX09BX0VOVEhBTFBZLlBSRVNFTlRfVkFMVUU'
# name = 'outsideair_enthalpy'


############### PV


# webid = 'P0-MYhSMORGkyGTe9bdohw0AE_YAAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19QVl9BTEw'
# name = 'PV_all'

# webid = 'P0-MYhSMORGkyGTe9bdohw0A6AoBAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19QVl9BTExfT05FIFlFQVI'
# name = 'PV_alloneyear'

#not all data, 2019 missed
# webid = 'P0-MYhSMORGkyGTe9bdohw0AxyIAAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19FRUVEX1BWSU5TVC5QUkVTRU5UX1ZBTFVF'
# name = 'PV_instant'


############### Geothermal heat pump

# webid = 'P0-MYhSMORGkyGTe9bdohw0AkTgAAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19BSFUtMSBXU0hQIEJUVSBNRVRFUl9TVVBQTFkgVEVNUC5QUkVTRU5UX1ZBTFVF'
# name = 'WSHP_GTSsupply_temp'

# webid = 'P0-MYhSMORGkyGTe9bdohw0AkDgAAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19BSFUtMSBXU0hQIEJUVSBNRVRFUl9SRVRVUk4gVEVNUC5QUkVTRU5UX1ZBTFVF'
# name = 'WSHP_GTSreturn_temp'

# webid = 'P0-MYhSMORGkyGTe9bdohw0AQSUAAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19FTEVDIE1UUiBCRVJORVIgVU5JVF9SRUFMX1BPV0VSLlBSRVNFTlRfVkFMVUU'
# name = 'WSHP_realPower'

# webid = 'P0-MYhSMORGkyGTe9bdohw0ArBsBAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19FTEVDIE1UUiBCRVJORVIgVU5JVF9SRUFMX1BPV0VSLkFESlVTVEVE'
# name = 'WSHP_realPower_adjusted'

# webid = 'P0-MYhSMORGkyGTe9bdohw0AnzgAAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19BSFUtMSBXU0hQIEJUVSBNRVRFUl9VU0FHRSBNVEQuUFJFU0VOVF9WQUxVRQ'
# name = 'Preheat_supply_temp'


# webid = 'P0-MYhSMORGkyGTe9bdohw0AOTgAAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19BSFUtMV9HVFMuUFJFU0VOVF9WQUxVRQ'
# name = 'geothermal_GTS'

webid = 'P0-MYhSMORGkyGTe9bdohw0AEjYAAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19NRVIgMTEyIEdFT1RIRVJNQUwgTE9PUF9HVFIuUFJFU0VOVF9WQUxVRQ'
name = 'geothermal_GTR'


################ search by elec

    # {
    #   "WebId": "P0-MYhSMORGkyGTe9bdohw0A1QoBAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19FTEVDIEFMTCBDT05TVU1QVElPTiBDU0xfSE9VUkxZ",
    #   "Id": 68309,
    #   "Name": "PHIPPS_Elec All Consumption CSL_Hourly",
    #   "PointClass": "classic",
    #   "PointType": "Float32",
    #   "Future": false,
    #   "Links": {
    #     "Self": "https://128.2.109.159/piwebapi/points/P0-MYhSMORGkyGTe9bdohw0A1QoBAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19FTEVDIEFMTCBDT05TVU1QVElPTiBDU0xfSE9VUkxZ",
    #     "DataServer": "https://128.2.109.159/piwebapi/dataservers/s0-MYhSMORGkyGTe9bdohw0AV0lOLTYyTlBVMkJWTDIw",
    #     "Attributes": "https://128.2.109.159/piwebapi/points/P0-MYhSMORGkyGTe9bdohw0A1QoBAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19FTEVDIEFMTCBDT05TVU1QVElPTiBDU0xfSE9VUkxZ/attributes",
    #     "Value": "https://128.2.109.159/piwebapi/streams/P0-MYhSMORGkyGTe9bdohw0A1QoBAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19FTEVDIEFMTCBDT05TVU1QVElPTiBDU0xfSE9VUkxZ/value",
    #     "InterpolatedData": "https://128.2.109.159/piwebapi/streams/P0-MYhSMORGkyGTe9bdohw0A1QoBAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19FTEVDIEFMTCBDT05TVU1QVElPTiBDU0xfSE9VUkxZ/interpolated",
    #     "RecordedData": "https://128.2.109.159/piwebapi/streams/P0-MYhSMORGkyGTe9bdohw0A1QoBAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19FTEVDIEFMTCBDT05TVU1QVElPTiBDU0xfSE9VUkxZ/recorded",
    #     "PlotData": "https://128.2.109.159/piwebapi/streams/P0-MYhSMORGkyGTe9bdohw0A1QoBAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19FTEVDIEFMTCBDT05TVU1QVElPTiBDU0xfSE9VUkxZ/plot",
    #     "SummaryData": "https://128.2.109.159/piwebapi/streams/P0-MYhSMORGkyGTe9bdohw0A1QoBAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19FTEVDIEFMTCBDT05TVU1QVElPTiBDU0xfSE9VUkxZ/summary",
    #     "EndValue": "https://128.2.109.159/piwebapi/streams/P0-MYhSMORGkyGTe9bdohw0A1QoBAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19FTEVDIEFMTCBDT05TVU1QVElPTiBDU0xfSE9VUkxZ/end"
    #   }
    # },

    #     {
    #   "WebId": "P0-MYhSMORGkyGTe9bdohw0Az5UBAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19FTEVDIEhWQUMgQ09OU1VNUFRJT04gQ1NMX0hPVVJMWQ",
    #   "Id": 103887,
    #   "Name": "PHIPPS_Elec HVAC Consumption CSL_Hourly",
    #   "PointClass": "classic",
    #   "PointType": "Float32",
    #   "Future": false,
    #   "Links": {
    #     "Self": "https://128.2.109.159/piwebapi/points/P0-MYhSMORGkyGTe9bdohw0Az5UBAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19FTEVDIEhWQUMgQ09OU1VNUFRJT04gQ1NMX0hPVVJMWQ",
    #     "DataServer": "https://128.2.109.159/piwebapi/dataservers/s0-MYhSMORGkyGTe9bdohw0AV0lOLTYyTlBVMkJWTDIw",
    #     "Attributes": "https://128.2.109.159/piwebapi/points/P0-MYhSMORGkyGTe9bdohw0Az5UBAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19FTEVDIEhWQUMgQ09OU1VNUFRJT04gQ1NMX0hPVVJMWQ/attributes",
    #     "Value": "https://128.2.109.159/piwebapi/streams/P0-MYhSMORGkyGTe9bdohw0Az5UBAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19FTEVDIEhWQUMgQ09OU1VNUFRJT04gQ1NMX0hPVVJMWQ/value",
    #     "InterpolatedData": "https://128.2.109.159/piwebapi/streams/P0-MYhSMORGkyGTe9bdohw0Az5UBAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19FTEVDIEhWQUMgQ09OU1VNUFRJT04gQ1NMX0hPVVJMWQ/interpolated",
    #     "RecordedData": "https://128.2.109.159/piwebapi/streams/P0-MYhSMORGkyGTe9bdohw0Az5UBAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19FTEVDIEhWQUMgQ09OU1VNUFRJT04gQ1NMX0hPVVJMWQ/recorded",
    #     "PlotData": "https://128.2.109.159/piwebapi/streams/P0-MYhSMORGkyGTe9bdohw0Az5UBAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19FTEVDIEhWQUMgQ09OU1VNUFRJT04gQ1NMX0hPVVJMWQ/plot",
    #     "SummaryData": "https://128.2.109.159/piwebapi/streams/P0-MYhSMORGkyGTe9bdohw0Az5UBAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19FTEVDIEhWQUMgQ09OU1VNUFRJT04gQ1NMX0hPVVJMWQ/summary",
    #     "EndValue": "https://128.2.109.159/piwebapi/streams/P0-MYhSMORGkyGTe9bdohw0Az5UBAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19FTEVDIEhWQUMgQ09OU1VNUFRJT04gQ1NMX0hPVVJMWQ/end"
    #   }
    # },

    #       "WebId": "P0-MYhSMORGkyGTe9bdohw0A2goBAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19FTEVDIExJR0hUSU5HIENPTlNVTVBUSU9OIENTTF9IT1VSTFk",
    #   "Id": 68314,
    #   "Name": "PHIPPS_Elec Lighting Consumption CSL_Hourly",
    #   "PointClass": "classic",
    #   "PointType": "Float32",
    #   "Future": false,
    #   "Links": {
    #     "Self": "https://128.2.109.159/piwebapi/points/P0-MYhSMORGkyGTe9bdohw0A2goBAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19FTEVDIExJR0hUSU5HIENPTlNVTVBUSU9OIENTTF9IT1VSTFk",
    #     "DataServer": "https://128.2.109.159/piwebapi/dataservers/s0-MYhSMORGkyGTe9bdohw0AV0lOLTYyTlBVMkJWTDIw",
    #     "Attributes": "https://128.2.109.159/piwebapi/points/P0-MYhSMORGkyGTe9bdohw0A2goBAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19FTEVDIExJR0hUSU5HIENPTlNVTVBUSU9OIENTTF9IT1VSTFk/attributes",
    #     "Value": "https://128.2.109.159/piwebapi/streams/P0-MYhSMORGkyGTe9bdohw0A2goBAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19FTEVDIExJR0hUSU5HIENPTlNVTVBUSU9OIENTTF9IT1VSTFk/value",
    #     "InterpolatedData": "https://128.2.109.159/piwebapi/streams/P0-MYhSMORGkyGTe9bdohw0A2goBAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19FTEVDIExJR0hUSU5HIENPTlNVTVBUSU9OIENTTF9IT1VSTFk/interpolated",
    #     "RecordedData": "https://128.2.109.159/piwebapi/streams/P0-MYhSMORGkyGTe9bdohw0A2goBAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19FTEVDIExJR0hUSU5HIENPTlNVTVBUSU9OIENTTF9IT1VSTFk/recorded",
    #     "PlotData": "https://128.2.109.159/piwebapi/streams/P0-MYhSMORGkyGTe9bdohw0A2goBAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19FTEVDIExJR0hUSU5HIENPTlNVTVBUSU9OIENTTF9IT1VSTFk/plot",
    #     "SummaryData": "https://128.2.109.159/piwebapi/streams/P0-MYhSMORGkyGTe9bdohw0A2goBAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19FTEVDIExJR0hUSU5HIENPTlNVTVBUSU9OIENTTF9IT1VSTFk/summary",
    #     "EndValue": "https://128.2.109.159/piwebapi/streams/P0-MYhSMORGkyGTe9bdohw0A2goBAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19FTEVDIExJR0hUSU5HIENPTlNVTVBUSU9OIENTTF9IT1VSTFk/end"
    #   }
    # },


    #     {
    #   "WebId": "P0-MYhSMORGkyGTe9bdohw0A0woBAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19FTEVDIFBMVUcgQ09OU1VNUFRJT04gQ1NMX0hPVVJMWQ",
    #   "Id": 68307,
    #   "Name": "PHIPPS_Elec Plug Consumption CSL_Hourly",
    #   "PointClass": "classic",
    #   "PointType": "Float32",
    #   "Future": false,
    #   "Links": {
    #     "Self": "https://128.2.109.159/piwebapi/points/P0-MYhSMORGkyGTe9bdohw0A0woBAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19FTEVDIFBMVUcgQ09OU1VNUFRJT04gQ1NMX0hPVVJMWQ",
    #     "DataServer": "https://128.2.109.159/piwebapi/dataservers/s0-MYhSMORGkyGTe9bdohw0AV0lOLTYyTlBVMkJWTDIw",
    #     "Attributes": "https://128.2.109.159/piwebapi/points/P0-MYhSMORGkyGTe9bdohw0A0woBAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19FTEVDIFBMVUcgQ09OU1VNUFRJT04gQ1NMX0hPVVJMWQ/attributes",
    #     "Value": "https://128.2.109.159/piwebapi/streams/P0-MYhSMORGkyGTe9bdohw0A0woBAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19FTEVDIFBMVUcgQ09OU1VNUFRJT04gQ1NMX0hPVVJMWQ/value",
    #     "InterpolatedData": "https://128.2.109.159/piwebapi/streams/P0-MYhSMORGkyGTe9bdohw0A0woBAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19FTEVDIFBMVUcgQ09OU1VNUFRJT04gQ1NMX0hPVVJMWQ/interpolated",
    #     "RecordedData": "https://128.2.109.159/piwebapi/streams/P0-MYhSMORGkyGTe9bdohw0A0woBAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19FTEVDIFBMVUcgQ09OU1VNUFRJT04gQ1NMX0hPVVJMWQ/recorded",
    #     "PlotData": "https://128.2.109.159/piwebapi/streams/P0-MYhSMORGkyGTe9bdohw0A0woBAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19FTEVDIFBMVUcgQ09OU1VNUFRJT04gQ1NMX0hPVVJMWQ/plot",
    #     "SummaryData": "https://128.2.109.159/piwebapi/streams/P0-MYhSMORGkyGTe9bdohw0A0woBAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19FTEVDIFBMVUcgQ09OU1VNUFRJT04gQ1NMX0hPVVJMWQ/summary",
    #     "EndValue": "https://128.2.109.159/piwebapi/streams/P0-MYhSMORGkyGTe9bdohw0A0woBAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19FTEVDIFBMVUcgQ09OU1VNUFRJT04gQ1NMX0hPVVJMWQ/end"
    #   }
    # },
#############

queryData(webid, name, starttime, endtime, interval)

