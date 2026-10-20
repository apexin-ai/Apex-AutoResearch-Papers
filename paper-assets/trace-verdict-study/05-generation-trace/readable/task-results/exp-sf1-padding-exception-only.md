# exp sf1 padding exception only

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_sf1_padding_exception_only_20260521T182445_result.json`
- **Structured JSON:** [`d85f28c79d35286879b8.json`](../../sessions/d8/d85f28c79d35286879b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

- **Padded 数据**：`exception_only_padded2048_{train,test}.jsonl` 已生成，所有样本 padding 到 2047 tokens（使用 `.\n` pattern 避免 tokenizer 合并）
- **训练脚本**：`train_sft.py` 和 `evaluate.py` 的 condition choices 已加 `exception_only_padded2048`
- **训练状态**：GPU 1 已占用 41GB，0/444 steps 开始训练，训练完自动接 eval
- **Registry**：`exception_only_padded2048_seed42` 已更新为 RUNNING

---
