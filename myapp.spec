# myapp.spec

# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['app.py'],  # Cambia 'app.py' al nombre del archivo principal de tu aplicación.
             pathex=['path/to/your/scripts'],  # Reemplaza 'path/to/your/scripts' con la ruta a tus scripts.
             binaries=[],
             datas=[('estado_ez.txt', '.')],  # Añade otros archivos necesarios aquí.
             ...
             )

pyz = PYZ(a.pure, a.zipped_data,
          cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          [],
          name='myapp',  # Nombre del ejecutable final.
          debug=False,
          bootloader_ignore_signals=False,
          bootloader_silent=False,
          ...

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               upx_include=[],
               name='myapp')  # Nombre del directorio de salida.

