# code hidden state probe prep

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_hidden_state_probe_prep_20260518T181756_result.json`
- **Structured JSON:** [`3bc880e29b284636a4b2.json`](../../sessions/3b/3bc880e29b284636a4b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp-028 完成。结果摘要：

### exp_028_entity_token_lp 结果

| LP Variant | W-Range | W-Rho | G-Rho | Sel.F1 | ΔGreedy |
|---|---|---|---|---|---|
| **full** | 0.040 | 0.094 | 0.297 | **0.647** | +0.004 |
| entity_text | 0.086 | 0.000 | 0.351 | 0.626 | -0.017 |
| entity_type | 0.156 | 0.053 | 0.324 | 0.638 | -0.005 |
| **entity_text_type** | 0.135 | 0.109 | **0.440** | 0.636 | -0.007 |
| entity_all | 0.187 | 0.000 | 0.140 | 0.613 | -0.030 |
| schema_only | 0.009 | 0.000 | 0.318 | 0.614 | -0.029 |

**结论（negative）**：假设部分成立，部分不成立。

- **Cross-instance**: 格式 token 确实稀释了 LP 信号。entity_text_type LP 的 global ρ = 0.440，比 full LP 的 0.297 高 48%（32% dilution ratio）。
- **Within-instance**: selection F1 几乎无差异（0.647 vs 0.636）。原因是 schema tokens 的 within-instance range 极低（median 0.009），跨 sample 几乎不变，因此不影响 within-instance ranking。
- **关键发现**: entity_span tokens（start/end 数字）的 global ρ 被 entity_all 拉低到 0.140，说明 span offset tokens 是纯噪声。最优分解是 entity_text + entity_type。
- LP compression 是 **cross-instance format-diluted** 但 **within-instance model-intrinsic**。

---
