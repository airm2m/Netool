from distutils.core import setup
import py2exe

setup(
console=['netool.py'],
options={
    "py2exe":{
        "bundle_files": 1
    }
}
)