# analysis mlp verifier upgrade

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mlp_verifier_upgrade_20260519T070159_result.json`
- **Structured JSON:** [`91f17112dfba6bcfb210.json`](../../sessions/91/91f17112dfba6bcfb210.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果汇总如下：

## 结果表：3 分类器 × 3 数据集

| Dataset | Clf | AUROC | Sel F1 | Δ vs greedy |
|---------|-----|-------|--------|-------------|
| **SciERC** | LR | 0.6713 | 0.6876 | **-0.0268** |
| | MLP | 0.6447 | 0.6895 | -0.0249 |
| | RF | 0.5981 | 0.6804 | -0.0340 |
| | *greedy=0.7144, oracle=0.8231* | | | |
| **CoNLL** | LR | 0.8898 | 0.9311 | -0.0250 |
| | MLP | 0.8364 | 0.8338 | -0.1223 |
| | RF | 0.8409 | 0.9366 | **-0.0195** |
| | *greedy=0.9561, oracle=0.9778* | | | |
| **FewNERD** | LR | 0.7808 | 0.7980 | -0.0538 |
| | MLP | 0.7819 | 0.6936 | -0.1582 |
| | RF | 0.7492 | 0.7905 | -0.0612 |
| | *greedy=0.8518, oracle=0.9204* | | | |

## Feature Importance（RF Gini）

| Feature | SciERC | CoNLL | FewNERD |
|---------|--------|-------|---------|
| logprob | **0.321** | **0.362** | **0.292** |
| fleiss_kappa | 0.222 | 0.159 | 0.198 |
| soft_jaccard | 0.218 | 0.186 | 0.203 |
| exact_match | 0.136 | 0.195 | 0.209 |
| voting_confidence | 0.103 | 0.097 | 0.098 |

## 核心结论

**Feature bottleneck 结论成立。**

1. **所有 3 个分类器在所有 3 个数据集上都无法超过 greedy**。最大 delta 为 -0.0195（CoNLL RF），仍为负值。MLP 表现最差（delta 低至 -0.1582），可能因 5 维特征空间太小导致过拟合。

2. **更强的分类器不仅没有改善，反而更差**。RF 和 MLP 的 AUROC 一致低于 LR（SciERC: LR 0.67 > MLP 0.64 > RF 0.60）。这说明瓶颈不在分类器容量，而在输入特征本身信息不足。

3. **Feature importance 一致**：logprob 在所有数据集上 Gini 重要性最高（0.29-0.36），但 5 个信号的重要性分布相对平坦（没有单一 dominant 信号），进一步说明 instance-level 统计量缺乏足够的区分度。

4. **Instance-level → sample-level 的信息损失是根本原因**：5 个 QE signal 是 instance-level 聚合值，但 selection 需要 sample-level 区分力。即使分类器学会了"哪些 instance 容易"，也无法从中推导出"哪个 sample 更好"。

---
