# analysis confidence selective prediction

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_confidence_selective_prediction_20260519T011958_result.json`
- **Structured JSON:** [`d238a9534748897f631c.json`](../../sessions/d2/d238a9534748897f631c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。所有 sanity check 通过：F1@100% = greedy F1，oracle 单调递减，random 近似平坦。

## 结果摘要

**VC (Voting Confidence) 在所有 4 个数据集上一致最强。**

| Dataset | Best Signal | AUPRC | F1@80% | F1@100% | Δ@80% |
|---------|------------|-------|--------|---------|-------|
| SciERC NER | VC | 0.7013 | 0.6944 | 0.6439 | +5.0pp |
| SciERC RE | VC | 0.4921 | 0.4605 | 0.4042 | +5.6pp |
| CoNLL NER | VC | 0.9202 | 0.9627 | 0.9070 | +5.6pp |
| FewNERD NER | VC | 0.8251 | 0.8320 | 0.7478 | **+8.4pp** |

信号排序（按 AUPRC 平均）: VC > LP > SJ > FK > EM

FewNERD 上效果最显著：过滤掉最不确定的 20% 实例后 F1 从 74.8% 提升至 83.2%。

## 产出文件

| 文件 | 路径 |
|------|------|
| 分析脚本 | `/root/autodl-tmp/struct_self_consist_ie/code/selective_prediction.py` |
| 结果 JSON | `output/prescriptive_analysis/selective_prediction.json` |
| Figure (PDF+PNG) | `output/prescriptive_analysis/fig_selective_prediction.pdf` |
| LaTeX 表格 | `output/prescriptive_analysis/selective_prediction_table.tex` |

---
