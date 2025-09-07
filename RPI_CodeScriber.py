#               END OF JS_API CLASS


def resize(window):
    ''' This code is only for Raspberry Pi
        to fix its initial screen rendering '''
    #print('Window size is ({0}, {1})'.format(window.width, window.height))
    time.sleep(1)
    neww = window.width + 1
    newh = window.height + 1
    window.resize(neww, newh)
    neww = window.width - 1
    newh = window.height - 1
    window.resize(neww, newh)
   # print('Window size is ({0}, {1})'.format(window.width, window.height))


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

    
    # webview.start()  # (debug=True)
    webview.start(resize, window)  # arguments for Raspberry Pi

