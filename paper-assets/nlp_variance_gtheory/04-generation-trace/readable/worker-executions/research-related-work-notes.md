# research related work notes

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/workers/worker_research_related_work_notes_20260520T171046.log`
- **Structured JSON:** [`f6d27c7fff979c7294c9.json`](../../sessions/f6/f6d27c7fff979c7294c9.json)

## Before a recorded user message

23 recorded events

### Log line

_source line 1_

Warning: no stdin data received in 3s, proceeding without it. If piping from a slow command, redirect stdin explicitly: < /dev/null to skip, or wait longer.

---

### System

_source line 2_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "session_id": "a8cdf46c-6eca-49b9-b703-27332b7232e2",
  "tools": [
    "Task",
    "AskUserQuestion",
    "Bash",
    "CronCreate",
    "CronDelete",
    "CronList",
    "Edit",
    "EnterPlanMode",
    "EnterWorktree",
    "ExitPlanMode",
    "ExitWorktree",
    "Glob",
    "Grep",
    "ListMcpResourcesTool",
    "Monitor",
    "NotebookEdit",
    "PushNotification",
    "Read",
    "ReadMcpResourceTool",
    "RemoteTrigger",
    "ScheduleWakeup",
    "Skill",
    "TaskOutput",
    "TaskStop",
    "TodoWrite",
    "ToolSearch",
    "WebFetch",
    "WebSearch",
    "Write",
    "mcp__agent-ml-research__append_idea",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__save_project_file"
  ],
  "mcp_servers": [
    {
      "name": "agent-ml-research",
      "status": "connected"
    }
  ],
  "model": "claude-opus-4-6",
  "permissionMode": "bypassPermissions",
  "slash_commands": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api",
    "clear",
    "compact",
    "context",
    "heapdump",
    "init",
    "review",
    "security-review",
    "extra-usage",
    "usage",
    "insights",
    "team-onboarding"
  ],
  "apiKeySource": "none",
  "claude_code_version": "2.1.126",
  "output_style": "default",
  "agents": [
    "claude",
    "Explore",
    "general-purpose",
    "Plan",
    "statusline-setup"
  ],
  "skills": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api"
  ],
  "plugins": [],
  "analytics_disabled": false,
  "uuid": "2c980e59-14ae-42ec-a9c8-fc61bd93509f",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0519-projects-nlp-variance-gtheory/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Runtime record

_source line 3_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1779314400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "8d7e1bfd-abfe-4d63-9bd5-081d30953903",
  "session_id": "a8cdf46c-6eca-49b9-b703-27332b7232e2"
}
```

---

### Assistant

_source line 4_

我先读取所需的输入文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8cdf46c-6eca-49b9-b703-27332b7232e2",
  "uuid": "8113d147-dbd8-404e-a44c-26940c8f57a8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rbdxx4XHRCfkuw99GVK4fC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11968,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11968
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 5_

<details open><summary>🔧 Tool call — Read · `toolu_01Xk5QYjPSSJJ998cmiJiDHu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/skills/projects/nlp_variance_gtheory/distilled-research.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8cdf46c-6eca-49b9-b703-27332b7232e2",
  "uuid": "ace46192-503c-47ff-a516-c673282a3293",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rbdxx4XHRCfkuw99GVK4fC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11968,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11968
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T17:10:58.325Z_

<details><summary>↩ Tool result · `toolu_01Xk5QYjPSSJJ998cmiJiDHu`</summary>

```text
1	---
2	name: LLM Evaluation Variance — Research Patterns
3	description: Experimental consensus on variance sources, decomposition methods, and gaps in LLM evaluation reproducibility (10 papers, 2024-2026)
4	type: research
5	source_papers: 10
6	---
7	
8	## Variance Source Taxonomy
9	
10	**Infrastructure variance** (4/10; high confidence):
11	- Numerical precision: BF16→9% accuracy std; FP32→~0% (Yuan 2025). Reasoning models most affected.
12	- Batch-size dependence: 80/1000 unique completions at T=0 from batch-invariance failure in RMSNorm/GEMM/attention (ThinkingMachines 2025).
13	- Background randomness at T=0: GPT~0.075, Gemini~0.065, Claude~0 effective temperature (Messina TMLR 2026).
14	
15	**Methodological variance** (6/10; high confidence):
16	- Judge choice dominates safety eval (43.8% variance); prompt~50% in open models, ~25% commercial (Mesting 2026, Brittlebench 2026).
17	- Much apparent prompt sensitivity is evaluation artifact — LLM-judge raises rank correlation 0.30→0.95 (Hua EMNLP 2025).
18	- Standard CIs omit 40-60% uncertainty; naive 95% CIs→79% coverage at scale (Mesting 2026).
19	
20	## Decomposition Frameworks
21	
22	| Framework | Paper | Method |
23	|-----------|-------|--------|
24	| TEE (G-theory) | Mesting 2026 | REML + D-study, facets: item/prompt/judge/temp |
25	| Total Variance | Brittlebench 2026 | V_data + V_brittleness via ANOVA |
26	| Intent Decomp | Kunievsky 2025 | intent/articulation/model uncertainty |
27	| Background Temp | Messina 2026 | Reference calibration→single T_bg scalar |
28	
29	G-theory adaptation is the most rigorous approach (Mesting). 4/10 papers use variance decomposition. **High confidence.**
30	
31	## Benchmarks & Models
32	
33	Top benchmarks: MMLU (3), GPQA (3), MATH (3), ARC (2), TruthfulQA (2). Models: Llama/Qwen/GPT families (5 papers each); 7B-8B open-weight as standard testbed. 10-100 runs per config is norm. **High confidence.**
34	
35	## Mitigations
36	
37	- LayerCast (BF16 store+FP32 compute): <3.4% divergence, 34% memory savings (Yuan). **Medium.**
38	- Batch-invariant kernels: determinism at 1.6-2.1× latency (ThinkingMachines). **Medium.**
39	- TEE-guided design: halves RMSE; 3 judges→38% SE reduction (Mesting). **Medium.**
40	
41	## Critical Gap — Our Niche
42	
43	**No paper unifies infrastructure (precision/batch/hardware) with methodological (prompt/judge/temp) variance in one G-theory framework.** Mesting applies G-theory to methodological facets only; Yuan/ThinkingMachines characterize infra variance without G-theory. Additional gaps: no cross-lingual analysis; training-time seed variance disconnected from inference-time; no standardized variance reporting protocol. **Support: 10/10 (absence), high confidence.**
44	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a8cdf46c-6eca-49b9-b703-27332b7232e2",
  "uuid": "d2bc70ea-043e-4f18-8ca1-e674917e24c4",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/skills/projects/nlp_variance_gtheory/distilled-research.skill.md",
      "content": "---\nname: LLM Evaluation Variance — Research Patterns\ndescription: Experimental consensus on variance sources, decomposition methods, and gaps in LLM evaluation reproducibility (10 papers, 2024-2026)\ntype: research\nsource_papers: 10\n---\n\n## Variance Source Taxonomy\n\n**Infrastructure variance** (4/10; high confidence):\n- Numerical precision: BF16→9% accuracy std; FP32→~0% (Yuan 2025). Reasoning models most affected.\n- Batch-size dependence: 80/1000 unique completions at T=0 from batch-invariance failure in RMSNorm/GEMM/attention (ThinkingMachines 2025).\n- Background randomness at T=0: GPT~0.075, Gemini~0.065, Claude~0 effective temperature (Messina TMLR 2026).\n\n**Methodological variance** (6/10; high confidence):\n- Judge choice dominates safety eval (43.8% variance); prompt~50% in open models, ~25% commercial (Mesting 2026, Brittlebench 2026).\n- Much apparent prompt sensitivity is evaluation artifact — LLM-judge raises rank correlation 0.30→0.95 (Hua EMNLP 2025).\n- Standard CIs omit 40-60% uncertainty; naive 95% CIs→79% coverage at scale (Mesting 2026).\n\n## Decomposition Frameworks\n\n| Framework | Paper | Method |\n|-----------|-------|--------|\n| TEE (G-theory) | Mesting 2026 | REML + D-study, facets: item/prompt/judge/temp |\n| Total Variance | Brittlebench 2026 | V_data + V_brittleness via ANOVA |\n| Intent Decomp | Kunievsky 2025 | intent/articulation/model uncertainty |\n| Background Temp | Messina 2026 | Reference calibration→single T_bg scalar |\n\nG-theory adaptation is the most rigorous approach (Mesting). 4/10 papers use variance decomposition. **High confidence.**\n\n## Benchmarks & Models\n\nTop benchmarks: MMLU (3), GPQA (3), MATH (3), ARC (2), TruthfulQA (2). Models: Llama/Qwen/GPT families (5 papers each); 7B-8B open-weight as standard testbed. 10-100 runs per config is norm. **High confidence.**\n\n## Mitigations\n\n- LayerCast (BF16 store+FP32 compute): <3.4% divergence, 34% memory savings (Yuan). **Medium.**\n- Batch-invariant kernels: determinism at 1.6-2.1× latency (ThinkingMachines). **Medium.**\n- TEE-guided design: halves RMSE; 3 judges→38% SE reduction (Mesting). **Medium.**\n\n## Critical Gap — Our Niche\n\n**No paper unifies infrastructure (precision/batch/hardware) with methodological (prompt/judge/temp) variance in one G-theory framework.** Mesting applies G-theory to methodological facets only; Yuan/ThinkingMachines characterize infra variance without G-theory. Additional gaps: no cross-lingual analysis; training-time seed variance disconnected from inference-time; no standardized variance reporting protocol. **Support: 10/10 (absence), high confidence.**\n",
      "numLines": 44,
      "startLine": 1,
      "totalLines": 44
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_015ZfkAkgH4DExQPfb46n8Pg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/skills/projects/nlp_variance_gtheory/distilled-writing.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8cdf46c-6eca-49b9-b703-27332b7232e2",
  "uuid": "38d59091-4dc8-4fb6-baec-39ea0fe0809d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rbdxx4XHRCfkuw99GVK4fC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11968,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11968
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T17:10:58.795Z_

<details><summary>↩ Tool result · `toolu_015ZfkAkgH4DExQPfb46n8Pg`</summary>

```text
1	---
2	name: LLM Evaluation Variance — Writing Patterns
3	description: Narrative strategies, figure/table conventions from LLM evaluation variance papers (8 deep-read, 2024-2026)
4	type: writing
5	source_papers: 8
6	---
7	
8	## Story Types
9	
10	- **Breaking limitations** (3/8): Brittlebench, Yuan, ThinkingMachines. "Everyone assumed X, we show it fails." High.
11	- **Simplification** (2/8): Hua, GeneralizIT. "Complex problem, simpler real answer." Medium.
12	- **Unifying framework** (2/8): Kunievsky, Messina. "Scattered observations, one formalism." Medium.
13	- **Cross-domain transfer** (1/8): Mesting (psychometrics→ML). Our paper fits this type — study Mesting's structure. Low but critical.
14	
15	## Hook: Counter-Intuitive Claim Dominates (4/8, high)
16	
17	"Greedy≠deterministic" (Yuan), "80/1000 unique at T=0" (ThinkingMachines), "sensitivity is artifact" (Hua), "95% CIs→79% coverage" (Mesting). **Pattern**: open with a concrete number violating expectations. Avoid vague "X is important."
18	
19	## Tension: "Everyone's Doing It Wrong" (4/8, high)
20	
21	(1) Cite widespread practice, (2) quantified evidence it fails, (3) identify overlooked factor. ThinkingMachines adds a twist: debunk the accepted explanation before presenting the correct one.
22	
23	## Intro: 4 Paragraphs + 3 Contributions (mode)
24	
25	(1) Context, (2) existing approaches + limitation, (3) gap/surprise, (4) contributions. 3 contributions standard: framework + empirical finding + practical tool. **Support: 5/8, high.**
26	
27	## Figure Conventions
28	
29	**Figure 1**: problem_illustration (4/8) — show problem exists before solution. Concrete examples with before/after or divergence visualization. **High.**
30	
31	**Result figures**: bar charts primary (5/8); stacked bars for variance decomposition (2/8, Mesting/Brittlebench — expected idiom for our paper); line plots for trends (3/8); heatmaps for divergence (2/8). **High.**
32	
33	**Figure count**: 4-6 total. **Flow**: problem illustration → method diagram → variance decomposition → D-study projections. **Support: 6/8, high.**
34	
35	## Table Conventions
36	
37	**Main table**: rows=models/configs, cols=benchmarks×metrics, grouped by category (commercial/open or reasoning/non-reasoning). Bold best, 4-8 baselines. **Support: 5/8, high.**
38	
39	**Ablation**: full_numbers (5/8) over checkmark_grid (2/8). Checkmark only for component-presence ablation. **High.**
40	
41	**Reporting**: std across configs/runs standard; only Mesting reports full REML components. **High.**
42	
43	**Figure vs table split**: figures for decomposition visuals/trends/qualitative; tables for exact numbers/comparisons. Appendix for per-config breakdowns and validation. **Support: 6/8, high.**
44	
45	## Our Paper Blueprint
46	
47	Open with shocking quantified finding about unreported variance → "everyone's CIs are wrong" tension → G-theory as borrowed lens → 2-3 domain demonstrations → stacked-bar variance decomposition as signature visual → D-study projections as practical value.
48	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a8cdf46c-6eca-49b9-b703-27332b7232e2",
  "uuid": "24fdb634-0a76-49b0-ae15-f092472cb5c4",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/skills/projects/nlp_variance_gtheory/distilled-writing.skill.md",
      "content": "---\nname: LLM Evaluation Variance — Writing Patterns\ndescription: Narrative strategies, figure/table conventions from LLM evaluation variance papers (8 deep-read, 2024-2026)\ntype: writing\nsource_papers: 8\n---\n\n## Story Types\n\n- **Breaking limitations** (3/8): Brittlebench, Yuan, ThinkingMachines. \"Everyone assumed X, we show it fails.\" High.\n- **Simplification** (2/8): Hua, GeneralizIT. \"Complex problem, simpler real answer.\" Medium.\n- **Unifying framework** (2/8): Kunievsky, Messina. \"Scattered observations, one formalism.\" Medium.\n- **Cross-domain transfer** (1/8): Mesting (psychometrics→ML). Our paper fits this type — study Mesting's structure. Low but critical.\n\n## Hook: Counter-Intuitive Claim Dominates (4/8, high)\n\n\"Greedy≠deterministic\" (Yuan), \"80/1000 unique at T=0\" (ThinkingMachines), \"sensitivity is artifact\" (Hua), \"95% CIs→79% coverage\" (Mesting). **Pattern**: open with a concrete number violating expectations. Avoid vague \"X is important.\"\n\n## Tension: \"Everyone's Doing It Wrong\" (4/8, high)\n\n(1) Cite widespread practice, (2) quantified evidence it fails, (3) identify overlooked factor. ThinkingMachines adds a twist: debunk the accepted explanation before presenting the correct one.\n\n## Intro: 4 Paragraphs + 3 Contributions (mode)\n\n(1) Context, (2) existing approaches + limitation, (3) gap/surprise, (4) contributions. 3 contributions standard: framework + empirical finding + practical tool. **Support: 5/8, high.**\n\n## Figure Conventions\n\n**Figure 1**: problem_illustration (4/8) — show problem exists before solution. Concrete examples with before/after or divergence visualization. **High.**\n\n**Result figures**: bar charts primary (5/8); stacked bars for variance decomposition (2/8, Mesting/Brittlebench — expected idiom for our paper); line plots for trends (3/8); heatmaps for divergence (2/8). **High.**\n\n**Figure count**: 4-6 total. **Flow**: problem illustration → method diagram → variance decomposition → D-study projections. **Support: 6/8, high.**\n\n## Table Conventions\n\n**Main table**: rows=models/configs, cols=benchmarks×metrics, grouped by category (commercial/open or reasoning/non-reasoning). Bold best, 4-8 baselines. **Support: 5/8, high.**\n\n**Ablation**: full_numbers (5/8) over checkmark_grid (2/8). Checkmark only for component-presence ablation. **High.**\n\n**Reporting**: std across configs/runs standard; only Mesting reports full REML components. **High.**\n\n**Figure vs table split**: figures for decomposition visuals/trends/qualitative; tables for exact numbers/comparisons. Appendix for per-config breakdowns and validation. **Support: 6/8, high.**\n\n## Our Paper Blueprint\n\nOpen with shocking quantified finding about unreported variance → \"everyone's CIs are wrong\" tension → G-theory as borrowed lens → 2-3 domain demonstrations → stacked-bar variance decomposition as signature visual → D-study projections as practical value.\n",
      "numLines": 48,
      "startLine": 1,
      "totalLines": 48
    }
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01VKpiJEGAGZoZPw7CZSuTy4`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8cdf46c-6eca-49b9-b703-27332b7232e2",
  "uuid": "8298ca9e-cc5a-4a53-a83d-241c0f05a421",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rbdxx4XHRCfkuw99GVK4fC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11968,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11968
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T17:10:59.193Z_

<details><summary>↩ Tool result · `toolu_01VKpiJEGAGZoZPw7CZSuTy4`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__register_artifact"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a8cdf46c-6eca-49b9-b703-27332b7232e2",
  "uuid": "dcd2e63f-c2ea-4c97-8322-4cfe6e276c66",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Assistant

_source line 11_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the ideas.md and ROADMAP.md files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8cdf46c-6eca-49b9-b703-27332b7232e2",
  "uuid": "47ee0b64-9221-4c98-97b9-6dcd75b7f968",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ksupeiDq8AYXDpEkyUeqP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3145,
      "cache_read_input_tokens": 23809,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3145
      },
      "output_tokens": 48,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01WYdrn7bZnpFJbjGeSBUEfb`</summary>

```json
{
  "project": "nlp_variance_gtheory",
  "file": "ideas.md",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8cdf46c-6eca-49b9-b703-27332b7232e2",
  "uuid": "82eddfd9-7f4f-4846-b38e-19c6b0362b1b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ksupeiDq8AYXDpEkyUeqP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3145,
      "cache_read_input_tokens": 23809,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3145
      },
      "output_tokens": 48,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-20T17:11:03.642Z_

<details><summary>↩ Tool result · `toolu_01WYdrn7bZnpFJbjGeSBUEfb`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'nlp_variance_gtheory'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a8cdf46c-6eca-49b9-b703-27332b7232e2",
  "uuid": "9e153f82-a3ab-49d7-839a-687dd408e085",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"No ideas.md found for 'nlp_variance_gtheory'.\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'nlp_variance_gtheory'.\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0194TcJtJdVwnxJMCorVABir`</summary>

```json
{
  "project": "nlp_variance_gtheory",
  "file": "ROADMAP.md",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8cdf46c-6eca-49b9-b703-27332b7232e2",
  "uuid": "a25dee8e-62a2-451a-ae76-91f8df99a072",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ksupeiDq8AYXDpEkyUeqP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3145,
      "cache_read_input_tokens": 23809,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3145
      },
      "output_tokens": 48,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-20T17:11:03.715Z_

<details><summary>↩ Tool result · `toolu_0194TcJtJdVwnxJMCorVABir`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/ROADMAP.md\", \"content\": \"# nlp_variance_gtheory — Research Dashboard\\n\\n> 最后更新: 2026-05-20 14:17 UTC | 更新原因: 服务器就绪，MVP 调整为 Phase A（单硬件三精度 108 条件），Agent 已派出部署\\n\\n## 核心方向\\n用 Generalizability Theory 联合分解 LLM 评估中基础设施因素（硬件类型、数值精度）与方法论因素（prompt 措辞、随机种子、温度、few-shot 顺序）的方差，检验 \\\"separability 假设\\\"。产出可量化的 reproducibility budget（D-study）。\\n\\n## 当前进展\\n- 阶段: MVP 验证\\n- 服务器: westd-32570（4× RTX 6000 PRO 96GB）已绑定，4 卡全部分配\\n- 代码: 18 文件已完成，Agent 正在部署到服务器\\n- 文献图谱: 10 篇核心论文，蒸馏完成（v1）\\n- 第二种 GPU 类型: 已向 Manager 申请（A100/H100），等待回复\\n\\n## MVP 验证方案（Phase A — 单硬件 + 三精度）\\n**核心假设**: G-theory 可成功分解 infrastructure × methodology 交叉方差分量。\\n\\n**调整后设计**（因当前只有 1 种 GPU 类型）:\\n- 1 模型: Llama-3.1-8B-Instruct\\n- 1 硬件: RTX 6000 PRO 96GB\\n- 3 精度: FP32, BF16, FP16（96GB VRAM 支持 FP32）\\n- 3 prompt paraphrases × 3 seeds × 2 温度 × 2 orderings\\n- 共 **108 条件** × 50 MMLU items = 5,400 次推理\\n\\n**Pass/Fail（已量化）**:\\n- PASS: (a) pipeline 完整运行; (b) 方差分解收敛; (c) ≥2 个方差分量占总方差 ≥5% 或 bootstrap 95% CI 不含零（含 ≥1 precision×methodology 交互项）\\n- FAIL: 分解不收敛 / 全条件零方差 / 种子控制失效\\n\\n**Phase B（待第二种 GPU 到位）**: 加入硬件因素，完成 hardware × methodology 交叉。\\n\\n## 近期任务\\n- [x] GPU 服务器配置\\n- [ ] Agent 环境搭建 + 代码部署（进行中）\\n- [ ] Seed determinism sanity check（同配置 10 次重复）\\n- [ ] 正式 MVP Phase A（108 条件）\\n- [ ] 方差分解分析 → pass/fail 判定\\n- [ ] 等待 Manager 回复第二种 GPU 类型\\n\\n## GPU 预算\\n- 本项目分配: westd-32570 cuda:0-3（4× RTX 6000 PRO 96GB）\\n- MVP Phase A 预估: ~8 GPU·h\\n- 全研究预估: ~2,200 GPU·h（需额外 A100/H100）\\n\\n## 投稿目标\\n- 主投: AAAI 2027（abstract Jul 21, paper Jul 28 — 10 周）\\n- 备选: ACL 2027 ARR Oct 15（21 周）/ TACL rolling\\n\", \"total_chars\": 1451, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a8cdf46c-6eca-49b9-b703-27332b7232e2",
  "uuid": "fff7626b-d64c-4a3b-a72b-b0fda3725742",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/ROADMAP.md\\\", \\\"content\\\": \\\"# nlp_variance_gtheory — Research Dashboard\\\\n\\\\n> 最后更新: 2026-05-20 14:17 UTC | 更新原因: 服务器就绪，MVP 调整为 Phase A（单硬件三精度 108 条件），Agent 已派出部署\\\\n\\\\n## 核心方向\\\\n用 Generalizability Theory 联合分解 LLM 评估中基础设施因素（硬件类型、数值精度）与方法论因素（prompt 措辞、随机种子、温度、few-shot 顺序）的方差，检验 \\\\\\\"separability 假设\\\\\\\"。产出可量化的 reproducibility budget（D-study）。\\\\n\\\\n## 当前进展\\\\n- 阶段: MVP 验证\\\\n- 服务器: westd-32570（4× RTX 6000 PRO 96GB）已绑定，4 卡全部分配\\\\n- 代码: 18 文件已完成，Agent 正在部署到服务器\\\\n- 文献图谱: 10 篇核心论文，蒸馏完成（v1）\\\\n- 第二种 GPU 类型: 已向 Manager 申请（A100/H100），等待回复\\\\n\\\\n## MVP 验证方案（Phase A — 单硬件 + 三精度）\\\\n**核心假设**: G-theory 可成功分解 infrastructure × methodology 交叉方差分量。\\\\n\\\\n**调整后设计**（因当前只有 1 种 GPU 类型）:\\\\n- 1 模型: Llama-3.1-8B-Instruct\\\\n- 1 硬件: RTX 6000 PRO 96GB\\\\n- 3 精度: FP32, BF16, FP16（96GB VRAM 支持 FP32）\\\\n- 3 prompt paraphrases × 3 seeds × 2 温度 × 2 orderings\\\\n- 共 **108 条件** × 50 MMLU items = 5,400 次推理\\\\n\\\\n**Pass/Fail（已量化）**:\\\\n- PASS: (a) pipeline 完整运行; (b) 方差分解收敛; (c) ≥2 个方差分量占总方差 ≥5% 或 bootstrap 95% CI 不含零（含 ≥1 precision×methodology 交互项）\\\\n- FAIL: 分解不收敛 / 全条件零方差 / 种子控制失效\\\\n\\\\n**Phase B（待第二种 GPU 到位）**: 加入硬件因素，完成 hardware × methodology 交叉。\\\\n\\\\n## 近期任务\\\\n- [x] GPU 服务器配置\\\\n- [ ] Agent 环境搭建 + 代码部署（进行中）\\\\n- [ ] Seed determinism sanity check（同配置 10 次重复）\\\\n- [ ] 正式 MVP Phase A（108 条件）\\\\n- [ ] 方差分解分析 → pass/fail 判定\\\\n- [ ] 等待 Manager 回复第二种 GPU 类型\\\\n\\\\n## GPU 预算\\\\n- 本项目分配: westd-32570 cuda:0-3（4× RTX 6000 PRO 96GB）\\\\n- MVP Phase A 预估: ~8 GPU·h\\\\n- 全研究预估: ~2,200 GPU·h（需额外 A100/H100）\\\\n\\\\n## 投稿目标\\\\n- 主投: AAAI 2027（abstract Jul 21, paper Jul 28 — 10 周）\\\\n- 备选: ACL 2027 ARR Oct 15（21 周）/ TACL rolling\\\\n\\\", \\\"total_chars\\\": 1451, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/ROADMAP.md\", \"content\": \"# nlp_variance_gtheory — Research Dashboard\\n\\n> 最后更新: 2026-05-20 14:17 UTC | 更新原因: 服务器就绪，MVP 调整为 Phase A（单硬件三精度 108 条件），Agent 已派出部署\\n\\n## 核心方向\\n用 Generalizability Theory 联合分解 LLM 评估中基础设施因素（硬件类型、数值精度）与方法论因素（prompt 措辞、随机种子、温度、few-shot 顺序）的方差，检验 \\\"separability 假设\\\"。产出可量化的 reproducibility budget（D-study）。\\n\\n## 当前进展\\n- 阶段: MVP 验证\\n- 服务器: westd-32570（4× RTX 6000 PRO 96GB）已绑定，4 卡全部分配\\n- 代码: 18 文件已完成，Agent 正在部署到服务器\\n- 文献图谱: 10 篇核心论文，蒸馏完成（v1）\\n- 第二种 GPU 类型: 已向 Manager 申请（A100/H100），等待回复\\n\\n## MVP 验证方案（Phase A — 单硬件 + 三精度）\\n**核心假设**: G-theory 可成功分解 infrastructure × methodology 交叉方差分量。\\n\\n**调整后设计**（因当前只有 1 种 GPU 类型）:\\n- 1 模型: Llama-3.1-8B-Instruct\\n- 1 硬件: RTX 6000 PRO 96GB\\n- 3 精度: FP32, BF16, FP16（96GB VRAM 支持 FP32）\\n- 3 prompt paraphrases × 3 seeds × 2 温度 × 2 orderings\\n- 共 **108 条件** × 50 MMLU items = 5,400 次推理\\n\\n**Pass/Fail（已量化）**:\\n- PASS: (a) pipeline 完整运行; (b) 方差分解收敛; (c) ≥2 个方差分量占总方差 ≥5% 或 bootstrap 95% CI 不含零（含 ≥1 precision×methodology 交互项）\\n- FAIL: 分解不收敛 / 全条件零方差 / 种子控制失效\\n\\n**Phase B（待第二种 GPU 到位）**: 加入硬件因素，完成 hardware × methodology 交叉。\\n\\n## 近期任务\\n- [x] GPU 服务器配置\\n- [ ] Agent 环境搭建 + 代码部署（进行中）\\n- [ ] Seed determinism sanity check（同配置 10 次重复）\\n- [ ] 正式 MVP Phase A（108 条件）\\n- [ ] 方差分解分析 → pass/fail 判定\\n- [ ] 等待 Manager 回复第二种 GPU 类型\\n\\n## GPU 预算\\n- 本项目分配: westd-32570 cuda:0-3（4× RTX 6000 PRO 96GB）\\n- MVP Phase A 预估: ~8 GPU·h\\n- 全研究预估: ~2,200 GPU·h（需额外 A100/H100）\\n\\n## 投稿目标\\n- 主投: AAAI 2027（abstract Jul 21, paper Jul 28 — 10 周）\\n- 备选: ACL 2027 ARR Oct 15（21 周）/ TACL rolling\\n\", \"total_chars\": 1451, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 16_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me compile the related work notes. Let me organize the papers into the three categories as specified:

**(a) G-theory & Variance Decomposition in NLP/ML:**
- Mesting et al. 2026 — G-theory (TEE) applied to NLG evaluation
- Kunievsky et al. 2025 — prompt sensitivity variance decomposition (intent/articulation/model uncertainty)
- GeneralizIT (Nalisnick et al.) — software for G-theory in ML


**(b) Infrastructure variance:**
- Yuan et al. 2025 — LayerCast mixed-precision inference variance
- Messina et al. 2026 — background temperature effects on GPU computation
- ThinkingMachines 2025 — batch invariance / non-determinism in inference
**(c) Prompt sensitivity & methodological variance:**
- Brittlebench 2026 — prompt brittleness benchmark
- Hua et al. 2025 — scoring artifacts in LLM evaluation
- "Same Prompt, Different Outcomes" — seed/sampling variance
- Bui et al. — seed sensitivity in LLM evaluation

Now let me verify I have everything covered.

Looking at the specific metrics from these papers: Yuan's LayerCast achieves under 3.4% divergence with 34% memory savings by mixing BF16 storage with FP32 computation, while ThinkingMachines found that batch-invariance failures in core operations like RMSNorm produce 80 unique completions at zero temperature, fixable with deterministic kernels at a 1.6-2.1× latency cost. Messina's work reveals that models have inherent background temperature even at T=0—GPT around 0.075, Gemini around 0.065, Claude near zero—which can be calibrated with a single reference scalar.

Mesting's generalizability theory analysis shows judge selection dominates safety evaluation variance at 43.8%, while prompt effects vary dramatically between open models (50%) and commercial systems (25%), and standard confidence intervals systematically underestimate uncertainty by 40-60%. Brittlebench decomposes variance into data and brittleness components with similar prompt sensitivity patterns, while Hua's work demonstrates that much apparent prompt sensitivity is actually an artifact of evaluation methodology—switching to LLM judges improves rank correlation from 0.30 to 0.95. Kunievsky proposes decomposing uncertainty into intent, articulation, and model components as a unifying framework. I can't find direct references to "Same Prompt, Different Outcomes" or "Bui et al." in the distilled research, so I'll mark those as needing verification. Now I'll compile the notes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8cdf46c-6eca-49b9-b703-27332b7232e2",
  "uuid": "147e913d-cd0a-4f57-8be0-c8866842a0e4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0194fb6XRK7fidRHYbksB2Nw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1481,
      "cache_read_input_tokens": 26954,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1481
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 17_

ideas.md 不存在，其余信息已齐全。开始整理笔记。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8cdf46c-6eca-49b9-b703-27332b7232e2",
  "uuid": "a2555c99-323b-494d-8140-fa3260764cae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0194fb6XRK7fidRHYbksB2Nw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1481,
      "cache_read_input_tokens": 26954,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1481
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Write · `toolu_01QBzRAXQCo5QsVnHLKXZJ3n`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/related_work_notes.md",
  "content": "# Related Work — Structured Notes\n\n> 用于论文 Related Work 章节起草。按 3 个子类组织。基于 10 篇蒸馏论文 + ROADMAP 定位。\n\n## (a) G-theory & Variance Decomposition in NLP/ML\n\n### [Mesting et al., 2026] — TEE: Generalizability Theory for NLG Evaluation\n- **核心发现**: 将心理测量学的 G-theory（REML + D-study）引入 NLG 评估；发现 judge 选择贡献 43.8% 方差，prompt 在开源模型中贡献~50%、商用模型~25%；标准 95% CI 实际覆盖率仅 79%\n- **与本工作关系**: extends — 我们直接继承其 TEE 框架和 REML 方法，将其扩展到 infrastructure facets\n- **差异化**: Mesting 只分解方法论 facets（item/prompt/judge/temp），未纳入硬件/精度等基础设施因素；我们的 G-theory 框架联合分解 infrastructure × methodology\n\n### [Kunievsky et al., 2025] — Prompt Sensitivity Variance Decomposition\n- **核心发现**: 将 prompt sensitivity 分解为 intent（意图）、articulation（表述）、model uncertainty（模型不确定性）三个独立分量\n- **与本工作关系**: complements — 提供了 prompt 方差的细粒度分解视角，其 articulation 分量对应我们框架中 prompt paraphrase facet\n- **差异化**: 专注 prompt 单一维度的语义分解，未涉及基础设施方差，也未采用 G-theory 的交叉设计\n\n### [Nalisnick et al.] — GeneralizIT: Software for G-theory in ML\n- **核心发现**: 为 ML 场景提供 G-theory 计算工具包，简化 REML 估计和 D-study 设计流程\n- **与本工作关系**: complements — 提供可复用的计算基础设施，我们的实验可能使用或参考其实现\n- **差异化**: 是通用工具而非针对特定方差源的实证研究；我们提供具体的 LLM 评估方差分解实证结果和 reproducibility budget\n\n## (b) Infrastructure Variance\n\n### [Yuan et al., 2025] — LayerCast: Mixed-Precision Inference Variance\n- **核心发现**: BF16 推理导致 9% 的 accuracy 标准差，FP32 接近 0%；提出 LayerCast（BF16 存储 + FP32 计算），将 divergence 控制在 <3.4% 同时节省 34% 显存；推理模型受影响最大\n- **与本工作关系**: addresses limitation of — 量化了精度对推理结果的影响，但未将其纳入统一的方差分解框架\n- **差异化**: Yuan 只刻画精度这一个 infrastructure 因素并提出缓解方案；我们将精度作为 G-theory 框架中的一个 facet，与方法论因素联合分解\n\n### [Messina et al., 2026 (TMLR)] — Background Temperature Effects on GPU Computation\n- **核心发现**: 即使 T=0，API 模型仍存在 \"背景随机性\"：GPT~0.075、Gemini~0.065、Claude~0 有效温度；提出 reference calibration 方法量化为单一标量 T_bg\n- **与本工作关系**: complements — 揭示了一类此前被忽视的 infrastructure 方差源（硬件层面的非确定性），为我们纳入硬件 facet 提供实证依据\n- **差异化**: Messina 聚焦 API 层面的背景温度刻画，未进行多因素交叉分解；我们将此类硬件非确定性纳入 G-theory 的交叉设计\n\n### [ThinkingMachines, 2025] — Batch Invariance Failure in LLM Inference\n- **核心发现**: T=0 下 1000 次推理产生 80 种不同输出；根因是 RMSNorm/GEMM/attention 的 batch-size 依赖性而非随机种子；提出确定性内核方案，代价为 1.6-2.1× 延迟\n- **与本工作关系**: addresses limitation of — 发现并解释了 batch 非确定性这一关键 infrastructure 方差源，但止步于工程修复\n- **差异化**: 仅刻画 batch-size 这一个因素并提出工程缓解方案；我们将 batch 非确定性与其他 infrastructure/methodology 因素一起纳入 G-theory 分解\n\n## (c) Prompt Sensitivity & Methodological Variance\n\n### [Brittlebench, 2026] — Prompt Brittleness Benchmark\n- **核心发现**: 系统性评估 prompt 脆弱性；通过 ANOVA 分解 V_data + V_brittleness；prompt 措辞贡献约 50% 方差（开源模型），商用模型约 25%\n- **与本工作关系**: complements — 提供了大规模 prompt 脆弱性的实证基准，其 V_brittleness 分量对应我们框架中 prompt facet 的方差\n- **差异化**: 使用传统 ANOVA 而非 G-theory，只分解 data vs. brittleness 两个分量；我们的框架支持更多 facets 的联合分解和交互项估计\n\n### [Hua et al., 2025 (EMNLP)] — Scoring Artifacts in LLM Evaluation\n- **核心发现**: 大量表观的 prompt sensitivity 实际上是评估方法的 artifact——使用 LLM-judge 后 rank correlation 从 0.30 跃升至 0.95\n- **与本工作关系**: complements — 警示区分\"真实方差\"与\"评估 artifact\"的重要性，为我们的实验设计提供方法论参考\n- **差异化**: Hua 聚焦揭示 artifact 现象而非系统性分解方差来源；我们的 G-theory 框架可将 scoring method 作为 facet 纳入，从而量化其贡献\n\n### \"Same Prompt, Different Outcomes\" — Seed/Sampling Variance\n- **核心发现**: [需补充]\n- **与本工作关系**: [需补充] — 预期与我们框架中 seed facet 直接相关\n- **差异化**: [需补充]\n\n### [Bui et al.] — Seed Sensitivity in LLM Evaluation\n- **核心发现**: [需补充]\n- **与本工作关系**: [需补充] — 预期聚焦 seed 这一单一因素\n- **差异化**: [需补充]\n\n## 定位总结\n\n本项目是首个用 Generalizability Theory 联合分解 infrastructure（硬件类型、数值精度、batch 非确定性）与 methodology（prompt 措辞、随机种子、温度、few-shot 顺序）方差的工作。现有研究要么只用 G-theory 分解方法论 facets（Mesting），要么只刻画单一 infrastructure 因素并提出工程修复（Yuan、ThinkingMachines、Messina），没有工作在一个统一的交叉设计中同时容纳两类因素并检验其 separability。我们的 D-study 产出可量化的 reproducibility budget，为社区提供实验设计的决策依据。\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8cdf46c-6eca-49b9-b703-27332b7232e2",
  "uuid": "880ac3c9-165e-41e8-a27e-5b070528ce6e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0194fb6XRK7fidRHYbksB2Nw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1481,
      "cache_read_input_tokens": 26954,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1481
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-20T17:12:06.218Z_

<details><summary>↩ Tool result · `toolu_01QBzRAXQCo5QsVnHLKXZJ3n`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/related_work_notes.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a8cdf46c-6eca-49b9-b703-27332b7232e2",
  "uuid": "63fb6578-24a7-4f18-a1ac-9abed14ca977",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/related_work_notes.md",
    "content": "# Related Work — Structured Notes\n\n> 用于论文 Related Work 章节起草。按 3 个子类组织。基于 10 篇蒸馏论文 + ROADMAP 定位。\n\n## (a) G-theory & Variance Decomposition in NLP/ML\n\n### [Mesting et al., 2026] — TEE: Generalizability Theory for NLG Evaluation\n- **核心发现**: 将心理测量学的 G-theory（REML + D-study）引入 NLG 评估；发现 judge 选择贡献 43.8% 方差，prompt 在开源模型中贡献~50%、商用模型~25%；标准 95% CI 实际覆盖率仅 79%\n- **与本工作关系**: extends — 我们直接继承其 TEE 框架和 REML 方法，将其扩展到 infrastructure facets\n- **差异化**: Mesting 只分解方法论 facets（item/prompt/judge/temp），未纳入硬件/精度等基础设施因素；我们的 G-theory 框架联合分解 infrastructure × methodology\n\n### [Kunievsky et al., 2025] — Prompt Sensitivity Variance Decomposition\n- **核心发现**: 将 prompt sensitivity 分解为 intent（意图）、articulation（表述）、model uncertainty（模型不确定性）三个独立分量\n- **与本工作关系**: complements — 提供了 prompt 方差的细粒度分解视角，其 articulation 分量对应我们框架中 prompt paraphrase facet\n- **差异化**: 专注 prompt 单一维度的语义分解，未涉及基础设施方差，也未采用 G-theory 的交叉设计\n\n### [Nalisnick et al.] — GeneralizIT: Software for G-theory in ML\n- **核心发现**: 为 ML 场景提供 G-theory 计算工具包，简化 REML 估计和 D-study 设计流程\n- **与本工作关系**: complements — 提供可复用的计算基础设施，我们的实验可能使用或参考其实现\n- **差异化**: 是通用工具而非针对特定方差源的实证研究；我们提供具体的 LLM 评估方差分解实证结果和 reproducibility budget\n\n## (b) Infrastructure Variance\n\n### [Yuan et al., 2025] — LayerCast: Mixed-Precision Inference Variance\n- **核心发现**: BF16 推理导致 9% 的 accuracy 标准差，FP32 接近 0%；提出 LayerCast（BF16 存储 + FP32 计算），将 divergence 控制在 <3.4% 同时节省 34% 显存；推理模型受影响最大\n- **与本工作关系**: addresses limitation of — 量化了精度对推理结果的影响，但未将其纳入统一的方差分解框架\n- **差异化**: Yuan 只刻画精度这一个 infrastructure 因素并提出缓解方案；我们将精度作为 G-theory 框架中的一个 facet，与方法论因素联合分解\n\n### [Messina et al., 2026 (TMLR)] — Background Temperature Effects on GPU Computation\n- **核心发现**: 即使 T=0，API 模型仍存在 \"背景随机性\"：GPT~0.075、Gemini~0.065、Claude~0 有效温度；提出 reference calibration 方法量化为单一标量 T_bg\n- **与本工作关系**: complements — 揭示了一类此前被忽视的 infrastructure 方差源（硬件层面的非确定性），为我们纳入硬件 facet 提供实证依据\n- **差异化**: Messina 聚焦 API 层面的背景温度刻画，未进行多因素交叉分解；我们将此类硬件非确定性纳入 G-theory 的交叉设计\n\n### [ThinkingMachines, 2025] — Batch Invariance Failure in LLM Inference\n- **核心发现**: T=0 下 1000 次推理产生 80 种不同输出；根因是 RMSNorm/GEMM/attention 的 batch-size 依赖性而非随机种子；提出确定性内核方案，代价为 1.6-2.1× 延迟\n- **与本工作关系**: addresses limitation of — 发现并解释了 batch 非确定性这一关键 infrastructure 方差源，但止步于工程修复\n- **差异化**: 仅刻画 batch-size 这一个因素并提出工程缓解方案；我们将 batch 非确定性与其他 infrastructure/methodology 因素一起纳入 G-theory 分解\n\n## (c) Prompt Sensitivity & Methodological Variance\n\n### [Brittlebench, 2026] — Prompt Brittleness Benchmark\n- **核心发现**: 系统性评估 prompt 脆弱性；通过 ANOVA 分解 V_data + V_brittleness；prompt 措辞贡献约 50% 方差（开源模型），商用模型约 25%\n- **与本工作关系**: complements — 提供了大规模 prompt 脆弱性的实证基准，其 V_brittleness 分量对应我们框架中 prompt facet 的方差\n- **差异化**: 使用传统 ANOVA 而非 G-theory，只分解 data vs. brittleness 两个分量；我们的框架支持更多 facets 的联合分解和交互项估计\n\n### [Hua et al., 2025 (EMNLP)] — Scoring Artifacts in LLM Evaluation\n- **核心发现**: 大量表观的 prompt sensitivity 实际上是评估方法的 artifact——使用 LLM-judge 后 rank correlation 从 0.30 跃升至 0.95\n- **与本工作关系**: complements — 警示区分\"真实方差\"与\"评估 artifact\"的重要性，为我们的实验设计提供方法论参考\n- **差异化**: Hua 聚焦揭示 artifact 现象而非系统性分解方差来源；我们的 G-theory 框架可将 scoring method 作为 facet 纳入，从而量化其贡献\n\n### \"Same Prompt, Different Outcomes\" — Seed/Sampling Variance\n- **核心发现**: [需补充]\n- **与本工作关系**: [需补充] — 预期与我们框架中 seed facet 直接相关\n- **差异化**: [需补充]\n\n### [Bui et al.] — Seed Sensitivity in LLM Evaluation\n- **核心发现**: [需补充]\n- **与本工作关系**: [需补充] — 预期聚焦 seed 这一单一因素\n- **差异化**: [需补充]\n\n## 定位总结\n\n本项目是首个用 Generalizability Theory 联合分解 infrastructure（硬件类型、数值精度、batch 非确定性）与 methodology（prompt 措辞、随机种子、温度、few-shot 顺序）方差的工作。现有研究要么只用 G-theory 分解方法论 facets（Mesting），要么只刻画单一 infrastructure 因素并提出工程修复（Yuan、ThinkingMachines、Messina），没有工作在一个统一的交叉设计中同时容纳两类因素并检验其 separability。我们的 D-study 产出可量化的 reproducibility budget，为社区提供实验设计的决策依据。\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01TWmUVLYoMiEHpvapdBx7Ri`</summary>

```json
{
  "name": "related_work_notes",
  "type": "report",
  "description": "Related Work 结构化笔记：10 篇论文按 G-theory/Infrastructure/Prompt-Methodology 三类组织，每篇含核心发现、与本工作关系、差异化。2 篇信息不足标注[需补充]。",
  "project": "nlp_variance_gtheory",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/related_work_notes.md",
  "tags": [
    "related-work",
    "literature",
    "paper-writing"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8cdf46c-6eca-49b9-b703-27332b7232e2",
  "uuid": "128230cd-b775-4255-a476-68664dcdff6b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R2D5QGzhN9NFfEsuDcFycH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3350,
      "cache_read_input_tokens": 28435,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3350
      },
      "output_tokens": 50,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-20T17:12:11.806Z_

<details><summary>↩ Tool result · `toolu_01TWmUVLYoMiEHpvapdBx7Ri`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260520_a9accf\", \"name\": \"related_work_notes\", \"type\": \"report\", \"description\": \"Related Work 结构化笔记：10 篇论文按 G-theory/Infrastructure/Prompt-Methodology 三类组织，每篇含核心发现、与本工作关系、差异化。2 篇信息不足标注[需补充]。\", \"path\": \"projects/nlp_variance_gtheory/artifacts/_project/report/related_work_notes.md\", \"url\": null, \"project\": \"nlp_variance_gtheory\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-20T17:12:11.794421+00:00\", \"tags\": [\"related-work\", \"literature\", \"paper-writing\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a8cdf46c-6eca-49b9-b703-27332b7232e2",
  "uuid": "a7418edc-ee57-41c1-bb3b-910b2e332c41",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260520_a9accf\\\", \\\"name\\\": \\\"related_work_notes\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"Related Work 结构化笔记：10 篇论文按 G-theory/Infrastructure/Prompt-Methodology 三类组织，每篇含核心发现、与本工作关系、差异化。2 篇信息不足标注[需补充]。\\\", \\\"path\\\": \\\"projects/nlp_variance_gtheory/artifacts/_project/report/related_work_notes.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"nlp_variance_gtheory\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-20T17:12:11.794421+00:00\\\", \\\"tags\\\": [\\\"related-work\\\", \\\"literature\\\", \\\"paper-writing\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260520_a9accf\", \"name\": \"related_work_notes\", \"type\": \"report\", \"description\": \"Related Work 结构化笔记：10 篇论文按 G-theory/Infrastructure/Prompt-Methodology 三类组织，每篇含核心发现、与本工作关系、差异化。2 篇信息不足标注[需补充]。\", \"path\": \"projects/nlp_variance_gtheory/artifacts/_project/report/related_work_notes.md\", \"url\": null, \"project\": \"nlp_variance_gtheory\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-20T17:12:11.794421+00:00\", \"tags\": [\"related-work\", \"literature\", \"paper-writing\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 22_

已完成，写入 `artifacts/related_work_notes.md` 并注册。

覆盖 8 篇论文的完整笔记（3 行格式：核心发现 / 与本工作关系 / 差异化），按 (a) G-theory & Variance Decomposition、(b) Infrastructure Variance、(c) Prompt Sensitivity & Methodological Variance 三类组织。"Same Prompt, Different Outcomes" 和 Bui et al. 两篇在蒸馏 skill 中无足够信息，已标注 `[需补充]`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8cdf46c-6eca-49b9-b703-27332b7232e2",
  "uuid": "4b1fa103-bc62-4f03-ab95-b5b3e8a94c1e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GFdvKHPTrhfRNYWNPHkpi3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 596,
      "cache_read_input_tokens": 31785,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 596
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Task result

_source line 23_

已完成，写入 `artifacts/related_work_notes.md` 并注册。

覆盖 8 篇论文的完整笔记（3 行格式：核心发现 / 与本工作关系 / 差异化），按 (a) G-theory & Variance Decomposition、(b) Infrastructure Variance、(c) Prompt Sensitivity & Methodological Variance 三类组织。"Same Prompt, Different Outcomes" 和 Bui et al. 两篇在蒸馏 skill 中无足够信息，已标注 `[需补充]`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 82349,
  "duration_api_ms": 83193,
  "num_turns": 8,
  "stop_reason": "end_turn",
  "session_id": "a8cdf46c-6eca-49b9-b703-27332b7232e2",
  "total_cost_usd": 0.297388,
  "usage": {
    "input_tokens": 9,
    "cache_creation_input_tokens": 20540,
    "cache_read_input_tokens": 122824,
    "output_tokens": 4238,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 20540,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 162,
        "cache_read_input_tokens": 31785,
        "cache_creation_input_tokens": 596,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 596
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1536,
      "outputTokens": 14,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001606,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 9,
      "outputTokens": 4238,
      "cacheReadInputTokens": 122824,
      "cacheCreationInputTokens": 20540,
      "webSearchRequests": 0,
      "costUSD": 0.295782,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "eb09e50d-f88c-4945-96a3-d57260157cfd"
}
```

</details>

---
