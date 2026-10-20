# paper consistency audit

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 86
- **Recorded user turns:** 1
- **Tool calls:** 27
- **Original source:** `logs/workers/worker_paper_consistency_audit_20260514T094456.log`
- **Structured JSON:** [`1ff9e8be4e36cfadec5b.json`](../../sessions/1f/1ff9e8be4e36cfadec5b.json)

## Before a recorded user message

27 recorded events

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
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
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
  "uuid": "0b5212bb-aaec-41ad-8426-c2aefc2a73d7",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/memory/"
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
    "status": "allowed_warning",
    "resetsAt": 1779267600,
    "rateLimitType": "seven_day",
    "utilization": 0.38,
    "isUsingOverage": false
  },
  "uuid": "ca019966-6339-47a7-a800-e088570cb744",
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to perform a full consistency audit of their paper for EMNLP 2026. Let me start by reading all the current version tex files and the paper_framing.md file to do the cross-checking.

Let me read all the files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "e7ae1694-afde-4a1f-9224-4f2a6c4951e7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EdBEMbD3qwr7Lh5TcAKsMH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12180,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12180
      },
      "output_tokens": 22,
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

开始全文一致性审查。先读取所有当前版本 tex 文件和 paper_framing.md。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "26aa1713-9f93-4ee8-b84e-80c832a6fe7b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EdBEMbD3qwr7Lh5TcAKsMH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12180,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12180
      },
      "output_tokens": 22,
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

<details open><summary>🔧 Tool call — Read · `toolu_01UUXvZKKWPGeWegD4MtSBNv`</summary>

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
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "a7226cbe-051b-424d-bcd0-e263a2d432bc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EdBEMbD3qwr7Lh5TcAKsMH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12180,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12180
      },
      "output_tokens": 22,
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

_source line 7 · 2026-05-14T09:45:08.466Z_

<details><summary>↩ Tool result · `toolu_01UUXvZKKWPGeWegD4MtSBNv`</summary>

```text
1	\begin{abstract}
2	Compound sparsity---simultaneously pruning attention heads and evicting KV cache entries---is essential for efficient LLM inference but produces super-additive quality degradation whose structure is poorly understood.
3	Prior work treats compound interaction magnitude as approximately constant across the generation process.
4	We show that this assumption is wrong: compound sparsity severity is an emergent phase-strategy interaction that varies by over an order of magnitude across reasoning phases.
5	
6	We evaluate compound sparsity on DeepSeek-R1-Distill-Qwen-7B and Qwen2.5-7B-Instruct (both Qwen2 architecture, 7B parameters) using 50 MATH-500 problems, measuring the Interaction Index---a super-additivity metric---across quantile-segmented reasoning phases at sparsity levels $s \in \{0.15, 0.20, 0.25, 0.30\}$.
7	Under importance-based KV cache eviction, the median Interaction Index difference between low-sparsity and high-sparsity reasoning phases increases monotonically from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with Cohen's $d$ growing from $0.44$ (small) to $0.80$ (large); Bonferroni-corrected permutation tests yield $p < 0.005$ at all four sparsity levels.
8	Random eviction produces no significant phase modulation in 7/8 conditions; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) shows negligible effect size ($d{=}{-}0.04$), confirming that the severity gradient is strategy-specific, not an inherent property of compound sparsity.
9	At $s{=}0.25$, a crossover emerges: importance-based eviction outperforms random in high-sparsity phases ($\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$) yet underperforms in low-sparsity phases ($\widetilde{\mathrm{II}} = 7.196$ vs.\ $1.363$)---a qualitative reversal in strategy ranking.
10	The pattern replicates on Qwen2.5-7B-Instruct at $s \geq 0.20$ (Cohen's $d \geq 0.55$; Spearman $\rho = 1.0$ across sparsity levels; gradient permutation $p = 0.043$).
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
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "9f3590ed-38a8-4fda-87c2-510325a0cea0",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex",
      "content": "\\begin{abstract}\nCompound sparsity---simultaneously pruning attention heads and evicting KV cache entries---is essential for efficient LLM inference but produces super-additive quality degradation whose structure is poorly understood.\nPrior work treats compound interaction magnitude as approximately constant across the generation process.\nWe show that this assumption is wrong: compound sparsity severity is an emergent phase-strategy interaction that varies by over an order of magnitude across reasoning phases.\n\nWe evaluate compound sparsity on DeepSeek-R1-Distill-Qwen-7B and Qwen2.5-7B-Instruct (both Qwen2 architecture, 7B parameters) using 50 MATH-500 problems, measuring the Interaction Index---a super-additivity metric---across quantile-segmented reasoning phases at sparsity levels $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$.\nUnder importance-based KV cache eviction, the median Interaction Index difference between low-sparsity and high-sparsity reasoning phases increases monotonically from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with Cohen's $d$ growing from $0.44$ (small) to $0.80$ (large); Bonferroni-corrected permutation tests yield $p < 0.005$ at all four sparsity levels.\nRandom eviction produces no significant phase modulation in 7/8 conditions; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) shows negligible effect size ($d{=}{-}0.04$), confirming that the severity gradient is strategy-specific, not an inherent property of compound sparsity.\nAt $s{=}0.25$, a crossover emerges: importance-based eviction outperforms random in high-sparsity phases ($\\widetilde{\\mathrm{II}} = 0.032$ vs.\\ $0.818$) yet underperforms in low-sparsity phases ($\\widetilde{\\mathrm{II}} = 7.196$ vs.\\ $1.363$)---a qualitative reversal in strategy ranking.\nThe pattern replicates on Qwen2.5-7B-Instruct at $s \\geq 0.20$ (Cohen's $d \\geq 0.55$; Spearman $\\rho = 1.0$ across sparsity levels; gradient permutation $p = 0.043$).\n\nWe propose entropy-discrimination collapse as an explanatory mechanism: head pruning flattens cumulative importance scores in phases where attention is already broadly distributed, degrading the discriminative power of importance-based eviction in a phase-dependent manner.\nThese findings challenge the phase-invariance assumption in compound sparsity deployment and motivate phase-aware compression budgets for reasoning models.\n\\end{abstract}",
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

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_01RhRjaY9GQKJa7bvjxNvgAY`</summary>

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
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "9f4a338a-7a8c-4755-9919-38109eb6a759",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EdBEMbD3qwr7Lh5TcAKsMH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12180,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12180
      },
      "output_tokens": 22,
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

_source line 9 · 2026-05-14T09:45:09.396Z_

<details><summary>↩ Tool result · `toolu_01RhRjaY9GQKJa7bvjxNvgAY`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Long-context language models place acute pressure on the key--value (KV) cache, which grows linearly with sequence length and dominates inference memory at scale \cite{kwon2023vllm, pope2023efficiently}.
5	Two complementary responses have emerged: \emph{attention head pruning}, which removes structurally redundant heads \cite{voita2019heads, michel2019sixteen}, and \emph{KV cache eviction}, which discards low-importance token positions from the cache \cite{snapkv-neurips2024, adakv-neurips2025}.
6	Deploying both simultaneously---\emph{compound sparsity}---is attractive because the compression gains multiply, but the resulting quality degradation can be super-additive: the joint loss exceeds the sum of individual losses \cite{spark-aaai2026, slim-icml2025}.
7	
8	Prior work has characterized compound interaction as a property of the sparsity level---higher sparsity yields more interaction---but treats the interaction magnitude as roughly constant across the generation process \cite{spark-aaai2026, unicomp-2026}.
9	This assumption is problematic for reasoning-capable models, whose generations are structurally heterogeneous: a single chain-of-thought trace alternates between phases of broadly distributed attention (exploratory reasoning) and phases of sharply concentrated attention (structured computation) \cite{thinkv-iclr2026, decision-repr-transition-2026}.
10	If compound interaction severity varies across these phases, then a uniform sparsity budget---the standard deployment practice---may be safe in one phase yet destructive in another.
11	
12	We investigate whether compound sparsity severity is modulated by reasoning phase and eviction strategy.
13	Our central finding is that it is, and strongly so: under importance-based KV cache eviction, the Interaction Index---a measure of super-additive compound degradation---is concentrated in the low-sparsity phase (where attention distributes broadly) and largely absent in the high-sparsity phase (where attention is focused).
14	This \emph{severity gradient} grows monotonically with the sparsity budget: on DeepSeek-R1-Distill-Qwen-7B, the median phase difference in Interaction Index rises from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired effect sizes increasing from $d{=}0.61$ (medium) to $d{=}1.13$ (large); Bonferroni-corrected permutation tests confirm significance at all four sparsity levels on this model ($p < 0.005$).
15	The pattern replicates at $s \geq 0.20$ on Qwen2.5-7B-Instruct ($d \geq 0.72$) with attenuated absolute magnitude, though the effect at $s{=}0.15$ is marginal ($d{=}0.37$, bootstrap CI includes zero).
16	Critically, random eviction produces no such gradient: 7/8 conditions across both models fail to exhibit a significant phase difference (the single exception---Qwen $s{=}0.30$---has negligible effect size, $d{=}{-}0.04$), confirming that the severity gradient is an emergent property of the interaction between importance scoring and phase-dependent attention structure, not an artifact of compound sparsity per se.
17	
18	We propose \emph{entropy-discrimination collapse} as an explanatory mechanism.
19	Head pruning forces surviving heads to redistribute attention mass, increasing attention entropy.
20	In low-sparsity phases, where attention is already broadly distributed, this redistribution flattens the cumulative importance scores used for KV eviction, degrading their discriminative power.
21	Importance-based eviction then degenerates into a biased pseudo-random process that can inadvertently remove critical positions---amplifying compound severity.
22	In high-sparsity phases, attention concentration is preserved after pruning, importance scores remain discriminative, and eviction remains well-targeted.
23	Random eviction is immune to this mechanism because its decisions are independent of attention patterns.
24	
25	Our contributions are as follows:
26	\begin{enumerate}[nosep,leftmargin=*]
27	    \item We identify a \textbf{phase--strategy interaction} in compound sparsity: importance-based eviction exhibits a severity gradient across reasoning phases that is absent under random eviction (\S\ref{sec:experiments}).
28	    \item We show that this severity gradient \textbf{increases monotonically with sparsity} and replicate the finding at moderate-to-high sparsity ($s \geq 0.20$) across two models with different training regimes (distillation vs.\ instruction tuning), establishing robustness within the Qwen2 architecture family (\S\ref{sec:experiments}).
29	    \item We propose \textbf{entropy-discrimination collapse} as a mechanistic explanation, linking head pruning to the degradation of importance-score discriminability in a phase-dependent manner (\S\ref{sec:analysis}).
30	\end{enumerate}
31	
32	These findings challenge the implicit assumption that compound interaction magnitude is phase-invariant, and suggest that sparsity budgets should be allocated in a phase-aware manner---tightening compression during low-sparsity reasoning phases where compound interaction is most severe.
33	The remainder of this paper is organized as follows: \S\ref{sec:related} surveys related work on compound compression, KV cache eviction, and phase-aware inference; \S\ref{sec:background} formalizes compound sparsity and introduces the Interaction Index; \S\ref{sec:experimental-setup} describes our experimental setup; \S\ref{sec:experiments} presents the main results; \S\ref{sec:analysis} analyzes the entropy-discrimination collapse mechanism; and \S\ref{sec:discussion} discusses implications and limitations.
34	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "7ef261c7-d0e9-4044-9218-25b99dcd5c95",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nLong-context language models place acute pressure on the key--value (KV) cache, which grows linearly with sequence length and dominates inference memory at scale \\cite{kwon2023vllm, pope2023efficiently}.\nTwo complementary responses have emerged: \\emph{attention head pruning}, which removes structurally redundant heads \\cite{voita2019heads, michel2019sixteen}, and \\emph{KV cache eviction}, which discards low-importance token positions from the cache \\cite{snapkv-neurips2024, adakv-neurips2025}.\nDeploying both simultaneously---\\emph{compound sparsity}---is attractive because the compression gains multiply, but the resulting quality degradation can be super-additive: the joint loss exceeds the sum of individual losses \\cite{spark-aaai2026, slim-icml2025}.\n\nPrior work has characterized compound interaction as a property of the sparsity level---higher sparsity yields more interaction---but treats the interaction magnitude as roughly constant across the generation process \\cite{spark-aaai2026, unicomp-2026}.\nThis assumption is problematic for reasoning-capable models, whose generations are structurally heterogeneous: a single chain-of-thought trace alternates between phases of broadly distributed attention (exploratory reasoning) and phases of sharply concentrated attention (structured computation) \\cite{thinkv-iclr2026, decision-repr-transition-2026}.\nIf compound interaction severity varies across these phases, then a uniform sparsity budget---the standard deployment practice---may be safe in one phase yet destructive in another.\n\nWe investigate whether compound sparsity severity is modulated by reasoning phase and eviction strategy.\nOur central finding is that it is, and strongly so: under importance-based KV cache eviction, the Interaction Index---a measure of super-additive compound degradation---is concentrated in the low-sparsity phase (where attention distributes broadly) and largely absent in the high-sparsity phase (where attention is focused).\nThis \\emph{severity gradient} grows monotonically with the sparsity budget: on DeepSeek-R1-Distill-Qwen-7B, the median phase difference in Interaction Index rises from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired effect sizes increasing from $d{=}0.61$ (medium) to $d{=}1.13$ (large); Bonferroni-corrected permutation tests confirm significance at all four sparsity levels on this model ($p < 0.005$).\nThe pattern replicates at $s \\geq 0.20$ on Qwen2.5-7B-Instruct ($d \\geq 0.72$) with attenuated absolute magnitude, though the effect at $s{=}0.15$ is marginal ($d{=}0.37$, bootstrap CI includes zero).\nCritically, random eviction produces no such gradient: 7/8 conditions across both models fail to exhibit a significant phase difference (the single exception---Qwen $s{=}0.30$---has negligible effect size, $d{=}{-}0.04$), confirming that the severity gradient is an emergent property of the interaction between importance scoring and phase-dependent attention structure, not an artifact of compound sparsity per se.\n\nWe propose \\emph{entropy-discrimination collapse} as an explanatory mechanism.\nHead pruning forces surviving heads to redistribute attention mass, increasing attention entropy.\nIn low-sparsity phases, where attention is already broadly distributed, this redistribution flattens the cumulative importance scores used for KV eviction, degrading their discriminative power.\nImportance-based eviction then degenerates into a biased pseudo-random process that can inadvertently remove critical positions---amplifying compound severity.\nIn high-sparsity phases, attention concentration is preserved after pruning, importance scores remain discriminative, and eviction remains well-targeted.\nRandom eviction is immune to this mechanism because its decisions are independent of attention patterns.\n\nOur contributions are as follows:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item We identify a \\textbf{phase--strategy interaction} in compound sparsity: importance-based eviction exhibits a severity gradient across reasoning phases that is absent under random eviction (\\S\\ref{sec:experiments}).\n    \\item We show that this severity gradient \\textbf{increases monotonically with sparsity} and replicate the finding at moderate-to-high sparsity ($s \\geq 0.20$) across two models with different training regimes (distillation vs.\\ instruction tuning), establishing robustness within the Qwen2 architecture family (\\S\\ref{sec:experiments}).\n    \\item We propose \\textbf{entropy-discrimination collapse} as a mechanistic explanation, linking head pruning to the degradation of importance-score discriminability in a phase-dependent manner (\\S\\ref{sec:analysis}).\n\\end{enumerate}\n\nThese findings challenge the implicit assumption that compound interaction magnitude is phase-invariant, and suggest that sparsity budgets should be allocated in a phase-aware manner---tightening compression during low-sparsity reasoning phases where compound interaction is most severe.\nThe remainder of this paper is organized as follows: \\S\\ref{sec:related} surveys related work on compound compression, KV cache eviction, and phase-aware inference; \\S\\ref{sec:background} formalizes compound sparsity and introduces the Interaction Index; \\S\\ref{sec:experimental-setup} describes our experimental setup; \\S\\ref{sec:experiments} presents the main results; \\S\\ref{sec:analysis} analyzes the entropy-discrimination collapse mechanism; and \\S\\ref{sec:discussion} discusses implications and limitations.\n",
      "numLines": 34,
      "startLine": 1,
      "totalLines": 34
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_01UBTYiWLbYaaEAMLXC5779Y`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "b796e0fe-c406-4d88-b81c-dd592ffe62b8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EdBEMbD3qwr7Lh5TcAKsMH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12180,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12180
      },
      "output_tokens": 22,
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

_source line 11 · 2026-05-14T09:45:09.882Z_

<details><summary>↩ Tool result · `toolu_01UBTYiWLbYaaEAMLXC5779Y`</summary>

```text
1	\section{Related Work}
2	\label{sec:related}
3	
4	\subsection{Compound and Joint Compression}
5	
6	Combining multiple compression axes produces non-additive errors.
7	\cite{spark-aaai2026} report super-additive degradation when combining channel pruning with token eviction, with up to 65\% quality loss exceeding individual component effects---the first explicit measurement of this phenomenon in KV cache sparsity.
8	\cite{slim-icml2025} formalize compound error for quantization and sparsity, deriving an invertible saliency function for low-rank compensation and confirming that aggregated error is strictly non-additive.
9	\cite{unicomp-2026} evaluate compound compression across 40+ benchmarks, revealing that reasoning and multilingual capabilities degrade disproportionately relative to factual recall.
10	The order of compression stages is itself consequential: \cite{compression-ordering-2025} show that early quantization causes irreversible information loss, making P$\to$KD$\to$Q strictly preferable.
11	At a more fundamental level, \cite{phase-transition-compression-2026} characterize independent phase transition points per compression dimension, implying that the joint safe region is the intersection---not the union---of per-dimension safe zones.
12	On the structural side, GRASPrune~\cite{graspune-acl2026} learns global budget-constrained gates to jointly prune FFN channels and attention heads, but treats the pruning decision as static across generation.
13	These works establish that compound interaction produces non-additive errors, but share an implicit assumption: the interaction magnitude is either constant across the generation process or varies only by task---not by reasoning phase or eviction strategy.
14	How compound severity shifts across reasoning phases within a single generation remains unexamined.
15	
16	\subsection{KV Cache Eviction}
17	
18	Most eviction methods rely on importance scoring, yet accumulating evidence questions its reliability.
19	Ada-KV~\cite{adakv-neurips2025} introduce per-head adaptive budget allocation, outperforming uniform distribution but assuming stable importance across generation.
20	SnapKV~\cite{snapkv-neurips2024} identifies important KV positions per head from an observation window at the end of the prompt, compressing the cache before generation begins---effective for long contexts but committing to a fixed importance snapshot that cannot adapt across reasoning phases.
21	\cite{defensivekv-iclr2026} show that standard mean-based importance aggregation is fragile, with worst-case quality loss 2.3--4.3$\times$ higher than expected; their defensive aggregation mitigates but does not eliminate the instability.
22	\cite{nacl-acl2024} combine proxy-token eviction with random eviction to counteract attention bias, improving robustness over pure importance-based methods; yet the eviction policy remains uniform throughout generation.
23	\cite{obcache-2025} derive a second-order joint K-V saliency score from optimal brain damage theory, establishing that key pruning impacts quality more than value pruning---a useful asymmetry, though the score remains time-invariant.
24	\cite{mustafar-neurips2025} achieve 70\% unstructured KV sparsity through per-token magnitude pruning without quality loss, demonstrating that fine-grained within-entry sparsity and coarse token eviction are complementary axes.
25	RetentiveKV~\cite{retentivekv-2026} identifies \emph{deferred importance}: tokens with low initial salience can become pivotal later, undermining single-snapshot importance estimates.
26	\cite{greedy-bias-kvcache-2026} further show that any single importance metric exhibits greedy bias, systematically missing structurally relevant tokens.
27	A recurring theme is that importance estimates become unreliable under specific conditions, but these conditions are characterized in terms of aggregation functions or metric choice---not the reasoning phase during which eviction occurs, nor the interaction with concurrent head pruning.
28	
29	\subsection{Phase-Aware Inference}
30	
31	Several concurrent works introduce phase-awareness into LLM inference.
32	ThinKV~\cite{thinkv-iclr2026} partitions generation into phases and applies different KV cache strategies per phase, achieving strong single-axis results that motivate our phase decomposition---but without compound interaction.
33	\cite{pagedeviction-eacl2026} manage block-wise eviction with separate prefill and decode policies, a coarse two-phase scheme that does not extend to within-generation reasoning phases.
34	\cite{decision-repr-transition-2026} discover that layer pruning sensitivity depends on whether a layer operates in the ``silent'' or ``decisive'' phase of representation formation, with silent-phase pruning causing collapse---direct evidence that compression tolerance is phase-modulated.
35	\cite{doing-more-with-less-2026} provide sign reversal evidence: unstructured pruning combined with test-time scaling can exceed unpruned baselines, suggesting that sparsity interacts constructively with extended reasoning under certain conditions.
36	\cite{raas-acl2025} report non-monotonic token importance across decoding steps, and \cite{sparse-frontier-2025} find no universally optimal sparse attention strategy across tasks and generation stages.
37	
38	These works establish that compression tolerance is phase-dependent, but each examines either phase-aware compression along a single axis or compound compression without phase conditioning.
39	Our work bridges this gap by quantifying how compound sparsity severity varies across reasoning phases and how this variation is modulated by eviction strategy---specifically, the phase-dependent severity gradient that distinguishes importance-based eviction from random baselines in compound settings.
40	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "0086ba20-317f-46ce-bbb2-63c5bed49774",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related}\n\n\\subsection{Compound and Joint Compression}\n\nCombining multiple compression axes produces non-additive errors.\n\\cite{spark-aaai2026} report super-additive degradation when combining channel pruning with token eviction, with up to 65\\% quality loss exceeding individual component effects---the first explicit measurement of this phenomenon in KV cache sparsity.\n\\cite{slim-icml2025} formalize compound error for quantization and sparsity, deriving an invertible saliency function for low-rank compensation and confirming that aggregated error is strictly non-additive.\n\\cite{unicomp-2026} evaluate compound compression across 40+ benchmarks, revealing that reasoning and multilingual capabilities degrade disproportionately relative to factual recall.\nThe order of compression stages is itself consequential: \\cite{compression-ordering-2025} show that early quantization causes irreversible information loss, making P$\\to$KD$\\to$Q strictly preferable.\nAt a more fundamental level, \\cite{phase-transition-compression-2026} characterize independent phase transition points per compression dimension, implying that the joint safe region is the intersection---not the union---of per-dimension safe zones.\nOn the structural side, GRASPrune~\\cite{graspune-acl2026} learns global budget-constrained gates to jointly prune FFN channels and attention heads, but treats the pruning decision as static across generation.\nThese works establish that compound interaction produces non-additive errors, but share an implicit assumption: the interaction magnitude is either constant across the generation process or varies only by task---not by reasoning phase or eviction strategy.\nHow compound severity shifts across reasoning phases within a single generation remains unexamined.\n\n\\subsection{KV Cache Eviction}\n\nMost eviction methods rely on importance scoring, yet accumulating evidence questions its reliability.\nAda-KV~\\cite{adakv-neurips2025} introduce per-head adaptive budget allocation, outperforming uniform distribution but assuming stable importance across generation.\nSnapKV~\\cite{snapkv-neurips2024} identifies important KV positions per head from an observation window at the end of the prompt, compressing the cache before generation begins---effective for long contexts but committing to a fixed importance snapshot that cannot adapt across reasoning phases.\n\\cite{defensivekv-iclr2026} show that standard mean-based importance aggregation is fragile, with worst-case quality loss 2.3--4.3$\\times$ higher than expected; their defensive aggregation mitigates but does not eliminate the instability.\n\\cite{nacl-acl2024} combine proxy-token eviction with random eviction to counteract attention bias, improving robustness over pure importance-based methods; yet the eviction policy remains uniform throughout generation.\n\\cite{obcache-2025} derive a second-order joint K-V saliency score from optimal brain damage theory, establishing that key pruning impacts quality more than value pruning---a useful asymmetry, though the score remains time-invariant.\n\\cite{mustafar-neurips2025} achieve 70\\% unstructured KV sparsity through per-token magnitude pruning without quality loss, demonstrating that fine-grained within-entry sparsity and coarse token eviction are complementary axes.\nRetentiveKV~\\cite{retentivekv-2026} identifies \\emph{deferred importance}: tokens with low initial salience can become pivotal later, undermining single-snapshot importance estimates.\n\\cite{greedy-bias-kvcache-2026} further show that any single importance metric exhibits greedy bias, systematically missing structurally relevant tokens.\nA recurring theme is that importance estimates become unreliable under specific conditions, but these conditions are characterized in terms of aggregation functions or metric choice---not the reasoning phase during which eviction occurs, nor the interaction with concurrent head pruning.\n\n\\subsection{Phase-Aware Inference}\n\nSeveral concurrent works introduce phase-awareness into LLM inference.\nThinKV~\\cite{thinkv-iclr2026} partitions generation into phases and applies different KV cache strategies per phase, achieving strong single-axis results that motivate our phase decomposition---but without compound interaction.\n\\cite{pagedeviction-eacl2026} manage block-wise eviction with separate prefill and decode policies, a coarse two-phase scheme that does not extend to within-generation reasoning phases.\n\\cite{decision-repr-transition-2026} discover that layer pruning sensitivity depends on whether a layer operates in the ``silent'' or ``decisive'' phase of representation formation, with silent-phase pruning causing collapse---direct evidence that compression tolerance is phase-modulated.\n\\cite{doing-more-with-less-2026} provide sign reversal evidence: unstructured pruning combined with test-time scaling can exceed unpruned baselines, suggesting that sparsity interacts constructively with extended reasoning under certain conditions.\n\\cite{raas-acl2025} report non-monotonic token importance across decoding steps, and \\cite{sparse-frontier-2025} find no universally optimal sparse attention strategy across tasks and generation stages.\n\nThese works establish that compression tolerance is phase-dependent, but each examines either phase-aware compression along a single axis or compound compression without phase conditioning.\nOur work bridges this gap by quantifying how compound sparsity severity varies across reasoning phases and how this variation is modulated by eviction strategy---specifically, the phase-dependent severity gradient that distinguishes importance-based eviction from random baselines in compound settings.\n",
      "numLines": 40,
      "startLine": 1,
      "totalLines": 40
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_01RF6zXDDtvrWiPj1EnUQ4j4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "e2d4b28d-5e2f-4b4c-ba90-705b8f17ddd2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EdBEMbD3qwr7Lh5TcAKsMH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12180,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12180
      },
      "output_tokens": 22,
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

_source line 13 · 2026-05-14T09:45:10.452Z_

<details><summary>↩ Tool result · `toolu_01RF6zXDDtvrWiPj1EnUQ4j4`</summary>

```text
1	% Section 3: Background and Problem Setup
2	% Note: eq:ii and eq:gradient are the canonical definitions.
3	% Methodology.tex should reference these via \eqref rather than redefining.
4	
5	\section{Background and Problem Setup}
6	\label{sec:background}
7	
8	We formalize compound sparsity as the simultaneous application of attention head pruning and KV cache eviction, define the Interaction Index to quantify their non-additive coupling, and introduce phase segmentation to localize the analysis across reasoning stages.
9	
10	\subsection{Compound Sparsity Formulation}
11	\label{sec:compound-sparsity}
12	
13	Consider a Transformer language model with $L$ layers, each containing $H$ attention heads.
14	Let $s \in (0,1)$ denote a unified sparsity budget applied to both compression axes.
15	
16	\paragraph{Attention head pruning.}
17	For each layer $\ell$, heads are ranked by Frobenius norm importance $w_j^{(\ell)} = \|\mathbf{A}_j^{(\ell)}\|_F$, where $\mathbf{A}_j^{(\ell)} \in \mathbb{R}^{T \times T}$ is the attention matrix for head $j$ \cite{voita2019heads, michel2019sixteen}.
18	A binary mask $m_j^{(\ell)} \in \{0,1\}$ retains the top-$(1{-}s)\cdot H$ heads, zeroing the output of pruned heads:
19	\begin{equation}
20	    \tilde{\mathbf{o}}_j^{(\ell)} = m_j^{(\ell)} \cdot \mathbf{o}_j^{(\ell)}.
21	    \label{eq:head-mask}
22	\end{equation}
23	
24	\paragraph{KV cache eviction.}
25	For a sequence of length $T$, a position mask $\mathbf{m}_k \in \{0,1\}^T$ retains the top-$(1{-}s)\cdot T$ positions, with the BOS token always preserved.
26	Evicted positions are blocked via attention masking:
27	\begin{equation}
28	    \tilde{a}_{ij} = a_{ij} \cdot m_{k,j}, \quad \forall\, i, j.
29	    \label{eq:kv-mask}
30	\end{equation}
31	We compare two strategies for constructing $\mathbf{m}_k$:
32	\begin{itemize}[nosep,leftmargin=*]
33	    \item \textbf{Importance-based:} Each position $j$ is scored by its cumulative attention mass with position normalization:
34	    \begin{equation}
35	        \mathrm{imp}(j) = \frac{\sum_{\ell, h, i} a_{ij}^{(\ell,h)}}{T - j},
36	        \label{eq:kv-importance}
37	    \end{equation}
38	    where the denominator compensates for causal bias---earlier positions are attended to by more queries \cite{thinkv-iclr2026, defensivekv-iclr2026}.
39	    \item \textbf{Random:} Positions (excluding BOS) are evicted uniformly at random.
40	\end{itemize}
41	
42	\paragraph{Compound sparsity.}
43	Applying both mechanisms simultaneously at sparsity level $s$ (pruning fraction $p = s$, eviction fraction $q = s$) yields \emph{compound sparsity}.
44	The two axes are not independent: head pruning redistributes attention mass among surviving heads, which alters the importance ranking used for KV cache eviction.
45	Prior analyses of compound compression \cite{spark-aaai2026} report that the joint effect is generally super-additive but treat the interaction magnitude as a fixed property of $s$.
46	We investigate whether the eviction strategy and reasoning phase introduce additional structure.
47	
48	\subsection{Interaction Index}
49	\label{sec:interaction-index}
50	
51	To quantify the interaction between head pruning and KV cache eviction, we define the \emph{Interaction Index} (II) following the factorial interaction framework from experimental design.
52	
53	For a given text segment, let $\text{PPL}_d$, $\text{PPL}_a$, $\text{PPL}_k$, and $\text{PPL}_b$ denote the perplexity under the dense (no sparsity), attention-pruning-only, KV-eviction-only, and compound conditions, respectively.
54	Perplexity is computed as $\text{PPL} = \exp\!\bigl(\frac{1}{|S|}\sum_{t \in S} \mathcal{L}_t\bigr)$, where $\mathcal{L}_t$ is the per-token cross-entropy loss over evaluated positions $S$.
55	Normalizing by the dense baseline yields relative degradation ratios $r_c = \text{PPL}_c\,/\,\text{PPL}_d$ for $c \in \{a, k, b\}$, and the Interaction Index:
56	\begin{equation}
57	    \mathrm{II} = r_b - r_a - r_k + 1.
58	    \label{eq:ii}
59	\end{equation}
60	
61	Under additive independence, $r_b \approx r_a + r_k - 1$, yielding $\mathrm{II} \approx 0$.
62	The sign of II determines the interaction regime:
63	\begin{itemize}[nosep,leftmargin=*]
64	    \item $\mathrm{II} > 0$: \textbf{super-additive}---compound degradation exceeds the sum of individual effects.
65	    \item $\mathrm{II} < 0$: \textbf{sub-additive}---the compound effect is less than the sum of parts.
66	    \item $\mathrm{II} = 0$: \textbf{additive}---the two mechanisms do not interact.
67	\end{itemize}
68	
69	\paragraph{Choice of additive null.}
70	Equation~\ref{eq:ii} posits an additive null $r_b = r_a + r_k - 1$ rather than multiplicative independence $r_b = r_a \cdot r_k$.
71	We adopt the additive form because head pruning and KV cache eviction operate on disjoint model dimensions---structural (which heads to retain) versus positional (which tokens to cache)---so their degradations sum rather than multiply at the sparsity levels we study ($s \leq 0.30$).
72	We verify in Appendix~\ref{app:multiplicative-null} that qualitative conclusions are unchanged under the multiplicative null.
73	
74	Normalizing by $\text{PPL}_d$ ensures cross-problem comparability.
75	Because the II distribution is heavily right-skewed, we report medians as the central tendency.
76	
77	\paragraph{Severity gradient.}
78	To capture how II varies across reasoning phases (defined in \S\ref{sec:phase-segmentation}), we define the \emph{severity gradient}:
79	\begin{equation}
80	    G = \frac{\widetilde{\mathrm{II}}_{\,\textit{low}}}{\widetilde{\mathrm{II}}_{\,\textit{high}}},
81	    \label{eq:gradient}
82	\end{equation}
83	where $\widetilde{\mathrm{II}}_{\,\textit{low}}$ and $\widetilde{\mathrm{II}}_{\,\textit{high}}$ are the median interaction indices in the low-sparsity and high-sparsity phases, respectively.
84	$G \gg 1$ indicates that compound interaction concentrates in low-sparsity phases; $G \approx 1$ indicates phase-invariant degradation.
85	When $\widetilde{\mathrm{II}}_{\,\textit{high}} < \varepsilon$ for a small threshold $\varepsilon > 0$, we report $G = \infty$.
86	
87	\subsection{Phase Segmentation}
88	\label{sec:phase-segmentation}
89	
90	Reasoning-capable LLMs produce token sequences with heterogeneous attention structure: some positions exhibit highly concentrated attention over a few key tokens, while others distribute attention broadly across the context.
91	We partition each generated sequence into three phases based on the local \emph{attention sparsity profile}, adapting the phase-aware methodology of ThinKV \cite{thinkv-iclr2026}.
92	
93	\paragraph{Attention sparsity.}
94	For each query position $i$ and head $h$, we compute the fraction of key positions receiving negligible attention:
95	\begin{equation}
96	    \sigma_i^{(h)} = \frac{1}{T} \sum_{j=1}^{T} \mathbf{1}\!\left[a_{ij}^{(h)} < 0.01 \cdot \max_k a_{ik}^{(h)}\right].
97	    \label{eq:attn-sparsity}
98	\end{equation}
99	The per-position sparsity $\sigma_i = \frac{1}{H}\sum_h \sigma_i^{(h)}$ averages across all heads.
100	
101	\paragraph{Quantile-based segmentation.}
102	Tokens are partitioned into three groups by the tercile boundaries of $\{\sigma_i\}_{i=1}^{T}$:
103	\begin{itemize}[nosep,leftmargin=*]
104	    \item \textbf{High-sparsity phase} (top tercile of $\sigma$): attention concentrates on few tokens; heads are largely redundant, making both pruning and eviction relatively benign.
105	    \item \textbf{Mid-sparsity phase} (middle tercile): intermediate attention patterns.
106	    \item \textbf{Low-sparsity phase} (bottom tercile of $\sigma$): attention distributes broadly; each surviving head carries non-redundant information, making both pruning and eviction more destructive.
107	\end{itemize}
108	Contiguous segments shorter than $\texttt{min\_phase\_length} = 10$ tokens are merged into adjacent phases to ensure sufficient tokens for stable perplexity estimation.
109	The segmentation is purely data-driven and requires only access to attention weights.
110	
111	This phase structure arises naturally during extended chain-of-thought reasoning, where the model alternates between focused retrieval of specific facts (high sparsity) and integrative reasoning across many context positions (low sparsity) \cite{phase-transition-compression-2026}.
112	Our central research question is: \emph{Is the Interaction Index constant across phases and eviction strategies, or does it exhibit a phase $\times$ strategy interaction?}
113	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "da0477a5-0b4c-49a9-8121-d83de6588135",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex",
      "content": "% Section 3: Background and Problem Setup\n% Note: eq:ii and eq:gradient are the canonical definitions.\n% Methodology.tex should reference these via \\eqref rather than redefining.\n\n\\section{Background and Problem Setup}\n\\label{sec:background}\n\nWe formalize compound sparsity as the simultaneous application of attention head pruning and KV cache eviction, define the Interaction Index to quantify their non-additive coupling, and introduce phase segmentation to localize the analysis across reasoning stages.\n\n\\subsection{Compound Sparsity Formulation}\n\\label{sec:compound-sparsity}\n\nConsider a Transformer language model with $L$ layers, each containing $H$ attention heads.\nLet $s \\in (0,1)$ denote a unified sparsity budget applied to both compression axes.\n\n\\paragraph{Attention head pruning.}\nFor each layer $\\ell$, heads are ranked by Frobenius norm importance $w_j^{(\\ell)} = \\|\\mathbf{A}_j^{(\\ell)}\\|_F$, where $\\mathbf{A}_j^{(\\ell)} \\in \\mathbb{R}^{T \\times T}$ is the attention matrix for head $j$ \\cite{voita2019heads, michel2019sixteen}.\nA binary mask $m_j^{(\\ell)} \\in \\{0,1\\}$ retains the top-$(1{-}s)\\cdot H$ heads, zeroing the output of pruned heads:\n\\begin{equation}\n    \\tilde{\\mathbf{o}}_j^{(\\ell)} = m_j^{(\\ell)} \\cdot \\mathbf{o}_j^{(\\ell)}.\n    \\label{eq:head-mask}\n\\end{equation}\n\n\\paragraph{KV cache eviction.}\nFor a sequence of length $T$, a position mask $\\mathbf{m}_k \\in \\{0,1\\}^T$ retains the top-$(1{-}s)\\cdot T$ positions, with the BOS token always preserved.\nEvicted positions are blocked via attention masking:\n\\begin{equation}\n    \\tilde{a}_{ij} = a_{ij} \\cdot m_{k,j}, \\quad \\forall\\, i, j.\n    \\label{eq:kv-mask}\n\\end{equation}\nWe compare two strategies for constructing $\\mathbf{m}_k$:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{Importance-based:} Each position $j$ is scored by its cumulative attention mass with position normalization:\n    \\begin{equation}\n        \\mathrm{imp}(j) = \\frac{\\sum_{\\ell, h, i} a_{ij}^{(\\ell,h)}}{T - j},\n        \\label{eq:kv-importance}\n    \\end{equation}\n    where the denominator compensates for causal bias---earlier positions are attended to by more queries \\cite{thinkv-iclr2026, defensivekv-iclr2026}.\n    \\item \\textbf{Random:} Positions (excluding BOS) are evicted uniformly at random.\n\\end{itemize}\n\n\\paragraph{Compound sparsity.}\nApplying both mechanisms simultaneously at sparsity level $s$ (pruning fraction $p = s$, eviction fraction $q = s$) yields \\emph{compound sparsity}.\nThe two axes are not independent: head pruning redistributes attention mass among surviving heads, which alters the importance ranking used for KV cache eviction.\nPrior analyses of compound compression \\cite{spark-aaai2026} report that the joint effect is generally super-additive but treat the interaction magnitude as a fixed property of $s$.\nWe investigate whether the eviction strategy and reasoning phase introduce additional structure.\n\n\\subsection{Interaction Index}\n\\label{sec:interaction-index}\n\nTo quantify the interaction between head pruning and KV cache eviction, we define the \\emph{Interaction Index} (II) following the factorial interaction framework from experimental design.\n\nFor a given text segment, let $\\text{PPL}_d$, $\\text{PPL}_a$, $\\text{PPL}_k$, and $\\text{PPL}_b$ denote the perplexity under the dense (no sparsity), attention-pruning-only, KV-eviction-only, and compound conditions, respectively.\nPerplexity is computed as $\\text{PPL} = \\exp\\!\\bigl(\\frac{1}{|S|}\\sum_{t \\in S} \\mathcal{L}_t\\bigr)$, where $\\mathcal{L}_t$ is the per-token cross-entropy loss over evaluated positions $S$.\nNormalizing by the dense baseline yields relative degradation ratios $r_c = \\text{PPL}_c\\,/\\,\\text{PPL}_d$ for $c \\in \\{a, k, b\\}$, and the Interaction Index:\n\\begin{equation}\n    \\mathrm{II} = r_b - r_a - r_k + 1.\n    \\label{eq:ii}\n\\end{equation}\n\nUnder additive independence, $r_b \\approx r_a + r_k - 1$, yielding $\\mathrm{II} \\approx 0$.\nThe sign of II determines the interaction regime:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item $\\mathrm{II} > 0$: \\textbf{super-additive}---compound degradation exceeds the sum of individual effects.\n    \\item $\\mathrm{II} < 0$: \\textbf{sub-additive}---the compound effect is less than the sum of parts.\n    \\item $\\mathrm{II} = 0$: \\textbf{additive}---the two mechanisms do not interact.\n\\end{itemize}\n\n\\paragraph{Choice of additive null.}\nEquation~\\ref{eq:ii} posits an additive null $r_b = r_a + r_k - 1$ rather than multiplicative independence $r_b = r_a \\cdot r_k$.\nWe adopt the additive form because head pruning and KV cache eviction operate on disjoint model dimensions---structural (which heads to retain) versus positional (which tokens to cache)---so their degradations sum rather than multiply at the sparsity levels we study ($s \\leq 0.30$).\nWe verify in Appendix~\\ref{app:multiplicative-null} that qualitative conclusions are unchanged under the multiplicative null.\n\nNormalizing by $\\text{PPL}_d$ ensures cross-problem comparability.\nBecause the II distribution is heavily right-skewed, we report medians as the central tendency.\n\n\\paragraph{Severity gradient.}\nTo capture how II varies across reasoning phases (defined in \\S\\ref{sec:phase-segmentation}), we define the \\emph{severity gradient}:\n\\begin{equation}\n    G = \\frac{\\widetilde{\\mathrm{II}}_{\\,\\textit{low}}}{\\widetilde{\\mathrm{II}}_{\\,\\textit{high}}},\n    \\label{eq:gradient}\n\\end{equation}\nwhere $\\widetilde{\\mathrm{II}}_{\\,\\textit{low}}$ and $\\widetilde{\\mathrm{II}}_{\\,\\textit{high}}$ are the median interaction indices in the low-sparsity and high-sparsity phases, respectively.\n$G \\gg 1$ indicates that compound interaction concentrates in low-sparsity phases; $G \\approx 1$ indicates phase-invariant degradation.\nWhen $\\widetilde{\\mathrm{II}}_{\\,\\textit{high}} < \\varepsilon$ for a small threshold $\\varepsilon > 0$, we report $G = \\infty$.\n\n\\subsection{Phase Segmentation}\n\\label{sec:phase-segmentation}\n\nReasoning-capable LLMs produce token sequences with heterogeneous attention structure: some positions exhibit highly concentrated attention over a few key tokens, while others distribute attention broadly across the context.\nWe partition each generated sequence into three phases based on the local \\emph{attention sparsity profile}, adapting the phase-aware methodology of ThinKV \\cite{thinkv-iclr2026}.\n\n\\paragraph{Attention sparsity.}\nFor each query position $i$ and head $h$, we compute the fraction of key positions receiving negligible attention:\n\\begin{equation}\n    \\sigma_i^{(h)} = \\frac{1}{T} \\sum_{j=1}^{T} \\mathbf{1}\\!\\left[a_{ij}^{(h)} < 0.01 \\cdot \\max_k a_{ik}^{(h)}\\right].\n    \\label{eq:attn-sparsity}\n\\end{equation}\nThe per-position sparsity $\\sigma_i = \\frac{1}{H}\\sum_h \\sigma_i^{(h)}$ averages across all heads.\n\n\\paragraph{Quantile-based segmentation.}\nTokens are partitioned into three groups by the tercile boundaries of $\\{\\sigma_i\\}_{i=1}^{T}$:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{High-sparsity phase} (top tercile of $\\sigma$): attention concentrates on few tokens; heads are largely redundant, making both pruning and eviction relatively benign.\n    \\item \\textbf{Mid-sparsity phase} (middle tercile): intermediate attention patterns.\n    \\item \\textbf{Low-sparsity phase} (bottom tercile of $\\sigma$): attention distributes broadly; each surviving head carries non-redundant information, making both pruning and eviction more destructive.\n\\end{itemize}\nContiguous segments shorter than $\\texttt{min\\_phase\\_length} = 10$ tokens are merged into adjacent phases to ensure sufficient tokens for stable perplexity estimation.\nThe segmentation is purely data-driven and requires only access to attention weights.\n\nThis phase structure arises naturally during extended chain-of-thought reasoning, where the model alternates between focused retrieval of specific facts (high sparsity) and integrative reasoning across many context positions (low sparsity) \\cite{phase-transition-compression-2026}.\nOur central research question is: \\emph{Is the Interaction Index constant across phases and eviction strategies, or does it exhibit a phase $\\times$ strategy interaction?}\n",
      "numLines": 113,
      "startLine": 1,
      "totalLines": 113
    }
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Read · `toolu_015HCYJbmezbn23stHNyCNzk`</summary>

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
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "067cd49a-9179-4cb1-ae6e-fabb054dce51",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EdBEMbD3qwr7Lh5TcAKsMH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12180,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12180
      },
      "output_tokens": 22,
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

_source line 15 · 2026-05-14T09:45:10.843Z_

<details><summary>↩ Tool result · `toolu_015HCYJbmezbn23stHNyCNzk`</summary>

```text
1	\section{Experimental Setup}
2	\label{sec:experimental-setup}
3	
4	\subsection{Models}
5	\label{sec:models}
6	
7	We conduct experiments on two 7B-parameter instruction-tuned models that share the Qwen2 backbone architecture (28 Transformer layers, 28 attention heads with 4-group GQA):
8	
9	\paragraph{DeepSeek-R1-Distill-Qwen-7B} serves as our primary evaluation target. This model was distilled from DeepSeek-R1 \cite{deepseek-r1} and produces explicit chain-of-thought traces delimited by \texttt{&lt;think>}$\cdots$\texttt{&lt;/think>} tags, yielding sequences with pronounced phase structure---extended reasoning followed by a concise solution. The structured generation pattern makes it well-suited for studying how sparsity interacts with distinct reasoning phases.
10	
11	\paragraph{Qwen2.5-7B-Instruct} \cite{qwen2.5} provides a cross-model replication. Although it shares the same backbone family, its instruction tuning does not enforce explicit reasoning delimiters, producing a different distribution of attention sparsity across the generation trajectory. Replication on this model tests whether our findings generalize beyond distillation-induced phase structure.
12	
13	Both models are loaded in \texttt{bfloat16} precision with eager attention (i.e., without FlashAttention) to permit direct manipulation of attention weight matrices during sparsity intervention.\footnote{An earlier \texttt{float16} configuration produced sporadic NaN values in Layer~27 of DeepSeek-R1-Distill-Qwen-7B, affecting ${\sim}$8\% of logit positions. Switching to \texttt{bfloat16} eliminated all NaN occurrences; we additionally apply NaN-guarded filtering as a safety net.}
14	
15	
16	\subsection{Dataset}
17	\label{sec:dataset}
18	
19	We evaluate on a 50-problem stratified subset of the MATH-500 benchmark \cite{math500}, sampling uniformly across problem categories (algebra, geometry, number theory, combinatorics, etc.) with a fixed seed for reproducibility. Mathematical reasoning tasks are a natural testbed for our study: they elicit long chain-of-thought sequences (up to 2048 tokens) in which the model alternates between exploratory reasoning and structured computation---phases that differ markedly in attention sparsity. Each problem is decoded greedily (\texttt{max\_new\_tokens}$=$2048) to eliminate sampling variance.
20	
21	
22	\subsection{Compound Sparsity Configuration}
23	\label{sec:sparsity-config}
24	
25	We apply \emph{symmetric} compound sparsity: for a given sparsity level $s$, we prune the same fraction $s$ of attention heads and evict the same fraction $s$ of KV cache entries. We evaluate four sparsity levels $s \in \{0.15, 0.20, 0.25, 0.30\}$, spanning from mild to aggressive compression.
26	
27	\paragraph{Sparsity conditions.} For each problem and each sparsity level, we compute perplexity under four conditions: (i)~\emph{dense}---no intervention; (ii)~\emph{attn-only}---head pruning without KV eviction; (iii)~\emph{kv-only}---KV eviction without head pruning; and (iv)~\emph{both}---simultaneous head pruning and KV eviction.
28	
29	\paragraph{Eviction strategies.} We compare two KV cache eviction strategies:
30	
31	\begin{itemize}[nosep,leftmargin=*]
32	\item \textbf{Importance-based.} Each KV position receives a score equal to its cumulative attention weight summed over all query positions and heads. To correct for the inherent causal bias---earlier positions accumulate more attention simply because they are attended to by more queries---we apply position normalization:
33	\begin{equation}
34	\label{eq:importance}
35	    \alpha_j = \frac{\sum_{i,h} a_{i,h,j}}{\texttt{seq\_len} - j}, \quad j \in \{1, \dots, T\},
36	\end{equation}
37	where $a_{i,h,j}$ is the attention weight from query~$i$, head~$h$ to key~$j$, and the denominator counts the number of queries that can attend to position~$j$ under causal masking. Position~0 (BOS) is always retained. The $T \cdot s$ positions with the lowest normalized scores are evicted.
38	
39	During masked forward passes, we guard against numerical instability from the interaction of head masking and KV eviction: zeroed-out heads that would otherwise produce $\infty \times 0 = \text{NaN}$ are handled via selective replacement (\texttt{torch.where}) prior to the softmax, and any layer producing NaN outputs is skipped from the sparsity loss computation.
40	
41	\item \textbf{Random.} KV positions (excluding BOS) are evicted uniformly at random, providing a strategy-agnostic baseline. Head pruning under the random condition selects heads via \texttt{torch.randperm} rather than by importance.
42	\end{itemize}
43	
44	\paragraph{Head pruning.} Under importance-based eviction, heads are ranked by their Frobenius norm across the full attention matrix $\mathbf{A}_\ell \in \mathbb{R}^{H \times T \times T}$ per layer $\ell$, and the bottom-$s$ fraction is masked. Under random eviction, heads are selected uniformly at random.
45	
46	
47	\subsection{Phase Segmentation}
48	\label{sec:phase-seg}
49	
50	We segment each generated sequence into three \emph{reasoning phases} based on the local attention sparsity of each token position. For each query position $i$, we compute per-head sparsity as the fraction of attention weights falling below $0.01 \times \max_j a_{i,h,j}$, then average across heads to obtain a scalar sparsity value per position. The resulting sparsity trajectory is partitioned into terciles via quantile boundaries: \emph{low-sparsity} (bottom third, corresponding to diffuse attention during exploratory reasoning), \emph{mid-sparsity}, and \emph{high-sparsity} (top third, corresponding to focused attention during structured computation). Contiguous segments shorter than $\texttt{min\_phase\_length}=10$ tokens are merged into adjacent phases to suppress noise.
51	
52	
53	\subsection{Metrics}
54	\label{sec:metrics}
55	
56	\paragraph{Perplexity.} For each sparsity condition $c \in \{d, a, k, b\}$ and each phase, we compute segment-level perplexity as
57	$\text{PPL}_c = \exp\!\bigl(\tfrac{1}{|I|}\sum_{i \in I} \mathcal{L}_c(x_i)\bigr)$,
58	where $I$ is the set of token indices belonging to the phase and $\mathcal{L}_c(x_i)$ is the per-token cross-entropy loss under condition $c$.
59	
60	\paragraph{Interaction Index.} The interaction index quantifies the synergistic (super-additive) effect of compound sparsity beyond the sum of individual interventions:
61	\begin{equation}
62	\label{eq:ii}
63	    \mathrm{II} = \frac{\text{PPL}_b}{\text{PPL}_d} - \frac{\text{PPL}_a}{\text{PPL}_d} - \frac{\text{PPL}_k}{\text{PPL}_d} + 1.
64	\end{equation}
65	When $\mathrm{II} > 0$, the two sparsity mechanisms amplify each other; $\mathrm{II} = 0$ indicates additive (independent) degradation.
66	
67	\paragraph{Severity Gradient.} To measure how the interaction varies across reasoning phases, we define the severity gradient:
68	\begin{equation}
69	\label{eq:gradient}
70	    G = \frac{\widetilde{\mathrm{II}}_{\,\textit{low}}}{\widetilde{\mathrm{II}}_{\,\textit{high}}},
71	\end{equation}
72	where $\widetilde{\mathrm{II}}_{\,\textit{low}}$ and $\widetilde{\mathrm{II}}_{\,\textit{high}}$ are the median interaction indices over the low-sparsity and high-sparsity phases, respectively. We report medians rather than means because the II distribution is heavily right-skewed (mean/median ratios up to 43:1 at $s{=}0.30$), making the median a more robust central tendency estimator.
73	
74	
75	\subsection{Statistical Analysis}
76	\label{sec:stats}
77	
78	All confidence intervals and significance tests are computed via the nonparametric bootstrap with $B = 10{,}000$ resamples \cite{efron1993bootstrap}.
79	
80	\paragraph{Per-problem bootstrap.} For each sparsity level and strategy, we resample the 50 per-problem II values with replacement and compute the mean of each resample, yielding a 95\% percentile confidence interval for the population mean II.
81	
82	\paragraph{Paired bootstrap.} To test whether the severity gradient differs between importance-based and random eviction, we pair observations by problem (same problem, same sparsity level) and bootstrap the difference in gradients. This controls for problem-level variance in difficulty and sequence length.
83	
84	\paragraph{Unpaired bootstrap.} We additionally compute per-strategy gradient confidence intervals without pairing, to verify that the importance-based gradient is significantly greater than 1 (i.e., phase modulation exists) independently of the random baseline.
85	
86	All tests yield $p < 0.0001$ at every sparsity level, confirming that the observed phase--strategy interactions are not artifacts of sampling variability.\footnote{Experiments were conducted on a server with 4$\times$ NVIDIA RTX PRO 6000 Blackwell Server Edition 96\,GB GPUs, with one model--sparsity configuration per GPU.}
87	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "0256bacc-1a7a-4b18-9670-d75e43247509",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex",
      "content": "\\section{Experimental Setup}\n\\label{sec:experimental-setup}\n\n\\subsection{Models}\n\\label{sec:models}\n\nWe conduct experiments on two 7B-parameter instruction-tuned models that share the Qwen2 backbone architecture (28 Transformer layers, 28 attention heads with 4-group GQA):\n\n\\paragraph{DeepSeek-R1-Distill-Qwen-7B} serves as our primary evaluation target. This model was distilled from DeepSeek-R1 \\cite{deepseek-r1} and produces explicit chain-of-thought traces delimited by \\texttt{&lt;think>}$\\cdots$\\texttt{&lt;/think>} tags, yielding sequences with pronounced phase structure---extended reasoning followed by a concise solution. The structured generation pattern makes it well-suited for studying how sparsity interacts with distinct reasoning phases.\n\n\\paragraph{Qwen2.5-7B-Instruct} \\cite{qwen2.5} provides a cross-model replication. Although it shares the same backbone family, its instruction tuning does not enforce explicit reasoning delimiters, producing a different distribution of attention sparsity across the generation trajectory. Replication on this model tests whether our findings generalize beyond distillation-induced phase structure.\n\nBoth models are loaded in \\texttt{bfloat16} precision with eager attention (i.e., without FlashAttention) to permit direct manipulation of attention weight matrices during sparsity intervention.\\footnote{An earlier \\texttt{float16} configuration produced sporadic NaN values in Layer~27 of DeepSeek-R1-Distill-Qwen-7B, affecting ${\\sim}$8\\% of logit positions. Switching to \\texttt{bfloat16} eliminated all NaN occurrences; we additionally apply NaN-guarded filtering as a safety net.}\n\n\n\\subsection{Dataset}\n\\label{sec:dataset}\n\nWe evaluate on a 50-problem stratified subset of the MATH-500 benchmark \\cite{math500}, sampling uniformly across problem categories (algebra, geometry, number theory, combinatorics, etc.) with a fixed seed for reproducibility. Mathematical reasoning tasks are a natural testbed for our study: they elicit long chain-of-thought sequences (up to 2048 tokens) in which the model alternates between exploratory reasoning and structured computation---phases that differ markedly in attention sparsity. Each problem is decoded greedily (\\texttt{max\\_new\\_tokens}$=$2048) to eliminate sampling variance.\n\n\n\\subsection{Compound Sparsity Configuration}\n\\label{sec:sparsity-config}\n\nWe apply \\emph{symmetric} compound sparsity: for a given sparsity level $s$, we prune the same fraction $s$ of attention heads and evict the same fraction $s$ of KV cache entries. We evaluate four sparsity levels $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$, spanning from mild to aggressive compression.\n\n\\paragraph{Sparsity conditions.} For each problem and each sparsity level, we compute perplexity under four conditions: (i)~\\emph{dense}---no intervention; (ii)~\\emph{attn-only}---head pruning without KV eviction; (iii)~\\emph{kv-only}---KV eviction without head pruning; and (iv)~\\emph{both}---simultaneous head pruning and KV eviction.\n\n\\paragraph{Eviction strategies.} We compare two KV cache eviction strategies:\n\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\textbf{Importance-based.} Each KV position receives a score equal to its cumulative attention weight summed over all query positions and heads. To correct for the inherent causal bias---earlier positions accumulate more attention simply because they are attended to by more queries---we apply position normalization:\n\\begin{equation}\n\\label{eq:importance}\n    \\alpha_j = \\frac{\\sum_{i,h} a_{i,h,j}}{\\texttt{seq\\_len} - j}, \\quad j \\in \\{1, \\dots, T\\},\n\\end{equation}\nwhere $a_{i,h,j}$ is the attention weight from query~$i$, head~$h$ to key~$j$, and the denominator counts the number of queries that can attend to position~$j$ under causal masking. Position~0 (BOS) is always retained. The $T \\cdot s$ positions with the lowest normalized scores are evicted.\n\nDuring masked forward passes, we guard against numerical instability from the interaction of head masking and KV eviction: zeroed-out heads that would otherwise produce $\\infty \\times 0 = \\text{NaN}$ are handled via selective replacement (\\texttt{torch.where}) prior to the softmax, and any layer producing NaN outputs is skipped from the sparsity loss computation.\n\n\\item \\textbf{Random.} KV positions (excluding BOS) are evicted uniformly at random, providing a strategy-agnostic baseline. Head pruning under the random condition selects heads via \\texttt{torch.randperm} rather than by importance.\n\\end{itemize}\n\n\\paragraph{Head pruning.} Under importance-based eviction, heads are ranked by their Frobenius norm across the full attention matrix $\\mathbf{A}_\\ell \\in \\mathbb{R}^{H \\times T \\times T}$ per layer $\\ell$, and the bottom-$s$ fraction is masked. Under random eviction, heads are selected uniformly at random.\n\n\n\\subsection{Phase Segmentation}\n\\label{sec:phase-seg}\n\nWe segment each generated sequence into three \\emph{reasoning phases} based on the local attention sparsity of each token position. For each query position $i$, we compute per-head sparsity as the fraction of attention weights falling below $0.01 \\times \\max_j a_{i,h,j}$, then average across heads to obtain a scalar sparsity value per position. The resulting sparsity trajectory is partitioned into terciles via quantile boundaries: \\emph{low-sparsity} (bottom third, corresponding to diffuse attention during exploratory reasoning), \\emph{mid-sparsity}, and \\emph{high-sparsity} (top third, corresponding to focused attention during structured computation). Contiguous segments shorter than $\\texttt{min\\_phase\\_length}=10$ tokens are merged into adjacent phases to suppress noise.\n\n\n\\subsection{Metrics}\n\\label{sec:metrics}\n\n\\paragraph{Perplexity.} For each sparsity condition $c \\in \\{d, a, k, b\\}$ and each phase, we compute segment-level perplexity as\n$\\text{PPL}_c = \\exp\\!\\bigl(\\tfrac{1}{|I|}\\sum_{i \\in I} \\mathcal{L}_c(x_i)\\bigr)$,\nwhere $I$ is the set of token indices belonging to the phase and $\\mathcal{L}_c(x_i)$ is the per-token cross-entropy loss under condition $c$.\n\n\\paragraph{Interaction Index.} The interaction index quantifies the synergistic (super-additive) effect of compound sparsity beyond the sum of individual interventions:\n\\begin{equation}\n\\label{eq:ii}\n    \\mathrm{II} = \\frac{\\text{PPL}_b}{\\text{PPL}_d} - \\frac{\\text{PPL}_a}{\\text{PPL}_d} - \\frac{\\text{PPL}_k}{\\text{PPL}_d} + 1.\n\\end{equation}\nWhen $\\mathrm{II} > 0$, the two sparsity mechanisms amplify each other; $\\mathrm{II} = 0$ indicates additive (independent) degradation.\n\n\\paragraph{Severity Gradient.} To measure how the interaction varies across reasoning phases, we define the severity gradient:\n\\begin{equation}\n\\label{eq:gradient}\n    G = \\frac{\\widetilde{\\mathrm{II}}_{\\,\\textit{low}}}{\\widetilde{\\mathrm{II}}_{\\,\\textit{high}}},\n\\end{equation}\nwhere $\\widetilde{\\mathrm{II}}_{\\,\\textit{low}}$ and $\\widetilde{\\mathrm{II}}_{\\,\\textit{high}}$ are the median interaction indices over the low-sparsity and high-sparsity phases, respectively. We report medians rather than means because the II distribution is heavily right-skewed (mean/median ratios up to 43:1 at $s{=}0.30$), making the median a more robust central tendency estimator.\n\n\n\\subsection{Statistical Analysis}\n\\label{sec:stats}\n\nAll confidence intervals and significance tests are computed via the nonparametric bootstrap with $B = 10{,}000$ resamples \\cite{efron1993bootstrap}.\n\n\\paragraph{Per-problem bootstrap.} For each sparsity level and strategy, we resample the 50 per-problem II values with replacement and compute the mean of each resample, yielding a 95\\% percentile confidence interval for the population mean II.\n\n\\paragraph{Paired bootstrap.} To test whether the severity gradient differs between importance-based and random eviction, we pair observations by problem (same problem, same sparsity level) and bootstrap the difference in gradients. This controls for problem-level variance in difficulty and sequence length.\n\n\\paragraph{Unpaired bootstrap.} We additionally compute per-strategy gradient confidence intervals without pairing, to verify that the importance-based gradient is significantly greater than 1 (i.e., phase modulation exists) independently of the random baseline.\n\nAll tests yield $p < 0.0001$ at every sparsity level, confirming that the observed phase--strategy interactions are not artifacts of sampling variability.\\footnote{Experiments were conducted on a server with 4$\\times$ NVIDIA RTX PRO 6000 Blackwell Server Edition 96\\,GB GPUs, with one model--sparsity configuration per GPU.}\n",
      "numLines": 87,
      "startLine": 1,
      "totalLines": 87
    }
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Read · `toolu_01Qdj6HgHf5k1crAqsDmm9DT`</summary>

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
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "6ca5f501-c9ce-4bcf-97ba-dd220e0a59a0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EdBEMbD3qwr7Lh5TcAKsMH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12180,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12180
      },
      "output_tokens": 22,
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

_source line 17 · 2026-05-14T09:45:11.797Z_

<details><summary>↩ Tool result · `toolu_01Qdj6HgHf5k1crAqsDmm9DT`</summary>

```text
1	
2	\section{Results}
3	\label{sec:results}
4	
5	We present our empirical findings in five parts: strategy-dependent compound severity (\S\ref{sec:strategy-severity}), phase-modulated amplification (\S\ref{sec:phase-amplification}), the phase-strategy crossover (\S\ref{sec:crossover}), cross-model replication (\S\ref{sec:cross-model}), and statistical validation (\S\ref{sec:stat-validation}).
6	
7	
8	\subsection{Experimental Overview}
9	\label{sec:exp-overview}
10	
11	We evaluate compound sparsity on DeepSeek-R1-Distill-Qwen-7B using a 50-problem stratified subset of MATH-500 (\S\ref{sec:dataset}). For each problem, we measure perplexity under four conditions---dense, attention-only pruning, KV-only eviction, and compound (both)---at sparsity levels $s \in \{0.15, 0.20, 0.25, 0.30\}$. We compare importance-based and random eviction strategies (\S\ref{sec:sparsity-config}), and segment each generated sequence into high-, mid-, and low-sparsity reasoning phases via quantile-based attention sparsity partitioning (\S\ref{sec:phase-seg}). The interaction index (II, Eq.~\ref{eq:ii}) quantifies compound super-additivity, and the severity gradient ($G$, Eq.~\ref{eq:gradient}) captures phase-dependent amplification.
12	Models are evaluated in \texttt{bfloat16} precision (\S\ref{sec:experimental-setup}). Full experimental details appear therein.
13	
14	
15	\subsection{Strategy-Dependent Severity (C1)}
16	\label{sec:strategy-severity}
17	
18	The compound severity difference reveals a stark dependence on eviction strategy. Table~\ref{tab:aggregate-ii} reports the median compound severity difference $\Delta = \widetilde{\mathrm{II}}_{\textit{low}} - \widetilde{\mathrm{II}}_{\textit{high}}$ across 50 problems for each strategy and sparsity level. Under importance-based eviction, compound sparsity produces substantial super-additive degradation that grows with sparsity: $\Delta$ increases from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, a $37{\times}$ amplification. Under random eviction, the severity difference shows no systematic growth, remaining near zero ($-0.02$ to $1.54$). % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json
19	
20	\begin{table}[t]
21	\centering
22	\small
23	\caption{Median compound severity difference ($\Delta = \widetilde{\mathrm{II}}_{\textit{low}} - \widetilde{\mathrm{II}}_{\textit{high}}$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}50$ MATH-500 problems).}
24	\label{tab:aggregate-ii}
25	\begin{tabular}{@{}lcccc@{}}
26	\toprule
27	Strategy & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
28	\midrule
29	Importance & 0.39 & 1.48 & 7.16 & 14.59 \\ % exp_id: bf16_importance_s015..s030; source: experiment_summary_table.json median_diff
30	Random     & 0.01 & $-$0.02 & 0.54 & 1.54 \\ % exp_id: bf16_ds_rand_s015..s030; source: experiment_summary_table.json median_diff
31	\bottomrule
32	\end{tabular}
33	\end{table}
34	
35	This strategy dependence indicates that compound sparsity severity is not an intrinsic property of the compression level. Rather, the same sparsity configuration produces qualitatively different compound behavior depending on the eviction strategy---an emergent phase-strategy interaction whose structure we unpack in the following subsections.
36	
37	
38	\subsection{Phase-Modulated Amplification (C2)}
39	\label{sec:phase-amplification}
40	
41	Decomposing the interaction index by reasoning phase reveals that the strategy-dependent severity observed in \S\ref{sec:strategy-severity} is driven by amplification concentrated in the low-sparsity phase. Table~\ref{tab:main-results} reports per-phase median II and the severity gradient $G$ at each sparsity level.
42	
43	Under importance-based eviction, the severity gradient---the ratio of low-phase to high-phase median II---increases with sparsity from $69{\times}$ at $s{=}0.15$ to $274{\times}$ at $s{=}0.30$. The low-sparsity phase---corresponding to exploratory reasoning with broadly distributed attention---bears disproportionate compound degradation, while the high-sparsity phase---corresponding to structured computation with focused attention---experiences near-zero compound interaction ($\widetilde{\mathrm{II}}_{\textit{high}}$ ranges from $0.006$ to $0.053$). Under random eviction, the gradient remains near unity ($G \approx 0.9$--$1.7{\times}$) at all sparsity levels, confirming that phase modulation is specific to the emergent interaction between head pruning and importance-based scoring. % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json
44	
45	\begin{table}[t]
46	\centering
47	\small
48	\caption{Interaction index (II) by eviction strategy, reasoning phase, and sparsity level. II values are problem-level medians across 50 problems. $\Delta = \widetilde{\mathrm{II}}_{\textit{low}} - \widetilde{\mathrm{II}}_{\textit{high}}$ is the median severity difference. $G = \widetilde{\mathrm{II}}_{\textit{low}} / \widetilde{\mathrm{II}}_{\textit{high}}$ quantifies phase-dependent amplification.}
49	\label{tab:main-results}
50	\begin{tabular}{@{}llccccr@{}}
51	\toprule
52	$s$ & Strategy & $\widetilde{\mathrm{II}}_{\textit{high}}$ & $\widetilde{\mathrm{II}}_{\textit{mid}}$ & $\widetilde{\mathrm{II}}_{\textit{low}}$ & $\Delta$ & $G$ \\
53	\midrule
54	0.15 & Importance & 0.006 & 0.081 & 0.398 & 0.39 & $\mathbf{69}$ \\ % exp_id: bf16_importance_s015
55	0.15 & Random     & 0.093 & 0.097 & 0.103 & 0.01 & 1.1 \\ % exp_id: bf16_ds_rand_s015
56	\addlinespace
57	0.20 & Importance & 0.015 & 0.203 & 1.496 & 1.48 & $\mathbf{103}$ \\ % exp_id: bf16_importance_s020
58	0.20 & Random     & 0.292 & 0.350 & 0.276 & $-$0.02 & 0.9 \\ % exp_id: bf16_ds_rand_s020
59	\addlinespace
60	0.25 & Importance & 0.032 & 1.118 & 7.196 & 7.16 & $\mathbf{222}$ \\ % exp_id: bf16_importance_s025
61	0.25 & Random     & 0.818 & 0.932 & 1.363 & 0.54 & 1.7 \\ % exp_id: bf16_ds_rand_s025
62	\addlinespace
63	0.30 & Importance & 0.053 & 2.283 & 14.639 & 14.59 & $\mathbf{274}$ \\ % exp_id: bf16_importance_s030
64	0.30 & Random     & 2.503 & 2.592 & 4.041 & 1.54 & 1.6 \\ % exp_id: bf16_ds_rand_s030
65	\bottomrule
66	\end{tabular}
67	\end{table}
68	
69	The gradient growth is sub-exponential: successive ratios of the median severity difference $\Delta$ between adjacent sparsity levels are $3.8{\times}$, $4.8{\times}$, and $2.0{\times}$---a decreasing terminal growth rate consistent with a ceiling effect as compound degradation in the low-sparsity phase approaches saturation. The severity gradient $G$ exhibits the same pattern, with consecutive ratios of $1.5{\times}$, $2.2{\times}$, and $1.2{\times}$. Figure~\ref{fig:hero} visualizes this trajectory, contrasting the steep importance-based curve against the flat random baseline. % exp_id: bf16_importance_s015..s030; source: experiment_summary_table.json median_diff
70	
71	\begin{figure}[t]
72	\centering
73	\includegraphics[width=\columnwidth]{figures/fig1_dose_response.pdf}
74	\caption{Severity gradient ($G$) as a function of sparsity level $s$. Importance-based eviction (solid) exhibits an increasing gradient from $69{\times}$ to $274{\times}$, while random eviction (dashed) remains flat near $1{\times}$. Shaded regions denote 95\% bootstrap confidence intervals.} % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030
75	\label{fig:hero}
76	\end{figure}
77	
78	We report medians throughout because the II distribution is right-skewed: the mean severity difference exceeds the median by a factor of $1.6{:}1$ at $s{=}0.30$ under importance-based eviction (mean $\Delta = 22.94$ vs.\ median $\Delta = 14.59$). The median resists the influence of outlier problems with exceptionally long reasoning traces, while bootstrap confidence intervals (\S\ref{sec:stat-validation}) account for this skewness via the resampling distribution. % exp_id: bf16_importance_s030; source: cohens_d_bf16.json mean_diff=22.939, experiment_summary_table.json median_diff=14.586
79	
80	
81	\subsection{Phase-Strategy Crossover (C3)}
82	\label{sec:crossover}
83	
84	The phase-modulated gradient produces a striking qualitative phenomenon: a \emph{crossover} in which importance-based eviction is simultaneously the better and worse strategy depending on the reasoning phase. At $s{=}0.25$, importance-based eviction yields a lower II than random in the high-sparsity phase ($\widetilde{\mathrm{II}}_{\textit{high}} = 0.032$ vs.\ $0.818$), but a higher II in the low-sparsity phase ($\widetilde{\mathrm{II}}_{\textit{low}} = 7.196$ vs.\ $1.363$). This is not merely a magnitude difference---it is a reversal in the relative ranking of strategies across phases. % exp_id: bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json
85	
86	Figure~\ref{fig:crossover} displays the crossover structure as a heatmap of per-phase II values across strategies and sparsity levels.
87	
88	\begin{figure}[t]
89	\centering
90	\includegraphics[width=\columnwidth]{figures/fig3_crossover.pdf}
91	\caption{Strategy-dependent crossover at $s{=}0.25$. Grouped bar chart of median II by eviction strategy and reasoning phase. Importance-based eviction outperforms random in the high-sparsity phase but produces $5.3{\times}$ higher II in the low-sparsity phase, reversing the strategy ranking.} % exp_id: bf16_importance_s025, bf16_ds_rand_s025; 7.196/1.363=5.28
92	\label{fig:crossover}
93	\end{figure}
94	
95	The crossover emerges from an emergent phase-strategy interaction: in the high-sparsity phase---where attention is already focused---importance-based eviction preserves genuinely critical positions, yielding lower compound severity than random eviction. In the low-sparsity phase, however, head pruning redistributes attention mass across surviving heads, altering the importance score landscape in a way that couples the two sparsity mechanisms (\S\ref{sec:analysis}). The result is that targeted eviction inadvertently removes positions that would have been retained under the pre-pruning importance ranking---producing \emph{higher} compound severity than the explicitly random baseline.
96	
97	The crossover is present at all four tested sparsity levels ($s \geq 0.15$): at each level, importance-based eviction achieves lower II in the high-sparsity phase but higher II in the low-sparsity phase relative to random eviction. The magnitude of the low-phase reversal grows from $3.9{\times}$ at $s{=}0.15$ to $5.4{\times}$ at $s{=}0.20$, before moderating to $3.6{\times}$ at $s{=}0.30$ as random eviction severity also rises. % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json; ratios: 0.398/0.103=3.87, 1.496/0.276=5.42, 7.196/1.363=5.28, 14.639/4.041=3.62
98	
99	
100	\subsection{Cross-Model Replication (C5)}
101	\label{sec:cross-model}
102	
103	To assess whether the phase-modulated severity gradient generalizes beyond DeepSeek-R1-Distill-Qwen-7B, we replicate the importance-based eviction experiments on Qwen2.5-7B-Instruct. Both models share the Qwen2ForCausalLM backbone architecture (28 layers, 28 heads, 4-group GQA) but differ in training: DeepSeek uses reasoning distillation from DeepSeek-R1, while Qwen2.5 uses standard instruction tuning without explicit reasoning delimiters. This controlled comparison isolates the effect of training methodology on the compound sparsity interaction.
104	
105	Despite lacking explicit \texttt{&lt;think>} delimiters, Qwen2.5-7B-Instruct exhibits sufficient variation in attention sparsity across its generation trajectory to permit phase segmentation via the same quantile-based method (\S\ref{sec:phase-seg}). Four of the 50 problems are excluded due to degenerate phase assignments, yielding $n{=}46$ valid problems for Qwen (vs.\ $n{=}50$ for DeepSeek).
106	
107	Table~\ref{tab:cross-model} compares the median severity difference across both models.
108	
109	\begin{table}[t]
110	\centering
111	\small
112	\caption{Cross-model replication: median compound severity difference ($\Delta = \widetilde{\mathrm{II}}_{\textit{low}} - \widetilde{\mathrm{II}}_{\textit{high}}$) under importance-based eviction. Both models share the Qwen2 architecture but differ in training methodology (distillation vs.\ instruction tuning).}
113	\label{tab:cross-model}
114	\begin{tabular}{@{}lcccc@{}}
115	\toprule
116	Model & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
117	\midrule
118	DeepSeek-R1-Distill-Qwen-7B & 0.39 & 1.48 & 7.16 & 14.59 \\ % exp_id: bf16_importance_s015..s030; source: experiment_summary_table.json
119	Qwen2.5-7B-Instruct         & 0.04 & 0.23 & 1.27 & 2.94 \\ % exp_id: bf16_qw_imp_s015..s030; source: experiment_summary_table.json
120	\bottomrule
121	\end{tabular}
122	\end{table}
123	
124	Qwen2.5-7B-Instruct qualitatively reproduces the monotonic severity gradient observed in DeepSeek. The median severity difference increases from $0.04$ at $s{=}0.15$ to $2.94$ at $s{=}0.30$ (Table~\ref{tab:cross-model}), paralleling DeepSeek's $0.39$-to-$14.59$ trajectory at approximately one-tenth to one-fifth the absolute magnitude. Both models yield strictly increasing Cohen's $d$ trajectories (DeepSeek: $0.61 \to 1.13$; Qwen: $0.37 \to 1.44$; Table~\ref{tab:cohens-d}), with Spearman $\rho = 1.0$ between the four-point $d$ sequences (gradient permutation $p = 0.043$). The per-problem concordance across models is not significant (mean $\rho = -0.11$, $p = 0.926$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking. The Qwen effect is marginal at $s{=}0.15$ ($d{=}0.37$, bootstrap CI includes zero), becoming reliable at $s \geq 0.20$ ($d \geq 0.72$); this onset lag relative to DeepSeek is consistent with the lower overall compound severity in instruction-tuned models lacking explicit reasoning structure. % exp_id: cross_model_analysis.json (spearman_rho=1.0, gradient_permutation_p=0.043, per_problem_concordance_p=0.926, mean_rho=-0.107); cohens_d_bf16_qwen.json
125	
126	As a control, random eviction on Qwen yields no systematic phase gradient at three of four sparsity levels (3/4 FAIL), mirroring DeepSeek's 4/4 FAIL pattern. At $s{=}0.30$, Qwen random produces a borderline PASS (permutation $p = 0.012$) but with negligible effect size (Cohen's $d = -0.04$, CI spans zero), indicating no meaningful phase modulation. % exp_id: bf16_qw_rand_s015..s030; source: experiment_summary_table.json
127	
128	\begin{figure}[t]
129	\centering
130	\includegraphics[width=\columnwidth]{figures/fig5_crossmodel.pdf}
131	\caption{Cross-model comparison of the median severity difference under importance-based eviction. Both DeepSeek (solid) and Qwen (dashed) exhibit monotonically increasing $\Delta$ with sparsity; Qwen's magnitude is approximately one-fifth of DeepSeek's.} % exp_id: bf16_importance_s015..s030, bf16_qw_imp_s015..s030
132	\label{fig:cross-model}
133	\end{figure}
134	
135	The replication on a second model with distinct training methodology suggests that the phase-modulated severity gradient is not an artifact of DeepSeek's distillation-induced phase structure, but rather an emergent property of how compound sparsity interacts with attention dynamics in Transformer-based reasoning. We note that both models share the same backbone architecture; generalization to other architectures (e.g., LLaMA, Mistral) remains an open question (\S\ref{sec:limitations}).
136	
137	
138	\subsection{Statistical Validation}
139	\label{sec:stat-validation}
140	
141	We validate the strategy-dependent severity using two complementary approaches: a paired permutation test on the difference statistic for significance, and Cohen's $d$ for effect size.
142	
143	\paragraph{Permutation test.}
144	For each problem $i$ and sparsity level $s$, we compute the compound severity difference $\Delta_i^{(\text{strat})} = \mathrm{II}_{\textit{low},i} - \mathrm{II}_{\textit{high},i}$ under each eviction strategy. The test statistic is the median of the paired difference $\widetilde{\Delta} = \text{median}_i\!\bigl(\Delta_i^{(\text{imp})} - \Delta_i^{(\text{rand})}\bigr)$, measuring whether importance-based eviction produces systematically larger phase-dependent severity than random eviction. We permute strategy labels $10{,}000$ times to construct the null distribution and apply Bonferroni correction for 4 sparsity-level comparisons.
145	
146	Table~\ref{tab:permutation} reports the results. All four sparsity levels reject $H_0$ (no strategy difference) after Bonferroni correction ($p_{\text{Bonf}} < 0.005$), with observed median differences increasing monotonically from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$. % exp_id: deepseek_bf16_permtest; source: permutation_test_results.json
147	
148	\begin{table}[t]
149	\centering
150	\small
151	\caption{Paired permutation test (difference statistic) for compound severity: importance vs.\ random eviction on DeepSeek-R1-Distill-Qwen-7B ($n{=}49$ paired problems, $10{,}000$ permutations). $p$-values are Bonferroni-corrected for 4 comparisons.}
152	\label{tab:permutation}
153	\begin{tabular}{@{}rrcl@{}}
154	\toprule
155	$s$ & Observed $\widetilde{\Delta}$ & 95\% CI & $p_{\text{Bonf}}$ \\
156	\midrule
157	0.15 & 0.37 & $[0.19,\; 0.62]$ & 0.0032 \\ % exp_id: deepseek_bf16_permtest_s015; source: permutation_test_results.json s015.permutation_test_difference
158	0.20 & 0.97 & $[0.69,\; 1.49]$ & ${<}\,0.001$ \\ % exp_id: deepseek_bf16_permtest_s020; source: permutation_test_results.json s020.permutation_test_difference
159	0.25 & 3.34 & $[1.66,\; 6.64]$ & ${<}\,0.001$ \\ % exp_id: deepseek_bf16_permtest_s025; source: permutation_test_results.json s025.permutation_test_difference
160	0.30 & 9.85 & $[6.70,\; 16.29]$ & ${<}\,0.001$ \\ % exp_id: deepseek_bf16_permtest_s030; source: permutation_test_results.json s030.permutation_test_difference
161	\bottomrule
162	\end{tabular}
163	\end{table}
164	
165	The monotonic growth of both the point estimate and the CI lower bound ($0.19 \to 0.69 \to 1.66 \to 6.70$) confirms that compound severity amplification under importance-based eviction strengthens with sparsity---not merely in central tendency but also in worst-case lower bounds. % exp_id: deepseek_bf16_permtest; source: permutation_test_results.json
166	
167	\begin{figure}[t]
168	\centering
169	\includegraphics[width=\columnwidth]{figures/fig4_bootstrap.pdf}
170	\caption{Forest plot of permutation test results for the difference statistic. Horizontal bars show 95\% permutation CIs; diamonds mark observed median differences $\widetilde{\Delta}$. All CIs lie entirely above zero (vertical dashed line), confirming significant strategy-dependent severity at every sparsity level.}
171	\label{fig:permtest-forest}
172	\end{figure}
173	
174	\paragraph{Effect sizes.}
175	Table~\ref{tab:cohens-d} reports Cohen's $d$ (bootstrap $B{=}10{,}000$) measuring the standardized difference in II between low- and high-sparsity phases under importance-based eviction.
176	
177	\begin{table}[t]
178	\centering
179	\small
180	\caption{Cohen's $d$ and per-problem median difference $\widetilde{\Delta}$ for the phase-dependent II (low $-$ high) under importance-based eviction. Bootstrap 95\% CIs for $\widetilde{\Delta}$ ($B{=}10{,}000$, per-problem paired). DeepSeek: $n{=}49$ problems (1 excluded); Qwen: $n{=}46$ problems (4 excluded).}
181	\label{tab:cohens-d}
182	\begin{tabular}{@{}lcccc@{}}
183	\toprule
184	$s$ & DeepSeek $d$ & $\widetilde{\Delta}$ [95\% CI] & Qwen $d$ & $\widetilde{\Delta}$ [95\% CI] \\
185	\midrule
186	0.15 & 0.61 (medium) & 0.32\; $[0.20,\; 0.47]$ & 0.37 (small) & 0.05\; $[-0.01,\; 0.11]$\textsuperscript{ns} \\ % exp_id: bf16_ds_imp_s015, bf16_qw_imp_s015; per-problem paired B=10000
187	0.20 & 0.73 (medium) & 1.15\; $[0.66,\; 1.26]$ & 0.72 (medium) & 0.21\; $[0.07,\; 0.40]$ \\ % exp_id: bf16_ds_imp_s020, bf16_qw_imp_s020; per-problem paired B=10000
188	0.25 & 0.95 (large) & 3.97\; $[2.83,\; 5.29]$ & 1.23 (large) & 1.11\; $[0.61,\; 1.47]$ \\ % exp_id: bf16_ds_imp_s025, bf16_qw_imp_s025; per-problem paired B=10000
189	0.30 & 1.13 (large) & 9.94\; $[8.39,\; 16.65]$ & 1.44 (large) & 2.62\; $[1.72,\; 3.65]$ \\ % exp_id: bf16_ds_imp_s030, bf16_qw_imp_s030; per-problem paired B=10000
190	\bottomrule
191	\multicolumn{5}{@{}l}{\footnotesize \textsuperscript{ns}CI spans zero; marginal at $s{=}0.15$ (bootstrap CI includes zero), becoming reliable at $s \geq 0.20$.}
192	\end{tabular}
193	\end{table}
194	
195	For DeepSeek, the effect size increases monotonically from medium ($d{=}0.61$) at $s{=}0.15$ to large ($d{=}1.13$) at $s{=}0.30$, with all bootstrap CIs for $\widetilde{\Delta}$ excluding zero (Table~\ref{tab:cohens-d}). % exp_id: bf16_ds_imp_s015..s030; per-problem paired B=10000
196	For Qwen, the compound interaction effect is marginal at $s{=}0.15$ ($d{=}0.37$, bootstrap CI includes zero), becoming reliable at $s \geq 0.20$ ($d \geq 0.72$), suggesting a model-dependent onset threshold for detectable phase modulation. % exp_id: bf16_qw_imp_s015..s030; per-problem paired B=10000
197	At higher sparsity levels ($s \geq 0.25$), Qwen exhibits larger standardized effect sizes than DeepSeek ($d{=}1.23$/$1.44$ vs.\ $0.95$/$1.13$), consistent with lower between-problem variance in Qwen's II distribution yielding larger standardized differences despite smaller absolute II values. % exp_id: bf16_ds_imp_s025..s030, bf16_qw_imp_s025..s030; per-problem paired B=10000
198	Full per-problem distributions and permutation null distributions appear in Appendix~\ref{app:bootstrap-details}.
199	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "11ce0eaf-86ca-46d4-9542-e5f802a14049",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex",
      "content": "\n\\section{Results}\n\\label{sec:results}\n\nWe present our empirical findings in five parts: strategy-dependent compound severity (\\S\\ref{sec:strategy-severity}), phase-modulated amplification (\\S\\ref{sec:phase-amplification}), the phase-strategy crossover (\\S\\ref{sec:crossover}), cross-model replication (\\S\\ref{sec:cross-model}), and statistical validation (\\S\\ref{sec:stat-validation}).\n\n\n\\subsection{Experimental Overview}\n\\label{sec:exp-overview}\n\nWe evaluate compound sparsity on DeepSeek-R1-Distill-Qwen-7B using a 50-problem stratified subset of MATH-500 (\\S\\ref{sec:dataset}). For each problem, we measure perplexity under four conditions---dense, attention-only pruning, KV-only eviction, and compound (both)---at sparsity levels $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$. We compare importance-based and random eviction strategies (\\S\\ref{sec:sparsity-config}), and segment each generated sequence into high-, mid-, and low-sparsity reasoning phases via quantile-based attention sparsity partitioning (\\S\\ref{sec:phase-seg}). The interaction index (II, Eq.~\\ref{eq:ii}) quantifies compound super-additivity, and the severity gradient ($G$, Eq.~\\ref{eq:gradient}) captures phase-dependent amplification.\nModels are evaluated in \\texttt{bfloat16} precision (\\S\\ref{sec:experimental-setup}). Full experimental details appear therein.\n\n\n\\subsection{Strategy-Dependent Severity (C1)}\n\\label{sec:strategy-severity}\n\nThe compound severity difference reveals a stark dependence on eviction strategy. Table~\\ref{tab:aggregate-ii} reports the median compound severity difference $\\Delta = \\widetilde{\\mathrm{II}}_{\\textit{low}} - \\widetilde{\\mathrm{II}}_{\\textit{high}}$ across 50 problems for each strategy and sparsity level. Under importance-based eviction, compound sparsity produces substantial super-additive degradation that grows with sparsity: $\\Delta$ increases from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, a $37{\\times}$ amplification. Under random eviction, the severity difference shows no systematic growth, remaining near zero ($-0.02$ to $1.54$). % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Median compound severity difference ($\\Delta = \\widetilde{\\mathrm{II}}_{\\textit{low}} - \\widetilde{\\mathrm{II}}_{\\textit{high}}$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}50$ MATH-500 problems).}\n\\label{tab:aggregate-ii}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nStrategy & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\\\\n\\midrule\nImportance & 0.39 & 1.48 & 7.16 & 14.59 \\\\ % exp_id: bf16_importance_s015..s030; source: experiment_summary_table.json median_diff\nRandom     & 0.01 & $-$0.02 & 0.54 & 1.54 \\\\ % exp_id: bf16_ds_rand_s015..s030; source: experiment_summary_table.json median_diff\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThis strategy dependence indicates that compound sparsity severity is not an intrinsic property of the compression level. Rather, the same sparsity configuration produces qualitatively different compound behavior depending on the eviction strategy---an emergent phase-strategy interaction whose structure we unpack in the following subsections.\n\n\n\\subsection{Phase-Modulated Amplification (C2)}\n\\label{sec:phase-amplification}\n\nDecomposing the interaction index by reasoning phase reveals that the strategy-dependent severity observed in \\S\\ref{sec:strategy-severity} is driven by amplification concentrated in the low-sparsity phase. Table~\\ref{tab:main-results} reports per-phase median II and the severity gradient $G$ at each sparsity level.\n\nUnder importance-based eviction, the severity gradient---the ratio of low-phase to high-phase median II---increases with sparsity from $69{\\times}$ at $s{=}0.15$ to $274{\\times}$ at $s{=}0.30$. The low-sparsity phase---corresponding to exploratory reasoning with broadly distributed attention---bears disproportionate compound degradation, while the high-sparsity phase---corresponding to structured computation with focused attention---experiences near-zero compound interaction ($\\widetilde{\\mathrm{II}}_{\\textit{high}}$ ranges from $0.006$ to $0.053$). Under random eviction, the gradient remains near unity ($G \\approx 0.9$--$1.7{\\times}$) at all sparsity levels, confirming that phase modulation is specific to the emergent interaction between head pruning and importance-based scoring. % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Interaction index (II) by eviction strategy, reasoning phase, and sparsity level. II values are problem-level medians across 50 problems. $\\Delta = \\widetilde{\\mathrm{II}}_{\\textit{low}} - \\widetilde{\\mathrm{II}}_{\\textit{high}}$ is the median severity difference. $G = \\widetilde{\\mathrm{II}}_{\\textit{low}} / \\widetilde{\\mathrm{II}}_{\\textit{high}}$ quantifies phase-dependent amplification.}\n\\label{tab:main-results}\n\\begin{tabular}{@{}llccccr@{}}\n\\toprule\n$s$ & Strategy & $\\widetilde{\\mathrm{II}}_{\\textit{high}}$ & $\\widetilde{\\mathrm{II}}_{\\textit{mid}}$ & $\\widetilde{\\mathrm{II}}_{\\textit{low}}$ & $\\Delta$ & $G$ \\\\\n\\midrule\n0.15 & Importance & 0.006 & 0.081 & 0.398 & 0.39 & $\\mathbf{69}$ \\\\ % exp_id: bf16_importance_s015\n0.15 & Random     & 0.093 & 0.097 & 0.103 & 0.01 & 1.1 \\\\ % exp_id: bf16_ds_rand_s015\n\\addlinespace\n0.20 & Importance & 0.015 & 0.203 & 1.496 & 1.48 & $\\mathbf{103}$ \\\\ % exp_id: bf16_importance_s020\n0.20 & Random     & 0.292 & 0.350 & 0.276 & $-$0.02 & 0.9 \\\\ % exp_id: bf16_ds_rand_s020\n\\addlinespace\n0.25 & Importance & 0.032 & 1.118 & 7.196 & 7.16 & $\\mathbf{222}$ \\\\ % exp_id: bf16_importance_s025\n0.25 & Random     & 0.818 & 0.932 & 1.363 & 0.54 & 1.7 \\\\ % exp_id: bf16_ds_rand_s025\n\\addlinespace\n0.30 & Importance & 0.053 & 2.283 & 14.639 & 14.59 & $\\mathbf{274}$ \\\\ % exp_id: bf16_importance_s030\n0.30 & Random     & 2.503 & 2.592 & 4.041 & 1.54 & 1.6 \\\\ % exp_id: bf16_ds_rand_s030\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe gradient growth is sub-exponential: successive ratios of the median severity difference $\\Delta$ between adjacent sparsity levels are $3.8{\\times}$, $4.8{\\times}$, and $2.0{\\times}$---a decreasing terminal growth rate consistent with a ceiling effect as compound degradation in the low-sparsity phase approaches saturation. The severity gradient $G$ exhibits the same pattern, with consecutive ratios of $1.5{\\times}$, $2.2{\\times}$, and $1.2{\\times}$. Figure~\\ref{fig:hero} visualizes this trajectory, contrasting the steep importance-based curve against the flat random baseline. % exp_id: bf16_importance_s015..s030; source: experiment_summary_table.json median_diff\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig1_dose_response.pdf}\n\\caption{Severity gradient ($G$) as a function of sparsity level $s$. Importance-based eviction (solid) exhibits an increasing gradient from $69{\\times}$ to $274{\\times}$, while random eviction (dashed) remains flat near $1{\\times}$. Shaded regions denote 95\\% bootstrap confidence intervals.} % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030\n\\label{fig:hero}\n\\end{figure}\n\nWe report medians throughout because the II distribution is right-skewed: the mean severity difference exceeds the median by a factor of $1.6{:}1$ at $s{=}0.30$ under importance-based eviction (mean $\\Delta = 22.94$ vs.\\ median $\\Delta = 14.59$). The median resists the influence of outlier problems with exceptionally long reasoning traces, while bootstrap confidence intervals (\\S\\ref{sec:stat-validation}) account for this skewness via the resampling distribution. % exp_id: bf16_importance_s030; source: cohens_d_bf16.json mean_diff=22.939, experiment_summary_table.json median_diff=14.586\n\n\n\\subsection{Phase-Strategy Crossover (C3)}\n\\label{sec:crossover}\n\nThe phase-modulated gradient produces a striking qualitative phenomenon: a \\emph{crossover} in which importance-based eviction is simultaneously the better and worse strategy depending on the reasoning phase. At $s{=}0.25$, importance-based eviction yields a lower II than random in the high-sparsity phase ($\\widetilde{\\mathrm{II}}_{\\textit{high}} = 0.032$ vs.\\ $0.818$), but a higher II in the low-sparsity phase ($\\widetilde{\\mathrm{II}}_{\\textit{low}} = 7.196$ vs.\\ $1.363$). This is not merely a magnitude difference---it is a reversal in the relative ranking of strategies across phases. % exp_id: bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json\n\nFigure~\\ref{fig:crossover} displays the crossover structure as a heatmap of per-phase II values across strategies and sparsity levels.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig3_crossover.pdf}\n\\caption{Strategy-dependent crossover at $s{=}0.25$. Grouped bar chart of median II by eviction strategy and reasoning phase. Importance-based eviction outperforms random in the high-sparsity phase but produces $5.3{\\times}$ higher II in the low-sparsity phase, reversing the strategy ranking.} % exp_id: bf16_importance_s025, bf16_ds_rand_s025; 7.196/1.363=5.28\n\\label{fig:crossover}\n\\end{figure}\n\nThe crossover emerges from an emergent phase-strategy interaction: in the high-sparsity phase---where attention is already focused---importance-based eviction preserves genuinely critical positions, yielding lower compound severity than random eviction. In the low-sparsity phase, however, head pruning redistributes attention mass across surviving heads, altering the importance score landscape in a way that couples the two sparsity mechanisms (\\S\\ref{sec:analysis}). The result is that targeted eviction inadvertently removes positions that would have been retained under the pre-pruning importance ranking---producing \\emph{higher} compound severity than the explicitly random baseline.\n\nThe crossover is present at all four tested sparsity levels ($s \\geq 0.15$): at each level, importance-based eviction achieves lower II in the high-sparsity phase but higher II in the low-sparsity phase relative to random eviction. The magnitude of the low-phase reversal grows from $3.9{\\times}$ at $s{=}0.15$ to $5.4{\\times}$ at $s{=}0.20$, before moderating to $3.6{\\times}$ at $s{=}0.30$ as random eviction severity also rises. % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json; ratios: 0.398/0.103=3.87, 1.496/0.276=5.42, 7.196/1.363=5.28, 14.639/4.041=3.62\n\n\n\\subsection{Cross-Model Replication (C5)}\n\\label{sec:cross-model}\n\nTo assess whether the phase-modulated severity gradient generalizes beyond DeepSeek-R1-Distill-Qwen-7B, we replicate the importance-based eviction experiments on Qwen2.5-7B-Instruct. Both models share the Qwen2ForCausalLM backbone architecture (28 layers, 28 heads, 4-group GQA) but differ in training: DeepSeek uses reasoning distillation from DeepSeek-R1, while Qwen2.5 uses standard instruction tuning without explicit reasoning delimiters. This controlled comparison isolates the effect of training methodology on the compound sparsity interaction.\n\nDespite lacking explicit \\texttt{&lt;think>} delimiters, Qwen2.5-7B-Instruct exhibits sufficient variation in attention sparsity across its generation trajectory to permit phase segmentation via the same quantile-based method (\\S\\ref{sec:phase-seg}). Four of the 50 problems are excluded due to degenerate phase assignments, yielding $n{=}46$ valid problems for Qwen (vs.\\ $n{=}50$ for DeepSeek).\n\nTable~\\ref{tab:cross-model} compares the median severity difference across both models.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-model replication: median compound severity difference ($\\Delta = \\widetilde{\\mathrm{II}}_{\\textit{low}} - \\widetilde{\\mathrm{II}}_{\\textit{high}}$) under importance-based eviction. Both models share the Qwen2 architecture but differ in training methodology (distillation vs.\\ instruction tuning).}\n\\label{tab:cross-model}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nModel & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\\\\n\\midrule\nDeepSeek-R1-Distill-Qwen-7B & 0.39 & 1.48 & 7.16 & 14.59 \\\\ % exp_id: bf16_importance_s015..s030; source: experiment_summary_table.json\nQwen2.5-7B-Instruct         & 0.04 & 0.23 & 1.27 & 2.94 \\\\ % exp_id: bf16_qw_imp_s015..s030; source: experiment_summary_table.json\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nQwen2.5-7B-Instruct qualitatively reproduces the monotonic severity gradient observed in DeepSeek. The median severity difference increases from $0.04$ at $s{=}0.15$ to $2.94$ at $s{=}0.30$ (Table~\\ref{tab:cross-model}), paralleling DeepSeek's $0.39$-to-$14.59$ trajectory at approximately one-tenth to one-fifth the absolute magnitude. Both models yield strictly increasing Cohen's $d$ trajectories (DeepSeek: $0.61 \\to 1.13$; Qwen: $0.37 \\to 1.44$; Table~\\ref{tab:cohens-d}), with Spearman $\\rho = 1.0$ between the four-point $d$ sequences (gradient permutation $p = 0.043$). The per-problem concordance across models is not significant (mean $\\rho = -0.11$, $p = 0.926$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking. The Qwen effect is marginal at $s{=}0.15$ ($d{=}0.37$, bootstrap CI includes zero), becoming reliable at $s \\geq 0.20$ ($d \\geq 0.72$); this onset lag relative to DeepSeek is consistent with the lower overall compound severity in instruction-tuned models lacking explicit reasoning structure. % exp_id: cross_model_analysis.json (spearman_rho=1.0, gradient_permutation_p=0.043, per_problem_concordance_p=0.926, mean_rho=-0.107); cohens_d_bf16_qwen.json\n\nAs a control, random eviction on Qwen yields no systematic phase gradient at three of four sparsity levels (3/4 FAIL), mirroring DeepSeek's 4/4 FAIL pattern. At $s{=}0.30$, Qwen random produces a borderline PASS (permutation $p = 0.012$) but with negligible effect size (Cohen's $d = -0.04$, CI spans zero), indicating no meaningful phase modulation. % exp_id: bf16_qw_rand_s015..s030; source: experiment_summary_table.json\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig5_crossmodel.pdf}\n\\caption{Cross-model comparison of the median severity difference under importance-based eviction. Both DeepSeek (solid) and Qwen (dashed) exhibit monotonically increasing $\\Delta$ with sparsity; Qwen's magnitude is approximately one-fifth of DeepSeek's.} % exp_id: bf16_importance_s015..s030, bf16_qw_imp_s015..s030\n\\label{fig:cross-model}\n\\end{figure}\n\nThe replication on a second model with distinct training methodology suggests that the phase-modulated severity gradient is not an artifact of DeepSeek's distillation-induced phase structure, but rather an emergent property of how compound sparsity interacts with attention dynamics in Transformer-based reasoning. We note that both models share the same backbone architecture; generalization to other architectures (e.g., LLaMA, Mistral) remains an open question (\\S\\ref{sec:limitations}).\n\n\n\\subsection{Statistical Validation}\n\\label{sec:stat-validation}\n\nWe validate the strategy-dependent severity using two complementary approaches: a paired permutation test on the difference statistic for significance, and Cohen's $d$ for effect size.\n\n\\paragraph{Permutation test.}\nFor each problem $i$ and sparsity level $s$, we compute the compound severity difference $\\Delta_i^{(\\text{strat})} = \\mathrm{II}_{\\textit{low},i} - \\mathrm{II}_{\\textit{high},i}$ under each eviction strategy. The test statistic is the median of the paired difference $\\widetilde{\\Delta} = \\text{median}_i\\!\\bigl(\\Delta_i^{(\\text{imp})} - \\Delta_i^{(\\text{rand})}\\bigr)$, measuring whether importance-based eviction produces systematically larger phase-dependent severity than random eviction. We permute strategy labels $10{,}000$ times to construct the null distribution and apply Bonferroni correction for 4 sparsity-level comparisons.\n\nTable~\\ref{tab:permutation} reports the results. All four sparsity levels reject $H_0$ (no strategy difference) after Bonferroni correction ($p_{\\text{Bonf}} < 0.005$), with observed median differences increasing monotonically from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$. % exp_id: deepseek_bf16_permtest; source: permutation_test_results.json\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Paired permutation test (difference statistic) for compound severity: importance vs.\\ random eviction on DeepSeek-R1-Distill-Qwen-7B ($n{=}49$ paired problems, $10{,}000$ permutations). $p$-values are Bonferroni-corrected for 4 comparisons.}\n\\label{tab:permutation}\n\\begin{tabular}{@{}rrcl@{}}\n\\toprule\n$s$ & Observed $\\widetilde{\\Delta}$ & 95\\% CI & $p_{\\text{Bonf}}$ \\\\\n\\midrule\n0.15 & 0.37 & $[0.19,\\; 0.62]$ & 0.0032 \\\\ % exp_id: deepseek_bf16_permtest_s015; source: permutation_test_results.json s015.permutation_test_difference\n0.20 & 0.97 & $[0.69,\\; 1.49]$ & ${<}\\,0.001$ \\\\ % exp_id: deepseek_bf16_permtest_s020; source: permutation_test_results.json s020.permutation_test_difference\n0.25 & 3.34 & $[1.66,\\; 6.64]$ & ${<}\\,0.001$ \\\\ % exp_id: deepseek_bf16_permtest_s025; source: permutation_test_results.json s025.permutation_test_difference\n0.30 & 9.85 & $[6.70,\\; 16.29]$ & ${<}\\,0.001$ \\\\ % exp_id: deepseek_bf16_permtest_s030; source: permutation_test_results.json s030.permutation_test_difference\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe monotonic growth of both the point estimate and the CI lower bound ($0.19 \\to 0.69 \\to 1.66 \\to 6.70$) confirms that compound severity amplification under importance-based eviction strengthens with sparsity---not merely in central tendency but also in worst-case lower bounds. % exp_id: deepseek_bf16_permtest; source: permutation_test_results.json\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4_bootstrap.pdf}\n\\caption{Forest plot of permutation test results for the difference statistic. Horizontal bars show 95\\% permutation CIs; diamonds mark observed median differences $\\widetilde{\\Delta}$. All CIs lie entirely above zero (vertical dashed line), confirming significant strategy-dependent severity at every sparsity level.}\n\\label{fig:permtest-forest}\n\\end{figure}\n\n\\paragraph{Effect sizes.}\nTable~\\ref{tab:cohens-d} reports Cohen's $d$ (bootstrap $B{=}10{,}000$) measuring the standardized difference in II between low- and high-sparsity phases under importance-based eviction.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cohen's $d$ and per-problem median difference $\\widetilde{\\Delta}$ for the phase-dependent II (low $-$ high) under importance-based eviction. Bootstrap 95\\% CIs for $\\widetilde{\\Delta}$ ($B{=}10{,}000$, per-problem paired). DeepSeek: $n{=}49$ problems (1 excluded); Qwen: $n{=}46$ problems (4 excluded).}\n\\label{tab:cohens-d}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n$s$ & DeepSeek $d$ & $\\widetilde{\\Delta}$ [95\\% CI] & Qwen $d$ & $\\widetilde{\\Delta}$ [95\\% CI] \\\\\n\\midrule\n0.15 & 0.61 (medium) & 0.32\\; $[0.20,\\; 0.47]$ & 0.37 (small) & 0.05\\; $[-0.01,\\; 0.11]$\\textsuperscript{ns} \\\\ % exp_id: bf16_ds_imp_s015, bf16_qw_imp_s015; per-problem paired B=10000\n0.20 & 0.73 (medium) & 1.15\\; $[0.66,\\; 1.26]$ & 0.72 (medium) & 0.21\\; $[0.07,\\; 0.40]$ \\\\ % exp_id: bf16_ds_imp_s020, bf16_qw_imp_s020; per-problem paired B=10000\n0.25 & 0.95 (large) & 3.97\\; $[2.83,\\; 5.29]$ & 1.23 (large) & 1.11\\; $[0.61,\\; 1.47]$ \\\\ % exp_id: bf16_ds_imp_s025, bf16_qw_imp_s025; per-problem paired B=10000\n0.30 & 1.13 (large) & 9.94\\; $[8.39,\\; 16.65]$ & 1.44 (large) & 2.62\\; $[1.72,\\; 3.65]$ \\\\ % exp_id: bf16_ds_imp_s030, bf16_qw_imp_s030; per-problem paired B=10000\n\\bottomrule\n\\multicolumn{5}{@{}l}{\\footnotesize \\textsuperscript{ns}CI spans zero; marginal at $s{=}0.15$ (bootstrap CI includes zero), becoming reliable at $s \\geq 0.20$.}\n\\end{tabular}\n\\end{table}\n\nFor DeepSeek, the effect size increases monotonically from medium ($d{=}0.61$) at $s{=}0.15$ to large ($d{=}1.13$) at $s{=}0.30$, with all bootstrap CIs for $\\widetilde{\\Delta}$ excluding zero (Table~\\ref{tab:cohens-d}). % exp_id: bf16_ds_imp_s015..s030; per-problem paired B=10000\nFor Qwen, the compound interaction effect is marginal at $s{=}0.15$ ($d{=}0.37$, bootstrap CI includes zero), becoming reliable at $s \\geq 0.20$ ($d \\geq 0.72$), suggesting a model-dependent onset threshold for detectable phase modulation. % exp_id: bf16_qw_imp_s015..s030; per-problem paired B=10000\nAt higher sparsity levels ($s \\geq 0.25$), Qwen exhibits larger standardized effect sizes than DeepSeek ($d{=}1.23$/$1.44$ vs.\\ $0.95$/$1.13$), consistent with lower between-problem variance in Qwen's II distribution yielding larger standardized differences despite smaller absolute II values. % exp_id: bf16_ds_imp_s025..s030, bf16_qw_imp_s025..s030; per-problem paired B=10000\nFull per-problem distributions and permutation null distributions appear in Appendix~\\ref{app:bootstrap-details}.\n",
      "numLines": 199,
      "startLine": 1,
      "totalLines": 199
    }
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Read · `toolu_01HKBZHZkLDzxKwMHt61GM2x`</summary>

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
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "9d8869ed-5a41-4d4d-ae70-55f19b10d05f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EdBEMbD3qwr7Lh5TcAKsMH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12180,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12180
      },
      "output_tokens": 22,
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

_source line 19 · 2026-05-14T09:45:12.367Z_

<details><summary>↩ Tool result · `toolu_01HKBZHZkLDzxKwMHt61GM2x`</summary>

```text
1	
2	\section{Analysis: Mechanisms of Phase-Modulated Severity}
3	\label{sec:analysis}
4	
5	The results in \S\ref{sec:results} reveal a striking asymmetry: importance-based eviction exhibits $69$--$274{\times}$ severity amplification in low-sparsity phases (Table~\ref{tab:main-results}), while random eviction remains flat at ${\sim}1{\times}$ across all phases. % exp_id: bf16_importance_s015..s030; G=69,103,222,274
6	Why is compound severity phase-modulated for one strategy but not the other? We identify two mechanisms. \emph{Discrimination collapse}---a systematic reduction in the discriminative power of KV importance scores under head pruning---is the primary mechanism, robustly observed across both models and all tested conditions. A secondary \emph{entropy redistribution} pattern is consistent for DeepSeek but only partially replicates on Qwen, indicating model-dependent modulation.
7	
8	\subsection{Discrimination Collapse Under Head Pruning}
9	\label{sec:discrimination-collapse}
10	
11	The KV importance score (Eq.~\ref{eq:kv-importance}) aggregates attention mass across surviving heads. When head pruning reduces the number of contributing heads, the cumulative importance distribution becomes more uniform: the gap between highly-attended and rarely-attended positions shrinks. We quantify this effect through two complementary metrics applied to the per-position importance distribution.
12	
13	The \textbf{Gini coefficient} measures inequality in the importance distribution ($\mathrm{Gini}{=}0$: perfectly uniform; $\mathrm{Gini}{=}1$: maximally concentrated). The \textbf{coefficient of variation} (CV) captures relative dispersion. A decrease in either metric after pruning indicates reduced discriminative power.
14	
15	We observe discrimination collapse across both models in all tested conditions (Table~\ref{tab:discrimination-metrics}). Under importance-based eviction, the Gini delta is negative at every sparsity level for both DeepSeek ($-0.030$ to $-0.081$) and Qwen ($-0.010$ to $-0.020$), with magnitude scaling monotonically with sparsity in DeepSeek. % exp_id: c4_entropy_deepseek, c4_entropy_qwen
16	The CV delta is likewise negative in all 8 importance-based conditions, ranging from $-0.56$ to $-1.66$ (DeepSeek) and $-0.05$ to $-1.49$ (Qwen). The same pattern holds under random eviction (DeepSeek: $-0.031$ to $-0.073$; Qwen: $-0.019$ to $-0.045$), confirming that discrimination collapse is a consequence of head pruning \emph{per se}, not of the eviction strategy.
17	
18	\begin{table}[t]
19	\centering
20	\caption{Discrimination collapse under importance-based eviction. $\Delta\mathrm{Gini}$ and $\Delta\mathrm{CV}$ are post-pruning minus baseline; negative values indicate reduced discriminative power. All 8 conditions show consistent negative deltas across both models.}
21	\label{tab:discrimination-metrics}
22	\small
23	\begin{tabular}{llrr}
24	\toprule
25	Model & $s$ & $\Delta\mathrm{Gini}$ & $\Delta\mathrm{CV}$ \\
26	\midrule
27	DeepSeek & $0.15$ & $-0.030$ & $-0.56$ \\
28	DeepSeek & $0.20$ & $-0.040$ & $-0.77$ \\
29	DeepSeek & $0.25$ & $-0.065$ & $-1.29$ \\
30	DeepSeek & $0.30$ & $-0.081$ & $-1.66$ \\
31	\midrule
32	Qwen & $0.15$ & $-0.010$ & $-0.05$ \\
33	Qwen & $0.20$ & $-0.012$ & $-0.21$ \\
34	Qwen & $0.25$ & $-0.010$ & $-1.49$ \\
35	Qwen & $0.30$ & $-0.020$ & $-1.14$ \\
36	\bottomrule
37	\end{tabular}
38	\end{table}
39	
40	This cross-model consistency establishes discrimination collapse as a robust consequence of compound sparsity. When importance scores lose discriminative power, thresholding the bottom-$s$ fraction becomes noise-sensitive: small perturbations change which positions cross the eviction boundary. In the limit of perfectly uniform scores, importance-based eviction degenerates into an arbitrary selection functionally equivalent to biased random eviction. The severity inversion observed in \S\ref{sec:crossover} is thus an emergent consequence of the interaction between head pruning and importance scoring conditioned on the phase-dependent attention structure.
41	
42	Random eviction is immune to this mechanism: its decisions are independent of importance score quality. This explains the flat severity gradient ($G \approx 1$) observed under random eviction at all sparsity levels.
43	
44	\subsection{Entropy Redistribution: Consistent in DeepSeek, Partial in Qwen}
45	\label{sec:entropy-redistribution}
46	
47	Beyond discrimination collapse, we examine whether head pruning also redistributes the attention entropy of surviving heads. We measure the mean attention entropy per head:
48	\begin{equation}
49	    \mathcal{H}_i^{(h)} = -\sum_{j=1}^{T} a_{ij}^{(h)} \log a_{ij}^{(h)}
50	    \label{eq:attn-entropy}
51	\end{equation}
52	and compute $\Delta\mathcal{H}$ as the change from baseline (no pruning) to the pruned condition.
53	
54	For DeepSeek under importance-based eviction, the entropy delta is consistently negative across all four sparsity levels ($\Delta\mathcal{H} \in [-0.040, -0.047]$; Table~\ref{tab:entropy-deltas}), with the effect stable across reasoning phases. % exp_id: c4_entropy_deepseek
55	This is consistent with importance-based eviction systematically selecting heads whose removal concentrates attention in the surviving heads, reinforcing the discrimination collapse documented above.
56	
57	For Qwen, the entropy pattern only partially replicates. The delta is negative at $s{=}0.15$ ($\Delta\mathcal{H} = -0.073$) and $s{=}0.20$ ($-0.076$), consistent with DeepSeek. However, at $s{=}0.25$, the delta reverses to $+0.045$, with 22 of 30 problems showing positive entropy change. At $s{=}0.30$, the delta is near zero ($-0.007$). % exp_id: c4_entropy_qwen
58	
59	The $s{=}0.25$ reversal is systematic rather than a statistical artifact: it is consistent across all three reasoning phases (low-sparsity: $+0.042$, mid-sparsity: $+0.034$, high-sparsity: $+0.017$). The mid-sparsity phase contains fewer segments (median~26), which reduces statistical power for that phase; however, the reversal is equally present in the low-sparsity phase with substantially more segments, so mid-phase power limitations are a confound but do not account for the full pattern. We interpret this as a genuine model-specific difference, possibly arising from distinct head specialization patterns: Qwen's instruction tuning (vs.\ DeepSeek's distillation-based training) may produce head configurations where removing 25\% of heads triggers compensatory broadening rather than concentration.
60	
61	\begin{table}[t]
62	\centering
63	\caption{Attention entropy deltas ($\Delta\mathcal{H}$) under importance-based eviction. DeepSeek shows consistent entropy compression at all sparsity levels. Qwen partially replicates: negative at $s{\leq}0.20$, reversed at $s{=}0.25$, near-zero at $s{=}0.30$.}
64	\label{tab:entropy-deltas}
65	\small
66	\begin{tabular}{llr}
67	\toprule
68	Model & $s$ & $\Delta\mathcal{H}$ \\
69	\midrule
70	DeepSeek & $0.15$ & $-0.040$ \\
71	DeepSeek & $0.20$ & $-0.047$ \\
72	DeepSeek & $0.25$ & $-0.045$ \\
73	DeepSeek & $0.30$ & $-0.044$ \\
74	\midrule
75	Qwen & $0.15$ & $-0.073$ \\
76	Qwen & $0.20$ & $-0.076$ \\
77	Qwen & $0.25$ & $+0.045$ \\
78	Qwen & $0.30$ & $-0.007$ \\
79	\bottomrule
80	\end{tabular}
81	\end{table}
82	
83	The partial replication of entropy redistribution, combined with the full replication of discrimination collapse, suggests a two-level mechanistic picture: head pruning universally degrades the discriminative power of importance scores (as measured by Gini and CV), while the specific direction of entropy redistribution depends on model-specific head specialization patterns. Discrimination collapse is sufficient on its own to explain the emergent phase-strategy interaction; entropy redistribution, where it co-occurs, may amplify the effect.
84	
85	\subsection{Implications for Compound Sparsity}
86	\label{sec:analysis-implications}
87	
88	The discrimination collapse mechanism suggests several broader conclusions.
89	
90	\paragraph{Architecture generality.} Discrimination collapse depends on two properties: (i)~attention-mass-based importance scoring for KV eviction, and (ii)~a sufficient number of pruned heads to degrade the importance distribution. Both are shared by the major KV cache compression methods---H$_2$O \cite{h2o2024}, SnapKV \cite{snapkv2024}, PyramidKV \cite{pyramidkv2024}---and by any autoregressive transformer producing extended reasoning traces. The cross-model consistency of the Gini and CV evidence (Table~\ref{tab:discrimination-metrics}) supports this generality. The entropy redistribution component, while consistent in DeepSeek, appears model-dependent; the full mechanism may thus manifest differently across architectures.
91	
92	\paragraph{Testable prediction.} Any importance metric derived from attention mass should exhibit discrimination collapse under head pruning, with the severity gradient scaling with the pruning-induced Gini decrease. Metrics that derive importance from sources independent of attention---such as activation magnitude or gradient-based saliency---would not be subject to the same collapse and should produce flatter severity gradients.
93	
94	\paragraph{Reframing compound severity.} The flat random baseline ($G \approx 1$) demonstrates that phase-modulated severity amplification is not an inherent cost of compound sparsity \emph{per se}. Rather, it is an emergent phase-strategy interaction---the consequence of applying a discrimination-sensitive eviction strategy in a regime where head pruning systematically degrades that discrimination. A phase-aware sparsity controller could, in principle, mitigate this interaction by adjusting the eviction budget or strategy per phase.
95	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "ef98206b-98c1-409a-8271-e2b4a6dc0015",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex",
      "content": "\n\\section{Analysis: Mechanisms of Phase-Modulated Severity}\n\\label{sec:analysis}\n\nThe results in \\S\\ref{sec:results} reveal a striking asymmetry: importance-based eviction exhibits $69$--$274{\\times}$ severity amplification in low-sparsity phases (Table~\\ref{tab:main-results}), while random eviction remains flat at ${\\sim}1{\\times}$ across all phases. % exp_id: bf16_importance_s015..s030; G=69,103,222,274\nWhy is compound severity phase-modulated for one strategy but not the other? We identify two mechanisms. \\emph{Discrimination collapse}---a systematic reduction in the discriminative power of KV importance scores under head pruning---is the primary mechanism, robustly observed across both models and all tested conditions. A secondary \\emph{entropy redistribution} pattern is consistent for DeepSeek but only partially replicates on Qwen, indicating model-dependent modulation.\n\n\\subsection{Discrimination Collapse Under Head Pruning}\n\\label{sec:discrimination-collapse}\n\nThe KV importance score (Eq.~\\ref{eq:kv-importance}) aggregates attention mass across surviving heads. When head pruning reduces the number of contributing heads, the cumulative importance distribution becomes more uniform: the gap between highly-attended and rarely-attended positions shrinks. We quantify this effect through two complementary metrics applied to the per-position importance distribution.\n\nThe \\textbf{Gini coefficient} measures inequality in the importance distribution ($\\mathrm{Gini}{=}0$: perfectly uniform; $\\mathrm{Gini}{=}1$: maximally concentrated). The \\textbf{coefficient of variation} (CV) captures relative dispersion. A decrease in either metric after pruning indicates reduced discriminative power.\n\nWe observe discrimination collapse across both models in all tested conditions (Table~\\ref{tab:discrimination-metrics}). Under importance-based eviction, the Gini delta is negative at every sparsity level for both DeepSeek ($-0.030$ to $-0.081$) and Qwen ($-0.010$ to $-0.020$), with magnitude scaling monotonically with sparsity in DeepSeek. % exp_id: c4_entropy_deepseek, c4_entropy_qwen\nThe CV delta is likewise negative in all 8 importance-based conditions, ranging from $-0.56$ to $-1.66$ (DeepSeek) and $-0.05$ to $-1.49$ (Qwen). The same pattern holds under random eviction (DeepSeek: $-0.031$ to $-0.073$; Qwen: $-0.019$ to $-0.045$), confirming that discrimination collapse is a consequence of head pruning \\emph{per se}, not of the eviction strategy.\n\n\\begin{table}[t]\n\\centering\n\\caption{Discrimination collapse under importance-based eviction. $\\Delta\\mathrm{Gini}$ and $\\Delta\\mathrm{CV}$ are post-pruning minus baseline; negative values indicate reduced discriminative power. All 8 conditions show consistent negative deltas across both models.}\n\\label{tab:discrimination-metrics}\n\\small\n\\begin{tabular}{llrr}\n\\toprule\nModel & $s$ & $\\Delta\\mathrm{Gini}$ & $\\Delta\\mathrm{CV}$ \\\\\n\\midrule\nDeepSeek & $0.15$ & $-0.030$ & $-0.56$ \\\\\nDeepSeek & $0.20$ & $-0.040$ & $-0.77$ \\\\\nDeepSeek & $0.25$ & $-0.065$ & $-1.29$ \\\\\nDeepSeek & $0.30$ & $-0.081$ & $-1.66$ \\\\\n\\midrule\nQwen & $0.15$ & $-0.010$ & $-0.05$ \\\\\nQwen & $0.20$ & $-0.012$ & $-0.21$ \\\\\nQwen & $0.25$ & $-0.010$ & $-1.49$ \\\\\nQwen & $0.30$ & $-0.020$ & $-1.14$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThis cross-model consistency establishes discrimination collapse as a robust consequence of compound sparsity. When importance scores lose discriminative power, thresholding the bottom-$s$ fraction becomes noise-sensitive: small perturbations change which positions cross the eviction boundary. In the limit of perfectly uniform scores, importance-based eviction degenerates into an arbitrary selection functionally equivalent to biased random eviction. The severity inversion observed in \\S\\ref{sec:crossover} is thus an emergent consequence of the interaction between head pruning and importance scoring conditioned on the phase-dependent attention structure.\n\nRandom eviction is immune to this mechanism: its decisions are independent of importance score quality. This explains the flat severity gradient ($G \\approx 1$) observed under random eviction at all sparsity levels.\n\n\\subsection{Entropy Redistribution: Consistent in DeepSeek, Partial in Qwen}\n\\label{sec:entropy-redistribution}\n\nBeyond discrimination collapse, we examine whether head pruning also redistributes the attention entropy of surviving heads. We measure the mean attention entropy per head:\n\\begin{equation}\n    \\mathcal{H}_i^{(h)} = -\\sum_{j=1}^{T} a_{ij}^{(h)} \\log a_{ij}^{(h)}\n    \\label{eq:attn-entropy}\n\\end{equation}\nand compute $\\Delta\\mathcal{H}$ as the change from baseline (no pruning) to the pruned condition.\n\nFor DeepSeek under importance-based eviction, the entropy delta is consistently negative across all four sparsity levels ($\\Delta\\mathcal{H} \\in [-0.040, -0.047]$; Table~\\ref{tab:entropy-deltas}), with the effect stable across reasoning phases. % exp_id: c4_entropy_deepseek\nThis is consistent with importance-based eviction systematically selecting heads whose removal concentrates attention in the surviving heads, reinforcing the discrimination collapse documented above.\n\nFor Qwen, the entropy pattern only partially replicates. The delta is negative at $s{=}0.15$ ($\\Delta\\mathcal{H} = -0.073$) and $s{=}0.20$ ($-0.076$), consistent with DeepSeek. However, at $s{=}0.25$, the delta reverses to $+0.045$, with 22 of 30 problems showing positive entropy change. At $s{=}0.30$, the delta is near zero ($-0.007$). % exp_id: c4_entropy_qwen\n\nThe $s{=}0.25$ reversal is systematic rather than a statistical artifact: it is consistent across all three reasoning phases (low-sparsity: $+0.042$, mid-sparsity: $+0.034$, high-sparsity: $+0.017$). The mid-sparsity phase contains fewer segments (median~26), which reduces statistical power for that phase; however, the reversal is equally present in the low-sparsity phase with substantially more segments, so mid-phase power limitations are a confound but do not account for the full pattern. We interpret this as a genuine model-specific difference, possibly arising from distinct head specialization patterns: Qwen's instruction tuning (vs.\\ DeepSeek's distillation-based training) may produce head configurations where removing 25\\% of heads triggers compensatory broadening rather than concentration.\n\n\\begin{table}[t]\n\\centering\n\\caption{Attention entropy deltas ($\\Delta\\mathcal{H}$) under importance-based eviction. DeepSeek shows consistent entropy compression at all sparsity levels. Qwen partially replicates: negative at $s{\\leq}0.20$, reversed at $s{=}0.25$, near-zero at $s{=}0.30$.}\n\\label{tab:entropy-deltas}\n\\small\n\\begin{tabular}{llr}\n\\toprule\nModel & $s$ & $\\Delta\\mathcal{H}$ \\\\\n\\midrule\nDeepSeek & $0.15$ & $-0.040$ \\\\\nDeepSeek & $0.20$ & $-0.047$ \\\\\nDeepSeek & $0.25$ & $-0.045$ \\\\\nDeepSeek & $0.30$ & $-0.044$ \\\\\n\\midrule\nQwen & $0.15$ & $-0.073$ \\\\\nQwen & $0.20$ & $-0.076$ \\\\\nQwen & $0.25$ & $+0.045$ \\\\\nQwen & $0.30$ & $-0.007$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe partial replication of entropy redistribution, combined with the full replication of discrimination collapse, suggests a two-level mechanistic picture: head pruning universally degrades the discriminative power of importance scores (as measured by Gini and CV), while the specific direction of entropy redistribution depends on model-specific head specialization patterns. Discrimination collapse is sufficient on its own to explain the emergent phase-strategy interaction; entropy redistribution, where it co-occurs, may amplify the effect.\n\n\\subsection{Implications for Compound Sparsity}\n\\label{sec:analysis-implications}\n\nThe discrimination collapse mechanism suggests several broader conclusions.\n\n\\paragraph{Architecture generality.} Discrimination collapse depends on two properties: (i)~attention-mass-based importance scoring for KV eviction, and (ii)~a sufficient number of pruned heads to degrade the importance distribution. Both are shared by the major KV cache compression methods---H$_2$O \\cite{h2o2024}, SnapKV \\cite{snapkv2024}, PyramidKV \\cite{pyramidkv2024}---and by any autoregressive transformer producing extended reasoning traces. The cross-model consistency of the Gini and CV evidence (Table~\\ref{tab:discrimination-metrics}) supports this generality. The entropy redistribution component, while consistent in DeepSeek, appears model-dependent; the full mechanism may thus manifest differently across architectures.\n\n\\paragraph{Testable prediction.} Any importance metric derived from attention mass should exhibit discrimination collapse under head pruning, with the severity gradient scaling with the pruning-induced Gini decrease. Metrics that derive importance from sources independent of attention---such as activation magnitude or gradient-based saliency---would not be subject to the same collapse and should produce flatter severity gradients.\n\n\\paragraph{Reframing compound severity.} The flat random baseline ($G \\approx 1$) demonstrates that phase-modulated severity amplification is not an inherent cost of compound sparsity \\emph{per se}. Rather, it is an emergent phase-strategy interaction---the consequence of applying a discrimination-sensitive eviction strategy in a regime where head pruning systematically degrades that discrimination. A phase-aware sparsity controller could, in principle, mitigate this interaction by adjusting the eviction budget or strategy per phase.\n",
      "numLines": 95,
      "startLine": 1,
      "totalLines": 95
    }
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Read · `toolu_01XCbeXcyRdViohD1t8zwV9k`</summary>

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
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "ed84b43b-16b0-41be-86e2-af79b258025a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EdBEMbD3qwr7Lh5TcAKsMH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12180,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12180
      },
      "output_tokens": 22,
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

_source line 21 · 2026-05-14T09:45:12.697Z_

<details><summary>↩ Tool result · `toolu_01XCbeXcyRdViohD1t8zwV9k`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{On the predictability of phase-modulated severity.}
5	One might argue that the qualitative direction of our findings is intuitive: in low-sparsity phases, attention distributes broadly across many tokens, so importance scores carry less discriminative signal, and importance-based eviction should degrade.
6	We do not dispute this intuition.
7	The surprise lies in the quantitative structure of the interaction, which is not predictable from first principles alone.
8	
9	First, the \emph{magnitude} of the severity gradient---$69$--$274{\times}$ amplification across sparsity levels (Table~\ref{tab:main-results})---far exceeds what a naive ``less discriminative $\Rightarrow$ somewhat worse'' argument would predict. % exp_id: bf16_importance_s015..s030; source: experiment_summary_table.json; G=low/high=69,103,222,274.
10	A reviewer expecting a $2$--$3\times$ effect would find two-orders-of-magnitude amplification difficult to anticipate without measurement.
11	Second, the gradient is \emph{phase-specific}: compound interaction concentrates in low-sparsity phases while high-sparsity phases exhibit near-zero compound interaction ($\widetilde{\mathrm{II}}_{\text{high}} < 0.06$ at $s \leq 0.30$; at $s = 0.35$, high-phase II rises to 0.105, indicating the onset of compound interaction even in high-sparsity phases at extreme pruning rates). % exp_id: bf16_importance_s015..s030; high-phase medians: 0.006, 0.015, 0.032, 0.053
12	This asymmetry means that importance-based eviction is not uniformly fragile---it is selectively fragile in a phase-dependent manner.
13	Third, and most strikingly, a \emph{crossover} emerges: at $s{=}0.25$, importance-based eviction \emph{outperforms} random eviction in high-sparsity phases (median severity $0.032$ vs.\ $0.818$) yet \emph{underperforms} in low-sparsity phases ($7.196$ vs.\ $1.363$---a ${>}5{\times}$ severity inflation relative to random). % exp_id: bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json; high: imp=0.032, rand=0.818; low: imp=7.196, rand=1.363
14	The same strategy reverses direction across phases---a phenomenon that cannot be derived from the observation that ``importance scores are noisier when attention is diffuse.''
15	% REVIEWER-ATTACK: "The qualitative direction is trivially expected from attention entropy arguments."
16	% REBUTTAL: (1) Qualitative direction ≠ quantitative structure: 69-274× amplification is two orders of magnitude, not marginal. (2) Phase-specific concentration + crossover cannot be predicted from single-layer entropy reasoning. (3) Random eviction's flat profile (~1×) shows the amplification is strategy-specific, not an inherent property of compound sparsity.
17	
18	\paragraph{Random masking as a falsification control.}
19	The random eviction baseline provides a decisive test against the ``trivially expected'' objection.
20	If compound severity amplification were an inherent property of applying two compression methods jointly---rather than an emergent phase-strategy interaction---random eviction should exhibit a comparable phase gradient.
21	It does not: random eviction fails seven of eight paired permutation tests across both models (7/8 FAIL); the single exception (Qwen $s{=}0.30$, $p{=}0.012$) exhibits negligible effect size ($d{=}{-}0.04$), producing no practically meaningful phase-modulated severity. % exp_id: bf16_ds_rand_s015..s030, bf16_qw_rand_s015..s030; verdict: 7/8 FAIL, 1 PASS (qw_rand_s030 p=0.012 d=-0.035 negligible)
22	The absence of a phase gradient under random masking isolates the amplification as strategy-specific: it arises from the interaction between importance-based eviction and phase structure, not from compound sparsity per se.
23	
24	\paragraph{Cross-model replication and magnitude asymmetry.}
25	The phase-strategy interaction replicates across both models with perfect ordinal agreement: the Spearman rank correlation of Cohen's $d$ effect sizes across sparsity levels is $\rho{=}1.0$, and a gradient permutation test confirms this monotonic co-escalation ($p{=}0.043$). % exp_id: cross_model_correlation; Spearman rho=1.0, gradient_perm p=0.043
26	All eight paired Wilcoxon tests (4 sparsity levels $\times$ 2 models) reject $H_0$, confirming the pattern is not an artifact of a single model's weight structure.
27	
28	The \emph{magnitude} of the effect, however, differs substantially.
29	Qwen's median severity differences ($0.039 \to 0.235 \to 1.268 \to 2.943$) are approximately one-fifth of DeepSeek's ($0.39 \to 1.48 \to 7.16 \to 14.59$), and the onset threshold differs: DeepSeek's gradient is significant from $s{=}0.15$ (Cohen's $d{=}0.607$), while Qwen's becomes clearly significant only at $s \geq 0.20$ ($d{=}0.722$; $s{=}0.15$ is borderline at $d{=}0.371$ with CI crossing zero). % exp_id: cohens_d_paired_b10000.json (ds: 0.607,0.725,0.953,1.126), cohens_d_bf16_qwen.json (qw: 0.371,0.722,1.233,1.439).
30	The two models share the Qwen2ForCausalLM architecture but differ in training: DeepSeek-R1-Distill-Qwen-7B is distilled from a larger reasoning model, while Qwen2.5-7B-Instruct undergoes standard instruction tuning.
31	We conjecture that distillation amplifies the phase-strategy interaction by producing sharper internal phase transitions---a hypothesis testable by comparing distilled and non-distilled variants at matched scale.
32	
33	\paragraph{Mechanistic evidence: discrimination collapse as the robust signal.}
34	The entropy-discrimination collapse hypothesis (\S\ref{sec:analysis}) receives partial cross-model support.
35	The discrimination components---Gini coefficient reduction and coefficient-of-variation compression under compound sparsity---are directionally consistent across both models, confirming that importance-based eviction loses discriminative power in low-sparsity phases regardless of training procedure.
36	However, the entropy component is model-dependent: DeepSeek exhibits consistent negative entropy shifts (attention concentrates further under head pruning), while Qwen shows a sign reversal at $s{=}0.25$ ($\Delta H {=} {+}0.045$) and near-zero shift at $s{=}0.30$ ($\Delta H {=} {-}0.007$). % exp_id: mechanism_entropy_qwen; s025: +0.045, s030: -0.007
37	This divergence suggests that discrimination collapse---not entropy redistribution---is the primary driver of the phase-strategy interaction, with entropy behavior being a model-dependent secondary effect.
38	We therefore characterize the mechanistic evidence as \emph{preliminary}: the discrimination pathway is robust across models, but the complete entropy-discrimination collapse narrative requires the qualification that its entropy component does not generalize.
39	
40	\paragraph{Implications for compound sparsity deployment.}
41	Our findings suggest that the standard practice of applying a uniform compression budget across all inference steps is suboptimal for reasoning models.
42	Compound severity is not distributed evenly: it concentrates in low-sparsity phases, where the entropy-discrimination collapse mechanism (\S\ref{sec:analysis}) renders importance-based eviction unreliable.
43	A deployment pipeline that allocates the same sparsity level $s$ to every token position implicitly accepts order-of-magnitude severity penalties during the exploratory reasoning stages that happen to fall in the low-sparsity regime.
44	
45	This observation motivates \emph{phase-aware compression budgets}: rather than a single global sparsity target, the system would allocate higher capacity (lower sparsity) to low-sparsity phases---where compound interaction is most severe---and reclaim that budget in high-sparsity phases, where compound behavior is near-additive and importance-based eviction remains effective.
46	The severity gradient $G$ reported in \S\ref{sec:phase-amplification} provides a natural signal for such allocation: phases with $G \gg 1$ receive a reduced sparsity budget, while phases with $G \leq 1$ tolerate aggressive compression with minimal quality loss.
47	
48	\paragraph{Future directions.}
49	The phase-aware allocation principle above points toward a concrete system design: a \emph{phase-gated controller} that monitors attention sparsity statistics in real time and dynamically adjusts the compound sparsity budget per reasoning phase.
50	The controller would route each generation step through a low-overhead phase classifier (\S\ref{sec:phase-seg}), then apply a phase-specific sparsity configuration derived from the severity gradient.
51	Whether such a controller can recover most of the compression benefit while avoiding the severity amplification in low-sparsity phases is an open empirical question.
52	
53	A second direction concerns completing the mechanistic picture.
54	The discrimination collapse component of our hypothesis is robust across models, but the entropy redistribution component is model-dependent (\S\ref{sec:discussion}).
55	Directly measuring per-head entropy shifts across architecturally distinct models---and identifying what training-time properties (e.g., distillation depth, RLHF intensity) determine whether entropy concentrates or disperses under head pruning---would clarify the boundary conditions of the full entropy-discrimination collapse mechanism.
56	
57	Finally, scaling the empirical methodology to larger models and diverse reasoning tasks would establish the generality of the phase-strategy interaction documented in this work.
58	
59	\subsection{Limitations}
60	\label{sec:limitations}
61	
62	\paragraph{Model scale.}
63	All experiments are conducted at the 7B parameter scale.
64	Whether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested.
65	Larger models may exhibit different attention redundancy structures that alter the discrimination collapse dynamics (and the model-dependent entropy component may behave differently at scale).
66	% REVIEWER-ATTACK: "7B is too small to be relevant for production."
67	% REBUTTAL: 7B is the most-deployed scale for on-device and cost-constrained serving—exactly where compound sparsity is needed. The mechanism (entropy-discrimination collapse) is scale-agnostic in principle. Scaling experiments are future work.
68	
69	\paragraph{Architectural scope.}
70	Our two models---DeepSeek-R1-Distill-Qwen-7B and Qwen2.5-7B-Instruct---share the Qwen2ForCausalLM architecture.
71	The cross-model replication (\S\ref{sec:cross-model}) confirms that the findings are not artifacts of a single model's weights, but both models share the same attention mechanism design.
72	The entropy-discrimination collapse mechanism is in principle agnostic across attention architectures (it depends on attention redistribution, not architecture-specific components), but empirical validation on architecturally distinct attention designs (e.g., GQA variants such as LLaMA~3 or Mistral, or multi-latent attention architectures) is needed.
73	% REVIEWER-ATTACK: "Cross-model ≠ cross-architecture. Both are Qwen2ForCausalLM."
74	% REBUTTAL: Correct—we explicitly state this is cross-model (different training: distillation vs instruction tuning), not cross-architecture. The two models isolate the training variable while controlling architecture. Cross-architecture validation (LLaMA, Mistral) is acknowledged as future work.
75	
76	\paragraph{Task coverage.}
77	We evaluate exclusively on MATH-500, a mathematical reasoning benchmark.
78	Different reasoning tasks---code generation, commonsense reasoning, multi-hop question answering---may induce different phase structures with different sparsity distributions, potentially altering the severity gradient profile.
79	Generalizing the phase-strategy interaction to broader reasoning domains is an important next step.
80	% REVIEWER-ATTACK: "Only MATH-500. How do we know this isn't a math-specific artifact?"
81	% REBUTTAL: The mechanism (entropy-discrimination collapse under head pruning) depends on attention distribution properties, not math-specific features. MATH-500 is a standard benchmark with diverse difficulty. However, different reasoning tasks may induce different phase structures—we state this limitation explicitly rather than overclaiming.
82	
83	\paragraph{Statistical scope.}
84	Bootstrap confidence intervals use $B{=}10{,}000$ resamples. The paired permutation test yields $n{=}49$ paired problems for DeepSeek (1 excluded) and $n{=}46$ for Qwen (4 excluded). % exp_id: cohens_d_bf16.json, cohens_d_bf16_qwen.json
85	The severity difference distribution is right-skewed (mean/median ratio ${\sim}1.6{:}1$ at $s{=}0.30$), motivating our use of medians and nonparametric tests rather than parametric alternatives. % exp_id: bf16_importance_s030; mean_diff=22.94, median_diff=14.59 (segment-level). Per-problem paired: median_diff=9.9436 at s030
86	All four permutation tests reject $H_0$ after Bonferroni correction ($p_{\text{Bonf}} < 0.005$; Table~\ref{tab:permutation}), with CI lower bounds increasing from $0.20$ to $8.39$---confirming the effect direction at every sparsity level. The permutation CIs at higher sparsity are wider (e.g., $[8.39,\; 16.65]$ at $s{=}0.30$), reflecting genuine variance in per-problem severity amplification. % exp_id: permutation_test_results.json; updated bf16 B=10000 per-problem paired CIs: s015=[0.199,0.472], s020=[0.655,1.256], s025=[2.829,5.292], s030=[8.392,16.653]
87	
88	A notable exception among the random baselines is the Qwen random condition at $s{=}0.30$, which yields a statistically significant result ($p{=}0.012$) despite negligible effect size ($d{=}{-}0.04$, bootstrap CI excluding zero). % exp_id: qw_rand_s030; B=10000, p=0.012, d=-0.035, negligible
89	This case illustrates that dichotomous significance testing can flag effects of no practical magnitude---reinforcing the importance of reporting effect sizes and confidence intervals alongside $p$-values.
90	
91	\paragraph{Sparsity range.}
92	Our experiments span $s \in \{0.15, 0.20, 0.25, 0.30\}$, a moderate range representative of practical deployment targets.
93	More extreme sparsity ($s > 0.50$) may exhibit qualitatively different interaction dynamics---the sub-exponential growth pattern suggests the severity gradient may plateau, but this remains unverified.
94	Conversely, the lower boundary at which phase-modulated amplification first emerges is not yet characterized.
95	% REVIEWER-ATTACK: "Why not test higher sparsity? 0.30 is conservative."
96	% REBUTTAL: Our focus is on the practically relevant regime where models retain usable quality. At s>0.30 both strategies degrade severely, making II measurement less informative. The sub-exponential growth (C6, $\Delta$ growth rate $3.8{\times} \to 4.8{\times} \to 2.0{\times}$) suggests saturation at higher sparsity, but confirming this is future work.
97	
98	\paragraph{No throughput evaluation.}
99	This work focuses on characterizing the \emph{structural} properties of compound sparsity severity---its phase dependence, strategy dependence, and interaction magnitude.
100	We do not report inference throughput or latency measurements, which are necessary for a complete deployment analysis but orthogonal to the severity characterization that is our primary contribution.
101	% REVIEWER-ATTACK: "No system evaluation. How do we know the severity amplification matters for real deployment?"
102	% REBUTTAL: This is an empirical finding paper, not a method/system paper. The contribution is characterizing *what happens* (phase-modulated severity) and *why* (entropy-discrimination collapse), not building a system to fix it. Phase-gated controllers are explicitly scoped as future work. The finding is actionable regardless: any compound sparsity deployment should be aware of phase-dependent severity.
103	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "860fbc48-a6c5-495c-abf0-6ef8a98c3f15",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex",
      "content": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{On the predictability of phase-modulated severity.}\nOne might argue that the qualitative direction of our findings is intuitive: in low-sparsity phases, attention distributes broadly across many tokens, so importance scores carry less discriminative signal, and importance-based eviction should degrade.\nWe do not dispute this intuition.\nThe surprise lies in the quantitative structure of the interaction, which is not predictable from first principles alone.\n\nFirst, the \\emph{magnitude} of the severity gradient---$69$--$274{\\times}$ amplification across sparsity levels (Table~\\ref{tab:main-results})---far exceeds what a naive ``less discriminative $\\Rightarrow$ somewhat worse'' argument would predict. % exp_id: bf16_importance_s015..s030; source: experiment_summary_table.json; G=low/high=69,103,222,274.\nA reviewer expecting a $2$--$3\\times$ effect would find two-orders-of-magnitude amplification difficult to anticipate without measurement.\nSecond, the gradient is \\emph{phase-specific}: compound interaction concentrates in low-sparsity phases while high-sparsity phases exhibit near-zero compound interaction ($\\widetilde{\\mathrm{II}}_{\\text{high}} < 0.06$ at $s \\leq 0.30$; at $s = 0.35$, high-phase II rises to 0.105, indicating the onset of compound interaction even in high-sparsity phases at extreme pruning rates). % exp_id: bf16_importance_s015..s030; high-phase medians: 0.006, 0.015, 0.032, 0.053\nThis asymmetry means that importance-based eviction is not uniformly fragile---it is selectively fragile in a phase-dependent manner.\nThird, and most strikingly, a \\emph{crossover} emerges: at $s{=}0.25$, importance-based eviction \\emph{outperforms} random eviction in high-sparsity phases (median severity $0.032$ vs.\\ $0.818$) yet \\emph{underperforms} in low-sparsity phases ($7.196$ vs.\\ $1.363$---a ${>}5{\\times}$ severity inflation relative to random). % exp_id: bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json; high: imp=0.032, rand=0.818; low: imp=7.196, rand=1.363\nThe same strategy reverses direction across phases---a phenomenon that cannot be derived from the observation that ``importance scores are noisier when attention is diffuse.''\n% REVIEWER-ATTACK: \"The qualitative direction is trivially expected from attention entropy arguments.\"\n% REBUTTAL: (1) Qualitative direction ≠ quantitative structure: 69-274× amplification is two orders of magnitude, not marginal. (2) Phase-specific concentration + crossover cannot be predicted from single-layer entropy reasoning. (3) Random eviction's flat profile (~1×) shows the amplification is strategy-specific, not an inherent property of compound sparsity.\n\n\\paragraph{Random masking as a falsification control.}\nThe random eviction baseline provides a decisive test against the ``trivially expected'' objection.\nIf compound severity amplification were an inherent property of applying two compression methods jointly---rather than an emergent phase-strategy interaction---random eviction should exhibit a comparable phase gradient.\nIt does not: random eviction fails seven of eight paired permutation tests across both models (7/8 FAIL); the single exception (Qwen $s{=}0.30$, $p{=}0.012$) exhibits negligible effect size ($d{=}{-}0.04$), producing no practically meaningful phase-modulated severity. % exp_id: bf16_ds_rand_s015..s030, bf16_qw_rand_s015..s030; verdict: 7/8 FAIL, 1 PASS (qw_rand_s030 p=0.012 d=-0.035 negligible)\nThe absence of a phase gradient under random masking isolates the amplification as strategy-specific: it arises from the interaction between importance-based eviction and phase structure, not from compound sparsity per se.\n\n\\paragraph{Cross-model replication and magnitude asymmetry.}\nThe phase-strategy interaction replicates across both models with perfect ordinal agreement: the Spearman rank correlation of Cohen's $d$ effect sizes across sparsity levels is $\\rho{=}1.0$, and a gradient permutation test confirms this monotonic co-escalation ($p{=}0.043$). % exp_id: cross_model_correlation; Spearman rho=1.0, gradient_perm p=0.043\nAll eight paired Wilcoxon tests (4 sparsity levels $\\times$ 2 models) reject $H_0$, confirming the pattern is not an artifact of a single model's weight structure.\n\nThe \\emph{magnitude} of the effect, however, differs substantially.\nQwen's median severity differences ($0.039 \\to 0.235 \\to 1.268 \\to 2.943$) are approximately one-fifth of DeepSeek's ($0.39 \\to 1.48 \\to 7.16 \\to 14.59$), and the onset threshold differs: DeepSeek's gradient is significant from $s{=}0.15$ (Cohen's $d{=}0.607$), while Qwen's becomes clearly significant only at $s \\geq 0.20$ ($d{=}0.722$; $s{=}0.15$ is borderline at $d{=}0.371$ with CI crossing zero). % exp_id: cohens_d_paired_b10000.json (ds: 0.607,0.725,0.953,1.126), cohens_d_bf16_qwen.json (qw: 0.371,0.722,1.233,1.439).\nThe two models share the Qwen2ForCausalLM architecture but differ in training: DeepSeek-R1-Distill-Qwen-7B is distilled from a larger reasoning model, while Qwen2.5-7B-Instruct undergoes standard instruction tuning.\nWe conjecture that distillation amplifies the phase-strategy interaction by producing sharper internal phase transitions---a hypothesis testable by comparing distilled and non-distilled variants at matched scale.\n\n\\paragraph{Mechanistic evidence: discrimination collapse as the robust signal.}\nThe entropy-discrimination collapse hypothesis (\\S\\ref{sec:analysis}) receives partial cross-model support.\nThe discrimination components---Gini coefficient reduction and coefficient-of-variation compression under compound sparsity---are directionally consistent across both models, confirming that importance-based eviction loses discriminative power in low-sparsity phases regardless of training procedure.\nHowever, the entropy component is model-dependent: DeepSeek exhibits consistent negative entropy shifts (attention concentrates further under head pruning), while Qwen shows a sign reversal at $s{=}0.25$ ($\\Delta H {=} {+}0.045$) and near-zero shift at $s{=}0.30$ ($\\Delta H {=} {-}0.007$). % exp_id: mechanism_entropy_qwen; s025: +0.045, s030: -0.007\nThis divergence suggests that discrimination collapse---not entropy redistribution---is the primary driver of the phase-strategy interaction, with entropy behavior being a model-dependent secondary effect.\nWe therefore characterize the mechanistic evidence as \\emph{preliminary}: the discrimination pathway is robust across models, but the complete entropy-discrimination collapse narrative requires the qualification that its entropy component does not generalize.\n\n\\paragraph{Implications for compound sparsity deployment.}\nOur findings suggest that the standard practice of applying a uniform compression budget across all inference steps is suboptimal for reasoning models.\nCompound severity is not distributed evenly: it concentrates in low-sparsity phases, where the entropy-discrimination collapse mechanism (\\S\\ref{sec:analysis}) renders importance-based eviction unreliable.\nA deployment pipeline that allocates the same sparsity level $s$ to every token position implicitly accepts order-of-magnitude severity penalties during the exploratory reasoning stages that happen to fall in the low-sparsity regime.\n\nThis observation motivates \\emph{phase-aware compression budgets}: rather than a single global sparsity target, the system would allocate higher capacity (lower sparsity) to low-sparsity phases---where compound interaction is most severe---and reclaim that budget in high-sparsity phases, where compound behavior is near-additive and importance-based eviction remains effective.\nThe severity gradient $G$ reported in \\S\\ref{sec:phase-amplification} provides a natural signal for such allocation: phases with $G \\gg 1$ receive a reduced sparsity budget, while phases with $G \\leq 1$ tolerate aggressive compression with minimal quality loss.\n\n\\paragraph{Future directions.}\nThe phase-aware allocation principle above points toward a concrete system design: a \\emph{phase-gated controller} that monitors attention sparsity statistics in real time and dynamically adjusts the compound sparsity budget per reasoning phase.\nThe controller would route each generation step through a low-overhead phase classifier (\\S\\ref{sec:phase-seg}), then apply a phase-specific sparsity configuration derived from the severity gradient.\nWhether such a controller can recover most of the compression benefit while avoiding the severity amplification in low-sparsity phases is an open empirical question.\n\nA second direction concerns completing the mechanistic picture.\nThe discrimination collapse component of our hypothesis is robust across models, but the entropy redistribution component is model-dependent (\\S\\ref{sec:discussion}).\nDirectly measuring per-head entropy shifts across architecturally distinct models---and identifying what training-time properties (e.g., distillation depth, RLHF intensity) determine whether entropy concentrates or disperses under head pruning---would clarify the boundary conditions of the full entropy-discrimination collapse mechanism.\n\nFinally, scaling the empirical methodology to larger models and diverse reasoning tasks would establish the generality of the phase-strategy interaction documented in this work.\n\n\\subsection{Limitations}\n\\label{sec:limitations}\n\n\\paragraph{Model scale.}\nAll experiments are conducted at the 7B parameter scale.\nWhether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested.\nLarger models may exhibit different attention redundancy structures that alter the discrimination collapse dynamics (and the model-dependent entropy component may behave differently at scale).\n% REVIEWER-ATTACK: \"7B is too small to be relevant for production.\"\n% REBUTTAL: 7B is the most-deployed scale for on-device and cost-constrained serving—exactly where compound sparsity is needed. The mechanism (entropy-discrimination collapse) is scale-agnostic in principle. Scaling experiments are future work.\n\n\\paragraph{Architectural scope.}\nOur two models---DeepSeek-R1-Distill-Qwen-7B and Qwen2.5-7B-Instruct---share the Qwen2ForCausalLM architecture.\nThe cross-model replication (\\S\\ref{sec:cross-model}) confirms that the findings are not artifacts of a single model's weights, but both models share the same attention mechanism design.\nThe entropy-discrimination collapse mechanism is in principle agnostic across attention architectures (it depends on attention redistribution, not architecture-specific components), but empirical validation on architecturally distinct attention designs (e.g., GQA variants such as LLaMA~3 or Mistral, or multi-latent attention architectures) is needed.\n% REVIEWER-ATTACK: \"Cross-model ≠ cross-architecture. Both are Qwen2ForCausalLM.\"\n% REBUTTAL: Correct—we explicitly state this is cross-model (different training: distillation vs instruction tuning), not cross-architecture. The two models isolate the training variable while controlling architecture. Cross-architecture validation (LLaMA, Mistral) is acknowledged as future work.\n\n\\paragraph{Task coverage.}\nWe evaluate exclusively on MATH-500, a mathematical reasoning benchmark.\nDifferent reasoning tasks---code generation, commonsense reasoning, multi-hop question answering---may induce different phase structures with different sparsity distributions, potentially altering the severity gradient profile.\nGeneralizing the phase-strategy interaction to broader reasoning domains is an important next step.\n% REVIEWER-ATTACK: \"Only MATH-500. How do we know this isn't a math-specific artifact?\"\n% REBUTTAL: The mechanism (entropy-discrimination collapse under head pruning) depends on attention distribution properties, not math-specific features. MATH-500 is a standard benchmark with diverse difficulty. However, different reasoning tasks may induce different phase structures—we state this limitation explicitly rather than overclaiming.\n\n\\paragraph{Statistical scope.}\nBootstrap confidence intervals use $B{=}10{,}000$ resamples. The paired permutation test yields $n{=}49$ paired problems for DeepSeek (1 excluded) and $n{=}46$ for Qwen (4 excluded). % exp_id: cohens_d_bf16.json, cohens_d_bf16_qwen.json\nThe severity difference distribution is right-skewed (mean/median ratio ${\\sim}1.6{:}1$ at $s{=}0.30$), motivating our use of medians and nonparametric tests rather than parametric alternatives. % exp_id: bf16_importance_s030; mean_diff=22.94, median_diff=14.59 (segment-level). Per-problem paired: median_diff=9.9436 at s030\nAll four permutation tests reject $H_0$ after Bonferroni correction ($p_{\\text{Bonf}} < 0.005$; Table~\\ref{tab:permutation}), with CI lower bounds increasing from $0.20$ to $8.39$---confirming the effect direction at every sparsity level. The permutation CIs at higher sparsity are wider (e.g., $[8.39,\\; 16.65]$ at $s{=}0.30$), reflecting genuine variance in per-problem severity amplification. % exp_id: permutation_test_results.json; updated bf16 B=10000 per-problem paired CIs: s015=[0.199,0.472], s020=[0.655,1.256], s025=[2.829,5.292], s030=[8.392,16.653]\n\nA notable exception among the random baselines is the Qwen random condition at $s{=}0.30$, which yields a statistically significant result ($p{=}0.012$) despite negligible effect size ($d{=}{-}0.04$, bootstrap CI excluding zero). % exp_id: qw_rand_s030; B=10000, p=0.012, d=-0.035, negligible\nThis case illustrates that dichotomous significance testing can flag effects of no practical magnitude---reinforcing the importance of reporting effect sizes and confidence intervals alongside $p$-values.\n\n\\paragraph{Sparsity range.}\nOur experiments span $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$, a moderate range representative of practical deployment targets.\nMore extreme sparsity ($s > 0.50$) may exhibit qualitatively different interaction dynamics---the sub-exponential growth pattern suggests the severity gradient may plateau, but this remains unverified.\nConversely, the lower boundary at which phase-modulated amplification first emerges is not yet characterized.\n% REVIEWER-ATTACK: \"Why not test higher sparsity? 0.30 is conservative.\"\n% REBUTTAL: Our focus is on the practically relevant regime where models retain usable quality. At s>0.30 both strategies degrade severely, making II measurement less informative. The sub-exponential growth (C6, $\\Delta$ growth rate $3.8{\\times} \\to 4.8{\\times} \\to 2.0{\\times}$) suggests saturation at higher sparsity, but confirming this is future work.\n\n\\paragraph{No throughput evaluation.}\nThis work focuses on characterizing the \\emph{structural} properties of compound sparsity severity---its phase dependence, strategy dependence, and interaction magnitude.\nWe do not report inference throughput or latency measurements, which are necessary for a complete deployment analysis but orthogonal to the severity characterization that is our primary contribution.\n% REVIEWER-ATTACK: \"No system evaluation. How do we know the severity amplification matters for real deployment?\"\n% REBUTTAL: This is an empirical finding paper, not a method/system paper. The contribution is characterizing *what happens* (phase-modulated severity) and *why* (entropy-discrimination collapse), not building a system to fix it. Phase-gated controllers are explicitly scoped as future work. The finding is actionable regardless: any compound sparsity deployment should be aware of phase-dependent severity.\n",
      "numLines": 103,
      "startLine": 1,
      "totalLines": 103
    }
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Read · `toolu_01FtggLWwnKFg3Txj5JdXR7U`</summary>

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
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "486c748f-8df6-4abb-bb85-f0dec1f42764",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EdBEMbD3qwr7Lh5TcAKsMH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12180,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12180
      },
      "output_tokens": 22,
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

_source line 23 · 2026-05-14T09:45:13.119Z_

<details><summary>↩ Tool result · `toolu_01FtggLWwnKFg3Txj5JdXR7U`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We presented an empirical investigation of how compound sparsity severity---the super-additive interaction between attention head pruning and KV cache eviction---varies across reasoning phases and eviction strategies in 7B-parameter language models. Our central finding is that compound severity is not a fixed property of the sparsity level but an emergent phase-strategy interaction whose magnitude spans over an order of magnitude within a single generation.
5	
6	Our contributions, mapped to confirmed claims, are:
7	\begin{enumerate}[nosep,leftmargin=*]
8	    \item \textbf{Strategy dependence (C1).} Compound severity depends qualitatively on the eviction strategy: importance-based eviction produces phase-modulated interaction (median phase difference $0.39$--$14.59$), while random eviction shows no significant phase modulation in 7/8 conditions (the sole exception---Qwen $s{=}0.30$, $p{=}0.012$, $d{=}{-}0.04$---has negligible effect size).
9	
10	    \item \textbf{Phase modulation (C2).} Under importance-based eviction, the median Interaction Index difference between low- and high-sparsity phases increases monotonically with sparsity (Bonferroni-corrected $p < 0.005$ at all four levels), with paired effect sizes growing from $d{=}0.44$ (small) to $d{=}0.80$ (large).
11	
12	    \item \textbf{Phase-strategy crossover (C3).} At $s{=}0.25$, importance-based eviction simultaneously outperforms random in high-sparsity phases ($\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$) and underperforms in low-sparsity phases ($\widetilde{\mathrm{II}} = 7.196$ vs.\ $1.363$)---a qualitative reversal in strategy ranking.
13	
14	    \item \textbf{Sub-exponential growth (C6).} The severity gradient grows with sparsity but at a decelerating rate, suggesting a natural ceiling on phase-dependent amplification.
15	
16	    \item \textbf{Cross-model replication (C5).} The monotonic gradient replicates on Qwen2.5-7B-Instruct at $s \geq 0.20$ ($d \geq 0.55$; Spearman $\rho = 1.0$ across sparsity levels; gradient permutation $p = 0.043$), with attenuated absolute magnitude (${\sim}1/5$ of DeepSeek).
17	
18	    \item \textbf{Mechanistic explanation (C4).} Discrimination collapse---whereby head pruning degrades the discriminative power of importance scores---is robustly confirmed across both models (Gini and CV decrease in all 16 conditions). A secondary entropy redistribution pattern is consistent for DeepSeek but partially replicates on Qwen (2/4 conditions), indicating model-dependent modulation.
19	\end{enumerate}
20	
21	\paragraph{Limitations.}
22	Both models share the Qwen2 architecture; our cross-model comparison isolates training methodology (distillation vs.\ instruction tuning) but not architectural design, so generalization to other architectures (e.g., LLaMA, Mistral, multi-latent attention) remains open.
23	All experiments are at the 7B scale; whether severity gradients persist, amplify, or attenuate at larger scales is untested.
24	We evaluate on a single benchmark (MATH-500); different reasoning domains may induce different phase structures.
25	The discrimination collapse mechanism is supported by correlational evidence but lacks direct causal validation through controlled entropy manipulation.
26	While discrimination collapse (Gini and CV reduction) is consistent across all conditions for both models, the entropy redistribution component replicates on only 2 of 4 sparsity levels for Qwen, suggesting model-specific factors modulate its manifestation.
27	
28	\paragraph{Future work.}
29	A \emph{phase-gated sparsity controller} that dynamically adjusts compound sparsity budgets per reasoning phase could mitigate the severity amplification we document while preserving compression gains where compound behavior is near-additive.
30	Cross-architecture validation and scaling to larger models would establish the generality of the phase-strategy interaction.
31	Direct measurement of per-head entropy shifts under pruning would provide causal evidence for the collapse mechanism.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "bdf5833e-0999-4bc4-aba2-4ea49d2d27d2",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex",
      "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe presented an empirical investigation of how compound sparsity severity---the super-additive interaction between attention head pruning and KV cache eviction---varies across reasoning phases and eviction strategies in 7B-parameter language models. Our central finding is that compound severity is not a fixed property of the sparsity level but an emergent phase-strategy interaction whose magnitude spans over an order of magnitude within a single generation.\n\nOur contributions, mapped to confirmed claims, are:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item \\textbf{Strategy dependence (C1).} Compound severity depends qualitatively on the eviction strategy: importance-based eviction produces phase-modulated interaction (median phase difference $0.39$--$14.59$), while random eviction shows no significant phase modulation in 7/8 conditions (the sole exception---Qwen $s{=}0.30$, $p{=}0.012$, $d{=}{-}0.04$---has negligible effect size).\n\n    \\item \\textbf{Phase modulation (C2).} Under importance-based eviction, the median Interaction Index difference between low- and high-sparsity phases increases monotonically with sparsity (Bonferroni-corrected $p < 0.005$ at all four levels), with paired effect sizes growing from $d{=}0.44$ (small) to $d{=}0.80$ (large).\n\n    \\item \\textbf{Phase-strategy crossover (C3).} At $s{=}0.25$, importance-based eviction simultaneously outperforms random in high-sparsity phases ($\\widetilde{\\mathrm{II}} = 0.032$ vs.\\ $0.818$) and underperforms in low-sparsity phases ($\\widetilde{\\mathrm{II}} = 7.196$ vs.\\ $1.363$)---a qualitative reversal in strategy ranking.\n\n    \\item \\textbf{Sub-exponential growth (C6).} The severity gradient grows with sparsity but at a decelerating rate, suggesting a natural ceiling on phase-dependent amplification.\n\n    \\item \\textbf{Cross-model replication (C5).} The monotonic gradient replicates on Qwen2.5-7B-Instruct at $s \\geq 0.20$ ($d \\geq 0.55$; Spearman $\\rho = 1.0$ across sparsity levels; gradient permutation $p = 0.043$), with attenuated absolute magnitude (${\\sim}1/5$ of DeepSeek).\n\n    \\item \\textbf{Mechanistic explanation (C4).} Discrimination collapse---whereby head pruning degrades the discriminative power of importance scores---is robustly confirmed across both models (Gini and CV decrease in all 16 conditions). A secondary entropy redistribution pattern is consistent for DeepSeek but partially replicates on Qwen (2/4 conditions), indicating model-dependent modulation.\n\\end{enumerate}\n\n\\paragraph{Limitations.}\nBoth models share the Qwen2 architecture; our cross-model comparison isolates training methodology (distillation vs.\\ instruction tuning) but not architectural design, so generalization to other architectures (e.g., LLaMA, Mistral, multi-latent attention) remains open.\nAll experiments are at the 7B scale; whether severity gradients persist, amplify, or attenuate at larger scales is untested.\nWe evaluate on a single benchmark (MATH-500); different reasoning domains may induce different phase structures.\nThe discrimination collapse mechanism is supported by correlational evidence but lacks direct causal validation through controlled entropy manipulation.\nWhile discrimination collapse (Gini and CV reduction) is consistent across all conditions for both models, the entropy redistribution component replicates on only 2 of 4 sparsity levels for Qwen, suggesting model-specific factors modulate its manifestation.\n\n\\paragraph{Future work.}\nA \\emph{phase-gated sparsity controller} that dynamically adjusts compound sparsity budgets per reasoning phase could mitigate the severity amplification we document while preserving compression gains where compound behavior is near-additive.\nCross-architecture validation and scaling to larger models would establish the generality of the phase-strategy interaction.\nDirect measurement of per-head entropy shifts under pruning would provide causal evidence for the collapse mechanism.",
      "numLines": 31,
      "startLine": 1,
      "totalLines": 31
    }
  }
}
```

</details>

---

### Assistant

_source line 24_

<details><summary>Logged reasoning block</summary>

```text
Now let me also read the paper_framing.md to check claims C1-C6, and check for any stale files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "dec1333c-8642-4c61-a88e-45a2cbb6c12f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YTDQDMH75r6WCvzKzmhcCt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 26095,
      "cache_read_input_tokens": 24021,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 26095
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

_source line 25_

Now reading paper_framing.md and checking stale files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "b05f6157-9ec5-4596-bfc8-cb1f36eb952c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YTDQDMH75r6WCvzKzmhcCt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 26095,
      "cache_read_input_tokens": 24021,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 26095
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

_source line 26_

<details open><summary>🔧 Tool call — Agent · `toolu_01LP3Uh1fWxdN8jFGJzRtP4T`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find paper_framing.md",
  "prompt": "Find any file named paper_framing.md or similar in /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/. Search recursively. Report the full path and its contents."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "992ea332-5598-4b75-97d7-f12a203d27db",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YTDQDMH75r6WCvzKzmhcCt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 26095,
      "cache_read_input_tokens": 24021,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 26095
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

_source line 27_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a4a5e16a935552112",
  "tool_use_id": "toolu_01LP3Uh1fWxdN8jFGJzRtP4T",
  "description": "Find paper_framing.md",
  "task_type": "local_agent",
  "prompt": "Find any file named paper_framing.md or similar in /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/. Search recursively. Report the full path and its contents.",
  "uuid": "8dee749c-4e45-4dbe-9fda-948595554933",
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86"
}
```

---

## Round 1

59 recorded events

### User

_source line 28 · 2026-05-14T09:45:19.957Z_

Find any file named paper_framing.md or similar in /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/. Search recursively. Report the full path and its contents.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LP3Uh1fWxdN8jFGJzRtP4T",
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "7d380fe2-5209-4257-b15d-0d71bc55f991"
}
```

</details>

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Glob · `toolu_018DGqmdK44LxtiBVAwVusWE`</summary>

```json
{
  "pattern": "*",
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
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "45665acc-e8ba-4292-b75b-e1d78a80a387",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YTDQDMH75r6WCvzKzmhcCt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 26095,
      "cache_read_input_tokens": 24021,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 26095
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

_source line 30 · 2026-05-14T09:45:20.666Z_

<details><summary>↩ Tool result · `toolu_018DGqmdK44LxtiBVAwVusWE`</summary>

```text
artifacts/_project/paper/related_work_46fb53.tex
artifacts/_project/paper/background_fc6d1d.tex
artifacts/_project/paper/methodology_4cc5f3.tex
artifacts/_project/paper/background.tex
artifacts/_project/paper/methodology.tex
artifacts/_project/paper/results_5_1.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/analysis.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/discussion.tex
artifacts/_project/paper/abstract.tex
artifacts/_project/paper/conclusion.tex
artifacts/_project/paper/results.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "91f8459c-d4ea-4ce0-bfd5-6409cd9f6e48",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/paper/related_work_46fb53.tex",
      "artifacts/_project/paper/background_fc6d1d.tex",
      "artifacts/_project/paper/methodology_4cc5f3.tex",
      "artifacts/_project/paper/background.tex",
      "artifacts/_project/paper/methodology.tex",
      "artifacts/_project/paper/results_5_1.tex",
      "artifacts/_project/paper/related_work.tex",
      "artifacts/_project/paper/analysis.tex",
      "artifacts/_project/paper/introduction.tex",
      "artifacts/_project/paper/discussion.tex",
      "artifacts/_project/paper/abstract.tex",
      "artifacts/_project/paper/conclusion.tex",
      "artifacts/_project/paper/results.tex"
    ],
    "durationMs": 15,
    "numFiles": 13,
    "truncated": false
  }
}
```

</details>

---

### System

_source line 31_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4a5e16a935552112",
  "tool_use_id": "toolu_01LP3Uh1fWxdN8jFGJzRtP4T",
  "description": "Finding **/paper_framing.md",
  "usage": {
    "total_tokens": 17825,
    "tool_uses": 1,
    "duration_ms": 1540
  },
  "last_tool_name": "Glob",
  "uuid": "b6701eb3-45d0-4e7c-9440-4ae298323fd1",
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86"
}
```

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — Glob · `toolu_01TsmE3r45zsUQ4n3xdFpA6V`</summary>

```json
{
  "pattern": "**/paper_framing.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LP3Uh1fWxdN8jFGJzRtP4T",
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "70774324-0714-4e8e-8ce0-3f16ed29728e",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013pyQm1NjwtgMvEE4smdqF8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17812,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17812,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 33 · 2026-05-14T09:45:21.532Z_

<details><summary>↩ Tool result · `toolu_01TsmE3r45zsUQ4n3xdFpA6V`</summary>

```text
artifacts/dream_reports/dream_20260514T054026/best/paper_framing.md
artifacts/dream_reports/dream_20260514T054026/median/paper_framing.md
artifacts/dream_reports/dream_20260514T054026/worst/paper_framing.md
paper_framing.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LP3Uh1fWxdN8jFGJzRtP4T",
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "b2882ab7-6bdd-4083-8cc5-0b5e9d61885a"
}
```

</details>

---

### System

_source line 34_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4a5e16a935552112",
  "tool_use_id": "toolu_01LP3Uh1fWxdN8jFGJzRtP4T",
  "description": "Reading paper_framing.md",
  "usage": {
    "total_tokens": 18879,
    "tool_uses": 2,
    "duration_ms": 2898
  },
  "last_tool_name": "Read",
  "uuid": "711b5152-fedd-4e2d-afbc-30b7033c516c",
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86"
}
```

---

### Tool call

_source line 35_

<details open><summary>🔧 Tool call — Read · `toolu_01QGSLsaqmyvFWJ3BDUz5aJn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LP3Uh1fWxdN8jFGJzRtP4T",
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "bd8d262b-53e5-4c18-8250-3a6ce55b6e57",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014xqrzGvxxDmYTpnwvHCnBr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1050,
      "cache_read_input_tokens": 17812,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1050,
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

_source line 36 · 2026-05-14T09:45:22.871Z_

<details><summary>↩ Tool result · `toolu_01QGSLsaqmyvFWJ3BDUz5aJn`</summary>

```text
1	# Paper Framing — Phase-Gated Compound Sparsity
2	
3	> 最后更新: 2026-05-14 09:20 UTC | 维护者: Director
4	
5	## Core Insight
6	
7	Compound sparsity（attention head pruning + KV cache eviction）的 severity 不是固定常数——它是 eviction strategy 和 reasoning phase 交互的涌现属性。Importance-based eviction 的 compound interaction severity（paired median difference: median(II_low_i − II_high_i)）随 sparsity 单调递增（DeepSeek: 0.32→1.15→3.97→9.94; Qwen: 0.048→0.208→1.109→2.619），而 random masking 三相 II 持平（7/8 FAIL; Qwen s030 PASS p=0.012 but d=-0.04 negligible）。Cohen's d（per-problem paired, B=10000）从 medium 到 large（DeepSeek: 0.61→1.13; Qwen: 0.37→1.44，s015 边缘）。这一发现挑战了 compound degradation 均匀分布的隐含假设。
8	
9	**数字基准**：所有数字基于 bf16 per-problem paired 统计量（B=10000 bootstrap）。median_diff 定义为 median(II_low_i − II_high_i)（逐 problem 配对差的中位数）。fp16 旧数据已弃用。
10	
11	## Narrative Arc
12	
13	Compound sparsity 是高效 LLM 推理的实用部署需求，但 prior work（SparK, Ada-KV, SLiM）将 compound interaction 视为均匀超可加。我们发现 severity 是 strategy × phase 交互的涌现属性：importance eviction 的 compound interaction 在 low-sparsity phase 远大于 high-sparsity phase（paired median difference 单调递增 0.32→9.94），而 random eviction 在所有 phase 保持平坦（7/8 FAIL; 唯一例外 Qwen s030 p=0.012 效应量可忽略 d=-0.04）。Cross-model replication 方向一致（Qwen magnitude ~1/4 of DeepSeek，onset threshold s≥0.20）。我们通过 discrimination collapse 机制解释这一现象：head pruning → importance score 的判别力崩塌（Gini/CV 下降跨模型一致）→ importance eviction 退化为有偏伪随机。Attention entropy redistribution 作为 model-dependent secondary effect 在 DeepSeek 上观察到，但在 Qwen 上不稳健（D044）。
14	
15	**Framing 硬约束（D015）**：
16	- MUST: "emergent phase-strategy interaction"
17	- MUST NOT: "importance metric limitation / importance is broken"
18	- MUST NOT: claim "importance masking produces super-additive interaction" without qualifier — random masking also produces positive II. The distinguishing signal is **phase-dependent gradient** (importance: paired median difference 0.32→9.94 单调递增 vs random: 7/8 FAIL), not the existence of super-additivity itself (D023)
19	
20	## Core Claims
21	
22	| ID | Claim | Status | Key Evidence |
23	|----|-------|--------|-------------|
24	| C1 | Compound sparsity severity is strategy-dependent | confirmed | importance paired median diff 0.32→9.94 单调递增 vs random 7/8 FAIL (bf16; Qwen s030 PASS p=0.012 d=-0.04 negligible) |
25	| C2 | Severity is phase-modulated (amplified in low-sparsity phase) | confirmed | bf16 paired median difference 单调递增: 0.32→1.15→3.97→9.94; Bonferroni p<0.005 全 4 水平 (D032) |
26	| C3 | Phase-strategy crossover exists | confirmed | s=0.25: importance high_phase=0.032 < random=0.818, importance low_phase=7.196 > random=1.363 (bf16) |
27	| C4 | Discrimination collapse as primary mechanism; entropy redistribution model-dependent | partially_confirmed | D044: Gini/CV 下降跨模型一致; entropy collapse DeepSeek 一致但 Qwen s025 反转(+0.045) s030≈0。30/30 problems completed. |
28	| C5 | Finding generalizes across models (same arch, different training) | confirmed | Qwen importance 4/4 PASS，paired median diff 0.048→2.619 单调递增。Cohen's d (paired) s≥0.20 显著，s015 边缘。Cross-model 非 cross-architecture。 |
29	| C6 | Severity gradient is sub-exponential | confirmed | Growth rate decreasing: Δ增长因子 3.8×→4.8×→2.0×（递减） |
30	
31	## Anticipated Reviewer Concerns
32	
33	### RC1: Generalizability — 7B models only, single benchmark
34	- **预期质疑**: "Results on two 7B models and MATH-500 only. How do we know this generalizes to larger models or other reasoning tasks?"
35	- **应对**: Cross-model replication (DeepSeek-R1-Distill-Qwen-7B + Qwen2.5-7B-Instruct) 控制架构变量、隔离训练方式影响（distillation vs instruction tuning）。注意：两模型共享 Qwen2ForCausalLM 架构，不能 claim 跨架构泛化。MATH-500 是 standard benchmark。Limitations 必须诚实声明：(1) 同架构不同训练，不是跨架构；(2) 7B scale only；(3) 单 benchmark。机制解释 (discrimination collapse) 原则上 architecture-agnostic，但未实证验证。
36	- **实验支撑**: C5 (Qwen cross-model). 若需加强可扩展到不同架构（如 LLaMA/Mistral），但 11 天 deadline 内不现实
37	
38	### RC2: Mechanism — entropy-discrimination collapse 缺乏直接测量
39	- **预期质疑**: "The mechanism is conceptual. Where is the empirical evidence for entropy increase and discrimination collapse?"
40	- **应对**: c4_entropy 实验已完成（DeepSeek 30/30 + Qwen 30/30）。D044 结论：Gini/CV 下降跨模型一致（discrimination collapse confirmed）；entropy redistribution 在 DeepSeek 上一致但在 Qwen 上 s025 方向反转、s030 近零（model-dependent）。论文以 discrimination collapse 为主线，entropy 作 DeepSeek 特有的强化因素。
41	- **实验支撑**: c4_entropy (DeepSeek DONE) + qwen_c4_entropy (DONE, negative for entropy universality)
42	
43	### RC3: Practical impact — 没有 throughput 数据
44	- **预期质疑**: "No wall-clock or throughput measurements. Is the severity amplification reflected in actual inference speed?"
45	- **应对**: 本文定位是 empirical finding paper（发现 + 机制解释），不是 method paper。Throughput 不是 claim 的一部分。Discussion 中明确 phase-gated controller 作为 future direction。
46	- **实验支撑**: 不需要额外实验
47	
48	### RC4: Statistical rigor — bootstrap 是否足够
49	- **预期质疑**: "Per-problem bootstrap with 50 problems — sufficient sample size?"
50	- **应对**: bf16 使用 B=10000 per-problem paired bootstrap，有效配对数 n=49 (DeepSeek) / n=46 (Qwen)。Permutation test 使用 paired median difference 作为 robust statistic（D032），Bonferroni 校正后全 4 水平 p<0.005。Cohen's d（per-problem paired）作为辅助效应量（DeepSeek 0.61→1.13, Qwen 0.37→1.44）。可在 appendix 补充 per-problem 分布图（已生成 fig4_per_problem_dist.pdf）。
51	- **实验支撑**: bf16 permutation test (D032) + Cohen's d per-problem paired (rebootstrap B=10000) 已完成
52	
53	### RC5: Novelty — prior work 是否已覆盖 phase-dependent sparsity
54	- **预期质疑**: "ThinKV and phase-aware methods already consider phase. What's new?"
55	- **应对**: Prior work 在单轴上分析 phase（ThinKV: phase-aware eviction）或 compound（SparK: joint compression）。没有工作同时分析 compound × phase × strategy 的三维交互。Crossover 现象（同一 strategy 在不同 phase 方向反转）是全新发现。
56	- **实验支撑**: C3 (crossover), Related Work §2 的 gap 分析
57	
58	## Paper Positioning
59	
60	**类型**: Empirical finding paper（非 method paper）
61	**核心贡献**:
62	1. 发现 compound sparsity severity 的 strategy × phase 交互
63	2. 量化 severity gradient（bf16 paired median difference 0.32→9.94, Cohen's d 0.61→1.13）和 crossover 现象
64	3. 提出 discrimination collapse 机制解释（Gini/CV 跨模型一致；entropy redistribution model-dependent）
65	4. Cross-model replication 验证泛化性
66	
67	**投稿目标**: EMNLP 2026 ARR, deadline 2026-05-25
68	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LP3Uh1fWxdN8jFGJzRtP4T",
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "e0eedcab-e76b-4bfa-b51f-31f11fe10e09"
}
```

</details>

---

### System

_source line 37_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4a5e16a935552112",
  "tool_use_id": "toolu_01LP3Uh1fWxdN8jFGJzRtP4T",
  "description": "Reading artifacts/dream_reports/dream_20260514T054026/best/paper_framing.md",
  "usage": {
    "total_tokens": 18880,
    "tool_uses": 3,
    "duration_ms": 3323
  },
  "last_tool_name": "Read",
  "uuid": "17f7c074-620d-4064-989d-2284a847ebcf",
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86"
}
```

---

### Tool call

_source line 38_

<details open><summary>🔧 Tool call — Read · `toolu_01CEmeQmNK1DnbmGW73VLhK8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260514T054026/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LP3Uh1fWxdN8jFGJzRtP4T",
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "32c35a4c-ad14-4409-a7cd-46fe306cd3e8",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014xqrzGvxxDmYTpnwvHCnBr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1050,
      "cache_read_input_tokens": 17812,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1050,
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

_source line 39 · 2026-05-14T09:45:23.289Z_

<details><summary>↩ Tool result · `toolu_01CEmeQmNK1DnbmGW73VLhK8`</summary>

```text
1	# Paper Framing — Phase-Gated Compound Sparsity
2	
3	> 最后更新: 2026-05-14 | 维护者: Director
4	
5	## Core Insight
6	
7	Compound sparsity（attention head pruning + KV cache eviction）的 severity 不是固定常数——它是 eviction strategy 和 reasoning phase 交互的涌现属性。Importance-based eviction 在 low-sparsity reasoning phase 产生 12-75× severity amplification，而 random eviction 保持 ~1× 平坦。这一发现挑战了 compound degradation 均匀分布的隐含假设。
8	
9	## Narrative Arc
10	
11	Compound sparsity 是高效 LLM 推理的实用部署需求，但 prior work（SparK, Ada-KV, SLiM）将 compound interaction 视为均匀超可加。我们发现 severity 是 strategy × phase 交互的涌现属性：importance eviction 在 distributed-attention phase 剧烈放大 compound degradation（gradient 12-75×），而 random eviction 在所有 phase 保持平坦（~1×）。我们通过 entropy-discrimination collapse 机制解释这一现象：head pruning → attention 重分布 → importance score 的判别力崩塌 → importance eviction 退化为有偏伪随机。这一发现为 phase-aware sparsity allocation 提供了动机。
12	
13	**Framing 硬约束（D015）**：
14	- MUST: "emergent phase-strategy interaction"
15	- MUST NOT: "importance metric limitation / importance is broken"
16	
17	## Core Claims
18	
19	| ID | Claim | Status | Key Evidence |
20	|----|-------|--------|-------------|
21	| C1 | Compound sparsity severity is strategy-dependent | confirmed | importance gradient 12-75× vs random ~1× |
22	| C2 | Severity is phase-modulated (amplified in low-sparsity phase) | confirmed | low phase >> high phase at all 4 sparsity levels; monotonic increase 12.8→28.7→52.9→74.9 |
23	| C3 | Phase-strategy crossover exists | confirmed | s=0.25: importance high_phase=0.584 < random=3.002, importance low_phase=30.903 > random=2.915 |
24	| C4 | Entropy-discrimination collapse explains the mechanism | partially_confirmed | Conceptual argument solid; empirical attention entropy data not yet collected |
25	| C5 | Finding generalizes across model families | pending | Qwen2.5-7B-Instruct experiments in progress |
26	| C6 | Severity gradient is sub-exponential | confirmed | Growth rate decreasing: 2.24×→1.84×→1.42× |
27	
28	## Anticipated Reviewer Concerns
29	
30	### RC1: Generalizability — 7B models only, single benchmark
31	- **预期质疑**: "Results on two 7B models and MATH-500 only. How do we know this generalizes to larger models or other reasoning tasks?"
32	- **应对**: Cross-model replication (DeepSeek + Qwen, 不同架构血统) 是第一层防御。MATH-500 是 standard benchmark。Limitations 明确声明 scale 限制。机制解释 (entropy-discrimination collapse) 是 architecture-agnostic 的，原则上适用于任何 attention-based model。
33	- **实验支撑**: C5 (Qwen cross-model), 若需加强可扩展到更多模型
34	
35	### RC2: Mechanism — entropy-discrimination collapse 缺乏直接测量
36	- **预期质疑**: "The mechanism is conceptual. Where is the empirical evidence for entropy increase and discrimination collapse?"
37	- **应对**: 如果有 GPU 预算，可以直接测量 pruned vs unpruned 的 attention entropy 和 importance score 分布。目前 C4 status = partially_confirmed，需要决定是否投入 GPU 时间做 direct measurement。
38	- **实验支撑**: 可选 ablation：测量 attention entropy pre/post pruning × phase
39	
40	### RC3: Practical impact — 没有 throughput 数据
41	- **预期质疑**: "No wall-clock or throughput measurements. Is the severity amplification reflected in actual inference speed?"
42	- **应对**: 本文定位是 empirical finding paper（发现 + 机制解释），不是 method paper。Throughput 不是 claim 的一部分。Discussion 中明确 phase-gated controller 作为 future direction。
43	- **实验支撑**: 不需要额外实验
44	
45	### RC4: Statistical rigor — bootstrap 是否足够
46	- **预期质疑**: "Per-problem bootstrap with 50 problems — sufficient sample size?"
47	- **应对**: B=10000 iterations, all p=0.0000, CI 不跨零。50 problems 的 paired bootstrap 统计效力已充分。可在 appendix 补充 per-problem 分布图。
48	- **实验支撑**: 已完成，fig4_bootstrap
49	
50	### RC5: Novelty — prior work 是否已覆盖 phase-dependent sparsity
51	- **预期质疑**: "ThinKV and phase-aware methods already consider phase. What's new?"
52	- **应对**: Prior work 在单轴上分析 phase（ThinKV: phase-aware eviction）或 compound（SparK: joint compression）。没有工作同时分析 compound × phase × strategy 的三维交互。Crossover 现象（同一 strategy 在不同 phase 方向反转）是全新发现。
53	- **实验支撑**: C3 (crossover), Related Work §2 的 gap 分析
54	
55	## Paper Positioning
56	
57	**类型**: Empirical finding paper（非 method paper）
58	**核心贡献**:
59	1. 发现 compound sparsity severity 的 strategy × phase 交互
60	2. 量化 severity gradient（12-75×）和 crossover 现象
61	3. 提出 entropy-discrimination collapse 机制解释
62	4. Cross-model replication 验证泛化性
63	
64	**投稿目标**: EMNLP 2026 ARR, deadline 2026-05-25
65	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LP3Uh1fWxdN8jFGJzRtP4T",
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "bd2f136f-f4fa-46d5-80ba-b326c156ca73"
}
```

</details>

---

### System

_source line 40_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4a5e16a935552112",
  "tool_use_id": "toolu_01LP3Uh1fWxdN8jFGJzRtP4T",
  "description": "Reading artifacts/dream_reports/dream_20260514T054026/median/paper_framing.md",
  "usage": {
    "total_tokens": 18881,
    "tool_uses": 4,
    "duration_ms": 3535
  },
  "last_tool_name": "Read",
  "uuid": "52578c07-feab-4e2a-a08d-d3e5262a8082",
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86"
}
```

---

### Tool call

_source line 41_

<details open><summary>🔧 Tool call — Read · `toolu_01CyZ73PaWrzbqwRfZSuvc5V`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260514T054026/median/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LP3Uh1fWxdN8jFGJzRtP4T",
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "fbbd904b-3ef0-4506-acfd-cd5b2fc4c758",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014xqrzGvxxDmYTpnwvHCnBr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1050,
      "cache_read_input_tokens": 17812,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1050,
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

_source line 42 · 2026-05-14T09:45:23.500Z_

<details><summary>↩ Tool result · `toolu_01CyZ73PaWrzbqwRfZSuvc5V`</summary>

```text
1	# Paper Framing — Phase-Gated Compound Sparsity
2	
3	> 最后更新: 2026-05-14 | 维护者: Director
4	
5	## Core Insight
6	
7	Compound sparsity（attention head pruning + KV cache eviction）的 severity 不是固定常数——它是 eviction strategy 和 reasoning phase 交互的涌现属性。Importance-based eviction 在 low-sparsity reasoning phase 产生 12-75× severity amplification，而 random eviction 保持 ~1× 平坦。这一发现挑战了 compound degradation 均匀分布的隐含假设。
8	
9	## Narrative Arc
10	
11	Compound sparsity 是高效 LLM 推理的实用部署需求，但 prior work（SparK, Ada-KV, SLiM）将 compound interaction 视为均匀超可加。我们发现 severity 是 strategy × phase 交互的涌现属性：importance eviction 在 distributed-attention phase 剧烈放大 compound degradation（gradient 12-75×），而 random eviction 在所有 phase 保持平坦（~1×）。我们通过 entropy-discrimination collapse 机制解释这一现象：head pruning → attention 重分布 → importance score 的判别力崩塌 → importance eviction 退化为有偏伪随机。这一发现为 phase-aware sparsity allocation 提供了动机。
12	
13	**Framing 硬约束（D015）**：
14	- MUST: "emergent phase-strategy interaction"
15	- MUST NOT: "importance metric limitation / importance is broken"
16	
17	## Core Claims
18	
19	| ID | Claim | Status | Key Evidence |
20	|----|-------|--------|-------------|
21	| C1 | Compound sparsity severity is strategy-dependent | confirmed | importance gradient 12-75× vs random ~1× |
22	| C2 | Severity is phase-modulated (amplified in low-sparsity phase) | confirmed | low phase >> high phase at all 4 sparsity levels; monotonic increase 12.8→28.7→52.9→74.9 |
23	| C3 | Phase-strategy crossover exists | confirmed | s=0.25: importance high_phase=0.584 < random=3.002, importance low_phase=30.903 > random=2.915 |
24	| C4 | Entropy-discrimination collapse explains the mechanism | partially_confirmed | Conceptual argument solid; empirical attention entropy data not yet collected |
25	| C5 | Finding generalizes across model families | pending | Qwen2.5-7B-Instruct experiments in progress |
26	| C6 | Severity gradient is sub-exponential | confirmed | Growth rate decreasing: 2.24×→1.84×→1.42× |
27	
28	## Anticipated Reviewer Concerns
29	
30	### RC1: Generalizability — 7B models only, single benchmark
31	- **预期质疑**: "Results on two 7B models and MATH-500 only. How do we know this generalizes to larger models or other reasoning tasks?"
32	- **应对**: Cross-model replication (DeepSeek + Qwen, 不同架构血统) 是第一层防御。MATH-500 是 standard benchmark。Limitations 明确声明 scale 限制。机制解释 (entropy-discrimination collapse) 是 architecture-agnostic 的，原则上适用于任何 attention-based model。
33	- **实验支撑**: C5 (Qwen cross-model), 若需加强可扩展到更多模型
34	
35	### RC2: Mechanism — entropy-discrimination collapse 缺乏直接测量
36	- **预期质疑**: "The mechanism is conceptual. Where is the empirical evidence for entropy increase and discrimination collapse?"
37	- **应对**: 如果有 GPU 预算，可以直接测量 pruned vs unpruned 的 attention entropy 和 importance score 分布。目前 C4 status = partially_confirmed，需要决定是否投入 GPU 时间做 direct measurement。
38	- **实验支撑**: 可选 ablation：测量 attention entropy pre/post pruning × phase
39	
40	### RC3: Practical impact — 没有 throughput 数据
41	- **预期质疑**: "No wall-clock or throughput measurements. Is the severity amplification reflected in actual inference speed?"
42	- **应对**: 本文定位是 empirical finding paper（发现 + 机制解释），不是 method paper。Throughput 不是 claim 的一部分。Discussion 中明确 phase-gated controller 作为 future direction。
43	- **实验支撑**: 不需要额外实验
44	
45	### RC4: Statistical rigor — bootstrap 是否足够
46	- **预期质疑**: "Per-problem bootstrap with 50 problems — sufficient sample size?"
47	- **应对**: B=10000 iterations, all p=0.0000, CI 不跨零。50 problems 的 paired bootstrap 统计效力已充分。可在 appendix 补充 per-problem 分布图。
48	- **实验支撑**: 已完成，fig4_bootstrap
49	
50	### RC5: Novelty — prior work 是否已覆盖 phase-dependent sparsity
51	- **预期质疑**: "ThinKV and phase-aware methods already consider phase. What's new?"
52	- **应对**: Prior work 在单轴上分析 phase（ThinKV: phase-aware eviction）或 compound（SparK: joint compression）。没有工作同时分析 compound × phase × strategy 的三维交互。Crossover 现象（同一 strategy 在不同 phase 方向反转）是全新发现。
53	- **实验支撑**: C3 (crossover), Related Work §2 的 gap 分析
54	
55	## Paper Positioning
56	
57	**类型**: Empirical finding paper（非 method paper）
58	**核心贡献**:
59	1. 发现 compound sparsity severity 的 strategy × phase 交互
60	2. 量化 severity gradient（12-75×）和 crossover 现象
61	3. 提出 entropy-discrimination collapse 机制解释
62	4. Cross-model replication 验证泛化性
63	
64	**投稿目标**: EMNLP 2026 ARR, deadline 2026-05-25
65	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LP3Uh1fWxdN8jFGJzRtP4T",
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "41792349-c771-40c2-9caa-0d86c6dcd076"
}
```

</details>

---

### System

_source line 43_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4a5e16a935552112",
  "tool_use_id": "toolu_01LP3Uh1fWxdN8jFGJzRtP4T",
  "description": "Reading artifacts/dream_reports/dream_20260514T054026/worst/paper_framing.md",
  "usage": {
    "total_tokens": 18882,
    "tool_uses": 5,
    "duration_ms": 3749
  },
  "last_tool_name": "Read",
  "uuid": "2d4efd61-5959-4da0-ba8e-f411cb7c6ff5",
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86"
}
```

---

### Tool call

_source line 44_

<details open><summary>🔧 Tool call — Read · `toolu_01LjdtKtV9EVsLGVHua738D5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260514T054026/worst/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LP3Uh1fWxdN8jFGJzRtP4T",
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "5ebe1ea6-9f2b-4a2b-a83a-f3001fd289b3",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014xqrzGvxxDmYTpnwvHCnBr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1050,
      "cache_read_input_tokens": 17812,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1050,
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

_source line 45 · 2026-05-14T09:45:23.712Z_

<details><summary>↩ Tool result · `toolu_01LjdtKtV9EVsLGVHua738D5`</summary>

```text
1	# Paper Framing — Phase-Gated Compound Sparsity
2	
3	> 最后更新: 2026-05-14 | 维护者: Director
4	
5	## Core Insight
6	
7	Compound sparsity（attention head pruning + KV cache eviction）的 severity 不是固定常数——它是 eviction strategy 和 reasoning phase 交互的涌现属性。Importance-based eviction 在 low-sparsity reasoning phase 产生 12-75× severity amplification，而 random eviction 保持 ~1× 平坦。这一发现挑战了 compound degradation 均匀分布的隐含假设。
8	
9	## Narrative Arc
10	
11	Compound sparsity 是高效 LLM 推理的实用部署需求，但 prior work（SparK, Ada-KV, SLiM）将 compound interaction 视为均匀超可加。我们发现 severity 是 strategy × phase 交互的涌现属性：importance eviction 在 distributed-attention phase 剧烈放大 compound degradation（gradient 12-75×），而 random eviction 在所有 phase 保持平坦（~1×）。我们通过 entropy-discrimination collapse 机制解释这一现象：head pruning → attention 重分布 → importance score 的判别力崩塌 → importance eviction 退化为有偏伪随机。这一发现为 phase-aware sparsity allocation 提供了动机。
12	
13	**Framing 硬约束（D015）**：
14	- MUST: "emergent phase-strategy interaction"
15	- MUST NOT: "importance metric limitation / importance is broken"
16	
17	## Core Claims
18	
19	| ID | Claim | Status | Key Evidence |
20	|----|-------|--------|-------------|
21	| C1 | Compound sparsity severity is strategy-dependent | confirmed | importance gradient 12-75× vs random ~1× |
22	| C2 | Severity is phase-modulated (amplified in low-sparsity phase) | confirmed | low phase >> high phase at all 4 sparsity levels; monotonic increase 12.8→28.7→52.9→74.9 |
23	| C3 | Phase-strategy crossover exists | confirmed | s=0.25: importance high_phase=0.584 < random=3.002, importance low_phase=30.903 > random=2.915 |
24	| C4 | Entropy-discrimination collapse explains the mechanism | partially_confirmed | Conceptual argument solid; empirical attention entropy data not yet collected |
25	| C5 | Finding generalizes across model families | pending | Qwen2.5-7B-Instruct experiments in progress |
26	| C6 | Severity gradient is sub-exponential | confirmed | Growth rate decreasing: 2.24×→1.84×→1.42× |
27	
28	## Anticipated Reviewer Concerns
29	
30	### RC1: Generalizability — 7B models only, single benchmark
31	- **预期质疑**: "Results on two 7B models and MATH-500 only. How do we know this generalizes to larger models or other reasoning tasks?"
32	- **应对**: Cross-model replication (DeepSeek + Qwen, 不同架构血统) 是第一层防御。MATH-500 是 standard benchmark。Limitations 明确声明 scale 限制。机制解释 (entropy-discrimination collapse) 是 architecture-agnostic 的，原则上适用于任何 attention-based model。
33	- **实验支撑**: C5 (Qwen cross-model), 若需加强可扩展到更多模型
34	
35	### RC2: Mechanism — entropy-discrimination collapse 缺乏直接测量
36	- **预期质疑**: "The mechanism is conceptual. Where is the empirical evidence for entropy increase and discrimination collapse?"
37	- **应对**: 如果有 GPU 预算，可以直接测量 pruned vs unpruned 的 attention entropy 和 importance score 分布。目前 C4 status = partially_confirmed，需要决定是否投入 GPU 时间做 direct measurement。
38	- **实验支撑**: 可选 ablation：测量 attention entropy pre/post pruning × phase
39	
40	### RC3: Practical impact — 没有 throughput 数据
41	- **预期质疑**: "No wall-clock or throughput measurements. Is the severity amplification reflected in actual inference speed?"
42	- **应对**: 本文定位是 empirical finding paper（发现 + 机制解释），不是 method paper。Throughput 不是 claim 的一部分。Discussion 中明确 phase-gated controller 作为 future direction。
43	- **实验支撑**: 不需要额外实验
44	
45	### RC4: Statistical rigor — bootstrap 是否足够
46	- **预期质疑**: "Per-problem bootstrap with 50 problems — sufficient sample size?"
47	- **应对**: B=10000 iterations, all p=0.0000, CI 不跨零。50 problems 的 paired bootstrap 统计效力已充分。可在 appendix 补充 per-problem 分布图。
48	- **实验支撑**: 已完成，fig4_bootstrap
49	
50	### RC5: Novelty — prior work 是否已覆盖 phase-dependent sparsity
51	- **预期质疑**: "ThinKV and phase-aware methods already consider phase. What's new?"
52	- **应对**: Prior work 在单轴上分析 phase（ThinKV: phase-aware eviction）或 compound（SparK: joint compression）。没有工作同时分析 compound × phase × strategy 的三维交互。Crossover 现象（同一 strategy 在不同 phase 方向反转）是全新发现。
53	- **实验支撑**: C3 (crossover), Related Work §2 的 gap 分析
54	
55	## Paper Positioning
56	
57	**类型**: Empirical finding paper（非 method paper）
58	**核心贡献**:
59	1. 发现 compound sparsity severity 的 strategy × phase 交互
60	2. 量化 severity gradient（12-75×）和 crossover 现象
61	3. 提出 entropy-discrimination collapse 机制解释
62	4. Cross-model replication 验证泛化性
63	
64	**投稿目标**: EMNLP 2026 ARR, deadline 2026-05-25
65	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LP3Uh1fWxdN8jFGJzRtP4T",
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "9a9b5c53-7199-4282-ac74-956ceabe06b4"
}
```

</details>

---

### System

_source line 46_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a4a5e16a935552112",
  "tool_use_id": "toolu_01LP3Uh1fWxdN8jFGJzRtP4T",
  "status": "completed",
  "output_file": "",
  "summary": "Find paper_framing.md",
  "usage": {
    "total_tokens": 27346,
    "tool_uses": 5,
    "duration_ms": 11082
  },
  "uuid": "4fa2795b-a119-41fb-a4f9-c1dd7cda975f",
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86"
}
```

---

### Tool result

_source line 47 · 2026-05-14T09:45:31.043Z_

<details><summary>↩ Tool result · `toolu_01LP3Uh1fWxdN8jFGJzRtP4T`</summary>

```text
Found 4 instances of paper_framing.md files:

**Main File:**
- **/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper_framing.md**

**Additional copies in dream_reports artifacts:**
- /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260514T054026/best/paper_framing.md
- /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260514T054026/median/paper_framing.md
- /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260514T054026/worst/paper_framing.md

The main file contains the most current version (updated 2026-05-14 09:20 UTC) with the most detailed information. The artifact copies appear to be from earlier iterations with slightly less detailed content.

**Summary of main file contents:**

The paper framing document outlines research on "Phase-Gated Compound Sparsity" - studying how compound sparsity (attention head pruning + KV cache eviction) severity emerges from the interaction between eviction strategy and reasoning phase. Key findings include:

- Compound sparsity severity is strategy-dependent: importance-based eviction shows increasing severity (0.32→9.94 paired median difference) while random masking remains flat
- Severity is phase-modulated, with amplification in low-sparsity phases
- A phase-strategy crossover phenomenon exists
- Discrimination collapse (Gini/CV decrease across models) is the primary explanatory mechanism
- Findings generalize across model families (DeepSeek-R1-Distill-Qwen-7B + Qwen2.5-7B-Instruct)
- The paper is positioned as an empirical finding paper targeted at EMNLP 2026 ARR (deadline 2026-05-25)

The document includes core claims with evidence, anticipated reviewer concerns and responses, and detailed framing constraints for the paper narrative.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "9aa6d51e-37ef-44e8-aca5-8b0ce06f5a49",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Find any file named paper_framing.md or similar in /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/. Search recursively. Report the full path and its contents.",
    "agentId": "a4a5e16a935552112",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Found 4 instances of paper_framing.md files:\n\n**Main File:**\n- **/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper_framing.md**\n\n**Additional copies in dream_reports artifacts:**\n- /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260514T054026/best/paper_framing.md\n- /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260514T054026/median/paper_framing.md\n- /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260514T054026/worst/paper_framing.md\n\nThe main file contains the most current version (updated 2026-05-14 09:20 UTC) with the most detailed information. The artifact copies appear to be from earlier iterations with slightly less detailed content.\n\n**Summary of main file contents:**\n\nThe paper framing document outlines research on \"Phase-Gated Compound Sparsity\" - studying how compound sparsity (attention head pruning + KV cache eviction) severity emerges from the interaction between eviction strategy and reasoning phase. Key findings include:\n\n- Compound sparsity severity is strategy-dependent: importance-based eviction shows increasing severity (0.32→9.94 paired median difference) while random masking remains flat\n- Severity is phase-modulated, with amplification in low-sparsity phases\n- A phase-strategy crossover phenomenon exists\n- Discrimination collapse (Gini/CV decrease across models) is the primary explanatory mechanism\n- Findings generalize across model families (DeepSeek-R1-Distill-Qwen-7B + Qwen2.5-7B-Instruct)\n- The paper is positioned as an empirical finding paper targeted at EMNLP 2026 ARR (deadline 2026-05-25)\n\nThe document includes core claims with evidence, anticipated reviewer concerns and responses, and detailed framing constraints for the paper narrative."
      }
    ],
    "totalDurationMs": 11085,
    "totalTokens": 27879,
    "totalToolUseCount": 5,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 8462,
      "cache_read_input_tokens": 18862,
      "output_tokens": 549,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8462
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 549,
          "cache_read_input_tokens": 18862,
          "cache_creation_input_tokens": 8462,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8462,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 4,
      "searchCount": 1,
      "bashCount": 0,
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

_source line 48_

<details><summary>Logged reasoning block</summary>

```text
Let me read the paper_framing.md for core claims, and the stale files to check for PENDING-BF16 or placeholder marks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "fa8cf53d-1d08-41c9-8dc8-da2b308351a1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011XB9F3MuVPZk5RriZiiNzs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 184,
      "cache_creation_input_tokens": 872,
      "cache_read_input_tokens": 50116,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 872
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

_source line 49_

<details open><summary>🔧 Tool call — Read · `toolu_017mjj7PQsB6iTHzkY4Aygye`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "4a27ce2b-915f-4bb8-9769-937a2f3c52f3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011XB9F3MuVPZk5RriZiiNzs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 184,
      "cache_creation_input_tokens": 872,
      "cache_read_input_tokens": 50116,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 872
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

_source line 50 · 2026-05-14T09:45:35.262Z_

<details><summary>↩ Tool result · `toolu_017mjj7PQsB6iTHzkY4Aygye`</summary>

```text
1	# Paper Framing — Phase-Gated Compound Sparsity
2	
3	> 最后更新: 2026-05-14 09:20 UTC | 维护者: Director
4	
5	## Core Insight
6	
7	Compound sparsity（attention head pruning + KV cache eviction）的 severity 不是固定常数——它是 eviction strategy 和 reasoning phase 交互的涌现属性。Importance-based eviction 的 compound interaction severity（paired median difference: median(II_low_i − II_high_i)）随 sparsity 单调递增（DeepSeek: 0.32→1.15→3.97→9.94; Qwen: 0.048→0.208→1.109→2.619），而 random masking 三相 II 持平（7/8 FAIL; Qwen s030 PASS p=0.012 but d=-0.04 negligible）。Cohen's d（per-problem paired, B=10000）从 medium 到 large（DeepSeek: 0.61→1.13; Qwen: 0.37→1.44，s015 边缘）。这一发现挑战了 compound degradation 均匀分布的隐含假设。
8	
9	**数字基准**：所有数字基于 bf16 per-problem paired 统计量（B=10000 bootstrap）。median_diff 定义为 median(II_low_i − II_high_i)（逐 problem 配对差的中位数）。fp16 旧数据已弃用。
10	
11	## Narrative Arc
12	
13	Compound sparsity 是高效 LLM 推理的实用部署需求，但 prior work（SparK, Ada-KV, SLiM）将 compound interaction 视为均匀超可加。我们发现 severity 是 strategy × phase 交互的涌现属性：importance eviction 的 compound interaction 在 low-sparsity phase 远大于 high-sparsity phase（paired median difference 单调递增 0.32→9.94），而 random eviction 在所有 phase 保持平坦（7/8 FAIL; 唯一例外 Qwen s030 p=0.012 效应量可忽略 d=-0.04）。Cross-model replication 方向一致（Qwen magnitude ~1/4 of DeepSeek，onset threshold s≥0.20）。我们通过 discrimination collapse 机制解释这一现象：head pruning → importance score 的判别力崩塌（Gini/CV 下降跨模型一致）→ importance eviction 退化为有偏伪随机。Attention entropy redistribution 作为 model-dependent secondary effect 在 DeepSeek 上观察到，但在 Qwen 上不稳健（D044）。
14	
15	**Framing 硬约束（D015）**：
16	- MUST: "emergent phase-strategy interaction"
17	- MUST NOT: "importance metric limitation / importance is broken"
18	- MUST NOT: claim "importance masking produces super-additive interaction" without qualifier — random masking also produces positive II. The distinguishing signal is **phase-dependent gradient** (importance: paired median difference 0.32→9.94 单调递增 vs random: 7/8 FAIL), not the existence of super-additivity itself (D023)
19	
20	## Core Claims
21	
22	| ID | Claim | Status | Key Evidence |
23	|----|-------|--------|-------------|
24	| C1 | Compound sparsity severity is strategy-dependent | confirmed | importance paired median diff 0.32→9.94 单调递增 vs random 7/8 FAIL (bf16; Qwen s030 PASS p=0.012 d=-0.04 negligible) |
25	| C2 | Severity is phase-modulated (amplified in low-sparsity phase) | confirmed | bf16 paired median difference 单调递增: 0.32→1.15→3.97→9.94; Bonferroni p<0.005 全 4 水平 (D032) |
26	| C3 | Phase-strategy crossover exists | confirmed | s=0.25: importance high_phase=0.032 < random=0.818, importance low_phase=7.196 > random=1.363 (bf16) |
27	| C4 | Discrimination collapse as primary mechanism; entropy redistribution model-dependent | partially_confirmed | D044: Gini/CV 下降跨模型一致; entropy collapse DeepSeek 一致但 Qwen s025 反转(+0.045) s030≈0。30/30 problems completed. |
28	| C5 | Finding generalizes across models (same arch, different training) | confirmed | Qwen importance 4/4 PASS，paired median diff 0.048→2.619 单调递增。Cohen's d (paired) s≥0.20 显著，s015 边缘。Cross-model 非 cross-architecture。 |
29	| C6 | Severity gradient is sub-exponential | confirmed | Growth rate decreasing: Δ增长因子 3.8×→4.8×→2.0×（递减） |
30	
31	## Anticipated Reviewer Concerns
32	
33	### RC1: Generalizability — 7B models only, single benchmark
34	- **预期质疑**: "Results on two 7B models and MATH-500 only. How do we know this generalizes to larger models or other reasoning tasks?"
35	- **应对**: Cross-model replication (DeepSeek-R1-Distill-Qwen-7B + Qwen2.5-7B-Instruct) 控制架构变量、隔离训练方式影响（distillation vs instruction tuning）。注意：两模型共享 Qwen2ForCausalLM 架构，不能 claim 跨架构泛化。MATH-500 是 standard benchmark。Limitations 必须诚实声明：(1) 同架构不同训练，不是跨架构；(2) 7B scale only；(3) 单 benchmark。机制解释 (discrimination collapse) 原则上 architecture-agnostic，但未实证验证。
36	- **实验支撑**: C5 (Qwen cross-model). 若需加强可扩展到不同架构（如 LLaMA/Mistral），但 11 天 deadline 内不现实
37	
38	### RC2: Mechanism — entropy-discrimination collapse 缺乏直接测量
39	- **预期质疑**: "The mechanism is conceptual. Where is the empirical evidence for entropy increase and discrimination collapse?"
40	- **应对**: c4_entropy 实验已完成（DeepSeek 30/30 + Qwen 30/30）。D044 结论：Gini/CV 下降跨模型一致（discrimination collapse confirmed）；entropy redistribution 在 DeepSeek 上一致但在 Qwen 上 s025 方向反转、s030 近零（model-dependent）。论文以 discrimination collapse 为主线，entropy 作 DeepSeek 特有的强化因素。
41	- **实验支撑**: c4_entropy (DeepSeek DONE) + qwen_c4_entropy (DONE, negative for entropy universality)
42	
43	### RC3: Practical impact — 没有 throughput 数据
44	- **预期质疑**: "No wall-clock or throughput measurements. Is the severity amplification reflected in actual inference speed?"
45	- **应对**: 本文定位是 empirical finding paper（发现 + 机制解释），不是 method paper。Throughput 不是 claim 的一部分。Discussion 中明确 phase-gated controller 作为 future direction。
46	- **实验支撑**: 不需要额外实验
47	
48	### RC4: Statistical rigor — bootstrap 是否足够
49	- **预期质疑**: "Per-problem bootstrap with 50 problems — sufficient sample size?"
50	- **应对**: bf16 使用 B=10000 per-problem paired bootstrap，有效配对数 n=49 (DeepSeek) / n=46 (Qwen)。Permutation test 使用 paired median difference 作为 robust statistic（D032），Bonferroni 校正后全 4 水平 p<0.005。Cohen's d（per-problem paired）作为辅助效应量（DeepSeek 0.61→1.13, Qwen 0.37→1.44）。可在 appendix 补充 per-problem 分布图（已生成 fig4_per_problem_dist.pdf）。
51	- **实验支撑**: bf16 permutation test (D032) + Cohen's d per-problem paired (rebootstrap B=10000) 已完成
52	
53	### RC5: Novelty — prior work 是否已覆盖 phase-dependent sparsity
54	- **预期质疑**: "ThinKV and phase-aware methods already consider phase. What's new?"
55	- **应对**: Prior work 在单轴上分析 phase（ThinKV: phase-aware eviction）或 compound（SparK: joint compression）。没有工作同时分析 compound × phase × strategy 的三维交互。Crossover 现象（同一 strategy 在不同 phase 方向反转）是全新发现。
56	- **实验支撑**: C3 (crossover), Related Work §2 的 gap 分析
57	
58	## Paper Positioning
59	
60	**类型**: Empirical finding paper（非 method paper）
61	**核心贡献**:
62	1. 发现 compound sparsity severity 的 strategy × phase 交互
63	2. 量化 severity gradient（bf16 paired median difference 0.32→9.94, Cohen's d 0.61→1.13）和 crossover 现象
64	3. 提出 discrimination collapse 机制解释（Gini/CV 跨模型一致；entropy redistribution model-dependent）
65	4. Cross-model replication 验证泛化性
66	
67	**投稿目标**: EMNLP 2026 ARR, deadline 2026-05-25
68	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "46efb56b-b57d-4446-ae81-0a48071d7529",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper_framing.md",
      "content": "# Paper Framing — Phase-Gated Compound Sparsity\n\n> 最后更新: 2026-05-14 09:20 UTC | 维护者: Director\n\n## Core Insight\n\nCompound sparsity（attention head pruning + KV cache eviction）的 severity 不是固定常数——它是 eviction strategy 和 reasoning phase 交互的涌现属性。Importance-based eviction 的 compound interaction severity（paired median difference: median(II_low_i − II_high_i)）随 sparsity 单调递增（DeepSeek: 0.32→1.15→3.97→9.94; Qwen: 0.048→0.208→1.109→2.619），而 random masking 三相 II 持平（7/8 FAIL; Qwen s030 PASS p=0.012 but d=-0.04 negligible）。Cohen's d（per-problem paired, B=10000）从 medium 到 large（DeepSeek: 0.61→1.13; Qwen: 0.37→1.44，s015 边缘）。这一发现挑战了 compound degradation 均匀分布的隐含假设。\n\n**数字基准**：所有数字基于 bf16 per-problem paired 统计量（B=10000 bootstrap）。median_diff 定义为 median(II_low_i − II_high_i)（逐 problem 配对差的中位数）。fp16 旧数据已弃用。\n\n## Narrative Arc\n\nCompound sparsity 是高效 LLM 推理的实用部署需求，但 prior work（SparK, Ada-KV, SLiM）将 compound interaction 视为均匀超可加。我们发现 severity 是 strategy × phase 交互的涌现属性：importance eviction 的 compound interaction 在 low-sparsity phase 远大于 high-sparsity phase（paired median difference 单调递增 0.32→9.94），而 random eviction 在所有 phase 保持平坦（7/8 FAIL; 唯一例外 Qwen s030 p=0.012 效应量可忽略 d=-0.04）。Cross-model replication 方向一致（Qwen magnitude ~1/4 of DeepSeek，onset threshold s≥0.20）。我们通过 discrimination collapse 机制解释这一现象：head pruning → importance score 的判别力崩塌（Gini/CV 下降跨模型一致）→ importance eviction 退化为有偏伪随机。Attention entropy redistribution 作为 model-dependent secondary effect 在 DeepSeek 上观察到，但在 Qwen 上不稳健（D044）。\n\n**Framing 硬约束（D015）**：\n- MUST: \"emergent phase-strategy interaction\"\n- MUST NOT: \"importance metric limitation / importance is broken\"\n- MUST NOT: claim \"importance masking produces super-additive interaction\" without qualifier — random masking also produces positive II. The distinguishing signal is **phase-dependent gradient** (importance: paired median difference 0.32→9.94 单调递增 vs random: 7/8 FAIL), not the existence of super-additivity itself (D023)\n\n## Core Claims\n\n| ID | Claim | Status | Key Evidence |\n|----|-------|--------|-------------|\n| C1 | Compound sparsity severity is strategy-dependent | confirmed | importance paired median diff 0.32→9.94 单调递增 vs random 7/8 FAIL (bf16; Qwen s030 PASS p=0.012 d=-0.04 negligible) |\n| C2 | Severity is phase-modulated (amplified in low-sparsity phase) | confirmed | bf16 paired median difference 单调递增: 0.32→1.15→3.97→9.94; Bonferroni p<0.005 全 4 水平 (D032) |\n| C3 | Phase-strategy crossover exists | confirmed | s=0.25: importance high_phase=0.032 < random=0.818, importance low_phase=7.196 > random=1.363 (bf16) |\n| C4 | Discrimination collapse as primary mechanism; entropy redistribution model-dependent | partially_confirmed | D044: Gini/CV 下降跨模型一致; entropy collapse DeepSeek 一致但 Qwen s025 反转(+0.045) s030≈0。30/30 problems completed. |\n| C5 | Finding generalizes across models (same arch, different training) | confirmed | Qwen importance 4/4 PASS，paired median diff 0.048→2.619 单调递增。Cohen's d (paired) s≥0.20 显著，s015 边缘。Cross-model 非 cross-architecture。 |\n| C6 | Severity gradient is sub-exponential | confirmed | Growth rate decreasing: Δ增长因子 3.8×→4.8×→2.0×（递减） |\n\n## Anticipated Reviewer Concerns\n\n### RC1: Generalizability — 7B models only, single benchmark\n- **预期质疑**: \"Results on two 7B models and MATH-500 only. How do we know this generalizes to larger models or other reasoning tasks?\"\n- **应对**: Cross-model replication (DeepSeek-R1-Distill-Qwen-7B + Qwen2.5-7B-Instruct) 控制架构变量、隔离训练方式影响（distillation vs instruction tuning）。注意：两模型共享 Qwen2ForCausalLM 架构，不能 claim 跨架构泛化。MATH-500 是 standard benchmark。Limitations 必须诚实声明：(1) 同架构不同训练，不是跨架构；(2) 7B scale only；(3) 单 benchmark。机制解释 (discrimination collapse) 原则上 architecture-agnostic，但未实证验证。\n- **实验支撑**: C5 (Qwen cross-model). 若需加强可扩展到不同架构（如 LLaMA/Mistral），但 11 天 deadline 内不现实\n\n### RC2: Mechanism — entropy-discrimination collapse 缺乏直接测量\n- **预期质疑**: \"The mechanism is conceptual. Where is the empirical evidence for entropy increase and discrimination collapse?\"\n- **应对**: c4_entropy 实验已完成（DeepSeek 30/30 + Qwen 30/30）。D044 结论：Gini/CV 下降跨模型一致（discrimination collapse confirmed）；entropy redistribution 在 DeepSeek 上一致但在 Qwen 上 s025 方向反转、s030 近零（model-dependent）。论文以 discrimination collapse 为主线，entropy 作 DeepSeek 特有的强化因素。\n- **实验支撑**: c4_entropy (DeepSeek DONE) + qwen_c4_entropy (DONE, negative for entropy universality)\n\n### RC3: Practical impact — 没有 throughput 数据\n- **预期质疑**: \"No wall-clock or throughput measurements. Is the severity amplification reflected in actual inference speed?\"\n- **应对**: 本文定位是 empirical finding paper（发现 + 机制解释），不是 method paper。Throughput 不是 claim 的一部分。Discussion 中明确 phase-gated controller 作为 future direction。\n- **实验支撑**: 不需要额外实验\n\n### RC4: Statistical rigor — bootstrap 是否足够\n- **预期质疑**: \"Per-problem bootstrap with 50 problems — sufficient sample size?\"\n- **应对**: bf16 使用 B=10000 per-problem paired bootstrap，有效配对数 n=49 (DeepSeek) / n=46 (Qwen)。Permutation test 使用 paired median difference 作为 robust statistic（D032），Bonferroni 校正后全 4 水平 p<0.005。Cohen's d（per-problem paired）作为辅助效应量（DeepSeek 0.61→1.13, Qwen 0.37→1.44）。可在 appendix 补充 per-problem 分布图（已生成 fig4_per_problem_dist.pdf）。\n- **实验支撑**: bf16 permutation test (D032) + Cohen's d per-problem paired (rebootstrap B=10000) 已完成\n\n### RC5: Novelty — prior work 是否已覆盖 phase-dependent sparsity\n- **预期质疑**: \"ThinKV and phase-aware methods already consider phase. What's new?\"\n- **应对**: Prior work 在单轴上分析 phase（ThinKV: phase-aware eviction）或 compound（SparK: joint compression）。没有工作同时分析 compound × phase × strategy 的三维交互。Crossover 现象（同一 strategy 在不同 phase 方向反转）是全新发现。\n- **实验支撑**: C3 (crossover), Related Work §2 的 gap 分析\n\n## Paper Positioning\n\n**类型**: Empirical finding paper（非 method paper）\n**核心贡献**:\n1. 发现 compound sparsity severity 的 strategy × phase 交互\n2. 量化 severity gradient（bf16 paired median difference 0.32→9.94, Cohen's d 0.61→1.13）和 crossover 现象\n3. 提出 discrimination collapse 机制解释（Gini/CV 跨模型一致；entropy redistribution model-dependent）\n4. Cross-model replication 验证泛化性\n\n**投稿目标**: EMNLP 2026 ARR, deadline 2026-05-25\n",
      "numLines": 68,
      "startLine": 1,
      "totalLines": 68
    }
  }
}
```

</details>

---

### Tool call

_source line 51_

<details open><summary>🔧 Tool call — Read · `toolu_01PmiPm93evytZ4QuiuFNuBH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results_5_1.tex",
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
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "8d5e4229-cf4c-49ec-9bb9-dcb1577ebf52",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011XB9F3MuVPZk5RriZiiNzs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 184,
      "cache_creation_input_tokens": 872,
      "cache_read_input_tokens": 50116,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 872
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

_source line 52 · 2026-05-14T09:45:35.731Z_

<details><summary>↩ Tool result · `toolu_01PmiPm93evytZ4QuiuFNuBH`</summary>

```text
1	% Section 5.1: Phase-Modulated Severity Gradient
2	% Data source: v6_importance_s015/s020/s025/s030, mvp_v5_random_s015/s020/s025/s030
3	% All numeric values are from fp16 runs; bf16 replication pending.
4	
5	\subsection{Phase-Modulated Severity Gradient}
6	\label{sec:severity-gradient-fp16}
7	
8	Under importance-based eviction, compound interaction severity varies by an order of magnitude across reasoning phases:
9	the severity gradient $G$ (Eq.~\eqref{eq:gradient}) ranges from $11.5\times$ at $s{=}0.15$ to% PENDING-BF16
10	$41.9\times$ at $s{=}0.30$% PENDING-BF16
11	(paired bootstrap, $B{=}1{,}000$; Table~\ref{tab:bootstrap-fp16}).
12	Random eviction yields a flat gradient of $G \approx 0.7$--$1.8\times$% PENDING-BF16
13	across all sparsity levels (Table~\ref{tab:main-results-fp16}), confirming that phase modulation is specific to importance-based strategies rather than an inherent property of compound sparsity.
14	Figure~\ref{fig:hero-fp16} visualizes the divergent severity profiles of the two strategies.
15	
16	%%% Table 1: Main results %%%
17	\begin{table}[t]
18	\centering
19	\small
20	\caption{Median Interaction Index ($\widetilde{\mathrm{II}}$) by reasoning phase and severity gradient $G$ for importance-based and random eviction on DeepSeek-R1-Distill-Qwen-7B (50 MATH-500 problems).
21	$G$ for importance-based eviction is estimated via paired problem-level bootstrap ($B{=}1{,}000$);
22	$G$ for random eviction is the simple median ratio $\widetilde{\mathrm{II}}_{\textit{low}} / \widetilde{\mathrm{II}}_{\textit{high}}$.
23	Higher $G$ indicates stronger phase modulation.
24	All values from \texttt{float16} runs; \texttt{bfloat16} replication pending.}
25	\label{tab:main-results-fp16}
26	\begin{tabular}{@{}llrrrr@{}}
27	\toprule
28	Strategy & $s$ & $\widetilde{\mathrm{II}}_{\textit{high}}$ & $\widetilde{\mathrm{II}}_{\textit{mid}}$ & $\widetilde{\mathrm{II}}_{\textit{low}}$ & $G$ \\
29	\midrule
30	Importance & 0.15 & 0.23 & 0.74 & 2.88 & \textbf{11.53} \\ % PENDING-BF16
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "00dd7011-6d29-4387-a14f-a8ad33816250",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results_5_1.tex",
      "content": "% Section 5.1: Phase-Modulated Severity Gradient\n% Data source: v6_importance_s015/s020/s025/s030, mvp_v5_random_s015/s020/s025/s030\n% All numeric values are from fp16 runs; bf16 replication pending.\n\n\\subsection{Phase-Modulated Severity Gradient}\n\\label{sec:severity-gradient-fp16}\n\nUnder importance-based eviction, compound interaction severity varies by an order of magnitude across reasoning phases:\nthe severity gradient $G$ (Eq.~\\eqref{eq:gradient}) ranges from $11.5\\times$ at $s{=}0.15$ to% PENDING-BF16\n$41.9\\times$ at $s{=}0.30$% PENDING-BF16\n(paired bootstrap, $B{=}1{,}000$; Table~\\ref{tab:bootstrap-fp16}).\nRandom eviction yields a flat gradient of $G \\approx 0.7$--$1.8\\times$% PENDING-BF16\nacross all sparsity levels (Table~\\ref{tab:main-results-fp16}), confirming that phase modulation is specific to importance-based strategies rather than an inherent property of compound sparsity.\nFigure~\\ref{fig:hero-fp16} visualizes the divergent severity profiles of the two strategies.\n\n%%% Table 1: Main results %%%\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Median Interaction Index ($\\widetilde{\\mathrm{II}}$) by reasoning phase and severity gradient $G$ for importance-based and random eviction on DeepSeek-R1-Distill-Qwen-7B (50 MATH-500 problems).\n$G$ for importance-based eviction is estimated via paired problem-level bootstrap ($B{=}1{,}000$);\n$G$ for random eviction is the simple median ratio $\\widetilde{\\mathrm{II}}_{\\textit{low}} / \\widetilde{\\mathrm{II}}_{\\textit{high}}$.\nHigher $G$ indicates stronger phase modulation.\nAll values from \\texttt{float16} runs; \\texttt{bfloat16} replication pending.}\n\\label{tab:main-results-fp16}\n\\begin{tabular}{@{}llrrrr@{}}\n\\toprule\nStrategy & $s$ & $\\widetilde{\\mathrm{II}}_{\\textit{high}}$ & $\\widetilde{\\mathrm{II}}_{\\textit{mid}}$ & $\\widetilde{\\mathrm{II}}_{\\textit{low}}$ & $G$ \\\\\n\\midrule\nImportance & 0.15 & 0.23 & 0.74 & 2.88 & \\textbf{11.53} \\\\ % PENDING-BF16",
      "numLines": 30,
      "startLine": 1,
      "totalLines": 129
    }
  }
}
```

</details>

---

### Assistant

_source line 53_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data I need to perform the consistency audit. Let me systematically go through each check:

## 1. Number Consistency

### DeepSeek median severity diff Δ (segment-level: median(II_low) − median(II_high)):
- Task spec: 0.39 / 1.48 / 7.16 / 14.59
- abstract.tex line 7: "median Interaction Index difference between low-sparsity and high-sparsity reasoning phases increases monotonically from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$" — only mentions endpoints. ✓


- introduction.tex line 14: "the median phase difference in Interaction Index rises from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$" — endpoints only. ✓
- results.tex Table 1 and Table 2 both show the full sequence 0.39 / 1.48 / 7.16 / 14.59 with consistent calculations. ✓
- conclusion.tex and discussion.tex both reference these same values across the parameter range. ✓
- paper_framing.md uses a different metric—paired median differences of 0.32→1.15→3.97→9.94—which diverges from the segment-level measurements I've been tracking.

Now I'm noticing a critical discrepancy in the Cohen's d values. The abstract states d ranges from 0.44 to 0.80, but the introduction claims d goes from 0.61 to 1.13. These don't match, and I need to trace through all the references to figure out which is correct or if there's been a calculation error somewhere. I've found a critical inconsistency—the d=0.44/0.80 values in the abstract and conclusion don't match the d=0.61→1.13 reported elsewhere, and they don't appear in results.tex at all, suggesting they might be outdated metrics. Now I'm checking the other metrics: DeepSeek G's severity gradient values (69/103/222/274) are consistent across results.tex, analysis.tex, and discussion.tex, and the high-phase II numbers (0.006/0.015/0.032/0.053) also align in results.tex and discussion.tex. Now I'm checking the precision consistency across the documents—the discussion section lists full precision values like 0.235, but the results table rounds to 0.23, which creates a rounding discrepancy since 0.235 should round to 0.24 at two decimal places. No, 0.235 rounds to 0.24 if rounding half-up, but could be 0.23 if the underlying number is 0.2349... Let me check - discussion.tex says 0.235 which would present as 0.24 at 2dp. But in the table it says 0.23. So either 0.235 is slightly wrong or 0.23 is slightly wrong. Let me look again:

discussion.tex line 29: "$0.039 \to 0.235 \to 1.268 \to 2.943$"
results.tex Table cross-model: 0.04 / 0.23 / 1.27 / 2.94

0.039 rounds to 0.04 ✓
1.268 rounds to 1.27 ✓
2.943 rounds to 2.94 ✓

The 0.235 to 0.23 discrepancy is ambiguous depending on the exact underlying value, so I'll flag that as a potential inconsistency. But now I'm noticing something else — paper_framing.md has different numbers entirely for the Qwen paired median difference (0.048→0.208→1.109→2.619), which are per-problem values, whereas the segment-level aggregates in results.tex are 0.04/0.23/1.27/2.94. These appear to be measuring different things. So discussion.tex uses segment-level numbers matching the cross-model table, while paper_framing pulls from paired calculations. Now looking at Cohen's d values — the task spec and results table both show 0.37 / 0.72 / 1.23 / 1.44, and introduction.tex correctly cites d ≥ 0.72 at s≥0.20, but conclusion.tex claims d ≥ 0.55 which doesn't align with any of these values. I'm noticing the abstract also cites d ≥ 0.55 for Qwen, which contradicts the introduction's d ≥ 0.72 — both documents are making claims about the same result but with different effect size thresholds, and I need to figure out which is actually correct based on the raw data. So the 0.55 value in the abstract and conclusion appears to be outdated—the correct Cohen's d value from the table is 0.72, which matches what the introduction and results sections report. I'm now cross-checking the other metrics like the Spearman correlation and permutation p-value across all sections to ensure consistency throughout the document. me check) — discussion doesn't seem to mention 0.043 directly, but let me look...
  - discussion.tex line 25: "$p{=}0.043$" ✓

### Random: 7/8 FAIL, Qwen s030 PASS p=0.012 d=-0.04:
- abstract.tex line 8: "Random eviction produces no significant phase modulation in 7/8 conditions; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) shows negligible effect size ($d{=}{-}0.04$)" ✓
- introduction.tex line 16: "7/8 conditions across both models fail to exhibit a significant phase difference (the single exception---Qwen $s{=}0.30$---has negligible effect size, $d{=}{-}0.04$)" ✓
- conclusion.tex line 8: "7/8 conditions (the sole exception---Qwen $s{=}0.30$, $p{=}0.012$, $d{=}{-}0.04$---has negligible effect size)" ✓
- discussion.tex line 21: "7/8 FAIL; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) exhibits negligible effect size ($d{=}{-}0.04$)" ✓
- results.tex line 126: "borderline PASS (permutation $p = 0.012$) but with negligible effect size (Cohen's $d = -0.04$, CI spans zero)" ✓

Now checking the sample size references across the documents... Continuing to verify the remaining parameters—checking that B=10,000 is consistently formatted across methodology, results tables, and discussion sections, and confirming the Bonferroni correction threshold of p<0.005 appears in the abstract and introduction.

Now I'm examining the distinction between paired-level and segment-level effect sizes for DeepSeek, where the paired approach yields smaller deltas (0.32/1.15/3.97/9.94) compared to the segment-level values used in the main tables (0.39/1.48/7.16/14.59).

Checking how each document reports these numbers: the abstract and introduction both cite the segment-level figures but use ambiguous language like "difference" and "phase difference" without clarifying whether they're comparing individual pairs or aggregated segments. The results tables explicitly use segment-level calculations, so I need to verify the abstract and introduction are consistent with this choice and add clarification where the terminology could be misinterpreted. The per-problem paired Cohen's d values should be 0.61 to 1.13, but the conclusion cites 0.44 to 0.80, which is incorrect. For the discussion section, those Qwen severity differences appear to be segment-level numbers at higher precision—0.039 rounds to 0.04, and 0.235 could be the full-precision value rounding to 0.23 at two decimal places, so I need to verify whether these are intentionally at three decimal places or if there's a rounding inconsistency.

DeepSeek's segment-level numbers (0.39/1.48/7.16/14.59) check out across the tables, but I should verify the paper doesn't accidentally swap paired and segment-level values anywhere—so far the aggregate and main results tables both use segment-level consistently.

The framing document uses paired numbers (0.32→9.94) and correctly labels them as such, which is fine since that's separate from the paper itself. Let me make sure there's no confusion between the two datasets in the actual manuscript.

Looking at the narrative sections—abstract, introduction, conclusion, and discussion—they all consistently cite segment-level Cohen's d values (0.39→14.59), while the paired analysis numbers (0.32/1.15/3.97/9.94) appear only in the table. That's a reasonable split.

But I'm noticing something troubling: the abstract and conclusion both claim Cohen's d ranges from 0.44 to 0.80, yet those exact values don't match anything in my data. The paired analysis gives 0.61→1.13, and the segment-level gives 0.39→14.59. Where are 0.44 and 0.80 coming from? This is a serious discrepancy I need to track down. let me check if there's another way these could be computed. Could 0.44 and 0.80 be segment-level (non-paired) Cohen's d? Or from the old fp16 data? These are mysterious numbers.

Actually I realize — checking the abstract more carefully:

Line 7: "with Cohen's $d$ growing from $0.44$ (small) to $0.80$ (large)"

These look like they could be from a different computation. The results.tex table has per-problem paired d = 0.61 (medium) to 1.13 (large). The 0.44/0.80 values don't match any data in the paper.

Let me also check if abstract/conclusion d values match some "unpaired" or "segment-level" d computation... I don't see evidence of that.

**CRITICAL**: abstract.tex and conclusion.tex both cite d=0.44→0.80 for DeepSeek, but everywhere else — results tables, other sections — the effect sizes are d=0.61→1.13. Now I'm going through the claim consistency checks. Strategy-dependent, phase-modulated, and crossover effects all check out across the paper. The discrimination collapse claim is only partially confirmed so far. Now I'm verifying the cross-model replication claims throughout the paper—checking that we consistently use "cross-model" rather than "cross-architecture" and that we're careful about claiming aggregate trends rather than per-problem replication. The terminology checks out across abstract, introduction, results, discussion, and conclusion sections. — this is in future work context, OK ✓

Let me search for "cross-architecture" usage...
- methodology.tex: not present
- results.tex line 103: "cross-model replication" ✓
- conclusion.tex: only in future work context ✓

Wait, I should double-check the introduction more carefully. Line 28 mentions replicating findings across two models with different training approaches within the Qwen2 architecture family — that's the right framing ✓

For sub-exponential growth, I'm seeing consistent confirmation across the paper: the severity differences show ratios of 3.8×, 4.8×, and 2.0× between sparsity levels, and the conclusion describes this as a decelerating rate ✓

On random masking, the paper consistently refers to "7/8 conditions" or "7/8 FAIL" rather than using "no phase gradient" as an absolute descriptor ✓

Now checking citations — I'm scanning through the files for any placeholder patterns or incomplete references. The citations I'm finding all appear to be properly formatted with standard keys like kwon2023vllm, voita2019heads, and various conference-specific identifiers for recent work ✓ I'm checking the citation formatting and don't see any placeholder references that need fixing. Now I'm verifying the consistency between labels and references across the document—I've got a comprehensive list of section labels from introduction through conclusion, plus equation labels for the key mathematical definitions, and I'm confirming they're all properly cross-referenced.

I'm spotting a critical issue: the equation labels `eq:ii` and `eq:gradient` are defined in multiple files, which will cause LaTeX to throw warnings and potentially point references to the wrong equations. I need to consolidate these duplicates by keeping one definition and removing the other, then verifying that all `\ref` calls point to the correct location.

There's also a reference problem in the introduction—it's calling `\ref{sec:experiments}` but that label doesn't exist anywhere; the actual section is labeled `sec:results` in the results file. I should track down all these broken cross-references and fix them systematically. I see that line 33 in the introduction actually lists three sections in sequence: the experimental setup, then "sec:experiments" which presents the results, and then analysis. So "sec:experiments" is being used as a label for what should be the results section, but results.tex actually defines it as "sec:results" instead. This is a broken cross-reference that needs fixing. Let me also verify the other references in the document — background.tex has a valid internal reference to sec:phase-segmentation, though I can't verify the appendix reference without seeing those files, and analysis.tex references a table that I should check.

Now I'm going through the remaining files to verify their references are correct, and I'm also noticing several stale files with hash suffixes or old data markers like results_5_1.tex with PENDING-BF16 flags and the background, related work, and methodology files that have hash suffixes in their names, suggesting they're outdated versions that should probably be removed.

I'm also catching a discrepancy in the abstract — it claims Cohen's d values range from 0.44 to 0.80, but when I look at the actual results table for DeepSeek, the values are 0.61, 0.73, 0.95, and 1.13, which don't match at all. I'm wondering if these numbers came from an earlier fp16 version or a different metric entirely.

Beyond the mismatch, there's another issue with how the abstract labels these effect sizes — it calls 0.44 "small" and 0.80 "large," but by standard Cohen's d conventions, 0.44 falls between small (0.2) and medium (0.5), and 0.80 is right at the boundary of large. The labeling seems off.

Looking at results.tex, the actual reported values are d=0.61 (correctly labeled "medium") and d=1.13 (correctly labeled "large"), which follow the conventions properly. But the abstract and conclusion both cite 0.44 to 0.80 with the same incorrect labels, suggesting these older fp16 values weren't updated when the results changed.

I need to trace back whether the abstract's Cohen's d values are specifically about DeepSeek or if they're describing a different metric altogether — let me check what the abstract actually says about the Interaction Index.

The abstract describes the Interaction Index increasing from 0.39 to 14.59 across sparsity levels with Cohen's d growing from 0.44 to 0.80, all in the context of DeepSeek. These should match the results.tex values of 0.61 to 1.13, so the abstract is definitely citing stale numbers.

Now checking whether the paper makes unsupported universal claims: "entropy-discrimination collapse" is presented as an explanatory mechanism without claiming universality across architectures, and the conclusion properly qualifies that it only partially replicates on Qwen. I should verify whether "cross-architecture" gets used inappropriately anywhere else.

Looking at the duplicate label issue in methodology.tex—the background.tex comment explicitly states that eq:ii and eq:gradient should be referenced via \eqref rather than redefined, but methodology.tex redefines them anyway, creating duplicate labels. I'm also checking the section numbering in the introduction's outline to make sure the cross-references are consistent. I'm now checking all the section references throughout results.tex to make sure they're properly defined. Going through the file systematically, I can see references to strategy-severity, phase-amplification, crossover, cross-model, and stat-validation sections, along with dataset, sparsity-config, and phase-seg references — all of which appear to be correctly defined in the document. Now I'm verifying the confidence interval values from the results table against what's cited in the discussion section—checking that the rounded values match across both documents. I'm noticing the discussion references the Cohen's d confidence interval [8.39, 16.65] for s030, but that's from a different table than the permutation test CIs—the permutation table shows [6.70, 16.29] for the same condition. The text seems to be mixing results from these two different statistical approaches without clearly distinguishing which table each CI comes from. I'm noticing a discrepancy in the citation—the text references Table permutation but the actual CI values ($0.20$ to $8.39$) appear to come from Table cohens-d instead. The permutation table shows different bounds ($0.19$ to $6.70$), so I need to figure out which table the paragraph is actually drawing from and whether the numbers are being cited correctly. The segment-level mean and median differences check out — 22.94 divided by 14.59 gives roughly 1.6, which matches what results.tex reports. Now I'm looking at the conclusion to verify the effect size range from 0.44 to 0.80.

Wait, that's for the DeepSeek phase modulation result, but those effect sizes seem off — they should be closer to 0.61 to 1.13 based on the data. I'm also noticing the abstract mentions Cohen's d ≥ 0.55 for Qwen, so there's a discrepancy in how these values are being reported across sections.

Looking at the actual numbers, the introduction correctly cites d ≥ 0.72 for Qwen at s ≥ 0.20, which matches what I see in the tables. The abstract's 0.55 appears to be an outdated value that didn't get updated when the data was finalized. And for the random condition claims, I'm verifying: DeepSeek fails all 4 sparsity levels, while Qwen passes at s030 but fails the other three, giving us 7 failures out of 8 total conditions.

Now I'm checking the abstract's specific numbers about the crossover at s=0.25, where importance-based eviction shows dramatically different performance between high and low sparsity phases. Let me verify these values against the results table. I'm noticing a reference to s=0.35 data in the discussion that doesn't appear in the experimental results, which only cover s∈{0.15, 0.20, 0.25, 0.30}. This is likely from supplementary experiments, so I'll flag it as informational rather than critical. Now let me organize the findings by severity, starting with the Cohen's d discrepancy in the abstract and conclusion where the values are stated as 0.44→0.80 but should actually be 0.61→1.13 based on the results.

Moving through the critical issues, I'm also seeing that Qwen's Cohen's d is reported as d≥0.55 when it should be d≥0.72, and there are several undefined cross-references where \ref{sec:experiments} should point to \ref{sec:results} instead. There's also a mismatch in the discussion where the text references permutation confidence intervals but the cited values come from the bootstrap table instead.

Beyond the critical errors, I'm finding duplicate equation labels that will cause LaTeX to use only the last definition, potentially breaking cross-references throughout the document.

Now I'm checking the remaining inconsistencies: there's a rounding discrepancy where Qwen's Δ is written as 0.235 in one place but 0.23 in the cross-model table, and the Cohen's d interpretation in the abstract calls d=0.44 "small" when it's actually small-to-medium by convention. I'm also noticing a reference to s=0.35 data in the discussion that doesn't appear anywhere in the results, and there are some stale files that should be removed or archived.

Looking at the conclusion more carefully, I'm finding another d value mismatch — the text claims paired effect sizes of d=0.44 to d=0.80, but the actual values from the results table show DeepSeek at 0.61, 0.73, and 0.95, which don't match what's being cited.

I've tried several interpretations — averaging across models, checking different problem sets — but nothing produces those 0.44 and 0.80 figures. These appear to be outdated values from an earlier version of the analysis that didn't get updated when the results changed.

Looking at what's actually correct in the paper: the introduction properly cites d=0.61→1.13 for the paired DeepSeek results, the results table matches this, and the discussion is consistent. But the abstract still has the stale 0.44/0.80 values that need to be corrected to align with the paired effect sizes.

For Qwen, the introduction correctly reports d≥0.72, while the abstract and conclusion use the less precise d≥0.55 threshold. Now I'm checking the conclusion's C5 claim about whether d≥0.55 is actually the right bound for Qwen at s≥0.20, since that's where the discrepancy lies. Looking at the segment-level ratios across different sparsity levels, they range from about 1/10 at the lowest to 1/5 at the highest, so the "~1/5" claim in the conclusion and discussion is somewhat misleading since the lower sparsity segments are closer to 1/10. I should flag this inconsistency in results.tex line 131.

The abstract doesn't explicitly mention the ratio, which is good, and I've confirmed the permutation test sample size of n=49 in the table caption. Let me now compile the full report with these findings. The paired median differences across both models match what's in paper_framing.md when rounded to two decimal places, so everything checks out. Now I'm ready to write the report.

Actually, let me verify the permutation CI bounds mentioned in results.tex and discussion.tex against the table values—the lower bounds of 0.19, 0.69, 1.66, and 6.70 all align with what's in the table, so those are consistent too. I'm realizing this is actually a critical error—the text explicitly references the permutation table but cites Cohen's d values from a different table entirely, which a reviewer would definitely catch. Let me compile the full list of issues I've found: there are five critical problems across the abstract, conclusion, and introduction files where Cohen's d ranges and thresholds are consistently misreported. I'm also noticing some stale backup files that need to be cleaned up, and there's an inconsistency in how the DeepSeek comparison is described—the conclusion overstates it as roughly one-fifth when the actual range spans from one-tenth to one-fifth, which the results section correctly captures. There's also an unverifiable appendix reference in the background section that I should flag. Now I'm ready to compile the final report.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "ae5de8eb-c0a4-41bb-b09e-0190f6eaa7a4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WgXLYxCsbmDP9tmjUmWm3f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3979,
      "cache_read_input_tokens": 50988,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3979
      },
      "output_tokens": 11,
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

_source line 54_

All files read. Now performing the systematic audit across all dimensions. Let me compile findings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "28bb3ac5-e26e-4185-baab-b728800b41d0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WgXLYxCsbmDP9tmjUmWm3f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3979,
      "cache_read_input_tokens": 50988,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3979
      },
      "output_tokens": 11,
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

_source line 55_

<details open><summary>🔧 Tool call — Grep · `toolu_01LJ6dPzU81oK38Swe2Dhksy`</summary>

```json
{
  "pattern": "\\\\ref\\{sec:experiments\\}",
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
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "d597570b-7261-46be-9cc5-4577b3d722a1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WgXLYxCsbmDP9tmjUmWm3f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3979,
      "cache_read_input_tokens": 50988,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3979
      },
      "output_tokens": 11,
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

_source line 56 · 2026-05-14T09:50:46.846Z_

<details><summary>↩ Tool result · `toolu_01LJ6dPzU81oK38Swe2Dhksy`</summary>

```text
artifacts/_project/paper/introduction.tex:27:    \item We identify a \textbf{phase--strategy interaction} in compound sparsity: importance-based eviction exhibits a severity gradient across reasoning phases that is absent under random eviction (\S\ref{sec:experiments}).
artifacts/_project/paper/introduction.tex:28:    \item We show that this severity gradient \textbf{increases monotonically with sparsity} and replicate the finding at moderate-to-high sparsity ($s \geq 0.20$) across two models with different training regimes (distillation vs.\ instruction tuning), establishing robustness within the Qwen2 architecture family (\S\ref{sec:experiments}).
artifacts/_project/paper/introduction.tex:33:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "7a772417-dbb0-48e5-883c-d07ce1890d24",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "artifacts/_project/paper/introduction.tex:27:    \\item We identify a \\textbf{phase--strategy interaction} in compound sparsity: importance-based eviction exhibits a severity gradient across reasoning phases that is absent under random eviction (\\S\\ref{sec:experiments}).\nartifacts/_project/paper/introduction.tex:28:    \\item We show that this severity gradient \\textbf{increases monotonically with sparsity} and replicate the finding at moderate-to-high sparsity ($s \\geq 0.20$) across two models with different training regimes (distillation vs.\\ instruction tuning), establishing robustness within the Qwen2 architecture family (\\S\\ref{sec:experiments}).\nartifacts/_project/paper/introduction.tex:33:[Omitted long matching line]",
    "numLines": 3
  }
}
```

</details>

---

### Tool call

_source line 57_

<details open><summary>🔧 Tool call — Grep · `toolu_015bsZcKi7ZbHP3XUhJtoQyj`</summary>

```json
{
  "pattern": "0\\.44|0\\.80",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "bf42eb64-965a-447a-a1dd-08b16ae5d6c2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WgXLYxCsbmDP9tmjUmWm3f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3979,
      "cache_read_input_tokens": 50988,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3979
      },
      "output_tokens": 11,
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

_source line 58 · 2026-05-14T09:50:48.272Z_

<details><summary>↩ Tool result · `toolu_015bsZcKi7ZbHP3XUhJtoQyj`</summary>

```text
artifacts/_project/paper/conclusion.tex:10:    \item \textbf{Phase modulation (C2).} Under importance-based eviction, the median Interaction Index difference between low- and high-sparsity phases increases monotonically with sparsity (Bonferroni-corrected $p < 0.005$ at all four levels), with paired effect sizes growing from $d{=}0.44$ (small) to $d{=}0.80$ (large).
artifacts/_project/paper/abstract.tex:7:Under importance-based KV cache eviction, the median Interaction Index difference between low-sparsity and high-sparsity reasoning phases increases monotonically from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with Cohen's $d$ growing from $0.44$ (small) to $0.80$ (large); Bonferroni-corrected permutation tests yield $p < 0.005$ at all four sparsity levels.
artifacts/_project/paper/introduction.tex:14:This \emph{severity gradient} grows monotonically with the sparsity budget: on DeepSeek-R1-Distill-Qwen-7B, the median phase difference in Interaction Index rises from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired effect sizes increasing from $d{=}0.44$ (small) to $d{=}0.80$ (large); Bonferroni-corrected permutation tests confirm significance at all four sparsity levels on this model ($p < 0.005$).
artifacts/_project/paper/results.tex:124:[Omitted long matching line]
artifacts/_project/paper/results.tex:186:0.15 & 0.44 (small) & 0.32\; $[0.20,\; 0.47]$ & 0.28 (small) & 0.05\; $[-0.01,\; 0.11]$\textsuperscript{ns} \\ % exp_id: bf16_ds_imp_s015, bf16_qw_imp_s015; per-problem paired B=10000; d_z from cohens_d_bf16.json
artifacts/_project/paper/results.tex:189:0.30 & 0.80 (large) & 9.94\; $[8.39,\; 16.65]$ & 1.02 (large) & 2.62\; $[1.72,\; 3.65]$ \\ % exp_id: bf16_ds_imp_s030, bf16_qw_imp_s030; per-problem paired B=10000; d_z from cohens_d_bf16.json
artifacts/_project/paper/results.tex:195:For DeepSeek, the effect size increases monotonically from small ($d{=}0.44$) at $s{=}0.15$ to large ($d{=}0.80$) at $s{=}0.30$, with all bootstrap CIs for $\widetilde{\Delta}$ excluding zero (Table~\ref{tab:cohens-d}). % exp_id: bf16_ds_imp_s015..s030; per-problem paired B=10000
artifacts/_project/paper/results.tex:197:At higher sparsity levels ($s \geq 0.25$), Qwen exhibits larger standardized effect sizes than DeepSeek ($d{=}0.89$/$1.02$ vs.\ $0.68$/$0.80$), consistent with lower between-problem variance in Qwen's II distribution yielding larger standardized differences despite smaller absolute II values. % exp_id: bf16_ds_imp_s025..s030, bf16_qw_imp_s025..s030; per-problem paired B=10000
artifacts/_project/paper/discussion.tex:29:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "f51d8c7d-99e6-4d75-92d2-d52b8ceb265b",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "artifacts/_project/paper/conclusion.tex:10:    \\item \\textbf{Phase modulation (C2).} Under importance-based eviction, the median Interaction Index difference between low- and high-sparsity phases increases monotonically with sparsity (Bonferroni-corrected $p < 0.005$ at all four levels), with paired effect sizes growing from $d{=}0.44$ (small) to $d{=}0.80$ (large).\nartifacts/_project/paper/abstract.tex:7:Under importance-based KV cache eviction, the median Interaction Index difference between low-sparsity and high-sparsity reasoning phases increases monotonically from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with Cohen's $d$ growing from $0.44$ (small) to $0.80$ (large); Bonferroni-corrected permutation tests yield $p < 0.005$ at all four sparsity levels.\nartifacts/_project/paper/introduction.tex:14:This \\emph{severity gradient} grows monotonically with the sparsity budget: on DeepSeek-R1-Distill-Qwen-7B, the median phase difference in Interaction Index rises from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired effect sizes increasing from $d{=}0.44$ (small) to $d{=}0.80$ (large); Bonferroni-corrected permutation tests confirm significance at all four sparsity levels on this model ($p < 0.005$).\nartifacts/_project/paper/results.tex:124:[Omitted long matching line]\nartifacts/_project/paper/results.tex:186:0.15 & 0.44 (small) & 0.32\\; $[0.20,\\; 0.47]$ & 0.28 (small) & 0.05\\; $[-0.01,\\; 0.11]$\\textsuperscript{ns} \\\\ % exp_id: bf16_ds_imp_s015, bf16_qw_imp_s015; per-problem paired B=10000; d_z from cohens_d_bf16.json\nartifacts/_project/paper/results.tex:189:0.30 & 0.80 (large) & 9.94\\; $[8.39,\\; 16.65]$ & 1.02 (large) & 2.62\\; $[1.72,\\; 3.65]$ \\\\ % exp_id: bf16_ds_imp_s030, bf16_qw_imp_s030; per-problem paired B=10000; d_z from cohens_d_bf16.json\nartifacts/_project/paper/results.tex:195:For DeepSeek, the effect size increases monotonically from small ($d{=}0.44$) at $s{=}0.15$ to large ($d{=}0.80$) at $s{=}0.30$, with all bootstrap CIs for $\\widetilde{\\Delta}$ excluding zero (Table~\\ref{tab:cohens-d}). % exp_id: bf16_ds_imp_s015..s030; per-problem paired B=10000\nartifacts/_project/paper/results.tex:197:At higher sparsity levels ($s \\geq 0.25$), Qwen exhibits larger standardized effect sizes than DeepSeek ($d{=}0.89$/$1.02$ vs.\\ $0.68$/$0.80$), consistent with lower between-problem variance in Qwen's II distribution yielding larger standardized differences despite smaller absolute II values. % exp_id: bf16_ds_imp_s025..s030, bf16_qw_imp_s025..s030; per-problem paired B=10000\nartifacts/_project/paper/discussion.tex:29:[Omitted long matching line]",
    "numLines": 9
  }
}
```

</details>

---

### Tool call

_source line 59_

<details open><summary>🔧 Tool call — Grep · `toolu_017ztqfeqhCHbTuz217PRQ71`</summary>

```json
{
  "pattern": "0\\.55",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "72b310ba-1f08-4ab9-8b86-4e7dff9f52b3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WgXLYxCsbmDP9tmjUmWm3f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3979,
      "cache_read_input_tokens": 50988,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3979
      },
      "output_tokens": 11,
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

_source line 60 · 2026-05-14T09:50:48.788Z_

<details><summary>↩ Tool result · `toolu_017ztqfeqhCHbTuz217PRQ71`</summary>

```text
artifacts/_project/paper/conclusion.tex:16:    \item \textbf{Cross-model replication (C5).} The monotonic gradient replicates on Qwen2.5-7B-Instruct at $s \geq 0.20$ ($d \geq 0.55$; Spearman $\rho = 1.0$ across sparsity levels; gradient permutation $p = 0.043$), with attenuated absolute magnitude (${\sim}1/5$ of DeepSeek).
artifacts/_project/paper/abstract.tex:10:The pattern replicates on Qwen2.5-7B-Instruct at $s \geq 0.20$ (Cohen's $d \geq 0.55$; Spearman $\rho = 1.0$ across sparsity levels; gradient permutation $p = 0.043$).
artifacts/_project/paper/introduction.tex:15:The pattern replicates at $s \geq 0.20$ on Qwen2.5-7B-Instruct ($d \geq 0.55$) with attenuated absolute magnitude, though the effect at $s{=}0.15$ is marginal ($d{=}0.28$, bootstrap CI includes zero).
artifacts/_project/paper/results.tex:124:[Omitted long matching line]
artifacts/_project/paper/results.tex:187:0.20 & 0.52 (medium) & 1.15\; $[0.66,\; 1.26]$ & 0.55 (medium) & 0.21\; $[0.07,\; 0.40]$ \\ % exp_id: bf16_ds_imp_s020, bf16_qw_imp_s020; per-problem paired B=10000; d_z from cohens_d_bf16.json
artifacts/_project/paper/results.tex:196:For Qwen, the compound interaction effect is marginal at $s{=}0.15$ ($d{=}0.28$, bootstrap CI includes zero), becoming reliable at $s \geq 0.20$ ($d \geq 0.55$), suggesting a model-dependent onset threshold for detectable phase modulation. % exp_id: bf16_qw_imp_s015..s030; per-problem paired B=10000
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "6866340e-a644-4488-832a-4d460c7601a6",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "artifacts/_project/paper/conclusion.tex:16:    \\item \\textbf{Cross-model replication (C5).} The monotonic gradient replicates on Qwen2.5-7B-Instruct at $s \\geq 0.20$ ($d \\geq 0.55$; Spearman $\\rho = 1.0$ across sparsity levels; gradient permutation $p = 0.043$), with attenuated absolute magnitude (${\\sim}1/5$ of DeepSeek).\nartifacts/_project/paper/abstract.tex:10:The pattern replicates on Qwen2.5-7B-Instruct at $s \\geq 0.20$ (Cohen's $d \\geq 0.55$; Spearman $\\rho = 1.0$ across sparsity levels; gradient permutation $p = 0.043$).\nartifacts/_project/paper/introduction.tex:15:The pattern replicates at $s \\geq 0.20$ on Qwen2.5-7B-Instruct ($d \\geq 0.55$) with attenuated absolute magnitude, though the effect at $s{=}0.15$ is marginal ($d{=}0.28$, bootstrap CI includes zero).\nartifacts/_project/paper/results.tex:124:[Omitted long matching line]\nartifacts/_project/paper/results.tex:187:0.20 & 0.52 (medium) & 1.15\\; $[0.66,\\; 1.26]$ & 0.55 (medium) & 0.21\\; $[0.07,\\; 0.40]$ \\\\ % exp_id: bf16_ds_imp_s020, bf16_qw_imp_s020; per-problem paired B=10000; d_z from cohens_d_bf16.json\nartifacts/_project/paper/results.tex:196:For Qwen, the compound interaction effect is marginal at $s{=}0.15$ ($d{=}0.28$, bootstrap CI includes zero), becoming reliable at $s \\geq 0.20$ ($d \\geq 0.55$), suggesting a model-dependent onset threshold for detectable phase modulation. % exp_id: bf16_qw_imp_s015..s030; per-problem paired B=10000",
    "numLines": 6
  }
}
```

</details>

---

### Assistant

_source line 61_

<details><summary>Logged reasoning block</summary>

````text
Interesting! So my earlier reading of results.tex was incomplete — let me re-read the actual table data more carefully. It seems the actual Table cohens-d data in results.tex is DIFFERENT from what I initially read. Let me re-read lines 182-198 of results.tex more carefully.

Wait, let me re-read. The results I first read showed:
```
0.15 & 0.61 (medium) & 0.32\; $[0.20,\; 0.47]$ & 0.37 (small) & 0.05\; $[-0.01,\; 0.11]$\textsuperscript{ns}


```

But now looking at the actual table rows, I'm seeing the effect sizes increase substantially as the threshold goes up — at 0.20 the Cohen's d jumps to 0.73 (medium), at 0.25 it reaches 0.95 (large), and by 0.30 it's at 1.13 (large), with the confidence intervals widening dramatically as the effect sizes grow.

Wait, that's strange — the grep output shows different values than what I just read. Let me check the file again to see what's actually there.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "64fa9058-3f47-4dd5-9077-cae3489ce5c2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Nn97AAqfGCYPhNyDBih3T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18471,
      "cache_read_input_tokens": 54967,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18471
      },
      "output_tokens": 20,
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

_source line 62_

The grep reveals the actual Table cohens-d data is different from what I initially noted. Let me re-read that section precisely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "aa4e6ddf-331e-4880-8732-9c16741a09fb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Nn97AAqfGCYPhNyDBih3T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18471,
      "cache_read_input_tokens": 54967,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18471
      },
      "output_tokens": 20,
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

_source line 63_

<details open><summary>🔧 Tool call — Read · `toolu_012wYhVQ3HhcsBdQj4Vyo5MA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex",
  "offset": 174,
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
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "f14e9755-9eb1-4c99-93d7-c9d128615d48",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Nn97AAqfGCYPhNyDBih3T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18471,
      "cache_read_input_tokens": 54967,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18471
      },
      "output_tokens": 20,
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

_source line 64 · 2026-05-14T09:51:02.993Z_

<details><summary>↩ Tool result · `toolu_012wYhVQ3HhcsBdQj4Vyo5MA`</summary>

```text
174	\paragraph{Effect sizes.}
175	Table~\ref{tab:cohens-d} reports Cohen's $d$ (bootstrap $B{=}10{,}000$) measuring the standardized difference in II between low- and high-sparsity phases under importance-based eviction.
176	
177	\begin{table}[t]
178	\centering
179	\small
180	\caption{Cohen's $d$ and per-problem median difference $\widetilde{\Delta}$ for the phase-dependent II (low $-$ high) under importance-based eviction. Bootstrap 95\% CIs for $\widetilde{\Delta}$ ($B{=}10{,}000$, per-problem paired). DeepSeek: $n{=}49$ problems (1 excluded); Qwen: $n{=}46$ problems (4 excluded).}
181	\label{tab:cohens-d}
182	\begin{tabular}{@{}lcccc@{}}
183	\toprule
184	$s$ & DeepSeek $d$ & $\widetilde{\Delta}$ [95\% CI] & Qwen $d$ & $\widetilde{\Delta}$ [95\% CI] \\
185	\midrule
186	0.15 & 0.44 (small) & 0.32\; $[0.20,\; 0.47]$ & 0.28 (small) & 0.05\; $[-0.01,\; 0.11]$\textsuperscript{ns} \\ % exp_id: bf16_ds_imp_s015, bf16_qw_imp_s015; per-problem paired B=10000; d_z from cohens_d_bf16.json
187	0.20 & 0.52 (medium) & 1.15\; $[0.66,\; 1.26]$ & 0.55 (medium) & 0.21\; $[0.07,\; 0.40]$ \\ % exp_id: bf16_ds_imp_s020, bf16_qw_imp_s020; per-problem paired B=10000; d_z from cohens_d_bf16.json
188	0.25 & 0.68 (medium) & 3.97\; $[2.83,\; 5.29]$ & 0.89 (large) & 1.11\; $[0.61,\; 1.47]$ \\ % exp_id: bf16_ds_imp_s025, bf16_qw_imp_s025; per-problem paired B=10000; d_z from cohens_d_bf16.json
189	0.30 & 0.80 (large) & 9.94\; $[8.39,\; 16.65]$ & 1.02 (large) & 2.62\; $[1.72,\; 3.65]$ \\ % exp_id: bf16_ds_imp_s030, bf16_qw_imp_s030; per-problem paired B=10000; d_z from cohens_d_bf16.json
190	\bottomrule
191	\multicolumn{5}{@{}l}{\footnotesize \textsuperscript{ns}CI spans zero; marginal at $s{=}0.15$ (bootstrap CI includes zero), becoming reliable at $s \geq 0.20$.}
192	\end{tabular}
193	\end{table}
194	
195	For DeepSeek, the effect size increases monotonically from small ($d{=}0.44$) at $s{=}0.15$ to large ($d{=}0.80$) at $s{=}0.30$, with all bootstrap CIs for $\widetilde{\Delta}$ excluding zero (Table~\ref{tab:cohens-d}). % exp_id: bf16_ds_imp_s015..s030; per-problem paired B=10000
196	For Qwen, the compound interaction effect is marginal at $s{=}0.15$ ($d{=}0.28$, bootstrap CI includes zero), becoming reliable at $s \geq 0.20$ ($d \geq 0.55$), suggesting a model-dependent onset threshold for detectable phase modulation. % exp_id: bf16_qw_imp_s015..s030; per-problem paired B=10000
197	At higher sparsity levels ($s \geq 0.25$), Qwen exhibits larger standardized effect sizes than DeepSeek ($d{=}0.89$/$1.02$ vs.\ $0.68$/$0.80$), consistent with lower between-problem variance in Qwen's II distribution yielding larger standardized differences despite smaller absolute II values. % exp_id: bf16_ds_imp_s025..s030, bf16_qw_imp_s025..s030; per-problem paired B=10000
198	Full per-problem distributions and permutation null distributions appear in Appendix~\ref{app:bootstrap-details}.
199	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "059a6153-c9a6-4408-b9f3-477057fb3442",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex",
      "content": "\\paragraph{Effect sizes.}\nTable~\\ref{tab:cohens-d} reports Cohen's $d$ (bootstrap $B{=}10{,}000$) measuring the standardized difference in II between low- and high-sparsity phases under importance-based eviction.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cohen's $d$ and per-problem median difference $\\widetilde{\\Delta}$ for the phase-dependent II (low $-$ high) under importance-based eviction. Bootstrap 95\\% CIs for $\\widetilde{\\Delta}$ ($B{=}10{,}000$, per-problem paired). DeepSeek: $n{=}49$ problems (1 excluded); Qwen: $n{=}46$ problems (4 excluded).}\n\\label{tab:cohens-d}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n$s$ & DeepSeek $d$ & $\\widetilde{\\Delta}$ [95\\% CI] & Qwen $d$ & $\\widetilde{\\Delta}$ [95\\% CI] \\\\\n\\midrule\n0.15 & 0.44 (small) & 0.32\\; $[0.20,\\; 0.47]$ & 0.28 (small) & 0.05\\; $[-0.01,\\; 0.11]$\\textsuperscript{ns} \\\\ % exp_id: bf16_ds_imp_s015, bf16_qw_imp_s015; per-problem paired B=10000; d_z from cohens_d_bf16.json\n0.20 & 0.52 (medium) & 1.15\\; $[0.66,\\; 1.26]$ & 0.55 (medium) & 0.21\\; $[0.07,\\; 0.40]$ \\\\ % exp_id: bf16_ds_imp_s020, bf16_qw_imp_s020; per-problem paired B=10000; d_z from cohens_d_bf16.json\n0.25 & 0.68 (medium) & 3.97\\; $[2.83,\\; 5.29]$ & 0.89 (large) & 1.11\\; $[0.61,\\; 1.47]$ \\\\ % exp_id: bf16_ds_imp_s025, bf16_qw_imp_s025; per-problem paired B=10000; d_z from cohens_d_bf16.json\n0.30 & 0.80 (large) & 9.94\\; $[8.39,\\; 16.65]$ & 1.02 (large) & 2.62\\; $[1.72,\\; 3.65]$ \\\\ % exp_id: bf16_ds_imp_s030, bf16_qw_imp_s030; per-problem paired B=10000; d_z from cohens_d_bf16.json\n\\bottomrule\n\\multicolumn{5}{@{}l}{\\footnotesize \\textsuperscript{ns}CI spans zero; marginal at $s{=}0.15$ (bootstrap CI includes zero), becoming reliable at $s \\geq 0.20$.}\n\\end{tabular}\n\\end{table}\n\nFor DeepSeek, the effect size increases monotonically from small ($d{=}0.44$) at $s{=}0.15$ to large ($d{=}0.80$) at $s{=}0.30$, with all bootstrap CIs for $\\widetilde{\\Delta}$ excluding zero (Table~\\ref{tab:cohens-d}). % exp_id: bf16_ds_imp_s015..s030; per-problem paired B=10000\nFor Qwen, the compound interaction effect is marginal at $s{=}0.15$ ($d{=}0.28$, bootstrap CI includes zero), becoming reliable at $s \\geq 0.20$ ($d \\geq 0.55$), suggesting a model-dependent onset threshold for detectable phase modulation. % exp_id: bf16_qw_imp_s015..s030; per-problem paired B=10000\nAt higher sparsity levels ($s \\geq 0.25$), Qwen exhibits larger standardized effect sizes than DeepSeek ($d{=}0.89$/$1.02$ vs.\\ $0.68$/$0.80$), consistent with lower between-problem variance in Qwen's II distribution yielding larger standardized differences despite smaller absolute II values. % exp_id: bf16_ds_imp_s025..s030, bf16_qw_imp_s025..s030; per-problem paired B=10000\nFull per-problem distributions and permutation null distributions appear in Appendix~\\ref{app:bootstrap-details}.\n",
      "numLines": 26,
      "startLine": 174,
      "totalLines": 199
    }
  }
}
```

</details>

---

### Tool call

_source line 65_

<details open><summary>🔧 Tool call — Read · `toolu_01YXJGTFEBBfSWtzhkasntJp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex",
  "offset": 25,
  "limit": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "b7a559fb-a509-4e31-a147-26fde194fdec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Nn97AAqfGCYPhNyDBih3T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18471,
      "cache_read_input_tokens": 54967,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18471
      },
      "output_tokens": 20,
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

_source line 66_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed_warning",
    "resetsAt": 1779267600,
    "rateLimitType": "seven_day",
    "utilization": 0.4,
    "isUsingOverage": false
  },
  "uuid": "ad57d494-51fa-4de0-8a30-d043cb1fb76c",
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86"
}
```

---

### Tool result

_source line 67 · 2026-05-14T09:51:03.837Z_

<details><summary>↩ Tool result · `toolu_01YXJGTFEBBfSWtzhkasntJp`</summary>

```text
25	The phase-strategy interaction replicates across both models with perfect ordinal agreement: the Spearman rank correlation of Cohen's $d$ effect sizes across sparsity levels is $\rho{=}1.0$, and a gradient permutation test confirms this monotonic co-escalation ($p{=}0.043$). % exp_id: cross_model_correlation; Spearman rho=1.0, gradient_perm p=0.043
26	All eight paired Wilcoxon tests (4 sparsity levels $\times$ 2 models) reject $H_0$, confirming the pattern is not an artifact of a single model's weight structure.
27	
28	The \emph{magnitude} of the effect, however, differs substantially.
29	Qwen's median severity differences ($0.039 \to 0.235 \to 1.268 \to 2.943$) are approximately one-fifth of DeepSeek's ($0.39 \to 1.48 \to 7.16 \to 14.59$), and the onset threshold differs: DeepSeek's gradient is significant from $s{=}0.15$ (Cohen's $d{=}0.442$), while Qwen's becomes clearly significant only at $s \geq 0.20$ ($d{=}0.549$; $s{=}0.15$ is borderline at $d{=}0.281$ with CI crossing zero). % exp_id: cohens_d_bf16.json (ds: 0.442,0.520,0.683,0.803), cohens_d_bf16_qwen.json (qw: 0.281,0.549,0.889,1.022).
30	The two models share the Qwen2ForCausalLM architecture but differ in training: DeepSeek-R1-Distill-Qwen-7B is distilled from a larger reasoning model, while Qwen2.5-7B-Instruct undergoes standard instruction tuning.
31	We conjecture that distillation amplifies the phase-strategy interaction by producing sharper internal phase transitions---a hypothesis testable by comparing distilled and non-distilled variants at matched scale.
32	
33	\paragraph{Mechanistic evidence: discrimination collapse as the robust signal.}
34	The entropy-discrimination collapse hypothesis (\S\ref{sec:analysis}) receives partial cross-model support.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "f9c26262-c209-4ebd-b11b-560bc173b828",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex",
      "content": "The phase-strategy interaction replicates across both models with perfect ordinal agreement: the Spearman rank correlation of Cohen's $d$ effect sizes across sparsity levels is $\\rho{=}1.0$, and a gradient permutation test confirms this monotonic co-escalation ($p{=}0.043$). % exp_id: cross_model_correlation; Spearman rho=1.0, gradient_perm p=0.043\nAll eight paired Wilcoxon tests (4 sparsity levels $\\times$ 2 models) reject $H_0$, confirming the pattern is not an artifact of a single model's weight structure.\n\nThe \\emph{magnitude} of the effect, however, differs substantially.\nQwen's median severity differences ($0.039 \\to 0.235 \\to 1.268 \\to 2.943$) are approximately one-fifth of DeepSeek's ($0.39 \\to 1.48 \\to 7.16 \\to 14.59$), and the onset threshold differs: DeepSeek's gradient is significant from $s{=}0.15$ (Cohen's $d{=}0.442$), while Qwen's becomes clearly significant only at $s \\geq 0.20$ ($d{=}0.549$; $s{=}0.15$ is borderline at $d{=}0.281$ with CI crossing zero). % exp_id: cohens_d_bf16.json (ds: 0.442,0.520,0.683,0.803), cohens_d_bf16_qwen.json (qw: 0.281,0.549,0.889,1.022).\nThe two models share the Qwen2ForCausalLM architecture but differ in training: DeepSeek-R1-Distill-Qwen-7B is distilled from a larger reasoning model, while Qwen2.5-7B-Instruct undergoes standard instruction tuning.\nWe conjecture that distillation amplifies the phase-strategy interaction by producing sharper internal phase transitions---a hypothesis testable by comparing distilled and non-distilled variants at matched scale.\n\n\\paragraph{Mechanistic evidence: discrimination collapse as the robust signal.}\nThe entropy-discrimination collapse hypothesis (\\S\\ref{sec:analysis}) receives partial cross-model support.",
      "numLines": 10,
      "startLine": 25,
      "totalLines": 103
    }
  }
}
```

</details>

---

### Assistant

_source line 68_

<details><summary>Logged reasoning block</summary>

```text
OK so now I see the ACTUAL data in the table. The Cohen's d values in results.tex Table cohens-d are:

DeepSeek: 0.44 / 0.52 / 0.68 / 0.80 (d_z, labeled as from cohens_d_bf16.json)
Qwen: 0.28 / 0.55 / 0.89 / 1.02 (d_z)

And discussion.tex line 29 confirms with full precision: ds: 0.442, 0.520, 0.683, 0.803; qw: 0.281, 0.549, 0.889, 1.022.


The table is reporting d_z values for paired data, but the task specification lists different values (0.61/0.73/0.95/1.13), suggesting these might be computed using different methods or formulas.

I'm seeing two distinct sets of Cohen's d values across the documents: one set in the results and discussion files (0.44/0.52/0.68/0.80 for DeepSeek), and another in the paper_framing markdown and task spec (0.61/0.73/0.95/1.13). The results file references d_z from a specific JSON file, so these appear to be fundamentally different calculations rather than just rounding differences.

Now I need to figure out which numbers are actually correct for the paper — the introduction uses the smaller values (0.44 to 0.80), but the task specification lists the larger ones (0.61 to 1.13), so there's a real inconsistency I need to resolve.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "2d0cc1ed-38e6-4548-adfc-b4d96f4a7652",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019aFDb4fj5jFoWzrEpEuzeV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2867,
      "cache_read_input_tokens": 73438,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2867
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

_source line 69_

I need to re-verify introduction.tex line 14 — my initial read may have been inaccurate based on the grep results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "c36888dc-1d41-41de-b2cf-6b0ca821a66e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019aFDb4fj5jFoWzrEpEuzeV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2867,
      "cache_read_input_tokens": 73438,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2867
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

_source line 70_

<details open><summary>🔧 Tool call — Read · `toolu_017ZGUG3Z1FbHAmM5Gfo3kSc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex",
  "offset": 12,
  "limit": 6
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "d68fdfa3-60ba-4d7d-bc96-8e8e8356f15d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019aFDb4fj5jFoWzrEpEuzeV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2867,
      "cache_read_input_tokens": 73438,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2867
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

_source line 71 · 2026-05-14T09:51:27.675Z_

<details><summary>↩ Tool result · `toolu_017ZGUG3Z1FbHAmM5Gfo3kSc`</summary>

```text
12	We investigate whether compound sparsity severity is modulated by reasoning phase and eviction strategy.
13	Our central finding is that it is, and strongly so: under importance-based KV cache eviction, the Interaction Index---a measure of super-additive compound degradation---is concentrated in the low-sparsity phase (where attention distributes broadly) and largely absent in the high-sparsity phase (where attention is focused).
14	This \emph{severity gradient} grows monotonically with the sparsity budget: on DeepSeek-R1-Distill-Qwen-7B, the median phase difference in Interaction Index rises from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired effect sizes increasing from $d{=}0.44$ (small) to $d{=}0.80$ (large); Bonferroni-corrected permutation tests confirm significance at all four sparsity levels on this model ($p < 0.005$).
15	The pattern replicates at $s \geq 0.20$ on Qwen2.5-7B-Instruct ($d \geq 0.55$) with attenuated absolute magnitude, though the effect at $s{=}0.15$ is marginal ($d{=}0.28$, bootstrap CI includes zero).
16	Critically, random eviction produces no such gradient: 7/8 conditions across both models fail to exhibit a significant phase difference (the single exception---Qwen $s{=}0.30$---has negligible effect size, $d{=}{-}0.04$), confirming that the severity gradient is an emergent property of the interaction between importance scoring and phase-dependent attention structure, not an artifact of compound sparsity per se.
17	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "675cc5e4-66b7-4fe4-ad22-8f1694764a78",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex",
      "content": "We investigate whether compound sparsity severity is modulated by reasoning phase and eviction strategy.\nOur central finding is that it is, and strongly so: under importance-based KV cache eviction, the Interaction Index---a measure of super-additive compound degradation---is concentrated in the low-sparsity phase (where attention distributes broadly) and largely absent in the high-sparsity phase (where attention is focused).\nThis \\emph{severity gradient} grows monotonically with the sparsity budget: on DeepSeek-R1-Distill-Qwen-7B, the median phase difference in Interaction Index rises from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired effect sizes increasing from $d{=}0.44$ (small) to $d{=}0.80$ (large); Bonferroni-corrected permutation tests confirm significance at all four sparsity levels on this model ($p < 0.005$).\nThe pattern replicates at $s \\geq 0.20$ on Qwen2.5-7B-Instruct ($d \\geq 0.55$) with attenuated absolute magnitude, though the effect at $s{=}0.15$ is marginal ($d{=}0.28$, bootstrap CI includes zero).\nCritically, random eviction produces no such gradient: 7/8 conditions across both models fail to exhibit a significant phase difference (the single exception---Qwen $s{=}0.30$---has negligible effect size, $d{=}{-}0.04$), confirming that the severity gradient is an emergent property of the interaction between importance scoring and phase-dependent attention structure, not an artifact of compound sparsity per se.\n",
      "numLines": 6,
      "startLine": 12,
      "totalLines": 34
    }
  }
}
```

</details>

---

### Assistant

_source line 72_

<details><summary>Logged reasoning block</summary>

```text
OK! So introduction.tex line 14 actually says d=0.44→0.80, NOT d=0.61→1.13. My initial read was wrong because the Read tool output was cut off at line 34 and I thought I read the numbers as 0.61→1.13 but they're actually 0.44→0.80.

And line 15 says d≥0.55 for Qwen and d=0.28 for Qwen s015.

So the paper consistently uses d_z values:
- DeepSeek: 0.44/0.52/0.68/0.80 (in abstract, intro, results, conclusion, discussion)


- Qwen: 0.28/0.55/0.89/1.02 (in intro, results, conclusion, discussion)

But paper_framing.md reports different values: DeepSeek: 0.61→1.13; Qwen: 0.37→1.44. The task spec also matches paper_framing with "Cohen's d: 0.61 / 0.73 / 0.95 / 1.13", so there's a clear mismatch between what the paper actually contains and what's documented in the framing file.

The paper itself is internally consistent — it uses d_z throughout and the values align across abstract, intro, results, conclusion, and discussion. The real issue is that paper_framing.md appears to be using a different Cohen's d calculation method than what's in the paper. I need to verify this by checking whether the paper's values are truly consistent across all sections. I'm verifying the Qwen values match across the paper—the Cohen's d measurements of 0.28/0.55/0.89/1.02 appear consistently in the results table, text, discussion, and conclusion sections. The paper maintains internal consistency with both model comparisons, where DeepSeek shows smaller effect sizes and Qwen shows larger ones.

But there's a mismatch between what the paper reports and what's documented in paper_framing.md—the framing document lists different d values entirely (0.37→1.44 for Qwen instead of 0.28→1.02), which suggests the framing document may be referencing a different version or calculation method than the final paper.

Now I'm going through the full audit again with this corrected understanding. Looking at the actual issues I've found: there are undefined LaTeX references in introduction.tex that will render as "??" in the PDF, and in discussion.tex there's a citation mismatch where the text references CI values from the wrong table—it's pulling numbers from the Cohen's d table when it should be citing the permutation test results instead.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "6620d714-0dea-4182-b697-ccc071e9632c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SPCU9z1gTNzKf5CMmt93qb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1490,
      "cache_read_input_tokens": 76305,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1490
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

_source line 73_

<details open><summary>🔧 Tool call — Read · `toolu_01RJQC2RKeBnpWhkqDYigsQK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex",
  "offset": 82,
  "limit": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "07cd45c1-9a43-4ae4-9b0b-b9fbb4dbc35d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SPCU9z1gTNzKf5CMmt93qb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1490,
      "cache_read_input_tokens": 76305,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1490
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

_source line 74 · 2026-05-14T09:51:57.027Z_

<details><summary>↩ Tool result · `toolu_01RJQC2RKeBnpWhkqDYigsQK`</summary>

```text
82	
83	\paragraph{Statistical scope.}
84	Bootstrap confidence intervals use $B{=}10{,}000$ resamples. The paired permutation test yields $n{=}49$ paired problems for DeepSeek (1 excluded) and $n{=}46$ for Qwen (4 excluded). % exp_id: cohens_d_bf16.json, cohens_d_bf16_qwen.json
85	The severity difference distribution is right-skewed (mean/median ratio ${\sim}1.6{:}1$ at $s{=}0.30$), motivating our use of medians and nonparametric tests rather than parametric alternatives. % exp_id: bf16_importance_s030; mean_diff=22.94, median_diff=14.59 (segment-level). Per-problem paired: median_diff=9.9436 at s030
86	All four permutation tests reject $H_0$ after Bonferroni correction ($p_{\text{Bonf}} < 0.005$; Table~\ref{tab:permutation}), with CI lower bounds increasing from $0.20$ to $8.39$---confirming the effect direction at every sparsity level. The permutation CIs at higher sparsity are wider (e.g., $[8.39,\; 16.65]$ at $s{=}0.30$), reflecting genuine variance in per-problem severity amplification. % exp_id: permutation_test_results.json; updated bf16 B=10000 per-problem paired CIs: s015=[0.199,0.472], s020=[0.655,1.256], s025=[2.829,5.292], s030=[8.392,16.653]
87	
88	A notable exception among the random baselines is the Qwen random condition at $s{=}0.30$, which yields a statistically significant result ($p{=}0.012$) despite negligible effect size ($d{=}{-}0.04$, bootstrap CI excluding zero). % exp_id: qw_rand_s030; B=10000, p=0.012, d=-0.035, negligible
89	This case illustrates that dichotomous significance testing can flag effects of no practical magnitude---reinforcing the importance of reporting effect sizes and confidence intervals alongside $p$-values.
90	
91	\paragraph{Sparsity range.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "d4067e23-45e6-49a8-b503-8a936ffd0b52",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex",
      "content": "\n\\paragraph{Statistical scope.}\nBootstrap confidence intervals use $B{=}10{,}000$ resamples. The paired permutation test yields $n{=}49$ paired problems for DeepSeek (1 excluded) and $n{=}46$ for Qwen (4 excluded). % exp_id: cohens_d_bf16.json, cohens_d_bf16_qwen.json\nThe severity difference distribution is right-skewed (mean/median ratio ${\\sim}1.6{:}1$ at $s{=}0.30$), motivating our use of medians and nonparametric tests rather than parametric alternatives. % exp_id: bf16_importance_s030; mean_diff=22.94, median_diff=14.59 (segment-level). Per-problem paired: median_diff=9.9436 at s030\nAll four permutation tests reject $H_0$ after Bonferroni correction ($p_{\\text{Bonf}} < 0.005$; Table~\\ref{tab:permutation}), with CI lower bounds increasing from $0.20$ to $8.39$---confirming the effect direction at every sparsity level. The permutation CIs at higher sparsity are wider (e.g., $[8.39,\\; 16.65]$ at $s{=}0.30$), reflecting genuine variance in per-problem severity amplification. % exp_id: permutation_test_results.json; updated bf16 B=10000 per-problem paired CIs: s015=[0.199,0.472], s020=[0.655,1.256], s025=[2.829,5.292], s030=[8.392,16.653]\n\nA notable exception among the random baselines is the Qwen random condition at $s{=}0.30$, which yields a statistically significant result ($p{=}0.012$) despite negligible effect size ($d{=}{-}0.04$, bootstrap CI excluding zero). % exp_id: qw_rand_s030; B=10000, p=0.012, d=-0.035, negligible\nThis case illustrates that dichotomous significance testing can flag effects of no practical magnitude---reinforcing the importance of reporting effect sizes and confidence intervals alongside $p$-values.\n\n\\paragraph{Sparsity range.}",
      "numLines": 10,
      "startLine": 82,
      "totalLines": 103
    }
  }
}
```

</details>

---

### Assistant

_source line 75_

<details><summary>Logged reasoning block</summary>

```text
OK so discussion.tex line 86 says:
"All four permutation tests reject $H_0$ after Bonferroni correction ($p_{\text{Bonf}} < 0.005$; Table~\ref{tab:permutation}), with CI lower bounds increasing from $0.20$ to $8.39$---confirming the effect direction at every sparsity level. The permutation CIs at higher sparsity are wider (e.g., $[8.39,\; 16.65]$ at $s{=}0.30$)"
 
Wait, I need to check what CIs are actually being cited here. The comment indicates the values in the text come from per-problem paired bootstrap CIs, not the permutation test CIs. Let me verify against the actual permutation table—the ranges don't quite match up with what's stated in the text. I'm spotting a critical issue here — the text is citing Cohen's d confidence intervals but attributing them to the permutation table, which is a fundamental data attribution error. Both tables use n=49 for DeepSeek, so that checks out, but I need to verify whether the discussion about bootstrap CIs excluding zero for Qwen's random condition actually holds up, since the Cohen's d value is negative there. I can't fully verify the bootstrap CI claims without the raw data, but the framing seems reasonable. What's more concerning is a discrepancy I'm noticing between paper_framing.md and the actual paper — the framing document reports plain Cohen's d values, while the paper itself uses d_z values pulled from a different source file. This is a critical inconsistency since paper_framing.md should be the authoritative reference.

Looking at the task description, those reference numbers actually match paper_framing.md, not the paper itself, which confirms the paper is using a different metric. Within the paper the d_z values are internally consistent, but there's a clear mismatch between what the framing document claims and what the paper reports. This is the key finding I need to document in my final report.

Now I'm verifying the paired Δ values across both documents — the median differences for DeepSeek and Qwen match between the paper and paper_framing when accounting for rounding, so at least those are consistent. The discrepancy is really just in how the effect sizes are being reported. Let me scan through the rest of the analysis to catch anything else I might have overlooked.

I'm checking whether the paper properly distinguishes between segment-level and per-problem paired Δ values. Looking at the tables and narrative, the segment-level Δ appears consistently as 0.39→14.59 across the abstract, intro, and conclusion, while the per-problem paired differences show up separately in the cohens-d table. The issue is that the narrative doesn't explicitly label these as segment-level, which could create confusion about which calculation is being referenced. So the paper distinguishes between two different statistics using notation: the aggregate median difference across problems versus the median of per-problem differences. The abstract's phrasing is ambiguous about which one it's referring to, though the numerical value suggests it's the aggregate version. This is worth flagging as a minor clarity issue. Now I'm ready to compile all my findings into a final report.

I've identified two critical issues: first, there's a mismatch between how Cohen's d is calculated in paper_framing.md versus the actual paper—one uses the pooled formula while the other uses the z-based approach, resulting in different values across all models. Second, there's a broken cross-reference in the introduction that points to a section that doesn't exist anywhere in the document.

Looking at the results section, I notice it uses a different label that won't resolve the introduction's reference, which will show as "??" in the compiled PDF. In the discussion, there's also a citation error where confidence interval values are attributed to the wrong table—the text references permutation CIs but the numbers actually come from the Cohen's d bootstrap table. Finally, I'm seeing duplicate equation labels defined in both the background and methodology sections, which will cause LaTeX compilation conflicts.

There's also a precision inconsistency in the Qwen delta values where the discussion shows three decimal places but the table uses two, and the rounding doesn't quite match up—though this might be due to the underlying raw value being slightly different than what's displayed.

I'm also noticing an unverifiable claim about s=0.35 producing a high-phase II value of 0.105, but I can't find any s=0.35 condition in the actual results tables, so the source for that data isn't traceable.

Beyond the content issues, there are several stale files that should be archived or removed: results_5_1.tex with old fp16 data, and a few versioned files with hash suffixes like background_fc6d1d.tex, related_work_46fb53.tex, and methodology_4cc5f3.tex that appear to be outdated.

There's also a reference in background.tex to an appendix section on multiplicative-null that I can't verify without seeing the actual appendix files.

The abstract mentions "median Interaction Index difference" ranging from 0.39 to 14.59 at the segment level, but this could get confused with the per-problem paired median difference of 0.32 to 9.94—the paper does use proper notation with Δ and Δ̃ in the tables, but the prose descriptions aren't always clear about which metric is being referenced.

Now let me check the consistency of the main claims across sections. The strategy-dependent, phase-modulated, and crossover findings all check out with consistent numbers throughout. The discrimination collapse claim is next to verify. The paper is internally consistent on the d values, but I need to reconcile this with the paper_framing reference document—the task spec treats paper_framing as the authoritative source, yet the paper's d_z values come directly from the actual data file. I'm trying to determine which set is actually correct before finalizing my verdict. The paper itself is internally consistent with its d values across sections, so C2's statement holds up—the real issue is that paper_framing.md contains different d values than what the paper actually reports. I'll mark this as a critical discrepancy between the reference document and the paper itself, then move forward with writing up the full audit report.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "2587cbe7-f2f2-4e99-b080-eeccc97d7434",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AVaXjjJRbX7z8U6hWcbvVh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2115,
      "cache_read_input_tokens": 77795,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2115
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

_source line 76_

Now I have the correct picture. The paper uses d_z values (0.44/0.52/0.68/0.80 for DeepSeek) consistently across all sections — my initial read was imprecise. Let me verify the remaining CI attribution issue and then write the report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "74573981-348f-41c3-9550-253f714802d3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AVaXjjJRbX7z8U6hWcbvVh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2115,
      "cache_read_input_tokens": 77795,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2115
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

_source line 77_

<details open><summary>🔧 Tool call — Read · `toolu_01B1Tg1E8CmEnnKXtgcfdJ5a`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex",
  "offset": 143,
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
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "a46fcf19-9f6e-4031-9d74-91672a55a788",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AVaXjjJRbX7z8U6hWcbvVh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2115,
      "cache_read_input_tokens": 77795,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2115
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

_source line 78 · 2026-05-14T09:53:40.659Z_

<details><summary>↩ Tool result · `toolu_01B1Tg1E8CmEnnKXtgcfdJ5a`</summary>

```text
143	\paragraph{Permutation test.}
144	For each problem $i$ and sparsity level $s$, we compute the compound severity difference $\Delta_i^{(\text{strat})} = \mathrm{II}_{\textit{low},i} - \mathrm{II}_{\textit{high},i}$ under each eviction strategy. The test statistic is the median of the paired difference $\widetilde{\Delta} = \text{median}_i\!\bigl(\Delta_i^{(\text{imp})} - \Delta_i^{(\text{rand})}\bigr)$, measuring whether importance-based eviction produces systematically larger phase-dependent severity than random eviction. We permute strategy labels $10{,}000$ times to construct the null distribution and apply Bonferroni correction for 4 sparsity-level comparisons.
145	
146	Table~\ref{tab:permutation} reports the results. All four sparsity levels reject $H_0$ (no strategy difference) after Bonferroni correction ($p_{\text{Bonf}} < 0.005$), with observed median differences increasing monotonically from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$. % exp_id: deepseek_bf16_permtest; source: permutation_test_results.json
147	
148	\begin{table}[t]
149	\centering
150	\small
151	\caption{Paired permutation test (difference statistic) for compound severity: importance vs.\ random eviction on DeepSeek-R1-Distill-Qwen-7B ($n{=}49$ paired problems, $10{,}000$ permutations). $p$-values are Bonferroni-corrected for 4 comparisons.}
152	\label{tab:permutation}
153	\begin{tabular}{@{}rrcl@{}}
154	\toprule
155	$s$ & Observed $\widetilde{\Delta}$ & 95\% CI & $p_{\text{Bonf}}$ \\
156	\midrule
157	0.15 & 0.37 & $[0.19,\; 0.62]$ & 0.0032 \\ % exp_id: deepseek_bf16_permtest_s015; source: permutation_test_results.json s015.permutation_test_difference
158	0.20 & 0.97 & $[0.69,\; 1.49]$ & ${<}\,0.001$ \\ % exp_id: deepseek_bf16_permtest_s020; source: permutation_test_results.json s020.permutation_test_difference
159	0.25 & 3.34 & $[1.66,\; 6.64]$ & ${<}\,0.001$ \\ % exp_id: deepseek_bf16_permtest_s025; source: permutation_test_results.json s025.permutation_test_difference
160	0.30 & 9.85 & $[6.70,\; 16.29]$ & ${<}\,0.001$ \\ % exp_id: deepseek_bf16_permtest_s030; source: permutation_test_results.json s030.permutation_test_difference
161	\bottomrule
162	\end{tabular}
163	\end{table}
164	
165	The monotonic growth of both the point estimate and the CI lower bound ($0.19 \to 0.69 \to 1.66 \to 6.70$) confirms that compound severity amplification under importance-based eviction strengthens with sparsity---not merely in central tendency but also in worst-case lower bounds. % exp_id: deepseek_bf16_permtest; source: permutation_test_results.json
166	
167	\begin{figure}[t]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "9e243d30-b40d-4eeb-ba29-23efc0e0ad12",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex",
      "content": "\\paragraph{Permutation test.}\nFor each problem $i$ and sparsity level $s$, we compute the compound severity difference $\\Delta_i^{(\\text{strat})} = \\mathrm{II}_{\\textit{low},i} - \\mathrm{II}_{\\textit{high},i}$ under each eviction strategy. The test statistic is the median of the paired difference $\\widetilde{\\Delta} = \\text{median}_i\\!\\bigl(\\Delta_i^{(\\text{imp})} - \\Delta_i^{(\\text{rand})}\\bigr)$, measuring whether importance-based eviction produces systematically larger phase-dependent severity than random eviction. We permute strategy labels $10{,}000$ times to construct the null distribution and apply Bonferroni correction for 4 sparsity-level comparisons.\n\nTable~\\ref{tab:permutation} reports the results. All four sparsity levels reject $H_0$ (no strategy difference) after Bonferroni correction ($p_{\\text{Bonf}} < 0.005$), with observed median differences increasing monotonically from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$. % exp_id: deepseek_bf16_permtest; source: permutation_test_results.json\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Paired permutation test (difference statistic) for compound severity: importance vs.\\ random eviction on DeepSeek-R1-Distill-Qwen-7B ($n{=}49$ paired problems, $10{,}000$ permutations). $p$-values are Bonferroni-corrected for 4 comparisons.}\n\\label{tab:permutation}\n\\begin{tabular}{@{}rrcl@{}}\n\\toprule\n$s$ & Observed $\\widetilde{\\Delta}$ & 95\\% CI & $p_{\\text{Bonf}}$ \\\\\n\\midrule\n0.15 & 0.37 & $[0.19,\\; 0.62]$ & 0.0032 \\\\ % exp_id: deepseek_bf16_permtest_s015; source: permutation_test_results.json s015.permutation_test_difference\n0.20 & 0.97 & $[0.69,\\; 1.49]$ & ${<}\\,0.001$ \\\\ % exp_id: deepseek_bf16_permtest_s020; source: permutation_test_results.json s020.permutation_test_difference\n0.25 & 3.34 & $[1.66,\\; 6.64]$ & ${<}\\,0.001$ \\\\ % exp_id: deepseek_bf16_permtest_s025; source: permutation_test_results.json s025.permutation_test_difference\n0.30 & 9.85 & $[6.70,\\; 16.29]$ & ${<}\\,0.001$ \\\\ % exp_id: deepseek_bf16_permtest_s030; source: permutation_test_results.json s030.permutation_test_difference\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe monotonic growth of both the point estimate and the CI lower bound ($0.19 \\to 0.69 \\to 1.66 \\to 6.70$) confirms that compound severity amplification under importance-based eviction strengthens with sparsity---not merely in central tendency but also in worst-case lower bounds. % exp_id: deepseek_bf16_permtest; source: permutation_test_results.json\n\n\\begin{figure}[t]",
      "numLines": 25,
      "startLine": 143,
      "totalLines": 199
    }
  }
}
```

</details>

---

### Runtime record

_source line 79_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed_warning",
    "resetsAt": 1779267600,
    "rateLimitType": "seven_day",
    "utilization": 0.41,
    "isUsingOverage": false
  },
  "uuid": "0f7931e1-2177-4293-8159-d6123ebb189e",
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86"
}
```

---

### Assistant

_source line 80_

<details><summary>Logged reasoning block</summary>

```text
OK, so now I can clearly see:

**Table permutation CIs:**
- s015: [0.19, 0.62]
- s020: [0.69, 1.49]
- s025: [1.66, 6.64]
- s030: [6.70, 16.29]

**Table cohens-d CIs:**
- s015: [0.20, 0.47]
- s020: [0.66, 1.26]
- s025: [2.83, 5.29]
- s030: [8.39, 16.65]


I'm noticing a mismatch in the Discussion section—it's citing Cohen's d values (0.20 and 8.39) when it should be using the permutation test values (0.19 and 6.70), and the interval [8.39, 16.65] is also from Cohen's d rather than permutation at s030.

The core issue is that these are actually testing different things: the permutation test measures the difference between importance and random strategies, while Cohen's d measures the magnitude of the importance-based phase difference itself, so they have different confidence intervals and are answering different hypotheses.

Looking at the specific citations in the discussion, the text attributes values like 0.20 to 8.39 and the interval [8.39, 16.65] to "permutation CIs," but these numbers are actually coming from the Cohen's d table. The comment about "updated bf16 B=10000 per-problem paired CIs" confirms these are Cohen's d results being mislabeled as permutation results. This is a clear data attribution error in discussion.tex around line 86 that needs to be corrected. I'm noticing the Limitations section actually does reference permutation CI values—the lower bounds of 0.20 to 8.39 match the permutation results, not the Cohen's d values. So this paragraph is correctly using permutation CIs despite my earlier concern about the table reference being wrong. The wider confidence intervals at higher sparsity levels make sense given the increased variance in the severity amplification across individual problems.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "936c915e-0097-4ba9-b0d7-2b930ad82cb0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AhxaSRowbJGSCtULi81e7P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5158,
      "cache_read_input_tokens": 79910,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5158
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

_source line 81_

All data verified. Writing the audit report now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "da923806-3902-4da4-ab43-33bdeb83648b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AhxaSRowbJGSCtULi81e7P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5158,
      "cache_read_input_tokens": 79910,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5158
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

_source line 82_

<details open><summary>🔧 Tool call — Write · `toolu_013EwSUPMsDra61sN6ZHSwBc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/consistency_audit_report.md",
  "content": "# Consistency Audit Report — Phase-Gated Compound Sparsity\n\n> Audit date: 2026-05-14 | Scope: all current .tex files + paper_framing.md | Auditor: automated\n\n---\n\n## CRITICAL Issues\n\n**[CRITICAL] introduction.tex:27,28,33 — Broken cross-reference `\\ref{sec:experiments}`**\n`sec:experiments` is not defined in any current .tex file. The results section uses `\\label{sec:results}`. These three references will produce \"??\" in the compiled PDF.\n- Line 27: `(\\S\\ref{sec:experiments})` → should be `(\\S\\ref{sec:results})`\n- Line 28: `(\\S\\ref{sec:experiments})` → should be `(\\S\\ref{sec:results})`\n- Line 33: `\\S\\ref{sec:experiments} presents the main results` → `\\S\\ref{sec:results}`\n\n**[CRITICAL] discussion.tex:86 — CI values attributed to wrong table**\nText says \"permutation CIs\" and references `Table~\\ref{tab:permutation}`, but the CI values quoted ([0.20, 0.47]→[8.39, 16.65]) are from Table cohens-d (per-problem paired bootstrap), not from Table permutation.\n- Text: \"CI lower bounds increasing from $0.20$ to $8.39$\" — cohens-d lower bounds\n- Text: \"permutation CIs…$[8.39, 16.65]$ at $s{=}0.30$\" — actually cohens-d CI\n- Actual permutation CI lower bounds (Table permutation): $0.19 \\to 0.69 \\to 1.66 \\to 6.70$\n- Actual permutation CI at s=0.30: $[6.70, 16.29]$\n- Fix: either change values to permutation CIs, or change text/reference to Table cohens-d.\n\n**[CRITICAL] paper_framing.md vs paper — Cohen's d metric mismatch**\npaper_framing.md reports Cohen's d (pooled SD) while the paper uses d_z (paired z-score). All paper sections are internally consistent using d_z, but paper_framing.md disagrees:\n\n| Sparsity | paper_framing.md (d) | Paper all sections (d_z) |\n|----------|---------------------|------------------------|\n| DeepSeek s015 | 0.61 (medium) | 0.44 (small) |\n| DeepSeek s020 | 0.73 (medium) | 0.52 (medium) |\n| DeepSeek s025 | 0.95 (large)  | 0.68 (medium) |\n| DeepSeek s030 | 1.13 (large)  | 0.80 (large) |\n| Qwen s015     | 0.37 (small)  | 0.28 (small) |\n| Qwen s020     | 0.72 (medium) | 0.55 (medium) |\n| Qwen s025     | 1.23 (large)  | 0.89 (large) |\n| Qwen s030     | 1.44 (large)  | 1.02 (large) |\n\nThe paper is internally consistent (abstract, intro, results, discussion, conclusion all use d_z). But paper_framing.md — the canonical reference document — uses different values. Either update paper_framing.md to d_z, or justify why the paper uses d_z instead of pooled d.\n\n---\n\n## WARNING Issues\n\n**[WARNING] background.tex:58,82 + methodology.tex:62,69 — Duplicate equation labels**\n`\\label{eq:ii}` defined in both background.tex:58 and methodology.tex:62. `\\label{eq:gradient}` defined in both background.tex:82 and methodology.tex:69. LaTeX will use the last-defined instance; cross-references may point to the wrong equation. background.tex comment explicitly says \"Methodology.tex should reference these via \\eqref rather than redefining.\" Fix: remove `\\label{eq:ii}` and `\\label{eq:gradient}` from methodology.tex, replace with `\\eqref{eq:ii}` and `\\eqref{eq:gradient}`.\n\n**[WARNING] discussion.tex:29 — Qwen Δ rounding inconsistency at s=0.20**\nDiscussion gives Qwen segment-level Δ at 3dp as $0.235$, but Table cross-model (results.tex) rounds to $0.23$ at 2dp. If the raw value is ≥0.235, it should round to 0.24 at 2dp, not 0.23. Minor but a reviewer checking precision could flag it. Verify against raw data and align precision.\n\n**[WARNING] discussion.tex:11 — Unverifiable s=0.35 data point**\nText: \"at $s = 0.35$, high-phase II rises to 0.105\". No s=0.35 condition appears in any results table or experimental setup. Either add source attribution (appendix/supplementary) or remove. A reviewer will ask where this number comes from.\n\n---\n\n## INFO Issues\n\n**[INFO] Stale files — should be archived or deleted before submission**\nThe following files in `artifacts/_project/paper/` are outdated and should not be included:\n- `results_5_1.tex` — fp16 old data, contains multiple `% PENDING-BF16` markers, references old float16 numbers\n- `background_fc6d1d.tex` — hash-suffixed backup of background.tex\n- `related_work_46fb53.tex` — hash-suffixed backup of related_work.tex\n- `methodology_4cc5f3.tex` — hash-suffixed backup of methodology.tex\n\n**[INFO] background.tex:72 — Appendix reference `app:multiplicative-null`**\nCannot verify existence without appendix files. Ensure appendix is included in the submission.\n\n**[INFO] Conclusion/discussion say \"~1/5 of DeepSeek\" for Qwen magnitude**\nActual ratio ranges from 1/10 (s=0.15: 0.04/0.39) to 1/5 (s=0.30: 2.94/14.59). results.tex:124 correctly says \"one-tenth to one-fifth\". The shorthand \"~1/5\" in conclusion.tex:16 and discussion.tex is an approximation biased toward the high end. Minor.\n\n---\n\n## Consistency Checks — PASS\n\n### 1. Segment-level Δ (DeepSeek): 0.39 / 1.48 / 7.16 / 14.59\n- abstract.tex:7 ✓ (endpoints 0.39→14.59)\n- introduction.tex:14 ✓ (endpoints 0.39→14.59)\n- results.tex Table aggregate-ii ✓\n- results.tex Table main-results ✓\n- conclusion.tex:8 ✓\n- discussion.tex:29 ✓\n\n### 2. Segment-level Δ (Qwen): 0.04 / 0.23 / 1.27 / 2.94\n- results.tex Table cross-model ✓\n- results.tex:124 text ✓ (endpoints 0.04→2.94)\n\n### 3. Cohen's d_z (DeepSeek): 0.44 / 0.52 / 0.68 / 0.80\n- abstract.tex:7 ✓ (endpoints 0.44→0.80)\n- introduction.tex:14 ✓ (endpoints 0.44→0.80)\n- results.tex Table cohens-d ✓\n- results.tex:195 text ✓\n- conclusion.tex:10 ✓\n- discussion.tex:29 ✓ (full precision 0.442→0.803)\n\n### 4. Cohen's d_z (Qwen): 0.28 / 0.55 / 0.89 / 1.02\n- abstract.tex:10 ✓ (d≥0.55 at s≥0.20)\n- introduction.tex:15 ✓ (d≥0.55, d=0.28 at s015)\n- results.tex Table cohens-d ✓\n- results.tex:196 text ✓ (d≥0.55)\n- conclusion.tex:16 ✓ (d≥0.55)\n- discussion.tex:29 ✓ (full precision 0.549→1.022)\n\n### 5. G (severity gradient): 69 / 103 / 222 / 274\n- results.tex Table main-results ✓\n- analysis.tex:5 ✓ (69–274×)\n- discussion.tex:9 ✓ (69–274×)\n\n### 6. High-phase II: 0.006 / 0.015 / 0.032 / 0.053\n- results.tex Table main-results ✓\n- discussion.tex:11 ✓ (<0.06 approximation)\n\n### 7. Permutation observed Δ: 0.37 / 0.97 / 3.34 / 9.85\n- results.tex Table permutation ✓\n- results.tex:146 text ✓ (endpoints 0.37→9.85)\n\n### 8. Random 7/8 FAIL, Qwen s030 PASS p=0.012 d=−0.04\n- abstract.tex:8 ✓\n- introduction.tex:16 ✓\n- results.tex:126 ✓\n- discussion.tex:21 ✓\n- conclusion.tex:8 ✓\n\n### 9. Sample sizes: n=50, DeepSeek n=49, Qwen n=46\n- All sections consistent ✓\n\n### 10. B=10000 bootstrap\n- methodology.tex:78, results.tex tables, discussion.tex:84 — all consistent ✓\n\n### 11. Bonferroni p<0.005\n- abstract.tex:7, introduction.tex:14, conclusion.tex:10 — all consistent ✓\n\n### 12. Per-problem paired Δ: 0.32 / 1.15 / 3.97 / 9.94 (DeepSeek)\n- results.tex Table cohens-d ✓\n- paper_framing.md ✓ (matches)\n- Correctly distinguished from segment-level Δ in tables ✓\n\n### 13. Cross-model Spearman ρ=1.0, gradient permutation p=0.043\n- abstract.tex:10, results.tex:124, conclusion.tex:16, discussion.tex:25 — all consistent ✓\n\n### 14. Crossover numbers (s=0.25): imp high=0.032, rand high=0.818; imp low=7.196, rand low=1.363\n- abstract.tex:9, results.tex:84, conclusion.tex:12, discussion.tex:13 — all consistent ✓\n\n### 15. Sub-exponential growth ratios: 3.8× / 4.8× / 2.0×\n- results.tex:69, discussion.tex:96 — consistent ✓\n\n---\n\n## Claim Consistency (C1–C6)\n\n| Claim | Status | Cross-section consistency |\n|-------|--------|--------------------------|\n| C1: Strategy-dependent | ✓ PASS | All sections consistent |\n| C2: Phase-modulated | ✓ PASS | All sections consistent |\n| C3: Crossover | ✓ PASS | Numbers match everywhere |\n| C4: Discrimination collapse primary, entropy model-dependent | ✓ PASS | Abstract doesn't overclaim entropy universality; conclusion correctly qualifies \"2/4 conditions\" |\n| C5: Cross-model (not cross-architecture) | ✓ PASS | Never called \"cross-architecture\" in claims; only in future-work context |\n| C6: Sub-exponential | ✓ PASS | Consistent everywhere |\n\n**C4 special check**: Abstract says \"entropy-discrimination collapse\" as compound term but describes it as \"head pruning flattens cumulative importance scores\" — this is about discrimination, not entropy universality. ✓\n**C5 special check**: No instance of \"cross-architecture\" used to describe current findings. ✓\n**Random masking check**: Never says \"no phase gradient\"; always says \"7/8 FAIL\". ✓\n\n---\n\n## Citation Completeness\n\nNo `placeholder_xxx` or suspicious citation keys found in current .tex files. All `\\cite{}` keys appear to reference legitimate entries. ✓\n\n---\n\n## Verdict: **FAIL — 3 CRITICAL issues require fixes**\n\n### Fix list (priority order):\n\n1. **introduction.tex** — Replace 3 instances of `\\ref{sec:experiments}` with `\\ref{sec:results}`\n2. **discussion.tex:86** — Fix CI values to match Table permutation ($0.19 \\to 6.70$; $[6.70, 16.29]$) or change text to reference Table cohens-d\n3. **paper_framing.md** — Update Cohen's d values to match the paper's d_z values (DeepSeek 0.44→0.80, Qwen 0.28→1.02), or document that the paper intentionally uses d_z with a note explaining the difference\n4. **methodology.tex** — Remove duplicate `\\label{eq:ii}` and `\\label{eq:gradient}`, use `\\eqref` instead\n5. **discussion.tex:29** — Verify Qwen s020 Δ precision (0.235 vs 0.23)\n6. **discussion.tex:11** — Add source for s=0.35 data or remove\n7. **Archive stale files** — Move results_5_1.tex, background_fc6d1d.tex, related_work_46fb53.tex, methodology_4cc5f3.tex out of paper/\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "8e1d4a66-fac3-455b-bf2f-24c30161e6ce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AhxaSRowbJGSCtULi81e7P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5158,
      "cache_read_input_tokens": 79910,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5158
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

_source line 83 · 2026-05-14T09:55:21.065Z_

<details><summary>↩ Tool result · `toolu_013EwSUPMsDra61sN6ZHSwBc`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/consistency_audit_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "257b8b9e-6984-42ec-9520-4f0969f45b33",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/consistency_audit_report.md",
    "content": "# Consistency Audit Report — Phase-Gated Compound Sparsity\n\n> Audit date: 2026-05-14 | Scope: all current .tex files + paper_framing.md | Auditor: automated\n\n---\n\n## CRITICAL Issues\n\n**[CRITICAL] introduction.tex:27,28,33 — Broken cross-reference `\\ref{sec:experiments}`**\n`sec:experiments` is not defined in any current .tex file. The results section uses `\\label{sec:results}`. These three references will produce \"??\" in the compiled PDF.\n- Line 27: `(\\S\\ref{sec:experiments})` → should be `(\\S\\ref{sec:results})`\n- Line 28: `(\\S\\ref{sec:experiments})` → should be `(\\S\\ref{sec:results})`\n- Line 33: `\\S\\ref{sec:experiments} presents the main results` → `\\S\\ref{sec:results}`\n\n**[CRITICAL] discussion.tex:86 — CI values attributed to wrong table**\nText says \"permutation CIs\" and references `Table~\\ref{tab:permutation}`, but the CI values quoted ([0.20, 0.47]→[8.39, 16.65]) are from Table cohens-d (per-problem paired bootstrap), not from Table permutation.\n- Text: \"CI lower bounds increasing from $0.20$ to $8.39$\" — cohens-d lower bounds\n- Text: \"permutation CIs…$[8.39, 16.65]$ at $s{=}0.30$\" — actually cohens-d CI\n- Actual permutation CI lower bounds (Table permutation): $0.19 \\to 0.69 \\to 1.66 \\to 6.70$\n- Actual permutation CI at s=0.30: $[6.70, 16.29]$\n- Fix: either change values to permutation CIs, or change text/reference to Table cohens-d.\n\n**[CRITICAL] paper_framing.md vs paper — Cohen's d metric mismatch**\npaper_framing.md reports Cohen's d (pooled SD) while the paper uses d_z (paired z-score). All paper sections are internally consistent using d_z, but paper_framing.md disagrees:\n\n| Sparsity | paper_framing.md (d) | Paper all sections (d_z) |\n|----------|---------------------|------------------------|\n| DeepSeek s015 | 0.61 (medium) | 0.44 (small) |\n| DeepSeek s020 | 0.73 (medium) | 0.52 (medium) |\n| DeepSeek s025 | 0.95 (large)  | 0.68 (medium) |\n| DeepSeek s030 | 1.13 (large)  | 0.80 (large) |\n| Qwen s015     | 0.37 (small)  | 0.28 (small) |\n| Qwen s020     | 0.72 (medium) | 0.55 (medium) |\n| Qwen s025     | 1.23 (large)  | 0.89 (large) |\n| Qwen s030     | 1.44 (large)  | 1.02 (large) |\n\nThe paper is internally consistent (abstract, intro, results, discussion, conclusion all use d_z). But paper_framing.md — the canonical reference document — uses different values. Either update paper_framing.md to d_z, or justify why the paper uses d_z instead of pooled d.\n\n---\n\n## WARNING Issues\n\n**[WARNING] background.tex:58,82 + methodology.tex:62,69 — Duplicate equation labels**\n`\\label{eq:ii}` defined in both background.tex:58 and methodology.tex:62. `\\label{eq:gradient}` defined in both background.tex:82 and methodology.tex:69. LaTeX will use the last-defined instance; cross-references may point to the wrong equation. background.tex comment explicitly says \"Methodology.tex should reference these via \\eqref rather than redefining.\" Fix: remove `\\label{eq:ii}` and `\\label{eq:gradient}` from methodology.tex, replace with `\\eqref{eq:ii}` and `\\eqref{eq:gradient}`.\n\n**[WARNING] discussion.tex:29 — Qwen Δ rounding inconsistency at s=0.20**\nDiscussion gives Qwen segment-level Δ at 3dp as $0.235$, but Table cross-model (results.tex) rounds to $0.23$ at 2dp. If the raw value is ≥0.235, it should round to 0.24 at 2dp, not 0.23. Minor but a reviewer checking precision could flag it. Verify against raw data and align precision.\n\n**[WARNING] discussion.tex:11 — Unverifiable s=0.35 data point**\nText: \"at $s = 0.35$, high-phase II rises to 0.105\". No s=0.35 condition appears in any results table or experimental setup. Either add source attribution (appendix/supplementary) or remove. A reviewer will ask where this number comes from.\n\n---\n\n## INFO Issues\n\n**[INFO] Stale files — should be archived or deleted before submission**\nThe following files in `artifacts/_project/paper/` are outdated and should not be included:\n- `results_5_1.tex` — fp16 old data, contains multiple `% PENDING-BF16` markers, references old float16 numbers\n- `background_fc6d1d.tex` — hash-suffixed backup of background.tex\n- `related_work_46fb53.tex` — hash-suffixed backup of related_work.tex\n- `methodology_4cc5f3.tex` — hash-suffixed backup of methodology.tex\n\n**[INFO] background.tex:72 — Appendix reference `app:multiplicative-null`**\nCannot verify existence without appendix files. Ensure appendix is included in the submission.\n\n**[INFO] Conclusion/discussion say \"~1/5 of DeepSeek\" for Qwen magnitude**\nActual ratio ranges from 1/10 (s=0.15: 0.04/0.39) to 1/5 (s=0.30: 2.94/14.59). results.tex:124 correctly says \"one-tenth to one-fifth\". The shorthand \"~1/5\" in conclusion.tex:16 and discussion.tex is an approximation biased toward the high end. Minor.\n\n---\n\n## Consistency Checks — PASS\n\n### 1. Segment-level Δ (DeepSeek): 0.39 / 1.48 / 7.16 / 14.59\n- abstract.tex:7 ✓ (endpoints 0.39→14.59)\n- introduction.tex:14 ✓ (endpoints 0.39→14.59)\n- results.tex Table aggregate-ii ✓\n- results.tex Table main-results ✓\n- conclusion.tex:8 ✓\n- discussion.tex:29 ✓\n\n### 2. Segment-level Δ (Qwen): 0.04 / 0.23 / 1.27 / 2.94\n- results.tex Table cross-model ✓\n- results.tex:124 text ✓ (endpoints 0.04→2.94)\n\n### 3. Cohen's d_z (DeepSeek): 0.44 / 0.52 / 0.68 / 0.80\n- abstract.tex:7 ✓ (endpoints 0.44→0.80)\n- introduction.tex:14 ✓ (endpoints 0.44→0.80)\n- results.tex Table cohens-d ✓\n- results.tex:195 text ✓\n- conclusion.tex:10 ✓\n- discussion.tex:29 ✓ (full precision 0.442→0.803)\n\n### 4. Cohen's d_z (Qwen): 0.28 / 0.55 / 0.89 / 1.02\n- abstract.tex:10 ✓ (d≥0.55 at s≥0.20)\n- introduction.tex:15 ✓ (d≥0.55, d=0.28 at s015)\n- results.tex Table cohens-d ✓\n- results.tex:196 text ✓ (d≥0.55)\n- conclusion.tex:16 ✓ (d≥0.55)\n- discussion.tex:29 ✓ (full precision 0.549→1.022)\n\n### 5. G (severity gradient): 69 / 103 / 222 / 274\n- results.tex Table main-results ✓\n- analysis.tex:5 ✓ (69–274×)\n- discussion.tex:9 ✓ (69–274×)\n\n### 6. High-phase II: 0.006 / 0.015 / 0.032 / 0.053\n- results.tex Table main-results ✓\n- discussion.tex:11 ✓ (<0.06 approximation)\n\n### 7. Permutation observed Δ: 0.37 / 0.97 / 3.34 / 9.85\n- results.tex Table permutation ✓\n- results.tex:146 text ✓ (endpoints 0.37→9.85)\n\n### 8. Random 7/8 FAIL, Qwen s030 PASS p=0.012 d=−0.04\n- abstract.tex:8 ✓\n- introduction.tex:16 ✓\n- results.tex:126 ✓\n- discussion.tex:21 ✓\n- conclusion.tex:8 ✓\n\n### 9. Sample sizes: n=50, DeepSeek n=49, Qwen n=46\n- All sections consistent ✓\n\n### 10. B=10000 bootstrap\n- methodology.tex:78, results.tex tables, discussion.tex:84 — all consistent ✓\n\n### 11. Bonferroni p<0.005\n- abstract.tex:7, introduction.tex:14, conclusion.tex:10 — all consistent ✓\n\n### 12. Per-problem paired Δ: 0.32 / 1.15 / 3.97 / 9.94 (DeepSeek)\n- results.tex Table cohens-d ✓\n- paper_framing.md ✓ (matches)\n- Correctly distinguished from segment-level Δ in tables ✓\n\n### 13. Cross-model Spearman ρ=1.0, gradient permutation p=0.043\n- abstract.tex:10, results.tex:124, conclusion.tex:16, discussion.tex:25 — all consistent ✓\n\n### 14. Crossover numbers (s=0.25): imp high=0.032, rand high=0.818; imp low=7.196, rand low=1.363\n- abstract.tex:9, results.tex:84, conclusion.tex:12, discussion.tex:13 — all consistent ✓\n\n### 15. Sub-exponential growth ratios: 3.8× / 4.8× / 2.0×\n- results.tex:69, discussion.tex:96 — consistent ✓\n\n---\n\n## Claim Consistency (C1–C6)\n\n| Claim | Status | Cross-section consistency |\n|-------|--------|--------------------------|\n| C1: Strategy-dependent | ✓ PASS | All sections consistent |\n| C2: Phase-modulated | ✓ PASS | All sections consistent |\n| C3: Crossover | ✓ PASS | Numbers match everywhere |\n| C4: Discrimination collapse primary, entropy model-dependent | ✓ PASS | Abstract doesn't overclaim entropy universality; conclusion correctly qualifies \"2/4 conditions\" |\n| C5: Cross-model (not cross-architecture) | ✓ PASS | Never called \"cross-architecture\" in claims; only in future-work context |\n| C6: Sub-exponential | ✓ PASS | Consistent everywhere |\n\n**C4 special check**: Abstract says \"entropy-discrimination collapse\" as compound term but describes it as \"head pruning flattens cumulative importance scores\" — this is about discrimination, not entropy universality. ✓\n**C5 special check**: No instance of \"cross-architecture\" used to describe current findings. ✓\n**Random masking check**: Never says \"no phase gradient\"; always says \"7/8 FAIL\". ✓\n\n---\n\n## Citation Completeness\n\nNo `placeholder_xxx` or suspicious citation keys found in current .tex files. All `\\cite{}` keys appear to reference legitimate entries. ✓\n\n---\n\n## Verdict: **FAIL — 3 CRITICAL issues require fixes**\n\n### Fix list (priority order):\n\n1. **introduction.tex** — Replace 3 instances of `\\ref{sec:experiments}` with `\\ref{sec:results}`\n2. **discussion.tex:86** — Fix CI values to match Table permutation ($0.19 \\to 6.70$; $[6.70, 16.29]$) or change text to reference Table cohens-d\n3. **paper_framing.md** — Update Cohen's d values to match the paper's d_z values (DeepSeek 0.44→0.80, Qwen 0.28→1.02), or document that the paper intentionally uses d_z with a note explaining the difference\n4. **methodology.tex** — Remove duplicate `\\label{eq:ii}` and `\\label{eq:gradient}`, use `\\eqref` instead\n5. **discussion.tex:29** — Verify Qwen s020 Δ precision (0.235 vs 0.23)\n6. **discussion.tex:11** — Add source for s=0.35 data or remove\n7. **Archive stale files** — Move results_5_1.tex, background_fc6d1d.tex, related_work_46fb53.tex, methodology_4cc5f3.tex out of paper/\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 84_

报告已写入 `artifacts/consistency_audit_report.md`。

**结论: FAIL — 3 个 CRITICAL 问题需修复。**

关键发现：

1. **introduction.tex** 有 3 处 `\ref{sec:experiments}` 引用了不存在的 label（应为 `sec:results`），编译会出 "??"
2. **discussion.tex:86** 把 Table cohens-d 的 CI 值 ([0.20→8.39], [8.39, 16.65]) 标注为 "permutation CIs" 并引用了 Table permutation，实际 permutation CI 是 [0.19→6.70], [6.70, 16.29]
3. **paper_framing.md** 的 Cohen's d 用的是 pooled d（0.61→1.13），论文全文用的是 d_z（0.44→0.80）——论文内部一致，但与 paper_framing 不一致

另有 3 个 WARNING（重复 equation label、Qwen Δ 精度舍入、s=0.35 无来源数据）和 4 个 stale 文件待归档。数字一致性、claim 表述、引用完整性均通过。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "uuid": "9ae55e04-1f67-4862-96cb-2593644c5667",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S7MBz2tJfnowuqR6GfNds7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4944,
      "cache_read_input_tokens": 85068,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4944
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

### Runtime record

_source line 85_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed_warning",
    "resetsAt": 1779267600,
    "rateLimitType": "seven_day",
    "utilization": 0.42,
    "isUsingOverage": false
  },
  "uuid": "d7bc18c7-0768-42bb-b820-f5125d796250",
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86"
}
```

---

### Task result

_source line 86_

报告已写入 `artifacts/consistency_audit_report.md`。

**结论: FAIL — 3 个 CRITICAL 问题需修复。**

关键发现：

1. **introduction.tex** 有 3 处 `\ref{sec:experiments}` 引用了不存在的 label（应为 `sec:results`），编译会出 "??"
2. **discussion.tex:86** 把 Table cohens-d 的 CI 值 ([0.20→8.39], [8.39, 16.65]) 标注为 "permutation CIs" 并引用了 Table permutation，实际 permutation CI 是 [0.19→6.70], [6.70, 16.29]
3. **paper_framing.md** 的 Cohen's d 用的是 pooled d（0.61→1.13），论文全文用的是 d_z（0.44→0.80）——论文内部一致，但与 paper_framing 不一致

另有 3 个 WARNING（重复 equation label、Qwen Δ 精度舍入、s=0.35 无来源数据）和 4 个 stale 文件待归档。数字一致性、claim 表述、引用完整性均通过。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 628954,
  "duration_api_ms": 630419,
  "num_turns": 23,
  "stop_reason": "end_turn",
  "session_id": "e3e7aace-1b13-41f4-b483-49ca612a8f86",
  "total_cost_usd": 1.5990696500000001,
  "usage": {
    "input_tokens": 194,
    "cache_creation_input_tokens": 78171,
    "cache_read_input_tokens": 584449,
    "output_tokens": 30884,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 78171,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 344,
        "cache_read_input_tokens": 85068,
        "cache_creation_input_tokens": 4944,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 4944
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2049,
      "outputTokens": 1067,
      "cacheReadInputTokens": 36674,
      "cacheCreationInputTokens": 27324,
      "webSearchRequests": 0,
      "costUSD": 0.045206399999999994,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 194,
      "outputTokens": 30884,
      "cacheReadInputTokens": 584449,
      "cacheCreationInputTokens": 78171,
      "webSearchRequests": 0,
      "costUSD": 1.55386325,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "aa8b5516-1e99-4bed-b99d-be055a9a1e1d"
}
```

</details>

---
