# ops batch64 faulthandler restart

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_batch64_faulthandler_restart_20260517T083602_result.json`
- **Structured JSON:** [`bffdb79676c251ef1db3.json`](../../sessions/bf/bffdb79676c251ef1db3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

1. **faulthandler 已添加** — 在 `train.py` 第 16 行后插入 `import faulthandler; faulthandler.enable()`
2. **原 checkpoint (step_000267) 损坏** — `PytorchStreamReader failed reading zip archive`，文件写入不完整，已删除
3. **训练已从 step 0 重启** — tmux session `batch64_v2`，GPU 0，从 step 0 开始，loss=1.5052 正常
4. 配置：`grad_accum=16, effective_batch=64, total_steps=100000`

无法从 checkpoint 恢复是因为上次进程被 kill 时 checkpoint 正在写入（文件只有 ~102MB 且 zip 结构不完整）。下次 save_every=2000 时会生成新的有效 checkpoint。

---
