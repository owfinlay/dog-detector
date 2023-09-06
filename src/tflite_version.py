import pathlib, os, platform

path = pathlib.Path("resources/tflite_runtimes")

base = "tflite_runtime-2.5.0.post1-cp39-cp39-linux_{}.whl"

versions = {
    "AARCH64": "aarch64",
    "ARMV71": "armv71",
    "x86_64": "x86_64"
}
machine = platform.machine()

with open("requirements.txt", "a") as requirements:
    requirements.write(
        "\n",
        str(path / base.format(versions[machine]))
    )