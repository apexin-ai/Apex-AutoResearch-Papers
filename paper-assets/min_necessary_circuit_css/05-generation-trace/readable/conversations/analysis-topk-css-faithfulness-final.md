# analysis topk css faithfulness final

**Transformer Model EAP-IG** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 79
- **Recorded user turns:** 0
- **Tool calls:** 39
- **Original source:** `logs/chats/worker_analysis_topk-css-faithfulness-final_20260513T042218.jsonl`
- **Structured JSON:** [`f72f0cb8623bd85786fd.json`](../../sessions/f7/f72f0cb8623bd85786fd.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

79 recorded events

### Tool call

_source line 1 · 2026-05-13T04:34:16.004963+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-13T04:34:16.005341+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-13T04:34:16.005549+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/structfuse-context/evaluation.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/structfuse-context/evaluation.py",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-13T04:34:16.005684+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/structfuse-context/eval_faithfulness.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/structfuse-context/eval_faithfulness.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-13T04:34:16.005911+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"import os\\nos.environ.setdefault(\\\"CUDA_VISIBLE_DEVICES\\\", \\\"5\\\")\\n\\n\\\"\\\"\\\"Circuit faithfulness evaluation via node-level zero ablation.\\\"\\\"\\\"\\n\\nimport re\\nfrom typing import Dict, Set, List, Any\\nfrom dataclasses import dataclass\\nfrom functools import partial\\n\\nimport torch\\n\\n\\n@dataclass\\nclass CircuitEvalResult:\\n    name: str\\n    num_edges: int\\n    cpr: float\\n    cmd: float\\n\\n    def to_dict(self) -> Dict[str, Any]:\\n        return {\\n            \\\"name\\\": self.name,\\n            \\\"num_edges\\\": self.num_edges,\\n            \\\"cpr\\\": round(self.cpr, 4),\\n            \\\"cmd\\\": round(self.cmd, 4),\\n        }\\n\\n\\ndef _extract_circuit_nodes(circuit_edges: Set[str]) -> Set[str]:\\n    \\\"\\\"\\\"Extract unique node names from edge set.\\\"\\\"\\\"\\n    nodes = set()\\n    for edge in circuit_edges:\\n        parts = edge.split('->')\\n        if len(parts) != 2:\\n            continue\\n        src = parts[0].strip()\\n        dst = parts[1].strip()\\n        nodes.add(src)\\n        dst_base = re.sub(r'\\\\.[qkv]$', '', dst)\\n        nodes.add(dst_base)\\n    nodes.discard('input')\\n    nodes.discard('logits')\\n    return nodes\\n\\n\\ndef _parse_node(node_name: str):\\n    \\\"\\\"\\\"Parse node name into (type, layer, head). Returns None if unparseable.\\\"\\\"\\\"\\n    m = re.match(r'a(\\\\d+)\\\\.h(\\\\d+)', node_name)\\n    if m:\\n        return ('attn', int(m.group(1)), int(m.group(2)))\\n    m = re.match(r'm(\\\\d+)', node_name)\\n    if m:\\n        return ('mlp', int(m.group(1)), None)\\n    return None\\n\\n\\ndef _head_ablation_hook(value, hook, heads_to_ablate):\\n    for h in heads_to_ablate:\\n        value[:, :, h, :] = 0\\n    return value\\n\\n\\ndef _mlp_ablation_hook(value, hook):\\n    return torch.zeros_like(value)\\n\\n\\ndef evaluate_circuit(model, circuit_edges: Set[str], clean_tokens, io_ids, s_ids) -> Circuit
…[truncated 2901 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-13T04:34:16.006079+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/structfuse-context/run_phase_d_only.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/structfuse-context/run_phase_d_only.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-13T04:34:16.006364+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"import os\\nos.environ[\\\"CUDA_VISIBLE_DEVICES\\\"] = \\\"5\\\"\\n\\nimport json, math, random\\nimport torch\\nfrom pathlib import Path\\n\\n# Load model\\nfrom transformer_lens import HookedTransformer\\nfrom transformers import AutoModelForCausalLM\\n\\nlocal_path = \\\"/root/autodl-tmp/gpt2-small\\\"\\nhf_model = AutoModelForCausalLM.from_pretrained(local_path)\\nmodel = HookedTransformer.from_pretrained(\\\"gpt2-small\\\", hf_model=hf_model, device=\\\"cuda\\\")\\nmodel.set_use_attn_result(True)\\nmodel.set_use_split_qkv_input(True)\\nmodel.set_use_hook_mlp_in(True)\\nprint(\\\"Model loaded\\\")\\n\\n# Generate IOI dataset\\nNAMES = [\\\"John\\\", \\\"Mary\\\", \\\"Alice\\\", \\\"Bob\\\", \\\"Charlie\\\", \\\"David\\\", \\\"Emma\\\", \\\"Frank\\\",\\n         \\\"Grace\\\", \\\"Henry\\\", \\\"Jack\\\", \\\"Kate\\\", \\\"Leo\\\", \\\"Mia\\\", \\\"Noah\\\", \\\"Tom\\\"]\\nTEMPLATES = [\\n    \\\"When {io} and {s} went to the {place}, {s} gave a {obj} to\\\",\\n    \\\"After {io} and {s} arrived at the {place}, {s} handed a {obj} to\\\",\\n    \\\"{io} and {s} were at the {place}. {s} gave a {obj} to\\\",\\n    \\\"Then, {io} and {s} had a meeting at the {place}, {s} passed a {obj} to\\\",\\n]\\nPLACES = [\\\"store\\\", \\\"park\\\", \\\"library\\\", \\\"school\\\", \\\"hospital\\\", \\\"restaurant\\\", \\\"office\\\"]\\nOBJECTS = [\\\"bottle\\\", \\\"book\\\", \\\"letter\\\", \\\"ball\\\", \\\"gift\\\", \\\"toy\\\", \\\"bag\\\"]\\n\\nrandom.seed(42)\\nprompts, labels = [], []\\nfor _ in range(50):\\n    io_name, s_name = random.sample(NAMES, 2)\\n    tmpl = random.choice(TEMPLATES)\\n    place, obj = random.choice(PLACES), random.choice(OBJECTS)\\n    prompts.append(tmpl.format(io=io_name, s=s_name, place=place, obj=obj))\\n    io_tok = model.to_tokens(\\\" \\\" + io_name, prepend_bos=False)[0, 0].item()\\n    s_tok = model.to_tokens(\\\" \\\" + s_name, prepend_bos=False)[0, 0].item()\\n    labels.append((i
…[truncated 4839 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-13T04:34:16.006532+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls /root/structfuse-context/eval_mean_ablation.py 2>/dev/null && cat /root/structfuse-context/eval_mean_ablation.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls /root/structfuse-context/eval_mean_ablation.py 2>/dev/null && cat /root/structfuse-context/eval_mean_ablation.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-13T04:34:16.006777+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Phase D only: evaluate circuits using cached Phase A-C results.\\n\\nFix: monkeypatch all HF from_pretrained calls to redirect \\\"gpt2\\\" to local path.\\n\\\"\\\"\\\"\\nimport os\\nos.environ[\\\"CUDA_VISIBLE_DEVICES\\\"] = \\\"5\\\"\\n\\nimport json\\nimport random\\nimport math\\nfrom pathlib import Path\\nfrom typing import Dict, Set\\nimport torch\\nimport numpy as np\\n\\nLOCAL_GPT2 = \\\"/root/autodl-tmp/gpt2-small\\\"\\nGPT2_ALIASES = (\\\"gpt2\\\", \\\"gpt2-small\\\", \\\"openai-community/gpt2\\\")\\n\\n# Monkeypatch all HF Auto*.from_pretrained to redirect gpt2 -> local path\\nfrom transformers import AutoConfig, AutoTokenizer, AutoModelForCausalLM\\n\\ndef _make_patched(orig_fn):\\n    def patched(pretrained_model_name_or_path, *args, **kwargs):\\n        if pretrained_model_name_or_path in GPT2_ALIASES:\\n            pretrained_model_name_or_path = LOCAL_GPT2\\n        return orig_fn(pretrained_model_name_or_path, *args, **kwargs)\\n    return patched\\n\\nAutoConfig.from_pretrained = staticmethod(_make_patched(AutoConfig.from_pretrained))\\nAutoTokenizer.from_pretrained = staticmethod(_make_patched(AutoTokenizer.from_pretrained))\\n\\n# IOI data generation (matches run_mvp.py exactly)\\nNAMES = [\\\"John\\\", \\\"Mary\\\", \\\"Alice\\\", \\\"Bob\\\", \\\"Charlie\\\", \\\"David\\\", \\\"Emma\\\", \\\"Frank\\\",\\n         \\\"Grace\\\", \\\"Henry\\\", \\\"Jack\\\", \\\"Kate\\\", \\\"Leo\\\", \\\"Mia\\\", \\\"Noah\\\", \\\"Tom\\\"]\\nTEMPLATES = [\\n    \\\"When {io} and {s} went to the {place}, {s} gave a {obj} to\\\",\\n    \\\"After {io} and {s} arrived at the {place}, {s} handed a {obj} to\\\",\\n    \\\"{io} and {s} were at the {place}. {s} gave a {obj} to\\\",\\n    \\\"Then, {io} and {s} had a meeting at the {place}, {s} passed a {obj} to\\\",\\n]\\nPLACES = [\\\"store\\\", \\\"park\\\", \\\"library\\\", \\\"school\\\", \\\"hospital\\\", \\\"restaurant\\\", \\\"office\\\"]\\nOBJE
…[truncated 6308 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-13T04:34:16.006952+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '&&' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-13T04:34:16.007091+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/structfuse-context/eval_mean_ablation.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/structfuse-context/eval_mean_ablation.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-13T04:34:16.007404+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"import os\\nos.environ[\\\"CUDA_VISIBLE_DEVICES\\\"] = \\\"5\\\"\\n\\n\\\"\\\"\\\"Mean ablation faithfulness evaluation for Arithmetic (Greaterthan) task.\\n\\nCompares zero ablation vs mean ablation to check if negative CPR\\nis an artifact of overly harsh zero ablation.\\n\\\"\\\"\\\"\\n\\nimport json\\nimport math\\nimport random\\nimport re\\nimport sys\\nfrom pathlib import Path\\nfrom functools import partial\\n\\nimport torch\\nimport numpy as np\\n\\nsys.path.insert(0, \\\"/root/structfuse-context\\\")\\n\\n_LOCAL_GPT2 = \\\"/root/autodl-tmp/gpt2-small\\\"\\n_GPT2_ALIASES = (\\\"gpt2\\\", \\\"gpt2-small\\\", \\\"openai-community/gpt2\\\")\\n\\ndef _patch_hf():\\n    from transformers import AutoConfig, AutoTokenizer, AutoModelForCausalLM\\n    def _make_patched(orig_fn):\\n        def patched(name_or_path, *args, **kwargs):\\n            if name_or_path in _GPT2_ALIASES:\\n                name_or_path = _LOCAL_GPT2\\n            return orig_fn(name_or_path, *args, **kwargs)\\n        return patched\\n    AutoConfig.from_pretrained = staticmethod(_make_patched(AutoConfig.from_pretrained))\\n    AutoTokenizer.from_pretrained = staticmethod(_make_patched(AutoTokenizer.from_pretrained))\\n    AutoModelForCausalLM.from_pretrained = staticmethod(_make_patched(AutoModelForCausalLM.from_pretrained))\\n\\n_patch_hf()\\n\\nGT_DATASET_PATH = \\\"/root/miniconda3/lib/python3.12/site-packages/datasets/greaterthan_gpt2-small_prompts.json\\\"\\n\\n\\ndef _precompute_year_tokens(tokenizer):\\n    tokens = {}\\n    for yr in range(100):\\n        s = f\\\"{yr:02d}\\\"\\n        ids = tokenizer.encode(s)\\n        tokens[s] = ids[0]\\n    return tokens\\n\\n\\ndef load_gt_data(tokenizer, num_samples=100, seed=42):\\n    with open(GT_DATASET_PATH) as f:\\n        all_prompts = json.load(f)[\\\"prompts\\\"]\\n    random.seed(seed)\\n    if len(all_prompts) > num_samples:\\n        all_prompts = random.sample(all_prompts, n
…[truncated 7179 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-13T04:34:16.007601+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls -la /root/structfuse-context/cache_*.json /root/structfuse-context/*results*.json /root/structfuse-context/*faithfulness*.json /root/structfuse-context/*topk*.json /root/structfuse-context/*sweep*.json 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls -la /root/structfuse-context/cache_*.json /root/structfuse-context/*results*.json /root/structfuse-context/*faithfulness*.json /root/structfuse-context/*topk*.json /root/structfuse-context/*sweep*.json 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-13T04:34:16.007787+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-13T04:34:16.007923+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/structfuse-context/topk_sweep_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/structfuse-context/topk_sweep_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-13T04:34:16.008047+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"cat: /root/structfuse-context/topk_sweep_results.json: No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-13T04:34:16.008193+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep -n \"def evaluate_circuit\\|def collect_mean\\|ablation_mode\\|attn_means\\|mlp_means\\|heads_to_ablate\\|hook_result\\|hook_mlp_out\\|baseline_diff\\|circuit_diff\\|cpr\\|cmd\\|def _head\\|def _mlp\\|io_ids\\|s_ids\\|ans_list\\|wrong_list\\|logit_diff\\|ans_logit\\|wrong_logit\" /root/structfuse-context/eval_mean_ablation.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep -n \"def evaluate_circuit\\|def collect_mean\\|ablation_mode\\|attn_means\\|mlp_means\\|heads_to_ablate\\|hook_result\\|hook_mlp_out\\|baseline_diff\\|circuit_diff\\|cpr\\|cmd\\|def _head\\|def _mlp\\|io_ids\\|s_ids\\|ans_list\\|wrong_list\\|logit_diff\\|ans_logit\\|wrong_logit\" /root/structfuse-context/eval_mean_ablation.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-13T04:34:16.008314+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-13T04:34:16.008434+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls -la /root/structfuse-context/*.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls -la /root/structfuse-context/*.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-13T04:34:16.008566+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root     926 May 13 09:27 /root/structfuse-context/analysis_fix_v3_results.json\\n-rw-r--r-- 1 root root    2170 May 13 11:35 /root/structfuse-context/arithmetic_results.json\\n-rw-r--r-- 1 root root 1307690 May 13 09:15 /root/structfuse-context/cache_acdc.json\\n-rw-r--r-- 1 root root 1307702 May 13 11:35 /root/structfuse-context/cache_acdc_arith.json\\n-rw-r--r-- 1 root root 1368566 May 13 01:43 /root/structfuse-context/cache_eap_ig.json\\n-rw-r--r-- 1 root root 1367981 May 13 10:05 /root/structfuse-context/cache_eap_ig_arith.json\\n-rw-r--r-- 1 root root 1343850 May 13 01:37 /root/structfuse-context/cache_edge_pruning.json\\n-rw-r--r-- 1 root root 1351396 May 13 10:05 /root/structfuse-context/cache_ep_arith.json\\n-rw-r--r-- 1 root root    2113 May 13 10:08 /root/structfuse-context/circus_fix_results.json\\n-rw-r--r-- 1 root root    7944 May 13 09:22 /root/structfuse-context/eval_faithfulness_results.json\\n-rw-r--r-- 1 root root    2389 May 13 11:59 /root/structfuse-context/mean_ablation_results.json\\n-rw-r--r-- 1 root root    2075 May 13 09:32 /root/structfuse-context/mvp_results.json\\n-rw-r--r-- 1 root root    1095 May 13 09:33 /root/structfuse-context/phase_d_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-13T04:34:16.008690+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/structfuse-context -name \"*topk*\" -o -name \"*top_k*\" -o -name \"*sweep*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root/structfuse-context -name \"*topk*\" -o -name \"*top_k*\" -o -name \"*sweep*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-13T04:34:16.008832+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/structfuse-context/acdc_topk_sweep.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-13T04:34:16.008943+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/structfuse-context/acdc_topk_sweep.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/structfuse-context/acdc_topk_sweep.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-13T04:34:16.009126+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"import os\\nos.environ[\\\"CUDA_VISIBLE_DEVICES\\\"] = \\\"5\\\"\\n\\nimport json\\nimport math\\nfrom collections import Counter\\n\\ndef load_scores(path):\\n    with open(path) as f:\\n        return json.load(f)\\n\\ndef get_topk_edges(scores, k, use_abs=True):\\n    if use_abs:\\n        sorted_edges = sorted(\\n            scores.items(),\\n            key=lambda x: abs(x[1]) if not math.isinf(x[1]) else float('inf'),\\n            reverse=True\\n        )\\n    else:\\n        sorted_edges = sorted(\\n            scores.items(),\\n            key=lambda x: x[1] if not math.isinf(x[1]) else float('inf'),\\n            reverse=True\\n        )\\n    return set(e[0] for e in sorted_edges[:k])\\n\\ndef get_inf_edges(scores):\\n    return set(k for k, v in scores.items() if math.isinf(v))\\n\\ndef jaccard(a, b):\\n    if len(a | b) == 0:\\n        return 0.0\\n    return len(a & b) / len(a | b)\\n\\ndef analyze_score_distribution(scores, name):\\n    vals = list(scores.values())\\n    inf_count = sum(1 for v in vals if math.isinf(v))\\n    unique_vals = set(v for v in vals if not math.isinf(v))\\n    print(f\\\"\\\\n--- {name} ---\\\")\\n    print(f\\\"  Total edges: {len(vals)}\\\")\\n    print(f\\\"  Infinity edges: {inf_count}\\\")\\n    print(f\\\"  Unique non-inf values: {len(unique_vals)}\\\")\\n    if len(unique_vals) <= 10:\\n        val_counts = Counter(v for v in vals if not math.isinf(v))\\n        for v, c in sorted(val_counts.items(), key=lambda x: x[0], reverse=True)[:10]:\\n            print(f\\\"    {v:.6f}: {c} edges\\\")\\n    else:\\n        non_inf = sorted([abs(v) for v in vals if not math.isinf(v)], reverse=True)\\n        print(f\\\"  Top-5 abs values: {[round(x,4) for x in non_inf[:5]]}\\\")\\n        print(f\\\"  Median abs value: {non_inf[len(non_inf)//2]:.6f}\\\")\\n\\ndef run_sweep(dataset_name, acdc_scores, eapig_scores, ep_scores):\\n    print(f\\\"\\\\n{'='*70}\\\")\\n    print(
…[truncated 4636 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-13T04:34:16.009287+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -120 /root/structfuse-context/eval_mean_ablation.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -120 /root/structfuse-context/eval_mean_ablation.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-13T04:34:16.009465+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"import os\\nos.environ[\\\"CUDA_VISIBLE_DEVICES\\\"] = \\\"5\\\"\\n\\n\\\"\\\"\\\"Mean ablation faithfulness evaluation for Arithmetic (Greaterthan) task.\\n\\nCompares zero ablation vs mean ablation to check if negative CPR\\nis an artifact of overly harsh zero ablation.\\n\\\"\\\"\\\"\\n\\nimport json\\nimport math\\nimport random\\nimport re\\nimport sys\\nfrom pathlib import Path\\nfrom functools import partial\\n\\nimport torch\\nimport numpy as np\\n\\nsys.path.insert(0, \\\"/root/structfuse-context\\\")\\n\\n_LOCAL_GPT2 = \\\"/root/autodl-tmp/gpt2-small\\\"\\n_GPT2_ALIASES = (\\\"gpt2\\\", \\\"gpt2-small\\\", \\\"openai-community/gpt2\\\")\\n\\ndef _patch_hf():\\n    from transformers import AutoConfig, AutoTokenizer, AutoModelForCausalLM\\n    def _make_patched(orig_fn):\\n        def patched(name_or_path, *args, **kwargs):\\n            if name_or_path in _GPT2_ALIASES:\\n                name_or_path = _LOCAL_GPT2\\n            return orig_fn(name_or_path, *args, **kwargs)\\n        return patched\\n    AutoConfig.from_pretrained = staticmethod(_make_patched(AutoConfig.from_pretrained))\\n    AutoTokenizer.from_pretrained = staticmethod(_make_patched(AutoTokenizer.from_pretrained))\\n    AutoModelForCausalLM.from_pretrained = staticmethod(_make_patched(AutoModelForCausalLM.from_pretrained))\\n\\n_patch_hf()\\n\\nGT_DATASET_PATH = \\\"/root/miniconda3/lib/python3.12/site-packages/datasets/greaterthan_gpt2-small_prompts.json\\\"\\n\\n\\ndef _precompute_year_tokens(tokenizer):\\n    tokens = {}\\n    for yr in range(100):\\n        s = f\\\"{yr:02d}\\\"\\n        ids = tokenizer.encode(s)\\n        tokens[s] = ids[0]\\n    return tokens\\n\\n\\ndef load_gt_data(tokenizer, num_samples=100, seed=42):\\n    with open(GT_DATASET_PATH) as f:\\n        all_prompts = json.load(f)[\\\"prompts\\\"]\\n    random.seed(seed)\\n    if len(all_prompts) > num_samples:\\n        all_prompts = random.sample(all_prompts, n
…[truncated 2551 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-13T04:34:16.009612+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/structfuse-context/mean_ablation_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/structfuse-context/mean_ablation_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-13T04:34:16.009819+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"zero_ablation\\\": {\\n    \\\"method_eap_ig\\\": {\\n      \\\"num_edges\\\": 100,\\n      \\\"cpr\\\": -0.131,\\n      \\\"cmd\\\": 4.966,\\n      \\\"name\\\": \\\"method_eap_ig\\\"\\n    },\\n    \\\"method_edge_pruning\\\": {\\n      \\\"num_edges\\\": 100,\\n      \\\"cpr\\\": -0.1628,\\n      \\\"cmd\\\": 5.1058,\\n      \\\"name\\\": \\\"method_edge_pruning\\\"\\n    },\\n    \\\"method_acdc\\\": {\\n      \\\"num_edges\\\": 17,\\n      \\\"cpr\\\": -0.1836,\\n      \\\"cmd\\\": 5.197,\\n      \\\"name\\\": \\\"method_acdc\\\"\\n    },\\n    \\\"css_0.33\\\": {\\n      \\\"num_edges\\\": 118,\\n      \\\"cpr\\\": -0.1929,\\n      \\\"cmd\\\": 5.238,\\n      \\\"name\\\": \\\"css_0.33\\\"\\n    },\\n    \\\"css_0.67\\\": {\\n      \\\"num_edges\\\": 82,\\n      \\\"cpr\\\": -0.1756,\\n      \\\"cmd\\\": 5.1618,\\n      \\\"name\\\": \\\"css_0.67\\\"\\n    },\\n    \\\"css_1.00\\\": {\\n      \\\"num_edges\\\": 17,\\n      \\\"cpr\\\": -0.1836,\\n      \\\"cmd\\\": 5.197,\\n      \\\"name\\\": \\\"css_1.00\\\"\\n    },\\n    \\\"circus_core\\\": {\\n      \\\"num_edges\\\": 915,\\n      \\\"cpr\\\": 0.9258,\\n      \\\"cmd\\\": 0.3257,\\n      \\\"name\\\": \\\"circus_core\\\"\\n    },\\n    \\\"stable_core\\\": {\\n      \\\"num_edges\\\": 65,\\n      \\\"cpr\\\": -0.097,\\n      \\\"cmd\\\": 4.8169,\\n      \\\"name\\\": \\\"stable_core\\\"\\n    }\\n  },\\n  \\\"mean_ablation\\\": {\\n    \\\"method_eap_ig\\\": {\\n      \\\"num_edges\\\": 100,\\n      \\\"cpr\\\": 0.9598,\\n      \\\"cmd\\\": 0.1767,\\n      \\\"name\\\": \\\"method_eap_ig\\\"\\n    },\\n    \\\"method_edge_pruning\\\": {\\n      \\\"num_edges\\\": 100,\\n      \\\"cpr\\\": 0.9177,\\n      \\\"cmd\\\": 0.3614,\\n      \\\"name\\\": \\\"method_edge_pruning\\\"\\n    },\\n    \\\"method_acdc\\\": {\\n      \\\"num_edges\\\": 17,\\n      \\\"cpr\\\": 0.9845,\\n      \\\"cmd\\\": 0.0679,\\n      \\\"name\\\": \\\"method_acdc\\\"
…[truncated 1495 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-13T04:34:16.009967+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/structfuse-context/phase_d_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/structfuse-context/phase_d_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-13T04:34:16.010119+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"evaluation\\\": [\\n    {\\n      \\\"name\\\": \\\"method_eap_ig\\\",\\n      \\\"num_edges\\\": 100,\\n      \\\"cpr\\\": -0.1092,\\n      \\\"cmd\\\": 1.1348\\n    },\\n    {\\n      \\\"name\\\": \\\"method_edge_pruning\\\",\\n      \\\"num_edges\\\": 100,\\n      \\\"cpr\\\": -0.2413,\\n      \\\"cmd\\\": 1.2699\\n    },\\n    {\\n      \\\"name\\\": \\\"method_acdc\\\",\\n      \\\"num_edges\\\": 14,\\n      \\\"cpr\\\": 0.0286,\\n      \\\"cmd\\\": 0.9937\\n    },\\n    {\\n      \\\"name\\\": \\\"css_0.33\\\",\\n      \\\"num_edges\\\": 155,\\n      \\\"cpr\\\": -0.4862,\\n      \\\"cmd\\\": 1.5205\\n    },\\n    {\\n      \\\"name\\\": \\\"css_0.67\\\",\\n      \\\"num_edges\\\": 52,\\n      \\\"cpr\\\": 0.0634,\\n      \\\"cmd\\\": 0.9582\\n    },\\n    {\\n      \\\"name\\\": \\\"css_1.00\\\",\\n      \\\"num_edges\\\": 7,\\n      \\\"cpr\\\": 0.1095,\\n      \\\"cmd\\\": 0.911\\n    },\\n    {\\n      \\\"name\\\": \\\"circus_core\\\",\\n      \\\"num_edges\\\": 15,\\n      \\\"cpr\\\": -0.1081,\\n      \\\"cmd\\\": 1.1337\\n    },\\n    {\\n      \\\"name\\\": \\\"stable_core\\\",\\n      \\\"num_edges\\\": 13,\\n      \\\"cpr\\\": -0.187,\\n      \\\"cmd\\\": 1.2143\\n    }\\n  ],\\n  \\\"circuits_evaluated\\\": {\\n    \\\"method_eap_ig\\\": 100,\\n    \\\"method_edge_pruning\\\": 100,\\n    \\\"method_acdc\\\": 14,\\n    \\\"css_0.33\\\": 155,\\n    \\\"css_0.67\\\": 52,\\n    \\\"css_1.00\\\": 7,\\n    \\\"circus_core\\\": 15,\\n    \\\"stable_core\\\": 13\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-13T04:34:16.010307+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "tail -n +120 /root/structfuse-context/eval_mean_ablation.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "tail -n +120 /root/structfuse-context/eval_mean_ablation.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-13T04:34:16.010567+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\n    attn_means, mlp_means = {}, {}\\n    for layer in range(n_layers):\\n        attn_means[layer] = accumulators[f\\\"attn_{layer}\\\"] / n_batches\\n        mlp_means[layer] = accumulators[f\\\"mlp_{layer}\\\"] / n_batches\\n\\n    return attn_means, mlp_means\\n\\n\\ndef compute_metric(logits, tokens, ans_list, wrong_list):\\n    diffs = []\\n    for i in range(len(tokens)):\\n        diffs.append(\\n            logits[i, -1, ans_list[i]].mean() - logits[i, -1, wrong_list[i]].mean()\\n        )\\n    return torch.stack(diffs).mean().item()\\n\\n\\ndef evaluate_circuit(model, circuit_edges, tokens, ans_list, wrong_list,\\n                     ablation_mode=\\\"zero\\\", attn_means=None, mlp_means=None):\\n    if len(circuit_edges) == 0:\\n        return {\\\"num_edges\\\": 0, \\\"cpr\\\": 0.0, \\\"cmd\\\": 0.0}\\n\\n    circuit_nodes = extract_circuit_nodes(circuit_edges)\\n    n_layers, n_heads = model.cfg.n_layers, model.cfg.n_heads\\n\\n    ablate_heads = {}\\n    ablate_mlps = []\\n    for layer in range(n_layers):\\n        heads = [h for h in range(n_heads) if f'a{layer}.h{h}' not in circuit_nodes]\\n        if heads:\\n            ablate_heads[layer] = heads\\n        if f'm{layer}' not in circuit_nodes:\\n            ablate_mlps.append(layer)\\n\\n    if ablation_mode == \\\"zero\\\":\\n        def _head_hook(value, hook, heads_to_ablate):\\n            for h in heads_to_ablate:\\n                value[:, :, h, :] = 0\\n            return value\\n\\n        def _mlp_hook(value, hook):\\n            return torch.zeros_like(value)\\n    else:\\n        def _head_hook(value, hook, heads_to_ablate, layer_idx=None):\\n            mean_val = attn_means[layer_idx]\\n            seq_len = value.shape[1]\\n            mean_seq = mean_val.shape[1]\\n            if mean_seq >= seq_len:\\n                m = mean_val[:, -seq_len:, :, :]\\n            else:\\n                m = torch.nn.functional.pad(mean_val
…[truncated 7108 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-13T04:34:16.010743+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/structfuse-context/analysis_fix_v3_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/structfuse-context/analysis_fix_v3_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-13T04:34:16.010874+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/structfuse-context/arithmetic_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/structfuse-context/arithmetic_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-13T04:34:16.011024+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"config\\\": {\\n    \\\"top_n\\\": 100,\\n    \\\"percentile\\\": null,\\n    \\\"circus_B\\\": 10,\\n    \\\"css_threshold\\\": 0.67,\\n    \\\"K\\\": 3,\\n    \\\"methods\\\": [\\n      \\\"eap_ig\\\",\\n      \\\"edge_pruning\\\",\\n      \\\"acdc\\\"\\n    ]\\n  },\\n  \\\"binarized_sizes\\\": {\\n    \\\"eap_ig\\\": 100,\\n    \\\"edge_pruning\\\": 100,\\n    \\\"acdc\\\": 14\\n  },\\n  \\\"union_size\\\": 155,\\n  \\\"circus_tiers_restricted\\\": {\\n    \\\"noise\\\": 70,\\n    \\\"contingent\\\": 70,\\n    \\\"core\\\": 15\\n  },\\n  \\\"css_distribution\\\": {\\n    \\\"1/3\\\": 103,\\n    \\\"2/3\\\": 45,\\n    \\\"3/3\\\": 7\\n  },\\n  \\\"cross_table\\\": {\\n    \\\"stable_core\\\": 13,\\n    \\\"method_specific\\\": 2,\\n    \\\"cross_unstable\\\": 39,\\n    \\\"noise\\\": 101,\\n    \\\"core_total\\\": 15,\\n    \\\"off_diagonal_pct\\\": 0.1333,\\n    \\\"ci_95\\\": {\\n      \\\"low\\\": 0.0166,\\n      \\\"high\\\": 0.4046\\n    }\\n  },\\n  \\\"gate_verdict\\\": \\\"PASS_MAIN\\\",\\n  \\\"pairwise_jaccard\\\": {\\n    \\\"eap_ig_x_edge_pruning\\\": 0.3072,\\n    \\\"eap_ig_x_acdc\\\": 0.0962,\\n    \\\"edge_pruning_x_acdc\\\": 0.0857\\n  },\\n  \\\"three_way_ratio\\\": 0.0452,\\n  \\\"three_way_intersection_size\\\": 7\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-13T04:34:16.011219+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"config\\\": {\\n    \\\"model\\\": \\\"gpt2-small\\\",\\n    \\\"task\\\": \\\"greaterthan\\\",\\n    \\\"K\\\": 3,\\n    \\\"methods\\\": [\\n      \\\"eap_ig\\\",\\n      \\\"edge_pruning\\\",\\n      \\\"acdc\\\"\\n    ]\\n  },\\n  \\\"binarization\\\": {\\n    \\\"acdc\\\": \\\"isinf\\\",\\n    \\\"eap_ig\\\": \\\"top-100\\\",\\n    \\\"edge_pruning\\\": \\\"top-100\\\"\\n  },\\n  \\\"method_edge_counts\\\": {\\n    \\\"eap_ig\\\": 100,\\n    \\\"edge_pruning\\\": 100,\\n    \\\"acdc\\\": 17\\n  },\\n  \\\"cross_table\\\": {\\n    \\\"stable_core\\\": 65,\\n    \\\"method_specific\\\": 850,\\n    \\\"cross_unstable\\\": 17,\\n    \\\"noise\\\": 31559,\\n    \\\"total\\\": 32491,\\n    \\\"core_total\\\": 915,\\n    \\\"core_off_diagonal_pct\\\": 0.929\\n  },\\n  \\\"core_off_diagonal_pct\\\": 0.9289617486338798,\\n  \\\"binomial_ci_95\\\": {\\n    \\\"low\\\": 0.9103,\\n    \\\"high\\\": 0.9447\\n  },\\n  \\\"css_distribution\\\": {\\n    \\\"1/3\\\": 36,\\n    \\\"2/3\\\": 65,\\n    \\\"3/3\\\": 17\\n  },\\n  \\\"circus_tier_counts\\\": {\\n    \\\"core\\\": 915,\\n    \\\"contingent\\\": 6284,\\n    \\\"noise\\\": 25292\\n  },\\n  \\\"evaluation\\\": [\\n    {\\n      \\\"name\\\": \\\"method_eap_ig\\\",\\n      \\\"num_edges\\\": 100,\\n      \\\"cpr\\\": -0.142,\\n      \\\"cmd\\\": 4.7533\\n    },\\n    {\\n      \\\"name\\\": \\\"method_edge_pruning\\\",\\n      \\\"num_edges\\\": 100,\\n      \\\"cpr\\\": -0.1772,\\n      \\\"cmd\\\": 4.8997\\n    },\\n    {\\n      \\\"name\\\": \\\"method_acdc\\\",\\n      \\\"num_edges\\\": 17,\\n      \\\"cpr\\\": -0.1973,\\n      \\\"cmd\\\": 4.9832\\n    },\\n    {\\n      \\\"name\\\": \\\"css_0.33\\\",\\n      \\\"num_edges\\\": 118,\\n      \\\"cpr\\\": -0.2077,\\n      \\\"cmd\\\": 5.0267\\n    },\\n    {\\n      \\\"name\\\": \\\"css_0.67\\\",\\n      \\\"num_edges\\\": 82,\\n      \\\"cpr\\\": -0.201,\\n      \\\"cmd\\\": 4.9989\\n    },\\n    {
…[truncated 1172 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-13T04:34:16.011418+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep -rn \"def load_circuits\" /root/structfuse-context/eval_mean_ablation.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep -rn \"def load_circuits\" /root/structfuse-context/eval_mean_ablation.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-13T04:34:16.011554+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"237:def load_circuits():\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-13T04:34:16.011670+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/structfuse-context/circus_fix_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/structfuse-context/circus_fix_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-13T04:34:16.011870+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"method\\\": \\\"random_subset_circus_weighted\\\",\\n  \\\"params\\\": {\\n    \\\"n_circuits\\\": 100,\\n    \\\"subset_fraction\\\": 0.1,\\n    \\\"core_thr\\\": 0.0667,\\n    \\\"cont_thr\\\": 0.0\\n  },\\n  \\\"cpr_stats\\\": {\\n    \\\"mean\\\": 0.1477,\\n    \\\"std\\\": 0.2417,\\n    \\\"min\\\": -0.6215,\\n    \\\"max\\\": 1.079\\n  },\\n  \\\"tier_counts\\\": {\\n    \\\"core\\\": 39,\\n    \\\"contingent\\\": 32,\\n    \\\"noise\\\": 84\\n  },\\n  \\\"cross_table\\\": {\\n    \\\"stable_core\\\": 8,\\n    \\\"method_specific\\\": 31,\\n    \\\"cross_unstable\\\": 44,\\n    \\\"noise\\\": 72\\n  },\\n  \\\"stable_core_edges\\\": [\\n    \\\"a4.h11->a5.h5.k\\\",\\n    \\\"a9.h8->logits\\\",\\n    \\\"a9.h9->a11.h10.q\\\",\\n    \\\"m0->a7.h9.v\\\",\\n    \\\"m0->a9.h6.v\\\",\\n    \\\"m0->m4\\\",\\n    \\\"m0->m5\\\",\\n    \\\"m10->logits\\\"\\n  ],\\n  \\\"circus_core_edges\\\": [\\n    \\\"a10.h0->a11.h10.q\\\",\\n    \\\"a10.h7->m10\\\",\\n    \\\"a3.h0->m4\\\",\\n    \\\"a4.h11->a5.h5.k\\\",\\n    \\\"a4.h7->m4\\\",\\n    \\\"a5.h5->a7.h1.q\\\",\\n    \\\"a5.h5->m6\\\",\\n    \\\"a7.h9->a9.h9.q\\\",\\n    \\\"a8.h6->m8\\\",\\n    \\\"a9.h8->logits\\\",\\n    \\\"a9.h9->a11.h10.q\\\",\\n    \\\"a9.h9->m10\\\",\\n    \\\"input->a0.h3.v\\\",\\n    \\\"m0->a1.h11.k\\\",\\n    \\\"m0->a3.h6.v\\\",\\n    \\\"m0->a7.h9.v\\\",\\n    \\\"m0->a8.h10.v\\\",\\n    \\\"m0->a9.h6.v\\\",\\n    \\\"m0->a9.h7.v\\\",\\n    \\\"m0->m2\\\",\\n    \\\"m0->m3\\\",\\n    \\\"m0->m4\\\",\\n    \\\"m0->m5\\\",\\n    \\\"m0->m6\\\",\\n    \\\"m1->a3.h0.q\\\",\\n    \\\"m1->a5.h5.q\\\",\\n    \\\"m1->a9.h9.v\\\",\\n    \\\"m1->m2\\\",\\n    \\\"m1->m4\\\",\\n    \\\"m10->logits\\\",\\n    \\\"m2->a6.h9.q\\\",\\n    \\\"m2->a9.h9.v\\\",\\n    \\\"m3->a9.h9.v\\\",\\n    \\\"m6->a10.h7.v\\\",\\n    \\\"m6->a9.h9.v\\\",\\n    \\\"m7->a10.h7.v\\\",\\n    \\\"m7->a11.h10.v\\\",\\n    \\\"m7->a9.h9.v\\\",\\n    \\\"m8->a
…[truncated 1125 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-13T04:34:16.012018+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -5 /root/structfuse-context/cache_acdc_arith.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -5 /root/structfuse-context/cache_acdc_arith.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-13T04:34:16.012271+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"a8.h8->a9.h6.k\\\": 0.009999999776482582, \\\"a1.h10->a5.h4.q\\\": 0.009999999776482582, \\\"a5.h0->a6.h1.q\\\": 0.009999999776482582, \\\"a4.h1->a6.h9.v\\\": 0.009999999776482582, \\\"a10.h3->a11.h0.q\\\": 0.009999999776482582, \\\"a8.h1->a9.h2.q\\\": 0.009999999776482582, \\\"a2.h3->a4.h0.v\\\": 0.009999999776482582, \\\"a7.h4->a10.h0.k\\\": 0.009999999776482582, \\\"a7.h11->a8.h6.q\\\": 0.009999999776482582, \\\"a7.h10->a9.h10.q\\\": 0.009999999776482582, \\\"a4.h9->a7.h5.v\\\": 0.009999999776482582, \\\"a0.h9->a4.h2.v\\\": 0.009999999776482582, \\\"a0.h5->a2.h4.q\\\": 0.009999999776482582, \\\"a5.h2->a8.h0.q\\\": 0.009999999776482582, \\\"a7.h1->a11.h7.k\\\": 0.009999999776482582, \\\"a2.h0->a9.h9.v\\\": 0.009999999776482582, \\\"a0.h9->a3.h7.q\\\": 0.009999999776482582, \\\"m6->a11.h4.q\\\": 0.009999999776482582, \\\"a2.h2->a8.h5.q\\\": 0.009999999776482582, \\\"a4.h11->a9.h11.k\\\": 0.009999999776482582, \\\"a6.h2->a7.h3.k\\\": 0.009999999776482582, \\\"a5.h3->a7.h8.k\\\": 0.009999999776482582, \\\"a7.h5->a8.h0.v\\\": 0.009999999776482582, \\\"a5.h10->m8\\\": 0.009999999776482582, \\\"a2.h10->a3.h6.v\\\": 0.009999999776482582, \\\"a1.h1->a4.h4.k\\\": 0.009999999776482582, \\\"a7.h5->a8.h4.v\\\": 0.009999999776482582, \\\"a5.h6->a7.h3.q\\\": 0.009999999776482582, \\\"a0.h3->a3.h2.k\\\": 0.009999999776482582, \\\"a2.h8->a4.h8.v\\\": 0.009999999776482582, \\\"a3.h0->a6.h10.q\\\": 0.009999999776482582, \\\"a5.h1->a11.h9.q\\\": 0.009999999776482582, \\\"a0.h4->a2.h4.k\\\": 0.009999999776482582, \\\"a2.h5->a11.h11.v\\\": 0.009999999776482582, \\\"a8.h11->a11.h9.k\\\": 0.009999999776482582, \\\"a5.h5->a6.h6.q\\\": 0.009999999776482582, \\\"a4.h11->a7.h9.v\\\": 0.009999999776482582, \\\"a1.h11->a8.h6.q\\\": 0.009999999776482582, \\\"a3.h10->a6.h9.q\\\": 0.009999999776482582, \\\"a4.h4->a6.h0.v\\\": 0.009999999776482582, \\\"a1.h8->a7.h4.q\\\": 0.009999999776482582, \\\"a3.h0->a5.h1.q\\\": 0.00999999977648258
…[truncated 7398 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-13T04:34:16.012601+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls /root/miniconda3/lib/python3.12/site-packages/datasets/greaterthan_gpt2-small_prompts.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls /root/miniconda3/lib/python3.12/site-packages/datasets/greaterthan_gpt2-small_prompts.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-13T04:34:16.012764+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/miniconda3/lib/python3.12/site-packages/datasets/greaterthan_gpt2-small_prompts.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-13T04:34:16.012892+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "nvidia-smi --query-gpu=index,name,memory.used,memory.total --format=csv,noheader -i 5",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "nvidia-smi --query-gpu=index,name,memory.used,memory.total --format=csv,noheader -i 5",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-13T04:34:16.013012+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"5, NVIDIA GeForce RTX 4090 D, 0 MiB, 24564 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-13T04:34:16.013230+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/eval_topk_faithfulness.py",
  "content": "import os\nos.environ[\"CUDA_VISIBLE_DEVICES\"] = \"5\"\n\nimport json, math, random, re, sys\nfrom pathlib import Path\nfrom functools import partial\n\nimport torch\nimport numpy as np\n\nsys.path.insert(0, \"/root/structfuse-context\")\n\n_LOCAL_GPT2 = \"/root/autodl-tmp/gpt2-small\"\n_GPT2_ALIASES = (\"gpt2\", \"gpt2-small\", \"openai-community/gpt2\")\n\ndef _patch_hf():\n    from transformers import AutoConfig, AutoTokenizer, AutoModelForCausalLM\n    def _make_patched(orig_fn):\n        def patched(name_or_path, *args, **kwargs):\n            if name_or_path in _GPT2_ALIASES:\n                name_or_path = _LOCAL_GPT2\n            return orig_fn(name_or_path, *args, **kwargs)\n        return patched\n    AutoConfig.from_pretrained = staticmethod(_make_patched(AutoConfig.from_pretrained))\n    AutoTokenizer.from_pretrained = staticmethod(_make_patched(AutoTokenizer.from_pretrained))\n    AutoModelForCausalLM.from_pretrained = staticmethod(_make_patched(AutoModelForCausalLM.from_pretrained))\n\n_patch_hf()\n\nGT_DATASET_PATH = \"/root/miniconda3/lib/python3.12/site-packages/datasets/greaterthan_gpt2-small_prompts.json\"\n\nNAMES = [\"John\", \"Mary\", \"Alice\", \"Bob\", \"Charlie\", \"David\", \"Emma\", \"Frank\",\n         \"Grace\", \"Henry\", \"Jack\", \"Kate\", \"Leo\", \"Mia\", \"Noah\", \"Tom\"]\nTEMPLATES = [\n    \"When {io} and {s} went to the {place}, {s} gave a {obj} to\",\n    \"After {io} and {s} arrived at the {place}, {s} handed a {obj} to\",\n    \"{io} and {s} were at the {place}. {s} gave a {obj} to\",\n    \"Then, {io} and {s} had a meeting at the {place}, {s} passed a {obj} to\",\n]\nPLACES = [\"store\", \"park\", \"library\", \"school\", \"hospital\", \"restaurant\", \"office\"]\nOBJECTS = [\"bottle\", \"book\", \"letter\", \"ball\", \"gift\", \"toy\", \"bag\"]\n\n# ── Data ──\n\ndef _precompute_year_tokens(tokenizer):\n    tokens = {}\n    for yr in range(100):\n        s = f\"{yr:02d}\"\n        ids = tokenizer.encode(s)\n        tokens[s] = ids[0]\n    return tokens\n\ndef load_gt_data(tokenizer, num_samples=100, seed=42):\n    with open(GT_DATASET_PATH) as f:\n        all_prompts = json.load(f)[\"prompts\"]\n    random.seed(seed)\n    if len(all_prompts) > num_samples:\n        all_prompts = random.sample(all_prompts, num_samples)\n    yr_tok = _precompute_year_tokens(tokenizer)\n    prompts, ans_list, wrong_list = [], [], []\n    for p in all_prompts:\n        prompts.append(p[\"clean\"])\n        ans_ids = torch.tensor([yr_tok[a] for a in p[\"answers\"] if a in yr_tok])\n        wrong_ids = torch.tensor([yr_tok[a] for a in p[\"wrong_answers\"] if a in yr_tok])\n        ans_list.append(ans_ids)\n        wrong_list.append(wrong_ids)\n    return prompts, ans_list, wrong_list\n\ndef generate_ioi_data(tokenizer, num_samples=100, seed=42):\n    random.seed(seed)\n    prompts, labels = [], []\n    for _ in range(num_samples):\n        io_name, s_name = random.sample(NAMES, 2)\n        template = random.choice(TEMPLATES)\n        place = random.choice(PLACES)\n        obj = random.choice(OBJECTS)\n        prompts.append(template.format(io=io_name, s=s_name, place=place, obj=obj))\n        io_tokens = tokenizer.encode(\" \" + io_name)\n        s_tokens = tokenizer.encode(\" \" + s_name)\n        labels.append((io_tokens[0], s_tokens[0]))\n    return prompts, labels\n\n# ── Model ──\n\ndef load_model(device=\"cuda\"):\n    from transformer_lens import HookedTransformer\n    from transformers import AutoModelForCausalLM\n    hf_model = AutoModelForCausalLM.from_pretrained(_LOCAL_GPT2)\n    model = HookedTransformer.from_pretrained(\"gpt2-small\", hf_model=hf_model, device=device)\n    model.set_use_attn_result(True)\n    model.set_use_split_qkv_input(True)\n    model.set_use_hook_mlp_in(True)\n    return model\n\n# ── Evaluation core ──\n\ndef extract_circuit_nodes(circuit_edges):\n    nodes = set()\n    for edge in circuit_edges:\n        parts = edge.split('->')\n        if len(parts) != 2:\n            continue\n        nodes.add(parts[0].strip())\n        dst_base = re.sub(r'\\.[qkv]$', '', parts[1].strip())\n        nodes.add(dst_base)\n    nodes.discard('input')\n    nodes.discard('logits')\n    return nodes\n\ndef collect_mean_activations(model, tokens):\n    n_layers = model.cfg.n_layers\n    accumulators = {}\n\n    def make_accumulator(key):\n        def hook_fn(value, hook):\n            if key not in accumulators:\n                accumulators[key] = value.detach().mean(dim=0, keepdim=True).clone()\n            else:\n                accumulators[key] += value.detach().mean(dim=0, keepdim=True)\n            return value\n        return hook_fn\n\n    hooks = []\n    for layer in range(n_layers):\n        hooks.append((f\"blocks.{layer}.attn.hook_result\", make_accumulator(f\"attn_{layer}\")))\n        hooks.append((f\"blocks.{layer}.hook_mlp_out\", make_accumulator(f\"mlp_{layer}\")))\n\n    batch_size = 25\n    n_batches = 0\n    with torch.no_grad():\n        for start in range(0, len(tokens), batch_size):\n            batch = tokens[start:start + batch_size]\n            model.run_with_hooks(batch, fwd_hooks=hooks)\n            n_batches += 1\n\n    attn_means, mlp_means = {}, {}\n    for layer in range(n_layers):\n        attn_means[layer] = accumulators[f\"attn_{layer}\"] / n_batches\n        mlp_means[layer] = accumulators[f\"mlp_{layer}\"] / n_batches\n    return attn_means, mlp_means\n\ndef evaluate_circuit(model, circuit_edges, tokens, metric_fn,\n                     ablation_mode=\"zero\", attn_means=None, mlp_means=None):\n    if len(circuit_edges) == 0:\n        return {\"num_edges\": 0, \"cpr\": 0.0, \"cmd\": 0.0}\n\n    circuit_nodes = extract_circuit_nodes(circuit_edges)\n    n_layers, n_heads = model.cfg.n_layers, model.cfg.n_heads\n\n    ablate_heads = {}\n    ablate_mlps = []\n    for layer in range(n_layers):\n        heads = [h for h in range(n_heads) if f'a{layer}.h{h}' not in circuit_nodes]\n        if heads:\n            ablate_heads[layer] = heads\n        if f'm{layer}' not in circuit_nodes:\n            ablate_mlps.append(layer)\n\n    if ablation_mode == \"zero\":\n        def _head_hook(value, hook, heads_to_ablate):\n            for h in heads_to_ablate:\n                value[:, :, h, :] = 0\n            return value\n        def _mlp_hook(value, hook):\n            return torch.zeros_like(value)\n    else:\n        def _head_hook(value, hook, heads_to_ablate, layer_idx=None):\n            mean_val = attn_means[layer_idx]\n            seq_len = value.shape[1]\n            mean_seq = mean_val.shape[1]\n            if mean_seq >= seq_len:\n                m = mean_val[:, -seq_len:, :, :]\n            else:\n                m = torch.nn.functional.pad(mean_val, (0,0,0,0,0,seq_len-mean_seq), mode='replicate')\n            for h in heads_to_ablate:\n                value[:, :, h, :] = m[:, :seq_len, h, :].expand(value.shape[0], -1, -1)\n            return value\n        def _mlp_hook(value, hook, layer_idx=None):\n            mean_val = mlp_means[layer_idx]\n            seq_len = value.shape[1]\n            mean_seq = mean_val.shape[1]\n            if mean_seq >= seq_len:\n                m = mean_val[:, -seq_len:, :]\n            else:\n                m = torch.nn.functional.pad(mean_val, (0,0,0,seq_len-mean_seq), mode='replicate')\n            return m[:, :seq_len, :].expand(value.shape[0], -1, -1)\n\n    with torch.no_grad():\n        baseline_logits = model(tokens)\n        baseline_diff = metric_fn(baseline_logits, tokens)\n\n        hooks = []\n        for layer, heads in ablate_heads.items():\n            if ablation_mode == \"zero\":\n                hooks.append((f\"blocks.{layer}.attn.hook_result\",\n                              partial(_head_hook, heads_to_ablate=heads)))\n            else:\n                hooks.append((f\"blocks.{layer}.attn.hook_result\",\n                              partial(_head_hook, heads_to_ablate=heads, layer_idx=layer)))\n        for layer in ablate_mlps:\n            if ablation_mode == \"zero\":\n                hooks.append((f\"blocks.{layer}.hook_mlp_out\", _mlp_hook))\n            else:\n                hooks.append((f\"blocks.{layer}.hook_mlp_out\", partial(_mlp_hook, layer_idx=layer)))\n\n        circ_logits = model.run_with_hooks(tokens, fwd_hooks=hooks)\n        circuit_diff = metric_fn(circ_logits, tokens)\n\n    cpr = circuit_diff / baseline_diff if abs(baseline_diff) > 1e-6 else 0.0\n    cmd = abs(baseline_diff - circuit_diff)\n    return {\"num_edges\": len(circuit_edges), \"cpr\": round(cpr, 4), \"cmd\": round(cmd, 4)}\n\n# ── Circuit construction ──\n\ndef topk_edges(scores, k):\n    sorted_edges = sorted(\n        scores.items(),\n        key=lambda x: abs(x[1]) if not math.isinf(x[1]) else float('inf'),\n        reverse=True\n    )\n    return set(e for e, _ in sorted_edges[:k])\n\ndef isinf_edges(scores):\n    return set(e for e, v in scores.items() if math.isinf(v))\n\ndef compute_css(methods_edges):\n    K = len(methods_edges)\n    union = set()\n    for edges in methods_edges.values():\n        union |= edges\n    return {e: sum(1 for es in methods_edges.values() if e in es) / K for e in union}\n\ndef threshold_css(css_scores, threshold):\n    return {e for e, s in css_scores.items() if s >= threshold - 1e-2}\n\ndef css_distribution(css_scores):\n    dist = {\"1/3\": 0, \"2/3\": 0, \"3/3\": 0}\n    for s in css_scores.values():\n        if s >= 1.0 - 1e-2:\n            dist[\"3/3\"] += 1\n        elif s >= 0.67 - 1e-2:\n            dist[\"2/3\"] += 1\n        else:\n            dist[\"1/3\"] += 1\n    return dist\n\n# ── Evaluation runner ──\n\ndef run_task_evaluation(model, tokens, metric_fn, attn_means, mlp_means,\n                        acdc_scores, eapig_scores, ep_scores,\n                        k_values, task_name):\n    results = {}\n\n    for k in k_values:\n        print(f\"\\n--- k={k} ---\")\n        # CSS: ACDC-topK, EAP-IG-top100, EP-top100 (matches sweep convention)\n        acdc_circ = topk_edges(acdc_scores, k)\n        eapig_100 = topk_edges(eapig_scores, 100)\n        ep_100 = topk_edges(ep_scores, 100)\n        css_scores = compute_css({\"acdc\": acdc_circ, \"eap_ig\": eapig_100, \"ep\": ep_100})\n        css_10 = threshold_css(css_scores, 1.0)\n        css_067 = threshold_css(css_scores, 0.67)\n        dist = css_distribution(css_scores)\n\n        # Individual method circuits at same k (for fair per-edge comparison)\n        eapig_k = topk_edges(eapig_scores, k)\n        ep_k = topk_edges(ep_scores, k)\n\n        circuits = {\n            \"CSS=1.0\": css_10,\n            \"CSS>=2/3\": css_067,\n            \"ACDC\": acdc_circ,\n            \"EAP-IG\": eapig_k,\n            \"EP\": ep_k,\n        }\n\n        print(f\"  CSS dist: {dist}\")\n        for name, edges in circuits.items():\n            print(f\"  {name}: {len(edges)} edges\")\n\n        k_results = {\"css_distribution\": dist}\n\n        for mode in [\"zero\", \"mean\"]:\n            print(f\"  [{mode} ablation]\")\n            mode_results = {}\n            for name, edges in circuits.items():\n                r = evaluate_circuit(\n                    model, edges, tokens, metric_fn,\n                    ablation_mode=mode,\n                    attn_means=attn_means if mode == \"mean\" else None,\n                    mlp_means=mlp_means if mode == \"mean\" else None,\n                )\n                r[\"name\"] = name\n                mode_results[name] = r\n                print(f\"    {name} ({len(edges)} edges): CPR={r['cpr']:.4f}, CMD={r['cmd']:.4f}\")\n            k_results[mode] = mode_results\n        results[f\"k={k}\"] = k_results\n\n    # Also EAP-IG-top100 and EP-top100 as reference\n    print(\"\\n--- Reference: top-100 / isinf ---\")\n    acdc_inf = isinf_edges(acdc_scores)\n    eapig_100 = topk_edges(eapig_scores, 100)\n    ep_100 = topk_edges(ep_scores, 100)\n\n    css_inf = compute_css({\"acdc\": acdc_inf, \"eap_ig\": eapig_100, \"ep\": ep_100})\n    css_inf_10 = threshold_css(css_inf, 1.0)\n    css_inf_067 = threshold_css(css_inf, 0.67)\n\n    ref_circuits = {\n        \"ACDC-isinf\": acdc_inf,\n        \"EAP-IG-100\": eapig_100,\n        \"EP-100\": ep_100,\n        \"CSS=1.0-isinf\": css_inf_10,\n        \"CSS>=2/3-isinf\": css_inf_067,\n    }\n\n    ref_results = {}\n    for mode in [\"zero\", \"mean\"]:\n        print(f\"  [{mode} ablation - ref]\")\n        mode_results = {}\n        for name, edges in ref_circuits.items():\n            r = evaluate_circuit(\n                model, edges, tokens, metric_fn,\n                ablation_mode=mode,\n                attn_means=attn_means if mode == \"mean\" else None,\n                mlp_means=mlp_means if mode == \"mean\" else None,\n            )\n            r[\"name\"] = name\n            mode_results[name] = r\n            print(f\"    {name} ({len(edges)} edges): CPR={r['cpr']:.4f}, CMD={r['cmd']:.4f}\")\n        ref_results[mode] = mode_results\n    results[\"isinf_ref\"] = ref_results\n\n    return results\n\ndef print_summary_table(task_name, results, k_values):\n    print(f\"\\n=== {task_name} Top-K Faithfulness ===\\n\")\n    print(f\"{'Circuit':<20} {'k':>5} {'Edges':>6} {'Zero CPR':>9} {'Zero CMD':>9} {'Mean CPR':>9} {'Mean CMD':>9}\")\n    print(\"-\" * 72)\n\n    for k in k_values:\n        key = f\"k={k}\"\n        data = results[key]\n        for name in [\"CSS=1.0\", \"CSS>=2/3\", \"ACDC\", \"EAP-IG\", \"EP\"]:\n            z = data[\"zero\"][name]\n            m = data[\"mean\"][name]\n            print(f\"{name:<20} {k:>5} {z['num_edges']:>6} {z['cpr']:>9.4f} {z['cmd']:>9.4f} {m['cpr']:>9.4f} {m['cmd']:>9.4f}\")\n        print()\n\n    # isinf reference\n    ref = results[\"isinf_ref\"]\n    for name in [\"CSS=1.0-isinf\", \"CSS>=2/3-isinf\", \"ACDC-isinf\", \"EAP-IG-100\", \"EP-100\"]:\n        z = ref[\"zero\"][name]\n        m = ref[\"mean\"][name]\n        print(f\"{name:<20} {'ref':>5} {z['num_edges']:>6} {z['cpr']:>9.4f} {z['cmd']:>9.4f} {m['cpr']:>9.4f} {m['cmd']:>9.4f}\")\n\ndef check_condition_4(task_name, results, k_values):\n    print(f\"\\n--- {task_name}: D025 Condition ④ ---\")\n    for k in k_values:\n        key = f\"k={k}\"\n        data = results[key]\n        for mode in [\"zero\", \"mean\"]:\n            css_cpr = data[mode][\"CSS=1.0\"][\"cpr\"]\n            css_edges = data[mode][\"CSS=1.0\"][\"num_edges\"]\n            methods = [\"ACDC\", \"EAP-IG\", \"EP\"]\n            best_name = max(methods, key=lambda n: data[mode][n][\"cpr\"])\n            best_cpr = data[mode][best_name][\"cpr\"]\n            best_edges = data[mode][best_name][\"num_edges\"]\n            passed = css_cpr > best_cpr\n            print(f\"  k={k} [{mode}]: CSS=1.0 CPR={css_cpr:.4f} ({css_edges}e) \"\n                  f\"vs {best_name} CPR={best_cpr:.4f} ({best_edges}e) \"\n                  f\"→ {'PASS ✓' if passed else 'FAIL ✗'}\")\n\n\ndef main():\n    device = torch.device(\"cuda\")\n    cache_dir = Path(\"/root/structfuse-context\")\n\n    print(f\"CUDA_VISIBLE_DEVICES={os.environ.get('CUDA_VISIBLE_DEVICES')}\")\n    print(\"Loading model...\")\n    model = load_model(device)\n\n    # ═══════════════ Arithmetic ═══════════════\n    print(\"\\n\" + \"=\" * 70)\n    print(\"  ARITHMETIC (Greaterthan)\")\n    print(\"=\" * 70)\n\n    prompts_a, ans_list, wrong_list = load_gt_data(model.tokenizer, num_samples=100, seed=42)\n    tokens_a = model.to_tokens(prompts_a, prepend_bos=True)\n    print(f\"Data: {len(prompts_a)} prompts, tokens {tokens_a.shape}\")\n\n    def metric_arith(logits, tokens):\n        diffs = []\n        for i in range(len(tokens)):\n            diffs.append(logits[i, -1, ans_list[i]].mean() - logits[i, -1, wrong_list[i]].mean())\n        return torch.stack(diffs).mean().item()\n\n    print(\"Collecting mean activations...\")\n    attn_m_a, mlp_m_a = collect_mean_activations(model, tokens_a)\n\n    with open(cache_dir / \"cache_acdc_arith.json\") as f: acdc_a = json.load(f)\n    with open(cache_dir / \"cache_eap_ig_arith.json\") as f: eapig_a = json.load(f)\n    with open(cache_dir / \"cache_ep_arith.json\") as f: ep_a = json.load(f)\n\n    arith_results = run_task_evaluation(\n        model, tokens_a, metric_arith, attn_m_a, mlp_m_a,\n        acdc_a, eapig_a, ep_a,\n        k_values=[50, 75, 100],\n        task_name=\"Arithmetic\"\n    )\n\n    with open(cache_dir / \"faithfulness_arithmetic_topk.json\", \"w\") as f:\n        json.dump(arith_results, f, indent=2)\n    print(f\"\\nSaved: faithfulness_arithmetic_topk.json\")\n\n    # ═══════════════ IOI ═══════════════\n    print(\"\\n\" + \"=\" * 70)\n    print(\"  IOI\")\n    print(\"=\" * 70)\n\n    prompts_i, labels_i = generate_ioi_data(model.tokenizer, num_samples=100, seed=42)\n    tokens_i = model.to_tokens(prompts_i, prepend_bos=True)\n    io_ids = torch.tensor([l[0] for l in labels_i])\n    s_ids = torch.tensor([l[1] for l in labels_i])\n    print(f\"Data: {len(prompts_i)} prompts, tokens {tokens_i.shape}\")\n\n    def metric_ioi(logits, tokens):\n        return (logits[range(len(tokens)), -1, io_ids] -\n                logits[range(len(tokens)), -1, s_ids]).mean().item()\n\n    print(\"Collecting mean activations...\")\n    attn_m_i, mlp_m_i = collect_mean_activations(model, tokens_i)\n\n    with open(cache_dir / \"cache_acdc.json\") as f: acdc_i = json.load(f)\n    with open(cache_dir / \"cache_eap_ig.json\") as f: eapig_i = json.load(f)\n    with open(cache_dir / \"cache_edge_pruning.json\") as f: ep_i = json.load(f)\n\n    ioi_results = run_task_evaluation(\n        model, tokens_i, metric_ioi, attn_m_i, mlp_m_i,\n        acdc_i, eapig_i, ep_i,\n        k_values=[50, 100],\n        task_name=\"IOI\"\n    )\n\n    with open(cache_dir / \"faithfulness_ioi_topk.json\", \"w\") as f:\n        json.dump(ioi_results, f, indent=2)\n    print(f\"\\nSaved: faithfulness_ioi_topk.json\")\n\n    # ═══════════════ Summary ═══════════════\n    print(\"\\n\" + \"=\" * 70)\n    print(\"  FULL SUMMARY\")\n    print(\"=\" * 70)\n\n    print_summary_table(\"Arithmetic\", arith_results, [50, 75, 100])\n    print_summary_table(\"IOI\", ioi_results, [50, 100])\n\n    check_condition_4(\"Arithmetic\", arith_results, [50, 75])\n    check_condition_4(\"IOI\", ioi_results, [50, 100])\n\n    # CPR inconsistency analysis\n    print(\"\\n=== IOI CPR Inconsistency Analysis ===\")\n    print(\"phase_d_results.json: IOI task, node-level zero ablation (evaluation.py)\")\n    print(\"mean_ablation_results.json: ARITHMETIC task, not IOI (eval_mean_ablation.py)\")\n    print(\"Conclusion: The files evaluate DIFFERENT TASKS.\")\n    print(\"  - evaluation.py uses io_ids/s_ids (IOI logit difference)\")\n    print(\"  - eval_mean_ablation.py uses ans_list/wrong_list (Greaterthan year tokens)\")\n    print(\"  - Numbers are incomparable. Both implementations are correct for their task.\")\n    print(\"  - The isinf issue (CSS=1.0 = ACDC) affects both tasks, now resolved with topk.\")\n\n    print(\"\\nDone.\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/eval_topk_faithfulness.py",
    "content": "import os\nos.environ[\"CUDA_VISIBLE_DEVICES\"] = \"5\"\n\nimport json, math, random, re, sys\nfrom pathlib import Path\nfrom functools import partial\n\nimport torch\nimport numpy as np\n\nsys.path.insert(0, \"/root/structfuse-context\")\n\n_LOCAL_GPT2 = \"/root/autodl-tmp/gpt2-small\"\n_GPT2_ALIASES = (\"gpt2\", \"gpt2-small\", \"openai-community/gpt2\")\n\ndef _patch_hf():\n    from transformers import AutoConfig, AutoTokenizer, AutoModelForCausalLM\n    def _make_patched(orig_fn):\n        def patched(name_or_path, *args, **kwargs):\n            if name_or_path in _GPT2_ALIASES:\n                name_or_path = _LOCAL_GPT2\n            return orig_fn(name_or_path, *args, **kwargs)\n        return patched\n    AutoConfig.from_pretrained = staticmethod(_make_patched(AutoConfig.from_pretrained))\n    AutoTokenizer.from_pretrained = staticmethod(_make_patched(AutoTokenizer.from_pretrained))\n    AutoModelForCausalLM.from_pretrained = staticmethod(_make_patched(AutoModelForCausalLM.from_pretrained))\n\n_patch_hf()\n\nGT_DATASET_PATH = \"/root/miniconda3/lib/python3.12/site-packages/datasets/greaterthan_gpt2-small_prompts.json\"\n\nNAMES = [\"John\", \"Mary\", \"Alice\", \"Bob\", \"Charlie\", \"David\", \"Emma\", \"Frank\",\n         \"Grace\", \"Henry\", \"Jack\", \"Kate\", \"Leo\", \"Mia\", \"Noah\", \"Tom\"]\nTEMPLATES = [\n    \"When {io} and {s} went to the {place}, {s} gave a {obj} to\",\n    \"After {io} and {s} arrived at the {place}, {s} handed a {obj} to\",\n    \"{io} and {s} were at the {place}. {s} gave a {obj} to\",\n    \"Then, {io} and {s} had a meeting at the {place}, {s} passed a {obj} to\",\n]\nPLACES = [\"store\", \"park\", \"library\", \"school\", \"hospital\", \"restaurant\", \"office\"]\nOBJECTS = [\"bottle\", \"book\", \"letter\", \"ball\", \"gift\", \"toy\", \"bag\"]\n\n# ── Data ──\n\ndef _precompute_year_tokens(tokenizer):\n    tokens = {}\n    for yr in range(100):\n        s = f\"{yr:02d}\"\n        ids = tokenizer.encode(s)\n        tokens[s] = ids[0]\n    return tokens\n\ndef load_gt_data(tokenizer, num_samples=100, seed=42):\n    with open(GT_DATASET_PATH) as f:\n        all_prompts = json.load(f)[\"prompts\"]\n    random.seed(seed)\n    if len(all_prompts) > num_samples:\n        all_prompts = random.sample(all_prompts, num_samples)\n    yr_tok = _precompute_year_tokens(tokenizer)\n    prompts, ans_list, wrong_list = [], [], []\n    for p in all_prompts:\n        prompts.append(p[\"clean\"])\n        ans_ids = torch.tensor([yr_tok[a] for a in p[\"answers\"] if a in yr_tok])\n        wrong_ids = torch.tensor([yr_tok[a] for a in p[\"wrong_answers\"] if a in yr_tok])\n        ans_list.append(ans_ids)\n        wrong_list.append(wrong_ids)\n    return prompts, ans_list, wrong_list\n\ndef generate_ioi_data(tokenizer, num_samples=100, seed=42):\n    random.seed(seed)\n    prompts, labels = [], []\n    for _ in range(num_samples):\n        io_name, s_name = random.sample(NAMES, 2)\n        template = random.choice(TEMPLATES)\n        place = random.choice(PLACES)\n        obj = random.choice(OBJECTS)\n        prompts.append(template.format(io=io_name, s=s_name, place=place, obj=obj))\n        io_tokens = tokenizer.encode(\" \" + io_name)\n        s_tokens = tokenizer.encode(\" \" + s_name)\n        labels.append((io_tokens[0], s_tokens[0]))\n    return prompts, labels\n\n# ── Model ──\n\ndef load_model(device=\"cuda\"):\n    from transformer_lens import HookedTransformer\n    from transformers import AutoModelForCausalLM\n    hf_model = AutoModelForCausalLM.from_pretrained(_LOCAL_GPT2)\n    model = HookedTransformer.from_pretrained(\"gpt2-small\", hf_model=hf_model, device=device)\n    model.set_use_attn_result(True)\n    model.set_use_split_qkv_input(True)\n    model.set_use_hook_mlp_in(True)\n    return model\n\n# ── Evaluation core ──\n\ndef extract_circuit_nodes(circuit_edges):\n    nodes = set()\n    for edge in circuit_edges:\n        parts = edge.split('->')\n        if len(parts) != 2:\n            continue\n        nodes.add(parts[0].strip())\n        dst_base = re.sub(r'\\.[qkv]$', '', parts[1].strip())\n        nodes.add(dst_base)\n    nodes.discard('input')\n    nodes.discard('logits')\n    return nodes\n\ndef collect_mean_activations(model, tokens):\n    n_layers = model.cfg.n_layers\n    accumulators = {}\n\n    def make_accumulator(key):\n        def hook_fn(value, hook):\n            if key not in accumulators:\n                accumulators[key] = value.detach().mean(dim=0, keepdim=True).clone()\n            else:\n                accumulators[key] += value.detach().mean(dim=0, keepdim=True)\n            return value\n        return hook_fn\n\n    hooks = []\n    for layer in range(n_layers):\n        hooks.append((f\"blocks.{layer}.attn.hook_result\", make_accumulator(f\"attn_{layer}\")))\n        hooks.append((f\"blocks.{layer}.hook_mlp_out\", make_accumulator(f\"mlp_{layer}\")))\n\n    batch_size = 25\n    n_batches = 0\n    with torch.no_grad():\n        for start in range(0, len(tokens), batch_size):\n            batch = tokens[start:start + batch_size]\n            model.run_with_hooks(batch, fwd_hooks=hooks)\n            n_batches += 1\n\n    attn_means, mlp_means = {}, {}\n    for layer in range(n_layers):\n        attn_means[layer] = accumulators[f\"attn_{layer}\"] / n_batches\n        mlp_means[layer] = accumulators[f\"mlp_{layer}\"] / n_batches\n    return attn_means, mlp_means\n\ndef evaluate_circuit(model, circuit_edges, tokens, metric_fn,\n                     ablation_mode=\"zero\", attn_means=None, mlp_means=None):\n    if len(circuit_edges) == 0:\n        return {\"num_edges\": 0, \"cpr\": 0.0, \"cmd\": 0.0}\n\n    circuit_nodes = extract_circuit_nodes(circuit_edges)\n    n_layers, n_heads = model.cfg.n_layers, model.cfg.n_heads\n\n    ablate_heads = {}\n    ablate_mlps = []\n    for layer in range(n_layers):\n        heads = [h for h in range(n_heads) if f'a{layer}.h{h}' not in circuit_nodes]\n        if heads:\n            ablate_heads[layer] = heads\n        if f'm{layer}' not in circuit_nodes:\n            ablate_mlps.append(layer)\n\n    if ablation_mode == \"zero\":\n        def _head_hook(value, hook, heads_to_ablate):\n            for h in heads_to_ablate:\n                value[:, :, h, :] = 0\n            return value\n        def _mlp_hook(value, hook):\n            return torch.zeros_like(value)\n    else:\n        def _head_hook(value, hook, heads_to_ablate, layer_idx=None):\n            mean_val = attn_means[layer_idx]\n            seq_len = value.shape[1]\n            mean_seq = mean_val.shape[1]\n            if mean_seq >= seq_len:\n                m = mean_val[:, -seq_len:, :, :]\n            else:\n                m = torch.nn.functional.pad(mean_val, (0,0,0,0,0,seq_len-mean_seq), mode='replicate')\n            for h in heads_to_ablate:\n                value[:, :, h, :] = m[:, :seq_len, h, :].expand(value.shape[0], -1, -1)\n            return value\n        def _mlp_hook(value, hook, layer_idx=None):\n            mean_val = mlp_means[layer_idx]\n            seq_len = value.shape[1]\n            mean_seq = mean_val.shape[1]\n            if mean_seq >= seq_len:\n                m = mean_val[:, -seq_len:, :]\n            else:\n                m = torch.nn.functional.pad(mean_val, (0,0,0,seq_len-mean_seq), mode='replicate')\n            return m[:, :seq_len, :].expand(value.shape[0], -1, -1)\n\n    with torch.no_grad():\n        baseline_logits = model(tokens)\n        baseline_diff = metric_fn(baseline_logits, tokens)\n\n        hooks = []\n        for layer, heads in ablate_heads.items():\n            if ablation_mode == \"zero\":\n                hooks.append((f\"blocks.{layer}.attn.hook_result\",\n                              partial(_head_hook, heads_to_ablate=heads)))\n            else:\n                hooks.append((f\"blocks.{layer}.attn.hook_result\",\n                              partial(_head_hook, heads_to_ablate=heads, layer_idx=layer)))\n        for layer in ablate_mlps:\n            if ablation_mode == \"zero\":\n                hooks.append((f\"blocks.{layer}.hook_mlp_out\", _mlp_hook))\n            else:\n                hooks.append((f\"blocks.{layer}.hook_mlp_out\", partial(_mlp_hook, layer_idx=layer)))\n\n        circ_logits = model.run_with_hooks(tokens, fwd_hooks=hooks)\n        circuit_diff = metric_fn(circ_logits, tokens)\n\n    cpr = circuit_diff / baseline_diff if abs(baseline_diff) > 1e-6 else 0.0\n    cmd = abs(baseline_diff - circuit_diff)\n    return {\"num_edges\": len(circuit_edges), \"cpr\": round(cpr, 4), \"cmd\": round(cmd, 4)}\n\n# ── Circuit construction ──\n\ndef topk_edges(scores, k):\n    sorted_edges = sorted(\n        scores.items(),\n        key=lambda x: abs(x[1]) if not math.isinf(x[1]) else float('inf'),\n        reverse=True\n    )\n    return set(e for e, _ in sorted_edges[:k])\n\ndef isinf_edges(scores):\n    return set(e for e, v in scores.items() if math.isinf(v))\n\ndef compute_css(methods_edges):\n    K = len(methods_edges)\n    union = set()\n    for edges in methods_edges.values():\n        union |= edges\n    return {e: sum(1 for es in methods_edges.values() if e in es) / K for e in union}\n\ndef threshold_css(css_scores, threshold):\n    return {e for e, s in css_scores.items() if s >= threshold - 1e-2}\n\ndef css_distribution(css_scores):\n    dist = {\"1/3\": 0, \"2/3\": 0, \"3/3\": 0}\n    for s in css_scores.values():\n        if s >= 1.0 - 1e-2:\n            dist[\"3/3\"] += 1\n        elif s >= 0.67 - 1e-2:\n            dist[\"2/3\"] += 1\n        else:\n            dist[\"1/3\"] += 1\n    return dist\n\n# ── Evaluation runner ──\n\ndef run_task_evaluation(model, tokens, metric_fn, attn_means, mlp_means,\n                        acdc_scores, eapig_scores, ep_scores,\n                        k_values, task_name):\n    results = {}\n\n    for k in k_values:\n        print(f\"\\n--- k={k} ---\")\n        # CSS: ACDC-topK, EAP-IG-top100, EP-top100 (matches sweep convention)\n        acdc_circ = topk_edges(acdc_scores, k)\n        eapig_100 = topk_edges(eapig_scores, 100)\n        ep_100 = topk_edges(ep_scores, 100)\n        css_scores = compute_css({\"acdc\": acdc_circ, \"eap_ig\": eapig_100, \"ep\": ep_100})\n        css_10 = threshold_css(css_scores, 1.0)\n        css_067 = threshold_css(css_scores, 0.67)\n        dist = css_distribution(css_scores)\n\n        # Individual method circuits at same k (for fair per-edge comparison)\n        eapig_k = topk_edges(eapig_scores, k)\n        ep_k = topk_edges(ep_scores, k)\n\n        circuits = {\n            \"CSS=1.0\": css_10,\n            \"CSS>=2/3\": css_067,\n            \"ACDC\": acdc_circ,\n            \"EAP-IG\": eapig_k,\n            \"EP\": ep_k,\n        }\n\n        print(f\"  CSS dist: {dist}\")\n        for name, edges in circuits.items():\n            print(f\"  {name}: {len(edges)} edges\")\n\n        k_results = {\"css_distribution\": dist}\n\n        for mode in [\"zero\", \"mean\"]:\n            print(f\"  [{mode} ablation]\")\n            mode_results = {}\n            for name, edges in circuits.items():\n                r = evaluate_circuit(\n                    model, edges, tokens, metric_fn,\n                    ablation_mode=mode,\n                    attn_means=attn_means if mode == \"mean\" else None,\n                    mlp_means=mlp_means if mode == \"mean\" else None,\n                )\n                r[\"name\"] = name\n                mode_results[name] = r\n                print(f\"    {name} ({len(edges)} edges): CPR={r['cpr']:.4f}, CMD={r['cmd']:.4f}\")\n            k_results[mode] = mode_results\n        results[f\"k={k}\"] = k_results\n\n    # Also EAP-IG-top100 and EP-top100 as reference\n    print(\"\\n--- Reference: top-100 / isinf ---\")\n    acdc_inf = isinf_edges(acdc_scores)\n    eapig_100 = topk_edges(eapig_scores, 100)\n    ep_100 = topk_edges(ep_scores, 100)\n\n    css_inf = compute_css({\"acdc\": acdc_inf, \"eap_ig\": eapig_100, \"ep\": ep_100})\n    css_inf_10 = threshold_css(css_inf, 1.0)\n    css_inf_067 = threshold_css(css_inf, 0.67)\n\n    ref_circuits = {\n        \"ACDC-isinf\": acdc_inf,\n        \"EAP-IG-100\": eapig_100,\n        \"EP-100\": ep_100,\n        \"CSS=1.0-isinf\": css_inf_10,\n        \"CSS>=2/3-isinf\": css_inf_067,\n    }\n\n    ref_results = {}\n    for mode in [\"zero\", \"mean\"]:\n        print(f\"  [{mode} ablation - ref]\")\n        mode_results = {}\n        for name, edges in ref_circuits.items():\n            r = evaluate_circuit(\n                model, edges, tokens, metric_fn,\n                ablation_mode=mode,\n                attn_means=attn_means if mode == \"mean\" else None,\n                mlp_means=mlp_means if mode == \"mean\" else None,\n            )\n            r[\"name\"] = name\n            mode_results[name] = r\n            print(f\"    {name} ({len(edges)} edges): CPR={r['cpr']:.4f}, CMD={r['cmd']:.4f}\")\n        ref_results[mode] = mode_results\n    results[\"isinf_ref\"] = ref_results\n\n    return results\n\ndef print_summary_table(task_name, results, k_values):\n    print(f\"\\n=== {task_name} Top-K Faithfulness ===\\n\")\n    print(f\"{'Circuit':<20} {'k':>5} {'Edges':>6} {'Zero CPR':>9} {'Zero CMD':>9} {'Mean CPR':>9} {'Mean CMD':>9}\")\n    print(\"-\" * 72)\n\n    for k in k_values:\n        key = f\"k={k}\"\n        data = results[key]\n        for name in [\"CSS=1.0\", \"CSS>=2/3\", \"ACDC\", \"EAP-IG\", \"EP\"]:\n            z = data[\"zero\"][name]\n            m = data[\"mean\"][name]\n            print(f\"{name:<20} {k:>5} {z['num_edges']:>6} {z['cpr']:>9.4f} {z['cmd']:>9.4f} {m['cpr']:>9.4f} {m['cmd']:>9.4f}\")\n        print()\n\n    # isinf reference\n    ref = results[\"isinf_ref\"]\n    for name in [\"CSS=1.0-isinf\", \"CSS>=2/3-isinf\", \"ACDC-isinf\", \"EAP-IG-100\", \"EP-100\"]:\n        z = ref[\"zero\"][name]\n        m = ref[\"mean\"][name]\n        print(f\"{name:<20} {'ref':>5} {z['num_edges']:>6} {z['cpr']:>9.4f} {z['cmd']:>9.4f} {m['cpr']:>9.4f} {m['cmd']:>9.4f}\")\n\ndef check_condition_4(task_name, results, k_values):\n    print(f\"\\n--- {task_name}: D025 Condition ④ ---\")\n    for k in k_values:\n        key = f\"k={k}\"\n        data = results[key]\n        for mode in [\"zero\", \"mean\"]:\n            css_cpr = data[mode][\"CSS=1.0\"][\"cpr\"]\n            css_edges = data[mode][\"CSS=1.0\"][\"num_edges\"]\n            methods = [\"ACDC\", \"EAP-IG\", \"EP\"]\n            best_name = max(methods, key=lambda n: data[mode][n][\"cpr\"])\n            best_cpr = data[mode][best_name][\"cpr\"]\n            best_edges = data[mode][best_name][\"num_edges\"]\n            passed = css_cpr > best_cpr\n            print(f\"  k={k} [{mode}]: CSS=1.0 CPR={css_cpr:.4f} ({css_edges}e) \"\n                  f\"vs {best_name} CPR={best_cpr:.4f} ({best_edges}e) \"\n                  f\"→ {'PASS ✓' if passed else 'FAIL ✗'}\")\n\n\ndef main():\n    device = torch.device(\"cuda\")\n    cache_dir = Path(\"/root/structfuse-context\")\n\n    print(f\"CUDA_VISIBLE_DEVICES={os.environ.get('CUDA_VISIBLE_DEVICES')}\")\n    print(\"Loading model...\")\n    model = load_model(device)\n\n    # ═══════════════ Arithmetic ═══════════════\n    print(\"\\n\" + \"=\" * 70)\n    print(\"  ARITHMETIC (Greaterthan)\")\n    print(\"=\" * 70)\n\n    prompts_a, ans_list, wrong_list = load_gt_data(model.tokenizer, num_samples=100, seed=42)\n    tokens_a = model.to_tokens(prompts_a, prepend_bos=True)\n    print(f\"Data: {len(prompts_a)} prompts, tokens {tokens_a.shape}\")\n\n    def metric_arith(logits, tokens):\n        diffs = []\n        for i in range(len(tokens)):\n            diffs.append(logits[i, -1, ans_list[i]].mean() - logits[i, -1, wrong_list[i]].mean())\n        return torch.stack(diffs).mean().item()\n\n    print(\"Collecting mean activations...\")\n    attn_m_a, mlp_m_a = collect_mean_activations(model, tokens_a)\n\n    with open(cache_dir / \"cache_acdc_arith.json\") as f: acdc_a = json.load(f)\n    with open(cache_dir / \"cache_eap_ig_arith.json\") as f: eapig_a = json.load(f)\n    with open(cache_dir / \"cache_ep_arith.json\") as f: ep_a = json.load(f)\n\n    arith_results = run_task_evaluation(\n        model, tokens_a, metric_arith, attn_m_a, mlp_m_a,\n        acdc_a, eapig_a, ep_a,\n        k_values=[50, 75, 100],\n        task_name=\"Arithmetic\"\n    )\n\n    with open(cache_dir / \"faithfulness_arithmetic_topk.json\", \"w\") as f:\n        json.dump(arith_results, f, indent=2)\n    print(f\"\\nSaved: faithfulness_arithmetic_topk.json\")\n\n    # ═══════════════ IOI ═══════════════\n    print(\"\\n\" + \"=\" * 70)\n    print(\"  IOI\")\n    print(\"=\" * 70)\n\n    prompts_i, labels_i = generate_ioi_data(model.tokenizer, num_samples=100, seed=42)\n    tokens_i = model.to_tokens(prompts_i, prepend_bos=True)\n    io_ids = torch.tensor([l[0] for l in labels_i])\n    s_ids = torch.tensor([l[1] for l in labels_i])\n    print(f\"Data: {len(prompts_i)} prompts, tokens {tokens_i.shape}\")\n\n    def metric_ioi(logits, tokens):\n        return (logits[range(len(tokens)), -1, io_ids] -\n                logits[range(len(tokens)), -1, s_ids]).mean().item()\n\n    print(\"Collecting mean activations...\")\n    attn_m_i, mlp_m_i = collect_mean_activations(model, tokens_i)\n\n    with open(cache_dir / \"cache_acdc.json\") as f: acdc_i = json.load(f)\n    with open(cache_dir / \"cache_eap_ig.json\") as f: eapig_i = json.load(f)\n    with open(cache_dir / \"cache_edge_pruning.json\") as f: ep_i = json.load(f)\n\n    ioi_results = run_task_evaluation(\n        model, tokens_i, metric_ioi, attn_m_i, mlp_m_i,\n        acdc_i, eapig_i, ep_i,\n        k_values=[50, 100],\n        task_name=\"IOI\"\n    )\n\n    with open(cache_dir / \"faithfulness_ioi_topk.json\", \"w\") as f:\n        json.dump(ioi_results, f, indent=2)\n    print(f\"\\nSaved: faithfulness_ioi_topk.json\")\n\n    # ═══════════════ Summary ═══════════════\n    print(\"\\n\" + \"=\" * 70)\n    print(\"  FULL SUMMARY\")\n    print(\"=\" * 70)\n\n    print_summary_table(\"Arithmetic\", arith_results, [50, 75, 100])\n    print_summary_table(\"IOI\", ioi_results, [50, 100])\n\n    check_condition_4(\"Arithmetic\", arith_results, [50, 75])\n    check_condition_4(\"IOI\", ioi_results, [50, 100])\n\n    # CPR inconsistency analysis\n    print(\"\\n=== IOI CPR Inconsistency Analysis ===\")\n    print(\"phase_d_results.json: IOI task, node-level zero ablation (evaluation.py)\")\n    print(\"mean_ablation_results.json: ARITHMETIC task, not IOI (eval_mean_ablation.py)\")\n    print(\"Conclusion: The files evaluate DIFFERENT TASKS.\")\n    print(\"  - evaluation.py uses io_ids/s_ids (IOI logit difference)\")\n    print(\"  - eval_mean_ablation.py uses ans_list/wrong_list (Greaterthan year tokens)\")\n    print(\"  - Numbers are incomparable. Both implementations are correct for their task.\")\n    print(\"  - The isinf issue (CSS=1.0 = ACDC) affects both tasks, now resolved with topk.\")\n\n    print(\"\\nDone.\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-13T04:34:16.013729+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/eval_topk_faithfulness.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-13T04:34:16.013955+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat > /root/structfuse-context/eval_topk_faithfulness.py << 'SCRIPT_EOF'\nimport os\nos.environ[\"CUDA_VISIBLE_DEVICES\"] = \"5\"\n\nimport json, math, random, re, sys\nfrom pathlib import Path\nfrom functools import partial\n\nimport torch\nimport numpy as np\n\nsys.path.insert(0, \"/root/structfuse-context\")\n\n_LOCAL_GPT2 = \"/root/autodl-tmp/gpt2-small\"\n_GPT2_ALIASES = (\"gpt2\", \"gpt2-small\", \"openai-community/gpt2\")\n\ndef _patch_hf():\n    from transformers import AutoConfig, AutoTokenizer, AutoModelForCausalLM\n    def _make_patched(orig_fn):\n        def patched(name_or_path, *args, **kwargs):\n            if name_or_path in _GPT2_ALIASES:\n                name_or_path = _LOCAL_GPT2\n            return orig_fn(name_or_path, *args, **kwargs)\n        return patched\n    AutoConfig.from_pretrained = staticmethod(_make_patched(AutoConfig.from_pretrained))\n    AutoTokenizer.from_pretrained = staticmethod(_make_patched(AutoTokenizer.from_pretrained))\n    AutoModelForCausalLM.from_pretrained = staticmethod(_make_patched(AutoModelForCausalLM.from_pretrained))\n\n_patch_hf()\n\nGT_DATASET_PATH = \"/root/miniconda3/lib/python3.12/site-packages/datasets/greaterthan_gpt2-small_prompts.json\"\n\nNAMES = [\"John\", \"Mary\", \"Alice\", \"Bob\", \"Charlie\", \"David\", \"Emma\", \"Frank\",\n         \"Grace\", \"Henry\", \"Jack\", \"Kate\", \"Leo\", \"Mia\", \"Noah\", \"Tom\"]\nTEMPLATES = [\n    \"When {io} and {s} went to the {place}, {s} gave a {obj} to\",\n    \"After {io} and {s} arrived at the {place}, {s} handed a {obj} to\",\n    \"{io} and {s} were at the {place}. {s} gave a {obj} to\",\n    \"Then, {io} and {s} had a meeting at the {place}, {s} passed a {obj} to\",\n]\nPLACES = [\"store\", \"park\", \"library\", \"school\", \"hospital\", \"restaurant\", \"office\"]\nOBJECTS = [\"bottle\", \"book\", \"letter\", \"ball\", \"gift\", \"toy\", \"bag\"]\n\ndef _precompute_year_tokens(tokenizer):\n    tokens = {}\n    for yr in range(100):\n        s = f\"{yr:02d}\"\n        ids = tokenizer.encode(s)\n        tokens[s] = ids[0]\n    return tokens\n\ndef load_gt_data(tokenizer, num_samples=100, seed=42):\n    with open(GT_DATASET_PATH) as f:\n        all_prompts = json.load(f)[\"prompts\"]\n    random.seed(seed)\n    if len(all_prompts) > num_samples:\n        all_prompts = random.sample(all_prompts, num_samples)\n    yr_tok = _precompute_year_tokens(tokenizer)\n    prompts, ans_list, wrong_list = [], [], []\n    for p in all_prompts:\n        prompts.append(p[\"clean\"])\n        ans_ids = torch.tensor([yr_tok[a] for a in p[\"answers\"] if a in yr_tok])\n        wrong_ids = torch.tensor([yr_tok[a] for a in p[\"wrong_answers\"] if a in yr_tok])\n        ans_list.append(ans_ids)\n        wrong_list.append(wrong_ids)\n    return prompts, ans_list, wrong_list\n\ndef generate_ioi_data(tokenizer, num_samples=100, seed=42):\n    random.seed(seed)\n    prompts, labels = [], []\n    for _ in range(num_samples):\n        io_name, s_name = random.sample(NAMES, 2)\n        template = random.choice(TEMPLATES)\n        place = random.choice(PLACES)\n        obj = random.choice(OBJECTS)\n        prompts.append(template.format(io=io_name, s=s_name, place=place, obj=obj))\n        io_tokens = tokenizer.encode(\" \" + io_name)\n        s_tokens = tokenizer.encode(\" \" + s_name)\n        labels.append((io_tokens[0], s_tokens[0]))\n    return prompts, labels\n\ndef load_model(device=\"cuda\"):\n    from transformer_lens import HookedTransformer\n    from transformers import AutoModelForCausalLM\n    hf_model = AutoModelForCausalLM.from_pretrained(_LOCAL_GPT2)\n    model = HookedTransformer.from_pretrained(\"gpt2-small\", hf_model=hf_model, device=device)\n    model.set_use_attn_result(True)\n    model.set_use_split_qkv_input(True)\n    model.set_use_hook_mlp_in(True)\n    return model\n\ndef extract_circuit_nodes(circuit_edges):\n    nodes = set()\n    for edge in circuit_edges:\n        parts = edge.split('->')\n        if len(parts) != 2:\n            continue\n        nodes.add(parts[0].strip())\n        dst_base = re.sub(r'\\.[qkv]$', '', parts[1].strip())\n        nodes.add(dst_base)\n    nodes.discard('input')\n    nodes.discard('logits')\n    return nodes\n\ndef collect_mean_activations(model, tokens):\n    n_layers = model.cfg.n_layers\n    accumulators = {}\n\n    def make_accumulator(key):\n        def hook_fn(value, hook):\n            if key not in accumulators:\n                accumulators[key] = value.detach().mean(dim=0, keepdim=True).clone()\n            else:\n                accumulators[key] += value.detach().mean(dim=0, keepdim=True)\n            return value\n        return hook_fn\n\n    hooks = []\n    for layer in range(n_layers):\n        hooks.append((f\"blocks.{layer}.attn.hook_result\", make_accumulator(f\"attn_{layer}\")))\n        hooks.append((f\"blocks.{layer}.hook_mlp_out\", make_accumulator(f\"mlp_{layer}\")))\n\n    batch_size = 25\n    n_batches = 0\n    with torch.no_grad():\n        for start in range(0, len(tokens), batch_size):\n            batch = tokens[start:start + batch_size]\n            model.run_with_hooks(batch, fwd_hooks=hooks)\n            n_batches += 1\n\n    attn_means, mlp_means = {}, {}\n    for layer in range(n_layers):\n        attn_means[layer] = accumulators[f\"attn_{layer}\"] / n_batches\n        mlp_means[layer] = accumulators[f\"mlp_{layer}\"] / n_batches\n    return attn_means, mlp_means\n\ndef evaluate_circuit(model, circuit_edges, tokens, metric_fn,\n                     ablation_mode=\"zero\", attn_means=None, mlp_means=None):\n    if len(circuit_edges) == 0:\n        return {\"num_edges\": 0, \"cpr\": 0.0, \"cmd\": 0.0}\n\n    circuit_nodes = extract_circuit_nodes(circuit_edges)\n    n_layers, n_heads = model.cfg.n_layers, model.cfg.n_heads\n\n    ablate_heads = {}\n    ablate_mlps = []\n    for layer in range(n_layers):\n        heads = [h for h in range(n_heads) if f'a{layer}.h{h}' not in circuit_nodes]\n        if heads:\n            ablate_heads[layer] = heads\n        if f'm{layer}' not in circuit_nodes:\n            ablate_mlps.append(layer)\n\n    if ablation_mode == \"zero\":\n        def _head_hook(value, hook, heads_to_ablate):\n            for h in heads_to_ablate:\n                value[:, :, h, :] = 0\n            return value\n        def _mlp_hook(value, hook):\n            return torch.zeros_like(value)\n    else:\n        def _head_hook(value, hook, heads_to_ablate, layer_idx=None):\n            mean_val = attn_means[layer_idx]\n            seq_len = value.shape[1]\n            mean_seq = mean_val.shape[1]\n            if mean_seq >= seq_len:\n                m = mean_val[:, -seq_len:, :, :]\n            else:\n                m = torch.nn.functional.pad(mean_val, (0,0,0,0,0,seq_len-mean_seq), mode='replicate')\n            for h in heads_to_ablate:\n                value[:, :, h, :] = m[:, :seq_len, h, :].expand(value.shape[0], -1, -1)\n            return value\n        def _mlp_hook(value, hook, layer_idx=None):\n            mean_val = mlp_means[layer_idx]\n            seq_len = value.shape[1]\n            mean_seq = mean_val.shape[1]\n            if mean_seq >= seq_len:\n                m = mean_val[:, -seq_len:, :]\n            else:\n                m = torch.nn.functional.pad(mean_val, (0,0,0,seq_len-mean_seq), mode='replicate')\n            return m[:, :seq_len, :].expand(value.shape[0], -1, -1)\n\n    with torch.no_grad():\n        baseline_logits = model(tokens)\n        baseline_diff = metric_fn(baseline_logits, tokens)\n\n        hooks = []\n        for layer, heads in ablate_heads.items():\n            if ablation_mode == \"zero\":\n                hooks.append((f\"blocks.{layer}.attn.hook_result\",\n                              partial(_head_hook, heads_to_ablate=heads)))\n            else:\n                hooks.append((f\"blocks.{layer}.attn.hook_result\",\n                              partial(_head_hook, heads_to_ablate=heads, layer_idx=layer)))\n        for layer in ablate_mlps:\n            if ablation_mode == \"zero\":\n                hooks.append((f\"blocks.{layer}.hook_mlp_out\", _mlp_hook))\n            else:\n                hooks.append((f\"blocks.{layer}.hook_mlp_out\", partial(_mlp_hook, layer_idx=layer)))\n\n        circ_logits = model.run_with_hooks(tokens, fwd_hooks=hooks)\n        circuit_diff = metric_fn(circ_logits, tokens)\n\n    cpr = circuit_diff / baseline_diff if abs(baseline_diff) > 1e-6 else 0.0\n    cmd = abs(baseline_diff - circuit_diff)\n    return {\"num_edges\": len(circuit_edges), \"cpr\": round(cpr, 4), \"cmd\": round(cmd, 4)}\n\ndef topk_edges(scores, k):\n    sorted_edges = sorted(\n        scores.items(),\n        key=lambda x: abs(x[1]) if not math.isinf(x[1]) else float('inf'),\n        reverse=True\n    )\n    return set(e for e, _ in sorted_edges[:k])\n\ndef isinf_edges(scores):\n    return set(e for e, v in scores.items() if math.isinf(v))\n\ndef compute_css(methods_edges):\n    K = len(methods_edges)\n    union = set()\n    for edges in methods_edges.values():\n        union |= edges\n    return {e: sum(1 for es in methods_edges.values() if e in es) / K for e in union}\n\ndef threshold_css(css_scores, threshold):\n    return {e for e, s in css_scores.items() if s >= threshold - 1e-2}\n\ndef css_distribution(css_scores):\n    dist = {\"1/3\": 0, \"2/3\": 0, \"3/3\": 0}\n    for s in css_scores.values():\n        if s >= 1.0 - 1e-2:\n            dist[\"3/3\"] += 1\n        elif s >= 0.67 - 1e-2:\n            dist[\"2/3\"] += 1\n        else:\n            dist[\"1/3\"] += 1\n    return dist\n\ndef run_task_evaluation(model, tokens, metric_fn, attn_means, mlp_means,\n                        acdc_scores, eapig_scores, ep_scores,\n                        k_values, task_name):\n    results = {}\n\n    for k in k_values:\n        print(f\"\\n--- k={k} ---\")\n        acdc_circ = topk_edges(acdc_scores, k)\n        eapig_100 = topk_edges(eapig_scores, 100)\n        ep_100 = topk_edges(ep_scores, 100)\n        css_scores = compute_css({\"acdc\": acdc_circ, \"eap_ig\": eapig_100, \"ep\": ep_100})\n        css_10 = threshold_css(css_scores, 1.0)\n        css_067 = threshold_css(css_scores, 0.67)\n        dist = css_distribution(css_scores)\n\n        eapig_k = topk_edges(eapig_scores, k)\n        ep_k = topk_edges(ep_scores, k)\n\n        circuits = {\n            \"CSS=1.0\": css_10,\n            \"CSS>=2/3\": css_067,\n            \"ACDC\": acdc_circ,\n            \"EAP-IG\": eapig_k,\n            \"EP\": ep_k,\n        }\n\n        print(f\"  CSS dist: {dist}\")\n        for name, edges in circuits.items():\n            print(f\"  {name}: {len(edges)} edges\")\n\n        k_results = {\"css_distribution\": dist}\n\n        for mode in [\"zero\", \"mean\"]:\n            print(f\"  [{mode} ablation]\")\n            mode_results = {}\n            for name, edges in circuits.items():\n                r = evaluate_circuit(\n                    model, edges, tokens, metric_fn,\n                    ablation_mode=mode,\n                    attn_means=attn_means if mode == \"mean\" else None,\n                    mlp_means=mlp_means if mode == \"mean\" else None,\n                )\n                r[\"name\"] = name\n                mode_results[name] = r\n                print(f\"    {name} ({len(edges)} edges): CPR={r['cpr']:.4f}, CMD={r['cmd']:.4f}\")\n            k_results[mode] = mode_results\n        results[f\"k={k}\"] = k_results\n\n    print(\"\\n--- Reference: isinf ---\")\n    acdc_inf = isinf_edges(acdc_scores)\n    eapig_100 = topk_edges(eapig_scores, 100)\n    ep_100 = topk_edges(ep_scores, 100)\n    css_inf = compute_css({\"acdc\": acdc_inf, \"eap_ig\": eapig_100, \"ep\": ep_100})\n    css_inf_10 = threshold_css(css_inf, 1.0)\n    css_inf_067 = threshold_css(css_inf, 0.67)\n\n    ref_circuits = {\n        \"ACDC-isinf\": acdc_inf,\n        \"EAP-IG-100\": eapig_100,\n        \"EP-100\": ep_100,\n        \"CSS=1.0-isinf\": css_inf_10,\n        \"CSS>=2/3-isinf\": css_inf_067,\n    }\n\n    ref_results = {}\n    for mode in [\"zero\", \"mean\"]:\n        print(f\"  [{mode} ablation - ref]\")\n        mode_results = {}\n        for name, edges in ref_circuits.items():\n            r = evaluate_circuit(\n                model, edges, tokens, metric_fn,\n                ablation_mode=mode,\n                attn_means=attn_means if mode == \"mean\" else None,\n                mlp_means=mlp_means if mode == \"mean\" else None,\n            )\n            r[\"name\"] = name\n            mode_results[name] = r\n            print(f\"    {name} ({len(edges)} edges): CPR={r['cpr']:.4f}, CMD={r['cmd']:.4f}\")\n        ref_results[mode] = mode_results\n    results[\"isinf_ref\"] = ref_results\n    return results\n\ndef print_summary_table(task_name, results, k_values):\n    print(f\"\\n=== {task_name} Top-K Faithfulness ===\\n\")\n    print(f\"{'Circuit':<20} {'k':>5} {'Edges':>6} {'Zero CPR':>9} {'Zero CMD':>9} {'Mean CPR':>9} {'Mean CMD':>9}\")\n    print(\"-\" * 72)\n    for k in k_values:\n        key = f\"k={k}\"\n        data = results[key]\n        for name in [\"CSS=1.0\", \"CSS>=2/3\", \"ACDC\", \"EAP-IG\", \"EP\"]:\n            z = data[\"zero\"][name]\n            m = data[\"mean\"][name]\n            print(f\"{name:<20} {k:>5} {z['num_edges']:>6} {z['cpr']:>9.4f} {z['cmd']:>9.4f} {m['cpr']:>9.4f} {m['cmd']:>9.4f}\")\n        print()\n    ref = results[\"isinf_ref\"]\n    for name in [\"CSS=1.0-isinf\", \"CSS>=2/3-isinf\", \"ACDC-isinf\", \"EAP-IG-100\", \"EP-100\"]:\n        z = ref[\"zero\"][name]\n        m = ref[\"mean\"][name]\n        print(f\"{name:<20} {'ref':>5} {z['num_edges']:>6} {z['cpr']:>9.4f} {z['cmd']:>9.4f} {m['cpr']:>9.4f} {m['cmd']:>9.4f}\")\n\ndef check_condition_4(task_name, results, k_values):\n    print(f\"\\n--- {task_name}: D025 Condition 4 ---\")\n    for k in k_values:\n        key = f\"k={k}\"\n        data = results[key]\n        for mode in [\"zero\", \"mean\"]:\n            css_cpr = data[mode][\"CSS=1.0\"][\"cpr\"]\n            css_edges = data[mode][\"CSS=1.0\"][\"num_edges\"]\n            methods = [\"ACDC\", \"EAP-IG\", \"EP\"]\n            best_name = max(methods, key=lambda n: data[mode][n][\"cpr\"])\n            best_cpr = data[mode][best_name][\"cpr\"]\n            best_edges = data[mode][best_name][\"num_edges\"]\n            passed = css_cpr > best_cpr\n            status = \"PASS\" if passed else \"FAIL\"\n            print(f\"  k={k} [{mode}]: CSS=1.0 CPR={css_cpr:.4f} ({css_edges}e) vs {best_name} CPR={best_cpr:.4f} ({best_edges}e) -> {status}\")\n\ndef main():\n    device = torch.device(\"cuda\")\n    cache_dir = Path(\"/root/structfuse-context\")\n\n    print(f\"CUDA_VISIBLE_DEVICES={os.environ.get('CUDA_VISIBLE_DEVICES')}\")\n    print(\"Loading model...\")\n    model = load_model(device)\n\n    # Arithmetic\n    print(\"\\n\" + \"=\" * 70)\n    print(\"  ARITHMETIC (Greaterthan)\")\n    print(\"=\" * 70)\n\n    prompts_a, ans_list, wrong_list = load_gt_data(model.tokenizer, num_samples=100, seed=42)\n    tokens_a = model.to_tokens(prompts_a, prepend_bos=True)\n    print(f\"Data: {len(prompts_a)} prompts, tokens {tokens_a.shape}\")\n\n    def metric_arith(logits, tokens):\n        diffs = []\n        for i in range(len(tokens)):\n            diffs.append(logits[i, -1, ans_list[i]].mean() - logits[i, -1, wrong_list[i]].mean())\n        return torch.stack(diffs).mean().item()\n\n    print(\"Collecting mean activations...\")\n    attn_m_a, mlp_m_a = collect_mean_activations(model, tokens_a)\n\n    with open(cache_dir / \"cache_acdc_arith.json\") as f: acdc_a = json.load(f)\n    with open(cache_dir / \"cache_eap_ig_arith.json\") as f: eapig_a = json.load(f)\n    with open(cache_dir / \"cache_ep_arith.json\") as f: ep_a = json.load(f)\n\n    arith_results = run_task_evaluation(\n        model, tokens_a, metric_arith, attn_m_a, mlp_m_a,\n        acdc_a, eapig_a, ep_a,\n        k_values=[50, 75, 100],\n        task_name=\"Arithmetic\"\n    )\n\n    with open(cache_dir / \"faithfulness_arithmetic_topk.json\", \"w\") as f:\n        json.dump(arith_results, f, indent=2)\n    print(f\"\\nSaved: faithfulness_arithmetic_topk.json\")\n\n    # IOI\n    print(\"\\n\" + \"=\" * 70)\n    print(\"  IOI\")\n    print(\"=\" * 70)\n\n    prompts_i, labels_i = generate_ioi_data(model.tokenizer, num_samples=100, seed=42)\n    tokens_i = model.to_tokens(prompts_i, prepend_bos=True)\n    io_ids = torch.tensor([l[0] for l in labels_i])\n    s_ids = torch.tensor([l[1] for l in labels_i])\n    print(f\"Data: {len(prompts_i)} prompts, tokens {tokens_i.shape}\")\n\n    def metric_ioi(logits, tokens):\n        return (logits[range(len(tokens)), -1, io_ids] -\n                logits[range(len(tokens)), -1, s_ids]).mean().item()\n\n    print(\"Collecting mean activations...\")\n    attn_m_i, mlp_m_i = collect_mean_activations(model, tokens_i)\n\n    with open(cache_dir / \"cache_acdc.json\") as f: acdc_i = json.load(f)\n    with open(cache_dir / \"cache_eap_ig.json\") as f: eapig_i = json.load(f)\n    with open(cache_dir / \"cache_edge_pruning.json\") as f: ep_i = json.load(f)\n\n    ioi_results = run_task_evaluation(\n        model, tokens_i, metric_ioi, attn_m_i, mlp_m_i,\n        acdc_i, eapig_i, ep_i,\n        k_values=[50, 100],\n        task_name=\"IOI\"\n    )\n\n    with open(cache_dir / \"faithfulness_ioi_topk.json\", \"w\") as f:\n        json.dump(ioi_results, f, indent=2)\n    print(f\"\\nSaved: faithfulness_ioi_topk.json\")\n\n    # Summary\n    print(\"\\n\" + \"=\" * 70)\n    print(\"  FULL SUMMARY\")\n    print(\"=\" * 70)\n\n    print_summary_table(\"Arithmetic\", arith_results, [50, 75, 100])\n    print_summary_table(\"IOI\", ioi_results, [50, 100])\n    check_condition_4(\"Arithmetic\", arith_results, [50, 75])\n    check_condition_4(\"IOI\", ioi_results, [50, 100])\n\n    print(\"\\n=== IOI CPR Inconsistency Analysis ===\")\n    print(\"phase_d_results.json: IOI task, node-level zero ablation (evaluation.py)\")\n    print(\"mean_ablation_results.json: ARITHMETIC task, not IOI (eval_mean_ablation.py)\")\n    print(\"Conclusion: The files evaluate DIFFERENT TASKS - numbers are incomparable.\")\n    print(\"  evaluation.py uses io_ids/s_ids (IOI logit diff)\")\n    print(\"  eval_mean_ablation.py uses ans_list/wrong_list (Greaterthan year tokens)\")\n    print(\"  Both implementations are correct for their respective task.\")\n\n    print(\"\\nDone.\")\n\nif __name__ == \"__main__\":\n    main()\nSCRIPT_EOF\necho \"Script uploaded OK\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat > /root/structfuse-context/eval_topk_faithfulness.py << 'SCRIPT_EOF'\nimport os\nos.environ[\"CUDA_VISIBLE_DEVICES\"] = \"5\"\n\nimport json, math, random, re, sys\nfrom pathlib import Path\nfrom functools import partial\n\nimport torch\nimport numpy as np\n\nsys.path.insert(0, \"/root/structfuse-context\")\n\n_LOCAL_GPT2 = \"/root/autodl-tmp/gpt2-small\"\n_GPT2_ALIASES = (\"gpt2\", \"gpt2-small\", \"openai-community/gpt2\")\n\ndef _patch_hf():\n    from transformers import AutoConfig, AutoTokenizer, AutoModelForCausalLM\n    def _make_patched(orig_fn):\n        def patched(name_or_path, *args, **kwargs):\n            if name_or_path in _GPT2_ALIASES:\n                name_or_path = _LOCAL_GPT2\n            return orig_fn(name_or_path, *args, **kwargs)\n        return patched\n    AutoConfig.from_pretrained = staticmethod(_make_patched(AutoConfig.from_pretrained))\n    AutoTokenizer.from_pretrained = staticmethod(_make_patched(AutoTokenizer.from_pretrained))\n    AutoModelForCausalLM.from_pretrained = staticmethod(_make_patched(AutoModelForCausalLM.from_pretrained))\n\n_patch_hf()\n\nGT_DATASET_PATH = \"/root/miniconda3/lib/python3.12/site-packages/datasets/greaterthan_gpt2-small_prompts.json\"\n\nNAMES = [\"John\", \"Mary\", \"Alice\", \"Bob\", \"Charlie\", \"David\", \"Emma\", \"Frank\",\n         \"Grace\", \"Henry\", \"Jack\", \"Kate\", \"Leo\", \"Mia\", \"Noah\", \"Tom\"]\nTEMPLATES = [\n    \"When {io} and {s} went to the {place}, {s} gave a {obj} to\",\n    \"After {io} and {s} arrived at the {place}, {s} handed a {obj} to\",\n    \"{io} and {s} were at the {place}. {s} gave a {obj} to\",\n    \"Then, {io} and {s} had a meeting at the {place}, {s} passed a {obj} to\",\n]\nPLACES = [\"store\", \"park\", \"library\", \"school\", \"hospital\", \"restaurant\", \"office\"]\nOBJECTS = [\"bottle\", \"book\", \"letter\", \"ball\", \"gift\", \"toy\", \"bag\"]\n\ndef _precompute_year_tokens(tokenizer):\n    tokens = {}\n    for yr in range(100):\n        s = f\"{yr:02d}\"\n        ids = tokenizer.encode(s)\n        tokens[s] = ids[0]\n    return tokens\n\ndef load_gt_data(tokenizer, num_samples=100, seed=42):\n    with open(GT_DATASET_PATH) as f:\n        all_prompts = json.load(f)[\"prompts\"]\n    random.seed(seed)\n    if len(all_prompts) > num_samples:\n        all_prompts = random.sample(all_prompts, num_samples)\n    yr_tok = _precompute_year_tokens(tokenizer)\n    prompts, ans_list, wrong_list = [], [], []\n    for p in all_prompts:\n        prompts.append(p[\"clean\"])\n        ans_ids = torch.tensor([yr_tok[a] for a in p[\"answers\"] if a in yr_tok])\n        wrong_ids = torch.tensor([yr_tok[a] for a in p[\"wrong_answers\"] if a in yr_tok])\n        ans_list.append(ans_ids)\n        wrong_list.append(wrong_ids)\n    return prompts, ans_list, wrong_list\n\ndef generate_ioi_data(tokenizer, num_samples=100, seed=42):\n    random.seed(seed)\n    prompts, labels = [], []\n    for _ in range(num_samples):\n        io_name, s_name = random.sample(NAMES, 2)\n        template = random.choice(TEMPLATES)\n        place = random.choice(PLACES)\n        obj = random.choice(OBJECTS)\n        prompts.append(template.format(io=io_name, s=s_name, place=place, obj=obj))\n        io_tokens = tokenizer.encode(\" \" + io_name)\n        s_tokens = tokenizer.encode(\" \" + s_name)\n        labels.append((io_tokens[0], s_tokens[0]))\n    return prompts, labels\n\ndef load_model(device=\"cuda\"):\n    from transformer_lens import HookedTransformer\n    from transformers import AutoModelForCausalLM\n    hf_model = AutoModelForCausalLM.from_pretrained(_LOCAL_GPT2)\n    model = HookedTransformer.from_pretrained(\"gpt2-small\", hf_model=hf_model, device=device)\n    model.set_use_attn_result(True)\n    model.set_use_split_qkv_input(True)\n    model.set_use_hook_mlp_in(True)\n    return model\n\ndef extract_circuit_nodes(circuit_edges):\n    nodes = set()\n    for edge in circuit_edges:\n        parts = edge.split('->')\n        if len(parts) != 2:\n            continue\n        nodes.add(parts[0].strip())\n        dst_base = re.sub(r'\\.[qkv]$', '', parts[1].strip())\n        nodes.add(dst_base)\n    nodes.discard('input')\n    nodes.discard('logits')\n    return nodes\n\ndef collect_mean_activations(model, tokens):\n    n_layers = model.cfg.n_layers\n    accumulators = {}\n\n    def make_accumulator(key):\n        def hook_fn(value, hook):\n            if key not in accumulators:\n                accumulators[key] = value.detach().mean(dim=0, keepdim=True).clone()\n            else:\n                accumulators[key] += value.detach().mean(dim=0, keepdim=True)\n            return value\n        return hook_fn\n\n    hooks = []\n    for layer in range(n_layers):\n        hooks.append((f\"blocks.{layer}.attn.hook_result\", make_accumulator(f\"attn_{layer}\")))\n        hooks.append((f\"blocks.{layer}.hook_mlp_out\", make_accumulator(f\"mlp_{layer}\")))\n\n    batch_size = 25\n    n_batches = 0\n    with torch.no_grad():\n        for start in range(0, len(tokens), batch_size):\n            batch = tokens[start:start + batch_size]\n            model.run_with_hooks(batch, fwd_hooks=hooks)\n            n_batches += 1\n\n    attn_means, mlp_means = {}, {}\n    for layer in range(n_layers):\n        attn_means[layer] = accumulators[f\"attn_{layer}\"] / n_batches\n        mlp_means[layer] = accumulators[f\"mlp_{layer}\"] / n_batches\n    return attn_means, mlp_means\n\ndef evaluate_circuit(model, circuit_edges, tokens, metric_fn,\n                     ablation_mode=\"zero\", attn_means=None, mlp_means=None):\n    if len(circuit_edges) == 0:\n        return {\"num_edges\": 0, \"cpr\": 0.0, \"cmd\": 0.0}\n\n    circuit_nodes = extract_circuit_nodes(circuit_edges)\n    n_layers, n_heads = model.cfg.n_layers, model.cfg.n_heads\n\n    ablate_heads = {}\n    ablate_mlps = []\n    for layer in range(n_layers):\n        heads = [h for h in range(n_heads) if f'a{layer}.h{h}' not in circuit_nodes]\n        if heads:\n            ablate_heads[layer] = heads\n        if f'm{layer}' not in circuit_nodes:\n            ablate_mlps.append(layer)\n\n    if ablation_mode == \"zero\":\n        def _head_hook(value, hook, heads_to_ablate):\n            for h in heads_to_ablate:\n                value[:, :, h, :] = 0\n            return value\n        def _mlp_hook(value, hook):\n            return torch.zeros_like(value)\n    else:\n        def _head_hook(value, hook, heads_to_ablate, layer_idx=None):\n            mean_val = attn_means[layer_idx]\n            seq_len = value.shape[1]\n            mean_seq = mean_val.shape[1]\n            if mean_seq >= seq_len:\n                m = mean_val[:, -seq_len:, :, :]\n            else:\n                m = torch.nn.functional.pad(mean_val, (0,0,0,0,0,seq_len-mean_seq), mode='replicate')\n            for h in heads_to_ablate:\n                value[:, :, h, :] = m[:, :seq_len, h, :].expand(value.shape[0], -1, -1)\n            return value\n        def _mlp_hook(value, hook, layer_idx=None):\n            mean_val = mlp_means[layer_idx]\n            seq_len = value.shape[1]\n            mean_seq = mean_val.shape[1]\n            if mean_seq >= seq_len:\n                m = mean_val[:, -seq_len:, :]\n            else:\n                m = torch.nn.functional.pad(mean_val, (0,0,0,seq_len-mean_seq), mode='replicate')\n            return m[:, :seq_len, :].expand(value.shape[0], -1, -1)\n\n    with torch.no_grad():\n        baseline_logits = model(tokens)\n        baseline_diff = metric_fn(baseline_logits, tokens)\n\n        hooks = []\n        for layer, heads in ablate_heads.items():\n            if ablation_mode == \"zero\":\n                hooks.append((f\"blocks.{layer}.attn.hook_result\",\n                              partial(_head_hook, heads_to_ablate=heads)))\n            else:\n                hooks.append((f\"blocks.{layer}.attn.hook_result\",\n                              partial(_head_hook, heads_to_ablate=heads, layer_idx=layer)))\n        for layer in ablate_mlps:\n            if ablation_mode == \"zero\":\n                hooks.append((f\"blocks.{layer}.hook_mlp_out\", _mlp_hook))\n            else:\n                hooks.append((f\"blocks.{layer}.hook_mlp_out\", partial(_mlp_hook, layer_idx=layer)))\n\n        circ_logits = model.run_with_hooks(tokens, fwd_hooks=hooks)\n        circuit_diff = metric_fn(circ_logits, tokens)\n\n    cpr = circuit_diff / baseline_diff if abs(baseline_diff) > 1e-6 else 0.0\n    cmd = abs(baseline_diff - circuit_diff)\n    return {\"num_edges\": len(circuit_edges), \"cpr\": round(cpr, 4), \"cmd\": round(cmd, 4)}\n\ndef topk_edges(scores, k):\n    sorted_edges = sorted(\n        scores.items(),\n        key=lambda x: abs(x[1]) if not math.isinf(x[1]) else float('inf'),\n        reverse=True\n    )\n    return set(e for e, _ in sorted_edges[:k])\n\ndef isinf_edges(scores):\n    return set(e for e, v in scores.items() if math.isinf(v))\n\ndef compute_css(methods_edges):\n    K = len(methods_edges)\n    union = set()\n    for edges in methods_edges.values():\n        union |= edges\n    return {e: sum(1 for es in methods_edges.values() if e in es) / K for e in union}\n\ndef threshold_css(css_scores, threshold):\n    return {e for e, s in css_scores.items() if s >= threshold - 1e-2}\n\ndef css_distribution(css_scores):\n    dist = {\"1/3\": 0, \"2/3\": 0, \"3/3\": 0}\n    for s in css_scores.values():\n        if s >= 1.0 - 1e-2:\n            dist[\"3/3\"] += 1\n        elif s >= 0.67 - 1e-2:\n            dist[\"2/3\"] += 1\n        else:\n            dist[\"1/3\"] += 1\n    return dist\n\ndef run_task_evaluation(model, tokens, metric_fn, attn_means, mlp_means,\n                        acdc_scores, eapig_scores, ep_scores,\n                        k_values, task_name):\n    results = {}\n\n    for k in k_values:\n        print(f\"\\n--- k={k} ---\")\n        acdc_circ = topk_edges(acdc_scores, k)\n        eapig_100 = topk_edges(eapig_scores, 100)\n        ep_100 = topk_edges(ep_scores, 100)\n        css_scores = compute_css({\"acdc\": acdc_circ, \"eap_ig\": eapig_100, \"ep\": ep_100})\n        css_10 = threshold_css(css_scores, 1.0)\n        css_067 = threshold_css(css_scores, 0.67)\n        dist = css_distribution(css_scores)\n\n        eapig_k = topk_edges(eapig_scores, k)\n        ep_k = topk_edges(ep_scores, k)\n\n        circuits = {\n            \"CSS=1.0\": css_10,\n            \"CSS>=2/3\": css_067,\n            \"ACDC\": acdc_circ,\n            \"EAP-IG\": eapig_k,\n            \"EP\": ep_k,\n        }\n\n        print(f\"  CSS dist: {dist}\")\n        for name, edges in circuits.items():\n            print(f\"  {name}: {len(edges)} edges\")\n\n        k_results = {\"css_distribution\": dist}\n\n        for mode in [\"zero\", \"mean\"]:\n            print(f\"  [{mode} ablation]\")\n            mode_results = {}\n            for name, edges in circuits.items():\n                r = evaluate_circuit(\n                    model, edges, tokens, metric_fn,\n                    ablation_mode=mode,\n                    attn_means=attn_means if mode == \"mean\" else None,\n                    mlp_means=mlp_means if mode == \"mean\" else None,\n                )\n                r[\"name\"] = name\n                mode_results[name] = r\n                print(f\"    {name} ({len(edges)} edges): CPR={r['cpr']:.4f}, CMD={r['cmd']:.4f}\")\n            k_results[mode] = mode_results\n        results[f\"k={k}\"] = k_results\n\n    print(\"\\n--- Reference: isinf ---\")\n    acdc_inf = isinf_edges(acdc_scores)\n    eapig_100 = topk_edges(eapig_scores, 100)\n    ep_100 = topk_edges(ep_scores, 100)\n    css_inf = compute_css({\"acdc\": acdc_inf, \"eap_ig\": eapig_100, \"ep\": ep_100})\n    css_inf_10 = threshold_css(css_inf, 1.0)\n    css_inf_067 = threshold_css(css_inf, 0.67)\n\n    ref_circuits = {\n        \"ACDC-isinf\": acdc_inf,\n        \"EAP-IG-100\": eapig_100,\n        \"EP-100\": ep_100,\n        \"CSS=1.0-isinf\": css_inf_10,\n        \"CSS>=2/3-isinf\": css_inf_067,\n    }\n\n    ref_results = {}\n    for mode in [\"zero\", \"mean\"]:\n        print(f\"  [{mode} ablation - ref]\")\n        mode_results = {}\n        for name, edges in ref_circuits.items():\n            r = evaluate_circuit(\n                model, edges, tokens, metric_fn,\n                ablation_mode=mode,\n                attn_means=attn_means if mode == \"mean\" else None,\n                mlp_means=mlp_means if mode == \"mean\" else None,\n            )\n            r[\"name\"] = name\n            mode_results[name] = r\n            print(f\"    {name} ({len(edges)} edges): CPR={r['cpr']:.4f}, CMD={r['cmd']:.4f}\")\n        ref_results[mode] = mode_results\n    results[\"isinf_ref\"] = ref_results\n    return results\n\ndef print_summary_table(task_name, results, k_values):\n    print(f\"\\n=== {task_name} Top-K Faithfulness ===\\n\")\n    print(f\"{'Circuit':<20} {'k':>5} {'Edges':>6} {'Zero CPR':>9} {'Zero CMD':>9} {'Mean CPR':>9} {'Mean CMD':>9}\")\n    print(\"-\" * 72)\n    for k in k_values:\n        key = f\"k={k}\"\n        data = results[key]\n        for name in [\"CSS=1.0\", \"CSS>=2/3\", \"ACDC\", \"EAP-IG\", \"EP\"]:\n            z = data[\"zero\"][name]\n            m = data[\"mean\"][name]\n            print(f\"{name:<20} {k:>5} {z['num_edges']:>6} {z['cpr']:>9.4f} {z['cmd']:>9.4f} {m['cpr']:>9.4f} {m['cmd']:>9.4f}\")\n        print()\n    ref = results[\"isinf_ref\"]\n    for name in [\"CSS=1.0-isinf\", \"CSS>=2/3-isinf\", \"ACDC-isinf\", \"EAP-IG-100\", \"EP-100\"]:\n        z = ref[\"zero\"][name]\n        m = ref[\"mean\"][name]\n        print(f\"{name:<20} {'ref':>5} {z['num_edges']:>6} {z['cpr']:>9.4f} {z['cmd']:>9.4f} {m['cpr']:>9.4f} {m['cmd']:>9.4f}\")\n\ndef check_condition_4(task_name, results, k_values):\n    print(f\"\\n--- {task_name}: D025 Condition 4 ---\")\n    for k in k_values:\n        key = f\"k={k}\"\n        data = results[key]\n        for mode in [\"zero\", \"mean\"]:\n            css_cpr = data[mode][\"CSS=1.0\"][\"cpr\"]\n            css_edges = data[mode][\"CSS=1.0\"][\"num_edges\"]\n            methods = [\"ACDC\", \"EAP-IG\", \"EP\"]\n            best_name = max(methods, key=lambda n: data[mode][n][\"cpr\"])\n            best_cpr = data[mode][best_name][\"cpr\"]\n            best_edges = data[mode][best_name][\"num_edges\"]\n            passed = css_cpr > best_cpr\n            status = \"PASS\" if passed else \"FAIL\"\n            print(f\"  k={k} [{mode}]: CSS=1.0 CPR={css_cpr:.4f} ({css_edges}e) vs {best_name} CPR={best_cpr:.4f} ({best_edges}e) -> {status}\")\n\ndef main():\n    device = torch.device(\"cuda\")\n    cache_dir = Path(\"/root/structfuse-context\")\n\n    print(f\"CUDA_VISIBLE_DEVICES={os.environ.get('CUDA_VISIBLE_DEVICES')}\")\n    print(\"Loading model...\")\n    model = load_model(device)\n\n    # Arithmetic\n    print(\"\\n\" + \"=\" * 70)\n    print(\"  ARITHMETIC (Greaterthan)\")\n    print(\"=\" * 70)\n\n    prompts_a, ans_list, wrong_list = load_gt_data(model.tokenizer, num_samples=100, seed=42)\n    tokens_a = model.to_tokens(prompts_a, prepend_bos=True)\n    print(f\"Data: {len(prompts_a)} prompts, tokens {tokens_a.shape}\")\n\n    def metric_arith(logits, tokens):\n        diffs = []\n        for i in range(len(tokens)):\n            diffs.append(logits[i, -1, ans_list[i]].mean() - logits[i, -1, wrong_list[i]].mean())\n        return torch.stack(diffs).mean().item()\n\n    print(\"Collecting mean activations...\")\n    attn_m_a, mlp_m_a = collect_mean_activations(model, tokens_a)\n\n    with open(cache_dir / \"cache_acdc_arith.json\") as f: acdc_a = json.load(f)\n    with open(cache_dir / \"cache_eap_ig_arith.json\") as f: eapig_a = json.load(f)\n    with open(cache_dir / \"cache_ep_arith.json\") as f: ep_a = json.load(f)\n\n    arith_results = run_task_evaluation(\n        model, tokens_a, metric_arith, attn_m_a, mlp_m_a,\n        acdc_a, eapig_a, ep_a,\n        k_values=[50, 75, 100],\n        task_name=\"Arithmetic\"\n    )\n\n    with open(cache_dir / \"faithfulness_arithmetic_topk.json\", \"w\") as f:\n        json.dump(arith_results, f, indent=2)\n    print(f\"\\nSaved: faithfulness_arithmetic_topk.json\")\n\n    # IOI\n    print(\"\\n\" + \"=\" * 70)\n    print(\"  IOI\")\n    print(\"=\" * 70)\n\n    prompts_i, labels_i = generate_ioi_data(model.tokenizer, num_samples=100, seed=42)\n    tokens_i = model.to_tokens(prompts_i, prepend_bos=True)\n    io_ids = torch.tensor([l[0] for l in labels_i])\n    s_ids = torch.tensor([l[1] for l in labels_i])\n    print(f\"Data: {len(prompts_i)} prompts, tokens {tokens_i.shape}\")\n\n    def metric_ioi(logits, tokens):\n        return (logits[range(len(tokens)), -1, io_ids] -\n                logits[range(len(tokens)), -1, s_ids]).mean().item()\n\n    print(\"Collecting mean activations...\")\n    attn_m_i, mlp_m_i = collect_mean_activations(model, tokens_i)\n\n    with open(cache_dir / \"cache_acdc.json\") as f: acdc_i = json.load(f)\n    with open(cache_dir / \"cache_eap_ig.json\") as f: eapig_i = json.load(f)\n    with open(cache_dir / \"cache_edge_pruning.json\") as f: ep_i = json.load(f)\n\n    ioi_results = run_task_evaluation(\n        model, tokens_i, metric_ioi, attn_m_i, mlp_m_i,\n        acdc_i, eapig_i, ep_i,\n        k_values=[50, 100],\n        task_name=\"IOI\"\n    )\n\n    with open(cache_dir / \"faithfulness_ioi_topk.json\", \"w\") as f:\n        json.dump(ioi_results, f, indent=2)\n    print(f\"\\nSaved: faithfulness_ioi_topk.json\")\n\n    # Summary\n    print(\"\\n\" + \"=\" * 70)\n    print(\"  FULL SUMMARY\")\n    print(\"=\" * 70)\n\n    print_summary_table(\"Arithmetic\", arith_results, [50, 75, 100])\n    print_summary_table(\"IOI\", ioi_results, [50, 100])\n    check_condition_4(\"Arithmetic\", arith_results, [50, 75])\n    check_condition_4(\"IOI\", ioi_results, [50, 100])\n\n    print(\"\\n=== IOI CPR Inconsistency Analysis ===\")\n    print(\"phase_d_results.json: IOI task, node-level zero ablation (evaluation.py)\")\n    print(\"mean_ablation_results.json: ARITHMETIC task, not IOI (eval_mean_ablation.py)\")\n    print(\"Conclusion: The files evaluate DIFFERENT TASKS - numbers are incomparable.\")\n    print(\"  evaluation.py uses io_ids/s_ids (IOI logit diff)\")\n    print(\"  eval_mean_ablation.py uses ans_list/wrong_list (Greaterthan year tokens)\")\n    print(\"  Both implementations are correct for their respective task.\")\n\n    print(\"\\nDone.\")\n\nif __name__ == \"__main__\":\n    main()\nSCRIPT_EOF\necho \"Script uploaded OK\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-13T04:34:16.014244+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Script uploaded OK\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-13T04:34:16.014390+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && echo \"CUDA=$CUDA_VISIBLE_DEVICES\" && cd /root/structfuse-context && nohup python eval_topk_faithfulness.py > /tmp/eval_topk.log 2>&1 & echo \"PID=$!\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && echo \"CUDA=$CUDA_VISIBLE_DEVICES\" && cd /root/structfuse-context && nohup python eval_topk_faithfulness.py > /tmp/eval_topk.log 2>&1 & echo \"PID=$!\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-13T04:34:16.014522+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && echo \\\"CUDA=$CUDA_VISIBLE_DEVICES\\\" && cd /root/structfuse-context && nohup python eval_topk_faithfulness.py > /tmp/eval_topk.log 2>&1 & echo \\\"PID=$!\\\"'\\n\\nStdout:\\n\\nPID=716585\\nCUDA=\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 30.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-13T04:34:16.014671+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "tail -30 /tmp/eval_topk.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "tail -30 /tmp/eval_topk.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-13T04:34:16.014826+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"bitsandbytes library load error: libnvJitLink.so.13: cannot open shared object file: No such file or directory\\nTraceback (most recent call last):\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/bitsandbytes/cextension.py\\\", line 320, in &lt;module>\\n    lib = get_native_library()\\n          ^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/bitsandbytes/cextension.py\\\", line 298, in get_native_library\\n    dll = ct.cdll.LoadLibrary(str(binary_path))\\n          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/ctypes/__init__.py\\\", line 460, in LoadLibrary\\n    return self._dlltype(name)\\n           ^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/ctypes/__init__.py\\\", line 379, in __init__\\n    self._handle = _dlopen(self._name, mode)\\n                   ^^^^^^^^^^^^^^^^^^^^^^^^^\\nOSError: libnvJitLink.so.13: cannot open shared object file: No such file or directory\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.2}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-13T04:34:16.014984+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "wc -l /tmp/eval_topk.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "wc -l /tmp/eval_topk.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-13T04:34:16.015107+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"15 /tmp/eval_topk.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-13T04:34:16.015220+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ps -p 716585 -o pid=",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ps -p 716585 -o pid=",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-13T04:34:16.015335+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"716585\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-13T04:34:16.015460+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "tail -20 /tmp/eval_topk.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "tail -20 /tmp/eval_topk.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-13T04:34:16.015586+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"bitsandbytes library load error: libnvJitLink.so.13: cannot open shared object file: No such file or directory\\nTraceback (most recent call last):\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/bitsandbytes/cextension.py\\\", line 320, in &lt;module>\\n    lib = get_native_library()\\n          ^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/bitsandbytes/cextension.py\\\", line 298, in get_native_library\\n    dll = ct.cdll.LoadLibrary(str(binary_path))\\n          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/ctypes/__init__.py\\\", line 460, in LoadLibrary\\n    return self._dlltype(name)\\n           ^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/ctypes/__init__.py\\\", line 379, in __init__\\n    self._handle = _dlopen(self._name, mode)\\n                   ^^^^^^^^^^^^^^^^^^^^^^^^^\\nOSError: libnvJitLink.so.13: cannot open shared object file: No such file or directory\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-13T04:34:16.015749+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "wc -l /tmp/eval_topk.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "wc -l /tmp/eval_topk.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-13T04:34:16.015878+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ps -p 716585 -o pid=",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ps -p 716585 -o pid=",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-13T04:34:16.015995+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"15 /tmp/eval_topk.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-13T04:34:16.016109+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"716585\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-13T04:34:16.016248+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "tail -30 /tmp/eval_topk.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "tail -30 /tmp/eval_topk.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-13T04:34:16.016367+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ps -p 716585 -o pid=",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ps -p 716585 -o pid=",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-13T04:34:16.016492+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"bitsandbytes library load error: libnvJitLink.so.13: cannot open shared object file: No such file or directory\\nTraceback (most recent call last):\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/bitsandbytes/cextension.py\\\", line 320, in &lt;module>\\n    lib = get_native_library()\\n          ^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/bitsandbytes/cextension.py\\\", line 298, in get_native_library\\n    dll = ct.cdll.LoadLibrary(str(binary_path))\\n          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/ctypes/__init__.py\\\", line 460, in LoadLibrary\\n    return self._dlltype(name)\\n           ^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/ctypes/__init__.py\\\", line 379, in __init__\\n    self._handle = _dlopen(self._name, mode)\\n                   ^^^^^^^^^^^^^^^^^^^^^^^^^\\nOSError: libnvJitLink.so.13: cannot open shared object file: No such file or directory\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-13T04:34:16.016611+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"716585\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.48}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-13T04:34:16.016765+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "kill 716585 2>/dev/null; sleep 1; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/structfuse-context && nohup python -u eval_topk_faithfulness.py > /tmp/eval_topk.log 2>&1 & echo \"PID=$!\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "kill 716585 2>/dev/null; sleep 1; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/structfuse-context && nohup python -u eval_topk_faithfulness.py > /tmp/eval_topk.log 2>&1 & echo \"PID=$!\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-13T04:34:16.016901+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'kill 716585 2>/dev/null; sleep 1; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/structfuse-context && nohup python -u eval_topk_faithfulness.py > /tmp/eval_topk.log 2>&1 & echo \\\"PID=$!\\\"'\\n\\nStdout:\\n\\nPID=731244\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 30.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-13T04:34:16.017100+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "tail -10 /tmp/eval_topk.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "tail -10 /tmp/eval_topk.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-13T04:34:16.017240+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\n=== IOI CPR Inconsistency Analysis ===\\nphase_d_results.json: IOI task, node-level zero ablation (evaluation.py)\\nmean_ablation_results.json: ARITHMETIC task, not IOI (eval_mean_ablation.py)\\nConclusion: The files evaluate DIFFERENT TASKS - numbers are incomparable.\\n  evaluation.py uses io_ids/s_ids (IOI logit diff)\\n  eval_mean_ablation.py uses ans_list/wrong_list (Greaterthan year tokens)\\n  Both implementations are correct for their respective task.\\n\\nDone.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.98}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-13T04:34:16.017442+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /tmp/eval_topk.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /tmp/eval_topk.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-13T04:34:16.017719+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"CUDA_VISIBLE_DEVICES=5\\nLoading model...\\nbitsandbytes library load error: libnvJitLink.so.13: cannot open shared object file: No such file or directory\\nTraceback (most recent call last):\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/bitsandbytes/cextension.py\\\", line 320, in &lt;module>\\n    lib = get_native_library()\\n          ^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/bitsandbytes/cextension.py\\\", line 298, in get_native_library\\n    dll = ct.cdll.LoadLibrary(str(binary_path))\\n          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/ctypes/__init__.py\\\", line 460, in LoadLibrary\\n    return self._dlltype(name)\\n           ^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/ctypes/__init__.py\\\", line 379, in __init__\\n    self._handle = _dlopen(self._name, mode)\\n                   ^^^^^^^^^^^^^^^^^^^^^^^^^\\nOSError: libnvJitLink.so.13: cannot open shared object file: No such file or directory\\nLoaded pretrained model gpt2-small into HookedTransformer\\n\\n======================================================================\\n  ARITHMETIC (Greaterthan)\\n======================================================================\\nData: 100 prompts, tokens torch.Size([100, 11])\\nCollecting mean activations...\\n\\n--- k=50 ---\\n  CSS dist: {'1/3': 40, '2/3': 39, '3/3': 44}\\n  CSS=1.0: 44 edges\\n  CSS>=2/3: 83 edges\\n  ACDC: 50 edges\\n  EAP-IG: 50 edges\\n  EP: 50 edges\\n  [zero ablation]\\n    CSS=1.0 (44 edges): CPR=-0.2411, CMD=5.4497\\n    CSS>=2/3 (83 edges): CPR=-0.1756, CMD=5.1618\\n    ACDC (50 edges): CPR=-0.2335, CMD=5.4159\\n    EAP-IG (50 edges): CPR=-0.0900, CMD=4.7861\\n    EP (50 edges): CPR=-0.0934, CMD=4.8010\\n  [mean ablation]\\n    CSS=1.0 (44 edges): CPR=0.9186, CMD=0.3574\\n    CSS>=2/3 (83 edges): CPR=0.9577, CMD=0.1859\\n    ACDC (50 edges): CPR=0.9073, CMD=0.4071\
…[truncated 6569 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-13T04:34:16.017915+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/structfuse-context/faithfulness_arithmetic_topk.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/structfuse-context/faithfulness_arithmetic_topk.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-13T04:34:16.018044+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/structfuse-context/faithfulness_ioi_topk.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/structfuse-context/faithfulness_ioi_topk.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-13T04:34:16.018293+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"k=50\\\": {\\n    \\\"css_distribution\\\": {\\n      \\\"1/3\\\": 40,\\n      \\\"2/3\\\": 39,\\n      \\\"3/3\\\": 44\\n    },\\n    \\\"zero\\\": {\\n      \\\"CSS=1.0\\\": {\\n        \\\"num_edges\\\": 44,\\n        \\\"cpr\\\": -0.2411,\\n        \\\"cmd\\\": 5.4497,\\n        \\\"name\\\": \\\"CSS=1.0\\\"\\n      },\\n      \\\"CSS>=2/3\\\": {\\n        \\\"num_edges\\\": 83,\\n        \\\"cpr\\\": -0.1756,\\n        \\\"cmd\\\": 5.1618,\\n        \\\"name\\\": \\\"CSS>=2/3\\\"\\n      },\\n      \\\"ACDC\\\": {\\n        \\\"num_edges\\\": 50,\\n        \\\"cpr\\\": -0.2335,\\n        \\\"cmd\\\": 5.4159,\\n        \\\"name\\\": \\\"ACDC\\\"\\n      },\\n      \\\"EAP-IG\\\": {\\n        \\\"num_edges\\\": 50,\\n        \\\"cpr\\\": -0.09,\\n        \\\"cmd\\\": 4.7861,\\n        \\\"name\\\": \\\"EAP-IG\\\"\\n      },\\n      \\\"EP\\\": {\\n        \\\"num_edges\\\": 50,\\n        \\\"cpr\\\": -0.0934,\\n        \\\"cmd\\\": 4.801,\\n        \\\"name\\\": \\\"EP\\\"\\n      }\\n    },\\n    \\\"mean\\\": {\\n      \\\"CSS=1.0\\\": {\\n        \\\"num_edges\\\": 44,\\n        \\\"cpr\\\": 0.9186,\\n        \\\"cmd\\\": 0.3574,\\n        \\\"name\\\": \\\"CSS=1.0\\\"\\n      },\\n      \\\"CSS>=2/3\\\": {\\n        \\\"num_edges\\\": 83,\\n        \\\"cpr\\\": 0.9577,\\n        \\\"cmd\\\": 0.1859,\\n        \\\"name\\\": \\\"CSS>=2/3\\\"\\n      },\\n      \\\"ACDC\\\": {\\n        \\\"num_edges\\\": 50,\\n        \\\"cpr\\\": 0.9073,\\n        \\\"cmd\\\": 0.4071,\\n        \\\"name\\\": \\\"ACDC\\\"\\n      },\\n      \\\"EAP-IG\\\": {\\n        \\\"num_edges\\\": 50,\\n        \\\"cpr\\\": 0.9853,\\n        \\\"cmd\\\": 0.0644,\\n        \\\"name\\\": \\\"EAP-IG\\\"\\n      },\\n      \\\"EP\\\": {\\n        \\\"num_edges\\\": 50,\\n        \\\"cpr\\\": 0.9619,\\n        \\\"cmd\\\": 0.1672,\\n        \\\"name\\\": \\\"EP\\\"\\n      }\\n    }\\n  },\\n  \\\"k=75\\\": {\\n    \\\"css_distr
…[truncated 5781 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-13T04:34:16.018555+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"k=50\\\": {\\n    \\\"css_distribution\\\": {\\n      \\\"1/3\\\": 96,\\n      \\\"2/3\\\": 56,\\n      \\\"3/3\\\": 14\\n    },\\n    \\\"zero\\\": {\\n      \\\"CSS=1.0\\\": {\\n        \\\"num_edges\\\": 14,\\n        \\\"cpr\\\": 0.1087,\\n        \\\"cmd\\\": 0.9118,\\n        \\\"name\\\": \\\"CSS=1.0\\\"\\n      },\\n      \\\"CSS>=2/3\\\": {\\n        \\\"num_edges\\\": 70,\\n        \\\"cpr\\\": -0.1512,\\n        \\\"cmd\\\": 1.1777,\\n        \\\"name\\\": \\\"CSS>=2/3\\\"\\n      },\\n      \\\"ACDC\\\": {\\n        \\\"num_edges\\\": 50,\\n        \\\"cpr\\\": 0.0088,\\n        \\\"cmd\\\": 1.014,\\n        \\\"name\\\": \\\"ACDC\\\"\\n      },\\n      \\\"EAP-IG\\\": {\\n        \\\"num_edges\\\": 50,\\n        \\\"cpr\\\": 0.0905,\\n        \\\"cmd\\\": 0.9305,\\n        \\\"name\\\": \\\"EAP-IG\\\"\\n      },\\n      \\\"EP\\\": {\\n        \\\"num_edges\\\": 50,\\n        \\\"cpr\\\": -0.0182,\\n        \\\"cmd\\\": 1.0416,\\n        \\\"name\\\": \\\"EP\\\"\\n      }\\n    },\\n    \\\"mean\\\": {\\n      \\\"CSS=1.0\\\": {\\n        \\\"num_edges\\\": 14,\\n        \\\"cpr\\\": 0.1803,\\n        \\\"cmd\\\": 0.8386,\\n        \\\"name\\\": \\\"CSS=1.0\\\"\\n      },\\n      \\\"CSS>=2/3\\\": {\\n        \\\"num_edges\\\": 70,\\n        \\\"cpr\\\": 0.223,\\n        \\\"cmd\\\": 0.7949,\\n        \\\"name\\\": \\\"CSS>=2/3\\\"\\n      },\\n      \\\"ACDC\\\": {\\n        \\\"num_edges\\\": 50,\\n        \\\"cpr\\\": 0.1987,\\n        \\\"cmd\\\": 0.8198,\\n        \\\"name\\\": \\\"ACDC\\\"\\n      },\\n      \\\"EAP-IG\\\": {\\n        \\\"num_edges\\\": 50,\\n        \\\"cpr\\\": 0.1794,\\n        \\\"cmd\\\": 0.8395,\\n        \\\"name\\\": \\\"EAP-IG\\\"\\n      },\\n      \\\"EP\\\": {\\n        \\\"num_edges\\\": 50,\\n        \\\"cpr\\\": 0.1902,\\n        \\\"cmd\\\": 0.8284,\\n        \\\"name\\\": \\\"EP\\\"\\n      }\\n    }\\n  },\\n  \\\"k=100\\\": {\\n    \\\"css_distri
…[truncated 3871 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 79 · 2026-05-13T04:34:16.018806+00:00_

评估完成。完整结果：

## Arithmetic Top-K Faithfulness

| Circuit | k | Edges | Zero CPR | Zero CMD | Mean CPR | Mean CMD |
|---------|---|-------|----------|----------|----------|----------|
| CSS=1.0 | 50 | 44 | -0.2411 | 5.4497 | 0.9186 | 0.3574 |
| CSS>=2/3 | 50 | 83 | -0.1756 | 5.1618 | 0.9577 | 0.1859 |
| ACDC | 50 | 50 | -0.2335 | 5.4159 | 0.9073 | 0.4071 |
| EAP-IG | 50 | 50 | -0.0900 | 4.7861 | **0.9853** | 0.0644 |
| EP | 50 | 50 | -0.0934 | 4.8010 | 0.9619 | 0.1672 |
| CSS=1.0 | 75 | 54 | -0.2411 | 5.4497 | 0.9186 | 0.3574 |
| CSS>=2/3 | 75 | 85 | -0.1756 | 5.1618 | 0.9577 | 0.1859 |
| ACDC | 75 | 75 | -0.2108 | 5.3163 | 0.9493 | 0.2227 |
| EAP-IG | 75 | 75 | -0.0433 | 4.5808 | **0.9959** | 0.0180 |
| EP | 75 | 75 | -0.1262 | 4.9449 | 0.9582 | 0.1836 |
| CSS=1.0-isinf | ref | 17 | -0.1836 | 5.1970 | 0.9845 | 0.0679 |
| ACDC-isinf | ref | 17 | -0.1836 | 5.1970 | 0.9845 | 0.0679 |

## IOI Top-K Faithfulness

| Circuit | k | Edges | Zero CPR | Zero CMD | Mean CPR | Mean CMD |
|---------|---|-------|----------|----------|----------|----------|
| **CSS=1.0** | **50** | **14** | **0.1087** | 0.9118 | **0.1803** | 0.8386 |
| CSS>=2/3 | 50 | 70 | -0.1512 | 1.1777 | 0.2230 | 0.7949 |
| ACDC | 50 | 50 | 0.0088 | 1.0140 | 0.1987 | 0.8198 |
| EAP-IG | 50 | 50 | 0.0905 | 0.9305 | 0.1794 | 0.8395 |
| EP | 50 | 50 | -0.0182 | 1.0416 | 0.1902 | 0.8284 |
| **CSS=1.0** | **100** | **24** | **0.1099** | 0.9106 | **0.1760** | 0.8430 |
| CSS>=2/3 | 100 | 84 | -0.1633 | 1.1902 | 0.1746 | 0.8444 |
| ACDC | 100 | 100 | -0.0017 | 1.0248 | 0.1440 | 0.8757 |
| EAP-IG | 100 | 100 | -0.1092 | 1.1348 | 0.1003 | 0.9205 |
| EP | 100 | 100 | -0.2413 | 1.2699 | 0.1722 | 0.8469 |
| CSS=1.0-isinf | ref | 7 | 0.1095 | 0.9110 | 0.1717 | 0.8473 |

## D025 条件④检验

**Arithmetic：FAIL**
- k=50 [mean]: CSS=1.0 CPR=0.9186 (44e) < EAP-IG CPR=0.9853 (50e)
- k=75 [mean]: CSS=1.0 CPR=0.9186 (54e) < EAP-IG CPR=0.9959 (75e)

**IOI：混合结果**
- k=50 [zero]: CSS=1.0 CPR=0.1087 (14e) > EAP-IG CPR=0.0905 (50e) → **PASS**
- k=50 [mean]: CSS=1.0 CPR=0.1803 (14e) < ACDC CPR=0.1987 (50e) → FAIL
- k=100 [zero]: CSS=1.0 CPR=0.1099 (24e) > ACDC CPR=-0.0017 (100e) → **PASS**
- k=100 [mean]: CSS=1.0 CPR=0.1760 (24e) > EP CPR=0.1722 (100e) → **PASS**

## 关键观察

1. **Arithmetic zero ablation 全面崩溃**：所有电路 CPR 均为负值，说明节点级 zero ablation 对 Greaterthan 任务过于激进。Mean ablation 下所有电路 CPR 都在 0.9+，**排名差异有意义但绝对差距小**。

2. **IOI 上 CSS=1.0 表现出色**：仅 14 edges（k=50）就达到 CPR=0.1087/0.1803，接近或超过 50 edges 的单方法电路。**边数效率极高**（每条边贡献的 CPR 远超单方法）。

3. **Arithmetic CSS=1.0 CPR 在 k=50/75/100 不变（-0.2411 / 0.9186）**：因为 CSS=1.0 覆盖的节点集在 k=50→100 增长后没变（44→54 edges 只加了连接已有节点的边）。这是**节点级 ablation 的固有局限**——无法区分边数不同但节点集相同的电路。

4. **CSS=1.0-isinf 确认退化为 ACDC**：Arithmetic 中 CSS=1.0-isinf（17e）和 ACDC-isinf（17e）CPR 完全相同，验证了 isinf 问题。Top-k binarization 成功解决了这个问题。

## IOI CPR 不一致排查

**原因：两个文件评估的是不同任务。**
- `phase_d_results.json`：IOI 任务，用 `io_ids/s_ids`（IOI logit difference）
- `mean_ablation_results.json`：**Arithmetic** 任务，用 `ans_list/wrong_list`（年份 token）
- 两个实现对各自任务都正确，数值不可比较

JSON 结果已保存：
- `/root/structfuse-context/faithfulness_arithmetic_topk.json`
- `/root/structfuse-context/faithfulness_ioi_topk.json`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_topk-css-faithfulness-final_20260513T042218"
}
```

</details>

---
