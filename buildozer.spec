[app]

# (str) Title of your application
title = Student Register

# (str) Package name
package.name = student_register

# (str) Package domain
package.domain = org.example

# (str) Source directory
source.dir = .

# (list) Source files for the application
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# Add your application dependencies here
requirements = python3,kivy

# (str) Version of your application
version = 0.1

# (str) Supported orientations (one of landscape, portrait, or sensorLandscape)
orientation = portrait

# (str) Android API to use
android.api = 31

# (str) Minimum API your APK will support
android.minapi = 21

# (int) Target API
android.target = 31

# (list) Permissions required for your app
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE

# (int) Android NDK API version (ensure it matches the NDK installed)
android.ndk_api = 21

# (str) Android SDK directory (ensure this is the correct path to your SDK)
android.sdk = /home/irobot/Android/Sdk

# (str) Android NDK version
android.ndk = 25b

# (bool) Whether to copy libraries instead of linking them
android.copy_libs = 1

# Uncomment and set the following if you are using a keystore for signing
# (str) Path to your keystore
# android.keystore = path/to/your.keystore

# (str) Key alias
# android.keyalias = your_keyalias

# (str) Key password
# android.keystore.password = your_keystore_password

# (str) Key alias password
# android.keyalias.password = your_keyalias_password

# (list) Additional Java .jar files to add to libs
# android.add_jars =

# (list) Application arguments passed to the python program
# (comma-separated, no spaces) Example: "arg1,arg2"
# arguments = 

# (bool) Indicate if the application should be fullscreen
fullscreen = 0
