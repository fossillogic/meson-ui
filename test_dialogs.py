import pytest
from tkinter import Tk
import tkinter as tk
import subprocess
from ..logic.dialog.init import InitDialog
from ..logic.dialog.configure import ConfigureDialog
from ..logic.dialog.setup import SetupDialog
from ..logic.dialog.subprojects import SubprojectsDialog
from ..logic.dialog.tutorial import TutorialDialog


class TestInitDialog:
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.root = Tk()
        self.root.withdraw()
        self.dialog = InitDialog(self.root, theme="light")
        yield
        self.root.destroy()

    def test_dialog_initialization(self):
        assert self.dialog.theme == "light"
        assert self.dialog.result is None

    def test_dialog_body(self):
        self.dialog.body(self.dialog)
        assert self.dialog.project_name_entry.winfo_exists()
        assert self.dialog.language_entry.winfo_exists()
        assert self.dialog.other_options_entry.winfo_exists()

    def test_apply_with_valid_data(self):
        self.dialog.project_name_entry.insert(0, "TestProject")
        self.dialog.language_entry.insert(0, "Python")
        self.dialog.other_options_entry.insert(0, "--option")
        self.dialog.apply()
        assert self.dialog.result == ("TestProject", "Python", "--option")

    def test_apply_with_empty_project_name(self):
        self.dialog.project_name_entry.insert(0, "")
        self.dialog.language_entry.insert(0, "Python")
        self.dialog.apply()
        assert self.dialog.result is None

    def test_apply_with_empty_language(self):
        self.dialog.project_name_entry.insert(0, "TestProject")
        self.dialog.language_entry.insert(0, "")
        self.dialog.apply()
        assert self.dialog.result is None

    def test_cancel(self):
        self.dialog.cancel()
        assert self.dialog.result is None

    def test_ok_with_valid_data(self):
        self.dialog.project_name_entry.insert(0, "TestProject")
        self.dialog.language_entry.insert(0, "Python")
        self.dialog.ok()
        assert self.dialog.result is None

    def test_apply_theme_light(self):
        self.dialog.apply_theme()
        assert self.dialog.cget("bg") == "white"

    def test_apply_theme_dark(self):
        dialog = InitDialog(self.root, theme="dark")
        dialog.apply_theme()
        assert dialog.cget("bg") == "black"

    def test_apply_theme_meson(self):
        dialog = InitDialog(self.root, theme="meson")
        dialog.apply_theme()
        assert dialog.cget("bg") == "dark gray"


class TestConfigureDialog:
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.root = Tk()
        self.root.withdraw()
        self.dialog = ConfigureDialog(self.root, theme="light")
        yield
        self.root.destroy()

    def test_dialog_initialization(self):
        assert self.dialog.theme == "light"
        assert self.dialog.result is None

    def test_dialog_body(self):
        self.dialog.body(self.dialog)
        assert self.dialog.build_dir_entry.winfo_exists()
        assert self.dialog.other_options_entry.winfo_exists()

    def test_apply_with_valid_data(self):
        self.dialog.build_dir_entry.insert(0, "builddir")
        self.dialog.other_options_entry.insert(0, "--option")
        self.dialog.apply()
        assert self.dialog.result == ("builddir", "--option")

    def test_apply_with_empty_build_dir(self):
        self.dialog.build_dir_entry.insert(0, "")
        self.dialog.other_options_entry.insert(0, "--option")
        self.dialog.apply()
        assert self.dialog.result is None

    def test_cancel(self):
        self.dialog.cancel()
        assert self.dialog.result is None

    def test_ok_with_valid_data(self):
        self.dialog.build_dir_entry.insert(0, "builddir")
        self.dialog.other_options_entry.insert(0, "--option")
        self.dialog.ok()
        assert self.dialog.result is None

    def test_apply_theme_light(self):
        self.dialog.apply_theme()
        assert self.dialog.cget("bg") == "white"

    def test_apply_theme_dark(self):
        dialog = ConfigureDialog(self.root, theme="dark")
        dialog.apply_theme()
        assert dialog.cget("bg") == "black"

    def test_apply_theme_meson(self):
        dialog = ConfigureDialog(self.root, theme="meson")
        dialog.apply_theme()
        assert dialog.cget("bg") == "dark gray"


class TestSetupDialog:
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.root = Tk()
        self.root.withdraw()
        self.dialog = SetupDialog(self.root, theme="light")
        yield
        self.root.destroy()

    def test_dialog_initialization(self):
        assert self.dialog.theme == "light"
        assert self.dialog.result is None

    def test_dialog_body(self):
        self.dialog.body(self.dialog)
        assert self.dialog.build_dir_entry.winfo_exists()
        assert self.dialog.other_options_entry.winfo_exists()

    def test_apply_with_valid_data(self):
        self.dialog.build_dir_entry.insert(0, "builddir")
        self.dialog.other_options_entry.insert(0, "--option")
        self.dialog.apply()
        assert self.dialog.result == ("builddir", "--option")

    def test_apply_with_empty_build_dir(self):
        self.dialog.build_dir_entry.insert(0, "")
        self.dialog.other_options_entry.insert(0, "--option")
        self.dialog.apply()
        assert self.dialog.result is None

    def test_cancel(self):
        self.dialog.cancel()
        assert self.dialog.result is None

    def test_ok_with_valid_data(self):
        self.dialog.build_dir_entry.insert(0, "builddir")
        self.dialog.other_options_entry.insert(0, "--option")
        self.dialog.ok()
        assert self.dialog.result is None

    def test_apply_theme_light(self):
        self.dialog.apply_theme()
        assert self.dialog.cget("bg") == "white"

    def test_apply_theme_dark(self):
        dialog = SetupDialog(self.root, theme="dark")
        dialog.apply_theme()
        assert dialog.cget("bg") == "black"

    def test_apply_theme_meson(self):
        dialog = SetupDialog(self.root, theme="meson")
        dialog.apply_theme()
        assert dialog.cget("bg") == "dark gray"


class TestSubprojectsDialog:
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.root = Tk()
        self.root.withdraw()
        self.dialog = SubprojectsDialog(self.root, theme="light")
        yield
        self.root.destroy()

    def test_dialog_initialization(self):
        assert self.dialog.theme == "light"

    def test_dialog_body(self):
        self.dialog.body(self.dialog)
        assert self.dialog.notebook.winfo_exists()
        assert self.dialog.update_button.winfo_exists()
        assert self.dialog.download_button.winfo_exists()
        assert self.dialog.purge_button.winfo_exists()

    def test_apply_theme_light(self):
        self.dialog.apply_theme()
        assert self.dialog.cget("bg") == "white"

    def test_apply_theme_dark(self):
        dialog = SubprojectsDialog(self.root, theme="dark")
        dialog.apply_theme()
        assert dialog.cget("bg") == "black"

    def test_apply_theme_meson(self):
        dialog = SubprojectsDialog(self.root, theme="meson")
        dialog.apply_theme()
        assert dialog.cget("bg") == "dark gray"

    def test_fetch_subprojects_no_directory(self, mocker):
        mocker.patch("os.path.exists", return_value=False)
        result = self.dialog.fetch_subprojects()
        assert result == "No subprojects directory found."

    def test_fetch_subprojects_empty_directory(self, mocker):
        mocker.patch("os.path.exists", return_value=True)
        mocker.patch("os.listdir", return_value=[])
        result = self.dialog.fetch_subprojects()
        assert result == "No subprojects found."

    def test_fetch_subprojects_with_subprojects(self, mocker):
        mocker.patch("os.path.exists", return_value=True)
        mocker.patch("os.listdir", return_value=["sub1", "sub2"])
        result = self.dialog.fetch_subprojects()
        assert result == "sub1\nsub2"

    def test_run_subprojects_command_success(self, mocker):
        mocker.patch(
            "subprocess.run", return_value=mocker.Mock(stdout="Success", check=True)
        )
        self.dialog.run_subprojects_command("update")
        assert "Success" in self.dialog.subprojects_text.get("1.0", tk.END)

    def test_run_subprojects_command_failure(self, mocker):
        mocker.patch(
            "subprocess.run",
            side_effect=subprocess.CalledProcessError(1, "meson", stderr="Error"),
        )
        mocker.patch("tk.messagebox.showerror")
        self.dialog.run_subprojects_command("update")
        tk.messagebox.showerror.assert_called_once_with(
            "Error", "Command failed: Error"
        )

    def test_run_subprojects_command_exception(self, mocker):
        mocker.patch("subprocess.run", side_effect=Exception("Unexpected error"))
        mocker.patch("tk.messagebox.showerror")
        self.dialog.run_subprojects_command("update")
        tk.messagebox.showerror.assert_called_once_with("Error", "Unexpected error")


class TestTutorialDialog:
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.root = Tk()
        self.root.withdraw()
        self.dialog = TutorialDialog(self.root, theme="light")
        yield
        self.root.destroy()

    def test_dialog_initialization(self):
        assert self.dialog.theme == "light"

    def test_dialog_body(self):
        self.dialog.body(self.dialog)
        assert self.dialog.notebook.winfo_exists()

    def test_apply_theme_light(self):
        self.dialog.apply_theme()
        assert self.dialog.cget("bg") == "white"

    def test_apply_theme_dark(self):
        dialog = TutorialDialog(self.root, theme="dark")
        dialog.apply_theme()
        assert dialog.cget("bg") == "black"

    def test_apply_theme_meson(self):
        dialog = TutorialDialog(self.root, theme="meson")
        dialog.apply_theme()
        assert dialog.cget("bg") == "dark gray"
