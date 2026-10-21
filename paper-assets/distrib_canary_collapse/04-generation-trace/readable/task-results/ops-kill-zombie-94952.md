# ops kill zombie 94952

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-zombie-94952_20260515T115110_result.json`
- **Structured JSON:** [`4bc378244432a4c0763f.json`](../../sessions/4b/4bc378244432a4c0763f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程已成功 kill。

**Kill 前状态**：
- PID 94952，PPID 1（孤儿进程），状态 `Rl`
- 运行时间 4h50min，CPU 4104%，内存 0.8%，GPU 0%
- 命令：`python -u iterative_train.py --seed 43 --data_dir data/wikitext103_5k --steps_per_gen 10 --num_generations 1 --synthetic_ratio 0.25 --output_dir /tmp/dryrun_a025_s43`

**结果**：SIGTERM 即终止，未需要 SIGKILL。

---
