# MameListGenerator

Utility for pulling arcade game metadata from a couple of source files and generating a rom/gamelist for either Attract Mode or EmulationStation based on a supplied set of ROM names. Designed to work with MAME's XML file and catver.ini

Usage:

```
python generate-gamelist.py
    
Parameters:
    -i  : Input file (list of ROMS)                 - REQUIRED
    -m  : MAME XML file                             - REQUIRED
    -c  : catver.ini file                           - REQUIRED
    -f  : Output file format (options: es or am)    - REQUIRED
    -r  : ROM output path prefix                    - OPTIONAL - EmulationStation mode only
    -p  : Image output path prefix                  - OPTIONAL - EmulationStation mode only
    -z  : ROM file extension                        - OPTIONAL - EmulationStation mode only
    -y  : Image file extension                      - OPTIONAL - EmulationStation mode only
```
