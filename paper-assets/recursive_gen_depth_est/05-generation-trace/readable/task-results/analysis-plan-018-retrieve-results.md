# analysis plan 018 retrieve results

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan_018_retrieve_results_20260522T112606_result.json`
- **Structured JSON:** [`f5ce6f69ee41915be90f.json`](../../sessions/f5/f5ce6f69ee41915be90f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已完成（耗时 ~81 分钟）。进程不再运行。以下是全 9-cell 结果。

## Binoculars + Fast-DetectGPT Ordinal Baseline（plan_018）

### 主对比表

| Cell | Method | 4cls-Acc | d0v1 AUC | d1v2 AUC | d2v3 AUC | Spearman ρ |
|------|--------|----------|----------|----------|----------|-----------|
| **pythia_nucleus** | RF-19feat | **0.787** | **0.999** | **0.895** | **0.760** | — |
| | Bino-LR | 0.376 | 0.738 | 0.529 | 0.515 | 0.448 |
| | FDGPT-LR | 0.395 | 0.797 | 0.596 | 0.530 | 0.364 |
| | Combined | 0.513 | 0.990 | 0.767 | 0.626 | — |
| **pythia_temp09** | RF-19feat | **0.768** | — | — | — | — |
| | Bino-LR | 0.386 | 0.747 | 0.509 | 0.512 | 0.460 |
| | FDGPT-LR | 0.387 | 0.783 | 0.577 | 0.509 | 0.351 |
| | Combined | 0.519 | 0.990 | 0.769 | 0.604 | — |
| **pythia_topk50** | RF-19feat | **0.689** | — | — | — | — |
| | Bino-LR | 0.330 | 0.692 | 0.501 | 0.507 | 0.318 |
| | FDGPT-LR | 0.359 | 0.737 | 0.547 | 0.511 | 0.311 |
| | Combined | 0.456 | 0.950 | 0.645 | 0.528 | — |
| **olmo_nucleus** | RF-19feat | **0.789** | — | — | — | — |
| | Bino-LR | 0.345 | 0.744 | 0.509 | 0.522 | −0.372 |
| | FDGPT-LR | 0.580 | 0.917 | 0.668 | 0.520 | 0.737 |
| | Combined | 0.588 | 0.949 | 0.742 | 0.550 | — |
| **olmo_temp09** | RF-19feat | **0.823** | — | — | — | — |
| | Bino-LR | 0.355 | 0.748 | 0.525 | 0.504 | −0.373 |
| | FDGPT-LR | 0.570 | 0.923 | 0.669 | 0.516 | 0.732 |
| | Combined | 0.578 | 0.951 | 0.752 | 0.517 | — |
| **olmo_topk50** | RF-19feat | **0.744** | — | — | — | — |
| | Bino-LR | 0.379 | 0.776 | 0.516 | 0.503 | −0.429 |
| | FDGPT-LR | 0.506 | 0.842 | 0.596 | 0.527 | 0.675 |
| | Combined | 0.508 | 0.869 | 0.641 | 0.532 | — |
| **gpt2xl_nucleus** | RF-19feat | **0.843** | — | — | — | — |
| | Bino-LR | 0.493 | 0.942 | 0.502 | 0.581 | −0.605 |
| | FDGPT-LR | 0.597 | 0.955 | 0.644 | 0.655 | 0.766 |
| | Combined | 0.613 | 0.969 | 0.724 | 0.703 | — |
| **gpt2xl_temp09** | RF-19feat | **0.859** | — | — | — | — |
| | Bino-LR | 0.508 | 0.944 | 0.594 | 0.537 | −0.631 |
| | FDGPT-LR | 0.614 | 0.957 | 0.714 | 0.602 | 0.770 |
| | Combined | 0.621 | 0.972 | 0.791 | 0.654 | — |
| **gpt2xl_topk50** | RF-19feat | **0.758** | — | — | — | — |
| | Bino-LR | 0.481 | 0.951 | 0.507 | 0.494 | −0.569 |
| | FDGPT-LR | 0.547 | 0.941 | 0.598 | 0.537 | 0.684 |
| | Combined | 0.563 | 0.958 | 0.642 | 0.568 | — |

### 9-cell 平均

| Method | Mean 4cls-Acc |
|--------|-------------|
| **RF-19feat** | **0.784** |
| Combined (Bino+FDGPT) | 0.551 |
| Fast-DetectGPT LR | 0.506 |
| Binoculars LR | 0.406 |

### 关键发现

1. **RF-19feat 大幅领先**：平均 78.4% vs Combined 55.1%，绝对差 23.3pp。单 scalar detector 即使组合也远不及多特征 RF。

2. **d0v1 区分 OK，d1v2/d2v3 接近随机**：Binoculars 在 d1v2/d2v3 AUC 基本 ~0.50-0.59（接近 chance），说明单一分数无法区分相邻 depth。Fast-DetectGPT 稍好但仍远逊 RF（d1v2 最高 0.714 vs RF 的 0.895）。

3. **Binoculars 在 OLMo/GPT2XL 上 ρ 为负**：因为 Binoculars score = observer_LL / performer_LL，对不同 model family 的 depth 方向可能反转。

4. **gpt2xl 系列 detector 效果最好**：FDGPT 在 gpt2xl_temp09 达到最高单方法 acc（61.4%），因为 observer=gpt2-xl 与 generator family 匹配。

5. **Combined 几乎不比 FDGPT 单独强多少**：平均 55.1% vs 50.6%，说明 Binoculars 提供的额外信息有限。

### 另有 binoculars_ordinal_9cell.json（Binoculars 多特征 RF）

这是用 Binoculars 衍生的 11 个统计特征（bino_score, ppl_mean/var/median/p10/p90/skew, xppl_mean/var/median, bino_score_median）训练 RF 的结果：

| Cell | RF_multi (Bino-11feat) | RF-19feat (参考) |
|------|----------------------|----------------|
| pythia_nucleus | 80.4% | 78.7% |
| gpt2xl_temp09 | 82.9% | 85.9% |
| **9-cell 平均** | **78.1%** | **78.4%** |

Binoculars 多特征 RF 与我们的 19-feature RF 几乎持平（78.1% vs 78.4%），但这需要 observer+performer 两个模型前向传播，计算成本高得多。

---
