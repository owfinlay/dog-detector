"""main audio input file"""
import pyaudio
import os, sys, requests
from model import _classify
import numpy as np

pa = pyaudio.PyAudio()

device_defaults = pa.get_default_input_device_info()
if device_defaults['maxInputChannels'] == 0:
	print("No suitable input channel")
	sys.exit(1)
del device_defaults


def update_frames(frames: np.ndarray, id_num: np.ndarray):
	return np.vstack([frames[1:,], id_num])

def update_chfls(check_flags: list[bool], id_num: np.ndarray, sensitivity: int):
	check_this_one = False
	if max(id_num) > (11 - sensitivity) * 0.1:
		check_this_one = True
	return check_flags[1:] + [check_this_one]

def classify_as_bark(frames: np.ndarray, decision_threshold: int):
	return _classify(frames, decision_threshold)

def notify(path: str):
	"""Placeholder for Arnold's URL call"""
	print("Do some URL thing here later")


SENSITIVITY = 5
DECISION_THRESHOLD = 4
samplerate = 16000
chunksize = 512

sensitivity = os.environ.get("SENSITIVITY", SENSITIVITY) # editable via environment variables
decision_threshold = os.environ.get("DECISION_THRESHOLD", DECISION_THRESHOLD)

frames = np.zeros((31, 512), dtype=np.float32)
check_flags = [False] * 31

def callback(in_data, frame_count, time_info, status_flags):
	global frames, check_flags, sensitivity, decision_threshold

	id_num = np.frombuffer(in_data, dtype=np.float32)

	frames = update_frames(frames, id_num)
	check_flags = update_chfls(check_flags, id_num, sensitivity)

	if any(check_flags):
		if classify_as_bark(frames, decision_threshold):
			print("Got one!\n")

	return (None, pyaudio.paContinue)


stream = pa.open(
	rate = samplerate,
	format = pyaudio.paFloat32,
	channels = 1,
	frames_per_buffer = chunksize,
	input = True,
	stream_callback = callback
)
inp = ""
while inp != "stop":
	inp = input("Listening... type 'stop' to end the stream ~\n\t")

stream.close()
pa.terminate()