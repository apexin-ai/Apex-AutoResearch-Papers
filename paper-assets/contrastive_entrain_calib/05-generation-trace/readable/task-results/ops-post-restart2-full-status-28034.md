# ops post restart2 full status 28034

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_post-restart2-full-status-28034_20260519T131046_result.json`
- **Structured JSON:** [`21a925e7b2a7d37d6dbd.json`](../../sessions/21/21a925e7b2a7d37d6dbd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### GPU 0: exp-004 multi-checkpoint eval — 进行中
- PID 134064 运行中（9h50m）
- 当前：ckpt500 评估中，**60/362** samples（~17%）
- 每 20 samples 约 3 分钟，预计 ckpt500 还需 ~45 分钟完成
- 尚无结果 JSON 产出
- GPU 占用 17.6GB / 32GB, 19% util

### GPU 3: exp-016 ActAdd 5-alpha re-eval — 进行中
- PID 126897 运行中（2h37m）
- 5 个 alpha (0, 0.5, 1.0, 2.0, 5.0)
- alpha=0.0 和 0.5 已完成，当前 **alpha=1.0 at 220/362**（~61%）
- 进度约 2.6/5 alphas，预计还需 ~1.5h
- 结果目录为空（尚未写出 JSON）
- GPU 占用 16.5GB / 32GB, 18% util

### GPU 1+2: exp-008v3 DCGRPO 训练 — 进行中
- **Step 1163/8000（15%）**，已跑 6h29m
- 最新 reward: combined_mean ≈ 0.62, r1_mean=0.5, r3_mean=0.66
- 预计剩余 ~36h（22s/it 估算）
- GPU 1: 31.4GB / 32GB, GPU 2: 30.7GB / 32GB

### GPU 可用性
| GPU | 占用 | 可用 |
|-----|------|------|
| 0 | exp-004 eval | **否** |
| 1 | exp-008v3 训练 | **否** |
| 2 | exp-008v3 训练 | **否** |
| 3 | exp-016 eval | **否** |

**4 卡全部占满，当前无法部署 exp-002v3。** 最早可用的是 GPU 0 和 GPU 3，预计分别在 ~1h 和 ~1.5h 后释放（取决于 eval 剩余 checkpoints 数量）。

---
