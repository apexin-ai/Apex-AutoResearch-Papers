# diagnose acis k07 final

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_acis_k07_final_20260517T073515_result.json`
- **Structured JSON:** [`34ef52047e87e3569e99.json`](../../sessions/34/34ef52047e87e3569e99.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练**仍在进行中**，未完成。

当前状态：
- **Step**: 4950/10000（截至 15:36:50 UTC）
- **Speed**: ~4.1 sps
- **margin_loss**: 波动在 0.07-0.28 之间，趋势下降
- **ETA**: 剩余 ~5050 steps / 4.1 sps ≈ 20 分钟 → **预计 ~15:57 UTC 完成**

注意：训练在 15:16 UTC 被重启（tmux session 重建于 15:16:34），这解释了 cron 之前报告"进程退出"。当前跑的是从头开始的新 run（wandb run `8r6bfv8x`），PID 11257 正常运行在 GPU 2 上。

不更新 registry 状态，保留 cron 继续监控。

---
