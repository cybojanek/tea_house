# Tea house desktop backgrounds

### What does this do?
Constructs a series of desktop backgrounds based on the Gmail Tea House theme. Also includes a script to update the background throughout the day.

### How?

* Run **get_files.sh** to download the image sources.

* Run **make.py** with a given width/height (height should be at least 940 to be pretty)

* To automatically cycle between backgrounds, add **background.py** to your crontab, every 15 minutes or so.

### Requirements

* Python PIL

