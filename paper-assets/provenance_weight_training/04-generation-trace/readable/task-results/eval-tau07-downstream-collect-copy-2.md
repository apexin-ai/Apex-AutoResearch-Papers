# eval tau07 downstream collect

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_tau07_downstream_collect_20260520T023911_result.json`
- **Structured JSON:** [`7d7a7a67810b6e29628a.json`](../../sessions/7d/7d7a7a67810b6e29628a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个 eval 全部完成，结果已收集。汇总如下：

```
τ=0.7 Downstream Results (3-seed):

| Benchmark          | τ=0.7 s42 | τ=0.7 s123 | τ=0.7 s456 | τ=0.7 Mean | τ=0.8 Mean | Uniform Mean | Δ(0.7−0.8) |
|--------------------|-----------|------------|------------|------------|------------|--------------|------------|
| ARC-E (acc_norm)   |    0.6166 |     0.6309 |     0.6111 |     0.6195 |     0.6185 |       0.6174 |    +0.0010 |
| ARC-C (acc_norm)   |    0.3473 |     0.3481 |     0.3515 |     0.3490 |     0.3515 |       0.3476 |    −0.0025 |
| HellaSwag (acc_norm)|   0.4795 |     0.4775 |     0.4811 |     0.4794 |     0.4799 |       0.4820 |    −0.0005 |
| PIQA (acc_norm)    |    0.6861 |     0.6866 |     0.6834 |     0.6854 |     0.6831 |       0.6841 |    +0.0023 |
| WinoGrande (acc)   |    0.5817 |     0.5675 |     0.5722 |     0.5738 |     0.5740 |       0.5762 |    −0.0002 |
| **Avg**            |    0.5422 |     0.5421 |     0.5399 |  **0.5414**|  **0.5414**|    **0.5414**| **+0.0000**|
```

关键发现：τ=0.7、τ=0.8、Uniform 三者的 downstream 平均分完全一致（0.5414），各 benchmark 差异均在 ±0.003 以内，无统计显著差异。Provenance weighting 的 τ 选择对 downstream task 性能无实质影响。

---
