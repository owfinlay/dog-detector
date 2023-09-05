"""ml-related shenanigans"""
import random
import tflite_runtime.interpreter as tflite
import numpy as np

def _normalize(arr: np.ndarray):
	"""goto range [-1,1]; assumes all are positive"""
	zerodiff = min(arr) + ((max(arr) - min(arr)) / 2)
	new_arr = (arr - zerodiff)
	new_arr = new_arr / max(new_arr)
	return new_arr

def _classify(input_arr: np.ndarray):
	"""Classification"""
	model_path = "yamnet_classification.tflite"
	normed_arr = _normalize(input_arr)

	interpreter = tflite.Interpreter(model_path)
	input_index = interpreter.get_input_details()[0]['index']
	output_index = interpreter.get_output_details()[0]['index']

	interpreter.allocate_tensors()
	interpreter.set_tensor(input_index, normed_arr)
	interpreter.invoke()

	output_data = interpreter.get_tensor(output_index)
	print(output_data)
	return random.random >= 0.81

def _test_response():
	return "1"

def _print_details():
	model_path = "yamnet_classification.tflite"
	interpreter = tflite.Interpreter(model_path)\

	print("Input details: ", interpreter.get_input_details())
	print("\nOutput details: ", interpreter.get_output_details())

if __name__ == "__main__":
	_print_details()
