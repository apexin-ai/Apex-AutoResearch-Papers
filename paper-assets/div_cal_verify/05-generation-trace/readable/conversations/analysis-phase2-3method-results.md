# analysis phase2 3method results

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 0
- **Tool calls:** 12
- **Original source:** `logs/chats/worker_analysis_phase2_3method_results_20260513T092435.jsonl`
- **Structured JSON:** [`cc28fcc048d0db44659f.json`](../../sessions/cc/cc28fcc048d0db44659f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

25 recorded events

### Tool call

_source line 1 · 2026-05-13T09:26:41.979755+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase2_3method_results_20260513T092435",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-13T09:26:41.980105+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase2_3method_results_20260513T092435",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-13T09:26:41.980303+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11235",
  "command": "tail -100 /root/runs/phase-gated-compound-sparse/phase2_3method_selfit.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase2_3method_results_20260513T092435",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11235",
    "command": "tail -100 /root/runs/phase-gated-compound-sparse/phase2_3method_selfit.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-13T09:26:41.980477+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11235",
  "command": "find /root/autodl-tmp/phase-gated-compound-sparse/ -name \"*.json\" -o -name \"*.csv\" 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase2_3method_results_20260513T092435",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11235",
    "command": "find /root/autodl-tmp/phase-gated-compound-sparse/ -name \"*.json\" -o -name \"*.csv\" 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-13T09:26:41.980656+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\n[4/5] Evaluating...\\n\\n[5/5] Gen 5 summary:\\n  Perplexity:     47.37\\n  RankMe:         290.25\\n  k-NN accuracy:  0.9880\\n  Rare n-gram:    0.010016343546075772\\n  Rank corr:      -0.0133\\n  Time:           1058s\\n\\n============================================================\\nGeneration 6/7 | Method: external_only\\n============================================================\\n\\n[1/5] Generating synthetic data...\\n  Generated 977 sequences\\n\\n[2/5] Selecting data (method=external_only)...\\nQuality filtering...\\n  Quality filter DISABLED: would have removed 0/977 (ppl threshold: 74.0)\\nComputing embeddings (method=contriever)...\\nComputing Contriever reference embeddings for PCA fit...\\nPCA projection to d=32...\\nGreedy submodular selection (budget=488)...\\n  Selected 100/488\\n  Selected 200/488\\n  Selected 300/488\\n  Selected 400/488\\n  Selected 488/977 sequences\\n  Selection diag: sel=0.0878 rej=0.0782 ratio=1.1227\\n  QF diag: would_remove=0, removed_rare=nan, kept_rare=nan\\n\\n[3/5] Training student (lr=5e-05, epochs=3)...\\n  Final avg loss: 0.2148\\n  Cleaned up gen_5 checkpoint\\n\\n[4/5] Evaluating...\\n\\n[5/5] Gen 6 summary:\\n  Perplexity:     46.11\\n  RankMe:         289.66\\n  k-NN accuracy:  0.9880\\n  Rare n-gram:    0.010268010469344007\\n  Rank corr:      -0.0054\\n  Time:           1869s\\n\\n============================================================\\nGeneration 7/7 | Method: external_only\\n============================================================\\n\\n[1/5] Generating synthetic data...\\n  Generated 977 sequences\\n\\n[2/5] Selecting data (method=external_only)...\\nQuality filtering...\\n  Quality filter DISABLED: would have removed 0/977 (ppl threshold: 71.5)\\nComputing embeddings (method=contriever)...\\nComputing Contriever reference embeddings for PCA fit...\\nPCA projection to d=32...\\nGreedy submodular selection (budget=488)...\\n  Selected 100
…[truncated 1421 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase2_3method_results_20260513T092435",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-13T09:26:41.980809+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase2_3method_results_20260513T092435",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-13T09:26:41.980949+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11235",
  "command": "find /root/phase-gated-compound-sparse/ -name \"*.json\" -o -name \"*.csv\" 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase2_3method_results_20260513T092435",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11235",
    "command": "find /root/phase-gated-compound-sparse/ -name \"*.json\" -o -name \"*.csv\" 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-13T09:26:41.981081+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase2_3method_results_20260513T092435",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-13T09:26:41.981203+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11235",
  "command": "ls -la /root/phase-gated-compound-sparse/analyze_phase2.py 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase2_3method_results_20260513T092435",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11235",
    "command": "ls -la /root/phase-gated-compound-sparse/analyze_phase2.py 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-13T09:26:41.981384+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase2_3method_results_20260513T092435",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-13T09:26:41.981548+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11235",
  "command": "grep -A 20 \"FINAL SUMMARY\" /root/runs/phase-gated-compound-sparse/phase2_3method_selfit.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase2_3method_results_20260513T092435",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11235",
    "command": "grep -A 20 \"FINAL SUMMARY\" /root/runs/phase-gated-compound-sparse/phase2_3method_selfit.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-13T09:26:41.981743+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"FINAL SUMMARY -- uncurated\\n============================================================\\n Gen      PPL   RankMe      kNN     Rare     Corr\\n   0    37.10   280.32   0.9880   0.0290  -0.0226\\n   1    44.89   297.80   0.9880   0.0192  -0.0548\\n   2    51.32   302.47   0.9880   0.0139  -0.0510\\n   3    56.25   303.05   0.9870   0.0118  -0.0458\\n   4    55.88   300.51   0.9880   0.0102  -0.0350\\n   5    50.08   296.54   0.9880   0.0099  -0.0452\\n   6    48.25   290.42   0.9880   0.0094  -0.0682\\n   7    50.28   291.43   0.9880   0.0090  -0.0880\\nDone uncurated: Wed May 13 12:41:10 CST 2026\\n\\n===== [2/3] RGDS =====\\nStart rgds: Wed May 13 12:41:10 CST 2026\\n`torch_dtype` is deprecated! Use `dtype` instead!\\n`loss_type=None` was set in the config but it is unrecognized. Using the default loss: `ForCausalLMLoss`.\\nLoading Contriever...\\nLoading student model: gpt2\\nComputing gen-0 RankMe baseline...\\n  Gen-0 RankMe: 231.08\\n--\\nFINAL SUMMARY -- rgds\\n============================================================\\n Gen      PPL   RankMe      kNN     Rare     Corr\\n   0    37.09   275.89   0.9880   0.0290  -0.0123\\n   1    45.36   291.76   0.9880   0.0202  -0.0459\\n   2    50.51   292.74   0.9880   0.0151  -0.0365\\n   3    53.82   294.03   0.9880   0.0124  -0.0308\\n   4    53.97   294.92   0.9880   0.0099  -0.0483\\n   5    61.75   293.84   0.9880   0.0082  -0.0388\\n   6    64.12   293.76   0.9880   0.0067  -0.0464\\n   7    75.07   292.72   0.9880   0.0051  -0.0387\\nDone rgds: Wed May 13 13:49:56 CST 2026\\n\\n===== [3/3] EXTERNAL_ONLY =====\\nStart external_only: Wed May 13 13:49:56 CST 2026\\n`torch_dtype` is deprecated! Use `dtype` instead!\\n`loss_type=None` was set in the config but it is unrecognized. Using the default loss: `ForCausalLMLoss`.\\nLoading Contriever...\\nLoading student model: gpt2\\nComputing gen-0 RankMe baseline...\\n  Gen-0 RankMe: 231.08\\n--\\nFINAL SUMMARY -- e
…[truncated 785 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase2_3method_results_20260513T092435",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-13T09:26:41.981927+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11235",
  "command": "grep \"Selection diag\" /root/runs/phase-gated-compound-sparse/phase2_3method_selfit.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase2_3method_results_20260513T092435",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11235",
    "command": "grep \"Selection diag\" /root/runs/phase-gated-compound-sparse/phase2_3method_selfit.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-13T09:26:41.982073+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  Selection diag: sel=0.0686 rej=0.0661 ratio=1.0371\\n  Selection diag: sel=0.0797 rej=0.0876 ratio=0.9096\\n  Selection diag: sel=0.0842 rej=0.0909 ratio=0.9267\\n  Selection diag: sel=0.0854 rej=0.0907 ratio=0.9409\\n  Selection diag: sel=0.0788 rej=0.0880 ratio=0.8955\\n  Selection diag: sel=0.0765 rej=0.0944 ratio=0.8108\\n  Selection diag: sel=0.0688 rej=0.0961 ratio=0.7165\\n  Selection diag: sel=0.0491 rej=0.0949 ratio=0.5173\\n  Selection diag: sel=0.0717 rej=0.0631 ratio=1.1366\\n  Selection diag: sel=0.0858 rej=0.0709 ratio=1.2108\\n  Selection diag: sel=0.0868 rej=0.0778 ratio=1.1164\\n  Selection diag: sel=0.0945 rej=0.0790 ratio=1.1963\\n  Selection diag: sel=0.0898 rej=0.0700 ratio=1.2817\\n  Selection diag: sel=0.0809 rej=0.0729 ratio=1.1093\\n  Selection diag: sel=0.0878 rej=0.0782 ratio=1.1227\\n  Selection diag: sel=0.0878 rej=0.0801 ratio=1.0953\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.48}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase2_3method_results_20260513T092435",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-13T09:26:41.982217+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11235",
  "command": "find /root/autodl-tmp/phase-gated-compound-sparse/ -name \"*.json\" -o -name \"*.csv\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase2_3method_results_20260513T092435",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11235",
    "command": "find /root/autodl-tmp/phase-gated-compound-sparse/ -name \"*.json\" -o -name \"*.csv\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-13T09:26:41.982526+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/phase-gated-compound-sparse/results/rgds/gen_0/metrics.json\\n/root/autodl-tmp/phase-gated-compound-sparse/results/rgds/gen_1/metrics.json\\n/root/autodl-tmp/phase-gated-compound-sparse/results/rgds/gen_2/metrics.json\\n/root/autodl-tmp/phase-gated-compound-sparse/results/rgds/gen_3/checkpoint/config.json\\n/root/autodl-tmp/phase-gated-compound-sparse/results/rgds/gen_3/checkpoint/generation_config.json\\n/root/autodl-tmp/phase-gated-compound-sparse/results/rgds/gen_3/checkpoint/tokenizer_config.json\\n/root/autodl-tmp/phase-gated-compound-sparse/results/rgds/gen_3/checkpoint/special_tokens_map.json\\n/root/autodl-tmp/phase-gated-compound-sparse/results/rgds/gen_3/checkpoint/added_tokens.json\\n/root/autodl-tmp/phase-gated-compound-sparse/results/rgds/gen_3/checkpoint/vocab.json\\n/root/autodl-tmp/phase-gated-compound-sparse/results/rgds/gen_3/checkpoint/tokenizer.json\\n/root/autodl-tmp/phase-gated-compound-sparse/results/rgds/gen_3/metrics.json\\n/root/autodl-tmp/phase-gated-compound-sparse/results/rgds/all_results.json\\n/root/autodl-tmp/phase-gated-compound-sparse/results/external_only/gen_0/metrics.json\\n/root/autodl-tmp/phase-gated-compound-sparse/results/external_only/gen_1/metrics.json\\n/root/autodl-tmp/phase-gated-compound-sparse/results/external_only/gen_2/metrics.json\\n/root/autodl-tmp/phase-gated-compound-sparse/results/external_only/gen_3/checkpoint/config.json\\n/root/autodl-tmp/phase-gated-compound-sparse/results/external_only/gen_3/checkpoint/generation_config.json\\n/root/autodl-tmp/phase-gated-compound-sparse/results/external_only/gen_3/checkpoint/tokenizer_config.json\\n/root/autodl-tmp/phase-gated-compound-sparse/results/external_only/gen_3/checkpoint/special_tokens_map.json\\n/root/autodl-tmp/phase-gated-compound-sparse/results/external_only/gen_3/checkpoint/added_tokens.json\\n/root/autodl-tmp/phase-gated-compound-sparse/results/external_only/gen_3/checkpoint/vocab.json
…[truncated 6365 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase2_3method_results_20260513T092435",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-13T09:26:41.982720+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11235",
  "command": "find /root/phase-gated-compound-sparse/ -name \"*.json\" -o -name \"*.csv\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase2_3method_results_20260513T092435",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11235",
    "command": "find /root/phase-gated-compound-sparse/ -name \"*.json\" -o -name \"*.csv\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-13T09:26:41.982860+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/phase-gated-compound-sparse/data/meta.json\\n/root/phase-gated-compound-sparse/data_gpt2/meta.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase2_3method_results_20260513T092435",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-13T09:26:41.983034+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11235",
  "command": "cat /root/autodl-tmp/phase-gated-compound-sparse/results_phase2/uncurated/all_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase2_3method_results_20260513T092435",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11235",
    "command": "cat /root/autodl-tmp/phase-gated-compound-sparse/results_phase2/uncurated/all_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-13T09:26:41.983292+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"method\\\": \\\"uncurated\\\",\\n  \\\"self_iterate\\\": true,\\n  \\\"generations\\\": [\\n    {\\n      \\\"held_out_perplexity\\\": 37.102710361067054,\\n      \\\"rankme\\\": 280.3191094474331,\\n      \\\"knn_probe_accuracy\\\": 0.988,\\n      \\\"rare_ngram_survival\\\": 0.029021637433826405,\\n      \\\"rank_correlation\\\": -0.022565274261097047,\\n      \\\"rank_correlation_pvalue\\\": 0.6146998858753108,\\n      \\\"generation\\\": 0,\\n      \\\"num_synthetic\\\": 975,\\n      \\\"num_selected\\\": 975,\\n      \\\"train_loss\\\": 1.1707164860162578,\\n      \\\"elapsed_seconds\\\": 415.5861828327179,\\n      \\\"selection_rare_ngram_selected\\\": NaN,\\n      \\\"selection_rare_ngram_rejected\\\": NaN,\\n      \\\"selection_rare_ngram_ratio\\\": NaN,\\n      \\\"qf_would_remove_count\\\": NaN,\\n      \\\"qf_removed_rare_ngram_mean\\\": NaN,\\n      \\\"qf_kept_rare_ngram_mean\\\": NaN\\n    },\\n    {\\n      \\\"held_out_perplexity\\\": 44.89425641997695,\\n      \\\"rankme\\\": 297.80240803510395,\\n      \\\"knn_probe_accuracy\\\": 0.988,\\n      \\\"rare_ngram_survival\\\": 0.019188862702369813,\\n      \\\"rank_correlation\\\": -0.05482284329137316,\\n      \\\"rank_correlation_pvalue\\\": 0.22105474945603323,\\n      \\\"generation\\\": 1,\\n      \\\"num_synthetic\\\": 977,\\n      \\\"num_selected\\\": 977,\\n      \\\"train_loss\\\": 0.46741220567907604,\\n      \\\"elapsed_seconds\\\": 413.15566778182983,\\n      \\\"selection_rare_ngram_selected\\\": NaN,\\n      \\\"selection_rare_ngram_rejected\\\": NaN,\\n      \\\"selection_rare_ngram_ratio\\\": NaN,\\n      \\\"qf_would_remove_count\\\": NaN,\\n      \\\"qf_removed_rare_ngram_mean\\\": NaN,\\n      \\\"qf_kept_rare_ngram_mean\\\": NaN\\n    },\\n    {\\n      \\\"held_out_perplexity\\\": 51.319646093335,\\n      \\\"rankme\\\": 302.47307456110633,\\n      \\\"knn_probe_accuracy\\\": 0.988,\\n      \\\"rare_ngram_survival\\
…[truncated 4957 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase2_3method_results_20260513T092435",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-13T09:26:41.983480+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11235",
  "command": "cat /root/autodl-tmp/phase-gated-compound-sparse/results_phase2/rgds/all_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase2_3method_results_20260513T092435",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11235",
    "command": "cat /root/autodl-tmp/phase-gated-compound-sparse/results_phase2/rgds/all_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-13T09:26:41.983712+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"method\\\": \\\"rgds\\\",\\n  \\\"self_iterate\\\": true,\\n  \\\"generations\\\": [\\n    {\\n      \\\"held_out_perplexity\\\": 37.0854700738961,\\n      \\\"rankme\\\": 275.89487699744393,\\n      \\\"knn_probe_accuracy\\\": 0.988,\\n      \\\"rare_ngram_survival\\\": 0.029021637433826405,\\n      \\\"rank_correlation\\\": -0.01232884931539726,\\n      \\\"rank_correlation_pvalue\\\": 0.7833147739664865,\\n      \\\"generation\\\": 0,\\n      \\\"num_synthetic\\\": 975,\\n      \\\"num_selected\\\": 487,\\n      \\\"train_loss\\\": 1.0696454766343853,\\n      \\\"elapsed_seconds\\\": 481.198694229126,\\n      \\\"selection_rare_ngram_selected\\\": 0.06859762296721308,\\n      \\\"selection_rare_ngram_rejected\\\": 0.06614179177205463,\\n      \\\"selection_rare_ngram_ratio\\\": 1.0371297953890033,\\n      \\\"qf_would_remove_count\\\": 6,\\n      \\\"qf_removed_rare_ngram_mean\\\": 0.075,\\n      \\\"qf_kept_rare_ngram_mean\\\": 0.06732119377687867\\n    },\\n    {\\n      \\\"held_out_perplexity\\\": 45.36063176320125,\\n      \\\"rankme\\\": 291.7626162558648,\\n      \\\"knn_probe_accuracy\\\": 0.988,\\n      \\\"rare_ngram_survival\\\": 0.02015407937278681,\\n      \\\"rank_correlation\\\": -0.045852663410653645,\\n      \\\"rank_correlation_pvalue\\\": 0.30618077349162387,\\n      \\\"generation\\\": 1,\\n      \\\"num_synthetic\\\": 977,\\n      \\\"num_selected\\\": 488,\\n      \\\"train_loss\\\": 0.497177140634568,\\n      \\\"elapsed_seconds\\\": 483.02173709869385,\\n      \\\"selection_rare_ngram_selected\\\": 0.07968304926737259,\\n      \\\"selection_rare_ngram_rejected\\\": 0.08760648621609315,\\n      \\\"selection_rare_ngram_ratio\\\": 0.9095565032801756,\\n      \\\"qf_would_remove_count\\\": 0,\\n      \\\"qf_removed_rare_ngram_mean\\\": NaN,\\n      \\\"qf_kept_rare_ngram_mean\\\": NaN\\n    },\\n    {\\n      \\\"held_out_perplexity\\\": 50.5136559592218,\\n      \\\"rankme\\\"
…[truncated 5317 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase2_3method_results_20260513T092435",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-13T09:26:41.983867+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11235",
  "command": "cat /root/autodl-tmp/phase-gated-compound-sparse/results_phase2/external_only/all_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase2_3method_results_20260513T092435",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11235",
    "command": "cat /root/autodl-tmp/phase-gated-compound-sparse/results_phase2/external_only/all_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-13T09:26:41.984102+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"method\\\": \\\"external_only\\\",\\n  \\\"self_iterate\\\": true,\\n  \\\"generations\\\": [\\n    {\\n      \\\"held_out_perplexity\\\": 37.04078437110428,\\n      \\\"rankme\\\": 275.0715092258104,\\n      \\\"knn_probe_accuracy\\\": 0.988,\\n      \\\"rare_ngram_survival\\\": 0.029021637433826405,\\n      \\\"rank_correlation\\\": 0.003078444313777255,\\n      \\\"rank_correlation_pvalue\\\": 0.9452570890038191,\\n      \\\"generation\\\": 0,\\n      \\\"num_synthetic\\\": 975,\\n      \\\"num_selected\\\": 487,\\n      \\\"train_loss\\\": 1.4189379479064317,\\n      \\\"elapsed_seconds\\\": 1064.5177867412567,\\n      \\\"selection_rare_ngram_selected\\\": 0.07168093471662981,\\n      \\\"selection_rare_ngram_rejected\\\": 0.0630647982844195,\\n      \\\"selection_rare_ngram_ratio\\\": 1.13662354699609,\\n      \\\"qf_would_remove_count\\\": 6,\\n      \\\"qf_removed_rare_ngram_mean\\\": 0.075,\\n      \\\"qf_kept_rare_ngram_mean\\\": 0.06732119377687867\\n    },\\n    {\\n      \\\"held_out_perplexity\\\": 44.285585544129205,\\n      \\\"rankme\\\": 291.6204669268669,\\n      \\\"knn_probe_accuracy\\\": 0.988,\\n      \\\"rare_ngram_survival\\\": 0.01839537169724173,\\n      \\\"rank_correlation\\\": -0.034508682034728136,\\n      \\\"rank_correlation_pvalue\\\": 0.441338089831013,\\n      \\\"generation\\\": 1,\\n      \\\"num_synthetic\\\": 977,\\n      \\\"num_selected\\\": 488,\\n      \\\"train_loss\\\": 0.595083087682724,\\n      \\\"elapsed_seconds\\\": 1073.4414548873901,\\n      \\\"selection_rare_ngram_selected\\\": 0.08583096728134776,\\n      \\\"selection_rare_ngram_rejected\\\": 0.07088767259252986,\\n      \\\"selection_rare_ngram_ratio\\\": 1.210802444801843,\\n      \\\"qf_would_remove_count\\\": 0,\\n      \\\"qf_removed_rare_ngram_mean\\\": NaN,\\n      \\\"qf_kept_rare_ngram_mean\\\": NaN\\n    },\\n    {\\n      \\\"held_out_perplexity\\\": 50.12278922311573,\\n      \\\"ran
…[truncated 5327 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase2_3method_results_20260513T092435",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-13T09:26:41.984380+00:00_

数据全部收集完毕。以下是 Phase 2 主实验完整分析。

---

## Phase 2 实验结果：3-method self-iterate (GPT2-125M, 8 代)

### 1. Perplexity (PPL) — 越低越好

| Gen | uncurated | rgds | external_only |
|-----|-----------|------|---------------|
| 0 | 37.10 | 37.09 | 37.04 |
| 1 | 44.89 | 45.36 | 44.29 |
| 2 | 51.32 | 50.51 | 50.12 |
| 3 | 56.25 | 53.82 | 53.55 |
| 4 | 55.88 | 53.97 | 52.27 |
| 5 | 50.08 | **61.75** | 47.37 |
| 6 | 48.25 | **64.12** | 46.11 |
| 7 | 50.28 | **75.07** | **45.51** |

**external_only** gen 3 后 PPL 持续下降（53.55→45.51），出现"自修复"效应。
**rgds** gen 4 后 PPL 爆炸式增长至 75.07——典型 model collapse。

### 2. Rare n-gram ratio — 越高越好（多样性保留）

| Gen | uncurated | rgds | external_only |
|-----|-----------|------|---------------|
| 0 | 0.0290 | 0.0290 | 0.0290 |
| 1 | 0.0192 | 0.0202 | 0.0184 |
| 2 | 0.0139 | 0.0151 | 0.0141 |
| 3 | 0.0118 | 0.0124 | 0.0117 |
| 4 | 0.0102 | 0.0099 | 0.0102 |
| 5 | 0.0099 | 0.0082 | 0.0100 |
| 6 | 0.0094 | **0.0067** | **0.0103** |
| 7 | 0.0090 | **0.0051** | **0.0099** |

**external_only** gen 4 后稳定在 ~0.010，gen 6 甚至回升。
**rgds** 单调下降至 0.0051——多样性崩塌最严重，仅剩 external_only 的一半。

### 3. Selection Ratio（alignment gap 核心指标）

| Gen | rgds | external_only |
|-----|------|---------------|
| 0 | 1.037 | **1.137** |
| 1 | 0.910 | **1.211** |
| 2 | 0.927 | **1.116** |
| 3 | 0.941 | **1.196** |
| 4 | 0.896 | **1.282** |
| 5 | 0.811 | **1.109** |
| 6 | 0.717 | **1.123** |
| 7 | **0.517** | **1.095** |

**external_only 全 8 代 ratio > 1.0**（范围 1.095–1.282），证明外部参考 consistently 偏好高多样性样本。

**rgds 仅 gen 0 > 1.0，随后单调下降至 0.517**——RGDS 在自迭代中逐渐偏好同质化内容，ratio < 1 意味着选出的数据比丢弃的数据**更不多样**。

### 4. Rank Correlation — 越接近 0 越好

| Gen | uncurated | rgds | external_only |
|-----|-----------|------|---------------|
| 0 | -0.023 | -0.012 | +0.003 |
| 4 | -0.035 | -0.048 | -0.017 |
| 7 | **-0.088** (p=0.049) | -0.039 | **+0.011** |

**external_only** 从 +0.003 到 +0.011，几乎无分布漂移。
**uncurated** 漂移至 -0.088（已达统计显著），分布系统性偏移。

### 5. RankMe & k-NN

- **k-NN accuracy**：三种方法全部 0.988，无区分度。
- **RankMe**：三者 gen 7 收敛至 290–293，区分度低。uncurated 早期最高（303），但最终无优势。

---

## 核心结论

| 维度 | 排名 | 说明 |
|------|------|------|
| PPL 稳定性 | external_only >> uncurated >> rgds | external_only 自修复，rgds 崩塌 |
| 多样性保留 | external_only > uncurated >> rgds | rgds 仅存 uncurated 57%、external_only 52% 的多样性 |
| Selection ratio | external_only 全程 >1.0 | rgds 从 1.04 崩至 0.52 |
| 分布漂移 | external_only ≈ 0 < rgds < uncurated | uncurated 漂移最大且显著 |

**三条关键发现：**

1. **RGDS 在 self-iterate 中有害**——验证 D008 结论。因为 RGDS 的参考分布来自模型自身（随代数退化），导致 selection ratio 单调下降，主动选出低多样性数据，加速崩塌。

2. **external_only 是唯一能抑制多样性崩塌的方法**——外部锚点（real data embedding）不随迭代退化，selection ratio 全程 > 1.0，rare n-gram 稳定在 0.010，PPL 在后期反而改善。

3. **uncurated 表现居中**——不做任何选择，多样性仍缓慢衰减，但不如 rgds 那样灾难性崩塌。这说明"不选择"优于"错误的选择"。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_phase2_3method_results_20260513T092435"
}
```

</details>

---
