import pathlib, os, platform

base = "tflite_runtime-2.5.0.post1-cp39-cp39-linux_{}.whl#sha={}"

versions = {
    "AARCH64": {
        "name": "aarch64",
        "sha256": "sha256=9839c3acb506b5003a9bd3860329a8ae20e675efbae14dbea02659b0054f42c6"
    },
    "ARMV71": {
        "name": "armv71",
        "sha256": "sha256=44ade5fa9d429ff7fcd439b596aa4df6f8fef67c9499eae3f1ed6243e4c99e53"
    },
    "x86_64": {
        "name": "x86_64",
        "sha256": "sha256=132f8c184b99d69e40040d8067eb962d9435cd2579f5563c33b8673d257d353d"
    }
}
machine = platform.machine()

to_add = "./resources/" + base.format(
    versions[machine]["name"],
    versions[machine]["sha256"]
)
with open("requirements.txt", "a") as requirements:
    requirements.write(
        "\n" + to_add
    )