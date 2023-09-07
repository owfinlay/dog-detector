"""Go get the proper tflite runtime from resources/"""
import os, platform


base_str = "resources/tflite_runtime-2.5.0.post1-cp39-cp39-linux_{}.whl"

version = {
    "AARCH64": "aarch64",
    "ARMV71": "armv71",
    "x86_64": "x86_64"
}
machine = platform.machine()
to_add = base_str.format(version[machine])

with open("requirements.txt", "a") as reqs:
    reqs.write("\n" + to_add)