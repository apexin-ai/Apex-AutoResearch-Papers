# check four experiments status

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_four_experiments_status_20260523T034112_result.json`
- **Structured JSON:** [`5c718159997123a3ebe4.json`](../../sessions/5c/5c718159997123a3ebe4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个实验全部存活，GPU 100% 利用率，无 final 目录。

| 实验 | GPU | Step | 进度 | 速度 | 预估剩余 |
|------|-----|------|------|------|---------|
| rho03_adaptive_seed456_r2 | 0 (28.7GB) | 401/6103 | 7% | 2.61s/it | ~4h08m |
| rho03_uniform_seed456 | 2 (26.2GB) | 1544/6103 | 25% | 2.45s/it | ~3h06m |
| bs8_nmin4_adaptive_seed123_r2 | 1 (48.3GB) | 873/6103 | 14% | 2.61s/it | ~3h47m |
| bs8_nmin4_uniform_seed123_r2 | 3 (48.3GB) | 880/6103 | 14% | 2.54s/it | ~3h41m |

磁盘：/root/autodl-tmp 250GB 用了 155GB，剩余 96GB (62%)。

注意：rho03_adaptive_seed456_r2 从 checkpoint-1000 恢复但进度条显示 401/6103，进度偏低，可能 step 计数被重置了。rho03_uniform_seed456 没有 resume 但跑得最快（已 25%），因为它不用 gradient_checkpointing 且更早启动。

---
