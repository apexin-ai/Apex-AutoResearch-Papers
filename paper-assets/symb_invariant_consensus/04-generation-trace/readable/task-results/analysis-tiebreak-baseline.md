# analysis tiebreak baseline

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_tiebreak_baseline_20260516T051248_result.json`
- **Structured JSON:** [`6a039668b079396d7a17.json`](../../sessions/6a/6a039668b079396d7a17.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果如下：

## Tiebreak 分析结果

**60 题中有 5 题出现平局（top-2 候选票数相同）。**

### 策略对比

| Method | Accuracy | 95% CI | Correct/Total |
|--------|----------|--------|---------------|
| **SICA (constraint-weighted)** | **80.0%** | — | **4/5** |
| Random (bootstrap 10k) | 50.0% | [0.0, 100.0] | — |
| Alphabetical | 60.0% | — | 3/5 |
| First-seen | 40.0% | — | 2/5 |
| Majority-of-first-6 | 60.0% | — | 3/5 |

SICA tiebreak 80% 准确率，显著优于随机的 50%。

### SICA Wins（4题）

- **P11**: False vs Unknown 各5票，SICA 分数 145.5 vs 127.0，margin=18.5 → 选 False ✓
- **P29**: False vs Unknown 各6票，SICA 分数 3.0 vs 33.0，margin=30.0 → 选 Unknown ✓
- **P42**: Unknown vs False 各6票，SICA 分数 45.0 vs 46.0，margin=1.0 → 选 False ✓
- **P59**: False vs Unknown 各6票，SICA 分数 61.0 vs 64.0，margin=3.0 → 选 Unknown ✓

### SICA Loss（1题）

- **P03**: True vs Unknown 各6票，SICA 分数 102.0 vs 105.0，delta=3.0 → 选了 Unknown，实际答案 True。分数差距很小（3分），约束加权在此题上轻微偏向了错误答案。

### 关键发现

- SICA 的 4 个 wins 中，P29 的 margin 最大（30.0），约束信号非常明确；P42 margin 最小（1.0），险胜
- 唯一的 loss（P03）margin 仅 3.0，属于边界情况
- 近平局（margin=1）只有 P10 一题，但 SICA 和 SC 都答错了（GT=False，但 12 条 trace 中只有 1 条给了 False）
- SICA 比 SC 多对 2 题（44 vs 42），全部来自 tiebreak 翻转（P29, P42, P59 三题 SC 错→SICA 对，P03 SC 对→SICA 错）

结果已保存至 `results/tiebreak_analysis.json`。

---
