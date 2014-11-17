import os
from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")
use_plugin("exec")


name = "ehw"
default_task = "publish"


@init
def set_properties(project):
    project.set_property("dir_source_main_python", "ehw")
    project.set_property("dir_source_main_scripts", "bin")

    project.set_property("dir_source_unittest_python", "tests")
    project.set_property("unittest_module_glob", "test_*")
    project.set_property("unittest_test_method_prefix", "test")
    project.set_property(
        "run_unit_tests_command",
        "py.test %s" % project.expand_path("$dir_source_unittest_python"))
    project.set_property("run_unit_tests_propagate_stdout", True)
    project.set_property("run_unit_tests_propagate_stderr", True)
