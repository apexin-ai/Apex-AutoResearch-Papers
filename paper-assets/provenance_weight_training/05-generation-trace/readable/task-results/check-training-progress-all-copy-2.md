# check training progress all

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_training_progress_all_20260523T033017_result.json`
- **Structured JSON:** [`791d068ab35d518dbf5e.json`](../../sessions/79/791d068ab35d518dbf5e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个进程全部存活，GPU 满载运行。

| 实验 | GPU | Step | 进度 | Loss (weighted) | 速度 | 已跑 | 预估剩余 |
|------|-----|------|------|-----------------|------|------|----------|
| rho03_adaptive_seed456_r2 | cuda:0 (29GB) | 152/6103 | 2.5% | 2.958 | 2.63s/it | ~7min | **~4h21m** |
| rho03_uniform_seed456 | cuda:2 (26GB) | 1277/6103 | 21% | 2.761 (b=0) | 2.45s/it | ~11min | **~3h17m** |
| bs8_nmin4_adaptive_seed123_r2 | cuda:1 (48GB) | 623/6103 | 10% | 2.107~2.784 | 2.58s/it | ~5min | **~3h56m** |
| bs8_nmin4_uniform_seed123_r2 | cuda:3 (48GB) | 625/6103 | 10% | 1.883 (b=0) | 2.54s/it | ~5min | **~3h52m** |

备注：
- rho03_uniform_seed456 从 ckpt-1000 恢复，进度最快；bs8 两组从 ckpt-500 恢复；adaptive_r2 从头训练所以最慢
- uniform 组 b=0 符合预期（无 reweighting）
- 磁盘 `/root/autodl-tmp`: 152G/250G (61%)，剩余 99G，空间充足

---
