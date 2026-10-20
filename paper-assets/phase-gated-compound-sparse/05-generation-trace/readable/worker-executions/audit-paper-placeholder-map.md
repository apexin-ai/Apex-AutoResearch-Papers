# audit paper placeholder map

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 63
- **Recorded user turns:** 0
- **Tool calls:** 22
- **Original source:** `logs/workers/worker_audit_paper_placeholder_map_20260515T014315.log`
- **Structured JSON:** [`b66a3ba5400884de6047.json`](../../sessions/b6/b66a3ba5400884de6047.json)

## Before a recorded user message

63 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250",
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
  "uuid": "d4227887-5b42-4640-9319-e40ea895ad8c",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/memory/"
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
    "resetsAt": 1778812800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "b31ee2f2-f3d7-4221-8c4b-dbb6ea63e7cf",
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to audit all the places in their paper that need updating when they switch from n=50 to n=500 data. I need to:

1. Scan all tex files for `\placeholder{` macros
2. Scan for hardcoded n=50 values
3. Check for existing planning documents
4. Generate a comprehensive audit report

Let me start by exploring the paper directory and searching for the relevant patterns.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250",
  "uuid": "96a22d94-285b-4edf-8036-2006368d2254",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016CBHzTTRfXvCh5fGrBpMeW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11965,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11965
      },
      "output_tokens": 21,
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

_source line 5_

I'll scan the paper files and search for existing planning documents in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250",
  "uuid": "c7caf855-a082-4e28-ac96-553998fb6d0a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016CBHzTTRfXvCh5fGrBpMeW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11965,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11965
      },
      "output_tokens": 21,
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

_source line 6_

<details open><summary>🔧 Tool call — Glob · `toolu_018qEVbxGMt9t7BCtr5qfV2R`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250",
  "uuid": "987dae64-712f-42e2-b74e-14e306a3958f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016CBHzTTRfXvCh5fGrBpMeW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11965,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11965
      },
      "output_tokens": 21,
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

_source line 7 · 2026-05-15T01:43:30.030Z_

<details><summary>↩ Tool result · `toolu_018qEVbxGMt9t7BCtr5qfV2R`</summary>

```text
artifacts/_project/paper/appendix.tex
artifacts/_project/paper/background.tex
artifacts/_project/paper/analysis.tex
artifacts/_project/paper/conclusion.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/results.tex
artifacts/_project/paper/appendix_disc_analysis.tex
artifacts/_project/paper/methodology.tex
artifacts/_project/paper/limitations.tex
artifacts/_project/paper/main.tex
artifacts/_project/paper/appendix_results.tex
artifacts/_project/paper/appendix_moved.tex
artifacts/_project/paper/abstract.tex
artifacts/_project/paper/discussion.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250",
  "uuid": "1401fb0c-8e0d-48a5-8553-88c728e72390",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/paper/appendix.tex",
      "artifacts/_project/paper/background.tex",
      "artifacts/_project/paper/analysis.tex",
      "artifacts/_project/paper/conclusion.tex",
      "artifacts/_project/paper/introduction.tex",
      "artifacts/_project/paper/related_work.tex",
      "artifacts/_project/paper/results.tex",
      "artifacts/_project/paper/appendix_disc_analysis.tex",
      "artifacts/_project/paper/methodology.tex",
      "artifacts/_project/paper/limitations.tex",
      "artifacts/_project/paper/main.tex",
      "artifacts/_project/paper/appendix_results.tex",
      "artifacts/_project/paper/appendix_moved.tex",
      "artifacts/_project/paper/abstract.tex",
      "artifacts/_project/paper/discussion.tex"
    ],
    "durationMs": 19,
    "numFiles": 15,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Grep · `toolu_01YXtcUuRXiMnjHT7eLG5asY`</summary>

```json
{
  "pattern": "\\\\placeholder\\{",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "output_mode": "content",
  "-n": true,
  "context": 1,
  "head_limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250",
  "uuid": "1b06aa1f-a56e-4bb2-b734-e84cf75c88fd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016CBHzTTRfXvCh5fGrBpMeW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11965,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11965
      },
      "output_tokens": 21,
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

_source line 9 · 2026-05-15T01:43:31.340Z_

<details><summary>↩ Tool result · `toolu_01YXtcUuRXiMnjHT7eLG5asY`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex-9-
artifacts/_project/paper/discussion.tex:10:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex-11-
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex-14-\paragraph{Architecture-dependent magnitude.}
artifacts/_project/paper/discussion.tex:15:[Omitted long matching line]
--
artifacts/_project/paper/appendix_moved.tex-29-\label{app:qwen-null-rate}
artifacts/_project/paper/appendix_moved.tex:30:Table~\ref{tab:qwen-effective-n} reports the per-phase effective sample size for Qwen2.5-7B-Instruct, defined as the number of problems with $|\mathrm{II}| > 0.001$ in each phase. The mid-phase null rate (\placeholder{NULL\_PCT}\%) reflects problems where compound interaction is absent in intermediate phases; this does not affect the low--high contrast ($\Delta$) used in the primary analysis.
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex-31-
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex-34-\small
artifacts/_project/paper/appendix_moved.tex:35:\caption{Per-phase effective sample size for Qwen2.5-7B-Instruct ($n_{\text{total}} = \placeholder{N\_QW}$).}
artifacts/_project/paper/appendix_moved.tex-36-\label{tab:qwen-effective-n}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex-40-\midrule
artifacts/_project/paper/appendix_moved.tex:41:High & \placeholder{} & \placeholder{} & \placeholder{} & \placeholder{} \\
artifacts/_project/paper/appendix_moved.tex:42:Mid  & \placeholder{} & \placeholder{} & \placeholder{} & \placeholder{} \\
artifacts/_project/paper/appendix_moved.tex:43:Low  & \placeholder{} & \placeholder{} & \placeholder{} & \placeholder{} \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex-44-\bottomrule
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex-72-\paragraph{Per-problem concordance.}
artifacts/_project/paper/appendix_moved.tex:73:The per-problem concordance across models is not significant (median $\rho = \placeholder{}$, $p = \placeholder{}$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking. % exp_id: cross_model_analysis.json (spearman_rho=1.0, gradient_permutation_p=0.043, per_problem_concordance_p=0.926, mean_rho=-0.107)
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex-74-
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex-75-\paragraph{Random eviction control.}
artifacts/_project/paper/appendix_moved.tex:76:As a control, random eviction on Qwen yields no systematic phase gradient at three of four sparsity levels (3/4 FAIL), mirroring DeepSeek's 4/4 FAIL pattern. At $s{=}0.30$, Qwen random produces a borderline PASS (permutation $p = 0.012$) but with negligible median difference ($\widetilde{\Delta} = \placeholder{}$, CI spans zero), indicating no meaningful phase modulation. % exp_id: bf16_qw_rand_s015..s030; source: experiment_summary_table.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex-77-
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_results.tex-6-\paragraph{Per-problem concordance.}
artifacts/_project/paper/appendix_results.tex:7:The per-problem concordance across models is not significant (median $\rho = \placeholder{}$, $p = \placeholder{}$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking. % exp_id: cross_model_analysis.json (spearman_rho=1.0, gradient_permutation_p=0.043, per_problem_concordance_p=0.926, mean_rho=-0.107)
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_results.tex-8-
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_results.tex-9-\paragraph{Random eviction control.}
artifacts/_project/paper/appendix_results.tex:10:As a control, random eviction on Qwen yields no systematic phase gradient at three of four sparsity levels (3/4 FAIL), mirroring DeepSeek's 4/4 FAIL pattern. At $s{=}0.30$, Qwen random produces a borderline PASS (permutation $p = 0.012$) but with negligible median difference ($\widetilde{\Delta} = \placeholder{}$, CI spans zero), indicating no meaningful phase modulation. % exp_id: bf16_qw_rand_s015..s030; source: experiment_summary_table.json
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex-7-Under importance-based KV cache eviction, the median Interaction Index difference between low-sparsity and high-sparsity reasoning phases increases monotonically from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired Cohen's $d_z$ growing from $0.44$ (small) to $0.80$ (large); Bonferroni-corrected permutation tests yield $p < 0.005$ at all four sparsity levels.
artifacts/_project/paper/abstract.tex:8:Random eviction produces no significant phase modulation in 7/8 conditions; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) shows negligible median difference ($\widetilde{\Delta} = \placeholder{}$), confirming that the severity gradient is strategy-specific, not an inherent property of compound sparsity.
artifacts/_project/paper/abstract.tex-9-At $s{=}0.25$, a crossover emerges: importance-based eviction outperforms random in high-sparsity phases ($\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$) yet underperforms in low-sparsity phases ($\widetilde{\mathrm{II}} = 7.196$ vs.\ $1.363$)---a qualitative reversal in strategy ranking.
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex-70-
artifacts/_project/paper/results.tex:71:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex-72-
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex-80-
artifacts/_project/paper/results.tex:81:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex-82-
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex-85-\small
artifacts/_project/paper/results.tex:86:\caption{Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM). $\widetilde{\Delta}$: median paired difference (importance $-$ random) with bootstrap 95\% CI ($B{=}10{,}000$); $p$: Bonferroni-corrected Wilcoxon signed-rank $p$ ($k{=}4$). $n{=}\placeholder{N\_LLAMA}$ paired problems.}
artifacts/_project/paper/results.tex-87-\label{tab:llama-cross-arch}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex-91-\midrule
artifacts/_project/paper/results.tex:92:0.15 & \placeholder{}\; $[\placeholder{}, \placeholder{}]$ & \placeholder{} \\
artifacts/_project/paper/results.tex:93:0.20 & \placeholder{}\; $[\placeholder{}, \placeholder{}]$ & \placeholder{} \\
artifacts/_project/paper/results.tex:94:0.25 & \placeholder{}\; $[\placeholder{}, \placeholder{}]$ & \placeholder{} \\
artifacts/_project/paper/results.tex:95:0.30 & \placeholder{}\; $[\placeholder{}, \placeholder{}]$ & $\mathbf{\placeholder{}}$ \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex-96-\bottomrule
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex-13-\paragraph{Random masking as falsification control.}
artifacts/_project/paper/appendix_disc_analysis.tex:14:Random eviction fails 7/8 paired permutation tests across both models; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) exhibits negligible effect size ($\widetilde{\Delta} = \placeholder{}$). The absence of a phase gradient under random masking isolates the amplification as strategy-specific. % exp_id: bf16_ds_rand_s015..s030, bf16_qw_rand_s015..s030
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex-15-
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex-48-
artifacts/_project/paper/appendix_disc_analysis.tex:49:A notable exception among the random baselines is the Qwen random condition at $s{=}0.30$, which yields a statistically significant result ($p{=}0.012$) despite negligible effect size ($\widetilde{\Delta} = \placeholder{}$, bootstrap CI spanning zero). % exp_id: qw_rand_s030; B=10000, p=0.012, d=-0.035, negligible
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex-50-This case illustrates that dichotomous significance testing can flag effects of no practical magnitude---reinforcing the importance of reporting effect sizes and confidence intervals alongside $p$-values.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250",
  "uuid": "d91cbad6-ad1f-4921-9abc-7afb38412d77",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex-9-\nartifacts/_project/paper/discussion.tex:10:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex-11-\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex-14-\\paragraph{Architecture-dependent magnitude.}\nartifacts/_project/paper/discussion.tex:15:[Omitted long matching line]\n--\nartifacts/_project/paper/appendix_moved.tex-29-\\label{app:qwen-null-rate}\nartifacts/_project/paper/appendix_moved.tex:30:Table~\\ref{tab:qwen-effective-n} reports the per-phase effective sample size for Qwen2.5-7B-Instruct, defined as the number of problems with $|\\mathrm{II}| > 0.001$ in each phase. The mid-phase null rate (\\placeholder{NULL\\_PCT}\\%) reflects problems where compound interaction is absent in intermediate phases; this does not affect the low--high contrast ($\\Delta$) used in the primary analysis.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex-31-\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex-34-\\small\nartifacts/_project/paper/appendix_moved.tex:35:\\caption{Per-phase effective sample size for Qwen2.5-7B-Instruct ($n_{\\text{total}} = \\placeholder{N\\_QW}$).}\nartifacts/_project/paper/appendix_moved.tex-36-\\label{tab:qwen-effective-n}\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex-40-\\midrule\nartifacts/_project/paper/appendix_moved.tex:41:High & \\placeholder{} & \\placeholder{} & \\placeholder{} & \\placeholder{} \\\\\nartifacts/_project/paper/appendix_moved.tex:42:Mid  & \\placeholder{} & \\placeholder{} & \\placeholder{} & \\placeholder{} \\\\\nartifacts/_project/paper/appendix_moved.tex:43:Low  & \\placeholder{} & \\placeholder{} & \\placeholder{} & \\placeholder{} \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex-44-\\bottomrule\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex-72-\\paragraph{Per-problem concordance.}\nartifacts/_project/paper/appendix_moved.tex:73:The per-problem concordance across models is not significant (median $\\rho = \\placeholder{}$, $p = \\placeholder{}$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking. % exp_id: cross_model_analysis.json (spearman_rho=1.0, gradient_permutation_p=0.043, per_problem_concordance_p=0.926, mean_rho=-0.107)\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex-74-\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex-75-\\paragraph{Random eviction control.}\nartifacts/_project/paper/appendix_moved.tex:76:As a control, random eviction on Qwen yields no systematic phase gradient at three of four sparsity levels (3/4 FAIL), mirroring DeepSeek's 4/4 FAIL pattern. At $s{=}0.30$, Qwen random produces a borderline PASS (permutation $p = 0.012$) but with negligible median difference ($\\widetilde{\\Delta} = \\placeholder{}$, CI spans zero), indicating no meaningful phase modulation. % exp_id: bf16_qw_rand_s015..s030; source: experiment_summary_table.json\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex-77-\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_results.tex-6-\\paragraph{Per-problem concordance.}\nartifacts/_project/paper/appendix_results.tex:7:The per-problem concordance across models is not significant (median $\\rho = \\placeholder{}$, $p = \\placeholder{}$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking. % exp_id: cross_model_analysis.json (spearman_rho=1.0, gradient_permutation_p=0.043, per_problem_concordance_p=0.926, mean_rho=-0.107)\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_results.tex-8-\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_results.tex-9-\\paragraph{Random eviction control.}\nartifacts/_project/paper/appendix_results.tex:10:As a control, random eviction on Qwen yields no systematic phase gradient at three of four sparsity levels (3/4 FAIL), mirroring DeepSeek's 4/4 FAIL pattern. At $s{=}0.30$, Qwen random produces a borderline PASS (permutation $p = 0.012$) but with negligible median difference ($\\widetilde{\\Delta} = \\placeholder{}$, CI spans zero), indicating no meaningful phase modulation. % exp_id: bf16_qw_rand_s015..s030; source: experiment_summary_table.json\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex-7-Under importance-based KV cache eviction, the median Interaction Index difference between low-sparsity and high-sparsity reasoning phases increases monotonically from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired Cohen's $d_z$ growing from $0.44$ (small) to $0.80$ (large); Bonferroni-corrected permutation tests yield $p < 0.005$ at all four sparsity levels.\nartifacts/_project/paper/abstract.tex:8:Random eviction produces no significant phase modulation in 7/8 conditions; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) shows negligible median difference ($\\widetilde{\\Delta} = \\placeholder{}$), confirming that the severity gradient is strategy-specific, not an inherent property of compound sparsity.\nartifacts/_project/paper/abstract.tex-9-At $s{=}0.25$, a crossover emerges: importance-based eviction outperforms random in high-sparsity phases ($\\widetilde{\\mathrm{II}} = 0.032$ vs.\\ $0.818$) yet underperforms in low-sparsity phases ($\\widetilde{\\mathrm{II}} = 7.196$ vs.\\ $1.363$)---a qualitative reversal in strategy ranking.\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex-70-\nartifacts/_project/paper/results.tex:71:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex-72-\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex-80-\nartifacts/_project/paper/results.tex:81:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex-82-\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex-85-\\small\nartifacts/_project/paper/results.tex:86:\\caption{Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM). $\\widetilde{\\Delta}$: median paired difference (importance $-$ random) with bootstrap 95\\% CI ($B{=}10{,}000$); $p$: Bonferroni-corrected Wilcoxon signed-rank $p$ ($k{=}4$). $n{=}\\placeholder{N\\_LLAMA}$ paired problems.}\nartifacts/_project/paper/results.tex-87-\\label{tab:llama-cross-arch}\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex-91-\\midrule\nartifacts/_project/paper/results.tex:92:0.15 & \\placeholder{}\\; $[\\placeholder{}, \\placeholder{}]$ & \\placeholder{} \\\\\nartifacts/_project/paper/results.tex:93:0.20 & \\placeholder{}\\; $[\\placeholder{}, \\placeholder{}]$ & \\placeholder{} \\\\\nartifacts/_project/paper/results.tex:94:0.25 & \\placeholder{}\\; $[\\placeholder{}, \\placeholder{}]$ & \\placeholder{} \\\\\nartifacts/_project/paper/results.tex:95:0.30 & \\placeholder{}\\; $[\\placeholder{}, \\placeholder{}]$ & $\\mathbf{\\placeholder{}}$ \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex-96-\\bottomrule\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex-13-\\paragraph{Random masking as falsification control.}\nartifacts/_project/paper/appendix_disc_analysis.tex:14:Random eviction fails 7/8 paired permutation tests across both models; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) exhibits negligible effect size ($\\widetilde{\\Delta} = \\placeholder{}$). The absence of a phase gradient under random masking isolates the amplification as strategy-specific. % exp_id: bf16_ds_rand_s015..s030, bf16_qw_rand_s015..s030\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex-15-\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex-48-\nartifacts/_project/paper/appendix_disc_analysis.tex:49:A notable exception among the random baselines is the Qwen random condition at $s{=}0.30$, which yields a statistically significant result ($p{=}0.012$) despite negligible effect size ($\\widetilde{\\Delta} = \\placeholder{}$, bootstrap CI spanning zero). % exp_id: qw_rand_s030; B=10000, p=0.012, d=-0.035, negligible\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex-50-This case illustrates that dichotomous significance testing can flag effects of no practical magnitude---reinforcing the importance of reporting effect sizes and confidence intervals alongside $p$-values.",
    "numLines": 64
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Grep · `toolu_01HqgjD7K3t2KyHHCvGppTNV`</summary>

```json
{
  "pattern": "n500_paper_update|paper_n500_update|paper_update",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts",
  "-i": true,
  "head_limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250",
  "uuid": "95c7e00b-c700-45f1-924e-1730dbae4bbe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016CBHzTTRfXvCh5fGrBpMeW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11965,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11965
      },
      "output_tokens": 21,
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

_source line 11 · 2026-05-15T01:43:32.525Z_

<details><summary>↩ Tool result · `toolu_01HqgjD7K3t2KyHHCvGppTNV`</summary>

```text
Found 2 files
artifacts/manifest.yaml
artifacts/n500_paper_update_checklist.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250",
  "uuid": "1da747ce-e994-4bc7-b1f1-05d03365426e",
  "tool_use_result": {
    "mode": "files_with_matches",
    "filenames": [
      "artifacts/manifest.yaml",
      "artifacts/n500_paper_update_checklist.md"
    ],
    "numFiles": 2
  }
}
```

</details>

---

### Assistant

_source line 12_

<details><summary>Logged reasoning block</summary>

```text
Good, I found the placeholder occurrences and there's an existing checklist file. Let me now:
1. Read the existing checklist
2. Read the full content of files that have placeholders to get exact line numbers
3. Search for hardcoded n=50 values in tables and inline statistics

Let me also read the lines that were omitted (long lines in discussion.tex and results.tex).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250",
  "uuid": "40408cfd-3f44-418f-81e2-064b4303c172",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015CLDLsECci42Epf4yqKCcN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4096,
      "cache_read_input_tokens": 23412,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4096
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

_source line 13_

Found placeholders and an existing checklist. Let me read the full files and search for hardcoded values.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250",
  "uuid": "80b04e6a-d08a-4337-a359-7f81279b3022",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015CLDLsECci42Epf4yqKCcN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4096,
      "cache_read_input_tokens": 23412,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4096
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

_source line 14_

<details open><summary>🔧 Tool call — Read · `toolu_015KxUR67KjxsP1bejnJ2h3F`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/n500_paper_update_checklist.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250",
  "uuid": "528f876b-cad1-478b-8962-a3ee5195daf6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015CLDLsECci42Epf4yqKCcN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4096,
      "cache_read_input_tokens": 23412,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4096
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

_source line 15 · 2026-05-15T01:43:39.645Z_

<details><summary>↩ Tool result · `toolu_015KxUR67KjxsP1bejnJ2h3F`</summary>

````text
1	# n=500 论文更新清单
2	
3	> 当 C2 n=500 实验（DeepSeek 8 conditions + Qwen 8 conditions）全部完成后，用此清单逐项替换论文中所有 n=50 数据。
4	> 数据来源均在服务器 `/root/autodl-tmp/pacs/analysis_output/` 下。
5	> **原则**：DeepSeek 和 Qwen 数值绝对值差 ~5×，不可混用；所有数值精确替换，不可近似。
6	> **基于**：`c2_n500_paper_update_checklist.md` 增补 LLaMA 间接影响、文献完整性、C5b/C8 叙事追踪。
7	
8	---
9	
10	## 1. 样本量文本替换（全局搜索 "50"）
11	
12	| 文件 | 行号 | 当前文本 | 替换为 | 类型 |
13	|------|------|---------|--------|------|
14	| abstract.tex | 6 | `50 MATH-500 problems` | `500 MATH-500 problems` | 文本 |
15	| methodology.tex | 10 | `50 problems stratified from MATH-500` | `500 problems from MATH-500` | 文本 |
16	| results.tex | 13 | `$n{=}50$ MATH-500 problems` (Table 1 caption) | `$n{=}500$` | 文本 |
17	| results.tex | 34 | `medians across 50 problems` (Table 2 caption) | `medians across 500 problems` | 文本 |
18	| appendix_moved.tex | 26 | `$n{=}46$ valid problems for Qwen (vs.\ $n{=}49$ for DeepSeek)` | n=500 后的有效样本量（需从数据计算） | 文本 |
19	| appendix_moved.tex | 26 | `Four of the 50 problems are excluded` | 新排除数/总数 | 文本 |
20	| appendix_moved.tex | 73 | `$n{=}49$, $10{,}000$ permutations` (Table permutation caption) | 新 n 值 | 文本 |
21	| appendix_disc_analysis.tex | 45 | `$n{=}49$ paired problems for DeepSeek (1 excluded) and $n{=}46$ for Qwen (4 excluded)` | 新排除数/有效 n | 文本 |
22	
23	**注意**：results.tex L77/L86 中 LLaMA 的 `$n{=}49$` **不改**（LLaMA 实验仍为 n=50）。
24	
25	---
26	
27	## 2. Tables
28	
29	### Table 1: Aggregate II (tab:aggregate-ii) — results.tex L10-23
30	
31	| 行/列 | 当前值 | 数据来源 | 更新类型 |
32	|--------|--------|----------|----------|
33	| Importance s=0.15 | 0.39 | experiment_summary_table.json → DS imp s015 median_diff | 数值替换 |
34	| Importance s=0.20 | 1.48 | experiment_summary_table.json → DS imp s020 median_diff | 数值替换 |
35	| Importance s=0.25 | 7.16 | experiment_summary_table.json → DS imp s025 median_diff | 数值替换 |
36	| Importance s=0.30 | 14.59 | experiment_summary_table.json → DS imp s030 median_diff | 数值替换 |
37	| Random s=0.15 | 0.01 | experiment_summary_table.json → DS rand s015 median_diff | 数值替换 |
38	| Random s=0.20 | −0.02 | experiment_summary_table.json → DS rand s020 median_diff | 数值替换 |
39	| Random s=0.25 | 0.54 | experiment_summary_table.json → DS rand s025 median_diff | 数值替换 |
40	| Random s=0.30 | 1.54 | experiment_summary_table.json → DS rand s030 median_diff | 数值替换 |
41	| 正文 L8 | `$0.39$...$14.59$...37×` | 同上，37× = 14.59/0.39 需重算 | 数值+比率 |
42	| 正文 L8 | `$-0.02$ to $1.54$` | random range 需从新数据取 | 数值替换 |
43	
44	### Table 2: Per-phase II breakdown (tab:main-results) — results.tex L31-53
45	
46	| 行 | II_high | II_mid | II_low | Δ | G | 数据来源 |
47	|----|---------|--------|--------|---|---|----------|
48	| 0.15 Imp | 0.006 | 0.081 | 0.398 | 0.39 | 69 | DS imp s015 per-phase medians |
49	| 0.15 Rand | 0.093 | 0.097 | 0.103 | 0.01 | 1.1 | DS rand s015 per-phase medians |
50	| 0.20 Imp | 0.015 | 0.203 | 1.496 | 1.48 | 103 | DS imp s020 per-phase medians |
51	| 0.20 Rand | 0.292 | 0.350 | 0.276 | −0.02 | 0.9 | DS rand s020 per-phase medians |
52	| 0.25 Imp | 0.032 | 1.118 | 7.196 | 7.16 | 222 | DS imp s025 per-phase medians |
53	| 0.25 Rand | 0.818 | 0.932 | 1.363 | 0.54 | 1.7 | DS rand s025 per-phase medians |
54	| 0.30 Imp | 0.053 | 2.283 | 14.639 | 14.59 | 274 | DS imp s030 per-phase medians |
55	| 0.30 Rand | 2.503 | 2.592 | 4.041 | 1.54 | 1.6 | DS rand s030 per-phase medians |
56	
57	数据来源：`experiment_summary_table.json` 中各 condition 的 `median_low`, `median_mid`, `median_high`。
58	
59	### Table 3: Cohen's d (tab:cohens-d) — results.tex L108-124
60	
61	| 行 | DS d_z | DS Δ̃ [CI] | QW d_z | QW Δ̃ [CI] | 数据来源 |
62	|----|--------|-----------|--------|-----------|----------|
63	| s=0.15 (L117) | 0.44 | 0.32 [0.20, 0.47] | 0.28 | 0.05 [−0.01, 0.11]^ns | cohens_d_bf16.json / cohens_d_bf16_qwen.json |
64	| s=0.20 (L118) | 0.52 | 1.15 [0.66, 1.26] | 0.55 | 0.21 [0.07, 0.40] | 同上 |
65	| s=0.25 (L119) | 0.68 | 3.97 [2.83, 5.29] | 0.89 | 1.11 [0.61, 1.47] | 同上 |
66	| s=0.30 (L120) | 0.80 | 9.94 [8.39, 16.65] | 1.02 | 2.62 [1.72, 3.65] | 同上 |
67	
68	**注意**：n=500 后 CI 会显著收窄（~√10 倍）。QW s015 的 `^ns` 标注取决于 CI 是否仍含零。
69	
70	### Table: LLaMA cross-arch (tab:llama-cross-arch) — results.tex L83-98
71	
72	**不需直接更新**（LLaMA 实验不重跑），但见 §10 间接影响。
73	
74	### Table: Cross-model comparison (tab:cross-model) — appendix_moved.tex L30-43
75	
76	| 行 | 当前值 | 数据来源 |
77	|----|--------|----------|
78	| DeepSeek s015/s020/s025/s030 | 0.39 / 1.48 / 7.16 / 14.59 | experiment_summary_table.json DS imp |
79	| Qwen s015/s020/s025/s030 | 0.04 / 0.23 / 1.27 / 2.94 | experiment_summary_table.json QW imp |
80	
81	### Table: Permutation test (tab:permutation) — appendix_moved.tex L70-85
82	
83	| s | Observed Δ̃ | 95% CI | p_Bonf | 数据来源 |
84	|---|-----------|--------|--------|----------|
85	| 0.15 | 0.37 | [0.19, 0.62] | 0.0032 | permutation_test_results.json |
86	| 0.20 | 0.97 | [0.69, 1.49] | <0.001 | 同上 |
87	| 0.25 | 3.34 | [1.66, 6.64] | <0.001 | 同上 |
88	| 0.30 | 9.85 | [6.70, 16.29] | <0.001 | 同上 |
89	
90	### Table: Discrimination metrics (tab:discrimination-metrics-full) — appendix_moved.tex L103-123
91	
92	| Model | s | ΔGini | ΔCV | 数据来源 |
93	|-------|---|-------|-----|----------|
94	| DS 0.15 | −0.030 | −0.56 | c4_entropy_deepseek |
95	| DS 0.20 | −0.040 | −0.77 | 同上 |
96	| DS 0.25 | −0.065 | −1.29 | 同上 |
97	| DS 0.30 | −0.081 | −1.66 | 同上 |
98	| QW 0.15 | −0.010 | −0.05 | c4_entropy_qwen |
99	| QW 0.20 | −0.012 | −0.21 | 同上 |
100	| QW 0.25 | −0.010 | −1.49 | 同上 |
101	| QW 0.30 | −0.020 | −1.14 | 同上 |
102	
103	**注意**：C4 entropy 分析需要用 n=500 数据重跑 `analysis/entropy_analysis.py`。
104	
105	### Table: Entropy deltas (tab:entropy-deltas) — appendix_moved.tex L143-163
106	
107	| Model | s | ΔH | 数据来源 |
108	|-------|---|----|----------|
109	| DS 0.15 | −0.040 | c4_entropy_deepseek |
110	| DS 0.20 | −0.047 | 同上 |
111	| DS 0.25 | −0.045 | 同上 |
112	| DS 0.30 | −0.044 | 同上 |
113	| QW 0.15 | −0.073 | c4_entropy_qwen |
114	| QW 0.20 | −0.076 | 同上 |
115	| QW 0.25 | +0.045 | 同上 |
116	| QW 0.30 | −0.007 | 同上 |
117	
118	---
119	
120	## 3. Figures
121	
122	| Figure | 文件 | 数据来源 | 需更新内容 |
123	|--------|------|----------|-----------|
124	| Fig 1 (fig:hero) — fig1_dose_response.pdf | results.tex L55-60 | experiment_summary_table.json G values | G 曲线数据点 + caption 中 `$69{\times}$ to $274{\times}$` |
125	| Fig 2 — fig2_cohens_d (如存在) | 位置待定 | cohens_d_bf16.json, cohens_d_bf16_qwen.json | Cohen's d 森林图 |
126	| Fig 3 (fig:crossover) — fig3_crossover.pdf | appendix_moved.tex L13-18 | experiment_summary_table.json DS s025 | 柱状图数据 + caption 中 `$5.3{\times}$` |
127	| Fig 4 (fig:permtest-forest) — fig4_bootstrap.pdf | appendix_moved.tex L87-92 | permutation_test_results.json | CI 横条 + 点估计值 |
128	| Fig 5 (fig:cross-model) — fig5_crossmodel.pdf | appendix_moved.tex L46-50 | experiment_summary_table.json DS+QW imp | 双曲线数据点 + caption 中 `one-fifth` 比例 |
129	
130	**图表生成脚本**（服务器端）：
131	- `/root/autodl-tmp/pacs/analysis/generate_paper_figures.py` — fig4, fig5
132	- `/root/autodl-tmp/pacs/analysis/generate_summary_table.py` — experiment_summary_table.json
133	- `/root/autodl-tmp/pacs/analysis/cross_model_analysis.py` — cross_model_analysis.json
134	- `/root/autodl-tmp/pacs/analysis/compute_cohens_d.py` — cohens_d_bf16.json
135	
136	**更新流程**：先用 n=500 profiling 数据重跑 `generate_summary_table.py`，再重跑各分析脚本，最后重新生成所有图表 PDF。
137	
138	---
139	
140	## 4. 正文中的内联统计声明
141	
142	### abstract.tex
143	
144	| 行 | 当前文本 | 数据来源 | 类型 |
145	|----|---------|----------|------|
146	| 6 | `50 MATH-500 problems` | — | 文本→500 |
147	| 7 | `from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$` | experiment_summary_table.json DS imp | 数值 |
148	| 7 | `$d_z$ growing from $0.44$ (small) to $0.80$ (large)` | cohens_d_bf16.json | 数值 |
149	| 7 | `$p < 0.005$ at all four sparsity levels` | permutation_test_results.json | 阈值判断 |
150	| 8 | `7/8 conditions` | 重新统计 random PASS/FAIL | 计数 |
151	| 8 | `Qwen $s{=}0.30$, $p{=}0.012$` | QW rand s030 permutation test | 数值 |
152	| 8 | `$d_z{=}{-}0.04$` | QW rand s030 Cohen's d | 数值 |
153	| 9 | `$\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$` | DS imp/rand s025 high-phase medians | 数值 |
154	| 9 | `$\widetilde{\mathrm{II}} = 7.196$ vs.\ $1.363$` | DS imp/rand s025 low-phase medians | 数值 |
155	| 10 | `$d_z \geq 0.55$` | cohens_d_bf16_qwen.json s020 | 阈值 |
156	| 10 | `Spearman $\rho = 1.0$` | cross_model_analysis.json | 数值 |
157	| 10 | `gradient permutation $p = 0.043$` | cross_model_analysis.json | 数值 |
158	| 10 | `${\sim}$1/40 the absolute magnitude` | **间接影响**：LLaMA Δ̃ 不变，DS Δ̃ 变 → 比率需重算 | 比率 |
159	
160	### introduction.tex
161	
162	| 行 | 当前文本 | 数据来源 | 类型 |
163	|----|---------|----------|------|
164	| 14 | `$0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$` | experiment_summary_table.json DS imp | 数值 |
165	| 14 | `$d_z$: $0.44 \to 0.80$` | cohens_d_bf16.json | 数值 |
166	| 14 | `Bonferroni-corrected $p < 0.005$ at all levels` | permutation_test_results.json | 阈值判断 |
167	| 15 | `$d_z \geq 0.55$` | cohens_d_bf16_qwen.json s020 | 阈值 |
168	| 16 | `7/8 conditions non-significant` | 重新统计 random PASS/FAIL | 计数 |
169	
170	### methodology.tex
171	
172	| 行 | 当前文本 | 数据来源 | 类型 |
173	|----|---------|----------|------|
174	| 10 | `50 problems stratified from MATH-500` | — | 文本→500 |
175	| 18 | `mean/median ratios up to 43:1` | 从 n=500 数据重新计算 | 数值 |
176	| 22 | `$p_{\text{Bonf}} < 0.005$ at every sparsity level` | permutation_test_results.json | 阈值判断 |
177	
178	### results.tex (正文段落)
179	
180	| 行 | 当前文本 | 数据来源 | 类型 |
181	|----|---------|----------|------|
182	| 8 | `$0.39$...$14.59$...37× amplification` | 新 Δ_s030 / Δ_s015 需重算 | 数值+比率 |
183	| 13 | `$n{=}50$` | — | 文本→500 |
184	| 29 | `$69{\times}$ at $s{=}0.15$ to $274{\times}$ at $s{=}0.30$` | Table 2 G 列 | 数值 |
185	| 29 | `$0.006$ to $0.053$` | Table 2 II_high 列 min/max | 数值 |
186	| 29 | `$G \approx 0.9$--$1.7{\times}$` | Table 2 random G 列 range | 数值 |
187	| 34 | `50 problems` | — | 文本→500 |
188	| 58 | `$69{\times}$ to $274{\times}$` | Table 2 G range | 数值 |
189	| 66 | `$0.032$ vs.\ $0.818$`...`$7.196$ vs.\ $1.363$---a $5.3{\times}$` | s025 per-phase medians | 数值+比率 |
190	| 71 | `$\Delta$ increases from $0.04$...$2.94$...${\sim}1/5$` | experiment_summary_table.json QW imp | 数值+比率 |
191	| 71 | `$d_z \geq 0.55$; Spearman $\rho = 1.0$; gradient permutation $p = 0.043$` | cross_model_analysis.json | 数值 |
192	| 71 | `$d_z{=}0.28$, CI includes zero` | cohens_d_bf16_qwen.json s015 | 数值+判断 |
193	| 77 | `$0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$` | permutation_test_results.json | 数值 |
194	| 81 | `${\sim}40{\times}$ smaller than DeepSeek and ${\sim}7{\times}$ smaller than Qwen` | **间接影响**：LLaMA Δ̃ 不变，DS/QW Δ̃ 变 → 比率需重算 | 比率 |
195	| 106 | `$d_z{=}0.44$ (small) to $d_z{=}0.80$ (large)` | cohens_d_bf16.json | 数值 |
196	| 106 | `$d_z{=}0.28$...CI includes zero`...`$d_z \geq 0.55$` | cohens_d_bf16_qwen.json | 数值+判断 |
197	| 106 | `$d_z{=}0.89$/$1.02$ vs.\ $0.68$/$0.80$` | cohens_d 两模型对比 | 数值 |
198	
199	### analysis.tex
200	
201	| 行 | 当前文本 | 数据来源 | 类型 |
202	|----|---------|----------|------|
203	| 4 | `$0.030$--$0.081$ (DeepSeek) and $0.010$--$0.020$ (Qwen)` | c4_entropy 分析 ΔGini ranges | 数值 |
204	| 4 | `16 conditions` | 确认是否仍为 16 | 计数 |
205	| 6 | `$\Delta\mathcal{H} \in [-0.047, -0.040]$` | c4_entropy_deepseek entropy deltas | 数值 |
206	| 6 | `$\Delta\mathcal{H} = +0.045$` | c4_entropy_qwen s025 | 数值 |
207	| 6 | `22 of 30 problems` | n=500 后需重算（可能变为 ~220 of 300 等） | 计数 |
208	
209	### discussion.tex
210	
211	| 行 | 当前文本 | 数据来源 | 类型 |
212	|----|---------|----------|------|
213	| 5 | `$69$--$274{\times}$` | Table 2 G range | 数值 |
214	| 5 | `$\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$` | s025 high-phase | 数值 |
215	| 5 | `$7.196$ vs.\ $1.363$` | s025 low-phase | 数值 |
216	| 5 | `$G \approx 1$` | random G（确认仍成立） | 数值 |
217	| 11 | `${\sim}40{\times}$ smaller than DeepSeek, ${\sim}7{\times}$ smaller than Qwen` | **间接影响**：LLaMA Δ̃ 不变，DS/QW Δ̃ 变 → 比率需重算 | 比率 |
218	
219	### conclusion.tex
220	
221	| 行 | 当前文本 | 数据来源 | 类型 |
222	|----|---------|----------|------|
223	| 4 | `$69{\times}$ to $274{\times}$` | Table 2 G range | 数值 |
224	| 4 | `$d_z$: $0.44 \to 0.80$` | cohens_d_bf16.json | 数值 |
225	| 4 | `7/8 conditions non-significant` | random PASS/FAIL 重统计 | 计数 |
226	| 4 | `$d_z \geq 0.55$` | cohens_d_bf16_qwen.json s020 | 阈值 |
227	| 4 | `$\sim$1/40 the magnitude` | **间接影响**：LLaMA Δ̃ 不变，DS Δ̃ 变 → 比率需重算 | 比率 |
228	
229	### appendix.tex
230	
231	| 行 | 当前文本 | 数据来源 | 类型 |
232	|----|---------|----------|------|
233	| 38 | `$G_{\times} = 58$--$241{\times}$` | 乘法 null 下 G range 需重算 | 数值 |
234	
235	### appendix_moved.tex (正文段落)
236	
237	| 行 | 当前文本 | 数据来源 | 类型 |
238	|----|---------|----------|------|
239	| 11 | `$0.032$ vs.\ $0.818$`...`$7.196$ vs.\ $1.363$---a $5.3{\times}$` | s025 per-phase medians | 数值+比率 |
240	| 11 | `$3.9{\times}$...$5.4{\times}$...$5.3{\times}$...$3.6{\times}$` | 各 sparsity level crossover reversal magnitudes | 数值 |
241	| 26 | `Four of the 50 problems are excluded` | QW excluded count n=500 | 计数 |
242	| 53 | `mean $\rho = -0.11$, $p = 0.926$` | cross_model_analysis.json | 数值 |
243	| 56 | `$p = 0.012$...d_z = -0.04` | QW rand s030 | 数值 |
244	| 64 | `mean/median ratios ranging from $1.2{\times}$...$1.6{\times}$` and `$1.1{\times}$ to $1.4{\times}$ for Qwen` | 从 n=500 per-problem diffs 计算 | 数值 |
245	| 66 | `$99.92$th percentile...p_Bonf = 0.0032` | permutation_test_results.json s015 | 数值 |
246	| 68 | `$0.37$...$9.85$...CI lower bound ($0.19 \to 0.69 \to 1.66 \to 6.70$)` | permutation_test_results.json | 数值 |
247	
248	### appendix_disc_analysis.tex (正文段落)
249	
250	| 行 | 当前文本 | 数据来源 | 类型 |
251	|----|---------|----------|------|
252	| 4 | `$-0.031$ to $-0.073$; Qwen: $-0.019$ to $-0.045$` | random eviction Gini 变化 | 数值 |
253	| 11 | `$\widetilde{\mathrm{II}}_{\text{high}} < 0.06$ at $s \leq 0.30$` | Table 2 high-phase range | 数值 |
254	| 11 | `$s = 0.35$, high-phase II rises to $0.105$` | bf16_ds_imp_s035 数据 | 数值 |
255	| 14 | `7/8...Qwen $s{=}0.30$, $p{=}0.012$...$d_z{=}{-}0.04$` | QW rand s030 统计 | 数值 |
256	| 45 | `$n{=}49$...$n{=}46$` | 有效样本量 | 计数 |
257	| 46 | `mean/median ratio ${\sim}1.6{:}1$...mean_diff=22.94, median_diff=14.59` | s030 skewness stats | 数值 |
258	| 47 | CIs: `$[0.19,\; 0.62]$...$[0.69,\; 1.49]$...$[1.66,\; 6.64]$...$[6.70,\; 16.29]$` | permutation_test_results.json | 数值 |
259	| 49 | `$p{=}0.012$...$d_z{=}{-}0.04$...d=-0.035` | QW rand s030 re-bootstrap | 数值 |
260	
261	### appendix_results.tex
262	
263	| 行 | 当前文本 | 数据来源 | 类型 |
264	|----|---------|----------|------|
265	| 7 | `mean $\rho = -0.11$, $p = 0.926$` | cross_model_analysis.json | 数值 |
266	| 10 | `$p = 0.012$...d_z = -0.04` | QW rand s030 | 数值 |
267	| 10 | `3/4 FAIL` (Qwen random) | n=500 后重统计 | 计数 |
268	
269	---
270	
271	## 5. Qwen s015 预注册决策点 (D037/D038)
272	
273	### 当前状态
274	Qwen s015: d_z=0.28, CI=[−0.006, 0.60] → **不显著**，论文采用 "threshold narrative"。
275	
276	### 决策矩阵
277	
278	| n=500 结果 | CI 位置 | 操作 |
279	|-----------|---------|------|
280	| CI 完全 > 0 | 例如 [0.05, 0.35] | **升级**：删除 `^ns` 标注，改叙事为 "effect reliable at all four sparsity levels for both models" |
281	| CI 仍跨零 | 例如 [−0.02, 0.15] | **维持 threshold narrative**：保持当前表述不变，仅更新数值 |
282	
283	### CI 跨零时需更新的叙事位置（仅更新数值，保留 threshold 表述）
284	
285	| 文件 | 行 | 当前叙事 | 操作 |
286	|------|------|---------|------|
287	| abstract.tex | 10 | `replicates on Qwen2.5-7B-Instruct at $s \geq 0.20$` | 更新 d_z 数值，保留 `$s \geq 0.20$` |
288	| introduction.tex | 15 | `$d_z \geq 0.55$` | 更新阈值数值 |
289	| results.tex | 71 | `marginal at $s{=}0.15$ ($d_z{=}0.28$, CI includes zero) but reliable at $s \geq 0.20$ ($d_z \geq 0.55$)` | 更新所有数值 |
290	| results.tex | 117 | `0.28` & `0.05\; $[-0.01, 0.11]$\textsuperscript{ns}` | 更新数值，保留 `^ns` |
291	| results.tex | 122 | `\textsuperscript{ns}Marginal at $s{=}0.15$; reliable at $s \geq 0.20$.` | 保留 |
292	| conclusion.tex | 4 | `$d_z \geq 0.55$` | 更新数值 |
293	
294	### CI > 0 时需更新的叙事位置（升级方案）
295	
296	| 文件 | 行 | 当前叙事 | 备选叙事 |
297	|------|------|---------|----------|
298	| abstract.tex | 10 | `at $s \geq 0.20$` | `at all four sparsity levels` |
299	| introduction.tex | 15 | `$d_z \geq 0.55$` | `$d_z \geq [新s015值]$`（改用 s015 值） |
300	| results.tex | 71 | `marginal at $s{=}0.15$...reliable at $s \geq 0.20$` | `reliable at all four sparsity levels ($d_z \geq [新值]$)` |
301	| results.tex | 117 | `\textsuperscript{ns}` | 删除 `^ns` 标注 |
302	| results.tex | 122 | 脚注 `Marginal at...reliable at...` | 删除或改为 `All levels significant.` |
303	| conclusion.tex | 4 | `$d_z \geq 0.55$` | `$d_z \geq [新s015值]$` |
304	
305	---
306	
307	## 6. 附属统计量（可能变化但方向不变）
308	
309	以下数值的 n=500 版本大概率方向不变，但绝对值会变：
310	
311	| 统计量 | 当前值 | 出现位置 | 预期变化 |
312	|--------|--------|---------|----------|
313	| mean/median ratio | up to 43:1 | methodology.tex L18 | n=500 尾部更极端，可能变大或变小 |
314	| "7/8 conditions" random non-significant | 7/8 | abstract L8, intro L16, conclusion L4, appendix_disc L14 | n=500 CI 更窄，QW rand s030 borderline PASS 可能翻转为 FAIL → 变成 8/8 |
315	| "3/4 FAIL" Qwen random | 3/4 | appendix_results.tex L10 | 同上，可能变为 4/4 |
316	| DS/QW magnitude ratio | ~1/5 | results.tex L71, fig5 caption | 可能略变 |
317	| Crossover reversal magnitudes | 3.9×–5.4× | appendix_moved.tex L11 | 数据驱动，需重算 |
318	| Spearman ρ for monotonicity | 1.0 | abstract L10, results L71 | 4 点排序，大概率仍=1.0 |
319	| Gradient permutation p | 0.043 | abstract L10, results L71 | 4! = 24 种排列，最小 p=1/24≈0.042 |
320	| Per-problem concordance | ρ=−0.11, p=0.926 | appendix_moved L53, appendix_results L7 | n=500 统计功效更高，可能变显著 |
321	
322	---
323	
324	## 7. 数据管道执行顺序
325	
326	1. **等 C2 n=500 全部 16 conditions 完成**（含 DeepSeek 8 + Qwen 8）
327	2. 在服务器执行分析脚本（按依赖顺序）：
328	   ```bash
329	   cd /root/autodl-tmp/pacs
330	   # Step 1: 生成汇总表
331	   python analysis/generate_summary_table.py        # → analysis_output/experiment_summary_table.json
332	
333	   # Step 2: 统计分析（可并行）
334	   python analysis/compute_cohens_d.py               # → analysis_output/cohens_d_bf16.json, cohens_d_bf16_qwen.json
335	   python analysis/cross_model_analysis.py           # → analysis_output/cross_model_analysis.json
336	   python analysis/run_permutation_test.py           # → analysis_output/permutation_test_results.json
337	   python analysis/entropy_analysis.py               # → C4 entropy data (如需更新)
338	
339	   # Step 3: 生成图表
340	   python analysis/generate_paper_figures.py         # → paper_figures/fig1-fig5 PDFs
341	   ```
342	3. 从 JSON 文件提取所有新数值，按本清单 §1-§4 逐项替换
343	4. **关键决策点**：检查 QW s015 Cohen's d CI 是否含零 → 决定 §5 中的叙事方案
344	5. 检查 QW rand s030 是否仍 PASS → 决定 "7/8" vs "8/8"（及 "3/4" vs "4/4"）
345	6. 重新编译 LaTeX 验证 → `pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex`
346	7. 全文搜索残留的旧数值（grep "n=50[^0]"、"0.39"、"14.59" 等）
347	
348	---
349	
350	## 8. 不需更新的部分
351	
352	- **related_work.tex** — 无实验数据
353	- **background.tex** — 公式定义，无实验数据
354	- **limitations.tex** — 无具体实验数值（sparsity range $s \in \{0.15,...,0.30\}$ 不变；LLaMA 描述性文字无需改）
355	- **methodology.tex** 公式/方法部分 — 无变化（仅 n 和统计描述需更新）
356	- **results.tex L83-98** (LLaMA table) — LLaMA 实验不重跑，表内数值不变
357	- **results.tex L79** (LLaMA d_z 0.19→0.34) — 不变
358	- 所有 `\cite{}` 引用 — 无变化
359	
360	---
361	
362	## 9. 更新总量统计
363	
364	| 类别 | 数量 |
365	|------|------|
366	| 样本量文本 "50"→"500" | 8 处 |
367	| 表格（含 8 个表） | ~80 个单元格 |
368	| 图表重新生成 | 5 个 PDF |
369	| 内联统计数值 | ~60 处 |
370	| 条件性叙事更新 (Qwen s015) | 6 处（两套方案） |
371	| 条件性叙事更新 (7/8 vs 8/8) | 5 处 |
372	| LLaMA 间接比率更新 | 4 处（§10） |
373	
374	---
375	
376	## 10. LLaMA 比较性声明间接影响（新增）
377	
378	LLaMA c3_llama 实验不重跑（n=50 不变），但 LLaMA 与 DS/QW 的**比率声明**会因 DS/QW 数值变化而需要重算：
379	
380	| 文件 | 行 | 当前声明 | 需重算内容 |
381	|------|------|---------|-----------|
382	| abstract.tex | 10 | `${\sim}$1/40 the absolute magnitude` | LLaMA s030 Δ̃=0.356 不变；DS s030 Δ̃ 从 n=500 获取 → 重算比率 |
383	| results.tex | 81 | `${\sim}40{\times}$ smaller than DeepSeek and ${\sim}7{\times}$ smaller than Qwen` | DS/QW 新 Δ̃ → 重算两个比率 |
384	| discussion.tex | 11 | `${\sim}40{\times}$ smaller than DeepSeek, ${\sim}7{\times}$ smaller than Qwen` | 同上 |
385	| conclusion.tex | 4 | `$\sim$1/40 the magnitude` | 同 abstract L10 |
386	
387	**计算方法**：LLaMA s030 median Δ̃ = 0.356（不变）。新比率 = 新 DS s030 Δ̃ / 0.356 和 新 QW s030 Δ̃ / 0.356。
388	
389	---
390	
391	## 11. C5b → Future Work 叙事位置追踪（新增）
392	
393	C5b (phase-aware mitigation pilot) 状态 = future_work (D056)。论文中已正确定位为 future work。n=500 不影响 C5b 叙事，但确认以下位置一致性：
394	
395	| 文件 | 行 | 内容 | 状态 |
396	|------|------|------|------|
397	| discussion.tex | 8 | `phase-aware compression budget` 作为 future direction | ✓ 无需改 |
398	| appendix_disc_analysis.tex | 28 | `Scaling experiments are future work.` (REBUTTAL comment) | ✓ 无需改 |
399	| appendix_disc_analysis.tex | 57 | `confirming this is future work` (REBUTTAL comment) | ✓ 无需改 |
400	| appendix_disc_analysis.tex | 62 | `Phase-gated controllers are explicitly scoped as future work` (REBUTTAL comment) | ✓ 无需改 |
401	
402	**如果 n=500 中 mid-phase 数据给 C5b 提供新 evidence**：可在 discussion.tex L8 后插入一句 pilot 结果简述。但这取决于 n=500 分析后的判断，不在机械替换范围内。
403	
404	---
405	
406	## 12. C8 (LLaMA cross-architecture) 限定语检查（新增）
407	
408	C8 状态 = partially_confirmed (D060)。论文中已使用恰当限定语。n=500 不影响 LLaMA 数据，但确认限定语位置：
409	
410	| 文件 | 行 | 限定语 | 状态 |
411	|------|------|--------|------|
412	| abstract.tex | 10 | `suggests cross-architecture generalization, though at ~1/40 magnitude and with substantially weaker interaction` | ✓ 恰当 |
413	| results.tex | 79 | `The qualitative pattern replicates` | ✓ 恰当 |
414	| results.tex | 81 | `qualitatively consistent...though the interaction magnitude is substantially weaker` | ✓ 恰当 |
415	| discussion.tex | 11 | `provides partial support for the qualitative pattern` | ✓ 恰当 |
416	| conclusion.tex | 4 | `qualitatively consistent but substantially weaker trend` | ✓ 恰当 |
417	| limitations.tex | 2 | `directional pattern is qualitatively consistent but the interaction magnitude is substantially weaker` | ✓ 恰当 |
418	
419	**无需修改**，除非 n=500 DS/QW 结果导致比率声明变化（见 §10）。
420	
421	---
422	
423	## 13. 文献完整性检查（新增）
424	
425	### literature_map.yaml 缺口
426	
427	| 缺失论文 | arXiv | 类别 | 为何需要 |
428	|----------|-------|------|---------|
429	| **HIES** | 2510.13832 (Oct 2025) | method-component / supporting evidence | paper_framing.md RC5/RC6 中引用了 HIES 的 importance score collapse 作为 discrimination collapse 的独立佐证。但 HIES 未收录在 literature_map.yaml 中。**需补录。** |
430	
431	### 已有文献完整性确认
432	
433	- **direct-competitor** (3): SparK ✓, GRASPrune ✓, DefensiveKV ✓ — 完整
434	- **phase-aware 单轴** (4): ThinKV ✓, PagedEviction ✓, R-KV ✓, Twilight ✓ — 完整
435	- **compound compression** (4): SLiM ✓, UniComp ✓, compression-ordering ✓, EVICPRESS ✓ — 完整
436	- **phase transition / mechanism** (3): Physics of KV Cache ✓, phase-transition-pruning-thermo ✓, decision-repr-transition ✓ — 完整
437	- **importance fragility** (3): DefensiveKV ✓, greedy-bias ✓, RetentiveKV ✓ — 完整，**但缺 HIES**
438	- **adaptive controllers** (4): Ada-KV ✓, SOL ✓, LKV ✓, LAVa ✓ — 完整
439	- **reasoning dynamics** (2): thinking-tokens-MI ✓, token-budget-aware ✓ — 完整
440	
441	### 近 2 周新论文扫描建议
442	
443	literature_map.yaml 最后扫描日期 2026-05-14。距投稿 2026-05-25 还有 11 天。建议在 Day 9 (2026-05-23) 做最终扫描，重点关注：
444	- arXiv cs.CL + cs.LG 中 "compound sparsity" / "KV cache pruning" / "attention head pruning" 相关
445	- 特别注意 2026-05 新出的 ICML 2026 camera-ready 版本是否有新 compound compression 工作
446	
447	---
448	
449	## 14. 残留旧值清扫 grep 命令（更新后执行）
450	
451	```bash
452	cd /path/to/paper/
453	# 以下命令在所有 .tex 文件完成替换后执行
454	grep -n "n=50[^0]" *.tex           # 应只剩 LLaMA 的 n=49
455	grep -n "\\b0\\.39\\b" *.tex        # 应为 0
456	grep -n "14\\.59" *.tex             # 应为 0
457	grep -n "\\b69\\b" *.tex            # 应为 0（注意排除年份如 2069）
458	grep -n "\\b274\\b" *.tex           # 应为 0
459	grep -n "\\b0\\.44\\b" *.tex        # 应为 0（DS d_z）
460	grep -n "\\b0\\.80\\b" *.tex        # 应为 0（DS d_z）
461	grep -n "7/8" *.tex                 # 应为 0（除非仍为 7/8）
462	```
463	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250",
  "uuid": "adf33332-3419-496e-b05a-9c35f29e1fbb",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/n500_paper_update_checklist.md",
      "content": "# n=500 论文更新清单\n\n> 当 C2 n=500 实验（DeepSeek 8 conditions + Qwen 8 conditions）全部完成后，用此清单逐项替换论文中所有 n=50 数据。\n> 数据来源均在服务器 `/root/autodl-tmp/pacs/analysis_output/` 下。\n> **原则**：DeepSeek 和 Qwen 数值绝对值差 ~5×，不可混用；所有数值精确替换，不可近似。\n> **基于**：`c2_n500_paper_update_checklist.md` 增补 LLaMA 间接影响、文献完整性、C5b/C8 叙事追踪。\n\n---\n\n## 1. 样本量文本替换（全局搜索 \"50\"）\n\n| 文件 | 行号 | 当前文本 | 替换为 | 类型 |\n|------|------|---------|--------|------|\n| abstract.tex | 6 | `50 MATH-500 problems` | `500 MATH-500 problems` | 文本 |\n| methodology.tex | 10 | `50 problems stratified from MATH-500` | `500 problems from MATH-500` | 文本 |\n| results.tex | 13 | `$n{=}50$ MATH-500 problems` (Table 1 caption) | `$n{=}500$` | 文本 |\n| results.tex | 34 | `medians across 50 problems` (Table 2 caption) | `medians across 500 problems` | 文本 |\n| appendix_moved.tex | 26 | `$n{=}46$ valid problems for Qwen (vs.\\ $n{=}49$ for DeepSeek)` | n=500 后的有效样本量（需从数据计算） | 文本 |\n| appendix_moved.tex | 26 | `Four of the 50 problems are excluded` | 新排除数/总数 | 文本 |\n| appendix_moved.tex | 73 | `$n{=}49$, $10{,}000$ permutations` (Table permutation caption) | 新 n 值 | 文本 |\n| appendix_disc_analysis.tex | 45 | `$n{=}49$ paired problems for DeepSeek (1 excluded) and $n{=}46$ for Qwen (4 excluded)` | 新排除数/有效 n | 文本 |\n\n**注意**：results.tex L77/L86 中 LLaMA 的 `$n{=}49$` **不改**（LLaMA 实验仍为 n=50）。\n\n---\n\n## 2. Tables\n\n### Table 1: Aggregate II (tab:aggregate-ii) — results.tex L10-23\n\n| 行/列 | 当前值 | 数据来源 | 更新类型 |\n|--------|--------|----------|----------|\n| Importance s=0.15 | 0.39 | experiment_summary_table.json → DS imp s015 median_diff | 数值替换 |\n| Importance s=0.20 | 1.48 | experiment_summary_table.json → DS imp s020 median_diff | 数值替换 |\n| Importance s=0.25 | 7.16 | experiment_summary_table.json → DS imp s025 median_diff | 数值替换 |\n| Importance s=0.30 | 14.59 | experiment_summary_table.json → DS imp s030 median_diff | 数值替换 |\n| Random s=0.15 | 0.01 | experiment_summary_table.json → DS rand s015 median_diff | 数值替换 |\n| Random s=0.20 | −0.02 | experiment_summary_table.json → DS rand s020 median_diff | 数值替换 |\n| Random s=0.25 | 0.54 | experiment_summary_table.json → DS rand s025 median_diff | 数值替换 |\n| Random s=0.30 | 1.54 | experiment_summary_table.json → DS rand s030 median_diff | 数值替换 |\n| 正文 L8 | `$0.39$...$14.59$...37×` | 同上，37× = 14.59/0.39 需重算 | 数值+比率 |\n| 正文 L8 | `$-0.02$ to $1.54$` | random range 需从新数据取 | 数值替换 |\n\n### Table 2: Per-phase II breakdown (tab:main-results) — results.tex L31-53\n\n| 行 | II_high | II_mid | II_low | Δ | G | 数据来源 |\n|----|---------|--------|--------|---|---|----------|\n| 0.15 Imp | 0.006 | 0.081 | 0.398 | 0.39 | 69 | DS imp s015 per-phase medians |\n| 0.15 Rand | 0.093 | 0.097 | 0.103 | 0.01 | 1.1 | DS rand s015 per-phase medians |\n| 0.20 Imp | 0.015 | 0.203 | 1.496 | 1.48 | 103 | DS imp s020 per-phase medians |\n| 0.20 Rand | 0.292 | 0.350 | 0.276 | −0.02 | 0.9 | DS rand s020 per-phase medians |\n| 0.25 Imp | 0.032 | 1.118 | 7.196 | 7.16 | 222 | DS imp s025 per-phase medians |\n| 0.25 Rand | 0.818 | 0.932 | 1.363 | 0.54 | 1.7 | DS rand s025 per-phase medians |\n| 0.30 Imp | 0.053 | 2.283 | 14.639 | 14.59 | 274 | DS imp s030 per-phase medians |\n| 0.30 Rand | 2.503 | 2.592 | 4.041 | 1.54 | 1.6 | DS rand s030 per-phase medians |\n\n数据来源：`experiment_summary_table.json` 中各 condition 的 `median_low`, `median_mid`, `median_high`。\n\n### Table 3: Cohen's d (tab:cohens-d) — results.tex L108-124\n\n| 行 | DS d_z | DS Δ̃ [CI] | QW d_z | QW Δ̃ [CI] | 数据来源 |\n|----|--------|-----------|--------|-----------|----------|\n| s=0.15 (L117) | 0.44 | 0.32 [0.20, 0.47] | 0.28 | 0.05 [−0.01, 0.11]^ns | cohens_d_bf16.json / cohens_d_bf16_qwen.json |\n| s=0.20 (L118) | 0.52 | 1.15 [0.66, 1.26] | 0.55 | 0.21 [0.07, 0.40] | 同上 |\n| s=0.25 (L119) | 0.68 | 3.97 [2.83, 5.29] | 0.89 | 1.11 [0.61, 1.47] | 同上 |\n| s=0.30 (L120) | 0.80 | 9.94 [8.39, 16.65] | 1.02 | 2.62 [1.72, 3.65] | 同上 |\n\n**注意**：n=500 后 CI 会显著收窄（~√10 倍）。QW s015 的 `^ns` 标注取决于 CI 是否仍含零。\n\n### Table: LLaMA cross-arch (tab:llama-cross-arch) — results.tex L83-98\n\n**不需直接更新**（LLaMA 实验不重跑），但见 §10 间接影响。\n\n### Table: Cross-model comparison (tab:cross-model) — appendix_moved.tex L30-43\n\n| 行 | 当前值 | 数据来源 |\n|----|--------|----------|\n| DeepSeek s015/s020/s025/s030 | 0.39 / 1.48 / 7.16 / 14.59 | experiment_summary_table.json DS imp |\n| Qwen s015/s020/s025/s030 | 0.04 / 0.23 / 1.27 / 2.94 | experiment_summary_table.json QW imp |\n\n### Table: Permutation test (tab:permutation) — appendix_moved.tex L70-85\n\n| s | Observed Δ̃ | 95% CI | p_Bonf | 数据来源 |\n|---|-----------|--------|--------|----------|\n| 0.15 | 0.37 | [0.19, 0.62] | 0.0032 | permutation_test_results.json |\n| 0.20 | 0.97 | [0.69, 1.49] | <0.001 | 同上 |\n| 0.25 | 3.34 | [1.66, 6.64] | <0.001 | 同上 |\n| 0.30 | 9.85 | [6.70, 16.29] | <0.001 | 同上 |\n\n### Table: Discrimination metrics (tab:discrimination-metrics-full) — appendix_moved.tex L103-123\n\n| Model | s | ΔGini | ΔCV | 数据来源 |\n|-------|---|-------|-----|----------|\n| DS 0.15 | −0.030 | −0.56 | c4_entropy_deepseek |\n| DS 0.20 | −0.040 | −0.77 | 同上 |\n| DS 0.25 | −0.065 | −1.29 | 同上 |\n| DS 0.30 | −0.081 | −1.66 | 同上 |\n| QW 0.15 | −0.010 | −0.05 | c4_entropy_qwen |\n| QW 0.20 | −0.012 | −0.21 | 同上 |\n| QW 0.25 | −0.010 | −1.49 | 同上 |\n| QW 0.30 | −0.020 | −1.14 | 同上 |\n\n**注意**：C4 entropy 分析需要用 n=500 数据重跑 `analysis/entropy_analysis.py`。\n\n### Table: Entropy deltas (tab:entropy-deltas) — appendix_moved.tex L143-163\n\n| Model | s | ΔH | 数据来源 |\n|-------|---|----|----------|\n| DS 0.15 | −0.040 | c4_entropy_deepseek |\n| DS 0.20 | −0.047 | 同上 |\n| DS 0.25 | −0.045 | 同上 |\n| DS 0.30 | −0.044 | 同上 |\n| QW 0.15 | −0.073 | c4_entropy_qwen |\n| QW 0.20 | −0.076 | 同上 |\n| QW 0.25 | +0.045 | 同上 |\n| QW 0.30 | −0.007 | 同上 |\n\n---\n\n## 3. Figures\n\n| Figure | 文件 | 数据来源 | 需更新内容 |\n|--------|------|----------|-----------|\n| Fig 1 (fig:hero) — fig1_dose_response.pdf | results.tex L55-60 | experiment_summary_table.json G values | G 曲线数据点 + caption 中 `$69{\\times}$ to $274{\\times}$` |\n| Fig 2 — fig2_cohens_d (如存在) | 位置待定 | cohens_d_bf16.json, cohens_d_bf16_qwen.json | Cohen's d 森林图 |\n| Fig 3 (fig:crossover) — fig3_crossover.pdf | appendix_moved.tex L13-18 | experiment_summary_table.json DS s025 | 柱状图数据 + caption 中 `$5.3{\\times}$` |\n| Fig 4 (fig:permtest-forest) — fig4_bootstrap.pdf | appendix_moved.tex L87-92 | permutation_test_results.json | CI 横条 + 点估计值 |\n| Fig 5 (fig:cross-model) — fig5_crossmodel.pdf | appendix_moved.tex L46-50 | experiment_summary_table.json DS+QW imp | 双曲线数据点 + caption 中 `one-fifth` 比例 |\n\n**图表生成脚本**（服务器端）：\n- `/root/autodl-tmp/pacs/analysis/generate_paper_figures.py` — fig4, fig5\n- `/root/autodl-tmp/pacs/analysis/generate_summary_table.py` — experiment_summary_table.json\n- `/root/autodl-tmp/pacs/analysis/cross_model_analysis.py` — cross_model_analysis.json\n- `/root/autodl-tmp/pacs/analysis/compute_cohens_d.py` — cohens_d_bf16.json\n\n**更新流程**：先用 n=500 profiling 数据重跑 `generate_summary_table.py`，再重跑各分析脚本，最后重新生成所有图表 PDF。\n\n---\n\n## 4. 正文中的内联统计声明\n\n### abstract.tex\n\n| 行 | 当前文本 | 数据来源 | 类型 |\n|----|---------|----------|------|\n| 6 | `50 MATH-500 problems` | — | 文本→500 |\n| 7 | `from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$` | experiment_summary_table.json DS imp | 数值 |\n| 7 | `$d_z$ growing from $0.44$ (small) to $0.80$ (large)` | cohens_d_bf16.json | 数值 |\n| 7 | `$p < 0.005$ at all four sparsity levels` | permutation_test_results.json | 阈值判断 |\n| 8 | `7/8 conditions` | 重新统计 random PASS/FAIL | 计数 |\n| 8 | `Qwen $s{=}0.30$, $p{=}0.012$` | QW rand s030 permutation test | 数值 |\n| 8 | `$d_z{=}{-}0.04$` | QW rand s030 Cohen's d | 数值 |\n| 9 | `$\\widetilde{\\mathrm{II}} = 0.032$ vs.\\ $0.818$` | DS imp/rand s025 high-phase medians | 数值 |\n| 9 | `$\\widetilde{\\mathrm{II}} = 7.196$ vs.\\ $1.363$` | DS imp/rand s025 low-phase medians | 数值 |\n| 10 | `$d_z \\geq 0.55$` | cohens_d_bf16_qwen.json s020 | 阈值 |\n| 10 | `Spearman $\\rho = 1.0$` | cross_model_analysis.json | 数值 |\n| 10 | `gradient permutation $p = 0.043$` | cross_model_analysis.json | 数值 |\n| 10 | `${\\sim}$1/40 the absolute magnitude` | **间接影响**：LLaMA Δ̃ 不变，DS Δ̃ 变 → 比率需重算 | 比率 |\n\n### introduction.tex\n\n| 行 | 当前文本 | 数据来源 | 类型 |\n|----|---------|----------|------|\n| 14 | `$0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$` | experiment_summary_table.json DS imp | 数值 |\n| 14 | `$d_z$: $0.44 \\to 0.80$` | cohens_d_bf16.json | 数值 |\n| 14 | `Bonferroni-corrected $p < 0.005$ at all levels` | permutation_test_results.json | 阈值判断 |\n| 15 | `$d_z \\geq 0.55$` | cohens_d_bf16_qwen.json s020 | 阈值 |\n| 16 | `7/8 conditions non-significant` | 重新统计 random PASS/FAIL | 计数 |\n\n### methodology.tex\n\n| 行 | 当前文本 | 数据来源 | 类型 |\n|----|---------|----------|------|\n| 10 | `50 problems stratified from MATH-500` | — | 文本→500 |\n| 18 | `mean/median ratios up to 43:1` | 从 n=500 数据重新计算 | 数值 |\n| 22 | `$p_{\\text{Bonf}} < 0.005$ at every sparsity level` | permutation_test_results.json | 阈值判断 |\n\n### results.tex (正文段落)\n\n| 行 | 当前文本 | 数据来源 | 类型 |\n|----|---------|----------|------|\n| 8 | `$0.39$...$14.59$...37× amplification` | 新 Δ_s030 / Δ_s015 需重算 | 数值+比率 |\n| 13 | `$n{=}50$` | — | 文本→500 |\n| 29 | `$69{\\times}$ at $s{=}0.15$ to $274{\\times}$ at $s{=}0.30$` | Table 2 G 列 | 数值 |\n| 29 | `$0.006$ to $0.053$` | Table 2 II_high 列 min/max | 数值 |\n| 29 | `$G \\approx 0.9$--$1.7{\\times}$` | Table 2 random G 列 range | 数值 |\n| 34 | `50 problems` | — | 文本→500 |\n| 58 | `$69{\\times}$ to $274{\\times}$` | Table 2 G range | 数值 |\n| 66 | `$0.032$ vs.\\ $0.818$`...`$7.196$ vs.\\ $1.363$---a $5.3{\\times}$` | s025 per-phase medians | 数值+比率 |\n| 71 | `$\\Delta$ increases from $0.04$...$2.94$...${\\sim}1/5$` | experiment_summary_table.json QW imp | 数值+比率 |\n| 71 | `$d_z \\geq 0.55$; Spearman $\\rho = 1.0$; gradient permutation $p = 0.043$` | cross_model_analysis.json | 数值 |\n| 71 | `$d_z{=}0.28$, CI includes zero` | cohens_d_bf16_qwen.json s015 | 数值+判断 |\n| 77 | `$0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$` | permutation_test_results.json | 数值 |\n| 81 | `${\\sim}40{\\times}$ smaller than DeepSeek and ${\\sim}7{\\times}$ smaller than Qwen` | **间接影响**：LLaMA Δ̃ 不变，DS/QW Δ̃ 变 → 比率需重算 | 比率 |\n| 106 | `$d_z{=}0.44$ (small) to $d_z{=}0.80$ (large)` | cohens_d_bf16.json | 数值 |\n| 106 | `$d_z{=}0.28$...CI includes zero`...`$d_z \\geq 0.55$` | cohens_d_bf16_qwen.json | 数值+判断 |\n| 106 | `$d_z{=}0.89$/$1.02$ vs.\\ $0.68$/$0.80$` | cohens_d 两模型对比 | 数值 |\n\n### analysis.tex\n\n| 行 | 当前文本 | 数据来源 | 类型 |\n|----|---------|----------|------|\n| 4 | `$0.030$--$0.081$ (DeepSeek) and $0.010$--$0.020$ (Qwen)` | c4_entropy 分析 ΔGini ranges | 数值 |\n| 4 | `16 conditions` | 确认是否仍为 16 | 计数 |\n| 6 | `$\\Delta\\mathcal{H} \\in [-0.047, -0.040]$` | c4_entropy_deepseek entropy deltas | 数值 |\n| 6 | `$\\Delta\\mathcal{H} = +0.045$` | c4_entropy_qwen s025 | 数值 |\n| 6 | `22 of 30 problems` | n=500 后需重算（可能变为 ~220 of 300 等） | 计数 |\n\n### discussion.tex\n\n| 行 | 当前文本 | 数据来源 | 类型 |\n|----|---------|----------|------|\n| 5 | `$69$--$274{\\times}$` | Table 2 G range | 数值 |\n| 5 | `$\\widetilde{\\mathrm{II}} = 0.032$ vs.\\ $0.818$` | s025 high-phase | 数值 |\n| 5 | `$7.196$ vs.\\ $1.363$` | s025 low-phase | 数值 |\n| 5 | `$G \\approx 1$` | random G（确认仍成立） | 数值 |\n| 11 | `${\\sim}40{\\times}$ smaller than DeepSeek, ${\\sim}7{\\times}$ smaller than Qwen` | **间接影响**：LLaMA Δ̃ 不变，DS/QW Δ̃ 变 → 比率需重算 | 比率 |\n\n### conclusion.tex\n\n| 行 | 当前文本 | 数据来源 | 类型 |\n|----|---------|----------|------|\n| 4 | `$69{\\times}$ to $274{\\times}$` | Table 2 G range | 数值 |\n| 4 | `$d_z$: $0.44 \\to 0.80$` | cohens_d_bf16.json | 数值 |\n| 4 | `7/8 conditions non-significant` | random PASS/FAIL 重统计 | 计数 |\n| 4 | `$d_z \\geq 0.55$` | cohens_d_bf16_qwen.json s020 | 阈值 |\n| 4 | `$\\sim$1/40 the magnitude` | **间接影响**：LLaMA Δ̃ 不变，DS Δ̃ 变 → 比率需重算 | 比率 |\n\n### appendix.tex\n\n| 行 | 当前文本 | 数据来源 | 类型 |\n|----|---------|----------|------|\n| 38 | `$G_{\\times} = 58$--$241{\\times}$` | 乘法 null 下 G range 需重算 | 数值 |\n\n### appendix_moved.tex (正文段落)\n\n| 行 | 当前文本 | 数据来源 | 类型 |\n|----|---------|----------|------|\n| 11 | `$0.032$ vs.\\ $0.818$`...`$7.196$ vs.\\ $1.363$---a $5.3{\\times}$` | s025 per-phase medians | 数值+比率 |\n| 11 | `$3.9{\\times}$...$5.4{\\times}$...$5.3{\\times}$...$3.6{\\times}$` | 各 sparsity level crossover reversal magnitudes | 数值 |\n| 26 | `Four of the 50 problems are excluded` | QW excluded count n=500 | 计数 |\n| 53 | `mean $\\rho = -0.11$, $p = 0.926$` | cross_model_analysis.json | 数值 |\n| 56 | `$p = 0.012$...d_z = -0.04` | QW rand s030 | 数值 |\n| 64 | `mean/median ratios ranging from $1.2{\\times}$...$1.6{\\times}$` and `$1.1{\\times}$ to $1.4{\\times}$ for Qwen` | 从 n=500 per-problem diffs 计算 | 数值 |\n| 66 | `$99.92$th percentile...p_Bonf = 0.0032` | permutation_test_results.json s015 | 数值 |\n| 68 | `$0.37$...$9.85$...CI lower bound ($0.19 \\to 0.69 \\to 1.66 \\to 6.70$)` | permutation_test_results.json | 数值 |\n\n### appendix_disc_analysis.tex (正文段落)\n\n| 行 | 当前文本 | 数据来源 | 类型 |\n|----|---------|----------|------|\n| 4 | `$-0.031$ to $-0.073$; Qwen: $-0.019$ to $-0.045$` | random eviction Gini 变化 | 数值 |\n| 11 | `$\\widetilde{\\mathrm{II}}_{\\text{high}} < 0.06$ at $s \\leq 0.30$` | Table 2 high-phase range | 数值 |\n| 11 | `$s = 0.35$, high-phase II rises to $0.105$` | bf16_ds_imp_s035 数据 | 数值 |\n| 14 | `7/8...Qwen $s{=}0.30$, $p{=}0.012$...$d_z{=}{-}0.04$` | QW rand s030 统计 | 数值 |\n| 45 | `$n{=}49$...$n{=}46$` | 有效样本量 | 计数 |\n| 46 | `mean/median ratio ${\\sim}1.6{:}1$...mean_diff=22.94, median_diff=14.59` | s030 skewness stats | 数值 |\n| 47 | CIs: `$[0.19,\\; 0.62]$...$[0.69,\\; 1.49]$...$[1.66,\\; 6.64]$...$[6.70,\\; 16.29]$` | permutation_test_results.json | 数值 |\n| 49 | `$p{=}0.012$...$d_z{=}{-}0.04$...d=-0.035` | QW rand s030 re-bootstrap | 数值 |\n\n### appendix_results.tex\n\n| 行 | 当前文本 | 数据来源 | 类型 |\n|----|---------|----------|------|\n| 7 | `mean $\\rho = -0.11$, $p = 0.926$` | cross_model_analysis.json | 数值 |\n| 10 | `$p = 0.012$...d_z = -0.04` | QW rand s030 | 数值 |\n| 10 | `3/4 FAIL` (Qwen random) | n=500 后重统计 | 计数 |\n\n---\n\n## 5. Qwen s015 预注册决策点 (D037/D038)\n\n### 当前状态\nQwen s015: d_z=0.28, CI=[−0.006, 0.60] → **不显著**，论文采用 \"threshold narrative\"。\n\n### 决策矩阵\n\n| n=500 结果 | CI 位置 | 操作 |\n|-----------|---------|------|\n| CI 完全 > 0 | 例如 [0.05, 0.35] | **升级**：删除 `^ns` 标注，改叙事为 \"effect reliable at all four sparsity levels for both models\" |\n| CI 仍跨零 | 例如 [−0.02, 0.15] | **维持 threshold narrative**：保持当前表述不变，仅更新数值 |\n\n### CI 跨零时需更新的叙事位置（仅更新数值，保留 threshold 表述）\n\n| 文件 | 行 | 当前叙事 | 操作 |\n|------|------|---------|------|\n| abstract.tex | 10 | `replicates on Qwen2.5-7B-Instruct at $s \\geq 0.20$` | 更新 d_z 数值，保留 `$s \\geq 0.20$` |\n| introduction.tex | 15 | `$d_z \\geq 0.55$` | 更新阈值数值 |\n| results.tex | 71 | `marginal at $s{=}0.15$ ($d_z{=}0.28$, CI includes zero) but reliable at $s \\geq 0.20$ ($d_z \\geq 0.55$)` | 更新所有数值 |\n| results.tex | 117 | `0.28` & `0.05\\; $[-0.01, 0.11]$\\textsuperscript{ns}` | 更新数值，保留 `^ns` |\n| results.tex | 122 | `\\textsuperscript{ns}Marginal at $s{=}0.15$; reliable at $s \\geq 0.20$.` | 保留 |\n| conclusion.tex | 4 | `$d_z \\geq 0.55$` | 更新数值 |\n\n### CI > 0 时需更新的叙事位置（升级方案）\n\n| 文件 | 行 | 当前叙事 | 备选叙事 |\n|------|------|---------|----------|\n| abstract.tex | 10 | `at $s \\geq 0.20$` | `at all four sparsity levels` |\n| introduction.tex | 15 | `$d_z \\geq 0.55$` | `$d_z \\geq [新s015值]$`（改用 s015 值） |\n| results.tex | 71 | `marginal at $s{=}0.15$...reliable at $s \\geq 0.20$` | `reliable at all four sparsity levels ($d_z \\geq [新值]$)` |\n| results.tex | 117 | `\\textsuperscript{ns}` | 删除 `^ns` 标注 |\n| results.tex | 122 | 脚注 `Marginal at...reliable at...` | 删除或改为 `All levels significant.` |\n| conclusion.tex | 4 | `$d_z \\geq 0.55$` | `$d_z \\geq [新s015值]$` |\n\n---\n\n## 6. 附属统计量（可能变化但方向不变）\n\n以下数值的 n=500 版本大概率方向不变，但绝对值会变：\n\n| 统计量 | 当前值 | 出现位置 | 预期变化 |\n|--------|--------|---------|----------|\n| mean/median ratio | up to 43:1 | methodology.tex L18 | n=500 尾部更极端，可能变大或变小 |\n| \"7/8 conditions\" random non-significant | 7/8 | abstract L8, intro L16, conclusion L4, appendix_disc L14 | n=500 CI 更窄，QW rand s030 borderline PASS 可能翻转为 FAIL → 变成 8/8 |\n| \"3/4 FAIL\" Qwen random | 3/4 | appendix_results.tex L10 | 同上，可能变为 4/4 |\n| DS/QW magnitude ratio | ~1/5 | results.tex L71, fig5 caption | 可能略变 |\n| Crossover reversal magnitudes | 3.9×–5.4× | appendix_moved.tex L11 | 数据驱动，需重算 |\n| Spearman ρ for monotonicity | 1.0 | abstract L10, results L71 | 4 点排序，大概率仍=1.0 |\n| Gradient permutation p | 0.043 | abstract L10, results L71 | 4! = 24 种排列，最小 p=1/24≈0.042 |\n| Per-problem concordance | ρ=−0.11, p=0.926 | appendix_moved L53, appendix_results L7 | n=500 统计功效更高，可能变显著 |\n\n---\n\n## 7. 数据管道执行顺序\n\n1. **等 C2 n=500 全部 16 conditions 完成**（含 DeepSeek 8 + Qwen 8）\n2. 在服务器执行分析脚本（按依赖顺序）：\n   ```bash\n   cd /root/autodl-tmp/pacs\n   # Step 1: 生成汇总表\n   python analysis/generate_summary_table.py        # → analysis_output/experiment_summary_table.json\n\n   # Step 2: 统计分析（可并行）\n   python analysis/compute_cohens_d.py               # → analysis_output/cohens_d_bf16.json, cohens_d_bf16_qwen.json\n   python analysis/cross_model_analysis.py           # → analysis_output/cross_model_analysis.json\n   python analysis/run_permutation_test.py           # → analysis_output/permutation_test_results.json\n   python analysis/entropy_analysis.py               # → C4 entropy data (如需更新)\n\n   # Step 3: 生成图表\n   python analysis/generate_paper_figures.py         # → paper_figures/fig1-fig5 PDFs\n   ```\n3. 从 JSON 文件提取所有新数值，按本清单 §1-§4 逐项替换\n4. **关键决策点**：检查 QW s015 Cohen's d CI 是否含零 → 决定 §5 中的叙事方案\n5. 检查 QW rand s030 是否仍 PASS → 决定 \"7/8\" vs \"8/8\"（及 \"3/4\" vs \"4/4\"）\n6. 重新编译 LaTeX 验证 → `pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex`\n7. 全文搜索残留的旧数值（grep \"n=50[^0]\"、\"0.39\"、\"14.59\" 等）\n\n---\n\n## 8. 不需更新的部分\n\n- **related_work.tex** — 无实验数据\n- **background.tex** — 公式定义，无实验数据\n- **limitations.tex** — 无具体实验数值（sparsity range $s \\in \\{0.15,...,0.30\\}$ 不变；LLaMA 描述性文字无需改）\n- **methodology.tex** 公式/方法部分 — 无变化（仅 n 和统计描述需更新）\n- **results.tex L83-98** (LLaMA table) — LLaMA 实验不重跑，表内数值不变\n- **results.tex L79** (LLaMA d_z 0.19→0.34) — 不变\n- 所有 `\\cite{}` 引用 — 无变化\n\n---\n\n## 9. 更新总量统计\n\n| 类别 | 数量 |\n|------|------|\n| 样本量文本 \"50\"→\"500\" | 8 处 |\n| 表格（含 8 个表） | ~80 个单元格 |\n| 图表重新生成 | 5 个 PDF |\n| 内联统计数值 | ~60 处 |\n| 条件性叙事更新 (Qwen s015) | 6 处（两套方案） |\n| 条件性叙事更新 (7/8 vs 8/8) | 5 处 |\n| LLaMA 间接比率更新 | 4 处（§10） |\n\n---\n\n## 10. LLaMA 比较性声明间接影响（新增）\n\nLLaMA c3_llama 实验不重跑（n=50 不变），但 LLaMA 与 DS/QW 的**比率声明**会因 DS/QW 数值变化而需要重算：\n\n| 文件 | 行 | 当前声明 | 需重算内容 |\n|------|------|---------|-----------|\n| abstract.tex | 10 | `${\\sim}$1/40 the absolute magnitude` | LLaMA s030 Δ̃=0.356 不变；DS s030 Δ̃ 从 n=500 获取 → 重算比率 |\n| results.tex | 81 | `${\\sim}40{\\times}$ smaller than DeepSeek and ${\\sim}7{\\times}$ smaller than Qwen` | DS/QW 新 Δ̃ → 重算两个比率 |\n| discussion.tex | 11 | `${\\sim}40{\\times}$ smaller than DeepSeek, ${\\sim}7{\\times}$ smaller than Qwen` | 同上 |\n| conclusion.tex | 4 | `$\\sim$1/40 the magnitude` | 同 abstract L10 |\n\n**计算方法**：LLaMA s030 median Δ̃ = 0.356（不变）。新比率 = 新 DS s030 Δ̃ / 0.356 和 新 QW s030 Δ̃ / 0.356。\n\n---\n\n## 11. C5b → Future Work 叙事位置追踪（新增）\n\nC5b (phase-aware mitigation pilot) 状态 = future_work (D056)。论文中已正确定位为 future work。n=500 不影响 C5b 叙事，但确认以下位置一致性：\n\n| 文件 | 行 | 内容 | 状态 |\n|------|------|------|------|\n| discussion.tex | 8 | `phase-aware compression budget` 作为 future direction | ✓ 无需改 |\n| appendix_disc_analysis.tex | 28 | `Scaling experiments are future work.` (REBUTTAL comment) | ✓ 无需改 |\n| appendix_disc_analysis.tex | 57 | `confirming this is future work` (REBUTTAL comment) | ✓ 无需改 |\n| appendix_disc_analysis.tex | 62 | `Phase-gated controllers are explicitly scoped as future work` (REBUTTAL comment) | ✓ 无需改 |\n\n**如果 n=500 中 mid-phase 数据给 C5b 提供新 evidence**：可在 discussion.tex L8 后插入一句 pilot 结果简述。但这取决于 n=500 分析后的判断，不在机械替换范围内。\n\n---\n\n## 12. C8 (LLaMA cross-architecture) 限定语检查（新增）\n\nC8 状态 = partially_confirmed (D060)。论文中已使用恰当限定语。n=500 不影响 LLaMA 数据，但确认限定语位置：\n\n| 文件 | 行 | 限定语 | 状态 |\n|------|------|--------|------|\n| abstract.tex | 10 | `suggests cross-architecture generalization, though at ~1/40 magnitude and with substantially weaker interaction` | ✓ 恰当 |\n| results.tex | 79 | `The qualitative pattern replicates` | ✓ 恰当 |\n| results.tex | 81 | `qualitatively consistent...though the interaction magnitude is substantially weaker` | ✓ 恰当 |\n| discussion.tex | 11 | `provides partial support for the qualitative pattern` | ✓ 恰当 |\n| conclusion.tex | 4 | `qualitatively consistent but substantially weaker trend` | ✓ 恰当 |\n| limitations.tex | 2 | `directional pattern is qualitatively consistent but the interaction magnitude is substantially weaker` | ✓ 恰当 |\n\n**无需修改**，除非 n=500 DS/QW 结果导致比率声明变化（见 §10）。\n\n---\n\n## 13. 文献完整性检查（新增）\n\n### literature_map.yaml 缺口\n\n| 缺失论文 | arXiv | 类别 | 为何需要 |\n|----------|-------|------|---------|\n| **HIES** | 2510.13832 (Oct 2025) | method-component / supporting evidence | paper_framing.md RC5/RC6 中引用了 HIES 的 importance score collapse 作为 discrimination collapse 的独立佐证。但 HIES 未收录在 literature_map.yaml 中。**需补录。** |\n\n### 已有文献完整性确认\n\n- **direct-competitor** (3): SparK ✓, GRASPrune ✓, DefensiveKV ✓ — 完整\n- **phase-aware 单轴** (4): ThinKV ✓, PagedEviction ✓, R-KV ✓, Twilight ✓ — 完整\n- **compound compression** (4): SLiM ✓, UniComp ✓, compression-ordering ✓, EVICPRESS ✓ — 完整\n- **phase transition / mechanism** (3): Physics of KV Cache ✓, phase-transition-pruning-thermo ✓, decision-repr-transition ✓ — 完整\n- **importance fragility** (3): DefensiveKV ✓, greedy-bias ✓, RetentiveKV ✓ — 完整，**但缺 HIES**\n- **adaptive controllers** (4): Ada-KV ✓, SOL ✓, LKV ✓, LAVa ✓ — 完整\n- **reasoning dynamics** (2): thinking-tokens-MI ✓, token-budget-aware ✓ — 完整\n\n### 近 2 周新论文扫描建议\n\nliterature_map.yaml 最后扫描日期 2026-05-14。距投稿 2026-05-25 还有 11 天。建议在 Day 9 (2026-05-23) 做最终扫描，重点关注：\n- arXiv cs.CL + cs.LG 中 \"compound sparsity\" / \"KV cache pruning\" / \"attention head pruning\" 相关\n- 特别注意 2026-05 新出的 ICML 2026 camera-ready 版本是否有新 compound compression 工作\n\n---\n\n## 14. 残留旧值清扫 grep 命令（更新后执行）\n\n```bash\ncd /path/to/paper/\n# 以下命令在所有 .tex 文件完成替换后执行\ngrep -n \"n=50[^0]\" *.tex           # 应只剩 LLaMA 的 n=49\ngrep -n \"\\\\b0\\\\.39\\\\b\" *.tex        # 应为 0\ngrep -n \"14\\\\.59\" *.tex             # 应为 0\ngrep -n \"\\\\b69\\\\b\" *.tex            # 应为 0（注意排除年份如 2069）\ngrep -n \"\\\\b274\\\\b\" *.tex           # 应为 0\ngrep -n \"\\\\b0\\\\.44\\\\b\" *.tex        # 应为 0（DS d_z）\ngrep -n \"\\\\b0\\\\.80\\\\b\" *.tex        # 应为 0（DS d_z）\ngrep -n \"7/8\" *.tex                 # 应为 0（除非仍为 7/8）\n```\n",
      "numLines": 463,
      "startLine": 1,
      "totalLines": 463
    }
  }
}
````

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Read · `toolu_014uqAgtWNFEUX84MkSrMuoz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250",
  "uuid": "cf40bf82-fcd9-40f3-a4d1-76d82cac92a1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015CLDLsECci42Epf4yqKCcN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4096,
      "cache_read_input_tokens": 23412,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4096
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

_source line 17 · 2026-05-15T01:43:40.425Z_

<details><summary>↩ Tool result · `toolu_014uqAgtWNFEUX84MkSrMuoz`</summary>

```text
1	
2	\section{Results}
3	\label{sec:results}
4	
5	\subsection{Strategy-Dependent Severity}
6	\label{sec:strategy-severity}
7	
8	Table~\ref{tab:aggregate-ii} reports the median compound severity difference across strategies and sparsity levels. Under importance-based eviction, $\Delta$ increases from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$---a $37{\times}$ amplification. Under random eviction, no systematic growth is observed ($-0.02$ to $1.54$), confirming that compound severity depends qualitatively on eviction strategy. % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json
9	
10	\begin{table}[t]
11	\centering
12	\small
13	\caption{Median compound severity difference ($\Delta = \widetilde{\mathrm{II}}_{\textit{low}} - \widetilde{\mathrm{II}}_{\textit{high}}$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}50$ MATH-500 problems).}
14	\label{tab:aggregate-ii}
15	\begin{tabular}{@{}lcccc@{}}
16	\toprule
17	Strategy & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
18	\midrule
19	Importance & 0.39 & 1.48 & 7.16 & 14.59 \\ % exp_id: bf16_importance_s015..s030; source: experiment_summary_table.json median_diff
20	Random     & 0.01 & $-$0.02 & 0.54 & 1.54 \\ % exp_id: bf16_ds_rand_s015..s030; source: experiment_summary_table.json median_diff
21	\bottomrule
22	\end{tabular}
23	\end{table}
24	
25	
26	\subsection{Phase-Modulated Amplification}
27	\label{sec:phase-amplification}
28	
29	Decomposing II by reasoning phase reveals that strategy-dependent severity is driven by amplification in the low-sparsity phase. Table~\ref{tab:main-results} reports the full per-phase breakdown. The severity gradient $G$ increases from $69{\times}$ at $s{=}0.15$ to $274{\times}$ at $s{=}0.30$ under importance-based eviction, while the high-sparsity phase experiences near-zero interaction ($\widetilde{\mathrm{II}}_{\textit{high}}$ ranges from $0.006$ to $0.053$). Under random eviction, $G \approx 0.9$--$1.7{\times}$ at all sparsity levels. Figure~\ref{fig:hero} visualizes this contrast. % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json
30	
31	\begin{table*}[t]
32	\centering
33	\small
34	\caption{Interaction index (II) by eviction strategy, reasoning phase, and sparsity level. II values are problem-level medians across 50 problems. $\Delta = \widetilde{\mathrm{II}}_{\textit{low}} - \widetilde{\mathrm{II}}_{\textit{high}}$. $G = \widetilde{\mathrm{II}}_{\textit{low}} / \widetilde{\mathrm{II}}_{\textit{high}}$.}
35	\label{tab:main-results}
36	\begin{tabular}{@{}llccccr@{}}
37	\toprule
38	$s$ & Strategy & $\widetilde{\mathrm{II}}_{\textit{high}}$ & $\widetilde{\mathrm{II}}_{\textit{mid}}$ & $\widetilde{\mathrm{II}}_{\textit{low}}$ & $\Delta$ & $G$ \\
39	\midrule
40	0.15 & Importance & 0.006 & 0.081 & 0.398 & 0.39 & $\mathbf{69}$ \\
41	0.15 & Random     & 0.093 & 0.097 & 0.103 & 0.01 & 1.1 \\
42	\addlinespace
43	0.20 & Importance & 0.015 & 0.203 & 1.496 & 1.48 & $\mathbf{103}$ \\
44	0.20 & Random     & 0.292 & 0.350 & 0.276 & $-$0.02 & 0.9 \\
45	\addlinespace
46	0.25 & Importance & 0.032 & 1.118 & 7.196 & 7.16 & $\mathbf{222}$ \\
47	0.25 & Random     & 0.818 & 0.932 & 1.363 & 0.54 & 1.7 \\
48	\addlinespace
49	0.30 & Importance & 0.053 & 2.283 & 14.639 & 14.59 & $\mathbf{274}$ \\
50	0.30 & Random     & 2.503 & 2.592 & 4.041 & 1.54 & 1.6 \\
51	\bottomrule
52	\end{tabular}
53	\end{table*}
54	
55	\begin{figure}[t]
56	\centering
57	\includegraphics[width=\columnwidth]{fig1_dose_response.pdf}
58	\caption{Severity gradient ($G$) as a function of sparsity level $s$. Importance-based eviction (solid) exhibits an increasing gradient from $69{\times}$ to $274{\times}$; random eviction (dashed) remains flat near $1{\times}$. Shaded regions: 95\% bootstrap CIs.} % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030
59	\label{fig:hero}
60	\end{figure}
61	
62	
63	\subsection{Phase-Strategy Crossover}
64	\label{sec:crossover}
65	
66	A strategy ranking reversal emerges across all sparsity levels: at $s{=}0.25$, importance-based eviction yields \emph{lower} II than random in the high-sparsity phase ($0.032$ vs.\ $0.818$) but \emph{higher} II in the low-sparsity phase ($7.196$ vs.\ $1.363$---a $5.3{\times}$ reversal), demonstrating that no single strategy dominates uniformly. Full crossover analysis and visualization appear in Appendix~\ref{app:crossover-details}. % exp_id: bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json; 7.196/1.363=5.28
67	
68	\subsection{Cross-Model Replication}
69	\label{sec:cross-model}
70	
71	Qwen2.5-7B-Instruct (standard instruction tuning, same Qwen2 backbone) reproduces the monotonic severity gradient: $\Delta$ increases from $0.04$ at $s{=}0.15$ to $2.94$ at $s{=}0.30$, paralleling DeepSeek at ${\sim}1/5$ the magnitude. Both models yield strictly increasing $d_z$ trajectories (Spearman $\rho = 1.0$; gradient permutation $p = 0.043$). The effect is marginal at $s{=}0.15$ ($d_z{=}0.28$, CI includes zero) but reliable at $s \geq 0.20$ ($d_z \geq 0.55$). A caveat applies to mid-phase comparisons: on Qwen2.5-7B-Instruct, approximately \placeholder{NULL\_PCT}\% of problems yield near-zero Interaction Index in the mid-sparsity phase, where attention patterns exhibit insufficient variation to produce measurable compound interaction. This elevated null rate reduces the effective sample size for mid-phase comparisons; our primary cross-model analysis therefore focuses on the low--high phase contrast ($\Delta$), which is unaffected by this limitation. Per-phase effective sample sizes are reported in Appendix~\ref{app:qwen-null-rate}. Full cross-model tables and figures appear in Appendix~\ref{app:cross-model-details}. % exp_id: cross_model_analysis.json; cohens_d_bf16_qwen.json
72	
73	
74	\subsection{Cross-Architecture Validation}
75	\label{sec:cross-arch}
76	
77	To test whether the phase-modulated severity pattern extends beyond the Qwen2 architecture, we replicate the experiment on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, 8B parameters; $n{=}49$ paired problems). Table~\ref{tab:llama-cross-arch} reports the strategy-dependent severity comparison across sparsity levels.
78	
79	Table~\ref{tab:llama-cross-arch} reports the full results. The evidence for a strategy contrast on LLaMA is mixed: at $s{=}0.15$, the bootstrap CI excludes zero ($[0.002, 0.043]$) but the Bonferroni-corrected Wilcoxon test is non-significant ($p_{\text{Bonf}}{=}0.219$); conversely, at $s{=}0.30$ the CI spans zero ($[-0.069, 0.544]$) while the Wilcoxon test reaches significance ($p_{\text{Bonf}}{=}0.029$). At intermediate levels ($s \in \{0.20, 0.25\}$), neither CI nor Wilcoxon reaches significance. The median paired difference increases monotonically ($\widetilde{\Delta}$: $0.020 \to 0.356$), consistent with a genuine but weak trend---partially confirming the cross-architecture hypothesis while underscoring the substantially weaker interaction on LlamaForCausalLM. % exp_id: c3_llama
80	
81	The absolute magnitude is architecture-dependent: LLaMA severity differences are ${\sim}40{\times}$ smaller than DeepSeek and ${\sim}7{\times}$ smaller than Qwen, and the interaction is substantially weaker---random eviction also shows a non-trivial phase gradient (Wilcoxon $p < \placeholder{}$ at $s{=}0.30$), reducing the strategy contrast observed in Qwen2 models. The directional pattern---importance $>$ random, larger phase gradient under importance---is qualitatively consistent across all three models spanning two architectures (Qwen2ForCausalLM, LlamaForCausalLM), though the interaction magnitude is substantially weaker on LlamaForCausalLM. % exp_id: c3_llama; cross_model_analysis.json
82	
83	\begin{table}[t]
84	\centering
85	\small
86	\caption{Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM). $\widetilde{\Delta}$: median paired difference (importance $-$ random) with bootstrap 95\% CI ($B{=}10{,}000$); $p$: Bonferroni-corrected Wilcoxon signed-rank $p$ ($k{=}4$). $n{=}\placeholder{N\_LLAMA}$ paired problems.}
87	\label{tab:llama-cross-arch}
88	\begin{tabular}{@{}lcc@{}}
89	\toprule
90	$s$ & $\widetilde{\Delta}$\; [95\% CI] & $p_{\text{Bonf}}$ \\
91	\midrule
92	0.15 & \placeholder{}\; $[\placeholder{}, \placeholder{}]$ & \placeholder{} \\
93	0.20 & \placeholder{}\; $[\placeholder{}, \placeholder{}]$ & \placeholder{} \\
94	0.25 & \placeholder{}\; $[\placeholder{}, \placeholder{}]$ & \placeholder{} \\
95	0.30 & \placeholder{}\; $[\placeholder{}, \placeholder{}]$ & $\mathbf{\placeholder{}}$ \\
96	\bottomrule
97	\end{tabular}
98	\end{table}
99	
100	
101	\subsection{Statistical Validation}
102	\label{sec:stat-validation}
103	
104	Paired permutation tests ($10{,}000$ permutations, Bonferroni-corrected) confirm that importance-based eviction produces significantly larger phase-dependent severity than random eviction at all four sparsity levels ($p_{\text{Bonf}} < 0.005$), with observed median differences increasing monotonically from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$. Full permutation test results and forest plot appear in Appendix~\ref{app:permutation-details}. % exp_id: deepseek_bf16_permtest; source: permutation_test_results.json
105	
106	Table~\ref{tab:cohens-d} reports paired Cohen's $d_z$ for both models. For DeepSeek, effect sizes grow from $d_z{=}0.44$ (small) to $d_z{=}0.80$ (large). For Qwen, the effect is marginal at $s{=}0.15$ ($d_z{=}0.28$, CI includes zero), becoming reliable at $s \geq 0.20$ ($d_z \geq 0.55$). At $s \geq 0.25$, Qwen exhibits larger standardized effect sizes ($d_z{=}0.89$/$1.02$ vs.\ $0.68$/$0.80$), consistent with lower between-problem variance despite smaller absolute II values. % exp_id: cohens_d_bf16.json; cohens_d_bf16_qwen.json
107	
108	\begin{table}[t]
109	\centering
110	\small
111	\caption{Paired $d_z$ for phase-dependent II (low $-$ high) under importance-based eviction. Bootstrap 95\% CIs ($B{=}10{,}000$).}
112	\label{tab:cohens-d}
113	\begin{tabular}{@{}lcccc@{}}
114	\toprule
115	$s$ & DS $d_z$ & $\widetilde{\Delta}$ [CI] & QW $d_z$ & $\widetilde{\Delta}$ [CI] \\
116	\midrule
117	0.15 & 0.44 & 0.32\; $[0.20, 0.47]$ & 0.28 & 0.05\; $[-0.01, 0.11]$\textsuperscript{ns} \\ % exp_id: bf16_ds_imp_s015, bf16_qw_imp_s015
118	0.20 & 0.52 & 1.15\; $[0.66, 1.26]$ & 0.55 & 0.21\; $[0.07, 0.40]$ \\ % exp_id: bf16_ds_imp_s020, bf16_qw_imp_s020
119	0.25 & 0.68 & 3.97\; $[2.83, 5.29]$ & 0.89 & 1.11\; $[0.61, 1.47]$ \\ % exp_id: bf16_ds_imp_s025, bf16_qw_imp_s025
120	0.30 & 0.80 & 9.94\; $[8.39, 16.65]$ & 1.02 & 2.62\; $[1.72, 3.65]$ \\ % exp_id: bf16_ds_imp_s030, bf16_qw_imp_s030
121	\bottomrule
122	\multicolumn{5}{@{}l}{\footnotesize \textsuperscript{ns}Marginal at $s{=}0.15$; reliable at $s \geq 0.20$.}
123	\end{tabular}
124	\end{table}
125	
126	We provide a mechanistic analysis in terms of entropy-discrimination collapse in \S\ref{sec:analysis}.
127	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250",
  "uuid": "bc5d199e-5eab-4432-b54d-326e192fa178",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex",
      "content": "\n\\section{Results}\n\\label{sec:results}\n\n\\subsection{Strategy-Dependent Severity}\n\\label{sec:strategy-severity}\n\nTable~\\ref{tab:aggregate-ii} reports the median compound severity difference across strategies and sparsity levels. Under importance-based eviction, $\\Delta$ increases from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$---a $37{\\times}$ amplification. Under random eviction, no systematic growth is observed ($-0.02$ to $1.54$), confirming that compound severity depends qualitatively on eviction strategy. % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Median compound severity difference ($\\Delta = \\widetilde{\\mathrm{II}}_{\\textit{low}} - \\widetilde{\\mathrm{II}}_{\\textit{high}}$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}50$ MATH-500 problems).}\n\\label{tab:aggregate-ii}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nStrategy & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\\\\n\\midrule\nImportance & 0.39 & 1.48 & 7.16 & 14.59 \\\\ % exp_id: bf16_importance_s015..s030; source: experiment_summary_table.json median_diff\nRandom     & 0.01 & $-$0.02 & 0.54 & 1.54 \\\\ % exp_id: bf16_ds_rand_s015..s030; source: experiment_summary_table.json median_diff\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Phase-Modulated Amplification}\n\\label{sec:phase-amplification}\n\nDecomposing II by reasoning phase reveals that strategy-dependent severity is driven by amplification in the low-sparsity phase. Table~\\ref{tab:main-results} reports the full per-phase breakdown. The severity gradient $G$ increases from $69{\\times}$ at $s{=}0.15$ to $274{\\times}$ at $s{=}0.30$ under importance-based eviction, while the high-sparsity phase experiences near-zero interaction ($\\widetilde{\\mathrm{II}}_{\\textit{high}}$ ranges from $0.006$ to $0.053$). Under random eviction, $G \\approx 0.9$--$1.7{\\times}$ at all sparsity levels. Figure~\\ref{fig:hero} visualizes this contrast. % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Interaction index (II) by eviction strategy, reasoning phase, and sparsity level. II values are problem-level medians across 50 problems. $\\Delta = \\widetilde{\\mathrm{II}}_{\\textit{low}} - \\widetilde{\\mathrm{II}}_{\\textit{high}}$. $G = \\widetilde{\\mathrm{II}}_{\\textit{low}} / \\widetilde{\\mathrm{II}}_{\\textit{high}}$.}\n\\label{tab:main-results}\n\\begin{tabular}{@{}llccccr@{}}\n\\toprule\n$s$ & Strategy & $\\widetilde{\\mathrm{II}}_{\\textit{high}}$ & $\\widetilde{\\mathrm{II}}_{\\textit{mid}}$ & $\\widetilde{\\mathrm{II}}_{\\textit{low}}$ & $\\Delta$ & $G$ \\\\\n\\midrule\n0.15 & Importance & 0.006 & 0.081 & 0.398 & 0.39 & $\\mathbf{69}$ \\\\\n0.15 & Random     & 0.093 & 0.097 & 0.103 & 0.01 & 1.1 \\\\\n\\addlinespace\n0.20 & Importance & 0.015 & 0.203 & 1.496 & 1.48 & $\\mathbf{103}$ \\\\\n0.20 & Random     & 0.292 & 0.350 & 0.276 & $-$0.02 & 0.9 \\\\\n\\addlinespace\n0.25 & Importance & 0.032 & 1.118 & 7.196 & 7.16 & $\\mathbf{222}$ \\\\\n0.25 & Random     & 0.818 & 0.932 & 1.363 & 0.54 & 1.7 \\\\\n\\addlinespace\n0.30 & Importance & 0.053 & 2.283 & 14.639 & 14.59 & $\\mathbf{274}$ \\\\\n0.30 & Random     & 2.503 & 2.592 & 4.041 & 1.54 & 1.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig1_dose_response.pdf}\n\\caption{Severity gradient ($G$) as a function of sparsity level $s$. Importance-based eviction (solid) exhibits an increasing gradient from $69{\\times}$ to $274{\\times}$; random eviction (dashed) remains flat near $1{\\times}$. Shaded regions: 95\\% bootstrap CIs.} % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030\n\\label{fig:hero}\n\\end{figure}\n\n\n\\subsection{Phase-Strategy Crossover}\n\\label{sec:crossover}\n\nA strategy ranking reversal emerges across all sparsity levels: at $s{=}0.25$, importance-based eviction yields \\emph{lower} II than random in the high-sparsity phase ($0.032$ vs.\\ $0.818$) but \\emph{higher} II in the low-sparsity phase ($7.196$ vs.\\ $1.363$---a $5.3{\\times}$ reversal), demonstrating that no single strategy dominates uniformly. Full crossover analysis and visualization appear in Appendix~\\ref{app:crossover-details}. % exp_id: bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json; 7.196/1.363=5.28\n\n\\subsection{Cross-Model Replication}\n\\label{sec:cross-model}\n\nQwen2.5-7B-Instruct (standard instruction tuning, same Qwen2 backbone) reproduces the monotonic severity gradient: $\\Delta$ increases from $0.04$ at $s{=}0.15$ to $2.94$ at $s{=}0.30$, paralleling DeepSeek at ${\\sim}1/5$ the magnitude. Both models yield strictly increasing $d_z$ trajectories (Spearman $\\rho = 1.0$; gradient permutation $p = 0.043$). The effect is marginal at $s{=}0.15$ ($d_z{=}0.28$, CI includes zero) but reliable at $s \\geq 0.20$ ($d_z \\geq 0.55$). A caveat applies to mid-phase comparisons: on Qwen2.5-7B-Instruct, approximately \\placeholder{NULL\\_PCT}\\% of problems yield near-zero Interaction Index in the mid-sparsity phase, where attention patterns exhibit insufficient variation to produce measurable compound interaction. This elevated null rate reduces the effective sample size for mid-phase comparisons; our primary cross-model analysis therefore focuses on the low--high phase contrast ($\\Delta$), which is unaffected by this limitation. Per-phase effective sample sizes are reported in Appendix~\\ref{app:qwen-null-rate}. Full cross-model tables and figures appear in Appendix~\\ref{app:cross-model-details}. % exp_id: cross_model_analysis.json; cohens_d_bf16_qwen.json\n\n\n\\subsection{Cross-Architecture Validation}\n\\label{sec:cross-arch}\n\nTo test whether the phase-modulated severity pattern extends beyond the Qwen2 architecture, we replicate the experiment on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, 8B parameters; $n{=}49$ paired problems). Table~\\ref{tab:llama-cross-arch} reports the strategy-dependent severity comparison across sparsity levels.\n\nTable~\\ref{tab:llama-cross-arch} reports the full results. The evidence for a strategy contrast on LLaMA is mixed: at $s{=}0.15$, the bootstrap CI excludes zero ($[0.002, 0.043]$) but the Bonferroni-corrected Wilcoxon test is non-significant ($p_{\\text{Bonf}}{=}0.219$); conversely, at $s{=}0.30$ the CI spans zero ($[-0.069, 0.544]$) while the Wilcoxon test reaches significance ($p_{\\text{Bonf}}{=}0.029$). At intermediate levels ($s \\in \\{0.20, 0.25\\}$), neither CI nor Wilcoxon reaches significance. The median paired difference increases monotonically ($\\widetilde{\\Delta}$: $0.020 \\to 0.356$), consistent with a genuine but weak trend---partially confirming the cross-architecture hypothesis while underscoring the substantially weaker interaction on LlamaForCausalLM. % exp_id: c3_llama\n\nThe absolute magnitude is architecture-dependent: LLaMA severity differences are ${\\sim}40{\\times}$ smaller than DeepSeek and ${\\sim}7{\\times}$ smaller than Qwen, and the interaction is substantially weaker---random eviction also shows a non-trivial phase gradient (Wilcoxon $p < \\placeholder{}$ at $s{=}0.30$), reducing the strategy contrast observed in Qwen2 models. The directional pattern---importance $>$ random, larger phase gradient under importance---is qualitatively consistent across all three models spanning two architectures (Qwen2ForCausalLM, LlamaForCausalLM), though the interaction magnitude is substantially weaker on LlamaForCausalLM. % exp_id: c3_llama; cross_model_analysis.json\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM). $\\widetilde{\\Delta}$: median paired difference (importance $-$ random) with bootstrap 95\\% CI ($B{=}10{,}000$); $p$: Bonferroni-corrected Wilcoxon signed-rank $p$ ($k{=}4$). $n{=}\\placeholder{N\\_LLAMA}$ paired problems.}\n\\label{tab:llama-cross-arch}\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n$s$ & $\\widetilde{\\Delta}$\\; [95\\% CI] & $p_{\\text{Bonf}}$ \\\\\n\\midrule\n0.15 & \\placeholder{}\\; $[\\placeholder{}, \\placeholder{}]$ & \\placeholder{} \\\\\n0.20 & \\placeholder{}\\; $[\\placeholder{}, \\placeholder{}]$ & \\placeholder{} \\\\\n0.25 & \\placeholder{}\\; $[\\placeholder{}, \\placeholder{}]$ & \\placeholder{} \\\\\n0.30 & \\placeholder{}\\; $[\\placeholder{}, \\placeholder{}]$ & $\\mathbf{\\placeholder{}}$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Statistical Validation}\n\\label{sec:stat-validation}\n\nPaired permutation tests ($10{,}000$ permutations, Bonferroni-corrected) confirm that importance-based eviction produces significantly larger phase-dependent severity than random eviction at all four sparsity levels ($p_{\\text{Bonf}} < 0.005$), with observed median differences increasing monotonically from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$. Full permutation test results and forest plot appear in Appendix~\\ref{app:permutation-details}. % exp_id: deepseek_bf16_permtest; source: permutation_test_results.json\n\nTable~\\ref{tab:cohens-d} reports paired Cohen's $d_z$ for both models. For DeepSeek, effect sizes grow from $d_z{=}0.44$ (small) to $d_z{=}0.80$ (large). For Qwen, the effect is marginal at $s{=}0.15$ ($d_z{=}0.28$, CI includes zero), becoming reliable at $s \\geq 0.20$ ($d_z \\geq 0.55$). At $s \\geq 0.25$, Qwen exhibits larger standardized effect sizes ($d_z{=}0.89$/$1.02$ vs.\\ $0.68$/$0.80$), consistent with lower between-problem variance despite smaller absolute II values. % exp_id: cohens_d_bf16.json; cohens_d_bf16_qwen.json\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Paired $d_z$ for phase-dependent II (low $-$ high) under importance-based eviction. Bootstrap 95\\% CIs ($B{=}10{,}000$).}\n\\label{tab:cohens-d}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n$s$ & DS $d_z$ & $\\widetilde{\\Delta}$ [CI] & QW $d_z$ & $\\widetilde{\\Delta}$ [CI] \\\\\n\\midrule\n0.15 & 0.44 & 0.32\\; $[0.20, 0.47]$ & 0.28 & 0.05\\; $[-0.01, 0.11]$\\textsuperscript{ns} \\\\ % exp_id: bf16_ds_imp_s015, bf16_qw_imp_s015\n0.20 & 0.52 & 1.15\\; $[0.66, 1.26]$ & 0.55 & 0.21\\; $[0.07, 0.40]$ \\\\ % exp_id: bf16_ds_imp_s020, bf16_qw_imp_s020\n0.25 & 0.68 & 3.97\\; $[2.83, 5.29]$ & 0.89 & 1.11\\; $[0.61, 1.47]$ \\\\ % exp_id: bf16_ds_imp_s025, bf16_qw_imp_s025\n0.30 & 0.80 & 9.94\\; $[8.39, 16.65]$ & 1.02 & 2.62\\; $[1.72, 3.65]$ \\\\ % exp_id: bf16_ds_imp_s030, bf16_qw_imp_s030\n\\bottomrule\n\\multicolumn{5}{@{}l}{\\footnotesize \\textsuperscript{ns}Marginal at $s{=}0.15$; reliable at $s \\geq 0.20$.}\n\\end{tabular}\n\\end{table}\n\nWe provide a mechanistic analysis in terms of entropy-discrimination collapse in \\S\\ref{sec:analysis}.\n",
      "numLines": 127,
      "startLine": 1,
      "totalLines": 127
    }
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Read · `toolu_01EBK6Y3whEWCeiNi93sGSwH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250",
  "uuid": "12f697e4-2610-484a-87a7-6e19a64531e2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015CLDLsECci42Epf4yqKCcN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4096,
      "cache_read_input_tokens": 23412,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4096
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

_source line 19 · 2026-05-15T01:43:40.673Z_

<details><summary>↩ Tool result · `toolu_01EBK6Y3whEWCeiNi93sGSwH`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Quantitative surprise.}
5	While the qualitative direction---importance scores degrade when attention is diffuse---may seem expected, the quantitative structure is not predictable from first principles. The severity gradient ($69$--$274{\times}$) far exceeds a naive ``somewhat worse'' prediction. The crossover---where importance-based eviction simultaneously outperforms random in high-sparsity phases ($\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$) and underperforms in low-sparsity phases ($7.196$ vs.\ $1.363$)---cannot be derived from single-axis entropy reasoning. The flat random baseline ($G \approx 1$) confirms the amplification is strategy-specific, not inherent to compound sparsity. % exp_id: bf16_importance_s015..s030, bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json
6	
7	\paragraph{Implications for deployment.}
8	Applying a uniform compression budget across all inference steps implicitly accepts order-of-magnitude severity penalties during low-sparsity reasoning phases. A \emph{phase-aware compression budget}---allocating lower sparsity to phases with $G \gg 1$ and reclaiming budget in near-additive high-sparsity phases---could mitigate this interaction while preserving compression gains. The severity gradient provides a natural signal for such allocation. Discrimination collapse depends on attention-mass-based importance scoring shared by major KV cache methods (H$_2$O \cite{h2o-neurips2023}, SnapKV \cite{snapkv-neurips2024}, PyramidKV \cite{pyramidkv-2024}), suggesting broad applicability.
9	
10	A preliminary pilot experiment explored oracle phase-aware budget reallocation, shifting sparsity budget from high-severity low-sparsity phases to low-severity high-sparsity phases. At $s{=}0.25$, oracle recovery---the fraction of compound interaction eliminated by phase-aware allocation---reached \placeholder{ORACLE\_PCT}\% (Wilcoxon $p = \placeholder{ORACLE\_P}$), below the pre-registered 30\% gate for claiming practical mitigation. A heuristic variant achieved \placeholder{HEUR\_PCT}\% recovery ($p = \placeholder{HEUR\_P}$), but 95\% CIs for both conditions span zero. These results indicate that phase-aware budget reallocation alone is insufficient to neutralize the severity gradient; effective mitigation likely requires joint optimization of budget allocation and eviction strategy selection across phases---a promising direction for future work.
11	
12	Extended discussion in Appendix~\ref{app:extended-discussion}.
13	
14	\paragraph{Architecture-dependent magnitude.}
15	Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM) provides partial support for the qualitative pattern---monotonically increasing severity gradient under importance-based eviction with within-strategy phase gradient $d_z \geq 1.0$---while revealing that absolute severity magnitudes are architecture-dependent (${\sim}40{\times}$ smaller than DeepSeek, ${\sim}7{\times}$ smaller than Qwen) and the strategy--phase interaction is substantially weaker than in Qwen2-based architectures. Notably, random pruning also exhibits a non-trivial phase gradient on LLaMA (Wilcoxon $p < \placeholder{}$), reducing the contrast between strategies. This dissociation between qualitatively consistent directional trends and markedly different magnitudes suggests the phase-strategy interaction may be a general property of compound sparsity on reasoning models, while its quantitative impact---and the degree to which it is strategy-specific---depends on architecture-specific attention distributions and head specialization patterns. % exp_id: c3_llama
16	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250",
  "uuid": "14a0ab78-9c88-461e-8c90-114d510cf97b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex",
      "content": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Quantitative surprise.}\nWhile the qualitative direction---importance scores degrade when attention is diffuse---may seem expected, the quantitative structure is not predictable from first principles. The severity gradient ($69$--$274{\\times}$) far exceeds a naive ``somewhat worse'' prediction. The crossover---where importance-based eviction simultaneously outperforms random in high-sparsity phases ($\\widetilde{\\mathrm{II}} = 0.032$ vs.\\ $0.818$) and underperforms in low-sparsity phases ($7.196$ vs.\\ $1.363$)---cannot be derived from single-axis entropy reasoning. The flat random baseline ($G \\approx 1$) confirms the amplification is strategy-specific, not inherent to compound sparsity. % exp_id: bf16_importance_s015..s030, bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json\n\n\\paragraph{Implications for deployment.}\nApplying a uniform compression budget across all inference steps implicitly accepts order-of-magnitude severity penalties during low-sparsity reasoning phases. A \\emph{phase-aware compression budget}---allocating lower sparsity to phases with $G \\gg 1$ and reclaiming budget in near-additive high-sparsity phases---could mitigate this interaction while preserving compression gains. The severity gradient provides a natural signal for such allocation. Discrimination collapse depends on attention-mass-based importance scoring shared by major KV cache methods (H$_2$O \\cite{h2o-neurips2023}, SnapKV \\cite{snapkv-neurips2024}, PyramidKV \\cite{pyramidkv-2024}), suggesting broad applicability.\n\nA preliminary pilot experiment explored oracle phase-aware budget reallocation, shifting sparsity budget from high-severity low-sparsity phases to low-severity high-sparsity phases. At $s{=}0.25$, oracle recovery---the fraction of compound interaction eliminated by phase-aware allocation---reached \\placeholder{ORACLE\\_PCT}\\% (Wilcoxon $p = \\placeholder{ORACLE\\_P}$), below the pre-registered 30\\% gate for claiming practical mitigation. A heuristic variant achieved \\placeholder{HEUR\\_PCT}\\% recovery ($p = \\placeholder{HEUR\\_P}$), but 95\\% CIs for both conditions span zero. These results indicate that phase-aware budget reallocation alone is insufficient to neutralize the severity gradient; effective mitigation likely requires joint optimization of budget allocation and eviction strategy selection across phases---a promising direction for future work.\n\nExtended discussion in Appendix~\\ref{app:extended-discussion}.\n\n\\paragraph{Architecture-dependent magnitude.}\nCross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM) provides partial support for the qualitative pattern---monotonically increasing severity gradient under importance-based eviction with within-strategy phase gradient $d_z \\geq 1.0$---while revealing that absolute severity magnitudes are architecture-dependent (${\\sim}40{\\times}$ smaller than DeepSeek, ${\\sim}7{\\times}$ smaller than Qwen) and the strategy--phase interaction is substantially weaker than in Qwen2-based architectures. Notably, random pruning also exhibits a non-trivial phase gradient on LLaMA (Wilcoxon $p < \\placeholder{}$), reducing the contrast between strategies. This dissociation between qualitatively consistent directional trends and markedly different magnitudes suggests the phase-strategy interaction may be a general property of compound sparsity on reasoning models, while its quantitative impact---and the degree to which it is strategy-specific---depends on architecture-specific attention distributions and head specialization patterns. % exp_id: c3_llama\n",
      "numLines": 16,
      "startLine": 1,
      "totalLines": 16
    }
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Read · `toolu_016Le2ZNShm6CpyvyCf6p87q`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250",
  "uuid": "6b0ba60d-d3a4-4437-a467-e5382d575234",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015CLDLsECci42Epf4yqKCcN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4096,
      "cache_read_input_tokens": 23412,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4096
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

_source line 21 · 2026-05-15T01:43:41.638Z_

<details><summary>↩ Tool result · `toolu_016Le2ZNShm6CpyvyCf6p87q`</summary>

```text
1	\begin{abstract}
2	Compound sparsity---simultaneously pruning attention heads and evicting KV cache entries---is essential for efficient LLM inference but produces super-additive quality degradation whose structure is poorly understood.
3	Prior work treats compound interaction magnitude as approximately constant across the generation process.
4	We show that this assumption is wrong: compound sparsity severity is an emergent phase-strategy interaction that varies by over an order of magnitude across reasoning phases.
5	
6	We evaluate compound sparsity on three models---DeepSeek-R1-Distill-Qwen-7B, Qwen2.5-7B-Instruct (both Qwen2ForCausalLM), and DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM)---spanning two architectures, using 50 MATH-500 problems, measuring the Interaction Index---a super-additivity metric---across quantile-segmented reasoning phases at sparsity levels $s \in \{0.15, 0.20, 0.25, 0.30\}$.
7	Under importance-based KV cache eviction, the median Interaction Index difference between low-sparsity and high-sparsity reasoning phases increases monotonically from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired Cohen's $d_z$ growing from $0.44$ (small) to $0.80$ (large); Bonferroni-corrected permutation tests yield $p < 0.005$ at all four sparsity levels.
8	Random eviction produces no significant phase modulation in 7/8 conditions; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) shows negligible median difference ($\widetilde{\Delta} = \placeholder{}$), confirming that the severity gradient is strategy-specific, not an inherent property of compound sparsity.
9	At $s{=}0.25$, a crossover emerges: importance-based eviction outperforms random in high-sparsity phases ($\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$) yet underperforms in low-sparsity phases ($\widetilde{\mathrm{II}} = 7.196$ vs.\ $1.363$)---a qualitative reversal in strategy ranking.
10	The pattern replicates on Qwen2.5-7B-Instruct at $s \geq 0.20$ ($d_z \geq 0.55$; Spearman $\rho = 1.0$; gradient permutation $p = 0.043$) and on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM), where monotonically increasing median paired differences ($\widetilde{\Delta}$: $0.020 \to 0.356$; $s{=}0.30$ Wilcoxon $p_{\text{Bonf}}{=}0.029$) provide mixed but directionally consistent evidence for cross-architecture generalization, though at ${\sim}$1/40 the absolute magnitude and with substantially weaker interaction than in Qwen2-based architectures. % exp_id: c3_llama
11	
12	We propose entropy-discrimination collapse as an explanatory mechanism: head pruning flattens cumulative importance scores in phases where attention is already broadly distributed, degrading the discriminative power of importance-based eviction in a phase-dependent manner.
13	These findings challenge the phase-invariance assumption in compound sparsity deployment and motivate phase-aware compression budgets for reasoning models.
14	\end{abstract}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250",
  "uuid": "a4db93d3-18d2-48a0-a6b1-d1b33983c6a7",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex",
      "content": "\\begin{abstract}\nCompound sparsity---simultaneously pruning attention heads and evicting KV cache entries---is essential for efficient LLM inference but produces super-additive quality degradation whose structure is poorly understood.\nPrior work treats compound interaction magnitude as approximately constant across the generation process.\nWe show that this assumption is wrong: compound sparsity severity is an emergent phase-strategy interaction that varies by over an order of magnitude across reasoning phases.\n\nWe evaluate compound sparsity on three models---DeepSeek-R1-Distill-Qwen-7B, Qwen2.5-7B-Instruct (both Qwen2ForCausalLM), and DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM)---spanning two architectures, using 50 MATH-500 problems, measuring the Interaction Index---a super-additivity metric---across quantile-segmented reasoning phases at sparsity levels $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$.\nUnder importance-based KV cache eviction, the median Interaction Index difference between low-sparsity and high-sparsity reasoning phases increases monotonically from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired Cohen's $d_z$ growing from $0.44$ (small) to $0.80$ (large); Bonferroni-corrected permutation tests yield $p < 0.005$ at all four sparsity levels.\nRandom eviction produces no significant phase modulation in 7/8 conditions; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) shows negligible median difference ($\\widetilde{\\Delta} = \\placeholder{}$), confirming that the severity gradient is strategy-specific, not an inherent property of compound sparsity.\nAt $s{=}0.25$, a crossover emerges: importance-based eviction outperforms random in high-sparsity phases ($\\widetilde{\\mathrm{II}} = 0.032$ vs.\\ $0.818$) yet underperforms in low-sparsity phases ($\\widetilde{\\mathrm{II}} = 7.196$ vs.\\ $1.363$)---a qualitative reversal in strategy ranking.\nThe pattern replicates on Qwen2.5-7B-Instruct at $s \\geq 0.20$ ($d_z \\geq 0.55$; Spearman $\\rho = 1.0$; gradient permutation $p = 0.043$) and on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM), where monotonically increasing median paired differences ($\\widetilde{\\Delta}$: $0.020 \\to 0.356$; $s{=}0.30$ Wilcoxon $p_{\\text{Bonf}}{=}0.029$) provide mixed but directionally consistent evidence for cross-architecture generalization, though at ${\\sim}$1/40 the absolute magnitude and with substantially weaker interaction than in Qwen2-based architectures. % exp_id: c3_llama\n\nWe propose entropy-discrimination collapse as an explanatory mechanism: head pruning flattens cumulative importance scores in phases where attention is already broadly distributed, degrading the discriminative power of importance-based eviction in a phase-dependent manner.\nThese findings challenge the phase-invariance assumption in compound sparsity deployment and motivate phase-aware compression budgets for reasoning models.\n\\end{abstract}",
      "numLines": 14,
      "startLine": 1,
      "totalLines": 14
    }
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Read · `toolu_018ch5UWAv9k4mL8Q7sfteg9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250",
  "uuid": "cda8a8d6-247b-455d-acad-512c7168f5dd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015CLDLsECci42Epf4yqKCcN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4096,
      "cache_read_input_tokens": 23412,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4096
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

_source line 23 · 2026-05-15T01:43:42.254Z_

<details><summary>↩ Tool result · `toolu_018ch5UWAv9k4mL8Q7sfteg9`</summary>

```text
1	% Content moved from main body to appendix:
2	% - Phase-strategy crossover details (from results §5.3)
3	% - Cross-model replication details with tables/figures (from results §5.4)
4	% - Permutation test details with table/forest plot (from results §5.5)
5	% - Full entropy-discrimination collapse analysis with tables (from analysis §6)
6	% Main body §6 (analysis.tex) contains a condensed summary referencing these tables.
7	
8	\section{Phase-Strategy Crossover Details}
9	\label{app:crossover-details}
10	
11	At $s{=}0.25$, a strategy ranking reversal emerges (Figure~\ref{fig:crossover}): importance-based eviction yields \emph{lower} II than random in the high-sparsity phase ($0.032$ vs.\ $0.818$) but \emph{higher} II in the low-sparsity phase ($7.196$ vs.\ $1.363$---a $5.3{\times}$ reversal). This crossover is present at all four sparsity levels, with reversal magnitude of $3.9{\times}$ at $s{=}0.15$, $5.4{\times}$ at $s{=}0.20$, $5.3{\times}$ at $s{=}0.25$, and $3.6{\times}$ at $s{=}0.30$ (as random eviction severity also rises). The reversal arises because head pruning redistributes attention mass, altering importance rankings in a way that couples the two sparsity mechanisms in low-sparsity phases (\S\ref{sec:discrimination-collapse}). % exp_id: bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json; 7.196/1.363=5.28
12	
13	\begin{figure}[t]
14	\centering
15	\includegraphics[width=\columnwidth]{fig3_crossover.pdf}
16	\caption{Strategy-dependent crossover at $s{=}0.25$. Grouped bar chart of median II by eviction strategy and reasoning phase. Importance-based eviction outperforms random in the high-sparsity phase but produces $5.3{\times}$ higher II in the low-sparsity phase, reversing the strategy ranking.}
17	\label{fig:crossover}
18	\end{figure}
19	
20	
21	\section{Cross-Model Replication Details}
22	\label{app:cross-model-details}
23	
24	Both models share the Qwen2ForCausalLM backbone (28 layers, 28 heads, 4-group GQA) but differ in training: DeepSeek uses reasoning distillation from DeepSeek-R1, while Qwen2.5 uses standard instruction tuning without explicit reasoning delimiters. This controlled comparison isolates the effect of training methodology on the compound sparsity interaction.
25	
26	Despite lacking explicit \texttt{&lt;think>} delimiters, Qwen2.5-7B-Instruct exhibits sufficient variation in attention sparsity to permit phase segmentation via the same quantile-based method (\S\ref{sec:phase-segmentation}). Four of the 50 problems are excluded due to degenerate phase assignments, yielding $n{=}46$ valid problems for Qwen (vs.\ $n{=}49$ for DeepSeek).
27	
28	\paragraph{Per-phase effective sample size.}
29	\label{app:qwen-null-rate}
30	Table~\ref{tab:qwen-effective-n} reports the per-phase effective sample size for Qwen2.5-7B-Instruct, defined as the number of problems with $|\mathrm{II}| > 0.001$ in each phase. The mid-phase null rate (\placeholder{NULL\_PCT}\%) reflects problems where compound interaction is absent in intermediate phases; this does not affect the low--high contrast ($\Delta$) used in the primary analysis.
31	
32	\begin{table}[t]
33	\centering
34	\small
35	\caption{Per-phase effective sample size for Qwen2.5-7B-Instruct ($n_{\text{total}} = \placeholder{N\_QW}$).}
36	\label{tab:qwen-effective-n}
37	\begin{tabular}{@{}lcccc@{}}
38	\toprule
39	Phase & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
40	\midrule
41	High & \placeholder{} & \placeholder{} & \placeholder{} & \placeholder{} \\
42	Mid  & \placeholder{} & \placeholder{} & \placeholder{} & \placeholder{} \\
43	Low  & \placeholder{} & \placeholder{} & \placeholder{} & \placeholder{} \\
44	\bottomrule
45	\end{tabular}
46	\end{table}
47	
48	Table~\ref{tab:cross-model} reports the cross-model comparison. Qwen reproduces the monotonic severity gradient at ${\sim}1/5$ of DeepSeek's magnitude. Figure~\ref{fig:cross-model} visualizes this comparison. % exp_id: cross_model_analysis.json; cohens_d_bf16_qwen.json
49	
50	\begin{table}[t]
51	\centering
52	\small
53	\caption{Cross-model comparison of median compound severity difference ($\Delta$) under importance-based eviction.}
54	\label{tab:cross-model}
55	\begin{tabular}{@{}lcccc@{}}
56	\toprule
57	Model & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
58	\midrule
59	DeepSeek-R1-Distill-Qwen-7B & 0.39 & 1.48 & 7.16 & 14.59 \\ % exp_id: bf16_importance_s015..s030
60	Qwen2.5-7B-Instruct         & 0.04 & 0.23 & 1.27 & 2.94 \\ % exp_id: bf16_qw_imp_s015..s030
61	\bottomrule
62	\end{tabular}
63	\end{table}
64	
65	\begin{figure}[t]
66	\centering
67	\includegraphics[width=\columnwidth]{fig5_crossmodel.pdf}
68	\caption{Cross-model comparison of the median severity difference under importance-based eviction. Both DeepSeek (solid) and Qwen (dashed) exhibit monotonically increasing $\Delta$ with sparsity; Qwen's magnitude is approximately one-fifth of DeepSeek's.} % exp_id: bf16_importance_s015..s030, bf16_qw_imp_s015..s030
69	\label{fig:cross-model}
70	\end{figure}
71	
72	\paragraph{Per-problem concordance.}
73	The per-problem concordance across models is not significant (median $\rho = \placeholder{}$, $p = \placeholder{}$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking. % exp_id: cross_model_analysis.json (spearman_rho=1.0, gradient_permutation_p=0.043, per_problem_concordance_p=0.926, mean_rho=-0.107)
74	
75	\paragraph{Random eviction control.}
76	As a control, random eviction on Qwen yields no systematic phase gradient at three of four sparsity levels (3/4 FAIL), mirroring DeepSeek's 4/4 FAIL pattern. At $s{=}0.30$, Qwen random produces a borderline PASS (permutation $p = 0.012$) but with negligible median difference ($\widetilde{\Delta} = \placeholder{}$, CI spans zero), indicating no meaningful phase modulation. % exp_id: bf16_qw_rand_s015..s030; source: experiment_summary_table.json
77	
78	
79	\section{Permutation Test Details}
80	\label{app:permutation-details}
81	
82	For each problem $i$ and sparsity level $s$, we compute the compound severity difference $\Delta_i^{(\text{strat})} = \mathrm{II}_{\textit{low},i} - \mathrm{II}_{\textit{high},i}$ under each eviction strategy. The test statistic is the median of the paired difference $\widetilde{\Delta} = \text{median}_i\!\bigl(\Delta_i^{(\text{imp})} - \Delta_i^{(\text{rand})}\bigr)$, measuring whether importance-based eviction produces systematically larger phase-dependent severity than random eviction. We permute strategy labels $10{,}000$ times to construct the null distribution and apply Bonferroni correction for 4 sparsity-level comparisons.
83	
84	Per-problem distributions of the paired severity difference $\Delta_i = \mathrm{II}_{\textit{low},i} - \mathrm{II}_{\textit{high},i}$ under importance-based eviction are right-skewed at all sparsity levels, with mean/median ratios ranging from $1.2{\times}$ ($s{=}0.15$) to $1.6{\times}$ ($s{=}0.30$) for DeepSeek and $1.1{\times}$ to $1.4{\times}$ for Qwen.
85	
86	The permutation null distributions are approximately symmetric around zero at all sparsity levels. At $s{=}0.15$, the observed statistic falls at the $99.92$th percentile of the null ($p_{\text{Bonf}} = 0.0032$); at $s \geq 0.20$, no permutation exceeds the observed statistic.
87	
88	Table~\ref{tab:permutation} reports the results. All four sparsity levels reject $H_0$ after Bonferroni correction ($p_{\text{Bonf}} < 0.005$), with observed median differences increasing monotonically from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$. The monotonic growth of both the point estimate and the CI lower bound ($0.19 \to 0.69 \to 1.66 \to 6.70$) confirms that compound severity amplification strengthens with sparsity---not merely in central tendency but also in worst-case lower bounds. Figure~\ref{fig:permtest-forest} presents these results as a forest plot. % exp_id: deepseek_bf16_permtest; source: permutation_test_results.json
89	
90	\begin{table}[t]
91	\centering
92	\small
93	\caption{Paired permutation test for compound severity: importance vs.\ random eviction on DeepSeek-R1-Distill-Qwen-7B ($n{=}49$, $10{,}000$ permutations, Bonferroni-corrected).}
94	\label{tab:permutation}
95	\begin{tabular}{@{}rrcl@{}}
96	\toprule
97	$s$ & Observed $\widetilde{\Delta}$ & 95\% CI & $p_{\text{Bonf}}$ \\
98	\midrule
99	0.15 & 0.37 & $[0.19,\; 0.62]$ & 0.0032 \\ % exp_id: deepseek_bf16_permtest_s015
100	0.20 & 0.97 & $[0.69,\; 1.49]$ & ${<}\,0.001$ \\ % exp_id: deepseek_bf16_permtest_s020
101	0.25 & 3.34 & $[1.66,\; 6.64]$ & ${<}\,0.001$ \\ % exp_id: deepseek_bf16_permtest_s025
102	0.30 & 9.85 & $[6.70,\; 16.29]$ & ${<}\,0.001$ \\ % exp_id: deepseek_bf16_permtest_s030
103	\bottomrule
104	\end{tabular}
105	\end{table}
106	
107	\begin{figure}[t]
108	\centering
109	\includegraphics[width=\columnwidth]{fig4_bootstrap.pdf}
110	\caption{Forest plot of permutation test results. Horizontal bars show 95\% permutation CIs; diamonds mark observed median differences $\widetilde{\Delta}$. All CIs lie entirely above zero, confirming significant strategy-dependent severity at every sparsity level.}
111	\label{fig:permtest-forest}
112	\end{figure}
113	
114	
115	\section{Analysis: Entropy-Discrimination Collapse}
116	\label{app:analysis}
117	
118	\subsection{Discrimination Collapse}
119	\label{sec:discrimination-collapse}
120	
121	Head pruning reduces the number of heads contributing to cumulative importance scores, flattening the score distribution. Table~\ref{tab:discrimination-metrics-full} quantifies this effect: the Gini coefficient decreases by $0.030$--$0.081$ (DeepSeek) and $0.010$--$0.020$ (Qwen) after pruning, with consistent negative deltas across all 16 conditions (both models $\times$ 4 sparsity levels $\times$ 2 strategies). The CV delta is likewise negative in all 8 importance-based conditions. The same pattern holds under random eviction, confirming that discrimination collapse is a consequence of head pruning \emph{per se}, not of the eviction strategy. % exp_id: c4_entropy_deepseek, c4_entropy_qwen
122	
123	\begin{table}[t]
124	\centering
125	\caption{Discrimination collapse under importance-based eviction. $\Delta\mathrm{Gini}$ and $\Delta\mathrm{CV}$ are post-pruning minus baseline; negative values indicate reduced discriminative power.}
126	\label{tab:discrimination-metrics-full}
127	\small
128	\begin{tabular}{llrr}
129	\toprule
130	Model & $s$ & $\Delta\mathrm{Gini}$ & $\Delta\mathrm{CV}$ \\
131	\midrule
132	DeepSeek & $0.15$ & $-0.030$ & $-0.56$ \\
133	DeepSeek & $0.20$ & $-0.040$ & $-0.77$ \\
134	DeepSeek & $0.25$ & $-0.065$ & $-1.29$ \\
135	DeepSeek & $0.30$ & $-0.081$ & $-1.66$ \\
136	\midrule
137	Qwen & $0.15$ & $-0.010$ & $-0.05$ \\
138	Qwen & $0.20$ & $-0.012$ & $-0.21$ \\
139	Qwen & $0.25$ & $-0.010$ & $-1.49$ \\
140	Qwen & $0.30$ & $-0.020$ & $-1.14$ \\
141	\bottomrule
142	\end{tabular}
143	\end{table}
144	
145	When importance scores lose discriminability, thresholding degenerates into noise-sensitive selection---functionally approaching biased random eviction. This is phase-dependent: in low-sparsity phases, attention is already broadly distributed, so pruning-induced flattening has maximum impact; in high-sparsity phases, concentration is preserved. Random eviction is immune because its decisions are independent of score quality, explaining $G \approx 1$. % exp_id: c4_entropy_deepseek, c4_entropy_qwen
146	
147	\subsection{Entropy Redistribution}
148	\label{sec:entropy-redistribution}
149	
150	Beyond discrimination collapse, we examine whether head pruning also redistributes the attention entropy of surviving heads. We measure the mean attention entropy per head:
151	\begin{equation}
152	    \mathcal{H}_i^{(h)} = -\sum_{j=1}^{T} a_{ij}^{(h)} \log a_{ij}^{(h)}
153	    \label{eq:attn-entropy}
154	\end{equation}
155	and compute $\Delta\mathcal{H}$ as the change from baseline (no pruning) to the pruned condition.
156	
157	For DeepSeek under importance-based eviction, the entropy delta is consistently negative across all four sparsity levels ($\Delta\mathcal{H} \in [-0.047, -0.040]$; Table~\ref{tab:entropy-deltas}), indicating that importance-based pruning systematically selects heads whose removal concentrates attention in the surviving heads, reinforcing discrimination collapse. % exp_id: c4_entropy_deepseek
158	
159	For Qwen, the entropy pattern only partially replicates. The delta is negative at $s{=}0.15$ ($\Delta\mathcal{H} = -0.073$) and $s{=}0.20$ ($-0.076$), consistent with DeepSeek. However, at $s{=}0.25$, the delta reverses to $+0.045$, with 22 of 30 problems showing positive entropy change. At $s{=}0.30$, the delta is near zero ($-0.007$). The $s{=}0.25$ reversal is systematic rather than a statistical artifact: it is consistent across all three reasoning phases (low: $+0.042$, mid: $+0.034$, high: $+0.017$). We interpret this as a genuine model-specific difference, possibly arising from distinct head specialization patterns: Qwen's instruction tuning (vs.\ DeepSeek's distillation-based training) may produce head configurations where removing 25\% of heads triggers compensatory broadening rather than concentration. % exp_id: c4_entropy_qwen
160	
161	We characterize discrimination collapse as the robust, model-independent driver of the phase-strategy interaction, with entropy redistribution as a secondary amplifier that is consistent in DeepSeek but model-dependent in Qwen.
162	
163	\begin{table}[t]
164	\centering
165	\caption{Attention entropy deltas ($\Delta\mathcal{H}$) under importance-based eviction. DeepSeek shows consistent entropy compression; Qwen partially replicates with a reversal at $s{=}0.25$.}
166	\label{tab:entropy-deltas}
167	\small
168	\begin{tabular}{llr}
169	\toprule
170	Model & $s$ & $\Delta\mathcal{H}$ \\
171	\midrule
172	DeepSeek & $0.15$ & $-0.040$ \\
173	DeepSeek & $0.20$ & $-0.047$ \\
174	DeepSeek & $0.25$ & $-0.045$ \\
175	DeepSeek & $0.30$ & $-0.044$ \\
176	\midrule
177	Qwen & $0.15$ & $-0.073$ \\
178	Qwen & $0.20$ & $-0.076$ \\
179	Qwen & $0.25$ & $+0.045$ \\
180	Qwen & $0.30$ & $-0.007$ \\
181	\bottomrule
182	\end{tabular}
183	\end{table}
184	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250",
  "uuid": "7c638ea0-8a70-4be8-bce5-87787008efd1",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex",
      "content": "% Content moved from main body to appendix:\n% - Phase-strategy crossover details (from results §5.3)\n% - Cross-model replication details with tables/figures (from results §5.4)\n% - Permutation test details with table/forest plot (from results §5.5)\n% - Full entropy-discrimination collapse analysis with tables (from analysis §6)\n% Main body §6 (analysis.tex) contains a condensed summary referencing these tables.\n\n\\section{Phase-Strategy Crossover Details}\n\\label{app:crossover-details}\n\nAt $s{=}0.25$, a strategy ranking reversal emerges (Figure~\\ref{fig:crossover}): importance-based eviction yields \\emph{lower} II than random in the high-sparsity phase ($0.032$ vs.\\ $0.818$) but \\emph{higher} II in the low-sparsity phase ($7.196$ vs.\\ $1.363$---a $5.3{\\times}$ reversal). This crossover is present at all four sparsity levels, with reversal magnitude of $3.9{\\times}$ at $s{=}0.15$, $5.4{\\times}$ at $s{=}0.20$, $5.3{\\times}$ at $s{=}0.25$, and $3.6{\\times}$ at $s{=}0.30$ (as random eviction severity also rises). The reversal arises because head pruning redistributes attention mass, altering importance rankings in a way that couples the two sparsity mechanisms in low-sparsity phases (\\S\\ref{sec:discrimination-collapse}). % exp_id: bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json; 7.196/1.363=5.28\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig3_crossover.pdf}\n\\caption{Strategy-dependent crossover at $s{=}0.25$. Grouped bar chart of median II by eviction strategy and reasoning phase. Importance-based eviction outperforms random in the high-sparsity phase but produces $5.3{\\times}$ higher II in the low-sparsity phase, reversing the strategy ranking.}\n\\label{fig:crossover}\n\\end{figure}\n\n\n\\section{Cross-Model Replication Details}\n\\label{app:cross-model-details}\n\nBoth models share the Qwen2ForCausalLM backbone (28 layers, 28 heads, 4-group GQA) but differ in training: DeepSeek uses reasoning distillation from DeepSeek-R1, while Qwen2.5 uses standard instruction tuning without explicit reasoning delimiters. This controlled comparison isolates the effect of training methodology on the compound sparsity interaction.\n\nDespite lacking explicit \\texttt{&lt;think>} delimiters, Qwen2.5-7B-Instruct exhibits sufficient variation in attention sparsity to permit phase segmentation via the same quantile-based method (\\S\\ref{sec:phase-segmentation}). Four of the 50 problems are excluded due to degenerate phase assignments, yielding $n{=}46$ valid problems for Qwen (vs.\\ $n{=}49$ for DeepSeek).\n\n\\paragraph{Per-phase effective sample size.}\n\\label{app:qwen-null-rate}\nTable~\\ref{tab:qwen-effective-n} reports the per-phase effective sample size for Qwen2.5-7B-Instruct, defined as the number of problems with $|\\mathrm{II}| > 0.001$ in each phase. The mid-phase null rate (\\placeholder{NULL\\_PCT}\\%) reflects problems where compound interaction is absent in intermediate phases; this does not affect the low--high contrast ($\\Delta$) used in the primary analysis.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Per-phase effective sample size for Qwen2.5-7B-Instruct ($n_{\\text{total}} = \\placeholder{N\\_QW}$).}\n\\label{tab:qwen-effective-n}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nPhase & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\\\\n\\midrule\nHigh & \\placeholder{} & \\placeholder{} & \\placeholder{} & \\placeholder{} \\\\\nMid  & \\placeholder{} & \\placeholder{} & \\placeholder{} & \\placeholder{} \\\\\nLow  & \\placeholder{} & \\placeholder{} & \\placeholder{} & \\placeholder{} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:cross-model} reports the cross-model comparison. Qwen reproduces the monotonic severity gradient at ${\\sim}1/5$ of DeepSeek's magnitude. Figure~\\ref{fig:cross-model} visualizes this comparison. % exp_id: cross_model_analysis.json; cohens_d_bf16_qwen.json\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-model comparison of median compound severity difference ($\\Delta$) under importance-based eviction.}\n\\label{tab:cross-model}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nModel & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\\\\n\\midrule\nDeepSeek-R1-Distill-Qwen-7B & 0.39 & 1.48 & 7.16 & 14.59 \\\\ % exp_id: bf16_importance_s015..s030\nQwen2.5-7B-Instruct         & 0.04 & 0.23 & 1.27 & 2.94 \\\\ % exp_id: bf16_qw_imp_s015..s030\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig5_crossmodel.pdf}\n\\caption{Cross-model comparison of the median severity difference under importance-based eviction. Both DeepSeek (solid) and Qwen (dashed) exhibit monotonically increasing $\\Delta$ with sparsity; Qwen's magnitude is approximately one-fifth of DeepSeek's.} % exp_id: bf16_importance_s015..s030, bf16_qw_imp_s015..s030\n\\label{fig:cross-model}\n\\end{figure}\n\n\\paragraph{Per-problem concordance.}\nThe per-problem concordance across models is not significant (median $\\rho = \\placeholder{}$, $p = \\placeholder{}$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking. % exp_id: cross_model_analysis.json (spearman_rho=1.0, gradient_permutation_p=0.043, per_problem_concordance_p=0.926, mean_rho=-0.107)\n\n\\paragraph{Random eviction control.}\nAs a control, random eviction on Qwen yields no systematic phase gradient at three of four sparsity levels (3/4 FAIL), mirroring DeepSeek's 4/4 FAIL pattern. At $s{=}0.30$, Qwen random produces a borderline PASS (permutation $p = 0.012$) but with negligible median difference ($\\widetilde{\\Delta} = \\placeholder{}$, CI spans zero), indicating no meaningful phase modulation. % exp_id: bf16_qw_rand_s015..s030; source: experiment_summary_table.json\n\n\n\\section{Permutation Test Details}\n\\label{app:permutation-details}\n\nFor each problem $i$ and sparsity level $s$, we compute the compound severity difference $\\Delta_i^{(\\text{strat})} = \\mathrm{II}_{\\textit{low},i} - \\mathrm{II}_{\\textit{high},i}$ under each eviction strategy. The test statistic is the median of the paired difference $\\widetilde{\\Delta} = \\text{median}_i\\!\\bigl(\\Delta_i^{(\\text{imp})} - \\Delta_i^{(\\text{rand})}\\bigr)$, measuring whether importance-based eviction produces systematically larger phase-dependent severity than random eviction. We permute strategy labels $10{,}000$ times to construct the null distribution and apply Bonferroni correction for 4 sparsity-level comparisons.\n\nPer-problem distributions of the paired severity difference $\\Delta_i = \\mathrm{II}_{\\textit{low},i} - \\mathrm{II}_{\\textit{high},i}$ under importance-based eviction are right-skewed at all sparsity levels, with mean/median ratios ranging from $1.2{\\times}$ ($s{=}0.15$) to $1.6{\\times}$ ($s{=}0.30$) for DeepSeek and $1.1{\\times}$ to $1.4{\\times}$ for Qwen.\n\nThe permutation null distributions are approximately symmetric around zero at all sparsity levels. At $s{=}0.15$, the observed statistic falls at the $99.92$th percentile of the null ($p_{\\text{Bonf}} = 0.0032$); at $s \\geq 0.20$, no permutation exceeds the observed statistic.\n\nTable~\\ref{tab:permutation} reports the results. All four sparsity levels reject $H_0$ after Bonferroni correction ($p_{\\text{Bonf}} < 0.005$), with observed median differences increasing monotonically from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$. The monotonic growth of both the point estimate and the CI lower bound ($0.19 \\to 0.69 \\to 1.66 \\to 6.70$) confirms that compound severity amplification strengthens with sparsity---not merely in central tendency but also in worst-case lower bounds. Figure~\\ref{fig:permtest-forest} presents these results as a forest plot. % exp_id: deepseek_bf16_permtest; source: permutation_test_results.json\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Paired permutation test for compound severity: importance vs.\\ random eviction on DeepSeek-R1-Distill-Qwen-7B ($n{=}49$, $10{,}000$ permutations, Bonferroni-corrected).}\n\\label{tab:permutation}\n\\begin{tabular}{@{}rrcl@{}}\n\\toprule\n$s$ & Observed $\\widetilde{\\Delta}$ & 95\\% CI & $p_{\\text{Bonf}}$ \\\\\n\\midrule\n0.15 & 0.37 & $[0.19,\\; 0.62]$ & 0.0032 \\\\ % exp_id: deepseek_bf16_permtest_s015\n0.20 & 0.97 & $[0.69,\\; 1.49]$ & ${<}\\,0.001$ \\\\ % exp_id: deepseek_bf16_permtest_s020\n0.25 & 3.34 & $[1.66,\\; 6.64]$ & ${<}\\,0.001$ \\\\ % exp_id: deepseek_bf16_permtest_s025\n0.30 & 9.85 & $[6.70,\\; 16.29]$ & ${<}\\,0.001$ \\\\ % exp_id: deepseek_bf16_permtest_s030\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig4_bootstrap.pdf}\n\\caption{Forest plot of permutation test results. Horizontal bars show 95\\% permutation CIs; diamonds mark observed median differences $\\widetilde{\\Delta}$. All CIs lie entirely above zero, confirming significant strategy-dependent severity at every sparsity level.}\n\\label{fig:permtest-forest}\n\\end{figure}\n\n\n\\section{Analysis: Entropy-Discrimination Collapse}\n\\label{app:analysis}\n\n\\subsection{Discrimination Collapse}\n\\label{sec:discrimination-collapse}\n\nHead pruning reduces the number of heads contributing to cumulative importance scores, flattening the score distribution. Table~\\ref{tab:discrimination-metrics-full} quantifies this effect: the Gini coefficient decreases by $0.030$--$0.081$ (DeepSeek) and $0.010$--$0.020$ (Qwen) after pruning, with consistent negative deltas across all 16 conditions (both models $\\times$ 4 sparsity levels $\\times$ 2 strategies). The CV delta is likewise negative in all 8 importance-based conditions. The same pattern holds under random eviction, confirming that discrimination collapse is a consequence of head pruning \\emph{per se}, not of the eviction strategy. % exp_id: c4_entropy_deepseek, c4_entropy_qwen\n\n\\begin{table}[t]\n\\centering\n\\caption{Discrimination collapse under importance-based eviction. $\\Delta\\mathrm{Gini}$ and $\\Delta\\mathrm{CV}$ are post-pruning minus baseline; negative values indicate reduced discriminative power.}\n\\label{tab:discrimination-metrics-full}\n\\small\n\\begin{tabular}{llrr}\n\\toprule\nModel & $s$ & $\\Delta\\mathrm{Gini}$ & $\\Delta\\mathrm{CV}$ \\\\\n\\midrule\nDeepSeek & $0.15$ & $-0.030$ & $-0.56$ \\\\\nDeepSeek & $0.20$ & $-0.040$ & $-0.77$ \\\\\nDeepSeek & $0.25$ & $-0.065$ & $-1.29$ \\\\\nDeepSeek & $0.30$ & $-0.081$ & $-1.66$ \\\\\n\\midrule\nQwen & $0.15$ & $-0.010$ & $-0.05$ \\\\\nQwen & $0.20$ & $-0.012$ & $-0.21$ \\\\\nQwen & $0.25$ & $-0.010$ & $-1.49$ \\\\\nQwen & $0.30$ & $-0.020$ & $-1.14$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWhen importance scores lose discriminability, thresholding degenerates into noise-sensitive selection---functionally approaching biased random eviction. This is phase-dependent: in low-sparsity phases, attention is already broadly distributed, so pruning-induced flattening has maximum impact; in high-sparsity phases, concentration is preserved. Random eviction is immune because its decisions are independent of score quality, explaining $G \\approx 1$. % exp_id: c4_entropy_deepseek, c4_entropy_qwen\n\n\\subsection{Entropy Redistribution}\n\\label{sec:entropy-redistribution}\n\nBeyond discrimination collapse, we examine whether head pruning also redistributes the attention entropy of surviving heads. We measure the mean attention entropy per head:\n\\begin{equation}\n    \\mathcal{H}_i^{(h)} = -\\sum_{j=1}^{T} a_{ij}^{(h)} \\log a_{ij}^{(h)}\n    \\label{eq:attn-entropy}\n\\end{equation}\nand compute $\\Delta\\mathcal{H}$ as the change from baseline (no pruning) to the pruned condition.\n\nFor DeepSeek under importance-based eviction, the entropy delta is consistently negative across all four sparsity levels ($\\Delta\\mathcal{H} \\in [-0.047, -0.040]$; Table~\\ref{tab:entropy-deltas}), indicating that importance-based pruning systematically selects heads whose removal concentrates attention in the surviving heads, reinforcing discrimination collapse. % exp_id: c4_entropy_deepseek\n\nFor Qwen, the entropy pattern only partially replicates. The delta is negative at $s{=}0.15$ ($\\Delta\\mathcal{H} = -0.073$) and $s{=}0.20$ ($-0.076$), consistent with DeepSeek. However, at $s{=}0.25$, the delta reverses to $+0.045$, with 22 of 30 problems showing positive entropy change. At $s{=}0.30$, the delta is near zero ($-0.007$). The $s{=}0.25$ reversal is systematic rather than a statistical artifact: it is consistent across all three reasoning phases (low: $+0.042$, mid: $+0.034$, high: $+0.017$). We interpret this as a genuine model-specific difference, possibly arising from distinct head specialization patterns: Qwen's instruction tuning (vs.\\ DeepSeek's distillation-based training) may produce head configurations where removing 25\\% of heads triggers compensatory broadening rather than concentration. % exp_id: c4_entropy_qwen\n\nWe characterize discrimination collapse as the robust, model-independent driver of the phase-strategy interaction, with entropy redistribution as a secondary amplifier that is consistent in DeepSeek but model-dependent in Qwen.\n\n\\begin{table}[t]\n\\centering\n\\caption{Attention entropy deltas ($\\Delta\\mathcal{H}$) under importance-based eviction. DeepSeek shows consistent entropy compression; Qwen partially replicates with a reversal at $s{=}0.25$.}\n\\label{tab:entropy-deltas}\n\\small\n\\begin{tabular}{llr}\n\\toprule\nModel & $s$ & $\\Delta\\mathcal{H}$ \\\\\n\\midrule\nDeepSeek & $0.15$ & $-0.040$ \\\\\nDeepSeek & $0.20$ & $-0.047$ \\\\\nDeepSeek & $0.25$ & $-0.045$ \\\\\nDeepSeek & $0.30$ & $-0.044$ \\\\\n\\midrule\nQwen & $0.15$ & $-0.073$ \\\\\nQwen & $0.20$ & $-0.076$ \\\\\nQwen & $0.25$ & $+0.045$ \\\\\nQwen & $0.30$ & $-0.007$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
      "numLines": 184,
      "startLine": 1,
      "totalLines": 184
    }
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Read · `toolu_01NCqbnNjiw9sg6b7LwLwSZD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250",
  "uuid": "5735a493-7cf8-41ad-b2c5-5aff4d671774",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015CLDLsECci42Epf4yqKCcN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4096,
      "cache_read_input_tokens": 23412,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4096
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

_source line 25 · 2026-05-15T01:43:42.609Z_

<details><summary>↩ Tool result · `toolu_01NCqbnNjiw9sg6b7LwLwSZD`</summary>

```text
1	% Appendix: supplementary results details
2	
3	\section{Cross-Model Replication Details}
4	\label{app:cross-model-details}
5	
6	\paragraph{Per-problem concordance.}
7	The per-problem concordance across models is not significant (median $\rho = \placeholder{}$, $p = \placeholder{}$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking. % exp_id: cross_model_analysis.json (spearman_rho=1.0, gradient_permutation_p=0.043, per_problem_concordance_p=0.926, mean_rho=-0.107)
8	
9	\paragraph{Random eviction control.}
10	As a control, random eviction on Qwen yields no systematic phase gradient at three of four sparsity levels (3/4 FAIL), mirroring DeepSeek's 4/4 FAIL pattern. At $s{=}0.30$, Qwen random produces a borderline PASS (permutation $p = 0.012$) but with negligible median difference ($\widetilde{\Delta} = \placeholder{}$, CI spans zero), indicating no meaningful phase modulation. % exp_id: bf16_qw_rand_s015..s030; source: experiment_summary_table.json
11	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250",
  "uuid": "2ef06aa7-4933-4f11-a87c-eeaf43264c57",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_results.tex",
      "content": "% Appendix: supplementary results details\n\n\\section{Cross-Model Replication Details}\n\\label{app:cross-model-details}\n\n\\paragraph{Per-problem concordance.}\nThe per-problem concordance across models is not significant (median $\\rho = \\placeholder{}$, $p = \\placeholder{}$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking. % exp_id: cross_model_analysis.json (spearman_rho=1.0, gradient_permutation_p=0.043, per_problem_concordance_p=0.926, mean_rho=-0.107)\n\n\\paragraph{Random eviction control.}\nAs a control, random eviction on Qwen yields no systematic phase gradient at three of four sparsity levels (3/4 FAIL), mirroring DeepSeek's 4/4 FAIL pattern. At $s{=}0.30$, Qwen random produces a borderline PASS (permutation $p = 0.012$) but with negligible median difference ($\\widetilde{\\Delta} = \\placeholder{}$, CI spans zero), indicating no meaningful phase modulation. % exp_id: bf16_qw_rand_s015..s030; source: experiment_summary_table.json\n",
      "numLines": 11,
      "startLine": 1,
      "totalLines": 11
    }
  }
}
```

</details>

---

### Tool call

_source line 26_

<details open><summary>🔧 Tool call — Read · `toolu_01SkQKJXrumVepxrpG7ucowR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250",
  "uuid": "2916f416-fb52-4e91-9afb-7eb63b8e18b3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015CLDLsECci42Epf4yqKCcN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4096,
      "cache_read_input_tokens": 23412,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4096
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

_source line 27 · 2026-05-15T01:43:43.233Z_

<details><summary>↩ Tool result · `toolu_01SkQKJXrumVepxrpG7ucowR`</summary>

```text
1	\section{Discrimination Collapse Details}
2	\label{app:discrimination-collapse-details}
3	
4	This cross-model consistency (Table~\ref{tab:discrimination-metrics-full}) establishes discrimination collapse as a robust consequence of compound sparsity. When importance scores lose discriminative power, thresholding the bottom-$s$ fraction becomes noise-sensitive: small perturbations change which positions cross the eviction boundary. In the limit of perfectly uniform scores, importance-based eviction degenerates into an arbitrary selection functionally equivalent to biased random eviction. The same pattern holds under random eviction (DeepSeek: $-0.031$ to $-0.073$; Qwen: $-0.019$ to $-0.045$), confirming that discrimination collapse is a consequence of head pruning \emph{per se}, not of the eviction strategy. % exp_id: c4_entropy_deepseek, c4_entropy_qwen
5	
6	
7	\section{Extended Discussion}
8	\label{app:extended-discussion}
9	
10	\paragraph{On the predictability of phase-modulated severity.}
11	The compound interaction is not uniformly fragile---it is selectively fragile in a phase-dependent manner ($\widetilde{\mathrm{II}}_{\text{high}} < 0.06$ at $s \leq 0.30$; at $s = 0.35$, high-phase II rises to $0.105$ in a supplementary experiment, indicating onset of compound interaction even in high-sparsity phases at extreme pruning rates). % exp_id: bf16_importance_s015..s030, bf16_ds_imp_s035; high-phase medians: 0.006, 0.015, 0.032, 0.053; s035 II_high=0.1051
12	
13	\paragraph{Random masking as falsification control.}
14	Random eviction fails 7/8 paired permutation tests across both models; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) exhibits negligible effect size ($\widetilde{\Delta} = \placeholder{}$). The absence of a phase gradient under random masking isolates the amplification as strategy-specific. % exp_id: bf16_ds_rand_s015..s030, bf16_qw_rand_s015..s030
15	
16	\paragraph{Entropy mechanism boundary conditions.}
17	Directly measuring per-head entropy shifts across architecturally distinct models---and identifying what training-time properties determine whether entropy concentrates or disperses under head pruning---would clarify the boundary conditions of the full mechanism.
18	
19	
20	\section{Extended Limitations}
21	\label{app:limitations}
22	
23	\paragraph{Model scale.}
24	All experiments are conducted at the 7B parameter scale.
25	Whether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested.
26	Larger models may exhibit different attention redundancy structures that alter the discrimination collapse dynamics (and the model-dependent entropy component may behave differently at scale).
27	% REVIEWER-ATTACK: "7B is too small to be relevant for production."
28	% REBUTTAL: 7B is the most-deployed scale for on-device and cost-constrained serving—exactly where compound sparsity is needed. The mechanism (entropy-discrimination collapse) is scale-agnostic in principle. Scaling experiments are future work.
29	
30	\paragraph{Architectural scope.}
31	Our two models---DeepSeek-R1-Distill-Qwen-7B and Qwen2.5-7B-Instruct---share the Qwen2ForCausalLM architecture.
32	The cross-model replication (\S\ref{sec:cross-model}) establishes that the findings are not artifacts of a single model's weights, though both models share the same Qwen2ForCausalLM architecture.
33	Preliminary cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \S\ref{sec:cross-arch}) shows qualitatively consistent within-importance phase gradients ($d_z \sim 1.0$) but a substantially weaker strategy $\times$ phase interaction than in Qwen2-based architectures; random pruning also exhibits a non-trivial phase gradient on LLaMA, reducing the strategy contrast. This partial confirmation ($s{=}0.30$ Wilcoxon $p_{\text{Bonf}}{=}0.029$; $s \leq 0.25$ non-significant) suggests the qualitative pattern may generalize but quantitative impact is architecture-dependent. Comprehensive cross-architecture validation across more diverse designs (e.g., Mistral, multi-latent attention architectures) and scales remains an important next step.
34	% REVIEWER-ATTACK: "Cross-model ≠ cross-architecture. Both are Qwen2ForCausalLM."
35	% REBUTTAL: We now include cross-architecture validation on LlamaForCausalLM (\S\ref{sec:cross-arch}), which shows a qualitatively consistent but substantially weaker pattern. We use qualified language ("partially supports") rather than claiming full generalization.
36	
37	\paragraph{Task coverage.}
38	We evaluate exclusively on MATH-500, a mathematical reasoning benchmark.
39	Different reasoning tasks---code generation, commonsense reasoning, multi-hop question answering---may induce different phase structures with different sparsity distributions, potentially altering the severity gradient profile.
40	Generalizing the phase-strategy interaction to broader reasoning domains is an important next step.
41	% REVIEWER-ATTACK: "Only MATH-500. How do we know this isn't a math-specific artifact?"
42	% REBUTTAL: The mechanism (entropy-discrimination collapse under head pruning) depends on attention distribution properties, not math-specific features. MATH-500 is a standard benchmark with diverse difficulty. However, different reasoning tasks may induce different phase structures—we state this limitation explicitly rather than overclaiming.
43	
44	\paragraph{Statistical scope.}
45	Bootstrap confidence intervals use $B{=}10{,}000$ resamples (recomputed from initial $B{=}1{,}000$ profiling runs). The paired permutation test yields $n{=}49$ paired problems for DeepSeek (1 excluded) and $n{=}46$ for Qwen (4 excluded). % exp_id: cohens_d_bf16.json, cohens_d_bf16_qwen.json
46	The severity difference distribution is right-skewed (mean/median ratio ${\sim}1.6{:}1$ at $s{=}0.30$), motivating our use of medians and nonparametric tests rather than parametric alternatives. % exp_id: bf16_importance_s030; mean_diff=22.94, median_diff=14.59 (segment-level). Per-problem paired: median_diff=9.9436 at s030
47	All four permutation tests reject $H_0$ after Bonferroni correction ($p_{\text{Bonf}} < 0.005$; Table~\ref{tab:permutation}), with CI lower bounds increasing from $0.19$ to $6.70$---confirming the effect direction at every sparsity level. The permutation CIs at higher sparsity are wider (e.g., $[6.70,\; 16.29]$ at $s{=}0.30$), reflecting genuine variance in per-problem severity amplification. % exp_id: permutation_test_results.json; permutation CIs: s015=[0.19,0.62], s020=[0.69,1.49], s025=[1.66,6.64], s030=[6.70,16.29]
48	
49	A notable exception among the random baselines is the Qwen random condition at $s{=}0.30$, which yields a statistically significant result ($p{=}0.012$) despite negligible effect size ($\widetilde{\Delta} = \placeholder{}$, bootstrap CI spanning zero). % exp_id: qw_rand_s030; B=10000, p=0.012, d=-0.035, negligible
50	This case illustrates that dichotomous significance testing can flag effects of no practical magnitude---reinforcing the importance of reporting effect sizes and confidence intervals alongside $p$-values.
51	
52	\paragraph{Sparsity range.}
53	Our experiments span $s \in \{0.15, 0.20, 0.25, 0.30\}$, a moderate range representative of practical deployment targets.
54	More extreme sparsity ($s > 0.50$) may exhibit qualitatively different interaction dynamics---the sub-exponential growth pattern suggests the severity gradient may plateau, but this remains unverified.
55	Conversely, the lower boundary at which phase-modulated amplification first emerges is not yet characterized.
56	% REVIEWER-ATTACK: "Why not test higher sparsity? 0.30 is conservative."
57	% REBUTTAL: Our focus is on the practically relevant regime where models retain usable quality. At s>0.30 both strategies degrade severely, making II measurement less informative. The sub-exponential growth (C6, $\Delta$ growth rate $3.8{\times} \to 4.8{\times} \to 2.0{\times}$) suggests saturation at higher sparsity, but confirming this is future work.
58	
59	\paragraph{No throughput evaluation.}
60	We do not report inference throughput or latency, which are necessary for deployment analysis but orthogonal to our severity characterization.
61	% REVIEWER-ATTACK: "No system evaluation. How do we know the severity amplification matters for real deployment?"
62	% REBUTTAL: This is an empirical finding paper, not a method/system paper. The contribution is characterizing *what happens* (phase-modulated severity) and *why* (entropy-discrimination collapse), not building a system to fix it. Phase-gated controllers are explicitly scoped as future work. The finding is actionable regardless: any compound sparsity deployment should be aware of phase-dependent severity.
63	
64	% Entropy redistribution analysis moved to main text \S\ref{sec:entropy-redistribution}
65	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250",
  "uuid": "17bff7bf-7694-4bab-b793-7b8517e6838e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex",
      "content": "\\section{Discrimination Collapse Details}\n\\label{app:discrimination-collapse-details}\n\nThis cross-model consistency (Table~\\ref{tab:discrimination-metrics-full}) establishes discrimination collapse as a robust consequence of compound sparsity. When importance scores lose discriminative power, thresholding the bottom-$s$ fraction becomes noise-sensitive: small perturbations change which positions cross the eviction boundary. In the limit of perfectly uniform scores, importance-based eviction degenerates into an arbitrary selection functionally equivalent to biased random eviction. The same pattern holds under random eviction (DeepSeek: $-0.031$ to $-0.073$; Qwen: $-0.019$ to $-0.045$), confirming that discrimination collapse is a consequence of head pruning \\emph{per se}, not of the eviction strategy. % exp_id: c4_entropy_deepseek, c4_entropy_qwen\n\n\n\\section{Extended Discussion}\n\\label{app:extended-discussion}\n\n\\paragraph{On the predictability of phase-modulated severity.}\nThe compound interaction is not uniformly fragile---it is selectively fragile in a phase-dependent manner ($\\widetilde{\\mathrm{II}}_{\\text{high}} < 0.06$ at $s \\leq 0.30$; at $s = 0.35$, high-phase II rises to $0.105$ in a supplementary experiment, indicating onset of compound interaction even in high-sparsity phases at extreme pruning rates). % exp_id: bf16_importance_s015..s030, bf16_ds_imp_s035; high-phase medians: 0.006, 0.015, 0.032, 0.053; s035 II_high=0.1051\n\n\\paragraph{Random masking as falsification control.}\nRandom eviction fails 7/8 paired permutation tests across both models; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) exhibits negligible effect size ($\\widetilde{\\Delta} = \\placeholder{}$). The absence of a phase gradient under random masking isolates the amplification as strategy-specific. % exp_id: bf16_ds_rand_s015..s030, bf16_qw_rand_s015..s030\n\n\\paragraph{Entropy mechanism boundary conditions.}\nDirectly measuring per-head entropy shifts across architecturally distinct models---and identifying what training-time properties determine whether entropy concentrates or disperses under head pruning---would clarify the boundary conditions of the full mechanism.\n\n\n\\section{Extended Limitations}\n\\label{app:limitations}\n\n\\paragraph{Model scale.}\nAll experiments are conducted at the 7B parameter scale.\nWhether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested.\nLarger models may exhibit different attention redundancy structures that alter the discrimination collapse dynamics (and the model-dependent entropy component may behave differently at scale).\n% REVIEWER-ATTACK: \"7B is too small to be relevant for production.\"\n% REBUTTAL: 7B is the most-deployed scale for on-device and cost-constrained serving—exactly where compound sparsity is needed. The mechanism (entropy-discrimination collapse) is scale-agnostic in principle. Scaling experiments are future work.\n\n\\paragraph{Architectural scope.}\nOur two models---DeepSeek-R1-Distill-Qwen-7B and Qwen2.5-7B-Instruct---share the Qwen2ForCausalLM architecture.\nThe cross-model replication (\\S\\ref{sec:cross-model}) establishes that the findings are not artifacts of a single model's weights, though both models share the same Qwen2ForCausalLM architecture.\nPreliminary cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \\S\\ref{sec:cross-arch}) shows qualitatively consistent within-importance phase gradients ($d_z \\sim 1.0$) but a substantially weaker strategy $\\times$ phase interaction than in Qwen2-based architectures; random pruning also exhibits a non-trivial phase gradient on LLaMA, reducing the strategy contrast. This partial confirmation ($s{=}0.30$ Wilcoxon $p_{\\text{Bonf}}{=}0.029$; $s \\leq 0.25$ non-significant) suggests the qualitative pattern may generalize but quantitative impact is architecture-dependent. Comprehensive cross-architecture validation across more diverse designs (e.g., Mistral, multi-latent attention architectures) and scales remains an important next step.\n% REVIEWER-ATTACK: \"Cross-model ≠ cross-architecture. Both are Qwen2ForCausalLM.\"\n% REBUTTAL: We now include cross-architecture validation on LlamaForCausalLM (\\S\\ref{sec:cross-arch}), which shows a qualitatively consistent but substantially weaker pattern. We use qualified language (\"partially supports\") rather than claiming full generalization.\n\n\\paragraph{Task coverage.}\nWe evaluate exclusively on MATH-500, a mathematical reasoning benchmark.\nDifferent reasoning tasks---code generation, commonsense reasoning, multi-hop question answering---may induce different phase structures with different sparsity distributions, potentially altering the severity gradient profile.\nGeneralizing the phase-strategy interaction to broader reasoning domains is an important next step.\n% REVIEWER-ATTACK: \"Only MATH-500. How do we know this isn't a math-specific artifact?\"\n% REBUTTAL: The mechanism (entropy-discrimination collapse under head pruning) depends on attention distribution properties, not math-specific features. MATH-500 is a standard benchmark with diverse difficulty. However, different reasoning tasks may induce different phase structures—we state this limitation explicitly rather than overclaiming.\n\n\\paragraph{Statistical scope.}\nBootstrap confidence intervals use $B{=}10{,}000$ resamples (recomputed from initial $B{=}1{,}000$ profiling runs). The paired permutation test yields $n{=}49$ paired problems for DeepSeek (1 excluded) and $n{=}46$ for Qwen (4 excluded). % exp_id: cohens_d_bf16.json, cohens_d_bf16_qwen.json\nThe severity difference distribution is right-skewed (mean/median ratio ${\\sim}1.6{:}1$ at $s{=}0.30$), motivating our use of medians and nonparametric tests rather than parametric alternatives. % exp_id: bf16_importance_s030; mean_diff=22.94, median_diff=14.59 (segment-level). Per-problem paired: median_diff=9.9436 at s030\nAll four permutation tests reject $H_0$ after Bonferroni correction ($p_{\\text{Bonf}} < 0.005$; Table~\\ref{tab:permutation}), with CI lower bounds increasing from $0.19$ to $6.70$---confirming the effect direction at every sparsity level. The permutation CIs at higher sparsity are wider (e.g., $[6.70,\\; 16.29]$ at $s{=}0.30$), reflecting genuine variance in per-problem severity amplification. % exp_id: permutation_test_results.json; permutation CIs: s015=[0.19,0.62], s020=[0.69,1.49], s025=[1.66,6.64], s030=[6.70,16.29]\n\nA notable exception among the random baselines is the Qwen random condition at $s{=}0.30$, which yields a statistically significant result ($p{=}0.012$) despite negligible effect size ($\\widetilde{\\Delta} = \\placeholder{}$, bootstrap CI spanning zero). % exp_id: qw_rand_s030; B=10000, p=0.012, d=-0.035, negligible\nThis case illustrates that dichotomous significance testing can flag effects of no practical magnitude---reinforcing the importance of reporting effect sizes and confidence intervals alongside $p$-values.\n\n\\paragraph{Sparsity range.}\nOur experiments span $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$, a moderate range representative of practical deployment targets.\nMore extreme sparsity ($s > 0.50$) may exhibit qualitatively different interaction dynamics---the sub-exponential growth pattern suggests the severity gradient may plateau, but this remains unverified.\nConversely, the lower boundary at which phase-modulated amplification first emerges is not yet characterized.\n% REVIEWER-ATTACK: \"Why not test higher sparsity? 0.30 is conservative.\"\n% REBUTTAL: Our focus is on the practically relevant regime where models retain usable quality. At s>0.30 both strategies degrade severely, making II measurement less informative. The sub-exponential growth (C6, $\\Delta$ growth rate $3.8{\\times} \\to 4.8{\\times} \\to 2.0{\\times}$) suggests saturation at higher sparsity, but confirming this is future work.\n\n\\paragraph{No throughput evaluation.}\nWe do not report inference throughput or latency, which are necessary for deployment analysis but orthogonal to our severity characterization.\n% REVIEWER-ATTACK: \"No system evaluation. How do we know the severity amplification matters for real deployment?\"\n% REBUTTAL: This is an empirical finding paper, not a method/system paper. The contribution is characterizing *what happens* (phase-modulated severity) and *why* (entropy-discrimination collapse), not building a system to fix it. Phase-gated controllers are explicitly scoped as future work. The finding is actionable regardless: any compound sparsity deployment should be aware of phase-dependent severity.\n\n% Entropy redistribution analysis moved to main text \\S\\ref{sec:entropy-redistribution}\n",
      "numLines": 65,
      "startLine": 1,
      "totalLines": 65
    }
  }
}
```

</details>

---

### Assistant

_source line 28_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the remaining files that might contain hardcoded values: introduction.tex, methodology.tex, conclusion.tex, analysis.tex, appendix.tex, limitations.tex.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250",
  "uuid": "5ba7bb0f-ab29-4ade-95bd-e80276f02a51",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016sxasNJ1VTaQ5dscBFfxnw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 28246,
      "cache_read_input_tokens": 27508,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 28246
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

_source line 29_

Now reading the remaining files with potential hardcoded values.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250",
  "uuid": "4c8bf6f4-926d-4386-b6ce-b3ca3169059b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016sxasNJ1VTaQ5dscBFfxnw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 28246,
      "cache_read_input_tokens": 27508,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 28246
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

_source line 30_

<details open><summary>🔧 Tool call — Read · `toolu_01Sobm5AyBmT3NC2f3HTbWSE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250",
  "uuid": "c9257e90-5aab-499e-b36c-a644c7fb44d3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016sxasNJ1VTaQ5dscBFfxnw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 28246,
      "cache_read_input_tokens": 27508,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 28246
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

_source line 31 · 2026-05-15T01:43:49.844Z_

<details><summary>↩ Tool result · `toolu_01Sobm5AyBmT3NC2f3HTbWSE`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Long-context language models place acute pressure on the key--value (KV) cache, which grows linearly with sequence length \cite{kwon-sosp2023, pope-mlsys2023}.
5	Two complementary responses---\emph{attention head pruning} \cite{voita-acl2019, michel-neurips2019} and \emph{KV cache eviction} \cite{snapkv-neurips2024, adakv-neurips2025}---can be deployed simultaneously as \emph{compound sparsity}, but the resulting quality degradation is often super-additive \cite{spark-aaai2026, slim-icml2025}. Recent evaluations confirm that reasoning capabilities degrade disproportionately under compound compression \cite{unicomp-2026}, and that per-dimension safe zones intersect to form a smaller joint safe region \cite{phase-transition-compression-2026}.
6	
7	Prior work treats compound interaction magnitude as roughly constant across generation \cite{spark-aaai2026, unicomp-2026}, despite evidence that pruning sensitivity depends on representational phase \cite{decision-repr-transition-2026} and that no single sparse attention strategy dominates across generation stages \cite{sparse-frontier-2025}.
8	This assumption is problematic for reasoning models, whose generations alternate between broadly distributed attention (exploratory reasoning) and sharply concentrated attention (structured computation) \cite{thinkv-iclr2026}.
9	Phase-aware methods like ThinKV \cite{thinkv-iclr2026} apply different KV strategies per phase but without considering compound interaction, while importance-based eviction itself faces challenges from greedy bias \cite{greedy-bias-kvcache-2026}, deferred importance \cite{retentivekv-2026}, and temporal dynamics in long generations \cite{lethe-aaai2026}. These methods each optimize a single pruning axis; we characterize the interaction when multiple mechanisms are composed.
10	If compound severity varies across these phases, a uniform sparsity budget may be safe in one phase yet destructive in another.
11	
12	We show that compound sparsity severity is strongly modulated by reasoning phase and eviction strategy.
13	Under importance-based KV cache eviction, the Interaction Index---a measure of super-additive degradation---concentrates in low-sparsity phases and is largely absent in high-sparsity phases.
14	On DeepSeek-R1-Distill-Qwen-7B, the median phase difference rises from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$ ($d_z$: $0.44 \to 0.80$; Bonferroni-corrected $p < 0.005$ at all levels).
15	The pattern replicates at $s \geq 0.20$ on Qwen2.5-7B-Instruct ($d_z \geq 0.55$) and partially extends to a distinct architecture (DeepSeek-R1-Distill-Llama-8B, LlamaForCausalLM) with a qualitatively consistent but substantially weaker trend at $\sim$1/40 the magnitude.
16	Critically, random eviction produces no such gradient (7/8 conditions non-significant), confirming the gradient is an emergent phase-strategy interaction.
17	
18	We propose \emph{entropy-discrimination collapse} as a mechanism: head pruning flattens cumulative importance scores in phases where attention is broadly distributed, degrading the discriminative power of importance-based eviction in a phase-dependent manner.
19	Random eviction is immune because its decisions are independent of attention patterns.
20	Our contributions:
21	\begin{enumerate}[nosep,leftmargin=*]
22	    \item We identify a \textbf{phase--strategy interaction}: importance-based eviction exhibits a severity gradient across reasoning phases that is absent under random eviction (\S\ref{sec:results}).
23	    \item We show this gradient \textbf{increases monotonically with sparsity} and replicates across three models spanning two architectures (\S\ref{sec:results}).
24	    \item We propose \textbf{entropy-discrimination collapse} as a mechanistic explanation (\S\ref{sec:analysis}).
25	\end{enumerate}
26	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250",
  "uuid": "066be48e-1962-45be-8b03-5e4319a0a0fd",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nLong-context language models place acute pressure on the key--value (KV) cache, which grows linearly with sequence length \\cite{kwon-sosp2023, pope-mlsys2023}.\nTwo complementary responses---\\emph{attention head pruning} \\cite{voita-acl2019, michel-neurips2019} and \\emph{KV cache eviction} \\cite{snapkv-neurips2024, adakv-neurips2025}---can be deployed simultaneously as \\emph{compound sparsity}, but the resulting quality degradation is often super-additive \\cite{spark-aaai2026, slim-icml2025}. Recent evaluations confirm that reasoning capabilities degrade disproportionately under compound compression \\cite{unicomp-2026}, and that per-dimension safe zones intersect to form a smaller joint safe region \\cite{phase-transition-compression-2026}.\n\nPrior work treats compound interaction magnitude as roughly constant across generation \\cite{spark-aaai2026, unicomp-2026}, despite evidence that pruning sensitivity depends on representational phase \\cite{decision-repr-transition-2026} and that no single sparse attention strategy dominates across generation stages \\cite{sparse-frontier-2025}.\nThis assumption is problematic for reasoning models, whose generations alternate between broadly distributed attention (exploratory reasoning) and sharply concentrated attention (structured computation) \\cite{thinkv-iclr2026}.\nPhase-aware methods like ThinKV \\cite{thinkv-iclr2026} apply different KV strategies per phase but without considering compound interaction, while importance-based eviction itself faces challenges from greedy bias \\cite{greedy-bias-kvcache-2026}, deferred importance \\cite{retentivekv-2026}, and temporal dynamics in long generations \\cite{lethe-aaai2026}. These methods each optimize a single pruning axis; we characterize the interaction when multiple mechanisms are composed.\nIf compound severity varies across these phases, a uniform sparsity budget may be safe in one phase yet destructive in another.\n\nWe show that compound sparsity severity is strongly modulated by reasoning phase and eviction strategy.\nUnder importance-based KV cache eviction, the Interaction Index---a measure of super-additive degradation---concentrates in low-sparsity phases and is largely absent in high-sparsity phases.\nOn DeepSeek-R1-Distill-Qwen-7B, the median phase difference rises from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$ ($d_z$: $0.44 \\to 0.80$; Bonferroni-corrected $p < 0.005$ at all levels).\nThe pattern replicates at $s \\geq 0.20$ on Qwen2.5-7B-Instruct ($d_z \\geq 0.55$) and partially extends to a distinct architecture (DeepSeek-R1-Distill-Llama-8B, LlamaForCausalLM) with a qualitatively consistent but substantially weaker trend at $\\sim$1/40 the magnitude.\nCritically, random eviction produces no such gradient (7/8 conditions non-significant), confirming the gradient is an emergent phase-strategy interaction.\n\nWe propose \\emph{entropy-discrimination collapse} as a mechanism: head pruning flattens cumulative importance scores in phases where attention is broadly distributed, degrading the discriminative power of importance-based eviction in a phase-dependent manner.\nRandom eviction is immune because its decisions are independent of attention patterns.\nOur contributions:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item We identify a \\textbf{phase--strategy interaction}: importance-based eviction exhibits a severity gradient across reasoning phases that is absent under random eviction (\\S\\ref{sec:results}).\n    \\item We show this gradient \\textbf{increases monotonically with sparsity} and replicates across three models spanning two architectures (\\S\\ref{sec:results}).\n    \\item We propose \\textbf{entropy-discrimination collapse} as a mechanistic explanation (\\S\\ref{sec:analysis}).\n\\end{enumerate}\n",
      "numLines": 26,
      "startLine": 1,
      "totalLines": 26
    }
  }
}
```

</details>

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — Read · `toolu_01RiWjP8XMCJFzN7YE87fWki`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250",
  "uuid": "fc223d0c-bb17-4a0a-be1b-ccaff02621e1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016sxasNJ1VTaQ5dscBFfxnw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 28246,
      "cache_read_input_tokens": 27508,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 28246
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

_source line 33 · 2026-05-15T01:43:50.283Z_

<details><summary>↩ Tool result · `toolu_01RiWjP8XMCJFzN7YE87fWki`</summary>

```text
1	\section{Experimental Setup}
2	\label{sec:experimental-setup}
3	
4	\paragraph{Models.}
5	\label{sec:models}
6	We evaluate on two 7B-parameter models sharing the Qwen2 backbone (28 layers, 28 heads, 4-group GQA): \textbf{DeepSeek-R1-Distill-Qwen-7B}~\cite{deepseek-r1-2025}, distilled from DeepSeek-R1 with explicit chain-of-thought traces yielding pronounced phase structure; and \textbf{Qwen2.5-7B-Instruct}~\cite{qwen25-2024}, with standard instruction tuning, providing a cross-model replication target. Both are loaded in \texttt{bfloat16} with eager attention.\footnote{An earlier \texttt{float16} configuration produced sporadic NaN values; \texttt{bfloat16} eliminated all occurrences.}
7	
8	\paragraph{Dataset.}
9	\label{sec:dataset}
10	We use 50 problems stratified from MATH-500~\cite{math500-neurips2021}, sampling uniformly across categories with a fixed seed. Each problem is decoded greedily (\texttt{max\_new\_tokens}$=$2048).
11	
12	\paragraph{Sparsity configuration.}
13	\label{sec:sparsity-config}
14	We apply symmetric compound sparsity at $s \in \{0.15, 0.20, 0.25, 0.30\}$, computing perplexity under four conditions: dense, attention-only, KV-only, and compound. We compare \emph{importance-based} eviction (position-normalized cumulative attention score, Eq.~\ref{eq:kv-importance}; BOS always retained) and \emph{random} eviction (uniform). Heads are pruned per layer by Frobenius norm; under random eviction, both heads and positions are selected uniformly.
15	
16	\paragraph{Phase segmentation and metrics.}
17	\label{sec:phase-seg}
18	Each sequence is segmented into three phases using the quantile-based method (\S\ref{sec:phase-segmentation}), with $\texttt{min\_phase\_length}{=}10$. We compute segment-level perplexity, II (Eq.~\ref{eq:ii}), and $G$ (Eq.~\ref{eq:gradient}), reporting medians due to heavy right-skew (mean/median ratios up to 43:1).
19	
20	\paragraph{Statistical analysis.}
21	\label{sec:stats}
22	All reported confidence intervals and significance tests use nonparametric bootstrap ($B{=}10{,}000$)~\cite{efron-1993}; initial profiling uses $B{=}1{,}000$ for computational efficiency, with all reported statistics recomputed at $B{=}10{,}000$. Paired bootstrap controls for problem-level variance. All tests yield $p_{\text{Bonf}} < 0.005$ at every sparsity level.\footnote{Experiments on 4$\times$ NVIDIA RTX PRO 6000 Blackwell 96\,GB GPUs.}
23	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250",
  "uuid": "f08b93c2-e4b3-4c32-bdf0-7b1544a4e1ac",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex",
      "content": "\\section{Experimental Setup}\n\\label{sec:experimental-setup}\n\n\\paragraph{Models.}\n\\label{sec:models}\nWe evaluate on two 7B-parameter models sharing the Qwen2 backbone (28 layers, 28 heads, 4-group GQA): \\textbf{DeepSeek-R1-Distill-Qwen-7B}~\\cite{deepseek-r1-2025}, distilled from DeepSeek-R1 with explicit chain-of-thought traces yielding pronounced phase structure; and \\textbf{Qwen2.5-7B-Instruct}~\\cite{qwen25-2024}, with standard instruction tuning, providing a cross-model replication target. Both are loaded in \\texttt{bfloat16} with eager attention.\\footnote{An earlier \\texttt{float16} configuration produced sporadic NaN values; \\texttt{bfloat16} eliminated all occurrences.}\n\n\\paragraph{Dataset.}\n\\label{sec:dataset}\nWe use 50 problems stratified from MATH-500~\\cite{math500-neurips2021}, sampling uniformly across categories with a fixed seed. Each problem is decoded greedily (\\texttt{max\\_new\\_tokens}$=$2048).\n\n\\paragraph{Sparsity configuration.}\n\\label{sec:sparsity-config}\nWe apply symmetric compound sparsity at $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$, computing perplexity under four conditions: dense, attention-only, KV-only, and compound. We compare \\emph{importance-based} eviction (position-normalized cumulative attention score, Eq.~\\ref{eq:kv-importance}; BOS always retained) and \\emph{random} eviction (uniform). Heads are pruned per layer by Frobenius norm; under random eviction, both heads and positions are selected uniformly.\n\n\\paragraph{Phase segmentation and metrics.}\n\\label{sec:phase-seg}\nEach sequence is segmented into three phases using the quantile-based method (\\S\\ref{sec:phase-segmentation}), with $\\texttt{min\\_phase\\_length}{=}10$. We compute segment-level perplexity, II (Eq.~\\ref{eq:ii}), and $G$ (Eq.~\\ref{eq:gradient}), reporting medians due to heavy right-skew (mean/median ratios up to 43:1).\n\n\\paragraph{Statistical analysis.}\n\\label{sec:stats}\nAll reported confidence intervals and significance tests use nonparametric bootstrap ($B{=}10{,}000$)~\\cite{efron-1993}; initial profiling uses $B{=}1{,}000$ for computational efficiency, with all reported statistics recomputed at $B{=}10{,}000$. Paired bootstrap controls for problem-level variance. All tests yield $p_{\\text{Bonf}} < 0.005$ at every sparsity level.\\footnote{Experiments on 4$\\times$ NVIDIA RTX PRO 6000 Blackwell 96\\,GB GPUs.}\n",
      "numLines": 23,
      "startLine": 1,
      "totalLines": 23
    }
  }
}
```

</details>

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Read · `toolu_01YYA6SnRhJsXiwTLjNdFhQ6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250",
  "uuid": "7b097faa-514b-4bd8-9b03-2b462f50349c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016sxasNJ1VTaQ5dscBFfxnw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 28246,
      "cache_read_input_tokens": 27508,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 28246
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

_source line 35 · 2026-05-15T01:43:50.814Z_

<details><summary>↩ Tool result · `toolu_01YYA6SnRhJsXiwTLjNdFhQ6`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We showed that compound sparsity severity---the super-additive interaction between head pruning and KV cache eviction---is not phase-invariant but exhibits an emergent phase-strategy interaction spanning over an order of magnitude within a single generation. Under importance-based eviction, the severity gradient grows from $69{\times}$ to $274{\times}$ across sparsity levels ($d_z$: $0.44 \to 0.80$); random eviction shows no such modulation (7/8 conditions non-significant). A crossover at $s{=}0.25$---where importance-based eviction reverses ranking across phases---demonstrates that no single strategy dominates uniformly. The pattern replicates on Qwen2.5-7B-Instruct at $s \geq 0.20$ ($d_z \geq 0.55$) and partially extends cross-architecture to DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM) with a qualitatively consistent but substantially weaker trend at $\sim$1/40 the magnitude. Discrimination collapse provides a mechanistic explanation supported by both Qwen2-based models; LLaMA results are directionally consistent but the interaction is weaker than in Qwen2 architectures.
5	These findings motivate phase-aware sparsity allocation for reasoning model deployment.
6	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250",
  "uuid": "404a3141-b500-492a-888d-2de51979d0d0",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex",
      "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe showed that compound sparsity severity---the super-additive interaction between head pruning and KV cache eviction---is not phase-invariant but exhibits an emergent phase-strategy interaction spanning over an order of magnitude within a single generation. Under importance-based eviction, the severity gradient grows from $69{\\times}$ to $274{\\times}$ across sparsity levels ($d_z$: $0.44 \\to 0.80$); random eviction shows no such modulation (7/8 conditions non-significant). A crossover at $s{=}0.25$---where importance-based eviction reverses ranking across phases---demonstrates that no single strategy dominates uniformly. The pattern replicates on Qwen2.5-7B-Instruct at $s \\geq 0.20$ ($d_z \\geq 0.55$) and partially extends cross-architecture to DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM) with a qualitatively consistent but substantially weaker trend at $\\sim$1/40 the magnitude. Discrimination collapse provides a mechanistic explanation supported by both Qwen2-based models; LLaMA results are directionally consistent but the interaction is weaker than in Qwen2 architectures.\nThese findings motivate phase-aware sparsity allocation for reasoning model deployment.\n",
      "numLines": 6,
      "startLine": 1,
      "totalLines": 6
    }
  }
}
```

</details>

---

### Tool call

_source line 36_

<details open><summary>🔧 Tool call — Read · `toolu_017oF6G8CVnoUfci7wN2nrgz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250",
  "uuid": "386be0b2-a00e-452f-9985-a3a893ae4cd9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016sxasNJ1VTaQ5dscBFfxnw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 28246,
      "cache_read_input_tokens": 27508,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 28246
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

_source line 37 · 2026-05-15T01:43:51.317Z_

<details><summary>↩ Tool result · `toolu_017oF6G8CVnoUfci7wN2nrgz`</summary>

```text
1	\section{Analysis: Entropy-Discrimination Collapse}
2	\label{sec:analysis}
3	
4	We propose \emph{discrimination collapse} as the primary mechanism driving the phase-strategy interaction. Head pruning reduces the number of heads contributing to cumulative importance scores, flattening the score distribution: the Gini coefficient decreases by $0.030$--$0.081$ (DeepSeek) and $0.010$--$0.020$ (Qwen) across all sparsity levels, with consistent negative deltas in all 16 conditions (Appendix~\ref{app:analysis}, Table~\ref{tab:discrimination-metrics-full}). When importance scores lose discriminability, thresholding degenerates into noise-sensitive selection---functionally approaching biased random eviction. This effect is phase-dependent: in low-sparsity phases, attention is already broadly distributed, so pruning-induced flattening has maximum impact; in high-sparsity phases, concentration is preserved. Random eviction is immune because its decisions are independent of score quality, explaining $G \approx 1$. % exp_id: c4_entropy_deepseek, c4_entropy_qwen
5	
6	Beyond discrimination collapse, head pruning redistributes the attention entropy of surviving heads. For DeepSeek, the entropy delta is consistently negative ($\Delta\mathcal{H} \in [-0.047, -0.040]$), indicating that importance-based pruning systematically selects heads whose removal concentrates attention in survivors. For Qwen, the pattern partially replicates at $s \leq 0.20$ but reverses at $s{=}0.25$ ($\Delta\mathcal{H} = +0.045$), suggesting model-specific head specialization patterns (Appendix~\ref{app:analysis}, Table~\ref{tab:entropy-deltas}). We characterize discrimination collapse as the robust, model-independent driver, with entropy redistribution as a secondary, model-dependent amplifier. % exp_id: c4_entropy_deepseek, c4_entropy_qwen
7	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250",
  "uuid": "e413baf2-ae5c-4833-8640-732e9a1aa229",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex",
      "content": "\\section{Analysis: Entropy-Discrimination Collapse}\n\\label{sec:analysis}\n\nWe propose \\emph{discrimination collapse} as the primary mechanism driving the phase-strategy interaction. Head pruning reduces the number of heads contributing to cumulative importance scores, flattening the score distribution: the Gini coefficient decreases by $0.030$--$0.081$ (DeepSeek) and $0.010$--$0.020$ (Qwen) across all sparsity levels, with consistent negative deltas in all 16 conditions (Appendix~\\ref{app:analysis}, Table~\\ref{tab:discrimination-metrics-full}). When importance scores lose discriminability, thresholding degenerates into noise-sensitive selection---functionally approaching biased random eviction. This effect is phase-dependent: in low-sparsity phases, attention is already broadly distributed, so pruning-induced flattening has maximum impact; in high-sparsity phases, concentration is preserved. Random eviction is immune because its decisions are independent of score quality, explaining $G \\approx 1$. % exp_id: c4_entropy_deepseek, c4_entropy_qwen\n\nBeyond discrimination collapse, head pruning redistributes the attention entropy of surviving heads. For DeepSeek, the entropy delta is consistently negative ($\\Delta\\mathcal{H} \\in [-0.047, -0.040]$), indicating that importance-based pruning systematically selects heads whose removal concentrates attention in survivors. For Qwen, the pattern partially replicates at $s \\leq 0.20$ but reverses at $s{=}0.25$ ($\\Delta\\mathcal{H} = +0.045$), suggesting model-specific head specialization patterns (Appendix~\\ref{app:analysis}, Table~\\ref{tab:entropy-deltas}). We characterize discrimination collapse as the robust, model-independent driver, with entropy redistribution as a secondary, model-dependent amplifier. % exp_id: c4_entropy_deepseek, c4_entropy_qwen\n",
      "numLines": 7,
      "startLine": 1,
      "totalLines": 7
    }
  }
}
```

</details>

---

### Tool call

_source line 38_

<details open><summary>🔧 Tool call — Read · `toolu_01BmJ4uL8bzoiGMsVBvXKTv6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250",
  "uuid": "5cd0ee9d-c68e-4756-b897-bbcda1811899",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016sxasNJ1VTaQ5dscBFfxnw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 28246,
      "cache_read_input_tokens": 27508,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 28246
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

_source line 39 · 2026-05-15T01:43:51.730Z_

<details><summary>↩ Tool result · `toolu_01BmJ4uL8bzoiGMsVBvXKTv6`</summary>

```text
1	\section{Compound Sparsity Formulation}
2	\label{app:formulation-details}
3	
4	\paragraph{Attention head pruning.}
5	Heads are ranked by Frobenius norm importance $w_j^{(\ell)} = \|\mathbf{A}_j^{(\ell)}\|_F$ \cite{voita-acl2019, michel-neurips2019}; a binary mask $m_j^{(\ell)} \in \{0,1\}$ retains the top-$(1{-}s)\cdot H$ heads:
6	\begin{equation}
7	    \tilde{\mathbf{o}}_j^{(\ell)} = m_j^{(\ell)} \cdot \mathbf{o}_j^{(\ell)}.
8	    \label{eq:head-mask}
9	\end{equation}
10	
11	\paragraph{KV cache eviction.}
12	A position mask $\mathbf{m}_k \in \{0,1\}^T$ retains the top-$(1{-}s)\cdot T$ positions (BOS always preserved):
13	\begin{equation}
14	    \tilde{a}_{ij} = a_{ij} \cdot m_{k,j}, \quad \forall\, i, j.
15	    \label{eq:kv-mask}
16	\end{equation}
17	Under importance-based eviction, each position $j$ is scored by its cumulative attention mass with position normalization:
18	\begin{equation}
19	    \mathrm{imp}(j) = \frac{\sum_{\ell, h, i} a_{ij}^{(\ell,h)}}{T - j},
20	    \label{eq:kv-importance}
21	\end{equation}
22	where the denominator compensates for causal bias---earlier positions are attended to by more queries \cite{thinkv-iclr2026, defensivekv-iclr2026}. Under random eviction, positions (excluding BOS) are evicted uniformly at random.
23	
24	\paragraph{Compound sparsity.}
25	Applying both mechanisms simultaneously yields compound sparsity. The two axes interact: head pruning redistributes attention mass, altering the importance ranking for KV eviction. Prior work \cite{spark-aaai2026} reports super-additive joint effects but treats interaction magnitude as a fixed property of $s$.
26	
27	\paragraph{Attention sparsity metric.}
28	For each query position $i$ and head $h$, we compute the fraction of key positions receiving negligible attention:
29	\begin{equation}
30	    \sigma_i^{(h)} = \frac{1}{T} \sum_{j=1}^{T} \mathbf{1}\!\left[a_{ij}^{(h)} < 0.01 \cdot \max_k a_{ik}^{(h)}\right].
31	    \label{eq:attn-sparsity}
32	\end{equation}
33	The per-position sparsity $\sigma_i = \frac{1}{H}\sum_h \sigma_i^{(h)}$ averages across all heads. Tokens are partitioned into high-, mid-, and low-sparsity phases by the tercile boundaries of $\{\sigma_i\}$; segments shorter than 10 tokens are merged into adjacent phases.
34	
35	\section{Multiplicative Null Verification}
36	\label{app:multiplicative-null}
37	
38	We verified that replacing the additive null $r_b = r_a + r_k - 1$ (Eq.~\ref{eq:ii}) with the multiplicative null $r_b = r_a \cdot r_k$ does not change qualitative conclusions. Under the multiplicative formulation, the interaction index becomes $\mathrm{II}_{\times} = r_b - r_a \cdot r_k$. Across all sparsity levels and both eviction strategies, the sign and relative ordering of $\mathrm{II}_{\times}$ match those of the additive II: importance-based eviction exhibits a monotonically increasing severity gradient ($G_{\times} = 58$--$241{\times}$), while random eviction remains flat ($G_{\times} \approx 1$). The crossover at $s{=}0.25$ is preserved. We adopt the additive formulation in the main text because the two sparsity axes operate on disjoint model dimensions (structural vs.\ positional), making additive independence the more natural null hypothesis at the sparsity levels studied.
39	
40	% Bootstrap and permutation details moved to main text \S\ref{sec:stat-validation}
41	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250",
  "uuid": "67681230-3a24-4a95-9d18-c42734dc9071",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex",
      "content": "\\section{Compound Sparsity Formulation}\n\\label{app:formulation-details}\n\n\\paragraph{Attention head pruning.}\nHeads are ranked by Frobenius norm importance $w_j^{(\\ell)} = \\|\\mathbf{A}_j^{(\\ell)}\\|_F$ \\cite{voita-acl2019, michel-neurips2019}; a binary mask $m_j^{(\\ell)} \\in \\{0,1\\}$ retains the top-$(1{-}s)\\cdot H$ heads:\n\\begin{equation}\n    \\tilde{\\mathbf{o}}_j^{(\\ell)} = m_j^{(\\ell)} \\cdot \\mathbf{o}_j^{(\\ell)}.\n    \\label{eq:head-mask}\n\\end{equation}\n\n\\paragraph{KV cache eviction.}\nA position mask $\\mathbf{m}_k \\in \\{0,1\\}^T$ retains the top-$(1{-}s)\\cdot T$ positions (BOS always preserved):\n\\begin{equation}\n    \\tilde{a}_{ij} = a_{ij} \\cdot m_{k,j}, \\quad \\forall\\, i, j.\n    \\label{eq:kv-mask}\n\\end{equation}\nUnder importance-based eviction, each position $j$ is scored by its cumulative attention mass with position normalization:\n\\begin{equation}\n    \\mathrm{imp}(j) = \\frac{\\sum_{\\ell, h, i} a_{ij}^{(\\ell,h)}}{T - j},\n    \\label{eq:kv-importance}\n\\end{equation}\nwhere the denominator compensates for causal bias---earlier positions are attended to by more queries \\cite{thinkv-iclr2026, defensivekv-iclr2026}. Under random eviction, positions (excluding BOS) are evicted uniformly at random.\n\n\\paragraph{Compound sparsity.}\nApplying both mechanisms simultaneously yields compound sparsity. The two axes interact: head pruning redistributes attention mass, altering the importance ranking for KV eviction. Prior work \\cite{spark-aaai2026} reports super-additive joint effects but treats interaction magnitude as a fixed property of $s$.\n\n\\paragraph{Attention sparsity metric.}\nFor each query position $i$ and head $h$, we compute the fraction of key positions receiving negligible attention:\n\\begin{equation}\n    \\sigma_i^{(h)} = \\frac{1}{T} \\sum_{j=1}^{T} \\mathbf{1}\\!\\left[a_{ij}^{(h)} < 0.01 \\cdot \\max_k a_{ik}^{(h)}\\right].\n    \\label{eq:attn-sparsity}\n\\end{equation}\nThe per-position sparsity $\\sigma_i = \\frac{1}{H}\\sum_h \\sigma_i^{(h)}$ averages across all heads. Tokens are partitioned into high-, mid-, and low-sparsity phases by the tercile boundaries of $\\{\\sigma_i\\}$; segments shorter than 10 tokens are merged into adjacent phases.\n\n\\section{Multiplicative Null Verification}\n\\label{app:multiplicative-null}\n\nWe verified that replacing the additive null $r_b = r_a + r_k - 1$ (Eq.~\\ref{eq:ii}) with the multiplicative null $r_b = r_a \\cdot r_k$ does not change qualitative conclusions. Under the multiplicative formulation, the interaction index becomes $\\mathrm{II}_{\\times} = r_b - r_a \\cdot r_k$. Across all sparsity levels and both eviction strategies, the sign and relative ordering of $\\mathrm{II}_{\\times}$ match those of the additive II: importance-based eviction exhibits a monotonically increasing severity gradient ($G_{\\times} = 58$--$241{\\times}$), while random eviction remains flat ($G_{\\times} \\approx 1$). The crossover at $s{=}0.25$ is preserved. We adopt the additive formulation in the main text because the two sparsity axes operate on disjoint model dimensions (structural vs.\\ positional), making additive independence the more natural null hypothesis at the sparsity levels studied.\n\n% Bootstrap and permutation details moved to main text \\S\\ref{sec:stat-validation}\n",
      "numLines": 41,
      "startLine": 1,
      "totalLines": 41
    }
  }
}
```

</details>

---

### Tool call

_source line 40_

<details open><summary>🔧 Tool call — Read · `toolu_01BzNgLoJa9FjxBTuq6xeuvJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250",
  "uuid": "367db9b3-217f-4721-9dd6-8ce400de94d7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016sxasNJ1VTaQ5dscBFfxnw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 28246,
      "cache_read_input_tokens": 27508,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 28246
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

_source line 41 · 2026-05-15T01:43:52.440Z_

<details><summary>↩ Tool result · `toolu_01BzNgLoJa9FjxBTuq6xeuvJ`</summary>

```text
1	\paragraph{Model scale and architecture.}
2	All experiments are conducted at the 7--8B parameter scale. Whether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested. Preliminary cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \S\ref{sec:cross-arch}) partially confirms the qualitative pattern beyond the Qwen2 architecture---monotonically increasing $d_z$ with within-importance phase gradient $\sim$1.0---but with substantially weaker interaction magnitude ($\sim$1/40 of DeepSeek) and mixed statistical evidence (only $s{=}0.30$ significant after Bonferroni correction). The pattern has been tested on two architecture families (Qwen2ForCausalLM, LlamaForCausalLM); comprehensive validation across more diverse architectures (e.g., Mistral, multi-latent attention) and larger scales is needed for full generalization claims.
3	
4	\paragraph{Task coverage.}
5	We evaluate exclusively on MATH-500, a mathematical reasoning benchmark. Different reasoning tasks---code generation, commonsense reasoning, multi-hop question answering---may induce different phase structures with different sparsity distributions, potentially altering the severity gradient profile.
6	
7	\paragraph{Mechanism.}
8	The discrimination collapse mechanism is supported by correlational evidence (consistent Gini/CV reduction across all conditions); causal validation through controlled entropy manipulation is needed. The entropy redistribution component replicates on only 2/4 Qwen conditions, suggesting model-specific factors.
9	
10	\paragraph{Sparsity range.}
11	Our experiments span $s \in \{0.15, 0.20, 0.25, 0.30\}$. More extreme sparsity ($s > 0.50$) may exhibit qualitatively different interaction dynamics. We do not report inference throughput or latency measurements, which are necessary for a complete deployment analysis but orthogonal to our severity characterization. Extended limitations in Appendix~\ref{app:limitations}.
12	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250",
  "uuid": "e29a2091-c99d-4f9e-8a83-05fedc407886",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/limitations.tex",
      "content": "\\paragraph{Model scale and architecture.}\nAll experiments are conducted at the 7--8B parameter scale. Whether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested. Preliminary cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \\S\\ref{sec:cross-arch}) partially confirms the qualitative pattern beyond the Qwen2 architecture---monotonically increasing $d_z$ with within-importance phase gradient $\\sim$1.0---but with substantially weaker interaction magnitude ($\\sim$1/40 of DeepSeek) and mixed statistical evidence (only $s{=}0.30$ significant after Bonferroni correction). The pattern has been tested on two architecture families (Qwen2ForCausalLM, LlamaForCausalLM); comprehensive validation across more diverse architectures (e.g., Mistral, multi-latent attention) and larger scales is needed for full generalization claims.\n\n\\paragraph{Task coverage.}\nWe evaluate exclusively on MATH-500, a mathematical reasoning benchmark. Different reasoning tasks---code generation, commonsense reasoning, multi-hop question answering---may induce different phase structures with different sparsity distributions, potentially altering the severity gradient profile.\n\n\\paragraph{Mechanism.}\nThe discrimination collapse mechanism is supported by correlational evidence (consistent Gini/CV reduction across all conditions); causal validation through controlled entropy manipulation is needed. The entropy redistribution component replicates on only 2/4 Qwen conditions, suggesting model-specific factors.\n\n\\paragraph{Sparsity range.}\nOur experiments span $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$. More extreme sparsity ($s > 0.50$) may exhibit qualitatively different interaction dynamics. We do not report inference throughput or latency measurements, which are necessary for a complete deployment analysis but orthogonal to our severity characterization. Extended limitations in Appendix~\\ref{app:limitations}.\n",
      "numLines": 12,
      "startLine": 1,
      "totalLines": 12
    }
  }
}
```

</details>

---

### Assistant

_source line 42_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data I need. Let me compile the comprehensive audit. Let me count all placeholders and hardcoded values systematically.

### \placeholder{} instances:

1. **abstract.tex:8** — `\placeholder{}` — QW rand s030 Δ̃
2. **results.tex:71** — `\placeholder{NULL_PCT}` — Qwen mid-phase null rate %
3. **results.tex:86** — `\placeholder{N_LLAMA}` — LLaMA n paired problems
4. **results.tex:92** — 4× `\placeholder{}` — LLaMA s=0.15 row (Δ̃, CI_lo, CI_hi, p)


5. **results.tex:93** — 4× `\placeholder{}` — LLaMA s=0.20 row
6. **results.tex:94** — 4× `\placeholder{}` — LLaMA s=0.25 row
7. **results.tex:95** — 5× `\placeholder{}` — LLaMA s=0.30 row (extra bold)
8. **discussion.tex:10** — `\placeholder{ORACLE_PCT}`, `\placeholder{ORACLE_P}`, `\placeholder{HEUR_PCT}`, `\placeholder{HEUR_P}` — C5b
9. **discussion.tex:15** — `\placeholder{}` — LLaMA random Wilcoxon p
10. **appendix_moved.tex:30** — `\placeholder{NULL_PCT}` — Qwen null rate %
11. **appendix_moved.tex:35** — `\placeholder{N_QW}` — Qwen total n
12. **appendix_moved.tex:41** — 4× `\placeholder{}` — Qwen effective-n High row
13. **appendix_moved.tex:42** — 4× `\placeholder{}` — Qwen effective-n Mid row
14. **appendix_moved.tex:43** — 4× `\placeholder{}` — Qwen effective-n Low row
15. **appendix_moved.tex:73** — 2× `\placeholder{}` — per-problem concordance ρ,

I'm tracking down the remaining placeholders across the results, discussion, and appendix sections—mostly numerical values for the LLaMA and Qwen model comparisons, statistical tests, and concordance metrics that need to be filled in. Now I'm tallying up all the placeholder instances across each file to get a complete count—going through results.tex, discussion.tex, and the appendices to sum everything up. I've found 48 placeholder instances total across the files. Now I'm cross-referencing the existing checklist against what I actually found in the files. The checklist covers all the main sections, but I need to verify limitations.tex since it wasn't included. Looking at that file, I found a ratio comparing to DeepSeek that will need updating, along with some LLaMA-specific values that remain unchanged. Let me examine this more carefully to see if that ratio actually shifts indirectly based on other updates.

I'm also checking appendix_disc_analysis.tex for any values that depend on the main results—there are several Gini coefficients and threshold values that reference Table 2 and may need revision depending on what changes there.

Looking at the checklist against what I'm finding, most of these updates are already accounted for, but limitations.tex has a reference to the DeepSeek-to-LLaMA ratio that wasn't explicitly flagged before. I should also verify whether discussion.tex still contains placeholder text for the C5b pilot that needs to be addressed.

Actually, I'm noticing something important — there are several placeholder instances in discussion.tex and results.tex that aren't on the checklist at all. The C5b pilot experiment has unfilled placeholders for oracle and heuristic percentages and p-values, and there's also a missing Wilcoxon p-value for LLaMA in results.tex. These aren't tied to the n=50→n=500 upgrade, but they're still unresolved placeholders that need attention.

Now I'm going to systematically go through each file to count all the hardcoded n=50 values and make sure the existing checklist is complete, then compile everything into a comprehensive audit document.

Generating audit document...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250",
  "uuid": "e612d1c6-4eb5-4b24-ac48-48d0ddee4dad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UuYWrFoiY2bo3sEVfGCY8R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5115,
      "cache_read_input_tokens": 55754,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5115
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

_source line 43_

All files read. Now loading the MCP tools to save the output.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250",
  "uuid": "64c42f1b-0a07-4afb-9129-366b0dbd5a9a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UuYWrFoiY2bo3sEVfGCY8R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5115,
      "cache_read_input_tokens": 55754,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5115
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

_source line 44_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01RYuf2UWbT545Km1fpsjXAM`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__read_project_file",
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
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250",
  "uuid": "4774a2a9-e8ca-45a4-a26e-63408802d9f1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UuYWrFoiY2bo3sEVfGCY8R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5115,
      "cache_read_input_tokens": 55754,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5115
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

_source line 45 · 2026-05-15T01:44:41.418Z_

<details><summary>↩ Tool result · `toolu_01RYuf2UWbT545Km1fpsjXAM`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
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
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250",
  "uuid": "2e34831f-23bf-42ed-8434-8c5dea927655",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__read_project_file"
    ],
    "query": "select:mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__read_project_file",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Runtime record

_source line 46_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1778812800,
    "rateLimitType": "five_hour",
    "overageStatus": "allowed",
    "overageResetsAt": 1778809200,
    "isUsingOverage": false
  },
  "uuid": "80e1748f-6897-4edb-bc66-c9fbe1d1c142",
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250"
}
```

---

### Assistant

_source line 47_

<details><summary>Logged reasoning block</summary>

```text
The save_project_file tool has a whitelist of writable files: memory.md, writing_plan.yaml, paper_framing.md. It says "Other files have dedicated tools." But the user wants me to save to `artifacts/paper_placeholder_audit.md`. This isn't in the whitelist, so I should use the Write tool directly to save the file to the artifacts directory.

Let me compile the full audit document now.

Let me carefully count all placeholders:

**abstract.tex:**
1. L8: `\placeholder{}` — QW rand s030 Δ̃


**results.tex:**
2. L71: `\placeholder{NULL_PCT}` — Qwen mid-phase null rate %
3. L81: `\placeholder{}` — LLaMA random Wilcoxon p
4. L86: `\placeholder{N_LLAMA}` — LLaMA n paired problems
5-8. L92: `\placeholder{}` × 4 — LLaMA s=0.15 (Δ̃, CI_lo, CI_hi, p)
9-12. L93: `\placeholder{}` × 4 — LLaMA s=0.20
13-16. L94: `\placeholder{}` × 4 — LLaMA s=0

.25
17-20. L95: `\placeholder{}` × 4 — LLaMA s=0.30 (Δ̃, CI_lo, CI_hi, p bold)

That gives me 16 placeholders across the four LLaMA sensitivity rows. Now I'm moving into the discussion section where I need to fill in the oracle recovery percentage and its corresponding Wilcoxon p-value, plus a few more metrics.

**discussion.tex:**
21. L10: `\placeholder{ORACLE_PCT}` — oracle recovery %
22. L10: `\placeholder{ORACLE_P}` — oracle Wilcoxon p
23. L10: `\placeholder{HEUR_PCT}` — heuristic recovery %
24. L10: `\placeholder{HEUR_P}` — heuristic Wilcoxon p
25. L15: `\placeholder{}` — LLaMA random Wilcoxon p

**appendix_moved.tex:**
26. L30: `\placeholder{NULL_PCT}` — Qwen null rate %
27. L35: `\placeholder{N_QW}` — Qwen total n
28-31. L41: `\placeholder{}` × 4 — Qwen effective-n High row
32-35. L42: `\placeholder{}` × 4 — Qwen effective-n Mid row
36-39. L43: `\placeholder{}` × 4 — Qwen effective-n Low row
40. L73: `\placeholder{}` — per-problem concordance ρ
41. L73: `\placeholder{}` — per-problem concordance p
42. L76: `\placeholder{}` — QW rand s030 Δ̃

**appendix_results.tex:**
43. L7: `\placeholder{}` — per-problem concordance ρ
44. L7: `\placeholder{}` — per-problem concordance p
45. L10: `\placeholder{}` — QW rand s030 Δ̃

**appendix_disc_analysis.tex:**
46. L14: `\placeholder{}` — QW rand s030 Δ̃
47. L49: `\placeholder{}` — QW rand s030 Δ̃

I'm seeing that QW rand s030 Δ̃ appears five times across different files, and NULL_PCT shows up twice. Let me organize these by the unique values I actually need to fill in.

Looking at the remaining placeholders, I've got the LLaMA table data spanning multiple cells, the Qwen effective-n table with its own set of values, and various statistical measures like the Wilcoxon p-values and concordance metrics scattered throughout. Now I'm ready to write out the comprehensive audit directly to the artifacts.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250",
  "uuid": "3e882aa4-6605-4130-ae50-7988c74ea3a6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017dKeA6Ff5PMEWveB3STLWw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2895,
      "cache_read_input_tokens": 60869,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2895
      },
      "output_tokens": 40,
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

_source line 48_

Now compiling the full audit. Let me write the output file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250",
  "uuid": "2c6dcbb0-7989-49f0-8756-e3b25b5822f2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017dKeA6Ff5PMEWveB3STLWw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2895,
      "cache_read_input_tokens": 60869,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2895
      },
      "output_tokens": 40,
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

_source line 49_

<details open><summary>🔧 Tool call — Write · `toolu_013i4csgJowYLz9AxwF2ZgTg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/paper_placeholder_audit.md",
  "content": "# Paper Placeholder & Hardcoded Value Audit\n\n> 审计日期: 2026-05-15\n> 论文路径: `artifacts/_project/paper/`\n> 对照文档: `artifacts/n500_paper_update_checklist.md`\n\n---\n\n## 一、\\placeholder{} 汇总 (48 处，10 个唯一数据源)\n\n### A. 命名 placeholder（6 处，4 个数据源）\n\n| # | 文件:行 | 内容 | 上下文 | 数据来源 |\n|---|---------|------|--------|----------|\n| 1 | results.tex:71 | `\\placeholder{NULL_PCT}` | Qwen mid-phase null rate，~X% of problems yield near-zero II | n=500 Qwen profiling数据 |\n| 2 | results.tex:86 | `\\placeholder{N_LLAMA}` | LLaMA cross-arch table caption: \"$n{=}\\placeholder{N\\_LLAMA}$ paired problems\" | c3_llama 实验（不变，但从未填入） |\n| 3 | appendix_moved.tex:30 | `\\placeholder{NULL_PCT}` | 同 #1 重复引用: \"null rate (\\placeholder{NULL\\_PCT}\\%)\" | 同 #1 |\n| 4 | appendix_moved.tex:35 | `\\placeholder{N_QW}` | Qwen effective-n table caption: \"$n_{\\text{total}} = \\placeholder{N\\_QW}$\" | n=500 Qwen 有效样本量 |\n| 5 | discussion.tex:10 | `\\placeholder{ORACLE_PCT}` | C5b pilot: \"oracle recovery reached \\placeholder{ORACLE\\_PCT}\\%\" | C5b 实验数据 |\n| 6 | discussion.tex:10 | `\\placeholder{ORACLE_P}` | C5b pilot: \"Wilcoxon $p = \\placeholder{ORACLE\\_P}$\" | C5b 实验数据 |\n| 7 | discussion.tex:10 | `\\placeholder{HEUR_PCT}` | C5b pilot: \"heuristic variant achieved \\placeholder{HEUR\\_PCT}\\% recovery\" | C5b 实验数据 |\n| 8 | discussion.tex:10 | `\\placeholder{HEUR_P}` | C5b pilot: \"$p = \\placeholder{HEUR\\_P}$\" | C5b 实验数据 |\n\n### B. 匿名 placeholder — QW rand s030 Δ̃（5 处，1 个数据源）\n\n| # | 文件:行 | 上下文 |\n|---|---------|--------|\n| 9 | abstract.tex:8 | \"negligible median difference ($\\widetilde{\\Delta} = \\placeholder{}$)\" |\n| 10 | appendix_moved.tex:76 | \"negligible median difference ($\\widetilde{\\Delta} = \\placeholder{}$, CI spans zero)\" |\n| 11 | appendix_results.tex:10 | \"negligible median difference ($\\widetilde{\\Delta} = \\placeholder{}$, CI spans zero)\" |\n| 12 | appendix_disc_analysis.tex:14 | \"negligible effect size ($\\widetilde{\\Delta} = \\placeholder{}$)\" |\n| 13 | appendix_disc_analysis.tex:49 | \"negligible effect size ($\\widetilde{\\Delta} = \\placeholder{}$, bootstrap CI spanning zero)\" |\n\n数据来源: experiment_summary_table.json → QW rand s030 median_diff\n\n### C. 匿名 placeholder — LLaMA random Wilcoxon p（2 处，1 个数据源）\n\n| # | 文件:行 | 上下文 |\n|---|---------|--------|\n| 14 | results.tex:81 | \"Wilcoxon $p < \\placeholder{}$ at $s{=}0.30$\" |\n| 15 | discussion.tex:15 | \"random pruning also exhibits a non-trivial phase gradient (Wilcoxon $p < \\placeholder{}$)\" |\n\n数据来源: c3_llama 实验（LLaMA 不重跑，数据已有但未填入）\n\n### D. 匿名 placeholder — Per-problem concordance ρ, p（4 处，1 个数据源）\n\n| # | 文件:行 | 上下文 |\n|---|---------|--------|\n| 16 | appendix_moved.tex:73 | \"median $\\rho = \\placeholder{}$, $p = \\placeholder{}$\" |\n| 17 | appendix_results.tex:7 | \"median $\\rho = \\placeholder{}$, $p = \\placeholder{}$\" |\n\n数据来源: cross_model_analysis.json (注释中已有: mean_rho=-0.107, p=0.926，但正文未填入)\n\n### E. 匿名 placeholder — LLaMA cross-arch table（16 处）\n\n| # | 文件:行 | 内容 |\n|---|---------|------|\n| 18-21 | results.tex:92 | s=0.15: Δ̃, CI_lo, CI_hi, p_Bonf |\n| 22-25 | results.tex:93 | s=0.20: Δ̃, CI_lo, CI_hi, p_Bonf |\n| 26-29 | results.tex:94 | s=0.25: Δ̃, CI_lo, CI_hi, p_Bonf |\n| 30-33 | results.tex:95 | s=0.30: Δ̃, CI_lo, CI_hi, p_Bonf |\n\n数据来源: c3_llama 实验（LLaMA 不重跑，数据已有但未填入）\n\n### F. 匿名 placeholder — Qwen effective-n table（12 处）\n\n| # | 文件:行 | 内容 |\n|---|---------|------|\n| 34-37 | appendix_moved.tex:41 | High phase: s=0.15, 0.20, 0.25, 0.30 |\n| 38-41 | appendix_moved.tex:42 | Mid phase: s=0.15, 0.20, 0.25, 0.30 |\n| 42-45 | appendix_moved.tex:43 | Low phase: s=0.15, 0.20, 0.25, 0.30 |\n\n数据来源: n=500 Qwen profiling（需从 n=500 数据计算 |II| > 0.001 的问题数）\n\n### Placeholder 汇总\n\n| 数据源 | 处数 | n=500 后需更新? |\n|--------|------|-----------------|\n| QW rand s030 Δ̃ | 5 | 是（n=500 重跑） |\n| NULL_PCT (Qwen null rate) | 2 | 是（n=500 重算） |\n| N_QW (Qwen total n) | 1 | 是 |\n| N_LLAMA (LLaMA n) | 1 | 否（LLaMA 不重跑，但需填入已有数据） |\n| LLaMA table 16 cells | 16 | 否（数据已有，需填入） |\n| LLaMA random Wilcoxon p | 2 | 否（数据已有，需填入） |\n| Per-problem concordance ρ, p | 4 | 是（n=500 重算） |\n| Qwen effective-n table 12 cells | 12 | 是（n=500 重算） |\n| C5b pilot (ORACLE/HEUR) | 4 | 独立于 n=500，取决于 C5b 实验 |\n| **合计** | **48** | |\n\n---\n\n## 二、硬编码数值汇总（~120 处）\n\n### 样本量文本 \"50\"→\"500\"（8 处）\n\n| # | 文件:行 | 当前值 | 需要更新? |\n|---|---------|--------|-----------|\n| 1 | abstract.tex:6 | `50 MATH-500 problems` | 是→500 |\n| 2 | methodology.tex:10 | `50 problems stratified from MATH-500` | 是→500 |\n| 3 | results.tex:13 | `$n{=}50$ MATH-500 problems` (Table 1 caption) | 是→500 |\n| 4 | results.tex:34 | `medians across 50 problems` (Table 2 caption) | 是→500 |\n| 5 | appendix_moved.tex:26 | `Four of the 50 problems are excluded` | 是→新排除数/总数 |\n| 6 | appendix_moved.tex:26 | `$n{=}46$ valid problems for Qwen (vs.\\ $n{=}49$ for DeepSeek)` | 是→新有效n |\n| 7 | appendix_moved.tex:93 (tab:permutation caption) | `$n{=}49$, $10{,}000$ permutations` | 是→新n |\n| 8 | appendix_disc_analysis.tex:45 | `$n{=}49$...and $n{=}46$ for Qwen (4 excluded)` | 是→新n |\n\n### Table 1: Aggregate II (results.tex:10-23) — 10 处\n\n| # | 文件:行 | 当前值 | 数据来源 | 需要更新? |\n|---|---------|--------|----------|-----------|\n| 9 | results.tex:19 | `0.39 & 1.48 & 7.16 & 14.59` | DS imp median_diff | 是 |\n| 10 | results.tex:20 | `0.01 & $-$0.02 & 0.54 & 1.54` | DS rand median_diff | 是 |\n| 11 | results.tex:8 | `$0.39$...$14.59$...37×` | 同上 + 比率重算 | 是 |\n| 12 | results.tex:8 | `$-0.02$ to $1.54$` | DS rand range | 是 |\n\n### Table 2: Per-phase II (results.tex:31-53) — 40 处 (8行×5列)\n\n| # | 文件:行 | 行标签 | 当前值 (II_high, II_mid, II_low, Δ, G) | 需要更新? |\n|---|---------|--------|----------------------------------------|-----------|\n| 13 | results.tex:40 | 0.15 Imp | 0.006, 0.081, 0.398, 0.39, 69 | 是 |\n| 14 | results.tex:41 | 0.15 Rand | 0.093, 0.097, 0.103, 0.01, 1.1 | 是 |\n| 15 | results.tex:43 | 0.20 Imp | 0.015, 0.203, 1.496, 1.48, 103 | 是 |\n| 16 | results.tex:44 | 0.20 Rand | 0.292, 0.350, 0.276, −0.02, 0.9 | 是 |\n| 17 | results.tex:46 | 0.25 Imp | 0.032, 1.118, 7.196, 7.16, 222 | 是 |\n| 18 | results.tex:47 | 0.25 Rand | 0.818, 0.932, 1.363, 0.54, 1.7 | 是 |\n| 19 | results.tex:49 | 0.30 Imp | 0.053, 2.283, 14.639, 14.59, 274 | 是 |\n| 20 | results.tex:50 | 0.30 Rand | 2.503, 2.592, 4.041, 1.54, 1.6 | 是 |\n\n### Table 3: Cohen's d (results.tex:108-124) — 16 处\n\n| # | 文件:行 | 当前值 | 需要更新? |\n|---|---------|--------|-----------|\n| 21 | results.tex:117 | DS: 0.44, 0.32 [0.20, 0.47]; QW: 0.28, 0.05 [−0.01, 0.11]^ns | 是 |\n| 22 | results.tex:118 | DS: 0.52, 1.15 [0.66, 1.26]; QW: 0.55, 0.21 [0.07, 0.40] | 是 |\n| 23 | results.tex:119 | DS: 0.68, 3.97 [2.83, 5.29]; QW: 0.89, 1.11 [0.61, 1.47] | 是 |\n| 24 | results.tex:120 | DS: 0.80, 9.94 [8.39, 16.65]; QW: 1.02, 2.62 [1.72, 3.65] | 是 |\n\n### Table: Cross-model (appendix_moved.tex:50-63) — 8 处\n\n| # | 文件:行 | 当前值 | 需要更新? |\n|---|---------|--------|-----------|\n| 25 | appendix_moved.tex:59 | DS: 0.39, 1.48, 7.16, 14.59 | 是 |\n| 26 | appendix_moved.tex:60 | QW: 0.04, 0.23, 1.27, 2.94 | 是 |\n\n### Table: Permutation test (appendix_moved.tex:90-105) — 12 处\n\n| # | 文件:行 | 当前值 | 需要更新? |\n|---|---------|--------|-----------|\n| 27 | appendix_moved.tex:99 | s015: 0.37, [0.19, 0.62], 0.0032 | 是 |\n| 28 | appendix_moved.tex:100 | s020: 0.97, [0.69, 1.49], <0.001 | 是 |\n| 29 | appendix_moved.tex:101 | s025: 3.34, [1.66, 6.64], <0.001 | 是 |\n| 30 | appendix_moved.tex:102 | s030: 9.85, [6.70, 16.29], <0.001 | 是 |\n\n### Table: Discrimination metrics (appendix_moved.tex:123-143) — 16 处\n\n| # | 文件:行 | 当前值 | 需要更新? |\n|---|---------|--------|-----------|\n| 31 | appendix_moved.tex:132 | DS 0.15: −0.030, −0.56 | 是 |\n| 32 | appendix_moved.tex:133 | DS 0.20: −0.040, −0.77 | 是 |\n| 33 | appendix_moved.tex:134 | DS 0.25: −0.065, −1.29 | 是 |\n| 34 | appendix_moved.tex:135 | DS 0.30: −0.081, −1.66 | 是 |\n| 35 | appendix_moved.tex:137 | QW 0.15: −0.010, −0.05 | 是 |\n| 36 | appendix_moved.tex:138 | QW 0.20: −0.012, −0.21 | 是 |\n| 37 | appendix_moved.tex:139 | QW 0.25: −0.010, −1.49 | 是 |\n| 38 | appendix_moved.tex:140 | QW 0.30: −0.020, −1.14 | 是 |\n\n### Table: Entropy deltas (appendix_moved.tex:163-183) — 8 处\n\n| # | 文件:行 | 当前值 | 需要更新? |\n|---|---------|--------|-----------|\n| 39 | appendix_moved.tex:171 | DS 0.15: −0.040 | 是 |\n| 40 | appendix_moved.tex:172 | DS 0.20: −0.047 | 是 |\n| 41 | appendix_moved.tex:173 | DS 0.25: −0.045 | 是 |\n| 42 | appendix_moved.tex:174 | DS 0.30: −0.044 | 是 |\n| 43 | appendix_moved.tex:177 | QW 0.15: −0.073 | 是 |\n| 44 | appendix_moved.tex:178 | QW 0.20: −0.076 | 是 |\n| 45 | appendix_moved.tex:179 | QW 0.25: +0.045 | 是 |\n| 46 | appendix_moved.tex:180 | QW 0.30: −0.007 | 是 |\n\n### 内联统计声明 — abstract.tex（~12 处）\n\n| # | 文件:行 | 当前值 | 数据来源 | 需要更新? |\n|---|---------|--------|----------|-----------|\n| 47 | abstract.tex:7 | `$0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$` | DS imp median_diff | 是 |\n| 48 | abstract.tex:7 | `$d_z$ growing from $0.44$ (small) to $0.80$ (large)` | cohens_d_bf16.json | 是 |\n| 49 | abstract.tex:7 | `$p < 0.005$` | permutation_test_results.json | 是（验证阈值） |\n| 50 | abstract.tex:8 | `7/8 conditions` | 重统计 random PASS/FAIL | 是（可能→8/8） |\n| 51 | abstract.tex:8 | `$p{=}0.012$` | QW rand s030 | 是 |\n| 52 | abstract.tex:9 | `$0.032$ vs.\\ $0.818$` | DS s025 high-phase | 是 |\n| 53 | abstract.tex:9 | `$7.196$ vs.\\ $1.363$` | DS s025 low-phase | 是 |\n| 54 | abstract.tex:10 | `$d_z \\geq 0.55$` | QW s020 d_z | 是 |\n| 55 | abstract.tex:10 | `Spearman $\\rho = 1.0$` | cross_model_analysis.json | 是（验证） |\n| 56 | abstract.tex:10 | `$p = 0.043$` | cross_model_analysis.json | 是 |\n| 57 | abstract.tex:10 | `${\\sim}$1/40 the absolute magnitude` | **间接**：DS Δ̃变→比率重算 | 是 |\n| 58 | abstract.tex:10 | `$0.020 \\to 0.356$` | c3_llama（不变） | 否 |\n\n### 内联统计声明 — introduction.tex（~5 处）\n\n| # | 文件:行 | 当前值 | 需要更新? |\n|---|---------|--------|-----------|\n| 59 | introduction.tex:14 | `$0.39$...$14.59$` | 是 |\n| 60 | introduction.tex:14 | `$d_z$: $0.44 \\to 0.80$` | 是 |\n| 61 | introduction.tex:14 | `$p < 0.005$` | 是（验证） |\n| 62 | introduction.tex:15 | `$d_z \\geq 0.55$` | 是 |\n| 63 | introduction.tex:15 | `$\\sim$1/40 the magnitude` | 是（间接） |\n| 64 | introduction.tex:16 | `7/8 conditions non-significant` | 是（可能→8/8） |\n\n### 内联统计声明 — methodology.tex（2 处）\n\n| # | 文件:行 | 当前值 | 需要更新? |\n|---|---------|--------|-----------|\n| 65 | methodology.tex:18 | `mean/median ratios up to 43:1` | 是 |\n| 66 | methodology.tex:22 | `$p_{\\text{Bonf}} < 0.005$` | 是（验证） |\n\n### 内联统计声明 — results.tex 正文（~20 处）\n\n| # | 文件:行 | 当前值 | 需要更新? |\n|---|---------|--------|-----------|\n| 67 | results.tex:29 | `$69{\\times}$...$274{\\times}$` | 是 |\n| 68 | results.tex:29 | `$0.006$ to $0.053$` | 是 |\n| 69 | results.tex:29 | `$G \\approx 0.9$--$1.7{\\times}$` | 是 |\n| 70 | results.tex:58 | `$69{\\times}$ to $274{\\times}$` (fig caption) | 是 |\n| 71 | results.tex:66 | `$0.032$ vs.\\ $0.818$` | 是 |\n| 72 | results.tex:66 | `$7.196$ vs.\\ $1.363$---a $5.3{\\times}$` | 是 |\n| 73 | results.tex:71 | `$0.04$...$2.94$...${\\sim}1/5$` | 是 |\n| 74 | results.tex:71 | `$d_z \\geq 0.55$; Spearman $\\rho = 1.0$; $p = 0.043$` | 是 |\n| 75 | results.tex:71 | `$d_z{=}0.28$, CI includes zero` | 是 |\n| 76 | results.tex:77 | `$0.37$...$9.85$` | 是 |\n| 77 | results.tex:81 | `${\\sim}40{\\times}$ smaller...and ${\\sim}7{\\times}$ smaller` | 是（间接） |\n| 78 | results.tex:106 | `$d_z{=}0.44$ (small) to $d_z{=}0.80$ (large)` | 是 |\n| 79 | results.tex:106 | `$d_z{=}0.28$...CI includes zero...$d_z \\geq 0.55$` | 是 |\n| 80 | results.tex:106 | `$d_z{=}0.89$/$1.02$ vs.\\ $0.68$/$0.80$` | 是 |\n\n### 内联统计声明 — analysis.tex（~5 处）\n\n| # | 文件:行 | 当前值 | 需要更新? |\n|---|---------|--------|-----------|\n| 81 | analysis.tex:4 | `$0.030$--$0.081$ (DeepSeek) and $0.010$--$0.020$ (Qwen)` | 是 |\n| 82 | analysis.tex:4 | `16 conditions` | 是（验证） |\n| 83 | analysis.tex:6 | `$\\Delta\\mathcal{H} \\in [-0.047, -0.040]$` | 是 |\n| 84 | analysis.tex:6 | `$\\Delta\\mathcal{H} = +0.045$` | 是 |\n| 85 | analysis.tex:6 | `22 of 30 problems` | 是 |\n\n### 内联统计声明 — discussion.tex（~7 处）\n\n| # | 文件:行 | 当前值 | 需要更新? |\n|---|---------|--------|-----------|\n| 86 | discussion.tex:5 | `$69$--$274{\\times}$` | 是 |\n| 87 | discussion.tex:5 | `$0.032$ vs.\\ $0.818$` | 是 |\n| 88 | discussion.tex:5 | `$7.196$ vs.\\ $1.363$` | 是 |\n| 89 | discussion.tex:5 | `$G \\approx 1$` | 是（验证） |\n| 90 | discussion.tex:15 | `${\\sim}40{\\times}$...${\\sim}7{\\times}$` | 是（间接） |\n| 91 | discussion.tex:15 | `$d_z \\geq 1.0$` | 否（LLaMA 不变） |\n\n### 内联统计声明 — conclusion.tex（~5 处）\n\n| # | 文件:行 | 当前值 | 需要更新? |\n|---|---------|--------|-----------|\n| 92 | conclusion.tex:4 | `$69{\\times}$ to $274{\\times}$` | 是 |\n| 93 | conclusion.tex:4 | `$d_z$: $0.44 \\to 0.80$` | 是 |\n| 94 | conclusion.tex:4 | `7/8 conditions non-significant` | 是（可能→8/8） |\n| 95 | conclusion.tex:4 | `$d_z \\geq 0.55$` | 是 |\n| 96 | conclusion.tex:4 | `$\\sim$1/40 the magnitude` | 是（间接） |\n\n### 内联统计声明 — appendix.tex（1 处）\n\n| # | 文件:行 | 当前值 | 需要更新? |\n|---|---------|--------|-----------|\n| 97 | appendix.tex:38 | `$G_{\\times} = 58$--$241{\\times}$` | 是 |\n\n### 内联统计声明 — appendix_moved.tex 正文（~12 处）\n\n| # | 文件:行 | 当前值 | 需要更新? |\n|---|---------|--------|-----------|\n| 98 | appendix_moved.tex:11 | `$0.032$ vs.\\ $0.818$`...`$7.196$ vs.\\ $1.363$---a $5.3{\\times}$` | 是 |\n| 99 | appendix_moved.tex:11 | `$3.9{\\times}$...$5.4{\\times}$...$5.3{\\times}$...$3.6{\\times}$` | 是 |\n| 100 | appendix_moved.tex:16 | `$5.3{\\times}$` (fig caption) | 是 |\n| 101 | appendix_moved.tex:26 | `Four of the 50 problems` | 是 |\n| 102 | appendix_moved.tex:48 | `${\\sim}1/5$` (fig caption) | 是 |\n| 103 | appendix_moved.tex:68 | `one-fifth` | 是 |\n| 104 | appendix_moved.tex:84 | `mean/median ratios...$1.2{\\times}$...$1.6{\\times}$` DS | 是 |\n| 105 | appendix_moved.tex:84 | `$1.1{\\times}$ to $1.4{\\times}$` QW | 是 |\n| 106 | appendix_moved.tex:86 | `$99.92$th percentile...$p_{\\text{Bonf}} = 0.0032$` | 是 |\n| 107 | appendix_moved.tex:88 | `$0.37$...$9.85$...CI lower bound ($0.19 \\to 0.69 \\to 1.66 \\to 6.70$)` | 是 |\n| 108 | appendix_moved.tex:53 (comment) | `mean $\\rho = -0.11$, $p = 0.926$` | 已在 placeholder 中 |\n\n### 内联统计声明 — appendix_disc_analysis.tex（~10 处）\n\n| # | 文件:行 | 当前值 | 需要更新? |\n|---|---------|--------|-----------|\n| 109 | appendix_disc_analysis.tex:4 | `$-0.031$ to $-0.073$; Qwen: $-0.019$ to $-0.045$` | 是 |\n| 110 | appendix_disc_analysis.tex:11 | `$\\widetilde{\\mathrm{II}}_{\\text{high}} < 0.06$` | 是 |\n| 111 | appendix_disc_analysis.tex:11 | `$s = 0.35$, high-phase II rises to $0.105$` | 否（s035 补充实验不重跑） |\n| 112 | appendix_disc_analysis.tex:14 | `7/8...Qwen $s{=}0.30$, $p{=}0.012$...$d_z{=}{-}0.04$` | 是 |\n| 113 | appendix_disc_analysis.tex:45 | `$n{=}49$...$n{=}46$` | 是（同 #8） |\n| 114 | appendix_disc_analysis.tex:46 | `mean/median ratio ${\\sim}1.6{:}1$...mean_diff=22.94, median_diff=14.59` | 是 |\n| 115 | appendix_disc_analysis.tex:47 | CIs: `[0.19, 0.62]...[0.69, 1.49]...[1.66, 6.64]...[6.70, 16.29]` | 是 |\n| 116 | appendix_disc_analysis.tex:49 | `$p{=}0.012$...$d_z{=}{-}0.04$...d=-0.035` | 是 |\n| 117 | appendix_disc_analysis.tex:57 | `$\\Delta$ growth rate $3.8{\\times} \\to 4.8{\\times} \\to 2.0{\\times}$` (comment) | 是（注释中的数据） |\n\n### 内联统计声明 — limitations.tex（1 处，新发现）\n\n| # | 文件:行 | 当前值 | 需要更新? |\n|---|---------|--------|-----------|\n| 118 | limitations.tex:2 | `$\\sim$1/40 of DeepSeek` | 是（间接：DS Δ̃变→比率重算） |\n\n---\n\n## 三、不需更新的值\n\n| 文件:行 | 当前值 | 原因 |\n|---------|--------|------|\n| results.tex:77 | `$n{=}49$ paired problems` | LLaMA 实验不重跑 |\n| results.tex:79 | `$[0.002, 0.043]$`, `$p_{\\text{Bonf}}{=}0.219$` 等 LLaMA 统计量 | LLaMA 数据不变 |\n| results.tex:79 | `$0.020 \\to 0.356$` LLaMA Δ̃ | LLaMA 数据不变 |\n| abstract.tex:10 | `$0.020 \\to 0.356$` LLaMA Δ̃ | LLaMA 数据不变 |\n| abstract.tex:10 | `$p_{\\text{Bonf}}{=}0.029$` LLaMA s030 | LLaMA 数据不变 |\n| discussion.tex:15 | `$d_z \\geq 1.0$` LLaMA within-importance d_z | LLaMA 数据不变 |\n| appendix_disc_analysis.tex:11 | `$s = 0.35$, high-phase II rises to $0.105$` | s035 补充实验不重跑 |\n| related_work.tex | 全文 | 无实验数据 |\n| background.tex | 全文 | 公式定义，无实验数据 |\n| limitations.tex (大部分) | 描述性限定语 | 无具体数值（除比率声明外） |\n| 所有 `\\cite{}` 引用 | — | 无变化 |\n\n**注意：LLaMA 绝对值不变，但 LLaMA 与 DS/QW 的比率声明需要重算（见间接影响）。**\n\n---\n\n## 四、间接影响：LLaMA 比率声明（4+1 处）\n\nLLaMA 数据不变（Δ̃_s030 = 0.356），但 DS/QW 的 Δ̃ 变化导致比率需重算：\n\n| # | 文件:行 | 当前声明 | 计算方法 |\n|---|---------|---------|----------|\n| 1 | abstract.tex:10 | `${\\sim}$1/40` | 新 DS s030 Δ̃ / 0.356 |\n| 2 | results.tex:81 | `${\\sim}40{\\times}$ smaller...and ${\\sim}7{\\times}$ smaller` | 新 DS/QW s030 Δ̃ / 0.356 |\n| 3 | discussion.tex:15 | `${\\sim}40{\\times}$...${\\sim}7{\\times}$` | 同上 |\n| 4 | conclusion.tex:4 | `$\\sim$1/40` | 同上 |\n| 5 | **limitations.tex:2** | `$\\sim$1/40 of DeepSeek` | 同上（**新发现，不在已有清单中**） |\n\n---\n\n## 五、条件性叙事更新\n\n### Qwen s015 决策点\n\nn=500 后 QW s015 Cohen's d CI 是否仍含零决定叙事方案：\n\n| 情况 | 影响位置数 | 操作 |\n|------|-----------|------|\n| CI 仍跨零 | 6 处 | 仅更新数值，保留 \"marginal at s015 / reliable at s≥0.20\" |\n| CI > 0 | 6 处 | 升级为 \"all four sparsity levels\"，删除 ^ns |\n\n影响文件: abstract.tex:10, introduction.tex:15, results.tex:71, results.tex:117, results.tex:122 (脚注), conclusion.tex:4\n\n### Random 7/8 vs 8/8 决策点\n\nn=500 后 QW rand s030 的 borderline PASS (p=0.012) 可能翻转为 FAIL：\n\n| 情况 | 影响位置数 | 操作 |\n|------|-----------|------|\n| 仍 PASS | 5 处 | 仅更新 p 值和 Δ̃ |\n| 翻转 FAIL | 5 处 | \"7/8\"→\"8/8\", \"3/4\"→\"4/4\", 删除 exception 叙事 |\n\n影响文件: abstract.tex:8, introduction.tex:16, conclusion.tex:4, appendix_disc_analysis.tex:14, appendix_results.tex:10\n\n---\n\n## 六、与已有规划文档的差异\n\n对照 `n500_paper_update_checklist.md`：\n\n### 已有清单覆盖的内容\n- §1 样本量文本替换: ✓ 完全覆盖\n- §2 Tables: ✓ 完全覆盖\n- §3 Figures: ✓ 完全覆盖（本审计不重复）\n- §4 内联统计声明: ✓ 基本覆盖\n- §5 Qwen s015 决策点: ✓ 完全覆盖\n- §6 附属统计量: ✓ 完全覆盖\n- §7 数据管道: ✓ 完全覆盖\n- §8 不需更新部分: ✓ 基本正确\n- §10 LLaMA 间接比率: ✓ 覆盖 4 处\n\n### **新发现（不在已有清单中）**\n\n| # | 发现 | 位置 | 说明 |\n|---|------|------|------|\n| **NEW-1** | **limitations.tex:2 的 LLaMA 比率声明** | `$\\sim$1/40 of DeepSeek` | 已有清单 §10 遗漏了 limitations.tex，仅列出 abstract/results/discussion/conclusion |\n| **NEW-2** | **C5b pilot placeholders 未纳入** | discussion.tex:10 的 4 个 `\\placeholder{ORACLE_*/HEUR_*}` | 已有清单 §11 仅确认 \"无需改\"，但这 4 个 placeholder 确实存在且需要填入 C5b 实验数据 |\n| **NEW-3** | **appendix_moved.tex:16 fig caption** | `$5.3{\\times}$` crossover 倍数 | 已有清单中 crossover 倍数仅列 L11，遗漏了 fig3 caption L16 |\n| **NEW-4** | **appendix_moved.tex:48/68 \"one-fifth\" 比率** | fig5 caption + 正文 | 已有清单提到了 fig5 caption 中的 \"one-fifth\" 但内联引用位置不完整 |\n\n### 已有清单的数量统计 vs 实际\n\n| 类别 | 清单统计 | 实际统计 |\n|------|---------|---------|\n| 样本量文本 | 8 处 | 8 处 ✓ |\n| 表格单元格 | ~80 | ~110（含 placeholder 表格 28 cells） |\n| 图表 PDF | 5 | 5 ✓ |\n| 内联统计数值 | ~60 | ~72 处 |\n| Qwen s015 叙事 | 6 处 | 6 处 ✓ |\n| 7/8 vs 8/8 叙事 | 5 处 | 5 处 ✓ |\n| LLaMA 间接比率 | 4 处 | **5 处**（+limitations.tex） |\n| Placeholder 总数 | 未统计 | **48 处** |\n\n---\n\n## 七、全量统计\n\n| 类别 | 数量 |\n|------|------|\n| `\\placeholder{}` 实例 | 48 |\n| 其中 n=500 后需更新 | 24 |\n| 其中 LLaMA 数据（已有未填） | 19 |\n| 其中 C5b 独立实验 | 4 |\n| 其中 per-problem concordance（注释有数据未填） | 4（注释中有 ρ=-0.107, p=0.926） |\n| 硬编码数值需更新 | ~118 |\n| 间接比率重算 | 5 |\n| 条件性叙事更新 | 11（两个决策点） |\n| 图表重新生成 | 5 PDF |\n| **总替换位置** | **~170+** |\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250",
  "uuid": "0fc8fa3a-25d4-4506-8a78-50f2965a6993",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017dKeA6Ff5PMEWveB3STLWw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2895,
      "cache_read_input_tokens": 60869,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2895
      },
      "output_tokens": 40,
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

### Runtime record

_source line 50_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1778812800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "253c68ea-2694-46c1-83cf-51eb71343ee9",
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250"
}
```

---

### Tool result

_source line 51 · 2026-05-15T01:47:47.743Z_

<details><summary>↩ Tool result · `toolu_013i4csgJowYLz9AxwF2ZgTg`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/paper_placeholder_audit.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250",
  "uuid": "8267083f-1cb4-43ab-bf66-f12ea74599bd",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/paper_placeholder_audit.md",
    "content": "# Paper Placeholder & Hardcoded Value Audit\n\n> 审计日期: 2026-05-15\n> 论文路径: `artifacts/_project/paper/`\n> 对照文档: `artifacts/n500_paper_update_checklist.md`\n\n---\n\n## 一、\\placeholder{} 汇总 (48 处，10 个唯一数据源)\n\n### A. 命名 placeholder（6 处，4 个数据源）\n\n| # | 文件:行 | 内容 | 上下文 | 数据来源 |\n|---|---------|------|--------|----------|\n| 1 | results.tex:71 | `\\placeholder{NULL_PCT}` | Qwen mid-phase null rate，~X% of problems yield near-zero II | n=500 Qwen profiling数据 |\n| 2 | results.tex:86 | `\\placeholder{N_LLAMA}` | LLaMA cross-arch table caption: \"$n{=}\\placeholder{N\\_LLAMA}$ paired problems\" | c3_llama 实验（不变，但从未填入） |\n| 3 | appendix_moved.tex:30 | `\\placeholder{NULL_PCT}` | 同 #1 重复引用: \"null rate (\\placeholder{NULL\\_PCT}\\%)\" | 同 #1 |\n| 4 | appendix_moved.tex:35 | `\\placeholder{N_QW}` | Qwen effective-n table caption: \"$n_{\\text{total}} = \\placeholder{N\\_QW}$\" | n=500 Qwen 有效样本量 |\n| 5 | discussion.tex:10 | `\\placeholder{ORACLE_PCT}` | C5b pilot: \"oracle recovery reached \\placeholder{ORACLE\\_PCT}\\%\" | C5b 实验数据 |\n| 6 | discussion.tex:10 | `\\placeholder{ORACLE_P}` | C5b pilot: \"Wilcoxon $p = \\placeholder{ORACLE\\_P}$\" | C5b 实验数据 |\n| 7 | discussion.tex:10 | `\\placeholder{HEUR_PCT}` | C5b pilot: \"heuristic variant achieved \\placeholder{HEUR\\_PCT}\\% recovery\" | C5b 实验数据 |\n| 8 | discussion.tex:10 | `\\placeholder{HEUR_P}` | C5b pilot: \"$p = \\placeholder{HEUR\\_P}$\" | C5b 实验数据 |\n\n### B. 匿名 placeholder — QW rand s030 Δ̃（5 处，1 个数据源）\n\n| # | 文件:行 | 上下文 |\n|---|---------|--------|\n| 9 | abstract.tex:8 | \"negligible median difference ($\\widetilde{\\Delta} = \\placeholder{}$)\" |\n| 10 | appendix_moved.tex:76 | \"negligible median difference ($\\widetilde{\\Delta} = \\placeholder{}$, CI spans zero)\" |\n| 11 | appendix_results.tex:10 | \"negligible median difference ($\\widetilde{\\Delta} = \\placeholder{}$, CI spans zero)\" |\n| 12 | appendix_disc_analysis.tex:14 | \"negligible effect size ($\\widetilde{\\Delta} = \\placeholder{}$)\" |\n| 13 | appendix_disc_analysis.tex:49 | \"negligible effect size ($\\widetilde{\\Delta} = \\placeholder{}$, bootstrap CI spanning zero)\" |\n\n数据来源: experiment_summary_table.json → QW rand s030 median_diff\n\n### C. 匿名 placeholder — LLaMA random Wilcoxon p（2 处，1 个数据源）\n\n| # | 文件:行 | 上下文 |\n|---|---------|--------|\n| 14 | results.tex:81 | \"Wilcoxon $p < \\placeholder{}$ at $s{=}0.30$\" |\n| 15 | discussion.tex:15 | \"random pruning also exhibits a non-trivial phase gradient (Wilcoxon $p < \\placeholder{}$)\" |\n\n数据来源: c3_llama 实验（LLaMA 不重跑，数据已有但未填入）\n\n### D. 匿名 placeholder — Per-problem concordance ρ, p（4 处，1 个数据源）\n\n| # | 文件:行 | 上下文 |\n|---|---------|--------|\n| 16 | appendix_moved.tex:73 | \"median $\\rho = \\placeholder{}$, $p = \\placeholder{}$\" |\n| 17 | appendix_results.tex:7 | \"median $\\rho = \\placeholder{}$, $p = \\placeholder{}$\" |\n\n数据来源: cross_model_analysis.json (注释中已有: mean_rho=-0.107, p=0.926，但正文未填入)\n\n### E. 匿名 placeholder — LLaMA cross-arch table（16 处）\n\n| # | 文件:行 | 内容 |\n|---|---------|------|\n| 18-21 | results.tex:92 | s=0.15: Δ̃, CI_lo, CI_hi, p_Bonf |\n| 22-25 | results.tex:93 | s=0.20: Δ̃, CI_lo, CI_hi, p_Bonf |\n| 26-29 | results.tex:94 | s=0.25: Δ̃, CI_lo, CI_hi, p_Bonf |\n| 30-33 | results.tex:95 | s=0.30: Δ̃, CI_lo, CI_hi, p_Bonf |\n\n数据来源: c3_llama 实验（LLaMA 不重跑，数据已有但未填入）\n\n### F. 匿名 placeholder — Qwen effective-n table（12 处）\n\n| # | 文件:行 | 内容 |\n|---|---------|------|\n| 34-37 | appendix_moved.tex:41 | High phase: s=0.15, 0.20, 0.25, 0.30 |\n| 38-41 | appendix_moved.tex:42 | Mid phase: s=0.15, 0.20, 0.25, 0.30 |\n| 42-45 | appendix_moved.tex:43 | Low phase: s=0.15, 0.20, 0.25, 0.30 |\n\n数据来源: n=500 Qwen profiling（需从 n=500 数据计算 |II| > 0.001 的问题数）\n\n### Placeholder 汇总\n\n| 数据源 | 处数 | n=500 后需更新? |\n|--------|------|-----------------|\n| QW rand s030 Δ̃ | 5 | 是（n=500 重跑） |\n| NULL_PCT (Qwen null rate) | 2 | 是（n=500 重算） |\n| N_QW (Qwen total n) | 1 | 是 |\n| N_LLAMA (LLaMA n) | 1 | 否（LLaMA 不重跑，但需填入已有数据） |\n| LLaMA table 16 cells | 16 | 否（数据已有，需填入） |\n| LLaMA random Wilcoxon p | 2 | 否（数据已有，需填入） |\n| Per-problem concordance ρ, p | 4 | 是（n=500 重算） |\n| Qwen effective-n table 12 cells | 12 | 是（n=500 重算） |\n| C5b pilot (ORACLE/HEUR) | 4 | 独立于 n=500，取决于 C5b 实验 |\n| **合计** | **48** | |\n\n---\n\n## 二、硬编码数值汇总（~120 处）\n\n### 样本量文本 \"50\"→\"500\"（8 处）\n\n| # | 文件:行 | 当前值 | 需要更新? |\n|---|---------|--------|-----------|\n| 1 | abstract.tex:6 | `50 MATH-500 problems` | 是→500 |\n| 2 | methodology.tex:10 | `50 problems stratified from MATH-500` | 是→500 |\n| 3 | results.tex:13 | `$n{=}50$ MATH-500 problems` (Table 1 caption) | 是→500 |\n| 4 | results.tex:34 | `medians across 50 problems` (Table 2 caption) | 是→500 |\n| 5 | appendix_moved.tex:26 | `Four of the 50 problems are excluded` | 是→新排除数/总数 |\n| 6 | appendix_moved.tex:26 | `$n{=}46$ valid problems for Qwen (vs.\\ $n{=}49$ for DeepSeek)` | 是→新有效n |\n| 7 | appendix_moved.tex:93 (tab:permutation caption) | `$n{=}49$, $10{,}000$ permutations` | 是→新n |\n| 8 | appendix_disc_analysis.tex:45 | `$n{=}49$...and $n{=}46$ for Qwen (4 excluded)` | 是→新n |\n\n### Table 1: Aggregate II (results.tex:10-23) — 10 处\n\n| # | 文件:行 | 当前值 | 数据来源 | 需要更新? |\n|---|---------|--------|----------|-----------|\n| 9 | results.tex:19 | `0.39 & 1.48 & 7.16 & 14.59` | DS imp median_diff | 是 |\n| 10 | results.tex:20 | `0.01 & $-$0.02 & 0.54 & 1.54` | DS rand median_diff | 是 |\n| 11 | results.tex:8 | `$0.39$...$14.59$...37×` | 同上 + 比率重算 | 是 |\n| 12 | results.tex:8 | `$-0.02$ to $1.54$` | DS rand range | 是 |\n\n### Table 2: Per-phase II (results.tex:31-53) — 40 处 (8行×5列)\n\n| # | 文件:行 | 行标签 | 当前值 (II_high, II_mid, II_low, Δ, G) | 需要更新? |\n|---|---------|--------|----------------------------------------|-----------|\n| 13 | results.tex:40 | 0.15 Imp | 0.006, 0.081, 0.398, 0.39, 69 | 是 |\n| 14 | results.tex:41 | 0.15 Rand | 0.093, 0.097, 0.103, 0.01, 1.1 | 是 |\n| 15 | results.tex:43 | 0.20 Imp | 0.015, 0.203, 1.496, 1.48, 103 | 是 |\n| 16 | results.tex:44 | 0.20 Rand | 0.292, 0.350, 0.276, −0.02, 0.9 | 是 |\n| 17 | results.tex:46 | 0.25 Imp | 0.032, 1.118, 7.196, 7.16, 222 | 是 |\n| 18 | results.tex:47 | 0.25 Rand | 0.818, 0.932, 1.363, 0.54, 1.7 | 是 |\n| 19 | results.tex:49 | 0.30 Imp | 0.053, 2.283, 14.639, 14.59, 274 | 是 |\n| 20 | results.tex:50 | 0.30 Rand | 2.503, 2.592, 4.041, 1.54, 1.6 | 是 |\n\n### Table 3: Cohen's d (results.tex:108-124) — 16 处\n\n| # | 文件:行 | 当前值 | 需要更新? |\n|---|---------|--------|-----------|\n| 21 | results.tex:117 | DS: 0.44, 0.32 [0.20, 0.47]; QW: 0.28, 0.05 [−0.01, 0.11]^ns | 是 |\n| 22 | results.tex:118 | DS: 0.52, 1.15 [0.66, 1.26]; QW: 0.55, 0.21 [0.07, 0.40] | 是 |\n| 23 | results.tex:119 | DS: 0.68, 3.97 [2.83, 5.29]; QW: 0.89, 1.11 [0.61, 1.47] | 是 |\n| 24 | results.tex:120 | DS: 0.80, 9.94 [8.39, 16.65]; QW: 1.02, 2.62 [1.72, 3.65] | 是 |\n\n### Table: Cross-model (appendix_moved.tex:50-63) — 8 处\n\n| # | 文件:行 | 当前值 | 需要更新? |\n|---|---------|--------|-----------|\n| 25 | appendix_moved.tex:59 | DS: 0.39, 1.48, 7.16, 14.59 | 是 |\n| 26 | appendix_moved.tex:60 | QW: 0.04, 0.23, 1.27, 2.94 | 是 |\n\n### Table: Permutation test (appendix_moved.tex:90-105) — 12 处\n\n| # | 文件:行 | 当前值 | 需要更新? |\n|---|---------|--------|-----------|\n| 27 | appendix_moved.tex:99 | s015: 0.37, [0.19, 0.62], 0.0032 | 是 |\n| 28 | appendix_moved.tex:100 | s020: 0.97, [0.69, 1.49], <0.001 | 是 |\n| 29 | appendix_moved.tex:101 | s025: 3.34, [1.66, 6.64], <0.001 | 是 |\n| 30 | appendix_moved.tex:102 | s030: 9.85, [6.70, 16.29], <0.001 | 是 |\n\n### Table: Discrimination metrics (appendix_moved.tex:123-143) — 16 处\n\n| # | 文件:行 | 当前值 | 需要更新? |\n|---|---------|--------|-----------|\n| 31 | appendix_moved.tex:132 | DS 0.15: −0.030, −0.56 | 是 |\n| 32 | appendix_moved.tex:133 | DS 0.20: −0.040, −0.77 | 是 |\n| 33 | appendix_moved.tex:134 | DS 0.25: −0.065, −1.29 | 是 |\n| 34 | appendix_moved.tex:135 | DS 0.30: −0.081, −1.66 | 是 |\n| 35 | appendix_moved.tex:137 | QW 0.15: −0.010, −0.05 | 是 |\n| 36 | appendix_moved.tex:138 | QW 0.20: −0.012, −0.21 | 是 |\n| 37 | appendix_moved.tex:139 | QW 0.25: −0.010, −1.49 | 是 |\n| 38 | appendix_moved.tex:140 | QW 0.30: −0.020, −1.14 | 是 |\n\n### Table: Entropy deltas (appendix_moved.tex:163-183) — 8 处\n\n| # | 文件:行 | 当前值 | 需要更新? |\n|---|---------|--------|-----------|\n| 39 | appendix_moved.tex:171 | DS 0.15: −0.040 | 是 |\n| 40 | appendix_moved.tex:172 | DS 0.20: −0.047 | 是 |\n| 41 | appendix_moved.tex:173 | DS 0.25: −0.045 | 是 |\n| 42 | appendix_moved.tex:174 | DS 0.30: −0.044 | 是 |\n| 43 | appendix_moved.tex:177 | QW 0.15: −0.073 | 是 |\n| 44 | appendix_moved.tex:178 | QW 0.20: −0.076 | 是 |\n| 45 | appendix_moved.tex:179 | QW 0.25: +0.045 | 是 |\n| 46 | appendix_moved.tex:180 | QW 0.30: −0.007 | 是 |\n\n### 内联统计声明 — abstract.tex（~12 处）\n\n| # | 文件:行 | 当前值 | 数据来源 | 需要更新? |\n|---|---------|--------|----------|-----------|\n| 47 | abstract.tex:7 | `$0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$` | DS imp median_diff | 是 |\n| 48 | abstract.tex:7 | `$d_z$ growing from $0.44$ (small) to $0.80$ (large)` | cohens_d_bf16.json | 是 |\n| 49 | abstract.tex:7 | `$p < 0.005$` | permutation_test_results.json | 是（验证阈值） |\n| 50 | abstract.tex:8 | `7/8 conditions` | 重统计 random PASS/FAIL | 是（可能→8/8） |\n| 51 | abstract.tex:8 | `$p{=}0.012$` | QW rand s030 | 是 |\n| 52 | abstract.tex:9 | `$0.032$ vs.\\ $0.818$` | DS s025 high-phase | 是 |\n| 53 | abstract.tex:9 | `$7.196$ vs.\\ $1.363$` | DS s025 low-phase | 是 |\n| 54 | abstract.tex:10 | `$d_z \\geq 0.55$` | QW s020 d_z | 是 |\n| 55 | abstract.tex:10 | `Spearman $\\rho = 1.0$` | cross_model_analysis.json | 是（验证） |\n| 56 | abstract.tex:10 | `$p = 0.043$` | cross_model_analysis.json | 是 |\n| 57 | abstract.tex:10 | `${\\sim}$1/40 the absolute magnitude` | **间接**：DS Δ̃变→比率重算 | 是 |\n| 58 | abstract.tex:10 | `$0.020 \\to 0.356$` | c3_llama（不变） | 否 |\n\n### 内联统计声明 — introduction.tex（~5 处）\n\n| # | 文件:行 | 当前值 | 需要更新? |\n|---|---------|--------|-----------|\n| 59 | introduction.tex:14 | `$0.39$...$14.59$` | 是 |\n| 60 | introduction.tex:14 | `$d_z$: $0.44 \\to 0.80$` | 是 |\n| 61 | introduction.tex:14 | `$p < 0.005$` | 是（验证） |\n| 62 | introduction.tex:15 | `$d_z \\geq 0.55$` | 是 |\n| 63 | introduction.tex:15 | `$\\sim$1/40 the magnitude` | 是（间接） |\n| 64 | introduction.tex:16 | `7/8 conditions non-significant` | 是（可能→8/8） |\n\n### 内联统计声明 — methodology.tex（2 处）\n\n| # | 文件:行 | 当前值 | 需要更新? |\n|---|---------|--------|-----------|\n| 65 | methodology.tex:18 | `mean/median ratios up to 43:1` | 是 |\n| 66 | methodology.tex:22 | `$p_{\\text{Bonf}} < 0.005$` | 是（验证） |\n\n### 内联统计声明 — results.tex 正文（~20 处）\n\n| # | 文件:行 | 当前值 | 需要更新? |\n|---|---------|--------|-----------|\n| 67 | results.tex:29 | `$69{\\times}$...$274{\\times}$` | 是 |\n| 68 | results.tex:29 | `$0.006$ to $0.053$` | 是 |\n| 69 | results.tex:29 | `$G \\approx 0.9$--$1.7{\\times}$` | 是 |\n| 70 | results.tex:58 | `$69{\\times}$ to $274{\\times}$` (fig caption) | 是 |\n| 71 | results.tex:66 | `$0.032$ vs.\\ $0.818$` | 是 |\n| 72 | results.tex:66 | `$7.196$ vs.\\ $1.363$---a $5.3{\\times}$` | 是 |\n| 73 | results.tex:71 | `$0.04$...$2.94$...${\\sim}1/5$` | 是 |\n| 74 | results.tex:71 | `$d_z \\geq 0.55$; Spearman $\\rho = 1.0$; $p = 0.043$` | 是 |\n| 75 | results.tex:71 | `$d_z{=}0.28$, CI includes zero` | 是 |\n| 76 | results.tex:77 | `$0.37$...$9.85$` | 是 |\n| 77 | results.tex:81 | `${\\sim}40{\\times}$ smaller...and ${\\sim}7{\\times}$ smaller` | 是（间接） |\n| 78 | results.tex:106 | `$d_z{=}0.44$ (small) to $d_z{=}0.80$ (large)` | 是 |\n| 79 | results.tex:106 | `$d_z{=}0.28$...CI includes zero...$d_z \\geq 0.55$` | 是 |\n| 80 | results.tex:106 | `$d_z{=}0.89$/$1.02$ vs.\\ $0.68$/$0.80$` | 是 |\n\n### 内联统计声明 — analysis.tex（~5 处）\n\n| # | 文件:行 | 当前值 | 需要更新? |\n|---|---------|--------|-----------|\n| 81 | analysis.tex:4 | `$0.030$--$0.081$ (DeepSeek) and $0.010$--$0.020$ (Qwen)` | 是 |\n| 82 | analysis.tex:4 | `16 conditions` | 是（验证） |\n| 83 | analysis.tex:6 | `$\\Delta\\mathcal{H} \\in [-0.047, -0.040]$` | 是 |\n| 84 | analysis.tex:6 | `$\\Delta\\mathcal{H} = +0.045$` | 是 |\n| 85 | analysis.tex:6 | `22 of 30 problems` | 是 |\n\n### 内联统计声明 — discussion.tex（~7 处）\n\n| # | 文件:行 | 当前值 | 需要更新? |\n|---|---------|--------|-----------|\n| 86 | discussion.tex:5 | `$69$--$274{\\times}$` | 是 |\n| 87 | discussion.tex:5 | `$0.032$ vs.\\ $0.818$` | 是 |\n| 88 | discussion.tex:5 | `$7.196$ vs.\\ $1.363$` | 是 |\n| 89 | discussion.tex:5 | `$G \\approx 1$` | 是（验证） |\n| 90 | discussion.tex:15 | `${\\sim}40{\\times}$...${\\sim}7{\\times}$` | 是（间接） |\n| 91 | discussion.tex:15 | `$d_z \\geq 1.0$` | 否（LLaMA 不变） |\n\n### 内联统计声明 — conclusion.tex（~5 处）\n\n| # | 文件:行 | 当前值 | 需要更新? |\n|---|---------|--------|-----------|\n| 92 | conclusion.tex:4 | `$69{\\times}$ to $274{\\times}$` | 是 |\n| 93 | conclusion.tex:4 | `$d_z$: $0.44 \\to 0.80$` | 是 |\n| 94 | conclusion.tex:4 | `7/8 conditions non-significant` | 是（可能→8/8） |\n| 95 | conclusion.tex:4 | `$d_z \\geq 0.55$` | 是 |\n| 96 | conclusion.tex:4 | `$\\sim$1/40 the magnitude` | 是（间接） |\n\n### 内联统计声明 — appendix.tex（1 处）\n\n| # | 文件:行 | 当前值 | 需要更新? |\n|---|---------|--------|-----------|\n| 97 | appendix.tex:38 | `$G_{\\times} = 58$--$241{\\times}$` | 是 |\n\n### 内联统计声明 — appendix_moved.tex 正文（~12 处）\n\n| # | 文件:行 | 当前值 | 需要更新? |\n|---|---------|--------|-----------|\n| 98 | appendix_moved.tex:11 | `$0.032$ vs.\\ $0.818$`...`$7.196$ vs.\\ $1.363$---a $5.3{\\times}$` | 是 |\n| 99 | appendix_moved.tex:11 | `$3.9{\\times}$...$5.4{\\times}$...$5.3{\\times}$...$3.6{\\times}$` | 是 |\n| 100 | appendix_moved.tex:16 | `$5.3{\\times}$` (fig caption) | 是 |\n| 101 | appendix_moved.tex:26 | `Four of the 50 problems` | 是 |\n| 102 | appendix_moved.tex:48 | `${\\sim}1/5$` (fig caption) | 是 |\n| 103 | appendix_moved.tex:68 | `one-fifth` | 是 |\n| 104 | appendix_moved.tex:84 | `mean/median ratios...$1.2{\\times}$...$1.6{\\times}$` DS | 是 |\n| 105 | appendix_moved.tex:84 | `$1.1{\\times}$ to $1.4{\\times}$` QW | 是 |\n| 106 | appendix_moved.tex:86 | `$99.92$th percentile...$p_{\\text{Bonf}} = 0.0032$` | 是 |\n| 107 | appendix_moved.tex:88 | `$0.37$...$9.85$...CI lower bound ($0.19 \\to 0.69 \\to 1.66 \\to 6.70$)` | 是 |\n| 108 | appendix_moved.tex:53 (comment) | `mean $\\rho = -0.11$, $p = 0.926$` | 已在 placeholder 中 |\n\n### 内联统计声明 — appendix_disc_analysis.tex（~10 处）\n\n| # | 文件:行 | 当前值 | 需要更新? |\n|---|---------|--------|-----------|\n| 109 | appendix_disc_analysis.tex:4 | `$-0.031$ to $-0.073$; Qwen: $-0.019$ to $-0.045$` | 是 |\n| 110 | appendix_disc_analysis.tex:11 | `$\\widetilde{\\mathrm{II}}_{\\text{high}} < 0.06$` | 是 |\n| 111 | appendix_disc_analysis.tex:11 | `$s = 0.35$, high-phase II rises to $0.105$` | 否（s035 补充实验不重跑） |\n| 112 | appendix_disc_analysis.tex:14 | `7/8...Qwen $s{=}0.30$, $p{=}0.012$...$d_z{=}{-}0.04$` | 是 |\n| 113 | appendix_disc_analysis.tex:45 | `$n{=}49$...$n{=}46$` | 是（同 #8） |\n| 114 | appendix_disc_analysis.tex:46 | `mean/median ratio ${\\sim}1.6{:}1$...mean_diff=22.94, median_diff=14.59` | 是 |\n| 115 | appendix_disc_analysis.tex:47 | CIs: `[0.19, 0.62]...[0.69, 1.49]...[1.66, 6.64]...[6.70, 16.29]` | 是 |\n| 116 | appendix_disc_analysis.tex:49 | `$p{=}0.012$...$d_z{=}{-}0.04$...d=-0.035` | 是 |\n| 117 | appendix_disc_analysis.tex:57 | `$\\Delta$ growth rate $3.8{\\times} \\to 4.8{\\times} \\to 2.0{\\times}$` (comment) | 是（注释中的数据） |\n\n### 内联统计声明 — limitations.tex（1 处，新发现）\n\n| # | 文件:行 | 当前值 | 需要更新? |\n|---|---------|--------|-----------|\n| 118 | limitations.tex:2 | `$\\sim$1/40 of DeepSeek` | 是（间接：DS Δ̃变→比率重算） |\n\n---\n\n## 三、不需更新的值\n\n| 文件:行 | 当前值 | 原因 |\n|---------|--------|------|\n| results.tex:77 | `$n{=}49$ paired problems` | LLaMA 实验不重跑 |\n| results.tex:79 | `$[0.002, 0.043]$`, `$p_{\\text{Bonf}}{=}0.219$` 等 LLaMA 统计量 | LLaMA 数据不变 |\n| results.tex:79 | `$0.020 \\to 0.356$` LLaMA Δ̃ | LLaMA 数据不变 |\n| abstract.tex:10 | `$0.020 \\to 0.356$` LLaMA Δ̃ | LLaMA 数据不变 |\n| abstract.tex:10 | `$p_{\\text{Bonf}}{=}0.029$` LLaMA s030 | LLaMA 数据不变 |\n| discussion.tex:15 | `$d_z \\geq 1.0$` LLaMA within-importance d_z | LLaMA 数据不变 |\n| appendix_disc_analysis.tex:11 | `$s = 0.35$, high-phase II rises to $0.105$` | s035 补充实验不重跑 |\n| related_work.tex | 全文 | 无实验数据 |\n| background.tex | 全文 | 公式定义，无实验数据 |\n| limitations.tex (大部分) | 描述性限定语 | 无具体数值（除比率声明外） |\n| 所有 `\\cite{}` 引用 | — | 无变化 |\n\n**注意：LLaMA 绝对值不变，但 LLaMA 与 DS/QW 的比率声明需要重算（见间接影响）。**\n\n---\n\n## 四、间接影响：LLaMA 比率声明（4+1 处）\n\nLLaMA 数据不变（Δ̃_s030 = 0.356），但 DS/QW 的 Δ̃ 变化导致比率需重算：\n\n| # | 文件:行 | 当前声明 | 计算方法 |\n|---|---------|---------|----------|\n| 1 | abstract.tex:10 | `${\\sim}$1/40` | 新 DS s030 Δ̃ / 0.356 |\n| 2 | results.tex:81 | `${\\sim}40{\\times}$ smaller...and ${\\sim}7{\\times}$ smaller` | 新 DS/QW s030 Δ̃ / 0.356 |\n| 3 | discussion.tex:15 | `${\\sim}40{\\times}$...${\\sim}7{\\times}$` | 同上 |\n| 4 | conclusion.tex:4 | `$\\sim$1/40` | 同上 |\n| 5 | **limitations.tex:2** | `$\\sim$1/40 of DeepSeek` | 同上（**新发现，不在已有清单中**） |\n\n---\n\n## 五、条件性叙事更新\n\n### Qwen s015 决策点\n\nn=500 后 QW s015 Cohen's d CI 是否仍含零决定叙事方案：\n\n| 情况 | 影响位置数 | 操作 |\n|------|-----------|------|\n| CI 仍跨零 | 6 处 | 仅更新数值，保留 \"marginal at s015 / reliable at s≥0.20\" |\n| CI > 0 | 6 处 | 升级为 \"all four sparsity levels\"，删除 ^ns |\n\n影响文件: abstract.tex:10, introduction.tex:15, results.tex:71, results.tex:117, results.tex:122 (脚注), conclusion.tex:4\n\n### Random 7/8 vs 8/8 决策点\n\nn=500 后 QW rand s030 的 borderline PASS (p=0.012) 可能翻转为 FAIL：\n\n| 情况 | 影响位置数 | 操作 |\n|------|-----------|------|\n| 仍 PASS | 5 处 | 仅更新 p 值和 Δ̃ |\n| 翻转 FAIL | 5 处 | \"7/8\"→\"8/8\", \"3/4\"→\"4/4\", 删除 exception 叙事 |\n\n影响文件: abstract.tex:8, introduction.tex:16, conclusion.tex:4, appendix_disc_analysis.tex:14, appendix_results.tex:10\n\n---\n\n## 六、与已有规划文档的差异\n\n对照 `n500_paper_update_checklist.md`：\n\n### 已有清单覆盖的内容\n- §1 样本量文本替换: ✓ 完全覆盖\n- §2 Tables: ✓ 完全覆盖\n- §3 Figures: ✓ 完全覆盖（本审计不重复）\n- §4 内联统计声明: ✓ 基本覆盖\n- §5 Qwen s015 决策点: ✓ 完全覆盖\n- §6 附属统计量: ✓ 完全覆盖\n- §7 数据管道: ✓ 完全覆盖\n- §8 不需更新部分: ✓ 基本正确\n- §10 LLaMA 间接比率: ✓ 覆盖 4 处\n\n### **新发现（不在已有清单中）**\n\n| # | 发现 | 位置 | 说明 |\n|---|------|------|------|\n| **NEW-1** | **limitations.tex:2 的 LLaMA 比率声明** | `$\\sim$1/40 of DeepSeek` | 已有清单 §10 遗漏了 limitations.tex，仅列出 abstract/results/discussion/conclusion |\n| **NEW-2** | **C5b pilot placeholders 未纳入** | discussion.tex:10 的 4 个 `\\placeholder{ORACLE_*/HEUR_*}` | 已有清单 §11 仅确认 \"无需改\"，但这 4 个 placeholder 确实存在且需要填入 C5b 实验数据 |\n| **NEW-3** | **appendix_moved.tex:16 fig caption** | `$5.3{\\times}$` crossover 倍数 | 已有清单中 crossover 倍数仅列 L11，遗漏了 fig3 caption L16 |\n| **NEW-4** | **appendix_moved.tex:48/68 \"one-fifth\" 比率** | fig5 caption + 正文 | 已有清单提到了 fig5 caption 中的 \"one-fifth\" 但内联引用位置不完整 |\n\n### 已有清单的数量统计 vs 实际\n\n| 类别 | 清单统计 | 实际统计 |\n|------|---------|---------|\n| 样本量文本 | 8 处 | 8 处 ✓ |\n| 表格单元格 | ~80 | ~110（含 placeholder 表格 28 cells） |\n| 图表 PDF | 5 | 5 ✓ |\n| 内联统计数值 | ~60 | ~72 处 |\n| Qwen s015 叙事 | 6 处 | 6 处 ✓ |\n| 7/8 vs 8/8 叙事 | 5 处 | 5 处 ✓ |\n| LLaMA 间接比率 | 4 处 | **5 处**（+limitations.tex） |\n| Placeholder 总数 | 未统计 | **48 处** |\n\n---\n\n## 七、全量统计\n\n| 类别 | 数量 |\n|------|------|\n| `\\placeholder{}` 实例 | 48 |\n| 其中 n=500 后需更新 | 24 |\n| 其中 LLaMA 数据（已有未填） | 19 |\n| 其中 C5b 独立实验 | 4 |\n| 其中 per-problem concordance（注释有数据未填） | 4（注释中有 ρ=-0.107, p=0.926） |\n| 硬编码数值需更新 | ~118 |\n| 间接比率重算 | 5 |\n| 条件性叙事更新 | 11（两个决策点） |\n| 图表重新生成 | 5 PDF |\n| **总替换位置** | **~170+** |\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 52_

Now registering the artifact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250",
  "uuid": "dffc2504-ad49-4f43-a56f-1a8f6aabc705",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Q4jDrjoLYUf5v9na92bRY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12135,
      "cache_read_input_tokens": 63764,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12135
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

### Tool call

_source line 53_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01RUu4ynMAfxkEyHPBaaBxmh`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__append_idea",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250",
  "uuid": "d2fae560-b280-4643-8b88-5e1fbc2f06a3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Q4jDrjoLYUf5v9na92bRY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12135,
      "cache_read_input_tokens": 63764,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12135
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

### Tool result

_source line 54 · 2026-05-15T01:47:51.836Z_

<details><summary>↩ Tool result · `toolu_01RUu4ynMAfxkEyHPBaaBxmh`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__append_idea"
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
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250",
  "uuid": "dc62cf85-b366-4128-8eb1-4819255528c4",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__append_idea"
    ],
    "query": "select:mcp__agent-ml-research__append_idea",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Tool call

_source line 55_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01HJfEjC8dwG1XkVLeoSZd8T`</summary>

```json
{
  "query": "register_artifact",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250",
  "uuid": "14e7d9ef-2176-40ec-8035-dab77f6c5bb1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Q4jDrjoLYUf5v9na92bRY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12135,
      "cache_read_input_tokens": 63764,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12135
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

### Tool result

_source line 56 · 2026-05-15T01:47:51.891Z_

<details><summary>↩ Tool result · `toolu_01HJfEjC8dwG1XkVLeoSZd8T`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250",
  "uuid": "964233fc-9145-4b94-845e-2e07df1e6740",
  "tool_use_result": {
    "matches": [],
    "query": "register_artifact",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 57_

<details><summary>Logged reasoning block</summary>

```text
The register_artifact tool doesn't exist as a deferred tool. Let me search for it differently.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250",
  "uuid": "3a57315b-8d0d-4a59-9a6c-f54ec37a7b33",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013ZZgnARWjchYCVcFXXW1Ae",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 406,
      "cache_read_input_tokens": 75899,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 406
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

### Tool call

_source line 58_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_013jtUxCWwRRnYQ3N7AwRhY2`</summary>

```json
{
  "query": "artifact register",
  "max_results": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250",
  "uuid": "70e8eaa7-847f-46a8-a393-4bdb244aa189",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013ZZgnARWjchYCVcFXXW1Ae",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 406,
      "cache_read_input_tokens": 75899,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 406
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

### Tool result

_source line 59 · 2026-05-15T01:47:56.902Z_

<details><summary>↩ Tool result · `toolu_013jtUxCWwRRnYQ3N7AwRhY2`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250",
  "uuid": "14d9f39d-3164-4f1c-ae93-af3a4c37aac0",
  "tool_use_result": {
    "matches": [],
    "query": "artifact register",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Tool call

_source line 60_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01XPLPebeCv61SEqa4GF1kjv`</summary>

```json
{
  "query": "artifact",
  "max_results": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250",
  "uuid": "dd20b7eb-6ecb-4ef1-99c3-c3a6f84303bd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UUKQqtf75xUfoDWdMGdJoD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 129,
      "cache_read_input_tokens": 76305,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 129
      },
      "output_tokens": 72,
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

_source line 61 · 2026-05-15T01:47:59.723Z_

<details><summary>↩ Tool result · `toolu_01XPLPebeCv61SEqa4GF1kjv`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250",
  "uuid": "23259969-f8b1-4508-8883-1d6500b1306c",
  "tool_use_result": {
    "matches": [],
    "query": "artifact",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 62_

`register_artifact` 工具不可用，文件已直接写入 `artifacts/paper_placeholder_audit.md`。

审计完成。核心发现：

**48 处 `\placeholder{}`**，分布在 8 个文件中，涉及 10 个唯一数据源：
- 24 处需 n=500 数据填入（QW rand Δ̃、NULL_PCT、Qwen effective-n 表等）
- 19 处是 LLaMA 数据（已有但从未填入正文）
- 4 处是 C5b pilot 实验数据（独立于 n=500）

**~118 处硬编码数值**需用 n=500 数据替换（6 个表格 ~110 cells + ~72 处内联统计）

**5 处间接 LLaMA 比率**需重算（DS/QW Δ̃ 变化导致 ~40×/~7× 比率失效）

**与已有清单的差异（4 处新发现）**：
1. **limitations.tex:2** 的 `$\sim$1/40 of DeepSeek` 比率声明被遗漏（清单 §10 只列了 abstract/results/discussion/conclusion）
2. **discussion.tex:10** 的 4 个 C5b placeholder（ORACLE_PCT/P, HEUR_PCT/P）清单 §11 标注"无需改"但实际需要填入数据
3. **appendix_moved.tex:16** fig3 caption 中的 `$5.3×$` 倍数被遗漏
4. **appendix_moved.tex:48/68** "one-fifth" 比率引用位置不完整

总替换位置 **~170+**。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250",
  "uuid": "f26b65fe-6105-4deb-8ce8-14d86a3cf5f6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Na3J4jHtCtRewQERx89NoQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 90,
      "cache_read_input_tokens": 76434,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 90
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

_source line 63_

`register_artifact` 工具不可用，文件已直接写入 `artifacts/paper_placeholder_audit.md`。

审计完成。核心发现：

**48 处 `\placeholder{}`**，分布在 8 个文件中，涉及 10 个唯一数据源：
- 24 处需 n=500 数据填入（QW rand Δ̃、NULL_PCT、Qwen effective-n 表等）
- 19 处是 LLaMA 数据（已有但从未填入正文）
- 4 处是 C5b pilot 实验数据（独立于 n=500）

**~118 处硬编码数值**需用 n=500 数据替换（6 个表格 ~110 cells + ~72 处内联统计）

**5 处间接 LLaMA 比率**需重算（DS/QW Δ̃ 变化导致 ~40×/~7× 比率失效）

**与已有清单的差异（4 处新发现）**：
1. **limitations.tex:2** 的 `$\sim$1/40 of DeepSeek` 比率声明被遗漏（清单 §10 只列了 abstract/results/discussion/conclusion）
2. **discussion.tex:10** 的 4 个 C5b placeholder（ORACLE_PCT/P, HEUR_PCT/P）清单 §11 标注"无需改"但实际需要填入数据
3. **appendix_moved.tex:16** fig3 caption 中的 `$5.3×$` 倍数被遗漏
4. **appendix_moved.tex:48/68** "one-fifth" 比率引用位置不完整

总替换位置 **~170+**。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 293336,
  "duration_api_ms": 294064,
  "num_turns": 23,
  "stop_reason": "end_turn",
  "session_id": "dc7be234-7d0d-4c67-98fa-5569aab68250",
  "total_cost_usd": 1.0653682500000001,
  "usage": {
    "input_tokens": 15,
    "cache_creation_input_tokens": 65077,
    "cache_read_input_tokens": 471392,
    "output_tokens": 16854,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 65077,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 487,
        "cache_read_input_tokens": 76434,
        "cache_creation_input_tokens": 90,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 90
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1411,
      "outputTokens": 21,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001516,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 15,
      "outputTokens": 16854,
      "cacheReadInputTokens": 471392,
      "cacheCreationInputTokens": 65077,
      "webSearchRequests": 0,
      "costUSD": 1.06385225,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "efd90986-fd53-49c2-b033-cdb2ad8416b6"
}
```

</details>

---
