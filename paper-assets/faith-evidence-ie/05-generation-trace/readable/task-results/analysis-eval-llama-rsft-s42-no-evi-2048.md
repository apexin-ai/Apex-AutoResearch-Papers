# analysis eval llama rsft s42 no evi 2048

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_llama_rsft_s42_no_evi_2048_20260521T140345_result.json`
- **Structured JSON:** [`304216d108ee0b43285a.json`](../../sessions/30/304216d108ee0b43285a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

---

## 分析报告：eval_llama_rsft_s42_no_evi_2048

### 1. 核心指标

| 指标 | 值 |
|------|-----|
| **Ign-F1** | **0.5559** |
| F1 | 0.5703 |
| Evi-F1 (DREEAM) | 0.0006 |
| Evi-F1 (TP) | 0.0007 |
| EDCR | 0.6250 |
| Format OK | 984/985 (99.9%) |
| Truncated | 140/985 (14.2%) |
| Predictions | 24,365 |
| Inference Time | 4h22m (15.95 s/doc) |

### 2. Matched@2048 Evidence Tax（s42）

| 条件 | Ign-F1 | 
|------|--------|
| with-evidence @2048 | 0.5774 |
| no-evidence @2048 | 0.5559 |
| **Evidence Tax** | **-2.15pp** |

### 3. 与 @1024 Tax 对比

| Seed | @1024 Tax | @2048 Tax |
|------|-----------|-----------|
| s42 | -1.88pp | **-2.15pp** |
| s43 | -1.16pp | — |
| s44 | -0.37pp | — |
| **@1024 3-seed mean** | **-1.14±0.76pp** | — |

@2048 s42 tax (-2.15pp) 比 @1024 s42 tax (-1.88pp) 增大了 0.27pp。原因：with-evidence 从 @1024→@2048 增益 (+0.60pp: 0.5714→0.5774) 大于 no-evidence 增益 (+0.33pp: 0.5526→0.5559)。

### 4. 截断率对比

| 条件 | @1024 | @2048 | 降幅 |
|------|-------|-------|------|
| no-evidence (s42) | ~18%* | 14.2% (140/985) | ~4pp |
| with-evidence (s42) | N/A | 9.1% (90/985) | — |
| no-evidence (s43 @1024) | 18.6% (183/985) | — | — |
| no-evidence (s44 @1024) | 18.1% (178/985) | — | — |

*s42 @1024 截断率未直接记录，参考 s43/s44 估计。

@2048 确实降低了截断率（~18%→14.2%），但 no-evidence 截断仍高于 with-evidence（140 vs 90），因为 no-evidence 模型输出更多 predictions（24365 vs 18129）。

### 5. 结论

**@2048 budget 下 RSFT evidence tax 略微增大但基本稳定。**

- Tax 从 @1024 的 -1.88pp 变为 @2048 的 -2.15pp（delta = -0.27pp），方向一致、幅度相近
- @2048 对 with-evidence 的增益大于 no-evidence（+0.60 vs +0.33pp），说明额外 token budget 更有利于 evidence 输出而非纯 relation 预测，符合直觉
- @2048 s42 tax (-2.15pp) 超出 @1024 3-seed 1-sigma 范围（-1.14±0.76 → [-1.90, -0.38]），但仅超出 0.25pp，在 seed variance 可解释范围内
- 需要 s43/s44 @2048 no-evi 数据才能做 matched-budget 3-seed 统计

---
