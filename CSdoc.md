# CodeScriber Documentation

![Image](images/CSdoc1.png "CodeScriber Image")

CodeScriber uses the "Ace" Code Editor - a Javascript library.

For detailed information about "Ace" visit the 
[Ace website](https://ace.c9.io/ "https://ace.c9.io/")

* The core application (CodeScriber) is written entirely in scripting languages—HTML, CSS, JavaScript, and Python 3—which makes it highly modifiable and extensible.

* The UI is built using HTML/JavaScript. A Python script acts as the host for the editor using _webview_ (via the pywebview module). On Linux (for example) the Gtk WebKit2 engine is used, while on Windows it might use a variant like edgechromium. This setup allows JavaScript in the webview to communicate with Python running on the host machine.

* Although nearly all functionality runs locally, the “Ace” code editor library is loaded from cdnjs.cloudflare.com. Additionally, the AI feature requires an internet connection, so not every feature is completely offline.

This design gives you several benefits:

* You have local file access and integration through Python.
* The UI enjoys the flexibility and ease of web technologies.
* Because it’s built entirely in scripting languages, users can dive in and customize or extend the tool.

### Functions of Ace Code Editor

<table style="font-size: 9pt;">
<tr>
<td>
goToNextError - Alt-E<br>
goToPreviousError - Alt-Shift-E<br>
selectall - Ctrl-A<br>
centerselection - null<br>
gotoline - Ctrl-L<br>
fold - Alt-L|Ctrl-F1<br>
unfold - Alt-Shift-L|Ctrl-Shift-F1<br>
toggleFoldWidget - F2<br>
toggleParentFoldWidget - Alt-F2<br>
foldall - null<br>
foldAllComments - null<br>
foldOther - Alt-0<br>
unfoldall - Alt-Shift-0<br>
findnext - Ctrl-K<br>
findprevious - Ctrl-Shift-K<br>
selectOrFindNext - Alt-K<br>
selectOrFindPrevious - Alt-Shift-K<br>
find - Ctrl-F<br>
selecttostart - Ctrl-Shift-Home<br>
gotostart - Ctrl-Home<br>
selectup - Shift-Up<br>
golineup - Up<br>
selecttoend - Ctrl-Shift-End<br>
gotoend - Ctrl-End<br>
selectdown - Shift-Down<br>
golinedown - Down<br>
selectwordleft - Ctrl-Shift-Left<br>
gotowordleft - Ctrl-Left<br>
selecttolinestart - Alt-Shift-Left<br>
</td>
<td>
gotolinestart - Alt-Left|Home<br>
selectleft - Shift-Left<br>
gotoleft - Left<br>
selectwordright - Ctrl-Shift-Right<br>
gotowordright - Ctrl-Right<br>
selecttolineend - Alt-Shift-Right<br>
gotolineend - Alt-Right|End<br>
selectright - Shift-Right<br>
gotoright - Right<br>
gotopagedown - PageDown<br>
scrollup - Ctrl-Up<br>
scrolldown - Ctrl-Down<br>
togglerecording - Ctrl-Alt-E<br>
replaymacro - Ctrl-Shift-E<br>
jumptomatching - Ctrl-\\|Ctrl-P<br>
selecttomatching - Ctrl-Shift-\\|Ctrl-Shift-P<br>
expandToMatching - Ctrl-Shift-M<br>
removeline - Ctrl-D<br>
duplicateSelection - Ctrl-Shift-D<br>
sortlines - Ctrl-Alt-S<br>
togglecomment - Ctrl-/<br>
toggleBlockComment - Ctrl-Shift-/<br>
modifyNumberUp - Ctrl-Shift-Up<br>
modifyNumberDown - Ctrl-Shift-Down<br>
replace - Ctrl-H<br>
undo - Ctrl-Z<br>
redo - Ctrl-Shift-Z|Ctrl-Y<br>
copylinesup - Alt-Shift-Up<br>
movelinesup - Alt-Up<br>
</td>
<td>
copylinesdown - Alt-Shift-Down<br>
movelinesdown - Alt-Down<br>
backspace - Shift-Backspace|Backspace<br>
cut_or_delete - Shift-Delete<br>
removetolinestart - Alt-Backspace<br>
removetolineend - Alt-Delete<br>
removetolinestarthard - Ctrl-Shift-Backspace<br>
removetolineendhard - Ctrl-Shift-Delete<br>
removewordleft - Ctrl-Backspace<br>
removewordright - Ctrl-Delete<br>
outdent - Shift-Tab<br>
indent - Tab<br>
blockoutdent - Ctrl-[<br>
blockindent - Ctrl-]<br>
transposeletters - Alt-Shift-X<br>
touppercase - Ctrl-U<br>
tolowercase - Ctrl-Shift-U<br>
expandtoline - Ctrl-Shift-L<br>
openCommandPallete - F1<br>
addCursorAbove - Ctrl-Alt-Up<br>
addCursorBelow - Ctrl-Alt-Down<br>
addCursorAboveSkipCurrent - Ctrl-Alt-Shift-Up<br>
addCursorBelowSkipCurrent - Ctrl-Alt-Shift-Down<br>
selectMoreBefore - Ctrl-Alt-Left<br>
selectMoreAfter - Ctrl-Alt-Right<br>
selectNextBefore - Ctrl-Alt-Shift-Left<br>
selectNextAfter - Ctrl-Alt-Shift-Right<br>
toggleSplitSelectionIntoLines - Ctrl-Alt-L<br>
alignCursors - Ctrl-Alt-A<br>
findAll - Ctrl-Alt-K<br>
</td>
</tr></table>

__Additional Functions:__

<table border=1 cellspacing=0 cellpadding=4>
	<tr>
		<td><b>Ctrl-S</b></td>
		<td>Save</td>
	</tr>
	<tr>
		<td><b>Ctrl-Shft-S</b></td>
		<td>Save-As</td>
	</tr>
	<tr>
		<td><b>Ctrl-Alt-C</b></td>
		<td>Spell Check Selected text</td>
	</tr>
	<tr>
		<td><b>Ctrl-Z</b></td>
		<td>Insert Zen Tag</td>
	</tr>
	<tr>
		<td><b>Alt-X</b></td>
		<td>Select Zen Snipit from List</td>
	</tr>
	<tr>
		<td><b>Ctrl-Alt-F</b></td>
		<td>Find Functions</td>
	</tr>
	<tr>
		<td><b>Ctrl-Alt-H</b></td>
		<td>Display All Keyboard Shortcuts</td>
	</tr>
	<tr>
		<td><b>Ctrl-Alt-X</b></td>
		<td>Display enclosure keys</td>
	</tr>
	<tr>
		<td><b>Ctrl-Q</b></td>
		<td>Quit</td>
	</tr>
	<tr>
		<td><b>Alt-E</b></td>
		<td>Set up temporary text encloser</td>
	</tr>
	<tr>
		<td><b>Ctrl-G</b></td>
		<td>Fire off an AI prompt from<br>
		    new page or selected text</td>
	</tr>
	<tr>
		<td><b>Ctrl-0 through 9</b></td>
		<td>Enclose selected text</td>
	</tr>
	<tr>
		<td><b>Alt-W</b></td>
		<td>Repeat last text enclosure</td>
	</tr>
	<tr>
		<td><b>Ctrl-Alt-1</b></td>
		<td>Run 1 (defined in options.ini)</td>
	</tr>
	<tr>
		<td><b>Ctrl-Alt-2</b></td>
		<td>Run 2 (defined in options.ini)</td>
	</tr>
	<tr>
		<td><b>Ctrl-Alt-3</b></td>
		<td>Run 3 (defined in options.ini)</td>
	</tr>
	<tr>
		<td><b>Ctrl-Alt-4</b></td>
		<td>Run 4 (defined in options.ini)</td>
	</tr>
	<tr>
		<td><b>Ctrl-R</b></td>
		<td>Recent File List</td>
	</tr>
	<tr>
		<td><b>Ctrl-O</b></td>
		<td>Open a file</td>
	</tr>
	<tr>
		<td><b>Ctrl-N</b></td>
		<td>New document (file)</td>
	</tr>
	<tr>
		<td><b>F1</b></td>
		<td>Command Pallete</td>
	</tr>
	<tr>
		<td><b>F3</b></td>
		<td>Next Bookmark</td>
	</tr>
	<tr>
		<td><b>Shift-F3</b></td>
		<td>Clear Bookmarks</td>
	</tr>
</table>

_All event keys are coded in the `cs.html` file._

- Ctrl-Alt-H displays all keyboard hot keys _except Ctrl-0..9 text enclosures_

- Right-Click file tab to close.

---

## *Zen Znipits*

The file `tags.js` holds a json array for use with the Zen snipit feature.

To use: type in the "command/trigger" word and hit **Alt-Z**. The word is replaced by the code 
associated with the command. Alternatively, hit **Alt-X** and select from a list.

Use the menu **Options --> Tags** to view and modify the `tags.js` file.

        const atags = {
          "command": "output",
          "command": "output",
          "command": "output",
        };


_Example from `tags.js`_  

        "input": "<input type='' id='' value='' />",

In the editor, type __input__ and press **Alt-Z**  
`input` is replaced by `<input type='' id='' value='' />`

### New Snipits

Creating a new Zen snipit is very easy.  
In the menu click on **Options --> New Snipit**.  
Enter a _trigger word_ that you will use with Ctrl-Z to insert the snip of code.  
Enter the snipit code to be inserted.  
Hitting _Save_ (or Ctrl-S) appends the snipit to the json array in `tags.js`.

**The new snipits will not be available to use until CodeScriber is re-launched.**

View and edit/delete snipits from the `tags.js` file.  
You can sort the individual lines of snipits in the `tags.js` file by
using the _sortlines_ feature of the editor (Ctrl-Alt-S) if desired.

---

## Enclosing text with markup hotkeys

You can designate up to 10 (0-9) surrounding markup texts.  
The defaults are set in the `tags.js` file.  
Use the menu **Options --> Tags** to modify the text enclosures.

        var stag = ["<strong>,</strong>",
                    "<center>,</center>",
                    "<em>,</em>",
                    "<code>,</code>",
                    "<dt>,</dt>",
                    "<dd>,</dd>",
                    "<div id=''>,</div>",
                    "<span id='',</span>",
                    "_,_",
                    "**,**"];

Apply these to selected text using **Ctrl-0, Ctrl-1, Ctrl-2, ... Ctrl-9**  
Change any of them for current session using **Ctrl-E**.  

---

_When working with Markdown, HTML is **generated on every save**._  
Use the Tools menu "**Markdown**" to open the HTML in a browser for review.  
There after refresh the browser whenever the markdown is saved.  
This Markdown follows rules from the 
[Markdown 3.7](https://pypi.org/project/Markdown/ "markdown module") python3 module.

---

## Bookmarking?

To bookmark a line of code use **Ctrl-Click in the "gutter"** (where the line numbers are)  
To travel through the bookmarks use **F3**.  
To clear all bookmarks use **Shift-F3**.

_Note: bookmarks will not align when lines are added or deleted._

---

## AI coding query

#### Setup

The advent of AI has definitely changed the art of computer programming.
This implementation requires an OpenAI API [key](https://platform.openai.com/api-keys "OpenAI").
Set up your key as a system environment variable and then put the variable name in the _options.ini_ file,
like `openai=MYKEY`
The OpenAI _model_ must also appear in the `options.ini` file, like `model=GPT-4o` or whatever model you use.

#### Prompt and Query

To run an AI query start a new document and construct your prompt,  
or select some text for the prompt.

Then use **Ctrl-G** to send the prompt.  
In a few seconds the response will fill a new document page.

---

## Spell Check

To spell check some text first select the text. Then hit **Ctrl-Alt-C**. You will get a list of
miss-spelled words and possible corrections.

---
## options.ini

**CodeScriber options**

    ailog=yes
    backup=yes
    terminal=gnome-terminal --working-directory=
    filemanager=thunar
    previous=yes
    browser=firefox
    theme=twilight
    scope=/home/UsEr
    openai=GPTKEY
    model=o1-mini
    run1=/blah/blahh/CodeSnips/csnips.py
    run2=gnome_terminal -e htop
    run3=python3 {f}
    run4=https://www.w3schools.com/
    nam1=CSnips
    nam2=htop
    nam3=python3
    nam4=w3schools

The Windows options.ini could look more like this:

    ailog=yes
    backup=yes
    terminal=wt -d
    filemanager=explorer.exe
    previous=yes
    browser="C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
    theme=monokai
    scope=C:\
    openai=GPTKEY
    model=o1-mini
    run1=https://www.w3schools.com/
    run2=cmd
    run3=C:\Users\User\AppData\Local\GitHubDesktop\GitHubDesktop.exe
    run4=calc.exe
    nam1=w3schools
    nam2=cmd
    nam3=GitHub
    nam4=Calculator


**ailog**
>Append OpenAI reponses to `ailog.md` **yes|no**

**backup**
>Create a backup of opened files **yes|no**  
Backups appear as `bkup_*`

**terminal**
>Enter your terminal preference and the option to  
start at a specific working directory.  
Current path will be added as final argument.

**filemanager**
>The name of your systems file manager executable file.  
Current path will be added as final argument.

**previous**
>Open last file at start-up **yes|no**

**browser**
>The executable of the browser you wish to use.  
**Default** if you want to use your system default browser.

**scope**
>Set the _starting directory_ in your file system that CodeScriber should use.

**openai**
>Environment variable for your OpenAI key  
[about OpenAI keys](https://platform.openai.com/settings/organization/api-keys "OpenAI keys")

**model**
>The model to use for the OpenAI API  
[about OpenAI models](https://platform.openai.com/docs/models "OpenAI")

**run1 ... run4**
>External programs you might want to execute via menus or  
_Ctrl-Alt-1_ _Ctrl-Alt-2_ _Ctrl-Alt-3_ _Ctrl-Alt-4_ 

**theme**
>Editor theme name for all file types.  
COLOR THEMES:  
monokai | cobalt | vibrant\_ink | clouds\_midnight | solarized\_dark  
tomorrow\_night\_eighties | twilight | kr\_theme | Terminal  
solarized\_light | textmate | tomorrow\_night


**Notes:** Non URL Run# items are implemented with a simple os.system() method.  
Make sure your executable is in your system path or supply it with a fullpath.  
A URL is opened in your system's default browser.

The **font family** and **size** are set in the cs.css file under #editor. 

---

Some additional **editor options** can be found in the `cs.html` file (around line 150).  

    // ACE CONFIGURE - set at startup
    editor.$blockScrolling = Infinity;  // ace debug suggestion
    editor.setShowPrintMargin(false);
    editor.setHighlightActiveLine(false);
    editor.session.setTabSize(4);
    editor.session.setUseSoftTabs(true); // use spaces instead of tab chars
    editor.session.setUseWrapMode(false);

[more info...](https://ace.c9.io/#nav=howto "Ace Editor Options")

---

## Menus

### Tools menu

- **Terminal**  
  Open a terminal as designated in the _options.ini_

- **Files**  
  Open your file manager as designated in the _options.ini_ 

- **Browser**  
  Open current file with the browser specified in _options.ini_

- **Markdown**  
  Open your markdown document's compiled HTML in your browser.  
  Each save of a markdown document generates it's HTML file.

- **Find File**  
  Find (and open) a file anywhere on the system

- **Functions**
  Go to a fuction from a list of functions _(most languages)_

- **Pic color**
  HTML5 color picker saves selected to clipboard

- **Delete Backups**  
  Remove all backups in directory of active tab (file)

- **Run 1 ... Run 4**   
  Executes an external process as designated in _options.ini_

**_The context menu has "Copy" and some of these commands_**

### Options menu

Changes will not take effect until CodeScriber is re-started.   

- **Options**  
  Open the `options.ini` file for editing various options

- **Re-Launch**  
  Closes and re-opens CodeScriber activating any changes to the Options

- **New Snipit**  
  Opens the Zen Snipit template for entering a new code snipit

- **Tags**  
  Open the `tags.js` file for editing the various tags and options

- **File Modes**  
  Open the `filemodes.js` file for editing language modes

- **Open AI Log**  
  Open the `ailog.md` file for editing or viewing

- **Wrapping**
  Toggles word wrap for current session (tab)

---

## Running CodeScriber

There's always more than one way, but here are some suggestions.

<code>
$>python3 cs.py  
$>python3 cs.py fileToOpen
</code>

bash file:  
<code>
>cd /home/user/ ... /codescriber  
>python3 cs.py $1 &  
**or**  
>python3 /home/user/ ... /CodeScriber/cs.py $1 &  
</code>
---

**The geometry of CodeScriber's window is saved.**

---

## Note for Windows Users

**If you uninstall Microsoft Edge or any of its components, CodeScriber will not work.  
This is because pywebview uses some Edge components for rendering.**

Suggest to use `C:\codescriber\` for location.

Create a CMD command file, like `cs.cmd` that contains:    
`pythonw.exe cs.py`

To execute:  
`C:/codescriber/cs.cmd`

For a shortcut use:  

![diagram](images/CS_Windows_Short.png "shorcut for windows")

---

> ![diagram](images/CSdiag.png "Conceptual")
