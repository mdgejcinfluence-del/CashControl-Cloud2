[app]
# (section) Nom de ton application
title = CashControl
package.name = cashcontrol
package.domain = org.mdgejc

# (section) Où se trouve le code (le point signifie "ici")
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

# (section) Les outils dont ton application a besoin
# On inclut cryptography pour ta sécurité AES et requests pour le cloud
requirements = python3,kivy,cryptography,requests,urllib3,certifi,idna,chardet

orientation = portrait
fullscreen = 0

# (section) Android spécifique
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
android.api = 31
android.minapi = 21

[buildozer]
log_level = 2
warn_on_root = 1
