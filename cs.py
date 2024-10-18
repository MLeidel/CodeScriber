'''
cs.py CodeScriber Code Editor
Hak-able Desktop Code Editor
Oct 2024 Michael Leidel
'''

import webview
import sys, os
import markdown
import tkinter as tk
import iniproc
import subprocess
from tkinter.ttk import *
from tkinter import filedialog
from ttkthemes import ThemedTk

p = os.path.realpath(__file__)
p = os.path.dirname(p) + "/"
# os.chdir(os.path.dirname(p))
optionsFileName = p+"options.ini"
lastFileName = p+"lastfile"
wingeo = p+"wingeo"

opts = []
opts = iniproc.read(optionsFileName,'width',
                                   'height',
                                   'terminal',
                                   'filemanager',
                                   'python',
                                   'browser',
                                   'startdir',
                                   'csnips')

current_file = ""  # tracks current file in use
current_path = opts[6]  # tracks path

# UNCOMMENT THIS FUNCTION TO WORK ON DUAL MONITORS (there is more)
def window_coord():
    px = window.x
    py = window.y
    geo = f"20x20+{px}+{py}" # keep tkinter on left screen
    return geo

def find_file(filename, search_path):
    ''' finds full-path of a file on Linux system '''
    for root, dirs, files in os.walk(search_path):
        if filename in files:
            return os.path.join(root, filename)
    return None

def mdToHTML():
    with open(current_file, 'r') as file:
        htmlText = markdown.markdown(file.read())
    htmlFile = current_file[:-3] + ".html"
    # open in default browser
    with open(htmlFile, 'w') as file:
        file.write(htmlText)

'''
            connections to/from the HTML/Javascript
'''
class Api:

    def onClose(self):
        ''' immediate close no ask '''
        # save last file name
        with open(lastFileName, "w") as fout:
            fout.write(current_file)
        # save last window dimensions
        with open(wingeo, "w")as fout:
            fout.write(str(window.x) + "|"
                       + str(window.y) + "|"
                       + str(window.width) + "|"
                       + str(window.height))
        # exit app
        window.destroy()

    def getFileName(self):
        global current_file
        return current_file

    def open_file(self):
        ''' called from javascript '''
        global current_file, current_path
        root = ThemedTk(theme="black")  # COMMENT IF USING SINGLE MONITOR SYSTEM
        root.configure(bg="dimgray")  # COMMENT IF USING SINGLE MONITOR SYSTEM
        #root = tk.Tk()  # COMMENT IF USING SINGLE MONITOR SYSTEM
        root.geometry(window_coord())  # COMMENT IF USING SINGLE MONITOR SYSTEM
        file_path = filedialog.askopenfilename(initialdir=current_path,
                                               initialfile=os.path.basename(current_file),
                                               title="Open file",
                                               filetypes=(("all files", "*"),
                                                         ("Python", "*.py"),
                                                         ("C", "*.c"),
                                                         ("h", "*.h"),
                                                         ("HTML", "*.html"),
                                                         ("CSS", "*.css")))
        root.destroy()  # COMMENT IF USING SINGLE MONITOR SYSTEM
        if file_path:
            current_file = file_path
            current_path = os.path.dirname(file_path)
        else:
            return ''

        if file_path:
            with open(current_file, 'r') as file:
                return file.read()
        return ''

    def save_file(self, content):
        ''' called from javascript '''
        global current_file, current_path
        # root = tk.Tk()  # COMMENT IF USING SINGLE MONITOR SYSTEM
        root = ThemedTk(theme="black")  # COMMENT IF USING SINGLE MONITOR SYSTEM
        root.configure(bg="dimgray")  # COMMENT IF USING SINGLE MONITOR SYSTEM
        root.geometry(window_coord())  # COMMENT IF USING SINGLE MONITOR SYSTEM
        file_path = filedialog.asksaveasfilename(initialdir=current_path,
                                                 defaultextension=".txt",
                                                 initialfile=os.path.basename(current_file),
                                                 filetypes=(("all files", "*"),
                                                            ("Python", "*.py"),
                                                            ("C", "*.c"),
                                                            ("h", "*.h"),
                                                            ("Javascript", "*.js"),
                                                            ("HTML", "*.html"),
                                                            ("CSS", "*.css")))
        root.destroy()  # remove if single monitor
        if file_path:
            current_file = file_path
            current_path = os.path.dirname(file_path)
            if current_file.endswith(".md"):
                mdToHTML()
        else:
            return ''

        if file_path:
            with open(file_path, 'w') as file:
                file.write(content)
            return current_file
        else:
            return ''

    def quick_save_file(self, content):
        global current_file, current_path
        with open(current_file, 'w') as file:
            file.write(content)
        if current_file.endswith(".md"):
            mdToHTML()
        return current_file

    def getCmdFile(self):
        ''' Get the starting file from command line '''
        global current_file, current_path
        if current_file:
            with open(current_file, 'r') as file:
                return file.read()
        return ''

    def execPython(self):
        global current_file, current_path
        os.system(opts[4] + " " + current_file)

    def execMarkdown(self):
        global current_file, current_path
        if not current_file.endswith(".md"):
            return
        # change to .html file
        htmlFile = current_file[:-3] + ".html"
        # open in default browser
        subprocess.call([opts[5], htmlFile])

    def execWebbrowser(self):
        global current_file, current_path
        subprocess.call([opts[5], current_file])

    def execFileMgr(self):
        global current_file, current_path
        os.system(opts[3] + " " + current_path)

    def execTerminal(self):
        global current_file, current_path
        print(opts[2] + current_path)
        os.system(opts[2] + "=" +current_path)

    def on_file_drop(self, file_name):
        global current_file, current_path
        current_file = find_file(file_name, "/home/")
        print(f"file file: {current_file}")
        current_path =  os.path.dirname(current_file)
        print(f"file path: {current_path}")
        if current_file:
            with open(current_file, 'r') as file:
                return file.read()
        else:
            return ''

    def execCSnips(self):
        subprocess.call(["python3", opts[7]])

#  END OF JS_API CLASS  END OF JS_API CLASS  END OF JS_API CLASS

if __name__ == '__main__':
    api = Api()

    win = [100,100,800,600] # initialize geo: left,top,width,height

    '''
    The following opens a file from the command line
    or by default the last file used at shut down.
    '''
    if len(sys.argv) > 1:
        current_file = sys.argv[1]
        current_path = os.path.realpath(current_file)
        #current_path =  os.path.dirname(sys.argv[1])
    else:
        if os.path.isfile(lastFileName):
            with open(lastFileName, 'r') as file:
                current_file = file.readline().strip()
                current_path =  os.path.dirname(current_file)

    if os.path.isfile(wingeo):
        with open(wingeo) as file:
            geo = file.read().strip()
        win = geo.split('|')  # 0 left, 1 top, 2 width, 3 height
        win = [int(i) for i in win]  # make integers

    window = webview.create_window('CodeScriber Code Editor',
                     url='cs.html', x=win[0], y=win[1],
                     width=win[2],
                     height=win[3],
                     js_api=api)

    webview.start()
