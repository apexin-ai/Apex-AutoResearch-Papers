# analysis per test majority voting

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_per-test-majority-voting_20260512T092605_result.json`
- **Structured JSON:** [`36d4e56f2d047a4645c2.json`](../../sessions/36/36d4e56f2d047a4645c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新（之前的 hook 已自动填充了大部分字段）。汇总：

**Per-test Majority Voting (K=3, temp=0.7) 结果**

| 指标 | Single-pass (greedy) | Majority Vote (K=3) | Delta |
|------|---------------------|---------------------|-------|
| Accuracy | 87.51% | 86.83% | **-0.69pp** |
| PASS F1 | 87.15% | 86.33% | -0.82pp |
| FAIL F1 | 87.86% | 87.29% | -0.57pp |
| PASS Precision | 93.24% | 93.24% | 0 |
| PASS Recall | 81.80% | 80.37% | -1.43pp |
| FAIL Precision | 82.75% | 81.66% | -1.09pp |
| FAIL Recall | 93.64% | 93.75% | +0.11pp |

**Majority Voting 特有指标：**
- Agreement: 93.3% unanimous (1763/1890), 6.7% split (127/1890)
- Flips: 15 correct→wrong, 28 wrong→correct → net -13
- Per-pass accuracies: 86.72%, 86.83%, 87.62%
- 推理时间: 30s → 120s (4x)

**结论: negative。** 模型错误是系统性偏差（precision/recall 不对称），不是随机噪声，majority voting 无法修复。93.3% 样本三次预测完全一致，仅在 127 个分歧样本中 voting 反而引入更多错误（28 wrong flips > 15 correct flips）。Single-pass greedy 仍是最优推理策略。

---
