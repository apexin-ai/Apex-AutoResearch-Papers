# analysis check server experiments status

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_check-server-experiments-status_20260520T103116_result.json`
- **Structured JSON:** [`0aec5f4e825501041289.json`](../../sessions/0a/0aec5f4e825501041289.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Direction F is still running (PID alive, 53/204). Here's the full report:

---

## 实验状态汇总

### westd-25068

| # | 实验 | 状态 | 详情 |
|---|------|------|------|
| 1 | **Direction F (Blind FOL)** | **RUNNING** | 53/204, PID 378776 alive |
| 2 | **Direction H (Adversarial)** | **MISSING** | 无任何文件/日志/进程 |
| 3 | **exp-075b-contrastive-mistral-folio** | **COMPLETED** | 204/204 |
| 4 | **exp-066-qwen14b-folio-seed123** | **COMPLETED** | 204/204 |

### westd-16639

| # | 实验 | 状态 | 详情 |
|---|------|------|------|
| 5 | **Direction G (Decoupling)** | **RUNNING** | 10/204 (conservative), PID 307164 alive |

---

### 1. Direction F (Blind FOL) — RUNNING

- **进度**: 53/204, 运行中 accuracy 39.6%
- **50题 checkpoint**: 42.0% (21/50)
- SC baseline: 54.41%, SICA: 59.31%
- **Per-label (at 50)**:
  - True: 16.67% (3/18)
  - False: 25.0% (3/12)
  - Unknown: **75.0%** (15/20) — 严重偏向 Unknown
- Extraction: premise 96.67%, conclusion 90.5%, Z3 compilation 90.5%
- **趋势**: 随着问题数增加，accuracy 在下降 (42.0% → 39.6%)

### 2. Direction H (Adversarial) — MISSING

服务器上无任何痕迹：无结果目录、无日志文件、无 nohup.out、无匹配进程。可能从未启动或已被清理。

### 3. exp-075b-contrastive-mistral-folio — COMPLETED

- **Contrastive accuracy: 47.55%**
- **SC accuracy: 56.86%**
- **Delta: -9.31pp** (contrastive 大幅低于 SC)
- Degenerate cases: 41/204 (20.1%)
- Wall time: 11613s (~3.2h)
- 结论：contrastive 方法在 Mistral-7B + FOLIO 上失败，比 SC 差近 10 个点

### 4. exp-066-qwen14b-folio-seed123 — COMPLETED

- **SICA accuracy: 75.0%** (153/204)
- **SC accuracy: 74.51%** (152/204)
- **Delta: +0.49pp**
- Extraction rate: 98.57%
- Contradiction rate: 0.80% (31 problems)
- Total constraints: 13570, unique: 6110
- Wall time: 8853s (~2.5h)
- 结论：Qwen-14B seed123 上 SICA 微幅领先 SC，delta 不显著

### 5. Direction G (Decoupling) — RUNNING

- **进度**: conservative 策略 10/204
- 当前 accuracy: 70.0% (7/10)
- avg_trunc: 3.2%, matched: 99%
- 速度: ~0.01 prob/s, 仅 conservative 预计还需 ~3.7h
- 尚需跑 standard 和 aggressive 两个策略，总时间可能 10h+
- results.json 当前仅有之前测试的 3 题结果 (standard: 66.67%)

---
