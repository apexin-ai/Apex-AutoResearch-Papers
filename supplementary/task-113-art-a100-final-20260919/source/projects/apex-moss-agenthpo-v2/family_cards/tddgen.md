# 任务说明卡:按测试写代码(tddgen)

> 本卡只描述任务类型本身,不含任何具体题目、分数或历史记录。

## 任务目标(task goal)

给定一个**只有函数签名和文档字符串的空壳** `solution.py` 和一组测试(`test_solution.py`),
从零实现函数体使全部测试通过。没有任何已有实现可参考——测试就是完整的需求说明。

## 工作环境(environment)

一个工作目录,内含 `solution.py`(空壳,待实现)和 `test_solution.py`(pytest 测试,只读)。

## 反馈方式(feedback mechanism)

运行 pytest:全部通过即成功。测试断言(输入 → 期望输出)是唯一可靠的需求来源;
文档字符串可能含糊,以测试为准。

## 可用工具(tool requirement)

- read_file(path):读文件
- write_file(path, content):写文件(只应写 solution.py)
- run_tests(test_path):运行 pytest 并返回输出

## 适合的思考模式(reasoning pattern)

构造式:**先精读测试**,从断言反推函数的完整行为规范(包括边界情况),
然后一次性写出完整实现,再跑测试。若有失败,对照失败的断言修正理解、重写。
与修 bug 不同,这里没有"最小修改"的约束——重要的是先从测试建立对需求的完整理解,
避免只满足部分断言的片面实现。
