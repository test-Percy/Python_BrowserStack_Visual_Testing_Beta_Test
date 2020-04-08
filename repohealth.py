import os,subprocess

try:
	subprocess.call(["python3","single.py"])

	subprocess.call(["python3","parallel.py"])

	subprocess.call(["python3","local.py"])

	subprocess.call(["python3","android-appium.py"])

	subprocess.call(["python3","ios-appium.py"])

	subprocess.call(["python3","espresso.py"])

	subprocess.call(["python3","xcuitest.py"])

	subprocess.call(["python3","earlgrey.py"])




except:
	print("something Wrong!!")

# subprocess.check_call("exit 1", shell=True)

# os.system("python3 single.py")

# os.system("python3 parallel.py")

# os.system("python3 local.py")

# os.system("python3 espresso.py")

# os.system("python3 earlgrey.py")

# os.system("python3 xcuittest.py")

# os.system("python3 android-appium.py")

# os.system("python3 ios-appium.py")




