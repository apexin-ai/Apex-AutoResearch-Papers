# debug check v7 2 eval code version

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_check-v7_2-eval-code-version_20260515T221625_result.json`
- **Structured JSON:** [`f64e30abc257562c1bbd.json`](../../sessions/f6/f64e30abc257562c1bbd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Fix 未生效，eval 需要重跑。**

证据：`eps0.0_pruneFalse` 的 action_loss = **0.0275**，接近修复前膨胀值 0.03，远高于修复后合理值 0.01。其他已完成 condition 同样偏高：
- `eps0.0_pruneTrue`: 0.0291
- `eps0.01_pruneFalse`: 0.0274

Eval 目前仍在运行（正在跑 `eps0.01_pruneTrue`），JSON 结果文件尚未生成。但已有数据足以判定——eval 进程使用的是 bug fix 之前的代码。

---
