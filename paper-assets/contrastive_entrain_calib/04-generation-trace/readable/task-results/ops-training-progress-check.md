# ops training progress check

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_training-progress-check_20260523T040420_result.json`
- **Structured JSON:** [`ad4dd07fff9e6a167c17.json`](../../sessions/ad/ad4dd07fff9e6a167c17.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练进度汇总

### westd-28034 GPU:1 — exp-004-reduced-lora (PID 30011)

| 指标 | 值 |
|------|-----|
| 当前 step | **5790 / 8000** (72.4%) |
| 每 step 耗时 | **~6.76s** |
| 剩余 steps | 2210 |
| 预估完成时间 | **~2026-05-23 16:15 UTC** (~4h 10min后) |
| 最新 checkpoint | **checkpoint-5500** |
| GPU | RTX 5090, 21770MiB / 32607MiB, **48%** util |
| 最新 loss | l2≈0.0019, total=0.0002 |

---

### westd-29046 GPU:0 — exp-003-gs8 (PID 516696)

| 指标 | 值 |
|------|-----|
| 当前 step | **1696 / 8000** (21.2%) |
| 每 step 耗时 | **~25.5s** |
| 剩余 steps | 6304 |
| 预估完成时间 | **~2026-05-25 08:45 UTC** (~44.7h后) |
| 最新 checkpoint | **checkpoint-1500** |
| GPU | RTX PRO 6000 Blackwell, 38197MiB / 97887MiB, **95%** util |
| 最新 reward | mean≈0.52-0.58 |

---

### westd-29046 GPU:1 — exp-003-len512-v3 (PID 553700)

| 指标 | 值 |
|------|-----|
| 当前 step | **130 / 8000** (1.6%) |
| 每 step 耗时 | **~49.8s** |
| 剩余 steps | 7870 |
| 预估完成时间 | **~2026-05-28 01:00 UTC** (~108.9h / 4.5天后) |
| 最新 checkpoint | **无**（首个 checkpoint 在 step 500） |
| GPU | RTX PRO 6000 Blackwell, 41337MiB / 97887MiB, **95%** util |
| 最新 reward | mean≈0.46, clipped_ratio=0.95-0.98 |

---

**要点：**
- exp-004 今天下午就能跑完
- exp-003-gs8 预计后天上午完成
- exp-003-len512 每 step 比 gs8 慢近一倍（49.8s vs 25.5s），主要因为 max_completion_length=512 导致 generation 更长，completions/clipped_ratio 高达 0.95-0.98，预计 5月28日才能完成

---
