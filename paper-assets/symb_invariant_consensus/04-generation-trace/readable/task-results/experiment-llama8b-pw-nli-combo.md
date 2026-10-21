# experiment llama8b pw nli combo

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_llama8b-pw-nli-combo_20260520T223535_result.json`
- **Structured JSON:** [`90b1bbf5af1424c054bf.json`](../../sessions/90/90b1bbf5af1424c054bf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果：

```
SC baseline:            70.00%
DeBERTa-large standalone: 55.00%
Capability gap:         -15.00 pp
Combo w=1:              72.83% (+2.83pp, p=0.0001)
Combo w=3:              74.17% (+4.17pp, p=0.0035)
Combo w=5:              71.67% (+1.67pp, p=0.4335)
```

结果已保存至 `/root/symb_invariant_consensus/results/exp092_llama8b_pw_nli_combo/results.json`。

关键发现：
- DeBERTa standalone 确认为 55.00%，与其他 PW combo 实验一致
- **w=1 和 w=3 均显著提升**（p<0.01），w=3 最优 (+4.17pp)
- w=5 时 NLI 权重过大反而稀释了 SC 优势，增益不显著
- 互补性：NLI 能纠正 120 道 SC 错题，但 SC 在 210 道题上优于 NLI，符合 -15pp capability gap 的预期

---
