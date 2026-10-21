# analyze eval pi05 random k085 long seed42 postfix v3

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_pi05_random_k085_long_seed42_postfix_v3_20260525T114904_result.json`
- **Structured JSON:** [`e699bc6c1d378d06adcc.json`](../../sessions/e6/e699bc6c1d378d06adcc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验 `eval_pi05_random_k085_long_seed42_postfix_v3` 分析完成。

**结果：π0.5 Random k=0.85 Long → SR=49.4% (247/500)**

Per-task 成功率：

| Task | SR |
|------|-----|
| T0 alphabet soup & tomato | 52% |
| T1 cream cheese & butter | 46% |
| T2 stove & moka pot | 66% |
| T3 black bowl drawer | 74% |
| T4 white mug left plate | 24% |
| T5 book back shelf | 44% |
| T6 white mug plate | 52% |
| T7 alphabet soup & cream | 52% |
| T8 both moka pots stove | 12% |
| T9 yellow white mug microwave | 72% |

**Disruption curve 更新（π0.5 Long Random）**：
- k=0.9 → ~77%
- **k=0.85 → 49.4%** ← 本次
- k=0.7 → ~58.4%
- k=0.5 → ~50.2%
- k=0.3 → ~29.0%

k=0.85 的 49.4% 低于 k=0.7 的 58.4%，这个结果异常——理论上保留更多 token 应该性能更好。可能是 seed/variance 导致，或者 k=0.85 恰好处于 cliff zone 的不稳定区间。Registry 已更新为 DONE/success。

---
