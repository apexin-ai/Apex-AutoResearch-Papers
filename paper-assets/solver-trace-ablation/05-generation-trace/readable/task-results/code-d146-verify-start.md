# code d146 verify start

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d146-verify-start_20260519T145552_result.json`
- **Structured JSON:** [`8a89213a9b6fc95b5002.json`](../../sessions/8a/8a89213a9b6fc95b5002.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**训练失败。** 崩溃原因明确：

**日志内容：**
```
Tue May 19 22:55:32 CST 2026 [D146] exec s42
bash: line 1: --config: command not found
EXIT_CODE=127
```

**诊断：**
- tmux session 已退出（无活跃 session）
- GPU 0：0 MiB 显存，0% 利用率 — 完全空闲
- 崩溃原因：**提交的命令缺少 Python 脚本调用**，`--config` 被 bash 当作可执行文件执行，返回 `command not found`（exit code 127）
- config 文件存在：`grpo_prooffol_exec_only.yaml`（436B）、`grpo_prooffol_isr_b01.yaml`（420B）
- 数据文件存在：`prooffol_train_500.jsonl`（629KB）

**结论：** 需要修复 submit 命令，确保格式为 `python train_grpo.py --config configs/grpo_prooffol_exec_only.yaml ...` 而非裸 `--config ...`。

---
