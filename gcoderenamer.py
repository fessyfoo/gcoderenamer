#!/usr/bin/env python

from __future__ import print_function
import argparse
import os.path
import re

parser = argparse.ArgumentParser(
    description='extract print time comments from gcode and rename the file' +
        ' note this currently works with Slic3r PE gcode')

parser.add_argument(
    '--dry-run', '-n',  
    action = 'store_true',
    help   = "don't actually rename filenames"
)

parser.add_argument(
    'filename',
    nargs  = '+',
    help   = 'the filename(s) to operate on'
)
args = parser.parse_args()

# Slic3r PE gcode example: 
#; filament used = 15355.7mm (36.9cm3)
#; filament used = 46.2
#; filament cost = 2.0
#; total filament cost = 2.0
#; estimated printing time (normal mode) = 4h 8m 40s

re_slic3r_pe_print_time = re.compile('^; estimated printing time.*= (.*)')


def make_label(filename):
    try:
      f = open(filename,'r')
    except IOError as i:
        print("error: %s %s" % (i.strerror, i.filename))
        close(f)
        return

    with f:
        for line in f:
            m = re.match(re_slic3r_pe_print_time, line)
            if m:
                return m.group(1).replace(' ','')


def newname(filename, label):
    root, ext = os.path.splitext(filename)
    _, _ext = os.path.splitext(root)

    if not label:
        return filename

    if _ext == "." + label:
        return filename

    return "%s.%s%s" % (root, label, ext)


def process_file(filename):
    dry_run = "(dry run) Would " if args.dry_run else ""

    label       = make_label(filename)
    newfilename = newname(filename, label)

    if newfilename != filename:
        print("%sRename:" % dry_run)
        print("  %s" % filename)
        print("  %s" % newfilename)

        if not args.dry_run:
            os.rename(filename, newfilename)

for filename in args.filename:
    process_file(filename)
