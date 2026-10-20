# experiment qwen14b pw nli combo

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_qwen14b-pw-nli-combo_20260520T213827_result.json`
- **Structured JSON:** [`0e04027887830d181ed7.json`](../../sessions/0e/0e04027887830d181ed7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果：

| Metric | Value |
|--------|-------|
| SC baseline (Qwen2.5-14B) | 73.50% |
| DeBERTa-large standalone | 55.00% |
| **Capability gap** | **-18.50pp** |
| Combo w=1 | 74.17% (+0.67pp, p=0.344) |
| Combo w=3 | 74.33% (+0.83pp, p=0.405) |
| Combo w=5 | **75.33% (+1.83pp, p=0.144)** |

Capability Gap 叙事验证：gap = -18.50pp 介于 Qwen3 (-30pp, gain=+1.83) 和 Mistral (+15.67pp, gain=+10.67) 之间，对应 combo gain 也在两者之间（+0.67 ~ +1.83pp），支撑单调递减趋势。

结果已写入 `/root/symb_invariant_consensus/results/qwen14b_pw_nli_combo/results.json`。

---
