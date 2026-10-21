# analysis mcnemar method experiments

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mcnemar-method-experiments_20260520T001141_result.json`
- **Structured JSON:** [`3df3a62059964ff79ee4.json`](../../sessions/3d/3df3a62059964ff79ee4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## McNemar's Test 结果

```
=== McNemar's Paired Test: Method vs SC ===

exp-076  Debate × FOLIO-204     (n=204, Δ=-18.63pp):
  a=56  b=60  c=22  d=66
  χ²=17.61, p=2.71e-05  [*** p<0.001]

exp-078  Debate × LogiQA-200    (n=200, Δ=-23.0pp):
  a=36  b=64  c=18  d=82
  χ²=25.80, p=3.79e-07  [*** p<0.001]

exp-075b Contrastive × FOLIO-204 (n=204, Δ=-9.31pp):
  a=82  b=34  c=15  d=73
  χ²=7.37,  p=0.0066    [**  p<0.01]

exp-080  Contrastive × LogiQA-200 (n=200, Δ=-4.50pp):
  a=75  b=25  c=16  d=84
  χ²=1.98,  p=0.160     [n.s.]

exp-074  ICG × FOLIO-204        (n=204, Δ=-1.96pp):
  a=103 b=7   c=3   d=91
  χ²=1.60,  p=0.206     [n.s.]
```

**关键发现**：

| 方法 | 显著性 | 解读 |
|------|--------|------|
| Debate | **两个数据集都极显著 (p<0.001)** | 硬证据：Debate 显著伤害准确率 |
| Contrastive | FOLIO 显著 (p<0.01)，LogiQA 不显著 (p=0.16) | 在 FOLIO 上有显著退化，LogiQA 上差异不够大 |
| ICG | 不显著 (p=0.21) | Δ=-1.96pp 太小，discordant pairs 仅 10 个 (b=7,c=3)，检验力不足 |

Debate 的 discordant pair 严重不对称（exp-076: b=60 vs c=22; exp-078: b=64 vs c=18），说明 Debate 大量翻转了 SC 原本答对的题目，同时很少纠正 SC 答错的题。

结果已保存到 `artifacts/mcnemar_method_experiments.json` 并注册 (`art_20260520_087dc0`)。

---
