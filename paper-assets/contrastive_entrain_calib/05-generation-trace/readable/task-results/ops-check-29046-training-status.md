# ops check 29046 training status

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-29046-training-status_20260519T111012_result.json`
- **Structured JSON:** [`8b4c57abd0767492faee.json`](../../sessions/8b/8b4c57abd0767492faee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练状态报告

### GPU 状态
| GPU | 利用率 | 显存占用 | 温度 |
|-----|--------|----------|------|
| 0 (exp002v2-recalib) | 68% | 66,907 MiB | 61°C |
| 1 (exp-003) | 95% | 38,161 MiB | 67°C |

两卡正常运行。

---

### exp-003 (R3-only GRPO, GPU 1)

- **进度**: step 2287 / 8000 (**28.6%**)
- **已运行**: ~18h 19m
- **ETA**: ~41h 40m (约 5/21 中午)
- **速度**: ~26-28 s/step
- **Reward**: R3 only (d_syc 未加载，仅返回 R3 reward)
  - R3 mean 在 0.25-0.67 之间波动，combined_mean 同步
- **注意**: 日志持续出现 `d_syc not loaded; returning R3-only rewards` warning，符合 R3-only 设计预期

---

### exp002v2-recalib (Cosine + Recalib, GPU 0)

- **进度**: step 1208 / 8000 (**15.1%**)
- **已运行**: ~4h 30m
- **ETA**: ~37h (约 5/21 上午)
- **速度**: ~20 s/step
- **Reward 趋势** (最近 8 步):
  - **R1 mean: -0.11 ~ +0.03** — 仍在零附近波动，未见改善
  - R2 mean: -0.06 ~ -0.08
  - R3 mean: 0.56 ~ 1.00 (波动大)
  - combined mean: 0.39 ~ 0.73

**R1 信号问题**: R1 reward 仍然 ≈ 0（甚至轻微负值），recalib 似乎未能有效放大 cosine 信号。1200 步后 R1 仍无正向趋势，需要关注是否 scaling 参数不足或 cosine similarity 本身区分度太低。

---
