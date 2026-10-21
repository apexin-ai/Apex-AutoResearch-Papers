# eval downstream monitor v2

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_downstream_monitor_v2_20260519T192139_result.json`
- **Structured JSON:** [`68297901f9b36718179d.json`](../../sessions/68/68297901f9b36718179d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

首轮检查完成。3 个进程均在运行：
- **adaptive_seed123** (339293): loglikelihood ~64%，预计几分钟内完成
- **adaptive_seed456** (339451): loglikelihood 刚开始
- **uniform_seed123** (339620): 数据集加载阶段

3 分钟后再次轮询。adaptive_seed123 最快，完成后会在其 GPU 上启动 uniform_ood_seed456。

---
