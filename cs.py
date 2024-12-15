'''
cs.py CodeScriber Code Editor
Hakable Desktop Code Editor
Oct 2024 Michael Leidel
'''

import sys
import os
import subprocess
import webbrowser
import platform
from tkinter.ttk import *
from tkinter import filedialog
from ttkthemes import ThemedTk
import webview
import markdown

import iniproc

p = os.path.realpath(__file__)
p = os.path.dirname(p) + "/"
# os.chdir(os.path.dirname(p))
optionsFileName = p+"options.ini"
lastFileName = p+"lastfile"
wingeo = p+"wingeo"


rec = []  # recent file list GLOBAL
srec = "" # csv string for javascript recent file list

opts = [] # storeing options from the options.ini file
opts = iniproc.read(optionsFileName,'future1',
                                   'future2',
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
                                   'theme')

current_file = ""  # tracks current file in use
current_path = opts[6]  # tracks path
myfpath = os.path.abspath(__file__)  # save this instance full path
myOS = platform.system()  # Linux or Windows
mypy = 'python3'  # for linux default

# UNCOMMENT THIS FUNCTION TO WORK ON DUAL MONITORS (there is more)
def window_coord():
    ''' use this func when using multiple monitors '''
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
    ''' convert MD file to HTML file '''
    with open(current_file, 'r', encoding='utf-8') as file:
        htmlText = markdown.markdown(file.read())
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
        if n > 5:             # keep the list to 6 or less items (COULD BE A VARIABLE)
            rec.pop(n-1)        # remove the bottom item (0 relative)
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

def select_file():
    ''' Prompt to open a file using desktop openFileDialog '''
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
        return file_path  # here is problem - changes current_file!!!!!!
    return ''

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

def windows_path(p):
    ''' reverse / for Windows path  '''
    ws = "\\"
    rp = p.replace("/", ws)
    return rp

def trim_trailing_spaces(code):
    ''' Trim Trailing space from lines of code '''
    lines = code.splitlines()
    trimmed_lines = [line.rstrip() for line in lines]
    trimmed_code = '\n'.join(trimmed_lines)
    return trimmed_code

'''
                    P Y W E B V I E W

    Javascript pywebview API functions to connect JAVASCRIPT

'''

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
        selected = select_file()
        if selected == '':
            return ''
        current_file = selected
        current_path = os.path.dirname(current_file)
        updateRecents(current_file)  # update recent files list/file
        with open(current_file, 'r', encoding='utf-8') as file:
            return file.read()


    def save_file(self, content):
        ''' Save-A or Ctrl-Shift-S
            builds HTML from an ".md" file save
        '''
        global current_file, current_path
        #root = tk.Tk()  # COMMENT IF USING SINGLE MONITOR SYSTEM
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
        else:
            return ''

        if not current_file.endswith(".md"):
            content = trim_trailing_spaces(content)

        with open(current_file, 'w', encoding='utf-8') as file:
            file.write(content)
        if current_file.endswith(".md"):
            mdToHTML()

        # save last file name
        with open(lastFileName, "w", encoding='utf-8') as fout:
            fout.write(current_file)

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
        with open(lastFileName, "w", encoding='utf-8') as fout:
            fout.write(current_file)

        return current_file

    def getCmdFile(self):
        ''' Get the starting file from command line
            File was switched into the current_file/path fields
            If no command line file then opens lastfile
        '''
        if os.path.isfile(current_file):
            updateRecents(current_file)
            with open(current_file, 'r', encoding='utf-8') as file:
                return file.read()
        return ''  # File Not Found or no previous on startup

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
            subprocess.call([opts[3], current_path])

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
        disk so we return 'file not found' '''
        global current_file, current_path
        current_file = filename
        current_path = os.path.dirname(current_file)
        if current_file:
            try:
                with open(current_file, 'r', encoding='utf-8') as file:
                    txt = file.read()
            except:
                return "file not found"
            updateRecents(current_file)
            return txt
        return ''

    def returnRecents(self):
        ''' requesting recent file list as csv string '''
        return srec

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


#  END OF JS_API CLASS  END OF JS_API CLASS  END OF JS_API CLASS


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
    else:
        if os.path.isfile(lastFileName) and opts[4] == "yes":
            with open(lastFileName, 'r', encoding='utf-8') as f:
                current_file = f.readline().strip()
                current_path =  os.path.dirname(current_file)
        updateRecents(current_file)

    # get last window size and location
    if os.path.isfile(wingeo):
        with open(wingeo) as f:
            geom = f.read().strip()
        win = geom.split('|')  # 0 left, 1 top, 2 width, 3 height
        win = [int(i) for i in win]  # make integers

    urlquery = f"cs.html?theme={opts[15]}"

    window = webview.create_window('CodeScriber 2.0',
                     url=urlquery, x=win[0], y=win[1],
                     width=win[2],
                     height=win[3],
                     js_api=api)

    webview.start()  # (debug=True)