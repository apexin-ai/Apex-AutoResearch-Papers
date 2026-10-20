# ssh submit qwen math sft math500 westb0

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_submit_qwen_math_sft_math500_westb0_20260522T230846_result.json`
- **Structured JSON:** [`c0c69006ab33f85aa882.json`](../../sessions/c0/c0c69006ab33f85aa882.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成：

- **任务已提交**: westb-23072 GPU:0, PID=250766
- **模型路径修正**: 实际路径为 `sft_qwen_math_cka_only_20_final/`（合并后的最终模型，非 checkpoint-935 子目录）
- **eval 脚本路径**: `/root/recovery_aware_struct_prune/src/eval_math500.py`
- **Registry**: `eval_math500_sft_qwen_math_cka_only_20` → RUNNING
- **Cron 监控**: 每 8 分钟检查进程状态和输出文件（job b4d98c3d）
- **westb:1 未触碰**: GRPO GSM8K eval (PID 220343) 继续运行

日志显示模型已开始加载，检测到 non-uniform MLP（符合剪枝后结构）。

---
