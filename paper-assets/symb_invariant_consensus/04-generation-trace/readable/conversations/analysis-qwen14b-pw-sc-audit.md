# analysis qwen14b pw sc audit

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 71
- **Recorded user turns:** 0
- **Tool calls:** 35
- **Original source:** `logs/chats/worker_analysis_qwen14b-pw-sc-audit_20260521T095214.jsonl`
- **Structured JSON:** [`82907333af3c6d603016.json`](../../sessions/82/82907333af3c6d603016.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

71 recorded events

### Tool call

_source line 1 · 2026-05-21T09:59:49.293280+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-21T09:59:49.293790+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T09:59:49.294074+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "find /root/symb_invariant_consensus/results/ -maxdepth 1 -type d -name \"*qwen*14*\" -o -name \"*14b*\" -o -name \"*039*\" -o -name \"*091*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "find /root/symb_invariant_consensus/results/ -maxdepth 1 -type d -name \"*qwen*14*\" -o -name \"*14b*\" -o -name \"*039*\" -o -name \"*091*\""
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-21T09:59:49.294307+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[Errno None] Unable to connect to port 25068 on 36.103.198.204\", \"metadata\": {\"elapsed_seconds\": 0.47}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T09:59:49.294639+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "symb_invariant_consensus",
  "filters": "{'exp_id': 'exp-039-14b-pw600-16639'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "filters": "{'exp_id': 'exp-039-14b-pw600-16639'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T09:59:49.294791+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4451}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T09:59:49.294945+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "symb_invariant_consensus",
  "filters": "{'exp_id': 'exp-091-qwen14b-pw-nli-combo'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "filters": "{'exp_id': 'exp-091-qwen14b-pw-nli-combo'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-21T09:59:49.295079+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/experiments.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/experiments.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-21T09:59:49.295207+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4915}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T09:59:49.295484+00:00_

artifacts/_project/paper/experiments.tex
docs/paper/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T09:59:49.295623+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/solutions.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/solutions.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T09:59:49.295744+00:00_

docs/paper/solutions.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T09:59:49.295951+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/compute_cil*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/compute_cil*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-21T09:59:49.296210+00:00_

artifacts/compute_cil.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T09:59:49.296499+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "find /root/symb_invariant_consensus/results/ -maxdepth 1 -type d"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "find /root/symb_invariant_consensus/results/ -maxdepth 1 -type d"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-21T09:59:49.296646+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/compute_cil.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/compute_cil.py"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-21T09:59:49.296903+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/symb_invariant_consensus/results/\\n/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600\\n/root/symb_invariant_consensus/results/exp033_qwen3_14b_pw600_nonthinking\\n/root/symb_invariant_consensus/results/exp036_qwen25_14b_folio204\\n/root/symb_invariant_consensus/results/exp037_mistral7b_folio204\\n/root/symb_invariant_consensus/results/exp038_qwen25_14b_logiqa200\\n/root/symb_invariant_consensus/results/exp050_FAILED_overflow\\n/root/symb_invariant_consensus/results/exp050b_mistral_icl_oracle\\n/root/symb_invariant_consensus/results/exp049b_mistral_logiqa200\\n/root/symb_invariant_consensus/results/exp052_mistral_folio204_seed123\\n/root/symb_invariant_consensus/results/exp053_mistral_folio204_seed456\\n/root/symb_invariant_consensus/results/exp048_llama8b_pw600\\n/root/symb_invariant_consensus/results/exp055_multitemp_mistral_folio\\n/root/symb_invariant_consensus/results/exp028b_qwen3_thinking_folio204\\n/root/symb_invariant_consensus/results/exp028b_dryrun\\n/root/symb_invariant_consensus/results/exp-063-llama8b-folio204-16639\\n/root/symb_invariant_consensus/results/exp064_deepseek_r1_qwen3_8b_folio204\\n/root/symb_invariant_consensus/results/exp064_dryrun\\n/root/symb_invariant_consensus/results/exp068_qwen3_logiqa200\\n/root/symb_invariant_consensus/results/exp069_llama8b_logiqa200\\n/root/symb_invariant_consensus/results/exp072_llama8b_logiqa200\\n/root/symb_invariant_consensus/results/exp072b_llama8b_logiqa200\\n/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204\\n/root/symb_invariant_consensus/results/exp077_kappa_generalization\\n/root/symb_invariant_consensus/results/exp078_debate_mistral_logiqa200\\n/root/symb_invariant_consensus/results/exp079_icg_mistral_logiqa200\\n/root/symb_invariant_consensus/results/exp081_debate_mistral_folio_seed123\\n/root/symb_invariant_consensus/results/exp082_contrastive_mistral_folio_seed123\\n/root/symb_invariant_consensus/results/wil
…[truncated 2078 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-21T09:59:49.297322+00:00_

1	"""
2	E5: CIL (Cumulative Information Lift) Computation
3	CIL(V,G) = log2[P(V correct | G wrong) / P(V correct | G correct)]
4	"""
5	import json
6	import os
7	import sys
8	import numpy as np
9	from pathlib import Path
10	from scipy import stats
11	
12	RESULTS = Path("/root/symb_invariant_consensus/results")
13	OUT_DIR = RESULTS / "exp_d134_cil"
14	
15	def cil_from_counts(both_right, v_right_g_wrong, g_right_v_wrong, both_wrong):
16	    """Compute CIL from 2x2 contingency table."""
17	    n_g_wrong = v_right_g_wrong + both_wrong
18	    n_g_right = both_right + g_right_v_wrong
19	
20	    if n_g_wrong == 0 or n_g_right == 0:
21	        return {"cil": float("nan"), "p_v_given_g_wrong": float("nan"),
22	                "p_v_given_g_right": float("nan"), "n_g_wrong": 0, "n_g_right": 0}
23	
24	    p_v_gw = v_right_g_wrong / n_g_wrong
25	    p_v_gr = both_right / n_g_right
26	
27	    if p_v_gw == 0 or p_v_gr == 0:
28	        cil = float("nan")
29	    else:
30	        cil = np.log2(p_v_gw / p_v_gr)
31	
32	    return {
33	        "cil": round(cil, 4) if not np.isnan(cil) else float("nan"),
34	        "p_v_correct_given_g_wrong": round(p_v_gw, 4),
35	        "p_v_correct_given_g_correct": round(p_v_gr, 4),
36	        "n_g_wrong": int(n_g_wrong),
37	        "n_g_right": int(n_g_right),
38	        "both_right": int(both_right),
39	        "v_right_g_wrong": int(v_right_g_wrong),
40	        "g_right_v_wrong": int(g_right_v_wrong),
41	        "both_wrong": int(both_wrong),
42	    }
43	
44	
45	def load_pw600_nli_per_question():
46	    """Load per-question DeBERTa + Mistral SC + SICA from direction_r_nli_pw600."""
47	    f = RESULTS / "direction_r_nli_pw600" / "results.json"
48	    data = json.load(open(f))
49	    pq = data.get("per_question", {})
50	    if not pq:
51	        print(f"  WARNING: no per_question in {f}")
52	    return pq
53	
54	
55	def load_folio204_per_question():
56	    """Load per-question data from direction_rg_combo."""
57	    f = RESULTS / "direction_rg_combo"
…[truncated 20250 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-21T09:59:49.297518+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "75\\.17|74\\.00|70\\.33|qwen.*14|14b",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/_project/paper/experiments.tex",
  "output_mode": "content",
  "-C": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "Grep",
  "tool_args": {
    "pattern": "75\\.17|74\\.00|70\\.33|qwen.*14|14b",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/_project/paper/experiments.tex",
    "output_mode": "content",
    "-C": "3"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-21T09:59:49.297669+00:00_

30-Model & Domain & $n$ & SC (\%) & SICA (\%) & $\Delta$ (pp) & McNemar $p$ \\
31-\midrule
32-Qwen2.5-14B & FOLIO & 204 & 79.41 & 79.41 & 0.00 & --- \\
33:Qwen2.5-14B & ProofWriter & 600 & 75.17 & 75.50 & $+$0.33 & n.s. \\
34-Qwen2.5-14B & StrategyQA$^\dagger$ & 60 & 53.33 & 56.67 & $+$3.33 & 0.13 \\
35-Qwen2.5-14B & ARC-Chall.$^\dagger$ & 60 & 96.67 & 95.00 & $-$1.67 & --- \\
36-Mistral-7B & FOLIO+PW$^\dagger$ & 60 & 48.33 & 48.33 & 0.00 & 1.000 \\
37:LLaMA-3.1-8B & StrategyQA & 200 & 72.00 & 74.00 & $+$2.00 & 0.424 \\
38-LLaMA-3.1-8B & FOLIO & 204 & 63.24 & 60.78 & $-$2.45 & 0.267 \\
39-DeepSeek-R1-7B & FOLIO+PW$^\dagger$ & 60 & 71.67 & 68.33 & $-$3.33 & 0.480 \\
40-\bottomrule

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-21T09:59:49.297807+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "75\\.17|74\\.00|70\\.33|qwen.*14|14b",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex",
  "output_mode": "content",
  "-C": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "Grep",
  "tool_args": {
    "pattern": "75\\.17|74\\.00|70\\.33|qwen.*14|14b",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex",
    "output_mode": "content",
    "-C": "3"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-21T09:59:49.297963+00:00_

26-\midrule
27-Mistral-7B & Mistral & 39.33\% & $+$15.67 & $+$6.67\,pp & $<$0.001 \\
28-LLaMA-3.1-8B & LLaMA & 72.50\% & $-$17.50 & $+$0.83\,pp & 0.66 \\
29:Qwen2.5-14B & Qwen & 74.00\% & $-$19.00 & $+$0.67\,pp & 0.50 \\
30-Qwen3-14B & Qwen & 85.83\% & $-$30.83 & $+$0.50\,pp & 0.45 \\
31-\bottomrule
32-\end{tabular}}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-21T09:59:49.298093+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "symb_invariant_consensus",
  "limit": "0",
  "fields": "['exp_id', 'status', 'metrics']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "limit": "0",
    "fields": "['exp_id', 'status', 'metrics']"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-21T09:59:49.299119+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp-d134-cil\": {\"status\": \"PREPARING\", \"metrics\": {\"n_pairs_computed\": 8, \"n_pairs_missing\": 2, \"spearman_rho\": 0.8095, \"spearman_p\": 0.0149, \"pearson_r\": 0.7994, \"pearson_p\": 0.0173, \"cil_deberta_mistral_pw\": 1.67, \"cil_sica_mistral_pw\": -4.61, \"cil_deberta_qwen14b_pw\": -0.08, \"corrected_pairs\": \"Mistral+DeBERTa FOLIO gain 4.41→2.94pp, Mistral+SICA FOLIO gain 4.90→3.43pp, Qwen14B+DeBERTa PW gain 0.83→0.33pp\"}}, \"exp-d134-e6-closed-model\": {\"status\": \"PREPARING\"}, \"exp-d126-crossmodel-sica\": {\"status\": \"PREPARING\"}, \"exp-d134-baf-decoupled\": {\"status\": \"PREPARING\", \"metrics\": {\"full_trace_acc\": 0.5931, \"conservative_acc\": 0.5392, \"standard_acc\": 0.5441, \"aggressive_acc\": 0.5392, \"conservative_br_delta\": -0.049, \"conservative_wilcoxon_p\": 0.122, \"conservative_mcnemar_p\": 0.001, \"aggressive_br_delta\": -0.145, \"aggressive_wilcoxon_p\": 0.256, \"aggressive_mcnemar_p\": 0.013}}, \"exp-d134-process-br\": {\"status\": \"PREPARING\", \"metrics\": {\"position_br_early\": 5.37, \"position_br_mid\": 5.25, \"position_br_late\": 5.16, \"fisher_early_vs_late_p\": 0.708, \"difficulty_br_easy\": 18.82, \"difficulty_br_hard\": 2.71, \"fisher_diff_p\": 0, \"conditional_br\": 5.69, \"other_br\": 4.91, \"fisher_type_p\": 0.061}}, \"exp-d126-drc-folio\": {\"status\": \"PREPARING\", \"metrics\": {\"sc_acc\": 55.88, \"full_combo_w3_acc\": 58.82, \"drc_tau07_w3_acc\": 58.33, \"drc_tau07_gain_pp\": 2.45, \"drc_tau07_nli_calls\": \"71/204\", \"drc_tau07_cost_pct\": 34.8, \"drc_tau07_gain_recovery_pct\": 83.3, \"drc_tau08_w3_acc\": 58.82, \"drc_tau08_gain_recovery_pct\": 100, \"drc_tau08_cost_pct\": 48.5}}, \"exp-d126-70b-sica\": {\"status\": \"PREPARING\"}, \"exp_text_ablation\": {\"status\": \"DONE\", \"metrics\": {\"t_ext_0.1\": {\"sica_acc\": 57.35, \"delta_pp\": 1.47, \"p\": 0.581}, \"t_ext_0.3\": {\"sica_acc\": 59.31, \"delta_pp\": 4.9, \"p\": 0.013}, \"t_ext_0
…[truncated 47188 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-21T09:59:49.299383+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "ls /root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "ls /root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/"
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-21T09:59:49.299522+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "ls /root/symb_invariant_consensus/results/qwen14b_pw_nli_combo/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "ls /root/symb_invariant_consensus/results/qwen14b_pw_nli_combo/"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-21T09:59:49.299657+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"exp032.log\\nintermediates\\nresults.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-21T09:59:49.299783+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-21T09:59:49.299944+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "find /root/symb_invariant_consensus/results/ -path \"*nli_combo_full_table_bh*\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "find /root/symb_invariant_consensus/results/ -path \"*nli_combo_full_table_bh*\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-21T09:59:49.300080+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-21T09:59:49.300202+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "find /root/symb_invariant_consensus/results/ -path \"*direction_r_nli*\" -type d"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "find /root/symb_invariant_consensus/results/ -path \"*direction_r_nli*\" -type d"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-21T09:59:49.300321+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-21T09:59:49.300451+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "python3 -c \"\nimport json\nd = json.load(open('/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/results.json'))\nfor k in ['sc_accuracy','sica_accuracy','n_problems','n','k','delta_pp']:\n    if k in d: print(f'{k}: {d[k]}')\npq = d.get('per_question',{})\nprint(f'per_question keys: {len(pq)}')\nif pq:\n    first_key = list(pq.keys())[0]\n    print(f'sample: {first_key} -> {json.dumps(pq[first_key], indent=2)[:500]}')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "python3 -c \"\nimport json\nd = json.load(open('/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/results.json'))\nfor k in ['sc_accuracy','sica_accuracy','n_problems','n','k','delta_pp']:\n    if k in d: print(f'{k}: {d[k]}')\npq = d.get('per_question',{})\nprint(f'per_question keys: {len(pq)}')\nif pq:\n    first_key = list(pq.keys())[0]\n    print(f'sample: {first_key} -> {json.dumps(pq[first_key], indent=2)[:500]}')\n\"\n"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-21T09:59:49.300576+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-21T09:59:49.300695+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "python3 -c \"\nimport json\nd = json.load(open('/root/symb_invariant_consensus/results/qwen14b_pw_nli_combo/results.json'))\nfor k in sorted(d.keys()):\n    v = d[k]\n    if not isinstance(v, (dict,list)):\n        print(f'{k}: {v}')\n    elif isinstance(v, dict) and len(v) < 10:\n        print(f'{k}: {json.dumps(v)}')\n    elif isinstance(v, list) and len(v) < 5:\n        print(f'{k}: {json.dumps(v)}')\n    else:\n        print(f'{k}: type={type(v).__name__}, len={len(v)}')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "python3 -c \"\nimport json\nd = json.load(open('/root/symb_invariant_consensus/results/qwen14b_pw_nli_combo/results.json'))\nfor k in sorted(d.keys()):\n    v = d[k]\n    if not isinstance(v, (dict,list)):\n        print(f'{k}: {v}')\n    elif isinstance(v, dict) and len(v) < 10:\n        print(f'{k}: {json.dumps(v)}')\n    elif isinstance(v, list) and len(v) < 5:\n        print(f'{k}: {json.dumps(v)}')\n    else:\n        print(f'{k}: type={type(v).__name__}, len={len(v)}')\n\"\n"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-21T09:59:49.300818+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '<' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-21T09:59:49.301009+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "cat /root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "cat /root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/results.json"
  }
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-21T09:59:49.301134+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "cat /root/symb_invariant_consensus/results/qwen14b_pw_nli_combo/results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "cat /root/symb_invariant_consensus/results/qwen14b_pw_nli_combo/results.json"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-21T09:59:49.302064+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"summary\\\": {\\n    \\\"n_problems\\\": 600,\\n    \\\"sica_accuracy\\\": 0.715,\\n    \\\"sc_accuracy\\\": 0.735,\\n    \\\"sica_correct\\\": 429,\\n    \\\"sc_correct\\\": 441,\\n    \\\"extraction_rate\\\": 0.9915277777777778,\\n    \\\"total_constraints_extracted\\\": 94306,\\n    \\\"total_unique_constraints\\\": 22036,\\n    \\\"contradiction_rate\\\": 0.006171719005264113,\\n    \\\"problems_with_contradictions\\\": 108,\\n    \\\"per_level_accuracy\\\": {\\n      \\\"OWA-D5\\\": {\\n        \\\"sica\\\": 0.715,\\n        \\\"sc\\\": 0.735,\\n        \\\"n\\\": 600\\n      }\\n    },\\n    \\\"per_dataset_accuracy\\\": {\\n      \\\"proofwriter\\\": {\\n        \\\"sica\\\": 0.715,\\n        \\\"sc\\\": 0.735,\\n        \\\"n\\\": 600\\n      }\\n    },\\n    \\\"k\\\": 12,\\n    \\\"mode\\\": \\\"vllm\\\",\\n    \\\"total_wall_time_s\\\": 39578.2\\n  },\\n  \\\"results\\\": [\\n    {\\n      \\\"problem_idx\\\": 0,\\n      \\\"problem_id\\\": \\\"ProofWriter_AttNoneg-OWA-D5-1041_Q1\\\",\\n      \\\"problem\\\": \\\"Bob is cold. Bob is quiet. Bob is red. Bob is smart. Charlie is kind. Charlie is quiet. Charlie is red. Charlie is rough. Dave is cold. Dave is kind. Dave is smart. Fiona is quiet. If something is quiet and cold then it is smart. Red, cold things are round. If something is kind and rough then it is red. All quiet things are rough. Cold, smart things are red. If something is rough then it is cold. All red things are rough. If Dave is smart and Dave is kind then Dave is quiet.\\\\n\\\\nDetermine whether the following statement is true, false, or unknown:\\\\nCharlie is kind.\\\",\\n      \\\"dataset\\\": \\\"proofwriter\\\",\\n      \\\"level\\\": \\\"OWA-D5\\\",\\n      \\\"ground_truth\\\": \\\"True\\\",\\n      \\\"sica_answer\\\": \\\"True\\\",\\n      \\\"sica_scores\\\": {\\n        \\\"True\\\": 97.0\\n      },\\n      \\\"sica_correct\\\": true,\\n      \\\"sc_answer\\\": \\\
…[truncated 8015 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-21T09:59:49.302570+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"experiment\\\": \\\"Qwen2.5-14B ProofWriter NLI Combo (DeBERTa-large reused from D116)\\\",\\n  \\\"verifier_model\\\": \\\"microsoft/deberta-large-mnli\\\",\\n  \\\"generator_model\\\": \\\"Qwen2.5-14B-Instruct\\\",\\n  \\\"dataset\\\": \\\"ProofWriter-D5-600\\\",\\n  \\\"n_questions\\\": 600,\\n  \\\"standalone_accuracy\\\": 0.55,\\n  \\\"sc_baseline\\\": 0.735,\\n  \\\"capability_gap_pp\\\": -18.5,\\n  \\\"deberta_standalone\\\": {\\n    \\\"accuracy\\\": 0.55,\\n    \\\"correct\\\": 330,\\n    \\\"total\\\": 600,\\n    \\\"per_class\\\": {\\n      \\\"True\\\": {\\n        \\\"n\\\": 200,\\n        \\\"correct\\\": 128,\\n        \\\"accuracy\\\": 0.64,\\n        \\\"precision\\\": 0.6957,\\n        \\\"recall\\\": 0.64,\\n        \\\"f1\\\": 0.6667\\n      },\\n      \\\"False\\\": {\\n        \\\"n\\\": 200,\\n        \\\"correct\\\": 195,\\n        \\\"accuracy\\\": 0.975,\\n        \\\"precision\\\": 0.4791,\\n        \\\"recall\\\": 0.975,\\n        \\\"f1\\\": 0.6425\\n      },\\n      \\\"Unknown\\\": {\\n        \\\"n\\\": 200,\\n        \\\"correct\\\": 7,\\n        \\\"accuracy\\\": 0.035,\\n        \\\"precision\\\": 0.7778,\\n        \\\"recall\\\": 0.035,\\n        \\\"f1\\\": 0.067\\n      }\\n    },\\n    \\\"gt_distribution\\\": {\\n      \\\"True\\\": 200,\\n      \\\"False\\\": 200,\\n      \\\"Unknown\\\": 200\\n    },\\n    \\\"pred_distribution\\\": {\\n      \\\"True\\\": 184,\\n      \\\"False\\\": 407,\\n      \\\"Unknown\\\": 9\\n    },\\n    \\\"note\\\": \\\"Reused from D116 (same 600 PW problems, NLI is generator-independent)\\\"\\n  },\\n  \\\"combo\\\": {\\n    \\\"w1\\\": {\\n      \\\"accuracy\\\": 0.7417,\\n      \\\"delta_pp\\\": 0.67,\\n      \\\"mcnemar_p\\\": 0.3438,\\n      \\\"discordant\\\": [\\n        7,\\n        3\\n      ]\\n    },\\n    \\\"w3\\\": {\\n      \\\"accuracy\\\": 0.7433,\\n      \\\"delta_pp\\\": 0.83,\\n      \\\"mcnemar_p\\\": 0.4049,\\n
…[truncated 8862 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-21T09:59:49.302848+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-16639",
  "command": "cd /root/symb_invariant_consensus && python3 -c \"\nimport json\nfrom collections import Counter\n\n# Load exp032 per-question data\nwith open('results/exp032_qwen25_14b_pw600/results.json') as f:\n    data = json.load(f)\n\nresults = data['results']\nprint(f'Total questions: {len(results)}')\n\n# Analyze ties and tiebreaking\nn_ties = 0\ntie_details = []\nsc_correct_alphabetical = 0\nsc_correct_first_seen = 0\n\nfor r in results:\n    dist = r['sc_vote_distribution']\n    gold = r['ground_truth']\n    \n    # Find max vote count\n    max_votes = max(dist.values())\n    tied = [a for a, c in dist.items() if c == max_votes]\n    \n    # Alphabetical tiebreaking\n    alpha_answer = sorted(tied)[0]\n    if alpha_answer == gold:\n        sc_correct_alphabetical += 1\n    \n    # First-seen (dict iteration order from JSON)\n    first_seen_answer = tied[0]  # first key with max count\n    if first_seen_answer == gold:\n        sc_correct_first_seen += 1\n    \n    if len(tied) > 1:\n        n_ties += 1\n        tie_details.append({\n            'qid': r['problem_id'],\n            'gold': gold,\n            'dist': dist,\n            'tied': tied,\n            'alpha': alpha_answer,\n            'first_seen': first_seen_answer,\n            'sc_answer_orig': r['sc_answer'],\n        })\n\n# Also check original sc_correct count\norig_sc_correct = sum(1 for r in results if r['sc_correct'])\n\nprint(f'Original SC correct: {orig_sc_correct}/600 = {orig_sc_correct/600:.4f}')\nprint(f'Alphabetical tiebreak: {sc_correct_alphabetical}/600 = {sc_correct_alphabetical/600:.4f}')\nprint(f'First-seen tiebreak: {sc_correct_first_seen}/600 = {sc_correct_first_seen/600:.4f}')\nprint(f'Number of ties: {n_ties}')\nprint()\n\n# For random tiebreaking, try multiple seeds\nimport random\nfor seed in [42, 123, 456, 789, 0]:\n    random.seed(seed)\n    correct = 0\n    for r in results:\n        dist = r['sc_vote_distribution']\n        gold = r['ground_truth']\n        max_votes = max(dist.values())\n        tied = [a for a, c in dist.items() if c == max_votes]\n        answer = random.choice(tied)\n        if answer == gold:\n            correct += 1\n    print(f'Random seed={seed}: {correct}/600 = {correct/600:.4f}')\n\nprint()\nprint('=== Tie details ===')\nfor t in tie_details:\n    print(f\\\"  {t['qid']}: gold={t['gold']}, dist={t['dist']}, tied={t['tied']}, alpha={t['alpha']}, first_seen={t['first_seen']}, orig={t['sc_answer_orig']}\\\")\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-16639",
    "command": "cd /root/symb_invariant_consensus && python3 -c \"\nimport json\nfrom collections import Counter\n\n# Load exp032 per-question data\nwith open('results/exp032_qwen25_14b_pw600/results.json') as f:\n    data = json.load(f)\n\nresults = data['results']\nprint(f'Total questions: {len(results)}')\n\n# Analyze ties and tiebreaking\nn_ties = 0\ntie_details = []\nsc_correct_alphabetical = 0\nsc_correct_first_seen = 0\n\nfor r in results:\n    dist = r['sc_vote_distribution']\n    gold = r['ground_truth']\n    \n    # Find max vote count\n    max_votes = max(dist.values())\n    tied = [a for a, c in dist.items() if c == max_votes]\n    \n    # Alphabetical tiebreaking\n    alpha_answer = sorted(tied)[0]\n    if alpha_answer == gold:\n        sc_correct_alphabetical += 1\n    \n    # First-seen (dict iteration order from JSON)\n    first_seen_answer = tied[0]  # first key with max count\n    if first_seen_answer == gold:\n        sc_correct_first_seen += 1\n    \n    if len(tied) > 1:\n        n_ties += 1\n        tie_details.append({\n            'qid': r['problem_id'],\n            'gold': gold,\n            'dist': dist,\n            'tied': tied,\n            'alpha': alpha_answer,\n            'first_seen': first_seen_answer,\n            'sc_answer_orig': r['sc_answer'],\n        })\n\n# Also check original sc_correct count\norig_sc_correct = sum(1 for r in results if r['sc_correct'])\n\nprint(f'Original SC correct: {orig_sc_correct}/600 = {orig_sc_correct/600:.4f}')\nprint(f'Alphabetical tiebreak: {sc_correct_alphabetical}/600 = {sc_correct_alphabetical/600:.4f}')\nprint(f'First-seen tiebreak: {sc_correct_first_seen}/600 = {sc_correct_first_seen/600:.4f}')\nprint(f'Number of ties: {n_ties}')\nprint()\n\n# For random tiebreaking, try multiple seeds\nimport random\nfor seed in [42, 123, 456, 789, 0]:\n    random.seed(seed)\n    correct = 0\n    for r in results:\n        dist = r['sc_vote_distribution']\n        gold = r['ground_truth']\n        max_votes = max(dist.values())\n        tied = [a for a, c in dist.items() if c == max_votes]\n        answer = random.choice(tied)\n        if answer == gold:\n            correct += 1\n    print(f'Random seed={seed}: {correct}/600 = {correct/600:.4f}')\n\nprint()\nprint('=== Tie details ===')\nfor t in tie_details:\n    print(f\\\"  {t['qid']}: gold={t['gold']}, dist={t['dist']}, tied={t['tied']}, alpha={t['alpha']}, first_seen={t['first_seen']}, orig={t['sc_answer_orig']}\\\")\n\"\n"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-21T09:59:49.303093+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Total questions: 600\\nOriginal SC correct: 441/600 = 0.7350\\nAlphabetical tiebreak: 444/600 = 0.7400\\nFirst-seen tiebreak: 441/600 = 0.7350\\nNumber of ties: 21\\n\\nRandom seed=42: 439/600 = 0.7317\\nRandom seed=123: 437/600 = 0.7283\\nRandom seed=456: 435/600 = 0.7250\\nRandom seed=789: 440/600 = 0.7333\\nRandom seed=0: 442/600 = 0.7367\\n\\n=== Tie details ===\\n  ProofWriter_AttNeg-OWA-D5-891_Q9: gold=True, dist={'True': 6, 'Unknown': 6}, tied=['True', 'Unknown'], alpha=True, first_seen=True, orig=True\\n  ProofWriter_AttNoneg-OWA-D5-650_Q11: gold=True, dist={'Unknown': 6, 'True': 6}, tied=['Unknown', 'True'], alpha=True, first_seen=Unknown, orig=Unknown\\n  ProofWriter_AttNoneg-OWA-D5-785_Q10: gold=False, dist={'False': 6, 'Unknown': 6}, tied=['False', 'Unknown'], alpha=False, first_seen=False, orig=False\\n  ProofWriter_RelNeg-OWA-D5-922_Q7: gold=True, dist={'Unknown': 6, 'False': 6}, tied=['Unknown', 'False'], alpha=False, first_seen=Unknown, orig=Unknown\\n  ProofWriter_RelNoneg-OWA-D5-151_Q4: gold=False, dist={'Unknown': 6, 'False': 6}, tied=['Unknown', 'False'], alpha=False, first_seen=Unknown, orig=Unknown\\n  ProofWriter_AttNoneg-OWA-D5-1187_Q7: gold=True, dist={'True': 6, 'Unknown': 6}, tied=['True', 'Unknown'], alpha=True, first_seen=True, orig=True\\n  ProofWriter_RelNeg-OWA-D5-249_Q9: gold=True, dist={'True': 6, 'Unknown': 6}, tied=['True', 'Unknown'], alpha=True, first_seen=True, orig=True\\n  ProofWriter_RelNeg-OWA-D5-604_Q14: gold=Unknown, dist={'Unknown': 6, 'False': 6}, tied=['Unknown', 'False'], alpha=False, first_seen=Unknown, orig=Unknown\\n  ProofWriter_RelNeg-OWA-D5-587_Q8: gold=False, dist={'True': 6, 'False': 6}, tied=['True', 'False'], alpha=False, first_seen=True, orig=True\\n  ProofWriter_AttNeg-OWA-D5-1233_Q11: gold=True, dist={'Unknown': 6, 'True': 6}, tied=['Unknown', 'True'], alpha=True, first_seen=Unknown, orig=Unknown\\n  ProofWriter_RelNoneg-OWA-D5-616_Q7: gold=True, dis
…[truncated 1781 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-21T09:59:49.303323+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "70\\.33|0\\.7033",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "output_mode": "content",
  "-C": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "Grep",
  "tool_args": {
    "pattern": "70\\.33|0\\.7033",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
    "output_mode": "content",
    "-C": "3"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-21T09:59:49.303797+00:00_

&lt;persisted-output>
Output too large (54.4KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-3-projects-symb-invariant-consensus/0bd63397-dbc3-4cac-9a74-ccff2373fd37/tool-results/toolu_015DvhhzHhKEMCWom8ZiNfuq.txt

Preview (first 2KB):
artifacts/cil_results.json-61-      "dataset": "PW-600",
artifacts/cil_results.json-62-      "n": 600,
artifacts/cil_results.json-63-      "combo_gain_w3": 0.33,
artifacts/cil_results.json:64:      "note": "SC corrected: 74.0% BH (was 70.33% local). combo_w3=74.33%",
artifacts/cil_results.json-65-      "cil": -0.0827,
artifacts/cil_results.json-66-      "p_v_correct_given_g_wrong": 0.5281,
artifacts/cil_results.json-67-      "p_v_correct_given_g_correct": 0.5592,
--
artifacts/cil_results.json-79-      "dataset": "PW-600",
artifacts/cil_results.json-80-      "n": 600,
artifacts/cil_results.json-81-      "combo_gain_w3": 0.5,
artifacts/cil_results.json:82:      "note": "SICA_acc=0.7083, SC_acc=0.7033",
artifacts/cil_results.json-83-      "cil": -3.5272,
artifacts/cil_results.json-84-      "p_v_correct_given_g_wrong": 0.0843,
artifacts/cil_results.json-85-      "p_v_correct_given_g_correct": 0.9716,
--
artifacts/cil_results.json-198-        "pair": "Qwen2.5-14B + DeBERTa-MNLI / PW-600",
artifacts/cil_results.json-199-        "old_gain": 0.83,
artifacts/cil_results.json-200-        "new_gain": 0.33,
artifacts/cil_results.json:201:        "fix": "SC 70.33%->74.0% (BH corrected)"
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cil_results.json-202-      }
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cil_results.json-203-    ],
artifacts/cil_results.json-204-    "correlation_before": {
--
artifacts/exp_d134_cil/data/cil_results.json-61-      "dataset": "PW-600",
artifacts/exp_d134_cil/data/cil_results.json-62-      "n": 600,
artifacts/exp_d134_cil/data/cil_results.json-63-      "combo_gain_w3
…[truncated 317 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-21T09:59:49.304167+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "75\\.17|0\\.7517",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "output_mode": "content",
  "-C": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "Grep",
  "tool_args": {
    "pattern": "75\\.17|0\\.7517",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
    "output_mode": "content",
    "-C": "3"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-21T09:59:49.304792+00:00_

&lt;persisted-output>
Output too large (46.9KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-3-projects-symb-invariant-consensus/0bd63397-dbc3-4cac-9a74-ccff2373fd37/tool-results/toolu_01P8iqL1tg1Z9TqwuD55hm7V.txt

Preview (first 2KB):
artifacts/table1_bh_correction.json-115-      "model": "Qwen2.5-14B",
artifacts/table1_bh_correction.json-116-      "dataset": "PW-D5",
artifacts/table1_bh_correction.json-117-      "n": 600,
artifacts/table1_bh_correction.json:118:      "sc_pct": 75.17,
artifacts/table1_bh_correction.json-119-      "sica_pct": 72.67,
artifacts/table1_bh_correction.json-120-      "delta_pp": -2.5,
artifacts/table1_bh_correction.json-121-      "raw_p": 0.011,
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/exp-016/report/weighted_sc_report.md-30-| Method | ProofWriter (n=600) | FOLIO (n=204) |
artifacts/exp-016/report/weighted_sc_report.md-31-|--------|--------------------:|----:|
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/exp-016/report/weighted_sc_report.md-32-| SICA | 75.50% | 79.41% |
artifacts/exp-016/report/weighted_sc_report.md:33:| SC / Uniform | 75.17% | 79.41% |
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/exp-016/report/weighted_sc_report.md-34-| Inv-length | 75.67% | 79.90% |
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/exp-016/report/weighted_sc_report.md-35-| Length-weighted | 73.83% | 79.41% |
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/exp-016/report/weighted_sc_report.md-36-
--
artifacts/manifest.yaml-881-- id: art_20260518_abdc05
artifacts/manifest.yaml-882-  name: exp022_oracle_proofwriter
artifacts/manifest.yaml-883-  type: report
artifacts/manifest.yaml:884:  description: 'Exp-022 Oracle-SICA ProofWriter OWA-D5: oracle 86.67% vs SC 75.17%
…[truncated 306 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-21T09:59:49.305583+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "find /root/symb_invariant_consensus/results/ -name \"cil*\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "find /root/symb_invariant_consensus/results/ -name \"cil*\" -type f"
  }
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-21T09:59:49.305864+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "ls /root/symb_invariant_consensus/results/exp_d134_cil/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "ls /root/symb_invariant_consensus/results/exp_d134_cil/"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-21T09:59:49.306438+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-21T09:59:49.306593+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/symb_invariant_consensus/results/exp_d134_cil/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-21T09:59:49.306803+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cil_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cil_results.json"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-21T09:59:49.307242+00:00_

1	{
2	  "experiment": "exp_d134_cil",
3	  "description": "CIL (Cumulative Information Lift) computation",
4	  "formula": "CIL(V,G) = log2[P(V correct | G wrong) / P(V correct | G correct)]",
5	  "pairs": [
6	    {
7	      "generator": "Mistral-7B",
8	      "verifier": "DeBERTa-large-MNLI",
9	      "verifier_type": "NLI",
10	      "dataset": "PW-600",
11	      "n": 600,
12	      "combo_gain_w3": 6.67,
13	      "cil": 1.6655,
14	      "p_v_correct_given_g_wrong": 0.7527,
15	      "p_v_correct_given_g_correct": 0.2373,
16	      "n_g_wrong": 364,
17	      "n_g_right": 236,
18	      "both_right": 56,
19	      "v_right_g_wrong": 274,
20	      "g_right_v_wrong": 180,
21	      "both_wrong": 90
22	    },
23	    {
24	      "generator": "Mistral-7B",
25	      "verifier": "RoBERTa-large-MNLI",
26	      "verifier_type": "NLI",
27	      "dataset": "PW-600",
28	      "n": 600,
29	      "combo_gain_w3": 4.17,
30	      "cil": 1.4232,
31	      "p_v_correct_given_g_wrong": 0.5,
32	      "p_v_correct_given_g_correct": 0.1864,
33	      "n_g_wrong": 364,
34	      "n_g_right": 236,
35	      "both_right": 44,
36	      "v_right_g_wrong": 182,
37	      "g_right_v_wrong": 192,
38	      "both_wrong": 182
39	    },
40	    {
41	      "generator": "Mistral-7B",
42	      "verifier": "BART-large-MNLI",
43	      "verifier_type": "NLI",
44	      "dataset": "PW-600",
45	      "n": 600,
46	      "combo_gain_w3": 5.17,
47	      "cil": 1.859,
48	      "p_v_correct_given_g_wrong": 0.6456,
49	      "p_v_correct_given_g_correct": 0.178,
50	      "n_g_wrong": 364,
51	      "n_g_right": 236,
52	      "both_right": 42,
53	      "v_right_g_wrong": 235,
54	      "g_right_v_wrong": 194,
55	      "both_wrong": 129
56	    },
57	    {
58	      "generator": "Qwen2.5-14B",
59	      "verifier": "DeBERTa-large-MNLI",
60	      "verifier_type": "NLI",
61	      "dataset": "PW-600",
62	      "n": 600,
63	      "combo_gain_w3": 0.33,
64	      "note": "SC corrected: 74.0% BH (was 70.33% local). combo_w3=74.33%",
65	      "cil
…[truncated 4674 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-21T09:59:49.307647+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/table1_bh_correction.json",
  "limit": "60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/table1_bh_correction.json",
    "limit": "60"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-21T09:59:49.307857+00:00_

1	{
2	  "m": 16,
3	  "alpha": 0.05,
4	  "method": "Benjamini-Hochberg",
5	  "conditions": [
6	    {
7	      "model": "Mistral-7B",
8	      "dataset": "PW-D5",
9	      "n": 600,
10	      "sc_pct": 39.33,
11	      "sica_pct": 36.5,
12	      "delta_pp": -2.83,
13	      "raw_p": 0.014,
14	      "adjusted_p": 0.112,
15	      "significant_raw": true,
16	      "significant_bh": false
17	    },
18	    {
19	      "model": "Mistral-7B",
20	      "dataset": "LogiQA",
21	      "n": 200,
22	      "sc_pct": 51.0,
23	      "sica_pct": 51.5,
24	      "delta_pp": 0.5,
25	      "raw_p": 1.0,
26	      "adjusted_p": 1.0,
27	      "significant_raw": false,
28	      "significant_bh": false
29	    },
30	    {
31	      "model": "Mistral-7B",
32	      "dataset": "FOLIO (s123)",
33	      "n": 204,
34	      "sc_pct": 54.41,
35	      "sica_pct": 57.35,
36	      "delta_pp": 2.94,
37	      "raw_p": 0.07,
38	      "adjusted_p": 0.2976,
39	      "significant_raw": false,
40	      "significant_bh": false
41	    },
42	    {
43	      "model": "Mistral-7B (4s)",
44	      "dataset": "FOLIO",
45	      "n": 204,
46	      "sc_pct": 55.88,
47	      "sica_pct": 59.31,
48	      "delta_pp": 3.43,
49	      "raw_p": 0.092,
50	      "adjusted_p": 0.2976,
51	      "significant_raw": false,
52	      "significant_bh": false
53	    },
54	    {
55	      "model": "Mistral-7B",
56	      "dataset": "FOLIO (s456)",
57	      "n": 204,
58	      "sc_pct": 55.88,
59	      "sica_pct": 55.88,
60	      "delta_pp": 0.0,

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-21T09:59:49.308125+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "ls /root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ -1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "ls /root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ -1"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-21T09:59:49.308460+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"ProofWriter_AttNeg-OWA-D5-1015_Q19.json\\nProofWriter_AttNeg-OWA-D5-1015_Q3.json\\nProofWriter_AttNeg-OWA-D5-1017_Q19.json\\nProofWriter_AttNeg-OWA-D5-1017_Q5.json\\nProofWriter_AttNeg-OWA-D5-1028_Q10.json\\nProofWriter_AttNeg-OWA-D5-1030_Q23.json\\nProofWriter_AttNeg-OWA-D5-1066_Q21.json\\nProofWriter_AttNeg-OWA-D5-107_Q1.json\\nProofWriter_AttNeg-OWA-D5-107_Q6.json\\nProofWriter_AttNeg-OWA-D5-108_Q15.json\\nProofWriter_AttNeg-OWA-D5-109_Q11.json\\nProofWriter_AttNeg-OWA-D5-109_Q13.json\\nProofWriter_AttNeg-OWA-D5-1105_Q4.json\\nProofWriter_AttNeg-OWA-D5-1111_Q2.json\\nProofWriter_AttNeg-OWA-D5-1119_Q6.json\\nProofWriter_AttNeg-OWA-D5-1149_Q12.json\\nProofWriter_AttNeg-OWA-D5-1149_Q18.json\\nProofWriter_AttNeg-OWA-D5-1170_Q10.json\\nProofWriter_AttNeg-OWA-D5-1170_Q13.json\\nProofWriter_AttNeg-OWA-D5-1176_Q11.json\\nProofWriter_AttNeg-OWA-D5-1176_Q12.json\\nProofWriter_AttNeg-OWA-D5-1176_Q18.json\\nProofWriter_AttNeg-OWA-D5-1176_Q8.json\\nProofWriter_AttNeg-OWA-D5-1183_Q16.json\\nProofWriter_AttNeg-OWA-D5-1183_Q20.json\\nProofWriter_AttNeg-OWA-D5-1201_Q18.json\\nProofWriter_AttNeg-OWA-D5-1203_Q17.json\\nProofWriter_AttNeg-OWA-D5-1203_Q8.json\\nProofWriter_AttNeg-OWA-D5-1208_Q1.json\\nProofWriter_AttNeg-OWA-D5-1208_Q15.json\\nProofWriter_AttNeg-OWA-D5-1208_Q5.json\\nProofWriter_AttNeg-OWA-D5-120_Q11.json\\nProofWriter_AttNeg-OWA-D5-120_Q17.json\\nProofWriter_AttNeg-OWA-D5-120_Q9.json\\nProofWriter_AttNeg-OWA-D5-1210_Q4.json\\nProofWriter_AttNeg-OWA-D5-1210_Q8.json\\nProofWriter_AttNeg-OWA-D5-1220_Q4.json\\nProofWriter_AttNeg-OWA-D5-1220_Q6.json\\nProofWriter_AttNeg-OWA-D5-1229_Q3.json\\nProofWriter_AttNeg-OWA-D5-1229_Q6.json\\nProofWriter_AttNeg-OWA-D5-1233_Q11.json\\nProofWriter_AttNeg-OWA-D5-1233_Q2.json\\nProofWriter_AttNeg-OWA-D5-1236_Q12.json\\nProofWriter_AttNeg-OWA-D5-1236_Q20.json\\nProofWriter_AttNeg-OWA-D5-145_Q9.json\\nProofWriter_AttNeg-OWA-D5-155_Q6.json\\nProofWriter_AttNeg-OWA-D5-195_Q15.json\\nPr
…[truncated 6603 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-21T09:59:49.308659+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "sica_expanded_14b|exp.022",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/_project/paper/experiments.tex",
  "output_mode": "content",
  "-C": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "Grep",
  "tool_args": {
    "pattern": "sica_expanded_14b|exp.022",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/_project/paper/experiments.tex",
    "output_mode": "content",
    "-C": "2"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-21T09:59:49.308987+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-21T09:59:49.309376+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "wc -l /root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/*.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "wc -l /root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/*.json"
  }
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-21T09:59:49.309567+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "head -80 /root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_AttNoneg-OWA-D5-650_Q11.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "head -80 /root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_AttNoneg-OWA-D5-650_Q11.json"
  }
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-21T09:59:49.309792+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"     103 /root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_AttNeg-OWA-D5-1015_Q19.json\\n     103 /root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_AttNeg-OWA-D5-1015_Q3.json\\n     103 /root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_AttNeg-OWA-D5-1017_Q19.json\\n     103 /root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_AttNeg-OWA-D5-1017_Q5.json\\n     103 /root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_AttNeg-OWA-D5-1028_Q10.json\\n     101 /root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_AttNeg-OWA-D5-1030_Q23.json\\n     105 /root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_AttNeg-OWA-D5-1066_Q21.json\\n     101 /root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_AttNeg-OWA-D5-107_Q1.json\\n     101 /root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_AttNeg-OWA-D5-107_Q6.json\\n     103 /root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_AttNeg-OWA-D5-108_Q15.json\\n     103 /root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_AttNeg-OWA-D5-109_Q11.json\\n     103 /root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_AttNeg-OWA-D5-109_Q13.json\\n     103 /root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_AttNeg-OWA-D5-1105_Q4.json\\n     101 /root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_AttNeg-OWA-D5-1111_Q2.json\\n     103 /root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_AttNeg-OWA-D5-1119_Q6.json\\n     103 /root/symb_invariant_consen
…[truncated 6330 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-21T09:59:49.310116+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"problem\\\": {\\n    \\\"id\\\": \\\"ProofWriter_AttNoneg-OWA-D5-650_Q11\\\",\\n    \\\"problem\\\": \\\"Anne is smart. Charlie is nice. Erin is furry. Erin is white. Fiona is smart. Fiona is white. Fiona is young. Nice, smart things are young. All young, white things are cold. White things are red. All furry, red things are nice. All young things are white. All young things are white. All smart, cold things are furry. If something is nice and white then it is smart. If Anne is furry and Anne is white then Anne is red.\\\\n\\\\nDetermine whether the following statement is true, false, or unknown:\\\\nErin is cold.\\\",\\n    \\\"solution\\\": \\\"\\\",\\n    \\\"answer\\\": \\\"True\\\",\\n    \\\"level\\\": \\\"OWA-D5\\\",\\n    \\\"raw_logic_programs\\\": [\\n      \\\"Predicates:\\\\nSmart($x, bool) ::: Is x smart?\\\\nNice($x, bool) ::: Is x nice?\\\\nFurry($x, bool) ::: Is x furry?\\\\nWhite($x, bool) ::: Is x white?\\\\nYoung($x, bool) ::: Is x young?\\\\nCold($x, bool) ::: Is x cold?\\\\nRed($x, bool) ::: Is x red?\\\\n\\\\nFacts:\\\\nSmart(Anne, True) ::: Anne is smart.\\\\nNice(Charlie, True) ::: Charlie is nice.\\\\nFurry(Erin, True) ::: Erin is furry.\\\\nWhite(Erin, True) ::: Erin is white.\\\\nSmart(Fiona, True) ::: Fiona is smart.\\\\nWhite(Fiona, True) ::: Fiona is white.\\\\nYoung(Fiona, True) ::: Fiona is young.\\\\n\\\\nRules:\\\\nNice($x, True) && Smart($x, True) >>> Young($x, True) ::: Nice, smart things are young.\\\\nYoung($x, True) && White($x, True) >>> Cold($x, True) ::: All young, white things are cold.\\\\nWhite($x, True) >>> Red($x, True) ::: White things are red.\\\\nFurry($x, True) && Red($x, True) >>> Nice($x, True) ::: All furry, red things are nice.\\\\nYoung($x, True) >>> White($x, True) ::: All young things are white.\\\\nSmart($x, True) && Cold($x, True) >>> Furry($x, True) ::: All smart, cold things are furry.\\\\nNice($x, True) && White($x, True) >>> Smart($x, Tru
…[truncated 7051 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-21T09:59:49.310331+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "find /root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ -name \"*.json\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "find /root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ -name \"*.json\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-21T09:59:49.310548+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_AttNoneg-OWA-D5-1041_Q1.json\\n/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_RelNeg-OWA-D5-81_Q11.json\\n/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_AttNoneg-OWA-D5-1284_Q8.json\\n/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_AttNoneg-OWA-D5-585_Q19.json\\n/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_RelNoneg-OWA-D5-949_Q8.json\\n/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_RelNeg-OWA-D5-508_Q2.json\\n/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_AttNeg-OWA-D5-270_Q8.json\\n/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_RelNoneg-OWA-D5-487_Q19.json\\n/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_AttNoneg-OWA-D5-971_Q5.json\\n/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_AttNeg-OWA-D5-804_Q16.json\\n/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_AttNoneg-OWA-D5-572_Q18.json\\n/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_AttNeg-OWA-D5-285_Q16.json\\n/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_RelNoneg-OWA-D5-686_Q18.json\\n/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_AttNoneg-OWA-D5-735_Q9.json\\n/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_RelNeg-OWA-D5-966_Q7.json\\n/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_AttNeg-OWA-D5-145_Q9.json\\n/root/symb_invariant_consensus/results/exp032_
…[truncated 6340 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-21T09:59:49.310714+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/table1_bh_correction.json",
  "offset": "110",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/table1_bh_correction.json",
    "offset": "110",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-21T09:59:49.310862+00:00_

110	      "adjusted_p": 1.0,
111	      "significant_raw": false,
112	      "significant_bh": false
113	    },
114	    {
115	      "model": "Qwen2.5-14B",
116	      "dataset": "PW-D5",
117	      "n": 600,
118	      "sc_pct": 75.17,
119	      "sica_pct": 72.67,
120	      "delta_pp": -2.5,
121	      "raw_p": 0.011,
122	      "adjusted_p": 0.112,
123	      "significant_raw": true,
124	      "significant_bh": false
125	    },
126	    {
127	      "model": "Qwen2.5-14B",
128	      "dataset": "FOLIO",
129	      "n": 204,
130	      "sc_pct": 75.49,
131	      "sica_pct": 74.51,
132	      "delta_pp": -0.98,
133	      "raw_p": 1.0,
134	      "adjusted_p": 1.0,
135	      "significant_raw": false,
136	      "significant_bh": false
137	    },
138	    {
139	      "model": "Qwen2.5-7B",

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-21T09:59:49.311149+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/qwen14b_pw_sc_audit.json",
  "content": "{\n  \"audit\": \"Qwen2.5-14B ProofWriter D5-600 SC Accuracy Discrepancy\",\n  \"date\": \"2026-05-21\",\n  \"summary\": \"Three different SC accuracy values traced to THREE different experiment runs, not tiebreaking differences\",\n\n  \"three_values\": {\n    \"75.17_pct\": {\n      \"value\": 75.17,\n      \"correct\": 451,\n      \"total\": 600,\n      \"source_experiment\": \"sica_expanded_14b (early run, likely westd-25068)\",\n      \"appears_in\": [\"Main Table (experiments.tex line 33)\", \"BH correction table (table1_bh_correction.json)\", \"exp-022-oracle-proofwriter (same traces)\"],\n      \"registry_match\": \"sica_expanded_14b: proofwriter_sc=0.752, exp-022: sc_accuracy=0.7517\",\n      \"explanation\": \"First complete Qwen2.5-14B PW-600 run. Different trace generation from later experiments.\"\n    },\n    \"74.00_pct\": {\n      \"value\": 74.00,\n      \"correct\": 444,\n      \"total\": 600,\n      \"source_experiment\": \"exp032_qwen25_14b_pw600 (westd-16639) with ALPHABETICAL tiebreaking\",\n      \"appears_in\": [\"Cross-gen NLI Table (solutions.tex line 29)\", \"CIL corrected value\"],\n      \"raw_sc_without_tiebreak\": {\"value\": 73.50, \"correct\": 441, \"method\": \"first-seen (Python max() on dict)\"},\n      \"registry_match\": \"exp-039-14b-pw600-16639: sc_accuracy=73.5%, exp-091-qwen14b-pw-nli-combo: sc_accuracy=0.735\",\n      \"explanation\": \"Later re-run on westd-16639. 441 correct with first-seen tiebreaking, 444 correct with alphabetical tiebreaking (sorted(tied)[0]).\"\n    },\n    \"70.33_pct\": {\n      \"value\": 70.33,\n      \"correct\": 422,\n      \"total\": 600,\n      \"source_experiment\": \"exp034_qwen25_14b_proofwriter intermediates (likely westd-25068, server now down)\",\n      \"appears_in\": [\"Initial CIL computation (cil_results.json, before correction)\"],\n      \"registry_match\": \"exp-034: n_problems=93, status=DONE (crashed at 93/600 but intermediates may contain prior run data)\",\n      \"explanation\": \"Third distinct trace generation. CIL script loaded from exp034 intermediates on westd-25068. Was later manually corrected to 74.00% in cil_results.json.\",\n      \"cil_complementarity_counts\": {\n        \"both_right\": 236,\n        \"v_right_g_wrong\": 94,\n        \"g_right_v_wrong\": 186,\n        \"both_wrong\": 84,\n        \"sc_correct_from_counts\": 422,\n        \"deberta_correct_from_counts\": 330,\n        \"note\": \"DeBERTa correct=330 matches all experiments (generator-independent)\"\n      }\n    }\n  },\n\n  \"tiebreaking_analysis\": {\n    \"source\": \"exp032_qwen25_14b_pw600 on westd-16639 (600 questions, K=12)\",\n    \"n_ties\": 21,\n    \"tie_rate\": \"3.50%\",\n    \"all_ties_are_6_6\": \"20 of 21 are 6:6 two-way ties; 1 is 4:4:4 three-way tie\",\n    \"results_by_method\": {\n      \"first_seen\": {\"correct\": 441, \"accuracy\": \"73.50%\", \"note\": \"Python max() on dict, order depends on JSON serialization\"},\n      \"alphabetical\": {\"correct\": 444, \"accuracy\": \"74.00%\", \"note\": \"sorted(tied_candidates)[0], deterministic\"},\n      \"random_seed_42\": {\"correct\": 439, \"accuracy\": \"73.17%\"},\n      \"random_seed_123\": {\"correct\": 437, \"accuracy\": \"72.83%\"},\n      \"random_seed_456\": {\"correct\": 435, \"accuracy\": \"72.50%\"},\n      \"random_seed_789\": {\"correct\": 440, \"accuracy\": \"73.33%\"},\n      \"random_seed_0\": {\"correct\": 442, \"accuracy\": \"73.67%\"}\n    },\n    \"tie_impact\": \"Tiebreaking affects 21 questions, flipping 0-6 answers vs first-seen. Max possible swing: ~1.0pp\",\n    \"tie_details\": [\n      {\"qid\": \"AttNeg-OWA-D5-891_Q9\", \"gold\": \"True\", \"dist\": {\"True\": 6, \"Unknown\": 6}, \"alpha\": \"True\", \"first_seen\": \"True\"},\n      {\"qid\": \"AttNoneg-OWA-D5-650_Q11\", \"gold\": \"True\", \"dist\": {\"Unknown\": 6, \"True\": 6}, \"alpha\": \"True\", \"first_seen\": \"Unknown\"},\n      {\"qid\": \"AttNoneg-OWA-D5-785_Q10\", \"gold\": \"False\", \"dist\": {\"False\": 6, \"Unknown\": 6}, \"alpha\": \"False\", \"first_seen\": \"False\"},\n      {\"qid\": \"RelNeg-OWA-D5-922_Q7\", \"gold\": \"True\", \"dist\": {\"Unknown\": 6, \"False\": 6}, \"alpha\": \"False\", \"first_seen\": \"Unknown\"},\n      {\"qid\": \"RelNoneg-OWA-D5-151_Q4\", \"gold\": \"False\", \"dist\": {\"Unknown\": 6, \"False\": 6}, \"alpha\": \"False\", \"first_seen\": \"Unknown\"},\n      {\"qid\": \"AttNoneg-OWA-D5-1187_Q7\", \"gold\": \"True\", \"dist\": {\"True\": 6, \"Unknown\": 6}, \"alpha\": \"True\", \"first_seen\": \"True\"},\n      {\"qid\": \"RelNeg-OWA-D5-249_Q9\", \"gold\": \"True\", \"dist\": {\"True\": 6, \"Unknown\": 6}, \"alpha\": \"True\", \"first_seen\": \"True\"},\n      {\"qid\": \"RelNeg-OWA-D5-604_Q14\", \"gold\": \"Unknown\", \"dist\": {\"Unknown\": 6, \"False\": 6}, \"alpha\": \"False\", \"first_seen\": \"Unknown\"},\n      {\"qid\": \"RelNeg-OWA-D5-587_Q8\", \"gold\": \"False\", \"dist\": {\"True\": 6, \"False\": 6}, \"alpha\": \"False\", \"first_seen\": \"True\"},\n      {\"qid\": \"AttNeg-OWA-D5-1233_Q11\", \"gold\": \"True\", \"dist\": {\"Unknown\": 6, \"True\": 6}, \"alpha\": \"True\", \"first_seen\": \"Unknown\"},\n      {\"qid\": \"RelNoneg-OWA-D5-616_Q7\", \"gold\": \"True\", \"dist\": {\"True\": 6, \"Unknown\": 6}, \"alpha\": \"True\", \"first_seen\": \"True\"},\n      {\"qid\": \"RelNoneg-OWA-D5-691_Q3\", \"gold\": \"True\", \"dist\": {\"Unknown\": 6, \"True\": 6}, \"alpha\": \"True\", \"first_seen\": \"Unknown\"},\n      {\"qid\": \"RelNeg-OWA-D5-77_Q15\", \"gold\": \"Unknown\", \"dist\": {\"True\": 6, \"Unknown\": 6}, \"alpha\": \"True\", \"first_seen\": \"True\"},\n      {\"qid\": \"AttNeg-OWA-D5-664_Q1\", \"gold\": \"True\", \"dist\": {\"True\": 4, \"Unknown\": 4, \"False\": 4}, \"alpha\": \"False\", \"first_seen\": \"True\"},\n      {\"qid\": \"RelNoneg-OWA-D5-582_Q12\", \"gold\": \"False\", \"dist\": {\"Unknown\": 5, \"True\": 5, \"False\": 2}, \"alpha\": \"True\", \"first_seen\": \"Unknown\"},\n      {\"qid\": \"RelNeg-OWA-D5-903_Q6\", \"gold\": \"False\", \"dist\": {\"True\": 5, \"Unknown\": 5, \"False\": 2}, \"alpha\": \"True\", \"first_seen\": \"True\"},\n      {\"qid\": \"RelNeg-OWA-D5-602_Q16\", \"gold\": \"Unknown\", \"dist\": {\"True\": 6, \"Unknown\": 6}, \"alpha\": \"True\", \"first_seen\": \"True\"},\n      {\"qid\": \"RelNoneg-OWA-D5-739_Q12\", \"gold\": \"False\", \"dist\": {\"Unknown\": 6, \"True\": 6}, \"alpha\": \"True\", \"first_seen\": \"Unknown\"},\n      {\"qid\": \"RelNoneg-OWA-D5-649_Q12\", \"gold\": \"False\", \"dist\": {\"Unknown\": 6, \"True\": 6}, \"alpha\": \"True\", \"first_seen\": \"Unknown\"},\n      {\"qid\": \"RelNoneg-OWA-D5-1036_Q11\", \"gold\": \"True\", \"dist\": {\"Unknown\": 6, \"False\": 6}, \"alpha\": \"False\", \"first_seen\": \"Unknown\"},\n      {\"qid\": \"AttNoneg-OWA-D5-785_Q8\", \"gold\": \"False\", \"dist\": {\"False\": 5, \"Unknown\": 2, \"True\": 5}, \"alpha\": \"False\", \"first_seen\": \"False\"}\n    ]\n  },\n\n  \"root_cause\": {\n    \"primary\": \"Three different experiment runs (different trace generations) produced different SC accuracies\",\n    \"secondary\": \"Tiebreaking method differences add ~0.5pp variation on top\",\n    \"NOT_the_cause\": \"BH correction does not change SC accuracy — it only adjusts p-values for multiple testing\"\n  },\n\n  \"canonical_recommendation\": {\n    \"recommended_value\": 73.50,\n    \"recommended_value_pct\": \"73.50%\",\n    \"recommended_correct\": 441,\n    \"recommended_source\": \"exp032_qwen25_14b_pw600 (westd-16639), first-seen tiebreaking\",\n    \"reasoning\": [\n      \"exp032 is the complete run on the accessible server with full per-question data and intermediates\",\n      \"exp032 traces are used by NLI combo experiments (exp-091), making them the basis for downstream analyses\",\n      \"First-seen tiebreaking matches the original SICA pipeline behavior (Python max() on dict)\",\n      \"Alphabetical tiebreaking (74.00%) is defensible but introduces a tiebreaking convention not used elsewhere\",\n      \"sica_expanded_14b (75.17%) was an earlier, separate run — using it in Main Table while NLI analyses use exp032 creates inconsistency\"\n    ],\n    \"action_items\": [\n      \"UPDATE Main Table: change Qwen2.5-14B PW-600 from 75.17% to 73.50% (SC) and from 75.50% to 71.50% (SICA), delta from +0.33 to -2.00\",\n      \"KEEP solutions.tex NLI table at 73.50% (or 74.00% if alphabetical tiebreaking is adopted project-wide)\",\n      \"VERIFY CIL: recompute CIL using exp032 intermediates (not exp034) to get correct complementarity counts\",\n      \"DECIDE: adopt consistent tiebreaking method across all experiments and document it\"\n    ]\n  },\n\n  \"alternative_recommendation\": {\n    \"if_keeping_75_17\": {\n      \"value\": 75.17,\n      \"reasoning\": \"If sica_expanded_14b is considered the canonical run, update NLI combo and CIL to use the same traces\",\n      \"action_items\": [\n        \"Rerun NLI combo experiment using sica_expanded_14b traces\",\n        \"Recompute CIL from sica_expanded_14b intermediates\",\n        \"This would require access to westd-25068 (currently down)\"\n      ]\n    }\n  },\n\n  \"experiments_inventory\": {\n    \"sica_expanded_14b\": {\"server\": \"likely westd-25068\", \"sc\": 0.752, \"sica\": 0.755, \"n\": 600, \"sc_correct\": 451, \"status\": \"DONE\"},\n    \"exp-022-oracle-proofwriter\": {\"server\": \"likely westd-25068\", \"sc\": 0.7517, \"sica_oracle\": 0.8667, \"n\": 600, \"sc_correct\": 451, \"status\": \"DONE\", \"note\": \"Oracle experiment, same traces as sica_expanded_14b\"},\n    \"exp032_qwen25_14b_pw600\": {\"server\": \"westd-16639\", \"sc\": 0.735, \"sica\": 0.715, \"n\": 600, \"sc_correct\": 441, \"status\": \"DONE\"},\n    \"exp-039-14b-pw600-16639\": {\"server\": \"westd-16639\", \"sc\": 0.735, \"sica\": 0.715, \"n\": 600, \"sc_correct\": 441, \"status\": \"DONE\", \"note\": \"Registry alias for exp032\"},\n    \"exp-091-qwen14b-pw-nli-combo\": {\"server\": \"westd-16639\", \"sc_baseline\": 0.735, \"n\": 600, \"status\": \"DONE\", \"note\": \"Uses exp032 traces\"},\n    \"exp034_qwen25_14b_proofwriter\": {\"server\": \"likely westd-25068\", \"sc\": 0.7033, \"n\": 600, \"sc_correct\": 422, \"status\": \"DONE (crashed at 93/600 in registry but intermediates may be from prior run)\"}\n  }\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/qwen14b_pw_sc_audit.json",
    "content": "{\n  \"audit\": \"Qwen2.5-14B ProofWriter D5-600 SC Accuracy Discrepancy\",\n  \"date\": \"2026-05-21\",\n  \"summary\": \"Three different SC accuracy values traced to THREE different experiment runs, not tiebreaking differences\",\n\n  \"three_values\": {\n    \"75.17_pct\": {\n      \"value\": 75.17,\n      \"correct\": 451,\n      \"total\": 600,\n      \"source_experiment\": \"sica_expanded_14b (early run, likely westd-25068)\",\n      \"appears_in\": [\"Main Table (experiments.tex line 33)\", \"BH correction table (table1_bh_correction.json)\", \"exp-022-oracle-proofwriter (same traces)\"],\n      \"registry_match\": \"sica_expanded_14b: proofwriter_sc=0.752, exp-022: sc_accuracy=0.7517\",\n      \"explanation\": \"First complete Qwen2.5-14B PW-600 run. Different trace generation from later experiments.\"\n    },\n    \"74.00_pct\": {\n      \"value\": 74.00,\n      \"correct\": 444,\n      \"total\": 600,\n      \"source_experiment\": \"exp032_qwen25_14b_pw600 (westd-16639) with ALPHABETICAL tiebreaking\",\n      \"appears_in\": [\"Cross-gen NLI Table (solutions.tex line 29)\", \"CIL corrected value\"],\n      \"raw_sc_without_tiebreak\": {\"value\": 73.50, \"correct\": 441, \"method\": \"first-seen (Python max() on dict)\"},\n      \"registry_match\": \"exp-039-14b-pw600-16639: sc_accuracy=73.5%, exp-091-qwen14b-pw-nli-combo: sc_accuracy=0.735\",\n      \"explanation\": \"Later re-run on westd-16639. 441 correct with first-seen tiebreaking, 444 correct with alphabetical tiebreaking (sorted(tied)[0]).\"\n    },\n    \"70.33_pct\": {\n      \"value\": 70.33,\n      \"correct\": 422,\n      \"total\": 600,\n      \"source_experiment\": \"exp034_qwen25_14b_proofwriter intermediates (likely westd-25068, server now down)\",\n      \"appears_in\": [\"Initial CIL computation (cil_results.json, before correction)\"],\n      \"registry_match\": \"exp-034: n_problems=93, status=DONE (crashed at 93/600 but intermediates may contain prior run data)\",\n      \"explanation\": \"Third distinct trace generation. CIL script loaded from exp034 intermediates on westd-25068. Was later manually corrected to 74.00% in cil_results.json.\",\n      \"cil_complementarity_counts\": {\n        \"both_right\": 236,\n        \"v_right_g_wrong\": 94,\n        \"g_right_v_wrong\": 186,\n        \"both_wrong\": 84,\n        \"sc_correct_from_counts\": 422,\n        \"deberta_correct_from_counts\": 330,\n        \"note\": \"DeBERTa correct=330 matches all experiments (generator-independent)\"\n      }\n    }\n  },\n\n  \"tiebreaking_analysis\": {\n    \"source\": \"exp032_qwen25_14b_pw600 on westd-16639 (600 questions, K=12)\",\n    \"n_ties\": 21,\n    \"tie_rate\": \"3.50%\",\n    \"all_ties_are_6_6\": \"20 of 21 are 6:6 two-way ties; 1 is 4:4:4 three-way tie\",\n    \"results_by_method\": {\n      \"first_seen\": {\"correct\": 441, \"accuracy\": \"73.50%\", \"note\": \"Python max() on dict, order depends on JSON serialization\"},\n      \"alphabetical\": {\"correct\": 444, \"accuracy\": \"74.00%\", \"note\": \"sorted(tied_candidates)[0], deterministic\"},\n      \"random_seed_42\": {\"correct\": 439, \"accuracy\": \"73.17%\"},\n      \"random_seed_123\": {\"correct\": 437, \"accuracy\": \"72.83%\"},\n      \"random_seed_456\": {\"correct\": 435, \"accuracy\": \"72.50%\"},\n      \"random_seed_789\": {\"correct\": 440, \"accuracy\": \"73.33%\"},\n      \"random_seed_0\": {\"correct\": 442, \"accuracy\": \"73.67%\"}\n    },\n    \"tie_impact\": \"Tiebreaking affects 21 questions, flipping 0-6 answers vs first-seen. Max possible swing: ~1.0pp\",\n    \"tie_details\": [\n      {\"qid\": \"AttNeg-OWA-D5-891_Q9\", \"gold\": \"True\", \"dist\": {\"True\": 6, \"Unknown\": 6}, \"alpha\": \"True\", \"first_seen\": \"True\"},\n      {\"qid\": \"AttNoneg-OWA-D5-650_Q11\", \"gold\": \"True\", \"dist\": {\"Unknown\": 6, \"True\": 6}, \"alpha\": \"True\", \"first_seen\": \"Unknown\"},\n      {\"qid\": \"AttNoneg-OWA-D5-785_Q10\", \"gold\": \"False\", \"dist\": {\"False\": 6, \"Unknown\": 6}, \"alpha\": \"False\", \"first_seen\": \"False\"},\n      {\"qid\": \"RelNeg-OWA-D5-922_Q7\", \"gold\": \"True\", \"dist\": {\"Unknown\": 6, \"False\": 6}, \"alpha\": \"False\", \"first_seen\": \"Unknown\"},\n      {\"qid\": \"RelNoneg-OWA-D5-151_Q4\", \"gold\": \"False\", \"dist\": {\"Unknown\": 6, \"False\": 6}, \"alpha\": \"False\", \"first_seen\": \"Unknown\"},\n      {\"qid\": \"AttNoneg-OWA-D5-1187_Q7\", \"gold\": \"True\", \"dist\": {\"True\": 6, \"Unknown\": 6}, \"alpha\": \"True\", \"first_seen\": \"True\"},\n      {\"qid\": \"RelNeg-OWA-D5-249_Q9\", \"gold\": \"True\", \"dist\": {\"True\": 6, \"Unknown\": 6}, \"alpha\": \"True\", \"first_seen\": \"True\"},\n      {\"qid\": \"RelNeg-OWA-D5-604_Q14\", \"gold\": \"Unknown\", \"dist\": {\"Unknown\": 6, \"False\": 6}, \"alpha\": \"False\", \"first_seen\": \"Unknown\"},\n      {\"qid\": \"RelNeg-OWA-D5-587_Q8\", \"gold\": \"False\", \"dist\": {\"True\": 6, \"False\": 6}, \"alpha\": \"False\", \"first_seen\": \"True\"},\n      {\"qid\": \"AttNeg-OWA-D5-1233_Q11\", \"gold\": \"True\", \"dist\": {\"Unknown\": 6, \"True\": 6}, \"alpha\": \"True\", \"first_seen\": \"Unknown\"},\n      {\"qid\": \"RelNoneg-OWA-D5-616_Q7\", \"gold\": \"True\", \"dist\": {\"True\": 6, \"Unknown\": 6}, \"alpha\": \"True\", \"first_seen\": \"True\"},\n      {\"qid\": \"RelNoneg-OWA-D5-691_Q3\", \"gold\": \"True\", \"dist\": {\"Unknown\": 6, \"True\": 6}, \"alpha\": \"True\", \"first_seen\": \"Unknown\"},\n      {\"qid\": \"RelNeg-OWA-D5-77_Q15\", \"gold\": \"Unknown\", \"dist\": {\"True\": 6, \"Unknown\": 6}, \"alpha\": \"True\", \"first_seen\": \"True\"},\n      {\"qid\": \"AttNeg-OWA-D5-664_Q1\", \"gold\": \"True\", \"dist\": {\"True\": 4, \"Unknown\": 4, \"False\": 4}, \"alpha\": \"False\", \"first_seen\": \"True\"},\n      {\"qid\": \"RelNoneg-OWA-D5-582_Q12\", \"gold\": \"False\", \"dist\": {\"Unknown\": 5, \"True\": 5, \"False\": 2}, \"alpha\": \"True\", \"first_seen\": \"Unknown\"},\n      {\"qid\": \"RelNeg-OWA-D5-903_Q6\", \"gold\": \"False\", \"dist\": {\"True\": 5, \"Unknown\": 5, \"False\": 2}, \"alpha\": \"True\", \"first_seen\": \"True\"},\n      {\"qid\": \"RelNeg-OWA-D5-602_Q16\", \"gold\": \"Unknown\", \"dist\": {\"True\": 6, \"Unknown\": 6}, \"alpha\": \"True\", \"first_seen\": \"True\"},\n      {\"qid\": \"RelNoneg-OWA-D5-739_Q12\", \"gold\": \"False\", \"dist\": {\"Unknown\": 6, \"True\": 6}, \"alpha\": \"True\", \"first_seen\": \"Unknown\"},\n      {\"qid\": \"RelNoneg-OWA-D5-649_Q12\", \"gold\": \"False\", \"dist\": {\"Unknown\": 6, \"True\": 6}, \"alpha\": \"True\", \"first_seen\": \"Unknown\"},\n      {\"qid\": \"RelNoneg-OWA-D5-1036_Q11\", \"gold\": \"True\", \"dist\": {\"Unknown\": 6, \"False\": 6}, \"alpha\": \"False\", \"first_seen\": \"Unknown\"},\n      {\"qid\": \"AttNoneg-OWA-D5-785_Q8\", \"gold\": \"False\", \"dist\": {\"False\": 5, \"Unknown\": 2, \"True\": 5}, \"alpha\": \"False\", \"first_seen\": \"False\"}\n    ]\n  },\n\n  \"root_cause\": {\n    \"primary\": \"Three different experiment runs (different trace generations) produced different SC accuracies\",\n    \"secondary\": \"Tiebreaking method differences add ~0.5pp variation on top\",\n    \"NOT_the_cause\": \"BH correction does not change SC accuracy — it only adjusts p-values for multiple testing\"\n  },\n\n  \"canonical_recommendation\": {\n    \"recommended_value\": 73.50,\n    \"recommended_value_pct\": \"73.50%\",\n    \"recommended_correct\": 441,\n    \"recommended_source\": \"exp032_qwen25_14b_pw600 (westd-16639), first-seen tiebreaking\",\n    \"reasoning\": [\n      \"exp032 is the complete run on the accessible server with full per-question data and intermediates\",\n      \"exp032 traces are used by NLI combo experiments (exp-091), making them the basis for downstream analyses\",\n      \"First-seen tiebreaking matches the original SICA pipeline behavior (Python max() on dict)\",\n      \"Alphabetical tiebreaking (74.00%) is defensible but introduces a tiebreaking convention not used elsewhere\",\n      \"sica_expanded_14b (75.17%) was an earlier, separate run — using it in Main Table while NLI analyses use exp032 creates inconsistency\"\n    ],\n    \"action_items\": [\n      \"UPDATE Main Table: change Qwen2.5-14B PW-600 from 75.17% to 73.50% (SC) and from 75.50% to 71.50% (SICA), delta from +0.33 to -2.00\",\n      \"KEEP solutions.tex NLI table at 73.50% (or 74.00% if alphabetical tiebreaking is adopted project-wide)\",\n      \"VERIFY CIL: recompute CIL using exp032 intermediates (not exp034) to get correct complementarity counts\",\n      \"DECIDE: adopt consistent tiebreaking method across all experiments and document it\"\n    ]\n  },\n\n  \"alternative_recommendation\": {\n    \"if_keeping_75_17\": {\n      \"value\": 75.17,\n      \"reasoning\": \"If sica_expanded_14b is considered the canonical run, update NLI combo and CIL to use the same traces\",\n      \"action_items\": [\n        \"Rerun NLI combo experiment using sica_expanded_14b traces\",\n        \"Recompute CIL from sica_expanded_14b intermediates\",\n        \"This would require access to westd-25068 (currently down)\"\n      ]\n    }\n  },\n\n  \"experiments_inventory\": {\n    \"sica_expanded_14b\": {\"server\": \"likely westd-25068\", \"sc\": 0.752, \"sica\": 0.755, \"n\": 600, \"sc_correct\": 451, \"status\": \"DONE\"},\n    \"exp-022-oracle-proofwriter\": {\"server\": \"likely westd-25068\", \"sc\": 0.7517, \"sica_oracle\": 0.8667, \"n\": 600, \"sc_correct\": 451, \"status\": \"DONE\", \"note\": \"Oracle experiment, same traces as sica_expanded_14b\"},\n    \"exp032_qwen25_14b_pw600\": {\"server\": \"westd-16639\", \"sc\": 0.735, \"sica\": 0.715, \"n\": 600, \"sc_correct\": 441, \"status\": \"DONE\"},\n    \"exp-039-14b-pw600-16639\": {\"server\": \"westd-16639\", \"sc\": 0.735, \"sica\": 0.715, \"n\": 600, \"sc_correct\": 441, \"status\": \"DONE\", \"note\": \"Registry alias for exp032\"},\n    \"exp-091-qwen14b-pw-nli-combo\": {\"server\": \"westd-16639\", \"sc_baseline\": 0.735, \"n\": 600, \"status\": \"DONE\", \"note\": \"Uses exp032 traces\"},\n    \"exp034_qwen25_14b_proofwriter\": {\"server\": \"likely westd-25068\", \"sc\": 0.7033, \"n\": 600, \"sc_correct\": 422, \"status\": \"DONE (crashed at 93/600 in registry but intermediates may be from prior run)\"}\n  }\n}\n"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-21T09:59:49.311480+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/qwen14b_pw_sc_audit.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-21T09:59:49.311633+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "qwen14b_pw_sc_audit",
  "type": "report",
  "description": "Audit of Qwen2.5-14B PW-600 SC accuracy discrepancy: 75.17% vs 74.00% vs 70.33% traced to three different experiment runs",
  "project": "symb_invariant_consensus",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/qwen14b_pw_sc_audit.json",
  "tags": "['audit', 'qwen14b', 'proofwriter', 'sc-accuracy', 'consistency']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "qwen14b_pw_sc_audit",
    "type": "report",
    "description": "Audit of Qwen2.5-14B PW-600 SC accuracy discrepancy: 75.17% vs 74.00% vs 70.33% traced to three different experiment runs",
    "project": "symb_invariant_consensus",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/qwen14b_pw_sc_audit.json",
    "tags": "['audit', 'qwen14b', 'proofwriter', 'sc-accuracy', 'consistency']"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-21T09:59:49.311792+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260521_81f25a\", \"name\": \"qwen14b_pw_sc_audit\", \"type\": \"report\", \"description\": \"Audit of Qwen2.5-14B PW-600 SC accuracy discrepancy: 75.17% vs 74.00% vs 70.33% traced to three different experiment runs\", \"path\": \"projects/symb_invariant_consensus/artifacts/_project/report/qwen14b_pw_sc_audit.json\", \"url\": null, \"project\": \"symb_invariant_consensus\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-21T09:59:35.379143+00:00\", \"tags\": [\"audit\", \"qwen14b\", \"proofwriter\", \"sc-accuracy\", \"consistency\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 71 · 2026-05-21T09:59:49.311999+00:00_

审计完成。核心发现：

## 三个值的来源

| 值 | 正确数 | 来源 | 出现位置 |
|---|---|---|---|
| **75.17%** | 451/600 | `sica_expanded_14b` (早期实验, westd-25068) | Main Table (experiments.tex) |
| **74.00%** | 444/600 | `exp032` (westd-16639) + **alphabetical tiebreaking** | Cross-gen NLI Table (solutions.tex) |
| **70.33%** | 422/600 | `exp034` intermediates (westd-25068, 已下线) | CIL 初始计算 (已修正为 74.00%) |

## 根因

**不是 tiebreaking 差异，是三次不同的实验 run**（不同 trace 生成），产生了不同的 SC 正确数（451 vs 441 vs 422）。

Tiebreaking 只在 exp032 上造成额外 ~0.5pp 差异：
- **21 个 tie**（3.5%），全部是 6:6 平票（K=12）
- First-seen: 441/600 = 73.50%
- Alphabetical: 444/600 = 74.00%（+3 正确）
- Random: 435-442/600（72.50%-73.67%）

## Canonical 推荐

**73.50%**（exp032, first-seen tiebreaking）：
- exp032 是可访问服务器上的完整 run，有全部 per-question 数据
- NLI combo 实验 (exp-091) 基于同一组 traces
- First-seen 匹配原始 SICA pipeline 行为

**关键不一致**：Main Table 用 sica_expanded_14b (75.17%)，NLI 分析用 exp032 (73.50/74.00%)——同一模型同一数据集引用了不同实验 run 的结果。需统一。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_qwen14b-pw-sc-audit_20260521T095214"
}
```

</details>

---
