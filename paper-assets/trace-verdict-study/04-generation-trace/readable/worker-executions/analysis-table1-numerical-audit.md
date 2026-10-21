# analysis table1 numerical audit

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 60
- **Recorded user turns:** 1
- **Tool calls:** 17
- **Original source:** `logs/workers/worker_analysis_table1_numerical_audit_20260521T194500.log`
- **Structured JSON:** [`903628e1c54a3a446ee3.json`](../../sessions/90/903628e1c54a3a446ee3.json)

## Before a recorded user message

15 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "session_id": "2d564421-8464-4d87-ad0f-5e3eefeb24a0",
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
    "mcp__agent-ml-research__detect_image",
    "mcp__agent-ml-research__kill_job",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__ssh_execute",
    "mcp__agent-ml-research__ssh_read_only",
    "mcp__agent-ml-research__update_registry"
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
  "uuid": "766eccb8-41eb-4cc5-ba52-d2adbf5e9cbd",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/memory/"
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
    "resetsAt": 1779402600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "d40608d9-9a58-40e2-80d7-165009335fba",
  "session_id": "2d564421-8464-4d87-ad0f-5e3eefeb24a0"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the registry and the paper's experiments.tex in parallel to gather all the data needed for the audit.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2d564421-8464-4d87-ad0f-5e3eefeb24a0",
  "uuid": "7e47cefa-1d05-483e-9a29-43234fb62308",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011jGsr19N8Afcd33H4FyRem",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12711,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12711
      },
      "output_tokens": 33,
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

开始交叉验证 Table 1 数值。先并行读取论文和 registry。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2d564421-8464-4d87-ad0f-5e3eefeb24a0",
  "uuid": "95c72cbe-4386-432a-8c5e-4ef6698cdae1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011jGsr19N8Afcd33H4FyRem",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12711,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12711
      },
      "output_tokens": 33,
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01KJe8266bxcnWFvViMU9ek7`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
  "max_results": 4
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2d564421-8464-4d87-ad0f-5e3eefeb24a0",
  "uuid": "a271dae8-3c5a-4c0c-9a2e-be7149dbcbaa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011jGsr19N8Afcd33H4FyRem",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12711,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12711
      },
      "output_tokens": 33,
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

_source line 7 · 2026-05-21T19:45:14.989Z_

<details><summary>↩ Tool result · `toolu_01KJe8266bxcnWFvViMU9ek7`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_read_only"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_registry"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__register_artifact"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
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
  "session_id": "2d564421-8464-4d87-ad0f-5e3eefeb24a0",
  "uuid": "dd78a1e7-48f5-4e70-840c-1576bcf4cc48",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 29
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_015VvFtkidyNCuM4u51p79zg`</summary>

```json
{
  "server": "westd-11235",
  "command": "cat /root/trace-verdict-study/docs/paper/experiments.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2d564421-8464-4d87-ad0f-5e3eefeb24a0",
  "uuid": "52d2a56d-6fbf-4c34-9e94-f3dfc828d44d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B1WLfk69QmxXvtCnfwedv7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1717,
      "cache_read_input_tokens": 24552,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1717
      },
      "output_tokens": 73,
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_013fCLroVZ5PA8czJoxsexD8`</summary>

```json
{
  "project": "trace-verdict-study",
  "limit": 0,
  "fields": [
    "*"
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
  "session_id": "2d564421-8464-4d87-ad0f-5e3eefeb24a0",
  "uuid": "4fbcae82-15b6-4ccd-afa8-eb8001bbbfcf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B1WLfk69QmxXvtCnfwedv7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1717,
      "cache_read_input_tokens": 24552,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1717
      },
      "output_tokens": 73,
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

_source line 10 · 2026-05-21T19:45:18.895Z_

<details><summary>↩ Tool result · `toolu_015VvFtkidyNCuM4u51p79zg`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\\section{Experiments}\\n\\nWe evaluate across two research questions:\\n(1)~Do Tier~1 exception signals generalize across models?\\n(2)~What is the relative contribution of each trace component?\\nAll experiments use $N{=}1{,}190$ test samples; accuracy is reported with Wilson 95\\\\% CIs.\\\\footnote{Data is partitioned at the problem level (472 train / 119 test problems, zero crossover; \\\\S\\\\ref{sec:dataset}). The \\\\texttt{exception\\\\_only} format collapses passing solutions into identical rows (48.99\\\\% test duplicates; Appendix~\\\\ref{sec:dedup_stats}), but these arise from within-problem variants, not cross-set leakage; deduplication sensitivity analysis confirms 0.00pp delta across all 19 experimental conditions.}\\nPairwise comparisons use paired bootstrap resampling ($B{=}10{,}000$, seed=42); all differences are significant at $p{<}.0001$ unless noted.\\n\\n\\\\subsection{Cross-Model Comparison}\\n\\\\label{sec:cross_model}\\n\\nTable~\\\\ref{tab:cross_model} compares four models spanning an 8.7$\\\\times$ parameter range (1.5B--13B) and three architecture families (Qwen, DeepSeek, CodeLlama) under key conditions.\\n\\n\\\\begin{table}[t]\\n\\\\centering\\n\\\\caption{Cross-model verdict accuracy (\\\\%, $N{=}1{,}190$) across four models (1.5B--13B) and three architecture families. Multi-seed entries report mean$\\\\pm$std over 2--3 seeds. Bold: best per model. Full per-seed breakdowns in Appendix~\\\\ref{sec:full_results}; per-class metrics in Appendix~\\\\ref{sec:per_class}. $\\\\dagger$Single seed (seed~42).}\\n\\\\label{tab:cross_model}\\n\\\\small\\n\\\\resizebox{\\\\columnwidth}{!}{%\\n\\\\begin{tabular}{lcccc}\\n\\\\toprule\\n\\\\textbf{Condition} & \\\\textbf{Qwen-7B} & \\\\textbf{Qwen-1.5B} & \\\\textbf{CL-13B} & \\\\textbf{DS-6.7B} \\\\\\\\\\n\\\\midrule\\nexception\\\\_only & \\\\textbf{99.83}{\\\\scriptsize$\\\\pm$0.00} & \\\\textbf{99.83}{\\\\scriptsize$\\\\pm$0.00} & \\\\textbf{99.89}{\\\\scriptsize$\\\\pm$0.10} & \\\\textbf{99.39}{\\\\scriptsize$\\\\pm$0.10} \\\\\\\\\\nae\\\\_only & 99.64{\\\\scriptsize$\\\\pm$0.49} & 98.83{\\\\scriptsize$\\\\pm$0.36} & 99.08{\\\\scriptsize$\\\\pm$0.00} & 98.53{\\\\scriptsize$\\\\pm$0.30} \\\\\\\\\\nVOTA & 99.05{\\\\scriptsize$\\\\pm$0.38} & 99.54{\\\\scriptsize$\\\\pm$0.06} & 98.74{\\\\scriptsize$\\\\pm$0.24} & 99.25$^\\\\ddag$ \\\\\\\\\\nloop\\\\_only & 86.05{\\\\scriptsize$\\\\pm$0.52} & 79.54{\\\\scriptsize$\\\\pm$1.42} & 77.40{\\\\scriptsize$\\\\pm$1.54} & 80.31{\\\\scriptsize$\\\\pm$1.65} \\\\\\\\\\nno\\\\_trace & 75.13$^\\\\dagger$ & 72.35{\\\\scriptsize$\\\\pm$4.48} & 76.47$^\\\\dagger$ & 73.36$^\\\\dagger$ \\\\\\\\\\n\\\\midrule\\nMajority baseline & \\\\multicolumn{4}{c}{71.51} \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}%\\n}\\n\\\\vspace{2pt}\\n\\\\par\\\\raggedright\\\\footnotesize\\nDeepSeek \\\\texttt{exception\\\\_only} 3 seeds: 99.33/99.50/99.33 ($\\\\sigma{=}$0.10pp).\\nVOTA on Qwen-7B: 99.41/98.66/99.08 ($\\\\sigma{=}$0.38).\\n\\\\texttt{ae\\\\_only} 3 seeds: 99.92/99.08/99.92 (mean 99.64\\\\%); Qwen-7B \\\\texttt{loop\\\\_only} 3 seeds: 85.63/85.88/86.64 (mean 86.05\\\\%).\\nQwen-1.5B \\\\texttt{exception\\\\_only}: 99.83\\\\% across 3 seeds ($\\\\sigma{=}$0).\\n$^\\\\ddag$DeepSeek VOTA 3 seeds: 84.45/99.16/99.33; seed 42 (84.45\\\\%, fail recall\\\\,=\\\\,45.4\\\\%) is a training failure due to tokenizer-driven truncation (Appendix~\\\\ref{sec:tokenizer_analysis}), reported as 2-seed mean.\\n\\\\end{table}\\n\\n\\\\paragraph{Exception dominance across families.}\\nUnder \\\\texttt{exception\\\\_only}, all four models achieve ${\\\\geq}$99.33\\\\% across all seeds: Qwen-7B (99.83\\\\%$\\\\pm$0.00, 3 seeds), Qwen-1.5B (99.83\\\\%), CodeLlama-13B (99.89\\\\%$\\\\pm$0.10, 3 seeds; seed 123 achieves 100\\\\%), and DeepSeek-6.7B (99.39\\\\%$\\\\pm$0.10, 3 seeds).\\nThe cross-model range is 0.50pp (99.39--99.89\\\\%), the tightest of any condition.\\n\\n\\\\paragraph{Scale invariance of exception signals.}\\nException-based accuracy is shared by models spanning 1.5B to 13B parameters (8.7$\\\\times$): both Qwen-1.5B and CodeLlama-13B achieve 99.83\\\\%+ on the same representation.\\nCodeLlama-13B seed 123 achieves 100\\\\% (0/1190 errors), confirming that Qwen's two persistent errors (from \\\\texttt{GeneratorExit}; Appendix~\\\\ref{sec:irreducible}) are high-probability convergence artifacts rather than hard data limitations.\\nIn contrast, \\\\texttt{no\\\\_trace} scales monotonically with capacity: 72.35\\\\% (1.5B) $\\\\to$ 75.13\\\\% (7B) $\\\\to$ 76.47\\\\% (13B), a\\n\\n... [截断: 输出过长，省略 9168 字符] ...\\n\\nimization dynamics; the 26\\\\%/74\\\\% attribution is an approximate decomposition (Qwen family, 2 scales, 3 seeds each).\\n\\n\\\\subsection{Additional Analyses}\\n\\\\label{sec:additional}\\n\\n\\\\paragraph{Trace length ablation.}\\n\\\\label{sec:trace_length}\\nVarying the head-truncated trace token budget (256--no limit) on Qwen-7B yields accuracy in a narrow 77.2\\\\%--81.8\\\\% band with a non-monotonic pattern: 1024-token prefixes (77.23\\\\%) underperform 512-token prefixes (80.42\\\\%, $p{=}.002$), because mid-length prefixes retain enough irrelevant content to mislead the model while discarding diagnostic events near the trace terminus (Appendix~\\\\ref{sec:trace_length_full}).\\nThis non-monotonicity is specific to head-truncation; under tail-truncation, accuracy increases monotonically for two of three models (Table~\\\\ref{tab:tail_cross_model} in Appendix), with only DeepSeek showing a mild architecture-specific reversal at tail-1024$\\\\to$tail-2048 ($-$1.5pp).\\n\\n\\\\paragraph{Truncation direction and budget curve.}\\nTail-truncation (retaining the last $k$ tokens) dramatically outperforms head-truncation: among the three models with complete data, tail-2048 exceeds head-2048 by 15.5--22.6pp, with the gap widening at smaller scale (Qwen-1.5B: +22.6pp vs.\\\\ Qwen-7B: +15.5pp; Appendix~\\\\ref{sec:trace_length_full}, Table~\\\\ref{tab:head_vs_tail}).\\nAll four models' head-2048 accuracies converge into a narrow 75.3--81.8\\\\% band (6.5pp), comparable to the tail-256 band (72.6--78.9\\\\%, 6.3pp), indicating that signal-poor conditions produce a shared performance floor regardless of scale or architecture.\\n\\nA cross-model budget sweep across four models and three architecture families reveals a phase transition localized between 384 and 512 tail tokens.\\nAt tail-384, all models remain near baseline (73.6--82.9\\\\%, only +1.0--6.5pp over tail-256); the steep jump occurs at 384$\\\\to$512 (+11.0--22.0pp), crossing from near-baseline to near-ceiling (${\\\\sim}$94--98\\\\%).\\nThis localizes the critical threshold to ${\\\\sim}$400--500 tokens, matching the typical exception traceback length (Table~\\\\ref{tab:tail_cross_model}).\\nBeyond 512 tokens, accuracy converges further: multi-seed validation across all 12 model$\\\\times$seed combinations confirms all tail-512 accuracies fall within a 4.63pp band [93.61\\\\%, 98.24\\\\%] (Table~\\\\ref{tab:tail512_seeds}); at tail-1024, three models reach 96.5--98.2\\\\%, compressing the 6.3pp cross-model spread observed at tail-256.\\n\\\\texttt{tail\\\\_2048} captures 95--98\\\\% of \\\\texttt{exception\\\\_only}'s accuracy across all completed configurations.\\nThe residual 2--5pp gap confirms that semantic extraction (identifying exception type and message) still outperforms positional extraction (retaining a fixed window containing non-diagnostic lines).\\n\\n\\\\paragraph{Calibration.}\\n\\\\label{sec:calibration}\\nCalibration mirrors the tier pattern: \\\\texttt{exception\\\\_only} achieves ECE = 0.0027 vs.\\\\ 0.171 for \\\\texttt{no\\\\_trace}, a 63$\\\\times$ gap (Figure~\\\\ref{fig:calibration}).\\nThis calibration advantage generalizes across architectures and scales: all four models (1.5B--13B) achieve ECE ${<}$ 0.007 under \\\\texttt{exception\\\\_only} (Appendix~\\\\ref{sec:calibration_full}).\\n\\n\\\\paragraph{Error orthogonality.}\\n\\\\texttt{exception\\\\_only}'s 2 errors have zero overlap with all other conditions' error sets (Jaccard = 0.000), confirming it operates on an independent signal dimension (Appendix~\\\\ref{sec:error_overlap}).\\n\\n\\\\paragraph{Exception type breakdown.}\\nA per-exception-type breakdown (Appendix~\\\\ref{sec:exception_type}) confirms that all standard exception types achieve 100\\\\% accuracy; the only failures arise from \\\\texttt{GeneratorExit}, a benign \\\\texttt{BaseException} subclass.\\n\\n\\\\paragraph{Supplementary out-of-distribution check.}\\n\\\\label{sec:debugbench}\\nOn DebugBench \\\\citep{tian2024debugbench} ($N{=}426$), the ranking is preserved: \\\\texttt{exception\\\\_only} 100\\\\%, VOTA 99.77\\\\%, \\\\texttt{no\\\\_trace} 96.71\\\\%; narrow margins reflect a ceiling effect from structurally distinctive mutations (Appendix~\\\\ref{sec:debugbench_full}).\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.15}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2d564421-8464-4d87-ad0f-5e3eefeb24a0",
  "uuid": "21a9d767-bea0-406c-a8fe-5775b29dd95d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\\section{Experiments}\\\\n\\\\nWe evaluate across two research questions:\\\\n(1)~Do Tier~1 exception signals generalize across models?\\\\n(2)~What is the relative contribution of each trace component?\\\\nAll experiments use $N{=}1{,}190$ test samples; accuracy is reported with Wilson 95\\\\\\\\% CIs.\\\\\\\\footnote{Data is partitioned at the problem level (472 train / 119 test problems, zero crossover; \\\\\\\\S\\\\\\\\ref{sec:dataset}). The \\\\\\\\texttt{exception\\\\\\\\_only} format collapses passing solutions into identical rows (48.99\\\\\\\\% test duplicates; Appendix~\\\\\\\\ref{sec:dedup_stats}), but these arise from within-problem variants, not cross-set leakage; deduplication sensitivity analysis confirms 0.00pp delta across all 19 experimental conditions.}\\\\nPairwise comparisons use paired bootstrap resampling ($B{=}10{,}000$, seed=42); all differences are significant at $p{<}.0001$ unless noted.\\\\n\\\\n\\\\\\\\subsection{Cross-Model Comparison}\\\\n\\\\\\\\label{sec:cross_model}\\\\n\\\\nTable~\\\\\\\\ref{tab:cross_model} compares four models spanning an 8.7$\\\\\\\\times$ parameter range (1.5B--13B) and three architecture families (Qwen, DeepSeek, CodeLlama) under key conditions.\\\\n\\\\n\\\\\\\\begin{table}[t]\\\\n\\\\\\\\centering\\\\n\\\\\\\\caption{Cross-model verdict accuracy (\\\\\\\\%, $N{=}1{,}190$) across four models (1.5B--13B) and three architecture families. Multi-seed entries report mean$\\\\\\\\pm$std over 2--3 seeds. Bold: best per model. Full per-seed breakdowns in Appendix~\\\\\\\\ref{sec:full_results}; per-class metrics in Appendix~\\\\\\\\ref{sec:per_class}. $\\\\\\\\dagger$Single seed (seed~42).}\\\\n\\\\\\\\label{tab:cross_model}\\\\n\\\\\\\\small\\\\n\\\\\\\\resizebox{\\\\\\\\columnwidth}{!}{%\\\\n\\\\\\\\begin{tabular}{lcccc}\\\\n\\\\\\\\toprule\\\\n\\\\\\\\textbf{Condition} & \\\\\\\\textbf{Qwen-7B} & \\\\\\\\textbf{Qwen-1.5B} & \\\\\\\\textbf{CL-13B} & \\\\\\\\textbf{DS-6.7B} \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\nexception\\\\\\\\_only & \\\\\\\\textbf{99.83}{\\\\\\\\scriptsize$\\\\\\\\pm$0.00} & \\\\\\\\textbf{99.83}{\\\\\\\\scriptsize$\\\\\\\\pm$0.00} & \\\\\\\\textbf{99.89}{\\\\\\\\scriptsize$\\\\\\\\pm$0.10} & \\\\\\\\textbf{99.39}{\\\\\\\\scriptsize$\\\\\\\\pm$0.10} \\\\\\\\\\\\\\\\\\\\nae\\\\\\\\_only & 99.64{\\\\\\\\scriptsize$\\\\\\\\pm$0.49} & 98.83{\\\\\\\\scriptsize$\\\\\\\\pm$0.36} & 99.08{\\\\\\\\scriptsize$\\\\\\\\pm$0.00} & 98.53{\\\\\\\\scriptsize$\\\\\\\\pm$0.30} \\\\\\\\\\\\\\\\\\\\nVOTA & 99.05{\\\\\\\\scriptsize$\\\\\\\\pm$0.38} & 99.54{\\\\\\\\scriptsize$\\\\\\\\pm$0.06} & 98.74{\\\\\\\\scriptsize$\\\\\\\\pm$0.24} & 99.25$^\\\\\\\\ddag$ \\\\\\\\\\\\\\\\\\\\nloop\\\\\\\\_only & 86.05{\\\\\\\\scriptsize$\\\\\\\\pm$0.52} & 79.54{\\\\\\\\scriptsize$\\\\\\\\pm$1.42} & 77.40{\\\\\\\\scriptsize$\\\\\\\\pm$1.54} & 80.31{\\\\\\\\scriptsize$\\\\\\\\pm$1.65} \\\\\\\\\\\\\\\\\\\\nno\\\\\\\\_trace & 75.13$^\\\\\\\\dagger$ & 72.35{\\\\\\\\scriptsize$\\\\\\\\pm$4.48} & 76.47$^\\\\\\\\dagger$ & 73.36$^\\\\\\\\dagger$ \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\nMajority baseline & \\\\\\\\multicolumn{4}{c}{71.51} \\\\\\\\\\\\\\\\\\\\n\\\\\\\\bottomrule\\\\n\\\\\\\\end{tabular}%\\\\n}\\\\n\\\\\\\\vspace{2pt}\\\\n\\\\\\\\par\\\\\\\\raggedright\\\\\\\\footnotesize\\\\nDeepSeek \\\\\\\\texttt{exception\\\\\\\\_only} 3 seeds: 99.33/99.50/99.33 ($\\\\\\\\sigma{=}$0.10pp).\\\\nVOTA on Qwen-7B: 99.41/98.66/99.08 ($\\\\\\\\sigma{=}$0.38).\\\\n\\\\\\\\texttt{ae\\\\\\\\_only} 3 seeds: 99.92/99.08/99.92 (mean 99.64\\\\\\\\%); Qwen-7B \\\\\\\\texttt{loop\\\\\\\\_only} 3 seeds: 85.63/85.88/86.64 (mean 86.05\\\\\\\\%).\\\\nQwen-1.5B \\\\\\\\texttt{exception\\\\\\\\_only}: 99.83\\\\\\\\% across 3 seeds ($\\\\\\\\sigma{=}$0).\\\\n$^\\\\\\\\ddag$DeepSeek VOTA 3 seeds: 84.45/99.16/99.33; seed 42 (84.45\\\\\\\\%, fail recall\\\\\\\\,=\\\\\\\\,45.4\\\\\\\\%) is a training failure due to tokenizer-driven truncation (Appendix~\\\\\\\\ref{sec:tokenizer_analysis}), reported as 2-seed mean.\\\\n\\\\\\\\end{table}\\\\n\\\\n\\\\\\\\paragraph{Exception dominance across families.}\\\\nUnder \\\\\\\\texttt{exception\\\\\\\\_only}, all four models achieve ${\\\\\\\\geq}$99.33\\\\\\\\% across all seeds: Qwen-7B (99.83\\\\\\\\%$\\\\\\\\pm$0.00, 3 seeds), Qwen-1.5B (99.83\\\\\\\\%), CodeLlama-13B (99.89\\\\\\\\%$\\\\\\\\pm$0.10, 3 seeds; seed 123 achieves 100\\\\\\\\%), and DeepSeek-6.7B (99.39\\\\\\\\%$\\\\\\\\pm$0.10, 3 seeds).\\\\nThe cross-model range is 0.50pp (99.39--99.89\\\\\\\\%), the tightest of any condition.\\\\n\\\\n\\\\\\\\paragraph{Scale invariance of exception signals.}\\\\nException-based accuracy is shared by models spanning 1.5B to 13B parameters (8.7$\\\\\\\\times$): both Qwen-1.5B and CodeLlama-13B achieve 99.83\\\\\\\\%+ on the same representation.\\\\nCodeLlama-13B seed 123 achieves 100\\\\\\\\% (0/1190 errors), confirming that Qwen's two persistent errors (from \\\\\\\\texttt{GeneratorExit}; Appendix~\\\\\\\\ref{sec:irreducible}) are high-probability convergence artifacts rather than hard data limitations.\\\\nIn contrast, \\\\\\\\texttt{no\\\\\\\\_trace} scales monotonically with capacity: 72.35\\\\\\\\% (1.5B) $\\\\\\\\to$ 75.13\\\\\\\\% (7B) $\\\\\\\\to$ 76.47\\\\\\\\% (13B), a\\\\n\\\\n... [截断: 输出过长，省略 9168 字符] ...\\\\n\\\\nimization dynamics; the 26\\\\\\\\%/74\\\\\\\\% attribution is an approximate decomposition (Qwen family, 2 scales, 3 seeds each).\\\\n\\\\n\\\\\\\\subsection{Additional Analyses}\\\\n\\\\\\\\label{sec:additional}\\\\n\\\\n\\\\\\\\paragraph{Trace length ablation.}\\\\n\\\\\\\\label{sec:trace_length}\\\\nVarying the head-truncated trace token budget (256--no limit) on Qwen-7B yields accuracy in a narrow 77.2\\\\\\\\%--81.8\\\\\\\\% band with a non-monotonic pattern: 1024-token prefixes (77.23\\\\\\\\%) underperform 512-token prefixes (80.42\\\\\\\\%, $p{=}.002$), because mid-length prefixes retain enough irrelevant content to mislead the model while discarding diagnostic events near the trace terminus (Appendix~\\\\\\\\ref{sec:trace_length_full}).\\\\nThis non-monotonicity is specific to head-truncation; under tail-truncation, accuracy increases monotonically for two of three models (Table~\\\\\\\\ref{tab:tail_cross_model} in Appendix), with only DeepSeek showing a mild architecture-specific reversal at tail-1024$\\\\\\\\to$tail-2048 ($-$1.5pp).\\\\n\\\\n\\\\\\\\paragraph{Truncation direction and budget curve.}\\\\nTail-truncation (retaining the last $k$ tokens) dramatically outperforms head-truncation: among the three models with complete data, tail-2048 exceeds head-2048 by 15.5--22.6pp, with the gap widening at smaller scale (Qwen-1.5B: +22.6pp vs.\\\\\\\\ Qwen-7B: +15.5pp; Appendix~\\\\\\\\ref{sec:trace_length_full}, Table~\\\\\\\\ref{tab:head_vs_tail}).\\\\nAll four models' head-2048 accuracies converge into a narrow 75.3--81.8\\\\\\\\% band (6.5pp), comparable to the tail-256 band (72.6--78.9\\\\\\\\%, 6.3pp), indicating that signal-poor conditions produce a shared performance floor regardless of scale or architecture.\\\\n\\\\nA cross-model budget sweep across four models and three architecture families reveals a phase transition localized between 384 and 512 tail tokens.\\\\nAt tail-384, all models remain near baseline (73.6--82.9\\\\\\\\%, only +1.0--6.5pp over tail-256); the steep jump occurs at 384$\\\\\\\\to$512 (+11.0--22.0pp), crossing from near-baseline to near-ceiling (${\\\\\\\\sim}$94--98\\\\\\\\%).\\\\nThis localizes the critical threshold to ${\\\\\\\\sim}$400--500 tokens, matching the typical exception traceback length (Table~\\\\\\\\ref{tab:tail_cross_model}).\\\\nBeyond 512 tokens, accuracy converges further: multi-seed validation across all 12 model$\\\\\\\\times$seed combinations confirms all tail-512 accuracies fall within a 4.63pp band [93.61\\\\\\\\%, 98.24\\\\\\\\%] (Table~\\\\\\\\ref{tab:tail512_seeds}); at tail-1024, three models reach 96.5--98.2\\\\\\\\%, compressing the 6.3pp cross-model spread observed at tail-256.\\\\n\\\\\\\\texttt{tail\\\\\\\\_2048} captures 95--98\\\\\\\\% of \\\\\\\\texttt{exception\\\\\\\\_only}'s accuracy across all completed configurations.\\\\nThe residual 2--5pp gap confirms that semantic extraction (identifying exception type and message) still outperforms positional extraction (retaining a fixed window containing non-diagnostic lines).\\\\n\\\\n\\\\\\\\paragraph{Calibration.}\\\\n\\\\\\\\label{sec:calibration}\\\\nCalibration mirrors the tier pattern: \\\\\\\\texttt{exception\\\\\\\\_only} achieves ECE = 0.0027 vs.\\\\\\\\ 0.171 for \\\\\\\\texttt{no\\\\\\\\_trace}, a 63$\\\\\\\\times$ gap (Figure~\\\\\\\\ref{fig:calibration}).\\\\nThis calibration advantage generalizes across architectures and scales: all four models (1.5B--13B) achieve ECE ${<}$ 0.007 under \\\\\\\\texttt{exception\\\\\\\\_only} (Appendix~\\\\\\\\ref{sec:calibration_full}).\\\\n\\\\n\\\\\\\\paragraph{Error orthogonality.}\\\\n\\\\\\\\texttt{exception\\\\\\\\_only}'s 2 errors have zero overlap with all other conditions' error sets (Jaccard = 0.000), confirming it operates on an independent signal dimension (Appendix~\\\\\\\\ref{sec:error_overlap}).\\\\n\\\\n\\\\\\\\paragraph{Exception type breakdown.}\\\\nA per-exception-type breakdown (Appendix~\\\\\\\\ref{sec:exception_type}) confirms that all standard exception types achieve 100\\\\\\\\% accuracy; the only failures arise from \\\\\\\\texttt{GeneratorExit}, a benign \\\\\\\\texttt{BaseException} subclass.\\\\n\\\\n\\\\\\\\paragraph{Supplementary out-of-distribution check.}\\\\n\\\\\\\\label{sec:debugbench}\\\\nOn DebugBench \\\\\\\\citep{tian2024debugbench} ($N{=}426$), the ranking is preserved: \\\\\\\\texttt{exception\\\\\\\\_only} 100\\\\\\\\%, VOTA 99.77\\\\\\\\%, \\\\\\\\texttt{no\\\\\\\\_trace} 96.71\\\\\\\\%; narrow margins reflect a ceiling effect from structurally distinctive mutations (Appendix~\\\\\\\\ref{sec:debugbench_full}).\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.15}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\\section{Experiments}\\n\\nWe evaluate across two research questions:\\n(1)~Do Tier~1 exception signals generalize across models?\\n(2)~What is the relative contribution of each trace component?\\nAll experiments use $N{=}1{,}190$ test samples; accuracy is reported with Wilson 95\\\\% CIs.\\\\footnote{Data is partitioned at the problem level (472 train / 119 test problems, zero crossover; \\\\S\\\\ref{sec:dataset}). The \\\\texttt{exception\\\\_only} format collapses passing solutions into identical rows (48.99\\\\% test duplicates; Appendix~\\\\ref{sec:dedup_stats}), but these arise from within-problem variants, not cross-set leakage; deduplication sensitivity analysis confirms 0.00pp delta across all 19 experimental conditions.}\\nPairwise comparisons use paired bootstrap resampling ($B{=}10{,}000$, seed=42); all differences are significant at $p{<}.0001$ unless noted.\\n\\n\\\\subsection{Cross-Model Comparison}\\n\\\\label{sec:cross_model}\\n\\nTable~\\\\ref{tab:cross_model} compares four models spanning an 8.7$\\\\times$ parameter range (1.5B--13B) and three architecture families (Qwen, DeepSeek, CodeLlama) under key conditions.\\n\\n\\\\begin{table}[t]\\n\\\\centering\\n\\\\caption{Cross-model verdict accuracy (\\\\%, $N{=}1{,}190$) across four models (1.5B--13B) and three architecture families. Multi-seed entries report mean$\\\\pm$std over 2--3 seeds. Bold: best per model. Full per-seed breakdowns in Appendix~\\\\ref{sec:full_results}; per-class metrics in Appendix~\\\\ref{sec:per_class}. $\\\\dagger$Single seed (seed~42).}\\n\\\\label{tab:cross_model}\\n\\\\small\\n\\\\resizebox{\\\\columnwidth}{!}{%\\n\\\\begin{tabular}{lcccc}\\n\\\\toprule\\n\\\\textbf{Condition} & \\\\textbf{Qwen-7B} & \\\\textbf{Qwen-1.5B} & \\\\textbf{CL-13B} & \\\\textbf{DS-6.7B} \\\\\\\\\\n\\\\midrule\\nexception\\\\_only & \\\\textbf{99.83}{\\\\scriptsize$\\\\pm$0.00} & \\\\textbf{99.83}{\\\\scriptsize$\\\\pm$0.00} & \\\\textbf{99.89}{\\\\scriptsize$\\\\pm$0.10} & \\\\textbf{99.39}{\\\\scriptsize$\\\\pm$0.10} \\\\\\\\\\nae\\\\_only & 99.64{\\\\scriptsize$\\\\pm$0.49} & 98.83{\\\\scriptsize$\\\\pm$0.36} & 99.08{\\\\scriptsize$\\\\pm$0.00} & 98.53{\\\\scriptsize$\\\\pm$0.30} \\\\\\\\\\nVOTA & 99.05{\\\\scriptsize$\\\\pm$0.38} & 99.54{\\\\scriptsize$\\\\pm$0.06} & 98.74{\\\\scriptsize$\\\\pm$0.24} & 99.25$^\\\\ddag$ \\\\\\\\\\nloop\\\\_only & 86.05{\\\\scriptsize$\\\\pm$0.52} & 79.54{\\\\scriptsize$\\\\pm$1.42} & 77.40{\\\\scriptsize$\\\\pm$1.54} & 80.31{\\\\scriptsize$\\\\pm$1.65} \\\\\\\\\\nno\\\\_trace & 75.13$^\\\\dagger$ & 72.35{\\\\scriptsize$\\\\pm$4.48} & 76.47$^\\\\dagger$ & 73.36$^\\\\dagger$ \\\\\\\\\\n\\\\midrule\\nMajority baseline & \\\\multicolumn{4}{c}{71.51} \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}%\\n}\\n\\\\vspace{2pt}\\n\\\\par\\\\raggedright\\\\footnotesize\\nDeepSeek \\\\texttt{exception\\\\_only} 3 seeds: 99.33/99.50/99.33 ($\\\\sigma{=}$0.10pp).\\nVOTA on Qwen-7B: 99.41/98.66/99.08 ($\\\\sigma{=}$0.38).\\n\\\\texttt{ae\\\\_only} 3 seeds: 99.92/99.08/99.92 (mean 99.64\\\\%); Qwen-7B \\\\texttt{loop\\\\_only} 3 seeds: 85.63/85.88/86.64 (mean 86.05\\\\%).\\nQwen-1.5B \\\\texttt{exception\\\\_only}: 99.83\\\\% across 3 seeds ($\\\\sigma{=}$0).\\n$^\\\\ddag$DeepSeek VOTA 3 seeds: 84.45/99.16/99.33; seed 42 (84.45\\\\%, fail recall\\\\,=\\\\,45.4\\\\%) is a training failure due to tokenizer-driven truncation (Appendix~\\\\ref{sec:tokenizer_analysis}), reported as 2-seed mean.\\n\\\\end{table}\\n\\n\\\\paragraph{Exception dominance across families.}\\nUnder \\\\texttt{exception\\\\_only}, all four models achieve ${\\\\geq}$99.33\\\\% across all seeds: Qwen-7B (99.83\\\\%$\\\\pm$0.00, 3 seeds), Qwen-1.5B (99.83\\\\%), CodeLlama-13B (99.89\\\\%$\\\\pm$0.10, 3 seeds; seed 123 achieves 100\\\\%), and DeepSeek-6.7B (99.39\\\\%$\\\\pm$0.10, 3 seeds).\\nThe cross-model range is 0.50pp (99.39--99.89\\\\%), the tightest of any condition.\\n\\n\\\\paragraph{Scale invariance of exception signals.}\\nException-based accuracy is shared by models spanning 1.5B to 13B parameters (8.7$\\\\times$): both Qwen-1.5B and CodeLlama-13B achieve 99.83\\\\%+ on the same representation.\\nCodeLlama-13B seed 123 achieves 100\\\\% (0/1190 errors), confirming that Qwen's two persistent errors (from \\\\texttt{GeneratorExit}; Appendix~\\\\ref{sec:irreducible}) are high-probability convergence artifacts rather than hard data limitations.\\nIn contrast, \\\\texttt{no\\\\_trace} scales monotonically with capacity: 72.35\\\\% (1.5B) $\\\\to$ 75.13\\\\% (7B) $\\\\to$ 76.47\\\\% (13B), a\\n\\n... [截断: 输出过长，省略 9168 字符] ...\\n\\nimization dynamics; the 26\\\\%/74\\\\% attribution is an approximate decomposition (Qwen family, 2 scales, 3 seeds each).\\n\\n\\\\subsection{Additional Analyses}\\n\\\\label{sec:additional}\\n\\n\\\\paragraph{Trace length ablation.}\\n\\\\label{sec:trace_length}\\nVarying the head-truncated trace token budget (256--no limit) on Qwen-7B yields accuracy in a narrow 77.2\\\\%--81.8\\\\% band with a non-monotonic pattern: 1024-token prefixes (77.23\\\\%) underperform 512-token prefixes (80.42\\\\%, $p{=}.002$), because mid-length prefixes retain enough irrelevant content to mislead the model while discarding diagnostic events near the trace terminus (Appendix~\\\\ref{sec:trace_length_full}).\\nThis non-monotonicity is specific to head-truncation; under tail-truncation, accuracy increases monotonically for two of three models (Table~\\\\ref{tab:tail_cross_model} in Appendix), with only DeepSeek showing a mild architecture-specific reversal at tail-1024$\\\\to$tail-2048 ($-$1.5pp).\\n\\n\\\\paragraph{Truncation direction and budget curve.}\\nTail-truncation (retaining the last $k$ tokens) dramatically outperforms head-truncation: among the three models with complete data, tail-2048 exceeds head-2048 by 15.5--22.6pp, with the gap widening at smaller scale (Qwen-1.5B: +22.6pp vs.\\\\ Qwen-7B: +15.5pp; Appendix~\\\\ref{sec:trace_length_full}, Table~\\\\ref{tab:head_vs_tail}).\\nAll four models' head-2048 accuracies converge into a narrow 75.3--81.8\\\\% band (6.5pp), comparable to the tail-256 band (72.6--78.9\\\\%, 6.3pp), indicating that signal-poor conditions produce a shared performance floor regardless of scale or architecture.\\n\\nA cross-model budget sweep across four models and three architecture families reveals a phase transition localized between 384 and 512 tail tokens.\\nAt tail-384, all models remain near baseline (73.6--82.9\\\\%, only +1.0--6.5pp over tail-256); the steep jump occurs at 384$\\\\to$512 (+11.0--22.0pp), crossing from near-baseline to near-ceiling (${\\\\sim}$94--98\\\\%).\\nThis localizes the critical threshold to ${\\\\sim}$400--500 tokens, matching the typical exception traceback length (Table~\\\\ref{tab:tail_cross_model}).\\nBeyond 512 tokens, accuracy converges further: multi-seed validation across all 12 model$\\\\times$seed combinations confirms all tail-512 accuracies fall within a 4.63pp band [93.61\\\\%, 98.24\\\\%] (Table~\\\\ref{tab:tail512_seeds}); at tail-1024, three models reach 96.5--98.2\\\\%, compressing the 6.3pp cross-model spread observed at tail-256.\\n\\\\texttt{tail\\\\_2048} captures 95--98\\\\% of \\\\texttt{exception\\\\_only}'s accuracy across all completed configurations.\\nThe residual 2--5pp gap confirms that semantic extraction (identifying exception type and message) still outperforms positional extraction (retaining a fixed window containing non-diagnostic lines).\\n\\n\\\\paragraph{Calibration.}\\n\\\\label{sec:calibration}\\nCalibration mirrors the tier pattern: \\\\texttt{exception\\\\_only} achieves ECE = 0.0027 vs.\\\\ 0.171 for \\\\texttt{no\\\\_trace}, a 63$\\\\times$ gap (Figure~\\\\ref{fig:calibration}).\\nThis calibration advantage generalizes across architectures and scales: all four models (1.5B--13B) achieve ECE ${<}$ 0.007 under \\\\texttt{exception\\\\_only} (Appendix~\\\\ref{sec:calibration_full}).\\n\\n\\\\paragraph{Error orthogonality.}\\n\\\\texttt{exception\\\\_only}'s 2 errors have zero overlap with all other conditions' error sets (Jaccard = 0.000), confirming it operates on an independent signal dimension (Appendix~\\\\ref{sec:error_overlap}).\\n\\n\\\\paragraph{Exception type breakdown.}\\nA per-exception-type breakdown (Appendix~\\\\ref{sec:exception_type}) confirms that all standard exception types achieve 100\\\\% accuracy; the only failures arise from \\\\texttt{GeneratorExit}, a benign \\\\texttt{BaseException} subclass.\\n\\n\\\\paragraph{Supplementary out-of-distribution check.}\\n\\\\label{sec:debugbench}\\nOn DebugBench \\\\citep{tian2024debugbench} ($N{=}426$), the ranking is preserved: \\\\texttt{exception\\\\_only} 100\\\\%, VOTA 99.77\\\\%, \\\\texttt{no\\\\_trace} 96.71\\\\%; narrow margins reflect a ceiling effect from structurally distinctive mutations (Appendix~\\\\ref{sec:debugbench_full}).\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.15}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-21T19:45:19.800Z_

<details><summary>↩ Tool result · `toolu_013fCLroVZ5PA8czJoxsexD8`</summary>

```text
Error: result (319,300 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/2d564421-8464-4d87-ad0f-5e3eefeb24a0/tool-results/mcp-agent-ml-research-read_registry-1779392719783.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/2d564421-8464-4d87-ad0f-5e3eefeb24a0/tool-results/mcp-agent-ml-research-read_registry-1779392719783.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/2d564421-8464-4d87-ad0f-5e3eefeb24a0/tool-results/mcp-agent-ml-research-read_registry-1779392719783.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2d564421-8464-4d87-ad0f-5e3eefeb24a0",
  "uuid": "def22dd6-b482-4868-a7e1-a1f24dde1447",
  "tool_use_result": {
    "content": "Error: result (319,300 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/2d564421-8464-4d87-ad0f-5e3eefeb24a0/tool-results/mcp-agent-ml-research-read_registry-1779392719783.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/2d564421-8464-4d87-ad0f-5e3eefeb24a0/tool-results/mcp-agent-ml-research-read_registry-1779392719783.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/2d564421-8464-4d87-ad0f-5e3eefeb24a0/tool-results/mcp-agent-ml-research-read_registry-1779392719783.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"regex_nomarker_baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T19:03:04.213Z\", \"updated_at\": \"2026-05-21T19:03:23.905Z\", \"hypothesis\": \"Regex baselines (B1-B5) on nomarker condition will show significant degradation, especially B5 which relies on the [No exception data in trace] marker. This reveals the marker-condition B5=99.33% is a format artifact, not genuine code reasoning.\", \"conclusion\": \"success\", \"spec\": {\"command\": \"python eval/regex_baseline.py on nomarker test data\", \"server\": \"westd-11235\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/exception_only_nomarker_test.jsonl\", \"data_count\": 1190, \"model_name\": \"regex_heuristics\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"log_path\": \"N/A\"}, \"completed_at\": \"2026-05-21T19:03:22.128Z\", \"metrics\": {\"B5_marker_acc\": 0.9933, \"B5_nomarker_acc\": 0.2849, \"B5_delta_pp\": -70.84, \"B1_marker_acc\": 0.9345, \"B1_nomarker_acc\": 0.7151, \"B4_marker_acc\": 0.9361, \"B4_nomarker_acc\": 0.9361, \"B5b_nomarker_acc\": 0.9345, \"n\": 1190}}, \"exception_only_padded2048_seed42\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T18:24:05.794Z\", \"updated_at\": \"2026-05-21T18:31:17.479Z\", \"hypothesis\": \"Padding exception_only traces to 2048 tokens (matching full_trace length) with neutral tokens should preserve ~99% accuracy, proving performance gap between exception_only and full_trace is due to information noise not sequence length. Controls for the 13x length confound (150 vs 2048 tokens).\", \"spec\": {\"command\": \"/root/miniconda3/bin/python train/train_sft.py --condition exception_only_padded2048 --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_padded2048_seed42 --wandb_project trace-verdict-study --wandb_run_name exception_only_padded2048_seed42\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"720490\", \"log_path\": \"~/runs/trace-verdict-study/exception_only_padded2048_seed42.log\", \"submitted_at\": \"2026-05-21T18:29:53.466Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/exception_only_padded2048_{train,test}.jsonl\", \"data_count\": 5910, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 42}}, \"fewshot_gpt41_no_trace_0shot\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T18:07:53.581Z\", \"updated_at\": \"2026-05-21T18:12:03.562Z\", \"hypothesis\": \"GPT-4.1 zero-shot on no_trace condition can outperform SFT Qwen-7B because frontier LLMs have stronger code understanding that compensates for missing trace information.\", \"conclusion\": \"success\", \"spec\": {\"command\": \"python eval/fewshot_baseline.py --model gpt41 --condition no_trace --shots 0\", \"server\": \"westd-11235\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/no_trace_test.jsonl\", \"data_count\": 1190, \"model_name\": \"gpt-4.1\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"log_path\": \"/tmp/fewshot_gpt41_no_trace_0shot.log\"}, \"completed_at\": \"2026-05-21T18:10:00.395Z\", \"metrics\": {\"accuracy\": 0.7731, \"fail_f1\": 0.6608}}, \"fewshot_gpt4o_no_trace_0shot\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T18:07:49.983Z\", \"updated_at\": \"2026-05-21T18:12:02.686Z\", \"hypothesis\": \"GPT-4o zero-shot on no_trace condition can outperform SFT Qwen-7B because frontier LLMs have stronger code understanding that compensates for missing trace information.\", \"conclusion\": \"success\", \"spec\": {\"command\": \"python eval/fewshot_baseline.py --model gpt4o --condition no_trace --shots 0\", \"server\": \"westd-11235\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/no_trace_test.jsonl\", \"data_count\": 1190, \"model_name\": \"gpt-4o\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"log_path\": \"/tmp/fewshot_gpt4o_no_trace_0shot.log\"}, \"completed_at\": \"2026-05-21T18:09:54.994Z\", \"metrics\": {\"accuracy\": 0.8445, \"fail_f1\": 0.7543}}, \"fewshot_gpt41_exception_only_3shot\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T18:07:52.778Z\", \"updated_at\": \"2026-05-21T18:12:01.712Z\", \"hypothesis\": \"Adding 3-shot examples to GPT-4.1 improves exception_only verdict prediction over zero-shot by providing task format demonstrations.\", \"conclusion\": \"negative\", \"spec\": {\"command\": \"python eval/fewshot_baseline.py --model gpt41 --condition exception_only --shots 3\", \"server\": \"westd-11235\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/exception_only_test.jsonl\", \"data_count\": 1190, \"model_name\": \"gpt-4.1\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"log_path\": \"/tmp/fewshot_gpt41_exception_only_3shot.log\"}, \"completed_at\": \"2026-05-21T18:09:58.619Z\", \"metrics\": {\"accuracy\": 0.8193, \"fail_f1\": 0.7413}}, \"fewshot_gpt41_exception_only_0shot\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T18:07:51.545Z\", \"updated_at\": \"2026-05-21T18:12:00.304Z\", \"hypothesis\": \"GPT-4.1 zero-shot on exception_only condition performs comparably to GPT-4o because both are frontier models with similar code reasoning capabilities.\", \"conclusion\": \"negative\", \"spec\": {\"command\": \"python eval/fewshot_baseline.py --model gpt41 --condition exception_only --shots 0\", \"server\": \"westd-11235\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/exception_only_test.jsonl\", \"data_count\": 1190, \"model_name\": \"gpt-4.1\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"log_path\": \"/tmp/fewshot_gpt41_exception_only_0shot.log\"}, \"completed_at\": \"2026-05-21T18:09:56.668Z\", \"metrics\": {\"accuracy\": 0.8218, \"fail_f1\": 0.7452}}, \"fewshot_gpt4o_exception_only_3shot\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T18:07:48.528Z\", \"updated_at\": \"2026-05-21T18:11:59.415Z\", \"hypothesis\": \"Adding 3-shot examples to GPT-4o improves exception_only verdict prediction over zero-shot by providing task format demonstrations and calibrating output expectations.\", \"conclusion\": \"negative\", \"spec\": {\"command\": \"python eval/fewshot_baseline.py --model gpt4o --condition exception_only --shots 3\", \"server\": \"westd-11235\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/exception_only_test.jsonl\", \"data_count\": 1190, \"model_name\": \"gpt-4o\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"log_path\": \"/tmp/fewshot_gpt4o_exception_only_3shot.log\"}, \"completed_at\": \"2026-05-21T18:09:52.461Z\", \"metrics\": {\"accuracy\": 0.8681, \"fail_f1\": 0.7995}}, \"fewshot_gpt4o_exception_only_0shot\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T18:07:46.863Z\", \"updated_at\": \"2026-05-21T18:11:58.377Z\", \"hypothesis\": \"Frontier LLM (GPT-4o) with zero-shot prompting can match SFT Qwen-7B on exception_only test verdict prediction because the task may be solvable via general code reasoning without task-specific fine-tuning.\", \"conclusion\": \"negative\", \"spec\": {\"command\": \"python eval/fewshot_baseline.py --model gpt4o --condition exception_only --shots 0\", \"server\": \"westd-11235\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/exception_only_test.jsonl\", \"data_count\": 1190, \"model_name\": \"gpt-4o\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"log_path\": \"/tmp/fewshot_gpt4o_exception_only_0shot.log\"}, \"completed_at\": \"2026-05-21T18:09:49.653Z\", \"metrics\": {\"accuracy\": 0.8798, \"fail_f1\": 0.8228}}, \"deepseek_exception_only_seed123\": {\"status\": \"DONE\", \"retry_count\": 1, \"conclusion\": \"killed\", \"failure_reason\": \"DDL 优先级降低，不再重跑（v2 已完成 99.50%）\", \"created_at\": \"2026-05-15T15:31:02.686Z\", \"updated_at\": \"2026-05-21T15:32:00.000Z\", \"hypothesis\": \"Cross-model seed robustness: exception_only with seed=123 on DeepSeek-Coder-6.7B (plan_008). Further validates exception signal cross-model generalization (99.33% seed42).\", \"reproduce\": {\"finished_at\": \"2026-05-15T20:04:43.247Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T20:04:44.489564+00:00\"}], \"previous_failure\": {\"conclusion\": \"negative\", \"metrics\": {\"accuracy\": 0.9109, \"pass_precision\": 1, \"pass_recall\": 0.993, \"pass_f1\": 0.996, \"fail_precision\": 0.976, \"fail_recall\": 0.705, \"fail_f1\": 0.818, \"ci_95\": [0.894, 0.926], \"train_loss\": 0.122, \"train_runtime_sec\": 6384}, \"notes\": \"NEGATIVE: accuracy 91.09% vs seed42 99.83% (-8.74pp). fail_recall=0.705, train_loss=0.122 偏高。DeepSeek exception_only 对 seed 不鲁棒，seed42 的 99.83% 可能是 LoRA 初始化运气。Exception signal 仍有效（+19.6pp over baseline）但跨模型稳定性不成立。\"}}, \"completed_at\": \"2026-05-15T20:08:02.101Z\", \"notes\": \"NEGATIVE: accuracy 91.09% vs seed42 99.83% (-8.74pp). fail_recall=0.705, train_loss=0.122 偏高。DeepSeek exception_only 对 seed 不鲁棒，seed42 的 99.83% 可能是 LoRA 初始化运气。Exception signal 仍有效（+19.6pp over baseline）但跨模型稳定性不成立。\", \"outputs\": {\"predictions_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_exception_only_seed123/checkpoint-148/predictions.jsonl\"}, \"parent\": \"deepseek_exception_only_seed42\"}, \"codellama13b_label_only_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:23:45.493Z\", \"updated_at\": \"2026-05-21T15:32:00.000Z\", \"conclusion\": \"killed\", \"failure_reason\": \"DDL 优先级降低，不再重跑\"}, \"qwen15b_label_only_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:23:46.314Z\", \"updated_at\": \"2026-05-21T15:32:00.000Z\", \"conclusion\": \"killed\", \"failure_reason\": \"DDL 优先级降低，不再重跑\"}, \"qwen1.5b_no_trace_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:27:36.233Z\", \"updated_at\": \"2026-05-21T15:23:12.652Z\", \"spec\": {\"hypothesis\": \"Multi-scale baseline: no_trace on Qwen-2.5-Coder-1.5B.\", \"model_name\": \"Qwen2.5-Coder-1.5B-Instruct\", \"seed\": 42, \"condition\": \"no_trace\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"account\": \"root\", \"command\": \"export CUDA_VISIBLE_DEVICES=0 && python train/train_sft.py --condition no_trace --gpu 0 --seed 42 --model_name /root/trace-verdict-study/models/Qwen2.5-Coder-1.5B-Instruct --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen1.5b_no_trace_seed42\", \"pid\": \"706059\", \"log_path\": \"/tmp/qwen15b_nt_train.log\", \"submitted_at\": \"2026-05-21T14:48:00Z\", \"submitted_via\": \"tmux\", \"backend\": \"tmux\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/no_trace_train.jsonl\", \"data_count\": 4720, \"checkpoint_source\": \"self-trained\", \"eval_data\": \"no_trace_test.jsonl (1190 samples)\"}, \"conclusion\": \"success\", \"hypothesis\": \"Qwen-1.5B no_trace 应在 65-75% (≈majority baseline)，确认无 trace 小模型表现更差、scale 无法补偿\", \"notes\": \"Eval completed 2026-05-21. Accuracy 72.6% (vs qwen15b_no_trace_seed42 67.31%, +5.3pp). 独立训练 checkpoint（不同训练命令/输出目录），非简单重复。 Lift over majority baseline +1.1pp, CI 含 0 → 不显著。\", \"metrics\": {\"accuracy\": 0.7261, \"accuracy_ci_lower\": 0.7008, \"accuracy_ci_upper\": 0.7529, \"majority_baseline\": 0.7151, \"lift_pp\": 1.09, \"pass_precision\": 0.831, \"pass_recall\": 0.774, \"pass_f1\": 0.802, \"fail_precision\": 0.516, \"fail_recall\": 0.605, \"fail_f1\": 0.557}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen1.5b_no_trace_seed42/final\", \"log_path\": \"/tmp/qwen15b_nt_train.log\"}, \"codellama_exception_only_seed42\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-16T07:27:41.475Z\", \"updated_at\": \"2026-05-21T15:22:00.000Z\", \"spec\": {\"hypothesis\": \"Multi-family validation: exception_only on CodeLlama-13B-Instruct. Tests if exception dominance generalizes to LLaMA family.\", \"model_name\": \"CodeLlama-13b-Instruct-hf\", \"seed\": 42, \"condition\": \"exception_only\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/exception_only_train.jsonl\", \"data_count\": 4720, \"checkpoint_source\": \"self-trained\", \"eval_data\": \"exception_only_test.jsonl (1190 samples)\"}, \"conclusion\": \"killed\", \"failure_reason\": \"确认为 codellama13b_exception_only_seed42 (99.83%) 的重复条目，不需重跑\", \"hypothesis\": \"CodeLlama-13B exception_only 应达 ≥99.33% accuracy，与其他 3 模型一致，确认 minimal sufficient signal 跨 4 模型 3 架构 1.5B-13B universal\", \"notes\": \"重复条目，已在 codellama13b_exception_only_seed42 (99.83%) 完成。命名差异：codellama_ → codellama13b_\"}, \"qwen7b_full_trace_seed456_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T08:06:16.598Z\", \"updated_at\": \"2026-05-21T12:25:14.457Z\", \"hypothesis\": \"Qwen-7B full_trace seed456 应在 ~81% 附近（与 seed42=81.76%, seed123=80.20% 一致），为 MF-3 multi-seed 要求补齐 full_trace 方差估计。3-seed mean 将替换 Table 2 中的占位符。\", \"parent\": \"full_trace_seed42_v5\", \"spec\": {\"command\": \"export CUDA_VISIBLE_DEVICES=1 && python train/train_sft.py --condition full_trace --seed 456 --gpu 0 --gradient_checkpointing --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen7b_full_trace_seed456\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"693144\", \"log_path\": \"/tmp/seed456_train.log\", \"submitted_at\": \"2026-05-21T10:05:00Z\", \"submitted_via\": \"tmux\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/trace-verdict-study/data/full_trace_train.jsonl\", \"data_count\": 4720, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 456, \"checkpoint_source\": \"self-trained\", \"eval_data\": \"full_trace_test.jsonl (1190 samples)\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen7b_full_trace_seed456/final\", \"wall_clock_seconds\": 8387.3, \"gpu_hours\": 2.33}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.8235, \"ci_lower\": 0.8017, \"ci_upper\": 0.8454, \"majority_baseline\": 0.7151, \"lift_pp\": 10.84, \"pass_precision\": 0.8885, \"pass_recall\": 0.8613, \"pass_f1\": 0.8747, \"fail_precision\": 0.6767, \"fail_recall\": 0.7286, \"fail_f1\": 0.7017, \"train_loss\": 0.0416, \"eval_loss\": 0.0794}, \"reproduce\": {\"finished_at\": \"2026-05-21T12:24:44.143Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-21T12:24:47.319Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-21T12:24:54.190947+00:00\"}]}}, \"qwen7b_full_trace_seed123\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-21T07:29:49.744Z\", \"updated_at\": \"2026-05-21T10:07:21.793Z\", \"hypothesis\": \"Qwen-7B full_trace seed123 应在 ~81% 附近（与 seed42=81.76% 一致），为 MF-3 multi-seed 要求补齐 full_trace 方差估计。full_trace 是 C2 \\\"more info hurts\\\" claim 的锚点，单 seed 在 review 中被标记为风险。\", \"parent\": \"full_trace_seed42_v5\", \"server\": \"westd-11235\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-11235\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-21T07:30:12.716Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition full_trace --gpu 0 --seed 123 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen7b_full_trace_seed123 --wandb_project trace-verdict-study --wandb_run_name qwen7b_full_trace_seed123 && python eval/evaluate.py --condition full_trace --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen7b_full_trace_seed123/final --gpu 0 --save_predictions\\\"\", \"code_commit\": \"e404237ccc765768e267d4d6fd3c89549dcf41a4\", \"finished_at\": \"2026-05-21T09:59:10.601Z\", \"training_hours\": 2.48}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"completed_at\": \"2026-05-21T07:32:51.653Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-21T07:32:55.588576+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-21T09:59:17.515644+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python train/train_sft.py --condition full_trace --gpu 0 --seed 123 --gradient_checkpointing --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen7b_full_trace_seed123 --wandb_project trace-verdict-study --wandb_run_name qwen7b_full_trace_seed123_v2\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"686085\", \"log_path\": \"/tmp/seed123_train.log\", \"submitted_at\": \"2026-05-21T15:41:44Z\", \"submitted_via\": \"tmux\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/trace-verdict-study/data/full_trace_train.jsonl\", \"data_count\": 4720, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 123, \"checkpoint_source\": \"self-trained\", \"eval_data\": \"full_trace_test.jsonl (1190 samples)\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen7b_full_trace_seed123/final\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.802, \"ci_lower\": 0.778, \"ci_upper\": 0.825, \"majority_baseline\": 0.715, \"lift_pp\": 8.7, \"pass_precision\": 0.88, \"pass_recall\": 0.84, \"pass_f1\": 0.86, \"fail_precision\": 0.64, \"fail_recall\": 0.7, \"fail_f1\": 0.67, \"train_loss\": 0.0415, \"eval_loss\": 0.0827}}, \"qwen7b_full_trace_seed456\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-21T07:29:51.585Z\", \"updated_at\": \"2026-05-21T08:06:01.308Z\", \"hypothesis\": \"Qwen-7B full_trace seed456 应在 ~81% 附近（与 seed42=81.76% 一致），为 MF-3 multi-seed 要求补齐 full_trace 方差估计。3-seed mean 将替换 Table 2 中的单 seed 值。\", \"parent\": \"full_trace_seed42_v5\", \"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-21T07:30:20.277Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition full_trace --gpu 0 --seed 456 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen7b_full_trace_seed456 --wandb_project trace-verdict-study --wandb_run_name qwen7b_full_trace_seed456 && python eval/evaluate.py --condition full_trace --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen7b_full_trace_seed456/final --gpu 0 --save_predictions\\\"\", \"code_commit\": \"e404237ccc765768e267d4d6fd3c89549dcf41a4\", \"finished_at\": \"2026-05-21T07:33:03.046Z\", \"training_hours\": 0.05}, \"failure_reason\": \"CUDA OOM: CUDA out of memory. Tried to allocate 4.64 GiB. GPU 0 has a total capacity of 94.97 GiB of which 225.56 MiB is free. Including non-PyTorch memory, this process has 94.74 GiB memory in use. Of the allocated memory 87.18 GiB is allocated by PyTorch, an\", \"completed_at\": \"2026-05-21T07:33:08.094Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-21T07:33:15.672357+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python train/train_sft.py --condition full_trace --gpu 0 --seed 456 --gradient_checkpointing --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen7b_full_trace_seed456 --wandb_project trace-verdict-study --wandb_run_name qwen7b_full_trace_seed456\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"683873\", \"log_path\": \"~/runs/trace-verdict-study/qwen7b_full_trace_seed456.log\", \"submitted_at\": \"2026-05-21T15:41:46Z\", \"submitted_via\": \"tmux\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/\", \"data_count\": 4720, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 456, \"checkpoint_source\": \"self-trained\", \"eval_data\": \"full_trace_test.jsonl (1190 samples)\"}, \"conclusion\": \"failed\", \"checkpoint_path\": \"N/A\"}, \"codellama13b_ae_only_seed42\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-19T12:55:37.558Z\", \"updated_at\": \"2026-05-21T07:25:52.875Z\", \"hypothesis\": \"CodeLlama-13B ae_only 应达 95-99% accuracy（介于 exception_only 99.83% 和 loop_only 77.40% 之间），验证 Tier 1/2 hierarchy 跨非 Qwen 架构成立。MF-2 要求至少一个非 Qwen 模型的 component ablation。\", \"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-19T12:56:46.334Z\"}, \"failure_reason\": \"\", \"completed_at\": \"2026-05-19T17:19:54.586Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"command\": \"CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python train/train_sft.py --condition ae_only --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf/ --seed 42 --gradient_checkpointing --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_ae_only_seed42/ --wandb_project trace-verdict-study --wandb_run_name codellama13b_ae_only_seed42\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/\", \"data_count\": 4720, \"model_name\": \"CodeLlama-13b-Instruct-hf\", \"seed\": 42}, \"metrics\": {\"accuracy\": 0.9908, \"accuracy_ci_lower\": 0.9849, \"accuracy_ci_upper\": 0.9958, \"pass_f1\": 0.9935, \"fail_f1\": 0.984, \"majority_baseline\": 0.7151}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_ae_only_seed42/final\", \"log_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_ae_only_seed42/runs/May19_20-58-59_autodl-container-ylrall2a4g-cea5a084\", \"conclusion\": \"success\"}, \"vota_seed42_v5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T01:46:04.015Z\", \"updated_at\": \"2026-05-21T06:31:45.878Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition vota --gpu 1 --wandb_project trace-verdict-study --wandb_run_name vota_seed42_v5\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"940786\", \"log_path\": \"~/runs/trace-verdict-study/vota_seed42_v5.log\", \"submitted_at\": \"2026-05-15T01:46:03.990Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/vota_train.jsonl\", \"data_count\": 4720, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/vota/final/\", \"wall_clock_seconds\": 8443, \"gpu_hours\": 2.35}, \"hypothesis\": \"VOTA trace provides verdict accuracy lift over no-trace baseline (v5: fixed chat template overhead, all labels preserved)\", \"reproduce\": {\"finished_at\": \"2026-05-15T04:08:40.446Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T04:08:41.358997+00:00\"}]}, \"metrics\": {\"accuracy\": 0.9941, \"pass_precision\": 1, \"pass_recall\": 0.9918, \"pass_f1\": 0.9959, \"fail_precision\": 0.9798, \"fail_recall\": 1, \"fail_f1\": 0.9898, \"n\": 1190, \"tp\": 844, \"fp\": 0, \"tn\": 339, \"fn\": 7}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T04:21:27.059Z\"}, \"cross_model_calibration\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T06:14:12.232Z\", \"updated_at\": \"2026-05-21T06:14:57.965Z\", \"hypothesis\": \"Calibration quality (ECE and Brier Score) of exception_only fine-tuned models is universally strong across different model architectures and sizes, not specific to Qwen-7B.\", \"spec\": {\"command\": \"bash eval/run_cross_model_calibration.sh\", \"server\": \"westd-11235\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/exception_only_test.jsonl\", \"data_count\": 1190, \"model_name\": \"Qwen-7B/Qwen-1.5B/CodeLlama-13B/DeepSeek-6.7B\", \"seed\": 42, \"checkpoint_source\": \"exception_only checkpoints for all 4 models\", \"eval_data\": \"exception_only_test.jsonl (1190 samples)\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/cross_model_calibration/\", \"log_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/cross_model_calibration/calibration.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T06:14:57.965Z\"}, \"codellama13b_label_only_seed123_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T21:19:06.021Z\", \"updated_at\": \"2026-05-21T01:06:42.518Z\", \"hypothesis\": \"CodeLlama-13B label_only seed123 确认 collapse 是否 systematic：seed42=28.5% (全预测 fail)，同 DeepSeek collapse pattern。如 seed123 也崩溃 → \\\"label-only collapse is systematic for non-Qwen architectures\\\"。\", \"parent\": \"codellama13b_label_only_seed42_v2\", \"server\": \"westd-11235\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-11235\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-20T21:19:41.720Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition full_trace --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf --gradient_checkpointing --label_only_loss --gpu 0 --seed 123 --output_dir /root/trace-verdict-study/outputs/codellama13b_label_only_seed123_v2 --wandb_project trace-verdict-study --wandb_run_name codellama13b_label_only_seed123_v2 && python eval/evaluate.py --condition full_trace --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf --checkpoint_dir /root/trace-verdict-study/outputs/codellama13b_label_only_seed123_v2/final --gpu 0 --save_predictions\\\"\", \"code_commit\": \"e404237ccc765768e267d4d6fd3c89549dcf41a4\", \"finished_at\": \"2026-05-21T01:02:37.155Z\", \"training_hours\": 3.72}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition full_trace --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf --gradient_checkpointing --label_only_loss --gpu 0 --seed 123 --output_dir /root/trace-verdict-study/outputs/codellama13b_label_only_seed123_v2 --wandb_project trace-verdict-study --wandb_run_name codellama13b_label_only_seed123_v2 && python eval/evaluate.py --condition full_trace --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf --checkpoint_dir /root/trace-verdict-study/outputs/codellama13b_label_only_seed123_v2/final --gpu 0 --save_predictions\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"pid\": \"654451\", \"log_path\": \"~/runs/trace-verdict-study/codellama13b_label_only_seed123_v2.log\", \"submitted_at\": \"2026-05-20T21:19:44.345Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 13375.8, \"gpu_hours\": 3.72}, \"pid\": \"654451\", \"log_path\": \"~/runs/trace-verdict-study/codellama13b_label_only_seed123_v2.log\", \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T01:02:40.132Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-21T01:02:44.162900+00:00\"}]}, \"metrics\": {\"accuracy\": \"collapsed\", \"eval_loss\": \"nan\", \"train_loss_final\": 0, \"grad_norm_final\": 0, \"entropy\": 0.25, \"note\": \"full collapse identical to seed42 (28.5%), eval never ran due to disk full but collapse confirmed from training metrics\"}}, \"qwen15b_no_trace_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T21:55:15.016Z\", \"updated_at\": \"2026-05-20T22:15:15.854Z\", \"hypothesis\": \"Qwen-1.5B no_trace 第 3 seed：seed42=67.31% vs seed123=75.88% 差 8.57pp，seed42 疑为异常值。seed456 确定 3-seed mean，判断 67.31% 是否 outlier。\", \"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-20T21:55:35.973Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition no_trace --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --gradient_checkpointing --gpu 0 --seed 456 --output_dir /root/trace-verdict-study/outputs/qwen15b_no_trace_seed456 --wandb_project trace-verdict-study --wandb_run_name qwen15b_no_trace_seed456 && python eval/evaluate.py --condition no_trace --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --checkpoint_dir /root/trace-verdict-study/outputs/qwen15b_no_trace_seed456/final --gpu 0 --save_predictions\\\"\", \"code_commit\": \"e404237ccc765768e267d4d6fd3c89549dcf41a4\", \"finished_at\": \"2026-05-20T22:12:44.259Z\", \"training_hours\": 0.29}, \"spec\": {\"data_path\": \"/root/trace-verdict-study/data/\", \"data_count\": 1640, \"model_name\": \"Qwen2.5-Coder-1.5B-Instruct\", \"seed\": 456}, \"pid\": \"657684\", \"log_path\": \"~/runs/trace-verdict-study/qwen15b_no_trace_seed456.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T22:12:48.771215+00:00\"}]}, \"metrics\": {\"accuracy\": 0.7387, \"fail_f1\": 0.5266, \"pass_f1\": 0.8195, \"eval_loss\": 0.7725, \"train_loss\": 0.2226, \"fail_precision\": 0.544, \"fail_recall\": 0.5103, \"pass_precision\": 0.8096, \"pass_recall\": 0.8296}, \"checkpoint_path\": \"/root/trace-verdict-study/outputs/qwen15b_no_trace_seed456/final\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T22:15:15.854Z\"}, \"qwen15b_no_trace_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T21:30:56.732Z\", \"updated_at\": \"2026-05-20T21:54:59.519Z\", \"hypothesis\": \"Qwen-1.5B no_trace 加第 2 seed：seed42=67.31% 是 C2 分解的 baseline 端，单 seed 易被质疑为 seed 运气差。seed123 加固 baseline 使分解更 robust。\", \"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-20T21:31:34.186Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition no_trace --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --gradient_checkpointing --gpu 0 --seed 123 --output_dir /root/trace-verdict-study/outputs/qwen15b_no_trace_seed123 --wandb_project trace-verdict-study --wandb_run_name qwen15b_no_trace_seed123 && python eval/evaluate.py --condition no_trace --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --checkpoint_dir /root/trace-verdict-study/outputs/qwen15b_no_trace_seed123/final --gpu 0 --save_predictions\\\"\", \"code_commit\": \"e404237ccc765768e267d4d6fd3c89549dcf41a4\", \"finished_at\": \"2026-05-20T21:52:47.650Z\", \"training_hours\": 0.35}, \"spec\": {\"data_path\": \"/root/trace-verdict-study/data/\", \"data_count\": 1640, \"model_name\": \"Qwen2.5-Coder-1.5B-Instruct\", \"seed\": 123}, \"pid\": \"655666\", \"log_path\": \"~/runs/trace-verdict-study/qwen15b_no_trace_seed123.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T21:52:52.119376+00:00\"}]}, \"metrics\": {\"accuracy\": 0.7588, \"accuracy_ci_lower\": 0.7328, \"accuracy_ci_upper\": 0.7824, \"majority_baseline\": 0.7151, \"lift\": 0.0437, \"pass_precision\": 0.8279, \"pass_recall\": 0.8367, \"pass_f1\": 0.8323, \"fail_precision\": 0.5788, \"fail_recall\": 0.5634, \"fail_f1\": 0.571, \"train_loss\": 0.2221, \"eval_loss\": 0.7838}, \"checkpoint_path\": \"/root/trace-verdict-study/outputs/qwen15b_no_trace_seed123/final\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T21:54:59.519Z\"}, \"qwen15b_label_only_seed456_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T20:17:58.672Z\", \"updated_at\": \"2026-05-20T21:35:38.062Z\", \"hypothesis\": \"Qwen-1.5B label_only 第3 seed 降低 variance：2-seed mean=80.13±1.72% (variance > Qwen-7B 的 1.12%)，第3 seed 使数据与 Qwen-7B 3-seed 可比。\", \"parent\": \"qwen15b_label_only_seed42_v2\", \"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-20T20:18:26.641Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition full_trace --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --gradient_checkpointing --label_only_loss --gpu 0 --seed 456 --output_dir /root/trace-verdict-study/outputs/qwen15b_label_only_seed456_v2 --wandb_project trace-verdict-study --wandb_run_name qwen15b_label_only_seed456_v2 && python eval/evaluate.py --condition full_trace --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --checkpoint_dir /root/trace-verdict-study/outputs/qwen15b_label_only_seed456_v2/final --gpu 0 --save_predictions\\\"\", \"code_commit\": \"e404237ccc765768e267d4d6fd3c89549dcf41a4\", \"finished_at\": \"2026-05-20T21:13:54.135Z\", \"training_hours\": 0.92}, \"spec\": {\"data_path\": \"/root/trace-verdict-study/data/\", \"data_count\": 1640, \"model_name\": \"Qwen2.5-Coder-1.5B-Instruct\", \"seed\": 456, \"checkpoint_source\": \"self-trained\", \"eval_data\": \"trace-verdict-study test split (164 samples)\"}, \"pid\": \"651166\", \"log_path\": \"~/runs/trace-verdict-study/qwen15b_label_only_seed456_v2.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T21:13:58.818964+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.8252, \"pass_f1\": 0.885, \"fail_f1\": 0.639, \"pass_precision\": 0.837, \"pass_recall\": 0.938, \"fail_precision\": 0.776, \"fail_recall\": 0.543, \"train_loss\": 0.2394, \"eval_loss\": 0.3064, \"majority_baseline\": 0.715}, \"checkpoint_path\": \"/root/trace-verdict-study/outputs/qwen15b_label_only_seed456_v2/final\", \"completed_at\": \"2026-05-20T21:35:38.062Z\"}, \"deepseek_no_trace_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T21:19:12.571Z\", \"updated_at\": \"2026-05-20T21:31:26.419Z\", \"hypothesis\": \"DeepSeek no_trace 只有 1 seed (73.36%)，加第 2 seed 使 baseline 更 robust。no_trace 是所有条件对比的锚点，单 seed baseline 在 rebuttal 中易被质疑。\", \"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-20T21:19:48.734Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition no_trace --model_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct --gradient_checkpointing --gpu 0 --seed 123 --output_dir /root/trace-verdict-study/outputs/deepseek_no_trace_seed123 --wandb_project trace-verdict-study --wandb_run_name deepseek_no_trace_seed123 && python eval/evaluate.py --condition no_trace --model_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct --checkpoint_dir /root/trace-verdict-study/outputs/deepseek_no_trace_seed123/final --gpu 0 --save_predictions\\\"\", \"code_commit\": \"e404237ccc765768e267d4d6fd3c89549dcf41a4\"}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition no_trace --model_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct --gradient_checkpointing --gpu 0 --seed 123 --output_dir /root/trace-verdict-study/outputs/deepseek_no_trace_seed123 --wandb_project trace-verdict-study --wandb_run_name deepseek_no_trace_seed123 && python eval/evaluate.py --condition no_trace --model_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct --checkpoint_dir /root/trace-verdict-study/outputs/deepseek_no_trace_seed123/final --gpu 0 --save_predictions\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"654604\", \"log_path\": \"~/runs/trace-verdict-study/deepseek_no_trace_seed123.log\", \"submitted_at\": \"2026-05-20T21:19:50.736Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 695.7, \"gpu_hours\": 0.19}, \"pid\": \"654604\", \"log_path\": \"~/runs/trace-verdict-study/deepseek_no_trace_seed123.log\", \"conclusion\": \"killed\", \"checkpoint_path\": \"N/A (killed before completion)\", \"completed_at\": \"2026-05-20T21:31:26.419Z\"}, \"codellama13b_label_only_seed42_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:24:00.685Z\", \"updated_at\": \"2026-05-20T21:18:58.996Z\", \"spec\": {\"command\": \"...full_trace --label_only_loss --model_path CodeLlama-13b-Instruct-hf...\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"pid\": \"642747\", \"log_path\": \"~/runs/trace-verdict-study/codellama13b_label_only_seed42_v2.log\", \"submitted_at\": \"2026-05-20T17:24:00.283Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/trace-verdict-study/data/\", \"data_count\": 1640, \"model_name\": \"CodeLlama-13B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"self-trained\", \"eval_data\": \"trace-verdict-study test split (164 samples)\", \"wall_clock_seconds\": 14098.7, \"gpu_hours\": 3.92}, \"hypothesis\": \"CodeLlama-13B label_only (full_trace with label-only loss) 验证 C2 decomposition 跨架构泛化：Qwen-7B label_only=86.22%, DeepSeek label_only=28.5%. CodeLlama 是第 3 个架构数据点。\", \"metrics\": {\"accuracy\": 0.2849, \"accuracy_ci_lower\": 0.2613, \"accuracy_ci_upper\": 0.3084, \"majority_baseline\": 0.7151, \"lift_pp\": -43.03, \"pass_recall\": 0, \"pass_precision\": 0, \"pass_f1\": 0, \"fail_recall\": 1, \"fail_precision\": 0.2849, \"fail_f1\": 0.4434}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_label_only_seed42_v2/final\", \"completed_at\": \"2026-05-20T21:18:58.996Z\"}, \"qwen15b_label_only_seed123_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T19:20:03.067Z\", \"updated_at\": \"2026-05-20T20:18:04.354Z\", \"hypothesis\": \"Qwen-1.5B label_only seed123 验证 C2 decomposition 跨 seed 稳定性：seed42=78.9%, 第 2 seed 确认 label formatting 贡献约 11pp (vs no_trace 67.31%)。\", \"parent\": \"qwen15b_label_only_seed42_v2\", \"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-20T19:20:24.443Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition full_trace --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --gradient_checkpointing --label_only_loss --gpu 0 --seed 123 --output_dir /root/trace-verdict-study/outputs/qwen15b_label_only_seed123_v2 --wandb_project trace-verdict-study --wandb_run_name qwen15b_label_only_seed123_v2 && python eval/evaluate.py --condition full_trace --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --checkpoint_dir /root/trace-verdict-study/outputs/qwen15b_label_only_seed123_v2/final --gpu 0 --save_predictions\\\"\", \"code_commit\": \"e404237ccc765768e267d4d6fd3c89549dcf41a4\", \"finished_at\": \"2026-05-20T20:15:42.280Z\", \"training_hours\": 0.92}, \"spec\": {\"data_path\": \"/root/trace-verdict-study/data/\", \"data_count\": 1640, \"model_name\": \"Qwen2.5-Coder-1.5B-Instruct\", \"seed\": 123, \"checkpoint_source\": \"self-trained\", \"eval_data\": \"trace-verdict-study test split (164 samples)\"}, \"pid\": \"648034\", \"log_path\": \"~/runs/trace-verdict-study/qwen15b_label_only_seed123_v2.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T20:15:46.560837+00:00\"}]}, \"metrics\": {\"accuracy\": 0.8134, \"accuracy_ci_lower\": 0.7924, \"accuracy_ci_upper\": 0.8345, \"majority_baseline\": 0.7151, \"lift_pp\": 9.83, \"pass_recall\": 0.94, \"pass_precision\": 0.824, \"pass_f1\": 0.878, \"fail_recall\": 0.496, \"fail_precision\": 0.767, \"fail_f1\": 0.602}, \"checkpoint_path\": \"/root/trace-verdict-study/outputs/qwen15b_label_only_seed123_v2/final\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T20:18:04.354Z\"}, \"qwen15b_label_only_seed42_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:24:03.330Z\", \"updated_at\": \"2026-05-20T19:18:53.550Z\", \"spec\": {\"command\": \"...full_trace --label_only_loss --model_path Qwen2.5-Coder-1.5B-Instruct...\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"642828\", \"log_path\": \"~/runs/trace-verdict-study/qwen15b_label_only_seed42_v2.log\", \"submitted_at\": \"2026-05-20T17:24:02.903Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/trace-verdict-study/data/\", \"data_count\": 1640, \"model_name\": \"Qwen2.5-Coder-1.5B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"self-trained\", \"eval_data\": \"trace-verdict-study test split (164 samples)\", \"wall_clock_seconds\": 6890.6, \"gpu_hours\": 1.91}, \"hypothesis\": \"Qwen-1.5B label_only (full_trace with label-only loss) 验证 C2 decomposition 跨 scale 泛化：Qwen-7B label_only=86.22%, Qwen-1.5B 是同架构不同 scale 的验证点。\", \"metrics\": {\"accuracy\": 0.789, \"accuracy_ci_lower\": 0.766, \"accuracy_ci_upper\": 0.812, \"majority_baseline\": 0.715, \"lift_pp\": 7.4, \"pass_recall\": 0.91, \"pass_precision\": 0.82, \"pass_f1\": 0.86, \"fail_recall\": 0.5, \"fail_precision\": 0.68, \"fail_f1\": 0.57}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/trace-verdict-study/outputs/qwen15b_label_only_seed42_v2/checkpoint-444\", \"completed_at\": \"2026-05-20T19:18:53.550Z\"}, \"qwen15b_ae_only_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T16:20:46.263Z\", \"updated_at\": \"2026-05-20T17:23:38.815Z\", \"spec\": {\"command\": \"bash -c \\\"...qwen15b_ae_only_seed123...\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"638597\", \"log_path\": \"~/runs/trace-verdict-study/qwen15b_ae_only_seed123.log\", \"submitted_at\": \"2026-05-20T16:20:45.493Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/trace-verdict-study/data/\", \"data_count\": 1640, \"model_name\": \"Qwen2.5-Coder-1.5B-Instruct\", \"seed\": 123, \"checkpoint_source\": \"self-trained\", \"eval_data\": \"trace-verdict-study test split (164 samples)\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_ae_only_seed123/final/\", \"wall_clock_seconds\": 3773.3, \"gpu_hours\": 1.05}, \"hypothesis\": \"Qwen-1.5B ae_only seed123 应 ≥98%（seed42=99.08%），补齐 Table 1 ae_only 行中 Qwen-1.5B 的 2-seed 覆盖\", \"parent\": \"qwen15b_ae_only_seed42\", \"metrics\": {\"accuracy\": 0.9857, \"majority_baseline\": 0.715, \"lift_pp\": 27.1, \"fail_f1\": 0.975}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T17:23:38.815Z\"}, \"deepseek_loop_only_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T14:55:41.209Z\", \"updated_at\": \"2026-05-20T17:23:37.284Z\", \"spec\": {\"command\": \"bash -c \\\"...deepseek_loop_only_seed456...\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"pid\": \"633962\", \"log_path\": \"~/runs/trace-verdict-study/deepseek_loop_only_seed456.log\", \"submitted_at\": \"2026-05-20T14:55:40.756Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/trace-verdict-study/data/\", \"data_count\": 1640, \"model_name\": \"DeepSeek-Coder-6.7B-Instruct\", \"seed\": 456, \"checkpoint_source\": \"self-trained\", \"eval_data\": \"trace-verdict-study test split (164 samples)\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_loop_only_seed456/final/\", \"wall_clock_seconds\": 8876.5, \"gpu_hours\": 2.47}, \"hypothesis\": \"DeepSeek loop_only seed456 验证 3-seed 稳定性：当前 seed42=seed123=81.26% (std=0)，reviewer 会质疑。第 3 seed 确认或修正这个异常一致性。\", \"parent\": \"deepseek_loop_only_seed42\", \"metrics\": {\"accuracy\": 0.784, \"majority_baseline\": 0.715, \"lift_pp\": 6.9, \"fail_f1\": 0.63}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T17:23:37.285Z\"}, \"qwen15b_vota_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T15:23:45.586Z\", \"updated_at\": \"2026-05-20T16:19:33.540Z\", \"spec\": {\"command\": \"bash -c \\\"...qwen15b_vota_seed123...\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"635814\", \"log_path\": \"~/runs/trace-verdict-study/qwen15b_vota_seed123.log\", \"submitted_at\": \"2026-05-20T15:23:45.139Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/trace-verdict-study/data/\", \"data_count\": 1640, \"model_name\": \"Qwen2.5-Coder-1.5B-Instruct\", \"seed\": 123, \"checkpoint_source\": \"self-trained\", \"eval_data\": \"trace-verdict-study test split (164 samples)\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_vota_seed123/final/\", \"wall_clock_seconds\": 3348.4, \"gpu_hours\": 0.93}, \"hypothesis\": \"Qwen-1.5B VOTA seed123 应 ≥98%（seed42=99.58%），补齐 C4 VOTA universality 的 Qwen-1.5B 2-seed 覆盖\", \"parent\": \"qwen15b_vota_seed42\", \"metrics\": {\"accuracy\": 0.995, \"ci_95\": [0.9908, 0.9983], \"pass_f1\": 0.9965, \"fail_f1\": 0.9912, \"lift_pp\": 28, \"n_samples\": 1190}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T16:19:33.540Z\"}, \"deepseek_ae_only_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T12:46:47.345Z\", \"updated_at\": \"2026-05-20T15:24:01.445Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition ae_only --model_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct --gradient_checkpointing --gpu 0 --seed 123 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_ae_only_seed123 --wandb_project trace-verdict-study --wandb_run_name deepseek_ae_only_seed123 && python eval/evaluate.py --condition ae_only --model_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_ae_only_seed123/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_ae_only_seed123/final/eval_results.json --save_predictions --max_length 2048\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"626709\", \"log_path\": \"~/runs/trace-verdict-study/deepseek_ae_only_seed123.log\", \"submitted_at\": \"2026-05-20T12:46:46.933Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/trace-verdict-study/data/\", \"data_count\": 1640, \"model_name\": \"DeepSeek-Coder-6.7B-Instruct\", \"seed\": 123, \"wall_clock_seconds\": 9299.3, \"gpu_hours\": 2.58}, \"hypothesis\": \"Cross-seed validation for ae_only on DeepSeek-6.7B: seed42 achieved 99.08%, seed123 should confirm ae_only's cross-seed robustness on DeepSeek (strengthening C2 ae_only universality claim)\", \"reproduce\": {\"finished_at\": \"2026-05-20T15:17:53.732Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T15:17:57.838508+00:00\"}]}, \"metrics\": {\"accuracy\": 0.9832}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_ae_only_seed123/final/\", \"log_path\": \"~/runs/trace-verdict-study/deepseek_ae_only_seed123.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T15:21:46.249Z\"}, \"qwen15b_loop_only_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T13:35:56.439Z\", \"updated_at\": \"2026-05-20T14:54:32.548Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition loop_only --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --gradient_checkpointing --gpu 0 --seed 456 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_loop_only_seed456 --wandb_project trace-verdict-study --wandb_run_name qwen15b_loop_only_seed456 && python eval/evaluate.py --condition loop_only --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_loop_only_seed456/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_loop_only_seed456/final/eval_results.json --save_predictions\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"pid\": \"630189\", \"log_path\": \"~/runs/trace-verdict-study/qwen15b_loop_only_seed456.log\", \"submitted_at\": \"2026-05-20T13:35:55.990Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/trace-verdict-study/data/\", \"data_count\": 1640, \"model_name\": \"Qwen2.5-Coder-1.5B-Instruct\", \"seed\": 456, \"checkpoint_source\": \"self-trained\", \"eval_data\": \"trace-verdict-study test split (164 samples)\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_loop_only_seed456/final/\", \"wall_clock_seconds\": 4716.6, \"gpu_hours\": 1.31}, \"hypothesis\": \"Qwen-1.5B loop_only seed456 应在 76-84%（与 seed42=78.32%, seed123=81.09% 接近），补齐 3-seed mean 确认 Tier 2 loop_only 跨种子稳定性\", \"parent\": \"qwen15b_loop_only_seed42\", \"metrics\": {\"accuracy\": 0.792, \"ci_95\": [0.768, 0.813], \"majority_baseline\": 0.715, \"lift_pp\": 7.6, \"pass_precision\": 0.85, \"pass_recall\": 0.86, \"pass_f1\": 0.86, \"fail_precision\": 0.64, \"fail_recall\": 0.62, \"fail_f1\": 0.63}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T14:54:32.548Z\"}, \"codellama13b_loop_only_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T09:03:02.178Z\", \"updated_at\": \"2026-05-20T13:14:57.428Z\", \"spec\": {\"command\": \"train_sft.py --condition loop_only + evaluate.py\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"pid\": \"609613\", \"log_path\": \"~/runs/trace-verdict-study/codellama13b_loop_only_seed456.log\", \"submitted_at\": \"2026-05-20T09:03:01.670Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/trace-verdict-study/data/\", \"data_count\": 1190, \"model_name\": \"CodeLlama-13B-Instruct\", \"seed\": 456, \"wall_clock_seconds\": 14064.0, \"gpu_hours\": 3.91}, \"reproduce\": {\"finished_at\": \"2026-05-20T12:53:42.048Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T12:53:45.150978+00:00\"}]}, \"metrics\": {\"accuracy\": 0.7908, \"majority_baseline\": 0.7151, \"lift\": 0.0757, \"pass_precision\": 0.912, \"pass_recall\": 0.783, \"pass_f1\": 0.843, \"fail_precision\": 0.598, \"fail_recall\": 0.811, \"fail_f1\": 0.688, \"n\": 1190}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_loop_only_seed456/final\", \"log_path\": \"/root/runs/trace-verdict-study/codellama13b_loop_only_seed456.log\", \"conclusion\": \"success\", \"hypothesis\": \"CodeLlama-13B loop_only seed456 应在 74-80% 范围（与 seed42=77.06%, seed123=76.05% 接近），验证 Tier 2 loop_only 在 13B scale 的跨 seed 稳定性\", \"completed_at\": \"2026-05-20T12:57:25.720Z\", \"parent\": \"codellama13b_loop_only_seed42\"}, \"qwen15b_exception_only_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T20:35:25.949Z\", \"updated_at\": \"2026-05-20T12:56:37.525Z\", \"hypothesis\": \"Qwen-1.5B exception_only seed123 应达 ~99.83%（与 seed42 一致），为 W3 reviewer concern 提供 1.5B scale 的方差估计\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition exception_only --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --gradient_checkpointing --gpu 0 --seed 123 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_exception_only_seed123 --wandb_project trace-verdict-study --wandb_run_name qwen15b_exception_only_seed123 && python eval/evaluate.py --condition exception_only --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_exception_only_seed123/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_exception_only_seed123/final/eval_results.json --save_predictions\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"pid\": \"627797\", \"log_path\": \"~/runs/trace-verdict-study/qwen15b_exception_only_seed123.log\", \"submitted_at\": \"2026-05-20T12:56:36.946Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"failed\", \"metrics\": {\"error\": \"CUDA OOM at step 3/444\", \"exit_code\": 1, \"cause\": \"GPU 0 had 45.15 GiB PyTorch allocated (likely concurrent model loading with codellama13b), only 1.80 GiB free when trying to allocate 4.64 GiB\", \"seed_comparison\": {\"seed42_accuracy\": 0.9983, \"seed123_accuracy\": \"N/A - OOM crash\"}}, \"completed_at\": \"2026-05-18T21:40:33.694Z\"}, \"qwen15b_loop_only_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:54:39.904Z\", \"updated_at\": \"2026-05-20T12:44:20.419Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition loop_only --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --gradient_checkpointing --gpu 0 --seed 123 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_loop_only_seed123 --wandb_project trace-verdict-study --wandb_run_name qwen15b_loop_only_seed123 && python eval/evaluate.py --condition loop_only --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_loop_only_seed123/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_loop_only_seed123/final/eval_results.json --save_predictions\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"623714\", \"log_path\": \"~/runs/trace-verdict-study/qwen15b_loop_only_seed123.log\", \"submitted_at\": \"2026-05-20T11:54:39.487Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/loop_only_train.jsonl\", \"data_count\": 4720, \"model_name\": \"Qwen2.5-Coder-1.5B-Instruct\", \"seed\": 123, \"checkpoint_source\": \"self-trained\", \"eval_data\": \"/root/autodl-tmp/trace-verdict-study-data/loop_only_test.jsonl\", \"wall_clock_seconds\": 2980.9, \"gpu_hours\": 0.83}, \"reproduce\": {\"finished_at\": \"2026-05-20T12:40:47.934Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T12:40:50.915806+00:00\"}]}, \"hypothesis\": \"Qwen-1.5B loop_only seed123 应与 seed42 (78.32%) 接近，验证 Tier 2 loop_only 在 1.5B scale 的跨 seed 稳定性\", \"parent\": \"qwen15b_loop_only_seed42\", \"metrics\": {\"accuracy\": 0.8109, \"pass_f1\": 0.8737, \"fail_f1\": 0.6244, \"pass_precision\": 0.8366, \"pass_recall\": 0.9142, \"fail_precision\": 0.7192, \"fail_recall\": 0.5516, \"train_loss\": 0.0843, \"train_runtime_sec\": 2659.73}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_loop_only_seed123/final/\", \"log_path\": \"~/runs/trace-verdict-study/qwen15b_loop_only_seed123.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T12:44:20.419Z\"}, \"codellama13b_vota_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T03:10:20.719Z\", \"updated_at\": \"2026-05-20T11:35:28.253Z\", \"hypothesis\": \"CodeLlama-13B VOTA seed123 应在 97-100%（与 seed42=98.57% 接近），验证 VOTA Tier 1 跨 seed 稳定性\", \"parent\": \"codellama13b_vota_seed42\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && ...\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"601095\", \"log_path\": \"~/runs/trace-verdict-study/codellama13b_vota_seed123.log\", \"submitted_at\": \"2026-05-20T07:35:22.845Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/vota_train.jsonl\", \"data_count\": 4720, \"model_name\": \"CodeLlama-13B-Instruct-hf\", \"seed\": 123, \"checkpoint_source\": \"self-trained\", \"eval_data\": \"/root/autodl-tmp/trace-verdict-study-data/vota_test.jsonl\", \"wall_clock_seconds\": 14382.3, \"gpu_hours\": 4.0}, \"reproduce\": {\"finished_at\": \"2026-05-20T11:32:16.006Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T11:32:20.242389+00:00\"}]}, \"metrics\": {\"accuracy\": 0.9891, \"accuracy_ci\": [0.9832, 0.9941], \"pass_precision\": 0.9929, \"pass_recall\": 0.9918, \"pass_f1\": 0.9924, \"fail_precision\": 0.9794, \"fail_recall\": 0.9823, \"fail_f1\": 0.9809, \"n\": 1190, \"majority_baseline\": 0.7151, \"lift\": 0.2739}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_vota_seed123/final\", \"log_path\": \"~/runs/trace-verdict-study/codellama13b_vota_seed123.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T11:35:05.193Z\"}, \"qwen15b_loop_only_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T07:51:37.747Z\", \"updated_at\": \"2026-05-20T08:44:07.965Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition loop_only --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_loop_only_seed42 --wandb_project trace-verdict-study --wandb_run_name qwen15b_loop_only_seed42 && python eval/evaluate.py --condition loop_only --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_loop_only_seed42/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_loop_only_seed42/final/eval_results.json --save_predictions\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"pid\": \"602560\", \"log_path\": \"~/runs/trace-verdict-study/qwen15b_loop_only_seed42.log\", \"submitted_at\": \"2026-05-20T07:51:37.348Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/loop_only_train.jsonl\", \"data_count\": 4720, \"model_name\": \"Qwen2.5-Coder-1.5B-Instruct\", \"seed\": 42, \"wall_clock_seconds\": 3102.7, \"gpu_hours\": 0.86}, \"reproduce\": {\"finished_at\": \"2026-05-20T08:39:30.273Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T08:39:33.542076+00:00\"}]}, \"hypothesis\": \"Qwen-1.5B loop_only 应在 75-85% 范围（与 Qwen-7B 86%/CodeLlama-13B 77%/DeepSeek 81% 对比），验证 Tier 2 loop_only 在最小 scale (1.5B) 的表现，观察 scale 对 Tier 2 信号密度条件的影响\", \"metrics\": {\"accuracy\": 0.7832, \"pass_f1\": 0.8526, \"fail_f1\": 0.5905, \"pass_precision\": 0.8298, \"pass_recall\": 0.8766, \"fail_precision\": 0.6392, \"fail_recall\": 0.5487, \"train_loss\": 0.0847, \"train_runtime_sec\": 2679}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_loop_only_seed42/final/\", \"log_path\": \"~/runs/trace-verdict-study/qwen15b_loop_only_seed42.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T08:43:20.070Z\"}, \"qwen15b_ae_only_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T06:52:17.793Z\", \"updated_at\": \"2026-05-20T07:50:58.882Z\", \"hypothesis\": \"Qwen-1.5B ae_only 应达 ≥95% accuracy，与 Qwen-7B (99.92%) / CodeLlama-13B (99.08%) / DeepSeek (98.74%) 一致，验证 Tier 1 ae_only 在最小 scale (1.5B) 仍然有效\", \"parent\": \"qwen15b_exception_only_seed42\", \"spec\": {\"command\": \"bash -c \\\"...qwen15b_ae_only_seed42...\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"pid\": \"598258\", \"log_path\": \"~/runs/trace-verdict-study/qwen15b_ae_only_seed42.log\", \"submitted_at\": \"2026-05-20T06:52:39.041Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/ae_only_train.jsonl\", \"data_count\": 4720, \"model_name\": \"Qwen2.5-Coder-1.5B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"self-trained\", \"eval_data\": \"/root/autodl-tmp/trace-verdict-study-data/ae_only_test.jsonl\", \"wall_clock_seconds\": 3499.8, \"gpu_hours\": 0.97}, \"reproduce\": {\"finished_at\": \"2026-05-20T07:46:34.828Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T07:46:39.544624+00:00\"}]}, \"metrics\": {\"accuracy\": 0.9908, \"majority_baseline\": 0.7151, \"lift\": 0.2756, \"pass_precision\": 1, \"pass_recall\": 0.987, \"pass_f1\": 0.9935, \"fail_precision\": 0.9686, \"fail_recall\": 1, \"fail_f1\": 0.984, \"n\": 1190, \"accuracy_ci_lower\": 0.9849, \"accuracy_ci_upper\": 0.9958}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_ae_only_seed42/final/\", \"log_path\": \"~/runs/trace-verdict-study/qwen15b_ae_only_seed42.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T07:50:58.882Z\"}, \"codellama13b_ae_only_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T03:04:54.397Z\", \"updated_at\": \"2026-05-20T07:33:40.315Z\", \"hypothesis\": \"CodeLlama-13B ae_only seed123 应在 98-100% 范围（与 seed42=99.08% 接近），验证 Tier 1 ae_only 跨 seed 稳定性（rebuttal 储备）\", \"parent\": \"codellama13b_ae_only_seed42\", \"spec\": {\"command\": \"bash -c \\\"...codellama13b_ae_only_seed123...\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"583496\", \"log_path\": \"~/runs/trace-verdict-study/codellama13b_ae_only_seed123.log\", \"submitted_at\": \"2026-05-20T03:05:13.102Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/ae_only_train.jsonl\", \"data_count\": 4720, \"model_name\": \"codellama/CodeLlama-13b-Instruct-hf\", \"seed\": 123, \"checkpoint_source\": \"self-trained\", \"eval_data\": \"/root/autodl-tmp/trace-verdict-study-data/ae_only_test.jsonl\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_ae_only_seed123/final\", \"wall_clock_seconds\": 15624.3, \"gpu_hours\": 4.34}, \"reproduce\": {\"finished_at\": \"2026-05-20T07:31:03.573Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T07:31:08.333919+00:00\"}]}, \"metrics\": {\"accuracy\": 0.9908, \"accuracy_ci_lower\": 0.9849, \"accuracy_ci_upper\": 0.9958, \"pass_precision\": 1, \"pass_recall\": 0.987, \"pass_f1\": 0.993, \"fail_precision\": 0.969, \"fail_recall\": 1, \"fail_f1\": 0.984, \"train_loss\": 0.0592, \"train_runtime_sec\": 15624, \"gpu_hours\": 4.34}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T07:33:40.315Z\"}, \"deepseek_exception_only_seed123_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T04:59:58.895Z\", \"updated_at\": \"2026-05-20T06:51:44.480Z\", \"hypothesis\": \"DeepSeek exception_only seed123 在当前代码下应 ≥98%（与 seed42=99.33% 接近），验证 5/15 的 91.09% 是否为代码旧版本导致\", \"parent\": \"deepseek_exception_only_seed42\", \"spec\": {\"command\": \"bash -c \\\"...deepseek_exception_only_seed123_v2...\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"pid\": \"591985\", \"log_path\": \"~/runs/trace-verdict-study/deepseek_exception_only_seed123_v2.log\", \"submitted_at\": \"2026-05-20T05:00:15.656Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/exception_only_train.jsonl\", \"data_count\": 4720, \"model_name\": \"deepseek-ai/deepseek-coder-6.7b-instruct\", \"seed\": 123, \"checkpoint_source\": \"self-trained\", \"eval_data\": \"/root/autodl-tmp/trace-verdict-study-data/exception_only_test.jsonl\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_exception_only_seed123_v2/final/\", \"wall_clock_seconds\": 6669.2, \"gpu_hours\": 1.85}, \"reproduce\": {\"finished_at\": \"2026-05-20T06:47:54.611Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T06:47:59.099687+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.995}, \"completed_at\": \"2026-05-20T06:51:24.856Z\"}, \"deepseek_vota_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T02:35:59.967Z\", \"updated_at\": \"2026-05-20T04:58:10.410Z\", \"hypothesis\": \"DeepSeek VOTA seed456 第 3 seed 仲裁：seed42=84.45% vs seed123=99.16% 差距 14.71pp。若 seed456 ∈ [95%, 100%] 则 seed42 是 outlier，DeepSeek VOTA 归 Tier 1；若 ∈ [82%, 88%] 则 VOTA 在 DeepSeek 上高方差，需重新评估 Tier 归属\", \"parent\": \"deepseek_vota_seed123\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition vota --model_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_vota_seed456 --gradient_checkpointing --gpu 0 --seed 456 --wandb_project trace-verdict-study --wandb_run_name deepseek_vota_seed456 && python eval/evaluate.py --condition vota --model_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_vota_seed456/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_vota_seed456/final/eval_results.json --save_predictions --max_length 2048\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"pid\": \"579517\", \"log_path\": \"~/runs/trace-verdict-study/deepseek_vota_seed456.log\", \"submitted_at\": \"2026-05-20T02:36:17.947Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/vota_train.jsonl\", \"data_count\": 4720, \"model_name\": \"deepseek-ai/deepseek-coder-6.7b-instruct\", \"seed\": 456, \"checkpoint_source\": \"self-trained\", \"eval_data\": \"/root/autodl-tmp/trace-verdict-study-data/vota_test.jsonl\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_vota_seed456/final\", \"wall_clock_seconds\": 8512.5, \"gpu_hours\": 2.36}, \"reproduce\": {\"finished_at\": \"2026-05-20T04:55:18.779Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T04:55:23.587676+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.9933}, \"completed_at\": \"2026-05-20T04:58:10.410Z\"}, \"codellama13b_no_trace_seed42\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-16T07:47:20.182Z\", \"updated_at\": \"2026-05-20T03:09:12.228Z\", \"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition no_trace --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_no_trace_seed42 --wandb_project trace-verdict-study --wandb_run_name codellama13b_no_trace_seed42 && python eval/evaluate.py --condition no_trace --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_no_trace_seed42/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_no_trace_seed42/final/eval_results.json --save_predictions\\\"\", \"wandb_run_id\": \"codellama13b_no_trace_seed42\", \"code_commit\": \"e404237ccc765768e267d4d6fd3c89549dcf41a4\", \"finished_at\": \"2026-05-16T14:19:42.177Z\"}, \"gpu_ids\": [\"cuda:1\"], \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T14:19:44.574583+00:00\"}], \"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.765, \"n\": 1190, \"majority_baseline\": 0.7151, \"lift\": 0.05, \"pass_precision\": 0.84, \"pass_recall\": 0.83, \"pass_f1\": 0.84, \"fail_precision\": 0.59, \"fail_recall\": 0.59, \"fail_f1\": 0.59, \"accuracy_ci\": [0.738, 0.787]}}}, \"completed_at\": \"2026-05-16T14:22:58.643Z\", \"hypothesis\": \"CodeLlama-13B no-trace baseline: without execution trace, larger model capacity does not compensate for missing diagnostic signal — accuracy near majority baseline as on smaller models\", \"parent\": \"no_trace_seed42_v5\", \"spec\": {\"command\": \"previously completed\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/no_trace_train.jsonl\", \"data_count\": 4720, \"model_name\": \"codellama/CodeLlama-13b-Instruct-hf\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_no_trace_seed42/final\", \"log_path\": \"~/runs/trace-verdict-study/codellama13b_no_trace_seed42.log\", \"checkpoint_source\": \"self-trained\", \"eval_data\": \"/root/autodl-tmp/trace-verdict-study-data/no_trace_test.jsonl\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.765, \"n\": 1190, \"majority_baseline\": 0.7151, \"lift\": 0.05, \"pass_precision\": 0.84, \"pass_recall\": 0.83, \"pass_f1\": 0.84, \"fail_precision\": 0.59, \"fail_recall\": 0.59, \"fail_f1\": 0.59, \"accuracy_ci_lower\": 0.738, \"accuracy_ci_upper\": 0.787}}, \"codellama13b_loop_only_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T23:10:32.075Z\", \"updated_at\": \"2026-05-20T03:04:16.177Z\", \"hypothesis\": \"CodeLlama-13B loop_only seed123 应在 74-80% 范围（与 seed42=77.06% 接近），验证 Tier 2 collapse（≈no_trace）是否 seed-robust，CodeLlama 是唯一 Tier 2 failed 的模型\", \"parent\": \"codellama13b_loop_only_seed42\", \"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"spec\": {\"command\": \"bash -c \\\"...codellama13b_loop_only_seed123...\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"543506\", \"log_path\": \"~/runs/trace-verdict-study/codellama13b_loop_only_seed123.log\", \"submitted_at\": \"2026-05-19T23:10:51.377Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/loop_only_train.jsonl\", \"data_count\": 4720, \"model_name\": \"codellama/CodeLlama-13b-Instruct-hf\", \"seed\": 123, \"checkpoint_source\": \"self-trained\", \"eval_data\": \"/root/autodl-tmp/trace-verdict-study-data/loop_only_test.jsonl\", \"wall_clock_seconds\": 14004.8, \"gpu_hours\": 3.89}, \"reproduce\": {\"finished_at\": \"2026-05-20T03:02:44.274Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T03:02:51.934438+00:00\"}]}, \"metrics\": {\"accuracy\": 0.7605, \"accuracy_ci_lower\": 0.7387, \"accuracy_ci_upper\": 0.7857, \"pass_precision\": 0.9478, \"pass_recall\": 0.7039, \"pass_f1\": 0.8078, \"fail_precision\": 0.5484, \"fail_recall\": 0.9027, \"fail_f1\": 0.6823, \"majority_baseline\": 0.7151, \"lift\": 0.0454, \"n\": 1190}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_loop_only_seed123/final\", \"completed_at\": \"2026-05-20T03:04:16.177Z\"}, \"deepseek_vota_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T00:13:27.141Z\", \"updated_at\": \"2026-05-20T02:38:03.290Z\", \"hypothesis\": \"DeepSeek VOTA seed123 accuracy ∈ [82%, 88%]，验证 seed42=84.45% 的稳定性，补充 VOTA 跨 seed robustness 证据（rebuttal 储备）\", \"parent\": \"deepseek_vota_seed42\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition vota --model_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_vota_seed123 --gradient_checkpointing --gpu 0 --seed 123 --wandb_project trace-verdict-study --wandb_run_name deepseek_vota_seed123 && python eval/evaluate.py --condition vota --model_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_vota_seed123/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_vota_seed123/final/eval_results.json --save_predictions --max_length 2048\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"pid\": \"553506\", \"log_path\": \"~/runs/trace-verdict-study/deepseek_vota_seed123.log\", \"submitted_at\": \"2026-05-20T00:13:45.484Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/vota_train.jsonl\", \"data_count\": 4720, \"model_name\": \"deepseek-ai/deepseek-coder-6.7b-instruct\", \"seed\": 123, \"checkpoint_source\": \"self-trained\", \"eval_data\": \"/root/autodl-tmp/trace-verdict-study-data/vota_test.jsonl\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_vota_seed123/final\", \"wall_clock_seconds\": 8533.1, \"gpu_hours\": 2.37}, \"reproduce\": {\"finished_at\": \"2026-05-20T02:33:53.965Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T02:33:58.617133+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.9916, \"accuracy_ci_lower\": 0.9857, \"accuracy_ci_upper\": 0.9966, \"fail_recall\": 0.973, \"pass_recall\": 0.999, \"train_loss\": 0.0625, \"eval_loss\": 0.11}, \"completed_at\": \"2026-05-20T02:35:58.540Z\"}, \"deepseek_loop_only_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T21:38:49.036Z\", \"updated_at\": \"2026-05-20T00:14:38.720Z\", \"hypothesis\": \"DeepSeek-6.7B loop_only seed123 应在 78-84% 范围（与 seed42=81.26% 接近），验证 Tier 2 跨 seed 稳定性，补充 reviewer single-seed concern\", \"parent\": \"deepseek_loop_only_seed42\", \"server\": \"westd-11235\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition loop_only --model_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct --gradient_checkpointing --gpu 0 --seed 123 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_loop_only_seed123 --wandb_project trace-verdict-study --wandb_run_name deepseek_loop_only_seed123 && python eval/evaluate.py --condition loop_only --model_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_loop_only_seed123/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_loop_only_seed123/final/eval_results.json --save_predictions --max_length 2048\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"pid\": \"538294\", \"log_path\": \"~/runs/trace-verdict-study/deepseek_loop_only_seed123.log\", \"submitted_at\": \"2026-05-19T21:39:34.717Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/loop_only_train.jsonl\", \"data_count\": 4720, \"model_name\": \"deepseek-ai/deepseek-coder-6.7b-instruct\", \"seed\": 123, \"checkpoint_source\": \"self-trained\", \"eval_data\": \"/root/autodl-tmp/trace-verdict-study-data/loop_only_test.jsonl\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_loop_only_seed123/final\", \"wall_clock_seconds\": 9221.4, \"gpu_hours\": 2.56}, \"reproduce\": {\"finished_at\": \"2026-05-20T00:10:53.831Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T00:10:57.808157+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.8126, \"accuracy_ci_lower\": 0.792, \"accuracy_ci_upper\": 0.834, \"pass_recall\": 0.856, \"fail_recall\": 0.705}, \"completed_at\": \"2026-05-20T00:13:16.133Z\"}, \"deepseek_ae_only_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T20:36:36.821Z\", \"updated_at\": \"2026-05-19T23:10:38.180Z\", \"hypothesis\": \"DeepSeek-6.7B ae_only 应达 ≥95% accuracy，与 Qwen-7B (99.92%) / CodeLlama-13B (99.08%) 一致，验证 Tier 1 (ae_only) 跨 3 模型 universal\", \"parent\": \"deepseek_exception_only_seed42\", \"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition ae_only --model_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_ae_only_seed42 --wandb_project trace-verdict-study --wandb_run_name deepseek_ae_only_seed42 && python eval/evaluate.py --condition ae_only --model_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_ae_only_seed42/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_ae_only_seed42/final/eval_results.json --save_predictions --max_length 2048\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"534976\", \"log_path\": \"~/runs/trace-verdict-study/deepseek_ae_only_seed42.log\", \"submitted_at\": \"2026-05-19T20:36:58.511Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/ae_only_train.jsonl\", \"data_count\": 4720, \"model_name\": \"deepseek-ai/deepseek-coder-6.7b-instruct\", \"seed\": 42, \"checkpoint_source\": \"self-trained\", \"eval_data\": \"/root/autodl-tmp/trace-verdict-study-data/ae_only_test.jsonl\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_ae_only_seed42/final\", \"wall_clock_seconds\": 9219.7, \"gpu_hours\": 2.56}, \"reproduce\": {\"finished_at\": \"2026-05-19T23:08:32.917Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T23:08:37.293936+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.9874, \"accuracy_ci_lower\": 0.9807, \"accuracy_ci_upper\": 0.9933, \"fail_recall\": 0.959, \"pass_recall\": 0.999, \"fail_f1\": 0.977, \"pass_f1\": 0.991}, \"completed_at\": \"2026-05-19T23:10:38.180Z\"}, \"cross_model_calibration_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T21:40:43.958Z\", \"updated_at\": \"2026-05-19T21:41:10.724Z\", \"hypothesis\": \"4 模型 × exception_only 的 ECE/Brier 应一致性低（ECE < 0.01），验证 calibration quality 跨模型 universal\", \"conclusion\": \"success\", \"metrics\": {\"qwen_7b\": {\"ece\": 0.0027, \"mce\": 0.8355, \"brier\": 0.0013, \"accuracy\": 0.9983}, \"qwen_1_5b\": {\"ece\": 0.002, \"mce\": 0.7549, \"brier\": 0.0013, \"accuracy\": 0.9983}, \"codellama_13b\": {\"ece\": 0.002, \"mce\": 0.0411, \"brier\": 0.0013, \"accuracy\": 0.9983}, \"deepseek_6_7b\": {\"ece\": 0.0064, \"mce\": 0.7756, \"brier\": 0.0061, \"accuracy\": 0.9933}}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/cross_model_calibration_results.json\", \"log_path\": \"N/A - eval only\", \"server\": \"westd-11235\", \"data_path\": \"existing exception_only checkpoints x4\", \"data_count\": 1190, \"model_name\": \"4 models x exception_only\", \"seed\": 42}, \"completed_at\": \"2026-05-19T21:41:10.724Z\"}, \"codellama13b_vota_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:47:21.632Z\", \"updated_at\": \"2026-05-19T21:37:28.024Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition vota --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_vota_seed42 --wandb_project trace-verdict-study --wandb_run_name codellama13b_vota_seed42 && python eval/evaluate.py --condition vota --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_vota_seed42/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_vota_seed42/final/eval_results.json --save_predictions\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"279473\", \"log_path\": \"~/runs/trace-verdict-study/codellama13b_vota_seed42.log\", \"submitted_at\": \"2026-05-16T14:23:09.712Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 14537.8, \"gpu_hours\": 4.04}, \"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"pid\": \"279473\", \"log_path\": \"~/runs/trace-verdict-study/codellama13b_vota_seed42.log\", \"wandb_run_id\": \"codellama13b_vota_seed42\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition vota --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_vota_seed42 --wandb_project trace-verdict-study --wandb_run_name codellama13b_vota_seed42 && python eval/evaluate.py --condition vota --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_vota_seed42/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_vota_seed42/final/eval_results.json --save_predictions\\\"\", \"wandb_run_id\": \"codellama13b_vota_seed42\", \"code_commit\": \"e404237ccc765768e267d4d6fd3c89549dcf41a4\", \"finished_at\": \"2026-05-16T18:21:13.833Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T18:21:16.129637+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.9857, \"accuracy_ci_lower\": 0.979, \"accuracy_ci_upper\": 0.9916, \"pass_f1\": 0.99, \"fail_f1\": 0.9748, \"n_test\": 1190}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_vota_seed42/final\", \"completed_at\": \"2026-05-16T18:25:27.552Z\", \"hypothesis\": \"CodeLlama-13B VOTA accuracy 应在 85-92%，与 Qwen-7B VOTA (~99%) 对比，验证 VOTA 压缩方法跨模型有效性（rebuttal 储备：reviewer 追问 VOTA cross-model generalization）\", \"parent\": \"vota_seed42_v5\"}, \"deepseek_label_only_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T17:52:51.095Z\", \"updated_at\": \"2026-05-19T21:34:38.836Z\", \"hypothesis\": \"DeepSeek-6.7B full_trace + label_only_loss 应显著高于标准 full_trace (79.16%)，预期 82-88%，跨模型验证 gradient dilution 是 full_trace collapse 的主因（26%/74% 分解），回应 Claim 2 跨模型泛化\", \"parent\": \"deepseek_full_trace_seed42_v3\", \"server\": \"westd-11235\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition full_trace --model_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct --gradient_checkpointing --label_only_loss --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_label_only_seed42 --wandb_project trace-verdict-study --wandb_run_name deepseek_label_only_seed42 && python eval/evaluate.py --condition full_trace --model_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_label_only_seed42/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_label_only_seed42/final/eval_results.json --save_predictions\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"pid\": \"530290\", \"log_path\": \"~/runs/trace-verdict-study/deepseek_label_only_seed42.log\", \"submitted_at\": \"2026-05-19T18:53:38.289Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/full_trace_train.jsonl\", \"data_count\": 4720, \"model_name\": \"deepseek-ai/deepseek-coder-6.7b-instruct\", \"seed\": 42, \"checkpoint_source\": \"self-trained\", \"eval_data\": \"/root/autodl-tmp/trace-verdict-study-data/full_trace_test.jsonl\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_label_only_seed42/final\", \"wall_clock_seconds\": 9660.5, \"gpu_hours\": 2.68}, \"reproduce\": {\"finished_at\": \"2026-05-19T21:14:38.257Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T21:14:42.796371+00:00\"}]}, \"conclusion\": \"negative\", \"metrics\": {\"accuracy\": 0.285, \"accuracy_ci_lower\": 0.261, \"accuracy_ci_upper\": 0.308, \"majority_baseline\": 0.7151, \"lift\": -0.43, \"pass_precision\": 0, \"pass_recall\": 0, \"pass_f1\": 0, \"fail_precision\": 0.28, \"fail_recall\": 1, \"fail_f1\": 0.44, \"train_loss\": 1.7839, \"eval_loss\": \"nan\"}, \"completed_at\": \"2026-05-19T21:34:38.836Z\"}, \"deepseek_loop_only_seed42\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-19T17:29:34.281Z\", \"updated_at\": \"2026-05-19T20:39:32.182Z\", \"hypothesis\": \"DeepSeek-6.7B loop_only 应显著低于 exception_only (99.33%)，预期 80-90%，验证 Tier hierarchy (Tier1 >> Tier2) 在第 3 个模型架构上成立，强化 MF2 跨模型证据\", \"parent\": \"deepseek_exception_only_seed42\", \"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"failure_reason\": \"\", \"completed_at\": \"2026-05-19T17:39:08.696Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\"}, \"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T20:27:03.192709+00:00\"}]}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition loop_only --model_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_loop_only_seed42 --wandb_project trace-verdict-study --wandb_run_name deepseek_loop_only_seed42 && python eval/evaluate.py --condition loop_only --model_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_loop_only_seed42/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_loop_only_seed42/final/eval_results.json --save_predictions\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"525732\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/\", \"data_count\": 4720, \"model_name\": \"deepseek-ai/deepseek-coder-6.7b-instruct\", \"seed\": 42, \"checkpoint_source\": \"self-trained\", \"eval_data\": \"/root/autodl-tmp/trace-verdict-study-data/loop_only_test.jsonl\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T20:26:57.867Z\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.8126, \"accuracy_ci_lower\": 0.7908, \"accuracy_ci_upper\": 0.8345, \"fail_recall\": 0.6372, \"pass_recall\": 0.8825}}, \"codellama13b_loop_only_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T14:59:26.886Z\", \"updated_at\": \"2026-05-19T18:55:37.408Z\", \"hypothesis\": \"CodeLlama-13B loop_only 应显著低于 ae_only（预期差距≥10pp），验证 Tier hierarchy（ae_only > loop_only）在非 Qwen 架构上成立，回应 Round 9 MF2 跨模型验证要求\", \"parent\": \"vota_loop_only_seed42\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition loop_only --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_loop_only_seed42 --wandb_project trace-verdict-study --wandb_run_name codellama13b_loop_only_seed42 && python eval/evaluate.py --condition loop_only --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_loop_only_seed42/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_loop_only_seed42/final/eval_results.json --save_predictions\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"pid\": \"517765\", \"log_path\": \"~/runs/trace-verdict-study/codellama13b_loop_only_seed42.log\", \"submitted_at\": \"2026-05-19T15:00:28.260Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 14090.4, \"gpu_hours\": 3.91}, \"server\": \"westd-11235\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"pid\": \"517765\", \"log_path\": \"~/runs/trace-verdict-study/codellama13b_loop_only_seed42.log\", \"wandb_run_id\": \"codellama13b_loop_only_seed42\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition loop_only --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_loop_only_seed42 --wandb_project trace-verdict-study --wandb_run_name codellama13b_loop_only_seed42 && python eval/evaluate.py --condition loop_only --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_loop_only_seed42/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_loop_only_seed42/final/eval_results.json --save_predictions\\\"\", \"wandb_run_id\": \"codellama13b_loop_only_seed42\", \"code_commit\": \"e404237ccc765768e267d4d6fd3c89549dcf41a4\", \"finished_at\": \"2026-05-19T18:51:05.347Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T18:51:09.241877+00:00\"}]}, \"metrics\": {\"accuracy\": 0.7706, \"accuracy_ci_lower\": 0.7487, \"accuracy_ci_upper\": 0.7941, \"n\": 1190, \"majority_baseline\": 0.7151, \"lift\": 0.0555, \"fail_recall\": 0.826, \"pass_recall\": 0.7485, \"pass_precision\": 0.92, \"fail_precision\": 0.57, \"pass_f1\": 0.82, \"fail_f1\": 0.67}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_loop_only_seed42/final\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-19T18:55:18.642Z\"}, \"qwen7b_full_trace_tail512_seed42\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-18T15:37:57.803Z\", \"updated_at\": \"2026-05-19T14:26:10.097Z\", \"hypothesis\": \"Qwen-7B tail-512 (硬截断 full_trace_tail_512) 应与原 full_trace_tail seed42 结果 (~93.6%) 接近，确认 condition 差异不影响 budget curve 结论；同时为 cross-seed 提供可比 baseline\", \"parent\": \"full_trace_tail_seed42\", \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-19T13:09:55.237Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\"}, \"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T14:26:11.468840+00:00\"}]}, \"spec\": {\"server\": \"westd-11235\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/trace-verdict-study && /root/miniconda3/bin/python train/train_sft.py --condition full_trace_tail_512 --model_path /root/trace-verdict-study/models/Qwen2.5-Coder-7B-Instruct --seed 42 --gradient_checkpointing --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen7b_full_trace_tail512_seed42/ --wandb_project trace-verdict-study --wandb_run_name qwen7b_full_trace_tail512_seed42 && /root/miniconda3/bin/python eval/evaluate.py --condition full_trace_tail_512 --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen7b_full_trace_tail512_seed42/final --model_path /root/trace-verdict-study/models/Qwen2.5-Coder-7B-Instruct --save_predictions\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/\", \"data_count\": 4720, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen7b_full_trace_tail512_seed42/final\", \"eval_data\": \"/root/autodl-tmp/trace-verdict-study-data/\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T14:26:06.191Z\"}, \"conclusion\": \"failed\"}, \"qwen1.5b_full_trace_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:27:39.587Z\", \"updated_at\": \"2026-05-19T12:52:36.469Z\", \"spec\": {\"hypothesis\": \"Multi-scale validation: full_trace on Qwen-2.5-Coder-1.5B.\", \"model_name\": \"Qwen2.5-Coder-1.5B-Instruct\", \"seed\": 42, \"condition\": \"full_trace\"}, \"conclusion\": \"killed\", \"failure_reason\": \"replaced by qwen15b_* entries (dot in exp_id incompatible with submit_on_allocated)\", \"hypothesis\": \"Qwen-1.5B full_trace 应达 ≥96% accuracy，确认 1.5B 小模型在 full trace 条件下与 7B 可比（trace quality 主导而非 model capacity）\", \"notes\": \"重复条目，已在 qwen15b_full_trace_seed42 (77.06%) 完成。命名差异：qwen1.5b_ → qwen15b_\"}, \"codellama_no_trace_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:27:42.805Z\", \"updated_at\": \"2026-05-19T12:52:35.073Z\", \"spec\": {\"hypothesis\": \"Multi-family baseline: no_trace on CodeLlama-7B-Instruct.\", \"model_name\": \"CodeLlama-13b-Instruct-hf\", \"seed\": 42, \"condition\": \"no_trace\"}, \"conclusion\": \"killed\", \"failure_reason\": \"user approved 13B not 7B\", \"hypothesis\": \"CodeLlama-13B no_trace 应在 70-78% (≈majority baseline)，确认无 trace 时 13B scale 无法补偿信息缺失\", \"notes\": \"重复条目，已在 codellama13b_no_trace_seed42 (76.5%) 完成。命名差异：codellama_ → codellama13b_\"}, \"qwen1.5b_vota_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:27:38.134Z\", \"updated_at\": \"2026-05-19T12:52:04.641Z\", \"spec\": {\"hypothesis\": \"Multi-scale validation: VOTA on Qwen-2.5-Coder-1.5B.\", \"model_name\": \"Qwen2.5-Coder-1.5B-Instruct\", \"seed\": 42, \"condition\": \"vota\"}, \"conclusion\": \"killed\", \"failure_reason\": \"replaced by qwen15b_* entries (dot in exp_id incompatible with submit_on_allocated)\", \"hypothesis\": \"Qwen-1.5B VOTA 应在 82-90% accuracy，可能略低于 7B 因 VOTA 条件下 scale-sensitivity 更明显\", \"notes\": \"重复条目，已在 qwen15b_vota_seed42 (99.58%) 完成。命名差异：qwen1.5b_ → qwen15b_\"}, \"codellama_vota_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:27:43.769Z\", \"updated_at\": \"2026-05-19T12:52:03.704Z\", \"spec\": {\"hypothesis\": \"Multi-family validation: VOTA on CodeLlama-7B-Instruct.\", \"model_name\": \"CodeLlama-13b-Instruct-hf\", \"seed\": 42, \"condition\": \"vota\"}, \"conclusion\": \"killed\", \"failure_reason\": \"user approved 13B not 7B\", \"hypothesis\": \"CodeLlama-13B VOTA 应在 85-92% accuracy，与 Qwen-7B/DeepSeek VOTA 对齐，作 rebuttal 储备验证 ablation condition 跨 scale 一致性\", \"notes\": \"重复条目，已在 codellama13b_vota_seed42 (98.57%) 完成。命名差异：codellama_ → codellama13b_\"}, \"qwen1.5b_exception_only_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:27:34.741Z\", \"updated_at\": \"2026-05-19T12:51:38.800Z\", \"spec\": {\"hypothesis\": \"Multi-scale validation: exception_only on Qwen-2.5-Coder-1.5B. Tests if exception dominance holds at smaller scale.\", \"model_name\": \"Qwen2.5-Coder-1.5B-Instruct\", \"seed\": 42, \"condition\": \"exception_only\", \"server\": \"westd-11235\", \"gpu\": \"cuda:0\", \"account\": \"root\"}, \"conclusion\": \"killed\", \"failure_reason\": \"replaced by qwen15b_* entries (dot in exp_id incompatible with submit_on_allocated)\", \"hypothesis\": \"Qwen-1.5B exception_only 应达 ≥99% accuracy，确认 minimal sufficient signal 在 1.5B scale 有效，signal quality 主导 model capacity\", \"notes\": \"重复条目，已在 qwen15b_exception_only_seed42 (99.83%) 完成。命名差异：qwen1.5b_ → qwen15b_\"}, \"qwen7b_full_trace_label_only_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:39:47.245Z\", \"updated_at\": \"2026-05-19T11:39:34.147Z\", \"hypothesis\": \"Qwen-7B full_trace (label_only_loss) seed456 应在 95-98% 范围（与 seed42 一致），为 N5 reviewer concern 提供 full_trace 条件的方差估计\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/trace-verdict-study && /root/miniconda3/bin/python train/train_sft.py --condition full_trace --model_path /root/trace-verdict-study/models/Qwen2.5-Coder-7B-Instruct --seed 456 --gradient_checkpointing --label_only_loss --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen7b_full_trace_label_only_seed456/ --wandb_project trace-verdict-study --wandb_run_name qwen7b_full_trace_label_only_seed456 && /root/miniconda3/bin/python eval/evaluate.py --condition full_trace --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen7b_full_trace_label_only_seed456/final --model_path /root/trace-verdict-study/models/Qwen2.5-Coder-7B-Instruct --save_predictions\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"501315\", \"log_path\": \"~/runs/trace-verdict-study/qwen7b_full_trace_label_only_seed456.log\", \"submitted_at\": \"2026-05-19T09:05:27.608Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/trace-verdict-study/data/\", \"data_count\": 1190, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 456, \"wall_clock_seconds\": 9246.5, \"gpu_hours\": 2.57}, \"reproduce\": {\"finished_at\": \"2026-05-19T11:36:54.329Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T11:36:58.222319+00:00\"}]}, \"metrics\": {\"accuracy\": 0.847, \"accuracy_ci_lower\": 0.827, \"accuracy_ci_upper\": 0.866, \"pass_f1\": 0.9, \"fail_f1\": 0.71, \"pass_precision\": 0.87, \"pass_recall\": 0.92, \"fail_precision\": 0.76, \"fail_recall\": 0.67, \"majority_baseline\": 0.7151, \"lift\": 0.1319, \"train_loss\": 0.2452, \"eval_loss\": 0.3366}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen7b_full_trace_label_only_seed456/final\", \"log_path\": \"~/runs/trace-verdict-study/qwen7b_full_trace_label_only_seed456.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T11:39:34.147Z\"}, \"qwen7b_full_trace_label_only_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:39:45.764Z\", \"updated_at\": \"2026-05-19T11:23:36.307Z\", \"hypothesis\": \"Qwen-7B full_trace (label_only_loss) seed123 应在 95-98% 范围（与 seed42 一致），为 N5 reviewer concern 提供 full_trace 条件的方差估计\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/trace-verdict-study && /root/miniconda3/bin/python train/train_sft.py --condition full_trace --model_path /root/trace-verdict-study/models/Qwen2.5-Coder-7B-Instruct --seed 123 --gradient_checkpointing --label_only_loss --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen7b_full_trace_label_only_seed123/ --wandb_project trace-verdict-study --wandb_run_name qwen7b_full_trace_label_only_seed123 && /root/miniconda3/bin/python eval/evaluate.py --condition full_trace --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen7b_full_trace_label_only_seed123/final --model_path /root/trace-verdict-study/models/Qwen2.5-Coder-7B-Instruct --save_predictions\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"pid\": \"499561\", \"log_path\": \"~/runs/trace-verdict-study/qwen7b_full_trace_label_only_seed123.log\", \"submitted_at\": \"2026-05-19T08:38:38.356Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/trace-verdict-study/data/\", \"data_count\": 1190, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 123, \"wall_clock_seconds\": 9898.0, \"gpu_hours\": 2.75}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.8689, \"accuracy_ci_lower\": 0.8496, \"accuracy_ci_upper\": 0.8874, \"pass_f1\": 0.9121, \"fail_f1\": 0.7426, \"pass_precision\": 0.8765, \"pass_recall\": 0.9506, \"fail_precision\": 0.8427, \"fail_recall\": 0.6637, \"majority_baseline\": 0.7151, \"lift\": 0.1538, \"train_loss\": 0.2425, \"eval_loss\": 0.2787}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen7b_full_trace_label_only_seed123/final\", \"log_path\": \"~/runs/trace-verdict-study/qwen7b_full_trace_label_only_seed123.log\", \"completed_at\": \"2026-05-19T11:23:36.307Z\"}, \"qwen7b_vota_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:39:43.207Z\", \"updated_at\": \"2026-05-19T09:06:16.721Z\", \"hypothesis\": \"Qwen-7B VOTA seed456 应在 84-92% 范围（与 vota_seed42_v4 一致），为 N5 reviewer concern 提供 VOTA 条件的方差估计\", \"spec\": {\"data_path\": \"/root/trace-verdict-study/data/\", \"data_count\": 1190, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 456, \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/trace-verdict-study && /root/miniconda3/bin/python train/train_sft.py --condition vota --model_path /root/trace-verdict-study/models/Qwen2.5-Coder-7B-Instruct --seed 456 --gradient_checkpointing --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen7b_vota_seed456/ --wandb_project trace-verdict-study --wandb_run_name qwen7b_vota_seed456 && /root/miniconda3/bin/python eval/evaluate.py --condition vota --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen7b_vota_seed456/final --model_path /root/trace-verdict-study/models/Qwen2.5-Coder-7B-Instruct --save_predictions\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"account\": \"root\", \"pid\": \"494086\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T09:02:56.001Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T09:03:00.101888+00:00\"}]}, \"metrics\": {\"accuracy\": 0.9908, \"accuracy_ci_lower\": 0.9849, \"accuracy_ci_upper\": 0.9958, \"majority_baseline\": 0.7151, \"lift\": 0.2756, \"n\": 1190, \"pass_precision\": 1, \"pass_recall\": 0.9871, \"pass_f1\": 0.9935, \"fail_precision\": 0.9686, \"fail_recall\": 1, \"fail_f1\": 0.984, \"train_loss\": 0.04969, \"eval_loss\": 0.08312}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen7b_vota_seed456/final\", \"log_path\": \"~/runs/trace-verdict-study/qwen7b_vota_seed456.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T09:06:16.721Z\"}, \"qwen7b_vota_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:39:41.038Z\", \"updated_at\": \"2026-05-19T08:37:58.799Z\", \"hypothesis\": \"Qwen-7B VOTA seed123 应在 84-92% 范围（与 vota_seed42_v4 一致），为 N5 reviewer concern 提供 VOTA 条件的方差估计\", \"spec\": {\"data_path\": \"/root/trace-verdict-study/data/\", \"data_count\": 1190, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 123, \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"account\": \"root\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/trace-verdict-study && /root/miniconda3/bin/python train/train_sft.py --condition vota --model_path /root/trace-verdict-study/models/Qwen2.5-Coder-7B-Instruct --seed 123 --gradient_checkpointing --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen7b_vota_seed123/ --wandb_project trace-verdict-study --wandb_run_name qwen7b_vota_seed123 && /root/miniconda3/bin/python eval/evaluate.py --condition vota --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen7b_vota_seed123/final --model_path /root/trace-verdict-study/models/Qwen2.5-Coder-7B-Instruct --save_predictions\\\"\", \"pid\": \"492009\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T08:27:29.961Z\"}, \"failure_reason\": \"N/A - EXIT_CODE=129 was SIGHUP after training+eval had already completed successfully\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T08:27:32.267Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T08:27:35.533591+00:00\"}]}, \"metrics\": {\"accuracy\": 0.9866, \"accuracy_ci_lower\": 0.979, \"accuracy_ci_upper\": 0.9925, \"majority_baseline\": 0.7151, \"lift\": 0.2714, \"n\": 1190, \"pass_precision\": 1, \"pass_recall\": 0.9812, \"pass_f1\": 0.9905, \"fail_precision\": 0.9549, \"fail_recall\": 1, \"fail_f1\": 0.9769, \"train_loss\": 0.0499, \"eval_loss\": 0.0864}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen7b_vota_seed123/final\", \"log_path\": \"~/runs/trace-verdict-study/qwen7b_vota_seed123.log\"}, \"qwen7b_full_trace_dynamics_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T03:21:30.436Z\", \"updated_at\": \"2026-05-19T07:03:18.865Z\", \"hypothesis\": \"full_trace (label_only_loss) 收敛速度应慢于 exception_only，因 trace 中冗余信息稀释了有效 signal density。通过每 50 steps eval 记录 learning curve 验证。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/trace-verdict-study && /root/miniconda3/bin/python train/train_sft.py --condition full_trace --model_path /root/trace-verdict-study/models/Qwen2.5-Coder-7B-Instruct --seed 42 --gradient_checkpointing --label_only_loss --save_steps 50 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen7b_full_trace_dynamics_seed42/ --wandb_project trace-verdict-study --wandb_run_name qwen7b_full_trace_dynamics_seed42 && echo '=== Training done, starting batch eval ===' && /root/miniconda3/bin/python eval/batch_eval_dynamics.py --checkpoint_root /root/autodl-tmp/trace-verdict-study-checkpoints/qwen7b_full_trace_dynamics_seed42/ --condition full_trace && echo '=== Batch eval done, cleaning checkpoints ===' && find /root/autodl-tmp/trace-verdict-study-checkpoints/qwen7b_full_trace_dynamics_seed42/ -maxdepth 1 -name 'checkpoint-*' -type d -exec rm -rf {} + && echo '=== All done ==='\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"485337\", \"log_path\": \"~/runs/trace-verdict-study/qwen7b_full_trace_dynamics_seed42.log\", \"submitted_at\": \"2026-05-19T03:27:23.137Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/trace-verdict-study/data/\", \"data_count\": 1190, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 42, \"wall_clock_seconds\": 12955.7, \"gpu_hours\": 3.6}, \"reproduce\": {\"finished_at\": \"2026-05-19T06:38:01.305Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T06:38:05.031265+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"step50_acc\": 0.8739, \"step100_acc\": 0.821, \"step150_acc\": 0.8571, \"step200_acc\": 0.8655, \"step250_acc\": 0.8739, \"step300_acc\": 0.8487, \"step350_acc\": 0.8882, \"step400_acc\": 0.8571, \"step444_acc\": 0.8824, \"best_step\": 350, \"best_acc\": 0.8882, \"final_loss\": 0.0085}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen7b_full_trace_dynamics_seed42/final\", \"completed_at\": \"2026-05-19T07:03:18.865Z\"}, \"qwen15b_exception_only_seed123_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T21:41:35.811Z\", \"updated_at\": \"2026-05-19T06:40:43.424Z\", \"hypothesis\": \"Qwen-1.5B exception_only seed123 应达 ~99.83%（与 seed42 一致），为 W3 reviewer concern 提供 1.5B scale 的方差估计。v1 因 GPU 并发 OOM 失败，重试。\", \"parent\": \"qwen15b_exception_only_seed123\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/trace-verdict-study && /root/miniconda3/bin/python train/train_sft.py --condition exception_only --model_path /root/trace-verdict-study/models/Qwen2.5-Coder-1.5B-Instruct --seed 123 --gradient_checkpointing --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_exception_only_seed123_v2/ --wandb_project trace-verdict-study --wandb_run_name qwen15b_exception_only_seed123_v2 && /root/miniconda3/bin/python eval/evaluate.py --condition exception_only --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_exception_only_seed123_v2/final --model_path /root/trace-verdict-study/models/Qwen2.5-Coder-1.5B-Instruct --save_predictions\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"pid\": \"473720\", \"log_path\": \"~/runs/trace-verdict-study/qwen15b_exception_only_seed123_v2.log\", \"submitted_at\": \"2026-05-18T23:09:41.499Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 27061.9, \"gpu_hours\": 7.52}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.9983, \"accuracy_ci_lower\": 0.9958, \"accuracy_ci_upper\": 1, \"seed_comparison\": {\"seed42_accuracy\": 0.9983, \"seed456_accuracy\": 0.9983, \"seed123_accuracy\": 0.9983}}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_exception_only_seed123_v2/final\", \"log_path\": \"~/runs/trace-verdict-study/qwen15b_exception_only_seed123_v2.log\", \"completed_at\": \"2026-05-19T06:40:43.424Z\"}, \"qwen7b_exception_only_dynamics_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T03:21:29.197Z\", \"updated_at\": \"2026-05-19T06:00:52.469Z\", \"hypothesis\": \"exception_only 因 information density 更高，收敛速度应显著快于 full_trace（即使 full_trace 用 label_only_loss）。通过每 50 steps eval 记录 learning curve 验证。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/trace-verdict-study && /root/miniconda3/bin/python train/train_sft.py --condition exception_only --model_path /root/trace-verdict-study/models/Qwen2.5-Coder-7B-Instruct --seed 42 --gradient_checkpointing --save_steps 50 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen7b_exception_only_dynamics_seed42/ --wandb_project trace-verdict-study --wandb_run_name qwen7b_exception_only_dynamics_seed42 && echo '=== Training done, starting batch eval ===' && /root/miniconda3/bin/python eval/batch_eval_dynamics.py --checkpoint_root /root/autodl-tmp/trace-verdict-study-checkpoints/qwen7b_exception_only_dynamics_seed42/ --condition exception_only && echo '=== Batch eval done, cleaning checkpoints ===' && find /root/autodl-tmp/trace-verdict-study-checkpoints/qwen7b_exception_only_dynamics_seed42/ -maxdepth 1 -name 'checkpoint-*' -type d -exec rm -rf {} + && echo '=== All done ==='\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"pid\": \"485193\", \"log_path\": \"~/runs/trace-verdict-study/qwen7b_exception_only_dynamics_seed42.log\", \"submitted_at\": \"2026-05-19T03:27:19.569Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/trace-verdict-study/data/\", \"data_count\": 1190, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 42, \"wall_clock_seconds\": 9212.9, \"gpu_hours\": 2.56}, \"conclusion\": \"success\", \"metrics\": {\"step50_acc\": 0.9933, \"step100_acc\": 0.9933, \"step150_acc\": 0.9933, \"step200_acc\": 0.9983, \"step250_acc\": 0.9983, \"step300_acc\": 0.9983, \"step350_acc\": 0.9983, \"step400_acc\": 0.9983, \"step444_acc\": 0.9983, \"saturation_step\": 200, \"final_loss\": 0.0329, \"pass_f1\": 0.9988, \"fail_f1\": 0.9971}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen7b_exception_only_dynamics_seed42/final\", \"log_path\": \"~/runs/trace-verdict-study/qwen7b_exception_only_dynamics_seed42.log\", \"completed_at\": \"2026-05-19T06:00:52.469Z\"}, \"codellama13b_full_trace_tail512_seed42\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-17T23:20:23.098Z\", \"updated_at\": \"2026-05-19T02:30:30.373Z\", \"hypothesis\": \"CodeLlama-13B tail-512 应在 93-96% 范围，与其他 3 模型 tail-512 收敛带一致，确认 phase transition 阈值跨 4 模型 universal\", \"parent\": \"codellama13b_exception_only_seed42\", \"reproduce\": {\"finished_at\": \"2026-05-18T01:13:45.920Z\"}, \"extra\": {\"seed_comparison\": {\"seed42\": 0.9824, \"seed123\": 0.9824, \"seed456\": 0.9824}}, \"completed_at\": \"2026-05-18T01:35:11.577Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/trace-verdict-study && /root/miniconda3/bin/python train/train_sft.py --condition full_trace_tail_512 --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf/ --seed 42 --gradient_checkpointing --label_only_loss --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_full_trace_tail512_seed42/ --wandb_project trace-verdict-study --wandb_run_name codellama13b_full_trace_tail512_seed42 && /root/miniconda3/bin/python eval/evaluate.py --condition full_trace_tail_512 --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_full_trace_tail512_seed42/final --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf/ --save_predictions\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"pid\": \"476956\", \"log_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_full_trace_tail512_seed42/\", \"submitted_at\": \"2026-05-19T00:11:39.795Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_full_trace_tail512_seed42/final\", \"wall_clock_seconds\": 8329.2, \"gpu_hours\": 2.31}, \"metrics\": {\"accuracy\": 0.9824, \"accuracy_ci_lower\": 0.9748, \"accuracy_ci_upper\": 0.9899, \"majority_baseline\": 0.7151, \"lift\": 0.2672, \"n\": 1190, \"pass_precision\": 0.9759, \"pass_recall\": 1, \"pass_f1\": 0.9878, \"fail_precision\": 1, \"fail_recall\": 0.9381, \"fail_f1\": 0.968}, \"conclusion\": \"success\"}, \"codellama13b_full_trace_tail512_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:30:05.472Z\", \"updated_at\": \"2026-05-19T01:34:01.229Z\", \"hypothesis\": \"CodeLlama-13B tail-512 seed456 (label_only_loss) 应在 93-97% range（与 seed42 一致），验证 phase transition 后 convergence band 的 seed robustness 跨架构成立\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_full_trace_tail512_seed456/final\", \"log_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_full_trace_tail512_seed456/\"}, \"metrics\": {\"accuracy\": 0.9824, \"accuracy_ci_lower\": 0.9748, \"accuracy_ci_upper\": 0.9899, \"majority_baseline\": 0.7151, \"lift\": 0.2672, \"n\": 1190, \"pass_precision\": 0.9759, \"pass_recall\": 1, \"pass_f1\": 0.9878, \"fail_precision\": 1, \"fail_recall\": 0.9381, \"fail_f1\": 0.968, \"seed_comparison\": {\"seed42_previous\": 0.975, \"seed123_accuracy\": 0.9824, \"seed456_accuracy\": 0.9824}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T01:33:54.360Z\"}, \"codellama13b_full_trace_tail512_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:30:04.091Z\", \"updated_at\": \"2026-05-18T23:09:01.135Z\", \"hypothesis\": \"CodeLlama-13B tail-512 seed123 (label_only_loss) 应在 93-97% range（与 seed42 一致），验证 phase transition 后 convergence band 的 seed robustness 跨架构成立\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/trace-verdict-study && /root/miniconda3/bin/python train/train_sft.py --condition full_trace_tail_512 --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf/ --seed 123 --gradient_checkpointing --label_only_loss --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_full_trace_tail512_seed123/ --wandb_project trace-verdict-study --wandb_run_name codellama13b_full_trace_tail512_seed123 && /root/miniconda3/bin/python eval/evaluate.py --condition full_trace_tail_512 --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_full_trace_tail512_seed123/final --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf/ --save_predictions\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"466393\", \"log_path\": \"~/runs/trace-verdict-study/codellama13b_full_trace_tail512_seed123.log\", \"submitted_at\": \"2026-05-18T20:55:23.272Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/trace-verdict-study/data/\", \"data_count\": 4720, \"model_name\": \"CodeLlama-13b-Instruct-hf\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_full_trace_tail512_seed123/final\", \"wall_clock_seconds\": 8017.9, \"gpu_hours\": 2.23}, \"metrics\": {\"accuracy\": 0.9824, \"accuracy_ci_lower\": 0.9748, \"accuracy_ci_upper\": 0.9899, \"majority_baseline\": 0.7151, \"lift\": 0.2672, \"n\": 1190, \"pass_precision\": 0.9759, \"pass_recall\": 1, \"pass_f1\": 0.9878, \"fail_precision\": 1, \"fail_recall\": 0.9381, \"fail_f1\": 0.968, \"seed_comparison\": {\"seed42_accuracy\": 0.975, \"seed123_accuracy\": 0.9824, \"diff\": 0.0074, \"note\": \"seed123 (98.24%) slightly exceeds seed42 (97.5%); both well above 97% — CodeLlama-13B tail-512 seed-robust\"}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T23:09:01.135Z\"}, \"qwen15b_exception_only_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T20:35:27.310Z\", \"updated_at\": \"2026-05-18T23:08:55.815Z\", \"hypothesis\": \"Qwen-1.5B exception_only seed456 应达 ~99.83%（与 seed42 一致），为 W3 reviewer concern 提供 1.5B scale 的方差估计\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python train/train_sft.py --condition exception_only --model_path /root/trace-verdict-study/models/Qwen2.5-Coder-1.5B-Instruct --seed 456 --gradient_checkpointing --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_exception_only_seed456/ --wandb_project trace-verdict-study --wandb_run_name qwen15b_exception_only_seed456\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/trace-verdict-study/qwen15b_exception_only_seed456.log\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/trace-verdict-study/data/\", \"data_count\": 4720, \"model_name\": \"Qwen2.5-Coder-1.5B-Instruct\", \"seed\": 456, \"fix_note\": \"Added --gradient_checkpointing to fix OOM\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_exception_only_seed456/final\"}, \"metrics\": {\"accuracy\": 0.9983, \"accuracy_ci_lower\": 0.9958, \"accuracy_ci_upper\": 1, \"majority_baseline\": 0.7151, \"lift\": 0.2832, \"n\": 1190, \"pass_precision\": 1, \"pass_recall\": 0.9976, \"pass_f1\": 0.9988, \"fail_precision\": 0.9941, \"fail_recall\": 1, \"fail_f1\": 0.9971, \"seed_comparison\": {\"seed42_accuracy\": 0.9983, \"seed456_accuracy\": 0.9983, \"diff\": 0, \"note\": \"Identical to seed42 to 4 decimal places — exception_only fully seed-robust on Qwen-1.5B\"}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T23:08:55.815Z\"}, \"qwen7b_full_trace_tail512_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:30:02.727Z\", \"updated_at\": \"2026-05-18T20:17:15.561Z\", \"hypothesis\": \"Qwen-7B tail-512 seed456 应在 93-97% range（与 full_trace_tail_512_seed42=93.6% 一致），验证 phase transition 后 convergence band 的 seed robustness\", \"spec\": {\"command\": \"train full_trace_tail_512 qwen7b seed456\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"461573\", \"log_path\": \"/root/runs/trace-verdict-study/qwen7b_full_trace_tail512_seed456.log\", \"submitted_at\": \"2026-05-18T19:15:06.380Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/trace-verdict-study/data/\", \"data_count\": 4720, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 456, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen7b_full_trace_tail512_seed456/final\", \"wall_clock_seconds\": 3729.2, \"gpu_hours\": 1.04}, \"metrics\": {\"accuracy\": 0.9765, \"majority_baseline\": 0.7151, \"lift\": 0.2613, \"n\": 1190, \"pass_precision\": 0.9746, \"pass_recall\": 0.9929, \"pass_f1\": 0.9837, \"fail_precision\": 0.9814, \"fail_recall\": 0.9351, \"fail_f1\": 0.9577, \"accuracy_ci\": [0.9681, 0.9849]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T20:17:15.562Z\"}, \"deepseek_full_trace_tail512_seed123_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:32:10.775Z\", \"updated_at\": \"2026-05-18T20:17:14.170Z\", \"hypothesis\": \"DeepSeek-6.7B tail-512 seed123 应在 93-97% range（与 seed42=93.61% 一致），验证 phase transition 后 convergence band 的 seed robustness。v1 因 GPU OOM 失败，重试。\", \"parent\": \"deepseek_full_trace_tail512_seed123\", \"spec\": {\"command\": \"train full_trace_tail_512 deepseek seed123 v2\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"pid\": \"459485\", \"log_path\": \"/root/runs/trace-verdict-study/deepseek_full_trace_tail512_seed123_v2.log\", \"submitted_at\": \"2026-05-18T18:55:41.122Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/trace-verdict-study/data/\", \"data_count\": 4720, \"model_name\": \"deepseek-coder-6.7b-instruct\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_full_trace_tail512_seed123_v2/final\", \"checkpoint_source\": \"deepseek_full_trace_tail512_seed123\", \"eval_data\": \"full_trace_tail_512_eval\", \"wall_clock_seconds\": 4893.0, \"gpu_hours\": 1.36}, \"metrics\": {\"accuracy\": 0.9504, \"majority_baseline\": 0.7151, \"lift\": 0.2353, \"n\": 1190, \"pass_precision\": 0.976, \"pass_recall\": 0.9542, \"pass_f1\": 0.9649, \"fail_precision\": 0.8911, \"fail_recall\": 0.941, \"fail_f1\": 0.9154, \"accuracy_ci\": [0.9387, 0.963]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T20:17:14.170Z\"}, \"qwen7b_full_trace_tail512_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:25:03.679Z\", \"updated_at\": \"2026-05-18T18:39:51.351Z\", \"hypothesis\": \"Qwen-7B tail-512 seed123 应在 93-97% range（与 full_trace_tail_512_seed42=93.6% 一致），验证 phase transition 后 convergence band 的 seed robustness\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/trace-verdict-study && /root/miniconda3/bin/python train/train_sft.py --condition full_trace_tail_512 --model_path /root/trace-verdict-study/models/Qwen2.5-Coder-7B-Instruct --seed 123 --gradient_checkpointing --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen7b_full_trace_tail512_seed123/ --wandb_project trace-verdict-study --wandb_run_name qwen7b_full_trace_tail512_seed123 && /root/miniconda3/bin/python eval/evaluate.py --condition full_trace_tail_512 --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen7b_full_trace_tail512_seed123/final --model_path /root/trace-verdict-study/models/Qwen2.5-Coder-7B-Instruct --save_predictions\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"pid\": \"452111\", \"log_path\": \"~/runs/trace-verdict-study/qwen7b_full_trace_tail512_seed123.log\", \"submitted_at\": \"2026-05-18T16:29:10.415Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen7b_full_trace_tail512_seed123/final\", \"wall_clock_seconds\": 7840.9, \"gpu_hours\": 2.18}, \"metrics\": {\"accuracy\": 0.9597, \"accuracy_ci_lower\": 0.9487, \"accuracy_ci_upper\": 0.9706, \"majority_baseline\": 0.7151, \"lift\": 0.2445, \"n\": 1190, \"pass_precision\": 0.9751, \"pass_recall\": 0.9683, \"pass_f1\": 0.9717, \"fail_precision\": 0.9217, \"fail_recall\": 0.9381, \"fail_f1\": 0.9298, \"seed_comparison\": {\"seed42_accuracy\": 0.936, \"seed123_accuracy\": 0.9597}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T18:39:51.351Z\"}, \"deepseek_full_trace_tail512_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:25:05.108Z\", \"updated_at\": \"2026-05-18T18:39:50.164Z\", \"hypothesis\": \"DeepSeek-6.7B tail-512 seed456 应在 93-97% range（与 seed42 一致），验证 phase transition 后 convergence band 的 seed robustness\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/trace-verdict-study && /root/miniconda3/bin/python train/train_sft.py --condition full_trace_tail_512 --model_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct --seed 456 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_full_trace_tail512_seed456/ --wandb_project trace-verdict-study --wandb_run_name deepseek_full_trace_tail512_seed456 && /root/miniconda3/bin/python eval/evaluate.py --condition full_trace_tail_512 --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_full_trace_tail512_seed456/final --model_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct --save_predictions\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"452190\", \"log_path\": \"~/runs/trace-verdict-study/deepseek_full_trace_tail512_seed456.log\", \"submitted_at\": \"2026-05-18T16:29:13.700Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_full_trace_tail512_seed456/final\", \"wall_clock_seconds\": 7836.5, \"gpu_hours\": 2.18}, \"metrics\": {\"accuracy\": 0.9605, \"accuracy_ci_lower\": 0.9496, \"accuracy_ci_upper\": 0.9714, \"majority_baseline\": 0.7151, \"lift\": 0.2454, \"n\": 1190, \"pass_precision\": 0.9752, \"pass_recall\": 0.9694, \"pass_f1\": 0.9723, \"fail_precision\": 0.9244, \"fail_recall\": 0.9381, \"fail_f1\": 0.9312, \"seed_comparison\": {\"seed42_accuracy\": 0.9361, \"seed456_accuracy\": 0.9605}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T18:39:50.164Z\"}, \"deepseek_full_trace_tail512_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T15:48:44.674Z\", \"updated_at\": \"2026-05-18T16:31:59.050Z\", \"hypothesis\": \"DeepSeek-6.7B tail-512 seed123 应在 93-97% range（与 seed42 一致），验证 phase transition 后 convergence band 的 seed robustness\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/trace-verdict-study && /root/miniconda3/bin/python train/train_sft.py --condition full_trace_tail_512 --model_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct --seed 123 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_full_trace_tail512_seed123/ --wandb_project trace-verdict-study --wandb_run_name deepseek_full_trace_tail512_seed123 && /root/miniconda3/bin/python eval/evaluate.py --condition full_trace_tail_512 --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_full_trace_tail512_seed123/final --model_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct --save_predictions\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"pid\": \"449827\", \"log_path\": \"/root/runs/trace-verdict-study/deepseek_full_trace_tail512_seed123.log\", \"submitted_at\": \"2026-05-18T15:49:10.240Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A - training OOM at step 0\", \"wall_clock_seconds\": 2537.4, \"gpu_hours\": 0.7}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-18T16:31:27.635Z\", \"metrics\": {\"error\": \"CUDA OOM at step 0/444\", \"exit_code\": 1, \"failure_time\": \"2026-05-18T15:49:48Z\", \"cause\": \"GPU 0 memory exhausted (43.45 GiB PyTorch allocated, only 167.56 MiB free when trying to allocate 178 MiB)\", \"seed_comparison\": {\"seed42_accuracy\": 0.9361, \"seed123_accuracy\": \"N/A - OOM crash\"}}}, \"qwen15b_full_trace_tail512_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T15:48:43.426Z\", \"updated_at\": \"2026-05-18T16:28:37.149Z\", \"hypothesis\": \"Qwen-1.5B tail-512 seed456 应在 93-97% range（与 seed42 一致），验证 phase transition 后 convergence band 的 seed robustness\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/trace-verdict-study && /root/miniconda3/bin/python train/train_sft.py --condition full_trace_tail_512 --model_path /root/trace-verdict-study/models/Qwen2.5-Coder-1.5B-Instruct --seed 456 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_tail512_seed456/ --wandb_project trace-verdict-study --wandb_run_name qwen15b_full_trace_tail512_seed456 && /root/miniconda3/bin/python eval/evaluate.py --condition full_trace_tail_512 --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_tail512_seed456/final --model_path /root/trace-verdict-study/models/Qwen2.5-Coder-1.5B-Instruct --save_predictions\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"449685\", \"log_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_tail512_seed456/\", \"submitted_at\": \"2026-05-18T15:49:06.692Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_tail512_seed456/final\", \"wall_clock_seconds\": 2370.5, \"gpu_hours\": 0.66}, \"metrics\": {\"accuracy\": 0.9672, \"accuracy_ci_lower\": 0.9563, \"accuracy_ci_upper\": 0.9773, \"majority_baseline\": 0.7151, \"lift\": 0.2521, \"n\": 1190, \"pass_precision\": 0.9765, \"pass_recall\": 0.9777, \"pass_f1\": 0.9771, \"fail_precision\": 0.9438, \"fail_recall\": 0.941, \"fail_f1\": 0.9424, \"seed_comparison\": {\"seed42_accuracy\": 0.956, \"seed123_accuracy\": 0.9765, \"seed456_accuracy\": 0.9672, \"note\": \"seed456 (96.72%) within convergence band [95.6%, 97.65%], confirming seed robustness post-phase-transition\"}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T16:28:37.149Z\"}, \"codellama13b_full_trace_tail384_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T12:06:06.157Z\", \"updated_at\": \"2026-05-18T15:51:11.441Z\", \"hypothesis\": \"CodeLlama-13B tail-384 (label_only_loss) 应在 85-95% 之间（256→512 phase transition 中间点），验证 label_only_loss 在短序列下也有效\", \"spec\": {\"data_path\": \"/root/trace-verdict-study/data/\", \"data_count\": 600, \"model_name\": \"CodeLlama-13b-Instruct-hf\", \"seed\": 42, \"checkpoint_source\": \"trained_from_scratch\", \"eval_data\": \"/root/trace-verdict-study/data/test.jsonl\", \"label_only_loss\": true}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_full_trace_tail384_seed42/final\", \"log_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_full_trace_tail384_seed42/runs\", \"metrics\": {\"accuracy\": 0.8269, \"accuracy_ci_lower\": 0.8067, \"accuracy_ci_upper\": 0.8471, \"majority_baseline\": 0.7151, \"lift\": 0.1118, \"n\": 1190, \"pass_precision\": 0.8314, \"pass_recall\": 0.9506, \"pass_f1\": 0.8871, \"fail_precision\": 0.8065, \"fail_recall\": 0.5162, \"fail_f1\": 0.6295}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-18T15:51:11.441Z\"}, \"qwen15b_full_trace_tail512_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T14:56:42.559Z\", \"updated_at\": \"2026-05-18T15:51:10.277Z\", \"hypothesis\": \"Qwen-1.5B tail-512 seed123 应在 93-97% range（与 seed42 一致），验证 phase transition 后 convergence band 的 seed robustness\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/trace-verdict-study && /root/miniconda3/bin/python train/train_sft.py --condition full_trace_tail_512 --model_path /root/trace-verdict-study/models/Qwen2.5-Coder-1.5B-Instruct --seed 123 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_tail512_seed123/ --wandb_project trace-verdict-study --wandb_run_name qwen15b_full_trace_tail512_seed123 && /root/miniconda3/bin/python eval/evaluate.py --condition full_trace_tail_512 --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_tail512_seed123/final --model_path /root/trace-verdict-study/models/Qwen2.5-Coder-1.5B-Instruct --save_predictions\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"447690\", \"log_path\": \"~/runs/trace-verdict-study/qwen15b_full_trace_tail512_seed123.log\", \"submitted_at\": \"2026-05-18T15:16:16.177Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 2094.1, \"gpu_hours\": 0.58}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_tail512_seed123/final\", \"log_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_tail512_seed123/runs\", \"metrics\": {\"accuracy\": 0.9765, \"accuracy_ci_lower\": 0.9681, \"accuracy_ci_upper\": 0.9849, \"majority_baseline\": 0.7151, \"lift\": 0.2613, \"n\": 1190, \"pass_precision\": 0.9757, \"pass_recall\": 0.9918, \"pass_f1\": 0.9837, \"fail_precision\": 0.9785, \"fail_recall\": 0.9381, \"fail_f1\": 0.9578, \"seed_comparison\": {\"seed42_accuracy\": 0.956, \"seed123_accuracy\": 0.9765, \"note\": \"seed123 (97.65%) exceeds seed42 (95.6%) by 2pp; both in convergence band post-phase-transition\"}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T15:51:10.277Z\"}, \"qwen15b_full_trace_tail384_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T12:06:04.119Z\", \"updated_at\": \"2026-05-18T15:17:01.787Z\", \"hypothesis\": \"Qwen-1.5B tail-384 应在 80-90% 之间（小模型在 transition zone 可能更低），精确定位 phase transition 曲线形状\", \"spec\": {\"data_path\": \"/root/trace-verdict-study/data/\", \"data_count\": 600, \"model_name\": \"Qwen2.5-Coder-1.5B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"trained_from_scratch\", \"eval_data\": \"/root/trace-verdict-study/data/test.jsonl\", \"label_only_loss\": false, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_tail384_seed42/final\", \"log_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_tail384_seed42\"}, \"metrics\": {\"accuracy\": 0.7361, \"majority_baseline\": 0.7151, \"lift\": 0.021, \"n\": 1190, \"pass_precision\": 0.8069, \"pass_recall\": 0.8296, \"pass_f1\": 0.8181, \"fail_precision\": 0.5397, \"fail_recall\": 0.5015, \"fail_f1\": 0.5199, \"accuracy_ci\": [0.7101, 0.7622]}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-18T15:17:01.788Z\"}, \"qwen7b_full_trace_tail384_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T12:06:01.294Z\", \"updated_at\": \"2026-05-18T13:52:36.911Z\", \"hypothesis\": \"Qwen-7B tail-384 应在 85-93% 之间（256→512 phase transition 的中间点），精确定位 phase transition 曲线形状\", \"spec\": {\"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"command\": \"source /root/miniconda3/bin/activate && python train/train_sft.py --condition full_trace_tail_384 --model_path /root/trace-verdict-study/models/Qwen2.5-Coder-7B-Instruct --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen7b_full_trace_tail384_seed42 --gpu 1 --seed 42 --gradient_checkpointing\", \"data_path\": \"/root/trace-verdict-study/data/\", \"data_count\": 600, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen7b_full_trace_tail384_seed42/final\", \"log_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen7b_full_trace_tail384_seed42/final/eval_results.json\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.798, \"accuracy_ci_lower\": 0.776, \"accuracy_ci_upper\": 0.821, \"majority_baseline\": 0.715, \"lift\": 0.083, \"n\": 1190, \"pass_precision\": 0.89, \"pass_recall\": 0.82, \"pass_f1\": 0.85, \"fail_precision\": 0.62, \"fail_recall\": 0.75, \"fail_f1\": 0.68}, \"completed_at\": \"2026-05-18T13:52:36.911Z\"}, \"deepseek_full_trace_tail384_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T12:06:02.727Z\", \"updated_at\": \"2026-05-18T13:52:35.606Z\", \"hypothesis\": \"DeepSeek-6.7B tail-384 应在 85-93% 之间（256→512 phase transition 的中间点），精确定位 phase transition 曲线形状\", \"spec\": {\"server\": \"westd-11235\", \"gpu\": \"cuda:0\", \"command\": \"source /root/miniconda3/bin/activate && python train/train_sft.py --condition full_trace_tail_384 --model_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_full_trace_tail384_seed42 --gpu 0 --seed 42\", \"data_path\": \"/root/trace-verdict-study/data/\", \"data_count\": 600, \"model_name\": \"deepseek-coder-6.7b-instruct\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_full_trace_tail384_seed42/final\", \"log_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_full_trace_tail384_seed42/final/eval_results.json\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.807, \"accuracy_ci_lower\": 0.786, \"accuracy_ci_upper\": 0.829, \"majority_baseline\": 0.715, \"lift\": 0.092, \"n\": 1190, \"pass_precision\": 0.83, \"pass_recall\": 0.92, \"pass_f1\": 0.87, \"fail_precision\": 0.73, \"fail_recall\": 0.51, \"fail_f1\": 0.6}, \"completed_at\": \"2026-05-18T13:52:35.607Z\"}, \"qwen7b_full_trace_head2048_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T08:01:11.546Z\", \"updated_at\": \"2026-05-18T12:07:15.686Z\", \"hypothesis\": \"Qwen-7B head-2048 应在 75-82% (signal-poor convergence band)，与其他 3 模型 head-2048 (75.3-79.9%) 对齐，补全 4 模型 head-tail gap claim\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen7b_full_trace_head2048_seed42/\", \"log_path\": \"~/runs/trace-verdict-study/qwen7b_full_trace_head2048_seed42.log\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy_epoch1\": 0.816, \"accuracy_epoch3\": 0.81, \"pass_f1_epoch1\": 0.87, \"fail_f1_epoch1\": 0.686, \"pass_f1_epoch3\": 0.866, \"fail_f1_epoch3\": 0.674, \"best_accuracy\": 0.816, \"best_epoch\": 1}, \"completed_at\": \"2026-05-18T12:07:15.686Z\"}, \"codellama13b_full_trace_tail2048_seed42_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T07:51:07.325Z\", \"updated_at\": \"2026-05-18T12:07:14.546Z\", \"hypothesis\": \"CodeLlama-13B tail-2048 用 label_only_loss 应恢复到 95-98%（与其他 3 模型 tail-2048 对齐），确认 v2 的 29.6% 源于 full-sequence loss 稀释\", \"parent\": \"codellama13b_full_trace_tail2048_seed42_v2\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_full_trace_tail2048_seed42_v3/\", \"log_path\": \"~/runs/trace-verdict-study/codellama13b_full_trace_tail2048_seed42_v3.log\"}, \"conclusion\": \"negative\", \"metrics\": {\"accuracy_epoch1\": 0.071, \"accuracy_epoch3\": 0.418, \"pass_f1_epoch3\": 0.416, \"fail_f1_epoch3\": 0.421, \"pass_f1_epoch1\": 0.035, \"fail_f1_epoch1\": 0.342, \"train_loss\": 0.785}, \"completed_at\": \"2026-05-18T12:07:14.546Z\"}, \"codellama13b_full_trace_tail1024_seed42_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T06:39:08.941Z\", \"updated_at\": \"2026-05-18T09:43:42.053Z\", \"hypothesis\": \"CodeLlama-13B tail-1024 用 label_only_loss 应恢复到 ~96.5%（与 DeepSeek 96.47%、Qwen-1.5B 96.6% 对齐），确认 v2 的 87.6% 源于 full-sequence loss 稀释而非 tail-1024 条件本身\", \"parent\": \"codellama13b_full_trace_tail1024_seed42_v2\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_full_trace_tail1024_seed42_v3/\", \"log_path\": \"~/runs/trace-verdict-study/codellama13b_full_trace_tail1024_seed42_v3.log\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy_epoch1\": 0.9824, \"accuracy_epoch3\": 0.9756, \"pass_f1_epoch1\": 0.988, \"fail_f1_epoch1\": 0.968, \"pass_f1_epoch3\": 0.983, \"fail_f1_epoch3\": 0.955, \"best_accuracy\": 0.9824, \"best_epoch\": 1, \"overfitting\": true}, \"completed_at\": \"2026-05-18T09:43:42.053Z\"}, \"codellama13b_full_trace_tail2048_seed42_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T03:52:51.335Z\", \"updated_at\": \"2026-05-18T07:51:13.642Z\", \"hypothesis\": \"CodeLlama-13B tail-2048 应在 95-98%，head-tail gap ≥15pp，确认 signal positional concentration 跨 4 模型\", \"parent\": \"codellama13b_full_trace_head2048_seed42\", \"spec\": {\"command\": \"bash -c 'cd /root/trace-verdict-study && /root/miniconda3/bin/python train/train_sft.py --condition full_trace_tail --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_full_trace_tail2048_seed42_v2 --seed 42 --wandb_project trace-verdict-study --wandb_run_name codellama13b_full_trace_tail2048_seed42_v2 --gradient_checkpointing'\", \"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"pid\": \"405136\", \"log_path\": \"~/runs/trace-verdict-study/codellama13b_full_trace_tail2048_seed42_v2.log\", \"submitted_at\": \"2026-05-18T03:53:12.769Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/trace-verdict-study/data/\", \"data_count\": 600, \"model_name\": \"CodeLlama-13b-Instruct-hf\", \"seed\": 42, \"checkpoint_source\": \"trained_from_scratch\", \"eval_data\": \"/root/trace-verdict-study/data/test.jsonl\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_full_trace_tail2048_seed42_v2/final\", \"wall_clock_seconds\": 14280.9, \"gpu_hours\": 3.97}, \"metrics\": {\"accuracy_epoch1\": 0.2849, \"accuracy_epoch3\": 0.2958, \"pass_recall_epoch3\": 0.016, \"fail_recall_epoch3\": 0.997, \"majority_baseline\": 0.715, \"n_test\": 1190, \"note\": \"Catastrophic failure: model predicts fail for almost everything. Full-sequence loss dilution with CodeLlama tokenizer at 2048 tokens.\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-18T07:51:13.642Z\"}, \"codellama13b_full_trace_tail1024_seed42_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T03:25:33.875Z\", \"updated_at\": \"2026-05-18T06:15:35.443Z\", \"hypothesis\": \"CodeLlama-13B tail-1024 应收敛到 96.5% 附近（与 DeepSeek 96.47%、Qwen-1.5B 96.6% 不可区分），确认 tail-1024 convergence band 跨 4 模型 universal\", \"parent\": \"codellama13b_full_trace_tail512_seed42\", \"spec\": {\"command\": \"bash -c 'cd /root/trace-verdict-study && /root/miniconda3/bin/python train/train_sft.py --condition full_trace_tail_1024 --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_full_trace_tail1024_seed42_v2 --seed 42 --wandb_project trace-verdict-study --wandb_run_name codellama13b_full_trace_tail1024_seed42_v2 --gradient_checkpointing'\", \"server\": \"westd-11235\", \"gpu\": \"cuda:0\", \"pid\": \"403386\", \"log_path\": \"~/runs/trace-verdict-study/codellama13b_full_trace_tail1024_seed42_v2.log\", \"submitted_at\": \"2026-05-18T03:26:05.733Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/trace-verdict-study/data/\", \"data_count\": 600, \"model_name\": \"CodeLlama-13b-Instruct-hf\", \"seed\": 42, \"checkpoint_source\": \"trained_from_scratch\", \"eval_data\": \"/root/trace-verdict-study/data/test.jsonl\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_full_trace_tail1024_seed42_v2/final\", \"wall_clock_seconds\": 10169.7, \"gpu_hours\": 2.82}, \"metrics\": {\"accuracy\": 0.876, \"accuracy_ci_lower\": 0.856, \"accuracy_ci_upper\": 0.893, \"majority_baseline\": 0.715, \"lift_pp\": 16.1, \"pass_precision\": 0.85, \"pass_recall\": 1, \"pass_f1\": 0.92, \"fail_precision\": 1, \"fail_recall\": 0.56, \"fail_f1\": 0.72, \"n_test\": 1190, \"train_loss\": 0.0937, \"eval_loss\": 0.1859}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-18T06:15:35.443Z\"}, \"codellama13b_full_trace_tail2048_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T03:47:21.197Z\", \"updated_at\": \"2026-05-18T03:52:43.842Z\", \"hypothesis\": \"CodeLlama-13B tail-2048 应在 95-98%，head-tail gap ≥15pp，确认 signal positional concentration 跨 4 模型\", \"parent\": \"codellama13b_full_trace_head2048_seed42\", \"spec\": {\"command\": \"bash -c 'cd /root/trace-verdict-study && /root/miniconda3/bin/python train/train_sft.py --condition full_trace_tail_2048 --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_full_trace_tail2048_seed42 --seed 42 --wandb_project trace-verdict-study --wandb_run_name codellama13b_full_trace_tail2048_seed42 --gradient_checkpointing'\", \"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"pid\": \"404579\", \"log_path\": \"N/A\", \"submitted_at\": \"2026-05-18T03:47:52.601Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/trace-verdict-study/data/\", \"data_count\": 600, \"model_name\": \"CodeLlama-13b-Instruct-hf\", \"seed\": 42, \"checkpoint_source\": \"trained_from_scratch\", \"eval_data\": \"/root/trace-verdict-study/data/test.jsonl\", \"checkpoint_path\": \"N/A\", \"failure_reason\": \"Invalid condition: full_trace_tail_2048 not in choices. Correct condition is full_trace_tail.\", \"wall_clock_seconds\": 291.2, \"gpu_hours\": 0.08}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-18T03:52:43.842Z\"}, \"codellama13b_full_trace_head2048_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T23:20:24.115Z\", \"updated_at\": \"2026-05-18T03:37:20.611Z\", \"hypothesis\": \"CodeLlama-13B head-2048 truncation should yield 75-82% accuracy, confirming signal positional concentration pattern across 4 model families where tail-2048 significantly outperforms head-2048\", \"parent\": \"codellama13b_exception_only_seed42\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python train.py --model /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf/ --condition full_trace --truncation head --max_tokens 2048 --seed 42'\", \"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"pid\": \"391743\", \"log_path\": \"~/runs/trace-verdict-study/codellama13b_full_trace_head2048_seed42.log\", \"submitted_at\": \"2026-05-17T23:42:34.564Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/trace-verdict-study/data/\", \"data_count\": 600, \"model_name\": \"CodeLlama-13b-Instruct-hf\", \"seed\": 42, \"checkpoint_source\": \"trained_from_scratch\", \"eval_data\": \"/root/trace-verdict-study/data/test.jsonl\", \"wall_clock_seconds\": 14086.0, \"gpu_hours\": 3.91}, \"reproduce\": {\"finished_at\": \"2026-05-18T03:32:04.847Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T03:32:08.458585+00:00\"}]}, \"metrics\": {\"accuracy\": 0.7992, \"majority_baseline\": 0.7151, \"lift\": 0.084, \"n_test\": 1190, \"pass_precision\": 0.8566, \"pass_recall\": 0.8637, \"pass_f1\": 0.8602, \"fail_precision\": 0.6506, \"fail_recall\": 0.6372, \"fail_f1\": 0.6438, \"train_loss\": 0.0452, \"eval_loss\": 0.111, \"accuracy_ci_lower\": 0.7765, \"accuracy_ci_upper\": 0.8227}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_full_trace_head2048_seed42/final\", \"log_path\": \"/root/trace-verdict-study/logs/codellama13b_head2048_seed42.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T03:37:20.611Z\"}, \"codellama13b_full_trace_tail256_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T01:37:42.953Z\", \"updated_at\": \"2026-05-18T03:33:11.185Z\", \"hypothesis\": \"CodeLlama-13B tail-256 应在 78-85%，与 7B 级模型 tail-256 (76-79%) 类似或略高，确认 256 tokens 信号不足是 universal 的\", \"parent\": \"codellama13b_full_trace_tail512_seed42\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python train.py --model /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf/ --condition full_trace --truncation tail --max_tokens 256 --seed 42'\", \"server\": \"westd-11235\", \"gpu\": \"cuda:0\", \"pid\": \"397742\", \"log_path\": \"~/runs/trace-verdict-study/codellama13b_full_trace_tail256_seed42.log\", \"submitted_at\": \"2026-05-18T01:41:17.373Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/trace-verdict-study/data/\", \"data_count\": 600, \"model_name\": \"CodeLlama-13b-Instruct-hf\", \"seed\": 42, \"checkpoint_source\": \"trained_from_scratch\", \"eval_data\": \"/root/trace-verdict-study/data/test.jsonl\", \"wall_clock_seconds\": 6713.8, \"gpu_hours\": 1.86}, \"reproduce\": {\"finished_at\": \"2026-05-18T02:23:11.443Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T02:23:17.445961+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.779, \"accuracy_ci_lower\": 0.757, \"accuracy_ci_upper\": 0.803, \"pass_f1\": 0.843, \"fail_f1\": 0.626, \"pass_precision\": 0.856, \"pass_recall\": 0.831, \"fail_precision\": 0.604, \"fail_recall\": 0.649, \"majority_baseline\": 0.715, \"lift\": 0.064, \"train_loss\": 0.245, \"eval_loss\": 0.615}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_full_trace_tail256_seed42/final\", \"log_path\": \"~/runs/trace-verdict-study/codellama13b_full_trace_tail256_seed42.log\", \"completed_at\": \"2026-05-18T03:33:11.186Z\"}, \"codellama13b_full_trace_tail1024_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T01:37:33.166Z\", \"updated_at\": \"2026-05-18T03:25:19.162Z\", \"hypothesis\": \"CodeLlama-13B tail-1024 应收敛到 96.5% 附近（与 DeepSeek 96.47%、Qwen-1.5B 96.6% 不可区分），确认 tail-1024 convergence band 跨 4 模型 universal\", \"parent\": \"codellama13b_full_trace_tail512_seed42\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/trace-verdict-study && python train.py --model /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf/ --condition full_trace --truncation tail --max_tokens 1024 --seed 42'\", \"server\": \"westd-11235\", \"gpu\": \"cuda:0\", \"pid\": \"unknown\", \"log_path\": \"N/A\", \"submitted_at\": \"2026-05-18T02:28:32.411Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/trace-verdict-study/data/\", \"data_count\": 600, \"model_name\": \"CodeLlama-13b-Instruct-hf\", \"seed\": 42, \"checkpoint_source\": \"trained_from_scratch\", \"eval_data\": \"/root/trace-verdict-study/data/test.jsonl\", \"checkpoint_path\": \"N/A\", \"failure_reason\": \"Wrong script path: used train.py instead of train/train_sft.py. Process exited immediately with Errno 2.\", \"wall_clock_seconds\": 3406.8, \"gpu_hours\": 0.95}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-18T03:25:19.162Z\"}, \"qwen15b_full_trace_tail1024_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T22:48:55.914Z\", \"updated_at\": \"2026-05-18T01:45:09.341Z\", \"hypothesis\": \"1.5B tail-1024 可能低于 tail-512 (95.6%)，如同 7B non-monotonicity；因中等长度 trace 包含 noisy intermediate states\", \"parent\": \"qwen15b_full_trace_tail512_seed42\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python train.py --model /root/trace-verdict-study/models/Qwen2.5-Coder-1.5B-Instruct --condition full_trace --truncation tail --max_tokens 1024 --seed 42'\", \"server\": \"westd-11235\", \"gpu\": \"cuda:0\", \"pid\": \"388161\", \"log_path\": \"~/runs/trace-verdict-study/qwen15b_full_trace_tail1024_seed42.log\", \"submitted_at\": \"2026-05-17T22:51:42.254Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/trace-verdict-study/data/\", \"data_count\": 600, \"model_name\": \"Qwen2.5-Coder-1.5B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"trained_from_scratch\", \"eval_data\": \"/root/trace-verdict-study/data/test.jsonl\", \"wall_clock_seconds\": 10407.1, \"gpu_hours\": 2.89}, \"reproduce\": {\"finished_at\": \"2026-05-17T23:12:12.100Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T23:12:15.209322+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_tail1024_seed42/final\", \"log_path\": \"~/runs/trace-verdict-study/qwen15b_full_trace_tail1024_seed42.log\", \"metrics\": {\"accuracy\": 0.966, \"accuracy_ci_low\": 0.955, \"accuracy_ci_high\": 0.976, \"pass_precision\": 0.96, \"pass_recall\": 0.99, \"pass_f1\": 0.98, \"fail_precision\": 0.97, \"fail_recall\": 0.91, \"fail_f1\": 0.94, \"eval_loss\": 0.1983, \"train_loss\": 0.1187, \"majority_baseline\": 0.715, \"lift_over_majority_pp\": 25}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T01:45:09.341Z\"}, \"deepseek_full_trace_tail1024_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T21:23:57.882Z\", \"updated_at\": \"2026-05-17T23:14:09.157Z\", \"hypothesis\": \"DeepSeek tail-1024 可能低于 tail-512（如同 Qwen-7B non-monotonicity），因为 1024 tokens 包含了 noisy intermediate states；如果也出现 non-monotonicity 则确认跨架构\", \"parent\": \"deepseek_full_trace_tail256_seed42\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_full_trace_tail1024_seed42/final\", \"log_path\": \"/root/trace-verdict-study/logs/deepseek_tail1024_seed42.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-17T23:09:36.935Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T23:09:39.909092+00:00\"}]}, \"metrics\": {\"accuracy\": 0.9647, \"accuracy_ci_lower\": 0.9538, \"accuracy_ci_upper\": 0.9748, \"pass_precision\": 0.964, \"pass_recall\": 0.987, \"pass_f1\": 0.976, \"fail_precision\": 0.966, \"fail_recall\": 0.909, \"fail_f1\": 0.936, \"majority_baseline\": 0.7151, \"n_test\": 1190}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T23:14:09.157Z\"}, \"deepseek_full_trace_tail512_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T21:12:42.017Z\", \"updated_at\": \"2026-05-17T22:32:35.246Z\", \"hypothesis\": \"DeepSeek tail-512 应在 88-94%，与 Qwen-7B tail-512 (93.61%) 对齐则 phase transition 阈值 architecture-independent\", \"parent\": \"deepseek_full_trace_tail256_seed42\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python train.py --model /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct --condition full_trace --truncation tail --max_tokens 512 --seed 42'\", \"server\": \"westd-11235\", \"gpu\": \"cuda:0\", \"pid\": \"382268\", \"log_path\": \"~/runs/trace-verdict-study/deepseek_full_trace_tail512_seed42.log\", \"submitted_at\": \"2026-05-17T21:14:49.694Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/trace-verdict-study/data/\", \"data_count\": 600, \"model_name\": \"deepseek-coder-6.7b-instruct\", \"seed\": 42, \"checkpoint_source\": \"trained_from_scratch\", \"eval_data\": \"/root/trace-verdict-study/data/test.jsonl\", \"wall_clock_seconds\": 4665.6, \"gpu_hours\": 1.3}, \"reproduce\": {\"finished_at\": \"2026-05-17T22:29:55.961Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T22:29:58.909048+00:00\"}]}, \"metrics\": {\"accuracy\": 0.939, \"accuracy_ci_lower\": 0.926, \"accuracy_ci_upper\": 0.953, \"majority_baseline\": 0.715, \"lift_over_majority\": 0.224, \"pass_precision\": 0.97, \"pass_recall\": 0.94, \"pass_f1\": 0.96, \"fail_precision\": 0.86, \"fail_recall\": 0.94, \"fail_f1\": 0.9, \"n_test\": 1190}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_full_trace_tail512_seed42/final\", \"log_path\": \"/root/trace-verdict-study/logs/deepseek_tail512_seed42.log\", \"completed_at\": \"2026-05-17T22:32:35.246Z\"}, \"qwen15b_full_trace_tail512_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T20:58:30.671Z\", \"updated_at\": \"2026-05-17T21:20:53.258Z\", \"hypothesis\": \"Qwen-1.5B with tail-512 truncation should achieve 88-94% accuracy, comparable to Qwen-7B tail-512 (93.61%), indicating the phase transition threshold between 256-512 tokens is scale-invariant across model sizes\", \"parent\": \"qwen15b_full_trace_tail256_seed42\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_tail512_seed42/final\", \"log_path\": \"/root/trace-verdict-study/logs/qwen15b_tail512_seed42.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-17T21:18:34.835Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T21:18:38.541236+00:00\"}]}, \"metrics\": {\"accuracy\": 0.956, \"accuracy_ci_lower\": 0.945, \"accuracy_ci_upper\": 0.968, \"majority_baseline\": 0.715, \"lift_over_majority\": 0.241, \"eval_loss\": 0.263, \"train_loss\": 0.154, \"pass_precision\": 0.98, \"pass_recall\": 0.96, \"pass_f1\": 0.97, \"fail_precision\": 0.91, \"fail_recall\": 0.94, \"fail_f1\": 0.92, \"eval_mean_token_accuracy\": 0.949}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T21:20:53.258Z\"}, \"deepseek_full_trace_tail256_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T20:34:26.838Z\", \"updated_at\": \"2026-05-17T21:10:51.276Z\", \"hypothesis\": \"DeepSeek tail-256 应在 75-82% 范围（与 Qwen-7B tail-256=78.9% 类似），确认 256-512 phase transition 是 architecture-independent\", \"parent\": \"full_trace_tail256_seed42\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python train.py --model /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct --condition full_trace --truncation tail --max_tokens 256 --seed 42'\", \"server\": \"westd-11235\", \"gpu\": \"cuda:0\", \"pid\": \"379548\", \"log_path\": \"~/runs/trace-verdict-study/deepseek_full_trace_tail256_seed42.log\", \"submitted_at\": \"2026-05-17T20:38:11.778Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/trace-verdict-study/data/\", \"data_count\": 600, \"model_name\": \"deepseek-coder-6.7b-instruct\", \"seed\": 42, \"checkpoint_source\": \"trained_from_scratch\", \"eval_data\": \"/root/trace-verdict-study/data/test.jsonl\", \"wall_clock_seconds\": 1959.5, \"gpu_hours\": 0.54}, \"reproduce\": {\"finished_at\": \"2026-05-17T21:07:49.509Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T21:07:52.391149+00:00\"}]}, \"metrics\": {\"accuracy\": 0.7639, \"accuracy_ci_lower\": 0.7403, \"accuracy_ci_upper\": 0.7874, \"pass_precision\": 0.8058, \"pass_recall\": 0.8825, \"pass_f1\": 0.8424, \"fail_precision\": 0.6124, \"fail_recall\": 0.4661, \"fail_f1\": 0.5293, \"majority_baseline\": 0.7151, \"lift\": 0.0487, \"eval_loss\": 0.5117, \"train_loss\": 0.2367}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_full_trace_tail256_seed42/final\", \"log_path\": \"/root/trace-verdict-study/logs/deepseek_tail256_seed42.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T21:10:51.276Z\"}, \"qwen15b_full_trace_tail256_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T20:27:09.863Z\", \"updated_at\": \"2026-05-17T20:55:21.799Z\", \"hypothesis\": \"Cross-scale tail-256: Qwen-1.5B tail-256 should show similar accuracy to 7B tail-256 (78.9%), confirming the 256-512 phase transition is signal-limited not capacity-limited\", \"parent\": \"full_trace_tail256_seed42\", \"spec\": {\"command\": \"python train.py --model Qwen2.5-Coder-1.5B-Instruct --condition full_trace --truncation tail --max_tokens 256 --seed 42\", \"server\": \"westd-11235\", \"data_path\": \"/root/trace-verdict-study/data/\", \"data_count\": 600, \"model_name\": \"Qwen2.5-Coder-1.5B-Instruct\", \"seed\": 42, \"gpu\": \"cuda:1\", \"checkpoint_source\": \"trained_from_scratch\", \"eval_data\": \"/root/trace-verdict-study/data/test.jsonl\"}, \"reproduce\": {\"finished_at\": \"2026-05-17T20:42:23.364Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-17T20:42:24.637Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-17T20:42:27.231757+00:00\"}]}, \"metrics\": {\"accuracy\": 0.726, \"accuracy_ci_lower\": 0.7, \"accuracy_ci_upper\": 0.753, \"majority_baseline\": 0.715, \"lift_over_majority\": 0.011, \"lift_ci_lower\": -0.021, \"lift_ci_upper\": 0.044, \"pass_precision\": 0.82, \"pass_recall\": 0.79, \"pass_f1\": 0.8, \"fail_precision\": 0.52, \"fail_recall\": 0.57, \"fail_f1\": 0.54, \"eval_loss\": 0.5936, \"train_loss\": 0.2687}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_tail256_seed42/final\", \"log_path\": \"/root/trace-verdict-study/logs/qwen15b_tail256_seed42.log\"}, \"deepseek_full_trace_head2048_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T17:56:22.154Z\", \"updated_at\": \"2026-05-17T20:31:41.861Z\", \"hypothesis\": \"Cross-architecture head-truncation: DeepSeek head-2048 should achieve 80-85% (similar to Qwen-7B 81.76%), and tail-2048 (94.96%) vs head-2048 gap should be >=10pp, confirming signal positional concentration is architecture-independent\", \"parent\": \"deepseek_full_trace_tail2048_seed42\", \"spec\": {\"command\": \"python train.py --model deepseek-coder-6.7b-instruct --condition full_trace --truncation head --max_tokens 2048 --seed 42\", \"server\": \"westd-11235\", \"data_path\": \"/root/trace-verdict-study/data/\", \"data_count\": 600, \"model_name\": \"deepseek-coder-6.7b-instruct\", \"seed\": 42, \"gpu\": \"cuda:0\", \"checkpoint_source\": \"trained_from_scratch\", \"eval_data\": \"/root/trace-verdict-study/data/test.jsonl\"}, \"metrics\": {\"accuracy\": 0.787, \"accuracy_ci_lower\": 0.765, \"accuracy_ci_upper\": 0.81, \"majority_baseline\": 0.715, \"lift_pp\": 7.2, \"pass_precision\": 0.84, \"pass_recall\": 0.86, \"pass_f1\": 0.85, \"fail_precision\": 0.63, \"fail_recall\": 0.6, \"fail_f1\": 0.62}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_full_trace_head2048_seed42/\", \"log_path\": \"/root/trace-verdict-study/logs/deepseek_head2048_seed42.log\", \"completed_at\": \"2026-05-17T20:31:41.861Z\"}, \"full_trace_tail256_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T19:29:18.715Z\", \"updated_at\": \"2026-05-17T20:26:35.350Z\", \"hypothesis\": \"Tail-256 truncation (keeping last 256 tokens of execution trace) still provides sufficient signal for verdict prediction, extending the budget curve below tail-512 (93.61%) to validate the accuracy-budget tradeoff at minimal trace length.\", \"parent\": \"full_trace_tail_512_seed42\", \"spec\": {\"command\": \"python train/train_sft.py --condition full_trace_tail_256 --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_tail256_seed42 && python eval/evaluate.py --condition full_trace_tail_256 --checkpoint_dir .../final --gpu 0 --save_predictions\", \"server\": \"westd-11235\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/full_trace_tail_256_{train,test}.jsonl\", \"data_count\": 5910, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_tail256_seed42/\", \"log_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_tail256_seed42.log\", \"checkpoint_source\": \"self-trained\", \"eval_data\": \"/root/autodl-tmp/trace-verdict-study-data/full_trace_tail_256_test.jsonl\"}, \"metrics\": {\"accuracy\": 0.789, \"accuracy_ci_lower\": 0.765, \"accuracy_ci_upper\": 0.813, \"pass_f1\": 0.845, \"fail_f1\": 0.671, \"n_test\": 1190}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-17T20:26:35.350Z\"}, \"qwen15b_full_trace_head2048_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T17:56:23.519Z\", \"updated_at\": \"2026-05-17T19:27:55.067Z\", \"hypothesis\": \"Cross-scale head-truncation: Qwen-1.5B head-2048 should achieve 75-82%, and tail-2048 (97.90%) vs head-2048 gap should be >=15pp, confirming signal positional concentration holds at small scale\", \"parent\": \"qwen15b_full_trace_tail2048_seed42\", \"metrics\": {\"accuracy\": 0.7529, \"accuracy_ci_lower\": 0.7286, \"accuracy_ci_upper\": 0.7782, \"pass_precision\": 0.799, \"pass_recall\": 0.874, \"pass_f1\": 0.835, \"fail_precision\": 0.587, \"fail_recall\": 0.448, \"fail_f1\": 0.508, \"n_test\": 1190}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_head2048_seed42/final/\", \"log_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_head2048_seed42/final/eval_results.json\", \"spec\": {\"command\": \"python train/train_sft.py --condition full_trace_head --model_path Qwen2.5-Coder-1.5B-Instruct + eval\", \"server\": \"westd-11235\", \"data_path\": \"/root/trace-verdict-study/data/full_trace_head_train.jsonl\", \"data_count\": 4720, \"model_name\": \"Qwen2.5-Coder-1.5B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"self-trained SFT on full_trace_head data\", \"eval_data\": \"/root/trace-verdict-study/data/full_trace_head_test.jsonl\"}, \"completed_at\": \"2026-05-17T19:27:55.067Z\"}, \"deepseek_full_trace_tail2048_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T14:52:23.728Z\", \"updated_at\": \"2026-05-17T17:18:48.327Z\", \"hypothesis\": \"Tail-truncation signal concentration hypothesis generalizes across architectures: DeepSeek-Coder-6.7B with tail-2048 truncation should achieve accuracy comparable to Qwen-7B tail-2048 (97.31%), because execution trace endings contain the most verdict-relevant signals regardless of model architecture.\", \"parent\": \"full_trace_tail_seed42\", \"spec\": {\"command\": \"/root/miniconda3/bin/python train/train_sft.py --condition full_trace_tail --model_path ... --gradient_checkpointing --gpu 0 --seed 42 --output_dir ... && /root/miniconda3/bin/python eval/evaluate.py --condition full_trace_tail --checkpoint_dir .../final --gpu 0 --save_predictions\", \"server\": \"westd-11235\", \"gpu\": \"cuda:0\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/full_trace_tail_{train,test}.jsonl\", \"data_count\": 4720, \"model_name\": \"DeepSeek-Coder-6.7B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_full_trace_tail2048_seed42/final\", \"log_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_full_trace_tail2048_seed42/train_eval.log\", \"checkpoint_source\": \"self-trained SFT on full_trace_tail data\", \"eval_data\": \"/root/autodl-tmp/trace-verdict-study-data/full_trace_tail_test.jsonl (1190 samples)\"}, \"metrics\": {\"accuracy\": 0.9496, \"accuracy_ci_lower\": 0.937, \"accuracy_ci_upper\": 0.9622, \"pass_precision\": 0.9692, \"pass_recall\": 0.96, \"pass_f1\": 0.9646, \"fail_precision\": 0.902, \"fail_recall\": 0.9233, \"fail_f1\": 0.9125, \"n_test\": 1190}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_full_trace_tail2048_seed42/final/\", \"completed_at\": \"2026-05-17T17:18:48.327Z\"}, \"qwen15b_full_trace_tail2048_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T14:52:25.576Z\", \"updated_at\": \"2026-05-17T17:18:47.435Z\", \"hypothesis\": \"Tail-truncation concentrates diagnostic signal (final execution states, exceptions) at training time. If this hypothesis holds, Qwen2.5-Coder-1.5B with tail-2048 truncation should achieve accuracy comparable to 7B tail-2048 (97.31%), significantly outperforming head-truncation baselines on the same model size.\", \"parent\": \"full_trace_tail_seed42\", \"spec\": {\"command\": \"python train/train_sft.py --condition full_trace_tail --model_path /root/trace-verdict-study/models/Qwen2.5-Coder-1.5B-Instruct --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_tail2048_seed42 --gradient_checkpointing --wandb_project trace-verdict-study --wandb_run_name qwen15b_full_trace_tail2048_seed42 && python eval/evaluate.py --condition full_trace_tail --model_path /root/trace-verdict-study/models/Qwen2.5-Coder-1.5B-Instruct --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_tail2048_seed42/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_tail2048_seed42/final/eval_results.json --save_predictions\", \"server\": \"westd-11235\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/full_trace_tail_train.jsonl\", \"data_count\": 4720, \"model_name\": \"Qwen2.5-Coder-1.5B-Instruct\", \"seed\": 42, \"gpu\": \"cuda:1\", \"checkpoint_source\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_tail2048_seed42/final\", \"eval_data\": \"/root/autodl-tmp/trace-verdict-study-data/full_trace_tail_test.jsonl\"}, \"metrics\": {\"accuracy\": 0.979, \"accuracy_ci_lower\": 0.9706, \"accuracy_ci_upper\": 0.9874, \"pass_precision\": 0.9758, \"pass_recall\": 0.9953, \"pass_f1\": 0.9855, \"fail_precision\": 0.9876, \"fail_recall\": 0.9381, \"fail_f1\": 0.9622, \"n_test\": 1190}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_tail2048_seed42/final/\", \"log_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_tail2048_seed42.log\", \"completed_at\": \"2026-05-17T17:18:47.435Z\"}, \"fewshot_qwen7b_exception_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T14:05:16.779Z\", \"updated_at\": \"2026-05-17T14:16:13.380Z\", \"hypothesis\": \"Few-shot (3 examples) improves over zero-shot (89.08%) but remains far below SFT (99.83%) because 3 in-context examples cannot cover all caught exception patterns, establishing the zero-shot → few-shot → SFT progression\", \"parent\": \"zeroshot_qwen7b_exception_only\", \"metrics\": {\"accuracy\": 0.9084, \"accuracy_ci_lower\": 0.8908, \"accuracy_ci_upper\": 0.9244, \"pass_precision\": 0.9245, \"pass_recall\": 0.9495, \"pass_f1\": 0.9368, \"fail_precision\": 0.8639, \"fail_recall\": 0.8053, \"fail_f1\": 0.8336, \"n_test\": 1190, \"n_unknown\": 0}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/fewshot_qwen7b_exception_only/\", \"log_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/fewshot_qwen7b_exception_only/eval_results.json\", \"spec\": {\"command\": \"python eval/fewshot_eval.py --model_path Qwen2.5-Coder-7B-Instruct --n_examples 3 --batch_size 2\", \"server\": \"westd-11235\", \"data_path\": \"/root/trace-verdict-study/data/exception_only_test.jsonl\", \"data_count\": 1190, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 0, \"checkpoint_source\": \"pretrained (no fine-tuning)\", \"eval_data\": \"/root/trace-verdict-study/data/exception_only_test.jsonl\"}, \"completed_at\": \"2026-05-17T14:16:13.380Z\"}, \"zeroshot_qwen15b_exception_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T14:05:17.683Z\", \"updated_at\": \"2026-05-17T14:13:44.604Z\", \"hypothesis\": \"Zero-shot cross-scale baseline: Qwen-1.5B zero-shot may perform poorly (similar to CodeLlama-13B) due to limited capacity, but SFT normalizes it to 99.83%, demonstrating SFT eliminates scale variance\", \"parent\": \"zeroshot_qwen7b_exception_only\", \"metrics\": {\"accuracy\": 0.9345, \"accuracy_ci_lower\": 0.9202, \"accuracy_ci_upper\": 0.9479, \"pass_f1\": 0.969, \"fail_f1\": 0.873, \"pass_recall\": 0.9906, \"fail_recall\": 0.7935, \"n_test\": 1190, \"n_unknown\": 24}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/zeroshot_qwen15b_exception_only/\", \"log_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/zeroshot_qwen15b_exception_only/eval_results.json\", \"spec\": {\"command\": \"python eval/zeroshot_eval.py --model_path Qwen2.5-Coder-1.5B-Instruct --data_path exception_only_test.jsonl --gpu 0\", \"server\": \"westd-11235\", \"data_path\": \"/root/trace-verdict-study/data/exception_only_test.jsonl\", \"data_count\": 1190, \"model_name\": \"Qwen2.5-Coder-1.5B-Instruct\", \"seed\": 0, \"checkpoint_source\": \"pretrained (no fine-tuning)\", \"eval_data\": \"/root/trace-verdict-study/data/exception_only_test.jsonl\"}, \"completed_at\": \"2026-05-17T14:13:44.604Z\"}, \"zeroshot_codellama13b_exception_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T13:49:28.046Z\", \"updated_at\": \"2026-05-17T14:03:43.831Z\", \"hypothesis\": \"Zero-shot cross-scale baseline: untuned CodeLlama-13B-Instruct (largest model tested) still cannot match SFT accuracy on exception_only verdict prediction, confirming SFT necessity holds even with 2x more parameters\", \"parent\": \"zeroshot_qwen7b_exception_only\", \"metrics\": {\"accuracy\": 0.5101, \"accuracy_ci_lower\": 0.4824, \"accuracy_ci_upper\": 0.5395, \"pass_precision\": 1, \"pass_recall\": 0.3502, \"pass_f1\": 0.5187, \"fail_precision\": 0.3585, \"fail_recall\": 0.9115, \"fail_f1\": 0.5146, \"n_test\": 1190, \"n_unknown\": 30}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/zeroshot_codellama13b_exception_only/\", \"log_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/zeroshot_codellama13b_exception_only/eval_results.json\", \"spec\": {\"command\": \"python eval/zeroshot_eval.py --model_path CodeLlama-13b-Instruct-hf --data_path exception_only_test.jsonl --gpu 0\", \"server\": \"westd-11235\", \"data_path\": \"/root/trace-verdict-study/data/exception_only_test.jsonl\", \"data_count\": 1190, \"model_name\": \"CodeLlama-13B-Instruct\", \"seed\": 0, \"checkpoint_source\": \"pretrained (no fine-tuning)\", \"eval_data\": \"/root/trace-verdict-study/data/exception_only_test.jsonl\"}, \"completed_at\": \"2026-05-17T14:03:43.831Z\"}, \"zeroshot_deepseek7b_exception_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T13:00:43.420Z\", \"updated_at\": \"2026-05-17T13:47:37.166Z\", \"hypothesis\": \"Zero-shot cross-model baseline: untuned DeepSeek-Coder-6.7B-Instruct similarly cannot reach SFT-level accuracy on exception_only verdict prediction, confirming SFT necessity is architecture-independent\", \"metrics\": {\"accuracy\": 0.9059, \"accuracy_ci_lower\": 0.8899, \"accuracy_ci_upper\": 0.9218, \"pass_precision\": 0.9743, \"pass_recall\": 0.8919, \"pass_f1\": 0.9313, \"fail_precision\": 0.7762, \"fail_recall\": 0.941, \"fail_f1\": 0.8507, \"n_test\": 1190, \"n_unknown\": 0}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/zeroshot_deepseek7b_exception_only/\", \"log_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/zeroshot_deepseek7b_exception_only/eval_results.json\", \"spec\": {\"command\": \"python eval/zeroshot_eval.py --model_path DeepSeek-Coder-6.7B-Instruct --data_path exception_only_test.jsonl --gpu 0 (logit-based)\", \"server\": \"westd-11235\", \"data_path\": \"/root/trace-verdict-study/data/exception_only_test.jsonl\", \"data_count\": 1190, \"model_name\": \"DeepSeek-Coder-6.7B-Instruct\", \"seed\": 0}, \"completed_at\": \"2026-05-17T13:47:37.166Z\"}, \"zeroshot_qwen7b_exception_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T13:00:40.251Z\", \"updated_at\": \"2026-05-17T13:47:19.462Z\", \"hypothesis\": \"Zero-shot prompting baseline: untuned Qwen2.5-7B-Instruct cannot match SFT accuracy (99.83%) on exception_only verdict prediction because distinguishing caught vs uncaught exceptions requires task-specific training signal, not just language understanding\", \"metrics\": {\"accuracy\": 0.8908, \"accuracy_ci_lower\": 0.8731, \"accuracy_ci_upper\": 0.9076, \"pass_precision\": 0.8815, \"pass_recall\": 0.9788, \"pass_f1\": 0.9276, \"fail_precision\": 0.9265, \"fail_recall\": 0.6696, \"fail_f1\": 0.7774, \"n_test\": 1190, \"n_unknown\": 0}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/zeroshot_qwen7b_exception_only/\", \"log_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/zeroshot_qwen7b_exception_only/eval_results_mapped.json\", \"spec\": {\"command\": \"python eval/zeroshot_eval.py --model_path Qwen2.5-Coder-7B-Instruct --data_path exception_only_test.jsonl --gpu 0\", \"server\": \"westd-11235\", \"data_path\": \"/root/trace-verdict-study/data/exception_only_test.jsonl\", \"data_count\": 1190, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 0}, \"completed_at\": \"2026-05-17T13:47:19.462Z\"}, \"codellama13b_exception_only_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:47:18.896Z\", \"updated_at\": \"2026-05-17T13:06:57.551Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition exception_only --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_exception_only_seed42 --wandb_project trace-verdict-study --wandb_run_name codellama13b_exception_only_seed42 && python eval/evaluate.py --condition exception_only --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_exception_only_seed42/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_exception_only_seed42/final/eval_results.json --save_predictions\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"pid\": \"271776\", \"log_path\": \"~/runs/trace-verdict-study/codellama13b_exception_only_seed42.log\", \"submitted_at\": \"2026-05-16T12:03:38.585Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 9885.3, \"gpu_hours\": 2.75}, \"server\": \"westd-11235\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"pid\": \"271776\", \"log_path\": \"~/runs/trace-verdict-study/codellama13b_exception_only_seed42.log\", \"wandb_run_id\": \"codellama13b_exception_only_seed42\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition exception_only --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_exception_only_seed42 --wandb_project trace-verdict-study --wandb_run_name codellama13b_exception_only_seed42 && python eval/evaluate.py --condition exception_only --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_exception_only_seed42/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_exception_only_seed42/final/eval_results.json --save_predictions\\\"\", \"wandb_run_id\": \"codellama13b_exception_only_seed42\", \"code_commit\": \"e404237ccc765768e267d4d6fd3c89549dcf41a4\", \"finished_at\": \"2026-05-16T14:45:17.342Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T14:45:19.404390+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_exception_only_seed42/final/\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.9983, \"accuracy_ci_lower\": 0.9958, \"accuracy_ci_upper\": 1, \"pass_f1\": 0.9988, \"fail_f1\": 0.9971, \"n_test\": 1190}, \"completed_at\": \"2026-05-16T14:48:23.848Z\", \"hypothesis\": \"Cross-architecture validation: exception_only signal sufficiency (99.83% on Qwen-7B) generalizes to CodeLlama-13B because diagnostic content (exception type + location) is architecture-agnostic\", \"parent\": \"vota_exception_only_seed42_v2\"}, \"full_trace_tail_1024_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T08:13:21.880Z\", \"updated_at\": \"2026-05-17T10:30:11.408Z\", \"hypothesis\": \"Tail-1024 token budget: tests diminishing returns of tail context. If tail-1024 approaches tail-2048 (97.3%), 1024 tokens already captures nearly all diagnostic signal; the extra 1024 tokens add marginal value\", \"parent\": \"full_trace_tail_seed42\", \"spec\": {\"command\": \"python train/train_sft.py --condition full_trace_tail_1024 --truncation_side left --gradient_checkpointing --gpu 0 --seed 42 + eval\", \"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"pid\": 340169, \"log_path\": \"~/runs/trace-verdict-study/full_trace_tail_1024_seed42.log\", \"submitted_at\": \"2026-05-17T08:20:01.416Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/full_trace_tail_1024_{train,test}.jsonl\", \"data_count\": {\"train\": 4720, \"test\": 1190}, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_tail_1024_seed42\", \"checkpoint_source\": \"self-trained\", \"eval_data\": \"full_trace_tail_1024_test.jsonl\", \"tmux_session\": \"full_trace_tail_1024_seed42\", \"wall_clock_seconds\": 7810.0, \"gpu_hours\": 2.17}, \"metrics\": {\"accuracy\": 0.9647, \"accuracy_ci\": [0.9546, 0.9748], \"majority_baseline\": 0.7151, \"lift\": 0.2496, \"n\": 1190, \"pass_f1\": 0.9753, \"fail_f1\": 0.9381}, \"conclusion\": \"success\", \"log_path\": \"~/runs/trace-verdict-study/full_trace_tail_1024_seed42.log\", \"completed_at\": \"2026-05-17T10:30:11.408Z\"}, \"full_trace_tail_256_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T08:13:21.000Z\", \"updated_at\": \"2026-05-17T10:30:10.501Z\", \"hypothesis\": \"Tail-256 token budget: tests if diagnostic signal is concentrated in the last 256 tokens. If tail-256 approaches tail-512 (93.6%), signal is extremely localized at trace end; if much lower, exception events need surrounding context for effective learning\", \"parent\": \"full_trace_tail_512_seed42\", \"spec\": {\"command\": \"python train/train_sft.py --condition full_trace_tail_256 --truncation_side left --gradient_checkpointing --gpu 0 --seed 42 + eval/evaluate.py\", \"server\": \"westd-11235\", \"gpu\": \"cuda:0\", \"pid\": 339962, \"log_path\": \"~/runs/trace-verdict-study/full_trace_tail_256_seed42.log\", \"submitted_at\": \"2026-05-17T08:19:49.240Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/full_trace_tail_256_{train,test}.jsonl\", \"data_count\": {\"train\": 4720, \"test\": 1190}, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_tail_256_seed42\", \"truncation\": \"tail-256 (keep last 256 tokens of trace)\", \"checkpoint_source\": \"self-trained\", \"eval_data\": \"/root/autodl-tmp/trace-verdict-study-data/full_trace_tail_256_test.jsonl\", \"wall_clock_seconds\": 7821.3, \"gpu_hours\": 2.17}, \"metrics\": {\"accuracy\": 0.7748, \"accuracy_ci\": [0.7496, 0.7975], \"majority_baseline\": 0.7151, \"lift\": 0.0597, \"n\": 1190, \"pass_f1\": 0.8333, \"fail_f1\": 0.6528}, \"conclusion\": \"negative\", \"log_path\": \"~/runs/trace-verdict-study/full_trace_tail_256_seed42.log\", \"completed_at\": \"2026-05-17T10:30:10.501Z\"}, \"full_trace_tail_512_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T04:55:57.365Z\", \"updated_at\": \"2026-05-17T07:36:14.051Z\", \"hypothesis\": \"Tail-truncation token budget: if tail-2048 >> head-2048, tail-512 reveals how concentrated the signal is. tail-512 ≈ tail-2048 means signal is in last ~500 tokens; tail-512 << tail-2048 means more context needed beyond immediate exception event\", \"parent\": \"full_trace_tail_seed42\", \"spec\": {\"command\": \"python train/train_sft.py --condition full_trace_tail_512 --truncation_side left --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_tail_512_seed42 && python eval/evaluate.py --condition full_trace_tail_512 --checkpoint_dir .../final --gpu 0 --save_predictions\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"pid\": \"330357\", \"model_name\": \"Qwen/Qwen2.5-Coder-7B-Instruct\", \"seed\": 42, \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/full_trace_tail_512_{train,test}.jsonl\", \"data_count\": 5910, \"submitted_at\": \"2026-05-17T05:03:00Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 9194.1, \"gpu_hours\": 2.55}, \"metrics\": {\"accuracy\": 0.936, \"accuracy_ci\": [0.922, 0.95], \"majority_baseline\": 0.7151, \"lift\": 0.221, \"n\": 1190, \"pass_precision\": 0.98, \"pass_recall\": 0.93, \"pass_f1\": 0.95, \"fail_precision\": 0.85, \"fail_recall\": 0.94, \"fail_f1\": 0.89}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_tail_512_seed42/final\", \"log_path\": \"~/runs/trace-verdict-study/full_trace_tail_512_seed42.log\", \"completed_at\": \"2026-05-17T07:36:14.051Z\"}, \"full_trace_tail_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T04:08:51.116Z\", \"updated_at\": \"2026-05-17T07:36:13.099Z\", \"hypothesis\": \"Tail-truncation baseline: keeping the last 2048 tokens of full trace (where exception events concentrate) should significantly outperform head-truncation (81.76%) and approach exception_only (99.83%), validating that diagnostic signal is positionally concentrated at trace end\", \"parent\": \"full_trace_1024tok_seed42\", \"spec\": {\"command\": \"python train/train_sft.py --condition full_trace_tail --truncation_side left --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_tail_seed42 && python eval/evaluate.py --condition full_trace_tail --checkpoint_dir .../final --gpu 0 --save_predictions\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"327379\", \"model_name\": \"Qwen/Qwen2.5-Coder-7B-Instruct\", \"seed\": 42, \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/full_trace_tail_{train,test}.jsonl\", \"data_count\": 5910, \"submitted_at\": \"2026-05-17T04:22:00Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 11653.1, \"gpu_hours\": 3.24}, \"metrics\": {\"accuracy\": 0.973, \"accuracy_ci\": [0.964, 0.982], \"majority_baseline\": 0.7151, \"lift\": 0.258, \"n\": 1190, \"pass_precision\": 0.98, \"pass_recall\": 0.99, \"pass_f1\": 0.98, \"fail_precision\": 0.97, \"fail_recall\": 0.94, \"fail_f1\": 0.95}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_tail_seed42/final\", \"log_path\": \"~/runs/trace-verdict-study/full_trace_tail_seed42.log\", \"completed_at\": \"2026-05-17T07:36:13.099Z\"}, \"codellama13b_nomarker_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T02:09:08.956Z\", \"updated_at\": \"2026-05-17T03:23:43.036Z\", \"hypothesis\": \"Cross-architecture marker contribution: format markers ([No exception data in trace], [ERROR] prefix) contribute ~2pp on CodeLlama-13B as on Qwen family, confirming marker contribution is architecture-independent\", \"spec\": {\"command\": \"python train/train_sft.py --condition exception_only_nomarker --model_path /root/trace-verdict-study/models/CodeLlama-13b-Instruct-hf --gradient_checkpointing --gpu 0 --seed 42\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"pid\": \"322984\", \"log_path\": \"~/runs/trace-verdict-study/codellama13b_nomarker_seed42.log\", \"submitted_at\": \"2026-05-17T03:04:06.715Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"CodeLlama-13b-Instruct-hf\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/exception_only_nomarker_train.jsonl\", \"data_count\": 4720, \"seed\": 42, \"wall_clock_seconds\": 1176.3, \"gpu_hours\": 0.33}, \"notes\": \"Cancelled by Director: model weights cleaned from disk, not worth re-downloading 26GB for speculative experiment. Worker re-submitted (PID 322984) before cancel order received — process killed. 论文 scope 已限定，Round 6 审稿人要求时再跑。\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-17T03:23:43.036Z\"}, \"eval_missing_predictions_batch_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:41:02.286Z\", \"updated_at\": \"2026-05-17T02:58:57.381Z\", \"spec\": {\"command\": \"bash run_missing_predictions.sh 1\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"221213\", \"log_path\": \"~/runs/trace-verdict-study/eval_missing_predictions_batch_v2.log\", \"submitted_at\": \"2026-05-16T01:41:02.047Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"deepseek_full_trace_v3 + debugbench_vota predictions\", \"data_count\": 1616, \"model_name\": \"DeepSeek-Coder-6.7B + Qwen-2.5-Coder-7B\", \"seed\": 42, \"wall_clock_seconds\": 1905.5, \"gpu_hours\": 0.53}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (eval-only batch)\", \"completed_at\": \"2026-05-16T02:12:47.505Z\", \"hypothesis\": \"Utility: second batch re-evaluation pass for remaining checkpoints without predictions.jsonl, ensuring all DONE experiments have comparable evaluation outputs\"}, \"eval_missing_predictions_batch\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:33:51.923Z\", \"updated_at\": \"2026-05-17T02:58:56.080Z\", \"spec\": {\"command\": \"python eval/evaluate.py --save_predictions\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"219832\", \"log_path\": \"~/runs/trace-verdict-study/eval_missing_predictions_batch.log\", \"submitted_at\": \"2026-05-16T01:33:51.795Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/\", \"data_count\": 1616, \"model_name\": \"DeepSeek-Coder-6.7B + Qwen2.5-Coder-7B\", \"seed\": 42, \"wall_clock_seconds\": 1480.2, \"gpu_hours\": 0.41}, \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"/tmp/deepseek_eval_preds.log, /tmp/debugbench_vota_eval_preds.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T01:58:31.993Z\", \"notes\": \"predictions.jsonl generated for both experiments. deepseek_full_trace_seed42_v3: 1190 lines, accuracy=28.5% (NOT 79.16% as expected — model predicts all fail, same result with max_length=16384). debugbench_vota_seed42: 426 lines, accuracy=99.77% (matches registry). Paths: /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_full_trace_seed42_v3/final/predictions.jsonl, /root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_vota/final/predictions.jsonl\", \"hypothesis\": \"Utility: batch re-evaluation of checkpoints missing predictions.jsonl to complete provenance records and enable systematic cross-experiment comparison\"}, \"full_trace_1024tok_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:27:17.607Z\", \"updated_at\": \"2026-05-17T02:58:46.678Z\", \"spec\": {\"hypothesis\": \"plan_006: trace length ablation - 1024 tokens. Tests if medium-length trace preserves enough signal to match or exceed untruncated full_trace (81.8%).\", \"model_name\": \"Qwen/Qwen2.5-Coder-7B-Instruct\", \"seed\": 42, \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/full_trace_{train,test}.jsonl\", \"data_count\": 4720, \"max_trace_tokens\": 1024, \"plan_id\": \"plan_006\", \"command\": \"train_sft.py --condition full_trace --max_trace_tokens 1024 + evaluate.py\", \"server\": \"westd-11235\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_1024tok\", \"log_path\": \"~/runs/trace-verdict-study/full_trace_1024tok_seed42.log\"}, \"server\": \"westd-11235\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-11235\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-16T00:15:42.746Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition full_trace --max_trace_tokens 1024 --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_1024tok --wandb_project trace-verdict-study --wandb_run_name full_trace_1024tok_seed42 && python eval/evaluate.py --condition full_trace --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_1024tok/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_1024tok/final/eval_results.json\\\"\", \"wandb_run_id\": \"full_trace_1024tok_seed42\", \"code_commit\": \"e404237ccc765768e267d4d6fd3c89549dcf41a4\", \"finished_at\": \"2026-05-16T01:54:26.200Z\", \"training_hours\": 1.65}, \"pid\": \"212643\", \"log_path\": \"~/runs/trace-verdict-study/full_trace_1024tok_seed42.log\", \"wandb_run_id\": \"full_trace_1024tok_seed42\", \"gpu_id\": \"cuda:0\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T01:54:27.781595+00:00\"}]}, \"metrics\": {\"accuracy\": 0.7723, \"majority_baseline\": 0.7151, \"lift\": 0.0571, \"n\": 1190, \"accuracy_ci\": [0.7487, 0.7958], \"pass_precision\": 0.9006, \"pass_recall\": 0.7662, \"pass_f1\": 0.8279, \"fail_precision\": 0.573, \"fail_recall\": 0.7876, \"fail_f1\": 0.6634, \"train_loss\": 0.0634, \"train_runtime_sec\": 5553, \"epochs\": 3}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-16T01:56:53.352Z\", \"hypothesis\": \"Token budget ablation (1024 tokens): near-full trace budget should approach no-limit accuracy (~81.76%), testing whether the last few hundred tokens contain marginal diagnostic value\", \"parent\": \"full_trace_seed42_v5\"}, \"full_trace_512tok_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:27:16.130Z\", \"updated_at\": \"2026-05-17T02:58:46.025Z\", \"spec\": {\"hypothesis\": \"plan_006: trace length ablation - 512 tokens. Tests accuracy with moderate trace length.\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/full_trace_{train,test}.jsonl\", \"data_count\": 4720, \"model_name\": \"Qwen/Qwen2.5-Coder-7B-Instruct\", \"seed\": 42, \"max_trace_tokens\": 512, \"plan_id\": \"plan_006\", \"command\": \"train_sft.py --condition full_trace --max_trace_tokens 512 --gradient_checkpointing --gpu 0 --seed 42 + evaluate.py\", \"server\": \"westd-11235\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_512tok/final\", \"log_path\": \"~/runs/trace-verdict-study/full_trace_512tok_seed42.log\"}, \"reproduce\": {\"pid\": 197608, \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-15T23:16:13Z\", \"wandb_run_name\": \"full_trace_512tok_seed42\", \"code_commit\": \"e404237ccc765768e267d4d6fd3c89549dcf41a4\"}, \"metrics\": {\"accuracy\": 0.8042, \"majority_baseline\": 0.7151, \"lift\": 0.0891, \"pass_precision\": 0.8705, \"pass_recall\": 0.8531, \"pass_f1\": 0.8617, \"fail_precision\": 0.6489, \"fail_recall\": 0.6814, \"fail_f1\": 0.6647, \"n\": 1190, \"accuracy_ci\": [0.7815, 0.8261]}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-16T00:14:32.967Z\", \"hypothesis\": \"Token budget ablation (512 tokens): moderate truncation retains some diagnostic events but still loses critical tail information, yielding accuracy between 256-tok and full (no-limit) conditions\", \"parent\": \"full_trace_seed42_v5\"}, \"full_trace_256tok_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:27:14.119Z\", \"updated_at\": \"2026-05-17T02:58:45.053Z\", \"spec\": {\"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/full_trace_{train,test}.jsonl\", \"data_count\": 4720, \"model_name\": \"Qwen/Qwen2.5-Coder-7B-Instruct\", \"seed\": 42, \"max_trace_tokens\": 256}, \"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-15T23:05:57.749Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition full_trace --max_trace_tokens 256 --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_256tok --wandb_project trace-verdict-study --wandb_run_name full_trace_256tok_seed42 && python eval/evaluate.py --condition full_trace --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_256tok/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_256tok/final/eval_results.json\\\"\", \"wandb_run_id\": \"full_trace_256tok_seed42\", \"code_commit\": \"0836dd49526be55ab8571a3f716512d4ccd72312\", \"finished_at\": \"2026-05-16T00:01:15.610Z\", \"training_hours\": 0.92}, \"pid\": \"187860\", \"log_path\": \"~/runs/trace-verdict-study/full_trace_256tok_seed42.log\", \"wandb_run_id\": \"full_trace_256tok_seed42\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T00:01:17.060104+00:00\"}]}, \"metrics\": {\"accuracy\": 0.7882, \"majority_baseline\": 0.7151, \"lift\": 0.0731, \"n\": 1190, \"pass_precision\": 0.903, \"pass_recall\": 0.788, \"pass_f1\": 0.842, \"fail_precision\": 0.597, \"fail_recall\": 0.788, \"fail_f1\": 0.679, \"accuracy_ci\": [0.764, 0.81], \"train_loss\": 0.1094, \"train_runtime_sec\": 3047, \"epochs\": 3}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_256tok/final\", \"completed_at\": \"2026-05-16T00:03:55.505Z\", \"hypothesis\": \"Token budget ablation (256 tokens): severely truncated full trace loses most diagnostic events, yielding accuracy near no-trace baseline because critical exception information is in the tail that gets cut\", \"parent\": \"full_trace_seed42_v5\"}, \"qwen15b_vota_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T09:22:02.463Z\", \"updated_at\": \"2026-05-17T02:58:44.124Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition vota --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_vota_seed42 --wandb_project trace-verdict-study --wandb_run_name qwen15b_vota_seed42 && python eval/evaluate.py --condition vota --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_vota_seed42/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_vota_seed42/final/eval_results.json --save_predictions\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"pid\": \"265006\", \"log_path\": \"~/runs/trace-verdict-study/qwen15b_vota_seed42.log\", \"submitted_at\": \"2026-05-16T10:15:27.340Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_vota_seed42/final\", \"wall_clock_seconds\": 3252.0, \"gpu_hours\": 0.9}, \"server\": \"westd-11235\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"pid\": \"265006\", \"log_path\": \"~/runs/trace-verdict-study/qwen15b_vota_seed42.log\", \"wandb_run_id\": \"qwen15b_vota_seed42\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition vota --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_vota_seed42 --wandb_project trace-verdict-study --wandb_run_name qwen15b_vota_seed42 && python eval/evaluate.py --condition vota --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_vota_seed42/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_vota_seed42/final/eval_results.json --save_predictions\\\"\", \"wandb_run_id\": \"qwen15b_vota_seed42\", \"code_commit\": \"e404237ccc765768e267d4d6fd3c89549dcf41a4\", \"finished_at\": \"2026-05-16T11:07:13.230Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T11:07:15.416174+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.9958, \"n\": 1190, \"pass_recall\": 0.9976, \"fail_recall\": 0.9912, \"pass_f1\": 0.9971, \"fail_f1\": 0.9926, \"training_time_sec\": 2922}, \"completed_at\": \"2026-05-16T11:09:39.319Z\", \"hypothesis\": \"Scale invariance: VOTA compressed trace (99.41% on 7B) maintains near-perfect accuracy at 1.5B scale because diagnostic signals are explicitly surfaced, reducing model capacity requirements\", \"parent\": \"vota_seed42_v5\"}, \"qwen15b_nomarker_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T17:29:18.046Z\", \"updated_at\": \"2026-05-17T02:58:43.172Z\", \"spec\": {\"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"account\": \"root\", \"command\": \"cd /root/trace-verdict-study && /root/miniconda3/bin/python train/train_sft.py --condition exception_only_nomarker --model_path /root/trace-verdict-study/models/Qwen2.5-Coder-1.5B-Instruct --gradient_checkpointing --gpu 0 --seed 42\", \"pid\": \"292150\", \"log_path\": \"/tmp/qwen15b_nomarker_seed42.log\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/exception_only_nomarker_train.jsonl\", \"data_count\": 4720, \"model_name\": \"Qwen2.5-Coder-1.5B-Instruct\", \"seed\": 42}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_nomarker/final/\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.978, \"n\": 1190, \"accuracy_ci\": [0.97, 0.986], \"majority_baseline\": 0.715, \"lift\": 0.263, \"pass_precision\": 0.97, \"pass_recall\": 1, \"pass_f1\": 0.98, \"fail_precision\": 1, \"fail_recall\": 0.92, \"fail_f1\": 0.96}, \"completed_at\": \"2026-05-16T17:47:36.397Z\", \"hypothesis\": \"Cross-scale nomarker validation: format marker contribution (~2pp at 7B) is consistent at 1.5B, confirming markers provide a small but architecture-and-scale-independent boost\", \"parent\": \"exception_only_nomarker_seed42\"}, \"qwen15b_no_trace_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T09:22:01.028Z\", \"updated_at\": \"2026-05-17T02:58:42.232Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition no_trace --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_no_trace_seed42 --wandb_project trace-verdict-study --wandb_run_name qwen15b_no_trace_seed42 && python eval/evaluate.py --condition no_trace --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_no_trace_seed42/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_no_trace_seed42/final/eval_results.json --save_predictions\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"pid\": \"263569\", \"log_path\": \"~/runs/trace-verdict-study/qwen15b_no_trace_seed42.log\", \"submitted_at\": \"2026-05-16T09:56:11.214Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_no_trace_seed42/final\", \"wall_clock_seconds\": 1138.8, \"gpu_hours\": 0.32}, \"server\": \"westd-11235\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"pid\": \"263569\", \"log_path\": \"~/runs/trace-verdict-study/qwen15b_no_trace_seed42.log\", \"wandb_run_id\": \"qwen15b_no_trace_seed42\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition no_trace --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_no_trace_seed42 --wandb_project trace-verdict-study --wandb_run_name qwen15b_no_trace_seed42 && python eval/evaluate.py --condition no_trace --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_no_trace_seed42/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_no_trace_seed42/final/eval_results.json --save_predictions\\\"\", \"wandb_run_id\": \"qwen15b_no_trace_seed42\", \"code_commit\": \"e404237ccc765768e267d4d6fd3c89549dcf41a4\", \"finished_at\": \"2026-05-16T10:13:02.700Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T10:13:04.620520+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.6731, \"n\": 1190, \"pass_f1\": 0.7527, \"fail_f1\": 0.518, \"lift_over_majority\": -0.042, \"training_time_sec\": 851}, \"completed_at\": \"2026-05-16T10:15:10.018Z\", \"hypothesis\": \"Scale sensitivity of no-trace: without diagnostic signal, 1.5B model performs worse than 7B (75.13%) because code-structure-only heuristics require more capacity to learn effectively\", \"parent\": \"no_trace_seed42_v5\"}, \"qwen15b_full_trace_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T09:22:03.743Z\", \"updated_at\": \"2026-05-17T02:58:41.323Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition full_trace --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_seed42 --wandb_project trace-verdict-study --wandb_run_name qwen15b_full_trace_seed42 && python eval/evaluate.py --condition full_trace --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_seed42/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_seed42/final/eval_results.json --save_predictions\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"pid\": \"267886\", \"log_path\": \"~/runs/trace-verdict-study/qwen15b_full_trace_seed42.log\", \"submitted_at\": \"2026-05-16T11:10:01.431Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 3228.4, \"gpu_hours\": 0.9}, \"server\": \"westd-11235\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"pid\": \"267886\", \"log_path\": \"~/runs/trace-verdict-study/qwen15b_full_trace_seed42.log\", \"wandb_run_id\": \"qwen15b_full_trace_seed42\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition full_trace --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_seed42 --wandb_project trace-verdict-study --wandb_run_name qwen15b_full_trace_seed42 && python eval/evaluate.py --condition full_trace --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_seed42/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_seed42/final/eval_results.json --save_predictions\\\"\", \"wandb_run_id\": \"qwen15b_full_trace_seed42\", \"code_commit\": \"e404237ccc765768e267d4d6fd3c89549dcf41a4\", \"finished_at\": \"2026-05-16T12:00:28.907Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T12:00:31.043272+00:00\"}]}, \"metrics\": {\"accuracy\": 0.7706, \"n\": 1190}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_seed42/final\", \"completed_at\": \"2026-05-16T12:03:49.820Z\", \"hypothesis\": \"Scale sensitivity of full_trace: noisy full trace (81.76% on 7B) degrades more at 1.5B because extracting signal from noise requires capacity that smaller models lack\", \"parent\": \"full_trace_seed42_v5\"}, \"qwen15b_exception_only_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T09:22:13.547Z\", \"updated_at\": \"2026-05-17T02:58:40.352Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition exception_only --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_exception_only_seed42 --wandb_project trace-verdict-study --wandb_run_name qwen15b_exception_only_seed42 && python eval/evaluate.py --condition exception_only --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_exception_only_seed42/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_exception_only_seed42/final/eval_results.json --save_predictions\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"pid\": \"261588\", \"log_path\": \"~/runs/trace-verdict-study/qwen15b_exception_only_seed42.log\", \"submitted_at\": \"2026-05-16T09:22:34.937Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_exception_only_seed42/final\", \"wall_clock_seconds\": 1990.3, \"gpu_hours\": 0.55}, \"server\": \"westd-11235\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"pid\": \"261588\", \"log_path\": \"~/runs/trace-verdict-study/qwen15b_exception_only_seed42.log\", \"wandb_run_id\": \"qwen15b_exception_only_seed42\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition exception_only --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_exception_only_seed42 --wandb_project trace-verdict-study --wandb_run_name qwen15b_exception_only_seed42 && python eval/evaluate.py --condition exception_only --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_exception_only_seed42/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_exception_only_seed42/final/eval_results.json --save_predictions\\\"\", \"wandb_run_id\": \"qwen15b_exception_only_seed42\", \"code_commit\": \"e404237ccc765768e267d4d6fd3c89549dcf41a4\", \"finished_at\": \"2026-05-16T09:53:32.293Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T09:53:34.556600+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.9983, \"accuracy_ci_lower\": 0.9958, \"accuracy_ci_upper\": 1, \"majority_baseline\": 0.7151, \"lift\": 0.283, \"n\": 1190, \"pass_precision\": 1, \"pass_recall\": 0.9976, \"pass_f1\": 0.9988, \"fail_precision\": 0.9941, \"fail_recall\": 1, \"fail_f1\": 0.9971, \"train_loss\": 0.1347, \"eval_loss\": 0.5761, \"wall_clock_seconds\": 1762}, \"completed_at\": \"2026-05-16T09:55:45.253Z\", \"hypothesis\": \"Scale invariance: exception_only signal sufficiency (99.83% on 7B) holds at 1.5B because high signal-to-noise ratio in exception traces requires minimal model capacity to exploit\", \"parent\": \"vota_exception_only_seed42_v2\"}, \"debugbench_vota_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T23:33:57.931Z\", \"updated_at\": \"2026-05-17T02:58:39.423Z\", \"spec\": {\"hypothesis\": \"plan_005: VOTA on DebugBench (bug detection). Tests if VOTA's structured trace analysis provides additional signal beyond exception_only on a logic-error-dominated benchmark.\", \"model_name\": \"Qwen/Qwen2.5-Coder-7B-Instruct\", \"seed\": 42, \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/debugbench_vota_{train,test}.jsonl\", \"data_count\": {\"train\": 1622, \"test\": 426}, \"plan_id\": \"plan_005\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && ... && python train/train_sft.py --condition debugbench_vota --gradient_checkpointing --gpu 0 --seed 42 --output_dir .../debugbench_vota --wandb_project trace-verdict-study --wandb_run_name debugbench_vota_seed42 && python eval/evaluate.py --condition debugbench_vota --checkpoint_dir .../debugbench_vota/final --gpu 0\\\"\", \"server\": \"westd-11235\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_vota\", \"log_path\": \"~/runs/trace-verdict-study/debugbench_vota_seed42.log\"}, \"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-16T00:01:37.634Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition debugbench_vota --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_vota --wandb_project trace-verdict-study --wandb_run_name debugbench_vota_seed42 && python eval/evaluate.py --condition debugbench_vota --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_vota/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_vota/final/eval_results.json\\\"\", \"wandb_run_id\": \"debugbench_vota_seed42\", \"code_commit\": \"e404237ccc765768e267d4d6fd3c89549dcf41a4\", \"finished_at\": \"2026-05-16T00:55:26.974Z\", \"training_hours\": 0.9}, \"pid\": \"211253\", \"log_path\": \"~/runs/trace-verdict-study/debugbench_vota_seed42.log\", \"wandb_run_id\": \"debugbench_vota_seed42\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T00:55:28.620314+00:00\"}]}, \"metrics\": {\"accuracy\": 0.9977, \"majority_baseline\": 0.5141, \"lift\": 0.4836, \"n\": 426, \"pass_precision\": 1, \"pass_recall\": 1, \"pass_f1\": 1, \"fail_precision\": 1, \"fail_recall\": 1, \"fail_f1\": 1, \"accuracy_ci\": [0.993, 1], \"train_loss\": 0.098, \"eval_loss\": 0.1179, \"eval_mean_token_accuracy\": 0.9737, \"errors\": 1}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T00:58:14.197Z\", \"notes\": \"predictions.jsonl generated (426 lines). Accuracy=99.77%, matches registry. Path: /root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_vota/final/predictions.jsonl\", \"hypothesis\": \"DebugBench VOTA generalization: VOTA compressed trace maintains near-perfect accuracy on out-of-distribution bugs, confirming trace compression captures generalizable diagnostic patterns\", \"parent\": \"vota_seed42_v5\"}, \"debugbench_no_trace_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T23:33:55.756Z\", \"updated_at\": \"2026-05-17T02:58:38.962Z\", \"spec\": {\"hypothesis\": \"plan_005: No-trace baseline on DebugBench. Establishes baseline for VOTA/exception_only comparison on bug detection task.\", \"model_name\": \"Qwen/Qwen2.5-Coder-7B-Instruct\", \"seed\": 42, \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/debugbench_no_trace_{train,test}.jsonl\", \"data_count\": {\"train\": 1622, \"test\": 426}, \"plan_id\": \"plan_005\", \"server\": \"westd-11235\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_no_trace\", \"log_path\": \"~/runs/trace-verdict-study/debugbench_no_trace_seed42.log\"}, \"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-16T00:58:18.036Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition debugbench_no_trace --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_no_trace --wandb_project trace-verdict-study --wandb_run_name debugbench_no_trace_seed42 && python eval/evaluate.py --condition debugbench_no_trace --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_no_trace/final --gpu 0 --save_predictions --output /root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_no_trace/final/eval_results.json\\\"\", \"wandb_run_id\": \"debugbench_no_trace_seed42\", \"code_commit\": \"e404237ccc765768e267d4d6fd3c89549dcf41a4\", \"finished_at\": \"2026-05-16T01:09:14.222Z\", \"training_hours\": 0.18}, \"pid\": \"215223\", \"log_path\": \"~/runs/trace-verdict-study/debugbench_no_trace_seed42.log\", \"wandb_run_id\": \"debugbench_no_trace_seed42\", \"gpu_id\": \"cuda:1\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T01:09:16.070113+00:00\"}]}, \"metrics\": {\"accuracy\": 0.9671, \"majority_baseline\": 0.5141, \"lift\": 0.4531, \"pass_precision\": 1, \"pass_recall\": 0.936, \"pass_f1\": 0.967, \"fail_precision\": 0.937, \"fail_recall\": 1, \"fail_f1\": 0.967, \"accuracy_ci\": [0.948, 0.984], \"train_loss\": 0.249, \"eval_loss\": 0.532}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T01:12:05.904Z\", \"hypothesis\": \"DebugBench no-trace baseline: without execution trace, model relies on code structure alone — on DebugBench (50/50 pass/fail) this yields higher lift than HumanEval (71.5% majority) but still far below trace conditions\", \"parent\": \"no_trace_seed42_v5\"}, \"debugbench_exception_only_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T23:33:52.790Z\", \"updated_at\": \"2026-05-17T02:58:38.028Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition debugbench_exception_only --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_exception_only --wandb_project trace-verdict-study --wandb_run_name debugbench_exception_only_seed42 && python eval/evaluate.py --condition debugbench_exception_only --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_exception_only/final --gpu 0 --save_predictions --output /root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_exception_only/final/eval_results.json\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"216806\", \"log_path\": \"~/runs/trace-verdict-study/debugbench_exception_only_seed42.log\", \"submitted_at\": \"2026-05-16T01:11:57.937Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1255.3, \"gpu_hours\": 0.35}, \"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"pid\": \"216806\", \"log_path\": \"~/runs/trace-verdict-study/debugbench_exception_only_seed42.log\", \"wandb_run_id\": \"debugbench_exception_only_seed42\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition debugbench_exception_only --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_exception_only --wandb_project trace-verdict-study --wandb_run_name debugbench_exception_only_seed42 && python eval/evaluate.py --condition debugbench_exception_only --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_exception_only/final --gpu 0 --save_predictions --output /root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_exception_only/final/eval_results.json\\\"\", \"wandb_run_id\": \"debugbench_exception_only_seed42\", \"code_commit\": \"e404237ccc765768e267d4d6fd3c89549dcf41a4\", \"finished_at\": \"2026-05-16T01:27:40.798Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T01:27:43.171585+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 1, \"majority_baseline\": 0.5141, \"lift\": 0.4859, \"n\": 426, \"pass_precision\": 1, \"pass_recall\": 1, \"pass_f1\": 1, \"fail_precision\": 1, \"fail_recall\": 1, \"fail_f1\": 1, \"accuracy_ci_wilson\": [0.9914, 1], \"accuracy_ci_bootstrap\": [1, 1], \"train_loss\": 0.2435, \"eval_loss\": 0.4157, \"train_runtime_sec\": 837}, \"notes\": \"100.0% accuracy (426/426 完美预测)。exception_only 在 DebugBench 上超越 VOTA (99.77%) 和 no_trace (96.71%)。Checkpoint: /root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_exception_only/final/。Predictions: predictions.jsonl (426条)。\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_exception_only/final/\", \"completed_at\": \"2026-05-16T01:32:53.272Z\", \"predictions_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_exception_only/final/predictions.jsonl\", \"hypothesis\": \"Out-of-distribution generalization: exception_only signal sufficiency transfers to DebugBench (different bug categories, different code styles) because exception events carry universal diagnostic information regardless of bug origin\", \"parent\": \"vota_exception_only_seed42_v2\"}, \"deepseek_full_trace_seed42_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:40:07.877Z\", \"updated_at\": \"2026-05-17T02:58:37.133Z\", \"hypothesis\": \"DeepSeek full_trace v3: retrain with label-preserving truncation fix in to_chat_text(). v1/v2 collapsed due to DeepSeek tokenizer producing >2048 tokens → SFTTrainer right-truncated labels. Tests if full_trace shows intermediate performance on DeepSeek (plan_004, 4th condition).\", \"parent\": \"deepseek_full_trace_seed42\", \"notes\": \"DeepSeek full_trace v3: label-preserving truncation fix. 79.16% confirmed with max_length=2048 (matches training). eval_results.json has stale 28.49% from max_length=16384 run; correct value in eval_results_maxlen2048.json. predictions.jsonl overwritten 2026-05-16 with maxlen2048 results (reliable). Systematic audit 2026-05-16 confirmed: adapter base_model=DeepSeek, no model mixup possible (dimension mismatch would crash).\", \"spec\": {\"command\": \"python train_sft.py --condition full_trace --model deepseek-coder-6.7b --max_length 2048 --seed 42\", \"server\": \"westd-11235\", \"data_path\": \"/root/trace-verdict-study/data\", \"data_count\": 5910, \"model_name\": \"deepseek-ai/deepseek-coder-6.7b-instruct\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_full_trace_seed42_v3\", \"log_path\": \"/root/trace-verdict-study/logs/deepseek_full_trace_seed42_v3\"}, \"gpu\": \"cuda:1\", \"metrics\": {\"accuracy\": 0.7916, \"majority_baseline\": 0.7151, \"lift\": 0.0765, \"n\": 1190, \"pass_precision\": 0.857, \"pass_recall\": 0.851, \"pass_f1\": 0.854, \"fail_precision\": 0.632, \"fail_recall\": 0.643, \"fail_f1\": 0.637, \"accuracy_ci\": [0.768, 0.813], \"train_loss\": 0.0547, \"train_runtime_seconds\": 8891, \"epochs\": 3, \"reeval_discrepancy\": {\"reeval_accuracy\": 0.285, \"reeval_note\": \"RESOLVED: 28.5% was caused by eval max_length=16384 (OOD). Re-eval with max_length=2048 reproduces 79.16%. predictions.jsonl updated to maxlen2048 results.\", \"status\": \"RESOLVED\"}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T23:27:54.219Z\", \"log_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_full_trace_seed42_v3.log\"}, \"loop_only_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T06:03:36.673Z\", \"updated_at\": \"2026-05-17T02:56:52.417Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition loop_only --gradient_checkpointing --gpu 0 --seed 456 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/loop_only_seed456 --wandb_project trace-verdict-study --wandb_run_name loop_only_seed456 && python eval/evaluate.py --condition loop_only --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/loop_only_seed456/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/loop_only_seed456/final/eval_results.json --save_predictions\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"269723\", \"log_path\": \"~/runs/trace-verdict-study/loop_only_seed456.log\", \"submitted_at\": \"2026-05-16T11:31:50.484Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 7892.7, \"gpu_hours\": 2.19}, \"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"pid\": \"269723\", \"log_path\": \"~/runs/trace-verdict-study/loop_only_seed456.log\", \"wandb_run_id\": \"loop_only_seed456\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition loop_only --gradient_checkpointing --gpu 0 --seed 456 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/loop_only_seed456 --wandb_project trace-verdict-study --wandb_run_name loop_only_seed456 && python eval/evaluate.py --condition loop_only --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/loop_only_seed456/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/loop_only_seed456/final/eval_results.json --save_predictions\\\"\", \"wandb_run_id\": \"loop_only_seed456\", \"code_commit\": \"e404237ccc765768e267d4d6fd3c89549dcf41a4\", \"finished_at\": \"2026-05-16T13:39:35.472Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T13:39:37.576842+00:00\"}]}, \"metrics\": {\"accuracy\": 0.8664, \"n\": 1190, \"pass_precision\": 0.9179, \"pass_recall\": 0.8931, \"pass_f1\": 0.9053, \"fail_precision\": 0.7486, \"fail_recall\": 0.7994, \"fail_f1\": 0.7732, \"accuracy_ci\": [0.847, 0.884], \"seed_comparison\": {\"seed42_accuracy\": 0.8563, \"seed123_accuracy\": 0.8588, \"seed456_accuracy\": 0.8664, \"mean_accuracy\": 0.8605, \"std\": 0.0053, \"note\": \"3-seed mean = 86.05% ± 0.53%. Moderate variance, seed456 best. loop_only is weakest trace condition (vs exception_only 99.83%, ae_only 99.64%, vota 99.41%).\"}}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/loop_only_seed456/final\", \"completed_at\": \"2026-05-16T13:43:23.144Z\", \"notes\": \"Loop_only seed robustness 完成: seed42=85.63%, seed123=85.88%, seed456=86.64%. Mean=86.05% ± 0.43. 稳定。\", \"hypothesis\": \"Seed robustness of loop_only: loop behavioral patterns alone yield ~85% accuracy consistently across seeds, confirming loop_only is a moderate-signal condition independent of initialization\", \"parent\": \"vota_loop_only_seed42\"}, \"loop_only_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T06:03:35.196Z\", \"updated_at\": \"2026-05-17T02:56:51.920Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition loop_only --gradient_checkpointing --gpu 0 --seed 123 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/loop_only_seed123 --wandb_project trace-verdict-study --wandb_run_name loop_only_seed123 && python eval/evaluate.py --condition loop_only --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/loop_only_seed123/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/loop_only_seed123/final/eval_results.json --save_predictions\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"261213\", \"log_path\": \"~/runs/trace-verdict-study/loop_only_seed123.log\", \"submitted_at\": \"2026-05-16T09:21:29.194Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/loop_only_seed123/final\", \"wall_clock_seconds\": 7779.8, \"gpu_hours\": 2.16}, \"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"pid\": \"261213\", \"log_path\": \"~/runs/trace-verdict-study/loop_only_seed123.log\", \"wandb_run_id\": \"loop_only_seed123\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition loop_only --gradient_checkpointing --gpu 0 --seed 123 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/loop_only_seed123 --wandb_project trace-verdict-study --wandb_run_name loop_only_seed123 && python eval/evaluate.py --condition loop_only --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/loop_only_seed123/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/loop_only_seed123/final/eval_results.json --save_predictions\\\"\", \"wandb_run_id\": \"loop_only_seed123\", \"code_commit\": \"e404237ccc765768e267d4d6fd3c89549dcf41a4\", \"finished_at\": \"2026-05-16T11:28:44.218Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T11:28:46.379629+00:00\"}]}, \"metrics\": {\"accuracy\": 0.8588, \"majority_baseline\": 0.7151, \"lift\": 0.1437, \"n\": 1190, \"pass_precision\": 0.9129, \"pass_recall\": 0.8872, \"pass_f1\": 0.8999, \"fail_precision\": 0.7355, \"fail_recall\": 0.7876, \"fail_f1\": 0.7607, \"accuracy_ci\": [0.8403, 0.8773]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T11:31:09.027Z\", \"notes\": \"Loop_only seed robustness 完成: seed42=85.63%, seed123=85.88%, seed456=86.64%. Mean=86.05% ± 0.43. 稳定。\", \"hypothesis\": \"Seed robustness of loop_only: loop behavioral patterns alone yield ~85% accuracy consistently across seeds, confirming loop_only is a moderate-signal condition independent of initialization\", \"parent\": \"vota_loop_only_seed42\"}, \"ae_only_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T03:41:51.316Z\", \"updated_at\": \"2026-05-17T02:56:50.865Z\", \"hypothesis\": \"Seed robustness: ae_only with seed=456 on Qwen-2.5-Coder-7B. Verifies ae_only 99.92% is stable across seeds (Reviewer P0 requirement).\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition ae_only --gradient_checkpointing --gpu 0 --seed 456 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/ae_only_seed456 --wandb_project trace-verdict-study --wandb_run_name ae_only_seed456 && python eval/evaluate.py --condition ae_only --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/ae_only_seed456/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/ae_only_seed456/final/eval_results.json --save_predictions\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/ae_only_{train,test}.jsonl\", \"data_count\": 4720, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 456, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/ae_only_seed456/final\", \"log_path\": \"/tmp/ae_only_seed456.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T06:26:31.454Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T06:26:32.421Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T06:26:34.050811+00:00\"}]}, \"metrics\": {\"accuracy\": 0.9992, \"n\": 1190, \"majority_baseline\": 0.7151, \"lift\": 0.2841, \"seed_comparison\": {\"seed42_accuracy\": 0.9992, \"seed123_accuracy\": 0.9908, \"seed456_accuracy\": 0.9992, \"mean_accuracy\": 0.9964, \"std\": 0.0049, \"note\": \"2/3 seeds = 99.92%, seed123 = 99.08%. Mean = 99.64% ± 0.49\"}}, \"parent\": \"vota_ae_only_seed42\"}, \"ae_only_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T03:41:50.753Z\", \"updated_at\": \"2026-05-17T02:56:49.985Z\", \"hypothesis\": \"Seed robustness: ae_only with seed=123 on Qwen-2.5-Coder-7B. Verifies ae_only 99.92% is stable across seeds (Reviewer P0 requirement).\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition ae_only --gradient_checkpointing --gpu 0 --seed 123 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/ae_only_seed123 --wandb_project trace-verdict-study --wandb_run_name ae_only_seed123 && python eval/evaluate.py --condition ae_only --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/ae_only_seed123/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/ae_only_seed123/final/eval_results.json --save_predictions\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/ae_only_{train,test}.jsonl\", \"data_count\": 4720, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/ae_only_seed123\", \"log_path\": \"/tmp/ae_only_seed123.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T06:16:31.845Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T06:16:33.018Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T06:16:35.841653+00:00\"}]}, \"metrics\": {\"accuracy\": 0.9908, \"n\": 1190, \"pass_recall\": 0.987, \"fail_recall\": 1, \"majority_baseline\": 0.7151, \"lift\": 0.2757}, \"notes\": \"Cron 误判为 failed（进程死亡 5× 无 sentinel/W&B），Reviewer 独立核实训练+eval 均成功完成。accuracy=99.08% 低于 seed42/456 (99.92%)，ae_only 3-seed mean=99.64% ± 0.49。\", \"parent\": \"vota_ae_only_seed42\"}, \"exception_only_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:31:02.005Z\", \"updated_at\": \"2026-05-17T02:56:49.009Z\", \"spec\": {\"plan_id\": \"plan_008a\", \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 456, \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/exception_only_{train,test}.jsonl\", \"data_count\": 4720, \"server\": \"westd-11235\"}, \"hypothesis\": \"Seed robustness: exception_only with seed=456 on Qwen-2.5-Coder-7B (plan_008). Verifies headline result 99.83% is stable across seeds.\", \"server\": \"westd-11235\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-11235\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-15T16:38:44.142Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition exception_only --gradient_checkpointing --gpu 0 --seed 456 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_seed456 --wandb_project trace-verdict-study --wandb_run_name exception_only_seed456 && python eval/evaluate.py --condition exception_only --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_seed456/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_seed456/final/eval_results.json\\\"\", \"wandb_run_id\": \"exception_only_seed456\", \"finished_at\": \"2026-05-15T17:56:16.196Z\", \"training_hours\": 1.29}, \"pid\": \"129476\", \"log_path\": \"~/runs/trace-verdict-study/exception_only_seed456.log\", \"wandb_run_id\": \"exception_only_seed456\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:56:17.874949+00:00\"}]}, \"metrics\": {\"accuracy\": 0.9983, \"accuracy_ci\": [0.9958, 1], \"majority_baseline\": 0.7151, \"lift\": 0.2832, \"n\": 1190, \"pass_precision\": 1, \"pass_recall\": 0.9976, \"pass_f1\": 0.9988, \"fail_precision\": 0.9941, \"fail_recall\": 1, \"fail_f1\": 0.9971, \"vs_seed42\": {\"seed42_accuracy\": 0.9983, \"seed456_accuracy\": 0.9983, \"diff\": 0, \"note\": \"identical accuracy to 4 decimal places; no predictions.jsonl for paired bootstrap\"}, \"train_loss\": 0.1087, \"eval_loss\": 0.4629, \"train_runtime_sec\": 4541, \"epochs\": 3}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_seed456/final\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T17:58:25.389Z\", \"notes\": \"Seed robustness 结论: exception_only 99.83% ± 0.00 (seeds 42/123/456), 每 seed 恰好 2/1190 errors。极大概率同一组 irreducible 样本。\", \"parent\": \"vota_exception_only_seed42_v2\"}, \"exception_only_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:31:01.555Z\", \"updated_at\": \"2026-05-17T02:56:48.058Z\", \"spec\": {\"plan_id\": \"plan_008a\", \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 123, \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/exception_only_{train,test}.jsonl\", \"data_count\": 4720, \"server\": \"westd-11235\"}, \"hypothesis\": \"Seed robustness: exception_only with seed=123 on Qwen-2.5-Coder-7B (plan_008). Verifies headline result 99.83% is stable across seeds.\", \"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-15T15:54:06.157Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition exception_only --gradient_checkpointing --gpu 0 --seed 123 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_seed123 --wandb_project trace-verdict-study --wandb_run_name exception_only_seed123 && python eval/evaluate.py --condition exception_only --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_seed123/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_seed123/final/eval_results.json\\\"\", \"wandb_run_id\": \"exception_only_seed123\", \"finished_at\": \"2026-05-15T18:00:50.835Z\", \"training_hours\": 2.11}, \"pid\": \"124197\", \"log_path\": \"~/runs/trace-verdict-study/exception_only_seed123.log\", \"wandb_run_id\": \"exception_only_seed123\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T18:00:52.169672+00:00\"}]}, \"notes\": \"Seed robustness 结论: exception_only 99.83% ± 0.00 (seeds 42/123/456), 每 seed 恰好 2/1190 errors。极大概率同一组 irreducible 样本。\", \"metrics\": {\"accuracy\": 0.9983, \"accuracy_ci\": [0.9958, 1], \"majority_baseline\": 0.7151, \"lift\": 0.2832, \"n\": 1190, \"pass_precision\": 1, \"pass_recall\": 0.9976, \"pass_f1\": 0.9988, \"fail_precision\": 0.9941, \"fail_recall\": 1, \"fail_f1\": 0.9971, \"train_loss\": 0.1096, \"train_runtime_sec\": 7507, \"epochs\": 3, \"seed_comparison\": {\"seed42_accuracy\": 0.9983, \"seed456_accuracy\": 0.9983, \"seed123_accuracy\": 0.9983, \"max_diff\": 0, \"note\": \"identical accuracy to 4 decimal places across all 3 seeds (42/456/123); each has exactly 2/1190 errors; exception_only fully seed-robust\"}}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_seed123/final\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T18:03:37.166Z\", \"parent\": \"vota_exception_only_seed42_v2\"}, \"exception_only_nomarker_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:12:12.683Z\", \"updated_at\": \"2026-05-17T02:56:47.143Z\", \"spec\": {\"hypothesis\": \"Task G: Format marker ablation — seed=456. Remove [No exception data in trace] marker from exception_only and retrain. Tests whether format marker affects model judgment.\", \"parent\": \"exception_only_seed42\", \"plan_id\": \"round5_task_g\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/exception_only_nomarker_train.jsonl\", \"data_count\": 4720, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 456}, \"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-16T18:24:34.339Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/trace-verdict-study && python train/train_sft.py --condition exception_only_nomarker --model_path /root/trace-verdict-study/models/Qwen2.5-Coder-7B-Instruct --gradient_checkpointing --gpu 0 --seed 456 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_nomarker_seed456 --wandb_project trace-verdict-study --wandb_run_name exception_only_nomarker_seed456 && python eval/evaluate.py --condition exception_only_nomarker --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_nomarker_seed456/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_nomarker_seed456/final/eval_results.json --save_predictions\\\"\", \"wandb_run_id\": \"exception_only_nomarker_seed456\", \"code_commit\": \"e404237ccc765768e267d4d6fd3c89549dcf41a4\", \"finished_at\": \"2026-05-16T19:44:27.466Z\", \"training_hours\": 1.33}, \"pid\": \"296962\", \"log_path\": \"~/runs/trace-verdict-study/exception_only_nomarker_seed456.log\", \"wandb_run_id\": \"exception_only_nomarker_seed456\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T19:44:29.627669+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.9807, \"n\": 1190, \"errors\": 23, \"ci_95\": [0.9712, 0.9871], \"pass_f1\": 0.9865, \"fail_f1\": 0.9658, \"pass_precision\": 0.9836, \"pass_recall\": 0.9894, \"fail_precision\": 0.9731, \"fail_recall\": 0.9587, \"lift_over_majority\": 0.266}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_nomarker_seed456/final\", \"completed_at\": \"2026-05-16T19:47:16.706Z\", \"hypothesis\": \"Seed robustness of nomarker ablation: format marker contribution (~2pp) is consistent across random seeds, not an artifact of specific LoRA initialization\", \"parent\": \"exception_only_nomarker_seed42\"}, \"exception_only_nomarker_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:12:11.533Z\", \"updated_at\": \"2026-05-17T02:56:41.485Z\", \"spec\": {\"hypothesis\": \"Task G: Format marker ablation — seed=123. Remove [No exception data in trace] marker from exception_only and retrain. Tests whether format marker affects model judgment.\", \"parent\": \"exception_only_seed42\", \"plan_id\": \"round5_task_g\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"account\": \"root\", \"command\": \"cd /root/trace-verdict-study && /root/miniconda3/bin/python train/train_sft.py --condition exception_only_nomarker --model_path /root/trace-verdict-study/models/Qwen2.5-Coder-7B-Instruct --gradient_checkpointing --gpu 0 --seed 123\", \"pid\": \"294700\", \"log_path\": \"/tmp/nomarker_seed123.log\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/exception_only_nomarker_train.jsonl\", \"data_count\": 4720, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 123}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.9832, \"n\": 1190, \"ci_95\": [0.9756, 0.9899], \"pass_f1\": 0.9882, \"fail_f1\": 0.9705, \"pass_precision\": 0.9882, \"pass_recall\": 0.9882, \"fail_precision\": 0.9705, \"fail_recall\": 0.9705, \"lift_over_majority\": 0.2681}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_nomarker/final\", \"completed_at\": \"2026-05-16T19:07:39.167Z\", \"hypothesis\": \"Seed robustness of nomarker ablation: format marker contribution (~2pp) is consistent across random seeds, not an artifact of specific LoRA initialization\", \"parent\": \"exception_only_nomarker_seed42\"}, \"exception_only_nomarker_seed42\": {\"status\": \"DONE\", \"retry_count\": 2, \"created_at\": \"2026-05-16T06:03:33.324Z\", \"updated_at\": \"2026-05-17T02:56:40.848Z\", \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"reproduce\": {\"finished_at\": \"2026-05-16T17:06:14.692Z\"}, \"completed_at\": \"2026-05-16T15:50:22.017Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T15:50:23.894246+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T17:06:17.875239+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"python train/train_sft.py --condition exception_only_nomarker --model_path models/Qwen2.5-Coder-7B-Instruct --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_nomarker_seed42 --wandb_run_name exception_only_nomarker_seed42 --gradient_checkpointing && python eval/evaluate.py --condition exception_only_nomarker --checkpoint_dir .../exception_only_nomarker_seed42/final --save_predictions\", \"server\": \"westd-11235\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/exception_only_nomarker_{train,test}.jsonl\", \"data_count\": 5910, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_nomarker_seed42\", \"log_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_nomarker_seed42_train.log\", \"gpu\": \"cuda:0\", \"tmux_session\": \"nomarker_seed42\", \"description\": \"R1-N1 control: exception_only with ALL bracket format markers removed\", \"markers_removed\": [\"[No exception data in trace]\", \"[ERROR] prefix\", \"[No trace available]\", \"[...trace truncated...]\"], \"train_samples\": 4720, \"test_samples\": 1190}, \"wandb_run_id\": \"exception_only_nomarker_seed42\", \"pid\": 287933, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.9655, \"n\": 1190, \"accuracy_ci\": [0.955, 0.976]}, \"hypothesis\": \"Format marker ablation: removing [No exception data in trace] and [ERROR] prefix markers reduces accuracy by ~2pp, isolating semantic content contribution (~97%) from formatting cue contribution (~2%)\", \"parent\": \"vota_exception_only_seed42_v2\"}, \"codellama13b_exception_only_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T19:59:26.563Z\", \"updated_at\": \"2026-05-17T02:56:39.750Z\", \"spec\": {\"hypothesis\": \"CodeLlama-13B exception_only seed456 — 3-seed robustness validation for cross-family core claim\", \"parent\": \"codellama13b_exception_only_seed42\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/exception_only_train.jsonl\", \"data_count\": 4720, \"model_name\": \"CodeLlama-13b-Instruct-hf\", \"seed\": 456, \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"account\": \"root\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition exception_only --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf --gradient_checkpointing --gpu 0 --seed 456 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_exception_only_seed456 --wandb_project trace-verdict-study --wandb_run_name codellama13b_exception_only_seed456 && python eval/evaluate.py --condition exception_only --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_exception_only_seed456/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_exception_only_seed456/final/eval_results.json --save_predictions\\\"\", \"pid\": \"303301\", \"log_path\": \"~/runs/trace-verdict-study/codellama13b_exception_only_seed456.log\", \"submitted_at\": \"2026-05-16T19:59:26Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"wall_clock_seconds\": 9834.4, \"gpu_hours\": 2.73}, \"reproduce\": {\"finished_at\": \"2026-05-16T22:41:10.285Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T22:41:13.148200+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.9983, \"n\": 1190, \"errors\": 2, \"pass_precision\": 1, \"pass_recall\": 0.9976, \"pass_f1\": 0.9988, \"fail_precision\": 0.9941, \"fail_recall\": 1, \"fail_f1\": 0.9971}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_exception_only_seed456/final\", \"hypothesis\": \"CodeLlama-13B exception_only seed456 — 3-seed robustness: exception signal sufficiency is consistent across random initializations, achieving near-perfect accuracy regardless of seed\", \"completed_at\": \"2026-05-16T22:43:20.359Z\", \"parent\": \"codellama13b_exception_only_seed42\"}, \"codellama13b_exception_only_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T19:10:52.335Z\", \"updated_at\": \"2026-05-17T02:56:38.799Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition exception_only --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf --gradient_checkpointing --gpu 0 --seed 123 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_exception_only_seed123 --wandb_project trace-verdict-study --wandb_run_name codellama13b_exception_only_seed123 && python eval/evaluate.py --condition exception_only --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_exception_only_seed123/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_exception_only_seed123/final/eval_results.json --save_predictions\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"pid\": \"299731\", \"log_path\": \"~/runs/trace-verdict-study/codellama13b_exception_only_seed123.log\", \"submitted_at\": \"2026-05-16T19:10:52.141Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/exception_only_train.jsonl\", \"data_count\": 4720, \"model_name\": \"CodeLlama-13b-Instruct-hf\", \"seed\": 123, \"wall_clock_seconds\": 9933.3, \"gpu_hours\": 2.76}, \"reproduce\": {\"finished_at\": \"2026-05-16T21:53:40.177Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T21:53:43.651373+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 1, \"n\": 1190, \"errors\": 0, \"pass_precision\": 1, \"pass_recall\": 1, \"pass_f1\": 1, \"fail_precision\": 1, \"fail_recall\": 1, \"fail_f1\": 1, \"lift_over_majority\": 0.2849}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_exception_only_seed123/final\", \"hypothesis\": \"CodeLlama-13B exception_only seed123 — multi-seed robustness: exception signal sufficiency is not seed-dependent and achieves near-perfect accuracy regardless of LoRA initialization\", \"completed_at\": \"2026-05-16T21:56:25.436Z\", \"parent\": \"codellama13b_exception_only_seed42\"}, \"label_only_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T04:40:19.669Z\", \"updated_at\": \"2026-05-16T09:22:46.929Z\", \"hypothesis\": \"Seed robustness: label_only (full_trace + label-only loss) with seed=456 on Qwen-2.5-Coder-7B. Verifies label_only 86.22% stability across seeds.\", \"parent\": \"full_trace_label_only_seed42\", \"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-16T05:31:03.019Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition full_trace --label_only_loss --gradient_checkpointing --gpu 0 --seed 456 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_label_only_seed456 --wandb_project trace-verdict-study --wandb_run_name label_only_seed456 && python eval/evaluate.py --condition full_trace --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_label_only_seed456/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_label_only_seed456/final/eval_results.json --save_predictions\\\"\", \"wandb_run_id\": \"label_only_seed456\", \"code_commit\": \"e404237ccc765768e267d4d6fd3c89549dcf41a4\", \"finished_at\": \"2026-05-16T09:01:08.445Z\", \"training_hours\": 3.5}, \"spec\": {\"command\": \"python train/train_sft.py --condition full_trace --label_only_loss --gradient_checkpointing --gpu 0 --seed 456 + evaluate.py\", \"server\": \"westd-11235\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/full_trace_{train,test}.jsonl\", \"data_count\": 5910, \"model_name\": \"Qwen/Qwen2.5-Coder-7B-Instruct\", \"seed\": 456, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_label_only_seed456/final\", \"log_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_label_only_seed456/final/eval_results.json\"}, \"pid\": \"249616\", \"log_path\": \"~/runs/trace-verdict-study/label_only_seed456.log\", \"wandb_run_id\": \"label_only_seed456\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T09:01:14.180779+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.859, \"n\": 1190, \"pass_recall\": 0.938, \"fail_recall\": 0.661, \"pass_f1\": 0.905, \"fail_f1\": 0.727}, \"completed_at\": \"2026-05-16T09:22:46.929Z\"}, \"label_only_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T04:40:18.683Z\", \"updated_at\": \"2026-05-16T09:01:41.007Z\", \"hypothesis\": \"Seed robustness: label_only (full_trace + label-only loss) with seed=123 on Qwen-2.5-Coder-7B. Verifies label_only 86.22% stability across seeds.\", \"parent\": \"full_trace_label_only_seed42\", \"server\": \"westd-11235\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-11235\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-16T05:31:02.488Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition full_trace --label_only_loss --gradient_checkpointing --gpu 0 --seed 123 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_label_only_seed123 --wandb_project trace-verdict-study --wandb_run_name label_only_seed123 && python eval/evaluate.py --condition full_trace --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_label_only_seed123/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_label_only_seed123/final/eval_results.json --save_predictions\\\"\", \"wandb_run_id\": \"label_only_seed123\", \"code_commit\": \"e404237ccc765768e267d4d6fd3c89549dcf41a4\", \"finished_at\": \"2026-05-16T08:58:33.644Z\", \"training_hours\": 3.46}, \"spec\": {\"command\": \"python train/train_sft.py --condition full_trace --label_only_loss --gradient_checkpointing --gpu 0 --seed 123 + evaluate.py\", \"server\": \"westd-11235\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/full_trace_{train,test}.jsonl\", \"data_count\": 5910, \"model_name\": \"Qwen/Qwen2.5-Coder-7B-Instruct\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_label_only_seed123/final\", \"log_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_label_only_seed123/final/eval_results.json\"}, \"pid\": \"249124\", \"log_path\": \"~/runs/trace-verdict-study/label_only_seed123.log\", \"wandb_run_id\": \"label_only_seed123\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T08:58:35.632418+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.8706, \"n\": 1190, \"pass_recall\": 0.974, \"fail_recall\": 0.611, \"pass_f1\": 0.915, \"fail_f1\": 0.729}, \"completed_at\": \"2026-05-16T09:01:41.007Z\"}, \"regex_baseline_analysis\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T03:43:17.799Z\", \"updated_at\": \"2026-05-16T04:08:29.402Z\", \"hypothesis\": \"Regex/heuristic baselines on exception_only test data. Tests if simple pattern matching can match SFT performance (Reviewer critical concern).\", \"conclusion\": \"success\", \"metrics\": {\"regex_B1_ERROR_presence\": 0.9345, \"regex_B2_Traceback\": 0.7151, \"regex_B3_any_keyword\": 0.9345, \"regex_B4_exception_type\": 0.9361, \"regex_B5_format_marker\": 0.9933, \"regex_B6_error_count_ge2\": 0.9202, \"sft_exception_only\": 0.9983, \"best_regex_gap_vs_sft\": -0.0622, \"B5_mcnemar_p\": 0.041, \"n\": 1190}, \"spec\": {\"checkpoint_path\": \"N/A (CPU analysis, no model)\", \"log_path\": \"N/A (CPU analysis)\"}, \"checkpoint_path\": \"N/A (analysis-only, no training)\", \"log_path\": \"N/A (analysis-only, no training)\", \"completed_at\": \"2026-05-16T04:08:09.296Z\"}, \"full_trace_2048tok_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:27:19.848Z\", \"updated_at\": \"2026-05-16T04:08:09.868Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition full_trace --data_dir /root/autodl-tmp/trace-verdict-study-data/ --model_path /root/trace-verdict-study/models/Qwen2.5-Coder-7B-Instruct --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_2048tok --max_trace_tokens 2048 --seed 42 --wandb_run_name full_trace_2048tok_seed42 --gradient_checkpointing && python eval/evaluate.py --condition full_trace --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_2048tok/final --gpu 0 --save_predictions --output /root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_2048tok/final/eval_results.json\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"220276\", \"log_path\": \"~/runs/trace-verdict-study/full_trace_2048tok_seed42.log\", \"submitted_at\": \"2026-05-16T01:35:43.979Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 9136.0, \"gpu_hours\": 2.54}, \"conclusion\": \"killed\", \"notes\": \"Director 取消：max_trace_tokens=2048 经 chat template overhead 后有效 trace ~1970 tok，与 no_limit (max_length=2048 封顶) 几乎一致。Token length ablation 最终设计改为 256/512/1024/no_limit 四点。\", \"completed_at\": \"2026-05-16T04:07:59.930Z\"}, \"deepseek_vota_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T10:13:39.391Z\", \"updated_at\": \"2026-05-16T02:45:56.773Z\", \"hypothesis\": \"Multi-model validation: VOTA on DeepSeek-Coder-6.7B-Instruct (plan_004). Tests if VOTA's verdict accuracy advantage generalizes beyond Qwen2.5-Coder to DCSH's same base model.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition vota --model_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_vota --gradient_checkpointing --gpu 0 --seed 42 --wandb_project trace-verdict-study --wandb_run_name deepseek_vota_seed42 && python eval/evaluate.py --condition vota --model_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_vota/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_vota/final/eval_results.json\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"pid\": \"93484\", \"log_path\": \"~/runs/trace-verdict-study/deepseek_vota_seed42.log\", \"submitted_at\": \"2026-05-15T10:45:36.891Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/vota_{train,test}.jsonl\", \"data_count\": 4720, \"model_name\": \"deepseek-ai/deepseek-coder-6.7b-instruct\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_vota/final\", \"wall_clock_seconds\": 8839.9, \"gpu_hours\": 2.46}, \"reproduce\": {\"finished_at\": \"2026-05-15T13:06:46.525Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T13:06:47.175122+00:00\"}]}, \"metrics\": {\"accuracy\": 0.8445, \"majority_baseline\": 0.7151, \"lift\": 0.1294, \"accuracy_ci\": [0.826, 0.864], \"pass_precision\": 0.821, \"pass_recall\": 1, \"pass_f1\": 0.902, \"fail_precision\": 1, \"fail_recall\": 0.454, \"fail_f1\": 0.625, \"eval_loss_epoch1\": 0.0679, \"eval_loss_epoch2\": 0.095, \"eval_loss_epoch3\": 0.1121, \"final_train_loss\": 0.0522, \"epoch1_checkpoint_eval\": {\"accuracy\": 0.7815, \"accuracy_ci\": [0.76, 0.803], \"fail_recall\": 0.233, \"fail_precision\": 1, \"pass_recall\": 1, \"pass_precision\": 0.766, \"fail_f1\": 0.378, \"pass_f1\": 0.867, \"conclusion\": \"epoch3_final_is_better\"}, \"reeval_with_fixed_script\": {\"accuracy\": 0.16, \"accuracy_ci\": [0.139, 0.18], \"fail_f1\": 0.61, \"fail_precision\": 0.9, \"fail_recall\": 0.47, \"pass_f1\": 0.07, \"pass_precision\": 1, \"pass_recall\": 0.04, \"note\": \"CATASTROPHIC: re-eval with corrected evaluate.py shows 16% (vs original 84.45%). Model predicts fail for almost everything. Previous 84.45% may have been from buggy eval. NEEDS INVESTIGATION.\"}, \"group_analysis\": {\"train_truncated\": {\"n\": 1091, \"accuracy\": 0.8304, \"ci_95\": [0.8075, 0.8524], \"correct\": 906, \"incorrect\": 185, \"pass_accuracy\": 1, \"pass_n\": 822, \"fail_accuracy\": 0.3123, \"fail_n\": 269}, \"train_intact\": {\"n\": 99, \"accuracy\": 1, \"ci_95\": [1, 1], \"correct\": 99, \"incorrect\": 0, \"pass_accuracy\": 1, \"pass_n\": 29, \"fail_accuracy\": 1, \"fail_n\": 70}, \"fisher_exact\": {\"odds_ratio\": 0, \"p_value\": 0}, \"overall_accuracy\": 0.8445, \"max_length\": 2048, \"note\": \"Grouped by whether training sample content exceeded token budget (DeepSeek tokenizer, max_length=2048). Inference used full-length input (no truncation). All 185 errors from truncated group's fail class (fail_recall=31.2%). Intact group: 100% accuracy.\"}}, \"conclusion\": \"success\", \"log_path\": \"/root/runs/trace-verdict-study/deepseek_vota_seed42.log\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_vota/final\", \"completed_at\": \"2026-05-15T13:12:56.838Z\", \"notes\": \"DeepSeek VOTA: 84.45% confirmed with max_length=16384 (re-verified 2026-05-16, exact match). max_length=2048 gives 16% due to evaluate.py front-truncation removing \\\"Answer: \\\" suffix from 91.7% of inputs. Training-time eval used old script (no truncation). exception_only/no_trace unaffected (short inputs). Systematic audit 2026-05-16: adapter base_model=DeepSeek confirmed, no model mixup possible.\"}, \"deepseek_exception_only_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:19:31.586Z\", \"updated_at\": \"2026-05-16T01:16:41.387Z\", \"hypothesis\": \"Cross-model seed robustness: exception_only seed=456 on DeepSeek-Coder-6.7B. Third seed to determine if seed42 (99.83%) is outlier or seed123 (91.09%) is outlier.\", \"parent\": \"deepseek_exception_only_seed123\", \"spec\": {\"command\": \"python train/train_sft.py --condition exception_only --model_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_exception_only_seed456 --gradient_checkpointing --gpu 0 --seed 456 --wandb_project trace-verdict-study --wandb_run_name deepseek_exception_only_seed456\", \"server\": \"westd-11235\", \"model_name\": \"deepseek-ai/deepseek-coder-6.7b-instruct\", \"seed\": 456, \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/exception_only_{train,test}.jsonl\", \"data_count\": 4720, \"checkpoint_source\": \"N/A - training run\", \"eval_data\": \"N/A - training run\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T22:08:34.111Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T22:08:35.359157+00:00\"}]}, \"metrics\": {\"accuracy\": 0.9933, \"majority_baseline\": 0.7151, \"lift\": 0.2782, \"n\": 1190, \"pass_precision\": 1, \"pass_recall\": 0.9906, \"pass_f1\": 0.9953, \"fail_precision\": 0.9769, \"fail_recall\": 1, \"fail_f1\": 0.9883, \"accuracy_ci\": [0.9882, 0.9975], \"train_loss\": 0.1225, \"eval_loss\": 0.4824, \"train_runtime_sec\": 6246, \"seed_comparison\": {\"seed42_accuracy\": 0.9933, \"seed456_accuracy\": 0.9933, \"seed123_accuracy\": 0.9109, \"note\": \"seed42 and seed456 identical (99.33%); seed123 outlier (91.09%). 2/3 seeds robust.\"}, \"epoch1_checkpoint_eval\": {\"accuracy\": 0.993, \"accuracy_ci\": [0.988, 0.997], \"fail_f1\": 0.99, \"fail_precision\": 0.98, \"fail_recall\": 1, \"pass_f1\": 1, \"pass_precision\": 1, \"pass_recall\": 0.99, \"conclusion\": \"epoch1 (99.3%) ≈ epoch3 (99.33%), 1 epoch convergence confirmed\"}}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_exception_only_seed456/final\", \"log_path\": \"/root/runs/trace-verdict-study/deepseek_exception_only_seed456.log\", \"conclusion\": \"success\", \"notes\": \"seed456 accuracy 99.33% = seed42 99.33%（完全一致）。seed123 (91.09%) 是离群值——2/3 seeds 在 DeepSeek 上稳定。Epoch1 checkpoint (checkpoint-148) 可用于 epoch1 eval。Eval 由 on_complete hook 的 eval 脚本 (PID 166680) 自动运行，结果写入 final/eval_results.json。\", \"completed_at\": \"2026-05-15T22:13:38.554Z\", \"outputs\": {\"predictions_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_exception_only_seed456/checkpoint-148/predictions.jsonl\"}}, \"deepseek_exception_only_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T10:17:07.674Z\", \"updated_at\": \"2026-05-16T01:16:38.239Z\", \"hypothesis\": \"Multi-model validation: exception_only on DeepSeek-Coder-6.7B-Instruct (plan_004). Tests if exception dominance (99.83% on Qwen) generalizes across models — the most valuable cross-model evidence.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition exception_only --model_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_exception_only --gradient_checkpointing --gpu 0 --seed 42 --wandb_project trace-verdict-study --wandb_run_name deepseek_exception_only_seed42 && python eval/evaluate.py --condition exception_only --model_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_exception_only/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_exception_only/final/eval_results.json\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"107188\", \"log_path\": \"~/runs/trace-verdict-study/deepseek_exception_only_seed42.log\", \"submitted_at\": \"2026-05-15T13:10:32.405Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/exception_only_{train,test}.jsonl\", \"data_count\": 4720, \"model_name\": \"deepseek-ai/deepseek-coder-6.7b-instruct\", \"seed\": 42, \"wall_clock_seconds\": 7358.8, \"gpu_hours\": 2.04}, \"reproduce\": {\"finished_at\": \"2026-05-15T15:06:51.643Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T15:06:52.877301+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_exception_only/final\", \"metrics\": {\"accuracy\": 0.9933, \"majority_baseline\": 0.7151, \"lift\": 0.2782, \"n\": 1190, \"pass_precision\": 1, \"pass_recall\": 0.9906, \"pass_f1\": 0.9953, \"fail_precision\": 0.9769, \"fail_recall\": 1, \"fail_f1\": 0.9883, \"epoch1_checkpoint_eval\": {\"accuracy\": 0.9983, \"fail_recall\": 1, \"fail_precision\": 0.9941, \"pass_recall\": 0.9976, \"conclusion\": \"epoch1_better_by_0.50pp\"}}, \"completed_at\": \"2026-05-15T15:13:11.215Z\", \"notes\": \"epoch 1 (step 148) accuracy = 99.83%，高于 final (epoch 3) 的 99.33%。eval_loss epoch 2→3 从 0.413 涨到 0.476 (+15%)。continued training 导致 token-level 过拟合，verdict accuracy 从 99.83% 降到 99.33% (-0.50pp)。这是 eval_loss/accuracy 解耦的又一例证——但此处 eval_loss 上升确实伴随 accuracy 下降，与 DeepSeek VOTA 的趋势相反。Epoch 1 的 99.83% 与 Qwen exception_only (99.83%) 完全一致——跨模型 gap = 0pp（在最佳 checkpoint 下）。\", \"outputs\": {\"predictions_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_exception_only/checkpoint-148/predictions.jsonl\"}}, \"deepseek_no_trace_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T10:13:40.004Z\", \"updated_at\": \"2026-05-16T01:16:37.143Z\", \"hypothesis\": \"Multi-model baseline: no-trace verdict prediction on DeepSeek-Coder-6.7B-Instruct (plan_004). Establishes DeepSeek baseline for comparison with VOTA and full_trace conditions.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition no_trace --model_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_no_trace --gradient_checkpointing --gpu 0 --seed 42 --wandb_project trace-verdict-study --wandb_run_name deepseek_no_trace_seed42 && python eval/evaluate.py --condition no_trace --model_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_no_trace/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_no_trace/final/eval_results.json\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"pid\": \"106822\", \"log_path\": \"~/runs/trace-verdict-study/deepseek_no_trace_seed42.log\", \"submitted_at\": \"2026-05-15T13:09:35.611Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/no_trace_{train,test}.jsonl\", \"data_count\": 4720, \"model_name\": \"deepseek-ai/deepseek-coder-6.7b-instruct\", \"seed\": 42, \"wall_clock_seconds\": 1791.4, \"gpu_hours\": 0.5}, \"reproduce\": {\"finished_at\": \"2026-05-15T13:37:07.125Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T13:37:08.315605+00:00\"}]}, \"conclusion\": \"negative\", \"metrics\": {\"accuracy\": 0.7336, \"majority_baseline\": 0.7151, \"lift\": 0.0185, \"n\": 1190, \"pass_precision\": 0.817, \"pass_recall\": 0.808, \"pass_f1\": 0.813, \"fail_precision\": 0.532, \"fail_recall\": 0.546, \"fail_f1\": 0.539, \"accuracy_ci\": [0.708, 0.757], \"lift_ci\": [-0.009, 0.046]}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_no_trace/final\", \"log_path\": \"~/runs/trace-verdict-study/deepseek_no_trace_seed42.log\", \"completed_at\": \"2026-05-15T13:39:27.031Z\", \"notes\": \"Negative: lift +1.85pp over majority, 95% CI [-0.93, +4.63] crosses 0. DeepSeek-Coder-6.7B no-trace verdict prediction is not statistically different from majority baseline. Within-model VOTA lift: +11.09pp (84.45% - 73.36%).\", \"outputs\": {\"predictions_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_no_trace/final/predictions.jsonl\"}}, \"debugbench_exception_bug_fix\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T23:14:24.382Z\", \"updated_at\": \"2026-05-15T23:26:16.029Z\", \"spec\": {\"command\": \"python data/debugbench_format_data.py\", \"server\": \"westd-11235\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/debugbench/raw_traces.jsonl\", \"data_count\": 2048, \"model_name\": \"data_processing\", \"seed\": 42, \"checkpoint_path\": \"/root/trace-verdict-study/data/debugbench_format_data.py\", \"log_path\": \"/tmp/debugbench_format.log\"}, \"conclusion\": \"success\", \"hypothesis\": \"BUG FIX: compress_exception_only() only checked trace_raw events, missing 625/1006 empty-trace fails (syntax errors) + 5 event-capped samples. Fix: fallback to test_results.error. Exception signal 376→1006/1006, upper bound 69.2%→100%. DebugBench 30.5% empty trace rate confirmed.\", \"completed_at\": \"2026-05-15T23:26:16.029Z\"}, \"vota_seed456_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:39:05.494Z\", \"updated_at\": \"2026-05-15T21:04:28.008Z\", \"hypothesis\": \"Seed robustness: VOTA with seed=456, retry with --gradient_checkpointing (v1 OOM). Verifies VOTA 99.2% accuracy stable across seeds.\", \"notes\": \"Auto-retried from vota_seed456 (OOM). PID 146592, cuda:1, --gradient_checkpointing enabled. Started 18:31 UTC, ~2h to complete. Low priority per Director (VOTA not primary claim).\", \"parent\": \"vota_seed456\", \"spec\": {\"command\": \"python train/train_sft.py --condition vota --gradient_checkpointing --gpu 0 --seed 456 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/vota_seed456 --wandb_project trace-verdict-study --wandb_run_name vota_seed456_v2\", \"server\": \"westd-11235\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/vota_{train,test}.jsonl\", \"data_count\": 4720, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 456, \"checkpoint_source\": \"N/A (training, not eval)\", \"eval_data\": \"N/A (training, not eval)\"}, \"metrics\": {\"accuracy\": 0.9908, \"pass_precision\": 1, \"pass_recall\": 0.987, \"pass_f1\": 0.993, \"fail_precision\": 0.969, \"fail_recall\": 1, \"fail_f1\": 0.984, \"ci_95\": [0.985, 0.996]}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/vota_seed456/final\", \"log_path\": \"/root/runs/trace-verdict-study/vota_seed456.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T21:04:28.008Z\"}, \"no_trace_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:58:31.125Z\", \"updated_at\": \"2026-05-15T19:53:26.153Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export WANDB_API_KEY=[REDACTED] /root/.wandb_api_key 2>/dev/null || echo '') && cd /root/trace-verdict-study && python train/train_sft.py --condition no_trace --gpu 0 --wandb_project trace-verdict-study --wandb_run_name no_trace_seed42\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"pid\": \"709277\", \"log_path\": \"~/runs/trace-verdict-study/no_trace_seed42.log\", \"submitted_at\": \"2026-05-14T17:58:31.124Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 93295.0, \"gpu_hours\": 25.92}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:53:26.153Z\"}, \"no_trace_seed42_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:59:53.488Z\", \"updated_at\": \"2026-05-15T19:53:25.181Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export WANDB_API_KEY=[REDACTED] /root/.wandb_api_key 2>/dev/null || echo '') && cd /root/trace-verdict-study && python train/train_sft.py --condition no_trace --gpu 0 --wandb_project trace-verdict-study --wandb_run_name no_trace_seed42\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"pid\": \"709781\", \"log_path\": \"~/runs/trace-verdict-study/no_trace_seed42_v2.log\", \"submitted_at\": \"2026-05-14T17:59:53.485Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 93211.7, \"gpu_hours\": 25.89}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:53:25.181Z\"}, \"vota_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:58:32.967Z\", \"updated_at\": \"2026-05-15T19:53:23.979Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export WANDB_API_KEY=[REDACTED] /root/.wandb_api_key 2>/dev/null || echo '') && cd /root/trace-verdict-study && python train/train_sft.py --condition vota --gpu 1 --wandb_project trace-verdict-study --wandb_run_name vota_seed42\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"709357\", \"log_path\": \"~/runs/trace-verdict-study/vota_seed42.log\", \"submitted_at\": \"2026-05-14T17:58:32.964Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 93291.0, \"gpu_hours\": 25.91}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:53:23.979Z\"}, \"vota_seed42_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:59:55.517Z\", \"updated_at\": \"2026-05-15T19:53:22.853Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export WANDB_API_KEY=[REDACTED] /root/.wandb_api_key 2>/dev/null || echo '') && cd /root/trace-verdict-study && python train/train_sft.py --condition vota --gpu 1 --wandb_project trace-verdict-study --wandb_run_name vota_seed42\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"709863\", \"log_path\": \"~/runs/trace-verdict-study/vota_seed42_v2.log\", \"submitted_at\": \"2026-05-14T17:59:55.513Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 93207.3, \"gpu_hours\": 25.89}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:53:22.853Z\"}, \"vota_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T12:38:51.823Z\", \"updated_at\": \"2026-05-15T18:38:53.768Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition vota --gradient_checkpointing --gpu 0 --seed 456 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/vota_seed456 --wandb_project trace-verdict-study --wandb_run_name vota_seed456_v2 && python eval/evaluate.py --condition vota --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/vota_seed456/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/vota_seed456/final/eval_results.json --save_predictions --max_length 2048\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"146582\", \"log_path\": \"~/runs/trace-verdict-study/vota_seed456.log\", \"submitted_at\": \"2026-05-15T18:31:33.049Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 87.5, \"gpu_hours\": 0.02}, \"hypothesis\": \"Seed robustness: VOTA with seed=456 (plan_008). Verifies VOTA 99.2% accuracy is stable across random seeds.\", \"notes\": \"Original PID 145908 OOM'd ~3min after start. Auto-retried as v2 (PID 146592) with --gradient_checkpointing on cuda:1. Step 15/444 (3.4%) at 18:37 UTC, ~2h to complete. W&B run: vota_seed456_v2. Director 决策: 低优先级，exception_only seed robustness 优先。\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T18:33:00.592Z\"}, \"deepseek_full_trace_seed42_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:13:29.181Z\", \"updated_at\": \"2026-05-15T18:27:46.453Z\", \"hypothesis\": \"DeepSeek full_trace v2: retrain with v5 code (chat-template-aware truncation preserving labels). v1 collapsed to 28.49% due to label truncation during training.\", \"spec\": {\"plan_id\": \"plan_004\", \"model_name\": \"deepseek-ai/deepseek-coder-6.7b-instruct\", \"seed\": 42, \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/full_trace_{train,test}.jsonl\", \"data_count\": 4720, \"server\": \"westd-11235\", \"command\": \"train_sft.py --condition full_trace + evaluate.py\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_full_trace_v2\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T18:27:40.446Z\", \"notes\": \"Killed by worker_ops_kill_and_submit_vota_seed456 to free cuda:1 for vota_seed456. Training incomplete — needs re-run after GPU available. PID 144864 killed at ~18:24 UTC.\"}, \"deepseek_full_trace_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T10:13:40.756Z\", \"updated_at\": \"2026-05-15T18:23:42.993Z\", \"hypothesis\": \"Multi-model comparison: full-trace verdict prediction on DeepSeek-Coder-6.7B-Instruct (plan_004). Tests if full_trace also shows intermediate performance on DeepSeek-Coder.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition full_trace --model_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_full_trace --gradient_checkpointing --gpu 0 --seed 42 --wandb_project trace-verdict-study --wandb_run_name deepseek_full_trace_seed42 && python eval/evaluate.py --condition full_trace --model_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_full_trace/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_full_trace/final/eval_results.json\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"pid\": \"112289\", \"log_path\": \"~/runs/trace-verdict-study/deepseek_full_trace_seed42.log\", \"submitted_at\": \"2026-05-15T13:47:47.241Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/full_trace_{train,test}.jsonl\", \"data_count\": 4720, \"model_name\": \"deepseek-ai/deepseek-coder-6.7b-instruct\", \"seed\": 42, \"wall_clock_seconds\": 10254.4, \"gpu_hours\": 2.85}, \"notes\": \"INVALIDATED: train-eval truncation mismatch。旧 eval (无截断): 28.49% (all predict fail)。修复后 eval (截断到 2048): 10.59% (模型输出垃圾 token: '{', 'execution', '{}', 'assert' 等, 从未输出 'pass')。结论：LoRA 本身训练失败，不仅是 eval 问题。truncation fix 暴露了更深层问题——训练时 label 被截断导致 LoRA 未学到有效分类行为。v2 重训已提交 (deepseek_full_trace_seed42_v2)。\", \"reproduce\": {\"finished_at\": \"2026-05-15T16:36:17.857Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T16:36:19.211594+00:00\"}]}, \"metrics\": {\"accuracy_no_truncation\": 0.2849, \"accuracy_with_truncation_fix\": 0.1059, \"accuracy_with_truncation_fix_ci\": [0.089, 0.123], \"majority_baseline\": 0.7151, \"n\": 1190, \"note\": \"Both evals show model failure. No-truncation: all predict fail. With-truncation: garbage tokens. LoRA training itself failed due to label truncation during training.\"}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_full_trace/final\", \"log_path\": \"~/runs/trace-verdict-study/deepseek_full_trace_seed42.log\", \"completed_at\": \"2026-05-15T16:38:41.604Z\"}, \"vota_exception_only_seed42_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:16:14.602Z\", \"updated_at\": \"2026-05-15T18:02:36.534Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition exception_only --gradient_checkpointing --gpu 1 --seed 42 --wandb_project trace-verdict-study --wandb_run_name vota_exception_only_seed42_v2 && python eval/evaluate.py --condition exception_only --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/exception_only/final --gpu 1 --output /root/autodl-tmp/trace-verdict-study-checkpoints/exception_only/final/eval_results.json\\\"\", \"server\": \"westd-11235\", \"data_path\": \"exception_only\", \"data_count\": 4720, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 42, \"pid\": \"79633\", \"gpu\": [\"cuda:1\"], \"submitted_at\": \"2026-05-15T15:15:14Z\", \"log_path\": \"~/runs/trace-verdict-study/vota_exception_only_seed42_v2.log\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/exception_only/final\"}, \"hypothesis\": \"VOTA component ablation: exception_only condition — retry with --gradient_checkpointing (v1 OOM at step 8). Tests if [ERROR] events are the primary driver of VOTA's 99.2% accuracy (plan_003 sub-b)\", \"metrics\": {\"accuracy\": 0.9983, \"majority_baseline\": 0.7151, \"lift\": 0.2832, \"n\": 1190, \"pass_precision\": 1, \"pass_recall\": 0.998, \"pass_f1\": 0.999, \"fail_precision\": 0.994, \"fail_recall\": 1, \"fail_f1\": 0.997, \"lift_vs_notrace\": 0.2471, \"lift_vs_notrace_ci_lower\": 0.2227, \"lift_vs_notrace_ci_upper\": 0.2714, \"lift_vs_fulltrace\": 0.1807, \"lift_vs_fulltrace_ci_lower\": 0.1588, \"lift_vs_fulltrace_ci_upper\": 0.2034, \"lift_vs_vota\": 0.0067, \"lift_vs_vota_ci_lower\": 0.0017, \"lift_vs_vota_ci_upper\": 0.0126, \"lift_vs_vota_pvalue\": 0.01}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T09:35:01.676Z\", \"notes\": \"Seed robustness confirmed: exception_only 99.83% ± 0.00 across seeds 42/123/456. Each seed has exactly 2/1190 errors. High probability same irreducible samples. [re-eval] 修复后 evaluate.py 重跑 Δ=0。\"}, \"vota_seed123\": {\"status\": \"DONE\", \"retry_count\": 2, \"created_at\": \"2026-05-15T12:38:48.954Z\", \"updated_at\": \"2026-05-15T16:58:40.507Z\", \"hypothesis\": \"Seed robustness: VOTA with seed=123 (plan_008). Verifies VOTA 99.2% accuracy is stable across random seeds.\", \"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-15T12:39:38.117Z\", \"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition vota --gradient_checkpointing --gpu 0 --seed 123 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/vota_seed123 --wandb_project trace-verdict-study --wandb_run_name vota_seed123_v2 && python eval/evaluate.py --condition vota --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/vota_seed123/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/vota_seed123/final/eval_results.json\\\"\", \"finished_at\": \"2026-05-15T12:59:09.843Z\", \"training_hours\": 0.33, \"wandb_run_id\": \"vota_seed123_v2\"}, \"failure_reason\": \"CUDA OOM: CUDA out of memory. Tried to allocate 4.64 GiB. GPU 0 has a total capacity of 94.97 GiB of which 614.25 MiB is free. Process 93494 has 21.86 GiB memory in use. Including non-PyTorch memory, this process has 24.48 GiB memory in use. Of the allocated m\", \"completed_at\": \"2026-05-15T12:42:01.260Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T12:42:02.205055+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T12:59:14.689674+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"conclusion\": \"failed\", \"spec\": {\"plan_id\": \"plan_008b\", \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 123, \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/vota_{train,test}.jsonl\", \"data_count\": 4720, \"server\": \"westd-11235\"}}, \"full_trace_label_only_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T04:01:29.625Z\", \"updated_at\": \"2026-05-15T16:36:05.917Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_label_only/final\", \"log_path\": \"~/runs/trace-verdict-study/full_trace_label_only_seed42.log\"}, \"hypothesis\": \"Label-only loss on full_trace fixes gradient dilution collapse (plan_002: loss only on pass/fail token, not trace tokens)\", \"reproduce\": {\"finished_at\": \"2026-05-15T07:15:28.991Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T07:15:30.057513+00:00\"}]}, \"metrics\": {\"accuracy\": 0.8622, \"accuracy_ci_lower\": 0.8437, \"accuracy_ci_upper\": 0.8807, \"majority_baseline\": 0.7151, \"lift\": 0.1471, \"n\": 1190, \"pass_precision\": 0.8821, \"pass_recall\": 0.9318, \"pass_f1\": 0.9063, \"fail_precision\": 0.8007, \"fail_recall\": 0.6873, \"fail_f1\": 0.7397, \"train_loss\": 0.2505, \"eval_loss\": 0.3205, \"lift_vs_notrace\": 0.1109, \"lift_vs_notrace_ci_lower\": 0.0849, \"lift_vs_notrace_ci_upper\": 0.137, \"lift_vs_standard_fulltrace\": 0.0445, \"lift_vs_standard_fulltrace_ci_lower\": 0.0235, \"lift_vs_standard_fulltrace_ci_upper\": 0.0655, \"lift_vs_standard_fulltrace_pvalue\": 0}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T07:23:57.111Z\", \"notes\": \"Label-only loss 将 full_trace 从 81.8% 提升到 86.2% (+4.4pp)，确认 gradient dilution 是 full_trace 性能受限的部分原因。但 86.2% vs VOTA 99.2% 仍有 13pp gap，说明 gradient dilution 只是部分解释——trace 信息密度（VOTA 的 decision-relevant compression）才是主因。[2026-05-15 re-eval] 用修复后 evaluate.py + --condition full_trace 重跑，accuracy 不变 (86.22% → 86.22%, Δ=0)，predictions.jsonl 1190行已生成。训练确认使用 full_trace 格式数据，label_only 仅改变 loss mask。\"}, \"vota_no_ae_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T04:21:27.279Z\", \"updated_at\": \"2026-05-15T16:25:20.610Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition vota_no_ae --gpu 1 --seed 42 --wandb_project trace-verdict-study --wandb_run_name vota_no_ae_seed42\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"953133\", \"log_path\": \"~/runs/trace-verdict-study/vota_no_ae_seed42.log\", \"submitted_at\": \"2026-05-15T04:21:27.215Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/vota_no_ae_train.jsonl\", \"data_count\": 4720, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/vota_no_ae/final\", \"wall_clock_seconds\": 6902.4, \"gpu_hours\": 1.92}, \"hypothesis\": \"VOTA without actual/expected values: tests if VOTA's accuracy comes from genuine behavioral understanding vs trivial string comparison (plan_001)\", \"reproduce\": {\"finished_at\": \"2026-05-15T06:10:18.839Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T06:10:19.847891+00:00\"}]}, \"metrics\": {\"accuracy\": 0.994, \"majority_baseline\": 0.7151, \"lift\": 0.279, \"n\": 1190, \"pass_f1\": 0.996, \"fail_f1\": 0.989, \"accuracy_ci_lower\": 0.989, \"accuracy_ci_upper\": 0.998, \"lift_vs_notrace\": 0.243, \"lift_vs_notrace_ci_lower\": 0.218, \"lift_vs_notrace_ci_upper\": 0.268, \"train_loss\": 0.0908, \"eval_loss\": 0.2215, \"wall_clock_seconds\": 6397.88}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T06:16:29.587Z\", \"notes\": \"✅ Eval verified: accuracy 99.4% [98.9, 99.8] confirmed by evaluate.py + bootstrap. 去掉 actual/expected 后性能不降（vs VOTA v5 99.2%），证明 VOTA 效果来自 trace 行为模式理解而非 trivial string comparison。Claim 1 走 full positive framing。[2026-05-15 re-eval] 用修复后 evaluate.py 重跑，accuracy 不变 (99.41% → 99.41%, Δ=0)，predictions.jsonl 1190行已生成。\"}, \"vota_loop_only_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:02:41.201Z\", \"updated_at\": \"2026-05-15T16:25:16.352Z\", \"hypothesis\": \"VOTA component ablation: loop_only condition — only loop compression summaries, no actual/expected or exception. Tests loop behavioral pattern contribution to VOTA 99.2% accuracy (plan_003 sub-c)\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition loop_only --gradient_checkpointing --gpu 0 --seed 42 --wandb_project trace-verdict-study --wandb_run_name vota_loop_only_seed42 && python eval/evaluate.py --condition loop_only --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/loop_only/final --gpu 0\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"pid\": \"82362\", \"log_path\": \"~/runs/trace-verdict-study/vota_loop_only_seed42.log\", \"submitted_at\": \"2026-05-15T07:58:06.023Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/loop_only_{train,test}.jsonl\", \"data_count\": 4720, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 42, \"wall_clock_seconds\": 7952.5, \"gpu_hours\": 2.21}, \"reproduce\": {\"finished_at\": \"2026-05-15T10:04:53.052Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T10:04:54.341040+00:00\"}]}, \"metrics\": {\"accuracy\": 0.8563, \"majority_baseline\": 0.7151, \"lift\": 0.1412, \"n\": 1190, \"pass_precision\": 0.9239, \"pass_recall\": 0.8707, \"pass_f1\": 0.8966, \"fail_precision\": 0.7165, \"fail_recall\": 0.8201, \"fail_f1\": 0.7648, \"accuracy_ci\": [0.8353, 0.8756], \"bootstrap_vs_no_trace\": {\"diff\": 0.105, \"ci\": [0.0824, 0.1286], \"significant\": true}, \"bootstrap_vs_vota\": {\"diff\": -0.1378, \"ci\": [-0.1571, -0.1185], \"significant\": true}, \"bootstrap_vs_full_trace\": {\"diff\": 0.0387, \"ci\": [0.0185, 0.0597], \"significant\": true}, \"train_loss\": 0.0718, \"wall_clock_seconds\": 7425.65}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/loop_only/final/\", \"log_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/loop_only/final/eval_results.json\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T10:10:38.549Z\", \"notes\": \"[2026-05-15 re-eval] 用修复后 evaluate.py 重跑，accuracy 不变 (85.63% → 85.63%, Δ=0)，predictions.jsonl 1190行已生成。\"}, \"vota_ae_only_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:11:44.999Z\", \"updated_at\": \"2026-05-15T16:25:14.973Z\", \"hypothesis\": \"VOTA component ablation: ae_only condition — only actual/expected values, no exception/loop compression (plan_003 sub-a)\", \"notes\": \"ae_only accuracy 99.92% [99.75%, 100%]。与 exception_only (99.83%) 统计等价，均为 Tier 1 diagnostic-moment signals。88% 样本含 fallback locals 行（无信息量的模块命名空间导入），85% 样本含 [ASSERT] 行的 actual/expected 对比（合法诊断信息）。Reviewer 核实 fallback locals 不含 verdict 信号，不构成 data leakage（D013 裁定）。Train: 3 epochs, 444 steps, final train_loss=0.022, eval_loss=0.166, eval_token_acc=96.76%。[2026-05-15 re-eval] 用修复后 evaluate.py 重跑，accuracy 不变 (99.92% → 99.92%, Δ=0)，predictions.jsonl 1190行已生成。\", \"spec\": {\"command\": \"python train/train_sft.py --condition ae_only --gradient_checkpointing --gpu 1 --seed 42 --wandb_project trace-verdict-study --wandb_run_name vota_ae_only_seed42 && python eval/evaluate.py --condition ae_only --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/ae_only/final --gpu 1 --output /root/autodl-tmp/trace-verdict-study-checkpoints/ae_only/final/eval_results.json\", \"server\": \"westd-11235\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/ae_only_train.jsonl\", \"data_count\": 4720, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 42}, \"reproduce\": {\"finished_at\": \"2026-05-15T12:13:36.539Z\"}, \"failure_reason\": \"N/A — cron 误判。实际已完成，eval_results.json 已生成。process dead 5x 是因为训练+eval 正常结束后进程退出，cron 无 W&B/sentinel 检测通道。\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T12:13:36.813Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T12:13:37.756005+00:00\"}]}, \"metrics\": {\"accuracy\": 0.9992, \"accuracy_ci\": [0.9975, 1], \"bootstrap_pairwise\": {\"ae_only_vs_no_trace\": {\"diff\": 0.2479, \"ci\": [0.2235, 0.2731], \"p_value\": 0, \"significant\": true}, \"ae_only_vs_exception_only\": {\"diff\": 0.0008, \"ci\": [-0.0017, 0.0034], \"p_value\": 0.8002, \"significant\": false}, \"ae_only_vs_vota\": {\"diff\": 0.005, \"ci\": [0.0017, 0.0092], \"p_value\": 0.0046, \"significant\": true}}, \"config\": {\"n_bootstrap\": 10000, \"seed\": 42, \"method\": \"paired_bootstrap\"}}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/ae_only/final\", \"log_path\": \"~/runs/trace-verdict-study/vota_ae_only_seed42.log\"}, \"full_trace_seed42_v5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T01:46:03.068Z\", \"updated_at\": \"2026-05-15T15:50:39.179Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/full_trace/final/\", \"log_path\": \"~/runs/trace-verdict-study/full_trace_seed42_v5.log\", \"wall_clock_seconds\": 7852, \"gpu_hours\": 2.18}, \"hypothesis\": \"Full execution trace with chat-template-aware truncation provides verdict accuracy lift vs no-trace baseline (v5: fixed chat template overhead)\", \"reproduce\": {\"finished_at\": \"2026-05-15T03:58:14.030Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T03:58:14.897249+00:00\"}]}, \"metrics\": {\"accuracy\": 0.8176, \"majority_baseline\": 0.7151, \"lift\": 0.1025, \"n\": 1190, \"pass_precision\": 0.8774, \"pass_recall\": 0.866, \"pass_f1\": 0.8717, \"fail_precision\": 0.6743, \"fail_recall\": 0.6962, \"fail_f1\": 0.6851, \"accuracy_ci_lower\": 0.797, \"accuracy_ci_upper\": 0.839, \"lift_vs_notrace\": 0.0664, \"lift_vs_notrace_ci_lower\": 0.0437, \"lift_vs_notrace_ci_upper\": 0.0899, \"train_loss\": 0.05, \"eval_loss\": 0.0867, \"wall_clock_seconds\": 7852, \"epoch_level\": {\"epoch1_accuracy\": 0.8303, \"epoch2_accuracy\": 0.763, \"final_accuracy\": 0.8176, \"trend\": \"non_monotonic_epoch1_best_epoch2_collapse\"}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T04:06:20.880Z\", \"notes\": \"✅ Paired bootstrap CI (2026-05-15): lift vs no_trace = +6.6pp [4.4, 9.0]pp (significant, N=10000). lift_ci in registry [7.4, 13.2] was vs majority, not vs no_trace — now corrected.\"}, \"no_trace_seed42_v5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T01:46:17.948Z\", \"updated_at\": \"2026-05-15T15:50:35.449Z\", \"hypothesis\": \"Baseline: verdict accuracy without execution trace (v5: same code version as vota_v5/full_trace_v5 for fair comparison)\", \"conclusion\": \"success\", \"spec\": {\"command\": \"python train/train_sft.py --condition no_trace --gpu 1 --seed 42 --wandb_project trace-verdict-study --wandb_run_name no_trace_seed42_v5\", \"server\": \"westd-11235\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/no_trace_train.jsonl\", \"data_count\": 4720, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/no_trace/final\", \"log_path\": \"~/runs/trace-verdict-study/no_trace_seed42_v5.log\"}, \"completed_at\": \"2026-05-15T06:45:11.265Z\", \"metrics\": {\"accuracy\": 0.7513, \"accuracy_ci_lower\": 0.7277, \"accuracy_ci_upper\": 0.7748, \"majority_baseline\": 0.7151, \"lift\": 0.0361, \"lift_ci_lower\": 0.0042, \"lift_ci_upper\": 0.0706, \"n\": 1190, \"pass_precision\": 0.8776, \"pass_recall\": 0.7579, \"pass_f1\": 0.8134, \"fail_precision\": 0.5473, \"fail_recall\": 0.7345, \"fail_f1\": 0.6272, \"epoch_level\": {\"epoch1_accuracy\": 0.7429, \"epoch2_accuracy\": 0.763, \"final_accuracy\": 0.7513, \"trend\": \"non_monotonic_epoch2_best\"}}}, \"calibration_analysis_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T12:27:04.073Z\", \"updated_at\": \"2026-05-15T13:09:52.711Z\", \"spec\": {\"plan_id\": \"plan_007\", \"command\": \"python eval/calibration_analysis.py\", \"server\": \"westd-11235\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/\", \"data_count\": 1190, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 42}, \"hypothesis\": \"Calibration analysis: ECE + reliability diagrams for VOTA/exception_only/full_trace/no_trace. Tests whether VOTA's compressed traces improve model calibration beyond accuracy (plan_007).\", \"conclusion\": \"success\", \"metrics\": {\"no_trace\": {\"ece\": 0.171476, \"mce\": 0.475643, \"brier_score\": 0.197152, \"accuracy\": 0.751261, \"n_samples\": 1190}, \"full_trace\": {\"ece\": 0.095817, \"mce\": 0.249061, \"brier_score\": 0.143924, \"accuracy\": 0.817647, \"n_samples\": 1190}, \"label_only\": {\"ece\": 0.110686, \"mce\": 0.417124, \"brier_score\": 0.120144, \"accuracy\": 0.862185, \"n_samples\": 1190}, \"loop_only\": {\"ece\": 0.083085, \"mce\": 0.183406, \"brier_score\": 0.118335, \"accuracy\": 0.856303, \"n_samples\": 1190}, \"ae_only\": {\"ece\": 0.000415, \"mce\": 0.000415, \"brier_score\": 0.000847, \"accuracy\": 0.99916, \"n_samples\": 1190}, \"exception_only\": {\"ece\": 0.002717, \"mce\": 0.835484, \"brier_score\": 0.001311, \"accuracy\": 0.998319, \"n_samples\": 1190}, \"vota\": {\"ece\": 0.00541, \"mce\": 0.622459, \"brier_score\": 0.005234, \"accuracy\": 0.994118, \"n_samples\": 1190}}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/calibration/\", \"log_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/calibration/calibration_metrics.json\", \"completed_at\": \"2026-05-15T12:36:49.992Z\"}, \"vota_exception_only_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:02:39.821Z\", \"updated_at\": \"2026-05-15T07:16:20.123Z\", \"hypothesis\": \"VOTA component ablation: exception_only condition — only exception summaries, no actual/expected or loop compression. Tests if [ERROR] events are the primary driver of VOTA's 99.2% accuracy (plan_003 sub-b)\", \"spec\": {\"command\": \"python train/train_sft.py --condition exception_only --gpu 1 --seed 42 --wandb_project trace-verdict-study --wandb_run_name vota_exception_only_seed42 && python eval/evaluate.py --condition exception_only --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/exception_only/final --gpu 1\", \"server\": \"westd-11235\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/exception_only_{train,test}.jsonl\", \"data_count\": {\"train\": 4720, \"test\": 1190}, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"log_path\": \"~/runs/trace-verdict-study/vota_exception_only_seed42.log\", \"failure_reason\": \"OOM at step 8/444 — missing --gradient_checkpointing flag\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T07:16:20.123Z\"}, \"vota_seed42_v4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:12:38.660Z\", \"updated_at\": \"2026-05-15T01:37:13.355Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/vota/final/\", \"log_path\": \"~/runs/trace-verdict-study/vota_seed42_v4.log\", \"wall_clock_seconds\": 8160, \"gpu_hours\": 2.27}, \"hypothesis\": \"VOTA trace provides verdict accuracy lift over no-trace baseline (v4: removed match leakage + fixed label truncation)\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.9563, \"majority_baseline\": 0.7151, \"lift\": 0.2412, \"n\": 1190, \"pass_precision\": 0.944, \"pass_recall\": 0.998, \"pass_f1\": 0.97, \"fail_precision\": 0.993, \"fail_recall\": 0.853, \"fail_f1\": 0.917, \"lift_vs_notrace\": 0.205, \"lift_vs_notrace_ci_lower\": 0.177, \"lift_vs_notrace_ci_upper\": 0.234, \"train_loss\": 0.046, \"eval_loss\": 0.0842}, \"completed_at\": \"2026-05-15T01:10:45.307Z\"}, \"full_trace_seed42_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:12:46.333Z\", \"updated_at\": \"2026-05-15T01:10:45.707Z\", \"hypothesis\": \"Full execution trace with smart truncation (label preserved) provides verdict accuracy lift vs no-trace baseline\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/full_trace/final/\", \"log_path\": \"~/runs/trace-verdict-study/full_trace_seed42_v2.log\", \"wall_clock_seconds\": 7860, \"gpu_hours\": 2.18}, \"metrics\": {\"accuracy\": 0.284, \"majority_baseline\": 0.7151, \"lift\": -0.4311, \"n\": 1190, \"pass_precision\": 0.923, \"pass_recall\": 0.085, \"pass_f1\": 0.155, \"fail_precision\": 0.445, \"fail_recall\": 0.785, \"fail_f1\": 0.568, \"train_loss\": 0.0373, \"eval_loss\": 0.082, \"eval_mean_token_accuracy\": 0.984}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-15T01:10:45.708Z\"}, \"no_trace_seed42_v4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:12:37.755Z\", \"updated_at\": \"2026-05-14T22:39:32.197Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/no_trace/final/\", \"log_path\": \"~/runs/trace-verdict-study/no_trace_seed42_v4.log\", \"wall_clock_seconds\": 1274.7, \"gpu_hours\": 0.35}, \"hypothesis\": \"Baseline: verdict accuracy without execution trace (v4: fixed label truncation)\", \"reproduce\": {\"finished_at\": \"2026-05-14T22:34:36.523Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T22:34:37.283133+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.7513, \"majority_baseline\": 0.7151, \"lift\": 0.0361, \"pass_precision\": 0.8776, \"pass_recall\": 0.7579, \"pass_f1\": 0.8134, \"fail_precision\": 0.5473, \"fail_recall\": 0.7345, \"fail_f1\": 0.6272, \"train_loss\": 0.18, \"eval_loss\": 0.6454, \"eval_mean_token_accuracy\": 0.8897}, \"completed_at\": \"2026-05-14T22:39:12.249Z\"}, \"full_trace_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:38:06.325Z\", \"updated_at\": \"2026-05-14T22:12:18.859Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition full_trace --gpu 0 --wandb_project trace-verdict-study --wandb_run_name full_trace_seed42\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"pid\": \"712469\", \"log_path\": \"~/runs/trace-verdict-study/full_trace_seed42.log\", \"submitted_at\": \"2026-05-14T18:38:06.317Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/full_trace_train.jsonl\", \"data_count\": 4720, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 42, \"hypothesis\": \"Full execution trace (line-by-line Scratchpad format) provides verdict accuracy lift vs no-trace baseline\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/full_trace/final/\", \"wall_clock_seconds\": 11247.5, \"gpu_hours\": 3.12}, \"conclusion\": \"killed\", \"metrics\": {\"train_loss\": 0.037, \"eval_loss\": 0.084, \"eval_mean_token_accuracy\": 0.984, \"accuracy\": 0.284, \"majority_baseline\": 0.7151, \"lift\": -0.431, \"pass_precision\": 0.88, \"pass_recall\": 0.08, \"pass_f1\": 0.16, \"fail_precision\": 0.31, \"fail_recall\": 0.97, \"fail_f1\": 0.57}, \"completed_at\": \"2026-05-14T21:45:33.847Z\"}, \"no_trace_seed42_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:01:02.647Z\", \"updated_at\": \"2026-05-14T22:12:18.583Z\", \"spec\": {\"command\": \"python train/train_sft.py --condition no_trace --gpu 0\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"pid\": \"710523\", \"log_path\": \"~/runs/trace-verdict-study/no_trace_seed42_v3.log\", \"submitted_at\": \"2026-05-14T18:01:02.641Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/no_trace_train.jsonl\", \"data_count\": 4720, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 42, \"hypothesis\": \"Baseline: verdict accuracy without execution trace\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/no_trace/final/\", \"wall_clock_seconds\": 4617.5, \"gpu_hours\": 1.28}, \"conclusion\": \"killed\", \"metrics\": {\"train_loss\": 0.18, \"eval_loss\": 0.645, \"eval_mean_token_accuracy\": 0.89, \"accuracy\": 0.7513, \"majority_baseline\": 0.7151, \"lift\": 0.0361, \"pass_precision\": 0.8776, \"pass_recall\": 0.7579, \"pass_f1\": 0.8134, \"fail_precision\": 0.5473, \"fail_recall\": 0.7345, \"fail_f1\": 0.6272}, \"completed_at\": \"2026-05-14T19:18:00.158Z\"}, \"vota_seed42_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:01:04.345Z\", \"updated_at\": \"2026-05-14T21:51:40.917Z\", \"spec\": {\"command\": \"python train/train_sft.py --condition vota --gpu 1\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"710601\", \"log_path\": \"~/runs/trace-verdict-study/vota_seed42_v3.log\", \"submitted_at\": \"2026-05-14T18:01:04.338Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/vota_train.jsonl\", \"data_count\": 4720, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 42, \"hypothesis\": \"VOTA trace provides significant verdict accuracy lift over no-trace baseline\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/vota/final/\", \"wall_clock_seconds\": 13468.8, \"gpu_hours\": 3.74}, \"conclusion\": \"killed\", \"metrics\": {\"train_loss\": 0.046, \"eval_loss\": 0.085, \"eval_mean_token_accuracy\": 0.983, \"accuracy\": 0.992, \"majority_baseline\": 0.7151, \"lift\": 0.276, \"pass_precision\": 0.99, \"pass_recall\": 0.99, \"pass_f1\": 0.99, \"fail_precision\": 0.99, \"fail_recall\": 0.99, \"fail_f1\": 0.99}, \"completed_at\": \"2026-05-14T21:45:33.135Z\"}}, \"count\": 168, \"total\": 168, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4631}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 12_

<details><summary>Logged reasoning block</summary>

```text
The registry output was too large. I have the paper table data. Now I need to extract the relevant experiment data from the registry. Let me parse the Table 1 data from the paper first, then query the registry for the specific experiments.

From Table 1 in the paper:

| Condition | Qwen-7B | Qwen-1.5B | CL-13B | DS-6.7B |
|-----------|---------|------------|--------|---------|
| exception_only | **99.83**±0.00 | **99.83**±0.00 | **99.89**±0.10 | **99.39**±0.10 |


| ae_only | 99.64±0.49 | 98.83±0.36 | 99.08±0.00 | 98.53±0.30 |
| VOTA | 99.05±0.38 | 99.54±0.06 | 98.74±0.24 | 99.25‡ |
| loop_only | 86.05±0.52 | 79.54±1.42 | 77.40±1.54 | 80.31±1.65 |
| no_trace | 75.13† | 72.35±4.48 | 76.47† | 73.36† |
| Majority baseline | 71.51 (all columns) |

Looking at the rest of the results, the no_trace approach drops significantly to the mid-70s, while the majority baseline sits at 71.51 across all datasets. I'm also noting the footnotes that detail the seed variations and specific model results—like how DeepSeek's exception_only approach achieved 99.33% consistently, and the Qwen models showed different performance profiles depending on the method used.

Now I need to pull the actual experiment data from the registry. I'm going to query the JSON file to extract all the relevant runs across the different model variants—Qwen-7B, Qwen-1.5B, CodeLlama-13B, and DeepSeek-6.7B—for each condition including exception_only, ae_only, VOTA, loop_only, and no_trace.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2d564421-8464-4d87-ad0f-5e3eefeb24a0",
  "uuid": "be8c98d4-ea3a-48ca-b1f7-413d25d6fcfe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VqhjaEA2kDhdZ78QqniuK4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4129,
      "cache_read_input_tokens": 26269,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4129
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

论文 Table 1 已读取。Registry 输出过大，需要用 agent 提取对应数据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2d564421-8464-4d87-ad0f-5e3eefeb24a0",
  "uuid": "38b91f3c-516a-412d-ad7f-2f780345e5fe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VqhjaEA2kDhdZ78QqniuK4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4129,
      "cache_read_input_tokens": 26269,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4129
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

<details open><summary>🔧 Tool call — Agent · `toolu_015HUchPTe4989tKrwAwPKeH`</summary>

```json
{
  "description": "Extract registry data for Table 1 audit",
  "prompt": "I need you to extract specific experiment data from a large registry JSON file for a numerical audit. The file is at:\n`/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/2d564421-8464-4d87-ad0f-5e3eefeb24a0/tool-results/mcp-agent-ml-research-read_registry-1779392719783.txt`\n\nThe file is JSON with schema `{result: string}` — the `result` field is a YAML string containing all experiments.\n\nI need you to find ALL experiments matching these conditions across 4 model families. The exp_id naming patterns are:\n- Qwen-7B: `{condition}_seed{N}` (e.g., `exception_only_seed42`, `full_trace_seed42`)\n- DeepSeek-6.7B: `deepseek_{condition}_seed{N}`\n- CodeLlama-13B: `codellama13b_{condition}_seed{N}`\n- Qwen-1.5B: `qwen15b_{condition}_seed{N}` (NOT `qwen1.5b_*` which are killed)\n\nConditions needed: exception_only, ae_only, vota, loop_only, no_trace, full_trace, nomarker\n\nFor EACH matching experiment, I need:\n1. exp_id\n2. status (DONE, KILLED, etc.)\n3. accuracy (from metrics, usually `metrics.accuracy` or similar)\n4. seed\n5. Any notes about multi-seed means\n\n**Steps:**\n1. First probe the structure: `jq 'type, length, keys' file.txt` — then extract the `result` field and parse it.\n2. Use python to parse the YAML content and extract the needed experiments.\n3. Output a clean table with: exp_id | status | accuracy | seed | notes\n\nFocus especially on:\n- full_trace seeds (should be 81.76, 80.17, 82.35 → mean 81.43)\n- exception_only all models/seeds\n- DeepSeek VOTA (seed42=84.45 outlier)\n- ae_only Qwen-7B seeds (99.92/99.08/99.92)\n- loop_only Qwen-7B seeds (85.63/85.88/86.64)\n- no_trace all models\n- VOTA Qwen-7B seeds (99.41/98.66/99.08)\n\nBe thorough — extract every experiment that could appear in Table 1. Report the raw numbers verbatim from the registry.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2d564421-8464-4d87-ad0f-5e3eefeb24a0",
  "uuid": "62f6cb52-68ec-4467-9a26-f1eb2885394c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VqhjaEA2kDhdZ78QqniuK4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4129,
      "cache_read_input_tokens": 26269,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4129
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

### System

_source line 15_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a6431a7f8bfe3bb97",
  "tool_use_id": "toolu_015HUchPTe4989tKrwAwPKeH",
  "description": "Extract registry data for Table 1 audit",
  "task_type": "local_agent",
  "prompt": "I need you to extract specific experiment data from a large registry JSON file for a numerical audit. The file is at:\n`/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/2d564421-8464-4d87-ad0f-5e3eefeb24a0/tool-results/mcp-agent-ml-research-read_registry-1779392719783.txt`\n\nThe file is JSON with schema `{result: string}` — the `result` field is a YAML string containing all experiments.\n\nI need you to find ALL experiments matching these conditions across 4 model families. The exp_id naming patterns are:\n- Qwen-7B: `{condition}_seed{N}` (e.g., `exception_only_seed42`, `full_trace_seed42`)\n- DeepSeek-6.7B: `deepseek_{condition}_seed{N}`\n- CodeLlama-13B: `codellama13b_{condition}_seed{N}`\n- Qwen-1.5B: `qwen15b_{condition}_seed{N}` (NOT `qwen1.5b_*` which are killed)\n\nConditions needed: exception_only, ae_only, vota, loop_only, no_trace, full_trace, nomarker\n\nFor EACH matching experiment, I need:\n1. exp_id\n2. status (DONE, KILLED, etc.)\n3. accuracy (from metrics, usually `metrics.accuracy` or similar)\n4. seed\n5. Any notes about multi-seed means\n\n**Steps:**\n1. First probe the structure: `jq 'type, length, keys' file.txt` — then extract the `result` field and parse it.\n2. Use python to parse the YAML content and extract the needed experiments.\n3. Output a clean table with: exp_id | status | accuracy | seed | notes\n\nFocus especially on:\n- full_trace seeds (should be 81.76, 80.17, 82.35 → mean 81.43)\n- exception_only all models/seeds\n- DeepSeek VOTA (seed42=84.45 outlier)\n- ae_only Qwen-7B seeds (99.92/99.08/99.92)\n- loop_only Qwen-7B seeds (85.63/85.88/86.64)\n- no_trace all models\n- VOTA Qwen-7B seeds (99.41/98.66/99.08)\n\nBe thorough — extract every experiment that could appear in Table 1. Report the raw numbers verbatim from the registry.",
  "uuid": "fafe1b9c-f881-45b5-bd6d-0dbcca44bef4",
  "session_id": "2d564421-8464-4d87-ad0f-5e3eefeb24a0"
}
```

---

## Round 1

45 recorded events

### User

_source line 16 · 2026-05-21T19:45:44.312Z_

I need you to extract specific experiment data from a large registry JSON file for a numerical audit. The file is at:
`/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/2d564421-8464-4d87-ad0f-5e3eefeb24a0/tool-results/mcp-agent-ml-research-read_registry-1779392719783.txt`

The file is JSON with schema `{result: string}` — the `result` field is a YAML string containing all experiments.

I need you to find ALL experiments matching these conditions across 4 model families. The exp_id naming patterns are:
- Qwen-7B: `{condition}_seed{N}` (e.g., `exception_only_seed42`, `full_trace_seed42`)
- DeepSeek-6.7B: `deepseek_{condition}_seed{N}`
- CodeLlama-13B: `codellama13b_{condition}_seed{N}`
- Qwen-1.5B: `qwen15b_{condition}_seed{N}` (NOT `qwen1.5b_*` which are killed)

Conditions needed: exception_only, ae_only, vota, loop_only, no_trace, full_trace, nomarker

For EACH matching experiment, I need:
1. exp_id
2. status (DONE, KILLED, etc.)
3. accuracy (from metrics, usually `metrics.accuracy` or similar)
4. seed
5. Any notes about multi-seed means

**Steps:**
1. First probe the structure: `jq 'type, length, keys' file.txt` — then extract the `result` field and parse it.
2. Use python to parse the YAML content and extract the needed experiments.
3. Output a clean table with: exp_id | status | accuracy | seed | notes

Focus especially on:
- full_trace seeds (should be 81.76, 80.17, 82.35 → mean 81.43)
- exception_only all models/seeds
- DeepSeek VOTA (seed42=84.45 outlier)
- ae_only Qwen-7B seeds (99.92/99.08/99.92)
- loop_only Qwen-7B seeds (85.63/85.88/86.64)
- no_trace all models
- VOTA Qwen-7B seeds (99.41/98.66/99.08)

Be thorough — extract every experiment that could appear in Table 1. Report the raw numbers verbatim from the registry.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015HUchPTe4989tKrwAwPKeH",
  "session_id": "2d564421-8464-4d87-ad0f-5e3eefeb24a0",
  "uuid": "c1fe206f-4430-4fa0-b41c-373fc808c111"
}
```

</details>

---

### System

_source line 17_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a6431a7f8bfe3bb97",
  "tool_use_id": "toolu_015HUchPTe4989tKrwAwPKeH",
  "description": "Running Check file size",
  "usage": {
    "total_tokens": 15359,
    "tool_uses": 1,
    "duration_ms": 3988
  },
  "last_tool_name": "Bash",
  "uuid": "d2c6440d-a093-4555-8acb-8bc75fed9520",
  "session_id": "2d564421-8464-4d87-ad0f-5e3eefeb24a0"
}
```

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Bash · `toolu_01JXt7UCvL8mVHmeMQ7XyrUL`</summary>

```json
{
  "command": "wc -c /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/2d564421-8464-4d87-ad0f-5e3eefeb24a0/tool-results/mcp-agent-ml-research-read_registry-1779392719783.txt",
  "description": "Check file size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015HUchPTe4989tKrwAwPKeH",
  "session_id": "2d564421-8464-4d87-ad0f-5e3eefeb24a0",
  "uuid": "57cb4c87-3e25-4a57-a3af-b252a8b61dbc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Suc7y2GpVAJVgfqYitwrYn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15348,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15348,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 19 · 2026-05-21T19:45:48.446Z_

<details><summary>↩ Tool result · `toolu_01JXt7UCvL8mVHmeMQ7XyrUL`</summary>

```text
323997 /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/2d564421-8464-4d87-ad0f-5e3eefeb24a0/tool-results/mcp-agent-ml-research-read_registry-1779392719783.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015HUchPTe4989tKrwAwPKeH",
  "session_id": "2d564421-8464-4d87-ad0f-5e3eefeb24a0",
  "uuid": "df3f99c8-7b5a-4e9b-b5d2-c640d7553ec9"
}
```

</details>

---

### System

_source line 20_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a6431a7f8bfe3bb97",
  "tool_use_id": "toolu_015HUchPTe4989tKrwAwPKeH",
  "description": "Running Peek at file start",
  "usage": {
    "total_tokens": 15363,
    "tool_uses": 2,
    "duration_ms": 4961
  },
  "last_tool_name": "Bash",
  "uuid": "3e902ee5-7ede-4351-850b-7b89db18f83b",
  "session_id": "2d564421-8464-4d87-ad0f-5e3eefeb24a0"
}
```

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Bash · `toolu_018bgYNviBxs15JaDiR7Rqgf`</summary>

```json
{
  "command": "head -c 500 /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/2d564421-8464-4d87-ad0f-5e3eefeb24a0/tool-results/mcp-agent-ml-research-read_registry-1779392719783.txt",
  "description": "Peek at file start"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015HUchPTe4989tKrwAwPKeH",
  "session_id": "2d564421-8464-4d87-ad0f-5e3eefeb24a0",
  "uuid": "d9f12a29-e09e-439c-a7d9-b4222584280c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Suc7y2GpVAJVgfqYitwrYn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15348,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15348,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 22 · 2026-05-21T19:45:49.339Z_

<details><summary>↩ Tool result · `toolu_018bgYNviBxs15JaDiR7Rqgf`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"regex_nomarker_baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T19:03:04.213Z\", \"updated_at\": \"2026-05-21T19:03:23.905Z\", \"hypothesis\": \"Regex baselines (B1-B5) on nomarker condition will show significant degradation, especially B5 which relies on the [No exception data in trace] marker. This reveals the marker-condition B5=99.33% is a format artifact, not genuine code reasoning.\", \"conclus
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015HUchPTe4989tKrwAwPKeH",
  "session_id": "2d564421-8464-4d87-ad0f-5e3eefeb24a0",
  "uuid": "2b89b63c-3a7b-472c-b2fe-a5926b31994c"
}
```

</details>

---

### System

_source line 23_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a6431a7f8bfe3bb97",
  "tool_use_id": "toolu_015HUchPTe4989tKrwAwPKeH",
  "description": "Running Parse JSON and list all experiment IDs",
  "usage": {
    "total_tokens": 16855,
    "tool_uses": 3,
    "duration_ms": 11064
  },
  "last_tool_name": "Bash",
  "uuid": "847201bf-af0a-4c28-b38d-477cbe661cc3",
  "session_id": "2d564421-8464-4d87-ad0f-5e3eefeb24a0"
}
```

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Bash · `toolu_0113XH2j1fhJkiLSqf2Lwoor`</summary>

```json
{
  "command": "cd /tmp && python3 << 'PYEOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/2d564421-8464-4d87-ad0f-5e3eefeb24a0/tool-results/mcp-agent-ml-research-read_registry-1779392719783.txt\"\n\nwith open(fpath) as f:\n    outer = json.load(f)\n\n# result is a JSON string\ninner = json.loads(outer[\"result\"])\nprint(\"Top keys:\", list(inner.keys()))\nprint(\"success:\", inner.get(\"success\"))\ndata = inner.get(\"data\", {})\nprint(\"Data keys:\", list(data.keys()))\nexps = data.get(\"experiments\", {})\nprint(f\"Total experiments: {len(exps)}\")\nprint(\"\\nAll exp_ids:\")\nfor eid in sorted(exps.keys()):\n    print(f\"  {eid}\")\nPYEOF\n",
  "description": "Parse JSON and list all experiment IDs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015HUchPTe4989tKrwAwPKeH",
  "session_id": "2d564421-8464-4d87-ad0f-5e3eefeb24a0",
  "uuid": "ace27bb0-6838-49fa-bec2-c37fa6ff3776",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Qvvn3eYSmeUWbJnMo4o4n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1492,
      "cache_read_input_tokens": 15348,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1492,
        "ephemeral_1h_input_tokens": 0
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

_source line 25 · 2026-05-21T19:45:55.472Z_

<details><summary>↩ Tool result · `toolu_0113XH2j1fhJkiLSqf2Lwoor`</summary>

```text
Top keys: ['success', 'data', 'error', 'metadata']
success: True
Data keys: ['experiments', 'count', 'total', 'baseline']
Total experiments: 168

All exp_ids:
  ae_only_seed123
  ae_only_seed456
  calibration_analysis_seed42
  codellama13b_ae_only_seed123
  codellama13b_ae_only_seed42
  codellama13b_exception_only_seed123
  codellama13b_exception_only_seed42
  codellama13b_exception_only_seed456
  codellama13b_full_trace_head2048_seed42
  codellama13b_full_trace_tail1024_seed42
  codellama13b_full_trace_tail1024_seed42_v2
  codellama13b_full_trace_tail1024_seed42_v3
  codellama13b_full_trace_tail2048_seed42
  codellama13b_full_trace_tail2048_seed42_v2
  codellama13b_full_trace_tail2048_seed42_v3
  codellama13b_full_trace_tail256_seed42
  codellama13b_full_trace_tail384_seed42
  codellama13b_full_trace_tail512_seed123
  codellama13b_full_trace_tail512_seed42
  codellama13b_full_trace_tail512_seed456
  codellama13b_label_only_seed123_v2
  codellama13b_label_only_seed42
  codellama13b_label_only_seed42_v2
  codellama13b_loop_only_seed123
  codellama13b_loop_only_seed42
  codellama13b_loop_only_seed456
  codellama13b_no_trace_seed42
  codellama13b_nomarker_seed42
  codellama13b_vota_seed123
  codellama13b_vota_seed42
  codellama_exception_only_seed42
  codellama_no_trace_seed42
  codellama_vota_seed42
  cross_model_calibration
  cross_model_calibration_eval
  debugbench_exception_bug_fix
  debugbench_exception_only_seed42
  debugbench_no_trace_seed42
  debugbench_vota_seed42
  deepseek_ae_only_seed123
  deepseek_ae_only_seed42
  deepseek_exception_only_seed123
  deepseek_exception_only_seed123_v2
  deepseek_exception_only_seed42
  deepseek_exception_only_seed456
  deepseek_full_trace_head2048_seed42
  deepseek_full_trace_seed42
  deepseek_full_trace_seed42_v2
  deepseek_full_trace_seed42_v3
  deepseek_full_trace_tail1024_seed42
  deepseek_full_trace_tail2048_seed42
  deepseek_full_trace_tail256_seed42
  deepseek_full_trace_tail384_seed42
  deepseek_full_trace_tail512_seed123
  deepseek_full_trace_tail512_seed123_v2
  deepseek_full_trace_tail512_seed42
  deepseek_full_trace_tail512_seed456
  deepseek_label_only_seed42
  deepseek_loop_only_seed123
  deepseek_loop_only_seed42
  deepseek_loop_only_seed456
  deepseek_no_trace_seed123
  deepseek_no_trace_seed42
  deepseek_vota_seed123
  deepseek_vota_seed42
  deepseek_vota_seed456
  eval_missing_predictions_batch
  eval_missing_predictions_batch_v2
  exception_only_nomarker_seed123
  exception_only_nomarker_seed42
  exception_only_nomarker_seed456
  exception_only_padded2048_seed42
  exception_only_seed123
  exception_only_seed456
  fewshot_gpt41_exception_only_0shot
  fewshot_gpt41_exception_only_3shot
  fewshot_gpt41_no_trace_0shot
  fewshot_gpt4o_exception_only_0shot
  fewshot_gpt4o_exception_only_3shot
  fewshot_gpt4o_no_trace_0shot
  fewshot_qwen7b_exception_only
  full_trace_1024tok_seed42
  full_trace_2048tok_seed42
  full_trace_256tok_seed42
  full_trace_512tok_seed42
  full_trace_label_only_seed42
  full_trace_seed42
  full_trace_seed42_v2
  full_trace_seed42_v5
  full_trace_tail256_seed42
  full_trace_tail_1024_seed42
  full_trace_tail_256_seed42
  full_trace_tail_512_seed42
  full_trace_tail_seed42
  label_only_seed123
  label_only_seed456
  loop_only_seed123
  loop_only_seed456
  no_trace_seed42
  no_trace_seed42_v2
  no_trace_seed42_v3
  no_trace_seed42_v4
  no_trace_seed42_v5
  qwen1.5b_exception_only_seed42
  qwen1.5b_full_trace_seed42
  qwen1.5b_no_trace_seed42
  qwen1.5b_vota_seed42
  qwen15b_ae_only_seed123
  qwen15b_ae_only_seed42
  qwen15b_exception_only_seed123
  qwen15b_exception_only_seed123_v2
  qwen15b_exception_only_seed42
  qwen15b_exception_only_seed456
  qwen15b_full_trace_head2048_seed42
  qwen15b_full_trace_seed42
  qwen15b_full_trace_tail1024_seed42
  qwen15b_full_trace_tail2048_seed42
  qwen15b_full_trace_tail256_seed42
  qwen15b_full_trace_tail384_seed42
  qwen15b_full_trace_tail512_seed123
  qwen15b_full_trace_tail512_seed42
  qwen15b_full_trace_tail512_seed456
  qwen15b_label_only_seed123_v2
  qwen15b_label_only_seed42
  qwen15b_label_only_seed42_v2
  qwen15b_label_only_seed456_v2
  qwen15b_loop_only_seed123
  qwen15b_loop_only_seed42
  qwen15b_loop_only_seed456
  qwen15b_no_trace_seed123
  qwen15b_no_trace_seed42
  qwen15b_no_trace_seed456
  qwen15b_nomarker_seed42
  qwen15b_vota_seed123
  qwen15b_vota_seed42
  qwen7b_exception_only_dynamics_seed42
  qwen7b_full_trace_dynamics_seed42
  qwen7b_full_trace_head2048_seed42
  qwen7b_full_trace_label_only_seed123
  qwen7b_full_trace_label_only_seed456
  qwen7b_full_trace_seed123
  qwen7b_full_trace_seed456
  qwen7b_full_trace_seed456_v2
  qwen7b_full_trace_tail384_seed42
  qwen7b_full_trace_tail512_seed123
  qwen7b_full_trace_tail512_seed42
  qwen7b_full_trace_tail512_seed456
  qwen7b_vota_seed123
  qwen7b_vota_seed456
  regex_baseline_analysis
  regex_nomarker_baseline
  vota_ae_only_seed42
  vota_exception_only_seed42
  vota_exception_only_seed42_v2
  vota_loop_only_seed42
  vota_no_ae_seed42
  vota_seed123
  vota_seed42
  vota_seed42_v2
  vota_seed42_v3
  vota_seed42_v4
  vota_seed42_v5
  vota_seed456
  vota_seed456_v2
  zeroshot_codellama13b_exception_only
  zeroshot_deepseek7b_exception_only
  zeroshot_qwen15b_exception_only
  zeroshot_qwen7b_exception_only
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015HUchPTe4989tKrwAwPKeH",
  "session_id": "2d564421-8464-4d87-ad0f-5e3eefeb24a0",
  "uuid": "7e2826e4-1c5f-4a11-b7a5-abc7ad2ca0a7"
}
```

</details>

---

### System

_source line 26_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a6431a7f8bfe3bb97",
  "tool_use_id": "toolu_015HUchPTe4989tKrwAwPKeH",
  "description": "Running Classify and extract all Table 1 experiments",
  "usage": {
    "total_tokens": 19510,
    "tool_uses": 4,
    "duration_ms": 36271
  },
  "last_tool_name": "Bash",
  "uuid": "76ba603a-45a8-4722-a52f-5b376e4be9f7",
  "session_id": "2d564421-8464-4d87-ad0f-5e3eefeb24a0"
}
```

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Bash · `toolu_01Tw6LYE83RCK1SpquiudVXd`</summary>

```json
{
  "command": "cd /tmp && python3 << 'PYEOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/2d564421-8464-4d87-ad0f-5e3eefeb24a0/tool-results/mcp-agent-ml-research-read_registry-1779392719783.txt\"\n\nwith open(fpath) as f:\n    outer = json.load(f)\n\ninner = json.loads(outer[\"result\"])\nexps = inner[\"data\"][\"experiments\"]\n\n# Define which exp_ids belong to Table 1 conditions\n# We need: exception_only, ae_only, vota, loop_only, no_trace, full_trace, nomarker\n# For 4 model families\n\nconditions = [\"exception_only\", \"ae_only\", \"vota\", \"loop_only\", \"no_trace\", \"full_trace\", \"nomarker\"]\n\n# Qwen-7B patterns (no prefix, or qwen7b_ prefix for some)\n# DeepSeek-6.7B: deepseek_\n# CodeLlama-13B: codellama13b_\n# Qwen-1.5B: qwen15b_ (not qwen1.5b_)\n\ndef extract_seed(eid):\n    \"\"\"Extract seed number from exp_id\"\"\"\n    import re\n    m = re.search(r'seed(\\d+)', eid)\n    return int(m.group(1)) if m else None\n\ndef extract_accuracy(exp):\n    \"\"\"Extract accuracy from experiment metrics\"\"\"\n    metrics = exp.get(\"metrics\", {})\n    if not metrics:\n        return None\n    # Check various possible keys\n    for key in [\"accuracy\", \"eval_accuracy\", \"test_accuracy\"]:\n        if key in metrics:\n            return metrics[key]\n    # Sometimes nested\n    if isinstance(metrics, dict):\n        for k, v in metrics.items():\n            if \"accuracy\" in str(k).lower() and isinstance(v, (int, float)):\n                return v\n    return None\n\ndef get_notes(exp):\n    \"\"\"Get any notes\"\"\"\n    notes = exp.get(\"notes\", \"\")\n    conclusion = exp.get(\"conclusion\", \"\")\n    parts = []\n    if notes:\n        parts.append(str(notes)[:100])\n    if conclusion:\n        parts.append(str(conclusion)[:100])\n    return \" | \".join(parts) if parts else \"\"\n\n# Group experiments by model family and condition\n# First, let's identify ALL relevant experiments\n\n# Qwen-7B base conditions (no model prefix)\nqwen7b_base = {\n    \"exception_only\": [\"exception_only_seed123\", \"exception_only_seed456\"],  # seed42 might be named differently\n    \"ae_only\": [\"ae_only_seed123\", \"ae_only_seed456\"],\n    \"vota\": [\"vota_seed42\", \"vota_seed123\", \"vota_seed456\"],\n    \"loop_only\": [\"loop_only_seed123\", \"loop_only_seed456\"],\n    \"no_trace\": [\"no_trace_seed42\"],\n    \"full_trace\": [\"full_trace_seed42\"],\n    \"nomarker\": [],\n}\n\n# Let me just scan ALL experiments and classify them\nprint(\"=\" * 140)\nprint(f\"{'exp_id':<55} {'status':<10} {'accuracy':>10} {'seed':>6} {'notes'}\")\nprint(\"=\" * 140)\n\n# Sort by model family then condition\ndef classify(eid):\n    if eid.startswith(\"deepseek_\"):\n        model = \"DeepSeek-6.7B\"\n        rest = eid[len(\"deepseek_\"):]\n    elif eid.startswith(\"codellama13b_\"):\n        model = \"CodeLlama-13B\"\n        rest = eid[len(\"codellama13b_\"):]\n    elif eid.startswith(\"qwen15b_\"):\n        model = \"Qwen-1.5B\"\n        rest = eid[len(\"qwen15b_\"):]\n    elif eid.startswith(\"qwen1.5b_\"):\n        model = \"Qwen-1.5B-KILLED\"\n        rest = eid[len(\"qwen1.5b_\"):]\n    elif eid.startswith(\"qwen7b_\"):\n        model = \"Qwen-7B\"\n        rest = eid[len(\"qwen7b_\"):]\n    else:\n        model = \"Qwen-7B\"\n        rest = eid\n    return model, rest\n\n# Filter to relevant conditions\nrelevant = []\nfor eid, exp in exps.items():\n    model, rest = classify(eid)\n    \n    # Check if this matches a Table 1 condition\n    matched_cond = None\n    for cond in conditions:\n        # Must match condition at start of rest, followed by _seed or _nomarker etc\n        if rest.startswith(cond + \"_seed\") or rest == cond + \"_seed42\" or rest.startswith(cond + \"_seed\"):\n            matched_cond = cond\n            break\n        # Also check exact patterns like \"vota_seed42_v2\" etc\n        if rest.startswith(cond + \"_seed\"):\n            matched_cond = cond\n            break\n    \n    # Special: some Qwen-7B experiments have qwen7b_ prefix\n    if matched_cond or any(rest.startswith(c) for c in conditions):\n        seed = extract_seed(eid)\n        acc = extract_accuracy(exp)\n        status = exp.get(\"status\", \"UNKNOWN\")\n        notes = get_notes(exp)\n        relevant.append((model, rest, eid, status, acc, seed, notes))\n\n# Sort by model, then condition\nrelevant.sort(key=lambda x: (x[0], x[1]))\n\ncurrent_model = None\nfor model, rest, eid, status, acc, seed, notes in relevant:\n    if model != current_model:\n        print(f\"\\n--- {model} ---\")\n        current_model = model\n    acc_str = f\"{acc}\" if acc is not None else \"N/A\"\n    seed_str = str(seed) if seed else \"?\"\n    # Truncate notes\n    notes_short = notes[:80] if notes else \"\"\n    print(f\"  {eid:<53} {status:<10} {acc_str:>10} {seed_str:>6}  {notes_short}\")\n\nPYEOF\n",
  "description": "Classify and extract all Table 1 experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015HUchPTe4989tKrwAwPKeH",
  "session_id": "2d564421-8464-4d87-ad0f-5e3eefeb24a0",
  "uuid": "621b9170-4b08-4bbd-9957-c5fbdeed352b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0145aY39PoAurZYPzfbPdYrr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2653,
      "cache_read_input_tokens": 16840,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2653,
        "ephemeral_1h_input_tokens": 0
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

_source line 28 · 2026-05-21T19:46:20.713Z_

<details><summary>↩ Tool result · `toolu_01Tw6LYE83RCK1SpquiudVXd`</summary>

```text
============================================================================================================================================
exp_id                                                  status       accuracy   seed notes
============================================================================================================================================

--- CodeLlama-13B ---
  codellama13b_ae_only_seed123                          DONE           0.9908    123  success
  codellama13b_ae_only_seed42                           DONE           0.9908     42  success
  codellama13b_exception_only_seed123                   DONE                1    123  success
  codellama13b_exception_only_seed42                    DONE           0.9983     42  success
  codellama13b_exception_only_seed456                   DONE           0.9983    456  success
  codellama13b_full_trace_head2048_seed42               DONE           0.7992     42  success
  codellama13b_full_trace_tail1024_seed42               DONE              N/A     42  failed
  codellama13b_full_trace_tail1024_seed42_v2            DONE            0.876     42  negative
  codellama13b_full_trace_tail1024_seed42_v3            DONE           0.9824     42  success
  codellama13b_full_trace_tail2048_seed42               DONE              N/A     42  failed
  codellama13b_full_trace_tail2048_seed42_v2            DONE           0.2849     42  negative
  codellama13b_full_trace_tail2048_seed42_v3            DONE            0.071     42  negative
  codellama13b_full_trace_tail256_seed42                DONE            0.779     42  success
  codellama13b_full_trace_tail384_seed42                DONE           0.8269     42  negative
  codellama13b_full_trace_tail512_seed123               DONE           0.9824    123  success
  codellama13b_full_trace_tail512_seed42                DONE           0.9824     42  success
  codellama13b_full_trace_tail512_seed456               DONE           0.9824    456  success
  codellama13b_loop_only_seed123                        DONE           0.7605    123  success
  codellama13b_loop_only_seed42                         DONE           0.7706     42  negative
  codellama13b_loop_only_seed456                        DONE           0.7908    456  success
  codellama13b_no_trace_seed42                          DONE            0.765     42  success
  codellama13b_nomarker_seed42                          DONE              N/A     42  Cancelled by Director: model weights cleaned from disk, not worth re-downloading
  codellama13b_vota_seed123                             DONE           0.9891    123  success
  codellama13b_vota_seed42                              DONE           0.9857     42  success

--- DeepSeek-6.7B ---
  deepseek_ae_only_seed123                              DONE           0.9832    123  success
  deepseek_ae_only_seed42                               DONE           0.9874     42  success
  deepseek_exception_only_seed123                       DONE              N/A    123  NEGATIVE: accuracy 91.09% vs seed42 99.83% (-8.74pp). fail_recall=0.705, train_l
  deepseek_exception_only_seed123_v2                    DONE            0.995    123  success
  deepseek_exception_only_seed42                        DONE           0.9933     42  epoch 1 (step 148) accuracy = 99.83%，高于 final (epoch 3) 的 99.33%。eval_loss epoch
  deepseek_exception_only_seed456                       DONE           0.9933    456  seed456 accuracy 99.33% = seed42 99.33%（完全一致）。seed123 (91.09%) 是离群值——2/3 seeds 在
  deepseek_full_trace_head2048_seed42                   DONE            0.787     42  success
  deepseek_full_trace_seed42                            DONE           0.2849     42  INVALIDATED: train-eval truncation mismatch。旧 eval (无截断): 28.49% (all predict fa
  deepseek_full_trace_seed42_v2                         DONE              N/A     42  Killed by worker_ops_kill_and_submit_vota_seed456 to free cuda:1 for vota_seed45
  deepseek_full_trace_seed42_v3                         DONE           0.7916     42  DeepSeek full_trace v3: label-preserving truncation fix. 79.16% confirmed with m
  deepseek_full_trace_tail1024_seed42                   DONE           0.9647     42  success
  deepseek_full_trace_tail2048_seed42                   DONE           0.9496     42  success
  deepseek_full_trace_tail256_seed42                    DONE           0.7639     42  success
  deepseek_full_trace_tail384_seed42                    DONE            0.807     42  success
  deepseek_full_trace_tail512_seed123                   DONE              N/A    123  failed
  deepseek_full_trace_tail512_seed123_v2                DONE           0.9504    123  success
  deepseek_full_trace_tail512_seed42                    DONE            0.939     42  success
  deepseek_full_trace_tail512_seed456                   DONE           0.9605    456  success
  deepseek_loop_only_seed123                            DONE           0.8126    123  success
  deepseek_loop_only_seed42                             DONE           0.8126     42  success
  deepseek_loop_only_seed456                            DONE            0.784    456  success
  deepseek_no_trace_seed123                             DONE              N/A    123  killed
  deepseek_no_trace_seed42                              DONE           0.7336     42  Negative: lift +1.85pp over majority, 95% CI [-0.93, +4.63] crosses 0. DeepSeek-
  deepseek_vota_seed123                                 DONE           0.9916    123  success
  deepseek_vota_seed42                                  DONE           0.8445     42  DeepSeek VOTA: 84.45% confirmed with max_length=16384 (re-verified 2026-05-16, e
  deepseek_vota_seed456                                 DONE           0.9933    456  success

--- Qwen-1.5B ---
  qwen15b_ae_only_seed123                               DONE           0.9857    123  success
  qwen15b_ae_only_seed42                                DONE           0.9908     42  success
  qwen15b_exception_only_seed123                        DONE              N/A    123  failed
  qwen15b_exception_only_seed123_v2                     DONE           0.9983    123  success
  qwen15b_exception_only_seed42                         DONE           0.9983     42  success
  qwen15b_exception_only_seed456                        DONE           0.9983    456  success
  qwen15b_full_trace_head2048_seed42                    DONE           0.7529     42  success
  qwen15b_full_trace_seed42                             DONE           0.7706     42  success
  qwen15b_full_trace_tail1024_seed42                    DONE            0.966     42  success
  qwen15b_full_trace_tail2048_seed42                    DONE            0.979     42  success
  qwen15b_full_trace_tail256_seed42                     DONE            0.726     42  negative
  qwen15b_full_trace_tail384_seed42                     DONE           0.7361     42  negative
  qwen15b_full_trace_tail512_seed123                    DONE           0.9765    123  success
  qwen15b_full_trace_tail512_seed42                     DONE            0.956     42  success
  qwen15b_full_trace_tail512_seed456                    DONE           0.9672    456  success
  qwen15b_loop_only_seed123                             DONE           0.8109    123  success
  qwen15b_loop_only_seed42                              DONE           0.7832     42  success
  qwen15b_loop_only_seed456                             DONE            0.792    456  success
  qwen15b_no_trace_seed123                              DONE           0.7588    123  success
  qwen15b_no_trace_seed42                               DONE           0.6731     42  success
  qwen15b_no_trace_seed456                              DONE           0.7387    456  success
  qwen15b_nomarker_seed42                               DONE            0.978     42  success
  qwen15b_vota_seed123                                  DONE            0.995    123  success
  qwen15b_vota_seed42                                   DONE           0.9958     42  success

--- Qwen-1.5B-KILLED ---
  qwen1.5b_exception_only_seed42                        DONE              N/A     42  重复条目，已在 qwen15b_exception_only_seed42 (99.83%) 完成。命名差异：qwen1.5b_ → qwen15b_ | ki
  qwen1.5b_full_trace_seed42                            DONE              N/A     42  重复条目，已在 qwen15b_full_trace_seed42 (77.06%) 完成。命名差异：qwen1.5b_ → qwen15b_ | killed
  qwen1.5b_no_trace_seed42                              DONE           0.7261     42  Eval completed 2026-05-21. Accuracy 72.6% (vs qwen15b_no_trace_seed42 67.31%, +5
  qwen1.5b_vota_seed42                                  DONE              N/A     42  重复条目，已在 qwen15b_vota_seed42 (99.58%) 完成。命名差异：qwen1.5b_ → qwen15b_ | killed

--- Qwen-7B ---
  ae_only_seed123                                       DONE           0.9908    123  Cron 误判为 failed（进程死亡 5× 无 sentinel/W&B），Reviewer 独立核实训练+eval 均成功完成。accuracy=99.0
  ae_only_seed456                                       DONE           0.9992    456  success
  qwen7b_exception_only_dynamics_seed42                 DONE              N/A     42  success
  exception_only_nomarker_seed123                       DONE           0.9832    123  success
  exception_only_nomarker_seed42                        DONE           0.9655     42  success
  exception_only_nomarker_seed456                       DONE           0.9807    456  success
  exception_only_padded2048_seed42                      RUNNING           N/A     42  
  exception_only_seed123                                DONE           0.9983    123  Seed robustness 结论: exception_only 99.83% ± 0.00 (seeds 42/123/456), 每 seed 恰好 2
  exception_only_seed456                                DONE           0.9983    456  Seed robustness 结论: exception_only 99.83% ± 0.00 (seeds 42/123/456), 每 seed 恰好 2
  full_trace_1024tok_seed42                             DONE           0.7723     42  negative
  full_trace_2048tok_seed42                             DONE              N/A     42  Director 取消：max_trace_tokens=2048 经 chat template overhead 后有效 trace ~1970 tok，与
  full_trace_256tok_seed42                              DONE           0.7882     42  negative
  full_trace_512tok_seed42                              DONE           0.8042     42  negative
  qwen7b_full_trace_dynamics_seed42                     DONE              N/A     42  success
  qwen7b_full_trace_head2048_seed42                     DONE            0.816     42  success
  qwen7b_full_trace_label_only_seed123                  DONE           0.8689    123  success
  full_trace_label_only_seed42                          DONE           0.8622     42  Label-only loss 将 full_trace 从 81.8% 提升到 86.2% (+4.4pp)，确认 gradient dilution 是 f
  qwen7b_full_trace_label_only_seed456                  DONE            0.847    456  success
  qwen7b_full_trace_seed123                             DONE            0.802    123  success
  full_trace_seed42                                     DONE            0.284     42  killed
  full_trace_seed42_v2                                  DONE            0.284     42  negative
  full_trace_seed42_v5                                  DONE           0.8176     42  ✅ Paired bootstrap CI (2026-05-15): lift vs no_trace = +6.6pp [4.4, 9.0]pp (sign
  qwen7b_full_trace_seed456                             DONE              N/A    456  failed
  qwen7b_full_trace_seed456_v2                          DONE           0.8235    456  success
  full_trace_tail256_seed42                             DONE            0.789     42  negative
  qwen7b_full_trace_tail384_seed42                      DONE            0.798     42  success
  qwen7b_full_trace_tail512_seed123                     DONE           0.9597    123  success
  qwen7b_full_trace_tail512_seed42                      DONE              N/A     42  failed
  qwen7b_full_trace_tail512_seed456                     DONE           0.9765    456  success
  full_trace_tail_1024_seed42                           DONE           0.9647     42  success
  full_trace_tail_256_seed42                            DONE           0.7748     42  negative
  full_trace_tail_512_seed42                            DONE            0.936     42  success
  full_trace_tail_seed42                                DONE            0.973     42  success
  loop_only_seed123                                     DONE           0.8588    123  Loop_only seed robustness 完成: seed42=85.63%, seed123=85.88%, seed456=86.64%. Mea
  loop_only_seed456                                     DONE           0.8664    456  Loop_only seed robustness 完成: seed42=85.63%, seed123=85.88%, seed456=86.64%. Mea
  no_trace_seed42                                       DONE              N/A     42  killed
  no_trace_seed42_v2                                    DONE              N/A     42  killed
  no_trace_seed42_v3                                    DONE           0.7513     42  killed
  no_trace_seed42_v4                                    DONE           0.7513     42  success
  no_trace_seed42_v5                                    DONE           0.7513     42  success
  vota_ae_only_seed42                                   DONE           0.9992     42  ae_only accuracy 99.92% [99.75%, 100%]。与 exception_only (99.83%) 统计等价，均为 Tier 1 
  vota_exception_only_seed42                            DONE              N/A     42  failed
  vota_exception_only_seed42_v2                         DONE           0.9983     42  Seed robustness confirmed: exception_only 99.83% ± 0.00 across seeds 42/123/456.
  vota_loop_only_seed42                                 DONE           0.8563     42  [2026-05-15 re-eval] 用修复后 evaluate.py 重跑，accuracy 不变 (85.63% → 85.63%, Δ=0)，pred
  vota_no_ae_seed42                                     DONE            0.994     42  ✅ Eval verified: accuracy 99.4% [98.9, 99.8] confirmed by evaluate.py + bootstra
  qwen7b_vota_seed123                                   DONE           0.9866    123  success
  vota_seed123                                          DONE              N/A    123  failed
  vota_seed42                                           DONE              N/A     42  killed
  vota_seed42_v2                                        DONE              N/A     42  killed
  vota_seed42_v3                                        DONE            0.992     42  killed
  vota_seed42_v4                                        DONE           0.9563     42  success
  vota_seed42_v5                                        DONE           0.9941     42  success
  qwen7b_vota_seed456                                   DONE           0.9908    456  success
  vota_seed456                                          DONE              N/A    456  Original PID 145908 OOM'd ~3min after start. Auto-retried as v2 (PID 146592) wit
  vota_seed456_v2                                       DONE           0.9908    456  Auto-retried from vota_seed456 (OOM). PID 146592, cuda:1, --gradient_checkpointi
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015HUchPTe4989tKrwAwPKeH",
  "session_id": "2d564421-8464-4d87-ad0f-5e3eefeb24a0",
  "uuid": "a70e0cfd-e4a5-4aa6-864d-2702041c53e2"
}
```

</details>

---

### System

_source line 29_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a6431a7f8bfe3bb97",
  "tool_use_id": "toolu_015HUchPTe4989tKrwAwPKeH",
  "description": "Running Full extraction with summary table and cross-checks",
  "usage": {
    "total_tokens": 25767,
    "tool_uses": 5,
    "duration_ms": 135008
  },
  "last_tool_name": "Bash",
  "uuid": "201abab2-56c1-4306-81ad-5241a1070d72",
  "session_id": "2d564421-8464-4d87-ad0f-5e3eefeb24a0"
}
```

---

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — Bash · `toolu_01Eh8UENEd4Pb1er5qWC6CrR`</summary>

```json
{
  "command": "cd /tmp && python3 << 'PYEOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/2d564421-8464-4d87-ad0f-5e3eefeb24a0/tool-results/mcp-agent-ml-research-read_registry-1779392719783.txt\"\n\nwith open(fpath) as f:\n    outer = json.load(f)\ninner = json.loads(outer[\"result\"])\nexps = inner[\"data\"][\"experiments\"]\n\ndef get_acc(eid):\n    \"\"\"Get accuracy as percentage\"\"\"\n    e = exps.get(eid)\n    if not e:\n        return None\n    m = e.get(\"metrics\", {})\n    if not m:\n        return None\n    a = m.get(\"accuracy\")\n    if a is None:\n        return None\n    return round(a * 100, 2)\n\ndef get_status(eid):\n    e = exps.get(eid)\n    return e.get(\"status\", \"???\") if e else \"MISSING\"\n\ndef get_notes(eid, max_len=120):\n    e = exps.get(eid)\n    if not e:\n        return \"\"\n    n = e.get(\"notes\", \"\") or \"\"\n    c = e.get(\"conclusion\", \"\") or \"\"\n    txt = f\"{n} | {c}\" if c else n\n    return txt[:max_len]\n\nprint(\"=\" * 160)\nprint(\"NUMERICAL AUDIT: All Table 1 experiments from registry\")\nprint(\"=\" * 160)\n\n# ============================================================\n# QWEN-7B\n# ============================================================\nprint(\"\\n\" + \"=\" * 80)\nprint(\"QWEN-7B (Qwen2.5-7B-Instruct)\")\nprint(\"=\" * 80)\n\nprint(\"\\n--- exception_only ---\")\nfor eid in [\"vota_exception_only_seed42_v2\", \"exception_only_seed123\", \"exception_only_seed456\"]:\n    print(f\"  {eid:<50} status={get_status(eid):<8} acc={get_acc(eid)}\")\nprint(f\"  => seeds: 42={get_acc('vota_exception_only_seed42_v2')}, 123={get_acc('exception_only_seed123')}, 456={get_acc('exception_only_seed456')}\")\naccs = [get_acc('vota_exception_only_seed42_v2'), get_acc('exception_only_seed123'), get_acc('exception_only_seed456')]\naccs = [a for a in accs if a is not None]\nif accs:\n    print(f\"  => mean = {sum(accs)/len(accs):.2f}\")\n\nprint(\"\\n--- ae_only ---\")\nfor eid in [\"vota_ae_only_seed42\", \"ae_only_seed123\", \"ae_only_seed456\"]:\n    print(f\"  {eid:<50} status={get_status(eid):<8} acc={get_acc(eid)}\")\naccs = [get_acc('vota_ae_only_seed42'), get_acc('ae_only_seed123'), get_acc('ae_only_seed456')]\naccs = [a for a in accs if a is not None]\nif accs:\n    print(f\"  => seeds: 42={get_acc('vota_ae_only_seed42')}, 123={get_acc('ae_only_seed123')}, 456={get_acc('ae_only_seed456')}\")\n    print(f\"  => mean = {sum(accs)/len(accs):.2f}\")\n\nprint(\"\\n--- vota ---\")\n# vota_seed42_v5 is the canonical seed42\nfor eid in [\"vota_seed42_v5\", \"qwen7b_vota_seed123\", \"qwen7b_vota_seed456\"]:\n    print(f\"  {eid:<50} status={get_status(eid):<8} acc={get_acc(eid)}\")\naccs = [get_acc('vota_seed42_v5'), get_acc('qwen7b_vota_seed123'), get_acc('qwen7b_vota_seed456')]\naccs = [a for a in accs if a is not None]\nif accs:\n    print(f\"  => seeds: 42={get_acc('vota_seed42_v5')}, 123={get_acc('qwen7b_vota_seed123')}, 456={get_acc('qwen7b_vota_seed456')}\")\n    print(f\"  => mean = {sum(accs)/len(accs):.2f}\")\n\nprint(\"\\n  Also: vota_no_ae_seed42 (VOTA minus AE):\")\nprint(f\"    vota_no_ae_seed42: acc={get_acc('vota_no_ae_seed42')}\")\n\nprint(\"\\n--- loop_only ---\")\nfor eid in [\"vota_loop_only_seed42\", \"loop_only_seed123\", \"loop_only_seed456\"]:\n    print(f\"  {eid:<50} status={get_status(eid):<8} acc={get_acc(eid)}\")\naccs = [get_acc('vota_loop_only_seed42'), get_acc('loop_only_seed123'), get_acc('loop_only_seed456')]\naccs = [a for a in accs if a is not None]\nif accs:\n    print(f\"  => seeds: 42={get_acc('vota_loop_only_seed42')}, 123={get_acc('loop_only_seed123')}, 456={get_acc('loop_only_seed456')}\")\n    print(f\"  => mean = {sum(accs)/len(accs):.2f}\")\n\nprint(\"\\n--- full_trace ---\")\nfor eid in [\"full_trace_seed42_v5\", \"qwen7b_full_trace_seed123\", \"qwen7b_full_trace_seed456_v2\"]:\n    print(f\"  {eid:<50} status={get_status(eid):<8} acc={get_acc(eid)}\")\naccs = [get_acc('full_trace_seed42_v5'), get_acc('qwen7b_full_trace_seed123'), get_acc('qwen7b_full_trace_seed456_v2')]\naccs = [a for a in accs if a is not None]\nif accs:\n    print(f\"  => seeds: 42={get_acc('full_trace_seed42_v5')}, 123={get_acc('qwen7b_full_trace_seed123')}, 456={get_acc('qwen7b_full_trace_seed456_v2')}\")\n    print(f\"  => mean = {sum(accs)/len(accs):.2f}\")\n\nprint(\"\\n  Older/invalidated full_trace runs:\")\nfor eid in [\"full_trace_seed42\", \"full_trace_seed42_v2\"]:\n    print(f\"    {eid:<48} status={get_status(eid):<8} acc={get_acc(eid)}  notes: {get_notes(eid, 80)}\")\n\nprint(\"\\n--- no_trace ---\")\nfor eid in [\"no_trace_seed42_v4\", \"no_trace_seed42_v5\"]:\n    print(f\"  {eid:<50} status={get_status(eid):<8} acc={get_acc(eid)}\")\nprint(f\"  NOTE: Only seed42 available for Qwen-7B no_trace. Canonical = no_trace_seed42_v4 or v5 = {get_acc('no_trace_seed42_v5')}\")\n\nprint(\"\\n--- nomarker ---\")\nfor eid in [\"exception_only_nomarker_seed42\", \"exception_only_nomarker_seed123\", \"exception_only_nomarker_seed456\"]:\n    print(f\"  {eid:<50} status={get_status(eid):<8} acc={get_acc(eid)}\")\naccs = [get_acc('exception_only_nomarker_seed42'), get_acc('exception_only_nomarker_seed123'), get_acc('exception_only_nomarker_seed456')]\naccs = [a for a in accs if a is not None]\nif accs:\n    print(f\"  => seeds: 42={get_acc('exception_only_nomarker_seed42')}, 123={get_acc('exception_only_nomarker_seed123')}, 456={get_acc('exception_only_nomarker_seed456')}\")\n    print(f\"  => mean = {sum(accs)/len(accs):.2f}\")\n\n\n# ============================================================\n# DEEPSEEK-6.7B\n# ============================================================\nprint(\"\\n\" + \"=\" * 80)\nprint(\"DEEPSEEK-6.7B (DeepSeek-Coder-6.7B-Instruct)\")\nprint(\"=\" * 80)\n\nprint(\"\\n--- exception_only ---\")\nfor eid in [\"deepseek_exception_only_seed42\", \"deepseek_exception_only_seed123_v2\", \"deepseek_exception_only_seed456\"]:\n    print(f\"  {eid:<50} status={get_status(eid):<8} acc={get_acc(eid)}\")\n# Also show the failed seed123\nprint(f\"  deepseek_exception_only_seed123 (FAILED):       acc={get_acc('deepseek_exception_only_seed123')}  notes: {get_notes('deepseek_exception_only_seed123', 80)}\")\naccs = [get_acc('deepseek_exception_only_seed42'), get_acc('deepseek_exception_only_seed123_v2'), get_acc('deepseek_exception_only_seed456')]\naccs = [a for a in accs if a is not None]\nif accs:\n    print(f\"  => seeds: 42={get_acc('deepseek_exception_only_seed42')}, 123(v2)={get_acc('deepseek_exception_only_seed123_v2')}, 456={get_acc('deepseek_exception_only_seed456')}\")\n    print(f\"  => mean = {sum(accs)/len(accs):.2f}\")\n\nprint(\"\\n--- ae_only ---\")\nfor eid in [\"deepseek_ae_only_seed42\", \"deepseek_ae_only_seed123\"]:\n    print(f\"  {eid:<50} status={get_status(eid):<8} acc={get_acc(eid)}\")\naccs = [get_acc('deepseek_ae_only_seed42'), get_acc('deepseek_ae_only_seed123')]\naccs = [a for a in accs if a is not None]\nif accs:\n    print(f\"  => seeds: 42={get_acc('deepseek_ae_only_seed42')}, 123={get_acc('deepseek_ae_only_seed123')}\")\n    print(f\"  NOTE: Only 2 seeds available\")\n\nprint(\"\\n--- vota ---\")\nfor eid in [\"deepseek_vota_seed42\", \"deepseek_vota_seed123\", \"deepseek_vota_seed456\"]:\n    print(f\"  {eid:<50} status={get_status(eid):<8} acc={get_acc(eid)}\")\n    if eid == \"deepseek_vota_seed42\":\n        print(f\"    *** OUTLIER: {get_acc(eid)}% — notes: {get_notes(eid, 120)}\")\naccs_all = [get_acc('deepseek_vota_seed42'), get_acc('deepseek_vota_seed123'), get_acc('deepseek_vota_seed456')]\naccs_all_clean = [a for a in accs_all if a is not None]\nif accs_all_clean:\n    print(f\"  => ALL seeds mean = {sum(accs_all_clean)/len(accs_all_clean):.2f}\")\n    # Without outlier\n    accs_no_outlier = [get_acc('deepseek_vota_seed123'), get_acc('deepseek_vota_seed456')]\n    accs_no_outlier = [a for a in accs_no_outlier if a is not None]\n    if accs_no_outlier:\n        print(f\"  => Without seed42 outlier: mean = {sum(accs_no_outlier)/len(accs_no_outlier):.2f}\")\n\nprint(\"\\n--- loop_only ---\")\nfor eid in [\"deepseek_loop_only_seed42\", \"deepseek_loop_only_seed123\", \"deepseek_loop_only_seed456\"]:\n    print(f\"  {eid:<50} status={get_status(eid):<8} acc={get_acc(eid)}\")\naccs = [get_acc('deepseek_loop_only_seed42'), get_acc('deepseek_loop_only_seed123'), get_acc('deepseek_loop_only_seed456')]\naccs = [a for a in accs if a is not None]\nif accs:\n    print(f\"  => seeds: 42={get_acc('deepseek_loop_only_seed42')}, 123={get_acc('deepseek_loop_only_seed123')}, 456={get_acc('deepseek_loop_only_seed456')}\")\n    print(f\"  => mean = {sum(accs)/len(accs):.2f}\")\n\nprint(\"\\n--- full_trace (canonical = tail512) ---\")\nfor eid in [\"deepseek_full_trace_tail512_seed42\", \"deepseek_full_trace_tail512_seed123_v2\", \"deepseek_full_trace_tail512_seed456\"]:\n    print(f\"  {eid:<50} status={get_status(eid):<8} acc={get_acc(eid)}\")\naccs = [get_acc('deepseek_full_trace_tail512_seed42'), get_acc('deepseek_full_trace_tail512_seed123_v2'), get_acc('deepseek_full_trace_tail512_seed456')]\naccs = [a for a in accs if a is not None]\nif accs:\n    print(f\"  => mean = {sum(accs)/len(accs):.2f}\")\n\nprint(\"\\n  Raw full_trace (before truncation fix):\")\nfor eid in [\"deepseek_full_trace_seed42\", \"deepseek_full_trace_seed42_v3\"]:\n    print(f\"    {eid:<48} acc={get_acc(eid)}  notes: {get_notes(eid, 80)}\")\n\nprint(\"\\n--- no_trace ---\")\nfor eid in [\"deepseek_no_trace_seed42\", \"deepseek_no_trace_seed123\"]:\n    print(f\"  {eid:<50} status={get_status(eid):<8} acc={get_acc(eid)}\")\nprint(f\"  NOTE: seed123 was killed. Only seed42 has data = {get_acc('deepseek_no_trace_seed42')}\")\n\n\n# ============================================================\n# CODELLAMA-13B\n# ============================================================\nprint(\"\\n\" + \"=\" * 80)\nprint(\"CODELLAMA-13B (CodeLlama-13B-Instruct)\")\nprint(\"=\" * 80)\n\nprint(\"\\n--- exception_only ---\")\nfor eid in [\"codellama13b_exception_only_seed42\", \"codellama13b_exception_only_seed123\", \"codellama13b_exception_only_seed456\"]:\n    print(f\"  {eid:<50} status={get_status(eid):<8} acc={get_acc(eid)}\")\naccs = [get_acc('codellama13b_exception_only_seed42'), get_acc('codellama13b_exception_only_seed123'), get_acc('codellama13b_exception_only_seed456')]\naccs = [a for a in accs if a is not None]\nif accs:\n    print(f\"  => seeds: 42={get_acc('codellama13b_exception_only_seed42')}, 123={get_acc('codellama13b_exception_only_seed123')}, 456={get_acc('codellama13b_exception_only_seed456')}\")\n    print(f\"  => mean = {sum(accs)/len(accs):.2f}\")\n\nprint(\"\\n--- ae_only ---\")\nfor eid in [\"codellama13b_ae_only_seed42\", \"codellama13b_ae_only_seed123\"]:\n    print(f\"  {eid:<50} status={get_status(eid):<8} acc={get_acc(eid)}\")\naccs = [get_acc('codellama13b_ae_only_seed42'), get_acc('codellama13b_ae_only_seed123')]\naccs = [a for a in accs if a is not None]\nif accs:\n    print(f\"  => seeds: 42={get_acc('codellama13b_ae_only_seed42')}, 123={get_acc('codellama13b_ae_only_seed123')}\")\n    print(f\"  NOTE: Only 2 seeds\")\n\nprint(\"\\n--- vota ---\")\nfor eid in [\"codellama13b_vota_seed42\", \"codellama13b_vota_seed123\"]:\n    print(f\"  {eid:<50} status={get_status(eid):<8} acc={get_acc(eid)}\")\naccs = [get_acc('codellama13b_vota_seed42'), get_acc('codellama13b_vota_seed123')]\naccs = [a for a in accs if a is not None]\nif accs:\n    print(f\"  => seeds: 42={get_acc('codellama13b_vota_seed42')}, 123={get_acc('codellama13b_vota_seed123')}\")\n    print(f\"  NOTE: Only 2 seeds\")\n\nprint(\"\\n--- loop_only ---\")\nfor eid in [\"codellama13b_loop_only_seed42\", \"codellama13b_loop_only_seed123\", \"codellama13b_loop_only_seed456\"]:\n    print(f\"  {eid:<50} status={get_status(eid):<8} acc={get_acc(eid)}\")\naccs = [get_acc('codellama13b_loop_only_seed42'), get_acc('codellama13b_loop_only_seed123'), get_acc('codellama13b_loop_only_seed456')]\naccs = [a for a in accs if a is not None]\nif accs:\n    print(f\"  => seeds: 42={get_acc('codellama13b_loop_only_seed42')}, 123={get_acc('codellama13b_loop_only_seed123')}, 456={get_acc('codellama13b_loop_only_seed456')}\")\n    print(f\"  => mean = {sum(accs)/len(accs):.2f}\")\n\nprint(\"\\n--- full_trace (canonical = tail512) ---\")\nfor eid in [\"codellama13b_full_trace_tail512_seed42\", \"codellama13b_full_trace_tail512_seed123\", \"codellama13b_full_trace_tail512_seed456\"]:\n    print(f\"  {eid:<50} status={get_status(eid):<8} acc={get_acc(eid)}\")\naccs = [get_acc('codellama13b_full_trace_tail512_seed42'), get_acc('codellama13b_full_trace_tail512_seed123'), get_acc('codellama13b_full_trace_tail512_seed456')]\naccs = [a for a in accs if a is not None]\nif accs:\n    print(f\"  => seeds: 42={get_acc('codellama13b_full_trace_tail512_seed42')}, 123={get_acc('codellama13b_full_trace_tail512_seed123')}, 456={get_acc('codellama13b_full_trace_tail512_seed456')}\")\n    print(f\"  => mean = {sum(accs)/len(accs):.2f}\")\n\nprint(\"\\n--- no_trace ---\")\nfor eid in [\"codellama13b_no_trace_seed42\"]:\n    print(f\"  {eid:<50} status={get_status(eid):<8} acc={get_acc(eid)}\")\nprint(f\"  NOTE: Only seed42 available = {get_acc('codellama13b_no_trace_seed42')}\")\n\nprint(\"\\n--- nomarker ---\")\nprint(f\"  codellama13b_nomarker_seed42: status={get_status('codellama13b_nomarker_seed42')}, acc={get_acc('codellama13b_nomarker_seed42')}\")\nprint(f\"    Notes: {get_notes('codellama13b_nomarker_seed42', 120)}\")\n\n\n# ============================================================\n# QWEN-1.5B\n# ============================================================\nprint(\"\\n\" + \"=\" * 80)\nprint(\"QWEN-1.5B (Qwen2.5-1.5B-Instruct)\")\nprint(\"=\" * 80)\n\nprint(\"\\n--- exception_only ---\")\nfor eid in [\"qwen15b_exception_only_seed42\", \"qwen15b_exception_only_seed123_v2\", \"qwen15b_exception_only_seed456\"]:\n    print(f\"  {eid:<50} status={get_status(eid):<8} acc={get_acc(eid)}\")\naccs = [get_acc('qwen15b_exception_only_seed42'), get_acc('qwen15b_exception_only_seed123_v2'), get_acc('qwen15b_exception_only_seed456')]\naccs = [a for a in accs if a is not None]\nif accs:\n    print(f\"  => seeds: 42={get_acc('qwen15b_exception_only_seed42')}, 123(v2)={get_acc('qwen15b_exception_only_seed123_v2')}, 456={get_acc('qwen15b_exception_only_seed456')}\")\n    print(f\"  => mean = {sum(accs)/len(accs):.2f}\")\n\nprint(\"\\n--- ae_only ---\")\nfor eid in [\"qwen15b_ae_only_seed42\", \"qwen15b_ae_only_seed123\"]:\n    print(f\"  {eid:<50} status={get_status(eid):<8} acc={get_acc(eid)}\")\naccs = [get_acc('qwen15b_ae_only_seed42'), get_acc('qwen15b_ae_only_seed123')]\naccs = [a for a in accs if a is not None]\nif accs:\n    print(f\"  => seeds: 42={get_acc('qwen15b_ae_only_seed42')}, 123={get_acc('qwen15b_ae_only_seed123')}\")\n    print(f\"  NOTE: Only 2 seeds\")\n\nprint(\"\\n--- vota ---\")\nfor eid in [\"qwen15b_vota_seed42\", \"qwen15b_vota_seed123\"]:\n    print(f\"  {eid:<50} status={get_status(eid):<8} acc={get_acc(eid)}\")\naccs = [get_acc('qwen15b_vota_seed42'), get_acc('qwen15b_vota_seed123')]\naccs = [a for a in accs if a is not None]\nif accs:\n    print(f\"  => seeds: 42={get_acc('qwen15b_vota_seed42')}, 123={get_acc('qwen15b_vota_seed123')}\")\n    print(f\"  NOTE: Only 2 seeds (no seed456)\")\n\nprint(\"\\n--- loop_only ---\")\nfor eid in [\"qwen15b_loop_only_seed42\", \"qwen15b_loop_only_seed123\", \"qwen15b_loop_only_seed456\"]:\n    print(f\"  {eid:<50} status={get_status(eid):<8} acc={get_acc(eid)}\")\naccs = [get_acc('qwen15b_loop_only_seed42'), get_acc('qwen15b_loop_only_seed123'), get_acc('qwen15b_loop_only_seed456')]\naccs = [a for a in accs if a is not None]\nif accs:\n    print(f\"  => seeds: 42={get_acc('qwen15b_loop_only_seed42')}, 123={get_acc('qwen15b_loop_only_seed123')}, 456={get_acc('qwen15b_loop_only_seed456')}\")\n    print(f\"  => mean = {sum(accs)/len(accs):.2f}\")\n\nprint(\"\\n--- full_trace ---\")\nprint(\"  Raw (no truncation):\")\nprint(f\"    qwen15b_full_trace_seed42:                        acc={get_acc('qwen15b_full_trace_seed42')}\")\nprint(\"  Tail512 (canonical):\")\nfor eid in [\"qwen15b_full_trace_tail512_seed42\", \"qwen15b_full_trace_tail512_seed123\", \"qwen15b_full_trace_tail512_seed456\"]:\n    print(f\"    {eid:<48} status={get_status(eid):<8} acc={get_acc(eid)}\")\naccs = [get_acc('qwen15b_full_trace_tail512_seed42'), get_acc('qwen15b_full_trace_tail512_seed123'), get_acc('qwen15b_full_trace_tail512_seed456')]\naccs = [a for a in accs if a is not None]\nif accs:\n    print(f\"  => tail512 mean = {sum(accs)/len(accs):.2f}\")\n\nprint(\"\\n--- no_trace ---\")\nfor eid in [\"qwen15b_no_trace_seed42\", \"qwen15b_no_trace_seed123\", \"qwen15b_no_trace_seed456\"]:\n    print(f\"  {eid:<50} status={get_status(eid):<8} acc={get_acc(eid)}\")\naccs = [get_acc('qwen15b_no_trace_seed42'), get_acc('qwen15b_no_trace_seed123'), get_acc('qwen15b_no_trace_seed456')]\naccs = [a for a in accs if a is not None]\nif accs:\n    print(f\"  => seeds: 42={get_acc('qwen15b_no_trace_seed42')}, 123={get_acc('qwen15b_no_trace_seed123')}, 456={get_acc('qwen15b_no_trace_seed456')}\")\n    print(f\"  => mean = {sum(accs)/len(accs):.2f}\")\n\nprint(\"\\n--- nomarker ---\")\nprint(f\"  qwen15b_nomarker_seed42: status={get_status('qwen15b_nomarker_seed42')}, acc={get_acc('qwen15b_nomarker_seed42')}\")\n\n# Also check the qwen1.5b_ killed ones\nprint(\"\\n--- qwen1.5b_ (killed/duplicate) entries ---\")\nfor eid in [\"qwen1.5b_exception_only_seed42\", \"qwen1.5b_full_trace_seed42\", \"qwen1.5b_no_trace_seed42\", \"qwen1.5b_vota_seed42\"]:\n    print(f\"  {eid:<50} status={get_status(eid):<8} acc={get_acc(eid)}  notes: {get_notes(eid, 80)}\")\n\n\n# ============================================================\n# SUMMARY TABLE\n# ============================================================\nprint(\"\\n\\n\" + \"=\" * 120)\nprint(\"SUMMARY: Canonical accuracy values for Table 1 (all in %)\")\nprint(\"=\" * 120)\nprint(f\"{'Condition':<20} {'Qwen-7B':<35} {'DeepSeek-6.7B':<35} {'CodeLlama-13B':<35} {'Qwen-1.5B':<35}\")\nprint(\"-\" * 120)\n\n# Helper to format multi-seed\ndef fmt(vals, ids=None):\n    \"\"\"vals = list of (seed, acc%)\"\"\"\n    if not vals:\n        return \"N/A\"\n    accs = [v for _, v in vals if v is not None]\n    if not accs:\n        return \"N/A\"\n    if len(accs) == 1:\n        return f\"{accs[0]:.2f} (1 seed)\"\n    mean = sum(accs)/len(accs)\n    seeds_str = \"/\".join(f\"{v:.2f}\" for _, v in vals if v is not None)\n    return f\"{mean:.2f} ({seeds_str})\"\n\nrows = {\n    \"exception_only\": {\n        \"Qwen-7B\": [(42, get_acc('vota_exception_only_seed42_v2')), (123, get_acc('exception_only_seed123')), (456, get_acc('exception_only_seed456'))],\n        \"DeepSeek-6.7B\": [(42, get_acc('deepseek_exception_only_seed42')), (123, get_acc('deepseek_exception_only_seed123_v2')), (456, get_acc('deepseek_exception_only_seed456'))],\n        \"CodeLlama-13B\": [(42, get_acc('codellama13b_exception_only_seed42')), (123, get_acc('codellama13b_exception_only_seed123')), (456, get_acc('codellama13b_exception_only_seed456'))],\n        \"Qwen-1.5B\": [(42, get_acc('qwen15b_exception_only_seed42')), (123, get_acc('qwen15b_exception_only_seed123_v2')), (456, get_acc('qwen15b_exception_only_seed456'))],\n    },\n    \"ae_only\": {\n        \"Qwen-7B\": [(42, get_acc('vota_ae_only_seed42')), (123, get_acc('ae_only_seed123')), (456, get_acc('ae_only_seed456'))],\n        \"DeepSeek-6.7B\": [(42, get_acc('deepseek_ae_only_seed42')), (123, get_acc('deepseek_ae_only_seed123'))],\n        \"CodeLlama-13B\": [(42, get_acc('codellama13b_ae_only_seed42')), (123, get_acc('codellama13b_ae_only_seed123'))],\n        \"Qwen-1.5B\": [(42, get_acc('qwen15b_ae_only_seed42')), (123, get_acc('qwen15b_ae_only_seed123'))],\n    },\n    \"vota\": {\n        \"Qwen-7B\": [(42, get_acc('vota_seed42_v5')), (123, get_acc('qwen7b_vota_seed123')), (456, get_acc('qwen7b_vota_seed456'))],\n        \"DeepSeek-6.7B\": [(42, get_acc('deepseek_vota_seed42')), (123, get_acc('deepseek_vota_seed123')), (456, get_acc('deepseek_vota_seed456'))],\n        \"CodeLlama-13B\": [(42, get_acc('codellama13b_vota_seed42')), (123, get_acc('codellama13b_vota_seed123'))],\n        \"Qwen-1.5B\": [(42, get_acc('qwen15b_vota_seed42')), (123, get_acc('qwen15b_vota_seed123'))],\n    },\n    \"loop_only\": {\n        \"Qwen-7B\": [(42, get_acc('vota_loop_only_seed42')), (123, get_acc('loop_only_seed123')), (456, get_acc('loop_only_seed456'))],\n        \"DeepSeek-6.7B\": [(42, get_acc('deepseek_loop_only_seed42')), (123, get_acc('deepseek_loop_only_seed123')), (456, get_acc('deepseek_loop_only_seed456'))],\n        \"CodeLlama-13B\": [(42, get_acc('codellama13b_loop_only_seed42')), (123, get_acc('codellama13b_loop_only_seed123')), (456, get_acc('codellama13b_loop_only_seed456'))],\n        \"Qwen-1.5B\": [(42, get_acc('qwen15b_loop_only_seed42')), (123, get_acc('qwen15b_loop_only_seed123')), (456, get_acc('qwen15b_loop_only_seed456'))],\n    },\n    \"full_trace\": {\n        \"Qwen-7B\": [(42, get_acc('full_trace_seed42_v5')), (123, get_acc('qwen7b_full_trace_seed123')), (456, get_acc('qwen7b_full_trace_seed456_v2'))],\n        \"DeepSeek-6.7B\": [(42, get_acc('deepseek_full_trace_seed42_v3'))],\n        \"CodeLlama-13B\": [],  # no raw full_trace for codellama, only tail variants\n        \"Qwen-1.5B\": [(42, get_acc('qwen15b_full_trace_seed42'))],\n    },\n    \"full_trace_t512\": {\n        \"Qwen-7B\": [(42, get_acc('full_trace_tail_512_seed42')), (123, get_acc('qwen7b_full_trace_tail512_seed123')), (456, get_acc('qwen7b_full_trace_tail512_seed456'))],\n        \"DeepSeek-6.7B\": [(42, get_acc('deepseek_full_trace_tail512_seed42')), (123, get_acc('deepseek_full_trace_tail512_seed123_v2')), (456, get_acc('deepseek_full_trace_tail512_seed456'))],\n        \"CodeLlama-13B\": [(42, get_acc('codellama13b_full_trace_tail512_seed42')), (123, get_acc('codellama13b_full_trace_tail512_seed123')), (456, get_acc('codellama13b_full_trace_tail512_seed456'))],\n        \"Qwen-1.5B\": [(42, get_acc('qwen15b_full_trace_tail512_seed42')), (123, get_acc('qwen15b_full_trace_tail512_seed123')), (456, get_acc('qwen15b_full_trace_tail512_seed456'))],\n    },\n    \"no_trace\": {\n        \"Qwen-7B\": [(42, get_acc('no_trace_seed42_v5'))],\n        \"DeepSeek-6.7B\": [(42, get_acc('deepseek_no_trace_seed42'))],\n        \"CodeLlama-13B\": [(42, get_acc('codellama13b_no_trace_seed42'))],\n        \"Qwen-1.5B\": [(42, get_acc('qwen15b_no_trace_seed42')), (123, get_acc('qwen15b_no_trace_seed123')), (456, get_acc('qwen15b_no_trace_seed456'))],\n    },\n    \"nomarker\": {\n        \"Qwen-7B\": [(42, get_acc('exception_only_nomarker_seed42')), (123, get_acc('exception_only_nomarker_seed123')), (456, get_acc('exception_only_nomarker_seed456'))],\n        \"DeepSeek-6.7B\": [],\n        \"CodeLlama-13B\": [(42, get_acc('codellama13b_nomarker_seed42'))],\n        \"Qwen-1.5B\": [(42, get_acc('qwen15b_nomarker_seed42'))],\n    },\n}\n\nfor cond, models in rows.items():\n    q7 = fmt(models.get(\"Qwen-7B\", []))\n    ds = fmt(models.get(\"DeepSeek-6.7B\", []))\n    cl = fmt(models.get(\"CodeLlama-13B\", []))\n    q15 = fmt(models.get(\"Qwen-1.5B\", []))\n    print(f\"{cond:<20} {q7:<35} {ds:<35} {cl:<35} {q15:<35}\")\n\n# Cross-check user's expected values\nprint(\"\\n\\n\" + \"=\" * 80)\nprint(\"CROSS-CHECK against user's expected values:\")\nprint(\"=\" * 80)\n\nchecks = [\n    (\"full_trace Qwen-7B seeds\", [81.76, 80.20, 82.35], [get_acc('full_trace_seed42_v5'), get_acc('qwen7b_full_trace_seed123'), get_acc('qwen7b_full_trace_seed456_v2')]),\n    (\"ae_only Qwen-7B seeds\", [99.92, 99.08, 99.92], [get_acc('vota_ae_only_seed42'), get_acc('ae_only_seed123'), get_acc('ae_only_seed456')]),\n    (\"loop_only Qwen-7B seeds\", [85.63, 85.88, 86.64], [get_acc('vota_loop_only_seed42'), get_acc('loop_only_seed123'), get_acc('loop_only_seed456')]),\n    (\"VOTA Qwen-7B seeds\", [99.41, 98.66, 99.08], [get_acc('vota_seed42_v5'), get_acc('qwen7b_vota_seed123'), get_acc('qwen7b_vota_seed456')]),\n    (\"DeepSeek VOTA seed42 outlier\", [84.45], [get_acc('deepseek_vota_seed42')]),\n]\n\nfor label, expected, actual in checks:\n    match = all(abs(e - (a or 0)) < 0.05 for e, a in zip(expected, actual))\n    status = \"MATCH\" if match else \"MISMATCH\"\n    print(f\"  {label}: expected={expected}, actual={actual} => {status}\")\n\nPYEOF\n",
  "description": "Full extraction with summary table and cross-checks"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015HUchPTe4989tKrwAwPKeH",
  "session_id": "2d564421-8464-4d87-ad0f-5e3eefeb24a0",
  "uuid": "2552be2d-9881-4612-a034-8ef459c5bf44",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RPHCSEFUCxjrX63cqYdPmF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6255,
      "cache_read_input_tokens": 19493,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6255,
        "ephemeral_1h_input_tokens": 0
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

_source line 31 · 2026-05-21T19:47:59.440Z_

<details><summary>↩ Tool result · `toolu_01Eh8UENEd4Pb1er5qWC6CrR`</summary>

```text
================================================================================================================================================================
NUMERICAL AUDIT: All Table 1 experiments from registry
================================================================================================================================================================

================================================================================
QWEN-7B (Qwen2.5-7B-Instruct)
================================================================================

--- exception_only ---
  vota_exception_only_seed42_v2                      status=DONE     acc=99.83
  exception_only_seed123                             status=DONE     acc=99.83
  exception_only_seed456                             status=DONE     acc=99.83
  => seeds: 42=99.83, 123=99.83, 456=99.83
  => mean = 99.83

--- ae_only ---
  vota_ae_only_seed42                                status=DONE     acc=99.92
  ae_only_seed123                                    status=DONE     acc=99.08
  ae_only_seed456                                    status=DONE     acc=99.92
  => seeds: 42=99.92, 123=99.08, 456=99.92
  => mean = 99.64

--- vota ---
  vota_seed42_v5                                     status=DONE     acc=99.41
  qwen7b_vota_seed123                                status=DONE     acc=98.66
  qwen7b_vota_seed456                                status=DONE     acc=99.08
  => seeds: 42=99.41, 123=98.66, 456=99.08
  => mean = 99.05

  Also: vota_no_ae_seed42 (VOTA minus AE):
    vota_no_ae_seed42: acc=99.4

--- loop_only ---
  vota_loop_only_seed42                              status=DONE     acc=85.63
  loop_only_seed123                                  status=DONE     acc=85.88
  loop_only_seed456                                  status=DONE     acc=86.64
  => seeds: 42=85.63, 123=85.88, 456=86.64
  => mean = 86.05

--- full_trace ---
  full_trace_seed42_v5                               status=DONE     acc=81.76
  qwen7b_full_trace_seed123                          status=DONE     acc=80.2
  qwen7b_full_trace_seed456_v2                       status=DONE     acc=82.35
  => seeds: 42=81.76, 123=80.2, 456=82.35
  => mean = 81.44

  Older/invalidated full_trace runs:
    full_trace_seed42                                status=DONE     acc=28.4  notes:  | killed
    full_trace_seed42_v2                             status=DONE     acc=28.4  notes:  | negative

--- no_trace ---
  no_trace_seed42_v4                                 status=DONE     acc=75.13
  no_trace_seed42_v5                                 status=DONE     acc=75.13
  NOTE: Only seed42 available for Qwen-7B no_trace. Canonical = no_trace_seed42_v4 or v5 = 75.13

--- nomarker ---
  exception_only_nomarker_seed42                     status=DONE     acc=96.55
  exception_only_nomarker_seed123                    status=DONE     acc=98.32
  exception_only_nomarker_seed456                    status=DONE     acc=98.07
  => seeds: 42=96.55, 123=98.32, 456=98.07
  => mean = 97.65

================================================================================
DEEPSEEK-6.7B (DeepSeek-Coder-6.7B-Instruct)
================================================================================

--- exception_only ---
  deepseek_exception_only_seed42                     status=DONE     acc=99.33
  deepseek_exception_only_seed123_v2                 status=DONE     acc=99.5
  deepseek_exception_only_seed456                    status=DONE     acc=99.33
  deepseek_exception_only_seed123 (FAILED):       acc=None  notes: NEGATIVE: accuracy 91.09% vs seed42 99.83% (-8.74pp). fail_recall=0.705, train_l
  => seeds: 42=99.33, 123(v2)=99.5, 456=99.33
  => mean = 99.39

--- ae_only ---
  deepseek_ae_only_seed42                            status=DONE     acc=98.74
  deepseek_ae_only_seed123                           status=DONE     acc=98.32
  => seeds: 42=98.74, 123=98.32
  NOTE: Only 2 seeds available

--- vota ---
  deepseek_vota_seed42                               status=DONE     acc=84.45
    *** OUTLIER: 84.45% — notes: DeepSeek VOTA: 84.45% confirmed with max_length=16384 (re-verified 2026-05-16, exact match). max_length=2048 gives 16% d
  deepseek_vota_seed123                              status=DONE     acc=99.16
  deepseek_vota_seed456                              status=DONE     acc=99.33
  => ALL seeds mean = 94.31
  => Without seed42 outlier: mean = 99.25

--- loop_only ---
  deepseek_loop_only_seed42                          status=DONE     acc=81.26
  deepseek_loop_only_seed123                         status=DONE     acc=81.26
  deepseek_loop_only_seed456                         status=DONE     acc=78.4
  => seeds: 42=81.26, 123=81.26, 456=78.4
  => mean = 80.31

--- full_trace (canonical = tail512) ---
  deepseek_full_trace_tail512_seed42                 status=DONE     acc=93.9
  deepseek_full_trace_tail512_seed123_v2             status=DONE     acc=95.04
  deepseek_full_trace_tail512_seed456                status=DONE     acc=96.05
  => mean = 95.00

  Raw full_trace (before truncation fix):
    deepseek_full_trace_seed42                       acc=None  notes: INVALIDATED: train-eval truncation mismatch。旧 eval (无截断): 28.49% (all predict fa
    deepseek_full_trace_seed42_v3                    acc=79.16  notes: DeepSeek full_trace v3: label-preserving truncation fix. 79.16% confirmed with m

--- no_trace ---
  deepseek_no_trace_seed42                           status=DONE     acc=73.36
  deepseek_no_trace_seed123                          status=DONE     acc=None
  NOTE: seed123 was killed. Only seed42 has data = 73.36

================================================================================
CODELLAMA-13B (CodeLlama-13B-Instruct)
================================================================================

--- exception_only ---
  codellama13b_exception_only_seed42                 status=DONE     acc=99.83
  codellama13b_exception_only_seed123                status=DONE     acc=100
  codellama13b_exception_only_seed456                status=DONE     acc=99.83
  => seeds: 42=99.83, 123=100, 456=99.83
  => mean = 99.89

--- ae_only ---
  codellama13b_ae_only_seed42                        status=DONE     acc=99.08
  codellama13b_ae_only_seed123                       status=DONE     acc=99.08
  => seeds: 42=99.08, 123=99.08
  NOTE: Only 2 seeds

--- vota ---
  codellama13b_vota_seed42                           status=DONE     acc=98.57
  codellama13b_vota_seed123                          status=DONE     acc=98.91
  => seeds: 42=98.57, 123=98.91
  NOTE: Only 2 seeds

--- loop_only ---
  codellama13b_loop_only_seed42                      status=DONE     acc=77.06
  codellama13b_loop_only_seed123                     status=DONE     acc=76.05
  codellama13b_loop_only_seed456                     status=DONE     acc=79.08
  => seeds: 42=77.06, 123=76.05, 456=79.08
  => mean = 77.40

--- full_trace (canonical = tail512) ---
  codellama13b_full_trace_tail512_seed42             status=DONE     acc=98.24
  codellama13b_full_trace_tail512_seed123            status=DONE     acc=98.24
  codellama13b_full_trace_tail512_seed456            status=DONE     acc=98.24
  => seeds: 42=98.24, 123=98.24, 456=98.24
  => mean = 98.24

--- no_trace ---
  codellama13b_no_trace_seed42                       status=DONE     acc=76.5
  NOTE: Only seed42 available = 76.5

--- nomarker ---
  codellama13b_nomarker_seed42: status=DONE, acc=None
    Notes: Cancelled by Director: model weights cleaned from disk, not worth re-downloading 26GB for speculative experiment. Worker

================================================================================
QWEN-1.5B (Qwen2.5-1.5B-Instruct)
================================================================================

--- exception_only ---
  qwen15b_exception_only_seed42                      status=DONE     acc=99.83
  qwen15b_exception_only_seed123_v2                  status=DONE     acc=99.83
  qwen15b_exception_only_seed456                     status=DONE     acc=99.83
  => seeds: 42=99.83, 123(v2)=99.83, 456=99.83
  => mean = 99.83

--- ae_only ---
  qwen15b_ae_only_seed42                             status=DONE     acc=99.08
  qwen15b_ae_only_seed123                            status=DONE     acc=98.57
  => seeds: 42=99.08, 123=98.57
  NOTE: Only 2 seeds

--- vota ---
  qwen15b_vota_seed42                                status=DONE     acc=99.58
  qwen15b_vota_seed123                               status=DONE     acc=99.5
  => seeds: 42=99.58, 123=99.5
  NOTE: Only 2 seeds (no seed456)

--- loop_only ---
  qwen15b_loop_only_seed42                           status=DONE     acc=78.32
  qwen15b_loop_only_seed123                          status=DONE     acc=81.09
  qwen15b_loop_only_seed456                          status=DONE     acc=79.2
  => seeds: 42=78.32, 123=81.09, 456=79.2
  => mean = 79.54

--- full_trace ---
  Raw (no truncation):
    qwen15b_full_trace_seed42:                        acc=77.06
  Tail512 (canonical):
    qwen15b_full_trace_tail512_seed42                status=DONE     acc=95.6
    qwen15b_full_trace_tail512_seed123               status=DONE     acc=97.65
    qwen15b_full_trace_tail512_seed456               status=DONE     acc=96.72
  => tail512 mean = 96.66

--- no_trace ---
  qwen15b_no_trace_seed42                            status=DONE     acc=67.31
  qwen15b_no_trace_seed123                           status=DONE     acc=75.88
  qwen15b_no_trace_seed456                           status=DONE     acc=73.87
  => seeds: 42=67.31, 123=75.88, 456=73.87
  => mean = 72.35

--- nomarker ---
  qwen15b_nomarker_seed42: status=DONE, acc=97.8

--- qwen1.5b_ (killed/duplicate) entries ---
  qwen1.5b_exception_only_seed42                     status=DONE     acc=None  notes: 重复条目，已在 qwen15b_exception_only_seed42 (99.83%) 完成。命名差异：qwen1.5b_ → qwen15b_ | ki
  qwen1.5b_full_trace_seed42                         status=DONE     acc=None  notes: 重复条目，已在 qwen15b_full_trace_seed42 (77.06%) 完成。命名差异：qwen1.5b_ → qwen15b_ | killed
  qwen1.5b_no_trace_seed42                           status=DONE     acc=72.61  notes: Eval completed 2026-05-21. Accuracy 72.6% (vs qwen15b_no_trace_seed42 67.31%, +5
  qwen1.5b_vota_seed42                               status=DONE     acc=None  notes: 重复条目，已在 qwen15b_vota_seed42 (99.58%) 完成。命名差异：qwen1.5b_ → qwen15b_ | killed


========================================================================================================================
SUMMARY: Canonical accuracy values for Table 1 (all in %)
========================================================================================================================
Condition            Qwen-7B                             DeepSeek-6.7B                       CodeLlama-13B                       Qwen-1.5B                          
------------------------------------------------------------------------------------------------------------------------
exception_only       99.83 (99.83/99.83/99.83)           99.39 (99.33/99.50/99.33)           99.89 (99.83/100.00/99.83)          99.83 (99.83/99.83/99.83)          
ae_only              99.64 (99.92/99.08/99.92)           98.53 (98.74/98.32)                 99.08 (99.08/99.08)                 98.82 (99.08/98.57)                
vota                 99.05 (99.41/98.66/99.08)           94.31 (84.45/99.16/99.33)           98.74 (98.57/98.91)                 99.54 (99.58/99.50)                
loop_only            86.05 (85.63/85.88/86.64)           80.31 (81.26/81.26/78.40)           77.40 (77.06/76.05/79.08)           79.54 (78.32/81.09/79.20)          
full_trace           81.44 (81.76/80.20/82.35)           79.16 (1 seed)                      N/A                                 77.06 (1 seed)                     
full_trace_t512      95.74 (93.60/95.97/97.65)           95.00 (93.90/95.04/96.05)           98.24 (98.24/98.24/98.24)           96.66 (95.60/97.65/96.72)          
no_trace             75.13 (1 seed)                      73.36 (1 seed)                      76.50 (1 seed)                      72.35 (67.31/75.88/73.87)          
nomarker             97.65 (96.55/98.32/98.07)           N/A                                 N/A                                 97.80 (1 seed)                     


================================================================================
CROSS-CHECK against user's expected values:
================================================================================
  full_trace Qwen-7B seeds: expected=[81.76, 80.2, 82.35], actual=[81.76, 80.2, 82.35] => MATCH
  ae_only Qwen-7B seeds: expected=[99.92, 99.08, 99.92], actual=[99.92, 99.08, 99.92] => MATCH
  loop_only Qwen-7B seeds: expected=[85.63, 85.88, 86.64], actual=[85.63, 85.88, 86.64] => MATCH
  VOTA Qwen-7B seeds: expected=[99.41, 98.66, 99.08], actual=[99.41, 98.66, 99.08] => MATCH
  DeepSeek VOTA seed42 outlier: expected=[84.45], actual=[84.45] => MATCH
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015HUchPTe4989tKrwAwPKeH",
  "session_id": "2d564421-8464-4d87-ad0f-5e3eefeb24a0",
  "uuid": "88a04ebe-bf9e-4910-b803-3126b1af570c"
}
```

</details>

---

### System

_source line 32_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a6431a7f8bfe3bb97",
  "tool_use_id": "toolu_015HUchPTe4989tKrwAwPKeH",
  "description": "Running Deep-dive on edge cases and supplementary experiments",
  "usage": {
    "total_tokens": 40069,
    "tool_uses": 6,
    "duration_ms": 160780
  },
  "last_tool_name": "Bash",
  "uuid": "6d813766-0cd2-4a0b-8a00-486b869fc5b9",
  "session_id": "2d564421-8464-4d87-ad0f-5e3eefeb24a0"
}
```

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — Bash · `toolu_011bEd7naWJXAZt8dyf1FSff`</summary>

```json
{
  "command": "cd /tmp && python3 << 'PYEOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/2d564421-8464-4d87-ad0f-5e3eefeb24a0/tool-results/mcp-agent-ml-research-read_registry-1779392719783.txt\"\n\nwith open(fpath) as f:\n    outer = json.load(f)\ninner = json.loads(outer[\"result\"])\nexps = inner[\"data\"][\"experiments\"]\n\n# Deep-dive on key experiments with full metrics and notes\n\ndef dump_exp(eid):\n    e = exps.get(eid)\n    if not e:\n        print(f\"  {eid}: NOT FOUND\")\n        return\n    print(f\"  {eid}:\")\n    print(f\"    status: {e.get('status')}\")\n    print(f\"    metrics: {e.get('metrics')}\")\n    print(f\"    notes: {str(e.get('notes',''))[:200]}\")\n    print(f\"    conclusion: {str(e.get('conclusion',''))[:200]}\")\n    print()\n\n# 1. DeepSeek exception_only seed42 — notes say epoch1 was 99.83%, final was 99.33%\nprint(\"=== DeepSeek exception_only seed42 (notes mention epoch1 vs final) ===\")\ndump_exp(\"deepseek_exception_only_seed42\")\n\n# 2. DeepSeek VOTA seed42 outlier\nprint(\"=== DeepSeek VOTA seed42 OUTLIER ===\")\ndump_exp(\"deepseek_vota_seed42\")\n\n# 3. Qwen-7B full_trace_seed42_v5 — check CI notes\nprint(\"=== Qwen-7B full_trace_seed42_v5 ===\")\ndump_exp(\"full_trace_seed42_v5\")\n\n# 4. Qwen-7B no_trace — check all versions\nprint(\"=== Qwen-7B no_trace versions ===\")\nfor eid in [\"no_trace_seed42\", \"no_trace_seed42_v2\", \"no_trace_seed42_v3\", \"no_trace_seed42_v4\", \"no_trace_seed42_v5\"]:\n    dump_exp(eid)\n\n# 5. Qwen-1.5B no_trace — seed42 is 67.31 but qwen1.5b_no_trace_seed42 is 72.61\nprint(\"=== Qwen-1.5B no_trace discrepancy ===\")\ndump_exp(\"qwen15b_no_trace_seed42\")\ndump_exp(\"qwen1.5b_no_trace_seed42\")\n\n# 6. Full_trace mean calculation\nprint(\"=== PRECISE MEAN CALCULATIONS ===\")\nprint(f\"Qwen-7B full_trace: (81.76 + 80.20 + 82.35) / 3 = {(81.76 + 80.20 + 82.35) / 3:.2f}\")\nprint(f\"  Note: 80.20 comes from 0.802 * 100 = 80.20 (registry stores 0.802)\")\n\n# 7. Check if there's a baseline section\nprint(\"\\n=== Baseline data ===\")\nbaseline = inner[\"data\"].get(\"baseline\")\nif baseline:\n    print(json.dumps(baseline, indent=2)[:2000])\nelse:\n    print(\"No baseline section found\")\n\n# 8. Label_only experiments (relevant for ablations)\nprint(\"\\n=== Label-only experiments ===\")\nfor eid in [\"full_trace_label_only_seed42\", \"qwen7b_full_trace_label_only_seed123\", \"qwen7b_full_trace_label_only_seed456\",\n            \"codellama13b_label_only_seed42\", \"codellama13b_label_only_seed42_v2\", \"codellama13b_label_only_seed123_v2\",\n            \"deepseek_label_only_seed42\",\n            \"qwen15b_label_only_seed42\", \"qwen15b_label_only_seed42_v2\", \"qwen15b_label_only_seed123_v2\", \"qwen15b_label_only_seed456_v2\"]:\n    e = exps.get(eid)\n    if e:\n        m = e.get(\"metrics\", {})\n        acc = m.get(\"accuracy\")\n        acc_pct = round(acc * 100, 2) if acc else None\n        print(f\"  {eid:<50} status={e.get('status'):<8} acc={acc_pct}\")\n\n# 9. Truncation ablation experiments (full_trace with different token limits)\nprint(\"\\n=== Truncation ablation (Qwen-7B) ===\")\nfor eid in [\"full_trace_256tok_seed42\", \"full_trace_512tok_seed42\", \"full_trace_1024tok_seed42\",\n            \"full_trace_tail_256_seed42\", \"full_trace_tail256_seed42\",\n            \"full_trace_tail_512_seed42\", \"full_trace_tail_1024_seed42\", \"full_trace_tail_seed42\",\n            \"qwen7b_full_trace_tail384_seed42\", \"qwen7b_full_trace_head2048_seed42\"]:\n    e = exps.get(eid)\n    if e:\n        m = e.get(\"metrics\", {})\n        acc = m.get(\"accuracy\")\n        acc_pct = round(acc * 100, 2) if acc else None\n        print(f\"  {eid:<50} acc={acc_pct}\")\n\nPYEOF\n",
  "description": "Deep-dive on edge cases and supplementary experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015HUchPTe4989tKrwAwPKeH",
  "session_id": "2d564421-8464-4d87-ad0f-5e3eefeb24a0",
  "uuid": "615804b7-bd3e-4e9b-9b6d-015138670c0a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NYCyxhfk6ktnKnPdw8EQfu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14300,
      "cache_read_input_tokens": 25748,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14300,
        "ephemeral_1h_input_tokens": 0
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

_source line 34 · 2026-05-21T19:48:25.309Z_

<details><summary>↩ Tool result · reported error · `toolu_011bEd7naWJXAZt8dyf1FSff`</summary>

```text
Exit code 1
=== DeepSeek exception_only seed42 (notes mention epoch1 vs final) ===
  deepseek_exception_only_seed42:
    status: DONE
    metrics: {'accuracy': 0.9933, 'majority_baseline': 0.7151, 'lift': 0.2782, 'n': 1190, 'pass_precision': 1, 'pass_recall': 0.9906, 'pass_f1': 0.9953, 'fail_precision': 0.9769, 'fail_recall': 1, 'fail_f1': 0.9883, 'epoch1_checkpoint_eval': {'accuracy': 0.9983, 'fail_recall': 1, 'fail_precision': 0.9941, 'pass_recall': 0.9976, 'conclusion': 'epoch1_better_by_0.50pp'}}
    notes: epoch 1 (step 148) accuracy = 99.83%，高于 final (epoch 3) 的 99.33%。eval_loss epoch 2→3 从 0.413 涨到 0.476 (+15%)。continued training 导致 token-level 过拟合，verdict accuracy 从 99.83% 降到 99.33% (-0.50pp)。这是 eval
    conclusion: success

=== DeepSeek VOTA seed42 OUTLIER ===
  deepseek_vota_seed42:
    status: DONE
    metrics: {'accuracy': 0.8445, 'majority_baseline': 0.7151, 'lift': 0.1294, 'accuracy_ci': [0.826, 0.864], 'pass_precision': 0.821, 'pass_recall': 1, 'pass_f1': 0.902, 'fail_precision': 1, 'fail_recall': 0.454, 'fail_f1': 0.625, 'eval_loss_epoch1': 0.0679, 'eval_loss_epoch2': 0.095, 'eval_loss_epoch3': 0.1121, 'final_train_loss': 0.0522, 'epoch1_checkpoint_eval': {'accuracy': 0.7815, 'accuracy_ci': [0.76, 0.803], 'fail_recall': 0.233, 'fail_precision': 1, 'pass_recall': 1, 'pass_precision': 0.766, 'fail_f1': 0.378, 'pass_f1': 0.867, 'conclusion': 'epoch3_final_is_better'}, 'reeval_with_fixed_script': {'accuracy': 0.16, 'accuracy_ci': [0.139, 0.18], 'fail_f1': 0.61, 'fail_precision': 0.9, 'fail_recall': 0.47, 'pass_f1': 0.07, 'pass_precision': 1, 'pass_recall': 0.04, 'note': 'CATASTROPHIC: re-eval with corrected evaluate.py shows 16% (vs original 84.45%). Model predicts fail for almost everything. Previous 84.45% may have been from buggy eval. NEEDS INVESTIGATION.'}, 'group_analysis': {'train_truncated': {'n': 1091, 'accuracy': 0.8304, 'ci_95': [0.8075, 0.8524], 'correct': 906, 'incorrect': 185, 'pass_accuracy': 1, 'pass_n': 822, 'fail_accuracy': 0.3123, 'fail_n': 269}, 'train_intact': {'n': 99, 'accuracy': 1, 'ci_95': [1, 1], 'correct': 99, 'incorrect': 0, 'pass_accuracy': 1, 'pass_n': 29, 'fail_accuracy': 1, 'fail_n': 70}, 'fisher_exact': {'odds_ratio': 0, 'p_value': 0}, 'overall_accuracy': 0.8445, 'max_length': 2048, 'note': "Grouped by whether training sample content exceeded token budget (DeepSeek tokenizer, max_length=2048). Inference used full-length input (no truncation). All 185 errors from truncated group's fail class (fail_recall=31.2%). Intact group: 100% accuracy."}}
    notes: DeepSeek VOTA: 84.45% confirmed with max_length=16384 (re-verified 2026-05-16, exact match). max_length=2048 gives 16% due to evaluate.py front-truncation removing "Answer: " suffix from 91.7% of inpu
    conclusion: success

=== Qwen-7B full_trace_seed42_v5 ===
  full_trace_seed42_v5:
    status: DONE
    metrics: {'accuracy': 0.8176, 'majority_baseline': 0.7151, 'lift': 0.1025, 'n': 1190, 'pass_precision': 0.8774, 'pass_recall': 0.866, 'pass_f1': 0.8717, 'fail_precision': 0.6743, 'fail_recall': 0.6962, 'fail_f1': 0.6851, 'accuracy_ci_lower': 0.797, 'accuracy_ci_upper': 0.839, 'lift_vs_notrace': 0.0664, 'lift_vs_notrace_ci_lower': 0.0437, 'lift_vs_notrace_ci_upper': 0.0899, 'train_loss': 0.05, 'eval_loss': 0.0867, 'wall_clock_seconds': 7852, 'epoch_level': {'epoch1_accuracy': 0.8303, 'epoch2_accuracy': 0.763, 'final_accuracy': 0.8176, 'trend': 'non_monotonic_epoch1_best_epoch2_collapse'}}
    notes: ✅ Paired bootstrap CI (2026-05-15): lift vs no_trace = +6.6pp [4.4, 9.0]pp (significant, N=10000). lift_ci in registry [7.4, 13.2] was vs majority, not vs no_trace — now corrected.
    conclusion: success

=== Qwen-7B no_trace versions ===
  no_trace_seed42:
    status: DONE
    metrics: None
    notes: 
    conclusion: killed

  no_trace_seed42_v2:
    status: DONE
    metrics: None
    notes: 
    conclusion: killed

  no_trace_seed42_v3:
    status: DONE
    metrics: {'train_loss': 0.18, 'eval_loss': 0.645, 'eval_mean_token_accuracy': 0.89, 'accuracy': 0.7513, 'majority_baseline': 0.7151, 'lift': 0.0361, 'pass_precision': 0.8776, 'pass_recall': 0.7579, 'pass_f1': 0.8134, 'fail_precision': 0.5473, 'fail_recall': 0.7345, 'fail_f1': 0.6272}
    notes: 
    conclusion: killed

  no_trace_seed42_v4:
    status: DONE
    metrics: {'accuracy': 0.7513, 'majority_baseline': 0.7151, 'lift': 0.0361, 'pass_precision': 0.8776, 'pass_recall': 0.7579, 'pass_f1': 0.8134, 'fail_precision': 0.5473, 'fail_recall': 0.7345, 'fail_f1': 0.6272, 'train_loss': 0.18, 'eval_loss': 0.6454, 'eval_mean_token_accuracy': 0.8897}
    notes: 
    conclusion: success

  no_trace_seed42_v5:
    status: DONE
    metrics: {'accuracy': 0.7513, 'accuracy_ci_lower': 0.7277, 'accuracy_ci_upper': 0.7748, 'majority_baseline': 0.7151, 'lift': 0.0361, 'lift_ci_lower': 0.0042, 'lift_ci_upper': 0.0706, 'n': 1190, 'pass_precision': 0.8776, 'pass_recall': 0.7579, 'pass_f1': 0.8134, 'fail_precision': 0.5473, 'fail_recall': 0.7345, 'fail_f1': 0.6272, 'epoch_level': {'epoch1_accuracy': 0.7429, 'epoch2_accuracy': 0.763, 'final_accuracy': 0.7513, 'trend': 'non_monotonic_epoch2_best'}}
    notes: 
    conclusion: success

=== Qwen-1.5B no_trace discrepancy ===
  qwen15b_no_trace_seed42:
    status: DONE
    metrics: {'accuracy': 0.6731, 'n': 1190, 'pass_f1': 0.7527, 'fail_f1': 0.518, 'lift_over_majority': -0.042, 'training_time_sec': 851}
    notes: 
    conclusion: success

  qwen1.5b_no_trace_seed42:
    status: DONE
    metrics: {'accuracy': 0.7261, 'accuracy_ci_lower': 0.7008, 'accuracy_ci_upper': 0.7529, 'majority_baseline': 0.7151, 'lift_pp': 1.09, 'pass_precision': 0.831, 'pass_recall': 0.774, 'pass_f1': 0.802, 'fail_precision': 0.516, 'fail_recall': 0.605, 'fail_f1': 0.557}
    notes: Eval completed 2026-05-21. Accuracy 72.6% (vs qwen15b_no_trace_seed42 67.31%, +5.3pp). 独立训练 checkpoint（不同训练命令/输出目录），非简单重复。 Lift over majority baseline +1.1pp, CI 含 0 → 不显著。
    conclusion: success

=== PRECISE MEAN CALCULATIONS ===
Qwen-7B full_trace: (81.76 + 80.20 + 82.35) / 3 = 81.44
  Note: 80.20 comes from 0.802 * 100 = 80.20 (registry stores 0.802)

=== Baseline data ===
No baseline section found

=== Label-only experiments ===
  full_trace_label_only_seed42                       status=DONE     acc=86.22
  qwen7b_full_trace_label_only_seed123               status=DONE     acc=86.89
  qwen7b_full_trace_label_only_seed456               status=DONE     acc=84.7
  codellama13b_label_only_seed42                     status=DONE     acc=None
  codellama13b_label_only_seed42_v2                  status=DONE     acc=28.49
Traceback (most recent call last):
  File "&lt;stdin>", line 69, in &lt;module>
TypeError: type str doesn't define __round__ method
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015HUchPTe4989tKrwAwPKeH",
  "session_id": "2d564421-8464-4d87-ad0f-5e3eefeb24a0",
  "uuid": "7d1e2107-23f1-4ae6-9a19-7e09923d73a2",
  "tool_use_result": "Error: Exit code 1\n=== DeepSeek exception_only seed42 (notes mention epoch1 vs final) ===\n  deepseek_exception_only_seed42:\n    status: DONE\n    metrics: {'accuracy': 0.9933, 'majority_baseline': 0.7151, 'lift': 0.2782, 'n': 1190, 'pass_precision': 1, 'pass_recall': 0.9906, 'pass_f1': 0.9953, 'fail_precision': 0.9769, 'fail_recall': 1, 'fail_f1': 0.9883, 'epoch1_checkpoint_eval': {'accuracy': 0.9983, 'fail_recall': 1, 'fail_precision': 0.9941, 'pass_recall': 0.9976, 'conclusion': 'epoch1_better_by_0.50pp'}}\n    notes: epoch 1 (step 148) accuracy = 99.83%，高于 final (epoch 3) 的 99.33%。eval_loss epoch 2→3 从 0.413 涨到 0.476 (+15%)。continued training 导致 token-level 过拟合，verdict accuracy 从 99.83% 降到 99.33% (-0.50pp)。这是 eval\n    conclusion: success\n\n=== DeepSeek VOTA seed42 OUTLIER ===\n  deepseek_vota_seed42:\n    status: DONE\n    metrics: {'accuracy': 0.8445, 'majority_baseline': 0.7151, 'lift': 0.1294, 'accuracy_ci': [0.826, 0.864], 'pass_precision': 0.821, 'pass_recall': 1, 'pass_f1': 0.902, 'fail_precision': 1, 'fail_recall': 0.454, 'fail_f1': 0.625, 'eval_loss_epoch1': 0.0679, 'eval_loss_epoch2': 0.095, 'eval_loss_epoch3': 0.1121, 'final_train_loss': 0.0522, 'epoch1_checkpoint_eval': {'accuracy': 0.7815, 'accuracy_ci': [0.76, 0.803], 'fail_recall': 0.233, 'fail_precision': 1, 'pass_recall': 1, 'pass_precision': 0.766, 'fail_f1': 0.378, 'pass_f1': 0.867, 'conclusion': 'epoch3_final_is_better'}, 'reeval_with_fixed_script': {'accuracy': 0.16, 'accuracy_ci': [0.139, 0.18], 'fail_f1': 0.61, 'fail_precision': 0.9, 'fail_recall': 0.47, 'pass_f1': 0.07, 'pass_precision': 1, 'pass_recall': 0.04, 'note': 'CATASTROPHIC: re-eval with corrected evaluate.py shows 16% (vs original 84.45%). Model predicts fail for almost everything. Previous 84.45% may have been from buggy eval. NEEDS INVESTIGATION.'}, 'group_analysis': {'train_truncated': {'n': 1091, 'accuracy': 0.8304, 'ci_95': [0.8075, 0.8524], 'correct': 906, 'incorrect': 185, 'pass_accuracy': 1, 'pass_n': 822, 'fail_accuracy': 0.3123, 'fail_n': 269}, 'train_intact': {'n': 99, 'accuracy': 1, 'ci_95': [1, 1], 'correct': 99, 'incorrect': 0, 'pass_accuracy': 1, 'pass_n': 29, 'fail_accuracy': 1, 'fail_n': 70}, 'fisher_exact': {'odds_ratio': 0, 'p_value': 0}, 'overall_accuracy': 0.8445, 'max_length': 2048, 'note': \"Grouped by whether training sample content exceeded token budget (DeepSeek tokenizer, max_length=2048). Inference used full-length input (no truncation). All 185 errors from truncated group's fail class (fail_recall=31.2%). Intact group: 100% accuracy.\"}}\n    notes: DeepSeek VOTA: 84.45% confirmed with max_length=16384 (re-verified 2026-05-16, exact match). max_length=2048 gives 16% due to evaluate.py front-truncation removing \"Answer: \" suffix from 91.7% of inpu\n    conclusion: success\n\n=== Qwen-7B full_trace_seed42_v5 ===\n  full_trace_seed42_v5:\n    status: DONE\n    metrics: {'accuracy': 0.8176, 'majority_baseline': 0.7151, 'lift': 0.1025, 'n': 1190, 'pass_precision': 0.8774, 'pass_recall': 0.866, 'pass_f1': 0.8717, 'fail_precision': 0.6743, 'fail_recall': 0.6962, 'fail_f1': 0.6851, 'accuracy_ci_lower': 0.797, 'accuracy_ci_upper': 0.839, 'lift_vs_notrace': 0.0664, 'lift_vs_notrace_ci_lower': 0.0437, 'lift_vs_notrace_ci_upper': 0.0899, 'train_loss': 0.05, 'eval_loss': 0.0867, 'wall_clock_seconds': 7852, 'epoch_level': {'epoch1_accuracy': 0.8303, 'epoch2_accuracy': 0.763, 'final_accuracy': 0.8176, 'trend': 'non_monotonic_epoch1_best_epoch2_collapse'}}\n    notes: ✅ Paired bootstrap CI (2026-05-15): lift vs no_trace = +6.6pp [4.4, 9.0]pp (significant, N=10000). lift_ci in registry [7.4, 13.2] was vs majority, not vs no_trace — now corrected.\n    conclusion: success\n\n=== Qwen-7B no_trace versions ===\n  no_trace_seed42:\n    status: DONE\n    metrics: None\n    notes: \n    conclusion: killed\n\n  no_trace_seed42_v2:\n    status: DONE\n    metrics: None\n    notes: \n    conclusion: killed\n\n  no_trace_seed42_v3:\n    status: DONE\n    metrics: {'train_loss': 0.18, 'eval_loss': 0.645, 'eval_mean_token_accuracy': 0.89, 'accuracy': 0.7513, 'majority_baseline': 0.7151, 'lift': 0.0361, 'pass_precision': 0.8776, 'pass_recall': 0.7579, 'pass_f1': 0.8134, 'fail_precision': 0.5473, 'fail_recall': 0.7345, 'fail_f1': 0.6272}\n    notes: \n    conclusion: killed\n\n  no_trace_seed42_v4:\n    status: DONE\n    metrics: {'accuracy': 0.7513, 'majority_baseline': 0.7151, 'lift': 0.0361, 'pass_precision': 0.8776, 'pass_recall': 0.7579, 'pass_f1': 0.8134, 'fail_precision': 0.5473, 'fail_recall': 0.7345, 'fail_f1': 0.6272, 'train_loss': 0.18, 'eval_loss': 0.6454, 'eval_mean_token_accuracy': 0.8897}\n    notes: \n    conclusion: success\n\n  no_trace_seed42_v5:\n    status: DONE\n    metrics: {'accuracy': 0.7513, 'accuracy_ci_lower': 0.7277, 'accuracy_ci_upper': 0.7748, 'majority_baseline': 0.7151, 'lift': 0.0361, 'lift_ci_lower': 0.0042, 'lift_ci_upper': 0.0706, 'n': 1190, 'pass_precision': 0.8776, 'pass_recall': 0.7579, 'pass_f1': 0.8134, 'fail_precision': 0.5473, 'fail_recall': 0.7345, 'fail_f1': 0.6272, 'epoch_level': {'epoch1_accuracy': 0.7429, 'epoch2_accuracy': 0.763, 'final_accuracy': 0.7513, 'trend': 'non_monotonic_epoch2_best'}}\n    notes: \n    conclusion: success\n\n=== Qwen-1.5B no_trace discrepancy ===\n  qwen15b_no_trace_seed42:\n    status: DONE\n    metrics: {'accuracy': 0.6731, 'n': 1190, 'pass_f1': 0.7527, 'fail_f1': 0.518, 'lift_over_majority': -0.042, 'training_time_sec': 851}\n    notes: \n    conclusion: success\n\n  qwen1.5b_no_trace_seed42:\n    status: DONE\n    metrics: {'accuracy': 0.7261, 'accuracy_ci_lower': 0.7008, 'accuracy_ci_upper': 0.7529, 'majority_baseline': 0.7151, 'lift_pp': 1.09, 'pass_precision': 0.831, 'pass_recall': 0.774, 'pass_f1': 0.802, 'fail_precision': 0.516, 'fail_recall': 0.605, 'fail_f1': 0.557}\n    notes: Eval completed 2026-05-21. Accuracy 72.6% (vs qwen15b_no_trace_seed42 67.31%, +5.3pp). 独立训练 checkpoint（不同训练命令/输出目录），非简单重复。 Lift over majority baseline +1.1pp, CI 含 0 → 不显著。\n    conclusion: success\n\n=== PRECISE MEAN CALCULATIONS ===\nQwen-7B full_trace: (81.76 + 80.20 + 82.35) / 3 = 81.44\n  Note: 80.20 comes from 0.802 * 100 = 80.20 (registry stores 0.802)\n\n=== Baseline data ===\nNo baseline section found\n\n=== Label-only experiments ===\n  full_trace_label_only_seed42                       status=DONE     acc=86.22\n  qwen7b_full_trace_label_only_seed123               status=DONE     acc=86.89\n  qwen7b_full_trace_label_only_seed456               status=DONE     acc=84.7\n  codellama13b_label_only_seed42                     status=DONE     acc=None\n  codellama13b_label_only_seed42_v2                  status=DONE     acc=28.49\nTraceback (most recent call last):\n  File \"&lt;stdin>\", line 69, in &lt;module>\nTypeError: type str doesn't define __round__ method"
}
```

</details>

---

### System

_source line 35_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a6431a7f8bfe3bb97",
  "tool_use_id": "toolu_015HUchPTe4989tKrwAwPKeH",
  "description": "Running Extract supplementary experiment data (label-only, truncation ablation, DeepSeek VOTA deep-dive)",
  "usage": {
    "total_tokens": 44700,
    "tool_uses": 7,
    "duration_ms": 181097
  },
  "last_tool_name": "Bash",
  "uuid": "e5a8de7c-206e-4bf2-bfc0-1ff028fdb8b4",
  "session_id": "2d564421-8464-4d87-ad0f-5e3eefeb24a0"
}
```

---

### Tool call

_source line 36_

<details open><summary>🔧 Tool call — Bash · `toolu_01Jo4C4NzrXz25GMPUP94ebx`</summary>

```json
{
  "command": "cd /tmp && python3 << 'PYEOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/2d564421-8464-4d87-ad0f-5e3eefeb24a0/tool-results/mcp-agent-ml-research-read_registry-1779392719783.txt\"\n\nwith open(fpath) as f:\n    outer = json.load(f)\ninner = json.loads(outer[\"result\"])\nexps = inner[\"data\"][\"experiments\"]\n\n# Fix: some accuracy values stored as strings\ndef safe_acc(eid):\n    e = exps.get(eid)\n    if not e:\n        return None\n    m = e.get(\"metrics\", {})\n    if not m:\n        return None\n    a = m.get(\"accuracy\")\n    if a is None:\n        return None\n    return round(float(a) * 100, 2)\n\n# Label-only experiments  \nprint(\"=== Label-only experiments ===\")\nfor eid in [\"full_trace_label_only_seed42\", \"qwen7b_full_trace_label_only_seed123\", \"qwen7b_full_trace_label_only_seed456\",\n            \"codellama13b_label_only_seed42\", \"codellama13b_label_only_seed42_v2\", \"codellama13b_label_only_seed123_v2\",\n            \"deepseek_label_only_seed42\",\n            \"qwen15b_label_only_seed42\", \"qwen15b_label_only_seed42_v2\", \"qwen15b_label_only_seed123_v2\", \"qwen15b_label_only_seed456_v2\"]:\n    e = exps.get(eid)\n    if e:\n        m = e.get(\"metrics\", {})\n        acc = m.get(\"accuracy\")\n        if acc is not None:\n            acc_pct = round(float(acc) * 100, 2)\n        else:\n            acc_pct = None\n        print(f\"  {eid:<50} status={e.get('status'):<8} acc={acc_pct}\")\n\n# Truncation ablation\nprint(\"\\n=== Truncation ablation ===\")\nprint(\"\\n  Qwen-7B:\")\nfor eid in [\"full_trace_256tok_seed42\", \"full_trace_512tok_seed42\", \"full_trace_1024tok_seed42\",\n            \"full_trace_tail_256_seed42\", \"full_trace_tail256_seed42\",\n            \"full_trace_tail_512_seed42\", \"qwen7b_full_trace_tail384_seed42\",\n            \"full_trace_tail_1024_seed42\", \"full_trace_tail_seed42\",\n            \"qwen7b_full_trace_head2048_seed42\"]:\n    print(f\"    {eid:<48} acc={safe_acc(eid)}\")\n\nprint(\"\\n  DeepSeek:\")\nfor eid in [\"deepseek_full_trace_tail256_seed42\", \"deepseek_full_trace_tail384_seed42\",\n            \"deepseek_full_trace_tail512_seed42\", \"deepseek_full_trace_tail1024_seed42\",\n            \"deepseek_full_trace_tail2048_seed42\", \"deepseek_full_trace_head2048_seed42\"]:\n    print(f\"    {eid:<48} acc={safe_acc(eid)}\")\n\nprint(\"\\n  CodeLlama-13B:\")\nfor eid in [\"codellama13b_full_trace_tail256_seed42\", \"codellama13b_full_trace_tail384_seed42\",\n            \"codellama13b_full_trace_tail512_seed42\", \"codellama13b_full_trace_tail1024_seed42_v3\",\n            \"codellama13b_full_trace_tail2048_seed42_v3\", \"codellama13b_full_trace_head2048_seed42\"]:\n    print(f\"    {eid:<48} acc={safe_acc(eid)}\")\n\nprint(\"\\n  Qwen-1.5B:\")\nfor eid in [\"qwen15b_full_trace_tail256_seed42\", \"qwen15b_full_trace_tail384_seed42\",\n            \"qwen15b_full_trace_tail512_seed42\", \"qwen15b_full_trace_tail1024_seed42\",\n            \"qwen15b_full_trace_tail2048_seed42\", \"qwen15b_full_trace_head2048_seed42\"]:\n    print(f\"    {eid:<48} acc={safe_acc(eid)}\")\n\n# DeepSeek VOTA re-eval note\nprint(\"\\n=== IMPORTANT NOTE on DeepSeek VOTA seed42 ===\")\ne = exps[\"deepseek_vota_seed42\"]\nreeval = e[\"metrics\"].get(\"reeval_with_fixed_script\", {})\nif reeval:\n    print(f\"  Original accuracy: 84.45%\")\n    print(f\"  Re-eval with fixed script: {float(reeval.get('accuracy', 0)) * 100:.1f}%\")\n    print(f\"  Note: {reeval.get('note', '')[:200]}\")\n    print(f\"  Registry conclusion: {e.get('conclusion')}\")\n    print(f\"  Registry notes: {str(e.get('notes',''))[:300]}\")\n\nPYEOF\n",
  "description": "Extract supplementary experiment data (label-only, truncation ablation, DeepSeek VOTA deep-dive)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015HUchPTe4989tKrwAwPKeH",
  "session_id": "2d564421-8464-4d87-ad0f-5e3eefeb24a0",
  "uuid": "962cc7ad-7621-494f-bf9f-12b4b13f5d30",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0117k2JmkUrCshDcPVtET1BS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4585,
      "cache_read_input_tokens": 40048,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4585,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 46,
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

_source line 37 · 2026-05-21T19:48:45.631Z_

<details><summary>↩ Tool result · reported error · `toolu_01Jo4C4NzrXz25GMPUP94ebx`</summary>

```text
Exit code 1
=== Label-only experiments ===
  full_trace_label_only_seed42                       status=DONE     acc=86.22
  qwen7b_full_trace_label_only_seed123               status=DONE     acc=86.89
  qwen7b_full_trace_label_only_seed456               status=DONE     acc=84.7
  codellama13b_label_only_seed42                     status=DONE     acc=None
  codellama13b_label_only_seed42_v2                  status=DONE     acc=28.49
Traceback (most recent call last):
  File "&lt;stdin>", line 34, in &lt;module>
ValueError: could not convert string to float: 'collapsed'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015HUchPTe4989tKrwAwPKeH",
  "session_id": "2d564421-8464-4d87-ad0f-5e3eefeb24a0",
  "uuid": "afd2192a-d9fa-48a9-8ce2-ab134d0719ed",
  "tool_use_result": "Error: Exit code 1\n=== Label-only experiments ===\n  full_trace_label_only_seed42                       status=DONE     acc=86.22\n  qwen7b_full_trace_label_only_seed123               status=DONE     acc=86.89\n  qwen7b_full_trace_label_only_seed456               status=DONE     acc=84.7\n  codellama13b_label_only_seed42                     status=DONE     acc=None\n  codellama13b_label_only_seed42_v2                  status=DONE     acc=28.49\nTraceback (most recent call last):\n  File \"&lt;stdin>\", line 34, in &lt;module>\nValueError: could not convert string to float: 'collapsed'"
}
```

</details>

---

### System

_source line 38_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a6431a7f8bfe3bb97",
  "tool_use_id": "toolu_015HUchPTe4989tKrwAwPKeH",
  "description": "Running Complete extraction of supplementary experiments",
  "usage": {
    "total_tokens": 46463,
    "tool_uses": 8,
    "duration_ms": 196766
  },
  "last_tool_name": "Bash",
  "uuid": "322714e6-0d78-411f-a749-6862de413e08",
  "session_id": "2d564421-8464-4d87-ad0f-5e3eefeb24a0"
}
```

---

### Tool call

_source line 39_

<details open><summary>🔧 Tool call — Bash · `toolu_01QBht24eUGeU4geYN1JC5Je`</summary>

```json
{
  "command": "cd /tmp && python3 << 'PYEOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/2d564421-8464-4d87-ad0f-5e3eefeb24a0/tool-results/mcp-agent-ml-research-read_registry-1779392719783.txt\"\n\nwith open(fpath) as f:\n    outer = json.load(f)\ninner = json.loads(outer[\"result\"])\nexps = inner[\"data\"][\"experiments\"]\n\ndef safe_acc(eid):\n    e = exps.get(eid)\n    if not e:\n        return None\n    m = e.get(\"metrics\", {})\n    if not m:\n        return None\n    a = m.get(\"accuracy\")\n    if a is None:\n        return None\n    try:\n        return round(float(a) * 100, 2)\n    except (ValueError, TypeError):\n        return f\"[{a}]\"  # non-numeric\n\n# Finish label_only\nprint(\"=== Label-only experiments ===\")\nfor eid in [\"full_trace_label_only_seed42\", \"qwen7b_full_trace_label_only_seed123\", \"qwen7b_full_trace_label_only_seed456\",\n            \"codellama13b_label_only_seed42\", \"codellama13b_label_only_seed42_v2\", \"codellama13b_label_only_seed123_v2\",\n            \"deepseek_label_only_seed42\",\n            \"qwen15b_label_only_seed42\", \"qwen15b_label_only_seed42_v2\", \"qwen15b_label_only_seed123_v2\", \"qwen15b_label_only_seed456_v2\"]:\n    e = exps.get(eid)\n    if e:\n        print(f\"  {eid:<50} status={e.get('status'):<8} acc={safe_acc(eid)}\")\n\n# Truncation ablation\nprint(\"\\n=== Truncation ablation ===\")\nfor label, ids in [\n    (\"Qwen-7B\", [\"full_trace_256tok_seed42\", \"full_trace_512tok_seed42\", \"full_trace_1024tok_seed42\",\n                  \"full_trace_tail_256_seed42\", \"full_trace_tail256_seed42\",\n                  \"full_trace_tail_512_seed42\", \"qwen7b_full_trace_tail384_seed42\",\n                  \"full_trace_tail_1024_seed42\", \"full_trace_tail_seed42\",\n                  \"qwen7b_full_trace_head2048_seed42\"]),\n    (\"DeepSeek\", [\"deepseek_full_trace_tail256_seed42\", \"deepseek_full_trace_tail384_seed42\",\n                  \"deepseek_full_trace_tail512_seed42\", \"deepseek_full_trace_tail1024_seed42\",\n                  \"deepseek_full_trace_tail2048_seed42\", \"deepseek_full_trace_head2048_seed42\"]),\n    (\"CodeLlama-13B\", [\"codellama13b_full_trace_tail256_seed42\", \"codellama13b_full_trace_tail384_seed42\",\n                       \"codellama13b_full_trace_tail512_seed42\", \"codellama13b_full_trace_tail1024_seed42_v3\",\n                       \"codellama13b_full_trace_tail2048_seed42_v3\", \"codellama13b_full_trace_head2048_seed42\"]),\n    (\"Qwen-1.5B\", [\"qwen15b_full_trace_tail256_seed42\", \"qwen15b_full_trace_tail384_seed42\",\n                    \"qwen15b_full_trace_tail512_seed42\", \"qwen15b_full_trace_tail1024_seed42\",\n                    \"qwen15b_full_trace_tail2048_seed42\", \"qwen15b_full_trace_head2048_seed42\"]),\n]:\n    print(f\"\\n  {label}:\")\n    for eid in ids:\n        a = safe_acc(eid)\n        if a is not None:\n            print(f\"    {eid:<48} acc={a}\")\n\n# DeepSeek VOTA\nprint(\"\\n=== DeepSeek VOTA seed42 deep-dive ===\")\ne = exps[\"deepseek_vota_seed42\"]\nm = e[\"metrics\"]\nprint(f\"  accuracy: {float(m['accuracy'])*100:.2f}%\")\nprint(f\"  CI: {m.get('accuracy_ci')}\")\nreeval = m.get(\"reeval_with_fixed_script\", {})\nif reeval:\n    try:\n        print(f\"  re-eval accuracy: {float(reeval['accuracy'])*100:.1f}%\")\n    except:\n        print(f\"  re-eval accuracy: {reeval.get('accuracy')}\")\n    print(f\"  re-eval note: {reeval.get('note', '')[:300]}\")\nprint(f\"  notes: {str(e.get('notes',''))[:300]}\")\n\n# Also check: fewshot / zeroshot experiments\nprint(\"\\n=== Few-shot / Zero-shot experiments ===\")\nfor eid in sorted(exps.keys()):\n    if \"fewshot\" in eid or \"zeroshot\" in eid:\n        print(f\"  {eid:<50} status={exps[eid].get('status'):<8} acc={safe_acc(eid)}\")\n\nPYEOF\n",
  "description": "Complete extraction of supplementary experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015HUchPTe4989tKrwAwPKeH",
  "session_id": "2d564421-8464-4d87-ad0f-5e3eefeb24a0",
  "uuid": "4a53366c-db23-47a3-98a0-0945fcb18f5b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NRwz3nCdDQpNvjWzfJDFwb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1691,
      "cache_read_input_tokens": 44633,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1691,
        "ephemeral_1h_input_tokens": 0
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

_source line 40 · 2026-05-21T19:49:01.169Z_

<details><summary>↩ Tool result · `toolu_01QBht24eUGeU4geYN1JC5Je`</summary>

```text
=== Label-only experiments ===
  full_trace_label_only_seed42                       status=DONE     acc=86.22
  qwen7b_full_trace_label_only_seed123               status=DONE     acc=86.89
  qwen7b_full_trace_label_only_seed456               status=DONE     acc=84.7
  codellama13b_label_only_seed42                     status=DONE     acc=None
  codellama13b_label_only_seed42_v2                  status=DONE     acc=28.49
  codellama13b_label_only_seed123_v2                 status=DONE     acc=[collapsed]
  deepseek_label_only_seed42                         status=DONE     acc=28.5
  qwen15b_label_only_seed42                          status=DONE     acc=None
  qwen15b_label_only_seed42_v2                       status=DONE     acc=78.9
  qwen15b_label_only_seed123_v2                      status=DONE     acc=81.34
  qwen15b_label_only_seed456_v2                      status=DONE     acc=82.52

=== Truncation ablation ===

  Qwen-7B:
    full_trace_256tok_seed42                         acc=78.82
    full_trace_512tok_seed42                         acc=80.42
    full_trace_1024tok_seed42                        acc=77.23
    full_trace_tail_256_seed42                       acc=77.48
    full_trace_tail256_seed42                        acc=78.9
    full_trace_tail_512_seed42                       acc=93.6
    qwen7b_full_trace_tail384_seed42                 acc=79.8
    full_trace_tail_1024_seed42                      acc=96.47
    full_trace_tail_seed42                           acc=97.3

  DeepSeek:
    deepseek_full_trace_tail256_seed42               acc=76.39
    deepseek_full_trace_tail384_seed42               acc=80.7
    deepseek_full_trace_tail512_seed42               acc=93.9
    deepseek_full_trace_tail1024_seed42              acc=96.47
    deepseek_full_trace_tail2048_seed42              acc=94.96
    deepseek_full_trace_head2048_seed42              acc=78.7

  CodeLlama-13B:
    codellama13b_full_trace_tail256_seed42           acc=77.9
    codellama13b_full_trace_tail384_seed42           acc=82.69
    codellama13b_full_trace_tail512_seed42           acc=98.24
    codellama13b_full_trace_head2048_seed42          acc=79.92

  Qwen-1.5B:
    qwen15b_full_trace_tail256_seed42                acc=72.6
    qwen15b_full_trace_tail384_seed42                acc=73.61
    qwen15b_full_trace_tail512_seed42                acc=95.6
    qwen15b_full_trace_tail1024_seed42               acc=96.6
    qwen15b_full_trace_tail2048_seed42               acc=97.9
    qwen15b_full_trace_head2048_seed42               acc=75.29

=== DeepSeek VOTA seed42 deep-dive ===
  accuracy: 84.45%
  CI: [0.826, 0.864]
  re-eval accuracy: 16.0%
  re-eval note: CATASTROPHIC: re-eval with corrected evaluate.py shows 16% (vs original 84.45%). Model predicts fail for almost everything. Previous 84.45% may have been from buggy eval. NEEDS INVESTIGATION.
  notes: DeepSeek VOTA: 84.45% confirmed with max_length=16384 (re-verified 2026-05-16, exact match). max_length=2048 gives 16% due to evaluate.py front-truncation removing "Answer: " suffix from 91.7% of inputs. Training-time eval used old script (no truncation). exception_only/no_trace unaffected (short in

=== Few-shot / Zero-shot experiments ===
  fewshot_gpt41_exception_only_0shot                 status=DONE     acc=82.18
  fewshot_gpt41_exception_only_3shot                 status=DONE     acc=81.93
  fewshot_gpt41_no_trace_0shot                       status=DONE     acc=77.31
  fewshot_gpt4o_exception_only_0shot                 status=DONE     acc=87.98
  fewshot_gpt4o_exception_only_3shot                 status=DONE     acc=86.81
  fewshot_gpt4o_no_trace_0shot                       status=DONE     acc=84.45
  fewshot_qwen7b_exception_only                      status=DONE     acc=90.84
  zeroshot_codellama13b_exception_only               status=DONE     acc=51.01
  zeroshot_deepseek7b_exception_only                 status=DONE     acc=90.59
  zeroshot_qwen15b_exception_only                    status=DONE     acc=93.45
  zeroshot_qwen7b_exception_only                     status=DONE     acc=89.08
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015HUchPTe4989tKrwAwPKeH",
  "session_id": "2d564421-8464-4d87-ad0f-5e3eefeb24a0",
  "uuid": "9b57e4fb-4678-4058-ab54-359665c47fda"
}
```

</details>

---

### System

_source line 41_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a6431a7f8bfe3bb97",
  "tool_use_id": "toolu_015HUchPTe4989tKrwAwPKeH",
  "status": "completed",
  "output_file": "",
  "summary": "Extract registry data for Table 1 audit",
  "usage": {
    "total_tokens": 49390,
    "tool_uses": 8,
    "duration_ms": 231889
  },
  "uuid": "e1e854c3-f694-4a13-a7cf-b165038bee15",
  "session_id": "2d564421-8464-4d87-ad0f-5e3eefeb24a0"
}
```

---

### Tool result

_source line 42 · 2026-05-21T19:49:36.204Z_

<details><summary>↩ Tool result · `toolu_015HUchPTe4989tKrwAwPKeH`</summary>

```text
Here is the complete numerical audit extracted verbatim from the registry.

---

## Table 1 Canonical Accuracy Values (all %)

### Qwen-7B (Qwen2.5-7B-Instruct)

| Condition | Seed 42 | Seed 123 | Seed 456 | Mean |
|---|---|---|---|---|
| exception_only | 99.83 (`vota_exception_only_seed42_v2`) | 99.83 (`exception_only_seed123`) | 99.83 (`exception_only_seed456`) | **99.83** |
| ae_only | 99.92 (`vota_ae_only_seed42`) | 99.08 (`ae_only_seed123`) | 99.92 (`ae_only_seed456`) | **99.64** |
| vota | 99.41 (`vota_seed42_v5`) | 98.66 (`qwen7b_vota_seed123`) | 99.08 (`qwen7b_vota_seed456`) | **99.05** |
| loop_only | 85.63 (`vota_loop_only_seed42`) | 85.88 (`loop_only_seed123`) | 86.64 (`loop_only_seed456`) | **86.05** |
| full_trace | 81.76 (`full_trace_seed42_v5`) | 80.20 (`qwen7b_full_trace_seed123`) | 82.35 (`qwen7b_full_trace_seed456_v2`) | **81.44** |
| no_trace | 75.13 (`no_trace_seed42_v5`) | — | — | **75.13** (1 seed) |
| nomarker | 96.55 (`exception_only_nomarker_seed42`) | 98.32 (`..._seed123`) | 98.07 (`..._seed456`) | **97.65** |

Additional: `vota_no_ae_seed42` = 99.40

### DeepSeek-6.7B (DeepSeek-Coder-6.7B-Instruct)

| Condition | Seed 42 | Seed 123 | Seed 456 | Mean |
|---|---|---|---|---|
| exception_only | 99.33 (`deepseek_exception_only_seed42`) | 99.50 (`..._seed123_v2`) | 99.33 (`..._seed456`) | **99.39** |
| ae_only | 98.74 (`deepseek_ae_only_seed42`) | 98.32 (`..._seed123`) | — | **98.53** (2 seeds) |
| vota | **84.45** (`deepseek_vota_seed42`) OUTLIER | 99.16 (`..._seed123`) | 99.33 (`..._seed456`) | 94.31 (all 3) / **99.25** (excl. outlier) |
| loop_only | 81.26 (`deepseek_loop_only_seed42`) | 81.26 (`..._seed123`) | 78.40 (`..._seed456`) | **80.31** |
| full_trace | 79.16 (`deepseek_full_trace_seed42_v3`) | — | — | **79.16** (1 seed) |
| full_trace_t512 | 93.90 | 95.04 (`..._seed123_v2`) | 96.05 | **95.00** |
| no_trace | 73.36 (`deepseek_no_trace_seed42`) | — (killed) | — | **73.36** (1 seed) |

**DeepSeek VOTA seed42 outlier note**: Registry stores 84.45% (CI [82.6, 86.4]). The metrics also contain a `reeval_with_fixed_script` sub-entry showing 16.0% — notes explain this was a max_length=2048 truncation issue in evaluate.py, and the 84.45% with max_length=16384 is confirmed correct.

### CodeLlama-13B (CodeLlama-13B-Instruct)

| Condition | Seed 42 | Seed 123 | Seed 456 | Mean |
|---|---|---|---|---|
| exception_only | 99.83 | 100.00 | 99.83 | **99.89** |
| ae_only | 99.08 | 99.08 | — | **99.08** (2 seeds) |
| vota | 98.57 | 98.91 | — | **98.74** (2 seeds) |
| loop_only | 77.06 | 76.05 | 79.08 | **77.40** |
| full_trace_t512 | 98.24 | 98.24 | 98.24 | **98.24** (identical across seeds) |
| no_trace | 76.50 | — | — | **76.50** (1 seed) |
| nomarker | N/A (cancelled — model weights deleted) | — | — | — |

### Qwen-1.5B (Qwen2.5-1.5B-Instruct)

| Condition | Seed 42 | Seed 123 | Seed 456 | Mean |
|---|---|---|---|---|
| exception_only | 99.83 | 99.83 (`..._seed123_v2`) | 99.83 | **99.83** |
| ae_only | 99.08 | 98.57 | — | **98.82** (2 seeds) |
| vota | 99.58 | 99.50 | — | **99.54** (2 seeds) |
| loop_only | 78.32 | 81.09 | 79.20 | **79.54** |
| full_trace | 77.06 (1 seed, raw) | — | — | **77.06** |
| full_trace_t512 | 95.60 | 97.65 | 96.72 | **96.66** |
| no_trace | 67.31 | 75.88 | 73.87 | **72.35** |
| nomarker | 97.80 (1 seed) | — | — | **97.80** |

Note: `qwen1.5b_no_trace_seed42` (old naming, different training run) = 72.61 vs `qwen15b_no_trace_seed42` = 67.31 — a 5.3pp discrepancy from different checkpoints.

---

## Cross-checks against expected values

All five user-specified cross-checks **MATCH**:
- full_trace Qwen-7B: 81.76 / 80.20 / 82.35 -> mean 81.44
- ae_only Qwen-7B: 99.92 / 99.08 / 99.92
- loop_only Qwen-7B: 85.63 / 85.88 / 86.64
- VOTA Qwen-7B: 99.41 / 98.66 / 99.08
- DeepSeek VOTA seed42 outlier: 84.45

---

## Supplementary data also extracted

**Truncation ablation** (tail-N tok, all seed42): Qwen-7B tail256=77.48/78.90, tail384=79.80, tail512=93.60, tail1024=96.47; DeepSeek tail256=76.39, tail384=80.70, tail512=93.90, tail1024=96.47; CodeLlama tail256=77.90, tail384=82.69, tail512=98.24; Qwen-1.5B tail256=72.60, tail384=73.61, tail512=95.60, tail1024=96.60, tail2048=97.90.

**Label-only loss**: Qwen-7B 86.22/86.89/84.70 (mean 85.94); Qwen-1.5B 78.90/81.34/82.52.

**Few-shot/zero-shot**: GPT-4o exception_only 0-shot=87.98, 3-shot=86.81; GPT-4.1 exception_only 0-shot=82.18, 3-shot=81.93; zero-shot Qwen-7B=89.08, DeepSeek=90.59, Qwen-1.5B=93.45, CodeLlama=51.01.

agentId: a6431a7f8bfe3bb97 (use SendMessage with to: 'a6431a7f8bfe3bb97' to continue this agent)
&lt;usage>total_tokens: 51415
tool_uses: 8
duration_ms: 231890&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2d564421-8464-4d87-ad0f-5e3eefeb24a0",
  "uuid": "c06f794a-b5b7-4dd1-8f2e-db92fa1e7757",
  "tool_use_result": {
    "status": "completed",
    "prompt": "I need you to extract specific experiment data from a large registry JSON file for a numerical audit. The file is at:\n`/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/2d564421-8464-4d87-ad0f-5e3eefeb24a0/tool-results/mcp-agent-ml-research-read_registry-1779392719783.txt`\n\nThe file is JSON with schema `{result: string}` — the `result` field is a YAML string containing all experiments.\n\nI need you to find ALL experiments matching these conditions across 4 model families. The exp_id naming patterns are:\n- Qwen-7B: `{condition}_seed{N}` (e.g., `exception_only_seed42`, `full_trace_seed42`)\n- DeepSeek-6.7B: `deepseek_{condition}_seed{N}`\n- CodeLlama-13B: `codellama13b_{condition}_seed{N}`\n- Qwen-1.5B: `qwen15b_{condition}_seed{N}` (NOT `qwen1.5b_*` which are killed)\n\nConditions needed: exception_only, ae_only, vota, loop_only, no_trace, full_trace, nomarker\n\nFor EACH matching experiment, I need:\n1. exp_id\n2. status (DONE, KILLED, etc.)\n3. accuracy (from metrics, usually `metrics.accuracy` or similar)\n4. seed\n5. Any notes about multi-seed means\n\n**Steps:**\n1. First probe the structure: `jq 'type, length, keys' file.txt` — then extract the `result` field and parse it.\n2. Use python to parse the YAML content and extract the needed experiments.\n3. Output a clean table with: exp_id | status | accuracy | seed | notes\n\nFocus especially on:\n- full_trace seeds (should be 81.76, 80.17, 82.35 → mean 81.43)\n- exception_only all models/seeds\n- DeepSeek VOTA (seed42=84.45 outlier)\n- ae_only Qwen-7B seeds (99.92/99.08/99.92)\n- loop_only Qwen-7B seeds (85.63/85.88/86.64)\n- no_trace all models\n- VOTA Qwen-7B seeds (99.41/98.66/99.08)\n\nBe thorough — extract every experiment that could appear in Table 1. Report the raw numbers verbatim from the registry.",
    "agentId": "a6431a7f8bfe3bb97",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is the complete numerical audit extracted verbatim from the registry.\n\n---\n\n## Table 1 Canonical Accuracy Values (all %)\n\n### Qwen-7B (Qwen2.5-7B-Instruct)\n\n| Condition | Seed 42 | Seed 123 | Seed 456 | Mean |\n|---|---|---|---|---|\n| exception_only | 99.83 (`vota_exception_only_seed42_v2`) | 99.83 (`exception_only_seed123`) | 99.83 (`exception_only_seed456`) | **99.83** |\n| ae_only | 99.92 (`vota_ae_only_seed42`) | 99.08 (`ae_only_seed123`) | 99.92 (`ae_only_seed456`) | **99.64** |\n| vota | 99.41 (`vota_seed42_v5`) | 98.66 (`qwen7b_vota_seed123`) | 99.08 (`qwen7b_vota_seed456`) | **99.05** |\n| loop_only | 85.63 (`vota_loop_only_seed42`) | 85.88 (`loop_only_seed123`) | 86.64 (`loop_only_seed456`) | **86.05** |\n| full_trace | 81.76 (`full_trace_seed42_v5`) | 80.20 (`qwen7b_full_trace_seed123`) | 82.35 (`qwen7b_full_trace_seed456_v2`) | **81.44** |\n| no_trace | 75.13 (`no_trace_seed42_v5`) | — | — | **75.13** (1 seed) |\n| nomarker | 96.55 (`exception_only_nomarker_seed42`) | 98.32 (`..._seed123`) | 98.07 (`..._seed456`) | **97.65** |\n\nAdditional: `vota_no_ae_seed42` = 99.40\n\n### DeepSeek-6.7B (DeepSeek-Coder-6.7B-Instruct)\n\n| Condition | Seed 42 | Seed 123 | Seed 456 | Mean |\n|---|---|---|---|---|\n| exception_only | 99.33 (`deepseek_exception_only_seed42`) | 99.50 (`..._seed123_v2`) | 99.33 (`..._seed456`) | **99.39** |\n| ae_only | 98.74 (`deepseek_ae_only_seed42`) | 98.32 (`..._seed123`) | — | **98.53** (2 seeds) |\n| vota | **84.45** (`deepseek_vota_seed42`) OUTLIER | 99.16 (`..._seed123`) | 99.33 (`..._seed456`) | 94.31 (all 3) / **99.25** (excl. outlier) |\n| loop_only | 81.26 (`deepseek_loop_only_seed42`) | 81.26 (`..._seed123`) | 78.40 (`..._seed456`) | **80.31** |\n| full_trace | 79.16 (`deepseek_full_trace_seed42_v3`) | — | — | **79.16** (1 seed) |\n| full_trace_t512 | 93.90 | 95.04 (`..._seed123_v2`) | 96.05 | **95.00** |\n| no_trace | 73.36 (`deepseek_no_trace_seed42`) | — (killed) | — | **73.36** (1 seed) |\n\n**DeepSeek VOTA seed42 outlier note**: Registry stores 84.45% (CI [82.6, 86.4]). The metrics also contain a `reeval_with_fixed_script` sub-entry showing 16.0% — notes explain this was a max_length=2048 truncation issue in evaluate.py, and the 84.45% with max_length=16384 is confirmed correct.\n\n### CodeLlama-13B (CodeLlama-13B-Instruct)\n\n| Condition | Seed 42 | Seed 123 | Seed 456 | Mean |\n|---|---|---|---|---|\n| exception_only | 99.83 | 100.00 | 99.83 | **99.89** |\n| ae_only | 99.08 | 99.08 | — | **99.08** (2 seeds) |\n| vota | 98.57 | 98.91 | — | **98.74** (2 seeds) |\n| loop_only | 77.06 | 76.05 | 79.08 | **77.40** |\n| full_trace_t512 | 98.24 | 98.24 | 98.24 | **98.24** (identical across seeds) |\n| no_trace | 76.50 | — | — | **76.50** (1 seed) |\n| nomarker | N/A (cancelled — model weights deleted) | — | — | — |\n\n### Qwen-1.5B (Qwen2.5-1.5B-Instruct)\n\n| Condition | Seed 42 | Seed 123 | Seed 456 | Mean |\n|---|---|---|---|---|\n| exception_only | 99.83 | 99.83 (`..._seed123_v2`) | 99.83 | **99.83** |\n| ae_only | 99.08 | 98.57 | — | **98.82** (2 seeds) |\n| vota | 99.58 | 99.50 | — | **99.54** (2 seeds) |\n| loop_only | 78.32 | 81.09 | 79.20 | **79.54** |\n| full_trace | 77.06 (1 seed, raw) | — | — | **77.06** |\n| full_trace_t512 | 95.60 | 97.65 | 96.72 | **96.66** |\n| no_trace | 67.31 | 75.88 | 73.87 | **72.35** |\n| nomarker | 97.80 (1 seed) | — | — | **97.80** |\n\nNote: `qwen1.5b_no_trace_seed42` (old naming, different training run) = 72.61 vs `qwen15b_no_trace_seed42` = 67.31 — a 5.3pp discrepancy from different checkpoints.\n\n---\n\n## Cross-checks against expected values\n\nAll five user-specified cross-checks **MATCH**:\n- full_trace Qwen-7B: 81.76 / 80.20 / 82.35 -> mean 81.44\n- ae_only Qwen-7B: 99.92 / 99.08 / 99.92\n- loop_only Qwen-7B: 85.63 / 85.88 / 86.64\n- VOTA Qwen-7B: 99.41 / 98.66 / 99.08\n- DeepSeek VOTA seed42 outlier: 84.45\n\n---\n\n## Supplementary data also extracted\n\n**Truncation ablation** (tail-N tok, all seed42): Qwen-7B tail256=77.48/78.90, tail384=79.80, tail512=93.60, tail1024=96.47; DeepSeek tail256=76.39, tail384=80.70, tail512=93.90, tail1024=96.47; CodeLlama tail256=77.90, tail384=82.69, tail512=98.24; Qwen-1.5B tail256=72.60, tail384=73.61, tail512=95.60, tail1024=96.60, tail2048=97.90.\n\n**Label-only loss**: Qwen-7B 86.22/86.89/84.70 (mean 85.94); Qwen-1.5B 78.90/81.34/82.52.\n\n**Few-shot/zero-shot**: GPT-4o exception_only 0-shot=87.98, 3-shot=86.81; GPT-4.1 exception_only 0-shot=82.18, 3-shot=81.93; zero-shot Qwen-7B=89.08, DeepSeek=90.59, Qwen-1.5B=93.45, CodeLlama=51.01."
      }
    ],
    "totalDurationMs": 231890,
    "totalTokens": 51415,
    "totalToolUseCount": 8,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2926,
      "cache_read_input_tokens": 46324,
      "output_tokens": 2164,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2926
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2164,
          "cache_read_input_tokens": 46324,
          "cache_creation_input_tokens": 2926,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2926,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 8,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  }
}
```

</details>

---

### Assistant

_source line 43_

<details><summary>Logged reasoning block</summary>

```text
Now I have both the paper Table 1 data and the registry data. Let me cross-verify each number.

Let me compile the audit table:

**Paper Table 1 values vs Registry:**

### Qwen-7B
| Condition | Paper Value | Paper std | Registry Value | Match? | Notes |
|-----------|-------------|-----------|----------------|--------|-------|
| exception_only | 99.83±0.00 | multi-seed | 99.83 (3 seeds: 99.83/99.83/99.83) | ✅ | |


| ae_only | 99.64±0.49 | multi-seed | 99.64 (3 seeds: 99.92/99.08/99.92) | ✅ | mean matches |
| VOTA | 99.05±0.38 | multi-seed | 99.05 (3 seeds: 99.41/98.66/99.08) | ✅ | |
| loop_only | 86.05±0.52 | multi-seed | 86.05 (3 seeds: 85.63/85.88/86.64) | ✅ | |

Continuing verification...

| no_trace | 75.13† | single seed | 75.13 (seed42) | ✅ | |

Now checking the Qwen-1.5B results. The exception_only condition shows perfect consistency across all three seeds at 99.83. For ae_only, the paper reports 99.83±0.36 but I'm seeing 98.82 from two seeds—the mean of 99.08 and 98.57 rounds to 98.825, which technically matches the paper's 98.83, though it's worth noting this is only two seeds rather than three.

Moving through the remaining conditions: VOTA matches at 99.54 with two seeds averaging to that value, loop_only holds steady at 79.54 across three seeds, and no_trace comes in at 72.35. Let me verify that no_trace calculation—adding 67.31, 75.88, and 73.87 gives 217.06, which divided by three equals 72.3533, rounding to 72.35. The standard deviation checks out as well. Generating comparison table... I'm now checking the DeepSeek results across different conditions. The exception_only, ae_only, and VOTA configurations all match between the paper and registry values, but I need to verify the loop_only metrics as well. Verifying the standard deviation calculations for the remaining footnotes—the DeepSeek exception_only result checks out at σ=0.10, and VOTA on Qwen-7B also matches at σ=0.38. Now I'm checking the ae_only entry with its reported mean of 99.64%. The DeepSeek VOTA seed 42 result appears to be a training failure. Now I'm checking the full_trace values against what the user specified—there's a slight discrepancy where the registry shows seed123=80.20 while the user expected 80.17, and the mean calculates to 81.44 rather than 81.43, though these are minor rounding differences.

Looking back at Table 1, full_trace isn't actually included there—the table only covers exception_only, ae_only, VOTA, loop_only, no_trace, and the majority baseline. So that check is supplementary. However, I'm noticing a potential mismatch: CodeLlama's no_trace shows 76.47† in the paper but 76.50 in the registry. I should also verify the ae_only standard deviation for Qwen-7B, which the paper lists as ±0.49—calculating from the seed values gives approximately 0.49, so that checks out.

For Qwen-1.5B ae_only (±0.36), the calculation from two seeds yields about 0.3606, which rounds correctly. The VOTA standard deviation (±0.06) also matches when I compute it from the seed values. CodeLlama-13B ae_only shows zero variance as expected, and I'm now verifying the VOTA standard deviation for that model as well.

Continuing with CodeLlama-13B loop_only (±1.54), I'm checking the standard deviation across three seed runs, which gives me approximately 1.54 when calculated from the deviations.

Now moving to DeepSeek's ae_only configuration (±0.30), the two seeds yield a standard deviation of about 0.30, matching the paper's reported value. For DeepSeek's loop_only setup (±1.65), I'm working through three seed runs to verify the standard deviation calculation. I'm noticing a discrepancy with CodeLlama's no_trace result—the registry shows 76.50% but the paper lists 76.47%. Let me work through the math: 76.47% of 1190 samples equals exactly 910 correct answers, while 76.50% would be 910.35, which isn't a whole number. So the paper's 76.47 is the precise value, and the registry's 76.50 is likely just a rounding artifact. The paper consistently reports 76.47% for CodeLlama-13B no_trace, but the agent extracted 76.50%, which doesn't align with any whole number of correct predictions from the 1190 total. This discrepancy suggests either a misreading by the agent or a different calculation method in the registry.

Let me verify this directly against the registry YAML and also check whether the † and ‡ footnote markers are consistent across the table entries.

Looking at the registry data, I can confirm the single-seed entries are correctly marked with † for no_trace Qwen-7B, no_trace CL-13B, and no_trace DS-6.7B, while the ‡ on VOTA DS-6.7B is appropriate given it's a 2-seed mean with an outlier footnote. The no_trace Qwen-1.5B entry checks out as a 3-seed result without a marker, which matches the paper's reported mean and standard deviation. Now I need to verify what's happening with the ae_only and VOTA variants for CL-13B and DS-6.7B.

The ae_only entries for both models are 2-seed means without † markers, which is correct since the † specifically denotes single-seed results. CL-13B ae_only shows 99.08±0.00 from two identical seeds, and DS-6.7B ae_only shows 98.53±0.30 from seeds 98.74 and 98.32, both properly reported as multi-seed results. I should check whether the paper's caption about † being single-seed (seed 42) is consistently applied across all single-seed entries.

Looking more carefully at the table, I notice VOTA DS-6.7B is marked with ‡ instead of † and shows 99.25 without a standard deviation, even though it's a 2-seed mean. If I average the two seeds (99.16 and 99.33), I get 99.245, which rounds to 99.25, so this entry should probably include the standard deviation like the other multi-seed results.

The paper's choice to omit the ±std here seems intentional—the ‡ marker points to a footnote explaining an outlier situation, which might justify the different formatting. Now I need to verify the Majority baseline at 71.51%, which represents the proportion of correct solutions in the dataset (851 out of 1190 samples).

I'm also noticing a few discrepancies to track: CodeLlama's no_trace shows 76.47 in the paper but 76.50 in the registry, and there's a full_trace entry with seed123=80.20 versus the user's 80.17—though full_trace isn't in Table 1 so it doesn't affect this audit. For Qwen-7B's ae_only condition, I'm recalculating the standard deviation from the three seed values to ensure precision before finalizing the report. the rounding difference is negligible—0.48 or 0.49 are essentially the same for practical purposes, so this minor discrepancy doesn't affect the validity of the result.

Now I need to compile the report with the data I've gathered, though I should double-check the CL-13B no_trace value from the registry first to make sure I have the right numbers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2d564421-8464-4d87-ad0f-5e3eefeb24a0",
  "uuid": "8c5dfbe1-7d74-4f38-8678-51fc729b4169",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015U62ET3GHxZXrzW6LcKUcV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3756,
      "cache_read_input_tokens": 30398,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3756
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

_source line 44_

Registry 数据已提取。发现一个潜在不一致（CL-13B no_trace），先验证一下。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2d564421-8464-4d87-ad0f-5e3eefeb24a0",
  "uuid": "a716bb5e-c2ae-4645-8f27-0a45009c54cf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015U62ET3GHxZXrzW6LcKUcV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3756,
      "cache_read_input_tokens": 30398,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3756
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

_source line 45_

<details open><summary>🔧 Tool call — Bash · `toolu_016wabrN8FN8AksybqKw6rBs`</summary>

```json
{
  "command": "grep -A 30 'codellama13b_no_trace' registry.yaml | head -40",
  "description": "Check CodeLlama no_trace registry entry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2d564421-8464-4d87-ad0f-5e3eefeb24a0",
  "uuid": "b1868deb-3b13-46c3-a365-7b31132b8ae0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015U62ET3GHxZXrzW6LcKUcV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3756,
      "cache_read_input_tokens": 30398,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3756
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

_source line 46 · 2026-05-21T19:51:11.621Z_

<details><summary>↩ Tool result · `toolu_016wabrN8FN8AksybqKw6rBs`</summary>

```text
    notes: 重复条目，已在 codellama13b_no_trace_seed42 (76.5%) 完成。命名差异：codellama_ → codellama13b_
  codellama_vota_seed42:
    status: DONE
    retry_count: 0
    created_at: '2026-05-16T07:27:43.769Z'
    updated_at: '2026-05-19T12:52:03.704Z'
    spec:
      hypothesis: 'Multi-family validation: VOTA on CodeLlama-7B-Instruct.'
      model_name: CodeLlama-13b-Instruct-hf
      seed: 42
      condition: vota
    conclusion: killed
    failure_reason: user approved 13B not 7B
    hypothesis: CodeLlama-13B VOTA 应在 85-92% accuracy，与 Qwen-7B/DeepSeek VOTA 对齐，作
      rebuttal 储备验证 ablation condition 跨 scale 一致性
    notes: 重复条目，已在 codellama13b_vota_seed42 (98.57%) 完成。命名差异：codellama_ → codellama13b_
  codellama13b_exception_only_seed42:
    status: DONE
    retry_count: 0
    created_at: '2026-05-16T07:47:18.896Z'
    updated_at: '2026-05-17T13:06:57.551Z'
    spec:
      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
        base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study
        && python train/train_sft.py --condition exception_only --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf
        --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_exception_only_seed42
        --wandb_project trace-verdict-study --wandb_run_name codellama13b_exception_only_seed42
        && python eval/evaluate.py --condition exception_only --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf
        --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_exception_only_seed42/final
        --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_exception_only_seed42/final/eval_results.json
        --save_predictions"
--
  codellama13b_no_trace_seed42:
    status: DONE
    retry_count: 1
    created_at: '2026-05-16T07:47:20.182Z'
    updated_at: '2026-05-20T03:09:12.228Z'
    server: westd-11235
    gpu: cuda:1
    account: root
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2d564421-8464-4d87-ad0f-5e3eefeb24a0",
  "uuid": "164bf1de-3a9d-4b22-b50d-7df5f18ef2a3",
  "tool_use_result": {
    "stdout": "    notes: 重复条目，已在 codellama13b_no_trace_seed42 (76.5%) 完成。命名差异：codellama_ → codellama13b_\n  codellama_vota_seed42:\n    status: DONE\n    retry_count: 0\n    created_at: '2026-05-16T07:27:43.769Z'\n    updated_at: '2026-05-19T12:52:03.704Z'\n    spec:\n      hypothesis: 'Multi-family validation: VOTA on CodeLlama-7B-Instruct.'\n      model_name: CodeLlama-13b-Instruct-hf\n      seed: 42\n      condition: vota\n    conclusion: killed\n    failure_reason: user approved 13B not 7B\n    hypothesis: CodeLlama-13B VOTA 应在 85-92% accuracy，与 Qwen-7B/DeepSeek VOTA 对齐，作\n      rebuttal 储备验证 ablation condition 跨 scale 一致性\n    notes: 重复条目，已在 codellama13b_vota_seed42 (98.57%) 完成。命名差异：codellama_ → codellama13b_\n  codellama13b_exception_only_seed42:\n    status: DONE\n    retry_count: 0\n    created_at: '2026-05-16T07:47:18.896Z'\n    updated_at: '2026-05-17T13:06:57.551Z'\n    spec:\n      command: bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate\n        base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study\n        && python train/train_sft.py --condition exception_only --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf\n        --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_exception_only_seed42\n        --wandb_project trace-verdict-study --wandb_run_name codellama13b_exception_only_seed42\n        && python eval/evaluate.py --condition exception_only --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf\n        --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_exception_only_seed42/final\n        --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_exception_only_seed42/final/eval_results.json\n        --save_predictions\"\n--\n  codellama13b_no_trace_seed42:\n    status: DONE\n    retry_count: 1\n    created_at: '2026-05-16T07:47:20.182Z'\n    updated_at: '2026-05-20T03:09:12.228Z'\n    server: westd-11235\n    gpu: cuda:1\n    account: root",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 47_

<details open><summary>🔧 Tool call — Bash · `toolu_01N3wYL6bfnR3whLjerHetkj`</summary>

```json
{
  "command": "grep -A 50 'codellama13b_no_trace_seed42:' /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/registry.yaml | head -60",
  "description": "Get full CodeLlama no_trace entry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2d564421-8464-4d87-ad0f-5e3eefeb24a0",
  "uuid": "8c6a4579-dca3-4884-aed2-325c5419d7ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CC5SzXffzm9p2xkGKSPR3j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7136,
      "cache_read_input_tokens": 34154,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7136
      },
      "output_tokens": 52,
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

_source line 48 · 2026-05-21T19:51:16.548Z_

<details><summary>↩ Tool result · `toolu_01N3wYL6bfnR3whLjerHetkj`</summary>

```text
  codellama13b_no_trace_seed42:
    status: DONE
    retry_count: 1
    created_at: '2026-05-16T07:47:20.182Z'
    updated_at: '2026-05-20T03:09:12.228Z'
    server: westd-11235
    gpu: cuda:1
    account: root
    reproduce:
      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
        base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study
        && python train/train_sft.py --condition no_trace --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf
        --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_no_trace_seed42
        --wandb_project trace-verdict-study --wandb_run_name codellama13b_no_trace_seed42
        && python eval/evaluate.py --condition no_trace --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf
        --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_no_trace_seed42/final
        --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_no_trace_seed42/final/eval_results.json
        --save_predictions"
      wandb_run_id: codellama13b_no_trace_seed42
      code_commit: e404237ccc765768e267d4d6fd3c89549dcf41a4
      finished_at: '2026-05-16T14:19:42.177Z'
    gpu_ids:
    - cuda:1
    extra:
      hook_events:
      - event: on_complete
        action: agent
        ts: '2026-05-16T14:19:44.574583+00:00'
      previous_failure:
        conclusion: success
        metrics:
          accuracy: 0.765
          n: 1190
          majority_baseline: 0.7151
          lift: 0.05
          pass_precision: 0.84
          pass_recall: 0.83
          pass_f1: 0.84
          fail_precision: 0.59
          fail_recall: 0.59
          fail_f1: 0.59
          accuracy_ci:
          - 0.738
          - 0.787
    completed_at: '2026-05-16T14:22:58.643Z'
    hypothesis: 'CodeLlama-13B no-trace baseline: without execution trace, larger
      model capacity does not compensate for missing diagnostic signal — accuracy
      near majority baseline as on smaller models'
    parent: no_trace_seed42_v5
    spec:
      command: previously completed
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2d564421-8464-4d87-ad0f-5e3eefeb24a0",
  "uuid": "5972c0a2-fc3b-4555-a1ee-7619ce324b64",
  "tool_use_result": {
    "stdout": "  codellama13b_no_trace_seed42:\n    status: DONE\n    retry_count: 1\n    created_at: '2026-05-16T07:47:20.182Z'\n    updated_at: '2026-05-20T03:09:12.228Z'\n    server: westd-11235\n    gpu: cuda:1\n    account: root\n    reproduce:\n      command: bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate\n        base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study\n        && python train/train_sft.py --condition no_trace --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf\n        --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_no_trace_seed42\n        --wandb_project trace-verdict-study --wandb_run_name codellama13b_no_trace_seed42\n        && python eval/evaluate.py --condition no_trace --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf\n        --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_no_trace_seed42/final\n        --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_no_trace_seed42/final/eval_results.json\n        --save_predictions\"\n      wandb_run_id: codellama13b_no_trace_seed42\n      code_commit: e404237ccc765768e267d4d6fd3c89549dcf41a4\n      finished_at: '2026-05-16T14:19:42.177Z'\n    gpu_ids:\n    - cuda:1\n    extra:\n      hook_events:\n      - event: on_complete\n        action: agent\n        ts: '2026-05-16T14:19:44.574583+00:00'\n      previous_failure:\n        conclusion: success\n        metrics:\n          accuracy: 0.765\n          n: 1190\n          majority_baseline: 0.7151\n          lift: 0.05\n          pass_precision: 0.84\n          pass_recall: 0.83\n          pass_f1: 0.84\n          fail_precision: 0.59\n          fail_recall: 0.59\n          fail_f1: 0.59\n          accuracy_ci:\n          - 0.738\n          - 0.787\n    completed_at: '2026-05-16T14:22:58.643Z'\n    hypothesis: 'CodeLlama-13B no-trace baseline: without execution trace, larger\n      model capacity does not compensate for missing diagnostic signal — accuracy\n      near majority baseline as on smaller models'\n    parent: no_trace_seed42_v5\n    spec:\n      command: previously completed",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 49_

<details open><summary>🔧 Tool call — Bash · `toolu_01FQ6n3jG4TxpiDTbda2hcnF`</summary>

```json
{
  "command": "grep -A 80 'codellama13b_no_trace_seed42:' /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/registry.yaml | grep -A 20 'metrics:' | head -30",
  "description": "Get metrics for CodeLlama no_trace"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2d564421-8464-4d87-ad0f-5e3eefeb24a0",
  "uuid": "21532271-7e41-4706-ba36-57de0fcac459",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014X88XPte2PknELb5tZJdJa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 920,
      "cache_read_input_tokens": 41290,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 920
      },
      "output_tokens": 66,
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

_source line 50 · 2026-05-21T19:51:19.656Z_

<details><summary>↩ Tool result · `toolu_01FQ6n3jG4TxpiDTbda2hcnF`</summary>

```text
        metrics:
          accuracy: 0.765
          n: 1190
          majority_baseline: 0.7151
          lift: 0.05
          pass_precision: 0.84
          pass_recall: 0.83
          pass_f1: 0.84
          fail_precision: 0.59
          fail_recall: 0.59
          fail_f1: 0.59
          accuracy_ci:
          - 0.738
          - 0.787
    completed_at: '2026-05-16T14:22:58.643Z'
    hypothesis: 'CodeLlama-13B no-trace baseline: without execution trace, larger
      model capacity does not compensate for missing diagnostic signal — accuracy
      near majority baseline as on smaller models'
    parent: no_trace_seed42_v5
    spec:
      command: previously completed
--
    metrics:
      accuracy: 0.765
      n: 1190
      majority_baseline: 0.7151
      lift: 0.05
      pass_precision: 0.84
      pass_recall: 0.83
      pass_f1: 0.84
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2d564421-8464-4d87-ad0f-5e3eefeb24a0",
  "uuid": "ab636d87-2f82-463a-84ae-ec1e9fe5bed2",
  "tool_use_result": {
    "stdout": "        metrics:\n          accuracy: 0.765\n          n: 1190\n          majority_baseline: 0.7151\n          lift: 0.05\n          pass_precision: 0.84\n          pass_recall: 0.83\n          pass_f1: 0.84\n          fail_precision: 0.59\n          fail_recall: 0.59\n          fail_f1: 0.59\n          accuracy_ci:\n          - 0.738\n          - 0.787\n    completed_at: '2026-05-16T14:22:58.643Z'\n    hypothesis: 'CodeLlama-13B no-trace baseline: without execution trace, larger\n      model capacity does not compensate for missing diagnostic signal — accuracy\n      near majority baseline as on smaller models'\n    parent: no_trace_seed42_v5\n    spec:\n      command: previously completed\n--\n    metrics:\n      accuracy: 0.765\n      n: 1190\n      majority_baseline: 0.7151\n      lift: 0.05\n      pass_precision: 0.84\n      pass_recall: 0.83\n      pass_f1: 0.84",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 51_

<details><summary>Logged reasoning block</summary>

```text
The registry shows `accuracy: 0.765` for codellama13b_no_trace_seed42. That's 76.5%, which is stored as 0.765 (3 decimal places). Now, 0.765 × 1190 = 910.35, which isn't an integer. So the raw correct count is either 910 (76.47%) or 911 (76.55%).

Let me check: if accuracy = 910/1190 = 0.764706... → stored as 0.765 (rounded to 3 decimal places). Then the paper uses the more precise 76.47% (which is floor to 2 decimal places: 76.47%).


So this isn't actually a discrepancy at all—it's just a matter of display precision. The underlying count is 910/1190, which equals 76.47% when shown to 2 decimals and rounds to 0.765 when stored to 3 decimals. The paper and registry are reporting the same result, just at different precision levels.

I should check the other experiments to see how the registry handles accuracy values more broadly. Let me look at the eval_results.json file to see the exact stored values for cases like exception_only Qwen-7B, which should be around 99.83%.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2d564421-8464-4d87-ad0f-5e3eefeb24a0",
  "uuid": "5f6e915b-bc01-4e36-aad3-b0ee3a352295",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014DD7BbWWxxnySLJxV4RV6p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 541,
      "cache_read_input_tokens": 42210,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 541
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

_source line 52_

Registry 存储 `accuracy: 0.765`，即 76.5%。但 910/1190 = 76.4706%，论文写 76.47%。这是精度差异还是真实不一致？让我看服务器上的原始 eval 结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2d564421-8464-4d87-ad0f-5e3eefeb24a0",
  "uuid": "8b1c27cd-144e-4b08-a124-010259971a7d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014DD7BbWWxxnySLJxV4RV6p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 541,
      "cache_read_input_tokens": 42210,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 541
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

_source line 53_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01QFQsw6CVpzNoYkGGkTWFV3`</summary>

```json
{
  "server": "westd-11235",
  "command": "cat /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_no_trace_seed42/final/eval_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2d564421-8464-4d87-ad0f-5e3eefeb24a0",
  "uuid": "001e5e9a-6cfa-44c4-b14e-06de41aaf82b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014DD7BbWWxxnySLJxV4RV6p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 541,
      "cache_read_input_tokens": 42210,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 541
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

_source line 54 · 2026-05-21T19:51:33.671Z_

<details><summary>↩ Tool result · `toolu_01QFQsw6CVpzNoYkGGkTWFV3`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"condition\\\": \\\"no_trace\\\",\\n  \\\"checkpoint_dir\\\": \\\"/root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_no_trace_seed42/final\\\",\\n  \\\"metrics\\\": {\\n    \\\"accuracy\\\": 0.7647058823529411,\\n    \\\"majority_baseline\\\": 0.7151260504201681,\\n    \\\"lift\\\": 0.049579831932773044,\\n    \\\"majority_class\\\": \\\"pass\\\",\\n    \\\"n\\\": 1190,\\n    \\\"pass_precision\\\": 0.8370720188902007,\\n    \\\"pass_recall\\\": 0.8331374853113983,\\n    \\\"pass_f1\\\": 0.8351001177856301,\\n    \\\"fail_precision\\\": 0.5860058309037901,\\n    \\\"fail_recall\\\": 0.5929203539823009,\\n    \\\"fail_f1\\\": 0.5894428152492669\\n  },\\n  \\\"confidence_intervals\\\": {\\n    \\\"accuracy_ci_lower\\\": 0.7378151260504202,\\n    \\\"accuracy_ci_upper\\\": 0.7873949579831933,\\n    \\\"majority_baseline_ci_lower\\\": 0.6915966386554622,\\n    \\\"majority_baseline_ci_upper\\\": 0.738655462184874,\\n    \\\"lift_ci_lower\\\": 0.020147058823529344,\\n    \\\"lift_ci_upper\\\": 0.07983193277310918,\\n    \\\"pass_precision_ci_lower\\\": 0.811963042887971,\\n    \\\"pass_precision_ci_upper\\\": 0.8619121224195242,\\n    \\\"pass_recall_ci_lower\\\": 0.8054834503839431,\\n    \\\"pass_recall_ci_upper\\\": 0.8589324563673714,\\n    \\\"pass_f1_ci_lower\\\": 0.8138420840865441,\\n    \\\"pass_f1_ci_upper\\\": 0.8531986183074266,\\n    \\\"fail_precision_ci_lower\\\": 0.5333280757097791,\\n    \\\"fail_precision_ci_upper\\\": 0.6383252740167634,\\n    \\\"fail_recall_ci_lower\\\": 0.5425679329167811,\\n    \\\"fail_recall_ci_upper\\\": 0.6440739734150318,\\n    \\\"fail_f1_ci_lower\\\": 0.5454348965155881,\\n    \\\"fail_f1_ci_upper\\\": 0.6287408380658682\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2d564421-8464-4d87-ad0f-5e3eefeb24a0",
  "uuid": "3d0759b6-636a-4c4c-907d-0c0bbc7183d7",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"condition\\\\\\\": \\\\\\\"no_trace\\\\\\\",\\\\n  \\\\\\\"checkpoint_dir\\\\\\\": \\\\\\\"/root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_no_trace_seed42/final\\\\\\\",\\\\n  \\\\\\\"metrics\\\\\\\": {\\\\n    \\\\\\\"accuracy\\\\\\\": 0.7647058823529411,\\\\n    \\\\\\\"majority_baseline\\\\\\\": 0.7151260504201681,\\\\n    \\\\\\\"lift\\\\\\\": 0.049579831932773044,\\\\n    \\\\\\\"majority_class\\\\\\\": \\\\\\\"pass\\\\\\\",\\\\n    \\\\\\\"n\\\\\\\": 1190,\\\\n    \\\\\\\"pass_precision\\\\\\\": 0.8370720188902007,\\\\n    \\\\\\\"pass_recall\\\\\\\": 0.8331374853113983,\\\\n    \\\\\\\"pass_f1\\\\\\\": 0.8351001177856301,\\\\n    \\\\\\\"fail_precision\\\\\\\": 0.5860058309037901,\\\\n    \\\\\\\"fail_recall\\\\\\\": 0.5929203539823009,\\\\n    \\\\\\\"fail_f1\\\\\\\": 0.5894428152492669\\\\n  },\\\\n  \\\\\\\"confidence_intervals\\\\\\\": {\\\\n    \\\\\\\"accuracy_ci_lower\\\\\\\": 0.7378151260504202,\\\\n    \\\\\\\"accuracy_ci_upper\\\\\\\": 0.7873949579831933,\\\\n    \\\\\\\"majority_baseline_ci_lower\\\\\\\": 0.6915966386554622,\\\\n    \\\\\\\"majority_baseline_ci_upper\\\\\\\": 0.738655462184874,\\\\n    \\\\\\\"lift_ci_lower\\\\\\\": 0.020147058823529344,\\\\n    \\\\\\\"lift_ci_upper\\\\\\\": 0.07983193277310918,\\\\n    \\\\\\\"pass_precision_ci_lower\\\\\\\": 0.811963042887971,\\\\n    \\\\\\\"pass_precision_ci_upper\\\\\\\": 0.8619121224195242,\\\\n    \\\\\\\"pass_recall_ci_lower\\\\\\\": 0.8054834503839431,\\\\n    \\\\\\\"pass_recall_ci_upper\\\\\\\": 0.8589324563673714,\\\\n    \\\\\\\"pass_f1_ci_lower\\\\\\\": 0.8138420840865441,\\\\n    \\\\\\\"pass_f1_ci_upper\\\\\\\": 0.8531986183074266,\\\\n    \\\\\\\"fail_precision_ci_lower\\\\\\\": 0.5333280757097791,\\\\n    \\\\\\\"fail_precision_ci_upper\\\\\\\": 0.6383252740167634,\\\\n    \\\\\\\"fail_recall_ci_lower\\\\\\\": 0.5425679329167811,\\\\n    \\\\\\\"fail_recall_ci_upper\\\\\\\": 0.6440739734150318,\\\\n    \\\\\\\"fail_f1_ci_lower\\\\\\\": 0.5454348965155881,\\\\n    \\\\\\\"fail_f1_ci_upper\\\\\\\": 0.6287408380658682\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.43}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"condition\\\": \\\"no_trace\\\",\\n  \\\"checkpoint_dir\\\": \\\"/root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_no_trace_seed42/final\\\",\\n  \\\"metrics\\\": {\\n    \\\"accuracy\\\": 0.7647058823529411,\\n    \\\"majority_baseline\\\": 0.7151260504201681,\\n    \\\"lift\\\": 0.049579831932773044,\\n    \\\"majority_class\\\": \\\"pass\\\",\\n    \\\"n\\\": 1190,\\n    \\\"pass_precision\\\": 0.8370720188902007,\\n    \\\"pass_recall\\\": 0.8331374853113983,\\n    \\\"pass_f1\\\": 0.8351001177856301,\\n    \\\"fail_precision\\\": 0.5860058309037901,\\n    \\\"fail_recall\\\": 0.5929203539823009,\\n    \\\"fail_f1\\\": 0.5894428152492669\\n  },\\n  \\\"confidence_intervals\\\": {\\n    \\\"accuracy_ci_lower\\\": 0.7378151260504202,\\n    \\\"accuracy_ci_upper\\\": 0.7873949579831933,\\n    \\\"majority_baseline_ci_lower\\\": 0.6915966386554622,\\n    \\\"majority_baseline_ci_upper\\\": 0.738655462184874,\\n    \\\"lift_ci_lower\\\": 0.020147058823529344,\\n    \\\"lift_ci_upper\\\": 0.07983193277310918,\\n    \\\"pass_precision_ci_lower\\\": 0.811963042887971,\\n    \\\"pass_precision_ci_upper\\\": 0.8619121224195242,\\n    \\\"pass_recall_ci_lower\\\": 0.8054834503839431,\\n    \\\"pass_recall_ci_upper\\\": 0.8589324563673714,\\n    \\\"pass_f1_ci_lower\\\": 0.8138420840865441,\\n    \\\"pass_f1_ci_upper\\\": 0.8531986183074266,\\n    \\\"fail_precision_ci_lower\\\": 0.5333280757097791,\\n    \\\"fail_precision_ci_upper\\\": 0.6383252740167634,\\n    \\\"fail_recall_ci_lower\\\": 0.5425679329167811,\\n    \\\"fail_recall_ci_upper\\\": 0.6440739734150318,\\n    \\\"fail_f1_ci_lower\\\": 0.5454348965155881,\\n    \\\"fail_f1_ci_upper\\\": 0.6287408380658682\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 55_

<details><summary>Logged reasoning block</summary>

```text
The raw eval result shows `accuracy: 0.7647058823529411`, which is exactly 910/1190 = 76.47058...%. So the paper's 76.47% is correct. The registry stored 0.765 which is a rounded version. This is a registry precision issue, not a paper error.

Now let me compile the complete audit report. Let me also verify a few more registry entries to ensure accuracy values are consistent with the raw eval files. But I think I have enough data now.

Let me also check if the paper says anything about full_trace being in Table 1... No, full_trace is NOT in Table 1. 

I've confirmed that Table 1 includes exception_only, ae_only, VOTA, loop_only, no_trace, and the Majority baseline. Now I have everything needed to finalize the audit report. The key finding is that the CL-13B no_trace discrepancy between paper and registry is just a rounding difference—the paper's 76.47% matches the raw eval data exactly, while the registry rounded it to 76.5%. All other values align between paper and registry, standard deviations check out with proper sample calculations, and the † markers are correctly placed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2d564421-8464-4d87-ad0f-5e3eefeb24a0",
  "uuid": "f311c9d8-34e8-4422-b3f4-29e077433e9c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LjsF2ZeDZ8oX2bZCXkrc8h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1529,
      "cache_read_input_tokens": 42751,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1529
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

_source line 56_

原始 eval 确认 accuracy = 0.76471 (910/1190)，论文的 76.47% 正确，registry 的 0.765 是精度截断。不存在真实不一致。

现在编写审计报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2d564421-8464-4d87-ad0f-5e3eefeb24a0",
  "uuid": "f0c781c7-1c6d-493d-8172-ccf2bf18f246",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LjsF2ZeDZ8oX2bZCXkrc8h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1529,
      "cache_read_input_tokens": 42751,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1529
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

_source line 57_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01QH7tF64vemzxzgiMMQknuZ`</summary>

```json
{
  "name": "table1_numerical_audit",
  "type": "report",
  "description": "Table 1 数值审计：论文 vs Registry 交叉验证 (EMNLP 2026 ARR Round 14 提交前校验)",
  "project": "trace-verdict-study",
  "tags": [
    "audit",
    "table1",
    "round14"
  ],
  "content_filename": "table1_numerical_audit.md",
  "content": "# Table 1 Numerical Audit — Paper vs Registry Cross-Verification\n\n**Date**: 2026-05-21  \n**Scope**: experiments.tex Table 1 (cross-model verdict accuracy)  \n**Registry**: trace-verdict-study/registry.yaml  \n\n## Audit Table\n\n### Qwen-7B (Qwen2.5-7B-Instruct)\n\n| 条件 | 论文值 | σ | Registry 值 | 来源 exp_id | Seeds | 匹配? | 备注 |\n|------|--------|---|-------------|-------------|-------|-------|------|\n| exception_only | **99.83**±0.00 | 0.00 | 99.83/99.83/99.83 → 99.83 | vota_exception_only_seed42_v2, exception_only_seed123, exception_only_seed456 | 3 | ✅ | |\n| ae_only | 99.64±0.49 | 0.49 | 99.92/99.08/99.92 → 99.64 | vota_ae_only_seed42, ae_only_seed123, ae_only_seed456 | 3 | ✅ | σ=√0.2352=0.485→0.49 |\n| VOTA | 99.05±0.38 | 0.38 | 99.41/98.66/99.08 → 99.05 | vota_seed42_v5, qwen7b_vota_seed123, qwen7b_vota_seed456 | 3 | ✅ | |\n| loop_only | 86.05±0.52 | 0.52 | 85.63/85.88/86.64 → 86.05 | vota_loop_only_seed42, loop_only_seed123, loop_only_seed456 | 3 | ✅ | |\n| no_trace | 75.13† | — | 75.13 | no_trace_seed42_v5 | 1 | ✅ | † correct |\n\n### Qwen-1.5B (Qwen2.5-1.5B-Instruct)\n\n| 条件 | 论文值 | σ | Registry 值 | 来源 exp_id | Seeds | 匹配? | 备注 |\n|------|--------|---|-------------|-------------|-------|-------|------|\n| exception_only | **99.83**±0.00 | 0.00 | 99.83/99.83/99.83 → 99.83 | qwen15b_exception_only_seed42/123/456 | 3 | ✅ | |\n| ae_only | 98.83±0.36 | 0.36 | 99.08/98.57 → 98.825→98.83 | qwen15b_ae_only_seed42, _seed123 | 2 | ✅ | 2-seed mean rounds to 98.83 |\n| VOTA | 99.54±0.06 | 0.06 | 99.58/99.50 → 99.54 | qwen15b_vota_seed42, _seed123 | 2 | ✅ | |\n| loop_only | 79.54±1.42 | 1.42 | 78.32/81.09/79.20 → 79.54 | qwen15b_loop_only_seed42/123/456 | 3 | ✅ | |\n| no_trace | 72.35±4.48 | 4.48 | 67.31/75.88/73.87 → 72.35 | qwen15b_no_trace_seed42/123/456 | 3 | ✅ | σ=√20.09=4.48 |\n\n### CodeLlama-13B (CodeLlama-13B-Instruct)\n\n| 条件 | 论文值 | σ | Registry 值 | 来源 exp_id | Seeds | 匹配? | 备注 |\n|------|--------|---|-------------|-------------|-------|-------|------|\n| exception_only | **99.89**±0.10 | 0.10 | 99.83/100.00/99.83 → 99.887→99.89 | codellama13b_exception_only_seed42/123/456 | 3 | ✅ | |\n| ae_only | 99.08±0.00 | 0.00 | 99.08/99.08 → 99.08 | codellama13b_ae_only_seed42, _seed123 | 2 | ✅ | |\n| VOTA | 98.74±0.24 | 0.24 | 98.57/98.91 → 98.74 | codellama13b_vota_seed42, _seed123 | 2 | ✅ | |\n| loop_only | 77.40±1.54 | 1.54 | 77.06/76.05/79.08 → 77.40 | codellama13b_loop_only_seed42/123/456 | 3 | ✅ | |\n| no_trace | 76.47† | — | raw eval=0.76471 (910/1190) | codellama13b_no_trace_seed42 | 1 | ✅ | Registry 存 0.765（3位截断），原始 eval 76.47% |\n\n### DeepSeek-6.7B (DeepSeek-Coder-6.7B-Instruct)\n\n| 条件 | 论文值 | σ | Registry 值 | 来源 exp_id | Seeds | 匹配? | 备注 |\n|------|--------|---|-------------|-------------|-------|-------|------|\n| exception_only | **99.39**±0.10 | 0.10 | 99.33/99.50/99.33 → 99.387→99.39 | deepseek_exception_only_seed42/123/456 | 3 | ✅ | |\n| ae_only | 98.53±0.30 | 0.30 | 98.74/98.32 → 98.53 | deepseek_ae_only_seed42, _seed123 | 2 | ✅ | |\n| VOTA | 99.25‡ | — | 84.45/99.16/99.33 → 2-seed mean 99.245→99.25 | deepseek_vota_seed42/123/456 | 3 (1 excluded) | ✅ | ‡ footnote explains seed42 outlier |\n| loop_only | 80.31±1.65 | 1.65 | 81.26/81.26/78.40 → 80.307→80.31 | deepseek_loop_only_seed42/123/456 | 3 | ✅ | |\n| no_trace | 73.36† | — | 73.36 | deepseek_no_trace_seed42 | 1 | ✅ | † correct |\n\n### Majority Baseline\n\n| 条件 | 论文值 | Registry 值 | 匹配? |\n|------|--------|-------------|-------|\n| Majority baseline | 71.51 | 0.7151 (851/1190) | ✅ |\n\n## Footnote Verification\n\n| 脚注声明 | Registry 原始值 | 匹配? |\n|----------|----------------|-------|\n| DS exception_only 3 seeds: 99.33/99.50/99.33 (σ=0.10pp) | 99.33/99.50/99.33, σ=0.098→0.10 | ✅ |\n| VOTA Qwen-7B: 99.41/98.66/99.08 (σ=0.38) | 99.41/98.66/99.08, σ=0.376→0.38 | ✅ |\n| ae_only 3 seeds: 99.92/99.08/99.92 (mean 99.64%) | 99.92/99.08/99.92, mean=99.64 | ✅ |\n| loop_only 3 seeds: 85.63/85.88/86.64 (mean 86.05%) | 85.63/85.88/86.64, mean=86.05 | ✅ |\n| Qwen-1.5B exception_only: 99.83% × 3 seeds (σ=0) | 99.83/99.83/99.83 | ✅ |\n| ‡DS VOTA 3 seeds: 84.45/99.16/99.33 | 84.45/99.16/99.33 | ✅ |\n\n## † / ‡ Marker Consistency\n\n| 标记 | 含义 | 应用位置 | 正确? |\n|------|------|----------|-------|\n| † | Single seed (seed 42) | Qwen-7B no_trace, CL-13B no_trace, DS-6.7B no_trace | ✅ 均为 1-seed |\n| ‡ | 2-seed mean (outlier excluded) | DS-6.7B VOTA | ✅ seed42 outlier 已排除 |\n| ±std (无标记) | Multi-seed mean | 所有其他条目 | ✅ 均为 2-3 seed |\n\n## σ Calculation Spot-Checks\n\nAll standard deviations use **sample std** (n-1 denominator), verified:\n\n- Qwen-7B ae_only: √(0.4704/2) = 0.485 → 论文 0.49 (rounding at boundary, acceptable)\n- Qwen-1.5B no_trace: √(40.17/2) = 4.48 ✅\n- CL-13B loop_only: √(4.76/2) = 1.54 ✅\n- DS loop_only: √(5.46/2) = 1.65 ✅\n\n## Summary\n\n**不一致数量: 0**\n\n所有 20 个数值条目（4 模型 × 5 条件）和 6 条脚注声明均与 registry 原始数据匹配。† / ‡ 标记使用正确。σ 计算验证通过（样本标准差，n-1 分母）。\n\n唯一需注意的边界情况：\n1. **Registry 精度截断**: CL-13B no_trace 在 registry 中存为 0.765（76.5%），但原始 eval_results.json 为 0.76471（76.47%）。论文使用了正确的精度值。建议将 registry 精度统一为 4 位小数。\n2. **ae_only σ 舍入**: Qwen-7B ae_only σ 精确值 0.485，论文写 0.49。处于 0.5 边界，两种舍入均可接受。\n\n**结论: Table 1 数值审计通过，无需修改。可安全提交 EMNLP 2026 ARR。**\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2d564421-8464-4d87-ad0f-5e3eefeb24a0",
  "uuid": "4960f91f-91dd-4bab-9af7-323ed71f6a1d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LjsF2ZeDZ8oX2bZCXkrc8h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1529,
      "cache_read_input_tokens": 42751,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1529
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

_source line 58 · 2026-05-21T19:52:31.547Z_

<details><summary>↩ Tool result · `toolu_01QH7tF64vemzxzgiMMQknuZ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260521_7d103d\", \"name\": \"table1_numerical_audit\", \"type\": \"report\", \"description\": \"Table 1 数值审计：论文 vs Registry 交叉验证 (EMNLP 2026 ARR Round 14 提交前校验)\", \"path\": \"projects/trace-verdict-study/artifacts/_project/report/table1_numerical_audit.md\", \"url\": null, \"project\": \"trace-verdict-study\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-21T19:52:31.300885+00:00\", \"tags\": [\"audit\", \"table1\", \"round14\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2d564421-8464-4d87-ad0f-5e3eefeb24a0",
  "uuid": "4ce9f14c-5c6d-4421-8860-273056a0fc4f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260521_7d103d\\\", \\\"name\\\": \\\"table1_numerical_audit\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"Table 1 数值审计：论文 vs Registry 交叉验证 (EMNLP 2026 ARR Round 14 提交前校验)\\\", \\\"path\\\": \\\"projects/trace-verdict-study/artifacts/_project/report/table1_numerical_audit.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"trace-verdict-study\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-21T19:52:31.300885+00:00\\\", \\\"tags\\\": [\\\"audit\\\", \\\"table1\\\", \\\"round14\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260521_7d103d\", \"name\": \"table1_numerical_audit\", \"type\": \"report\", \"description\": \"Table 1 数值审计：论文 vs Registry 交叉验证 (EMNLP 2026 ARR Round 14 提交前校验)\", \"path\": \"projects/trace-verdict-study/artifacts/_project/report/table1_numerical_audit.md\", \"url\": null, \"project\": \"trace-verdict-study\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-21T19:52:31.300885+00:00\", \"tags\": [\"audit\", \"table1\", \"round14\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 59_

## 审计结果：Table 1 数值全部匹配，0 处不一致

全量交叉验证了 20 个数值条目（4 模型 × 5 条件）+ 6 条脚注 + 所有 σ 值 + † / ‡ 标记：

| 检查项 | 数量 | 结果 |
|--------|------|------|
| 主表准确率 | 20 | ✅ 全部匹配 |
| 脚注 per-seed 值 | 6 条 | ✅ 全部匹配 |
| σ 计算 | 16 个 | ✅ 样本标准差正确 |
| † / ‡ 标记 | 4 处 | ✅ 与 seed 数量一致 |

**两个边界注意点**（不影响正确性）：
1. Registry 存 CL-13B no_trace 为 `0.765`（3 位截断），原始 eval 为 `0.76471`，论文 76.47% 正确
2. Qwen-7B ae_only σ 精确值 0.485，论文写 0.49，处于舍入边界

报告已注册为 artifact `table1_numerical_audit`（art_20260521_7d103d）。可安全提交。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2d564421-8464-4d87-ad0f-5e3eefeb24a0",
  "uuid": "b1d3cd9f-ab24-4c20-8229-f6dac6c03ca5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018fhorqFikPYyBMpTTtrvhu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3935,
      "cache_read_input_tokens": 44280,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3935
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

_source line 60_

## 审计结果：Table 1 数值全部匹配，0 处不一致

全量交叉验证了 20 个数值条目（4 模型 × 5 条件）+ 6 条脚注 + 所有 σ 值 + † / ‡ 标记：

| 检查项 | 数量 | 结果 |
|--------|------|------|
| 主表准确率 | 20 | ✅ 全部匹配 |
| 脚注 per-seed 值 | 6 条 | ✅ 全部匹配 |
| σ 计算 | 16 个 | ✅ 样本标准差正确 |
| † / ‡ 标记 | 4 处 | ✅ 与 seed 数量一致 |

**两个边界注意点**（不影响正确性）：
1. Registry 存 CL-13B no_trace 为 `0.765`（3 位截断），原始 eval 为 `0.76471`，论文 76.47% 正确
2. Qwen-7B ae_only σ 精确值 0.485，论文写 0.49，处于舍入边界

报告已注册为 artifact `table1_numerical_audit`（art_20260521_7d103d）。可安全提交。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 449870,
  "duration_api_ms": 448607,
  "num_turns": 10,
  "stop_reason": "end_turn",
  "session_id": "2d564421-8464-4d87-ad0f-5e3eefeb24a0",
  "total_cost_usd": 1.6003555,
  "usage": {
    "input_tokens": 12,
    "cache_creation_input_tokens": 36374,
    "cache_read_input_tokens": 297745,
    "output_tokens": 13233,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 36374,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 382,
        "cache_read_input_tokens": 44280,
        "cache_creation_input_tokens": 3935,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 3935
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1916,
      "outputTokens": 18,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002006,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 22,
      "outputTokens": 32400,
      "cacheReadInputTokens": 506179,
      "cacheCreationInputTokens": 85624,
      "webSearchRequests": 0,
      "costUSD": 1.5983495,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "271bb3af-7e06-4e56-8d9c-b1e2d64e91d6"
}
```

</details>

---
