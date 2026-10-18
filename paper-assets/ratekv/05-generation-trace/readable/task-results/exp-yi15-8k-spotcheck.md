# exp yi15 8k spotcheck

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_yi15_8k_spotcheck_20260515T132509_result.json`
- **Structured JSON:** [`250f977fa2102361b498.json`](../../sessions/25/250f977fa2102361b498.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已启动并注册为 RUNNING。

**状态**：
- **PID**: 337148 on `westd-37397` cuda:0
- **进度**: 模型已加载 (bf16, ~17GB)，正在跑 WikiText-2 8K stride baseline PPL 评估
- **Solver 分配**: 180×4bit, 8×2bit, 4×8bit（与 2K 的 k=2 不同，这里用 k=8 允许更多 2-bit heads）
- **Registry**: `yi15_8k_spotcheck` → RUNNING
- **预计耗时**: 8K stride 评估 3 组约 15-30 分钟（9B 模型 + 8K context window）
- **日志**: `tail /tmp/yi15_8k_spotcheck.log`

token sequence length 警告 (338838 > 4096) 是正常的——Yi-1.5-9B 的 `max_position_embeddings=4096` 但 RoPE theta=5M 支持外推到 8K。

---
