/*
.   ____         __
.  / __/__  ____/ /__  ___ __ _________ ___
. / _// _ \/ __/ / _ \(_-</ // / __/ -_|_-<
./___/_//_/\__/_/\___/___/\_,_/_/  \__/___/

change default surrounding tags here
They are used with Ctrl-0,1,2,3, ... 9
Change during session with Alt-E
Restart CodeScriber for new settings to take effect
*/
var stag = ["<u>,</u>",
"<em>,</em>",
"<code>,</code>",
"<dt>,</dt>",
"<dd>,</dd>",
"<div id=''>,</div>",
"<span id='',</span>",
"<center>,</center>",
"_,_",
"**,**"];

/*
.  ____             __
. /_  / ___ ___    / /____ ____ ____
.  / /_/ -_) _ \  / __/ _ `/ _ `(_-<
. /___/\__/_//_/  \__/\_,_/\_, /___/
.                         /___/

Type the tag and hit Ctrl-Z

Use fzen.py at command line to easily format new tags
and append to this array.
USAGE:
1. open terminal
2. copy code into clipboard
3. python3 fzen.py
4. enter new tag name
5. [repeat] then check tags.js to verify
6. test new tags in codescriber
*/
const atags = {
"a": "<a href=\"\" id=\"\" target=\"_blank\"></a>",
"br": "<br style=\"clear:left;\">",
"button": "<input type=\"button\" onclick=\"\" value=\"\">",
"checkbox": "<label for='AA'>description</label>\n<input type='checkbox' id='AA' name='postfield' value='postvalue'>",
"form": "<form name=\"\" action=\"someprocess.php\" method=\"post\">\n	<input type=\"hidden\" name=\"\" id=\"\" value=\"\">\n	<input type=\"submit\" name=\"\" value=\"\">\n</form>\n\n",
"html": "<!DOCTYPE HTML>\n<html lang='en-US'>\n<head>\n	<meta charset='UTF-8'>\n	<meta name='viewport' content='width=device-width, initial-scale=1'>\n	<link rel='manifest' href='manifest.json'>\n	<title>XXXXX</title>\n	<script type='text/javascript' src='../js/myJS-1.2.min.js'></script>\n  <script src='../js/JSmodal.min.js'></script>\n  <link rel='stylesheet' href='../css/JSmodalani.css'>\n  \n</head>\n<body>\n\n</body>\n</html>\n\n",
"input": "<input type=\"text\" id=\"\" value=\"\">",
"label": "<label for=\"id\"></label>",
"link": "<link rel=\"stylesheet\" href=\"\">",
"mdimage": '![alttext](http:// "title")',
"mdlink": '[linktext](http:// "title")',
"mdtable": "\n| xxxxx | xxxxx | xxxxx | xxxxx |\n| :---: | :---: | :---: | :---: |\n|       |       |       |       |\n\n\n\n",
"py_env": "\n# import os\nuser = os.environ.get(\"USER\")\n\n\n",
"py_file1": "\nwith open(FILENAME, 'w|r|a', encoding='utf-8') as file:\n    file.write(CONTENT)\n\n",
"py_file2": "\nVAR = open(FILENAME, encoding='utf-8').read().strip()\n\n",
"py_file3": "\nwith open(\"Rose.txt\", \"r\") as file:\n    lines = file.readlines()\n \n",
"py_list_strip": "\nlines = [line.strip() for line in lines]\n\n",
"py_striplist": "\nfo = open(\"test.txt\")\nlst = fo.readlines()\nlst = [i.strip() for i in lst]\n\n",
"radio": "<label for='AA'>description</label>\n<input type='radio' id='AA' name='postfield' value='postvalue' checked>",
"script": "<script>\n\n<\/script>",
"script2": "<script src=\"\"><\/script>",
"select": "<select name=\"\" id=\"\" size=\"\" onchange=\"\" autofocus required>\n	<option value=\"\" selected>\n	<option value=\"\">\n</select>\n",
"table": "<table cellpadding=1 cellspacing=1>\n<tr>\n    <td></td>\n</tr>\n</table>\n",
"textarea": "<textarea id=\"\" rows=\"\" cols=\"\" onchange=\"\" wrap=\"off\" spellcheck=\"false\"></textarea>\n\n",
"tk_button": "w = Button(self, text='button', command=self.cmdfunc)\n  w.grid(row=1, column=1, rowspan=1, columnspan=1, padx=4, pady=20)\n\n",
"tk_check": "self.vw = IntVar()\nw = Checkbutton(self, variable=self.vw, text='Checkbutton')\nw.grid(row=1, column=1, sticky='', pady=20)\n\n",
"tk_clip": "# CLIPBOARD HANDLING\n# # import pyperclip\n# pyperclip.copy(string)\n# string = pyperclip.paste()\n#\n# # Or just use tkinter.clipboard\n# root.clipboard_clear()  # clear clipboard contents\n# root.clipboard_append(string)  # append new value to clipbaord\n# root.update()\n# root.clipboard_get()\n\n",
"tk_combo": "self.vw = StringVar()\nw = Combobox(self, textvariable=self.vw)\nw['values'] = ('Item 0', 'Second Item', 'Third String')\nw.current(0)  # set start selection\nw.grid(row=0, column=0, sticky='nsew', pady=20)\nw.bind(\"<<ComboboxSelected>>\", self.commandfunc)\n\n",
"tk_entry": "self.vw = StringVar()\n w = Entry(self, textvariable=self.vw)\n w.grid(row=1, column=1, pady=20)\n #self.vw.set(\"Entry widget\")\n #self.vw.get()\n #w.select_range(0, END)\n #w.focus()\n\n",
"tk_file": "# FILEDIALOG HANDLING\n# # from tkinter import filedialog\n# filename =  filedialog.askopenfilename(initialdir = \"/\",\n#             title = \"Open file\",\n#             filetypes = ((\"jpeg files\",\"*.jpg\"),(\"all files\",\"*.*\")))\n\n#filename = filedialog.askopenfilename(initialdir = os.getcwd(),\n#                 #initialdir = os.getcwd(),\n#                 title = \"Please select a file:\",\n#                 filetypes = ((\"All Files\",\"*\"),))\n\n# filename = filedialog.asksaveasfilename(initialdir = \"/\",\n#             title = \"Save file\",\n#             filetypes = ((\"jpeg files\",\"*.jpg\"),(\"all files\",\"*.*\")))\n\n# fname = filedialog.asksaveasfilename(confirmoverwrite=True,\n#     initialdir=os.path.dirname(os.path.abspath(__file__)))\n# if fname:\n#     try:\n#         with open(fname, \"w\") as f:\n#             f.write(self.tex.get(\"1.0\", END))  # contents of the demo Text widget\n#     except:\n#         showerror(\"Save File\", \"Failed to save file '%s'\" % fname)\n#     return\n\n",
"tk_frame": "w = Frame(self, width=100, height=100, relief=SUNKEN)\nw.grid(row=1, column=1, rowspan=1, columnspan=1,\n       sticky='nsew', pady=20)\n\n",
"tk_geometry": "# UNCOMMENT THE FOLLOWING TO SAVE GEOMETRY INFO\n# if os.path.isfile(\"winfo\"):\n#     with open(\"winfo\") as f:\n#         lcoor = f.read()\n#     root.geometry(lcoor.strip())\n# else:\n#     root.geometry(\"350x200\") # WxH+left+top\n\n",
"tk_hscroll": "VAR = Scrollbar(PARENT, orient=HORIZONTAL, command = WIDGET.xview)\nVAR.grid(row=0, column=0, rowspan=0, columnspan=0, sticky='new')\nWIDGET['xscrollcommand'] = VAR.set\n\n",
"tk_label": "self.vw = StringVar()\nw = Label(self, textvariable=self.vw)\nw.grid(row=1, column=1, rowspan=1, columnspan=1, pady=20)\nself.vw.set(\"label ... text\")\n\n",
"tk_lblframe": "w = LabelFrame(self, text=\"LabelFrame\", width=100, height=100)\nw.grid(row=1, column=1, rowspan=1, columnspan=1, sticky='nsew', pady=20)\n\n",
"tk_list": "    # LISTBOX WIDGET\n    self.w = Listbox(self)\n    self.w.grid(row=1, column=1, rowspan=1, columnspan=1,\n                sticky='nse', pady=10)\n    self.w.bind(\"<<ListboxSelect>>\", self.w_selected)\n    for i in range(100):\n        self.w.insert(i, str(i) + \"Item\")\n    # code to load list box\n    # self.w.delete(0,'end')\n    # for inx, item in enumerate(LIST_OF_ITEMS):\n    #    self.w.insert(inx, item[0])\n    ## Handler for List selection\ndef w_selected(self, e=None):\n    list_item = self.w.curselection()\n    fp = self.w.get(list_item[0])\n    print(str(fp) + \" --> \" + str(list_item[0]) +\n        \" of \" + str(self.w.size()))\n		# or:\n        # list_item = self.lst.get(ANCHOR)\n        # list_inx = self.lst.index(ANCHOR)\n        # print(list_item, str(list_inx) +\n        #       \" of \" + str(self.lst.size()))\n\n    # FUNCS TO EDIT LISTBOX CONTENTS\n    #\n    # def delete_item(self):\n    #     if self.w.curselection() == ():\n    #         return # nothing selected\n    #     print(\"Deleting: \" + str(self.w.curselection()))\n    #     self.w.delete(self.w.curselection())\n    #\n    # def insert_item(self, txt):\n    #     if self.w.curselection() == ():\n    #         return # nothing selected\n    #     list_item = self.w.curselection()\n    #     self.w.insert(list_item[0], txt)\n    #     print(\"inserted at \" + str(list_item[0]))\n\n\n",
"tk_msgbox": "# # from tkinter import messagebox\n# messagebox.showerror(\"Error\", \"Error message\")\n# messagebox.showwarning(\"Warning\",\"Warning message\")\n# messagebox.showinfo(\"Information\",\"Informative message\")\n# messagebox.askokcancel('Message title', 'Message content')\n# messagebox.askretrycancel('Message title', 'Message content')\n#     ok, yes, retry returns TRUE\n#     no, cancel returns FALSE\n\n",
"tk_notebook": "VAR = Notebook(PARENT)\ntab1 = Frame(VAR, width=200, height=200)\ntab2 = Frame(VAR)\ntab3 = Frame(VAR)\nVAR.add(tab1, text = 'tab 1')\nVAR.add(tab2, text = 'tab 2')\nVAR.add(tab3, text = 'tab 3')\nVAR.grid(row=0, column=0, rowspan=0, columnspan=0)\n\n",
"tk_option": "optionlist = ('GNOME', 'Xfce', 'MATE', 'LXDE', 'KDE', 'Windows 10')\nself.vVAR = StringVar()\nVAR = OptionMenu(PARENT, self.vVAR, *optionlist)\nVAR.grid(row=0, column=0, sticky='')\nself.vVAR.set(optionlist[1])\n\n",
"tk_radio": "self.vVAR = StringVar()  # JUST ONE PER SET\nVAR = Radiobutton(PARENT, variable=self.vVAR, value='ON', text='On')\nVAR.grid(row=0,column=0, sticky='')  # sticky here keeps closer together\nself.vVAR.set('ON')\n\n",
"tk_root": "root.title(\"Tkinter Demo\")\n# root.protocol(\"WM_DELETE_WINDOW\", save_location)  # UNCOMMENT TO SAVE GEOMETRY INFO\n# Sizegrip(root).place(rely=1.0, relx=1.0, x=0, y=0, anchor=SE)\n# root.resizable(w,h) # no resize & removes maximize button\n# root.minsize(w, h)  # width, height\n# root.maxsize(w, h)\n# root.overrideredirect(True) # removed window decorations\n# root.iconphoto(False, PhotoImage(file='icon.png'))\n# root.attributes(\"-topmost\", True)  # Keep on top of other windows\napp = Application(root)\napp.mainloop()\n\n",
"tk_simple": "# tkinter simpledialog version\ndef btn_dlgstr(self):\n	str_item = simpledialog.askstring(\"Single item string entry\",\n                                    \"What is your first name?\",\n                                    parent=self)\n	messagebox.showinfo(\"You entered your name as:\", str_item)\n\n",
"tk_template": "# template\n\nfrom tkinter import *\nfrom tkinter.ttk import *  # defaults all widgets as ttk\nfrom ttkthemes import ThemedTk  # module applied to all widgets\n                                # pip install ttkthemes\n\nclass Application(Frame):\n    ''' use oop format for GUI program '''\n    def __init__(self, master=None):\n        super().__init__(master)\n        self.pack()\n        self.create_widgets()\n\n    def create_widgets(self):\n        ''' define widgets and show '''\n        style = Style()\n        style.configure('TButton', width=14, font='Purisa 15')\n\n        btn1 = Button(self, text=\"Close App\", command=exit)\n        btn1.grid(row=0,column=0, padx=5, pady=5)\n\n        btn2 = Button(self, text=\"Ok\", command=exit)\n        btn2.grid(row=1,column=0, padx=5, pady=5)\n\n# 'alt', 'scidsand', 'classic', 'scidblue',\n# 'scidmint', 'scidgreen', 'default', 'scidpink',\n# 'arc', 'scidgrey', 'scidpurple', 'clam'\nroot = ThemedTk(theme=\"scidsand\")\nroot.title(\"TITLE\")\napp = Application(master=root)\napp.mainloop()\n\n",
"tk_vscroll": "VAR = Scrollbar(PARENT, orient=VERTICAL, command = WIDGET.yview)\nVAR.grid(row=0, column=0, rowspan=0, columnspan=0, sticky='nsw')\nWIDGET['yscrollcommand'] = VAR.set\n\n",
}; //
