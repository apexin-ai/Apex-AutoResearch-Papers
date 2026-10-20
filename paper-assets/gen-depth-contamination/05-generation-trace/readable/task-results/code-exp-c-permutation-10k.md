# code exp C permutation 10k

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_C_permutation_10k_20260515T102312_result.json`
- **Structured JSON:** [`197a2da80f4902c29340.json`](../../sessions/19/197a2da80f4902c29340.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

10,000 permutation resamples 完成（~13 分钟）。结果已保存到 `artifacts/exp_C_permutation_10k.json`。

**汇总表：**

| Config | Pair | AUC | 95% CI | p-value |
|--------|------|-----|--------|---------|
| **qwen_rw** | 0v1 | 0.9956 | [0.9946, 0.9965] | 0.0001 |
| | 1v2 | 0.6955 | [0.6860, 0.7044] | 0.0001 |
| | 2v3 | 0.5893 | [0.5801, 0.5986] | 0.0001 |
| | 3v4 | 0.5435 | [0.5333, 0.5545] | 0.0001 |
| | 4v5 | 0.5340 | [0.5236, 0.5459] | 0.0001 |
| **pythia** | 0v1 | 0.9932 | [0.9921, 0.9943] | 0.0001 |
| | 1v2 | 0.6539 | [0.6445, 0.6638] | 0.0001 |
| | 2v3 | 0.5514 | [0.5410, 0.5624] | 0.0001 |
| | 3v4 | 0.5152 | [0.5044, 0.5255] | 0.0033 |
| | 4v5 | 0.5136 | [0.5027, 0.5248] | 0.0097 |
| **olmo** | 0v1 | 0.9970 | [0.9964, 0.9975] | 0.0001 |
| | 1v2 | 0.6145 | [0.6050, 0.6245] | 0.0001 |
| | 2v3 | 0.5496 | [0.5399, 0.5593] | 0.0001 |
| | 3v4 | 0.5091 | [0.4980, 0.5198] | **0.0627** |
| | 4v5 | 0.5045 | [0.4937, 0.5151] | **0.2258** |
| **qwen_cont** | 0v1 | 0.9971 | [0.9963, 0.9978] | 0.0001 |
| | 1v2 | 0.6112 | [0.6003, 0.6212] | 0.0001 |
| | 2v3 | 0.5609 | [0.5512, 0.5718] | 0.0001 |
| | 3v4 | 0.5409 | [0.5307, 0.5516] | 0.0001 |
| | 4v5 | 0.5141 | [0.5035, 0.5249] | 0.0067 |

**关键发现：**
- 之前 500 次 permutation 时 p=0.002（floor），现在 10k 次大部分变为 p=0.0001（= 1/10001，conservative estimator）
- OLMo 3v4 和 4v5 是仅有的不显著 pairs（p=0.063, p=0.226），CI 跨越 0.5——符合 depth signal 在深层消失的预期
- Pythia 4v5 边缘显著（p=0.0097），但 AUC 仅 0.5136

---
