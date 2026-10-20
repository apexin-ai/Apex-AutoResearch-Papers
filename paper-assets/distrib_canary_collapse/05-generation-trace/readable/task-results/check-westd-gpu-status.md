# check westd gpu status

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_westd_gpu_status_20260525T190231_result.json`
- **Structured JSON:** [`c78aad12e392f2f9a504.json`](../../sessions/c7/c78aad12e392f2f9a504.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

| 项目 | 详情 |
|------|------|
| **GPU 数量** | 1 张 |
| **型号** | NVIDIA RTX PRO 6000 Blackwell Server Edition |
| **显存** | 97,887 MiB (~96GB) |
| **显存占用** | 0 MiB |
| **GPU 利用率** | 0% |
| **运行进程** | 无 |
| **Driver** | 580.119.02 |
| **CUDA** | 13.0 |

**C2-s42 输出目录** (`a050_s42_fp32/`): 完整，gen_0 ~ gen_10 + `all_metrics.json` + `config.json` + `analysis/` + `EXIT_CODE` 均存在。

`tmux ls` 被 read-only 白名单拦截，无法执行。GPU 当前完全空闲，可用。

---
