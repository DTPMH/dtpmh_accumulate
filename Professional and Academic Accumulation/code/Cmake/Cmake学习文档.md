<center><span style="font-size:2rem;font-weight:bold;">CMake 学习文档</span></center>

<div style="page-break-after: always;"></div>

[toc]

<div style="page-break-after: always;"></div>

# 一、综述

CMake 是一个**跨平台的自动化构建系统生成器**，它不会直接编译代码，而是生成具体平台的构建脚本，例如：

- Linux → 生成 `Makefile`
- Windows → 生成 `.sln`（Visual Studio 工程）
- macOS → 生成 Xcode 工程

CMake 的目标是：
- **统一构建配置方式**
- **让大型项目易于维护**
- **管理依赖与第三方库**
- **支持多平台和多编译器**

CMake 的配置文件名为 **`CMakeLists.txt`**，每个子目录都可以有一个。  
CMake 读取它们以构建完整的依赖图。

---

# 二、基础框架

最小示例：

```cmake
cmake_minimum_required(VERSION 3.20)    # 指定CMake最小版本
project(hello LANGUAGES CXX)            # 定义项目名称与语言
add_executable(hello main.cpp)          # 构建一个可执行文件
```

执行：

```bash
mkdir build && cd build
cmake ..
make
./hello
```

---

# 三、核心命令详解

以下命令涵盖常见构建场景，配有详细解释、用法示例和最佳实践建议。

---

## 1️⃣ cmake_minimum_required()

**作用**：告诉 CMake 需要的最低版本。
必须放在顶层 `CMakeLists.txt` 的第一行。

```cmake
cmake_minimum_required(VERSION 3.15)
```

> 💡 **小贴士**：
> 写高一点版本有好处，可以用上现代语法和新特性（如 `target_compile_features`）。

---

## 2️⃣ project()

**作用**：定义项目名称、版本、语言类型。

```cmake
project(MyProject VERSION 1.2.0 LANGUAGES CXX)
```

CMake 自动生成以下变量：

| 变量                    | 含义         |
| ----------------------- | ------------ |
| `${PROJECT_NAME}`       | 项目名称     |
| `${PROJECT_VERSION}`    | 项目版本号   |
| `${PROJECT_SOURCE_DIR}` | 源码根路径   |
| `${PROJECT_BINARY_DIR}` | 构建输出路径 |

---

## 3️⃣ set()

**作用**：定义变量（就像定义全局常量）。

```cmake
set(SRC_FILES main.cpp util.cpp)
set(CMAKE_CXX_STANDARD 17)
```

> 📘 **技巧**：
> 变量区分大小写。访问时使用 `${VAR_NAME}`。

---

## 4️⃣ message()

**作用**：打印调试或提示信息。

```cmake
message(STATUS "CMake Version: ${CMAKE_VERSION}")
message(WARNING "Debug mode only!")
```

输出级别：

| 级别        | 效果             |
| ----------- | ---------------- |
| STATUS      | 普通提示（绿色） |
| WARNING     | 警告             |
| SEND_ERROR  | 不中断但标记错误 |
| FATAL_ERROR | 立即中止 CMake   |

---

## 5️⃣ add_executable()

**作用**：生成可执行文件目标。

```cmake
add_executable(demo main.cpp util.cpp)
```

> 💡 **相当于**：告诉 CMake，“请帮我编译出一个叫 demo 的可执行程序，用这些源文件组成。”

---

## 6️⃣ add_library()

**作用**：创建一个静态或动态库。

```cmake
add_library(math STATIC math.cpp)
add_library(core SHARED core.cpp)
```

类型说明：

| 类型   | 说明                     |
| ------ | ------------------------ |
| STATIC | 生成 `.a` 静态库         |
| SHARED | 生成 `.so` 动态库        |
| MODULE | 插件库（运行时动态加载） |

---

## 7️⃣ target_link_libraries()

**作用**：指定目标要链接的库。

```cmake
target_link_libraries(demo PRIVATE math pthread)
```

作用域说明：

| 关键字    | 含义                         |
| --------- | ---------------------------- |
| PRIVATE   | 仅当前目标使用               |
| PUBLIC    | 当前目标及依赖它的目标都可见 |
| INTERFACE | 仅对依赖的目标可见           |

---

## 8️⃣ include_directories()

**作用**：指定头文件搜索路径（相当于 `g++ -I`）。

```cmake
include_directories(${PROJECT_SOURCE_DIR}/include)
```

> ⚠️ 建议在现代CMake中使用：

```cmake
target_include_directories(target PRIVATE include)
```

---

## 9️⃣ link_directories()

**作用**：添加库文件的搜索路径（相当于 `g++ -L`）。

```cmake
link_directories(${PROJECT_SOURCE_DIR}/lib)
```

---

## 🔟 add_definitions()

**作用**：向编译器添加宏定义（相当于 `-D`）。

```cmake
add_definitions(-DUSE_DEBUG -DVERSION=3)
```

> ⚠️ 推荐现代写法：

```cmake
target_compile_definitions(app PRIVATE USE_DEBUG VERSION=3)
```

---

## 11️⃣ add_subdirectory()

**作用**：递归地包含子目录中的 CMakeLists.txt。

```cmake
add_subdirectory(src)
add_subdirectory(test)
```

> 💡 就像“调用子工程”。父项目会自动知道子项目的目标。

---

## 12️⃣ target_compile_options()

**作用**：为指定目标添加编译选项。

```cmake
target_compile_options(app PRIVATE -Wall -O3)
```

---

## 13️⃣ find_package()

**作用**：查找系统或第三方库。

```cmake
find_package(Eigen3 REQUIRED)
include_directories(${EIGEN3_INCLUDE_DIR})
```

> 🔍 CMake 会在 `/usr/share/cmake*/Modules` 下寻找对应的 `FindEigen3.cmake`。

---

## 14️⃣ file()

**作用**：操作文件和目录。

```cmake
file(GLOB SRC_FILES src/*.cpp)
file(MAKE_DIRECTORY ${PROJECT_BINARY_DIR}/output)
```

子命令：

| 功能     | 示例                             |
| -------- | -------------------------------- |
| 读文件   | `file(READ config.txt VAR)`      |
| 写文件   | `file(WRITE output.txt "hello")` |
| 匹配文件 | `file(GLOB SRC src/*.cpp)`       |

---

## 15️⃣ install()

**作用**：定义安装规则（例如 `make install` 时执行）。

```cmake
install(TARGETS app DESTINATION bin)
install(FILES config.ini DESTINATION etc)
```

---

## 16️⃣ configure_file()

**作用**：根据模板生成配置文件。

```cmake
configure_file(config.in config.h)
```

`config.in` 中可写：

```text
#define VERSION "@PROJECT_VERSION@"
```

生成的 `config.h` 会自动替换。

---

## 17️⃣ option()

**作用**：提供可开关的配置选项（布尔变量）。

```cmake
option(ENABLE_LOG "Enable logging system" ON)

if(ENABLE_LOG)
  add_definitions(-DENABLE_LOG)
endif()
```

---

## 18️⃣ foreach() / endforeach()

**作用**：循环结构。

```cmake
foreach(file IN LISTS SRC_FILES)
  message(STATUS "File: ${file}")
endforeach()
```

---

## 19️⃣ while() / endwhile()

**作用**：循环执行条件为真时的命令。

```cmake
set(i 0)
while(i LESS 5)
  message(STATUS "i = ${i}")
  math(EXPR i "${i}+1")
endwhile()
```

---

## 20️⃣ list()

**作用**：操作列表变量。

```cmake
set(my_list a b c)
list(APPEND my_list d)
message(STATUS "List: ${my_list}")
```

---

## 21️⃣ math()

**作用**：执行整数计算。

```cmake
math(EXPR SUM "3 + 5")
message(STATUS "SUM = ${SUM}")
```

---

## 22️⃣ execute_process()

**作用**：执行系统命令并获取结果。

```cmake
execute_process(COMMAND ls OUTPUT_VARIABLE files)
message(STATUS "Files: ${files}")
```

---

## 23️⃣ add_custom_command()

**作用**：添加自定义构建命令。

```cmake
add_custom_command(
  OUTPUT generated.cpp
  COMMAND python gen_code.py
  DEPENDS gen_code.py
)
```

---

## 24️⃣ add_custom_target()

**作用**：添加自定义目标，不生成实际文件。

```cmake
add_custom_target(clean_cache COMMAND rm -rf CMakeCache.txt)
```

---

## 25️⃣ include()

**作用**：加载其他 `.cmake` 文件（类似 C++ 的 `#include`）。

```cmake
include(${PROJECT_SOURCE_DIR}/cmake/Utils.cmake)
```

---

## 26️⃣ find_file() / find_library()

**作用**：查找特定文件或库。

```cmake
find_file(CONFIG_FILE myconfig.yaml PATHS /etc /usr/local/etc)
find_library(MATH_LIB m PATHS /usr/lib)
```

---

## 27️⃣ get_filename_component()

**作用**：从路径中提取部分信息。

```cmake
get_filename_component(PARENT_DIR ${CMAKE_SOURCE_DIR} DIRECTORY)
```

---

## 28️⃣ catkin_package() （ROS）

**作用**：在 ROS 中导出包依赖信息。

```cmake
catkin_package(
  INCLUDE_DIRS include
  LIBRARIES my_node
  CATKIN_DEPENDS roscpp std_msgs
)
```

---

## 29️⃣ export() / install(EXPORT)

**作用**：导出目标供其他项目使用。

```cmake
install(EXPORT MyTargets DESTINATION share/MyProject/cmake)
```

---

## 30️⃣ find_path() / find_program()

**作用**：查找路径或程序。

```cmake
find_path(EIGEN_INCLUDE_DIR Eigen/Core)
find_program(GIT_EXECUTABLE git)
```

---

# 四、项目结构实例

## ✅ 单文件项目

```
hello/
 ├── main.cpp
 └── CMakeLists.txt
```

```cmake
cmake_minimum_required(VERSION 3.15)
project(hello)
add_executable(hello main.cpp)
```

---

## ✅ 多文件项目

```
multi/
 ├── CMakeLists.txt
 ├── add.cpp
 ├── add.h
 └── main.cpp
```

```cmake
cmake_minimum_required(VERSION 3.15)
project(multi)
set(SRC main.cpp add.cpp)
add_executable(multi ${SRC})
include_directories(${PROJECT_SOURCE_DIR})
```

---

## ✅ 大型工程示例

```
project_root/
 ├── include/
 │   └── app.h
 ├── lib/
 │   ├── math.cpp
 │   └── CMakeLists.txt
 ├── src/
 │   ├── main.cpp
 │   └── CMakeLists.txt
 └── CMakeLists.txt
```

**顶层 CMakeLists.txt**

```cmake
cmake_minimum_required(VERSION 3.15)
project(big_project LANGUAGES CXX)
set(CMAKE_CXX_STANDARD 17)

include_directories(${PROJECT_SOURCE_DIR}/include)
add_subdirectory(lib)
add_subdirectory(src)
```

**lib/CMakeLists.txt**

```cmake
add_library(math STATIC math.cpp)
target_include_directories(math PUBLIC ${PROJECT_SOURCE_DIR}/lib)
```

**src/CMakeLists.txt**

```cmake
file(GLOB SRC_FILES *.cpp)
add_executable(main ${SRC_FILES})
target_link_libraries(main PRIVATE math)
```

---

# 五、常用内置变量速查表

| 变量名                   | 说明                      |
| ------------------------ | ------------------------- |
| `PROJECT_NAME`           | 当前项目名称              |
| `CMAKE_SOURCE_DIR`       | 顶层源文件路径            |
| `CMAKE_BINARY_DIR`       | 构建输出路径              |
| `CMAKE_BUILD_TYPE`       | 构建类型（Debug/Release） |
| `CMAKE_CXX_COMPILER`     | 使用的C++编译器           |
| `CMAKE_CXX_FLAGS`        | 全局C++编译标志           |
| `EXECUTABLE_OUTPUT_PATH` | 可执行文件输出路径        |
| `LIBRARY_OUTPUT_PATH`    | 库文件输出路径            |
| `CMAKE_INSTALL_PREFIX`   | 安装前缀目录              |

---

# 六、总结

CMake 是 C/C++ 世界中最通用的构建系统配置工具。
它的强大之处在于：

* **模块化构建**（add_subdirectory）
* **灵活条件判断**
* **跨平台支持**
* **第三方库自动查找**
* **一键安装与导出**

> 🌟 **学习建议**：
>
> 1. 优先使用现代写法（target_ 系列命令）
> 2. 多用 message() 调试
> 3. 结合 `ccmake` 或 `cmake-gui` 查看变量配置
> 4. 多读优秀开源项目的 CMakeLists（如 ROS、OpenCV）

---

```

---

是否希望我现在直接把这份 **Markdown 文档导出为精美 PDF 文件**（带封面、目录分页和代码高亮）？  
我可以直接帮你生成。
```