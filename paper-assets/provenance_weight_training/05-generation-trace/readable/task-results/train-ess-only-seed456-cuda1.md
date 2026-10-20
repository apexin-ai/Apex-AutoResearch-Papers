# train ess only seed456 cuda1

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_ess_only_seed456_cuda1_20260517T153230_result.json`
- **Structured JSON:** [`ccdefd0eed5fa8007446.json`](../../sessions/cc/ccdefd0eed5fa8007446.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已确认 ess_only_seed456 在 cuda:1 上启动成功：

- **PID**: 115525
- **GPU 显存**: 46530MiB / 97887MiB
- **GPU 利用率**: 96%
- **tmux session**: `ess_only_seed456`
- **脚本修复**: 添加 `WANDB_MODE=disabled`，删除 wandb 参数，`save_steps` 改为 500 对齐 `eval_steps`

当前 4 张 GPU 全部在用（GPU0/1/2/3）。

---
