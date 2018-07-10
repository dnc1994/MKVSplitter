MKVSplitter
=========
MKVSplitter is a small script, which harnesses ffprobe and ffmpeg to automatically parse chapter information of a given MKV file (for instances, videos of live concerts) and split the file into pieces chapter by chapter, with filenames set correspondingly.

Usage
-----
Make sure that the script and the MKV file are in the same folder (also ffprobe.exe and ffmpeg.exe for Windows)
Then just run MKVSplitter.py

Author
------
Zhang Ling Hao, Fudan University.
Contact me: zlhdnc1994@gmail.com

Requirements
------------
Python 3 and ffmpeg

To-do list
----------
- Add selection to choose the chapters you wanted to export.
- Improve support for subtitles.
- Deal with illegitimate filenames.
- Fix issues about paths and introduce clean-up to make it tidier.
- (Maybe) Write a GUI.
