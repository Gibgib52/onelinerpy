# this program takes input.py and makes it into a one line exec()
# does not support docstrings.

# open as read
with open("input.py", "r") as f:
    lst = f.read().split("\n") # split fileint list, on linebreaks
    for item in lst:
        item.replace("\n", "")

# write to output
with open("output.py", "w") as f:
    # turn list to string
    out = ""
    for item in lst:
        out += f"{item}\\n"

    # wrap in an exec()
    out = f'exec("""{out}""")'

    f.write(out)
    print("Output saved to output.py")