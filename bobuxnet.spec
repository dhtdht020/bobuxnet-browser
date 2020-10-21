# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['bobuxnet.py'],
             binaries=[],
             datas=[('gui/assets/elements/heading.png', './gui/assets/elements/'),
                    ('gui/assets/elements/label.png', './gui/assets/elements/'),
                    ('gui/assets/elements/spacer.png', './gui/assets/elements/'),
                    ('gui/assets/elements/type/alignment.png', './gui/assets/elements/type/'),
                    ('gui/assets/elements/type/bold.png', './gui/assets/elements/type/'),
                    ('gui/assets/elements/type/font_size.png', './gui/assets/elements/type/'),
                    ('gui/assets/elements/type/height.png', './gui/assets/elements/type/'),
                    ('gui/assets/elements/type/text.png', './gui/assets/elements/type/'),
                    ('gui/assets/elements/type/link.png', './gui/assets/elements/type/'),
                    ('gui/assets/elements/horizontal_line.png', './gui/assets/elements/'),
                    ('gui/assets/elements/link.png', './gui/assets/elements/')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='bobuxnet_browser',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True)
