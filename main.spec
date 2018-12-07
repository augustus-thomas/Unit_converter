# -*- mode: python -*-

block_cipher = None

added_files = [
	]

a = Analysis(['main.py'],
             pathex=['C:\\Windows\\WinSxS\\x86_microsoft-windows-m..namespace-downlevel_31bf3856ad364e35_10.0.17134.1_none_50c6cb8431e7428f', 'C:\\Users\\jesset\\Documents\\GitHub\\Unit_converter'],
             binaries=[],
             datas = added_files,
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
          [],
          exclude_binaries=True,
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='main')
