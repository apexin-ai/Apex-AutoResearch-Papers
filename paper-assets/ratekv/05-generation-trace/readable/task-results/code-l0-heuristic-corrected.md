# code l0 heuristic corrected

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_l0_heuristic_corrected_20260514T061624_result.json`
- **Structured JSON:** [`bb8144c3ee052a534ab8.json`](../../sessions/bb/bb8144c3ee052a534ab8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验正常运行中：

- Qwen2.5-7B 模型已加载，budget 验证通过 (448/1792 = 0.25)
- 正在评估 baseline bf16 PPL（298938 tokens, 583 chunks）
- 使用 GPU 0，bf16 精度

每个模型需要 8 次 PPL eval（1 baseline + 1 uniform + 5 L0-random + 1 naive），3 个模型共 24 次。每次 eval ~2-3 分钟，预计总耗时 50-70 分钟。

Cron 每 8 分钟自动检查进度，实验完成后会自动汇报结果并更新 registry。

---
