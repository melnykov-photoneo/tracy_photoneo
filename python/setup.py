# -*- coding: utf-8 -*-

import glob
import os
import shutil


from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext

MODULE_NAME = "tracy_client"


def find_files(pattern):
    return glob.glob(os.path.join(MODULE_NAME, pattern))


class ManualExtension(Extension, object):
    def __init__(self):
        super(ManualExtension, self).__init__(name=MODULE_NAME, sources=[])


class DummyBuild(build_ext):
    def build_extension(self, ext):
        extdir = os.path.abspath(os.path.dirname(self.get_ext_fullpath(ext.name)))
        extdir = os.path.join(extdir, MODULE_NAME)

        for entry in find_files("*cpython*"):
            shutil.copy(
                os.path.abspath(entry),
                os.path.join(extdir, os.path.basename(entry)),
            )


setup(
    name=MODULE_NAME,
    version="0.10.0",
    author="Bartosz Taudul",
    author_email="wolf@nereid.pl",
    description="A real time, nanosecond resolution, remote telemetry, hybrid frame and sampling profiler for games and other applications.",
    long_description="This package contains the client code only. See the documentation for further details.",
    url="https://github.com/wolfpld/tracy",
    ext_modules=[ManualExtension()],
    cmdclass={"build_ext": DummyBuild},
    package_dir={"": "."},
    package_data={"": ["py.typed"]},
    data_files=[
        ("lib", find_files("lib*")),
        ("include/client", find_files("client/*.h*")),
        ("include/common", find_files("common/*.h*")),
        ("include/tracy", find_files("tracy/*.h*")),
    ],
    include_package_data=True,
    zip_safe=False,
)
