# exp cls downsample 400 complete

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_cls-downsample-400-complete_20260523T194112_result.json`
- **Structured JSON:** [`1bd30f47c933cd4adaeb.json`](../../sessions/1b/1bd30f47c933cd4adaeb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

**CLS@400 Downsample (Qwen3-4B, function-level)**

| Seed | Accuracy | F1 macro |
|------|----------|----------|
| 42   | 79.47%   | 79.47%   |
| 123  | 78.20%   | 78.12%   |
| 456  | 78.04%   | 78.00%   |
| **Mean** | **78.57 ± 0.78** | **78.53 ± 0.82** |

vs TRAJ 4B function-level: **86.30 ± 0.97%** → TRAJ 领先 **7.73 pp**（使用 18× 更多样本但数据量匹配时依然如此）。结果已写入 artifacts 并注册。

---
