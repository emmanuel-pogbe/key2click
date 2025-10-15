; Minimal Key2Click Installer

[Setup]
AppName=Key2Click
AppVersion=1.0.0
DefaultDirName={autopf}\Key2Click
DefaultGroupName=Key2Click
OutputBaseFilename=Key2Click_Setup
OutputDir=output
SetupIconFile=click icon.ico
UninstallDisplayIcon={app}\Key2Click.exe

Compression=lzma2/max
SolidCompression=yes
WizardStyle=modern

; No admin rights needed
PrivilegesRequired=lowest

AppPublisher=Emmanuel Pogbe
AppPublisherURL=https://github.com/emmanuel-pogbe/key2click

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
; Desktop shortcut option
Name: "desktopicon"; Description: "Make a desktop shortcut"

[Files]
Source: "dist\Key2Click.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
; Start menu shortcuts 
Name: "{group}\Key2Click"; Filename: "{app}\Key2Click.exe"
Name: "{group}\Uninstall Key2Click"; Filename: "{uninstallexe}"

; Desktop shortcut
Name: "{autodesktop}\Key2Click"; Filename: "{app}\Key2Click.exe"; Tasks: desktopicon

[Run]
; Offer to launch after install
Filename: "{app}\Key2Click.exe"; Description: "Launch Key2Click"; Flags: nowait postinstall skipifsilent