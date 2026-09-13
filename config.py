# -*- coding: utf-8 -*-
"""
config.py
---------
تنظیمات ساده پروژه — همه از Environment Variable خوانده می‌شوند
تا هیچ مقدار حساسی داخل کد هاردکد نشود.
"""

import os

# اسمی که به‌عنوان نام سشن به Client داده می‌شود (فقط یک برچسب داخلی است)
SESSION_LABEL = os.environ.get("SESSION_LABEL", "idbot_session")
