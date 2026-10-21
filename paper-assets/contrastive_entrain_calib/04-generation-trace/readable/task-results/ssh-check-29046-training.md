# ssh check 29046 training

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-29046-training_20260522T052258_result.json`
- **Structured JSON:** [`33411825778023bd537d.json`](../../sessions/33/33411825778023bd537d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

| 实验 | Step | 进度 | Loss | Reward (mean) | GPU 利用率 | ETA |
|------|------|------|------|--------|------------|-----|
| **exp-003-s2** (R3-only, GPU0, PID 237432) | 6589 / 8000 | 82% | 0.0006 | 0.582 | 97%, 38G/97G | ~今晚 23:30 UTC |
| **exp-004-s2** (ACT, GPU1, PID 447710) | 430 / 8000 | 5.4% | sft=0.0019, total=0.0027 | — | 38%, 23G/97G | ~明天 08:00 UTC |

**ckpt-6500**: 已生成，路径 `/root/autodl-tmp/checkpoints/exp003_r3only_seed2/checkpoint-6500/`（May 22 12:45 写入）。已有全部 checkpoints: 500 ~ 6500（每 500 步一个）。

**关键指标 exp-003-s2 最近**：loss=0.0006, reward=0.582, kl=0.016, lr=3.9e-06, ~25.8s/step。还剩约 1411 步，约 10 小时完成。

**exp-004-s2**：刚启动约 1 小时，~8.9s/step，loss 已从 0.23 快速下降到 0.002。还需约 18.7 小时。GPU1 利用率偏低（38%），可能是 batch 间 data loading 开销。

---
