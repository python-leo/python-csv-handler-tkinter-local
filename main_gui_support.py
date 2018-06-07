#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    May 05, 2018 12:31:24 PM


try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True


def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top


def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None


if __name__ == '__main__':
    import data_proc_main_gui

    data_proc_main_gui.vp_start_gui()
