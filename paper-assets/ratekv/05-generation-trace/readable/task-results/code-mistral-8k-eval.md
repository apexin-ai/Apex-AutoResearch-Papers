# code mistral 8k eval

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mistral_8k_eval_20260516T032251_result.json`
- **Structured JSON:** [`3102c78b3e266567de3c.json`](../../sessions/31/3102c78b3e266567de3c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

运行正常。模型已加载，正在评估 BF16 baseline @ 8K。

任务已完成：
- 脚本 `run_mistral_8k_eval.py` 已写入本地（已 commit）和服务器
- Dry-run 通过，import 无误
- 已提交到 westd-37397 cuda:1，exp_id=`mistral_8k_eval`
- 日志：`~/runs/ratekv/mistral_8k_eval.log`
- 配置：Mistral-7B-v0.3, k=2, budget=0.25, 8192 stride, Flat shape (c=0.22)
- 预计输出：`artifacts/mistral_8k_eval_results.json`（BF16/MCKP/uniform 三组 8K PPL）

---
