# check verify training start

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_verify-training-start_20260514T055033_result.json`
- **Structured JSON:** [`0cf6a04e6a2ed2b21319.json`](../../sessions/0c/0cf6a04e6a2ed2b21319.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个训练 session 完全空白。session 存在但没有运行任何命令。汇报：

- **GPU 0**: 84% 利用率, 13.0/32.6 GB — `eval_cwm_seed123` CWM eval 进行中, 2696/9784 (27.5%), running_acc=57.4%
- **GPU 1**: 88% 利用率, 13.0/32.6 GB — `eval_cwm_v12` CWM eval 进行中, 2720/9784 (27.8%), running_acc=57.9%
- **GPU 2**: 0% 利用率, 0 MB 显存 — `repo-level-cwm-8b-conda` session 存在但 **pane 为空，训练未启动**，无任何输出
- **GPU 3**: 0% 利用率, 0 MB 显存 — `repo-level-cls-8b-seed123-conda` session 存在但 **pane 为空，训练未启动**，无任何输出

**结论**: 两个训练 tmux session 已创建但里面没有执行训练命令，需要手动进入 session 启动训练脚本。

---
