import functools
import importlib.metadata
from pathlib import Path
from typing import Final

@functools.cache
def get_distribution() -> importlib.metadata.Distribution:
    try:
        distribution = importlib.metadata.distribution("vsg")
    except importlib.metadata.PackageNotFoundError:
        distribution = importlib.metadata.PathDistribution(path=Path())
    return distribution


@functools.cache
def get_version() -> str:
    return get_distribution().version or "DEVELOP"


def print_version(oCommandLineArguments):
    if (oCommandLineArguments.version):
        print('VHDL Style Guide (VSG) version: ' + get_version())
        exit(0)
