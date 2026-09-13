# -*- coding: utf-8 -*-
"""
session_loader.py
------------------
موقع استارت روی Railway (یا هر سروری)، این ماژول مقدار Environment Variable
با نام RUBIKA_SESSION را می‌خواند، base64-decode می‌کند و آن را به یک فایل
سشن واقعی (که rubpy می‌تواند مستقیم بخواندش) تبدیل می‌کند.
"""

import base64
import os

SESSION_ENV_VAR = "RUBIKA_SESSION"
SESSION_FILE_PATH = os.environ.get("SESSION_FILE_PATH", "/tmp/idbot_session")


def ensure_session_file() -> str:
    """
    فایل سشن را از متغیر محیطی بازسازی می‌کند (اگر از قبل روی دیسک نبود)
    و مسیر نهایی فایل سشن را برمی‌گرداند تا به rubpy.Client داده شود.
    """
    encoded = os.environ.get(SESSION_ENV_VAR)
    if not encoded:
        raise RuntimeError(
            f"متغیر محیطی {SESSION_ENV_VAR} تنظیم نشده است. "
            "ابتدا login.py را لوکال اجرا کن و مقدار خروجی را در Railway قرار بده."
        )

    raw = base64.b64decode(encoded)

    with open(SESSION_FILE_PATH, "wb") as f:
        f.write(raw)

    return SESSION_FILE_PATH
