# code olmo c4 cross scorer

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_olmo_c4_cross_scorer_20260524T103724_result.json`
- **Structured JSON:** [`a7b8cfeaf0f5f604d82b.json`](../../sessions/a7/a7b8cfeaf0f5f604d82b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成，278.7s。结果汇总：

## OLMo-1B C4 Cross-Scorer 结果

**K\* (cross-scorer) = 1**，与自评分一致。

| Pair | AUC | 95% CI | p_perm | Sig | CI>θ |
|------|-----|--------|--------|-----|------|
| 0v1 | 0.9860 | [0.9842, 0.9877] | 0.0001 | SIG | PASS |
| 1v2 | 0.4999 | [0.4885, 0.5112] | 0.5056 | n.s. | FAIL |
| 2v3 | 0.4982 | [0.4869, 0.5096] | 0.6286 | n.s. | FAIL |
| 3v4 | 0.5016 | [0.4903, 0.5130] | 0.3955 | n.s. | FAIL |
| 4v5 | 0.4946 | [0.4830, 0.5060] | 0.8183 | n.s. | FAIL |

**与旧实验对比：**
- Self-scoring K\*=1 (0v1=0.9871, 1v2=0.4984)
- Cross-scoring 旧 pipeline K\*=1 (0v1=0.9861, 1v2=0.5001)
- Cross-scoring 新 pipeline K\*=1 (0v1=0.9860, 1v2=0.4999)

三套结果高度一致。OLMo-1B 在 C4 上仅 depth 0→1 可区分（生成 vs 原始），depth 1+ 全部退化到随机水平。Cross-scorer 确认了 OLMo 作为"弱模型例外"的结论。

结果已保存至 `results/olmo_c4_cross_scorer/results.json`。

---
