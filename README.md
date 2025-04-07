# CodeScriber

## A Desktop Code Editor for Linux and Windows

__Uses "web app" technology via Python, pywebview, Ace Code Editor API__

>![CodeScriber](images/CS1.png "CodeScriber")

CodeScriber uses the "Ace" Code Editor - a Javascript library.

For detailed information about "Ace" visit the 
[Ace website](https://ace.c9.io/ "https://ace.c9.io/")

* The entire application runs locally on the user's machine, which is great for privacy and performance.  
* External dependencies include the Ace library loaded from cdnjs.cloudflare.com and an AI feature that requires an Internet connection.  
* The application is primarily implemented in scripting languages: HTML, CSS, JavaScript, and Python3, making it flexible and easy to modify.  
* The editor component is implemented as a Python script that uses the pywebview module to communicate with a JavaScript-based GUI (leveraging the Gtk WebKit2 engine on Linux and edgechromium on Windows). This design effectively bridges the gap between native host capabilities and a modern web-based interface.

_See_ <a href='https://ace.c9.io/'>https://ace.c9.io</a> _for information on the Ace Code Editor._

[Documentation](CSdoc.md "CodeScriber Documentation")

### Features:

- Syntax highlighting
- Multi Session Interface
- AI access built-in (requires Internet)
- Auto indentation and outdent
- An optional command line
- Work with large documents (handles hundreds of thousands of lines without issue)
- Fully customizable key bindings including vi and Emacs modes
- Themes and many language models
- Search and replace with regular expressions
- Highlight matching parentheses
- Toggle between soft tabs and real tabs
- Displays hidden characters
- Highlight selected word
- Multiple cursor selection
- Column select and edit mode
- Customizable Keyword code snipits
- Drag & Drop to open file
- Markdown
- Spell check
- Find File
- Sort
- Recent Files
- Context Menu
- Optional file backups
- Snipit Management

[Documentation](CSdoc.md "CodeScriber Documentation")

### CodeScriber combines the following technologies:
> - python (pywebview, markdown, tkinter.ttk)
> - javascript
> - API (ace.js)
> - css
> - html

### Default language modes:
> _python, c, html, css, markdown, javascript, bash, sql, golang, json_  
Modify this list in `filemodes.js` - see **File Modes** under Options menu.

>![diagram](images/CSdiag.png "Conceptual")

[Documentation](CSdoc.md "CodeScriber Documentation")

---

