import ctypes
import sys


class AdminUtils:
    """Windows系统管理员权限工具类"""

    @staticmethod
    def is_admin():
        """检查当前是否以管理员权限运行"""
        try:
            return bool(ctypes.windll.shell32.IsUserAnAdmin())
        except:
            return False

    @staticmethod
    def request_admin():
        """请求以管理员权限重新运行程序"""
        try:
            if not AdminUtils.is_admin():
                ctypes.windll.shell32.ShellExecuteW(
                    None, "runas", sys.executable, __file__, None, 1
                )
                return True
            return False
        except:
            return False
