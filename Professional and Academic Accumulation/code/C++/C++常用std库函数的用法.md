<center><span style="font-size:2rem;font-weight:bold;">C++常用的std库函数的使用</span></center>

[toc]

<div style="page-break-after: always;"></div>

# std::lower_bound函数与std::upper_bound函数的使用

`std::lower_bound` 和 `std::upper_bound` 是 C++ 标准库中的两个函数，定义在 `<algorithm>` 头文件中，用于在已排序的区间中查找指定值的位置。两者之间的主要区别在于它们查找的元素的位置不同。

### 函数原型

#### `std::lower_bound`

```cpp
template< class ForwardIt, class T >
ForwardIt lower_bound(ForwardIt first, ForwardIt last, const T& value);
```

#### `std::upper_bound`

```cpp
template< class ForwardIt, class T >
ForwardIt upper_bound(ForwardIt first, ForwardIt last, const T& value);
```

### 参数
- **first, last**：指定待查找的区间的开始和结束迭代器，`[first, last)`。
- **value**：要查找的值。

### 返回值
- **`std::lower_bound`**：返回一个迭代器，指向第一个不小于 `value` 的元素。如果所有元素都小于 `value`，返回 `last`。
- **`std::upper_bound`**：返回一个迭代器，指向第一个大于 `value` 的元素。如果所有元素都不大于 `value`，返回 `last`。

### 示例代码
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::vector<int> vec = {1, 2, 4, 4, 5, 6, 8, 9};

    int value = 4;

    auto lower = std::lower_bound(vec.begin(), vec.end(), value);
    auto upper = std::upper_bound(vec.begin(), vec.end(), value);

    if (lower != vec.end()) {
        std::cout << "First element not less than " << value << " is " << *lower << std::endl;
    } else {
        std::cout << "No element not less than " << value << std::endl;
    }

    if (upper != vec.end()) {
        std::cout << "First element greater than " << value << " is " << *upper << std::endl;
    } else {
        std::cout << "No element greater than " << value << std::endl;
    }

    return 0;
}
```

### 代码解释
1. **包含头文件**：
   - `<iostream>` 用于输入输出。
   - `<vector>` 用于使用 `std::vector` 容器。
   - `<algorithm>` 用于使用算法函数，如 `std::lower_bound` 和 `std::upper_bound`。

2. **初始化向量**：
   - 创建一个已排序的整数向量 `vec`。

3. **调用 `std::lower_bound` 和 `std::upper_bound`**：
   - 调用 `std::lower_bound(vec.begin(), vec.end(), value)` 查找第一个不小于 `4` 的元素的迭代器 `lower`。
   - 调用 `std::upper_bound(vec.begin(), vec.end(), value)` 查找第一个大于 `4` 的元素的迭代器 `upper`。

4. **输出结果**：
   - 检查 `lower` 是否等于 `vec.end()`，如果不相等，输出该迭代器指向的元素值。
   - 检查 `upper` 是否等于 `vec.end()`，如果不相等，输出该迭代器指向的元素值。

### 注意事项
- 确保输入的区间是排序好的，否则 `std::lower_bound` 和 `std::upper_bound` 的行为是未定义的。
- 时间复杂度为 O(log N)，其中 N 是区间的长度。

### 总结
- **`std::lower_bound`** 查找的是第一个不小于指定值的位置。
- **`std::upper_bound`** 查找的是第一个大于指定值的位置。

这两个函数常用于在有序数据中高效地查找元素，特别是在需要进行二分查找或实现集合操作时。