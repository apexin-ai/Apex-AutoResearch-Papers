# W3: 1.7B Per-Class Confusion Matrix

**Source**: westb-13313:/root/autodl-tmp/simgate-modular-routing/artifacts/w3_confusion_matrix.md
**Model**: plan-008-v4-seed42, greedy decoding, 300 steps, 10 episodes

## Overall
- Accuracy: 0.64, Balanced Accuracy: 0.58
- Class imbalance: 270 deterministic vs 30 internal

## Death vs Non-Death Split

| Metric | Death Episodes (180 steps) | Non-Death (120 steps) |
|--------|--------------------------|----------------------|
| Accuracy | 0.667 | 0.600 |
| Det Recall | 0.667 | 0.633 |
| Int Recall | n/a (0 true internal) | 0.500 |
| Det Precision | 1.000 | 0.792 |
| Int Precision | 0.000 | 0.310 |

## Key Findings

1. **33% of death-episode steps mispredicted as "internal"** (60/180). These FPs would route to LLM agent in death-prone situations.

2. **No death-specific detection**: Router prediction rate similar across death (66.7% det) and non-death (60.0% det) episodes. Router doesn't detect death risk, just pattern-matches step context.

3. **Internal class weak everywhere**: Overall precision = 0.14. Router over-predicts "internal", producing many FPs from deterministic class.

4. **High task variance**: Accuracy 0.43 (identify-life-stages-2) to 0.83 (grow-fruit).

## Paper Implication
The router cannot distinguish death-prone from safe episodes. This supports the core claim: death dominance is a structural property of the routing signal, not something a better router could overcome.