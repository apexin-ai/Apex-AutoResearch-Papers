# analysis arxiv multi source bootstrap

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_arxiv_multi_source_bootstrap_20260524T101433_result.json`
- **Structured JSON:** [`b1c4872b9e7355bf036b.json`](../../sessions/b1/b1c4872b9e7355bf036b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Bootstrap CI Results

| Config | Pair | AUC | CI_lower | CI_upper | p-value | bonf_p |
|--------|------|-----|----------|----------|---------|--------|
| **Qwen2.5-1.5B** | 0v1 | 0.9938 | 0.9917 | 0.9957 | 0.0001 | 0.0005 |
| | 1v2 | 0.8578 | 0.8479 | 0.8677 | 0.0001 | 0.0005 |
| | **2v3** | **0.6437** | **0.6290** | **0.6587** | **0.0001** | **0.0005** |
| | 3v4 | 0.5501 | 0.5338 | 0.5660 | 0.0001 | 0.0005 |
| | 4v5 | 0.5302 | 0.5139 | 0.5463 | 0.0007 | 0.0035 |
| **Pythia-1.4B** | 0v1 | 0.9873 | 0.9847 | 0.9897 | 0.0001 | 0.0005 |
| | 1v2 | 0.8024 | 0.7907 | 0.8139 | 0.0001 | 0.0005 |
| | **2v3** | **0.6484** | **0.6338** | **0.6626** | **0.0001** | **0.0005** |
| | 3v4 | 0.5522 | 0.5366 | 0.5679 | 0.0001 | 0.0005 |
| | 4v5 | 0.5404 | 0.5242 | 0.5568 | 0.0001 | 0.0005 |
| **Pooled (Q+P)** | 0v1 | 0.9972 | 0.9965 | 0.9979 | 0.0001 | 0.0005 |
| | 1v2 | 0.8387 | 0.8312 | 0.8462 | 0.0001 | 0.0005 |
| | **2v3** | **0.6565** | **0.6466** | **0.6666** | **0.0001** | **0.0005** |
| | 3v4 | 0.5477 | 0.5367 | 0.5585 | 0.0001 | 0.0005 |
| | 4v5 | 0.5476 | 0.5366 | 0.5586 | 0.0001 | 0.0005 |

## K\*=3 验证

| Config | 2v3 AUC | CI_lower | > θ=0.60? | Status |
|--------|---------|----------|-----------|--------|
| Qwen2.5-1.5B | 0.6437 | 0.6290 | **YES** | **CONFIRMED** |
| Pythia-1.4B | 0.6484 | 0.6338 | **YES** | **CONFIRMED** |
| Pooled | 0.6565 | 0.6466 | **YES** | **CONFIRMED** |

**K\*=3 统计显著性全面确认：**
- 所有 3 个配置的 2v3 CI lower bound 均 > 0.60（最低 0.6290，超出阈值 0.029）
- 所有 pair 的 permutation test p < 0.001（Bonferroni 校正后仍 < 0.005）
- 方法：10K doc-level bootstrap + 10K label permutation + Bonferroni correction (α/5)

结果保存于 `results/arxiv_multi_source_bootstrap/bootstrap_ci.json`。

---
