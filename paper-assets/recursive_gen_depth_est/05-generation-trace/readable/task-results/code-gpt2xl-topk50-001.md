# code gpt2xl topk50 001

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gpt2xl_topk50_001_20260514T224607_result.json`
- **Structured JSON:** [`5c53d1f625dcc50f73e5.json`](../../sessions/5c/5c53d1f625dcc50f73e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务已在运行，GPT-2 XL 模型正在加载，即将开始 depth-1 生成。

**总结**：
- 创建了 `scripts/run_pipeline_gpt2xl_topk50.sh`，解码策略 top-k k=50, temperature=1.0
- depth-0 adapter 通过 symlink 复用自 `checkpoints/gpt2xl/lora_depth_0`，跳过重复 finetune
- 已提交为 `gpt2xl_topk50_001`，PID 211326，cuda:0，registry 状态 RUNNING

---
