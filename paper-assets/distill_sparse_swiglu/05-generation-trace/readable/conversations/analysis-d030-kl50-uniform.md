# analysis d030 kl50 uniform

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_analysis_d030_kl50_uniform_20260516T050416.jsonl`
- **Structured JSON:** [`78c49f2d00a9784a3eb9.json`](../../sessions/78/78c49f2d00a9784a3eb9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-16T05:05:15.866331+00:00_

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
  "session": "worker_analysis_d030_kl50_uniform_20260516T050416",
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

_source line 2 · 2026-05-16T05:05:15.866799+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d030_kl50_uniform_20260516T050416",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T05:05:15.867081+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34887",
  "command": "tail -100 /root/runs/distill_sparse_swiglu/d030_kl50_uniform.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d030_kl50_uniform_20260516T050416",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34887",
    "command": "tail -100 /root/runs/distill_sparse_swiglu/d030_kl50_uniform.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-16T05:05:15.867311+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34887",
  "command": "find /root/distill_sparse_swiglu/results/ -name \"*uniform*\" -o -name \"*kl50*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d030_kl50_uniform_20260516T050416",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34887",
    "command": "find /root/distill_sparse_swiglu/results/ -name \"*uniform*\" -o -name \"*kl50*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-16T05:05:15.867657+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Overwriting default num_fewshot of mmlu_high_school_geography from None to 5\\nOverwriting default num_fewshot of mmlu_high_school_government_and_politics from None to 5\\nOverwriting default num_fewshot of mmlu_high_school_macroeconomics from None to 5\\nOverwriting default num_fewshot of mmlu_high_school_microeconomics from None to 5\\nOverwriting default num_fewshot of mmlu_high_school_psychology from None to 5\\nOverwriting default num_fewshot of mmlu_human_sexuality from None to 5\\nOverwriting default num_fewshot of mmlu_professional_psychology from None to 5\\nOverwriting default num_fewshot of mmlu_public_relations from None to 5\\nOverwriting default num_fewshot of mmlu_security_studies from None to 5\\nOverwriting default num_fewshot of mmlu_sociology from None to 5\\nOverwriting default num_fewshot of mmlu_us_foreign_policy from None to 5\\nOverwriting default num_fewshot of mmlu_formal_logic from None to 5\\nOverwriting default num_fewshot of mmlu_high_school_european_history from None to 5\\nOverwriting default num_fewshot of mmlu_high_school_us_history from None to 5\\nOverwriting default num_fewshot of mmlu_high_school_world_history from None to 5\\nOverwriting default num_fewshot of mmlu_international_law from None to 5\\nOverwriting default num_fewshot of mmlu_jurisprudence from None to 5\\nOverwriting default num_fewshot of mmlu_logical_fallacies from None to 5\\nOverwriting default num_fewshot of mmlu_moral_disputes from None to 5\\nOverwriting default num_fewshot of mmlu_moral_scenarios from None to 5\\nOverwriting default num_fewshot of mmlu_philosophy from None to 5\\nOverwriting default num_fewshot of mmlu_prehistory from None to 5\\nOverwriting default num_fewshot of mmlu_professional_law from None to 5\\nOverwriting default num_fewshot of mmlu_world_religions from None to 5\\n\\r  0%|          | 0/1267 [00:00<?, ?it/s]\\r100%|██████████| 1267/1267 [00:00<00:00, 38217.24it/s]\\n\\r  0%| 
…[truncated 6463 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d030_kl50_uniform_20260516T050416",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T05:05:15.867931+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/distill_sparse_swiglu/results/benchmark/d030_kl30_uniform\\n/root/distill_sparse_swiglu/results/benchmark/bench_mistral_kl50_s42\\n/root/distill_sparse_swiglu/results/benchmark/d030_kl50_uniform\\n/root/distill_sparse_swiglu/results/uniform_30pct_dryrun\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d030_kl50_uniform_20260516T050416",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T05:05:15.868346+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34887",
  "command": "cat /root/distill_sparse_swiglu/results/benchmark/d030_kl50_uniform/results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d030_kl50_uniform_20260516T050416",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34887",
    "command": "cat /root/distill_sparse_swiglu/results/benchmark/d030_kl50_uniform/results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T05:05:15.868718+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"exp_id\\\": \\\"d030_kl50_uniform\\\",\\n  \\\"config\\\": {\\n    \\\"model_name_or_path\\\": \\\"/root/autodl-tmp/models/llama-3.1-8b\\\",\\n    \\\"checkpoint\\\": \\\"checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt\\\",\\n    \\\"tasks\\\": \\\"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\\\",\\n    \\\"sparsity_mode\\\": \\\"teal_global\\\",\\n    \\\"baseline_mode\\\": null,\\n    \\\"dense\\\": false,\\n    \\\"exp_id\\\": \\\"d030_kl50_uniform\\\",\\n    \\\"sparsity_target\\\": 0.5,\\n    \\\"allocation\\\": \\\"uniform\\\",\\n    \\\"gpu\\\": 0,\\n    \\\"seq_len\\\": 2048,\\n    \\\"calibration_samples\\\": 32,\\n    \\\"batch_size\\\": 8,\\n    \\\"bottleneck_size\\\": 128,\\n    \\\"svd_rank\\\": 256,\\n    \\\"max_eval_samples\\\": null\\n  },\\n  \\\"mode\\\": {\\n    \\\"mode\\\": \\\"teal_global\\\",\\n    \\\"checkpoint\\\": \\\"/root/distill_sparse_swiglu/checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt\\\",\\n    \\\"sparsity_target\\\": 0.5,\\n    \\\"allocation\\\": \\\"uniform\\\"\\n  },\\n  \\\"metrics\\\": {\\n    \\\"wikitext2_ppl\\\": 11.9631,\\n    \\\"lm_eval\\\": {\\n      \\\"arc_challenge\\\": {\\n        \\\"sample_len\\\": 1172,\\n        \\\"acc\\\": 0.2833,\\n        \\\"acc_stderr\\\": 0.013167478735134564,\\n        \\\"acc_norm\\\": 0.3276,\\n        \\\"acc_norm_stderr\\\": 0.013715847940719344\\n      },\\n      \\\"winogrande\\\": {\\n        \\\"sample_len\\\": 1267,\\n        \\\"acc\\\": 0.629,\\n        \\\"acc_stderr\\\": 0.013576399902231513\\n      },\\n      \\\"mmlu\\\": {\\n        \\\"sample_len\\\": 14042,\\n        \\\"acc\\\": 0.2777,\\n        \\\"acc_stderr\\\": 0.0037492851439913264\\n      },\\n      \\\"gsm8k\\\": {\\n        \\\"sample_len\\\": 1319,\\n        \\\"exact_match\\\": 0.0212,\\n        \\\"exact_match_stderr\\\": 0.003970449129848636\\n      }\\n    },\\n    \\\"lm_eval_raw\\\": {\\n      \\\"arc_challenge\\
…[truncated 1582 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d030_kl50_uniform_20260516T050416",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T05:05:15.868993+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34887",
  "command": "find /root/distill_sparse_swiglu/results/benchmark/d030_kl50_uniform/ -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d030_kl50_uniform_20260516T050416",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34887",
    "command": "find /root/distill_sparse_swiglu/results/benchmark/d030_kl50_uniform/ -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T05:05:15.869238+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/distill_sparse_swiglu/results/benchmark/d030_kl50_uniform/results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d030_kl50_uniform_20260516T050416",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T05:05:15.869511+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34887",
  "command": "grep -i \"layer.*sparsity\\|sparsity.*layer\\|per.layer\\|uniform.*0\\.5\\|actual.*sparsity\\|target.*sparsity\\|overall.*sparsity\" /root/runs/distill_sparse_swiglu/d030_kl50_uniform.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d030_kl50_uniform_20260516T050416",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34887",
    "command": "grep -i \"layer.*sparsity\\|sparsity.*layer\\|per.layer\\|uniform.*0\\.5\\|actual.*sparsity\\|target.*sparsity\\|overall.*sparsity\" /root/runs/distill_sparse_swiglu/d030_kl50_uniform.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T05:05:15.869731+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d030_kl50_uniform_20260516T050416",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T05:05:15.869939+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34887",
  "command": "grep -iE \"sparsity\" /root/runs/distill_sparse_swiglu/d030_kl50_uniform.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d030_kl50_uniform_20260516T050416",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34887",
    "command": "grep -iE \"sparsity\" /root/runs/distill_sparse_swiglu/d030_kl50_uniform.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T05:05:15.870170+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Per-layer sparsity (TEAL-predictor):\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d030_kl50_uniform_20260516T050416",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T05:05:15.870355+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34887",
  "command": "grep -A 40 \"Per-layer sparsity\" /root/runs/distill_sparse_swiglu/d030_kl50_uniform.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d030_kl50_uniform_20260516T050416",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34887",
    "command": "grep -A 40 \"Per-layer sparsity\" /root/runs/distill_sparse_swiglu/d030_kl50_uniform.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T05:05:15.870556+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Per-layer sparsity (TEAL-predictor):\\n  Layer  0: 0.500\\n  Layer  1: 0.500\\n  Layer  2: 0.500\\n  Layer  3: 0.500\\n  Layer  4: 0.500\\n  Layer  5: 0.500\\n  Layer  6: 0.500\\n  Layer  7: 0.500\\n  Layer  8: 0.500\\n  Layer  9: 0.500\\n  Layer 10: 0.500\\n  Layer 11: 0.500\\n  Layer 12: 0.500\\n  Layer 13: 0.500\\n  Layer 14: 0.500\\n  Layer 15: 0.500\\n  Layer 16: 0.500\\n  Layer 17: 0.500\\n  Layer 18: 0.500\\n  Layer 19: 0.500\\n  Layer 20: 0.500\\n  Layer 21: 0.500\\n  Layer 22: 0.500\\n  Layer 23: 0.500\\n  Layer 24: 0.500\\n  Layer 25: 0.500\\n  Layer 26: 0.500\\n  Layer 27: 0.500\\n  Layer 28: 0.500\\n  Layer 29: 0.500\\n  Layer 30: 0.500\\n  Layer 31: 0.500\\n  Model-level: 0.500\\n\\n--- WikiText-2 PPL ---\\nUsing the latest cached version of the dataset since wikitext couldn't be found on the Hugging Face Hub (offline mode is enabled).\\nFound the latest cached dataset configuration 'wikitext-2-raw-v1' at /root/autodl-tmp/.hf_cache/datasets/wikitext/wikitext-2-raw-v1/0.0.0/b08601e04326c79dfdd32d625aee71d232d685c3 (last modified on Fri May 15 18:41:41 2026).\\n  WikiText-2: 141 sequences, seq_len=2048\\n  PPL = 11.9631  (15.5s)\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d030_kl50_uniform_20260516T050416",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-16T05:05:15.870804+00:00_

全部数据到手。Per-layer sparsity 确认全部 32 层均为 0.500，model-level 0.500。

## d030_kl50_uniform 结果

### 核心指标

| Metric | WikiText-2 PPL | ARC-c (acc_norm) | WinoGrande (acc) | MMLU (acc) | GSM8K (exact_match) |
|--------|:-:|:-:|:-:|:-:|:-:|
| **KL 50% Uniform** | **11.96** | **0.3276** | **0.6290** | **0.2777** | **0.0212** |

Per-layer sparsity: 全部 32 层 = 0.500, model-level = 0.500 ✓

### 全方法对比

| Method | ARC-c | WG | MMLU | GSM8K |
|--------|:-----:|:--:|:----:|:-----:|
| Dense | 0.5819 | 0.7814 | 0.6532 | 0.5004 |
| KL 30% Uniform | 0.4078 | 0.6859 | **0.4061** | 0.0735 |
| **KL 50% Uniform** | **0.3276** | **0.6290** | **0.2777** | **0.0212** |
| KL 50% Global top-k | 0.3771 | 0.6156 | 0.2591 | 0.0121 |
| TEAL 50% | 0.2910 | 0.5556 | 0.2856 | 0.0190 |

### 50% Uniform vs Baselines (delta)

| vs. | ARC-c | WG | MMLU | GSM8K |
|-----|:-----:|:--:|:----:|:-----:|
| vs Dense | -0.2543 | -0.1524 | -0.3755 | -0.4792 |
| vs KL 50% Global | -0.0495 | +0.0134 | +0.0186 | +0.0091 |
| vs TEAL 50% | +0.0366 | +0.0734 | -0.0079 | +0.0022 |
| vs KL 30% Uniform | -0.0802 | -0.0569 | -0.1284 | -0.0523 |

### 结论

**50% uniform 未能修复 MMLU。** MMLU = 27.77%，接近随机水平（25%），与 KL 50% global top-k 的 25.91% 几乎无差异（仅 +1.86pp）。对比之下，30% uniform 曾将 MMLU 从 28.74% 拉到 40.61%（+12pp）。**Uniform allocation 的 MMLU 修复效应在 50% sparsity 下完全消失。**

**GSM8K 仍然接近 0**（2.12%），与 50% global（1.21%）和 TEAL 50%（1.90%）同级别。

**50% 是断崖点（Narrative B）：** 在 50% sparsity 下，uniform allocation 无法提供 30% 时观察到的知识保留优势。ARC-c 和 WG 相比 50% global 也基本持平（WG 略好 +1.3pp），uniform 的分配优势已不显著。唯一亮点是相比 TEAL 50%，WG 还有 +7.3pp 的优势，说明 KL predictor 本身在 50% 下仍优于 TEAL，但 uniform vs global 的差距在此 sparsity 下基本消失。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_d030_kl50_uniform_20260516T050416"
}
```

</details>

---
