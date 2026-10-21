# analysis c4 ood eval results

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_analysis_c4-ood-eval-results_20260516T210158.jsonl`
- **Structured JSON:** [`4b3b362527f95ce94175.json`](../../sessions/4b/4b3b362527f95ce94175.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-16T21:02:39.994998+00:00_

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
  "session": "worker_analysis_c4-ood-eval-results_20260516T210158",
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

_source line 2 · 2026-05-16T21:02:39.995463+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_c4-ood-eval-results_20260516T210158",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T21:02:39.995719+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34887",
  "command": "find /root/distill_sparse_swiglu/ -name \"*c4*\" -o -name \"*ood*\" -mtime -1 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_c4-ood-eval-results_20260516T210158",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34887",
    "command": "find /root/distill_sparse_swiglu/ -name \"*c4*\" -o -name \"*ood*\" -mtime -1 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T21:02:39.995958+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_c4-ood-eval-results_20260516T210158",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T21:02:39.996206+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34887",
  "command": "ls -lt /root/distill_sparse_swiglu/results/ 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_c4-ood-eval-results_20260516T210158",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34887",
    "command": "ls -lt /root/distill_sparse_swiglu/results/ 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T21:02:39.996432+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_c4-ood-eval-results_20260516T210158",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T21:02:39.996670+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34887",
  "command": "find /root/distill_sparse_swiglu/ -name \"*c4*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_c4-ood-eval-results_20260516T210158",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34887",
    "command": "find /root/distill_sparse_swiglu/ -name \"*c4*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-16T21:02:39.996890+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34887",
  "command": "find /root/distill_sparse_swiglu/ -name \"*ood*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_c4-ood-eval-results_20260516T210158",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34887",
    "command": "find /root/distill_sparse_swiglu/ -name \"*ood*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-16T21:02:39.997156+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/distill_sparse_swiglu/src/eval_c4_ood.py\\n/root/distill_sparse_swiglu/results/c4_ood_ppl.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.57}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_c4-ood-eval-results_20260516T210158",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-16T21:02:39.997373+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34887",
  "command": "ls -lt /root/distill_sparse_swiglu/results/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_c4-ood-eval-results_20260516T210158",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34887",
    "command": "ls -lt /root/distill_sparse_swiglu/results/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-16T21:02:39.997597+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/distill_sparse_swiglu/src/eval_c4_ood.py\\n/root/distill_sparse_swiglu/results/c4_ood_ppl.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.49}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_c4-ood-eval-results_20260516T210158",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T21:02:39.997863+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 788\\ndrwxr-xr-x 34 root root   4096 May 17 04:42 benchmark\\n-rw-r--r--  1 root root    191 May 17 03:14 c4_ood_ppl.json\\ndrwxr-xr-x  2 root root     58 May 16 12:05 lm_eval_mistral_kl_50pct\\ndrwxr-xr-x  2 root root     58 May 16 11:51 uniform_30pct_dryrun\\ndrwxr-xr-x  2 root root     58 May 16 11:24 lm_eval_teal_30pct\\ndrwxr-xr-x  2 root root     58 May 16 10:45 lm_eval_kl_30pct\\ndrwxr-xr-x  2 root root     58 May 16 10:29 lm_eval_teal_50pct\\ndrwxr-xr-x  2 root root     58 May 16 09:01 lm_eval_kl_s42\\ndrwxr-xr-x  2 root root     91 May 16 08:47 plan_009_mistral\\ndrwxr-xr-x 10 root root   4096 May 16 07:53 plan_007\\ndrwxr-xr-x  2 root root     58 May 16 07:51 dryrun\\ndrwxr-xr-x  2 root root     91 May 16 07:33 lm_eval\\n-rw-r--r--  1 root root 601731 May 16 07:33 lm_eval_dense_final.log\\n-rw-r--r--  1 root root   2192 May 16 06:57 plan_007_all_ppl_fixed.json\\n-rw-r--r--  1 root root     80 May 16 06:55 plan_007_sparsity70.json\\n-rw-r--r--  1 root root    130 May 16 06:49 plan_007_fixed_remaining.json\\n-rw-r--r--  1 root root  33205 May 16 06:47 lm_eval_dense_gpu1.log\\n-rw-r--r--  1 root root   2453 May 16 06:45 lm_eval_dense_v3.log\\ndrwxr-xr-x  2 root root     10 May 16 06:44 plan_007_fixed_p4\\ndrwxr-xr-x  2 root root     91 May 16 06:44 plan_007_fixed_p3\\n-rw-r--r--  1 root root   2427 May 16 06:44 lm_eval_dense_v2.log\\n-rw-r--r--  1 root root  37030 May 16 06:42 lm_eval_dense.log\\ndrwxr-xr-x  2 root root     91 May 16 06:42 plan_007_fixed_p2\\n-rw-r--r--  1 root root  33647 May 16 06:37 lm_eval_full.log\\ndrwxr-xr-x  2 root root     91 May 16 06:35 plan_007_fixed\\n-rw-r--r--  1 root root  46711 May 16 06:33 lm_eval_dense_test.log\\ndrwxr-xr-x  2 root root    129 May 16 06:03 plan_006_reeval\\n-rw-r--r--  1 root root   4902 May 16 04:38 cuda1_diagnosis_report.txt\\ndrwxr-xr-x  2 root root     46 May 16 04:20 subsumption_test\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": nu
…[truncated 47 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_c4-ood-eval-results_20260516T210158",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T21:02:39.998171+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34887",
  "command": "cat /root/distill_sparse_swiglu/results/c4_ood_ppl.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_c4-ood-eval-results_20260516T210158",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34887",
    "command": "cat /root/distill_sparse_swiglu/results/c4_ood_ppl.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-16T21:02:39.998399+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34887",
  "command": "cat /root/distill_sparse_swiglu/src/eval_c4_ood.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_c4-ood-eval-results_20260516T210158",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34887",
    "command": "cat /root/distill_sparse_swiglu/src/eval_c4_ood.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-16T21:02:39.998636+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"dense\\\": {\\n    \\\"ppl\\\": 9.2075,\\n    \\\"time_s\\\": 14.6\\n  },\\n  \\\"kl_predictor_50\\\": {\\n    \\\"ppl\\\": 18.401,\\n    \\\"time_s\\\": 15.4\\n  },\\n  \\\"teal_vanilla_50\\\": {\\n    \\\"ppl\\\": 38.7503,\\n    \\\"time_s\\\": 14.5\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_c4-ood-eval-results_20260516T210158",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T21:02:39.999065+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"C4 OOD PPL evaluation: dense vs KL-predictor-sparse vs vanilla-TEAL at 50% sparsity.\\\"\\\"\\\"\\nimport os, sys, time, json\\nimport torch\\nimport torch.nn.functional as F\\n\\nos.environ[\\\"HF_HOME\\\"] = \\\"/root/autodl-tmp/.hf_cache\\\"\\nos.environ[\\\"HF_DATASETS_OFFLINE\\\"] = \\\"1\\\"\\nos.environ[\\\"TRANSFORMERS_OFFLINE\\\"] = \\\"1\\\"\\nos.environ[\\\"WANDB_MODE\\\"] = \\\"offline\\\"\\n\\nsys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))\\nfrom data_utils import get_eval_dataset\\nfrom predictor import PredictorWrapper\\nfrom evaluate import vanilla_teal_global_masks, _collect_swiglu_magnitudes, evaluate_perplexity, evaluate_true_dense\\n\\nimport importlib.util\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\\n\\n\\ndef _best_attn():\\n    if importlib.util.find_spec(\\\"flash_attn\\\"):\\n        return \\\"flash_attention_2\\\"\\n    return \\\"sdpa\\\"\\n\\n\\n@torch.no_grad()\\ndef compute_ppl_predictor_dynamic(wrapper, dataset, device):\\n    \\\"\\\"\\\"PPL with per-token dynamic predictor masks (actual inference mode).\\\"\\\"\\\"\\n    wrapper.sparse_mode = True\\n    wrapper.gumbel_mask.hard = True\\n    total_loss = 0.0\\n    total_tokens = 0\\n    for sample in dataset:\\n        ids = sample[\\\"input_ids\\\"].unsqueeze(0).to(device)\\n        labels = sample[\\\"labels\\\"].unsqueeze(0).to(device)\\n        out = wrapper.forward_sparse(ids)\\n        logits = out.logits\\n        loss = F.cross_entropy(logits.view(-1, logits.size(-1)), labels.view(-1), reduction=\\\"sum\\\")\\n        total_loss += loss.item()\\n        total_tokens += labels.numel()\\n    return torch.exp(torch.tensor(total_loss / total_tokens)).item()\\n\\n\\ndef main():\\n    device = torch.device(\\\"cuda:0\\\")\\n    MODEL_PATH = \\\"/root/autodl-tmp/models/llama-3.1-8b\\\"\\n    CKPT_PATH = \\\"/root/distill_sparse_swiglu/checkpoints/mvp_kl_norm_v2_s42/predictor_kl_no
…[truncated 4654 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_c4-ood-eval-results_20260516T210158",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-16T21:02:39.999411+00:00_

## C4 OOD Evaluation 结果

### 结果 (`c4_ood_ppl.json`)

| Condition | C4 PPL | Δ vs Dense |
|-----------|--------|------------|
| Dense (LLaMA-3.1-8B) | **9.2075** | baseline |
| KL Predictor 50% | **18.401** | +99.8% |
| TEAL Vanilla 50% | **38.7503** | +320.9% |

**KL advantage over TEAL: 52.5% lower PPL**

### 评估配置

- **Checkpoint**: `/root/distill_sparse_swiglu/checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt`
- **Sparsity**: 50% (global)
- **Model**: LLaMA-3.1-8B (bf16, flash_attention_2)
- **Eval data**: C4 validation, 200 samples × 2048 tokens
- **Predictor**: dynamic per-token Gumbel mask, `d_b=128`, hard=True
- **TEAL calibration**: 32 samples from C4 itself (fair OOD comparison)
- **Eval mode**: KL=dynamic per-token; TEAL=static global magnitude mask

### 与 WikiText-2 对比

| | WikiText-2 | C4 (OOD) | 差距 |
|---|---|---|---|
| Dense | ~7.97 | 9.21 | +15.5% |
| KL Predictor 50% | 11.79 | 18.40 | +56.1% |
| TEAL 50% | ~23.x | 38.75 | ~+60% |

KL predictor 在 OOD 上降幅更大（PPL 从 11.79 → 18.40），但仍大幅优于 TEAL（18.4 vs 38.8），OOD 泛化优势保持。可用于回应 C3 concern：predictor 不是过拟合训练域，在 C4 上仍保持 2.1x advantage over TEAL。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_c4-ood-eval-results_20260516T210158"
}
```

</details>

---
