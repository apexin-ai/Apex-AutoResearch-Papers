# data plan 005 debugbench supplement

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_plan_005_debugbench_supplement_20260515T225700_result.json`
- **Structured JSON:** [`7afa6baefb18e9678883.json`](../../sessions/7a/7afa6baefb18e9678883.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

### 1. 数据衰减 (1414 → 1024, -390)
- **Stage 1** test_builder (-192): skip_complex 160 (TreeNode/ListNode), skip_parse_fail 26, skip_nondeterministic 6
- **Stage 2** validation (-198): 正确解未通过生成的测试用例

### 2. VOTA 条件：**缺失**
`debugbench_format_data.py` 只实现了 no_trace / exception_only / full_trace 三个条件，没有 VOTA 格式化路径。

### 3. Exception_only 理论上限：**71.1% 已验证**
- 测试集 207 个 fail 样本中 59.4% (123) 无异常（logic error），exception_only 无法区分这些和 pass
- 所有 219 个 pass 样本均无异常 → "有异常"是 fail 确定信号，"无异常"则歧义
- 上限 = (219 + 84) / 426 = 71.1%

### 4. Full_trace token 分布
- **68.9% 被截断**（1412/2048 样本命中 2048 上限）
- Median = 2048, Mean = 1508
- exception_only mean 372, no_trace mean 274（均安全）

### 5. Registry
无 plan_005 实验注册。仅数据准备完成。

报告已注册为 artifact `debugbench_data_audit`，memory.md 已更新。

---
