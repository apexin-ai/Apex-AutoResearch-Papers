# diag gemma2 downstream k8 4task

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_gemma2_downstream_k8_4task_20260515T193635_result.json`
- **Structured JSON:** [`3ccc1c9d02b57ecd9a46.json`](../../sessions/3c/3ccc1c9d02b57ecd9a46.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### Root cause

`eval_ppl.py:30` 用 `hidden_size // num_attention_heads` 计算 `head_dim`，得到 `3584 // 16 = 224`。但 Gemma-2-9B 的实际 `head_dim = 256`（模型 config 显式设置，`q_proj` 输出维度为 `16 * 256 = 4096 ≠ 3584`）。

### 日志关键错误

```
File "/root/ratekv/eval_ppl.py", line 61, in compressed_forward
    q = orig_attn.q_proj(hidden_states).view(bsz, seq_len, -1, hd).transpose(1, 2)
RuntimeError: shape '[8, 236, -1, 224]' is invalid for input of size 7733248
```

验证：`7733248 / (8 × 236) = 4096 = 16 × 256`，说明 q_proj 输出确实是 head_dim=256。

### 修复建议

`eval_ppl.py:30`，将：
```python
head_dim = config.hidden_size // num_q_heads
```
改为：
```python
head_dim = getattr(config, 'head_dim', config.hidden_size // num_q_heads)
```

Gemma-2 的 config 有显式 `head_dim` 字段。这个修复同时兼容其他模型（Llama/Mistral/Qwen/Yi 等 `hidden_size == num_heads * head_dim` 的模型不受影响）。

### 是否可重跑

修复这一行后可直接重跑。Baseline (bf16) 阶段已跑完（不经过 patch），崩溃发生在 [2/3] Uniform 4-bit 阶段首次调用 `compressed_forward` 时。

需要我直接修复本地的 `eval_ppl.py` 吗？

---
