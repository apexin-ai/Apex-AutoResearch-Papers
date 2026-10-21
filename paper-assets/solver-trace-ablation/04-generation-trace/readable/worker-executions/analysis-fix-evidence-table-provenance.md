# analysis fix evidence table provenance

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 12
- **Recorded user turns:** 0
- **Tool calls:** 2
- **Original source:** `logs/workers/worker_analysis_fix-evidence-table-provenance_20260514T071442.log`
- **Structured JSON:** [`46b228e649ccc41c084e.json`](../../sessions/46/46b228e649ccc41c084e.json)

## Before a recorded user message

12 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "session_id": "09394bbd-fea8-4b59-808c-91e90f73c874",
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
  "uuid": "8a854c1a-ef0a-410a-beda-86ba7ea33263",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/memory/"
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
    "resetsAt": 1778747400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "c5b70acb-52e7-4070-a489-069e420a62e2",
  "session_id": "09394bbd-fea8-4b59-808c-91e90f73c874"
}
```

---

### Assistant

_source line 4_

Let me start by reading the current file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "09394bbd-fea8-4b59-808c-91e90f73c874",
  "uuid": "5516006a-fd59-4eab-ad01-2d9d6a8e596f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017AdydNkgvqHcmNCX2WBEAB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11940,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11940
      },
      "output_tokens": 2,
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

<details open><summary>🔧 Tool call — Read · `toolu_0158csex4sssqy7EsRKr1fCL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/paper_table1_evidence.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "09394bbd-fea8-4b59-808c-91e90f73c874",
  "uuid": "2103e26a-62ec-4c22-ac6f-64f44e2ada2c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017AdydNkgvqHcmNCX2WBEAB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11940,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11940
      },
      "output_tokens": 2,
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

_source line 6 · 2026-05-14T07:14:54.707Z_

<details><summary>↩ Tool result · `toolu_0158csex4sssqy7EsRKr1fCL`</summary>

```text
1	# Table 1: Comprehensive Experimental Evidence for Solver-Trace Ablation
2	
3	**Model**: Qwen3-4B | **Training**: GRPO, 500 steps, K=8 | **Data**: train_500_seed42.jsonl (500 problems) | **Eval**: proofwriter_fol_100.jsonl (100 problems)
4	
5	## Main Results Table
6	
7	### Group A: Reference Baselines
8	
9	| Experiment ID | Reward Mode | Formula | β | Seed | Eval PR | Eval Mean ISR | ISR Std | Comp. Mean | Comp.=2 (%) | Eval Method | Diagnosis | Claims |
10	|---|---|---|---|---|---|---|---|---|---|---|---|---|
11	| sta-phase0-baseline | — (base model) | — | — | — | 0.12 | 0.0641 | 0.1983 | — | — | eval_sta.py | pre-training reference | — |
12	| sta-gt-isr-baseline | — (ground truth FOL) | — | — | — | 0.18 | 0.5588 | 0.2582 | — | — | direct computation | ISR ceiling on gold FOL | — |
13	
14	### Group B: Exec-Only Reward (r = r_exec)
15	
16	| Experiment ID | Reward Mode | Formula | β | Seed | Eval PR | Eval Mean ISR | ISR Std | Comp. Mean | Comp.=2 (%) | Eval Method | Diagnosis | Claims |
17	|---|---|---|---|---|---|---|---|---|---|---|---|---|
18	| plan001-exec-only-s42-r2 | exec-only | r = r_exec | — | 42 | 0.93 | 0.1232 | 0.1887 | 6.58† | — | eval_sta.py | genuine proofs | C1 |
19	| plan001-exec-only-s43-r4 | exec-only | r = r_exec | — | 43 | 0.14‡ | 0.00‡ | — | — | — | sampling (T=0.7)‡ | degraded (87% max_tokens) | C1, C2 |
20	| plan001-exec-only-s44 | exec-only | r = r_exec | — | 44 | 0.98 | 0.5700 | 0.2013 | 2.04 | 94% | eval_sta.py | tautological collapse | C1, C2 |
21	
22	**Exec-only 3-seed summary**: mean PR = 0.68 ± 0.47, 2/3 seeds degenerate. Cross-seed instability is the primary finding.
23	
24	### Group C: Additive ISR Bonus (r = r_exec · (1 + β · ISR))
25	
26	| Experiment ID | Reward Mode | Formula | β | Seed | Eval PR | Eval Mean ISR | ISR Std | Comp. Mean | Comp.=2 (%) | Eval Method | Diagnosis | Claims |
27	|---|---|---|---|---|---|---|---|---|---|---|---|---|
28	| plan002-additive-b03-s42 | additive ISR | r = r_exec · (1 + β·ISR) | 0.3 | 42 | 0.18 | 0.0257 | 0.0742 | — | — | eval_sta.py§ | PR collapse (Goodhart) | C3 |
29	| plan002-additive-b01-s42 | additive ISR | r = r_exec · (1 + β·ISR) | 0.1 | 42 | 0.81 | 0.3365 | 0.3227 | 5.58 | 3.7% | eval_sta.py | **best: PR preserved + ISR 2.73x** | C3 |
30	
31	**Dose-response**: β=0.3 → PR collapse (0.18); β=0.1 → PR preserved (0.81) with ISR 2.73x over exec-only baseline.
32	
33	### Group D: Convex ISR (r = α · r_exec + β · ISR)
34	
35	| Experiment ID | Reward Mode | Formula | β | Seed | Eval PR | Eval Mean ISR | ISR Std | Comp. Mean | Comp.=2 (%) | Eval Method | Diagnosis | Claims |
36	|---|---|---|---|---|---|---|---|---|---|---|---|---|
37	| plan005-sta-low-s42 | convex ISR | r = 0.9·r_exec + 0.1·ISR | 0.1 | 42 | —¶ | —¶ | —¶ | — | — | training logs only¶ | PR suppressed (train last100 PR=0.77) | C3 |
38	
39	### Group E: Convex Random Control (r = α · r_exec + β · random)
40	
41	| Experiment ID | Reward Mode | Formula | β | Seed | Eval PR | Eval Mean ISR | ISR Std | Comp. Mean | Comp.=2 (%) | Eval Method | Diagnosis | Claims |
42	|---|---|---|---|---|---|---|---|---|---|---|---|---|
43	| plan013-random-reward-s42-r4 | convex random | r = 0.9·r_exec + 0.1·random | 0.1 | 42 | 1.00 | 0.5350 | 0.1282 | ~2†† | ~100%†† | eval_sta.py | tautological collapse | C2 |
44	
45	### Group F: Additive Random Control (r = r_exec · (1 + β · random))
46	
47	| Experiment ID | Reward Mode | Formula | β | Seed | Eval PR | Eval Mean ISR | ISR Std | Comp. Mean | Comp.=2 (%) | Eval Method | Diagnosis | Claims |
48	|---|---|---|---|---|---|---|---|---|---|---|---|---|
49	| plan017-additive-random-s42 | additive random | r = r_exec · (1 + β·random) | 0.3 | 42 | 0.48 | 0.0453 | 0.0759 | 9.60 | 0% | eval_sta.py | complex but useless formalizations | C2, C3 |
50	
51	## Claim Evidence Summary
52	
53	### Claim 1: Exec-only reward exhibits cross-seed degeneration
54	| Seed | Eval PR | Eval ISR | Comp. Mean | Failure Mode |
55	|---|---|---|---|---|
56	| 42 | 0.93 | 0.1232 | 6.58 | None (genuine) |
57	| 43 | 0.14 | 0.00 | — | Output degeneration (max_tokens) |
58	| 44 | 0.98 | 0.5700 | 2.04 | Tautological collapse (premise=conclusion) |
59	
60	**Verdict**: 2/3 seeds degenerate under exec-only reward. High training PR does not guarantee genuine formalization.
61	
62	### Claim 2: ISR + component count diagnoses genuine vs degenerate proofs
63	| Experiment | Eval PR | Eval ISR | Comp. Mean | ISR Diagnosis |
64	|---|---|---|---|---|
65	| exec-only s42 (genuine) | 0.93 | 0.12 | 6.58 | Low ISR + high comp → genuine but imperfect |
66	| exec-only s44 (tautological) | 0.98 | 0.57 | 2.04 | High ISR + low comp → **tautological artifact** |
67	| convex random (tautological) | 1.00 | 0.54 | ~2 | High ISR + low comp → **tautological artifact** |
68	| additive random (complex junk) | 0.48 | 0.05 | 9.60 | Low ISR + high comp → many premises but unused |
69	| additive ISR β=0.1 (best) | 0.81 | 0.34 | 5.58 | Moderate ISR + high comp → **genuine improvement** |
70	
71	**Verdict**: ISR alone is ambiguous (s44 ISR=0.57 looks good but is tautological). Component count resolves the ambiguity: comp≈2 flags tautological collapse; comp>5 with moderate ISR indicates genuine proofs.
72	
73	### Claim 3: ISR-as-reward shows Goodhart effect at high dose, effective at low dose
74	| Reward Mode | β | Eval PR | Eval ISR | Goodhart? |
75	|---|---|---|---|---|
76	| additive ISR | 0.3 | 0.18 | 0.03 | **Yes** — PR collapse |
77	| additive ISR | 0.1 | 0.81 | 0.34 | **No** — sweet spot |
78	| convex ISR | 0.1 | —¶ | — | Partially (train PR suppressed) |
79	| convex random | 0.1 | 1.00 | 0.54 | Tautological (no ISR signal) |
80	| additive random | 0.3 | 0.48 | 0.05 | N/A (random control) |
81	
82	**Verdict**: Clear dose-response. β=0.1 additive is the working point; β=0.3 triggers Goodhart collapse. Random controls confirm ISR signal is causal (not just variance regularization).
83	
84	## Notes
85	
86	† Component count for plan001-exec-only-s42-r2 (6.58) is cross-referenced from plan001-exec-only-s44 notes, not stored in registry eval metrics. May need re-verification with eval_sta.py.
87	
88	‡ **D029**: plan001-exec-only-s43-r4 was evaluated with sampling (do_sample=True, temperature=0.7) instead of eval_sta.py greedy decoding used for all other experiments. The PR=14% result is a failure case regardless of eval method — 87% of outputs hit max_new_tokens and are unparseable. Decision: not re-evaluated; paper will note the method difference.
89	
90	§ plan002-additive-b03-s42 eval_method not explicitly recorded in registry, but eval fields (eval_prove_rate, eval_mean_isr) are consistent with eval_sta.py output format.
91	
92	¶ **D030**: plan005-sta-low-s42 checkpoint was deleted; no eval was performed. Training log windowed metrics are the only available data. Paper uses training curves as evidence for "ISR suppresses reward hacking" (ISR/PR ratio stable at 0.30 across training).
93	
94	†† plan013-random-reward-s42-r4 component count not in registry metrics but noted as "trivial 2-component proofs (premise=conclusion, conclusion=conclusion)" in eval_note.
95	
96	## Excluded Experiments (Failed / Developmental)
97	
98	The following DONE experiments are excluded from Table 1 (crashes, early phases, duplicates):
99	
100	| Experiment ID | Reason for Exclusion |
101	|---|---|
102	| sta-phase1-exec-only-r2/r3/r4/r5 | 100-step developmental runs |
103	| sta-phase1-exec-sta-r2/r3/r4/r5 | 100-step developmental runs |
104	| plan001-exec-only-s42 | Failed (pre-checkpoint crash) |
105	| plan001-exec-only-s42-r3 | Failed (OOM duplicate submission) |
106	| plan001-exec-only-s43 | Failed (OOM from plan013 GPU overflow) |
107	| plan001-exec-only-s43-r2 | Failed (process crashed) |
108	| plan001-exec-only-s43-r3 | Failed (disk full at step 23) |
109	| plan013-random-reward-s42 | Failed (CUDA_VISIBLE_DEVICES not set) |
110	| plan013-random-reward-s42-r2 | Failed (process crashed) |
111	| plan013-random-reward-s42-r3 | Failed (disk full at step 28) |
112	| plan003-eval-exec-only-r5 | Eval of 100-step checkpoint (not 500-step) |
113	| plan014-downstream-nli-s42 | Downstream NLI task (separate analysis) |
114	
115	## Compact Table for Paper
116	
117	| Reward Mode | β | Seed | PR↑ | ISR↑ | Comp.↓ | Collapse? |
118	|---|---|---|---|---|---|---|
119	| *Base model* | — | — | .12 | .064 | — | — |
120	| Exec-only | — | 42 | **.93** | .123 | 6.58 | No |
121	| Exec-only | — | 43 | .14‡ | .000 | — | Degenerate |
122	| Exec-only | — | 44 | .98 | .570 | 2.04 | **Tautological** |
123	| Add. ISR | 0.3 | 42 | .18 | .026 | — | PR collapse |
124	| **Add. ISR** | **0.1** | **42** | **.81** | **.337** | **5.58** | **No** |
125	| Cvx. Random | 0.1 | 42 | 1.00 | .535 | ~2 | **Tautological** |
126	| Add. Random | 0.3 | 42 | .48 | .045 | 9.60 | Complex junk |
127	
128	*Generated 2026-05-14. All eval metrics from eval_sta.py full STA unless noted.*
129	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "09394bbd-fea8-4b59-808c-91e90f73c874",
  "uuid": "4b58e9a1-72ed-4334-b763-302dd992b4b7",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/paper_table1_evidence.md",
      "content": "# Table 1: Comprehensive Experimental Evidence for Solver-Trace Ablation\n\n**Model**: Qwen3-4B | **Training**: GRPO, 500 steps, K=8 | **Data**: train_500_seed42.jsonl (500 problems) | **Eval**: proofwriter_fol_100.jsonl (100 problems)\n\n## Main Results Table\n\n### Group A: Reference Baselines\n\n| Experiment ID | Reward Mode | Formula | β | Seed | Eval PR | Eval Mean ISR | ISR Std | Comp. Mean | Comp.=2 (%) | Eval Method | Diagnosis | Claims |\n|---|---|---|---|---|---|---|---|---|---|---|---|---|\n| sta-phase0-baseline | — (base model) | — | — | — | 0.12 | 0.0641 | 0.1983 | — | — | eval_sta.py | pre-training reference | — |\n| sta-gt-isr-baseline | — (ground truth FOL) | — | — | — | 0.18 | 0.5588 | 0.2582 | — | — | direct computation | ISR ceiling on gold FOL | — |\n\n### Group B: Exec-Only Reward (r = r_exec)\n\n| Experiment ID | Reward Mode | Formula | β | Seed | Eval PR | Eval Mean ISR | ISR Std | Comp. Mean | Comp.=2 (%) | Eval Method | Diagnosis | Claims |\n|---|---|---|---|---|---|---|---|---|---|---|---|---|\n| plan001-exec-only-s42-r2 | exec-only | r = r_exec | — | 42 | 0.93 | 0.1232 | 0.1887 | 6.58† | — | eval_sta.py | genuine proofs | C1 |\n| plan001-exec-only-s43-r4 | exec-only | r = r_exec | — | 43 | 0.14‡ | 0.00‡ | — | — | — | sampling (T=0.7)‡ | degraded (87% max_tokens) | C1, C2 |\n| plan001-exec-only-s44 | exec-only | r = r_exec | — | 44 | 0.98 | 0.5700 | 0.2013 | 2.04 | 94% | eval_sta.py | tautological collapse | C1, C2 |\n\n**Exec-only 3-seed summary**: mean PR = 0.68 ± 0.47, 2/3 seeds degenerate. Cross-seed instability is the primary finding.\n\n### Group C: Additive ISR Bonus (r = r_exec · (1 + β · ISR))\n\n| Experiment ID | Reward Mode | Formula | β | Seed | Eval PR | Eval Mean ISR | ISR Std | Comp. Mean | Comp.=2 (%) | Eval Method | Diagnosis | Claims |\n|---|---|---|---|---|---|---|---|---|---|---|---|---|\n| plan002-additive-b03-s42 | additive ISR | r = r_exec · (1 + β·ISR) | 0.3 | 42 | 0.18 | 0.0257 | 0.0742 | — | — | eval_sta.py§ | PR collapse (Goodhart) | C3 |\n| plan002-additive-b01-s42 | additive ISR | r = r_exec · (1 + β·ISR) | 0.1 | 42 | 0.81 | 0.3365 | 0.3227 | 5.58 | 3.7% | eval_sta.py | **best: PR preserved + ISR 2.73x** | C3 |\n\n**Dose-response**: β=0.3 → PR collapse (0.18); β=0.1 → PR preserved (0.81) with ISR 2.73x over exec-only baseline.\n\n### Group D: Convex ISR (r = α · r_exec + β · ISR)\n\n| Experiment ID | Reward Mode | Formula | β | Seed | Eval PR | Eval Mean ISR | ISR Std | Comp. Mean | Comp.=2 (%) | Eval Method | Diagnosis | Claims |\n|---|---|---|---|---|---|---|---|---|---|---|---|---|\n| plan005-sta-low-s42 | convex ISR | r = 0.9·r_exec + 0.1·ISR | 0.1 | 42 | —¶ | —¶ | —¶ | — | — | training logs only¶ | PR suppressed (train last100 PR=0.77) | C3 |\n\n### Group E: Convex Random Control (r = α · r_exec + β · random)\n\n| Experiment ID | Reward Mode | Formula | β | Seed | Eval PR | Eval Mean ISR | ISR Std | Comp. Mean | Comp.=2 (%) | Eval Method | Diagnosis | Claims |\n|---|---|---|---|---|---|---|---|---|---|---|---|---|\n| plan013-random-reward-s42-r4 | convex random | r = 0.9·r_exec + 0.1·random | 0.1 | 42 | 1.00 | 0.5350 | 0.1282 | ~2†† | ~100%†† | eval_sta.py | tautological collapse | C2 |\n\n### Group F: Additive Random Control (r = r_exec · (1 + β · random))\n\n| Experiment ID | Reward Mode | Formula | β | Seed | Eval PR | Eval Mean ISR | ISR Std | Comp. Mean | Comp.=2 (%) | Eval Method | Diagnosis | Claims |\n|---|---|---|---|---|---|---|---|---|---|---|---|---|\n| plan017-additive-random-s42 | additive random | r = r_exec · (1 + β·random) | 0.3 | 42 | 0.48 | 0.0453 | 0.0759 | 9.60 | 0% | eval_sta.py | complex but useless formalizations | C2, C3 |\n\n## Claim Evidence Summary\n\n### Claim 1: Exec-only reward exhibits cross-seed degeneration\n| Seed | Eval PR | Eval ISR | Comp. Mean | Failure Mode |\n|---|---|---|---|---|\n| 42 | 0.93 | 0.1232 | 6.58 | None (genuine) |\n| 43 | 0.14 | 0.00 | — | Output degeneration (max_tokens) |\n| 44 | 0.98 | 0.5700 | 2.04 | Tautological collapse (premise=conclusion) |\n\n**Verdict**: 2/3 seeds degenerate under exec-only reward. High training PR does not guarantee genuine formalization.\n\n### Claim 2: ISR + component count diagnoses genuine vs degenerate proofs\n| Experiment | Eval PR | Eval ISR | Comp. Mean | ISR Diagnosis |\n|---|---|---|---|---|\n| exec-only s42 (genuine) | 0.93 | 0.12 | 6.58 | Low ISR + high comp → genuine but imperfect |\n| exec-only s44 (tautological) | 0.98 | 0.57 | 2.04 | High ISR + low comp → **tautological artifact** |\n| convex random (tautological) | 1.00 | 0.54 | ~2 | High ISR + low comp → **tautological artifact** |\n| additive random (complex junk) | 0.48 | 0.05 | 9.60 | Low ISR + high comp → many premises but unused |\n| additive ISR β=0.1 (best) | 0.81 | 0.34 | 5.58 | Moderate ISR + high comp → **genuine improvement** |\n\n**Verdict**: ISR alone is ambiguous (s44 ISR=0.57 looks good but is tautological). Component count resolves the ambiguity: comp≈2 flags tautological collapse; comp>5 with moderate ISR indicates genuine proofs.\n\n### Claim 3: ISR-as-reward shows Goodhart effect at high dose, effective at low dose\n| Reward Mode | β | Eval PR | Eval ISR | Goodhart? |\n|---|---|---|---|---|\n| additive ISR | 0.3 | 0.18 | 0.03 | **Yes** — PR collapse |\n| additive ISR | 0.1 | 0.81 | 0.34 | **No** — sweet spot |\n| convex ISR | 0.1 | —¶ | — | Partially (train PR suppressed) |\n| convex random | 0.1 | 1.00 | 0.54 | Tautological (no ISR signal) |\n| additive random | 0.3 | 0.48 | 0.05 | N/A (random control) |\n\n**Verdict**: Clear dose-response. β=0.1 additive is the working point; β=0.3 triggers Goodhart collapse. Random controls confirm ISR signal is causal (not just variance regularization).\n\n## Notes\n\n† Component count for plan001-exec-only-s42-r2 (6.58) is cross-referenced from plan001-exec-only-s44 notes, not stored in registry eval metrics. May need re-verification with eval_sta.py.\n\n‡ **D029**: plan001-exec-only-s43-r4 was evaluated with sampling (do_sample=True, temperature=0.7) instead of eval_sta.py greedy decoding used for all other experiments. The PR=14% result is a failure case regardless of eval method — 87% of outputs hit max_new_tokens and are unparseable. Decision: not re-evaluated; paper will note the method difference.\n\n§ plan002-additive-b03-s42 eval_method not explicitly recorded in registry, but eval fields (eval_prove_rate, eval_mean_isr) are consistent with eval_sta.py output format.\n\n¶ **D030**: plan005-sta-low-s42 checkpoint was deleted; no eval was performed. Training log windowed metrics are the only available data. Paper uses training curves as evidence for \"ISR suppresses reward hacking\" (ISR/PR ratio stable at 0.30 across training).\n\n†† plan013-random-reward-s42-r4 component count not in registry metrics but noted as \"trivial 2-component proofs (premise=conclusion, conclusion=conclusion)\" in eval_note.\n\n## Excluded Experiments (Failed / Developmental)\n\nThe following DONE experiments are excluded from Table 1 (crashes, early phases, duplicates):\n\n| Experiment ID | Reason for Exclusion |\n|---|---|\n| sta-phase1-exec-only-r2/r3/r4/r5 | 100-step developmental runs |\n| sta-phase1-exec-sta-r2/r3/r4/r5 | 100-step developmental runs |\n| plan001-exec-only-s42 | Failed (pre-checkpoint crash) |\n| plan001-exec-only-s42-r3 | Failed (OOM duplicate submission) |\n| plan001-exec-only-s43 | Failed (OOM from plan013 GPU overflow) |\n| plan001-exec-only-s43-r2 | Failed (process crashed) |\n| plan001-exec-only-s43-r3 | Failed (disk full at step 23) |\n| plan013-random-reward-s42 | Failed (CUDA_VISIBLE_DEVICES not set) |\n| plan013-random-reward-s42-r2 | Failed (process crashed) |\n| plan013-random-reward-s42-r3 | Failed (disk full at step 28) |\n| plan003-eval-exec-only-r5 | Eval of 100-step checkpoint (not 500-step) |\n| plan014-downstream-nli-s42 | Downstream NLI task (separate analysis) |\n\n## Compact Table for Paper\n\n| Reward Mode | β | Seed | PR↑ | ISR↑ | Comp.↓ | Collapse? |\n|---|---|---|---|---|---|---|\n| *Base model* | — | — | .12 | .064 | — | — |\n| Exec-only | — | 42 | **.93** | .123 | 6.58 | No |\n| Exec-only | — | 43 | .14‡ | .000 | — | Degenerate |\n| Exec-only | — | 44 | .98 | .570 | 2.04 | **Tautological** |\n| Add. ISR | 0.3 | 42 | .18 | .026 | — | PR collapse |\n| **Add. ISR** | **0.1** | **42** | **.81** | **.337** | **5.58** | **No** |\n| Cvx. Random | 0.1 | 42 | 1.00 | .535 | ~2 | **Tautological** |\n| Add. Random | 0.3 | 42 | .48 | .045 | 9.60 | Complex junk |\n\n*Generated 2026-05-14. All eval metrics from eval_sta.py full STA unless noted.*\n",
      "numLines": 129,
      "startLine": 1,
      "totalLines": 129
    }
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the file and identify what needs to be changed:

1. **plan002-b03 component_count=10.67**: I need to find this. Looking at the file... In Group C, plan002-additive-b03-s42 has `—` for Comp. Mean already. In the Compact Table, it also shows `—`. Let me search more carefully... The user says "10.67" but I don't see 10.67 in the file. Let me re-read carefully.

Wait, I don't see 10.67 anywhere in this file. 

I'm searching through the document for "10.67" but it's not appearing anywhere. The plan002-b03 row already shows `—` for Comp. Mean in both tables, so either this change was already made or the number isn't present in the current version.

2. **plan013-r4 component_count ~2**: This is already shown as `~2` with footnote `††` that references an eval_note about trivial 2-component proofs. The task wants me to update the footnote to clarify that this is an estimated value from eval_note, not a precise calculation from eval_sta.py.

3. **plan002-b01**: I'm checking the file and plan002-additive-b01-s42 appears in Group C with PR=0.81, ISR=0.3365, and component_count=5.58, marked as "best: PR preserved + ISR 2.73x". It's also in the Compact Table with matching values, so it doesn't appear to be marked as incomplete or running. Let me verify what the task is asking me to find regarding plan002-b01.

Looking at the specific instructions again: I need to check if 10.67 appears anywhere in the file for plan002-b03 — it doesn't, the file already shows `—`. For plan013-r4, there's already a footnote `††` but I need to verify what the task requires for the footnote content.  The main actionable item is updating that footnote wording, while plan002-b01 doesn't seem to have any incomplete markers that need attention. Looking at the footnote more carefully, I need to update the `††` note to clarify that the component count is an estimate from eval_note rather than a precise calculation from eval_sta.py, and I should express this in Chinese to match the document's language. The revised footnote should indicate the source and nature of the estimate clearly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "09394bbd-fea8-4b59-808c-91e90f73c874",
  "uuid": "7e6e8875-03dd-4ff5-ac44-971c176e3cf5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017coWXF5FJd8smiBFRgvGFB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3779,
      "cache_read_input_tokens": 23781,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3779
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

_source line 8_

文件中 10.67 并不存在（plan002-b03 的 Comp. Mean 已经是 `—`），plan002-b01 也已标记为已完成状态。唯一需要修改的是 plan013-r4 的 `††` 脚注。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "09394bbd-fea8-4b59-808c-91e90f73c874",
  "uuid": "75becbf7-5482-475a-b620-f0a44cd4ad60",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017coWXF5FJd8smiBFRgvGFB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3779,
      "cache_read_input_tokens": 23781,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3779
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

_source line 9_

<details open><summary>🔧 Tool call — Edit · `toolu_01HJaSgRLc4JAchfui2zxB5k`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/paper_table1_evidence.md",
  "old_string": "†† plan013-random-reward-s42-r4 component count not in registry metrics but noted as \"trivial 2-component proofs (premise=conclusion, conclusion=conclusion)\" in eval_note.",
  "new_string": "†† plan013-random-reward-s42-r4 component count (~2) is an estimate from eval_note (\"trivial 2-component proofs, premise=conclusion, conclusion=conclusion\"), not a precise eval_sta.py computation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "09394bbd-fea8-4b59-808c-91e90f73c874",
  "uuid": "e190bd42-359f-4211-af29-f4efba8e4df7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017coWXF5FJd8smiBFRgvGFB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3779,
      "cache_read_input_tokens": 23781,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3779
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

_source line 10 · 2026-05-14T07:15:26.410Z_

<details><summary>↩ Tool result · `toolu_01HJaSgRLc4JAchfui2zxB5k`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/paper_table1_evidence.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "09394bbd-fea8-4b59-808c-91e90f73c874",
  "uuid": "a6ac3191-425a-48ed-8855-facd3b2915a3",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/paper_table1_evidence.md",
    "oldString": "†† plan013-random-reward-s42-r4 component count not in registry metrics but noted as \"trivial 2-component proofs (premise=conclusion, conclusion=conclusion)\" in eval_note.",
    "newString": "†† plan013-random-reward-s42-r4 component count (~2) is an estimate from eval_note (\"trivial 2-component proofs, premise=conclusion, conclusion=conclusion\"), not a precise eval_sta.py computation.",
    "originalFile": "# Table 1: Comprehensive Experimental Evidence for Solver-Trace Ablation\n\n**Model**: Qwen3-4B | **Training**: GRPO, 500 steps, K=8 | **Data**: train_500_seed42.jsonl (500 problems) | **Eval**: proofwriter_fol_100.jsonl (100 problems)\n\n## Main Results Table\n\n### Group A: Reference Baselines\n\n| Experiment ID | Reward Mode | Formula | β | Seed | Eval PR | Eval Mean ISR | ISR Std | Comp. Mean | Comp.=2 (%) | Eval Method | Diagnosis | Claims |\n|---|---|---|---|---|---|---|---|---|---|---|---|---|\n| sta-phase0-baseline | — (base model) | — | — | — | 0.12 | 0.0641 | 0.1983 | — | — | eval_sta.py | pre-training reference | — |\n| sta-gt-isr-baseline | — (ground truth FOL) | — | — | — | 0.18 | 0.5588 | 0.2582 | — | — | direct computation | ISR ceiling on gold FOL | — |\n\n### Group B: Exec-Only Reward (r = r_exec)\n\n| Experiment ID | Reward Mode | Formula | β | Seed | Eval PR | Eval Mean ISR | ISR Std | Comp. Mean | Comp.=2 (%) | Eval Method | Diagnosis | Claims |\n|---|---|---|---|---|---|---|---|---|---|---|---|---|\n| plan001-exec-only-s42-r2 | exec-only | r = r_exec | — | 42 | 0.93 | 0.1232 | 0.1887 | 6.58† | — | eval_sta.py | genuine proofs | C1 |\n| plan001-exec-only-s43-r4 | exec-only | r = r_exec | — | 43 | 0.14‡ | 0.00‡ | — | — | — | sampling (T=0.7)‡ | degraded (87% max_tokens) | C1, C2 |\n| plan001-exec-only-s44 | exec-only | r = r_exec | — | 44 | 0.98 | 0.5700 | 0.2013 | 2.04 | 94% | eval_sta.py | tautological collapse | C1, C2 |\n\n**Exec-only 3-seed summary**: mean PR = 0.68 ± 0.47, 2/3 seeds degenerate. Cross-seed instability is the primary finding.\n\n### Group C: Additive ISR Bonus (r = r_exec · (1 + β · ISR))\n\n| Experiment ID | Reward Mode | Formula | β | Seed | Eval PR | Eval Mean ISR | ISR Std | Comp. Mean | Comp.=2 (%) | Eval Method | Diagnosis | Claims |\n|---|---|---|---|---|---|---|---|---|---|---|---|---|\n| plan002-additive-b03-s42 | additive ISR | r = r_exec · (1 + β·ISR) | 0.3 | 42 | 0.18 | 0.0257 | 0.0742 | — | — | eval_sta.py§ | PR collapse (Goodhart) | C3 |\n| plan002-additive-b01-s42 | additive ISR | r = r_exec · (1 + β·ISR) | 0.1 | 42 | 0.81 | 0.3365 | 0.3227 | 5.58 | 3.7% | eval_sta.py | **best: PR preserved + ISR 2.73x** | C3 |\n\n**Dose-response**: β=0.3 → PR collapse (0.18); β=0.1 → PR preserved (0.81) with ISR 2.73x over exec-only baseline.\n\n### Group D: Convex ISR (r = α · r_exec + β · ISR)\n\n| Experiment ID | Reward Mode | Formula | β | Seed | Eval PR | Eval Mean ISR | ISR Std | Comp. Mean | Comp.=2 (%) | Eval Method | Diagnosis | Claims |\n|---|---|---|---|---|---|---|---|---|---|---|---|---|\n| plan005-sta-low-s42 | convex ISR | r = 0.9·r_exec + 0.1·ISR | 0.1 | 42 | —¶ | —¶ | —¶ | — | — | training logs only¶ | PR suppressed (train last100 PR=0.77) | C3 |\n\n### Group E: Convex Random Control (r = α · r_exec + β · random)\n\n| Experiment ID | Reward Mode | Formula | β | Seed | Eval PR | Eval Mean ISR | ISR Std | Comp. Mean | Comp.=2 (%) | Eval Method | Diagnosis | Claims |\n|---|---|---|---|---|---|---|---|---|---|---|---|---|\n| plan013-random-reward-s42-r4 | convex random | r = 0.9·r_exec + 0.1·random | 0.1 | 42 | 1.00 | 0.5350 | 0.1282 | ~2†† | ~100%†† | eval_sta.py | tautological collapse | C2 |\n\n### Group F: Additive Random Control (r = r_exec · (1 + β · random))\n\n| Experiment ID | Reward Mode | Formula | β | Seed | Eval PR | Eval Mean ISR | ISR Std | Comp. Mean | Comp.=2 (%) | Eval Method | Diagnosis | Claims |\n|---|---|---|---|---|---|---|---|---|---|---|---|---|\n| plan017-additive-random-s42 | additive random | r = r_exec · (1 + β·random) | 0.3 | 42 | 0.48 | 0.0453 | 0.0759 | 9.60 | 0% | eval_sta.py | complex but useless formalizations | C2, C3 |\n\n## Claim Evidence Summary\n\n### Claim 1: Exec-only reward exhibits cross-seed degeneration\n| Seed | Eval PR | Eval ISR | Comp. Mean | Failure Mode |\n|---|---|---|---|---|\n| 42 | 0.93 | 0.1232 | 6.58 | None (genuine) |\n| 43 | 0.14 | 0.00 | — | Output degeneration (max_tokens) |\n| 44 | 0.98 | 0.5700 | 2.04 | Tautological collapse (premise=conclusion) |\n\n**Verdict**: 2/3 seeds degenerate under exec-only reward. High training PR does not guarantee genuine formalization.\n\n### Claim 2: ISR + component count diagnoses genuine vs degenerate proofs\n| Experiment | Eval PR | Eval ISR | Comp. Mean | ISR Diagnosis |\n|---|---|---|---|---|\n| exec-only s42 (genuine) | 0.93 | 0.12 | 6.58 | Low ISR + high comp → genuine but imperfect |\n| exec-only s44 (tautological) | 0.98 | 0.57 | 2.04 | High ISR + low comp → **tautological artifact** |\n| convex random (tautological) | 1.00 | 0.54 | ~2 | High ISR + low comp → **tautological artifact** |\n| additive random (complex junk) | 0.48 | 0.05 | 9.60 | Low ISR + high comp → many premises but unused |\n| additive ISR β=0.1 (best) | 0.81 | 0.34 | 5.58 | Moderate ISR + high comp → **genuine improvement** |\n\n**Verdict**: ISR alone is ambiguous (s44 ISR=0.57 looks good but is tautological). Component count resolves the ambiguity: comp≈2 flags tautological collapse; comp>5 with moderate ISR indicates genuine proofs.\n\n### Claim 3: ISR-as-reward shows Goodhart effect at high dose, effective at low dose\n| Reward Mode | β | Eval PR | Eval ISR | Goodhart? |\n|---|---|---|---|---|\n| additive ISR | 0.3 | 0.18 | 0.03 | **Yes** — PR collapse |\n| additive ISR | 0.1 | 0.81 | 0.34 | **No** — sweet spot |\n| convex ISR | 0.1 | —¶ | — | Partially (train PR suppressed) |\n| convex random | 0.1 | 1.00 | 0.54 | Tautological (no ISR signal) |\n| additive random | 0.3 | 0.48 | 0.05 | N/A (random control) |\n\n**Verdict**: Clear dose-response. β=0.1 additive is the working point; β=0.3 triggers Goodhart collapse. Random controls confirm ISR signal is causal (not just variance regularization).\n\n## Notes\n\n† Component count for plan001-exec-only-s42-r2 (6.58) is cross-referenced from plan001-exec-only-s44 notes, not stored in registry eval metrics. May need re-verification with eval_sta.py.\n\n‡ **D029**: plan001-exec-only-s43-r4 was evaluated with sampling (do_sample=True, temperature=0.7) instead of eval_sta.py greedy decoding used for all other experiments. The PR=14% result is a failure case regardless of eval method — 87% of outputs hit max_new_tokens and are unparseable. Decision: not re-evaluated; paper will note the method difference.\n\n§ plan002-additive-b03-s42 eval_method not explicitly recorded in registry, but eval fields (eval_prove_rate, eval_mean_isr) are consistent with eval_sta.py output format.\n\n¶ **D030**: plan005-sta-low-s42 checkpoint was deleted; no eval was performed. Training log windowed metrics are the only available data. Paper uses training curves as evidence for \"ISR suppresses reward hacking\" (ISR/PR ratio stable at 0.30 across training).\n\n†† plan013-random-reward-s42-r4 component count not in registry metrics but noted as \"trivial 2-component proofs (premise=conclusion, conclusion=conclusion)\" in eval_note.\n\n## Excluded Experiments (Failed / Developmental)\n\nThe following DONE experiments are excluded from Table 1 (crashes, early phases, duplicates):\n\n| Experiment ID | Reason for Exclusion |\n|---|---|\n| sta-phase1-exec-only-r2/r3/r4/r5 | 100-step developmental runs |\n| sta-phase1-exec-sta-r2/r3/r4/r5 | 100-step developmental runs |\n| plan001-exec-only-s42 | Failed (pre-checkpoint crash) |\n| plan001-exec-only-s42-r3 | Failed (OOM duplicate submission) |\n| plan001-exec-only-s43 | Failed (OOM from plan013 GPU overflow) |\n| plan001-exec-only-s43-r2 | Failed (process crashed) |\n| plan001-exec-only-s43-r3 | Failed (disk full at step 23) |\n| plan013-random-reward-s42 | Failed (CUDA_VISIBLE_DEVICES not set) |\n| plan013-random-reward-s42-r2 | Failed (process crashed) |\n| plan013-random-reward-s42-r3 | Failed (disk full at step 28) |\n| plan003-eval-exec-only-r5 | Eval of 100-step checkpoint (not 500-step) |\n| plan014-downstream-nli-s42 | Downstream NLI task (separate analysis) |\n\n## Compact Table for Paper\n\n| Reward Mode | β | Seed | PR↑ | ISR↑ | Comp.↓ | Collapse? |\n|---|---|---|---|---|---|---|\n| *Base model* | — | — | .12 | .064 | — | — |\n| Exec-only | — | 42 | **.93** | .123 | 6.58 | No |\n| Exec-only | — | 43 | .14‡ | .000 | — | Degenerate |\n| Exec-only | — | 44 | .98 | .570 | 2.04 | **Tautological** |\n| Add. ISR | 0.3 | 42 | .18 | .026 | — | PR collapse |\n| **Add. ISR** | **0.1** | **42** | **.81** | **.337** | **5.58** | **No** |\n| Cvx. Random | 0.1 | 42 | 1.00 | .535 | ~2 | **Tautological** |\n| Add. Random | 0.3 | 42 | .48 | .045 | 9.60 | Complex junk |\n\n*Generated 2026-05-14. All eval metrics from eval_sta.py full STA unless noted.*\n",
    "structuredPatch": [
      {
        "oldStart": 91,
        "oldLines": 7,
        "newStart": 91,
        "newLines": 7,
        "lines": [
          " ",
          " ¶ **D030**: plan005-sta-low-s42 checkpoint was deleted; no eval was performed. Training log windowed metrics are the only available data. Paper uses training curves as evidence for \"ISR suppresses reward hacking\" (ISR/PR ratio stable at 0.30 across training).",
          " ",
          "-†† plan013-random-reward-s42-r4 component count not in registry metrics but noted as \"trivial 2-component proofs (premise=conclusion, conclusion=conclusion)\" in eval_note.",
          "+†† plan013-random-reward-s42-r4 component count (~2) is an estimate from eval_note (\"trivial 2-component proofs, premise=conclusion, conclusion=conclusion\"), not a precise eval_sta.py computation.",
          " ",
          " ## Excluded Experiments (Failed / Developmental)",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 11_

修改完成。实际变更：

1. **plan002-b03 component_count=10.67**：文件中不存在 10.67，Comp. Mean 列已经是 `—`，无需修改。
2. **plan013-r4 `††` 脚注**：已更新，明确标注 `~2` 为 eval_note 估算值，非 eval_sta.py 精确计算。
3. **plan002-b01**：文件中无"待完成"或"RUNNING"标记，已显示完成数据（PR=0.81, ISR=0.3365, Comp.=5.58），无需修改。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "09394bbd-fea8-4b59-808c-91e90f73c874",
  "uuid": "d60b1598-cae9-4fef-9cca-c066a1b9f21e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KkQa1Fu5uTdFRWJyYrGAUt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1804,
      "cache_read_input_tokens": 27560,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1804
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

_source line 12_

修改完成。实际变更：

1. **plan002-b03 component_count=10.67**：文件中不存在 10.67，Comp. Mean 列已经是 `—`，无需修改。
2. **plan013-r4 `††` 脚注**：已更新，明确标注 `~2` 为 eval_note 估算值，非 eval_sta.py 精确计算。
3. **plan002-b01**：文件中无"待完成"或"RUNNING"标记，已显示完成数据（PR=0.81, ISR=0.3365, Comp.=5.58），无需修改。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 39439,
  "duration_api_ms": 40310,
  "num_turns": 3,
  "stop_reason": "end_turn",
  "session_id": "09394bbd-fea8-4b59-808c-91e90f73c874",
  "total_cost_usd": 0.19339874999999998,
  "usage": {
    "input_tokens": 5,
    "cache_creation_input_tokens": 17523,
    "cache_read_input_tokens": 63182,
    "output_tokens": 2015,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 17523,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 181,
        "cache_read_input_tokens": 27560,
        "cache_creation_input_tokens": 1804,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1804
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1809,
      "outputTokens": 16,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001889,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 5,
      "outputTokens": 2015,
      "cacheReadInputTokens": 63182,
      "cacheCreationInputTokens": 17523,
      "webSearchRequests": 0,
      "costUSD": 0.19150975,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "f67fc417-847c-4d32-9e5f-577b13a1a2c3"
}
```

</details>

---
