# check westd41074 status 20250525

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_westd41074_status_20250525_20260525T230839_result.json`
- **Structured JSON:** [`106d343471f841d7f4f9.json`](../../sessions/10/106d343471f841d7f4f9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
GPU0: [运行中] eval_openvla_random_k05_object_seed42_v2 — 未被 kill，Task 6/10 ~ep40/50
GPU1: [运行中] eval_openvla_l2norm_k05_object_seed42_v2 — 未被 kill，Task 5/10 ~ep40/50
              eval_pi05_attention_k0925_long_seed42 — Task 6/10 ep30/50 (T6: 17% SR)
GPU2: [运行中] eval_openvla_attn_k085_long_seed42 — 刚启动，Task 1/10 ep20/50 (0% SR)
GPU3: [空闲]   zeromask_l2norm 已完成 (2026-05-25 22:44 UTC)

空闲 GPU: GPU3
```

**注意**: GPU0/GPU1 的 random_k05 和 l2norm_k05 实验 **并未被 kill**，仍在运行并占用 GPU。

---

### zeromask L2norm 结果（已完成）

**Overall SR: 68.8%** (344/500)

Per-task:
| Task | SR |
|------|-----|
| alphabet soup | 84% |
| cream cheese | 62% |
| salad dressing | 88% |
| bbq sauce | 26% |
| ketchup | 82% |
| tomato sauce | 54% |
| butter | 62% |
| milk | 82% |
| chocolate pudding | 60% |
| orange juice | 88% |

### 2×2 Zeromask 对比表（完整）

| | Random | L2norm |
|---|---|---|
| **hard-prune** | 62.8% | 70.6% |
| **zeromask** | 71.8% | **68.8%** |

解读：
- hard-prune 下 L2norm >> Random（70.6 vs 62.8），说明 L2norm 选的 token 确实更重要
- zeromask 下 Random ≈ L2norm（71.8 vs 68.8），甚至 Random 略高
- zeromask Random (71.8%) 最高，说明零掩码 + 随机选择的组合保留了更多信息冗余

---

### π0.5 Profiling 结果（已完成）

| k | Median (ms) | P5-P95 | Speedup |
|---|---|---|---|
| 1.0 (baseline) | 209.88 | 197.76–221.67 | — |
| 0.9 | 206.36 | 171.43–225.03 | 1.7% |
| 0.5 | 201.87 | 189.21–211.31 | 4.0% |

Speedup 很小（k=0.5 仅 4%），vision token pruning 对 π0.5 推理延迟影响有限。

---
