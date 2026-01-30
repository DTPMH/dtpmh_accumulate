<center><span style="font-size:2rem;font-weight:bold;">C++中Eigen的简单使用</span></center>

[toc]

<div style="page-break-after: always;"></div>

# Eigen的说明介绍



# Eigen中矩阵的创建与初始时化以及赋值操作



# Eigen中常用的矩阵类型





# Eigen中常用到函数以及用法

## Eigen::ArrayXf::LinSpaced函数用法

`Eigen::ArrayXf::LinSpaced` 是 Eigen 库中的一个函数，用于生成具有均匀间隔值的数组。它生成从起始值到结束值之间等间隔的数值。`ArrayXf` 是表示浮点数一维数组的类型。

下面是一个示例，展示如何使用 `LinSpaced` 函数：

```cpp
#include <iostream>
#include <Eigen/Dense>

int main() {
    // 定义生成数组的大小、起始值和结束值
    int size = 10;
    float start = 0.0f;
    float end = 1.0f;

    // 使用 LinSpaced 函数生成等间隔数组
    Eigen::ArrayXf array = Eigen::ArrayXf::LinSpaced(size, start, end);

    // 打印生成的数组
    std::cout << "Generated array: \n" << array << std::endl;

    return 0;
}
```

在这个示例中：

1. 包含 `Eigen/Dense` 头文件，使用 Eigen 库的密集矩阵和数组功能。
2. 定义了生成数组的大小 (`size`)、起始值 (`start`) 和结束值 (`end`)。
3. 使用 `Eigen::ArrayXf::LinSpaced` 函数生成一个从 `start` 到 `end` 间隔的大小为 `size` 的数组。
4. 打印生成的数组。

运行这段代码后，将生成一个从 0.0 到 1.0 之间等间隔的 10 个浮点数值数组，并打印到控制台。

`LinSpaced` 函数的参数如下：
- `size`：数组的大小，即要生成的元素数量。
- `start`：数组的第一个元素的值。
- `end`：数组的最后一个元素的值。

这对于需要生成线性分布的数据（如在数值计算、数据分析或绘图中）非常有用。