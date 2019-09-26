# -*- mode: python ; coding: utf-8 -*-

block_cipher = None
specpath = os.path.dirname(os.path.abspath(SPEC))

a = Analysis(['fp.py'],
             pathex=['C:\\Users\\jeffw\\Documents\\code\\fp'],
             binaries=[],
             datas=[ ('C:\\Users\\jeffw\\Documents\\code\\fp\\fpicon_64.ico', '.') ],
             hiddenimports=['wx._adv', 'wx._html'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='fp',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False, icon = os.path.join(specpath, 'C:\\Users\\jeffw\\Documents\\code\\fp\\fpicon_64.ico'))