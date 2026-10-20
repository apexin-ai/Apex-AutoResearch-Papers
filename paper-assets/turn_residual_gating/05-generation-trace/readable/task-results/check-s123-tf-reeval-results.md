# check s123 tf reeval results

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_s123_tf_reeval_results_20260524T065033_result.json`
- **Structured JSON:** [`0b3ba348c388f250d17e.json`](../../sessions/0b/0b3ba348c388f250d17e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个 seed 的 TF GAR 全部到手，计算统计。

## 结果汇总

### s123 TF re-eval
- **s123 mid_turns_avg_gar = 0.4952**（之前是 NaN，已修复）

### 3-seed TF GAR (teacher-forcing)

| Seed | TF GAR |
|------|--------|
| s42 | 0.5025 |
| s123 | 0.4952 |
| s456 | 0.4964 |
| **mean±std** | **0.4980 ± 0.0039** |

### 3-seed AR GAR (auto-regressive, 已知)

| Seed | AR GAR |
|------|--------|
| s42 | 0.347 |
| s123 | 0.423 |
| s456 | 0.433 |
| **mean±std** | **0.401 ± 0.047** |

### 3-seed Gap (TF / AR)

| Seed | TF | AR | TF/AR ratio |
|------|----|----|-------------|
| s42 | 0.5025 | 0.347 | 1.448 |
| s123 | 0.4952 | 0.423 | 1.171 |
| s456 | 0.4964 | 0.433 | 1.146 |
| **mean±std** | | | **1.255 ± 0.170** |

TF GAR 跨 seed 非常稳定（std=0.004），AR GAR 方差大得多（std=0.047）。TF/AR gap 在 1.15×–1.45× 之间，s42 gap 最大主要因为其 AR GAR 偏低。

---
