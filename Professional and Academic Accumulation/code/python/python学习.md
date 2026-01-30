<center><span style="font-size:2rem;font-weight:bold;">Python入门学习</span></center>

[toc]

<div style="page-break-after: always;"></div>

# python文件的书写

python代码文件需要标注为.py的文件

文本里面加入一行

```python
#!/usr/bin/env python3

```

在 Python 脚本的第一行加入 `#!/usr/bin/env python3` 是一种称为 shebang 或 hashbang 的行，主要用于 Unix 和 Unix-like 操作系统（如 Linux 和 macOS）。这行代码的作用是告诉系统如何执行这个脚本。具体解释如下：

### 解释

1. **Shebang 行**：这行代码以 `#!` 开头，称为 shebang。shebang 行告诉系统这个文件应该使用哪个解释器来执行。

2. **`/usr/bin/env`**：`env` 是一个 Unix 实用程序，用于在修改环境的同时运行另一个程序。在这种情况下，它用于定位 `python3` 解释器的路径。使用 `env` 的好处是，它会根据用户的环境变量 `PATH` 查找 `python3`，从而找到适当的解释器。这比直接指定解释器路径（如 `#!/usr/bin/python3`）更灵活，因为解释器的位置可能因系统配置不同而变化。

3. **`python3`**：这是指向 Python 3 解释器的路径。通过使用 `python3`，明确指示该脚本应由 Python 3 解释器执行，而不是 Python 2。

### 作用

在脚本文件的顶部包含这行 shebang 行，具有以下作用：

- **可执行性**：使脚本文件可以直接作为可执行文件运行，而无需明确调用 Python 解释器。这样，你可以通过在命令行中输入脚本文件名来执行它，而无需显式调用 Python 解释器。
  
- **解释器指定**：确保脚本使用正确的 Python 版本进行解释和执行，避免 Python 2 和 Python 3 之间的兼容性问题。

### 示例

假设有一个名为 `myscript.py` 的 Python 脚本，内容如下：

```python
#!/usr/bin/env python3

print("Hello, world!")
```

#### 步骤：

1. **确保文件具有执行权限**：

```sh
chmod +x myscript.py
```

2. **直接运行脚本**：

```sh
./myscript.py
```

这样系统就会使用 `env` 找到 `python3` 解释器，并用它来执行 `myscript.py` 中的代码。

### 总结

在 Python 脚本的顶部包含 `#!/usr/bin/env python3` 行，能够使脚本在 Unix 和 Unix-like 操作系统中直接运行，确保脚本使用 Python 3 解释器执行，同时增加了灵活性，使脚本能够在不同系统配置中找到合适的 Python 3 解释器。



# 输入输出

python中可以使用$input函数$以及$print()$函数进行输入输出

在 Python 中，`print` 和 `input` 是两个最常用的内置函数，用于输出和输入操作。

### `print` 函数

`print` 函数用于在控制台输出文本或其他类型的值。它可以接受多个参数，并在输出时自动添加空格。此外，它还可以通过指定 `sep`、`end` 和 `file` 参数来定制输出行为。

#### 基本用法

```python
print("Hello, world!")
```

#### 输出多个值

```python
name = "Alice"
age = 30
print("Name:", name, "Age:", age)
```

#### 使用 `sep` 参数指定分隔符

默认情况下，`print` 会在输出多个值时使用空格作为分隔符。可以使用 `sep` 参数更改分隔符：

```python
print("apple", "banana", "cherry", sep=", ")
```

输出：

```
apple, banana, cherry
```

#### 使用 `end` 参数指定结束符

默认情况下，`print` 会在输出后添加换行符。可以使用 `end` 参数更改结束符：

```python
print("Hello", end=" ")
print("world!")
```

输出：

```
Hello world!
```

#### 输出到文件

可以使用 `file` 参数将输出写入文件而不是控制台：

```python
with open("output.txt", "w") as file:
    print("This will be written to the file.", file=file)
```

### `input` 函数

`input` 函数用于从控制台读取用户输入。它会暂停程序的执行，直到用户输入一些内容并按下回车键。输入的内容将被返回为字符串。

#### 基本用法

```python
name = input("Enter your name: ")
print("Hello, " + name + "!")
```

#### 转换输入类型

`input` 函数返回的总是字符串类型。如果需要特定类型的数据，可以使用相应的类型转换函数：

```python
age = input("Enter your age: ")
age = int(age)
print("Next year, you will be", age + 1, "years old.")
```

或者可以直接在读取输入时进行转换：

```python
age = int(input("Enter your age: "))
print("Next year, you will be", age + 1, "years old.")
```

### 综合示例

下面是一个使用 `print` 和 `input` 函数的完整示例，展示如何读取用户输入并进行处理：

```python
# 获取用户的名字
name = input("Enter your name: ")

# 获取用户的年龄，并将其转换为整数
age = int(input("Enter your age: "))

# 计算用户明年的年龄
next_year_age = age + 1

# 输出结果
print("Hello,", name + "!")
print("You are", age, "years old.")
print("Next year, you will be", next_year_age, "years old.")
```

这个示例中，程序会先提示用户输入名字和年龄，然后计算并输出用户明年的年龄。

### 总结

- `print` 函数用于输出信息到控制台，可以通过 `sep`、`end` 和 `file` 参数进行定制。
- `input` 函数用于从控制台读取用户输入，返回值为字符串，可以通过类型转换函数转换为其他类型。

# 常用占位符

![image-20240623115215194](python学习.assets/image-20240623115215194.png) 