# analysis d150 p02 a045 seed count

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 57
- **Recorded user turns:** 0
- **Tool calls:** 28
- **Original source:** `logs/chats/worker_analysis_d150_p02_a045_seed_count_20260520T132027.jsonl`
- **Structured JSON:** [`240b4ea6ac80b7bcb0d2.json`](../../sessions/24/240b4ea6ac80b7bcb0d2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

57 recorded events

### Tool call

_source line 1 · 2026-05-20T13:22:32.365706+00:00_

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
  "session": "worker_analysis_d150_p02_a045_seed_count_20260520T132027",
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

_source line 2 · 2026-05-20T13:22:32.368641+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_p02_a045_seed_count_20260520T132027",
  "tool": "ToolSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T13:22:32.368949+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "artifacts/*a045*/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_p02_a045_seed_count_20260520T132027",
  "tool": "Glob",
  "tool_args": {
    "pattern": "artifacts/*a045*/**",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T13:22:32.369155+00:00_

artifacts/alpha_sweep_a045_s42_fp32/report/analysis_alpha_sweep_a045_s42_fp32.md
artifacts/alpha_sweep_a045_s42_fp32/report/analysis_alpha_sweep_a045_s42_fp32_e27341.md
artifacts/alpha_sweep_a045_s43_fp32/analysis_report.md
artifacts/alpha_sweep_a045_s43_fp32/report/analysis_report.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_p02_a045_seed_count_20260520T132027",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T13:22:32.369437+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "find /root/distrib_canary_collapse -maxdepth 3 -type d -name \"*a045*\" 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_p02_a045_seed_count_20260520T132027",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "find /root/distrib_canary_collapse -maxdepth 3 -type d -name \"*a045*\" 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T13:22:32.369679+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_p02_a045_seed_count_20260520T132027",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T13:22:32.369894+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "find /root/autodl-tmp/distrib_canary_collapse -maxdepth 3 -type d -name \"*a045*\" 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_p02_a045_seed_count_20260520T132027",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "find /root/autodl-tmp/distrib_canary_collapse -maxdepth 3 -type d -name \"*a045*\" 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T13:22:32.370109+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_p02_a045_seed_count_20260520T132027",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T13:22:32.370335+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/alpha_sweep_a045_s42_fp32/report/analysis_alpha_sweep_a045_s42_fp32.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_p02_a045_seed_count_20260520T132027",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/alpha_sweep_a045_s42_fp32/report/analysis_alpha_sweep_a045_s42_fp32.md"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T13:22:32.370680+00:00_

1	# Analysis: alpha_sweep_a045_s42_fp32
2	
3	## 1. Config
4	
5	| Key | Value |
6	|-----|-------|
7	| Model | EleutherAI/pythia-410m |
8	| Dataset | WikiText-103 (5k subset) |
9	| α (synthetic_ratio) | 0.45 |
10	| Seed | 42 |
11	| Precision | fp32 |
12	| Generations | 10 (gen_0–gen_10) |
13	| Steps/gen | 5,000 |
14	| LR | 5e-5 |
15	| Batch size | 4 |
16	| Server | westd-17855 |
17	
18	## 2. Hypothesis
19	
20	α=0.45 is an onset-refinement point between α=0.40 (PermG=0/8, blind zone) and α=0.50 (PermG=6/8, detected). If PermG>0, onset ∈ [0.40, 0.45]; if PermG=0, onset ∈ [0.45, 0.50].
21	
22	## 3. Result Summary
23	
24	**PermG fwd (FDR) = 0/8. Onset boundary narrowed to [0.45, 0.50].**
25	
26	The entropy/ECE canaries do not Granger-cause diversity metrics at α=0.45 after FDR correction. However, multiple raw PermG p-values fall in [0.030, 0.070] — marginally sub-threshold — suggesting α=0.45 is near but below the detection onset.
27	
28	## 4. Training Completion
29	
30	- **EXIT_CODE**: 0
31	- **Generations**: gen_0 through gen_10, all present with metrics.json
32	- **W&B**: No wandb run found
33	
34	## 5. Per-Generation Metrics
35	
36	| Gen | token_entropy | ece      | distinct_1 | distinct_2 | distinct_3 | perplexity | effective_rank | mauve   |
37	|-----|--------------|----------|------------|------------|------------|------------|----------------|---------|
38	| 0   | 3.2342       | 0.0108   | 0.0980     | 0.5141     | 0.8127     | 26.949     | 46.613         | 0.0311  |
39	| 1   | 2.4941       | 0.0667   | 0.0976     | 0.5125     | 0.8122     | 22.538     | 58.307         | 0.0314  |
40	| 2   | 2.5341       | 0.0777   | 0.0839     | 0.4433     | 0.7361     | 25.144     | 62.231         | 0.0326  |
41	| 3   | 2.5902       | 0.0767   | 0.0784     | 0.4003     | 0.6718     | 26.117     | 63.462         | 0.0322  |
42	| 4   | 2.5707       | 0.0836   | 0.0731     | 0.3636     | 0.6132     | 27.209     | 63.454         | 0.0317  |
43	| 5   | 2.5728       | 0.0887   | 0.06
…[truncated 5722 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_p02_a045_seed_count_20260520T132027",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T13:22:32.370941+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/alpha_sweep_a045_s43_fp32/analysis_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_p02_a045_seed_count_20260520T132027",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/alpha_sweep_a045_s43_fp32/analysis_report.md"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T13:22:32.371168+00:00_

1	# Analysis Report: alpha_sweep_a045_s43_fp32
2	
3	## Experiment Config
4	- **Model**: EleutherAI/pythia-410m
5	- **α**: 0.45 (synthetic ratio)
6	- **Seed**: 43
7	- **Precision**: fp32
8	- **Data**: WikiText-103 5k
9	- **Generations**: 10 (gen0–gen10, 11 total)
10	- **Steps/gen**: 5000
11	- **Server**: westd-17855
12	
13	## Hypothesis
14	> Onset boundary cross-seed at α=0.45: s42 shows PermG=0/8 (blind zone, K3=3/8). If s43 also PermG=0/8 → onset > 0.45 is seed-robust, strengthening the [0.45, 0.50] onset claim.
15	
16	## Result: **SUCCESS** — PermG=0/8 confirmed, onset > 0.45 is seed-robust
17	
18	---
19	
20	## s42 vs s43 Comparison
21	
22	### Core Causality Metrics
23	
24	| Metric | s42 | s43 | Δ |
25	|--------|-----|-----|---|
26	| PermG_fwd | 0/8 | 0/8 | = |
27	| PermG_rev | 0/8 | 0/8 | = |
28	| K≥3 | 3/8 | 2/8 | -1 |
29	| K≥4 | 0/8 | 0/8 | = |
30	| naive_xcorr (fwd) | 7/8 | 1/8 | -6 |
31	| diff_xcorr (fwd) | 3/8 | 1/8 | -2 |
32	| threshold_onset | 8/8 | 8/8 | = |
33	| ty_granger | 1/8 | 7/8 | +6 (C003: not usable as evidence at α≤0.50) |
34	
35	### Drift Metrics (gen0→gen10, % change)
36	
37	| Metric | s42 | s43 | Δ |
38	|--------|-----|-----|---|
39	| token_entropy | -18.73% | -19.61% | -0.88pp |
40	| perplexity | +12.19% | +12.37% | +0.18pp |
41	| ece | — | +800.00% | — |
42	| distinct_1 | — | -34.69% | — |
43	| distinct_2 | — | -47.24% | — |
44	| distinct_3 | — | -47.55% | — |
45	| mauve | — | -18.78% | — |
46	| effective_rank | — | +26.45% | — |
47	
48	### Absolute Values (gen0 / gen10)
49	
50	| Metric | s43 gen0 | s43 gen10 |
51	|--------|----------|-----------|
52	| token_entropy | 3.2342 | 2.5999 |
53	| ece | 0.0108 | 0.0972 |
54	| distinct_1 | 0.0983 | 0.0642 |
55	| distinct_2 | 0.5146 | 0.2715 |
56	| distinct_3 | 0.8140 | 0.4269 |
57	| perplexity | 26.95 | 30.28 |
58	| mauve | 0.0315 | 0.0256 |
59	| effective_rank | 46.61 | 58.94 |
60	
61	## Consensus Detail (s43, per-pair)
62	
63	| Pair | K | Methods |
64	|------|---|---------|
65	| token_entropy→dis
…[truncated 1825 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_p02_a045_seed_count_20260520T132027",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T13:22:32.371485+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "find /root/distrib_canary_collapse -maxdepth 3 -type d -name \"*a045*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_p02_a045_seed_count_20260520T132027",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "find /root/distrib_canary_collapse -maxdepth 3 -type d -name \"*a045*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-20T13:22:32.371697+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"find: '/root/distrib_canary_collapse': No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 1.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_p02_a045_seed_count_20260520T132027",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T13:22:32.371874+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "find /root/autodl-tmp/distrib_canary_collapse -maxdepth 3 -type d -name \"*a045*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_p02_a045_seed_count_20260520T132027",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "find /root/autodl-tmp/distrib_canary_collapse -maxdepth 3 -type d -name \"*a045*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T13:22:32.372050+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.82}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_p02_a045_seed_count_20260520T132027",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T13:22:32.372282+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "artifacts/*a045*/**/*.json",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_p02_a045_seed_count_20260520T132027",
  "tool": "Glob",
  "tool_args": {
    "pattern": "artifacts/*a045*/**/*.json",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T13:22:32.372496+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_p02_a045_seed_count_20260520T132027",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T13:22:32.372755+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "find /root -maxdepth 3 -type d -name \"*a045*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_p02_a045_seed_count_20260520T132027",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "find /root -maxdepth 3 -type d -name \"*a045*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-20T13:22:32.372974+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "artifacts/*a045*/**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_p02_a045_seed_count_20260520T132027",
  "tool": "Glob",
  "tool_args": {
    "pattern": "artifacts/*a045*/**/*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-20T13:22:32.373184+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_p02_a045_seed_count_20260520T132027",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-20T13:22:32.373414+00:00_

artifacts/alpha_sweep_a045_s42_fp32/report/analysis_alpha_sweep_a045_s42_fp32.md
artifacts/alpha_sweep_a045_s42_fp32/report/analysis_alpha_sweep_a045_s42_fp32_e27341.md
artifacts/alpha_sweep_a045_s43_fp32/analysis_report.md
artifacts/alpha_sweep_a045_s43_fp32/report/analysis_report.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_p02_a045_seed_count_20260520T132027",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-20T13:22:32.373674+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "a045",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "glob": "**/registry*.json",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_p02_a045_seed_count_20260520T132027",
  "tool": "Grep",
  "tool_args": {
    "pattern": "a045",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
    "glob": "**/registry*.json",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-20T13:22:32.373895+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_p02_a045_seed_count_20260520T132027",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T13:22:32.374100+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "a045",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "glob": "**/D120*\"",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_p02_a045_seed_count_20260520T132027",
  "tool": "Grep",
  "tool_args": {
    "pattern": "a045",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
    "glob": "**/D120*\"",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-20T13:22:32.374330+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_p02_a045_seed_count_20260520T132027",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T13:22:32.374546+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0\\\\.45|a045",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "glob": "**/*registry*\"",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_p02_a045_seed_count_20260520T132027",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0\\\\.45|a045",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
    "glob": "**/*registry*\"",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-20T13:22:32.374754+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_p02_a045_seed_count_20260520T132027",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-20T13:22:32.374955+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "a045|0\\.45",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "glob": "**/*.json",
  "output_mode": "files_with_matches",
  "head_limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_p02_a045_seed_count_20260520T132027",
  "tool": "Grep",
  "tool_args": {
    "pattern": "a045|0\\.45",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
    "glob": "**/*.json",
    "output_mode": "files_with_matches",
    "head_limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-20T13:22:32.375177+00:00_

Found 20 files limit: 20
logs/workers/worker_analysis_d028_directive28_alpha_c_20260520T122910_result.json
artifacts/d028_directive28_alpha_c_analysis.json
logs/workers/worker_ops_t20_progress_check_20260520T125247_result.json
logs/workers/worker_ops_fix_t20_a045_registry_20260520T125202_result.json
checkpoints/t20_a045_s42_fp32_RUNNING_20260520T125348.json
artifacts/_project/data/d028_directive28_alpha_c_analysis.json
artifacts/d147_alpha_c_vs_delta_alpha.json
checkpoints/alpha_sweep_a060_s42_fp32_v4_DONE_20260520T115757.json
checkpoints/alpha_sweep_a060_s42_fp32_v4_DONE_20260520T115737.json
artifacts/alpha_sweep_a060_s42_fp32_v4/5method_leadlag.json
artifacts/alpha_sweep_a060_s42_fp32_v4/data/5method_leadlag.json
checkpoints/alpha_sweep_a060_s42_fp32_v4_DONE_20260520T115247.json
checkpoints/alpha_sweep_a060_s42_fp32_v4_ANALYZING_20260520T115243.json
checkpoints/t20_a045_s42_fp32_ALLOCATED_20260520T115020.json
checkpoints/t20_a045_s42_fp32_QUEUED_20260520T115011.json
checkpoints/t20_a045_s42_fp32_PENDING_20260520T114855.json
checkpoints/alpha_sweep_a060_s42_fp32_v4_ANALYZING_20260520T114352.json
artifacts/t20_predictions_locked.json
logs/workers/worker_analysis_fdr_gradient_a045_20260520T110756_result.json
artifacts/_project/data/fdr_gradient_a045.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_p02_a045_seed_count_20260520T132027",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-20T13:22:32.375452+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "a045",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "glob": "**/*.csv",
  "output_mode": "files_with_matches",
  "head_limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_p02_a045_seed_count_20260520T132027",
  "tool": "Grep",
  "tool_args": {
    "pattern": "a045",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
    "glob": "**/*.csv",
    "output_mode": "files_with_matches",
    "head_limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-20T13:22:32.375665+00:00_

Found 3 files
artifacts/_project/data/consensus_heatmap_data_m035.csv
artifacts/_project/data/dose_response_5method_regime_m035.csv
artifacts/_project/data/dose_response_5method_regime.csv

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_p02_a045_seed_count_20260520T132027",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-20T13:22:32.375933+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "a045|0\\.45",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/data/consensus_heatmap_data_m035.csv",
  "output_mode": "content",
  "head_limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_p02_a045_seed_count_20260520T132027",
  "tool": "Grep",
  "tool_args": {
    "pattern": "a045|0\\.45",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/data/consensus_heatmap_data_m035.csv",
    "output_mode": "content",
    "head_limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-20T13:22:32.376155+00:00_

58:0.45,a045_s42_fp32,token_entropy->distinct_1,0,1,1,0,0,2
59:0.45,a045_s42_fp32,token_entropy->distinct_2,0,1,1,0,0,2
60:0.45,a045_s42_fp32,token_entropy->distinct_3,0,0,1,0,0,1
61:0.45,a045_s42_fp32,token_entropy->mauve,0,0,1,0,0,1
62:0.45,a045_s42_fp32,ece->distinct_1,0,1,1,0,0,2
63:0.45,a045_s42_fp32,ece->distinct_2,0,0,1,0,0,1
64:0.45,a045_s42_fp32,ece->distinct_3,0,0,1,0,0,1
65:0.45,a045_s42_fp32,ece->mauve,1,0,1,0,1,3

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_p02_a045_seed_count_20260520T132027",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-20T13:22:32.376384+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/data/fdr_gradient_a045.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_p02_a045_seed_count_20260520T132027",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/data/fdr_gradient_a045.json"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-20T13:22:32.376666+00:00_

1	{
2	  "generated_at": "2026-05-20T12:00:00Z",
3	  "description": "Complete fdr_p values for α=0.45 across 2 seeds × 8 pairs",
4	  "seeds": {
5	    "s42": {
6	      "pairs": [
7	        {"canary": "token_entropy", "downstream": "distinct_1", "fdr_p": 0.093581, "raw_p": 0.070186, "significant_fdr": false},
8	        {"canary": "token_entropy", "downstream": "distinct_2", "fdr_p": 0.091181, "raw_p": 0.034193, "significant_fdr": false},
9	        {"canary": "token_entropy", "downstream": "distinct_3", "fdr_p": 0.091181, "raw_p": 0.031194, "significant_fdr": false},
10	        {"canary": "token_entropy", "downstream": "mauve", "fdr_p": 0.211158, "raw_p": 0.211158, "significant_fdr": false},
11	        {"canary": "ece", "downstream": "distinct_1", "fdr_p": 0.093581, "raw_p": 0.063987, "significant_fdr": false},
12	        {"canary": "ece", "downstream": "distinct_2", "fdr_p": 0.093581, "raw_p": 0.052190, "significant_fdr": false},
13	        {"canary": "ece", "downstream": "distinct_3", "fdr_p": 0.091181, "raw_p": 0.030594, "significant_fdr": false},
14	        {"canary": "ece", "downstream": "mauve", "fdr_p": 0.211158, "raw_p": 0.198960, "significant_fdr": false}
15	      ],
16	      "min_fdr_p": 0.091181,
17	      "sig_count": 0
18	    },
19	    "s43": {
20	      "pairs": [
21	        {"canary": "token_entropy", "downstream": "distinct_1", "fdr_p": 0.058921, "raw_p": 0.030794, "significant_fdr": false},
22	        {"canary": "token_entropy", "downstream": "distinct_2", "fdr_p": 0.058921, "raw_p": 0.039792, "significant_fdr": false},
23	        {"canary": "token_entropy", "downstream": "distinct_3", "fdr_p": 0.058921, "raw_p": 0.044191, "significant_fdr": false},
24	        {"canary": "token_entropy", "downstream": "mauve", "fdr_p": 0.098952, "raw_p": 0.086583, "significant_fdr": false},
25	        {"canary": "ece", "downstream": "distinct_1", "fdr_p": 0.058921, "raw_p": 0.023395, "significant_fdr": false},
26	        {"canary": "ece", "downstream": "distinct_2", "fdr_
…[truncated 510 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_p02_a045_seed_count_20260520T132027",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-20T13:22:32.376928+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/data/dose_response_5method_regime.csv",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_p02_a045_seed_count_20260520T132027",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/data/dose_response_5method_regime.csv",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-20T13:22:32.377172+00:00_

1	alpha,n_seeds,permG_fwd_rate,permG_rev_rate,naive_rate,diff_rate,threshold_3sigma_rate,TY_rate,K_ge3_rate,K_ge4_rate,regime
2	0.00,1,0.000,0.000,1.000,0.500,0.500,0.250,0.375,0.000,null
3	0.05,1,0.000,0.000,0.875,0.375,0.625,0.375,0.375,0.000,null
4	0.10,1,0.000,0.000,0.875,0.750,0.625,0.375,0.500,0.250,null
5	0.25,1,0.000,0.000,1.000,0.375,0.625,0.375,0.500,0.000,null
6	0.30,1,,,,,,,,,"RUNNING (a030_s42)"
7	0.35,1,0.000,0.000,1.000,0.500,1.000,0.500,0.750,0.250,null
8	0.40,1,0.000,0.000,1.000,0.375,1.000,0.500,0.750,0.125,null
9	0.45,1,,,,,,,,,"RUNNING (a045_s42)"
10	0.50,1,0.750,0.000,1.000,0.875,1.000,0.500,0.875,0.750,onset
11	0.60,1,0.375,0.000,0.875,1.000,1.000,1.000,1.000,0.875,sync_collapse
12	0.75,1,0.750,0.000,0.875,0.750,1.000,1.000,0.875,0.750,detection
13	1.00,1,0.750,0.000,1.000,0.750,1.000,0.375,0.750,0.750,detection
14	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_p02_a045_seed_count_20260520T132027",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-20T13:22:32.377471+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0\\.45|a045",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/data/dose_response_5method_regime_m035.csv",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_p02_a045_seed_count_20260520T132027",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0\\.45|a045",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/data/dose_response_5method_regime_m035.csv",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-20T13:22:32.377679+00:00_

9:0.45,42,a045_s42_fp32,,0,0,1,3,8,1,1,0,0.0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_p02_a045_seed_count_20260520T132027",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-20T13:22:32.377876+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0\\.45|a045",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "glob": "**/paper/**\"",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_p02_a045_seed_count_20260520T132027",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0\\.45|a045",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
    "glob": "**/paper/**\"",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-20T13:22:32.378086+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_p02_a045_seed_count_20260520T132027",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-20T13:22:32.378306+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "single.seed|single seed|probing point",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "glob": "**/*.tex",
  "output_mode": "content",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_p02_a045_seed_count_20260520T132027",
  "tool": "Grep",
  "tool_args": {
    "pattern": "single.seed|single seed|probing point",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
    "glob": "**/*.tex",
    "output_mode": "content",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-20T13:22:32.378580+00:00_

artifacts/generalization_draft.tex:26:architecture family, and training domain ($\alpha{=}1.0$, single seed
artifacts/generalization_draft.tex:31:reproduces the single-seed Pythia-410M result for comparison; 4-seed
artifacts/generalization_draft.tex:85:conditions at $\alpha{=}1.0$ (single seed). The baseline Pythia-410M
artifacts/_project/paper/experiments.tex:30:\caption{Metric drift (\%, generation~0$\to$10) across contamination levels. $\alpha{=}1.0$: 4-seed mean${\pm}$std; other levels: single seed (seed=42). Non-monotonic distinct-1 pattern across $\alpha \in \{0.25, 0.50\}$ is observed at seed=42, pending multi-seed confirmation.}
artifacts/_project/paper/experiments.tex:87:[Omitted long matching line]
artifacts/_project/paper/experiments.tex:117:At $\alpha{=}0.75$ (single seed, seed=42), 3/8 pairs reach FDR significance; this result requires multi-seed replication before serving as primary evidence.
artifacts/_project/paper/experiments.tex:120:This boundary is sharp rather than gradual: method-level consensus ($K{\geq}4/5$) identifies 0--1 of 16 candidate pairs as robust at $\alpha{\leq}0.50$ but 11/16 at $\alpha{=}0.75$ (single seed, pre-pipeline filtering; the stricter $K{\geq}4/5$, $S{\geq}3/4$ criterion at $\alpha{=}1.0$ retains 6/16 after excluding failed candidates and spurious channels per \S\ref{sec:case_study}).
artifacts/_project/paper/experiments.tex:121:The lower count at $\alpha{=}1.0$ despite stronger contamination reflects the stricter validation standard: multi-seed replication ($S{\geq}3/4$) filters seed-specific artifacts, and pipeline filtering removes the perplexity channel (spurious per \S\ref{sec:method_sensitivity}) and failed canary candidates (effective rank, Self-BLEU), both of which contribute to the $\alpha{=}0.75$ single-seed count.
artifacts/_project/paper/experiments.tex:144:\paragraph{High contamination ($\alpha{=}0.75$, single seed).}
artifacts/_project/paper/experiments.tex:148:These single-seed results require multi-seed con
…[truncated 4417 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_p02_a045_seed_count_20260520T132027",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-20T13:22:32.378908+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0\\.45|a045",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "output_mode": "content",
  "-C": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_p02_a045_seed_count_20260520T132027",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0\\.45|a045",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
    "output_mode": "content",
    "-C": "5"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-20T13:22:32.379167+00:00_

132-0.10 & 0 & 24 & Clean \\
133-\bottomrule
134-\end{tabular}}
135-\end{table}
136-
137:\paragraph{PermG $p$-value gradient at the onset boundary ($\alpha{=}0.45$).}
138-At the onset boundary, PermG operates near its detection limit, and marginal $p$-values exhibit seed-dependent variation consistent with the statistical power interpretation (\S\ref{sec:theory}).
139:Table~\ref{tab:fdr_gradient_a045} reports BH-corrected $p$-values for all 8 canary$\to$downstream pairs across two seeds at $\alpha{=}0.45$.
140-Seed~43 reaches a minimum FDR-corrected $p{=}0.059$ (18\% above the $q{=}0.05$ threshold), while seed~42 reaches $p{=}0.091$ (82\% above threshold).
141-No pair crosses the significance threshold at either seed, yielding the aggregate 0/8 detection rate reported in \S\ref{sec:regime}.
142:The gradient is consistent with a continuous power transition rather than a binary absence of signal: PermG operates near its detection limit at $\alpha{=}0.45$, with seed-dependent variation in marginal $p$-values.
143-
144-\begin{table}[h]
145-\centering
146-\small
147:\caption{BH-corrected PermG $p$-values at $\alpha{=}0.45$ (8 canary$\to$downstream pairs $\times$ 2 seeds). Min $p_{\mathrm{fdr}}$ per seed shown. All pairs remain above the $q{=}0.05$ threshold, yielding 0/8 aggregate detection.}
148:\label{tab:fdr_gradient_a045}
149-\begin{tabular}{lcc}
150-\toprule
151- & Seed 42 & Seed 43 \\
152-\midrule
153-Min FDR $p$ & 0.091 & 0.059 \\
--
174-\toprule
175-Canary & Downstream & TE\textsubscript{fwd} (mean) & $p$\textsubscript{fwd} (mean) & TE\textsubscript{rev} (mean) & $p$\textsubscript{rev} (mean) \\
176-\midrule
177-token\_entropy & distinct-1 & 0.289 & 0.559 & 0.480 & 0.490 \\
178-token\_entropy & distinct-2 & 0.300 & 0.529 & 0.496 & 0.447 \\
179:token\_entropy & distinct-3 & 0.255 & 0.645 & 0.484 & 0.459 \\
180-token\_entropy & perplexity & 0.257 & 0.676 & 0.386 & 0.626 \\
181-ECE & distinct-1 & 0.185 & 0.720 & 0.184 & 0.891 \\
182-ECE & distinct-2 & 0.208 & 0.683 
…[truncated 130 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_p02_a045_seed_count_20260520T132027",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-20T13:22:32.379485+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex",
  "offset": "10",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_p02_a045_seed_count_20260520T132027",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex",
    "offset": "10",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-20T13:22:32.379728+00:00_

10	Training data is drawn from WikiText-103 \cite{merity2017pointer}, using 5{,}000-sample subsets per generation.
11	
12	Our protocol follows the replace paradigm of \citet{shumailov2024curse}, adapted for mixed synthetic-real training at $\alpha{<}1.0$.
13	Each generation $t$ proceeds in three steps: (1)~fine-tune the generation-$(t{-}1)$ model for 5{,}000 steps on a mixture of $\alpha$ fraction synthetic data and $(1{-}\alpha)$ fraction real data (AdamW optimizer, learning rate $5 \times 10^{-5}$, 500 warmup steps, weight decay $0.01$, batch size 4 for Pythia-410M, 32 for GPT-2-medium); (2)~generate 5{,}000 synthetic samples from the fine-tuned model (temperature $1.0$, top-$k{=}50$, max length 512 tokens); (3)~fully replace the synthetic pool.
14	We run $T{=}10$ generations (11 time points including the generation-0 baseline) across six primary contamination levels $\alpha \in \{0.00, 0.10, 0.25, 0.50, 0.75, 1.00\}$ with multi-seed replication, plus seven single-seed probing points ($\alpha \in \{0.05, 0.30, 0.35, 0.40, 0.45, 0.55, 0.60\}$) to resolve the onset boundary, yielding a 13-point $\alpha$ grid.
15	The $\alpha{=}1.0$ condition uses four random seeds $\{42, 43, 44, 45\}$; $\alpha \in \{0.00, 0.25, 0.50, 0.75\}$ each use three seeds $\{42, 43, 44\}$; remaining levels use a single seed (42).
16	
17	We track two \emph{canary metrics} (cheap-to-compute statistics hypothesized to precede downstream degradation, inspired by early-warning signals in dynamical systems \cite{scheffer2009early}) and three \emph{downstream metrics}.
18	Canary metrics are token entropy (next-token prediction entropy averaged over held-out samples) and expected calibration error (ECE).
19	Downstream metrics are distinct-1 and distinct-2 ($n$-gram diversity \cite{li2016diversity}, computed over all 5{,}000 generated samples per generation) and perplexity (evaluated on held-out real data).
20	Token entropy is the mean next-token prediction entropy $H(p_\theta | \text{context})$ averag
…[truncated 2029 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_p02_a045_seed_count_20260520T132027",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-20T13:22:32.379971+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex",
  "offset": "125",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_p02_a045_seed_count_20260520T132027",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex",
    "offset": "125",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-20T13:22:32.380186+00:00_

125	Pythia-1.4B    & 1.4B & Wiki & 2--6/8$^\dagger$ \\
126	Pythia-6.9B    & 6.9B & Wiki & 7/8$^*$ \\
127	GPT-2-medium   & 345M & Wiki & 6/8 \\
128	OPT-1.3B       & 1.3B & Wiki & 6/8 \\
129	Qwen3.5-0.8B   & 0.8B & Wiki & 8/8 \\
130	SmolLM3-3B     & 3.0B & Wiki & 3/8$^\ddagger$ \\
131	Padding-410M   & 410M & Wiki & 6/8 \\
132	\addlinespace
133	Pythia-1B      & 1.0B & C4   & 8/8 \\
134	Pythia-1.4B    & 1.4B & C4   & 8/8 \\
135	\bottomrule
136	\multicolumn{4}{l}{\footnotesize $^\dagger$Seed-dependent (s42: 2/8, s43: 6/8).} \\
137	\multicolumn{4}{l}{\footnotesize $^*$bf16 (exceeds single-GPU fp32 capacity).} \\
138	\multicolumn{4}{l}{\footnotesize $^\ddagger$ECE-only canary (entropy 0/4).} \\
139	\multicolumn{4}{l}{\footnotesize Multi-seed (range shown): Pythia-410M, -1.4B Wiki,} \\
140	\multicolumn{4}{l}{\footnotesize GPT-2-med, OPT-1.3B, Pythia-1B C4 (2 seeds each).} \\
141	\multicolumn{4}{l}{\footnotesize Others: single seed. Total: 15 combinations.} \\
142	\end{tabular}
143	\end{table}
144	
145	
146	\subsection{Canary-Based Early Intervention}
147	\label{sec:intervention}
148	
149	We implement a predictive cessation protocol: training with synthetic data ($\alpha{=}1.0$) continues until token entropy drops ${>}15\%$ relative to generation~0, at which point $\alpha$ switches to $0.0$ (pure real data).
150	A reactive baseline triggers when distinct-1 drops ${>}10\%$.
151	The predictive trigger fires at generation~1 in both Pythia-410M and Pythia-1.4B (s42 fp32), one generation before the reactive baseline (generation~2).
152	Peak perplexity under predictive intervention is $56.99$ versus $157.09$ under reactive (s42 fp32), a 58\% reduction (bootstrap 95\% CI: 29--64\%).
153	Recovery occurs at generation~2 under predictive cessation versus generation~4 under reactive.
154	Both models converge to the $\alpha{=}0.0$ baseline by generation~10.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_p02_a045_seed_count_20260520T132027",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-20T13:22:32.380476+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "offset": "1",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_p02_a045_seed_count_20260520T132027",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
    "offset": "1",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-20T13:22:32.380710+00:00_

1	\appendix
2	
3	\section{Metric Drift Summary}
4	\label{app:drift}
5	
6	\begin{table}[h]
7	\centering
8	\small
9	\caption{Metric drift (\%, generation~0$\to$10) for Pythia-410M across contamination levels. Diversity collapse occurs at all $\alpha$ levels, with the strongest decline at low-to-moderate contamination ($\alpha{=}0.25$: distinct-1 $-40.3{\pm}0.3\%$) rather than full replacement ($\alpha{=}1.0$: $-27.8{\pm}1.6\%$). $^\dagger$$\alpha{=}0.10$: single seed (seed~42, preliminary). $\alpha{=}0.00$, $\alpha{=}0.25$, $\alpha{=}0.50$, $\alpha{=}0.75$: 3-seed mean${\pm}$std (seeds 42, 43, 44); $\alpha{=}1.0$: 4-seed mean${\pm}$std (seeds 42, 43, 44, 45).}
10	\label{tab:drift_summary}
11	\resizebox{\columnwidth}{!}{%
12	\begin{tabular}{lccccc}
13	\toprule
14	$\alpha$ & Entropy & ECE & Distinct-1 & Distinct-2 & Perplexity \\
15	\midrule
16	0.00 & $-4.6{\pm}0.4$ & $+37.6{\pm}14$ & $-14.1{\pm}0.4$ & $-9.6{\pm}0.4$ & $-20.6{\pm}1.0$ \\
17	0.10$^\dagger$ & $-5.3$ & $+57$ & $-39.6$ & $-56.4$ & $-21.0$ \\
18	0.25 & $-4.7{\pm}0.5$ & $+81.8{\pm}15.9$ & $-40.3{\pm}0.3$ & $-56.4{\pm}0.7$ & $-18.1{\pm}0.8$ \\
19	0.50 & $-18.0{\pm}0.5$ & $+822.6{\pm}18.3$ & $-37.1{\pm}0.4$ & $-50.4{\pm}1.0$ & $+21.0{\pm}0.1$ \\
20	0.75 & $-27.6{\pm}0.2$ & $+1791{\pm}18$ & $-32.3{\pm}0.5$ & $-41.0{\pm}1.0$ & $+182.6{\pm}0.7$ \\
21	1.00 & $-60.8{\pm}1.2$ & $+3780{\pm}30$ & $-27.8{\pm}1.6$ & $-34.0{\pm}3.3$ & $+3674{\pm}45$ \\
22	\bottomrule
23	\end{tabular}}
24	\end{table}
25	
26	
27	\section{Distinct-3 Results}
28	\label{app:distinct3}
29	
30	Table~\ref{tab:distinct3_drift} reports distinct-3 drift across all contamination levels.
31	Distinct-3 exhibits the largest absolute decline among diversity metrics at low contamination ($-58.9{\pm}0.9\%$ at $\alpha{=}0.25$) but attenuates at higher levels ($-30.5\%$ at $\alpha{=}1.0$), consistent with the diversity--calibration dissociation discussed in \S\ref{sec:discussion}.
32	
33	\begin{table}[h]
34	\centering
35	\small
36	\caption{Distinct-3 drift (
…[truncated 501 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_p02_a045_seed_count_20260520T132027",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-20T13:22:32.380949+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "offset": "230",
  "limit": "40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_p02_a045_seed_count_20260520T132027",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
    "offset": "230",
    "limit": "40"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-20T13:22:32.381162+00:00_

230	token\_entropy & 1.0 & 3.21 & 1/3 & canary \\
231	ECE & 1.0 & 3.10 & 1/3 & canary \\
232	distinct-1 & 2.3 & 2.18 & 3/3 & downstream \\
233	distinct-2 & 3.0 & 1.97 & 3/3 & downstream \\
234	distinct-3 & 3.7 & 1.86 & 3/3 & downstream \\
235	perplexity & 4.0 & 1.70 & 3/3 & downstream \\
236	\bottomrule
237	\end{tabular}}
238	\end{table}
239	
240	\paragraph{Dose-response ordering pattern.}
241	Table~\ref{tab:cp_ordering} summarizes the ordering pattern across contamination levels.
242	The canary-to-downstream gap shifts monotonically from negative (downstream first) under the null to positive (canary first) under treatment, ruling out a methodological artifact in which canary metrics would systematically appear earlier regardless of condition.
243	The $\alpha{=}1.0$ analysis is limited to a single seed (s42); all other conditions use 3 seeds.
244	
245	\begin{table}[h]
246	\centering
247	\small
248	\resizebox{\columnwidth}{!}{%
249	\begin{tabular}{lcccl}
250	\toprule
251	$\alpha$ & Canary cp & Downstream cp & Gap & Direction \\
252	\midrule
253	0.00 & gen 4--8 & gen 2 & $-$2.5 & Downstream first \\
254	0.25 & gen 3--4 & gen 3--4 & $\approx$0 & Simultaneous \\
255	0.75 & gen 1 & gen 2--4 & $+$2.25 & Canary first \\
256	1.00 & gen 2 & gen 2--5 & $+$1.0 & Canary first \\
257	\bottomrule
258	\end{tabular}}
259	\caption{Change-point ordering reversal across contamination levels. Under the null ($\alpha{=}0.00$), downstream metrics break before canary metrics; this ordering reverses monotonically as $\alpha$ increases, consistent with the Granger-causal precedence analysis.}
260	\label{tab:cp_ordering}
261	\end{table}
262	
263	
264	\section{Sequential Monitoring: CUSUM vs Calibrated Threshold}
265	\label{app:csmp}
266	
267	We translate the Granger-precedence finding into a deployable monitoring protocol using CUSUM (cumulative sum) sequential testing, calibrated against the $\alpha{=}0.0$ null control.
268	The null-calibration procedure sets the alarm threshold $h$ such th
…[truncated 121 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_p02_a045_seed_count_20260520T132027",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-20T13:22:32.381496+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/d150_p02_a045_seed_audit.md",
  "content": "# D150-P02: α=0.45 Seed Audit\n\n## 找到的 Seed 列表\n\n| Seed | 本地 Artifact 目录 | 分析报告 | 服务器数据 |\n|------|-------------------|---------|-----------|\n| s42 | `artifacts/alpha_sweep_a045_s42_fp32/` | ✅ 完整 | 两台服务器均已清理 |\n| s43 | `artifacts/alpha_sweep_a045_s43_fp32/` | ✅ 完整 | 两台服务器均已清理 |\n| s44 | — | ❌ 不存在 | — |\n\n**实际 seed 数 = 2**（s42, s43）\n\n## 每个 Seed 的 PermG 结果\n\n### s42 (fp32, WikiText-103, Pythia-410M)\n- **PermG fwd (FDR) = 0/8**\n- Min FDR-p = 0.091（距阈值 0.05 有 82%）\n- K≥3 = 3/8, K≥4 = 0/8\n\n### s43 (fp32, WikiText-103, Pythia-410M)\n- **PermG fwd (FDR) = 0/8**\n- Min FDR-p = 0.059（距阈值 0.05 仅 18%）\n- K≥3 = 2/8, K≥4 = 0/8\n\n**两个 seed 一致: PermG = 0/8，blind zone 判定稳健。**\n\n## D120 Canonical 分析状态\n\n无独立 D120 JSON（D120 pipeline 可能在 a045 完成前建立）。但有：\n- `fdr_gradient_a045.json` — 完整的 2 seed × 8 pair FDR p-values\n- 两份独立分析报告（s42: `analysis_alpha_sweep_a045_s42_fp32.md`, s43: `analysis_report.md`）\n- `consensus_heatmap_data_m035.csv` — 仅收录 s42（s43 未入 heatmap）\n- `dose_response_5method_regime_m035.csv` — α=0.45 行仅 1 seed\n\n## 论文不一致\n\n| 位置 | 当前表述 | 实际情况 |\n|------|---------|---------|\n| `docs/paper/experiments.tex` L14 | \"seven single-seed probing points (α ∈ {0.05, 0.30, 0.35, 0.40, **0.45**, 0.55, 0.60})\" | α=0.45 有 2 seeds |\n| `docs/paper/experiments.tex` L15 | \"remaining levels use a single seed (42)\" | α=0.45 实际有 s42+s43 |\n| `docs/paper/appendix.tex` L139 | \"Table reports BH-corrected p-values ... across **two seeds** at α=0.45\" | ✅ 正确 |\n| `docs/paper/appendix.tex` Tab `fdr_gradient_a045` | 报了 Seed 42 和 Seed 43 | ✅ 正确 |\n\n**矛盾**：主体文 Section 4.1 称 α=0.45 为 \"single-seed probing point\"，但 Appendix Table 明确报了 2 seeds。\n\n## 建议修正\n\n`docs/paper/experiments.tex` L14-15 应改为：\n\n> **方案 A**（推荐）：将 α=0.45 从 \"single-seed probing points\" 列表移出，改为 \"six single-seed probing points (α ∈ {0.05, 0.30, 0.35, 0.40, 0.55, 0.60})\"，并补充 \"α=0.45 uses two seeds {42, 43} to confirm the onset boundary\"。\n\n> **方案 B**：L15 改为 \"remaining levels use a single seed (42), except α=0.45 which uses two seeds {42, 43}\"。\n\n两种方案均需同步更新 seed count 总数（当前 \"Total: 15 combinations\" 可能也需核实）。\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d150_p02_a045_seed_count_20260520T132027",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/d150_p02_a045_seed_audit.md",
    "content": "# D150-P02: α=0.45 Seed Audit\n\n## 找到的 Seed 列表\n\n| Seed | 本地 Artifact 目录 | 分析报告 | 服务器数据 |\n|------|-------------------|---------|-----------|\n| s42 | `artifacts/alpha_sweep_a045_s42_fp32/` | ✅ 完整 | 两台服务器均已清理 |\n| s43 | `artifacts/alpha_sweep_a045_s43_fp32/` | ✅ 完整 | 两台服务器均已清理 |\n| s44 | — | ❌ 不存在 | — |\n\n**实际 seed 数 = 2**（s42, s43）\n\n## 每个 Seed 的 PermG 结果\n\n### s42 (fp32, WikiText-103, Pythia-410M)\n- **PermG fwd (FDR) = 0/8**\n- Min FDR-p = 0.091（距阈值 0.05 有 82%）\n- K≥3 = 3/8, K≥4 = 0/8\n\n### s43 (fp32, WikiText-103, Pythia-410M)\n- **PermG fwd (FDR) = 0/8**\n- Min FDR-p = 0.059（距阈值 0.05 仅 18%）\n- K≥3 = 2/8, K≥4 = 0/8\n\n**两个 seed 一致: PermG = 0/8，blind zone 判定稳健。**\n\n## D120 Canonical 分析状态\n\n无独立 D120 JSON（D120 pipeline 可能在 a045 完成前建立）。但有：\n- `fdr_gradient_a045.json` — 完整的 2 seed × 8 pair FDR p-values\n- 两份独立分析报告（s42: `analysis_alpha_sweep_a045_s42_fp32.md`, s43: `analysis_report.md`）\n- `consensus_heatmap_data_m035.csv` — 仅收录 s42（s43 未入 heatmap）\n- `dose_response_5method_regime_m035.csv` — α=0.45 行仅 1 seed\n\n## 论文不一致\n\n| 位置 | 当前表述 | 实际情况 |\n|------|---------|---------|\n| `docs/paper/experiments.tex` L14 | \"seven single-seed probing points (α ∈ {0.05, 0.30, 0.35, 0.40, **0.45**, 0.55, 0.60})\" | α=0.45 有 2 seeds |\n| `docs/paper/experiments.tex` L15 | \"remaining levels use a single seed (42)\" | α=0.45 实际有 s42+s43 |\n| `docs/paper/appendix.tex` L139 | \"Table reports BH-corrected p-values ... across **two seeds** at α=0.45\" | ✅ 正确 |\n| `docs/paper/appendix.tex` Tab `fdr_gradient_a045` | 报了 Seed 42 和 Seed 43 | ✅ 正确 |\n\n**矛盾**：主体文 Section 4.1 称 α=0.45 为 \"single-seed probing point\"，但 Appendix Table 明确报了 2 seeds。\n\n## 建议修正\n\n`docs/paper/experiments.tex` L14-15 应改为：\n\n> **方案 A**（推荐）：将 α=0.45 从 \"single-seed probing points\" 列表移出，改为 \"six single-seed probing points (α ∈ {0.05, 0.30, 0.35, 0.40, 0.55, 0.60})\"，并补充 \"α=0.45 uses two seeds {42, 43} to confirm the onset boundary\"。\n\n> **方案 B**：L15 改为 \"remaining levels use a single seed (42), except α=0.45 which uses two seeds {42, 43}\"。\n\n两种方案均需同步更新 seed count 总数（当前 \"Total: 15 combinations\" 可能也需核实）。\n"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-20T13:22:32.381799+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/d150_p02_a045_seed_audit.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d150_p02_a045_seed_count_20260520T132027",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 57 · 2026-05-20T13:22:32.382080+00:00_

审计完成。报告已写入 `artifacts/d150_p02_a045_seed_audit.md`。

**核心发现**：

- **实际 seed 数 = 2**（s42 + s43），无 s44
- **PermG 结果**：s42 = 0/8 (min FDR-p 0.091)，s43 = 0/8 (min FDR-p 0.059)，两 seed 一致
- **不一致确认**：`experiments.tex` L14-15 把 α=0.45 归入 "single-seed probing points"，但 appendix Table `fdr_gradient_a045` 明确报了 2 seeds 的数据

建议将 α=0.45 从 "seven single-seed probing points" 列表中移出，在 L15 补充说明其使用了 2 seeds {42, 43}。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_d150_p02_a045_seed_count_20260520T132027"
}
```

</details>

---
