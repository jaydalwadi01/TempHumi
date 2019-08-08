import constants
import smbus

bus = 0

def begin(channel):
	global bus
	bus = smbus.SMBus(channel)

def Read_Temperature():
	global bus
	bus.write_byte_data(constants.DEVICE_ID, constants.REG_CONFIG, constants.CMD_MEASURE_TEMP)
	while Is_Available() == 0:
		pass
	high = bus.read_byte_data(constants.DEVICE_ID, constants.REG_DATA_H)
	low = bus.read_byte_data(constants.DEVICE_ID, constants.REG_DATA_L)
	data  = (high << 8) | low
	temp_val  = data >> 2
	temp = (temp_val / 32.0) - 50.0
	return temp

def Read_Humidity():
	global bus
	bus.write_byte_data(constants.DEVICE_ID, constants.REG_CONFIG, constants.CMD_MEASURE_HUMI)
	while Is_Available() == 0:
		pass
	high = bus.read_byte_data(constants.DEVICE_ID, constants.REG_DATA_H)
	low = bus.read_byte_data(constants.DEVICE_ID, constants.REG_DATA_L)
	data  = (high << 8) | low
	humi_val = data >> 4
	humi = (humi_val / 16.0) - 24.0
	return humi

def Is_Available():
	global bus
	val = bus.read_byte_data(constants.DEVICE_ID, constants.REG_STATUS)
	return val

