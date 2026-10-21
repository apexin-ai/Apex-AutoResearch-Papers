# cron bjb1 32546 get pids

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cron_bjb1-32546-get-pids_20260520T175321_result.json`
- **Structured JSON:** [`ad76744bf7949f2ef9ce.json`](../../sessions/ad/ad76744bf7949f2ef9ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

| exp_id | GPU | PID | Registry | Cron |
|--------|-----|-----|----------|------|
| eval-obs-only-spatial-norm02-seed50 | cuda:0 | 542128 | ✓ | ✓ |
| eval-perdof-object-norm02-seed50 | cuda:1 | 542405 | ✓ | ✓ |
| eval-vla-only-object-seed49 | cuda:3 | 542620 | ✓ | ✓ |
| eval-obs-only-object-norm02-seed51 | cuda:4 | 542894 | ✓ | ✓ |

**GPU 利用率** (6/6 全部在用)：

| GPU | 利用率 | 显存占用 |
|-----|--------|---------|
| 0 | 35% | 5249/24564 MiB |
| 1 | 32% | 5265/24564 MiB |
| 2 | 27% | 4760/24564 MiB |
| 3 | 19% | 5167/24564 MiB |
| 4 | 33% | 5267/24564 MiB |
| 5 | 51% | 4940/24564 MiB |

另外注意到 GPU 2 和 GPU 5 上还跑着两个之前的实验（eval-k5-obs-only-object-seed44 和 eval-k20-obs-only-object-seed44），也在正常运行。

---
