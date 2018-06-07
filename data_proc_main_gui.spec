# -*- mode: python -*-

block_cipher = None


a = Analysis(['data_proc_main_gui.py'],
             pathex=['D:\\Leo-Camera-Software\\common-useful\\Python-Learn\\PycharmProjects\\Tensorflow-Helloworld'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='data_proc_main_gui',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='test01-csv-icon.ico')
