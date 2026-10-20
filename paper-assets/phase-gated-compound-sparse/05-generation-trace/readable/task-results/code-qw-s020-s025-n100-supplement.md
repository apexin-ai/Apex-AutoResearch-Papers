# code qw s020 s025 n100 supplement

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_qw_s020_s025_n100_supplement_20260515T210822_result.json`
- **Structured JSON:** [`83e174d8f2210b35ee80.json`](../../sessions/83/83e174d8f2210b35ee80.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已提交。汇总：

| 实验 | exp_id | GPU | tmux session | 输出文件 |
|------|--------|-----|-------------|---------|
| QW importance_s020 p51-100 | `acc_qw_s020_n100` | cuda:2 | `acc_qw_s020` | `accuracy_eval_qw_s020_n51_100.json` |
| QW importance_s025 p51-100 | `acc_qw_s025_n100` | cuda:3 | `acc_qw_s025` | `accuracy_eval_qw_s025_n51_100.json` |

修改内容：给 `run_accuracy_eval.py` 添加了 `--start-index` 参数（原文件备份为 `.bak`），数据切片改为 `data[start_index : start_index + num_problems]`。

两个任务已在跑，日志显示 Problem 1/50 已开始处理（即全局第 51 题）。seed=42，max_new_tokens=2048，与前 50 题一致。

---
