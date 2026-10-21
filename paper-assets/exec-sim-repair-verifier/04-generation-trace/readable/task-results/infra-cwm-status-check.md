# infra cwm status check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_cwm-status-check_20260511T222609_result.json`
- **Structured JSON:** [`f722ab5ca5aaf99eff77.json`](../../sessions/f7/f722ab5ca5aaf99eff77.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE。结果：

| 指标 | Classification | CWM Generation | 差值 |
|------|---------------|----------------|------|
| Overall Acc | 87.5% | 87.51% | +0.01pp |
| Pass F1 | 87.1% | 87.31% | +0.21pp |
| Fail F1 | 87.9% | 87.71% | -0.19pp |

**结论: negative** — 假设未得到验证。CWM generation 与 classification 在 pass/fail 判别上几乎持平，task reformulation (generation→classification) 没有带来显著提升。

附加发现：
- CWM exact match rate 84.02%（生成的 output 与 ground truth 完全匹配的比例）
- SyntaxError/NameError 类别 exact match 很高（98.8%/77.3%），但 IndexError/OverflowError 很差（25%/0%）——罕见错误类型泛化不足
- Classification 方案更轻量高效，在 pass/fail 判别上效果等价，仍是更优选择

---
