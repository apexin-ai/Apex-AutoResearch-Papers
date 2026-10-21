# diag all experiments progress

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_all-experiments-progress_20260519T045704_result.json`
- **Structured JSON:** [`97714c9ead1c6d3ff897.json`](../../sessions/97/97714c9ead1c6d3ff897.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 全实验进度快照

### westd-29046 (2× RTX PRO 6000, 98GB each)

| 实验 | GPU | PID | 状态 | Step | 进度 | 最近指标 | 预计完成 |
|------|-----|------|------|------|------|----------|----------|
| **exp-002v2** (DCGRPO cosine) | 0 | 130467 | ✅ 运行中 | ~344/8000 | 4.3% | r1_mean=-0.02, combined=0.41 | ~May 22 06:00 (~66h) |
| **exp-003** (R3-only) | 1 | 70649 | ✅ 运行中 | 1530/8000 | 19.1% | r3_mean=0.40~0.77, combined=0.40~0.77 | ~May 21 15:00 (~50h) |

- exp-002v2: ~31s/step, 10:09 启动, combined_mean 在 0.17~0.55 间波动
- exp-003: ~28s/step, 00:51 启动, 只训 R3 reward, r3_mean 波动较大 (0.40~0.77)

### westd-28034 (4× RTX 5090, 32GB each)

| 实验 | GPU | PID | 状态 | Step | 进度 | 最近指标 | 预计完成 |
|------|-----|------|------|------|------|----------|----------|
| **exp-004** (ACT baseline) | 0 | 18204 | ✅ 运行中 | 5120/8000 | 64.0% | l2=0.0012, sft=0.0000 | ~May 19 20:30 (~7.5h) |
| **exp-014** (Continuous Probe) | 1,2 | 40314/40315 | ✅ 运行中 | 2710/8000 | 33.9% | r1=0.85, r3=0.99, combined=0.97 | ~May 20 09:00 (~20h) |
| **exp-016** (ActAdd Steering) | 3 | 85458 | ✅ 运行中 | — | eval中 | results_summary.json 已产出 | 持续评估中 |

- exp-004: ~9.2s/step, 今天最先完成
- exp-014: DeepSpeed 2-GPU, ~13.8s/step, r1/r3 reward 都很高 (combined 接近 0.97)
- exp-016: 不在原始列表中，正在 GPU 3 上运行 ActAdd steering 评估

### 注意事项
- exp-004 的 dry-run launch log 显示过一次 OOM，但实际训练进程正常运行且已到 64%
- exp-016 是额外发现的实验，已产出评估结果文件

---
