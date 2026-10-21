# data plan 005 debugbench prep

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_plan_005_debugbench_prep_20260515T222547_result.json`
- **Structured JSON:** [`6ba4cdb9c9f9e6c97147.json`](../../sessions/6b/6ba4cdb9c9f9e6c97147.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据准备完成。以下是完整报告：

---

## DebugBench 数据准备报告

### 数据处理 Pipeline

| 阶段 | 数量 | 比率 |
|------|------|------|
| DebugBench Python subset | 1414 | 100% |
| Test cases 构造成功 | 1222 | 86.4% |
| 验证通过（correct code passes） | 1024 | 83.8% |
| Raw traces 收集（×2 = correct+buggy） | 2048 | - |

**排除原因**: TreeNode/ListNode (160), parse 失败 (26), 非确定性 (6), 验证失败 (198)

### Trace 收集结果

- Correct code: 1016 pass / 8 fail (99.2%)
- Buggy code: 26 pass / 998 fail (97.5%)

### 最终数据文件

| 文件 | Train | Test | Pass% | Fail% |
|------|-------|------|-------|-------|
| debugbench_no_trace | 1622 | 426 | 50.7% | 49.3% |
| debugbench_exception_only | 1622 | 426 | 50.7% | 49.3% |
| debugbench_full_trace | 1622 | 426 | 50.7% | 49.3% |

### 对比 HumanEval+MBPP

| | DebugBench | HumanEval+MBPP |
|---|-----------|----------------|
| Train | 1622 | 4720 |
| Test | 426 | 1190 |
| Label balance | 50.7/49.3 | 65.8/34.2 |
| exception_only 空 trace | 81.6% | - |
| full_trace 截断率 | 68.9% | - |

### Token 长度分布

| Condition | Min | Median | Mean | Max | >2048 |
|-----------|-----|--------|------|-----|-------|
| no_trace | 117 | 226 | 274 | 1849 | 0% |
| exception_only | 127 | 293 | 372 | 1859 | 0% |
| full_trace | 125 | 2048 | 1508 | 2048 | 0% |

### 训练时间估算

- 基准: HumanEval+MBPP 4720 train → ~2h/condition on A6000
- DebugBench 1622 train → 34.4% 数据量
- **预计 ~40 min/condition, 3 条件共 ~2h**

### 存储路径

所有文件在 `/root/autodl-tmp/trace-verdict-study-data/`:
- `debugbench_exception_only_{train,test}.jsonl`
- `debugbench_full_trace_{train,test}.jsonl`
- `debugbench_no_trace_{train,test}.jsonl`

原始数据在 `/root/autodl-tmp/trace-verdict-study-data/debugbench/`:
- `debugbench_python.jsonl` (1414 完整 Python subset)
- `test_cases.jsonl` / `test_cases_validated.jsonl`
- `raw_traces.jsonl` (81.3 MB)

### 注意事项

1. DebugBench label 比 HumanEval+MBPP 更平衡（50/50 vs 66/34），因为每个问题恰好一个 correct + 一个 buggy
2. 81.6% 的 exception_only 样本为空 trace——这其实是有效信号：无 exception = pass
3. 26 个 buggy code 通过了测试（2.5%）——因为 examples 覆盖有限，部分 bug 未被触发
4. 代码是 LeetCode `class Solution` 风格，与 HumanEval/MBPP 独立函数不同

---
