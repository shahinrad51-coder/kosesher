[app]
# عنوان اپلیکیشن
title = My OMP App
# نام پکیج (به صورت انگلیسی و بدون فاصله)
package.name = ompapp
package.domain = org.test
# مسیر اصلی سورس کد (همان نقطه‌ای که باعث خطای قبلی شده بود)
source.dir = .
# فایل‌هایی که باید در APK قرار بگیرند
source.include_exts = py,png,jpg,kv,atlas
# ورژن اپلیکیشن
version = 0.1
# پیش‌نیازهای پایتونی (حتماً requests و kivy باشند)
requirements = python3,kivy,requests

# دسترسی‌های مورد نیاز اندروید
android.permissions = INTERNET

# تنظیمات نسخه اندروید برای پایداری در بیلد
android.api = 33
android.minapi = 21
android.sdk = 24
android.ndk = 25b
android.arch = armeabi-v7a

[buildozer]
# تنظیمات لاگ برای اینکه اگر موقع بیلد خطایی داد، دقیقاً بفهمیم کجاست
log_level = 2
warn_on_root = 1
