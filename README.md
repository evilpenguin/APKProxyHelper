# APKProxyHelper
APKProxyHelper paches an apk for proxying.

Usage
----------
```
$ python3 aph.py -h               
usage: APKProxyHelper [-h] --apk APK [--apktool APKTOOL]

optional arguments:
  -h, --help            show this help message and exit
  --apk APK, -a APK     The path to the apk file
  --apktool APKTOOL, -atv APKTOOL
                        apktool version 2.4.1 or 2.5.0
```

Output
----------
```
$ python3 aph.py -a apk.apk
[*] Decompiling apk.apk
.....
[*] Adding network file to apk/res/xml
[*] Updating manifest at apk/AndroidManifest.xml
[*] Repackaging to apk_proxy.apk
......
[*] Re-signing apk apk_proxy.apk
.....
[*] Cleaing up directory apk
```

Manual Resign
----------
- `keytool -genkey -v -keystore debug.keystore -storepass android -alias androiddebugkey -keypass android -keyalg RSA -keysize 2048 -validity 10000`
- `jarsigner -verbose -keystore debug.keystore -storepass android -keypass android *.apk androiddebugkey`
