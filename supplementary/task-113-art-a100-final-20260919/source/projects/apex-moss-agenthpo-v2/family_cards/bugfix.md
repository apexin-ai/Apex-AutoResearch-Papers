# 任务说明卡:修 bug(bugfix)

> 本卡只描述任务类型本身,不含任何具体题目、分数或历史记录。

## 任务目标(task goal)

给定一段**已经写好但含有 bug** 的 Python 代码(`solution.py`)和一组测试(`test_solution.py`),
修改 `solution.py` 使全部测试通过。bug 通常很小(边界条件、运算符、索引、初始化等),
原代码的整体结构和意图是正确的。

## 工作环境(environment)

一个工作目录,内含 `solution.py`(待修)和 `test_solution.py`(pytest 测试,只读)。
可能还有测试用的数据文件(只读)。

## 反馈方式(feedback mechanism)

运行 pytest:全部通过即成功。失败时能看到具体哪个断言失败、期望值和实际值——
这是定位 bug 的最直接线索。

## 可用工具(tool requirement)

- read_file(path):读文件
- write_file(path, content):写文件(只应写 solution.py)
- run_tests(test_path):运行 pytest 并返回输出

## 适合的思考模式(reasoning pattern)

诊断式:先看测试失败信息(期望 vs 实际)推断 bug 位置,再读代码定位具体行,
做**最小修改**,立即重跑测试验证。改动越小越好——大重写容易引入新 bug。
如果一次修复不成功,应根据新的失败信息重新诊断,而不是盲目重试。
