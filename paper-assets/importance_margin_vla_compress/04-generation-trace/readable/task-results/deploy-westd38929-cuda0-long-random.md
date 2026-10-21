# deploy westd38929 cuda0 long random

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd38929_cuda0_long_random_20260522T190956_result.json`
- **Structured JSON:** [`4d9ca41a112b9cb6dc81.json`](../../sessions/4d/4d9ca41a112b9cb6dc81.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

cuda:0 VRAM 目前 4 MiB（模型正在加载中），日志确认进程已启动：

- **exp_id**: `eval_pi05_random_k09_long_seed42`
- **配置**: Random k=0.9, LIBERO-Long (libero_10), 50 episodes, seed 42, cuda:0
- **日志**: `logs/eval_pi05_random_k09_long_seed42.log`

模型加载完成后 VRAM 会升至 ~10GB。L2norm k=0.85 Long 日志不存在，无结果可收割。其余 GPU (1/2/3) 未受影响。

---
