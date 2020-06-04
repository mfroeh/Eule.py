# Eule.py

A Diablo III Macro Collection.\
Working with all 16:9 Resolutions guaranteed.\
Use in Fullscreen (Windowed) for Auto Features.\
Should also work on any Resolution (not tested).

There are two different Versions. The difference between them beeing Image Recognition.\
Check below at __Auto Stuff__ to see the differences.

## Macros

All Macros are sent directly to Diablo III without using your physical mouse or keyboard.\
This has numerous advantages, such as

* Faster Macro execution time
* Reliability
* Working without Diablo III beeing in the foreground

## Setting Hotkeys

To set a Hotkey

1. Click the Button next to the Label of the Hotkey you would like to set
2. Press the combination of keys you would like to use
3. Accept the new Combination

You may cancel setting a Hotkey by pressing __Escape__.\
You may delete a Hotkey by clicking and pressing __Delete__.

## Abbrevations

* Replaces Abbrevations with full sentences.
* To use an added Abbrevation, type it in the chat and then tap __space__ once.

[Video](https://www.youtube.com/watch?v=iwmcFQ65hb0)\
I prefer this Version of sending Messages over a simple Hotkey Version due to having to remember less Hotkeys.

## Third Party Launcher

* Launches your Third Party Tools.
* Upon first Startup select the paths to your Tools.
* You will have to reconfigure pHelper at first use.
* Start Eule.py as Admin to not have to accept the Popups.

[Video](https://www.youtube.com/watch?v=yIaNNIQuIOY)

## Auto Stuff

* Automates some of the Macros using Image Recognition.
* Requires Diablo to be in Windowed (Fullscreen) Mode
* Check at the Bottom if it is working for your Resolution.

[Video](https://www.youtube.com/watch?v=mjKnKkUijIk)

There are two different Versions.

Regular Version (Eule.py):
* Everything works with TurboHUD enabled.
* More performant once started.
* Bigger Size => Longer Startup (depending on your Hardware).

AHK Image Recognition Version (Eule.py (AHK)):
* Uses AHK for Image Recognition.
* Only Auto Start Game works with TurboHUD enabled.
* Smaller Size => Shorter Startup.

The Size of the regular Version sadly is more or less staying the way it is.\
This is the case due to Python Image Librarys beeing extremely large when compiled.\
If you're willing to put up with potentially "long" Startup, the performance afterwards will be better.

## Macro Explanations

#### Spam Right / Left Click

Spam Clicks the Right / Left Mousebutton.\
[Video](https://www.youtube.com/watch?v=Dy1rWLSG2VY)

#### Normalize Difficulty

Sets the Game Difficulty to normal.\
[Video](https://www.youtube.com/watch?v=zOXCv5Dp7b0)

#### Swap Armor

Swaps your equipped Items with Items from your Inventory.\
[Video](https://www.youtube.com/watch?v=dM50BkYp81M)\

#### Pause Eule

Stops any Hotkey or Screen Listeners.\
[Video](https://www.youtube.com/watch?v=Rp9x4hEfUi8)

#### Port to Ax Town

Ports to the Town of Act x.

#### Port to Pool

Ports to the next Poolspot from the Poolspots List (Settings).\
[Video](https://www.youtube.com/watch?v=KfkVtLCQiNo)

#### Open Grift

Opens a Greater Rift from when you have clicked the Obelisk.\
[Video](https://www.youtube.com/watch?v=-PjyOAo1a0I)

#### Upgrade Gem

Upgrades the Gem in the top left Spot.\
[Video](https://www.youtube.com/watch?v=b7HS-NXbUus)\
Set the amount of Upgrades to do before porting to town with the Empowered option.

#### Leave Game

Leaves the Game.\
[Video](https://www.youtube.com/watch?v=1SfbbTvYITY)


#### Salvage / Drop Inventory

Salvages or Drops the Items from your Inventory.\
[Video](https://www.youtube.com/watch?v=q5NzPwmcIP4)\
Spares x Columns looking from the left of the Inventory.
![](https://i.ibb.co/BfdL0kC/spare-columns.png)\
Spare Columns = 0: Salvages the entire Inventory - including the Blue Column\
Spare Columns = 1: Salvages everything besides the Blue Column\
and so on

#### Gamble

Gambles the Itemtype specified in Settings.\
[Video](https://www.youtube.com/watch?v=NJsJpJb3Fas)

#### Convert 1/2-Slot

Converts all the Items in your Inventory whilst taking vertical steps the size of 1/2 Inventory slots.\
E.g. use 1-Slot for Rings and 2-Slot for Gloves.\
The SoL Option does two converting rotations in less time than a non SoL convert takes for one Rotation.

#### Reforge / Convert Set

Reforges or Converts the Item in the top left corner.\
[Video](https://www.youtube.com/watch?v=B3Z23ZkxH4M)

## Image Recognition Checklist

| Feature           | 1920x1080 |      2715x1527      |  3840x2160  |
| ----------------- | :-------: | :-----------------: | :------: |
| Start Game        | &#10003;  |      &#10003;       | &#10003;  (untested)|
| Open Rift / Grift | &#10003;  |      &#10003;       | &#10003;  (untested)|
| Accept Grift      | &#10003;  | &#10003; (untested) |          |
| Upgrade Gem       | &#10003;  |      &#10003;  (untested)      | &#10003;  (untested)|
| Gamble            | &#10003;  |      &#10003;       | &#10003;  (untested)|
