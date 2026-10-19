# ops post restart healthcheck 2

**tbab multi turn** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_post-restart-healthcheck-2_20260518T162639_result.json`
- **Structured JSON:** [`82c23c36635cdd3b0101.json`](../../sessions/82/82c23c36635cdd3b0101.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部进程存活，汇总如下：

| 进程 | 状态 | 进度 | 备注 |
|---|---|---|---|
| **mvp_c4_s137 训练** (PID 46199) | **存活** | 269/471 (57%), 运行 1h22m | ~12-25s/it, 预计还需 ~1h24m |
| **eval_c4_s42** (tmux) | **存活** | 28/91 (31%) | 当前跑 HumanEval/71 |
| **eval_c1_s137** (tmux) | **存活** | 20/91 (22%) | 当前跑 HumanEval/17 |

**GPU 状态** (RTX PRO 6000, 98GB):
- 利用率：100%
- 显存：74,489 / 97,887 MiB (76%)
- 3 个进程占用：训练 ~41GB, eval_c4_s42 ~17GB, eval_c1_s137 ~16GB

**eval 结果文件**：
- `c4_s42_code_n1/results_full_tbab.jsonl` — 5.5KB, 持续写入中
- `c1_s137_code_n1/results_lora_only.jsonl` — 3.9KB, 持续写入中

所有进程正常运行，无需干预。

---
