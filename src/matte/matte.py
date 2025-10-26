import argparse
import tomllib
import pathlib
import os

current_dir = pathlib.Path(__file__).parent.resolve()
package_toml_path = os.path.join(current_dir, "../../pyproject.toml")

with open(package_toml_path, "rb") as f:
    project_data = tomllib.load(f)

parser = argparse.ArgumentParser(description=project_data["project"]["description"])

parser.add_argument("-i", "--input", help="Path to input file", required=True)
parser.add_argument("-o", "--outpath", help="Path to output directory", required=False)
parser.add_argument("-c", "--config", help="Path to configuration file", required=False)

args = vars(parser.parse_args())
