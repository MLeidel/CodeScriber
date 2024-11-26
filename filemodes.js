    function setFileMode(fname) {
        /*
        Add or change language choices and syntax color themes
        set theme on file load and (gvar.setm) for tab switch
        */
      let ext;
        ext = fname.substring( fname.lastIndexOf(".") + 1 );
        // if (ext === "") {
        //     return;
        // }
        /*                      COLOR THEMES
            monokai  cobalt  vibrant_ink  clouds_midnight  solarized_dark
            tomorrow_night_eighties  twilight  kr_theme  Terminal
            solarized_light  textmate  tomorrow_night  twilight
        */
        switch(ext) {
        case "c":
            editor.session.setMode("ace/mode/c_cpp");
            editor.setTheme("ace/theme/monokai");
            gvar.setm[gvar.sinx] = "ace/theme/monokai";
            break;
        case "py":
            editor.session.setMode("ace/mode/python");
            editor.setTheme("ace/theme/twilight");
            gvar.setm[gvar.sinx] = "ace/theme/twilight";
            break;
        case "js":
            editor.session.setMode("ace/mode/javascript");
            editor.setTheme("ace/theme/monokai");
            gvar.setm[gvar.sinx] = "ace/theme/monokai";
            break;
        case "md":
            editor.session.setMode("ace/mode/markdown");
            editor.setTheme("ace/theme/solarized_dark");
            gvar.setm[gvar.sinx] = "ace/theme/solarized_dark";
            break;
        case "json":
            editor.session.setMode("ace/mode/json");
            editor.setTheme("ace/theme/cobalt");
            gvar.setm[gvar.sinx] = "ace/theme/cobalt";
            break;
        case "ini":
            editor.session.setMode("ace/mode/ini");
            editor.setTheme("ace/theme/clouds_midnight");
            gvar.setm[gvar.sinx] = "ace/theme/clouds_midnight";
            break;
        case "sh":
            editor.session.setMode("ace/mode/sh");
            editor.setTheme("ace/theme/terminal");
            gvar.setm[gvar.sinx] = "ace/theme/terminal";
            break;
        case "h":
            editor.session.setMode("ace/mode/c_cpp");
            editor.setTheme("ace/theme/twilight");
            gvar.setm[gvar.sinx] = "ace/theme/twilight";
            break;
        case "html":
            editor.session.setMode("ace/mode/html");
            editor.setTheme("ace/theme/tomorrow_night");
            gvar.setm[gvar.sinx] = "ace/theme/tomorrow_night";
            break;
        case "css":
            editor.session.setMode("ace/mode/css");
            editor.setTheme("ace/theme/solarized_dark");
            gvar.setm[gvar.sinx] = "ace/theme/solarized_dark";
            break;
        case "go":
            editor.session.setMode("ace/mode/golang");
            editor.setTheme("ace/theme/twilight");
            gvar.setm[gvar.sinx] = "ace/theme/twilight";
            break;
        case "rb":
            editor.session.setMode("ace/mode/ruby");
            editor.setTheme("ace/theme/monokai");
            gvar.setm[gvar.sinx] = "ace/theme/monokai";
            break;
        case "sql":
            editor.session.setMode("ace/mode/sql");
            editor.setTheme("ace/theme/monokai");
            gvar.setm[gvar.sinx] = "ace/theme/monokai";
            break;
        default:
            editor.session.setMode("ace/mode/text");
            editor.setTheme("ace/theme/GitHub");
            gvar.setm[gvar.sinx] = "ace/theme/GitHub";
      }
    }
