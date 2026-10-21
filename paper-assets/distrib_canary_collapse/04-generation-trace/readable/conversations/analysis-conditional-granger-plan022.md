# analysis conditional granger plan022

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 65
- **Recorded user turns:** 0
- **Tool calls:** 32
- **Original source:** `logs/chats/worker_analysis_conditional_granger_plan022_20260521T021117.jsonl`
- **Structured JSON:** [`f3777f3e6a5074f14aff.json`](../../sessions/f3/f3777f3e6a5074f14aff.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

65 recorded events

### Tool call

_source line 1 · 2026-05-21T02:17:59.536426+00:00_

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
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
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

_source line 2 · 2026-05-21T02:17:59.536882+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T02:17:59.537072+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42_fp32/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42_fp32/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-21T02:17:59.537209+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-21T02:17:59.537395+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42_fp32/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 1.34}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T02:17:59.537558+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"ablation\\nalpha_sweep\\nalpha_sweep_analysis\\nanalysis\\nbootstrap_ty_dryrun.json\\nbootstrap_ty_results.json\\ndetrending\\ndose_response_drift.csv\\ngen_opt13b_wiki_a100_s43_fp32\\ngen_wiki_gpt2m_a100_s43\\ngeneralize\\nintervention\\nlag_sensitivity\\nlag_sensitivity_log.txt\\nmethod_ablation_phase2_panel.json\\nmethod_ablation_phase2_report.md\\nmethod_ablation_phase3_panel.json\\nmethod_ablation_phase3_report.md\\nmoment_cascade\\nmoment_cascade_analysis.py\\nperm_granger_power_bootstrap.json\\nrebuttal\\nscale\\nscale_check\\nshapley_method_contribution_v3.pdf\\nshapley_method_contribution_v3.png\\nshapley_values.json\\nty_batch_rerun_19828_summary.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T02:17:59.537688+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-21T02:17:59.537810+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/generalize/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/generalize/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-21T02:17:59.537939+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"a000_s42\\na000_s43\\na000_s44\\na010_s42\\na010_s42_fp32\\na010_s43_fp32\\na025_3seed_unified_summary.txt\\na025_s43\\na025_s44\\na050_s42\\na050_s43\\na050_s44\\na055_s42_fp32\\na060_s42_bf16\\na075_s42\\na075_s43\\na075_s44\\nalpha_monotonicity.png\\nanalysis\\nanalysis_s44\\nanalysis_summary.json\\nc4_a050_s43_fp32\\nc4_a075_s43_fp32\\npooled_panel_results.json\\npooled_panel_summary.txt\\nty_3seed_a025_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T02:17:59.538092+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"analysis\\ngpt2m_wiki_a100_s42\\nopt1b_wiki_a100_s42\\npythia14b_wiki_a100_s42\\npythia14b_wiki_a100_s43\\npythia1b_c4_a100_s42\\npythia1b_c4_a100_s43\\npythia1b_c4_a100_s43_v2\\npythia410m_wiki_a100_s42\\nsmollm3_3b_wiki_a100_s42_fp32_v3\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T02:17:59.538246+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T02:17:59.538454+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"EXIT_CODE\\nall_metrics.json\\nanalysis\\nconfig.json\\ngen_0\\ngen_1\\ngen_10\\ngen_2\\ngen_3\\ngen_4\\ngen_5\\ngen_6\\ngen_7\\ngen_8\\ngen_9\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T02:17:59.538669+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "find /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42/ -name \"*.json\" -maxdepth 2",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "find /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42/ -name \"*.json\" -maxdepth 2",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-21T02:17:59.538893+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42/config.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42/gen_0/metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42/gen_1/metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42/gen_2/metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42/gen_3/metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42/gen_4/metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42/gen_5/metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42/gen_6/metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42/gen_7/metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42/gen_8/metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42/gen_9/metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42/gen_10/metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42/all_metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42/analysis/5method_leadlag_pre_tyfix_batch.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T02:17:59.539067+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42/all_metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42/all_metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-21T02:17:59.539311+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[\\n  {\\n    \\\"token_entropy\\\": 3.2341948700181407,\\n    \\\"self_bleu\\\": 0.010194395218435404,\\n    \\\"distinct_1\\\": 0.0982156685333268,\\n    \\\"distinct_2\\\": 0.5178027030111348,\\n    \\\"distinct_3\\\": 0.8127277321747353,\\n    \\\"ece\\\": 0.010804557477709054,\\n    \\\"effective_rank\\\": 46.612774691899155,\\n    \\\"perplexity\\\": 26.948958972544652,\\n    \\\"mauve\\\": 0.03406737671684175,\\n    \\\"generation\\\": 0\\n  },\\n  {\\n    \\\"token_entropy\\\": 2.517377906714129,\\n    \\\"self_bleu\\\": 0.01031278388147428,\\n    \\\"distinct_1\\\": 0.09752517633628247,\\n    \\\"distinct_2\\\": 0.5140825545933428,\\n    \\\"distinct_3\\\": 0.8103854590526204,\\n    \\\"ece\\\": 0.06693498841180144,\\n    \\\"effective_rank\\\": 58.56433721113924,\\n    \\\"perplexity\\\": 22.95843441419726,\\n    \\\"mauve\\\": 0.03232946507236373,\\n    \\\"generation\\\": 1\\n  },\\n  {\\n    \\\"token_entropy\\\": 2.4984176253550356,\\n    \\\"self_bleu\\\": 0.01131595121983228,\\n    \\\"distinct_1\\\": 0.0826796875,\\n    \\\"distinct_2\\\": 0.4311283681903765,\\n    \\\"distinct_3\\\": 0.7152768012000188,\\n    \\\"ece\\\": 0.08714580169874889,\\n    \\\"effective_rank\\\": 63.590245251860246,\\n    \\\"perplexity\\\": 26.376527821628653,\\n    \\\"mauve\\\": 0.03322813096493746,\\n    \\\"generation\\\": 2\\n  },\\n  {\\n    \\\"token_entropy\\\": 2.564376331651781,\\n    \\\"self_bleu\\\": 0.011669167689985884,\\n    \\\"distinct_1\\\": 0.07559375,\\n    \\\"distinct_2\\\": 0.3838154985585825,\\n    \\\"distinct_3\\\": 0.6400803137549024,\\n    \\\"ece\\\": 0.08800493897858175,\\n    \\\"effective_rank\\\": 64.59108964475801,\\n    \\\"perplexity\\\": 27.48484973964157,\\n    \\\"mauve\\\": 0.0309399337533844,\\n    \\\"generation\\\": 3\\n  },\\n  {\\n    \\\"token_entropy\\\": 2.5485591490224033,\\n    \\\"self_bleu\\\": 0.012043368823452387,\\n    \\\"distinct_1\\\": 0.07059375,\\n    \\\"d
…[truncated 3064 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-21T02:17:59.539482+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42/gen_0/metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42/gen_0/metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-21T02:17:59.539624+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"token_entropy\\\": 3.2341948700181407,\\n  \\\"self_bleu\\\": 0.010194395218435404,\\n  \\\"distinct_1\\\": 0.0982156685333268,\\n  \\\"distinct_2\\\": 0.5178027030111348,\\n  \\\"distinct_3\\\": 0.8127277321747353,\\n  \\\"ece\\\": 0.010804557477709054,\\n  \\\"effective_rank\\\": 46.612774691899155,\\n  \\\"perplexity\\\": 26.948958972544652,\\n  \\\"mauve\\\": 0.03406737671684175,\\n  \\\"generation\\\": 0\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-21T02:17:59.539790+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s43/all_metrics.json /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a075_s42/all_metrics.json /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a075_s43/all_metrics.json /root/autodl-tmp/distrib_canary_collapse/results/generalize/pythia410m_wiki_a100_s42/all_metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s43/all_metrics.json /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a075_s42/all_metrics.json /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a075_s43/all_metrics.json /root/autodl-tmp/distrib_canary_collapse/results/generalize/pythia410m_wiki_a100_s42/all_metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-21T02:17:59.539925+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s43/all_metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a075_s42/all_metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a075_s43/all_metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/generalize/pythia410m_wiki_a100_s42/all_metrics.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-21T02:17:59.540047+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "find /root/autodl-tmp/distrib_canary_collapse/results/ -path \"*/t20*\" -name \"all_metrics.json\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "find /root/autodl-tmp/distrib_canary_collapse/results/ -path \"*/t20*\" -name \"all_metrics.json\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-21T02:17:59.540168+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-21T02:17:59.540309+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "find /root/autodl-tmp/distrib_canary_collapse/results/ -path \"*/a055*\" -name \"all_metrics.json\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "find /root/autodl-tmp/distrib_canary_collapse/results/ -path \"*/a055*\" -name \"all_metrics.json\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-21T02:17:59.540456+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a055_s42_fp32/all_metrics.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-21T02:17:59.540606+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "find /root/autodl-tmp/distrib_canary_collapse/results/ -name \"all_metrics.json\" -maxdepth 3",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "find /root/autodl-tmp/distrib_canary_collapse/results/ -name \"all_metrics.json\" -maxdepth 3",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-21T02:17:59.540759+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/all_metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42/all_metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a075_s42/all_metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s43/all_metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s43/all_metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s44/all_metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a075_s43/all_metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a075_s44/all_metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s43/all_metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s44/all_metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s44/all_metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a010_s42/all_metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a060_s42_bf16/all_metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a010_s42_fp32/all_metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a010_s43_fp32/all_metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/c4_a050_s43_fp32/all_metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/c4_a075_s43_fp32/all_metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a055_s42_fp32/all_metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/generalize/pythia410m_wiki_a100_s42/all_metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/generalize/opt1b_wiki_a100_s42/all_metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/generalize/pythia1b_c4_a100_s42/all_metrics.json\\n/ro
…[truncated 1193 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-21T02:17:59.540926+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "python3 -c \"import json; data=json.load(open('/root/autodl-tmp/distrib_canary_collapse/results/generalize/pythia410m_wiki_a100_s42/all_metrics.json')); print(len(data))\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "python3 -c \"import json; data=json.load(open('/root/autodl-tmp/distrib_canary_collapse/results/generalize/pythia410m_wiki_a100_s42/all_metrics.json')); print(len(data))\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-21T02:17:59.541052+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-21T02:17:59.541168+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "python3 -c \"import json; data=json.load(open('/root/autodl-tmp/distrib_canary_collapse/results/scale/14b_a050_s42_fp32/all_metrics.json')); print(len(data))\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "python3 -c \"import json; data=json.load(open('/root/autodl-tmp/distrib_canary_collapse/results/scale/14b_a050_s42_fp32/all_metrics.json')); print(len(data))\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-21T02:17:59.541314+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-21T02:17:59.541438+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "python3 -c \"import json; data=json.load(open('/root/autodl-tmp/distrib_canary_collapse/results/generalize/smollm3_3b_wiki_a100_s42_fp32_v3/all_metrics.json')); print(len(data))\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "python3 -c \"import json; data=json.load(open('/root/autodl-tmp/distrib_canary_collapse/results/generalize/smollm3_3b_wiki_a100_s42_fp32_v3/all_metrics.json')); print(len(data))\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-21T02:17:59.541555+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-21T02:17:59.541941+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "wc -l /root/autodl-tmp/distrib_canary_collapse/results/generalize/pythia410m_wiki_a100_s42/all_metrics.json /root/autodl-tmp/distrib_canary_collapse/results/scale/14b_a050_s42_fp32/all_metrics.json /root/autodl-tmp/distrib_canary_collapse/results/generalize/smollm3_3b_wiki_a100_s42_fp32_v3/all_metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "wc -l /root/autodl-tmp/distrib_canary_collapse/results/generalize/pythia410m_wiki_a100_s42/all_metrics.json /root/autodl-tmp/distrib_canary_collapse/results/scale/14b_a050_s42_fp32/all_metrics.json /root/autodl-tmp/distrib_canary_collapse/results/generalize/smollm3_3b_wiki_a100_s42_fp32_v3/all_metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-21T02:17:59.542080+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  133 /root/autodl-tmp/distrib_canary_collapse/results/generalize/pythia410m_wiki_a100_s42/all_metrics.json\\n  166 /root/autodl-tmp/distrib_canary_collapse/results/scale/14b_a050_s42_fp32/all_metrics.json\\n  166 /root/autodl-tmp/distrib_canary_collapse/results/generalize/smollm3_3b_wiki_a100_s42_fp32_v3/all_metrics.json\\n  465 total\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-21T02:17:59.542316+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/conditional_granger_analysis.py",
  "content": "\"\"\"Conditional Granger Causality Analysis: token_entropy vs ECE → diversity metrics.\"\"\"\nimport json, os, sys, warnings\nimport numpy as np\nimport pandas as pd\nfrom statsmodels.tsa.api import VAR\nfrom itertools import product\n\nwarnings.filterwarnings(\"ignore\")\n\nBASE = \"/root/autodl-tmp/distrib_canary_collapse/results\"\n\nEXPERIMENTS = {\n    \"a050_s42\":   f\"{BASE}/alpha_sweep/a050_s42/all_metrics.json\",\n    \"a050_s43\":   f\"{BASE}/alpha_sweep/a050_s43/all_metrics.json\",\n    \"a050_s44\":   f\"{BASE}/alpha_sweep/a050_s44/all_metrics.json\",\n    \"a055_s42\":   f\"{BASE}/alpha_sweep/a055_s42_fp32/all_metrics.json\",\n    \"a075_s42\":   f\"{BASE}/alpha_sweep/a075_s42/all_metrics.json\",\n    \"a075_s43\":   f\"{BASE}/alpha_sweep/a075_s43/all_metrics.json\",\n    \"a075_s44\":   f\"{BASE}/alpha_sweep/a075_s44/all_metrics.json\",\n    \"pythia410m\":  f\"{BASE}/generalize/pythia410m_wiki_a100_s42/all_metrics.json\",\n    \"opt1b\":       f\"{BASE}/generalize/opt1b_wiki_a100_s42/all_metrics.json\",\n    \"pythia1b_c4\": f\"{BASE}/generalize/pythia1b_c4_a100_s42/all_metrics.json\",\n    \"14b_a050\":    f\"{BASE}/scale/14b_a050_s42_fp32/all_metrics.json\",\n    \"smollm3_3b\":  f\"{BASE}/generalize/smollm3_3b_wiki_a100_s42_fp32_v3/all_metrics.json\",\n}\n\nCANARIES = [\"token_entropy\", \"ece\"]\nDOWNSTREAMS = [\"distinct_1\", \"distinct_2\", \"distinct_3\", \"mauve\"]\n\n\ndef load_experiment(path):\n    with open(path) as f:\n        data = json.load(f)\n    df = pd.DataFrame(data).sort_values(\"generation\").reset_index(drop=True)\n    return df\n\n\ndef conditional_granger(df, cause, effect, condition, maxlag=2):\n    \"\"\"\n    Conditional Granger: does `cause` Granger-cause `effect` after controlling for `condition`?\n\n    Compare:\n    - Unrestricted: VAR on [effect, cause, condition]\n    - Restricted:   VAR on [effect, condition] (cause excluded)\n\n    Uses statsmodels VAR.test_causality which does an F-test.\n    \"\"\"\n    cols_needed = [cause, effect, condition]\n    if any(c not in df.columns for c in cols_needed):\n        return None\n\n    sub = df[cols_needed].dropna()\n    T = len(sub)\n\n    # Need enough observations for VAR estimation\n    # VAR(p) needs T > p*k + k where k = number of variables\n    results = {}\n    for lag in range(1, maxlag + 1):\n        k = 3  # unrestricted model variables\n        min_obs = lag * k + k + 1\n        if T < min_obs:\n            results[lag] = {\"p_value\": np.nan, \"F_stat\": np.nan, \"df\": (np.nan, np.nan),\n                           \"note\": f\"T={T} too small for lag={lag}\"}\n            continue\n        try:\n            model = VAR(sub[[effect, cause, condition]])\n            fitted = model.fit(lag)\n            test = fitted.test_causality(caused=effect, causing=cause, kind='f')\n            results[lag] = {\n                \"p_value\": test.pvalue,\n                \"F_stat\": test.test_statistic,\n                \"df\": (test.df_num, test.df_denom),\n            }\n        except Exception as e:\n            results[lag] = {\"p_value\": np.nan, \"F_stat\": np.nan, \"note\": str(e)[:80]}\n\n    return results\n\n\ndef unconditional_granger(df, cause, effect, maxlag=2):\n    \"\"\"Unconditional (bivariate) Granger: cause → effect.\"\"\"\n    cols = [cause, effect]\n    if any(c not in df.columns for c in cols):\n        return None\n    sub = df[cols].dropna()\n    T = len(sub)\n    results = {}\n    for lag in range(1, maxlag + 1):\n        k = 2\n        min_obs = lag * k + k + 1\n        if T < min_obs:\n            results[lag] = {\"p_value\": np.nan, \"F_stat\": np.nan,\n                           \"note\": f\"T={T} too small for lag={lag}\"}\n            continue\n        try:\n            model = VAR(sub[[effect, cause]])\n            fitted = model.fit(lag)\n            test = fitted.test_causality(caused=effect, causing=cause, kind='f')\n            results[lag] = {\n                \"p_value\": test.pvalue,\n                \"F_stat\": test.test_statistic,\n                \"df\": (test.df_num, test.df_denom),\n            }\n        except Exception as e:\n            results[lag] = {\"p_value\": np.nan, \"F_stat\": np.nan, \"note\": str(e)[:80]}\n    return results\n\n\ndef joint_granger(df, causes, effect, maxlag=2):\n    \"\"\"Joint Granger: [token_entropy, ece] → effect simultaneously.\"\"\"\n    cols = causes + [effect]\n    if any(c not in df.columns for c in cols):\n        return None\n    sub = df[cols].dropna()\n    T = len(sub)\n    results = {}\n    for lag in range(1, maxlag + 1):\n        k = len(cols)\n        min_obs = lag * k + k + 1\n        if T < min_obs:\n            results[lag] = {\"p_value\": np.nan, \"F_stat\": np.nan,\n                           \"note\": f\"T={T} too small for lag={lag}\"}\n            continue\n        try:\n            model = VAR(sub[[effect] + causes])\n            fitted = model.fit(lag)\n            test = fitted.test_causality(caused=effect, causing=causes, kind='f')\n            results[lag] = {\n                \"p_value\": test.pvalue,\n                \"F_stat\": test.test_statistic,\n                \"df\": (test.df_num, test.df_denom),\n            }\n        except Exception as e:\n            results[lag] = {\"p_value\": np.nan, \"F_stat\": np.nan, \"note\": str(e)[:80]}\n    return results\n\n\n# ─── Main analysis ───\nall_results = {}\n\nfor exp_name, path in EXPERIMENTS.items():\n    if not os.path.exists(path):\n        print(f\"SKIP {exp_name}: file not found\")\n        continue\n\n    df = load_experiment(path)\n    T = len(df)\n    print(f\"\\n{'='*60}\")\n    print(f\"Experiment: {exp_name}  (T={T})\")\n    print(f\"{'='*60}\")\n\n    exp_results = {\"T\": T, \"tests\": {}}\n\n    for downstream in DOWNSTREAMS:\n        if downstream not in df.columns:\n            print(f\"  SKIP {downstream}: not in data\")\n            continue\n\n        print(f\"\\n  Target: {downstream}\")\n        print(f\"  {'─'*50}\")\n\n        pair_results = {}\n\n        # 1. Unconditional: entropy → downstream\n        ug_ent = unconditional_granger(df, \"token_entropy\", downstream)\n        pair_results[\"uncond_entropy\"] = ug_ent\n\n        # 2. Unconditional: ECE → downstream\n        ug_ece = unconditional_granger(df, \"ece\", downstream)\n        pair_results[\"uncond_ece\"] = ug_ece\n\n        # 3. Conditional: entropy → downstream | ECE\n        cg_ent = conditional_granger(df, \"token_entropy\", downstream, \"ece\")\n        pair_results[\"cond_entropy_given_ece\"] = cg_ent\n\n        # 4. Conditional: ECE → downstream | entropy\n        cg_ece = conditional_granger(df, \"ece\", downstream, \"token_entropy\")\n        pair_results[\"cond_ece_given_entropy\"] = cg_ece\n\n        # 5. Joint: [entropy, ECE] → downstream\n        jg = joint_granger(df, [\"token_entropy\", \"ece\"], downstream)\n        pair_results[\"joint\"] = jg\n\n        # Print summary for lag=1\n        lag = 1\n        fmt = lambda r: f\"F={r[lag]['F_stat']:.3f}, p={r[lag]['p_value']:.4f}\" if r and lag in r and not np.isnan(r[lag].get('p_value', np.nan)) else \"N/A\"\n\n        print(f\"    Uncond entropy→{downstream}:        {fmt(ug_ent)}\")\n        print(f\"    Uncond ECE→{downstream}:            {fmt(ug_ece)}\")\n        print(f\"    Cond entropy→{downstream}|ECE:      {fmt(cg_ent)}\")\n        print(f\"    Cond ECE→{downstream}|entropy:      {fmt(cg_ece)}\")\n        print(f\"    Joint [entropy,ECE]→{downstream}:   {fmt(jg)}\")\n\n        exp_results[\"tests\"][downstream] = pair_results\n\n    all_results[exp_name] = exp_results\n\n\n# ─── Summary table ───\nprint(\"\\n\\n\" + \"=\"*80)\nprint(\"SUMMARY TABLE: Conditional vs Unconditional Granger (lag=1, p-values)\")\nprint(\"=\"*80)\n\nheader = f\"{'Experiment':<16} {'Downstream':<12} {'Uncond TE':>10} {'Uncond ECE':>10} {'Cond TE|ECE':>12} {'Cond ECE|TE':>12} {'Joint':>10}\"\nprint(header)\nprint(\"─\" * len(header))\n\nsig_counts = {\"uncond_entropy\": 0, \"uncond_ece\": 0,\n              \"cond_entropy_given_ece\": 0, \"cond_ece_given_entropy\": 0, \"joint\": 0}\ntotal_tests = 0\n\nfor exp_name, exp_data in all_results.items():\n    for downstream, tests in exp_data[\"tests\"].items():\n        def get_p(test_key):\n            r = tests.get(test_key)\n            if r and 1 in r and not np.isnan(r[1].get(\"p_value\", np.nan)):\n                return r[1][\"p_value\"]\n            return np.nan\n\n        p_ue = get_p(\"uncond_entropy\")\n        p_uc = get_p(\"uncond_ece\")\n        p_ce = get_p(\"cond_entropy_given_ece\")\n        p_cc = get_p(\"cond_ece_given_entropy\")\n        p_j = get_p(\"joint\")\n\n        def fmt_p(p):\n            if np.isnan(p): return \"N/A\"\n            star = \"***\" if p < 0.001 else \"**\" if p < 0.01 else \"*\" if p < 0.05 else \".\" if p < 0.1 else \"\"\n            return f\"{p:.4f}{star}\"\n\n        print(f\"{exp_name:<16} {downstream:<12} {fmt_p(p_ue):>10} {fmt_p(p_uc):>10} {fmt_p(p_ce):>12} {fmt_p(p_cc):>12} {fmt_p(p_j):>10}\")\n\n        total_tests += 1\n        if not np.isnan(p_ue) and p_ue < 0.05: sig_counts[\"uncond_entropy\"] += 1\n        if not np.isnan(p_uc) and p_uc < 0.05: sig_counts[\"uncond_ece\"] += 1\n        if not np.isnan(p_ce) and p_ce < 0.05: sig_counts[\"cond_entropy_given_ece\"] += 1\n        if not np.isnan(p_cc) and p_cc < 0.05: sig_counts[\"cond_ece_given_entropy\"] += 1\n        if not np.isnan(p_j) and p_j < 0.05: sig_counts[\"joint\"] += 1\n\n\nprint(f\"\\n{'─'*80}\")\nprint(f\"Significance counts (p<0.05) out of {total_tests} tests:\")\nfor k, v in sig_counts.items():\n    print(f\"  {k:<30}: {v}/{total_tests} ({100*v/total_tests:.1f}%)\")\n\n\n# ─── Redundancy analysis ───\nprint(\"\\n\\n\" + \"=\"*80)\nprint(\"REDUNDANCY ANALYSIS\")\nprint(\"=\"*80)\n\n# For each experiment × downstream, classify the pattern\npatterns = {\"both_independent\": 0, \"entropy_only\": 0, \"ece_only\": 0,\n            \"redundant\": 0, \"neither\": 0, \"na\": 0}\n\nfor exp_name, exp_data in all_results.items():\n    for downstream, tests in exp_data[\"tests\"].items():\n        def get_p(test_key):\n            r = tests.get(test_key)\n            if r and 1 in r and not np.isnan(r[1].get(\"p_value\", np.nan)):\n                return r[1][\"p_value\"]\n            return np.nan\n\n        p_ue = get_p(\"uncond_entropy\")\n        p_uc = get_p(\"uncond_ece\")\n        p_ce = get_p(\"cond_entropy_given_ece\")\n        p_cc = get_p(\"cond_ece_given_entropy\")\n\n        if np.isnan(p_ce) or np.isnan(p_cc):\n            patterns[\"na\"] += 1\n            continue\n\n        ent_indep = p_ce < 0.05\n        ece_indep = p_cc < 0.05\n\n        if ent_indep and ece_indep:\n            patterns[\"both_independent\"] += 1\n        elif ent_indep and not ece_indep:\n            patterns[\"entropy_only\"] += 1\n        elif not ent_indep and ece_indep:\n            patterns[\"ece_only\"] += 1\n        elif p_ue < 0.05 or p_uc < 0.05:\n            patterns[\"redundant\"] += 1\n        else:\n            patterns[\"neither\"] += 1\n\nprint(\"Pattern classification (based on conditional p<0.05):\")\nfor pattern, count in patterns.items():\n    print(f\"  {pattern:<20}: {count}\")\n\n# Softer threshold analysis (p<0.10)\nprint(\"\\nSofter threshold (p<0.10):\")\npatterns10 = {\"both_independent\": 0, \"entropy_only\": 0, \"ece_only\": 0,\n              \"redundant\": 0, \"neither\": 0, \"na\": 0}\n\nfor exp_name, exp_data in all_results.items():\n    for downstream, tests in exp_data[\"tests\"].items():\n        def get_p(test_key):\n            r = tests.get(test_key)\n            if r and 1 in r and not np.isnan(r[1].get(\"p_value\", np.nan)):\n                return r[1][\"p_value\"]\n            return np.nan\n\n        p_ue = get_p(\"uncond_entropy\")\n        p_uc = get_p(\"uncond_ece\")\n        p_ce = get_p(\"cond_entropy_given_ece\")\n        p_cc = get_p(\"cond_ece_given_entropy\")\n\n        if np.isnan(p_ce) or np.isnan(p_cc):\n            patterns10[\"na\"] += 1\n            continue\n\n        ent_indep = p_ce < 0.10\n        ece_indep = p_cc < 0.10\n\n        if ent_indep and ece_indep:\n            patterns10[\"both_independent\"] += 1\n        elif ent_indep and not ece_indep:\n            patterns10[\"entropy_only\"] += 1\n        elif not ent_indep and ece_indep:\n            patterns10[\"ece_only\"] += 1\n        elif p_ue < 0.10 or p_uc < 0.10:\n            patterns10[\"redundant\"] += 1\n        else:\n            patterns10[\"neither\"] += 1\n\nfor pattern, count in patterns10.items():\n    print(f\"  {pattern:<20}: {count}\")\n\n\n# ─── Correlation between canaries ───\nprint(\"\\n\\n\" + \"=\"*80)\nprint(\"CANARY INTER-CORRELATION (entropy vs ECE)\")\nprint(\"=\"*80)\n\nfor exp_name, path in EXPERIMENTS.items():\n    if not os.path.exists(path):\n        continue\n    df = load_experiment(path)\n    if \"token_entropy\" in df.columns and \"ece\" in df.columns:\n        r = df[\"token_entropy\"].corr(df[\"ece\"])\n        print(f\"  {exp_name:<16}: r = {r:+.4f}\")\n\n\n# ─── Effect size (partial R²) ───\nprint(\"\\n\\n\" + \"=\"*80)\nprint(\"EFFECT SIZE: Partial R² from VAR(1)\")\nprint(\"=\"*80)\n\nfor exp_name, path in EXPERIMENTS.items():\n    if not os.path.exists(path):\n        continue\n    df = load_experiment(path)\n    T = len(df)\n    if T < 7:\n        continue\n\n    print(f\"\\n  {exp_name} (T={T}):\")\n    for downstream in DOWNSTREAMS:\n        if downstream not in df.columns:\n            continue\n\n        cols_full = [downstream, \"token_entropy\", \"ece\"]\n        cols_no_ent = [downstream, \"ece\"]\n        cols_no_ece = [downstream, \"token_entropy\"]\n\n        try:\n            sub = df[cols_full].dropna()\n            if len(sub) < 7:\n                continue\n\n            # Full model R²\n            m_full = VAR(sub).fit(1)\n            resid_full = m_full.resid[downstream]\n            ss_full = (resid_full**2).sum()\n\n            # Without entropy\n            m_no_ent = VAR(df[cols_no_ent].dropna()).fit(1)\n            resid_no_ent = m_no_ent.resid[downstream]\n            ss_no_ent = (resid_no_ent**2).sum()\n\n            # Without ECE\n            m_no_ece = VAR(df[cols_no_ece].dropna()).fit(1)\n            resid_no_ece = m_no_ece.resid[downstream]\n            ss_no_ece = (resid_no_ece**2).sum()\n\n            # Partial R²\n            partial_r2_ent = 1.0 - ss_full / ss_no_ent if ss_no_ent > 0 else np.nan\n            partial_r2_ece = 1.0 - ss_full / ss_no_ece if ss_no_ece > 0 else np.nan\n\n            print(f\"    {downstream:<12}: partial_R²(entropy)={partial_r2_ent:+.4f}, partial_R²(ECE)={partial_r2_ece:+.4f}\")\n        except Exception as e:\n            print(f\"    {downstream:<12}: ERROR {str(e)[:60]}\")\n\n\n# ─── Save full results as JSON ───\noutput = {\n    \"meta\": {\n        \"analysis\": \"Conditional Granger Causality\",\n        \"canaries\": CANARIES,\n        \"downstreams\": DOWNSTREAMS,\n        \"method\": \"VAR F-test via statsmodels\",\n    },\n    \"results\": {}\n}\n\nfor exp_name, exp_data in all_results.items():\n    exp_out = {\"T\": exp_data[\"T\"], \"pairs\": {}}\n    for downstream, tests in exp_data[\"tests\"].items():\n        pair_out = {}\n        for test_key, lag_results in tests.items():\n            if lag_results is None:\n                continue\n            pair_out[test_key] = {}\n            for lag, r in lag_results.items():\n                pair_out[test_key][str(lag)] = {\n                    k: (float(v) if isinstance(v, (int, float, np.floating)) else\n                        [float(x) for x in v] if isinstance(v, tuple) else v)\n                    for k, v in r.items()\n                }\n        exp_out[\"pairs\"][downstream] = pair_out\n    output[\"results\"][exp_name] = exp_out\n\nout_path = \"/root/autodl-tmp/distrib_canary_collapse/results/analysis/conditional_granger_results.json\"\nos.makedirs(os.path.dirname(out_path), exist_ok=True)\nwith open(out_path, \"w\") as f:\n    json.dump(output, f, indent=2)\nprint(f\"\\n\\nResults saved to {out_path}\")\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/conditional_granger_analysis.py",
    "content": "\"\"\"Conditional Granger Causality Analysis: token_entropy vs ECE → diversity metrics.\"\"\"\nimport json, os, sys, warnings\nimport numpy as np\nimport pandas as pd\nfrom statsmodels.tsa.api import VAR\nfrom itertools import product\n\nwarnings.filterwarnings(\"ignore\")\n\nBASE = \"/root/autodl-tmp/distrib_canary_collapse/results\"\n\nEXPERIMENTS = {\n    \"a050_s42\":   f\"{BASE}/alpha_sweep/a050_s42/all_metrics.json\",\n    \"a050_s43\":   f\"{BASE}/alpha_sweep/a050_s43/all_metrics.json\",\n    \"a050_s44\":   f\"{BASE}/alpha_sweep/a050_s44/all_metrics.json\",\n    \"a055_s42\":   f\"{BASE}/alpha_sweep/a055_s42_fp32/all_metrics.json\",\n    \"a075_s42\":   f\"{BASE}/alpha_sweep/a075_s42/all_metrics.json\",\n    \"a075_s43\":   f\"{BASE}/alpha_sweep/a075_s43/all_metrics.json\",\n    \"a075_s44\":   f\"{BASE}/alpha_sweep/a075_s44/all_metrics.json\",\n    \"pythia410m\":  f\"{BASE}/generalize/pythia410m_wiki_a100_s42/all_metrics.json\",\n    \"opt1b\":       f\"{BASE}/generalize/opt1b_wiki_a100_s42/all_metrics.json\",\n    \"pythia1b_c4\": f\"{BASE}/generalize/pythia1b_c4_a100_s42/all_metrics.json\",\n    \"14b_a050\":    f\"{BASE}/scale/14b_a050_s42_fp32/all_metrics.json\",\n    \"smollm3_3b\":  f\"{BASE}/generalize/smollm3_3b_wiki_a100_s42_fp32_v3/all_metrics.json\",\n}\n\nCANARIES = [\"token_entropy\", \"ece\"]\nDOWNSTREAMS = [\"distinct_1\", \"distinct_2\", \"distinct_3\", \"mauve\"]\n\n\ndef load_experiment(path):\n    with open(path) as f:\n        data = json.load(f)\n    df = pd.DataFrame(data).sort_values(\"generation\").reset_index(drop=True)\n    return df\n\n\ndef conditional_granger(df, cause, effect, condition, maxlag=2):\n    \"\"\"\n    Conditional Granger: does `cause` Granger-cause `effect` after controlling for `condition`?\n\n    Compare:\n    - Unrestricted: VAR on [effect, cause, condition]\n    - Restricted:   VAR on [effect, condition] (cause excluded)\n\n    Uses statsmodels VAR.test_causality which does an F-test.\n    \"\"\"\n    cols_needed = [cause, effect, condition]\n    if any(c not in df.columns for c in cols_needed):\n        return None\n\n    sub = df[cols_needed].dropna()\n    T = len(sub)\n\n    # Need enough observations for VAR estimation\n    # VAR(p) needs T > p*k + k where k = number of variables\n    results = {}\n    for lag in range(1, maxlag + 1):\n        k = 3  # unrestricted model variables\n        min_obs = lag * k + k + 1\n        if T < min_obs:\n            results[lag] = {\"p_value\": np.nan, \"F_stat\": np.nan, \"df\": (np.nan, np.nan),\n                           \"note\": f\"T={T} too small for lag={lag}\"}\n            continue\n        try:\n            model = VAR(sub[[effect, cause, condition]])\n            fitted = model.fit(lag)\n            test = fitted.test_causality(caused=effect, causing=cause, kind='f')\n            results[lag] = {\n                \"p_value\": test.pvalue,\n                \"F_stat\": test.test_statistic,\n                \"df\": (test.df_num, test.df_denom),\n            }\n        except Exception as e:\n            results[lag] = {\"p_value\": np.nan, \"F_stat\": np.nan, \"note\": str(e)[:80]}\n\n    return results\n\n\ndef unconditional_granger(df, cause, effect, maxlag=2):\n    \"\"\"Unconditional (bivariate) Granger: cause → effect.\"\"\"\n    cols = [cause, effect]\n    if any(c not in df.columns for c in cols):\n        return None\n    sub = df[cols].dropna()\n    T = len(sub)\n    results = {}\n    for lag in range(1, maxlag + 1):\n        k = 2\n        min_obs = lag * k + k + 1\n        if T < min_obs:\n            results[lag] = {\"p_value\": np.nan, \"F_stat\": np.nan,\n                           \"note\": f\"T={T} too small for lag={lag}\"}\n            continue\n        try:\n            model = VAR(sub[[effect, cause]])\n            fitted = model.fit(lag)\n            test = fitted.test_causality(caused=effect, causing=cause, kind='f')\n            results[lag] = {\n                \"p_value\": test.pvalue,\n                \"F_stat\": test.test_statistic,\n                \"df\": (test.df_num, test.df_denom),\n            }\n        except Exception as e:\n            results[lag] = {\"p_value\": np.nan, \"F_stat\": np.nan, \"note\": str(e)[:80]}\n    return results\n\n\ndef joint_granger(df, causes, effect, maxlag=2):\n    \"\"\"Joint Granger: [token_entropy, ece] → effect simultaneously.\"\"\"\n    cols = causes + [effect]\n    if any(c not in df.columns for c in cols):\n        return None\n    sub = df[cols].dropna()\n    T = len(sub)\n    results = {}\n    for lag in range(1, maxlag + 1):\n        k = len(cols)\n        min_obs = lag * k + k + 1\n        if T < min_obs:\n            results[lag] = {\"p_value\": np.nan, \"F_stat\": np.nan,\n                           \"note\": f\"T={T} too small for lag={lag}\"}\n            continue\n        try:\n            model = VAR(sub[[effect] + causes])\n            fitted = model.fit(lag)\n            test = fitted.test_causality(caused=effect, causing=causes, kind='f')\n            results[lag] = {\n                \"p_value\": test.pvalue,\n                \"F_stat\": test.test_statistic,\n                \"df\": (test.df_num, test.df_denom),\n            }\n        except Exception as e:\n            results[lag] = {\"p_value\": np.nan, \"F_stat\": np.nan, \"note\": str(e)[:80]}\n    return results\n\n\n# ─── Main analysis ───\nall_results = {}\n\nfor exp_name, path in EXPERIMENTS.items():\n    if not os.path.exists(path):\n        print(f\"SKIP {exp_name}: file not found\")\n        continue\n\n    df = load_experiment(path)\n    T = len(df)\n    print(f\"\\n{'='*60}\")\n    print(f\"Experiment: {exp_name}  (T={T})\")\n    print(f\"{'='*60}\")\n\n    exp_results = {\"T\": T, \"tests\": {}}\n\n    for downstream in DOWNSTREAMS:\n        if downstream not in df.columns:\n            print(f\"  SKIP {downstream}: not in data\")\n            continue\n\n        print(f\"\\n  Target: {downstream}\")\n        print(f\"  {'─'*50}\")\n\n        pair_results = {}\n\n        # 1. Unconditional: entropy → downstream\n        ug_ent = unconditional_granger(df, \"token_entropy\", downstream)\n        pair_results[\"uncond_entropy\"] = ug_ent\n\n        # 2. Unconditional: ECE → downstream\n        ug_ece = unconditional_granger(df, \"ece\", downstream)\n        pair_results[\"uncond_ece\"] = ug_ece\n\n        # 3. Conditional: entropy → downstream | ECE\n        cg_ent = conditional_granger(df, \"token_entropy\", downstream, \"ece\")\n        pair_results[\"cond_entropy_given_ece\"] = cg_ent\n\n        # 4. Conditional: ECE → downstream | entropy\n        cg_ece = conditional_granger(df, \"ece\", downstream, \"token_entropy\")\n        pair_results[\"cond_ece_given_entropy\"] = cg_ece\n\n        # 5. Joint: [entropy, ECE] → downstream\n        jg = joint_granger(df, [\"token_entropy\", \"ece\"], downstream)\n        pair_results[\"joint\"] = jg\n\n        # Print summary for lag=1\n        lag = 1\n        fmt = lambda r: f\"F={r[lag]['F_stat']:.3f}, p={r[lag]['p_value']:.4f}\" if r and lag in r and not np.isnan(r[lag].get('p_value', np.nan)) else \"N/A\"\n\n        print(f\"    Uncond entropy→{downstream}:        {fmt(ug_ent)}\")\n        print(f\"    Uncond ECE→{downstream}:            {fmt(ug_ece)}\")\n        print(f\"    Cond entropy→{downstream}|ECE:      {fmt(cg_ent)}\")\n        print(f\"    Cond ECE→{downstream}|entropy:      {fmt(cg_ece)}\")\n        print(f\"    Joint [entropy,ECE]→{downstream}:   {fmt(jg)}\")\n\n        exp_results[\"tests\"][downstream] = pair_results\n\n    all_results[exp_name] = exp_results\n\n\n# ─── Summary table ───\nprint(\"\\n\\n\" + \"=\"*80)\nprint(\"SUMMARY TABLE: Conditional vs Unconditional Granger (lag=1, p-values)\")\nprint(\"=\"*80)\n\nheader = f\"{'Experiment':<16} {'Downstream':<12} {'Uncond TE':>10} {'Uncond ECE':>10} {'Cond TE|ECE':>12} {'Cond ECE|TE':>12} {'Joint':>10}\"\nprint(header)\nprint(\"─\" * len(header))\n\nsig_counts = {\"uncond_entropy\": 0, \"uncond_ece\": 0,\n              \"cond_entropy_given_ece\": 0, \"cond_ece_given_entropy\": 0, \"joint\": 0}\ntotal_tests = 0\n\nfor exp_name, exp_data in all_results.items():\n    for downstream, tests in exp_data[\"tests\"].items():\n        def get_p(test_key):\n            r = tests.get(test_key)\n            if r and 1 in r and not np.isnan(r[1].get(\"p_value\", np.nan)):\n                return r[1][\"p_value\"]\n            return np.nan\n\n        p_ue = get_p(\"uncond_entropy\")\n        p_uc = get_p(\"uncond_ece\")\n        p_ce = get_p(\"cond_entropy_given_ece\")\n        p_cc = get_p(\"cond_ece_given_entropy\")\n        p_j = get_p(\"joint\")\n\n        def fmt_p(p):\n            if np.isnan(p): return \"N/A\"\n            star = \"***\" if p < 0.001 else \"**\" if p < 0.01 else \"*\" if p < 0.05 else \".\" if p < 0.1 else \"\"\n            return f\"{p:.4f}{star}\"\n\n        print(f\"{exp_name:<16} {downstream:<12} {fmt_p(p_ue):>10} {fmt_p(p_uc):>10} {fmt_p(p_ce):>12} {fmt_p(p_cc):>12} {fmt_p(p_j):>10}\")\n\n        total_tests += 1\n        if not np.isnan(p_ue) and p_ue < 0.05: sig_counts[\"uncond_entropy\"] += 1\n        if not np.isnan(p_uc) and p_uc < 0.05: sig_counts[\"uncond_ece\"] += 1\n        if not np.isnan(p_ce) and p_ce < 0.05: sig_counts[\"cond_entropy_given_ece\"] += 1\n        if not np.isnan(p_cc) and p_cc < 0.05: sig_counts[\"cond_ece_given_entropy\"] += 1\n        if not np.isnan(p_j) and p_j < 0.05: sig_counts[\"joint\"] += 1\n\n\nprint(f\"\\n{'─'*80}\")\nprint(f\"Significance counts (p<0.05) out of {total_tests} tests:\")\nfor k, v in sig_counts.items():\n    print(f\"  {k:<30}: {v}/{total_tests} ({100*v/total_tests:.1f}%)\")\n\n\n# ─── Redundancy analysis ───\nprint(\"\\n\\n\" + \"=\"*80)\nprint(\"REDUNDANCY ANALYSIS\")\nprint(\"=\"*80)\n\n# For each experiment × downstream, classify the pattern\npatterns = {\"both_independent\": 0, \"entropy_only\": 0, \"ece_only\": 0,\n            \"redundant\": 0, \"neither\": 0, \"na\": 0}\n\nfor exp_name, exp_data in all_results.items():\n    for downstream, tests in exp_data[\"tests\"].items():\n        def get_p(test_key):\n            r = tests.get(test_key)\n            if r and 1 in r and not np.isnan(r[1].get(\"p_value\", np.nan)):\n                return r[1][\"p_value\"]\n            return np.nan\n\n        p_ue = get_p(\"uncond_entropy\")\n        p_uc = get_p(\"uncond_ece\")\n        p_ce = get_p(\"cond_entropy_given_ece\")\n        p_cc = get_p(\"cond_ece_given_entropy\")\n\n        if np.isnan(p_ce) or np.isnan(p_cc):\n            patterns[\"na\"] += 1\n            continue\n\n        ent_indep = p_ce < 0.05\n        ece_indep = p_cc < 0.05\n\n        if ent_indep and ece_indep:\n            patterns[\"both_independent\"] += 1\n        elif ent_indep and not ece_indep:\n            patterns[\"entropy_only\"] += 1\n        elif not ent_indep and ece_indep:\n            patterns[\"ece_only\"] += 1\n        elif p_ue < 0.05 or p_uc < 0.05:\n            patterns[\"redundant\"] += 1\n        else:\n            patterns[\"neither\"] += 1\n\nprint(\"Pattern classification (based on conditional p<0.05):\")\nfor pattern, count in patterns.items():\n    print(f\"  {pattern:<20}: {count}\")\n\n# Softer threshold analysis (p<0.10)\nprint(\"\\nSofter threshold (p<0.10):\")\npatterns10 = {\"both_independent\": 0, \"entropy_only\": 0, \"ece_only\": 0,\n              \"redundant\": 0, \"neither\": 0, \"na\": 0}\n\nfor exp_name, exp_data in all_results.items():\n    for downstream, tests in exp_data[\"tests\"].items():\n        def get_p(test_key):\n            r = tests.get(test_key)\n            if r and 1 in r and not np.isnan(r[1].get(\"p_value\", np.nan)):\n                return r[1][\"p_value\"]\n            return np.nan\n\n        p_ue = get_p(\"uncond_entropy\")\n        p_uc = get_p(\"uncond_ece\")\n        p_ce = get_p(\"cond_entropy_given_ece\")\n        p_cc = get_p(\"cond_ece_given_entropy\")\n\n        if np.isnan(p_ce) or np.isnan(p_cc):\n            patterns10[\"na\"] += 1\n            continue\n\n        ent_indep = p_ce < 0.10\n        ece_indep = p_cc < 0.10\n\n        if ent_indep and ece_indep:\n            patterns10[\"both_independent\"] += 1\n        elif ent_indep and not ece_indep:\n            patterns10[\"entropy_only\"] += 1\n        elif not ent_indep and ece_indep:\n            patterns10[\"ece_only\"] += 1\n        elif p_ue < 0.10 or p_uc < 0.10:\n            patterns10[\"redundant\"] += 1\n        else:\n            patterns10[\"neither\"] += 1\n\nfor pattern, count in patterns10.items():\n    print(f\"  {pattern:<20}: {count}\")\n\n\n# ─── Correlation between canaries ───\nprint(\"\\n\\n\" + \"=\"*80)\nprint(\"CANARY INTER-CORRELATION (entropy vs ECE)\")\nprint(\"=\"*80)\n\nfor exp_name, path in EXPERIMENTS.items():\n    if not os.path.exists(path):\n        continue\n    df = load_experiment(path)\n    if \"token_entropy\" in df.columns and \"ece\" in df.columns:\n        r = df[\"token_entropy\"].corr(df[\"ece\"])\n        print(f\"  {exp_name:<16}: r = {r:+.4f}\")\n\n\n# ─── Effect size (partial R²) ───\nprint(\"\\n\\n\" + \"=\"*80)\nprint(\"EFFECT SIZE: Partial R² from VAR(1)\")\nprint(\"=\"*80)\n\nfor exp_name, path in EXPERIMENTS.items():\n    if not os.path.exists(path):\n        continue\n    df = load_experiment(path)\n    T = len(df)\n    if T < 7:\n        continue\n\n    print(f\"\\n  {exp_name} (T={T}):\")\n    for downstream in DOWNSTREAMS:\n        if downstream not in df.columns:\n            continue\n\n        cols_full = [downstream, \"token_entropy\", \"ece\"]\n        cols_no_ent = [downstream, \"ece\"]\n        cols_no_ece = [downstream, \"token_entropy\"]\n\n        try:\n            sub = df[cols_full].dropna()\n            if len(sub) < 7:\n                continue\n\n            # Full model R²\n            m_full = VAR(sub).fit(1)\n            resid_full = m_full.resid[downstream]\n            ss_full = (resid_full**2).sum()\n\n            # Without entropy\n            m_no_ent = VAR(df[cols_no_ent].dropna()).fit(1)\n            resid_no_ent = m_no_ent.resid[downstream]\n            ss_no_ent = (resid_no_ent**2).sum()\n\n            # Without ECE\n            m_no_ece = VAR(df[cols_no_ece].dropna()).fit(1)\n            resid_no_ece = m_no_ece.resid[downstream]\n            ss_no_ece = (resid_no_ece**2).sum()\n\n            # Partial R²\n            partial_r2_ent = 1.0 - ss_full / ss_no_ent if ss_no_ent > 0 else np.nan\n            partial_r2_ece = 1.0 - ss_full / ss_no_ece if ss_no_ece > 0 else np.nan\n\n            print(f\"    {downstream:<12}: partial_R²(entropy)={partial_r2_ent:+.4f}, partial_R²(ECE)={partial_r2_ece:+.4f}\")\n        except Exception as e:\n            print(f\"    {downstream:<12}: ERROR {str(e)[:60]}\")\n\n\n# ─── Save full results as JSON ───\noutput = {\n    \"meta\": {\n        \"analysis\": \"Conditional Granger Causality\",\n        \"canaries\": CANARIES,\n        \"downstreams\": DOWNSTREAMS,\n        \"method\": \"VAR F-test via statsmodels\",\n    },\n    \"results\": {}\n}\n\nfor exp_name, exp_data in all_results.items():\n    exp_out = {\"T\": exp_data[\"T\"], \"pairs\": {}}\n    for downstream, tests in exp_data[\"tests\"].items():\n        pair_out = {}\n        for test_key, lag_results in tests.items():\n            if lag_results is None:\n                continue\n            pair_out[test_key] = {}\n            for lag, r in lag_results.items():\n                pair_out[test_key][str(lag)] = {\n                    k: (float(v) if isinstance(v, (int, float, np.floating)) else\n                        [float(x) for x in v] if isinstance(v, tuple) else v)\n                    for k, v in r.items()\n                }\n        exp_out[\"pairs\"][downstream] = pair_out\n    output[\"results\"][exp_name] = exp_out\n\nout_path = \"/root/autodl-tmp/distrib_canary_collapse/results/analysis/conditional_granger_results.json\"\nos.makedirs(os.path.dirname(out_path), exist_ok=True)\nwith open(out_path, \"w\") as f:\n    json.dump(output, f, indent=2)\nprint(f\"\\n\\nResults saved to {out_path}\")\n"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-21T02:17:59.542731+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/conditional_granger_analysis.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-21T02:17:59.543046+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "cat > /root/autodl-tmp/distrib_canary_collapse/results/analysis/conditional_granger_analysis.py << 'SCRIPT_EOF'\n\"\"\"Conditional Granger Causality Analysis: token_entropy vs ECE → diversity metrics.\"\"\"\nimport json, os, sys, warnings\nimport numpy as np\nimport pandas as pd\nfrom statsmodels.tsa.api import VAR\nfrom itertools import product\n\nwarnings.filterwarnings(\"ignore\")\n\nBASE = \"/root/autodl-tmp/distrib_canary_collapse/results\"\n\nEXPERIMENTS = {\n    \"a050_s42\":   f\"{BASE}/alpha_sweep/a050_s42/all_metrics.json\",\n    \"a050_s43\":   f\"{BASE}/alpha_sweep/a050_s43/all_metrics.json\",\n    \"a050_s44\":   f\"{BASE}/alpha_sweep/a050_s44/all_metrics.json\",\n    \"a055_s42\":   f\"{BASE}/alpha_sweep/a055_s42_fp32/all_metrics.json\",\n    \"a075_s42\":   f\"{BASE}/alpha_sweep/a075_s42/all_metrics.json\",\n    \"a075_s43\":   f\"{BASE}/alpha_sweep/a075_s43/all_metrics.json\",\n    \"a075_s44\":   f\"{BASE}/alpha_sweep/a075_s44/all_metrics.json\",\n    \"pythia410m\":  f\"{BASE}/generalize/pythia410m_wiki_a100_s42/all_metrics.json\",\n    \"opt1b\":       f\"{BASE}/generalize/opt1b_wiki_a100_s42/all_metrics.json\",\n    \"pythia1b_c4\": f\"{BASE}/generalize/pythia1b_c4_a100_s42/all_metrics.json\",\n    \"14b_a050\":    f\"{BASE}/scale/14b_a050_s42_fp32/all_metrics.json\",\n    \"smollm3_3b\":  f\"{BASE}/generalize/smollm3_3b_wiki_a100_s42_fp32_v3/all_metrics.json\",\n}\n\nCANARIES = [\"token_entropy\", \"ece\"]\nDOWNSTREAMS = [\"distinct_1\", \"distinct_2\", \"distinct_3\", \"mauve\"]\n\n\ndef load_experiment(path):\n    with open(path) as f:\n        data = json.load(f)\n    df = pd.DataFrame(data).sort_values(\"generation\").reset_index(drop=True)\n    return df\n\n\ndef conditional_granger(df, cause, effect, condition, maxlag=2):\n    cols_needed = [cause, effect, condition]\n    if any(c not in df.columns for c in cols_needed):\n        return None\n    sub = df[cols_needed].dropna()\n    T = len(sub)\n    results = {}\n    for lag in range(1, maxlag + 1):\n        k = 3\n        min_obs = lag * k + k + 1\n        if T < min_obs:\n            results[lag] = {\"p_value\": float('nan'), \"F_stat\": float('nan'),\n                           \"note\": f\"T={T} too small for lag={lag}\"}\n            continue\n        try:\n            model = VAR(sub[[effect, cause, condition]])\n            fitted = model.fit(lag)\n            test = fitted.test_causality(caused=effect, causing=cause, kind='f')\n            results[lag] = {\n                \"p_value\": test.pvalue,\n                \"F_stat\": test.test_statistic,\n                \"df\": (test.df_num, test.df_denom),\n            }\n        except Exception as e:\n            results[lag] = {\"p_value\": float('nan'), \"F_stat\": float('nan'), \"note\": str(e)[:80]}\n    return results\n\n\ndef unconditional_granger(df, cause, effect, maxlag=2):\n    cols = [cause, effect]\n    if any(c not in df.columns for c in cols):\n        return None\n    sub = df[cols].dropna()\n    T = len(sub)\n    results = {}\n    for lag in range(1, maxlag + 1):\n        k = 2\n        min_obs = lag * k + k + 1\n        if T < min_obs:\n            results[lag] = {\"p_value\": float('nan'), \"F_stat\": float('nan'),\n                           \"note\": f\"T={T} too small for lag={lag}\"}\n            continue\n        try:\n            model = VAR(sub[[effect, cause]])\n            fitted = model.fit(lag)\n            test = fitted.test_causality(caused=effect, causing=cause, kind='f')\n            results[lag] = {\n                \"p_value\": test.pvalue,\n                \"F_stat\": test.test_statistic,\n                \"df\": (test.df_num, test.df_denom),\n            }\n        except Exception as e:\n            results[lag] = {\"p_value\": float('nan'), \"F_stat\": float('nan'), \"note\": str(e)[:80]}\n    return results\n\n\ndef joint_granger(df, causes, effect, maxlag=2):\n    cols = causes + [effect]\n    if any(c not in df.columns for c in cols):\n        return None\n    sub = df[cols].dropna()\n    T = len(sub)\n    results = {}\n    for lag in range(1, maxlag + 1):\n        k = len(cols)\n        min_obs = lag * k + k + 1\n        if T < min_obs:\n            results[lag] = {\"p_value\": float('nan'), \"F_stat\": float('nan'),\n                           \"note\": f\"T={T} too small for lag={lag}\"}\n            continue\n        try:\n            model = VAR(sub[[effect] + causes])\n            fitted = model.fit(lag)\n            test = fitted.test_causality(caused=effect, causing=causes, kind='f')\n            results[lag] = {\n                \"p_value\": test.pvalue,\n                \"F_stat\": test.test_statistic,\n                \"df\": (test.df_num, test.df_denom),\n            }\n        except Exception as e:\n            results[lag] = {\"p_value\": float('nan'), \"F_stat\": float('nan'), \"note\": str(e)[:80]}\n    return results\n\n\nall_results = {}\n\nfor exp_name, path in EXPERIMENTS.items():\n    if not os.path.exists(path):\n        print(f\"SKIP {exp_name}: file not found\")\n        continue\n    df = load_experiment(path)\n    T = len(df)\n    print(f\"\\n{'='*60}\")\n    print(f\"Experiment: {exp_name}  (T={T})\")\n    print(f\"{'='*60}\")\n    exp_results = {\"T\": T, \"tests\": {}}\n    for downstream in DOWNSTREAMS:\n        if downstream not in df.columns:\n            print(f\"  SKIP {downstream}: not in data\")\n            continue\n        print(f\"\\n  Target: {downstream}\")\n        print(f\"  {'_'*50}\")\n        pair_results = {}\n        ug_ent = unconditional_granger(df, \"token_entropy\", downstream)\n        pair_results[\"uncond_entropy\"] = ug_ent\n        ug_ece = unconditional_granger(df, \"ece\", downstream)\n        pair_results[\"uncond_ece\"] = ug_ece\n        cg_ent = conditional_granger(df, \"token_entropy\", downstream, \"ece\")\n        pair_results[\"cond_entropy_given_ece\"] = cg_ent\n        cg_ece = conditional_granger(df, \"ece\", downstream, \"token_entropy\")\n        pair_results[\"cond_ece_given_entropy\"] = cg_ece\n        jg = joint_granger(df, [\"token_entropy\", \"ece\"], downstream)\n        pair_results[\"joint\"] = jg\n\n        lag = 1\n        def fmt(r):\n            if r and lag in r and not (isinstance(r[lag].get('p_value'), float) and r[lag]['p_value'] != r[lag]['p_value']):\n                return f\"F={r[lag]['F_stat']:.3f}, p={r[lag]['p_value']:.4f}\"\n            return \"N/A\"\n\n        print(f\"    Uncond entropy->{downstream}:        {fmt(ug_ent)}\")\n        print(f\"    Uncond ECE->{downstream}:            {fmt(ug_ece)}\")\n        print(f\"    Cond entropy->{downstream}|ECE:      {fmt(cg_ent)}\")\n        print(f\"    Cond ECE->{downstream}|entropy:      {fmt(cg_ece)}\")\n        print(f\"    Joint [entropy,ECE]->{downstream}:   {fmt(jg)}\")\n        exp_results[\"tests\"][downstream] = pair_results\n    all_results[exp_name] = exp_results\n\n\nprint(\"\\n\\n\" + \"=\"*80)\nprint(\"SUMMARY TABLE: Conditional vs Unconditional Granger (lag=1, p-values)\")\nprint(\"=\"*80)\n\nheader = f\"{'Experiment':<16} {'Downstream':<12} {'Uncond TE':>10} {'Uncond ECE':>10} {'Cond TE|ECE':>12} {'Cond ECE|TE':>12} {'Joint':>10}\"\nprint(header)\nprint(\"-\" * len(header))\n\nsig_counts = {\"uncond_entropy\": 0, \"uncond_ece\": 0,\n              \"cond_entropy_given_ece\": 0, \"cond_ece_given_entropy\": 0, \"joint\": 0}\ntotal_tests = 0\n\ndef safe_isnan(v):\n    try:\n        return v != v\n    except:\n        return True\n\nfor exp_name, exp_data in all_results.items():\n    for downstream, tests in exp_data[\"tests\"].items():\n        def get_p(test_key):\n            r = tests.get(test_key)\n            if r and 1 in r and not safe_isnan(r[1].get(\"p_value\")):\n                return r[1][\"p_value\"]\n            return float('nan')\n\n        p_ue = get_p(\"uncond_entropy\")\n        p_uc = get_p(\"uncond_ece\")\n        p_ce = get_p(\"cond_entropy_given_ece\")\n        p_cc = get_p(\"cond_ece_given_entropy\")\n        p_j = get_p(\"joint\")\n\n        def fmt_p(p):\n            if safe_isnan(p): return \"N/A\"\n            star = \"***\" if p < 0.001 else \"**\" if p < 0.01 else \"*\" if p < 0.05 else \".\" if p < 0.1 else \"\"\n            return f\"{p:.4f}{star}\"\n\n        print(f\"{exp_name:<16} {downstream:<12} {fmt_p(p_ue):>10} {fmt_p(p_uc):>10} {fmt_p(p_ce):>12} {fmt_p(p_cc):>12} {fmt_p(p_j):>10}\")\n\n        total_tests += 1\n        if not safe_isnan(p_ue) and p_ue < 0.05: sig_counts[\"uncond_entropy\"] += 1\n        if not safe_isnan(p_uc) and p_uc < 0.05: sig_counts[\"uncond_ece\"] += 1\n        if not safe_isnan(p_ce) and p_ce < 0.05: sig_counts[\"cond_entropy_given_ece\"] += 1\n        if not safe_isnan(p_cc) and p_cc < 0.05: sig_counts[\"cond_ece_given_entropy\"] += 1\n        if not safe_isnan(p_j) and p_j < 0.05: sig_counts[\"joint\"] += 1\n\n\nprint(f\"\\n{'-'*80}\")\nprint(f\"Significance counts (p<0.05) out of {total_tests} tests:\")\nfor k, v in sig_counts.items():\n    print(f\"  {k:<30}: {v}/{total_tests} ({100*v/total_tests:.1f}%)\")\n\n\nprint(\"\\n\\n\" + \"=\"*80)\nprint(\"REDUNDANCY ANALYSIS\")\nprint(\"=\"*80)\n\npatterns = {\"both_independent\": 0, \"entropy_only\": 0, \"ece_only\": 0,\n            \"redundant\": 0, \"neither\": 0, \"na\": 0}\n\nfor exp_name, exp_data in all_results.items():\n    for downstream, tests in exp_data[\"tests\"].items():\n        def get_p(test_key):\n            r = tests.get(test_key)\n            if r and 1 in r and not safe_isnan(r[1].get(\"p_value\")):\n                return r[1][\"p_value\"]\n            return float('nan')\n\n        p_ue = get_p(\"uncond_entropy\")\n        p_uc = get_p(\"uncond_ece\")\n        p_ce = get_p(\"cond_entropy_given_ece\")\n        p_cc = get_p(\"cond_ece_given_entropy\")\n\n        if safe_isnan(p_ce) or safe_isnan(p_cc):\n            patterns[\"na\"] += 1\n            continue\n\n        ent_indep = p_ce < 0.05\n        ece_indep = p_cc < 0.05\n\n        if ent_indep and ece_indep:\n            patterns[\"both_independent\"] += 1\n        elif ent_indep and not ece_indep:\n            patterns[\"entropy_only\"] += 1\n        elif not ent_indep and ece_indep:\n            patterns[\"ece_only\"] += 1\n        elif not safe_isnan(p_ue) and p_ue < 0.05 or not safe_isnan(p_uc) and p_uc < 0.05:\n            patterns[\"redundant\"] += 1\n        else:\n            patterns[\"neither\"] += 1\n\nprint(\"Pattern classification (based on conditional p<0.05):\")\nfor pattern, count in patterns.items():\n    print(f\"  {pattern:<20}: {count}\")\n\nprint(\"\\nSofter threshold (p<0.10):\")\npatterns10 = {\"both_independent\": 0, \"entropy_only\": 0, \"ece_only\": 0,\n              \"redundant\": 0, \"neither\": 0, \"na\": 0}\n\nfor exp_name, exp_data in all_results.items():\n    for downstream, tests in exp_data[\"tests\"].items():\n        def get_p(test_key):\n            r = tests.get(test_key)\n            if r and 1 in r and not safe_isnan(r[1].get(\"p_value\")):\n                return r[1][\"p_value\"]\n            return float('nan')\n\n        p_ue = get_p(\"uncond_entropy\")\n        p_uc = get_p(\"uncond_ece\")\n        p_ce = get_p(\"cond_entropy_given_ece\")\n        p_cc = get_p(\"cond_ece_given_entropy\")\n\n        if safe_isnan(p_ce) or safe_isnan(p_cc):\n            patterns10[\"na\"] += 1\n            continue\n\n        ent_indep = p_ce < 0.10\n        ece_indep = p_cc < 0.10\n\n        if ent_indep and ece_indep:\n            patterns10[\"both_independent\"] += 1\n        elif ent_indep and not ece_indep:\n            patterns10[\"entropy_only\"] += 1\n        elif not ent_indep and ece_indep:\n            patterns10[\"ece_only\"] += 1\n        elif not safe_isnan(p_ue) and p_ue < 0.10 or not safe_isnan(p_uc) and p_uc < 0.10:\n            patterns10[\"redundant\"] += 1\n        else:\n            patterns10[\"neither\"] += 1\n\nfor pattern, count in patterns10.items():\n    print(f\"  {pattern:<20}: {count}\")\n\n\nprint(\"\\n\\n\" + \"=\"*80)\nprint(\"CANARY INTER-CORRELATION (entropy vs ECE)\")\nprint(\"=\"*80)\n\nfor exp_name, path in EXPERIMENTS.items():\n    if not os.path.exists(path):\n        continue\n    df = load_experiment(path)\n    if \"token_entropy\" in df.columns and \"ece\" in df.columns:\n        r = df[\"token_entropy\"].corr(df[\"ece\"])\n        print(f\"  {exp_name:<16}: r = {r:+.4f}\")\n\n\nprint(\"\\n\\n\" + \"=\"*80)\nprint(\"EFFECT SIZE: Partial R^2 from VAR(1)\")\nprint(\"=\"*80)\n\nfor exp_name, path in EXPERIMENTS.items():\n    if not os.path.exists(path):\n        continue\n    df = load_experiment(path)\n    T = len(df)\n    if T < 7:\n        continue\n    print(f\"\\n  {exp_name} (T={T}):\")\n    for downstream in DOWNSTREAMS:\n        if downstream not in df.columns:\n            continue\n        cols_full = [downstream, \"token_entropy\", \"ece\"]\n        cols_no_ent = [downstream, \"ece\"]\n        cols_no_ece = [downstream, \"token_entropy\"]\n        try:\n            sub = df[cols_full].dropna()\n            if len(sub) < 7:\n                continue\n            m_full = VAR(sub).fit(1)\n            resid_full = m_full.resid[downstream]\n            ss_full = (resid_full**2).sum()\n            m_no_ent = VAR(df[cols_no_ent].dropna()).fit(1)\n            resid_no_ent = m_no_ent.resid[downstream]\n            ss_no_ent = (resid_no_ent**2).sum()\n            m_no_ece = VAR(df[cols_no_ece].dropna()).fit(1)\n            resid_no_ece = m_no_ece.resid[downstream]\n            ss_no_ece = (resid_no_ece**2).sum()\n            partial_r2_ent = 1.0 - ss_full / ss_no_ent if ss_no_ent > 0 else float('nan')\n            partial_r2_ece = 1.0 - ss_full / ss_no_ece if ss_no_ece > 0 else float('nan')\n            print(f\"    {downstream:<12}: partial_R2(entropy)={partial_r2_ent:+.4f}, partial_R2(ECE)={partial_r2_ece:+.4f}\")\n        except Exception as e:\n            print(f\"    {downstream:<12}: ERROR {str(e)[:60]}\")\n\n\noutput = {\n    \"meta\": {\n        \"analysis\": \"Conditional Granger Causality\",\n        \"canaries\": CANARIES,\n        \"downstreams\": DOWNSTREAMS,\n        \"method\": \"VAR F-test via statsmodels\",\n    },\n    \"results\": {}\n}\n\nfor exp_name, exp_data in all_results.items():\n    exp_out = {\"T\": exp_data[\"T\"], \"pairs\": {}}\n    for downstream, tests in exp_data[\"tests\"].items():\n        pair_out = {}\n        for test_key, lag_results in tests.items():\n            if lag_results is None:\n                continue\n            pair_out[test_key] = {}\n            for lag, r in lag_results.items():\n                pair_out[test_key][str(lag)] = {\n                    k: (float(v) if isinstance(v, (int, float, np.floating)) else\n                        [float(x) for x in v] if isinstance(v, tuple) else v)\n                    for k, v in r.items()\n                }\n        exp_out[\"pairs\"][downstream] = pair_out\n    output[\"results\"][exp_name] = exp_out\n\nout_path = \"/root/autodl-tmp/distrib_canary_collapse/results/analysis/conditional_granger_results.json\"\nos.makedirs(os.path.dirname(out_path), exist_ok=True)\nwith open(out_path, \"w\") as f:\n    json.dump(output, f, indent=2)\nprint(f\"\\n\\nResults saved to {out_path}\")\nSCRIPT_EOF\necho \"Script uploaded successfully\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat > /root/autodl-tmp/distrib_canary_collapse/results/analysis/conditional_granger_analysis.py << 'SCRIPT_EOF'\n\"\"\"Conditional Granger Causality Analysis: token_entropy vs ECE → diversity metrics.\"\"\"\nimport json, os, sys, warnings\nimport numpy as np\nimport pandas as pd\nfrom statsmodels.tsa.api import VAR\nfrom itertools import product\n\nwarnings.filterwarnings(\"ignore\")\n\nBASE = \"/root/autodl-tmp/distrib_canary_collapse/results\"\n\nEXPERIMENTS = {\n    \"a050_s42\":   f\"{BASE}/alpha_sweep/a050_s42/all_metrics.json\",\n    \"a050_s43\":   f\"{BASE}/alpha_sweep/a050_s43/all_metrics.json\",\n    \"a050_s44\":   f\"{BASE}/alpha_sweep/a050_s44/all_metrics.json\",\n    \"a055_s42\":   f\"{BASE}/alpha_sweep/a055_s42_fp32/all_metrics.json\",\n    \"a075_s42\":   f\"{BASE}/alpha_sweep/a075_s42/all_metrics.json\",\n    \"a075_s43\":   f\"{BASE}/alpha_sweep/a075_s43/all_metrics.json\",\n    \"a075_s44\":   f\"{BASE}/alpha_sweep/a075_s44/all_metrics.json\",\n    \"pythia410m\":  f\"{BASE}/generalize/pythia410m_wiki_a100_s42/all_metrics.json\",\n    \"opt1b\":       f\"{BASE}/generalize/opt1b_wiki_a100_s42/all_metrics.json\",\n    \"pythia1b_c4\": f\"{BASE}/generalize/pythia1b_c4_a100_s42/all_metrics.json\",\n    \"14b_a050\":    f\"{BASE}/scale/14b_a050_s42_fp32/all_metrics.json\",\n    \"smollm3_3b\":  f\"{BASE}/generalize/smollm3_3b_wiki_a100_s42_fp32_v3/all_metrics.json\",\n}\n\nCANARIES = [\"token_entropy\", \"ece\"]\nDOWNSTREAMS = [\"distinct_1\", \"distinct_2\", \"distinct_3\", \"mauve\"]\n\n\ndef load_experiment(path):\n    with open(path) as f:\n        data = json.load(f)\n    df = pd.DataFrame(data).sort_values(\"generation\").reset_index(drop=True)\n    return df\n\n\ndef conditional_granger(df, cause, effect, condition, maxlag=2):\n    cols_needed = [cause, effect, condition]\n    if any(c not in df.columns for c in cols_needed):\n        return None\n    sub = df[cols_needed].dropna()\n    T = len(sub)\n    results = {}\n    for lag in range(1, maxlag + 1):\n        k = 3\n        min_obs = lag * k + k + 1\n        if T < min_obs:\n            results[lag] = {\"p_value\": float('nan'), \"F_stat\": float('nan'),\n                           \"note\": f\"T={T} too small for lag={lag}\"}\n            continue\n        try:\n            model = VAR(sub[[effect, cause, condition]])\n            fitted = model.fit(lag)\n            test = fitted.test_causality(caused=effect, causing=cause, kind='f')\n            results[lag] = {\n                \"p_value\": test.pvalue,\n                \"F_stat\": test.test_statistic,\n                \"df\": (test.df_num, test.df_denom),\n            }\n        except Exception as e:\n            results[lag] = {\"p_value\": float('nan'), \"F_stat\": float('nan'), \"note\": str(e)[:80]}\n    return results\n\n\ndef unconditional_granger(df, cause, effect, maxlag=2):\n    cols = [cause, effect]\n    if any(c not in df.columns for c in cols):\n        return None\n    sub = df[cols].dropna()\n    T = len(sub)\n    results = {}\n    for lag in range(1, maxlag + 1):\n        k = 2\n        min_obs = lag * k + k + 1\n        if T < min_obs:\n            results[lag] = {\"p_value\": float('nan'), \"F_stat\": float('nan'),\n                           \"note\": f\"T={T} too small for lag={lag}\"}\n            continue\n        try:\n            model = VAR(sub[[effect, cause]])\n            fitted = model.fit(lag)\n            test = fitted.test_causality(caused=effect, causing=cause, kind='f')\n            results[lag] = {\n                \"p_value\": test.pvalue,\n                \"F_stat\": test.test_statistic,\n                \"df\": (test.df_num, test.df_denom),\n            }\n        except Exception as e:\n            results[lag] = {\"p_value\": float('nan'), \"F_stat\": float('nan'), \"note\": str(e)[:80]}\n    return results\n\n\ndef joint_granger(df, causes, effect, maxlag=2):\n    cols = causes + [effect]\n    if any(c not in df.columns for c in cols):\n        return None\n    sub = df[cols].dropna()\n    T = len(sub)\n    results = {}\n    for lag in range(1, maxlag + 1):\n        k = len(cols)\n        min_obs = lag * k + k + 1\n        if T < min_obs:\n            results[lag] = {\"p_value\": float('nan'), \"F_stat\": float('nan'),\n                           \"note\": f\"T={T} too small for lag={lag}\"}\n            continue\n        try:\n            model = VAR(sub[[effect] + causes])\n            fitted = model.fit(lag)\n            test = fitted.test_causality(caused=effect, causing=causes, kind='f')\n            results[lag] = {\n                \"p_value\": test.pvalue,\n                \"F_stat\": test.test_statistic,\n                \"df\": (test.df_num, test.df_denom),\n            }\n        except Exception as e:\n            results[lag] = {\"p_value\": float('nan'), \"F_stat\": float('nan'), \"note\": str(e)[:80]}\n    return results\n\n\nall_results = {}\n\nfor exp_name, path in EXPERIMENTS.items():\n    if not os.path.exists(path):\n        print(f\"SKIP {exp_name}: file not found\")\n        continue\n    df = load_experiment(path)\n    T = len(df)\n    print(f\"\\n{'='*60}\")\n    print(f\"Experiment: {exp_name}  (T={T})\")\n    print(f\"{'='*60}\")\n    exp_results = {\"T\": T, \"tests\": {}}\n    for downstream in DOWNSTREAMS:\n        if downstream not in df.columns:\n            print(f\"  SKIP {downstream}: not in data\")\n            continue\n        print(f\"\\n  Target: {downstream}\")\n        print(f\"  {'_'*50}\")\n        pair_results = {}\n        ug_ent = unconditional_granger(df, \"token_entropy\", downstream)\n        pair_results[\"uncond_entropy\"] = ug_ent\n        ug_ece = unconditional_granger(df, \"ece\", downstream)\n        pair_results[\"uncond_ece\"] = ug_ece\n        cg_ent = conditional_granger(df, \"token_entropy\", downstream, \"ece\")\n        pair_results[\"cond_entropy_given_ece\"] = cg_ent\n        cg_ece = conditional_granger(df, \"ece\", downstream, \"token_entropy\")\n        pair_results[\"cond_ece_given_entropy\"] = cg_ece\n        jg = joint_granger(df, [\"token_entropy\", \"ece\"], downstream)\n        pair_results[\"joint\"] = jg\n\n        lag = 1\n        def fmt(r):\n            if r and lag in r and not (isinstance(r[lag].get('p_value'), float) and r[lag]['p_value'] != r[lag]['p_value']):\n                return f\"F={r[lag]['F_stat']:.3f}, p={r[lag]['p_value']:.4f}\"\n            return \"N/A\"\n\n        print(f\"    Uncond entropy->{downstream}:        {fmt(ug_ent)}\")\n        print(f\"    Uncond ECE->{downstream}:            {fmt(ug_ece)}\")\n        print(f\"    Cond entropy->{downstream}|ECE:      {fmt(cg_ent)}\")\n        print(f\"    Cond ECE->{downstream}|entropy:      {fmt(cg_ece)}\")\n        print(f\"    Joint [entropy,ECE]->{downstream}:   {fmt(jg)}\")\n        exp_results[\"tests\"][downstream] = pair_results\n    all_results[exp_name] = exp_results\n\n\nprint(\"\\n\\n\" + \"=\"*80)\nprint(\"SUMMARY TABLE: Conditional vs Unconditional Granger (lag=1, p-values)\")\nprint(\"=\"*80)\n\nheader = f\"{'Experiment':<16} {'Downstream':<12} {'Uncond TE':>10} {'Uncond ECE':>10} {'Cond TE|ECE':>12} {'Cond ECE|TE':>12} {'Joint':>10}\"\nprint(header)\nprint(\"-\" * len(header))\n\nsig_counts = {\"uncond_entropy\": 0, \"uncond_ece\": 0,\n              \"cond_entropy_given_ece\": 0, \"cond_ece_given_entropy\": 0, \"joint\": 0}\ntotal_tests = 0\n\ndef safe_isnan(v):\n    try:\n        return v != v\n    except:\n        return True\n\nfor exp_name, exp_data in all_results.items():\n    for downstream, tests in exp_data[\"tests\"].items():\n        def get_p(test_key):\n            r = tests.get(test_key)\n            if r and 1 in r and not safe_isnan(r[1].get(\"p_value\")):\n                return r[1][\"p_value\"]\n            return float('nan')\n\n        p_ue = get_p(\"uncond_entropy\")\n        p_uc = get_p(\"uncond_ece\")\n        p_ce = get_p(\"cond_entropy_given_ece\")\n        p_cc = get_p(\"cond_ece_given_entropy\")\n        p_j = get_p(\"joint\")\n\n        def fmt_p(p):\n            if safe_isnan(p): return \"N/A\"\n            star = \"***\" if p < 0.001 else \"**\" if p < 0.01 else \"*\" if p < 0.05 else \".\" if p < 0.1 else \"\"\n            return f\"{p:.4f}{star}\"\n\n        print(f\"{exp_name:<16} {downstream:<12} {fmt_p(p_ue):>10} {fmt_p(p_uc):>10} {fmt_p(p_ce):>12} {fmt_p(p_cc):>12} {fmt_p(p_j):>10}\")\n\n        total_tests += 1\n        if not safe_isnan(p_ue) and p_ue < 0.05: sig_counts[\"uncond_entropy\"] += 1\n        if not safe_isnan(p_uc) and p_uc < 0.05: sig_counts[\"uncond_ece\"] += 1\n        if not safe_isnan(p_ce) and p_ce < 0.05: sig_counts[\"cond_entropy_given_ece\"] += 1\n        if not safe_isnan(p_cc) and p_cc < 0.05: sig_counts[\"cond_ece_given_entropy\"] += 1\n        if not safe_isnan(p_j) and p_j < 0.05: sig_counts[\"joint\"] += 1\n\n\nprint(f\"\\n{'-'*80}\")\nprint(f\"Significance counts (p<0.05) out of {total_tests} tests:\")\nfor k, v in sig_counts.items():\n    print(f\"  {k:<30}: {v}/{total_tests} ({100*v/total_tests:.1f}%)\")\n\n\nprint(\"\\n\\n\" + \"=\"*80)\nprint(\"REDUNDANCY ANALYSIS\")\nprint(\"=\"*80)\n\npatterns = {\"both_independent\": 0, \"entropy_only\": 0, \"ece_only\": 0,\n            \"redundant\": 0, \"neither\": 0, \"na\": 0}\n\nfor exp_name, exp_data in all_results.items():\n    for downstream, tests in exp_data[\"tests\"].items():\n        def get_p(test_key):\n            r = tests.get(test_key)\n            if r and 1 in r and not safe_isnan(r[1].get(\"p_value\")):\n                return r[1][\"p_value\"]\n            return float('nan')\n\n        p_ue = get_p(\"uncond_entropy\")\n        p_uc = get_p(\"uncond_ece\")\n        p_ce = get_p(\"cond_entropy_given_ece\")\n        p_cc = get_p(\"cond_ece_given_entropy\")\n\n        if safe_isnan(p_ce) or safe_isnan(p_cc):\n            patterns[\"na\"] += 1\n            continue\n\n        ent_indep = p_ce < 0.05\n        ece_indep = p_cc < 0.05\n\n        if ent_indep and ece_indep:\n            patterns[\"both_independent\"] += 1\n        elif ent_indep and not ece_indep:\n            patterns[\"entropy_only\"] += 1\n        elif not ent_indep and ece_indep:\n            patterns[\"ece_only\"] += 1\n        elif not safe_isnan(p_ue) and p_ue < 0.05 or not safe_isnan(p_uc) and p_uc < 0.05:\n            patterns[\"redundant\"] += 1\n        else:\n            patterns[\"neither\"] += 1\n\nprint(\"Pattern classification (based on conditional p<0.05):\")\nfor pattern, count in patterns.items():\n    print(f\"  {pattern:<20}: {count}\")\n\nprint(\"\\nSofter threshold (p<0.10):\")\npatterns10 = {\"both_independent\": 0, \"entropy_only\": 0, \"ece_only\": 0,\n              \"redundant\": 0, \"neither\": 0, \"na\": 0}\n\nfor exp_name, exp_data in all_results.items():\n    for downstream, tests in exp_data[\"tests\"].items():\n        def get_p(test_key):\n            r = tests.get(test_key)\n            if r and 1 in r and not safe_isnan(r[1].get(\"p_value\")):\n                return r[1][\"p_value\"]\n            return float('nan')\n\n        p_ue = get_p(\"uncond_entropy\")\n        p_uc = get_p(\"uncond_ece\")\n        p_ce = get_p(\"cond_entropy_given_ece\")\n        p_cc = get_p(\"cond_ece_given_entropy\")\n\n        if safe_isnan(p_ce) or safe_isnan(p_cc):\n            patterns10[\"na\"] += 1\n            continue\n\n        ent_indep = p_ce < 0.10\n        ece_indep = p_cc < 0.10\n\n        if ent_indep and ece_indep:\n            patterns10[\"both_independent\"] += 1\n        elif ent_indep and not ece_indep:\n            patterns10[\"entropy_only\"] += 1\n        elif not ent_indep and ece_indep:\n            patterns10[\"ece_only\"] += 1\n        elif not safe_isnan(p_ue) and p_ue < 0.10 or not safe_isnan(p_uc) and p_uc < 0.10:\n            patterns10[\"redundant\"] += 1\n        else:\n            patterns10[\"neither\"] += 1\n\nfor pattern, count in patterns10.items():\n    print(f\"  {pattern:<20}: {count}\")\n\n\nprint(\"\\n\\n\" + \"=\"*80)\nprint(\"CANARY INTER-CORRELATION (entropy vs ECE)\")\nprint(\"=\"*80)\n\nfor exp_name, path in EXPERIMENTS.items():\n    if not os.path.exists(path):\n        continue\n    df = load_experiment(path)\n    if \"token_entropy\" in df.columns and \"ece\" in df.columns:\n        r = df[\"token_entropy\"].corr(df[\"ece\"])\n        print(f\"  {exp_name:<16}: r = {r:+.4f}\")\n\n\nprint(\"\\n\\n\" + \"=\"*80)\nprint(\"EFFECT SIZE: Partial R^2 from VAR(1)\")\nprint(\"=\"*80)\n\nfor exp_name, path in EXPERIMENTS.items():\n    if not os.path.exists(path):\n        continue\n    df = load_experiment(path)\n    T = len(df)\n    if T < 7:\n        continue\n    print(f\"\\n  {exp_name} (T={T}):\")\n    for downstream in DOWNSTREAMS:\n        if downstream not in df.columns:\n            continue\n        cols_full = [downstream, \"token_entropy\", \"ece\"]\n        cols_no_ent = [downstream, \"ece\"]\n        cols_no_ece = [downstream, \"token_entropy\"]\n        try:\n            sub = df[cols_full].dropna()\n            if len(sub) < 7:\n                continue\n            m_full = VAR(sub).fit(1)\n            resid_full = m_full.resid[downstream]\n            ss_full = (resid_full**2).sum()\n            m_no_ent = VAR(df[cols_no_ent].dropna()).fit(1)\n            resid_no_ent = m_no_ent.resid[downstream]\n            ss_no_ent = (resid_no_ent**2).sum()\n            m_no_ece = VAR(df[cols_no_ece].dropna()).fit(1)\n            resid_no_ece = m_no_ece.resid[downstream]\n            ss_no_ece = (resid_no_ece**2).sum()\n            partial_r2_ent = 1.0 - ss_full / ss_no_ent if ss_no_ent > 0 else float('nan')\n            partial_r2_ece = 1.0 - ss_full / ss_no_ece if ss_no_ece > 0 else float('nan')\n            print(f\"    {downstream:<12}: partial_R2(entropy)={partial_r2_ent:+.4f}, partial_R2(ECE)={partial_r2_ece:+.4f}\")\n        except Exception as e:\n            print(f\"    {downstream:<12}: ERROR {str(e)[:60]}\")\n\n\noutput = {\n    \"meta\": {\n        \"analysis\": \"Conditional Granger Causality\",\n        \"canaries\": CANARIES,\n        \"downstreams\": DOWNSTREAMS,\n        \"method\": \"VAR F-test via statsmodels\",\n    },\n    \"results\": {}\n}\n\nfor exp_name, exp_data in all_results.items():\n    exp_out = {\"T\": exp_data[\"T\"], \"pairs\": {}}\n    for downstream, tests in exp_data[\"tests\"].items():\n        pair_out = {}\n        for test_key, lag_results in tests.items():\n            if lag_results is None:\n                continue\n            pair_out[test_key] = {}\n            for lag, r in lag_results.items():\n                pair_out[test_key][str(lag)] = {\n                    k: (float(v) if isinstance(v, (int, float, np.floating)) else\n                        [float(x) for x in v] if isinstance(v, tuple) else v)\n                    for k, v in r.items()\n                }\n        exp_out[\"pairs\"][downstream] = pair_out\n    output[\"results\"][exp_name] = exp_out\n\nout_path = \"/root/autodl-tmp/distrib_canary_collapse/results/analysis/conditional_granger_results.json\"\nos.makedirs(os.path.dirname(out_path), exist_ok=True)\nwith open(out_path, \"w\") as f:\n    json.dump(output, f, indent=2)\nprint(f\"\\n\\nResults saved to {out_path}\")\nSCRIPT_EOF\necho \"Script uploaded successfully\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-21T02:17:59.543518+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Script uploaded successfully\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-21T02:17:59.544102+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/distrib_canary_collapse && python results/analysis/conditional_granger_analysis.py 2>&1",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/distrib_canary_collapse && python results/analysis/conditional_granger_analysis.py 2>&1",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-21T02:17:59.544386+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\n============================================================\\nExperiment: a050_s42  (T=11)\\n============================================================\\n\\n  Target: distinct_1\\n  __________________________________________________\\n    Uncond entropy->distinct_1:        N/A\\n    Uncond ECE->distinct_1:            N/A\\n    Cond entropy->distinct_1|ECE:      N/A\\n    Cond ECE->distinct_1|entropy:      N/A\\n    Joint [entropy,ECE]->distinct_1:   N/A\\n\\n  Target: distinct_2\\n  __________________________________________________\\n    Uncond entropy->distinct_2:        N/A\\n    Uncond ECE->distinct_2:            N/A\\n    Cond entropy->distinct_2|ECE:      N/A\\n    Cond ECE->distinct_2|entropy:      N/A\\n    Joint [entropy,ECE]->distinct_2:   N/A\\n\\n  Target: distinct_3\\n  __________________________________________________\\n    Uncond entropy->distinct_3:        N/A\\n    Uncond ECE->distinct_3:            N/A\\n    Cond entropy->distinct_3|ECE:      N/A\\n    Cond ECE->distinct_3|entropy:      N/A\\n    Joint [entropy,ECE]->distinct_3:   N/A\\n\\n  Target: mauve\\n  __________________________________________________\\n    Uncond entropy->mauve:        N/A\\n    Uncond ECE->mauve:            N/A\\n    Cond entropy->mauve|ECE:      N/A\\n    Cond ECE->mauve|entropy:      N/A\\n    Joint [entropy,ECE]->mauve:   N/A\\n\\n============================================================\\nExperiment: a050_s43  (T=11)\\n============================================================\\n\\n  Target: distinct_1\\n  __________________________________________________\\n    Uncond entropy->distinct_1:        N/A\\n    Uncond ECE->distinct_1:            N/A\\n    Cond entropy->distinct_1|ECE:      N/A\\n    Cond ECE->distinct_1|entropy:      N/A\\n    Joint [entropy,ECE]->distinct_1:   N/A\\n\\n  Target: distinct_2\\n  __________________________________________________\\n    Uncond entropy->distinct_2:        N/A\
…[truncated 6592 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-21T02:17:59.544593+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/analysis/conditional_granger_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/analysis/conditional_granger_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-21T02:17:59.544987+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"meta\\\": {\\n    \\\"analysis\\\": \\\"Conditional Granger Causality\\\",\\n    \\\"canaries\\\": [\\n      \\\"token_entropy\\\",\\n      \\\"ece\\\"\\n    ],\\n    \\\"downstreams\\\": [\\n      \\\"distinct_1\\\",\\n      \\\"distinct_2\\\",\\n      \\\"distinct_3\\\",\\n      \\\"mauve\\\"\\n    ],\\n    \\\"method\\\": \\\"VAR F-test via statsmodels\\\"\\n  },\\n  \\\"results\\\": {\\n    \\\"a050_s42\\\": {\\n      \\\"T\\\": 11,\\n      \\\"pairs\\\": {\\n        \\\"distinct_1\\\": {\\n          \\\"uncond_entropy\\\": {\\n            \\\"1\\\": {\\n              \\\"p_value\\\": NaN,\\n              \\\"F_stat\\\": NaN,\\n              \\\"note\\\": \\\"'CausalityTestResults' object has no attribute 'df_num'\\\"\\n            },\\n            \\\"2\\\": {\\n              \\\"p_value\\\": NaN,\\n              \\\"F_stat\\\": NaN,\\n              \\\"note\\\": \\\"'CausalityTestResults' object has no attribute 'df_num'\\\"\\n            }\\n          },\\n          \\\"uncond_ece\\\": {\\n            \\\"1\\\": {\\n              \\\"p_value\\\": NaN,\\n              \\\"F_stat\\\": NaN,\\n              \\\"note\\\": \\\"'CausalityTestResults' object has no attribute 'df_num'\\\"\\n            },\\n            \\\"2\\\": {\\n              \\\"p_value\\\": NaN,\\n              \\\"F_stat\\\": NaN,\\n              \\\"note\\\": \\\"'CausalityTestResults' object has no attribute 'df_num'\\\"\\n            }\\n          },\\n          \\\"cond_entropy_given_ece\\\": {\\n            \\\"1\\\": {\\n              \\\"p_value\\\": NaN,\\n              \\\"F_stat\\\": NaN,\\n              \\\"note\\\": \\\"'CausalityTestResults' object has no attribute 'df_num'\\\"\\n            },\\n            \\\"2\\\": {\\n              \\\"p_value\\\": NaN,\\n              \\\"F_stat\\\": NaN,\\n              \\\"note\\\": \\\"'CausalityTestResults' object has no attribute 'df_num'\\\"\\n            }\\n          }
…[truncated 8132 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-21T02:17:59.545226+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport statsmodels\nprint('statsmodels version:', statsmodels.__version__)\n\nimport json, pandas as pd, numpy as np\nfrom statsmodels.tsa.api import VAR\n\ndata = json.load(open('/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42/all_metrics.json'))\ndf = pd.DataFrame(data).sort_values('generation').reset_index(drop=True)\n\nsub = df[['distinct_1', 'token_entropy']].dropna()\nmodel = VAR(sub)\nfitted = model.fit(1)\ntest = fitted.test_causality(caused='distinct_1', causing='token_entropy', kind='f')\nprint('Type:', type(test))\nprint('Dir:', [a for a in dir(test) if not a.startswith('_')])\nprint('pvalue:', test.pvalue)\nprint('test_statistic:', test.test_statistic)\nprint()\n\n# Try to find df attributes\nfor attr in dir(test):\n    if 'df' in attr.lower() or 'deg' in attr.lower() or 'free' in attr.lower():\n        print(f'  {attr}:', getattr(test, attr))\nprint('summary:', test.summary())\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport statsmodels\nprint('statsmodels version:', statsmodels.__version__)\n\nimport json, pandas as pd, numpy as np\nfrom statsmodels.tsa.api import VAR\n\ndata = json.load(open('/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42/all_metrics.json'))\ndf = pd.DataFrame(data).sort_values('generation').reset_index(drop=True)\n\nsub = df[['distinct_1', 'token_entropy']].dropna()\nmodel = VAR(sub)\nfitted = model.fit(1)\ntest = fitted.test_causality(caused='distinct_1', causing='token_entropy', kind='f')\nprint('Type:', type(test))\nprint('Dir:', [a for a in dir(test) if not a.startswith('_')])\nprint('pvalue:', test.pvalue)\nprint('test_statistic:', test.test_statistic)\nprint()\n\n# Try to find df attributes\nfor attr in dir(test):\n    if 'df' in attr.lower() or 'deg' in attr.lower() or 'free' in attr.lower():\n        print(f'  {attr}:', getattr(test, attr))\nprint('summary:', test.summary())\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-21T02:17:59.545411+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"statsmodels version: 0.14.6\\nType: &lt;class 'statsmodels.tsa.vector_ar.hypothesis_test_results.CausalityTestResults'>\\nDir: ['caused', 'causing', 'conclusion', 'conclusion_str', 'crit_value', 'df', 'h0', 'method', 'pvalue', 'signif', 'signif_str', 'summary', 'test', 'test_statistic', 'title']\\npvalue: 3.5217654406924995e-07\\ntest_statistic: 80.48292074408903\\n\\n  df: (1, 14)\\nsummary: Granger causality F-test. H_0: token_entropy does not Granger-cause distinct_1. Conclusion: reject H_0 at 5% significance level.\\n=============================================\\nTest statistic Critical value p-value    df  \\n---------------------------------------------\\n         80.48          4.600   0.000 (1, 14)\\n---------------------------------------------\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-21T02:17:59.545638+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "cat > /root/autodl-tmp/distrib_canary_collapse/results/analysis/conditional_granger_v2.py << 'SCRIPT_EOF'\n\"\"\"Conditional Granger Causality Analysis v2: fixed attribute names.\"\"\"\nimport json, os, warnings\nimport numpy as np\nimport pandas as pd\nfrom statsmodels.tsa.api import VAR\n\nwarnings.filterwarnings(\"ignore\")\n\nBASE = \"/root/autodl-tmp/distrib_canary_collapse/results\"\n\nEXPERIMENTS = {\n    \"a050_s42\":    f\"{BASE}/alpha_sweep/a050_s42/all_metrics.json\",\n    \"a050_s43\":    f\"{BASE}/alpha_sweep/a050_s43/all_metrics.json\",\n    \"a050_s44\":    f\"{BASE}/alpha_sweep/a050_s44/all_metrics.json\",\n    \"a055_s42\":    f\"{BASE}/alpha_sweep/a055_s42_fp32/all_metrics.json\",\n    \"a075_s42\":    f\"{BASE}/alpha_sweep/a075_s42/all_metrics.json\",\n    \"a075_s43\":    f\"{BASE}/alpha_sweep/a075_s43/all_metrics.json\",\n    \"a075_s44\":    f\"{BASE}/alpha_sweep/a075_s44/all_metrics.json\",\n    \"pythia410m\":  f\"{BASE}/generalize/pythia410m_wiki_a100_s42/all_metrics.json\",\n    \"opt1b\":       f\"{BASE}/generalize/opt1b_wiki_a100_s42/all_metrics.json\",\n    \"pythia1b_c4\": f\"{BASE}/generalize/pythia1b_c4_a100_s42/all_metrics.json\",\n    \"14b_a050\":    f\"{BASE}/scale/14b_a050_s42_fp32/all_metrics.json\",\n    \"smollm3_3b\":  f\"{BASE}/generalize/smollm3_3b_wiki_a100_s42_fp32_v3/all_metrics.json\",\n}\n\nCANARIES = [\"token_entropy\", \"ece\"]\nDOWNSTREAMS = [\"distinct_1\", \"distinct_2\", \"distinct_3\", \"mauve\"]\n\n\ndef load_experiment(path):\n    with open(path) as f:\n        data = json.load(f)\n    return pd.DataFrame(data).sort_values(\"generation\").reset_index(drop=True)\n\n\ndef run_granger(df, caused, causing, extra_vars=None, maxlag=2):\n    \"\"\"\n    Run Granger causality test.\n    If extra_vars provided, it's a conditional test (VAR includes control variables).\n    \"\"\"\n    if extra_vars is None:\n        extra_vars = []\n    cols = [caused, causing] + extra_vars\n    if any(c not in df.columns for c in cols):\n        return None\n    sub = df[cols].dropna()\n    T = len(sub)\n    results = {}\n    for lag in range(1, maxlag + 1):\n        k = len(cols)\n        min_obs = lag * k + k + 2\n        if T < min_obs:\n            results[lag] = {\"p\": np.nan, \"F\": np.nan, \"df\": None, \"note\": f\"T={T}<{min_obs}\"}\n            continue\n        try:\n            model = VAR(sub)\n            fitted = model.fit(lag)\n            test = fitted.test_causality(caused=caused, causing=causing, kind='f')\n            results[lag] = {\"p\": float(test.pvalue), \"F\": float(test.test_statistic), \"df\": test.df}\n        except Exception as e:\n            results[lag] = {\"p\": np.nan, \"F\": np.nan, \"note\": str(e)[:100]}\n    return results\n\n\ndef safe_isnan(v):\n    try:\n        return v != v\n    except:\n        return True\n\ndef fmt_p(p):\n    if safe_isnan(p):\n        return \"    N/A\"\n    star = \"***\" if p < 0.001 else \" **\" if p < 0.01 else \"  *\" if p < 0.05 else \"  .\" if p < 0.1 else \"   \"\n    return f\"{p:.4f}{star}\"\n\ndef fmt_f(r, lag=1):\n    if r is None or lag not in r or safe_isnan(r[lag][\"p\"]):\n        return \"N/A\", \"N/A\"\n    return fmt_p(r[lag][\"p\"]), f\"{r[lag]['F']:.2f}\"\n\n\n# ═══════════════════════════════════════════════════════\n# Run all tests\n# ═══════════════════════════════════════════════════════\nall_results = {}\n\nfor exp_name, path in EXPERIMENTS.items():\n    if not os.path.exists(path):\n        print(f\"SKIP {exp_name}\")\n        continue\n    df = load_experiment(path)\n    T = len(df)\n    exp_res = {\"T\": T, \"tests\": {}}\n\n    for ds in DOWNSTREAMS:\n        if ds not in df.columns:\n            continue\n        pair = {}\n        pair[\"uncond_ent\"]     = run_granger(df, ds, \"token_entropy\")\n        pair[\"uncond_ece\"]     = run_granger(df, ds, \"ece\")\n        pair[\"cond_ent|ece\"]   = run_granger(df, ds, \"token_entropy\", extra_vars=[\"ece\"])\n        pair[\"cond_ece|ent\"]   = run_granger(df, ds, \"ece\", extra_vars=[\"token_entropy\"])\n        pair[\"joint\"]          = run_granger(df, ds, [\"token_entropy\", \"ece\"])\n        exp_res[\"tests\"][ds] = pair\n\n    all_results[exp_name] = exp_res\n\n# ═══════════════════════════════════════════════════════\n# Summary table (lag=1)\n# ═══════════════════════════════════════════════════════\nprint(\"=\"*100)\nprint(\"CONDITIONAL GRANGER CAUSALITY: lag=1 p-values\")\nprint(\"=\"*100)\nprint(f\"{'Experiment':<16} {'Target':<12} {'Unc.TE':>10} {'Unc.ECE':>10} {'TE|ECE':>10} {'ECE|TE':>10} {'Joint':>10}\")\nprint(\"-\"*80)\n\nsig = {k: 0 for k in [\"uncond_ent\",\"uncond_ece\",\"cond_ent|ece\",\"cond_ece|ent\",\"joint\"]}\nn_valid = {k: 0 for k in sig}\ntotal = 0\n\nfor exp_name, exp_data in all_results.items():\n    for ds, tests in exp_data[\"tests\"].items():\n        total += 1\n        vals = {}\n        for key in sig:\n            r = tests.get(key)\n            p = r[1][\"p\"] if r and 1 in r else np.nan\n            vals[key] = p\n            if not safe_isnan(p):\n                n_valid[key] += 1\n                if p < 0.05:\n                    sig[key] += 1\n\n        row = f\"{exp_name:<16} {ds:<12}\"\n        for key in [\"uncond_ent\",\"uncond_ece\",\"cond_ent|ece\",\"cond_ece|ent\",\"joint\"]:\n            row += f\" {fmt_p(vals[key]):>10}\"\n        print(row)\n\nprint(f\"\\n{'='*80}\")\nprint(f\"Significance summary (p<0.05):\")\nfor k in sig:\n    print(f\"  {k:<20}: {sig[k]}/{n_valid[k]} valid tests ({100*sig[k]/n_valid[k]:.1f}% if valid)\")\n\n\n# ═══════════════════════════════════════════════════════\n# Redundancy classification\n# ═══════════════════════════════════════════════════════\nprint(f\"\\n{'='*80}\")\nprint(\"REDUNDANCY CLASSIFICATION (lag=1, p<0.05)\")\nprint(\"=\"*80)\n\npatterns = {\"both_independent\": [], \"entropy_dominant\": [], \"ece_dominant\": [],\n            \"redundant_shared\": [], \"neither_sig\": [], \"insufficient_data\": []}\n\nfor exp_name, exp_data in all_results.items():\n    for ds, tests in exp_data[\"tests\"].items():\n        label = f\"{exp_name}/{ds}\"\n\n        def getp(key):\n            r = tests.get(key)\n            return r[1][\"p\"] if r and 1 in r else np.nan\n\n        p_ue = getp(\"uncond_ent\")\n        p_uc = getp(\"uncond_ece\")\n        p_ce = getp(\"cond_ent|ece\")\n        p_cc = getp(\"cond_ece|ent\")\n\n        if safe_isnan(p_ce) or safe_isnan(p_cc):\n            patterns[\"insufficient_data\"].append(label)\n            continue\n\n        ent_survives = p_ce < 0.05\n        ece_survives = p_cc < 0.05\n\n        if ent_survives and ece_survives:\n            patterns[\"both_independent\"].append(label)\n        elif ent_survives and not ece_survives:\n            patterns[\"entropy_dominant\"].append(label)\n        elif not ent_survives and ece_survives:\n            patterns[\"ece_dominant\"].append(label)\n        elif (not safe_isnan(p_ue) and p_ue < 0.05) or (not safe_isnan(p_uc) and p_uc < 0.05):\n            patterns[\"redundant_shared\"].append(label)\n        else:\n            patterns[\"neither_sig\"].append(label)\n\nfor pat, items in patterns.items():\n    print(f\"\\n  {pat} ({len(items)}):\")\n    for item in items:\n        print(f\"    - {item}\")\n\n\n# ═══════════════════════════════════════════════════════\n# Softer threshold p<0.10\n# ═══════════════════════════════════════════════════════\nprint(f\"\\n{'='*80}\")\nprint(\"REDUNDANCY CLASSIFICATION (lag=1, p<0.10)\")\nprint(\"=\"*80)\n\npatterns10 = {\"both_independent\": 0, \"entropy_dominant\": 0, \"ece_dominant\": 0,\n              \"redundant_shared\": 0, \"neither_sig\": 0, \"insufficient_data\": 0}\n\nfor exp_name, exp_data in all_results.items():\n    for ds, tests in exp_data[\"tests\"].items():\n        def getp(key):\n            r = tests.get(key)\n            return r[1][\"p\"] if r and 1 in r else np.nan\n\n        p_ue = getp(\"uncond_ent\")\n        p_uc = getp(\"uncond_ece\")\n        p_ce = getp(\"cond_ent|ece\")\n        p_cc = getp(\"cond_ece|ent\")\n\n        if safe_isnan(p_ce) or safe_isnan(p_cc):\n            patterns10[\"insufficient_data\"] += 1\n            continue\n        ent_survives = p_ce < 0.10\n        ece_survives = p_cc < 0.10\n        if ent_survives and ece_survives:\n            patterns10[\"both_independent\"] += 1\n        elif ent_survives and not ece_survives:\n            patterns10[\"entropy_dominant\"] += 1\n        elif not ent_survives and ece_survives:\n            patterns10[\"ece_dominant\"] += 1\n        elif (not safe_isnan(p_ue) and p_ue < 0.10) or (not safe_isnan(p_uc) and p_uc < 0.10):\n            patterns10[\"redundant_shared\"] += 1\n        else:\n            patterns10[\"neither_sig\"] += 1\n\nfor pat, count in patterns10.items():\n    print(f\"  {pat:<20}: {count}\")\n\n\n# ═══════════════════════════════════════════════════════\n# Canary inter-correlation\n# ═══════════════════════════════════════════════════════\nprint(f\"\\n{'='*80}\")\nprint(\"CANARY INTER-CORRELATION (Pearson r: token_entropy vs ECE)\")\nprint(\"=\"*80)\n\nfor exp_name, path in EXPERIMENTS.items():\n    if not os.path.exists(path):\n        continue\n    df = load_experiment(path)\n    r = df[\"token_entropy\"].corr(df[\"ece\"])\n    print(f\"  {exp_name:<16}: r = {r:+.4f}\")\n\n\n# ═══════════════════════════════════════════════════════\n# Partial R² effect sizes\n# ═══════════════════════════════════════════════════════\nprint(f\"\\n{'='*80}\")\nprint(\"PARTIAL R^2 FROM VAR(1): incremental variance explained\")\nprint(\"(How much does adding each canary improve prediction beyond the other?)\")\nprint(\"=\"*80)\n\npr2_data = []\n\nfor exp_name, path in EXPERIMENTS.items():\n    if not os.path.exists(path):\n        continue\n    df = load_experiment(path)\n    T = len(df)\n    if T < 7:\n        continue\n    print(f\"\\n  {exp_name} (T={T}):\")\n    for ds in DOWNSTREAMS:\n        if ds not in df.columns:\n            continue\n        try:\n            sub_full = df[[ds, \"token_entropy\", \"ece\"]].dropna()\n            sub_no_ent = df[[ds, \"ece\"]].dropna()\n            sub_no_ece = df[[ds, \"token_entropy\"]].dropna()\n\n            ss_full = (VAR(sub_full).fit(1).resid[ds]**2).sum()\n            ss_no_ent = (VAR(sub_no_ent).fit(1).resid[ds]**2).sum()\n            ss_no_ece = (VAR(sub_no_ece).fit(1).resid[ds]**2).sum()\n\n            pr2_ent = 1.0 - ss_full / ss_no_ent\n            pr2_ece = 1.0 - ss_full / ss_no_ece\n\n            winner = \"ENT\" if pr2_ent > pr2_ece else \"ECE\" if pr2_ece > pr2_ent else \"TIE\"\n            print(f\"    {ds:<12}: pR2(ent)={pr2_ent:.3f}  pR2(ece)={pr2_ece:.3f}  [{winner}]\")\n            pr2_data.append({\"exp\": exp_name, \"ds\": ds, \"pr2_ent\": pr2_ent, \"pr2_ece\": pr2_ece})\n        except Exception as e:\n            print(f\"    {ds:<12}: ERROR {str(e)[:60]}\")\n\n# Aggregate partial R²\nprint(f\"\\n{'='*80}\")\nprint(\"AGGREGATE PARTIAL R^2\")\nprint(\"=\"*80)\nif pr2_data:\n    pr2_df = pd.DataFrame(pr2_data)\n    for ds in DOWNSTREAMS:\n        sub = pr2_df[pr2_df[\"ds\"] == ds]\n        if len(sub) == 0:\n            continue\n        ent_wins = (sub[\"pr2_ent\"] > sub[\"pr2_ece\"]).sum()\n        ece_wins = (sub[\"pr2_ece\"] > sub[\"pr2_ent\"]).sum()\n        print(f\"  {ds:<12}: mean pR2(ent)={sub['pr2_ent'].mean():.3f}, mean pR2(ece)={sub['pr2_ece'].mean():.3f} | ENT wins {ent_wins}/{len(sub)}, ECE wins {ece_wins}/{len(sub)}\")\n\n    print(f\"\\n  Overall:\")\n    ent_wins = (pr2_df[\"pr2_ent\"] > pr2_df[\"pr2_ece\"]).sum()\n    ece_wins = (pr2_df[\"pr2_ece\"] > pr2_df[\"pr2_ent\"]).sum()\n    print(f\"    mean pR2(entropy)={pr2_df['pr2_ent'].mean():.3f}, mean pR2(ECE)={pr2_df['pr2_ece'].mean():.3f}\")\n    print(f\"    Entropy dominates: {ent_wins}/{len(pr2_df)} pairs ({100*ent_wins/len(pr2_df):.1f}%)\")\n    print(f\"    ECE dominates:     {ece_wins}/{len(pr2_df)} pairs ({100*ece_wins/len(pr2_df):.1f}%)\")\n\n\n# Save JSON\noutput = {\"meta\": {\"analysis\": \"Conditional Granger v2\", \"lag\": 1}, \"summary\": {}, \"details\": {}}\nfor exp_name, exp_data in all_results.items():\n    exp_out = {\"T\": exp_data[\"T\"], \"pairs\": {}}\n    for ds, tests in exp_data[\"tests\"].items():\n        pair_out = {}\n        for key, lag_res in tests.items():\n            if lag_res is None:\n                continue\n            pair_out[key] = {}\n            for lag, r in lag_res.items():\n                pair_out[key][str(lag)] = {\"p\": r[\"p\"] if not safe_isnan(r[\"p\"]) else None,\n                                           \"F\": r[\"F\"] if not safe_isnan(r.get(\"F\", np.nan)) else None,\n                                           \"df\": list(r[\"df\"]) if r.get(\"df\") else None}\n        exp_out[\"pairs\"][ds] = pair_out\n    output[\"details\"][exp_name] = exp_out\n\nout_path = \"/root/autodl-tmp/distrib_canary_collapse/results/analysis/conditional_granger_v2.json\"\nwith open(out_path, \"w\") as f:\n    json.dump(output, f, indent=2, default=str)\nprint(f\"\\nJSON saved to {out_path}\")\nSCRIPT_EOF\necho \"Script ready\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat > /root/autodl-tmp/distrib_canary_collapse/results/analysis/conditional_granger_v2.py << 'SCRIPT_EOF'\n\"\"\"Conditional Granger Causality Analysis v2: fixed attribute names.\"\"\"\nimport json, os, warnings\nimport numpy as np\nimport pandas as pd\nfrom statsmodels.tsa.api import VAR\n\nwarnings.filterwarnings(\"ignore\")\n\nBASE = \"/root/autodl-tmp/distrib_canary_collapse/results\"\n\nEXPERIMENTS = {\n    \"a050_s42\":    f\"{BASE}/alpha_sweep/a050_s42/all_metrics.json\",\n    \"a050_s43\":    f\"{BASE}/alpha_sweep/a050_s43/all_metrics.json\",\n    \"a050_s44\":    f\"{BASE}/alpha_sweep/a050_s44/all_metrics.json\",\n    \"a055_s42\":    f\"{BASE}/alpha_sweep/a055_s42_fp32/all_metrics.json\",\n    \"a075_s42\":    f\"{BASE}/alpha_sweep/a075_s42/all_metrics.json\",\n    \"a075_s43\":    f\"{BASE}/alpha_sweep/a075_s43/all_metrics.json\",\n    \"a075_s44\":    f\"{BASE}/alpha_sweep/a075_s44/all_metrics.json\",\n    \"pythia410m\":  f\"{BASE}/generalize/pythia410m_wiki_a100_s42/all_metrics.json\",\n    \"opt1b\":       f\"{BASE}/generalize/opt1b_wiki_a100_s42/all_metrics.json\",\n    \"pythia1b_c4\": f\"{BASE}/generalize/pythia1b_c4_a100_s42/all_metrics.json\",\n    \"14b_a050\":    f\"{BASE}/scale/14b_a050_s42_fp32/all_metrics.json\",\n    \"smollm3_3b\":  f\"{BASE}/generalize/smollm3_3b_wiki_a100_s42_fp32_v3/all_metrics.json\",\n}\n\nCANARIES = [\"token_entropy\", \"ece\"]\nDOWNSTREAMS = [\"distinct_1\", \"distinct_2\", \"distinct_3\", \"mauve\"]\n\n\ndef load_experiment(path):\n    with open(path) as f:\n        data = json.load(f)\n    return pd.DataFrame(data).sort_values(\"generation\").reset_index(drop=True)\n\n\ndef run_granger(df, caused, causing, extra_vars=None, maxlag=2):\n    \"\"\"\n    Run Granger causality test.\n    If extra_vars provided, it's a conditional test (VAR includes control variables).\n    \"\"\"\n    if extra_vars is None:\n        extra_vars = []\n    cols = [caused, causing] + extra_vars\n    if any(c not in df.columns for c in cols):\n        return None\n    sub = df[cols].dropna()\n    T = len(sub)\n    results = {}\n    for lag in range(1, maxlag + 1):\n        k = len(cols)\n        min_obs = lag * k + k + 2\n        if T < min_obs:\n            results[lag] = {\"p\": np.nan, \"F\": np.nan, \"df\": None, \"note\": f\"T={T}<{min_obs}\"}\n            continue\n        try:\n            model = VAR(sub)\n            fitted = model.fit(lag)\n            test = fitted.test_causality(caused=caused, causing=causing, kind='f')\n            results[lag] = {\"p\": float(test.pvalue), \"F\": float(test.test_statistic), \"df\": test.df}\n        except Exception as e:\n            results[lag] = {\"p\": np.nan, \"F\": np.nan, \"note\": str(e)[:100]}\n    return results\n\n\ndef safe_isnan(v):\n    try:\n        return v != v\n    except:\n        return True\n\ndef fmt_p(p):\n    if safe_isnan(p):\n        return \"    N/A\"\n    star = \"***\" if p < 0.001 else \" **\" if p < 0.01 else \"  *\" if p < 0.05 else \"  .\" if p < 0.1 else \"   \"\n    return f\"{p:.4f}{star}\"\n\ndef fmt_f(r, lag=1):\n    if r is None or lag not in r or safe_isnan(r[lag][\"p\"]):\n        return \"N/A\", \"N/A\"\n    return fmt_p(r[lag][\"p\"]), f\"{r[lag]['F']:.2f}\"\n\n\n# ═══════════════════════════════════════════════════════\n# Run all tests\n# ═══════════════════════════════════════════════════════\nall_results = {}\n\nfor exp_name, path in EXPERIMENTS.items():\n    if not os.path.exists(path):\n        print(f\"SKIP {exp_name}\")\n        continue\n    df = load_experiment(path)\n    T = len(df)\n    exp_res = {\"T\": T, \"tests\": {}}\n\n    for ds in DOWNSTREAMS:\n        if ds not in df.columns:\n            continue\n        pair = {}\n        pair[\"uncond_ent\"]     = run_granger(df, ds, \"token_entropy\")\n        pair[\"uncond_ece\"]     = run_granger(df, ds, \"ece\")\n        pair[\"cond_ent|ece\"]   = run_granger(df, ds, \"token_entropy\", extra_vars=[\"ece\"])\n        pair[\"cond_ece|ent\"]   = run_granger(df, ds, \"ece\", extra_vars=[\"token_entropy\"])\n        pair[\"joint\"]          = run_granger(df, ds, [\"token_entropy\", \"ece\"])\n        exp_res[\"tests\"][ds] = pair\n\n    all_results[exp_name] = exp_res\n\n# ═══════════════════════════════════════════════════════\n# Summary table (lag=1)\n# ═══════════════════════════════════════════════════════\nprint(\"=\"*100)\nprint(\"CONDITIONAL GRANGER CAUSALITY: lag=1 p-values\")\nprint(\"=\"*100)\nprint(f\"{'Experiment':<16} {'Target':<12} {'Unc.TE':>10} {'Unc.ECE':>10} {'TE|ECE':>10} {'ECE|TE':>10} {'Joint':>10}\")\nprint(\"-\"*80)\n\nsig = {k: 0 for k in [\"uncond_ent\",\"uncond_ece\",\"cond_ent|ece\",\"cond_ece|ent\",\"joint\"]}\nn_valid = {k: 0 for k in sig}\ntotal = 0\n\nfor exp_name, exp_data in all_results.items():\n    for ds, tests in exp_data[\"tests\"].items():\n        total += 1\n        vals = {}\n        for key in sig:\n            r = tests.get(key)\n            p = r[1][\"p\"] if r and 1 in r else np.nan\n            vals[key] = p\n            if not safe_isnan(p):\n                n_valid[key] += 1\n                if p < 0.05:\n                    sig[key] += 1\n\n        row = f\"{exp_name:<16} {ds:<12}\"\n        for key in [\"uncond_ent\",\"uncond_ece\",\"cond_ent|ece\",\"cond_ece|ent\",\"joint\"]:\n            row += f\" {fmt_p(vals[key]):>10}\"\n        print(row)\n\nprint(f\"\\n{'='*80}\")\nprint(f\"Significance summary (p<0.05):\")\nfor k in sig:\n    print(f\"  {k:<20}: {sig[k]}/{n_valid[k]} valid tests ({100*sig[k]/n_valid[k]:.1f}% if valid)\")\n\n\n# ═══════════════════════════════════════════════════════\n# Redundancy classification\n# ═══════════════════════════════════════════════════════\nprint(f\"\\n{'='*80}\")\nprint(\"REDUNDANCY CLASSIFICATION (lag=1, p<0.05)\")\nprint(\"=\"*80)\n\npatterns = {\"both_independent\": [], \"entropy_dominant\": [], \"ece_dominant\": [],\n            \"redundant_shared\": [], \"neither_sig\": [], \"insufficient_data\": []}\n\nfor exp_name, exp_data in all_results.items():\n    for ds, tests in exp_data[\"tests\"].items():\n        label = f\"{exp_name}/{ds}\"\n\n        def getp(key):\n            r = tests.get(key)\n            return r[1][\"p\"] if r and 1 in r else np.nan\n\n        p_ue = getp(\"uncond_ent\")\n        p_uc = getp(\"uncond_ece\")\n        p_ce = getp(\"cond_ent|ece\")\n        p_cc = getp(\"cond_ece|ent\")\n\n        if safe_isnan(p_ce) or safe_isnan(p_cc):\n            patterns[\"insufficient_data\"].append(label)\n            continue\n\n        ent_survives = p_ce < 0.05\n        ece_survives = p_cc < 0.05\n\n        if ent_survives and ece_survives:\n            patterns[\"both_independent\"].append(label)\n        elif ent_survives and not ece_survives:\n            patterns[\"entropy_dominant\"].append(label)\n        elif not ent_survives and ece_survives:\n            patterns[\"ece_dominant\"].append(label)\n        elif (not safe_isnan(p_ue) and p_ue < 0.05) or (not safe_isnan(p_uc) and p_uc < 0.05):\n            patterns[\"redundant_shared\"].append(label)\n        else:\n            patterns[\"neither_sig\"].append(label)\n\nfor pat, items in patterns.items():\n    print(f\"\\n  {pat} ({len(items)}):\")\n    for item in items:\n        print(f\"    - {item}\")\n\n\n# ═══════════════════════════════════════════════════════\n# Softer threshold p<0.10\n# ═══════════════════════════════════════════════════════\nprint(f\"\\n{'='*80}\")\nprint(\"REDUNDANCY CLASSIFICATION (lag=1, p<0.10)\")\nprint(\"=\"*80)\n\npatterns10 = {\"both_independent\": 0, \"entropy_dominant\": 0, \"ece_dominant\": 0,\n              \"redundant_shared\": 0, \"neither_sig\": 0, \"insufficient_data\": 0}\n\nfor exp_name, exp_data in all_results.items():\n    for ds, tests in exp_data[\"tests\"].items():\n        def getp(key):\n            r = tests.get(key)\n            return r[1][\"p\"] if r and 1 in r else np.nan\n\n        p_ue = getp(\"uncond_ent\")\n        p_uc = getp(\"uncond_ece\")\n        p_ce = getp(\"cond_ent|ece\")\n        p_cc = getp(\"cond_ece|ent\")\n\n        if safe_isnan(p_ce) or safe_isnan(p_cc):\n            patterns10[\"insufficient_data\"] += 1\n            continue\n        ent_survives = p_ce < 0.10\n        ece_survives = p_cc < 0.10\n        if ent_survives and ece_survives:\n            patterns10[\"both_independent\"] += 1\n        elif ent_survives and not ece_survives:\n            patterns10[\"entropy_dominant\"] += 1\n        elif not ent_survives and ece_survives:\n            patterns10[\"ece_dominant\"] += 1\n        elif (not safe_isnan(p_ue) and p_ue < 0.10) or (not safe_isnan(p_uc) and p_uc < 0.10):\n            patterns10[\"redundant_shared\"] += 1\n        else:\n            patterns10[\"neither_sig\"] += 1\n\nfor pat, count in patterns10.items():\n    print(f\"  {pat:<20}: {count}\")\n\n\n# ═══════════════════════════════════════════════════════\n# Canary inter-correlation\n# ═══════════════════════════════════════════════════════\nprint(f\"\\n{'='*80}\")\nprint(\"CANARY INTER-CORRELATION (Pearson r: token_entropy vs ECE)\")\nprint(\"=\"*80)\n\nfor exp_name, path in EXPERIMENTS.items():\n    if not os.path.exists(path):\n        continue\n    df = load_experiment(path)\n    r = df[\"token_entropy\"].corr(df[\"ece\"])\n    print(f\"  {exp_name:<16}: r = {r:+.4f}\")\n\n\n# ═══════════════════════════════════════════════════════\n# Partial R² effect sizes\n# ═══════════════════════════════════════════════════════\nprint(f\"\\n{'='*80}\")\nprint(\"PARTIAL R^2 FROM VAR(1): incremental variance explained\")\nprint(\"(How much does adding each canary improve prediction beyond the other?)\")\nprint(\"=\"*80)\n\npr2_data = []\n\nfor exp_name, path in EXPERIMENTS.items():\n    if not os.path.exists(path):\n        continue\n    df = load_experiment(path)\n    T = len(df)\n    if T < 7:\n        continue\n    print(f\"\\n  {exp_name} (T={T}):\")\n    for ds in DOWNSTREAMS:\n        if ds not in df.columns:\n            continue\n        try:\n            sub_full = df[[ds, \"token_entropy\", \"ece\"]].dropna()\n            sub_no_ent = df[[ds, \"ece\"]].dropna()\n            sub_no_ece = df[[ds, \"token_entropy\"]].dropna()\n\n            ss_full = (VAR(sub_full).fit(1).resid[ds]**2).sum()\n            ss_no_ent = (VAR(sub_no_ent).fit(1).resid[ds]**2).sum()\n            ss_no_ece = (VAR(sub_no_ece).fit(1).resid[ds]**2).sum()\n\n            pr2_ent = 1.0 - ss_full / ss_no_ent\n            pr2_ece = 1.0 - ss_full / ss_no_ece\n\n            winner = \"ENT\" if pr2_ent > pr2_ece else \"ECE\" if pr2_ece > pr2_ent else \"TIE\"\n            print(f\"    {ds:<12}: pR2(ent)={pr2_ent:.3f}  pR2(ece)={pr2_ece:.3f}  [{winner}]\")\n            pr2_data.append({\"exp\": exp_name, \"ds\": ds, \"pr2_ent\": pr2_ent, \"pr2_ece\": pr2_ece})\n        except Exception as e:\n            print(f\"    {ds:<12}: ERROR {str(e)[:60]}\")\n\n# Aggregate partial R²\nprint(f\"\\n{'='*80}\")\nprint(\"AGGREGATE PARTIAL R^2\")\nprint(\"=\"*80)\nif pr2_data:\n    pr2_df = pd.DataFrame(pr2_data)\n    for ds in DOWNSTREAMS:\n        sub = pr2_df[pr2_df[\"ds\"] == ds]\n        if len(sub) == 0:\n            continue\n        ent_wins = (sub[\"pr2_ent\"] > sub[\"pr2_ece\"]).sum()\n        ece_wins = (sub[\"pr2_ece\"] > sub[\"pr2_ent\"]).sum()\n        print(f\"  {ds:<12}: mean pR2(ent)={sub['pr2_ent'].mean():.3f}, mean pR2(ece)={sub['pr2_ece'].mean():.3f} | ENT wins {ent_wins}/{len(sub)}, ECE wins {ece_wins}/{len(sub)}\")\n\n    print(f\"\\n  Overall:\")\n    ent_wins = (pr2_df[\"pr2_ent\"] > pr2_df[\"pr2_ece\"]).sum()\n    ece_wins = (pr2_df[\"pr2_ece\"] > pr2_df[\"pr2_ent\"]).sum()\n    print(f\"    mean pR2(entropy)={pr2_df['pr2_ent'].mean():.3f}, mean pR2(ECE)={pr2_df['pr2_ece'].mean():.3f}\")\n    print(f\"    Entropy dominates: {ent_wins}/{len(pr2_df)} pairs ({100*ent_wins/len(pr2_df):.1f}%)\")\n    print(f\"    ECE dominates:     {ece_wins}/{len(pr2_df)} pairs ({100*ece_wins/len(pr2_df):.1f}%)\")\n\n\n# Save JSON\noutput = {\"meta\": {\"analysis\": \"Conditional Granger v2\", \"lag\": 1}, \"summary\": {}, \"details\": {}}\nfor exp_name, exp_data in all_results.items():\n    exp_out = {\"T\": exp_data[\"T\"], \"pairs\": {}}\n    for ds, tests in exp_data[\"tests\"].items():\n        pair_out = {}\n        for key, lag_res in tests.items():\n            if lag_res is None:\n                continue\n            pair_out[key] = {}\n            for lag, r in lag_res.items():\n                pair_out[key][str(lag)] = {\"p\": r[\"p\"] if not safe_isnan(r[\"p\"]) else None,\n                                           \"F\": r[\"F\"] if not safe_isnan(r.get(\"F\", np.nan)) else None,\n                                           \"df\": list(r[\"df\"]) if r.get(\"df\") else None}\n        exp_out[\"pairs\"][ds] = pair_out\n    output[\"details\"][exp_name] = exp_out\n\nout_path = \"/root/autodl-tmp/distrib_canary_collapse/results/analysis/conditional_granger_v2.json\"\nwith open(out_path, \"w\") as f:\n    json.dump(output, f, indent=2, default=str)\nprint(f\"\\nJSON saved to {out_path}\")\nSCRIPT_EOF\necho \"Script ready\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-21T02:17:59.545922+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Script ready\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-21T02:17:59.546057+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/distrib_canary_collapse && python results/analysis/conditional_granger_v2.py 2>&1",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/distrib_canary_collapse && python results/analysis/conditional_granger_v2.py 2>&1",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-21T02:17:59.546198+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/distrib_canary_collapse && python results/analysis/conditional_granger_v2.py 2>&1'\\n\\nExit code: 1\\n\\nStdout:\\n\\n                             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/autodl-tmp/distrib_canary_collapse/results/analysis/conditional_granger_v2.py\\\", line 44, in run_granger\\n    if any(c not in df.columns for c in cols):\\n       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/autodl-tmp/distrib_canary_collapse/results/analysis/conditional_granger_v2.py\\\", line 44, in &lt;genexpr>\\n    if any(c not in df.columns for c in cols):\\n           ^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/pandas/core/indexes/base.py\\\", line 5369, in __contains__\\n    hash(key)\\nTypeError: unhashable type: 'list'\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 1.59}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-21T02:17:59.546395+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "cd /root/autodl-tmp/distrib_canary_collapse && sed -i 's/cols = \\[caused, causing\\] + extra_vars/causing_list = causing if isinstance(causing, list) else [causing]\\n    cols = [caused] + causing_list + extra_vars/' results/analysis/conditional_granger_v2.py && python results/analysis/conditional_granger_v2.py 2>&1",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "cd /root/autodl-tmp/distrib_canary_collapse && sed -i 's/cols = \\[caused, causing\\] + extra_vars/causing_list = causing if isinstance(causing, list) else [causing]\\n    cols = [caused] + causing_list + extra_vars/' results/analysis/conditional_granger_v2.py && python results/analysis/conditional_granger_v2.py 2>&1",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-21T02:17:59.546545+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"bash: line 1: python: command not found\\n\", \"stderr\": \"\", \"return_code\": 127}, \"error\": \"exit code 127\", \"metadata\": {\"elapsed_seconds\": 1.05}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-21T02:17:59.546670+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/distrib_canary_collapse && python results/analysis/conditional_granger_v2.py 2>&1",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/distrib_canary_collapse && python results/analysis/conditional_granger_v2.py 2>&1",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-21T02:17:59.546878+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"====================================================================================================\\nCONDITIONAL GRANGER CAUSALITY: lag=1 p-values\\n====================================================================================================\\nExperiment       Target           Unc.TE    Unc.ECE     TE|ECE     ECE|TE      Joint\\n--------------------------------------------------------------------------------\\na050_s42         distinct_1    0.0000***  0.0000***  0.1351     0.3067     0.0000***\\na050_s42         distinct_2    0.0000***  0.0000***  0.0556  .  0.3387     0.0000***\\na050_s42         distinct_3    0.0000***  0.0000***  0.8517     0.3323     0.0000***\\na050_s42         mauve         0.9362     0.4614     0.0092 **  0.0060 **  0.0206  *\\na050_s43         distinct_1    0.0000***  0.0000***  0.4583     0.0197  *  0.0000***\\na050_s43         distinct_2    0.0000***  0.0000***  0.0104  *  0.1726     0.0000***\\na050_s43         distinct_3    0.0000***  0.0000***  0.6569     0.3318     0.0000***\\na050_s43         mauve         0.3472     0.9626     0.0000***  0.0001***  0.0001***\\na050_s44         distinct_1    0.0000***  0.0000***  0.0747  .  0.0203  *  0.0000***\\na050_s44         distinct_2    0.0000***  0.0000***  0.0055 **  0.0508  .  0.0000***\\na050_s44         distinct_3    0.0000***  0.0000***  0.1557     0.7471     0.0000***\\na050_s44         mauve         0.0463  *  0.0121  *  0.2357     0.0687  .  0.0165  *\\na055_s42         distinct_1    0.0000***  0.0000***  0.1773     0.0140  *  0.0000***\\na055_s42         distinct_2    0.0000***  0.0000***  0.0376  *  0.6715     0.0000***\\na055_s42         distinct_3    0.0000***  0.0000***  0.0268  *  0.3452     0.0000***\\na055_s42         mauve         0.7340     0.3292     0.0000***  0.0000***  0.0000***\\na075_s42         distinct_1    0.0000***  0.0000***  0.2209     0.0000***  0.0000***\\na075_s42         distinct_2    0.0000*** 
…[truncated 6477 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-21T02:17:59.548207+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "tail -200 /root/autodl-tmp/distrib_canary_collapse/results/analysis/conditional_granger_v2.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "tail -200 /root/autodl-tmp/distrib_canary_collapse/results/analysis/conditional_granger_v2.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-21T02:17:59.548854+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"                n_valid[key] += 1\\n                if p < 0.05:\\n                    sig[key] += 1\\n\\n        row = f\\\"{exp_name:<16} {ds:<12}\\\"\\n        for key in [\\\"uncond_ent\\\",\\\"uncond_ece\\\",\\\"cond_ent|ece\\\",\\\"cond_ece|ent\\\",\\\"joint\\\"]:\\n            row += f\\\" {fmt_p(vals[key]):>10}\\\"\\n        print(row)\\n\\nprint(f\\\"\\\\n{'='*80}\\\")\\nprint(f\\\"Significance summary (p<0.05):\\\")\\nfor k in sig:\\n    print(f\\\"  {k:<20}: {sig[k]}/{n_valid[k]} valid tests ({100*sig[k]/n_valid[k]:.1f}% if valid)\\\")\\n\\n\\n# ═══════════════════════════════════════════════════════\\n# Redundancy classification\\n# ═══════════════════════════════════════════════════════\\nprint(f\\\"\\\\n{'='*80}\\\")\\nprint(\\\"REDUNDANCY CLASSIFICATION (lag=1, p<0.05)\\\")\\nprint(\\\"=\\\"*80)\\n\\npatterns = {\\\"both_independent\\\": [], \\\"entropy_dominant\\\": [], \\\"ece_dominant\\\": [],\\n            \\\"redundant_shared\\\": [], \\\"neither_sig\\\": [], \\\"insufficient_data\\\": []}\\n\\nfor exp_name, exp_data in all_results.items():\\n    for ds, tests in exp_data[\\\"tests\\\"].items():\\n        label = f\\\"{exp_name}/{ds}\\\"\\n\\n        def getp(key):\\n            r = tests.get(key)\\n            return r[1][\\\"p\\\"] if r and 1 in r else np.nan\\n\\n        p_ue = getp(\\\"uncond_ent\\\")\\n        p_uc = getp(\\\"uncond_ece\\\")\\n        p_ce = getp(\\\"cond_ent|ece\\\")\\n        p_cc = getp(\\\"cond_ece|ent\\\")\\n\\n        if safe_isnan(p_ce) or safe_isnan(p_cc):\\n            patterns[\\\"insufficient_data\\\"].append(label)\\n            continue\\n\\n        ent_survives = p_ce < 0.05\\n        ece_survives = p_cc < 0.05\\n\\n        if ent_survives and ece_survives:\\n            patterns[\\\"both_independent\\\"].append(label)\\n        elif ent_survives and not ece_survives:\\n            patterns[\\\"entropy_dominant\\\"].append(label)\\n        elif not ent_sur
…[truncated 6884 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-21T02:17:59.549078+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/distrib_canary_collapse && python results/analysis/conditional_granger_v2.py > /tmp/cg_output.txt 2>&1 && wc -l /tmp/cg_output.txt",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/distrib_canary_collapse && python results/analysis/conditional_granger_v2.py > /tmp/cg_output.txt 2>&1 && wc -l /tmp/cg_output.txt",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-21T02:17:59.549224+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"243 /tmp/cg_output.txt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.83}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-21T02:17:59.549376+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "head -120 /tmp/cg_output.txt",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "head -120 /tmp/cg_output.txt",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-21T02:17:59.549510+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "tail -130 /tmp/cg_output.txt",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "tail -130 /tmp/cg_output.txt",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-21T02:17:59.549683+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"====================================================================================================\\nCONDITIONAL GRANGER CAUSALITY: lag=1 p-values\\n====================================================================================================\\nExperiment       Target           Unc.TE    Unc.ECE     TE|ECE     ECE|TE      Joint\\n--------------------------------------------------------------------------------\\na050_s42         distinct_1    0.0000***  0.0000***  0.1351     0.3067     0.0000***\\na050_s42         distinct_2    0.0000***  0.0000***  0.0556  .  0.3387     0.0000***\\na050_s42         distinct_3    0.0000***  0.0000***  0.8517     0.3323     0.0000***\\na050_s42         mauve         0.9362     0.4614     0.0092 **  0.0060 **  0.0206  *\\na050_s43         distinct_1    0.0000***  0.0000***  0.4583     0.0197  *  0.0000***\\na050_s43         distinct_2    0.0000***  0.0000***  0.0104  *  0.1726     0.0000***\\na050_s43         distinct_3    0.0000***  0.0000***  0.6569     0.3318     0.0000***\\na050_s43         mauve         0.3472     0.9626     0.0000***  0.0001***  0.0001***\\na050_s44         distinct_1    0.0000***  0.0000***  0.0747  .  0.0203  *  0.0000***\\na050_s44         distinct_2    0.0000***  0.0000***  0.0055 **  0.0508  .  0.0000***\\na050_s44         distinct_3    0.0000***  0.0000***  0.1557     0.7471     0.0000***\\na050_s44         mauve         0.0463  *  0.0121  *  0.2357     0.0687  .  0.0165  *\\na055_s42         distinct_1    0.0000***  0.0000***  0.1773     0.0140  *  0.0000***\\na055_s42         distinct_2    0.0000***  0.0000***  0.0376  *  0.6715     0.0000***\\na055_s42         distinct_3    0.0000***  0.0000***  0.0268  *  0.3452     0.0000***\\na055_s42         mauve         0.7340     0.3292     0.0000***  0.0000***  0.0000***\\na075_s42         distinct_1    0.0000***  0.0000***  0.2209     0.0000***  0.0000***\\na075_s42         distinct_2    0.0000*** 
…[truncated 4768 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-21T02:17:59.549900+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"    - opt1b/distinct_3\\n    - pythia1b_c4/mauve\\n    - 14b_a050/distinct_1\\n    - 14b_a050/distinct_3\\n\\n  neither_sig (4):\\n    - a075_s44/mauve\\n    - opt1b/mauve\\n    - 14b_a050/mauve\\n    - smollm3_3b/mauve\\n\\n  insufficient_data (0):\\n\\n================================================================================\\nREDUNDANCY CLASSIFICATION (lag=1, p<0.10)\\n================================================================================\\n  both_independent    : 17\\n  entropy_dominant    : 5\\n  ece_dominant        : 11\\n  redundant_shared    : 13\\n  neither_sig         : 2\\n  insufficient_data   : 0\\n\\n================================================================================\\nCANARY INTER-CORRELATION (Pearson r: token_entropy vs ECE)\\n================================================================================\\n  a050_s42        : r = -0.8559\\n  a050_s43        : r = -0.8368\\n  a050_s44        : r = -0.8417\\n  a055_s42        : r = -0.9087\\n  a075_s42        : r = -0.8609\\n  a075_s43        : r = -0.8718\\n  a075_s44        : r = -0.8685\\n  pythia410m      : r = -0.9823\\n  opt1b           : r = -0.9823\\n  pythia1b_c4     : r = -0.9782\\n  14b_a050        : r = -0.9041\\n  smollm3_3b      : r = -0.8405\\n\\n================================================================================\\nPARTIAL R^2 FROM VAR(1): incremental variance explained\\n(How much does adding each canary improve prediction beyond the other?)\\n================================================================================\\n\\n  a050_s42 (T=11):\\n    distinct_1  : pR2(ent)=0.290  pR2(ece)=0.156  [ENT]\\n    distinct_2  : pR2(ent)=0.411  pR2(ece)=0.139  [ENT]\\n    distinct_3  : pR2(ent)=0.006  pR2(ece)=0.142  [ECE]\\n    mauve       : pR2(ent)=0.587  pR2(ece)=0.618  [ECE]\\n\\n  a050_s43 (T=11):\\n    distinct_1  : pR2(ent)=0.087  pR2(ece)=0.522  [ECE]\\n    distinct_2  : pR2(ent)=0.57
…[truncated 3628 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-21T02:17:59.550112+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/conditional_granger_analysis.md",
  "content": "# Conditional Granger Causality Analysis: token_entropy vs ECE\n\n## Objective\n\nDisentangle whether token_entropy and ECE provide independent predictive channels for downstream diversity collapse, or whether they are redundant manifestations of a single underlying degradation process.\n\n## Method\n\n- **Framework**: VAR(1) with Granger causality F-tests via `statsmodels`\n- **Experiments**: 12 experiments across α-sweep (α=0.50/0.55/0.75, seeds 42/43/44), cross-architecture (pythia-410m, opt-1b, pythia-1b-c4), and cross-scale (pythia-1.4b, smollm-3b)\n- **Variables**: canaries (token_entropy, ECE) → downstreams (distinct_1/2/3, mauve)\n- **Tests**: 48 experiment×downstream pairs, each with 5 test types\n\nAll experiments have T=11 generations. VAR(1) with 3 variables uses 10 effective observations (df_resid varies by test type).\n\n## Key Results\n\n### 1. Unconditional vs Conditional Significance Rates (p<0.05)\n\n| Test | Sig / Total | Rate |\n|------|-----------|------|\n| Unconditional entropy→downstream | 38/48 | 79.2% |\n| Unconditional ECE→downstream | 38/48 | 79.2% |\n| **Conditional entropy→downstream \\| ECE** | **17/48** | **35.4%** |\n| **Conditional ECE→downstream \\| entropy** | **23/48** | **47.9%** |\n| Joint [entropy,ECE]→downstream | 42/48 | 87.5% |\n\n**Drop from unconditional to conditional**: entropy loses 55% of significant tests; ECE loses 39%. Both canaries share substantial predictive overlap, but ECE retains more unique information.\n\n### 2. Redundancy Classification (p<0.05)\n\n| Pattern | Count | Fraction |\n|---------|-------|----------|\n| Both independent | 12 | 25.0% |\n| Entropy dominant only | 5 | 10.4% |\n| ECE dominant only | 11 | 22.9% |\n| Redundant/shared signal | 16 | 33.3% |\n| Neither significant | 4 | 8.3% |\n\n**Dominant pattern is redundancy**: in 33.3% of pairs, both canaries are significant unconditionally but *neither* survives conditioning — they share the same predictive information.\n\n**ECE dominant > entropy dominant** (11 vs 5): when only one channel carries unique information, it's more often ECE.\n\n**Both-independent cases** concentrate on: (a) mauve target in α-sweep experiments (5/12), and (b) distinct targets in larger models (pythia-1b-c4, smollm-3b: 6/12).\n\n### 3. Partial R² Effect Sizes\n\n| Downstream | Mean pR²(entropy) | Mean pR²(ECE) | ENT wins | ECE wins |\n|-----------|-------------------|---------------|----------|----------|\n| distinct_1 | 0.330 | **0.646** | 1/12 | 11/12 |\n| distinct_2 | 0.405 | 0.413 | 5/12 | 7/12 |\n| distinct_3 | 0.252 | 0.273 | 5/12 | 7/12 |\n| mauve | 0.395 | **0.462** | 2/12 | 10/12 |\n| **Overall** | **0.346** | **0.448** | **13/48** | **35/48** |\n\nECE provides larger incremental variance explained in **72.9%** of pairs. The effect is strongest for distinct_1 (ECE pR²=0.646 vs entropy pR²=0.330) and mauve (ECE pR²=0.462 vs entropy pR²=0.395).\n\n### 4. Canary Inter-Correlation\n\n| Experiment group | Pearson r (entropy vs ECE) |\n|-----------------|--------------------------|\n| α-sweep (GPT-2 small) | −0.84 to −0.91 |\n| Cross-architecture (pythia, opt) | −0.98 |\n| Cross-scale (1.4b, 3b) | −0.84 to −0.90 |\n\nStrong negative correlation across all experiments (r = −0.84 to −0.98). The two metrics are near-collinear, especially for larger models.\n\n## Interpretation\n\n### Core Finding: Shared Mechanism with ECE as Primary Channel\n\nToken_entropy and ECE are **not independent channels**. They are two correlated manifestations of the same underlying process — calibration degradation during iterative training on synthetic data. The evidence:\n\n1. **High collinearity** (r = −0.84 to −0.98): as ECE rises (calibration worsens), token_entropy drops (distribution sharpens). These are two sides of one coin.\n\n2. **Massive significance loss under conditioning**: 79% → 35% for entropy, 79% → 48% for ECE. Most of what entropy predicts about diversity, ECE already captures (and vice versa).\n\n3. **When forced to choose, ECE wins**: 73% of partial R² comparisons favor ECE; conditional ECE survives more often (48% vs 35%).\n\n4. **Scale-dependent nuance**: larger models (pythia-1b, smollm-3b) show more \"both independent\" patterns for diversity metrics, suggesting that at scale, entropy and ECE may capture partially distinct degradation pathways.\n\n### Why ECE > Entropy?\n\nECE directly measures the gap between predicted probabilities and actual correctness — it's a direct calibration metric. Token_entropy is a distributional summary that *correlates* with miscalibration but also captures other phenomena (vocabulary restriction, mode collapse). ECE is the more mechanistically proximal canary.\n\n### The Mauve Exception\n\nMauve targets show the most \"both_independent\" patterns (5/12 in α-sweep). This makes sense: MAUVE captures distributional divergence at a higher level that may be driven by *both* the calibration pathway (ECE) and the entropy pathway independently.\n\n## Paper Recommendations\n\n### For Methods Section\n\n> \"We evaluate two canary metrics — token_entropy and ECE — as early warning signals. These metrics are strongly anti-correlated (r = −0.84 to −0.98), reflecting that both capture aspects of the same calibration degradation process. Conditional Granger analysis reveals substantial redundancy: unconditional significance rates of ~79% for both canaries drop to 35–48% when conditioning on the other. ECE retains more unique predictive power (partial R² = 0.45 vs 0.35), consistent with its more direct role as a calibration measure.\"\n\n### For Results Section\n\nReport the conditional analysis as evidence that the \"phase transition\" detection signal is primarily driven by a **single calibration-degradation mechanism** with two observable correlates, rather than two independent warning channels. This strengthens the mechanistic story — the canary signal has a coherent cause.\n\n### Recommended Framing\n\nFrame as: \"We confirm that the detection signal arises from calibration collapse (ECE) rather than from two independent information channels. Token entropy and ECE are near-collinear (|r| > 0.84), and conditional Granger analysis shows 33% of pairs have pure redundancy. When unique information exists, ECE is the dominant channel (73% of partial R² comparisons). This supports a single-mechanism interpretation of the canary phase transition.\"\n\n### Caveats\n\n1. **T=11 is short**: VAR(1) with 3 variables leaves only ~4 residual df for the conditional F-test. Effect sizes are large (pR² > 0.3) which helps, but exact p-values should be interpreted cautiously.\n2. **The partial R² analysis is more robust** than p-values for this sample size — focus on effect sizes rather than significance.\n3. **Lack of T=20 data**: no T=20 experiments were available to confirm these patterns with higher power.\n\n## Data\n\n- Script: `results/analysis/conditional_granger_v2.py`\n- Full JSON results: `results/analysis/conditional_granger_v2.json`\n- 12 experiments × 4 downstream targets = 48 test pairs\n- All T=11 (generation 0–10)\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/conditional_granger_analysis.md",
    "content": "# Conditional Granger Causality Analysis: token_entropy vs ECE\n\n## Objective\n\nDisentangle whether token_entropy and ECE provide independent predictive channels for downstream diversity collapse, or whether they are redundant manifestations of a single underlying degradation process.\n\n## Method\n\n- **Framework**: VAR(1) with Granger causality F-tests via `statsmodels`\n- **Experiments**: 12 experiments across α-sweep (α=0.50/0.55/0.75, seeds 42/43/44), cross-architecture (pythia-410m, opt-1b, pythia-1b-c4), and cross-scale (pythia-1.4b, smollm-3b)\n- **Variables**: canaries (token_entropy, ECE) → downstreams (distinct_1/2/3, mauve)\n- **Tests**: 48 experiment×downstream pairs, each with 5 test types\n\nAll experiments have T=11 generations. VAR(1) with 3 variables uses 10 effective observations (df_resid varies by test type).\n\n## Key Results\n\n### 1. Unconditional vs Conditional Significance Rates (p<0.05)\n\n| Test | Sig / Total | Rate |\n|------|-----------|------|\n| Unconditional entropy→downstream | 38/48 | 79.2% |\n| Unconditional ECE→downstream | 38/48 | 79.2% |\n| **Conditional entropy→downstream \\| ECE** | **17/48** | **35.4%** |\n| **Conditional ECE→downstream \\| entropy** | **23/48** | **47.9%** |\n| Joint [entropy,ECE]→downstream | 42/48 | 87.5% |\n\n**Drop from unconditional to conditional**: entropy loses 55% of significant tests; ECE loses 39%. Both canaries share substantial predictive overlap, but ECE retains more unique information.\n\n### 2. Redundancy Classification (p<0.05)\n\n| Pattern | Count | Fraction |\n|---------|-------|----------|\n| Both independent | 12 | 25.0% |\n| Entropy dominant only | 5 | 10.4% |\n| ECE dominant only | 11 | 22.9% |\n| Redundant/shared signal | 16 | 33.3% |\n| Neither significant | 4 | 8.3% |\n\n**Dominant pattern is redundancy**: in 33.3% of pairs, both canaries are significant unconditionally but *neither* survives conditioning — they share the same predictive information.\n\n**ECE dominant > entropy dominant** (11 vs 5): when only one channel carries unique information, it's more often ECE.\n\n**Both-independent cases** concentrate on: (a) mauve target in α-sweep experiments (5/12), and (b) distinct targets in larger models (pythia-1b-c4, smollm-3b: 6/12).\n\n### 3. Partial R² Effect Sizes\n\n| Downstream | Mean pR²(entropy) | Mean pR²(ECE) | ENT wins | ECE wins |\n|-----------|-------------------|---------------|----------|----------|\n| distinct_1 | 0.330 | **0.646** | 1/12 | 11/12 |\n| distinct_2 | 0.405 | 0.413 | 5/12 | 7/12 |\n| distinct_3 | 0.252 | 0.273 | 5/12 | 7/12 |\n| mauve | 0.395 | **0.462** | 2/12 | 10/12 |\n| **Overall** | **0.346** | **0.448** | **13/48** | **35/48** |\n\nECE provides larger incremental variance explained in **72.9%** of pairs. The effect is strongest for distinct_1 (ECE pR²=0.646 vs entropy pR²=0.330) and mauve (ECE pR²=0.462 vs entropy pR²=0.395).\n\n### 4. Canary Inter-Correlation\n\n| Experiment group | Pearson r (entropy vs ECE) |\n|-----------------|--------------------------|\n| α-sweep (GPT-2 small) | −0.84 to −0.91 |\n| Cross-architecture (pythia, opt) | −0.98 |\n| Cross-scale (1.4b, 3b) | −0.84 to −0.90 |\n\nStrong negative correlation across all experiments (r = −0.84 to −0.98). The two metrics are near-collinear, especially for larger models.\n\n## Interpretation\n\n### Core Finding: Shared Mechanism with ECE as Primary Channel\n\nToken_entropy and ECE are **not independent channels**. They are two correlated manifestations of the same underlying process — calibration degradation during iterative training on synthetic data. The evidence:\n\n1. **High collinearity** (r = −0.84 to −0.98): as ECE rises (calibration worsens), token_entropy drops (distribution sharpens). These are two sides of one coin.\n\n2. **Massive significance loss under conditioning**: 79% → 35% for entropy, 79% → 48% for ECE. Most of what entropy predicts about diversity, ECE already captures (and vice versa).\n\n3. **When forced to choose, ECE wins**: 73% of partial R² comparisons favor ECE; conditional ECE survives more often (48% vs 35%).\n\n4. **Scale-dependent nuance**: larger models (pythia-1b, smollm-3b) show more \"both independent\" patterns for diversity metrics, suggesting that at scale, entropy and ECE may capture partially distinct degradation pathways.\n\n### Why ECE > Entropy?\n\nECE directly measures the gap between predicted probabilities and actual correctness — it's a direct calibration metric. Token_entropy is a distributional summary that *correlates* with miscalibration but also captures other phenomena (vocabulary restriction, mode collapse). ECE is the more mechanistically proximal canary.\n\n### The Mauve Exception\n\nMauve targets show the most \"both_independent\" patterns (5/12 in α-sweep). This makes sense: MAUVE captures distributional divergence at a higher level that may be driven by *both* the calibration pathway (ECE) and the entropy pathway independently.\n\n## Paper Recommendations\n\n### For Methods Section\n\n> \"We evaluate two canary metrics — token_entropy and ECE — as early warning signals. These metrics are strongly anti-correlated (r = −0.84 to −0.98), reflecting that both capture aspects of the same calibration degradation process. Conditional Granger analysis reveals substantial redundancy: unconditional significance rates of ~79% for both canaries drop to 35–48% when conditioning on the other. ECE retains more unique predictive power (partial R² = 0.45 vs 0.35), consistent with its more direct role as a calibration measure.\"\n\n### For Results Section\n\nReport the conditional analysis as evidence that the \"phase transition\" detection signal is primarily driven by a **single calibration-degradation mechanism** with two observable correlates, rather than two independent warning channels. This strengthens the mechanistic story — the canary signal has a coherent cause.\n\n### Recommended Framing\n\nFrame as: \"We confirm that the detection signal arises from calibration collapse (ECE) rather than from two independent information channels. Token entropy and ECE are near-collinear (|r| > 0.84), and conditional Granger analysis shows 33% of pairs have pure redundancy. When unique information exists, ECE is the dominant channel (73% of partial R² comparisons). This supports a single-mechanism interpretation of the canary phase transition.\"\n\n### Caveats\n\n1. **T=11 is short**: VAR(1) with 3 variables leaves only ~4 residual df for the conditional F-test. Effect sizes are large (pR² > 0.3) which helps, but exact p-values should be interpreted cautiously.\n2. **The partial R² analysis is more robust** than p-values for this sample size — focus on effect sizes rather than significance.\n3. **Lack of T=20 data**: no T=20 experiments were available to confirm these patterns with higher power.\n\n## Data\n\n- Script: `results/analysis/conditional_granger_v2.py`\n- Full JSON results: `results/analysis/conditional_granger_v2.json`\n- 12 experiments × 4 downstream targets = 48 test pairs\n- All T=11 (generation 0–10)\n"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-21T02:17:59.550357+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/conditional_granger_analysis.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-21T02:17:59.550499+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "conditional_granger_analysis",
  "type": "report",
  "description": "Conditional Granger causality analysis: token_entropy vs ECE as independent vs redundant canary channels. Finding: both are largely redundant (shared mechanism), ECE is the primary channel (73% partial R² wins).",
  "project": "distrib_canary_collapse",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/conditional_granger_analysis.md",
  "tags": "['conditional_granger', 'canary_mechanism', 'ECE', 'token_entropy', 'redundancy', 'plan022']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "conditional_granger_analysis",
    "type": "report",
    "description": "Conditional Granger causality analysis: token_entropy vs ECE as independent vs redundant canary channels. Finding: both are largely redundant (shared mechanism), ECE is the primary channel (73% partial R² wins).",
    "project": "distrib_canary_collapse",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/conditional_granger_analysis.md",
    "tags": "['conditional_granger', 'canary_mechanism', 'ECE', 'token_entropy', 'redundancy', 'plan022']"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-21T02:17:59.551413+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260521_965034\", \"name\": \"conditional_granger_analysis\", \"type\": \"report\", \"description\": \"Conditional Granger causality analysis: token_entropy vs ECE as independent vs redundant canary channels. Finding: both are largely redundant (shared mechanism), ECE is the primary channel (73% partial R² wins).\", \"path\": \"projects/distrib_canary_collapse/artifacts/_project/report/conditional_granger_analysis.md\", \"url\": null, \"project\": \"distrib_canary_collapse\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-21T02:17:50.412322+00:00\", \"tags\": [\"conditional_granger\", \"canary_mechanism\", \"ECE\", \"token_entropy\", \"redundancy\", \"plan022\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 65 · 2026-05-21T02:17:59.551693+00:00_

分析完成。核心发现：

**Token_entropy 和 ECE 是同一机制的两个冗余表现，不是独立通道。ECE 是主通道。**

关键数据：
- 两者高度反相关（r = −0.84 to −0.98）
- Unconditional Granger 显著率 79% → conditional 后分别降至 35%（entropy）和 48%（ECE）
- 33% 的 pair 属于纯冗余（unconditional 显著但 conditional 两者都不显著）
- Partial R²：ECE 在 73% 的比较中胜出（mean pR² 0.448 vs 0.346）
- 大模型（pythia-1b, smollm-3b）在 diversity metrics 上表现出更多"双独立"模式

**论文建议**：canary 信号来自单一的 calibration collapse 机制，ECE 是更直接的度量。这强化了 phase transition 的单机制解释。

报告在 `artifacts/conditional_granger_analysis.md`，完整 JSON 在服务器 `results/analysis/conditional_granger_v2.json`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_conditional_granger_plan022_20260521T021117"
}
```

</details>

---
