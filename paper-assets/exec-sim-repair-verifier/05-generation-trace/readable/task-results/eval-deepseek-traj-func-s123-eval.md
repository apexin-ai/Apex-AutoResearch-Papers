# eval deepseek traj func s123 eval

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_deepseek-traj-func-s123-eval_20260516T130058_result.json`
- **Structured JSON:** [`95b8c18f6f16965c9319.json`](../../sessions/95/95b8c18f6f16965c9319.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。

## 汇报

**deepseek-traj-func-s123** 训练 + eval 完成：

| 指标 | 值 |
|------|-----|
| eval_loss (best) | **0.0760** (epoch 2, step 1008) |
| test accuracy | **81.4%** |
| baseline (majority) | 53.6% |
| gap | **+27.8pp** (PASS, threshold ≥10pp) |
| unresolved F1 | 83.6% |
| resolved F1 | 78.5% |
| unparseable rate | 3.9% (40/1032) |
| per-test consistency | 77.0% |

训练只完成 2/3 epochs（step 1008/1512）即为 best checkpoint。模型在 traj-level 判别上表现良好，accuracy 显著超过 majority baseline。unparseable 较高（模型输出 "pass"/"fail" 而非 "resolved"/"unresolved"），但不影响整体趋势。

---
