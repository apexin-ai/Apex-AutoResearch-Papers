# collect westd evals and next

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_collect_westd-evals-and-next_20260515T072436_result.json`
- **Structured JSON:** [`7b444d26c370c77cd63c.json`](../../sessions/7b/7b444d26c370c77cd63c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

---

### 1. ckpt-1600 test@8192 (s42) — 完整指标

| 指标 | 值 |
|------|-----|
| **Accuracy** | **84.99%** |
| F1 macro | 78.94% |
| F1 fail | 67.65% (P=81.06%, R=58.05%) |
| F1 pass | 90.22% (P=85.93%, R=94.97%) |
| Majority baseline | 72.96% |
| Gap vs majority | +12.03pp |
| Unparseable | 0 |
| Total samples | 9,784 |

**s42 test curve 完整：** 400:84.79% → 600:79.05% → 800:83.53% → 1000:83.52% → 1200:83.84% → 1400:85.47% → **1600:84.99%**

ckpt-1400 仍是 test-best (85.47%)，ckpt-1600 略降但差距很小。

---

### 2. seed123 ckpt-6600 val@8192 — 完整指标

| 指标 | 值 |
|------|-----|
| **Accuracy** | **87.23%** |
| F1 macro | 79.02% |
| F1 fail | 65.90% (P=92.60%, R=51.15%) |
| F1 pass | 92.14% (P=86.40%, R=98.70%) |
| Majority baseline | 75.88% |
| Gap vs majority | +11.36pp |
| Unparseable | 9 |
| Total samples | 9,335 |

---

### 3. ckpt-6400 val@8192 提交确认

已提交到 cuda:3，PID=343011，tmux session: `cls8b-seed123-ckpt6400-val8192-eval`

---

### 4. GPU 状态

| GPU | 状态 |
|-----|------|
| cuda:0 | **空闲** (0%, 0 MiB) |
| cuda:1 | 占用 (95%, 27.3GB) |
| cuda:2 | 占用 (96%, 30.7GB) |
| cuda:3 | 刚提交 ckpt-6400 eval |

---
