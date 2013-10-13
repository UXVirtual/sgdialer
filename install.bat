@ECHO OFF
CLS
ECHO pygame 1.9.1 or higher is required. Download and install the
ECHO appropriate binary from http://www.pygame.org/download.shtml
ECHO before continuing.
ECHO.
ECHO ============================================================
ECHO.
ECHO 1. Install other dependencies (default).
ECHO 2. Quit.
ECHO.
ECHO ============================================================
ECHO.
CHOICE /C 1234 /N /T 10 /D 1 /M "Please choose a menu option."
IF ERRORLEVEL == 2 GOTO QUIT_MENU
IF ERRORLEVEL == 1 GOTO RUN_INSTALL
:RUN_INSTALL
ECHO.
ECHO Installing dependencies...
ECHO.
c:\Python27\Scripts\pip.exe install xmltodict
ECHO.
PAUSE
:QUIT_MENU