import os
import sys

# So we can access app_info.py
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))


def _get_ver_string():
    from app_info import APP_INFO

    return "{}.{}.{}".format(
        APP_INFO.APP_VERSION.Major,
        APP_INFO.APP_VERSION.Minor,
        APP_INFO.APP_VERSION.Revision,
    )


def build_resources():
    import os
    import PySide

    QRC_FILE = 'resources.qrc'
    PY_OUTPUT = os.path.join('src', 'resources.py')

    pyside_dir = os.path.dirname(PySide.__file__)
    pyrcc_path = os.path.join(pyside_dir, 'pyside-rcc')

    cmd = "{} -o {} {}".format(
        pyrcc_path,
        PY_OUTPUT,
        QRC_FILE
    )

    os.system(cmd)


def build_ui():
    import os
    from pysideuic import compileUiDir

    design_dir = os.path.join(os.path.dirname(__file__), 'designer')

    def uicmap(py_dir, py_file):
        rtn_dir = os.path.join("src", "ui")
        rtn_file = py_file.replace(".py", "_ui.py")

        return rtn_dir, rtn_file

    compileUiDir(design_dir, map=uicmap)


def build_exe():
    import os
    import sys
    import cx_Freeze

    from app_info import APP_INFO

    # have to make sure args looks right
    sys.argv = sys.argv[:1] + ['build']

    app_path = os.path.join(os.path.dirname(__file__), "src", "application.py")

    if sys.platform == 'win32':
        executables = [cx_Freeze.Executable(
            app_path,
            targetName=APP_INFO.APP_NAME + ".exe",
            icon=os.path.join('icons', 'icon.ico'),
            base="Win32GUI")]
    else:
        executables = [cx_Freeze.Executable(
            app_path,
            targetName=APP_INFO.APP_NAME,
            icon=os.path.join('icons', 'icon.png'))]

    include_files = [
        os.path.join("icons", 'icon.ico')
    ]

    options = {
        'build_exe': {
            "include_files": include_files
        }
    }

    cx_Freeze.setup(
        name=APP_INFO.APP_NAME,
        version=_get_ver_string(),
        executables=executables,
        options=options
    )


def build_win_install():
    from app_info import APP_INFO
    import os
    os.system('iscc' +
              ' /DMyAppVersion="{}"'.format(_get_ver_string()) +
              ' /DMyAppName="{}"'.format(APP_INFO.APP_NAME) +
              ' /DMyAppPublisher="{}"'.format(APP_INFO.APP_PUBLISHER) +
              ' /DMyAppURL="{}"'.format(APP_INFO.APP_URL) +
              ' /DMyAppExeName="{}"'.format(APP_INFO.APP_NAME + ".exe") +
              ' inno_setup.iss'
    )


def _usage():
    import sys
    sys.stdout.write("""
Usage:

    build resources  -  Build resources.py
    build ui         -  Build .py files from .ui files in ui directory.
    build exe        -  Build executable using cx-Freeze.
    build installer  -  Build windows installer using Inno Setup.

""")


if __name__ == '__main__':
    import sys
    args = sys.argv[1:]

    if len(args) != 1:
        _usage()
        sys.exit(1)

    mode = args[0]

    if mode == "resources":
        build_resources()
    elif mode == "ui":
        build_ui()
    elif mode == "exe":
        build_resources()
        build_ui()
        build_exe()
    elif mode == "installer":
        if sys.platform == 'win32':
            build_resources()
            build_ui()
            build_exe()
            build_win_install()
        else:
            sys.stdout.write("Can't build windows installer on non windows system.")
            sys.exit(1)
    else:
        _usage()
        sys.exit(1)
