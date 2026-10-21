# analysis exp arXiv llama8b crossscorer

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_arXiv_llama8b_crossscorer_20260518T030302_result.json`
- **Structured JSON:** [`e0c37351b29c3335bad8.json`](../../sessions/e0/e0c37351b29c3335bad8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

## exp_arXiv_llama8b_crossscorer 结果

**Conclusion: SUCCESS** — K\*=3，与原实验完全一致。

| Depth Pair | Qwen-1.5B | Pythia-1.4B | Delta |
|---|---|---|---|
| 0v1 | 0.9754 | 0.9629 | -0.013 |
| 1v2 | 0.8447 | 0.8433 | -0.001 |
| 2v3 | 0.6215 | 0.6201 | -0.001 |
| 3v4 | 0.5362 | 0.5230 | -0.013 |
| 4v5 | 0.5331 | 0.5245 | -0.009 |

两个 scorer 的 AUC 差异均 < 1.5%，K\* boundary 落在完全相同的位置（depth 2v3 仍 >0.60，depth 3v4 降至 chance）。Scorer family bias 在 arXiv domain 被排除，arXiv K\*=3 是 robust 的。

---
