    function setFileMode(fname) {
        /*
        Add or change language choices and syntax color themes
        set theme on file load and (//gvar.setm) for tab switch
        */
      let ext;
        ext = fname.substring( fname.lastIndexOf(".") + 1 );
        // if (ext === "") {
        //     return;
        // }
        switch(ext) {
        case "c":
            editor.session.setMode("ace/mode/c_cpp");
            break;
        case "py":
            editor.session.setMode("ace/mode/python");
            break;
        case "js":
            editor.session.setMode("ace/mode/javascript");
            break;
        case "md":
            editor.session.setMode("ace/mode/markdown");
            break;
        case "json":
            editor.session.setMode("ace/mode/json");
            break;
        case "ini":
            editor.session.setMode("ace/mode/ini");
            break;
        case "sh":
            editor.session.setMode("ace/mode/sh");
            break;
        case "h":
            editor.session.setMode("ace/mode/c_cpp");
            break;
        case "html":
            editor.session.setMode("ace/mode/html");
            break;
        case "css":
            editor.session.setMode("ace/mode/css");
            break;
        case "go":
            editor.session.setMode("ace/mode/golang");
            break;
        case "rb":
            editor.session.setMode("ace/mode/ruby");
            break;
        case "sql":
            editor.session.setMode("ace/mode/sql");
            break;
        default:
            editor.session.setMode("ace/mode/text");
      }
    }
