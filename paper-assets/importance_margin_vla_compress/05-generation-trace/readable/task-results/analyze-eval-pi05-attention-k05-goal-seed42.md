# analyze eval pi05 attention k05 goal seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_pi05_attention_k05_goal_seed42_20260523T210642_result.json`
- **Structured JSON:** [`c38e470bbc6047a4557a.json`](../../sessions/c3/c38e470bbc6047a4557a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果：π0.5 Attention k=0.5 Goal seed42

### 总体

| 指标 | 值 |
|---|---|
| **Overall SR** | **70.2%** |
| Total successes | 351 / 500 |
| Total episodes | 500 (50 × 10 tasks) |
| 耗时 | 84.9 min |
| 错误/异常 | 无（EXIT_CODE=0） |

### 每个 Task

| Task | SR |
|---|---|
| T0: open the middle drawer of the cabinet | 76% |
| T1: put the bowl on the stove | 40% |
| T2: put the wine bottle on top of the cabinet | 76% |
| T3: open the top drawer and put the bowl inside | 68% |
| T4: put the bowl on top of the cabinet | **94%** |
| T5: push the plate to the front of the stove | 70% |
| T6: put the cream cheese in the bowl | 54% |
| T7: turn on the stove | **100%** |
| T8: put the bowl on the plate | 86% |
| T9: put the wine bottle on the rack | 38% |

### 与 Random Goal k=0.5 (73.6%) 对比

**Attention 70.2% < Random 73.6%，差 3.4pp。Attention 在 π0.5 Goal 上确实不如 Random pruning。**

这与 π0.5 Object 的 pattern 一致（attention k=0.7 → 0.6% cliff），进一步确认 **attention scores 在 π0.5 上是 anti-informative**——用 attention 选 token 比随机选更差。

结合 X-VLA 的结果（attention Goal k=0.5 = 98.2%），2×2 crossover 叙事成立：
- X-VLA: attention 有效（98.2%），random 差
- π0.5: attention 反向（70.2%），random 更好（73.6%）

JSON 结果已保存在服务器：`/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_attention_k0.50_libero_goal_seed42.json`。日志中无 W&B run ID。

---
