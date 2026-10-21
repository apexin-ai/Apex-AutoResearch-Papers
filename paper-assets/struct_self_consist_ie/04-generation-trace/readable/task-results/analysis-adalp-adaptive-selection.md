# analysis adalp adaptive selection

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_adalp_adaptive_selection_20260517T141535_result.json`
- **Structured JSON:** [`3c6cdf545be8d0bb1a6c.json`](../../sessions/3c/3c6cdf545be8d0bb1a6c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果总结：

## 主结果表

| Dataset | Greedy F1 | LP F1 | AdaLP F1 | Oracle F1 | AdaLP vs Greedy | AdaLP vs LP |
|---------|-----------|-------|----------|-----------|-----------------|-------------|
| SciERC  | 0.6105    | 0.6080| 0.6090   | 0.7712    | -0.15pp (p=0.42)| +0.10pp     |
| CoNLL   | 0.9087    | 0.8981| 0.9054   | 0.9531    | -0.32pp (p=0.003)| +0.74pp    |
| Few-NERD| 0.7712    | 0.7799| 0.7734   | 0.8829    | +0.22pp (p=0.047)| -0.65pp    |

## LODO CV

| Fold | Train sets | Test set | Best τ | AdaLP F1 (test) |
|------|-----------|----------|--------|-----------------|
| 1 | CoNLL, FewNERD | SciERC | 0.625 | 0.6090 |
| 2 | SciERC, FewNERD | CoNLL | 0.500 | 0.9054 |
| 3 | SciERC, CoNLL | FewNERD | 0.500 | 0.7734 |

Mean CV F1: 0.7626

## 关键发现

AdaLP 效果不理想：
- 在 CoNLL 上显著差于 greedy（-0.32pp, p=0.003）
- 在 FewNERD 上显著差于 LP（-0.65pp, p<0.001）
- SciERC 上无显著差异

根本原因从 bin 分析可见：N=8 的 NER 任务中，绝大多数 instance 的 degeneracy 极高（CoNLL 78% 的 instance degen > 0.75），导致 AdaLP 几乎总是选 greedy，失去了自适应的意义。在低 degeneracy bin 中，LP selection 反而经常比 greedy 差（CoNLL 的 (0,0.25] bin 中 LP 比 greedy 低 11.4pp），说明低 degeneracy 不一定意味着 LP 更可靠。

产出文件：
- `scripts/adalp_analysis.py`
- `output/adalp_analysis_results.json`

---
