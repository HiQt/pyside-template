import os


def build_ui():
    from pysideuic import compileUiDir

    def uic_map(directory, module_name):
        directory = os.path.join("src", directory)
        return directory, module_name

    compileUiDir(
        "ui",
        recurse=True,
        map=uic_map
    )

if __name__ == '__main__':
    build_ui()
