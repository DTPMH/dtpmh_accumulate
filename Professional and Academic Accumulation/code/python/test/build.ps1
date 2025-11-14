# MCTS C++ 快速编译脚本 (PowerShell 版本)
# 用法: 在 PowerShell 中运行: .\build.ps1

Write-Host "===== MCTS C++ 编译和运行脚本 =====" -ForegroundColor Cyan
Write-Host ""

# 检查 g++ 是否可用
$gppPath = (Get-Command g++ -ErrorAction SilentlyContinue).Path

if ($gppPath) {
    Write-Host "[✓] 检测到 g++ 编译器" -ForegroundColor Green
    Write-Host "路径: $gppPath"
    Write-Host ""
    
    # 编译
    Write-Host "[*] 正在编译 mcts.cpp..." -ForegroundColor Yellow
    & g++ -std=c++17 -o mcts.exe mcts.cpp
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "[✓] 编译成功！" -ForegroundColor Green
        Write-Host ""
        
        # 运行
        Write-Host "[*] 启动程序..." -ForegroundColor Yellow
        Write-Host ""
        & .\mcts.exe
    } else {
        Write-Host "[✗] 编译失败！" -ForegroundColor Red
        Write-Host "请检查代码中是否有错误"
        exit 1
    }
} else {
    Write-Host "[✗] 未找到 g++ 编译器" -ForegroundColor Red
    Write-Host ""
    Write-Host "请按照以下步骤安装 MinGW-w64："
    Write-Host ""
    Write-Host "方法 1：使用 Chocolatey（推荐）" -ForegroundColor Cyan
    Write-Host "  1. 打开 PowerShell (以管理员身份)"
    Write-Host "  2. 运行: choco install mingw"
    Write-Host ""
    Write-Host "方法 2：手动下载" -ForegroundColor Cyan
    Write-Host "  1. 访问: https://winlibs.com"
    Write-Host "  2. 下载最新的 GCC (x86_64-posix-seh)"
    Write-Host "  3. 解压到: C:\MinGW\"
    Write-Host "  4. 将 C:\MinGW\bin 添加到系统 PATH"
    Write-Host ""
    Write-Host "方法 3：在线编译" -ForegroundColor Cyan
    Write-Host "  1. 访问: https://replit.com 或 https://onlinegdb.com"
    Write-Host "  2. 复制 mcts.cpp 代码并在线编译"
    Write-Host ""
    Write-Host "完成安装后，重新运行此脚本。"
    exit 1
}
