# ops confirm batch64 status

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_confirm_batch64_status_20260517T111244_result.json`
- **Structured JSON:** [`702fad57a86817591f12.json`](../../sessions/70/702fad57a86817591f12.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**batch64_v2 训练状态报告**

| 项目 | 值 |
|------|-----|
| tmux session | `batch64_v2` — 运行中 |
| PID | 23996 |
| 当前 step | **1300 / 100,000** (1.3%) |
| 最近 loss | 0.1337 (step 1300) |
| 学习率 | 1.00e-04 (warmup 已完成) |
| 速度 | ~0.1 sps (~5.7 min/50 steps) |
| GPU | **GPU 0** (RTX 4090 D), 2718MiB / 24564MiB, 84W |
| 运行时间 | ~2.5h (16:38 启动至现在 19:13) |

Loss 趋势正常，从 step 850 的 0.1446 降至 step 1300 的 0.1337，warmup 在 step 1000 完成 (lr=1e-4)。按当前速度，预计总训练时间约 **560 小时 (~23 天)**。

---
