import requests,os,json

BROWSERSTACK_USERNAME = os.environ['BROWSERSTACK_USERNAME']
BROWSERSTACK_ACCESS_KEY = os.environ['BROWSERSTACK_ACCESS_KEY']


# APP UPLOAD
# app
###################XCUITest App Upload #########################
response = requests.get('https://api-cloud.browserstack.com/app-automate/recent_apps', auth=(BROWSERSTACK_USERNAME,BROWSERSTACK_ACCESS_KEY))
not_uploaded = False
json_data = response.json()
for item in json_data:
	try:
		if item["custom_id"] == "XCUIApp" :
			not_uploaded = True
			print("Found App Here!")
			break
	except:
		print("custom_id not found!!")
if not_uploaded == False:
	files = {
    'data': (None, '{"url": "https://docs.google.com/uc?export=download&id=1uDi_V38XEhnYmklrex0XeREb2j9A4flg","custom_id":"XCUIApp"}'),
	}

	response = requests.post('https://api-cloud.browserstack.com/app-automate/upload', files=files, auth=(BROWSERSTACK_USERNAME,BROWSERSTACK_ACCESS_KEY))
	print(response.status_code)


###################XCUITest App Upload #########################

###################XCUITest Test App Upload #########################
response = requests.get('https://api-cloud.browserstack.com/app-automate/xcuitest/test-suites', auth=(BROWSERSTACK_USERNAME,BROWSERSTACK_ACCESS_KEY))
not_uploaded = False
json_data = response.json()
for item in json_data:
	try:
		if item["custom_id"] == "XCUITestApp" :
			not_uploaded = True
			print("Found Test App Here!")
			break
	except:
		print("custom_id not found!!")
if not_uploaded == False:
	files = {
    'data': (None, '{"url": "https://docs.google.com/uc?export=download&id=10jArmkUCWldHeNajwRX3gMvzM5iaVdKe","custom_id":"XCUITestApp"}'),
	}

	response = requests.post('https://api-cloud.browserstack.com/app-automate/xcuitest/test-suite', files=files, auth=(BROWSERSTACK_USERNAME,BROWSERSTACK_ACCESS_KEY))
	print(response.status_code)


###################XCUITest Test App Upload #########################


###################XCUITest Run Test #########################

headers = {
    'Content-Type': 'application/json',
}

data = '{"devices": ["iPhone 8 Plus-11"], "app": "XCUIApp", "deviceLogs" : "true", "testSuite": "XCUITestApp"}'

response = requests.post('https://api-cloud.browserstack.com/app-automate/xcuitest/build', headers=headers, data=data, auth=(BROWSERSTACK_USERNAME,BROWSERSTACK_ACCESS_KEY))
print(response.status_code)
print(response.json())
###################XCUITest Run Test #########################




