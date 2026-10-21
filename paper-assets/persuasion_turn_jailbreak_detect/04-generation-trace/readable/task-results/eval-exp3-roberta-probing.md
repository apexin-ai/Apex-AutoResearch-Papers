# eval exp3 roberta probing

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_exp3-roberta-probing_20260518T105923_result.json`
- **Structured JSON:** [`9c8258e55c0c377c6799.json`](../../sessions/9c/9c8258e55c0c377c6799.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### Part A: RoBERTa Linear Probing

| Task | Vanilla | MLM | 9-class |
|---|---|---|---|
| Turn Position | 0.7665 ± 0.1081 | 0.7526 ± 0.1078 | **0.8294** ± 0.1034 |
| Escalation Level | 0.7272 ± 0.0336 | 0.7243 ± 0.0268 | **0.7448** ± 0.0284 |
| Persuasion Presence | 0.9420 ± 0.0891 | 0.9411 ± 0.0893 | **0.9509** ± 0.0905 |

与 DeBERTa 一致的趋势：9-class > vanilla ≈ MLM。MLM 续训对 RoBERTa 的线性可分性几乎无影响。

### Part A: RoBERTa CKA

| Pair | IID | DD OOD |
|---|---|---|
| vanilla vs MLM | 0.9991 | 0.9985 |
| vanilla vs 9class | 0.5564 | 0.9599 |
| mlm vs 9class | 0.5529 | 0.9598 |

RoBERTa vanilla vs MLM CKA ≈ 0.999（接近但未到1.0），9-class 在 IID 上偏离更大（0.556），DD OOD 上偏离小（0.96）。

### Part B: DeBERTa CKA=1.0 审计

**结论：CKA=1.0（4位小数四舍五入）是正确的。**

- 权重**不完全相同**：198 个 param tensor 的 L2 diff 之和 = 28.59，最大元素差 = 0.00347
- 最大差异集中在 layer 8-11 的 `intermediate.dense.weight` 和 `word_embeddings`
- CLS embedding 层面：mean cosine_sim = 0.997，mean L2_diff = 1.41
- CKA 重新计算 = **0.9999869**，四舍五入到 4 位 = 1.0000
- 原因：MLM 目标从不 mask CLS token，CLS representation 仅通过间接梯度流改变，变化极小

两份结果已保存到服务器 `results/exp3_roberta_probing.json` 和本地 artifact。

---
