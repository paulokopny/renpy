﻿# Copyright 2004-2016 Tom Rothamel <pytom@bishoujo.us>
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from gui7.code import CodeGenerator
from gui7.images import ImageGenerator
from gui7.parameters import GuiParameters

import renpy.arguments
import os


def generate_gui_command():

    ap = renpy.arguments.ArgumentParser()

    ap.add_argument("target", action="store", help="The game into which the generated gui should be placed.")
    ap.add_argument("--width", default=1280, action="store", type=int, help="The width of the generated gui.")
    ap.add_argument("--height", default=720, action="store", type=int, help="The height of the generated gui.")
    ap.add_argument("--accent", default="#00b8c3", action="store", help="The accent color used throughout the gui.")
    ap.add_argument("--boring", default="#000000", action="store", help="The boring color used for the gui background.")
    ap.add_argument("--light", default=False, action="store_true", help="True if this is considered a light theme.")
    ap.add_argument("--overwrite-images", default=False, action="store_true", help="True if existing images should be overwritten.")
    ap.add_argument("--overwrite-code", default=False, action="store_true", help="True if an existing gui.rpy file should be overwritten.")
    ap.add_argument("--source", default="interface_7/game/gui.rpy", action="store", help="The source code for the gui file.")

    args = ap.parse_args()

    prefix = os.path.join(args.target, "game")

    if not os.path.isdir(prefix):
        ap.error("{} does not appear to be a Ren'Py game.".format(prefix))

    p = GuiParameters(
        prefix,
        args.width,
        args.height,
        args.accent,
        args.boring,
        args.light)

    ImageGenerator(p, args.overwrite_images).generate_all()
    CodeGenerator(p, args.source, args.overwrite_code).generate()


renpy.arguments.register_command("generate_gui", generate_gui_command)






