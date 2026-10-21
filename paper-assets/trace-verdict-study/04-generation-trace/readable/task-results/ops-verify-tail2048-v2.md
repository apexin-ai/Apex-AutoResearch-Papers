# ops verify tail2048 v2

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify_tail2048_v2_20260518T035329_result.json`
- **Structured JSON:** [`6632ce63345435c4e14a.json`](../../sessions/66/6632ce63345435c4e14a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**启动成功，无报错。**

状态汇总：
- **进程 405136** 存活，子进程 PID 405141 在 GPU 1 上运行
- **GPU 1**: 25782MiB 已占用（CodeLlama-13B 加载完成）
- **GPU 0**: 另一任务 (PID 403391) 占用 42630MiB，100% 利用率
- **日志**: 模型加载完成，Train 4720 / Eval 1190 样本，tokenization 完成，已进入训练循环 (`0/444 steps`)
- **配置确认**: `full_trace_tail` condition, gradient_checkpointing 启用, seed=42, wandb 已配置

注意：`--model_path` 指向 `/root/autodl-tmp/models/CodeLlama-13b-Instruct-hf`，`--output_dir` 指向 `/root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_full_trace_tail2048_seed42_v2`（均在 autodl-tmp 下）。

---
