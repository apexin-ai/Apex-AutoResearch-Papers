# analyze d140 1 7b sft s42 with evi 2048

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_d140_1_7b_sft_s42_with_evi_2048_20260521T062635_result.json`
- **Structured JSON:** [`83ae3ecfa5a9eddcef5f.json`](../../sessions/83/83ae3ecfa5a9eddcef5f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验正常完成。汇总分析如下：

---

## D140: 1.7B SFT s42 with-evi @2048 结果分析

### with-evi@2048 全量 Metrics

| Metric | Value |
|--------|-------|
| **ign_f1** | **0.4806** |
| f1 | 0.4951 |
| ign_precision | 0.4759 |
| ign_recall | 0.4854 |
| precision | 0.5005 |
| recall | 0.4897 |
| evi_f1 (TP) | 0.8006 |
| evi_f1_joint (DREEAM) | 0.3941 |
| edcr | 0.7175 |
| format_ok | 985/985 (100%) |
| **truncated** | **267/985 (27.1%)** |
| n_predictions | 25,534 |

### 与 @1024 对比

| | with-evi@1024 | with-evi@2048 | Delta |
|--|---------------|---------------|-------|
| ign_f1 | 0.4710 | 0.4806 | **+0.96pp** |
| truncated | 314/985 (31.9%) | 267/985 (27.1%) | **-4.8pp** |

with-evi 从更大 token budget 中获益：截断率下降 4.8pp，ign_f1 提升近 1pp。

### Matched Evidence Tax @2048

| | no-evi | with-evi | Tax (no-evi − with-evi) |
|--|--------|----------|-------------------------|
| @1024 | 0.3982 | 0.4710 | **-7.28pp** |
| @2048 | 0.3925 | 0.4806 | **-8.81pp** |

Tax 为负 = evidence 有帮助。@2048 下 evidence benefit 从 7.28pp **扩大到 8.81pp**（+1.53pp）。

### 截断不对称性分析

| | with-evi truncated | no-evi truncated | 差距 |
|--|-------------------|-----------------|------|
| @1024 | 31.9% | 50.9% | 19.0pp |
| @2048 | 27.1% | 50.6% | **23.5pp** |

关键发现：@2048 时 with-evi 截断从 31.9%→27.1%（下降 4.8pp），而 no-evi 几乎不变（50.9%→50.6%）。这解释了 evidence tax 为何扩大——with-evi 能利用额外 token budget，no-evi 不能（其截断是模型生成能力瓶颈，不是 budget 限制）。

### 结论

**Positive result。** 1.7B with-evi@2048 ign_f1=0.4806 显著优于 no-evi@2048 ign_f1=0.3925，evidence tax = -8.81pp。在 matched@2048 条件下，evidence benefit 比 @1024 更大，因为 with-evi 模型实际利用了更多 token budget 而 no-evi 模型没有。这进一步证实了 1.7B 模型中 evidence 的正面作用不是截断差异的 artifact。

---
