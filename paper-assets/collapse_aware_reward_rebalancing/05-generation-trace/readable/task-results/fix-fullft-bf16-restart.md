# fix fullft bf16 restart

**Does Reward Curation Kill Diversity? Systematic Evidence of Surprising Resilience in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_fullft_bf16_restart_20260516T165351_result.json`
- **Structured JSON:** [`f23e32a6c354fd1fad66.json`](../../sessions/f2/f23e32a6c354fd1fad66.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程启动正常：
- 数据集从离线 cache 加载成功
- `torch_dtype` deprecation warning 无害（新版 transformers 推荐用 `dtype`）
- 无 import error，无崩溃

完成：
1. `train_sft.py` 第86-87行：Full-FT 分支改为 `bf16=True`，LoRA 保持 `fp16=True`
2. 模型加载已条件化（之前已改过）
3. `carr_fullft_k4_probe_02` 已在 cuda:1 启动，Gen 0 generation 会从 checkpoint 恢复，然后从 scoring 开始重跑

---
