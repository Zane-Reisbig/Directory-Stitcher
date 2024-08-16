from time import time
from lib.TKinter_Wrapper import dir_name_picker
from os import walk
from os.path import join, basename

extension = input("Extension: ('.py')\n('.py', '.js') > ")
if extension == "":
    extension = ".py"
comment_syntax = input("Comment Syntax: ('# <CONTENTS>')\n('# ', '//') > ")
if comment_syntax == "":
    comment_syntax = "# "

in_dir = dir_name_picker("FOLDER")

all_files = [
    join(dp, f)
    for dp, _, fn in walk(in_dir)
    for f in fn
    if (basename(f).endswith(extension))
]
now = time()
with open(f"out{extension}", "w") as master:
    print("WORKING ON: ")

    for file in all_files:
        print(f"\t{file}")

        with open(file) as cur:
            master.write(f"{comment_syntax}START_FILE: '{file}'")
            master.write(cur.read())
            master.write(f"\n{comment_syntax}EOF: '{file}'")
            master.write("\n")

time_took = time() - now
print(f"Done in {time_took:.2} seconds...")
