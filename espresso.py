import requests,os,json

USERNAME = os.environ['BROWSERSTACK_USERNAME']
BROWSERSTACK_ACCESS_KEY = os.environ['BROWSERSTACK_ACCESS_KEY']


# APP UPLOAD
# app
###################Espresso App Upload #########################
response = requests.get('https://api-cloud.browserstack.com/app-automate/recent_apps', auth=(USERNAME,BROWSERSTACK_ACCESS_KEY))
not_uploaded = False
json_data = response.json()
for item in json_data:
	try:
		if item["custom_id"] == "EspressoApp" :
			not_uploaded = True
			print("Found App Here!")
			break
	except:
		print("custom_id not found!!")
if not_uploaded == False:
	files = {
    'data': (None, '{"url": "https://docs.google.com/uc?export=download&id=1MuhENYHjWoPThFQgkrofmWLt-AWjDdm8","custom_id":"EspressoApp"}'),
	}

	response = requests.post('https://api-cloud.browserstack.com/app-automate/upload', files=files, auth=(USERNAME,BROWSERSTACK_ACCESS_KEY))
	print(response.status_code)


###################Espresso App Upload #########################

###################Espresso Test App Upload #########################
response = requests.get('https://api-cloud.browserstack.com/app-automate/espresso/test-suites', auth=(USERNAME,BROWSERSTACK_ACCESS_KEY))
not_uploaded = False
json_data = response.json()
for item in json_data:
	try:
		if item["custom_id"] == "EspressoTestApp" :
			not_uploaded = True
			print("Found Test App Here!")
			break
	except:
		print("custom_id not found!!")
if not_uploaded == False:
	files = {
    'data': (None, '{"url": "https://docs.google.com/uc?export=download&id=1fSDCibYeOZLSlOA1wdgRX9uqGZLqyh8l","custom_id":"EspressoTestApp"}'),
	}

	response = requests.post('https://api-cloud.browserstack.com/app-automate/espresso/test-suite', files=files, auth=(USERNAME,BROWSERSTACK_ACCESS_KEY))
	print(response.status_code)


###################Espresso Test App Upload #########################


###################Espresso Run Test #########################

headers = {
    'Content-Type': 'application/json',
}

data = '{"devices": ["Samsung Galaxy S8-7.0"], "app": "EspressoApp", "deviceLogs" : "true", "testSuite": "EspressoTestApp"}'

response = requests.post('https://api-cloud.browserstack.com/app-automate/espresso/build', headers=headers, data=data, auth=(USERNAME,BROWSERSTACK_ACCESS_KEY))
print(response.status_code)
print(response.json())
###################Espresso Run Test #########################

# APP URL

# curl -u "$BROWSERSTACK_USERNAME:$BROWSERSTACK_ACCESS_KEY" \
#      -X POST "https://api-cloud.browserstack.com/app-automate/upload" \
#      -F "file=@/Users/rathilpatel/Downloads/demo/app/apps/Espresso-App.apk"


# {"app_url":"bs://f9e110a62cc12d4d3556b486912fe2e423ded53e"}

# TEST URL :
# curl -u "$BROWSERSTACK_USERNAME:$BROWSERSTACK_ACCESS_KEY" \
#      -X POST "https://api-cloud.browserstack.com/app-automate/espresso/test-suite" \
#      -F "file=@/Users/rathilpatel/Downloads/demo/app/apps/Espresso-AppTest.apk"


# {"test_url":"bs://03d0b583adc729e224be1891dd8f0a875f7f9794"}


# BUILD


# curl -X POST "https://api-cloud.browserstack.com/app-automate/espresso/build" \
#      -d "{\"devices\": [\"Samsung Galaxy S8-7.0\"], \"app\": \"bs://f9e110a62cc12d4d3556b486912fe2e423ded53e\", \"deviceLogs\" : true, \"testSuite\": \"bs://03d0b583adc729e224be1891dd8f0a875f7f9794\"}" \
#      -H "Content-Type: application/json" \
#      -u "$BROWSERSTACK_USERNAME:$BROWSERSTACK_ACCESS_KEY"





