# -*- mode: python -*-

import os
import tinycss2
import cssselect2
import subprocess

version = subprocess.check_output("git describe").strip().decode()

block_cipher = None


a = Analysis(['run_app.py', 'build.spec'],
             binaries=[],
             pathex=['C:/Users/AA/ZZ'],
             datas=[
                 (os.path.join(os.path.dirname(tinycss2.__file__), 'VERSION'), 'tinycss2'),
                 (os.path.join(os.path.dirname(cssselect2.__file__), 'VERSION'), 'cssselect2'),
                 ('weather_reporter/img', 'weather_reporter/img')
             ],
             hiddenimports=['tinycss2'],
             win_no_prefer_redirects=False,
             win_private_assemblies=True,
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

name = 'SHEAR-Weather-Reporter-{}'.format(version)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name=name,
          upx=False,
          strip=False,
          console=True,
          debug=True)
