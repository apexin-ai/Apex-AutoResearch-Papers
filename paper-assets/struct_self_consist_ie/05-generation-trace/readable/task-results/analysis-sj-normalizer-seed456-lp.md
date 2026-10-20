# analysis sj normalizer seed456 lp

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_sj_normalizer_seed456_lp_20260515T153520_result.json`
- **Structured JSON:** [`06bb66fbf3a9f142e111.json`](../../sessions/06/06bb66fbf3a9f142e111.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务都完成了。

### Task 2: SJ Normalizer Ablation

| Metric | SJ_max | SJ_union |
|--------|--------|----------|
| ρ (Spearman) | 0.3599 | **0.3650** |
| AUROC | **0.7180** | 0.7154 |
| Mean SJ | 0.7026 | 0.6918 |
| Std SJ | 0.1956 | 0.1977 |

Union normalizer ρ 略高 (+0.005)，AUROC 略低 (-0.003)。差异极小，两种 normalizer 本质等价。

### Task 3: Seed 456 LP Range

| Metric | seed42 (N=8, joint) | seed456 (N=8, joint) |
|--------|---------------------|----------------------|
| Median LP range | 0.0401 | 0.0396 |
| IQR [25, 75] | [0.0265, 0.0685] | [0.0236, 0.0733] |
| Tied fraction (ε=0.05) | 60.3% | 62.2% |

两个 seed 的 LP range 分布几乎一致。~60% 实例的 LP range < 0.05（即 tied），说明 mean_logprob 在大多数实例上区分力很弱，且不受 seed 影响。

注：exp_018_qwen_scierc_seed456 实际为 N=8（非 N=16），subtask=joint，与 seed42 数据可比。

输出已保存至 `output/analysis_round8/sj_normalizer_ablation.json` 和 `output/analysis_round8/seed456_lp_range.json`。

---
