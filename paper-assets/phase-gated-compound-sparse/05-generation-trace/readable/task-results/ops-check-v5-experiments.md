# ops check v5 experiments

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-v5-experiments_20260514T023043_result.json`
- **Structured JSON:** [`87dbf5ab26b64dcd81dd.json`](../../sessions/87/87dbf5ab26b64dcd81dd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个实验全部存活，运行正常：

| 实验 | 进度 | ETA |
|------|------|-----|
| mvp_v5_fixed_s020_r2 (GPU 0) | **29/50** | ~10:45 UTC |
| mvp_v5_fixed_s030_r2 (GPU 1) | **29/50** | ~10:45 UTC |
| mvp_v5_random_s015 (GPU 2) | **20/50** | ~10:49 UTC |
| mvp_v5_random_s025 (GPU 3) | **20/50** | ~10:49 UTC |

GPU 利用率正常。Importance 实验（GPU 0/1）VRAM 更高（33.5 GB vs 26.6 GB），GPU 利用率反而较低（76-78% vs 99%）。输出目录均为空，结果在 50/50 完成后一次性写入。预计全部完成时间约 10:49 UTC（~18 分钟后）。

状态报告已写入 `artifacts/v5_status_check.md`。

---
