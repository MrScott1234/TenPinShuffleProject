# Welcome to the 10 Pin Shuffle Project!

![Bowling Icon@2x](https://user-images.githubusercontent.com/97776260/149610169-6ff8bb38-a2e8-406c-8827-28f94df16d72.png)

### About

10 Pin Shuffle is a popular mobile bowling game developed by Digital Smoke.
I gained a bit of interest in beefing up the graphics and textures in the game to fit modern standards, so I decided to start this project in order to document and develop modding tools for this decades old mobile game.

###### Note: This is not documentation about gameplay, strategies, bugs, or the like. This documentation is strictly technical for the purposes of modding and understanding the technology used by the game.

### Quick Start

To get started you'll need to grab the .APK file for 10 Pin Shuffle and extract the contents into a folder somewhere on your computer.
This can be done quite easily with any off the shelf .APK extractor app on the Google Play store and a USB cable to transfer the file.

# Assets and File Documentation

###### DISCLAIMER: This is all speculation on my part purely based on educated guesses and is subject to change.

### The Basics

All of 10 Pin Shuffle's assets are located in the "assets" folder of the extracted source files.

![image](https://user-images.githubusercontent.com/97776260/149610299-9cb0b07b-0fcd-45d4-b249-cd77c98c90c5.png)

The assets themselves are quite small in size, amounting to a total of only 26.4 MB.

### Texture Files

Texture files are very convienently stored as simple PNG and JPG files at quite low resolutions.

![image](https://user-images.githubusercontent.com/97776260/149610441-7064d8bb-da35-4d6f-8742-267f0c385ac6.png)

###### TODO: Figure out where some textures are stored, as I cannot find where the brick or ground wood texture is located

### Sound Files

Similar to the textures, sounds are stored as .WAV files.

![image](https://user-images.githubusercontent.com/97776260/149610872-f3581737-2304-46ab-9535-80ec339dcc17.png)


### .S3E Files

In 10 Pin Shuffle and all apps made with the Marmalade SDK, a .S3E file exists. This is where I suspect all of the game code / logic is stored.

![image](https://user-images.githubusercontent.com/97776260/149611019-01e309c6-322f-4763-a419-e588e59b6a63.png)

### .DSFNT Files

These files are the game's fonts.

![image](https://user-images.githubusercontent.com/97776260/149611099-06b95fa2-fa33-46e7-a26d-260b2bb1aec1.png)

### .DSSTR Files

These files are responsible for language localization.

![image](https://user-images.githubusercontent.com/97776260/149611183-b00a95f5-d314-49f7-bd65-052e8e314cc9.png)


# Game Tutorial Files

10 Pin Shuffle stores the tutorials in separate html files for each language, and simply picks the one it needs based on the language and specific tutorial the player wants to read.

![image](https://user-images.githubusercontent.com/97776260/149611253-a8e66592-9ec0-4da8-ac37-6a699acdc839.png)

Opening any of these files in a web browser will greet you with an unstyled web page, as the game appears to style the content itself.

![image](https://user-images.githubusercontent.com/97776260/149611283-e68f8f83-c9d2-4c23-9df7-140b8237a654.png)



# Currently Undocumented File Formats

### .16k, .16l, .16p, .16p2x Files

Judging by the names of the files, I suspect these files are responsible for handling different UI layouts / sizes for different devices.
However, I'm not 100% sure, so I consider it undocumented.

![image](https://user-images.githubusercontent.com/97776260/149611069-7c863ff3-e05b-4a4a-ba39-827d6691c186.png)

### .DSMDL Files

I suspect these files contain geometry and material properties for the 3D objects in the game, but I do not yet know how these files are structured and how they actually store this data.

![image](https://user-images.githubusercontent.com/97776260/149611136-920d8bed-164a-43c3-9b61-89a7cc0ff472.png)

