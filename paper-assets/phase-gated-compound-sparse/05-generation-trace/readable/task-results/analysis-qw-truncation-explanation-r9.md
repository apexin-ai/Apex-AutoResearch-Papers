# analysis qw truncation explanation r9

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qw_truncation_explanation_r9_20260515T193550_result.json`
- **Structured JSON:** [`6c6b8f7f5cf16ff2d74c.json`](../../sessions/6c/6c6b8f7f5cf16ff2d74c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据完整了。以下是完整分析结果。

---

## Truncation 统计表

**GSM8K (n=50, 用于 gradient 分析的数据)**:

| Model | Strategy | N | Truncated | Rate | Avg Length |
|-------|----------|---|-----------|------|------------|
| DS    | importance | 50 | 15/50 | 30.0% | 1332.5 |
| DS    | random     | 50 | 15/50 | 30.0% | 1332.5 |
| **QW** | **importance** | **50** | **50/50** | **100.0%** | **2047.0** |
| **QW** | **random**     | **50** | **50/50** | **100.0%** | **2047.0** |

**MATH-500 (n=50, bf16)**:

| Model | Strategy | N | Truncated | Rate | Avg Length |
|-------|----------|---|-----------|------|------------|
| DS    | importance | 50 | 19/50 | 38.0% | 1242.8 |
| DS    | random     | 50 | 19/50 | 38.0% | 1242.8 |
| QW    | importance | 50 | 12/50 | 24.0% | 1057.8 |
| QW    | random     | 50 | 12/50 | 24.0% | 1057.8 |

**MATH-500 (n=500, bf16)**:

| Model | Strategy | N | Truncated | Rate | Avg Length |
|-------|----------|---|-----------|------|------------|
| DS    | importance | 500 | 205/500 | 41.0% | 1396.8 |
| DS    | random     | 500 | 205/500 | 41.0% | 1396.8 |
| QW    | importance | 500 | 139/500 | 27.8% | 1174.0 |
| QW    | random     | 500 | 139/500 | 27.8% | 1174.0 |

> 注：同一 (model, dataset, n_problems) 组内，所有 sparsity level 和 masking strategy 的截断数完全一致——因为生成由 dense 模型完成，sparsity masking 仅影响 PPL 评估。

---

## DS importance 的截断情况

**DS importance 有截断，但远低于 QW。** GSM8K 上 DS 为 15/50 (30%)，MATH-500 上为 19/50 (38%)。不存在"DS 无截断"的情况。

---

## 技术解释

**GSM8K 上 QW 100% 截断而 DS 仅 30% 的原因：**

Qwen2.5-7B-Instruct 是通用 chat 模型，缺乏 `&lt;think>→answer` 的结构化推理模式。面对 GSM8K 算术题时，它生成冗长的格式化步骤说明（markdown 标题、重复验算、详细排版），没有自然终止信号，100% 填满 2047 token 预算。DeepSeek-R1-Distill-Qwen-7B 作为推理模型，产生紧凑的思维链，简单算术题在 300–700 token 内完成，仅复杂题才截断。

反向模式出现在 MATH-500 上（DS 38% > QW 24%）：竞赛数学对推理深度要求更高，DS 的深度推理链更容易超长；QW 对难题往往生成较浅但较短的响应。

---

## 论文脚注

**QW random s030 GSM8K 数据因系统性生成截断被标记为不可靠：Qwen2.5-7B-Instruct 作为非推理模型缺乏自然生成终止点，在全部 50 个 GSM8K 问题上均达到 max\_new\_tokens=2047 上限（截断率 100%，对比 DeepSeek-R1-Distill 的 30%），导致相位分割在人为等长的截断序列上运行，产生伪相位结构，使 interaction index 出现极端离群值（gradient=92.9，95% CI: [3.8, 258.8]）并包含 NaN 值。**

---
