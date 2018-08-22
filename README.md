Display Brightness
=================

Adjust your display's brightness with Alfred

![Display Brightness Screenshot](https://raw.github.com/fniephaus/alfred-brightness/master/screenshot.png)

This workflow uses a modified version of [screenbrightness](https://github.com/jmstacey/screenbrightness).

---

## Configuration Options

There are a number of options that can be changed through workflow variables.
[Click here for instructions on changing workflow variables.](https://www.alfredapp.com/help/workflows/advanced/variables/#getting-started)

### Brightness Levels

* Variable: `brightness_levels`
* Format: Comma-separated list of numbers between 0 and 100
* Default: `0,20,40,60,80,100`
* Examples:
    * `0,25,75,100`
    * `0,50,100`

### Minimum/Maximum Brightness

Keywords that you want to use to set your brightness to the minimum or maximum value (e.g. `brightness min`)

* Variables: `keyword_min` and `keyword_max`
* Format: String
* Defaults: `min` and `max`
* Examples:
    * `low` and `high`
    * `dim` and `bright`

Minimum and maximum brightness values

* Variables: `value_min` and `value_max`
* Format: Number between 0 and 100
* Defaults: `0` and `100`
* Examples:
    * `0` and `100` _(`0` turns the screen completely off)_
    * `2` and `100` _(`2` is the lowest visible MacBook brightness)_

Show minimum and maximum options?
You can show the minimum option, maximum option, or both.

* Variables: `show_min` and `show_max`
* Format: String; `true` or `false`
* Defaults: both `false`
* Examples:
    * Show both: `true` and `true`
    * Show only minimum: `true` and `false`
    * Show only maximum: `false` and `true`
