import pytest
import subprocess
from unittest.mock import patch

from ..logic.mesonbuild import MesonBuild

class TestMesonBuild:
    @pytest.fixture
    def meson_build(self):
        return MesonBuild("source_dir", "build_dir")

    @patch('subprocess.run')
    def test_setup(self, mock_run, meson_build):
        mock_run.return_value = subprocess.CompletedProcess(args=[], returncode=0, stdout="setup success", stderr="")
        result = meson_build.setup()
        assert result == "setup success"
        mock_run.assert_called_with(["meson", "setup", "build_dir", "source_dir"], capture_output=True, text=True, check=True)

    @patch('subprocess.run')
    def test_configure(self, mock_run, meson_build):
        mock_run.return_value = subprocess.CompletedProcess(args=[], returncode=0, stdout="configure success", stderr="")
        result = meson_build.configure()
        assert result == "configure success"
        mock_run.assert_called_with(["meson", "configure", "build_dir"], capture_output=True, text=True, check=True)

    @patch('subprocess.run')
    def test_compile(self, mock_run, meson_build):
        mock_run.return_value = subprocess.CompletedProcess(args=[], returncode=0, stdout="compile success", stderr="")
        result = meson_build.compile()
        assert result == "compile success"
        mock_run.assert_called_with(["meson", "compile", "-C", "build_dir"], capture_output=True, text=True, check=True)

    @patch('subprocess.run')
    def test_test(self, mock_run, meson_build):
        mock_run.return_value = subprocess.CompletedProcess(args=[], returncode=0, stdout="test success", stderr="")
        result = meson_build.test()
        assert result == "test success"
        mock_run.assert_called_with(["meson", "test", "-C", "build_dir"], capture_output=True, text=True, check=True)

    @patch('subprocess.run')
    def test_install(self, mock_run, meson_build):
        mock_run.return_value = subprocess.CompletedProcess(args=[], returncode=0, stdout="install success", stderr="")
        result = meson_build.install()
        assert result == "install success"
        mock_run.assert_called_with(["meson", "install", "-C", "build_dir"], capture_output=True, text=True, check=True)

    @patch('subprocess.run')
    def test_introspect(self, mock_run, meson_build):
        mock_run.return_value = subprocess.CompletedProcess(args=[], returncode=0, stdout="introspect success", stderr="")
        result = meson_build.introspect()
        assert result == "introspect success"
        mock_run.assert_called_with(["meson", "introspect", "build_dir"], capture_output=True, text=True, check=True)

    @patch('subprocess.run')
    def test_rewrite(self, mock_run, meson_build):
        mock_run.return_value = subprocess.CompletedProcess(args=[], returncode=0, stdout="rewrite success", stderr="")
        result = meson_build.rewrite()
        assert result == "rewrite success"
        mock_run.assert_called_with(["meson", "rewrite"], capture_output=True, text=True, check=True)

    @patch('subprocess.run')
    def test_dist(self, mock_run, meson_build):
        mock_run.return_value = subprocess.CompletedProcess(args=[], returncode=0, stdout="dist success", stderr="")
        result = meson_build.dist()
        assert result == "dist success"
        mock_run.assert_called_with(["meson", "dist"], capture_output=True, text=True, check=True)

    @patch('subprocess.run')
    def test_devenv(self, mock_run, meson_build):
        mock_run.return_value = subprocess.CompletedProcess(args=[], returncode=0, stdout="devenv success", stderr="")
        result = meson_build.devenv()
        assert result == "devenv success"
        mock_run.assert_called_with(["meson", "devenv"], capture_output=True, text=True, check=True)

    @patch('subprocess.run')
    def test_wrap(self, mock_run, meson_build):
        mock_run.return_value = subprocess.CompletedProcess(args=[], returncode=0, stdout="wrap success", stderr="")
        result = meson_build.wrap()
        assert result == "wrap success"
        mock_run.assert_called_with(["meson", "wrap"], capture_output=True, text=True, check=True)

    @patch('subprocess.run')
    def test_subprojects(self, mock_run, meson_build):
        mock_run.return_value = subprocess.CompletedProcess(args=[], returncode=0, stdout="subprojects success", stderr="")
        result = meson_build.subprojects()
        assert result == "subprojects success"
        mock_run.assert_called_with(["meson", "subprojects"], capture_output=True, text=True, check=True)

    @patch('subprocess.run')
    def test_init(self, mock_run, meson_build):
        mock_run.return_value = subprocess.CompletedProcess(args=[], returncode=0, stdout="init success", stderr="")
        result = meson_build.init()
        assert result == "init success"
        mock_run.assert_called_with(["meson", "init"], capture_output=True, text=True, check=True)
