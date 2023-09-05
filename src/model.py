"""ml-related shenanigans"""
import random
import tflite_runtime.interpreter as tflite
import numpy as np

def _get_model():
	model_path = "yamnet_classification.tflite"
	interpreter = tflite.Interpreter(model_path)

	input_details = interpreter.get_input_details()
	print(input_details)

	output_details = interpreter.get_output_details()
	print("\n", output_details)

	return interpreter

def _normalize(arr: np.ndarray):
	"""goto range [-1,1]; assumes all are positive"""
	zerodiff = min(arr) + ((max(arr) - min(arr)) / 2)
	new_arr = (arr - zerodiff)
	new_arr = new_arr / max(new_arr)
	return new_arr

def _classify(input_arr: np.ndarray, interpreter):
	"""Classification"""
	nrmd_arr = _normalize(input_arr)
	res = interpreter(nrmd_arr)
	print(res)
	return True



def _classify_fake(frames):
	return random.random() >= 0.85

def _test_response():
	return "1"

if __name__ == "__main__":
	_get_model()