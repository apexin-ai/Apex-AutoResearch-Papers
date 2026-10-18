# monitor v8 early loss retry

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_v8-early-loss-retry_20260515T232440_result.json`
- **Structured JSON:** [`13c7472c47166b052004.json`](../../sessions/13/13c7472c47166b052004.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程存活，训练已超过 step 250。日志每 50 步记录一次，以下是完整趋势：

| Step | Total Loss | Action Loss | Margin Loss | Δ (margin) | Grad Norm | SPS |
|------|-----------|-------------|-------------|------------|-----------|-----|
| 0 | 0.2770 | 0.2770 | 0.2976 | 0.0024 | 1.60 | 0.6 |
| 50 | 0.3150 | 0.3125 | 0.2996 | 0.0004 | 1.64 | 3.0 |
| 100 | 0.3561 | 0.3511 | 0.2994 | 0.0006 | 1.78 | 3.1 |
| 150 | 0.3088 | 0.3014 | 0.2977 | 0.0023 | 2.71 | 3.1 |
| 200 | 0.2238 | 0.2141 | 0.2911 | 0.0089 | 1.38 | 3.2 |
| 250 | 0.0590 | 0.0478 | 0.2689 | 0.0311 | 1.03 | 3.2 |

**健康判定: 正常，趋势良好。**

关键观察：
- **Action loss** 显著下降：0.277 → 0.048（step 100 有短暂上升后快速回落，典型的 warmup 阶段行为）
- **Margin loss** 缓慢下降：0.298 → 0.269，符合预期（margin loss 变化慢）
- **Δ (importance margin)** 持续增大：0.002 → 0.031，说明模型正在学会区分重要/不重要参数，gradient isolation 在起作用
- **Grad norm** 稳定在 1.0–2.7，无梯度爆炸
- **训练速度** 稳定 ~3.1 sps，无异常减速
- 无 warning/error

---
