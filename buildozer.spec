[app]
# (str) Title of your application
title = CashControl

# (str) Package name
package.name = cashcontrol

# (str) Package domain (needed for android packaging)
package.domain = org.mdgejc

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
# J'ai inclus toutes les dépendances nécessaires pour MDGEJ-C DIGITAL
# notamment pour la sécurité AES et les appels API
requirements = python3,kivy,cryptography,requests,urllib3,certifi,idna,chardet

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# ==================================
# Android specific configurations
# ==================================

# (list) Permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
# Nous utilisons la 31 pour garantir la stabilité sur GitHub
android.api = 31

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (list) The Android architectures to build for.
# TRÈS IMPORTANT : On ne garde que arm64-v8a pour éviter le crash "Broken Pipe" 
# dû au manque de mémoire sur GitHub Actions
android.archs = arm64-v8a

# (bool) Allow backup
android.allow_backup = True

# (str) Icon of the application
# icon.filename = %(source.dir)s/icon.png

# (str) Presplash of the application
# presplash.filename = %(source.dir)s/presplash.png

# ==================================
# Buildozer specific configurations
# ==================================

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
# Réglé sur 2 pour voir exactement où ça bloque si besoin
log_level = 2

# (int) Display warning if buildozer is run as root (0 = off, 1 = on)
warn_on_root = 1

# (str) Path to build artifact storage, cache and simple recipes
# build_dir = ./.buildozer

# (str) Path to bin directory where the APK will be stored
bin_dir = ./bin
