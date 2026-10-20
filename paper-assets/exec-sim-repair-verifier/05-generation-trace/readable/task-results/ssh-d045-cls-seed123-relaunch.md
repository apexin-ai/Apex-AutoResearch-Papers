# ssh d045 cls seed123 relaunch

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d045-cls-seed123-relaunch_20260513T070140_result.json`
- **Structured JSON:** [`f5884bdd6612c0e574f8.json`](../../sessions/f5/f5884bdd6612c0e574f8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已启动并在运行。

**汇报：**

1. **旧进程**：PID 2940525/2940520 已成功 kill
2. **新进程**：PID 126190（Python 子进程），参数确认 `--max_steps 400 --seed 123`
3. **GPU 使用**：GPU 0 占用 24915/32607 MiB（99% 利用率），GPU 2 继续跑 eval_repo_cwm
4. **训练日志确认**：
   - `max_steps=400`（进度条 0/400）
   - trainable params: 11,796,480 (0.29%)
   - 速度 ~7.8s/step → 预计 ~52 分钟完成
   - 输出目录：`checkpoints_repo_cls_seed123/`

**额外发现**：`--eval_steps`、`--save_steps`、`--save_total_limit` 不是 `train_repo_verifier.py` 支持的参数，已去掉。脚本内部的 TrainingArguments 会使用自己的默认值。

---
