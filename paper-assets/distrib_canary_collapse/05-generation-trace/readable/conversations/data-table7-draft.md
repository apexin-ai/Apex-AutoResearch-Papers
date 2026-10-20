# data table7 draft

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 77
- **Recorded user turns:** 0
- **Tool calls:** 38
- **Original source:** `logs/chats/worker_data_table7_draft_20260519T025439.jsonl`
- **Structured JSON:** [`2929c2c318fc5880ac57.json`](../../sessions/29/2929c2c318fc5880ac57.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

77 recorded events

### Tool call

_source line 1 · 2026-05-19T03:05:25.808543+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-19T03:05:25.808828+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T03:05:25.808999+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'DONE'}",
  "fields": "['*']",
  "limit": "0",
  "project": "distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'DONE'}",
    "fields": "['*']",
    "limit": "0",
    "project": "distrib_canary_collapse"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-19T03:05:25.809621+00:00_

Error: result (131,152 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/e2477f49-dc9e-4a39-9dea-aa9e7b9521bb/tool-results/mcp-agent-ml-research-read_registry-1779159298008.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/e2477f49-dc9e-4a39-9dea-aa9e7b9521bb/tool-results/mcp-agent-ml-research-read_registry-1779159298008.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T03:05:25.809827+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/e2477f49-dc9e-4a39-9dea-aa9e7b9521bb/tool-results/mcp-agent-ml-research-read_registry-1779159298008.txt | python3 -c \"\nimport json, sys\n\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\n\n# Count total and success\ntotal = len(result)\nsuccess = [e for e in result if e.get('conclusion') == 'success']\nprint(f'Total DONE: {total}, conclusion=success: {len(success)}')\nprint()\n\n# For each success experiment, extract key info\nfor e in success:\n    exp_id = e.get('exp_id', '?')\n    hypothesis = e.get('hypothesis', '')[:80]\n    metrics = e.get('metrics', {})\n    spec = e.get('spec', {})\n    notes = e.get('notes', '')[:100] if e.get('notes') else ''\n    tags = e.get('tags', [])\n    print(f'--- {exp_id} ---')\n    print(f'  hypothesis: {hypothesis}')\n    print(f'  tags: {tags}')\n    print(f'  notes: {notes}')\n    print(f'  spec keys: {list(spec.keys()) if spec else \\\"none\\\"}')\n    print(f'  metrics keys: {list(metrics.keys()) if metrics else \\\"none\\\"}')\n    print()\n\" 2>&1 | head -500\n",
  "description": "Extract key fields from registry experiments",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/e2477f49-dc9e-4a39-9dea-aa9e7b9521bb/tool-results/mcp-agent-ml-research-read_registry-1779159298008.txt | python3 -c \"\nimport json, sys\n\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\n\n# Count total and success\ntotal = len(result)\nsuccess = [e for e in result if e.get('conclusion') == 'success']\nprint(f'Total DONE: {total}, conclusion=success: {len(success)}')\nprint()\n\n# For each success experiment, extract key info\nfor e in success:\n    exp_id = e.get('exp_id', '?')\n    hypothesis = e.get('hypothesis', '')[:80]\n    metrics = e.get('metrics', {})\n    spec = e.get('spec', {})\n    notes = e.get('notes', '')[:100] if e.get('notes') else ''\n    tags = e.get('tags', [])\n    print(f'--- {exp_id} ---')\n    print(f'  hypothesis: {hypothesis}')\n    print(f'  tags: {tags}')\n    print(f'  notes: {notes}')\n    print(f'  spec keys: {list(spec.keys()) if spec else \\\"none\\\"}')\n    print(f'  metrics keys: {list(metrics.keys()) if metrics else \\\"none\\\"}')\n    print()\n\" 2>&1 | head -500\n",
    "description": "Extract key fields from registry experiments",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T03:05:25.809968+00:00_

Traceback (most recent call last):
  File "&lt;string>", line 9, in &lt;module>
    success = [e for e in result if e.get('conclusion') == 'success']
                                    ^^^^^
AttributeError: 'str' object has no attribute 'get'

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T03:05:25.810088+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/e2477f49-dc9e-4a39-9dea-aa9e7b9521bb/tool-results/mcp-agent-ml-research-read_registry-1779159298008.txt",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/e2477f49-dc9e-4a39-9dea-aa9e7b9521bb/tool-results/mcp-agent-ml-research-read_registry-1779159298008.txt",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T03:05:25.810309+00:00_

File content (56992 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T03:05:25.810451+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "head -c 2000 /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/e2477f49-dc9e-4a39-9dea-aa9e7b9521bb/tool-results/mcp-agent-ml-research-read_registry-1779159298008.txt",
  "description": "Check file structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "tool_args": {
    "command": "head -c 2000 /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/e2477f49-dc9e-4a39-9dea-aa9e7b9521bb/tool-results/mcp-agent-ml-research-read_registry-1779159298008.txt",
    "description": "Check file structure"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T03:05:25.810595+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"alpha_sweep_a005_s42\": {\"status\": \"DONE\", \"retry_count\": 2, \"created_at\": \"2026-05-18T20:52:49.138Z\", \"updated_at\": \"2026-05-19T01:34:43.774Z\", \"hypothesis\": \"α=0.05 定位 diversity 悬崖精确位置: α=0.00 d1=-14% 到 α=0.10 d1=-40% 之间存在非线性断崖，α=0.05 确定断崖在 0-5% 还是 5-10% 区间。\", \"parent\": \"alpha_sweep_a010_s42_v2\", \"server\": \"westd-17855\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-17855\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-18T20:56:02.420Z\", \"finished_at\": \"2026-05-18T23:56:36.428Z\", \"training_hours\": 3.01}, \"failure_reason\": \"EXIT_CODE=127 (command not found — check bash -c wrapping / env activate)\", \"completed_at\": \"2026-05-18T22:07:45.970Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T22:07:49.417515+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T23:56:42.687842+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"FAILED EXIT_CODE=127 (第2次): 提交命令缺少 conda 激活（裸 `python` 在非交互 shell 找不到）。已知模式，见 memory.md \\\"westd-17855 环境提交规范\\\"。正确模板需 `bash -c '... source conda.sh && conda activate base && ...'`。将用正确模板重新提交。\"}}, \"notes\": \"D080: torch_dtype=None bug → fp16 without GradScaler → NaN. Killed and resubmitting as v3\", \"spec\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/distrib_canary_collapse && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && CUDA_VISIBLE_DEVICES=3 python -u iterative_train.py --model_name EleutherAI/pythia-410m --seed 42 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T03:05:25.810738+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/e2477f49-dc9e-4a39-9dea-aa9e7b9521bb/tool-results/mcp-agent-ml-research-read_registry-1779159298008.txt') as f:\n    raw = json.load(f)\n\nresult = json.loads(raw['result'])\nexps = result['data']['experiments']\n\ntotal = len(exps)\nsuccess = {k: v for k, v in exps.items() if v.get('conclusion') == 'success'}\nprint(f'Total DONE: {total}, conclusion=success: {len(success)}')\nprint(f'Other conclusions: {set(v.get(\\\"conclusion\\\",\\\"none\\\") for k,v in exps.items() if v.get(\\\"conclusion\\\") != \\\"success\\\")}')\nprint()\n\nfor eid, e in sorted(success.items()):\n    print(f'=== {eid} ===')\n\" 2>&1\n",
  "description": "Parse registry structure and list success experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/e2477f49-dc9e-4a39-9dea-aa9e7b9521bb/tool-results/mcp-agent-ml-research-read_registry-1779159298008.txt') as f:\n    raw = json.load(f)\n\nresult = json.loads(raw['result'])\nexps = result['data']['experiments']\n\ntotal = len(exps)\nsuccess = {k: v for k, v in exps.items() if v.get('conclusion') == 'success'}\nprint(f'Total DONE: {total}, conclusion=success: {len(success)}')\nprint(f'Other conclusions: {set(v.get(\\\"conclusion\\\",\\\"none\\\") for k,v in exps.items() if v.get(\\\"conclusion\\\") != \\\"success\\\")}')\nprint()\n\nfor eid, e in sorted(success.items()):\n    print(f'=== {eid} ===')\n\" 2>&1\n",
    "description": "Parse registry structure and list success experiments"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T03:05:25.810874+00:00_

Total DONE: 70, conclusion=success: 39
Other conclusions: {'negative', 'failed', 'killed'}

=== alpha_sweep_a000_s42 ===
=== alpha_sweep_a000_s43 ===
=== alpha_sweep_a000_s44 ===
=== alpha_sweep_a010_s43 ===
=== alpha_sweep_a025_s42_v3 ===
=== alpha_sweep_a025_s43 ===
=== alpha_sweep_a025_s44 ===
=== alpha_sweep_a050_s42 ===
=== alpha_sweep_a050_s43 ===
=== alpha_sweep_a050_s44 ===
=== alpha_sweep_a060_s42_bf16 ===
=== alpha_sweep_a075_s42 ===
=== alpha_sweep_a075_s43 ===
=== alpha_sweep_a075_s44 ===
=== alpha_sweep_c4_a050_s42_bf16 ===
=== conditional_granger_d061 ===
=== gen_gpt2m_a100_s43_bf16 ===
=== gen_wiki_gpt2m_a025_s42 ===
=== gen_wiki_gpt2m_a100_s42_v3 ===
=== gen_wiki_gpt2m_a100_s42_v4 ===
=== generalize_opt1b_wiki_a100_s42 ===
=== generalize_pythia14b_wiki_a100_s42 ===
=== generalize_pythia14b_wiki_a100_s43 ===
=== generalize_pythia1b_c4_a100_s42_v2 ===
=== generalize_pythia1b_c4_a100_s43 ===
=== generalize_pythia410m_wiki_a100_s42 ===
=== interv_pred_s43_bf16 ===
=== interv_react_s43_bf16 ===
=== intervention_predictive_s42 ===
=== intervention_reactive_s42 ===
=== method_ablation_phase1 ===
=== method_ablation_phase2 ===
=== method_ablation_phase3 ===
=== mvp_v4_rep42 ===
=== mvp_v4_rep43 ===
=== mvp_v4_rep44 ===
=== mvp_v4_rep45 ===
=== plan_009_bootstrap_ty ===
=== scale_14b_a050_s42 ===

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T03:05:25.811003+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/e2477f49-dc9e-4a39-9dea-aa9e7b9521bb/tool-results/mcp-agent-ml-research-read_registry-1779159298008.txt') as f:\n    raw = json.load(f)\n\nresult = json.loads(raw['result'])\nexps = result['data']['experiments']\nsuccess = {k: v for k, v in exps.items() if v.get('conclusion') == 'success'}\n\nfor eid, e in sorted(success.items()):\n    metrics = e.get('metrics', {})\n    spec = e.get('spec', {})\n    notes = (e.get('notes') or '')[:200]\n    hyp = (e.get('hypothesis') or '')[:150]\n    tags = e.get('tags', [])\n    \n    # Extract spec command to check for bf16 / model / alpha / seed / dataset\n    cmd = ''\n    if isinstance(spec, dict):\n        cmd = spec.get('command', '')[:300]\n    \n    print(f'=== {eid} ===')\n    print(f'  hyp: {hyp}')\n    print(f'  tags: {tags}')\n    print(f'  notes: {notes}')\n    print(f'  metrics_keys: {list(metrics.keys())[:20]}')\n    print(f'  cmd_excerpt: {cmd[:200]}')\n    print()\n\" 2>&1\n",
  "description": "Extract detailed fields for all success experiments",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/e2477f49-dc9e-4a39-9dea-aa9e7b9521bb/tool-results/mcp-agent-ml-research-read_registry-1779159298008.txt') as f:\n    raw = json.load(f)\n\nresult = json.loads(raw['result'])\nexps = result['data']['experiments']\nsuccess = {k: v for k, v in exps.items() if v.get('conclusion') == 'success'}\n\nfor eid, e in sorted(success.items()):\n    metrics = e.get('metrics', {})\n    spec = e.get('spec', {})\n    notes = (e.get('notes') or '')[:200]\n    hyp = (e.get('hypothesis') or '')[:150]\n    tags = e.get('tags', [])\n    \n    # Extract spec command to check for bf16 / model / alpha / seed / dataset\n    cmd = ''\n    if isinstance(spec, dict):\n        cmd = spec.get('command', '')[:300]\n    \n    print(f'=== {eid} ===')\n    print(f'  hyp: {hyp}')\n    print(f'  tags: {tags}')\n    print(f'  notes: {notes}')\n    print(f'  metrics_keys: {list(metrics.keys())[:20]}')\n    print(f'  cmd_excerpt: {cmd[:200]}')\n    print()\n\" 2>&1\n",
    "description": "Extract detailed fields for all success experiments",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T03:05:25.811151+00:00_

Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 27, in &lt;module>
    print(f'  metrics_keys: {list(metrics.keys())[:20]}')
                                  ^^^^^^^^^^^^
AttributeError: 'str' object has no attribute 'keys'
=== alpha_sweep_a000_s42 ===
  hyp: 
  tags: []
  notes: 
  metrics_keys: ['gen0_token_entropy', 'gen10_token_entropy', 'gen0_ece', 'gen10_ece', 'gen0_perplexity', 'gen10_perplexity', 'gen0_distinct_1', 'gen10_distinct_1', 'token_entropy_drift_pct', 'ece_drift_pct', 'perplexity_drift_pct', 'distinct_1_drift_pct', 'distinct_2_drift_pct', 'distinct_3_drift_pct', 'gen1_10_perplexity_drift_pct', 'gen1_10_distinct_1_drift_pct', 'gen1_10_entropy_drift_pct']
  cmd_excerpt: bash -c "cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && source /root/miniconda3/

=== alpha_sweep_a000_s43 ===
  hyp: α=0.0 null control multi-seed: 无合成数据再训练在跨 seed 复现下仍不产生 spurious causal signal（PermG FDR 0/8），证实 signal 源于合成污染而非训练随机性
  tags: []
  notes: 
  metrics_keys: ['gen0', 'gen10', 'drift_pct', 'five_method']
  cmd_excerpt: bash -c "cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && export REQUESTS_CA_BUNDL

=== alpha_sweep_a000_s44 ===
  hyp: α=0.0 null control multi-seed: 无合成数据再训练在跨 seed 复现下仍不产生 spurious causal signal（PermG FDR 0/8），证实 signal 源于合成污染而非训练随机性
  tags: []
  notes: 
  metrics_keys: ['gen0', 'gen10', 'drift_pct', 'five_method']
  cmd_excerpt: bash -c "cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && export REQUESTS_CA_BUNDL

=== alpha_sweep_a010_s43 ===
  hyp: α=0.10 multi-seed s43: Validates D075 canary blind zone finding (α=0.10 diversity collapse saturated at -39.7% but entropy canary shows no s
…[truncated 1720 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T03:05:25.811344+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/e2477f49-dc9e-4a39-9dea-aa9e7b9521bb/tool-results/mcp-agent-ml-research-read_registry-1779159298008.txt') as f:\n    raw = json.load(f)\n\nresult = json.loads(raw['result'])\nexps = result['data']['experiments']\nsuccess = {k: v for k, v in exps.items() if v.get('conclusion') == 'success'}\n\n# Save just the success experiments for easier processing\nwith open('/tmp/success_exps.json', 'w') as f:\n    json.dump(success, f, indent=2, ensure_ascii=False)\n\nprint(f\"Saved {len(success)} success experiments to /tmp/success_exps.json\")\n\n# Also get RUNNING experiments\nrunning = {k: v for k, v in exps.items() if v.get('status') == 'RUNNING' or v.get('conclusion') not in ('success','failed','negative','killed')}\nprint(f\"\\nNon-terminal experiments:\")\nfor eid, e in sorted(exps.items()):\n    if e.get('conclusion') not in ('success','failed','negative','killed'):\n        print(f\"  {eid}: status={e.get('status')}, conclusion={e.get('conclusion')}\")\nPYEOF\n",
  "description": "Save success experiments and check running ones",
  "timeout": "15000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/e2477f49-dc9e-4a39-9dea-aa9e7b9521bb/tool-results/mcp-agent-ml-research-read_registry-1779159298008.txt') as f:\n    raw = json.load(f)\n\nresult = json.loads(raw['result'])\nexps = result['data']['experiments']\nsuccess = {k: v for k, v in exps.items() if v.get('conclusion') == 'success'}\n\n# Save just the success experiments for easier processing\nwith open('/tmp/success_exps.json', 'w') as f:\n    json.dump(success, f, indent=2, ensure_ascii=False)\n\nprint(f\"Saved {len(success)} success experiments to /tmp/success_exps.json\")\n\n# Also get RUNNING experiments\nrunning = {k: v for k, v in exps.items() if v.get('status') == 'RUNNING' or v.get('conclusion') not in ('success','failed','negative','killed')}\nprint(f\"\\nNon-terminal experiments:\")\nfor eid, e in sorted(exps.items()):\n    if e.get('conclusion') not in ('success','failed','negative','killed'):\n        print(f\"  {eid}: status={e.get('status')}, conclusion={e.get('conclusion')}\")\nPYEOF\n",
    "description": "Save success experiments and check running ones",
    "timeout": "15000"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T03:05:25.811480+00:00_

Saved 39 success experiments to /tmp/success_exps.json

Non-terminal experiments:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T03:05:25.811605+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\n# Also check for RUNNING in the full registry (not just DONE filter)\n# We already filtered status=DONE, so no running exps in this set\n# Let me check the notes\nwith open('/tmp/success_exps.json') as f:\n    success = json.load(f)\n\nfor eid, e in sorted(success.items()):\n    metrics = e.get('metrics', {})\n    notes = (e.get('notes') or '')\n    hyp = (e.get('hypothesis') or '')\n    spec = e.get('spec', {})\n    cmd = spec.get('command', '') if isinstance(spec, dict) else ''\n    \n    # Detect model\n    model = 'Pythia-410M'  # default\n    if 'gpt2m' in eid or 'gpt2-medium' in cmd.lower() or 'gpt-2-medium' in hyp.lower() or 'gpt2m' in hyp.lower():\n        model = 'GPT-2-Medium'\n    elif 'opt1b' in eid or 'opt-1.3b' in cmd.lower():\n        model = 'OPT-1.3B'\n    elif 'pythia14b' in eid or 'pythia-1.4b' in cmd.lower():\n        model = 'Pythia-1.4B'\n    elif 'pythia1b_c4' in eid or 'pythia-1b' in cmd.lower():\n        model = 'Pythia-1B'\n    elif 'scale_14b' in eid:\n        model = 'Pythia-1.4B'\n    elif 'scale_69b' in eid:\n        model = 'Pythia-6.9B'\n    \n    # Detect alpha\n    alpha = '?'\n    if '_a000_' in eid: alpha = '0.00'\n    elif '_a005_' in eid: alpha = '0.05'\n    elif '_a010_' in eid: alpha = '0.10'\n    elif '_a025_' in eid: alpha = '0.25'\n    elif '_a050_' in eid: alpha = '0.50'\n    elif '_a060_' in eid: alpha = '0.60'\n    elif '_a075_' in eid: alpha = '0.75'\n    elif '_a100_' in eid: alpha = '1.00'\n    elif 'mvp_v4' in eid: alpha = '1.00'\n    \n    # Detect seed\n    seed = '?'\n    if '_s42' in eid or 'rep42' in eid: seed = '42'\n    elif '_s43' in eid or 'rep43' in eid: seed = '43'\n    elif '_s44' in eid or 'rep44' in eid: seed = '44'\n    elif '_s45' in eid or 'rep45' in eid: seed = '45'\n    \n    # Detect dataset\n    dataset = 'WikiText-103'\n    if '_c4_' in eid or 'c4' in eid.lower():\n        dataset = 'C4'\n    \n    # Detect precision\n    precision = 'fp32'\n    if '_bf16' in eid or 'bf16' in notes.lower():\n        precision = 'bf16'\n    elif 'fp16' in notes.lower():\n        precision = 'fp16*'\n    \n    # Detect category\n    category = 'main'\n    if 'interv' in eid or 'intervention' in eid:\n        category = 'intervention'\n    elif 'generalize' in eid or 'gen_wiki' in eid or 'gen_gpt2m' in eid:\n        category = 'cross-arch'\n    elif '_c4_' in eid:\n        category = 'cross-dataset'\n    elif 'scale_' in eid:\n        category = 'scale'\n    elif 'mvp_' in eid:\n        category = 'mvp'\n    elif 'method_ablation' in eid:\n        category = 'ablation'\n    elif 'plan_009' in eid or 'conditional_granger' in eid:\n        category = 'analysis'\n    \n    # Extract lead-lag metrics\n    ll = {}\n    if isinstance(metrics, dict):\n        # Check for five_method nested structure\n        fm = metrics.get('five_method', {})\n        if isinstance(fm, dict):\n            ll['naive'] = fm.get('naive_xcorr_fwd', fm.get('naive', ''))\n            ll['diff'] = fm.get('diff_xcorr_fwd', fm.get('diff', ''))\n            ll['thresh'] = fm.get('threshold_onset_fwd', fm.get('thresh', ''))\n            ll['pg_fwd'] = fm.get('perm_granger_fwd', fm.get('pg_fwd', ''))\n            ll['pg_rev'] = fm.get('perm_granger_rev', fm.get('pg_rev', ''))\n            ll['ty'] = fm.get('ty_granger_fwd', fm.get('ty', ''))\n            ll['k_gte4'] = fm.get('k_gte4', '')\n            ll['mmct_wt'] = fm.get('mmct_weighted_fwd', fm.get('mmct_wt', ''))\n        else:\n            # flat metrics\n            ll['naive'] = metrics.get('naive_xcorr_fwd', '')\n            ll['diff'] = metrics.get('diff_xcorr_fwd', '')\n            ll['thresh'] = metrics.get('threshold_onset_fwd', '')\n            ll['pg_fwd'] = metrics.get('perm_granger_fwd', '')\n            ll['pg_rev'] = metrics.get('perm_granger_rev', '')\n            ll['ty'] = metrics.get('ty_granger_fwd', '')\n            ll['k_gte4'] = metrics.get('k_gte4', '')\n            ll['mmct_wt'] = metrics.get('mmct_weighted_fwd', metrics.get('mmct_wt', ''))\n    elif isinstance(metrics, str):\n        ll['raw'] = metrics[:200]\n    \n    print(f'=== {eid} ===')\n    print(f'  model={model}, alpha={alpha}, seed={seed}, dataset={dataset}, prec={precision}, cat={category}')\n    print(f'  lead-lag: {ll}')\n    print(f'  notes: {notes[:150]}')\n    print()\nPYEOF\n",
  "description": "Parse all success experiments into structured data",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport json\n\n# Also check for RUNNING in the full registry (not just DONE filter)\n# We already filtered status=DONE, so no running exps in this set\n# Let me check the notes\nwith open('/tmp/success_exps.json') as f:\n    success = json.load(f)\n\nfor eid, e in sorted(success.items()):\n    metrics = e.get('metrics', {})\n    notes = (e.get('notes') or '')\n    hyp = (e.get('hypothesis') or '')\n    spec = e.get('spec', {})\n    cmd = spec.get('command', '') if isinstance(spec, dict) else ''\n    \n    # Detect model\n    model = 'Pythia-410M'  # default\n    if 'gpt2m' in eid or 'gpt2-medium' in cmd.lower() or 'gpt-2-medium' in hyp.lower() or 'gpt2m' in hyp.lower():\n        model = 'GPT-2-Medium'\n    elif 'opt1b' in eid or 'opt-1.3b' in cmd.lower():\n        model = 'OPT-1.3B'\n    elif 'pythia14b' in eid or 'pythia-1.4b' in cmd.lower():\n        model = 'Pythia-1.4B'\n    elif 'pythia1b_c4' in eid or 'pythia-1b' in cmd.lower():\n        model = 'Pythia-1B'\n    elif 'scale_14b' in eid:\n        model = 'Pythia-1.4B'\n    elif 'scale_69b' in eid:\n        model = 'Pythia-6.9B'\n    \n    # Detect alpha\n    alpha = '?'\n    if '_a000_' in eid: alpha = '0.00'\n    elif '_a005_' in eid: alpha = '0.05'\n    elif '_a010_' in eid: alpha = '0.10'\n    elif '_a025_' in eid: alpha = '0.25'\n    elif '_a050_' in eid: alpha = '0.50'\n    elif '_a060_' in eid: alpha = '0.60'\n    elif '_a075_' in eid: alpha = '0.75'\n    elif '_a100_' in eid: alpha = '1.00'\n    elif 'mvp_v4' in eid: alpha = '1.00'\n    \n    # Detect seed\n    seed = '?'\n    if '_s42' in eid or 'rep42' in eid: seed = '42'\n    elif '_s43' in eid or 'rep43' in eid: seed = '43'\n    elif '_s44' in eid or 'rep44' in eid: seed = '44'\n    elif '_s45' in eid or 'rep45' in eid: seed = '45'\n    \n    # Detect dataset\n    dataset = 'WikiText-103'\n    if '_c4_' in eid or 'c4' in eid.lower():\n        dataset = 'C4'\n    \n    # Detect precision\n    precision = 'fp32'\n    if '_bf16' in eid or 'bf16' in notes.lower():\n        precision = 'bf16'\n    elif 'fp16' in notes.lower():\n        precision = 'fp16*'\n    \n    # Detect category\n    category = 'main'\n    if 'interv' in eid or 'intervention' in eid:\n        category = 'intervention'\n    elif 'generalize' in eid or 'gen_wiki' in eid or 'gen_gpt2m' in eid:\n        category = 'cross-arch'\n    elif '_c4_' in eid:\n        category = 'cross-dataset'\n    elif 'scale_' in eid:\n        category = 'scale'\n    elif 'mvp_' in eid:\n        category = 'mvp'\n    elif 'method_ablation' in eid:\n        category = 'ablation'\n    elif 'plan_009' in eid or 'conditional_granger' in eid:\n        category = 'analysis'\n    \n    # Extract lead-lag metrics\n    ll = {}\n    if isinstance(metrics, dict):\n        # Check for five_method nested structure\n        fm = metrics.get('five_method', {})\n        if isinstance(fm, dict):\n            ll['naive'] = fm.get('naive_xcorr_fwd', fm.get('naive', ''))\n            ll['diff'] = fm.get('diff_xcorr_fwd', fm.get('diff', ''))\n            ll['thresh'] = fm.get('threshold_onset_fwd', fm.get('thresh', ''))\n            ll['pg_fwd'] = fm.get('perm_granger_fwd', fm.get('pg_fwd', ''))\n            ll['pg_rev'] = fm.get('perm_granger_rev', fm.get('pg_rev', ''))\n            ll['ty'] = fm.get('ty_granger_fwd', fm.get('ty', ''))\n            ll['k_gte4'] = fm.get('k_gte4', '')\n            ll['mmct_wt'] = fm.get('mmct_weighted_fwd', fm.get('mmct_wt', ''))\n        else:\n            # flat metrics\n            ll['naive'] = metrics.get('naive_xcorr_fwd', '')\n            ll['diff'] = metrics.get('diff_xcorr_fwd', '')\n            ll['thresh'] = metrics.get('threshold_onset_fwd', '')\n            ll['pg_fwd'] = metrics.get('perm_granger_fwd', '')\n            ll['pg_rev'] = metrics.get('perm_granger_rev', '')\n            ll['ty'] = metrics.get('ty_granger_fwd', '')\n            ll['k_gte4'] = metrics.get('k_gte4', '')\n            ll['mmct_wt'] = metrics.get('mmct_weighted_fwd', metrics.get('mmct_wt', ''))\n    elif isinstance(metrics, str):\n        ll['raw'] = metrics[:200]\n    \n    print(f'=== {eid} ===')\n    print(f'  model={model}, alpha={alpha}, seed={seed}, dataset={dataset}, prec={precision}, cat={category}')\n    print(f'  lead-lag: {ll}')\n    print(f'  notes: {notes[:150]}')\n    print()\nPYEOF\n",
    "description": "Parse all success experiments into structured data",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T03:05:25.811808+00:00_

=== alpha_sweep_a000_s42 ===
  model=Pythia-410M, alpha=0.00, seed=42, dataset=WikiText-103, prec=fp32, cat=main
  lead-lag: {'naive': '', 'diff': '', 'thresh': '', 'pg_fwd': '', 'pg_rev': '', 'ty': '', 'k_gte4': '', 'mmct_wt': ''}
  notes: 

=== alpha_sweep_a000_s43 ===
  model=Pythia-410M, alpha=0.00, seed=43, dataset=WikiText-103, prec=fp32, cat=main
  lead-lag: {'naive': '', 'diff': '', 'thresh': '', 'pg_fwd': '', 'pg_rev': '', 'ty': '', 'k_gte4': '', 'mmct_wt': ''}
  notes: 

=== alpha_sweep_a000_s44 ===
  model=Pythia-410M, alpha=0.00, seed=44, dataset=WikiText-103, prec=fp32, cat=main
  lead-lag: {'naive': '', 'diff': '', 'thresh': '', 'pg_fwd': '', 'pg_rev': '', 'ty': '', 'k_gte4': '', 'mmct_wt': ''}
  notes: 

=== alpha_sweep_a010_s43 ===
  model=Pythia-410M, alpha=0.10, seed=43, dataset=WikiText-103, prec=fp32, cat=main
  lead-lag: {'naive': '', 'diff': '', 'thresh': '', 'pg_fwd': '', 'pg_rev': '', 'ty': '', 'k_gte4': '', 'mmct_wt': ''}
  notes: 

=== alpha_sweep_a025_s42_v3 ===
  model=Pythia-410M, alpha=0.25, seed=42, dataset=WikiText-103, prec=fp32, cat=main
  lead-lag: {'naive': '', 'diff': '', 'thresh': '', 'pg_fwd': '', 'pg_rev': '', 'ty': '', 'k_gte4': '', 'mmct_wt': ''}
  notes: 实际磁盘路径为 results/alpha_sweep/a025_s42/（无 v3 后缀）。Registry ID 带 v3 是历史原因，数据已核实无误。

=== alpha_sweep_a025_s43 ===
  model=Pythia-410M, alpha=0.25, seed=43, dataset=WikiText-103, prec=fp32, cat=main
  lead-lag: {'naive': '', 'diff': '', 'thresh': '', 'pg_fwd': '', 'pg_rev': '', 'ty': '', 'k_gte4': '', 'mmct_wt': ''}
  notes: 

=== alpha_sweep_a025_s44 ===
  model=Pythia-410M, alpha=0.25, seed=44, dataset=WikiText-103, prec=fp32, cat=main
  lead-lag: {'raw': '{\n  "gen0": {\n    "token_entropy": 3.2342, "ece": 0.01080, "perplexity": 26.949,\n    "distinct_1": 0.09809, "distinct_2": 0.51324, "distinct_3": 0.80577,\n    "effective_rank": 46.613, "mauve": 0.02954'}
  notes: 

=== alpha_sweep_a050_s42 ===
  model=Pythia-410M, alpha=0.50, seed=42, dataset=WikiText-103, prec=fp32, cat=m
…[truncated 8246 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-19T03:05:25.812009+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/tmp/success_exps.json') as f:\n    success = json.load(f)\n\n# Print full metrics for experiments that have them\nfor eid in sorted(success.keys()):\n    e = success[eid]\n    metrics = e.get('metrics', {})\n    if not metrics:\n        continue\n    \n    if isinstance(metrics, str):\n        # Parse string metrics\n        try:\n            m = json.loads(metrics)\n        except:\n            m = metrics\n    else:\n        m = metrics\n    \n    # Check if it has five_method or lead-lag keys\n    has_leadlag = False\n    if isinstance(m, dict):\n        for k in m:\n            if any(x in str(k).lower() for x in ['naive', 'granger', 'perm', 'xcorr', 'thresh', 'k_gte', 'five_method', 'mmct']):\n                has_leadlag = True\n                break\n    \n    if has_leadlag:\n        print(f'=== {eid} ===')\n        # Print only lead-lag relevant keys\n        if isinstance(m, dict):\n            for k, v in m.items():\n                if any(x in str(k).lower() for x in ['naive', 'granger', 'perm', 'xcorr', 'thresh', 'k_gte', 'five_method', 'mmct', 'lead_lag']):\n                    print(f'  {k}: {json.dumps(v, ensure_ascii=False)[:300]}')\n        print()\n\nprint(\"---\\nExperiments WITHOUT lead-lag in registry metrics:\")\nfor eid in sorted(success.keys()):\n    e = success[eid]\n    metrics = e.get('metrics', {})\n    if isinstance(metrics, str):\n        try:\n            m = json.loads(metrics)\n        except:\n            m = {}\n    else:\n        m = metrics if isinstance(metrics, dict) else {}\n    \n    has_ll = False\n    if isinstance(m, dict):\n        for k in m:\n            if any(x in str(k).lower() for x in ['naive', 'granger', 'perm', 'xcorr', 'thresh', 'k_gte', 'five_method', 'mmct']):\n                has_ll = True\n                break\n    if not has_ll:\n        print(f'  {eid}')\nPYEOF\n",
  "description": "Find experiments with lead-lag metrics in registry",
  "timeout": "15000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/tmp/success_exps.json') as f:\n    success = json.load(f)\n\n# Print full metrics for experiments that have them\nfor eid in sorted(success.keys()):\n    e = success[eid]\n    metrics = e.get('metrics', {})\n    if not metrics:\n        continue\n    \n    if isinstance(metrics, str):\n        # Parse string metrics\n        try:\n            m = json.loads(metrics)\n        except:\n            m = metrics\n    else:\n        m = metrics\n    \n    # Check if it has five_method or lead-lag keys\n    has_leadlag = False\n    if isinstance(m, dict):\n        for k in m:\n            if any(x in str(k).lower() for x in ['naive', 'granger', 'perm', 'xcorr', 'thresh', 'k_gte', 'five_method', 'mmct']):\n                has_leadlag = True\n                break\n    \n    if has_leadlag:\n        print(f'=== {eid} ===')\n        # Print only lead-lag relevant keys\n        if isinstance(m, dict):\n            for k, v in m.items():\n                if any(x in str(k).lower() for x in ['naive', 'granger', 'perm', 'xcorr', 'thresh', 'k_gte', 'five_method', 'mmct', 'lead_lag']):\n                    print(f'  {k}: {json.dumps(v, ensure_ascii=False)[:300]}')\n        print()\n\nprint(\"---\\nExperiments WITHOUT lead-lag in registry metrics:\")\nfor eid in sorted(success.keys()):\n    e = success[eid]\n    metrics = e.get('metrics', {})\n    if isinstance(metrics, str):\n        try:\n            m = json.loads(metrics)\n        except:\n            m = {}\n    else:\n        m = metrics if isinstance(metrics, dict) else {}\n    \n    has_ll = False\n    if isinstance(m, dict):\n        for k in m:\n            if any(x in str(k).lower() for x in ['naive', 'granger', 'perm', 'xcorr', 'thresh', 'k_gte', 'five_method', 'mmct']):\n                has_ll = True\n                break\n    if not has_ll:\n        print(f'  {eid}')\nPYEOF\n",
    "description": "Find experiments with lead-lag metrics in registry",
    "timeout": "15000"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T03:05:25.812203+00:00_

=== alpha_sweep_a000_s43 ===
  five_method: {"perm_granger_fdr_sig": "0/8", "ty_sig": "1/8 (df_resid=1 unreliable)", "robust_pairs_ge3": "0/8", "fpr_controlled": true}

=== alpha_sweep_a000_s44 ===
  five_method: {"perm_granger_fdr_sig": "0/8", "ty_sig": "0/8", "robust_pairs_ge3": "0/8", "fpr_controlled": true}

=== alpha_sweep_a010_s43 ===
  naive_xcorr_fwd: "7/8"
  diff_xcorr_fwd: "8/8"
  threshold_onset_fwd: "3/8"
  perm_granger_fwd: "0/8"
  perm_granger_rev: "0/8"
  ty_granger_fwd: "0/8"
  k_gte4: "0/8"

=== alpha_sweep_a050_s42 ===
  granger_entropy_to_d1_p_raw: 0.095
  granger_entropy_to_d2_p_raw: 0.097
  granger_ece_to_d1_p_raw: 0.019
  granger_ece_to_d2_p_raw: 0.039
  granger_fdr_note: "4 tests within alpha=0.50; BH FDR threshold rank1=0.0125, rank2=0.025 → 0/4 FDR-sig at q=0.05. Raw p pattern (ECE < entropy) is qualitative signal only."

=== alpha_sweep_a050_s44 ===
  perm_granger_fdr_fwd: "3/8"
  perm_granger_fdr_rev: "0/8"
  naive_xcorr_fwd: "4/8"
  diff_xcorr_fdr_fwd: "6/8"
  threshold_onset_fwd: "0/8"
  ty_granger_fwd: "0/8"

=== alpha_sweep_a060_s42_bf16 ===
  lead_lag_unified_2sigma: {"naive_xcorr_fwd": "8/8", "diff_xcorr_fwd": "8/8", "threshold_onset_fwd": "6/8", "perm_granger_fwd": "8/8", "perm_granger_rev": "0/8", "ty_granger_fwd": "0/8", "consensus_K4": "6/8"}
  mmct: {"uniform_forward": "0/8", "uniform_bidirectional": "0/8", "weighted_pair_forward": "6/8", "weighted_pair_bidirectional": "6/8", "weighted_global_forward": "0/8", "weighted_global_bidirectional": "0/8"}

=== alpha_sweep_a075_s42 ===
  granger_ece_to_d1_p_fdr: 0.046
  granger_ece_to_d2_p_fdr: 0.046
  granger_entropy_to_d2_p_fdr: 0.048
  granger_entropy_to_d1_p_fdr: 0.054
  granger_fdr_sig_count: "3/8"
  xcorr_entropy_d1_lag: 2
  xcorr_entropy_d1_r: 0.973

=== alpha_sweep_c4_a050_s42_bf16 ===
  diff_xcorr_te_d1_lag: 1
  diff_xcorr_te_d1_r: 0.914
  permg_fwd_fdr_sig: "0/8"
  permg_rev_fdr_sig: "0/8"

=== gen_gpt2m_a100_s43_bf16 ===
  naive: "8/8"
  thresh: "8/8"
  k_gte4: "1/8"
  mmct_w
…[truncated 2841 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-19T03:05:25.812420+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/tmp/success_exps.json') as f:\n    success = json.load(f)\n\n# Build comprehensive extraction\nresults = {}\nfor eid in sorted(success.keys()):\n    e = success[eid]\n    metrics = e.get('metrics', {})\n    notes = e.get('notes') or ''\n    hyp = e.get('hypothesis') or ''\n    spec = e.get('spec', {})\n    cmd = spec.get('command', '') if isinstance(spec, dict) else ''\n    \n    if isinstance(metrics, str):\n        try:\n            metrics = json.loads(metrics)\n        except:\n            metrics = {}\n    if not isinstance(metrics, dict):\n        metrics = {}\n    \n    # Model detection\n    model = 'Pythia-410M'\n    if 'gpt2m' in eid or 'gpt2-medium' in cmd.lower() or 'gpt-2-medium' in hyp.lower():\n        model = 'GPT-2-Medium'\n    elif 'opt1b' in eid: model = 'OPT-1.3B'\n    elif 'pythia14b' in eid or 'scale_14b' in eid: model = 'Pythia-1.4B'\n    elif 'pythia1b_c4' in eid: model = 'Pythia-1B'\n    elif 'scale_69b' in eid: model = 'Pythia-6.9B'\n    \n    # Alpha\n    alpha_map = {'_a000_':'0.00','_a005_':'0.05','_a010_':'0.10','_a025_':'0.25',\n                 '_a050_':'0.50','_a060_':'0.60','_a075_':'0.75','_a100_':'1.00'}\n    alpha = '1.00' if 'mvp_v4' in eid else '?'\n    for pat, val in alpha_map.items():\n        if pat in eid: alpha = val; break\n    \n    # Seed\n    seed = '?'\n    for s in ['42','43','44','45']:\n        if f'_s{s}' in eid or f'rep{s}' in eid: seed = s; break\n    \n    # Dataset\n    dataset = 'C4' if '_c4_' in eid or 'pythia1b_c4' in eid else 'WikiText-103'\n    \n    # Precision\n    precision = 'fp32'\n    if '_bf16' in eid: precision = 'bf16'\n    \n    # Category\n    cat = 'main'\n    if 'interv' in eid or 'intervention' in eid: cat = 'intervention'\n    elif 'generalize' in eid or 'gen_wiki' in eid or 'gen_gpt2m' in eid: cat = 'cross-arch'\n    elif '_c4_' in eid and 'generalize' not in eid: cat = 'cross-dataset'\n    elif 'scale_' in eid: cat = 'scale'\n    elif 'mvp_' in eid: cat = 'mvp'\n    elif 'method_ablation' in eid: cat = 'ablation'\n    elif 'plan_009' in eid or 'conditional_granger' in eid: cat = 'analysis'\n    \n    # Extract lead-lag from various metric formats\n    ll = {'naive':'—','diff':'—','thresh':'—','pg_fwd':'—','pg_rev':'—','ty':'—','k_gte4':'—','mmct_wt':'—'}\n    \n    # Check five_method nested\n    fm = metrics.get('five_method', {})\n    if isinstance(fm, dict) and fm:\n        ll['pg_fwd'] = fm.get('perm_granger_fdr_sig', '—')\n        ll['ty'] = fm.get('ty_sig', '—')\n        ll['k_gte4'] = fm.get('robust_pairs_ge3', '—')  # k_gte4 maps to robust_pairs?\n    \n    # Direct keys (newer format)\n    if metrics.get('naive'): ll['naive'] = metrics['naive']\n    if metrics.get('naive_xcorr_fwd'): ll['naive'] = metrics['naive_xcorr_fwd']\n    if metrics.get('diff_xcorr_fwd'): ll['diff'] = metrics['diff_xcorr_fwd']\n    if metrics.get('threshold_onset_fwd'): ll['thresh'] = metrics['threshold_onset_fwd']\n    if metrics.get('thresh'): ll['thresh'] = metrics['thresh']\n    if metrics.get('perm_granger_fwd'): ll['pg_fwd'] = metrics['perm_granger_fwd']\n    if metrics.get('perm_granger_rev'): ll['pg_rev'] = metrics['perm_granger_rev']\n    if metrics.get('ty_granger_fwd'): ll['ty'] = metrics['ty_granger_fwd']\n    if metrics.get('k_gte4'): ll['k_gte4'] = metrics['k_gte4']\n    if metrics.get('mmct_weighted_fwd'): ll['mmct_wt'] = metrics['mmct_weighted_fwd']\n    \n    # lead_lag_unified_2sigma\n    llu = metrics.get('lead_lag_unified_2sigma', {})\n    if isinstance(llu, dict) and llu:\n        if llu.get('naive_xcorr_fwd'): ll['naive'] = llu['naive_xcorr_fwd']\n        if llu.get('diff_xcorr_fwd'): ll['diff'] = llu['diff_xcorr_fwd']\n        if llu.get('threshold_onset_fwd'): ll['thresh'] = llu['threshold_onset_fwd']\n        if llu.get('perm_granger_fwd'): ll['pg_fwd'] = llu['perm_granger_fwd']\n        if llu.get('perm_granger_rev'): ll['pg_rev'] = llu['perm_granger_rev']\n        if llu.get('ty_granger_fwd'): ll['ty'] = llu['ty_granger_fwd']\n        if llu.get('consensus_K4'): ll['k_gte4'] = llu['consensus_K4']\n    \n    # mmct nested\n    mmct = metrics.get('mmct', {})\n    if isinstance(mmct, dict) and mmct:\n        if mmct.get('weighted_pair_forward'): ll['mmct_wt'] = mmct['weighted_pair_forward']\n    \n    # Older format: perm_granger_fdr_fwd, diff_xcorr_fdr_fwd\n    if metrics.get('perm_granger_fdr_fwd'): ll['pg_fwd'] = metrics['perm_granger_fdr_fwd']\n    if metrics.get('perm_granger_fdr_rev'): ll['pg_rev'] = metrics['perm_granger_fdr_rev']\n    if metrics.get('diff_xcorr_fdr_fwd'): ll['diff'] = metrics['diff_xcorr_fdr_fwd']\n    if metrics.get('naive_xcorr_fwd'): ll['naive'] = metrics['naive_xcorr_fwd']\n    \n    # granger_fdr_sig_count (old a075_s42 format)\n    if metrics.get('granger_fdr_sig_count'): ll['pg_fwd'] = metrics['granger_fdr_sig_count']\n    \n    # permg_fwd_fdr_sig (c4 format)\n    if metrics.get('permg_fwd_fdr_sig'): ll['pg_fwd'] = metrics['permg_fwd_fdr_sig']\n    if metrics.get('permg_rev_fdr_sig'): ll['pg_rev'] = metrics['permg_rev_fdr_sig']\n    \n    results[eid] = {\n        'model': model, 'alpha': alpha, 'seed': seed, 'dataset': dataset,\n        'precision': precision, 'category': cat, 'lead_lag': ll, 'notes': notes[:200]\n    }\n\n# Save for later use\nwith open('/tmp/parsed_exps.json', 'w') as f:\n    json.dump(results, f, indent=2, ensure_ascii=False)\n\n# Show which experiments still have all dashes\nmissing = [eid for eid, r in results.items() if all(v == '—' for v in r['lead_lag'].values())]\nprint(\"Experiments with NO lead-lag data in registry:\")\nfor m in missing:\n    print(f\"  {m} ({results[m]['category']})\")\n\nprint(f\"\\nTotal with some lead-lag: {len(results) - len(missing)}/{len(results)}\")\nPYEOF\n",
  "description": "Parse all metrics into uniform format",
  "timeout": "15000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/tmp/success_exps.json') as f:\n    success = json.load(f)\n\n# Build comprehensive extraction\nresults = {}\nfor eid in sorted(success.keys()):\n    e = success[eid]\n    metrics = e.get('metrics', {})\n    notes = e.get('notes') or ''\n    hyp = e.get('hypothesis') or ''\n    spec = e.get('spec', {})\n    cmd = spec.get('command', '') if isinstance(spec, dict) else ''\n    \n    if isinstance(metrics, str):\n        try:\n            metrics = json.loads(metrics)\n        except:\n            metrics = {}\n    if not isinstance(metrics, dict):\n        metrics = {}\n    \n    # Model detection\n    model = 'Pythia-410M'\n    if 'gpt2m' in eid or 'gpt2-medium' in cmd.lower() or 'gpt-2-medium' in hyp.lower():\n        model = 'GPT-2-Medium'\n    elif 'opt1b' in eid: model = 'OPT-1.3B'\n    elif 'pythia14b' in eid or 'scale_14b' in eid: model = 'Pythia-1.4B'\n    elif 'pythia1b_c4' in eid: model = 'Pythia-1B'\n    elif 'scale_69b' in eid: model = 'Pythia-6.9B'\n    \n    # Alpha\n    alpha_map = {'_a000_':'0.00','_a005_':'0.05','_a010_':'0.10','_a025_':'0.25',\n                 '_a050_':'0.50','_a060_':'0.60','_a075_':'0.75','_a100_':'1.00'}\n    alpha = '1.00' if 'mvp_v4' in eid else '?'\n    for pat, val in alpha_map.items():\n        if pat in eid: alpha = val; break\n    \n    # Seed\n    seed = '?'\n    for s in ['42','43','44','45']:\n        if f'_s{s}' in eid or f'rep{s}' in eid: seed = s; break\n    \n    # Dataset\n    dataset = 'C4' if '_c4_' in eid or 'pythia1b_c4' in eid else 'WikiText-103'\n    \n    # Precision\n    precision = 'fp32'\n    if '_bf16' in eid: precision = 'bf16'\n    \n    # Category\n    cat = 'main'\n    if 'interv' in eid or 'intervention' in eid: cat = 'intervention'\n    elif 'generalize' in eid or 'gen_wiki' in eid or 'gen_gpt2m' in eid: cat = 'cross-arch'\n    elif '_c4_' in eid and 'generalize' not in eid: cat = 'cross-dataset'\n    elif 'scale_' in eid: cat = 'scale'\n    elif 'mvp_' in eid: cat = 'mvp'\n    elif 'method_ablation' in eid: cat = 'ablation'\n    elif 'plan_009' in eid or 'conditional_granger' in eid: cat = 'analysis'\n    \n    # Extract lead-lag from various metric formats\n    ll = {'naive':'—','diff':'—','thresh':'—','pg_fwd':'—','pg_rev':'—','ty':'—','k_gte4':'—','mmct_wt':'—'}\n    \n    # Check five_method nested\n    fm = metrics.get('five_method', {})\n    if isinstance(fm, dict) and fm:\n        ll['pg_fwd'] = fm.get('perm_granger_fdr_sig', '—')\n        ll['ty'] = fm.get('ty_sig', '—')\n        ll['k_gte4'] = fm.get('robust_pairs_ge3', '—')  # k_gte4 maps to robust_pairs?\n    \n    # Direct keys (newer format)\n    if metrics.get('naive'): ll['naive'] = metrics['naive']\n    if metrics.get('naive_xcorr_fwd'): ll['naive'] = metrics['naive_xcorr_fwd']\n    if metrics.get('diff_xcorr_fwd'): ll['diff'] = metrics['diff_xcorr_fwd']\n    if metrics.get('threshold_onset_fwd'): ll['thresh'] = metrics['threshold_onset_fwd']\n    if metrics.get('thresh'): ll['thresh'] = metrics['thresh']\n    if metrics.get('perm_granger_fwd'): ll['pg_fwd'] = metrics['perm_granger_fwd']\n    if metrics.get('perm_granger_rev'): ll['pg_rev'] = metrics['perm_granger_rev']\n    if metrics.get('ty_granger_fwd'): ll['ty'] = metrics['ty_granger_fwd']\n    if metrics.get('k_gte4'): ll['k_gte4'] = metrics['k_gte4']\n    if metrics.get('mmct_weighted_fwd'): ll['mmct_wt'] = metrics['mmct_weighted_fwd']\n    \n    # lead_lag_unified_2sigma\n    llu = metrics.get('lead_lag_unified_2sigma', {})\n    if isinstance(llu, dict) and llu:\n        if llu.get('naive_xcorr_fwd'): ll['naive'] = llu['naive_xcorr_fwd']\n        if llu.get('diff_xcorr_fwd'): ll['diff'] = llu['diff_xcorr_fwd']\n        if llu.get('threshold_onset_fwd'): ll['thresh'] = llu['threshold_onset_fwd']\n        if llu.get('perm_granger_fwd'): ll['pg_fwd'] = llu['perm_granger_fwd']\n        if llu.get('perm_granger_rev'): ll['pg_rev'] = llu['perm_granger_rev']\n        if llu.get('ty_granger_fwd'): ll['ty'] = llu['ty_granger_fwd']\n        if llu.get('consensus_K4'): ll['k_gte4'] = llu['consensus_K4']\n    \n    # mmct nested\n    mmct = metrics.get('mmct', {})\n    if isinstance(mmct, dict) and mmct:\n        if mmct.get('weighted_pair_forward'): ll['mmct_wt'] = mmct['weighted_pair_forward']\n    \n    # Older format: perm_granger_fdr_fwd, diff_xcorr_fdr_fwd\n    if metrics.get('perm_granger_fdr_fwd'): ll['pg_fwd'] = metrics['perm_granger_fdr_fwd']\n    if metrics.get('perm_granger_fdr_rev'): ll['pg_rev'] = metrics['perm_granger_fdr_rev']\n    if metrics.get('diff_xcorr_fdr_fwd'): ll['diff'] = metrics['diff_xcorr_fdr_fwd']\n    if metrics.get('naive_xcorr_fwd'): ll['naive'] = metrics['naive_xcorr_fwd']\n    \n    # granger_fdr_sig_count (old a075_s42 format)\n    if metrics.get('granger_fdr_sig_count'): ll['pg_fwd'] = metrics['granger_fdr_sig_count']\n    \n    # permg_fwd_fdr_sig (c4 format)\n    if metrics.get('permg_fwd_fdr_sig'): ll['pg_fwd'] = metrics['permg_fwd_fdr_sig']\n    if metrics.get('permg_rev_fdr_sig'): ll['pg_rev'] = metrics['permg_rev_fdr_sig']\n    \n    results[eid] = {\n        'model': model, 'alpha': alpha, 'seed': seed, 'dataset': dataset,\n        'precision': precision, 'category': cat, 'lead_lag': ll, 'notes': notes[:200]\n    }\n\n# Save for later use\nwith open('/tmp/parsed_exps.json', 'w') as f:\n    json.dump(results, f, indent=2, ensure_ascii=False)\n\n# Show which experiments still have all dashes\nmissing = [eid for eid, r in results.items() if all(v == '—' for v in r['lead_lag'].values())]\nprint(\"Experiments with NO lead-lag data in registry:\")\nfor m in missing:\n    print(f\"  {m} ({results[m]['category']})\")\n\nprint(f\"\\nTotal with some lead-lag: {len(results) - len(missing)}/{len(results)}\")\nPYEOF\n",
    "description": "Parse all metrics into uniform format",
    "timeout": "15000"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-19T03:05:25.812615+00:00_

Experiments with NO lead-lag data in registry:
  alpha_sweep_a000_s42 (main)
  alpha_sweep_a025_s42_v3 (main)
  alpha_sweep_a025_s43 (main)
  alpha_sweep_a025_s44 (main)
  alpha_sweep_a050_s42 (main)
  alpha_sweep_a050_s43 (main)
  alpha_sweep_a075_s43 (main)
  alpha_sweep_a075_s44 (main)
  conditional_granger_d061 (analysis)
  gen_wiki_gpt2m_a025_s42 (cross-arch)
  gen_wiki_gpt2m_a100_s42_v3 (cross-arch)
  interv_pred_s43_bf16 (intervention)
  interv_react_s43_bf16 (intervention)
  intervention_predictive_s42 (intervention)
  intervention_reactive_s42 (intervention)
  method_ablation_phase1 (ablation)
  method_ablation_phase2 (ablation)
  method_ablation_phase3 (ablation)
  mvp_v4_rep42 (mvp)
  mvp_v4_rep43 (mvp)
  mvp_v4_rep44 (mvp)
  mvp_v4_rep45 (mvp)
  plan_009_bootstrap_ty (analysis)
  scale_14b_a050_s42 (scale)

Total with some lead-lag: 15/39

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-19T03:05:25.812771+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ssh westd-19828 'cd /root/autodl-tmp/distrib_canary_collapse && find results/ -name \"all_metrics.json\" -type f 2>/dev/null | sort'",
  "description": "Find all_metrics.json files on server",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "tool_args": {
    "command": "ssh westd-19828 'cd /root/autodl-tmp/distrib_canary_collapse && find results/ -name \"all_metrics.json\" -type f 2>/dev/null | sort'",
    "description": "Find all_metrics.json files on server",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-19T03:05:25.812898+00:00_

Warning: Permanently added '[connect.westd.seetacloud.com]:19828' (ED25519) to the list of known hosts.
results/alpha_sweep/a000_s42/all_metrics.json
results/alpha_sweep/a000_s43/all_metrics.json
results/alpha_sweep/a000_s44/all_metrics.json
results/alpha_sweep/a010_s42/all_metrics.json
results/alpha_sweep/a025_s43/all_metrics.json
results/alpha_sweep/a025_s44/all_metrics.json
results/alpha_sweep/a050_s42/all_metrics.json
results/alpha_sweep/a050_s43/all_metrics.json
results/alpha_sweep/a050_s44/all_metrics.json
results/alpha_sweep/a060_s42_bf16/all_metrics.json
results/alpha_sweep/a075_s42/all_metrics.json
results/alpha_sweep/a075_s43/all_metrics.json
results/alpha_sweep/a075_s44/all_metrics.json
results/generalize/gpt2m_wiki_a100_s42/all_metrics.json
results/generalize/opt1b_wiki_a100_s42/all_metrics.json
results/generalize/pythia14b_wiki_a100_s42/all_metrics.json
results/generalize/pythia14b_wiki_a100_s43/all_metrics.json
results/generalize/pythia1b_c4_a100_s42/all_metrics.json
results/generalize/pythia1b_c4_a100_s43/all_metrics.json
results/generalize/pythia410m_wiki_a100_s42/all_metrics.json
results/intervention/predictive_te_s42/all_metrics.json
results/intervention/reactive_d1_s42/all_metrics.json
results/scale_check/pythia14b_a050_s42/all_metrics.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-19T03:05:25.813033+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ssh westd-19828 'cd /root/autodl-tmp/distrib_canary_collapse && find results/ -name \"lead_lag_results.json\" -o -name \"five_method*.json\" -o -name \"lead_lag*.json\" 2>/dev/null | sort'",
  "description": "Find lead-lag result files on server",
  "timeout": "15000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "tool_args": {
    "command": "ssh westd-19828 'cd /root/autodl-tmp/distrib_canary_collapse && find results/ -name \"lead_lag_results.json\" -o -name \"five_method*.json\" -o -name \"lead_lag*.json\" 2>/dev/null | sort'",
    "description": "Find lead-lag result files on server",
    "timeout": "15000"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-19T03:05:25.813177+00:00_

Warning: Permanently added '[connect.westd.seetacloud.com]:19828' (ED25519) to the list of known hosts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-19T03:05:25.813332+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ssh westd-19828 'cd /root/autodl-tmp/distrib_canary_collapse && for f in results/alpha_sweep/a000_s42/all_metrics.json results/alpha_sweep/a025_s43/all_metrics.json results/alpha_sweep/a050_s42/all_metrics.json results/alpha_sweep/a050_s43/all_metrics.json results/alpha_sweep/a075_s42/all_metrics.json results/alpha_sweep/a075_s43/all_metrics.json results/alpha_sweep/a075_s44/all_metrics.json results/intervention/predictive_te_s42/all_metrics.json results/intervention/reactive_d1_s42/all_metrics.json results/scale_check/pythia14b_a050_s42/all_metrics.json results/generalize/gpt2m_wiki_a100_s42/all_metrics.json; do echo \"=== $f ===\"; python3 -c \"\nimport json\nwith open(\\\"$f\\\") as fp:\n    m = json.load(fp)\n# Look for lead-lag keys\nkeys_of_interest = [k for k in m.keys() if any(x in k.lower() for x in [\\\"naive\\\",\\\"granger\\\",\\\"perm\\\",\\\"xcorr\\\",\\\"thresh\\\",\\\"k_gte\\\",\\\"five_method\\\",\\\"mmct\\\",\\\"lead_lag\\\",\\\"consensus\\\"])]\nif keys_of_interest:\n    for k in keys_of_interest:\n        v = m[k]\n        print(f\\\"  {k}: {json.dumps(v)[:200]}\\\")\nelse:\n    print(\\\"  [no lead-lag keys found]\\\")\n    print(f\\\"  all keys: {list(m.keys())[:20]}\\\")\n\" 2>&1; done'",
  "description": "Extract lead-lag metrics from server all_metrics.json",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "tool_args": {
    "command": "ssh westd-19828 'cd /root/autodl-tmp/distrib_canary_collapse && for f in results/alpha_sweep/a000_s42/all_metrics.json results/alpha_sweep/a025_s43/all_metrics.json results/alpha_sweep/a050_s42/all_metrics.json results/alpha_sweep/a050_s43/all_metrics.json results/alpha_sweep/a075_s42/all_metrics.json results/alpha_sweep/a075_s43/all_metrics.json results/alpha_sweep/a075_s44/all_metrics.json results/intervention/predictive_te_s42/all_metrics.json results/intervention/reactive_d1_s42/all_metrics.json results/scale_check/pythia14b_a050_s42/all_metrics.json results/generalize/gpt2m_wiki_a100_s42/all_metrics.json; do echo \"=== $f ===\"; python3 -c \"\nimport json\nwith open(\\\"$f\\\") as fp:\n    m = json.load(fp)\n# Look for lead-lag keys\nkeys_of_interest = [k for k in m.keys() if any(x in k.lower() for x in [\\\"naive\\\",\\\"granger\\\",\\\"perm\\\",\\\"xcorr\\\",\\\"thresh\\\",\\\"k_gte\\\",\\\"five_method\\\",\\\"mmct\\\",\\\"lead_lag\\\",\\\"consensus\\\"])]\nif keys_of_interest:\n    for k in keys_of_interest:\n        v = m[k]\n        print(f\\\"  {k}: {json.dumps(v)[:200]}\\\")\nelse:\n    print(\\\"  [no lead-lag keys found]\\\")\n    print(f\\\"  all keys: {list(m.keys())[:20]}\\\")\n\" 2>&1; done'",
    "description": "Extract lead-lag metrics from server all_metrics.json",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-19T03:05:25.813481+00:00_

Exit code 1
Warning: Permanently added '[connect.westd.seetacloud.com]:19828' (ED25519) to the list of known hosts.
=== results/alpha_sweep/a000_s42/all_metrics.json ===
Traceback (most recent call last):
  File "&lt;string>", line 6, in &lt;module>
AttributeError: 'list' object has no attribute 'keys'
=== results/alpha_sweep/a025_s43/all_metrics.json ===
Traceback (most recent call last):
  File "&lt;string>", line 6, in &lt;module>
AttributeError: 'list' object has no attribute 'keys'
=== results/alpha_sweep/a050_s42/all_metrics.json ===
Traceback (most recent call last):
  File "&lt;string>", line 6, in &lt;module>
AttributeError: 'list' object has no attribute 'keys'
=== results/alpha_sweep/a050_s43/all_metrics.json ===
Traceback (most recent call last):
  File "&lt;string>", line 6, in &lt;module>
AttributeError: 'list' object has no attribute 'keys'
=== results/alpha_sweep/a075_s42/all_metrics.json ===
Traceback (most recent call last):
  File "&lt;string>", line 6, in &lt;module>
AttributeError: 'list' object has no attribute 'keys'
=== results/alpha_sweep/a075_s43/all_metrics.json ===
Traceback (most recent call last):
  File "&lt;string>", line 6, in &lt;module>
AttributeError: 'list' object has no attribute 'keys'
=== results/alpha_sweep/a075_s44/all_metrics.json ===
Traceback (most recent call last):
  File "&lt;string>", line 6, in &lt;module>
AttributeError: 'list' object has no attribute 'keys'
=== results/intervention/predictive_te_s42/all_metrics.json ===
Traceback (most recent call last):
  File "&lt;string>", line 6, in &lt;module>
AttributeError: 'list' object has no attribute 'keys'
=== results/intervention/reactive_d1_s42/all_metrics.json ===
Traceback (most recent call last):
  File "&lt;string>", line 6, in &lt;module>
AttributeError: 'list' object has no attribute 'keys'
=== results/scale_check/pythia14b_a050_s42/all_metrics.json ===
Traceback (most recent call last):
  File "&lt;string>", line 6, in &lt;module>
AttributeError: 'list' object has no attribute 'keys'
=== results/generalize/gpt2m_wiki_a
…[truncated 156 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-19T03:05:25.813619+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ssh westd-19828 'cd /root/autodl-tmp/distrib_canary_collapse && python3 -c \"\nimport json\nwith open(\\\"results/alpha_sweep/a000_s42/all_metrics.json\\\") as f:\n    m = json.load(f)\nprint(type(m))\nif isinstance(m, list):\n    print(f\\\"len={len(m)}\\\")\n    print(f\\\"first element type: {type(m[0])}\\\")\n    if isinstance(m[0], dict):\n        print(f\\\"first element keys: {list(m[0].keys())[:15]}\\\")\n        print(json.dumps(m[0], indent=2)[:500])\n\"'",
  "description": "Check structure of all_metrics.json",
  "timeout": "15000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "tool_args": {
    "command": "ssh westd-19828 'cd /root/autodl-tmp/distrib_canary_collapse && python3 -c \"\nimport json\nwith open(\\\"results/alpha_sweep/a000_s42/all_metrics.json\\\") as f:\n    m = json.load(f)\nprint(type(m))\nif isinstance(m, list):\n    print(f\\\"len={len(m)}\\\")\n    print(f\\\"first element type: {type(m[0])}\\\")\n    if isinstance(m[0], dict):\n        print(f\\\"first element keys: {list(m[0].keys())[:15]}\\\")\n        print(json.dumps(m[0], indent=2)[:500])\n\"'",
    "description": "Check structure of all_metrics.json",
    "timeout": "15000"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-19T03:05:25.813749+00:00_

Warning: Permanently added '[connect.westd.seetacloud.com]:19828' (ED25519) to the list of known hosts.
&lt;class 'list'>
len=11
first element type: &lt;class 'dict'>
first element keys: ['token_entropy', 'self_bleu', 'distinct_1', 'distinct_2', 'distinct_3', 'ece', 'effective_rank', 'perplexity', 'mauve', 'generation']
{
  "token_entropy": 3.2341948700181407,
  "self_bleu": 0.010194395218435404,
  "distinct_1": 0.0982156685333268,
  "distinct_2": 0.5178027030111348,
  "distinct_3": 0.8127277321747353,
  "ece": 0.010804557477709054,
  "effective_rank": 46.612774691899155,
  "perplexity": 26.948958972544652,
  "mauve": 0.03406737671684175,
  "generation": 0
}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-19T03:05:25.813897+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ssh westd-19828 'cd /root/autodl-tmp/distrib_canary_collapse && find results/ -name \"*.json\" -not -name \"all_metrics.json\" -not -name \"config.json\" 2>/dev/null | head -50'",
  "description": "Find other JSON result files",
  "timeout": "15000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "tool_args": {
    "command": "ssh westd-19828 'cd /root/autodl-tmp/distrib_canary_collapse && find results/ -name \"*.json\" -not -name \"all_metrics.json\" -not -name \"config.json\" 2>/dev/null | head -50'",
    "description": "Find other JSON result files",
    "timeout": "15000"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-19T03:05:25.814029+00:00_

Warning: Permanently added '[connect.westd.seetacloud.com]:19828' (ED25519) to the list of known hosts.
results/alpha_sweep/a000_s42/gen_0/metrics.json
results/alpha_sweep/a000_s42/gen_1/metrics.json
results/alpha_sweep/a000_s42/gen_2/metrics.json
results/alpha_sweep/a000_s42/gen_3/metrics.json
results/alpha_sweep/a000_s42/gen_4/metrics.json
results/alpha_sweep/a000_s42/gen_5/metrics.json
results/alpha_sweep/a000_s42/gen_6/metrics.json
results/alpha_sweep/a000_s42/gen_7/metrics.json
results/alpha_sweep/a000_s42/gen_8/metrics.json
results/alpha_sweep/a000_s42/gen_9/metrics.json
results/alpha_sweep/a000_s42/gen_10/checkpoint/generation_config.json
results/alpha_sweep/a000_s42/gen_10/checkpoint/tokenizer_config.json
results/alpha_sweep/a000_s42/gen_10/checkpoint/special_tokens_map.json
results/alpha_sweep/a000_s42/gen_10/checkpoint/tokenizer.json
results/alpha_sweep/a000_s42/gen_10/metrics.json
results/alpha_sweep/a000_s42/analysis/5method_leadlag.json
results/alpha_sweep/analysis_summary.json
results/alpha_sweep/analysis/alpha_sweep_analysis.json
results/alpha_sweep/a050_s42/gen_0/metrics.json
results/alpha_sweep/a050_s42/gen_1/metrics.json
results/alpha_sweep/a050_s42/gen_2/metrics.json
results/alpha_sweep/a050_s42/gen_3/metrics.json
results/alpha_sweep/a050_s42/gen_4/metrics.json
results/alpha_sweep/a050_s42/gen_5/metrics.json
results/alpha_sweep/a050_s42/gen_6/metrics.json
results/alpha_sweep/a050_s42/gen_7/metrics.json
results/alpha_sweep/a050_s42/gen_8/metrics.json
results/alpha_sweep/a050_s42/gen_9/metrics.json
results/alpha_sweep/a050_s42/gen_10/checkpoint/generation_config.json
results/alpha_sweep/a050_s42/gen_10/checkpoint/tokenizer_config.json
results/alpha_sweep/a050_s42/gen_10/checkpoint/special_tokens_map.json
results/alpha_sweep/a050_s42/gen_10/checkpoint/tokenizer.json
results/alpha_sweep/a050_s42/gen_10/metrics.json
results/alpha_sweep/a050_s42/analysis/5method_leadlag.json
results/alpha_sweep/pooled_panel_results.json
results/alpha_sweep/a075_s42/gen
…[truncated 768 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-19T03:05:25.814161+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ssh westd-19828 'cd /root/autodl-tmp/distrib_canary_collapse && find results/ -name \"5method_leadlag.json\" -o -name \"lead_lag*.json\" -o -name \"five_method*.json\" -o -name \"*leadlag*\" -o -name \"*lead_lag*\" 2>/dev/null | sort'",
  "description": "Find all lead-lag analysis files",
  "timeout": "15000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "tool_args": {
    "command": "ssh westd-19828 'cd /root/autodl-tmp/distrib_canary_collapse && find results/ -name \"5method_leadlag.json\" -o -name \"lead_lag*.json\" -o -name \"five_method*.json\" -o -name \"*leadlag*\" -o -name \"*lead_lag*\" 2>/dev/null | sort'",
    "description": "Find all lead-lag analysis files",
    "timeout": "15000"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-19T03:05:25.814309+00:00_

Warning: Permanently added '[connect.westd.seetacloud.com]:19828' (ED25519) to the list of known hosts.
results/alpha_sweep/a000_s42/analysis/5method_leadlag.json
results/alpha_sweep/a000_s43/analysis/5method_leadlag.json
results/alpha_sweep/a000_s44/analysis/5method_leadlag.json
results/alpha_sweep/a025_s43/analysis/5method_leadlag.json
results/alpha_sweep/a025_s44/analysis/5method_leadlag.json
results/alpha_sweep/a050_s42/analysis/5method_leadlag.json
results/alpha_sweep/a050_s43/analysis/5method_leadlag.json
results/alpha_sweep/a050_s44/analysis/5method_leadlag.json
results/alpha_sweep/a060_s42_bf16/analysis/5method_leadlag.json
results/alpha_sweep/a075_s42/analysis/5method_leadlag.json
results/alpha_sweep/a075_s43/analysis/5method_leadlag.json
results/alpha_sweep/a075_s44/analysis/5method_leadlag.json
results/generalize/gpt2m_wiki_a100_s42/analysis/5method_leadlag.json
results/generalize/opt1b_wiki_a100_s42/analysis/5method_leadlag.json
results/generalize/pythia14b_wiki_a100_s42/analysis/5method_leadlag.json
results/generalize/pythia14b_wiki_a100_s43/analysis/5method_leadlag.json
results/generalize/pythia1b_c4_a100_s42/analysis/5method_leadlag.json
results/generalize/pythia1b_c4_a100_s43/analysis/5method_leadlag.json
results/generalize/pythia410m_wiki_a100_s42/analysis/5method_leadlag.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-19T03:05:25.814445+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ssh westd-19828 'cd /root/autodl-tmp/distrib_canary_collapse && python3 -c \"\nimport json, os\n\ndirs = [\n    \\\"results/alpha_sweep/a000_s42\\\",\n    \\\"results/alpha_sweep/a025_s43\\\",\n    \\\"results/alpha_sweep/a050_s42\\\",\n    \\\"results/alpha_sweep/a050_s43\\\",\n    \\\"results/alpha_sweep/a075_s42\\\",\n    \\\"results/alpha_sweep/a075_s43\\\",\n    \\\"results/alpha_sweep/a075_s44\\\",\n    \\\"results/generalize/gpt2m_wiki_a100_s42\\\",\n]\n\nfor d in dirs:\n    fp = os.path.join(d, \\\"analysis/5method_leadlag.json\\\")\n    if os.path.exists(fp):\n        with open(fp) as f:\n            m = json.load(f)\n        print(f\\\"=== {d} ===\\\")\n        if isinstance(m, dict):\n            # Look for summary keys\n            summary = m.get(\\\"summary\\\", m.get(\\\"pair_summary\\\", {}))\n            if summary:\n                print(f\\\"  summary keys: {list(summary.keys())[:10]}\\\")\n                print(f\\\"  summary: {json.dumps(summary)[:400]}\\\")\n            else:\n                print(f\\\"  top keys: {list(m.keys())[:15]}\\\")\n                # Try to find totals\n                for k in [\\\"naive_xcorr_fwd\\\",\\\"diff_xcorr_fwd\\\",\\\"threshold_onset_fwd\\\",\\\"perm_granger_fwd\\\",\\\"perm_granger_rev\\\",\\\"ty_granger_fwd\\\",\\\"consensus_K4\\\",\\\"k_gte4\\\",\\\"totals\\\",\\\"overall\\\"]:\n                    if k in m:\n                        print(f\\\"  {k}: {json.dumps(m[k])[:200]}\\\")\n        print()\n\"'",
  "description": "Read 5method_leadlag.json structure",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "tool_args": {
    "command": "ssh westd-19828 'cd /root/autodl-tmp/distrib_canary_collapse && python3 -c \"\nimport json, os\n\ndirs = [\n    \\\"results/alpha_sweep/a000_s42\\\",\n    \\\"results/alpha_sweep/a025_s43\\\",\n    \\\"results/alpha_sweep/a050_s42\\\",\n    \\\"results/alpha_sweep/a050_s43\\\",\n    \\\"results/alpha_sweep/a075_s42\\\",\n    \\\"results/alpha_sweep/a075_s43\\\",\n    \\\"results/alpha_sweep/a075_s44\\\",\n    \\\"results/generalize/gpt2m_wiki_a100_s42\\\",\n]\n\nfor d in dirs:\n    fp = os.path.join(d, \\\"analysis/5method_leadlag.json\\\")\n    if os.path.exists(fp):\n        with open(fp) as f:\n            m = json.load(f)\n        print(f\\\"=== {d} ===\\\")\n        if isinstance(m, dict):\n            # Look for summary keys\n            summary = m.get(\\\"summary\\\", m.get(\\\"pair_summary\\\", {}))\n            if summary:\n                print(f\\\"  summary keys: {list(summary.keys())[:10]}\\\")\n                print(f\\\"  summary: {json.dumps(summary)[:400]}\\\")\n            else:\n                print(f\\\"  top keys: {list(m.keys())[:15]}\\\")\n                # Try to find totals\n                for k in [\\\"naive_xcorr_fwd\\\",\\\"diff_xcorr_fwd\\\",\\\"threshold_onset_fwd\\\",\\\"perm_granger_fwd\\\",\\\"perm_granger_rev\\\",\\\"ty_granger_fwd\\\",\\\"consensus_K4\\\",\\\"k_gte4\\\",\\\"totals\\\",\\\"overall\\\"]:\n                    if k in m:\n                        print(f\\\"  {k}: {json.dumps(m[k])[:200]}\\\")\n        print()\n\"'",
    "description": "Read 5method_leadlag.json structure",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-19T03:05:25.814592+00:00_

Warning: Permanently added '[connect.westd.seetacloud.com]:19828' (ED25519) to the list of known hosts.
=== results/alpha_sweep/a000_s42 ===
  summary keys: ['perm_granger_fdr_forward_sig', 'perm_granger_fdr_reverse_sig', 'diff_xcorr_fdr_forward_sig', 'diff_xcorr_fdr_reverse_sig', 'threshold_forward_sig', 'ty_forward_sig', 'robust_pairs']
  summary: {"perm_granger_fdr_forward_sig": 0, "perm_granger_fdr_reverse_sig": 1, "diff_xcorr_fdr_forward_sig": 4, "diff_xcorr_fdr_reverse_sig": 4, "threshold_forward_sig": 3, "ty_forward_sig": 1, "robust_pairs": 1}

=== results/alpha_sweep/a025_s43 ===
  summary keys: ['perm_granger_fdr_forward_sig', 'perm_granger_fdr_reverse_sig', 'diff_xcorr_fdr_forward_sig', 'diff_xcorr_fdr_reverse_sig', 'threshold_forward_sig', 'ty_forward_sig', 'robust_pairs']
  summary: {"perm_granger_fdr_forward_sig": 0, "perm_granger_fdr_reverse_sig": 0, "diff_xcorr_fdr_forward_sig": 3, "diff_xcorr_fdr_reverse_sig": 3, "threshold_forward_sig": 0, "ty_forward_sig": 0, "robust_pairs": 0}

=== results/alpha_sweep/a050_s42 ===
  summary keys: ['perm_granger_fdr_forward_sig', 'perm_granger_fdr_reverse_sig', 'diff_xcorr_fdr_forward_sig', 'diff_xcorr_fdr_reverse_sig', 'threshold_forward_sig', 'ty_forward_sig', 'robust_pairs']
  summary: {"perm_granger_fdr_forward_sig": 0, "perm_granger_fdr_reverse_sig": 0, "diff_xcorr_fdr_forward_sig": 8, "diff_xcorr_fdr_reverse_sig": 8, "threshold_forward_sig": 0, "ty_forward_sig": 0, "robust_pairs": 0}

=== results/alpha_sweep/a050_s43 ===
  summary keys: ['perm_granger_fdr_forward_sig', 'perm_granger_fdr_reverse_sig', 'diff_xcorr_fdr_forward_sig', 'diff_xcorr_fdr_reverse_sig', 'threshold_forward_sig', 'ty_forward_sig', 'robust_pairs']
  summary: {"perm_granger_fdr_forward_sig": 6, "perm_granger_fdr_reverse_sig": 0, "diff_xcorr_fdr_forward_sig": 6, "diff_xcorr_fdr_reverse_sig": 6, "threshold_forward_sig": 0, "ty_forward_sig": 0, "robust_pairs": 1}

=== results/alpha_sweep/a075_s42 ===
  summary keys: ['perm_granger_fdr_forward
…[truncated 1745 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-19T03:05:25.814749+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ssh westd-19828 'cd /root/autodl-tmp/distrib_canary_collapse && python3 << \"PYEOF\"\nimport json, os, glob\n\n# All 5method files\nfiles = sorted(glob.glob(\"results/**/5method_leadlag.json\", recursive=True))\n\nfor fp in files:\n    with open(fp) as f:\n        m = json.load(f)\n    \n    s = m.get(\"summary\", {})\n    \n    # Also look for naive xcorr info in the pairs\n    pairs = m.get(\"pairs\", m.get(\"pair_results\", {}))\n    naive_fwd = 0\n    total_pairs = 0\n    if isinstance(pairs, dict):\n        for pk, pv in pairs.items():\n            if isinstance(pv, dict):\n                total_pairs += 1\n                # naive xcorr\n                naive = pv.get(\"naive_xcorr\", {})\n                if isinstance(naive, dict):\n                    r = abs(naive.get(\"max_r\", 0))\n                    if r > 0.5:  # significant naive correlation\n                        naive_fwd += 1\n    elif isinstance(pairs, list):\n        for pv in pairs:\n            if isinstance(pv, dict):\n                total_pairs += 1\n                naive = pv.get(\"naive_xcorr\", {})\n                if isinstance(naive, dict):\n                    r = abs(naive.get(\"max_r\", 0))\n                    if r > 0.5:\n                        naive_fwd += 1\n    \n    dir_name = os.path.dirname(os.path.dirname(fp))\n    print(f\"{dir_name}: PG_fwd={s.get(\\\"perm_granger_fdr_forward_sig\\\",\\\"?\\\")}/8  PG_rev={s.get(\\\"perm_granger_fdr_reverse_sig\\\",\\\"?\\\")}/8  Diff={s.get(\\\"diff_xcorr_fdr_forward_sig\\\",\\\"?\\\")}/8  Thresh={s.get(\\\"threshold_forward_sig\\\",\\\"?\\\")}/8  TY={s.get(\\\"ty_forward_sig\\\",\\\"?\\\")}/8  RobustK4={s.get(\\\"robust_pairs\\\",\\\"?\\\")}/8  Naive~={naive_fwd}/{total_pairs}\")\n\nPYEOF\n'",
  "description": "Extract all lead-lag summaries from server",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "tool_args": {
    "command": "ssh westd-19828 'cd /root/autodl-tmp/distrib_canary_collapse && python3 << \"PYEOF\"\nimport json, os, glob\n\n# All 5method files\nfiles = sorted(glob.glob(\"results/**/5method_leadlag.json\", recursive=True))\n\nfor fp in files:\n    with open(fp) as f:\n        m = json.load(f)\n    \n    s = m.get(\"summary\", {})\n    \n    # Also look for naive xcorr info in the pairs\n    pairs = m.get(\"pairs\", m.get(\"pair_results\", {}))\n    naive_fwd = 0\n    total_pairs = 0\n    if isinstance(pairs, dict):\n        for pk, pv in pairs.items():\n            if isinstance(pv, dict):\n                total_pairs += 1\n                # naive xcorr\n                naive = pv.get(\"naive_xcorr\", {})\n                if isinstance(naive, dict):\n                    r = abs(naive.get(\"max_r\", 0))\n                    if r > 0.5:  # significant naive correlation\n                        naive_fwd += 1\n    elif isinstance(pairs, list):\n        for pv in pairs:\n            if isinstance(pv, dict):\n                total_pairs += 1\n                naive = pv.get(\"naive_xcorr\", {})\n                if isinstance(naive, dict):\n                    r = abs(naive.get(\"max_r\", 0))\n                    if r > 0.5:\n                        naive_fwd += 1\n    \n    dir_name = os.path.dirname(os.path.dirname(fp))\n    print(f\"{dir_name}: PG_fwd={s.get(\\\"perm_granger_fdr_forward_sig\\\",\\\"?\\\")}/8  PG_rev={s.get(\\\"perm_granger_fdr_reverse_sig\\\",\\\"?\\\")}/8  Diff={s.get(\\\"diff_xcorr_fdr_forward_sig\\\",\\\"?\\\")}/8  Thresh={s.get(\\\"threshold_forward_sig\\\",\\\"?\\\")}/8  TY={s.get(\\\"ty_forward_sig\\\",\\\"?\\\")}/8  RobustK4={s.get(\\\"robust_pairs\\\",\\\"?\\\")}/8  Naive~={naive_fwd}/{total_pairs}\")\n\nPYEOF\n'",
    "description": "Extract all lead-lag summaries from server",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-19T03:05:25.814887+00:00_

Exit code 1
Warning: Permanently added '[connect.westd.seetacloud.com]:19828' (ED25519) to the list of known hosts.
  File "&lt;stdin>", line 37
    print(f"{dir_name}: PG_fwd={s.get(\"perm_granger_fdr_forward_sig\",\"?\")}/8  PG_rev={s.get(\"perm_granger_fdr_reverse_sig\",\"?\")}/8  Diff={s.get(\"diff_xcorr_fdr_forward_sig\",\"?\")}/8  Thresh={s.get(\"threshold_forward_sig\",\"?\")}/8  TY={s.get(\"ty_forward_sig\",\"?\")}/8  RobustK4={s.get(\"robust_pairs\",\"?\")}/8  Naive~={naive_fwd}/{total_pairs}")
                                                                                                                                                                                                                                                                                                                                                                          ^
SyntaxError: f-string expression part cannot include a backslash

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-19T03:05:25.815017+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ssh westd-19828 'cd /root/autodl-tmp/distrib_canary_collapse && python3 -c \"\nimport json, os, glob\n\nfiles = sorted(glob.glob(\\\"results/**/5method_leadlag.json\\\", recursive=True))\nfor fp in files:\n    with open(fp) as f:\n        m = json.load(f)\n    s = m.get(\\\"summary\\\", {})\n    d = os.path.dirname(os.path.dirname(fp))\n    pg_f = s.get(\\\"perm_granger_fdr_forward_sig\\\", \\\"?\\\")\n    pg_r = s.get(\\\"perm_granger_fdr_reverse_sig\\\", \\\"?\\\")\n    diff = s.get(\\\"diff_xcorr_fdr_forward_sig\\\", \\\"?\\\")\n    thresh = s.get(\\\"threshold_forward_sig\\\", \\\"?\\\")\n    ty = s.get(\\\"ty_forward_sig\\\", \\\"?\\\")\n    rk = s.get(\\\"robust_pairs\\\", \\\"?\\\")\n    print(d, pg_f, pg_r, diff, thresh, ty, rk, sep=\\\"|\\\")\n\"'",
  "description": "Extract all lead-lag summaries (fixed quoting)",
  "timeout": "15000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "tool_args": {
    "command": "ssh westd-19828 'cd /root/autodl-tmp/distrib_canary_collapse && python3 -c \"\nimport json, os, glob\n\nfiles = sorted(glob.glob(\\\"results/**/5method_leadlag.json\\\", recursive=True))\nfor fp in files:\n    with open(fp) as f:\n        m = json.load(f)\n    s = m.get(\\\"summary\\\", {})\n    d = os.path.dirname(os.path.dirname(fp))\n    pg_f = s.get(\\\"perm_granger_fdr_forward_sig\\\", \\\"?\\\")\n    pg_r = s.get(\\\"perm_granger_fdr_reverse_sig\\\", \\\"?\\\")\n    diff = s.get(\\\"diff_xcorr_fdr_forward_sig\\\", \\\"?\\\")\n    thresh = s.get(\\\"threshold_forward_sig\\\", \\\"?\\\")\n    ty = s.get(\\\"ty_forward_sig\\\", \\\"?\\\")\n    rk = s.get(\\\"robust_pairs\\\", \\\"?\\\")\n    print(d, pg_f, pg_r, diff, thresh, ty, rk, sep=\\\"|\\\")\n\"'",
    "description": "Extract all lead-lag summaries (fixed quoting)",
    "timeout": "15000"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-19T03:05:25.815144+00:00_

Warning: Permanently added '[connect.westd.seetacloud.com]:19828' (ED25519) to the list of known hosts.
results/alpha_sweep/a000_s42|0|1|4|3|1|1
results/alpha_sweep/a000_s43|0|0|3|1|1|0
results/alpha_sweep/a000_s44|0|0|3|1|0|0
results/alpha_sweep/a025_s43|0|0|3|0|0|0
results/alpha_sweep/a025_s44|0|0|1|0|2|0
results/alpha_sweep/a050_s42|0|0|8|0|0|0
results/alpha_sweep/a050_s43|6|0|6|0|0|1
results/alpha_sweep/a050_s44|3|0|6|0|0|0
results/alpha_sweep/a060_s42_bf16|8|0|8|0|0|1
results/alpha_sweep/a075_s42|8|0|8|4|1|5
results/alpha_sweep/a075_s43|5|0|8|0|1|4
results/alpha_sweep/a075_s44|6|0|8|4|1|5
results/generalize/gpt2m_wiki_a100_s42|6|3|8|0|2|2
results/generalize/opt1b_wiki_a100_s42|6|0|8|1|0|2
results/generalize/pythia14b_wiki_a100_s42|2|0|6|0|0|1
results/generalize/pythia14b_wiki_a100_s43|6|0|6|0|2|6
results/generalize/pythia1b_c4_a100_s42|6|3|6|0|1|2
results/generalize/pythia1b_c4_a100_s43|4|0|6|0|2|3
results/generalize/pythia410m_wiki_a100_s42|6|0|8|0|2|2

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-19T03:05:25.815293+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ssh westd-19828 'cd /root/autodl-tmp/distrib_canary_collapse && python3 -c \"\nimport json, os, glob\n\nfiles = sorted(glob.glob(\\\"results/**/5method_leadlag.json\\\", recursive=True))\nfor fp in files:\n    with open(fp) as f:\n        m = json.load(f)\n    \n    pairs = m.get(\\\"pairs\\\", m.get(\\\"pair_results\\\", []))\n    naive_fwd = 0\n    total = 0\n    if isinstance(pairs, dict):\n        items = pairs.values()\n    elif isinstance(pairs, list):\n        items = pairs\n    else:\n        items = []\n    \n    for pv in items:\n        if not isinstance(pv, dict):\n            continue\n        total += 1\n        nx = pv.get(\\\"naive_xcorr\\\", {})\n        if isinstance(nx, dict):\n            r = abs(nx.get(\\\"max_r\\\", nx.get(\\\"r\\\", 0)))\n            p = nx.get(\\\"p_value\\\", nx.get(\\\"p\\\", 1))\n            if r > 0.5 and p < 0.05:\n                naive_fwd += 1\n    \n    d = os.path.dirname(os.path.dirname(fp))\n    print(d, naive_fwd, total, sep=\\\"|\\\")\n\"'",
  "description": "Extract naive xcorr counts",
  "timeout": "15000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "tool_args": {
    "command": "ssh westd-19828 'cd /root/autodl-tmp/distrib_canary_collapse && python3 -c \"\nimport json, os, glob\n\nfiles = sorted(glob.glob(\\\"results/**/5method_leadlag.json\\\", recursive=True))\nfor fp in files:\n    with open(fp) as f:\n        m = json.load(f)\n    \n    pairs = m.get(\\\"pairs\\\", m.get(\\\"pair_results\\\", []))\n    naive_fwd = 0\n    total = 0\n    if isinstance(pairs, dict):\n        items = pairs.values()\n    elif isinstance(pairs, list):\n        items = pairs\n    else:\n        items = []\n    \n    for pv in items:\n        if not isinstance(pv, dict):\n            continue\n        total += 1\n        nx = pv.get(\\\"naive_xcorr\\\", {})\n        if isinstance(nx, dict):\n            r = abs(nx.get(\\\"max_r\\\", nx.get(\\\"r\\\", 0)))\n            p = nx.get(\\\"p_value\\\", nx.get(\\\"p\\\", 1))\n            if r > 0.5 and p < 0.05:\n                naive_fwd += 1\n    \n    d = os.path.dirname(os.path.dirname(fp))\n    print(d, naive_fwd, total, sep=\\\"|\\\")\n\"'",
    "description": "Extract naive xcorr counts",
    "timeout": "15000"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-19T03:05:25.815433+00:00_

Warning: Permanently added '[connect.westd.seetacloud.com]:19828' (ED25519) to the list of known hosts.
results/alpha_sweep/a000_s42|0|8
results/alpha_sweep/a000_s43|0|8
results/alpha_sweep/a000_s44|0|8
results/alpha_sweep/a025_s43|0|8
results/alpha_sweep/a025_s44|0|8
results/alpha_sweep/a050_s42|0|8
results/alpha_sweep/a050_s43|0|8
results/alpha_sweep/a050_s44|0|8
results/alpha_sweep/a060_s42_bf16|0|8
results/alpha_sweep/a075_s42|0|8
results/alpha_sweep/a075_s43|0|8
results/alpha_sweep/a075_s44|0|8
results/generalize/gpt2m_wiki_a100_s42|0|8
results/generalize/opt1b_wiki_a100_s42|0|8
results/generalize/pythia14b_wiki_a100_s42|0|8
results/generalize/pythia14b_wiki_a100_s43|0|8
results/generalize/pythia1b_c4_a100_s42|0|8
results/generalize/pythia1b_c4_a100_s43|0|8
results/generalize/pythia410m_wiki_a100_s42|0|8

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-19T03:05:25.815569+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ssh westd-19828 'cd /root/autodl-tmp/distrib_canary_collapse && python3 -c \"\nimport json\n\n# Check the structure of a pair in detail\nwith open(\\\"results/alpha_sweep/a075_s42/analysis/5method_leadlag.json\\\") as f:\n    m = json.load(f)\n\npairs = m.get(\\\"pairs\\\", m.get(\\\"pair_results\\\", []))\nif isinstance(pairs, dict):\n    for k, v in list(pairs.items())[:2]:\n        print(f\\\"Pair: {k}\\\")\n        print(json.dumps(v, indent=2)[:600])\n        print()\nelif isinstance(pairs, list):\n    for v in pairs[:2]:\n        print(json.dumps(v, indent=2)[:600])\n        print()\n\"'",
  "description": "Check pair structure for naive xcorr format",
  "timeout": "15000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "tool_args": {
    "command": "ssh westd-19828 'cd /root/autodl-tmp/distrib_canary_collapse && python3 -c \"\nimport json\n\n# Check the structure of a pair in detail\nwith open(\\\"results/alpha_sweep/a075_s42/analysis/5method_leadlag.json\\\") as f:\n    m = json.load(f)\n\npairs = m.get(\\\"pairs\\\", m.get(\\\"pair_results\\\", []))\nif isinstance(pairs, dict):\n    for k, v in list(pairs.items())[:2]:\n        print(f\\\"Pair: {k}\\\")\n        print(json.dumps(v, indent=2)[:600])\n        print()\nelif isinstance(pairs, list):\n    for v in pairs[:2]:\n        print(json.dumps(v, indent=2)[:600])\n        print()\n\"'",
    "description": "Check pair structure for naive xcorr format",
    "timeout": "15000"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-19T03:05:25.815703+00:00_

Warning: Permanently added '[connect.westd.seetacloud.com]:19828' (ED25519) to the list of known hosts.
{
  "forward": {
    "canary": "token_entropy",
    "downstream": "distinct_1",
    "direction": "forward",
    "naive_xcorr": {
      "method": "naive_xcorr",
      "peak_lag": 5,
      "r": -0.9716,
      "p_value": 0.001198,
      "significant": true,
      "all_lags": [
        {
          "lag": -5,
          "r": 0.8178,
          "p": 0.046795
        },
        {
          "lag": -4,
          "r": 0.7991,
          "p": 0.03109
        },
        {
          "lag": -3,
          "r": 0.7715,
          "p": 0.024957
        },
        {
          "lag": -2,
          "r": 0.8124,
     

{
  "forward": {
    "canary": "token_entropy",
    "downstream": "distinct_2",
    "direction": "forward",
    "naive_xcorr": {
      "method": "naive_xcorr",
      "peak_lag": 5,
      "r": -0.9788,
      "p_value": 0.000669,
      "significant": true,
      "all_lags": [
        {
          "lag": -5,
          "r": 0.821,
          "p": 0.045172
        },
        {
          "lag": -4,
          "r": 0.7897,
          "p": 0.034673
        },
        {
          "lag": -3,
          "r": 0.7243,
          "p": 0.042159
        },
        {
          "lag": -2,
          "r": 0.7716,

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-19T03:05:25.815829+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ssh westd-19828 'cd /root/autodl-tmp/distrib_canary_collapse && python3 -c \"\nimport json, os, glob\n\nfiles = sorted(glob.glob(\\\"results/**/5method_leadlag.json\\\", recursive=True))\nfor fp in files:\n    with open(fp) as f:\n        m = json.load(f)\n    \n    pairs = m.get(\\\"pairs\\\", m.get(\\\"pair_results\\\", []))\n    if isinstance(pairs, dict):\n        items = list(pairs.values())\n    elif isinstance(pairs, list):\n        items = pairs\n    else:\n        items = []\n    \n    naive_sig = 0\n    total = 0\n    for pv in items:\n        if not isinstance(pv, dict):\n            continue\n        fwd = pv.get(\\\"forward\\\", pv)\n        if isinstance(fwd, dict):\n            nx = fwd.get(\\\"naive_xcorr\\\", {})\n            if isinstance(nx, dict):\n                total += 1\n                if nx.get(\\\"significant\\\", False):\n                    naive_sig += 1\n    \n    d = os.path.dirname(os.path.dirname(fp))\n    print(d, naive_sig, total, sep=\\\"|\\\")\n\"'",
  "description": "Extract naive xcorr significant count from forward pairs",
  "timeout": "15000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "tool_args": {
    "command": "ssh westd-19828 'cd /root/autodl-tmp/distrib_canary_collapse && python3 -c \"\nimport json, os, glob\n\nfiles = sorted(glob.glob(\\\"results/**/5method_leadlag.json\\\", recursive=True))\nfor fp in files:\n    with open(fp) as f:\n        m = json.load(f)\n    \n    pairs = m.get(\\\"pairs\\\", m.get(\\\"pair_results\\\", []))\n    if isinstance(pairs, dict):\n        items = list(pairs.values())\n    elif isinstance(pairs, list):\n        items = pairs\n    else:\n        items = []\n    \n    naive_sig = 0\n    total = 0\n    for pv in items:\n        if not isinstance(pv, dict):\n            continue\n        fwd = pv.get(\\\"forward\\\", pv)\n        if isinstance(fwd, dict):\n            nx = fwd.get(\\\"naive_xcorr\\\", {})\n            if isinstance(nx, dict):\n                total += 1\n                if nx.get(\\\"significant\\\", False):\n                    naive_sig += 1\n    \n    d = os.path.dirname(os.path.dirname(fp))\n    print(d, naive_sig, total, sep=\\\"|\\\")\n\"'",
    "description": "Extract naive xcorr significant count from forward pairs",
    "timeout": "15000"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-19T03:05:25.815974+00:00_

Warning: Permanently added '[connect.westd.seetacloud.com]:19828' (ED25519) to the list of known hosts.
results/alpha_sweep/a000_s42|8|8
results/alpha_sweep/a000_s43|7|8
results/alpha_sweep/a000_s44|8|8
results/alpha_sweep/a025_s43|8|8
results/alpha_sweep/a025_s44|8|8
results/alpha_sweep/a050_s42|8|8
results/alpha_sweep/a050_s43|8|8
results/alpha_sweep/a050_s44|8|8
results/alpha_sweep/a060_s42_bf16|8|8
results/alpha_sweep/a075_s42|8|8
results/alpha_sweep/a075_s43|8|8
results/alpha_sweep/a075_s44|8|8
results/generalize/gpt2m_wiki_a100_s42|8|8
results/generalize/opt1b_wiki_a100_s42|8|8
results/generalize/pythia14b_wiki_a100_s42|7|8
results/generalize/pythia14b_wiki_a100_s43|8|8
results/generalize/pythia1b_c4_a100_s42|8|8
results/generalize/pythia1b_c4_a100_s43|8|8
results/generalize/pythia410m_wiki_a100_s42|8|8

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-19T03:05:25.816108+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ssh westd-19828 'cd /root/autodl-tmp/distrib_canary_collapse && find results/ -name \"mmct*.json\" 2>/dev/null | sort && echo \"---\" && ls results/mvp/ 2>/dev/null && echo \"---\" && ls results/intervention/ 2>/dev/null && echo \"---\" && ls results/scale_check/ 2>/dev/null && echo \"---\" && ls results/alpha_sweep/c4_a050_s42_bf16/ 2>/dev/null || ls results/c4/ 2>/dev/null || echo \"no c4 dir\"'",
  "description": "Find MMCT files and other experiment dirs",
  "timeout": "15000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "tool_args": {
    "command": "ssh westd-19828 'cd /root/autodl-tmp/distrib_canary_collapse && find results/ -name \"mmct*.json\" 2>/dev/null | sort && echo \"---\" && ls results/mvp/ 2>/dev/null && echo \"---\" && ls results/intervention/ 2>/dev/null && echo \"---\" && ls results/scale_check/ 2>/dev/null && echo \"---\" && ls results/alpha_sweep/c4_a050_s42_bf16/ 2>/dev/null || ls results/c4/ 2>/dev/null || echo \"no c4 dir\"'",
    "description": "Find MMCT files and other experiment dirs",
    "timeout": "15000"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-19T03:05:25.816223+00:00_

Warning: Permanently added '[connect.westd.seetacloud.com]:19828' (ED25519) to the list of known hosts.
results/alpha_sweep/a060_s42_bf16/analysis/mmct_results.json
---
no c4 dir

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-19T03:05:25.816356+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ssh westd-19828 'cd /root/autodl-tmp/distrib_canary_collapse && ls results/ && echo \"---\" && ls results/mvp/ 2>/dev/null || echo \"no mvp dir\" && echo \"---\" && ls results/intervention/ 2>/dev/null || echo \"no intervention dir\" && echo \"---\" && ls results/scale_check/ 2>/dev/null || echo \"no scale_check dir\"'",
  "description": "List result directory structure",
  "timeout": "15000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "tool_args": {
    "command": "ssh westd-19828 'cd /root/autodl-tmp/distrib_canary_collapse && ls results/ && echo \"---\" && ls results/mvp/ 2>/dev/null || echo \"no mvp dir\" && echo \"---\" && ls results/intervention/ 2>/dev/null || echo \"no intervention dir\" && echo \"---\" && ls results/scale_check/ 2>/dev/null || echo \"no scale_check dir\"'",
    "description": "List result directory structure",
    "timeout": "15000"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-19T03:05:25.816475+00:00_

Warning: Permanently added '[connect.westd.seetacloud.com]:19828' (ED25519) to the list of known hosts.
alpha_sweep
alpha_sweep_analysis
analysis
bootstrap_ty_dryrun.json
bootstrap_ty_results.json
detrending
dose_response_drift.csv
gen_wiki_gpt2m_a100_s43
generalize
intervention
method_ablation_phase2_panel.json
method_ablation_phase2_report.md
method_ablation_phase3_panel.json
method_ablation_phase3_report.md
perm_granger_power_bootstrap.json
rebuttal
scale_check
shapley_values.json
---
no mvp dir
---
predictive_te_s42
reactive_d1_s42
---
pythia14b_a050_s42

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-19T03:05:25.816630+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ssh westd-19828 'cd /root/autodl-tmp/distrib_canary_collapse && echo \"=== intervention/predictive ===\" && ls results/intervention/predictive_te_s42/ && echo \"---\" && echo \"=== intervention/reactive ===\" && ls results/intervention/reactive_d1_s42/ && echo \"---\" && echo \"=== scale_check ===\" && ls results/scale_check/pythia14b_a050_s42/ && echo \"---\" && echo \"=== gen_wiki_gpt2m_a100_s43 ===\" && ls results/gen_wiki_gpt2m_a100_s43/ 2>/dev/null || echo \"no dir\"'",
  "description": "Check intervention, scale, gpt2m dirs",
  "timeout": "15000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "tool_args": {
    "command": "ssh westd-19828 'cd /root/autodl-tmp/distrib_canary_collapse && echo \"=== intervention/predictive ===\" && ls results/intervention/predictive_te_s42/ && echo \"---\" && echo \"=== intervention/reactive ===\" && ls results/intervention/reactive_d1_s42/ && echo \"---\" && echo \"=== scale_check ===\" && ls results/scale_check/pythia14b_a050_s42/ && echo \"---\" && echo \"=== gen_wiki_gpt2m_a100_s43 ===\" && ls results/gen_wiki_gpt2m_a100_s43/ 2>/dev/null || echo \"no dir\"'",
    "description": "Check intervention, scale, gpt2m dirs",
    "timeout": "15000"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-19T03:05:25.816771+00:00_

Warning: Permanently added '[connect.westd.seetacloud.com]:19828' (ED25519) to the list of known hosts.
=== intervention/predictive ===
EXIT_CODE
all_metrics.json
config.json
gen_0
gen_1
gen_10
gen_2
gen_3
gen_4
gen_5
gen_6
gen_7
gen_8
gen_9
---
=== intervention/reactive ===
EXIT_CODE
all_metrics.json
config.json
gen_0
gen_1
gen_10
gen_2
gen_3
gen_4
gen_5
gen_6
gen_7
gen_8
gen_9
---
=== scale_check ===
EXIT_CODE
all_metrics.json
config.json
gen_0
gen_1
gen_10
gen_2
gen_3
gen_4
gen_5
gen_6
gen_7
gen_8
gen_9
---
=== gen_wiki_gpt2m_a100_s43 ===
config.json
gen_0
gen_1
gen_2

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-19T03:05:25.816940+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ssh westd-19828 'cd /root/autodl-tmp/distrib_canary_collapse && cat results/alpha_sweep/pooled_panel_results.json 2>/dev/null | python3 -c \"\nimport json, sys\nm = json.load(sys.stdin)\nprint(json.dumps(m, indent=2)[:3000])\n\"'",
  "description": "Read pooled panel results",
  "timeout": "15000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "tool_args": {
    "command": "ssh westd-19828 'cd /root/autodl-tmp/distrib_canary_collapse && cat results/alpha_sweep/pooled_panel_results.json 2>/dev/null | python3 -c \"\nimport json, sys\nm = json.load(sys.stdin)\nprint(json.dumps(m, indent=2)[:3000])\n\"'",
    "description": "Read pooled panel results",
    "timeout": "15000"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-19T03:05:25.817093+00:00_

Warning: Permanently added '[connect.westd.seetacloud.com]:19828' (ED25519) to the list of known hosts.
{
  "meta": {
    "timestamp": "2026-05-15T12:34:44.745746",
    "alphas": [
      0.0,
      0.25
    ],
    "n_alphas": 2,
    "n_runs": 2,
    "n_obs_per_pair": 18,
    "canary_metrics": [
      "token_entropy",
      "ece"
    ],
    "diversity_metrics": [
      "distinct_1",
      "distinct_2",
      "distinct_3"
    ],
    "n_permutations": 500,
    "warnings": [
      "Only 2 alpha points \u2014 panel regression and monotonicity tests are underpowered. Results are structural validation only."
    ]
  },
  "panel_regression": [
    {
      "canary": "token_entropy",
      "downstream": "distinct_1",
      "n_obs": 18,
      "n_alphas": 2,
      "r_squared": 0.7256,
      "r_squared_adj": 0.6668,
      "f_stat": 98.8383,
      "f_pvalue": 0.0,
      "coefficients": {
        "const": {
          "coef": -0.000763,
          "se": 0.000359,
          "t": -2.1253,
          "p": 0.033562,
          "significant": true
        },
        "lag1_d_canary": {
          "coef": 0.031205,
          "se": 0.001986,
          "t": 15.7102,
          "p": 0.0,
          "significant": true
        },
        "alpha": {
          "coef": -0.011816,
          "se": 0.005199,
          "t": -2.2727,
          "p": 0.023047,
          "significant": true
        },
        "interaction": {
          "coef": 0.066553,
          "se": 0.036868,
          "t": 1.8052,
          "p": 0.071047,
          "significant": false
        }
      },
      "warning": "Only 2 alpha points \u2014 panel regression is underpowered. Interaction term estimates unreliable. Wait for >=3 alpha points.",
      "interaction_p_fdr": 0.420056,
      "interaction_sig_fdr": false
    },
    {
      "canary": "token_entropy",
      "downstream": "distinct_2",
      "n_obs": 18,
      "n_alphas": 2,
      "r_squared": 0.6135,
      "r_squared_adj": 0.5307,
      "f_stat": 30.8004,
      "f_pvalue": 2
…[truncated 1105 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-19T03:05:25.817239+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ssh westd-19828 'cd /root/autodl-tmp/distrib_canary_collapse && cat results/alpha_sweep/analysis_summary.json 2>/dev/null | python3 -c \"\nimport json, sys\nm = json.load(sys.stdin)\nprint(json.dumps(m, indent=2)[:3000])\n\" 2>&1 | head -80'",
  "description": "Read analysis summary",
  "timeout": "15000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "tool_args": {
    "command": "ssh westd-19828 'cd /root/autodl-tmp/distrib_canary_collapse && cat results/alpha_sweep/analysis_summary.json 2>/dev/null | python3 -c \"\nimport json, sys\nm = json.load(sys.stdin)\nprint(json.dumps(m, indent=2)[:3000])\n\" 2>&1 | head -80'",
    "description": "Read analysis summary",
    "timeout": "15000"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-19T03:05:25.817401+00:00_

Warning: Permanently added '[connect.westd.seetacloud.com]:19828' (ED25519) to the list of known hosts.
{
  "meta": {
    "test": "toda_yamamoto",
    "alpha_stat": 0.05,
    "min_gens": 5,
    "valid_pairs": [
      [
        "ece",
        "distinct_1"
      ],
      [
        "token_entropy",
        "distinct_1"
      ],
      [
        "token_entropy",
        "distinct_2"
      ],
      [
        "token_entropy",
        "distinct_3"
      ],
      [
        "token_entropy",
        "perplexity"
      ]
    ]
  },
  "runs": {
    "a000_s42": {
      "alpha": 0.0,
      "seed": 42,
      "n_gens": 5,
      "analyzed": true
    },
    "a025_s42": {
      "alpha": 0.25,
      "seed": 42,
      "n_gens": 0,
      "analyzed": false
    }
  },
  "by_alpha": {
    "0.00": {
      "ece_to_distinct_1": {
        "n_seeds": 1,
        "n_significant": 0,
        "sig_rate": 0.0,
        "p_median": null,
        "p_mean": null,
        "F_mean": null,
        "F_std": null,
        "per_seed": [
          {
            "p": 1,
            "d_max": 1,
            "k": 2,
            "wald_F": null,
            "p_value": null,
            "significant": false,
            "note": "no residual df (T_eff=3, params=5)",
            "d_canary": 1,
            "d_downstream": 1
          }
        ]
      },
      "token_entropy_to_distinct_1": {
        "n_seeds": 1,
        "n_significant": 0,
        "sig_rate": 0.0,
        "p_median": null,
        "p_mean": null,
        "F_mean": null,
        "F_std": null,
        "per_seed": [
          {
            "p": 1,
            "d_max": 1,
            "k": 2,
            "wald_F": null,

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-19T03:05:25.817586+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ssh westd-19828 'cd /root/autodl-tmp/distrib_canary_collapse && for d in results/intervention/predictive_te_s42 results/intervention/reactive_d1_s42 results/scale_check/pythia14b_a050_s42; do echo \"=== $d ===\"; python3 -c \"\nimport json\nwith open(\\\"$d/config.json\\\") as f:\n    c = json.load(f)\nprint(json.dumps(c, indent=2)[:500])\n\"; done'",
  "description": "Check intervention and scale configs",
  "timeout": "15000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "tool_args": {
    "command": "ssh westd-19828 'cd /root/autodl-tmp/distrib_canary_collapse && for d in results/intervention/predictive_te_s42 results/intervention/reactive_d1_s42 results/scale_check/pythia14b_a050_s42; do echo \"=== $d ===\"; python3 -c \"\nimport json\nwith open(\\\"$d/config.json\\\") as f:\n    c = json.load(f)\nprint(json.dumps(c, indent=2)[:500])\n\"; done'",
    "description": "Check intervention and scale configs",
    "timeout": "15000"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-19T03:05:25.817729+00:00_

Warning: Permanently added '[connect.westd.seetacloud.com]:19828' (ED25519) to the list of known hosts.
=== results/intervention/predictive_te_s42 ===
{
  "model_name": "EleutherAI/pythia-410m",
  "data_dir": "data/wikitext103_5k",
  "dataset": "wikitext-103-v1",
  "synthetic_ratio": 1.0,
  "num_generations": 10,
  "steps_per_gen": 5000,
  "output_dir": "results/intervention/predictive_te_s42",
  "seed": 42,
  "batch_size": 4,
  "max_length": 512,
  "lr": 5e-05,
  "gen_max_new_tokens": 256,
  "gen_batch_size": 16,
  "top_p": 0.95,
  "accumulate": false,
  "start_gen": 0,
  "gradient_checkpointing": false,
  "optim": "adamw_torch",
  "intervent
=== results/intervention/reactive_d1_s42 ===
{
  "model_name": "EleutherAI/pythia-410m",
  "data_dir": "data/wikitext103_5k",
  "dataset": "wikitext-103-v1",
  "synthetic_ratio": 1.0,
  "num_generations": 10,
  "steps_per_gen": 5000,
  "output_dir": "results/intervention/reactive_d1_s42",
  "seed": 42,
  "batch_size": 4,
  "max_length": 512,
  "lr": 5e-05,
  "gen_max_new_tokens": 256,
  "gen_batch_size": 16,
  "top_p": 0.95,
  "accumulate": false,
  "start_gen": 0,
  "gradient_checkpointing": false,
  "optim": "adamw_torch",
  "interventio
=== results/scale_check/pythia14b_a050_s42 ===
{
  "model_name": "EleutherAI/pythia-1.4b",
  "data_dir": "data/wikitext103_5k",
  "dataset": "wikitext-103-v1",
  "synthetic_ratio": 0.5,
  "num_generations": 10,
  "steps_per_gen": 5000,
  "output_dir": "results/scale_check/pythia14b_a050_s42",
  "seed": 42,
  "batch_size": 4,
  "max_length": 512,
  "lr": 5e-05,
  "gen_max_new_tokens": 256,
  "gen_batch_size": 16,
  "top_p": 0.95,
  "accumulate": false,
  "start_gen": 0,
  "gradient_checkpointing": false,
  "bf16": false,
  "optim": "adamw_tor

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-19T03:05:25.817874+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ssh westd-19828 'cd /root/autodl-tmp/distrib_canary_collapse && python3 -c \"\nimport json\n\n# Check alpha_sweep a025_s42 config\nwith open(\\\"results/alpha_sweep/a050_s42/config.json\\\") as f:\n    c = json.load(f)\nprint(\\\"a050_s42 bf16:\\\", c.get(\\\"bf16\\\", \\\"not set\\\"), \\\"torch_dtype:\\\", c.get(\\\"torch_dtype\\\", \\\"not set\\\"))\n\n# Check a010_s42 config  \ntry:\n    with open(\\\"results/alpha_sweep/a010_s42/config.json\\\") as f:\n        c = json.load(f)\n    print(\\\"a010_s42 bf16:\\\", c.get(\\\"bf16\\\", \\\"not set\\\"), \\\"torch_dtype:\\\", c.get(\\\"torch_dtype\\\", \\\"not set\\\"), \\\"alpha:\\\", c.get(\\\"synthetic_ratio\\\", \\\"?\\\"))\nexcept: \n    print(\\\"a010_s42 not found\\\")\n    \n# Check a025_s42\nimport os\nfor p in [\\\"results/alpha_sweep/a025_s42\\\", \\\"results/alpha_sweep/a025_s42_v3\\\"]:\n    if os.path.exists(p):\n        with open(os.path.join(p, \\\"config.json\\\")) as f:\n            c = json.load(f)\n        print(f\\\"{p} bf16:\\\", c.get(\\\"bf16\\\", \\\"not set\\\"))\n\n# Check c4 experiments\nimport glob\nc4_dirs = glob.glob(\\\"results/alpha_sweep/c4*\\\") + glob.glob(\\\"results/**/c4*\\\", recursive=True)\nprint(\\\"C4 dirs:\\\", c4_dirs)\n\n# Check bf16 experiments location\nbf16_dirs = glob.glob(\\\"results/**/*bf16*\\\", recursive=True)\nprint(\\\"bf16 dirs:\\\", [d for d in bf16_dirs if os.path.isdir(d)])\n\n# Check gen_gpt2m dirs\ngpt2m_dirs = glob.glob(\\\"results/**/gpt2m*\\\", recursive=True) + glob.glob(\\\"results/gen_*\\\", recursive=True)\nprint(\\\"GPT2m dirs:\\\", [d for d in gpt2m_dirs if os.path.isdir(d)])\n\"'",
  "description": "Check configs for precision and find experiment dirs",
  "timeout": "15000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "tool_args": {
    "command": "ssh westd-19828 'cd /root/autodl-tmp/distrib_canary_collapse && python3 -c \"\nimport json\n\n# Check alpha_sweep a025_s42 config\nwith open(\\\"results/alpha_sweep/a050_s42/config.json\\\") as f:\n    c = json.load(f)\nprint(\\\"a050_s42 bf16:\\\", c.get(\\\"bf16\\\", \\\"not set\\\"), \\\"torch_dtype:\\\", c.get(\\\"torch_dtype\\\", \\\"not set\\\"))\n\n# Check a010_s42 config  \ntry:\n    with open(\\\"results/alpha_sweep/a010_s42/config.json\\\") as f:\n        c = json.load(f)\n    print(\\\"a010_s42 bf16:\\\", c.get(\\\"bf16\\\", \\\"not set\\\"), \\\"torch_dtype:\\\", c.get(\\\"torch_dtype\\\", \\\"not set\\\"), \\\"alpha:\\\", c.get(\\\"synthetic_ratio\\\", \\\"?\\\"))\nexcept: \n    print(\\\"a010_s42 not found\\\")\n    \n# Check a025_s42\nimport os\nfor p in [\\\"results/alpha_sweep/a025_s42\\\", \\\"results/alpha_sweep/a025_s42_v3\\\"]:\n    if os.path.exists(p):\n        with open(os.path.join(p, \\\"config.json\\\")) as f:\n            c = json.load(f)\n        print(f\\\"{p} bf16:\\\", c.get(\\\"bf16\\\", \\\"not set\\\"))\n\n# Check c4 experiments\nimport glob\nc4_dirs = glob.glob(\\\"results/alpha_sweep/c4*\\\") + glob.glob(\\\"results/**/c4*\\\", recursive=True)\nprint(\\\"C4 dirs:\\\", c4_dirs)\n\n# Check bf16 experiments location\nbf16_dirs = glob.glob(\\\"results/**/*bf16*\\\", recursive=True)\nprint(\\\"bf16 dirs:\\\", [d for d in bf16_dirs if os.path.isdir(d)])\n\n# Check gen_gpt2m dirs\ngpt2m_dirs = glob.glob(\\\"results/**/gpt2m*\\\", recursive=True) + glob.glob(\\\"results/gen_*\\\", recursive=True)\nprint(\\\"GPT2m dirs:\\\", [d for d in gpt2m_dirs if os.path.isdir(d)])\n\"'",
    "description": "Check configs for precision and find experiment dirs",
    "timeout": "15000"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-19T03:05:25.818005+00:00_

Warning: Permanently added '[connect.westd.seetacloud.com]:19828' (ED25519) to the list of known hosts.
a050_s42 bf16: not set torch_dtype: not set
a010_s42 bf16: not set torch_dtype: not set alpha: 0.1
C4 dirs: ['results/generalize/pythia1b_c4_a100_s42/analysis/c4_8pair_6method_analysis.json']
bf16 dirs: ['results/alpha_sweep/a060_s42_bf16']
GPT2m dirs: ['results/generalize/gpt2m_wiki_a100_s42', 'results/gen_wiki_gpt2m_a100_s43']

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-19T03:05:25.818126+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ssh westd-19828 'cd /root/autodl-tmp/distrib_canary_collapse && python3 -c \"\nimport json\n\n# Check gen_wiki_gpt2m_a025_s42 location\nimport os, glob\nfor pattern in [\\\"results/**/gpt2m*a025*\\\", \\\"results/**/a025*gpt2m*\\\", \\\"results/gen_wiki*a025*\\\"]:\n    matches = glob.glob(pattern, recursive=True)\n    if matches: print(f\\\"{pattern}: {matches}\\\")\n\n# Check gen_gpt2m_a100_s43_bf16 location\nfor pattern in [\\\"results/**/gpt2m*s43*\\\", \\\"results/**/s43*gpt2m*\\\", \\\"results/gen_*s43*\\\"]:\n    matches = glob.glob(pattern, recursive=True)\n    if matches: print(f\\\"{pattern}: {matches}\\\")\n\n# Check interv_pred_s43_bf16 / interv_react_s43_bf16\nfor pattern in [\\\"results/intervention/*s43*\\\", \\\"results/interv*s43*\\\"]:\n    matches = glob.glob(pattern, recursive=True)\n    if matches: print(f\\\"{pattern}: {matches}\\\")\n\n# Check alpha_sweep c4\nfor pattern in [\\\"results/alpha_sweep/*c4*\\\", \\\"results/c4*\\\"]:\n    matches = glob.glob(pattern, recursive=True)\n    if matches: print(f\\\"{pattern}: {matches}\\\")\n\"'",
  "description": "Find remaining experiment directories",
  "timeout": "15000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "tool_args": {
    "command": "ssh westd-19828 'cd /root/autodl-tmp/distrib_canary_collapse && python3 -c \"\nimport json\n\n# Check gen_wiki_gpt2m_a025_s42 location\nimport os, glob\nfor pattern in [\\\"results/**/gpt2m*a025*\\\", \\\"results/**/a025*gpt2m*\\\", \\\"results/gen_wiki*a025*\\\"]:\n    matches = glob.glob(pattern, recursive=True)\n    if matches: print(f\\\"{pattern}: {matches}\\\")\n\n# Check gen_gpt2m_a100_s43_bf16 location\nfor pattern in [\\\"results/**/gpt2m*s43*\\\", \\\"results/**/s43*gpt2m*\\\", \\\"results/gen_*s43*\\\"]:\n    matches = glob.glob(pattern, recursive=True)\n    if matches: print(f\\\"{pattern}: {matches}\\\")\n\n# Check interv_pred_s43_bf16 / interv_react_s43_bf16\nfor pattern in [\\\"results/intervention/*s43*\\\", \\\"results/interv*s43*\\\"]:\n    matches = glob.glob(pattern, recursive=True)\n    if matches: print(f\\\"{pattern}: {matches}\\\")\n\n# Check alpha_sweep c4\nfor pattern in [\\\"results/alpha_sweep/*c4*\\\", \\\"results/c4*\\\"]:\n    matches = glob.glob(pattern, recursive=True)\n    if matches: print(f\\\"{pattern}: {matches}\\\")\n\"'",
    "description": "Find remaining experiment directories",
    "timeout": "15000"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-19T03:05:25.818266+00:00_

Warning: Permanently added '[connect.westd.seetacloud.com]:19828' (ED25519) to the list of known hosts.
results/gen_*s43*: ['results/gen_wiki_gpt2m_a100_s43']

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-19T03:05:25.818432+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'RUNNING'}",
  "fields": "['exp_id', 'status', 'hypothesis', 'spec', 'notes']",
  "limit": "0",
  "project": "distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'RUNNING'}",
    "fields": "['exp_id', 'status', 'hypothesis', 'spec', 'notes']",
    "limit": "0",
    "project": "distrib_canary_collapse"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-19T03:05:25.818674+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"qwen35_08b_wiki_a100_s42_v2\": {\"status\": \"RUNNING\", \"hypothesis\": \"D080 fix: Qwen3.5-0.8B fp32 cross-architecture validation. Resubmit with explicit .to(dtype=float32) cast after from_pretrained, because transformers 5.8.1 ignores dtype param for Qwen3.5 (loads bfloat16 from safetensors regardless).\", \"spec\": {\"command\": \"iterative_train.py --model_name Qwen3.5-0.8B-Base --seed 42 --synthetic_ratio 1.0\", \"server\": \"westd-17855\", \"gpu\": [\"cuda:1\"], \"pid\": \"74455\", \"log_path\": \"~/runs/distrib_canary_collapse/qwen35_08b_wiki_a100_s42_v2.log\", \"submitted_at\": \"2026-05-19T00:29:15.328Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/wikitext103_5k\", \"data_count\": 5000, \"model_name\": \"Qwen3.5-0.8B-Base\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models/Qwen3.5-0.8B-Base/\", \"eval_data\": \"data/wikitext103_5k\"}}, \"smollm3_3b_wiki_a100_s42_v3\": {\"status\": \"RUNNING\", \"hypothesis\": \"D080 fix: SmolLM3-3B fp32 cross-architecture validation. Resubmit with torch_dtype=float32 to satisfy D079 fp32 requirement.\", \"spec\": {\"command\": \"iterative_train.py --model_name SmolLM3-3B-Base --seed 42 --synthetic_ratio 1.0\", \"server\": \"westd-19828\", \"gpu\": [\"cuda:1\"], \"pid\": \"408261\", \"log_path\": \"~/runs/distrib_canary_collapse/smollm3_3b_wiki_a100_s42_v3.log\", \"submitted_at\": \"2026-05-19T00:24:32.263Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/wikitext103_5k\", \"data_count\": 5000, \"model_name\": \"SmolLM3-3B-Base\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models/SmolLM3-3B-Base/\", \"eval_data\": \"data/wikitext103_5k\"}}, \"interv_pred_a075_s42_fp32_v4\": {\"status\": \"RUNNING\", \"hypothesis\": \"D080 fix: predictive intervention α=0.75 fp32 (torch_dtype=float32). Resubmit with dty
…[truncated 5607 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-19T03:05:25.818847+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/tmp/success_exps.json') as f:\n    success = json.load(f)\n\n# Check intervention experiments for alpha\nfor eid in ['intervention_predictive_s42', 'intervention_reactive_s42', 'interv_pred_s43_bf16', 'interv_react_s43_bf16']:\n    e = success.get(eid, {})\n    spec = e.get('spec', {})\n    cmd = spec.get('command', '') if isinstance(spec, dict) else ''\n    hyp = e.get('hypothesis', '')\n    notes = e.get('notes', '') or ''\n    \n    # Find synthetic_ratio in command\n    import re\n    alpha_match = re.search(r'synthetic_ratio[= ]+([0-9.]+)', cmd)\n    alpha = alpha_match.group(1) if alpha_match else '?'\n    \n    print(f'{eid}: alpha={alpha}')\n    print(f'  hyp: {hyp[:200]}')\n    print(f'  notes: {notes[:200]}')\n    print()\n\n# Check mvp experiments\nfor eid in ['mvp_v4_rep42']:\n    e = success.get(eid, {})\n    spec = e.get('spec', {})\n    cmd = spec.get('command', '') if isinstance(spec, dict) else ''\n    hyp = e.get('hypothesis', '')\n    print(f'{eid}: cmd={cmd[:200]}')\n    print(f'  hyp: {hyp[:200]}')\n    print()\n\n# Check gen_wiki_gpt2m duplicates\nfor eid in ['gen_wiki_gpt2m_a100_s42_v3', 'gen_wiki_gpt2m_a100_s42_v4', 'gen_wiki_gpt2m_a025_s42']:\n    e = success.get(eid, {})\n    hyp = e.get('hypothesis', '')[:200]\n    notes = (e.get('notes', '') or '')[:200]\n    print(f'{eid}: hyp={hyp}')\n    print(f'  notes={notes}')\n    print()\n    \n# Check method_ablation and analysis experiments\nfor eid in ['method_ablation_phase1','method_ablation_phase2','method_ablation_phase3','conditional_granger_d061','plan_009_bootstrap_ty']:\n    e = success.get(eid, {})\n    hyp = e.get('hypothesis', '')[:200]\n    print(f'{eid}: {hyp}')\nPYEOF\n",
  "description": "Get alpha/details for remaining experiments",
  "timeout": "15000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/tmp/success_exps.json') as f:\n    success = json.load(f)\n\n# Check intervention experiments for alpha\nfor eid in ['intervention_predictive_s42', 'intervention_reactive_s42', 'interv_pred_s43_bf16', 'interv_react_s43_bf16']:\n    e = success.get(eid, {})\n    spec = e.get('spec', {})\n    cmd = spec.get('command', '') if isinstance(spec, dict) else ''\n    hyp = e.get('hypothesis', '')\n    notes = e.get('notes', '') or ''\n    \n    # Find synthetic_ratio in command\n    import re\n    alpha_match = re.search(r'synthetic_ratio[= ]+([0-9.]+)', cmd)\n    alpha = alpha_match.group(1) if alpha_match else '?'\n    \n    print(f'{eid}: alpha={alpha}')\n    print(f'  hyp: {hyp[:200]}')\n    print(f'  notes: {notes[:200]}')\n    print()\n\n# Check mvp experiments\nfor eid in ['mvp_v4_rep42']:\n    e = success.get(eid, {})\n    spec = e.get('spec', {})\n    cmd = spec.get('command', '') if isinstance(spec, dict) else ''\n    hyp = e.get('hypothesis', '')\n    print(f'{eid}: cmd={cmd[:200]}')\n    print(f'  hyp: {hyp[:200]}')\n    print()\n\n# Check gen_wiki_gpt2m duplicates\nfor eid in ['gen_wiki_gpt2m_a100_s42_v3', 'gen_wiki_gpt2m_a100_s42_v4', 'gen_wiki_gpt2m_a025_s42']:\n    e = success.get(eid, {})\n    hyp = e.get('hypothesis', '')[:200]\n    notes = (e.get('notes', '') or '')[:200]\n    print(f'{eid}: hyp={hyp}')\n    print(f'  notes={notes}')\n    print()\n    \n# Check method_ablation and analysis experiments\nfor eid in ['method_ablation_phase1','method_ablation_phase2','method_ablation_phase3','conditional_granger_d061','plan_009_bootstrap_ty']:\n    e = success.get(eid, {})\n    hyp = e.get('hypothesis', '')[:200]\n    print(f'{eid}: {hyp}')\nPYEOF\n",
    "description": "Get alpha/details for remaining experiments",
    "timeout": "15000"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-19T03:05:25.818997+00:00_

intervention_predictive_s42: alpha=1.0
  hyp: Predictive intervention: monitoring token_entropy drop >15% as early-warning trigger, switching α from 1.0 to 0.0 at trigger generation. Tests whether canary-triggered intervention halts collapse earl
  notes: 

intervention_reactive_s42: alpha=1.0
  hyp: Reactive intervention baseline: monitoring distinct_1 drop >10% as trigger, switching α from 1.0 to 0.0 at trigger generation. Tests whether downstream-triggered intervention (without canary) can halt
  notes: 

interv_pred_s43_bf16: alpha=1.0
  hyp: Intervention predictive multi-seed s43 (bf16): Pythia-410M WikiText α=1.0, token_entropy >15% drop trigger, switch to α=0.0. Validates s42 result (trigger Gen 1, recovery Gen 2) is reproducible across
  notes: 

interv_react_s43_bf16: alpha=1.0
  hyp: Intervention reactive multi-seed s43: Pythia-410M WikiText α=1.0, distinct_1 >10% drop trigger, switch to α=0.0. Validates s42 reactive result.
  notes: 

mvp_v4_rep42: cmd=bash -c "cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && export REQUESTS_CA_BUNDL
  hyp: α=1.0 full replacement baseline: 完全合成污染下 canary→downstream 因果领先性在多 seeds 可复现，建立 confirmatory regime 证据基础

gen_wiki_gpt2m_a100_s42_v3: hyp=
  notes=

gen_wiki_gpt2m_a100_s42_v4: hyp=GPT-2-medium 重跑以产出可审计 artifact：用统一参数 (n_perm=5000, xcorr_lag=5) 验证跨架构泛化，填充 Table 7 GPT-2m 行
  notes=

gen_wiki_gpt2m_a025_s42: hyp=跨架构验证: GPT-2-medium (355M) 在 α=0.25 下展示与 Pythia-410M 相同的 regime-dependent 模式（diversity collapse 显著但 causal signal sub-threshold），确认 detectability boundary 非模型特异性
  notes=

method_ablation_phase1: 
method_ablation_phase2: 
method_ablation_phase3: Phase 3 method ablation: 扩展 7 个 α 点（0.00-1.00）的 5 种检测方法 significance rate 矩阵，验证 permG/TY 在不同 contamination regime 下的灵敏度。
conditional_granger_d061: Conditional Granger analysis: 控制 ECE 后测 token_entropy→diversity，控制 token_entropy 后测 ECE→diversity。验证两个 canary
…[truncated 33 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-19T03:05:25.819198+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ssh westd-19828 'cd /root/autodl-tmp/distrib_canary_collapse && python3 -c \"\nimport json, glob\n\n# Get the full 5method data for generalize experiments too\nfiles = sorted(glob.glob(\\\"results/**/5method_leadlag.json\\\", recursive=True))\nfor fp in files:\n    with open(fp) as f:\n        m = json.load(f)\n    s = m.get(\\\"summary\\\", {})\n    pairs = m.get(\\\"pairs\\\", [])\n    if isinstance(pairs, dict):\n        items = list(pairs.values())\n    else:\n        items = pairs\n    \n    naive_sig = sum(1 for pv in items if isinstance(pv, dict) and isinstance(pv.get(\\\"forward\\\",pv), dict) and pv.get(\\\"forward\\\",pv).get(\\\"naive_xcorr\\\",{}).get(\\\"significant\\\", False))\n    total = sum(1 for pv in items if isinstance(pv, dict))\n    \n    import os\n    d = os.path.dirname(os.path.dirname(fp))\n    print(f\\\"{d}|{naive_sig}/{total}|{s.get(\\\"diff_xcorr_fdr_forward_sig\\\",\\\"?\\\")}/8|{s.get(\\\"threshold_forward_sig\\\",\\\"?\\\")}/8|{s.get(\\\"perm_granger_fdr_forward_sig\\\",\\\"?\\\")}/8|{s.get(\\\"perm_granger_fdr_reverse_sig\\\",\\\"?\\\")}/8|{s.get(\\\"ty_forward_sig\\\",\\\"?\\\")}/8|{s.get(\\\"robust_pairs\\\",\\\"?\\\")}/8\\\")\n\"'",
  "description": "Final extraction of all 5method data",
  "timeout": "15000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "tool_args": {
    "command": "ssh westd-19828 'cd /root/autodl-tmp/distrib_canary_collapse && python3 -c \"\nimport json, glob\n\n# Get the full 5method data for generalize experiments too\nfiles = sorted(glob.glob(\\\"results/**/5method_leadlag.json\\\", recursive=True))\nfor fp in files:\n    with open(fp) as f:\n        m = json.load(f)\n    s = m.get(\\\"summary\\\", {})\n    pairs = m.get(\\\"pairs\\\", [])\n    if isinstance(pairs, dict):\n        items = list(pairs.values())\n    else:\n        items = pairs\n    \n    naive_sig = sum(1 for pv in items if isinstance(pv, dict) and isinstance(pv.get(\\\"forward\\\",pv), dict) and pv.get(\\\"forward\\\",pv).get(\\\"naive_xcorr\\\",{}).get(\\\"significant\\\", False))\n    total = sum(1 for pv in items if isinstance(pv, dict))\n    \n    import os\n    d = os.path.dirname(os.path.dirname(fp))\n    print(f\\\"{d}|{naive_sig}/{total}|{s.get(\\\"diff_xcorr_fdr_forward_sig\\\",\\\"?\\\")}/8|{s.get(\\\"threshold_forward_sig\\\",\\\"?\\\")}/8|{s.get(\\\"perm_granger_fdr_forward_sig\\\",\\\"?\\\")}/8|{s.get(\\\"perm_granger_fdr_reverse_sig\\\",\\\"?\\\")}/8|{s.get(\\\"ty_forward_sig\\\",\\\"?\\\")}/8|{s.get(\\\"robust_pairs\\\",\\\"?\\\")}/8\\\")\n\"'",
    "description": "Final extraction of all 5method data",
    "timeout": "15000"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-19T03:05:25.819360+00:00_

Exit code 1
Warning: Permanently added '[connect.westd.seetacloud.com]:19828' (ED25519) to the list of known hosts.
  File "&lt;string>", line 21
    print(f"{d}|{naive_sig}/{total}|{s.get("diff_xcorr_fdr_forward_sig","?")}/8|{s.get("threshold_forward_sig","?")}/8|{s.get("perm_granger_fdr_forward_sig","?")}/8|{s.get("perm_granger_fdr_reverse_sig","?")}/8|{s.get("ty_forward_sig","?")}/8|{s.get("robust_pairs","?")}/8")
                                            ^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: f-string: unmatched '('

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-19T03:05:25.819490+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ssh westd-19828 'cd /root/autodl-tmp/distrib_canary_collapse && python3 -c \"\nimport json, glob, os\n\nfiles = sorted(glob.glob(\\\"results/**/5method_leadlag.json\\\", recursive=True))\nfor fp in files:\n    with open(fp) as f:\n        m = json.load(f)\n    s = m.get(\\\"summary\\\", {})\n    pairs = m.get(\\\"pairs\\\", [])\n    if isinstance(pairs, dict):\n        items = list(pairs.values())\n    else:\n        items = pairs\n    \n    naive_sig = 0\n    total = 0\n    for pv in items:\n        if not isinstance(pv, dict):\n            continue\n        fwd = pv.get(\\\"forward\\\", pv)\n        if isinstance(fwd, dict):\n            nx = fwd.get(\\\"naive_xcorr\\\", {})\n            if isinstance(nx, dict):\n                total += 1\n                if nx.get(\\\"significant\\\", False):\n                    naive_sig += 1\n    \n    d = os.path.dirname(os.path.dirname(fp))\n    diff = s.get(\\\"diff_xcorr_fdr_forward_sig\\\", \\\"?\\\")\n    thresh = s.get(\\\"threshold_forward_sig\\\", \\\"?\\\")\n    pg_f = s.get(\\\"perm_granger_fdr_forward_sig\\\", \\\"?\\\")\n    pg_r = s.get(\\\"perm_granger_fdr_reverse_sig\\\", \\\"?\\\")\n    ty = s.get(\\\"ty_forward_sig\\\", \\\"?\\\")\n    rp = s.get(\\\"robust_pairs\\\", \\\"?\\\")\n    \n    row = \\\"|\\\".join([d, str(naive_sig)+\\\"/\\\"+str(total), str(diff)+\\\"/8\\\", str(thresh)+\\\"/8\\\", str(pg_f)+\\\"/8\\\", str(pg_r)+\\\"/8\\\", str(ty)+\\\"/8\\\", str(rp)+\\\"/8\\\"])\n    print(row)\n\"'",
  "description": "Final 5method extraction with fixed quoting",
  "timeout": "15000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "tool_args": {
    "command": "ssh westd-19828 'cd /root/autodl-tmp/distrib_canary_collapse && python3 -c \"\nimport json, glob, os\n\nfiles = sorted(glob.glob(\\\"results/**/5method_leadlag.json\\\", recursive=True))\nfor fp in files:\n    with open(fp) as f:\n        m = json.load(f)\n    s = m.get(\\\"summary\\\", {})\n    pairs = m.get(\\\"pairs\\\", [])\n    if isinstance(pairs, dict):\n        items = list(pairs.values())\n    else:\n        items = pairs\n    \n    naive_sig = 0\n    total = 0\n    for pv in items:\n        if not isinstance(pv, dict):\n            continue\n        fwd = pv.get(\\\"forward\\\", pv)\n        if isinstance(fwd, dict):\n            nx = fwd.get(\\\"naive_xcorr\\\", {})\n            if isinstance(nx, dict):\n                total += 1\n                if nx.get(\\\"significant\\\", False):\n                    naive_sig += 1\n    \n    d = os.path.dirname(os.path.dirname(fp))\n    diff = s.get(\\\"diff_xcorr_fdr_forward_sig\\\", \\\"?\\\")\n    thresh = s.get(\\\"threshold_forward_sig\\\", \\\"?\\\")\n    pg_f = s.get(\\\"perm_granger_fdr_forward_sig\\\", \\\"?\\\")\n    pg_r = s.get(\\\"perm_granger_fdr_reverse_sig\\\", \\\"?\\\")\n    ty = s.get(\\\"ty_forward_sig\\\", \\\"?\\\")\n    rp = s.get(\\\"robust_pairs\\\", \\\"?\\\")\n    \n    row = \\\"|\\\".join([d, str(naive_sig)+\\\"/\\\"+str(total), str(diff)+\\\"/8\\\", str(thresh)+\\\"/8\\\", str(pg_f)+\\\"/8\\\", str(pg_r)+\\\"/8\\\", str(ty)+\\\"/8\\\", str(rp)+\\\"/8\\\"])\n    print(row)\n\"'",
    "description": "Final 5method extraction with fixed quoting",
    "timeout": "15000"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-19T03:05:25.819628+00:00_

Warning: Permanently added '[connect.westd.seetacloud.com]:19828' (ED25519) to the list of known hosts.
results/alpha_sweep/a000_s42|8/8|4/8|3/8|0/8|1/8|1/8|1/8
results/alpha_sweep/a000_s43|7/8|3/8|1/8|0/8|0/8|1/8|0/8
results/alpha_sweep/a000_s44|8/8|3/8|1/8|0/8|0/8|0/8|0/8
results/alpha_sweep/a025_s43|8/8|3/8|0/8|0/8|0/8|0/8|0/8
results/alpha_sweep/a025_s44|8/8|1/8|0/8|0/8|0/8|2/8|0/8
results/alpha_sweep/a050_s42|8/8|8/8|0/8|0/8|0/8|0/8|0/8
results/alpha_sweep/a050_s43|8/8|6/8|0/8|6/8|0/8|0/8|1/8
results/alpha_sweep/a050_s44|8/8|6/8|0/8|3/8|0/8|0/8|0/8
results/alpha_sweep/a060_s42_bf16|8/8|8/8|0/8|8/8|0/8|0/8|1/8
results/alpha_sweep/a075_s42|8/8|8/8|4/8|8/8|0/8|1/8|5/8
results/alpha_sweep/a075_s43|8/8|8/8|0/8|5/8|0/8|1/8|4/8
results/alpha_sweep/a075_s44|8/8|8/8|4/8|6/8|0/8|1/8|5/8
results/generalize/gpt2m_wiki_a100_s42|8/8|8/8|0/8|6/8|3/8|2/8|2/8
results/generalize/opt1b_wiki_a100_s42|8/8|8/8|1/8|6/8|0/8|0/8|2/8
results/generalize/pythia14b_wiki_a100_s42|7/8|6/8|0/8|2/8|0/8|0/8|1/8
results/generalize/pythia14b_wiki_a100_s43|8/8|6/8|0/8|6/8|0/8|2/8|6/8
results/generalize/pythia1b_c4_a100_s42|8/8|6/8|0/8|6/8|3/8|1/8|2/8
results/generalize/pythia1b_c4_a100_s43|8/8|6/8|0/8|4/8|0/8|2/8|3/8
results/generalize/pythia410m_wiki_a100_s42|8/8|8/8|0/8|6/8|0/8|2/8|2/8

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-19T03:05:25.819763+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/ 2>/dev/null || echo \"dir exists or not\"",
  "description": "Check artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/ 2>/dev/null || echo \"dir exists or not\"",
    "description": "Check artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-19T03:05:25.819899+00:00_

D040
_project
a050_s44_draft_versions.tex
a075_analysis_prep.md
alpha_sweep
alpha_sweep_a000_s43
alpha_sweep_a000_s44
alpha_sweep_a005_s42
alpha_sweep_a010_s42_v2
alpha_sweep_a010_s43
alpha_sweep_a050_s42
alpha_sweep_a050_s43
alpha_sweep_a050_s44
alpha_sweep_a060_s42_bf16
alpha_sweep_a075_s42
alpha_sweep_a075_s43
alpha_sweep_a075_s44
alpha_sweep_c4_a050_s42_bf16
analysis
analysis_alpha_sweep_a010_s42_v2.md
analyze_extended.py
analyze_mvp.py
c4_vs_wikitext_a050_collapse.md
ccf_maxlag7_report.md
check_progress.sh
consensus_framework
cross_alpha_aggregation
cross_alpha_analysis_v4.py
cross_alpha_v4_ready.md
d024_literature_notes.md
d026_optimized_commands.md
d059_mvp_reverse_reanalysis.md
d060_pythia69b_prep.md
d061_conditional_granger_analysis.md
detrending_utils.py
diag_gen_gpt2m_a100_s43_bf16.md
dream_reports
drift_discrepancy_audit
figures
framing_alignment_check.md
gen_gpt2m_a100_s43_bf16
gen_wiki_gpt2m_a025_s42
gen_wiki_gpt2m_a100_s42_v3
gen_wiki_gpt2m_a100_s42_v4
generalization_draft.tex
generalization_prep.md
generalize_pythia14b_wiki_a100_s43
generalize_pythia1b_c4_a100_s42
generalize_pythia1b_c4_a100_s43
generalize_pythia410m
generalize_pythia410m_wiki_a100_s42
gpt2m_a025_analysis_plan.md
gpt2m_kappa
intervention_reactive_s42
iterative_train.py
literature_map.yaml
literature_scan_20260514.md
literature_scan_20260515
manifest.yaml
method_ablation
method_ablation_phase2
method_ablation_phase3
metrics.py
mvp_evaluation_criteria.md
panel_analysis_feasibility.md
paper_consistency_audit.md
permutation_granger.py
pipeline_analysis
plan_006_s42
prep_c4_gpt2m_readiness.md
prep_cross_alpha_v5_verify.md
prepare_data.py
report_gen_wiki_gpt2m_failure.md
review_issues.yaml
review_reports
run_mvp.sh
scale_14b_a050_s42
scale_14b_effrank_analysis
scale_s42_failure_analysis.md
shapley_method_contribution.pdf
shapley_method_contribution.png
shapley_values.json
tables
test_alpha_sweep.py
ty_seed_audit
window_sensitivity
window_sensitivity_t11

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-19T03:05:25.820060+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/table7_draft.md",
  "content": "# Table 7: Complete Lead-Lag Detection Results\n\n> Generated: 2026-05-19. Data sources: `5method_leadlag.json` (on-disk analysis) + registry metrics.\n> All fractions are X/8 (8 canary-diversity pairs: {token_entropy, ece} × {distinct_1, distinct_2, distinct_3, effective_rank}).\n> Constraint C003: TY values at α≤0.50 are seed-unstable and should NOT be cited as supporting evidence.\n\n## A. Main Axis: Pythia-410M, WikiText-103, fp32\n\n| Condition | Model | Dataset | α | Seeds | Precision | Naive | Diff | Thresh | PermG_fwd | PermG_rev | TY | K≥4 | MMCT_wt | Notes |\n|-----------|-------|---------|---|-------|-----------|-------|------|--------|-----------|-----------|-----|------|---------|-------|\n| a000_s42 | Pythia-410M | Wiki-103 | 0.00 | 42 | fp32 | 8/8 | 4/8 | 3/8 | 0/8 | 1/8 | 1/8 | 1/8 | — | Null control |\n| a000_s43 | Pythia-410M | Wiki-103 | 0.00 | 43 | fp32 | 7/8 | 3/8 | 1/8 | 0/8 | 0/8 | 1/8 | 0/8 | — | Null control |\n| a000_s44 | Pythia-410M | Wiki-103 | 0.00 | 44 | fp32 | 8/8 | 3/8 | 1/8 | 0/8 | 0/8 | 0/8 | 0/8 | — | Null control |\n| a010_s43 | Pythia-410M | Wiki-103 | 0.10 | 43 | fp32 | 7/8 | 8/8 | 3/8 | 0/8 | 0/8 | 0/8 | 0/8 | — | Canary blind zone (D075) |\n| a025_s42_v3 | Pythia-410M | Wiki-103 | 0.25 | 42 | fp32 | — | — | — | — | — | — | — | — | **GAP**: no lead-lag analysis on disk |\n| a025_s43 | Pythia-410M | Wiki-103 | 0.25 | 43 | fp32 | 8/8 | 3/8 | 0/8 | 0/8 | 0/8 | 0/8 | 0/8 | — | Sub-threshold regime |\n| a025_s44 | Pythia-410M | Wiki-103 | 0.25 | 44 | fp32 | 8/8 | 1/8 | 0/8 | 0/8 | 0/8 | 2/8 | 0/8 | — | Sub-threshold; TY unstable (C003) |\n| a050_s42 | Pythia-410M | Wiki-103 | 0.50 | 42 | fp32 | 8/8 | 8/8 | 0/8 | 0/8 | 0/8 | 0/8 | 0/8 | — | Threshold boundary |\n| a050_s43 | Pythia-410M | Wiki-103 | 0.50 | 43 | fp32 | 8/8 | 6/8 | 0/8 | 6/8 | 0/8 | 0/8 | 1/8 | — | PermG emerges in s43 only |\n| a050_s44 | Pythia-410M | Wiki-103 | 0.50 | 44 | fp32 | 8/8 | 6/8 | 0/8 | 3/8 | 0/8 | 0/8 | 0/8 | — | PermG partial |\n| a075_s42 | Pythia-410M | Wiki-103 | 0.75 | 42 | fp32 | 8/8 | 8/8 | 4/8 | 8/8 | 0/8 | 1/8 | 5/8 | — | Confirmatory regime |\n| a075_s43 | Pythia-410M | Wiki-103 | 0.75 | 43 | fp32 | 8/8 | 8/8 | 0/8 | 5/8 | 0/8 | 1/8 | 4/8 | — | Confirmatory regime |\n| a075_s44 | Pythia-410M | Wiki-103 | 0.75 | 44 | fp32 | 8/8 | 8/8 | 4/8 | 6/8 | 0/8 | 1/8 | 5/8 | — | Confirmatory regime |\n| a100_s42 | Pythia-410M | Wiki-103 | 1.00 | 42 | fp32 | 8/8 | 8/8 | 0/8 | 6/8 | 0/8 | 2/8 | 2/8 | — | Full contamination (generalize_pythia410m) |\n| mvp_v4_rep42 | Pythia-410M | Wiki-103 | 1.00 | 42 | fp32 | — | — | — | — | — | — | — | — | Early MVP; no 5method analysis |\n| mvp_v4_rep43 | Pythia-410M | Wiki-103 | 1.00 | 43 | fp32 | — | — | — | — | — | — | — | — | Early MVP; no 5method analysis |\n| mvp_v4_rep44 | Pythia-410M | Wiki-103 | 1.00 | 44 | fp32 | — | — | — | — | — | — | — | — | Early MVP; no 5method analysis |\n| mvp_v4_rep45 | Pythia-410M | Wiki-103 | 1.00 | 45 | fp32 | — | — | — | — | — | — | — | — | Early MVP; no 5method analysis |\n\n## B. Cross-Architecture: WikiText-103, α=1.00, fp32\n\n| Condition | Model | Dataset | α | Seeds | Precision | Naive | Diff | Thresh | PermG_fwd | PermG_rev | TY | K≥4 | MMCT_wt | Notes |\n|-----------|-------|---------|---|-------|-----------|-------|------|--------|-----------|-----------|-----|------|---------|-------|\n| gen_wiki_gpt2m_a100_s42_v4 | GPT-2-Medium | Wiki-103 | 1.00 | 42 | fp32 | 8/8 | 8/8 | 0/8 | 6/8 | 3/8 | 2/8 | 2/8 | — | 5method on disk; rev=3/8 from ECE pairs |\n| gen_wiki_gpt2m_a025_s42 | GPT-2-Medium | Wiki-103 | 0.25 | 42 | fp32 | — | — | — | — | — | — | — | — | **GAP**: no lead-lag analysis |\n| generalize_opt1b_wiki_a100_s42 | OPT-1.3B | Wiki-103 | 1.00 | 42 | fp32 | 8/8 | 8/8 | 1/8 | 6/8 | 0/8 | 0/8 | 2/8 | — | |\n| generalize_pythia14b_wiki_a100_s42 | Pythia-1.4B | Wiki-103 | 1.00 | 42 | fp32 | 7/8 | 6/8 | 0/8 | 2/8 | 0/8 | 0/8 | 1/8 | — | Low PermG; seed variance? |\n| generalize_pythia14b_wiki_a100_s43 | Pythia-1.4B | Wiki-103 | 1.00 | 43 | fp32 | 8/8 | 6/8 | 0/8 | 6/8 | 0/8 | 2/8 | 6/8 | — | Strong confirmation vs s42 |\n\n## C. Cross-Dataset: C4\n\n| Condition | Model | Dataset | α | Seeds | Precision | Naive | Diff | Thresh | PermG_fwd | PermG_rev | TY | K≥4 | MMCT_wt | Notes |\n|-----------|-------|---------|---|-------|-----------|-------|------|--------|-----------|-----------|-----|------|---------|-------|\n| generalize_pythia1b_c4_a100_s42_v2 | Pythia-1B | C4 | 1.00 | 42 | fp32 | 8/8 | 6/8 | 0/8 | 6/8 | 3/8 | 1/8 | 2/8 | — | rev=3/8 from ECE-diversity bidirectional coupling |\n| generalize_pythia1b_c4_a100_s43 | Pythia-1B | C4 | 1.00 | 43 | fp32 | 8/8 | 6/8 | 0/8 | 4/8 | 0/8 | 2/8 | 3/8 | — | |\n| alpha_sweep_c4_a050_s42_bf16 | Pythia-410M | C4 | 0.50 | 42 | bf16 | — | — | — | 0/8 | 0/8 | — | — | — | Registry only: permg_fwd=0/8; **bf16 caveat** |\n\n## D. Scale\n\n| Condition | Model | Dataset | α | Seeds | Precision | Naive | Diff | Thresh | PermG_fwd | PermG_rev | TY | K≥4 | MMCT_wt | Notes |\n|-----------|-------|---------|---|-------|-----------|-------|------|--------|-----------|-----------|-----|------|---------|-------|\n| scale_14b_a050_s42 | Pythia-1.4B | Wiki-103 | 0.50 | 42 | fp32 | — | — | — | — | — | — | — | — | **GAP**: no lead-lag analysis on disk |\n\n## E. Intervention: Pythia-410M, WikiText-103, α=1.00\n\n| Condition | Model | Dataset | α | Seeds | Precision | Naive | Diff | Thresh | PermG_fwd | PermG_rev | TY | K≥4 | MMCT_wt | Notes |\n|-----------|-------|---------|---|-------|-----------|-------|------|--------|-----------|-----------|-----|------|---------|-------|\n| intervention_predictive_s42 | Pythia-410M | Wiki-103 | 1.00 | 42 | fp32 | — | — | — | — | — | — | — | — | **GAP**: no lead-lag analysis; canary-triggered at Gen 1 |\n| intervention_reactive_s42 | Pythia-410M | Wiki-103 | 1.00 | 42 | fp32 | — | — | — | — | — | — | — | — | **GAP**: no lead-lag analysis; downstream-triggered |\n\n## F. Supplementary: bf16 Experiments\n\n| Condition | Model | Dataset | α | Seeds | Precision | Naive | Diff | Thresh | PermG_fwd | PermG_rev | TY | K≥4 | MMCT_wt | Notes |\n|-----------|-------|---------|---|-------|-----------|-------|------|--------|-----------|-----------|-----|------|---------|-------|\n| a060_s42_bf16 | Pythia-410M | Wiki-103 | 0.60 | 42 | bf16 | 8/8 | 8/8 | 6/8 | 8/8 | 0/8 | 0/8 | 6/8 | 6/8 | Registry unified_2sigma; 5method shows thresh=0, K4=1 (different threshold) |\n| c4_a050_s42_bf16 | Pythia-410M | C4 | 0.50 | 42 | bf16 | — | — | — | 0/8 | 0/8 | — | — | — | (same as Section C row) |\n| gen_gpt2m_a100_s43_bf16 | GPT-2-Medium | Wiki-103 | 1.00 | 43 | bf16 | 8/8 | — | 8/8 | — | — | — | 1/8 | 6/8 | Registry only (n_perm=5000) |\n| interv_pred_s43_bf16 | Pythia-410M | Wiki-103 | 1.00 | 43 | bf16 | — | — | — | — | — | — | — | — | **GAP**: no lead-lag analysis |\n| interv_react_s43_bf16 | Pythia-410M | Wiki-103 | 1.00 | 43 | bf16 | — | — | — | — | — | — | — | — | **GAP**: no lead-lag analysis |\n\n## G. Analysis-Only Experiments (no individual training runs)\n\nThese experiments analyze existing data across multiple conditions and do not have per-condition lead-lag metrics:\n\n| Condition | Description | Key Findings |\n|-----------|-------------|--------------|\n| method_ablation_phase1 | 16-pair method comparison | naive_sig=16/16, threshold=9/16, permG=6/16 |\n| method_ablation_phase2 | FDR correction impact | PermG FDR sig: α=0.00→0%, α=0.25→0%, α=0.50→0%, α=1.00→75% |\n| method_ablation_phase3 | Step-change analysis | PermG: 0% (α≤0.50) → 100% (α=0.60) → 83% (α=0.75) |\n| conditional_granger_d061 | Conditional Granger controlling ECE/entropy | Independent canary signals confirmed |\n| plan_009_bootstrap_ty | Bootstrap TY analysis | TY instability confirmed (basis for C003) |\n\n## H. Pending (RUNNING Experiments)\n\n| Condition | Model | Dataset | α | Seed | Precision | Status |\n|-----------|-------|---------|---|------|-----------|--------|\n| alpha_sweep_a005_s42_v3 | Pythia-410M | Wiki-103 | 0.05 | 42 | fp32 | RUNNING (D080 fix) |\n| alpha_sweep_a010_s43_fp32 | Pythia-410M | Wiki-103 | 0.10 | 43 | fp32 | RUNNING (fp32 re-run) |\n| alpha_sweep_a060_s42_fp32_v3 | Pythia-410M | Wiki-103 | 0.60 | 42 | fp32 | RUNNING (D080 fix, replaces bf16) |\n| interv_pred_a075_s42_fp32_v4 | Pythia-410M | Wiki-103 | 0.75 | 42 | fp32 | RUNNING (D080 fix) |\n| gen_gpt2m_a100_s43_fp32 | GPT-2-Medium | Wiki-103 | 1.00 | 43 | fp32 | RUNNING (replaces bf16 version) |\n| qwen35_08b_wiki_a100_s42_v2 | Qwen3.5-0.8B | Wiki-103 | 1.00 | 42 | fp32 | RUNNING (new architecture) |\n| smollm3_3b_wiki_a100_s42_v3 | SmolLM3-3B | Wiki-103 | 1.00 | 42 | fp32 | RUNNING (new architecture) |\n| scale_69b_a100_s42 | Pythia-6.9B | Wiki-103 | 1.00 | 42 | bf16 | RUNNING (scale-up) |\n\n---\n\n## Coverage Summary\n\n### Completed conditions with lead-lag analysis: 19/39\n\n| Category | With lead-lag | Without lead-lag | Total |\n|----------|--------------|-----------------|-------|\n| Main axis (Pythia-410M, Wiki, fp32) | 13 | 5 (a025_s42, mvp×4) | 18 |\n| Cross-architecture (fp32) | 4 | 1 (gpt2m_a025) | 5 |\n| Cross-dataset (C4) | 2 | 1 (c4_a050 bf16, partial) | 3 |\n| Scale | 0 | 1 (scale_14b) | 1 |\n| Intervention | 0 | 4 | 4 |\n| Analysis-only | N/A | N/A | 5 |\n| bf16 supplementary | 2 | 1 (partial) | 3 |\n\n### Precision distribution\n- **fp32**: 28 experiments (20 main/cross-arch, 4 intervention, 4 mvp)\n- **bf16**: 5 experiments (a060, c4_a050, gpt2m_s43, interv_pred_s43, interv_react_s43)\n- **fp32 pending**: 6 of 8 RUNNING experiments are D080 fp32 re-runs\n\n### Seed coverage (Main axis, Pythia-410M, Wiki-103, fp32)\n| α | s42 | s43 | s44 | s45 |\n|---|-----|-----|-----|-----|\n| 0.00 | ✓ | ✓ | ✓ | — |\n| 0.05 | pending | — | — | — |\n| 0.10 | — | ✓ (+ fp32 pending) | — | — |\n| 0.25 | **GAP** (no analysis) | ✓ | ✓ | — |\n| 0.50 | ✓ | ✓ | ✓ | — |\n| 0.60 | bf16 only (fp32 pending) | — | — | — |\n| 0.75 | ✓ | ✓ | ✓ | — |\n| 1.00 | ✓ | mvp (no analysis) | mvp (no analysis) | mvp (no analysis) |\n\n## Identified Gaps\n\n### Critical (blocks Table 7 completeness):\n1. **α=0.25, s42**: `alpha_sweep_a025_s42_v3` has no 5method_leadlag.json. Need to run analysis.\n2. **α=1.00 multi-seed**: mvp_v4_rep42-45 lack lead-lag analysis. Need to run 5method on mvp data or use generalize_pythia410m_wiki_a100_s42 as the canonical α=1.00 row.\n3. **Intervention experiments**: All 4 (predictive/reactive × s42/s43) lack lead-lag analysis. These need different analysis since intervention changes α mid-run.\n4. **scale_14b_a050_s42**: No lead-lag analysis on disk.\n5. **α=0.10, s42**: No success experiment in registry (only s43).\n\n### Medium priority:\n6. **GPT-2-Medium α=0.25 s42**: `gen_wiki_gpt2m_a025_s42` has no lead-lag analysis.\n7. **MMCT coverage**: Only a060_bf16 (6/8) and gen_gpt2m_s43_bf16 (6/8) have MMCT data. All other experiments lack MMCT.\n8. **α=0.60 fp32**: Currently only bf16 version completed. fp32 version RUNNING.\n9. **α=0.05**: No completed experiment. RUNNING.\n\n### Low priority:\n10. **gen_wiki_gpt2m_a100_s42_v3 vs v4**: Duplicate entries for same data. v4 is canonical.\n11. **Pythia-1.4B s42 weak signal**: PermG=2/8, K4=1/8 vs s43's 6/8, 6/8. Seed variance or anomaly?\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/table7_draft.md",
    "content": "# Table 7: Complete Lead-Lag Detection Results\n\n> Generated: 2026-05-19. Data sources: `5method_leadlag.json` (on-disk analysis) + registry metrics.\n> All fractions are X/8 (8 canary-diversity pairs: {token_entropy, ece} × {distinct_1, distinct_2, distinct_3, effective_rank}).\n> Constraint C003: TY values at α≤0.50 are seed-unstable and should NOT be cited as supporting evidence.\n\n## A. Main Axis: Pythia-410M, WikiText-103, fp32\n\n| Condition | Model | Dataset | α | Seeds | Precision | Naive | Diff | Thresh | PermG_fwd | PermG_rev | TY | K≥4 | MMCT_wt | Notes |\n|-----------|-------|---------|---|-------|-----------|-------|------|--------|-----------|-----------|-----|------|---------|-------|\n| a000_s42 | Pythia-410M | Wiki-103 | 0.00 | 42 | fp32 | 8/8 | 4/8 | 3/8 | 0/8 | 1/8 | 1/8 | 1/8 | — | Null control |\n| a000_s43 | Pythia-410M | Wiki-103 | 0.00 | 43 | fp32 | 7/8 | 3/8 | 1/8 | 0/8 | 0/8 | 1/8 | 0/8 | — | Null control |\n| a000_s44 | Pythia-410M | Wiki-103 | 0.00 | 44 | fp32 | 8/8 | 3/8 | 1/8 | 0/8 | 0/8 | 0/8 | 0/8 | — | Null control |\n| a010_s43 | Pythia-410M | Wiki-103 | 0.10 | 43 | fp32 | 7/8 | 8/8 | 3/8 | 0/8 | 0/8 | 0/8 | 0/8 | — | Canary blind zone (D075) |\n| a025_s42_v3 | Pythia-410M | Wiki-103 | 0.25 | 42 | fp32 | — | — | — | — | — | — | — | — | **GAP**: no lead-lag analysis on disk |\n| a025_s43 | Pythia-410M | Wiki-103 | 0.25 | 43 | fp32 | 8/8 | 3/8 | 0/8 | 0/8 | 0/8 | 0/8 | 0/8 | — | Sub-threshold regime |\n| a025_s44 | Pythia-410M | Wiki-103 | 0.25 | 44 | fp32 | 8/8 | 1/8 | 0/8 | 0/8 | 0/8 | 2/8 | 0/8 | — | Sub-threshold; TY unstable (C003) |\n| a050_s42 | Pythia-410M | Wiki-103 | 0.50 | 42 | fp32 | 8/8 | 8/8 | 0/8 | 0/8 | 0/8 | 0/8 | 0/8 | — | Threshold boundary |\n| a050_s43 | Pythia-410M | Wiki-103 | 0.50 | 43 | fp32 | 8/8 | 6/8 | 0/8 | 6/8 | 0/8 | 0/8 | 1/8 | — | PermG emerges in s43 only |\n| a050_s44 | Pythia-410M | Wiki-103 | 0.50 | 44 | fp32 | 8/8 | 6/8 | 0/8 | 3/8 | 0/8 | 0/8 | 0/8 | — | PermG partial |\n| a075_s42 | Pythia-410M | Wiki-103 | 0.75 | 42 | fp32 | 8/8 | 8/8 | 4/8 | 8/8 | 0/8 | 1/8 | 5/8 | — | Confirmatory regime |\n| a075_s43 | Pythia-410M | Wiki-103 | 0.75 | 43 | fp32 | 8/8 | 8/8 | 0/8 | 5/8 | 0/8 | 1/8 | 4/8 | — | Confirmatory regime |\n| a075_s44 | Pythia-410M | Wiki-103 | 0.75 | 44 | fp32 | 8/8 | 8/8 | 4/8 | 6/8 | 0/8 | 1/8 | 5/8 | — | Confirmatory regime |\n| a100_s42 | Pythia-410M | Wiki-103 | 1.00 | 42 | fp32 | 8/8 | 8/8 | 0/8 | 6/8 | 0/8 | 2/8 | 2/8 | — | Full contamination (generalize_pythia410m) |\n| mvp_v4_rep42 | Pythia-410M | Wiki-103 | 1.00 | 42 | fp32 | — | — | — | — | — | — | — | — | Early MVP; no 5method analysis |\n| mvp_v4_rep43 | Pythia-410M | Wiki-103 | 1.00 | 43 | fp32 | — | — | — | — | — | — | — | — | Early MVP; no 5method analysis |\n| mvp_v4_rep44 | Pythia-410M | Wiki-103 | 1.00 | 44 | fp32 | — | — | — | — | — | — | — | — | Early MVP; no 5method analysis |\n| mvp_v4_rep45 | Pythia-410M | Wiki-103 | 1.00 | 45 | fp32 | — | — | — | — | — | — | — | — | Early MVP; no 5method analysis |\n\n## B. Cross-Architecture: WikiText-103, α=1.00, fp32\n\n| Condition | Model | Dataset | α | Seeds | Precision | Naive | Diff | Thresh | PermG_fwd | PermG_rev | TY | K≥4 | MMCT_wt | Notes |\n|-----------|-------|---------|---|-------|-----------|-------|------|--------|-----------|-----------|-----|------|---------|-------|\n| gen_wiki_gpt2m_a100_s42_v4 | GPT-2-Medium | Wiki-103 | 1.00 | 42 | fp32 | 8/8 | 8/8 | 0/8 | 6/8 | 3/8 | 2/8 | 2/8 | — | 5method on disk; rev=3/8 from ECE pairs |\n| gen_wiki_gpt2m_a025_s42 | GPT-2-Medium | Wiki-103 | 0.25 | 42 | fp32 | — | — | — | — | — | — | — | — | **GAP**: no lead-lag analysis |\n| generalize_opt1b_wiki_a100_s42 | OPT-1.3B | Wiki-103 | 1.00 | 42 | fp32 | 8/8 | 8/8 | 1/8 | 6/8 | 0/8 | 0/8 | 2/8 | — | |\n| generalize_pythia14b_wiki_a100_s42 | Pythia-1.4B | Wiki-103 | 1.00 | 42 | fp32 | 7/8 | 6/8 | 0/8 | 2/8 | 0/8 | 0/8 | 1/8 | — | Low PermG; seed variance? |\n| generalize_pythia14b_wiki_a100_s43 | Pythia-1.4B | Wiki-103 | 1.00 | 43 | fp32 | 8/8 | 6/8 | 0/8 | 6/8 | 0/8 | 2/8 | 6/8 | — | Strong confirmation vs s42 |\n\n## C. Cross-Dataset: C4\n\n| Condition | Model | Dataset | α | Seeds | Precision | Naive | Diff | Thresh | PermG_fwd | PermG_rev | TY | K≥4 | MMCT_wt | Notes |\n|-----------|-------|---------|---|-------|-----------|-------|------|--------|-----------|-----------|-----|------|---------|-------|\n| generalize_pythia1b_c4_a100_s42_v2 | Pythia-1B | C4 | 1.00 | 42 | fp32 | 8/8 | 6/8 | 0/8 | 6/8 | 3/8 | 1/8 | 2/8 | — | rev=3/8 from ECE-diversity bidirectional coupling |\n| generalize_pythia1b_c4_a100_s43 | Pythia-1B | C4 | 1.00 | 43 | fp32 | 8/8 | 6/8 | 0/8 | 4/8 | 0/8 | 2/8 | 3/8 | — | |\n| alpha_sweep_c4_a050_s42_bf16 | Pythia-410M | C4 | 0.50 | 42 | bf16 | — | — | — | 0/8 | 0/8 | — | — | — | Registry only: permg_fwd=0/8; **bf16 caveat** |\n\n## D. Scale\n\n| Condition | Model | Dataset | α | Seeds | Precision | Naive | Diff | Thresh | PermG_fwd | PermG_rev | TY | K≥4 | MMCT_wt | Notes |\n|-----------|-------|---------|---|-------|-----------|-------|------|--------|-----------|-----------|-----|------|---------|-------|\n| scale_14b_a050_s42 | Pythia-1.4B | Wiki-103 | 0.50 | 42 | fp32 | — | — | — | — | — | — | — | — | **GAP**: no lead-lag analysis on disk |\n\n## E. Intervention: Pythia-410M, WikiText-103, α=1.00\n\n| Condition | Model | Dataset | α | Seeds | Precision | Naive | Diff | Thresh | PermG_fwd | PermG_rev | TY | K≥4 | MMCT_wt | Notes |\n|-----------|-------|---------|---|-------|-----------|-------|------|--------|-----------|-----------|-----|------|---------|-------|\n| intervention_predictive_s42 | Pythia-410M | Wiki-103 | 1.00 | 42 | fp32 | — | — | — | — | — | — | — | — | **GAP**: no lead-lag analysis; canary-triggered at Gen 1 |\n| intervention_reactive_s42 | Pythia-410M | Wiki-103 | 1.00 | 42 | fp32 | — | — | — | — | — | — | — | — | **GAP**: no lead-lag analysis; downstream-triggered |\n\n## F. Supplementary: bf16 Experiments\n\n| Condition | Model | Dataset | α | Seeds | Precision | Naive | Diff | Thresh | PermG_fwd | PermG_rev | TY | K≥4 | MMCT_wt | Notes |\n|-----------|-------|---------|---|-------|-----------|-------|------|--------|-----------|-----------|-----|------|---------|-------|\n| a060_s42_bf16 | Pythia-410M | Wiki-103 | 0.60 | 42 | bf16 | 8/8 | 8/8 | 6/8 | 8/8 | 0/8 | 0/8 | 6/8 | 6/8 | Registry unified_2sigma; 5method shows thresh=0, K4=1 (different threshold) |\n| c4_a050_s42_bf16 | Pythia-410M | C4 | 0.50 | 42 | bf16 | — | — | — | 0/8 | 0/8 | — | — | — | (same as Section C row) |\n| gen_gpt2m_a100_s43_bf16 | GPT-2-Medium | Wiki-103 | 1.00 | 43 | bf16 | 8/8 | — | 8/8 | — | — | — | 1/8 | 6/8 | Registry only (n_perm=5000) |\n| interv_pred_s43_bf16 | Pythia-410M | Wiki-103 | 1.00 | 43 | bf16 | — | — | — | — | — | — | — | — | **GAP**: no lead-lag analysis |\n| interv_react_s43_bf16 | Pythia-410M | Wiki-103 | 1.00 | 43 | bf16 | — | — | — | — | — | — | — | — | **GAP**: no lead-lag analysis |\n\n## G. Analysis-Only Experiments (no individual training runs)\n\nThese experiments analyze existing data across multiple conditions and do not have per-condition lead-lag metrics:\n\n| Condition | Description | Key Findings |\n|-----------|-------------|--------------|\n| method_ablation_phase1 | 16-pair method comparison | naive_sig=16/16, threshold=9/16, permG=6/16 |\n| method_ablation_phase2 | FDR correction impact | PermG FDR sig: α=0.00→0%, α=0.25→0%, α=0.50→0%, α=1.00→75% |\n| method_ablation_phase3 | Step-change analysis | PermG: 0% (α≤0.50) → 100% (α=0.60) → 83% (α=0.75) |\n| conditional_granger_d061 | Conditional Granger controlling ECE/entropy | Independent canary signals confirmed |\n| plan_009_bootstrap_ty | Bootstrap TY analysis | TY instability confirmed (basis for C003) |\n\n## H. Pending (RUNNING Experiments)\n\n| Condition | Model | Dataset | α | Seed | Precision | Status |\n|-----------|-------|---------|---|------|-----------|--------|\n| alpha_sweep_a005_s42_v3 | Pythia-410M | Wiki-103 | 0.05 | 42 | fp32 | RUNNING (D080 fix) |\n| alpha_sweep_a010_s43_fp32 | Pythia-410M | Wiki-103 | 0.10 | 43 | fp32 | RUNNING (fp32 re-run) |\n| alpha_sweep_a060_s42_fp32_v3 | Pythia-410M | Wiki-103 | 0.60 | 42 | fp32 | RUNNING (D080 fix, replaces bf16) |\n| interv_pred_a075_s42_fp32_v4 | Pythia-410M | Wiki-103 | 0.75 | 42 | fp32 | RUNNING (D080 fix) |\n| gen_gpt2m_a100_s43_fp32 | GPT-2-Medium | Wiki-103 | 1.00 | 43 | fp32 | RUNNING (replaces bf16 version) |\n| qwen35_08b_wiki_a100_s42_v2 | Qwen3.5-0.8B | Wiki-103 | 1.00 | 42 | fp32 | RUNNING (new architecture) |\n| smollm3_3b_wiki_a100_s42_v3 | SmolLM3-3B | Wiki-103 | 1.00 | 42 | fp32 | RUNNING (new architecture) |\n| scale_69b_a100_s42 | Pythia-6.9B | Wiki-103 | 1.00 | 42 | bf16 | RUNNING (scale-up) |\n\n---\n\n## Coverage Summary\n\n### Completed conditions with lead-lag analysis: 19/39\n\n| Category | With lead-lag | Without lead-lag | Total |\n|----------|--------------|-----------------|-------|\n| Main axis (Pythia-410M, Wiki, fp32) | 13 | 5 (a025_s42, mvp×4) | 18 |\n| Cross-architecture (fp32) | 4 | 1 (gpt2m_a025) | 5 |\n| Cross-dataset (C4) | 2 | 1 (c4_a050 bf16, partial) | 3 |\n| Scale | 0 | 1 (scale_14b) | 1 |\n| Intervention | 0 | 4 | 4 |\n| Analysis-only | N/A | N/A | 5 |\n| bf16 supplementary | 2 | 1 (partial) | 3 |\n\n### Precision distribution\n- **fp32**: 28 experiments (20 main/cross-arch, 4 intervention, 4 mvp)\n- **bf16**: 5 experiments (a060, c4_a050, gpt2m_s43, interv_pred_s43, interv_react_s43)\n- **fp32 pending**: 6 of 8 RUNNING experiments are D080 fp32 re-runs\n\n### Seed coverage (Main axis, Pythia-410M, Wiki-103, fp32)\n| α | s42 | s43 | s44 | s45 |\n|---|-----|-----|-----|-----|\n| 0.00 | ✓ | ✓ | ✓ | — |\n| 0.05 | pending | — | — | — |\n| 0.10 | — | ✓ (+ fp32 pending) | — | — |\n| 0.25 | **GAP** (no analysis) | ✓ | ✓ | — |\n| 0.50 | ✓ | ✓ | ✓ | — |\n| 0.60 | bf16 only (fp32 pending) | — | — | — |\n| 0.75 | ✓ | ✓ | ✓ | — |\n| 1.00 | ✓ | mvp (no analysis) | mvp (no analysis) | mvp (no analysis) |\n\n## Identified Gaps\n\n### Critical (blocks Table 7 completeness):\n1. **α=0.25, s42**: `alpha_sweep_a025_s42_v3` has no 5method_leadlag.json. Need to run analysis.\n2. **α=1.00 multi-seed**: mvp_v4_rep42-45 lack lead-lag analysis. Need to run 5method on mvp data or use generalize_pythia410m_wiki_a100_s42 as the canonical α=1.00 row.\n3. **Intervention experiments**: All 4 (predictive/reactive × s42/s43) lack lead-lag analysis. These need different analysis since intervention changes α mid-run.\n4. **scale_14b_a050_s42**: No lead-lag analysis on disk.\n5. **α=0.10, s42**: No success experiment in registry (only s43).\n\n### Medium priority:\n6. **GPT-2-Medium α=0.25 s42**: `gen_wiki_gpt2m_a025_s42` has no lead-lag analysis.\n7. **MMCT coverage**: Only a060_bf16 (6/8) and gen_gpt2m_s43_bf16 (6/8) have MMCT data. All other experiments lack MMCT.\n8. **α=0.60 fp32**: Currently only bf16 version completed. fp32 version RUNNING.\n9. **α=0.05**: No completed experiment. RUNNING.\n\n### Low priority:\n10. **gen_wiki_gpt2m_a100_s42_v3 vs v4**: Duplicate entries for same data. v4 is canonical.\n11. **Pythia-1.4B s42 weak signal**: PermG=2/8, K4=1/8 vs s43's 6/8, 6/8. Seed variance or anomaly?\n"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-19T03:05:25.820335+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/table7_draft.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-19T03:05:25.820469+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "Table 7 Draft",
  "type": "report",
  "description": "Complete Table 7 draft with lead-lag detection results across all 39 success experiments, organized by category (main axis, cross-architecture, cross-dataset, scale, intervention, bf16). Includes coverage summary, seed matrix, and 11 identified gaps.",
  "project": "distrib_canary_collapse",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/table7_draft.md",
  "tags": "['table7', 'lead-lag', 'paper']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "Table 7 Draft",
    "type": "report",
    "description": "Complete Table 7 draft with lead-lag detection results across all 39 success experiments, organized by category (main axis, cross-architecture, cross-dataset, scale, intervention, bf16). Includes coverage summary, seed matrix, and 11 identified gaps.",
    "project": "distrib_canary_collapse",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/table7_draft.md",
    "tags": "['table7', 'lead-lag', 'paper']"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-19T03:05:25.820608+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260519_ed67c8\", \"name\": \"Table 7 Draft\", \"type\": \"report\", \"description\": \"Complete Table 7 draft with lead-lag detection results across all 39 success experiments, organized by category (main axis, cross-architecture, cross-dataset, scale, intervention, bf16). Includes coverage summary, seed matrix, and 11 identified gaps.\", \"path\": \"projects/distrib_canary_collapse/artifacts/_project/report/table7_draft.md\", \"url\": null, \"project\": \"distrib_canary_collapse\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-19T03:05:16.378498+00:00\", \"tags\": [\"table7\", \"lead-lag\", \"paper\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data_table7_draft_20260519T025439",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 77 · 2026-05-19T03:05:25.820764+00:00_

写入完成。

**产出**: `artifacts/table7_draft.md`

**核心数据**:
- 39 个 success 实验中，19 个有 5method lead-lag 分析数据，5 个有 registry 部分数据，15 个缺失
- 8 个实验 RUNNING (含 6 个 D080 fp32 修复重跑 + Qwen3.5 + SmolLM3 新架构)
- 表格按 7 个分区组织：Main axis / Cross-arch / Cross-dataset / Scale / Intervention / bf16 supplementary / Analysis-only

**关键 gaps**:
1. α=0.25 s42 和 α=1.00 mvp×4 缺 lead-lag 分析
2. 全部 4 个 intervention 实验缺分析
3. scale_14b_a050_s42 缺分析
4. MMCT 覆盖率极低（仅 2 个实验有数据）
5. α=0.10 只有 s43 一个 seed

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_data_table7_draft_20260519T025439"
}
```

</details>

---
