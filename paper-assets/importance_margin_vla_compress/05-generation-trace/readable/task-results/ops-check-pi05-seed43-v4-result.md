# ops check pi05 seed43 v4 result

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_pi05_seed43_v4_result_20260523T074613_result.json`
- **Structured JSON:** [`0d7b49b735a81727e764.json`](../../sessions/0d/0d7b49b735a81727e764.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 已不存在，无需清除。

---

**实验结果汇总：**

| 项目 | 值 |
|------|-----|
| 实验 | eval_pi05_random_k09_object_seed43_v4 |
| 状态 | **DONE (success)** |
| SR | **9.6%** (48/500) |
| Episodes | 500 (完整) |
| 耗时 | 119.5 min |

**Cliff 验证结论：** seed42=12.0%, seed43=9.6%，两个 seed 在 random k=0.9 Object 上均极低（<15%），**cliff behavior 可复现**，非 seed 偶然。Random pruning 在 Object suite 即使只移除 10% token 也会导致性能崩塌。

---
