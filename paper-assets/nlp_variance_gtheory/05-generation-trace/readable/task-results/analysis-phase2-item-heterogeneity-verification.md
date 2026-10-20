# analysis phase2 item heterogeneity verification

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_phase2_item_heterogeneity_verification_20260521T224243_result.json`
- **Structured JSON:** [`74d47d0a1c396458bdda.json`](../../sessions/74/74d47d0a1c396458bdda.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## D014 验证结果

| Benchmark | std(p) | item_id% | mean_m×i_var | n_models |
|-----------|--------|----------|-------------|----------|
| MMLU | 0.3120 | 40.48 | 0.0770 | 8 |
| ARC | 0.2744 | 42.46 | 0.0677 | 8 |
| HellaSwag | 0.2829 | 32.20 | 0.0900 | 6 |
| GSM8K | 0.2209 | 16.86 | 0.0672 | 8 |
| MATH | 0.2543 | 26.48 | 0.0511 | 7 |

**Spearman 相关:**
- std(p) vs item_id%: **ρ = 0.70, p = 0.188** → 未达到 0.8 阈值
- mean_model×item_var vs item_id%: **ρ = 0.50, p = 0.391**

**结论: 假说 NOT FULLY SUPPORTED。**

item difficulty heterogeneity 与 item_id% 之间存在中等正相关 (ρ=0.70)，但未达到强相关阈值。主要偏离来自 **HellaSwag**：它的 std(p)=0.283 偏高（接近 MMLU），但 item_id% 只有 32.2%，低于 MMLU/ARC。这说明 item difficulty heterogeneity 是 item_id variance component 的一个驱动因素，但不是唯一的——model×item 交互模式、item 类型（MC vs FF）等其他机制也在起作用。

产出文件在 westd-32570: `results/exp004_8model_analysis/item_heterogeneity_verification.json` 和 `item_heterogeneity_scatter.png`。

---
