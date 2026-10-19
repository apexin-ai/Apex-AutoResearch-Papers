# ssh check 14b uniform results

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/chats/worker_ssh_check_14b_uniform_results_20260518T013405.jsonl`
- **Structured JSON:** [`fa3bd491166f9382f724.json`](../../sessions/fa/fa3bd491166f9382f724.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

11 recorded events

### Tool call

_source line 1 · 2026-05-18T01:34:48.296756+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_check_14b_uniform_results_20260518T013405",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-18T01:34:48.297167+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_check_14b_uniform_results_20260518T013405",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T01:34:48.297385+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-34887",
  "command": "ps aux | grep -E \"87144|87283\" | grep -v grep",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_check_14b_uniform_results_20260518T013405",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-34887",
    "command": "ps aux | grep -E \"87144|87283\" | grep -v grep",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-18T01:34:48.297526+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-34887",
  "command": "find /root/distill_sparse_swiglu -name \"results.json\" -mmin -120 2>/dev/null",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_check_14b_uniform_results_20260518T013405",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-34887",
    "command": "find /root/distill_sparse_swiglu -name \"results.json\" -mmin -120 2>/dev/null",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-18T01:34:48.297661+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 1.94}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_check_14b_uniform_results_20260518T013405",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-18T01:34:48.297790+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/distill_sparse_swiglu/results/benchmark/qwen14b_kl30_uniform_4task/results.json\\n/root/distill_sparse_swiglu/results/benchmark/qwen14b_teal30_uniform_4task/results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.69}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_check_14b_uniform_results_20260518T013405",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-18T01:34:48.297930+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-34887",
  "command": "cat /root/distill_sparse_swiglu/results/benchmark/qwen14b_kl30_uniform_4task/results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_check_14b_uniform_results_20260518T013405",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-34887",
    "command": "cat /root/distill_sparse_swiglu/results/benchmark/qwen14b_kl30_uniform_4task/results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-18T01:34:48.298091+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-34887",
  "command": "cat /root/distill_sparse_swiglu/results/benchmark/qwen14b_teal30_uniform_4task/results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_check_14b_uniform_results_20260518T013405",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-34887",
    "command": "cat /root/distill_sparse_swiglu/results/benchmark/qwen14b_teal30_uniform_4task/results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-18T01:34:48.298299+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"exp_id\\\": \\\"qwen14b_kl30_uniform_4task\\\",\\n  \\\"config\\\": {\\n    \\\"model_name_or_path\\\": \\\"/root/autodl-tmp/models/qwen2.5-14b/\\\",\\n    \\\"checkpoint\\\": \\\"checkpoints/qwen14b_kl30_s42/predictor_kl_normalized.pt\\\",\\n    \\\"tasks\\\": \\\"wikitext2,arc_challenge,winogrande,mmlu\\\",\\n    \\\"sparsity_mode\\\": \\\"teal_global\\\",\\n    \\\"baseline_mode\\\": null,\\n    \\\"dense\\\": false,\\n    \\\"exp_id\\\": \\\"qwen14b_kl30_uniform_4task\\\",\\n    \\\"sparsity_target\\\": 0.3,\\n    \\\"allocation\\\": \\\"uniform\\\",\\n    \\\"gpu\\\": 0,\\n    \\\"multi_gpu\\\": false,\\n    \\\"seq_len\\\": 2048,\\n    \\\"calibration_samples\\\": 32,\\n    \\\"batch_size\\\": 8,\\n    \\\"bottleneck_size\\\": 128,\\n    \\\"svd_rank\\\": 256,\\n    \\\"max_eval_samples\\\": null\\n  },\\n  \\\"mode\\\": {\\n    \\\"mode\\\": \\\"teal_global\\\",\\n    \\\"checkpoint\\\": \\\"/root/distill_sparse_swiglu/checkpoints/qwen14b_kl30_s42/predictor_kl_normalized.pt\\\",\\n    \\\"sparsity_target\\\": 0.3,\\n    \\\"allocation\\\": \\\"uniform\\\"\\n  },\\n  \\\"metrics\\\": {\\n    \\\"wikitext2_ppl\\\": 7.6318,\\n    \\\"lm_eval\\\": {\\n      \\\"arc_challenge\\\": {\\n        \\\"sample_len\\\": 1172,\\n        \\\"acc\\\": 0.4949,\\n        \\\"acc_stderr\\\": 0.014610624890309135,\\n        \\\"acc_norm\\\": 0.5444,\\n        \\\"acc_norm_stderr\\\": 0.014553749939306847\\n      },\\n      \\\"winogrande\\\": {\\n        \\\"sample_len\\\": 1267,\\n        \\\"acc\\\": 0.7245,\\n        \\\"acc_stderr\\\": 0.012555690055709634\\n      },\\n      \\\"mmlu\\\": {\\n        \\\"sample_len\\\": 14042,\\n        \\\"acc\\\": 0.6449,\\n        \\\"acc_stderr\\\": 0.003863900035041307\\n      }\\n    },\\n    \\\"lm_eval_raw\\\": {\\n      \\\"arc_challenge\\\": {\\n        \\\"name\\\": \\\"arc_challenge\\\",\\n        \\\"alias\\\": \\\"arc_challenge\\\",\\n        \\\"sample_len\\\": 
…[truncated 1014 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_check_14b_uniform_results_20260518T013405",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-18T01:34:48.298526+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"exp_id\\\": \\\"qwen14b_teal30_uniform_4task\\\",\\n  \\\"config\\\": {\\n    \\\"model_name_or_path\\\": \\\"/root/autodl-tmp/models/qwen2.5-14b/\\\",\\n    \\\"checkpoint\\\": null,\\n    \\\"tasks\\\": \\\"wikitext2,arc_challenge,winogrande,mmlu\\\",\\n    \\\"sparsity_mode\\\": \\\"per_token\\\",\\n    \\\"baseline_mode\\\": \\\"teal_vanilla\\\",\\n    \\\"dense\\\": false,\\n    \\\"exp_id\\\": \\\"qwen14b_teal30_uniform_4task\\\",\\n    \\\"sparsity_target\\\": 0.3,\\n    \\\"allocation\\\": \\\"uniform\\\",\\n    \\\"gpu\\\": 0,\\n    \\\"multi_gpu\\\": false,\\n    \\\"seq_len\\\": 2048,\\n    \\\"calibration_samples\\\": 32,\\n    \\\"batch_size\\\": 8,\\n    \\\"bottleneck_size\\\": 128,\\n    \\\"svd_rank\\\": 256,\\n    \\\"max_eval_samples\\\": null\\n  },\\n  \\\"mode\\\": {\\n    \\\"mode\\\": \\\"baseline_teal_vanilla\\\",\\n    \\\"sparsity_target\\\": 0.3,\\n    \\\"allocation\\\": \\\"uniform\\\"\\n  },\\n  \\\"metrics\\\": {\\n    \\\"wikitext2_ppl\\\": 8.0054,\\n    \\\"lm_eval\\\": {\\n      \\\"arc_challenge\\\": {\\n        \\\"sample_len\\\": 1172,\\n        \\\"acc\\\": 0.5128,\\n        \\\"acc_stderr\\\": 0.014606603181012609,\\n        \\\"acc_norm\\\": 0.5529,\\n        \\\"acc_norm_stderr\\\": 0.01452938016052677\\n      },\\n      \\\"winogrande\\\": {\\n        \\\"sample_len\\\": 1267,\\n        \\\"acc\\\": 0.6985,\\n        \\\"acc_stderr\\\": 0.01289762807254676\\n      },\\n      \\\"mmlu\\\": {\\n        \\\"sample_len\\\": 14042,\\n        \\\"acc\\\": 0.6634,\\n        \\\"acc_stderr\\\": 0.0037714668883685686\\n      }\\n    },\\n    \\\"lm_eval_raw\\\": {\\n      \\\"arc_challenge\\\": {\\n        \\\"name\\\": \\\"arc_challenge\\\",\\n        \\\"alias\\\": \\\"arc_challenge\\\",\\n        \\\"sample_len\\\": 1172,\\n        \\\"acc,none\\\": 0.5127986348122867,\\n        \\\"acc_stderr,none\\\": 0.014606603181012609,\\n        \\\"acc_norm,none\\\": 0.55290
…[truncated 861 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_check_14b_uniform_results_20260518T013405",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-18T01:34:48.298730+00:00_

两个实验均已完成。结果汇总：

## 14B Uniform Allocation 4-Task Eval Results

| Metric | KL-Predictor (ours) | TEAL Vanilla (baseline) | Delta |
|--------|---------------------|------------------------|-------|
| **WikiText2 PPL** | **7.63** | 8.01 | -0.37 (better) |
| **MMLU** | 0.6449 | **0.6634** | -1.85pp (worse) |
| ARC-C (acc_norm) | 0.5444 | **0.5529** | -0.85pp |
| WinoGrande | **0.7245** | 0.6985 | +2.60pp (better) |

**关键发现**: MMLU 64.49% vs baseline 66.34%，KL predictor 在 uniform allocation 下 MMLU 仍然落后 ~1.9pp。这与之前 learned allocation 的结果一致：KL 目标在 14B 上的 MMLU gap 是 intrinsic 的，不是 allocation 策略导致的。

PPL 方面 KL predictor 更优 (7.63 vs 8.01)，WinoGrande 也更优，但 MMLU 和 ARC-C 均略低于 TEAL vanilla baseline。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_ssh_check_14b_uniform_results_20260518T013405"
}
```

</details>

---
