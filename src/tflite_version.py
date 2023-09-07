"""script for builder step"""
def edit_reqs():
    import platform

    base_str = "resources/tflite_runtime-2.5.0.post1-cp39-cp39-linux_{}.whl"
    interim = {
        "AARCH64": "aarch64",
        "ARMV71": "armv71",
        "x86_64": "x86_64"
    }
    machine = platform.machine()
    rel_pathstr = base_str.format(interim[machine])

    with open("requirements.txt", "a") as reqs:
        reqs.write("\n" + rel_pathstr)
    return rel_pathstr

def rm_extra_runtimes(rel_pathstr):
    import os, pathlib

    rel_wheel = pathlib.Path(rel_pathstr)

    other_wheels = [f for f in rel_path.glob("*/*.whl") if f != rel_wheel]
    for f in other_wheels:
        os.remove(f)

if __name__ == "__main__":
    pathstr = edit_reqs()
    rm_extra_runtimes(pathstr)