# analyze per test majority voting

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_per-test-majority-voting_20260512T092930_result.json`
- **Structured JSON:** [`cb620a139eb74116898d.json`](../../sessions/cb/cb620a139eb74116898d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Per-test Majority Voting 实验结果

**实验状态：成功完成** (EXIT_CODE=0)

### 关键 Metrics

| Metric | Single-pass (greedy) | Majority Vote (K=3) | Delta |
|--------|---------------------|---------------------|-------|
| **Accuracy** | 87.51% | 86.83% | **-0.69pp** |
| FAIL F1 | 87.86% | 87.29% | -0.57pp |
| PASS F1 | 87.15% | 86.33% | -0.82pp |
| FAIL Recall | 93.64% | 93.75% | +0.11pp |
| PASS Recall | 81.80% | 80.37% | -1.43pp |

### 与 Baseline 对比

| Method | Accuracy |
|--------|----------|
| 3-seed mean (baseline) | 88.41% |
| Single-pass seed 42 | 87.83% |
| 本次 greedy | 87.51% |
| **Majority vote K=3** | **86.83%** |

### Flip 分析

- 3/3 unanimous: 1763 (93.3%) — 绝大多数样本三次预测一致
- 2/3 split: 127 (6.7%)
- Flipped correct→wrong: **28**, Flipped wrong→correct: **15**, Net: **-13**

Majority voting 在 127 个分歧样本上翻转了 43 个预测，但翻错的比翻对的多 13 个，导致整体下降。

### Per-pass 采样准确率

Pass 1: 86.72%, Pass 2: 86.83%, Pass 3: 87.62% — 三次采样均低于 greedy (87.51%)，temperature=0.7 引入的随机性降低了单次准确率。

### 结论

**Majority voting 无效，反而降低了 accuracy (-0.69pp)**。原因：

1. 模型在 greedy 模式下已经高度校准（87.5%），temperature 采样引入的噪声大于纠错收益
2. 93.3% 的样本三次一致，说明模型对大部分样本已高度 confident，self-consistency 无空间发挥
3. 在少数分歧样本上，错误翻转多于正确翻转（28 vs 15），说明模型错误不是随机噪声而是系统性偏差，voting 无法修复

**Per-test majority voting 不值得采用。** Single-pass greedy 更快（30s vs 120s）且更准。

---
