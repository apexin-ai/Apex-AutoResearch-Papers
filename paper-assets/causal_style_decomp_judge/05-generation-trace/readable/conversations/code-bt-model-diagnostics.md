# code bt model diagnostics

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 0
- **Tool calls:** 12
- **Original source:** `logs/chats/worker_code_bt_model_diagnostics_20260521T114335.jsonl`
- **Structured JSON:** [`5339c6ef10a41017d32e.json`](../../sessions/53/5339c6ef10a41017d32e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

25 recorded events

### Tool call

_source line 1 · 2026-05-21T11:49:13.639796+00:00_

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
  "session": "worker_code_bt_model_diagnostics_20260521T114335",
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

_source line 2 · 2026-05-21T11:49:13.640110+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_bt_model_diagnostics_20260521T114335",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T11:49:13.640267+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-29275",
  "command": "head -50 /root/causal_style_decomp_judge/data/pairwise_results_32b.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_bt_model_diagnostics_20260521T114335",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-29275",
    "command": "head -50 /root/causal_style_decomp_judge/data/pairwise_results_32b.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-21T11:49:13.640458+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-29275",
  "command": "head -50 /root/causal_style_decomp_judge/data/verified_32b.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_bt_model_diagnostics_20260521T114335",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-29275",
    "command": "head -50 /root/causal_style_decomp_judge/data/verified_32b.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T11:49:13.640589+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-29275",
  "command": "head -50 /root/causal_style_decomp_judge/data/pairwise_results_qwen32b_verbosity.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_bt_model_diagnostics_20260521T114335",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-29275",
    "command": "head -50 /root/causal_style_decomp_judge/data/pairwise_results_qwen32b_verbosity.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T11:49:13.640913+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"id\\\": \\\"mvp_0002\\\", \\\"instruction\\\": \\\"What happened on October 1, 2017 in Catalonia?\\\", \\\"original_formality\\\": \\\"formal\\\", \\\"nli_cf\\\": 0.9359870553016663, \\\"bertscore_cf\\\": 0.9339630603790283, \\\"trial1_choice\\\": \\\"A\\\", \\\"trial1_prefers_formal\\\": true, \\\"trial2_choice\\\": \\\"B\\\", \\\"trial2_prefers_formal\\\": true, \\\"consistent\\\": true, \\\"formal_wins\\\": true}\\n{\\\"id\\\": \\\"mvp_0042\\\", \\\"instruction\\\": \\\"Suggest an appropriate title for the below passage A global pandemic forced the hospitality industry to re-evaluate its practices and adapt to a new world of health and safety protocols.\\\", \\\"original_formality\\\": \\\"formal\\\", \\\"nli_cf\\\": 0.0008847906137816608, \\\"bertscore_cf\\\": 0.6714367866516113, \\\"trial1_choice\\\": \\\"A\\\", \\\"trial1_prefers_formal\\\": true, \\\"trial2_choice\\\": \\\"B\\\", \\\"trial2_prefers_formal\\\": true, \\\"consistent\\\": true, \\\"formal_wins\\\": true}\\n{\\\"id\\\": \\\"mvp_0082\\\", \\\"instruction\\\": \\\"Generate a word association for the word \\\\\\\"dog\\\\\\\"\\\", \\\"original_formality\\\": \\\"casual\\\", \\\"nli_cf\\\": 0.9940401911735535, \\\"bertscore_cf\\\": 0.9465831518173218, \\\"trial1_choice\\\": \\\"B\\\", \\\"trial1_prefers_formal\\\": false, \\\"trial2_choice\\\": \\\"A\\\", \\\"trial2_prefers_formal\\\": false, \\\"consistent\\\": true, \\\"formal_wins\\\": false}\\n{\\\"id\\\": \\\"mvp_0000\\\", \\\"instruction\\\": \\\"Hey, what can you do for me?\\\", \\\"original_formality\\\": \\\"formal\\\", \\\"nli_cf\\\": 0.9937858581542969, \\\"bertscore_cf\\\": 0.9007428884506226, \\\"trial1_choice\\\": \\\"A\\\", \\\"trial1_prefers_formal\\\": true, \\\"trial2_choice\\\": \\\"B\\\", \\\"trial2_prefers_formal\\\": true, \\\"consistent\\\": true, \\\"formal_wins\\\": true}\\n{\\\"id\\\": \\\"mvp_0023\\\", \\\"instruction\\\": \\\"Compute the derivative of 2x^2 + 5x.\\
…[truncated 8269 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_bt_model_diagnostics_20260521T114335",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T11:49:13.641084+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-29275",
  "command": "head -50 /root/causal_style_decomp_judge/data/verified_verbosity.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_bt_model_diagnostics_20260521T114335",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-29275",
    "command": "head -50 /root/causal_style_decomp_judge/data/verified_verbosity.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-21T11:49:13.641224+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-29275",
  "command": "ls /root/causal_style_decomp_judge/csd_pipeline/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_bt_model_diagnostics_20260521T114335",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-29275",
    "command": "ls /root/causal_style_decomp_judge/csd_pipeline/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-21T11:49:13.641518+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"instruction\\\": \\\"Hey, what can you do for me?\\\", \\\"response\\\": \\\"As an AI assistant, there are a few things I can't do for you:\\\\n\\\\n1. Physical tasks: I can't perform any physical tasks for you, such as cleaning your house or running errands.\\\\n\\\\n2. Emotional support: I can't provide emotional support like a human can. If you need someone to talk to, it's best to reach out to a friend, family member, or a professional.\\\\n\\\\n3. Make decisions for you: It's important to consider multiple perspectives and make choices based on your own judgment.\\\\n\\\\n4. Access personal accounts: I don't have access to personal accounts or sensitive information unless you explicitly provide it to me. It's important to be cautious and avoid sharing any personal or sensitive information with me or any other AI assistant.\\\\n\\\\n5. Physical sensations: I can't experience physical sensations or perceive the physical world.\\\\n\\\\nRemember, while I can assist you with various tasks, there are limitations to what I can do.\\\", \\\"source\\\": \\\"GPTInst\\\", \\\"label\\\": 2, \\\"id\\\": \\\"mvp_0000\\\", \\\"original_text\\\": \\\"As an AI assistant, there are a few things I can't do for you:\\\\n\\\\n1. Physical tasks: I can't perform any physical tasks for you, such as cleaning your house or running errands.\\\\n\\\\n2. Emotional support: I can't provide emotional support like a human can. If you need someone to talk to, it's best to reach out to a friend, family member, or a professional.\\\\n\\\\n3. Make decisions for you: It's important to consider multiple perspectives and make choices based on your own judgment.\\\\n\\\\n4. Access personal accounts: I don't have access to personal accounts or sensitive information unless you explicitly provide it to me. It's important to be cautious and avoid sharing any personal or sensitive information with me or any other AI assistant.\\\\n\\\\n5. Physi
…[truncated 6595 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_bt_model_diagnostics_20260521T114335",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T11:49:13.641855+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"id\\\": \\\"mvp_0027\\\", \\\"instruction\\\": \\\"Create a false fact about the planet Mars\\\", \\\"original_verbosity\\\": \\\"verbose\\\", \\\"nli_cf\\\": 0.9988196492195129, \\\"bertscore_cf\\\": 0.8647546768188477, \\\"trial1_choice\\\": \\\"A\\\", \\\"trial1_prefers_verbose\\\": true, \\\"trial2_choice\\\": \\\"B\\\", \\\"trial2_prefers_verbose\\\": true, \\\"consistent\\\": true, \\\"verbose_wins\\\": true}\\n{\\\"id\\\": \\\"mvp_0011\\\", \\\"instruction\\\": \\\"Create a story about a rabbit living with an adventurous squirrel in the forest.\\\", \\\"original_verbosity\\\": \\\"verbose\\\", \\\"nli_cf\\\": 0.9014860391616821, \\\"bertscore_cf\\\": 0.8093522787094116, \\\"trial1_choice\\\": \\\"A\\\", \\\"trial1_prefers_verbose\\\": true, \\\"trial2_choice\\\": \\\"B\\\", \\\"trial2_prefers_verbose\\\": true, \\\"consistent\\\": true, \\\"verbose_wins\\\": true}\\n{\\\"id\\\": \\\"mvp_0042\\\", \\\"instruction\\\": \\\"Suggest an appropriate title for the below passage A global pandemic forced the hospitality industry to re-evaluate its practices and adapt to a new world of health and safety protocols.\\\", \\\"original_verbosity\\\": \\\"concise\\\", \\\"nli_cf\\\": 0.9694910049438477, \\\"bertscore_cf\\\": 0.8620831966400146, \\\"trial1_choice\\\": \\\"A\\\", \\\"trial1_prefers_verbose\\\": true, \\\"trial2_choice\\\": \\\"A\\\", \\\"trial2_prefers_verbose\\\": false, \\\"consistent\\\": false, \\\"verbose_wins\\\": null}\\n{\\\"id\\\": \\\"mvp_0057\\\", \\\"instruction\\\": \\\"please answer the following questions based on the following documents: \\\\nhttps://www.gepf.gov.za/wp-content/uploads/2021/11/GEPF-Annual-Report-2020%EF%80%A221-30-September-2021.pdf\\\", \\\"original_verbosity\\\": \\\"concise\\\", \\\"nli_cf\\\": 0.018466269597411156, \\\"bertscore_cf\\\": 0.7943933606147766, \\\"trial1_choice\\\": \\\"A\\\", \\\"trial1_prefers_verbose\\\": true, \\\"trial2_choice\\\": \\\"B\\\", \\\
…[truncated 8046 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_bt_model_diagnostics_20260521T114335",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-21T11:49:13.642101+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"instruction\\\": \\\"Hey, what can you do for me?\\\", \\\"response\\\": \\\"As an AI assistant, there are a few things I can't do for you:\\\\n\\\\n1. Physical tasks: I can't perform any physical tasks for you, such as cleaning your house or running errands.\\\\n\\\\n2. Emotional support: I can't provide emotional support like a human can. If you need someone to talk to, it's best to reach out to a friend, family member, or a professional.\\\\n\\\\n3. Make decisions for you: It's important to consider multiple perspectives and make choices based on your own judgment.\\\\n\\\\n4. Access personal accounts: I don't have access to personal accounts or sensitive information unless you explicitly provide it to me. It's important to be cautious and avoid sharing any personal or sensitive information with me or any other AI assistant.\\\\n\\\\n5. Physical sensations: I can't experience physical sensations or perceive the physical world.\\\\n\\\\nRemember, while I can assist you with various tasks, there are limitations to what I can do.\\\", \\\"source\\\": \\\"GPTInst\\\", \\\"label\\\": 2, \\\"id\\\": \\\"mvp_0000\\\", \\\"original_text\\\": \\\"As an AI assistant, there are a few things I can't do for you:\\\\n\\\\n1. Physical tasks: I can't perform any physical tasks for you, such as cleaning your house or running errands.\\\\n\\\\n2. Emotional support: I can't provide emotional support like a human can. If you need someone to talk to, it's best to reach out to a friend, family member, or a professional.\\\\n\\\\n3. Make decisions for you: It's important to consider multiple perspectives and make choices based on your own judgment.\\\\n\\\\n4. Access personal accounts: I don't have access to personal accounts or sensitive information unless you explicitly provide it to me. It's important to be cautious and avoid sharing any personal or sensitive information with me or any other AI assistant.\\\\n\\\\n5. Physi
…[truncated 6535 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_bt_model_diagnostics_20260521T114335",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T11:49:13.642299+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"__init__.py\\n__pycache__\\nalpacaeval_qwen32b_scoring.py\\nalpacaeval_verbosity_qwen32b.py\\nate_analysis.py\\nbootstrap_10k_holm.py\\nclaude_judge_scoring.py\\ncontent_verification.py\\ncorrection_poc.py\\ncounterfactual_gen.py\\ndata_prep.py\\nexp010_binarized_likert.py\\nexp011_nli_sensitivity.py\\nexp012_consistency_bias.py\\nexp013_nli_validation.py\\nexp013_spotcheck.py\\nexp014_logistic_decomposition.py\\nexp015_clmm_analysis.py\\nexp016_bradley_terry.py\\nfix_formality_rewriter_bt.py\\ngate_comparison_bt.py\\ngee_diagnostics.py\\ngen_forest_plot.py\\ngen_pipeline_figure.py\\ngen_power_curve.py\\ngpt4o_analysis.py\\ngpt4o_crossbenchmark_scoring.py\\ngpt4o_rewriter_formality_scoring.py\\njudge_scoring.py\\nmtbench_qwen32b_scoring.py\\nnli_fn_selection_bias.py\\nnli_gate_fn_selection_bias.py\\nnli_gate_gpt4o_spotcheck.py\\nnli_only_verify.py\\npairwise_scoring.py\\nqwen32b_analysis.py\\nqwen32b_register_bt.py\\nverbosity_gee.py\\nverbosity_length_confound.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.25}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_bt_model_diagnostics_20260521T114335",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T11:49:13.642589+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-29275",
  "command": "head -80 /root/causal_style_decomp_judge/csd_pipeline/exp016_bradley_terry.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_bt_model_diagnostics_20260521T114335",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-29275",
    "command": "head -80 /root/causal_style_decomp_judge/csd_pipeline/exp016_bradley_terry.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-21T11:49:13.642767+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"exp-016: Bradley-Terry model for pairwise style preference.\\n\\nPair-level bootstrap (corrected): resamples pairs, not individual comparisons,\\nbecause within-pair trials (AB + BA) are correlated.\\n\\nRuns on both all-data and NLI-filtered (>=0.90) subsets.\\n\\nInput:  data/pairwise_results_32b.jsonl\\nOutput: console summary with BT parameters and bootstrap CI\\n\\\"\\\"\\\"\\n\\nimport json\\n\\nimport choix\\nimport numpy as np\\n\\nDATA_PATH = \\\"/root/causal_style_decomp_judge/data/pairwise_results_32b.jsonl\\\"\\nN_BOOT = 10000\\nFORMAL, CASUAL = 0, 1\\n\\n\\ndef load_data(path, nli_threshold=None):\\n    raw = []\\n    with open(path) as f:\\n        for line in f:\\n            if line.strip():\\n                raw.append(json.loads(line))\\n\\n    if nli_threshold is not None:\\n        raw = [d for d in raw if d.get(\\\"nli_cf\\\", 0) >= nli_threshold]\\n\\n    comparisons = []\\n    pair_groups = {}\\n    t1_formal, t1_total = 0, 0\\n    t2_formal, t2_total = 0, 0\\n\\n    for rec in raw:\\n        pair_id = rec[\\\"id\\\"]\\n        pcomps = []\\n\\n        t1 = rec.get(\\\"trial1_choice\\\")\\n        if t1 in (\\\"A\\\", \\\"B\\\"):\\n            t1_total += 1\\n            if t1 == \\\"A\\\":\\n                pcomps.append((FORMAL, CASUAL))\\n                t1_formal += 1\\n            else:\\n                pcomps.append((CASUAL, FORMAL))\\n\\n        t2 = rec.get(\\\"trial2_choice\\\")\\n        if t2 in (\\\"A\\\", \\\"B\\\"):\\n            t2_total += 1\\n            if t2 == \\\"A\\\":\\n                pcomps.append((CASUAL, FORMAL))\\n            else:\\n                pcomps.append((FORMAL, CASUAL))\\n                t2_formal += 1\\n\\n        comparisons.extend(pcomps)\\n        pair_groups[pair_id] = pcomps\\n\\n    total_formal = t1_formal + t2_formal\\n    total = t1_total + t2_total\\n    if t1_total:\\n        print(f\\\"  Trial 1: {t1_formal}/{t1_total} forma
…[truncated 756 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_bt_model_diagnostics_20260521T114335",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T11:49:13.642937+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-29275",
  "command": "tail -80 /root/causal_style_decomp_judge/csd_pipeline/exp016_bradley_terry.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_bt_model_diagnostics_20260521T114335",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-29275",
    "command": "tail -80 /root/causal_style_decomp_judge/csd_pipeline/exp016_bradley_terry.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-21T11:49:13.643122+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"    print(f\\\"{'='*60}\\\")\\n    print(f\\\"  N pairs: {len(pair_groups)}\\\")\\n    print(f\\\"  N comparisons: {len(comparisons)}\\\")\\n    print(f\\\"  Position-consistent pairs: {n_consistent}/{n_data}\\\")\\n\\n    diff = fit_bt(comparisons)\\n    p_formal = 1.0 / (1.0 + np.exp(-diff))\\n    print(f\\\"\\\\n  BT formal-casual strength: {diff:+.4f}\\\")\\n    print(f\\\"  BT P(formal wins): {p_formal:.4f}\\\")\\n\\n    # --- Pair-level bootstrap (CORRECTED) ---\\n    print(f\\\"\\\\n  Pair-level bootstrap ({N_BOOT} iterations)...\\\")\\n    bp = bootstrap_pair(pair_groups)\\n    bp_lo, bp_hi = np.percentile(bp, [2.5, 97.5])\\n    bp_lo_p = 1.0 / (1.0 + np.exp(-bp_lo))\\n    bp_hi_p = 1.0 / (1.0 + np.exp(-bp_hi))\\n    bp_probs = 1.0 / (1.0 + np.exp(-bp))\\n    n_below = int(np.sum(bp_probs < 0.5))\\n    bp_pval = n_below / len(bp)\\n\\n    print(f\\\"  [PAIR] Strength 95% CI: [{bp_lo:+.4f}, {bp_hi:+.4f}]\\\")\\n    print(f\\\"  [PAIR] Win prob 95% CI: [{bp_lo_p:.4f}, {bp_hi_p:.4f}]\\\")\\n    print(f\\\"  [PAIR] Mean: {np.mean(bp):+.4f} (sd={np.std(bp):.4f})\\\")\\n    if bp_pval == 0:\\n        print(f\\\"  [PAIR] p < {1/len(bp):.6f} (0/{len(bp)} below 0.5)\\\")\\n    else:\\n        print(f\\\"  [PAIR] p = {bp_pval:.6f} ({n_below}/{len(bp)} below 0.5)\\\")\\n\\n    # --- Comparison-level bootstrap (old, for comparison) ---\\n    print(f\\\"\\\\n  Comparison-level bootstrap ({N_BOOT} iterations, reference)...\\\")\\n    bc = bootstrap_comp(comparisons)\\n    bc_lo, bc_hi = np.percentile(bc, [2.5, 97.5])\\n    bc_lo_p = 1.0 / (1.0 + np.exp(-bc_lo))\\n    bc_hi_p = 1.0 / (1.0 + np.exp(-bc_hi))\\n\\n    print(f\\\"  [COMP] Strength 95% CI: [{bc_lo:+.4f}, {bc_hi:+.4f}]\\\")\\n    print(f\\\"  [COMP] Win prob 95% CI: [{bc_lo_p:.4f}, {bc_hi_p:.4f}]\\\")\\n    print(f\\\"  [COMP] Mean: {np.mean(bc):+.4f} (sd={np.std(bc):.4f})\\\")\\n\\n    pair_w = bp_hi_p - bp_lo_p\\n    comp_w = bc_hi_p - bc_lo_p\\n    print
…[truncated 1664 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_bt_model_diagnostics_20260521T114335",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-21T11:49:13.643342+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westb-29275",
  "command": "cat > /root/causal_style_decomp_judge/csd_pipeline/bt_model_diagnostics.py << 'PYEOF'\n\"\"\"BT Model Diagnostics (W-MF2): GoF deviance + stratified BT stability.\"\"\"\n\nimport json\nimport os\n\nimport choix\nimport numpy as np\nfrom scipy import stats\n\nNLI_THRESHOLD = 0.90\nN_BOOT = 10000\nSEED = 42\n\n\ndef load_filtered(path, wins_key):\n    \"\"\"Load NLI-filtered, consistent pairs with definitive outcome.\"\"\"\n    pairs = []\n    with open(path) as f:\n        for line in f:\n            if not line.strip():\n                continue\n            r = json.loads(line)\n            if (r[\"nli_cf\"] >= NLI_THRESHOLD\n                    and r.get(\"consistent\", False)\n                    and r[wins_key] is not None):\n                pairs.append(r)\n    return pairs\n\n\ndef bt_prob(win_count, total):\n    \"\"\"BT win probability for 2-item model (item 0 = positive style).\"\"\"\n    if total == 0:\n        return 0.5\n    data = [(0, 1)] * win_count + [(1, 0)] * (total - win_count)\n    params = choix.ilsr_pairwise(2, data, alpha=0.01)\n    return float(np.exp(params[0]) / np.sum(np.exp(params)))\n\n\ndef gof_deviance(pairs, wins_key):\n    \"\"\"Goodness-of-fit deviance test: all pairs share one BT probability.\"\"\"\n    n = len(pairs)\n    w = sum(1 for p in pairs if p[wins_key])\n    p_hat = bt_prob(w, n)\n\n    eps = 1e-15\n    p_s = np.clip(p_hat, eps, 1 - eps)\n    D = -2.0 * (w * np.log(p_s) + (n - w) * np.log(1 - p_s))\n    df = n - 1\n    p_val = float(stats.chi2.sf(D, df))\n\n    return {\n        \"deviance\": round(float(D), 4),\n        \"df\": df,\n        \"p_value\": round(p_val, 6),\n        \"n_pairs\": n,\n        \"wins\": w,\n        \"bt_prob\": round(p_hat, 4),\n    }\n\n\ndef pair_bootstrap(pairs, wins_key, n_boot=N_BOOT, seed=SEED):\n    \"\"\"Pair-level bootstrap CI for win rate.\"\"\"\n    rng = np.random.RandomState(seed)\n    outcomes = np.array([1 if p[wins_key] else 0 for p in pairs])\n    n = len(outcomes)\n    rates = np.empty(n_boot)\n    for i in range(n_boot):\n        idx = rng.randint(0, n, size=n)\n        rates[i] = outcomes[idx].mean()\n    ci = np.percentile(rates, [2.5, 97.5]).tolist()\n    return float(outcomes.mean()), [round(ci[0], 4), round(ci[1], 4)]\n\n\ndef stratified(pairs, dir_key, wins_key, pos_label, neg_label):\n    \"\"\"Stratified BT by originality direction + Fisher/chi2 tests.\"\"\"\n    grp_pos = [p for p in pairs if p[dir_key] == pos_label]\n    grp_neg = [p for p in pairs if p[dir_key] == neg_label]\n\n    out = {}\n    for name, grp in [(f\"orig_is_{pos_label}\", grp_pos),\n                       (f\"orig_is_{neg_label}\", grp_neg)]:\n        n = len(grp)\n        wc = sum(1 for p in grp if p[wins_key])\n        rate, ci = pair_bootstrap(grp, wins_key)\n        out[name] = {\n            \"n\": n,\n            \"bt\": round(rate, 4),\n            \"ci\": ci,\n            \"win_count\": wc,\n            \"total\": n,\n        }\n\n    a = out[f\"orig_is_{pos_label}\"][\"win_count\"]\n    b = out[f\"orig_is_{pos_label}\"][\"total\"] - a\n    c = out[f\"orig_is_{neg_label}\"][\"win_count\"]\n    d = out[f\"orig_is_{neg_label}\"][\"total\"] - c\n\n    _, fisher_p = stats.fisher_exact([[a, b], [c, d]])\n    chi2_stat, chi2_p, _, _ = stats.chi2_contingency(\n        [[a, b], [c, d]], correction=False\n    )\n\n    out[\"fisher_p\"] = round(float(fisher_p), 6)\n    out[\"chi2_p\"] = round(float(chi2_p), 6)\n    return out\n\n\ndef main():\n    os.chdir(\"/root/causal_style_decomp_judge\")\n\n    form = load_filtered(\"data/pairwise_results_32b.jsonl\", \"formal_wins\")\n    verb = load_filtered(\n        \"data/pairwise_results_qwen32b_verbosity.jsonl\", \"verbose_wins\"\n    )\n\n    print(f\"Formality: {len(form)} consistent NLI-pass pairs\")\n    print(f\"Verbosity: {len(verb)} consistent NLI-pass pairs\")\n\n    result = {\n        \"gof\": {\n            \"formality\": gof_deviance(form, \"formal_wins\"),\n            \"verbosity\": gof_deviance(verb, \"verbose_wins\"),\n        },\n        \"stratified_bt\": {\n            \"formality\": stratified(\n                form, \"original_formality\", \"formal_wins\",\n                \"formal\", \"casual\"\n            ),\n            \"verbosity\": stratified(\n                verb, \"original_verbosity\", \"verbose_wins\",\n                \"verbose\", \"concise\"\n            ),\n        },\n    }\n\n    out_path = \"data/bt_model_diagnostics.json\"\n    with open(out_path, \"w\") as f:\n        json.dump(result, f, indent=2)\n\n    print(f\"\\nSaved to {out_path}\")\n    print(json.dumps(result, indent=2))\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"DONE\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_bt_model_diagnostics_20260521T114335",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westb-29275",
    "command": "cat > /root/causal_style_decomp_judge/csd_pipeline/bt_model_diagnostics.py << 'PYEOF'\n\"\"\"BT Model Diagnostics (W-MF2): GoF deviance + stratified BT stability.\"\"\"\n\nimport json\nimport os\n\nimport choix\nimport numpy as np\nfrom scipy import stats\n\nNLI_THRESHOLD = 0.90\nN_BOOT = 10000\nSEED = 42\n\n\ndef load_filtered(path, wins_key):\n    \"\"\"Load NLI-filtered, consistent pairs with definitive outcome.\"\"\"\n    pairs = []\n    with open(path) as f:\n        for line in f:\n            if not line.strip():\n                continue\n            r = json.loads(line)\n            if (r[\"nli_cf\"] >= NLI_THRESHOLD\n                    and r.get(\"consistent\", False)\n                    and r[wins_key] is not None):\n                pairs.append(r)\n    return pairs\n\n\ndef bt_prob(win_count, total):\n    \"\"\"BT win probability for 2-item model (item 0 = positive style).\"\"\"\n    if total == 0:\n        return 0.5\n    data = [(0, 1)] * win_count + [(1, 0)] * (total - win_count)\n    params = choix.ilsr_pairwise(2, data, alpha=0.01)\n    return float(np.exp(params[0]) / np.sum(np.exp(params)))\n\n\ndef gof_deviance(pairs, wins_key):\n    \"\"\"Goodness-of-fit deviance test: all pairs share one BT probability.\"\"\"\n    n = len(pairs)\n    w = sum(1 for p in pairs if p[wins_key])\n    p_hat = bt_prob(w, n)\n\n    eps = 1e-15\n    p_s = np.clip(p_hat, eps, 1 - eps)\n    D = -2.0 * (w * np.log(p_s) + (n - w) * np.log(1 - p_s))\n    df = n - 1\n    p_val = float(stats.chi2.sf(D, df))\n\n    return {\n        \"deviance\": round(float(D), 4),\n        \"df\": df,\n        \"p_value\": round(p_val, 6),\n        \"n_pairs\": n,\n        \"wins\": w,\n        \"bt_prob\": round(p_hat, 4),\n    }\n\n\ndef pair_bootstrap(pairs, wins_key, n_boot=N_BOOT, seed=SEED):\n    \"\"\"Pair-level bootstrap CI for win rate.\"\"\"\n    rng = np.random.RandomState(seed)\n    outcomes = np.array([1 if p[wins_key] else 0 for p in pairs])\n    n = len(outcomes)\n    rates = np.empty(n_boot)\n    for i in range(n_boot):\n        idx = rng.randint(0, n, size=n)\n        rates[i] = outcomes[idx].mean()\n    ci = np.percentile(rates, [2.5, 97.5]).tolist()\n    return float(outcomes.mean()), [round(ci[0], 4), round(ci[1], 4)]\n\n\ndef stratified(pairs, dir_key, wins_key, pos_label, neg_label):\n    \"\"\"Stratified BT by originality direction + Fisher/chi2 tests.\"\"\"\n    grp_pos = [p for p in pairs if p[dir_key] == pos_label]\n    grp_neg = [p for p in pairs if p[dir_key] == neg_label]\n\n    out = {}\n    for name, grp in [(f\"orig_is_{pos_label}\", grp_pos),\n                       (f\"orig_is_{neg_label}\", grp_neg)]:\n        n = len(grp)\n        wc = sum(1 for p in grp if p[wins_key])\n        rate, ci = pair_bootstrap(grp, wins_key)\n        out[name] = {\n            \"n\": n,\n            \"bt\": round(rate, 4),\n            \"ci\": ci,\n            \"win_count\": wc,\n            \"total\": n,\n        }\n\n    a = out[f\"orig_is_{pos_label}\"][\"win_count\"]\n    b = out[f\"orig_is_{pos_label}\"][\"total\"] - a\n    c = out[f\"orig_is_{neg_label}\"][\"win_count\"]\n    d = out[f\"orig_is_{neg_label}\"][\"total\"] - c\n\n    _, fisher_p = stats.fisher_exact([[a, b], [c, d]])\n    chi2_stat, chi2_p, _, _ = stats.chi2_contingency(\n        [[a, b], [c, d]], correction=False\n    )\n\n    out[\"fisher_p\"] = round(float(fisher_p), 6)\n    out[\"chi2_p\"] = round(float(chi2_p), 6)\n    return out\n\n\ndef main():\n    os.chdir(\"/root/causal_style_decomp_judge\")\n\n    form = load_filtered(\"data/pairwise_results_32b.jsonl\", \"formal_wins\")\n    verb = load_filtered(\n        \"data/pairwise_results_qwen32b_verbosity.jsonl\", \"verbose_wins\"\n    )\n\n    print(f\"Formality: {len(form)} consistent NLI-pass pairs\")\n    print(f\"Verbosity: {len(verb)} consistent NLI-pass pairs\")\n\n    result = {\n        \"gof\": {\n            \"formality\": gof_deviance(form, \"formal_wins\"),\n            \"verbosity\": gof_deviance(verb, \"verbose_wins\"),\n        },\n        \"stratified_bt\": {\n            \"formality\": stratified(\n                form, \"original_formality\", \"formal_wins\",\n                \"formal\", \"casual\"\n            ),\n            \"verbosity\": stratified(\n                verb, \"original_verbosity\", \"verbose_wins\",\n                \"verbose\", \"concise\"\n            ),\n        },\n    }\n\n    out_path = \"data/bt_model_diagnostics.json\"\n    with open(out_path, \"w\") as f:\n        json.dump(result, f, indent=2)\n\n    print(f\"\\nSaved to {out_path}\")\n    print(json.dumps(result, indent=2))\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"DONE\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-21T11:49:13.643527+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"DONE\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.54}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_bt_model_diagnostics_20260521T114335",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-21T11:49:13.643666+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westb-29275",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/causal_style_decomp_judge && python csd_pipeline/bt_model_diagnostics.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_bt_model_diagnostics_20260521T114335",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westb-29275",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/causal_style_decomp_judge && python csd_pipeline/bt_model_diagnostics.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-21T11:49:13.643829+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Formality: 46 consistent NLI-pass pairs\\nVerbosity: 63 consistent NLI-pass pairs\\n\\nSaved to data/bt_model_diagnostics.json\\n{\\n  \\\"gof\\\": {\\n    \\\"formality\\\": {\\n      \\\"deviance\\\": 52.8047,\\n      \\\"df\\\": 45,\\n      \\\"p_value\\\": 0.197992,\\n      \\\"n_pairs\\\": 46,\\n      \\\"wins\\\": 34,\\n      \\\"bt_prob\\\": 0.7389\\n    },\\n    \\\"verbosity\\\": {\\n      \\\"deviance\\\": 47.9573,\\n      \\\"df\\\": 62,\\n      \\\"p_value\\\": 0.904924,\\n      \\\"n_pairs\\\": 63,\\n      \\\"wins\\\": 55,\\n      \\\"bt_prob\\\": 0.8728\\n    }\\n  },\\n  \\\"stratified_bt\\\": {\\n    \\\"formality\\\": {\\n      \\\"orig_is_formal\\\": {\\n        \\\"n\\\": 27,\\n        \\\"bt\\\": 0.8889,\\n        \\\"ci\\\": [\\n          0.7778,\\n          1.0\\n        ],\\n        \\\"win_count\\\": 24,\\n        \\\"total\\\": 27\\n      },\\n      \\\"orig_is_casual\\\": {\\n        \\\"n\\\": 19,\\n        \\\"bt\\\": 0.5263,\\n        \\\"ci\\\": [\\n          0.3158,\\n          0.7368\\n        ],\\n        \\\"win_count\\\": 10,\\n        \\\"total\\\": 19\\n      },\\n      \\\"fisher_p\\\": 0.014644,\\n      \\\"chi2_p\\\": 0.005826\\n    },\\n    \\\"verbosity\\\": {\\n      \\\"orig_is_verbose\\\": {\\n        \\\"n\\\": 29,\\n        \\\"bt\\\": 0.8276,\\n        \\\"ci\\\": [\\n          0.6897,\\n          0.9655\\n        ],\\n        \\\"win_count\\\": 24,\\n        \\\"total\\\": 29\\n      },\\n      \\\"orig_is_concise\\\": {\\n        \\\"n\\\": 34,\\n        \\\"bt\\\": 0.9118,\\n        \\\"ci\\\": [\\n          0.7941,\\n          1.0\\n        ],\\n        \\\"win_count\\\": 31,\\n        \\\"total\\\": 34\\n      },\\n      \\\"fisher_p\\\": 0.453064,\\n      \\\"chi2_p\\\": 0.317217\\n    }\\n  }\\n}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.66}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_bt_model_diagnostics_20260521T114335",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-21T11:49:13.644013+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/csd_pipeline/",
  "description": "List local csd_pipeline directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_bt_model_diagnostics_20260521T114335",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/csd_pipeline/",
    "description": "List local csd_pipeline directory"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-21T11:49:13.644224+00:00_

alpacaeval_qwen32b_scoring.py
bootstrap_10k_holm.py
claude_judge_scoring.py
claude_tost_equivalence.py
fix_formality_rewriter_bt.py
gate_comparison_bt.py
gee_diagnostics.py
gen_forest_plot.py
gpt4o_crossbenchmark_scoring.py
gpt4o_rewriter_formality_scoring.py
nli_fn_selection_bias.py
nli_gate_fn_selection_bias.py
nli_gate_gpt4o_spotcheck.py
qwen32b_analysis.py
qwen32b_register_bt.py
verbosity_gee.py
verbosity_length_confound.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_bt_model_diagnostics_20260521T114335",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-21T11:49:13.644463+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/csd_pipeline/bt_model_diagnostics.py",
  "content": "\"\"\"BT Model Diagnostics (W-MF2): GoF deviance + stratified BT stability.\"\"\"\n\nimport json\nimport os\n\nimport choix\nimport numpy as np\nfrom scipy import stats\n\nNLI_THRESHOLD = 0.90\nN_BOOT = 10000\nSEED = 42\n\n\ndef load_filtered(path, wins_key):\n    \"\"\"Load NLI-filtered, consistent pairs with definitive outcome.\"\"\"\n    pairs = []\n    with open(path) as f:\n        for line in f:\n            if not line.strip():\n                continue\n            r = json.loads(line)\n            if (r[\"nli_cf\"] >= NLI_THRESHOLD\n                    and r.get(\"consistent\", False)\n                    and r[wins_key] is not None):\n                pairs.append(r)\n    return pairs\n\n\ndef bt_prob(win_count, total):\n    \"\"\"BT win probability for 2-item model (item 0 = positive style).\"\"\"\n    if total == 0:\n        return 0.5\n    data = [(0, 1)] * win_count + [(1, 0)] * (total - win_count)\n    params = choix.ilsr_pairwise(2, data, alpha=0.01)\n    return float(np.exp(params[0]) / np.sum(np.exp(params)))\n\n\ndef gof_deviance(pairs, wins_key):\n    \"\"\"Goodness-of-fit deviance test: all pairs share one BT probability.\"\"\"\n    n = len(pairs)\n    w = sum(1 for p in pairs if p[wins_key])\n    p_hat = bt_prob(w, n)\n\n    eps = 1e-15\n    p_s = np.clip(p_hat, eps, 1 - eps)\n    D = -2.0 * (w * np.log(p_s) + (n - w) * np.log(1 - p_s))\n    df = n - 1\n    p_val = float(stats.chi2.sf(D, df))\n\n    return {\n        \"deviance\": round(float(D), 4),\n        \"df\": df,\n        \"p_value\": round(p_val, 6),\n        \"n_pairs\": n,\n        \"wins\": w,\n        \"bt_prob\": round(p_hat, 4),\n    }\n\n\ndef pair_bootstrap(pairs, wins_key, n_boot=N_BOOT, seed=SEED):\n    \"\"\"Pair-level bootstrap CI for win rate.\"\"\"\n    rng = np.random.RandomState(seed)\n    outcomes = np.array([1 if p[wins_key] else 0 for p in pairs])\n    n = len(outcomes)\n    rates = np.empty(n_boot)\n    for i in range(n_boot):\n        idx = rng.randint(0, n, size=n)\n        rates[i] = outcomes[idx].mean()\n    ci = np.percentile(rates, [2.5, 97.5]).tolist()\n    return float(outcomes.mean()), [round(ci[0], 4), round(ci[1], 4)]\n\n\ndef stratified(pairs, dir_key, wins_key, pos_label, neg_label):\n    \"\"\"Stratified BT by originality direction + Fisher/chi2 tests.\"\"\"\n    grp_pos = [p for p in pairs if p[dir_key] == pos_label]\n    grp_neg = [p for p in pairs if p[dir_key] == neg_label]\n\n    out = {}\n    for name, grp in [(f\"orig_is_{pos_label}\", grp_pos),\n                       (f\"orig_is_{neg_label}\", grp_neg)]:\n        n = len(grp)\n        wc = sum(1 for p in grp if p[wins_key])\n        rate, ci = pair_bootstrap(grp, wins_key)\n        out[name] = {\n            \"n\": n,\n            \"bt\": round(rate, 4),\n            \"ci\": ci,\n            \"win_count\": wc,\n            \"total\": n,\n        }\n\n    a = out[f\"orig_is_{pos_label}\"][\"win_count\"]\n    b = out[f\"orig_is_{pos_label}\"][\"total\"] - a\n    c = out[f\"orig_is_{neg_label}\"][\"win_count\"]\n    d = out[f\"orig_is_{neg_label}\"][\"total\"] - c\n\n    _, fisher_p = stats.fisher_exact([[a, b], [c, d]])\n    chi2_stat, chi2_p, _, _ = stats.chi2_contingency(\n        [[a, b], [c, d]], correction=False\n    )\n\n    out[\"fisher_p\"] = round(float(fisher_p), 6)\n    out[\"chi2_p\"] = round(float(chi2_p), 6)\n    return out\n\n\ndef main():\n    os.chdir(\"/root/causal_style_decomp_judge\")\n\n    form = load_filtered(\"data/pairwise_results_32b.jsonl\", \"formal_wins\")\n    verb = load_filtered(\n        \"data/pairwise_results_qwen32b_verbosity.jsonl\", \"verbose_wins\"\n    )\n\n    print(f\"Formality: {len(form)} consistent NLI-pass pairs\")\n    print(f\"Verbosity: {len(verb)} consistent NLI-pass pairs\")\n\n    result = {\n        \"gof\": {\n            \"formality\": gof_deviance(form, \"formal_wins\"),\n            \"verbosity\": gof_deviance(verb, \"verbose_wins\"),\n        },\n        \"stratified_bt\": {\n            \"formality\": stratified(\n                form, \"original_formality\", \"formal_wins\",\n                \"formal\", \"casual\"\n            ),\n            \"verbosity\": stratified(\n                verb, \"original_verbosity\", \"verbose_wins\",\n                \"verbose\", \"concise\"\n            ),\n        },\n    }\n\n    out_path = \"data/bt_model_diagnostics.json\"\n    with open(out_path, \"w\") as f:\n        json.dump(result, f, indent=2)\n\n    print(f\"\\nSaved to {out_path}\")\n    print(json.dumps(result, indent=2))\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_bt_model_diagnostics_20260521T114335",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/csd_pipeline/bt_model_diagnostics.py",
    "content": "\"\"\"BT Model Diagnostics (W-MF2): GoF deviance + stratified BT stability.\"\"\"\n\nimport json\nimport os\n\nimport choix\nimport numpy as np\nfrom scipy import stats\n\nNLI_THRESHOLD = 0.90\nN_BOOT = 10000\nSEED = 42\n\n\ndef load_filtered(path, wins_key):\n    \"\"\"Load NLI-filtered, consistent pairs with definitive outcome.\"\"\"\n    pairs = []\n    with open(path) as f:\n        for line in f:\n            if not line.strip():\n                continue\n            r = json.loads(line)\n            if (r[\"nli_cf\"] >= NLI_THRESHOLD\n                    and r.get(\"consistent\", False)\n                    and r[wins_key] is not None):\n                pairs.append(r)\n    return pairs\n\n\ndef bt_prob(win_count, total):\n    \"\"\"BT win probability for 2-item model (item 0 = positive style).\"\"\"\n    if total == 0:\n        return 0.5\n    data = [(0, 1)] * win_count + [(1, 0)] * (total - win_count)\n    params = choix.ilsr_pairwise(2, data, alpha=0.01)\n    return float(np.exp(params[0]) / np.sum(np.exp(params)))\n\n\ndef gof_deviance(pairs, wins_key):\n    \"\"\"Goodness-of-fit deviance test: all pairs share one BT probability.\"\"\"\n    n = len(pairs)\n    w = sum(1 for p in pairs if p[wins_key])\n    p_hat = bt_prob(w, n)\n\n    eps = 1e-15\n    p_s = np.clip(p_hat, eps, 1 - eps)\n    D = -2.0 * (w * np.log(p_s) + (n - w) * np.log(1 - p_s))\n    df = n - 1\n    p_val = float(stats.chi2.sf(D, df))\n\n    return {\n        \"deviance\": round(float(D), 4),\n        \"df\": df,\n        \"p_value\": round(p_val, 6),\n        \"n_pairs\": n,\n        \"wins\": w,\n        \"bt_prob\": round(p_hat, 4),\n    }\n\n\ndef pair_bootstrap(pairs, wins_key, n_boot=N_BOOT, seed=SEED):\n    \"\"\"Pair-level bootstrap CI for win rate.\"\"\"\n    rng = np.random.RandomState(seed)\n    outcomes = np.array([1 if p[wins_key] else 0 for p in pairs])\n    n = len(outcomes)\n    rates = np.empty(n_boot)\n    for i in range(n_boot):\n        idx = rng.randint(0, n, size=n)\n        rates[i] = outcomes[idx].mean()\n    ci = np.percentile(rates, [2.5, 97.5]).tolist()\n    return float(outcomes.mean()), [round(ci[0], 4), round(ci[1], 4)]\n\n\ndef stratified(pairs, dir_key, wins_key, pos_label, neg_label):\n    \"\"\"Stratified BT by originality direction + Fisher/chi2 tests.\"\"\"\n    grp_pos = [p for p in pairs if p[dir_key] == pos_label]\n    grp_neg = [p for p in pairs if p[dir_key] == neg_label]\n\n    out = {}\n    for name, grp in [(f\"orig_is_{pos_label}\", grp_pos),\n                       (f\"orig_is_{neg_label}\", grp_neg)]:\n        n = len(grp)\n        wc = sum(1 for p in grp if p[wins_key])\n        rate, ci = pair_bootstrap(grp, wins_key)\n        out[name] = {\n            \"n\": n,\n            \"bt\": round(rate, 4),\n            \"ci\": ci,\n            \"win_count\": wc,\n            \"total\": n,\n        }\n\n    a = out[f\"orig_is_{pos_label}\"][\"win_count\"]\n    b = out[f\"orig_is_{pos_label}\"][\"total\"] - a\n    c = out[f\"orig_is_{neg_label}\"][\"win_count\"]\n    d = out[f\"orig_is_{neg_label}\"][\"total\"] - c\n\n    _, fisher_p = stats.fisher_exact([[a, b], [c, d]])\n    chi2_stat, chi2_p, _, _ = stats.chi2_contingency(\n        [[a, b], [c, d]], correction=False\n    )\n\n    out[\"fisher_p\"] = round(float(fisher_p), 6)\n    out[\"chi2_p\"] = round(float(chi2_p), 6)\n    return out\n\n\ndef main():\n    os.chdir(\"/root/causal_style_decomp_judge\")\n\n    form = load_filtered(\"data/pairwise_results_32b.jsonl\", \"formal_wins\")\n    verb = load_filtered(\n        \"data/pairwise_results_qwen32b_verbosity.jsonl\", \"verbose_wins\"\n    )\n\n    print(f\"Formality: {len(form)} consistent NLI-pass pairs\")\n    print(f\"Verbosity: {len(verb)} consistent NLI-pass pairs\")\n\n    result = {\n        \"gof\": {\n            \"formality\": gof_deviance(form, \"formal_wins\"),\n            \"verbosity\": gof_deviance(verb, \"verbose_wins\"),\n        },\n        \"stratified_bt\": {\n            \"formality\": stratified(\n                form, \"original_formality\", \"formal_wins\",\n                \"formal\", \"casual\"\n            ),\n            \"verbosity\": stratified(\n                verb, \"original_verbosity\", \"verbose_wins\",\n                \"verbose\", \"concise\"\n            ),\n        },\n    }\n\n    out_path = \"data/bt_model_diagnostics.json\"\n    with open(out_path, \"w\") as f:\n        json.dump(result, f, indent=2)\n\n    print(f\"\\nSaved to {out_path}\")\n    print(json.dumps(result, indent=2))\n\n\nif __name__ == \"__main__\":\n    main()\n"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-21T11:49:13.644739+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/csd_pipeline/bt_model_diagnostics.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_bt_model_diagnostics_20260521T114335",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-21T11:49:13.644973+00:00_

完成。结果摘要：

**GoF Deviance Test** — 两个维度 BT 模型均 adequate：
- Formality: D=52.80, df=45, **p=0.198** (n=46 consistent pairs, BT prob=0.739)
- Verbosity: D=47.96, df=62, **p=0.905** (n=63 consistent pairs, BT prob=0.873)

**Stratified BT Stability:**
- **Formality: 显著方向差异**
  - orig_is_formal: 88.9% [77.8%, 100%], 24/27
  - orig_is_casual: 52.6% [31.6%, 73.7%], 10/19
  - Fisher p=0.015, chi2 p=0.006
- **Verbosity: 无显著方向差异**
  - orig_is_verbose: 82.8% [69.0%, 96.6%], 24/29
  - orig_is_concise: 91.2% [79.4%, 100%], 31/34
  - Fisher p=0.453, chi2 p=0.317

Formality 的分层差异 (Fisher p=0.015) 提示原始文本为 formal 时 judge 更倾向选择 formal，originality preference confound 显著。Verbosity 无此问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_bt_model_diagnostics_20260521T114335"
}
```

</details>

---
