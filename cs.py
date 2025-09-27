'''
cs.py CodeScriber Code Editor
Hak-able Desktop Code Editor
Oct 2024 Michael Leidel
https://github.com/MLeidel/CodeScriber
'''

import sys
import os
import glob
import time
import subprocess
import webbrowser
import platform
import shutil
from tkinter.ttk import *
from tkinter import filedialog
from tkinter import messagebox
from datetime import datetime
from ttkthemes import ThemedTk
from openai import OpenAI
from spellchecker import SpellChecker
import webview
import markdown
import iniproc

p = os.path.realpath(__file__)
p = os.path.dirname(p) + "/"
optionsFileName = p+"options.ini"
lastFileName = p+"lastfile"
tags = p+"tags.js"
wingeo = p+"wingeo"
spell = SpellChecker()

rec = []  # recent file list GLOBAL
srec = "" # csv string for javascript recent file list

opts = [] # storeing options from the options.ini file
opts = iniproc.read(optionsFileName,'ailog',
                                   'backup',
                                   'terminal',
                                   'filemanager',
                                   'previous',
                                   'browser',
                                   'scope',
                                   'run1',
                                   'run2',
                                   'run3',
                                   'run4',
                                   'nam1',
                                   'nam2',
                                   'nam3',
                                   'nam4',
                                   'theme',
                                   'openai',
                                   'model',
                                   'role')

current_file = ""  # tracks current file in use
current_path = opts[6]  # tracks path
myfpath = os.path.abspath(__file__)  # save this instance full path
myOS = platform.system()  # Linux or Windows
mypy = 'python3'  # for linux default

messages = []

# UNCOMMENT THIS FUNCTION TO WORK ON DUAL MONITORS (there is more)
def window_coord():
    ''' use this func when using multiple monitors '''
    px = window.x
    py = window.y
    geo = f"0x0+{px}+{py}" # keep tkinter on left screen
    return geo

def find_file(filename, search_path):
    ''' finds full-path of a file on Linux system '''
    for root, dirs, files in os.walk(search_path):
        if filename in files:
            return os.path.join(root, filename)
    return None

def mdToHTML():
    ''' convert MD file to HTML file '''
    with open(current_file, 'r', encoding='utf-8') as file:
        htmlText = markdown.markdown(file.read(), extensions=['tables', 'fenced_code'])
    htmlFile = current_file[:-3] + ".html"
    # open in default browser
    with open(htmlFile, 'w', encoding='utf-8') as file:
        file.write(htmlText)

#
#  Recent File Functions
#

def loadRecent():
    ''' open and read in the 'recent' text file containing recent file list '''
    global rec
    with open('recent', 'r', encoding='utf-8') as file:
        rec = file.readlines()
        rec = [item.rstrip('\n') for item in rec]

def saveRecent():
    ''' save the recent file list to 'recent' text file '''
    global srec
    n = len(rec)
    c = 0
    with open("recent", "w", encoding='utf-8') as file:
        srec = ""
        for item in rec:
            file.write(item + "\n")
            # also re-build csv string for javascript
            srec += item
            c += 1
            if c < n:
                srec += ","

def newRecent(item):
    ''' modify the recent file list '''
    global rec
    c = rec.count(item) # is item in the current list
    if c > 0:
        x = rec.index(item) # get the index of the item
        if x > 0:
            rec.remove(item)  # move the item up to the top of list
            rec.insert(0, item)
        else:
            pass #  already at top of list
    else:
        n = len(rec)          # put new item into to list
        if n > 8:             # keep the list to 9 or less items (COULD BE A VARIABLE)
            rec.pop(n-1)      # remove the bottom item (0 relative)
        rec.insert(0, item)   # put the new item at the top

def updateRecents(item):
    ''' update the recent file with next item ( open file )
        Every 'open file' performs this function '''
    if os.path.isfile("recent") is False:
        with open("recent", "w", encoding='utf-8') as fout:
            fout.write("options.ini\n")
    loadRecent()  # read in the recent file list
    if item != "":
        newRecent(item)  # put item at the top of list
    saveRecent()  # write back the recent file list


def select_files():
    ''' Prompt to open a file using desktop openFileDialog '''
    root = ThemedTk(theme="black")  # provides a theme for dialogs
    # root.configure(bg="#954056")    # and keeps dialog
    root.geometry(window_coord())   # on current monitor
    file_paths = filedialog.askopenfilenames(initialdir=current_path,
                                           # initialfile=os.path.basename(current_file),
                                           title="Open files",
                                           filetypes=(("all files", "*.*"),
                                                      ("Python", "*.py *.pyw"),
                                                      ("C/C++", "*.c *.cpp"),
                                                      ("h", "*.h"),
                                                      ("Javascript", "*.js"),
                                                      ("HTML", "*.html"),
                                                      ("CSS", "*.css")))
    root.destroy()  # no longer needed
    if file_paths:
        return list(file_paths)  # Return as a list of file paths
    return []

def runOptions(inx):
    ''' User executes external process (run1 - run4)
    checks for web page or system process '''
    item = opts[inx]
    if item.startswith("http"):
        webbrowser.open(item)
    else:
        # check for fullpath or path {f} or {p}
        run = item.replace("{f}", current_file)
        run = run.replace("{p}", current_path)
        os.system(run)

def windows_path(path):
    ''' reverse / for Windows path  '''
    ws = "\\"
    rp = path.replace("/", ws)
    return rp

def trim_trailing_spaces(code):
    ''' Trim Trailing space from lines of code '''
    lines = code.splitlines()
    trimmed_lines = [line.rstrip() for line in lines]
    trimmed_code = '\n'.join(trimmed_lines)
    return trimmed_code + '\n'

def save_backup_file():
    ''' Check if the file exists '''
    if not os.path.isfile(current_file):
        return
    # Extract the directory and the base file name
    dir_name, base_name = os.path.split(current_file)
    # Get the current date and time
    current_time = datetime.now()
    # Format the current time as a string
    timestamp_str = current_time.strftime("%Y%m%d_%H") # %M%S
    # Construct the backup file name
    backup_file_name = f"bkup_{base_name}_{timestamp_str}"
    backup_file_path = os.path.join(dir_name, backup_file_name)
    # Copy the original file to the backup file
    shutil.copy2(current_file, backup_file_path)

def gptCode(key: str, model: str, query: str) -> str:
    ''' method to access OpenAI API '''
    global messages
    # print(opts[18])
    try:
        client = OpenAI(
        api_key = os.environ.get(key)  # openai API
    )
    except Exception as e:
        return e

    # add the new query to the messages
    messages.append(
        {"role": "user", "content": query}
    )

    try:
        response = client.chat.completions.create(
          model=model,
          messages=messages
        )
        output = response.choices[0].message.content

        # append response to messages
        messages.append(
            {"role": "assistant", "content": output}
        )
        return output

    except Exception as e:
        return e

#
#                    P Y W E B V I E W
#
#    Javascript pywebview API functions connect to JAVASCRIPT
#
#

class Api:

    ''' All of these are called from Javascript '''

    def onClose(self):
        ''' immediate close no ask '''
        # save last opened filename
        with open(lastFileName, "w", encoding='utf-8') as fout:
            fout.write(current_file)
        # save last window dimensions
        with open(wingeo, "w", encoding='utf-8')as fout:
            fout.write(str(window.x) + "|"
                       + str(window.y) + "|"
                       + str(window.width) + "|"
                       + str(window.height))
        # exit app
        window.destroy()
        sys.exit()

    def set_current_file(self, content):
        ''' In a tab switch the current_file is updated '''
        global current_file, current_path
        current_file = content
        current_path = os.path.dirname(current_file)

    def getFileName(self):
        ''' JS/HTML needs the current filename '''
        return current_file

    def open_file(self):
        ''' Prompt to open a file using desktop openFileDialog '''
        global current_file, current_path
        selected = select_files()
        print(selected)
        if len(selected) == 0:
            return ''
        for file in selected:
            print(file)
            current_file = file
            current_path = os.path.dirname(current_file)
            updateRecents(current_file)  # update recent files list/file
            if opts[1] == "yes":
                save_backup_file()  # save backup on open file
            window.evaluate_js("openCmdFile()")
            time.sleep(.3)

    def save_file(self, content):
        ''' Save-A or Ctrl-Shift-S
            builds HTML from an ".md" file save
        '''
        global current_file, current_path
        root = ThemedTk(theme="black")  # provides a theme for dialogs
        # root.configure(bg="#954056")    # and keeps dialog
        root.geometry(window_coord())   # on current monitor
        file_path = filedialog.asksaveasfilename(initialdir=current_path,
                                                 defaultextension=".txt",
                                                 initialfile=os.path.basename(current_file),
                                                 filetypes=(("all files", "*.*"),
                                                            ("Python", "*.py *.pyw"),
                                                            ("C/C++", "*.c *.cpp"),
                                                            ("h", "*.h"),
                                                            ("Javascript", "*.js"),
                                                            ("HTML", "*.html"),
                                                            ("CSS", "*.css")))
        root.destroy()  # no longer needed
        if file_path:
            current_file = file_path
            current_path = os.path.dirname(file_path)
        else:
            return ''

        if not current_file.endswith(".md"):
            content = trim_trailing_spaces(content)

        with open(current_file, 'w', encoding='utf-8') as file:
            file.write(content)
        if current_file.endswith(".md"):
            mdToHTML()

        # save last file name
        # with open(lastFileName, "w", encoding='utf-8') as fout:
        #     fout.write(current_file)

        return current_file

    def quick_save_file(self, content):
        ''' Save or Ctrl-S
            builds HTML from an ".md" file save
        '''
        if not current_file.endswith(".md"):
            content = trim_trailing_spaces(content)
        with open(current_file, 'w', encoding='utf-8') as file:
            file.write(content)
        if current_file.endswith(".md"):
            mdToHTML()
        # save last file name
        # with open(lastFileName, "w", encoding='utf-8') as fout:
        #     fout.write(current_file)

        return current_file

    def getCmdFile(self):
        ''' Get the starting file from command line
            File was switched into the current_file/path fields
            If no command line file then opens lastfile '''
        if os.path.isfile(current_file):
            updateRecents(current_file)
            with open(current_file, 'r', encoding='utf-8') as file:
                return file.read()
        return ''  # File Not Found or no previous on startup

    def gptAccess(self, content) -> str:
        ''' User has hit Ctrl-G with either an AI prompt or the word "log".
            Access OpenAI and return query response
            or, return ailog.md if "log" was requested
            Also write response to the log if option is turned on. '''
        global messages

        if content.lower().strip() == "log":
            with open("ailog.md", 'r', encoding='utf-8') as fin:
                return fin.read()
        if content.lower().strip() == "new":
            messages = []
            return "NEW CHAT"
        key = opts[16]  # openai User Key
        mod = opts[17]  # model to use
        res = gptCode(key, mod, content)
        if opts[0].lower() == "yes":
            timestamp_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open("ailog.md", "a", encoding='utf-8') as fout:
                fout.write(timestamp_str + "\n\n")
                fout.write(content + "\n---\n")
                fout.write(res + "\n\n---\n\n")
            with open("ailog.md", 'r', encoding='utf-8') as file:
                htmlText = markdown.markdown(file.read(), extensions=['tables', 'fenced_code'])
            with open("ailog.html", 'w', encoding='utf-8') as file:
                file.write(htmlText)
        return res

    def execMarkdown(self):
        ''' open the markdown's HTML file in specified browser '''
        if not current_file.endswith(".md"):
            return
        # change to .html file
        htmlFile = current_file[:-3] + ".html"
        # open in default browser
        if opts[5].lower() == "default":
            webbrowser.open(htmlFile)
        else:
            subprocess.call([opts[5], htmlFile])

    def execWebbrowser(self):
        ''' open the web browser specified in the options.ini '''
        if opts[5].lower() == "default":
            webbrowser.open(current_file)
        else:
            subprocess.call([opts[5], current_file])

    def execFileMgr(self):
        ''' open the file manager specified in the options.ini '''
        #os.system(opts[3] + " " + current_path)
        if myOS == "Windows":
            wp = windows_path(current_path)
            subprocess.call([opts[3], wp])
        else:
            fm = opts[3].split()
            fm.append(current_path)
            # subprocess.call([opts[3], current_path])
            subprocess.call(fm)

    def execTerminal(self):
        ''' open the terminal specified in the options.ini
        This logic is to accommodate Windows Terminal:
            wt -d
        and Linux FMs like gnome-terminal:
            gnome-terminal --working-directory=
        Windows requires the extra space before the directory path
        '''
        if myOS == 'Windows':
            os.system(opts[2] + " " + current_path)
        else:
            os.system(opts[2] + current_path)

    def delete_backups(self):
        root = ThemedTk(theme="black")  # provides a theme for dialogs
        # root.configure(bg="#954056")    # and keeps dialog
        root.geometry(window_coord())   # on current monitor
        rsp = messagebox.askokcancel("Remove Backups?", f" for: {current_path}")
        if rsp is True:
            files = glob.glob(current_path + "/bkup_*")
            for file_path in files:
                os.remove(file_path)
        root.destroy()


    def exec1(self):
        ''' execute/open run 1 opts[7] '''
        runOptions(7)

    def exec2(self):
        ''' open run 2 '''
        runOptions(8)

    def exec3(self):
        ''' open run 3 '''
        runOptions(9)

    def exec4(self):
        ''' open run 4 '''
        runOptions(10)

    def getRunNames(self):
        ''' title names for run1-4 tools menu items -
        send names 1-4 from options.ini 11 12 13 14 '''
        names = ",".join(opts[11:15])
        return names

    def openSelected(self, filename):
        ''' open the requested recent file
        it's possible file was removed on
        disk so we return 'file not found'
        When no path for file assume program
        directory "p" '''
        global current_file, current_path
        current_file = filename
        current_path = os.path.dirname(current_file)
        if current_path == "":
            current_path = p
            current_file = current_path + current_file
        if current_file:
            try:
                with open(current_file, 'r', encoding='utf-8') as file:
                    txt = file.read()
            except:
                return "file not found"
            updateRecents(current_file)
            if opts[1] == "yes":
                save_backup_file()
            return txt
        return ''

    def returnRecents(self):
        ''' requesting recent file list as csv string '''
        return srec

    def open_spellcheck(self, content):
        ''' process sting of words and return results '''
        wlist = content.split()         # string to list
        words = spell.unknown(wlist)    # spell check the list
        strwords = "<br>"
        for word in words:              # concat spell output into one string
            strwords += word + "<br>"
            # Get the one `most likely` answer
            #   spell.correction(word)
            # Get a list of `likely` options
            strwords += str(spell.candidates(word))
            strwords += "<hr>"
        return strwords


    def on_file_drop(self, filename):
        ''' Search for the specified filename in the given directory
            and its subdirectories. Return a csv string of fullpaths. '''
        search_path = opts[6]  # file system scope. ex: /home/usER...
        matches = []
        drpath = ""  # holds csv string
        c = 0  # for counting "," in the csv string

        for root, dirs, files in os.walk(search_path):
            if filename in files:
                matches.append(os.path.join(root, filename))

        # create csv string from matches list
        n = len(matches)
        for item in matches:
            drpath += item
            c += 1
            if c < n:
                drpath += ","

        return drpath

    def reLaunch(self):
        ''' close and re-open this instance '''
        python = sys.executable
        window.destroy()
        os.execl(python, python, *sys.argv)

    def addsnipit(self, content):
        ''' extract trigger word and code to
            append a new zen snipit to tags.js
            this replaces the fzen.py program '''
        sniplist = content.split("\n")
        parts = sniplist[1].split(":")
        trig = parts[1].strip()
        code = sniplist[2:]

        # print(trig)
        # print(code)

        tagstr = "\"" + trig + "\": \""

        # escape all double quotes
        for line in code:
            line = line.replace('"', r'\"')
            tagstr += line + "\\n"
        tagstr += "\","  # concat final double quote

        print("")
        print(tagstr)
        print("")

        # read in the Zen tags file
        with open(tags, "r") as fin:
            zenlst = fin.readlines()
        zenlst = [i.strip() for i in zenlst]

        # add the new tag at end of list
        zenlst.remove("}; //")
        zenlst.append(tagstr)

        # write back the list to the file
        with open(tags, "w") as fout:
            for line in zenlst:
                fout.write(line + "\n")
            fout.write("}; //\n")


#               END OF JS_API CLASS


if __name__ == '__main__':
    api = Api()

    win = [100,100,800,600] # initialize geo: left,top,width,height

    if myOS == 'Windows':
        mypy = 'pythonw.exe'

    '''
    The following opens a file from the command line
    or by default the last file used at shut down.
    '''
    if len(sys.argv) > 1:
        current_file = sys.argv[1]  # needs a full path !
        current_path = os.path.dirname(current_file)
    elif os.path.isfile(lastFileName) and opts[4] == "yes":
        with open(lastFileName, 'r', encoding='utf-8') as f:
            current_file = f.readline().strip()
            current_path =  os.path.dirname(current_file)
        updateRecents(current_file)
        if opts[1] == "yes":
            save_backup_file()

    # get last window size and location
    if os.path.isfile(wingeo):
        with open(wingeo) as f:
            geom = f.read().strip()
        win = geom.split('|')  # 0 left, 1 top, 2 width, 3 height
        win = [int(i) for i in win]  # make integers

    urlquery = f"cs.html?theme={opts[15]}"

    window = webview.create_window('CodeScriber 2.5',
                     url=urlquery, x=win[0], y=win[1],
                     width=win[2],
                     height=win[3],
                     js_api=api)

    webview.start()  # (debug=True)
