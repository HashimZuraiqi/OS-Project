@echo off
echo.
echo =====================================================
echo  CPU Scheduling Report Viewer Generator
echo =====================================================
echo.
echo  [1] Generate HTML (one-shot)
echo  [2] Watch mode   (auto-regenerate on MD changes)
echo.
set /p choice="Enter 1 or 2 (default 1): "

if "%choice%"=="2" (
    echo.
    echo Starting watch mode... open docs\REPORT_VIEWER.html in your browser.
    echo The page will auto-refresh every 3 seconds when you save the markdown.
    echo Press Ctrl+C to stop watching.
    echo.
    python scripts\update_report.py --watch
) else (
    echo.
    python scripts\update_report.py
    echo.
    echo Opening report in browser...
    start docs\REPORT_VIEWER.html
)
echo.
pause
