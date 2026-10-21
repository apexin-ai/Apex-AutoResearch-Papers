# fix westb disk cleanup and eval rlvr

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_westb_disk_cleanup_and_eval_rlvr_20260516T145016_result.json`
- **Structured JSON:** [`f9f9b18d071eac6aaae8.json`](../../sessions/f9/f9f9b18d071eac6aaae8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

模型正在加载（12GB safetensors → GPU），进程正常运行。

**汇报：**

| 项目 | 结果 |
|------|------|
| 磁盘清理 | checkpoint-935 (35GB) + optimizer.pt (4.3GB) 已删除，释放 39GB → 数据盘 212G/250G (85%) |
| checkpoint-1870 | 完整保留：config.json, model.safetensors, tokenizer 文件, chat_template |
| eval 任务 | PID 625458, cuda:1, tmux session `eval_sft_rasp_rlvr_20` |
| 日志 | `~/runs/recovery_aware_struct_prune/eval_sft_rasp_rlvr_20.log` |
| 状态 | 模型加载中（Non-uniform MLP detected，正常），等待进入 GSM8K 评估 |

注意：GPU 0 上还有一个先前的 `eval_sft_rasp_25` 任务在运行（PID 602990, 28.9GB VRAM）。

---
