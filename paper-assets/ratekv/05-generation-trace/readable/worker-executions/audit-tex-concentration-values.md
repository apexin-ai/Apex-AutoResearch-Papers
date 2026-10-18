# audit tex concentration values

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/workers/worker_audit_tex_concentration_values_20260515T141741.log`
- **Structured JSON:** [`46ccaafab7c0b579abd6.json`](../../sessions/46/46ccaafab7c0b579abd6.json)

## Before a recorded user message

21 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "session_id": "f9734027-5e0c-4d70-9553-47857b654bd4",
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
  "uuid": "ba170488-0264-423e-955d-503d725ac8cb",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-ratekv/memory/"
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
    "resetsAt": 1778868000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "b5100334-ae45-4681-baf2-cc1b3086ddbd",
  "session_id": "f9734027-5e0c-4d70-9553-47857b654bd4"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me systematically audit all .tex files for concentration and t1/t5 values across all 7 models.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f9734027-5e0c-4d70-9553-47857b654bd4",
  "uuid": "3aa6d6bf-8796-4083-95d3-9577f6ddf116",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LAGWhTJbjGk9GVhMQ6yEYC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13203,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13203
      },
      "output_tokens": 28,
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

开始系统性审计 .tex 文件中的 concentration 和 t1/t5 值。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f9734027-5e0c-4d70-9553-47857b654bd4",
  "uuid": "e7c3a513-e1cc-4d64-8f9e-3cae443f4aad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LAGWhTJbjGk9GVhMQ6yEYC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13203,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13203
      },
      "output_tokens": 28,
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

<details open><summary>🔧 Tool call — Grep · `toolu_01SnF1dpHc8x83KA57WC6V14`</summary>

```json
{
  "pattern": "concentration|conc\\.?|t_1.*t_5|t_\\{1\\}.*t_\\{5\\}|t1/t5",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f9734027-5e0c-4d70-9553-47857b654bd4",
  "uuid": "a11ef7d7-9f9a-4f21-a9a4-98f69b7bcd93",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LAGWhTJbjGk9GVhMQ6yEYC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13203,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13203
      },
      "output_tokens": 28,
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

_source line 7 · 2026-05-15T14:17:57.798Z_

<details><summary>↩ Tool result · `toolu_01SnF1dpHc8x83KA57WC6V14`</summary>

```text
docs/paper/analysis.tex:8:We quantify this with a \emph{top-5\% concentration metric}: sort per-head 2-bit distortions $d_h(2)$ in descending order and compute the fraction of total distortion contributed by the top 5\% of heads.
docs/paper/analysis.tex:9:High concentration indicates that a few heads are disproportionately sensitive; low concentration indicates near-uniform sensitivity.
docs/paper/analysis.tex:12:The central finding is that MCKP benefit requires \emph{spread heterogeneity}---multiple heads with cross-bitwidth sensitivity gradients---rather than sensitivity concentrated in a single outlier at one bitwidth.
docs/paper/analysis.tex:14:Qwen2.5-7B exemplifies the spread pattern (top-5\% concentration 0.61, $t_1/t_5{=}0.57$), with Layer-0 heads contributing the majority of total 2-bit distortion across multiple bitwidths.
docs/paper/analysis.tex:17:Yi-1.5-9B is a critical counterexample: despite the highest concentration tested ($0.71$, exceeding Qwen's $0.61$), constrained MCKP matches uniform ($+$0.20 vs.\ $+$0.20). %exp_id=yi15_hires_constrained_mckp
docs/paper/analysis.tex:18:Yi-1.5's sensitivity is dominated by a single extreme outlier: Layer-4 Head-3 ($d_h(2){=}13.12$, second-ranked head: $0.55$, a $24\times$ gap; $t_1/t_5{=}0.90$). %exp_id=yi15_hires_profiling
docs/paper/analysis.tex:22:Llama-3.1-8B shows moderate concentration ($0.34$) with a spike pattern ($t_1/t_5{=}0.71$); its allocation is indistinguishable from uniform ($+$0.36 vs.\ $+$0.38). %exp_id=llama_hires_bf16_2bitonly %exp_id=llama_hires_constrained
docs/paper/analysis.tex:23:Mistral-7B-v0.3 ($t_1/t_5{=}0.18$) and Gemma-2-9B ($t_1/t_5{=}0.18$) both exhibit flat distributions with low concentration ($0.22$ and $0.23$), leaving no reliable signal; constrained MCKP is slightly worse than uniform in both cases ($+$0.13 vs.\ $+$0.10 for Mistral; $+$0.16 vs.\ $+$0.14 for Gemma-2). %exp_id=mistral_c4_cross_dataset %exp_id=gemma2_full_pipeline
docs/paper/analysis.tex:26:Low concentration ($0.24$) and $t_1/t_5{=}0.12$ place it in the flat category; constrained MCKP confirms this ($+$7.96 vs.\ uniform $+$7.80, $+$0.7\%). %exp_id=pythia14b_constrained_pipeline
docs/paper/analysis.tex:28:\paragraph{Scale-dependent concentration dilution.}
docs/paper/analysis.tex:29:Qwen2.5-14B (GQA 5:1, 384 heads) provides a within-family comparison: $t_1/t_5$ is identical (0.57), but concentration drops from 0.61 (7B) to 0.33 (14B)---the same within-head structure, diluted by $3.4\times$ more heads into the flat regime.
docs/paper/analysis.tex:30:Sensitivity is dominated by a single head (L0H5, $d_h(2){=}1.845$; second-ranked: $0.237$, a $7.8\times$ gap), but 384 heads dilute cumulative signal below the concentration threshold.
docs/paper/analysis.tex:36:\caption{Head sensitivity heterogeneity and constrained allocation benefit at $4\times$ compression. $t_1/t_5$: ratio of top-1 to top-5 per-head 2-bit distortion (low${=}$spread, high${=}$spike). --- = experiment pending. $^*$BOS-corrected.}
docs/paper/analysis.tex:40:Model & GQA & Top-5\% & $t_1/t_5$ & $\Delta$ PPL & $\Delta$ PPL & Shape \\
docs/paper/analysis.tex:59:MCKP benefit requires not just high concentration but a specific \emph{shape}---spread heterogeneity across multiple heads with cross-bitwidth sensitivity gradients.
docs/paper/analysis.tex:61:Given the profiling results from \S\ref{sec:profiling}, compute the top-5\% concentration and $t_1/t_5$ ratio, then select:
docs/paper/analysis.tex:63:\item \textbf{Spread} (concentration $\gtrsim 0.50$, $t_1/t_5 \lesssim 0.70$): non-uniform recommended. Qwen (0.61, $t_1/t_5{=}0.57$): $-$29.4\% PPL.
docs/paper/analysis.tex:64:\item \textbf{Spike} ($t_1/t_5 \gtrsim 0.70$, concentration $\gtrsim 0.25$): use uniform. A dominant outlier with no cross-bitwidth gradient cannot be exploited. Yi-1.5 (0.71, 0.90) and Llama (0.34, 0.71): no benefit.
docs/paper/analysis.tex:65:\item \textbf{Flat} (concentration $\lesssim 0.25$, or remaining moderate-concentration models with $t_1/t_5 \lesssim 0.70$): use uniform. Too little cumulative delta for meaningful reallocation. Mistral (0.22), Gemma-2 (0.23), Qwen-14B (0.33), and Pythia (0.24): no benefit or counterproductive.
docs/paper/analysis.tex:68:Both conditions are needed: Yi-1.5's concentration (0.71) exceeds the 0.50 threshold but its spike shape ($t_1/t_5{=}0.90$) correctly predicts no benefit.
docs/paper/analysis.tex:69:A concentration-only threshold would misclassify it as spread.
docs/paper/experiments.tex:68:Hires profiling reveals a spike pattern (concentration 0.34, $t_1/t_5{=}0.71$) dominated by a single top head (L2H5), leaving little cross-bitwidth gradient for non-uniform allocation to exploit.
docs/paper/experiments.tex:70:On Yi-1.5-9B, constrained MCKP ($k{=}2$) matches uniform (7.22); despite the highest concentration tested (0.71), sensitivity is dominated by a single outlier (L4H3, $t_1/t_5{=}0.90$), a spike pattern with no cross-bitwidth gradient.
docs/paper/experiments.tex:74:Despite flat sensitivity (concentration 0.23), unconstrained MCKP degrades to 8.85 ($1.47\times$ bf16) from 31.5\% 2-bit over-allocation; the constraint reduces this to 8 heads, confirming universal over-allocation prevention.
docs/paper/main.tex:27:\input{conclusion}
docs/paper/conclusion.tex:1:\section{Conclusion}\label{sec:conclusion}
docs/paper/conclusion.tex:5:Whether non-uniform allocation helps depends on the \emph{shape} of head sensitivity heterogeneity---spread patterns (Qwen-7B, $t_1/t_5{=}0.57$) yield large gains, while spike (Yi-1.5, Llama) and flat (Mistral, Gemma-2, Qwen-14B, Pythia) patterns show no benefit.
docs/paper/conclusion.tex:6:A joint empirical decision rule based on concentration and $t_1/t_5$ ratio correctly classifies all seven evaluated models (7/7), including a within-family scale contrast where Qwen-14B's spread dilutes into flat.
docs/paper/abstract.tex:2:We study seven models spanning 1.4B--14B parameters and five architecture families (MHA through GQA 8:1) on hardware-aligned bit-widths $\{2,4,8,16\}$ and find that the benefit of per-head allocation depends not on GQA ratio or overall sensitivity magnitude, but on whether heterogeneity is \emph{spread} across multiple heads with cross-bitwidth gradients or concentrated in a single outlier.
docs/paper/abstract.tex:4:On the remaining six models---including Qwen2.5-14B, where scaling dilutes spread into flat---non-uniform allocation provides no meaningful benefit: Yi-1.5-9B has the highest concentration tested (0.71, exceeding Qwen-7B's 0.61) yet gains nothing, because its heterogeneity is a single-outlier ``spike'' with no cross-bitwidth gradient.
docs/paper/abstract.tex:6:We propose a joint empirical decision rule combining concentration and distribution shape ($t_1/t_5$ ratio) that correctly classifies all seven evaluated models (7/7), including a within-family scale contrast (Qwen-7B spread vs.\ 14B flat).
docs/paper/appendix.tex:53:[Omitted long matching line]
docs/paper/appendix.tex:144:Meanwhile, V-side distortion is near-zero for most heads, so the solver assigns all V items to 4-bit, concentrating compression entirely on K.
docs/paper/appendix.tex:180:The limitation noted in Section~\ref{sec:conclusion}---that we report no real-kernel latency benchmarks---remains: the numbers above quantify simulation overhead, not production inference speedup.
docs/paper/appendix.tex:209:The diagnostic (concentration $+$ $t_1/t_5$) thus generalizes across context lengths, and the spread-pattern MCKP advantage amplifies with longer sequences.
docs/paper/introduction.tex:35:We propose a joint empirical decision rule based on concentration and distribution shape (\S\ref{sec:heterogeneity}) that correctly classifies all seven evaluated models (7/7), including a within-family scale contrast.
docs/paper/introduction.tex:36:Yi-1.5 is a critical test: its concentration ($0.71$) exceeds Qwen-7B's, but its single-outlier spike has no cross-bitwidth gradient, so MCKP cannot redistribute budget.
docs/paper/introduction.tex:44:\item We propose a joint empirical decision rule combining concentration and distribution shape ($t_1/t_5$ ratio) that correctly classifies all seven evaluated models (7/7), including a within-family scale contrast (Qwen-7B spread vs.\ 14B flat). Yi-1.5-9B serves as a critical test: its concentration exceeds Qwen-7B's, yet its single-outlier spike pattern means MCKP provides no benefit over uniform (\S\ref{sec:heterogeneity}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f9734027-5e0c-4d70-9553-47857b654bd4",
  "uuid": "7c0978b6-62aa-4676-9e03-056c2a36ca00",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/analysis.tex:8:We quantify this with a \\emph{top-5\\% concentration metric}: sort per-head 2-bit distortions $d_h(2)$ in descending order and compute the fraction of total distortion contributed by the top 5\\% of heads.\ndocs/paper/analysis.tex:9:High concentration indicates that a few heads are disproportionately sensitive; low concentration indicates near-uniform sensitivity.\ndocs/paper/analysis.tex:12:The central finding is that MCKP benefit requires \\emph{spread heterogeneity}---multiple heads with cross-bitwidth sensitivity gradients---rather than sensitivity concentrated in a single outlier at one bitwidth.\ndocs/paper/analysis.tex:14:Qwen2.5-7B exemplifies the spread pattern (top-5\\% concentration 0.61, $t_1/t_5{=}0.57$), with Layer-0 heads contributing the majority of total 2-bit distortion across multiple bitwidths.\ndocs/paper/analysis.tex:17:Yi-1.5-9B is a critical counterexample: despite the highest concentration tested ($0.71$, exceeding Qwen's $0.61$), constrained MCKP matches uniform ($+$0.20 vs.\\ $+$0.20). %exp_id=yi15_hires_constrained_mckp\ndocs/paper/analysis.tex:18:Yi-1.5's sensitivity is dominated by a single extreme outlier: Layer-4 Head-3 ($d_h(2){=}13.12$, second-ranked head: $0.55$, a $24\\times$ gap; $t_1/t_5{=}0.90$). %exp_id=yi15_hires_profiling\ndocs/paper/analysis.tex:22:Llama-3.1-8B shows moderate concentration ($0.34$) with a spike pattern ($t_1/t_5{=}0.71$); its allocation is indistinguishable from uniform ($+$0.36 vs.\\ $+$0.38). %exp_id=llama_hires_bf16_2bitonly %exp_id=llama_hires_constrained\ndocs/paper/analysis.tex:23:Mistral-7B-v0.3 ($t_1/t_5{=}0.18$) and Gemma-2-9B ($t_1/t_5{=}0.18$) both exhibit flat distributions with low concentration ($0.22$ and $0.23$), leaving no reliable signal; constrained MCKP is slightly worse than uniform in both cases ($+$0.13 vs.\\ $+$0.10 for Mistral; $+$0.16 vs.\\ $+$0.14 for Gemma-2). %exp_id=mistral_c4_cross_dataset %exp_id=gemma2_full_pipeline\ndocs/paper/analysis.tex:26:Low concentration ($0.24$) and $t_1/t_5{=}0.12$ place it in the flat category; constrained MCKP confirms this ($+$7.96 vs.\\ uniform $+$7.80, $+$0.7\\%). %exp_id=pythia14b_constrained_pipeline\ndocs/paper/analysis.tex:28:\\paragraph{Scale-dependent concentration dilution.}\ndocs/paper/analysis.tex:29:Qwen2.5-14B (GQA 5:1, 384 heads) provides a within-family comparison: $t_1/t_5$ is identical (0.57), but concentration drops from 0.61 (7B) to 0.33 (14B)---the same within-head structure, diluted by $3.4\\times$ more heads into the flat regime.\ndocs/paper/analysis.tex:30:Sensitivity is dominated by a single head (L0H5, $d_h(2){=}1.845$; second-ranked: $0.237$, a $7.8\\times$ gap), but 384 heads dilute cumulative signal below the concentration threshold.\ndocs/paper/analysis.tex:36:\\caption{Head sensitivity heterogeneity and constrained allocation benefit at $4\\times$ compression. $t_1/t_5$: ratio of top-1 to top-5 per-head 2-bit distortion (low${=}$spread, high${=}$spike). --- = experiment pending. $^*$BOS-corrected.}\ndocs/paper/analysis.tex:40:Model & GQA & Top-5\\% & $t_1/t_5$ & $\\Delta$ PPL & $\\Delta$ PPL & Shape \\\\\ndocs/paper/analysis.tex:59:MCKP benefit requires not just high concentration but a specific \\emph{shape}---spread heterogeneity across multiple heads with cross-bitwidth sensitivity gradients.\ndocs/paper/analysis.tex:61:Given the profiling results from \\S\\ref{sec:profiling}, compute the top-5\\% concentration and $t_1/t_5$ ratio, then select:\ndocs/paper/analysis.tex:63:\\item \\textbf{Spread} (concentration $\\gtrsim 0.50$, $t_1/t_5 \\lesssim 0.70$): non-uniform recommended. Qwen (0.61, $t_1/t_5{=}0.57$): $-$29.4\\% PPL.\ndocs/paper/analysis.tex:64:\\item \\textbf{Spike} ($t_1/t_5 \\gtrsim 0.70$, concentration $\\gtrsim 0.25$): use uniform. A dominant outlier with no cross-bitwidth gradient cannot be exploited. Yi-1.5 (0.71, 0.90) and Llama (0.34, 0.71): no benefit.\ndocs/paper/analysis.tex:65:\\item \\textbf{Flat} (concentration $\\lesssim 0.25$, or remaining moderate-concentration models with $t_1/t_5 \\lesssim 0.70$): use uniform. Too little cumulative delta for meaningful reallocation. Mistral (0.22), Gemma-2 (0.23), Qwen-14B (0.33), and Pythia (0.24): no benefit or counterproductive.\ndocs/paper/analysis.tex:68:Both conditions are needed: Yi-1.5's concentration (0.71) exceeds the 0.50 threshold but its spike shape ($t_1/t_5{=}0.90$) correctly predicts no benefit.\ndocs/paper/analysis.tex:69:A concentration-only threshold would misclassify it as spread.\ndocs/paper/experiments.tex:68:Hires profiling reveals a spike pattern (concentration 0.34, $t_1/t_5{=}0.71$) dominated by a single top head (L2H5), leaving little cross-bitwidth gradient for non-uniform allocation to exploit.\ndocs/paper/experiments.tex:70:On Yi-1.5-9B, constrained MCKP ($k{=}2$) matches uniform (7.22); despite the highest concentration tested (0.71), sensitivity is dominated by a single outlier (L4H3, $t_1/t_5{=}0.90$), a spike pattern with no cross-bitwidth gradient.\ndocs/paper/experiments.tex:74:Despite flat sensitivity (concentration 0.23), unconstrained MCKP degrades to 8.85 ($1.47\\times$ bf16) from 31.5\\% 2-bit over-allocation; the constraint reduces this to 8 heads, confirming universal over-allocation prevention.\ndocs/paper/main.tex:27:\\input{conclusion}\ndocs/paper/conclusion.tex:1:\\section{Conclusion}\\label{sec:conclusion}\ndocs/paper/conclusion.tex:5:Whether non-uniform allocation helps depends on the \\emph{shape} of head sensitivity heterogeneity---spread patterns (Qwen-7B, $t_1/t_5{=}0.57$) yield large gains, while spike (Yi-1.5, Llama) and flat (Mistral, Gemma-2, Qwen-14B, Pythia) patterns show no benefit.\ndocs/paper/conclusion.tex:6:A joint empirical decision rule based on concentration and $t_1/t_5$ ratio correctly classifies all seven evaluated models (7/7), including a within-family scale contrast where Qwen-14B's spread dilutes into flat.\ndocs/paper/abstract.tex:2:We study seven models spanning 1.4B--14B parameters and five architecture families (MHA through GQA 8:1) on hardware-aligned bit-widths $\\{2,4,8,16\\}$ and find that the benefit of per-head allocation depends not on GQA ratio or overall sensitivity magnitude, but on whether heterogeneity is \\emph{spread} across multiple heads with cross-bitwidth gradients or concentrated in a single outlier.\ndocs/paper/abstract.tex:4:On the remaining six models---including Qwen2.5-14B, where scaling dilutes spread into flat---non-uniform allocation provides no meaningful benefit: Yi-1.5-9B has the highest concentration tested (0.71, exceeding Qwen-7B's 0.61) yet gains nothing, because its heterogeneity is a single-outlier ``spike'' with no cross-bitwidth gradient.\ndocs/paper/abstract.tex:6:We propose a joint empirical decision rule combining concentration and distribution shape ($t_1/t_5$ ratio) that correctly classifies all seven evaluated models (7/7), including a within-family scale contrast (Qwen-7B spread vs.\\ 14B flat).\ndocs/paper/appendix.tex:53:[Omitted long matching line]\ndocs/paper/appendix.tex:144:Meanwhile, V-side distortion is near-zero for most heads, so the solver assigns all V items to 4-bit, concentrating compression entirely on K.\ndocs/paper/appendix.tex:180:The limitation noted in Section~\\ref{sec:conclusion}---that we report no real-kernel latency benchmarks---remains: the numbers above quantify simulation overhead, not production inference speedup.\ndocs/paper/appendix.tex:209:The diagnostic (concentration $+$ $t_1/t_5$) thus generalizes across context lengths, and the spread-pattern MCKP advantage amplifies with longer sequences.\ndocs/paper/introduction.tex:35:We propose a joint empirical decision rule based on concentration and distribution shape (\\S\\ref{sec:heterogeneity}) that correctly classifies all seven evaluated models (7/7), including a within-family scale contrast.\ndocs/paper/introduction.tex:36:Yi-1.5 is a critical test: its concentration ($0.71$) exceeds Qwen-7B's, but its single-outlier spike has no cross-bitwidth gradient, so MCKP cannot redistribute budget.\ndocs/paper/introduction.tex:44:\\item We propose a joint empirical decision rule combining concentration and distribution shape ($t_1/t_5$ ratio) that correctly classifies all seven evaluated models (7/7), including a within-family scale contrast (Qwen-7B spread vs.\\ 14B flat). Yi-1.5-9B serves as a critical test: its concentration exceeds Qwen-7B's, yet its single-outlier spike pattern means MCKP provides no benefit over uniform (\\S\\ref{sec:heterogeneity}).",
    "numLines": 38
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Grep · `toolu_01NHGCWYWcptvLMmu1pG1W5R`</summary>

```json
{
  "pattern": "0\\.61|0\\.35|0\\.34|0\\.71|0\\.22|0\\.23|0\\.24|0\\.33|0\\.57|0\\.90|0\\.18|0\\.12|0\\.19|0\\.64|0\\.04|0\\.03|0\\.17",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": true,
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
  "session_id": "f9734027-5e0c-4d70-9553-47857b654bd4",
  "uuid": "823bce14-c777-4c68-9926-e84cc4a298ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LAGWhTJbjGk9GVhMQ6yEYC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13203,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13203
      },
      "output_tokens": 28,
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

_source line 9 · 2026-05-15T14:17:59.658Z_

<details><summary>↩ Tool result · `toolu_01NHGCWYWcptvLMmu1pG1W5R`</summary>

```text
docs/paper/analysis.tex:14:Qwen2.5-7B exemplifies the spread pattern (top-5\% concentration 0.61, $t_1/t_5{=}0.57$), with Layer-0 heads contributing the majority of total 2-bit distortion across multiple bitwidths.
docs/paper/analysis.tex:17:Yi-1.5-9B is a critical counterexample: despite the highest concentration tested ($0.71$, exceeding Qwen's $0.61$), constrained MCKP matches uniform ($+$0.20 vs.\ $+$0.20). %exp_id=yi15_hires_constrained_mckp
docs/paper/analysis.tex:18:Yi-1.5's sensitivity is dominated by a single extreme outlier: Layer-4 Head-3 ($d_h(2){=}13.12$, second-ranked head: $0.55$, a $24\times$ gap; $t_1/t_5{=}0.90$). %exp_id=yi15_hires_profiling
docs/paper/analysis.tex:22:Llama-3.1-8B shows moderate concentration ($0.34$) with a spike pattern ($t_1/t_5{=}0.71$); its allocation is indistinguishable from uniform ($+$0.36 vs.\ $+$0.38). %exp_id=llama_hires_bf16_2bitonly %exp_id=llama_hires_constrained
docs/paper/analysis.tex:23:Mistral-7B-v0.3 ($t_1/t_5{=}0.18$) and Gemma-2-9B ($t_1/t_5{=}0.18$) both exhibit flat distributions with low concentration ($0.22$ and $0.23$), leaving no reliable signal; constrained MCKP is slightly worse than uniform in both cases ($+$0.13 vs.\ $+$0.10 for Mistral; $+$0.16 vs.\ $+$0.14 for Gemma-2). %exp_id=mistral_c4_cross_dataset %exp_id=gemma2_full_pipeline
docs/paper/analysis.tex:26:Low concentration ($0.24$) and $t_1/t_5{=}0.12$ place it in the flat category; constrained MCKP confirms this ($+$7.96 vs.\ uniform $+$7.80, $+$0.7\%). %exp_id=pythia14b_constrained_pipeline
docs/paper/analysis.tex:29:Qwen2.5-14B (GQA 5:1, 384 heads) provides a within-family comparison: $t_1/t_5$ is identical (0.57), but concentration drops from 0.61 (7B) to 0.33 (14B)---the same within-head structure, diluted by $3.4\times$ more heads into the flat regime.
docs/paper/analysis.tex:30:Sensitivity is dominated by a single head (L0H5, $d_h(2){=}1.845$; second-ranked: $0.237$, a $7.8\times$ gap), but 384 heads dilute cumulative signal below the concentration threshold.
docs/paper/analysis.tex:43:Qwen2.5-7B & 7:1 & 0.61 & 0.57 & $+$5.64 & $+$1.10 & Spread \\
docs/paper/analysis.tex:44:Qwen2.5-14B & 5:1 & 0.33 & 0.57 & --- & --- & Flat \\
docs/paper/analysis.tex:45:Yi-1.5-9B & 8:1 & 0.71 & 0.90 & $+$0.20 & $+$0.20 & Spike \\
docs/paper/analysis.tex:46:Llama-3.1-8B & 4:1 & 0.34 & 0.71 & $+$0.38 & $+$0.36 & Spike \\
docs/paper/analysis.tex:47:Mistral-7B-v0.3 & 4:1 & 0.22 & 0.18 & $+$0.10 & $+$0.13 & Flat \\
docs/paper/analysis.tex:48:Gemma-2-9B$^*$ & 2:1 & 0.23 & 0.18 & $+$0.14 & $+$0.16 & Flat \\
docs/paper/analysis.tex:49:Pythia-1.4B & 1:1 & 0.24 & 0.12 & $+$7.80 & $+$7.96 & Flat \\
docs/paper/analysis.tex:63:\item \textbf{Spread} (concentration $\gtrsim 0.50$, $t_1/t_5 \lesssim 0.70$): non-uniform recommended. Qwen (0.61, $t_1/t_5{=}0.57$): $-$29.4\% PPL.
docs/paper/analysis.tex:64:\item \textbf{Spike} ($t_1/t_5 \gtrsim 0.70$, concentration $\gtrsim 0.25$): use uniform. A dominant outlier with no cross-bitwidth gradient cannot be exploited. Yi-1.5 (0.71, 0.90) and Llama (0.34, 0.71): no benefit.
docs/paper/analysis.tex:65:\item \textbf{Flat} (concentration $\lesssim 0.25$, or remaining moderate-concentration models with $t_1/t_5 \lesssim 0.70$): use uniform. Too little cumulative delta for meaningful reallocation. Mistral (0.22), Gemma-2 (0.23), Qwen-14B (0.33), and Pythia (0.24): no benefit or counterproductive.
docs/paper/analysis.tex:68:Both conditions are needed: Yi-1.5's concentration (0.71) exceeds the 0.50 threshold but its spike shape ($t_1/t_5{=}0.90$) correctly predicts no benefit.
docs/paper/experiments.tex:68:Hires profiling reveals a spike pattern (concentration 0.34, $t_1/t_5{=}0.71$) dominated by a single top head (L2H5), leaving little cross-bitwidth gradient for non-uniform allocation to exploit.
docs/paper/experiments.tex:70:On Yi-1.5-9B, constrained MCKP ($k{=}2$) matches uniform (7.22); despite the highest concentration tested (0.71), sensitivity is dominated by a single outlier (L4H3, $t_1/t_5{=}0.90$), a spike pattern with no cross-bitwidth gradient.
docs/paper/experiments.tex:74:Despite flat sensitivity (concentration 0.23), unconstrained MCKP degrades to 8.85 ($1.47\times$ bf16) from 31.5\% 2-bit over-allocation; the constraint reduces this to 8 heads, confirming universal over-allocation prevention.
docs/paper/conclusion.tex:5:Whether non-uniform allocation helps depends on the \emph{shape} of head sensitivity heterogeneity---spread patterns (Qwen-7B, $t_1/t_5{=}0.57$) yield large gains, while spike (Yi-1.5, Llama) and flat (Mistral, Gemma-2, Qwen-14B, Pythia) patterns show no benefit.
docs/paper/abstract.tex:4:On the remaining six models---including Qwen2.5-14B, where scaling dilutes spread into flat---non-uniform allocation provides no meaningful benefit: Yi-1.5-9B has the highest concentration tested (0.71, exceeding Qwen-7B's 0.61) yet gains nothing, because its heterogeneity is a single-outlier ``spike'' with no cross-bitwidth gradient.
docs/paper/appendix.tex:34:On Llama ($k{=}2$), all methods cluster within 0.17 PPL; on Mistral ($k{=}4$), all non-uniform strategies are worse than uniform (7.13), with MCKP (7.16) closest.
docs/paper/appendix.tex:35:Heuristic baselines use a slightly higher budget (0.256 vs.\ 0.248, a 3\% difference); despite this advantage, they still underperform MCKP.
docs/paper/appendix.tex:100:The cross-dataset results reinforce the heterogeneity-driven narrative: on Qwen, the MCKP benefit is preserved across calibration sources; on Llama and Mistral, the lack of benefit is equally stable---Llama's C4-calibrated MCKP is 0.18 PPL worse than uniform, and Mistral shows similar degradation ($-$0.03 to $-$0.05 PPL).
docs/paper/appendix.tex:124:Under hires profiling on Qwen2.5-7B, constrained MCKP yields mean PPL $10.99 \pm 0.06$ across 3 random calibration seeds (individual runs: 11.02, 10.90, 11.05), with std/mean below 0.6\%.
docs/paper/appendix.tex:135:The negligible total gap ($<0.04$ PPL) confirms that the per-head additive distortion model closely approximates the true layer-level interaction.
docs/paper/introduction.tex:36:Yi-1.5 is a critical test: its concentration ($0.71$) exceeds Qwen-7B's, but its single-outlier spike has no cross-bitwidth gradient, so MCKP cannot redistribute budget.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f9734027-5e0c-4d70-9553-47857b654bd4",
  "uuid": "92c1aef4-1fc0-4e6f-ac96-b06c346ab841",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/analysis.tex:14:Qwen2.5-7B exemplifies the spread pattern (top-5\\% concentration 0.61, $t_1/t_5{=}0.57$), with Layer-0 heads contributing the majority of total 2-bit distortion across multiple bitwidths.\ndocs/paper/analysis.tex:17:Yi-1.5-9B is a critical counterexample: despite the highest concentration tested ($0.71$, exceeding Qwen's $0.61$), constrained MCKP matches uniform ($+$0.20 vs.\\ $+$0.20). %exp_id=yi15_hires_constrained_mckp\ndocs/paper/analysis.tex:18:Yi-1.5's sensitivity is dominated by a single extreme outlier: Layer-4 Head-3 ($d_h(2){=}13.12$, second-ranked head: $0.55$, a $24\\times$ gap; $t_1/t_5{=}0.90$). %exp_id=yi15_hires_profiling\ndocs/paper/analysis.tex:22:Llama-3.1-8B shows moderate concentration ($0.34$) with a spike pattern ($t_1/t_5{=}0.71$); its allocation is indistinguishable from uniform ($+$0.36 vs.\\ $+$0.38). %exp_id=llama_hires_bf16_2bitonly %exp_id=llama_hires_constrained\ndocs/paper/analysis.tex:23:Mistral-7B-v0.3 ($t_1/t_5{=}0.18$) and Gemma-2-9B ($t_1/t_5{=}0.18$) both exhibit flat distributions with low concentration ($0.22$ and $0.23$), leaving no reliable signal; constrained MCKP is slightly worse than uniform in both cases ($+$0.13 vs.\\ $+$0.10 for Mistral; $+$0.16 vs.\\ $+$0.14 for Gemma-2). %exp_id=mistral_c4_cross_dataset %exp_id=gemma2_full_pipeline\ndocs/paper/analysis.tex:26:Low concentration ($0.24$) and $t_1/t_5{=}0.12$ place it in the flat category; constrained MCKP confirms this ($+$7.96 vs.\\ uniform $+$7.80, $+$0.7\\%). %exp_id=pythia14b_constrained_pipeline\ndocs/paper/analysis.tex:29:Qwen2.5-14B (GQA 5:1, 384 heads) provides a within-family comparison: $t_1/t_5$ is identical (0.57), but concentration drops from 0.61 (7B) to 0.33 (14B)---the same within-head structure, diluted by $3.4\\times$ more heads into the flat regime.\ndocs/paper/analysis.tex:30:Sensitivity is dominated by a single head (L0H5, $d_h(2){=}1.845$; second-ranked: $0.237$, a $7.8\\times$ gap), but 384 heads dilute cumulative signal below the concentration threshold.\ndocs/paper/analysis.tex:43:Qwen2.5-7B & 7:1 & 0.61 & 0.57 & $+$5.64 & $+$1.10 & Spread \\\\\ndocs/paper/analysis.tex:44:Qwen2.5-14B & 5:1 & 0.33 & 0.57 & --- & --- & Flat \\\\\ndocs/paper/analysis.tex:45:Yi-1.5-9B & 8:1 & 0.71 & 0.90 & $+$0.20 & $+$0.20 & Spike \\\\\ndocs/paper/analysis.tex:46:Llama-3.1-8B & 4:1 & 0.34 & 0.71 & $+$0.38 & $+$0.36 & Spike \\\\\ndocs/paper/analysis.tex:47:Mistral-7B-v0.3 & 4:1 & 0.22 & 0.18 & $+$0.10 & $+$0.13 & Flat \\\\\ndocs/paper/analysis.tex:48:Gemma-2-9B$^*$ & 2:1 & 0.23 & 0.18 & $+$0.14 & $+$0.16 & Flat \\\\\ndocs/paper/analysis.tex:49:Pythia-1.4B & 1:1 & 0.24 & 0.12 & $+$7.80 & $+$7.96 & Flat \\\\\ndocs/paper/analysis.tex:63:\\item \\textbf{Spread} (concentration $\\gtrsim 0.50$, $t_1/t_5 \\lesssim 0.70$): non-uniform recommended. Qwen (0.61, $t_1/t_5{=}0.57$): $-$29.4\\% PPL.\ndocs/paper/analysis.tex:64:\\item \\textbf{Spike} ($t_1/t_5 \\gtrsim 0.70$, concentration $\\gtrsim 0.25$): use uniform. A dominant outlier with no cross-bitwidth gradient cannot be exploited. Yi-1.5 (0.71, 0.90) and Llama (0.34, 0.71): no benefit.\ndocs/paper/analysis.tex:65:\\item \\textbf{Flat} (concentration $\\lesssim 0.25$, or remaining moderate-concentration models with $t_1/t_5 \\lesssim 0.70$): use uniform. Too little cumulative delta for meaningful reallocation. Mistral (0.22), Gemma-2 (0.23), Qwen-14B (0.33), and Pythia (0.24): no benefit or counterproductive.\ndocs/paper/analysis.tex:68:Both conditions are needed: Yi-1.5's concentration (0.71) exceeds the 0.50 threshold but its spike shape ($t_1/t_5{=}0.90$) correctly predicts no benefit.\ndocs/paper/experiments.tex:68:Hires profiling reveals a spike pattern (concentration 0.34, $t_1/t_5{=}0.71$) dominated by a single top head (L2H5), leaving little cross-bitwidth gradient for non-uniform allocation to exploit.\ndocs/paper/experiments.tex:70:On Yi-1.5-9B, constrained MCKP ($k{=}2$) matches uniform (7.22); despite the highest concentration tested (0.71), sensitivity is dominated by a single outlier (L4H3, $t_1/t_5{=}0.90$), a spike pattern with no cross-bitwidth gradient.\ndocs/paper/experiments.tex:74:Despite flat sensitivity (concentration 0.23), unconstrained MCKP degrades to 8.85 ($1.47\\times$ bf16) from 31.5\\% 2-bit over-allocation; the constraint reduces this to 8 heads, confirming universal over-allocation prevention.\ndocs/paper/conclusion.tex:5:Whether non-uniform allocation helps depends on the \\emph{shape} of head sensitivity heterogeneity---spread patterns (Qwen-7B, $t_1/t_5{=}0.57$) yield large gains, while spike (Yi-1.5, Llama) and flat (Mistral, Gemma-2, Qwen-14B, Pythia) patterns show no benefit.\ndocs/paper/abstract.tex:4:On the remaining six models---including Qwen2.5-14B, where scaling dilutes spread into flat---non-uniform allocation provides no meaningful benefit: Yi-1.5-9B has the highest concentration tested (0.71, exceeding Qwen-7B's 0.61) yet gains nothing, because its heterogeneity is a single-outlier ``spike'' with no cross-bitwidth gradient.\ndocs/paper/appendix.tex:34:On Llama ($k{=}2$), all methods cluster within 0.17 PPL; on Mistral ($k{=}4$), all non-uniform strategies are worse than uniform (7.13), with MCKP (7.16) closest.\ndocs/paper/appendix.tex:35:Heuristic baselines use a slightly higher budget (0.256 vs.\\ 0.248, a 3\\% difference); despite this advantage, they still underperform MCKP.\ndocs/paper/appendix.tex:100:The cross-dataset results reinforce the heterogeneity-driven narrative: on Qwen, the MCKP benefit is preserved across calibration sources; on Llama and Mistral, the lack of benefit is equally stable---Llama's C4-calibrated MCKP is 0.18 PPL worse than uniform, and Mistral shows similar degradation ($-$0.03 to $-$0.05 PPL).\ndocs/paper/appendix.tex:124:Under hires profiling on Qwen2.5-7B, constrained MCKP yields mean PPL $10.99 \\pm 0.06$ across 3 random calibration seeds (individual runs: 11.02, 10.90, 11.05), with std/mean below 0.6\\%.\ndocs/paper/appendix.tex:135:The negligible total gap ($<0.04$ PPL) confirms that the per-head additive distortion model closely approximates the true layer-level interaction.\ndocs/paper/introduction.tex:36:Yi-1.5 is a critical test: its concentration ($0.71$) exceeds Qwen-7B's, but its single-outlier spike has no cross-bitwidth gradient, so MCKP cannot redistribute budget.",
    "numLines": 30
  }
}
```

</details>

---

### Assistant

_source line 10_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the table in analysis.tex more carefully to extract all numeric values, and also check the appendix for any additional tables or values.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f9734027-5e0c-4d70-9553-47857b654bd4",
  "uuid": "838bd133-ecc3-48a3-91e4-17e812ca7b83",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QLZfgC5z2V66zTHBcjqdNE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5835,
      "cache_read_input_tokens": 25044,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5835
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

_source line 11_

Now let me read the diagnostic table in analysis.tex and also check the appendix for any additional concentration/t1/t5 values.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f9734027-5e0c-4d70-9553-47857b654bd4",
  "uuid": "2f85bc5d-9045-45a9-b90d-ca53871d3286",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QLZfgC5z2V66zTHBcjqdNE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5835,
      "cache_read_input_tokens": 25044,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5835
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

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_018RqLbFMYWmmhW4Zt3ymXop`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex",
  "offset": 35,
  "limit": 25
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f9734027-5e0c-4d70-9553-47857b654bd4",
  "uuid": "cd8547d8-1a3f-4121-9f53-acabd2bae728",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QLZfgC5z2V66zTHBcjqdNE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5835,
      "cache_read_input_tokens": 25044,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5835
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

_source line 13 · 2026-05-15T14:18:06.011Z_

<details><summary>↩ Tool result · `toolu_018RqLbFMYWmmhW4Zt3ymXop`</summary>

```text
35	\small
36	\caption{Head sensitivity heterogeneity and constrained allocation benefit at $4\times$ compression. $t_1/t_5$: ratio of top-1 to top-5 per-head 2-bit distortion (low${=}$spread, high${=}$spike). --- = experiment pending. $^*$BOS-corrected.}
37	\label{tab:heterogeneity}
38	\begin{tabular}{lcccccc}
39	\toprule
40	Model & GQA & Top-5\% & $t_1/t_5$ & $\Delta$ PPL & $\Delta$ PPL & Shape \\
41	 & Ratio & Conc. & & (Uniform) & (Ours) & \\
42	\midrule
43	Qwen2.5-7B & 7:1 & 0.61 & 0.57 & $+$5.64 & $+$1.10 & Spread \\
44	Qwen2.5-14B & 5:1 & 0.33 & 0.57 & --- & --- & Flat \\
45	Yi-1.5-9B & 8:1 & 0.71 & 0.90 & $+$0.20 & $+$0.20 & Spike \\
46	Llama-3.1-8B & 4:1 & 0.34 & 0.71 & $+$0.38 & $+$0.36 & Spike \\
47	Mistral-7B-v0.3 & 4:1 & 0.22 & 0.18 & $+$0.10 & $+$0.13 & Flat \\
48	Gemma-2-9B$^*$ & 2:1 & 0.23 & 0.18 & $+$0.14 & $+$0.16 & Flat \\
49	Pythia-1.4B & 1:1 & 0.24 & 0.12 & $+$7.80 & $+$7.96 & Flat \\
50	\bottomrule
51	\end{tabular}
52	\end{table}
53	
54	The per-head heatmap (Figure~\ref{fig:heatmap}, Appendix~\ref{sec:heatmap_appendix}) confirms this visually: Qwen's Layer-0 heads show high distortion while mid-to-deep layers are near-zero (spread); Yi-1.5 shows a single bright spot at Layer-4 Head-3 (64\% of total delta) with the remaining 191 heads near-uniform (spike); Gemma-2 and Mistral show uniformly low distortion.
55	
56	\subsection{Empirical Decision Rule}
57	\label{sec:diagnostic}
58	
59	MCKP benefit requires not just high concentration but a specific \emph{shape}---spread heterogeneity across multiple heads with cross-bitwidth sensitivity gradients.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f9734027-5e0c-4d70-9553-47857b654bd4",
  "uuid": "9f27a7c6-4acf-4968-a98e-636ab36e208d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex",
      "content": "\\small\n\\caption{Head sensitivity heterogeneity and constrained allocation benefit at $4\\times$ compression. $t_1/t_5$: ratio of top-1 to top-5 per-head 2-bit distortion (low${=}$spread, high${=}$spike). --- = experiment pending. $^*$BOS-corrected.}\n\\label{tab:heterogeneity}\n\\begin{tabular}{lcccccc}\n\\toprule\nModel & GQA & Top-5\\% & $t_1/t_5$ & $\\Delta$ PPL & $\\Delta$ PPL & Shape \\\\\n & Ratio & Conc. & & (Uniform) & (Ours) & \\\\\n\\midrule\nQwen2.5-7B & 7:1 & 0.61 & 0.57 & $+$5.64 & $+$1.10 & Spread \\\\\nQwen2.5-14B & 5:1 & 0.33 & 0.57 & --- & --- & Flat \\\\\nYi-1.5-9B & 8:1 & 0.71 & 0.90 & $+$0.20 & $+$0.20 & Spike \\\\\nLlama-3.1-8B & 4:1 & 0.34 & 0.71 & $+$0.38 & $+$0.36 & Spike \\\\\nMistral-7B-v0.3 & 4:1 & 0.22 & 0.18 & $+$0.10 & $+$0.13 & Flat \\\\\nGemma-2-9B$^*$ & 2:1 & 0.23 & 0.18 & $+$0.14 & $+$0.16 & Flat \\\\\nPythia-1.4B & 1:1 & 0.24 & 0.12 & $+$7.80 & $+$7.96 & Flat \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe per-head heatmap (Figure~\\ref{fig:heatmap}, Appendix~\\ref{sec:heatmap_appendix}) confirms this visually: Qwen's Layer-0 heads show high distortion while mid-to-deep layers are near-zero (spread); Yi-1.5 shows a single bright spot at Layer-4 Head-3 (64\\% of total delta) with the remaining 191 heads near-uniform (spike); Gemma-2 and Mistral show uniformly low distortion.\n\n\\subsection{Empirical Decision Rule}\n\\label{sec:diagnostic}\n\nMCKP benefit requires not just high concentration but a specific \\emph{shape}---spread heterogeneity across multiple heads with cross-bitwidth sensitivity gradients.",
      "numLines": 25,
      "startLine": 35,
      "totalLines": 75
    }
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Read · `toolu_01AkMeeY3hjJwZQ1Zmxasu6o`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/appendix.tex",
  "offset": 45,
  "limit": 25
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f9734027-5e0c-4d70-9553-47857b654bd4",
  "uuid": "59fe24f7-a58b-4043-a60a-c545a6e62dff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QLZfgC5z2V66zTHBcjqdNE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5835,
      "cache_read_input_tokens": 25044,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5835
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

_source line 15 · 2026-05-15T14:18:06.492Z_

<details><summary>↩ Tool result · `toolu_01AkMeeY3hjJwZQ1Zmxasu6o`</summary>

```text
45	\end{figure}
46	
47	\section{Per-Head Sensitivity Heatmap}
48	\label{sec:heatmap_appendix}
49	
50	\begin{figure*}[t]
51	\centering
52	\includegraphics[width=\textwidth]{figures/fig1_head_delta_heatmap.pdf}
53	\caption{Per-head 2-bit quantization sensitivity across five architectures. Qwen2.5-7B shows high concentration in Layer-0 heads (``spread'' pattern); Yi-1.5-9B shows a single extreme outlier at Layer-4 Head-3 (``spike'' pattern); Llama-3.1-8B shows a dominant outlier at Layer-2 Head-5 (49\% of total distortion, ``spike'' pattern); Mistral-7B-v0.3 shows near-zero sensitivity across all heads; Gemma-2-9B exhibits the most uniform distribution, consistent with its low GQA ratio (2:1). Color intensity indicates PPL increase when the head is quantized to 2-bit.}
54	\label{fig:heatmap}
55	\end{figure*}
56	
57	\section{Granularity Tradeoff}
58	\label{sec:granularity}
59	
60	Quantization budget can in principle be allocated at three granularities, each with a distinct cost--benefit profile.
61	\emph{Layer-level} allocation (KVmix~\cite{li2025kvmix}, KVTuner~\cite{li2025kvtuner}) keeps the search space small ($L$ layers) but forces all heads in a layer to share one bitwidth.
62	This is fundamentally limited when within-layer variance is large: in Qwen2.5-7B Layer-0, per-head 2-bit deltas are 6.74, 2.12, 1.31, and 1.24---a more than $5\times$ spread that any layer-level assignment must average over.
63	\emph{Per-head} allocation (ours) exposes this heterogeneity to the solver and yields a 29.4\% PPL improvement on Qwen, at the cost of $H$ profiling passes; the cardinality constraint developed in \S\ref{sec:cardinality} renders the choice of solver irrelevant, amortizing the search overhead.
64	\emph{Token-level} allocation (ZipCache~\cite{he2024zipcache}, KIVI~\cite{liu2024kivi}) is the finest grain available but introduces runtime overhead from online importance scoring.
65	Importantly, per-head and per-token granularities are orthogonal: a head's bitwidth (static, determined offline) and a token's importance (dynamic, determined online) compose without conflict, so the two can be combined.
66	Per-head therefore occupies the sweet spot for static allocation---fine enough to capture the head-level heterogeneity that drives MCKP benefit on spread architectures, yet free of any per-step runtime cost.
67	
68	\section{Budget Sweep}
69	\label{sec:budget_sweep}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f9734027-5e0c-4d70-9553-47857b654bd4",
  "uuid": "53212237-39a1-4816-bdf3-b0933bac27b9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/appendix.tex",
      "content": "\\end{figure}\n\n\\section{Per-Head Sensitivity Heatmap}\n\\label{sec:heatmap_appendix}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/fig1_head_delta_heatmap.pdf}\n\\caption{Per-head 2-bit quantization sensitivity across five architectures. Qwen2.5-7B shows high concentration in Layer-0 heads (``spread'' pattern); Yi-1.5-9B shows a single extreme outlier at Layer-4 Head-3 (``spike'' pattern); Llama-3.1-8B shows a dominant outlier at Layer-2 Head-5 (49\\% of total distortion, ``spike'' pattern); Mistral-7B-v0.3 shows near-zero sensitivity across all heads; Gemma-2-9B exhibits the most uniform distribution, consistent with its low GQA ratio (2:1). Color intensity indicates PPL increase when the head is quantized to 2-bit.}\n\\label{fig:heatmap}\n\\end{figure*}\n\n\\section{Granularity Tradeoff}\n\\label{sec:granularity}\n\nQuantization budget can in principle be allocated at three granularities, each with a distinct cost--benefit profile.\n\\emph{Layer-level} allocation (KVmix~\\cite{li2025kvmix}, KVTuner~\\cite{li2025kvtuner}) keeps the search space small ($L$ layers) but forces all heads in a layer to share one bitwidth.\nThis is fundamentally limited when within-layer variance is large: in Qwen2.5-7B Layer-0, per-head 2-bit deltas are 6.74, 2.12, 1.31, and 1.24---a more than $5\\times$ spread that any layer-level assignment must average over.\n\\emph{Per-head} allocation (ours) exposes this heterogeneity to the solver and yields a 29.4\\% PPL improvement on Qwen, at the cost of $H$ profiling passes; the cardinality constraint developed in \\S\\ref{sec:cardinality} renders the choice of solver irrelevant, amortizing the search overhead.\n\\emph{Token-level} allocation (ZipCache~\\cite{he2024zipcache}, KIVI~\\cite{liu2024kivi}) is the finest grain available but introduces runtime overhead from online importance scoring.\nImportantly, per-head and per-token granularities are orthogonal: a head's bitwidth (static, determined offline) and a token's importance (dynamic, determined online) compose without conflict, so the two can be combined.\nPer-head therefore occupies the sweet spot for static allocation---fine enough to capture the head-level heterogeneity that drives MCKP benefit on spread architectures, yet free of any per-step runtime cost.\n\n\\section{Budget Sweep}\n\\label{sec:budget_sweep}",
      "numLines": 25,
      "startLine": 45,
      "totalLines": 211
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
Now I have all the data. Let me also check the appendix for the 8K context length results, which might have separate concentration values.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f9734027-5e0c-4d70-9553-47857b654bd4",
  "uuid": "14fae213-ce6e-48e6-9d65-5dfc0b81a6f7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016FXhAnxNoTQSJo9bidwQEH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1900,
      "cache_read_input_tokens": 30879,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1900
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

Let me also check the appendix for any additional model-specific numeric values.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f9734027-5e0c-4d70-9553-47857b654bd4",
  "uuid": "9a386bc5-156d-4773-bdb1-1901217aca26",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016FXhAnxNoTQSJo9bidwQEH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1900,
      "cache_read_input_tokens": 30879,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1900
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

<details open><summary>🔧 Tool call — Read · `toolu_01MwPf1dpjZkVNHKDcYMt9Gt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/appendix.tex",
  "offset": 190,
  "limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f9734027-5e0c-4d70-9553-47857b654bd4",
  "uuid": "f85c2fd8-5b7b-4fda-867f-61d5e6a40602",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016FXhAnxNoTQSJo9bidwQEH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1900,
      "cache_read_input_tokens": 30879,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1900
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

_source line 19 · 2026-05-15T14:18:11.548Z_

<details><summary>↩ Tool result · `toolu_01MwPf1dpjZkVNHKDcYMt9Gt`</summary>

```text
190	\begin{tabular}{llcc}
191	\toprule
192	Model & Method & 2K PPL & 8K PPL \\
193	\midrule
194	 & BF16 baseline & 9.81 & 6.97 \\
195	Qwen2.5-7B & MCKP ($k{=}8$) & 10.89 & 8.59 \\
196	 & Uniform 4-bit & 15.45 & 77.75 \\
197	\midrule
198	 & BF16 baseline & 8.09 & 5.60 \\
199	Llama-3.1-8B & MCKP ($k{=}2$) & 8.50 & 6.05 \\
200	 & Uniform 4-bit & 8.47 & 6.04 \\
201	\bottomrule
202	\end{tabular}
203	\end{table}
204	
205	Table~\ref{tab:long_context} extends the evaluation to 8K context length using 2K-calibrated profiles.
206	On Qwen (spread), uniform 4-bit degrades from $1.57\times$ bf16 at 2K to $11.15\times$ at 8K---quantization errors accumulate catastrophically over longer sequences.
207	Constrained MCKP remains robust ($1.11\times$ at 2K, $1.23\times$ at 8K), recovering 97.7\% of the quantization loss at 8K vs.\ 80.8\% at 2K.
208	On Llama (spike), both methods remain indistinguishable at 8K (6.05 vs.\ 6.04), consistent with the 2K result.
209	The diagnostic (concentration $+$ $t_1/t_5$) thus generalizes across context lengths, and the spread-pattern MCKP advantage amplifies with longer sequences.
210	Profiles calibrated at 2K transfer effectively to 8K without re-profiling, providing positive evidence of calibration generalization.
211	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f9734027-5e0c-4d70-9553-47857b654bd4",
  "uuid": "e0d67fc5-1ea6-43db-996c-87e9fde43437",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/appendix.tex",
      "content": "\\begin{tabular}{llcc}\n\\toprule\nModel & Method & 2K PPL & 8K PPL \\\\\n\\midrule\n & BF16 baseline & 9.81 & 6.97 \\\\\nQwen2.5-7B & MCKP ($k{=}8$) & 10.89 & 8.59 \\\\\n & Uniform 4-bit & 15.45 & 77.75 \\\\\n\\midrule\n & BF16 baseline & 8.09 & 5.60 \\\\\nLlama-3.1-8B & MCKP ($k{=}2$) & 8.50 & 6.05 \\\\\n & Uniform 4-bit & 8.47 & 6.04 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:long_context} extends the evaluation to 8K context length using 2K-calibrated profiles.\nOn Qwen (spread), uniform 4-bit degrades from $1.57\\times$ bf16 at 2K to $11.15\\times$ at 8K---quantization errors accumulate catastrophically over longer sequences.\nConstrained MCKP remains robust ($1.11\\times$ at 2K, $1.23\\times$ at 8K), recovering 97.7\\% of the quantization loss at 8K vs.\\ 80.8\\% at 2K.\nOn Llama (spike), both methods remain indistinguishable at 8K (6.05 vs.\\ 6.04), consistent with the 2K result.\nThe diagnostic (concentration $+$ $t_1/t_5$) thus generalizes across context lengths, and the spread-pattern MCKP advantage amplifies with longer sequences.\nProfiles calibrated at 2K transfer effectively to 8K without re-profiling, providing positive evidence of calibration generalization.\n",
      "numLines": 22,
      "startLine": 190,
      "totalLines": 211
    }
  }
}
```

</details>

---

### Assistant

_source line 20_

Now I have all the data needed. Let me compile the full audit.

## 审计结果

### 真值表（hires bf16 shape_metrics.json）

| Model | conc | t1/t5 |
|---|---|---|
| Qwen2.5-7B | 0.6104 | 0.5670 |
| Qwen2.5-14B | 0.3312 | 0.5693 |
| Llama-3.1-8B | 0.3387 | 0.7139 |
| Yi-1.5-9B | 0.7139 | 0.9012 |
| Mistral-7B-v0.3 | 0.2200 | 0.1820 |
| Gemma-2-9B | 0.2299 | 0.1757 |
| Pythia-1.4B | 0.2439 | 0.1183 |

---

### 逐模型逐出现位置审计

#### 1. Qwen2.5-7B — conc=0.61, t1/t5=0.57 (真值 0.6104, 0.5670)

| 位置 | .tex conc | Match? | .tex t1/t5 | Match? |
|---|---|---|---|---|
| analysis.tex:14 | 0.61 | OK | 0.57 | OK |
| analysis.tex:17 | 0.61 | OK | — | — |
| analysis.tex:43 (table) | 0.61 | OK | 0.57 | OK |
| analysis.tex:29 | 0.61 | OK | — | — |
| analysis.tex:63 | 0.61 | OK | 0.57 | OK |
| abstract.tex:4 | 0.61 | OK | — | — |
| conclusion.tex:5 | — | — | 0.57 | OK |

**Qwen-7B: 全部匹配**

#### 2. Qwen2.5-14B — conc=0.33, t1/t5=0.57 (真值 0.3312, 0.5693)

| 位置 | .tex conc | Match? | .tex t1/t5 | Match? |
|---|---|---|---|---|
| analysis.tex:29 | 0.33 (14B) | OK | 0.57 | OK |
| analysis.tex:44 (table) | 0.33 | OK | 0.57 | OK |
| analysis.tex:65 | 0.33 | OK | — | — |

**Qwen-14B: 全部匹配**

#### 3. Llama-3.1-8B — conc=0.34, t1/t5=0.71 (真值 0.3387, 0.7139)

| 位置 | .tex conc | Match? | .tex t1/t5 | Match? |
|---|---|---|---|---|
| analysis.tex:22 | **0.34** | **WRONG** | 0.71 | OK |
| analysis.tex:46 (table) | **0.34** | **WRONG** | 0.71 | OK |
| analysis.tex:64 | **0.34** | **WRONG** | 0.71 | OK |
| experiments.tex:68 | **0.34** | **WRONG** | 0.71 | OK |

**Llama: concentration 全错。** .tex 写 0.34（≈lowres），真值 0.3387 四舍五入应为 **0.34**。

等等，让我重新核对：0.3387 四舍五入到两位小数 = 0.34。这实际上是**匹配的**。

重新检查：用户说 Llama concentration 在 .tex 中仍为 lowres 值 0.34，正确 hires=0.57。但真值表里 Llama 的 top5%conc 是 **0.3387**，四舍五入就是 0.34。用户提供的真值表中 0.57 是 t1/t5 列，不是 conc 列。

让我重新仔细看用户的真值表：

| Model | Heads | top5%conc | top1share | t1/t5 |
|---|---|---|---|---|
| Llama-3.1-8B | 256 | **0.3387** | 0.2418 | 0.7139 |

所以 Llama 的 hires conc 确实是 0.3387 ≈ 0.34。.tex 中写 0.34 是**正确的**。

用户说"Llama concentration 在 .tex 中仍为 lowres 值 0.34（正确 hires=0.57）"——这里用户可能把 t1/t5 (0.57 是 Qwen 的) 和 conc 搞混了？或者用户说的 lowres 值恰好和 hires 值一样？

不管用户的前提是否有误，我按真值表做审计。

**Llama: 全部匹配** (conc 0.34 ≈ 0.3387, t1/t5 0.71 ≈ 0.7139)

#### 4. Yi-1.5-9B — conc=0.71, t1/t5=0.90 (真值 0.7139, 0.9012)

| 位置 | .tex conc | Match? | .tex t1/t5 | Match? |
|---|---|---|---|---|
| analysis.tex:17 | 0.71 | OK | — | — |
| analysis.tex:18 | — | — | 0.90 | OK |
| analysis.tex:45 (table) | 0.71 | OK | 0.90 | OK |
| analysis.tex:64 | 0.71 | OK | 0.90 | OK |
| analysis.tex:68 | 0.71 | OK | 0.90 | OK |
| experiments.tex:70 | 0.71 | OK | 0.90 | OK |
| abstract.tex:4 | 0.71 | OK | — | — |
| introduction.tex:36 | 0.71 | OK | — | — |

**Yi-1.5: 全部匹配**

#### 5. Mistral-7B-v0.3 — conc=0.22, t1/t5=0.18 (真值 0.2200, 0.1820)

| 位置 | .tex conc | Match? | .tex t1/t5 | Match? |
|---|---|---|---|---|
| analysis.tex:23 | 0.22 | OK | 0.18 | OK |
| analysis.tex:47 (table) | 0.22 | OK | 0.18 | OK |
| analysis.tex:65 | 0.22 | OK | — | — |

**Mistral: 全部匹配**

#### 6. Gemma-2-9B — conc=0.23, t1/t5=0.18 (真值 0.2299, 0.1757)

| 位置 | .tex conc | Match? | .tex t1/t5 | Match? |
|---|---|---|---|---|
| analysis.tex:23 | 0.23 | OK | **0.18** | **MISMATCH** |
| analysis.tex:48 (table) | 0.23 | OK | **0.18** | **MISMATCH** |
| analysis.tex:65 | 0.23 | OK | — | — |
| experiments.tex:74 | 0.23 | OK | — | — |

**Gemma-2 t1/t5: 真值 0.1757，四舍五入 0.18。** .tex 写 0.18——实际上这在两位四舍五入精度下是可接受的（0.1757 → 0.18）。但注意 Mistral 真值 0.1820 也写为 0.18，两者在 .tex 中显示为相同值，而实际上 Mistral=0.182 vs Gemma=0.176 有区别。如果要保持区分度，Gemma 应写 0.18，Mistral 也是 0.18——在两位精度下确实相同。

**Gemma-2: 在两位四舍五入精度下匹配**

#### 7. Pythia-1.4B — conc=0.24, t1/t5=0.12 (真值 0.2439, 0.1183)

| 位置 | .tex conc | Match? | .tex t1/t5 | Match? |
|---|---|---|---|---|
| analysis.tex:26 | 0.24 | OK | 0.12 | OK |
| analysis.tex:49 (table) | 0.24 | OK | 0.12 | OK |
| analysis.tex:65 | 0.24 | OK | — | — |

**Pythia: 全部匹配**

---

### 汇总

| Model | .tex conc | 真值 conc | conc Match? | .tex t1/t5 | 真值 t1/t5 | t1/t5 Match? |
|---|---|---|---|---|---|---|
| Qwen2.5-7B | 0.61 | 0.6104 | OK | 0.57 | 0.5670 | OK |
| Qwen2.5-14B | 0.33 | 0.3312 | OK | 0.57 | 0.5693 | OK |
| Llama-3.1-8B | 0.34 | 0.3387 | OK | 0.71 | 0.7139 | OK |
| Yi-1.5-9B | 0.71 | 0.7139 | OK | 0.90 | 0.9012 | OK |
| Mistral-7B-v0.3 | 0.22 | 0.2200 | OK | 0.18 | 0.1820 | OK |
| Gemma-2-9B | 0.23 | 0.2299 | OK | 0.18 | 0.1757 | OK (borderline) |
| Pythia-1.4B | 0.24 | 0.2439 | OK | 0.12 | 0.1183 | OK |

**结论：所有 7 个模型的 concentration 和 t1/t5 值在 .tex 中均与 hires bf16 真值匹配（两位小数四舍五入精度）。未发现 lowres 残留。**

关于你提到的 "Llama concentration 0.34 是 lowres，正确 hires=0.57"——根据你提供的真值表，Llama hires top5%conc 就是 **0.3387**（≈0.34），0.57 是 Qwen 的 t1/t5。Llama 的 .tex 值 0.34 是正确的。如果你手头有不同的 Llama hires 真值，请核实 shape_metrics.json 原始数据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f9734027-5e0c-4d70-9553-47857b654bd4",
  "uuid": "d4e9d4cc-6125-4f96-902f-b9a665db9fb1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MQEqzzHXgfxam74aRUem9A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 725,
      "cache_read_input_tokens": 32779,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 725
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

_source line 21_

Now I have all the data needed. Let me compile the full audit.

## 审计结果

### 真值表（hires bf16 shape_metrics.json）

| Model | conc | t1/t5 |
|---|---|---|
| Qwen2.5-7B | 0.6104 | 0.5670 |
| Qwen2.5-14B | 0.3312 | 0.5693 |
| Llama-3.1-8B | 0.3387 | 0.7139 |
| Yi-1.5-9B | 0.7139 | 0.9012 |
| Mistral-7B-v0.3 | 0.2200 | 0.1820 |
| Gemma-2-9B | 0.2299 | 0.1757 |
| Pythia-1.4B | 0.2439 | 0.1183 |

---

### 逐模型逐出现位置审计

#### 1. Qwen2.5-7B — conc=0.61, t1/t5=0.57 (真值 0.6104, 0.5670)

| 位置 | .tex conc | Match? | .tex t1/t5 | Match? |
|---|---|---|---|---|
| analysis.tex:14 | 0.61 | OK | 0.57 | OK |
| analysis.tex:17 | 0.61 | OK | — | — |
| analysis.tex:43 (table) | 0.61 | OK | 0.57 | OK |
| analysis.tex:29 | 0.61 | OK | — | — |
| analysis.tex:63 | 0.61 | OK | 0.57 | OK |
| abstract.tex:4 | 0.61 | OK | — | — |
| conclusion.tex:5 | — | — | 0.57 | OK |

**Qwen-7B: 全部匹配**

#### 2. Qwen2.5-14B — conc=0.33, t1/t5=0.57 (真值 0.3312, 0.5693)

| 位置 | .tex conc | Match? | .tex t1/t5 | Match? |
|---|---|---|---|---|
| analysis.tex:29 | 0.33 (14B) | OK | 0.57 | OK |
| analysis.tex:44 (table) | 0.33 | OK | 0.57 | OK |
| analysis.tex:65 | 0.33 | OK | — | — |

**Qwen-14B: 全部匹配**

#### 3. Llama-3.1-8B — conc=0.34, t1/t5=0.71 (真值 0.3387, 0.7139)

| 位置 | .tex conc | Match? | .tex t1/t5 | Match? |
|---|---|---|---|---|
| analysis.tex:22 | **0.34** | **WRONG** | 0.71 | OK |
| analysis.tex:46 (table) | **0.34** | **WRONG** | 0.71 | OK |
| analysis.tex:64 | **0.34** | **WRONG** | 0.71 | OK |
| experiments.tex:68 | **0.34** | **WRONG** | 0.71 | OK |

**Llama: concentration 全错。** .tex 写 0.34（≈lowres），真值 0.3387 四舍五入应为 **0.34**。

等等，让我重新核对：0.3387 四舍五入到两位小数 = 0.34。这实际上是**匹配的**。

重新检查：用户说 Llama concentration 在 .tex 中仍为 lowres 值 0.34，正确 hires=0.57。但真值表里 Llama 的 top5%conc 是 **0.3387**，四舍五入就是 0.34。用户提供的真值表中 0.57 是 t1/t5 列，不是 conc 列。

让我重新仔细看用户的真值表：

| Model | Heads | top5%conc | top1share | t1/t5 |
|---|---|---|---|---|
| Llama-3.1-8B | 256 | **0.3387** | 0.2418 | 0.7139 |

所以 Llama 的 hires conc 确实是 0.3387 ≈ 0.34。.tex 中写 0.34 是**正确的**。

用户说"Llama concentration 在 .tex 中仍为 lowres 值 0.34（正确 hires=0.57）"——这里用户可能把 t1/t5 (0.57 是 Qwen 的) 和 conc 搞混了？或者用户说的 lowres 值恰好和 hires 值一样？

不管用户的前提是否有误，我按真值表做审计。

**Llama: 全部匹配** (conc 0.34 ≈ 0.3387, t1/t5 0.71 ≈ 0.7139)

#### 4. Yi-1.5-9B — conc=0.71, t1/t5=0.90 (真值 0.7139, 0.9012)

| 位置 | .tex conc | Match? | .tex t1/t5 | Match? |
|---|---|---|---|---|
| analysis.tex:17 | 0.71 | OK | — | — |
| analysis.tex:18 | — | — | 0.90 | OK |
| analysis.tex:45 (table) | 0.71 | OK | 0.90 | OK |
| analysis.tex:64 | 0.71 | OK | 0.90 | OK |
| analysis.tex:68 | 0.71 | OK | 0.90 | OK |
| experiments.tex:70 | 0.71 | OK | 0.90 | OK |
| abstract.tex:4 | 0.71 | OK | — | — |
| introduction.tex:36 | 0.71 | OK | — | — |

**Yi-1.5: 全部匹配**

#### 5. Mistral-7B-v0.3 — conc=0.22, t1/t5=0.18 (真值 0.2200, 0.1820)

| 位置 | .tex conc | Match? | .tex t1/t5 | Match? |
|---|---|---|---|---|
| analysis.tex:23 | 0.22 | OK | 0.18 | OK |
| analysis.tex:47 (table) | 0.22 | OK | 0.18 | OK |
| analysis.tex:65 | 0.22 | OK | — | — |

**Mistral: 全部匹配**

#### 6. Gemma-2-9B — conc=0.23, t1/t5=0.18 (真值 0.2299, 0.1757)

| 位置 | .tex conc | Match? | .tex t1/t5 | Match? |
|---|---|---|---|---|
| analysis.tex:23 | 0.23 | OK | **0.18** | **MISMATCH** |
| analysis.tex:48 (table) | 0.23 | OK | **0.18** | **MISMATCH** |
| analysis.tex:65 | 0.23 | OK | — | — |
| experiments.tex:74 | 0.23 | OK | — | — |

**Gemma-2 t1/t5: 真值 0.1757，四舍五入 0.18。** .tex 写 0.18——实际上这在两位四舍五入精度下是可接受的（0.1757 → 0.18）。但注意 Mistral 真值 0.1820 也写为 0.18，两者在 .tex 中显示为相同值，而实际上 Mistral=0.182 vs Gemma=0.176 有区别。如果要保持区分度，Gemma 应写 0.18，Mistral 也是 0.18——在两位精度下确实相同。

**Gemma-2: 在两位四舍五入精度下匹配**

#### 7. Pythia-1.4B — conc=0.24, t1/t5=0.12 (真值 0.2439, 0.1183)

| 位置 | .tex conc | Match? | .tex t1/t5 | Match? |
|---|---|---|---|---|
| analysis.tex:26 | 0.24 | OK | 0.12 | OK |
| analysis.tex:49 (table) | 0.24 | OK | 0.12 | OK |
| analysis.tex:65 | 0.24 | OK | — | — |

**Pythia: 全部匹配**

---

### 汇总

| Model | .tex conc | 真值 conc | conc Match? | .tex t1/t5 | 真值 t1/t5 | t1/t5 Match? |
|---|---|---|---|---|---|---|
| Qwen2.5-7B | 0.61 | 0.6104 | OK | 0.57 | 0.5670 | OK |
| Qwen2.5-14B | 0.33 | 0.3312 | OK | 0.57 | 0.5693 | OK |
| Llama-3.1-8B | 0.34 | 0.3387 | OK | 0.71 | 0.7139 | OK |
| Yi-1.5-9B | 0.71 | 0.7139 | OK | 0.90 | 0.9012 | OK |
| Mistral-7B-v0.3 | 0.22 | 0.2200 | OK | 0.18 | 0.1820 | OK |
| Gemma-2-9B | 0.23 | 0.2299 | OK | 0.18 | 0.1757 | OK (borderline) |
| Pythia-1.4B | 0.24 | 0.2439 | OK | 0.12 | 0.1183 | OK |

**结论：所有 7 个模型的 concentration 和 t1/t5 值在 .tex 中均与 hires bf16 真值匹配（两位小数四舍五入精度）。未发现 lowres 残留。**

关于你提到的 "Llama concentration 0.34 是 lowres，正确 hires=0.57"——根据你提供的真值表，Llama hires top5%conc 就是 **0.3387**（≈0.34），0.57 是 Qwen 的 t1/t5。Llama 的 .tex 值 0.34 是正确的。如果你手头有不同的 Llama hires 真值，请核实 shape_metrics.json 原始数据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 61854,
  "duration_api_ms": 63005,
  "num_turns": 6,
  "stop_reason": "end_turn",
  "session_id": "f9734027-5e0c-4d70-9553-47857b654bd4",
  "total_cost_usd": 0.28696325,
  "usage": {
    "input_tokens": 6,
    "cache_creation_input_tokens": 21663,
    "cache_read_input_tokens": 100543,
    "output_tokens": 3961,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 21663,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 3002,
        "cache_read_input_tokens": 32779,
        "cache_creation_input_tokens": 725,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 725
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2113,
      "outputTokens": 26,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0022429999999999998,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 6,
      "outputTokens": 3961,
      "cacheReadInputTokens": 100543,
      "cacheCreationInputTokens": 21663,
      "webSearchRequests": 0,
      "costUSD": 0.28472025,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "991c3fb7-d1a2-4466-a4ca-ebc85885fa03"
}
```

</details>

---
