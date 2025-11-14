# MCTS 井字棋 C++ 版本 - 运行指南

## ❌ 问题
VS Code 无法编译和运行 C++ 代码，错误信息：
```
无法打开源文件 "iostream"
```

## ✅ 解决方案

### 方法 1：安装 MinGW-w64（推荐）

#### 第 1 步：下载 MinGW-w64
1. 访问 [MinGW-w64 官方网站](https://www.mingw-w64.org/)
2. 选择 "Installer" 或直接访问 [WinLibs.com](https://winlibs.com/)
3. 下载 GCC 最新版本（带 POSIX 线程模型）

#### 第 2 步：安装 MinGW
1. 运行安装程序，选择安装路径（如 `C:\MinGW\`）
2. 选择以下组件：
   - mingw32-base
   - mingw32-gcc-g++
   - msys-base

#### 第 3 步：配置系统环境变量
1. 打开"环境变量"：
   - Windows 10/11: 搜索"环境变量" → 编辑系统环境变量
   - 或按 Win+Pause → 高级系统设置

2. 在"系统变量"中编辑 `Path`：
   - 添加：`C:\MinGW\bin`（根据实际安装路径调整）

3. 验证安装：
   ```powershell
   g++ --version
   gdb --version
   ```

### 方法 2：使用 Visual Studio C++ 工具链

1. 安装 Visual Studio Community（带 C++ 工作负载）
2. VS Code 会自动检测到编译器

### 方法 3：使用在线编译器（快速测试）

如果不想安装编译器，可以使用在线 C++ 编译器：
- [Replit](https://replit.com)
- [OnlineGDB](https://www.onlinegdb.com)
- [Wandbox](https://wandbox.org)

复制 `mcts.cpp` 代码到在线编译器即可运行。

---

## 🚀 编译和运行

### 方法 A：使用 VS Code 任务

1. 确保 MinGW 已安装并配置到 PATH
2. 打开 `mcts.cpp`
3. 按 `Ctrl+Shift+B` 编译，或选择 Terminal → Run Build Task
4. 按 `Ctrl+F5` 运行程序

### 方法 B：手动编译

```powershell
# 在 PowerShell 中进入项目目录
cd "D:\Dtpmh_Accumulate\dtpmh_accumulate\Professional and Academic Accumulation\code\python\test"

# 编译
g++ -std=c++17 -o mcts.exe mcts.cpp

# 运行
.\mcts.exe
```

### 方法 C：使用 CMake（可选）

创建 `CMakeLists.txt`：
```cmake
cmake_minimum_required(VERSION 3.10)
project(MCTS)

set(CMAKE_CXX_STANDARD 17)
add_executable(mcts mcts.cpp)
```

编译：
```powershell
cmake -B build
cmake --build build
.\build\Debug\mcts.exe
```

---

## 📋 文件说明

- `mcts.cpp` - C++ MCTS 实现
- `.vscode/tasks.json` - VS Code 编译任务配置
- `.vscode/launch.json` - VS Code 调试配置
- `.vscode/c_cpp_properties.json` - C++ 编译器和 IntelliSense 配置

---

## 🐛 调试常见问题

### 问题 1：无法找到 iostream
**解决**：需要安装 MinGW-w64，配置 PATH

### 问题 2：g++ 命令未找到
**解决**：
```powershell
# 检查 g++ 是否可用
g++ --version

# 如果找不到，添加 MinGW 到 PATH
$env:Path += ";C:\MinGW\bin"
g++ --version
```

### 问题 3：编译错误 "无法打开文件"
**解决**：确保在正确的目录中运行编译命令，或使用绝对路径

---

## 🎮 程序说明

MCTS（蒙特卡洛树搜索）井字棋 AI：
- **X 玩家**：使用 MCTS 算法的 AI（强大）
- **O 玩家**：随机策略

程序会显示：
1. 当前棋盘状态
2. 搜索进度
3. 每个移动的访问次数和胜率
4. 最终游戏结果

---

## 💡 推荐配置

最简单的快速设置：
1. 下载 [WinLibs GCC](https://winlibs.com/) 的独立版本
2. 解压到 `C:\MinGW\`
3. 将 `C:\MinGW\bin` 添加到 PATH
4. 重启 VS Code

完成！现在就可以编译和运行了。
