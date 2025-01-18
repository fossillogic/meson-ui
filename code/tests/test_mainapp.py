import pytest
from unittest.mock import patch
import tkinter as tk
from tkinter import ttk
from ..logic.appmain import MesonBuildGUI


class TestMesonBuildGUI:
    
    @pytest.fixture
    def app(self):
        root = tk.Tk()
        app = MesonBuildGUI(root)
        yield app
        root.destroy()

    def test_initialization(self, app):
        assert app.root.title() == "Meson Build GUI"
        assert app.root.geometry() == "660x400"
        assert not app.root.resizable()

    def test_apply_styles(self, app):
        app.apply_styles()
        style = ttk.Style()
        assert style.lookup("Blue.TButton", "foreground") == "black"
        assert style.lookup("Blue.TButton", "background") == "#ADD8E6"

    def test_create_widgets(self, app):
        app.create_widgets()
        assert isinstance(app.setup_button, ttk.Button)
        assert app.setup_button.cget("text") == "Setup"
        assert isinstance(app.source_dir_label, ttk.Label)
        assert app.source_dir_label.cget("text") == "Source Directory:"

    def test_set_theme(self, app):
        app.set_theme("light")
        assert app.root.cget("bg") == "white"
        app.set_theme("dark")
        assert app.root.cget("bg") == "black"
        app.set_theme("meson")
        assert app.root.cget("bg") == "dark gray"

    def test_browse_source_dir(self, app):
        with patch("tkinter.filedialog.askdirectory", return_value="/path/to/source"):
            app.browse_source_dir()
            assert app.source_dir_entry.get() == "/path/to/source"
            assert app.build_dir_entry.get() == "/path/to/source/builddir"

    def test_clear_paths(self, app):
        app.source_dir_entry.insert(0, "some/path")
        app.build_dir_entry.insert(0, "some/path")
        app.clear_paths()
        assert app.source_dir_entry.get() == ""
        assert app.build_dir_entry.get() == ""

    def test_update_terminal(self, app):
        app.update_terminal("Test message")
        assert "Test message" in app.terminal.get("1.0", tk.END)

    def test_setup_project(self, app):
        with patch("threading.Thread.start") as mock_thread:
            app.setup_project()
            assert mock_thread.called

    def test_configure_project(self, app):
        with patch("threading.Thread.start") as mock_thread:
            app.configure_project()
            assert mock_thread.called

    def test_compile_project(self, app):
        with patch("threading.Thread.start") as mock_thread:
            app.compile_project()
            assert mock_thread.called

    def test_test_project(self, app):
        with patch("threading.Thread.start") as mock_thread:
            app.test_project()
            assert mock_thread.called

    def test_install_project(self, app):
        with patch("threading.Thread.start") as mock_thread:
            app.install_project()
            assert mock_thread.called

    def test_show_version(self, app):
        with patch("threading.Thread.start") as mock_thread:
            app.show_version()
            assert mock_thread.called

    def test_show_introspection(self, app):
        with patch("threading.Thread.start") as mock_thread:
            app.show_introspection()
            assert mock_thread.called

    def test_clear_terminal(self, app):
        app.terminal.insert(tk.END, "Some text")
        app.clear_terminal()
        assert app.terminal.get("1.0", tk.END) == "\n"

    def test_get_tool_info(self, app):
        with patch("threading.Thread.start") as mock_thread:
            app.get_tool_info()
            assert mock_thread.called

    def test_show_tutorial(self, app):
        with patch("tkinter.messagebox.showerror") as mock_messagebox:
            app.show_tutorial()
            assert not mock_messagebox.called

    def test_init_project(self, app):
        with patch("threading.Thread.start") as mock_thread:
            app.init_project()
            assert mock_thread.called

    def test_manage_subprojects(self, app):
        with patch("tkinter.messagebox.showerror") as mock_messagebox:
            app.manage_subprojects()
            assert not mock_messagebox.called
