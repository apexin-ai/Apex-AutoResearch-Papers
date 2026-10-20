# data error analysis fix

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_error-analysis-fix_20260515T081655_result.json`
- **Structured JSON:** [`d5d1c5be29f903c44bea.json`](../../sessions/d5/d5d1c5be29f903c44bea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两份文件均已修改完成。变更汇总：

| 位置 | 旧值 | 新值 |
|------|------|------|
| §1 列标题 | CLS 8B best | CLS 8B (val-sel) |
| §1 Accuracy | 84.79% | **83.52%** |
| §1 F1 macro/fail/pass | 81.18% / 72.93% / 89.43% | ⚠️ TBD（需从 ckpt-1000 eval 补填） |
| §1 vs Majority | +11.83 | +10.56 |
| §1 8B gap | 84.79% vs 58.04% = 26.75pp | 83.52% vs 58.04% = 25.48pp |
| §1 实验引用 | ckpt-400 为 primary | ckpt-400 标 superseded，ckpt-1000 标 primary (val-sel) |
| §4 Repo-level 表 | 84.79% / +26.75 | 83.52% / +25.48 |

新增 D088 修正说明注释。§10 Key Sentences 中未直接引用 84.79%/8B 数字，无需改动。

**待办**: CLS 8B ckpt-1000 的 test F1 macro/fail/pass 需要从 eval 结果补填到 TBD 位置。

---
