# fix restart all evals correct params

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_restart_all_evals_correct_params_20260519T100242_result.json`
- **Structured JSON:** [`d5ae96b60f33e5758bd0.json`](../../sessions/d5/d5ae96b60f33e5758bd0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**已完成操作：**
1. **确认 seed42 参数**：已有 eval 结果都用 `num_episodes_per_task: 50`，与 50/task 一致
2. **Kill 4 个旧进程**（PID 81335, 762597, 763352, 764778）：全部用了错误的 `--num_episodes 500`
3. **重启 4 个 eval**，全部用 `--num_episodes 50`：

| GPU | Experiment | PID | Checkpoint |
|-----|-----------|-----|------------|
| cuda:3 | eval_smart_compress_m32_official | 160116 | m32_official (seed42) |
| cuda:0 | eval_smart_compress_m32_seed44_v2 | 160877 | m32_seed44 |
| cuda:1 | eval_smart_compress_m64_seed44_v2 | 162254 | m64_seed44 |
| cuda:2 | eval_smart_compress_m96_seed44_v2 | 164042 | m96_seed44 |

4. **Registry 更新**：旧 3 个 seed44 eval 标记为 DONE/killed，4 个新实验注册为 RUNNING

---
