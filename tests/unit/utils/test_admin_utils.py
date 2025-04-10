import pytest
from unittest.mock import patch, MagicMock
from monitormaestro.utils.admin_utils import AdminUtils


class TestAdminUtils:
    @patch("ctypes.windll.shell32.IsUserAnAdmin")
    def test_is_admin_true(self, mock_is_admin):
        """测试管理员权限检查(有权限)"""
        mock_is_admin.return_value = True
        assert AdminUtils.is_admin() is True

    @patch("ctypes.windll.shell32.IsUserAnAdmin")
    def test_is_admin_false(self, mock_is_admin):
        """测试管理员权限检查(无权限)"""
        mock_is_admin.return_value = False
        assert AdminUtils.is_admin() is False

    @patch("monitormaestro.utils.admin_utils.AdminUtils.is_admin")
    @patch("ctypes.windll.shell32.ShellExecuteW")
    def test_request_admin_when_not_admin(self, mock_shell_exec, mock_is_admin):
        """测试请求管理员权限(当前无权限)"""
        mock_is_admin.return_value = False
        mock_shell_exec.return_value = 1

        result = AdminUtils.request_admin()
        assert result is True
        mock_shell_exec.assert_called_once()

    @patch("monitormaestro.utils.admin_utils.AdminUtils.is_admin")
    def test_request_admin_when_already_admin(self, mock_is_admin):
        """测试请求管理员权限(当前已有权限)"""
        mock_is_admin.return_value = True

        result = AdminUtils.request_admin()
        assert result is False
