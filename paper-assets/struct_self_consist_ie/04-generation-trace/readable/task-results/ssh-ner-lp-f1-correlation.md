# ssh ner lp f1 correlation

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_ner_lp_f1_correlation_20260522T073121_result.json`
- **Structured JSON:** [`e30bfa8e829609c69acb.json`](../../sessions/e3/e30bfa8e829609c69acb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个数据集全部完成。结果汇总：

```
NER LP-F1 Spearman ρ (finetuned, N=8, seed=42)

| Dataset  | Pooled ρ | p-value  | Within-inst ρ | n_valid       | Zero-F1%  |
|----------|----------|----------|----------------|---------------|-----------|
| SciERC   |   0.3118 | 5.48e-100|         0.1878 |   437 / 551   |     4.7%  |
| CoNLL    |   0.4109 | 0.00e+00 |         0.2843 |  1120 / 3453  |     2.7%  |
| FewNERD  |   0.6739 | 0.00e+00 |         0.5411 | 28899 / 37648 |     5.4%  |
```

要点：
- 三个 NER 数据集的 LP-F1 pooled ρ 全部显著为正（0.31–0.67），FewNERD 最强
- Within-instance ρ 方向一致但弱于 pooled（0.19–0.54），符合预期——instance 内仅 8 个点，方差大
- CoNLL 的 n_valid 比例最低（1120/3453=32%），说明大量 instance 的 8 个 sample F1 完全一致（无方差），finetuned 模型在 CoNLL 上较稳定
- Zero-F1% 都较低（2.7–5.4%），finetuned 模型很少完全失败

---
