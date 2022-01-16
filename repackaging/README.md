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

###### NOTE: You will need to install JDK 14.0.2 to get the jarsigner application needed to sign the APK

In the repackaging folder, edit the "sign.bat" file; as we will need to make some changes to make it work.

```markdown
cd DIRECTORY_HERE
"C:\Program Files\Java\jdk-14.0.2\bin\jarsigner" -verbose -keystore my-release-key.keystore "10_Pin_Shuffle_base.apk" alias_name
```

Specifically, we will need to change the DIRECTORY_HERE to be the folder that the APK is located in.

###### NOTE: If you installed the JDK in a different location, you will need to change the location in the .bat file.

After that, simply double click the file to sign it.
You will be prompted to enter the keystore's password to continue.
I've set the provided keystore password to "password".

If you're using your own keystore, you will have to change the keystore file name and the alias_name in the .bat file.

### Step 4: Finished!

Congrats! You've packaged the game successfully. Now just put it back onto an Android device and install it.
###### NOTE: You may need to adjust your security settings to allow the app to install
