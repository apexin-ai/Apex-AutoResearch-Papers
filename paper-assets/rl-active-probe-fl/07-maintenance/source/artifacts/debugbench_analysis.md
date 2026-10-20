# DebugBench 数据集分析报告

**数据集**: `Rtian/DebugBench` (HuggingFace)
**论文**: arXiv:2401.04621
**License**: Apache 2.0
**分析日期**: 2026-05-14

---

## 1. 数据集概览

| 项目 | 值 |
|------|-----|
| Splits | test (仅一个) |
| 总条数 | 4,253 |
| 语言 | C++ (1,438), Python3 (1,414), Java (1,401) |
| 数据来源 | LeetCode 题目 |

## 2. 字段结构

| 字段名 | 类型 | 含义 |
|--------|------|------|
| `question` | string | LeetCode 题目描述 |
| `examples` | list[string] | 输入输出样例（通常 1-3 个） |
| `constraints` | string | 约束条件 |
| `buggy_code` | string | 含 bug 的代码 |
| `solution` | string | 正确代码 |
| `bug_explanation` | string | bug 的自然语言解释 |
| `solution_explanation` | string | 正确解法的详细解释 |
| `category` | string | bug 大类（syntax error / reference error / logic error / multiple error） |
| `subtype` | string | bug 子类型（如 illegal indentation, condition error 等） |
| `level` | string | 题目难度（easy / medium / hard） |
| `slug` | string | LeetCode 题目 slug |
| `release_time` | int64 | 题目发布时间戳 |
| `language` | string | 编程语言（cpp / python3 / java） |

**注意**: 没有独立的 test cases 字段，测试用例仅以 `examples` 形式存在（输入输出样例的文本描述，非可执行格式）。

## 3. 样例数据

### 样例 1 (Python3, syntax error, easy)

- **slug**: most-frequent-even-element
- **level**: easy
- **category**: syntax error
- **subtype**: illegal separation
- **question**: Given an integer array nums, return the most frequent even element. If there is a tie, return the smallest one. If there is no such element, return -1.
- **buggy_code**:
```python
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        ...
        for(auto y:freq)
            if(y.first%2==0 && y.second> evefreq)
                ans=y.first;
                evefreq=y.second;  # 此行不在 if 控制范围内
        return ans;
```
- **bug_explanation**: There's a missing bracket for the if-statement in the second loop causing wrong assignment to evefreq.

### 样例 2 (Python3, syntax error, medium)

- **slug**: moving-stones-until-consecutive-ii
- **level**: medium
- **category**: syntax error
- **subtype**: illegal indentation
- **bug_explanation**: In python, indentation is significant in that it denotes a block of code. The increment operator for 'starting_index' is incorrectly indented outside the while loop.

### 样例 3 (Python3, multiple error, hard)

- **slug**: longest-palindromic-substring
- **level**: hard
- **category**: multiple error
- **subtype**: triple (3 个独立 bug)

## 4. Python 子集统计

### 基本信息

| 项目 | 值 |
|------|-----|
| Python 样本总数 | 1,414 |
| 语言标签 | `python3`（注意不是 `python`） |
| 占总数据集比例 | 33.2% |

### Bug Category 分布

| Category | 数量 | 占比 |
|----------|------|------|
| multiple error | 731 | 51.7% |
| syntax error | 260 | 18.4% |
| reference error | 227 | 16.1% |
| logic error | 196 | 13.9% |

### Bug Subtype 分布

| Subtype | 数量 | 占比 |
|---------|------|------|
| triple | 250 | 17.7% |
| double | 250 | 17.7% |
| quadruple | 231 | 16.3% |
| condition error | 83 | 5.9% |
| faulty indexing | 72 | 5.1% |
| operation error | 62 | 4.4% |
| undefined objects | 60 | 4.2% |
| undefined methods | 56 | 4.0% |
| illegal indentation | 45 | 3.2% |
| unclosed parentheses | 45 | 3.2% |
| misused == or = | 45 | 3.2% |
| missing colons | 43 | 3.0% |
| unclosed string | 42 | 3.0% |
| illegal comment | 40 | 2.8% |
| illegal keywords | 39 | 2.8% |
| variable error | 31 | 2.2% |
| other error | 20 | 1.4% |

**说明**: `double`/`triple`/`quadruple` 属于 `multiple error` category，表示代码中同时存在 2/3/4 个 bug。

### Difficulty (Level) 分布

| Level | 数量 | 占比 |
|-------|------|------|
| medium | 590 | 41.7% |
| hard | 469 | 33.2% |
| easy | 355 | 25.1% |

### 字段长度统计

| 字段 | 均值 | 中位数 | 最小值 | 最大值 | 标准差 |
|------|------|--------|--------|--------|--------|
| buggy_code (chars) | 656 | 570 | 76 | 8,159 | 475 |
| solution (chars) | 744 | 588 | 82 | 8,177 | 844 |
| question (chars) | 471 | 431 | 83 | 1,869 | 273 |
| bug_explanation (chars) | 81 | 82 | 39 | 626 | 27 |
| examples (count) | 2.4 | - | 1 | 3 | - |

## 5. 关键发现与注意事项

### 对后续 pipeline 的影响

1. **无可执行测试用例**: `examples` 字段是自然语言描述的输入输出样例，不是结构化的 test cases。如果需要自动验证修复结果，需要另外构造或解析测试用例。

2. **multiple error 占比过半 (51.7%)**: Python 子集中超过一半的样本包含多个 bug（2-4 个）。这对 pipeline 设计有重要影响——如果只修复一个 bug，样本仍然不能通过。需要决定是：
   - 只使用 single-bug 样本（683 条）
   - 设计支持多 bug 修复的 pipeline

3. **语言标签是 `python3`**: 筛选时需用 `python3` 而非 `python`。

4. **代码长度差异大**: buggy_code 从 76 到 8,159 字符不等，需要考虑 token 长度限制。平均 ~656 字符（约 200-300 tokens）。

5. **bug_explanation 较短**: 平均仅 81 字符，提供了简洁的 bug 描述，可用于构造 prompt 或作为 reward signal 的参考。

6. **solution_explanation 可能很长**: 部分样例的解法解释超过 10K 字符，包含完整的算法分析。

7. **LeetCode 题目可能有版权问题**: 数据来源于 LeetCode，虽然数据集 license 是 Apache 2.0，但使用时需注意。

8. **slug 字段可用于去重**: 不同 bug 类型可能对应同一道 LeetCode 题目，slug 可用于识别。
