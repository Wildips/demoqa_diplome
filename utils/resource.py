import json
from pathlib import Path


def image_path(file_name):
    # try for os implementation
    # os.path.abspath(os.path.join(os.path.dirname(__file__), '../schema'))
    return str(
        Path(__file__).parent.parent.joinpath(f"images/examples/{file_name}").absolute()
    )


def load_schema(schema_cursor):
    with open(
        Path(__file__).parent.parent.joinpath(f"schemes/{schema_cursor}").absolute()
    ) as file:
        schema = json.load(file)
        return schema
