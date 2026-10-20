# ssh check reeval progress

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_reeval_progress_20260516T052109_result.json`
- **Structured JSON:** [`53b035bc89081a4295b8.json`](../../sessions/53/53b035bc89081a4295b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Re-eval 进度汇总

| 实验 | PID | GPU | 进度 (batch) | 进度 (docs≈) | 状态 | 预计剩余 |
|------|-----|-----|-------------|-------------|------|---------|
| reeval_flat_nli_s43_r2 | 291003 | cuda:3 | 191/247 | ~764/985 (77%) | 运行中 | ~40 min |
| reeval_ced_s44 | 297190 | cuda:0 | 76/247 | ~304/985 (31%) | 运行中 | ~2h20m |
| reeval_ced_s42 | 298018 | cuda:2 | 84/247 | ~336/985 (34%) | 运行中 | ~1h50m |
| reeval_flat_nli_s42 | 296732 | cuda:0 | 76/247 | ~304/985 (31%) | 运行中 | ~2h20m |

4 个进程全部存活，无 metrics.json 输出（均未完成）。

**GPU 显存:**
| GPU | 已用 / 总量 | 利用率 |
|-----|------------|--------|
| cuda:0 | 21.7GB / 32GB | 83% (跑 2 个 eval) |
| cuda:1 | 0 MB / 32GB | 0% |
| cuda:2 | 10.9GB / 32GB | 49% |
| cuda:3 | 11.1GB / 32GB | 49% |

**cuda:1 空闲可用**，显存占用 0。

---
