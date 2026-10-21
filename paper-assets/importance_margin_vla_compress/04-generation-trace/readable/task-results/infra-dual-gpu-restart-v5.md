# infra dual gpu restart v5

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_dual-gpu-restart-v5_20260515T153156_result.json`
- **Structured JSON:** [`087c38198ad1ccca11fe.json`](../../sessions/08/087c38198ad1ccca11fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

---

**产出汇总：**

| 实验 | Registry ID | GPU | PID | 当前 Step | Loss | SPS |
|------|-------------|-----|-----|-----------|------|-----|
| Baseline | `mvp_baseline_v5` | cuda:0 (41%, 2279 MiB) | 31871 | 300/30000 | 0.114 | 3.7 |
| IMM Anchor | `mvp_imm_anchor_v5` | cuda:1 (79%, 2459 MiB) | 32009 | 250/30000 | 0.054 | 3.2 |

- 两个实验均已进入训练循环，日志无报错
- Registry 状态均已推进至 RUNNING
- Cron 监控已注册（每 12 分钟检查进程存活 + 最新 step/loss）

---
