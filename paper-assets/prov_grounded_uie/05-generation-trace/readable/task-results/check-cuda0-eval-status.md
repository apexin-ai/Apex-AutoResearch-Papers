# check cuda0 eval status

**prov grounded uie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_cuda0_eval_status_20260513T105353_result.json`
- **Structured JSON:** [`703a2d4676994a9432f9.json`](../../sessions/70/703a2d4676994a9432f9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**cuda:0 被 eval 占用，正在运行中。**

| 指标 | 值 |
|------|-----|
| GPU 0 利用率 | 100% |
| GPU 0 显存占用 | 59665 MiB |
| GPU 1 | 空闲 (0%, 0 MiB) |

GPU 0 上有 3 个 python 进程（PID 104325/104686/104918），合计占用 ~60GB 显存。

日志 `/tmp/grpo_v2_final_eval.log` 显示模型 checkpoint 刚加载完（4/4 shards loaded），eval 刚启动不久。`eval_results.json` 尚未生成——eval 仍在进行中。

---
