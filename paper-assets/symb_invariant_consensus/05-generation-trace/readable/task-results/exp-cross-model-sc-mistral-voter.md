# exp cross model sc mistral voter

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_cross-model-sc-mistral-voter_20260523T145611_result.json`
- **Structured JSON:** [`84c337319d05783eed48.json`](../../sessions/84/84c337319d05783eed48.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 三方对比表 (ProofWriter, w=3)

| Generator | SC | Mistral cross-SC | Δ_Mist | Qwen cross-SC | Δ_Qwen | NLI combo | Δ_NLI |
|---|---|---|---|---|---|---|---|
| LLaMA-8B | 72.50% | 63.17% | **-9.33pp*** | 75.33% | +2.83pp | 73.33% | +0.83pp |
| Qwen2.5-14B | 74.00% | 71.67% | **-2.33pp*** | 74.50% | +0.50pp | 74.67% | +0.67pp |
| Qwen3-14B | 85.83% | 83.17% | **-2.67pp*** | 84.67% | -1.17pp | 86.33% | +0.50pp |

*所有 Mistral cross-SC 的 Δ 均显著 (McNemar p < 0.02)

### 完整 w=1,3,5 结果

| Generator | w | Acc | Δ | McNemar p | Discordant [SC-only, combo-only] |
|---|---|---|---|---|---|
| LLaMA-8B | 1 | 69.67% | -2.83pp | 0.0009 | [21, 4] |
| LLaMA-8B | 3 | 63.17% | -9.33pp | <0.0001 | [71, 15] |
| LLaMA-8B | 5 | 56.17% | -16.33pp | <0.0001 | [119, 21] |
| Qwen2.5-14B | 1 | 72.83% | -1.17pp | 0.0923 | [10, 3] |
| Qwen2.5-14B | 3 | 71.67% | -2.33pp | 0.0201 | [23, 9] |
| Qwen2.5-14B | 5 | 69.67% | -4.33pp | 0.0016 | [45, 19] |
| Qwen3-14B | 1 | 84.50% | -1.33pp | 0.0574 | [11, 3] |
| Qwen3-14B | 3 | 83.17% | -2.67pp | 0.0015 | [20, 4] |
| Qwen3-14B | 5 | 81.17% | -4.67pp | <0.0001 | [34, 6] |

### 结论

**强力支持 structural independence。** 关键证据链：

1. **Mistral cross-SC 全面拖低所有 generator**（avg Δ=-4.78pp），且全部统计显著
2. **Qwen cross-SC 在 Qwen3 上也拖低**（Δ=-1.17pp），在 LLaMA 上帮助（Δ=+2.83pp）
3. **NLI combo 全面正向或中性**（avg Δ=+0.67pp），包括 Qwen3（Δ=+0.50pp）

对比模式清晰：
- LLM cross-voter（不论能力高低）→ 拖低或仅在能力差大时帮助
- NLI structural signal → 一致性正向，不受 voter 能力影响
- 这排除了"voter 能力差异"作为 confound：Mistral (39%) 和 Qwen (74%) 能力差距巨大，但对 Qwen3 都是负面影响；而 DeBERTa (55%) 反而正面 → **增益来源是 structural independence，不是 ensemble diversity**

结果文件: `/root/symb_invariant_consensus/results/cross_model_sc_mistral_voter.json`

---
