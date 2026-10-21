# analysis math pilot output audit

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_math-pilot-output-audit_20260514T141111_result.json`
- **Structured JSON:** [`d9627f5892dd2e2ae373.json`](../../sessions/d9/d9627f5892dd2e2ae373.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 审计结果

### 三类问题统计

| 分类 | 数量 | 占比 | CodeInterp 准确率 | Internal 准确率 |
|------|------|------|-------------------|----------------|
| **A** (代码执行，output 非空) | 27 | 54% | **88.9%** (24/27) | 85.2% (23/27) |
| **B** (代码执行，output 空) | 14 | 28% | **28.6%** (4/14) | 64.3% (9/14) |
| **C** (无代码执行) | 9 | 18% | 88.9% (8/9) | 88.9% (8/9) |

### 关键发现

- **空 output 率 34.1%**（14/41 有代码执行的记录），远超 10% 阈值——系统性 bug
- **"干净" CodeInterp 准确率是 88.9%**（Category A），不是报告的 72%
- Category B 的 CodeInterp 准确率仅 28.6%——LLM 看不到代码结果，被迫心算，准确率断崖式下降
- 所有 14 条空 output 记录的代码都没有 `print()`，最后一行是裸表达式（`solution`、`expanded_expr` 等）

### Bug 根因：`src/code_sandbox.py`

`execute_code()` 将代码写入临时 `.py` 文件，用 `subprocess.run(capture_output=True)` 执行。Python 脚本模式下裸表达式不产生 stdout（不像 Jupyter/REPL 会自动显示）。LLM 收到空的执行结果后退化为纯推理。

**修复方向**：用 `ast` 模块检测代码末尾的 `Expr` 节点，自动包装为 `print()`。

### 产出

1. 统计表如上
2. 14 条空 output 题目列表：`math_level4_0002`, `0004`, `math_level5_0005`, `0007`, `0009`, `0011`, `math_level4_0022`, `0027`, `0039`, `math_level5_0040`, `math_level4_0041`, `0042`, `0043`, `0044`
3. Bug 根因：`code_sandbox.py` 只捕获 stdout，不处理裸表达式
4. 分析脚本已保存：服务器和本地 `src/analyze_math_pilot.py`

---
