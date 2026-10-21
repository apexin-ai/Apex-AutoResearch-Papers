# analysis c4 kl30 s42 eval

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 5
- **Recorded user turns:** 0
- **Tool calls:** 2
- **Original source:** `logs/chats/worker_analysis_c4_kl30_s42_eval_20260523T030806.jsonl`
- **Structured JSON:** [`612eed329ddc6c5cfca0.json`](../../sessions/61/612eed329ddc6c5cfca0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

5 recorded events

### Tool call

_source line 1 · 2026-05-23T03:08:40.007971+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_c4_kl30_s42_eval_20260523T030806",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-23T03:08:40.008343+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_c4_kl30_s42_eval_20260523T030806",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T03:08:40.008520+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34887",
  "command": "cat /root/runs/distill_sparse_swiglu/c4_kl30_s42_eval.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_c4_kl30_s42_eval_20260523T030806",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34887",
    "command": "cat /root/runs/distill_sparse_swiglu/c4_kl30_s42_eval.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-23T03:08:40.008747+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Loading model: /root/autodl-tmp/models/llama-3.1-8b\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading weights:   0%|          | 0/291 [00:00<?, ?it/s]\\rLoading weights:   0%|          | 1/291 [00:00<00:33,  8.65it/s]\\rLoading weights:   1%|          | 2/291 [00:00<00:38,  7.55it/s]\\rLoading weights:   5%|▍         | 14/291 [00:00<00:05, 51.17it/s]\\rLoading weights:  10%|▉         | 28/291 [00:00<00:03, 81.97it/s]\\rLoading weights:  14%|█▍        | 41/291 [00:00<00:02, 96.00it/s]\\rLoading weights:  19%|█▉        | 56/291 [00:00<00:02, 80.70it/s]\\rLoading weights:  30%|██▉       | 86/291 [00:00<00:01, 133.47it/s]\\rLoading weights:  35%|███▌      | 103/291 [00:01<00:01, 140.68it/s]\\rLoading weights:  41%|████      | 119/291 [00:01<00:01, 138.86it/s]\\rLoading weights:  46%|████▌     | 134/291 [00:01<00:01, 132.95it/s]\\rLoading weights:  51%|█████     | 149/291 [00:01<00:01, 132.08it/s]\\rLoading weights:  56%|█████���    | 164/291 [00:01<00:00, 136.59it/s]\\rLoading weights:  62%|██████▏   | 179/291 [00:01<00:00, 134.25it/s]\\rLoading weights:  67%|██████▋   | 194/291 [00:01<00:00, 133.32it/s]\\rLoading weights:  71%|███████▏  | 208/291 [00:01<00:00, 132.61it/s]\\rLoading weights:  76%|███████▋  | 222/291 [00:01<00:00, 127.40it/s]\\rLoading weights:  82%|████████▏ | 239/291 [00:02<00:00, 135.03it/s]\\rLoading weights:  88%|████████▊ | 256/291 [00:02<00:00, 142.01it/s]\\rLoading weights:  93%|█████████▎| 271/291 [00:02<00:00, 128.81it/s]\\rLoading weights:  98%|█████████▊| 285/291 [00:02<00:00, 122.25it/s]\\rLoading weights: 100%|██████████| 291/291 [00:02<00:00, 120.14it/s]\\nMode: TEAL global mask from predictor (allocation=uniform)\\n  checkpoint: /root/distill_sparse_swiglu/checkpoints/c4_kl30_s42/predictor_kl_normalized.pt\\nComputing TEAL global masks from predictor ...\\n\\nPer-layer sparsity (TEAL-predictor):\\n  Layer  0: 0.293\\n  Layer  1: 0.297\\n  Layer  2: 0.297
…[truncated 6485 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_c4_kl30_s42_eval_20260523T030806",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-23T03:08:40.008977+00:00_

实验正常完成，EXIT_CODE=0，无报错。

## C4 KL30 S42 Eval 结果 vs 基线

| Task | Metric | C4 KL30 | Baseline (WT103) | Δ |
|------|--------|---------|-------------------|---|
| WikiText-2 | PPL ↓ | **11.554** | 8.81 | +2.74 (worse) |
| ARC-Challenge | acc_norm | **43.09%** | 43.7% | −0.61pp |
| WinoGrande | acc | **68.67%** | 68.9% | −0.23pp |
| MMLU | acc | **39.95%** | 40.7% | −0.75pp |
| GSM8K | exact_match | **4.09%** | 7.5% | −3.41pp |
| HellaSwag | acc_norm | **69.24%** | — | — |
| PIQA | acc | **75.03%** | — | — |

模型级稀疏率：29.5%（TEAL uniform allocation）。

## 总结

C4 训练数据**未能改善** MMLU 和 GSM8K，反而全面退步：

- **PPL 大幅恶化** (+2.74)，说明 C4 训练的 predictor 在 WikiText-2 上泛化更差
- **GSM8K 跌幅最大** (−3.41pp)，从 7.5% 降到 4.09%
- **MMLU 也下降** (−0.75pp)，与预期的"多样数据改善下游"相反
- ARC-c 和 WinoGrande 基本持平，略微下降

结论：WikiText-103 训练的 predictor 在所有可比指标上优于 C4 训练版本。C4 数据的多样性未能转化为更好的稀疏掩码质量。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_c4_kl30_s42_eval_20260523T030806"
}
```

</details>

---
