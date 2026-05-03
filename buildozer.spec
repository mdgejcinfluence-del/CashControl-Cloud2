[app]
title = CashControl
package.name = cashcontrol
package.domain = org.mdgejc
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# IMPORTANT : Ces dépendances sont nécessaires pour votre sécurité AES et vos appels API
requirements = python3,kivy,cryptography,requests,urllib3,certifi,idna,chardet

orientation = portrait
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a
android.api = 31
android.minapi = 21

[buildozer]
log_level = 2
warn_on_root = 1
