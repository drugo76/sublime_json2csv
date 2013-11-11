# Sublime Text 2 Plugin: JSON to CSV Converter

A Sublime Text 2 plugin to generate a csv from json.  
It works both on the entire file and on single or multiple selections (if the input is a valid JSON).

The source JSON should contain only one nesting level (at least for now...).

Standalone version available here: [https://github.com/drugo76/json2csv](https://github.com/drugo76/json2csv)

## Installation

- Plugin requires simplejson python library. Can be found at [https://github.com/simplejson/simplejson](https://github.com/simplejson/simplejson).

- Install this plugin via [Package Control](http://wbond.net/sublime_packages/package_control)

- Otherwise clone this repository inside the Sublime Text 2 Packages folder.  
```` bash
git clone https://github.com/drugo76/sublime_json2csv.git "json2csv"
````
To get the path to the Packages folder go to `Preferences -> Browse Packages`.

## Usage

Having a valid JSON (or a valid JSON selection) in the active view, from the menu choose `Tools -> Command Palette`, start typing 'csv' and select the `Json2Csv: Convert JSON to CSV` item.

## Future Improvements

- Filter the columns to be added in csv
