# Welcome to the 10 Pin Shuffle Project!

![Bowling Icon@2x](https://user-images.githubusercontent.com/97776260/149610169-6ff8bb38-a2e8-406c-8827-28f94df16d72.png)

## About

10 Pin Shuffle is a popular mobile bowling game developed by Digital Smoke.
I gained a bit of interest in beefing up the graphics and textures in the game to fit modern standards, so I decided to start this project in order to document and develop modding tools for this decades old mobile game.

###### Note: This is not documentation about gameplay, strategies, bugs, or the like. This documentation is strictly technical for the purposes of modding and understanding the technology used by the game.

## Quick Start

To get started you'll need to grab the .APK file for 10 Pin Shuffle and extract the contents into a folder somewhere on your computer.
This can be done quite easily with any off the shelf .APK extractor app on the Google Play store and a USB cable to transfer the file.

Once all of that is done, you'll simply need to extract the contents using a program like 7zip.

# Assets and File Documentation

###### DISCLAIMER: This is all speculation on my part purely based on educated guesses and is subject to change.

## The Basics

All of 10 Pin Shuffle's assets are located in the "assets" folder of the extracted source files.

![image](https://user-images.githubusercontent.com/97776260/149610299-9cb0b07b-0fcd-45d4-b249-cd77c98c90c5.png)

The assets themselves are quite small in size, amounting to a total of only 26.4 MB.

## Texture Files

Texture files are very convienently stored as simple PNG and JPG files at quite low resolutions.

![image](https://user-images.githubusercontent.com/97776260/149610441-7064d8bb-da35-4d6f-8742-267f0c385ac6.png)

###### NOTE: This does not include textures used for the 3D objects, as those are embedded in the 3D asset files directly.

## Sound Files

Similar to the textures, sounds are stored as .WAV files at a 22khz sample-rate.

![image](https://user-images.githubusercontent.com/97776260/149610872-f3581737-2304-46ab-9535-80ec339dcc17.png)


## .S3E Files

In 10 Pin Shuffle and all apps made with the Marmalade SDK, a .S3E file exists. This is where I suspect all of the game code / logic is stored.

![image](https://user-images.githubusercontent.com/97776260/149611019-01e309c6-322f-4763-a419-e588e59b6a63.png)

## .DSFNT Files

These files are the game's fonts.

![image](https://user-images.githubusercontent.com/97776260/149611099-06b95fa2-fa33-46e7-a26d-260b2bb1aec1.png)

## .DSSTR Files

These files are responsible for language localization.

![image](https://user-images.githubusercontent.com/97776260/149611183-b00a95f5-d314-49f7-bd65-052e8e314cc9.png)


## Game Tutorial Files

10 Pin Shuffle stores the tutorials in separate html files for each language, and simply picks the one it needs based on the language and specific tutorial the player wants to read.

![image](https://user-images.githubusercontent.com/97776260/149611253-a8e66592-9ec0-4da8-ac37-6a699acdc839.png)

Taking a look at any of these files in a web browser will greet you with an unstyled web page. 
Opening the instructions in the game will look identical, as it appears the game actually opens a web browser in-game.

![image](https://user-images.githubusercontent.com/97776260/149611283-e68f8f83-c9d2-4c23-9df7-140b8237a654.png)



# Currently Undocumented or Partially Documented File Formats

## .16k, .16l, .16p, .16p2x Files

Judging by the names of the files, I suspect these files are responsible for handling different UI layouts / sizes for different devices.
However, I'm not 100% sure, so I consider it undocumented.

![image](https://user-images.githubusercontent.com/97776260/149611069-7c863ff3-e05b-4a4a-ba39-827d6691c186.png)

## .DSMDL Model / Material Files

DSMDL files contain information about the 3d geometry, material properties, and textures all in one similar to a GLTF file.

![image](https://user-images.githubusercontent.com/97776260/149611136-920d8bed-164a-43c3-9b61-89a7cc0ff472.png)

The data in the file can be split up into several sections:

#### The Header

The header consists of the characters "DIGSMK3D....MTRX":

```markdown
44 49 47 53 4D 4B 33 44 00 00 00 00 4D 54 52 58  |  DIGSMK3D....MTRX  
```

#### Texture Data

Delimited by the 4 bytes "TXTR", the bytes after appear to contain texture data. 
What format the data is in and whether or not it is compressed is still unknown.

![image](https://user-images.githubusercontent.com/97776260/149614034-591c3e1d-cb46-49b7-b046-dd5184eb94af.png)

#### Material Data

Near the end of the file is where the material data is stored; marked by the 4 bytes "MTLS":

![image](https://user-images.githubusercontent.com/97776260/149614159-83348034-fa76-4770-a3ae-df16e9fabcda.png)

#### Polygon Data

Delimited by the 4 bytes "POLY", this is where the individual faces are; or more accurately which verticies they are attached to.

![image](https://user-images.githubusercontent.com/97776260/149614402-04eb9cd4-e6a5-463b-9b6c-ac31756c96c0.png)

#### Vertex Data

Delimited by the 4 bytes "NODE", this is where the vertex positions are located.

![image](https://user-images.githubusercontent.com/97776260/149614424-e570ab08-53b0-4ec0-bdbf-129b388c405a.png)


#### The END!

At the very end of the file there are a few extra bytes that mark the end:

```markdown
45 4E 44 21  |  END!
```


