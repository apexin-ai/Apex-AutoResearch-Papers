# run 5090c conll t ablation

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 87
- **Recorded user turns:** 0
- **Tool calls:** 43
- **Original source:** `logs/chats/worker_run_5090c_conll_t_ablation_20260520T223840.jsonl`
- **Structured JSON:** [`a478ef5a41ba9e7cb9f1.json`](../../sessions/a4/a478ef5a41ba9e7cb9f1.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

87 recorded events

### Tool call

_source line 1 · 2026-05-20T22:45:00.339801+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__register_artifact",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__register_artifact",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-20T22:45:00.340157+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T22:45:00.340366+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090-c",
  "command": "hostname",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090-c",
    "command": "hostname",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T22:45:00.340512+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'hostname' is not in the read-only allowlist. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T22:45:00.340655+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090-c",
  "command": "hostname && nvidia-smi --query-gpu=index,name,memory.used,utilization.gpu --format=csv,noheader",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090-c",
    "command": "hostname && nvidia-smi --query-gpu=index,name,memory.used,utilization.gpu --format=csv,noheader",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T22:45:00.340785+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"autodl-container-jb1uyxxe0t-1a1cc6c5\\n0, NVIDIA GeForce RTX 5090, 31061 MiB, 99 %\\n1, NVIDIA GeForce RTX 5090, 0 MiB, 0 %\\n2, NVIDIA GeForce RTX 5090, 0 MiB, 0 %\\n3, NVIDIA GeForce RTX 5090, 0 MiB, 0 %\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.63}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T22:45:00.340936+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090-c",
  "command": "find /root/autodl-tmp/struct_self_consist_ie/checkpoints/ -maxdepth 2 -name \"config.json\" 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090-c",
    "command": "find /root/autodl-tmp/struct_self_consist_ie/checkpoints/ -maxdepth 2 -name \"config.json\" 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T22:45:00.341081+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T22:45:00.341239+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090-c",
  "command": "ls /root/autodl-tmp/struct_self_consist_ie/checkpoints/ 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090-c",
    "command": "ls /root/autodl-tmp/struct_self_consist_ie/checkpoints/ 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T22:45:00.341366+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T22:45:00.341495+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090-c",
  "command": "find /root/autodl-tmp/struct_self_consist_ie/code/ -name \"*.py\" 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090-c",
    "command": "find /root/autodl-tmp/struct_self_consist_ie/code/ -name \"*.py\" 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T22:45:00.341616+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T22:45:00.341734+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090-c",
  "command": "find /root/autodl-tmp/struct_self_consist_ie/data/ -name \"*conll*\" 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090-c",
    "command": "find /root/autodl-tmp/struct_self_consist_ie/data/ -name \"*conll*\" 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-20T22:45:00.341851+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T22:45:00.341999+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090-c",
  "command": "ls /root/autodl-tmp/struct_self_consist_ie/checkpoints/ && echo \"---SEPARATOR---\" && find /root/autodl-tmp/struct_self_consist_ie/checkpoints/ -maxdepth 2 -name \"config.json\" && echo \"---SEPARATOR---\" && find /root/autodl-tmp/struct_self_consist_ie/code/ -name \"*.py\" | head -20 && echo \"---SEPARATOR---\" && find /root/autodl-tmp/struct_self_consist_ie/data/ -name \"*conll*\" | head -10 && echo \"---SEPARATOR---\" && find /root/autodl-tmp/struct_self_consist_ie/ -name \"scs_inference.py\" && echo \"---SEPARATOR---\" && find /root/autodl-tmp/struct_self_consist_ie/ -name \"run_mvp_pilot.py\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090-c",
    "command": "ls /root/autodl-tmp/struct_self_consist_ie/checkpoints/ && echo \"---SEPARATOR---\" && find /root/autodl-tmp/struct_self_consist_ie/checkpoints/ -maxdepth 2 -name \"config.json\" && echo \"---SEPARATOR---\" && find /root/autodl-tmp/struct_self_consist_ie/code/ -name \"*.py\" | head -20 && echo \"---SEPARATOR---\" && find /root/autodl-tmp/struct_self_consist_ie/data/ -name \"*conll*\" | head -10 && echo \"---SEPARATOR---\" && find /root/autodl-tmp/struct_self_consist_ie/ -name \"scs_inference.py\" && echo \"---SEPARATOR---\" && find /root/autodl-tmp/struct_self_consist_ie/ -name \"run_mvp_pilot.py\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T22:45:00.342169+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"llama3.1-8b-scierc-lora\\nllama3.1-8b-scierc-merged\\nqwen25-14b-fewnerd-merged-ckpt36000\\nqwen25-14b-fewnerd-merged-final\\nqwen25-14b-fewnerd-qlora-s42\\nqwen25-7b-fewnerd-merged\\nqwen25-7b-fewnerd-qlora-s42\\nqwen25-7b-wnut17-merged\\nqwen25-7b-wnut17-qlora-s42\\nqwen3-8b-conll2003-merged\\nqwen3-8b-fewnerd-exp021-lora\\nqwen3-8b-fewnerd-exp021-merged\\nqwen3-8b-scierc-merged-v2\\n---SEPARATOR---\\n/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-fewnerd-exp021-merged/config.json\\n/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-conll2003-merged/config.json\\n/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-merged-v2/config.json\\n/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen25-7b-wnut17-merged/config.json\\n/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen25-7b-fewnerd-merged/config.json\\n/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen25-14b-fewnerd-merged-ckpt36000/config.json\\n/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen25-14b-fewnerd-merged-final/config.json\\n---SEPARATOR---\\n/root/autodl-tmp/struct_self_consist_ie/code/data_utils.py\\n/root/autodl-tmp/struct_self_consist_ie/code/convert_to_llamafactory.py\\n/root/autodl-tmp/struct_self_consist_ie/code/evaluation.py\\n/root/autodl-tmp/struct_self_consist_ie/code/consistency.py\\n/root/autodl-tmp/struct_self_consist_ie/code/sampling.py\\n/root/autodl-tmp/struct_self_consist_ie/code/run_mvp_pilot.py\\n/root/autodl-tmp/struct_self_consist_ie/code/gate0_eval.py\\n/root/autodl-tmp/struct_self_consist_ie/code/gate0_diagnose.py\\n/root/autodl-tmp/struct_self_consist_ie/code/gate0_realign_eval.py\\n/root/autodl-tmp/struct_self_consist_ie/code/mvp_pilot.py\\n/root/autodl-tmp/struct_self_consist_ie/code/analyze_component_wise_re.py\\n/root/autodl-tmp/struct_self_consist_ie/code/convert_wnut17.py\\n/root/autodl-tmp/struct_self_consist_ie/code/convert_conll2003.py\\n/root/autodl
…[truncated 860 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T22:45:00.342358+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090-c",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python -c \"import vllm; print(vllm.__version__)\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090-c",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python -c \"import vllm; print(vllm.__version__)\"",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-20T22:45:00.342489+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090-c",
  "command": "head -100 /root/autodl-tmp/struct_self_consist_ie/code/run_mvp_pilot.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090-c",
    "command": "head -100 /root/autodl-tmp/struct_self_consist_ie/code/run_mvp_pilot.py",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T22:45:00.342609+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090-c",
  "command": "ls /root/autodl-tmp/struct_self_consist_ie/data/conll2003/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090-c",
    "command": "ls /root/autodl-tmp/struct_self_consist_ie/data/conll2003/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T22:45:00.342732+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0.18.1\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.07}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-20T22:45:00.342927+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"MVP pilot experiment script for structured self-consistency IE.\\n\\nIntegrates data loading, vLLM sampling, consistency scoring, and evaluation\\ninto a single CLI-driven pipeline. Outputs a verdict (PASS/MARGINAL/FAIL)\\nbased on the correlation between structural consistency and per-instance F1.\\n\\\"\\\"\\\"\\n\\nfrom __future__ import annotations\\n\\nimport argparse\\nimport json\\nimport os\\nimport random\\nimport sys\\n\\nimport numpy as np\\n\\nfrom data_utils import load_scierc, load_ace05, load_conll2003, load_wnut17, load_fewnerd\\nfrom sampling import (\\n    VLLMSampler,\\n    run_sampling_pipeline,\\n    save_sampled_results,\\n    load_sampled_results,\\n    realign_spans,\\n    SCIERC_SCHEMA_HINT,\\n    CONLL2003_SCHEMA_HINT,\\n    WNUT17_SCHEMA_HINT,\\n    FEWNERD_SCHEMA_HINT,\\n)\\nfrom consistency import compute_all_consistency_scores\\nfrom evaluation import (\\n    per_instance_f1,\\n    compute_ner_f1,\\n    compute_re_f1,\\n    compute_eae_f1,\\n    spearman_correlation,\\n    kendall_correlation,\\n    compute_auroc,\\n    compute_sample_f1_distribution,\\n)\\n\\n\\ndef parse_args() -> argparse.Namespace:\\n    \\\"\\\"\\\"Parse command-line arguments.\\\"\\\"\\\"\\n    p = argparse.ArgumentParser(description=\\\"MVP pilot for structured self-consistency IE\\\")\\n    p.add_argument(\\\"--model_path\\\", type=str, required=True, help=\\\"Path to the fine-tuned model\\\")\\n    p.add_argument(\\\"--data_dir\\\", type=str, required=True, help=\\\"Dataset directory (SciERC or ACE05)\\\")\\n    p.add_argument(\\\"--dataset\\\", type=str, default=\\\"scierc\\\", choices=[\\\"scierc\\\", \\\"ace05\\\", \\\"conll2003\\\", \\\"wnut17\\\", \\\"fewnerd\\\"],\\n                   help=\\\"Dataset name (default: scierc)\\\")\\n    p.add_argument(\\\"--subtask\\\", type=str, default=\\\"ner\\\", choices=[\\\"ner\\\", \\\"re\\\", \\\"eae\\\", \\\"joint\\\"],\\n                   help=\\
…[truncated 4108 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-20T22:45:00.343087+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"dev.json\\nllmfactory_dev.json\\nllmfactory_train.json\\ntest.json\\ntrain.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.88}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-20T22:45:00.343275+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090-c",
  "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/ | grep -i \"t_ablation\\|temp\\|conll\" | head -20",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090-c",
    "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/ | grep -i \"t_ablation\\|temp\\|conll\" | head -20",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-20T22:45:00.343410+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"exp_conll_seed789\\nexp_conll_seed789.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.73}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T22:45:00.343533+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-20T22:45:00.343653+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T22:45:00.343782+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "struct_self_consist_ie",
  "filters": "{'status': 'RUNNING'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "filters": "{'status': 'RUNNING'}"
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-20T22:45:00.343904+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "struct_self_consist_ie",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "limit": "10"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-20T22:45:00.344047+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp_14b_inference_fewnerd\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-20T14:36:27.954Z\", \"updated_at\": \"2026-05-20T20:42:00.000Z\", \"hypothesis\": \"14B Qwen2.5 inference on FewNERD (N∈{1,2,4,8}): primary dataset should show oracle scaling law F1(N)=a-b*N^(-c) consistent at 14B scale, filling the scaling curve between 7B and 32B. N=16 cut per Director decision.\", \"notes\": \"CORRECTED 2026-05-20T20:42: Reviewer verified PID 230885 still running on 5090-c:cuda:0 (31052 MiB). Previous diagnostic worker incorrectly claimed zero output — actual results in 14b_final_inference/ directory. FewNERD N=1 done (greedy_f1=0.7985), N=2 done, N=4 in progress. SciERC/CoNLL N=1-16 all done. Kill after N=8 mechanism should be active.\"}, \"exp_qwen25_32b_fewnerd\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-19T06:19:25.428Z\", \"updated_at\": \"2026-05-20T07:15:23.641Z\", \"hypothesis\": \"Scaling from Qwen3-8B to Qwen2.5-32B-Instruct with QLoRA fine-tuning on FewNERD will improve structured self-consistency IE performance due to stronger base model capabilities in instruction following and entity recognition.\", \"notes\": \"2026-05-19 11:36 UTC: step 2177/41180 (5.3%), loss 0.0663, ~2.44s/it, ETA ~26h. checkpoint-2000 saved. PID 804438, 4×5090 87-100% util.\", \"metrics\": {\"training_progress\": \"56.9% (23448/41180, checked 07:14 UTC)\", \"epoch\": \"2.84/5.0\", \"loss\": 0.027, \"speed\": \"~2.50s/step\", \"eta\": \"~05-20 20:00-22:00 UTC (train 12h30m remaining + eval pauses)\"}}}, \"count\": 2, \"total\": 2, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5764}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-20T22:45:00.344332+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp_spider_sc_pilot\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T18:41:49.560Z\", \"updated_at\": \"2026-05-20T22:37:08.907Z\", \"hypothesis\": \"SC diagnostic cascade (degeneracy, agreement-correctness correlation, failure mode classification F1-F4) validated on NER structured generation will also manifest in SQL structured generation with GPT-5.5 on Spider-dev (200 examples, N=8, T=1.0), demonstrating cross-task universality. Key adaptation: uses execution-result equivalence (not SQL text) for agreement/degeneracy, since semantically equivalent SQL can have different surface forms.\", \"conclusion\": \"success\", \"metrics\": {\"n_instances\": 196, \"n_target\": 200, \"n_skipped\": 2, \"n_samples\": 8, \"temperature\": 1, \"model\": \"gpt-5.5\", \"greedy_acc\": 0.7653, \"mv_acc\": 0.7704, \"oracle_acc\": 0.8061, \"mv_gain_pp\": 0.51, \"degeneracy_rate\": 0.8724, \"spearman_rho\": 0.5501, \"spearman_p\": 6.77e-17, \"kendall_tau\": 0.5259, \"F1_degeneracy_rate\": 0.872, \"F2_low_agreement_rate\": 0, \"F3_high_agree_wrong_rate\": 0.082, \"F4_selection_gap_rate\": 0, \"sc_success_rate\": 0.046, \"nondegen_n\": 25, \"nondegen_greedy_acc\": 0.32, \"nondegen_mv_acc\": 0.36, \"nondegen_oracle_acc\": 0.64, \"nondegen_spearman_rho\": 0.13}, \"notes\": \"Data quality verified: all 196 instances generated AFTER F2/F3 bugfix (code modified 20:47:22, checkpoint started 20:47:52). Zero mismatch between embedded and recomputed failure modes. F1-F4 distribution: F1=87.2%, F2=0%, F3=8.2%, F4=0%, OK=4.6%. F2=0 means SQL has no low-agreement zone (either degenerate or high consensus). Paper-ready. Note: F4 is dead code in SQL context (greedy_correct AND NOT mv_correct never occurs). Cross-task threshold note: SQL uses agreement<0.5 for F2/F3 split, RE uses kappa<0.3.\"}, \"exp_fewrel_re_sc\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T21:13:10.685Z\", \"updated_at\": \"2026-05-20T22:08:51.973Z\", \"hypot
…[truncated 6745 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-20T22:45:00.344504+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "struct_self_consist_ie",
  "filters": "{'status': 'DONE'}",
  "limit": "20",
  "fields": "['exp_id', 'hypothesis', 'status', 'metrics']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "filters": "{'status': 'DONE'}",
    "limit": "20",
    "fields": "['exp_id', 'hypothesis', 'status', 'metrics']"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-20T22:45:00.344902+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp_spider_sc_pilot\": {\"status\": \"DONE\", \"hypothesis\": \"SC diagnostic cascade (degeneracy, agreement-correctness correlation, failure mode classification F1-F4) validated on NER structured generation will also manifest in SQL structured generation with GPT-5.5 on Spider-dev (200 examples, N=8, T=1.0), demonstrating cross-task universality. Key adaptation: uses execution-result equivalence (not SQL text) for agreement/degeneracy, since semantically equivalent SQL can have different surface forms.\", \"metrics\": {\"n_instances\": 196, \"n_target\": 200, \"n_skipped\": 2, \"n_samples\": 8, \"temperature\": 1, \"model\": \"gpt-5.5\", \"greedy_acc\": 0.7653, \"mv_acc\": 0.7704, \"oracle_acc\": 0.8061, \"mv_gain_pp\": 0.51, \"degeneracy_rate\": 0.8724, \"spearman_rho\": 0.5501, \"spearman_p\": 6.77e-17, \"kendall_tau\": 0.5259, \"F1_degeneracy_rate\": 0.872, \"F2_low_agreement_rate\": 0, \"F3_high_agree_wrong_rate\": 0.082, \"F4_selection_gap_rate\": 0, \"sc_success_rate\": 0.046, \"nondegen_n\": 25, \"nondegen_greedy_acc\": 0.32, \"nondegen_mv_acc\": 0.36, \"nondegen_oracle_acc\": 0.64, \"nondegen_spearman_rho\": 0.13}}, \"exp_fewrel_re_sc\": {\"status\": \"DONE\", \"hypothesis\": \"SC consensus construction improves RE micro-F1 over greedy decoding on FewRel (16 relation types, Wikipedia domain), extending cross-task universality evidence beyond SciERC and DocRED\", \"metrics\": {\"greedy_micro_f1\": 0.0751, \"construction_micro_f1\": 0.0881, \"majority_vote_f1_mean\": 0.0591, \"oracle_f1_mean\": 0.1768, \"fleiss_kappa_mean\": 0.1506, \"soft_jaccard_mean\": 0.3918, \"degeneracy_rate\": 0.0586, \"bootstrap_p_value\": 0.7572, \"failure_modes\": {\"F2_low_agreement\": \"75.8%\", \"F3_high_agreement_low_quality\": \"15.2%\", \"F1_degeneracy\": \"5.9%\", \"none\": \"2.3%\", \"F4_lp_quality_gap\": \"0.8%\"}}}, \"exp_a2_humaneval_sc\": {\"status\": \"DONE\", \"hypothesis\": \"SC failure modes (degeneracy, f
…[truncated 15151 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-20T22:45:00.345108+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "struct_self_consist_ie",
  "limit": "5",
  "filters": "{'hypothesis': 'temperature ablation'}",
  "fields": "['exp_id', 'hypothesis', 'status', 'metrics', 'notes']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "limit": "5",
    "filters": "{'hypothesis': 'temperature ablation'}",
    "fields": "['exp_id', 'hypothesis', 'status', 'metrics', 'notes']"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-20T22:45:00.345297+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.535}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-20T22:45:00.345441+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090-c",
  "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/ | grep -i \"temp\\|ablat\\|t0\\.\\|t1\\.\" | head -20",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090-c",
    "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/ | grep -i \"temp\\|ablat\\|t0\\.\\|t1\\.\" | head -20",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-20T22:45:00.345569+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.73}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-20T22:45:00.345710+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090-c",
  "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/ | head -30",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090-c",
    "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/ | head -30",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-20T22:45:00.345847+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"14b_final_inference\\n7b_ft_signals\\ndocred_re_sc\\nexp_b3_prompted_diversity\\nexp_conll_seed789\\nexp_conll_seed789.log\\nexp_esj_entity_self_judgment\\nexp_esj_entity_self_judgment.log\\nexp_esj_entity_self_judgment_dryrun\\nexp_fewnerd_seed456\\nexp_fewnerd_seed789\\nexp_fewnerd_seed789.log\\nexp_llama_scierc_seed123\\nexp_lsc_latent_sc\\nexp_lsc_latent_sc.log\\nexp_lsc_latent_sc_dryrun\\nexp_mrsc_multi_round\\nexp_mrsc_multi_round.log\\nexp_scierc_seed789_5090c\\nexp_scierc_seed789_5090c.log\\nexp_scierc_t12_seed456\\nexp_scierc_t12_seed456.log\\nexp_tlow_fewnerd_t05_s42\\nexp_tlow_fewnerd_t05_s42.log\\nfewnerd_14b_ckpt36000\\nfewnerd_7b\\nfewrel_re_sc\\nre_sc\\nwnut17\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.74}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-20T22:45:00.345989+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__update_registry",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__update_registry",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-20T22:45:00.346107+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-20T22:45:00.346292+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_conll_t_ablation_t05",
  "field": "hypothesis",
  "value": "CoNLL temperature ablation (T=0.5): test how temperature affects degeneracy rate and SC diagnostic cascade on CoNLL-2003, complementing SciERC and FewNERD T-ablation data to form 3-dataset temperature-degeneracy frontier. N=8, Qwen3-8B-FT, seed=42.",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_conll_t_ablation_t05",
    "field": "hypothesis",
    "value": "CoNLL temperature ablation (T=0.5): test how temperature affects degeneracy rate and SC diagnostic cascade on CoNLL-2003, complementing SciERC and FewNERD T-ablation data to form 3-dataset temperature-degeneracy frontier. N=8, Qwen3-8B-FT, seed=42.",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-20T22:45:00.346431+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_conll_t_ablation_t05\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T22:40:58.068Z\", \"updated_at\": \"2026-05-20T22:40:58.068Z\", \"hypothesis\": \"CoNLL temperature ablation (T=0.5): test how temperature affects degeneracy rate and SC diagnostic cascade on CoNLL-2003, complementing SciERC and FewNERD T-ablation data to form 3-dataset temperature-degeneracy frontier. N=8, Qwen3-8B-FT, seed=42.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9176}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-20T22:45:00.346555+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_conll_t_ablation_t08",
  "field": "hypothesis",
  "value": "CoNLL temperature ablation (T=0.8): test how temperature affects degeneracy rate and SC diagnostic cascade on CoNLL-2003, complementing SciERC and FewNERD T-ablation data to form 3-dataset temperature-degeneracy frontier. N=8, Qwen3-8B-FT, seed=42.",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_conll_t_ablation_t08",
    "field": "hypothesis",
    "value": "CoNLL temperature ablation (T=0.8): test how temperature affects degeneracy rate and SC diagnostic cascade on CoNLL-2003, complementing SciERC and FewNERD T-ablation data to form 3-dataset temperature-degeneracy frontier. N=8, Qwen3-8B-FT, seed=42.",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-20T22:45:00.346690+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_conll_t_ablation_t08\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T22:40:59.474Z\", \"updated_at\": \"2026-05-20T22:40:59.474Z\", \"hypothesis\": \"CoNLL temperature ablation (T=0.8): test how temperature affects degeneracy rate and SC diagnostic cascade on CoNLL-2003, complementing SciERC and FewNERD T-ablation data to form 3-dataset temperature-degeneracy frontier. N=8, Qwen3-8B-FT, seed=42.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.912}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-20T22:45:00.346815+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_conll_t_ablation_t12",
  "field": "hypothesis",
  "value": "CoNLL temperature ablation (T=1.2): test how temperature affects degeneracy rate and SC diagnostic cascade on CoNLL-2003, complementing SciERC and FewNERD T-ablation data to form 3-dataset temperature-degeneracy frontier. N=8, Qwen3-8B-FT, seed=42.",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_conll_t_ablation_t12",
    "field": "hypothesis",
    "value": "CoNLL temperature ablation (T=1.2): test how temperature affects degeneracy rate and SC diagnostic cascade on CoNLL-2003, complementing SciERC and FewNERD T-ablation data to form 3-dataset temperature-degeneracy frontier. N=8, Qwen3-8B-FT, seed=42.",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-20T22:45:00.346988+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_conll_t_ablation_t12\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T22:41:01.169Z\", \"updated_at\": \"2026-05-20T22:41:01.169Z\", \"hypothesis\": \"CoNLL temperature ablation (T=1.2): test how temperature affects degeneracy rate and SC diagnostic cascade on CoNLL-2003, complementing SciERC and FewNERD T-ablation data to form 3-dataset temperature-degeneracy frontier. N=8, Qwen3-8B-FT, seed=42.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.1039}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-20T22:45:00.347203+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090-c",
  "command": "mkdir -p /root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t05_seed42 && cd /root/autodl-tmp/struct_self_consist_ie/code && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=1 nohup python run_mvp_pilot.py --model_path /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-conll2003-merged --data_dir /root/autodl-tmp/struct_self_consist_ie/data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 0.5 --seed 42 --output_dir /root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t05_seed42 --gpu_memory_utilization 0.90 --max_model_len 4096 > /root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t05_seed42.log 2>&1 & echo \"PID=$!\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090-c",
    "command": "mkdir -p /root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t05_seed42 && cd /root/autodl-tmp/struct_self_consist_ie/code && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=1 nohup python run_mvp_pilot.py --model_path /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-conll2003-merged --data_dir /root/autodl-tmp/struct_self_consist_ie/data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 0.5 --seed 42 --output_dir /root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t05_seed42 --gpu_memory_utilization 0.90 --max_model_len 4096 > /root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t05_seed42.log 2>&1 & echo \"PID=$!\"",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-20T22:45:00.347347+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090-c",
  "command": "mkdir -p /root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t08_seed42 && cd /root/autodl-tmp/struct_self_consist_ie/code && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=2 nohup python run_mvp_pilot.py --model_path /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-conll2003-merged --data_dir /root/autodl-tmp/struct_self_consist_ie/data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 0.8 --seed 42 --output_dir /root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t08_seed42 --gpu_memory_utilization 0.90 --max_model_len 4096 > /root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t08_seed42.log 2>&1 & echo \"PID=$!\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090-c",
    "command": "mkdir -p /root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t08_seed42 && cd /root/autodl-tmp/struct_self_consist_ie/code && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=2 nohup python run_mvp_pilot.py --model_path /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-conll2003-merged --data_dir /root/autodl-tmp/struct_self_consist_ie/data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 0.8 --seed 42 --output_dir /root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t08_seed42 --gpu_memory_utilization 0.90 --max_model_len 4096 > /root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t08_seed42.log 2>&1 & echo \"PID=$!\"",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-20T22:45:00.347480+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090-c",
  "command": "mkdir -p /root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t12_seed42 && cd /root/autodl-tmp/struct_self_consist_ie/code && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=3 nohup python run_mvp_pilot.py --model_path /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-conll2003-merged --data_dir /root/autodl-tmp/struct_self_consist_ie/data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 1.2 --seed 42 --output_dir /root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t12_seed42 --gpu_memory_utilization 0.90 --max_model_len 4096 > /root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t12_seed42.log 2>&1 & echo \"PID=$!\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090-c",
    "command": "mkdir -p /root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t12_seed42 && cd /root/autodl-tmp/struct_self_consist_ie/code && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=3 nohup python run_mvp_pilot.py --model_path /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-conll2003-merged --data_dir /root/autodl-tmp/struct_self_consist_ie/data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 1.2 --seed 42 --output_dir /root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t12_seed42 --gpu_memory_utilization 0.90 --max_model_len 4096 > /root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t12_seed42.log 2>&1 & echo \"PID=$!\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-20T22:45:00.347610+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'mkdir -p /root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t05_seed42 && cd /root/autodl-tmp/struct_self_consist_ie/code && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=1 nohup python run_mvp_pilot.py --model_path /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-conll2003-merged --data_dir /root/autodl-tmp/struct_self_consist_ie/data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 0.5 --seed 42 --output_dir /root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t05_seed42 --gpu_memory_utilization 0.90 --max_model_len 4096 > /root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t05_seed42.log 2>&1 & echo \\\"PID=$!\\\"'\\n\\nStdout:\\n\\nPID=242197\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 31.32}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-20T22:45:00.347740+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'mkdir -p /root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t08_seed42 && cd /root/autodl-tmp/struct_self_consist_ie/code && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=2 nohup python run_mvp_pilot.py --model_path /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-conll2003-merged --data_dir /root/autodl-tmp/struct_self_consist_ie/data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 0.8 --seed 42 --output_dir /root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t08_seed42 --gpu_memory_utilization 0.90 --max_model_len 4096 > /root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t08_seed42.log 2>&1 & echo \\\"PID=$!\\\"'\\n\\nStdout:\\n\\nPID=242682\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 32.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-20T22:45:00.347866+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'mkdir -p /root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t12_seed42 && cd /root/autodl-tmp/struct_self_consist_ie/code && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=3 nohup python run_mvp_pilot.py --model_path /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-conll2003-merged --data_dir /root/autodl-tmp/struct_self_consist_ie/data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 1.2 --seed 42 --output_dir /root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t12_seed42 --gpu_memory_utilization 0.90 --max_model_len 4096 > /root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t12_seed42.log 2>&1 & echo \\\"PID=$!\\\"'\\n\\nStdout:\\n\\nPID=243594\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 32.98}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-20T22:45:00.348025+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090-c",
  "command": "nvidia-smi --query-gpu=index,name,memory.used,utilization.gpu --format=csv,noheader && echo \"---\" && ps -p 242197,242682,243594 -o pid,stat,etime,cmd --no-headers 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090-c",
    "command": "nvidia-smi --query-gpu=index,name,memory.used,utilization.gpu --format=csv,noheader && echo \"---\" && ps -p 242197,242682,243594 -o pid,stat,etime,cmd --no-headers 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-20T22:45:00.348191+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, NVIDIA GeForce RTX 5090, 31061 MiB, 98 %\\n1, NVIDIA GeForce RTX 5090, 30053 MiB, 93 %\\n2, NVIDIA GeForce RTX 5090, 30043 MiB, 92 %\\n3, NVIDIA GeForce RTX 5090, 30087 MiB, 90 %\\n---\\n242197 S          01:48 bash -c mkdir -p /root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t05_seed42 && cd /root/autodl-tmp/struct_self_consist_ie/code && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=1 nohup python run_mvp_pilot.py --model_path /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-conll2003-merged --data_dir /root/autodl-tmp/struct_self_consist_ie/data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 0.5 --seed 42 --output_dir /root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t05_seed42 --gpu_memory_utilization 0.90 --max_model_len 4096 > /root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t05_seed42.log 2>&1 & echo \\\"PID=$!\\\"\\n242682 S          01:16 bash -c mkdir -p /root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t08_seed42 && cd /root/autodl-tmp/struct_self_consist_ie/code && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=2 nohup python run_mvp_pilot.py --model_path /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-conll2003-merged --data_dir /root/autodl-tmp/struct_self_consist_ie/data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 0.8 --seed 42 --output_dir /root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t08_seed42 --gpu_memory_utilization 0.90 --max_model_len 4096 > /root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t08_seed42.log 2>&1 & echo \\\"PID=$!\\\"\\n243594 S          00:43 bash -c mkdir -p /root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t12_seed42 && cd /root/autodl-tmp/struct_self_consist_ie/code && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA
…[truncated 621 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-20T22:45:00.348372+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090-c",
  "command": "tail -5 /root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t05_seed42.log && echo \"===T08===\" && tail -5 /root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t08_seed42.log && echo \"===T12===\" && tail -5 /root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t12_seed42.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090-c",
    "command": "tail -5 /root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t05_seed42.log && echo \"===T08===\" && tail -5 /root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t08_seed42.log && echo \"===T12===\" && tail -5 /root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t12_seed42.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-20T22:45:00.348570+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"(EngineCore pid=242475) INFO 05-21 06:42:08 [gpu_worker.py:617] CUDA graph pool memory: 0.4 GiB (actual), 0.36 GiB (estimated), difference: 0.05 GiB (11.7%).\\n(EngineCore pid=242475) INFO 05-21 06:42:08 [core.py:281] init engine (profile, create kv cache, warmup model) took 16.55 seconds\\nINFO 05-21 06:42:09 [llm.py:391] Supported tasks: ['generate']\\n\\rRendering prompts:   0%|          | 0/3453 [00:00<?, ?it/s]\\rRendering prompts:   1%|          | 40/3453 [00:00<00:08, 398.45it/s]\\rRendering prompts:   3%|▎         | 97/3453 [00:00<00:06, 498.81it/s]\\rRendering prompts:   4%|▍         | 154/3453 [00:00<00:06, 529.58it/s]\\rRendering prompts:   6%|▌         | 211/3453 [00:00<00:05, 544.04it/s]\\rRendering prompts:   8%|▊         | 269/3453 [00:00<00:05, 555.33it/s]\\rRendering prompts:   9%|▉         | 325/3453 [00:00<00:05, 551.73it/s]\\rRendering prompts:  11%|█         | 383/3453 [00:00<00:05, 558.59it/s]\\rRendering prompts:  13%|█▎        | 440/3453 [00:00<00:05, 560.99it/s]\\rRendering prompts:  14%|█▍        | 498/3453 [00:00<00:05, 564.70it/s]\\rRendering prompts:  16%|█▌        | 556/3453 [00:01<00:05, 568.65it/s]\\rRendering prompts:  18%|█▊        | 613/3453 [00:01<00:05, 566.56it/s]\\rRendering prompts:  19%|█▉        | 671/3453 [00:01<00:04, 567.72it/s]\\rRendering prompts:  21%|██        | 728/3453 [00:01<00:04, 566.30it/s]\\rRendering prompts:  23%|██▎       | 785/3453 [00:01<00:04, 566.70it/s]\\rRendering prompts:  24%|██▍       | 842/3453 [00:01<00:04, 564.46it/s]\\rRendering prompts:  26%|██▌       | 899/3453 [00:01<00:04, 560.92it/s]\\rRendering prompts:  28%|██▊       | 956/3453 [00:01<00:04, 557.15it/s]\\rRendering prompts:  29%|██▉       | 1013/3453 [00:01<00:04, 559.08it/s]\\rRendering prompts:  31%|███       | 1069/3453 [00:01<00:04, 557.95it/s]\\rRendering prompts:  33%|███▎      | 1126/3453 [00:02<00:04, 561.27it/s]\\rRendering prompts:  34%|███▍      | 1183/3453 [00:02<00:04, 5
…[truncated 6374 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-20T22:45:00.348722+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_conll_t_ablation_t05",
  "field": "status",
  "value": "RUNNING",
  "project": "struct_self_consist_ie",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=1 python run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 0.5 --seed 42 --output_dir output/exp_conll_t05_seed42', 'server': 'autodl-5090-c', 'data_path': '/root/autodl-tmp/struct_self_consist_ie/data/conll2003', 'data_count': 2756, 'model_name': 'qwen3-8b-conll2003-merged', 'seed': 42, 'pid': 242197, 'gpu': 'cuda:1', 'log_path': '/root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t05_seed42.log', 'checkpoint_path': '/root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t05_seed42'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_conll_t_ablation_t05",
    "field": "status",
    "value": "RUNNING",
    "project": "struct_self_consist_ie",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=1 python run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 0.5 --seed 42 --output_dir output/exp_conll_t05_seed42', 'server': 'autodl-5090-c', 'data_path': '/root/autodl-tmp/struct_self_consist_ie/data/conll2003', 'data_count': 2756, 'model_name': 'qwen3-8b-conll2003-merged', 'seed': 42, 'pid': 242197, 'gpu': 'cuda:1', 'log_path': '/root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t05_seed42.log', 'checkpoint_path': '/root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t05_seed42'}"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-20T22:45:00.348868+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.5361}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-20T22:45:00.348995+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_conll_t_ablation_t08",
  "field": "status",
  "value": "RUNNING",
  "project": "struct_self_consist_ie",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=2 python run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 0.8 --seed 42 --output_dir output/exp_conll_t08_seed42', 'server': 'autodl-5090-c', 'data_path': '/root/autodl-tmp/struct_self_consist_ie/data/conll2003', 'data_count': 2756, 'model_name': 'qwen3-8b-conll2003-merged', 'seed': 42, 'pid': 242682, 'gpu': 'cuda:2', 'log_path': '/root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t08_seed42.log', 'checkpoint_path': '/root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t08_seed42'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_conll_t_ablation_t08",
    "field": "status",
    "value": "RUNNING",
    "project": "struct_self_consist_ie",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=2 python run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 0.8 --seed 42 --output_dir output/exp_conll_t08_seed42', 'server': 'autodl-5090-c', 'data_path': '/root/autodl-tmp/struct_self_consist_ie/data/conll2003', 'data_count': 2756, 'model_name': 'qwen3-8b-conll2003-merged', 'seed': 42, 'pid': 242682, 'gpu': 'cuda:2', 'log_path': '/root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t08_seed42.log', 'checkpoint_path': '/root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t08_seed42'}"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-20T22:45:00.349169+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.5379}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-20T22:45:00.349306+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_conll_t_ablation_t12",
  "field": "status",
  "value": "RUNNING",
  "project": "struct_self_consist_ie",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=3 python run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 1.2 --seed 42 --output_dir output/exp_conll_t12_seed42', 'server': 'autodl-5090-c', 'data_path': '/root/autodl-tmp/struct_self_consist_ie/data/conll2003', 'data_count': 2756, 'model_name': 'qwen3-8b-conll2003-merged', 'seed': 42, 'pid': 243594, 'gpu': 'cuda:3', 'log_path': '/root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t12_seed42.log', 'checkpoint_path': '/root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t12_seed42'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_conll_t_ablation_t12",
    "field": "status",
    "value": "RUNNING",
    "project": "struct_self_consist_ie",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=3 python run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 1.2 --seed 42 --output_dir output/exp_conll_t12_seed42', 'server': 'autodl-5090-c', 'data_path': '/root/autodl-tmp/struct_self_consist_ie/data/conll2003', 'data_count': 2756, 'model_name': 'qwen3-8b-conll2003-merged', 'seed': 42, 'pid': 243594, 'gpu': 'cuda:3', 'log_path': '/root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t12_seed42.log', 'checkpoint_path': '/root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t12_seed42'}"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-20T22:45:00.349445+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.5951}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-20T22:45:00.349601+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_conll_t_ablation_t05",
  "field": "status",
  "value": "PENDING",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_conll_t_ablation_t05",
    "field": "status",
    "value": "PENDING",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-20T22:45:00.349724+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_conll_t_ablation_t08",
  "field": "status",
  "value": "PENDING",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_conll_t_ablation_t08",
    "field": "status",
    "value": "PENDING",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-20T22:45:00.349850+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_conll_t_ablation_t05\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T22:40:58.068Z\", \"updated_at\": \"2026-05-20T22:43:57.849Z\", \"hypothesis\": \"CoNLL temperature ablation (T=0.5): test how temperature affects degeneracy rate and SC diagnostic cascade on CoNLL-2003, complementing SciERC and FewNERD T-ablation data to form 3-dataset temperature-degeneracy frontier. N=8, Qwen3-8B-FT, seed=42.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.4465}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-20T22:45:00.349977+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_conll_t_ablation_t12",
  "field": "status",
  "value": "PENDING",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_conll_t_ablation_t12",
    "field": "status",
    "value": "PENDING",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-20T22:45:00.350102+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_conll_t_ablation_t08\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T22:40:59.474Z\", \"updated_at\": \"2026-05-20T22:44:00.276Z\", \"hypothesis\": \"CoNLL temperature ablation (T=0.8): test how temperature affects degeneracy rate and SC diagnostic cascade on CoNLL-2003, complementing SciERC and FewNERD T-ablation data to form 3-dataset temperature-degeneracy frontier. N=8, Qwen3-8B-FT, seed=42.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.4824}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-20T22:45:00.350248+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_conll_t_ablation_t12\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T22:41:01.169Z\", \"updated_at\": \"2026-05-20T22:44:02.767Z\", \"hypothesis\": \"CoNLL temperature ablation (T=1.2): test how temperature affects degeneracy rate and SC diagnostic cascade on CoNLL-2003, complementing SciERC and FewNERD T-ablation data to form 3-dataset temperature-degeneracy frontier. N=8, Qwen3-8B-FT, seed=42.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.3727}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-20T22:45:00.350370+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_conll_t_ablation_t05",
  "field": "status",
  "value": "RUNNING",
  "project": "struct_self_consist_ie",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=1 python run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 0.5 --seed 42 --output_dir output/exp_conll_t05_seed42', 'server': 'autodl-5090-c', 'data_path': '/root/autodl-tmp/struct_self_consist_ie/data/conll2003', 'data_count': 2756, 'model_name': 'qwen3-8b-conll2003-merged', 'seed': 42, 'pid': 242197, 'gpu': 'cuda:1', 'log_path': '/root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t05_seed42.log', 'checkpoint_path': '/root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t05_seed42'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_conll_t_ablation_t05",
    "field": "status",
    "value": "RUNNING",
    "project": "struct_self_consist_ie",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=1 python run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 0.5 --seed 42 --output_dir output/exp_conll_t05_seed42', 'server': 'autodl-5090-c', 'data_path': '/root/autodl-tmp/struct_self_consist_ie/data/conll2003', 'data_count': 2756, 'model_name': 'qwen3-8b-conll2003-merged', 'seed': 42, 'pid': 242197, 'gpu': 'cuda:1', 'log_path': '/root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t05_seed42.log', 'checkpoint_path': '/root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t05_seed42'}"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-20T22:45:00.350507+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PENDING → RUNNING. Allowed: ['DONE', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.5568}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-20T22:45:00.350630+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_conll_t_ablation_t08",
  "field": "status",
  "value": "RUNNING",
  "project": "struct_self_consist_ie",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=2 python run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 0.8 --seed 42 --output_dir output/exp_conll_t08_seed42', 'server': 'autodl-5090-c', 'data_path': '/root/autodl-tmp/struct_self_consist_ie/data/conll2003', 'data_count': 2756, 'model_name': 'qwen3-8b-conll2003-merged', 'seed': 42, 'pid': 242682, 'gpu': 'cuda:2', 'log_path': '/root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t08_seed42.log', 'checkpoint_path': '/root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t08_seed42'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_conll_t_ablation_t08",
    "field": "status",
    "value": "RUNNING",
    "project": "struct_self_consist_ie",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=2 python run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 0.8 --seed 42 --output_dir output/exp_conll_t08_seed42', 'server': 'autodl-5090-c', 'data_path': '/root/autodl-tmp/struct_self_consist_ie/data/conll2003', 'data_count': 2756, 'model_name': 'qwen3-8b-conll2003-merged', 'seed': 42, 'pid': 242682, 'gpu': 'cuda:2', 'log_path': '/root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t08_seed42.log', 'checkpoint_path': '/root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t08_seed42'}"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-20T22:45:00.350772+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PENDING → RUNNING. Allowed: ['DONE', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.5448}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-20T22:45:00.350897+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_conll_t_ablation_t12",
  "field": "status",
  "value": "RUNNING",
  "project": "struct_self_consist_ie",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=3 python run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 1.2 --seed 42 --output_dir output/exp_conll_t12_seed42', 'server': 'autodl-5090-c', 'data_path': '/root/autodl-tmp/struct_self_consist_ie/data/conll2003', 'data_count': 2756, 'model_name': 'qwen3-8b-conll2003-merged', 'seed': 42, 'pid': 243594, 'gpu': 'cuda:3', 'log_path': '/root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t12_seed42.log', 'checkpoint_path': '/root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t12_seed42'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_conll_t_ablation_t12",
    "field": "status",
    "value": "RUNNING",
    "project": "struct_self_consist_ie",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=3 python run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 1.2 --seed 42 --output_dir output/exp_conll_t12_seed42', 'server': 'autodl-5090-c', 'data_path': '/root/autodl-tmp/struct_self_consist_ie/data/conll2003', 'data_count': 2756, 'model_name': 'qwen3-8b-conll2003-merged', 'seed': 42, 'pid': 243594, 'gpu': 'cuda:3', 'log_path': '/root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t12_seed42.log', 'checkpoint_path': '/root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t12_seed42'}"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-20T22:45:00.351030+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PENDING → RUNNING. Allowed: ['DONE', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.6173}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-20T22:45:00.351183+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_conll_t_ablation_t05",
  "field": "status",
  "value": "QUEUED",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_conll_t_ablation_t05",
    "field": "status",
    "value": "QUEUED",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-20T22:45:00.351309+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_conll_t_ablation_t08",
  "field": "status",
  "value": "QUEUED",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_conll_t_ablation_t08",
    "field": "status",
    "value": "QUEUED",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-20T22:45:00.351423+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_conll_t_ablation_t12",
  "field": "status",
  "value": "QUEUED",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_conll_t_ablation_t12",
    "field": "status",
    "value": "QUEUED",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-20T22:45:00.351545+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_conll_t_ablation_t05\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-20T22:40:58.068Z\", \"updated_at\": \"2026-05-20T22:44:26.366Z\", \"hypothesis\": \"CoNLL temperature ablation (T=0.5): test how temperature affects degeneracy rate and SC diagnostic cascade on CoNLL-2003, complementing SciERC and FewNERD T-ablation data to form 3-dataset temperature-degeneracy frontier. N=8, Qwen3-8B-FT, seed=42.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.427}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-20T22:45:00.351676+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_conll_t_ablation_t08\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-20T22:40:59.474Z\", \"updated_at\": \"2026-05-20T22:44:28.789Z\", \"hypothesis\": \"CoNLL temperature ablation (T=0.8): test how temperature affects degeneracy rate and SC diagnostic cascade on CoNLL-2003, complementing SciERC and FewNERD T-ablation data to form 3-dataset temperature-degeneracy frontier. N=8, Qwen3-8B-FT, seed=42.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.3736}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-20T22:45:00.351800+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_conll_t_ablation_t12\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-20T22:41:01.169Z\", \"updated_at\": \"2026-05-20T22:44:31.171Z\", \"hypothesis\": \"CoNLL temperature ablation (T=1.2): test how temperature affects degeneracy rate and SC diagnostic cascade on CoNLL-2003, complementing SciERC and FewNERD T-ablation data to form 3-dataset temperature-degeneracy frontier. N=8, Qwen3-8B-FT, seed=42.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.4832}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-20T22:45:00.351919+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_conll_t_ablation_t05",
  "field": "status",
  "value": "RUNNING",
  "project": "struct_self_consist_ie",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=1 python run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 0.5 --seed 42 --output_dir output/exp_conll_t05_seed42', 'server': 'autodl-5090-c', 'data_path': '/root/autodl-tmp/struct_self_consist_ie/data/conll2003', 'data_count': 2756, 'model_name': 'qwen3-8b-conll2003-merged', 'seed': 42, 'pid': 242197, 'gpu': 'cuda:1', 'log_path': '/root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t05_seed42.log', 'checkpoint_path': '/root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t05_seed42'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_conll_t_ablation_t05",
    "field": "status",
    "value": "RUNNING",
    "project": "struct_self_consist_ie",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=1 python run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 0.5 --seed 42 --output_dir output/exp_conll_t05_seed42', 'server': 'autodl-5090-c', 'data_path': '/root/autodl-tmp/struct_self_consist_ie/data/conll2003', 'data_count': 2756, 'model_name': 'qwen3-8b-conll2003-merged', 'seed': 42, 'pid': 242197, 'gpu': 'cuda:1', 'log_path': '/root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t05_seed42.log', 'checkpoint_path': '/root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t05_seed42'}"
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-20T22:45:00.352065+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_conll_t_ablation_t05\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T22:40:58.068Z\", \"updated_at\": \"2026-05-20T22:44:41.854Z\", \"hypothesis\": \"CoNLL temperature ablation (T=0.5): test how temperature affects degeneracy rate and SC diagnostic cascade on CoNLL-2003, complementing SciERC and FewNERD T-ablation data to form 3-dataset temperature-degeneracy frontier. N=8, Qwen3-8B-FT, seed=42.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 0.5 --seed 42 --output_dir output/exp_conll_t05_seed42\", \"server\": \"autodl-5090-c\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/conll2003\", \"data_count\": 2756, \"model_name\": \"qwen3-8b-conll2003-merged\", \"seed\": 42, \"pid\": 242197, \"gpu\": \"cuda:1\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t05_seed42.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t05_seed42\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.3939}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-20T22:45:00.352219+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_conll_t_ablation_t08",
  "field": "status",
  "value": "RUNNING",
  "project": "struct_self_consist_ie",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=2 python run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 0.8 --seed 42 --output_dir output/exp_conll_t08_seed42', 'server': 'autodl-5090-c', 'data_path': '/root/autodl-tmp/struct_self_consist_ie/data/conll2003', 'data_count': 2756, 'model_name': 'qwen3-8b-conll2003-merged', 'seed': 42, 'pid': 242682, 'gpu': 'cuda:2', 'log_path': '/root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t08_seed42.log', 'checkpoint_path': '/root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t08_seed42'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_conll_t_ablation_t08",
    "field": "status",
    "value": "RUNNING",
    "project": "struct_self_consist_ie",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=2 python run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 0.8 --seed 42 --output_dir output/exp_conll_t08_seed42', 'server': 'autodl-5090-c', 'data_path': '/root/autodl-tmp/struct_self_consist_ie/data/conll2003', 'data_count': 2756, 'model_name': 'qwen3-8b-conll2003-merged', 'seed': 42, 'pid': 242682, 'gpu': 'cuda:2', 'log_path': '/root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t08_seed42.log', 'checkpoint_path': '/root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t08_seed42'}"
  }
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-20T22:45:00.352360+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_conll_t_ablation_t12",
  "field": "status",
  "value": "RUNNING",
  "project": "struct_self_consist_ie",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=3 python run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 1.2 --seed 42 --output_dir output/exp_conll_t12_seed42', 'server': 'autodl-5090-c', 'data_path': '/root/autodl-tmp/struct_self_consist_ie/data/conll2003', 'data_count': 2756, 'model_name': 'qwen3-8b-conll2003-merged', 'seed': 42, 'pid': 243594, 'gpu': 'cuda:3', 'log_path': '/root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t12_seed42.log', 'checkpoint_path': '/root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t12_seed42'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_conll_t_ablation_t12",
    "field": "status",
    "value": "RUNNING",
    "project": "struct_self_consist_ie",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=3 python run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 1.2 --seed 42 --output_dir output/exp_conll_t12_seed42', 'server': 'autodl-5090-c', 'data_path': '/root/autodl-tmp/struct_self_consist_ie/data/conll2003', 'data_count': 2756, 'model_name': 'qwen3-8b-conll2003-merged', 'seed': 42, 'pid': 243594, 'gpu': 'cuda:3', 'log_path': '/root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t12_seed42.log', 'checkpoint_path': '/root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t12_seed42'}"
  }
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-20T22:45:00.352505+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_conll_t_ablation_t08\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T22:40:59.474Z\", \"updated_at\": \"2026-05-20T22:44:44.972Z\", \"hypothesis\": \"CoNLL temperature ablation (T=0.8): test how temperature affects degeneracy rate and SC diagnostic cascade on CoNLL-2003, complementing SciERC and FewNERD T-ablation data to form 3-dataset temperature-degeneracy frontier. N=8, Qwen3-8B-FT, seed=42.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 0.8 --seed 42 --output_dir output/exp_conll_t08_seed42\", \"server\": \"autodl-5090-c\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/conll2003\", \"data_count\": 2756, \"model_name\": \"qwen3-8b-conll2003-merged\", \"seed\": 42, \"pid\": 242682, \"gpu\": \"cuda:2\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t08_seed42.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t08_seed42\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.6796}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-20T22:45:00.352643+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_conll_t_ablation_t12\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T22:41:01.169Z\", \"updated_at\": \"2026-05-20T22:44:48.411Z\", \"hypothesis\": \"CoNLL temperature ablation (T=1.2): test how temperature affects degeneracy rate and SC diagnostic cascade on CoNLL-2003, complementing SciERC and FewNERD T-ablation data to form 3-dataset temperature-degeneracy frontier. N=8, Qwen3-8B-FT, seed=42.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 1.2 --seed 42 --output_dir output/exp_conll_t12_seed42\", \"server\": \"autodl-5090-c\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/conll2003\", \"data_count\": 2756, \"model_name\": \"qwen3-8b-conll2003-merged\", \"seed\": 42, \"pid\": 243594, \"gpu\": \"cuda:3\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t12_seed42.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t12_seed42\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.3923}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 87 · 2026-05-20T22:45:00.352814+00:00_

3 个 CoNLL T-ablation 实验全部启动成功，registry 已更新为 RUNNING。

**汇总：**

| 实验 | GPU | PID | 温度 | Registry ID |
|------|-----|-----|------|-------------|
| T=0.5 | cuda:1 (30GB) | 242197 | 0.5 | `exp_conll_t_ablation_t05` |
| T=0.8 | cuda:2 (30GB) | 242682 | 0.8 | `exp_conll_t_ablation_t08` |
| T=1.2 | cuda:3 (30GB) | 243594 | 1.2 | `exp_conll_t_ablation_t12` |

- cuda:0 未触碰（14B 推理 PID 230885 正常运行，31GB/98%）
- 模型：`qwen3-8b-conll2003-merged`，N=8，seed=42
- 总 prompts：27624（3453 test instances × 8 samples），推理速度 ~5500 toks/s，预计 ~30-50 分钟完成
- 日志路径：`/root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t{05,08,12}_seed42.log`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_run_5090c_conll_t_ablation_20260520T223840"
}
```

</details>

---
