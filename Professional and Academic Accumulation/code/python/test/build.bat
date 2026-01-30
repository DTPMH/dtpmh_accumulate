@echo off
REM MCTS C++ 快速编译脚本
REM 这个脚本会自动编译 mcts.cpp 并运行

setlocal enabledelayedexpansion

echo ===== MCTS C++ 编译和运行脚本 =====
echo.

REM 检查 g++ 是否可用
where g++ >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    echo [✓] 检测到 g++ 编译器
    echo.
    
    REM 编译
    echo [*] 正在编译 mcts.cpp...
    g++ -std=c++17 -o mcts.exe mcts.cpp
    
    if %ERRORLEVEL% EQU 0 (
        echo [✓] 编译成功！
        echo.
        
        REM 运行
        echo [*] 启动程序...
        echo.
        mcts.exe
    ) else (
        echo [✗] 编译失败！
        pause
        exit /b 1
    )
) else (
    echo [✗] 未找到 g++ 编译器
    echo.
    echo 请按照以下步骤安装 MinGW-w64：
    echo.
    echo 1. 访问 https://winlibs.com
    echo 2. 下载最新的 GCC (x86_64-posix-seh)
    echo 3. 解压到 C:\MinGW\
    echo 4. 将 C:\MinGW\bin 添加到系统 PATH
    echo 5. 重启 PowerShell 或 VS Code
    echo.
    echo 或者使用 Chocolatey 安装：
    echo   choco install mingw
    echo.
    pause
    exit /b 1
)

endlocal
