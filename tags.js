
/*
   ___              __  ___                _  __
  / _ \__ _____    /  |/  /__ ___  __ __  / |/ /__ ___ _  ___ ___
 / , _/ // / _ \  / /|_/ / -_) _ \/ // / /    / _ `/  ' \/ -_|_-<
/_/|_|\_,_/_//_/ /_/  /_/\__/_//_/\_,_/ /_/|_/\_,_/_/_/_/\__/___/

    menu titles for options.ini run items
    Restart CodeScriber for new settings to take effect
*/
var menu = {
    run1: "Run 1",
    run2: "Run 2",
    run3: "Run 3",
    run4: "Run 4"
};


/*
   ____         __
  / __/__  ____/ /__  ___ __ _________ ___
 / _// _ \/ __/ / _ \(_-</ // / __/ -_|_-<
/___/_//_/\__/_/\___/___/\_,_/_/  \__/___/

	change default surrounding tags here
    They are used with Ctrl-0,1,2,3, ... 9
    Change during session with Ctrl-g
    Restart CodeScriber for new settings to take effect
*/
var stag = ["<strong>,</strong>",
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
  ____             __
 /_  / ___ ___    / /____ ____ ____
  / /_/ -_) _ \  / __/ _ `/ _ `(_-<
 /___/\__/_//_/  \__/\_,_/\_, /___/
                         /___/

Type the tag and hit Ctrl-Z
Use fzen.py at command line to easily format new tags
then add to this array.

fzen.py
    format zen zen tag and append to tags.js file
USAGE:
1. open terminal
2. copy code into clipboard
3. python3 fzen.py
4. enter new tag name
5. [repeat] then check tags.js to verify
6. test new tags in codescriber

*/

const atags = {
"mdimage": '![alttext](http:// "title")',
"mdlink": '[linktext](http:// "title")',
"tk_entry": "self.vw = StringVar()\n w = Entry(self, textvariable=self.vw)\n w.grid(row=1, column=1, pady=20)\n #self.vw.set(\"Entry widget\")\n #self.vw.get()\n #w.select_range(0, END)\n #w.focus()\n\n",
"tk_button": "w = Button(self, text='button', command=self.cmdfunc)\n  w.grid(row=1, column=1, rowspan=1, columnspan=1, padx=4, pady=20)\n\n",
"tk_check": "self.vw = IntVar()\nw = Checkbutton(self, variable=self.vw, text='Checkbutton')\nw.grid(row=1, column=1, sticky='', pady=20)\n\n",
"tk_radio": "self.vVAR = StringVar()  # JUST ONE PER SET\nVAR = Radiobutton(PARENT, variable=self.vVAR, value='ON', text='On')\nVAR.grid(row=0,column=0, sticky='')  # sticky here keeps closer together\nself.vVAR.set('ON')\n\n",
}; //
