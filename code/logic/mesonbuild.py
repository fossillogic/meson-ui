#
# ==============================================================================
# Author: Michael Gene Brockus (Dreamer)
# Email: michaelbrockus@gmail.com
# Organization: Fossil Logic
# Description:
#     This file is part of the Fossil Logic project, where innovation meets
#     excellence in software development. Michael Gene Brockus, also known as
#     "Dreamer," is a dedicated contributor to this project. For any inquiries,
#     feel free to contact Michael at michaelbrockus@gmail.com.
# ==============================================================================
#
import subprocess


class MesonBuild:
    def __init__(self, source_dir, build_dir):
        self.source_dir = source_dir
        self.build_dir = build_dir

    def setup(self, options=""):
        command = ["meson", "setup", self.build_dir, self.source_dir] + options.split()
        return self.run_command(command)

    def configure(self, options=""):
        command = ["meson", "configure", self.build_dir] + options.split()
        return self.run_command(command)

    def compile(self):
        command = ["meson", "compile", "-C", self.build_dir]
        return self.run_command(command)

    def test(self):
        command = ["meson", "test", "-C", self.build_dir]
        return self.run_command(command)

    def install(self):
        command = ["meson", "install", "-C", self.build_dir]
        return self.run_command(command)

    def introspect(self, options=""):
        command = ["meson", "introspect", self.build_dir] + options.split()
        return self.run_command(command)

    def rewrite(self, options=""):
        command = ["meson", "rewrite"] + options.split()
        return self.run_command(command)

    def dist(self, options=""):
        command = ["meson", "dist"] + options.split()
        return self.run_command(command)

    def devenv(self, options=""):
        command = ["meson", "devenv"] + options.split()
        return self.run_command(command)

    def wrap(self, options=""):
        command = ["meson", "wrap"] + options.split()
        return self.run_command(command)

    def subprojects(self, options=""):
        command = ["meson", "subprojects"] + options.split()
        return self.run_command(command)

    def init(self, options=""):
        command = ["meson", "init"] + options.split()
        return self.run_command(command)

    def run_command(self, command):
        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f"Command '{' '.join(command)}' failed with error: {e.stderr}"
        except Exception as e:
            return f"An unexpected error occurred: {str(e)}"
