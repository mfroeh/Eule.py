# Eule.py

A Diablo III Macro Collection.\
Working with all 16:9 Resolutions guaranteed.\
Should work on any Resolution (not tested).

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

I prefer this Version of sending Messages over a simple Hotkey Version due to having to remember less Hotkeys.

## Third Party Launcher

* Launches your Third Party Tools.
* Upon first Startup select the paths to your Tools.

## Auto Stuff

* Automates some of the Macros using Image Recognition.
* Check at the Bottom if it is working for your Resolution.

This Feature is _VERY_ suboptimal right now, as it is using AHK to capture the Screen.\
I am sadly forced to that compromise, due to Python Image Librarys beeing extremely large when compiled (Current exe with better Image Recognition would be 6x the Size).

### Limitations
Image Recognition with AHK requires a basicly pixel perfect match to recognise an Image, which means that, in Order to work with a certain Resolution, you first have to take screenshot of the image to be recognised in that Resolution .\
Upscaling Images also does not work.\
If you want your Resolution to be supported, sent me Screenshots of the Events.

For working Resolutions there also cannot be Image Recognition of inactive Windows => No Image Recognition inside Rift when using TurboHUD.

## Macro Explanations

#### Spam Right / Left Click

Spam Clicks the Right / Left Mousebutton.

#### Normalize Difficulty

Sets the Game Difficulty to normal.

#### Swap Armor

Swaps your equipped Items with Items from your Inventory.\
![](https://i.ibb.co/YQ5KNX8/swap-armor.png)\
BountyDH swaps the Items in the orange, Cains the ones in the blue rectangle.

#### Pause Eule

Stops any Hotkey or Screen Listeners.

#### Port to Ax Town

Ports to Town of Act x.

#### Port to Pool

Ports to the next Poolspot from the Poolspots List (Settings).

#### Open Grift

Opens a Greater Rift from when you have clicked the Obelisk.

#### Upgrade Gem

Upgrades the Gem in the top left Spot.\
Set the amount of Upgrades to do before porting to town with the Empowered option.

#### Leave Game

Leaves the Game.

#### Salvage / Drop Inventory

Salvages or Drops the Items from your Inventory.\
Spares x Columns looking from the left of the Inventory.
![](https://i.ibb.co/BfdL0kC/spare-columns.png)\
Spare Columns = 0: Salvages the entire Inventory - including the Blue Column\
Spare Columns = 1: Salvages everything besides the Blue Column\
and so on

#### Gamble

Gambles the Itemtype specified in Settings.

#### Convert 1/2-Slot

Converts all the Items in your Inventory whilst taking vertical steps the size of 1/2 Inventory slots.\
E.g. use 1-Slot for Rings and 2-Slot for Gloves.\
The SoL Option does two converting rotations in less time than a non SoL convert takes for one Rotation.

#### Reforge / Convert Set

Reforges or Converts the Item in the top left corner.

## Image Recognition Checklist

| Feature           |      1920x1080      |           2715x1527            | others |
| :---------------- | :-----------------: | :----------------------------: | :----: |
| Start Game        |      &#10003;       |            &#10003;            |        |
| Open Rift / Grift |      &#10003;       |      &#10003; (untested)       |        |
| Accept Grift      | &#10003; (untested) |                                |        |
| Upgrade Gem       |      &#10003;       |        
| Gamble            |      &#10003;       |      &#10003; (untested)
