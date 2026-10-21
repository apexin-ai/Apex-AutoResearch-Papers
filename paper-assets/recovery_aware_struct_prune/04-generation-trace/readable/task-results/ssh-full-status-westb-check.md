# ssh full status westb check

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_full_status_westb_check_20260522T150432_result.json`
- **Structured JSON:** [`fbbbaa1a06e4747d350b.json`](../../sessions/fb/fbbbaa1a06e4747d350b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westb-23072 状态汇报

### GPU:0 — seed456 GRPO v5 (PID 209508)
- **状态: Running** ✓
- **PID 209508** 确认存活，已运行 ~2h，CPU 118%，显存 55718/97887 MiB
- **进度**: completions 已到 `completions_00060.parquet`（共 60 steps），目标 100 steps → **约 60% 完成**
- **checkpoint-100 尚未生成**，训练仍在进行中
- 输出目录目前只有 `completions/` 子目录

### GPU:1 — MF3 v2 N=500 eval (PID 217798)
- **状态: 已崩溃（进程残留）** ✗
- PID 217798 仍占用 GPU 显存 16538 MiB，但 **eval 脚本已报错退出**
- **错误原因**: `OSError: Can't load the configuration of 'grpo_qwen_math_cka_only_20'` — model_path 传入的是相对名称而非完整路径，找不到 config.json
- 日志中仅匹配到 2 行 "correct"，基本没有产出有效结果
- 进程可能是 vLLM/模型加载残留，需 kill 释放显存

### 磁盘
- `/root/autodl-tmp/`: 218G/250G used (88%)，剩余 33G

### 需要处理
1. **GPU:1**: kill PID 217798 释放显存，修复 model_path 后重跑 MF3 v2 eval
2. **GPU:0**: 正常运行，预计再 ~1.3h 完成剩余 40 steps

---
