#!/usr/bin/env python
import datetime
import subprocess
import os

SCRIPT = """/usr/bin/osascript<<END
tell application "Finder"
set desktop picture to POSIX file "%s"
end tell
END"""

TIMES = ["midnight", "2am", "4am", "6am", "8am", "10am", "noon", "2pm", "4pm",
         "6pm", "8pm", "10pm"]

if __name__ == '__main__':
    now = datetime.datetime.now()
    directory = os.path.dirname(os.path.realpath(__file__))
    if now.hour == 3 and now.minute >= 14:
        time = "314am"
    else:
         time = TIMES[now.hour/2]
    filename = "%s/teahouse_%s.jpg" % (directory, time)
    subprocess.Popen(SCRIPT % filename, shell=True)
