# research verify framing data

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_verify_framing_data_20260514T043015_result.json`
- **Structured JSON:** [`d6fb3f452eedb24f0392.json`](../../sessions/d6/d6fb3f452eedb24f0392.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据齐全。以下是验证结果。

---

## 数据点 1：exp_008c @35K value/eval ratio

**来源文件**: `logdir/exp_008c_fixed_dt2_no_subsample_h8/metrics.jsonl`, step=35000

| 字段 | 值 |
|---|---|
| value_mean | 40.430 |
| eval_return | 185.096 |
| **v/e ratio** | **40.43 / 185.10 = 0.2184 = 21.8%** |

- **paper_framing.md 声称**: `v/e: @35K=19%`
- **实际值**: **21.8%**
- **差异**: +2.8 个百分点，paper 数据不准确
- **建议修正**: 改为 `@35K=22%`（或精确值 21.8%）

Registry 交叉验证：55K=0.291 和 65K=0.328 与日志一致（70.32/241.87=0.291, 78.96/240.86=0.328 ✓），但 35K 数据点不在 registry 中。

---

## 数据点 2：exp_006 (fixed_dt2_v1_s1) @55K value/eval ratio

**来源文件**: `logdir/fixed_dt2_v1_s1/metrics.jsonl`

| Step | value_mean | eval_return | v/e ratio |
|---|---|---|---|
| **45000** | 254.287 | 477.000 | **53.3%** |
| **55000** | 336.444 | 360.441 | **93.3%** |

- **ROADMAP 声称**: `exp_006 v/e=53.3%@55K`
- **实际 @55K**: **93.3%**（不是 53.3%）
- **53.3% 的真实来源**: **step 45K**（254.29/477.00=0.5331）
- **差异**: ROADMAP 标错了 step 号，53.3% 属于 45K 而非 55K
- **建议修正**: 改为 `v/e=53.3%@45K` 或 `v/e=93.3%@55K`

---

### 总结

| 数据点 | 声称值 | 实际值 | 问题 |
|---|---|---|---|
| exp_008c v/e @35K | 19% | **21.8%** | 数值偏差 -2.8pp |
| exp_006 v/e @55K | 53.3% | **93.3%** | step 标错（53.3% 实际来自 @45K） |

---
