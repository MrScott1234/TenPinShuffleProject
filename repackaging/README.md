# Repackaging

After you've made all of the changes you'd like, you need to repackage all the game assets back into an .APK file.

### Step 1: Remove the META-INF file

First step is to make sure you delete the META-INF file from the source assets.
This is done to allow us to sign the .APK file later.

![image](https://user-images.githubusercontent.com/97776260/149640594-74241b1a-dd91-447c-9428-ee3459e9b034.png)

### Step 2: Run the python script

Firstly open up and run the python script.
You should be greeted with a window requesting a directory. This is what folder to package.
You should target the folder above the assets folder like so:

![image](https://user-images.githubusercontent.com/97776260/149640567-ee7816e8-f090-408d-b389-4d0154d4a285.png)

Next, you should be greeted with another window requesting a directory. This is where the apk file will be dumped.

### Step 3: Sign the .APK

By default, the .APK does not have a signature, and therefore will not work on any device.
To fix this, we will need to re-sign the .APK file, and it's why we deleted that META-INF file.

I won't go into too much detail here, but this guide outlines a very easy method of signing your own .APKs.

http://www.androiddevelopment.org/2009/01/19/signing-an-android-application-for-real-life-mobile-device-usage-installation/

### Step 4: Finished!

Congrats! You've packaged the game successfully. Now just put it back onto an Android device and install it.
###### NOTE: You may need to adjust your security settings to allow the app to install
