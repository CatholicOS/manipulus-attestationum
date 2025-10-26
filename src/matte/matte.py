import os, argparse, pathlib, tomllib
from query_handler import handle_query
from formatter import format_files

current_dir = pathlib.Path(__file__).parent.resolve()
package_toml_path = os.path.join(current_dir, "../../pyproject.toml")

with open(package_toml_path, "rb") as f:
    project_data = tomllib.load(f)


# ----------------------------------------
# Main point of entry into MATTE functions
# ----------------------------------------


def handle_user_query(query_input):
    print(f"[MATTE] Handling user query: {query_input}.")

    # Do whatever transforms are needed before passing
    # data into system
    processed_query = f"placeholder: {query_input}"

    # Retrieve scripture text
    scripture_data = handle_query(processed_query)

    # Format and package scripture text
    packaged_files = format_files(scripture_data)

    return packaged_files


# ----------------------------------------
# CLI Invocation
# ----------------------------------------


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description=project_data["project"]["description"])

    parser.add_argument("-i", "--input", help="Path to input file", required=True)
    parser.add_argument(
        "-o", "--outpath", help="Path to output directory", required=False
    )
    parser.add_argument(
        "-c", "--config", help="Path to configuration file", required=False
    )

    args = vars(parser.parse_args())
    print(args)

    input = args["input"]
    outpath = args["outpath"]
    config = args["config"]

    print(f"[MATTE] Input: {input}")
    print(f"[MATTE] Output Path: {outpath}")
    print(f"[MATTE] Config: {config}")

    query_in = {"placeholder": True}

    outfiles = handle_user_query(query_in)
    print(f"[MATTE] Sending final output: {outfiles}")
