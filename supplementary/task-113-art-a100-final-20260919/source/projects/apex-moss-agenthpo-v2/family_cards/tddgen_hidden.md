# 任务说明卡:少量可见测试的隐藏终验构造(tddgen_hidden)

> 本卡只描述任务类型本身,不含任何具体题目、分数或历史记录。

## 任务目标(task goal)

给定只有 imports、函数签名和详细文档字符串的 `solution.py`,从零实现完整函数行为。
`test_solution.py` 只包含官方测试中的一个行为样例;更多边界条件由不可见的终验套件检查。

## 工作环境(environment)

工作目录只含可编辑的 `solution.py` 和只读的 `test_solution.py`。隐藏终验不在工作目录内,
不能读取或运行;评分器只在 Harness 完成后运行它。

## 反馈方式(feedback mechanism)

可反复运行可见 pytest,但它只验证一个样例,通过不代表任务完成。隐藏终验的测试名、断言和
失败输出永不反馈给 Harness;因此详细文档字符串是完整行为的主要规格。

## 可用工具(tool requirement)

- read_file(path):读取工作目录内文件
- write_file(path, content):只写 `solution.py`
- run_tests(test_path):只运行可见 `test_solution.py`

## 适合的思考模式(reasoning pattern)

规格驱动的构造式思考:先逐条提取文档中的输入域、输出结构、异常、空值和边界条件,再把唯一
可见测试当作接口校准而非完整需求。实现后应主动枚举或在脑中模拟未展示的边界,完整自审,
不要因为可见测试变绿就立即停止。
