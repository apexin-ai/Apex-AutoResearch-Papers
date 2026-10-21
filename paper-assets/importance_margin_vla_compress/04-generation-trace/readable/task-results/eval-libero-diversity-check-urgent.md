# eval libero diversity check urgent

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_libero_diversity_check_urgent_20260516T153157_result.json`
- **Structured JSON:** [`b218669508b01951e528.json`](../../sessions/b2/b218669508b01951e528.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果出来了。

## Diversity Check 结果 — LIBERO 10K Checkpoints

```
Full FT 10K:  diversity_std=0.1987 [PASS]
LoRA 10K:     diversity_std=0.1736 [PASS]
阈值: std > 0.05 = PASS
```

**两个模型都通过**，无 mode collapse。Full FT 的 diversity 略高于 LoRA（0.199 vs 0.174），均远超 0.05 阈值。

各 observation 的明细：

| | Obs 0 | Obs 1 | Obs 2 | Obs 3 | Obs 4 | Avg |
|---|---|---|---|---|---|---|
| **Full FT** | 0.193 | 0.192 | 0.203 | 0.193 | 0.213 | **0.199** |
| **LoRA** | 0.166 | 0.177 | 0.154 | 0.198 | 0.174 | **0.174** |

---
