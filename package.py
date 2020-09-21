
name = "PySide2"

description = "Python bindings for the Qt cross-platform application " \
              "and UI framework"

version = "5.15.0"

requires = [
    "shiboken2==5.15.0"
]

variants = [
    ["os-*", "python-3.6"],
    ["os-*", "python-3.7"],
]


private_build_requires = ["rezutil-1", "pipz"]
build_command = "python -m rezutil build {root} --use-pipz"


def commands():
    env = globals()["env"]

    env.PATH.prepend("{root}/bin")
    env.PYTHONPATH.prepend("{root}/python")
