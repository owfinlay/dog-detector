"""ml-related shenanigans"""
import random
import tflite_runtime.interpreter as tflite
import numpy as np

def get_model_path():
	import os
	return 

def normalize(arr: np.ndarray) -> np.ndarray:
	"""goto range [-1,1]; assumes all are positive"""
	zerodiff = arr.min() + ((arr.max() - arr.min()) / 2)
	new_arr = (arr - zerodiff)
	new_arr = (new_arr / new_arr.max()).flatten()
	return new_arr[:15600]

def _classify(input_arr: np.ndarray) -> bool:
	"""Classification"""
	model_path = "E:\\Learning\\DS_Comms\\upwork\\DDD\\src\\src\\yamnet_classification.tflite"
	normed_arr = normalize(input_arr)

	interpreter = tflite.Interpreter(model_path)
	input_details = interpreter.get_input_details()
	output_details = interpreter.get_output_details()

	interpreter.allocate_tensors()
	interpreter.set_tensor(input_details[0]['index'], normed_arr)
	interpreter.invoke()

	output_data = interpreter.get_tensor(output_details[0]['index'])
	bark_probability = output_data[0][70]
	return(bark_probability >= .5)

def _test_response():
	return random.random() > 0.8

def _print_details():
	model_path = "yamnet_classification.tflite"
	interpreter = tflite.Interpreter(model_path)\

	print("Input details: ", interpreter.get_input_details())
	print("\nOutput details: ", interpreter.get_output_details())

if __name__ == "__main__":
	_print_details()
