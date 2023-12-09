from pathlib import Path


def path(file_name):
    # os.path.realpath(f'image/{file_name}')
    return str(
        Path(__file__).parent.parent.joinpath(f"images/examples/{file_name}").absolute()
    )
