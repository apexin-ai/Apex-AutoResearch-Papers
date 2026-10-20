# analysis exp wiki olmo v2

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_wiki_olmo_v2_20260517T131106_result.json`
- **Structured JSON:** [`a87fe61e50ddcc67b0ce.json`](../../sessions/a8/a87fe61e50ddcc67b0ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验正常完成。结果非常清晰：

## 实验结果

| Depth Pair | AUC | 判定 |
|---|---|---|
| 0 vs 1 | **0.9932** ± 0.0013 | 可区分 |
| 1 vs 2 | 0.4986 ± 0.0082 | 不可区分 (≈随机) |
| 2 vs 3 | 0.5012 ± 0.0134 | 不可区分 |
| 3 vs 4 | 0.5057 ± 0.0051 | 不可区分 |
| 4 vs 5 | 0.5009 ± 0.0113 | 不可区分 |

JSD 同样印证：0v1 的 JSD=0.1688 远高于后续 pairs（均 ≈0.003）。

## Conclusion

- **K* = 1**（第一个 AUC < 0.6 的 pair 是 1v2，K* = min depth of that pair = 1）
- **Conclusion: negative**

K* = 1 而非预期的 K* = 2。这意味着 OLMo-1B 在 Wikipedia domain 上，仅经过一次 continuation 就已经达到 saturation（depth 1 之后的文本与更高 depth 不可区分）。这与 Qwen2.5-1.5B 在 Wikipedia 上 K*=2 的结论不一致，表明 K* 可能是 model-dependent 的（OLMo-1B 的 continuation 能力较弱，一次生成就丢失了足够多的 human signal 使后续 depths 无差异）。

补充指标：
- Ordinal 6-class accuracy = 0.3227（接近随机 1/6 ≈ 0.167，但高于随机说明 depth 0 仍可分离）
- Top features: `surp_mean`, `surp_d1_skew`, `surp_d1_mean` — surprisal 类特征主导区分

---
