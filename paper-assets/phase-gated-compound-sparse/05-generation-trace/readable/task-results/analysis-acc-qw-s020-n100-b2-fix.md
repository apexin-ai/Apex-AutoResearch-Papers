# analysis acc qw s020 n100 b2 fix

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_acc_qw_s020_n100_b2_fix_20260515T224237_result.json`
- **Structured JSON:** [`0536eb875e0a2314d068.json`](../../sessions/05/0536eb875e0a2314d068.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。总结：

**acc_qw_s020_n100_b2_fix 结果**

| 指标 | 值 |
|------|-----|
| batch2 fix | 23/50 = 0.46 |
| 原 batch2 (2048 tokens) | 22/50 = 0.44 |
| **差异** | **+1 correct (+0.02)** |
| batch1 v2 rescored | 13/50 = 0.26 |
| **combined** | **36/100 = 0.36** |
| null predictions | 2 |
| truncated (hit 8192) | 1 |
| 用时 | 884s |

**更新后 QW dose curve**：

| sparsity | accuracy |
|----------|----------|
| dense | 0.40 |
| s015 | 0.36 |
| **s020** | **0.36** (原 0.35) |
| s025 | 0.33 |
| s030 | 0.19 |

max_new_tokens 修复影响极小（仅 +1 题），s020 从 0.35 微调至 0.36，与 s015 持平。

---
