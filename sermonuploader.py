# Copyright (C) 2017 Simon Biggs
# This program is free software: you can redistribute it and/or
# modify it under the terms of the GNU Affero General Public
# License as published by the Free Software Foundation, either
# version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Affero General Public License for more details.
# You should have received a copy of the GNU Affero General Public
# License along with this program. If not, see
# http://www.gnu.org/licenses/.

"""SermonUploader"""

import os
import tkinter as tk
from  tkinter import filedialog

def browsefunc(string_var):
    directory = filedialog.askdirectory()
    string_var.set(directory)


def read_persistent_file(root, filename):
    string_var = tk.StringVar(root, value="")

    if os.path.exists(filename):
        with open(filename, 'r') as file:
            string_var.set(file.read())

    return string_var

def save_persistent_file(entry, filename):
    with open(filename, 'w') as file:
        file.write(entry.get())

def initial_prompt():
    """Prompt user for relevant passwords and the directory to watch."""
    results = {}

    root = tk.Tk()

    root.wm_title("Sermon Uploader")
    
    label_intro = tk.Label(
        root, 
        text="Please provide the directory where sermons will be placed:")
    label_intro.grid(row=0, column=0, columnspan=4, padx=10, pady=(10,5))

    persistent_filenames = {
       "directory": "directory_to_watch.txt",
       "archiveorg": "archiveorg_username.txt",
       "wordpress": "wordpress_username.txt"
    }

    string_vars = {
        key: read_persistent_file(root, item)
        for key, item in persistent_filenames.items()
    }

    widths = {
       "directory": 40,
       "archiveorg": 15,
       "wordpress": 15
    }

    persistent_entries = {
        key: tk.Entry(root, textvariable=item, width=widths[key])
        for key, item in string_vars.items()
    }
    persistent_entries['directory'].grid(row=1, column=0, columnspan=3, padx=20)
    persistent_entries['archiveorg'].grid(row=3, column=1, padx=10)
    persistent_entries['wordpress'].grid(row=3, column=3, padx=10)

    button_browse = tk.Button(root, text="Browse", command= lambda: browsefunc(string_vars['directory']))
    button_browse.grid(row=1, column=3)

    label_details = [
        tk.Label(root, text="Please provide {} details:".format(item))
        for item in ["archive.org", "wordpress"]]
    label_details[0].grid(row=2, column=0, columnspan=2, pady=10)
    label_details[1].grid(row=2, column=2, columnspan=2, pady=10)

    label_username = [
        tk.Label(root, text="Username:")
        for _ in range(2)]
    label_username[0].grid(row=3, column=0)
    label_username[1].grid(row=3, column=2)

    label_password = [
        tk.Label(root, text="Password:")
        for _ in range(2)]
    label_password[0].grid(row=4, column=0)
    label_password[1].grid(row=4, column=2)

    def complete(event=None):
        for key, filename in persistent_filenames.items():
            save_persistent_file(persistent_entries[key], filename)

        
        
        root.destroy()

    button = tk.Button(root, text="Begin watching", command=complete)
    button.grid(row=7, column=3)

    persistent_entries['directory'].focus()
    
    root.mainloop()


def main():
    initial_prompt()

if __name__ == "__main__":
    main()
