# ssh deepseek cwm s123 diagnosis

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_deepseek-cwm-s123-diagnosis_20260520T012557_result.json`
- **Structured JSON:** [`ad96545e7c43b723989d.json`](../../sessions/ad/ad96545e7c43b723989d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已成功启动。

**死因**: s123 启动命令多了 `--dataloader_num_workers 0` 参数，`train_unified.py` 不接受该 CLI 参数（硬编码为 4），argparse 直接报错退出 (EXIT_CODE=2)。

**修复**: 去掉 `--dataloader_num_workers 0`，其余参数与 s42 一致（seed=123, GPU=2, output_dir 改为 `checkpoints_deepseek_cwm_repo_s123`）。

**当前状态**: 训练正常运行中，GPU 2 占用 7185 MiB，总步数 2865，刚开始第一步。

---
