# analysis qwen s025 entropy investigation

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen_s025_entropy_investigation_20260514T091123_result.json`
- **Structured JSON:** [`d0918ecaeb139d283895.json`](../../sessions/d0/d0918ecaeb139d283895.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据齐全，汇报结果。

---

## 调查结果

### 调查 1：Qwen s025 entropy 符号反转 → **Systematic，非 outlier**

**Qwen importance entropy_delta 分布：**

| Sparsity | n | pos:neg | mean | median | std | trimmed mean |
|----------|---|---------|------|--------|-----|-------------|
| s015 | 30 | 2:28 | **-0.0733** | -0.0685 | 0.0831 | -0.0702 |
| s020 | 30 | 4:26 | **-0.0759** | -0.0815 | 0.1089 | -0.0714 |
| s025 | 30 | **22:8** | **+0.0451** | +0.1088 | 0.1378 | +0.0603 |
| s030 | 30 | 15:15 | **-0.0072** | +0.0065 | 0.1557 | +0.0066 |

**DeepSeek 对比（全部一致负值）：**

| Sparsity | pos:neg | mean | std |
|----------|---------|------|-----|
| s015 | 1:29 | -0.0402 | 0.0222 |
| s020 | 1:29 | -0.0472 | 0.0240 |
| s025 | 1:29 | -0.0446 | 0.0242 |
| s030 | 2:28 | -0.0436 | 0.0266 |

**关键发现：**
- Qwen s025 的正值由 **22/30 problems** 支撑，是 systematic effect
- 唯一极端 outlier 是 **负值** (-0.4865)，它拉低了 mean；去掉后 mean 更正 (0.0634)
- trimmed mean (+0.0603) 和 median (+0.1088) 都确认方向
- Qwen 呈现 **非单调模式**：s015/s020 负 → s025 翻正 → s030 回到零附近。DeepSeek 则全程稳定负值
- Qwen 的 std 比 DeepSeek 大 4-6 倍（0.08-0.16 vs 0.02-0.03），表明 Qwen 对 importance masking 的 entropy 响应异质性远高于 DeepSeek

**结论：** Qwen s025 entropy 反转是 **systematic cross-model difference**，不是 outlier artifact。可能原因：Qwen（非 distill 版）的 attention head importance 分布与 DeepSeek-R1-Distill 有质的不同——在 25% sparsity 时，importance masking 反而打乱了 Qwen 的注意力集中模式。

---

### 调查 2：8 个 importance 实验 bootstrap 值 → **全部 B=1000，需要 re-bootstrap**

| 实验 | B | per_problem_ii |
|------|---|---------------|
| DS s015 | 1000 | ✓ |
| DS s020 | 1000 | ✓ |
| DS s025 | 1000 | ✓ |
| DS s030 | 1000 | ✓ |
| QW s015 | 1000 | ✓ |
| QW s020 | 1000 | ✓ |
| QW s025 | 1000 | ✓ |
| QW s030 | 1000 | ✓ |

全部 8 个实验均有 `per_problem_ii` 原始数据，可直接 re-bootstrap 到 B=10000 而无需重跑实验。

---

### 调查 3：cross_model_analysis.json → **已是最新值，无需修复**

`random_median_diffs.qwen.s030 = 2.418272`，匹配 B=10000 期望值。`gradient_permutation_test.B = 10000`。文件已更新。

---
