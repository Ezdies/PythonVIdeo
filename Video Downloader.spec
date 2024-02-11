# -*- mode: python ; coding: utf-8 -*-

application = Analysis(
    ["Source\\main.py"],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

archive = PYZ(application.pure)

executable = EXE(
    archive,
    application.scripts,
    [],
    exclude_binaries=True,
    name="Video Downloader",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

collection = COLLECT(
    executable,
    application.binaries,
    application.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name="Video Downloader",
)
