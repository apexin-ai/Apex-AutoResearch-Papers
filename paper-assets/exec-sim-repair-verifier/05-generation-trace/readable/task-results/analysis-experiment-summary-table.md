# analysis experiment summary table

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_experiment-summary-table_20260514T003543_result.json`
- **Structured JSON:** [`398dffacae1cb94b7158.json`](../../sessions/39/398dffacae1cb94b7158.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总报告已注册为 artifact `art_20260514_515c1c`，核心数字已追加到 memory.md。

**关键结果**:

| 配置 | Accuracy | CLS−CWM Gap |
|------|----------|-------------|
| 4B (5-seed) | CLS 88.43±0.78 / CWM 87.19±0.37 | +1.25±1.01pp (p=0.051) |
| 8B (3-seed) | CLS 89.39±1.09 / CWM 86.96±0.72 | +2.42±0.37pp (p=0.008) |
| Traj (5-seed) | 86.30±0.97 | TOST≈CLS (p=0.007) |
| Zero-shot 32B | 71.69 | vs FT 4B: −16.74pp |
| Repo CLS v5 | 76.92 | CWM eval invalid |

Scaling 放大 gap +1.24pp (CLS 吃到 scaling, CWM 不吃)。Repo-level 只有 CLS v5 有效，CWM 因 unparseable 过高不可用。

---
