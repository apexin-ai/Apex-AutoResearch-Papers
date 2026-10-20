# ops check running progress

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-running-progress_20260516T054137_result.json`
- **Structured JSON:** [`cb6fc7bc6cc4588f6353.json`](../../sessions/cb/cb6fc7bc6cc4588f6353.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

| 实验 | GPU | 当前 step / 总 steps | 进度 % | 预估剩余时间 |
|------|-----|---------------------|--------|-------------|
| contamination_60_tau07_seed42 | 0-3 | 5684 / 6103 | 93% | ~16 min |
| contamination_60_tau06_seed42 | 0-3 | 3754 / 6103 | 61% | ~1h 26min |
| grid_b0_1_seed42 | 0-3 | 1050 / 6103 | 17% | ~2h 58min |
| threshold_q03_seed42 | 0-3 | 60 / 6103 | 1% | ~3h 33min |

**GPU 状态**（4× H800 95GB）：

| GPU | 利用率 | 显存 |
|-----|--------|------|
| 0 | 84% | 46.5 / 95.6 GB |
| 1 | 99% | 46.5 / 95.6 GB |
| 2 | 94% | 46.5 / 95.6 GB |
| 3 | 94% | 46.5 / 95.6 GB |

速度约 2.1-2.3 s/it，4 个实验并行运行正常。第一个实验约 16 分钟内完成。

---
