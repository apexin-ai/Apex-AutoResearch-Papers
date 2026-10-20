# paper tex consistency fixes

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 55
- **Recorded user turns:** 0
- **Tool calls:** 20
- **Original source:** `logs/workers/worker_paper_tex_consistency_fixes_20260516T224936.log`
- **Structured JSON:** [`39612d45b352ad0020ca.json`](../../sessions/39/39612d45b352ad0020ca.json)

## Before a recorded user message

55 recorded events

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
  "session_id": "7c8d5505-1cf3-4db2-81a6-3ef2a3c9c146",
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
  "uuid": "5708b103-05cf-46f2-a4ac-c0f5d95d712a",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/memory/"
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
    "resetsAt": 1778988000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "c10d0a00-3fdc-42c4-96e7-98330830d731",
  "session_id": "7c8d5505-1cf3-4db2-81a6-3ef2a3c9c146"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me read the relevant tex files to confirm the issues and make the fixes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7c8d5505-1cf3-4db2-81a6-3ef2a3c9c146",
  "uuid": "e1771243-f09d-4174-b515-b5f3f8619493",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FGkFGeyG6Kpqho9BBwGiuo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12740,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12740
      },
      "output_tokens": 31,
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

<details open><summary>🔧 Tool call — Read · `toolu_01FYJ1Mi9wet5aFdGzMyideP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex",
  "offset": 80,
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
  "session_id": "7c8d5505-1cf3-4db2-81a6-3ef2a3c9c146",
  "uuid": "aa8bf28a-b39a-4904-a4c5-cef32fbcbc48",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FGkFGeyG6Kpqho9BBwGiuo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12740,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12740
      },
      "output_tokens": 31,
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

_source line 6 · 2026-05-16T22:49:50.544Z_

<details><summary>↩ Tool result · `toolu_01FYJ1Mi9wet5aFdGzMyideP`</summary>

```text
80	\toprule
81	Model & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
82	\midrule
83	DeepSeek-R1-Distill-Qwen-7B ($n{=}496$) & 0.39 & 1.21 & 3.99 & 8.48 \\
84	Qwen2.5-7B-Instruct ($n{=}475$)         & 0.07 & 0.31 & 1.07 & 3.16 \\
85	\bottomrule
86	\end{tabular}
87	\end{table}
88	
89	\begin{figure}[t]
90	\centering
91	\includegraphics[width=\columnwidth]{fig5_crossmodel.pdf}
92	\caption{Cross-training-paradigm comparison of the median severity difference under importance-based eviction ($n{=}496$/$475$). Both DeepSeek (solid) and Qwen (dashed) exhibit monotonically increasing $\Delta$ with sparsity; Qwen's magnitude is approximately one-quarter to one-sixth of DeepSeek's.}
93	\label{fig:cross-model}
94	\end{figure}
95	
96	\paragraph{Per-problem concordance.}
97	The per-problem concordance across models is not significant (mean $\rho = -0.107$, $p = 0.926$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking.
98	
99	\paragraph{Random eviction control.}
100	As a control, random eviction on Qwen mirrors DeepSeek: non-significant at $s \leq 0.20$ ($\Delta$: $-0.01$, $0.02$; CIs span zero) but significant at $s \geq 0.25$ ($\Delta{=}0.39$, $p_{\text{Bonf}} < 10^{-10}$; $\Delta{=}0.91$, $p_{\text{Bonf}} < 10^{-13}$). Where significant, the random phase gradient is $2.7$--$3.5{\times}$ weaker than importance-based ($0.39$ vs.\ $1.07$ at $s{=}0.25$; $0.91$ vs.\ $3.16$ at $s{=}0.30$), supporting strategy-specific amplification.
101	
102	
103	\section{Permutation Test Details}
104	\label{app:permutation-details}
105	
106	For each problem $i$ and sparsity level $s$, we compute the compound severity difference $\Delta_i^{(\text{strat})} = \mathrm{II}_{\textit{low},i} - \mathrm{II}_{\textit{high},i}$ under each eviction strategy. The test statistic is the median of the paired difference $\widetilde{\Delta} = \text{median}_i\!\bigl(\Delta_i^{(\text{imp})} - \Delta_i^{(\text{rand})}\bigr)$, measuring whether importance-based eviction produces systematically larger phase-dependent severity than random eviction. We permute strategy labels $10{,}000$ times to construct the null distribution and apply Bonferroni correction for 4 sparsity-level comparisons.
107	
108	Per-problem distributions of the paired severity difference $\Delta_i = \mathrm{II}_{\textit{low},i} - \mathrm{II}_{\textit{high},i}$ under importance-based eviction are right-skewed at all sparsity levels, with mean/median ratios ranging from $1.2{\times}$ ($s{=}0.15$) to $1.6{\times}$ ($s{=}0.30$) for DeepSeek and $1.1{\times}$ to $1.4{\times}$ for Qwen.
109	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7c8d5505-1cf3-4db2-81a6-3ef2a3c9c146",
  "uuid": "1f4ade8e-d5ad-412a-b278-e06e1ea1d558",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex",
      "content": "\\toprule\nModel & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\\\\n\\midrule\nDeepSeek-R1-Distill-Qwen-7B ($n{=}496$) & 0.39 & 1.21 & 3.99 & 8.48 \\\\\nQwen2.5-7B-Instruct ($n{=}475$)         & 0.07 & 0.31 & 1.07 & 3.16 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig5_crossmodel.pdf}\n\\caption{Cross-training-paradigm comparison of the median severity difference under importance-based eviction ($n{=}496$/$475$). Both DeepSeek (solid) and Qwen (dashed) exhibit monotonically increasing $\\Delta$ with sparsity; Qwen's magnitude is approximately one-quarter to one-sixth of DeepSeek's.}\n\\label{fig:cross-model}\n\\end{figure}\n\n\\paragraph{Per-problem concordance.}\nThe per-problem concordance across models is not significant (mean $\\rho = -0.107$, $p = 0.926$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking.\n\n\\paragraph{Random eviction control.}\nAs a control, random eviction on Qwen mirrors DeepSeek: non-significant at $s \\leq 0.20$ ($\\Delta$: $-0.01$, $0.02$; CIs span zero) but significant at $s \\geq 0.25$ ($\\Delta{=}0.39$, $p_{\\text{Bonf}} < 10^{-10}$; $\\Delta{=}0.91$, $p_{\\text{Bonf}} < 10^{-13}$). Where significant, the random phase gradient is $2.7$--$3.5{\\times}$ weaker than importance-based ($0.39$ vs.\\ $1.07$ at $s{=}0.25$; $0.91$ vs.\\ $3.16$ at $s{=}0.30$), supporting strategy-specific amplification.\n\n\n\\section{Permutation Test Details}\n\\label{app:permutation-details}\n\nFor each problem $i$ and sparsity level $s$, we compute the compound severity difference $\\Delta_i^{(\\text{strat})} = \\mathrm{II}_{\\textit{low},i} - \\mathrm{II}_{\\textit{high},i}$ under each eviction strategy. The test statistic is the median of the paired difference $\\widetilde{\\Delta} = \\text{median}_i\\!\\bigl(\\Delta_i^{(\\text{imp})} - \\Delta_i^{(\\text{rand})}\\bigr)$, measuring whether importance-based eviction produces systematically larger phase-dependent severity than random eviction. We permute strategy labels $10{,}000$ times to construct the null distribution and apply Bonferroni correction for 4 sparsity-level comparisons.\n\nPer-problem distributions of the paired severity difference $\\Delta_i = \\mathrm{II}_{\\textit{low},i} - \\mathrm{II}_{\\textit{high},i}$ under importance-based eviction are right-skewed at all sparsity levels, with mean/median ratios ranging from $1.2{\\times}$ ($s{=}0.15$) to $1.6{\\times}$ ($s{=}0.30$) for DeepSeek and $1.1{\\times}$ to $1.4{\\times}$ for Qwen.\n",
      "numLines": 30,
      "startLine": 80,
      "totalLines": 246
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_01X8YwGfJigA9GbcGBBQBhpC`</summary>

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
  "session_id": "7c8d5505-1cf3-4db2-81a6-3ef2a3c9c146",
  "uuid": "bc3a7c94-78d0-47a9-bed2-054a136ab74e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FGkFGeyG6Kpqho9BBwGiuo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12740,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12740
      },
      "output_tokens": 31,
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

_source line 8 · 2026-05-16T22:49:51.021Z_

<details><summary>↩ Tool result · `toolu_01X8YwGfJigA9GbcGBBQBhpC`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We showed that compound sparsity severity is not phase-invariant but exhibits an emergent phase-strategy interaction. Under importance-based eviction, the paired median difference $\Delta$ increases from $0.39$ to $8.48$ (DeepSeek, $n{=}500$; Spearman $\rho{=}1.0$) and $0.07$ to $3.16$ (Qwen, $n{=}475$), all $p < 10^{-13}$. Random eviction is $2.7$--$17{\times}$ weaker where both strategies are significant ($s \geq 0.25$; DeepSeek $15$--$17{\times}$, Qwen $2.7$--$3.5{\times}$). The importance phase gradient replicates on LlamaForCausalLM ($d_z{=}0.81$--$1.15$, $n{=}250$, all $p < 10^{-29}$), supporting architecture-generality of phase modulation, while strategy specificity is architecture-dependent ($2.0$--$2.6{\times}$ on LLaMA vs.\ $15$--$17{\times}$ on DeepSeek). A model-dependent crossover on DeepSeek demonstrates that no single strategy dominates uniformly. Per-phase Gini analysis reveals importance discrimination collapse as a correlational diagnostic: despite near-identical aggregate Gini drops, severity diverges by $2.7$--$17{\times}$, implicating the structural specificity of importance-based pruning.
5	Beyond the empirical findings, the phase-gated analysis framework itself---decomposing compound severity by reasoning phase and eviction strategy---transforms a scalar interaction metric into a structured diagnostic that reveals where compound sparsity fails and why. This framework provides practitioners with a principled basis for phase-aware sparsity allocation: applying aggressive compression during high-sparsity (structured computation) phases while preserving budget during low-sparsity (exploratory reasoning) phases. Future work could explore generalization to other reasoning domains, causal validation of importance discrimination collapse, and systematic characterization of asymmetric compound interactions.
6	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7c8d5505-1cf3-4db2-81a6-3ef2a3c9c146",
  "uuid": "e85c75e3-04bf-4505-a608-445e11baeb4b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex",
      "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe showed that compound sparsity severity is not phase-invariant but exhibits an emergent phase-strategy interaction. Under importance-based eviction, the paired median difference $\\Delta$ increases from $0.39$ to $8.48$ (DeepSeek, $n{=}500$; Spearman $\\rho{=}1.0$) and $0.07$ to $3.16$ (Qwen, $n{=}475$), all $p < 10^{-13}$. Random eviction is $2.7$--$17{\\times}$ weaker where both strategies are significant ($s \\geq 0.25$; DeepSeek $15$--$17{\\times}$, Qwen $2.7$--$3.5{\\times}$). The importance phase gradient replicates on LlamaForCausalLM ($d_z{=}0.81$--$1.15$, $n{=}250$, all $p < 10^{-29}$), supporting architecture-generality of phase modulation, while strategy specificity is architecture-dependent ($2.0$--$2.6{\\times}$ on LLaMA vs.\\ $15$--$17{\\times}$ on DeepSeek). A model-dependent crossover on DeepSeek demonstrates that no single strategy dominates uniformly. Per-phase Gini analysis reveals importance discrimination collapse as a correlational diagnostic: despite near-identical aggregate Gini drops, severity diverges by $2.7$--$17{\\times}$, implicating the structural specificity of importance-based pruning.\nBeyond the empirical findings, the phase-gated analysis framework itself---decomposing compound severity by reasoning phase and eviction strategy---transforms a scalar interaction metric into a structured diagnostic that reveals where compound sparsity fails and why. This framework provides practitioners with a principled basis for phase-aware sparsity allocation: applying aggressive compression during high-sparsity (structured computation) phases while preserving budget during low-sparsity (exploratory reasoning) phases. Future work could explore generalization to other reasoning domains, causal validation of importance discrimination collapse, and systematic characterization of asymmetric compound interactions.\n",
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

_source line 9_

<details open><summary>🔧 Tool call — Read · `toolu_01X2qShFCCgM3PeYNBnW8D2L`</summary>

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
  "session_id": "7c8d5505-1cf3-4db2-81a6-3ef2a3c9c146",
  "uuid": "81ffe4f4-108d-49ea-97fb-83f8e3921935",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FGkFGeyG6Kpqho9BBwGiuo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12740,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12740
      },
      "output_tokens": 31,
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

_source line 10 · 2026-05-16T22:49:51.518Z_

<details><summary>↩ Tool result · `toolu_01X2qShFCCgM3PeYNBnW8D2L`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Implications for deployment.}
5	A uniform compression budget implicitly accepts order-of-magnitude severity penalties during low-sparsity reasoning phases. Pilot evaluation ($n{=}30$, $s{=}0.25$; Appendix~\ref{app:pilot-mitigation}) achieved 18\% oracle recovery (95\% CI: $[-39\%, 45.8\%]$), falling below the pre-registered 30\% gate; the CI spans zero, indicating no statistically distinguishable improvement. Effective phase-aware allocation likely requires finer phase boundary estimation than current proxies provide. Additional mechanisms (e.g., strategy switching, adaptive thresholding) warrant investigation. We hypothesize that phase-modulated severity may extend to alternative attention-mass-based scoring methods (H$_2$O \cite{h2o-neurips2023}, SnapKV \cite{snapkv-neurips2024}, PyramidKV \cite{pyramidkv-colm2025}), which remains an open question for future work. Extended discussion in Appendix~\ref{app:extended-discussion}.
6	
7	\paragraph{Reasoning depth scaling.}
8	Strategy specificity is not a fixed property but scales with reasoning chain depth: MATH-500 ($15$--$17{\times}$) $>$ GSM8K (${\sim}3{\times}$), with within-MATH-500 correlational support (Spearman $\rho > 0$, $p < 0.02$ between trace length and specificity). This scaling is consistent with the discrimination collapse mechanism: longer low-sparsity phases provide more tokens over which pruning-degraded importance scores accumulate errors, amplifying the gap between importance-based and random eviction. The implication is practical: as models generate longer reasoning chains (a trend driven by test-time compute scaling~\cite{snell-2024-scaling-test-time}), the penalty for naive compound compression grows superlinearly.
9	
10	\paragraph{Diagnostic framework value.}
11	While we do not propose a new compression method, the phase-gated analysis framework has direct engineering utility: (1)~the Interaction Index can serve as a per-phase evaluation metric for assessing the phase robustness of any new compound compression scheme; (2)~the dose-response curves (Figure~\ref{fig:hero}) provide target operating points for phase-aware controllers---e.g., maintaining $s \leq 0.20$ during low-sparsity phases to keep $\Delta < 1.5$; (3)~the strategy specificity finding carries a concrete engineering implication: importance-based eviction under compound sparsity requires phase-aware protection that random eviction does not, because the interaction is structurally coupled to the scoring mechanism rather than to compression magnitude alone.
12	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7c8d5505-1cf3-4db2-81a6-3ef2a3c9c146",
  "uuid": "64618587-0092-4d91-814c-8f418ee6efe0",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex",
      "content": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Implications for deployment.}\nA uniform compression budget implicitly accepts order-of-magnitude severity penalties during low-sparsity reasoning phases. Pilot evaluation ($n{=}30$, $s{=}0.25$; Appendix~\\ref{app:pilot-mitigation}) achieved 18\\% oracle recovery (95\\% CI: $[-39\\%, 45.8\\%]$), falling below the pre-registered 30\\% gate; the CI spans zero, indicating no statistically distinguishable improvement. Effective phase-aware allocation likely requires finer phase boundary estimation than current proxies provide. Additional mechanisms (e.g., strategy switching, adaptive thresholding) warrant investigation. We hypothesize that phase-modulated severity may extend to alternative attention-mass-based scoring methods (H$_2$O \\cite{h2o-neurips2023}, SnapKV \\cite{snapkv-neurips2024}, PyramidKV \\cite{pyramidkv-colm2025}), which remains an open question for future work. Extended discussion in Appendix~\\ref{app:extended-discussion}.\n\n\\paragraph{Reasoning depth scaling.}\nStrategy specificity is not a fixed property but scales with reasoning chain depth: MATH-500 ($15$--$17{\\times}$) $>$ GSM8K (${\\sim}3{\\times}$), with within-MATH-500 correlational support (Spearman $\\rho > 0$, $p < 0.02$ between trace length and specificity). This scaling is consistent with the discrimination collapse mechanism: longer low-sparsity phases provide more tokens over which pruning-degraded importance scores accumulate errors, amplifying the gap between importance-based and random eviction. The implication is practical: as models generate longer reasoning chains (a trend driven by test-time compute scaling~\\cite{snell-2024-scaling-test-time}), the penalty for naive compound compression grows superlinearly.\n\n\\paragraph{Diagnostic framework value.}\nWhile we do not propose a new compression method, the phase-gated analysis framework has direct engineering utility: (1)~the Interaction Index can serve as a per-phase evaluation metric for assessing the phase robustness of any new compound compression scheme; (2)~the dose-response curves (Figure~\\ref{fig:hero}) provide target operating points for phase-aware controllers---e.g., maintaining $s \\leq 0.20$ during low-sparsity phases to keep $\\Delta < 1.5$; (3)~the strategy specificity finding carries a concrete engineering implication: importance-based eviction under compound sparsity requires phase-aware protection that random eviction does not, because the interaction is structurally coupled to the scoring mechanism rather than to compression magnitude alone.\n",
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

_source line 11_

Now I need to find the "2.7-20×" reference near line 88 of appendix_moved.tex. Let me look earlier in the file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7c8d5505-1cf3-4db2-81a6-3ef2a3c9c146",
  "uuid": "d645e86e-7da4-42c8-bb32-73c625dc7705",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016big5AyEDKt6NnNt9A3fJ1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2644,
      "cache_read_input_tokens": 24581,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2644
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

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_01CgWFWi3R15tGRcAr6CkXJj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex",
  "offset": 60,
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
  "session_id": "7c8d5505-1cf3-4db2-81a6-3ef2a3c9c146",
  "uuid": "cd430584-ff73-4b43-b8e0-66a8e4ca477d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016big5AyEDKt6NnNt9A3fJ1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2644,
      "cache_read_input_tokens": 24581,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2644
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

_source line 13 · 2026-05-16T22:49:58.896Z_

<details><summary>↩ Tool result · `toolu_01CgWFWi3R15tGRcAr6CkXJj`</summary>

```text
60	\label{tab:qwen-effective-n}
61	\begin{tabular}{@{}lcccc@{}}
62	\toprule
63	Phase & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
64	\midrule
65	High & 475 & 475 & 475 & 475 \\
66	Mid  & 274 & 274 & 274 & 274 \\
67	Low  & 475 & 475 & 475 & 475 \\
68	\bottomrule
69	\end{tabular}
70	\end{table}
71	
72	Table~\ref{tab:cross-model} reports the cross-training-paradigm comparison. Qwen reproduces the monotonic severity gradient at ${\sim}1/5$ of DeepSeek's magnitude. Figure~\ref{fig:cross-model} visualizes this comparison.
73	
74	\begin{table}[t]
75	\centering
76	\small
77	\caption{Cross-training-paradigm comparison of median compound severity difference ($\Delta$) under importance-based eviction.}
78	\label{tab:cross-model}
79	\begin{tabular}{@{}lcccc@{}}
80	\toprule
81	Model & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
82	\midrule
83	DeepSeek-R1-Distill-Qwen-7B ($n{=}496$) & 0.39 & 1.21 & 3.99 & 8.48 \\
84	Qwen2.5-7B-Instruct ($n{=}475$)         & 0.07 & 0.31 & 1.07 & 3.16 \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7c8d5505-1cf3-4db2-81a6-3ef2a3c9c146",
  "uuid": "ead4a754-dda0-49dc-bec4-584c51da1e85",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex",
      "content": "\\label{tab:qwen-effective-n}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nPhase & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\\\\n\\midrule\nHigh & 475 & 475 & 475 & 475 \\\\\nMid  & 274 & 274 & 274 & 274 \\\\\nLow  & 475 & 475 & 475 & 475 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:cross-model} reports the cross-training-paradigm comparison. Qwen reproduces the monotonic severity gradient at ${\\sim}1/5$ of DeepSeek's magnitude. Figure~\\ref{fig:cross-model} visualizes this comparison.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-training-paradigm comparison of median compound severity difference ($\\Delta$) under importance-based eviction.}\n\\label{tab:cross-model}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nModel & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\\\\n\\midrule\nDeepSeek-R1-Distill-Qwen-7B ($n{=}496$) & 0.39 & 1.21 & 3.99 & 8.48 \\\\\nQwen2.5-7B-Instruct ($n{=}475$)         & 0.07 & 0.31 & 1.07 & 3.16 \\\\",
      "numLines": 25,
      "startLine": 60,
      "totalLines": 246
    }
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Grep · `toolu_01HPJEuKpXtxB9eftWR8r8hU`</summary>

```json
{
  "pattern": "2\\.7.*20",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7c8d5505-1cf3-4db2-81a6-3ef2a3c9c146",
  "uuid": "e312bc47-1def-465d-81a9-da0e45fe6e6a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016big5AyEDKt6NnNt9A3fJ1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2644,
      "cache_read_input_tokens": 24581,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2644
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

_source line 15 · 2026-05-16T22:49:59.743Z_

<details><summary>↩ Tool result · `toolu_01HPJEuKpXtxB9eftWR8r8hU`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7c8d5505-1cf3-4db2-81a6-3ef2a3c9c146",
  "uuid": "8e0436e4-340d-4686-9548-027b7f341dd7",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  }
}
```

</details>

---

### Assistant

_source line 16_

The "20×" might not be in appendix_moved.tex. Let me search more broadly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7c8d5505-1cf3-4db2-81a6-3ef2a3c9c146",
  "uuid": "05da0433-aaa8-4a99-9020-0e6b381fd10a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PvQijrb8wuiiMnUFeo4j4E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 850,
      "cache_read_input_tokens": 27225,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 850
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

_source line 17_

<details open><summary>🔧 Tool call — Grep · `toolu_018cBWzfZ4x4GkK7ZKdWaHXk`</summary>

```json
{
  "pattern": "20\\{?\\\\times\\}?",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7c8d5505-1cf3-4db2-81a6-3ef2a3c9c146",
  "uuid": "64a7d045-8b81-4fe2-a43b-469ccaea86a1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PvQijrb8wuiiMnUFeo4j4E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 850,
      "cache_read_input_tokens": 27225,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 850
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

_source line 18 · 2026-05-16T22:50:05.247Z_

<details><summary>↩ Tool result · `toolu_018cBWzfZ4x4GkK7ZKdWaHXk`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7c8d5505-1cf3-4db2-81a6-3ef2a3c9c146",
  "uuid": "924bb325-b076-486e-aa6d-4867fab3e511",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Grep · `toolu_01C3eH4gYpxo5mYGgAmKceUZ`</summary>

```json
{
  "pattern": "2\\.7.*weaker",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7c8d5505-1cf3-4db2-81a6-3ef2a3c9c146",
  "uuid": "de049bd2-7335-47c8-8fa0-1ae3ee1e5ad4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PvQijrb8wuiiMnUFeo4j4E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 850,
      "cache_read_input_tokens": 27225,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 850
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

_source line 20 · 2026-05-16T22:50:06.085Z_

<details><summary>↩ Tool result · `toolu_01C3eH4gYpxo5mYGgAmKceUZ`</summary>

```text
artifacts/_project/paper/results.tex:88:[Omitted long matching line]
artifacts/_project/paper/conclusion.tex:4:[Omitted long matching line]
artifacts/_project/paper/appendix_moved.tex:100:As a control, random eviction on Qwen mirrors DeepSeek: non-significant at $s \leq 0.20$ ($\Delta$: $-0.01$, $0.02$; CIs span zero) but significant at $s \geq 0.25$ ($\Delta{=}0.39$, $p_{\text{Bonf}} < 10^{-10}$; $\Delta{=}0.91$, $p_{\text{Bonf}} < 10^{-13}$). Where significant, the random phase gradient is $2.7$--$3.5{\times}$ weaker than importance-based ($0.39$ vs.\ $1.07$ at $s{=}0.25$; $0.91$ vs.\ $3.16$ at $s{=}0.30$), supporting strategy-specific amplification.
artifacts/_project/paper/appendix_disc_analysis.tex:14:[Omitted long matching line]
artifacts/_project/paper/appendix_disc_analysis.tex:53:These effects are genuine but $2.7$--$20{\times}$ weaker than importance-based eviction at the same sparsity levels, consistent with a weak phase gradient that is detectable at sufficient sample size but not the primary driver of compound severity.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7c8d5505-1cf3-4db2-81a6-3ef2a3c9c146",
  "uuid": "a978c687-5d0d-4930-b7c2-1412d9ea6b02",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "artifacts/_project/paper/results.tex:88:[Omitted long matching line]\nartifacts/_project/paper/conclusion.tex:4:[Omitted long matching line]\nartifacts/_project/paper/appendix_moved.tex:100:As a control, random eviction on Qwen mirrors DeepSeek: non-significant at $s \\leq 0.20$ ($\\Delta$: $-0.01$, $0.02$; CIs span zero) but significant at $s \\geq 0.25$ ($\\Delta{=}0.39$, $p_{\\text{Bonf}} < 10^{-10}$; $\\Delta{=}0.91$, $p_{\\text{Bonf}} < 10^{-13}$). Where significant, the random phase gradient is $2.7$--$3.5{\\times}$ weaker than importance-based ($0.39$ vs.\\ $1.07$ at $s{=}0.25$; $0.91$ vs.\\ $3.16$ at $s{=}0.30$), supporting strategy-specific amplification.\nartifacts/_project/paper/appendix_disc_analysis.tex:14:[Omitted long matching line]\nartifacts/_project/paper/appendix_disc_analysis.tex:53:These effects are genuine but $2.7$--$20{\\times}$ weaker than importance-based eviction at the same sparsity levels, consistent with a weak phase gradient that is detectable at sufficient sample size but not the primary driver of compound severity.",
    "numLines": 5
  }
}
```

</details>

---

### Assistant

_source line 21_

Found it — the issue is in `appendix_disc_analysis.tex` line 53, not `appendix_moved.tex` line 88. Let me also check the results.tex line 88 for context on the GSM8K data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7c8d5505-1cf3-4db2-81a6-3ef2a3c9c146",
  "uuid": "2ad828b1-7c39-4c5e-9b3e-ee5d8cd5a516",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BmBstPFNSbniszxBesarMz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 701,
      "cache_read_input_tokens": 28075,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 701
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

_source line 22_

<details open><summary>🔧 Tool call — Read · `toolu_012M68FvY5UosFjqDeNUwKyd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex",
  "offset": 45,
  "limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7c8d5505-1cf3-4db2-81a6-3ef2a3c9c146",
  "uuid": "8496ddfb-8016-4d8b-9eeb-dafafea8108d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BmBstPFNSbniszxBesarMz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 701,
      "cache_read_input_tokens": 28075,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 701
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

_source line 23 · 2026-05-16T22:50:14.448Z_

<details><summary>↩ Tool result · `toolu_012M68FvY5UosFjqDeNUwKyd`</summary>

```text
45	
46	
47	\paragraph{Statistical scope.}
48	Bootstrap confidence intervals use $B{=}10{,}000$ resamples (seed$=$42). The primary analysis uses $n{=}496$ paired problems for DeepSeek (4 excluded) and $n{=}475$ for Qwen (25 excluded); the permutation test (Table~\ref{tab:permutation}) uses $n{=}49$ from an initial profiling subset.
49	The severity difference distribution is right-skewed (mean/median ratios up to $43{:}1$), motivating our use of medians and nonparametric tests rather than parametric alternatives.
50	All four profiling-subset permutation tests reject $H_0$ after Bonferroni correction ($p_{\text{Bonf}} < 0.005$; Table~\ref{tab:permutation}), with CI lower bounds increasing from $0.19$ to $6.70$---supporting the effect direction at every sparsity level. At $n{=}496$, Wilcoxon signed-rank tests support all conditions with $p_{\text{Bonf}} < 10^{-13}$ (Table~\ref{tab:cohens-d}). The permutation CIs at higher sparsity are wider (e.g., $[6.70,\; 16.29]$ at $s{=}0.30$), reflecting genuine variance in per-problem severity amplification.
51	
52	At $n{=}500$, random eviction on both models becomes significant at $s \geq 0.25$ (Qwen: $\Delta{=}0.39$, $p_{\text{Bonf}} < 10^{-10}$ at $s{=}0.25$; $\Delta{=}0.91$, $p_{\text{Bonf}} < 10^{-13}$ at $s{=}0.30$; bootstrap CIs exclude zero).
53	These effects are genuine but $2.7$--$20{\times}$ weaker than importance-based eviction at the same sparsity levels, consistent with a weak phase gradient that is detectable at sufficient sample size but not the primary driver of compound severity.
54	
55	\paragraph{Sparsity range.}
56	Our primary analysis spans $s \in \{0.15, 0.20, 0.25, 0.30\}$; pilot data at $s{=}0.10$ and $s{=}0.35$ exist (6 total sparsity levels) but are not included in the main analysis due to limited sample size at these boundary conditions. Monotonicity is established at the tested sparsity levels (JT test $p \ll 10^{-10}$); the functional form of $G(s)$ between and beyond these levels is not characterized.
57	More extreme sparsity ($s > 0.50$) may exhibit qualitatively different interaction dynamics---the sub-exponential growth pattern suggests the severity gradient may plateau, but this remains unverified.
58	
59	
60	\paragraph{No throughput evaluation.}
61	We do not report inference throughput or latency, which are necessary for deployment analysis but orthogonal to our severity characterization.
62	
63	
64	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7c8d5505-1cf3-4db2-81a6-3ef2a3c9c146",
  "uuid": "5dcd91a3-3025-4649-b23a-90f883269caa",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex",
      "content": "\n\n\\paragraph{Statistical scope.}\nBootstrap confidence intervals use $B{=}10{,}000$ resamples (seed$=$42). The primary analysis uses $n{=}496$ paired problems for DeepSeek (4 excluded) and $n{=}475$ for Qwen (25 excluded); the permutation test (Table~\\ref{tab:permutation}) uses $n{=}49$ from an initial profiling subset.\nThe severity difference distribution is right-skewed (mean/median ratios up to $43{:}1$), motivating our use of medians and nonparametric tests rather than parametric alternatives.\nAll four profiling-subset permutation tests reject $H_0$ after Bonferroni correction ($p_{\\text{Bonf}} < 0.005$; Table~\\ref{tab:permutation}), with CI lower bounds increasing from $0.19$ to $6.70$---supporting the effect direction at every sparsity level. At $n{=}496$, Wilcoxon signed-rank tests support all conditions with $p_{\\text{Bonf}} < 10^{-13}$ (Table~\\ref{tab:cohens-d}). The permutation CIs at higher sparsity are wider (e.g., $[6.70,\\; 16.29]$ at $s{=}0.30$), reflecting genuine variance in per-problem severity amplification.\n\nAt $n{=}500$, random eviction on both models becomes significant at $s \\geq 0.25$ (Qwen: $\\Delta{=}0.39$, $p_{\\text{Bonf}} < 10^{-10}$ at $s{=}0.25$; $\\Delta{=}0.91$, $p_{\\text{Bonf}} < 10^{-13}$ at $s{=}0.30$; bootstrap CIs exclude zero).\nThese effects are genuine but $2.7$--$20{\\times}$ weaker than importance-based eviction at the same sparsity levels, consistent with a weak phase gradient that is detectable at sufficient sample size but not the primary driver of compound severity.\n\n\\paragraph{Sparsity range.}\nOur primary analysis spans $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$; pilot data at $s{=}0.10$ and $s{=}0.35$ exist (6 total sparsity levels) but are not included in the main analysis due to limited sample size at these boundary conditions. Monotonicity is established at the tested sparsity levels (JT test $p \\ll 10^{-10}$); the functional form of $G(s)$ between and beyond these levels is not characterized.\nMore extreme sparsity ($s > 0.50$) may exhibit qualitatively different interaction dynamics---the sub-exponential growth pattern suggests the severity gradient may plateau, but this remains unverified.\n\n\n\\paragraph{No throughput evaluation.}\nWe do not report inference throughput or latency, which are necessary for deployment analysis but orthogonal to our severity characterization.\n\n\n",
      "numLines": 20,
      "startLine": 45,
      "totalLines": 164
    }
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Read · `toolu_018m5JPKQ3jgEB6VM6s6J6WE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex",
  "offset": 80,
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
  "session_id": "7c8d5505-1cf3-4db2-81a6-3ef2a3c9c146",
  "uuid": "5ef93b30-7ee6-4e23-b160-7a1dc2664204",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BmBstPFNSbniszxBesarMz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 701,
      "cache_read_input_tokens": 28075,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 701
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

_source line 25 · 2026-05-16T22:50:15.133Z_

<details><summary>↩ Tool result · `toolu_018m5JPKQ3jgEB6VM6s6J6WE`</summary>

```text
80	\label{sec:crossover}
81	
82	The phase-strategy crossover is model-dependent. For DeepSeek ($n{=}496$), a strategy ranking reversal emerges at all four sparsity levels: at $s{=}0.25$, importance-based eviction yields \emph{lower} II than random in the high-sparsity phase ($0.021$ vs.\ $1.113$) but \emph{higher} II in the low-sparsity phase ($3.971$ vs.\ $1.514$---a $2.6{\times}$ reversal; both $p < 10^{-4}$), with reversal magnitude ranging from $2.2{\times}$ to $4.0{\times}$ across $s \in \{0.15, 0.20, 0.25, 0.30\}$. Qwen does \emph{not} exhibit this crossover: importance-based eviction produces lower II than random in both phases (e.g., at $s{=}0.25$: high $0.004$ vs.\ $1.108$; low $1.053$ vs.\ $1.769$). This divergence suggests the crossover arises from model-specific attention head specialization patterns rather than a universal compound-sparsity property. Full crossover analysis appears in Appendix~\ref{app:crossover-details}.
83	
84	\subsection{Replication Across Training Paradigms}
85	\label{sec:cross-model}
86	
87	DeepSeek-R1-Distill-Qwen-7B (distillation-trained) and Qwen2.5-7B-Instruct (instruction-tuned) share the Qwen2 backbone but differ in training objective, providing a within-architecture-family comparison across training paradigms.
88	Qwen2.5-7B-Instruct ($n_{\text{eff}}{=}475$) reproduces the monotonic severity gradient: $\Delta$ increases from $0.07$ at $s{=}0.15$ to $3.16$ at $s{=}0.30$ (all Bonferroni-corrected $p < 10^{-14}$), paralleling DeepSeek at approximately one-quarter to one-sixth the magnitude. Both models yield strictly increasing median $\Delta$ trajectories (Jonckheere-Terpstra $z \geq 6.2$, $p < 10^{-9}$; see \S\ref{par:stats}). Random eviction on Qwen mirrors DeepSeek: non-significant at $s \leq 0.20$, becoming significant at $s \geq 0.25$ ($\Delta{=}0.39$--$0.91$; $p_{\text{Bonf}} < 10^{-10}$) but $2.7$--$20{\times}$ weaker than importance-based. A caveat: 45.2\% of Qwen problems yield null mid-phase segments due to low temporal autocorrelation ($r{=}0.718$ vs.\ $0.894$); this does not affect $\Delta$ (Appendix~\ref{app:qwen-null-rate}). Full tables in Appendix~\ref{app:cross-model-details}.
89	
90	\subsection{Cross-Architecture Validation}
91	\label{sec:cross-arch}
92	
93	Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, $n{=}250$, MATH-500) supports the generality of phase-modulated compound interaction beyond the Qwen2 architecture family. Under importance-based eviction, the paired median difference $\Delta$ rises monotonically from $0.050$ ($s{=}0.15$) to $0.695$ ($s{=}0.30$), with large effect sizes throughout ($d_z{=}0.81$--$1.15$; all $p < 10^{-29}$; Table~\ref{tab:llama-cross-arch}).
94	
95	A key architectural difference emerges in strategy specificity. On LLaMA, random eviction also exhibits significant phase gradients ($\Delta{=}0.025$--$0.271$; $d_z{=}0.41$--$0.46$; all $p < 10^{-12}$), unlike DeepSeek and Qwen where random is non-significant at $s \leq 0.20$. The importance/random $\Delta$ ratio is $2.0$--$2.6{\times}$ on LLaMA, substantially weaker than the $15$--$17{\times}$ observed on DeepSeek. Dose-response monotonicity holds for both strategies (all conditions monotonic). This indicates that the phase gradient itself is architecture-general, while the degree of strategy specificity is architecture-dependent, likely reflecting differences between GQA (LLaMA, 32 heads with 8 KV groups) and MHA (Qwen2, 28 heads) in how head pruning differentially disrupts importance scoring.
96	
97	Absolute interaction magnitudes are approximately $7$--$12{\times}$ smaller than Qwen2-family models at matched sparsity, consistent with architecture-specific attention head specialization patterns. Full per-condition breakdowns appear in Appendix~\ref{app:cross-arch}.
98	
99	\subsection{Scale Analysis: Qwen2.5-14B}
100	\label{sec:scale-14b}
101	
102	To assess whether phase-modulated severity persists at larger model scale within the same architecture family, we evaluate Qwen2.5-14B-Instruct on MATH-500 ($n{=}500$) at $s \in \{0.15, 0.20, 0.25, 0.30\}$.
103	
104	\begin{table}[t]
105	\centering
106	\small
107	\caption{Median of per-problem paired severity differences ($\Delta$) under importance-based eviction on Qwen2.5-14B-Instruct (MATH-500). \textit{Results pending.}}
108	\label{tab:scale-14b}
109	\begin{tabular}{@{}lcccc@{}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7c8d5505-1cf3-4db2-81a6-3ef2a3c9c146",
  "uuid": "7bc54ac3-4d3a-460c-bd73-0333cc826851",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex",
      "content": "\\label{sec:crossover}\n\nThe phase-strategy crossover is model-dependent. For DeepSeek ($n{=}496$), a strategy ranking reversal emerges at all four sparsity levels: at $s{=}0.25$, importance-based eviction yields \\emph{lower} II than random in the high-sparsity phase ($0.021$ vs.\\ $1.113$) but \\emph{higher} II in the low-sparsity phase ($3.971$ vs.\\ $1.514$---a $2.6{\\times}$ reversal; both $p < 10^{-4}$), with reversal magnitude ranging from $2.2{\\times}$ to $4.0{\\times}$ across $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$. Qwen does \\emph{not} exhibit this crossover: importance-based eviction produces lower II than random in both phases (e.g., at $s{=}0.25$: high $0.004$ vs.\\ $1.108$; low $1.053$ vs.\\ $1.769$). This divergence suggests the crossover arises from model-specific attention head specialization patterns rather than a universal compound-sparsity property. Full crossover analysis appears in Appendix~\\ref{app:crossover-details}.\n\n\\subsection{Replication Across Training Paradigms}\n\\label{sec:cross-model}\n\nDeepSeek-R1-Distill-Qwen-7B (distillation-trained) and Qwen2.5-7B-Instruct (instruction-tuned) share the Qwen2 backbone but differ in training objective, providing a within-architecture-family comparison across training paradigms.\nQwen2.5-7B-Instruct ($n_{\\text{eff}}{=}475$) reproduces the monotonic severity gradient: $\\Delta$ increases from $0.07$ at $s{=}0.15$ to $3.16$ at $s{=}0.30$ (all Bonferroni-corrected $p < 10^{-14}$), paralleling DeepSeek at approximately one-quarter to one-sixth the magnitude. Both models yield strictly increasing median $\\Delta$ trajectories (Jonckheere-Terpstra $z \\geq 6.2$, $p < 10^{-9}$; see \\S\\ref{par:stats}). Random eviction on Qwen mirrors DeepSeek: non-significant at $s \\leq 0.20$, becoming significant at $s \\geq 0.25$ ($\\Delta{=}0.39$--$0.91$; $p_{\\text{Bonf}} < 10^{-10}$) but $2.7$--$20{\\times}$ weaker than importance-based. A caveat: 45.2\\% of Qwen problems yield null mid-phase segments due to low temporal autocorrelation ($r{=}0.718$ vs.\\ $0.894$); this does not affect $\\Delta$ (Appendix~\\ref{app:qwen-null-rate}). Full tables in Appendix~\\ref{app:cross-model-details}.\n\n\\subsection{Cross-Architecture Validation}\n\\label{sec:cross-arch}\n\nCross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, $n{=}250$, MATH-500) supports the generality of phase-modulated compound interaction beyond the Qwen2 architecture family. Under importance-based eviction, the paired median difference $\\Delta$ rises monotonically from $0.050$ ($s{=}0.15$) to $0.695$ ($s{=}0.30$), with large effect sizes throughout ($d_z{=}0.81$--$1.15$; all $p < 10^{-29}$; Table~\\ref{tab:llama-cross-arch}).\n\nA key architectural difference emerges in strategy specificity. On LLaMA, random eviction also exhibits significant phase gradients ($\\Delta{=}0.025$--$0.271$; $d_z{=}0.41$--$0.46$; all $p < 10^{-12}$), unlike DeepSeek and Qwen where random is non-significant at $s \\leq 0.20$. The importance/random $\\Delta$ ratio is $2.0$--$2.6{\\times}$ on LLaMA, substantially weaker than the $15$--$17{\\times}$ observed on DeepSeek. Dose-response monotonicity holds for both strategies (all conditions monotonic). This indicates that the phase gradient itself is architecture-general, while the degree of strategy specificity is architecture-dependent, likely reflecting differences between GQA (LLaMA, 32 heads with 8 KV groups) and MHA (Qwen2, 28 heads) in how head pruning differentially disrupts importance scoring.\n\nAbsolute interaction magnitudes are approximately $7$--$12{\\times}$ smaller than Qwen2-family models at matched sparsity, consistent with architecture-specific attention head specialization patterns. Full per-condition breakdowns appear in Appendix~\\ref{app:cross-arch}.\n\n\\subsection{Scale Analysis: Qwen2.5-14B}\n\\label{sec:scale-14b}\n\nTo assess whether phase-modulated severity persists at larger model scale within the same architecture family, we evaluate Qwen2.5-14B-Instruct on MATH-500 ($n{=}500$) at $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Median of per-problem paired severity differences ($\\Delta$) under importance-based eviction on Qwen2.5-14B-Instruct (MATH-500). \\textit{Results pending.}}\n\\label{tab:scale-14b}\n\\begin{tabular}{@{}lcccc@{}}",
      "numLines": 30,
      "startLine": 80,
      "totalLines": 195
    }
  }
}
```

</details>

---

### Assistant

_source line 26_

Now I can see the "2.7--20×" appears in both `results.tex` line 88 and `appendix_disc_analysis.tex` line 53. Let me check the GSM8K data in results.tex for problem 3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7c8d5505-1cf3-4db2-81a6-3ef2a3c9c146",
  "uuid": "16daff93-dade-4849-854b-36e2ac2c0a5c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013pmvNYBcBQrPV6ouK6K6zp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2805,
      "cache_read_input_tokens": 28776,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2805
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

_source line 27_

<details open><summary>🔧 Tool call — Grep · `toolu_01GP7bEWtUKtpVVGLZuWCBfJ`</summary>

```json
{
  "pattern": "GSM8K",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex",
  "output_mode": "content",
  "-n": true,
  "-C": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7c8d5505-1cf3-4db2-81a6-3ef2a3c9c146",
  "uuid": "a2341265-2b4a-41da-9b3b-b498f4527ae0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013pmvNYBcBQrPV6ouK6K6zp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2805,
      "cache_read_input_tokens": 28776,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2805
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

_source line 28 · 2026-05-16T22:50:20.218Z_

<details><summary>↩ Tool result · `toolu_01GP7bEWtUKtpVVGLZuWCBfJ`</summary>

```text
119-%% PLACEHOLDER: Fill Table~\ref{tab:scale-14b} when c12 experiment completes.
120-%% Expected analysis: (1) whether 14B amplifies or attenuates severity relative to 7B,
121-%% (2) whether strategy specificity ratio is scale-invariant,
122-%% (3) comparison of phase segmentation thresholds at larger scale.
123-
124:\subsection{Cross-Benchmark Validation: GSM8K}
125-\label{sec:cross-benchmark}
126-
127:[Omitted long matching line]
128-
129:[Omitted long matching line]
130-
131:\paragraph{GSM8K accuracy under compound sparsity.}
132:[Omitted long matching line]
133-
134-\subsection{Cross-Benchmark Validation: GPQA Diamond}
135-\label{sec:cross-benchmark-gpqa}
136-
137-To assess generalization beyond mathematical reasoning, we evaluate both models on GPQA Diamond~\cite{rein-gpqa-2024} ($n{=}198$), a graduate-level science QA benchmark requiring multi-step reasoning across physics, chemistry, and biology.
--
150-\bottomrule
151-\end{tabular}
152-\end{table}
153-
154-%% PLACEHOLDER: Fill Table~\ref{tab:gpqa-results} when c11 experiment completes.
155:%% Expected analysis: (1) phase gradient direction consistency with MATH-500/GSM8K,
156-%% (2) strategy specificity comparison across task types (math vs. science reasoning),
157-%% (3) whether cognitive load modulation hypothesis extends to non-mathematical domains.
158-
159-\subsection{Statistical Validation}
160-\label{sec:stat-validation}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7c8d5505-1cf3-4db2-81a6-3ef2a3c9c146",
  "uuid": "4f1c19df-b9ab-45a0-9817-8cfdf2524342",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "119-%% PLACEHOLDER: Fill Table~\\ref{tab:scale-14b} when c12 experiment completes.\n120-%% Expected analysis: (1) whether 14B amplifies or attenuates severity relative to 7B,\n121-%% (2) whether strategy specificity ratio is scale-invariant,\n122-%% (3) comparison of phase segmentation thresholds at larger scale.\n123-\n124:\\subsection{Cross-Benchmark Validation: GSM8K}\n125-\\label{sec:cross-benchmark}\n126-\n127:[Omitted long matching line]\n128-\n129:[Omitted long matching line]\n130-\n131:\\paragraph{GSM8K accuracy under compound sparsity.}\n132:[Omitted long matching line]\n133-\n134-\\subsection{Cross-Benchmark Validation: GPQA Diamond}\n135-\\label{sec:cross-benchmark-gpqa}\n136-\n137-To assess generalization beyond mathematical reasoning, we evaluate both models on GPQA Diamond~\\cite{rein-gpqa-2024} ($n{=}198$), a graduate-level science QA benchmark requiring multi-step reasoning across physics, chemistry, and biology.\n--\n150-\\bottomrule\n151-\\end{tabular}\n152-\\end{table}\n153-\n154-%% PLACEHOLDER: Fill Table~\\ref{tab:gpqa-results} when c11 experiment completes.\n155:%% Expected analysis: (1) phase gradient direction consistency with MATH-500/GSM8K,\n156-%% (2) strategy specificity comparison across task types (math vs. science reasoning),\n157-%% (3) whether cognitive load modulation hypothesis extends to non-mathematical domains.\n158-\n159-\\subsection{Statistical Validation}\n160-\\label{sec:stat-validation}",
    "numLines": 31
  }
}
```

</details>

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Read · `toolu_0137fCoFKwAicew3W4PiuVgZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex",
  "offset": 124,
  "limit": 12
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7c8d5505-1cf3-4db2-81a6-3ef2a3c9c146",
  "uuid": "60ecde2b-d00f-4729-bbef-b1b103db51c3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GsqR6XSfi9eBk4CQnD7pfG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 667,
      "cache_read_input_tokens": 31581,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 667
      },
      "output_tokens": 68,
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

_source line 30 · 2026-05-16T22:50:23.875Z_

<details><summary>↩ Tool result · `toolu_0137fCoFKwAicew3W4PiuVgZ`</summary>

```text
124	\subsection{Cross-Benchmark Validation: GSM8K}
125	\label{sec:cross-benchmark}
126	
127	To assess task generalization, we evaluate both models on GSM8K ($n{=}50$) at $s \in \{0.15, 0.20, 0.25, 0.30\}$. On DeepSeek (clean data, no output truncation), importance-based eviction replicates the MATH-500 phase gradient across all four sparsity levels with a strict dose-response: $\Delta{=}0.24$ at $s{=}0.15$ rising to $4.68$ at $s{=}0.30$ (all $p \leq 0.0003$, Wilcoxon). Strategy specificity on GSM8K manifests as a \emph{qualitative} gap: importance-based eviction produces significant phase gradients while random eviction is non-significant across all conditions (CIs spanning zero).
128	
129	We interpret this attenuation as \emph{reasoning depth scaling}: strategy specificity scales with reasoning chain depth. MATH-500 (complex multi-step reasoning, strategy ratio $15$--$17{\times}$) produces stronger phase contrast than GSM8K (simpler arithmetic, ratio ${\sim}3{\times}$). Within MATH-500, longer traces exhibit higher strategy specificity (Spearman $\rho > 0$, $p < 0.02$), providing continuous correlational support. This scaling relationship is predictive: tasks with deeper reasoning chains should exhibit stronger strategy${\times}$phase interactions, because longer low-sparsity phases provide more opportunity for importance discrimination collapse to accumulate. Qwen GSM8K results are inconclusive due to generation truncation (\texttt{max\_new\_tokens}${=}$2047): while directional consistency holds at $s \geq 0.25$ ($\Delta{=}1.14$--$4.62$; $p < 10^{-4}$), absolute values and phase assignments are unreliable because all outputs hit the token limit. Full tables in Appendix~\ref{app:gsm8k}.
130	
131	\paragraph{GSM8K accuracy under compound sparsity.}
132	A power analysis on GSM8K ($n{=}50$) reveals a strategy-dependent asymmetry in downstream accuracy. Under random head removal, all 8 conditions (2 models $\times$ 4 sparsity levels) are non-significant (max $|d|{=}0.164$). Post-hoc power analysis indicates $n{=}50$ can detect effects of $d \geq 0.40$ ($\alpha{=}0.05$, power${=}0.80$); all random conditions showed $|d| \leq 0.164$, meaning the null results may reflect insufficient power rather than true absence of effect. Under importance-based pruning, Qwen exhibits a medium-sized accuracy degradation at $s \geq 0.25$ ($d \approx 0.63$, power ${>}\,0.99$), consistent with the PPL-based severity gradient observed on MATH-500. DeepSeek importance conditions exhibit a qualitative downward trend in accuracy but are excluded from parametric inference due to heavy-tailed distributions that violate test assumptions.
133	
134	\subsection{Cross-Benchmark Validation: GPQA Diamond}
135	\label{sec:cross-benchmark-gpqa}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7c8d5505-1cf3-4db2-81a6-3ef2a3c9c146",
  "uuid": "66cae9d0-389d-4d34-b31f-56fb74ebf807",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex",
      "content": "\\subsection{Cross-Benchmark Validation: GSM8K}\n\\label{sec:cross-benchmark}\n\nTo assess task generalization, we evaluate both models on GSM8K ($n{=}50$) at $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$. On DeepSeek (clean data, no output truncation), importance-based eviction replicates the MATH-500 phase gradient across all four sparsity levels with a strict dose-response: $\\Delta{=}0.24$ at $s{=}0.15$ rising to $4.68$ at $s{=}0.30$ (all $p \\leq 0.0003$, Wilcoxon). Strategy specificity on GSM8K manifests as a \\emph{qualitative} gap: importance-based eviction produces significant phase gradients while random eviction is non-significant across all conditions (CIs spanning zero).\n\nWe interpret this attenuation as \\emph{reasoning depth scaling}: strategy specificity scales with reasoning chain depth. MATH-500 (complex multi-step reasoning, strategy ratio $15$--$17{\\times}$) produces stronger phase contrast than GSM8K (simpler arithmetic, ratio ${\\sim}3{\\times}$). Within MATH-500, longer traces exhibit higher strategy specificity (Spearman $\\rho > 0$, $p < 0.02$), providing continuous correlational support. This scaling relationship is predictive: tasks with deeper reasoning chains should exhibit stronger strategy${\\times}$phase interactions, because longer low-sparsity phases provide more opportunity for importance discrimination collapse to accumulate. Qwen GSM8K results are inconclusive due to generation truncation (\\texttt{max\\_new\\_tokens}${=}$2047): while directional consistency holds at $s \\geq 0.25$ ($\\Delta{=}1.14$--$4.62$; $p < 10^{-4}$), absolute values and phase assignments are unreliable because all outputs hit the token limit. Full tables in Appendix~\\ref{app:gsm8k}.\n\n\\paragraph{GSM8K accuracy under compound sparsity.}\nA power analysis on GSM8K ($n{=}50$) reveals a strategy-dependent asymmetry in downstream accuracy. Under random head removal, all 8 conditions (2 models $\\times$ 4 sparsity levels) are non-significant (max $|d|{=}0.164$). Post-hoc power analysis indicates $n{=}50$ can detect effects of $d \\geq 0.40$ ($\\alpha{=}0.05$, power${=}0.80$); all random conditions showed $|d| \\leq 0.164$, meaning the null results may reflect insufficient power rather than true absence of effect. Under importance-based pruning, Qwen exhibits a medium-sized accuracy degradation at $s \\geq 0.25$ ($d \\approx 0.63$, power ${>}\\,0.99$), consistent with the PPL-based severity gradient observed on MATH-500. DeepSeek importance conditions exhibit a qualitative downward trend in accuracy but are excluded from parametric inference due to heavy-tailed distributions that violate test assumptions.\n\n\\subsection{Cross-Benchmark Validation: GPQA Diamond}\n\\label{sec:cross-benchmark-gpqa}",
      "numLines": 12,
      "startLine": 124,
      "totalLines": 195
    }
  }
}
```

</details>

---

### Assistant

_source line 31_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the context I need. Let me summarize:

**Problem 1**: The "2.7--20×" appears in two places:
- `results.tex` line 88: "but $2.7$--$20{\times}$ weaker than importance-based"
- `appendix_disc_analysis.tex` line 53: "but $2.7$--$20{\times}$ weaker than importance-based"

The correct value per line 100 of `appendix_moved.tex` is "2.7--3.5×" (for Qwen specifically). But wait — the context in results.tex line 88 says "Random eviction on Qwen mirrors DeepSeek: non-significant at $s \leq 0.20$, becoming significant at $s \geq 0.25$ ($\Delta{=}0.39$--$0.91$; $p_{\text{Bonf}} < 10^{-10}$)

but $2.7$--$20{\times}$ weaker than importance-based."

Looking at appendix_moved.tex line 100, for Qwen specifically, random is 2.7--3.5× weaker than importance-based. The "20×" must be referring to the DeepSeek ratio. Checking the conclusion at line 4: "Random eviction is $2.7$--$17{\times}$ weaker where both strategies are significant ($s \geq 0.25$; DeepSeek $15$--$17{\times}$, Qwen $2.7$--$3.5{\times}$)"

So the combined range across both models is 2.7--17×, not 2.7--20×. Looking at the full sentence structure, "Random eviction on Qwen mirrors DeepSeek" describes the pattern, but the 2.7--20× ratio that follows is specifically about Qwen's performance compared to importance-based methods. Since Qwen's actual range is 2.7--3.5×, not 2.7--20×, this appears to be an error in the manuscript—the upper bound should be corrected to 3.5× rather than 20×. I'm finding the actual occurrences in results.tex line 88 and appendix_disc_analysis.tex line 53 rather than the file reference mentioned in the task, but both contain the same "2.7--20×" text that needs to be changed to "2.7--3.5×" based on the Qwen-specific data. Looking at the appendix text more carefully, the sentence about "2.7--20×" applies to both models even though only Qwen's specific metrics are listed. I need to check what the actual ratio is for DeepSeek at that same sparsity level to determine if the range should be adjusted to reflect both models' comparisons. The user is pointing out that the "20×" figure can't be validated from the actual data—the calculations show 2.7× and 3.5× instead. This applies to the Qwen random vs importance comparison in results.tex line 88. For the broader statement about both models in appendix_disc_analysis.tex line 53, if DeepSeek ranges from 15–17×, I need to recalculate what the combined range actually is.

So my approach should be: fix results.tex line 88 to use the Qwen-specific values of 2.7–3.5×, and fix appendix_disc_analysis.tex line 53 to reflect the correct combined range of 2.7–17× rather than 2.7–20×. But I should double-check what the user's original task actually specified, since they may have only asked for one correction. I'm checking the context for the appendix statement about random eviction across both models. The sentence references $n{=}500$ and describes effects on both DeepSeek and Qwen, so the combined range should be 2.7× to 17×, not the narrower Qwen-specific range of 2.7–3.5×. Looking at the user's original problem statement more carefully, they're pointing to specific data: the ratio calculations show 0.39 vs 1.07 equals 2.7×, and 0.91 vs 3.16 equals 3.5×. So the range should be 2.7--3.5× for Qwen's performance. I need to fix results.tex line 88 with this correct range, and also update appendix_disc_analysis.tex line 53 accordingly since it references the same comparison. Looking at results.tex line 129, the "~3×" ratio for GSM8K is actually stated in the paper itself when comparing it to MATH-500's 15--17× ratio. The issue is that while this ratio is mentioned, the random eviction condition shows non-significant results with confidence intervals spanning zero on GSM8K, which seems to contradict claiming a meaningful 3× effect there.

The user's suggestion to reframe this as "MATH-500 (15--17×) > GSM8K (2.3--3.8×, though random gradients less reliably estimated)" makes sense — it acknowledges the point estimates while flagging that the random condition isn't reliably estimated. I need to find the actual point estimates for GSM8K random in the appendix to see what range we're working with.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7c8d5505-1cf3-4db2-81a6-3ef2a3c9c146",
  "uuid": "e9db0e03-e23b-43c1-b80a-851ea74a822f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DPLm3aXCpQGWaWdkjfWNJ7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 967,
      "cache_read_input_tokens": 32248,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 967
      },
      "output_tokens": 13,
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

_source line 32_

Let me find the GSM8K appendix data for problem 3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7c8d5505-1cf3-4db2-81a6-3ef2a3c9c146",
  "uuid": "9e58d2d8-f04d-4a72-83bd-f20cc2a2f398",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DPLm3aXCpQGWaWdkjfWNJ7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 967,
      "cache_read_input_tokens": 32248,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 967
      },
      "output_tokens": 13,
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

_source line 33_

<details open><summary>🔧 Tool call — Grep · `toolu_013scDQ62Thg6ypLigFgEoLv`</summary>

```json
{
  "pattern": "GSM8K.*random|random.*GSM8K",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
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
  "session_id": "7c8d5505-1cf3-4db2-81a6-3ef2a3c9c146",
  "uuid": "1cdc0402-b829-485f-a7e3-e8749af3542f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DPLm3aXCpQGWaWdkjfWNJ7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 967,
      "cache_read_input_tokens": 32248,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 967
      },
      "output_tokens": 13,
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

_source line 34 · 2026-05-16T22:51:32.741Z_

<details><summary>↩ Tool result · `toolu_013scDQ62Thg6ypLigFgEoLv`</summary>

```text
artifacts/_project/paper/discussion.tex:8:[Omitted long matching line]
artifacts/_project/paper/limitations.tex:5:[Omitted long matching line]
artifacts/_project/paper/appendix_disc_analysis.tex:68:[Omitted long matching line]
artifacts/_project/paper/introduction.tex:25:    \item We characterize a \textbf{phase-modulated compound severity gradient}: importance-based eviction exhibits a monotonic dose-response ($\rho{=}1.0$; $\Delta$: $0.39 \to 8.48$) with a phase gradient $2.7$--$17{\times}$ larger than random eviction where both strategies are significant ($s \geq 0.25$) on MATH-500; the gradient direction is consistent on GSM8K, while strategy specificity attenuates (\S\ref{sec:cross-benchmark}).
artifacts/_project/paper/results.tex:127:[Omitted long matching line]
artifacts/_project/paper/results.tex:132:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7c8d5505-1cf3-4db2-81a6-3ef2a3c9c146",
  "uuid": "6fbc97d1-ee1b-4148-a918-ba73da22c01d",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "artifacts/_project/paper/discussion.tex:8:[Omitted long matching line]\nartifacts/_project/paper/limitations.tex:5:[Omitted long matching line]\nartifacts/_project/paper/appendix_disc_analysis.tex:68:[Omitted long matching line]\nartifacts/_project/paper/introduction.tex:25:    \\item We characterize a \\textbf{phase-modulated compound severity gradient}: importance-based eviction exhibits a monotonic dose-response ($\\rho{=}1.0$; $\\Delta$: $0.39 \\to 8.48$) with a phase gradient $2.7$--$17{\\times}$ larger than random eviction where both strategies are significant ($s \\geq 0.25$) on MATH-500; the gradient direction is consistent on GSM8K, while strategy specificity attenuates (\\S\\ref{sec:cross-benchmark}).\nartifacts/_project/paper/results.tex:127:[Omitted long matching line]\nartifacts/_project/paper/results.tex:132:[Omitted long matching line]",
    "numLines": 6
  }
}
```

</details>

---

### Tool call

_source line 35_

<details open><summary>🔧 Tool call — Grep · `toolu_011Nt22nFFWUDAKXmMLboacA`</summary>

```json
{
  "pattern": "app:gsm8k|gsm8k",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7c8d5505-1cf3-4db2-81a6-3ef2a3c9c146",
  "uuid": "2858c771-1416-4d68-9518-0e45f3522217",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DPLm3aXCpQGWaWdkjfWNJ7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 967,
      "cache_read_input_tokens": 32248,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 967
      },
      "output_tokens": 13,
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

_source line 36 · 2026-05-16T22:51:33.611Z_

<details><summary>↩ Tool result · `toolu_011Nt22nFFWUDAKXmMLboacA`</summary>

```text
Found 3 files
artifacts/_project/paper/appendix_disc_analysis.tex
artifacts/_project/paper/results.tex
artifacts/_project/paper/main.aux
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7c8d5505-1cf3-4db2-81a6-3ef2a3c9c146",
  "uuid": "2ccbe68a-cbb7-408a-bc99-3f0a91c51628",
  "tool_use_result": {
    "mode": "files_with_matches",
    "filenames": [
      "artifacts/_project/paper/appendix_disc_analysis.tex",
      "artifacts/_project/paper/results.tex",
      "artifacts/_project/paper/main.aux"
    ],
    "numFiles": 3
  }
}
```

</details>

---

### Tool call

_source line 37_

<details open><summary>🔧 Tool call — Read · `toolu_01XDLDJusmonaquJoMj5Dn72`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex",
  "offset": 62,
  "limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7c8d5505-1cf3-4db2-81a6-3ef2a3c9c146",
  "uuid": "af2dc9b4-5ec2-4a67-ba02-d7a6201dbc6c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LnybzWbuirFP9x9Dxtjw1S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4484,
      "cache_read_input_tokens": 33215,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4484
      },
      "output_tokens": 53,
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

_source line 38 · 2026-05-16T22:51:38.035Z_

<details><summary>↩ Tool result · `toolu_01XDLDJusmonaquJoMj5Dn72`</summary>

```text
62	
63	
64	
65	\section{Cross-Benchmark Validation: GSM8K}
66	\label{app:gsm8k}
67	
68	Tables~\ref{tab:gsm8k-ds} and \ref{tab:gsm8k-qw} report the per-phase II breakdown on GSM8K ($n{=}50$) for DeepSeek and Qwen, respectively. All statistics use medians, Wilcoxon signed-rank tests, and bootstrap median CIs ($B{=}10{,}000$), matching the MATH-500 methodology. DeepSeek importance-based eviction replicates the MATH-500 phase gradient across all four sparsity levels (all $p \leq 0.0003$) with a strict dose-response ($\Delta$: $0.24 \to 4.68$). Qwen importance-based eviction is significant at $s \geq 0.25$ ($p < 10^{-4}$). Random eviction is non-significant across all conditions for both models; Qwen random $s{=}0.30$ is excluded due to data quality concerns (output truncation producing extreme II values).
69	
70	\paragraph{Power analysis for random conditions.}
71	Post-hoc power analysis indicates that at $n{=}50$, the minimum detectable effect size is $d \geq 0.40$ ($\alpha{=}0.05$, power${=}0.80$). All 8 random conditions (2 models $\times$ 4 sparsity levels) show $|d| \leq 0.164$, well below the detectability threshold; their non-significance should therefore be interpreted as absence of evidence rather than evidence of absence. By contrast, Qwen importance-based eviction at $s \geq 0.25$ is adequately powered ($d \approx 0.63$, power ${>}\,0.99$), indicating that the observed significance reflects a genuine effect.
72	
73	\begin{table*}[t]
74	\centering
75	\small
76	\caption{Per-phase interaction index on GSM8K: DeepSeek-R1-Distill-Qwen-7B ($n{=}50$). $\Delta$: paired median difference ($\widetilde{\mathrm{II}}_{\textit{low}} - \widetilde{\mathrm{II}}_{\textit{high}}$) with bootstrap 95\% CI ($B{=}10{,}000$, median statistic). $p$: Wilcoxon signed-rank, Bonferroni-corrected ($k{=}4$).}
77	\label{tab:gsm8k-ds}
78	\begin{tabular}{@{}llcccc@{}}
79	\toprule
80	$s$ & Strategy & $\widetilde{\mathrm{II}}_{\textit{high}}$ & $\widetilde{\mathrm{II}}_{\textit{low}}$ & $\Delta$\; [95\% CI] & $p_{\text{Bonf}}$ \\
81	\midrule
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7c8d5505-1cf3-4db2-81a6-3ef2a3c9c146",
  "uuid": "c7815ba0-53e8-4d43-aae5-1c8ed7229151",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex",
      "content": "\n\n\n\\section{Cross-Benchmark Validation: GSM8K}\n\\label{app:gsm8k}\n\nTables~\\ref{tab:gsm8k-ds} and \\ref{tab:gsm8k-qw} report the per-phase II breakdown on GSM8K ($n{=}50$) for DeepSeek and Qwen, respectively. All statistics use medians, Wilcoxon signed-rank tests, and bootstrap median CIs ($B{=}10{,}000$), matching the MATH-500 methodology. DeepSeek importance-based eviction replicates the MATH-500 phase gradient across all four sparsity levels (all $p \\leq 0.0003$) with a strict dose-response ($\\Delta$: $0.24 \\to 4.68$). Qwen importance-based eviction is significant at $s \\geq 0.25$ ($p < 10^{-4}$). Random eviction is non-significant across all conditions for both models; Qwen random $s{=}0.30$ is excluded due to data quality concerns (output truncation producing extreme II values).\n\n\\paragraph{Power analysis for random conditions.}\nPost-hoc power analysis indicates that at $n{=}50$, the minimum detectable effect size is $d \\geq 0.40$ ($\\alpha{=}0.05$, power${=}0.80$). All 8 random conditions (2 models $\\times$ 4 sparsity levels) show $|d| \\leq 0.164$, well below the detectability threshold; their non-significance should therefore be interpreted as absence of evidence rather than evidence of absence. By contrast, Qwen importance-based eviction at $s \\geq 0.25$ is adequately powered ($d \\approx 0.63$, power ${>}\\,0.99$), indicating that the observed significance reflects a genuine effect.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Per-phase interaction index on GSM8K: DeepSeek-R1-Distill-Qwen-7B ($n{=}50$). $\\Delta$: paired median difference ($\\widetilde{\\mathrm{II}}_{\\textit{low}} - \\widetilde{\\mathrm{II}}_{\\textit{high}}$) with bootstrap 95\\% CI ($B{=}10{,}000$, median statistic). $p$: Wilcoxon signed-rank, Bonferroni-corrected ($k{=}4$).}\n\\label{tab:gsm8k-ds}\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\n$s$ & Strategy & $\\widetilde{\\mathrm{II}}_{\\textit{high}}$ & $\\widetilde{\\mathrm{II}}_{\\textit{low}}$ & $\\Delta$\\; [95\\% CI] & $p_{\\text{Bonf}}$ \\\\\n\\midrule",
      "numLines": 20,
      "startLine": 62,
      "totalLines": 164
    }
  }
}
```

</details>

---

### Tool call

_source line 39_

<details open><summary>🔧 Tool call — Read · `toolu_01RmjqAF9u5m6gX9Q2TCGAjw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex",
  "offset": 81,
  "limit": 40
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7c8d5505-1cf3-4db2-81a6-3ef2a3c9c146",
  "uuid": "15f79bbc-8441-4d50-9103-94355b7f5e0e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HJHo6WSBds5Ts7nGe1RTe9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 915,
      "cache_read_input_tokens": 37699,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 915
      },
      "output_tokens": 68,
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

_source line 40 · 2026-05-16T22:51:41.560Z_

<details><summary>↩ Tool result · `toolu_01RmjqAF9u5m6gX9Q2TCGAjw`</summary>

```text
81	\midrule
82	0.15 & Importance & $-$0.001 & 0.241 & 0.24\; $[0.08,\; 0.48]$ & 0.0003 \\
83	0.15 & Random     & 0.036 & 0.105 & $-$0.04\textsuperscript{ns} & 0.90 \\
84	\addlinespace
85	0.20 & Importance & $-$0.002 & 0.740 & 0.74\; $[0.31,\; 1.12]$ & ${<}\,10^{-4}$ \\
86	0.20 & Random     & 0.143 & 0.423 & 0.28\textsuperscript{ns} & 0.96 \\
87	\addlinespace
88	0.25 & Importance & 0.009 & 1.992 & 1.99\; $[0.93,\; 2.82]$ & ${<}\,10^{-4}$ \\
89	0.25 & Random     & 0.619 & 1.603 & 0.98\textsuperscript{ns} & 0.83 \\
90	\addlinespace
91	0.30 & Importance & 0.024 & 4.682 & 4.68\; $[2.12,\; 10.56]$ & ${<}\,10^{-4}$ \\
92	0.30 & Random     & 1.837 & 4.683 & 2.85\textsuperscript{ns} & 0.54 \\
93	\bottomrule
94	\end{tabular}
95	\end{table*}
96	
97	\begin{table*}[t]
98	\centering
99	\small
100	\caption{Per-phase interaction index on GSM8K: Qwen2.5-7B-Instruct ($n{=}50$). Outputs truncated at \texttt{max\_new\_tokens}${=}$2047; absolute values should be interpreted with this limitation. $^{\ddagger}$Excluded: extreme II values from truncation artifacts render this condition invalid.}
101	\label{tab:gsm8k-qw}
102	\begin{tabular}{@{}llcccc@{}}
103	\toprule
104	$s$ & Strategy & $\widetilde{\mathrm{II}}_{\textit{high}}$ & $\widetilde{\mathrm{II}}_{\textit{low}}$ & $\Delta$\; [95\% CI] & $p_{\text{Bonf}}$ \\
105	\midrule
106	0.15 & Importance & 0.000 & 0.029 & 0.03\textsuperscript{ns} & 0.39 \\
107	0.15 & Random     & 0.089 & 0.033 & $-$1.58\textsuperscript{ns} & 0.69 \\
108	\addlinespace
109	0.20 & Importance & 0.004 & 0.180 & 0.09\textsuperscript{ns} & 0.62 \\
110	0.20 & Random     & 0.201 & 0.356 & 4.88\textsuperscript{ns} & 0.57 \\
111	\addlinespace
112	0.25 & Importance & 0.009 & 1.064 & 1.14\; $[0.62,\; 1.66]$ & ${<}\,10^{-4}$ \\
113	0.25 & Random     & 0.802 & 1.213 & 11.1\textsuperscript{ns} & 0.39 \\
114	\addlinespace
115	0.30 & Importance & 0.023 & 2.140 & 4.62\; $[2.88,\; 6.92]$ & ${<}\,10^{-4}$ \\
116	0.30 & Random$^{\ddagger}$     & \multicolumn{4}{c}{\textit{excluded (data quality)}} \\
117	\bottomrule
118	\end{tabular}
119	\end{table*}
120	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7c8d5505-1cf3-4db2-81a6-3ef2a3c9c146",
  "uuid": "eb5ce4bc-9b5a-48eb-8b47-5ef2611b842d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex",
      "content": "\\midrule\n0.15 & Importance & $-$0.001 & 0.241 & 0.24\\; $[0.08,\\; 0.48]$ & 0.0003 \\\\\n0.15 & Random     & 0.036 & 0.105 & $-$0.04\\textsuperscript{ns} & 0.90 \\\\\n\\addlinespace\n0.20 & Importance & $-$0.002 & 0.740 & 0.74\\; $[0.31,\\; 1.12]$ & ${<}\\,10^{-4}$ \\\\\n0.20 & Random     & 0.143 & 0.423 & 0.28\\textsuperscript{ns} & 0.96 \\\\\n\\addlinespace\n0.25 & Importance & 0.009 & 1.992 & 1.99\\; $[0.93,\\; 2.82]$ & ${<}\\,10^{-4}$ \\\\\n0.25 & Random     & 0.619 & 1.603 & 0.98\\textsuperscript{ns} & 0.83 \\\\\n\\addlinespace\n0.30 & Importance & 0.024 & 4.682 & 4.68\\; $[2.12,\\; 10.56]$ & ${<}\\,10^{-4}$ \\\\\n0.30 & Random     & 1.837 & 4.683 & 2.85\\textsuperscript{ns} & 0.54 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Per-phase interaction index on GSM8K: Qwen2.5-7B-Instruct ($n{=}50$). Outputs truncated at \\texttt{max\\_new\\_tokens}${=}$2047; absolute values should be interpreted with this limitation. $^{\\ddagger}$Excluded: extreme II values from truncation artifacts render this condition invalid.}\n\\label{tab:gsm8k-qw}\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\n$s$ & Strategy & $\\widetilde{\\mathrm{II}}_{\\textit{high}}$ & $\\widetilde{\\mathrm{II}}_{\\textit{low}}$ & $\\Delta$\\; [95\\% CI] & $p_{\\text{Bonf}}$ \\\\\n\\midrule\n0.15 & Importance & 0.000 & 0.029 & 0.03\\textsuperscript{ns} & 0.39 \\\\\n0.15 & Random     & 0.089 & 0.033 & $-$1.58\\textsuperscript{ns} & 0.69 \\\\\n\\addlinespace\n0.20 & Importance & 0.004 & 0.180 & 0.09\\textsuperscript{ns} & 0.62 \\\\\n0.20 & Random     & 0.201 & 0.356 & 4.88\\textsuperscript{ns} & 0.57 \\\\\n\\addlinespace\n0.25 & Importance & 0.009 & 1.064 & 1.14\\; $[0.62,\\; 1.66]$ & ${<}\\,10^{-4}$ \\\\\n0.25 & Random     & 0.802 & 1.213 & 11.1\\textsuperscript{ns} & 0.39 \\\\\n\\addlinespace\n0.30 & Importance & 0.023 & 2.140 & 4.62\\; $[2.88,\\; 6.92]$ & ${<}\\,10^{-4}$ \\\\\n0.30 & Random$^{\\ddagger}$     & \\multicolumn{4}{c}{\\textit{excluded (data quality)}} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n",
      "numLines": 40,
      "startLine": 81,
      "totalLines": 164
    }
  }
}
```

</details>

---

### Assistant

_source line 41_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data. Let me compute the strategy specificity ratios for GSM8K (DeepSeek, since Qwen has truncation issues):

For DeepSeek GSM8K:
- s=0.15: imp Δ=0.24, rand Δ=-0.04 (NS) → ratio undefined/negative
- s=0.20: imp Δ=0.74, rand Δ=0.28 (NS) → point estimate ratio: 0.74/0.28 = 2.6×


- s=0.25: imp Δ=1.99, rand Δ=0.98 (NS) → point estimate ratio: 1.99/0.98 = 2.0×
- s=0.30: imp Δ=4.68, rand Δ=2.85 (NS) → point estimate ratio: 4.68/2.85 = 1.6×

So the point estimate ratios are actually ranging from 1.6× to 2.6×, not the 3× I was expecting. All the random conditions are non-significant with p-values well above 0.05, which makes sense given the wide confidence intervals. Let me check what the discussion section says about GSM8K.

The current text approximates it as ~3×, but that's not really supported by the data—the DeepSeek point estimates give me 1.6–2.6×, and reporting a ratio when the random baseline isn't significantly different from zero is misleading. I should qualify this by noting that the importance gradient is significant while the random gradient is not, which suggests the effect is qualitative rather than just a magnitude difference. Something like acknowledging that strategy specificity shows up as a significant-versus-nonsignificant pattern on GSM8K, rather than a clean multiplicative effect. I need to follow the user's guidance and check the results.tex file for the specific p-values and confidence intervals on the GSM8K random conditions to determine the best way to fix this. Looking at the data, all eight random conditions show non-significant results with very high p-values (DeepSeek ranges from 0.54 to 0.96, similar pattern for Qwen), so I should qualify the discussion.tex statement to acknowledge that random gradients aren't reliably estimated rather than claiming they're simply non-significant. I'm looking at the full sentence and realizing my proposed fix is getting too wordy. The core issue is that I need to acknowledge GSM8K shows lower strategy specificity than MATH-500 without overstating precision from the random condition results. I'll simplify to just note the point estimate range and flag that the random conditions don't support the effect, keeping it concise enough to fit naturally in the paragraph. I'm checking the actual ratios from the data points where random estimates are reasonably reliable—at s=0.20, s=0.25, and s=0.30, I'm getting roughly 1.6× to 2.6× for the importance-to-random ratio, which doesn't match the 2.3–3.8× range suggested. Let me stick with what the data actually shows rather than forcing numbers that don't align.

I'll revise the claim to be more precise: approximately 2× for GSM8K with a note that the random baseline isn't statistically significant at n=50. Now I need to go through and fix the specific instances in the tex files where I had overstated the range as 2.7–20×, replacing them with the more accurate 2.7–3.5× for the Qwen-specific results. I'm noticing the range cited in the appendix doesn't match what's in the conclusion—the combined range should be 2.7–17× for both models, but I need to verify whether the individual model ratios (DeepSeek 15–17×, Qwen 2.7–3.5×) are actually comparing random versus importance-based eviction or if they're referring to something else entirely. Now I'm ready to apply these corrections across the files—updating the Qwen-specific range in results.tex, adjusting the combined model range in the appendix, fixing the sample size in conclusion.tex, and addressing the GSM8K ratio note in discussion.tex.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7c8d5505-1cf3-4db2-81a6-3ef2a3c9c146",
  "uuid": "e8583f7e-7f80-4e7c-9eb2-50e2806e9aad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xy4HWiPkXNhCw9zi8q61vJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1266,
      "cache_read_input_tokens": 38614,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1266
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

_source line 42_

Now I have all the data. Let me make the fixes.

**Problem 1 summary**: "2.7--20×" appears in two files:
- `results.tex` line 88 (Qwen-specific context → should be 2.7--3.5×)
- `appendix_disc_analysis.tex` line 53 (both-models context → should be 2.7--17× per conclusion.tex)

**Problem 3 data**: GSM8K random is NS across all 8 conditions (DeepSeek p: 0.90, 0.96, 0.83, 0.54). Point-estimate ratios (imp/rand) from DeepSeek: 2.6× (s=0.20), 2.0× (s=0.25), 1.6× (s=0.30). The "~3×" overstates and doesn't acknowledge the NS denominator.

Applying all fixes now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7c8d5505-1cf3-4db2-81a6-3ef2a3c9c146",
  "uuid": "ce44d849-f190-4235-84d8-cea83742a324",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xy4HWiPkXNhCw9zi8q61vJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1266,
      "cache_read_input_tokens": 38614,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1266
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

_source line 43_

<details open><summary>🔧 Tool call — Edit · `toolu_01QjNuygtr6ULkKMFHwpMeNM`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex",
  "old_string": "but $2.7$--$20{\\times}$ weaker than importance-based",
  "new_string": "but $2.7$--$3.5{\\times}$ weaker than importance-based"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7c8d5505-1cf3-4db2-81a6-3ef2a3c9c146",
  "uuid": "f66b828f-1bd2-408d-bdbe-9f381d027ec0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xy4HWiPkXNhCw9zi8q61vJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1266,
      "cache_read_input_tokens": 38614,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1266
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

_source line 44 · 2026-05-16T22:52:37.491Z_

<details><summary>↩ Tool result · `toolu_01QjNuygtr6ULkKMFHwpMeNM`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7c8d5505-1cf3-4db2-81a6-3ef2a3c9c146",
  "uuid": "48bbce2b-e689-410b-8813-978762665d5d",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex",
    "oldString": "but $2.7$--$20{\\times}$ weaker than importance-based",
    "newString": "but $2.7$--$3.5{\\times}$ weaker than importance-based",
    "originalFile": "\n\\section{Results}\n\\label{sec:results}\n\n\\subsection{Strategy-Dependent Severity}\n\\label{sec:strategy-severity}\n\nTable~\\ref{tab:aggregate-ii} reports the median compound severity difference across strategies and sparsity levels. Under importance-based eviction, $\\Delta$ increases from $0.39$ at $s{=}0.15$ to $8.48$ at $s{=}0.30$---a $22{\\times}$ amplification (all Bonferroni-corrected $p \\ll 10^{-10}$). Random eviction develops a detectable but weak phase gradient above $s \\approx 0.20$: at $s \\leq 0.20$, $\\Delta$ is non-significant ($0.01$--$0.03$; CIs span zero); at $s \\geq 0.25$, $\\Delta$ becomes significant ($0.26$--$0.51$; $p_{\\text{Bonf}} < 0.006$) but $15$--$17{\\times}$ smaller than under importance-based eviction. Both strategies exhibit monotonic dose-response (Jonckheere-Terpstra $z{=}6.2$--$33.7$, all $p < 10^{-9}$), but importance masking effect sizes are an order of magnitude larger.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Median of per-problem paired severity differences ($\\Delta$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}496$, MATH-500).}\n\\label{tab:aggregate-ii}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nStrategy & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\\\\n\\midrule\nImportance & 0.39 & 1.21 & 3.99 & 8.48 \\\\\nRandom     & 0.01 & 0.03 & 0.26 & 0.51 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Phase-Modulated Amplification}\n\\label{sec:phase-amplification}\n\nDecomposing II by reasoning phase reveals that strategy-dependent severity is driven by amplification in the low-sparsity phase. Table~\\ref{tab:main-results} reports the per-phase breakdown. Under importance-based eviction, the median II in the low-sparsity phase rises from $0.357$ ($s{=}0.15$) to $8.456$ ($s{=}0.30$), while the high-sparsity phase remains near zero ($0.003$--$0.038$), yielding paired median differences $\\Delta$ from $0.39$ to $8.48$ (all $p \\ll 10^{-10}$). Random eviction shows a detectable but much weaker phase gradient at $s \\geq 0.25$ ($\\Delta{=}0.26$--$0.51$; $p_{\\text{Bonf}} < 0.006$), $15$--$17{\\times}$ smaller than importance-based at matched sparsity. Figure~\\ref{fig:hero} visualizes the dose-response relationship for both models. The per-problem amplification ratio $G$ (Eq.~\\ref{eq:gradient}) provides an auxiliary illustrative perspective and is reported in Appendix~\\ref{app:g-metric}.\nUnder the multiplicative null ($r_b = r_a \\cdot r_k$; Appendix~\\ref{app:multiplicative-null}), the phase-severity gradient is preserved ($G_{\\times}{=}21$--$64{\\times}$); we report additive-null values throughout as the more conservative estimates.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Per-phase interaction index (II) at $n{=}496$/$475$. $\\Delta{=}\\widetilde{\\mathrm{II}^{(i)}_{\\textit{low}} - \\mathrm{II}^{(i)}_{\\textit{high}}}$: median of per-problem paired differences (not the difference of column medians) with bootstrap 95\\% CI ($B{=}10{,}000$). $G$ values reported in Appendix~\\ref{app:g-metric}. Profiling-subset values ($n{=}50$) in Table~\\ref{tab:profiling-subset}.}\n\\label{tab:main-results}\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\n$s$ & Strategy & $\\widetilde{\\mathrm{II}}_{\\textit{high}}$ & $\\widetilde{\\mathrm{II}}_{\\textit{low}}$ & $\\Delta$\\; [95\\% CI] & $p_{\\text{Bonf}}$ \\\\\n\\midrule\n\\multicolumn{6}{@{}l}{\\textit{DeepSeek-R1-Distill-Qwen-7B ($n{=}496$)}} \\\\\n0.15 & Importance & 0.003 & 0.357 & 0.39\\; $[0.35,\\; 0.44]$ & $< 10^{-10}$ \\\\\n0.15 & Random     & 0.083 & 0.090 & 0.01\\; $[-0.02,\\; 0.04]$ & ns \\\\\n\\addlinespace\n0.20 & Importance & 0.008 & 1.211 & 1.21\\; $[1.11,\\; 1.34]$ & $< 10^{-10}$ \\\\\n0.20 & Random     & 0.270 & 0.357 & 0.03\\; $[-0.01,\\; 0.08]$ & ns \\\\\n\\addlinespace\n0.25 & Importance & 0.021 & 3.971 & 3.99\\; $[3.53,\\; 4.36]$ & $< 10^{-10}$ \\\\\n0.25 & Random     & 1.113 & 1.514 & 0.26\\; $[0.13,\\; 0.35]$ & $< 0.006$ \\\\\n\\addlinespace\n0.30 & Importance & 0.038 & 8.456 & 8.48\\; $[7.75,\\; 9.69]$ & $< 10^{-10}$ \\\\\n0.30 & Random     & 3.112 & 3.848 & 0.51\\; $[0.26,\\; 0.89]$ & $< 0.006$ \\\\\n\\midrule\n\\multicolumn{6}{@{}l}{\\textit{Qwen2.5-7B-Instruct ($n{=}475$)}} \\\\\n0.15 & Importance & $-$0.000$^{\\ddagger}$ & 0.044 & 0.07\\; $[0.05,\\; 0.09]$ & $< 10^{-14}$ \\\\\n0.15 & Random     & 0.094 & 0.097 & $-$0.01\\; $[-0.04,\\; 0.01]$ & ns \\\\\n\\addlinespace\n0.20 & Importance & 0.000 & 0.275 & 0.31\\; $[0.26,\\; 0.36]$ & $< 10^{-14}$ \\\\\n0.20 & Random     & 0.291 & 0.356 & 0.02\\; $[-0.01,\\; 0.07]$ & ns \\\\\n\\addlinespace\n0.25 & Importance & 0.004 & 1.053 & 1.07\\; $[0.98,\\; 1.18]$ & $< 10^{-14}$ \\\\\n0.25 & Random     & 1.108 & 1.769 & 0.39\\; $[0.24,\\; 0.55]$ & $< 10^{-10}$ \\\\\n\\addlinespace\n0.30 & Importance & 0.014 & 3.208 & 3.16\\; $[2.78,\\; 3.56]$ & $< 10^{-14}$ \\\\\n0.30 & Random     & 2.819 & 4.253 & 0.91\\; $[0.61,\\; 1.26]$ & $< 10^{-13}$ \\\\\n\\bottomrule\n\\multicolumn{6}{@{}p{0.92\\textwidth}}{\\footnotesize $^{\\ddagger}$ Negative II at this sparsity reflects \\texttt{bfloat16} numerical noise when the interaction effect approaches zero ($|\\mathrm{II}| < 10^{-4}$). $\\Delta{=}0.07$, $p{=}8.7 \\times 10^{-15}$ supports $\\mathrm{II}_{\\textit{low}} > \\mathrm{II}_{\\textit{high}}$.}\n\\end{tabular}\n\\end{table*}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig1_ii_scatter.pdf}\n\\caption{Paired median difference $\\Delta$ (primary metric) as a function of sparsity level $s$ for DeepSeek-R1-Distill-Qwen-7B ($n{=}496$, left) and Qwen2.5-7B-Instruct ($n{=}475$, right). Importance-based eviction (red) exhibits monotonically increasing $\\Delta$ ($0.39$--$8.48$ for DeepSeek, $0.07$--$3.16$ for Qwen); random eviction (blue) remains near zero at low sparsity (ns) and shows weak effects at $s \\geq 0.25$. Error bars show asymmetric bootstrap 95\\% CIs. DeepSeek importance effects are ${\\sim}2.7{\\times}$ larger than Qwen, consistent with the training-paradigm contrast (\\S\\ref{sec:cross-model}). Significance: {*}{*}{*}\\,$p_{\\text{Bonf}} < 0.001$; {*}{*}\\,$p_{\\text{Bonf}} < 0.01$; ns\\,$p_{\\text{Bonf}} > 0.05$.}\n\\label{fig:hero}\n\\end{figure*}\n\n\n\\subsection{Phase-Strategy Crossover}\n\\label{sec:crossover}\n\nThe phase-strategy crossover is model-dependent. For DeepSeek ($n{=}496$), a strategy ranking reversal emerges at all four sparsity levels: at $s{=}0.25$, importance-based eviction yields \\emph{lower} II than random in the high-sparsity phase ($0.021$ vs.\\ $1.113$) but \\emph{higher} II in the low-sparsity phase ($3.971$ vs.\\ $1.514$---a $2.6{\\times}$ reversal; both $p < 10^{-4}$), with reversal magnitude ranging from $2.2{\\times}$ to $4.0{\\times}$ across $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$. Qwen does \\emph{not} exhibit this crossover: importance-based eviction produces lower II than random in both phases (e.g., at $s{=}0.25$: high $0.004$ vs.\\ $1.108$; low $1.053$ vs.\\ $1.769$). This divergence suggests the crossover arises from model-specific attention head specialization patterns rather than a universal compound-sparsity property. Full crossover analysis appears in Appendix~\\ref{app:crossover-details}.\n\n\\subsection{Replication Across Training Paradigms}\n\\label{sec:cross-model}\n\nDeepSeek-R1-Distill-Qwen-7B (distillation-trained) and Qwen2.5-7B-Instruct (instruction-tuned) share the Qwen2 backbone but differ in training objective, providing a within-architecture-family comparison across training paradigms.\nQwen2.5-7B-Instruct ($n_{\\text{eff}}{=}475$) reproduces the monotonic severity gradient: $\\Delta$ increases from $0.07$ at $s{=}0.15$ to $3.16$ at $s{=}0.30$ (all Bonferroni-corrected $p < 10^{-14}$), paralleling DeepSeek at approximately one-quarter to one-sixth the magnitude. Both models yield strictly increasing median $\\Delta$ trajectories (Jonckheere-Terpstra $z \\geq 6.2$, $p < 10^{-9}$; see \\S\\ref{par:stats}). Random eviction on Qwen mirrors DeepSeek: non-significant at $s \\leq 0.20$, becoming significant at $s \\geq 0.25$ ($\\Delta{=}0.39$--$0.91$; $p_{\\text{Bonf}} < 10^{-10}$) but $2.7$--$20{\\times}$ weaker than importance-based. A caveat: 45.2\\% of Qwen problems yield null mid-phase segments due to low temporal autocorrelation ($r{=}0.718$ vs.\\ $0.894$); this does not affect $\\Delta$ (Appendix~\\ref{app:qwen-null-rate}). Full tables in Appendix~\\ref{app:cross-model-details}.\n\n\\subsection{Cross-Architecture Validation}\n\\label{sec:cross-arch}\n\nCross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, $n{=}250$, MATH-500) supports the generality of phase-modulated compound interaction beyond the Qwen2 architecture family. Under importance-based eviction, the paired median difference $\\Delta$ rises monotonically from $0.050$ ($s{=}0.15$) to $0.695$ ($s{=}0.30$), with large effect sizes throughout ($d_z{=}0.81$--$1.15$; all $p < 10^{-29}$; Table~\\ref{tab:llama-cross-arch}).\n\nA key architectural difference emerges in strategy specificity. On LLaMA, random eviction also exhibits significant phase gradients ($\\Delta{=}0.025$--$0.271$; $d_z{=}0.41$--$0.46$; all $p < 10^{-12}$), unlike DeepSeek and Qwen where random is non-significant at $s \\leq 0.20$. The importance/random $\\Delta$ ratio is $2.0$--$2.6{\\times}$ on LLaMA, substantially weaker than the $15$--$17{\\times}$ observed on DeepSeek. Dose-response monotonicity holds for both strategies (all conditions monotonic). This indicates that the phase gradient itself is architecture-general, while the degree of strategy specificity is architecture-dependent, likely reflecting differences between GQA (LLaMA, 32 heads with 8 KV groups) and MHA (Qwen2, 28 heads) in how head pruning differentially disrupts importance scoring.\n\nAbsolute interaction magnitudes are approximately $7$--$12{\\times}$ smaller than Qwen2-family models at matched sparsity, consistent with architecture-specific attention head specialization patterns. Full per-condition breakdowns appear in Appendix~\\ref{app:cross-arch}.\n\n\\subsection{Scale Analysis: Qwen2.5-14B}\n\\label{sec:scale-14b}\n\nTo assess whether phase-modulated severity persists at larger model scale within the same architecture family, we evaluate Qwen2.5-14B-Instruct on MATH-500 ($n{=}500$) at $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Median of per-problem paired severity differences ($\\Delta$) under importance-based eviction on Qwen2.5-14B-Instruct (MATH-500). \\textit{Results pending.}}\n\\label{tab:scale-14b}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nStrategy & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\\\\n\\midrule\nImportance & --- & --- & --- & --- \\\\\nRandom     & --- & --- & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%% PLACEHOLDER: Fill Table~\\ref{tab:scale-14b} when c12 experiment completes.\n%% Expected analysis: (1) whether 14B amplifies or attenuates severity relative to 7B,\n%% (2) whether strategy specificity ratio is scale-invariant,\n%% (3) comparison of phase segmentation thresholds at larger scale.\n\n\\subsection{Cross-Benchmark Validation: GSM8K}\n\\label{sec:cross-benchmark}\n\nTo assess task generalization, we evaluate both models on GSM8K ($n{=}50$) at $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$. On DeepSeek (clean data, no output truncation), importance-based eviction replicates the MATH-500 phase gradient across all four sparsity levels with a strict dose-response: $\\Delta{=}0.24$ at $s{=}0.15$ rising to $4.68$ at $s{=}0.30$ (all $p \\leq 0.0003$, Wilcoxon). Strategy specificity on GSM8K manifests as a \\emph{qualitative} gap: importance-based eviction produces significant phase gradients while random eviction is non-significant across all conditions (CIs spanning zero).\n\nWe interpret this attenuation as \\emph{reasoning depth scaling}: strategy specificity scales with reasoning chain depth. MATH-500 (complex multi-step reasoning, strategy ratio $15$--$17{\\times}$) produces stronger phase contrast than GSM8K (simpler arithmetic, ratio ${\\sim}3{\\times}$). Within MATH-500, longer traces exhibit higher strategy specificity (Spearman $\\rho > 0$, $p < 0.02$), providing continuous correlational support. This scaling relationship is predictive: tasks with deeper reasoning chains should exhibit stronger strategy${\\times}$phase interactions, because longer low-sparsity phases provide more opportunity for importance discrimination collapse to accumulate. Qwen GSM8K results are inconclusive due to generation truncation (\\texttt{max\\_new\\_tokens}${=}$2047): while directional consistency holds at $s \\geq 0.25$ ($\\Delta{=}1.14$--$4.62$; $p < 10^{-4}$), absolute values and phase assignments are unreliable because all outputs hit the token limit. Full tables in Appendix~\\ref{app:gsm8k}.\n\n\\paragraph{GSM8K accuracy under compound sparsity.}\nA power analysis on GSM8K ($n{=}50$) reveals a strategy-dependent asymmetry in downstream accuracy. Under random head removal, all 8 conditions (2 models $\\times$ 4 sparsity levels) are non-significant (max $|d|{=}0.164$). Post-hoc power analysis indicates $n{=}50$ can detect effects of $d \\geq 0.40$ ($\\alpha{=}0.05$, power${=}0.80$); all random conditions showed $|d| \\leq 0.164$, meaning the null results may reflect insufficient power rather than true absence of effect. Under importance-based pruning, Qwen exhibits a medium-sized accuracy degradation at $s \\geq 0.25$ ($d \\approx 0.63$, power ${>}\\,0.99$), consistent with the PPL-based severity gradient observed on MATH-500. DeepSeek importance conditions exhibit a qualitative downward trend in accuracy but are excluded from parametric inference due to heavy-tailed distributions that violate test assumptions.\n\n\\subsection{Cross-Benchmark Validation: GPQA Diamond}\n\\label{sec:cross-benchmark-gpqa}\n\nTo assess generalization beyond mathematical reasoning, we evaluate both models on GPQA Diamond~\\cite{rein-gpqa-2024} ($n{=}198$), a graduate-level science QA benchmark requiring multi-step reasoning across physics, chemistry, and biology.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Median of per-problem paired severity differences ($\\Delta$) under importance-based eviction on GPQA Diamond. \\textit{Results pending.}}\n\\label{tab:gpqa-results}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nModel & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\\\\n\\midrule\nDeepSeek-R1-Distill-Qwen-7B & --- & --- & --- & --- \\\\\nQwen2.5-7B-Instruct         & --- & --- & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%% PLACEHOLDER: Fill Table~\\ref{tab:gpqa-results} when c11 experiment completes.\n%% Expected analysis: (1) phase gradient direction consistency with MATH-500/GSM8K,\n%% (2) strategy specificity comparison across task types (math vs. science reasoning),\n%% (3) whether cognitive load modulation hypothesis extends to non-mathematical domains.\n\n\\subsection{Statistical Validation}\n\\label{sec:stat-validation}\n\nTable~\\ref{tab:cohens-d} reports the paired median difference $\\Delta$ under importance-based eviction for both models at $n{=}496$/$475$. All eight conditions yield CIs excluding zero; within-importance dose-response $d_z$ (s015 vs.\\ s030) is $0.94$ (DeepSeek) and $0.92$ (Qwen), both large effects. Importance-based eviction produces significantly larger phase gradients than random at all four sparsity levels ($p_{\\text{Bonf}} \\ll 10^{-10}$, Wilcoxon; permutation tests in Appendix~\\ref{app:permutation-details}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Median of paired differences ($\\Delta_i = \\mathrm{II}^{(i)}_{\\textit{low}} - \\mathrm{II}^{(i)}_{\\textit{high}}$) under importance-based eviction with bootstrap 95\\% CIs ($B{=}10{,}000$).}\n\\label{tab:cohens-d}\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n$s$ & DS ($n{=}496$): $\\widetilde{\\Delta}$\\; [95\\% CI] & QW ($n{=}475$): $\\widetilde{\\Delta}$\\; [95\\% CI] \\\\\n\\midrule\n0.15 & $0.39$\\; $[0.35,\\; 0.44]$ & $0.07$\\; $[0.05,\\; 0.09]$ \\\\\n0.20 & $1.21$\\; $[1.11,\\; 1.34]$ & $0.31$\\; $[0.26,\\; 0.36]$ \\\\\n0.25 & $3.99$\\; $[3.53,\\; 4.36]$ & $1.07$\\; $[0.98,\\; 1.18]$ \\\\\n0.30 & $8.48$\\; $[7.75,\\; 9.69]$ & $3.16$\\; $[2.78,\\; 3.56]$ \\\\\n\\bottomrule\n\\multicolumn{3}{@{}l}{\\footnotesize All $p_{\\text{Bonf}} < 10^{-13}$. Within-importance $d_z$ (s015 vs.\\ s030): DS $0.94$, QW $0.92$.}\n\\end{tabular}\n\\end{table}\n\n\\subsection{Answer-Region Analysis}\n\\label{sec:answer-region}\n\nAcross both models, 93.2\\% of answer tokens (\\verb|\\boxed{}| markers) fall within the high-sparsity phase, where compound interaction is minimal. This non-uniformity identifies \\emph{where} severity concentrates: reasoning-trace tokens show $5.7$--$43.5{\\times}$ PPL degradation vs.\\ $1.3$--$5.3{\\times}$ for answer tokens (Wilcoxon $p < 0.001$). However, reasoning-trace degradation may produce \\emph{silent reasoning errors}---correct formatting with corrupted intermediate logic \\cite{lanham-2023-faithfulness, turpin-2023-biased-cot}---a failure mode that PPL detects but answer-level accuracy may miss.\n\n\\subsection{Downstream Accuracy Validation}\n\\label{sec:accuracy-validation}\n\nTo validate that the PPL-based severity gradient translates to downstream task performance, we evaluate MATH-500 accuracy under compound sparsity (importance-based eviction, \\texttt{max\\_new\\_tokens}${=}$8192; Table~\\ref{tab:accuracy}). Qwen's minimal truncation ($\\leq 4\\%$) provides a clean PPL-accuracy bridge.\nQwen ($n{=}100$; truncation $\\leq 4\\%$) shows gradual decline from $46\\%$ (dense) through $s{=}0.25$ ($\\delta{=}-4$ to $-13$\\,pp) with a sharp cliff at $s{=}0.30$ ($19\\%$, $\\delta{=}-27$\\,pp). DeepSeek ($n{=}50$) degrades more steeply ($74\\% \\to 4\\%$) with a dual-regime structure: at $s \\leq 0.20$, degradation is primarily truncation-driven (non-truncated accuracy remains $68$--$71\\%$ at $s{=}0.15$--$0.20$ vs.\\ $88\\%$ dense); at $s \\geq 0.25$, both truncation and reasoning quality collapse simultaneously (Appendix~\\ref{app:accuracy-details}).\nThe two models exhibit distinct failure modes reflecting training-paradigm dependence: DeepSeek failures are \\emph{truncation-dominated} (truncation $16\\% \\to 76\\%$), while Qwen failures are \\emph{wrong-answer-dominated} (truncation $\\leq 4\\%$, reasoning quality degrades directly). Given minimal truncation, Qwen accuracy data provide a reliable PPL-accuracy bridge; DeepSeek accuracy results, confounded by truncation rates of $16\\%$--$76\\%$, should be interpreted as qualitative observations only.\n\nWe provide a correlational mechanistic analysis in terms of importance discrimination collapse in \\S\\ref{sec:analysis}.\n",
    "structuredPatch": [
      {
        "oldStart": 85,
        "oldLines": 7,
        "newStart": 85,
        "newLines": 7,
        "lines": [
          " \\label{sec:cross-model}",
          " ",
          " DeepSeek-R1-Distill-Qwen-7B (distillation-trained) and Qwen2.5-7B-Instruct (instruction-tuned) share the Qwen2 backbone but differ in training objective, providing a within-architecture-family comparison across training paradigms.",
          "-Qwen2.5-7B-Instruct ($n_{\\text{eff}}{=}475$) reproduces the monotonic severity gradient: $\\Delta$ increases from $0.07$ at $s{=}0.15$ to $3.16$ at $s{=}0.30$ (all Bonferroni-corrected $p < 10^{-14}$), paralleling DeepSeek at approximately one-quarter to one-sixth the magnitude. Both models yield strictly increasing median $\\Delta$ trajectories (Jonckheere-Terpstra $z \\geq 6.2$, $p < 10^{-9}$; see \\S\\ref{par:stats}). Random eviction on Qwen mirrors DeepSeek: non-significant at $s \\leq 0.20$, becoming significant at $s \\geq 0.25$ ($\\Delta{=}0.39$--$0.91$; $p_{\\text{Bonf}} < 10^{-10}$) but $2.7$--$20{\\times}$ weaker than importance-based. A caveat: 45.2\\% of Qwen problems yield null mid-phase segments due to low temporal autocorrelation ($r{=}0.718$ vs.\\ $0.894$); this does not affect $\\Delta$ (Appendix~\\ref{app:qwen-null-rate}). Full tables in Appendix~\\ref{app:cross-model-details}.",
          "+Qwen2.5-7B-Instruct ($n_{\\text{eff}}{=}475$) reproduces the monotonic severity gradient: $\\Delta$ increases from $0.07$ at $s{=}0.15$ to $3.16$ at $s{=}0.30$ (all Bonferroni-corrected $p < 10^{-14}$), paralleling DeepSeek at approximately one-quarter to one-sixth the magnitude. Both models yield strictly increasing median $\\Delta$ trajectories (Jonckheere-Terpstra $z \\geq 6.2$, $p < 10^{-9}$; see \\S\\ref{par:stats}). Random eviction on Qwen mirrors DeepSeek: non-significant at $s \\leq 0.20$, becoming significant at $s \\geq 0.25$ ($\\Delta{=}0.39$--$0.91$; $p_{\\text{Bonf}} < 10^{-10}$) but $2.7$--$3.5{\\times}$ weaker than importance-based. A caveat: 45.2\\% of Qwen problems yield null mid-phase segments due to low temporal autocorrelation ($r{=}0.718$ vs.\\ $0.894$); this does not affect $\\Delta$ (Appendix~\\ref{app:qwen-null-rate}). Full tables in Appendix~\\ref{app:cross-model-details}.",
          " ",
          " \\subsection{Cross-Architecture Validation}",
          " \\label{sec:cross-arch}"
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

### Tool call

_source line 45_

<details open><summary>🔧 Tool call — Edit · `toolu_01MufogSULJKiNtuYHRV2L4j`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex",
  "old_string": "These effects are genuine but $2.7$--$20{\\times}$ weaker than importance-based eviction at the same sparsity levels",
  "new_string": "These effects are genuine but $2.7$--$17{\\times}$ weaker than importance-based eviction at the same sparsity levels"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7c8d5505-1cf3-4db2-81a6-3ef2a3c9c146",
  "uuid": "eb922294-f6f9-4593-9e29-c9b5a20fa8b8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xy4HWiPkXNhCw9zi8q61vJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1266,
      "cache_read_input_tokens": 38614,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1266
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

_source line 46 · 2026-05-16T22:52:38.896Z_

<details><summary>↩ Tool result · `toolu_01MufogSULJKiNtuYHRV2L4j`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7c8d5505-1cf3-4db2-81a6-3ef2a3c9c146",
  "uuid": "211f44c6-754f-4988-b093-3dad332c976e",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex",
    "oldString": "These effects are genuine but $2.7$--$20{\\times}$ weaker than importance-based eviction at the same sparsity levels",
    "newString": "These effects are genuine but $2.7$--$17{\\times}$ weaker than importance-based eviction at the same sparsity levels",
    "originalFile": "\\section{Importance Discrimination Collapse Details}\n\\label{app:discrimination-collapse-details}\n\nThis cross-model consistency (Table~\\ref{tab:discrimination-metrics-full}) supports importance discrimination collapse as a robust consequence of compound sparsity. When importance scores lose discriminative power, thresholding the bottom-$s$ fraction becomes noise-sensitive: small perturbations change which positions cross the eviction boundary. In the limit of perfectly uniform scores, importance-based eviction degenerates into an arbitrary selection functionally equivalent to biased random eviction. The same pattern holds under random eviction (DeepSeek: $-0.031$ to $-0.071$; Qwen: $-0.019$ to $-0.046$), indicating that importance discrimination collapse is a consequence of head pruning \\emph{per se}, not of the eviction strategy.\n\n\n\\section{Extended Discussion}\n\\label{app:extended-discussion}\n\n\\paragraph{On the predictability of phase-modulated severity.}\nThe compound interaction is not uniformly fragile---it is selectively fragile in a phase-dependent manner ($\\widetilde{\\mathrm{II}}_{\\text{high}} < 0.06$ at $s \\leq 0.30$).\n\n\\paragraph{Random masking as falsification control.}\nAt $n{=}500$, random eviction develops a detectable but weak phase gradient above $s \\approx 0.20$: non-significant at $s \\leq 0.20$ for both models, but significant at $s \\geq 0.25$ (DS: $\\Delta{=}0.26$--$0.51$, $p_{\\text{Bonf}} < 0.006$; QW: $\\Delta{=}0.39$--$0.91$, $p_{\\text{Bonf}} < 10^{-10}$). Where significant, the random phase gradient is $2.7$--$17{\\times}$ weaker than importance-based (restricted to conditions where both strategies are significant, $s \\geq 0.25$), supporting that the dominant amplification is strategy-specific.\n\n\\paragraph{Entropy mechanism boundary conditions.}\nDirectly measuring per-head entropy shifts across architecturally distinct models---and identifying what training-time properties determine whether entropy concentrates or disperses under head pruning---would clarify the boundary conditions of the full mechanism.\n\n\n\\section{Pilot Mitigation Experiment}\n\\label{app:pilot-mitigation}\n\nWe explored oracle phase-aware budget reallocation, shifting sparsity budget from high-severity low-sparsity phases to low-severity high-sparsity phases ($n{=}30$ problems at $s{=}0.25$). Oracle recovery---the fraction of compound interaction eliminated by phase-aware allocation---reached 18\\% (95\\% CI: $[-39\\%, 45.8\\%]$; Wilcoxon $p = 0.002$), below the pre-registered 30\\% gate for claiming practical mitigation. A heuristic variant achieved 32\\% recovery (95\\% CI: $[-22.8\\%, 66\\%]$; $p = 0.024$). \\textbf{Critically, 95\\% bootstrap CIs for both conditions span zero}, meaning neither recovery estimate is statistically distinguishable from no improvement. \\textbf{Gate status: FAIL}---neither oracle nor heuristic recovery meets the pre-registered threshold, and neither is statistically distinguishable from zero improvement. These results indicate that phase-aware budget reallocation alone is insufficient to neutralize the severity gradient; effective mitigation likely requires joint optimization of budget allocation and eviction strategy selection across phases.\n\n\n\\section{Extended Limitations}\n\\label{app:limitations}\n\n\\paragraph{Model scale.}\nAll experiments are conducted at the 7B parameter scale.\nWhether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested.\nLarger models may exhibit different attention redundancy structures that alter the importance discrimination collapse dynamics (and the model-dependent entropy component may behave differently at scale).\n\n\n\\paragraph{Architectural scope.}\nOur two models---DeepSeek-R1-Distill-Qwen-7B and Qwen2.5-7B-Instruct---share the Qwen2ForCausalLM architecture.\nThe cross-training-paradigm replication (\\S\\ref{sec:cross-model}) suggests that the findings are not artifacts of a single model's weights, though both models share the same Qwen2ForCausalLM architecture.\nCross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, $n{=}250$, \\S\\ref{sec:cross-arch}, Appendix~\\ref{app:cross-arch}) confirms qualitatively consistent within-importance phase gradients ($d_z{=}0.81$--$1.15$; all $p < 10^{-29}$) but a substantially weaker strategy${\\times}$phase interaction than in Qwen2-based architectures: random eviction also exhibits significant phase gradients on LLaMA ($d_z{=}0.41$--$0.46$; all $p < 10^{-12}$), reducing the importance/random ratio to $2.0$--$2.6{\\times}$ (vs.\\ $15$--$17{\\times}$ on DeepSeek). The phase gradient direction and dose-response monotonicity are architecture-general; quantitative strategy specificity is architecture-dependent. Comprehensive cross-architecture validation across more diverse designs (e.g., Mistral, multi-latent attention architectures) and scales remains an important next step.\n\n\n\\paragraph{Task coverage.}\nWe evaluate exclusively on MATH-500, a mathematical reasoning benchmark.\nDifferent reasoning tasks---code generation, commonsense reasoning, multi-hop question answering---may induce different phase structures with different sparsity distributions, potentially altering the severity gradient profile.\nGeneralizing the phase-strategy interaction to broader reasoning domains is an important next step.\n\n\n\\paragraph{Statistical scope.}\nBootstrap confidence intervals use $B{=}10{,}000$ resamples (seed$=$42). The primary analysis uses $n{=}496$ paired problems for DeepSeek (4 excluded) and $n{=}475$ for Qwen (25 excluded); the permutation test (Table~\\ref{tab:permutation}) uses $n{=}49$ from an initial profiling subset.\nThe severity difference distribution is right-skewed (mean/median ratios up to $43{:}1$), motivating our use of medians and nonparametric tests rather than parametric alternatives.\nAll four profiling-subset permutation tests reject $H_0$ after Bonferroni correction ($p_{\\text{Bonf}} < 0.005$; Table~\\ref{tab:permutation}), with CI lower bounds increasing from $0.19$ to $6.70$---supporting the effect direction at every sparsity level. At $n{=}496$, Wilcoxon signed-rank tests support all conditions with $p_{\\text{Bonf}} < 10^{-13}$ (Table~\\ref{tab:cohens-d}). The permutation CIs at higher sparsity are wider (e.g., $[6.70,\\; 16.29]$ at $s{=}0.30$), reflecting genuine variance in per-problem severity amplification.\n\nAt $n{=}500$, random eviction on both models becomes significant at $s \\geq 0.25$ (Qwen: $\\Delta{=}0.39$, $p_{\\text{Bonf}} < 10^{-10}$ at $s{=}0.25$; $\\Delta{=}0.91$, $p_{\\text{Bonf}} < 10^{-13}$ at $s{=}0.30$; bootstrap CIs exclude zero).\nThese effects are genuine but $2.7$--$20{\\times}$ weaker than importance-based eviction at the same sparsity levels, consistent with a weak phase gradient that is detectable at sufficient sample size but not the primary driver of compound severity.\n\n\\paragraph{Sparsity range.}\nOur primary analysis spans $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$; pilot data at $s{=}0.10$ and $s{=}0.35$ exist (6 total sparsity levels) but are not included in the main analysis due to limited sample size at these boundary conditions. Monotonicity is established at the tested sparsity levels (JT test $p \\ll 10^{-10}$); the functional form of $G(s)$ between and beyond these levels is not characterized.\nMore extreme sparsity ($s > 0.50$) may exhibit qualitatively different interaction dynamics---the sub-exponential growth pattern suggests the severity gradient may plateau, but this remains unverified.\n\n\n\\paragraph{No throughput evaluation.}\nWe do not report inference throughput or latency, which are necessary for deployment analysis but orthogonal to our severity characterization.\n\n\n\n\\section{Cross-Benchmark Validation: GSM8K}\n\\label{app:gsm8k}\n\nTables~\\ref{tab:gsm8k-ds} and \\ref{tab:gsm8k-qw} report the per-phase II breakdown on GSM8K ($n{=}50$) for DeepSeek and Qwen, respectively. All statistics use medians, Wilcoxon signed-rank tests, and bootstrap median CIs ($B{=}10{,}000$), matching the MATH-500 methodology. DeepSeek importance-based eviction replicates the MATH-500 phase gradient across all four sparsity levels (all $p \\leq 0.0003$) with a strict dose-response ($\\Delta$: $0.24 \\to 4.68$). Qwen importance-based eviction is significant at $s \\geq 0.25$ ($p < 10^{-4}$). Random eviction is non-significant across all conditions for both models; Qwen random $s{=}0.30$ is excluded due to data quality concerns (output truncation producing extreme II values).\n\n\\paragraph{Power analysis for random conditions.}\nPost-hoc power analysis indicates that at $n{=}50$, the minimum detectable effect size is $d \\geq 0.40$ ($\\alpha{=}0.05$, power${=}0.80$). All 8 random conditions (2 models $\\times$ 4 sparsity levels) show $|d| \\leq 0.164$, well below the detectability threshold; their non-significance should therefore be interpreted as absence of evidence rather than evidence of absence. By contrast, Qwen importance-based eviction at $s \\geq 0.25$ is adequately powered ($d \\approx 0.63$, power ${>}\\,0.99$), indicating that the observed significance reflects a genuine effect.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Per-phase interaction index on GSM8K: DeepSeek-R1-Distill-Qwen-7B ($n{=}50$). $\\Delta$: paired median difference ($\\widetilde{\\mathrm{II}}_{\\textit{low}} - \\widetilde{\\mathrm{II}}_{\\textit{high}}$) with bootstrap 95\\% CI ($B{=}10{,}000$, median statistic). $p$: Wilcoxon signed-rank, Bonferroni-corrected ($k{=}4$).}\n\\label{tab:gsm8k-ds}\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\n$s$ & Strategy & $\\widetilde{\\mathrm{II}}_{\\textit{high}}$ & $\\widetilde{\\mathrm{II}}_{\\textit{low}}$ & $\\Delta$\\; [95\\% CI] & $p_{\\text{Bonf}}$ \\\\\n\\midrule\n0.15 & Importance & $-$0.001 & 0.241 & 0.24\\; $[0.08,\\; 0.48]$ & 0.0003 \\\\\n0.15 & Random     & 0.036 & 0.105 & $-$0.04\\textsuperscript{ns} & 0.90 \\\\\n\\addlinespace\n0.20 & Importance & $-$0.002 & 0.740 & 0.74\\; $[0.31,\\; 1.12]$ & ${<}\\,10^{-4}$ \\\\\n0.20 & Random     & 0.143 & 0.423 & 0.28\\textsuperscript{ns} & 0.96 \\\\\n\\addlinespace\n0.25 & Importance & 0.009 & 1.992 & 1.99\\; $[0.93,\\; 2.82]$ & ${<}\\,10^{-4}$ \\\\\n0.25 & Random     & 0.619 & 1.603 & 0.98\\textsuperscript{ns} & 0.83 \\\\\n\\addlinespace\n0.30 & Importance & 0.024 & 4.682 & 4.68\\; $[2.12,\\; 10.56]$ & ${<}\\,10^{-4}$ \\\\\n0.30 & Random     & 1.837 & 4.683 & 2.85\\textsuperscript{ns} & 0.54 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Per-phase interaction index on GSM8K: Qwen2.5-7B-Instruct ($n{=}50$). Outputs truncated at \\texttt{max\\_new\\_tokens}${=}$2047; absolute values should be interpreted with this limitation. $^{\\ddagger}$Excluded: extreme II values from truncation artifacts render this condition invalid.}\n\\label{tab:gsm8k-qw}\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\n$s$ & Strategy & $\\widetilde{\\mathrm{II}}_{\\textit{high}}$ & $\\widetilde{\\mathrm{II}}_{\\textit{low}}$ & $\\Delta$\\; [95\\% CI] & $p_{\\text{Bonf}}$ \\\\\n\\midrule\n0.15 & Importance & 0.000 & 0.029 & 0.03\\textsuperscript{ns} & 0.39 \\\\\n0.15 & Random     & 0.089 & 0.033 & $-$1.58\\textsuperscript{ns} & 0.69 \\\\\n\\addlinespace\n0.20 & Importance & 0.004 & 0.180 & 0.09\\textsuperscript{ns} & 0.62 \\\\\n0.20 & Random     & 0.201 & 0.356 & 4.88\\textsuperscript{ns} & 0.57 \\\\\n\\addlinespace\n0.25 & Importance & 0.009 & 1.064 & 1.14\\; $[0.62,\\; 1.66]$ & ${<}\\,10^{-4}$ \\\\\n0.25 & Random     & 0.802 & 1.213 & 11.1\\textsuperscript{ns} & 0.39 \\\\\n\\addlinespace\n0.30 & Importance & 0.023 & 2.140 & 4.62\\; $[2.88,\\; 6.92]$ & ${<}\\,10^{-4}$ \\\\\n0.30 & Random$^{\\ddagger}$     & \\multicolumn{4}{c}{\\textit{excluded (data quality)}} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\n\\section{Downstream Accuracy Validation Details}\n\\label{app:accuracy-details}\n\nTable~\\ref{tab:accuracy} reports MATH-500 accuracy under compound sparsity (importance-based eviction) at $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$ with \\texttt{max\\_new\\_tokens}${=}$8192, complementing the PPL-based analysis in \\S\\ref{sec:accuracy-validation}. Qwen ($n{=}100$; truncation $\\leq 4\\%$ across all conditions) provides the cleanest dose-response evidence: accuracy declines gradually from $46\\%$ (dense) through $s{=}0.25$ ($\\delta{=}-4$ to $-13$\\,pp) before a sharp cliff at $s{=}0.30$ ($19\\%$, $\\delta{=}-27$\\,pp). DeepSeek ($n{=}50$) shows steeper overall degradation ($74\\% \\to 4\\%$), confounded by rising truncation ($16\\% \\to 76\\%$); non-truncated analysis (\\S\\ref{app:accuracy-nt}) reveals a dual-regime structure.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{MATH-500 accuracy under compound sparsity (importance-based eviction, \\texttt{max\\_new\\_tokens}${=}$8192). $\\delta$: accuracy change vs.\\ dense. Trunc: truncation rate under sparse condition. DS: $n{=}50$ (dense truncation $16\\%$); QW: $n{=}100$ (truncation $\\leq 4\\%$ all conditions).}\n\\label{tab:accuracy}\n\\begin{tabular}{@{}lccccc@{}}\n\\toprule\nModel & $s$ & Dense & Sparse & $\\delta$ & Trunc \\\\\n\\midrule\nDS & 0.15 & 74\\% & 48\\% & $-$26\\,pp & 32\\% \\\\\nDS & 0.20 & 74\\% & 30\\% & $-$44\\,pp & 56\\% \\\\\nDS & 0.25 & 74\\% & 8\\% & $-$66\\,pp & 76\\% \\\\\nDS & 0.30 & 74\\% & 4\\% & $-$70\\,pp & 76\\% \\\\\n\\addlinespace\nQW & 0.15 & 46\\% & 42\\% & $-$4\\,pp & $\\leq$4\\% \\\\\nQW & 0.20 & 46\\% & 36\\% & $-$10\\,pp & $\\leq$4\\% \\\\\nQW & 0.25 & 46\\% & 33\\% & $-$13\\,pp & $\\leq$4\\% \\\\\nQW & 0.30 & 46\\% & 19\\% & $-$27\\,pp & $\\leq$4\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Failure mode divergence.}\nDeepSeek and Qwen exhibit qualitatively distinct failure modes under compound sparsity. DeepSeek failures are \\emph{truncation-dominated}: compound sparsity is associated with verbose, repetitive chain-of-thought that exceeds the token limit (truncation rises from $16\\%$ at dense to $32\\%$ at $s{=}0.15$ and $76\\%$ at $s{=}0.30$, even with \\texttt{max\\_new\\_tokens}${=}$8192). Qwen failures are \\emph{wrong-answer-dominated}: outputs complete within the token limit (truncation $\\leq 4\\%$) but produce incorrect answers, indicating that compound sparsity disrupts reasoning quality directly. This divergence likely reflects training-paradigm differences: DeepSeek's distillation from DeepSeek-R1 produces extended CoT traces susceptible to truncation under degraded conditions.\n\n\\paragraph{Language switching under high sparsity.}\nDeepSeek problems exhibit language switching to Chinese mid-generation at the following observed rates: 0\\% at dense, 4\\% at $s{=}0.15$, and 40\\% at $s{=}0.30$ (intermediate sparsity levels not yet measured).\\footnote{Language switching rates were detected from \\texttt{gen\\_snippet} fields in 2048-token evaluations, not from the independent 8192-token generations used in Table~\\ref{tab:accuracy}. Rates under the 8192-token budget were not re-measured.} This qualitative pathology---absent in Qwen---is a \\emph{symptom} of compound-sparsity-induced degradation rather than a cause of accuracy loss: at $s{=}0.30$, Chinese-language and English-language outputs achieve comparable accuracy ($\\sim$10\\%), indicating that the accuracy decline reflects pruning-induced reasoning corruption regardless of output language. The switching pattern is consistent with the model's Chinese-language pretraining corpus surfacing under degraded attention in distillation-trained models.\n\n\n\\section{Non-Truncated Sensitivity Analysis}\n\\label{app:accuracy-nt}\n\nWith \\texttt{max\\_new\\_tokens}${=}$8192, Qwen truncation remains $\\leq 4\\%$ across all sparsity levels, so the full-sample accuracy decline ($\\delta{=}-4$ to $-27$\\,pp; Table~\\ref{tab:accuracy}) reflects pure reasoning quality degradation without truncation confound.\n\nDeepSeek exhibits substantial truncation ($16\\%$ at dense to $76\\%$ at $s{=}0.25$--$0.30$). Restricting to non-truncated outputs reveals a \\emph{dual-regime} structure. At $s \\leq 0.20$, non-truncated accuracy remains $68$--$71\\%$ (vs.\\ $88\\%$ dense; $n_{\\text{NT}}{=}34$ at $s{=}0.15$, $n_{\\text{NT}}{=}22$ at $s{=}0.20$), while full-sample accuracy drops to $30$--$48\\%$---indicating that degradation at low sparsity is primarily truncation-driven rather than reflecting reasoning quality loss. At $s \\geq 0.25$, non-truncated accuracy itself collapses: $33\\%$ at $s{=}0.25$ and $17\\%$ at $s{=}0.30$ ($n_{\\text{NT}}{=}12$ for both; reported as reference values given small samples), showing that high-dose compound sparsity degrades both generation length \\emph{and} reasoning quality simultaneously. The NT accuracy cliff from $68\\%$ ($s{=}0.20$) to $33\\%$ ($s{=}0.25$) localizes the transition between truncation-driven and dual-collapse regimes.\n\nThis dual-regime structure complements the importance discrimination collapse analysis (\\S\\ref{sec:analysis}): at low sparsity, compound interaction primarily manifests as increased verbosity (degraded attention produces repetitive CoT); at high sparsity, the interaction additionally corrupts reasoning-critical computations.\n",
    "structuredPatch": [
      {
        "oldStart": 50,
        "oldLines": 7,
        "newStart": 50,
        "newLines": 7,
        "lines": [
          " All four profiling-subset permutation tests reject $H_0$ after Bonferroni correction ($p_{\\text{Bonf}} < 0.005$; Table~\\ref{tab:permutation}), with CI lower bounds increasing from $0.19$ to $6.70$---supporting the effect direction at every sparsity level. At $n{=}496$, Wilcoxon signed-rank tests support all conditions with $p_{\\text{Bonf}} < 10^{-13}$ (Table~\\ref{tab:cohens-d}). The permutation CIs at higher sparsity are wider (e.g., $[6.70,\\; 16.29]$ at $s{=}0.30$), reflecting genuine variance in per-problem severity amplification.",
          " ",
          " At $n{=}500$, random eviction on both models becomes significant at $s \\geq 0.25$ (Qwen: $\\Delta{=}0.39$, $p_{\\text{Bonf}} < 10^{-10}$ at $s{=}0.25$; $\\Delta{=}0.91$, $p_{\\text{Bonf}} < 10^{-13}$ at $s{=}0.30$; bootstrap CIs exclude zero).",
          "-These effects are genuine but $2.7$--$20{\\times}$ weaker than importance-based eviction at the same sparsity levels, consistent with a weak phase gradient that is detectable at sufficient sample size but not the primary driver of compound severity.",
          "+These effects are genuine but $2.7$--$17{\\times}$ weaker than importance-based eviction at the same sparsity levels, consistent with a weak phase gradient that is detectable at sufficient sample size but not the primary driver of compound severity.",
          " ",
          " \\paragraph{Sparsity range.}",
          " Our primary analysis spans $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$; pilot data at $s{=}0.10$ and $s{=}0.35$ exist (6 total sparsity levels) but are not included in the main analysis due to limited sample size at these boundary conditions. Monotonicity is established at the tested sparsity levels (JT test $p \\ll 10^{-10}$); the functional form of $G(s)$ between and beyond these levels is not characterized."
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

### Tool call

_source line 47_

<details open><summary>🔧 Tool call — Edit · `toolu_01TY4bqhUaFxb6YBBA6B5xTE`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex",
  "old_string": "(DeepSeek, $n{=}500$;",
  "new_string": "(DeepSeek, $n{=}496$;"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7c8d5505-1cf3-4db2-81a6-3ef2a3c9c146",
  "uuid": "77b93ca3-2d12-4176-a216-925ba1b2872d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xy4HWiPkXNhCw9zi8q61vJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1266,
      "cache_read_input_tokens": 38614,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1266
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

_source line 48 · 2026-05-16T22:52:40.310Z_

<details><summary>↩ Tool result · `toolu_01TY4bqhUaFxb6YBBA6B5xTE`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7c8d5505-1cf3-4db2-81a6-3ef2a3c9c146",
  "uuid": "a9bcba86-95d5-4934-a64a-3c071067a355",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex",
    "oldString": "(DeepSeek, $n{=}500$;",
    "newString": "(DeepSeek, $n{=}496$;",
    "originalFile": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe showed that compound sparsity severity is not phase-invariant but exhibits an emergent phase-strategy interaction. Under importance-based eviction, the paired median difference $\\Delta$ increases from $0.39$ to $8.48$ (DeepSeek, $n{=}500$; Spearman $\\rho{=}1.0$) and $0.07$ to $3.16$ (Qwen, $n{=}475$), all $p < 10^{-13}$. Random eviction is $2.7$--$17{\\times}$ weaker where both strategies are significant ($s \\geq 0.25$; DeepSeek $15$--$17{\\times}$, Qwen $2.7$--$3.5{\\times}$). The importance phase gradient replicates on LlamaForCausalLM ($d_z{=}0.81$--$1.15$, $n{=}250$, all $p < 10^{-29}$), supporting architecture-generality of phase modulation, while strategy specificity is architecture-dependent ($2.0$--$2.6{\\times}$ on LLaMA vs.\\ $15$--$17{\\times}$ on DeepSeek). A model-dependent crossover on DeepSeek demonstrates that no single strategy dominates uniformly. Per-phase Gini analysis reveals importance discrimination collapse as a correlational diagnostic: despite near-identical aggregate Gini drops, severity diverges by $2.7$--$17{\\times}$, implicating the structural specificity of importance-based pruning.\nBeyond the empirical findings, the phase-gated analysis framework itself---decomposing compound severity by reasoning phase and eviction strategy---transforms a scalar interaction metric into a structured diagnostic that reveals where compound sparsity fails and why. This framework provides practitioners with a principled basis for phase-aware sparsity allocation: applying aggressive compression during high-sparsity (structured computation) phases while preserving budget during low-sparsity (exploratory reasoning) phases. Future work could explore generalization to other reasoning domains, causal validation of importance discrimination collapse, and systematic characterization of asymmetric compound interactions.\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 5,
        "newStart": 1,
        "newLines": 5,
        "lines": [
          " \\section{Conclusion}",
          " \\label{sec:conclusion}",
          " ",
          "-We showed that compound sparsity severity is not phase-invariant but exhibits an emergent phase-strategy interaction. Under importance-based eviction, the paired median difference $\\Delta$ increases from $0.39$ to $8.48$ (DeepSeek, $n{=}500$; Spearman $\\rho{=}1.0$) and $0.07$ to $3.16$ (Qwen, $n{=}475$), all $p < 10^{-13}$. Random eviction is $2.7$--$17{\\times}$ weaker where both strategies are significant ($s \\geq 0.25$; DeepSeek $15$--$17{\\times}$, Qwen $2.7$--$3.5{\\times}$). The importance phase gradient replicates on LlamaForCausalLM ($d_z{=}0.81$--$1.15$, $n{=}250$, all $p < 10^{-29}$), supporting architecture-generality of phase modulation, while strategy specificity is architecture-dependent ($2.0$--$2.6{\\times}$ on LLaMA vs.\\ $15$--$17{\\times}$ on DeepSeek). A model-dependent crossover on DeepSeek demonstrates that no single strategy dominates uniformly. Per-phase Gini analysis reveals importance discrimination collapse as a correlational diagnostic: despite near-identical aggregate Gini drops, severity diverges by $2.7$--$17{\\times}$, implicating the structural specificity of importance-based pruning.",
          "+We showed that compound sparsity severity is not phase-invariant but exhibits an emergent phase-strategy interaction. Under importance-based eviction, the paired median difference $\\Delta$ increases from $0.39$ to $8.48$ (DeepSeek, $n{=}496$; Spearman $\\rho{=}1.0$) and $0.07$ to $3.16$ (Qwen, $n{=}475$), all $p < 10^{-13}$. Random eviction is $2.7$--$17{\\times}$ weaker where both strategies are significant ($s \\geq 0.25$; DeepSeek $15$--$17{\\times}$, Qwen $2.7$--$3.5{\\times}$). The importance phase gradient replicates on LlamaForCausalLM ($d_z{=}0.81$--$1.15$, $n{=}250$, all $p < 10^{-29}$), supporting architecture-generality of phase modulation, while strategy specificity is architecture-dependent ($2.0$--$2.6{\\times}$ on LLaMA vs.\\ $15$--$17{\\times}$ on DeepSeek). A model-dependent crossover on DeepSeek demonstrates that no single strategy dominates uniformly. Per-phase Gini analysis reveals importance discrimination collapse as a correlational diagnostic: despite near-identical aggregate Gini drops, severity diverges by $2.7$--$17{\\times}$, implicating the structural specificity of importance-based pruning.",
          " Beyond the empirical findings, the phase-gated analysis framework itself---decomposing compound severity by reasoning phase and eviction strategy---transforms a scalar interaction metric into a structured diagnostic that reveals where compound sparsity fails and why. This framework provides practitioners with a principled basis for phase-aware sparsity allocation: applying aggressive compression during high-sparsity (structured computation) phases while preserving budget during low-sparsity (exploratory reasoning) phases. Future work could explore generalization to other reasoning domains, causal validation of importance discrimination collapse, and systematic characterization of asymmetric compound interactions."
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

### Tool call

_source line 49_

<details open><summary>🔧 Tool call — Edit · `toolu_019daV2WDGukGASnCuPd4pmR`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex",
  "old_string": "MATH-500 ($15$--$17{\\times}$) $>$ GSM8K (${\\sim}3{\\times}$)",
  "new_string": "MATH-500 ($15$--$17{\\times}$) $>$ GSM8K (${\\sim}2{\\times}$ point-estimate ratio; random non-significant at $n{=}50$)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7c8d5505-1cf3-4db2-81a6-3ef2a3c9c146",
  "uuid": "3ed0fc09-f8b6-4034-9346-cb3711279402",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xy4HWiPkXNhCw9zi8q61vJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1266,
      "cache_read_input_tokens": 38614,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1266
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

_source line 50 · 2026-05-16T22:52:41.593Z_

<details><summary>↩ Tool result · `toolu_019daV2WDGukGASnCuPd4pmR`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7c8d5505-1cf3-4db2-81a6-3ef2a3c9c146",
  "uuid": "f844eeae-bc3c-481c-a55b-588b2cfcc0a1",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex",
    "oldString": "MATH-500 ($15$--$17{\\times}$) $>$ GSM8K (${\\sim}3{\\times}$)",
    "newString": "MATH-500 ($15$--$17{\\times}$) $>$ GSM8K (${\\sim}2{\\times}$ point-estimate ratio; random non-significant at $n{=}50$)",
    "originalFile": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Implications for deployment.}\nA uniform compression budget implicitly accepts order-of-magnitude severity penalties during low-sparsity reasoning phases. Pilot evaluation ($n{=}30$, $s{=}0.25$; Appendix~\\ref{app:pilot-mitigation}) achieved 18\\% oracle recovery (95\\% CI: $[-39\\%, 45.8\\%]$), falling below the pre-registered 30\\% gate; the CI spans zero, indicating no statistically distinguishable improvement. Effective phase-aware allocation likely requires finer phase boundary estimation than current proxies provide. Additional mechanisms (e.g., strategy switching, adaptive thresholding) warrant investigation. We hypothesize that phase-modulated severity may extend to alternative attention-mass-based scoring methods (H$_2$O \\cite{h2o-neurips2023}, SnapKV \\cite{snapkv-neurips2024}, PyramidKV \\cite{pyramidkv-colm2025}), which remains an open question for future work. Extended discussion in Appendix~\\ref{app:extended-discussion}.\n\n\\paragraph{Reasoning depth scaling.}\nStrategy specificity is not a fixed property but scales with reasoning chain depth: MATH-500 ($15$--$17{\\times}$) $>$ GSM8K (${\\sim}3{\\times}$), with within-MATH-500 correlational support (Spearman $\\rho > 0$, $p < 0.02$ between trace length and specificity). This scaling is consistent with the discrimination collapse mechanism: longer low-sparsity phases provide more tokens over which pruning-degraded importance scores accumulate errors, amplifying the gap between importance-based and random eviction. The implication is practical: as models generate longer reasoning chains (a trend driven by test-time compute scaling~\\cite{snell-2024-scaling-test-time}), the penalty for naive compound compression grows superlinearly.\n\n\\paragraph{Diagnostic framework value.}\nWhile we do not propose a new compression method, the phase-gated analysis framework has direct engineering utility: (1)~the Interaction Index can serve as a per-phase evaluation metric for assessing the phase robustness of any new compound compression scheme; (2)~the dose-response curves (Figure~\\ref{fig:hero}) provide target operating points for phase-aware controllers---e.g., maintaining $s \\leq 0.20$ during low-sparsity phases to keep $\\Delta < 1.5$; (3)~the strategy specificity finding carries a concrete engineering implication: importance-based eviction under compound sparsity requires phase-aware protection that random eviction does not, because the interaction is structurally coupled to the scoring mechanism rather than to compression magnitude alone.\n",
    "structuredPatch": [
      {
        "oldStart": 5,
        "oldLines": 7,
        "newStart": 5,
        "newLines": 7,
        "lines": [
          " A uniform compression budget implicitly accepts order-of-magnitude severity penalties during low-sparsity reasoning phases. Pilot evaluation ($n{=}30$, $s{=}0.25$; Appendix~\\ref{app:pilot-mitigation}) achieved 18\\% oracle recovery (95\\% CI: $[-39\\%, 45.8\\%]$), falling below the pre-registered 30\\% gate; the CI spans zero, indicating no statistically distinguishable improvement. Effective phase-aware allocation likely requires finer phase boundary estimation than current proxies provide. Additional mechanisms (e.g., strategy switching, adaptive thresholding) warrant investigation. We hypothesize that phase-modulated severity may extend to alternative attention-mass-based scoring methods (H$_2$O \\cite{h2o-neurips2023}, SnapKV \\cite{snapkv-neurips2024}, PyramidKV \\cite{pyramidkv-colm2025}), which remains an open question for future work. Extended discussion in Appendix~\\ref{app:extended-discussion}.",
          " ",
          " \\paragraph{Reasoning depth scaling.}",
          "-Strategy specificity is not a fixed property but scales with reasoning chain depth: MATH-500 ($15$--$17{\\times}$) $>$ GSM8K (${\\sim}3{\\times}$), with within-MATH-500 correlational support (Spearman $\\rho > 0$, $p < 0.02$ between trace length and specificity). This scaling is consistent with the discrimination collapse mechanism: longer low-sparsity phases provide more tokens over which pruning-degraded importance scores accumulate errors, amplifying the gap between importance-based and random eviction. The implication is practical: as models generate longer reasoning chains (a trend driven by test-time compute scaling~\\cite{snell-2024-scaling-test-time}), the penalty for naive compound compression grows superlinearly.",
          "+Strategy specificity is not a fixed property but scales with reasoning chain depth: MATH-500 ($15$--$17{\\times}$) $>$ GSM8K (${\\sim}2{\\times}$ point-estimate ratio; random non-significant at $n{=}50$), with within-MATH-500 correlational support (Spearman $\\rho > 0$, $p < 0.02$ between trace length and specificity). This scaling is consistent with the discrimination collapse mechanism: longer low-sparsity phases provide more tokens over which pruning-degraded importance scores accumulate errors, amplifying the gap between importance-based and random eviction. The implication is practical: as models generate longer reasoning chains (a trend driven by test-time compute scaling~\\cite{snell-2024-scaling-test-time}), the penalty for naive compound compression grows superlinearly.",
          " ",
          " \\paragraph{Diagnostic framework value.}",
          " While we do not propose a new compression method, the phase-gated analysis framework has direct engineering utility: (1)~the Interaction Index can serve as a per-phase evaluation metric for assessing the phase robustness of any new compound compression scheme; (2)~the dose-response curves (Figure~\\ref{fig:hero}) provide target operating points for phase-aware controllers---e.g., maintaining $s \\leq 0.20$ during low-sparsity phases to keep $\\Delta < 1.5$; (3)~the strategy specificity finding carries a concrete engineering implication: importance-based eviction under compound sparsity requires phase-aware protection that random eviction does not, because the interaction is structurally coupled to the scoring mechanism rather than to compression magnitude alone."
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

_source line 51_

Also need to fix results.tex line 129 which uses the same "~3×" for GSM8K:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7c8d5505-1cf3-4db2-81a6-3ef2a3c9c146",
  "uuid": "f398718b-0ef8-4312-a220-08ce66e732e3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LpAWDByhXx9Tq3Wsqfc4FS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4261,
      "cache_read_input_tokens": 39880,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4261
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

_source line 52_

<details open><summary>🔧 Tool call — Edit · `toolu_013WcdAGF5vEcq663FS9RDWE`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex",
  "old_string": "GSM8K (simpler arithmetic, ratio ${\\sim}3{\\times}$)",
  "new_string": "GSM8K (simpler arithmetic, ratio ${\\sim}2{\\times}$ from point estimates)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7c8d5505-1cf3-4db2-81a6-3ef2a3c9c146",
  "uuid": "50b7e0b6-c735-46fc-8ed1-ff5493441217",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LpAWDByhXx9Tq3Wsqfc4FS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4261,
      "cache_read_input_tokens": 39880,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4261
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

_source line 53 · 2026-05-16T22:52:47.471Z_

<details><summary>↩ Tool result · `toolu_013WcdAGF5vEcq663FS9RDWE`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7c8d5505-1cf3-4db2-81a6-3ef2a3c9c146",
  "uuid": "287c6bae-471e-462c-a0ae-7b90df9b6e5a",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex",
    "oldString": "GSM8K (simpler arithmetic, ratio ${\\sim}3{\\times}$)",
    "newString": "GSM8K (simpler arithmetic, ratio ${\\sim}2{\\times}$ from point estimates)",
    "originalFile": "\n\\section{Results}\n\\label{sec:results}\n\n\\subsection{Strategy-Dependent Severity}\n\\label{sec:strategy-severity}\n\nTable~\\ref{tab:aggregate-ii} reports the median compound severity difference across strategies and sparsity levels. Under importance-based eviction, $\\Delta$ increases from $0.39$ at $s{=}0.15$ to $8.48$ at $s{=}0.30$---a $22{\\times}$ amplification (all Bonferroni-corrected $p \\ll 10^{-10}$). Random eviction develops a detectable but weak phase gradient above $s \\approx 0.20$: at $s \\leq 0.20$, $\\Delta$ is non-significant ($0.01$--$0.03$; CIs span zero); at $s \\geq 0.25$, $\\Delta$ becomes significant ($0.26$--$0.51$; $p_{\\text{Bonf}} < 0.006$) but $15$--$17{\\times}$ smaller than under importance-based eviction. Both strategies exhibit monotonic dose-response (Jonckheere-Terpstra $z{=}6.2$--$33.7$, all $p < 10^{-9}$), but importance masking effect sizes are an order of magnitude larger.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Median of per-problem paired severity differences ($\\Delta$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}496$, MATH-500).}\n\\label{tab:aggregate-ii}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nStrategy & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\\\\n\\midrule\nImportance & 0.39 & 1.21 & 3.99 & 8.48 \\\\\nRandom     & 0.01 & 0.03 & 0.26 & 0.51 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Phase-Modulated Amplification}\n\\label{sec:phase-amplification}\n\nDecomposing II by reasoning phase reveals that strategy-dependent severity is driven by amplification in the low-sparsity phase. Table~\\ref{tab:main-results} reports the per-phase breakdown. Under importance-based eviction, the median II in the low-sparsity phase rises from $0.357$ ($s{=}0.15$) to $8.456$ ($s{=}0.30$), while the high-sparsity phase remains near zero ($0.003$--$0.038$), yielding paired median differences $\\Delta$ from $0.39$ to $8.48$ (all $p \\ll 10^{-10}$). Random eviction shows a detectable but much weaker phase gradient at $s \\geq 0.25$ ($\\Delta{=}0.26$--$0.51$; $p_{\\text{Bonf}} < 0.006$), $15$--$17{\\times}$ smaller than importance-based at matched sparsity. Figure~\\ref{fig:hero} visualizes the dose-response relationship for both models. The per-problem amplification ratio $G$ (Eq.~\\ref{eq:gradient}) provides an auxiliary illustrative perspective and is reported in Appendix~\\ref{app:g-metric}.\nUnder the multiplicative null ($r_b = r_a \\cdot r_k$; Appendix~\\ref{app:multiplicative-null}), the phase-severity gradient is preserved ($G_{\\times}{=}21$--$64{\\times}$); we report additive-null values throughout as the more conservative estimates.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Per-phase interaction index (II) at $n{=}496$/$475$. $\\Delta{=}\\widetilde{\\mathrm{II}^{(i)}_{\\textit{low}} - \\mathrm{II}^{(i)}_{\\textit{high}}}$: median of per-problem paired differences (not the difference of column medians) with bootstrap 95\\% CI ($B{=}10{,}000$). $G$ values reported in Appendix~\\ref{app:g-metric}. Profiling-subset values ($n{=}50$) in Table~\\ref{tab:profiling-subset}.}\n\\label{tab:main-results}\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\n$s$ & Strategy & $\\widetilde{\\mathrm{II}}_{\\textit{high}}$ & $\\widetilde{\\mathrm{II}}_{\\textit{low}}$ & $\\Delta$\\; [95\\% CI] & $p_{\\text{Bonf}}$ \\\\\n\\midrule\n\\multicolumn{6}{@{}l}{\\textit{DeepSeek-R1-Distill-Qwen-7B ($n{=}496$)}} \\\\\n0.15 & Importance & 0.003 & 0.357 & 0.39\\; $[0.35,\\; 0.44]$ & $< 10^{-10}$ \\\\\n0.15 & Random     & 0.083 & 0.090 & 0.01\\; $[-0.02,\\; 0.04]$ & ns \\\\\n\\addlinespace\n0.20 & Importance & 0.008 & 1.211 & 1.21\\; $[1.11,\\; 1.34]$ & $< 10^{-10}$ \\\\\n0.20 & Random     & 0.270 & 0.357 & 0.03\\; $[-0.01,\\; 0.08]$ & ns \\\\\n\\addlinespace\n0.25 & Importance & 0.021 & 3.971 & 3.99\\; $[3.53,\\; 4.36]$ & $< 10^{-10}$ \\\\\n0.25 & Random     & 1.113 & 1.514 & 0.26\\; $[0.13,\\; 0.35]$ & $< 0.006$ \\\\\n\\addlinespace\n0.30 & Importance & 0.038 & 8.456 & 8.48\\; $[7.75,\\; 9.69]$ & $< 10^{-10}$ \\\\\n0.30 & Random     & 3.112 & 3.848 & 0.51\\; $[0.26,\\; 0.89]$ & $< 0.006$ \\\\\n\\midrule\n\\multicolumn{6}{@{}l}{\\textit{Qwen2.5-7B-Instruct ($n{=}475$)}} \\\\\n0.15 & Importance & $-$0.000$^{\\ddagger}$ & 0.044 & 0.07\\; $[0.05,\\; 0.09]$ & $< 10^{-14}$ \\\\\n0.15 & Random     & 0.094 & 0.097 & $-$0.01\\; $[-0.04,\\; 0.01]$ & ns \\\\\n\\addlinespace\n0.20 & Importance & 0.000 & 0.275 & 0.31\\; $[0.26,\\; 0.36]$ & $< 10^{-14}$ \\\\\n0.20 & Random     & 0.291 & 0.356 & 0.02\\; $[-0.01,\\; 0.07]$ & ns \\\\\n\\addlinespace\n0.25 & Importance & 0.004 & 1.053 & 1.07\\; $[0.98,\\; 1.18]$ & $< 10^{-14}$ \\\\\n0.25 & Random     & 1.108 & 1.769 & 0.39\\; $[0.24,\\; 0.55]$ & $< 10^{-10}$ \\\\\n\\addlinespace\n0.30 & Importance & 0.014 & 3.208 & 3.16\\; $[2.78,\\; 3.56]$ & $< 10^{-14}$ \\\\\n0.30 & Random     & 2.819 & 4.253 & 0.91\\; $[0.61,\\; 1.26]$ & $< 10^{-13}$ \\\\\n\\bottomrule\n\\multicolumn{6}{@{}p{0.92\\textwidth}}{\\footnotesize $^{\\ddagger}$ Negative II at this sparsity reflects \\texttt{bfloat16} numerical noise when the interaction effect approaches zero ($|\\mathrm{II}| < 10^{-4}$). $\\Delta{=}0.07$, $p{=}8.7 \\times 10^{-15}$ supports $\\mathrm{II}_{\\textit{low}} > \\mathrm{II}_{\\textit{high}}$.}\n\\end{tabular}\n\\end{table*}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig1_ii_scatter.pdf}\n\\caption{Paired median difference $\\Delta$ (primary metric) as a function of sparsity level $s$ for DeepSeek-R1-Distill-Qwen-7B ($n{=}496$, left) and Qwen2.5-7B-Instruct ($n{=}475$, right). Importance-based eviction (red) exhibits monotonically increasing $\\Delta$ ($0.39$--$8.48$ for DeepSeek, $0.07$--$3.16$ for Qwen); random eviction (blue) remains near zero at low sparsity (ns) and shows weak effects at $s \\geq 0.25$. Error bars show asymmetric bootstrap 95\\% CIs. DeepSeek importance effects are ${\\sim}2.7{\\times}$ larger than Qwen, consistent with the training-paradigm contrast (\\S\\ref{sec:cross-model}). Significance: {*}{*}{*}\\,$p_{\\text{Bonf}} < 0.001$; {*}{*}\\,$p_{\\text{Bonf}} < 0.01$; ns\\,$p_{\\text{Bonf}} > 0.05$.}\n\\label{fig:hero}\n\\end{figure*}\n\n\n\\subsection{Phase-Strategy Crossover}\n\\label{sec:crossover}\n\nThe phase-strategy crossover is model-dependent. For DeepSeek ($n{=}496$), a strategy ranking reversal emerges at all four sparsity levels: at $s{=}0.25$, importance-based eviction yields \\emph{lower} II than random in the high-sparsity phase ($0.021$ vs.\\ $1.113$) but \\emph{higher} II in the low-sparsity phase ($3.971$ vs.\\ $1.514$---a $2.6{\\times}$ reversal; both $p < 10^{-4}$), with reversal magnitude ranging from $2.2{\\times}$ to $4.0{\\times}$ across $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$. Qwen does \\emph{not} exhibit this crossover: importance-based eviction produces lower II than random in both phases (e.g., at $s{=}0.25$: high $0.004$ vs.\\ $1.108$; low $1.053$ vs.\\ $1.769$). This divergence suggests the crossover arises from model-specific attention head specialization patterns rather than a universal compound-sparsity property. Full crossover analysis appears in Appendix~\\ref{app:crossover-details}.\n\n\\subsection{Replication Across Training Paradigms}\n\\label{sec:cross-model}\n\nDeepSeek-R1-Distill-Qwen-7B (distillation-trained) and Qwen2.5-7B-Instruct (instruction-tuned) share the Qwen2 backbone but differ in training objective, providing a within-architecture-family comparison across training paradigms.\nQwen2.5-7B-Instruct ($n_{\\text{eff}}{=}475$) reproduces the monotonic severity gradient: $\\Delta$ increases from $0.07$ at $s{=}0.15$ to $3.16$ at $s{=}0.30$ (all Bonferroni-corrected $p < 10^{-14}$), paralleling DeepSeek at approximately one-quarter to one-sixth the magnitude. Both models yield strictly increasing median $\\Delta$ trajectories (Jonckheere-Terpstra $z \\geq 6.2$, $p < 10^{-9}$; see \\S\\ref{par:stats}). Random eviction on Qwen mirrors DeepSeek: non-significant at $s \\leq 0.20$, becoming significant at $s \\geq 0.25$ ($\\Delta{=}0.39$--$0.91$; $p_{\\text{Bonf}} < 10^{-10}$) but $2.7$--$3.5{\\times}$ weaker than importance-based. A caveat: 45.2\\% of Qwen problems yield null mid-phase segments due to low temporal autocorrelation ($r{=}0.718$ vs.\\ $0.894$); this does not affect $\\Delta$ (Appendix~\\ref{app:qwen-null-rate}). Full tables in Appendix~\\ref{app:cross-model-details}.\n\n\\subsection{Cross-Architecture Validation}\n\\label{sec:cross-arch}\n\nCross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, $n{=}250$, MATH-500) supports the generality of phase-modulated compound interaction beyond the Qwen2 architecture family. Under importance-based eviction, the paired median difference $\\Delta$ rises monotonically from $0.050$ ($s{=}0.15$) to $0.695$ ($s{=}0.30$), with large effect sizes throughout ($d_z{=}0.81$--$1.15$; all $p < 10^{-29}$; Table~\\ref{tab:llama-cross-arch}).\n\nA key architectural difference emerges in strategy specificity. On LLaMA, random eviction also exhibits significant phase gradients ($\\Delta{=}0.025$--$0.271$; $d_z{=}0.41$--$0.46$; all $p < 10^{-12}$), unlike DeepSeek and Qwen where random is non-significant at $s \\leq 0.20$. The importance/random $\\Delta$ ratio is $2.0$--$2.6{\\times}$ on LLaMA, substantially weaker than the $15$--$17{\\times}$ observed on DeepSeek. Dose-response monotonicity holds for both strategies (all conditions monotonic). This indicates that the phase gradient itself is architecture-general, while the degree of strategy specificity is architecture-dependent, likely reflecting differences between GQA (LLaMA, 32 heads with 8 KV groups) and MHA (Qwen2, 28 heads) in how head pruning differentially disrupts importance scoring.\n\nAbsolute interaction magnitudes are approximately $7$--$12{\\times}$ smaller than Qwen2-family models at matched sparsity, consistent with architecture-specific attention head specialization patterns. Full per-condition breakdowns appear in Appendix~\\ref{app:cross-arch}.\n\n\\subsection{Scale Analysis: Qwen2.5-14B}\n\\label{sec:scale-14b}\n\nTo assess whether phase-modulated severity persists at larger model scale within the same architecture family, we evaluate Qwen2.5-14B-Instruct on MATH-500 ($n{=}500$) at $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Median of per-problem paired severity differences ($\\Delta$) under importance-based eviction on Qwen2.5-14B-Instruct (MATH-500). \\textit{Results pending.}}\n\\label{tab:scale-14b}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nStrategy & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\\\\n\\midrule\nImportance & --- & --- & --- & --- \\\\\nRandom     & --- & --- & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%% PLACEHOLDER: Fill Table~\\ref{tab:scale-14b} when c12 experiment completes.\n%% Expected analysis: (1) whether 14B amplifies or attenuates severity relative to 7B,\n%% (2) whether strategy specificity ratio is scale-invariant,\n%% (3) comparison of phase segmentation thresholds at larger scale.\n\n\\subsection{Cross-Benchmark Validation: GSM8K}\n\\label{sec:cross-benchmark}\n\nTo assess task generalization, we evaluate both models on GSM8K ($n{=}50$) at $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$. On DeepSeek (clean data, no output truncation), importance-based eviction replicates the MATH-500 phase gradient across all four sparsity levels with a strict dose-response: $\\Delta{=}0.24$ at $s{=}0.15$ rising to $4.68$ at $s{=}0.30$ (all $p \\leq 0.0003$, Wilcoxon). Strategy specificity on GSM8K manifests as a \\emph{qualitative} gap: importance-based eviction produces significant phase gradients while random eviction is non-significant across all conditions (CIs spanning zero).\n\nWe interpret this attenuation as \\emph{reasoning depth scaling}: strategy specificity scales with reasoning chain depth. MATH-500 (complex multi-step reasoning, strategy ratio $15$--$17{\\times}$) produces stronger phase contrast than GSM8K (simpler arithmetic, ratio ${\\sim}3{\\times}$). Within MATH-500, longer traces exhibit higher strategy specificity (Spearman $\\rho > 0$, $p < 0.02$), providing continuous correlational support. This scaling relationship is predictive: tasks with deeper reasoning chains should exhibit stronger strategy${\\times}$phase interactions, because longer low-sparsity phases provide more opportunity for importance discrimination collapse to accumulate. Qwen GSM8K results are inconclusive due to generation truncation (\\texttt{max\\_new\\_tokens}${=}$2047): while directional consistency holds at $s \\geq 0.25$ ($\\Delta{=}1.14$--$4.62$; $p < 10^{-4}$), absolute values and phase assignments are unreliable because all outputs hit the token limit. Full tables in Appendix~\\ref{app:gsm8k}.\n\n\\paragraph{GSM8K accuracy under compound sparsity.}\nA power analysis on GSM8K ($n{=}50$) reveals a strategy-dependent asymmetry in downstream accuracy. Under random head removal, all 8 conditions (2 models $\\times$ 4 sparsity levels) are non-significant (max $|d|{=}0.164$). Post-hoc power analysis indicates $n{=}50$ can detect effects of $d \\geq 0.40$ ($\\alpha{=}0.05$, power${=}0.80$); all random conditions showed $|d| \\leq 0.164$, meaning the null results may reflect insufficient power rather than true absence of effect. Under importance-based pruning, Qwen exhibits a medium-sized accuracy degradation at $s \\geq 0.25$ ($d \\approx 0.63$, power ${>}\\,0.99$), consistent with the PPL-based severity gradient observed on MATH-500. DeepSeek importance conditions exhibit a qualitative downward trend in accuracy but are excluded from parametric inference due to heavy-tailed distributions that violate test assumptions.\n\n\\subsection{Cross-Benchmark Validation: GPQA Diamond}\n\\label{sec:cross-benchmark-gpqa}\n\nTo assess generalization beyond mathematical reasoning, we evaluate both models on GPQA Diamond~\\cite{rein-gpqa-2024} ($n{=}198$), a graduate-level science QA benchmark requiring multi-step reasoning across physics, chemistry, and biology.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Median of per-problem paired severity differences ($\\Delta$) under importance-based eviction on GPQA Diamond. \\textit{Results pending.}}\n\\label{tab:gpqa-results}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nModel & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\\\\n\\midrule\nDeepSeek-R1-Distill-Qwen-7B & --- & --- & --- & --- \\\\\nQwen2.5-7B-Instruct         & --- & --- & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%% PLACEHOLDER: Fill Table~\\ref{tab:gpqa-results} when c11 experiment completes.\n%% Expected analysis: (1) phase gradient direction consistency with MATH-500/GSM8K,\n%% (2) strategy specificity comparison across task types (math vs. science reasoning),\n%% (3) whether cognitive load modulation hypothesis extends to non-mathematical domains.\n\n\\subsection{Statistical Validation}\n\\label{sec:stat-validation}\n\nTable~\\ref{tab:cohens-d} reports the paired median difference $\\Delta$ under importance-based eviction for both models at $n{=}496$/$475$. All eight conditions yield CIs excluding zero; within-importance dose-response $d_z$ (s015 vs.\\ s030) is $0.94$ (DeepSeek) and $0.92$ (Qwen), both large effects. Importance-based eviction produces significantly larger phase gradients than random at all four sparsity levels ($p_{\\text{Bonf}} \\ll 10^{-10}$, Wilcoxon; permutation tests in Appendix~\\ref{app:permutation-details}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Median of paired differences ($\\Delta_i = \\mathrm{II}^{(i)}_{\\textit{low}} - \\mathrm{II}^{(i)}_{\\textit{high}}$) under importance-based eviction with bootstrap 95\\% CIs ($B{=}10{,}000$).}\n\\label{tab:cohens-d}\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n$s$ & DS ($n{=}496$): $\\widetilde{\\Delta}$\\; [95\\% CI] & QW ($n{=}475$): $\\widetilde{\\Delta}$\\; [95\\% CI] \\\\\n\\midrule\n0.15 & $0.39$\\; $[0.35,\\; 0.44]$ & $0.07$\\; $[0.05,\\; 0.09]$ \\\\\n0.20 & $1.21$\\; $[1.11,\\; 1.34]$ & $0.31$\\; $[0.26,\\; 0.36]$ \\\\\n0.25 & $3.99$\\; $[3.53,\\; 4.36]$ & $1.07$\\; $[0.98,\\; 1.18]$ \\\\\n0.30 & $8.48$\\; $[7.75,\\; 9.69]$ & $3.16$\\; $[2.78,\\; 3.56]$ \\\\\n\\bottomrule\n\\multicolumn{3}{@{}l}{\\footnotesize All $p_{\\text{Bonf}} < 10^{-13}$. Within-importance $d_z$ (s015 vs.\\ s030): DS $0.94$, QW $0.92$.}\n\\end{tabular}\n\\end{table}\n\n\\subsection{Answer-Region Analysis}\n\\label{sec:answer-region}\n\nAcross both models, 93.2\\% of answer tokens (\\verb|\\boxed{}| markers) fall within the high-sparsity phase, where compound interaction is minimal. This non-uniformity identifies \\emph{where} severity concentrates: reasoning-trace tokens show $5.7$--$43.5{\\times}$ PPL degradation vs.\\ $1.3$--$5.3{\\times}$ for answer tokens (Wilcoxon $p < 0.001$). However, reasoning-trace degradation may produce \\emph{silent reasoning errors}---correct formatting with corrupted intermediate logic \\cite{lanham-2023-faithfulness, turpin-2023-biased-cot}---a failure mode that PPL detects but answer-level accuracy may miss.\n\n\\subsection{Downstream Accuracy Validation}\n\\label{sec:accuracy-validation}\n\nTo validate that the PPL-based severity gradient translates to downstream task performance, we evaluate MATH-500 accuracy under compound sparsity (importance-based eviction, \\texttt{max\\_new\\_tokens}${=}$8192; Table~\\ref{tab:accuracy}). Qwen's minimal truncation ($\\leq 4\\%$) provides a clean PPL-accuracy bridge.\nQwen ($n{=}100$; truncation $\\leq 4\\%$) shows gradual decline from $46\\%$ (dense) through $s{=}0.25$ ($\\delta{=}-4$ to $-13$\\,pp) with a sharp cliff at $s{=}0.30$ ($19\\%$, $\\delta{=}-27$\\,pp). DeepSeek ($n{=}50$) degrades more steeply ($74\\% \\to 4\\%$) with a dual-regime structure: at $s \\leq 0.20$, degradation is primarily truncation-driven (non-truncated accuracy remains $68$--$71\\%$ at $s{=}0.15$--$0.20$ vs.\\ $88\\%$ dense); at $s \\geq 0.25$, both truncation and reasoning quality collapse simultaneously (Appendix~\\ref{app:accuracy-details}).\nThe two models exhibit distinct failure modes reflecting training-paradigm dependence: DeepSeek failures are \\emph{truncation-dominated} (truncation $16\\% \\to 76\\%$), while Qwen failures are \\emph{wrong-answer-dominated} (truncation $\\leq 4\\%$, reasoning quality degrades directly). Given minimal truncation, Qwen accuracy data provide a reliable PPL-accuracy bridge; DeepSeek accuracy results, confounded by truncation rates of $16\\%$--$76\\%$, should be interpreted as qualitative observations only.\n\nWe provide a correlational mechanistic analysis in terms of importance discrimination collapse in \\S\\ref{sec:analysis}.\n",
    "structuredPatch": [
      {
        "oldStart": 126,
        "oldLines": 7,
        "newStart": 126,
        "newLines": 7,
        "lines": [
          " ",
          " To assess task generalization, we evaluate both models on GSM8K ($n{=}50$) at $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$. On DeepSeek (clean data, no output truncation), importance-based eviction replicates the MATH-500 phase gradient across all four sparsity levels with a strict dose-response: $\\Delta{=}0.24$ at $s{=}0.15$ rising to $4.68$ at $s{=}0.30$ (all $p \\leq 0.0003$, Wilcoxon). Strategy specificity on GSM8K manifests as a \\emph{qualitative} gap: importance-based eviction produces significant phase gradients while random eviction is non-significant across all conditions (CIs spanning zero).",
          " ",
          "-We interpret this attenuation as \\emph{reasoning depth scaling}: strategy specificity scales with reasoning chain depth. MATH-500 (complex multi-step reasoning, strategy ratio $15$--$17{\\times}$) produces stronger phase contrast than GSM8K (simpler arithmetic, ratio ${\\sim}3{\\times}$). Within MATH-500, longer traces exhibit higher strategy specificity (Spearman $\\rho > 0$, $p < 0.02$), providing continuous correlational support. This scaling relationship is predictive: tasks with deeper reasoning chains should exhibit stronger strategy${\\times}$phase interactions, because longer low-sparsity phases provide more opportunity for importance discrimination collapse to accumulate. Qwen GSM8K results are inconclusive due to generation truncation (\\texttt{max\\_new\\_tokens}${=}$2047): while directional consistency holds at $s \\geq 0.25$ ($\\Delta{=}1.14$--$4.62$; $p < 10^{-4}$), absolute values and phase assignments are unreliable because all outputs hit the token limit. Full tables in Appendix~\\ref{app:gsm8k}.",
          "+We interpret this attenuation as \\emph{reasoning depth scaling}: strategy specificity scales with reasoning chain depth. MATH-500 (complex multi-step reasoning, strategy ratio $15$--$17{\\times}$) produces stronger phase contrast than GSM8K (simpler arithmetic, ratio ${\\sim}2{\\times}$ from point estimates). Within MATH-500, longer traces exhibit higher strategy specificity (Spearman $\\rho > 0$, $p < 0.02$), providing continuous correlational support. This scaling relationship is predictive: tasks with deeper reasoning chains should exhibit stronger strategy${\\times}$phase interactions, because longer low-sparsity phases provide more opportunity for importance discrimination collapse to accumulate. Qwen GSM8K results are inconclusive due to generation truncation (\\texttt{max\\_new\\_tokens}${=}$2047): while directional consistency holds at $s \\geq 0.25$ ($\\Delta{=}1.14$--$4.62$; $p < 10^{-4}$), absolute values and phase assignments are unreliable because all outputs hit the token limit. Full tables in Appendix~\\ref{app:gsm8k}.",
          " ",
          " \\paragraph{GSM8K accuracy under compound sparsity.}",
          " A power analysis on GSM8K ($n{=}50$) reveals a strategy-dependent asymmetry in downstream accuracy. Under random head removal, all 8 conditions (2 models $\\times$ 4 sparsity levels) are non-significant (max $|d|{=}0.164$). Post-hoc power analysis indicates $n{=}50$ can detect effects of $d \\geq 0.40$ ($\\alpha{=}0.05$, power${=}0.80$); all random conditions showed $|d| \\leq 0.164$, meaning the null results may reflect insufficient power rather than true absence of effect. Under importance-based pruning, Qwen exhibits a medium-sized accuracy degradation at $s \\geq 0.25$ ($d \\approx 0.63$, power ${>}\\,0.99$), consistent with the PPL-based severity gradient observed on MATH-500. DeepSeek importance conditions exhibit a qualitative downward trend in accuracy but are excluded from parametric inference due to heavy-tailed distributions that violate test assumptions."
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

_source line 54_

修改完成，共 5 处：

| # | 文件 | 修改 | 原因 |
|---|------|------|------|
| 1a | `results.tex:88` | `$2.7$--$20{\times}$` → `$2.7$--$3.5{\times}$` | Qwen-specific，数据验证 0.39/1.07=2.7×, 0.91/3.16=3.5× |
| 1b | `appendix_disc_analysis.tex:53` | `$2.7$--$20{\times}$` → `$2.7$--$17{\times}$` | "both models" 语境，与 conclusion.tex 一致（DeepSeek 15–17×, Qwen 2.7–3.5×） |
| 2 | `conclusion.tex:4` | `$n{=}500$` → `$n{=}496$` | 与 results.tex table caption 一致 |
| 3a | `discussion.tex:8` | `GSM8K (${\sim}3{\times}$)` → `GSM8K (${\sim}2{\times}$ point-estimate ratio; random non-significant at $n{=}50$)` | 实际点估计 1.6–2.6×，且 random 全部 NS |
| 3b | `results.tex:129` | `ratio ${\sim}3{\times}$` → `ratio ${\sim}2{\times}$ from point estimates` | 同上，保持一致 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7c8d5505-1cf3-4db2-81a6-3ef2a3c9c146",
  "uuid": "96b48300-ad68-4078-ab12-14b2a62b5e6f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0145n1pp62yqqbZYbg9fcfZA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 273,
      "cache_read_input_tokens": 44141,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 273
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

_source line 55_

修改完成，共 5 处：

| # | 文件 | 修改 | 原因 |
|---|------|------|------|
| 1a | `results.tex:88` | `$2.7$--$20{\times}$` → `$2.7$--$3.5{\times}$` | Qwen-specific，数据验证 0.39/1.07=2.7×, 0.91/3.16=3.5× |
| 1b | `appendix_disc_analysis.tex:53` | `$2.7$--$20{\times}$` → `$2.7$--$17{\times}$` | "both models" 语境，与 conclusion.tex 一致（DeepSeek 15–17×, Qwen 2.7–3.5×） |
| 2 | `conclusion.tex:4` | `$n{=}500$` → `$n{=}496$` | 与 results.tex table caption 一致 |
| 3a | `discussion.tex:8` | `GSM8K (${\sim}3{\times}$)` → `GSM8K (${\sim}2{\times}$ point-estimate ratio; random non-significant at $n{=}50$)` | 实际点估计 1.6–2.6×，且 random 全部 NS |
| 3b | `results.tex:129` | `ratio ${\sim}3{\times}$` → `ratio ${\sim}2{\times}$ from point estimates` | 同上，保持一致 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 190021,
  "duration_api_ms": 190823,
  "num_turns": 21,
  "stop_reason": "end_turn",
  "session_id": "7c8d5505-1cf3-4db2-81a6-3ef2a3c9c146",
  "total_cost_usd": 0.6519882500000002,
  "usage": {
    "input_tokens": 14,
    "cache_creation_input_tokens": 32573,
    "cache_read_input_tokens": 377876,
    "output_tokens": 10319,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 32573,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 406,
        "cache_read_input_tokens": 44141,
        "cache_creation_input_tokens": 273,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 273
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1339,
      "outputTokens": 17,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001424,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 14,
      "outputTokens": 10319,
      "cacheReadInputTokens": 377876,
      "cacheCreationInputTokens": 32573,
      "webSearchRequests": 0,
      "costUSD": 0.6505642500000002,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "bd0fd5d1-a2ca-4b57-9226-da54eaa68d93"
}
```

</details>

---
