#!/bin/python3

'''
Scan assigned folder and it's subfolder
1. link kicad_sym or lib or dcm to /home/[USER]/.local/share/kicad/[VER]/symbols
2. link subfolder [model_name].pretty to /home/[USER]/.local/share/kicad/[VER]/footprints
3. link subfolder [model_name].3dshapes to /home/[USER]/.local/share/kicad/[VER]/3dmodels
[optional]4. Add upper folders into kicad symbol and footprint
'''

'''
[usage]
lnk.py -s [src folder] -ov [target version] -op [target path]
'''

import shutil
import os, sys
import argparse

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="link source folder to target kicad version")
  parser.add_argument("-s", "--src-path", type=str, required=True, help="Soruce folder of kicad resources")
  parser.add_argument("-v", "--output-ver", type=str, help="Output kicad version")
  parser.add_argument("-p", "--output-path", type=str, help="Output kicad resource folder")

  args = parser.parse_args()

  if not (args.output_ver or args.output_path):
    print("Error: you must provide -v or -p")
    sys.exit(-1)
  elif (args.output_ver and args.output_path):
    print("Error: you cannot provide both of -v or -p")
    sys.exit(-1)

  print(args.src_path)
  if (args.output_path):
    print(args.output_path)
  if (args.output_ver):
    print(args.output_ver)