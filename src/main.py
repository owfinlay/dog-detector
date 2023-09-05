"""main audio input file"""
import pyaudio
import os, sys, requests
from model import _classify_fake, _test_response
import numpy as np

SENSITIVITY = 5

samplerate = 16000
chunksize = 512

def updated_frames(frames, id_num):
	"""Returns updated cache of audio data
	Input:
		frames: cached frames (bytes)
		id_num: new frame (bytes)
	Output:
		Updated frames
	"""
	return np.vstack([frames[1:], id_num])


def updated_chfls(check_flags, id_num, sensitivity):
	"""Updating check-flags
	Input:
		check_flags: cached check-flags corresponding to frame cache
		id_num: new frame (bytecode)
		sensitivity: user-defined sensitivity rating
	Output:
		Updated check flags
	"""
	check_this_one = False
	if max(id_num) - min(id_num) >= (11 - sensitivity) * 0.1:
		check_this_one = True
	return check_flags[1:] + [check_this_one]


def classify(frames):
	"""Running the classification model
	Input:
		frames: cached bytecode
	Output:
		Boolean, True if bark else False
	"""
	print("Do something with frames here later")
	return _classify_fake(frames)


def notify(path: str):
	"""Placeholder for Arnold's URL call"""
	print("Do some URL thing here later")

pa = pyaudio.PyAudio()

# Maybe put in separate config file // set ENV variables there
device_defaults = pa.get_default_input_device_info()
if device_defaults['maxInputChannels'] == 0:
	print("Can't find an input channel")
	sys.exit(1)
else:
	channels = 1
del device_defaults


potential_barks = 0
sensitivity = os.environ.get("SENSITIVITY", SENSITIVITY)
frames = np.zeros((31, 512))
check_flags = [False] * 31


def callback(in_data, frame_count, time_info, status_flags):
	global frames
	global check_flags
	global sensitivity
	global potential_barks

	id_num = np.frombuffer(in_data, dtype=np.float32)
	print("Lengths of in data num and in data: ", len(id_num), len(in_data))

	frames = updated_frames(frames, id_num)
	check_flags = updated_chfls(check_flags, id_num, sensitivity)

	if any(check_flags):
		potential_barks += 1

	print(f"Callback has ended. {potential_barks} potential barks.")
	return (None, pyaudio.paContinue)


with pa.open(
	rate = samplerate,
	format = pyaudio.paFloat32,
	channels = 1,
	frames_per_buffer = chunksize,
	input = True,
	stream_callback = callback
) as stream:

	inp = ""
	while inp != "stop":
		inp = input("Listening... type 'stop' to end the stream ~\n\t")

pa.terminate()
print("Noises checked: ", potential_barks)