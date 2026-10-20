# check gpu progress quick

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gpu_progress_quick_20260521T143054_result.json`
- **Structured JSON:** [`600a3d69f9da2bf74274.json`](../../sessions/60/600a3d69f9da2bf74274.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

| GPU | 显存占用 | 利用率 | 实验 | Step/Total | ETA |
|-----|---------|--------|------|-----------|-----|
| 0 | 45.6 GB | 100% | detect_remove_q05_seed42 | 5229/6103 (86%) | ~30 min |
| 1 | 90.2 GB | 100% | bs16_adaptive_tau07_seed42 | 1218/6103 (20%) | ~3h20m |
| 2 | 90.2 GB | 100% | bs16_uniform_seed42 | 671/6103 (11%) | ~3h40m |
| 3 | 45.6 GB | 97% | random_reweight_baseline_seed42 | 4359/6103 (71%) | ~1h06m |

GPU 0 的 detect_remove 实验最快完成，约 30 分钟后结束。GPU 1/2 上的 bs16 实验显存占用翻倍（90GB），速度较慢，预计还需 3+ 小时。

---
