# check qwen s456 eval done

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_qwen-s456-eval-done_20260522T122901_result.json`
- **Structured JSON:** [`07d38e6793bf32cc6692.json`](../../sessions/07/07d38e6793bf32cc6692.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。Qwen3-8B CWM repo-level 3-seed eval 全部完成：

| Seed | Accuracy | F1_macro | F1_fail | Unparseable% |
|------|----------|----------|---------|--------------|
| s42  | 65.17%   | —        | —       | —            |
| s123 | 67.33%   | —        | —       | —            |
| **s456** | **66.93%** | **51.97** | **25.16** | **60.39%** |

s456 accuracy=66.93%，落在 65-68% 预期区间内，3-seed 均值约 66.48%。进程正常退出，checkpoint-6633，n=9784 instances 全部评完。Cron 无需删除（当前 session 无活跃 cron）。

数据可直接用于 Table 3。

---
