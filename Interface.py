#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
from gi.repository import Gtk, Gio
from os import path
import subprocess
from subprocess import Popen
import themeChooser
class Handler:

    def __init__(self, fol):
        self.f = fol
        
    def on_mainWindow_quit(self, *args):
        Gtk.main_quit(*args)
        
    def on_comboboxAwesomeTheme_changed(self, widget):
        self.f.defineTheme(self.f.folderList[int(widget.get_active_id())])

    def on_buttonRestartAwesome_clicked(self, widget):
        p1 = Popen(["echo", "awesome.restart()"], stdout=subprocess.PIPE)
        p2 = Popen(["awesome-client"], stdin=p1.stdout, stdout=subprocess.PIPE)
        p1.stdout.close()
        output = p2.communicate()[0]

    def on_filechooserbutton1_file_changed(self, widget):
        self.f.rcLua = widget.get_filename()
        
        
def main():

    f = themeChooser.FolderListing()
    
    builder = Gtk.Builder()
    builder.add_from_file("ui.glade")
    builder.connect_signals(Handler(f))

    comboboxAwesomeTheme = builder.get_object("comboboxAwesomeTheme")
    
    i = 0
    indic = 0
    
    for name in f.folderList:
        if name+"/theme.lua" == f.actualTheme:
            indic = i
        comboboxAwesomeTheme.append(str(i), path.basename(name))
        i+=1


    comboboxAwesomeTheme.set_active(indic)

    filechooser =  builder.get_object("filechooserbuttonRcLua")

    fi = Gio.File.new_for_path(f.rcLua) 
    filechooser.set_file(fi)
    print(filechooser.get_file())
    window = builder.get_object("mainWindow")
    window.show_all()

    Gtk.main()



if  __name__ =='__main__':
    main()
