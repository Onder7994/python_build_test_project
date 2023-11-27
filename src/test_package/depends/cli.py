import argparse
from dataclasses import dataclass
from importlib.metadata import version

@dataclass
class CommandLineParser:
    file: str

    @classmethod
    def create_parser(cls):
        parser = argparse.ArgumentParser(description="Test CMD")
        parser.add_argument(
            "-f", "--file", dest="file",
            required=True,
            help="Path to yaml file"
        )
        parser.add_argument(
            "-v", "--version",
            action="version",
            version=f"%(prog)s {version('test-package')}",
            help="Show package version"
        )
        return parser
