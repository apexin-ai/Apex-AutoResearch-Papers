# code 5090b multiseed inference

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_5090b_multiseed_inference_20260518T184514_result.json`
- **Structured JSON:** [`2f7035fe11d9f2347dda.json`](../../sessions/2f/2f7035fe11d9f2347dda.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

FewNERD seed123: 19664/301184 = 6.5%，处理速度约 ~40 it/s。剩余 ~281520 prompts / 40 = ~7038 秒 ≈ **约 2 小时**。

**当前完成汇总：**

| 数据集 | seed | greedy F1 | oracle F1 | headroom | degeneracy | 最佳 ρ | DGS delta |
|--------|------|-----------|-----------|----------|------------|--------|-----------|
| SciERC | 456 | 0.6453 | 0.7726 | +12.72pp | 19.3% | VC=0.41 | -0.30pp |
| CoNLL | 123 | 0.9074 | 0.9477 | +4.03pp | 63.0% | EM=0.47 | -0.60pp |
| CoNLL | 456 | 0.9076 | 0.9443 | +3.67pp | 63.0% | VC=0.48 | -0.71pp |
| FewNERD | 123 | -- | -- | -- | -- | -- | -- |

GPU3 FewNERD seed123 预计还需约 2 小时完成。

---
