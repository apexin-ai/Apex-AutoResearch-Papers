# 任务说明卡:纯规格隐藏终验构造(specgen_hidden)

> 本卡只描述任务类型本身,不含任何具体题目、分数或历史记录。

## 任务目标(task goal)

给定只有 imports、函数签名和详细文档字符串的 `solution.py`,完全依照公开规格从零实现函数。
可见测试不包含任何输入输出行为断言;完整正确性只由不可见终验套件检查。

## 工作环境(environment)

工作目录只含可编辑的 `solution.py` 和只读的 `test_solution.py`。后者仅检查模块可导入且
入口函数可调用。隐藏终验不在工作目录内,不能读取或运行。

## 反馈方式(feedback mechanism)

可见 pytest 只能发现语法、导入或入口缺失,不能确认算法行为。隐藏终验在 Harness 完成后
运行,其测试名、断言和失败输出永不反馈。因此工作流不能依赖测试驱动迭代来补规格。

## 可用工具(tool requirement)

- read_file(path):读取工作目录内文件
- write_file(path, content):只写 `solution.py`
- run_tests(test_path):只运行无行为断言的可见冒烟测试

## 适合的思考模式(reasoning pattern)

纯规格构造与提交前验证:把文档转换成显式检查清单,覆盖正常路径、边界、异常和返回类型;
一次写出完整实现后做静态自审和自拟输入的心智执行。可见冒烟变绿只说明代码可加载,绝不能
作为提前停止依据。
