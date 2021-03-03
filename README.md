# renpy_logger

A simple utility for capturing stdout/stderr in various Ren'Py games,
especially in environments where this is hard (looking at you, Windows).

Assumes your gamedir is writable, which might not be the case on certain
platforms (especially mobile). Let me know if this is an issue.

To use, make a ZIP file containing only `autorun.py` (in the root), rename it
to have an `.rpe` extension, and drop into the gamedir. The script will write
`output.txt` in the gamedir, after rotating any old `output.txt` to
`output.NUM.txt`, where NUM is an integer starting at 0 and incremented up to
99, using the first name that doesn't exist. If all of those exist, the old
`output.txt` is deleted.

(The `Makefile` in the root creates the above archive automatically. Check the
releases page of this [repository on GitHub][gh] for a prebuilt artifact that can be
downloaded and dropped in.)

As a developer, if you encounter a crash in early Ren'Py, ask your users to
install this and capture `output.txt` (and possibly the latest few numbered
outputs).

This extension was expressly developed for _Angels with Scaly Wings_, but
should work in any Ren'Py engine, and was written with forward-compatibilty in
mind.

As usual, if you have any comments, questions, faint praise, or free beer, feel
free to open an issue or PR on the [original GitHub repository][gh].

[gh]: https://github.com/Grissess/renpy_logger
