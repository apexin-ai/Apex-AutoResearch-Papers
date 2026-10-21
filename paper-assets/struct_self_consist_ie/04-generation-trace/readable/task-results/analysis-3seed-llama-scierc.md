# analysis 3seed llama scierc

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_3seed_llama_scierc_20260515T060020_result.json`
- **Structured JSON:** [`0a9df0e7f6ba0e346529.json`](../../sessions/0a/0a9df0e7f6ba0e346529.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Sanity check 完全匹配 report.json（SJ ρ=0.3630, FK ρ=0.3266, LP ρ=0.1827, LP AUROC=0.5964）。

结果：

### NER — LLaMA/SciERC 3-seed (42, 123, 456)

| Signal | Spearman ρ | AUROC |
|---|---|---|
| Voting Confidence | 0.4023 ± 0.0122 | 0.6940 ± 0.0067 |
| Soft Jaccard | 0.3615 ± 0.0047 | 0.6715 ± 0.0024 |
| Exact Match | 0.3117 ± 0.0122 | 0.6477 ± 0.0047 |
| Fleiss' Kappa | 0.3093 ± 0.0151 | 0.6391 ± 0.0065 |
| Log-probability | 0.1903 ± 0.0059 | 0.5931 ± 0.0066 |

### RE — LLaMA/SciERC 3-seed (42, 123, 456)

| Signal | Spearman ρ | AUROC |
|---|---|---|
| Voting Confidence | 0.3301 ± 0.0122 | 0.6804 ± 0.0071 |
| Log-probability | 0.3061 ± 0.0148 | 0.6552 ± 0.0100 |
| Fleiss' Kappa | 0.2872 ± 0.0225 | 0.6492 ± 0.0141 |
| Soft Jaccard | 0.2772 ± 0.0224 | 0.6565 ± 0.0137 |
| Exact Match | 0.1860 ± 0.0186 | 0.6108 ± 0.0107 |

JSON 已保存到 `output/review_round2/llama_scierc_3seed_summary.json`。各 seed 间标准差很小（σ ≤ 0.02），信号排序稳定——NER 端 Voting Confidence 最强（ρ=0.40），RE 端同样 Voting Confidence 领先（ρ=0.33）。

---
