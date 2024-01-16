from pathlib import Path


def image_path(file_name):
    return str(
        Path(__file__)
        .parent.parent.parent.joinpath(f"images/examples/{file_name}")
        .absolute()
    )
