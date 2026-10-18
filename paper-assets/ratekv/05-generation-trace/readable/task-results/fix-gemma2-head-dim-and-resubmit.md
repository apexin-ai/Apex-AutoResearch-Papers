# fix gemma2 head dim and resubmit

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_gemma2_head_dim_and_resubmit_20260515T193817_result.json`
- **Structured JSON:** [`6e14329e4f4b2e6c1ca6.json`](../../sessions/6e/6e14329e4f4b2e6c1ca6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成：

1. **Bug 修复**: `/root/ratekv/eval_ppl.py` L32 改为 `head_dim = getattr(config, 'head_dim', config.hidden_size // num_q_heads)` — Gemma-2 现在正确取 256 而非 224，其他模型不受影响。
2. **Import 验证**: `from eval_ppl import patch_attention` 通过。
3. **实验注册**: `gemma2_downstream_k8_4task_v2` 已创建，状态 QUEUED，parent 指向 v1 失败实验。等 Main Agent 提交。

---
