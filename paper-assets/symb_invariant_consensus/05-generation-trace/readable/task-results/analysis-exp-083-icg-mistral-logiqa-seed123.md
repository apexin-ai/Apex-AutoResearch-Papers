# analysis exp 083 icg mistral logiqa seed123

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-083-icg-mistral-logiqa-seed123_20260519T221941_result.json`
- **Structured JSON:** [`283f07ec1943888f646d.json`](../../sessions/28/283f07ec1943888f646d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-083 分析报告

### 原始指标
来源: `/root/symb_invariant_consensus/results/exp083_icg_mistral_logiqa_seed123/results.json`

| 指标 | 值 |
|---|---|
| n | 200 |
| SC accuracy | **36.5%** (73/200) |
| ICG accuracy | **33.0%** (66/200) |
| Δ | **-3.5pp** |
| K=12, K_ICG=10, T=0.7, seed=123 | |
| Wall time | 3653s (~61 min), 18.3s/question |
| Constraints | mean 31.4 generated, 27.9 unique |
| MaxSAT | mean 27.7 satisfied, 0.2 excluded |

### 交叉验证
Per-question count: sc_correct=73, icg_correct=66 → 73/200=0.365, 66/200=0.33 — **与 summary 一致 ✓**

Confusion matrix: both=62, sc_only=11, icg_only=4, neither=123. ICG 净翻转 -7（rescued 4, degraded 11）。

### 2-seed 汇总

| seed | SC% | ICG% | Δpp | exp_id |
|---|---|---|---|---|
| 42 | 47.5 | 47.0 | -0.5 | exp-079 |
| 123 | 36.5 | 33.0 | -3.5 | exp-083 |
| **mean** | **42.0** | **40.0** | **-2.0±2.12** | |

SC baseline 跨 seed 方差极大（47.5% vs 36.5%, gap=11pp），ICG delta 两个 seed 均为负。

### Conclusion: **negative**

理由：两个 seed 的 Δ 均 ≤ 0（-0.5pp, -3.5pp），mean=-2.0pp。seed=123 的 ICG 比 SC 差 3.5pp，confusion matrix 显示 ICG 净损失 7 题。ICG 在 LogiQA 上无改善作用，与 FOLIO 上的 3-seed 结论一致（mean Δ=-0.49pp）——独立约束生成无法绕过 model bias。

### Registry 更新确认
- status: ANALYZING → **DONE** ✓
- conclusion: **negative** ✓
- metrics: 全量写入 ✓
- checkpoint_path: 已设置 ✓
- log_path: 已设置 ✓
- memory.md: 已追加 exp-083 段落 ✓

---
