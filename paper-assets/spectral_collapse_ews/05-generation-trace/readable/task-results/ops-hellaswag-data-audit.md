# ops hellaswag data audit

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_hellaswag-data-audit_20260521T102439_result.json`
- **Structured JSON:** [`32eb8019f6b77603b23f.json`](../../sessions/32/32eb8019f6b77603b23f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。以下是完整报告。

---

## HellaSwag 数据完整性审计报告

### 1. 数据存在性矩阵

| Gen | Seed42 (`hellaswag_gen*`) | Seed43 (`hellaswag_seed43_gen*`) | Seed44 (`hellaswag_seed44_gen*`) |
|-----|:---:|:---:|:---:|
| 0  | 0.4130 | -- | 0.4130 |
| 1  | 0.3897 | -- | 0.3911 |
| 2  | 0.3764 | -- | 0.3841 |
| 3  | 0.3658 | -- | 0.3721 |
| 4  | 0.3558 | -- | -- (running ~44%) |
| 5  | 0.3439 | -- | -- |
| 6  | 0.3311 | -- | -- |
| 7  | 0.3187 | -- | -- |
| 8  | 0.3103 | -- | -- |
| 9  | 0.3009 | -- | -- |
| 10 | 0.2951 | -- | -- |

**Seed42**: 完整 (gen0-10), 来源 `results/hellaswag_gen{N}/results.json`
**Seed43**: **零个结果文件**。旧 eval 仅在 log 中记录了 gen2: 0.3809，但未保存 results.json。新 eval 刚启动 (PID 567248)，正在评估 gen0。
**Seed44**: gen0-3 已完成，gen4 正在运行 (~44% loglikelihood requests)。

### 2. Pipeline Results 检查

`phase0_results.json`、`phase1_pure_collapse_seed43_results.json`、`phase1_pure_collapse_seed44_results.json` 均 **不包含** HellaSwag 数据。HellaSwag 不是训练 pipeline 内置 eval 的一部分，所有 HeSw 数据来自独立的 `lm_eval` 评估。

### 3. Table 1 声称 vs 实际数据

Table 1 caption 声称 "mean of seeds 42 and 43"。验证：

| Gen | Table 1 HeSw | Seed42 only (rounded) | 匹配? |
|-----|:-----------:|:--------------------:|:-----:|
| 0   | .413 | .413 | (trivial, 同一 base model) |
| 2   | .378 | .376 | 不匹配 |
| 5   | .341 | .344 | 不匹配 |
| 7   | .319 | .319 | 匹配 |
| 10  | .293 | .295 | 不匹配 |

Table 1 的 HeSw 值 **不是** 纯 seed42 数据。但 seed43 的 HellaSwag 结果文件 **不存在**。可能存在过已被删除的旧 eval 结果，或 table 值来自无法溯源的计算。

### 4. 数据完整性结论

**确认存在数据完整性问题：** Table 1 声称 HeSw 列为 seed 42 和 43 的均值，但服务器上不存在 seed43 的 HellaSwag 结果文件。该声称无法从现有文件验证。

### 5. 正在运行的 eval 进度

- **Seed43 eval**: PID 567248, 刚启动 gen0, 预计全部 gen0-10 需要 ~40 分钟 (每 gen ~3.5 分钟)
- **Seed44 eval**: gen4 在 ~44%, 预计全部 gen4-10 还需 ~25 分钟 (gen4 剩余 ~2 分钟 + gen5-10 各 ~3.5 分钟)

---
