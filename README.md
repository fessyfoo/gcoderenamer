
# gcoderenamer

prototype script to extract [PrusaSlicer/Slic3r PE][1] timing information from a gcode file
and rename that gcode file with the timing info

could be extended to grab other metadata from in the gcode file.

Note that [PrusaSlicer/Slic3r PE][1] as of 1.42 (alpha)
[supports new template variables in the output filename][2] which 
let you do this right from the start.

## example run:
```
% ./gcoderenamer.py -n ./gcode/*
(dry run) Would Rename:
  ./gcode/test.gcode
  ./gcode/test.4h8m40s.gcode
(dry run) Would Rename:
  ./gcode/test.gcode
  ./gcode/test.4h8m40s.gcode
```


## usage
```
usage: gcoderenamer.py [-h] [--dry-run] filename [filename ...]

extract print time comments from gcode and rename the file note this currently
works with Slic3r PE gcode

positional arguments:
  filename       the filename(s) to operate on

  optional arguments:
    -h, --help     show this help message and exit
      --dry-run, -n  don't actually rename filenames

```

[1]: https://github.com/prusa3d/PrusaSlicer/
[2]: https://github.com/prusa3d/PrusaSlicer/issues/922

