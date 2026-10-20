# w5_llama_lora_scierc_constrained_eval Results

## Checker Version
fixed_20260514_v2 (strip + alias + unique_et)

## Violation Rates
| Metric | Value |
|--------|-------|
| Entity Type (ET) | 0/1757 (0.00%) |
| Relation Vocab (RV) | 0/1081 (0.00%) |
| Domain/Range (DR) | 1/1081 (0.09%) |
| Cross-field Consistency (CF) | 8/1757 (0.46%) |
| JSON parse rate | 100.0% |

## F1 Metrics
| Metric | Precision | Recall | F1 |
|--------|-----------|--------|------|
| Entity | 0.6647 | 0.6910 | 0.6776 |
| Relation | 0.4324 | 0.4795 | 0.4547 |

## Basic Stats
- Total samples: 551
- Total entities predicted: 1757 (gold: 1673)
- Total relations predicted: 1081 (gold: 974)

## Delta vs Unconstrained (Llama FT)
| Metric | Unconstrained | Constrained | Delta |
|--------|--------------|-------------|-------|
| DR | 1.11% | 0.09% | -0.92pp (-91.9%) |
| CF | 0.00% | 0.46% | +0.46pp |
| E-F1 | 67.76% | 67.76% | 0.00pp |
| R-F1 | 45.45% | 45.47% | +0.02pp |

## Llama SciERC 2×2 Matrix
| | Unconstrained | Constrained | ΔDR | ΔR-F1 |
|--|--|--|--|--|
| Zero-shot | DR=13.34%, R-F1=2.68% | DR=0.08%, R-F1=2.54% | -99.4% | -0.14pp |
| Fine-tuned LoRA | DR=1.11%, R-F1=45.47% | DR=0.09%, R-F1=45.47% | -91.9% | +0.02pp |

## Conclusion: SUCCESS
- DR from 1.11% → 0.09% (92% reduction), only 1 residual DR violation
- R-F1 essentially unchanged (45.45% → 45.47%, +0.02pp)
- E-F1 identical (67.76%)
- Composability confirmed: constrained decoding on fine-tuned Llama works without F1 loss
