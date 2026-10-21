# analysis d150 shapley v3 dedup fdr

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 85
- **Recorded user turns:** 0
- **Tool calls:** 42
- **Original source:** `logs/chats/worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236.jsonl`
- **Structured JSON:** [`308ca97ac9b85fad9462.json`](../../sessions/30/308ca97ac9b85fad9462.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

85 recorded events

### Tool call

_source line 1 · 2026-05-20T14:33:05.270385+00:00_

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
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
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

_source line 2 · 2026-05-20T14:33:05.270868+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T14:33:05.271040+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/shapley_v2/shapley_values_v2.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/shapley_v2/shapley_values_v2.json"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T14:33:05.271269+00:00_

1	{
2	  "version": "v2_d120_compliant",
3	  "generated_at": "2026-05-20T13:54:43.392607",
4	  "data_sources": [
5	    "19828:alpha_sweep/a000_s42",
6	    "19828:alpha_sweep/a000_s43",
7	    "19828:alpha_sweep/a000_s44",
8	    "19828:ablation/accumulate_a050_s43",
9	    "19828:alpha_sweep/a010_s42",
10	    "19828:alpha_sweep/a025_s43",
11	    "19828:alpha_sweep/a025_s44",
12	    "19828:alpha_sweep/a050_s42",
13	    "19828:alpha_sweep/a050_s43",
14	    "19828:alpha_sweep/a050_s44",
15	    "19828:alpha_sweep/a055_s42_fp32",
16	    "19828:alpha_sweep/a075_s42",
17	    "19828:alpha_sweep/a075_s43",
18	    "19828:alpha_sweep/a075_s44",
19	    "19828:alpha_sweep/c4_a050_s43_fp32",
20	    "19828:alpha_sweep/c4_a075_s43_fp32",
21	    "19828:gen_opt13b_wiki_a100_s43_fp32",
22	    "19828:gen_wiki_gpt2m_a100_s43",
23	    "19828:generalize/gpt2m_wiki_a100_s42",
24	    "19828:generalize/opt1b_wiki_a100_s42",
25	    "19828:generalize/pythia14b_wiki_a100_s42",
26	    "19828:generalize/pythia14b_wiki_a100_s43",
27	    "19828:generalize/pythia1b_c4_a100_s42",
28	    "19828:generalize/pythia1b_c4_a100_s43",
29	    "19828:generalize/pythia410m_wiki_a100_s42",
30	    "19828:generalize/smollm3_3b_wiki_a100_s42_fp32_v3",
31	    "19828:intervention/predictive_te_s42",
32	    "19828:intervention/reactive_d1_s42",
33	    "19828:scale_check/pythia14b_a050_s42",
34	    "17855:alpha_sweep/a000_s42_fp32",
35	    "17855:alpha_sweep/a005_s42_fp32_v3_d080",
36	    "17855:alpha_sweep/a010_s42_fp32",
37	    "17855:alpha_sweep/a010_s43_fp32",
38	    "17855:alpha_sweep/a025_s42_fp32",
39	    "17855:alpha_sweep/a025_s43_fp32",
40	    "17855:alpha_sweep/a025_s44_fp32",
41	    "17855:alpha_sweep/a030_s42_fp32",
42	    "17855:alpha_sweep/a035_s42_fp32",
43	    "17855:alpha_sweep/a040_s42_fp32",
44	    "17855:alpha_sweep/a045_s42_fp32",
45	    "17855:alpha_sweep/a050_postd093_s42_fp32",
46	    "17855:alpha_sweep/a050_s42_fp32",
47	    "17855:alpha_sweep/a050_s43_fp32",
48	    "17855:alpha_sweep/a050_s44_fp3
…[truncated 3304 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T14:33:05.271469+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "find /root/autodl-tmp/distrib_canary_collapse -name \"5method_leadlag.json\" -path \"*/analysis/*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "find /root/autodl-tmp/distrib_canary_collapse -name \"5method_leadlag.json\" -path \"*/analysis/*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-20T14:33:05.271609+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "find /root/distrib_canary_collapse -name \"5method_leadlag.json\" -path \"*/analysis/*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "find /root/distrib_canary_collapse -name \"5method_leadlag.json\" -path \"*/analysis/*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-20T14:33:05.271766+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a075_s42/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s43/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s43/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s44/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a075_s43/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a075_s44/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s43/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s44/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s44/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a010_s42/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a060_s42_bf16/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/c4_a050_s43_fp32/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/c4_a075_s43_fp32/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a055_s42_fp32/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/generalize/pythia410m_wiki_a100_s42/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/generalize/opt1b_wiki_a100_s42/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/generali
…[truncated 1402 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T14:33:05.271919+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"find: '/root/distrib_canary_collapse': No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.87}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T14:33:05.272070+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "find /root/autodl-tmp -maxdepth 2 -name \"distrib_canary_collapse\" -type d",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "find /root/autodl-tmp -maxdepth 2 -name \"distrib_canary_collapse\" -type d",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T14:33:05.272198+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T14:33:05.272344+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "find /root/autodl-tmp/distrib_canary_collapse -name \"5method_leadlag.json\" -path \"*/analysis/*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "find /root/autodl-tmp/distrib_canary_collapse -name \"5method_leadlag.json\" -path \"*/analysis/*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T14:33:05.272497+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/results/intervention/reactive_d1_s43_bf16/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/intervention/predictive_te_s43_bf16/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a010_s43_bf16/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a005_s42_fp32_v3_d080/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a060_s42_fp32_v3_d080/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a010_s43_fp32/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a010_s42_fp32/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42_fp32/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s43_fp32/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s44_fp32/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s42_fp32/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a075_s42_fp32/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s43_fp32/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s44_fp32/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a060_s43_fp32/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a040_s42_fp32/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a030_s42_fp32/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/c4_a075_s42_fp32/analysis/5met
…[truncated 2052 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T14:33:05.272697+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "python3 -c \"\nimport json\nd=json.load(open('/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a045_s42_fp32/analysis/5method_leadlag.json'))\nprint('TOP KEYS:', list(d.keys())[:10])\nprint('threshold_criterion:', d.get('threshold_criterion','MISSING'))\n# get first pair\npairs = d.get('pair_results', d.get('results', {}))\nif isinstance(pairs, dict):\n    pk = list(pairs.keys())[0]\n    print('PAIR:', pk)\n    pr = pairs[pk]\n    if isinstance(pr, dict):\n        mk = list(pr.keys())[0]\n        print('METHOD:', mk)\n        print('METHOD_KEYS:', list(pr[mk].keys()) if isinstance(pr[mk], dict) else type(pr[mk]))\n        print('METHOD_DATA:', json.dumps(pr[mk], indent=2)[:800])\nelif isinstance(pairs, list):\n    print('PAIR_ITEM_KEYS:', list(pairs[0].keys()) if pairs else 'empty')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "python3 -c \"\nimport json\nd=json.load(open('/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a045_s42_fp32/analysis/5method_leadlag.json'))\nprint('TOP KEYS:', list(d.keys())[:10])\nprint('threshold_criterion:', d.get('threshold_criterion','MISSING'))\n# get first pair\npairs = d.get('pair_results', d.get('results', {}))\nif isinstance(pairs, dict):\n    pk = list(pairs.keys())[0]\n    print('PAIR:', pk)\n    pr = pairs[pk]\n    if isinstance(pr, dict):\n        mk = list(pr.keys())[0]\n        print('METHOD:', mk)\n        print('METHOD_KEYS:', list(pr[mk].keys()) if isinstance(pr[mk], dict) else type(pr[mk]))\n        print('METHOD_DATA:', json.dumps(pr[mk], indent=2)[:800])\nelif isinstance(pairs, list):\n    print('PAIR_ITEM_KEYS:', list(pairs[0].keys()) if pairs else 'empty')\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-20T14:33:05.272835+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: python expression contains disallowed call 'open('. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T14:33:05.272961+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "python3 -c \"\nimport json\nd=json.load(open('/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/analysis/5method_leadlag.json'))\nprint('TOP KEYS:', list(d.keys())[:10])\nprint('threshold_criterion:', d.get('threshold_criterion','MISSING'))\npairs = d.get('pair_results', d.get('results', {}))\nif isinstance(pairs, dict):\n    pk = list(pairs.keys())[0]\n    print('PAIR:', pk)\n    pr = pairs[pk]\n    mk = list(pr.keys())[0]\n    print('METHOD:', mk)\n    print('METHOD_KEYS:', list(pr[mk].keys()) if isinstance(pr[mk], dict) else type(pr[mk]))\n    print('METHOD_DATA:', json.dumps(pr[mk], indent=2)[:800])\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "python3 -c \"\nimport json\nd=json.load(open('/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/analysis/5method_leadlag.json'))\nprint('TOP KEYS:', list(d.keys())[:10])\nprint('threshold_criterion:', d.get('threshold_criterion','MISSING'))\npairs = d.get('pair_results', d.get('results', {}))\nif isinstance(pairs, dict):\n    pk = list(pairs.keys())[0]\n    print('PAIR:', pk)\n    pr = pairs[pk]\n    mk = list(pr.keys())[0]\n    print('METHOD:', mk)\n    print('METHOD_KEYS:', list(pr[mk].keys()) if isinstance(pr[mk], dict) else type(pr[mk]))\n    print('METHOD_DATA:', json.dumps(pr[mk], indent=2)[:800])\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T14:33:05.273091+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: python expression contains disallowed call 'open('. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T14:33:05.273221+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "head -100 /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a045_s42_fp32/analysis/5method_leadlag.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "head -100 /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a045_s42_fp32/analysis/5method_leadlag.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T14:33:05.273427+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"meta\\\": {\\n    \\\"alpha\\\": 0.45,\\n    \\\"seed\\\": 42,\\n    \\\"n_gens\\\": 11,\\n    \\\"data_dir\\\": \\\"results/alpha_sweep/a045_s42_fp32\\\",\\n    \\\"methods\\\": [\\n      \\\"naive_xcorr\\\",\\n      \\\"diff_xcorr\\\",\\n      \\\"threshold_onset\\\",\\n      \\\"perm_granger\\\",\\n      \\\"ty_granger\\\"\\n    ],\\n    \\\"n_perm\\\": 5000,\\n    \\\"canaries\\\": [\\n      \\\"token_entropy\\\",\\n      \\\"ece\\\"\\n    ],\\n    \\\"downstreams\\\": [\\n      \\\"distinct_1\\\",\\n      \\\"distinct_2\\\",\\n      \\\"distinct_3\\\",\\n      \\\"mauve\\\"\\n    ],\\n    \\\"threshold_criterion\\\": \\\"true_3sigma_d105\\\"\\n  },\\n  \\\"pairs\\\": [\\n    {\\n      \\\"canary\\\": \\\"token_entropy\\\",\\n      \\\"downstream\\\": \\\"distinct_1\\\",\\n      \\\"forward\\\": {\\n        \\\"naive_xcorr\\\": {\\n          \\\"method\\\": \\\"naive_xcorr\\\",\\n          \\\"peak_lag\\\": 5,\\n          \\\"r\\\": -0.932,\\n          \\\"p_value\\\": 0.006786,\\n          \\\"significant\\\": true,\\n          \\\"all_lags\\\": [\\n            {\\n              \\\"lag\\\": -5,\\n              \\\"r\\\": 0.709,\\n              \\\"p\\\": 0.114668\\n            },\\n            {\\n              \\\"lag\\\": -4,\\n              \\\"r\\\": 0.6994,\\n              \\\"p\\\": 0.080279\\n            },\\n            {\\n              \\\"lag\\\": -3,\\n              \\\"r\\\": 0.7072,\\n              \\\"p\\\": 0.049796\\n            },\\n            {\\n              \\\"lag\\\": -2,\\n              \\\"r\\\": 0.6377,\\n              \\\"p\\\": 0.064669\\n            },\\n            {\\n              \\\"lag\\\": -1,\\n              \\\"r\\\": 0.6871,\\n              \\\"p\\\": 0.028151\\n            },\\n            {\\n              \\\"lag\\\": 0,\\n              \\\"r\\\": 0.4395,\\n              \\\"p\\\": 0.176207\\n            },\\n            {\\n              \\\"lag\\\": 
…[truncated 954 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T14:33:05.273582+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "head -100 /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/analysis/5method_leadlag.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "head -100 /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/analysis/5method_leadlag.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T14:33:05.273761+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"alpha\\\": 0.0,\\n  \\\"seed\\\": 42,\\n  \\\"n_generations\\\": 11,\\n  \\\"data_dir\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42\\\",\\n  \\\"methods\\\": [\\n    \\\"naive_xcorr\\\",\\n    \\\"diff_xcorr\\\",\\n    \\\"threshold_onset\\\",\\n    \\\"perm_granger\\\",\\n    \\\"ty_granger\\\"\\n  ],\\n  \\\"config\\\": {\\n    \\\"n_perm\\\": 5000,\\n    \\\"fdr_alpha\\\": 0.05,\\n    \\\"threshold_criterion\\\": \\\"true_3sigma_d105\\\"\\n  },\\n  \\\"pairs\\\": [\\n    {\\n      \\\"canary\\\": \\\"token_entropy\\\",\\n      \\\"downstream\\\": \\\"distinct_1\\\",\\n      \\\"forward\\\": {\\n        \\\"naive_xcorr\\\": {\\n          \\\"method\\\": \\\"naive_xcorr\\\",\\n          \\\"peak_lag\\\": -5,\\n          \\\"r\\\": 0.9023,\\n          \\\"p_value\\\": 0.013857,\\n          \\\"significant\\\": true,\\n          \\\"all_lags\\\": [\\n            {\\n              \\\"lag\\\": -5,\\n              \\\"r\\\": 0.9023,\\n              \\\"p\\\": 0.013857\\n            },\\n            {\\n              \\\"lag\\\": -4,\\n              \\\"r\\\": 0.7904,\\n              \\\"p\\\": 0.034399\\n            },\\n            {\\n              \\\"lag\\\": -3,\\n              \\\"r\\\": 0.694,\\n              \\\"p\\\": 0.056207\\n            },\\n            {\\n              \\\"lag\\\": -2,\\n              \\\"r\\\": 0.3609,\\n              \\\"p\\\": 0.339995\\n            },\\n            {\\n              \\\"lag\\\": -1,\\n              \\\"r\\\": 0.741,\\n              \\\"p\\\": 0.014202\\n            },\\n            {\\n              \\\"lag\\\": 0,\\n              \\\"r\\\": 0.3702,\\n              \\\"p\\\": 0.262357\\n            },\\n            {\\n              \\\"lag\\\": 1,\\n              \\\"r\\\": -0.8365,\\n              \\\"p\\\": 0.002552\\n            },\\n            {\\n              \\\"lag\\\": 2,\\n              \\\"r\\\": -0.8667,\\
…[truncated 1035 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-20T14:33:05.273945+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "grep -c \"significant_fdr\" /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a045_s42_fp32/analysis/5method_leadlag.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "grep -c \"significant_fdr\" /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a045_s42_fp32/analysis/5method_leadlag.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-20T14:33:05.274077+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"32\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-20T14:33:05.274200+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "grep -c \"significant_fdr\" /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/analysis/5method_leadlag.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "grep -c \"significant_fdr\" /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/analysis/5method_leadlag.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-20T14:33:05.274348+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"32\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T14:33:05.274487+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "grep -A2 \"significant_fdr\" /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a045_s42_fp32/analysis/5method_leadlag.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "grep -A2 \"significant_fdr\" /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a045_s42_fp32/analysis/5method_leadlag.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-20T14:33:05.274607+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "grep -B5 \"significant_fdr\" /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a045_s42_fp32/analysis/5method_leadlag.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "grep -B5 \"significant_fdr\" /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a045_s42_fp32/analysis/5method_leadlag.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-20T14:33:05.274773+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"          \\\"significant_fdr\\\": true\\n        },\\n        \\\"threshold_onset\\\": {\\n--\\n          \\\"significant_fdr\\\": false\\n        },\\n        \\\"ty_granger\\\": {\\n--\\n          \\\"significant_fdr\\\": true\\n        },\\n        \\\"threshold_onset\\\": {\\n--\\n          \\\"significant_fdr\\\": false\\n        },\\n        \\\"ty_granger\\\": {\\n--\\n          \\\"significant_fdr\\\": true\\n        },\\n        \\\"threshold_onset\\\": {\\n--\\n          \\\"significant_fdr\\\": false\\n        },\\n        \\\"ty_granger\\\": {\\n--\\n          \\\"significant_fdr\\\": true\\n        },\\n        \\\"threshold_onset\\\": {\\n--\\n          \\\"significant_fdr\\\": false\\n        },\\n        \\\"ty_granger\\\": {\\n--\\n          \\\"significant_fdr\\\": true\\n        },\\n        \\\"threshold_onset\\\": {\\n--\\n          \\\"significant_fdr\\\": false\\n        },\\n        \\\"ty_granger\\\": {\\n--\\n          \\\"significant_fdr\\\": true\\n        },\\n        \\\"threshold_onset\\\": {\\n--\\n          \\\"significant_fdr\\\": false\\n        },\\n        \\\"ty_granger\\\": {\\n--\\n          \\\"significant_fdr\\\": false\\n        },\\n        \\\"threshold_onset\\\": {\\n--\\n          \\\"significant_fdr\\\": false\\n        },\\n        \\\"ty_granger\\\": {\\n--\\n          \\\"significant_fdr\\\": false\\n        },\\n        \\\"threshold_onset\\\": {\\n--\\n          \\\"significant_fdr\\\": false\\n        },\\n        \\\"ty_granger\\\": {\\n--\\n          \\\"significant_fdr\\\": true\\n        },\\n        \\\"threshold_onset\\\": {\\n--\\n          \\\"significant_fdr\\\": false\\n        },\\n        \\\"ty_granger\\\": {\\n--\\n          \\\"significant_fdr\\\": true\\n        },\\n        \\\"threshold_onset\\\": {\\n--\\n          \\\"significant_fdr\\\": false\\n        },\\n        \\\"ty_granger\\\": {\\n--\\n          \\\"significant_fdr\\\": true\\n
…[truncated 1199 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-20T14:33:05.275029+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"              \\\"r\\\": -0.5904,\\n              \\\"p\\\": 0.294621\\n            }\\n          ],\\n          \\\"p_fdr\\\": 0.007932,\\n          \\\"significant_fdr\\\": true\\n--\\n          \\\"method\\\": \\\"perm_granger\\\",\\n          \\\"f_stat\\\": 82.0863,\\n          \\\"p_value\\\": 0.070186,\\n          \\\"significant\\\": false,\\n          \\\"p_fdr\\\": 0.093581,\\n          \\\"significant_fdr\\\": false\\n--\\n              \\\"r\\\": 0.5595,\\n              \\\"p\\\": 0.326809\\n            }\\n          ],\\n          \\\"p_fdr\\\": 0.007932,\\n          \\\"significant_fdr\\\": true\\n--\\n          \\\"method\\\": \\\"perm_granger\\\",\\n          \\\"f_stat\\\": 1.7494,\\n          \\\"p_value\\\": 0.233353,\\n          \\\"significant\\\": false,\\n          \\\"p_fdr\\\": 0.978804,\\n          \\\"significant_fdr\\\": false\\n--\\n              \\\"r\\\": -0.7048,\\n              \\\"p\\\": 0.18381\\n            }\\n          ],\\n          \\\"p_fdr\\\": 0.027739,\\n          \\\"significant_fdr\\\": true\\n--\\n          \\\"method\\\": \\\"perm_granger\\\",\\n          \\\"f_stat\\\": 118.8267,\\n          \\\"p_value\\\": 0.034193,\\n          \\\"significant\\\": true,\\n          \\\"p_fdr\\\": 0.091181,\\n          \\\"significant_fdr\\\": false\\n--\\n              \\\"r\\\": 0.4587,\\n              \\\"p\\\": 0.437173\\n            }\\n          ],\\n          \\\"p_fdr\\\": 0.027739,\\n          \\\"significant_fdr\\\": true\\n--\\n          \\\"method\\\": \\\"perm_granger\\\",\\n          \\\"f_stat\\\": 0.6308,\\n          \\\"p_value\\\": 0.453709,\\n          \\\"significant\\\": false,\\n          \\\"p_fdr\\\": 0.978804,\\n          \\\"significant_fdr\\\": false\\n--\\n              \\\"r\\\": -0.7416,\\n              \\\"p\\\": 0.151442\\n            }\\n          ],\\n          \\\"p_fdr\\\": 0.037763,\\n          \\\"significant_fdr\\\": true\\n--\\n          
…[truncated 5140 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-20T14:33:05.275208+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "grep -A10 \"threshold_onset\" /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a045_s42_fp32/analysis/5method_leadlag.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "grep -A10 \"threshold_onset\" /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a045_s42_fp32/analysis/5method_leadlag.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-20T14:33:05.275509+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"      \\\"threshold_onset\\\",\\n      \\\"perm_granger\\\",\\n      \\\"ty_granger\\\"\\n    ],\\n    \\\"n_perm\\\": 5000,\\n    \\\"canaries\\\": [\\n      \\\"token_entropy\\\",\\n      \\\"ece\\\"\\n    ],\\n    \\\"downstreams\\\": [\\n      \\\"distinct_1\\\",\\n--\\n        \\\"threshold_onset\\\": {\\n          \\\"method\\\": \\\"threshold_onset\\\",\\n          \\\"canary_onset\\\": 1,\\n          \\\"downstream_onset\\\": null,\\n          \\\"lead_time\\\": null,\\n          \\\"significant\\\": false,\\n          \\\"threshold\\\": \\\"true_3sigma_d105\\\"\\n        },\\n        \\\"perm_granger\\\": {\\n          \\\"method\\\": \\\"perm_granger\\\",\\n          \\\"f_stat\\\": 82.0863,\\n          \\\"p_value\\\": 0.070186,\\n--\\n        \\\"threshold_onset\\\": {\\n          \\\"method\\\": \\\"threshold_onset\\\",\\n          \\\"canary_onset\\\": null,\\n          \\\"downstream_onset\\\": 1,\\n          \\\"lead_time\\\": null,\\n          \\\"significant\\\": false,\\n          \\\"threshold\\\": \\\"true_3sigma_d105\\\"\\n        },\\n        \\\"perm_granger\\\": {\\n          \\\"method\\\": \\\"perm_granger\\\",\\n          \\\"f_stat\\\": 1.7494,\\n          \\\"p_value\\\": 0.233353,\\n--\\n        \\\"threshold_onset\\\": {\\n          \\\"method\\\": \\\"threshold_onset\\\",\\n          \\\"canary_onset\\\": 1,\\n          \\\"downstream_onset\\\": null,\\n          \\\"lead_time\\\": null,\\n          \\\"significant\\\": false,\\n          \\\"threshold\\\": \\\"true_3sigma_d105\\\"\\n        },\\n        \\\"perm_granger\\\": {\\n          \\\"method\\\": \\\"perm_granger\\\",\\n          \\\"f_stat\\\": 118.8267,\\n          \\\"p_value\\\": 0.034193,\\n--\\n        \\\"threshold_onset\\\": {\\n          \\\"method\\\": \\\"threshold_onset\\\",\\n          \\\"canary_onset\\\": null,\\n          \\\"downstream_onset\\\": 1,\\n          \\\"lead_time\\\": null,\\n          \\\"s
…[truncated 6130 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-20T14:33:05.275985+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "cat > /tmp/extract_sig.py << 'PYEOF'\nimport json, os, sys, re\n\nBASE = \"/root/autodl-tmp/distrib_canary_collapse/results\"\nEXCLUDE_PAT = re.compile(r\"v3_d080|postd093|bf16\")\nMETHODS = [\"naive_xcorr\", \"diff_xcorr\", \"threshold_onset\", \"perm_granger\", \"ty_granger\"]\n\nresults = []\nfor root, dirs, files in os.walk(BASE):\n    if \"5method_leadlag.json\" in files and \"analysis\" in root:\n        fpath = os.path.join(root, \"5method_leadlag.json\")\n        exp_dir = os.path.dirname(root)  # parent of analysis/\n        dir_name = os.path.relpath(exp_dir, BASE)\n        \n        if EXCLUDE_PAT.search(dir_name):\n            continue\n        \n        with open(fpath) as f:\n            d = json.load(f)\n        \n        # Extract threshold criterion (different formats)\n        tc = (d.get(\"meta\", {}).get(\"threshold_criterion\") or\n              d.get(\"config\", {}).get(\"threshold_criterion\") or\n              d.get(\"threshold_criterion\", \"UNKNOWN\"))\n        if tc != \"true_3sigma_d105\":\n            continue\n        \n        # Extract alpha and seed\n        alpha = d.get(\"meta\", {}).get(\"alpha\", d.get(\"alpha\"))\n        seed = d.get(\"meta\", {}).get(\"seed\", d.get(\"seed\"))\n        \n        # Extract significance per pair per method\n        pairs_data = {}\n        for pair in d.get(\"pairs\", []):\n            canary = pair[\"canary\"]\n            downstream = pair[\"downstream\"]\n            pair_key = f\"{canary}->{downstream}\"\n            fwd = pair.get(\"forward\", {})\n            \n            method_sigs = {}\n            for m in METHODS:\n                if m not in fwd:\n                    method_sigs[m] = None\n                    continue\n                md = fwd[m]\n                if m == \"threshold_onset\":\n                    method_sigs[m] = md.get(\"significant\", False)\n                else:\n                    method_sigs[m] = md.get(\"significant_fdr\", md.get(\"significant\", False))\n            pairs_data[pair_key] = method_sigs\n        \n        results.append({\n            \"dir\": dir_name,\n            \"alpha\": alpha,\n            \"seed\": seed,\n            \"threshold\": tc,\n            \"pairs\": pairs_data\n        })\n\nresults.sort(key=lambda x: (x[\"alpha\"] or 0, x[\"seed\"] or 0, x[\"dir\"]))\nprint(json.dumps(results, indent=2))\nPYEOF\npython3 /tmp/extract_sig.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat > /tmp/extract_sig.py << 'PYEOF'\nimport json, os, sys, re\n\nBASE = \"/root/autodl-tmp/distrib_canary_collapse/results\"\nEXCLUDE_PAT = re.compile(r\"v3_d080|postd093|bf16\")\nMETHODS = [\"naive_xcorr\", \"diff_xcorr\", \"threshold_onset\", \"perm_granger\", \"ty_granger\"]\n\nresults = []\nfor root, dirs, files in os.walk(BASE):\n    if \"5method_leadlag.json\" in files and \"analysis\" in root:\n        fpath = os.path.join(root, \"5method_leadlag.json\")\n        exp_dir = os.path.dirname(root)  # parent of analysis/\n        dir_name = os.path.relpath(exp_dir, BASE)\n        \n        if EXCLUDE_PAT.search(dir_name):\n            continue\n        \n        with open(fpath) as f:\n            d = json.load(f)\n        \n        # Extract threshold criterion (different formats)\n        tc = (d.get(\"meta\", {}).get(\"threshold_criterion\") or\n              d.get(\"config\", {}).get(\"threshold_criterion\") or\n              d.get(\"threshold_criterion\", \"UNKNOWN\"))\n        if tc != \"true_3sigma_d105\":\n            continue\n        \n        # Extract alpha and seed\n        alpha = d.get(\"meta\", {}).get(\"alpha\", d.get(\"alpha\"))\n        seed = d.get(\"meta\", {}).get(\"seed\", d.get(\"seed\"))\n        \n        # Extract significance per pair per method\n        pairs_data = {}\n        for pair in d.get(\"pairs\", []):\n            canary = pair[\"canary\"]\n            downstream = pair[\"downstream\"]\n            pair_key = f\"{canary}->{downstream}\"\n            fwd = pair.get(\"forward\", {})\n            \n            method_sigs = {}\n            for m in METHODS:\n                if m not in fwd:\n                    method_sigs[m] = None\n                    continue\n                md = fwd[m]\n                if m == \"threshold_onset\":\n                    method_sigs[m] = md.get(\"significant\", False)\n                else:\n                    method_sigs[m] = md.get(\"significant_fdr\", md.get(\"significant\", False))\n            pairs_data[pair_key] = method_sigs\n        \n        results.append({\n            \"dir\": dir_name,\n            \"alpha\": alpha,\n            \"seed\": seed,\n            \"threshold\": tc,\n            \"pairs\": pairs_data\n        })\n\nresults.sort(key=lambda x: (x[\"alpha\"] or 0, x[\"seed\"] or 0, x[\"dir\"]))\nprint(json.dumps(results, indent=2))\nPYEOF\npython3 /tmp/extract_sig.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-20T14:33:05.276501+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[\\n  {\\n    \\\"dir\\\": \\\"alpha_sweep/a000_s42\\\",\\n    \\\"alpha\\\": 0.0,\\n    \\\"seed\\\": 42,\\n    \\\"threshold\\\": \\\"true_3sigma_d105\\\",\\n    \\\"pairs\\\": {\\n      \\\"token_entropy->distinct_1\\\": {\\n        \\\"naive_xcorr\\\": true,\\n        \\\"diff_xcorr\\\": true,\\n        \\\"threshold_onset\\\": false,\\n        \\\"perm_granger\\\": false,\\n        \\\"ty_granger\\\": false\\n      },\\n      \\\"token_entropy->distinct_2\\\": {\\n        \\\"naive_xcorr\\\": true,\\n        \\\"diff_xcorr\\\": true,\\n        \\\"threshold_onset\\\": true,\\n        \\\"perm_granger\\\": false,\\n        \\\"ty_granger\\\": false\\n      },\\n      \\\"token_entropy->distinct_3\\\": {\\n        \\\"naive_xcorr\\\": true,\\n        \\\"diff_xcorr\\\": true,\\n        \\\"threshold_onset\\\": true,\\n        \\\"perm_granger\\\": false,\\n        \\\"ty_granger\\\": false\\n      },\\n      \\\"token_entropy->mauve\\\": {\\n        \\\"naive_xcorr\\\": true,\\n        \\\"diff_xcorr\\\": false,\\n        \\\"threshold_onset\\\": true,\\n        \\\"perm_granger\\\": false,\\n        \\\"ty_granger\\\": false\\n      },\\n      \\\"ece->distinct_1\\\": {\\n        \\\"naive_xcorr\\\": true,\\n        \\\"diff_xcorr\\\": false,\\n        \\\"threshold_onset\\\": false,\\n        \\\"perm_granger\\\": false,\\n        \\\"ty_granger\\\": false\\n      },\\n      \\\"ece->distinct_2\\\": {\\n        \\\"naive_xcorr\\\": true,\\n        \\\"diff_xcorr\\\": false,\\n        \\\"threshold_onset\\\": false,\\n        \\\"perm_granger\\\": false,\\n        \\\"ty_granger\\\": false\\n      },\\n      \\\"ece->distinct_3\\\": {\\n        \\\"naive_xcorr\\\": true,\\n        \\\"diff_xcorr\\\": false,\\n        \\\"threshold_onset\\\": false,\\n        \\\"perm_granger\\\": false,\\n        \\\"ty_granger\\\": true\\n      },\\n      \\\"ece->mauve\\\": {\\n        \\\"naive_xcorr\\\": true,\\n       
…[truncated 8425 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-20T14:33:05.276719+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-17855",
  "command": "cat > /tmp/extract_sig.py << 'PYEOF'\nimport json, os, sys, re\n\nBASE = \"/root/autodl-tmp/distrib_canary_collapse/results\"\nEXCLUDE_PAT = re.compile(r\"v3_d080|postd093|bf16\")\nMETHODS = [\"naive_xcorr\", \"diff_xcorr\", \"threshold_onset\", \"perm_granger\", \"ty_granger\"]\n\nresults = []\nfor root, dirs, files in os.walk(BASE):\n    if \"5method_leadlag.json\" in files and \"analysis\" in root:\n        fpath = os.path.join(root, \"5method_leadlag.json\")\n        exp_dir = os.path.dirname(root)  # parent of analysis/\n        dir_name = os.path.relpath(exp_dir, BASE)\n        \n        if EXCLUDE_PAT.search(dir_name):\n            continue\n        \n        with open(fpath) as f:\n            d = json.load(f)\n        \n        # Extract threshold criterion (different formats)\n        tc = (d.get(\"meta\", {}).get(\"threshold_criterion\") or\n              d.get(\"config\", {}).get(\"threshold_criterion\") or\n              d.get(\"threshold_criterion\", \"UNKNOWN\"))\n        if tc != \"true_3sigma_d105\":\n            continue\n        \n        # Extract alpha and seed\n        alpha = d.get(\"meta\", {}).get(\"alpha\", d.get(\"alpha\"))\n        seed = d.get(\"meta\", {}).get(\"seed\", d.get(\"seed\"))\n        \n        # Extract significance per pair per method\n        pairs_data = {}\n        for pair in d.get(\"pairs\", []):\n            canary = pair[\"canary\"]\n            downstream = pair[\"downstream\"]\n            pair_key = f\"{canary}->{downstream}\"\n            fwd = pair.get(\"forward\", {})\n            \n            method_sigs = {}\n            for m in METHODS:\n                if m not in fwd:\n                    method_sigs[m] = None\n                    continue\n                md = fwd[m]\n                if m == \"threshold_onset\":\n                    method_sigs[m] = md.get(\"significant\", False)\n                else:\n                    method_sigs[m] = md.get(\"significant_fdr\", md.get(\"significant\", False))\n            pairs_data[pair_key] = method_sigs\n        \n        results.append({\n            \"dir\": dir_name,\n            \"alpha\": alpha,\n            \"seed\": seed,\n            \"threshold\": tc,\n            \"pairs\": pairs_data\n        })\n\nresults.sort(key=lambda x: (x[\"alpha\"] or 0, x[\"seed\"] or 0, x[\"dir\"]))\nprint(json.dumps(results, indent=2))\nPYEOF\npython3 /tmp/extract_sig.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-17855",
    "command": "cat > /tmp/extract_sig.py << 'PYEOF'\nimport json, os, sys, re\n\nBASE = \"/root/autodl-tmp/distrib_canary_collapse/results\"\nEXCLUDE_PAT = re.compile(r\"v3_d080|postd093|bf16\")\nMETHODS = [\"naive_xcorr\", \"diff_xcorr\", \"threshold_onset\", \"perm_granger\", \"ty_granger\"]\n\nresults = []\nfor root, dirs, files in os.walk(BASE):\n    if \"5method_leadlag.json\" in files and \"analysis\" in root:\n        fpath = os.path.join(root, \"5method_leadlag.json\")\n        exp_dir = os.path.dirname(root)  # parent of analysis/\n        dir_name = os.path.relpath(exp_dir, BASE)\n        \n        if EXCLUDE_PAT.search(dir_name):\n            continue\n        \n        with open(fpath) as f:\n            d = json.load(f)\n        \n        # Extract threshold criterion (different formats)\n        tc = (d.get(\"meta\", {}).get(\"threshold_criterion\") or\n              d.get(\"config\", {}).get(\"threshold_criterion\") or\n              d.get(\"threshold_criterion\", \"UNKNOWN\"))\n        if tc != \"true_3sigma_d105\":\n            continue\n        \n        # Extract alpha and seed\n        alpha = d.get(\"meta\", {}).get(\"alpha\", d.get(\"alpha\"))\n        seed = d.get(\"meta\", {}).get(\"seed\", d.get(\"seed\"))\n        \n        # Extract significance per pair per method\n        pairs_data = {}\n        for pair in d.get(\"pairs\", []):\n            canary = pair[\"canary\"]\n            downstream = pair[\"downstream\"]\n            pair_key = f\"{canary}->{downstream}\"\n            fwd = pair.get(\"forward\", {})\n            \n            method_sigs = {}\n            for m in METHODS:\n                if m not in fwd:\n                    method_sigs[m] = None\n                    continue\n                md = fwd[m]\n                if m == \"threshold_onset\":\n                    method_sigs[m] = md.get(\"significant\", False)\n                else:\n                    method_sigs[m] = md.get(\"significant_fdr\", md.get(\"significant\", False))\n            pairs_data[pair_key] = method_sigs\n        \n        results.append({\n            \"dir\": dir_name,\n            \"alpha\": alpha,\n            \"seed\": seed,\n            \"threshold\": tc,\n            \"pairs\": pairs_data\n        })\n\nresults.sort(key=lambda x: (x[\"alpha\"] or 0, x[\"seed\"] or 0, x[\"dir\"]))\nprint(json.dumps(results, indent=2))\nPYEOF\npython3 /tmp/extract_sig.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-20T14:33:05.276927+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'cat > /tmp/extract_sig.py << \\\\'PYEOF\\\\'\\\\nimport json, os, sys, re\\\\n\\\\nBASE = \\\"/root/autodl-tmp/distrib_canary_collapse/results\\\"\\\\nEXCLUDE_PAT = re.compile(r\\\"v3_d080|postd093|bf16\\\")\\\\nMETHODS = [\\\"naive_xcorr\\\", \\\"diff_xcorr\\\", \\\"threshold_onset\\\", \\\"perm_granger\\\", \\\"ty_granger\\\"]\\\\n\\\\nresults = []\\\\nfor root, dirs, files in os.walk(BASE):\\\\n    if \\\"5method_leadlag.json\\\" in files and \\\"analysis\\\" in root:\\\\n        fpath = os.path.join(root, \\\"5method_leadlag.json\\\")\\\\n        exp_dir = os.path.dirname(root)  # parent of analysis/\\\\n        dir_name = os.path.relpath(exp_dir, BASE)\\\\n        \\\\n        if EXCLUDE_PAT.search(dir_name):\\\\n            continue\\\\n        \\\\n        with open(fpath) as f:\\\\n            d = json.load(f)\\\\n        \\\\n        # Extract threshold criterion (different formats)\\\\n        tc = (d.get(\\\"meta\\\", {}).get(\\\"threshold_criterion\\\") or\\\\n              d.get(\\\"config\\\", {}).get(\\\"threshold_criterion\\\") or\\\\n              d.get(\\\"threshold_criterion\\\", \\\"UNKNOWN\\\"))\\\\n        if tc != \\\"true_3sigma_d105\\\":\\\\n            continue\\\\n        \\\\n        # Extract alpha and seed\\\\n        alpha = d.get(\\\"meta\\\", {}).get(\\\"alpha\\\", d.get(\\\"alpha\\\"))\\\\n        seed = d.get(\\\"meta\\\", {}).get(\\\"seed\\\", d.get(\\\"seed\\\"))\\\\n        \\\\n        # Extract significance per pair per method\\\\n        pairs_data = {}\\\\n        for pair in d.get(\\\"pairs\\\", []):\\\\n            canary = pair[\\\"canary\\\"]\\\\n            downstream = pair[\\\"downstream\\\"]\\\\n            pair_key = f\\\"{canary}->{downstream}\\\"\\\\n            fwd = pair.get(\\\"forward\\\", {})\\\\n            \\\\n            method_sigs = {}\\\\n            for m in METHODS:\\\\n                if m 
…[truncated 1024 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-20T14:33:05.277113+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-17855",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 /tmp/extract_sig.py",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-17855",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 /tmp/extract_sig.py",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-20T14:33:05.277486+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[\\n  {\\n    \\\"dir\\\": \\\"alpha_sweep/a000_s42_fp32\\\",\\n    \\\"alpha\\\": 0.0,\\n    \\\"seed\\\": 42,\\n    \\\"threshold\\\": \\\"true_3sigma_d105\\\",\\n    \\\"pairs\\\": {\\n      \\\"token_entropy->distinct_1\\\": {\\n        \\\"naive_xcorr\\\": true,\\n        \\\"diff_xcorr\\\": true,\\n        \\\"threshold_onset\\\": false,\\n        \\\"perm_granger\\\": false,\\n        \\\"ty_granger\\\": false\\n      },\\n      \\\"token_entropy->distinct_2\\\": {\\n        \\\"naive_xcorr\\\": true,\\n        \\\"diff_xcorr\\\": true,\\n        \\\"threshold_onset\\\": true,\\n        \\\"perm_granger\\\": false,\\n        \\\"ty_granger\\\": true\\n      },\\n      \\\"token_entropy->distinct_3\\\": {\\n        \\\"naive_xcorr\\\": true,\\n        \\\"diff_xcorr\\\": true,\\n        \\\"threshold_onset\\\": true,\\n        \\\"perm_granger\\\": false,\\n        \\\"ty_granger\\\": false\\n      },\\n      \\\"token_entropy->mauve\\\": {\\n        \\\"naive_xcorr\\\": true,\\n        \\\"diff_xcorr\\\": false,\\n        \\\"threshold_onset\\\": true,\\n        \\\"perm_granger\\\": false,\\n        \\\"ty_granger\\\": false\\n      },\\n      \\\"ece->distinct_1\\\": {\\n        \\\"naive_xcorr\\\": true,\\n        \\\"diff_xcorr\\\": false,\\n        \\\"threshold_onset\\\": false,\\n        \\\"perm_granger\\\": false,\\n        \\\"ty_granger\\\": false\\n      },\\n      \\\"ece->distinct_2\\\": {\\n        \\\"naive_xcorr\\\": true,\\n        \\\"diff_xcorr\\\": false,\\n        \\\"threshold_onset\\\": false,\\n        \\\"perm_granger\\\": false,\\n        \\\"ty_granger\\\": false\\n      },\\n      \\\"ece->distinct_3\\\": {\\n        \\\"naive_xcorr\\\": true,\\n        \\\"diff_xcorr\\\": false,\\n        \\\"threshold_onset\\\": false,\\n        \\\"perm_granger\\\": false,\\n        \\\"ty_granger\\\": false\\n      },\\n      \\\"ece->mauve\\\": {\\n        \\\"naive_xcorr\\\": true,\\n  
…[truncated 8408 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-20T14:33:05.277704+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "python3 /tmp/extract_sig.py > /tmp/data_19828.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "python3 /tmp/extract_sig.py > /tmp/data_19828.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-20T14:33:05.277844+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.48}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-20T14:33:05.277965+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-17855",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 /tmp/extract_sig.py > /tmp/data_17855.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-17855",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 /tmp/extract_sig.py > /tmp/data_17855.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-20T14:33:05.278086+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.55}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-20T14:33:05.278203+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "scp westd-17855:/tmp/data_17855.json /tmp/data_17855.json && scp westd-19828:/tmp/data_19828.json /tmp/data_19828.json && echo \"OK\" && wc -l /tmp/data_17855.json /tmp/data_19828.json",
  "description": "Copy extracted data from both servers to local"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "Bash",
  "tool_args": {
    "command": "scp westd-17855:/tmp/data_17855.json /tmp/data_17855.json && scp westd-19828:/tmp/data_19828.json /tmp/data_19828.json && echo \"OK\" && wc -l /tmp/data_17855.json /tmp/data_19828.json",
    "description": "Copy extracted data from both servers to local"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-20T14:33:05.278351+00:00_

Exit code 255
ssh: Could not resolve hostname westd-17855: Temporary failure in name resolution
scp: Connection closed

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-20T14:33:05.278490+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "which python3 && python3 --version",
  "description": "Check local Python availability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "Bash",
  "tool_args": {
    "command": "which python3 && python3 --version",
    "description": "Check local Python availability"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-20T14:33:05.278607+00:00_

/usr/bin/python3
Python 3.14.4

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-20T14:33:05.278731+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "python3 -c \"\nimport json\nd = json.load(open('/tmp/data_19828.json'))\n# Compact output: one line per experiment\nfor exp in d:\n    print(json.dumps(exp, separators=(',', ':')))\nprint('---END---')\nprint(f'Total: {len(d)} experiments')\n\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "python3 -c \"\nimport json\nd = json.load(open('/tmp/data_19828.json'))\n# Compact output: one line per experiment\nfor exp in d:\n    print(json.dumps(exp, separators=(',', ':')))\nprint('---END---')\nprint(f'Total: {len(d)} experiments')\n\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-20T14:33:05.279101+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"dir\\\":\\\"alpha_sweep/a000_s42\\\",\\\"alpha\\\":0.0,\\\"seed\\\":42,\\\"threshold\\\":\\\"true_3sigma_d105\\\",\\\"pairs\\\":{\\\"token_entropy->distinct_1\\\":{\\\"naive_xcorr\\\":true,\\\"diff_xcorr\\\":true,\\\"threshold_onset\\\":false,\\\"perm_granger\\\":false,\\\"ty_granger\\\":false},\\\"token_entropy->distinct_2\\\":{\\\"naive_xcorr\\\":true,\\\"diff_xcorr\\\":true,\\\"threshold_onset\\\":true,\\\"perm_granger\\\":false,\\\"ty_granger\\\":false},\\\"token_entropy->distinct_3\\\":{\\\"naive_xcorr\\\":true,\\\"diff_xcorr\\\":true,\\\"threshold_onset\\\":true,\\\"perm_granger\\\":false,\\\"ty_granger\\\":false},\\\"token_entropy->mauve\\\":{\\\"naive_xcorr\\\":true,\\\"diff_xcorr\\\":false,\\\"threshold_onset\\\":true,\\\"perm_granger\\\":false,\\\"ty_granger\\\":false},\\\"ece->distinct_1\\\":{\\\"naive_xcorr\\\":true,\\\"diff_xcorr\\\":false,\\\"threshold_onset\\\":false,\\\"perm_granger\\\":false,\\\"ty_granger\\\":false},\\\"ece->distinct_2\\\":{\\\"naive_xcorr\\\":true,\\\"diff_xcorr\\\":false,\\\"threshold_onset\\\":false,\\\"perm_granger\\\":false,\\\"ty_granger\\\":false},\\\"ece->distinct_3\\\":{\\\"naive_xcorr\\\":true,\\\"diff_xcorr\\\":false,\\\"threshold_onset\\\":false,\\\"perm_granger\\\":false,\\\"ty_granger\\\":true},\\\"ece->mauve\\\":{\\\"naive_xcorr\\\":true,\\\"diff_xcorr\\\":true,\\\"threshold_onset\\\":false,\\\"perm_granger\\\":false,\\\"ty_granger\\\":false}}}\\n{\\\"dir\\\":\\\"alpha_sweep/a000_s43\\\",\\\"alpha\\\":0.0,\\\"seed\\\":43,\\\"threshold\\\":\\\"true_3sigma_d105\\\",\\\"pairs\\\":{\\\"token_entropy->distinct_1\\\":{\\\"naive_xcorr\\\":true,\\\"diff_xcorr\\\":false,\\\"threshold_onset\\\":false,\\\"perm_granger\\\":false,\\\"ty_granger\\\":true},\\\"token_entropy->distinct_2\\\":{\\\"naive_xcorr\\\":true,\\\"diff_xcorr\\\":true,\\\"threshold_onset\\\":false,\\\"perm_granger\\\":false,\\\"ty_granger\\\":false},\\\"token_entropy->distinct_3\\\":{\\\"naive_xcorr\\
…[truncated 8626 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-20T14:33:05.279318+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-17855",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json\nd = json.load(open('/tmp/data_17855.json'))\nfor exp in d:\n    print(json.dumps(exp, separators=(',', ':')))\nprint('---END---')\nprint(f'Total: {len(d)} experiments')\n\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-17855",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json\nd = json.load(open('/tmp/data_17855.json'))\nfor exp in d:\n    print(json.dumps(exp, separators=(',', ':')))\nprint('---END---')\nprint(f'Total: {len(d)} experiments')\n\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-20T14:33:05.279718+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"dir\\\":\\\"alpha_sweep/a000_s42_fp32\\\",\\\"alpha\\\":0.0,\\\"seed\\\":42,\\\"threshold\\\":\\\"true_3sigma_d105\\\",\\\"pairs\\\":{\\\"token_entropy->distinct_1\\\":{\\\"naive_xcorr\\\":true,\\\"diff_xcorr\\\":true,\\\"threshold_onset\\\":false,\\\"perm_granger\\\":false,\\\"ty_granger\\\":false},\\\"token_entropy->distinct_2\\\":{\\\"naive_xcorr\\\":true,\\\"diff_xcorr\\\":true,\\\"threshold_onset\\\":true,\\\"perm_granger\\\":false,\\\"ty_granger\\\":true},\\\"token_entropy->distinct_3\\\":{\\\"naive_xcorr\\\":true,\\\"diff_xcorr\\\":true,\\\"threshold_onset\\\":true,\\\"perm_granger\\\":false,\\\"ty_granger\\\":false},\\\"token_entropy->mauve\\\":{\\\"naive_xcorr\\\":true,\\\"diff_xcorr\\\":false,\\\"threshold_onset\\\":true,\\\"perm_granger\\\":false,\\\"ty_granger\\\":false},\\\"ece->distinct_1\\\":{\\\"naive_xcorr\\\":true,\\\"diff_xcorr\\\":false,\\\"threshold_onset\\\":false,\\\"perm_granger\\\":false,\\\"ty_granger\\\":false},\\\"ece->distinct_2\\\":{\\\"naive_xcorr\\\":true,\\\"diff_xcorr\\\":false,\\\"threshold_onset\\\":false,\\\"perm_granger\\\":false,\\\"ty_granger\\\":false},\\\"ece->distinct_3\\\":{\\\"naive_xcorr\\\":true,\\\"diff_xcorr\\\":false,\\\"threshold_onset\\\":false,\\\"perm_granger\\\":false,\\\"ty_granger\\\":false},\\\"ece->mauve\\\":{\\\"naive_xcorr\\\":true,\\\"diff_xcorr\\\":true,\\\"threshold_onset\\\":false,\\\"perm_granger\\\":false,\\\"ty_granger\\\":false}}}\\n{\\\"dir\\\":\\\"alpha_sweep/a010_s42_fp32\\\",\\\"alpha\\\":0.1,\\\"seed\\\":42,\\\"threshold\\\":\\\"true_3sigma_d105\\\",\\\"pairs\\\":{\\\"token_entropy->distinct_1\\\":{\\\"naive_xcorr\\\":true,\\\"diff_xcorr\\\":true,\\\"threshold_onset\\\":false,\\\"perm_granger\\\":false,\\\"ty_granger\\\":false},\\\"token_entropy->distinct_2\\\":{\\\"naive_xcorr\\\":true,\\\"diff_xcorr\\\":true,\\\"threshold_onset\\\":false,\\\"perm_granger\\\":false,\\\"ty_granger\\\":false},\\\"token_entropy->distinct_3\\\":{\\\"nai
…[truncated 8602 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-20T14:33:05.279967+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "cat > /tmp/shapley_v3.py << 'PYEOF'\nimport json, os, sys\nfrom math import factorial\nfrom itertools import combinations\nfrom datetime import datetime\n\n# ============== DATA LOADING ==============\ndata_19828 = json.load(open('/tmp/data_19828.json'))\ndata_17855 = json.load(open('/tmp/data_17855.json'))\n\n# Tag with server\nfor exp in data_19828:\n    exp['server'] = '19828'\n    exp['source'] = f\"19828:{exp['dir']}\"\nfor exp in data_17855:\n    exp['server'] = '17855'\n    exp['source'] = f\"17855:{exp['dir']}\"\n\nall_exps = data_19828 + data_17855\n\n# ============== DEDUP ==============\n# For alpha_sweep experiments with same (alpha, seed) on both servers,\n# prefer 17855 fp32\n\ndef extract_alpha_seed_key(exp):\n    \"\"\"For alpha_sweep experiments, extract (alpha, seed) dedup key.\"\"\"\n    d = exp['dir']\n    if not d.startswith('alpha_sweep/'):\n        return None\n    return (exp['alpha'], exp['seed'])\n\n# Build index of alpha_sweep experiments by (alpha, seed)\ndedup_map = {}  # (alpha, seed) -> list of exps\nfor exp in all_exps:\n    key = extract_alpha_seed_key(exp)\n    if key is not None:\n        dedup_map.setdefault(key, []).append(exp)\n\n# Resolve duplicates\nkeep_sources = set()\nfor key, exps in dedup_map.items():\n    if len(exps) == 1:\n        keep_sources.add(exps[0]['source'])\n    else:\n        # Multiple experiments for same (alpha, seed)\n        # Prefer 17855 fp32\n        has_17855 = [e for e in exps if e['server'] == '17855']\n        has_19828 = [e for e in exps if e['server'] == '19828']\n        if has_17855:\n            keep_sources.add(has_17855[0]['source'])\n        else:\n            keep_sources.add(has_19828[0]['source'])\n\n# For non alpha_sweep experiments, keep all (no dedup needed)\nfor exp in all_exps:\n    key = extract_alpha_seed_key(exp)\n    if key is None:\n        keep_sources.add(exp['source'])\n\n# Filter\nclean_exps = [e for e in all_exps if e['source'] in keep_sources]\nclean_exps.sort(key=lambda x: (x['alpha'] or 0, x['seed'] or 0, x['source']))\n\n# ============== VERIFICATION ==============\n# Check no v3_d080/postd093/bf16 (should already be excluded by extraction)\nimport re\nfor e in clean_exps:\n    assert not re.search(r'v3_d080|postd093|bf16', e['dir']), f\"Non-standard variant: {e['source']}\"\n\n# Check alpha=0.00 seed=42 only once\nnull_s42 = [e for e in clean_exps if e['alpha'] == 0.0 and e['seed'] == 42\n            and e['dir'].startswith('alpha_sweep/')]\nassert len(null_s42) == 1, f\"alpha=0.00 seed=42 dedup failed: {[e['source'] for e in null_s42]}\"\nprint(f\"alpha=0.00 seed=42 dedup: kept {null_s42[0]['source']}\", file=sys.stderr)\n\n# ============== CLASSIFY EXPERIMENTS ==============\nPAIRS_8 = [\n    \"token_entropy->distinct_1\", \"token_entropy->distinct_2\",\n    \"token_entropy->distinct_3\", \"token_entropy->mauve\",\n    \"ece->distinct_1\", \"ece->distinct_2\",\n    \"ece->distinct_3\", \"ece->mauve\"\n]\nPAIRS_6 = [p for p in PAIRS_8 if \"mauve\" not in p]\nMETHODS = [\"naive_xcorr\", \"diff_xcorr\", \"threshold_onset\", \"perm_granger\", \"ty_granger\"]\nN = len(METHODS)\n\nnull_exps = [e for e in clean_exps if e['alpha'] == 0.0]\nsignal_exps = [e for e in clean_exps if e['alpha'] is not None and e['alpha'] > 0]\n\nprint(f\"Null experiments: {len(null_exps)}\", file=sys.stderr)\nprint(f\"Signal experiments: {len(signal_exps)}\", file=sys.stderr)\nprint(f\"Total clean experiments: {len(clean_exps)}\", file=sys.stderr)\n\n# ============== COALITION VALUE FUNCTIONS ==============\n\ndef fpr_value(coalition, null_exps, pairs):\n    \"\"\"FP rate: fraction of (exp, pair) where any method in coalition fires.\"\"\"\n    if not coalition:\n        return 0.0\n    total = 0\n    fp = 0\n    for exp in null_exps:\n        for pair in pairs:\n            if pair not in exp['pairs']:\n                continue\n            total += 1\n            sigs = exp['pairs'][pair]\n            if any(sigs.get(m, False) for m in coalition):\n                fp += 1\n    return fp / total if total > 0 else 0.0\n\ndef fnr_value(coalition, signal_exps, pairs):\n    \"\"\"FN rate: fraction of (exp, pair) where no method in coalition fires.\"\"\"\n    if not coalition:\n        return 1.0\n    total = 0\n    fn = 0\n    for exp in signal_exps:\n        for pair in pairs:\n            if pair not in exp['pairs']:\n                continue\n            total += 1\n            sigs = exp['pairs'][pair]\n            if not any(sigs.get(m, False) for m in coalition):\n                fn += 1\n    return fn / total if total > 0 else 1.0\n\n# ============== SHAPLEY COMPUTATION ==============\n\ndef compute_shapley(value_func, exps, pairs):\n    \"\"\"Compute Shapley values for all methods using exact enumeration.\"\"\"\n    shapley = {m: 0.0 for m in METHODS}\n    \n    for i, method in enumerate(METHODS):\n        others = [m for m in METHODS if m != method]\n        phi = 0.0\n        for s_size in range(N):\n            # All subsets of size s_size from others\n            weight = factorial(s_size) * factorial(N - s_size - 1) / factorial(N)\n            for subset in combinations(others, s_size):\n                s_list = list(subset)\n                v_with = value_func(s_list + [method], exps, pairs)\n                v_without = value_func(s_list, exps, pairs)\n                phi += weight * (v_with - v_without)\n        shapley[method] = round(phi, 6)\n    \n    return shapley\n\nprint(\"Computing FPR Shapley (8-pair)...\", file=sys.stderr)\nfpr_shapley = compute_shapley(fpr_value, null_exps, PAIRS_8)\n\nprint(\"Computing FNR Shapley (6-pair)...\", file=sys.stderr)\nfnr_shapley_6 = compute_shapley(fnr_value, signal_exps, PAIRS_6)\n\nprint(\"Computing FNR Shapley (8-pair)...\", file=sys.stderr)\nfnr_shapley_8 = compute_shapley(fnr_value, signal_exps, PAIRS_8)\n\n# Combined = FPR + FNR (both to be minimized)\ncombined_6 = {m: round(fpr_shapley[m] + fnr_shapley_6[m], 6) for m in METHODS}\ncombined_8 = {m: round(fpr_shapley[m] + fnr_shapley_8[m], 6) for m in METHODS}\n\n# ============== RAW RATES ==============\n# Compute raw FPR and FNR per method (for diagnostics)\ndef raw_rates(null_exps, signal_exps, pairs, pairs_label):\n    \"\"\"Compute per-method FP/FN rates.\"\"\"\n    rates = {}\n    for m in METHODS:\n        # FPR\n        fp_total = fp_count = 0\n        for exp in null_exps:\n            for pair in pairs:\n                if pair not in exp['pairs']:\n                    continue\n                fp_total += 1\n                if exp['pairs'][pair].get(m, False):\n                    fp_count += 1\n        \n        # FNR\n        fn_total = fn_count = 0\n        for exp in signal_exps:\n            for pair in pairs:\n                if pair not in exp['pairs']:\n                    continue\n                fn_total += 1\n                if not exp['pairs'][pair].get(m, False):\n                    fn_count += 1\n        \n        rates[m] = {\n            \"fpr\": round(fp_count / fp_total, 4) if fp_total > 0 else 0,\n            \"fnr\": round(fn_count / fn_total, 4) if fn_total > 0 else 0,\n            \"fp_count\": fp_count,\n            \"fp_total\": fp_total,\n            \"fn_count\": fn_count,\n            \"fn_total\": fn_total\n        }\n    return rates\n\nraw_8 = raw_rates(null_exps, signal_exps, PAIRS_8, \"8pair\")\n\n# ============== OUTPUT ==============\nn_null_obs = sum(1 for e in null_exps for p in PAIRS_8 if p in e['pairs'])\nn_signal_obs_6 = sum(1 for e in signal_exps for p in PAIRS_6 if p in e['pairs'])\nn_signal_obs_8 = sum(1 for e in signal_exps for p in PAIRS_8 if p in e['pairs'])\n\nresult = {\n    \"version\": \"v3_dedup_fdr\",\n    \"generated_at\": datetime.utcnow().isoformat(),\n    \"data_sources\": sorted([e['source'] for e in clean_exps]),\n    \"dedup_rules\": [\n        \"exclude dir names matching v3_d080|postd093|bf16\",\n        \"same (alpha, seed) in alpha_sweep: prefer westd-17855 fp32\",\n        \"only true_3sigma_d105 threshold\"\n    ],\n    \"fdr_field_used\": {\n        \"naive_xcorr\": \"significant_fdr\",\n        \"diff_xcorr\": \"significant_fdr\",\n        \"threshold_onset\": \"significant (deterministic, no p-value)\",\n        \"perm_granger\": \"significant_fdr\",\n        \"ty_granger\": \"significant_fdr\"\n    },\n    \"threshold_criterion\": \"true_3sigma_d105\",\n    \"n_methods\": 5,\n    \"n_coalitions\": 32,\n    \"n_null_experiments\": len(null_exps),\n    \"n_signal_experiments\": len(signal_exps),\n    \"n_null_obs\": n_null_obs,\n    \"n_signal_obs_6pair\": n_signal_obs_6,\n    \"n_signal_obs_8pair\": n_signal_obs_8,\n    \"fpr_pairs\": PAIRS_8,\n    \"fnr_pairs_6\": PAIRS_6,\n    \"fnr_pairs_8\": PAIRS_8,\n    \"methods\": METHODS,\n    \"main_result_6pair\": {\n        \"fpr_shapley\": fpr_shapley,\n        \"fnr_shapley\": fnr_shapley_6,\n        \"combined_shapley\": combined_6\n    },\n    \"robustness_8pair\": {\n        \"fpr_shapley\": fpr_shapley,\n        \"fnr_shapley\": fnr_shapley_8,\n        \"combined_shapley\": combined_8\n    },\n    \"raw_rates_8pair\": raw_8,\n    \"diagnostics\": {\n        \"null_s42_source\": null_s42[0]['source'],\n        \"excluded_from_v2\": [\n            \"17855:alpha_sweep/a005_s42_fp32_v3_d080\",\n            \"17855:alpha_sweep/a060_s42_fp32_v3_d080\",\n            \"17855:alpha_sweep/a050_postd093_s42_fp32\",\n            \"17855:generalize/gpt2m_wiki_a100_s43_bf16\",\n            \"19828:alpha_sweep/a060_s42_bf16 (was not in v2 but excluded from scan)\"\n        ],\n        \"deduped_from_v2\": {\n            \"19828:alpha_sweep/a000_s42\": \"replaced by 17855:alpha_sweep/a000_s42_fp32\",\n            \"19828:alpha_sweep/a010_s42\": \"replaced by 17855:alpha_sweep/a010_s42_fp32\",\n            \"19828:alpha_sweep/a025_s43\": \"replaced by 17855:alpha_sweep/a025_s43_fp32\",\n            \"19828:alpha_sweep/a025_s44\": \"replaced by 17855:alpha_sweep/a025_s44_fp32\",\n            \"19828:alpha_sweep/a050_s42\": \"replaced by 17855:alpha_sweep/a050_s42_fp32\",\n            \"19828:alpha_sweep/a050_s43\": \"replaced by 17855:alpha_sweep/a050_s43_fp32\",\n            \"19828:alpha_sweep/a050_s44\": \"replaced by 17855:alpha_sweep/a050_s44_fp32\",\n            \"19828:alpha_sweep/a075_s42\": \"replaced by 17855:alpha_sweep/a075_s42_fp32\"\n        }\n    }\n}\n\n# Verify perm_granger FPR contribution ~ 0\nprint(f\"\\nVerification:\", file=sys.stderr)\nprint(f\"  perm_granger FPR Shapley: {fpr_shapley['perm_granger']}\", file=sys.stderr)\nprint(f\"  perm_granger raw FPR: {raw_8['perm_granger']['fpr']} ({raw_8['perm_granger']['fp_count']}/{raw_8['perm_granger']['fp_total']})\", file=sys.stderr)\n\n# Shapley sum check (should equal v(grand coalition) - v(empty))\nfpr_grand = fpr_value(METHODS, null_exps, PAIRS_8)\nfpr_empty = fpr_value([], null_exps, PAIRS_8)\nprint(f\"  FPR: grand={fpr_grand:.4f}, empty={fpr_empty:.4f}, sum_shapley={sum(fpr_shapley.values()):.6f}\", file=sys.stderr)\n\nfnr_grand_6 = fnr_value(METHODS, signal_exps, PAIRS_6)\nfnr_empty_6 = fnr_value([], signal_exps, PAIRS_6)\nprint(f\"  FNR(6): grand={fnr_grand_6:.4f}, empty={fnr_empty_6:.4f}, sum_shapley={sum(fnr_shapley_6.values()):.6f}\", file=sys.stderr)\n\nprint(json.dumps(result, indent=2))\nPYEOF\necho \"Script written OK\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat > /tmp/shapley_v3.py << 'PYEOF'\nimport json, os, sys\nfrom math import factorial\nfrom itertools import combinations\nfrom datetime import datetime\n\n# ============== DATA LOADING ==============\ndata_19828 = json.load(open('/tmp/data_19828.json'))\ndata_17855 = json.load(open('/tmp/data_17855.json'))\n\n# Tag with server\nfor exp in data_19828:\n    exp['server'] = '19828'\n    exp['source'] = f\"19828:{exp['dir']}\"\nfor exp in data_17855:\n    exp['server'] = '17855'\n    exp['source'] = f\"17855:{exp['dir']}\"\n\nall_exps = data_19828 + data_17855\n\n# ============== DEDUP ==============\n# For alpha_sweep experiments with same (alpha, seed) on both servers,\n# prefer 17855 fp32\n\ndef extract_alpha_seed_key(exp):\n    \"\"\"For alpha_sweep experiments, extract (alpha, seed) dedup key.\"\"\"\n    d = exp['dir']\n    if not d.startswith('alpha_sweep/'):\n        return None\n    return (exp['alpha'], exp['seed'])\n\n# Build index of alpha_sweep experiments by (alpha, seed)\ndedup_map = {}  # (alpha, seed) -> list of exps\nfor exp in all_exps:\n    key = extract_alpha_seed_key(exp)\n    if key is not None:\n        dedup_map.setdefault(key, []).append(exp)\n\n# Resolve duplicates\nkeep_sources = set()\nfor key, exps in dedup_map.items():\n    if len(exps) == 1:\n        keep_sources.add(exps[0]['source'])\n    else:\n        # Multiple experiments for same (alpha, seed)\n        # Prefer 17855 fp32\n        has_17855 = [e for e in exps if e['server'] == '17855']\n        has_19828 = [e for e in exps if e['server'] == '19828']\n        if has_17855:\n            keep_sources.add(has_17855[0]['source'])\n        else:\n            keep_sources.add(has_19828[0]['source'])\n\n# For non alpha_sweep experiments, keep all (no dedup needed)\nfor exp in all_exps:\n    key = extract_alpha_seed_key(exp)\n    if key is None:\n        keep_sources.add(exp['source'])\n\n# Filter\nclean_exps = [e for e in all_exps if e['source'] in keep_sources]\nclean_exps.sort(key=lambda x: (x['alpha'] or 0, x['seed'] or 0, x['source']))\n\n# ============== VERIFICATION ==============\n# Check no v3_d080/postd093/bf16 (should already be excluded by extraction)\nimport re\nfor e in clean_exps:\n    assert not re.search(r'v3_d080|postd093|bf16', e['dir']), f\"Non-standard variant: {e['source']}\"\n\n# Check alpha=0.00 seed=42 only once\nnull_s42 = [e for e in clean_exps if e['alpha'] == 0.0 and e['seed'] == 42\n            and e['dir'].startswith('alpha_sweep/')]\nassert len(null_s42) == 1, f\"alpha=0.00 seed=42 dedup failed: {[e['source'] for e in null_s42]}\"\nprint(f\"alpha=0.00 seed=42 dedup: kept {null_s42[0]['source']}\", file=sys.stderr)\n\n# ============== CLASSIFY EXPERIMENTS ==============\nPAIRS_8 = [\n    \"token_entropy->distinct_1\", \"token_entropy->distinct_2\",\n    \"token_entropy->distinct_3\", \"token_entropy->mauve\",\n    \"ece->distinct_1\", \"ece->distinct_2\",\n    \"ece->distinct_3\", \"ece->mauve\"\n]\nPAIRS_6 = [p for p in PAIRS_8 if \"mauve\" not in p]\nMETHODS = [\"naive_xcorr\", \"diff_xcorr\", \"threshold_onset\", \"perm_granger\", \"ty_granger\"]\nN = len(METHODS)\n\nnull_exps = [e for e in clean_exps if e['alpha'] == 0.0]\nsignal_exps = [e for e in clean_exps if e['alpha'] is not None and e['alpha'] > 0]\n\nprint(f\"Null experiments: {len(null_exps)}\", file=sys.stderr)\nprint(f\"Signal experiments: {len(signal_exps)}\", file=sys.stderr)\nprint(f\"Total clean experiments: {len(clean_exps)}\", file=sys.stderr)\n\n# ============== COALITION VALUE FUNCTIONS ==============\n\ndef fpr_value(coalition, null_exps, pairs):\n    \"\"\"FP rate: fraction of (exp, pair) where any method in coalition fires.\"\"\"\n    if not coalition:\n        return 0.0\n    total = 0\n    fp = 0\n    for exp in null_exps:\n        for pair in pairs:\n            if pair not in exp['pairs']:\n                continue\n            total += 1\n            sigs = exp['pairs'][pair]\n            if any(sigs.get(m, False) for m in coalition):\n                fp += 1\n    return fp / total if total > 0 else 0.0\n\ndef fnr_value(coalition, signal_exps, pairs):\n    \"\"\"FN rate: fraction of (exp, pair) where no method in coalition fires.\"\"\"\n    if not coalition:\n        return 1.0\n    total = 0\n    fn = 0\n    for exp in signal_exps:\n        for pair in pairs:\n            if pair not in exp['pairs']:\n                continue\n            total += 1\n            sigs = exp['pairs'][pair]\n            if not any(sigs.get(m, False) for m in coalition):\n                fn += 1\n    return fn / total if total > 0 else 1.0\n\n# ============== SHAPLEY COMPUTATION ==============\n\ndef compute_shapley(value_func, exps, pairs):\n    \"\"\"Compute Shapley values for all methods using exact enumeration.\"\"\"\n    shapley = {m: 0.0 for m in METHODS}\n    \n    for i, method in enumerate(METHODS):\n        others = [m for m in METHODS if m != method]\n        phi = 0.0\n        for s_size in range(N):\n            # All subsets of size s_size from others\n            weight = factorial(s_size) * factorial(N - s_size - 1) / factorial(N)\n            for subset in combinations(others, s_size):\n                s_list = list(subset)\n                v_with = value_func(s_list + [method], exps, pairs)\n                v_without = value_func(s_list, exps, pairs)\n                phi += weight * (v_with - v_without)\n        shapley[method] = round(phi, 6)\n    \n    return shapley\n\nprint(\"Computing FPR Shapley (8-pair)...\", file=sys.stderr)\nfpr_shapley = compute_shapley(fpr_value, null_exps, PAIRS_8)\n\nprint(\"Computing FNR Shapley (6-pair)...\", file=sys.stderr)\nfnr_shapley_6 = compute_shapley(fnr_value, signal_exps, PAIRS_6)\n\nprint(\"Computing FNR Shapley (8-pair)...\", file=sys.stderr)\nfnr_shapley_8 = compute_shapley(fnr_value, signal_exps, PAIRS_8)\n\n# Combined = FPR + FNR (both to be minimized)\ncombined_6 = {m: round(fpr_shapley[m] + fnr_shapley_6[m], 6) for m in METHODS}\ncombined_8 = {m: round(fpr_shapley[m] + fnr_shapley_8[m], 6) for m in METHODS}\n\n# ============== RAW RATES ==============\n# Compute raw FPR and FNR per method (for diagnostics)\ndef raw_rates(null_exps, signal_exps, pairs, pairs_label):\n    \"\"\"Compute per-method FP/FN rates.\"\"\"\n    rates = {}\n    for m in METHODS:\n        # FPR\n        fp_total = fp_count = 0\n        for exp in null_exps:\n            for pair in pairs:\n                if pair not in exp['pairs']:\n                    continue\n                fp_total += 1\n                if exp['pairs'][pair].get(m, False):\n                    fp_count += 1\n        \n        # FNR\n        fn_total = fn_count = 0\n        for exp in signal_exps:\n            for pair in pairs:\n                if pair not in exp['pairs']:\n                    continue\n                fn_total += 1\n                if not exp['pairs'][pair].get(m, False):\n                    fn_count += 1\n        \n        rates[m] = {\n            \"fpr\": round(fp_count / fp_total, 4) if fp_total > 0 else 0,\n            \"fnr\": round(fn_count / fn_total, 4) if fn_total > 0 else 0,\n            \"fp_count\": fp_count,\n            \"fp_total\": fp_total,\n            \"fn_count\": fn_count,\n            \"fn_total\": fn_total\n        }\n    return rates\n\nraw_8 = raw_rates(null_exps, signal_exps, PAIRS_8, \"8pair\")\n\n# ============== OUTPUT ==============\nn_null_obs = sum(1 for e in null_exps for p in PAIRS_8 if p in e['pairs'])\nn_signal_obs_6 = sum(1 for e in signal_exps for p in PAIRS_6 if p in e['pairs'])\nn_signal_obs_8 = sum(1 for e in signal_exps for p in PAIRS_8 if p in e['pairs'])\n\nresult = {\n    \"version\": \"v3_dedup_fdr\",\n    \"generated_at\": datetime.utcnow().isoformat(),\n    \"data_sources\": sorted([e['source'] for e in clean_exps]),\n    \"dedup_rules\": [\n        \"exclude dir names matching v3_d080|postd093|bf16\",\n        \"same (alpha, seed) in alpha_sweep: prefer westd-17855 fp32\",\n        \"only true_3sigma_d105 threshold\"\n    ],\n    \"fdr_field_used\": {\n        \"naive_xcorr\": \"significant_fdr\",\n        \"diff_xcorr\": \"significant_fdr\",\n        \"threshold_onset\": \"significant (deterministic, no p-value)\",\n        \"perm_granger\": \"significant_fdr\",\n        \"ty_granger\": \"significant_fdr\"\n    },\n    \"threshold_criterion\": \"true_3sigma_d105\",\n    \"n_methods\": 5,\n    \"n_coalitions\": 32,\n    \"n_null_experiments\": len(null_exps),\n    \"n_signal_experiments\": len(signal_exps),\n    \"n_null_obs\": n_null_obs,\n    \"n_signal_obs_6pair\": n_signal_obs_6,\n    \"n_signal_obs_8pair\": n_signal_obs_8,\n    \"fpr_pairs\": PAIRS_8,\n    \"fnr_pairs_6\": PAIRS_6,\n    \"fnr_pairs_8\": PAIRS_8,\n    \"methods\": METHODS,\n    \"main_result_6pair\": {\n        \"fpr_shapley\": fpr_shapley,\n        \"fnr_shapley\": fnr_shapley_6,\n        \"combined_shapley\": combined_6\n    },\n    \"robustness_8pair\": {\n        \"fpr_shapley\": fpr_shapley,\n        \"fnr_shapley\": fnr_shapley_8,\n        \"combined_shapley\": combined_8\n    },\n    \"raw_rates_8pair\": raw_8,\n    \"diagnostics\": {\n        \"null_s42_source\": null_s42[0]['source'],\n        \"excluded_from_v2\": [\n            \"17855:alpha_sweep/a005_s42_fp32_v3_d080\",\n            \"17855:alpha_sweep/a060_s42_fp32_v3_d080\",\n            \"17855:alpha_sweep/a050_postd093_s42_fp32\",\n            \"17855:generalize/gpt2m_wiki_a100_s43_bf16\",\n            \"19828:alpha_sweep/a060_s42_bf16 (was not in v2 but excluded from scan)\"\n        ],\n        \"deduped_from_v2\": {\n            \"19828:alpha_sweep/a000_s42\": \"replaced by 17855:alpha_sweep/a000_s42_fp32\",\n            \"19828:alpha_sweep/a010_s42\": \"replaced by 17855:alpha_sweep/a010_s42_fp32\",\n            \"19828:alpha_sweep/a025_s43\": \"replaced by 17855:alpha_sweep/a025_s43_fp32\",\n            \"19828:alpha_sweep/a025_s44\": \"replaced by 17855:alpha_sweep/a025_s44_fp32\",\n            \"19828:alpha_sweep/a050_s42\": \"replaced by 17855:alpha_sweep/a050_s42_fp32\",\n            \"19828:alpha_sweep/a050_s43\": \"replaced by 17855:alpha_sweep/a050_s43_fp32\",\n            \"19828:alpha_sweep/a050_s44\": \"replaced by 17855:alpha_sweep/a050_s44_fp32\",\n            \"19828:alpha_sweep/a075_s42\": \"replaced by 17855:alpha_sweep/a075_s42_fp32\"\n        }\n    }\n}\n\n# Verify perm_granger FPR contribution ~ 0\nprint(f\"\\nVerification:\", file=sys.stderr)\nprint(f\"  perm_granger FPR Shapley: {fpr_shapley['perm_granger']}\", file=sys.stderr)\nprint(f\"  perm_granger raw FPR: {raw_8['perm_granger']['fpr']} ({raw_8['perm_granger']['fp_count']}/{raw_8['perm_granger']['fp_total']})\", file=sys.stderr)\n\n# Shapley sum check (should equal v(grand coalition) - v(empty))\nfpr_grand = fpr_value(METHODS, null_exps, PAIRS_8)\nfpr_empty = fpr_value([], null_exps, PAIRS_8)\nprint(f\"  FPR: grand={fpr_grand:.4f}, empty={fpr_empty:.4f}, sum_shapley={sum(fpr_shapley.values()):.6f}\", file=sys.stderr)\n\nfnr_grand_6 = fnr_value(METHODS, signal_exps, PAIRS_6)\nfnr_empty_6 = fnr_value([], signal_exps, PAIRS_6)\nprint(f\"  FNR(6): grand={fnr_grand_6:.4f}, empty={fnr_empty_6:.4f}, sum_shapley={sum(fnr_shapley_6.values()):.6f}\", file=sys.stderr)\n\nprint(json.dumps(result, indent=2))\nPYEOF\necho \"Script written OK\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-20T14:33:05.280205+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Script written OK\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-20T14:33:05.280390+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "wc -c /tmp/data_17855.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "wc -c /tmp/data_17855.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-20T14:33:05.280524+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"44797 /tmp/data_17855.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-20T14:33:05.280670+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-17855",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json, base64, gzip\ndata = open('/tmp/data_17855.json','rb').read()\ncompressed = gzip.compress(data)\nprint(base64.b64encode(compressed).decode())\n\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-17855",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json, base64, gzip\ndata = open('/tmp/data_17855.json','rb').read()\ncompressed = gzip.compress(data)\nprint(base64.b64encode(compressed).decode())\n\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-20T14:33:05.280805+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"H4sIAPTEDWoC/+2d0XKaQBSG730Kx2tbgV1M0ou+SKezs4FVGREoi6Zpp+9eNEljTIOoIHuW/yLORBY5qyuf/zn/7n4bDIe/y7/hcBRG+ejLcCTjbCGFflAqm0jHcYTmnphlzBuNn9rtGpQtnc/O8zNaqbB8gnvP/xeLXOlFGm+fHBX5Wgmmo/lKitB1/JeXyWSU67LB09W3Z6VLlQiVFHmaPX76Gka6iJKgEO5eo7JZIqONEj+DNN+Gu3318evBMJrNPjr2LyqRJloVZYOZjPV+i0zlKzHPZTJX+X8OF4+HB5+P/Rkf64PXWh8OGpzShe2ptXvATOxBrQ9hJdcbdW707y7ffvgqUE2M/uORNz/834bu0Q2dkQv9olF+vTvl4OVxF34Vedwq8rggT+fkuV4fGN0+HP1aHl6i6/gbok/nkXtkI+8Ze64Y9YnwYTXhw+yCz+H59FRPcz1gJn4IdXRbuz8HTdU8oE79AdMQdDoK3D7keH6F3vF8CJ62odPFz6fGuWNAJ6h8NZFwA31Anx19Ai4AoIYKJR79LjCq1Spzk+A1boJQPYRybR1JZOuqPDvosLrQMSzTZpJiMFT2XIc7UD1QPbAZoNRzNoF4XQJxEAiJNyAICAKCgKCmEMSqrG4MlR9k3giouL7Sp+u0IdgDl/UF6Kkq+jC4DmCzhvYBfVD6gfBpgz68SvhwOA6QeLMfPrAd2CV82rS7AT3NoadK+HAIHwgfO+aXQvdA9xDwWveKPX6V7LEcPZdObMTk0lZ7QNtlbTRyTh8410JO0wPeDI/1ycPc3qk9AA5pqWP5egbm59guvQWCOa3/TDRE5Jz5hhs7uvff6xMFDqvJGyyfA4VjWg96umYoJI49Eqe7jFpTo/tE3vCavOHgDfQN9A2IQ2zMQ+EYVcSZvubUxIa/x84UFgJYCGAhwBLV8BDAQ9ASfj5KsU3tTrGBPdgeAfABfGh4Bu1jz02Vd/oGfgLK+TZDFgrtPN0G8LRSmIehgEC6zVQbG7iDOg/25YGNDTY2M+OmMbirkDNXicplHP1Skx8PKmG+cG7vxUO0jIR0nf2KzzsCubZvh01g5k6vdQ/wA80D+lCmTybDMErmIk/v17pIlNaTN9QBcqB5kGxDsg3uNnLpNlNGeBV+dCBjNXH5vQg4mAPmwE8NpQPgwE7djtjZ0UYECxUsJ9ljsYjk9O4g1Qb2gD29Y0+r8+tMXg8U7IG3oMEprzXLPE/o4a6zesMedpw9WLcA9R1y9R1k2uAwsLnGQyHPdtxkwGqm3oAgyB+k3oAg6B8sZXAugvQqjeMVE+wQQe7Nre+TYxB2xMbGPJBD2BIbO8MRm+1zvB6EnBwEEfxvkESQRPC/XU6gwffBXyIPJmr9rgAA\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-20T14:33:05.280955+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "echo 'H4sIAPTEDWoC/+2d0XKaQBSG730Kx2tbgV1M0ou+SKezs4FVGREoi6Zpp+9eNEljTIOoIHuW/yLORBY5qyuf/zn/7n4bDIe/y7/hcBRG+ejLcCTjbCGFflAqm0jHcYTmnphlzBuNn9rtGpQtnc/O8zNaqbB8gnvP/xeLXOlFGm+fHBX5Wgmmo/lKitB1/JeXyWSU67LB09W3Z6VLlQiVFHmaPX76Gka6iJKgEO5eo7JZIqONEj+DNN+Gu3318evBMJrNPjr2LyqRJloVZYOZjPV+i0zlKzHPZTJX+X8OF4+HB5+P/Rkf64PXWh8OGpzShe2ptXvATOxBrQ9hJdcbdW707y7ffvgqUE2M/uORNz/834bu0Q2dkQv9olF+vTvl4OVxF34Vedwq8rggT+fkuV4fGN0+HP1aHl6i6/gbok/nkXtkI+8Ze64Y9YnwYTXhw+yCz+H59FRPcz1gJn4IdXRbuz8HTdU8oE79AdMQdDoK3D7keH6F3vF8CJ62odPFz6fGuWNAJ6h8NZFwA31Anx19Ai4AoIYKJR79LjCq1Spzk+A1boJQPYRybR1JZOuqPDvosLrQMSzTZpJiMFT2XIc7UD1QPbAZoNRzNoF4XQJxEAiJNyAICAKCgKCmEMSqrG4MlR9k3giouL7Sp+u0IdgDl/UF6Kkq+jC4DmCzhvYBfVD6gfBpgz68SvhwOA6QeLMfPrAd2CV82rS7AT3NoadK+HAIHwgfO+aXQvdA9xDwWveKPX6V7LEcPZdObMTk0lZ7QNtlbTRyTh8410JO0wPeDI/1ycPc3qk9AA5pqWP5egbm59guvQWCOa3/TDRE5Jz5hhs7uvff6xMFDqvJGyyfA4VjWg96umYoJI49Eqe7jFpTo/tE3vCavOHgDfQN9A2IQ2zMQ+EYVcSZvubUxIa/x84UFgJYCGAhwBLV8BDAQ9ASfj5KsU3tTrGBPdgeAfABfGh4Bu1jz02Vd/oGfgLK+TZDFgrtPN0G8LRSmIehgEC6zVQbG7iDOg/25YGNDTY2M+OmMbirkDNXicplHP1Skx8PKmG+cG7vxUO0jIR0nf2KzzsCubZvh01g5k6vdQ/wA80D+lCmTybDMErmIk/v17pIlNaTN9QBcqB5kGxDsg3uNnLpNlNGeBV+dCBjNXH5vQg4mAPmwE8NpQPgwE7djtjZ0UYECxUsJ9ljsYjk9O4g1Qb2gD29Y0+r8+tMXg8U7IG3oMEprzXLPE/o4a6zesMedpw9WLcA9R1y9R1k2uAwsLnGQyHPdtxkwGqm3oAgyB+k3oAg6B8sZXAugvQqjeMVE+wQQe7Nre+TYxB2xMbGPJBD2BIbO8MRm+1zvB6EnBwEEfxvkESQRPC/XU6gwffBXyIPJmr9rgAA' | python3 -c \"\nimport sys, base64, gzip\nb64 = sys.stdin.read().strip()\ndata = gzip.decompress(base64.b64decode(b64))\nwith open('/tmp/data_17855.json', 'wb') as f:\n    f.write(data)\nimport json\nd = json.loads(data)\nprint(f'Decoded {len(d)} experiments from 17855')\n\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "echo 'H4sIAPTEDWoC/+2d0XKaQBSG730Kx2tbgV1M0ou+SKezs4FVGREoi6Zpp+9eNEljTIOoIHuW/yLORBY5qyuf/zn/7n4bDIe/y7/hcBRG+ejLcCTjbCGFflAqm0jHcYTmnphlzBuNn9rtGpQtnc/O8zNaqbB8gnvP/xeLXOlFGm+fHBX5Wgmmo/lKitB1/JeXyWSU67LB09W3Z6VLlQiVFHmaPX76Gka6iJKgEO5eo7JZIqONEj+DNN+Gu3318evBMJrNPjr2LyqRJloVZYOZjPV+i0zlKzHPZTJX+X8OF4+HB5+P/Rkf64PXWh8OGpzShe2ptXvATOxBrQ9hJdcbdW707y7ffvgqUE2M/uORNz/834bu0Q2dkQv9olF+vTvl4OVxF34Vedwq8rggT+fkuV4fGN0+HP1aHl6i6/gbok/nkXtkI+8Ze64Y9YnwYTXhw+yCz+H59FRPcz1gJn4IdXRbuz8HTdU8oE79AdMQdDoK3D7keH6F3vF8CJ62odPFz6fGuWNAJ6h8NZFwA31Anx19Ai4AoIYKJR79LjCq1Spzk+A1boJQPYRybR1JZOuqPDvosLrQMSzTZpJiMFT2XIc7UD1QPbAZoNRzNoF4XQJxEAiJNyAICAKCgKCmEMSqrG4MlR9k3giouL7Sp+u0IdgDl/UF6Kkq+jC4DmCzhvYBfVD6gfBpgz68SvhwOA6QeLMfPrAd2CV82rS7AT3NoadK+HAIHwgfO+aXQvdA9xDwWveKPX6V7LEcPZdObMTk0lZ7QNtlbTRyTh8410JO0wPeDI/1ycPc3qk9AA5pqWP5egbm59guvQWCOa3/TDRE5Jz5hhs7uvff6xMFDqvJGyyfA4VjWg96umYoJI49Eqe7jFpTo/tE3vCavOHgDfQN9A2IQ2zMQ+EYVcSZvubUxIa/x84UFgJYCGAhwBLV8BDAQ9ASfj5KsU3tTrGBPdgeAfABfGh4Bu1jz02Vd/oGfgLK+TZDFgrtPN0G8LRSmIehgEC6zVQbG7iDOg/25YGNDTY2M+OmMbirkDNXicplHP1Skx8PKmG+cG7vxUO0jIR0nf2KzzsCubZvh01g5k6vdQ/wA80D+lCmTybDMErmIk/v17pIlNaTN9QBcqB5kGxDsg3uNnLpNlNGeBV+dCBjNXH5vQg4mAPmwE8NpQPgwE7djtjZ0UYECxUsJ9ljsYjk9O4g1Qb2gD29Y0+r8+tMXg8U7IG3oMEprzXLPE/o4a6zesMedpw9WLcA9R1y9R1k2uAwsLnGQyHPdtxkwGqm3oAgyB+k3oAg6B8sZXAugvQqjeMVE+wQQe7Nre+TYxB2xMbGPJBD2BIbO8MRm+1zvB6EnBwEEfxvkESQRPC/XU6gwffBXyIPJmr9rgAA' | python3 -c \"\nimport sys, base64, gzip\nb64 = sys.stdin.read().strip()\ndata = gzip.decompress(base64.b64decode(b64))\nwith open('/tmp/data_17855.json', 'wb') as f:\n    f.write(data)\nimport json\nd = json.loads(data)\nprint(f'Decoded {len(d)} experiments from 17855')\n\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-20T14:33:05.281090+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Decoded 27 experiments from 17855\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-20T14:33:05.281219+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "python3 /tmp/shapley_v3.py > /tmp/shapley_v3_result.json 2>/tmp/shapley_v3_log.txt && cat /tmp/shapley_v3_log.txt && echo \"---\" && cat /tmp/shapley_v3_result.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "python3 /tmp/shapley_v3.py > /tmp/shapley_v3_result.json 2>/tmp/shapley_v3_log.txt && cat /tmp/shapley_v3_log.txt && echo \"---\" && cat /tmp/shapley_v3_result.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-20T14:33:05.281491+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"alpha=0.00 seed=42 dedup: kept 17855:alpha_sweep/a000_s42_fp32\\nNull experiments: 3\\nSignal experiments: 40\\nTotal clean experiments: 43\\nComputing FPR Shapley (8-pair)...\\nComputing FNR Shapley (6-pair)...\\nComputing FNR Shapley (8-pair)...\\n\\nVerification:\\n  perm_granger FPR Shapley: 0.0\\n  perm_granger raw FPR: 0.0 (0/24)\\n  FPR: grand=0.9167, empty=0.0000, sum_shapley=0.916666\\n  FNR(6): grand=0.0000, empty=1.0000, sum_shapley=-1.000000\\n---\\n{\\n  \\\"version\\\": \\\"v3_dedup_fdr\\\",\\n  \\\"generated_at\\\": \\\"2026-05-20T14:28:24.530753\\\",\\n  \\\"data_sources\\\": [\\n    \\\"17855:alpha_sweep/a000_s42_fp32\\\",\\n    \\\"17855:alpha_sweep/a010_s42_fp32\\\",\\n    \\\"17855:alpha_sweep/a010_s43_fp32\\\",\\n    \\\"17855:alpha_sweep/a025_s42_fp32\\\",\\n    \\\"17855:alpha_sweep/a025_s43_fp32\\\",\\n    \\\"17855:alpha_sweep/a025_s44_fp32\\\",\\n    \\\"17855:alpha_sweep/a030_s42_fp32\\\",\\n    \\\"17855:alpha_sweep/a035_s42_fp32\\\",\\n    \\\"17855:alpha_sweep/a040_s42_fp32\\\",\\n    \\\"17855:alpha_sweep/a045_s42_fp32\\\",\\n    \\\"17855:alpha_sweep/a050_s42_fp32\\\",\\n    \\\"17855:alpha_sweep/a050_s43_fp32\\\",\\n    \\\"17855:alpha_sweep/a050_s44_fp32\\\",\\n    \\\"17855:alpha_sweep/a060_s42_fp32_v4\\\",\\n    \\\"17855:alpha_sweep/a060_s43_fp32\\\",\\n    \\\"17855:alpha_sweep/a075_s42_fp32\\\",\\n    \\\"17855:generalize/pythia410m_wiki_a100_s43\\\",\\n    \\\"17855:generalize/qwen35_08b_wiki_a100_s42_fp32_v2\\\",\\n    \\\"17855:generalize/qwen35_08b_wiki_a100_s43_fp32\\\",\\n    \\\"17855:generalize/smollm3_3b_wiki_a100_s43_17855\\\",\\n    \\\"17855:padding_robustness/a100_s42_fp32\\\",\\n    \\\"17855:scale/14b_c4_s42_fp32\\\",\\n    \\\"17855:scale_check/pythia69b_wiki_a100_s42\\\",\\n    \\\"17855:scale_check/pythia69b_wiki_a100_s43\\\",\\n    \\\"19828:ablation/accumulate_a050_s43\\\",\\n    \\\"19828:alpha_sweep/a000_s43\\\",\\n    \\\"19828:alpha_sweep/a000_s44\\
…[truncated 6705 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-20T14:33:05.281738+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "cat > /tmp/shapley_v3.py << 'PYEOF'\nimport json, os, sys\nfrom math import factorial\nfrom itertools import combinations\nfrom datetime import datetime\n\ndata_19828 = json.load(open('/tmp/data_19828.json'))\ndata_17855 = json.load(open('/tmp/data_17855.json'))\n\nfor exp in data_19828:\n    exp['server'] = '19828'\n    exp['source'] = f\"19828:{exp['dir']}\"\nfor exp in data_17855:\n    exp['server'] = '17855'\n    exp['source'] = f\"17855:{exp['dir']}\"\n\nall_exps = data_19828 + data_17855\n\ndef extract_dedup_key(exp):\n    \"\"\"For alpha_sweep experiments, extract (dataset, alpha, seed) dedup key.\"\"\"\n    d = exp['dir']\n    if not d.startswith('alpha_sweep/'):\n        return None\n    basename = d.split('/')[-1]\n    dataset = \"c4\" if basename.startswith(\"c4_\") else \"wikitext\"\n    return (dataset, exp['alpha'], exp['seed'])\n\ndedup_map = {}\nfor exp in all_exps:\n    key = extract_dedup_key(exp)\n    if key is not None:\n        dedup_map.setdefault(key, []).append(exp)\n\nkeep_sources = set()\nfor key, exps in dedup_map.items():\n    if len(exps) == 1:\n        keep_sources.add(exps[0]['source'])\n    else:\n        has_17855 = [e for e in exps if e['server'] == '17855']\n        if has_17855:\n            keep_sources.add(has_17855[0]['source'])\n        else:\n            keep_sources.add(exps[0]['source'])\n\nfor exp in all_exps:\n    key = extract_dedup_key(exp)\n    if key is None:\n        keep_sources.add(exp['source'])\n\nclean_exps = [e for e in all_exps if e['source'] in keep_sources]\nclean_exps.sort(key=lambda x: (x['alpha'] or 0, x['seed'] or 0, x['source']))\n\nimport re\nfor e in clean_exps:\n    assert not re.search(r'v3_d080|postd093|bf16', e['dir']), f\"Non-standard: {e['source']}\"\n\nnull_s42 = [e for e in clean_exps if e['alpha'] == 0.0 and e['seed'] == 42\n            and e['dir'].startswith('alpha_sweep/')]\nassert len(null_s42) == 1, f\"alpha=0.00 seed=42 dedup failed: {[e['source'] for e in null_s42]}\"\nprint(f\"alpha=0.00 seed=42: {null_s42[0]['source']}\", file=sys.stderr)\n\nPAIRS_8 = [\n    \"token_entropy->distinct_1\", \"token_entropy->distinct_2\",\n    \"token_entropy->distinct_3\", \"token_entropy->mauve\",\n    \"ece->distinct_1\", \"ece->distinct_2\",\n    \"ece->distinct_3\", \"ece->mauve\"\n]\nPAIRS_6 = [p for p in PAIRS_8 if \"mauve\" not in p]\nMETHODS = [\"naive_xcorr\", \"diff_xcorr\", \"threshold_onset\", \"perm_granger\", \"ty_granger\"]\nN = len(METHODS)\n\nnull_exps = [e for e in clean_exps if e['alpha'] == 0.0]\nsignal_exps = [e for e in clean_exps if e['alpha'] is not None and e['alpha'] > 0]\n\nprint(f\"Null: {len(null_exps)}, Signal: {len(signal_exps)}, Total: {len(clean_exps)}\", file=sys.stderr)\n\n# Check dedup details\ndedup_details = {}\nfor key, exps in dedup_map.items():\n    if len(exps) > 1:\n        kept = [e['source'] for e in exps if e['source'] in keep_sources]\n        dropped = [e['source'] for e in exps if e['source'] not in keep_sources]\n        for d in dropped:\n            dedup_details[d] = f\"replaced by {kept[0]}\"\nprint(f\"Deduped entries: {len(dedup_details)}\", file=sys.stderr)\nfor k,v in sorted(dedup_details.items()):\n    print(f\"  {k} -> {v}\", file=sys.stderr)\n\ndef fpr_value(coalition, null_exps, pairs):\n    if not coalition:\n        return 0.0\n    total = fp = 0\n    for exp in null_exps:\n        for pair in pairs:\n            if pair not in exp['pairs']:\n                continue\n            total += 1\n            if any(exp['pairs'][pair].get(m, False) for m in coalition):\n                fp += 1\n    return fp / total if total > 0 else 0.0\n\ndef fnr_value(coalition, signal_exps, pairs):\n    if not coalition:\n        return 1.0\n    total = fn = 0\n    for exp in signal_exps:\n        for pair in pairs:\n            if pair not in exp['pairs']:\n                continue\n            total += 1\n            if not any(exp['pairs'][pair].get(m, False) for m in coalition):\n                fn += 1\n    return fn / total if total > 0 else 1.0\n\ndef compute_shapley(value_func, exps, pairs):\n    shapley = {m: 0.0 for m in METHODS}\n    for i, method in enumerate(METHODS):\n        others = [m for m in METHODS if m != method]\n        phi = 0.0\n        for s_size in range(N):\n            weight = factorial(s_size) * factorial(N - s_size - 1) / factorial(N)\n            for subset in combinations(others, s_size):\n                s_list = list(subset)\n                v_with = value_func(s_list + [method], exps, pairs)\n                v_without = value_func(s_list, exps, pairs)\n                phi += weight * (v_with - v_without)\n        shapley[method] = round(phi, 6)\n    return shapley\n\nprint(\"Computing Shapley values...\", file=sys.stderr)\nfpr_shapley = compute_shapley(fpr_value, null_exps, PAIRS_8)\nfnr_shapley_6 = compute_shapley(fnr_value, signal_exps, PAIRS_6)\nfnr_shapley_8 = compute_shapley(fnr_value, signal_exps, PAIRS_8)\n\ncombined_6 = {m: round(fpr_shapley[m] + fnr_shapley_6[m], 6) for m in METHODS}\ncombined_8 = {m: round(fpr_shapley[m] + fnr_shapley_8[m], 6) for m in METHODS}\n\ndef raw_rates(null_exps, signal_exps, pairs):\n    rates = {}\n    for m in METHODS:\n        fp_total = fp_count = fn_total = fn_count = 0\n        for exp in null_exps:\n            for pair in pairs:\n                if pair not in exp['pairs']: continue\n                fp_total += 1\n                if exp['pairs'][pair].get(m, False): fp_count += 1\n        for exp in signal_exps:\n            for pair in pairs:\n                if pair not in exp['pairs']: continue\n                fn_total += 1\n                if not exp['pairs'][pair].get(m, False): fn_count += 1\n        rates[m] = {\n            \"fpr\": round(fp_count / fp_total, 4) if fp_total > 0 else 0,\n            \"fnr\": round(fn_count / fn_total, 4) if fn_total > 0 else 0,\n            \"fp_count\": fp_count, \"fp_total\": fp_total,\n            \"fn_count\": fn_count, \"fn_total\": fn_total\n        }\n    return rates\n\nraw_8 = raw_rates(null_exps, signal_exps, PAIRS_8)\n\nn_null_obs = sum(1 for e in null_exps for p in PAIRS_8 if p in e['pairs'])\nn_signal_obs_6 = sum(1 for e in signal_exps for p in PAIRS_6 if p in e['pairs'])\nn_signal_obs_8 = sum(1 for e in signal_exps for p in PAIRS_8 if p in e['pairs'])\n\nresult = {\n    \"version\": \"v3_dedup_fdr\",\n    \"generated_at\": datetime.utcnow().isoformat(),\n    \"data_sources\": sorted([e['source'] for e in clean_exps]),\n    \"dedup_rules\": [\n        \"exclude dir names matching v3_d080|postd093|bf16\",\n        \"same (dataset, alpha, seed) in alpha_sweep: prefer westd-17855 fp32\",\n        \"only true_3sigma_d105 threshold\"\n    ],\n    \"fdr_field_used\": {\n        \"naive_xcorr\": \"significant_fdr\",\n        \"diff_xcorr\": \"significant_fdr\",\n        \"threshold_onset\": \"significant (deterministic, no p-value)\",\n        \"perm_granger\": \"significant_fdr\",\n        \"ty_granger\": \"significant_fdr\"\n    },\n    \"threshold_criterion\": \"true_3sigma_d105\",\n    \"n_methods\": 5,\n    \"n_coalitions\": 32,\n    \"n_null_experiments\": len(null_exps),\n    \"n_signal_experiments\": len(signal_exps),\n    \"n_null_obs\": n_null_obs,\n    \"n_signal_obs_6pair\": n_signal_obs_6,\n    \"n_signal_obs_8pair\": n_signal_obs_8,\n    \"fpr_pairs\": PAIRS_8,\n    \"fnr_pairs_6\": PAIRS_6,\n    \"fnr_pairs_8\": PAIRS_8,\n    \"methods\": METHODS,\n    \"main_result_6pair\": {\n        \"fpr_shapley\": fpr_shapley,\n        \"fnr_shapley\": fnr_shapley_6,\n        \"combined_shapley\": combined_6\n    },\n    \"robustness_8pair\": {\n        \"fpr_shapley\": fpr_shapley,\n        \"fnr_shapley\": fnr_shapley_8,\n        \"combined_shapley\": combined_8\n    },\n    \"raw_rates_8pair\": raw_8,\n    \"diagnostics\": {\n        \"null_s42_source\": null_s42[0]['source'],\n        \"excluded_from_v2\": [\n            \"17855:alpha_sweep/a005_s42_fp32_v3_d080\",\n            \"17855:alpha_sweep/a060_s42_fp32_v3_d080\",\n            \"17855:alpha_sweep/a050_postd093_s42_fp32\",\n            \"17855:generalize/gpt2m_wiki_a100_s43_bf16\"\n        ],\n        \"deduped_from_v2\": dedup_details\n    }\n}\n\n# Verification\nprint(f\"\\nVerification:\", file=sys.stderr)\nprint(f\"  perm_granger FPR Shapley: {fpr_shapley['perm_granger']}\", file=sys.stderr)\nprint(f\"  perm_granger raw FPR: {raw_8['perm_granger']['fpr']} ({raw_8['perm_granger']['fp_count']}/{raw_8['perm_granger']['fp_total']})\", file=sys.stderr)\nfpr_grand = fpr_value(METHODS, null_exps, PAIRS_8)\nprint(f\"  FPR sum check: grand={fpr_grand:.4f}, sum_shapley={sum(fpr_shapley.values()):.6f}\", file=sys.stderr)\nfnr_grand_6 = fnr_value(METHODS, signal_exps, PAIRS_6)\nprint(f\"  FNR(6) sum check: grand={fnr_grand_6:.4f}, sum_shapley={sum(fnr_shapley_6.values()):.6f}\", file=sys.stderr)\n\nprint(json.dumps(result, indent=2))\nPYEOF\npython3 /tmp/shapley_v3.py > /tmp/shapley_v3_result.json 2>/tmp/shapley_v3_log.txt && cat /tmp/shapley_v3_log.txt && echo \"===JSON===\" && cat /tmp/shapley_v3_result.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat > /tmp/shapley_v3.py << 'PYEOF'\nimport json, os, sys\nfrom math import factorial\nfrom itertools import combinations\nfrom datetime import datetime\n\ndata_19828 = json.load(open('/tmp/data_19828.json'))\ndata_17855 = json.load(open('/tmp/data_17855.json'))\n\nfor exp in data_19828:\n    exp['server'] = '19828'\n    exp['source'] = f\"19828:{exp['dir']}\"\nfor exp in data_17855:\n    exp['server'] = '17855'\n    exp['source'] = f\"17855:{exp['dir']}\"\n\nall_exps = data_19828 + data_17855\n\ndef extract_dedup_key(exp):\n    \"\"\"For alpha_sweep experiments, extract (dataset, alpha, seed) dedup key.\"\"\"\n    d = exp['dir']\n    if not d.startswith('alpha_sweep/'):\n        return None\n    basename = d.split('/')[-1]\n    dataset = \"c4\" if basename.startswith(\"c4_\") else \"wikitext\"\n    return (dataset, exp['alpha'], exp['seed'])\n\ndedup_map = {}\nfor exp in all_exps:\n    key = extract_dedup_key(exp)\n    if key is not None:\n        dedup_map.setdefault(key, []).append(exp)\n\nkeep_sources = set()\nfor key, exps in dedup_map.items():\n    if len(exps) == 1:\n        keep_sources.add(exps[0]['source'])\n    else:\n        has_17855 = [e for e in exps if e['server'] == '17855']\n        if has_17855:\n            keep_sources.add(has_17855[0]['source'])\n        else:\n            keep_sources.add(exps[0]['source'])\n\nfor exp in all_exps:\n    key = extract_dedup_key(exp)\n    if key is None:\n        keep_sources.add(exp['source'])\n\nclean_exps = [e for e in all_exps if e['source'] in keep_sources]\nclean_exps.sort(key=lambda x: (x['alpha'] or 0, x['seed'] or 0, x['source']))\n\nimport re\nfor e in clean_exps:\n    assert not re.search(r'v3_d080|postd093|bf16', e['dir']), f\"Non-standard: {e['source']}\"\n\nnull_s42 = [e for e in clean_exps if e['alpha'] == 0.0 and e['seed'] == 42\n            and e['dir'].startswith('alpha_sweep/')]\nassert len(null_s42) == 1, f\"alpha=0.00 seed=42 dedup failed: {[e['source'] for e in null_s42]}\"\nprint(f\"alpha=0.00 seed=42: {null_s42[0]['source']}\", file=sys.stderr)\n\nPAIRS_8 = [\n    \"token_entropy->distinct_1\", \"token_entropy->distinct_2\",\n    \"token_entropy->distinct_3\", \"token_entropy->mauve\",\n    \"ece->distinct_1\", \"ece->distinct_2\",\n    \"ece->distinct_3\", \"ece->mauve\"\n]\nPAIRS_6 = [p for p in PAIRS_8 if \"mauve\" not in p]\nMETHODS = [\"naive_xcorr\", \"diff_xcorr\", \"threshold_onset\", \"perm_granger\", \"ty_granger\"]\nN = len(METHODS)\n\nnull_exps = [e for e in clean_exps if e['alpha'] == 0.0]\nsignal_exps = [e for e in clean_exps if e['alpha'] is not None and e['alpha'] > 0]\n\nprint(f\"Null: {len(null_exps)}, Signal: {len(signal_exps)}, Total: {len(clean_exps)}\", file=sys.stderr)\n\n# Check dedup details\ndedup_details = {}\nfor key, exps in dedup_map.items():\n    if len(exps) > 1:\n        kept = [e['source'] for e in exps if e['source'] in keep_sources]\n        dropped = [e['source'] for e in exps if e['source'] not in keep_sources]\n        for d in dropped:\n            dedup_details[d] = f\"replaced by {kept[0]}\"\nprint(f\"Deduped entries: {len(dedup_details)}\", file=sys.stderr)\nfor k,v in sorted(dedup_details.items()):\n    print(f\"  {k} -> {v}\", file=sys.stderr)\n\ndef fpr_value(coalition, null_exps, pairs):\n    if not coalition:\n        return 0.0\n    total = fp = 0\n    for exp in null_exps:\n        for pair in pairs:\n            if pair not in exp['pairs']:\n                continue\n            total += 1\n            if any(exp['pairs'][pair].get(m, False) for m in coalition):\n                fp += 1\n    return fp / total if total > 0 else 0.0\n\ndef fnr_value(coalition, signal_exps, pairs):\n    if not coalition:\n        return 1.0\n    total = fn = 0\n    for exp in signal_exps:\n        for pair in pairs:\n            if pair not in exp['pairs']:\n                continue\n            total += 1\n            if not any(exp['pairs'][pair].get(m, False) for m in coalition):\n                fn += 1\n    return fn / total if total > 0 else 1.0\n\ndef compute_shapley(value_func, exps, pairs):\n    shapley = {m: 0.0 for m in METHODS}\n    for i, method in enumerate(METHODS):\n        others = [m for m in METHODS if m != method]\n        phi = 0.0\n        for s_size in range(N):\n            weight = factorial(s_size) * factorial(N - s_size - 1) / factorial(N)\n            for subset in combinations(others, s_size):\n                s_list = list(subset)\n                v_with = value_func(s_list + [method], exps, pairs)\n                v_without = value_func(s_list, exps, pairs)\n                phi += weight * (v_with - v_without)\n        shapley[method] = round(phi, 6)\n    return shapley\n\nprint(\"Computing Shapley values...\", file=sys.stderr)\nfpr_shapley = compute_shapley(fpr_value, null_exps, PAIRS_8)\nfnr_shapley_6 = compute_shapley(fnr_value, signal_exps, PAIRS_6)\nfnr_shapley_8 = compute_shapley(fnr_value, signal_exps, PAIRS_8)\n\ncombined_6 = {m: round(fpr_shapley[m] + fnr_shapley_6[m], 6) for m in METHODS}\ncombined_8 = {m: round(fpr_shapley[m] + fnr_shapley_8[m], 6) for m in METHODS}\n\ndef raw_rates(null_exps, signal_exps, pairs):\n    rates = {}\n    for m in METHODS:\n        fp_total = fp_count = fn_total = fn_count = 0\n        for exp in null_exps:\n            for pair in pairs:\n                if pair not in exp['pairs']: continue\n                fp_total += 1\n                if exp['pairs'][pair].get(m, False): fp_count += 1\n        for exp in signal_exps:\n            for pair in pairs:\n                if pair not in exp['pairs']: continue\n                fn_total += 1\n                if not exp['pairs'][pair].get(m, False): fn_count += 1\n        rates[m] = {\n            \"fpr\": round(fp_count / fp_total, 4) if fp_total > 0 else 0,\n            \"fnr\": round(fn_count / fn_total, 4) if fn_total > 0 else 0,\n            \"fp_count\": fp_count, \"fp_total\": fp_total,\n            \"fn_count\": fn_count, \"fn_total\": fn_total\n        }\n    return rates\n\nraw_8 = raw_rates(null_exps, signal_exps, PAIRS_8)\n\nn_null_obs = sum(1 for e in null_exps for p in PAIRS_8 if p in e['pairs'])\nn_signal_obs_6 = sum(1 for e in signal_exps for p in PAIRS_6 if p in e['pairs'])\nn_signal_obs_8 = sum(1 for e in signal_exps for p in PAIRS_8 if p in e['pairs'])\n\nresult = {\n    \"version\": \"v3_dedup_fdr\",\n    \"generated_at\": datetime.utcnow().isoformat(),\n    \"data_sources\": sorted([e['source'] for e in clean_exps]),\n    \"dedup_rules\": [\n        \"exclude dir names matching v3_d080|postd093|bf16\",\n        \"same (dataset, alpha, seed) in alpha_sweep: prefer westd-17855 fp32\",\n        \"only true_3sigma_d105 threshold\"\n    ],\n    \"fdr_field_used\": {\n        \"naive_xcorr\": \"significant_fdr\",\n        \"diff_xcorr\": \"significant_fdr\",\n        \"threshold_onset\": \"significant (deterministic, no p-value)\",\n        \"perm_granger\": \"significant_fdr\",\n        \"ty_granger\": \"significant_fdr\"\n    },\n    \"threshold_criterion\": \"true_3sigma_d105\",\n    \"n_methods\": 5,\n    \"n_coalitions\": 32,\n    \"n_null_experiments\": len(null_exps),\n    \"n_signal_experiments\": len(signal_exps),\n    \"n_null_obs\": n_null_obs,\n    \"n_signal_obs_6pair\": n_signal_obs_6,\n    \"n_signal_obs_8pair\": n_signal_obs_8,\n    \"fpr_pairs\": PAIRS_8,\n    \"fnr_pairs_6\": PAIRS_6,\n    \"fnr_pairs_8\": PAIRS_8,\n    \"methods\": METHODS,\n    \"main_result_6pair\": {\n        \"fpr_shapley\": fpr_shapley,\n        \"fnr_shapley\": fnr_shapley_6,\n        \"combined_shapley\": combined_6\n    },\n    \"robustness_8pair\": {\n        \"fpr_shapley\": fpr_shapley,\n        \"fnr_shapley\": fnr_shapley_8,\n        \"combined_shapley\": combined_8\n    },\n    \"raw_rates_8pair\": raw_8,\n    \"diagnostics\": {\n        \"null_s42_source\": null_s42[0]['source'],\n        \"excluded_from_v2\": [\n            \"17855:alpha_sweep/a005_s42_fp32_v3_d080\",\n            \"17855:alpha_sweep/a060_s42_fp32_v3_d080\",\n            \"17855:alpha_sweep/a050_postd093_s42_fp32\",\n            \"17855:generalize/gpt2m_wiki_a100_s43_bf16\"\n        ],\n        \"deduped_from_v2\": dedup_details\n    }\n}\n\n# Verification\nprint(f\"\\nVerification:\", file=sys.stderr)\nprint(f\"  perm_granger FPR Shapley: {fpr_shapley['perm_granger']}\", file=sys.stderr)\nprint(f\"  perm_granger raw FPR: {raw_8['perm_granger']['fpr']} ({raw_8['perm_granger']['fp_count']}/{raw_8['perm_granger']['fp_total']})\", file=sys.stderr)\nfpr_grand = fpr_value(METHODS, null_exps, PAIRS_8)\nprint(f\"  FPR sum check: grand={fpr_grand:.4f}, sum_shapley={sum(fpr_shapley.values()):.6f}\", file=sys.stderr)\nfnr_grand_6 = fnr_value(METHODS, signal_exps, PAIRS_6)\nprint(f\"  FNR(6) sum check: grand={fnr_grand_6:.4f}, sum_shapley={sum(fnr_shapley_6.values()):.6f}\", file=sys.stderr)\n\nprint(json.dumps(result, indent=2))\nPYEOF\npython3 /tmp/shapley_v3.py > /tmp/shapley_v3_result.json 2>/tmp/shapley_v3_log.txt && cat /tmp/shapley_v3_log.txt && echo \"===JSON===\" && cat /tmp/shapley_v3_result.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-20T14:33:05.282080+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"alpha=0.00 seed=42: 17855:alpha_sweep/a000_s42_fp32\\nNull: 3, Signal: 45, Total: 48\\nDeduped entries: 8\\n  19828:alpha_sweep/a000_s42 -> replaced by 17855:alpha_sweep/a000_s42_fp32\\n  19828:alpha_sweep/a010_s42 -> replaced by 17855:alpha_sweep/a010_s42_fp32\\n  19828:alpha_sweep/a025_s43 -> replaced by 17855:alpha_sweep/a025_s43_fp32\\n  19828:alpha_sweep/a025_s44 -> replaced by 17855:alpha_sweep/a025_s44_fp32\\n  19828:alpha_sweep/a050_s42 -> replaced by 17855:alpha_sweep/a050_s42_fp32\\n  19828:alpha_sweep/a050_s43 -> replaced by 17855:alpha_sweep/a050_s43_fp32\\n  19828:alpha_sweep/a050_s44 -> replaced by 17855:alpha_sweep/a050_s44_fp32\\n  19828:alpha_sweep/a075_s42 -> replaced by 17855:alpha_sweep/a075_s42_fp32\\nComputing Shapley values...\\n\\nVerification:\\n  perm_granger FPR Shapley: 0.0\\n  perm_granger raw FPR: 0.0 (0/24)\\n  FPR sum check: grand=0.9167, sum_shapley=0.916666\\n  FNR(6) sum check: grand=0.0000, sum_shapley=-1.000000\\n===JSON===\\n{\\n  \\\"version\\\": \\\"v3_dedup_fdr\\\",\\n  \\\"generated_at\\\": \\\"2026-05-20T14:29:55.778865\\\",\\n  \\\"data_sources\\\": [\\n    \\\"17855:alpha_sweep/a000_s42_fp32\\\",\\n    \\\"17855:alpha_sweep/a010_s42_fp32\\\",\\n    \\\"17855:alpha_sweep/a010_s43_fp32\\\",\\n    \\\"17855:alpha_sweep/a025_s42_fp32\\\",\\n    \\\"17855:alpha_sweep/a025_s43_fp32\\\",\\n    \\\"17855:alpha_sweep/a025_s44_fp32\\\",\\n    \\\"17855:alpha_sweep/a030_s42_fp32\\\",\\n    \\\"17855:alpha_sweep/a035_s42_fp32\\\",\\n    \\\"17855:alpha_sweep/a040_s42_fp32\\\",\\n    \\\"17855:alpha_sweep/a045_s42_fp32\\\",\\n    \\\"17855:alpha_sweep/a050_s42_fp32\\\",\\n    \\\"17855:alpha_sweep/a050_s43_fp32\\\",\\n    \\\"17855:alpha_sweep/a050_s44_fp32\\\",\\n    \\\"17855:alpha_sweep/a060_s42_fp32_v4\\\",\\n    \\\"17855:alpha_sweep/a060_s43_fp32\\\",\\n    \\\"17855:alpha_sweep/a075_s42_fp32\\\",\\n    \\\"17855:alpha_sweep/c4_a025_s42_fp32\\\",\\n    \\\"17855:alpha_sweep
…[truncated 7377 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-20T14:33:05.282321+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /tmp/shapley_v3_result.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /tmp/shapley_v3_result.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-20T14:33:05.282589+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"version\\\": \\\"v3_dedup_fdr\\\",\\n  \\\"generated_at\\\": \\\"2026-05-20T14:29:55.778865\\\",\\n  \\\"data_sources\\\": [\\n    \\\"17855:alpha_sweep/a000_s42_fp32\\\",\\n    \\\"17855:alpha_sweep/a010_s42_fp32\\\",\\n    \\\"17855:alpha_sweep/a010_s43_fp32\\\",\\n    \\\"17855:alpha_sweep/a025_s42_fp32\\\",\\n    \\\"17855:alpha_sweep/a025_s43_fp32\\\",\\n    \\\"17855:alpha_sweep/a025_s44_fp32\\\",\\n    \\\"17855:alpha_sweep/a030_s42_fp32\\\",\\n    \\\"17855:alpha_sweep/a035_s42_fp32\\\",\\n    \\\"17855:alpha_sweep/a040_s42_fp32\\\",\\n    \\\"17855:alpha_sweep/a045_s42_fp32\\\",\\n    \\\"17855:alpha_sweep/a050_s42_fp32\\\",\\n    \\\"17855:alpha_sweep/a050_s43_fp32\\\",\\n    \\\"17855:alpha_sweep/a050_s44_fp32\\\",\\n    \\\"17855:alpha_sweep/a060_s42_fp32_v4\\\",\\n    \\\"17855:alpha_sweep/a060_s43_fp32\\\",\\n    \\\"17855:alpha_sweep/a075_s42_fp32\\\",\\n    \\\"17855:alpha_sweep/c4_a025_s42_fp32\\\",\\n    \\\"17855:alpha_sweep/c4_a050_s42_fp32\\\",\\n    \\\"17855:alpha_sweep/c4_a075_s42_fp32\\\",\\n    \\\"17855:generalize/pythia410m_wiki_a100_s43\\\",\\n    \\\"17855:generalize/qwen35_08b_wiki_a100_s42_fp32_v2\\\",\\n    \\\"17855:generalize/qwen35_08b_wiki_a100_s43_fp32\\\",\\n    \\\"17855:generalize/smollm3_3b_wiki_a100_s43_17855\\\",\\n    \\\"17855:padding_robustness/a100_s42_fp32\\\",\\n    \\\"17855:scale/14b_c4_s42_fp32\\\",\\n    \\\"17855:scale_check/pythia69b_wiki_a100_s42\\\",\\n    \\\"17855:scale_check/pythia69b_wiki_a100_s43\\\",\\n    \\\"19828:ablation/accumulate_a050_s43\\\",\\n    \\\"19828:alpha_sweep/a000_s43\\\",\\n    \\\"19828:alpha_sweep/a000_s44\\\",\\n    \\\"19828:alpha_sweep/a055_s42_fp32\\\",\\n    \\\"19828:alpha_sweep/a075_s43\\\",\\n    \\\"19828:alpha_sweep/a075_s44\\\",\\n    \\\"19828:alpha_sweep/c4_a050_s43_fp32\\\",\\n    \\\"19828:alpha_sweep/c4_a075_s43_fp32\\\",\\n    \\\"19828:gen_opt13b_wiki_a100_s43_fp32\\\",\\n    \\\"19828:gen_wiki_gpt2m
…[truncated 6400 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-20T14:33:05.282792+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/shapley_v2/shapley_values_v2.json",
  "content": "{\n  \"version\": \"v3_dedup_fdr\",\n  \"generated_at\": \"2026-05-20T14:29:55.778865\",\n  \"data_sources\": [\n    \"17855:alpha_sweep/a000_s42_fp32\",\n    \"17855:alpha_sweep/a010_s42_fp32\",\n    \"17855:alpha_sweep/a010_s43_fp32\",\n    \"17855:alpha_sweep/a025_s42_fp32\",\n    \"17855:alpha_sweep/a025_s43_fp32\",\n    \"17855:alpha_sweep/a025_s44_fp32\",\n    \"17855:alpha_sweep/a030_s42_fp32\",\n    \"17855:alpha_sweep/a035_s42_fp32\",\n    \"17855:alpha_sweep/a040_s42_fp32\",\n    \"17855:alpha_sweep/a045_s42_fp32\",\n    \"17855:alpha_sweep/a050_s42_fp32\",\n    \"17855:alpha_sweep/a050_s43_fp32\",\n    \"17855:alpha_sweep/a050_s44_fp32\",\n    \"17855:alpha_sweep/a060_s42_fp32_v4\",\n    \"17855:alpha_sweep/a060_s43_fp32\",\n    \"17855:alpha_sweep/a075_s42_fp32\",\n    \"17855:alpha_sweep/c4_a025_s42_fp32\",\n    \"17855:alpha_sweep/c4_a050_s42_fp32\",\n    \"17855:alpha_sweep/c4_a075_s42_fp32\",\n    \"17855:generalize/pythia410m_wiki_a100_s43\",\n    \"17855:generalize/qwen35_08b_wiki_a100_s42_fp32_v2\",\n    \"17855:generalize/qwen35_08b_wiki_a100_s43_fp32\",\n    \"17855:generalize/smollm3_3b_wiki_a100_s43_17855\",\n    \"17855:padding_robustness/a100_s42_fp32\",\n    \"17855:scale/14b_c4_s42_fp32\",\n    \"17855:scale_check/pythia69b_wiki_a100_s42\",\n    \"17855:scale_check/pythia69b_wiki_a100_s43\",\n    \"19828:ablation/accumulate_a050_s43\",\n    \"19828:alpha_sweep/a000_s43\",\n    \"19828:alpha_sweep/a000_s44\",\n    \"19828:alpha_sweep/a055_s42_fp32\",\n    \"19828:alpha_sweep/a075_s43\",\n    \"19828:alpha_sweep/a075_s44\",\n    \"19828:alpha_sweep/c4_a050_s43_fp32\",\n    \"19828:alpha_sweep/c4_a075_s43_fp32\",\n    \"19828:gen_opt13b_wiki_a100_s43_fp32\",\n    \"19828:gen_wiki_gpt2m_a100_s43\",\n    \"19828:generalize/gpt2m_wiki_a100_s42\",\n    \"19828:generalize/opt1b_wiki_a100_s42\",\n    \"19828:generalize/pythia14b_wiki_a100_s42\",\n    \"19828:generalize/pythia14b_wiki_a100_s43\",\n    \"19828:generalize/pythia1b_c4_a100_s42\",\n    \"19828:generalize/pythia1b_c4_a100_s43\",\n    \"19828:generalize/pythia410m_wiki_a100_s42\",\n    \"19828:generalize/smollm3_3b_wiki_a100_s42_fp32_v3\",\n    \"19828:intervention/predictive_te_s42\",\n    \"19828:intervention/reactive_d1_s42\",\n    \"19828:scale_check/pythia14b_a050_s42\"\n  ],\n  \"dedup_rules\": [\n    \"exclude dir names matching v3_d080|postd093|bf16\",\n    \"same (dataset, alpha, seed) in alpha_sweep: prefer westd-17855 fp32\",\n    \"only true_3sigma_d105 threshold\"\n  ],\n  \"fdr_field_used\": {\n    \"naive_xcorr\": \"significant_fdr\",\n    \"diff_xcorr\": \"significant_fdr\",\n    \"threshold_onset\": \"significant (deterministic, no p-value)\",\n    \"perm_granger\": \"significant_fdr\",\n    \"ty_granger\": \"significant_fdr\"\n  },\n  \"threshold_criterion\": \"true_3sigma_d105\",\n  \"n_methods\": 5,\n  \"n_coalitions\": 32,\n  \"n_null_experiments\": 3,\n  \"n_signal_experiments\": 45,\n  \"n_null_obs\": 24,\n  \"n_signal_obs_6pair\": 270,\n  \"n_signal_obs_8pair\": 360,\n  \"fpr_pairs\": [\n    \"token_entropy->distinct_1\",\n    \"token_entropy->distinct_2\",\n    \"token_entropy->distinct_3\",\n    \"token_entropy->mauve\",\n    \"ece->distinct_1\",\n    \"ece->distinct_2\",\n    \"ece->distinct_3\",\n    \"ece->mauve\"\n  ],\n  \"fnr_pairs_6\": [\n    \"token_entropy->distinct_1\",\n    \"token_entropy->distinct_2\",\n    \"token_entropy->distinct_3\",\n    \"ece->distinct_1\",\n    \"ece->distinct_2\",\n    \"ece->distinct_3\"\n  ],\n  \"fnr_pairs_8\": [\n    \"token_entropy->distinct_1\",\n    \"token_entropy->distinct_2\",\n    \"token_entropy->distinct_3\",\n    \"token_entropy->mauve\",\n    \"ece->distinct_1\",\n    \"ece->distinct_2\",\n    \"ece->distinct_3\",\n    \"ece->mauve\"\n  ],\n  \"methods\": [\n    \"naive_xcorr\",\n    \"diff_xcorr\",\n    \"threshold_onset\",\n    \"perm_granger\",\n    \"ty_granger\"\n  ],\n  \"main_result_6pair\": {\n    \"fpr_shapley\": {\n      \"naive_xcorr\": 0.621528,\n      \"diff_xcorr\": 0.163194,\n      \"threshold_onset\": 0.100694,\n      \"perm_granger\": 0.0,\n      \"ty_granger\": 0.03125\n    },\n    \"fnr_shapley\": {\n      \"naive_xcorr\": -0.41858,\n      \"diff_xcorr\": -0.305617,\n      \"threshold_onset\": -0.026914,\n      \"perm_granger\": -0.18,\n      \"ty_granger\": -0.068889\n    },\n    \"combined_shapley\": {\n      \"naive_xcorr\": 0.202948,\n      \"diff_xcorr\": -0.142423,\n      \"threshold_onset\": 0.07378,\n      \"perm_granger\": -0.18,\n      \"ty_granger\": -0.037639\n    }\n  },\n  \"robustness_8pair\": {\n    \"fpr_shapley\": {\n      \"naive_xcorr\": 0.621528,\n      \"diff_xcorr\": 0.163194,\n      \"threshold_onset\": 0.100694,\n      \"perm_granger\": 0.0,\n      \"ty_granger\": 0.03125\n    },\n    \"fnr_shapley\": {\n      \"naive_xcorr\": -0.451852,\n      \"diff_xcorr\": -0.269444,\n      \"threshold_onset\": -0.037963,\n      \"perm_granger\": -0.15162,\n      \"ty_granger\": -0.058565\n    },\n    \"combined_shapley\": {\n      \"naive_xcorr\": 0.169676,\n      \"diff_xcorr\": -0.10625,\n      \"threshold_onset\": 0.062731,\n      \"perm_granger\": -0.15162,\n      \"ty_granger\": -0.027315\n    }\n  },\n  \"raw_rates_8pair\": {\n    \"naive_xcorr\": {\n      \"fpr\": 0.9167,\n      \"fnr\": 0.0528,\n      \"fp_count\": 22,\n      \"fp_total\": 24,\n      \"fn_count\": 19,\n      \"fn_total\": 360\n    },\n    \"diff_xcorr\": {\n      \"fpr\": 0.375,\n      \"fnr\": 0.2528,\n      \"fp_count\": 9,\n      \"fp_total\": 24,\n      \"fn_count\": 91,\n      \"fn_total\": 360\n    },\n    \"threshold_onset\": {\n      \"fpr\": 0.25,\n      \"fnr\": 0.8889,\n      \"fp_count\": 6,\n      \"fp_total\": 24,\n      \"fn_count\": 320,\n      \"fn_total\": 360\n    },\n    \"perm_granger\": {\n      \"fpr\": 0.0,\n      \"fnr\": 0.5028,\n      \"fp_count\": 0,\n      \"fp_total\": 24,\n      \"fn_count\": 181,\n      \"fn_total\": 360\n    },\n    \"ty_granger\": {\n      \"fpr\": 0.0833,\n      \"fnr\": 0.7944,\n      \"fp_count\": 2,\n      \"fp_total\": 24,\n      \"fn_count\": 286,\n      \"fn_total\": 360\n    }\n  },\n  \"diagnostics\": {\n    \"null_s42_source\": \"17855:alpha_sweep/a000_s42_fp32\",\n    \"excluded_from_v2\": [\n      \"17855:alpha_sweep/a005_s42_fp32_v3_d080\",\n      \"17855:alpha_sweep/a060_s42_fp32_v3_d080\",\n      \"17855:alpha_sweep/a050_postd093_s42_fp32\",\n      \"17855:generalize/gpt2m_wiki_a100_s43_bf16\"\n    ],\n    \"deduped_from_v2\": {\n      \"19828:alpha_sweep/a000_s42\": \"replaced by 17855:alpha_sweep/a000_s42_fp32\",\n      \"19828:alpha_sweep/a010_s42\": \"replaced by 17855:alpha_sweep/a010_s42_fp32\",\n      \"19828:alpha_sweep/a025_s43\": \"replaced by 17855:alpha_sweep/a025_s43_fp32\",\n      \"19828:alpha_sweep/a025_s44\": \"replaced by 17855:alpha_sweep/a025_s44_fp32\",\n      \"19828:alpha_sweep/a050_s42\": \"replaced by 17855:alpha_sweep/a050_s42_fp32\",\n      \"19828:alpha_sweep/a050_s43\": \"replaced by 17855:alpha_sweep/a050_s43_fp32\",\n      \"19828:alpha_sweep/a050_s44\": \"replaced by 17855:alpha_sweep/a050_s44_fp32\",\n      \"19828:alpha_sweep/a075_s42\": \"replaced by 17855:alpha_sweep/a075_s42_fp32\"\n    }\n  }\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/shapley_v2/shapley_values_v2.json",
    "content": "{\n  \"version\": \"v3_dedup_fdr\",\n  \"generated_at\": \"2026-05-20T14:29:55.778865\",\n  \"data_sources\": [\n    \"17855:alpha_sweep/a000_s42_fp32\",\n    \"17855:alpha_sweep/a010_s42_fp32\",\n    \"17855:alpha_sweep/a010_s43_fp32\",\n    \"17855:alpha_sweep/a025_s42_fp32\",\n    \"17855:alpha_sweep/a025_s43_fp32\",\n    \"17855:alpha_sweep/a025_s44_fp32\",\n    \"17855:alpha_sweep/a030_s42_fp32\",\n    \"17855:alpha_sweep/a035_s42_fp32\",\n    \"17855:alpha_sweep/a040_s42_fp32\",\n    \"17855:alpha_sweep/a045_s42_fp32\",\n    \"17855:alpha_sweep/a050_s42_fp32\",\n    \"17855:alpha_sweep/a050_s43_fp32\",\n    \"17855:alpha_sweep/a050_s44_fp32\",\n    \"17855:alpha_sweep/a060_s42_fp32_v4\",\n    \"17855:alpha_sweep/a060_s43_fp32\",\n    \"17855:alpha_sweep/a075_s42_fp32\",\n    \"17855:alpha_sweep/c4_a025_s42_fp32\",\n    \"17855:alpha_sweep/c4_a050_s42_fp32\",\n    \"17855:alpha_sweep/c4_a075_s42_fp32\",\n    \"17855:generalize/pythia410m_wiki_a100_s43\",\n    \"17855:generalize/qwen35_08b_wiki_a100_s42_fp32_v2\",\n    \"17855:generalize/qwen35_08b_wiki_a100_s43_fp32\",\n    \"17855:generalize/smollm3_3b_wiki_a100_s43_17855\",\n    \"17855:padding_robustness/a100_s42_fp32\",\n    \"17855:scale/14b_c4_s42_fp32\",\n    \"17855:scale_check/pythia69b_wiki_a100_s42\",\n    \"17855:scale_check/pythia69b_wiki_a100_s43\",\n    \"19828:ablation/accumulate_a050_s43\",\n    \"19828:alpha_sweep/a000_s43\",\n    \"19828:alpha_sweep/a000_s44\",\n    \"19828:alpha_sweep/a055_s42_fp32\",\n    \"19828:alpha_sweep/a075_s43\",\n    \"19828:alpha_sweep/a075_s44\",\n    \"19828:alpha_sweep/c4_a050_s43_fp32\",\n    \"19828:alpha_sweep/c4_a075_s43_fp32\",\n    \"19828:gen_opt13b_wiki_a100_s43_fp32\",\n    \"19828:gen_wiki_gpt2m_a100_s43\",\n    \"19828:generalize/gpt2m_wiki_a100_s42\",\n    \"19828:generalize/opt1b_wiki_a100_s42\",\n    \"19828:generalize/pythia14b_wiki_a100_s42\",\n    \"19828:generalize/pythia14b_wiki_a100_s43\",\n    \"19828:generalize/pythia1b_c4_a100_s42\",\n    \"19828:generalize/pythia1b_c4_a100_s43\",\n    \"19828:generalize/pythia410m_wiki_a100_s42\",\n    \"19828:generalize/smollm3_3b_wiki_a100_s42_fp32_v3\",\n    \"19828:intervention/predictive_te_s42\",\n    \"19828:intervention/reactive_d1_s42\",\n    \"19828:scale_check/pythia14b_a050_s42\"\n  ],\n  \"dedup_rules\": [\n    \"exclude dir names matching v3_d080|postd093|bf16\",\n    \"same (dataset, alpha, seed) in alpha_sweep: prefer westd-17855 fp32\",\n    \"only true_3sigma_d105 threshold\"\n  ],\n  \"fdr_field_used\": {\n    \"naive_xcorr\": \"significant_fdr\",\n    \"diff_xcorr\": \"significant_fdr\",\n    \"threshold_onset\": \"significant (deterministic, no p-value)\",\n    \"perm_granger\": \"significant_fdr\",\n    \"ty_granger\": \"significant_fdr\"\n  },\n  \"threshold_criterion\": \"true_3sigma_d105\",\n  \"n_methods\": 5,\n  \"n_coalitions\": 32,\n  \"n_null_experiments\": 3,\n  \"n_signal_experiments\": 45,\n  \"n_null_obs\": 24,\n  \"n_signal_obs_6pair\": 270,\n  \"n_signal_obs_8pair\": 360,\n  \"fpr_pairs\": [\n    \"token_entropy->distinct_1\",\n    \"token_entropy->distinct_2\",\n    \"token_entropy->distinct_3\",\n    \"token_entropy->mauve\",\n    \"ece->distinct_1\",\n    \"ece->distinct_2\",\n    \"ece->distinct_3\",\n    \"ece->mauve\"\n  ],\n  \"fnr_pairs_6\": [\n    \"token_entropy->distinct_1\",\n    \"token_entropy->distinct_2\",\n    \"token_entropy->distinct_3\",\n    \"ece->distinct_1\",\n    \"ece->distinct_2\",\n    \"ece->distinct_3\"\n  ],\n  \"fnr_pairs_8\": [\n    \"token_entropy->distinct_1\",\n    \"token_entropy->distinct_2\",\n    \"token_entropy->distinct_3\",\n    \"token_entropy->mauve\",\n    \"ece->distinct_1\",\n    \"ece->distinct_2\",\n    \"ece->distinct_3\",\n    \"ece->mauve\"\n  ],\n  \"methods\": [\n    \"naive_xcorr\",\n    \"diff_xcorr\",\n    \"threshold_onset\",\n    \"perm_granger\",\n    \"ty_granger\"\n  ],\n  \"main_result_6pair\": {\n    \"fpr_shapley\": {\n      \"naive_xcorr\": 0.621528,\n      \"diff_xcorr\": 0.163194,\n      \"threshold_onset\": 0.100694,\n      \"perm_granger\": 0.0,\n      \"ty_granger\": 0.03125\n    },\n    \"fnr_shapley\": {\n      \"naive_xcorr\": -0.41858,\n      \"diff_xcorr\": -0.305617,\n      \"threshold_onset\": -0.026914,\n      \"perm_granger\": -0.18,\n      \"ty_granger\": -0.068889\n    },\n    \"combined_shapley\": {\n      \"naive_xcorr\": 0.202948,\n      \"diff_xcorr\": -0.142423,\n      \"threshold_onset\": 0.07378,\n      \"perm_granger\": -0.18,\n      \"ty_granger\": -0.037639\n    }\n  },\n  \"robustness_8pair\": {\n    \"fpr_shapley\": {\n      \"naive_xcorr\": 0.621528,\n      \"diff_xcorr\": 0.163194,\n      \"threshold_onset\": 0.100694,\n      \"perm_granger\": 0.0,\n      \"ty_granger\": 0.03125\n    },\n    \"fnr_shapley\": {\n      \"naive_xcorr\": -0.451852,\n      \"diff_xcorr\": -0.269444,\n      \"threshold_onset\": -0.037963,\n      \"perm_granger\": -0.15162,\n      \"ty_granger\": -0.058565\n    },\n    \"combined_shapley\": {\n      \"naive_xcorr\": 0.169676,\n      \"diff_xcorr\": -0.10625,\n      \"threshold_onset\": 0.062731,\n      \"perm_granger\": -0.15162,\n      \"ty_granger\": -0.027315\n    }\n  },\n  \"raw_rates_8pair\": {\n    \"naive_xcorr\": {\n      \"fpr\": 0.9167,\n      \"fnr\": 0.0528,\n      \"fp_count\": 22,\n      \"fp_total\": 24,\n      \"fn_count\": 19,\n      \"fn_total\": 360\n    },\n    \"diff_xcorr\": {\n      \"fpr\": 0.375,\n      \"fnr\": 0.2528,\n      \"fp_count\": 9,\n      \"fp_total\": 24,\n      \"fn_count\": 91,\n      \"fn_total\": 360\n    },\n    \"threshold_onset\": {\n      \"fpr\": 0.25,\n      \"fnr\": 0.8889,\n      \"fp_count\": 6,\n      \"fp_total\": 24,\n      \"fn_count\": 320,\n      \"fn_total\": 360\n    },\n    \"perm_granger\": {\n      \"fpr\": 0.0,\n      \"fnr\": 0.5028,\n      \"fp_count\": 0,\n      \"fp_total\": 24,\n      \"fn_count\": 181,\n      \"fn_total\": 360\n    },\n    \"ty_granger\": {\n      \"fpr\": 0.0833,\n      \"fnr\": 0.7944,\n      \"fp_count\": 2,\n      \"fp_total\": 24,\n      \"fn_count\": 286,\n      \"fn_total\": 360\n    }\n  },\n  \"diagnostics\": {\n    \"null_s42_source\": \"17855:alpha_sweep/a000_s42_fp32\",\n    \"excluded_from_v2\": [\n      \"17855:alpha_sweep/a005_s42_fp32_v3_d080\",\n      \"17855:alpha_sweep/a060_s42_fp32_v3_d080\",\n      \"17855:alpha_sweep/a050_postd093_s42_fp32\",\n      \"17855:generalize/gpt2m_wiki_a100_s43_bf16\"\n    ],\n    \"deduped_from_v2\": {\n      \"19828:alpha_sweep/a000_s42\": \"replaced by 17855:alpha_sweep/a000_s42_fp32\",\n      \"19828:alpha_sweep/a010_s42\": \"replaced by 17855:alpha_sweep/a010_s42_fp32\",\n      \"19828:alpha_sweep/a025_s43\": \"replaced by 17855:alpha_sweep/a025_s43_fp32\",\n      \"19828:alpha_sweep/a025_s44\": \"replaced by 17855:alpha_sweep/a025_s44_fp32\",\n      \"19828:alpha_sweep/a050_s42\": \"replaced by 17855:alpha_sweep/a050_s42_fp32\",\n      \"19828:alpha_sweep/a050_s43\": \"replaced by 17855:alpha_sweep/a050_s43_fp32\",\n      \"19828:alpha_sweep/a050_s44\": \"replaced by 17855:alpha_sweep/a050_s44_fp32\",\n      \"19828:alpha_sweep/a075_s42\": \"replaced by 17855:alpha_sweep/a075_s42_fp32\"\n    }\n  }\n}\n"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-20T14:33:05.283119+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/shapley_v2/shapley_values_v2.json has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-20T14:33:05.283308+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "cat > /tmp/plot_shapley.py << 'PYEOF'\nimport json\nimport matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nimport numpy as np\n\ndata = json.load(open('/tmp/shapley_v3_result.json'))\nmethods = data['methods']\nlabels = ['Naive\\nXCorr', 'Diff\\nXCorr', 'Threshold\\nOnset', 'Perm\\nGranger', 'TY\\nGranger']\n\nr6 = data['main_result_6pair']\nfpr_vals = [r6['fpr_shapley'][m] for m in methods]\nfnr_vals = [r6['fnr_shapley'][m] for m in methods]\ncombined_vals = [r6['combined_shapley'][m] for m in methods]\n\nfig, axes = plt.subplots(1, 3, figsize=(14, 4.5), sharey=False)\nx = np.arange(len(methods))\nw = 0.6\n\ncolors_fpr = ['#d62728' if v > 0.1 else '#ff7f0e' if v > 0.01 else '#2ca02c' for v in fpr_vals]\ncolors_fnr = ['#2ca02c' if v < -0.15 else '#ff7f0e' if v < -0.05 else '#d62728' for v in fnr_vals]\ncolors_comb = ['#d62728' if v > 0.05 else '#2ca02c' if v < -0.05 else '#ff7f0e' for v in combined_vals]\n\nax = axes[0]\nbars = ax.bar(x, fpr_vals, w, color=colors_fpr, edgecolor='black', linewidth=0.5)\nax.set_title('FPR Contribution', fontsize=12, fontweight='bold')\nax.set_ylabel('Shapley Value (FPR)', fontsize=10)\nax.set_xticks(x)\nax.set_xticklabels(labels, fontsize=8)\nax.axhline(y=0, color='black', linewidth=0.5)\nfor i, v in enumerate(fpr_vals):\n    ax.text(i, v + 0.01, f'{v:.3f}', ha='center', va='bottom', fontsize=7.5)\n\nax = axes[1]\nbars = ax.bar(x, fnr_vals, w, color=colors_fnr, edgecolor='black', linewidth=0.5)\nax.set_title('FNR Contribution (6-pair)', fontsize=12, fontweight='bold')\nax.set_ylabel('Shapley Value (FNR)', fontsize=10)\nax.set_xticks(x)\nax.set_xticklabels(labels, fontsize=8)\nax.axhline(y=0, color='black', linewidth=0.5)\nfor i, v in enumerate(fnr_vals):\n    ax.text(i, v - 0.015, f'{v:.3f}', ha='center', va='top', fontsize=7.5)\n\nax = axes[2]\nbars = ax.bar(x, combined_vals, w, color=colors_comb, edgecolor='black', linewidth=0.5)\nax.set_title('Combined (FPR + FNR)', fontsize=12, fontweight='bold')\nax.set_ylabel('Shapley Value (Combined)', fontsize=10)\nax.set_xticks(x)\nax.set_xticklabels(labels, fontsize=8)\nax.axhline(y=0, color='black', linewidth=0.5)\nfor i, v in enumerate(combined_vals):\n    offset = 0.008 if v >= 0 else -0.015\n    va = 'bottom' if v >= 0 else 'top'\n    ax.text(i, v + offset, f'{v:.3f}', ha='center', va=va, fontsize=7.5)\n\nfig.suptitle(f'Shapley Method Contribution Analysis (v3: {data[\"n_null_experiments\"]} null + {data[\"n_signal_experiments\"]} signal experiments, FDR-corrected)',\n             fontsize=11, y=1.02)\nplt.tight_layout()\nplt.savefig('/tmp/shapley_method_contribution.pdf', bbox_inches='tight', dpi=150)\nplt.savefig('/tmp/shapley_method_contribution.png', bbox_inches='tight', dpi=150)\nprint(\"Figures saved\")\nPYEOF\npython3 /tmp/plot_shapley.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat > /tmp/plot_shapley.py << 'PYEOF'\nimport json\nimport matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nimport numpy as np\n\ndata = json.load(open('/tmp/shapley_v3_result.json'))\nmethods = data['methods']\nlabels = ['Naive\\nXCorr', 'Diff\\nXCorr', 'Threshold\\nOnset', 'Perm\\nGranger', 'TY\\nGranger']\n\nr6 = data['main_result_6pair']\nfpr_vals = [r6['fpr_shapley'][m] for m in methods]\nfnr_vals = [r6['fnr_shapley'][m] for m in methods]\ncombined_vals = [r6['combined_shapley'][m] for m in methods]\n\nfig, axes = plt.subplots(1, 3, figsize=(14, 4.5), sharey=False)\nx = np.arange(len(methods))\nw = 0.6\n\ncolors_fpr = ['#d62728' if v > 0.1 else '#ff7f0e' if v > 0.01 else '#2ca02c' for v in fpr_vals]\ncolors_fnr = ['#2ca02c' if v < -0.15 else '#ff7f0e' if v < -0.05 else '#d62728' for v in fnr_vals]\ncolors_comb = ['#d62728' if v > 0.05 else '#2ca02c' if v < -0.05 else '#ff7f0e' for v in combined_vals]\n\nax = axes[0]\nbars = ax.bar(x, fpr_vals, w, color=colors_fpr, edgecolor='black', linewidth=0.5)\nax.set_title('FPR Contribution', fontsize=12, fontweight='bold')\nax.set_ylabel('Shapley Value (FPR)', fontsize=10)\nax.set_xticks(x)\nax.set_xticklabels(labels, fontsize=8)\nax.axhline(y=0, color='black', linewidth=0.5)\nfor i, v in enumerate(fpr_vals):\n    ax.text(i, v + 0.01, f'{v:.3f}', ha='center', va='bottom', fontsize=7.5)\n\nax = axes[1]\nbars = ax.bar(x, fnr_vals, w, color=colors_fnr, edgecolor='black', linewidth=0.5)\nax.set_title('FNR Contribution (6-pair)', fontsize=12, fontweight='bold')\nax.set_ylabel('Shapley Value (FNR)', fontsize=10)\nax.set_xticks(x)\nax.set_xticklabels(labels, fontsize=8)\nax.axhline(y=0, color='black', linewidth=0.5)\nfor i, v in enumerate(fnr_vals):\n    ax.text(i, v - 0.015, f'{v:.3f}', ha='center', va='top', fontsize=7.5)\n\nax = axes[2]\nbars = ax.bar(x, combined_vals, w, color=colors_comb, edgecolor='black', linewidth=0.5)\nax.set_title('Combined (FPR + FNR)', fontsize=12, fontweight='bold')\nax.set_ylabel('Shapley Value (Combined)', fontsize=10)\nax.set_xticks(x)\nax.set_xticklabels(labels, fontsize=8)\nax.axhline(y=0, color='black', linewidth=0.5)\nfor i, v in enumerate(combined_vals):\n    offset = 0.008 if v >= 0 else -0.015\n    va = 'bottom' if v >= 0 else 'top'\n    ax.text(i, v + offset, f'{v:.3f}', ha='center', va=va, fontsize=7.5)\n\nfig.suptitle(f'Shapley Method Contribution Analysis (v3: {data[\"n_null_experiments\"]} null + {data[\"n_signal_experiments\"]} signal experiments, FDR-corrected)',\n             fontsize=11, y=1.02)\nplt.tight_layout()\nplt.savefig('/tmp/shapley_method_contribution.pdf', bbox_inches='tight', dpi=150)\nplt.savefig('/tmp/shapley_method_contribution.png', bbox_inches='tight', dpi=150)\nprint(\"Figures saved\")\nPYEOF\npython3 /tmp/plot_shapley.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-20T14:33:05.283577+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'cat > /tmp/plot_shapley.py << \\\\'PYEOF\\\\'\\\\nimport json\\\\nimport matplotlib\\\\nmatplotlib.use(\\\\'Agg\\\\')\\\\nimport matplotlib.pyplot as plt\\\\nimport numpy as np\\\\n\\\\ndata = json.load(open(\\\\'/tmp/shapley_v3_result.json\\\\'))\\\\nmethods = data[\\\\'methods\\\\']\\\\nlabels = [\\\\'Naive\\\\\\\\nXCorr\\\\', \\\\'Diff\\\\\\\\nXCorr\\\\', \\\\'Threshold\\\\\\\\nOnset\\\\', \\\\'Perm\\\\\\\\nGranger\\\\', \\\\'TY\\\\\\\\nGranger\\\\']\\\\n\\\\nr6 = data[\\\\'main_result_6pair\\\\']\\\\nfpr_vals = [r6[\\\\'fpr_shapley\\\\'][m] for m in methods]\\\\nfnr_vals = [r6[\\\\'fnr_shapley\\\\'][m] for m in methods]\\\\ncombined_vals = [r6[\\\\'combined_shapley\\\\'][m] for m in methods]\\\\n\\\\nfig, axes = plt.subplots(1, 3, figsize=(14, 4.5), sharey=False)\\\\nx = np.arange(len(methods))\\\\nw = 0.6\\\\n\\\\ncolors_fpr = [\\\\'#d62728\\\\' if v > 0.1 else \\\\'#ff7f0e\\\\' if v > 0.01 else \\\\'#2ca02c\\\\' for v in fpr_vals]\\\\ncolors_fnr = [\\\\'#2ca02c\\\\' if v < -0.15 else \\\\'#ff7f0e\\\\' if v < -0.05 else \\\\'#d62728\\\\' for v in fnr_vals]\\\\ncolors_comb = [\\\\'#d62728\\\\' if v > 0.05 else \\\\'#2ca02c\\\\' if v < -0.05 else \\\\'#ff7f0e\\\\' for v in combined_vals]\\\\n\\\\nax = axes[0]\\\\nbars = ax.bar(x, fpr_vals, w, color=colors_fpr, edgecolor=\\\\'black\\\\', linewidth=0.5)\\\\nax.set_title(\\\\'FPR Contribution\\\\', fontsize=12, fontweight=\\\\'bold\\\\')\\\\nax.set_ylabel(\\\\'Shapley Value (FPR)\\\\', fontsize=10)\\\\nax.set_xticks(x)\\\\nax.set_xticklabels(labels, fontsize=8)\\\\nax.axhline(y=0, color=\\\\'black\\\\', linewidth=0.5)\\\\nfor i, v in enumerate(fpr_vals):\\\\n    ax.text(i, v + 0.01, f\\\\'{v:.3f}\\\\', ha=\\\\'center\\\\', va=\\\\'bottom\\\\', fontsize=7.5)\\\\n\\\\nax = axes[1]\\\\nbars = ax.bar(x, fnr_vals, w, color=colors_fnr, edgecolor=\\\\'black\\\\', linewidth=0.5)\\\\nax.set_title(\\\\'FNR Contributi
…[truncated 1831 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-20T14:33:05.283751+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "pip install matplotlib -q 2>&1 | tail -3",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "pip install matplotlib -q 2>&1 | tail -3",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-20T14:33:05.283892+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"bash: line 1: pip: command not found\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.01}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-20T14:33:05.284022+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && pip install matplotlib -q 2>&1 | tail -3 && python3 /tmp/plot_shapley.py",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && pip install matplotlib -q 2>&1 | tail -3 && python3 /tmp/plot_shapley.py",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-20T14:33:05.284159+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv\\nFigures saved\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.97}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-20T14:33:05.284339+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "cp /tmp/shapley_method_contribution.pdf /root/autodl-tmp/distrib_canary_collapse/results/shapley_method_contribution_v3.pdf && cp /tmp/shapley_method_contribution.png /root/autodl-tmp/distrib_canary_collapse/results/shapley_method_contribution_v3.png && echo \"Copied to server results dir\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "cp /tmp/shapley_method_contribution.pdf /root/autodl-tmp/distrib_canary_collapse/results/shapley_method_contribution_v3.pdf && cp /tmp/shapley_method_contribution.png /root/autodl-tmp/distrib_canary_collapse/results/shapley_method_contribution_v3.png && echo \"Copied to server results dir\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-20T14:33:05.284488+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Copied to server results dir\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-20T14:33:05.284615+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport base64, gzip\ndata = open('/tmp/shapley_method_contribution.pdf','rb').read()\ncompressed = gzip.compress(data)\nprint(base64.b64encode(compressed).decode())\n\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport base64, gzip\ndata = open('/tmp/shapley_method_contribution.pdf','rb').read()\ncompressed = gzip.compress(data)\nprint(base64.b64encode(compressed).decode())\n\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-20T14:33:05.284799+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"H4sIAODFDWoC/6y8BVSVS982rnQjLb2Rkt7FppHu7pYO6RQJpUNCukO6BQRFUrpTkA4J6VBAQQT5Nuh5nvO9Z3//l3XWf7GGu/bM/OqeuWbmmptRRUKKA8QJxWIsnweUNWCBAECAo+kjLEFBAJfGEycLAJe4iZuJnaMVgEvFxMrCFQCG/0ANICyMZeFgfvVD3r9lkHJ0cANArn/ApaNs+sjCzA3A8/tS0tNNWt3NxM0CAP19Q8XEzc3CxQHAfXWJxaVubWJu42AFgP156uJopm7hBtCHn0pIwUWx8HQDcMnaw0UQ+3MU/3OUBRj+TRzQPxW4kvvqv4sFXLrf4nOpWbg6uruYwfXh/V2/ooW5jYmYoye8RiD8DwQEAjmh3LwgMDcAAuHmBEMhMPipIdwccB3hBbkC+H6XJOrg4Ai/AgH/h134/iaHgoWDlZs1APSncikbO7jq8KMd3B4SFmaO5hZXGV3dXCxM7LE8M4b05pSoZAl9KyuLpUc5tyKbpPbTuWzl6Sse2+XNkO/tIgfOwbSQYcYjg0sH4dsh/bul/Y8U6rrFAGcqJOTMXM58a3lWEZVWRRFTXFm1ykvQF2fKRVO4b2i/XrR83JP2uVxU+4m0dEAZpbyBa1OReKTQvXr0+tSuQrt7xu9hsmfT6WmOzSL3C5qOUe5F7zHocOld7UqbxN4Bs40oRi0TIqP1qnAtGyP9vShiJ57pDQ87DKJMuQpnKdVP3x+N/SpqtqYVgmU+fG4P9owOtK+95xhH//y2gmboioXyHsm61JNBHE/ig9ofAkPdAoqrgQHJWdjtg8/zPIixW4QeIbEchMt+EsBGxXqrnKa997gnWabsJQuvPpDpnWw4tbooXyARC3raMOY8Zd/yQZJr6yiTJLXcMAurY8CpkdP+cms/0CYa6UTK5fR2BgvFQVwh8SeXjVdK5YZfkxWHZx4ePk6LepzWraLW3XNXrW3GU23XcPTzZFZAT6SgH6TNBv1ZY3CEk16l4aQBIQetHQ8NigAK6UiWfX1EBd7z6aA4yRftLMooue0VPLEdj+cdkjFFkxk2WVsMUYIWwnjuFWgoObxIK57f+1IlvXcwZHU+sRcbwt2JuSIRSU9cXxCWSeXr7bUoyOdAI1SUNLf62ND8wdO58zohzycu392dp39VCv3K+bHhfPSoQwNDmP+7qRwSsfPQ5EgoR1PnPukSXpaREXX/6dM3YejaP+5Tr4YoqGBuMaQc7h47ZbKZYLvjqx1nrPcJC3ifOASwxWqz6BYmlvjGWKh14xw+RBuJwSXEbUS3Cqd55oeMNlITv4FHOkXLmexYVByan1G9EH/UdOnr3PyO/DVE5mIRfQU8Y+GUmQky0g3sq0KL9chafhHKoVC5S83e3/cgG8BKEIo0rxsFGvnW9bGv62dXrx6F0vMZuteJdt6eIRwCM/ZtKD3ddtVZ7xVUxV46N+egq1BUDmdIXYDuD0thbM3FimbADACGZ35h+pS05CpmSwDoxuqJta+PuZqZmPEqkEWTuXgdxWaXU56TROnYegHzQ365+21lCsdSo5RSsl6abqbQAo75zWXyB+xsoRdhrM8J2m2fTpfSgljYCnTqmcGe3S/um4g0ptx9UPb0XRptCJIevuO7eUpywRq+vuJPM7HV5mUOp6WUNFvUqvkGiTSZzu2MJOJVw12bO/rQhB6jXapwSRdWpsZF61j3i6bmH06HNvWnNReYLGzFmr2Cuk91a9/TCF5+/VYZ+gOwpPYk9XuoO3kNZzXsbMCb++lQepMY4bive23UTDgagaU0umD2LvRrty81LXUjfwDp0x3WGP6kAx5WoAcNtbv2IF15SZB9oIG/WyoHr9qS8cZdiO7WS9OoScYgJg1+lpe8+Lx37wfYLzChClhATPe+PWJqvZMucG8dxd4S51Fav203Cwzze27+owgY7zKE8HGKM+HnT+av
…[truncated 6204 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-20T14:33:05.284961+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"import matplotlib; print(matplotlib.__version__)\" 2>&1 || echo \"NO_MATPLOTLIB\"",
  "description": "Check if matplotlib is available locally"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"import matplotlib; print(matplotlib.__version__)\" 2>&1 || echo \"NO_MATPLOTLIB\"",
    "description": "Check if matplotlib is available locally"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-20T14:33:05.285089+00:00_

3.10.9

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-20T14:33:05.285229+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/tmp/plot_shapley_v3.py",
  "content": "import json\nimport matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nimport numpy as np\n\ndata = json.load(open('/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/shapley_v2/shapley_values_v2.json'))\nmethods = data['methods']\nlabels = ['Naive\\nXCorr', 'Diff\\nXCorr', 'Threshold\\nOnset', 'Perm\\nGranger', 'TY\\nGranger']\n\nr6 = data['main_result_6pair']\nfpr_vals = [r6['fpr_shapley'][m] for m in methods]\nfnr_vals = [r6['fnr_shapley'][m] for m in methods]\ncombined_vals = [r6['combined_shapley'][m] for m in methods]\n\nfig, axes = plt.subplots(1, 3, figsize=(14, 4.5), sharey=False)\nx = np.arange(len(methods))\nw = 0.6\n\ncolors_fpr = ['#d62728' if v > 0.1 else '#ff7f0e' if v > 0.01 else '#2ca02c' for v in fpr_vals]\ncolors_fnr = ['#2ca02c' if v < -0.15 else '#ff7f0e' if v < -0.05 else '#d62728' for v in fnr_vals]\ncolors_comb = ['#d62728' if v > 0.05 else '#2ca02c' if v < -0.05 else '#ff7f0e' for v in combined_vals]\n\nax = axes[0]\nax.bar(x, fpr_vals, w, color=colors_fpr, edgecolor='black', linewidth=0.5)\nax.set_title('FPR Contribution', fontsize=12, fontweight='bold')\nax.set_ylabel('Shapley Value (FPR)', fontsize=10)\nax.set_xticks(x)\nax.set_xticklabels(labels, fontsize=8)\nax.axhline(y=0, color='black', linewidth=0.5)\nfor i, v in enumerate(fpr_vals):\n    ax.text(i, v + 0.01, f'{v:.3f}', ha='center', va='bottom', fontsize=7.5)\n\nax = axes[1]\nax.bar(x, fnr_vals, w, color=colors_fnr, edgecolor='black', linewidth=0.5)\nax.set_title('FNR Contribution (6-pair)', fontsize=12, fontweight='bold')\nax.set_ylabel('Shapley Value (FNR)', fontsize=10)\nax.set_xticks(x)\nax.set_xticklabels(labels, fontsize=8)\nax.axhline(y=0, color='black', linewidth=0.5)\nfor i, v in enumerate(fnr_vals):\n    ax.text(i, v - 0.015, f'{v:.3f}', ha='center', va='top', fontsize=7.5)\n\nax = axes[2]\nax.bar(x, combined_vals, w, color=colors_comb, edgecolor='black', linewidth=0.5)\nax.set_title('Combined (FPR + FNR)', fontsize=12, fontweight='bold')\nax.set_ylabel('Shapley Value (Combined)', fontsize=10)\nax.set_xticks(x)\nax.set_xticklabels(labels, fontsize=8)\nax.axhline(y=0, color='black', linewidth=0.5)\nfor i, v in enumerate(combined_vals):\n    offset = 0.008 if v >= 0 else -0.015\n    va = 'bottom' if v >= 0 else 'top'\n    ax.text(i, v + offset, f'{v:.3f}', ha='center', va=va, fontsize=7.5)\n\nfig.suptitle(f'Shapley Method Contribution Analysis (v3: {data[\"n_null_experiments\"]} null + {data[\"n_signal_experiments\"]} signal experiments, FDR-corrected)',\n             fontsize=11, y=1.02)\nplt.tight_layout()\n\nout_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/shapley_v2'\nplt.savefig(f'{out_dir}/shapley_method_contribution.pdf', bbox_inches='tight', dpi=150)\nplt.savefig(f'{out_dir}/shapley_method_contribution.png', bbox_inches='tight', dpi=150)\nprint(\"Figures saved\")\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "Write",
  "tool_args": {
    "file_path": "/tmp/plot_shapley_v3.py",
    "content": "import json\nimport matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nimport numpy as np\n\ndata = json.load(open('/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/shapley_v2/shapley_values_v2.json'))\nmethods = data['methods']\nlabels = ['Naive\\nXCorr', 'Diff\\nXCorr', 'Threshold\\nOnset', 'Perm\\nGranger', 'TY\\nGranger']\n\nr6 = data['main_result_6pair']\nfpr_vals = [r6['fpr_shapley'][m] for m in methods]\nfnr_vals = [r6['fnr_shapley'][m] for m in methods]\ncombined_vals = [r6['combined_shapley'][m] for m in methods]\n\nfig, axes = plt.subplots(1, 3, figsize=(14, 4.5), sharey=False)\nx = np.arange(len(methods))\nw = 0.6\n\ncolors_fpr = ['#d62728' if v > 0.1 else '#ff7f0e' if v > 0.01 else '#2ca02c' for v in fpr_vals]\ncolors_fnr = ['#2ca02c' if v < -0.15 else '#ff7f0e' if v < -0.05 else '#d62728' for v in fnr_vals]\ncolors_comb = ['#d62728' if v > 0.05 else '#2ca02c' if v < -0.05 else '#ff7f0e' for v in combined_vals]\n\nax = axes[0]\nax.bar(x, fpr_vals, w, color=colors_fpr, edgecolor='black', linewidth=0.5)\nax.set_title('FPR Contribution', fontsize=12, fontweight='bold')\nax.set_ylabel('Shapley Value (FPR)', fontsize=10)\nax.set_xticks(x)\nax.set_xticklabels(labels, fontsize=8)\nax.axhline(y=0, color='black', linewidth=0.5)\nfor i, v in enumerate(fpr_vals):\n    ax.text(i, v + 0.01, f'{v:.3f}', ha='center', va='bottom', fontsize=7.5)\n\nax = axes[1]\nax.bar(x, fnr_vals, w, color=colors_fnr, edgecolor='black', linewidth=0.5)\nax.set_title('FNR Contribution (6-pair)', fontsize=12, fontweight='bold')\nax.set_ylabel('Shapley Value (FNR)', fontsize=10)\nax.set_xticks(x)\nax.set_xticklabels(labels, fontsize=8)\nax.axhline(y=0, color='black', linewidth=0.5)\nfor i, v in enumerate(fnr_vals):\n    ax.text(i, v - 0.015, f'{v:.3f}', ha='center', va='top', fontsize=7.5)\n\nax = axes[2]\nax.bar(x, combined_vals, w, color=colors_comb, edgecolor='black', linewidth=0.5)\nax.set_title('Combined (FPR + FNR)', fontsize=12, fontweight='bold')\nax.set_ylabel('Shapley Value (Combined)', fontsize=10)\nax.set_xticks(x)\nax.set_xticklabels(labels, fontsize=8)\nax.axhline(y=0, color='black', linewidth=0.5)\nfor i, v in enumerate(combined_vals):\n    offset = 0.008 if v >= 0 else -0.015\n    va = 'bottom' if v >= 0 else 'top'\n    ax.text(i, v + offset, f'{v:.3f}', ha='center', va=va, fontsize=7.5)\n\nfig.suptitle(f'Shapley Method Contribution Analysis (v3: {data[\"n_null_experiments\"]} null + {data[\"n_signal_experiments\"]} signal experiments, FDR-corrected)',\n             fontsize=11, y=1.02)\nplt.tight_layout()\n\nout_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/shapley_v2'\nplt.savefig(f'{out_dir}/shapley_method_contribution.pdf', bbox_inches='tight', dpi=150)\nplt.savefig(f'{out_dir}/shapley_method_contribution.png', bbox_inches='tight', dpi=150)\nprint(\"Figures saved\")\n"
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-20T14:33:05.285406+00:00_

File created successfully at: /tmp/plot_shapley_v3.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-20T14:33:05.285524+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 /tmp/plot_shapley_v3.py",
  "description": "Generate Shapley v3 figure locally"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 /tmp/plot_shapley_v3.py",
    "description": "Generate Shapley v3 figure locally"
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-20T14:33:05.285640+00:00_

Figures saved

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-20T14:33:05.285757+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/shapley_v2/shapley_method_contribution.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/shapley_v2/shapley_method_contribution.png"
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-20T14:33:05.286387+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-20T14:33:05.286666+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\nd = json.load(open('/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/shapley_v2/shapley_values_v2.json'))\n\nprint('=== VERIFICATION ===')\nprint(f'Version: {d[\\\"version\\\"]}')\nprint(f'Experiments: {d[\\\"n_null_experiments\\\"]} null + {d[\\\"n_signal_experiments\\\"]} signal = {d[\\\"n_null_experiments\\\"] + d[\\\"n_signal_experiments\\\"]} total')\nprint(f'Data sources: {len(d[\\\"data_sources\\\"])}')\n\n# Check 1: no non-standard variants\nimport re\nbad = [s for s in d['data_sources'] if re.search(r'v3_d080|postd093|bf16', s)]\nprint(f'\\n[CHECK 1] Non-standard variants in sources: {bad if bad else \\\"NONE (PASS)\\\"}')\n\n# Check 2: alpha=0.00 seed=42 only once\nnull_s42 = [s for s in d['data_sources'] if 'a000_s42' in s and 'alpha_sweep' in s]\nprint(f'[CHECK 2] alpha=0.00 seed=42 entries: {null_s42} ({\\\"PASS\\\" if len(null_s42) == 1 else \\\"FAIL\\\"})')\n\n# Check 3: perm_granger FPR ~ 0\npg_fpr = d['main_result_6pair']['fpr_shapley']['perm_granger']\nprint(f'[CHECK 3] perm_granger FPR Shapley: {pg_fpr} ({\\\"PASS\\\" if pg_fpr == 0.0 else \\\"FAIL\\\"})')\nprint(f'          perm_granger raw FPR: {d[\\\"raw_rates_8pair\\\"][\\\"perm_granger\\\"][\\\"fpr\\\"]} ({d[\\\"raw_rates_8pair\\\"][\\\"perm_granger\\\"][\\\"fp_count\\\"]}/{d[\\\"raw_rates_8pair\\\"][\\\"perm_granger\\\"][\\\"fp_total\\\"]})')\n\n# Check 4: FDR field documented\nprint(f'[CHECK 4] FDR field used: {d[\\\"fdr_field_used\\\"][\\\"perm_granger\\\"]}')\n\n# Check 5: Shapley sum = grand coalition - empty\nfpr_sum = sum(d['main_result_6pair']['fpr_shapley'].values())\nfnr_sum = sum(d['main_result_6pair']['fnr_shapley'].values())\nprint(f'[CHECK 5] FPR Shapley sum: {fpr_sum:.6f} (should be ~0.917)')\nprint(f'          FNR Shapley sum: {fnr_sum:.6f} (should be ~-1.000)')\n\n# Summary comparison v2 vs v3\nprint(f'\\n=== V2 -> V3 CHANGES ===')\nprint(f'Sources: 60 -> {len(d[\\\"data_sources\\\"])} (excluded {len(d[\\\"diagnostics\\\"][\\\"excluded_from_v2\\\"])} non-standard, deduped {len(d[\\\"diagnostics\\\"][\\\"deduped_from_v2\\\"])})')\nprint(f'Null experiments: 4 -> {d[\\\"n_null_experiments\\\"]} (deduped a000_s42)')\nprint(f'Signal experiments: 56 -> {d[\\\"n_signal_experiments\\\"]}')\n\"\n",
  "description": "Run verification checks on the final output"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\nd = json.load(open('/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/shapley_v2/shapley_values_v2.json'))\n\nprint('=== VERIFICATION ===')\nprint(f'Version: {d[\\\"version\\\"]}')\nprint(f'Experiments: {d[\\\"n_null_experiments\\\"]} null + {d[\\\"n_signal_experiments\\\"]} signal = {d[\\\"n_null_experiments\\\"] + d[\\\"n_signal_experiments\\\"]} total')\nprint(f'Data sources: {len(d[\\\"data_sources\\\"])}')\n\n# Check 1: no non-standard variants\nimport re\nbad = [s for s in d['data_sources'] if re.search(r'v3_d080|postd093|bf16', s)]\nprint(f'\\n[CHECK 1] Non-standard variants in sources: {bad if bad else \\\"NONE (PASS)\\\"}')\n\n# Check 2: alpha=0.00 seed=42 only once\nnull_s42 = [s for s in d['data_sources'] if 'a000_s42' in s and 'alpha_sweep' in s]\nprint(f'[CHECK 2] alpha=0.00 seed=42 entries: {null_s42} ({\\\"PASS\\\" if len(null_s42) == 1 else \\\"FAIL\\\"})')\n\n# Check 3: perm_granger FPR ~ 0\npg_fpr = d['main_result_6pair']['fpr_shapley']['perm_granger']\nprint(f'[CHECK 3] perm_granger FPR Shapley: {pg_fpr} ({\\\"PASS\\\" if pg_fpr == 0.0 else \\\"FAIL\\\"})')\nprint(f'          perm_granger raw FPR: {d[\\\"raw_rates_8pair\\\"][\\\"perm_granger\\\"][\\\"fpr\\\"]} ({d[\\\"raw_rates_8pair\\\"][\\\"perm_granger\\\"][\\\"fp_count\\\"]}/{d[\\\"raw_rates_8pair\\\"][\\\"perm_granger\\\"][\\\"fp_total\\\"]})')\n\n# Check 4: FDR field documented\nprint(f'[CHECK 4] FDR field used: {d[\\\"fdr_field_used\\\"][\\\"perm_granger\\\"]}')\n\n# Check 5: Shapley sum = grand coalition - empty\nfpr_sum = sum(d['main_result_6pair']['fpr_shapley'].values())\nfnr_sum = sum(d['main_result_6pair']['fnr_shapley'].values())\nprint(f'[CHECK 5] FPR Shapley sum: {fpr_sum:.6f} (should be ~0.917)')\nprint(f'          FNR Shapley sum: {fnr_sum:.6f} (should be ~-1.000)')\n\n# Summary comparison v2 vs v3\nprint(f'\\n=== V2 -> V3 CHANGES ===')\nprint(f'Sources: 60 -> {len(d[\\\"data_sources\\\"])} (excluded {len(d[\\\"diagnostics\\\"][\\\"excluded_from_v2\\\"])} non-standard, deduped {len(d[\\\"diagnostics\\\"][\\\"deduped_from_v2\\\"])})')\nprint(f'Null experiments: 4 -> {d[\\\"n_null_experiments\\\"]} (deduped a000_s42)')\nprint(f'Signal experiments: 56 -> {d[\\\"n_signal_experiments\\\"]}')\n\"\n",
    "description": "Run verification checks on the final output"
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-20T14:33:05.286890+00:00_

=== VERIFICATION ===
Version: v3_dedup_fdr
Experiments: 3 null + 45 signal = 48 total
Data sources: 48

[CHECK 1] Non-standard variants in sources: NONE (PASS)
[CHECK 2] alpha=0.00 seed=42 entries: ['17855:alpha_sweep/a000_s42_fp32'] (PASS)
[CHECK 3] perm_granger FPR Shapley: 0.0 (PASS)
          perm_granger raw FPR: 0.0 (0/24)
[CHECK 4] FDR field used: significant_fdr
[CHECK 5] FPR Shapley sum: 0.916666 (should be ~0.917)
          FNR Shapley sum: -1.000000 (should be ~-1.000)

=== V2 -> V3 CHANGES ===
Sources: 60 -> 48 (excluded 4 non-standard, deduped 8)
Null experiments: 4 -> 3 (deduped a000_s42)
Signal experiments: 56 -> 45

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 85 · 2026-05-20T14:33:05.287139+00:00_

All checks pass. Here's the summary:

**Shapley v3 完成。**

**修复内容：**
- **排除 4 个非标准变体**: `a005_s42_fp32_v3_d080`, `a060_s42_fp32_v3_d080`, `a050_postd093_s42_fp32`, `gpt2m_wiki_a100_s43_bf16`
- **去重 8 个 alpha_sweep 条目**: 同一 (dataset, alpha, seed) 保留 17855 fp32 版本（含 α=0.00 s42 去重）
- **FDR 字段已验证**: 4 个 p-value 方法使用 `significant_fdr`，threshold_onset 使用 `significant`（确定性，无 p-value）

**数据规模变化**: 60 → 48 experiments, null 4→3, signal 56→45

**验证通过**:
- 无 v3_d080/postd093/bf16 污染
- α=0.00 s42 仅 1 条（17855 fp32）
- perm_granger FPR Shapley = 0.000（raw 0/24）
- Shapley sum 精确匹配 grand coalition

**输出文件**:
- `artifacts/shapley_v2/shapley_values_v2.json` — 已覆盖为 v3 内容
- `artifacts/shapley_v2/shapley_method_contribution.pdf` — 已重画

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_d150_shapley_v3_dedup_fdr_20260520T142236"
}
```

</details>

---
