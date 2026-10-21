# ops check westd27271 l2norm k07 seed43

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-westd27271-l2norm-k07-seed43_20260520T221501_result.json`
- **Structured JSON:** [`14a76e21ba8c5b260793.json`](../../sessions/14/14a76e21ba8c5b260793.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## 结果汇总

| 指标 | 值 |
|------|-----|
| **Success Rate** | **74.0%** (370/500) |
| **Wilson CI 95%** | [0.700, 0.777] |
| Seed | 43 |
| 耗时 | 237.8 min |

**Per-task 分布**：ketchup 最高 (96%)，bbq_sauce 最低 (46%)，butter 偏低 (58%)。

**关键发现**：假设预期 seed43 ≈ seed42 的 49.8%，但实际 seed43 得到 **74.0%**，差距巨大（+24.2pp）。结果 JSON 中 `mode: "baseline"`, `k_ratio: null` 的 metadata 异常，**这很可能实际跑的是 baseline（未剪枝）而非 k=0.7 剪枝模型**。建议核查 eval 脚本是否正确应用了 L2 norm pruning。

**GPU 状态**：
- GPU 0: 空闲（0%, 0 MiB）
- GPU 1: 无计算但占用 42 GiB 显存

---
