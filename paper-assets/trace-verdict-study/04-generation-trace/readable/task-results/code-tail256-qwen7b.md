# code tail256 qwen7b

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_tail256_qwen7b_20260517T192951_result.json`
- **Structured JSON:** [`37ef2eae339013a0d583.json`](../../sessions/37/37ef2eae339013a0d583.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成：

- **数据**：`full_trace_tail_256_{train,test}.jsonl` 已存在（4720 train / 1190 test）
- **代码**：`train_sft.py` 和 `evaluate.py` 已支持 `full_trace_tail_256` condition
- **训练**：tmux session `tail256_train` 在 cuda:1 上运行，444 steps（3 epochs），训练完成后自动执行评估
- **日志**：`/root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_tail256_seed42.log`
- **Registry**：`full_trace_tail256_seed42` 状态 RUNNING

查看进度：`tmux capture-pane -t tail256_train -p | tail -5`

---
