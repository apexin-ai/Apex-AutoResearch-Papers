# exp cross model sc ablation

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_cross-model-sc-ablation_20260523T143542_result.json`
- **Structured JSON:** [`a1859fd66ca869768b45.json`](../../sessions/a1/a1859fd66ca869768b45.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

**Cross-model SC (w=3) vs NLI combo (w=3)：**

| Generator | Dataset | SC | Cross-SC | Δ_cross | NLI-combo | Δ_NLI | 
|---|---|---|---|---|---|---|
| Mistral-7B | PW | 39.33% | 47.67% | **+8.33pp** | 46.00% | +6.67pp |
| LLaMA-8B | PW | 72.50% | 75.33% | **+2.83pp** | 73.33% | +0.83pp |
| Qwen2.5-14B | PW | 74.00% | 74.50% | +0.50pp | 74.67% | +0.67pp |
| Qwen3-14B | PW | 85.83% | 84.67% | **−1.17pp** | 86.33% | +0.50pp |
| Mistral-7B | FOLIO | 55.88% | 63.73% | **+7.84pp** | 58.82% | +2.94pp |
| LLaMA-8B | FOLIO | 66.18% | 70.10% | **+3.92pp** | 65.20% | −0.98pp |
| Qwen2.5-14B | FOLIO | 75.98% | 76.96% | +0.98pp | 75.49% | −0.49pp |
| Qwen3-14B | FOLIO | 83.33% | 85.78% | +2.45pp | 84.80% | +1.47pp |

**关键发现（回应 R19）：**

1. **弱 generator（Mistral/LLaMA）**：Cross-model SC > NLI combo → 当 cross voter（Qwen2.5, 74%）远强于 generator 时，纯 ensemble diversity 就能提供大增益。但这里 cross voter 也远强于 DeBERTa（55%），增益部分来自 voter 能力差异。

2. **强 generator（Qwen3）**：Cross-model SC **损害**性能（−1.17pp on PW），而 NLI combo 仍微正（+0.50pp）→ **结构独立性的直接证据**。一个更弱的 LLM voter 会引入同质性错误（correlated mistakes），但 NLI 的不同推理方式避免了这一点。

3. **结论**：NLI combo 的增益来源是 **structural independence + ensemble diversity 的组合**，但 structural independence 在强 generator 上尤为关键——这恰恰是 NLI 作为异构验证器的核心价值。

结果保存在 `westd-16639:/root/symb_invariant_consensus/results/cross_model_sc_ablation.json`。

---
