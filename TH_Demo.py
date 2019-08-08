import TH_apis
import time

TH_apis.begin(1)

while 1:

	temp = TH_apis.Read_Temperature()
	humi = TH_apis.Read_Humidity()
	print(temp)
	print(humi)
	time.sleep(10)
