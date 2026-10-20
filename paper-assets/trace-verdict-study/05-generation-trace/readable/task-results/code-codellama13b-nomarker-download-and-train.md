# code codellama13b nomarker download and train

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_codellama13b_nomarker_download_and_train_20260517T030241_result.json`
- **Structured JSON:** [`ce352dea42f653a121ea.json`](../../sessions/ce/ce352dea42f653a121ea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成：

- **模型下载 + 训练 + 评估**已提交为一条串联任务，PID: 322984，tmux session: `codellama13b_nomarker_seed42`
- 执行顺序：huggingface-cli 下载 CodeLlama-13b-Instruct-hf → tokenizer 验证 → train_sft.py 训练 → evaluate.py 评估
- 训练数据：exception_only_nomarker（train 4720 条 / test 1190 条）
- Registry 已更新为 RUNNING 状态
- 日志：`~/runs/trace-verdict-study/codellama13b_nomarker_seed42.log`

模型下载约 26GB，下载完成后会自动进入训练阶段。可以稍后用 `check-training-status` 查看进度。

---
