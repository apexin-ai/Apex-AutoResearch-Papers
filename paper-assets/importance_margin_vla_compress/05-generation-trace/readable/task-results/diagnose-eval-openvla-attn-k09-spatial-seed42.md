# diagnose eval openvla attn k09 spatial seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_openvla_attn_k09_spatial_seed42_20260524T225823_result.json`
- **Structured JSON:** [`f21fe208ce404279e2bd.json`](../../sessions/f2/f21fe208ce404279e2bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成，registry 已更新为 DONE，cron 已清除。

**结果汇总：**

| 指标 | 值 |
|------|-----|
| **Overall SR** | **80.4% (402/500)** |
| 耗时 | 190.8 min |
| Attention pruning | k=0.9, 256→230 vision tokens |

**Per-task SR：**

| Task | SR |
|------|-----|
| 1. bowl between plate & ramekin → plate | 88.0% |
| 2. bowl next to ramekin → plate | 90.0% |
| 3. bowl from table center → plate | 90.0% |
| 4. bowl on cookie box → plate | 94.0% |
| 5. bowl in top drawer → plate | 74.0% |
| 6. bowl on ramekin → plate | **24.0%** |
| 7. bowl next to cookie box → plate | **96.0%** |
| 8. bowl on stove → plate | 90.0% |
| 9. bowl next to plate → plate | 78.0% |
| 10. bowl on wooden cabinet → plate | 80.0% |

Task 6（bowl on ramekin）显著低于其他任务（24%），与其他 pruning 配置的表现一致，是该 suite 的难点任务。

---
