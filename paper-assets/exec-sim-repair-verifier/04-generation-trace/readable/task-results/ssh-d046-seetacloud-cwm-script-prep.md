# ssh d046 seetacloud cwm script prep

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d046-seetacloud-cwm-script-prep_20260513T072220_result.json`
- **Structured JSON:** [`1a524f4956a13ce7cd88.json`](../../sessions/1a/1a524f4956a13ce7cd88.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

**文件路径**: `/home/sonny/exec-sim-repair-verifier/train_repo_cwm.py`

**超参修改前后对比**:

| 参数 | 修改前 | 修改后 |
|------|--------|--------|
| learning_rate (`--lr`) | 2e-4 | **5e-5** |
| weight_decay | 不存在 | **0.01** (新增 argparse + TrainingArguments) |
| warmup_ratio | 0.1 | **0.05** |
| save_total_limit | 5 | 5 (无需修改) |

**CWM eval PID 123610**: 仍在运行，已跑 58 分 7 秒。命令为 `eval_repo_cwm.py`，使用 checkpoint-400 在 cuda:0 上执行，进程未被干扰。

---
