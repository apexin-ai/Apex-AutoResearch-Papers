# exp bootstrap ci size controlled

**Transformer Model EAP-IG** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 75
- **Recorded user turns:** 0
- **Tool calls:** 37
- **Original source:** `logs/chats/worker_exp_bootstrap_ci_size_controlled_20260513T160804.jsonl`
- **Structured JSON:** [`3e36584d9f9d412a82e0.json`](../../sessions/3e/3e36584d9f9d412a82e0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

75 recorded events

### Tool call

_source line 1 · 2026-05-13T16:13:04.346906+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__detect_image",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__detect_image",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-13T16:13:04.347219+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-13T16:13:04.347392+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "head -200 /root/min_necessary_circuit_css/ioi_size_controlled_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "head -200 /root/min_necessary_circuit_css/ioi_size_controlled_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-13T16:13:04.347625+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"N\\\": 16,\\n  \\\"css_10_edges\\\": [\\n    \\\"a0.h1->a9.h9.v\\\",\\n    \\\"a10.h0->logits\\\",\\n    \\\"a10.h10->logits\\\",\\n    \\\"a10.h6->logits\\\",\\n    \\\"a10.h7->logits\\\",\\n    \\\"a9.h6->logits\\\",\\n    \\\"a9.h9->a10.h7.q\\\",\\n    \\\"a9.h9->logits\\\",\\n    \\\"input->a0.h1.v\\\",\\n    \\\"input->m0\\\",\\n    \\\"m0->a10.h7.k\\\",\\n    \\\"m0->a9.h6.v\\\",\\n    \\\"m0->a9.h9.v\\\",\\n    \\\"m4->a9.h9.v\\\",\\n    \\\"m5->a9.h9.v\\\",\\n    \\\"m6->a9.h9.v\\\"\\n  ],\\n  \\\"binarization\\\": {\\n    \\\"acdc\\\": \\\"isinf\\\",\\n    \\\"eap_ig\\\": \\\"top-100\\\",\\n    \\\"ep\\\": \\\"top-100\\\"\\n  },\\n  \\\"results\\\": {\\n    \\\"CSS=1.0\\\": {\\n      \\\"num_edges\\\": 16,\\n      \\\"zero\\\": {\\n        \\\"num_edges\\\": 16,\\n        \\\"cpr\\\": 0.0295,\\n        \\\"cmd\\\": 0.9929\\n      },\\n      \\\"mean\\\": {\\n        \\\"num_edges\\\": 16,\\n        \\\"cpr\\\": 0.177,\\n        \\\"cmd\\\": 0.842\\n      }\\n    },\\n    \\\"EAP-IG top-N\\\": {\\n      \\\"num_edges\\\": 16,\\n      \\\"zero\\\": {\\n        \\\"num_edges\\\": 16,\\n        \\\"cpr\\\": -0.0585,\\n        \\\"cmd\\\": 1.0829\\n      },\\n      \\\"mean\\\": {\\n        \\\"num_edges\\\": 16,\\n        \\\"cpr\\\": 0.182,\\n        \\\"cmd\\\": 0.8369\\n      }\\n    },\\n    \\\"EP top-N\\\": {\\n      \\\"num_edges\\\": 16,\\n      \\\"zero\\\": {\\n        \\\"num_edges\\\": 16,\\n        \\\"cpr\\\": -0.0091,\\n        \\\"cmd\\\": 1.0323\\n      },\\n      \\\"mean\\\": {\\n        \\\"num_edges\\\": 16,\\n        \\\"cpr\\\": 0.1832,\\n        \\\"cmd\\\": 0.8356\\n      }\\n    },\\n    \\\"ACDC top-N\\\": {\\n      \\\"num_edges\\\": 16,\\n      \\\"zero\\\": {\\n        \\\"num_edges\\\": 16,\\n        \\\"cpr\\\": 0.0295,\\n        \\\"cmd\\\": 0.9929\\n      },\\n      \\\"mean\\\": {\\n        \\\"num_edges\\\": 16,\\n        \\\"cpr\\\": 0.177,\\n        \\\"cmd\\
…[truncated 3473 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-13T16:13:04.347880+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "wc -l /root/min_necessary_circuit_css/ioi_size_controlled_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "wc -l /root/min_necessary_circuit_css/ioi_size_controlled_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-13T16:13:04.348036+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"407 /root/min_necessary_circuit_css/ioi_size_controlled_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-13T16:13:04.348164+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "find /root/min_necessary_circuit_css -name \"*.json\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "find /root/min_necessary_circuit_css -name \"*.json\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-13T16:13:04.348298+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/min_necessary_circuit_css/cache_eap_ig_sva.json\\n/root/min_necessary_circuit_css/cache/Qwen_Qwen2.5_0.5B/ioi/cache_eap_ig.json\\n/root/min_necessary_circuit_css/cache/Qwen_Qwen2.5_0.5B/ioi/cache_edge_pruning.json\\n/root/min_necessary_circuit_css/cache/Qwen_Qwen2.5_0.5B/ioi/cache_ifr.json\\n/root/min_necessary_circuit_css/cache/Qwen_Qwen2.5_0.5B/ioi_acdc/cache_eap_ig.json\\n/root/min_necessary_circuit_css/cache/Qwen_Qwen2.5_0.5B/ioi_acdc/cache_edge_pruning.json\\n/root/min_necessary_circuit_css/cache/Qwen_Qwen2.5_0.5B/ioi_acdc/cache_acdc.json\\n/root/min_necessary_circuit_css/results/Qwen_Qwen2.5_0.5B_ioi/Qwen_Qwen2.5_0.5B_ioi_K3.json\\n/root/min_necessary_circuit_css/results/Qwen_Qwen2.5_0.5B_ioi/proportional_binarize_ablation.json\\n/root/min_necessary_circuit_css/results/Qwen_Qwen2.5_0.5B_ioi_acdc/Qwen_Qwen2.5_0.5B_ioi_acdc_K3.json\\n/root/min_necessary_circuit_css/cache_ep_sva.json\\n/root/min_necessary_circuit_css/cache_acdc_sva.json\\n/root/min_necessary_circuit_css/sva_results.json\\n/root/min_necessary_circuit_css/sva_css067_fix_results.json\\n/root/min_necessary_circuit_css/cache_eap_ig_fr.json\\n/root/min_necessary_circuit_css/cache_ep_fr.json\\n/root/min_necessary_circuit_css/cache_acdc_fr.json\\n/root/min_necessary_circuit_css/factual_recall_results.json\\n/root/min_necessary_circuit_css/cache_eap_ig.json\\n/root/min_necessary_circuit_css/cache_edge_pruning.json\\n/root/min_necessary_circuit_css/bootstrap_ci_results.json\\n/root/min_necessary_circuit_css/cache_acdc.json\\n/root/min_necessary_circuit_css/ioi_size_controlled_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-13T16:13:04.348426+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "grep -r \"per_prompt\\|per-prompt\\|prompt_cprs\\|cpr_values\\|cpr_list\" /root/min_necessary_circuit_css/ --include=\"*.py\" -l",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "grep -r \"per_prompt\\|per-prompt\\|prompt_cprs\\|cpr_values\\|cpr_list\" /root/min_necessary_circuit_css/ --include=\"*.py\" -l",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-13T16:13:04.348544+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-13T16:13:04.348683+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "find /root/min_necessary_circuit_css -name \"*.py\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "find /root/min_necessary_circuit_css -name \"*.py\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-13T16:13:04.348894+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/min_necessary_circuit_css/acdc_topk_sweep.py\\n/root/min_necessary_circuit_css/analysis_fix_v3.py\\n/root/min_necessary_circuit_css/circuit_discovery.py\\n/root/min_necessary_circuit_css/circus.py\\n/root/min_necessary_circuit_css/config.py\\n/root/min_necessary_circuit_css/cross_tabulate.py\\n/root/min_necessary_circuit_css/css.py\\n/root/min_necessary_circuit_css/edge_pruning_l0.py\\n/root/min_necessary_circuit_css/eval_faithfulness.py\\n/root/min_necessary_circuit_css/eval_mean_ablation.py\\n/root/min_necessary_circuit_css/eval_topk_faithfulness.py\\n/root/min_necessary_circuit_css/evaluation.py\\n/root/min_necessary_circuit_css/ifr_discovery.py\\n/root/min_necessary_circuit_css/ifr_scoring.py\\n/root/min_necessary_circuit_css/run_arithmetic.py\\n/root/min_necessary_circuit_css/run_circus.py\\n/root/min_necessary_circuit_css/run_circus_fix.py\\n/root/min_necessary_circuit_css/run_mvp.py\\n/root/min_necessary_circuit_css/run_phase2_experiment.py\\n/root/min_necessary_circuit_css/run_phase_d_only.py\\n/root/min_necessary_circuit_css/run_sva.py\\n/root/min_necessary_circuit_css/run_sva_cuda1.py\\n/root/min_necessary_circuit_css/e2e_validate.py\\n/root/min_necessary_circuit_css/run_qwen_ioi.py\\n/root/min_necessary_circuit_css/diagnose_ifr_perhead.py\\n/root/min_necessary_circuit_css/diagnose_proportional_binarize.py\\n/root/min_necessary_circuit_css/fix_css067_eval.py\\n/root/min_necessary_circuit_css/run_factual_recall.py\\n/root/min_necessary_circuit_css/run_qwen_ioi_acdc.py\\n/root/min_necessary_circuit_css/run_size_controlled_ioi.py\\n/root/min_necessary_circuit_css/run_bootstrap_ci.py\\n/root/min_necessary_circuit_css/_gen_arith_caches.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-13T16:13:04.349031+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "cat /root/min_necessary_circuit_css/bootstrap_ci_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "cat /root/min_necessary_circuit_css/bootstrap_ci_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-13T16:13:04.349175+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"ioi\\\": {\\n    \\\"task\\\": \\\"ioi\\\",\\n    \\\"ablation\\\": \\\"zero\\\",\\n    \\\"n_prompts\\\": 100,\\n    \\\"css_10\\\": {\\n      \\\"num_edges\\\": 16,\\n      \\\"cpr\\\": 0.02947526052594185\\n    },\\n    \\\"best_single\\\": {\\n      \\\"method\\\": \\\"edge_pruning\\\",\\n      \\\"num_edges\\\": 100,\\n      \\\"cpr\\\": 0.08292677253484726\\n    },\\n    \\\"all_methods\\\": {\\n      \\\"eap_ig\\\": {\\n        \\\"edges\\\": 100,\\n        \\\"cpr\\\": -0.10921436548233032\\n      },\\n      \\\"edge_pruning\\\": {\\n        \\\"edges\\\": 100,\\n        \\\"cpr\\\": 0.08292677253484726\\n      },\\n      \\\"acdc\\\": {\\n        \\\"edges\\\": 16,\\n        \\\"cpr\\\": 0.02947526052594185\\n      }\\n    },\\n    \\\"delta\\\": -0.05345151200890541,\\n    \\\"bootstrap\\\": {\\n      \\\"observed_delta\\\": -0.05345151200890541,\\n      \\\"bootstrap_mean\\\": -0.0424281507730484,\\n      \\\"bootstrap_std\\\": 0.1454060971736908,\\n      \\\"ci_lo\\\": -0.29016661643981934,\\n      \\\"ci_hi\\\": 0.2586621046066284,\\n      \\\"p_value\\\": 0.342,\\n      \\\"n_valid\\\": 1000\\n    },\\n    \\\"significant\\\": false\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.47}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-13T16:13:04.349362+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "cat /root/min_necessary_circuit_css/run_bootstrap_ci.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "cat /root/min_necessary_circuit_css/run_bootstrap_ci.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-13T16:13:04.349641+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Bootstrap confidence intervals for CSS=1.0 CPR advantage.\\n\\nFor each task, computes the 95% CI for:\\n  delta = CPR(CSS=1.0) - CPR(best_single_method)\\n\\nMethod: prompt-level resampling with replacement.\\nCircuit edges are fixed; only which prompts contribute to CPR changes.\\n\\nUsage:\\n  # Dry-run (SVA, 5 bootstrap, CPU)\\n  python run_bootstrap_ci.py --dry-run --device cpu\\n\\n  # Full run (all tasks, 1000 bootstrap, GPU)\\n  CUDA_VISIBLE_DEVICES=1 python run_bootstrap_ci.py --device cuda\\n\\\"\\\"\\\"\\n\\nimport os\\nos.environ.setdefault(\\\"CUDA_VISIBLE_DEVICES\\\", \\\"1\\\")\\n\\nimport json\\nimport math\\nimport random\\nimport re\\nimport gc\\nimport argparse\\nimport sys\\nfrom pathlib import Path\\nfrom functools import partial\\n\\nimport torch\\nimport numpy as np\\n\\n# ── Constants ──────────────────────────────────────────────────────────\\nLOCAL_GPT2 = \\\"/root/autodl-tmp/gpt2-small\\\"\\nGPT2_ALIASES = (\\\"gpt2\\\", \\\"gpt2-small\\\", \\\"openai-community/gpt2\\\")\\nCACHE_DIR = Path(\\\"/root/min_necessary_circuit_css\\\")\\nGT_DATASET_PATH = \\\"/root/miniconda3/lib/python3.12/site-packages/datasets/greaterthan_gpt2-small_prompts.json\\\"\\nFR_DATASET_PATH = \\\"/root/miniconda3/lib/python3.12/site-packages/datasets/factual_recall_gpt2-small_prompts.json\\\"\\n\\n\\n# ── HF patching ────────────────────────────────────────────────────────\\ndef patch_hf():\\n    from transformers import AutoConfig, AutoTokenizer, AutoModelForCausalLM\\n    def _make_patched(orig_fn):\\n        def patched(name_or_path, *args, **kwargs):\\n            if name_or_path in GPT2_ALIASES:\\n                name_or_path = LOCAL_GPT2\\n            return orig_fn(name_or_path, *args, **kwargs)\\n        return patched\\n    AutoConfig.from_pretrained = staticmethod(_make_patched(AutoConfig.from_pretrained))\\n    AutoTokenizer.from_pretrained = staticmethod(_make_pa
…[truncated 7592 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-13T16:13:04.349857+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "cat /root/min_necessary_circuit_css/run_size_controlled_ioi.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "cat /root/min_necessary_circuit_css/run_size_controlled_ioi.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-13T16:13:04.350154+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"import os\\nos.environ[\\\"CUDA_VISIBLE_DEVICES\\\"] = \\\"0\\\"\\n\\nimport json, math, random, re, gc, sys\\nfrom pathlib import Path\\nfrom functools import partial\\n\\nimport torch\\nimport numpy as np\\n\\nsys.path.insert(0, \\\"/root/min_necessary_circuit_css\\\")\\n\\n_LOCAL_GPT2 = \\\"/root/autodl-tmp/gpt2-small\\\"\\n_GPT2_ALIASES = (\\\"gpt2\\\", \\\"gpt2-small\\\", \\\"openai-community/gpt2\\\")\\n\\ndef _patch_hf():\\n    from transformers import AutoConfig, AutoTokenizer, AutoModelForCausalLM\\n    def _make_patched(orig_fn):\\n        def patched(name_or_path, *args, **kwargs):\\n            if name_or_path in _GPT2_ALIASES:\\n                name_or_path = _LOCAL_GPT2\\n            return orig_fn(name_or_path, *args, **kwargs)\\n        return patched\\n    AutoConfig.from_pretrained = staticmethod(_make_patched(AutoConfig.from_pretrained))\\n    AutoTokenizer.from_pretrained = staticmethod(_make_patched(AutoTokenizer.from_pretrained))\\n    AutoModelForCausalLM.from_pretrained = staticmethod(_make_patched(AutoModelForCausalLM.from_pretrained))\\n\\n_patch_hf()\\n\\nNAMES = [\\\"John\\\", \\\"Mary\\\", \\\"Alice\\\", \\\"Bob\\\", \\\"Charlie\\\", \\\"David\\\", \\\"Emma\\\", \\\"Frank\\\",\\n         \\\"Grace\\\", \\\"Henry\\\", \\\"Jack\\\", \\\"Kate\\\", \\\"Leo\\\", \\\"Mia\\\", \\\"Noah\\\", \\\"Tom\\\"]\\nTEMPLATES = [\\n    \\\"When {io} and {s} went to the {place}, {s} gave a {obj} to\\\",\\n    \\\"After {io} and {s} arrived at the {place}, {s} handed a {obj} to\\\",\\n    \\\"{io} and {s} were at the {place}. {s} gave a {obj} to\\\",\\n    \\\"Then, {io} and {s} had a meeting at the {place}, {s} passed a {obj} to\\\",\\n]\\nPLACES = [\\\"store\\\", \\\"park\\\", \\\"library\\\", \\\"school\\\", \\\"hospital\\\", \\\"restaurant\\\", \\\"office\\\"]\\nOBJECTS = [\\\"bottle\\\", \\\"book\\\", \\\"letter\\\", \\\"ball\\\", \\\"gift\\\", \\\"toy\\\", \\\"bag\\\"]\\n\\nCACHE_DIR = Path(\\\"/
…[truncated 7506 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-13T16:13:04.350359+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "grep -n \"def evaluate_circuit\\|def run_with_ablation\\|def bootstrap_delta_ci\" /root/min_necessary_circuit_css/run_size_controlled_ioi.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "grep -n \"def evaluate_circuit\\|def run_with_ablation\\|def bootstrap_delta_ci\" /root/min_necessary_circuit_css/run_size_controlled_ioi.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-13T16:13:04.350495+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-13T16:13:04.350619+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "grep -n \"def evaluate_circuit\\|def run_with_ablation\\|def bootstrap_delta_ci\" /root/min_necessary_circuit_css/run_bootstrap_ci.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "grep -n \"def evaluate_circuit\\|def run_with_ablation\\|def bootstrap_delta_ci\" /root/min_necessary_circuit_css/run_bootstrap_ci.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-13T16:13:04.350762+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-13T16:13:04.350891+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "grep -n \"def evaluate_circuit\\|def run_with_ablation\\|def bootstrap_delta_ci\" /root/min_necessary_circuit_css/run_size_controlled_ioi.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "grep -n \"def evaluate_circuit\\|def run_with_ablation\\|def bootstrap_delta_ci\" /root/min_necessary_circuit_css/run_size_controlled_ioi.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-13T16:13:04.351011+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-13T16:13:04.351126+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "grep -n \"def evaluate_circuit\\|def run_with_ablation\\|def bootstrap_delta_ci\" /root/min_necessary_circuit_css/run_bootstrap_ci.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "grep -n \"def evaluate_circuit\\|def run_with_ablation\\|def bootstrap_delta_ci\" /root/min_necessary_circuit_css/run_bootstrap_ci.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-13T16:13:04.351239+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-13T16:13:04.351364+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "grep -n \"def evaluate_circuit\" /root/min_necessary_circuit_css/run_size_controlled_ioi.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "grep -n \"def evaluate_circuit\" /root/min_necessary_circuit_css/run_size_controlled_ioi.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-13T16:13:04.351483+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"118:def evaluate_circuit(model, circuit_edges, tokens, metric_fn,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-13T16:13:04.351597+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "grep -n \"def run_with_ablation\" /root/min_necessary_circuit_css/run_size_controlled_ioi.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "grep -n \"def run_with_ablation\" /root/min_necessary_circuit_css/run_size_controlled_ioi.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-13T16:13:04.351729+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-13T16:13:04.351847+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "grep -n \"def bootstrap_delta_ci\" /root/min_necessary_circuit_css/run_bootstrap_ci.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "grep -n \"def bootstrap_delta_ci\" /root/min_necessary_circuit_css/run_bootstrap_ci.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-13T16:13:04.351969+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"381:def bootstrap_delta_ci(css_diffs, best_diffs, baseline_diffs,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-13T16:13:04.352094+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "head -180 /root/min_necessary_circuit_css/run_size_controlled_ioi.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "head -180 /root/min_necessary_circuit_css/run_size_controlled_ioi.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-13T16:13:04.352286+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"import os\\nos.environ[\\\"CUDA_VISIBLE_DEVICES\\\"] = \\\"0\\\"\\n\\nimport json, math, random, re, gc, sys\\nfrom pathlib import Path\\nfrom functools import partial\\n\\nimport torch\\nimport numpy as np\\n\\nsys.path.insert(0, \\\"/root/min_necessary_circuit_css\\\")\\n\\n_LOCAL_GPT2 = \\\"/root/autodl-tmp/gpt2-small\\\"\\n_GPT2_ALIASES = (\\\"gpt2\\\", \\\"gpt2-small\\\", \\\"openai-community/gpt2\\\")\\n\\ndef _patch_hf():\\n    from transformers import AutoConfig, AutoTokenizer, AutoModelForCausalLM\\n    def _make_patched(orig_fn):\\n        def patched(name_or_path, *args, **kwargs):\\n            if name_or_path in _GPT2_ALIASES:\\n                name_or_path = _LOCAL_GPT2\\n            return orig_fn(name_or_path, *args, **kwargs)\\n        return patched\\n    AutoConfig.from_pretrained = staticmethod(_make_patched(AutoConfig.from_pretrained))\\n    AutoTokenizer.from_pretrained = staticmethod(_make_patched(AutoTokenizer.from_pretrained))\\n    AutoModelForCausalLM.from_pretrained = staticmethod(_make_patched(AutoModelForCausalLM.from_pretrained))\\n\\n_patch_hf()\\n\\nNAMES = [\\\"John\\\", \\\"Mary\\\", \\\"Alice\\\", \\\"Bob\\\", \\\"Charlie\\\", \\\"David\\\", \\\"Emma\\\", \\\"Frank\\\",\\n         \\\"Grace\\\", \\\"Henry\\\", \\\"Jack\\\", \\\"Kate\\\", \\\"Leo\\\", \\\"Mia\\\", \\\"Noah\\\", \\\"Tom\\\"]\\nTEMPLATES = [\\n    \\\"When {io} and {s} went to the {place}, {s} gave a {obj} to\\\",\\n    \\\"After {io} and {s} arrived at the {place}, {s} handed a {obj} to\\\",\\n    \\\"{io} and {s} were at the {place}. {s} gave a {obj} to\\\",\\n    \\\"Then, {io} and {s} had a meeting at the {place}, {s} passed a {obj} to\\\",\\n]\\nPLACES = [\\\"store\\\", \\\"park\\\", \\\"library\\\", \\\"school\\\", \\\"hospital\\\", \\\"restaurant\\\", \\\"office\\\"]\\nOBJECTS = [\\\"bottle\\\", \\\"book\\\", \\\"letter\\\", \\\"ball\\\", \\\"gift\\\", \\\"toy\\\", \\\"bag\\\"]\\n\\nCACHE_DIR = Path(\\\"/
…[truncated 5897 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-13T16:13:04.352426+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "tail -n +381 /root/min_necessary_circuit_css/run_bootstrap_ci.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "tail -n +381 /root/min_necessary_circuit_css/run_bootstrap_ci.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-13T16:13:04.352722+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"def bootstrap_delta_ci(css_diffs, best_diffs, baseline_diffs,\\n                       n_bootstrap=1000, seed=42):\\n    \\\"\\\"\\\"Bootstrap CI for delta = CPR(CSS=1.0) - CPR(best_single).\\n\\n    CPR = mean(circuit_diffs) / mean(baseline_diffs).\\n    Resamples prompt indices with replacement.\\n    \\\"\\\"\\\"\\n    rng = np.random.RandomState(seed)\\n    n = len(baseline_diffs)\\n    deltas = []\\n\\n    for _ in range(n_bootstrap):\\n        idx = rng.choice(n, n, replace=True)\\n        bl = baseline_diffs[idx].mean()\\n        if abs(bl) < 1e-8:\\n            continue\\n        cpr_css = css_diffs[idx].mean() / bl\\n        cpr_best = best_diffs[idx].mean() / bl\\n        deltas.append(cpr_css - cpr_best)\\n\\n    deltas = np.array(deltas)\\n    lo = np.percentile(deltas, 2.5)\\n    hi = np.percentile(deltas, 97.5)\\n\\n    observed_bl = baseline_diffs.mean()\\n    observed_delta = (css_diffs.mean() / observed_bl - best_diffs.mean() / observed_bl\\n                      if abs(observed_bl) > 1e-8 else 0.0)\\n\\n    if observed_delta >= 0:\\n        p_value = float(np.mean(deltas <= 0))\\n    else:\\n        p_value = float(np.mean(deltas >= 0))\\n\\n    return {\\n        \\\"observed_delta\\\": float(observed_delta),\\n        \\\"bootstrap_mean\\\": float(deltas.mean()),\\n        \\\"bootstrap_std\\\": float(deltas.std()),\\n        \\\"ci_lo\\\": float(lo),\\n        \\\"ci_hi\\\": float(hi),\\n        \\\"p_value\\\": p_value,\\n        \\\"n_valid\\\": len(deltas),\\n    }\\n\\n\\n# ── Task configurations ───────────────────────────────────────────────\\nTASK_CONFIGS = {\\n    \\\"ioi\\\": {\\n        \\\"caches\\\": {\\n            \\\"eap_ig\\\": \\\"cache_eap_ig.json\\\",\\n            \\\"edge_pruning\\\": \\\"cache_edge_pruning.json\\\",\\n            \\\"acdc\\\": \\\"cache_acdc.json\\\",\\n        },\\n        \\\"binarize\\\": {\\n            \\\"eap_ig\\\": \\\"topk-100\\\",\\n         
…[truncated 7672 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-13T16:13:04.352909+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "tail -n +170 /root/min_necessary_circuit_css/run_size_controlled_ioi.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "tail -n +170 /root/min_necessary_circuit_css/run_size_controlled_ioi.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-13T16:13:04.353175+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"            if ablation_mode == \\\"zero\\\":\\n                hooks.append((f\\\"blocks.{layer}.attn.hook_result\\\",\\n                              partial(_head_hook, heads_to_ablate=heads)))\\n            else:\\n                hooks.append((f\\\"blocks.{layer}.attn.hook_result\\\",\\n                              partial(_head_hook, heads_to_ablate=heads, layer_idx=layer)))\\n        for layer in ablate_mlps:\\n            if ablation_mode == \\\"zero\\\":\\n                hooks.append((f\\\"blocks.{layer}.hook_mlp_out\\\", _mlp_hook))\\n            else:\\n                hooks.append((f\\\"blocks.{layer}.hook_mlp_out\\\", partial(_mlp_hook, layer_idx=layer)))\\n\\n        circ_logits = model.run_with_hooks(tokens, fwd_hooks=hooks)\\n        circuit_diff = metric_fn(circ_logits, tokens)\\n\\n    cpr = circuit_diff / baseline_diff if abs(baseline_diff) > 1e-6 else 0.0\\n    cmd = abs(baseline_diff - circuit_diff)\\n    return {\\\"num_edges\\\": len(circuit_edges), \\\"cpr\\\": round(cpr, 4), \\\"cmd\\\": round(cmd, 4)}\\n\\n\\ndef topk_edges(scores, k):\\n    sorted_edges = sorted(\\n        scores.items(),\\n        key=lambda x: abs(x[1]) if not math.isinf(x[1]) else float('inf'),\\n        reverse=True\\n    )\\n    return set(e for e, _ in sorted_edges[:k])\\n\\n\\ndef isinf_edges(scores):\\n    return set(e for e, v in scores.items() if math.isinf(v))\\n\\n\\ndef compute_css(methods_edges):\\n    K = len(methods_edges)\\n    union = set()\\n    for edges in methods_edges.values():\\n        union |= edges\\n    return {e: sum(1 for es in methods_edges.values() if e in es) / K for e in union}\\n\\n\\ndef threshold_css(css_scores, threshold):\\n    return {e for e, s in css_scores.items() if s >= threshold - 1e-2}\\n\\n\\ndef run_circuit_discovery():\\n    \\\"\\\"\\\"Run EAP-IG, EP, ACDC and cache results.\\\"\\\"\\\"\\n    from torch.utils.data import DataLoader, Dataset\\n    from config import 
…[truncated 7309 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-13T16:13:04.353392+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "grep -n \"def metric_ioi\" /root/min_necessary_circuit_css/run_size_controlled_ioi.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "grep -n \"def metric_ioi\" /root/min_necessary_circuit_css/run_size_controlled_ioi.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-13T16:13:04.353536+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"370:    def metric_ioi(logits, tokens_arg):\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-13T16:13:04.353656+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "tail -n +370 /root/min_necessary_circuit_css/run_size_controlled_ioi.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "tail -n +370 /root/min_necessary_circuit_css/run_size_controlled_ioi.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-13T16:13:04.353925+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"    def metric_ioi(logits, tokens_arg):\\n        return (logits[range(len(tokens_arg)), -1, io_ids[:len(tokens_arg)]] -\\n                logits[range(len(tokens_arg)), -1, s_ids[:len(tokens_arg)]]).mean().item()\\n\\n    print(\\\"Collecting mean activations...\\\")\\n    attn_means, mlp_means = collect_mean_activations(model, tokens)\\n\\n    circuits_to_eval = {\\n        \\\"CSS=1.0\\\": css_10,\\n        \\\"EAP-IG top-N\\\": eapig_topN,\\n        \\\"EP top-N\\\": ep_topN,\\n        \\\"ACDC top-N\\\": acdc_topN,\\n    }\\n\\n    results = {}\\n    for name, edges in circuits_to_eval.items():\\n        print(f\\\"\\\\nEvaluating: {name} ({len(edges)} edges)\\\")\\n        r_zero = evaluate_circuit(model, edges, tokens, metric_ioi, \\\"zero\\\")\\n        r_mean = evaluate_circuit(model, edges, tokens, metric_ioi, \\\"mean\\\", attn_means, mlp_means)\\n        results[name] = {\\n            \\\"num_edges\\\": len(edges),\\n            \\\"edges\\\": sorted(edges),\\n            \\\"zero\\\": r_zero,\\n            \\\"mean\\\": r_mean,\\n        }\\n        print(f\\\"  zero: CPR={r_zero['cpr']:.4f}, CMD={r_zero['cmd']:.4f}\\\")\\n        print(f\\\"  mean: CPR={r_mean['cpr']:.4f}, CMD={r_mean['cmd']:.4f}\\\")\\n\\n    # Random-N evaluation\\n    print(f\\\"\\\\nEvaluating: Random-{N} (10 samples)\\\")\\n    rand_zero_cprs, rand_zero_cmds = [], []\\n    rand_mean_cprs, rand_mean_cmds = [], []\\n    rand_details = []\\n    for i, edges in enumerate(random_circuits):\\n        r_zero = evaluate_circuit(model, edges, tokens, metric_ioi, \\\"zero\\\")\\n        r_mean = evaluate_circuit(model, edges, tokens, metric_ioi, \\\"mean\\\", attn_means, mlp_means)\\n        rand_zero_cprs.append(r_zero[\\\"cpr\\\"])\\n        rand_zero_cmds.append(r_zero[\\\"cmd\\\"])\\n        rand_mean_cprs.append(r_mean[\\\"cpr\\\"])\\n        rand_mean_cmds.append(r_mean[\\\"cmd\\\"])\\n        rand_details.append({\\\"zero\\\": 
…[truncated 4413 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-13T16:13:04.354099+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "tail -n +300 /root/min_necessary_circuit_css/run_size_controlled_ioi.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "tail -n +300 /root/min_necessary_circuit_css/run_size_controlled_ioi.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-13T16:13:04.354378+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"            gc.collect(); torch.cuda.empty_cache()\\n\\n        if need_acdc:\\n            print(\\\"ACDC: running...\\\")\\n            all_scores[\\\"acdc\\\"] = run_acdc(ac_task, config)\\n            with open(acdc_cache, \\\"w\\\") as f:\\n                json.dump(all_scores[\\\"acdc\\\"], f)\\n            print(f\\\"  ACDC: {len(all_scores['acdc'])} edges, cached\\\")\\n\\n        del ac_task; gc.collect(); torch.cuda.empty_cache()\\n\\n    return all_scores\\n\\n\\ndef main():\\n    device = torch.device(\\\"cuda\\\")\\n    print(f\\\"CUDA_VISIBLE_DEVICES={os.environ.get('CUDA_VISIBLE_DEVICES')}\\\")\\n    print(\\\"=\\\" * 70)\\n    print(\\\"  IOI Size-Controlled Baseline Analysis\\\")\\n    print(\\\"=\\\" * 70)\\n\\n    # Step 1: Get edge scores\\n    print(\\\"\\\\n--- Step 1: Circuit Discovery ---\\\")\\n    all_scores = run_circuit_discovery()\\n\\n    eapig_scores = all_scores[\\\"eap_ig\\\"]\\n    ep_scores = all_scores[\\\"edge_pruning\\\"]\\n    acdc_scores = all_scores[\\\"acdc\\\"]\\n    print(f\\\"Edge scores: EAP-IG={len(eapig_scores)}, EP={len(ep_scores)}, ACDC={len(acdc_scores)}\\\")\\n\\n    # Step 2: Reproduce CSS=1.0 circuit (isinf binarization for ACDC, top-100 for EAP-IG/EP)\\n    print(\\\"\\\\n--- Step 2: CSS=1.0 Circuit ---\\\")\\n    acdc_circuit = isinf_edges(acdc_scores)\\n    eapig_100 = topk_edges(eapig_scores, 100)\\n    ep_100 = topk_edges(ep_scores, 100)\\n    print(f\\\"Binarized: ACDC-isinf={len(acdc_circuit)}, EAP-IG-100={len(eapig_100)}, EP-100={len(ep_100)}\\\")\\n\\n    css_scores = compute_css({\\\"acdc\\\": acdc_circuit, \\\"eap_ig\\\": eapig_100, \\\"ep\\\": ep_100})\\n    css_10 = threshold_css(css_scores, 1.0)\\n    N = len(css_10)\\n    print(f\\\"CSS=1.0 circuit: {N} edges\\\")\\n    print(f\\\"CSS=1.0 edges: {sorted(css_10)}\\\")\\n\\n    # Step 3: Build size-controlled circuits\\n    print(f\\\"\\\\n--- Step 3: Size-Controlled Circuits (N={N}) ---\\\")\\n
…[truncated 7461 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-13T16:13:04.354574+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "ls /root/autodl-tmp/gpt2-small/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "ls /root/autodl-tmp/gpt2-small/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-13T16:13:04.354724+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"config.json\\nconfiguration.json\\ngeneration_config.json\\nmerges.txt\\nmodel.safetensors\\nonnx\\ntokenizer.json\\nvocab.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-13T16:13:04.354852+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "nvidia-smi --query-gpu=name,memory.total --format=csv,noheader",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "nvidia-smi --query-gpu=name,memory.total --format=csv,noheader",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-13T16:13:04.354971+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"NVIDIA RTX PRO 6000 Blackwell Server Edition, 97887 MiB\\nNVIDIA RTX PRO 6000 Blackwell Server Edition, 97887 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.54}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-13T16:13:04.355179+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-39279",
  "command": "cat > /root/min_necessary_circuit_css/run_bootstrap_ci_size_controlled.py << 'PYEOF'\n#!/usr/bin/env python3\n\"\"\"Size-controlled bootstrap CI for CSS=1.0 CPR advantage (IOI task).\n\nRecomputes per-prompt diffs for each method's top-16 circuit, then\nbootstraps delta = CPR(CSS=1.0) - CPR(method) with prompt-level resampling.\n\nInput: cached edge scores (cache_eap_ig.json, cache_edge_pruning.json, cache_acdc.json)\nOutput: /root/min_necessary_circuit_css/bootstrap_ci_size_controlled_results.json\n\"\"\"\n\nimport os\nos.environ.setdefault(\"CUDA_VISIBLE_DEVICES\", \"0\")\n\nimport json, math, random, re, gc\nfrom pathlib import Path\nfrom functools import partial\n\nimport torch\nimport numpy as np\n\n# ── Config ────────────────────────────────────────────────────────────\nLOCAL_GPT2 = \"/root/autodl-tmp/gpt2-small\"\nGPT2_ALIASES = (\"gpt2\", \"gpt2-small\", \"openai-community/gpt2\")\nCACHE_DIR = Path(\"/root/min_necessary_circuit_css\")\nRESULT_PATH = CACHE_DIR / \"bootstrap_ci_size_controlled_results.json\"\nN_BOOTSTRAP = 1000\nSEED = 42\n\nNAMES = [\"John\", \"Mary\", \"Alice\", \"Bob\", \"Charlie\", \"David\", \"Emma\", \"Frank\",\n         \"Grace\", \"Henry\", \"Jack\", \"Kate\", \"Leo\", \"Mia\", \"Noah\", \"Tom\"]\nTEMPLATES = [\n    \"When {io} and {s} went to the {place}, {s} gave a {obj} to\",\n    \"After {io} and {s} arrived at the {place}, {s} handed a {obj} to\",\n    \"{io} and {s} were at the {place}. {s} gave a {obj} to\",\n    \"Then, {io} and {s} had a meeting at the {place}, {s} passed a {obj} to\",\n]\nPLACES = [\"store\", \"park\", \"library\", \"school\", \"hospital\", \"restaurant\", \"office\"]\nOBJECTS = [\"bottle\", \"book\", \"letter\", \"ball\", \"gift\", \"toy\", \"bag\"]\n\n\n# ── HF patching ──────────────────────────────────────────────────────\ndef patch_hf():\n    from transformers import AutoConfig, AutoTokenizer, AutoModelForCausalLM\n    def _make_patched(orig_fn):\n        def patched(name_or_path, *args, **kwargs):\n            if name_or_path in GPT2_ALIASES:\n                name_or_path = LOCAL_GPT2\n            return orig_fn(name_or_path, *args, **kwargs)\n        return patched\n    AutoConfig.from_pretrained = staticmethod(_make_patched(AutoConfig.from_pretrained))\n    AutoTokenizer.from_pretrained = staticmethod(_make_patched(AutoTokenizer.from_pretrained))\n    AutoModelForCausalLM.from_pretrained = staticmethod(_make_patched(AutoModelForCausalLM.from_pretrained))\n\npatch_hf()\n\n\n# ── Model ─────────────────────────────────────────────────────────────\ndef load_model(device=\"cuda\"):\n    from transformer_lens import HookedTransformer\n    from transformers import AutoModelForCausalLM\n    hf_model = AutoModelForCausalLM.from_pretrained(LOCAL_GPT2)\n    model = HookedTransformer.from_pretrained(\"gpt2-small\", hf_model=hf_model, device=device)\n    model.set_use_attn_result(True)\n    model.set_use_split_qkv_input(True)\n    model.set_use_hook_mlp_in(True)\n    return model\n\n\n# ── Data ──────────────────────────────────────────────────────────────\ndef generate_ioi_data(tokenizer, num_samples=100, seed=42):\n    random.seed(seed)\n    prompts, labels = [], []\n    for _ in range(num_samples):\n        io_name, s_name = random.sample(NAMES, 2)\n        template = random.choice(TEMPLATES)\n        place = random.choice(PLACES)\n        obj = random.choice(OBJECTS)\n        prompts.append(template.format(io=io_name, s=s_name, place=place, obj=obj))\n        labels.append((tokenizer.encode(\" \" + io_name)[0],\n                        tokenizer.encode(\" \" + s_name)[0]))\n    return prompts, labels\n\n\n# ── Circuit helpers ───────────────────────────────────────────────────\ndef extract_circuit_nodes(circuit_edges):\n    nodes = set()\n    for edge in circuit_edges:\n        parts = edge.split('->')\n        if len(parts) != 2:\n            continue\n        nodes.add(parts[0].strip())\n        dst_base = re.sub(r'\\.[qkv]$', '', parts[1].strip())\n        nodes.add(dst_base)\n    nodes.discard('input')\n    nodes.discard('logits')\n    return nodes\n\n\ndef topk_edges(scores, k):\n    sorted_edges = sorted(\n        scores.items(),\n        key=lambda x: abs(x[1]) if not math.isinf(x[1]) else float('inf'),\n        reverse=True\n    )\n    return set(e for e, _ in sorted_edges[:k])\n\n\ndef isinf_edges(scores):\n    return set(e for e, v in scores.items() if math.isinf(v))\n\n\ndef compute_css(methods_edges):\n    K = len(methods_edges)\n    union = set()\n    for edges in methods_edges.values():\n        union |= edges\n    return {e: sum(1 for es in methods_edges.values() if e in es) / K for e in union}\n\n\ndef threshold_css(css_scores, threshold):\n    return {e for e, s in css_scores.items() if s >= threshold - 1e-2}\n\n\n# ── Mean activations ─────────────────────────────────────────────────\ndef collect_mean_activations(model, tokens):\n    n_layers = model.cfg.n_layers\n    accumulators = {}\n\n    def make_accumulator(key):\n        def hook_fn(value, hook):\n            if key not in accumulators:\n                accumulators[key] = value.detach().mean(dim=0, keepdim=True).clone()\n            else:\n                accumulators[key] += value.detach().mean(dim=0, keepdim=True)\n            return value\n        return hook_fn\n\n    hooks = []\n    for layer in range(n_layers):\n        hooks.append((f\"blocks.{layer}.attn.hook_result\", make_accumulator(f\"attn_{layer}\")))\n        hooks.append((f\"blocks.{layer}.hook_mlp_out\", make_accumulator(f\"mlp_{layer}\")))\n\n    batch_size = 25\n    n_batches = 0\n    with torch.no_grad():\n        for start in range(0, len(tokens), batch_size):\n            batch = tokens[start:start + batch_size]\n            model.run_with_hooks(batch, fwd_hooks=hooks)\n            n_batches += 1\n\n    attn_means, mlp_means = {}, {}\n    for layer in range(n_layers):\n        attn_means[layer] = accumulators[f\"attn_{layer}\"] / n_batches\n        mlp_means[layer] = accumulators[f\"mlp_{layer}\"] / n_batches\n    return attn_means, mlp_means\n\n\n# ── Per-prompt diffs with ablation ────────────────────────────────────\ndef get_per_prompt_diffs(model, circuit_edges, tokens, io_ids, s_ids,\n                         ablation_mode=\"zero\", attn_means=None, mlp_means=None):\n    \"\"\"Run model with ablation and return per-prompt logit diffs (io - s).\"\"\"\n    circuit_nodes = extract_circuit_nodes(circuit_edges)\n    n_layers, n_heads = model.cfg.n_layers, model.cfg.n_heads\n\n    ablate_heads = {}\n    ablate_mlps = []\n    for layer in range(n_layers):\n        heads = [h for h in range(n_heads) if f'a{layer}.h{h}' not in circuit_nodes]\n        if heads:\n            ablate_heads[layer] = heads\n        if f'm{layer}' not in circuit_nodes:\n            ablate_mlps.append(layer)\n\n    if ablation_mode == \"zero\":\n        def _head_hook(value, hook, heads_to_ablate):\n            for h in heads_to_ablate:\n                value[:, :, h, :] = 0\n            return value\n        def _mlp_hook(value, hook):\n            return torch.zeros_like(value)\n    else:\n        def _head_hook(value, hook, heads_to_ablate, layer_idx=None):\n            mean_val = attn_means[layer_idx]\n            seq_len = value.shape[1]\n            mean_seq = mean_val.shape[1]\n            if mean_seq >= seq_len:\n                m = mean_val[:, -seq_len:, :, :]\n            else:\n                m = torch.nn.functional.pad(mean_val, (0,0,0,0,0,seq_len-mean_seq), mode='replicate')\n            for h in heads_to_ablate:\n                value[:, :, h, :] = m[:, :seq_len, h, :].expand(value.shape[0], -1, -1)\n            return value\n        def _mlp_hook(value, hook, layer_idx=None):\n            mean_val = mlp_means[layer_idx]\n            seq_len = value.shape[1]\n            mean_seq = mean_val.shape[1]\n            if mean_seq >= seq_len:\n                m = mean_val[:, -seq_len:, :]\n            else:\n                m = torch.nn.functional.pad(mean_val, (0,0,0,seq_len-mean_seq), mode='replicate')\n            return m[:, :seq_len, :].expand(value.shape[0], -1, -1)\n\n    hooks = []\n    for layer, heads in ablate_heads.items():\n        if ablation_mode == \"zero\":\n            hooks.append((f\"blocks.{layer}.attn.hook_result\",\n                          partial(_head_hook, heads_to_ablate=heads)))\n        else:\n            hooks.append((f\"blocks.{layer}.attn.hook_result\",\n                          partial(_head_hook, heads_to_ablate=heads, layer_idx=layer)))\n    for layer in ablate_mlps:\n        if ablation_mode == \"zero\":\n            hooks.append((f\"blocks.{layer}.hook_mlp_out\", _mlp_hook))\n        else:\n            hooks.append((f\"blocks.{layer}.hook_mlp_out\", partial(_mlp_hook, layer_idx=layer)))\n\n    with torch.no_grad():\n        logits = model.run_with_hooks(tokens, fwd_hooks=hooks)\n\n    n = logits.shape[0]\n    diffs = (logits[range(n), -1, io_ids[:n]] - logits[range(n), -1, s_ids[:n]]).cpu().numpy()\n    return diffs\n\n\n# ── Bootstrap ─────────────────────────────────────────────────────────\ndef bootstrap_delta_ci(css_diffs, method_diffs, baseline_diffs,\n                       n_bootstrap=1000, seed=42):\n    rng = np.random.RandomState(seed)\n    n = len(baseline_diffs)\n    deltas = []\n\n    for _ in range(n_bootstrap):\n        idx = rng.choice(n, n, replace=True)\n        bl = baseline_diffs[idx].mean()\n        if abs(bl) < 1e-8:\n            continue\n        cpr_css = css_diffs[idx].mean() / bl\n        cpr_method = method_diffs[idx].mean() / bl\n        deltas.append(cpr_css - cpr_method)\n\n    deltas = np.array(deltas)\n    lo = float(np.percentile(deltas, 2.5))\n    hi = float(np.percentile(deltas, 97.5))\n\n    observed_bl = baseline_diffs.mean()\n    if abs(observed_bl) > 1e-8:\n        observed_delta = float(css_diffs.mean() / observed_bl - method_diffs.mean() / observed_bl)\n    else:\n        observed_delta = 0.0\n\n    if observed_delta >= 0:\n        p_value = float(np.mean(deltas <= 0))\n    else:\n        p_value = float(np.mean(deltas >= 0))\n\n    return {\n        \"observed_delta\": observed_delta,\n        \"bootstrap_mean\": float(deltas.mean()),\n        \"bootstrap_std\": float(deltas.std()),\n        \"ci_lo\": lo,\n        \"ci_hi\": hi,\n        \"p_value\": p_value,\n        \"n_valid\": len(deltas),\n    }\n\n\n# ── Main ──────────────────────────────────────────────────────────────\ndef main():\n    np.random.seed(SEED)\n    device = \"cuda\" if torch.cuda.is_available() else \"cpu\"\n    print(f\"Device: {device}\")\n    print(f\"Bootstrap: {N_BOOTSTRAP}, seed: {SEED}\")\n\n    # Load score caches\n    print(\"\\nLoading edge score caches...\")\n    with open(CACHE_DIR / \"cache_eap_ig.json\") as f:\n        eapig_scores = json.load(f)\n    with open(CACHE_DIR / \"cache_edge_pruning.json\") as f:\n        ep_scores = json.load(f)\n    with open(CACHE_DIR / \"cache_acdc.json\") as f:\n        acdc_scores = json.load(f)\n    print(f\"  EAP-IG: {len(eapig_scores)}, EP: {len(ep_scores)}, ACDC: {len(acdc_scores)}\")\n\n    # Reconstruct CSS=1.0 circuit\n    acdc_circuit = isinf_edges(acdc_scores)\n    eapig_100 = topk_edges(eapig_scores, 100)\n    ep_100 = topk_edges(ep_scores, 100)\n    css_scores = compute_css({\"acdc\": acdc_circuit, \"eap_ig\": eapig_100, \"ep\": ep_100})\n    css_10 = threshold_css(css_scores, 1.0)\n    N = len(css_10)\n    print(f\"  CSS=1.0: {N} edges\")\n\n    # Top-N circuits\n    eapig_topN = topk_edges(eapig_scores, N)\n    ep_topN = topk_edges(ep_scores, N)\n    acdc_topN = topk_edges(acdc_scores, N)\n\n    circuits = {\n        \"CSS=1.0\": css_10,\n        \"EAP-IG\": eapig_topN,\n        \"EP\": ep_topN,\n        \"ACDC\": acdc_topN,\n    }\n\n    # Load model & data\n    print(\"\\nLoading model...\")\n    model = load_model(device)\n    prompts, labels = generate_ioi_data(model.tokenizer, 100, SEED)\n    tokens = model.to_tokens(prompts, prepend_bos=True).to(device)\n    io_ids = torch.tensor([l[0] for l in labels])\n    s_ids = torch.tensor([l[1] for l in labels])\n    print(f\"  {len(prompts)} prompts\")\n\n    # Baseline (no ablation) per-prompt diffs\n    print(\"\\nBaseline forward pass...\")\n    with torch.no_grad():\n        baseline_logits = model(tokens)\n    n = baseline_logits.shape[0]\n    baseline_diffs = (baseline_logits[range(n), -1, io_ids[:n]] -\n                      baseline_logits[range(n), -1, s_ids[:n]]).cpu().numpy()\n    del baseline_logits\n    print(f\"  Baseline mean diff: {baseline_diffs.mean():.4f}\")\n\n    # Collect mean activations for mean ablation\n    print(\"Collecting mean activations...\")\n    attn_means, mlp_means = collect_mean_activations(model, tokens)\n\n    # Per-prompt diffs for each circuit under both ablation modes\n    all_results = {}\n    for ablation in [\"zero\", \"mean\"]:\n        print(f\"\\n{'='*60}\")\n        print(f\"  ABLATION: {ablation}\")\n        print(f\"{'='*60}\")\n\n        circuit_diffs = {}\n        for name, edges in circuits.items():\n            print(f\"  {name} ({len(edges)} edges)...\", end=\" \", flush=True)\n            if ablation == \"mean\":\n                diffs = get_per_prompt_diffs(model, edges, tokens, io_ids, s_ids,\n                                             \"mean\", attn_means, mlp_means)\n            else:\n                diffs = get_per_prompt_diffs(model, edges, tokens, io_ids, s_ids, \"zero\")\n            cpr = float(diffs.mean() / baseline_diffs.mean()) if abs(baseline_diffs.mean()) > 1e-8 else 0.0\n            print(f\"CPR={cpr:.4f}\")\n            circuit_diffs[name] = diffs\n\n        # Bootstrap: CSS vs each method\n        css_diffs = circuit_diffs[\"CSS=1.0\"]\n        comparisons = {}\n        for method_name in [\"EAP-IG\", \"EP\", \"ACDC\"]:\n            print(f\"\\n  Bootstrap CSS=1.0 vs {method_name}...\")\n            ci = bootstrap_delta_ci(css_diffs, circuit_diffs[method_name],\n                                    baseline_diffs, N_BOOTSTRAP, SEED)\n            significant = (ci[\"ci_lo\"] > 0) or (ci[\"ci_hi\"] < 0)\n            ci[\"significant\"] = significant\n\n            bl_mean = baseline_diffs.mean()\n            css_cpr = float(css_diffs.mean() / bl_mean) if abs(bl_mean) > 1e-8 else 0.0\n            method_cpr = float(circuit_diffs[method_name].mean() / bl_mean) if abs(bl_mean) > 1e-8 else 0.0\n\n            comparisons[method_name] = {\n                \"css_cpr\": css_cpr,\n                \"method_cpr\": method_cpr,\n                \"num_edges\": N,\n                **ci,\n            }\n            print(f\"    delta={ci['observed_delta']:+.4f}, \"\n                  f\"CI=[{ci['ci_lo']:+.4f}, {ci['ci_hi']:+.4f}], \"\n                  f\"p={ci['p_value']:.4f}, sig={'Yes' if significant else 'No'}\")\n\n        all_results[ablation] = comparisons\n\n    # Summary\n    print(f\"\\n{'='*75}\")\n    print(f\"  SIZE-CONTROLLED BOOTSTRAP CI SUMMARY (N={N}, n_boot={N_BOOTSTRAP})\")\n    print(f\"{'='*75}\")\n    for ablation in [\"zero\", \"mean\"]:\n        print(f\"\\n  Ablation: {ablation}\")\n        header = f\"  {'Comparison':<25} | {'Delta':>8} | {'95% CI':>22} | {'p-value':>8} | {'Sig':>4}\"\n        print(header)\n        print(\"  \" + \"-\" * (len(header) - 2))\n        for method, r in all_results[ablation].items():\n            sig = \"Yes\" if r[\"significant\"] else \"No\"\n            ci_str = f\"[{r['ci_lo']:+.4f}, {r['ci_hi']:+.4f}]\"\n            print(f\"  CSS vs {method:<20} | {r['observed_delta']:>+8.4f} | {ci_str:>22} | {r['p_value']:>8.4f} | {sig:>4}\")\n\n    # Save\n    output = {\n        \"task\": \"ioi\",\n        \"N\": N,\n        \"n_bootstrap\": N_BOOTSTRAP,\n        \"seed\": SEED,\n        \"n_prompts\": len(prompts),\n        \"css_10_edges\": sorted(css_10),\n        \"baseline_mean_diff\": float(baseline_diffs.mean()),\n        \"results\": all_results,\n    }\n    with open(RESULT_PATH, \"w\") as f:\n        json.dump(output, f, indent=2)\n    print(f\"\\nSaved: {RESULT_PATH}\")\n\n    del model; gc.collect()\n    if torch.cuda.is_available():\n        torch.cuda.empty_cache()\n    print(\"Done.\")\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"Script written.\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-39279",
    "command": "cat > /root/min_necessary_circuit_css/run_bootstrap_ci_size_controlled.py << 'PYEOF'\n#!/usr/bin/env python3\n\"\"\"Size-controlled bootstrap CI for CSS=1.0 CPR advantage (IOI task).\n\nRecomputes per-prompt diffs for each method's top-16 circuit, then\nbootstraps delta = CPR(CSS=1.0) - CPR(method) with prompt-level resampling.\n\nInput: cached edge scores (cache_eap_ig.json, cache_edge_pruning.json, cache_acdc.json)\nOutput: /root/min_necessary_circuit_css/bootstrap_ci_size_controlled_results.json\n\"\"\"\n\nimport os\nos.environ.setdefault(\"CUDA_VISIBLE_DEVICES\", \"0\")\n\nimport json, math, random, re, gc\nfrom pathlib import Path\nfrom functools import partial\n\nimport torch\nimport numpy as np\n\n# ── Config ────────────────────────────────────────────────────────────\nLOCAL_GPT2 = \"/root/autodl-tmp/gpt2-small\"\nGPT2_ALIASES = (\"gpt2\", \"gpt2-small\", \"openai-community/gpt2\")\nCACHE_DIR = Path(\"/root/min_necessary_circuit_css\")\nRESULT_PATH = CACHE_DIR / \"bootstrap_ci_size_controlled_results.json\"\nN_BOOTSTRAP = 1000\nSEED = 42\n\nNAMES = [\"John\", \"Mary\", \"Alice\", \"Bob\", \"Charlie\", \"David\", \"Emma\", \"Frank\",\n         \"Grace\", \"Henry\", \"Jack\", \"Kate\", \"Leo\", \"Mia\", \"Noah\", \"Tom\"]\nTEMPLATES = [\n    \"When {io} and {s} went to the {place}, {s} gave a {obj} to\",\n    \"After {io} and {s} arrived at the {place}, {s} handed a {obj} to\",\n    \"{io} and {s} were at the {place}. {s} gave a {obj} to\",\n    \"Then, {io} and {s} had a meeting at the {place}, {s} passed a {obj} to\",\n]\nPLACES = [\"store\", \"park\", \"library\", \"school\", \"hospital\", \"restaurant\", \"office\"]\nOBJECTS = [\"bottle\", \"book\", \"letter\", \"ball\", \"gift\", \"toy\", \"bag\"]\n\n\n# ── HF patching ──────────────────────────────────────────────────────\ndef patch_hf():\n    from transformers import AutoConfig, AutoTokenizer, AutoModelForCausalLM\n    def _make_patched(orig_fn):\n        def patched(name_or_path, *args, **kwargs):\n            if name_or_path in GPT2_ALIASES:\n                name_or_path = LOCAL_GPT2\n            return orig_fn(name_or_path, *args, **kwargs)\n        return patched\n    AutoConfig.from_pretrained = staticmethod(_make_patched(AutoConfig.from_pretrained))\n    AutoTokenizer.from_pretrained = staticmethod(_make_patched(AutoTokenizer.from_pretrained))\n    AutoModelForCausalLM.from_pretrained = staticmethod(_make_patched(AutoModelForCausalLM.from_pretrained))\n\npatch_hf()\n\n\n# ── Model ─────────────────────────────────────────────────────────────\ndef load_model(device=\"cuda\"):\n    from transformer_lens import HookedTransformer\n    from transformers import AutoModelForCausalLM\n    hf_model = AutoModelForCausalLM.from_pretrained(LOCAL_GPT2)\n    model = HookedTransformer.from_pretrained(\"gpt2-small\", hf_model=hf_model, device=device)\n    model.set_use_attn_result(True)\n    model.set_use_split_qkv_input(True)\n    model.set_use_hook_mlp_in(True)\n    return model\n\n\n# ── Data ──────────────────────────────────────────────────────────────\ndef generate_ioi_data(tokenizer, num_samples=100, seed=42):\n    random.seed(seed)\n    prompts, labels = [], []\n    for _ in range(num_samples):\n        io_name, s_name = random.sample(NAMES, 2)\n        template = random.choice(TEMPLATES)\n        place = random.choice(PLACES)\n        obj = random.choice(OBJECTS)\n        prompts.append(template.format(io=io_name, s=s_name, place=place, obj=obj))\n        labels.append((tokenizer.encode(\" \" + io_name)[0],\n                        tokenizer.encode(\" \" + s_name)[0]))\n    return prompts, labels\n\n\n# ── Circuit helpers ───────────────────────────────────────────────────\ndef extract_circuit_nodes(circuit_edges):\n    nodes = set()\n    for edge in circuit_edges:\n        parts = edge.split('->')\n        if len(parts) != 2:\n            continue\n        nodes.add(parts[0].strip())\n        dst_base = re.sub(r'\\.[qkv]$', '', parts[1].strip())\n        nodes.add(dst_base)\n    nodes.discard('input')\n    nodes.discard('logits')\n    return nodes\n\n\ndef topk_edges(scores, k):\n    sorted_edges = sorted(\n        scores.items(),\n        key=lambda x: abs(x[1]) if not math.isinf(x[1]) else float('inf'),\n        reverse=True\n    )\n    return set(e for e, _ in sorted_edges[:k])\n\n\ndef isinf_edges(scores):\n    return set(e for e, v in scores.items() if math.isinf(v))\n\n\ndef compute_css(methods_edges):\n    K = len(methods_edges)\n    union = set()\n    for edges in methods_edges.values():\n        union |= edges\n    return {e: sum(1 for es in methods_edges.values() if e in es) / K for e in union}\n\n\ndef threshold_css(css_scores, threshold):\n    return {e for e, s in css_scores.items() if s >= threshold - 1e-2}\n\n\n# ── Mean activations ─────────────────────────────────────────────────\ndef collect_mean_activations(model, tokens):\n    n_layers = model.cfg.n_layers\n    accumulators = {}\n\n    def make_accumulator(key):\n        def hook_fn(value, hook):\n            if key not in accumulators:\n                accumulators[key] = value.detach().mean(dim=0, keepdim=True).clone()\n            else:\n                accumulators[key] += value.detach().mean(dim=0, keepdim=True)\n            return value\n        return hook_fn\n\n    hooks = []\n    for layer in range(n_layers):\n        hooks.append((f\"blocks.{layer}.attn.hook_result\", make_accumulator(f\"attn_{layer}\")))\n        hooks.append((f\"blocks.{layer}.hook_mlp_out\", make_accumulator(f\"mlp_{layer}\")))\n\n    batch_size = 25\n    n_batches = 0\n    with torch.no_grad():\n        for start in range(0, len(tokens), batch_size):\n            batch = tokens[start:start + batch_size]\n            model.run_with_hooks(batch, fwd_hooks=hooks)\n            n_batches += 1\n\n    attn_means, mlp_means = {}, {}\n    for layer in range(n_layers):\n        attn_means[layer] = accumulators[f\"attn_{layer}\"] / n_batches\n        mlp_means[layer] = accumulators[f\"mlp_{layer}\"] / n_batches\n    return attn_means, mlp_means\n\n\n# ── Per-prompt diffs with ablation ────────────────────────────────────\ndef get_per_prompt_diffs(model, circuit_edges, tokens, io_ids, s_ids,\n                         ablation_mode=\"zero\", attn_means=None, mlp_means=None):\n    \"\"\"Run model with ablation and return per-prompt logit diffs (io - s).\"\"\"\n    circuit_nodes = extract_circuit_nodes(circuit_edges)\n    n_layers, n_heads = model.cfg.n_layers, model.cfg.n_heads\n\n    ablate_heads = {}\n    ablate_mlps = []\n    for layer in range(n_layers):\n        heads = [h for h in range(n_heads) if f'a{layer}.h{h}' not in circuit_nodes]\n        if heads:\n            ablate_heads[layer] = heads\n        if f'm{layer}' not in circuit_nodes:\n            ablate_mlps.append(layer)\n\n    if ablation_mode == \"zero\":\n        def _head_hook(value, hook, heads_to_ablate):\n            for h in heads_to_ablate:\n                value[:, :, h, :] = 0\n            return value\n        def _mlp_hook(value, hook):\n            return torch.zeros_like(value)\n    else:\n        def _head_hook(value, hook, heads_to_ablate, layer_idx=None):\n            mean_val = attn_means[layer_idx]\n            seq_len = value.shape[1]\n            mean_seq = mean_val.shape[1]\n            if mean_seq >= seq_len:\n                m = mean_val[:, -seq_len:, :, :]\n            else:\n                m = torch.nn.functional.pad(mean_val, (0,0,0,0,0,seq_len-mean_seq), mode='replicate')\n            for h in heads_to_ablate:\n                value[:, :, h, :] = m[:, :seq_len, h, :].expand(value.shape[0], -1, -1)\n            return value\n        def _mlp_hook(value, hook, layer_idx=None):\n            mean_val = mlp_means[layer_idx]\n            seq_len = value.shape[1]\n            mean_seq = mean_val.shape[1]\n            if mean_seq >= seq_len:\n                m = mean_val[:, -seq_len:, :]\n            else:\n                m = torch.nn.functional.pad(mean_val, (0,0,0,seq_len-mean_seq), mode='replicate')\n            return m[:, :seq_len, :].expand(value.shape[0], -1, -1)\n\n    hooks = []\n    for layer, heads in ablate_heads.items():\n        if ablation_mode == \"zero\":\n            hooks.append((f\"blocks.{layer}.attn.hook_result\",\n                          partial(_head_hook, heads_to_ablate=heads)))\n        else:\n            hooks.append((f\"blocks.{layer}.attn.hook_result\",\n                          partial(_head_hook, heads_to_ablate=heads, layer_idx=layer)))\n    for layer in ablate_mlps:\n        if ablation_mode == \"zero\":\n            hooks.append((f\"blocks.{layer}.hook_mlp_out\", _mlp_hook))\n        else:\n            hooks.append((f\"blocks.{layer}.hook_mlp_out\", partial(_mlp_hook, layer_idx=layer)))\n\n    with torch.no_grad():\n        logits = model.run_with_hooks(tokens, fwd_hooks=hooks)\n\n    n = logits.shape[0]\n    diffs = (logits[range(n), -1, io_ids[:n]] - logits[range(n), -1, s_ids[:n]]).cpu().numpy()\n    return diffs\n\n\n# ── Bootstrap ─────────────────────────────────────────────────────────\ndef bootstrap_delta_ci(css_diffs, method_diffs, baseline_diffs,\n                       n_bootstrap=1000, seed=42):\n    rng = np.random.RandomState(seed)\n    n = len(baseline_diffs)\n    deltas = []\n\n    for _ in range(n_bootstrap):\n        idx = rng.choice(n, n, replace=True)\n        bl = baseline_diffs[idx].mean()\n        if abs(bl) < 1e-8:\n            continue\n        cpr_css = css_diffs[idx].mean() / bl\n        cpr_method = method_diffs[idx].mean() / bl\n        deltas.append(cpr_css - cpr_method)\n\n    deltas = np.array(deltas)\n    lo = float(np.percentile(deltas, 2.5))\n    hi = float(np.percentile(deltas, 97.5))\n\n    observed_bl = baseline_diffs.mean()\n    if abs(observed_bl) > 1e-8:\n        observed_delta = float(css_diffs.mean() / observed_bl - method_diffs.mean() / observed_bl)\n    else:\n        observed_delta = 0.0\n\n    if observed_delta >= 0:\n        p_value = float(np.mean(deltas <= 0))\n    else:\n        p_value = float(np.mean(deltas >= 0))\n\n    return {\n        \"observed_delta\": observed_delta,\n        \"bootstrap_mean\": float(deltas.mean()),\n        \"bootstrap_std\": float(deltas.std()),\n        \"ci_lo\": lo,\n        \"ci_hi\": hi,\n        \"p_value\": p_value,\n        \"n_valid\": len(deltas),\n    }\n\n\n# ── Main ──────────────────────────────────────────────────────────────\ndef main():\n    np.random.seed(SEED)\n    device = \"cuda\" if torch.cuda.is_available() else \"cpu\"\n    print(f\"Device: {device}\")\n    print(f\"Bootstrap: {N_BOOTSTRAP}, seed: {SEED}\")\n\n    # Load score caches\n    print(\"\\nLoading edge score caches...\")\n    with open(CACHE_DIR / \"cache_eap_ig.json\") as f:\n        eapig_scores = json.load(f)\n    with open(CACHE_DIR / \"cache_edge_pruning.json\") as f:\n        ep_scores = json.load(f)\n    with open(CACHE_DIR / \"cache_acdc.json\") as f:\n        acdc_scores = json.load(f)\n    print(f\"  EAP-IG: {len(eapig_scores)}, EP: {len(ep_scores)}, ACDC: {len(acdc_scores)}\")\n\n    # Reconstruct CSS=1.0 circuit\n    acdc_circuit = isinf_edges(acdc_scores)\n    eapig_100 = topk_edges(eapig_scores, 100)\n    ep_100 = topk_edges(ep_scores, 100)\n    css_scores = compute_css({\"acdc\": acdc_circuit, \"eap_ig\": eapig_100, \"ep\": ep_100})\n    css_10 = threshold_css(css_scores, 1.0)\n    N = len(css_10)\n    print(f\"  CSS=1.0: {N} edges\")\n\n    # Top-N circuits\n    eapig_topN = topk_edges(eapig_scores, N)\n    ep_topN = topk_edges(ep_scores, N)\n    acdc_topN = topk_edges(acdc_scores, N)\n\n    circuits = {\n        \"CSS=1.0\": css_10,\n        \"EAP-IG\": eapig_topN,\n        \"EP\": ep_topN,\n        \"ACDC\": acdc_topN,\n    }\n\n    # Load model & data\n    print(\"\\nLoading model...\")\n    model = load_model(device)\n    prompts, labels = generate_ioi_data(model.tokenizer, 100, SEED)\n    tokens = model.to_tokens(prompts, prepend_bos=True).to(device)\n    io_ids = torch.tensor([l[0] for l in labels])\n    s_ids = torch.tensor([l[1] for l in labels])\n    print(f\"  {len(prompts)} prompts\")\n\n    # Baseline (no ablation) per-prompt diffs\n    print(\"\\nBaseline forward pass...\")\n    with torch.no_grad():\n        baseline_logits = model(tokens)\n    n = baseline_logits.shape[0]\n    baseline_diffs = (baseline_logits[range(n), -1, io_ids[:n]] -\n                      baseline_logits[range(n), -1, s_ids[:n]]).cpu().numpy()\n    del baseline_logits\n    print(f\"  Baseline mean diff: {baseline_diffs.mean():.4f}\")\n\n    # Collect mean activations for mean ablation\n    print(\"Collecting mean activations...\")\n    attn_means, mlp_means = collect_mean_activations(model, tokens)\n\n    # Per-prompt diffs for each circuit under both ablation modes\n    all_results = {}\n    for ablation in [\"zero\", \"mean\"]:\n        print(f\"\\n{'='*60}\")\n        print(f\"  ABLATION: {ablation}\")\n        print(f\"{'='*60}\")\n\n        circuit_diffs = {}\n        for name, edges in circuits.items():\n            print(f\"  {name} ({len(edges)} edges)...\", end=\" \", flush=True)\n            if ablation == \"mean\":\n                diffs = get_per_prompt_diffs(model, edges, tokens, io_ids, s_ids,\n                                             \"mean\", attn_means, mlp_means)\n            else:\n                diffs = get_per_prompt_diffs(model, edges, tokens, io_ids, s_ids, \"zero\")\n            cpr = float(diffs.mean() / baseline_diffs.mean()) if abs(baseline_diffs.mean()) > 1e-8 else 0.0\n            print(f\"CPR={cpr:.4f}\")\n            circuit_diffs[name] = diffs\n\n        # Bootstrap: CSS vs each method\n        css_diffs = circuit_diffs[\"CSS=1.0\"]\n        comparisons = {}\n        for method_name in [\"EAP-IG\", \"EP\", \"ACDC\"]:\n            print(f\"\\n  Bootstrap CSS=1.0 vs {method_name}...\")\n            ci = bootstrap_delta_ci(css_diffs, circuit_diffs[method_name],\n                                    baseline_diffs, N_BOOTSTRAP, SEED)\n            significant = (ci[\"ci_lo\"] > 0) or (ci[\"ci_hi\"] < 0)\n            ci[\"significant\"] = significant\n\n            bl_mean = baseline_diffs.mean()\n            css_cpr = float(css_diffs.mean() / bl_mean) if abs(bl_mean) > 1e-8 else 0.0\n            method_cpr = float(circuit_diffs[method_name].mean() / bl_mean) if abs(bl_mean) > 1e-8 else 0.0\n\n            comparisons[method_name] = {\n                \"css_cpr\": css_cpr,\n                \"method_cpr\": method_cpr,\n                \"num_edges\": N,\n                **ci,\n            }\n            print(f\"    delta={ci['observed_delta']:+.4f}, \"\n                  f\"CI=[{ci['ci_lo']:+.4f}, {ci['ci_hi']:+.4f}], \"\n                  f\"p={ci['p_value']:.4f}, sig={'Yes' if significant else 'No'}\")\n\n        all_results[ablation] = comparisons\n\n    # Summary\n    print(f\"\\n{'='*75}\")\n    print(f\"  SIZE-CONTROLLED BOOTSTRAP CI SUMMARY (N={N}, n_boot={N_BOOTSTRAP})\")\n    print(f\"{'='*75}\")\n    for ablation in [\"zero\", \"mean\"]:\n        print(f\"\\n  Ablation: {ablation}\")\n        header = f\"  {'Comparison':<25} | {'Delta':>8} | {'95% CI':>22} | {'p-value':>8} | {'Sig':>4}\"\n        print(header)\n        print(\"  \" + \"-\" * (len(header) - 2))\n        for method, r in all_results[ablation].items():\n            sig = \"Yes\" if r[\"significant\"] else \"No\"\n            ci_str = f\"[{r['ci_lo']:+.4f}, {r['ci_hi']:+.4f}]\"\n            print(f\"  CSS vs {method:<20} | {r['observed_delta']:>+8.4f} | {ci_str:>22} | {r['p_value']:>8.4f} | {sig:>4}\")\n\n    # Save\n    output = {\n        \"task\": \"ioi\",\n        \"N\": N,\n        \"n_bootstrap\": N_BOOTSTRAP,\n        \"seed\": SEED,\n        \"n_prompts\": len(prompts),\n        \"css_10_edges\": sorted(css_10),\n        \"baseline_mean_diff\": float(baseline_diffs.mean()),\n        \"results\": all_results,\n    }\n    with open(RESULT_PATH, \"w\") as f:\n        json.dump(output, f, indent=2)\n    print(f\"\\nSaved: {RESULT_PATH}\")\n\n    del model; gc.collect()\n    if torch.cuda.is_available():\n        torch.cuda.empty_cache()\n    print(\"Done.\")\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"Script written.\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-13T16:13:04.355488+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Script written.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-13T16:13:04.355638+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-39279",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/min_necessary_circuit_css && python run_bootstrap_ci_size_controlled.py 2>&1",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-39279",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/min_necessary_circuit_css && python run_bootstrap_ci_size_controlled.py 2>&1",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-13T16:13:04.355812+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Device: cuda\\nBootstrap: 1000, seed: 42\\n\\nLoading edge score caches...\\n  EAP-IG: 32491, EP: 32491, ACDC: 32491\\n  CSS=1.0: 16 edges\\n\\nLoading model...\\nLoaded pretrained model gpt2-small into HookedTransformer\\n  100 prompts\\n\\nBaseline forward pass...\\n  Baseline mean diff: 1.0231\\nCollecting mean activations...\\n\\n============================================================\\n  ABLATION: zero\\n============================================================\\n  CSS=1.0 (16 edges)... CPR=0.0295\\n  EAP-IG (16 edges)... CPR=-0.0585\\n  EP (16 edges)... CPR=-0.0091\\n  ACDC (16 edges)... CPR=0.0295\\n\\n  Bootstrap CSS=1.0 vs EAP-IG...\\n    delta=+0.0880, CI=[-0.0664, +0.2667], p=0.1120, sig=No\\n\\n  Bootstrap CSS=1.0 vs EP...\\n    delta=+0.0386, CI=[-0.0790, +0.1468], p=0.2490, sig=No\\n\\n  Bootstrap CSS=1.0 vs ACDC...\\n    delta=+0.0000, CI=[+0.0000, +0.0000], p=1.0000, sig=No\\n\\n============================================================\\n  ABLATION: mean\\n============================================================\\n  CSS=1.0 (16 edges)... CPR=0.1770\\n  EAP-IG (16 edges)... CPR=0.1820\\n  EP (16 edges)... CPR=0.1832\\n  ACDC (16 edges)... CPR=0.1770\\n\\n  Bootstrap CSS=1.0 vs EAP-IG...\\n    delta=-0.0050, CI=[-0.0392, +0.0227], p=0.3590, sig=No\\n\\n  Bootstrap CSS=1.0 vs EP...\\n    delta=-0.0062, CI=[-0.0318, +0.0141], p=0.2790, sig=No\\n\\n  Bootstrap CSS=1.0 vs ACDC...\\n    delta=+0.0000, CI=[+0.0000, +0.0000], p=1.0000, sig=No\\n\\n===========================================================================\\n  SIZE-CONTROLLED BOOTSTRAP CI SUMMARY (N=16, n_boot=1000)\\n===========================================================================\\n\\n  Ablation: zero\\n  Comparison                |    Delta |                 95% CI |  p-value |  Sig\\n  -------------------------------------------------------------------------------\\n  CSS vs EAP-IG               |  +0.0880 | 
…[truncated 862 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-13T16:13:04.355990+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "cat /root/min_necessary_circuit_css/bootstrap_ci_size_controlled_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "cat /root/min_necessary_circuit_css/bootstrap_ci_size_controlled_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-13T16:13:04.356177+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"task\\\": \\\"ioi\\\",\\n  \\\"N\\\": 16,\\n  \\\"n_bootstrap\\\": 1000,\\n  \\\"seed\\\": 42,\\n  \\\"n_prompts\\\": 100,\\n  \\\"css_10_edges\\\": [\\n    \\\"a0.h1->a9.h9.v\\\",\\n    \\\"a10.h0->logits\\\",\\n    \\\"a10.h10->logits\\\",\\n    \\\"a10.h6->logits\\\",\\n    \\\"a10.h7->logits\\\",\\n    \\\"a9.h6->logits\\\",\\n    \\\"a9.h9->a10.h7.q\\\",\\n    \\\"a9.h9->logits\\\",\\n    \\\"input->a0.h1.v\\\",\\n    \\\"input->m0\\\",\\n    \\\"m0->a10.h7.k\\\",\\n    \\\"m0->a9.h6.v\\\",\\n    \\\"m0->a9.h9.v\\\",\\n    \\\"m4->a9.h9.v\\\",\\n    \\\"m5->a9.h9.v\\\",\\n    \\\"m6->a9.h9.v\\\"\\n  ],\\n  \\\"baseline_mean_diff\\\": 1.0230518579483032,\\n  \\\"results\\\": {\\n    \\\"zero\\\": {\\n      \\\"EAP-IG\\\": {\\n        \\\"css_cpr\\\": 0.02947526052594185,\\n        \\\"method_cpr\\\": -0.05848280340433121,\\n        \\\"num_edges\\\": 16,\\n        \\\"observed_delta\\\": 0.08795806765556335,\\n        \\\"bootstrap_mean\\\": 0.09158056974411011,\\n        \\\"bootstrap_std\\\": 0.08166132122278214,\\n        \\\"ci_lo\\\": -0.06643012911081314,\\n        \\\"ci_hi\\\": 0.26667043566703796,\\n        \\\"p_value\\\": 0.112,\\n        \\\"n_valid\\\": 1000,\\n        \\\"significant\\\": false\\n      },\\n      \\\"EP\\\": {\\n        \\\"css_cpr\\\": 0.02947526052594185,\\n        \\\"method_cpr\\\": -0.009082772769033909,\\n        \\\"num_edges\\\": 16,\\n        \\\"observed_delta\\\": 0.03855803236365318,\\n        \\\"bootstrap_mean\\\": 0.03707165643572807,\\n        \\\"bootstrap_std\\\": 0.05869181081652641,\\n        \\\"ci_lo\\\": -0.07896982878446579,\\n        \\\"ci_hi\\\": 0.14684949815273285,\\n        \\\"p_value\\\": 0.249,\\n        \\\"n_valid\\\": 1000,\\n        \\\"significant\\\": false\\n      },\\n      \\\"ACDC\\\": {\\n        \\\"css_cpr\\\": 0.02947526052594185,\\n        \\\"method_cpr\\\": 0.02947526052594185,\\n        \\\"num_edges\\\": 16,\\n     
…[truncated 1945 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-13T16:13:04.356329+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "bootstrap_ci_size_controlled",
  "field": "status",
  "value": "DONE",
  "project": "min_necessary_circuit_css",
  "spec": "{'command': 'python run_bootstrap_ci_size_controlled.py', 'server': 'westd-39279', 'data_path': '/root/min_necessary_circuit_css/cache_eap_ig.json', 'data_count': 100, 'model_name': 'gpt2-small', 'seed': 42}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "bootstrap_ci_size_controlled",
    "field": "status",
    "value": "DONE",
    "project": "min_necessary_circuit_css",
    "spec": "{'command': 'python run_bootstrap_ci_size_controlled.py', 'server': 'westd-39279', 'data_path': '/root/min_necessary_circuit_css/cache_eap_ig.json', 'data_count': 100, 'model_name': 'gpt2-small', 'seed': 42}"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-13T16:13:04.356462+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → DONE. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.0516}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-13T16:13:04.356583+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "bootstrap_ci_size_controlled",
  "field": "status",
  "value": "QUEUED",
  "project": "min_necessary_circuit_css",
  "spec": "{'command': 'python run_bootstrap_ci_size_controlled.py', 'server': 'westd-39279', 'data_path': '/root/min_necessary_circuit_css/cache_eap_ig.json', 'data_count': 100, 'model_name': 'gpt2-small', 'seed': 42}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "bootstrap_ci_size_controlled",
    "field": "status",
    "value": "QUEUED",
    "project": "min_necessary_circuit_css",
    "spec": "{'command': 'python run_bootstrap_ci_size_controlled.py', 'server': 'westd-39279', 'data_path': '/root/min_necessary_circuit_css/cache_eap_ig.json', 'data_count': 100, 'model_name': 'gpt2-small', 'seed': 42}"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-13T16:13:04.356739+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"bootstrap_ci_size_controlled\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-13T16:07:41.034Z\", \"updated_at\": \"2026-05-13T16:12:22.770Z\", \"hypothesis\": \"Size-controlled Bootstrap CI (n=1000): CSS=1.0 top-16 vs EAP-IG/EP/ACDC top-16 的 per-prompt CPR delta 统计显著性检验（公平比较，控制电路大小 N=16）\", \"parent\": \"ioi_size_controlled_baseline\", \"spec\": {\"command\": \"python run_bootstrap_ci_size_controlled.py\", \"server\": \"westd-39279\", \"data_path\": \"/root/min_necessary_circuit_css/cache_eap_ig.json\", \"data_count\": 100, \"model_name\": \"gpt2-small\", \"seed\": 42}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2775}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-13T16:13:04.356875+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "bootstrap_ci_size_controlled",
  "field": "status",
  "value": "RUNNING",
  "project": "min_necessary_circuit_css",
  "spec": "{'command': 'python run_bootstrap_ci_size_controlled.py', 'server': 'westd-39279', 'data_path': '/root/min_necessary_circuit_css/cache_eap_ig.json', 'data_count': 100, 'model_name': 'gpt2-small', 'seed': 42}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "bootstrap_ci_size_controlled",
    "field": "status",
    "value": "RUNNING",
    "project": "min_necessary_circuit_css",
    "spec": "{'command': 'python run_bootstrap_ci_size_controlled.py', 'server': 'westd-39279', 'data_path': '/root/min_necessary_circuit_css/cache_eap_ig.json', 'data_count': 100, 'model_name': 'gpt2-small', 'seed': 42}"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-13T16:13:04.357005+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Eval experiment requires additional spec fields: ['checkpoint_source', 'eval_data']. Eval spec must include: ['checkpoint_source', 'eval_data']\", \"metadata\": {\"elapsed_seconds\": 0.0481}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-13T16:13:04.357123+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "bootstrap_ci_size_controlled",
  "field": "status",
  "value": "RUNNING",
  "project": "min_necessary_circuit_css",
  "spec": "{'command': 'python run_bootstrap_ci_size_controlled.py', 'server': 'westd-39279', 'data_path': '/root/min_necessary_circuit_css/cache_eap_ig.json', 'data_count': 100, 'model_name': 'gpt2-small', 'seed': 42, 'checkpoint_source': 'ioi_size_controlled_baseline', 'eval_data': 'IOI 100 prompts seed=42'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "bootstrap_ci_size_controlled",
    "field": "status",
    "value": "RUNNING",
    "project": "min_necessary_circuit_css",
    "spec": "{'command': 'python run_bootstrap_ci_size_controlled.py', 'server': 'westd-39279', 'data_path': '/root/min_necessary_circuit_css/cache_eap_ig.json', 'data_count': 100, 'model_name': 'gpt2-small', 'seed': 42, 'checkpoint_source': 'ioi_size_controlled_baseline', 'eval_data': 'IOI 100 prompts seed=42'}"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-13T16:13:04.357264+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"bootstrap_ci_size_controlled\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-13T16:07:41.034Z\", \"updated_at\": \"2026-05-13T16:12:33.898Z\", \"hypothesis\": \"Size-controlled Bootstrap CI (n=1000): CSS=1.0 top-16 vs EAP-IG/EP/ACDC top-16 的 per-prompt CPR delta 统计显著性检验（公平比较，控制电路大小 N=16）\", \"parent\": \"ioi_size_controlled_baseline\", \"spec\": {\"command\": \"python run_bootstrap_ci_size_controlled.py\", \"server\": \"westd-39279\", \"data_path\": \"/root/min_necessary_circuit_css/cache_eap_ig.json\", \"data_count\": 100, \"model_name\": \"gpt2-small\", \"seed\": 42, \"checkpoint_source\": \"ioi_size_controlled_baseline\", \"eval_data\": \"IOI 100 prompts seed=42\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2596}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-13T16:13:04.357433+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "bootstrap_ci_size_controlled",
  "field": "checkpoint_path",
  "value": "/root/min_necessary_circuit_css/bootstrap_ci_size_controlled_results.json",
  "project": "min_necessary_circuit_css"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "bootstrap_ci_size_controlled",
    "field": "checkpoint_path",
    "value": "/root/min_necessary_circuit_css/bootstrap_ci_size_controlled_results.json",
    "project": "min_necessary_circuit_css"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-13T16:13:04.357575+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"bootstrap_ci_size_controlled\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-13T16:07:41.034Z\", \"updated_at\": \"2026-05-13T16:12:39.022Z\", \"hypothesis\": \"Size-controlled Bootstrap CI (n=1000): CSS=1.0 top-16 vs EAP-IG/EP/ACDC top-16 的 per-prompt CPR delta 统计显著性检验（公平比较，控制电路大小 N=16）\", \"parent\": \"ioi_size_controlled_baseline\", \"spec\": {\"command\": \"python run_bootstrap_ci_size_controlled.py\", \"server\": \"westd-39279\", \"data_path\": \"/root/min_necessary_circuit_css/cache_eap_ig.json\", \"data_count\": 100, \"model_name\": \"gpt2-small\", \"seed\": 42, \"checkpoint_source\": \"ioi_size_controlled_baseline\", \"eval_data\": \"IOI 100 prompts seed=42\"}, \"checkpoint_path\": \"/root/min_necessary_circuit_css/bootstrap_ci_size_controlled_results.json\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1246}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-13T16:13:04.357726+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "bootstrap_ci_size_controlled",
  "field": "log_path",
  "value": "/root/min_necessary_circuit_css/run_bootstrap_ci_size_controlled.py",
  "project": "min_necessary_circuit_css"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "bootstrap_ci_size_controlled",
    "field": "log_path",
    "value": "/root/min_necessary_circuit_css/run_bootstrap_ci_size_controlled.py",
    "project": "min_necessary_circuit_css"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-13T16:13:04.357876+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"bootstrap_ci_size_controlled\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-13T16:07:41.034Z\", \"updated_at\": \"2026-05-13T16:12:39.658Z\", \"hypothesis\": \"Size-controlled Bootstrap CI (n=1000): CSS=1.0 top-16 vs EAP-IG/EP/ACDC top-16 的 per-prompt CPR delta 统计显著性检验（公平比较，控制电路大小 N=16）\", \"parent\": \"ioi_size_controlled_baseline\", \"spec\": {\"command\": \"python run_bootstrap_ci_size_controlled.py\", \"server\": \"westd-39279\", \"data_path\": \"/root/min_necessary_circuit_css/cache_eap_ig.json\", \"data_count\": 100, \"model_name\": \"gpt2-small\", \"seed\": 42, \"checkpoint_source\": \"ioi_size_controlled_baseline\", \"eval_data\": \"IOI 100 prompts seed=42\"}, \"checkpoint_path\": \"/root/min_necessary_circuit_css/bootstrap_ci_size_controlled_results.json\", \"log_path\": \"/root/min_necessary_circuit_css/run_bootstrap_ci_size_controlled.py\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0898}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-13T16:13:04.358004+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "bootstrap_ci_size_controlled",
  "field": "conclusion",
  "value": "negative",
  "project": "min_necessary_circuit_css"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "bootstrap_ci_size_controlled",
    "field": "conclusion",
    "value": "negative",
    "project": "min_necessary_circuit_css"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-13T16:13:04.358144+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"bootstrap_ci_size_controlled\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-13T16:07:41.034Z\", \"updated_at\": \"2026-05-13T16:12:42.564Z\", \"hypothesis\": \"Size-controlled Bootstrap CI (n=1000): CSS=1.0 top-16 vs EAP-IG/EP/ACDC top-16 的 per-prompt CPR delta 统计显著性检验（公平比较，控制电路大小 N=16）\", \"parent\": \"ioi_size_controlled_baseline\", \"spec\": {\"command\": \"python run_bootstrap_ci_size_controlled.py\", \"server\": \"westd-39279\", \"data_path\": \"/root/min_necessary_circuit_css/cache_eap_ig.json\", \"data_count\": 100, \"model_name\": \"gpt2-small\", \"seed\": 42, \"checkpoint_source\": \"ioi_size_controlled_baseline\", \"eval_data\": \"IOI 100 prompts seed=42\"}, \"checkpoint_path\": \"/root/min_necessary_circuit_css/bootstrap_ci_size_controlled_results.json\", \"log_path\": \"/root/min_necessary_circuit_css/run_bootstrap_ci_size_controlled.py\", \"conclusion\": \"negative\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0843}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-13T16:13:04.358288+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "bootstrap_ci_size_controlled",
  "field": "metrics",
  "value": "{'zero_ablation': {'css_vs_eapig': {'delta': 0.088, 'ci': [-0.066, 0.267], 'p': 0.112, 'sig': False}, 'css_vs_ep': {'delta': 0.039, 'ci': [-0.079, 0.147], 'p': 0.249, 'sig': False}, 'css_vs_acdc': {'delta': 0, 'ci': [0, 0], 'p': 1, 'sig': False}}, 'mean_ablation': {'css_vs_eapig': {'delta': -0.005, 'ci': [-0.039, 0.023], 'p': 0.359, 'sig': False}, 'css_vs_ep': {'delta': -0.006, 'ci': [-0.032, 0.014], 'p': 0.279, 'sig': False}, 'css_vs_acdc': {'delta': 0, 'ci': [0, 0], 'p': 1, 'sig': False}}}",
  "project": "min_necessary_circuit_css"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "bootstrap_ci_size_controlled",
    "field": "metrics",
    "value": "{'zero_ablation': {'css_vs_eapig': {'delta': 0.088, 'ci': [-0.066, 0.267], 'p': 0.112, 'sig': False}, 'css_vs_ep': {'delta': 0.039, 'ci': [-0.079, 0.147], 'p': 0.249, 'sig': False}, 'css_vs_acdc': {'delta': 0, 'ci': [0, 0], 'p': 1, 'sig': False}}, 'mean_ablation': {'css_vs_eapig': {'delta': -0.005, 'ci': [-0.039, 0.023], 'p': 0.359, 'sig': False}, 'css_vs_ep': {'delta': -0.006, 'ci': [-0.032, 0.014], 'p': 0.279, 'sig': False}, 'css_vs_acdc': {'delta': 0, 'ci': [0, 0], 'p': 1, 'sig': False}}}",
    "project": "min_necessary_circuit_css"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-13T16:13:04.358484+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"bootstrap_ci_size_controlled\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-13T16:07:41.034Z\", \"updated_at\": \"2026-05-13T16:12:48.876Z\", \"hypothesis\": \"Size-controlled Bootstrap CI (n=1000): CSS=1.0 top-16 vs EAP-IG/EP/ACDC top-16 的 per-prompt CPR delta 统计显著性检验（公平比较，控制电路大小 N=16）\", \"parent\": \"ioi_size_controlled_baseline\", \"spec\": {\"command\": \"python run_bootstrap_ci_size_controlled.py\", \"server\": \"westd-39279\", \"data_path\": \"/root/min_necessary_circuit_css/cache_eap_ig.json\", \"data_count\": 100, \"model_name\": \"gpt2-small\", \"seed\": 42, \"checkpoint_source\": \"ioi_size_controlled_baseline\", \"eval_data\": \"IOI 100 prompts seed=42\"}, \"checkpoint_path\": \"/root/min_necessary_circuit_css/bootstrap_ci_size_controlled_results.json\", \"log_path\": \"/root/min_necessary_circuit_css/run_bootstrap_ci_size_controlled.py\", \"conclusion\": \"negative\", \"metrics\": {\"zero_ablation\": {\"css_vs_eapig\": {\"delta\": 0.088, \"ci\": [-0.066, 0.267], \"p\": 0.112, \"sig\": false}, \"css_vs_ep\": {\"delta\": 0.039, \"ci\": [-0.079, 0.147], \"p\": 0.249, \"sig\": false}, \"css_vs_acdc\": {\"delta\": 0, \"ci\": [0, 0], \"p\": 1, \"sig\": false}}, \"mean_ablation\": {\"css_vs_eapig\": {\"delta\": -0.005, \"ci\": [-0.039, 0.023], \"p\": 0.359, \"sig\": false}, \"css_vs_ep\": {\"delta\": -0.006, \"ci\": [-0.032, 0.014], \"p\": 0.279, \"sig\": false}, \"css_vs_acdc\": {\"delta\": 0, \"ci\": [0, 0], \"p\": 1, \"sig\": false}}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0839}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-13T16:13:04.358619+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "bootstrap_ci_size_controlled",
  "field": "status",
  "value": "DONE",
  "project": "min_necessary_circuit_css"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "bootstrap_ci_size_controlled",
    "field": "status",
    "value": "DONE",
    "project": "min_necessary_circuit_css"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-13T16:13:04.358809+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"bootstrap_ci_size_controlled\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T16:07:41.034Z\", \"updated_at\": \"2026-05-13T16:12:52.449Z\", \"hypothesis\": \"Size-controlled Bootstrap CI (n=1000): CSS=1.0 top-16 vs EAP-IG/EP/ACDC top-16 的 per-prompt CPR delta 统计显著性检验（公平比较，控制电路大小 N=16）\", \"parent\": \"ioi_size_controlled_baseline\", \"spec\": {\"command\": \"python run_bootstrap_ci_size_controlled.py\", \"server\": \"westd-39279\", \"data_path\": \"/root/min_necessary_circuit_css/cache_eap_ig.json\", \"data_count\": 100, \"model_name\": \"gpt2-small\", \"seed\": 42, \"checkpoint_source\": \"ioi_size_controlled_baseline\", \"eval_data\": \"IOI 100 prompts seed=42\"}, \"checkpoint_path\": \"/root/min_necessary_circuit_css/bootstrap_ci_size_controlled_results.json\", \"log_path\": \"/root/min_necessary_circuit_css/run_bootstrap_ci_size_controlled.py\", \"conclusion\": \"negative\", \"metrics\": {\"zero_ablation\": {\"css_vs_eapig\": {\"delta\": 0.088, \"ci\": [-0.066, 0.267], \"p\": 0.112, \"sig\": false}, \"css_vs_ep\": {\"delta\": 0.039, \"ci\": [-0.079, 0.147], \"p\": 0.249, \"sig\": false}, \"css_vs_acdc\": {\"delta\": 0, \"ci\": [0, 0], \"p\": 1, \"sig\": false}}, \"mean_ablation\": {\"css_vs_eapig\": {\"delta\": -0.005, \"ci\": [-0.039, 0.023], \"p\": 0.359, \"sig\": false}, \"css_vs_ep\": {\"delta\": -0.006, \"ci\": [-0.032, 0.014], \"p\": 0.279, \"sig\": false}, \"css_vs_acdc\": {\"delta\": 0, \"ci\": [0, 0], \"p\": 1, \"sig\": false}}}, \"completed_at\": \"2026-05-13T16:12:52.449Z\"}, \"hint\": \"💡 建议将本次教训写入 memory.md（什么不 work、为什么）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2479}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-13T16:13:04.359015+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "bootstrap_ci_size_controlled",
  "field": "notes",
  "value": "N=16, 100 prompts, 1000 bootstrap. CSS=1.0 circuit 与 ACDC top-16 完全相同（delta=0）。Zero ablation 下 CSS vs EAP-IG delta=+0.088 (p=0.112), vs EP delta=+0.039 (p=0.249)，均不显著。Mean ablation 下 CSS 略逊于 EAP-IG/EP（delta 为负），也不显著。结论：控制电路大小后 CSS=1.0 无统计显著优势。",
  "project": "min_necessary_circuit_css"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "bootstrap_ci_size_controlled",
    "field": "notes",
    "value": "N=16, 100 prompts, 1000 bootstrap. CSS=1.0 circuit 与 ACDC top-16 完全相同（delta=0）。Zero ablation 下 CSS vs EAP-IG delta=+0.088 (p=0.112), vs EP delta=+0.039 (p=0.249)，均不显著。Mean ablation 下 CSS 略逊于 EAP-IG/EP（delta 为负），也不显著。结论：控制电路大小后 CSS=1.0 无统计显著优势。",
    "project": "min_necessary_circuit_css"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-13T16:13:04.359198+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"bootstrap_ci_size_controlled\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T16:07:41.034Z\", \"updated_at\": \"2026-05-13T16:12:55.945Z\", \"hypothesis\": \"Size-controlled Bootstrap CI (n=1000): CSS=1.0 top-16 vs EAP-IG/EP/ACDC top-16 的 per-prompt CPR delta 统计显著性检验（公平比较，控制电路大小 N=16）\", \"parent\": \"ioi_size_controlled_baseline\", \"spec\": {\"command\": \"python run_bootstrap_ci_size_controlled.py\", \"server\": \"westd-39279\", \"data_path\": \"/root/min_necessary_circuit_css/cache_eap_ig.json\", \"data_count\": 100, \"model_name\": \"gpt2-small\", \"seed\": 42, \"checkpoint_source\": \"ioi_size_controlled_baseline\", \"eval_data\": \"IOI 100 prompts seed=42\"}, \"checkpoint_path\": \"/root/min_necessary_circuit_css/bootstrap_ci_size_controlled_results.json\", \"log_path\": \"/root/min_necessary_circuit_css/run_bootstrap_ci_size_controlled.py\", \"conclusion\": \"negative\", \"metrics\": {\"zero_ablation\": {\"css_vs_eapig\": {\"delta\": 0.088, \"ci\": [-0.066, 0.267], \"p\": 0.112, \"sig\": false}, \"css_vs_ep\": {\"delta\": 0.039, \"ci\": [-0.079, 0.147], \"p\": 0.249, \"sig\": false}, \"css_vs_acdc\": {\"delta\": 0, \"ci\": [0, 0], \"p\": 1, \"sig\": false}}, \"mean_ablation\": {\"css_vs_eapig\": {\"delta\": -0.005, \"ci\": [-0.039, 0.023], \"p\": 0.359, \"sig\": false}, \"css_vs_ep\": {\"delta\": -0.006, \"ci\": [-0.032, 0.014], \"p\": 0.279, \"sig\": false}, \"css_vs_acdc\": {\"delta\": 0, \"ci\": [0, 0], \"p\": 1, \"sig\": false}}}, \"completed_at\": \"2026-05-13T16:12:52.449Z\", \"notes\": \"N=16, 100 prompts, 1000 bootstrap. CSS=1.0 circuit 与 ACDC top-16 完全相同（delta=0）。Zero ablation 下 CSS vs EAP-IG delta=+0.088 (p=0.112), vs EP delta=+0.039 (p=0.249)，均不显著。Mean ablation 下 CSS 略逊于 EAP-IG/EP（delta 为负），也不显著。结论：控制电路大小后 CSS=1.0 无统计显著优势。\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0866}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 75 · 2026-05-13T16:13:04.359410+00:00_

Registry 已更新。汇报结果：

## Bootstrap CI 结果（Size-Controlled, N=16 edges, 1000 bootstrap）

**结论：negative — CSS=1.0 在控制电路大小后无统计显著优势。**

### Zero Ablation

| 比较 | Delta | 95% CI | p-value | 显著 |
|------|-------|--------|---------|------|
| CSS vs EAP-IG | +0.088 | [-0.066, +0.267] | 0.112 | No |
| CSS vs EP | +0.039 | [-0.079, +0.147] | 0.249 | No |
| CSS vs ACDC | 0.000 | [0, 0] | 1.000 | No |

### Mean Ablation

| 比较 | Delta | 95% CI | p-value | 显著 |
|------|-------|--------|---------|------|
| CSS vs EAP-IG | -0.005 | [-0.039, +0.023] | 0.359 | No |
| CSS vs EP | -0.006 | [-0.032, +0.014] | 0.279 | No |
| CSS vs ACDC | 0.000 | [0, 0] | 1.000 | No |

关键发现：
- CSS=1.0 的 16 条边与 ACDC top-16 完全相同（delta=0），说明 CSS=1.0 intersection 恰好是 ACDC 贡献的边集
- Zero ablation 下 CSS 方向正确（正 delta），但 CI 跨零，不显著
- Mean ablation 下 CSS 反而略逊于 EAP-IG/EP，也不显著

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_exp_bootstrap_ci_size_controlled_20260513T160804"
}
```

</details>

---
