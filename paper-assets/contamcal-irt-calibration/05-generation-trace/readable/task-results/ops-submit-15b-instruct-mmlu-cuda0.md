# ops submit 15B instruct mmlu cuda0

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_submit_15B_instruct_mmlu_cuda0_20260516T211836_result.json`
- **Structured JSON:** [`0099c667fcbb6db172e0.json`](../../sessions/00/0099c667fcbb6db172e0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成：

- **exp_002_signals_15B_instruct_mmlu_v2** 已在 cuda:0 上启动（PID 870969）
- 模型：`/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B-Instruct`
- 使用 `HF_DATASETS_OFFLINE=1` 绕过 HuggingFace 网络超时，从本地缓存加载 MMLU（14042 items）
- tmux session：`exp002_15B_instruct_mmlu_v2`
- 当前状态：S1 embedding 编码中（sentence-transformers），进度 ~5%
- Registry 已更新为 RUNNING

与 v1 的区别：使用 cuda:0（非 cuda:4）、batch-size 4、离线模式、显式指定完整模型路径。

---
