# check bootstrap v2 final status

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_bootstrap_v2_final_status_20260523T012854_result.json`
- **Structured JSON:** [`f810763c21e577c03e9c.json`](../../sessions/f8/f810763c21e577c03e9c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**实验仍在运行，2/20 conditions 完成。**

### 当前状态 (01:30 UTC)
| 卡 | 当前任务 | 阶段 | 进度 |
|---|---|---|---|
| cuda:0 | openvla_goal/untrained | Bootstrap (1000 iter, 100 workers) | 刚开始 |
| cuda:1 | tracvla_goal/untrained | Extraction | 1250/5000 |

GPU 进程活跃，0% GPU util 是因为当前阶段是 CPU-bound 的 bootstrap/extraction。

### 已完成结果 (2/20)

| Condition | Peak R² | Exit R² | Delta | CI 95% | 显著? |
|---|---|---|---|---|---|
| **openvla_goal/trained** | 0.4556 (L1) | 0.3395 (L31) | 0.116 | **[-0.2528, -0.0117]** | CI 全负 — bootstrap 下 exit > peak，方向反转 |
| **tracvla_goal/trained** | 0.5399 (L13) | 0.2065 (L31) | 0.334 | **[0.0546, 0.3416]** | CI 不含 0，drop 显著 |

### 预计完成时间
- cuda:0 (openvla×8 + nora×4 = 12 conditions): ~05:00 UTC
- cuda:1 (tracvla×8 = 8 conditions): ~05:30 UTC

早期结果符合假设：VLM→VLA (TracVLA) drop 显著，VLA→VLA (OpenVLA) drop 不显著（甚至 bootstrap 下反转）。需要等全部 20 conditions 完成后再下结论。

---
