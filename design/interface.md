# MATTE INTERFACE

[Back to README](../README.md)

## INPUTS

### COMMAND LINE INTERFACE

Something like:

`> matte.py -i “path/to/input.json” -o “/somewhere/there”`

|Flags|Flags (short)|Example value|
|---|---|---|
|--input|-i|“path/to/input.json”|
|--outpath|-o|“path/to/directory”|
|--config|-c|“path/to/config.json”|

The `input.json` file would contain info from the user:

- Scripture section – starting verse and/or ending verse
- Options
    + Languages
    + Styling options
    + Output data types

## OUTPUTS

The following output files will be packaged into a single .ZIP

- .TXT (plain text)
- .MD (markdown text)
- .HTML (document)
- .SVG (image)
