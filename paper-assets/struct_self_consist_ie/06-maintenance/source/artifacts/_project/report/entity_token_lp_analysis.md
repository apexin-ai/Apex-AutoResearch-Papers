# Entity-Token LP Analysis: SciERC NER

## Summary

Decomposed full-sequence log-probability into token subsets to test whether entity-relevant tokens carry stronger quality signal than the full sequence average. Result: **entity text+type LP is a substantially stronger signal** (within-rho 0.38 vs 0.30, AUROC 0.72 vs 0.64), confirming that full-sequence LP is diluted by low-information schema tokens. However, full-sequence LP still wins on selection F1 (0.6465 vs 0.6357) due to lower estimation variance from averaging over more tokens.

## Data Source

- `output/exp_entity_token_lp/scierc/samples.jsonl` (551 instances, N=8 samples, Qwen3-8B + LoRA 5-epoch)
- Per-token logprobs and token texts available for all samples
- 529 instances with gold entities and valid token data

## Token Classification

Each output token classified by regex on reconstructed JSON:

| Category | Median tokens | Fraction of total |
|---|---|---|
| entity_text | 10 | ~5.8% |
| entity_type | 5 | ~2.9% |
| entity_span | 13 | ~7.6% |
| schema (JSON keys, brackets, etc.) | ~48 | ~28% |
| relation section | ~65 | ~38% |
| **total** | **172** | 100% |

## Main Results

| LP Variant | Within-rho | Global-rho | AUROC | Sel.F1 | Delta vs Greedy |
|---|---|---|---|---|---|
| full (baseline) | 0.2994 | 0.2971 | 0.6417 | **0.6465** | +0.0035 |
| entity-text | 0.1933 | 0.3508 | 0.6641 | 0.6262 | -0.0168 |
| entity-type | 0.3273 | 0.3239 | 0.6577 | 0.6378 | -0.0052 |
| entity-span | 0.0000 | -0.0008 | 0.5072 | 0.5923 | -0.0507 |
| entity-all (text+type+span) | 0.1277 | 0.1396 | 0.5751 | 0.6131 | -0.0299 |
| **entity-text-type** | **0.3819** | **0.4401** | **0.7191** | 0.6357 | -0.0073 |
| nonentity | 0.2171 | 0.2536 | 0.6248 | 0.6199 | -0.0231 |
| schema-only | 0.2470 | 0.3175 | 0.6462 | 0.6141 | -0.0289 |

Baselines: Greedy F1 = 0.6430, Oracle F1 = 0.7845.

## Key Findings

1. **Entity text+type LP is the strongest quality signal**: within-rho 0.3819 (+27.5% vs full), global-rho 0.4401 (+48.1%), AUROC 0.7191 (+12.1%). This confirms the hypothesis that full-sequence LP is diluted by non-entity token noise.

2. **Entity-span LP carries zero signal**: rho ~ 0, AUROC ~ 0.50. Start/end character offsets are either trivially correct (copied from input text) or completely wrong, with no correlation to overall extraction quality.

3. **Entity-all LP is worse than its subsets**: because span tokens (13 tokens, zero signal) dilute the entity text+type signal (15 tokens, strong signal). The composition matters.

4. **Full-sequence LP still wins on selection F1**: 0.6465 vs 0.6357 for entity-text-type. With only ~15 entity tokens per sample, the LP estimate has high variance, leading to noisier argmax selection. Full-sequence LP averages over 172 tokens, reducing estimation variance.

5. **Bias-variance tradeoff**: entity-text-type LP has higher correlation (less bias) but more estimation noise (more variance). Full-sequence LP has lower correlation (more bias from schema token dilution) but lower variance. For argmax selection, variance dominates.

## Implications

- Token-level LP decomposition reveals that quality signal is concentrated in entity text and type tokens (~9% of total tokens)
- A weighted LP that upweights entity text+type tokens and downweights schema/span tokens could combine the best of both worlds
- The entity-span LP being zero-signal suggests that offset prediction uncertainty is orthogonal to extraction quality
- This supports the paper narrative that structured output quality can be better estimated by focusing on semantically meaningful tokens rather than the full sequence
