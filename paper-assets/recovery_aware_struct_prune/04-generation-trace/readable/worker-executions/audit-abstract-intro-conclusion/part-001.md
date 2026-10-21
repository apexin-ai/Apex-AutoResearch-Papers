# audit abstract intro conclusion — Part 1 of 2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Worker execution logs

[Transcript overview](../audit-abstract-intro-conclusion.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/f7/f7e55c830b100713d244.json)

## Before a recorded user message

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
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
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__register_artifact",
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
  "uuid": "b5535f92-bf33-4247-a388-bce63209cbc3",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/memory/"
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
    "resetsAt": 1779612600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "ee066359-047e-4cf6-8505-169fcb244c2e",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db"
}
```

---


### Assistant

_source line 4_

我先读取四个 LaTeX 文件和 registry 数据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "6e697d4c-27e7-4c16-b8ca-ed8d96199865",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013tZUEJiGLjd4MBdX4Ssicy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12910,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12910
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

<details open><summary>🔧 Tool call — Read · `toolu_01Be3beASWGvRxYwDUbesD5E`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "c48b83c5-319e-4386-bcae-5605f28baccc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013tZUEJiGLjd4MBdX4Ssicy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12910,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12910
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

_source line 6 · 2026-05-24T04:32:23.170Z_

<details><summary>↩ Tool result · `toolu_01Be3beASWGvRxYwDUbesD5E`</summary>

```text
1	Fine-grained structured pruning of reasoning Large Language Models (LLMs), which removes MLP channel groups rather than entire layers, is typically followed by recovery training (SFT or RLVR) to restore reasoning capabilities.
2	RLVR is widely believed to be superior, yet we show this hierarchy reflects suboptimal pruning, not a fundamental property of RL\@.
3	When pruning preserves representational diversity, recovery method choice becomes irrelevant---a phenomenon we term \emph{reward-accuracy decoupling}: GRPO and SFT produce near-identical accuracy despite vastly different reward trajectories, a pattern that holds across sparsity levels and benchmarks.
4	We propose Recovery-Aware Structured Pruning (\rasp{}), which balances gradient importance with CKA-based representational diversity via a coefficient $\alpha$.
5	On DeepSeek-R1-Distill-Qwen-7B at 20\% sparsity, a dose-response analysis reveals an inverted-U in recovery accuracy, peaking at $\alpha{=}2.0$ (66.11\% on GSM8K).
6	Under GRPO training, four pruning criteria produce a \emph{recovery capacity spectrum}: diversity-preserving pruning achieves active learning (peak reward 4.4$\times$ vs importance-only), while importance-dominated pruning collapses entirely.
7	The spectrum tracks preserved representational diversity rather than gradient importance, with initial evidence for generality across scales (1.5B) and architectures (Qwen2.5-Math-7B).
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "b072245a-cac4-4cad-9647-85e2e43572fa",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/abstract.tex",
      "content": "Fine-grained structured pruning of reasoning Large Language Models (LLMs), which removes MLP channel groups rather than entire layers, is typically followed by recovery training (SFT or RLVR) to restore reasoning capabilities.\nRLVR is widely believed to be superior, yet we show this hierarchy reflects suboptimal pruning, not a fundamental property of RL\\@.\nWhen pruning preserves representational diversity, recovery method choice becomes irrelevant---a phenomenon we term \\emph{reward-accuracy decoupling}: GRPO and SFT produce near-identical accuracy despite vastly different reward trajectories, a pattern that holds across sparsity levels and benchmarks.\nWe propose Recovery-Aware Structured Pruning (\\rasp{}), which balances gradient importance with CKA-based representational diversity via a coefficient $\\alpha$.\nOn DeepSeek-R1-Distill-Qwen-7B at 20\\% sparsity, a dose-response analysis reveals an inverted-U in recovery accuracy, peaking at $\\alpha{=}2.0$ (66.11\\% on GSM8K).\nUnder GRPO training, four pruning criteria produce a \\emph{recovery capacity spectrum}: diversity-preserving pruning achieves active learning (peak reward 4.4$\\times$ vs importance-only), while importance-dominated pruning collapses entirely.\nThe spectrum tracks preserved representational diversity rather than gradient importance, with initial evidence for generality across scales (1.5B) and architectures (Qwen2.5-Math-7B).\n",
      "numLines": 8,
      "startLine": 1,
      "totalLines": 8
    }
  }
}
```

</details>

---


### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_0117STtJnxpKMjMrytzGy2xY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "59307e2c-08bb-4c66-b7d3-e72bf92bbc04",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013tZUEJiGLjd4MBdX4Ssicy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12910,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12910
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

_source line 8 · 2026-05-24T04:32:23.627Z_

<details><summary>↩ Tool result · `toolu_0117STtJnxpKMjMrytzGy2xY`</summary>

```text
1	\section{Introduction}
2	\label{sec:intro}
3	
4	Reasoning Large Language Models can be compressed through structured pruning, but the pruned model must recover its reasoning capabilities through fine-tuning.
5	The dominant assumption is that the recovery paradigm (SFT versus RLVR) determines recovery quality: \citet{selfhealing2025} demonstrate that RLVR restores pruned reasoning models to near-original accuracy, significantly outperforming SFT.
6	We show that this hierarchy is an artifact of suboptimal pruning.
7	When pruning preserves representational diversity, recovery method choice becomes irrelevant: at 20\% sparsity, mean $|\Delta(\text{GRPO}-\text{SFT})| {=} 0.54$\,pp across the four fine-grained criteria (max $0.61$\,pp); including dose-response variations and MBPP, the maximum is $1.34$\,pp.
8	What matters is not \emph{how} you train after pruning, but \emph{which structures} you remove.
9	
10	This gap is surprising because RL and SFT impose fundamentally different demands on model representations: RL compresses incorrect paths while SFT expands correct ones~\citep{rlsqueezes2026}. Yet existing structured pruning methods for reasoning LLMs~\citep{graspprune2026,resp2025,llmpruner2023,bonsai2025} optimize for post-pruning quality without studying how the criterion shapes downstream RL recovery.
11	No prior work has compared multiple pruning criteria under RL or asked whether the ``RLVR $>$ SFT'' advantage persists across pruning strategies.
12	We note that \citet{selfhealing2025} evaluate unstructured magnitude pruning retaining 96.5\% of dense parameters; our findings concern fine-grained structural pruning where entire channel groups are removed, and the two settings may impose different demands on RL recovery.
13	
14	\begin{figure}[t]
15	\centering
16	\includegraphics[width=\columnwidth]{../figures/paper/fig1_dose_response.pdf}
17	\caption{Dose-response curve for the CKA diversity coefficient $\alpha$ at 20\% MLP channel sparsity on GSM8K ($N{=}1{,}319$). Recovery accuracy follows an inverted-U, peaking at $\alpha{=}2.0$ (66.11\%). SFT and GRPO curves nearly overlap ($|\Delta| \leq 1.14$\,pp at every point), visually demonstrating reward-accuracy decoupling: the pruning criterion, not the recovery paradigm, determines outcome.}
18	\label{fig:dose_response}
19	\end{figure}
20	
21	We present a controlled comparison on DeepSeek-R1-Distill-Qwen-7B~\citep{deepseek2025r1} at 20\% MLP channel sparsity, varying the balance between gradient importance and CKA-based representational diversity~\citep{kornblith2019cka} via a coefficient $\alpha$ in the pruning score (Figure~\ref{fig:dose_response}).
22	The dose-response curve reveals an inverted-U: recovery peaks at $\alpha{=}2.0$ (66.11\% GRPO on GSM8K~\citep{cobbe2021gsm8k}), where importance and diversity reach optimal balance.
23	Under GRPO~\citep{shao2024grpo} training, four criteria produce a \textbf{recovery capacity spectrum}---from active learning (CKA-only, peak reward 4.4$\times$ Standard) through stagnation (Random) to collapse ($\alpha{=}1.0$)---that tracks preserved representational diversity, not gradient importance.
24	A depth pruning baseline (ShortGPT;~\citealp{shortgpt2024}) is the only method with $|\Delta| > 1$\,pp on GSM8K ($-$1.36\,pp), confirming that pruning granularity interacts with RL trainability.
25	
26	Our contributions are:
27	\begin{enumerate}[nosep,leftmargin=*]
28	    \item \textbf{Reward-accuracy decoupling.} At 20--25\% sparsity, GRPO and SFT produce near-identical accuracy across all four fine-grained criteria: mean $|\Delta| {=} 0.54$\,pp at 20\% (max $0.61$\,pp; $1.34$\,pp including dose-response variations and MBPP). At 15\%, GRPO can still amplify the CKA-guided advantage ($+$1.51\,pp differential), but this partial exception reinforces the main pattern: the pruning criterion, not the recovery paradigm, determines outcome (\S\ref{sec:decoupling}).
29	    \item \textbf{Recovery capacity spectrum.} We propose \rasp{}, which balances gradient importance with CKA-based representational diversity via a coefficient $\alpha$. A dose-response analysis on GSM8K reveals an inverted-U peaking at $\alpha{=}2.0$ (66.11\%). Under GRPO training, four criteria produce qualitatively distinct dynamics---from active learning to full collapse---that track preserved diversity, not gradient importance. The spectrum is validated across scales (1.5B) and, via SFT-based recovery, across architectures (Qwen2.5-Math-7B) (\S\ref{sec:scoring}, \S\ref{sec:recovery_gradient}, \S\ref{sec:extended_analysis}).
30	\end{enumerate}
31	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "27fb5ee0-f1eb-4e84-9fba-b64c7d356f2d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:intro}\n\nReasoning Large Language Models can be compressed through structured pruning, but the pruned model must recover its reasoning capabilities through fine-tuning.\nThe dominant assumption is that the recovery paradigm (SFT versus RLVR) determines recovery quality: \\citet{selfhealing2025} demonstrate that RLVR restores pruned reasoning models to near-original accuracy, significantly outperforming SFT.\nWe show that this hierarchy is an artifact of suboptimal pruning.\nWhen pruning preserves representational diversity, recovery method choice becomes irrelevant: at 20\\% sparsity, mean $|\\Delta(\\text{GRPO}-\\text{SFT})| {=} 0.54$\\,pp across the four fine-grained criteria (max $0.61$\\,pp); including dose-response variations and MBPP, the maximum is $1.34$\\,pp.\nWhat matters is not \\emph{how} you train after pruning, but \\emph{which structures} you remove.\n\nThis gap is surprising because RL and SFT impose fundamentally different demands on model representations: RL compresses incorrect paths while SFT expands correct ones~\\citep{rlsqueezes2026}. Yet existing structured pruning methods for reasoning LLMs~\\citep{graspprune2026,resp2025,llmpruner2023,bonsai2025} optimize for post-pruning quality without studying how the criterion shapes downstream RL recovery.\nNo prior work has compared multiple pruning criteria under RL or asked whether the ``RLVR $>$ SFT'' advantage persists across pruning strategies.\nWe note that \\citet{selfhealing2025} evaluate unstructured magnitude pruning retaining 96.5\\% of dense parameters; our findings concern fine-grained structural pruning where entire channel groups are removed, and the two settings may impose different demands on RL recovery.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../figures/paper/fig1_dose_response.pdf}\n\\caption{Dose-response curve for the CKA diversity coefficient $\\alpha$ at 20\\% MLP channel sparsity on GSM8K ($N{=}1{,}319$). Recovery accuracy follows an inverted-U, peaking at $\\alpha{=}2.0$ (66.11\\%). SFT and GRPO curves nearly overlap ($|\\Delta| \\leq 1.14$\\,pp at every point), visually demonstrating reward-accuracy decoupling: the pruning criterion, not the recovery paradigm, determines outcome.}\n\\label{fig:dose_response}\n\\end{figure}\n\nWe present a controlled comparison on DeepSeek-R1-Distill-Qwen-7B~\\citep{deepseek2025r1} at 20\\% MLP channel sparsity, varying the balance between gradient importance and CKA-based representational diversity~\\citep{kornblith2019cka} via a coefficient $\\alpha$ in the pruning score (Figure~\\ref{fig:dose_response}).\nThe dose-response curve reveals an inverted-U: recovery peaks at $\\alpha{=}2.0$ (66.11\\% GRPO on GSM8K~\\citep{cobbe2021gsm8k}), where importance and diversity reach optimal balance.\nUnder GRPO~\\citep{shao2024grpo} training, four criteria produce a \\textbf{recovery capacity spectrum}---from active learning (CKA-only, peak reward 4.4$\\times$ Standard) through stagnation (Random) to collapse ($\\alpha{=}1.0$)---that tracks preserved representational diversity, not gradient importance.\nA depth pruning baseline (ShortGPT;~\\citealp{shortgpt2024}) is the only method with $|\\Delta| > 1$\\,pp on GSM8K ($-$1.36\\,pp), confirming that pruning granularity interacts with RL trainability.\n\nOur contributions are:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item \\textbf{Reward-accuracy decoupling.} At 20--25\\% sparsity, GRPO and SFT produce near-identical accuracy across all four fine-grained criteria: mean $|\\Delta| {=} 0.54$\\,pp at 20\\% (max $0.61$\\,pp; $1.34$\\,pp including dose-response variations and MBPP). At 15\\%, GRPO can still amplify the CKA-guided advantage ($+$1.51\\,pp differential), but this partial exception reinforces the main pattern: the pruning criterion, not the recovery paradigm, determines outcome (\\S\\ref{sec:decoupling}).\n    \\item \\textbf{Recovery capacity spectrum.} We propose \\rasp{}, which balances gradient importance with CKA-based representational diversity via a coefficient $\\alpha$. A dose-response analysis on GSM8K reveals an inverted-U peaking at $\\alpha{=}2.0$ (66.11\\%). Under GRPO training, four criteria produce qualitatively distinct dynamics---from active learning to full collapse---that track preserved diversity, not gradient importance. The spectrum is validated across scales (1.5B) and, via SFT-based recovery, across architectures (Qwen2.5-Math-7B) (\\S\\ref{sec:scoring}, \\S\\ref{sec:recovery_gradient}, \\S\\ref{sec:extended_analysis}).\n\\end{enumerate}\n",
      "numLines": 31,
      "startLine": 1,
      "totalLines": 31
    }
  }
}
```

</details>

---


### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Read · `toolu_014jJ4z9djDcBJMoQv9V97zr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "3f8d2d67-e6c7-4207-8f5e-d62378e0b5c9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013tZUEJiGLjd4MBdX4Ssicy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12910,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12910
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

_source line 10 · 2026-05-24T04:32:24.105Z_

<details><summary>↩ Tool result · `toolu_014jJ4z9djDcBJMoQv9V97zr`</summary>

```text
1	\section{Discussion and Conclusion}
2	\label{sec:conclusion}
3	
4	The belief that RLVR is inherently superior to SFT for recovering pruned reasoning models turns out to depend on how the model was pruned.
5	Under diversity-preserving pruning, the two paradigms produce near-identical accuracy (mean $|\Delta| {=} 0.54$\,pp across four fine-grained criteria at 20\%; max $1.34$\,pp including dose-response and MBPP), yet the pruning criterion itself creates a 4.4$\times$ gap in peak reward between CKA-only and Standard---a gap that persists through 300 training steps (\S\ref{sec:extended_analysis}).
6	The dose-response across $\alpha$ identifies representational diversity as the causal driver: recovery peaks at $\alpha{=}2.0$ (66.11\%), and CKA similarity tracks the full spectrum ($\mu{=}0.62$ for CKA-only vs.\ $\mu{\geq}0.88$ for collapsing methods).
7	
8	\paragraph{Why does diversity preservation enable RL recovery?}
9	Policy gradient methods require trajectory variation to estimate reward gradients; importance-based pruning collapses the model onto the dense model's dominant reasoning mode, while CKA-only pruning preserves representationally distinct pathways that sustain exploration.
10	Gradient flow evidence supports this: CKA-only exhibits 2.89$\times$ mean gradient magnitude vs.\ Standard (\S\ref{sec:extended_analysis}), consistent with diversity preventing zero-variance batches ($f_0 > 0.5$).
11	Since RL fine-tuning updates only 5--30\% of parameters~\citep{mukherjee2025rlsubnetworks}, CKA-based pruning may preferentially preserve this active subnetwork---a recovery analogue of the Lottery Ticket Hypothesis~\citep{frankle2019lth}---though decoupling shows accuracy is paradigm-invariant.
12	
13	\paragraph{Practitioner guidelines.}
14	Use \rasp{} at $\alpha \approx 2.0$, which outperforms both pure importance (Standard) and pure diversity (CKA-only) on the dose-response curve (Figure~\ref{fig:dose_response}).
15	Under SFT alone, the criterion still matters (4.62\,pp gap; Table~\ref{tab:decoupling}).
16	Maintain per-layer floors ($\geq$40\%), stay below 25\% sparsity (\S\ref{sec:sparsity_cliff}), and monitor early-step $f_0$ as a pruning quality diagnostic.
17	
18	\paragraph{Scope and outlook.}
19	Reward-accuracy decoupling holds across all tested sparsity levels ($|\Delta| \leq 1$\,pp at 15--25\%), with initial generality evidence across scales (1.5B) and architectures (Qwen2.5-Math-7B).
20	Our findings concern fine-grained structural pruning; extension to unstructured~\citep{selfhealing2025} or online rollout pruning~\citep{xu2026arrol} remains open. Code, pruning masks, and model checkpoints will be released upon acceptance.
21	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "d64dc9d0-07d7-4ac3-97eb-44a2279ff8fe",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/conclusion.tex",
      "content": "\\section{Discussion and Conclusion}\n\\label{sec:conclusion}\n\nThe belief that RLVR is inherently superior to SFT for recovering pruned reasoning models turns out to depend on how the model was pruned.\nUnder diversity-preserving pruning, the two paradigms produce near-identical accuracy (mean $|\\Delta| {=} 0.54$\\,pp across four fine-grained criteria at 20\\%; max $1.34$\\,pp including dose-response and MBPP), yet the pruning criterion itself creates a 4.4$\\times$ gap in peak reward between CKA-only and Standard---a gap that persists through 300 training steps (\\S\\ref{sec:extended_analysis}).\nThe dose-response across $\\alpha$ identifies representational diversity as the causal driver: recovery peaks at $\\alpha{=}2.0$ (66.11\\%), and CKA similarity tracks the full spectrum ($\\mu{=}0.62$ for CKA-only vs.\\ $\\mu{\\geq}0.88$ for collapsing methods).\n\n\\paragraph{Why does diversity preservation enable RL recovery?}\nPolicy gradient methods require trajectory variation to estimate reward gradients; importance-based pruning collapses the model onto the dense model's dominant reasoning mode, while CKA-only pruning preserves representationally distinct pathways that sustain exploration.\nGradient flow evidence supports this: CKA-only exhibits 2.89$\\times$ mean gradient magnitude vs.\\ Standard (\\S\\ref{sec:extended_analysis}), consistent with diversity preventing zero-variance batches ($f_0 > 0.5$).\nSince RL fine-tuning updates only 5--30\\% of parameters~\\citep{mukherjee2025rlsubnetworks}, CKA-based pruning may preferentially preserve this active subnetwork---a recovery analogue of the Lottery Ticket Hypothesis~\\citep{frankle2019lth}---though decoupling shows accuracy is paradigm-invariant.\n\n\\paragraph{Practitioner guidelines.}\nUse \\rasp{} at $\\alpha \\approx 2.0$, which outperforms both pure importance (Standard) and pure diversity (CKA-only) on the dose-response curve (Figure~\\ref{fig:dose_response}).\nUnder SFT alone, the criterion still matters (4.62\\,pp gap; Table~\\ref{tab:decoupling}).\nMaintain per-layer floors ($\\geq$40\\%), stay below 25\\% sparsity (\\S\\ref{sec:sparsity_cliff}), and monitor early-step $f_0$ as a pruning quality diagnostic.\n\n\\paragraph{Scope and outlook.}\nReward-accuracy decoupling holds across all tested sparsity levels ($|\\Delta| \\leq 1$\\,pp at 15--25\\%), with initial generality evidence across scales (1.5B) and architectures (Qwen2.5-Math-7B).\nOur findings concern fine-grained structural pruning; extension to unstructured~\\citep{selfhealing2025} or online rollout pruning~\\citep{xu2026arrol} remains open. Code, pruning masks, and model checkpoints will be released upon acceptance.\n",
      "numLines": 21,
      "startLine": 1,
      "totalLines": 21
    }
  }
}
```

</details>

---


### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Read · `toolu_01SXVTAnZUmnvx9sgVbBYd7C`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "6cb642b1-f0fc-4538-a683-8f4345bdaff1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013tZUEJiGLjd4MBdX4Ssicy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12910,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12910
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

_source line 12 · 2026-05-24T04:32:25.039Z_

<details><summary>↩ Tool result · `toolu_01SXVTAnZUmnvx9sgVbBYd7C`</summary>

```text
1	% Limitations --- required by ACL/EMNLP
2	
3	\paragraph{Architecture and scale.}
4	Our primary results are on DeepSeek-R1-Distill-Qwen-7B~\citep{deepseek2025r1} with GQA ($G{=}7$).
5	Cross-architecture validation on Qwen2.5-Math-7B covers SFT recovery only ($N{=}200$); both models share the Qwen2.5 base architecture, so our cross-architecture evidence does not extend to different architecture families (e.g., LLaMA, Mistral).
6	Whether the spectrum generalizes across architecture families and scales (1B--70B) remains open.
7	
8	\paragraph{Diagnostic limitations.}
9	Reward-accuracy decoupling at 20--25\% sparsity means that recovery capacity---operationalized as peak reward---does not predict downstream accuracy improvements within our training horizon.
10	Recovery capacity captures the model's ability to sustain RL training without collapse, but practitioners seeking accuracy gains may require longer training, different reward formulations, or lower sparsity levels.
11	The per-layer capacity floor (40\% retention) was chosen heuristically; an ablation over $\tau \in \{0.3, 0.4, 0.5, 0.6\}$ (Appendix~\ref{sec:appendix_floor}) suggests moderate sensitivity, but a full search over continuous $\tau$ values was not performed.
12	
13	\paragraph{Replication and scope.}
14	CKA-only, Standard, and Random are validated over 3 GRPO seeds; \rasp{} uses a single seed ($N{=}1$).
15	We evaluate on three benchmarks (GSM8K, MATH-500, MBPP) covering math reasoning and code generation; logical, commonsense, and multi-modal reasoning are not addressed.
16	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "136990d6-86b8-49a9-be80-34055c066175",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/limitations.tex",
      "content": "% Limitations --- required by ACL/EMNLP\n\n\\paragraph{Architecture and scale.}\nOur primary results are on DeepSeek-R1-Distill-Qwen-7B~\\citep{deepseek2025r1} with GQA ($G{=}7$).\nCross-architecture validation on Qwen2.5-Math-7B covers SFT recovery only ($N{=}200$); both models share the Qwen2.5 base architecture, so our cross-architecture evidence does not extend to different architecture families (e.g., LLaMA, Mistral).\nWhether the spectrum generalizes across architecture families and scales (1B--70B) remains open.\n\n\\paragraph{Diagnostic limitations.}\nReward-accuracy decoupling at 20--25\\% sparsity means that recovery capacity---operationalized as peak reward---does not predict downstream accuracy improvements within our training horizon.\nRecovery capacity captures the model's ability to sustain RL training without collapse, but practitioners seeking accuracy gains may require longer training, different reward formulations, or lower sparsity levels.\nThe per-layer capacity floor (40\\% retention) was chosen heuristically; an ablation over $\\tau \\in \\{0.3, 0.4, 0.5, 0.6\\}$ (Appendix~\\ref{sec:appendix_floor}) suggests moderate sensitivity, but a full search over continuous $\\tau$ values was not performed.\n\n\\paragraph{Replication and scope.}\nCKA-only, Standard, and Random are validated over 3 GRPO seeds; \\rasp{} uses a single seed ($N{=}1$).\nWe evaluate on three benchmarks (GSM8K, MATH-500, MBPP) covering math reasoning and code generation; logical, commonsense, and multi-modal reasoning are not addressed.\n",
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

_source line 13_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01WD35KNizZEKbGpwXtxdT1d`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry",
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
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "f74ee975-3aa5-44cc-8940-91607f9423d4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013tZUEJiGLjd4MBdX4Ssicy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12910,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12910
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

_source line 14 · 2026-05-24T04:32:25.721Z_

<details><summary>↩ Tool result · `toolu_01WD35KNizZEKbGpwXtxdT1d`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_registry"
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
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "5f9104fa-9ca7-4262-9a3f-88465ab41f7a",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_registry"
    ],
    "query": "select:mcp__agent-ml-research__read_registry",
    "total_deferred_tools": 22
  }
}
```

</details>

---


### Assistant

_source line 15_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the registry to get all successful experiments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "d92e8eb2-1976-49db-8c26-bdc0920faa0d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ARv4DVfLBREEgDrZf1UFBQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3937,
      "cache_read_input_tokens": 24751,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3937
      },
      "output_tokens": 18,
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

_source line 16_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01RkNy9GadtyaG3JBd6CoqTA`</summary>

```json
{
  "project": "recovery_aware_struct_prune",
  "filters": {
    "status": "DONE",
    "conclusion": "success"
  },
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
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "d98618f1-5f14-455b-bb6d-fd739ea5b1e6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ARv4DVfLBREEgDrZf1UFBQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3937,
      "cache_read_input_tokens": 24751,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3937
      },
      "output_tokens": 18,
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

_source line 17 · 2026-05-24T04:32:32.379Z_

<details><summary>↩ Tool result · `toolu_01RkNy9GadtyaG3JBd6CoqTA`</summary>

```text
Error: result (430,814 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "a56a345b-e124-4656-8098-e457902ca1a8",
  "tool_use_result": {
    "content": "Error: result (430,814 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval_math500_sft_rasp_alpha2p0_20_fixed\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T19:48:01.183Z\", \"updated_at\": \"2026-05-24T03:10:25.471Z\", \"hypothesis\": \"SFT RASP α=2.0 20% MATH-500 with fixed eval script. Model on westd (sft_rasp_alpha2p0_20). P1 dose-response table.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha2p0_20 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_rasp_alpha2p0_20_fixed.json\\\"\", \"server\": \"westd-32935\", \"gpu\": [\"cuda:2\"], \"pid\": \"171964\", \"checkpoint_source\": \"sft_rasp_alpha2p0_20\", \"eval_data\": \"MATH-500\", \"model_name\": \"sft_rasp_alpha2p0_20\", \"seed\": 42, \"data_path\": \"MATH-500\", \"data_count\": 500}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.256, \"n_correct\": 128, \"n_total\": 500, \"stderr\": 0.01952, \"truncated\": 155, \"natural_eos\": 345, \"truncated_pct\": 0.31, \"avg_response_length\": 805.754}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha2p0_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_rasp_alpha2p0_20_fixed.json\", \"completed_at\": \"2026-05-24T03:10:25.471Z\"}, \"eval_math500_grpo_rasp_alpha2p0_20_fixed\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T22:20:57.401Z\", \"updated_at\": \"2026-05-24T02:37:29.497Z\", \"hypothesis\": \"GRPO RASP α=2.0 20% MATH-500 with fixed eval script. Model on westd (grpo_rasp_alpha2p0_20). P1 dose-response table.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha2p0_20 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_rasp_alpha2p0_20_fixed.json\\\"\", \"server\": \"westd-32935\", \"gpu\": [\"cuda:1\"], \"pid\": \"168524\", \"checkpoint_source\": \"grpo_rasp_alpha2p0_20\", \"eval_data\": \"MATH-500\", \"model_name\": \"grpo_rasp_alpha2p0_20\", \"seed\": 42, \"data_path\": \"MATH-500\", \"data_count\": 500}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_rasp_alpha2p0_20_fixed.json\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_math500_grpo_rasp_alpha2p0_20_fixed.log\", \"completed_at\": \"2026-05-24T02:36:32.046Z\", \"metrics\": {\"accuracy\": 0.274, \"n_correct\": 137, \"n_total\": 500, \"truncated_pct\": 0.302, \"truncated\": 151, \"natural_eos\": 349}}, \"eval_math500_grpo_cka_only_25_fixed\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T19:48:08.783Z\", \"updated_at\": \"2026-05-24T01:57:05.294Z\", \"hypothesis\": \"GRPO CKA-only 25% MATH-500 with fixed eval script. Model on westd (grpo_cka_only_25). P1 25% sparsity table.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_25 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_cka_only_25_fixed.json\\\"\", \"server\": \"westd-32935\", \"gpu\": [\"cuda:3\"], \"pid\": \"168451\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_25\", \"eval_data\": \"MATH-500\", \"model_name\": \"grpo_cka_only_25\", \"seed\": 42, \"data_path\": \"MATH-500\", \"data_count\": 500}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.176, \"n_correct\": 88, \"n_total\": 500, \"stderr\": 0.017, \"natural_eos\": 367, \"truncated\": 133, \"truncated_pct\": 0.266, \"avg_response_length\": 719.35}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_25\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_cka_only_25_fixed.json\", \"completed_at\": \"2026-05-24T01:53:10.148Z\"}, \"eval_math500_grpo_cka_only_20_fixed\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T15:50:01.329Z\", \"updated_at\": \"2026-05-23T23:14:58.954Z\", \"hypothesis\": \"GRPO CKA-only 20% MATH-500 with fixed eval script. Model on westb (grpo_cka_only_20/checkpoint-100). P0 method comparison.\", \"server\": \"westb-23072\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westb-23072\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-23T19:35:44.377Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20/checkpoint-100 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_cka_only_20_fixed.json --seed 42 --dtype bfloat16\\\"\", \"code_commit\": \"e6ce5f70bb3b993ba8964f0ea62d2f6001155551\", \"finished_at\": \"2026-05-23T23:11:32.857Z\", \"training_hours\": 3.6}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20/checkpoint-100 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_cka_only_20_fixed.json --seed 42 --dtype bfloat16\\\"\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:0\"], \"pid\": \"321423\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_grpo_cka_only_20_fixed.log\", \"submitted_at\": \"2026-05-23T19:35:48.851Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 13096.9, \"gpu_hours\": 3.64}, \"pid\": \"321423\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_grpo_cka_only_20_fixed.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-23T23:11:41.994371+00:00\"}]}, \"metrics\": {\"accuracy\": 0.276, \"n_correct\": 138, \"n_total\": 500, \"stderr\": 0.02}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20/checkpoint-100\", \"completed_at\": \"2026-05-23T23:14:05.791Z\"}, \"eval_math500_grpo_standard_20_fixed\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T14:42:17.751Z\", \"updated_at\": \"2026-05-23T22:12:20.152Z\", \"hypothesis\": \"GRPO Standard 20% MATH-500 with fixed eval script. Replaces OLD v2 (26.4%) with consistently-scored result across all methods.\", \"server\": \"westd-32935\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-23T15:04:01.353Z\", \"finished_at\": \"2026-05-23T22:10:17.318Z\", \"training_hours\": 7.1}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_standard_20_fair_fixed.json\\\"\", \"server\": \"westd-32935\", \"gpu\": [\"cuda:2\"], \"pid\": \"142477\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_grpo_standard_20_fixed.log\", \"submitted_at\": \"2026-05-23T15:04:04.656Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"grpo_stage2_standard_20_fair\", \"eval_data\": \"MATH-500\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair\", \"data_count\": 500, \"data_path\": \"hendrycks/MATH (500 test)\", \"seed\": 42, \"wall_clock_seconds\": 25695.5, \"gpu_hours\": 7.14}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-23T22:10:29.409278+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"math500_acc\": 0.27, \"math500_correct\": 135, \"math500_total\": 500, \"math500_stderr\": 0.0199, \"natural_eos\": 278, \"truncated\": 222, \"avg_response_length\": 1127.844}, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_grpo_standard_20_fixed.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_standard_20_fair_fixed.json\", \"completed_at\": \"2026-05-23T22:12:20.152Z\"}, \"eval_math500_grpo_rasp_alpha1p0_20_fixed\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T15:44:56.850Z\", \"updated_at\": \"2026-05-23T21:47:09.624Z\", \"hypothesis\": \"GRPO RASP α=1.0 20% MATH-500 with fixed eval script. Replaces buggy NEW result (22.6%) with consistent scoring.\", \"server\": \"westd-32935\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-23T15:45:34.279Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_rasp_alpha1p0_20_fixed.json\\\"\", \"code_commit\": \"39afb8c6309aad601973b2b3cd6b4f1a8a3b0b6c\", \"finished_at\": \"2026-05-23T21:23:51.075Z\", \"training_hours\": 5.64}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_rasp_alpha1p0_20_fixed.json\\\"\", \"server\": \"westd-32935\", \"gpu\": [\"cuda:1\"], \"pid\": \"145167\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_grpo_rasp_alpha1p0_20_fixed.log\", \"submitted_at\": \"2026-05-23T15:45:38.369Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 20452.8, \"gpu_hours\": 5.68}, \"pid\": \"145167\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_grpo_rasp_alpha1p0_20_fixed.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-23T21:24:01.803640+00:00\"}]}, \"metrics\": {\"accuracy\": 0.23, \"n_correct\": 115, \"n_total\": 500, \"stderr\": 0.0188, \"natural_eos\": 320, \"truncated\": 180, \"avg_response_length\": 903.536}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_rasp_alpha1p0_20_fixed.json\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T21:26:31.216Z\"}, \"eval_math500_sft_cka_only_20_fixed_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T15:44:55.222Z\", \"updated_at\": \"2026-05-23T19:42:45.920Z\", \"hypothesis\": \"SFT CKA-only 20% MATH-500 with fixed eval script. Retry on westb (checkpoint location). Replaces buggy NEW result (26.8%) with consistent scoring.\", \"server\": \"westb-23072\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westb-23072\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-23T15:45:16.783Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_cka_only_20_fixed.json\\\"\", \"code_commit\": \"e6ce5f70bb3b993ba8964f0ea62d2f6001155551\", \"finished_at\": \"2026-05-23T19:34:41.450Z\", \"training_hours\": 3.82}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_cka_only_20_fixed.json\\\"\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:1\"], \"pid\": \"306963\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_sft_cka_only_20_fixed_v2.log\", \"submitted_at\": \"2026-05-23T15:45:23.180Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 14242.7, \"gpu_hours\": 3.96}, \"pid\": \"306963\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_sft_cka_only_20_fixed_v2.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-23T19:34:51.495317+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.274, \"num_correct\": 137, \"num_total\": 500, \"stderr\": 0.02, \"truncated_pct\": 0.232}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_cka_only_20_fixed.json\", \"completed_at\": \"2026-05-23T19:42:45.920Z\"}, \"grpo_random_20_retrain_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T16:17:14.338Z\", \"updated_at\": \"2026-05-23T19:25:17.675Z\", \"hypothesis\": \"Retrain GRPO Random 20% from sft_random_20 (100 steps, seed 42). v1 failed: --save_only_model not supported by train_grpo_v5.py. P0 method comparison baseline.\", \"server\": \"westb-23072\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westb-23072\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-23T16:17:37.827Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_retrain --max_steps 100 --save_steps 100 --seed 42\\\"\", \"code_commit\": \"e6ce5f70bb3b993ba8964f0ea62d2f6001155551\", \"finished_at\": \"2026-05-23T19:21:35.751Z\", \"training_hours\": 3.07}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_retrain --max_steps 100 --save_steps 100 --seed 42\\\"\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:0\"], \"pid\": \"309964\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_random_20_retrain_v2.log\", \"submitted_at\": \"2026-05-23T16:17:44.194Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 11246.3, \"gpu_hours\": 3.12}, \"pid\": \"309964\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_random_20_retrain_v2.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-23T19:21:51.845739+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_retrain/model.safetensors\", \"metrics\": {\"final_reward\": 0.2875, \"final_reward_std\": 0.4291, \"final_loss\": 0.06684, \"final_kl\": 0.004236, \"final_entropy\": 0.1704, \"final_completion_length_mean\": 189.1, \"final_grad_norm\": 5.531, \"frac_reward_zero_std\": 0.4, \"wandb_run_id\": \"9c16hnf7\", \"wandb_run_name\": \"grpo_sft_random_20\", \"training_steps\": 100, \"training_time_hours\": 3.07}, \"completed_at\": \"2026-05-23T19:25:10.463Z\"}, \"eval_math500_sft_rasp_alpha1p0_20_fixed\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T14:42:23.684Z\", \"updated_at\": \"2026-05-23T18:39:04.256Z\", \"hypothesis\": \"SFT RASP α=1.0 20% MATH-500 with fixed eval script. Replaces buggy NEW result (21.2%) with consistent scoring.\", \"spec\": {\"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (sft_rasp_20_westd, α=1.0)\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"seed\": 42, \"checkpoint_source\": \"sft_rasp_20_westd\", \"eval_data\": \"MATH-500 (N=500, max_new_tokens=2048)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_rasp_alpha1p0_20_fixed.json --seed 42 --dtype bfloat16\\\"\", \"server\": \"westd-32935\", \"gpu\": \"cuda:0\", \"pid\": \"147914\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.216, \"num_correct\": 108, \"num_total\": 500}, \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_rasp_alpha1p0_20_fixed.json\", \"completed_at\": \"2026-05-23T18:39:04.256Z\"}, \"grpo_standard_25\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25_qwen_math/\", \"completed_at\": \"2026-05-16T19:37:31.250Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T08:42:41.240Z\", \"hypothesis\": \"DeepSeek-R1-Distill-Qwen-7B Standard 25% GRPO (100 steps). 25% Standard 对照，配合 grpo_rasp_25 (frac_zero=0.875)。Parent: sft_standard_25_westd.\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/grpo_standard_25_qwen_math.log\", \"metrics\": {\"clipped_ratio\": 0.92, \"collapse_pattern\": \"near_total_collapse\", \"comparison_vs_rasp_25\": \"worse_than_rasp_25(0.009)\", \"kl_final\": 0.0012, \"reward_final\": 0.0075, \"total_steps\": 100, \"wall_clock_min\": 44, \"wandb_run_id\": \"16vqw4e6\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25 --gpu 0 --max_completion_length 1024 --beta 0.04 --temperature 0.4 --repetition_penalty 1.15 --format_reward_weight 0.1 --gradient_checkpointing true --optim adamw_bnb_8bit --loss_type dapo --learning_rate 5e-7 --max_steps 100 --save_steps 100 --save_total_limit 3 --reward_desert_patience 50 --run_name grpo_standard_25 --seed 42\", \"data_count\": null, \"data_path\": \"built-in GSM8K\", \"eval_data\": \"GSM8K (built-in GRPO reward)\", \"gpu\": \"cuda:1\", \"hypothesis\": \"DeepSeek-R1-Distill-Qwen-7B Standard 25% GRPO (100 steps). 25% Standard 对照，配合 grpo_rasp_25 (frac_zero=0.875)。Parent: sft_standard_25_westd.\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (Standard 25% pruned, SFT recovered)\", \"parent\": \"sft_standard_25_westd\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-23T17:52:19.644Z\"}, \"sft_standard_25_retrain\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T15:49:44.201Z\", \"updated_at\": \"2026-05-23T17:28:50.960Z\", \"hypothesis\": \"Retrain SFT Standard 25% from pruned_standard_25 (2 epochs). Original SFT checkpoint deleted during disk cleanup. P1 — needed for 25% sparsity table. pruned_standard_25 confirmed on westd (10.8G).\", \"spec\": {\"command\": \"HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/train_sft_warmup.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_25 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25 --gpu_id 0 --num_epochs 2 --lr 2e-5 --batch_size 1 --gradient_accumulation_steps 8 --logging_steps 10\", \"server\": \"westd-32935\", \"gpu\": [\"cuda:0\"], \"pid\": \"148228\", \"model_name\": \"pruned_standard_25\", \"data_path\": \"MATH-train (SFT)\", \"data_count\": 7500, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_25\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/model.safetensors\", \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_standard_25_retrain.log\"}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.8584, \"token_accuracy\": 0.8, \"steps\": 1870, \"epochs\": 2}, \"completed_at\": \"2026-05-23T17:28:50.960Z\"}, \"floor_ablation_0p6_cka_only_20_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T12:10:30.113Z\", \"updated_at\": \"2026-05-23T16:34:08.036Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 bash scripts/run_floor_ablation.sh 0.6 0\\\"\", \"server\": \"westd-32935\", \"gpu\": \"cuda:0\", \"pid\": \"132494\", \"log_path\": \"~/runs/recovery_aware_struct_prune/floor_ablation_0p6_cka_only_20_v2.log\", \"submitted_at\": \"2026-05-23T12:10:29.192Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"data_path\": \"MATH-train (SFT) + GSM8K (eval)\", \"data_count\": 1319, \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_floor_0.6/checkpoint-100/\", \"wall_clock_seconds\": 15818.8, \"gpu_hours\": 4.39}, \"hypothesis\": \"Floor ratio ablation retry: floor=0.6, CKA-only 20% pruning. v1 GRPO completed but save_model crashed (disk full). v2 reruns after disk cleanup (168GB freed). Pipeline SKIP mechanism skips Prune+SFT, only reruns GRPO+eval.\", \"reproduce\": {\"finished_at\": \"2026-05-23T16:26:13.151Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-23T16:26:21.440127+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.6202, \"gsm8k_correct\": 818, \"gsm8k_total\": 1319, \"gsm8k_ci\": 0.0134, \"eos_rate\": 0.9803, \"avg_response_length\": 252.7, \"grpo_train_loss\": 0.006503, \"grpo_final_reward\": 0.2419}, \"completed_at\": \"2026-05-23T16:34:08.037Z\"}, \"eval_gsm8k_grpo_cka_only_20_verify\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T13:51:49.789Z\", \"updated_at\": \"2026-05-23T16:14:49.034Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20/checkpoint-100 --max_samples 1319 --max_new_tokens 4096 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_cka_only_20_verify.json\\\"\", \"server\": \"westb-23072\", \"gpu\": \"cuda:0\", \"pid\": \"300394\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_cka_only_20_verify.log\", \"submitted_at\": \"2026-05-23T13:51:48.865Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"grpo_cka_only_20\", \"data_path\": \"GSM8K\", \"data_count\": 1319, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20/checkpoint-100\", \"eval_data\": \"GSM8K\", \"wall_clock_seconds\": 8580.2, \"gpu_hours\": 2.38}, \"hypothesis\": \"Reproducibility verification of core result: CKA-only 20% GRPO GSM8K accuracy=64.39%. Independent rerun on westb (different server from original westd) to confirm the key number used in Tab 1 and Tab 2.\", \"reproduce\": {\"finished_at\": \"2026-05-23T16:11:04.114Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-23T16:11:18.625777+00:00\"}]}, \"metrics\": {\"accuracy\": 0.6406, \"n_correct\": 845, \"n_total\": 1319, \"stderr\": 0.0132, \"eos_rate\": 0.9894, \"avg_response_length\": 201.76, \"original_accuracy\": 0.6437, \"accuracy_diff_pp\": -0.31}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20/checkpoint-100\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_cka_only_20_verify.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T16:14:49.034Z\"}, \"eval_math500_sft_standard_20_2048_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T06:00:31.430Z\", \"updated_at\": \"2026-05-23T14:11:05.391Z\", \"hypothesis\": \"SFT Standard 20% MATH-500 @2048 rerun with NEW eval script. Previous 25.8% (eval_math500_sft_standard_20_2048_v2) used OLD answer extraction. Rerun ensures consistent comparison with other MATH-500 evals (all NEW version).\", \"parent\": \"eval_math500_sft_standard_20_2048_v2\", \"spec\": {\"command\": \"ghost entry - never started\", \"server\": \"westd-32935\", \"gpu\": \"cuda:1\", \"model_name\": \"sft_standard_20\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20\", \"eval_data\": \"MATH-500\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"checkpoint_path\": \"\", \"log_path\": \"\"}, \"conclusion\": \"success\", \"notes\": \"Final accuracy=23.4% (117/500) with NEW eval script. Previous premature read was 26.0% (partial file). OLD script (v2) gave 25.8%. Tab_math500 Standard SFT row should use 23.4%.\", \"completed_at\": \"2026-05-23T11:57:31.063Z\", \"metrics\": {\"math500_accuracy\": 0.234, \"math500_correct\": 117, \"math500_total\": 500}}, \"floor_ablation_0p5_cka_only_20_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T09:23:12.274Z\", \"updated_at\": \"2026-05-23T12:48:18.281Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 bash scripts/run_floor_ablation.sh 0.5 3\\\"\", \"server\": \"westd-32935\", \"gpu\": \"cuda:3\", \"pid\": \"120474\", \"log_path\": \"~/runs/recovery_aware_struct_prune/floor_ablation_0p5_cka_only_20_v2.log\", \"submitted_at\": \"2026-05-23T09:23:11.382Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"data_path\": \"MATH-train (SFT) + GSM8K (eval)\", \"data_count\": 1319, \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_floor_0.5/checkpoint-100/\", \"wall_clock_seconds\": 12306.9, \"gpu_hours\": 3.42}, \"hypothesis\": \"Floor ratio ablation (retry): floor=0.5, CKA-only 20% pruning on DeepSeek-R1-Distill-Qwen-7B. Pipeline: Prune → SFT(2ep) → GRPO(100 steps) → GSM8K eval. v1 failed during pruning save due to disk full; v2 reruns full pipeline after disk cleanup.\", \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.6171, \"gsm8k_correct\": 814, \"gsm8k_total\": 1319, \"eos_rate\": 0.992}, \"completed_at\": \"2026-05-23T12:48:18.281Z\"}, \"floor_ablation_0p3_cka_only_20_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T09:23:27.547Z\", \"updated_at\": \"2026-05-23T12:07:53.712Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 bash scripts/run_floor_ablation.sh 0.3 0\\\"\", \"server\": \"westd-32935\", \"gpu\": \"cuda:0\", \"pid\": \"120742\", \"log_path\": \"~/runs/recovery_aware_struct_prune/floor_ablation_0p3_cka_only_20_v2.log\", \"submitted_at\": \"2026-05-23T09:23:26.593Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"data_path\": \"MATH-train (SFT) + GSM8K (eval)\", \"data_count\": 1319, \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_floor_0.3/checkpoint-100/\", \"wall_clock_seconds\": 9867.1, \"gpu_hours\": 2.74}, \"hypothesis\": \"Floor ratio ablation (retry): floor=0.3, CKA-only 20% pruning on DeepSeek-R1-Distill-Qwen-7B. Pipeline: Prune → SFT(2ep) → GRPO(100 steps) → GSM8K eval. v1 failed at GRPO save due to disk full; v2 resumes from completed Prune+SFT, only reruns GRPO+eval.\", \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.6505, \"gsm8k_correct\": 858, \"gsm8k_total\": 1319}, \"completed_at\": \"2026-05-23T12:07:53.712Z\"}, \"eval_postprune_qwen_math_standard_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T11:33:21.029Z\", \"updated_at\": \"2026-05-23T11:34:40.180Z\", \"hypothesis\": \"Qwen2.5-Math-7B Standard 20% post-prune GSM8K accuracy. Baseline for comparing CKA-only vs Standard pruning before recovery training on Qwen-Math model.\", \"conclusion\": \"success\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_20_qwen_math/ --max_samples 200\", \"server\": \"westb-23072\", \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 200, \"model_name\": \"Qwen2.5-Math-7B (pruned_standard_20)\", \"seed\": 42, \"checkpoint_source\": \"pruned_standard_20_qwen_math\", \"eval_data\": \"gsm8k test N=200\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_20_qwen_math/\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/gsm8k_postprune_standard_20_qwen_math_n200.json\"}, \"completed_at\": \"2026-05-23T11:34:29.604Z\", \"metrics\": {\"accuracy\": 0.185, \"n_correct\": 37, \"n_total\": 200, \"stderr\": 0.02746, \"eos_rate\": 0.69, \"avg_response_length\": 506.83, \"note\": \"Qwen-Math Standard 20% post-prune = 18.5%. Significantly better than CKA-only (1.0%) at post-prune stage.\"}}, \"eval_postprune_qwen_math_cka_only_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T11:33:19.445Z\", \"updated_at\": \"2026-05-23T11:34:38.567Z\", \"hypothesis\": \"Qwen2.5-Math-7B CKA-only 20% post-prune GSM8K accuracy. Tests whether CKA-only pruning generalizes from DeepSeek-R1 to Qwen-Math. Low post-prune accuracy expected; key comparison is CKA-only vs Standard post-prune.\", \"conclusion\": \"success\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_cka_only_20_qwen_math/ --max_samples 200\", \"server\": \"westb-23072\", \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 200, \"model_name\": \"Qwen2.5-Math-7B (pruned_cka_only_20)\", \"seed\": 42, \"checkpoint_source\": \"pruned_cka_only_20_qwen_math\", \"eval_data\": \"gsm8k test N=200\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_cka_only_20_qwen_math/\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/gsm8k_postprune_cka_only_20_qwen_math_n200.json\"}, \"completed_at\": \"2026-05-23T11:34:26.756Z\", \"metrics\": {\"accuracy\": 0.01, \"n_correct\": 2, \"n_total\": 200, \"stderr\": 0.00704, \"eos_rate\": 0.065, \"avg_response_length\": 958.3, \"note\": \"Qwen-Math CKA-only 20% post-prune = 1.0%. Severe collapse (repetition, gibberish).\"}}, \"eval_gsm8k_grpo_depth_first_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T14:20:41.126Z\", \"updated_at\": \"2026-05-23T11:32:52.439Z\", \"hypothesis\": \"MF5 depth-first GRPO GSM8K eval re-run. Previous pipeline_depth_first_20 results lost due to disk-full during JSON write. GRPO checkpoint intact. Re-running eval to get formal JSON result file. Prior log recovery showed ~24.18% from nohup output.\", \"parent\": \"pipeline_depth_first_20\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path grpo_depth_first_20/checkpoint-100 --output_path results/eval_gsm8k_grpo_depth_first_20.json --seed 42 --dtype bfloat16\", \"server\": \"westd-32935\", \"gpu\": \"cuda:3\", \"pid\": \"51981\", \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (grpo_depth_first_20)\", \"seed\": 42, \"checkpoint_source\": \"grpo_depth_first_20/checkpoint-100\", \"eval_data\": \"gsm8k test 1319\", \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_gsm8k_grpo_depth_first_20.log\", \"note\": \"Early-stopped by Director at ~60-88 samples. Interim accuracy ~8%@50 (GRPO). Conclusive: depth-first 20% GRPO dramatically worse than CKA-only 64%. MF5 claim validated — CKA-only advantage is NOT simply removing deep layers.\", \"checkpoint_path\": \"N/A (eval only)\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T15:18:38.970Z\", \"metrics\": {\"accuracy_approx\": 0.08, \"note\": \"Early-stopped by Director at ~60-88 samples. Interim accuracy ~8%@50 (GRPO). Prior log recovery showed ~24.18% from nohup output. No JSON result file produced.\", \"early_stopped\": true, \"result_file_on_westb\": false}}, \"eval_gsm8k_sft_depth_first_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T14:20:43.950Z\", \"updated_at\": \"2026-05-23T11:32:50.632Z\", \"hypothesis\": \"MF5 depth-first SFT GSM8K eval. Establishes SFT baseline for depth-first pruning method, paired with GRPO eval to check C1 decoupling for this baseline method.\", \"parent\": \"pipeline_depth_first_20\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path sft_depth_first_20 --output_path results/eval_gsm8k_sft_depth_first_20.json --seed 42 --dtype bfloat16\", \"server\": \"westd-32935\", \"gpu\": \"cuda:2\", \"pid\": \"54882\", \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (sft_depth_first_20)\", \"seed\": 42, \"checkpoint_source\": \"sft_depth_first_20\", \"eval_data\": \"gsm8k test 1319\", \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_gsm8k_sft_depth_first_20.log\", \"note\": \"Early-stopped by Director at ~60-88 samples. Interim accuracy ~10%@50 (SFT). Conclusive: depth-first 20% SFT dramatically worse than CKA-only 64%. MF5 claim validated — CKA-only advantage is NOT simply removing deep layers.\", \"checkpoint_path\": \"N/A (eval only)\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T15:19:31.829Z\", \"metrics\": {\"accuracy_approx\": 0.1, \"note\": \"Early-stopped by Director at ~60-88 samples. Interim accuracy ~10%@50 (SFT). No JSON result file produced.\", \"early_stopped\": true, \"result_file_on_westb\": false}}, \"eval_gsm8k_grpo_random_20_seed123_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T14:22:33.753Z\", \"updated_at\": \"2026-05-23T11:32:48.936Z\", \"hypothesis\": \"MF2 seed123 v2 GSM8K eval (N=1319, greedy, max_new_tokens=2048). 配对 seed42 (50.57%) 和 seed456 (pending). 验证 C1 decoupling 跨 seed 鲁棒性。v1 因 batch_size=1 配置错误作废。\", \"parent\": \"grpo_random_20_seed123_v2\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed123_v2/checkpoint-100 --output_path results/eval_gsm8k_grpo_random_20_seed123_v2.json --seed 123 --dtype bfloat16\", \"server\": \"westd-32935\", \"gpu\": \"cuda:0\", \"pid\": \"56283\", \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (grpo_random_20_seed123_v2)\", \"seed\": 123, \"checkpoint_source\": \"grpo_random_20_seed123_v2/checkpoint-100\", \"eval_data\": \"gsm8k test 1319\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_random_20_seed123_v2.json\", \"accuracy\": 0.5072, \"total_correct\": 669, \"total_samples\": 1319, \"eos_rate\": 0.9939, \"stderr\": 0.01377, \"avg_response_length\": 177.9, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed123_v2/checkpoint-100\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T16:49:54.123Z\", \"metrics\": {\"accuracy\": 0.5072, \"n_correct\": 669, \"n_total\": 1319, \"stderr\": 0.01377, \"eos_rate\": 0.9939, \"avg_response_length\": 177.9}}, \"eval_math500_grpo_random_20_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T22:24:42.604Z\", \"updated_at\": \"2026-05-23T11:01:52.883Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20/checkpoint-100 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_random_20_v2.json --seed 42 --dtype bfloat16 --max_new_tokens 2048\", \"server\": \"westd-32935\", \"gpu\": \"cuda:2\", \"data_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_random_20_v2.json\", \"data_count\": 500, \"model_name\": \"grpo_random_20/checkpoint-100\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20/checkpoint-100\", \"eval_data\": \"MATH-500\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_random_20_v2.json\", \"log_path\": \"/tmp/eval_math500_grpo_random_20_v3.log\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.134, \"correct\": 67, \"total\": 500, \"stderr\": 0.0152, \"natural_eos\": 167, \"truncated\": 333, \"avg_response_length\": 1479.2}, \"hypothesis\": \"GRPO training on randomly pruned 20% model recovers math reasoning ability measurably above untrained pruned baseline on MATH-500\", \"completed_at\": \"2026-05-23T11:01:52.883Z\"}, \"eval_math500_sft_qwen_math_cka_only_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T23:11:09.017Z\", \"updated_at\": \"2026-05-23T10:44:00.535Z\", \"hypothesis\": \"Qwen2.5-Math-7B CKA-only 20% SFT MATH-500 eval @2048. Cross-architecture validation: if CKA-only criterion generalizes from DeepSeek-R1-Distill to Qwen-Math on MATH-500. SFT GSM8K = 51.5% (N=200). Paired with westb:1 GRPO GSM8K for C1 decoupling cross-arch.\", \"parent\": \"sft_qwen_math_cka_only_20\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_cka_only_20_final --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_qwen_math_cka_only_20.json --seed 42 --dtype bfloat16 --max_new_tokens 2048\", \"server\": \"westb-23072\", \"gpu\": \"cuda:0\", \"data_path\": \"HuggingFaceH4/MATH-500\", \"data_count\": 500, \"model_name\": \"Qwen2.5-Math-7B-CKA-only-20%-SFT-ep1\", \"seed\": 42, \"checkpoint_source\": \"sft_qwen_math_cka_only_20_final\", \"eval_data\": \"MATH-500 (N=500, max_new_tokens=2048)\", \"pid\": 250766, \"log_path\": \"/tmp/eval_math500_sft_qwen_cka_only_20.log\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.216, \"stderr\": 0.0184, \"correct\": 108, \"total\": 500, \"natural_eos\": 90, \"truncated\": 410, \"avg_response_length\": 1745.338}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_qwen_math_cka_only_20.json\", \"completed_at\": \"2026-05-23T10:44:00.535Z\"}, \"eval_math500_grpo_rasp_alpha0p5_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T02:59:15.985Z\", \"updated_at\": \"2026-05-23T10:11:11.002Z\", \"hypothesis\": \"GRPO RASP α=0.5 MATH-500 eval @2048. C1 decoupling on MATH-500: SFT α=0.5 = 25.4%. GSM8K GRPO α=0.5 = 61.18%. Completes MATH-500 GRPO dose-response curve.\", \"parent\": \"eval_gsm8k_grpo_alpha0p5_20\", \"spec\": {\"command\": \"python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha0p5_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_rasp_alpha0p5_20.json --seed 42 --dtype bfloat16 --max_new_tokens 2048\", \"server\": \"westb-23072\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"grpo_rasp_alpha0p5_20\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha0p5_20\", \"eval_data\": \"MATH-500\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.248, \"stderr\": 0.0193, \"correct\": 124, \"total\": 500, \"natural_eos\": 274, \"truncated\": 226, \"avg_response_length\": 1110.462}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_rasp_alpha0p5_20.json\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_rasp_alpha0p5_20.log\", \"completed_at\": \"2026-05-23T10:11:11.002Z\"}, \"eval_math500_grpo_cka_only_20_2048_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T05:07:09.002Z\", \"updated_at\": \"2026-05-23T08:55:58.278Z\", \"hypothesis\": \"GRPO CKA-only 20% MATH-500 @2048 rerun with NEW eval script. Previous 29.2% (eval_math500_grpo_cka_only_20_2048) used OLD answer extraction. SFT CKA-only = 26.8% (NEW). Rerun ensures consistent C1 |Δ| comparison.\", \"parent\": \"eval_math500_grpo_cka_only_20_2048\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=3 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20/checkpoint-100 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_cka_only_20_2048_v2.json --seed 42 --dtype bfloat16 --max_new_tokens 2048'\", \"server\": \"westd-32935\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"grpo_cka_only_20/checkpoint-100\", \"seed\": 42, \"checkpoint_source\": \"westb-23072:/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20/checkpoint-100\", \"eval_data\": \"MATH-500\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.274, \"correct\": 137, \"total\": 500, \"stderr\": 0.01995, \"natural_eos\": 390, \"truncated\": 110, \"avg_response_length\": 654.746}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_cka_only_20_2048_v2.json\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_math500_grpo_cka_only_20_2048_v2.log\", \"completed_at\": \"2026-05-23T08:55:58.278Z\"}, \"eval_math500_grpo_rasp_alpha3p0_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T03:19:40.950Z\", \"updated_at\": \"2026-05-23T07:48:57.618Z\", \"hypothesis\": \"GRPO RASP α=3.0 MATH-500 eval @2048. C1 decoupling on MATH-500: SFT α=3.0 = 23.2%. GSM8K GRPO α=3.0 = 63.45%. Completes MATH-500 GRPO dose-response curve for α=3.0 data point.\", \"parent\": \"eval_gsm8k_grpo_alpha3p0_20\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20_v2/checkpoint-100 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_rasp_alpha3p0_20.json --seed 42 --dtype bfloat16 --max_new_tokens 2048\\\"\", \"server\": \"westd-32935\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"grpo_rasp_alpha3p0_20_v2/checkpoint-100\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20_v2/checkpoint-100\", \"eval_data\": \"MATH-500\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_rasp_alpha3p0_20.json\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_math500_grpo_alpha3p0_20.log\", \"completed_at\": \"2026-05-23T07:48:50.736Z\", \"metrics\": {\"accuracy\": 0.228, \"correct\": 114, \"total\": 500, \"stderr\": 0.0188, \"truncated_ratio\": 0.28, \"avg_response_length\": 745.038}}, \"eval_math500_grpo_rasp_alpha4p0_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T00:01:54.194Z\", \"updated_at\": \"2026-05-23T05:58:52.769Z\", \"hypothesis\": \"GRPO RASP α=4.0 MATH-500 eval @2048. C1 decoupling on MATH-500: SFT α=4.0 = 26.6%. If |GRPO - SFT| < 2pp, C1 decoupling holds cross-benchmark for α=4.0. GSM8K GRPO α=4.0 = 62.77%.\", \"parent\": \"eval_gsm8k_grpo_alpha4_20_v3\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_alpha4_20/checkpoint-100\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_math500_grpo_rasp_alpha4p0_20.log\"}, \"metrics\": {\"accuracy\": 0.262, \"stderr\": 0.01966, \"correct\": 131, \"total\": 500, \"truncated\": 180, \"natural_eos\": 320, \"avg_response_length\": 925.48}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T05:58:52.769Z\"}, \"eval_math500_grpo_rasp_alpha1p0_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T23:02:44.335Z\", \"updated_at\": \"2026-05-23T04:44:32.303Z\", \"hypothesis\": \"GRPO RASP α=1.0 MATH-500 eval @2048. C1 decoupling on MATH-500: SFT α=1.0 = 21.2%. If |GRPO - SFT| < 2pp, C1 decoupling holds cross-benchmark for α=1.0.\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_grpo_rasp_alpha1p0_20.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-23T04:41:44.783Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-23T04:41:56.794961+00:00\"}]}, \"metrics\": {\"accuracy\": 0.226, \"stderr\": 0.0187, \"n_correct\": 113, \"n_total\": 500, \"avg_response_length\": 903.536, \"natural_eos\": 320, \"truncated\": 180}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T04:44:32.303Z\"}, \"eval_math500_sft_cka_only_20_westd\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T20:45:21.526Z\", \"updated_at\": \"2026-05-23T03:21:26.164Z\", \"hypothesis\": \"CKA-only 20% SFT MATH-500 eval @2048 on westd (migrated from westb for speed). Dose-response endpoint control: CKA-only is the best-performing pruning method (GSM8K 64.37%). MATH-500 result establishes upper bound for cross-benchmark dose-response curve.\", \"parent\": \"eval_math500_sft_cka_only_20_westb\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 --output_path results/eval_math500_sft_cka_only_20.json --seed 42 --dtype bfloat16 --max_new_tokens 2048\", \"server\": \"westd-32935\", \"gpu\": \"cuda:1\", \"pid\": \"75284\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (sft_cka_only_20)\", \"seed\": 42, \"checkpoint_source\": \"sft_cka_only_20\", \"eval_data\": \"MATH-500 (N=500, max_new_tokens=2048)\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_math500_sft_cka_only_20.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20\"}, \"metrics\": {\"accuracy\": 0.268, \"correct\": 134, \"total\": 500, \"truncated\": 116, \"stderr\": 0.0198, \"natural_eos_pct\": 0.768, \"avg_response_length\": 673.278, \"note\": \"PID 75284 actual output = 26.8% (134/500). Previous 29.0% (145/500) was from v4 run (May 19) with different answer extraction. Same model generations, different scoring.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T00:00:43.009Z\"}, \"eval_math500_grpo_rasp_alpha2p0_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T22:23:27.589Z\", \"updated_at\": \"2026-05-23T03:16:40.537Z\", \"hypothesis\": \"GRPO RASP α=2.0 MATH-500 eval @2048. C1 decoupling evidence on MATH-500: SFT α=2.0 = 24.0%, GRPO expected similar (~24%). If |GRPO - SFT| < 1pp, C1 decoupling holds cross-benchmark.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha2p0_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_rasp_alpha2p0_20.json --seed 42 --dtype bfloat16 --max_new_tokens 2048\\\"\", \"server\": \"westd-32935\", \"gpu\": \"cuda:0\", \"pid\": \"83709\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_grpo_rasp_alpha2p0_20.log\", \"submitted_at\": \"2026-05-22T22:25:27.490Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (grpo_rasp_alpha2p0_20)\", \"seed\": 42, \"checkpoint_source\": \"grpo_rasp_alpha2p0_20\", \"eval_data\": \"MATH-500 (N=500, max_new_tokens=2048)\", \"wall_clock_seconds\": 17473.0, \"gpu_hours\": 4.85}, \"reproduce\": {\"finished_at\": \"2026-05-23T03:14:21.897Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-23T03:14:37.164633+00:00\"}]}, \"metrics\": {\"accuracy\": 0.262, \"correct\": 131, \"total\": 500, \"stderr\": 0.0197, \"natural_eos\": 349, \"truncated\": 151, \"avg_response_length\": 785.326}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha2p0_20\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_grpo_rasp_alpha2p0_20.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T03:16:40.537Z\"}, \"eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T15:12:46.181Z\", \"updated_at\": \"2026-05-23T02:53:37.071Z\", \"hypothesis\": \"MF3 cross-architecture validation v3 (N=500, max_new_tokens=2048): Qwen2.5-Math-7B CKA-only 20% GRPO GSM8K eval with absolute model_path fix. v2 crashed due to relative path OSError. v1 killed due to 337s/sample (no token limit). Tests whether CKA-only pruning + GRPO recovery generalizes beyond DeepSeek-R1-Distill to Qwen-Math architecture.\", \"parent\": \"eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v2\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/recovery_aware_struct_prune && python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_qwen_math_cka_only_20 --max_samples 500 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v3.json'\", \"server\": \"westb-23072\", \"gpu\": \"cuda:1\", \"pid\": \"220343\", \"data_path\": \"GSM8K test split\", \"data_count\": 500, \"model_name\": \"Qwen2.5-Math-7B-pruned-cka_only-20pct-GRPO\", \"seed\": 42, \"checkpoint_source\": \"grpo_qwen_math_cka_only_20\", \"eval_data\": \"GSM8K\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_qwen_math_cka_only_20\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v3.log\"}, \"metrics\": {\"accuracy\": 0.486, \"correct\": 243, \"total\": 500, \"stderr\": 0.0224, \"truncated_pct\": 0.838, \"natural_eos_pct\": 0.162, \"avg_response_length\": 1766.5}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T02:53:37.071Z\"}, \"eval_math500_sft_rasp_alpha1p0_20_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T20:50:24.239Z\", \"updated_at\": \"2026-05-22T23:01:03.419Z\", \"hypothesis\": \"α=1.0 SFT MATH-500 eval @2048 v2 (on westb). Default RASP α=1.0. Cross-benchmark dose-response: GSM8K α=1.0 SFT=63.31%. v1 killed at 304/500, result file never written. Completes 5-point dose-response curve on MATH-500.\", \"parent\": \"eval_math500_sft_rasp_alpha1p0_20\", \"notes\": \"westb submission failed: model sft_rasp_20_westd not found on westb. Only exists on westd-32935. Waiting for westd:3 (α=4.0, 85%) to free up.\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_math500_sft_rasp_alpha1p0_20_v2.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T22:58:10.208Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T22:58:19.219921+00:00\"}]}, \"metrics\": {\"accuracy\": 0.212, \"correct\": 106, \"total\": 500, \"truncated\": 186, \"stderr\": 0.0183}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T23:01:03.420Z\"}, \"eval_math500_sft_standard_20_2048_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T01:34:44.782Z\", \"updated_at\": \"2026-05-22T22:19:38.080Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_standard_20_2048_v2.json --seed 42 --dtype bfloat16 --max_new_tokens 2048\\\"\", \"server\": \"westd-32935\", \"gpu\": [\"cuda:0\"], \"pid\": \"82301\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_sft_standard_20_2048_v2.log\", \"submitted_at\": \"2026-05-22T22:15:58.026Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"Standard (random) 20% SFT MATH-500 eval @2048. Baseline comparison: Standard pruning without CKA guidance. Cross-benchmark extension of GSM8K Standard results.\", \"parent\": \"eval_math500_sft_standard_20\", \"reproduce\": {\"finished_at\": \"2026-05-19T08:54:35.352Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T08:54:40.855817+00:00\"}]}, \"metrics\": {\"accuracy\": 0.258, \"n_correct\": 129, \"n_total\": 500}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T13:08:16.850Z\"}, \"eval_math500_sft_rasp_alpha0p5_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T15:20:44.460Z\", \"updated_at\": \"2026-05-22T22:18:43.350Z\", \"hypothesis\": \"α=0.5 SFT MATH-500 eval @2048. Cross-benchmark dose-response validation: GSM8K shows α=0.5 SFT=60.73%. If MATH-500 also shows α=0.5 < α=2.0, inverted-U generalizes beyond GSM8K (strengthens MF4 + N1).\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha0p5_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_math500_sft_rasp_alpha0p5_20.log\"}, \"metrics\": {\"accuracy\": 0.254, \"correct\": 127, \"total\": 500, \"truncated\": 220, \"stderr\": 0.0195}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T22:18:43.350Z\"}, \"eval_math500_sft_rasp_alpha3p0_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T18:26:16.273Z\", \"updated_at\": \"2026-05-22T22:12:26.406Z\", \"hypothesis\": \"α=3.0 SFT MATH-500 eval @2048. Dose-response \\\"下降段确认点\\\": GSM8K α=3.0 SFT=64.14% (below α=2.0 peak 64.97%). If MATH-500 also shows α=3.0 < α=2.0, confirms inverted-U descending arm cross-benchmark. Completes 5/5 MATH-500 dose-response.\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha3p0_20/checkpoint-935\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_math500_sft_rasp_alpha3p0_20.log\"}, \"metrics\": {\"accuracy\": 0.232, \"correct\": 116, \"total\": 500, \"truncated\": 144, \"stderr\": 0.0189}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T22:12:26.406Z\"}, \"eval_math500_sft_rasp_alpha4p0_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T15:20:47.150Z\", \"updated_at\": \"2026-05-22T21:22:35.441Z\", \"hypothesis\": \"α=4.0 SFT MATH-500 eval @2048. Cross-benchmark dose-response validation: GSM8K shows α=4.0 SFT=61.94%. If MATH-500 also shows α=4.0 < α=2.0, inverted-U generalizes beyond GSM8K (strengthens MF4 + N1).\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_alpha4_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_math500_sft_rasp_alpha4p0_20.log\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.266, \"correct\": 133, \"total\": 500, \"truncated\": 190, \"stderr\": 0.0198}, \"completed_at\": \"2026-05-22T21:22:35.442Z\"}, \"eval_math500_sft_rasp_alpha2p0_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T15:06:22.386Z\", \"updated_at\": \"2026-05-22T20:44:52.970Z\", \"hypothesis\": \"α=2.0 SFT MATH-500 eval @2048. Dose-response peak on GSM8K (64.97% SFT). Cross-benchmark validation: if α=2.0 also peaks on MATH-500, inverted-U generalizes beyond GSM8K (strengthens MF4 + N1).\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha2p0_20 --output_path results/eval_math500_sft_rasp_alpha2p0_20.json --seed 42 --dtype bfloat16 --max_new_tokens 2048\", \"server\": \"westd-32935\", \"gpu\": \"cuda:1\", \"pid\": \"57202\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (sft_rasp_alpha2p0_20)\", \"seed\": 42, \"checkpoint_source\": \"sft_rasp_alpha2p0_20\", \"eval_data\": \"MATH-500 (N=500, max_new_tokens=2048)\", \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_math500_sft_rasp_alpha2p0_20.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha2p0_20\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T20:12:27.595Z\"}, \"failure_reason\": \"cron false positive: process exited normally, result file confirmed by Reviewer (24.0% accuracy)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T20:12:32.633Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T20:12:40.230344+00:00\"}]}, \"metrics\": {\"accuracy\": 0.24, \"correct\": 120, \"total\": 500, \"truncated\": 155, \"stderr\": 0.0191}}, \"eval_gsm8k_grpo_random_20_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T16:26:01.516Z\", \"updated_at\": \"2026-05-22T18:27:22.282Z\", \"hypothesis\": \"MF2 seed456 GSM8K eval (N=1319, greedy, max_new_tokens=2048). Paired with seed42 (50.57%) and seed123 v2 (running, interim 52.40%@1000). Validates C1 decoupling robustness across random seeds.\", \"parent\": \"grpo_random_20_seed456\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed456/checkpoint-100 --seed 456 --dtype bfloat16 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_random_20_seed456.json\", \"server\": \"westb-23072\", \"gpu\": \"cuda:0\", \"pid\": \"224705\", \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (grpo_random_20_seed456)\", \"seed\": 456, \"checkpoint_source\": \"grpo_random_20_seed456/checkpoint-100\", \"eval_data\": \"GSM8K test 1319\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_random_20_seed456.log\", \"accuracy\": 0.5087, \"total_correct\": 671, \"total_samples\": 1319, \"eos_rate\": 0.9955, \"stderr\": 0.01377, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed456/checkpoint-100\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T17:48:12.480Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T17:48:17.521Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T17:48:25.193120+00:00\"}]}, \"metrics\": {\"gsm8k_accuracy\": 0.5087, \"gsm8k_accuracy_se\": 0.0138, \"gsm8k_correct\": 671, \"gsm8k_total\": 1319, \"eos_rate\": 0.9954, \"avg_response_length\": 163.5, \"truncated\": 6}, \"notes\": \"Cron 误判 (已知模式): 实验实际完成 1319/1319, acc=50.87%. 与 seed42 (50.57%) 一致, 验证 C1 decoupling. Results: /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_random_20_seed456.json\"}, \"grpo_random_20_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T12:00:38.940Z\", \"updated_at\": \"2026-05-22T16:27:46.810Z\", \"hypothesis\": \"MF2 multi-seed validation: Random pruning 20% GRPO with seed456. Third seed for C1 decoupling robustness check. seed42: Δ=-0.68pp, seed123: pending eval. If all seeds show |Δ(GRPO-SFT)| ≤ 2pp, C1 claim is robust across random seeds.\", \"spec\": {\"server\": \"westb-23072\", \"gpu\": \"cuda:0\", \"command\": \"CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 nohup python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed456 --max_steps 100 --save_steps 100 --seed 456\", \"pid\": \"209508\", \"data_path\": \"openai/gsm8k (train split)\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (sft_random_20)\", \"seed\": 456, \"checkpoint_source\": \"sft_random_20\", \"eval_data\": \"N/A - GRPO training\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed456/checkpoint-100\", \"log_path\": \"/tmp/grpo_random_seed456.log\", \"note\": \"100/100 steps completed. Final trainer.save_model() hit disk-full but TRL checkpoint-100 is intact (model.safetensors=12,174,631,264 bytes, matching seed42/seed123_v2). Reviewer independently verified.\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T16:22:39.316Z\"}, \"failure_reason\": \"磁盘满: GRPO训练100/100完成但save_pretrained失败 (No space left on device)。westb-23072:/root/autodl-tmp 空间不足。\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T16:22:44.289Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T16:22:54.301751+00:00\"}]}, \"notes\": \"失败原因: GRPO 训练 100/100 步已完成 (3h02min)，但 save_pretrained 时磁盘满 (No space left on device, os error 28)。保存路径: /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed456。W&B run auv9riek 有完整训练 metrics。save_steps=100=max_steps，无中间 checkpoint，需重跑。 | 已有成果: W&B metrics 完整 | 建议: 清理 westb-23072 磁盘后重提交\"}, \"grpo_random_20_seed123_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T14:22:29.868Z\", \"updated_at\": \"2026-05-22T15:00:23.101Z\", \"hypothesis\": \"MF2 multi-seed validation v2: Random 20% GRPO with seed123, correct batch_size=2 (matching seed42/seed456). v1 used batch_size=1 (half data per 100 steps), results invalidated. Tests C1 decoupling robustness across random seeds.\", \"parent\": \"grpo_random_20_seed123\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 nohup python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed123_v2 --max_steps 100 --save_steps 100 --seed 123\", \"server\": \"westd-32935\", \"gpu\": \"cuda:1\", \"pid\": \"53822\", \"data_path\": \"openai/gsm8k (train split)\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (sft_random_20)\", \"seed\": 123, \"checkpoint_source\": \"sft_random_20\", \"eval_data\": \"N/A - GRPO training\", \"log_path\": \"/tmp/grpo_random_seed123_v2.log\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed123_v2/checkpoint-100\", \"completed_at\": \"2026-05-22T15:00:23.101Z\"}, \"eval_gsm8k_grpo_alpha3p0_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T09:30:06.630Z\", \"updated_at\": \"2026-05-22T14:47:06.188Z\", \"hypothesis\": \"α=3.0 GRPO GSM8K eval. Dose-response 5th data point: α=3.0 between α=2.0 (66.11%) and α=4.0 (62.77%). Completes the 5-point dose-response curve for causal evidence of CKA overlap suppression effect.\", \"notes\": \"UNBLOCKED: grpo_rasp_alpha3p0_20_v2 checkpoint-100 完整 (12.3GB). Eval 已启动 PID 43755 on westd:0, 2.8s/sample, ETA ~60 min.\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:0\", \"command\": \"CUDA_VISIBLE_DEVICES=0 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20_v2/checkpoint-100 --output_path results/eval_gsm8k_grpo_rasp_alpha3p0_20.json --max_samples 1319 --seed 42 --dtype bfloat16\", \"pid\": \"43755\", \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (grpo_rasp_alpha3p0_20_v2)\", \"seed\": 42, \"checkpoint_source\": \"grpo_rasp_alpha3p0_20_v2/checkpoint-100\", \"eval_data\": \"gsm8k test 1319\", \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_gsm8k_grpo_rasp_alpha3p0_20.log\"}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.6345, \"correct\": 837, \"total\": 1319, \"stderr\": 0.0133, \"eos_rate\": 0.9864, \"truncated\": 18, \"avg_response_length\": 219.7}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20_v2/checkpoint-100\", \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_gsm8k_grpo_rasp_alpha3p0_20.log\", \"completed_at\": \"2026-05-22T14:46:15.365Z\"}, \"eval_math500_sft_random_20_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T04:11:52.462Z\", \"updated_at\": \"2026-05-22T14:10:18.359Z\", \"hypothesis\": \"Random 20% SFT MATH-500 @2048. v2 failed due to old eval_math500.py on westd-32935. Code synced from westb.\", \"parent\": \"eval_math500_sft_random_20_v2\", \"spec\": {\"command\": \"python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20 --max_new_tokens 2048 --output_path /root/recovery_aware_struct_prune/results/eval_math500_sft_random_20_v3.json\", \"server\": \"westd-32935\", \"gpu\": [\"cuda:1\"], \"pid\": \"5236\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"sft_random_20\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_random_20\", \"seed\": 42, \"checkpoint_source\": \"sft_random_20\", \"eval_data\": \"MATH-500\", \"log_path\": \"/root/recovery_aware_struct_prune/logs/eval_math500_sft_random_20_v3.log\", \"checkpoint_path\": \"N/A - eval\"}, \"metrics\": {\"accuracy\": 0.144, \"correct\": 72, \"total\": 500, \"stderr\": 0.0157, \"natural_eos\": 171, \"truncated\": 329, \"avg_response_length\": 1470.44}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T14:10:18.359Z\"}, \"eval_gsm8k_sft_alpha3p0_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T10:24:58.696Z\", \"updated_at\": \"2026-05-22T12:38:25.600Z\", \"hypothesis\": \"α=3.0 SFT GSM8K eval (checkpoint-935, 1 epoch). Dose-response 5th SFT data point for C1 decoupling. Paired with α=3.0 GRPO (pending). Completes the 5-point dose-response SFT column.\", \"parent\": \"grpo_rasp_alpha3p0_20\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:2\", \"command\": \"eval_gsm8k.py --model_path sft_rasp_alpha3p0_20/checkpoint-935 --max_new_tokens 2048\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"checkpoint_source\": \"sft_rasp_alpha3p0_20/checkpoint-935 (SCP from westb)\", \"eval_data\": \"gsm8k test 1319\", \"pid\": \"37024\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T12:34:57.027Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T12:35:05.634Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T12:35:15.663664+00:00\"}]}, \"metrics\": {\"gsm8k_accuracy\": 0.6414, \"gsm8k_correct\": 846, \"gsm8k_total\": 1319, \"gsm8k_stderr\": 0.0132, \"eos_rate\": 0.9879, \"avg_response_length\": 188.63, \"natural_eos\": 1303, \"truncated\": 16}, \"log_path\": \"/tmp/eval_gsm8k_sft_alpha3p0.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha3p0_20/checkpoint-935\", \"notes\": \"Cron 误判。评估 1319/1319 全部完成，accuracy=64.14%。进程因写结果 JSON 时磁盘满 (OSError: No space left on device) 以非零码退出，但所有推理已完成、accuracy 已计算。结果 JSON 未写入磁盘，数据从日志提取。中间进度 ~64.15%@1300 与最终 64.14% 一致。\"}, \"grpo_rasp_alpha3p0_20_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T10:40:19.362Z\", \"updated_at\": \"2026-05-22T11:58:15.586Z\", \"hypothesis\": \"Re-run of grpo_rasp_alpha3p0_20 (checkpoint corrupted by disk-full). α=3.0 GRPO 100 steps on sft_rasp_alpha3p0_20/checkpoint-935. Critical for dose-response curve (α=3.0 between α=2.0 peak and α=4.0 decline).\", \"parent\": \"grpo_rasp_alpha3p0_20\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:0\", \"command\": \"CUDA_VISIBLE_DEVICES=0 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha3p0_20/checkpoint-935 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20_v2 --max_steps 100 --save_total_limit 1\", \"pid\": \"42003\", \"data_path\": \"openai/gsm8k (train split)\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (sft_rasp_alpha3p0_20)\", \"seed\": 42, \"checkpoint_source\": \"sft_rasp_alpha3p0_20/checkpoint-935\", \"eval_data\": \"N/A - GRPO training\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20_v2\", \"log_path\": \"/tmp/grpo_alpha3p0_v2.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T11:58:15.586Z\"}, \"eval_math500_grpo_standard_20_fair_2048_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T03:49:45.575Z\", \"updated_at\": \"2026-05-22T11:17:52.493Z\", \"hypothesis\": \"Standard 20% fair GRPO MATH-500 @2048. P0 data gap for cross-method MATH-500 table. Re-run on westd-32935 after westd-29022 outage.\", \"parent\": \"eval_math500_grpo_standard_20_fair_2048\", \"spec\": {\"command\": \"python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair --max_new_tokens 2048 --output_path /root/recovery_aware_struct_prune/results/eval_math500_grpo_standard_20_fair_2048_v2.json\", \"server\": \"westd-32935\", \"gpu\": [\"cuda:0\"], \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"grpo_stage2_standard_20_fair\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair\", \"seed\": 42, \"checkpoint_source\": \"grpo_stage2_standard_20_fair\", \"eval_data\": \"MATH-500\", \"log_path\": \"/root/recovery_aware_struct_prune/logs/eval_math500_grpo_standard_20_fair_2048_v2.log\", \"checkpoint_path\": \"N/A (eval)\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T11:12:19.798Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T11:12:27.767Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T11:12:38.330160+00:00\"}]}, \"metrics\": {\"math500_accuracy\": 0.264, \"math500_correct\": 132, \"math500_total\": 500, \"math500_stderr\": 0.0197}, \"notes\": \"Cron 误判。实际正常完成。MATH-500 Accuracy = 0.2640 ± 0.0197 (132/500)。运行时长 ~7h11min。结果文件: /root/recovery_aware_struct_prune/results/eval_math500_grpo_standard_20_fair_2048_v2.json\"}, \"grpo_random_20_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T10:34:12.100Z\", \"updated_at\": \"2026-05-22T11:17:21.388Z\", \"hypothesis\": \"MF2 multi-seed validation: Random pruning 20% GRPO with seed123. Tests if GRPO decoupling result (C1) is robust across random seeds. If variance across seeds is low (±2pp), C1 claim is strengthened.\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:2\", \"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed123 --num_steps 100 --seed 123'\", \"pid\": \"36832\", \"data_path\": \"openai/gsm8k (train split)\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (sft_random_20)\", \"seed\": 123, \"checkpoint_source\": \"sft_random_20\", \"eval_data\": \"N/A - GRPO training, not eval\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed123\", \"log_path\": \"/tmp/mf2_random_seed123_grpo.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T11:12:49.435Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T11:12:57.919Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T11:13:16.493425+00:00\"}]}, \"notes\": \"Cron 误判 (已知 pattern: process dead 5× with no sentinel/W&B)。实际 GRPO 训练正常完成 (19:02 CST)。模型保存: /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed123。WandB run: grpo_sft_random_20 (ID: 1silchcm)。日志: /tmp/mf2_random_seed123_grpo.log\"}, \"grpo_rasp_alpha3p0_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T08:48:06.001Z\", \"updated_at\": \"2026-05-22T10:39:07.034Z\", \"hypothesis\": \"α=3.0 GRPO 100 steps on checkpoint-935 (1 epoch SFT). Dose-response data point between α=2.0 and α=4.0. If monotonic: higher α → higher GSM8K accuracy, confirming CKA overlap suppression causally harms recovery.\", \"parent\": \"grpo_alpha4_20\", \"spec\": {\"server\": \"westb-23072\", \"gpu\": \"cuda:0\", \"command\": \"train_grpo_v5.py --model_path sft_rasp_alpha3p0_20/checkpoint-935 --output_dir grpo_rasp_alpha3p0_20 --max_steps 100 --learning_rate 1e-6 --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --max_completion_length 512 --temperature 0.4 --beta 0.01 --loss_type dapo --format_reward_weight 0.1 --gradient_checkpointing true --optim adamw_8bit\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"pid\": \"170676\", \"data_path\": \"openai/gsm8k (train split)\", \"data_count\": 7473, \"checkpoint_source\": \"sft_rasp_alpha3p0_20/checkpoint-935\", \"eval_data\": \"N/A - GRPO training\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20/checkpoint-100\", \"log_path\": \"/tmp/alpha3p0_grpo.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T10:31:57.909Z\", \"notes\": \"GRPO 训练 100/100 steps 完成，但 checkpoint-100/model.safetensors 被截断（7.2GB vs 应有 11.5GB）。原因：westb 数据盘在保存时 100% 满。需要重跑 GRPO。SFT checkpoint-935 完好（11.5GB）。\"}, \"eval_gsm8k_sft_alpha2p0_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T10:19:50.623Z\", \"updated_at\": \"2026-05-22T10:22:56.503Z\", \"hypothesis\": \"α=2.0 SFT GSM8K eval for C1 decoupling. Paired with α=2.0 GRPO (66.11%). Critical: if SFT ~61-62%, Δ ≈ +4-5pp would break C1 universal ±2pp claim. Reviewer-flagged risk.\", \"parent\": \"pipeline_alpha2p0_20\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:2\", \"command\": \"eval_gsm8k.py --model_path sft_rasp_alpha2p0_20 --max_new_tokens 2048\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"checkpoint_source\": \"sft_rasp_alpha2p0_20\", \"eval_data\": \"gsm8k test 1319\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha2p0_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/eval_gsm8k_sft_alpha2p0_20.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T10:22:49.360Z\", \"metrics\": {\"gsm8k_accuracy\": 0.6497, \"gsm8k_correct\": 857, \"gsm8k_total\": 1319}}, \"eval_gsm8k_sft_alpha0p5_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T10:19:48.133Z\", \"updated_at\": \"2026-05-22T10:20:57.690Z\", \"hypothesis\": \"α=0.5 SFT GSM8K eval for C1 decoupling. Paired with α=0.5 GRPO (61.18%). Δ(GRPO-SFT) tests whether GRPO benefit is universal ±2pp across α values.\", \"parent\": \"pipeline_alpha0p5_20\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:3\", \"command\": \"eval_gsm8k.py --model_path sft_rasp_alpha0p5_20 --max_new_tokens 2048\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"checkpoint_source\": \"sft_rasp_alpha0p5_20\", \"eval_data\": \"gsm8k test 1319\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha0p5_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/eval_gsm8k_sft_alpha0p5_20.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T10:20:50.793Z\", \"metrics\": {\"gsm8k_accuracy\": 0.6073, \"gsm8k_correct\": 801, \"gsm8k_total\": 1319}}, \"grpo_qwen_math_cka_only_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T08:50:34.293Z\", \"updated_at\": \"2026-05-22T09:54:05.974Z\", \"hypothesis\": \"MF3 cross-architecture validation: Qwen2.5-Math-7B CKA-only 20% pruned → SFT → GRPO 100 steps. Tests if CKA-guided pruning advantage transfers beyond DeepSeek-R1 to Qwen-Math family. P0 highest priority.\", \"parent\": \"sft_qwen_math_cka_only_20_v2\", \"spec\": {\"server\": \"westb-23072\", \"gpu\": \"cuda:1\", \"command\": \"train_grpo_v5.py --model_path sft_qwen_math_cka_only_20_v2 --max_steps 100 --learning_rate 1e-6 --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --max_completion_length 512 --temperature 0.4 --beta 0.01 --loss_type dapo --format_reward_weight 0.1 --gradient_checkpointing true --optim adamw_8bit\", \"model_name\": \"Qwen2.5-Math-7B\", \"seed\": 42, \"pid\": \"164710\", \"data_path\": \"openai/gsm8k (train split)\", \"data_count\": 7473, \"checkpoint_source\": \"sft_qwen_math_cka_only_20_v2\", \"eval_data\": \"N/A - this is GRPO training, not eval\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_qwen_math_cka_only_20\", \"log_path\": \"/tmp/mf3_qwen_grpo.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T09:54:05.974Z\"}, \"eval_gsm8k_grpo_alpha2p0_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T09:28:08.089Z\", \"updated_at\": \"2026-05-22T09:29:24.824Z\", \"hypothesis\": \"α=2.0 GRPO GSM8K eval. Dose-response data point: moderate overlap suppression (α=2.0) between α=1.0 (61.49%) and α=4.0 (62.77%). Tests monotonicity of dose-response curve.\", \"parent\": \"pipeline_alpha2p0_20\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:2\", \"command\": \"eval_gsm8k.py --model_path grpo_rasp_alpha2p0_20 --max_new_tokens 2048\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"checkpoint_source\": \"grpo_rasp_alpha2p0_20\", \"eval_data\": \"gsm8k test 1319\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha2p0_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/eval_gsm8k_grpo_alpha2p0_20.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T09:29:16.837Z\", \"metrics\": {\"gsm8k_accuracy\": 0.6611, \"gsm8k_correct\": 872, \"gsm8k_total\": 1319}}, \"eval_gsm8k_grpo_alpha0p5_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T09:28:05.478Z\", \"updated_at\": \"2026-05-22T09:29:23.350Z\", \"hypothesis\": \"α=0.5 GRPO GSM8K eval. Dose-response data point: low overlap suppression (α=0.5) should yield lower accuracy than α=1.0 (61.49%) if CKA overlap suppression causally harms recovery.\", \"parent\": \"pipeline_alpha0p5_20\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:3\", \"command\": \"eval_gsm8k.py --model_path grpo_rasp_alpha0p5_20 --max_new_tokens 2048\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"checkpoint_source\": \"grpo_rasp_alpha0p5_20\", \"eval_data\": \"gsm8k test 1319\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha0p5_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/eval_gsm8k_grpo_alpha0p5_20.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T09:29:13.196Z\", \"metrics\": {\"gsm8k_accuracy\": 0.6118, \"gsm8k_correct\": 807, \"gsm8k_total\": 1319}}, \"eval_math500_sft_standard_20_1p5b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T04:31:30.202Z\", \"updated_at\": \"2026-05-22T08:27:40.167Z\", \"hypothesis\": \"1.5B Standard 20% SFT MATH-500 @2048. Cross-scale comparison with CKA-only 1.5B (10.6%) to test if CKA-guided pruning advantage is scale-invariant.\", \"spec\": {\"command\": \"python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b --max_new_tokens 2048 --output_path /root/recovery_aware_struct_prune/results/eval_math500_sft_standard_20_1p5b.json\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:0\"], \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"sft_standard_20_1p5b\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b\", \"seed\": 42, \"checkpoint_source\": \"sft_standard_20_1p5b\", \"eval_data\": \"MATH-500\", \"log_path\": \"/root/recovery_aware_struct_prune/logs/eval_math500_sft_standard_20_1p5b.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b\"}, \"conclusion\": \"success\", \"metrics\": {\"math500_accuracy\": 0.054, \"correct\": 27, \"total\": 500, \"truncated\": 335}, \"completed_at\": \"2026-05-22T07:50:22.759Z\"}, \"eval_gsm8k_sft_alpha4_20_v5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T03:49:50.201Z\", \"updated_at\": \"2026-05-22T06:05:53.848Z\", \"hypothesis\": \"α=4.0 SFT GSM8K N=1319 full eval @2048. D100 critical for C1 decoupling universality. v4 lost to westd-29022 outage. Re-run on westd-32935.\", \"parent\": \"eval_gsm8k_sft_alpha4_20_v4\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_alpha4_20\", \"log_path\": \"/root/recovery_aware_struct_prune/logs/eval_gsm8k_sft_alpha4_20_v5.log\", \"result_path\": \"/root/recovery_aware_struct_prune/results/eval_gsm8k_sft_alpha4_20_v5.json\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T05:47:27.370Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T05:47:34.101Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T05:47:41.693855+00:00\"}]}, \"metrics\": {\"gsm8k_accuracy\": 0.6194, \"correct\": 817, \"total\": 1319, \"stderr\": 0.0134, \"eos_rate\": 0.981, \"avg_response_length\": 197.85}}, \"eval_gsm8k_grpo_alpha4_20_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T03:49:52.414Z\", \"updated_at\": \"2026-05-22T05:33:39.349Z\", \"hypothesis\": \"α=4.0 GRPO GSM8K N=1319 full eval @2048. v1 timed out at 774/1319 (62.93% interim). v2 ALLOCATED but westd-29022 died. Re-run on westd-32935 with --max_new_tokens 2048.\", \"parent\": \"eval_gsm8k_grpo_alpha4_20_v2\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_alpha4_20/checkpoint-100 --max_new_tokens 2048 --output_path /root/recovery_aware_struct_prune/results/eval_gsm8k_grpo_alpha4_20_v3.json\", \"server\": \"westd-32935\", \"gpu\": [\"cuda:3\"], \"data_path\": \"GSM8K\", \"data_count\": 1319, \"model_name\": \"grpo_alpha4_20/checkpoint-100\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_alpha4_20/checkpoint-100\", \"seed\": 42, \"checkpoint_source\": \"grpo_alpha4_20/checkpoint-100\", \"eval_data\": \"GSM8K\", \"log_path\": \"/root/recovery_aware_struct_prune/logs/eval_gsm8k_grpo_alpha4_20_v3.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T05:30:52.773Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T05:30:50.611Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T05:31:04.453494+00:00\"}]}, \"metrics\": {\"gsm8k_accuracy\": 0.6277, \"gsm8k_accuracy_ci\": 0.0133, \"gsm8k_correct\": 828, \"gsm8k_total\": 1319, \"eos_rate\": 0.9856, \"avg_response_length\": 188.16, \"natural_eos\": 1300, \"truncated\": 19}, \"notes\": \"Cron 误判为 failed（进程正常退出但 cron 未检测到 sentinel）。实际完成 1319/1319，accuracy=62.77%。α=4.0 GRPO > Standard GRPO (59.84%) > RASP α=1.0 GRPO (54.43%)。确认 α tuning 有效缓解 RASP collapse。checkpoint_path: /root/autodl-tmp/recovery_aware_struct_prune/grpo_alpha4_20/checkpoint-100, log_path: /root/recovery_aware_struct_prune/logs/eval_gsm8k_grpo_alpha4_20_v3.log, results_path: /root/recovery_aware_struct_prune/results/eval_gsm8k_grpo_alpha4_20_v3.json\"}, \"eval_math500_sft_standard_25\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-21T02:58:32.492Z\", \"updated_at\": \"2026-05-22T02:31:03.648Z\", \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"reproduce\": {\"finished_at\": \"2026-05-21T02:58:40.587Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-21T02:58:45.343074+00:00\"}], \"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"math500_accuracy\": 0.13, \"correct\": 65, \"n_total\": 500}, \"notes\": \"v1 结果采用（v2 启动即崩溃）。结果文件: /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_standard_25.json。Director 于 2026-05-21 批准采用 v1 数据。\"}}, \"notes\": \"v1 结果采用（v2 启动即崩溃）。结果文件: /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_standard_25.json。Director 于 2026-05-21 批准采用 v1 数据。\", \"hypothesis\": \"Standard 25% SFT model MATH-500 accuracy establishes pre-GRPO baseline for standard pruning at 25% sparsity, enabling SFT→GRPO recovery delta on MATH-500\", \"completed_at\": \"2026-05-21T19:22:29.444Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870 --output_path /root/runs/recovery_aware_struct_prune/eval_math500_sft_standard_25/results.json --max_new_tokens 2048 --seed 42\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:1\"], \"pid\": \"104592\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"sft_standard_25/checkpoint-1870\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870\", \"seed\": 42, \"checkpoint_source\": \"sft_standard_25\", \"eval_data\": \"MATH-500\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_math500_sft_standard_25/run.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870\"}, \"conclusion\": \"success\", \"metrics\": {\"math500_accuracy\": 0.14, \"correct\": 70, \"n_total\": 500, \"natural_eos\": 185, \"truncated\": 315, \"avg_response_length\": 1367.82, \"v1_accuracy\": 0.13, \"v1_correct\": 65}}, \"grpo_alpha4_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T18:59:18.863Z\", \"updated_at\": \"2026-05-21T19:32:31.353Z\", \"hypothesis\": \"α=4.0 GRPO after SFT: if reward collapses (→0 like α=1.0 RASP GRPO), proves RASP collapse is structural, not hyperparameter-dependent. If reward stays positive and GSM8K improves over SFT, α tuning can mitigate collapse.\", \"parent\": \"sft_alpha4_20_v2\", \"spec\": {\"command\": \"python src/train_grpo_v5.py --alpha 4.0 --max_steps 100\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:2\"], \"pid\": \"406593\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_alpha4_20.log\", \"submitted_at\": \"2026-05-21T18:59:44.258Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Qwen2.5-7B\", \"seed\": 42, \"data_path\": \"gsm8k\", \"data_count\": 7473, \"checkpoint_source\": \"sft_alpha4_20_v2\", \"eval_data\": \"gsm8k\", \"wall_clock_seconds\": 1659.0, \"gpu_hours\": 0.46}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_alpha4_20/checkpoint-100\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/grpo_alpha4_20.log\", \"metrics\": {\"final_reward\": 0.198, \"reward_range\": \"0.146-0.256\", \"steps\": 100, \"final_loss\": 0.018, \"final_kl\": 0.00198}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T19:27:23.228Z\"}, \"eval_math500_grpo_cka_only_25_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T13:54:50.310Z\", \"updated_at\": \"2026-05-21T17:33:50.709Z\", \"hypothesis\": \"CKA-only 25% GRPO model MATH-500 @2048 accuracy for cross-benchmark validation, re-run with correct max_new_tokens=2048 for consistency with 20% data\", \"parent\": \"eval_math500_grpo_cka_only_25\", \"spec\": {\"command\": \"nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=0 python /root/recovery_aware_struct_prune/src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_25 --output_path /root/runs/recovery_aware_struct_prune/eval_math500_grpo_cka_only_25_v2 --seed 42 --max_new_tokens 2048' > /root/runs/recovery_aware_struct_prune/eval_math500_grpo_cka_only_25_v2/eval_math500_grpo_cka_only_25_v2.log 2>&1 &\", \"server\": \"westd-29022\", \"gpu\": \"cuda:0\", \"pid\": 379999, \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"Qwen2.5-7B CKA-only 25% GRPO\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_25\", \"seed\": 42, \"checkpoint_source\": \"grpo_cka_only_25\", \"eval_data\": \"MATH-500\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_math500_grpo_cka_only_25_v2/eval_math500_grpo_cka_only_25_v2.log\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-21T17:33:40.068Z\", \"metrics\": {\"math500_accuracy\": 0.184, \"math500_stderr\": 0.0173, \"correct\": 92, \"n_total\": 500}, \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_math500_grpo_cka_only_25_v2/eval_math500_grpo_cka_only_25_v2.log\"}, \"eval_math500_sft_cka_only_25_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T13:54:51.945Z\", \"updated_at\": \"2026-05-21T17:29:14.940Z\", \"hypothesis\": \"CKA-only 25% SFT model MATH-500 @2048 accuracy establishes pre-GRPO baseline, re-run with correct max_new_tokens=2048 for consistency\", \"parent\": \"eval_math500_sft_cka_only_25\", \"spec\": {\"command\": \"nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=2 python /root/recovery_aware_struct_prune/src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_25 --output_path /root/runs/recovery_aware_struct_prune/eval_math500_sft_cka_only_25_v2 --seed 42 --max_new_tokens 2048' > /root/runs/recovery_aware_struct_prune/eval_math500_sft_cka_only_25_v2/eval_math500_sft_cka_only_25_v2.log 2>&1 &\", \"server\": \"westd-29022\", \"gpu\": \"cuda:2\", \"pid\": 380074, \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"Qwen2.5-7B CKA-only 25% SFT\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_25\", \"seed\": 42, \"checkpoint_source\": \"sft_cka_only_25\", \"eval_data\": \"MATH-500\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_math500_sft_cka_only_25_v2/eval_math500_sft_cka_only_25_v2.log\"}, \"conclusion\": \"success\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_math500_sft_cka_only_25_v2/eval_math500_sft_cka_only_25_v2.log\", \"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-21T17:29:10.900Z\", \"metrics\": {\"math500_accuracy\": 0.192, \"correct\": 96, \"n_total\": 500, \"std_err\": 0.0176}, \"notes\": \"Eval completed all 500 problems. Result JSON not saved due to IsADirectoryError (output_path pointed to directory instead of file). Metrics extracted from log.\"}, \"eval_gsm8k_sft_standard_25\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T08:13:12.112Z\", \"updated_at\": \"2026-05-21T14:40:37.092Z\", \"hypothesis\": \"Standard 25% SFT GSM8K accuracy establishes pre-GRPO floor for importance-based pruning at 25% sparsity, enabling SFT→GRPO recovery delta comparison with CKA-only 25%\", \"spec\": {\"command\": \"nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=3 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870 --max_samples 1319 --seed 42'\", \"server\": \"westd-29022\", \"gpu\": \"cuda:3\", \"pid\": 335301, \"data_path\": \"GSM8K (N=1319)\", \"data_count\": 1319, \"model_name\": \"sft_standard_25\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870\", \"seed\": 42, \"checkpoint_source\": \"sft_standard_25\", \"eval_data\": \"GSM8K\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_gsm8k_sft_standard_25.log\", \"checkpoint_path\": \"N/A (eval only)\"}, \"metrics\": {\"gsm8k_accuracy\": 0.5087, \"stderr\": 0.0138, \"correct\": 671, \"n_total\": 1319, \"eos_rate\": 0.953, \"avg_response_length\": 333.15}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T14:40:37.092Z\"}, \"eval_math500_grpo_cka_only_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T02:41:32.199Z\", \"updated_at\": \"2026-05-21T12:47:30.348Z\", \"hypothesis\": \"CKA-only 20% GRPO model MATH-500 accuracy provides cross-benchmark validation at 20% sparsity and cross-method comparison with Random 20% GRPO MATH-500\", \"spec\": {\"max_new_tokens_actual\": 4096, \"note\": \"未显式指定 --max_new_tokens，脚本默认 4096。与 @2048 evals 不可直接比较。需用 eval_math500_grpo_cka_only_20_2048 重跑公平对比。\"}, \"parent\": \"grpo_cka_only_20\", \"reproduce\": {\"finished_at\": \"2026-05-18T14:05:38.456Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T14:05:47.086682+00:00\"}]}, \"metrics\": {\"accuracy\": 0.266, \"n_correct\": 133, \"n_total\": 500, \"stderr\": 0.0198, \"truncated\": 108, \"truncation_rate\": 0.216, \"avg_response_length\": 1124.24}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/math500_grpo_cka_only_20.json\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_grpo_cka_only_20.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T14:09:25.937Z\"}, \"eval_gsm8k_grpo_standard_25\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T06:42:08.819Z\", \"updated_at\": \"2026-05-21T12:37:17.579Z\", \"hypothesis\": \"Standard 25% GRPO后GSM8K评估。GRPO reward=0.00813 (near-total collapse)。验证 Standard pruning 在 25% 稀疏度下 GRPO 后数学推理能力。\", \"parent\": \"grpo_standard_25_westb\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25_westb/checkpoint-100 --max_samples 1319 --seed 42\", \"server\": \"westb-23072\", \"gpu\": \"cuda:1\", \"pid\": 75282, \"data_path\": \"gsm8k\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-standard-25pct-GRPO-v5fair\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25_westb/checkpoint-100\", \"eval_data\": \"GSM8K\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_standard_25.log\"}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.5186, \"stderr\": 0.0138, \"correct\": 684, \"n_total\": 1319, \"eos_rate\": 0.9575, \"avg_response_length\": 314.47}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25_westb/checkpoint-100\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_standard_25.log\", \"completed_at\": \"2026-05-21T12:37:17.579Z\"}, \"eval_gsm8k_sft_cka_only_25\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T06:47:14.010Z\", \"updated_at\": \"2026-05-21T10:17:58.203Z\", \"hypothesis\": \"CKA-only 25% SFT model retains higher GSM8K accuracy than GRPO-recovered model's SFT baseline, establishing the pre-GRPO accuracy floor for measuring recovery delta at 25% sparsity\", \"spec\": {\"command\": \"nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_25 --max_samples 1319 --seed 42'\", \"server\": \"westd-29022\", \"gpu\": \"cuda:1\", \"pid\": 329698, \"data_path\": \"GSM8K (N=1319)\", \"data_count\": 1319, \"model_name\": \"sft_cka_only_25\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_25\", \"seed\": 42, \"checkpoint_source\": \"sft_cka_only_25\", \"eval_data\": \"GSM8K\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_gsm8k_sft_cka_only_25.log\"}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.6012, \"correct\": 793, \"n_total\": 1319, \"stderr\": 0.0135, \"eos_rate\": 0.9803, \"avg_response_length\": 243.6}, \"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-21T10:17:58.203Z\"}, \"eval_gsm8k_sft_random_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T06:47:16.459Z\", \"updated_at\": \"2026-05-21T08:47:06.620Z\", \"hypothesis\": \"Random 20% SFT model GSM8K accuracy establishes the pre-GRPO floor for random pruning, enabling SFT→GRPO recovery delta comparison across pruning methods at 20% sparsity\", \"spec\": {\"command\": \"nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=2 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20 --max_samples 1319 --seed 42'\", \"server\": \"westd-29022\", \"gpu\": \"cuda:2\", \"pid\": 329770, \"data_path\": \"GSM8K (N=1319)\", \"data_count\": 1319, \"model_name\": \"sft_random_20\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_random_20\", \"seed\": 42, \"checkpoint_source\": \"sft_random_20\", \"eval_data\": \"GSM8K\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_gsm8k_sft_random_20.log\"}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.5125, \"correct\": 676, \"n_total\": 1319, \"stderr\": 0.0138, \"eos_rate\": 0.9932, \"avg_response_length\": 182.4}, \"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-21T08:47:06.620Z\"}, \"eval_gsm8k_grpo_cka_only_25_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:56:52.006Z\", \"updated_at\": \"2026-05-21T08:17:13.429Z\", \"hypothesis\": \"CKA-only 25% GRPO后GSM8K评估。model_path=/grpo_cka_only_25（根目录）。Cross-sparsity对比: Standard 25% GRPO=51.1%, RASP 25% GRPO=53.15%。\", \"parent\": \"grpo_cka_only_25\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_25 --max_samples 1319 --seed 42\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:0\"], \"pid\": \"322443\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_cka_only_25_v3.log\", \"data_path\": \"gsm8k\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-cka_only-25pct-GRPO\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_25\", \"eval_data\": \"GSM8K\"}, \"notes\": \"正确 PID=322443 (v3提交)。323174 是重复提交已 kill。\", \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.5959, \"correct\": 786, \"n_total\": 1319, \"eos_rate\": 0.9818}, \"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-21T08:17:13.429Z\"}, \"grpo_standard_25_westb\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T03:00:00.000Z\", \"updated_at\": \"2026-05-21T06:40:00.000Z\", \"hypothesis\": \"Standard 25% GRPO v5 fair config (100 steps, lr=1e-6, beta=0.01, T=0.4, seed=42) on westb. Re-run with fair config for cross-method comparison.\", \"parent\": \"sft_standard_25\", \"spec\": {\"command\": \"python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25_westb --max_steps 100 --save_steps 100 --seed 42\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:1\"], \"pid\": \"64194\", \"data_path\": \"gsm8k\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-standard-25pct-SFT\", \"seed\": 42}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T06:40:00.000Z\", \"metrics\": {\"reward\": 0.00813, \"steps\": 100, \"collapse_pattern\": \"near_total_collapse\"}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25_westb/checkpoint-100\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_standard_25.log\"}, \"eval_gsm8k_grpo_random_20_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:56:53.980Z\", \"updated_at\": \"2026-05-21T06:38:00.000Z\", \"hypothesis\": \"Random 20% GRPO后GSM8K评估。Random pruning reward=0.189（最低），验证无结构保留的pruning在GRPO后数学推理能力。\", \"parent\": \"grpo_random_20\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20/checkpoint-100 --max_samples 1319 --seed 42\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:1\"], \"pid\": \"322611\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_random_20_v2.log\", \"data_path\": \"gsm8k\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-random-20pct-GRPO\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20/checkpoint-100\", \"eval_data\": \"GSM8K\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T06:38:00.000Z\", \"metrics\": {\"gsm8k_accuracy\": 0.5057, \"gsm8k_stderr\": 0.0138, \"correct\": 667, \"total\": 1319, \"eos_rate\": 0.9954, \"avg_response_length\": 173}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20/checkpoint-100\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_random_20_v2.log\"}, \"sft_random_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T03:44:24.654Z\", \"updated_at\": \"2026-05-21T04:45:00.000Z\", \"hypothesis\": \"Random 20% pruning baseline SFT recovery. Random pruning 不保留任何结构信息，作为 ablation baseline 验证 CKA-guided pruning 的结构保留优势。\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T03:50:00.000Z\", \"spec\": {\"server\": \"westd-29022\", \"gpu\": [\"cuda:0\"], \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-random-20pct\", \"command\": \"python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_random_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20\", \"data_path\": \"gsm8k\", \"seed\": 42}, \"metrics\": {\"steps\": 1870, \"model_size_gb\": 12}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_random_20\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/sft_random_20.log\"}, \"grpo_random_20\": {\"created_at\": \"2026-05-17T13:30:31.016Z\", \"hypothesis\": \"Random pruning 的 GRPO collapse 行为 — 如果 collapse ≈ RASP (step~10)，则所有结构剪枝伤 RL；如果 ≈ Standard (step~60)，则 CKA-aware 选择特别伤 RL（redundancy-stability tradeoff 确认）；如果 stable（无 collapse），则 CKA narrative 需要重构。\", \"parent\": \"scoring_ablation_random_20\", \"retry_count\": 0, \"spec\": {\"command\": \"bash -c \\\"cd /root/recovery_aware_struct_prune && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20 --max_steps 100 --save_steps 100 --seed 42\\\"\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:0\"], \"pid\": \"317332\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_random_20.log\", \"submitted_at\": \"2026-05-21T03:46:03.569Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T04:42:00.000Z\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T04:42:00.000Z\", \"metrics\": {\"reward_mean\": 0.164, \"reward_range\": [0.14, 0.19], \"reward_peak\": 0.19, \"reward_peak_step\": 70, \"frac_zero_std_mean\": 0.333, \"frac_zero_std_range\": [0.3, 0.4], \"entropy_mean\": 0.221, \"entropy_range\": [0.2, 0.24], \"kl_mean\": 0.0045, \"steps_captured\": 9, \"max_step\": 90, \"pattern\": \"stable plateau, no collapse\", \"data_source\": \"log_file (W&B crashed before sync)\"}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20/checkpoint-100\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/grpo_random_20.log\", \"notes\": \"Dynamics data from steps 10-90 sufficient for C2 gradient analysis. Timeout at step 97 (EXIT_CODE=124), no final checkpoint saved (save_steps=99999). W&B crashed before sync. Pattern confirmed: stable plateau, no collapse. Reclassified from failed. Note: no step 100 data, no checkpoint for downstream eval.\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T01:39:50.153522+00:00\"}]}}, \"grpo_cka_only_25\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:49:22.258Z\", \"updated_at\": \"2026-05-21T03:22:07.134Z\", \"hypothesis\": \"CKA-only 25% GRPO training (v5 fair config, 100 steps, lr=1e-6, beta=0.01, T=0.4, seed=42). Cross-sparsity comparison: Standard 25%=51.1%, RASP 25%=53.15%. Tests if CKA-guided pruning advantage holds at 25%.\", \"parent\": \"sft_cka_only_25\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_25 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_25 --max_steps 100 --save_steps 100 --seed 42\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:2\"], \"pid\": \"310542\", \"data_path\": \"gsm8k\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-cka_only-25pct-SFT\", \"seed\": 42}, \"notes\": \"W&B run: mirgxi5b. Cron 5x miss 误判 failed，实际正常完成。\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T03:19:26.772Z\", \"metrics\": {\"reward\": 0.2875, \"steps\": 100}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_25/checkpoint-100\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_25/runs/\"}, \"eval_humaneval_sft_standard_25\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:43:32.214Z\", \"updated_at\": \"2026-05-21T02:44:15.495Z\", \"hypothesis\": \"Standard 25% structured pruning + SFT recovery on HumanEval: measures code generation capability of the standard pruning baseline at 25% sparsity after SFT recovery.\", \"spec\": {\"command\": \"python eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870\", \"server\": \"westb-23072\", \"data_path\": \"openai/openai_humaneval\", \"data_count\": 164, \"model_name\": \"Qwen2.5-Coder-3B-pruned-standard-25-sft\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870\", \"eval_data\": \"HumanEval\"}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870\", \"log_path\": \"/tmp/eval_humaneval_sft_standard_25.log\", \"conclusion\": \"success\", \"metrics\": {\"pass_at_1\": 0.0183, \"stderr\": 0.0105, \"n_passed\": 3, \"n_total\": 164}, \"completed_at\": \"2026-05-21T02:44:15.495Z\"}, \"sft_cka_only_25\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T01:50:42.758Z\", \"updated_at\": \"2026-05-21T02:40:00.000Z\", \"conclusion\": \"success\", \"hypothesis\": \"CKA-only 25% SFT recovery training. 2 epochs on pruned model (5.81B params, 23.67% actual sparsity). Prepares for GRPO → eval pipeline.\", \"metrics\": {\"final_loss\": 0.6508, \"mean_token_accuracy\": 0.8285, \"training_time_s\": 1644}, \"completed_at\": \"2026-05-21T02:20:00.000Z\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_25\", \"spec\": {\"command\": \"python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_cka_only_25 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_25 --gpu 1 --num_train_epochs 2 --learning_rate 2e-5 --batch_size 1 --gradient_accumulation_steps 8 --max_seq_length 2048 --seed 42\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:1\"], \"pid\": \"307651\", \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_cka_only_25.log\", \"account\": \"root\", \"data_path\": \"openai/gsm8k (cached)\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-cka_only-25pct\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_cka_only_25\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_25\"}}, \"prune_cka_only_25\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T13:43:54.266Z\", \"updated_at\": \"2026-05-21T01:50:00.000Z\", \"conclusion\": \"success\", \"hypothesis\": \"CKA-only pruning at 25% sparsity. Generates pruned model for SFT→GRPO→eval pipeline to complete cross-sparsity comparison (15%/20%/25%).\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_HUB_OFFLINE=1 python src/prune.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --mode cka_only --sparsity 0.25 --output_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_cka_only_25 --seed 42 --dtype bfloat16\", \"server\": \"westd-29022\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42}, \"metrics\": {\"actual_sparsity\": 0.2367, \"mlp_groups_pruned\": 248, \"mlp_groups_total\": 784, \"attn_groups_pruned\": 0, \"attn_groups_total\": 112, \"param_count_B\": 5.81, \"original_param_count_B\": 7.62}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_cka_only_25\", \"completed_at\": \"2026-05-21T01:50:00.000Z\", \"notes\": \"[2026-05-21] 重跑成功。2026-05-18 首次尝试失败（PREPARING 状态卡住）。今天用 worker 重新执行 pruning，CPU 运行约 5 min 完成。α 默认值（未显式设置），calibration 样本数使用脚本默认。\"}, \"eval_gsm8k_grpo_standard_15_seed123_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T23:00:14.007Z\", \"updated_at\": \"2026-05-21T00:57:58.499Z\", \"hypothesis\": \"GSM8K N=1319 eval on Standard 15% GRPO seed123 (v3 checkpoint on data disk). Fixed: HF_HOME pointing to data disk cache, removed HF_DATASETS_OFFLINE.\", \"parent\": \"grpo_standard_15_seed123_v3\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_15_seed123_v3/checkpoint-100 --max_samples 1319 --seed 42\", \"server\": \"westd-29022\", \"data_path\": \"gsm8k\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-standard-15pct-grpo-seed123\", \"seed\": 42, \"checkpoint_source\": \"grpo_standard_15_seed123_v3\", \"eval_data\": \"gsm8k_test_n1319\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.6513, \"accuracy_se\": 0.0131, \"n_correct\": 859, \"n_total\": 1319, \"eos_rate\": 0.9932, \"avg_response_length\": 183.25}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_standard_15_seed123_n1319.json\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_standard_15_seed123_v3.log\", \"completed_at\": \"2026-05-21T00:57:58.499Z\"}, \"eval_gsm8k_grpo_standard_15_seed456_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T23:00:15.387Z\", \"updated_at\": \"2026-05-21T00:51:20.262Z\", \"hypothesis\": \"GSM8K N=1319 eval on Standard 15% GRPO seed456 (v3 checkpoint on data disk). Fixed: tokenizer.json copied from seed123, HF_HOME pointing to data disk cache.\", \"parent\": \"grpo_standard_15_seed456_v3\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_15_seed456_v3/checkpoint-100 --max_samples 1319 --seed 42\", \"server\": \"westd-29022\", \"data_path\": \"gsm8k\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-standard-15pct-grpo-seed456\", \"seed\": 42, \"checkpoint_source\": \"grpo_standard_15_seed456_v3\", \"eval_data\": \"gsm8k_test_n1319\"}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.6543, \"gsm8k_stderr\": 0.0131, \"n_correct\": 863, \"n_total\": 1319, \"eos_rate\": 0.9939, \"avg_response_length\": 180.23}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_standard_15_seed456_n1319.json\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_standard_15_seed456_v3.log\", \"completed_at\": \"2026-05-21T00:51:20.262Z\"}, \"eval_gsm8k_grpo_cka_only_15_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T21:35:28.222Z\", \"updated_at\": \"2026-05-21T00:18:00.000Z\", \"hypothesis\": \"GSM8K N=1319 eval on CKA-only 15% GRPO seed123. Multi-seed validation for 15% sparsity gap statistical significance.\", \"parent\": \"grpo_cka_only_15_seed123\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 73.09, \"n_correct\": 964, \"n_total\": 1319, \"stderr\": 1.22, \"eos_rate\": 98.79, \"truncated\": 16}, \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_15_seed123/checkpoint-100 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_cka_only_15_seed123_n1319.json\", \"server\": \"westd-29022\", \"data_path\": \"gsm8k\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-cka_only-15pct-grpo-seed123\", \"seed\": 42, \"checkpoint_source\": \"grpo_cka_only_15_seed123\", \"eval_data\": \"gsm8k_test_n1319\"}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_15_seed123/checkpoint-100\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/gsm8k_grpo_cka_only_15_seed123.log\", \"completed_at\": \"2026-05-21T00:18:00.000Z\", \"notes\": \"GSM8K accuracy 73.09% (964/1319). Cron 曾误判 failed 后由 Director 恢复 RUNNING，最终正常完成。\"}, \"eval_gsm8k_grpo_cka_only_15_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T21:35:29.444Z\", \"updated_at\": \"2026-05-21T00:06:17.294Z\", \"hypothesis\": \"GSM8K N=1319 eval on CKA-only 15% GRPO seed456. Multi-seed validation for 15% sparsity gap statistical significance.\", \"parent\": \"grpo_cka_only_15_seed456\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_15_seed456/checkpoint-100 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_cka_only_15_seed456_n1319.json\", \"server\": \"westd-29022\", \"data_path\": \"gsm8k\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-cka_only-15pct-grpo-seed456\", \"seed\": 42, \"checkpoint_source\": \"grpo_cka_only_15_seed456\", \"eval_data\": \"gsm8k_test_n1319\"}, \"notes\": \"[2026-05-20T23:15] Director 确认进程仍在运行 (PID 285821, cuda:1, 824/1319, 98% GPU利用率)。Cron 5x miss 误判为 failed，已恢复 RUNNING。\", \"metrics\": {\"accuracy\": 0.721, \"n_correct\": 951, \"n_total\": 1319, \"stderr\": 0.0123, \"eos_rate\": 0.9894, \"avg_response_length\": 201.94}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_cka_only_15_seed456_n1319.json\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/gsm8k_grpo_cka_only_15_seed456.log\", \"completed_at\": \"2026-05-21T00:06:17.294Z\"}, \"grpo_standard_15_seed456_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T21:58:14.439Z\", \"updated_at\": \"2026-05-20T22:51:31.775Z\", \"spec\": {\"command\": \"python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_15 --output_dir grpo_standard_15_seed456_v3 --max_steps 100 --seed 456\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:3\"], \"pid\": \"287862\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_standard_15_seed456_v3.log\", \"submitted_at\": \"2026-05-20T21:58:13.750Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"gsm8k\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-standard-15pct\", \"seed\": 456}, \"hypothesis\": \"Retry of grpo_standard_15_seed456 (v1 disk full, v2 wrong model path). Same v5 fair config (100 steps, beta=0.01, temperature=0.4, lr=1e-6, dapo loss, format_reward=0.1). Fixed: absolute model path + HF_HUB_OFFLINE=1. 88G free disk.\", \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_15_seed456_v3/checkpoint-100\"}, \"grpo_standard_15_seed123_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T21:58:11.697Z\", \"updated_at\": \"2026-05-20T22:51:30.499Z\", \"spec\": {\"command\": \"python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_15 --output_dir grpo_standard_15_seed123_v3 --max_steps 100 --seed 123\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:2\"], \"pid\": \"287784\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_standard_15_seed123_v3.log\", \"submitted_at\": \"2026-05-20T21:58:10.978Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"gsm8k\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-standard-15pct\", \"seed\": 123}, \"hypothesis\": \"Retry of grpo_standard_15_seed123 (v1 disk full, v2 wrong model path). Same v5 fair config (100 steps, beta=0.01, temperature=0.4, lr=1e-6, dapo loss, format_reward=0.1). Fixed: absolute model path + HF_HUB_OFFLINE=1. 88G free disk.\", \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_15_seed123_v3/checkpoint-100\"}, \"grpo_cka_only_15_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T20:54:57.409Z\", \"updated_at\": \"2026-05-20T21:35:16.671Z\", \"spec\": {\"command\": \"python src/train_grpo_v5.py --model_path sft_cka_only_15 --output_dir grpo_cka_only_15_seed456 --max_steps 100 --seed 456\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:1\"], \"pid\": \"281727\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_cka_only_15_seed456.log\", \"submitted_at\": \"2026-05-20T20:54:56.719Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"gsm8k\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-cka_only-15pct\", \"seed\": 456, \"wall_clock_seconds\": 2420.0, \"gpu_hours\": 0.67}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_15_seed456/checkpoint-100\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_cka_only_15_seed456.log\", \"hypothesis\": \"Multi-seed validation (seed=456) of CKA-only 15% GRPO training. v5 fair config (100 steps). Seed=42 (grpo_cka_only_15_v2): completed with reward=0.4019. Third seed point for CKA-only 15% recovery consistency and statistical significance.\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T21:35:16.671Z\"}, \"grpo_cka_only_15_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T20:54:54.710Z\", \"updated_at\": \"2026-05-20T21:35:14.509Z\", \"spec\": {\"command\": \"python src/train_grpo_v5.py --model_path sft_cka_only_15 --output_dir grpo_cka_only_15_seed123 --max_steps 100 --seed 123\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:0\"], \"pid\": \"281647\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_cka_only_15_seed123.log\", \"submitted_at\": \"2026-05-20T20:54:54.017Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"gsm8k\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-cka_only-15pct\", \"seed\": 123, \"wall_clock_seconds\": 2420.5, \"gpu_hours\": 0.67}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_15_seed123/checkpoint-100\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_cka_only_15_seed123.log\", \"hypothesis\": \"Multi-seed validation (seed=123) of CKA-only 15% GRPO training. v5 fair config (100 steps). Seed=42 (grpo_cka_only_15_v2): completed with reward=0.4019. Second seed point to establish CKA-only 15% recovery consistency for cross-sparsity significance testing.\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T21:35:14.509Z\"}, \"eval_gsm8k_sft_standard_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:07:58.760Z\", \"updated_at\": \"2026-05-20T19:58:14.139Z\", \"hypothesis\": \"GSM8K N=1319 eval on Standard 20% SFT checkpoint (pre-GRPO). Direct measurement of SFT baseline for Standard 20% — needed for paper Table 2 exact GRPO delta calculation.\", \"parent\": \"pipeline_standard_20\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_standard_20_n1319.json\", \"server\": \"westd-29022\", \"gpu\": \"cuda:0\", \"pid\": 266847, \"data_path\": \"gsm8k/test\", \"data_count\": 1319, \"model_name\": \"sft_standard_20 (Qwen2.5-7B, 20% standard sparsity, SFT only)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20\", \"eval_data\": \"gsm8k:test:1319\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_sft_standard_20.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_standard_20_n1319.json\"}, \"metrics\": {\"gsm8k_accuracy\": 0.5921, \"stderr\": 0.0135, \"correct\": 781, \"total\": 1319, \"eos_rate\": 0.9848, \"avg_response_length\": 206.68}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T19:58:14.139Z\"}, \"eval_gsm8k_dense_unpruned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T16:28:28.020Z\", \"updated_at\": \"2026-05-20T19:36:49.374Z\", \"hypothesis\": \"GSM8K N=1319 eval on dense unpruned DeepSeek-R1-Distill-Qwen-7B. Ceiling reference for paper — all pruned models should be compared against this baseline to show accuracy retention rate.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_dense_unpruned_n1319.json\", \"server\": \"westb-23072\", \"gpu\": \"cuda:0\", \"pid\": 32154, \"data_path\": \"gsm8k/test\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (dense, unpruned)\", \"seed\": 42, \"eval_data\": \"gsm8k:test:1319\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_dense_unpruned.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_dense_unpruned_n1319.json\"}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.9083, \"gsm8k_accuracy_ci\": 0.0079, \"correct\": 1198, \"total\": 1319, \"eos_rate\": 0.9871, \"avg_response_length\": 594, \"truncated\": 17, \"eval_time\": \"3h7m\"}}, \"eval_gsm8k_sft_cka_only_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T16:32:21.874Z\", \"updated_at\": \"2026-05-20T18:49:11.554Z\", \"hypothesis\": \"GSM8K N=1319 eval on CKA-only 20% SFT checkpoint (pre-GRPO). Direct measurement of SFT baseline for 20% sparsity — needed for paper table to calculate exact GRPO delta. Current estimate ~63.91% from reverse calculation.\", \"parent\": \"pipeline_cka_only_20\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_cka_only_20_n1319.json\", \"server\": \"westd-29022\", \"gpu\": \"cuda:2\", \"pid\": 264522, \"data_path\": \"gsm8k/test\", \"data_count\": 1319, \"model_name\": \"sft_cka_only_20 (Qwen2.5-7B, 20% CKA-only sparsity, SFT only)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20\", \"eval_data\": \"gsm8k:test:1319\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_sft_cka_only_20.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_cka_only_20_n1319.json\"}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.6391, \"gsm8k_accuracy_ci\": 0.0132, \"correct\": 843, \"total\": 1319, \"eos_rate\": 0.9901, \"avg_response_length\": 198.1, \"truncated\": 13}, \"completed_at\": \"2026-05-20T18:49:11.554Z\"}, \"eval_gsm8k_sft_cka_only_15\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T15:19:42.152Z\", \"updated_at\": \"2026-05-20T18:33:53.213Z\", \"hypothesis\": \"GSM8K N=1319 eval on CKA-only 15% SFT checkpoint (pre-GRPO). Fills cross-sparsity comparison table: CKA-only 15% SFT baseline. Compare with Standard 15% SFT (eval_gsm8k_sft_standard_15) to quantify pruning method effect at SFT stage for 15% sparsity.\", \"parent\": \"pipeline_cka_only_15\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_15 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_cka_only_15_n1319.json\", \"server\": \"westd-29022\", \"gpu\": \"cuda:1\", \"pid\": 262728, \"data_path\": \"gsm8k/test\", \"data_count\": 1319, \"model_name\": \"sft_cka_only_15 (Qwen2.5-7B, 15% CKA-only sparsity, SFT only)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_15\", \"eval_data\": \"gsm8k:test:1319\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_sft_cka_only_15.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_cka_only_15_n1319.json\"}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.7218, \"correct\": 952, \"total\": 1319}, \"completed_at\": \"2026-05-20T18:33:53.213Z\"}, \"eval_gsm8k_sft_rasp_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:09:04.809Z\", \"updated_at\": \"2026-05-20T18:10:54.576Z\", \"hypothesis\": \"GSM8K N=1319 eval on RASP 20% SFT checkpoint (pre-GRPO). Fills Table 2 SFT column for RASP method. Compare with CKA-only and Standard SFT baselines at same sparsity.\", \"parent\": \"pipeline_rasp_20\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_rasp_20_n1319.json\", \"server\": \"westd-29022\", \"gpu\": \"cuda:3\", \"pid\": 267009, \"data_path\": \"gsm8k/test\", \"data_count\": 1319, \"model_name\": \"sft_rasp_20_westd (Qwen2.5-7B, 20% RASP sparsity, SFT only)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd\", \"eval_data\": \"gsm8k:test:1319\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_sft_rasp_20.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_rasp_20_n1319.json\"}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.6149, \"gsm8k_accuracy_ci\": 0.0134, \"correct\": 811, \"total\": 1319, \"eos_rate\": 0.9826, \"avg_response_length\": 216.5}, \"completed_at\": \"2026-05-20T18:10:54.576Z\"}, \"eval_gsm8k_grpo_standard_15_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T14:43:21.408Z\", \"updated_at\": \"2026-05-20T16:28:25.206Z\", \"hypothesis\": \"GSM8K N=1319 full eval on Standard 15% GRPO v2 (reward=0.1375). W-C6 cross-sparsity: compare with CKA-only 15% GRPO (interim 74.22%). If Standard 15% << CKA-only 15%, confirms recovery gradient holds at lower sparsity.\", \"parent\": \"grpo_standard_15_v2\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_15_v2 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_standard_15_v2_n1319.json\", \"server\": \"westd-29022\", \"gpu\": \"cuda:3\", \"pid\": 256586, \"data_path\": \"gsm8k/test\", \"data_count\": 1319, \"model_name\": \"grpo_standard_15_v2\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_15_v2\", \"eval_data\": \"gsm8k:test:1319\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_standard_15_v2.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_standard_15_v2_n1319.json\"}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.6611, \"correct\": 872, \"total\": 1319, \"eos_rate\": 0.993, \"avg_response_length\": 184}, \"completed_at\": \"2026-05-20T16:27:32.096Z\"}, \"eval_gsm8k_sft_standard_15\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T14:23:49.568Z\", \"updated_at\": \"2026-05-20T16:28:23.020Z\", \"hypothesis\": \"GSM8K N=1319 eval on Standard 15% SFT checkpoint (pre-GRPO). Establishes SFT baseline accuracy for Standard 15% sparsity. Paired with eval_gsm8k_grpo_standard_15_v2 to measure GRPO recovery delta. Compare with SFT CKA-only 15% to quantify pruning method effect at SFT stage.\", \"parent\": \"pipeline_standard_15\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_15 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_standard_15_n1319.json\", \"server\": \"westd-29022\", \"gpu\": \"cuda:2\", \"pid\": 256743, \"data_path\": \"gsm8k/test\", \"data_count\": 1319, \"model_name\": \"sft_standard_15 (Qwen2.5-7B, 15% standard sparsity, SFT only)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_15\", \"eval_data\": \"gsm8k:test:1319\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_sft_standard_15.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_standard_15_n1319.json\"}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.6649, \"correct\": 877, \"total\": 1319, \"eos_rate\": 0.993, \"avg_response_length\": 183}, \"completed_at\": \"2026-05-20T16:27:28.365Z\"}, \"eval_gsm8k_grpo_cka_only_15_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T13:32:17.474Z\", \"updated_at\": \"2026-05-20T16:04:05.569Z\", \"hypothesis\": \"GSM8K N=1319 full eval on CKA-only 15% GRPO v2. Training complete: loss=0.2027, reward=0.4019. W-C6 cross-sparsity: if 15% CKA-only > 15% Standard (pending), confirms recovery gradient holds at lower sparsity. Compare with 20% CKA-only (64.37% seed42).\", \"parent\": \"grpo_cka_only_15_v2\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_15_v2 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_cka_only_15_v2_n1319.json\", \"server\": \"westd-29022\", \"gpu\": \"cuda:1\", \"pid\": 252919, \"data_path\": \"gsm8k:test\", \"data_count\": 1319, \"model_name\": \"grpo_cka_only_15_v2\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_15_v2\", \"eval_data\": \"gsm8k:test:1319\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_cka_only_15_v2.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_cka_only_15_v2_n1319.json\"}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.7309, \"gsm8k_accuracy_ci\": 0.0122, \"correct\": 964, \"total\": 1319, \"eos_rate\": 0.9894, \"avg_response_length\": 202.4}, \"completed_at\": \"2026-05-20T16:04:05.569Z\"}, \"eval_gsm8k_grpo_cka_only_20_seed456_full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T13:31:33.529Z\", \"updated_at\": \"2026-05-20T16:04:03.508Z\", \"hypothesis\": \"GSM8K N=1319 full eval on CKA-only GRPO seed=456. Training complete: loss=0.0999, reward=0.2925. Seed=42: 64.37%, seed=123: 64.22%. If seed=456 matches, confirms CKA-only GRPO recovery is consistent across seeds (3-seed parity with Standard). P0 W-C4.\", \"parent\": \"grpo_cka_only_20_seed456\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_seed456 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_cka_only_20_seed456_n1319.json\", \"server\": \"westd-29022\", \"gpu\": \"cuda:0\", \"pid\": 252604, \"data_path\": \"gsm8k\", \"data_count\": 1319, \"model_name\": \"grpo_cka_only_20_seed456\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_seed456\", \"eval_data\": \"gsm8k_n1319\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_cka_only_20_seed456_full.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_seed456\"}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.6459, \"gsm8k_accuracy_ci\": 0.0132, \"correct\": 852, \"total\": 1319, \"eos_rate\": 0.9886, \"avg_response_length\": 204.3}, \"completed_at\": \"2026-05-20T16:04:03.508Z\"}, \"eval_gsm8k_sft_qwen_standard_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:32:12.883Z\", \"updated_at\": \"2026-05-20T15:44:54.102Z\", \"hypothesis\": \"GSM8K N=200 eval of Qwen2.5-Math-7B Standard 20% SFT epoch 1 (checkpoint-935). Post-prune accuracy was 18.5%. Standard uses importance-based pruning. Fair comparison with CKA-only at same training point (epoch 1.0, step 935).\", \"parent\": \"sft_qwen_math_standard_20\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_qwen_math/checkpoint-935 --max_samples 200 --seed 42 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_qwen_standard_20.json\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:1\"], \"pid\": \"18114\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_sft_qwen_standard_20.log\", \"submitted_at\": \"2026-05-20T11:32:15Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"gsm8k/test\", \"data_count\": 200, \"model_name\": \"Qwen2.5-Math-7B-Standard-20%-SFT-ep1\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_qwen_math/checkpoint-935\", \"eval_data\": \"gsm8k-test-N200\", \"wall_clock_seconds\": 15018.0, \"gpu_hours\": 4.17}, \"reproduce\": {\"finished_at\": \"2026-05-20T15:42:28.206Z\"}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T15:42:32.993Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-20T15:42:39.040093+00:00\"}]}, \"metrics\": {\"gsm8k_accuracy\": 0.21, \"correct\": 42, \"total\": 200}}, \"eval_gsm8k_sft_qwen_cka_only_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:32:11.084Z\", \"updated_at\": \"2026-05-20T15:39:07.657Z\", \"hypothesis\": \"GSM8K N=200 eval of Qwen2.5-Math-7B CKA-only 20% SFT epoch 1 (checkpoint-935). Post-prune accuracy was 1.00% (near zero). CKA-only preserves layer diversity but causes severe initial damage. Fair comparison with Standard at same training point (epoch 1.0, step 935). If CKA-only SFT recovers above Standard, validates recovery-aware principle on Qwen-Math.\", \"parent\": \"sft_qwen_math_cka_only_20\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_cka_only_20/checkpoint-935 --max_samples 200 --seed 42 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_qwen_cka_only_20.json\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:0\"], \"pid\": \"18038\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_sft_qwen_cka_only_20.log\", \"submitted_at\": \"2026-05-20T11:32:13Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"gsm8k/test\", \"data_count\": 200, \"model_name\": \"Qwen2.5-Math-7B-CKA-only-20%-SFT-ep1\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_cka_only_20/checkpoint-935\", \"eval_data\": \"gsm8k-test-N200\", \"wall_clock_seconds\": 14658.4, \"gpu_hours\": 4.07}, \"reproduce\": {\"finished_at\": \"2026-05-20T15:36:25.631Z\"}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T15:36:31.442Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-20T15:36:42.911537+00:00\"}]}, \"metrics\": {\"gsm8k_accuracy\": 0.515, \"gsm8k_accuracy_ci\": 0.0353, \"correct\": 103, \"total\": 200, \"eos_rate\": 0.27, \"avg_response_length\": 1536, \"truncated\": 146, \"eval_time\": \"4h00m04s\"}}, \"grpo_standard_15_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T13:42:06.715Z\", \"updated_at\": \"2026-05-20T14:23:39.083Z\", \"hypothesis\": \"Standard 15% GRPO training (100 steps, v5 config). W-C6 cross-sparsity pair with grpo_cka_only_15_v2 (reward=0.4019). If Standard 15% < CKA-only 15%, confirms recovery gradient holds at lower sparsity.\", \"parent\": \"pipeline_standard_15\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 WANDB_MODE=offline nohup python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_15 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_15_v2 --max_steps 100 --save_steps 100 --seed 42\", \"server\": \"westd-29022\", \"gpu\": \"cuda:2\", \"pid\": 253918, \"data_path\": \"openai/gsm8k (cached)\", \"data_count\": 7473, \"model_name\": \"sft_standard_15 (pruned Qwen2.5-7B, 15% standard sparsity)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_15\", \"eval_data\": \"openai/gsm8k\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_standard_15_v2.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_15_v2\"}, \"conclusion\": \"success\", \"metrics\": {\"loss\": 0.01142, \"reward\": 0.1375, \"reward_std\": 0.2778, \"kl\": 0.004099, \"entropy\": 0.1932, \"grad_norm\": 3.547, \"total_steps\": 100, \"training_time\": \"21m49s\"}, \"completed_at\": \"2026-05-20T14:23:39.083Z\"}, \"eval_gsm8k_grpo_standard_20_seed123_full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:27:04.283Z\", \"updated_at\": \"2026-05-20T13:38:49.241Z\", \"hypothesis\": \"GSM8K N=1319 full eval on Standard GRPO seed=123. N=200 quick eval showed 64.00% (128/200). Seed=42 full eval: 59.44% (784/1319). Full eval to determine if seed123's higher accuracy holds or is small-sample noise (N=200 95% CI ≈ ±6.7pp).\", \"parent\": \"grpo_standard_20_seed123\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_seed123 --max_samples 1319 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_standard_20_seed123_n1319.json\", \"server\": \"westd-29022\", \"gpu\": \"cuda:2\", \"data_path\": \"openai/gsm8k\", \"data_count\": 1319, \"model_name\": \"grpo_standard_20_seed123\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_seed123\", \"eval_data\": \"GSM8K test (N=1319)\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_standard_20_seed123_n1319.json\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_standard_20_seed123_n1319.json\"}, \"metrics\": {\"accuracy\": 0.5989, \"n_correct\": 790, \"n_total\": 1319, \"stderr\": 0.0135, \"eos_rate\": null}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T13:38:49.241Z\"}, \"eval_gsm8k_grpo_standard_20_seed456_full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:27:05.741Z\", \"updated_at\": \"2026-05-20T13:38:47.186Z\", \"hypothesis\": \"GSM8K N=1319 full eval on Standard GRPO seed=456. N=200 quick eval showed 66.50% (133/200), exceeding CKA-only's 64.37%. Seed=42 full eval: 59.44% (784/1319). Full eval to determine if seed456's high accuracy holds or is small-sample noise (N=200 95% CI ≈ ±6.5pp).\", \"parent\": \"grpo_standard_20_seed456\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_seed456 --max_samples 1319 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_standard_20_seed456_n1319.json\", \"server\": \"westd-29022\", \"gpu\": \"cuda:3\", \"data_path\": \"openai/gsm8k\", \"data_count\": 1319, \"model_name\": \"grpo_standard_20_seed456\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_seed456\", \"eval_data\": \"GSM8K test (N=1319)\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_standard_20_seed456_n1319.json\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_standard_20_seed456_n1319.json\"}, \"metrics\": {\"accuracy\": 0.602, \"n_correct\": 794, \"n_total\": 1319, \"stderr\": 0.01348, \"eos_rate\": 0.9856}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T13:38:47.186Z\"}, \"grpo_cka_only_15_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:58:03.218Z\", \"updated_at\": \"2026-05-20T13:35:06.015Z\", \"hypothesis\": \"CKA-only 15% GRPO restart (resume from checkpoint-20). Original pipeline_cka_only_15 failed at checkpoint-20 due to disk full. Now disk has 185G available. W-C6 cross-sparsity validation: if CKA-only > Standard holds at 15%, strengthens the claim.\", \"parent\": \"pipeline_cka_only_15\", \"notes\": \"checkpoint-20 from original pipeline_cka_only_15 is corrupted (safetensors incomplete metadata, disk-full damage). Starting fresh from sft_cka_only_15. New output_dir: grpo_cka_only_15_v2. Director requested --save_only_model but script doesn't support it.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_15 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_15_v2 --max_steps 100 --save_steps 100 --seed 42\", \"server\": \"westd-29022\", \"gpu\": \"cuda:1\", \"pid\": 250149, \"log_path\": \"/root/runs/recovery_aware_struct_prune/grpo_cka_only_15_v2.log\", \"model_name\": \"sft_cka_only_15\", \"data_path\": \"openai/gsm8k (cached)\", \"data_count\": 7473, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_15\", \"eval_data\": \"gsm8k train (GRPO training, not eval)\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_15_v2\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T13:35:03.878Z\", \"metrics\": {\"final_loss\": 0.2027, \"avg_train_loss\": 0.11, \"final_reward\": 0.4019, \"final_kl\": 0.0018, \"train_steps\": 100, \"train_runtime_min\": 22.5}}, \"grpo_cka_only_20_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:36:13.866Z\", \"updated_at\": \"2026-05-20T13:35:02.652Z\", \"hypothesis\": \"Multi-seed validation (seed=456) of CKA-only 20% GRPO training. v5 fair config (100 steps, beta=0.01, loss_type=dapo, temperature=0.4). Seed=42: 64.37%, seed=123: 64.22%. Third seed point to establish CKA-only method's recovery consistency and enable 3-seed parity comparison with Standard (3 seeds: 59.44%, pending, pending). P0 审稿硬需求 W-C4.\", \"parent\": \"grpo_cka_only_20\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_seed456 --max_steps 100 --save_steps 100 --seed 456\", \"server\": \"westd-29022\", \"gpu\": \"cuda:0\", \"pid\": 249963, \"log_path\": \"/root/runs/recovery_aware_struct_prune/grpo_cka_only_20_seed456.log\", \"model_name\": \"sft_cka_only_20\", \"data_path\": \"openai/gsm8k (cached)\", \"data_count\": 7473, \"seed\": 456, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20\", \"eval_data\": \"gsm8k train (GRPO training, not eval)\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_seed456\"}, \"notes\": \"Director requested --save_only_model but script doesn't support it. Training started at step 0, ~12.7s/step, ETA ~21min for 100 steps. tmux session: grpo_seed456.\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T13:34:58.996Z\", \"metrics\": {\"final_loss\": 0.0999, \"avg_train_loss\": 0.0881, \"final_reward\": 0.2925, \"final_kl\": 0.0017, \"train_steps\": 100, \"train_runtime_min\": 21.8}}, \"prune_eval_standard_30\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T04:08:24.071Z\", \"updated_at\": \"2026-05-20T11:56:25.682Z\", \"hypothesis\": \"Standard importance pruning at 30% sparsity post-prune GSM8K accuracy. Extends sparsity ladder (20%→25%→30%) to probe Standard degradation curve. No SFT/GRPO recovery, raw post-prune performance.\", \"spec\": {\"command\": \"python src/prune.py --mode standard --sparsity 0.30 + python src/eval_gsm8k.py\", \"server\": \"westd-29022\", \"gpu\": \"cuda:1\", \"pid\": 190349, \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/prune_eval_standard_30.log\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"data_path\": \"gsm8k test\", \"data_count\": 1319, \"seed\": 42}, \"notes\": \"Original run killed (PID 191519). Re-submitted in tmux eval_std30, PID 202006 on GPU cuda:1. Diagnostic confirms model on cuda:0 (CUDA_VISIBLE_DEVICES=1), 86% util. Speed ~30-48s/sample = ~15-17h ETA for N=1319.\", \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T09:22:44.252Z\", \"metrics\": {\"accuracy\": 2.8, \"note\": \"N=500 partial result (killed by Director, 30% sparsity = complete collapse, N=500 precision sufficient)\", \"n_evaluated\": 500, \"n_total\": 1319, \"eos_rate\": 1.2, \"avg_len\": 4057}}, \"prune_eval_cka_only_30\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T04:08:22.614Z\", \"updated_at\": \"2026-05-20T11:56:24.517Z\", \"hypothesis\": \"CKA-only pruning at 30% sparsity post-prune GSM8K accuracy. Extends sparsity ladder (20%→25%→30%) to probe CKA-only degradation curve. No SFT/GRPO recovery, raw post-prune performance.\", \"spec\": {\"command\": \"python src/prune.py --mode cka_only --sparsity 0.30 + python src/eval_gsm8k.py\", \"server\": \"westd-29022\", \"gpu\": \"cuda:0\", \"pid\": 190269, \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/prune_eval_cka_only_30.log\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"data_path\": \"gsm8k test\", \"data_count\": 1319, \"seed\": 42}, \"notes\": \"Original run killed (PID 191446). Re-submitted in tmux eval_cka30, PID 201928 on GPU cuda:0. Diagnostic confirms model on cuda:0, 85% util, 11.5GB VRAM. Speed ~48s/sample = ~17h ETA for N=1319. Original run was likely also on GPU (identical speed pattern).\", \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T09:22:39.147Z\", \"metrics\": {\"accuracy\": 1.6, \"note\": \"N=500 partial result (killed by Director, 30% sparsity = complete collapse, N=500 precision sufficient)\", \"n_evaluated\": 500, \"n_total\": 1319, \"eos_rate\": 5.6, \"avg_len\": 4009}}, \"sft_qwen_math_cka_only_20_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T09:18:17.089Z\", \"updated_at\": \"2026-05-20T09:50:15.333Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_cka_only_20/checkpoint-935 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_cka_only_20_final --gpu 0 --num_train_epochs 1 --save_strategy no\\\"\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:0\"], \"pid\": \"9952\", \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_qwen_math_cka_only_20_v2.log\", \"submitted_at\": \"2026-05-20T09:18:16.420Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"openai/gsm8k (cached)\", \"data_count\": 7473, \"model_name\": \"Qwen2.5-Math-7B-CKA-only-Pruned-20%\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_cka_only_20/checkpoint-935\", \"eval_data\": \"GSM8K train (7473 samples, SFT epoch 2)\", \"wall_clock_seconds\": 1918.9, \"gpu_hours\": 0.53}, \"hypothesis\": \"Qwen2.5-Math-7B CKA-only 20% SFT recovery epoch 2 (resume from checkpoint-935 = epoch 1 完成). 原始 sft_qwen_math_cka_only_20 训练完成 1870 steps 但最终 checkpoint 保存失败（磁盘满）。checkpoint-935 验证完好（339 tensors）。从 epoch 1 权重续跑 1 epoch。\", \"parent\": \"sft_qwen_math_cka_only_20\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.3481, \"mean_token_accuracy\": 0.8595, \"train_runtime_sec\": 1013, \"train_samples_per_second\": 7.38, \"epochs\": 1}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_cka_only_20_final\", \"completed_at\": \"2026-05-20T09:50:15.333Z\"}, \"eval_gsm8k_grpo_standard_20_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T09:15:10.283Z\", \"updated_at\": \"2026-05-20T09:49:10.630Z\", \"hypothesis\": \"GSM8K N=200 quick eval on Standard GRPO seed=456 model. Seed=42 accuracy: 59.44% (N=1319), seed=123 being evaluated. If seed=456 within ±5pp of seed=42, confirms Standard recovery capacity is not seed-dependent.\", \"parent\": \"grpo_standard_20_seed456\", \"spec\": {\"command\": \"eval_gsm8k.py --model_path grpo_standard_20_seed456 --max_samples 200\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:3\"], \"pid\": \"221008\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_standard_20_seed456.log\", \"submitted_at\": \"2026-05-20T09:15:19.738Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"openai/gsm8k\", \"data_count\": 200, \"model_name\": \"grpo_standard_20_seed456\", \"seed\": 456, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_seed456\", \"eval_data\": \"GSM8K test (N=200)\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/gsm8k_grpo_standard_20_seed456_n200.json\", \"wall_clock_seconds\": 2030.9, \"gpu_hours\": 0.56}, \"metrics\": {\"accuracy\": 0.665, \"n_correct\": 133, \"n_total\": 200, \"stderr\": 0.0334, \"eos_rate\": 0.995, \"avg_response_length\": 166.9}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T09:49:10.630Z\"}, \"eval_gsm8k_grpo_standard_20_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T09:15:16.595Z\", \"updated_at\": \"2026-05-20T09:49:08.654Z\", \"hypothesis\": \"GSM8K N=200 quick eval on Standard GRPO seed=123 model. Seed=42 accuracy: 59.44% (N=1319). If seed=123 within ±5pp of seed=42, confirms Standard stagnation pattern produces consistent accuracy across seeds.\", \"parent\": \"grpo_standard_20_seed123\", \"spec\": {\"command\": \"eval_gsm8k.py --model_path grpo_standard_20_seed123 --max_samples 200\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:2\"], \"pid\": \"221158\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_standard_20_seed123.log\", \"submitted_at\": \"2026-05-20T09:15:26.368Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"openai/gsm8k\", \"data_count\": 200, \"model_name\": \"grpo_standard_20_seed123\", \"seed\": 123, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_seed123\", \"eval_data\": \"GSM8K test (N=200)\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/gsm8k_grpo_standard_20_seed123_n200.json\", \"wall_clock_seconds\": 2022.3, \"gpu_hours\": 0.56}, \"metrics\": {\"accuracy\": 0.64, \"n_correct\": 128, \"n_total\": 200, \"stderr\": 0.0339, \"eos_rate\": 0.99, \"avg_response_length\": 187.9}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T09:49:08.654Z\"}, \"grpo_standard_20_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T06:22:10.493Z\", \"updated_at\": \"2026-05-20T09:13:48.616Z\", \"hypothesis\": \"Multi-seed validation (seed=456) of Standard 20% GRPO. v5 fair config (100 steps, beta=0.01, loss_type=dapo, temperature=0.4). Seed=42 baseline: 59.44% GSM8K. Third seed point to establish Standard method's recovery variance.\", \"parent\": \"grpo_stage2_standard_20_fair\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 WANDB_MODE=offline python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_seed456 --max_steps 100 --save_steps 100 --gpu 0 --seed 456\\\"\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:3\"], \"pid\": \"211798\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_standard_20_seed456.log\", \"submitted_at\": \"2026-05-20T06:22:19.535Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"openai/gsm8k\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-Standard-20%-SFT\", \"seed\": 456, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_seed456\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20\", \"eval_data\": \"GSM8K train (7473 samples, GRPO RLVR training)\", \"wall_clock_seconds\": 10289.1, \"gpu_hours\": 2.86}, \"metrics\": {\"steps_completed\": 100, \"runtime_sec\": 2745, \"peak_reward\": 0.0844, \"peak_reward_step\": 90, \"final_reward\": 0.06, \"final_frac_zero_std\": 0.65, \"seed\": 456, \"wandb_run\": \"wg0iv4oi\", \"wandb_mode\": \"offline\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T09:13:48.616Z\"}, \"grpo_standard_20_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T06:22:27.444Z\", \"updated_at\": \"2026-05-20T09:13:45.445Z\", \"hypothesis\": \"Multi-seed validation (seed=123) of Standard 20% GRPO. v5 fair config (100 steps, beta=0.01, loss_type=dapo, temperature=0.4, max_completion_length=1024). Seed=42 baseline: 59.44% GSM8K (784/1319). If seed=123 result within ±3pp, confirms Standard method's recovery capacity is stable across seeds.\", \"parent\": \"grpo_stage2_standard_20_fair\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 WANDB_MODE=offline python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_seed123 --max_steps 100 --max_completion_length 1024 --save_steps 100 --gpu 0 --run_name grpo_standard_20_seed123 --seed 123\\\"\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:2\"], \"pid\": \"211972\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_standard_20_seed123.log\", \"submitted_at\": \"2026-05-20T06:22:37.312Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-Standard-20%-SFT\", \"data_path\": \"openai/gsm8k\", \"data_count\": 7473, \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_seed123\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20\", \"eval_data\": \"GSM8K train (7473 samples, GRPO RLVR training)\", \"tmux_session\": \"grpo_standard_20_seed123\", \"wall_clock_seconds\": 10268.1, \"gpu_hours\": 2.85}, \"metrics\": {\"steps_completed\": 100, \"runtime_sec\": 2783, \"peak_reward\": 0.0619, \"peak_reward_step\": 80, \"final_reward\": 0.0594, \"final_frac_zero_std\": 0.6, \"seed\": 123, \"wandb_run\": \"pgzwv725\", \"wandb_mode\": \"offline\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T09:13:45.445Z\"}, \"eval_mbpp_grpo_standard_20_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T21:00:40.293Z\", \"updated_at\": \"2026-05-20T03:06:43.359Z\", \"conclusion\": \"success\", \"failure_reason\": \"RuntimeError: Cannot send a request, as the client has been closed. datasets.load_dataset(\\\"mbpp\\\") HTTP client died due to AutoDL network issues.\", \"spec\": {\"server\": \"westd-29022\", \"gpu\": \"cuda:2\", \"command\": \"python src/eval_mbpp.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_grpo_standard_20.json\", \"data_path\": \"mbpp\", \"data_count\": 374, \"model_name\": \"grpo_stage2_standard_20_fair\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/autodl-tmp/logs/eval_mbpp_grpo_standard_20_v3.log\"}, \"completed_at\": \"2026-05-19T21:01:12.805Z\", \"metrics\": {\"pass_at_1\": 0.131, \"correct\": 49, \"total\": 374, \"stderr\": 0.0174}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_grpo_standard_20.json\"}, \"eval_humaneval_sft_standard_20_1p5b_2048\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T11:35:45.876Z\", \"updated_at\": \"2026-05-20T03:06:22.483Z\", \"hypothesis\": \"1.5B SFT Standard HumanEval pass@1 @2048 on westb. Cross-scale validation of capability breadth claim. Running on westb cuda:0 where checkpoints already exist (no scp needed).\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_sft_standard_20_1p5b_2048.json\\\"\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:0\"], \"pid\": \"890564\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_humaneval_sft_standard_20_1p5b_2048.log\", \"submitted_at\": \"2026-05-19T12:23:31.889Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b\", \"eval_data\": \"HumanEval (164 problems, pass@1, max_new_tokens=2048)\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"sft_standard_20_1p5b\", \"seed\": 42, \"wall_clock_seconds\": 5434.5, \"gpu_hours\": 1.51}, \"reproduce\": {\"finished_at\": \"2026-05-19T13:50:34.259Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T13:50:39.347512+00:00\"}]}, \"metrics\": {\"pass_at_1\": 0.0061, \"correct\": 1, \"total\": 164, \"stderr\": 0.0061}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_humaneval_sft_standard_20_1p5b_2048.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T13:54:06.392Z\"}, \"eval_humaneval_sft_standard_20_2048_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T10:05:36.497Z\", \"updated_at\": \"2026-05-20T03:06:20.863Z\", \"hypothesis\": \"SFT Standard 20% HumanEval pass@1 @2048. Uses current sft_standard_20 model on westd-29022 (same model as MATH-500 eval at 25.8%). Fills SFT×method HumanEval matrix. Compare with GRPO Standard fair (~10% interim) and SFT CKA-only (~24% interim).\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_sft_standard_20_2048_v3.json'\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:3\"], \"pid\": \"86171\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"sft_standard_20\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20\", \"eval_data\": \"HumanEval (164 problems, pass@1, max_new_tokens=2048)\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_standard_20_2048_v3.log\", \"result_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_sft_standard_20_2048_v3.json\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T13:51:50.117Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T13:51:51.044Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T13:52:04.682130+00:00\"}]}, \"metrics\": {\"pass_at_1\": 0.1341, \"correct\": 22, \"total\": 164, \"stderr\": 0.0266}}, \"eval_humaneval_sft_cka_only_20_1p5b_2048\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T11:32:47.965Z\", \"updated_at\": \"2026-05-20T03:06:19.658Z\", \"hypothesis\": \"1.5B SFT CKA-only HumanEval pass@1 @2048. Cross-scale validation of capability breadth claim. 7B SFT CKA-only result: failed (pass@1=0). Testing whether 1.5B scale shows different pattern, as SFT alone may not activate code generation capability regardless of pruning criterion.\", \"spec\": {\"command\": \"python src/eval_humaneval.py --model_path /root/autodl-tmp/models/sft_cka_only_20_1p5b --max_tokens 2048\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:1\"], \"pid\": \"95940\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_humaneval_sft_cka_only_20_1p5b_2048.log\", \"submitted_at\": \"2026-05-19T11:45:57.991Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"sft_cka_only_20_1p5b\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"seed\": 42, \"checkpoint_source\": \"sft_cka_only_20_1p5b\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20_1p5b\", \"metrics\": {\"pass_at_1\": 0.0061, \"n_correct\": 1, \"n_total\": 164, \"avg_response_length\": 1968.76, \"median_response_length\": 2048}, \"wall_clock_seconds\": 6208.0, \"gpu_hours\": 1.72}, \"reproduce\": {\"finished_at\": \"2026-05-19T13:25:01.078Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T13:25:12.353193+00:00\"}]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T13:29:26.015Z\", \"metrics\": {\"pass_at_1\": 0.0061, \"correct\": 1, \"total\": 164, \"stderr\": 0.0061}}, \"eval_humaneval_grpo_cka_only_20_1p5b_2048\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T11:32:50.649Z\", \"updated_at\": \"2026-05-20T03:06:18.579Z\", \"hypothesis\": \"1.5B GRPO CKA-only HumanEval pass@1 @2048. Cross-scale validation of capability breadth claim. 7B result: pass@1=20.12%. If 1.5B CKA-only also shows strong code generation after GRPO (>> Standard/RASP), strengthens cross-scale evidence that CKA-based pruning preserves broader capability spectrum.\", \"spec\": {\"command\": \"python src/eval_humaneval.py --model_path /root/autodl-tmp/models/grpo_cka_only_20_1p5b --max_tokens 2048\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:2\"], \"pid\": \"96018\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_humaneval_grpo_cka_only_20_1p5b_2048.log\", \"submitted_at\": \"2026-05-19T11:46:00.256Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"grpo_cka_only_20_1p5b\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"seed\": 42, \"checkpoint_source\": \"grpo_cka_only_20_1p5b\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_1p5b\", \"wall_clock_seconds\": 7116.7, \"gpu_hours\": 1.98}, \"reproduce\": {\"finished_at\": \"2026-05-19T13:25:21.278Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T13:25:34.034561+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"pass_at_1\": 0, \"correct\": 0, \"total\": 164, \"stderr\": 0}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_1p5b\", \"completed_at\": \"2026-05-19T13:44:36.960Z\"}, \"eval_mbpp_sft_shortgpt_20_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T22:23:35.431Z\", \"updated_at\": \"2026-05-20T02:43:15.577Z\", \"hypothesis\": \"Retry of eval_mbpp_sft_shortgpt_20 which failed with EXIT_CODE=127 (command not found — missing conda activation). ShortGPT SFT 20% MBPP pass@1 @2048. ShortGPT GSM8K SFT=44.73%, GRPO=43.37%. Depth pruning 在 MBPP 上预期显著差于 fine-grained methods (CKA-only SFT 12.83%, RASP SFT 11.76%). 验证 coarse layer removal 对代码生成的破坏性。关联 ShortGPT baseline comparison。\", \"parent\": \"eval_mbpp_sft_shortgpt_20\", \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_shortgpt_20\", \"eval_data\": \"MBPP sanitized (374 tasks)\", \"data_path\": \"google-research-datasets/mbpp (sanitized)\", \"data_count\": 374, \"model_name\": \"Qwen2.5-7B-ShortGPT-20%-SFT\", \"seed\": 42, \"server\": \"westd-29022\", \"gpu\": [\"cuda:1\"], \"account\": \"root\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_mbpp.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_shortgpt_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/mbpp_sft_shortgpt_20.json\\\"\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_shortgpt_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/mbpp_sft_shortgpt_20.json\"}, \"server\": \"westd-29022\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"metrics\": {\"pass_at_1\": 0.1043, \"stderr\": 0.0158, \"n_correct\": 39, \"n_total\": 374, \"avg_response_length\": 1166.4, \"median_response_length\": 773.5}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T02:43:15.577Z\"}, \"eval_mbpp_grpo_shortgpt_20_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T22:33:19.363Z\", \"updated_at\": \"2026-05-20T02:43:06.318Z\", \"hypothesis\": \"Retry of eval_mbpp_grpo_shortgpt_20 which failed with EXIT_CODE=127 (missing conda activation). GRPO ShortGPT 20% MBPP pass@1 @2048. ShortGPT GSM8K: SFT=44.73%, GRPO=43.37% (GRPO退化). Depth pruning 在 MBPP 上预期显著差于 fine-grained methods。与 eval_mbpp_sft_shortgpt_20_v2 配对，完成 ShortGPT MBPP SFT/GRPO 对比。关联 ShortGPT baseline。\", \"parent\": \"grpo_shortgpt_20\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_mbpp.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_shortgpt_20/checkpoint-100 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/mbpp_grpo_shortgpt_20.json\\\"\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:3\"], \"account\": \"root\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_shortgpt_20/checkpoint-100\", \"eval_data\": \"MBPP sanitized (374 tasks)\", \"data_path\": \"google-research-datasets/mbpp (sanitized)\", \"data_count\": 374, \"model_name\": \"Qwen2.5-7B-ShortGPT-20%-GRPO\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_shortgpt_20/checkpoint-100\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/mbpp_grpo_shortgpt_20.json\"}, \"server\": \"westd-29022\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"pid\": \"unknown\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_mbpp_grpo_shortgpt_20_v2.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_mbpp.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_shortgpt_20/checkpoint-100 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/mbpp_grpo_shortgpt_20.json\\\"\", \"finished_at\": \"2026-05-19T22:35:33.272Z\"}, \"failure_reason\": \"EXIT_CODE=2 (shell misuse / syntax)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T22:35:37.037Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T22:35:44.977403+00:00\"}]}, \"metrics\": {\"pass_at_1\": 0.1444, \"stderr\": 0.0182, \"n_correct\": 54, \"n_total\": 374, \"avg_response_length\": 1140.8, \"median_response_length\": 804.5}}, \"eval_mbpp_sft_standard_20_v4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T22:26:22.996Z\", \"updated_at\": \"2026-05-20T02:16:04.699Z\", \"hypothesis\": \"MBPP pass@1 eval on SFT Standard 20% @2048. Dense baseline=53.48%. 此为手动 tmux 提交的 orphan 进程补录。目前 85/374 (23%), interim pass@1=0.175。HF_DATASETS_OFFLINE=1。关联 C2。\", \"parent\": \"eval_mbpp_sft_standard_20_clean\", \"server\": \"westd-29022\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"spec\": {\"command\": \"HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_mbpp.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/mbpp_sft_standard_20.json\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:0\"], \"data_path\": \"google-research-datasets/mbpp (sanitized)\", \"data_count\": 374, \"model_name\": \"sft_standard_20\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20\", \"eval_data\": \"MBPP sanitized (374 tasks)\", \"tmux_session\": \"eval_mbpp_sft_standard_20_v4\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_sft_standard_20.json\"}, \"metrics\": {\"pass_at_1\": 0.1203, \"stderr\": 0.0168, \"n_correct\": 45, \"n_total\": 374, \"avg_response_length\": 1084.1, \"median_response_length\": 746.5}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T02:16:04.699Z\"}, \"eval_mbpp_grpo_standard_20_v4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T21:01:23.058Z\", \"updated_at\": \"2026-05-20T01:46:54.906Z\", \"hypothesis\": \"GRPO Standard 20% pruned model should achieve ~13% pass@1 on MBPP, consistent with prior v1 partial results at 335/374 tasks\", \"parent\": \"eval_mbpp_grpo_standard_20_v3\", \"spec\": {\"server\": \"westd-29022\", \"gpu\": \"cuda:2\", \"command\": \"python src/eval_mbpp.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_grpo_standard_20.json\", \"data_path\": \"mbpp\", \"data_count\": 374, \"model_name\": \"grpo_stage2_standard_20_fair\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair\", \"eval_data\": \"mbpp_sanitized_374\"}, \"metrics\": {\"pass_at_1\": 0.131, \"n_correct\": 49, \"n_total\": 374, \"stderr\": 0.01745, \"avg_response_length\": 1058.7, \"median_response_length\": 726}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_grpo_standard_20.json\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T01:46:54.906Z\"}, \"cka_scoring_stability_ablation\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T21:21:10.933Z\", \"updated_at\": \"2026-05-19T22:21:53.770Z\", \"hypothesis\": \"CKA scoring stability across calibration sizes (256/512/1024). If Spearman ρ > 0.95 between all pairs, CKA scoring is robust to calibration size — directly answers reviewer concern about scoring sensitivity. Plan_014, C2 mechanism evidence.\", \"server\": \"westd-29022\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-29022\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-19T21:22:39.744Z\"}, \"spec\": {\"command\": \"python src/cka_stability_analysis.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --output_path /root/autodl-tmp/recovery_aware_struct_prune/cka_stability_results.json --device cuda:0\", \"server\": \"westd-29022\", \"gpu\": \"cuda:3\", \"pid\": 143187, \"data_path\": \"openai/gsm8k\", \"data_count\": 1024, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/cka_stability_results.json\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/cka_stability_results.json\"}, \"metrics\": {\"spearman_256v512_attn\": 0.989, \"spearman_256v512_mlp\": 0.9683, \"spearman_256v512_combined\": 0.9788, \"spearman_256v1024_attn\": 0.9762, \"spearman_256v1024_mlp\": 0.9464, \"spearman_256v1024_combined\": 0.9641, \"spearman_512v1024_attn\": 0.995, \"spearman_512v1024_mlp\": 0.9908, \"spearman_512v1024_combined\": 0.9938, \"min_combined_rho\": 0.964, \"mean_combined_rho\": 0.979, \"stable\": true}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T22:21:53.771Z\"}, \"eval_mbpp_sft_standard_20_1p5b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T18:56:15.766Z\", \"updated_at\": \"2026-05-19T21:57:06.135Z\", \"hypothesis\": \"1.5B SFT Standard 20% MBPP pass@1 @2048. 与 westb:1 同时跑的 1.5B SFT CKA-only MBPP 对比，验证 recovery gradient 在 1.5B scale 上的 MBPP 表现。预期 CKA-only > Standard，与 7B GSM8K 跨 scale 一致。关联 C2。\", \"parent\": \"eval_mbpp_sft_standard_20\", \"spec\": {\"command\": \"python src/eval_mbpp.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_sft_standard_20_1p5b.json\", \"server\": \"westb-23072\", \"gpu\": \"0\", \"model_name\": \"sft_standard_20_1p5b\", \"checkpoint_source\": \"sft_standard_20_1p5b\", \"eval_data\": \"mbpp\", \"data_path\": \"mbpp\", \"data_count\": 0, \"seed\": 0}, \"conclusion\": \"success\", \"metrics\": {\"pass_at_1\": 0.008021, \"n_correct\": 3, \"n_total\": 374, \"stderr\": 0.004613, \"avg_response_length\": 1658.6, \"median_response_length\": 2048}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_sft_standard_20_1p5b.json\", \"completed_at\": \"2026-05-19T21:57:06.135Z\"}, \"eval_mbpp_grpo_rasp_20\": {\"status\": \"DONE\", \"retry_count\": 2, \"created_at\": \"2026-05-19T18:18:35.729Z\", \"updated_at\": \"2026-05-19T21:55:32.779Z\", \"hypothesis\": \"MBPP pass@1 eval on GRPO RASP 20% model @2048. Dense baseline=53.48% (200/374). RASP GRPO GSM8K=60.88%, HumanEval=10.37%. Tests RASP GRPO code generation on MBPP. Completes MBPP 3×2 matrix. Expected: between CKA-only GRPO (14.17%) and Standard GRPO (running). Recovery gradient on MBPP validates C2 capability breadth claim on second code benchmark.\", \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"completed_at\": \"2026-05-19T18:24:28.539Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T18:24:39.007529+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T18:33:14.502436+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T21:52:57.836056+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"失败原因: 进程在加载 MBPP 数据集时被 SIGHUP (EXIT_CODE=129) 终止。模型 /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair 加载成功，非代码/路径问题。疑似资源竞争或外部信号。待诊断后重试。\"}}, \"notes\": \"第3次失败: EXIT_CODE=129 (SIGHUP) 进程在加载 MBPP 数据集时被终止。模型加载成功。与 eval_mbpp_sft_standard_20 (SIGTERM 143)、eval_mbpp_grpo_standard_20 (timeout 124) 同一模式——submit_training_job 框架的信号管理导致。需要手动 tmux + HF_DATASETS_OFFLINE=1 绕过。将创建 v2 重试。\", \"reproduce\": {\"finished_at\": \"2026-05-19T21:52:49.258Z\"}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 python src/eval_mbpp.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_grpo_rasp_20.json\\\"\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:1\"], \"pid\": \"127964\", \"data_path\": \"MBPP\", \"data_count\": 374, \"model_name\": \"grpo_stage2_rasp_20_fair\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair\", \"eval_data\": \"MBPP (374 tasks, sanitized, pass@1, max_new_tokens=2048)\"}, \"conclusion\": \"success\", \"metrics\": {\"pass_at_1\": 0.131, \"n_correct\": 49, \"n_total\": 374, \"stderr\": 0.0174}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_grpo_rasp_20.json\", \"log_path\": \"/root/autodl-tmp/logs/eval_mbpp_grpo_rasp_20.log\"}, \"eval_mbpp_sft_rasp_20\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-19T18:18:34.640Z\", \"updated_at\": \"2026-05-19T21:08:00.610Z\", \"hypothesis\": \"SFT RASP 20% model retains more MBPP code generation capability than CKA-only pruning due to recovery-aware pruning preserving structurally important parameters\", \"server\": \"westd-29022\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"westb-23072\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-19T18:19:54.269Z\", \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/eval_mbpp.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_sft_rasp_20.json\\\"\", \"code_commit\": \"39afb8c6309aad601973b2b3cd6b4f1a8a3b0b6c\", \"finished_at\": \"2026-05-19T21:05:26.016Z\", \"training_hours\": 2.76}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"completed_at\": \"2026-05-19T18:21:31.440Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T18:21:37.020361+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T21:05:32.937237+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"Model not found on westb. 7B SFT RASP checkpoint is on westd (sft_rasp_20_westd), not westb. Need to rerun on westd when GPU available.\"}}, \"notes\": \"Model not found on westb. 7B SFT RASP checkpoint is on westd (sft_rasp_20_westd), not westb. Need to rerun on westd when GPU available.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/eval_mbpp.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_sft_rasp_20.json\\\"\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:3\"], \"pid\": \"133674\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_mbpp_sft_rasp_20.log\", \"submitted_at\": \"2026-05-19T20:00:13.578Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd\", \"wall_clock_seconds\": 4067.0, \"gpu_hours\": 1.13}, \"pid\": \"133674\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_mbpp_sft_rasp_20.log\", \"conclusion\": \"success\", \"metrics\": {\"pass_at_1\": 0.1176, \"stderr\": 0.0167, \"n_correct\": 44, \"n_total\": 374, \"dense_baseline_pass_at_1\": 0.5348, \"degradation_pct\": 78.01, \"avg_response_length\": 810.7, \"median_response_length\": 247}}, \"eval_mbpp_sft_cka_only_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T17:20:00.596Z\", \"updated_at\": \"2026-05-19T19:58:30.970Z\", \"hypothesis\": \"MBPP pass@1 eval on SFT CKA-only 20% model. Dense baseline=53.48% (200/374). CKA-only preserves most code generation capability after pruning. Compare SFT vs GRPO on MBPP to test redistribution hypothesis on second code benchmark.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python src/eval_mbpp.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/mbpp_sft_cka_only_20.json\", \"server\": \"westd-29022\", \"gpu\": \"cuda:3\", \"pid\": 123029, \"log_path\": \"/tmp/eval_mbpp_sft_cka_only_20.log\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20\", \"eval_data\": \"MBPP sanitized (374 tasks)\", \"data_path\": \"google-research-datasets/mbpp (sanitized)\", \"data_count\": 374, \"model_name\": \"Qwen2.5-7B-pruned-20%-SFT-CKA-only\", \"seed\": 42}, \"conclusion\": \"success\", \"metrics\": {\"pass_at_1\": 0.1283, \"stderr\": 0.0173, \"n_correct\": 48, \"n_total\": 374, \"dense_baseline_pass_at_1\": 0.5348, \"degradation_pct\": 76.01, \"avg_response_length\": 643.8, \"median_response_length\": 363.5}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20\", \"log_path\": \"/tmp/eval_mbpp_sft_cka_only_20.log\", \"completed_at\": \"2026-05-19T19:58:30.970Z\"}, \"eval_humaneval_sft_rasp_20_1p5b_2048\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-19T11:35:50.597Z\", \"updated_at\": \"2026-05-19T18:52:30.545Z\", \"hypothesis\": \"1.5B SFT RASP HumanEval pass@1 @2048. Cross-scale validation. 7B GRPO RASP: 10.98%. RASP pruning expected between Standard and CKA-only on code generation at 1.5B scale.\", \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"completed_at\": \"2026-05-19T17:41:24.131Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_1p5b --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_rasp_20_1p5b_2048.json --seed 42\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:0\"], \"pid\": \"909411\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_1p5b\", \"eval_data\": \"HumanEval\", \"model_name\": \"Qwen2.5-1.5B-pruned-rasp-20-SFT\", \"metrics\": {\"pass_at_1\": 0, \"stderr\": 0, \"n_passed\": 0, \"n_total\": 164}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_rasp_20_1p5b_2048.json\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_humaneval_sft_rasp_20_1p5b_2048.log\"}, \"conclusion\": \"success\", \"metrics\": {\"pass_at_1\": 0, \"n_correct\": 0, \"n_total\": 164, \"note\": \"1.5B SFT RASP, all truncated at 2048 tokens\"}}, \"eval_mbpp_grpo_cka_only_20\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-19T14:41:07.213Z\", \"updated_at\": \"2026-05-19T18:17:54.178Z\", \"hypothesis\": \"MBPP pass@1 eval on GRPO CKA-only 20% model @2048. Dense baseline=53.48% (200/374). CKA-only GRPO showed strongest recovery on GSM8K (64.37%) and HumanEval (20.12%). If MBPP follows same pattern (CKA-only > Standard > RASP), confirms capability breadth claim (C2) generalizes to second code benchmark. Compare with parallel eval_mbpp_grpo_standard_20 and eval_mbpp_sft_cka_only_20.\", \"completed_at\": \"2026-05-19T17:21:48.228Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"negative\", \"metrics\": {\"pass_at_1\": 0.1417, \"n_correct\": 53, \"n_total\": 374, \"stderr\": 0.018, \"note\": \"Result extracted from log; JSON save failed due to disk full\"}}, \"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T18:08:24.415449+00:00\"}]}, \"server\": \"westb-23072\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westb-23072\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-19T18:06:40.359Z\", \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 python src/eval_mbpp.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_grpo_cka_only_20.json\\\"\", \"code_commit\": \"e6ce5f70bb3b993ba8964f0ea62d2f6001155551\", \"finished_at\": \"2026-05-19T18:08:15.493Z\", \"training_hours\": 0.03}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 python src/eval_mbpp.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_grpo_cka_only_20.json\\\"\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:1\"], \"pid\": \"unknown\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_mbpp_grpo_cka_only_20.log\", \"submitted_at\": \"2026-05-19T18:08:02.259Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 17.3, \"gpu_hours\": 0.0}, \"pid\": \"unknown\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_mbpp_grpo_cka_only_20.log\", \"failure_reason\": \"EXIT_CODE=2 (shell misuse / syntax)\", \"conclusion\": \"success\", \"metrics\": {\"pass_at_1\": 0.1417, \"n_correct\": 53, \"n_total\": 374, \"stderr\": 0.018}}, \"eval_gsm8k_grpo_shortgpt_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T17:19:18.419Z\", \"updated_at\": \"2026-05-19T18:17:53.164Z\", \"hypothesis\": \"GSM8K eval on ShortGPT GRPO checkpoint-100. ShortGPT SFT=44.73%, if GRPO improves significantly it suggests depth-pruned models can still benefit from RL. If minimal improvement or collapse, confirms coarse layer removal limits GRPO recovery capacity vs fine-grained methods (CKA-only 64.37%, Standard 59.44%).\", \"parent\": \"grpo_shortgpt_20\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_shortgpt_20/checkpoint-100 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/gsm8k_grpo_shortgpt_20.json\", \"server\": \"westd-29022\", \"gpu\": \"cuda:0\", \"pid\": 122867, \"data_path\": \"gsm8k test set\", \"data_count\": 1319, \"model_name\": \"grpo_shortgpt_20/checkpoint-100\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_shortgpt_20/checkpoint-100\", \"eval_data\": \"gsm8k_test\", \"log_path\": \"/tmp/eval_gsm8k_grpo_shortgpt_20.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_shortgpt_20/checkpoint-100\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T18:17:50.692Z\", \"metrics\": {\"gsm8k_accuracy\": 43.37, \"n_correct\": 572, \"n_total\": 1319, \"stderr\": 0.0136}}, \"eval_gsm8k_sft_shortgpt_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T15:47:16.122Z\", \"updated_at\": \"2026-05-19T18:03:15.831Z\", \"hypothesis\": \"ShortGPT SFT checkpoint GSM8K eval. After depth pruning (5/28 layers removed by Block Influence scoring) + SFT warmup (loss=0.62, token_accuracy=0.83), measure GSM8K accuracy. Compare with fine-grained pruning SFT results: CKA-only SFT ~60%, Standard SFT ~64%. ShortGPT expected lower due to coarse layer removal destroying more representations.\", \"parent\": \"sft_shortgpt_20\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_shortgpt_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/gsm8k_sft_shortgpt_20.json\", \"server\": \"westd-29022\", \"data_path\": \"gsm8k:test\", \"data_count\": 1319, \"model_name\": \"Qwen2.5-7B-ShortGPT-20pct-SFT\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_shortgpt_20/\", \"eval_data\": \"gsm8k:test\"}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T17:41:33.038Z\", \"metrics\": {\"gsm8k_accuracy\": 44.73, \"n_correct\": 590, \"n_total\": 1319}}, \"sft_shortgpt_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T14:22:26.084Z\", \"updated_at\": \"2026-05-19T18:02:48.590Z\", \"hypothesis\": \"ShortGPT depth pruning (20%, 5/28 layers removed) after SFT warmup will show lower recovery capacity than fine-grained structural pruning methods (Standard/CKA-only/RASP) because coarse layer removal destroys more distributed representations needed for GRPO recovery. Layers removed: [15,16,17,24,25], actual param sparsity 15.30%.\", \"spec\": {\"command\": \"python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/shortgpt_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_shortgpt_20 --gpu 3 --num_train_epochs 2 --learning_rate 2e-5 --batch_size 1 --gradient_accumulation_steps 8 --max_seq_length 2048 --logging_steps 10 --seed 42\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:3\"], \"pid\": \"112015\", \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_shortgpt_20.log\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"openai/gsm8k\", \"data_count\": 7473, \"model_name\": \"shortgpt_20\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/shortgpt_20\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_shortgpt_20\"}, \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T17:41:29.305Z\"}, \"eval_gsm8k_grpo_cka_only_20_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T17:47:34.008Z\", \"updated_at\": \"2026-05-19T17:48:24.627Z\", \"hypothesis\": \"GSM8K eval on GRPO CKA-only 20% seed123 checkpoint. Tests reproducibility of CKA-only GRPO GSM8K performance (original seed42 = 64.37%). If seed123 matches closely, confirms CKA-only GRPO advantage is robust across seeds.\", \"parent\": \"grpo_cka_only_20_seed123\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_seed123 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/gsm8k_grpo_cka_only_20_seed123.json\", \"server\": \"westb-23072\", \"gpu\": \"cuda:1\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_seed123.log\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_seed123\", \"eval_data\": \"gsm8k_test\", \"data_path\": \"gsm8k test set\", \"data_count\": 1319, \"model_name\": \"grpo_cka_only_20_seed123\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_seed123\"}, \"metrics\": {\"accuracy\": 0.6422, \"stderr\": 0.0132, \"n_correct\": 847, \"n_total\": 1319, \"eos_rate\": 0.9909, \"avg_response_length\": 195.97, \"natural_eos\": 1307, \"truncated\": 12}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T17:48:24.627Z\"}, \"eval_humaneval_grpo_standard_20_1p5b_2048\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T11:35:48.029Z\", \"updated_at\": \"2026-05-19T17:02:50.370Z\", \"hypothesis\": \"1.5B GRPO Standard HumanEval pass@1 @2048. Cross-scale validation baseline. 7B GRPO Standard HumanEval failed (multiple attempts). If 1.5B Standard also shows weak code generation after GRPO (vs CKA-only), strengthens claim that standard pruning loses broader capabilities.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_1p5b --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_standard_20_1p5b_2048.json --seed 42\", \"server\": \"westb-23072\", \"gpu\": \"cuda:0\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_1p5b\", \"eval_data\": \"HumanEval\", \"model_name\": \"Qwen2.5-1.5B-pruned-standard-20-GRPO\", \"tmux_session\": \"eval_humaneval_grpo_standard_1p5b\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_1p5b\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_standard_20_1p5b_2048.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T17:02:50.370Z\"}, \"gradient_flow_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T15:03:16.535Z\", \"updated_at\": \"2026-05-19T16:38:41.269Z\", \"hypothesis\": \"CKA-only pruned models exhibit significantly stronger gradient signals (per-layer L2 norm) compared to Standard and RASP, with statistical significance (Wilcoxon p<0.05). This gradient magnitude difference is consistent with CKA-only's superior GRPO recovery capacity.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python src/gradient_flow_analysis.py --model_paths pruned_cka_only_20 pruned_standard_20 pruned_rasp_20 --model_names CKA-only Standard RASP --n_steps 200 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/results/gradient_flow_v3 --seed 42\", \"server\": \"westb-23072\", \"gpu\": \"cuda:0\", \"pid\": \"901553\", \"data_path\": \"openai/gsm8k train split\", \"data_count\": 200, \"model_name\": \"pruned_cka_only_20 + pruned_standard_20 + pruned_rasp_20\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/gradient_flow_v3/\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/gradient_flow_v3.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T15:18:53.782Z\", \"metrics\": {\"cka_only_mean_grad_norm\": 0.3229, \"standard_mean_grad_norm\": 0.1118, \"rasp_mean_grad_norm\": 0.1431, \"cka_vs_standard_ratio\": 2.89, \"rasp_vs_standard_ratio\": 1.28, \"cka_vs_standard_significant_layers\": \"55/56\", \"cka_vs_rasp_significant_layers\": \"56/56\", \"rasp_vs_standard_significant_layers\": \"45/56\", \"rasp_vs_standard_nonsig_layers\": \"layer_18_mlp,layer_19_attn,layer_19_mlp,layer_20_attn,layer_20_mlp,layer_21_attn,layer_21_mlp,layer_22_attn,layer_24_mlp,layer_27_attn,layer_27_mlp\", \"n_samples\": 200, \"statistical_test\": \"Wilcoxon signed-rank, per-layer\", \"bootstrap_n\": 1000, \"seed\": 42}}, \"eval_gsm8k_grpo_rasp_20_fair\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T12:47:37.399Z\", \"updated_at\": \"2026-05-19T16:17:16.053Z\", \"hypothesis\": \"GRPO RASP 20% fair (v5 config) GSM8K 全量评估。RASP 结合 recovery-awareness 与 structural pruning，预期性能介于 Standard (59.44%) 和 CKA-only (64.37%) 之间。若 RASP ≈ Standard，说明 recovery-awareness 的增益主要来自 CKA 信号而非 RASP 的混合策略。N=1319。\", \"parent\": \"eval_gsm8k_grpo_standard_20_fair_v2\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair --max_samples 1319 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_rasp_20_fair.json\", \"server\": \"westd-29022\", \"data_path\": \"GSM8K\", \"data_count\": 1319, \"model_name\": \"grpo_stage2_rasp_20_fair\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair\", \"eval_data\": \"GSM8K\", \"gpu\": [\"cuda:0\"], \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_rasp_20_fair.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T15:28:58.925Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T15:29:02.102Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T15:29:07.839181+00:00\"}]}, \"metrics\": {\"accuracy\": 0.6088, \"stderr\": 0.0134, \"n_correct\": 803, \"n_total\": 1319, \"eos_rate\": 0.9879, \"avg_response_length\": 195.7}, \"notes\": \"Cron false positive: eval脚本不走W&B误判failed。实际 accuracy=60.88% (803/1319)。RASP 介于 Standard (59.44%) 和 CKA-only (64.37%) 之间，更靠近 Standard。RASP-Standard gap=1.44pp, CKA-RASP gap=3.49pp。recovery-awareness 增益主要来自 CKA 信号。\"}, \"eval_mbpp_dense_unpruned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T13:47:53.814Z\", \"updated_at\": \"2026-05-19T16:17:00.452Z\", \"hypothesis\": \"Dense unpruned DeepSeek-R1-Distill-Qwen-7B MBPP pass@1 baseline @2048. Establishes ceiling performance for MBPP code generation. All pruned models' MBPP results will be compared against this baseline.\", \"spec\": {\"server\": \"westd-29022\", \"gpu\": [\"cuda:2\"], \"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=2 /root/miniconda3/bin/python src/eval_mbpp.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_dense_unpruned.json'\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_mbpp_dense_unpruned.log\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"MBPP\", \"data_count\": 374, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B\", \"eval_data\": \"MBPP (374 tasks, sanitized, pass@1, max_new_tokens=2048)\", \"checkpoint_path\": \"/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B\", \"pid\": \"108291\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T16:14:39.089Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T16:14:42.070Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T16:14:46.802899+00:00\"}]}, \"metrics\": {\"pass_at_1\": 0.5348, \"stderr\": 0.0258, \"n_correct\": 200, \"n_total\": 374}, \"notes\": \"Cron false positive: eval脚本不走W&B，进程正常退出后cron检测不到指标误判failed。实际 pass@1=53.48% (200/374), stderr=0.0258。Dense baseline for MBPP.\"}, \"eval_humaneval_sft_rasp_20_2048_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T13:18:20.664Z\", \"updated_at\": \"2026-05-19T15:47:14.846Z\", \"hypothesis\": \"SFT RASP 20% HumanEval pass@1 @2048. Fills RASP SFT cell in HumanEval matrix. GRPO RASP = 10.98%. If SFT RASP ≈ GRPO RASP, confirms redistribution-not-expansion pattern holds for RASP too. Compare with CKA-only SFT=GRPO=20.12%.\", \"parent\": \"eval_humaneval_sft_rasp_20_2048\", \"spec\": {\"server\": \"westd-29022\", \"gpu\": \"cuda:1\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_sft_rasp_20_2048_v2.json\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"sft_rasp_20_westd\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd\", \"eval_data\": \"HumanEval\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_sft_rasp_20_2048_v2.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_sft_rasp_20_2048_v2.json\", \"pid\": \"107932\"}, \"conclusion\": \"success\", \"metrics\": {\"pass_at_1\": 0.1037, \"stderr\": 0.0238, \"n_correct\": 17, \"n_total\": 164, \"avg_response_length\": 1253.7, \"median_response_length\": 2048}, \"completed_at\": \"2026-05-19T14:36:48.406Z\"}, \"grpo_cka_only_20_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T09:27:11.294Z\", \"updated_at\": \"2026-05-19T15:21:17.415Z\", \"hypothesis\": \"Multi-seed validation (seed=123) of CKA-only 20% GRPO training. If CKA-only advantage holds across seeds, strengthens C1 claim that pruning criteria determine recovery capacity. Seed 42 result: 64.37% GSM8K.\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 python src/grpo_train.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_cka_only_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_seed123 --num_train_steps 100 --seed 123'\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:1\"], \"pid\": \"857962\", \"data_path\": \"gsm8k\", \"data_count\": 7473, \"model_name\": \"pruned_cka_only_20\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_seed123\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/grpo_cka_only_20_seed123.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T15:21:11.189Z\", \"metrics\": {\"train_loss\": 0.1361, \"final_step_loss\": 0.05054, \"final_reward\": 0.2975, \"final_reward_std\": 0.4097, \"train_steps\": 100, \"train_runtime_hours\": 11.63, \"wandb_run\": \"j8kn0sqd\"}}, \"gradient_flow_analysis\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T14:44:25.606Z\", \"updated_at\": \"2026-05-19T14:45:13.584Z\", \"hypothesis\": \"CKA-only pruned models exhibit stronger gradient flow (higher per-layer gradient norms) compared to Standard pruned models, enabling more effective GRPO recovery. Standard pruning creates weaker gradient signals that limit training effectiveness.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python src/gradient_flow_analysis.py --model_paths pruned_cka_only_20 pruned_standard_20 --model_names CKA-only Standard --n_steps 20 --seed 42\", \"server\": \"westb-23072\", \"data_path\": \"openai/gsm8k (cached)\", \"data_count\": 20, \"model_name\": \"Qwen2-7B pruned variants\", \"seed\": 42, \"checkpoint_path\": \"N/A (analysis only)\", \"log_path\": \"/tmp/gradient_flow.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T14:45:06.578Z\", \"metrics\": {\"cka_only_attn_grad_mean\": 0.3135, \"cka_only_attn_grad_cv\": 1.2231, \"cka_only_mlp_grad_mean\": 0.285, \"cka_only_mlp_grad_cv\": 1.2424, \"standard_attn_grad_mean\": 0.1316, \"standard_attn_grad_cv\": 1.1363, \"standard_mlp_grad_mean\": 0.1222, \"standard_mlp_grad_cv\": 1.1489, \"grad_magnitude_ratio_attn\": 2.38, \"grad_magnitude_ratio_mlp\": 2.33}}, \"cka_calibration_stability_ablation\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T14:21:15.548Z\", \"updated_at\": \"2026-05-19T14:32:43.647Z\", \"hypothesis\": \"CKA-based functional overlap scores F(h) are stable across calibration sizes (256/512/1024 samples), with Spearman rho > 0.95 between any two sizes. This validates that our pruning criterion is not sensitive to calibration hyperparameter.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python src/run_cka_reliability.py --original_model /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --pruned_model /root/autodl-tmp/recovery_aware_struct_prune/pruned_cka_only_20 --num_samples 1024 --n_splits 5 --max_length 512 --output /root/autodl-tmp/recovery_aware_struct_prune/results/cka_reliability_ablation.json --seed 42\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:0\"], \"pid\": \"cka_reliability\", \"data_path\": \"GSM8K calibration subset\", \"data_count\": 1024, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B + pruned_cka_only_20\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/cka_reliability_ablation.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/cka_reliability_ablation.json\", \"backend\": \"tmux\", \"account\": \"root\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T14:30:36.155Z\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T14:30:39.149Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T14:30:46.615642+00:00\"}]}, \"metrics\": {\"split_half_rho\": 0.9932, \"n_splits\": 5, \"size_sensitivity_128\": 0.982, \"size_sensitivity_256\": 0.989, \"size_sensitivity_512\": 0.995}}, \"eval_humaneval_grpo_standard_20_fair_2048_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T07:05:14.343Z\", \"updated_at\": \"2026-05-19T14:20:25.129Z\", \"hypothesis\": \"GRPO stage2 with standard 20% fair pruning recovers meaningful code generation ability on HumanEval, demonstrating that the fair pruning strategy preserves code-critical layers better than CKA-only pruning.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair --max_new_tokens 2048\", \"server\": \"westd-29022\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_grpo_standard_20_fair_2048_v3.log\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"grpo_stage2_standard_20_fair\", \"seed\": 42}, \"notes\": \"2026-05-19 19:06 progress check: 156/164 (95.1%), interim pass@1 ~0.1143 at problem 140. ~15min remaining.\", \"reproduce\": {\"finished_at\": \"2026-05-19T11:24:53.134Z\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T11:24:55.932Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T11:25:06.462224+00:00\"}]}, \"metrics\": {\"pass_at_1\": 0.1098, \"n_correct\": 18, \"n_total\": 164}}, \"eval_humaneval_sft_cka_only_20_2048_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T09:27:07.470Z\", \"updated_at\": \"2026-05-19T13:22:29.762Z\", \"hypothesis\": \"SFT CKA-only HumanEval v2 (PATH bug 修复版重跑)，验证 v1 的 0% 是否为假结果。v1 因 eval_humaneval.py 用裸 python 导致 164 题全部 sandbox 失败。修复后用 sys.executable 重跑。\", \"parent\": \"eval_humaneval_sft_cka_only_20_2048\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_sft_cka_only_20_2048_v2.json'\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:1\"], \"pid\": \"78740\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"sft_cka_only_20\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20\", \"eval_data\": \"HumanEval (164 problems, pass@1, max_new_tokens=2048, sys.executable fix)\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T11:13:52.207Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T11:13:55.007Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T11:13:59.644866+00:00\"}]}, \"metrics\": {\"pass_at_1\": 20.12, \"n_correct\": 33, \"n_total\": 164}, \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_sft_cka_only_20_2048_v2.json\"}, \"eval_math500_grpo_cka_only_20_2048\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:36:14.421Z\", \"updated_at\": \"2026-05-19T13:08:18.617Z\", \"hypothesis\": \"GRPO CKA-only 20% MATH-500 accuracy with explicit max_new_tokens=2048. Re-eval for fair C1 OOD comparison: previous eval (26.6%) did not specify max_new_tokens. SFT CKA-only @2048 = 29.0%. If GRPO < SFT on MATH-500, C1 decoupling shows GRPO benefit is benchmark-dependent.\", \"parent\": \"eval_math500_grpo_cka_only_20\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=2 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/math500_grpo_cka_only_20_2048.json --max_new_tokens 2048'\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:2\"], \"pid\": \"36703\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/math500_grpo_cka_only_20_2048.log\", \"submitted_at\": \"2026-05-18T23:23:59.014Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"grpo_cka_only_20\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20\", \"eval_data\": \"MATH-500\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20\", \"wall_clock_seconds\": 49459.6, \"gpu_hours\": 13.74}, \"reproduce\": {\"finished_at\": \"2026-05-19T03:07:45.553Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T03:07:51.024172+00:00\"}]}, \"metrics\": {\"accuracy\": 0.292, \"n_correct\": 146, \"n_total\": 500}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T13:08:18.617Z\"}, \"eval_gsm8k_sft_standard_20_1p5b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T18:10:55.912Z\", \"updated_at\": \"2026-05-19T13:07:57.786Z\", \"hypothesis\": \"1.5B Standard post-SFT GSM8K accuracy (N=1319). SFT baseline for computing GRPO delta on Standard pruning at 1.5B scale. Compare with GRPO Standard 1.5B (22.29%) to quantify GRPO benefit. Completes 3-method SFT vs GRPO comparison at 1.5B.\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_standard_20_1p5b.json'\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:1\"], \"pid\": \"842784\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_sft_standard_20_1p5b.log\", \"submitted_at\": \"2026-05-18T23:02:19.301Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Qwen2.5-1.5B-sft-standard-20\", \"checkpoint_source\": \"sft_standard_20_1p5b\", \"eval_data\": \"gsm8k\", \"data_path\": \"gsm8k\", \"data_count\": 1319, \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b\", \"wall_clock_seconds\": 50738.5, \"gpu_hours\": 14.09}, \"reproduce\": {\"finished_at\": \"2026-05-19T03:18:37.549Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T03:18:43.249877+00:00\"}]}, \"metrics\": {\"accuracy\": 0.22896133434420016, \"n_correct\": 302, \"n_total\": 1319}, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_sft_standard_20_1p5b.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T13:07:57.786Z\"}, \"eval_gsm8k_grpo_standard_20_fair_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T09:27:09.334Z\", \"updated_at\": \"2026-05-19T12:47:36.437Z\", \"hypothesis\": \"验证 Standard GRPO fair (v5 config: beta=0.01, temp=0.4, maxlen=1024, DAPO, lr=1e-6) 的 GSM8K 准确率。替换 phantom 58.91% (从未被实际验证过的数字)。使用 grpo_stage2_standard_20_fair checkpoint, N=1319。\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair --max_samples 1319 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_standard_20_fair_v2.json'\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:0\"], \"pid\": \"83299\", \"data_path\": \"GSM8K\", \"data_count\": 1319, \"model_name\": \"grpo_stage2_standard_20_fair\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair\", \"eval_data\": \"GSM8K (1319 samples)\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T12:37:12.256Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T12:37:14.980Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T12:37:19.684680+00:00\"}]}, \"metrics\": {\"accuracy\": 59.44, \"n_correct\": 784, \"n_total\": 1319}}, \"eval_humaneval_grpo_rasp_20_fair_2048\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T06:38:59.146Z\", \"updated_at\": \"2026-05-19T09:44:43.320Z\", \"hypothesis\": \"HumanEval pass@1 for GRPO RASP 20% (fair model) with max_new_tokens=2048. Fair model trained with same setup as Standard/CKA-only for unbiased comparison on code generation.\", \"parent\": \"grpo_stage2_rasp_20_fair\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_grpo_rasp_20_fair_2048.json\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:3\"], \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_grpo_rasp_20_fair_2048.log\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"grpo_stage2_rasp_20_fair\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair\", \"eval_data\": \"HumanEval\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T09:40:10.950Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T09:40:16.316Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T09:40:25.969149+00:00\"}]}, \"metrics\": {\"pass_at_1\": 0.1098, \"n_correct\": 18, \"n_total\": 164, \"stderr\": 0.0244, \"avg_response_length\": null}}, \"eval_gsm8k_grpo_unstructured_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T04:46:38.286Z\", \"updated_at\": \"2026-05-19T08:05:04.224Z\", \"hypothesis\": \"GSM8K accuracy for GRPO-recovered unstructured 20% pruned model. Pre-GRPO baseline was 87.87%. Compare with structured GRPO results (CKA-only 64.37%, Standard 58.91%, RASP 56.71%) to quantify structured vs unstructured recovery dynamics.\", \"parent\": \"grpo_unstructured_20\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_unstructured_20/checkpoint-100 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_unstructured_20.json\", \"server\": \"westb-23072\", \"data_path\": \"gsm8k test set\", \"data_count\": 1319, \"model_name\": \"grpo_unstructured_20/checkpoint-100\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_unstructured_20/checkpoint-100\", \"eval_data\": \"gsm8k_test\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.8764, \"n_correct\": 1156, \"n_total\": 1319, \"stderr\": 0.00906, \"eos_rate\": 0.9818, \"truncated\": 24, \"avg_response_length\": 600}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_unstructured_20/checkpoint-100\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_unstructured_20.json\", \"completed_at\": \"2026-05-19T08:05:04.224Z\"}, \"eval_humaneval_grpo_cka_only_20_2048\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T04:11:28.637Z\", \"updated_at\": \"2026-05-19T07:36:55.239Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20 --max_new_tokens 2048\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:1\"], \"pid\": \"66521\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_humaneval_grpo_cka_only_20_2048.log\", \"submitted_at\": \"2026-05-19T04:11:28.118Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"grpo_cka_only_20\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20\", \"eval_data\": \"HumanEval\", \"wall_clock_seconds\": 12309.1, \"gpu_hours\": 3.42}, \"reproduce\": {\"finished_at\": \"2026-05-19T07:32:48.290Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T07:32:52.921144+00:00\"}]}, \"hypothesis\": \"GRPO recovery training on CKA-only 20% pruned model recovers code generation ability on HumanEval from SFT baseline of 0% pass@1, because CKA-only preserves structural similarity that GRPO can exploit for cross-task recovery\", \"parent\": \"grpo_cka_only_20\", \"metrics\": {\"pass_at_1\": 0.2012, \"n_correct\": 33, \"n_total\": 164, \"stderr\": 0.0313, \"avg_response_length\": 1523.31, \"median_response_length\": 2048, \"wall_clock_seconds\": 11933}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_grpo_cka_only_20_2048.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T07:36:37.174Z\"}, \"grpo_standard_20_fair\": {\"created_at\": \"2026-05-18T01:05:44.644Z\", \"hypothesis\": \"GRPO recovery training on standard-pruned 20% model (fair v5 config: beta=0.01, dapo loss, format_reward=0.1, temp=0.4, rep_penalty=1.15, adamw_bnb_8bit). Tests whether standard pruning + GRPO can recover GSM8K reasoning. Part of 4-method fair comparison (CKA-only, Standard, RASP, Random) under identical GRPO v4 config.\", \"parent\": \"grpo_rasp_20_fair\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"sft_standard_20_westd\", \"command\": \"bash -c \\\"export HF_HOME=/root/autodl-tmp/.hf_cache && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/recovery_aware_struct_prune && python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_westd --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair --gpu 0 --max_completion_length 1024 --beta 0.01 --temperature 0.4 --repetition_penalty 1.15 --format_reward_weight 0.1 --gradient_checkpointing true --optim adamw_bnb_8bit --loss_type dapo --learning_rate 1e-6 --max_steps 100 --save_total_limit 3 --save_steps 10 --reward_desert_patience 200 --run_name grpo_standard_20_fair\\\"\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k (GRPO training)\", \"eval_data\": \"N/A (GRPO training, not eval)\", \"gpu\": [\"cuda:0\"], \"hyperparams\": {\"beta\": 0.01, \"format_reward_weight\": 0.1, \"loss_type\": \"dapo\", \"lr\": 1e-06, \"max_completion_length\": 1024, \"max_steps\": 100, \"optim\": \"adamw_bnb_8bit\", \"repetition_penalty\": 1.15, \"reward_desert_patience\": 200, \"save_steps\": 10, \"save_total_limit\": 3, \"temperature\": 0.4}, \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_standard_20_fair.log\", \"model_name\": \"sft_standard_20_westd\", \"pid\": \"74224\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-18T01:05:44.210Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 3631.9, \"gpu_hours\": 1.01}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T06:39:34.930Z\", \"reproduce\": {\"finished_at\": \"2026-05-18T02:00:43.663Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T02:00:50.834061+00:00\"}]}, \"metrics\": {\"wandb_run_id\": \"tyv20u2k\", \"total_steps\": 100, \"runtime_seconds\": 3017, \"reward_trajectory\": [0.051, 0.056, 0.067, 0.081, 0.019, 0.043, 0.047, 0.046, 0.031, 0.054], \"frac_zero_std_trajectory\": [0.5, 0.625, 0.5, 0.5, 0.575, 0.55, 0.575, 0.55, 0.55, 0.55], \"peak_reward\": 0.081, \"peak_reward_step\": 40, \"final_reward\": 0.054, \"final_frac_zero_std\": 0.55, \"dynamics_pattern\": \"dip_then_partial_recovery\", \"dip_step\": 50, \"dip_reward\": 0.019}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_standard_20_fair.log\", \"conclusion\": \"success\", \"notes\": \"Standard shows stagnation pattern: reward flat 0.03-0.08 全程无上升趋势, frac_zero_std stuck 0.5-0.55. 比 RASP (permanent collapse to 0.01 reward, frac_zero_std→0.85) 略好但也未恢复. 4-way gradient confirmed: CKA-only (active recovery) > Random (plateau) > Standard (stagnation) > RASP (permanent collapse). D058 fair comparison 完成.\", \"completed_at\": \"2026-05-18T02:06:16.075Z\"}, \"inference_bench_clean_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T01:42:25.421Z\", \"updated_at\": \"2026-05-19T02:44:07.178Z\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=3 python src/measure_inference_speed.py --models original:/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B pruned_cka_only_20:/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20 pruned_standard_20:/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/inference_bench_clean_v2.json --n_prompts 50 --max_new_tokens 256'\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:3\"], \"pid\": \"56892\", \"log_path\": \"~/runs/recovery_aware_struct_prune/inference_bench_clean_v2.log\", \"submitted_at\": \"2026-05-19T01:42:24.921Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Dense + CKA-only 20% + Standard 20%\", \"data_path\": \"gsm8k test (50 prompts)\", \"data_count\": 50, \"seed\": 42, \"checkpoint_path\": \"N/A (benchmark)\", \"wall_clock_seconds\": 3702.3, \"gpu_hours\": 1.03}, \"hypothesis\": \"Clean inference benchmark (Dense + CKA-only 20% + Standard 20%) on isolated GPU. Previous plan_016 benchmark was polluted by GPU contention. Measures per-token throughput and latency for speedup claims. 50 prompts x 256 max_new_tokens, GSM8K test set.\", \"reproduce\": {\"finished_at\": \"2026-05-19T01:55:27.662Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T01:55:33.007338+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"original_tps\": 72.02, \"cka_only_20_tps\": 58.28, \"standard_20_tps\": 58.25, \"cka_only_20_speedup\": 0.809, \"standard_20_speedup\": 0.809, \"original_first_token_ms\": 20.05, \"cka_only_20_first_token_ms\": 16.35, \"standard_20_first_token_ms\": 16.4, \"original_per_token_ms\": 13.89, \"cka_only_20_per_token_ms\": 16.73, \"standard_20_per_token_ms\": 16.71, \"original_params\": 7615616512, \"pruned_params\": 6161946112, \"param_reduction_pct\": 19.1}, \"log_path\": \"/root/runs/recovery_aware_struct_prune/inference_bench_clean_v2.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/inference_bench_clean_v2.json\", \"completed_at\": \"2026-05-19T02:44:07.178Z\"}, \"eval_gsm8k_sft_rasp_20_1p5b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T18:10:57.471Z\", \"updated_at\": \"2026-05-19T02:43:38.445Z\", \"hypothesis\": \"1.5B RASP post-SFT GSM8K accuracy (N=1319). SFT baseline for computing GRPO delta on RASP pruning at 1.5B. Compare with GRPO RASP 1.5B (26.16%).\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_1p5b --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_rasp_20_1p5b.json'\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:0\"], \"pid\": \"845212\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_rasp_20_1p5b.json\", \"submitted_at\": \"2026-05-18T23:43:58.904Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"sft_rasp_20_1p5b\", \"data_path\": \"gsm8k\", \"data_count\": 1319, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_1p5b\", \"eval_data\": \"gsm8k\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_1p5b\", \"wall_clock_seconds\": 10779.5, \"gpu_hours\": 2.99}, \"parent\": \"sft_rasp_20_1p5b\", \"reproduce\": {\"finished_at\": \"2026-05-19T02:40:07.920Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T02:40:13.441665+00:00\"}]}, \"metrics\": {\"accuracy\": 0.2691, \"n_correct\": 355, \"n_total\": 1319, \"stderr\": 0.0122, \"grpo_delta_pp\": -0.75}, \"conclusion\": \"success\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_rasp_20_1p5b.json\", \"completed_at\": \"2026-05-19T02:43:38.445Z\"}, \"eval_math500_grpo_standard_20_fair_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T18:24:25.108Z\", \"updated_at\": \"2026-05-19T01:39:52.608Z\", \"hypothesis\": \"Standard 20% post-GRPO (fair v5) MATH-500 accuracy with max_new_tokens=2048. Restart of slow original. Interim Acc@100=36%. Cross-benchmark validation for C1 decoupling claim.\", \"parent\": \"eval_math500_grpo_standard_20_fair\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/math500_grpo_standard_20_fair_v2.json --max_new_tokens 2048'\", \"gpu\": [\"cuda:1\"], \"pid\": \"22049\", \"model_name\": \"grpo_stage2_standard_20_fair\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair\", \"eval_data\": \"MATH-500\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_grpo_standard_20_fair_v2.log\"}, \"metrics\": {\"accuracy\": 0.264, \"n_correct\": 132, \"n_total\": 500, \"stderr\": 0.0197}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T01:39:36.502Z\"}, \"eval_math500_sft_rasp_20_2048\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:36:16.836Z\", \"updated_at\": \"2026-05-19T01:39:03.294Z\", \"hypothesis\": \"SFT RASP 20% MATH-500 accuracy with max_new_tokens=2048. Fair comparison with GRPO RASP @2048 (24.0%) for C1 decoupling on MATH-500. SFT recovery should show lower reasoning capability than GRPO recovery on structurally pruned model.\", \"parent\": \"eval_math500_sft_rasp_20\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=3 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/math500_sft_rasp_20_2048.json --max_new_tokens 2048'\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:3\"], \"pid\": \"39767\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/math500_sft_rasp_20_2048.log\", \"submitted_at\": \"2026-05-18T23:54:16.231Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"sft_rasp_20_westd\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd\", \"eval_data\": \"MATH-500\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd\", \"wall_clock_seconds\": 6287.1, \"gpu_hours\": 1.75}, \"reproduce\": {\"finished_at\": \"2026-05-19T01:36:05.254Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T01:36:12.478557+00:00\"}]}, \"metrics\": {\"accuracy\": 0.226, \"n_correct\": 113, \"n_total\": 500, \"stderr\": 0.0187, \"natural_eos\": 314, \"truncated\": 186, \"natural_eos_pct\": 0.628, \"avg_response_length\": 930.58, \"median_response_length\": 274}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T01:39:03.294Z\"}, \"eval_math500_dense_2048\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:08:58.081Z\", \"updated_at\": \"2026-05-19T01:34:41.598Z\", \"hypothesis\": \"Dense (unpruned) DeepSeek-R1-Distill-Qwen-7B MATH-500 eval with max_new_tokens=2048. Fair comparison baseline for all pruned model MATH-500 evals which also use 2048 max tokens. Previous Dense baseline (73.6%) used 4096 tokens.\", \"parent\": \"eval_math500_dense_unpruned\", \"spec\": {\"gpu\": [\"cuda:0\"], \"pid\": \"32469\", \"checkpoint_path\": \"/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/math500_dense_2048.json\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.53, \"n_correct\": 265, \"n_total\": 500, \"stderr\": 0.0223, \"natural_eos_pct\": 0.468, \"truncated_pct\": 0.532, \"avg_response_length\": 1724.5, \"median_response_length\": 2048}, \"completed_at\": \"2026-05-19T01:34:41.598Z\"}, \"eval_math500_grpo_rasp_20_fair\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T18:16:25.616Z\", \"updated_at\": \"2026-05-18T23:53:54.384Z\", \"hypothesis\": \"GRPO RASP 20% pruned model on MATH-500 with max_new_tokens=2048. Fair comparison for C1 decoupling: GRPO recovery on RASP-pruned model should show different accuracy profile compared to SFT recovery, measuring reasoning capability after RL-based fine-tuning on structurally pruned model.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/math500_grpo_rasp_20_fair.json --max_new_tokens 2048\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:3\"], \"model_name\": \"grpo_stage2_rasp_20_fair\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair\", \"eval_data\": \"MATH-500\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair\", \"log_path\": \"~/runs/recovery_aware_struct_prune/math500_grpo_rasp_20_fair.log\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.24, \"n_correct\": 120, \"n_total\": 500, \"stderr\": 0.0191, \"natural_eos_pct\": 0.64, \"truncated_pct\": 0.36, \"avg_response_length\": 903.5, \"median_response_length\": 272, \"max_new_tokens\": 2048}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/math500_grpo_rasp_20_fair.json\", \"completed_at\": \"2026-05-18T23:53:54.384Z\"}, \"eval_gsm8k_sft_cka_only_20_1p5b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T17:51:20.577Z\", \"updated_at\": \"2026-05-18T23:46:01.152Z\", \"hypothesis\": \"1.5B CKA-only post-SFT GSM8K accuracy (N=1319). SFT baseline for computing GRPO delta: if GRPO CKA-only 1.5B GSM8K > SFT CKA-only 1.5B GSM8K, GRPO adds value beyond SFT recovery on 1.5B scale. Completes C1 decoupling evidence at 1.5B.\", \"parent\": \"sft_cka_only_20_1p5b\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20_1p5b --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_cka_only_20_1p5b.json\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:0\"], \"checkpoint_source\": \"sft_cka_only_20_1p5b\", \"eval_data\": \"gsm8k\", \"data_path\": \"gsm8k\", \"data_count\": 1319, \"model_name\": \"Qwen2.5-1.5B-sft-cka-only-20\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20_1p5b/\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_cka_only_20_1p5b.json\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.3563, \"n_correct\": 470, \"n_total\": 1319, \"stderr\": 0.0132, \"eos_rate\": 0.9507, \"avg_response_length\": 336.76}, \"completed_at\": \"2026-05-18T23:46:01.152Z\"}, \"sft_standard_20_retrain_westd\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:40:50.567Z\", \"updated_at\": \"2026-05-18T23:24:15.076Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20 --gpu 2\\\"\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:2\"], \"pid\": \"34346\", \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_standard_20_retrain_westd.log\", \"submitted_at\": \"2026-05-18T22:40:50.078Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"pruned_standard_20 -> sft_standard_20\", \"data_path\": \"gsm8k (SFT recovery)\", \"data_count\": 7473, \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20\", \"wall_clock_seconds\": 2533.8, \"gpu_hours\": 0.7}, \"hypothesis\": \"Retrain SFT Standard 20% on westd from pruned_standard_20. Original sft_standard_20 model lost (was on old westd-11672). Needed for eval_math500_sft_standard_20_2048 with correct model.\", \"reproduce\": {\"finished_at\": \"2026-05-18T23:21:01.355Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T23:21:07.869075+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.758, \"mean_token_accuracy\": 0.8252, \"train_runtime_sec\": 1688, \"train_samples_per_second\": 8.856, \"epochs\": 2, \"total_steps\": 1870}, \"completed_at\": \"2026-05-18T23:23:03.857Z\"}, \"eval_gsm8k_grpo_rasp_20_1p5b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:59:22.921Z\", \"updated_at\": \"2026-05-18T23:02:00.110Z\", \"hypothesis\": \"1.5B RASP post-GRPO GSM8K accuracy (N=1319). Cross-model generalization: 7B RASP GRPO collapsed (reward 0.01), but 1.5B RASP showed reward=0.099 without collapse. If 1.5B RASP GSM8K is lower than CKA-only but not catastrophically low, confirms scale-dependent recovery dynamics. Completes 3-method 1.5B GSM8K comparison.\", \"parent\": \"grpo_rasp_20_1p5b\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_20_1p5b/checkpoint-100 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_rasp_20_1p5b.json'\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:1\"], \"data_path\": \"gsm8k:test\", \"data_count\": 1319, \"model_name\": \"grpo_rasp_20_1p5b/checkpoint-100\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_20_1p5b/checkpoint-100\", \"eval_data\": \"gsm8k:test\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_20_1p5b/checkpoint-100\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_rasp_20_1p5b.json\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.2616, \"n_correct\": 345, \"n_total\": 1319, \"stderr\": 0.0121, \"eos_rate\": 0.9378, \"avg_response_length\": 392.7}, \"completed_at\": \"2026-05-18T23:02:00.110Z\"}, \"eval_math500_sft_cka_only_20_v4_restart\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T18:16:24.171Z\", \"updated_at\": \"2026-05-18T22:12:04.614Z\", \"hypothesis\": \"CKA-only 20% post-SFT MATH-500 accuracy (restart of v4 which had cuda:2 conflict). Full 500 samples, max_new_tokens=2048. Core C1 evidence for decoupling claim.\", \"parent\": \"eval_math500_sft_cka_only_20_v4\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20\", \"log_path\": \"~/runs/recovery_aware_struct_prune/math500_sft_cka_only_20_v4.log\", \"results_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/math500_sft_cka_only_20_v4.json\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.29, \"n_correct\": 145, \"n_total\": 500, \"stderr\": 0.0203, \"natural_eos\": 384, \"truncated\": 116, \"natural_eos_pct\": 0.768, \"avg_response_length\": 673.278, \"median_response_length\": 242.5}, \"completed_at\": \"2026-05-18T22:12:04.614Z\"}, \"grpo_cka_only_20_extended_300\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T14:51:36.423Z\", \"updated_at\": \"2026-05-18T21:43:18.847Z\", \"hypothesis\": \"Extended GRPO CKA-only 7B from step 100 to 300. Paired control for E2 Standard extended: if CKA-only continues improving while Standard enters reward desert, proves CKA-only's structural advantage persists under longer training. Standard showed reward decline after step 260 (0.102→0.056); CKA-only's peak at step 100 was 0.354 — expect continued learning.\", \"parent\": \"grpo_cka_only_20\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_extended_300 --beta 0.01 --temperature 0.4 --repetition_penalty 1.15 --format_reward_weight 0.1 --loss_type dapo --learning_rate 1e-6 --max_steps 300 --save_steps 50 --save_total_limit 3 --resume_from_checkpoint /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20/checkpoint-100'\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:0\"], \"pid\": \"11457\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_cka_only_20_extended_300.log\", \"submitted_at\": \"2026-05-18T15:10:04.515Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (CKA-only 20% pruned, SFT recovered, GRPO extended)\", \"data_path\": \"openai/gsm8k\", \"data_count\": 7473, \"seed\": 42, \"wandb_run_id\": \"z9f0z901\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20/checkpoint-100\", \"eval_data\": \"openai/gsm8k (GRPO RL training)\", \"hyperparams\": {\"beta\": 0.01, \"temperature\": 0.4, \"repetition_penalty\": 1.15, \"format_reward_weight\": 0.1, \"loss_type\": \"dapo\", \"lr\": 1e-06, \"max_steps\": 300, \"save_steps\": 50, \"save_total_limit\": 3, \"resume_from_step\": 100}, \"wall_clock_seconds\": 23392.2, \"gpu_hours\": 6.5}, \"reproduce\": {\"finished_at\": \"2026-05-18T21:39:55.802Z\"}, \"failure_reason\": \"FALSE POSITIVE: Training completed 300/300 steps successfully, model saved. EXIT_CODE=129 (SIGHUP) occurred after training finished — wrapper process cleanup signal. Checkpoint at /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_extended_300. Pending metrics extraction and reclassification.\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T21:39:56.740Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T21:40:03.874593+00:00\"}]}, \"metrics\": {\"final_reward\": 0.3075, \"peak_reward\": 0.4444, \"peak_reward_step\": 280, \"reward_step100\": 0.354, \"reward_step300\": 0.3075, \"train_loss_final\": 0.0349, \"global_step\": 300, \"runtime_seconds\": 23004, \"gpu_hours\": 6.5, \"final_frac_zero_std\": 0.275, \"reward_range\": [0.22, 0.44], \"pattern\": \"sustained oscillation, no collapse\", \"wandb_run_id\": \"z9f0z901\"}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_extended_300\"}, \"eval_gsm8k_grpo_standard_20_1p5b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:38:01.585Z\", \"updated_at\": \"2026-05-18T21:03:21.558Z\", \"hypothesis\": \"Standard GRPO 1.5B (100 steps, reward=0.084) on GSM8K eval: expect low accuracy (~5-10%) given minimal training, serving as baseline for pruned model comparison.\", \"parent\": \"grpo_standard_20_1p5b\", \"spec\": {\"gpu\": [\"cuda:0\"], \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_1p5b/\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_standard_20_1p5b.json\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.2229, \"n_correct\": 294, \"n_total\": 1319, \"stderr\": 0.0115}, \"completed_at\": \"2026-05-18T21:03:21.558Z\"}, \"eval_gsm8k_grpo_cka_only_20_1p5b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:35:29.923Z\", \"updated_at\": \"2026-05-18T20:09:40.771Z\", \"hypothesis\": \"1.5B CKA-only post-GRPO GSM8K accuracy (N=1319). Cross-model generalization: 7B CKA-only GRPO achieved 64.37% GSM8K. If 1.5B CKA-only GRPO also leads among pruning methods, confirms scale-invariant recovery capacity gradient. Parent: grpo_cka_only_20_1p5b (reward=0.2375, highest among 1.5B methods).\", \"parent\": \"grpo_cka_only_20_1p5b\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_1p5b/checkpoint-100\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_cka_only_20_1p5b.json\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.3548, \"n_correct\": 468, \"n_total\": 1319, \"stderr\": 0.0132}, \"completed_at\": \"2026-05-18T20:09:40.771Z\"}, \"eval_math500_dense_unpruned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T13:42:10.786Z\", \"updated_at\": \"2026-05-18T18:15:28.383Z\", \"hypothesis\": \"Dense unpruned DeepSeek-R1-Distill-Qwen-7B MATH-500 baseline. Establishes upper bound for all pruned model MATH-500 evaluations. Previous result on westd showed 73.6%; this is a verification run on westd-29022.\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=3 python src/eval_math500.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/math500_dense_unpruned.json'\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:3\"], \"pid\": \"4223\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (dense unpruned)\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B\", \"eval_data\": \"MATH-500\", \"checkpoint_path\": \"/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B\", \"log_path\": \"~/runs/recovery_aware_struct_prune/math500_dense_unpruned.log\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.736, \"stderr\": 0.0197, \"n_correct\": 368, \"n_total\": 500, \"natural_eos_pct\": 0.752}, \"completed_at\": \"2026-05-18T18:13:54.213Z\"}, \"grpo_rasp_20_1p5b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T15:12:41.395Z\", \"updated_at\": \"2026-05-18T16:32:13.529Z\", \"hypothesis\": \"RASP 20% GRPO on 1.5B model. Cross-model generalization: 7B RASP collapsed to reward 0.01, frac_zero_std 0.85. If 1.5B shows same collapse pattern, confirms scale-invariant recovery capacity gradient bottom tier. Completes 3-method 1.5B comparison: CKA-only (reward ~0.26) >> Standard (0.08) >> RASP (expected collapse).\", \"parent\": \"sft_rasp_20_1p5b\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_1p5b --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_20_1p5b --beta 0.01 --temperature 0.4 --repetition_penalty 1.15 --format_reward_weight 0.1 --loss_type dapo --learning_rate 1e-6 --max_steps 100\", \"server\": \"westb-23072\", \"gpu\": \"cuda:1\", \"pid\": \"815395\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_rasp_20_1p5b.log\", \"submitted_at\": \"2026-05-18T15:13:38.510Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-1.5B (RASP 20% pruned, SFT recovered)\", \"data_path\": \"openai/gsm8k\", \"data_count\": 7473, \"seed\": 42, \"wandb_run_id\": \"a18r8uyw\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_1p5b\", \"eval_data\": \"openai/gsm8k (GRPO RL training)\", \"hyperparams\": {\"beta\": 0.01, \"temperature\": 0.4, \"repetition_penalty\": 1.15, \"format_reward_weight\": 0.1, \"loss_type\": \"dapo\", \"learning_rate\": 1e-06, \"max_steps\": 100, \"optimizer\": \"adamw_8bit\"}, \"wall_clock_seconds\": 4438.5, \"gpu_hours\": 1.23}, \"failure_reason\": \"Traceback → packages/torch/serialization.py\\\", line 977, in save _save( File \\\"/root/miniconda3/lib/python3.12/site-packages/torch/serialization.py\\\", line 1286, in _save zip_file.write_record(name, storage, num_bytes) RuntimeError: basic_ios::clear: iostream error\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T16:27:37.027Z\", \"metrics\": {\"final_reward\": 0.099, \"frac_zero_std\": 0.175, \"clipped_ratio\": 0.82}}, \"grpo_cka_only_20_1p5b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T12:50:08.570Z\", \"updated_at\": \"2026-05-18T16:08:40.491Z\", \"hypothesis\": \"CKA-only 20% GRPO on 1.5B model. Cross-model generalization: if CKA-only's superior GRPO dynamics (peak reward 0.354 on 7B) hold on 1.5B, confirms scale-invariant recovery capacity gradient. Parent: sft_cka_only_20_1p5b.\", \"parent\": \"sft_cka_only_20_1p5b\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20_1p5b --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_1p5b --beta 0.01 --temperature 0.4 --repetition_penalty 1.15 --format_reward_weight 0.1 --loss_type dapo --learning_rate 1e-6 --max_steps 100'\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:0\"], \"pid\": \"806188\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-1.5B (CKA-only 20% pruned, SFT recovered)\", \"data_path\": \"openai/gsm8k\", \"data_count\": 7473, \"seed\": 42, \"wandb_run_id\": \"8zkpr0hh\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20_1p5b\", \"eval_data\": \"openai/gsm8k (GRPO RL training, not eval)\", \"hyperparams\": {\"beta\": 0.01, \"temperature\": 0.4, \"repetition_penalty\": 1.15, \"format_reward_weight\": 0.1, \"loss_type\": \"dapo\", \"lr\": 1e-06, \"max_steps\": 100}}, \"conclusion\": \"success\", \"metrics\": {\"reward_mean\": 0.2375, \"frac_reward_zero_std\": 0.175, \"loss\": 0.0595, \"kl\": 0.00215, \"grad_norm\": 1.445, \"global_step\": 100, \"note\": \"training completed 100/100 but save_model failed (disk full). checkpoint-100 has complete model.\"}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_1p5b/checkpoint-100\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_cka_only_20_1p5b.log\", \"completed_at\": \"2026-05-18T16:08:40.491Z\"}, \"grpo_standard_20_1p5b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T14:15:13.990Z\", \"updated_at\": \"2026-05-18T15:11:31.870Z\", \"hypothesis\": \"Standard 20% GRPO on 1.5B model. Cross-model generalization: if Standard's dip-then-recovery GRPO dynamics (peak 0.081, dip 0.019 on 7B) hold on 1.5B, confirms scale-invariant recovery capacity gradient. Paired with CKA-only 1.5B GRPO for direct comparison.\", \"parent\": \"sft_standard_20_1p5b\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_1p5b --beta 0.01 --temperature 0.4 --repetition_penalty 1.15 --format_reward_weight 0.1 --loss_type dapo --learning_rate 1e-6 --max_steps 100'\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:1\"], \"pid\": \"811558\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-1.5B (Standard 20% pruned, SFT recovered)\", \"data_path\": \"openai/gsm8k\", \"data_count\": 7473, \"seed\": 42, \"wandb_run_id\": \"mm31apn0\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b\", \"eval_data\": \"openai/gsm8k (GRPO RL training)\", \"hyperparams\": {\"beta\": 0.01, \"temperature\": 0.4, \"repetition_penalty\": 1.15, \"format_reward_weight\": 0.1, \"loss_type\": \"dapo\", \"lr\": 1e-06, \"max_steps\": 100}}, \"metrics\": {\"reward_mean\": 0.0844, \"frac_reward_zero_std\": 0.15, \"loss\": 0.0151, \"grad_norm\": 4.03125, \"kl\": 0.0044, \"entropy\": 0.4617, \"final_step\": 100, \"max_steps\": 100, \"total_time_min\": 53}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_1p5b/\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/grpo_standard_1p5b_100steps.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T15:11:31.870Z\"}, \"grpo_standard_20_extended_300_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T13:53:41.781Z\", \"updated_at\": \"2026-05-18T14:50:59.377Z\", \"hypothesis\": \"Extended GRPO Standard 7B from step 110 to 300 (resumed after disk-full crash at step 120). Tests whether longer GRPO training changes the recovery capacity gradient. save_steps=50, save_total_limit=3 to prevent disk issues.\", \"parent\": \"grpo_standard_20_extended_300\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_extended_300/checkpoint-110 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_extended_300 --beta 0.01 --temperature 0.4 --repetition_penalty 1.15 --format_reward_weight 0.1 --loss_type dapo --learning_rate 1e-6 --max_steps 300 --save_steps 50 --save_total_limit 3 --resume_from_checkpoint /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_extended_300/checkpoint-110'\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:0\"], \"pid\": \"6346\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (Standard 20% pruned, SFT recovered, GRPO extended v2)\", \"data_path\": \"openai/gsm8k\", \"data_count\": 7473, \"seed\": 42, \"wandb_run_id\": \"44cjdoiy\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_extended_300/checkpoint-110\", \"eval_data\": \"openai/gsm8k (GRPO RL training)\", \"hyperparams\": {\"beta\": 0.01, \"temperature\": 0.4, \"repetition_penalty\": 1.15, \"format_reward_weight\": 0.1, \"loss_type\": \"dapo\", \"lr\": 1e-06, \"max_steps\": 300, \"save_steps\": 50, \"save_total_limit\": 3, \"resume_from_step\": 111}}, \"metrics\": {\"reward_mean_step300\": 0.0562, \"loss_step300\": 0.0367, \"frac_reward_zero_std_step300\": 0.525, \"kl_step300\": 0.00306, \"entropy_step300\": 0.157, \"lr_step300\": 3.33e-09, \"runtime_min\": 48, \"reward_decline_after_step260\": true}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_extended_300/checkpoint-300\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_standard_20_extended_300_v2.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T14:47:49.037Z\"}, \"sft_standard_20_1p5b\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-18T12:09:56.278Z\", \"updated_at\": \"2026-05-18T12:31:29.300Z\", \"hypothesis\": \"Standard 20% SFT recovery on 1.5B model. Cross-model generalization test: if Standard SFT recovery pattern holds on 1.5B as on 7B. Paired with CKA-only and RASP 1.5B SFT for cross-scale comparison of recovery capacity gradient.\", \"completed_at\": \"2026-05-18T12:17:36.938Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\"}}, \"spec\": {\"command\": \"python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_20_1p5b --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b --num_train_epochs 2 --batch_size 4 --gradient_accumulation_steps 2 --learning_rate 2e-5 --save_strategy no --gpu 0\", \"server\": \"westb-23072\", \"data_path\": \"openai/gsm8k (train split, cached)\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-1.5B (Standard 20% pruned)\", \"seed\": 42}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b\", \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_standard_20_1p5b.log\", \"conclusion\": \"success\"}, \"sft_cka_only_20_1p5b\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-18T11:29:09.842Z\", \"updated_at\": \"2026-05-18T12:31:27.978Z\", \"hypothesis\": \"CKA-only 20% SFT recovery on 1.5B model. Cross-model generalization test: if CKA-only SFT recovery pattern (high accuracy) holds on 1.5B as on 7B, validates that CKA-guided pruning preserves recovery capacity across model scales.\", \"notes\": \"Training completed 1870/1870 steps. Checkpoint save crashed (RuntimeError at inline_container.cc:668) due to disk 100% full. Model weights rescued from checkpoint-1870 (optimizer.pt truncated but model.safetensors intact). Checkpoints cleaned, model files promoted to output dir. Pending load validation.\", \"completed_at\": \"2026-05-18T12:09:49.634Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"notes\": \"Training completed 1870/1870 steps. Checkpoint save crashed (RuntimeError at inline_container.cc:668) due to disk 100% full. Model weights rescued from checkpoint-1870 (optimizer.pt truncated but model.safetensors intact). Checkpoints cleaned, model files promoted to output dir. Pending load validation.\"}}, \"spec\": {\"command\": \"python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_cka_only_20_1p5b --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20_1p5b --num_train_epochs 2 --batch_size 4 --gradient_accumulation_steps 2 --learning_rate 2e-5 --save_strategy epoch --gpu 0\", \"server\": \"westb-23072\", \"data_path\": \"openai/gsm8k (train split, cached)\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-1.5B (CKA-only 20% pruned)\", \"seed\": 42}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20_1p5b\", \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_cka_only_20_1p5b.log\", \"conclusion\": \"success\"}, \"sft_rasp_20_1p5b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T12:09:57.178Z\", \"updated_at\": \"2026-05-18T12:29:19.746Z\", \"hypothesis\": \"RASP 20% SFT recovery on 1.5B model. Cross-model generalization test: if RASP SFT recovery pattern holds on 1.5B as on 7B. Paired with CKA-only and Standard 1.5B SFT for cross-scale comparison of recovery capacity gradient.\", \"spec\": {\"command\": \"python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_20_1p5b --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_1p5b --num_train_epochs 2 --batch_size 4 --gradient_accumulation_steps 2 --learning_rate 2e-5 --save_strategy no --gpu 0\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:0\"], \"pid\": \"802010\", \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_rasp_20_1p5b.log\", \"account\": \"root\", \"data_path\": \"openai/gsm8k (train split, cached)\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-1.5B (RASP 20% pruned)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_20_1p5b\"}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_1p5b\", \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_rasp_20_1p5b.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T12:29:19.746Z\"}, \"inference_bench_cka_only_20_clean\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T09:47:42.247Z\", \"updated_at\": \"2026-05-18T10:07:56.924Z\", \"hypothesis\": \"Clean CKA-only inference benchmark (rerun after GPU contention in v1). Validates CKA-only latency/memory vs dense baseline on clean cuda:0. Dense dummy in rasp slot (rasp model not on westb).\", \"parent\": \"inference_bench_cka_only_20\", \"metrics\": {\"dense\": {\"tokens_per_second\": 75.73, \"avg_latency_sec\": 6.729, \"peak_memory_gb\": 16.22, \"total_tokens\": 25477, \"validation\": \"PASS (75.73 vs expected 76.25, <1% deviation)\"}, \"cka_only_20\": {\"tokens_per_second\": 51.86, \"avg_latency_sec\": 4.078, \"peak_memory_gb\": 11.6, \"total_tokens\": 10574, \"latency_speedup_vs_dense\": \"39.4%\", \"memory_reduction_vs_dense\": \"28.5%\"}, \"rasp_20_dummy\": {\"tokens_per_second\": 75.79, \"avg_latency_sec\": 6.723, \"peak_memory_gb\": 16.23, \"note\": \"Dense model used as dummy (rasp not on westb)\"}}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/inference_benchmark_cka_only_clean.json\", \"log_path\": \"~/runs/recovery_aware_struct_prune/inference_bench_cka_only_20_clean.log\", \"conclusion\": \"success\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 python src/benchmark_inference.py --dense_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --rasp_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --standard_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 --n_prompts 50 --max_new_tokens 512 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/inference_benchmark_cka_only_clean.json\\\"\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:0\"], \"data_path\": \"openai/gsm8k (50 prompts)\", \"data_count\": 50, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B + sft_cka_only_20\", \"seed\": 42, \"checkpoint_source\": \"sft_cka_only_20 + dense\", \"eval_data\": \"GSM8K 50 prompts (inference latency benchmark)\"}, \"completed_at\": \"2026-05-18T10:07:56.924Z\"}, \"eval_gsm8k_grpo_cka_only_20_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T05:54:02.634Z\", \"updated_at\": \"2026-05-18T08:50:27.816Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/gsm8k_grpo_cka_only_20.json --device_map cuda:0\\\"\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:0\"], \"pid\": \"776884\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_cka_only_20_v2.log\", \"submitted_at\": \"2026-05-18T05:54:02.072Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"openai/gsm8k\", \"data_count\": 1319, \"model_name\": \"grpo_cka_only_20\", \"seed\": 42, \"checkpoint_source\": \"grpo_cka_only_20\", \"eval_data\": \"GSM8K test (1319 samples)\", \"wall_clock_seconds\": 10583.6, \"gpu_hours\": 2.94}, \"hypothesis\": \"CKA-only GRPO GSM8K accuracy (v2, on westb). Tab2 critical data point: if CKA-only GRPO > SFT (63.91%), GRPO genuinely helps CKA-only recovery. Re-run after westd outage killed v1.\", \"parent\": \"eval_gsm8k_grpo_cka_only_20\", \"metrics\": {\"accuracy\": 0.6437, \"n_correct\": 849, \"n_total\": 1319, \"stderr\": 0.0132, \"eos_rate\": 0.9886, \"avg_response_length\": 203.43, \"truncated\": 15, \"wall_time_sec\": 8921}, \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_cka_only_20_v2.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T08:50:25.666Z\"}, \"grpo_cka_only_20\": {\"created_at\": \"2026-05-17T14:51:36.653Z\", \"hypothesis\": \"CKA-only pruning removes highest functional overlap first (post-prune 38.5% = least damage). Predicts GRPO collapse faster than RASP due to fewer backup paths. If confirmed, this is direct evidence of Redundancy-Stability Tradeoff: post-prune optimal = GRPO least stable.\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20 --gpu 0 --max_completion_length 1024 --beta 0.01 --temperature 0.4 --repetition_penalty 1.15 --format_reward_weight 0.1 --gradient_checkpointing true --optim adamw_bnb_8bit --loss_type dapo --learning_rate 1e-6 --max_steps 100 --save_steps 99999 --reward_desert_patience 50 --run_name grpo_cka_only_20\\\"\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_cka_only_20.log\", \"pid\": \"725227\", \"server\": \"westb-23072\", \"submitted_at\": \"2026-05-17T14:51:36.270Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 41272.3, \"gpu_hours\": 11.46, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20\", \"wandb_run_id\": \"li451oi4\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T02:21:23.748Z\", \"reproduce\": {\"finished_at\": \"2026-05-18T02:15:28.764Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T02:15:39.403491+00:00\"}]}, \"metrics\": {\"final_step\": 100, \"final_reward\": 0.3444, \"peak_reward\": 0.3544, \"peak_reward_step\": 50, \"final_frac_zero_std\": 0.2, \"final_loss\": 0.23, \"final_kl\": 0.001609, \"final_entropy\": 0.08751, \"final_reward_std\": 0.444, \"runtime_seconds\": 40710}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T02:19:28.551Z\"}, \"grpo_rasp_20_fair\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair\", \"completed_at\": \"2026-05-18T01:04:00Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T23:50:31.502Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-18T01:00:54.533595+00:00\"}]}, \"hypothesis\": \"Fair retrain of GRPO on RASP 20% pruned model using v5 config (same as CKA-only/Random). Resolves D058 confound: if RASP GRPO dynamics under v5 config show similar reward stagnation as original (old config), confirms the recovery capacity gradient is real and not an artifact of config differences.\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/grpo_rasp_20_fair.log\", \"metrics\": {\"final_completion_length\": 963.0, \"final_frac_zero_std\": 0.85, \"final_reward\": 0.01, \"min_frac_zero_std\": 0.675, \"peak_reward\": 0.061, \"total_steps\": 100, \"training_time_minutes\": 62.5, \"trend\": \"stagnation_then_collapse\"}, \"reproduce\": {\"finished_at\": \"2026-05-18T01:00:50.548Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair\", \"checkpoint_source\": \"sft_rasp_20_westd\", \"command\": \"python src/train_grpo_v5.py --model_path sft_rasp_20_westd --output_dir grpo_stage2_rasp_20_fair --gpu 0 --max_steps 100 --lr 1e-6 --beta 0.01 --loss_type dapo\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"N/A (GRPO training, not eval)\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 1.3, \"hyperparams\": {\"beta\": 0.01, \"format_reward_weight\": 0.1, \"loss_type\": \"dapo\", \"lr\": 1e-06, \"max_completion_length\": 1024, \"max_steps\": 100, \"optim\": \"adamw_bnb_8bit\", \"repetition_penalty\": 1.15, \"reward_desert_patience\": 200, \"save_steps\": 10, \"save_total_limit\": 3, \"temperature\": 0.4}, \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_rasp_20_fair.log\", \"model_name\": \"sft_rasp_20_westd\", \"pid\": \"68913\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-17T23:50:31.086Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 4668.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T01:08:19.563Z\"}, \"eval_postprune_standard_30\": {\"completed_at\": \"2026-05-18T00:27:39.362Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T19:08:46.051Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-18T00:25:39.283839+00:00\"}]}, \"hypothesis\": \"Standard 30% post-prune GSM8K accuracy (N=200). At 20% Standard post-prune was 17.5%, at 25% was ~15%. 30% should show further degradation. Compared with RASP 30% post-prune (running) to verify RASP advantage persists at higher sparsity. Extends multi-sparsity degradation curve.\", \"metrics\": {\"avg_response_length\": 3907.875, \"correct\": 8, \"eos_rate\": 0.055, \"gsm8k_accuracy\": 0.04, \"natural_eos\": 11, \"total\": 200, \"truncated\": 189}, \"parent\": \"prune_standard_30\", \"reproduce\": {\"finished_at\": \"2026-05-18T00:25:35.734Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_postprune_standard_30.json\", \"checkpoint_source\": \"pruned_standard_30\", \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_30 --max_samples 200 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_postprune_standard_30.json\\\"\", \"data_count\": 200, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"GSM8K (N=200, post-prune accuracy eval)\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 5.3, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_postprune_standard_30.log\", \"model_name\": \"pruned_standard_30\", \"pid\": \"47667\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-17T19:09:42.413Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 19076.9}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T00:27:39.362Z\"}, \"eval_sft_cka_only_20_n1319\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20\", \"completed_at\": \"2026-05-17T23:46:00Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T18:20:20.406Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-17T23:44:59.944695+00:00\"}]}, \"hypothesis\": \"CKA-only pruning preserves more recoverable structure than RASP/Standard, so post-SFT accuracy should be highest among all 20% pruning methods on full GSM8K (N=1319).\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_sft_cka_only_20_n1319.log\", \"metrics\": {\"avg_response_length\": 198.1, \"correct\": 843, \"eos_rate\": 0.9901, \"gsm8k_accuracy\": 0.6391, \"stderr\": 0.0132, \"total\": 1319}, \"reproduce\": {\"finished_at\": \"2026-05-17T23:44:55.094Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"sft_cka_only_20\", \"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_sft_cka_only_20_n1319.json\", \"data_count\": 1319, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"GSM8K (1319 samples, greedy)\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_sft_cka_only_20_n1319.log\", \"model_name\": \"sft_cka_only_20\", \"pid\": \"49475\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-17T19:17:43.358Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T23:48:58.392Z\"}, \"prune_cka_only_30\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_cka_only_30\", \"completed_at\": \"2026-05-17T21:54:34.000Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T21:42:06.467Z\", \"hypothesis\": \"CKA-only pruning at 30% sparsity. CKA-only 20% had highest post-prune accuracy (38.5%). At 30%, if still > 0% (vs RASP 30% = 0%), proves representational diversity scoring is more robust at high sparsity than composite scoring.\", \"metrics\": {\"actual_sparsity\": 0.2892, \"attn_heads_pruned\": \"0\", \"method\": \"dummy_ones_importance + rasp_alpha1 = pure CKA-only\", \"mlp_groups_pruned\": \"303/784\"}, \"retry_count\": 0, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=\\\"\\\" python src/prune.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --mode rasp --sparsity 0.30 --alpha 1.0 --dtype bfloat16 --importance_path results/importance_scores_dummy_ones.pt --cka_path results/cka_scores.pt --output_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_cka_only_30\", \"data_count\": 0, \"data_path\": \"importance_scores_dummy_ones.pt + cka_scores.pt\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T21:42:06.467Z\"}, \"eval_postprune_rasp_30\": {\"completed_at\": \"2026-05-17T19:38:55.561Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T18:22:00Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-17T19:38:59.282399+00:00\"}, {\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-17T21:37:12.892372+00:00\"}]}, \"failure_reason\": \"\", \"hypothesis\": \"RASP 30% post-prune GSM8K accuracy (N=200). At 20% RASP post-prune was 29%, at 25% was 21%. 30% should be lower. Establishes degradation curve for multi-sparsity analysis.\", \"metrics\": {\"accuracy\": 0, \"avg_response_length\": 3984.31, \"eos_rate\": 0.03, \"n_correct\": 0, \"n_total\": 200, \"natural_eos\": 6, \"truncated_rate\": 0.97}, \"notes\": \"实际完成全部 200 样本，EXIT_CODE=129 是 SSH 断连（SIGHUP），非真正失败。结果：accuracy=0.0%，97% 样本被截断（avg_len=3984/4096），模型在 30% sparsity 完全崩溃。降级曲线：29%(20%) → 21%(25%) → 0%(30%)，25%-30% 间存在 cliff。\", \"reproduce\": {\"finished_at\": \"2026-05-17T21:37:05.564Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_postprune_rasp_30.json\", \"checkpoint_source\": \"pruned_rasp_30\", \"data_count\": 200, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"GSM8K (200 samples, greedy)\", \"gpu\": [\"cuda:2\"], \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_postprune_rasp_30.log\", \"model_name\": \"pruned_rasp_30\", \"pid\": \"43911\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T21:39:43.149Z\"}, \"eval_humaneval_sft_standard_20_2048_v2\": {\"completed_at\": \"2026-05-17T17:46:56.057Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T16:26:15.836Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-17T17:43:52.491819+00:00\"}]}, \"hypothesis\": \"HumanEval pass@1 for SFT Standard 20% with max_new_tokens=2048. Completes 5-way HumanEval@2048 matrix. Compares SFT Standard vs SFT RASP (10.37%) code generation after recovery.\", \"metrics\": {\"avg_response_length\": 1850.7, \"correct\": 19, \"max_new_tokens\": 2048, \"median_response_length\": 2048, \"pass_at_1\": 0.1159, \"total\": 164}, \"reproduce\": {\"finished_at\": \"2026-05-17T17:43:47.471Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_standard_20_2048.json\", \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_westd --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_standard_20_2048.json\\\"\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 1.34, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_humaneval_sft_standard_20_2048_v2.log\", \"pid\": \"36724\", \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-17T16:26:15.449Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 4840.6}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T19:09:18.456Z\"}, \"eval_humaneval_grpo_standard_20_2048\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_standard_20_2048.json\", \"completed_at\": \"2026-05-17T18:16:11.481Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T13:41:03.761Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-17T17:53:39.102917+00:00\"}]}, \"hypothesis\": \"HumanEval pass@1 for GRPO Standard 20% with max_new_tokens=2048. 512-token results invalidated due to truncation artifact (RASP shorter outputs biased). Part of complete 4-way HumanEval@2048 comparison: unpruned / SFT RASP / GRPO Standard / GRPO RASP.\", \"metrics\": {\"avg_response_length\": 1843, \"correct\": 17, \"max_new_tokens\": 2048, \"median_response_length\": 2048, \"pass_at_1\": 0.1037, \"total\": 164}, \"parent\": \"eval_humaneval_grpo_standard_20\", \"reproduce\": {\"finished_at\": \"2026-05-17T17:53:32.827Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_standard_20_2048.json\\\"\", \"gpu\": [\"cuda:2\"], \"gpu_hours\": 4.58, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_humaneval_grpo_standard_20_2048.log\", \"pid\": \"27194\", \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-17T13:41:38.223Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 16473.3}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T18:16:11.481Z\"}, \"grpo_rasp_25\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_25\", \"completed_at\": \"2026-05-16T17:02:51.984Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T08:42:40.256Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-16T17:02:53.863552+00:00\"}], \"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"step_100\": {\"entropy\": 0.04262, \"frac_reward_zero_std\": 0.875, \"grad_norm\": 0.05371, \"kl\": 0.0007035, \"loss\": 0.01275, \"reward\": 0.009375, \"reward_std\": 0.03149}, \"wall_clock_min\": 57.95, \"wandb_run_id\": \"bc4ojqie\"}}}, \"failure_reason\": \"FALSE POSITIVE: Cron 误判。实验实际 100/100 步完成，模型已保存，W&B (bc4ojqie) 正常 finalize。进程正常退出后 ~7min Cron 检测到无存活进程，错误标记为 failed。\", \"hypothesis\": \"RASP 25% GRPO recovery (100 steps). 预期 collapse 比 20% 更快更严重。与 grpo_standard_25 对比验证 C3: recovery method conditions pruning order. Parent: sft_rasp_25.\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_rasp_25.log\", \"metrics\": {\"note\": \"Restored from previous_failure — cron false positive, experiment actually completed 100/100 steps successfully\", \"step_100\": {\"entropy\": 0.04262, \"frac_reward_zero_std\": 0.875, \"grad_norm\": 0.05371, \"kl\": 0.0007035, \"loss\": 0.01275, \"reward\": 0.009375, \"reward_std\": 0.03149}, \"wall_clock_min\": 57.95, \"wandb_run_id\": \"bc4ojqie\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T17:02:50.600Z\"}, \"retry_count\": 1, \"spec\": {\"command\": \"previous run (bc4ojqie) completed 100/100 steps, restoring status\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"model_name\": \"sft_rasp_25 (RASP 25% pruned + SFT)\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T18:06:56.419Z\"}, \"eval_humaneval_grpo_rasp_20_2048\": {\"completed_at\": \"2026-05-17T16:24:44.117Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T13:41:44.795Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-17T16:24:47.836792+00:00\"}]}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"hypothesis\": \"HumanEval pass@1 for GRPO RASP 20% with max_new_tokens=2048. Completes 4-way HumanEval@2048 matrix. If GRPO RASP > GRPO Standard on code generation, reinforces C3 (RASP preserves transferable structures). Queued for westd cuda:0 after unpruned 2048 completes.\", \"metrics\": {\"correct\": 24, \"max_new_tokens\": 2048, \"pass_at_1\": 0.1463, \"stderr\": 0.0276, \"total\": 164}, \"reproduce\": {\"finished_at\": \"2026-05-17T16:24:41.714Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"checkpoint_source\": \"grpo_stage2_rasp_20_v9\", \"data_count\": 164, \"data_path\": \"openai/openai_humaneval\", \"eval_data\": \"HumanEval (164 problems, max_new_tokens=2048)\", \"gpu\": [\"cuda:0\"], \"model_name\": \"grpo_stage2_rasp_20_v9\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T16:24:44.117Z\"}, \"eval_sft_cka_only_20\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-17T14:28:35.380Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-17T14:45:45.988283+00:00\"}]}, \"hypothesis\": \"CKA-only 20% post-SFT GSM8K accuracy (N=200). Post-prune was 38.5% (highest among all methods). If post-SFT >> 60%, CKA-only scoring is superior for SFT recovery. If ~60% like RASP/Standard/Random, confirms SFT equalizes all scoring methods regardless of post-prune advantage.\", \"metrics\": {\"avg_response_length\": 182.73, \"eos_rate\": 0.995, \"gsm8k_accuracy\": 0.64, \"gsm8k_stderr\": 0.0339, \"mode\": \"greedy\", \"n_correct\": 128, \"n_total\": 200, \"seed\": 42, \"truncated\": 1}, \"parent\": \"sft_cka_only_20\", \"reproduce\": {\"finished_at\": \"2026-05-17T14:45:37.016Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"sft_cka_only_20\", \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 --max_samples 200 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_sft_cka_only_20.json\\\"\", \"data_count\": 200, \"data_path\": \"gsm8k\", \"eval_data\": \"GSM8K (N=200)\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_sft_cka_only_20.log\", \"model_name\": \"sft_cka_only_20\", \"pid\": \"723605\", \"seed\": 42, \"server\": \"westb-23072\", \"submitted_at\": \"2026-05-17T14:29:08.063Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T14:48:17.267Z\"}, \"sft_cka_only_20\": {\"completed_at\": \"2026-05-17T14:28:29.688Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T13:43:50.320Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-17T14:25:05.697649+00:00\"}]}, \"hypothesis\": \"CKA-only scoring 20% post-SFT accuracy. Post-prune accuracy was 38.5% (N=200), higher than RASP 29% and Random 34%. If post-SFT converges to ~60% like other methods, confirms SFT equalizes different pruning strategies. If significantly higher, CKA-only might be superior scoring for SFT recovery.\", \"metrics\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20/\", \"note\": \"Initial loss 1.958 > RASP 1.86 > Standard 1.70 (CKA-only has most initial damage). Final loss 0.62 comparable to baselines. No greedy eval run yet.\", \"token_accuracy\": 0.8362, \"total_steps\": 1870, \"train_loss_final\": 0.6165, \"train_loss_initial\": 1.958, \"train_time_min\": 33.4}, \"parent\": \"scoring_ablation_cka_only_20\", \"reproduce\": {\"finished_at\": \"2026-05-17T14:25:02.351Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20/\", \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_cka_only_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 --save_strategy no --gpu 0\\\"\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 0.69, \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_cka_only_20.log\", \"pid\": \"720955\", \"server\": \"westb-23072\", \"submitted_at\": \"2026-05-17T13:47:02.912Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2486.8}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T14:28:29.688Z\"}, \"eval_humaneval_unpruned_2048\": {\"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-17T13:53:24.205Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T12:40:50.255Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-17T13:51:38.304442+00:00\"}]}, \"hypothesis\": \"HumanEval pass@1 for unpruned DeepSeek-R1-Distill-Qwen-7B with max_new_tokens=2048 (previous run used 512 which truncated thinking chain). Establishes dense model ceiling for code generation comparison.\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_humaneval_unpruned_2048.log\", \"metrics\": {\"avg_response_length\": 1771, \"correct\": 74, \"max_new_tokens\": 2048, \"median_response_length\": 2048, \"pass_at_1\": 0.4512, \"stderr\": 0.0389, \"total\": 164, \"wall_time_min\": 67.6}, \"reproduce\": {\"finished_at\": \"2026-05-17T13:50:48.122Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A (eval only)\", \"command\": \"python src/eval_humaneval.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --max_new_tokens 2048\", \"data_count\": 164, \"data_path\": \"HumanEval\", \"eval_data\": \"HumanEval (164 problems, max_new_tokens=2048)\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 1.2, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_humaneval_unpruned_2048.log\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (unpruned)\", \"pid\": \"23707\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-17T12:41:06.754Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 4337.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T13:53:59.636Z\"}, \"eval_humaneval_sft_rasp_20_2048\": {\"completed_at\": \"2026-05-17T13:42:41.560Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T12:40:51.686Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-17T13:35:19.516014+00:00\"}]}, \"hypothesis\": \"HumanEval pass@1 for SFT RASP 20% with max_new_tokens=2048 (previous run used 512 which truncated thinking chain). Tests whether longer generation improves code quality for pruned+recovered model.\", \"metrics\": {\"correct\": 17, \"max_new_tokens\": 2048, \"median_response_length\": 2048, \"note\": \"still truncating at median=2048, main failure mode is thinking chain leaking into code output\", \"pass_at_1\": 0.1037, \"stderr\": 0.0238, \"total\": 164, \"wall_time_min\": 42}, \"reproduce\": {\"finished_at\": \"2026-05-17T13:35:15.143Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"sft_rasp_20_westd\", \"command\": \"python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd --max_new_tokens 2048\", \"data_count\": 164, \"data_path\": \"HumanEval\", \"eval_data\": \"HumanEval (164 problems, max_new_tokens=2048)\", \"gpu\": [\"cuda:2\"], \"gpu_hours\": 1.03, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_humaneval_sft_rasp_20_2048.log\", \"model_name\": \"sft_rasp_20_westd\", \"pid\": \"23785\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-17T12:41:09.839Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 3691.7}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T13:42:41.560Z\"}, \"eval_humaneval_grpo_standard_20\": {\"completed_at\": \"2026-05-17T13:33:59.897Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T10:00:40.683Z\", \"hypothesis\": \"HumanEval pass@1 for grpo_standard_20 vs sft_standard_20 (3.05%). If grpo_standard >> sft_standard on HumanEval, GRPO transfers code generation ability even with Standard pruning. Completes HumanEval comparison matrix.\", \"metrics\": {\"correct\": 3, \"max_new_tokens\": 512, \"note\": \"512-token truncation, low quality\", \"pass_at_1\": 0.0183, \"total\": 164}, \"parent\": \"eval_humaneval_sft_standard_20\", \"reproduce\": {\"finished_at\": \"2026-05-17T12:09:38.756Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"grpo_stage2_standard_20_v8/checkpoint-50\", \"command\": \"python src/eval_humaneval.py --model_path grpo_stage2_standard_20_v8/checkpoint-50\", \"data_count\": 164, \"data_path\": \"HumanEval\", \"eval_data\": \"HumanEval (164 problems)\", \"gpu\": [\"cuda:2\"], \"gpu_hours\": 3.56, \"log_path\": \"westd results/eval_humaneval_grpo_standard_20.json\", \"model_name\": \"grpo_stage2_standard_20_v8\", \"pid\": \"16483\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-17T10:00:40.348Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 12799.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T13:33:59.897Z\"}, \"eval_math500_unpruned\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_unpruned.json\", \"completed_at\": \"2026-05-17T12:40:26.343Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T06:23:49.923Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-17T11:34:16.017881+00:00\"}]}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"hypothesis\": \"MATH-500 baseline: unpruned DeepSeek-R1-Distill-Qwen-7B accuracy on MATH-500. Establishes dense model ceiling for cross-benchmark generalization comparison with pruned+recovered models.\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_unpruned.json\", \"metrics\": {\"N\": 500, \"accuracy\": 0.736, \"correct\": 368, \"stderr\": 0.02}, \"reproduce\": {\"finished_at\": \"2026-05-17T11:34:07.227Z\"}, \"retry_count\": 0, \"spec\": {\"command\": \"python src/eval_math500.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B\", \"data_count\": 500, \"data_path\": \"MATH-500\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (unpruned)\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T12:40:26.343Z\"}, \"eval_gradient_postsft\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_gradient_20\", \"completed_at\": \"2026-05-17T11:24:16.260Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T10:07:58.644Z\", \"hypothesis\": \"GSM8K accuracy after SFT recovery on gradient-pruned model. Pre-SFT was 25.5%. If post-SFT reaches ~50-60%, gradient scoring is viable but weaker than RASP (~61%). If much lower, gradient scoring causes partially irreversible damage.\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gradient_postsft.log\", \"metrics\": {\"accuracy\": 0.615, \"avg_response_length\": 167.455, \"correct\": 123, \"eos_rate\": 0.995, \"stderr\": 0.0344, \"total\": 200}, \"parent\": \"gradient_sft_v3\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_gradient_20 --max_samples 200 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gradient_postsft.json\\\"\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 1.27, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gradient_postsft.log\", \"pid\": \"701495\", \"server\": \"westb-23072\", \"submitted_at\": \"2026-05-17T10:07:58.275Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 4578.0}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T11:24:16.260Z\"}, \"gradient_sft_v3\": {\"completed_at\": \"2026-05-17T10:08:07.026Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T09:28:21.646Z\", \"hypothesis\": \"SFT recovery on gradient-pruned model (25.5% post-prune acc). If SFT recovers gradient to ~50-60%, gradient scoring is viable but weaker than CKA-aware. If recovery fails or minimal, gradient scoring causes irreversible damage similar to magnitude.\", \"metrics\": {\"epochs\": 2, \"final_loss\": 0.644, \"output_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_gradient_20\", \"steps\": 1870, \"token_accuracy\": 0.825}, \"parent\": \"scoring_ablation_batch_v2\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_gradient_20\", \"checkpoint_source\": \"pruned_gradient_20 (gradient scoring, 19.09% sparsity)\", \"command\": \"python src/sft_recovery.py --model_path pruned_gradient_20 --output_dir sft_gradient_20 --gpu 0 --save_strategy no --seed 42\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k (SFT training data)\", \"eval_data\": \"N/A - this is SFT training, not eval\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 0.66, \"log_path\": \"~/runs/recovery_aware_struct_prune/gradient_sft_v3.log\", \"model_name\": \"pruned_gradient_20\", \"pid\": \"699032\", \"seed\": 42, \"server\": \"westb-23072\", \"submitted_at\": \"2026-05-17T09:28:21.306Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2385.7}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T10:08:07.026Z\"}, \"eval_math500_sft_standard_20\": {\"completed_at\": \"2026-05-17T10:00:26.439Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T06:23:54.283Z\", \"hypothesis\": \"MATH-500 eval for Standard 20% post-SFT model. Comparison point: does Standard pruning preserve MATH-500 capability similarly to its GSM8K performance (64%)? Part of Plan_012 extended eval.\", \"metrics\": {\"correct\": 130, \"eos_rate\": 0.578, \"math500_acc\": 0.26, \"stderr\": 0.0196, \"total\": 500, \"truncated\": 211, \"wall_time_hours\": 3.58}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"sft_standard_20_westd\", \"command\": \"python src/eval_math500.py --model_path sft_standard_20_westd\", \"data_count\": 500, \"data_path\": \"MATH-500\", \"eval_data\": \"MATH-500 (500 problems)\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_math500_sft_standard.log\", \"model_name\": \"sft_standard_20_westd\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T10:00:26.439Z\"}, \"eval_math500_sft_rasp_20\": {\"completed_at\": \"2026-05-17T09:24:16.959Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T06:23:52.474Z\", \"hypothesis\": \"MATH-500 eval for RASP 20% post-SFT model. Tests whether RASP pruning+recovery generalizes beyond GSM8K to harder math reasoning (MATH-500). Part of Plan_012 extended eval.\", \"metrics\": {\"correct\": 121, \"math500_acc\": 0.242, \"stderr\": 0.0192, \"total\": 500, \"wall_time_hours\": 2.94}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"sft_rasp_20_westd\", \"command\": \"python src/eval_math500.py --model_path sft_rasp_20_westd\", \"data_count\": 500, \"data_path\": \"MATH-500\", \"eval_data\": \"MATH-500 (500 problems)\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_math500_sft_rasp.log\", \"model_name\": \"sft_rasp_20_westd\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T09:24:16.959Z\"}, \"eval_unstructured_20\": {\"completed_at\": \"2026-05-17T08:50:18.688Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T05:35:41.205Z\", \"hypothesis\": \"Unstructured magnitude pruning at 20% sparsity should retain more accuracy than structured pruning (RASP/Standard) at same sparsity level, since unstructured preserves model architecture. Serves as calibration baseline for structured vs unstructured gap. Expected post-prune accuracy ~75-80% (mild degradation from 82% dense).\", \"metrics\": {\"avg_response_length\": 641, \"correct\": 1159, \"eos_rate\": 0.9803, \"gsm8k_acc\": 0.8787, \"stderr\": 0.009, \"total\": 1319, \"truncated\": 26, \"wall_time_hours\": 3.23}, \"parent\": \"prune_unstructured_20\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_unstructured_20\", \"checkpoint_source\": \"pruned_unstructured_20\", \"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_unstructured_20 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_unstructured_20_n1319.json'\", \"data_count\": 1319, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"GSM8K test (n=1319, greedy)\", \"gpu\": [\"cuda:1\"], \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_unstructured_20.log\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (unstructured magnitude 20%)\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_unstructured_20\", \"pid\": \"eval_unstructured_20\", \"seed\": 42, \"server\": \"westb-23072\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T08:50:18.688Z\"}, \"eval_humaneval_sft_standard_20\": {\"completed_at\": \"2026-05-17T08:31:52.684Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T07:56:08.222Z\", \"hypothesis\": \"HumanEval pass@1 for sft_standard_20 compared to sft_rasp_20 (7.32%) and grpo_rasp_20 (10.37%). If sft_standard ≈ sft_rasp → pruning method doesn't affect code generation recovery. If sft_standard << sft_rasp → RASP pruning preserves more code-relevant structure.\", \"metrics\": {\"correct\": 5, \"failure_modes\": \"model generates CoT natural language instead of code, all responses truncated at max_tokens=512\", \"pass_at_1\": 0.0305, \"stderr\": 0.0134, \"total\": 164, \"wall_time_min\": 17}, \"parent\": \"eval_humaneval_sft_rasp_20\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"sft_standard_20_westd\", \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && export HF_ENDPOINT=https://hf-mirror.com && python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_westd --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_standard_20.json\\\"\", \"data_count\": 164, \"data_path\": \"HumanEval\", \"eval_data\": \"HumanEval (164 problems)\", \"gpu\": [\"cuda:3\"], \"gpu_hours\": 0.6, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_humaneval_sft_standard_20.log\", \"model_name\": \"sft_standard_20_westd\", \"pid\": \"9605\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-17T07:56:07.888Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2144.8}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T08:31:52.684Z\"}, \"eval_humaneval_sft_rasp_20\": {\"completed_at\": \"2026-05-17T07:55:52.564Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T07:19:22.820Z\", \"hypothesis\": \"If SFT (without GRPO) already produces ~10% HumanEval pass@1 on pruned model, then GRPO adds no HumanEval increment, confirming C1 decoupling (reward improves but code generation ability comes from SFT instruction-following, not GRPO)\", \"metrics\": {\"correct\": 12, \"failure_modes\": \"model outputs natural language thinking instead of code (SyntaxError), parenthesis mismatch\", \"median_response_length\": 512, \"note\": \"max_tokens truncation frequent\", \"pass_at_1\": 0.0732, \"stderr\": 0.0203, \"total\": 164}, \"parent\": \"eval_humaneval_grpo_rasp_20\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"sft_rasp_20_westd\", \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && export HF_ENDPOINT=https://hf-mirror.com && python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_rasp_20.json\\\"\", \"data_count\": 164, \"data_path\": \"HumanEval\", \"eval_data\": \"HumanEval (164 problems)\", \"gpu\": [\"cuda:3\"], \"gpu_hours\": 0.61, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_humaneval_sft_rasp_20.log\", \"model_name\": \"sft_rasp_20_westd\", \"pid\": \"7528\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-17T07:19:22.501Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2190.1}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T07:55:52.564Z\"}, \"multiseed_serial_westb\": {\"completed_at\": \"2026-05-17T07:50:11.807Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T05:47:08.060Z\", \"hypothesis\": \"Multi-seed variance estimation (westb fallback): 4 serial evals (RASP×2 + Standard×2, seeds 123/456, N=200) to complement seed=42 data. Transferred from failed westd-11672. Results needed for 5-seed statistical significance in Paper Table 1.\", \"metrics\": {\"missing\": \"seed 42 and seed 789 not executed\", \"note\": \"2 seeds x 2 methods (not 4 seeds as planned). Script ran RASP+Standard for seeds 123,456.\", \"rasp_seed123\": {\"acc\": 0.605, \"correct\": 121, \"total\": 200}, \"rasp_seed456\": {\"acc\": 0.6, \"correct\": 120, \"total\": 200}, \"standard_seed123\": {\"acc\": 0.645, \"correct\": 129, \"total\": 200}, \"standard_seed456\": {\"acc\": 0.61, \"correct\": 122, \"total\": 200}}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"sft_rasp_20, sft_standard_20\", \"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py (4 serial evals)'\", \"data_count\": 200, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"GSM8K test (n=200, seeds 123+456)\", \"gpu\": [\"cuda:0\"], \"log_path\": \"/root/runs/recovery_aware_struct_prune/multiseed_serial.log\", \"model_name\": \"sft_rasp_20 + sft_standard_20\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_{rasp,standard}_20\", \"pid\": 681896, \"seed\": \"123,456\", \"server\": \"westb-23072\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T07:50:11.807Z\"}, \"eval_humaneval_grpo_rasp_20\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9\", \"completed_at\": \"2026-05-17T07:15:58.856Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T06:42:19.044Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-17T07:12:26.070132+00:00\"}]}, \"hypothesis\": \"HumanEval eval for RASP 20% post-GRPO model. Verifies C1 on code generation: post-GRPO accuracy should ≈ post-SFT (GRPO doesn't improve non-GSM8K tasks on pruned models). Baseline unpruned = 1.83% pass@1.\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_humaneval_grpo_rasp_20.log\", \"metrics\": {\"n_passed\": 17, \"n_total\": 164, \"pass_at_1\": 0.1037, \"stderr\": 0.0238}, \"reproduce\": {\"finished_at\": \"2026-05-17T07:12:22.138Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"grpo_stage2_rasp_20_v9\", \"command\": \"python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9\", \"data_count\": 164, \"data_path\": \"openai/openai_humaneval\", \"eval_data\": \"humaneval\", \"gpu\": [\"cuda:3\"], \"gpu_hours\": 0.56, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_humaneval_grpo_rasp_20.log\", \"model_name\": \"grpo_stage2_rasp_20_v9\", \"pid\": \"5264\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-17T06:42:18.740Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2020.1}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T07:15:58.856Z\"}, \"eval_humaneval_unpruned\": {\"completed_at\": \"2026-05-17T06:42:38.578Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T06:23:55.527Z\", \"hypothesis\": \"HumanEval baseline: unpruned DeepSeek-R1-Distill-Qwen-7B pass@1 on HumanEval (164 problems). Establishes dense model ceiling for code generation capability comparison.\", \"metrics\": {\"n_passed\": 3, \"n_total\": 164, \"pass_at_1\": 0.0183, \"stderr\": 0.0105}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B\", \"checkpoint_source\": \"DeepSeek-R1-Distill-Qwen-7B\", \"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && export HF_ENDPOINT=https://hf-mirror.com && CUDA_VISIBLE_DEVICES=3 python src/eval_humaneval.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_unpruned.json'\", \"data_count\": 164, \"data_path\": \"openai/openai_humaneval\", \"eval_data\": \"HumanEval (164 problems, pass@1)\", \"gpu\": [\"cuda:3\"], \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_humaneval_unpruned.log\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (unpruned)\", \"model_path\": \"/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B\", \"output_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_unpruned.json\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T06:42:38.578Z\"}, \"eval_grpo_rasp_25\": {\"completed_at\": \"2026-05-17T05:27:33.072Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T20:04:16.057Z\", \"hypothesis\": \"DeepSeek-R1-Distill-Qwen-7B RASP 25% post-GRPO GSM8K eval (N=1319, greedy, seed=42). GRPO frac_zero=0.875 (severe collapse), reward=0.009. C1 25% ��键验证：collapse 后 accuracy 是否 ≈ pre-GRPO (52.99%)。Parent: grpo_rasp_25.\", \"metrics\": {\"accuracy\": 0.5315, \"avg_len\": 433.85, \"eos_rate\": 0.9272, \"max_len\": 4096, \"min_len\": 39, \"n_correct\": 701, \"n_total\": 1319, \"stderr\": 0.0137, \"truncated\": 96}, \"parent\": \"grpo_rasp_25\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_25\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_25\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_25 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_rasp_25_n1319.json\", \"data_count\": 1319, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"GSM8K test split (N=1319, greedy)\", \"gpu\": \"cuda:0\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_grpo_rasp_25.log\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (RASP 25% pruned, SFT, GRPO 100 steps)\", \"output_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_rasp_25_n1319.json\", \"pid\": \"639423\", \"seed\": 42, \"server\": \"westb-23072\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T05:27:33.072Z\"}, \"eval_grpo_standard_25\": {\"completed_at\": \"2026-05-16T21:13:27.442Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T19:39:31.510Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-16T21:13:33.404018+00:00\"}, {\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-16T21:29:08.933205+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"failure_reason\": \"\", \"hypothesis\": \"DeepSeek-R1-Distill-Qwen-7B Standard 25% post-GRPO GSM8K eval (N=1319, greedy, seed=42). GRPO reward=0.0075(near-collapse)，验证 accuracy 损失程度。对比 pre-GRPO sft_standard_25: 51.25%. Parent: grpo_standard_25.\", \"metrics\": {\"accuracy\": 0.511, \"avg_len\": 292.86, \"eos_rate\": 0.9628, \"n_correct\": 674, \"n_total\": 1319, \"stderr\": 0.01376}, \"notes\": \"Registry 被 cron 误标 DONE(failed)。实际 PID 48540 仍在运行（SSH 确认 2026-05-17T02:00: 1205/1319=91.4%, acc=51.17%, eos=96.5%）。预计 5-10 min 后完成。结果写入 /root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_standard_25_n1319.json。完成后需手动收割。\", \"parent\": \"grpo_standard_25\", \"reproduce\": {\"finished_at\": \"2026-05-16T21:29:03.454Z\"}, \"retry_count\": 2, \"spec\": {\"command\": \"source /root/miniconda3/bin/activate && CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_standard_25_n1319.json\", \"eval_data\": \"GSM8K test (n=1319)\", \"gpu\": \"cuda:1\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_grpo_standard_25.log\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25\", \"output_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_standard_25_n1319.json\", \"pid\": 48540, \"seed\": 42, \"server\": \"westd-11672\", \"started_at\": \"2026-05-17T05:19:52\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T04:49:07.062Z\"}, \"sft_standard_20_retrain\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20/\", \"completed_at\": \"2026-05-15T12:35:56.639Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-15T08:00:22.779Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-15T12:30:34.816944+00:00\"}]}, \"hypothesis\": \"Standard 20% SFT retrain with identical hyperparameters reproduces original loss/accuracy, confirming SFT recovery is deterministic and prior result was not anomalous\", \"metrics\": {\"conclusion\": \"Matches original sft_standard_20 (loss 0.64, token_accuracy 83%). Retrain successful.\", \"token_accuracy\": 0.83, \"train_loss_final\": 0.64}, \"notes\": \"SFT Standard retrain 完成. loss 0.64, token_accuracy 83%, 与原始 sft_standard_20 完全一致. Checkpoint: /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20/. 用于 Standard GRPO v5 对照实验.\", \"parent\": \"prune_standard_20\", \"reproduce\": {\"finished_at\": \"2026-05-15T12:30:33.744Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20/\", \"checkpoint_source\": \"/root/autodl-tmp/pruned_standard_20\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && python src/sft_recovery.py --model_path /root/autodl-tmp/pruned_standard_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20 --gpu 1 --num_train_epochs 2 --learning_rate 2e-5 --batch_size 1 --gradient_accumulation_steps 8 --max_seq_length 2048 --logging_steps 10 --seed 42\\\"\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.81, \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_standard_20_retrain.log\", \"model_name\": \"pruned_standard_20\", \"pid\": \"515168\", \"seed\": 42, \"server\": \"westb-23072\", \"submitted_at\": \"2026-05-15T11:47:22.611Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2914.0}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:29:39.616Z\"}, \"eval-sft-alpha-0p0\": {\"completed_at\": \"2026-05-15T14:52:01.132Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-15T14:26:31.883Z\", \"hypothesis\": \"Alpha=0.0 (no CKA, pure magnitude) post-SFT matches Standard pruning recovery (~64%), establishing that removing CKA collapses RASP to standard behavior (C2 ablation endpoint)\", \"metrics\": {\"accuracy\": 0.64, \"avg_len\": 257.9, \"eos_rate\": 0.97, \"n_correct\": 64, \"n_total\": 100}, \"parent\": \"sft-alpha-0p0\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_0.0\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_0.0\", \"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_0.0 --max_samples 100 --max_new_tokens 4096\", \"data_count\": 100, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k_test_n100\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.42, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval-sft-alpha-0p0.log\", \"model_name\": \"Qwen2.5-7B pruned alpha=0.0 post-SFT\", \"pid\": \"40489\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-15T14:26:31.816Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 1529.3}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:29:37.940Z\"}, \"eval-sft-alpha-1p0\": {\"completed_at\": \"2026-05-15T15:24:56.027Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-15T14:51:22.694Z\", \"hypothesis\": \"Alpha=1.0 (full CKA weight) post-SFT accuracy matches RASP default (~57%), confirming alpha=1.0 produces identical pruning structure to standard RASP (C2 ablation endpoint)\", \"metrics\": {\"accuracy\": 0.57, \"avg_len\": 224.18, \"eos_rate\": 0.98, \"n_correct\": 57, \"n_total\": 100, \"natural_eos\": 98, \"stderr\": 0.0495, \"truncated\": 2}, \"notes\": \"α=1.0 SFT eval (N=100, greedy) 运行中。PID 42535 on GPU 1 (westd). 33/100 samples at 15:05 UTC, ~4-5s/sample, 预计 5-6 min 完成。Cron 已注册。\", \"parent\": \"sft-alpha-1p0\", \"reproduce\": {\"finished_at\": \"2026-05-15T15:22:49.510Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_1.0\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_1.0\", \"command\": \"python eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_1.0 --n_samples 100\", \"data_count\": 100, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k_test_n100\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.56, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval-sft-alpha-1p0.log\", \"model_name\": \"Qwen2.5-7B pruned alpha=1.0 post-SFT\", \"pid\": \"42530\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-15T14:51:22.611Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2013.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:29:36.910Z\"}, \"eval_sft_unpruned_n100\": {\"completed_at\": \"2026-05-16T01:40:33.108Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T01:40:17.686Z\", \"hypothesis\": \"Unpruned post-SFT achieves ~84% GSM8K on N=100 subset, providing quick baseline confirmation consistent with full eval for three-way pruning method comparison\", \"metrics\": {\"accuracy\": 0.84, \"avg_response_length\": 187.22, \"eos_rate\": 1, \"n_correct\": 84, \"n_total\": 100, \"stderr\": 0.0367}, \"parent\": \"sft_unpruned_baseline\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/recovery_aware_struct_prune/results/eval_sft_unpruned_baseline_n100.json\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_unpruned_baseline\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python eval_gsm8k.py --model_path sft_unpruned_baseline --max_samples 100 --seed 42\", \"data_count\": 100, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k_test_n100\", \"log_path\": \"/tmp/eval_unpruned_n100.log\", \"model_name\": \"Qwen2.5-7B (unpruned, SFT)\", \"parent\": \"sft_unpruned_baseline\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:29:35.970Z\"}, \"eval_sft_unpruned_full\": {\"completed_at\": \"2026-05-16T02:45:56.559Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T01:40:17.174Z\", \"hypothesis\": \"Unpruned post-SFT achieves >80% GSM8K on full test set (N=1319), establishing accuracy ceiling for pruned model SFT recovery comparison and confirming SFT effectiveness intact (C1/C3 control)\", \"metrics\": {\"accuracy\": 81.27, \"accuracy_ci\": 1.07, \"avg_response_length\": 207.18, \"correct\": 1072, \"eos_rate\": 99.7, \"total\": 1319, \"truncated\": 4}, \"notes\": \"Unpruned SFT N=1319 full eval on westd cuda:0. PID 74129, ~2.5s/it. Started 09:39 UTC. Progress at 09:46 UTC: 155/1319 (12%), acc=86.67% (at 150), eos_rate=100%, avg_len=188. ETA ~10:35 UTC. Model: /root/autodl-tmp/recovery_aware_struct_prune/sft_unpruned_baseline. N=100 checkpoint: 84% (84/100). Three-way comparison pending: Standard 59.29%, RASP 61.49%, Unpruned ?%.\", \"parent\": \"sft_unpruned_baseline\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/recovery_aware_struct_prune/results/eval_sft_unpruned_baseline_full.json\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_unpruned_baseline\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python eval_gsm8k.py --model_path sft_unpruned_baseline --max_samples 1319 --seed 42\", \"data_count\": 1319, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k_test_full_1319\", \"gpu\": \"cuda:0\", \"hypothesis\": \"Unpruned SFT baseline full GSM8K eval for three-way comparison\", \"log_path\": \"/tmp/eval_unpruned_full.log\", \"model_name\": \"Qwen2.5-7B (unpruned, SFT)\", \"parent\": \"sft_unpruned_baseline\", \"pid\": 74129, \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:29:35.056Z\"}, \"eval_grpo_unpruned_v2_step90\": {\"completed_at\": \"2026-05-16T05:22:28.433Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T03:05:00.333Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-16T05:21:01.910684+00:00\"}]}, \"hypothesis\": \"Unpruned model GRPO step-90 shows accuracy tracking reward throughout training, confirming reward-accuracy coupling is intact when no structural pruning damage exists (C1 control)\", \"metrics\": {\"accuracy\": 80.59, \"avg_response_length\": 213, \"correct\": 1063, \"eos_rate\": 99.6, \"seed\": 42, \"total\": 1319}, \"parent\": \"grpo_unpruned_v2\", \"reproduce\": {\"finished_at\": \"2026-05-16T05:20:55.145Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_unpruned_v2/checkpoint-90\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_unpruned_v2/checkpoint-90 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_unpruned_v2_step90.json\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 1.72, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_grpo_unpruned_v2_step90.log\", \"pid\": \"83667\", \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-16T03:39:13.660Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 6194.8}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:29:34.226Z\"}, \"eval_grpo_unpruned_v2_step100\": {\"completed_at\": \"2026-05-16T05:22:27.217Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T03:04:55.936Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-16T05:20:51.768048+00:00\"}]}, \"hypothesis\": \"Unpruned model GRPO step-100 achieves >80% GSM8K accuracy, proving reward-accuracy coupling holds without structural damage and decoupling is pruning-specific (C1 control)\", \"metrics\": {\"accuracy\": 81.27, \"avg_response_length\": 209, \"correct\": 1072, \"eos_rate\": 99.7, \"seed\": 42, \"total\": 1319}, \"parent\": \"grpo_unpruned_v2\", \"reproduce\": {\"finished_at\": \"2026-05-16T05:20:49.514Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_unpruned_v2/checkpoint-100\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_unpruned_v2/checkpoint-100 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_unpruned_v2_step100.json\\\"\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 1.72, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_grpo_unpruned_v2_step100.log\", \"pid\": \"83589\", \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-16T03:39:11.392Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 6195.8}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:29:33.203Z\"}, \"sft_rasp_25\": {\"completed_at\": \"2026-05-16T06:17:10.629Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T05:26:38.517Z\", \"hypothesis\": \"RASP 25% pruned model recovers higher GSM8K accuracy post-SFT than Standard 25% because CKA-preserved functional redundancy enables more efficient gradient-based recovery (C3)\", \"metrics\": {\"runtime_seconds\": 1635, \"token_accuracy\": 0.8073, \"train_loss\": 0.8498}, \"parent\": \"prune_rasp_25\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_25\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_25 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_25 --num_train_epochs 2 --learning_rate 2e-5 --batch_size 1 --gradient_accumulation_steps 8 --max_seq_length 2048 --seed 42\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 0.83, \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_rasp_25.log\", \"model_name\": \"pruned_rasp_25 (RASP 25% pruned DeepSeek-R1-Distill-Qwen-7B)\", \"pid\": \"88528\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-16T05:27:08.163Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 3002.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:29:32.685Z\"}, \"sft_standard_25\": {\"completed_at\": \"2026-05-16T05:35:39.684Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T05:21:16.758Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\"}}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"hypothesis\": \"Standard 25% pruned DeepSeek-R1-Distill-Qwen-7B recovers partial accuracy via SFT but below RASP 25% because magnitude-only pruning destroys recovery-critical redundancy (C3)\", \"metrics\": {\"model_keys\": 339, \"model_params\": \"5.79B\", \"note\": \"optimizer.pt save failed (RuntimeError) but model.safetensors intact\", \"runtime_seconds\": 2130, \"total_steps\": 1870}, \"parent\": \"prune_standard_25\", \"retry_count\": 1, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_25 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25 --gpu 1 --num_train_epochs 2 --learning_rate 2e-5 --batch_size 1 --gradient_accumulation_steps 8 --max_seq_length 2048 --seed 42\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/sft_standard_25_retry.log\", \"model_name\": \"pruned_standard_25 (Standard 25% pruned DeepSeek-R1-Distill-Qwen-7B)\", \"seed\": 42, \"server\": \"westb-23072\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:29:22.232Z\"}, \"sft_standard_25_westd\": {\"completed_at\": \"2026-05-16T16:47:03.556Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T15:52:30.818Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-16T16:47:05.612374+00:00\"}]}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"hypothesis\": \"Standard 25% pruned DeepSeek-R1-Distill-Qwen-7B SFT recovery yields lower GSM8K accuracy than RASP 25% due to irreversible functional redundancy destruction (C3 25% extension)\", \"metrics\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/model.safetensors\", \"final_loss\": 0.8381, \"token_acc\": 0.8018}, \"parent\": \"prune_standard_25\", \"reproduce\": {\"finished_at\": \"2026-05-16T16:47:02.031Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_25 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25 --gpu 1 --learning_rate 2e-5 --num_train_epochs 2 --batch_size 1 --gradient_accumulation_steps 8 --max_seq_length 2048 --seed 42\\\"\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.91, \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_standard_25_westd.log\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (Standard 25% pruned)\", \"pid\": \"21488\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-16T15:52:30.596Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 3273.0}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:29:21.686Z\"}, \"eval_grpo_rasp_20_qwen_math\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_rasp_20_qwen_math.json\", \"completed_at\": \"2026-05-16T16:30:45.885Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T15:59:57.504Z\", \"hypothesis\": \"RASP 20% pruned Qwen Math post-GRPO shows accuracy plateau despite reward improvement, confirming C1 decoupling occurs regardless of pruning method on second model\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_rasp_20_qwen_math.log\", \"metrics\": {\"accuracy\": 0.725, \"n_samples\": 200, \"seed\": 42}, \"parent\": \"grpo_rasp_qwen_math_v3\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_qwen_math\", \"command\": \"CUDA_VISIBLE_DEVICES=2 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_qwen_math --max_samples 200 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_rasp_20_qwen_math.json\", \"data_count\": 200, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k\", \"gpu\": \"cuda:2\", \"hypothesis\": \"Qwen2.5-Math-7B RASP 20% post-GRPO GSM8K eval (N=200, seed=42). 验证 GRPO 后 accuracy 变化，reward-accuracy decoupling 证据 (C1)。Parent: grpo_rasp_qwen_math_v3.\", \"model_name\": \"Qwen2.5-Math-7B-RASP-20%-postGRPO\", \"parent\": \"grpo_rasp_qwen_math_v3\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:29:20.851Z\"}, \"eval_grpo_standard_20_qwen_math\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_standard_20_qwen_math.json\", \"completed_at\": \"2026-05-16T16:30:46.768Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T15:59:59.175Z\", \"hypothesis\": \"Standard 20% pruned Qwen Math post-GRPO shows accuracy plateau below unpruned despite reward improvement, confirming reward-accuracy decoupling is cross-model (C1)\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_standard_20_qwen_math.log\", \"metrics\": {\"accuracy\": 0.705, \"n_samples\": 200, \"seed\": 42}, \"parent\": \"grpo_standard_qwen_math_v3\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_qwen_math\", \"command\": \"CUDA_VISIBLE_DEVICES=3 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_qwen_math --max_samples 200 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_standard_20_qwen_math.json\", \"data_count\": 200, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k\", \"gpu\": \"cuda:3\", \"hypothesis\": \"Qwen2.5-Math-7B Standard 20% post-GRPO GSM8K eval (N=200, seed=42). 验证 GRPO 后 accuracy 变化，reward-accuracy decoupling 证据 (C1)。Parent: grpo_standard_qwen_math_v3.\", \"model_name\": \"Qwen2.5-Math-7B-Standard-20%-postGRPO\", \"parent\": \"grpo_standard_qwen_math_v3\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:29:19.801Z\"}, \"eval_grpo_rasp_25_qwen_math\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_rasp_25_qwen_math.json\", \"completed_at\": \"2026-05-16T16:30:47.624Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T15:59:53.951Z\", \"hypothesis\": \"RASP 25% pruned Qwen Math post-GRPO shows reward-accuracy decoupling on GSM8K, confirming C1 generalizes to higher sparsity on second model family\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_rasp_25_qwen_math.log\", \"metrics\": {\"accuracy\": 0.625, \"n_samples\": 200, \"seed\": 42}, \"parent\": \"grpo_rasp_25_qwen_math\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_25_qwen_math\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_25_qwen_math --max_samples 200 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_rasp_25_qwen_math.json\", \"data_count\": 200, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k\", \"gpu\": \"cuda:0\", \"hypothesis\": \"Qwen2.5-Math-7B RASP 25% post-GRPO GSM8K eval (N=200, seed=42). 验证 GRPO 后 accuracy 变化，reward-accuracy decoupling 证据 (C1)。Parent: grpo_rasp_25_qwen_math.\", \"model_name\": \"Qwen2.5-Math-7B-RASP-25%-postGRPO\", \"parent\": \"grpo_rasp_25_qwen_math\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:29:18.878Z\"}, \"eval_pass_k8_unpruned_qwen_math\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_pass_k8_unpruned_qwen_math.json\", \"completed_at\": \"2026-05-16T18:00:04.086Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T16:43:10.425Z\", \"hypothesis\": \"Unpruned Qwen Math post-GRPO achieves near-ceiling pass@8 on GSM8K, establishing that GRPO preserves solution diversity when no structural pruning damage exists (C1 control)\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_pass_k8_unpruned_qwen_math.log\", \"metrics\": {\"accuracy\": 0.965, \"k\": 8, \"n_samples\": 200, \"pass_at_k\": 0.965, \"stderr\": 0.013, \"temperature\": 0.7}, \"parent\": \"grpo_unpruned_v2\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_unpruned_v2\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_unpruned_v2 --max_samples 200 --seed 42 --pass_k 8 --temperature 0.7 --num_samples_per_prompt 8 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_pass_k8_unpruned_qwen_math.json\", \"data_count\": 200, \"data_path\": \"GSM8K\", \"eval_data\": \"GSM8K (N=200, pass@8, T=0.7)\", \"gpu\": \"cuda:1\", \"model_name\": \"grpo_unpruned_v2\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:29:17.923Z\"}, \"eval_pass_k8_rasp_20_grpo_qwen_math\": {\"completed_at\": \"2026-05-16T18:13:49.651Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T16:43:12.096Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-16T18:13:51.489018+00:00\"}]}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"hypothesis\": \"RASP 20% post-GRPO on Qwen Math shows pass@8 below unpruned baseline, indicating GRPO fails to recover full solution diversity on structurally pruned models (C1 diversity)\", \"metrics\": {\"accuracy\": 0.915, \"k\": 8, \"n_samples\": 200, \"pass_at_k\": 0.915, \"stderr\": 0.0197, \"temperature\": 0.7}, \"parent\": \"grpo_rasp_qwen_math_v3\", \"reproduce\": {\"finished_at\": \"2026-05-16T18:13:48.390Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_qwen_math\", \"command\": \"CUDA_VISIBLE_DEVICES=3 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_qwen_math --max_samples 200 --seed 42 --pass_k 8 --temperature 0.7 --num_samples_per_prompt 8 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_pass_k8_rasp_20_grpo_qwen_math.json\", \"data_count\": 200, \"data_path\": \"GSM8K\", \"eval_data\": \"GSM8K (N=200, pass@8, T=0.7)\", \"gpu\": \"cuda:3\", \"model_name\": \"grpo_rasp_qwen_math\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:29:16.961Z\"}, \"eval_grpo_standard_25_qwen_math\": {\"completed_at\": \"2026-05-16T18:47:10.092Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T15:59:55.747Z\", \"hypothesis\": \"Standard 25% pruned Qwen Math post-GRPO exhibits reward-accuracy decoupling on GSM8K, confirming C1 generalizes across sparsity levels on second model family\", \"metrics\": {\"accuracy\": 0.635, \"n_samples\": 200, \"seed\": 42}, \"parent\": \"grpo_standard_25_qwen_math\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25_qwen_math\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25_qwen_math\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25_qwen_math --max_samples 200 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_standard_25_qwen_math.json\", \"data_count\": 200, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Qwen2.5-Math-7B Standard 25% post-GRPO GSM8K eval (N=200, seed=42). 验证 GRPO 后 accuracy 变化，reward-accuracy decoupling 证据 (C1)。Parent: grpo_standard_25_qwen_math.\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_standard_25_qwen_math.json\", \"model_name\": \"Qwen2.5-Math-7B-Standard-25%-postGRPO\", \"parent\": \"grpo_standard_25_qwen_math\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:29:14.637Z\"}, \"eval_pass_k8_rasp_20_sft_qwen_math\": {\"completed_at\": \"2026-05-16T18:30:20.418Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T16:43:11.344Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-16T18:30:22.400738+00:00\"}]}, \"failure_reason\": null, \"hypothesis\": \"RASP 20% pruned Qwen Math post-SFT maintains high pass@8 near unpruned level because preserved functional redundancy supports multiple diverse reasoning paths (C1 diversity)\", \"metrics\": {\"avg_response_length\": 139.86, \"eos_rate\": 0.99625, \"k\": 8, \"n_problems\": 200, \"natural_eos\": 1594, \"pass_at_k\": 0.935, \"stderr\": 0.0174, \"temperature\": 0.7, \"truncated\": 6}, \"parent\": \"sft_rasp_20_qwen_math\", \"reproduce\": {\"finished_at\": \"2026-05-16T18:30:19.034Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_rasp_20\", \"command\": \"CUDA_VISIBLE_DEVICES=2 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_rasp_20 --max_samples 200 --seed 42 --pass_k 8 --temperature 0.7 --num_samples_per_prompt 8 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_pass_k8_rasp_20_sft_qwen_math.json\", \"data_count\": 200, \"data_path\": \"GSM8K\", \"eval_data\": \"GSM8K (N=200, pass@8, T=0.7)\", \"gpu\": \"cuda:2\", \"model_name\": \"sft_qwen_math_rasp_20\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:29:13.689Z\"}, \"sft-alpha-1p0\": {\"completed_at\": \"2026-05-15T14:28:01.989Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-15T13:53:32.178Z\", \"hypothesis\": \"SFT on alpha=1.0 pruned model (full CKA weight) recovers to level matching RASP default because alpha=1.0 IS the standard RASP scoring function (C2 ablation consistency)\", \"metrics\": {\"post_prune_accuracy\": 0.27, \"token_accuracy\": 0.83, \"total_steps\": 1870, \"train_loss_final\": 0.64, \"train_time_min\": 28}, \"notes\": \"α=1.0 SFT 完成 (1870/1870 steps, 2 epochs, ~28min). loss=0.64, token_acc=0.83. Post-prune 27% → post-SFT 需 eval 确认 (预期 ~57% 与 sft_rasp_20 一致，因 α=1.0 = RASP default). Checkpoint: /root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_1.0\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_1.0\", \"command\": \"python -u src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/alpha_ablation/alpha_1.0 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_1.0 --gpu 1 --num_train_epochs 2 --learning_rate 2e-5 --batch_size 1 --gradient_accumulation_steps 8 --max_seq_length 2048 --logging_steps 10 --seed 42\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.57, \"log_path\": \"~/runs/recovery_aware_struct_prune/sft-alpha-1p0.log\", \"model_name\": \"pruned_alpha1.0 (α=1.0, 20% sparsity)\", \"pid\": \"38797\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-15T13:53:32.117Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2069.9}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:28:07.214Z\"}, \"prune_rasp_30\": {\"completed_at\": \"2026-05-16T09:04:22.915Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T09:03:45.925Z\", \"hypothesis\": \"RASP scoring at 30% sparsity maintains measurably higher post-prune accuracy than standard, testing whether CKA-preservation delays the structural collapse threshold\", \"metrics\": {\"actual_sparsity\": 0.2873, \"attn_groups_pruned\": \"0/112\", \"mlp_groups_pruned\": \"301/784\", \"model_size_gb\": 11, \"params_pruned\": 5427842560, \"target_sparsity\": 0.3}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_30\", \"command\": \"python src/prune.py --model_path /root/autodl-tmp/models/DeepSeek-R1-Distill-Qwen-7B --mode rasp --sparsity 0.30 --alpha 1.0 --dtype bfloat16 --importance_path results/importance_scores.pt --cka_path results/cka_scores.pt\", \"data_count\": 512, \"data_path\": \"calibration data\", \"log_path\": \"N/A (CPU)\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"server\": \"westb-23072\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:28:01.089Z\"}, \"prune_standard_30\": {\"completed_at\": \"2026-05-16T09:09:17.139Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T09:06:31.546Z\", \"hypothesis\": \"Standard importance at 30% sparsity crosses structural collapse threshold where post-prune accuracy approaches zero, defining upper bound of viable pruning for DeepSeek-R1-Distill-Qwen-7B\", \"metrics\": {\"actual_sparsity\": 0.2854, \"attn_gqa_groups_pruned\": \"0/112\", \"mlp_groups_pruned\": \"299/784\", \"params_after\": 5442379264, \"target_sparsity\": 0.3}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_30/\", \"command\": \"CUDA_VISIBLE_DEVICES='' python src/prune.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --mode standard --sparsity 0.30 --dtype bfloat16 --importance_path results/importance_scores.pt --output_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_30\", \"data_count\": 0, \"data_path\": \"results/importance_scores.pt\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/logs/workers/worker_ops_prune_standard_30_20260516T090533.log\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"server\": \"westb-23072\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:27:59.680Z\"}, \"prune_rasp_25_qwen_math\": {\"completed_at\": \"2026-05-16T11:00:32.812Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T09:30:44.270Z\", \"hypothesis\": \"RASP CKA-weighted scoring at 25% on Qwen2.5-Math-7B preserves functionally redundant groups, maintaining higher post-prune accuracy than standard at same sparsity (C3 cross-model)\", \"metrics\": {\"actual_sparsity\": 0.2405, \"attn_gqa_groups_pruned\": \"0/112\", \"mlp_groups_pruned\": \"252/784\", \"params_after\": 5783991808, \"target_sparsity\": 0.25}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_25_qwen_math/\", \"command\": \"CUDA_VISIBLE_DEVICES='' python src/prune.py --model_path /root/autodl-tmp/models/Qwen2.5-Math-7B --mode rasp --sparsity 0.25 --alpha 1.0 --dtype bfloat16 --importance_path results/importance_scores.pt --cka_path results/cka_scores.pt --output_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_25_qwen_math\", \"data_count\": 0, \"data_path\": \"results/importance_scores.pt + results/cka_scores.pt\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/logs/workers/worker_ops_westd_disk_cleanup_qwen25_20260516T105526.log\", \"model_name\": \"Qwen2.5-Math-7B\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:27:58.263Z\"}, \"prune_standard_25_qwen_math\": {\"completed_at\": \"2026-05-16T11:00:50.302Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T11:00:13.880Z\", \"hypothesis\": \"Standard importance at 25% on Qwen2.5-Math-7B removes groups by magnitude alone, destroying more functional redundancy than RASP at equal sparsity (C3 cross-model baseline)\", \"metrics\": {\"actual_sparsity\": 0.2396, \"attn_gqa_groups_pruned\": \"0/112\", \"mlp_groups_pruned\": \"251/784\", \"target_sparsity\": 0.25}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_25_qwen_math/\", \"command\": \"CUDA_VISIBLE_DEVICES='' python src/prune.py --model_path /root/autodl-tmp/models/Qwen2.5-Math-7B --mode standard --sparsity 0.25 --dtype bfloat16 --importance_path results/importance_scores.pt --output_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_25_qwen_math\", \"data_count\": 0, \"data_path\": \"results/importance_scores.pt\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/logs/workers/worker_ops_westd_disk_cleanup_qwen25_20260516T105526.log\", \"model_name\": \"Qwen2.5-Math-7B\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:27:56.876Z\"}, \"prune_rasp_rlvr_20_qwen_math\": {\"completed_at\": \"2026-05-16T17:11:24.806Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T17:11:05.915Z\", \"hypothesis\": \"RASP-RLVR scoring on Qwen2.5-Math-7B at 20% sparsity preserves RLVR-relevant functional groups, yielding higher post-prune reasoning accuracy than standard importance (C3 cross-model)\", \"metrics\": {\"actual_sparsity\": 0.1909, \"attn_groups_pruned\": 0, \"attn_groups_total\": 112, \"mlp_groups_pruned\": 200, \"mlp_groups_total\": 784, \"pruned_params\": 6161946112}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_rlvr_20_qwen_math\", \"command\": \"python src/prune.py --mode rasp-rlvr --sparsity 0.20\", \"data_count\": 0, \"data_path\": \"N/A\", \"log_path\": \"/tmp/prune_rasp_rlvr_qwen_math.log\", \"model_name\": \"Qwen2.5-Math-7B\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:27:55.586Z\"}, \"eval_pass_k8_rasp_20_grpo_deepseek\": {\"completed_at\": \"2026-05-17T00:20:11.075Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T23:27:01.192Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-17T00:20:15.777602+00:00\"}]}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"hypothesis\": \"DeepSeek-R1-Distill-Qwen-7B RASP 20% post-GRPO pass@k=8 (N=200, T=0.7, seed=42). C1 diversity 验证：RASP collapse 模型的 sampling diversity。构建 pass@k 2×2 矩阵。Parent: grpo_stage2_rasp_20_v9.\", \"metrics\": {\"n_problems\": 200, \"pass_k8\": 0.89, \"temperature\": 0.7}, \"notes\": \"Cron auto-resolved as failed (5/5 miss on old PID 60022). 实际进程 PID 61473 仍在正常运行（已多次 SSH 确认，GPU 0 占用 12982MiB, 99% util, 进度 32% at 00:42 UTC）。参数已修正为 eval_pass_k.py + max_new_tokens=4096。等完成后手动收割结果更新 conclusion。\", \"parent\": \"grpo_stage2_rasp_20_v9\", \"reproduce\": {\"finished_at\": \"2026-05-17T00:20:12.488Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9\", \"checkpoint_source\": \"grpo_stage2_rasp_20_v9\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python eval_pass_k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9 --k 8 --temperature 0.7 --max_samples 200 --seed 42 --max_new_tokens 4096 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_pass_k8_rasp_20_grpo_deepseek.json\", \"data_count\": 200, \"data_path\": \"gsm8k_test\", \"eval_data\": \"gsm8k_test\", \"gpu\": \"cuda:0\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_pass_k8_rasp_20_grpo_deepseek.log\", \"metrics\": {\"avg_response_length\": 162.58, \"eos_rate\": 0.995, \"k\": 8, \"n_problems\": 200, \"pass_at_k\": 0.89, \"stderr\": 0.0221, \"temperature\": 0.7, \"truncated\": 8}, \"model_name\": \"grpo_stage2_rasp_20_v9\", \"pid\": \"61473\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:15:54.640Z\"}, \"eval_pass_k8_standard_20_grpo_deepseek\": {\"completed_at\": \"2026-05-17T01:56:11.192Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T23:31:55.162Z\", \"hypothesis\": \"DeepSeek-R1-Distill-Qwen-7B Standard 20% post-GRPO pass@k=8 (N=200, T=0.7, seed=42). C1 diversity 验证：Standard collapse 模型的 sampling diversity。完成 pass@k 2×2 矩阵。Parent: grpo_stage2_standard_20_v8.\", \"parent\": \"grpo_stage2_standard_20_v8\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50\", \"command\": \"CUDA_VISIBLE_DEVICES=2 python eval_pass_k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50 --k 8 --temperature 0.7 --max_samples 200 --seed 42 --max_new_tokens 4096 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_pass_k8_standard_20_grpo_deepseek.json\", \"data_count\": 200, \"data_path\": \"openai/gsm8k (test split, N=200)\", \"eval_data\": \"GSM8K test (200 samples, pass@k=8, T=0.7)\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_pass_k8_standard_20_grpo_deepseek.log\", \"metrics\": {\"avg_response_length\": 164.15, \"eos_rate\": 0.9956, \"k\": 8, \"n_problems\": 200, \"pass_at_k\": 0.855, \"stderr\": 0.0249, \"temperature\": 0.7}, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B Standard 20% post-GRPO\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T01:56:11.192Z\"}, \"eval_sft_rasp_20_full\": {\"completed_at\": \"2026-05-17T01:29:36.754Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-15T16:21:29.964Z\", \"hypothesis\": \"RASP post-SFT full GSM8K eval (N=1319, greedy, seed=42). N=100 result: 57%. Full eval provides statistical significance for RASP vs Standard comparison. Parent: sft_rasp_20.\", \"metrics\": {\"accuracy\": 0.6156, \"avg_response_length\": 210.95, \"eos_rate\": 0.9841, \"n_correct\": 812, \"n_samples\": 1319, \"natural_eos\": 1298, \"stderr\": 0.0134, \"truncated\": 21}, \"parent\": \"sft_rasp_20\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_sft_rasp_20_full_n1319.json\", \"data_count\": 1319, \"data_path\": \"gsm8k:test\", \"eval_data\": \"gsm8k:test:1319\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_sft_rasp_20_full.log\", \"model_name\": \"sft_rasp_20\", \"seed\": 42, \"server\": \"westb-23072\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T01:29:36.754Z\"}, \"inference_speedup_plan016_v2\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/inference_benchmark.json\", \"completed_at\": \"2026-05-16T22:23:11.645Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T21:56:34.646Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-16T22:23:15.603802+00:00\"}]}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"hypothesis\": \"Inference speedup benchmark v2 (code fix applied): Dense vs RASP 20% vs Standard 20%. 测量 wall-clock latency, tokens/s, memory_peak. 50 GSM8K prompts, batch_size=1, greedy, max_new_tokens=512. Parent: inference_speedup_plan016 (failed due to model loading bug, now fixed with load_pruned_model).\", \"metrics\": {\"dense\": {\"avg_latency_sec\": 6.682, \"peak_memory_gb\": 16.22, \"tokens_per_second\": 76.25}, \"rasp_20\": {\"avg_latency_sec\": 4.156, \"latency_speedup_vs_dense\": \"37.8%\", \"memory_reduction_vs_dense\": \"28.5%\", \"peak_memory_gb\": 11.6, \"tokens_per_second\": 52.07}, \"standard_20\": {\"avg_latency_sec\": 6.167, \"latency_speedup_vs_dense\": \"7.7%\", \"memory_reduction_vs_dense\": \"28.4%\", \"peak_memory_gb\": 11.61, \"tokens_per_second\": 49.78}}, \"parent\": \"inference_speedup_plan016\", \"reproduce\": {\"finished_at\": \"2026-05-16T22:23:10.199Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"sft_rasp_20 + sft_standard_20 + dense\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python src/benchmark_inference.py --dense_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --rasp_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20 --standard_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20 --n_prompts 50 --max_new_tokens 512\", \"data_count\": 50, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"GSM8K test 50 prompts (inference latency benchmark)\", \"gpu\": \"cuda:1\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/inference_bench.log\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (dense/rasp_20/standard_20)\", \"seed\": 42, \"server\": \"westb-23072\", \"tmux_session\": \"inference_bench\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T00:49:42.978Z\"}, \"eval_pass_k8_standard_20_grpo_qwen_math_v2\": {\"completed_at\": \"2026-05-16T23:21:50.021Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T21:54:25.214Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-16T23:21:53.898541+00:00\"}]}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed. Worker diagnosing root cause.\", \"hypothesis\": \"Qwen2.5-Math-7B Standard 20% post-GRPO pass@k=8 (N=200, T=0.7, seed=42). C1 diversity 对照：frac_zero=0.85 collapse 模型的 sampling diversity。重跑 v1（僵尸进程被 kill）。Parent: grpo_standard_qwen_math_v3.\", \"parent\": \"grpo_standard_qwen_math_v3\", \"reproduce\": {\"finished_at\": \"2026-05-16T23:21:48.638Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_qwen_math\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_qwen_math\", \"command\": \"CUDA_VISIBLE_DEVICES=2 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_qwen_math --pass_k 8 --num_samples_per_prompt 8 --temperature 0.7 --max_samples 200 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_pass_k8_standard_20_grpo_qwen_math_v2.json\", \"data_count\": 200, \"data_path\": \"gsm8k test split\", \"eval_data\": \"gsm8k test (200 samples)\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_pass_k8_standard_20_v2.log\", \"metrics\": {\"avg_response_length\": 129.995, \"eos_rate\": 0.999375, \"k\": 8, \"n_problems\": 200, \"natural_eos\": 1599, \"pass_at_k\": 0.91, \"stderr\": 0.0202, \"temperature\": 0.7, \"truncated\": 1}, \"model_name\": \"Qwen2.5-Math-7B-Standard-20%-post-GRPO\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T23:23:37.778Z\"}, \"eval_grpo_rasp_rlvr_20_qwen_math\": {\"completed_at\": \"2026-05-16T20:18:05.252Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T19:39:30.069Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-16T20:18:07.204564+00:00\"}]}, \"failure_reason\": null, \"hypothesis\": \"Qwen2.5-Math-7B RASP-RLVR 20% post-GRPO GSM8K eval (N=200, greedy, seed=42). GRPO reward=0.090(最高)，验证 accuracy 是否也改善或依然 decoupling (C1)。对比 pre-GRPO: 73%. Parent: grpo_rasp_rlvr_20_qwen_math.\", \"metrics\": {\"accuracy\": 0.71, \"mode\": \"greedy\", \"n_samples\": 200, \"seed\": 42}, \"notes\": \"Cron 误判 (eval 无 W&B 信号)。实际成功完成。Post-GRPO accuracy 71.0% vs pre-GRPO SFT 73%: Δ=-2pp, 确认 C1 universal decoupling (reward=0.090 最高但 accuracy 不升反微降)。EOS=100%, avg_len=128, 生成行为正常。\", \"parent\": \"grpo_rasp_rlvr_20_qwen_math\", \"reproduce\": {\"finished_at\": \"2026-05-16T20:18:03.885Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_rlvr_20_qwen_math\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_rlvr_20_qwen_math --max_samples 200 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_rasp_rlvr_20_qwen_math.json\", \"data_count\": 200, \"data_path\": \"gsm8k\", \"eval_data\": \"gsm8k\", \"model_name\": \"grpo_rasp_rlvr_20_qwen_math\", \"parent\": \"grpo_rasp_rlvr_20_qwen_math\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T20:25:58.464Z\"}, \"eval_postprune_rasp_25\": {\"completed_at\": \"2026-05-16T08:07:24.066Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T08:07:02.187Z\", \"hypothesis\": \"25% RASP post-prune GSM8K eval (N=100, greedy). 对比 20% post-prune (31%). Parent: pruned_rasp_25.\", \"metrics\": {\"accuracy\": 21, \"avg_response_length\": 2032.9, \"correct\": 21, \"eos_rate\": 56, \"natural_eos\": 56, \"seed\": 42, \"stderr\": 4.07, \"total\": 100, \"truncated\": 44}, \"parent\": \"prune_rasp_25\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_postprune_rasp_25.json\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_25\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_25 --max_samples 100 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_postprune_rasp_25.json\", \"data_count\": 100, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"openai/gsm8k test split (N=100)\", \"log_path\": \"N/A\", \"model_name\": \"pruned_rasp_25 (RASP 25% pruned, no SFT)\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T20:09:54.911Z\"}, \"grpo_rasp_rlvr_20_qwen_math\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_rlvr_20_qwen_math/\", \"completed_at\": \"2026-05-16T19:38:28.565Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T19:37:40.324Z\", \"hypothesis\": \"Qwen2.5-Math-7B RASP-RLVR 20% post-GRPO (100 steps). RLVR 剪枝后 SFT→GRPO 全管线。对比 grpo_rasp_qwen_math_v3 (regular RASP, reward=0.061) 和 grpo_standard_qwen_math_v3 (Standard, reward=0.044)。D050 ablation: RLVR 是否在 Qwen Math 上提供额外 GRPO 恢复能力。Parent: sft_rasp_rlvr_20_qwen_math.\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/grpo_rasp_rlvr_20_qwen_math.log\", \"metrics\": {\"clipped_ratio\": 0.54, \"comparison_vs_rasp_20\": \"RLVR reward 0.090 > RASP 0.061 (+48%), entropy 0.275 >> 0.073 (3.8x)\", \"comparison_vs_standard_20\": \"RLVR reward 0.090 >> Standard 0.044 (+105%)\", \"entropy_final\": 0.275, \"frac_zero_std_final\": 0.7, \"grad_norm_final\": 16.125, \"kl_final\": 0.00581, \"kl_spike_recovery\": \"immediate\", \"kl_spike_step70\": 5756.85, \"loss_final\": 0.0793, \"reward_final\": 0.09, \"reward_std_final\": 0.234, \"total_steps\": 100, \"wall_clock_min\": 45.8, \"wandb_run_id\": \"clzm2cy4\"}, \"parent\": \"sft_rasp_rlvr_20_qwen_math\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_rlvr_20_qwen_math\", \"command\": \"python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_rlvr_20_qwen_math --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_rlvr_20_qwen_math --gpu 0 --max_steps 100 --run_name grpo_rasp_rlvr_20_qwen_math --seed 42\", \"data_count\": null, \"data_path\": \"built-in GSM8K\", \"eval_data\": \"GSM8K (built-in GRPO reward)\", \"gpu\": \"cuda:0\", \"model_name\": \"Qwen2.5-Math-7B (RASP-RLVR 20% pruned, SFT recovered)\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T20:02:41.614Z\"}, \"eval_sft_rasp_25\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_sft_rasp_25.json\", \"completed_at\": \"2026-05-16T19:15:43.879Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T06:17:33.814Z\", \"failure_reason\": \"Killed on westd due to GPU stall (10+h est). Restarting on westb-23072 cuda:0.\", \"hypothesis\": \"RASP 25% post-SFT GSM8K eval (N=1319, greedy, seed=42). sft_rasp_25 刚完成 (loss=0.8498, token_acc=0.8073)，对比 sft_standard_25 (待完成) 和 20% sparsity 结果 (RASP 57% vs Standard 64%)。Parent: sft_rasp_25.\", \"metrics\": {\"accuracy\": 0.5299, \"eos_rate\": 0.918, \"n_correct\": 699, \"n_samples\": 1319, \"seed\": 42, \"stderr\": 0.0137, \"truncated\": 108}, \"parent\": \"sft_rasp_25\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_25\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_25 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_sft_rasp_25.json\", \"data_count\": 1319, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"openai/gsm8k test split\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_sft_rasp_25.log\", \"model_name\": \"sft_rasp_25 (RASP 25% SFT recovered)\", \"pid\": \"602990\", \"seed\": 42, \"server\": \"westb-23072\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T19:15:43.879Z\"}, \"sft_rasp_rlvr_20_qwen_math\": {\"completed_at\": \"2026-05-16T17:50:56.549Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T17:11:51.076Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-16T17:50:58.470427+00:00\"}]}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"hypothesis\": \"Qwen2.5-Math-7B RASP-RLVR 20% SFT recovery (2 epochs). 验证反向 CKA 剪枝后的恢复质量。\", \"reproduce\": {\"finished_at\": \"2026-05-16T17:50:55.281Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_rlvr_20_qwen_math\", \"command\": \"python src/sft_recovery.py --model_path pruned_rasp_rlvr_20_qwen_math --num_train_epochs 2 --lr 2e-5\", \"data_count\": 0, \"data_path\": \"built-in SFT data\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/sft_rasp_rlvr_20_qwen_math.log\", \"model_name\": \"Qwen2.5-Math-7B (RASP-RLVR pruned 20%)\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T18:01:41.992Z\"}, \"grpo_rasp_qwen_math_v3\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_qwen_math/\", \"completed_at\": \"2026-05-16T15:50:13.550Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T14:49:39.708Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-16T15:43:36.937539+00:00\"}]}, \"hypothesis\": \"Qwen2.5-Math-7B RASP 20% GRPO v3 (100 steps, save_steps=100). 跨模型验证 C1/C2. 修复 save_steps=5 磁盘膨胀问题。Parent: sft_qwen_math_rasp_20.\", \"metrics\": {\"clipped_ratio_final\": 0.975, \"clipped_ratio_mean\": 0.981, \"collapse_onset\": \"step1\", \"collapse_pattern\": \"entropy_length_collapse\", \"cross_model_match\": \"partial\", \"entropy_mean\": 0.073, \"entropy_vs_standard_ratio\": 0.39, \"frac_zero_std_final\": 0.675, \"frac_zero_std_max\": 0.7, \"frac_zero_std_min\": 0.55, \"kl_final\": 0.009, \"llama_pattern\": \"permanent_reward_collapse\", \"mean_completion_length\": 1010, \"recovery\": false, \"reward_final\": 0.061, \"reward_min\": 0.048, \"reward_peak\": 0.102, \"reward_std_final\": 0.2, \"total_steps\": 100}, \"notes\": \"Cross-model C1/C2 PARTIAL. Expected Llama-like reward collapse + frac_zero_std→0.95; instead got ENTROPY collapse (0.07 vs Standard's 0.18) + length pathology (clipped_ratio 0.97-1.0, mean_len ~1010). Reward actually functional (0.05-0.10), frac_zero_std moderate (0.55-0.70) — LOWER than Standard. Model can still solve problems but generates pathologically repetitive non-terminating outputs. Collapse IS permanent but mechanism completely different from Llama RASP. Interpretation: Qwen-Math-7B has enough capacity to maintain problem-solving under RASP damage; damage manifests as mode collapse in output space rather than inability. Paper should frame as \\\"pruning-method-dependent GRPO fragility\\\" not \\\"universal collapse signature\\\".\", \"reproduce\": {\"finished_at\": \"2026-05-16T15:43:34.213Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_rasp_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_qwen_math --gpu 0 --max_completion_length 1024 --beta 0.04 --temperature 0.4 --repetition_penalty 1.15 --format_reward_weight 0.1 --gradient_checkpointing true --optim adamw_bnb_8bit --loss_type dapo --learning_rate 5e-7 --max_steps 100 --save_steps 100 --save_total_limit 3 --reward_desert_patience 50 --run_name grpo_rasp_qwen_math_v3 --seed 42\\\"\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 1.01, \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_rasp_qwen_math_v3.log\", \"model_name\": \"Qwen2.5-Math-7B (RASP 20% SFT recovered)\", \"pid\": \"16812\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-16T14:49:39.494Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 3634.1}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T15:54:29.413Z\", \"wandb_run_id\": \"yyg9ty4u\"}, \"sft_rasp_rlvr_20\": {\"completed_at\": \"2026-05-16T14:20:32.511Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T09:50:43.369Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-16T14:20:34.191603+00:00\"}]}, \"failure_reason\": \"磁盘空间不足：训练完成但保存 optimizer state 时 torch.save 失败 (RuntimeError: iostream error)。模型 shards 已写入，checkpoint 可能可用。\", \"hypothesis\": \"RASP-RLVR 20% post-prune SFT recovery (lr=2e-5, epochs=2). 验证反向 CKA scoring (保留冗余结构) 是否产生更好的 RLVR 恢复基础。对比 RASP SFT 和 Standard SFT。Parent: prune_rasp_rlvr_20.\", \"notes\": \"v1 failed (EXIT_CODE=2): wrong arg names. v2 fixed args but EXIT_CODE=1: 训练完成 2 epochs (1870 steps, 36min), loss ~0.64, token_acc ~0.83。模型 shards 已保存到 checkpoint-1870（6.16B params, 验证可加载，需用 load_pruned_model）。optimizer state 被截断（4.3G vs 预期 23G）不可恢复训练，但模型推理可用。westb 数据盘 250GB 100% 满，需清理 checkpoint-935 (35GB) 后才能跑新实验。\", \"reproduce\": {\"finished_at\": \"2026-05-16T14:20:31.427Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_rlvr_20\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_rlvr_20\", \"command\": \"python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_rlvr_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_rlvr_20 --gpu 1 --learning_rate 2e-5 --num_train_epochs 2 --batch_size 1 --gradient_accumulation_steps 8 --max_seq_len 2048 --seed 42\", \"data_count\": 7473, \"data_path\": \"gsm8k_sft\", \"gpu\": \"cuda:1\", \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_rasp_rlvr_20.log\", \"model_name\": \"Qwen2.5-7B-Instruct (RASP-RLVR pruned 20%)\", \"pid\": \"620651\", \"seed\": 42, \"server\": \"westb-23072\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T14:50:02.686Z\"}, \"eval_sft_standard_25\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_sft_standard_25.json\", \"completed_at\": \"2026-05-16T13:23:38.482Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T07:05:10.825Z\", \"hypothesis\": \"Standard 25% post-SFT GSM8K eval (N=1319, greedy, seed=42). 对比 eval_sft_rasp_25 (同时在 westd 运行)，25% sparsity 下 RASP vs Standard post-SFT recovery 对比。20% 结果: Standard 64% > RASP 57%。Parent: sft_standard_25.\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_sft_standard_25.log\", \"metrics\": {\"accuracy\": 0.5125, \"avg_len\": 326.26, \"eos_rate\": 0.9545, \"n_correct\": 676, \"n_total\": 1319, \"stderr\": 0.0138}, \"parent\": \"sft_standard_25\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_sft_standard_25.json\", \"data_count\": 1319, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"openai/gsm8k test split\", \"model_name\": \"sft_standard_25 (Standard 25% pruned + SFT)\", \"seed\": 42, \"server\": \"westb-23072\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T13:23:38.482Z\"}, \"eval_sft_qwen_math_standard_25\": {\"completed_at\": \"2026-05-16T12:50:43.619Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T12:04:49.969Z\", \"hypothesis\": \"Qwen2.5-Math-7B Standard 25% post-SFT GSM8K eval (N=200, greedy, seed=42). Control for eval_sft_qwen_math_rasp_25。对比 20% 结果 (Standard 71.0%)。Parent: sft_qwen_math_standard_25.\", \"metrics\": {\"accuracy\": 63, \"correct\": 126, \"eos_rate\": 1, \"total\": 200}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_standard_25\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_standard_25/\", \"command\": \"CUDA_VISIBLE_DEVICES=3 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_standard_25 --max_samples 200 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_sft_qwen_math_standard_25.json\", \"data_count\": 200, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k_test\", \"gpu\": [\"cuda:3\"], \"gpu_hours\": 0.76, \"gpu_id\": \"cuda:3\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_sft_qwen_math_standard_25.log\", \"model_name\": \"Qwen2.5-Math-7B-Standard-25%-SFT\", \"pid\": \"6215\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-16T12:05:12.481Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2731.1}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T12:50:43.619Z\"}, \"eval_sft_qwen_math_rasp_25\": {\"completed_at\": \"2026-05-16T12:50:42.647Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T12:04:49.248Z\", \"hypothesis\": \"Qwen2.5-Math-7B RASP 25% post-SFT GSM8K eval (N=200, greedy, seed=42). 验证 25% sparsity 下 RASP SFT 恢复质量。对比 Standard 25% 和 20% 结果 (RASP 72.5% vs Standard 71.0%)。Parent: sft_qwen_math_rasp_25.\", \"metrics\": {\"accuracy\": 64, \"correct\": 128, \"eos_rate\": 0.995, \"total\": 200}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_rasp_25\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_rasp_25/\", \"command\": \"CUDA_VISIBLE_DEVICES=2 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_rasp_25 --max_samples 200 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_sft_qwen_math_rasp_25.json\", \"data_count\": 200, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k_test\", \"gpu\": [\"cuda:2\"], \"gpu_hours\": 0.76, \"gpu_id\": \"cuda:2\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_sft_qwen_math_rasp_25.log\", \"model_name\": \"Qwen2.5-Math-7B-RASP-25%-SFT\", \"pid\": \"6135\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-16T12:05:10.285Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2732.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T12:50:42.647Z\"}, \"sft_qwen_math_standard_25\": {\"completed_at\": \"2026-05-16T12:04:20.943Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T11:15:20.187Z\", \"hypothesis\": \"Qwen2.5-Math-7B Standard 25% SFT recovery (lr=2e-5, epochs=2). Control for sft_qwen_math_rasp_25. Parent: prune_standard_25_qwen_math.\", \"metrics\": {\"epochs\": 2, \"final_loss\": 0.6122, \"mean_token_accuracy\": 0.8607, \"throughput_samples_per_sec\": 8.973, \"total_steps\": 1870, \"train_runtime_sec\": 1666}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_standard_25/\", \"command\": \"python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_25_qwen_math --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_standard_25 --gpu 3 --lr 2e-5 --epochs 2 --batch_size 1 --grad_accum 8 --max_seq_len 2048 --seed 42\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_qwen_math_standard_25.log\", \"model_name\": \"Qwen2.5-Math-7B-Standard-25%\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T12:04:20.943Z\"}, \"sft_qwen_math_rasp_25\": {\"completed_at\": \"2026-05-16T12:03:33.361Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T11:15:13.431Z\", \"hypothesis\": \"Qwen2.5-Math-7B RASP 25% SFT recovery (lr=2e-5, epochs=2). 验证更高稀疏度下 RASP 的跨模型 SFT 恢复。Parent: prune_rasp_25_qwen_math.\", \"metrics\": {\"epochs\": 2, \"final_loss\": 0.6062, \"mean_token_accuracy\": 0.8673, \"throughput_samples_per_sec\": 9.046, \"total_steps\": 1870, \"train_runtime_sec\": 1652}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_rasp_25/\", \"command\": \"python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_25_qwen_math --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_rasp_25 --gpu 2 --lr 2e-5 --epochs 2 --batch_size 1 --grad_accum 8 --max_seq_len 2048 --seed 42\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_qwen_math_rasp_25.log\", \"model_name\": \"Qwen2.5-Math-7B-RASP-25%\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T12:03:33.361Z\"}, \"eval_sft_standard_qwen_math_n200\": {\"completed_at\": \"2026-05-16T11:32:27.012Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T11:15:10.910Z\", \"hypothesis\": \"Qwen2.5-Math-7B Standard 20% post-SFT GSM8K eval (N=200, greedy, seed=42). EOS fixed. Control for eval_sft_rasp_qwen_math_n200. Parent: sft_standard_20_qwen_math.\", \"metrics\": {\"accuracy\": 0.71, \"avg_len\": 127.7, \"correct\": 142, \"eos_rate\": 1, \"n_total\": 200, \"stderr\": 0.0321}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_sft_standard_qwen_math.json\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_standard_20\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_standard_20 --max_samples 200 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_sft_standard_qwen_math.json\", \"data_count\": 200, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k_test\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/eval_standard_n200.log\", \"model_name\": \"Qwen2.5-Math-7B-Standard-20%-SFT\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T11:32:27.012Z\"}, \"eval_sft_rasp_qwen_math_n200\": {\"completed_at\": \"2026-05-16T11:32:23.931Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T11:15:07.028Z\", \"hypothesis\": \"Qwen2.5-Math-7B RASP 20% post-SFT GSM8K eval (N=200, greedy, seed=42). EOS fixed (eos_token_id=[151643,151645]). Cross-model validation. Parent: sft_rasp_20_qwen_math.\", \"metrics\": {\"accuracy\": 0.725, \"avg_len\": 121.8, \"correct\": 145, \"eos_rate\": 1, \"n_total\": 200, \"stderr\": 0.0316}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_sft_rasp_qwen_math.json\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_rasp_20\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_rasp_20 --max_samples 200 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_sft_rasp_qwen_math.json\", \"data_count\": 200, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k_test\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/eval_rasp_n200.log\", \"model_name\": \"Qwen2.5-Math-7B-RASP-20%-SFT\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T11:32:23.931Z\"}, \"prune_rasp_rlvr_20\": {\"completed_at\": \"2026-05-16T10:31:42.144Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T09:50:39.656Z\", \"hypothesis\": \"RASP-RLVR 20% pruning: score = importance * cka^alpha. 反转 CKA scoring——剪掉功能独特的结构（低 CKA overlap），保留冗余结构（高 overlap），使 RLVR 更容易通过冗余路径恢复能力。对比 RASP (1-cka)^alpha 和 Standard (importance only)。\", \"metrics\": {\"actual_sparsity\": 0.1909, \"attn_gqa_groups_pruned\": \"0/112\", \"group_selection_diff_vs_rasp\": \"RASP重剪前6层+后段(19,23-25,27)保中间; RLVR重剪前6层+中后段(16-26)保Layer6-7,27\", \"mlp_groups_pruned\": \"200/784\", \"params_after\": \"6.16B\", \"target_sparsity\": 0.2}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_rlvr_20/\", \"command\": \"CUDA_VISIBLE_DEVICES='' python src/prune.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --mode rasp-rlvr --sparsity 0.20 --alpha 1.0 --dtype bfloat16 --importance_path results/importance_scores.pt --cka_path results/cka_scores.pt --output_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_rlvr_20\", \"data_count\": 0, \"data_path\": \"results/importance_scores.pt + results/cka_scores.pt\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/logs/workers/worker_code_rasp_rlvr_prune_20260516T095028.log\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"server\": \"westb-23072\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T10:31:42.144Z\"}, \"sft_standard_20_qwen_math\": {\"completed_at\": \"2026-05-16T10:10:19.019Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T08:11:00.051Z\", \"hypothesis\": \"Qwen2.5-Math-7B Standard 20% pruned SFT recovery. 验证 RASP 方法在第二个模型族上的 SFT 恢复效果。\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_standard_20/\", \"command\": \"python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_qwen_math_standard_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_standard_20 --gpu 1 --num_train_epochs 3 --learning_rate 2e-5 --batch_size 1 --gradient_accumulation_steps 8 --max_seq_length 2048 --seed 42\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"log_path\": \"tmux session on westd-11672\", \"model_name\": \"Qwen2.5-Math-7B-Standard-20%\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T10:10:19.019Z\"}, \"sft_rasp_20_qwen_math\": {\"completed_at\": \"2026-05-16T10:10:17.853Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T08:10:59.311Z\", \"hypothesis\": \"Qwen2.5-Math-7B RASP 20% pruned SFT recovery. 验证 RASP 方法在第二个模型族上的 SFT 恢复效果。\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_rasp_20/\", \"command\": \"python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_qwen_math_rasp_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_rasp_20 --gpu 0 --num_train_epochs 3 --learning_rate 2e-5 --batch_size 1 --gradient_accumulation_steps 8 --max_seq_length 2048 --seed 42\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"log_path\": \"tmux session on westd-11672\", \"model_name\": \"Qwen2.5-Math-7B-RASP-20%\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T10:10:17.852Z\"}, \"prune_standard_20_qwen_math\": {\"completed_at\": \"2026-05-16T08:04:14.036Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T08:03:56.378Z\", \"hypothesis\": \"Qwen2.5-Math-7B Standard 20% structured pruning (negative control). Scope expansion Phase 2 对照组。\", \"metrics\": {\"attn_groups_pruned\": 0, \"mlp_groups_pruned\": 202, \"model_keys\": 339, \"original_params\": 7615616512, \"pruned_params\": 6147409408, \"sparsity_actual\": 0.1928, \"sparsity_target\": 0.2}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_qwen_math_standard_20\", \"command\": \"python src/prune.py --model_path /root/autodl-tmp/models/Qwen2.5-Math-7B --mode standard --sparsity 0.20 --dtype bfloat16 --output_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_qwen_math_standard_20\", \"data_count\": 256, \"data_path\": \"importance_scores_qwen_math.pt\", \"log_path\": \"N/A (CPU-only)\", \"model_name\": \"Qwen2.5-Math-7B\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T08:04:22.864Z\"}, \"prune_rasp_20_qwen_math\": {\"completed_at\": \"2026-05-16T08:04:13.355Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T08:01:57.095Z\", \"hypothesis\": \"Qwen2.5-Math-7B RASP 20% structured pruning. Scope expansion Phase 2: 验证 RASP 在第二个模型上的有效性（CKA-guided pruning preserves reasoning across model families）。使用已计算的 importance_scores_qwen_math.pt + cka_scores_qwen_math.pt。\", \"metrics\": {\"alpha\": 1, \"attn_groups_pruned\": 0, \"mlp_groups_pruned\": 199, \"model_keys\": 339, \"original_params\": 7615616512, \"pruned_params\": 6169214464, \"sparsity_actual\": 0.1899, \"sparsity_target\": 0.2}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_qwen_math_rasp_20\", \"command\": \"python src/prune.py --model_path /root/autodl-tmp/models/Qwen2.5-Math-7B --mode rasp --sparsity 0.20 --alpha 1.0 --dtype bfloat16 --output_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_qwen_math_rasp_20\", \"data_count\": 256, \"data_path\": \"importance_scores_qwen_math.pt + cka_scores_qwen_math.pt\", \"log_path\": \"N/A (CPU-only)\", \"model_name\": \"Qwen2.5-Math-7B\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T08:04:20.185Z\"}, \"eval_grpo_rasp_v9_step10\": {\"completed_at\": \"2026-05-16T08:01:06.191Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T03:40:46.186Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-16T07:58:10.228000+00:00\"}]}, \"hypothesis\": \"RASP GRPO v9 step-10 checkpoint GSM8K eval (N=1319, greedy, seed=42). Step 10 = collapse onset (reward=0.015, frac_zero_std=0.875). 对比 step-5 eval 和 Standard step-50 eval (58.91%) 量化 collapse 影响。Parent: grpo_stage2_rasp_20_v9.\", \"metrics\": {\"accuracy\": 61.87, \"avg_response_length\": 213.6, \"correct\": 816, \"eos_rate\": 98.33, \"seed\": 42, \"stderr\": 1.34, \"total\": 1319, \"truncated\": 22}, \"parent\": \"grpo_stage2_rasp_20_v9\", \"reproduce\": {\"finished_at\": \"2026-05-16T07:58:08.513Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_rasp_v9_step10.json\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9/checkpoint-10\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_HUB_OFFLINE=1 CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9/checkpoint-10 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_rasp_v9_step10.json\\\"\", \"data_count\": 1319, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"openai/gsm8k test split\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 3.06, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_grpo_rasp_v9_step10.log\", \"model_name\": \"grpo_stage2_rasp_20_v9 checkpoint-10\", \"pid\": \"585618\", \"seed\": 42, \"server\": \"westb-23072\", \"submitted_at\": \"2026-05-16T04:57:36.867Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 11009.3}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T08:01:06.191Z\"}, \"eval_grpo_rasp_v9_step5\": {\"completed_at\": \"2026-05-16T05:17:47.734Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T01:55:35.424Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-16T04:41:38.932275+00:00\"}]}, \"hypothesis\": \"RASP GRPO v9 step-5 checkpoint GSM8K eval (N=1319, greedy, seed=42). Step 5 是 RASP collapse 前最后可能的 pre-collapse checkpoint（v9 collapse onset ≤step 10, logging_steps=10 无法判断 step 5 状态）。与 Standard step-50 eval (58.91%) 对比，量化 RASP GRPO 短暂训练的效果。Parent: grpo_stage2_rasp_20_v9.\", \"metrics\": {\"accuracy\": 60.65, \"seed\": 42, \"total\": 1319}, \"parent\": \"grpo_stage2_rasp_20_v9\", \"reproduce\": {\"finished_at\": \"2026-05-16T04:41:37.201Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9/checkpoint-5\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_grpo_rasp_v9_step5.log\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T05:18:16.131Z\"}, \"prune_standard_25\": {\"completed_at\": \"2026-05-16T05:16:34.661Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T05:13:52.855Z\", \"hypothesis\": \"Standard importance-only pruning at 25% sparsity (calibration=256). Negative control for RASP 25%. Multi-sparsity extension.\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_25\", \"command\": \"python prune.py --model_path DeepSeek-R1-Distill-Qwen-7B --mode standard --sparsity 0.25 --dtype bfloat16\", \"data_count\": 256, \"data_path\": \"calibration data (from importance scores)\", \"log_path\": \"N/A (CPU-only, <1min)\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"server\": \"westb-23072\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T05:16:41.032Z\"}, \"prune_rasp_25\": {\"completed_at\": \"2026-05-16T05:16:35.749Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T05:13:52.292Z\", \"hypothesis\": \"RASP pruning at 25% sparsity (α=1.0, calibration=256). Multi-sparsity extension: compare with 20% to establish sparsity-collapse relationship.\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_25\", \"command\": \"python prune.py --model_path DeepSeek-R1-Distill-Qwen-7B --mode rasp --sparsity 0.25 --alpha 1.0 --dtype bfloat16\", \"data_count\": 256, \"data_path\": \"calibration data (from importance/CKA scores)\", \"log_path\": \"N/A (CPU-only, <1min)\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"server\": \"westb-23072\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T05:16:39.998Z\"}, \"grpo_unpruned_v2\": {\"account\": \"root\", \"completed_at\": \"2026-05-16T01:58:25.504Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T01:45:10.586Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-16T01:58:26.876600+00:00\"}, {\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-16T03:01:13.625476+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"metrics\": {\"checkpoints_saved\": [\"checkpoint-5\", \"checkpoint-10\", \"checkpoint-15\", \"checkpoint-20\"], \"comparison\": {\"rasp_v9_step10_reward\": 0.015, \"ratio_vs_rasp\": \"36.8x\", \"ratio_vs_standard_peak\": \"5.75x\", \"standard_v8_step40_peak_reward\": 0.096, \"unpruned_v2_step20_reward\": 0.552}, \"disk_warning\": \"93% full, 20GB remaining, each checkpoint ~33GB — will crash at step 25 save\", \"kl\": 0.0046, \"loss\": 0.024, \"max_steps\": 100, \"reward_mean\": 0.552, \"status\": \"HEALTHY\", \"step\": 20, \"step_time_sec\": 21}, \"notes\": \"PID 75381 on westd cuda:1 (first attempt PID 74579 failed due to missing wandb credentials, restarted). VRAM 44836 MiB. tmux session: grpo_unpruned_v2. output_dir: /root/autodl-tmp/recovery_aware_struct_prune/grpo_unpruned_v2. Disk cleaned to 141GB free before launch. Config: beta=0.01, loss=dapo, lr=1e-6, temp=0.4, rep_pen=1.15, format_reward=0.1, max_steps=100, save_steps=5, save_total_limit=10.\"}}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"gpu\": \"cuda:1\", \"hypothesis\": \"D043+ Unpruned GRPO v2 (D041 fix) — 修复 v1 设计缺陷（无 SFT 步骤）。使用 sft_unpruned_baseline checkpoint (84% N=100, loss=0.332) → GRPO，与 v8 完全相同参数 (8-bit AdamW, max_completion_length=1024, beta=0.01, temp=0.4, rep_penalty=1.15, format_reward=0.1, lr=1e-6, max_steps=100, save_steps=5)。三模型 collapse dynamics 最后一块拼图：RASP ~step10, Standard ~step60, Unpruned ?。如果 Unpruned collapse 显著晚于 pruned models → 确立 pruning-specificity (Claim 1/2)。如果 Unpruned 也快速 collapse → GRPO 方法本身问题，需重新 frame。Parent: sft_unpruned_baseline.\", \"metrics\": {\"avg_step_time_sec\": 23, \"checkpoints_available\": [\"checkpoint-90\", \"checkpoint-95\", \"checkpoint-100\"], \"collapse_onset\": \"N/A\", \"final_entropy\": 0.194, \"final_grad_norm\": 6.97, \"final_kl\": 0.0051, \"final_reward\": 0.661, \"max_steps\": 100, \"peak_reward\": 0.669, \"peak_reward_step\": 80, \"reward_range\": \"0.425-0.669\", \"training_seconds\": 2660}, \"notes\": \"Unpruned GRPO 100 步全程未 collapse。Reward 稳定 0.4-0.67，peak 0.669 (step 80)，final 0.661 (step 100)。Grad norm 健康 (2.45-14.94)，entropy 平稳 (0.184-0.214)，KL 极稳定 (0.0046-0.0053)。Step 30 有浅 dip (0.425) 但 step 40 即回升。三模型 severity gradient 确立：RASP collapse step~10 (永久) > Standard step~60 (transient) > Unpruned 无 collapse。save_total_limit 导致仅剩 checkpoint-90/95/100。W&B runs: nhsx0bt2 (首次), hwucjf2n (恢复)。\", \"parent\": \"sft_unpruned_baseline\", \"reproduce\": {\"finished_at\": \"2026-05-16T03:01:11.703Z\", \"gpu\": \"cuda:1\", \"server\": \"westd-11672\", \"started_at\": \"2026-05-16T01:47:46.093Z\", \"training_hours\": 1.22}, \"retry_count\": 1, \"server\": \"westd-11672\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_unpruned_v2/checkpoint-100\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_unpruned_baseline\", \"command\": \"resume from checkpoint-20, save_total_limit=3, max_steps=100\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k_train_7473\", \"gpu_id\": \"cuda:1\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_unpruned_v2.log\", \"model_name\": \"sft_unpruned_baseline (unpruned)\", \"pid\": 77647, \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T04:43:16.844Z\", \"wandb_run_id\": \"hwucjf2n\"}, \"grpo_stage2_rasp_20_v9\": {\"completed_at\": \"2026-05-16T03:38:31.943Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-15T22:37:13.593Z\", \"hypothesis\": \"D043 plan_003 (Claim 1 核心对比): RASP GRPO v9 — save_steps=5 捕获 collapse 前 peak checkpoint。v8 全版本零 checkpoint (save_steps=50, kill at step ~28)。v9 用 save_steps=5, save_total_limit=5, max_steps=30。其余参数与 v8 一致 (8-bit AdamW, max_completion_length=1024, beta=0.01, temp=0.4, rep_penalty=1.15, format_reward=0.1, lr=1e-6)。RASP collapse onset ~step 10, 需要 step 5/10 checkpoint 做 eval 与 Standard step-50 对比。Parent: sft_rasp_20.\", \"metrics\": {\"checkpoints\": [\"checkpoint-10\", \"checkpoint-15\", \"checkpoint-20\", \"checkpoint-25\", \"checkpoint-30\"], \"collapse_note\": \"frac_zero_std peaked at 95% by step 30, reward dropped from peak 0.039 (step 20) to 0.021 (step 30)\", \"collapse_status\": \"COLLAPSED\", \"final_clipped_ratio\": 0.956, \"final_frac_zero_std\": 0.95, \"final_grad_norm\": 1.398, \"final_kl\": 0.00118, \"final_loss\": 0.00686, \"final_mean_length\": 996, \"final_mean_terminated_length\": 176, \"final_reward\": 0.021, \"max_steps\": 30, \"reward_history\": [{\"frac_zero_std\": 0.875, \"reward\": 0.015, \"step\": 10}, {\"frac_zero_std\": 0.8, \"reward\": 0.039, \"step\": 20}, {\"frac_zero_std\": 0.95, \"reward\": 0.021, \"step\": 30}], \"step\": 30, \"step_time_sec\": 418, \"total_time\": \"3h28m25s\", \"wandb_url\": \"https://wandb.ai/xiaoyucorynne-/recovery_aware_struct_prune/runs/mrikafz3\"}, \"parent\": \"sft_rasp_20\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20\", \"command\": \"CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python /root/recovery_aware_struct_prune/src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9 --gpu 0 --max_completion_length 1024 --beta 0.01 --temperature 0.4 --repetition_penalty 1.15 --format_reward_weight 0.1 --gradient_checkpointing true --optim adamw_bnb_8bit --loss_type dapo --learning_rate 1e-6 --max_steps 30 --save_steps 5 --save_total_limit 5 --reward_desert_patience 50 --run_name grpo_stage2_rasp_20_v9\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k\", \"gpu_id\": \"cuda:0\", \"log_path\": \"/tmp/grpo_rasp_v9.log\", \"model_name\": \"sft_rasp_20\", \"notes\": \"Auto-launcher tmux session auto_v9_launcher waiting for alpha sweep to finish before starting on cuda:0\", \"pid\": 566666, \"seed\": 42, \"server\": \"westb-23072\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T03:38:37.387Z\", \"wandb_run_id\": \"mrikafz3\"}, \"alpha_ablation_sweep\": {\"checkpoint_path\": \"/root/recovery_aware_struct_prune/results/\", \"completed_at\": \"2026-05-16T00:14:46.464Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-15T20:15:39.765Z\", \"hypothesis\": \"plan_015 (Claim 2): α sensitivity ablation on westb (cal=512). Sweep α∈{0, 0.25, 0.5, 1, 2} at 20% sparsity. RASP scoring S(h)=I(h)×(1-F(h))^α. Each α: prune + post-prune GSM8K N=100 eval. Tests whether CKA weight α systematically affects post-prune reasoning retention. Prior westd (cal=256) results: α=0.0→30%, α=0.5→25%, α=1.0→27%, α=4.0→40% (non-monotonic). westb cal=512 may show different pattern due to group selection sensitivity at 20% sparsity.\", \"log_path\": \"/tmp/alpha_sweep_fix.log\", \"metrics\": {\"alpha_0.0\": {\"accuracy\": 0.27, \"avg_len\": 1192, \"eos_rate\": 0.8, \"n_correct\": 27, \"n_total\": 100}, \"alpha_0.25\": {\"accuracy\": 0.23, \"avg_len\": 1834, \"eos_rate\": 0.63, \"n_correct\": 23, \"n_total\": 100}, \"alpha_0.5\": {\"accuracy\": 0.22, \"avg_len\": 1141, \"eos_rate\": 0.81, \"n_correct\": 22, \"n_total\": 100}, \"alpha_1.0\": {\"accuracy\": 0.31, \"avg_len\": 733, \"eos_rate\": 0.92, \"n_correct\": 31, \"n_total\": 100}, \"alpha_2.0\": {\"accuracy\": 0.36, \"avg_len\": 2130, \"eos_rate\": 0.59, \"n_correct\": 36, \"n_total\": 100}}, \"retry_count\": 0, \"spec\": {\"alphas\": [0, 0.25, 0.5, 1, 2], \"calibration_samples\": 512, \"checkpoint_path\": \"/root/recovery_aware_struct_prune/results/\", \"command\": \"bash run_alpha_sweep_fix.sh\", \"data_count\": 100, \"data_path\": \"openai/gsm8k\", \"gpu_id\": \"cuda:0\", \"log_path\": \"/tmp/alpha_sweep_fix.log\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"notes\": \"Alpha ablation: 0.25, 0.5, 1.0, 2.0. Partial results: alpha=0.0 acc=0.27 eos=0.80, alpha=0.25 acc=0.23 eos=0.63. Currently running alpha=0.5 eval.\", \"pid\": 556867, \"seed\": 42, \"server\": \"westb-23072\", \"sparsity\": 0.2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T00:18:46.780Z\"}, \"sft_unpruned_baseline\": {\"completed_at\": \"2026-05-16T00:18:44.096Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-15T22:07:43.929Z\", \"hypothesis\": \"D043 plan_002 (Claim 1): Unpruned DeepSeek-R1-Distill-Qwen-7B SFT baseline。与 RASP/Standard SFT 完全相同配置 (2 epochs, lr=2e-5, batch=1, grad_accum=8, GSM8K train, seed=42)。三方公平对比必要条件：unpruned SFT → 然后才能做 unpruned GRPO baseline (修复 D041 设计缺陷)。\", \"metrics\": {\"epochs\": 2, \"final_loss\": 0.3321, \"final_token_accuracy\": 0.909, \"total_steps\": 1870, \"train_loss_avg\": 0.4253, \"train_runtime_sec\": 1908, \"train_samples_per_second\": 7.833}, \"notes\": \"tmux session: sft_unpruned, westd cuda:1. 1870 steps (2 epochs), ETA ~35-40min from 06:30 UTC. Cleaned sft_ablation/alpha_4.0/checkpoint-1870 (35G) to free disk.\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_unpruned_baseline\", \"checkpoint_source\": \"/root/autodl-tmp/models/DeepSeek-R1-Distill-Qwen-7B\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && HF_HUB_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets /root/miniconda3/bin/python /root/recovery_aware_struct_prune/src/sft_recovery.py --model_path /root/autodl-tmp/models/DeepSeek-R1-Distill-Qwen-7B --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_unpruned_baseline --gpu 1 --num_train_epochs 2 --learning_rate 2e-5 --batch_size 1 --gradient_accumulation_steps 8 --max_seq_length 2048 --seed 42 --save_strategy no --run_name sft_unpruned_baseline_v2\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k train\", \"estimated_time_minutes\": 33, \"gpu_id\": \"cuda:1\", \"hyperparams\": {\"batch_size\": 1, \"epochs\": 2, \"gradient_accumulation_steps\": 8, \"lr\": 2e-05, \"max_seq_length\": 2048, \"save_strategy\": \"no\", \"seed\": 42}, \"log_path\": \"/tmp/sft_unpruned.log\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (unpruned)\", \"pid\": 67546, \"seed\": 42, \"server\": \"westd-11672\", \"tmux_session\": \"sft_unpruned\", \"total_steps\": 1870}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T00:18:44.096Z\"}, \"eval_sft_rasp_full_westd\": {\"completed_at\": \"2026-05-15T21:42:35.245Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-15T20:36:02.786Z\", \"hypothesis\": \"plan_001 (Claim 1): RASP SFT full GSM8K eval (N=1319, greedy, seed=42) on westd. N=100 results: westb 57%, westd 67% (10pp gap, needs full eval to confirm). Full eval resolves whether RASP advantage is real or N=100 noise. Parent: sft_rasp_20_westd_retrain.\", \"metrics\": {\"accuracy\": 0.6149, \"avg_len\": 216.5, \"eos_rate\": 0.9826, \"n_correct\": 811, \"n_total\": 1319, \"stderr\": 0.0134}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"results/eval_sft_rasp_20_westd_full.json\", \"checkpoint_source\": \"sft_rasp_20_westd\", \"command\": \"python eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd --output results/eval_sft_rasp_20_westd_full.json --n_samples 1319\", \"data_count\": 1319, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k_test_full\", \"gpu_id\": \"cuda:1\", \"log_path\": \"/tmp/eval_rasp_full.log\", \"model_name\": \"sft_rasp_20_westd\", \"output_path\": \"results/eval_sft_rasp_20_westd_full.json\", \"pid\": 62565, \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T21:42:41.916Z\"}, \"eval_sft_standard_full_westd\": {\"completed_at\": \"2026-05-15T21:42:34.808Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-15T20:36:01.803Z\", \"hypothesis\": \"plan_001 (Claim 1): Standard SFT full GSM8K eval (N=1319, greedy, seed=42) on westd. N=100 results: westb 64%, westd 63% (cross-server consistent). Full eval for statistical significance. Parent: sft_standard_20_westd_retrain.\", \"metrics\": {\"accuracy\": 0.5929, \"avg_len\": 226.7, \"eos_rate\": 0.9803, \"n_correct\": 782, \"n_total\": 1319, \"stderr\": 0.01353}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"results/eval_sft_standard_20_westd_full.json\", \"checkpoint_source\": \"sft_standard_20_westd\", \"command\": \"python eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_westd --output results/eval_sft_standard_20_westd_full.json --n_samples 1319\", \"data_count\": 1319, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k_test_full\", \"gpu_id\": \"cuda:0\", \"log_path\": \"/tmp/eval_standard_full.log\", \"model_name\": \"sft_standard_20_westd\", \"output_path\": \"results/eval_sft_standard_20_westd_full.json\", \"pid\": 62463, \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T21:42:40.854Z\"}, \"eval_sft_rasp_20_westd_n100_v2\": {\"checkpoint_path\": \"/root/recovery_aware_struct_prune/results/eval_sft_rasp_20_westd_n100.json\", \"completed_at\": \"2026-05-15T20:10:55.875Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-15T19:24:08.437Z\", \"hypothesis\": \"N=100 quick validation of RASP SFT retrain on westd (v2 retry — fixed working directory from autodl-tmp to project root). Expected ~57% (matching westb). Cross-server reproducibility check. Parent: sft_rasp_20_westd_retrain.\", \"metrics\": {\"accuracy\": 0.67, \"avg_len\": 182.39, \"eos_rate\": 0.99, \"n_correct\": 67, \"n_total\": 100}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd\", \"command\": \"bash -c \\\"cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 python -u src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd --max_samples 100 --max_new_tokens 4096 --output_path results/eval_sft_rasp_20_westd_n100.json --seed 42\\\"\", \"data_count\": 100, \"data_path\": \"gsm8k test\", \"eval_data\": \"gsm8k test N=100\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 0.78, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_sft_rasp_20_westd_n100_v2.log\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (RASP pruned 20% + SFT westd)\", \"pid\": \"unknown\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-15T19:24:08.325Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2807.6}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T20:11:02.033Z\"}, \"eval_sft_standard_20_westd_n100_v2\": {\"checkpoint_path\": \"/root/recovery_aware_struct_prune/results/eval_sft_standard_20_westd_n100.json\", \"completed_at\": \"2026-05-15T20:10:55.158Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-15T19:24:09.850Z\", \"hypothesis\": \"N=100 quick validation of Standard SFT retrain on westd (v2 retry — fixed working directory + output_path typo). Expected ~64% (matching westb). Cross-server reproducibility check. Parent: sft_standard_20_westd_retrain.\", \"metrics\": {\"accuracy\": 0.63, \"avg_len\": 260.57, \"eos_rate\": 0.97, \"n_correct\": 63, \"n_total\": 100}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_westd\", \"command\": \"bash -c \\\"cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 python -u src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_westd --max_samples 100 --max_new_tokens 4096 --output_path results/eval_sft_standard_20_westd_n100.json --seed 42\\\"\", \"data_count\": 100, \"data_path\": \"gsm8k test\", \"eval_data\": \"gsm8k test N=100\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.78, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_sft_standard_20_westd_n100_v2.log\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (Standard pruned 20% + SFT westd)\", \"pid\": \"unknown\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-15T19:24:09.745Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2805.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T20:11:00.967Z\"}, \"eval_sft_standard_20_westd_n100\": {\"checkpoint_path\": \"/root/recovery_aware_struct_prune/results/eval_sft_standard_20_westd_n100.json\", \"completed_at\": \"2026-05-15T19:04:25.288Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-15T17:39:03.607Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-15T19:04:27.416819+00:00\"}, {\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-15T19:23:03.873165+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"Retry #3: fixed python path (python -> /root/miniconda3/bin/python) and ensured cd /root/recovery_aware_struct_prune in command. eval_gsm8k.py confirmed 14595 bytes with apply_chat_template. PID=59675 on cuda:1.\"}}, \"failure_reason\": \"src/eval_gsm8k.py not found at /root/autodl-tmp/recovery_aware_struct_prune/ — code not synced to data disk before launch. Also --output_path typo (used rasp filename instead of standard)\", \"hypothesis\": \"N=100 quick validation of Standard SFT retrain on westd. Expected ~64% (matching westb). Cross-server reproducibility check before N=1319 full eval. Parent: sft_standard_20_westd_retrain.\", \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_sft_standard_20_westd_n100.json\", \"metrics\": {\"accuracy\": 0.63, \"avg_len\": 260.57, \"eos_rate\": 0.97, \"n_correct\": 63, \"n_total\": 100, \"stderr\": 0.048}, \"notes\": \"Standard 63% on westd — matches westb expectation (~64%). Cross-server reproducibility confirmed for Standard. RASP outperforms Standard by 4pp on westd (67% vs 63%), reversed from westb pattern.\", \"reproduce\": {\"finished_at\": \"2026-05-15T19:23:00.256Z\"}, \"retry_count\": 2, \"spec\": {\"checkpoint_source\": \"sft_standard_20_westd_retrain\", \"command\": \"bash -c \\\"cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_westd --max_samples 100 --max_new_tokens 4096 --seed 42 --output_path results/eval_sft_standard_20_westd_n100.json\\\"\", \"data_count\": 100, \"data_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_westd\", \"eval_data\": \"gsm8k\", \"model_name\": \"sft_standard_20_westd\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:30:00.797Z\"}, \"eval_sft_rasp_20_westd_n100\": {\"checkpoint_path\": \"/root/recovery_aware_struct_prune/results/eval_sft_rasp_20_westd_n100.json\", \"completed_at\": \"2026-05-15T19:04:17.476Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-15T17:35:08.417Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-15T19:04:19.129814+00:00\"}, {\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-15T19:22:57.955307+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"Retry #3: fixed python path (python -> /root/miniconda3/bin/python) and ensured cd /root/recovery_aware_struct_prune in command. eval_gsm8k.py confirmed 14595 bytes with apply_chat_template. PID=59601 on cuda:0.\"}}, \"failure_reason\": \"src/eval_gsm8k.py not found at /root/autodl-tmp/recovery_aware_struct_prune/ — code not synced to data disk before launch\", \"hypothesis\": \"N=100 quick validation of RASP SFT retrain on westd. Expected ~57% (matching westb). Cross-server reproducibility check before N=1319 full eval. Parent: sft_rasp_20_westd_retrain.\", \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_sft_rasp_20_westd_n100.json\", \"metrics\": {\"accuracy\": 0.67, \"avg_len\": 182.39, \"eos_rate\": 0.99, \"n_correct\": 67, \"n_total\": 100, \"stderr\": 0.047}, \"notes\": \"RASP 67% vs expected ~57% — 10pp higher than westb. Standard 63% matches westb expectation. RASP > Standard by 4pp on westd (reversed from westb where Standard led). Cross-server reproducibility NOT confirmed for RASP — needs investigation with full N=1319 eval.\", \"reproduce\": {\"finished_at\": \"2026-05-15T19:22:56.266Z\"}, \"retry_count\": 2, \"spec\": {\"checkpoint_source\": \"sft_rasp_20_westd_retrain\", \"command\": \"bash -c \\\"cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python -u src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd --max_samples 100 --max_new_tokens 4096 --seed 42 --output_path results/eval_sft_rasp_20_westd_n100.json\\\"\", \"data_count\": 100, \"data_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd\", \"eval_data\": \"gsm8k\", \"model_name\": \"sft_rasp_20_westd\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:29:59.250Z\"}, \"sft_rasp_20_westd_retrain\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd\", \"completed_at\": \"2026-05-15T18:36:33.103Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-15T16:59:51.103Z\", \"hypothesis\": \"RASP SFT retrain on westd for cross-server reproducibility + full N=1319 eval. Same params as westb (2 epochs, lr=2e-5, batch=1, grad_accum=8, seed=42). Expected: ~57% post-SFT (matching westb). Parent: reeval_postprune_definitive.\", \"log_path\": \"tmux session sft_rasp_westd (no separate log file)\", \"notes\": \"RASP SFT retrain 启动 on westd cuda:0. PID 48946, tmux session sft_rasp_westd. 参数: epochs=2, lr=2e-5, bs=1, grad_accum=8, max_seq_len=2048, seed=42. Output: /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd. 预计 ~35-40min。完成后先 N=100 快速验证 (~57% expected)，再 N=1319 full eval。\", \"retry_count\": 0, \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd --gpu 0 --epochs 2 --lr 2e-5 --batch_size 1 --grad_accum 8 --seed 42\", \"data_count\": 7473, \"data_path\": \"gsm8k train\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (RASP pruned 20%)\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T18:36:33.103Z\"}, \"sft_standard_20_westd_retrain\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_westd\", \"completed_at\": \"2026-05-15T18:36:32.558Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-15T17:05:52.927Z\", \"hypothesis\": \"Standard SFT retrain on westd for cross-server reproducibility + full N=1319 eval. Same params as westb (2 epochs, lr=2e-5, batch=1, grad_accum=8, seed=42). Expected: ~64% post-SFT (matching westb). Parent: reeval_postprune_definitive.\", \"log_path\": \"/tmp/sft_std20_westd.log\", \"metrics\": {\"epochs\": 2, \"final_step_loss\": 0.6403, \"final_token_accuracy\": 0.8258, \"total_steps\": 1870, \"train_loss\": 0.7577, \"train_runtime_sec\": 1679, \"train_samples_per_second\": 8.902}, \"notes\": \"Standard SFT retrain 启动 on westd cuda:1. PID 49645. 参数: epochs=2, lr=2e-5, bs=1, grad_accum=8, max_seq_len=2048, seed=42. Output: /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_westd. 模型加载中。预计 ~35-40min。完成后先 N=100 快速验证 (~64% expected)，再 N=1319 full eval。\", \"retry_count\": 0, \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_westd --gpu 1 --epochs 2 --lr 2e-5 --batch_size 1 --grad_accum 8 --seed 42\", \"data_count\": 7473, \"data_path\": \"gsm8k train\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (Standard pruned 20%)\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T18:36:32.558Z\"}, \"grasp_baseline_westd\": {\"checkpoint_path\": \"results/eval_pruned_graspune_20_greedy.json\", \"completed_at\": \"2026-05-15T17:12:21.555Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-15T12:40:34.072Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-15T15:06:17.807624+00:00\"}, {\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-15T15:10:56.704857+00:00\"}]}, \"hypothesis\": \"D027: GraSP baseline on westd — compare GraSP pruning criterion against RASP at 20% sparsity. If RASP > GraSP post-recovery, confirms CKA-aware scoring advantage over gradient-based saliency. Critical for plan_005 and Dream reviewer concern.\", \"metrics\": {\"avg_len\": 4018, \"eos_rate\": 0.02, \"grasp_20_accuracy_n100\": 0.07, \"json_path\": \"results/eval_pruned_graspune_20_greedy.json\", \"n_correct\": 7, \"n_total\": 100, \"rasp_20_accuracy_ref\": 0.31, \"standard_20_accuracy_ref\": 0.27}, \"notes\": \"GraSP post-prune eval (N=100) 运行中 on westd GPU 0. PID 38120. 71/100 at 15:25 UTC, ~51s/sample, 预计 ~25min 完成。中间结果 (50 samples): accuracy 6%, eos_rate 2%, avg_len 4018. 输出确认安全: seed 默认 42, output_path 默认 results/eval_pruned_graspune_20_greedy.json. 完成后立即启动 GraSP post-SFT eval (cuda:0, model at sft_graspune_20/). Cron 监控中。\", \"reproduce\": {\"finished_at\": \"2026-05-15T15:10:55.707Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"GraSP pruning pipeline\", \"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_graspune_20 --max_samples 100 --max_new_tokens 4096\", \"command_note\": \"实际运行命令无 --output_path 和 --seed，但源码默认 seed=42 且 output_path 自动回退到 results/eval_pruned_graspune_20_greedy.json\", \"data_count\": 100, \"data_path\": \"gsm8k test split\", \"eval_data\": \"gsm8k test N=100\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 4.44, \"log_path\": \"results/eval_grasp_n100.log\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (GraSP pruned 20%)\", \"pid\": \"38120\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-15T12:45:44.074Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 15997.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T17:12:21.555Z\"}, \"eval_sft_alpha_2p0\": {\"completed_at\": \"2026-05-15T16:41:41.929Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-15T15:42:36.917Z\", \"hypothesis\": \"α=2.0 post-SFT GSM8K eval (N=100, greedy). Post-prune 29%, post-SFT loss=0.61, token_acc=0.84. Completes α ablation sweep: α=0.0 (64%), α=1.0 (57%), α=4.0 (62%), α=2.0 (?). Parent: sft_alpha2_0_westd.\", \"metrics\": {\"accuracy\": 0.62, \"avg_len\": 277.41, \"eos_rate\": 0.97, \"n_correct\": 62, \"n_total\": 100, \"stderr\": 0.0485}, \"parent\": \"sft_alpha2_0_westd\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_2.0\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_2.0\", \"command\": \"python -u src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_2.0 --max_samples 100 --max_new_tokens 4096 --seed 42 --output_path results/eval_sft_alpha_2.0_n100.json\", \"data_count\": 100, \"data_path\": \"gsm8k\", \"eval_data\": \"gsm8k_test_n100\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.98, \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_sft_alpha_2.0_n100.log\", \"model_name\": \"alpha_2.0_sft\", \"pid\": \"45428\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-15T15:42:47.927Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 3534.0}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T16:41:41.929Z\"}, \"sft_alpha2_0_westd\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_2.0\", \"completed_at\": \"2026-05-15T15:41:22.891Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-15T14:32:54.953Z\", \"hypothesis\": \"D027: α=2.0 pruned model SFT recovery on westd. α=2.0 post-prune accuracy 29%. Same SFT params as other α variants (2 epochs, lr=2e-5, batch=1, grad_accum=8). Completes α ablation sweep.\", \"log_path\": \"/tmp/sft_alpha2_0.log\", \"metrics\": {\"epoch\": 2, \"mean_token_accuracy_final\": 0.8354, \"post_prune_accuracy\": 0.29, \"total_steps\": 1870, \"train_loss\": 0.7424, \"train_loss_final\": 0.6114, \"train_runtime_sec\": 2422}, \"notes\": \"α=2.0 SFT 完成 (1870/1870 steps, 2 epochs, ~40min). train_loss=0.7424, final loss=0.6114, token_acc=0.8354. Post-prune 29% → post-SFT 需 eval 确认. Checkpoint: /root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_2.0 (model.safetensors 11.5GB).\", \"parent\": \"alpha_ablation_westd_cal256\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"alpha_ablation_westd_cal256 (pruned_rasp_20_alpha2.0)\", \"command\": \"python sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_models/pruned_rasp_20_alpha2.0 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_2.0 --gpu 1 --epochs 2 --lr 2e-5 --batch_size 1 --grad_accum 8\", \"data_count\": 7473, \"data_path\": \"gsm8k train split\", \"eval_data\": \"gsm8k train (SFT recovery, not eval)\", \"gpu\": \"cuda:1\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (RASP pruned alpha=2.0, 20% sparsity)\", \"pid\": 43065, \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T15:41:31.384Z\"}, \"sft_grasp_20_westd\": {\"completed_at\": \"2026-05-15T15:00:56.053Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-15T13:50:39.294Z\", \"hypothesis\": \"D028: GraSP pruned model (8% post-prune) SFT recovery. Same params as RASP/Standard SFT (2 epochs, lr=2e-5, batch=1, grad_accum=8). Completes three-way comparison: Standard 27%→64%, RASP 31%→57%, GraSP 8%→?. Tests whether importance metric choice affects recovery potential.\", \"notes\": \"GraSP SFT 完成 (exit_code=0). 1870/1870 steps, 2 epochs, 58.5min. Final loss=0.5857, mean_token_accuracy=0.8392, grad_norm=9.375. train_runtime=3510s, train_loss=0.706. Model saved to /root/autodl-tmp/recovery_aware_struct_prune/sft_graspune_20/ (12.6GB). GraSP eval (N=100) 仍在 GPU 0 运行中 (PID 38120, 41/100, ~1.5h remaining).\", \"parent\": \"grasp_baseline_westd\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_graspune_20\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && python -u src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_graspune_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_graspune_20 --gpu 0 --num_train_epochs 2 --learning_rate 2e-5 --batch_size 1 --gradient_accumulation_steps 8 --max_seq_length 2048 --logging_steps 10 --seed 42\\\"\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 1.15, \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_grasp_20_westd.log\", \"pid\": \"38509\", \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-15T13:51:47.632Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 4148.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T15:01:02.359Z\"}, \"sft_alpha4_0_westd_retry\": {\"completed_at\": \"2026-05-15T13:48:02.432Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-15T12:46:36.918Z\", \"hypothesis\": \"D027: α=4.0 pruned model SFT recovery on westd (retry #3). α=4.0 gave highest post-prune accuracy (40%). Fix: CUDA_VISIBLE_DEVICES=1 + --gpu 0 (prevent GPU 0 collision with GraSP) + --save_strategy no (prevent checkpoint serialization crash). Same SFT params: 2 epochs, lr=2e-5, batch=1, grad_accum=8.\", \"metrics\": {\"accuracy_stderr\": 0.049, \"avg_response_length\": 238.56, \"eos_rate\": 0.98, \"mean_token_accuracy_final\": 0.8368, \"n_correct\": 62, \"n_total\": 100, \"post_prune_accuracy\": 0.4, \"post_sft_accuracy_100\": 0.62, \"sft_recovery_gain_pp\": 22, \"train_loss_final\": 0.7393, \"train_loss_last_logged\": 0.6106}, \"notes\": \"SFT training completed (1870/1870 steps, 2 epochs, ~30 min). GSM8K eval (N=100, greedy): 62% accuracy (62/100, stderr=0.049), EOS rate 98%, avg_len 238.56. Post-prune 40% → post-SFT 62% (+22pp recovery). Compared to α=1.0 RASP post-SFT (57%), α=4.0 is +5pp higher, confirming higher α amplifies recovery. Checkpoint: /root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_4.0. Eval JSON: results/eval_alpha_4.0_greedy.json.\", \"parent\": \"alpha_ablation_westd_cal256\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_4.0\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/alpha_ablation/alpha_4.0\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 python -u src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/alpha_ablation/alpha_4.0 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_4.0 --gpu 0 --num_train_epochs 2 --learning_rate 2e-5 --batch_size 1 --gradient_accumulation_steps 8 --max_seq_length 2048 --logging_steps 10 --seed 42\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.1, \"log_path\": \"/tmp/sft_alpha4.0.log\", \"model_name\": \"pruned_alpha4.0 (a=4.0, 20% sparsity)\", \"pid\": \"37013\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-15T13:42:03.641Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 358.8}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T13:48:13.666Z\"}, \"reeval_postprune_definitive\": {\"completed_at\": \"2026-05-15T12:30:41.698Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-15T09:46:32.498Z\", \"hypothesis\": \"D023: Definitive re-eval of pruned_standard_20 and pruned_rasp_20 with current eval_gsm8k.py + load_pruned_model. N=100, max_new_tokens=4096, greedy. Validates whether original 1% vs 29% is reproducible with current code.\", \"metrics\": {\"conclusion\": \"Original 29x advantage (29% vs 1%) not reproducible. Actual gap 4pp (31% vs 27% on westb), not statistically significant.\", \"original_claim_rasp\": 0.29, \"original_claim_standard\": 0.01, \"rasp_20_accuracy_westb\": 0.31, \"rasp_20_accuracy_westd\": 0.29, \"rasp_vs_standard_gap_pp\": 4, \"standard_20_accuracy_westb\": 0.27}, \"notes\": \"D023 definitive re-eval complete. westb: RASP 31%, Standard 27% (4pp gap). westd: RASP 29% (2pp delta from westb due to GPU driver 580 vs 595). Original 29% vs 1% claim invalidated — Standard was never 1%, likely eval bug in v4 pipeline. Post-prune gap is ~4pp, not statistically significant at N=100. GRPO Stage 2 is now the sole deterministic experiment for the paper narrative.\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A (eval only)\", \"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/pruned_{rasp,standard}_20 --max_samples 100 --max_new_tokens 4096\", \"data_count\": 100, \"data_path\": \"gsm8k_test\", \"log_path\": \"N/A\", \"model_name\": \"pruned_rasp_20 + pruned_standard_20\", \"seed\": 42, \"server\": \"westb-23072 + westd-11672\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T12:30:41.698Z\"}, \"sft_standard_20\": {\"completed_at\": \"2026-05-15T00:37:24.899Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-14T23:37:34.863Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-15T00:28:25.338475+00:00\"}]}, \"hypothesis\": \"D013 Stage 1: SFT warmup on Standard-pruned model (20%, 1% GSM8K) as negative control. Expected: SFT partially recovers format but reasoning remains limited.\", \"metrics\": {\"eos_rate_greedy_100\": 0.99, \"greedy_accuracy_100\": 0.64, \"greedy_avg_len\": 176.31, \"greedy_correct\": 64, \"greedy_max_len\": 4096, \"greedy_min_len\": 43, \"greedy_total\": 100, \"sampling_eos_rate_5\": 1, \"token_accuracy\": 0.83, \"total_steps\": 1870, \"train_loss_final\": 0.64, \"train_loss_initial\": 1.7, \"train_time_min\": 37}, \"notes\": \"SFT warmup SUCCESS (负对照). EOS恢复100% (3/3测试). Loss 1.70→0.64, token_accuracy 83%. 但推理准确率有限(2/3, 12+15算成41), 说明standard pruning破坏了关键推理结构, SFT只恢复了格式+EOS, 无法完全恢复数学推理. 平均生成49 tokens, 无重复循环. 训练37min, 1870 steps. Greedy eval N=100: 64% accuracy, avg_len=176.31, eos_rate=99%. N=100 sampling eval was killed (OOM by concurrent GRPO). Eval JSON: /root/recovery_aware_struct_prune/results/eval_sft_standard_20_combined.json. Checkpoint: /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20/\", \"reproduce\": {\"finished_at\": \"2026-05-15T00:28:23.640Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20\", \"command\": \"python src/sft_recovery.py --model_path /root/autodl-tmp/pruned_standard_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20 --num_train_epochs 2 --learning_rate 2e-5\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.83, \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_standard_20.log\", \"model_name\": \"pruned_standard_20\", \"pid\": \"249655\", \"seed\": 42, \"server\": \"westb-23072\", \"submitted_at\": \"2026-05-14T23:47:25.361Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2999.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T02:49:41.141Z\"}, \"sft_rasp_20\": {\"completed_at\": \"2026-05-15T00:36:44.657Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-14T23:37:33.162Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-15T00:28:21.234043+00:00\"}]}, \"hypothesis\": \"D013 Stage 1: SFT warmup on RASP-pruned model (20%, 29% GSM8K) to restore EOS generation ability before GRPO Stage 2.\", \"metrics\": {\"eos_rate_greedy_100\": 0.99, \"greedy_accuracy_100\": 0.57, \"greedy_avg_len\": 179.83, \"greedy_correct\": 57, \"greedy_max_len\": 4096, \"greedy_min_len\": 59, \"greedy_total\": 100, \"sampling_eos_rate_5\": 1, \"token_accuracy\": 0.83, \"total_steps\": 1870, \"train_loss_final\": 0.64, \"train_loss_initial\": 1.86, \"train_time_min\": 37}, \"notes\": \"SFT warmup SUCCESS. EOS恢复100% (5/5测试). Loss 1.86→0.64, token_accuracy 83%. 平均生成77 tokens, 无重复循环, 遵循GSM8K格式. 训练时间37min, 1870 steps (2 epochs). Greedy eval N=100: 57% accuracy, avg_len=179.83, eos_rate=99%. N=100 sampling eval was killed (OOM by concurrent GRPO). Eval JSON: /root/recovery_aware_struct_prune/results/eval_sft_rasp_20_combined.json. Checkpoint: /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20/\", \"reproduce\": {\"finished_at\": \"2026-05-15T00:28:21.036Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20\", \"command\": \"python src/sft_recovery.py --model_path /root/autodl-tmp/pruned_rasp_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20 --num_train_epochs 2 --learning_rate 2e-5\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 0.82, \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_rasp_20.log\", \"model_name\": \"pruned_rasp_20\", \"pid\": \"249577\", \"seed\": 42, \"server\": \"westb-23072\", \"submitted_at\": \"2026-05-14T23:47:23.413Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2961.2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T02:49:39.222Z\"}}, \"count\": 263, \"total\": 263, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.0981}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 18_

<details><summary>Logged reasoning block</summary>

```text
The registry data is too large. I need to delegate the audit work to subagents that can process the registry data and cross-reference it with the numbers in the paper. Let me spawn agents to handle this.

Let me think about the numbers I need to verify from each file:

**abstract.tex:**
1. Line 5: "20\% sparsity" - sparsity level parameter
2. Line 5: "$\alpha{=}2.0$" - alpha parameter
3. Line 5: "66.11\%" - GSM8K accuracy at alpha=2.0


4. Line 6: "4.4$\times$" - peak reward ratio CKA-only vs Standard
5. Line 7: "1.5B" - scale (model size)

**introduction.tex:**
1. Line 7: "20\% sparsity" 
2. Line 7: "0.54\,pp" - mean |Δ(GRPO-SFT)| across four criteria
3. Line 7: "0.61\,pp" - max of same
4. Line 7: "1.34\,pp" - max including dose-response and MBPP
5. Line 17: continuing to identify key metrics to cross-reference...

Generating markdown table... I'm now looking at the limitations section to extract the remaining numerical parameters—sample sizes, hyperparameter ranges, and seed counts—then I'll set up a process to systematically pull all the metrics from the paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "e31eb8e8-8c55-48ae-a8f4-d63363ad5ae4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015xCEAN4mwbVRdMaTy2uRnt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 686,
      "cache_read_input_tokens": 28688,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 686
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

_source line 19_

Registry 太大，我用 subagent 来处理数据审计。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "619004fe-974d-4965-b1a1-5b49af774069",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015xCEAN4mwbVRdMaTy2uRnt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 686,
      "cache_read_input_tokens": 28688,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 686
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

_source line 20_

<details open><summary>🔧 Tool call — Agent · `toolu_01DqLXKVyB8HFXo9RAjWmpwT`</summary>

````json
{
  "description": "Registry data audit for paper numbers",
  "prompt": "You are auditing quantitative claims in a paper against an experiment registry. The registry JSON is at:\n/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt\n\nThe file has schema: {result: string} where `result` is itself a JSON string that needs to be parsed.\n\nI need you to extract specific numbers from the registry to verify paper claims. Here are ALL the numbers I need you to find:\n\n1. **GSM8K accuracy at alpha=2.0, 20% sparsity, GRPO recovery** — paper claims 66.11%\n2. **Mean |Δ(GRPO-SFT)| across four fine-grained criteria at 20% sparsity on GSM8K** — paper claims 0.54 pp\n3. **Max |Δ(GRPO-SFT)| across four fine-grained criteria at 20% sparsity on GSM8K** — paper claims 0.61 pp  \n4. **Max |Δ(GRPO-SFT)| including dose-response variations and MBPP** — paper claims 1.34 pp\n5. **Peak reward ratio: CKA-only vs Standard under GRPO** — paper claims 4.4×\n6. **ShortGPT |Δ(GRPO-SFT)| on GSM8K** — paper claims -1.36 pp (or 1.36 pp)\n7. **|Δ(GRPO-SFT)| at each dose-response alpha point** — paper claims ≤ 1.14 pp at every point\n8. **15% sparsity GRPO-SFT differential for CKA-guided** — paper claims +1.51 pp\n9. **CKA similarity mean for CKA-only pruning** — paper claims μ=0.62\n10. **CKA similarity mean for collapsing methods** — paper claims μ≥0.88\n11. **Gradient magnitude ratio: CKA-only vs Standard** — paper claims 2.89×\n12. **f_0 (zero-variance batch fraction)** — paper claims > 0.5 for some condition\n13. **SFT-only gap across criteria** — paper claims 4.62 pp (in Table tab:decoupling)\n14. **|Δ(GRPO-SFT)| at 15-25% sparsity** — paper claims ≤ 1 pp\n15. **Qwen2.5-Math-7B cross-architecture N=200 sample size** — verify\n16. **1.5B scale experiment** — verify existence\n17. **MATH-500 results** — check if there are fixed eval versions; report both old and new values if available\n\n**How to process:**\n1. First probe the file structure: `jq 'type' file`, then parse the result string\n2. Use python/jq to extract all experiments, look at their exp_id, metrics, config fields\n3. Search for experiments related to: dose-response, decoupling, CKA-only, Standard, Random, alpha ablation, GRPO, SFT, ShortGPT, 1.5B, Qwen2.5-Math, MATH-500 fixed eval\n4. For each number above, report: the exp_id(s) that support it, the actual metric value in the registry, and whether it matches the paper claim\n\n**Output format** — for each number, one line:\n```\n[NUMBER] paper=X registry=Y exp_id=Z ✓/✗/⚠️\n```\nIf a number involves computation across multiple experiments (like mean |Δ|), show the individual values and the computation.\n\nBe thorough — I need EVERY number verified. If you can't find a registry source, say so explicitly.",
  "model": "sonnet"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "5a0186e5-314e-4707-8675-a905d44f71f7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015xCEAN4mwbVRdMaTy2uRnt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 686,
      "cache_read_input_tokens": 28688,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 686
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

_source line 21_

````json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a2a92311f30a7bab6",
  "tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "description": "Registry data audit for paper numbers",
  "task_type": "local_agent",
  "prompt": "You are auditing quantitative claims in a paper against an experiment registry. The registry JSON is at:\n/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt\n\nThe file has schema: {result: string} where `result` is itself a JSON string that needs to be parsed.\n\nI need you to extract specific numbers from the registry to verify paper claims. Here are ALL the numbers I need you to find:\n\n1. **GSM8K accuracy at alpha=2.0, 20% sparsity, GRPO recovery** — paper claims 66.11%\n2. **Mean |Δ(GRPO-SFT)| across four fine-grained criteria at 20% sparsity on GSM8K** — paper claims 0.54 pp\n3. **Max |Δ(GRPO-SFT)| across four fine-grained criteria at 20% sparsity on GSM8K** — paper claims 0.61 pp  \n4. **Max |Δ(GRPO-SFT)| including dose-response variations and MBPP** — paper claims 1.34 pp\n5. **Peak reward ratio: CKA-only vs Standard under GRPO** — paper claims 4.4×\n6. **ShortGPT |Δ(GRPO-SFT)| on GSM8K** — paper claims -1.36 pp (or 1.36 pp)\n7. **|Δ(GRPO-SFT)| at each dose-response alpha point** — paper claims ≤ 1.14 pp at every point\n8. **15% sparsity GRPO-SFT differential for CKA-guided** — paper claims +1.51 pp\n9. **CKA similarity mean for CKA-only pruning** — paper claims μ=0.62\n10. **CKA similarity mean for collapsing methods** — paper claims μ≥0.88\n11. **Gradient magnitude ratio: CKA-only vs Standard** — paper claims 2.89×\n12. **f_0 (zero-variance batch fraction)** — paper claims > 0.5 for some condition\n13. **SFT-only gap across criteria** — paper claims 4.62 pp (in Table tab:decoupling)\n14. **|Δ(GRPO-SFT)| at 15-25% sparsity** — paper claims ≤ 1 pp\n15. **Qwen2.5-Math-7B cross-architecture N=200 sample size** — verify\n16. **1.5B scale experiment** — verify existence\n17. **MATH-500 results** — check if there are fixed eval versions; report both old and new values if available\n\n**How to process:**\n1. First probe the file structure: `jq 'type' file`, then parse the result string\n2. Use python/jq to extract all experiments, look at their exp_id, metrics, config fields\n3. Search for experiments related to: dose-response, decoupling, CKA-only, Standard, Random, alpha ablation, GRPO, SFT, ShortGPT, 1.5B, Qwen2.5-Math, MATH-500 fixed eval\n4. For each number above, report: the exp_id(s) that support it, the actual metric value in the registry, and whether it matches the paper claim\n\n**Output format** — for each number, one line:\n```\n[NUMBER] paper=X registry=Y exp_id=Z ✓/✗/⚠️\n```\nIf a number involves computation across multiple experiments (like mean |Δ|), show the individual values and the computation.\n\nBe thorough — I need EVERY number verified. If you can't find a registry source, say so explicitly.",
  "uuid": "49c10e5f-a0d3-4b2c-a3d6-0dad46ced67e",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db"
}
````

---


## Round 1

## Round 1

212 recorded events


### User

_source line 22 · 2026-05-24T04:33:11.610Z_

You are auditing quantitative claims in a paper against an experiment registry. The registry JSON is at:
/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt

The file has schema: {result: string} where `result` is itself a JSON string that needs to be parsed.

I need you to extract specific numbers from the registry to verify paper claims. Here are ALL the numbers I need you to find:

1. **GSM8K accuracy at alpha=2.0, 20% sparsity, GRPO recovery** — paper claims 66.11%
2. **Mean |Δ(GRPO-SFT)| across four fine-grained criteria at 20% sparsity on GSM8K** — paper claims 0.54 pp
3. **Max |Δ(GRPO-SFT)| across four fine-grained criteria at 20% sparsity on GSM8K** — paper claims 0.61 pp  
4. **Max |Δ(GRPO-SFT)| including dose-response variations and MBPP** — paper claims 1.34 pp
5. **Peak reward ratio: CKA-only vs Standard under GRPO** — paper claims 4.4×
6. **ShortGPT |Δ(GRPO-SFT)| on GSM8K** — paper claims -1.36 pp (or 1.36 pp)
7. **|Δ(GRPO-SFT)| at each dose-response alpha point** — paper claims ≤ 1.14 pp at every point
8. **15% sparsity GRPO-SFT differential for CKA-guided** — paper claims +1.51 pp
9. **CKA similarity mean for CKA-only pruning** — paper claims μ=0.62
10. **CKA similarity mean for collapsing methods** — paper claims μ≥0.88
11. **Gradient magnitude ratio: CKA-only vs Standard** — paper claims 2.89×
12. **f_0 (zero-variance batch fraction)** — paper claims > 0.5 for some condition
13. **SFT-only gap across criteria** — paper claims 4.62 pp (in Table tab:decoupling)
14. **|Δ(GRPO-SFT)| at 15-25% sparsity** — paper claims ≤ 1 pp
15. **Qwen2.5-Math-7B cross-architecture N=200 sample size** — verify
16. **1.5B scale experiment** — verify existence
17. **MATH-500 results** — check if there are fixed eval versions; report both old and new values if available

**How to process:**
1. First probe the file structure: `jq 'type' file`, then parse the result string
2. Use python/jq to extract all experiments, look at their exp_id, metrics, config fields
3. Search for experiments related to: dose-response, decoupling, CKA-only, Standard, Random, alpha ablation, GRPO, SFT, ShortGPT, 1.5B, Qwen2.5-Math, MATH-500 fixed eval
4. For each number above, report: the exp_id(s) that support it, the actual metric value in the registry, and whether it matches the paper claim

**Output format** — for each number, one line:
```
[NUMBER] paper=X registry=Y exp_id=Z ✓/✗/⚠️
```
If a number involves computation across multiple experiments (like mean |Δ|), show the individual values and the computation.

Be thorough — I need EVERY number verified. If you can't find a registry source, say so explicitly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "b1cbc01f-82ba-437e-8ff1-8ee6fcae35f4"
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
  "task_id": "a2a92311f30a7bab6",
  "tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "description": "Reading ~/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt",
  "usage": {
    "total_tokens": 15745,
    "tool_uses": 1,
    "duration_ms": 2708
  },
  "last_tool_name": "Read",
  "uuid": "d1a6a887-4e2b-4931-af78-99deb0d91ed8",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db"
}
```

---


### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Read · `toolu_01DJCXGE5nrcCecgcHjjoQpw`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "e41cb5cb-e5ff-41db-9ef5-dd9c05a44715",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01AA6BxXTYB1BrvDv2uFJNLz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15736,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15736,
        "ephemeral_1h_input_tokens": 0
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

_source line 25 · 2026-05-24T04:33:14.334Z_

<details><summary>↩ Tool result · reported error · `toolu_01DJCXGE5nrcCecgcHjjoQpw`</summary>

```text
File content (425.2KB) exceeds maximum allowed size (256KB). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "ff23e5f0-7b14-45b7-affb-eff63a5ad178",
  "tool_use_result": "Error: File content (425.2KB) exceeds maximum allowed size (256KB). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
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
  "task_id": "a2a92311f30a7bab6",
  "tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "description": "Reading ~/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt",
  "usage": {
    "total_tokens": 16807,
    "tool_uses": 2,
    "duration_ms": 5947
  },
  "last_tool_name": "Read",
  "uuid": "4980c6b3-a056-4ad3-918d-95cfc6b7e0af",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db"
}
```

---


### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Read · `toolu_01GXQo4KhNG4qZU1S5bAZpbS`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "8d3a0914-d591-4669-9555-d1f02b3a48f1",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_011yf4UParNcb9DUbaF6gTuJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1062,
      "cache_read_input_tokens": 15736,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1062,
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

_source line 28 · 2026-05-24T04:33:17.985Z_

<details><summary>↩ Tool result · reported error · `toolu_01GXQo4KhNG4qZU1S5bAZpbS`</summary>

```text
File content (182475 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "d2c1a6c2-daf4-4014-b5bf-73d195415add",
  "tool_use_result": "Error: File content (182475 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
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
  "task_id": "a2a92311f30a7bab6",
  "tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "description": "Running Check file structure and parse outer JSON",
  "usage": {
    "total_tokens": 17099,
    "tool_uses": 3,
    "duration_ms": 14265
  },
  "last_tool_name": "Bash",
  "uuid": "07c4e767-105b-4409-989d-8b82df0151c4",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db"
}
```

---


### Tool call

_source line 30_

<details open><summary>🔧 Tool call — Bash · `toolu_01M3fibCHZET58YZRkjnjqxc`</summary>

```json
{
  "command": "FPATH=\"/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt\"\nwc -c \"$FPATH\"\npython3 -c \"\nimport json\nwith open('$FPATH') as f:\n    raw = f.read()\nouter = json.loads(raw)\nprint('outer keys:', list(outer.keys()))\nresult_str = outer['result']\nprint('result type:', type(result_str))\nprint('result preview (first 500):', result_str[:500])\n\"",
  "description": "Check file structure and parse outer JSON"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "63a8dd7b-9a56-48d7-8439-bea53a16d18c",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0129qizNJCoqaVwt9ebZ68Rh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 246,
      "cache_read_input_tokens": 16798,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 246,
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

_source line 31 · 2026-05-24T04:33:26.082Z_

<details><summary>↩ Tool result · `toolu_01M3fibCHZET58YZRkjnjqxc`</summary>

```text
435436 /home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt
outer keys: ['result']
result type: &lt;class 'str'>
result preview (first 500): {"success": true, "data": {"experiments": {"eval_math500_sft_rasp_alpha2p0_20_fixed": {"status": "DONE", "retry_count": 0, "created_at": "2026-05-23T19:48:01.183Z", "updated_at": "2026-05-24T03:10:25.471Z", "hypothesis": "SFT RASP α=2.0 20% MATH-500 with fixed eval script. Model on westd (sft_rasp_alpha2p0_20). P1 dose-response table.", "spec": {"command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLI
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "0080cc1a-3bae-4419-998b-7f10a6bafcd2"
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
  "task_id": "a2a92311f30a7bab6",
  "tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "description": "Running List all experiment IDs in registry",
  "usage": {
    "total_tokens": 17774,
    "tool_uses": 4,
    "duration_ms": 18016
  },
  "last_tool_name": "Bash",
  "uuid": "10bd841c-b0b5-4ac2-a397-cce5e7784bdd",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db"
}
```

---


### Tool call

_source line 33_

<details open><summary>🔧 Tool call — Bash · `toolu_014v4TnQXGux7H2xsL8ktTvv`</summary>

```json
{
  "command": "FPATH=\"/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt\"\npython3 -c \"\nimport json\nwith open('$FPATH') as f:\n    raw = f.read()\nouter = json.loads(raw)\ndata = json.loads(outer['result'])\nexps = data['data']['experiments']\nprint('Total experiments:', len(exps))\nprint()\nprint('All exp_ids:')\nfor eid in sorted(exps.keys()):\n    print(' ', eid)\n\"",
  "description": "List all experiment IDs in registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "ceb975a7-7ae2-42e8-abc7-ac6438a1610c",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01MRgg6rQ5Qu3tcxp6B9k7wT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 610,
      "cache_read_input_tokens": 17044,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 610,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
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

_source line 34 · 2026-05-24T04:33:29.759Z_

<details><summary>↩ Tool result · `toolu_014v4TnQXGux7H2xsL8ktTvv`</summary>

```text
Total experiments: 263

All exp_ids:
  alpha_ablation_sweep
  cka_calibration_stability_ablation
  cka_scoring_stability_ablation
  eval-sft-alpha-0p0
  eval-sft-alpha-1p0
  eval_gradient_postsft
  eval_grpo_rasp_20_qwen_math
  eval_grpo_rasp_25
  eval_grpo_rasp_25_qwen_math
  eval_grpo_rasp_rlvr_20_qwen_math
  eval_grpo_rasp_v9_step10
  eval_grpo_rasp_v9_step5
  eval_grpo_standard_20_qwen_math
  eval_grpo_standard_25
  eval_grpo_standard_25_qwen_math
  eval_grpo_unpruned_v2_step100
  eval_grpo_unpruned_v2_step90
  eval_gsm8k_dense_unpruned
  eval_gsm8k_grpo_alpha0p5_20
  eval_gsm8k_grpo_alpha2p0_20
  eval_gsm8k_grpo_alpha3p0_20
  eval_gsm8k_grpo_alpha4_20_v3
  eval_gsm8k_grpo_cka_only_15_seed123
  eval_gsm8k_grpo_cka_only_15_seed456
  eval_gsm8k_grpo_cka_only_15_v2
  eval_gsm8k_grpo_cka_only_20_1p5b
  eval_gsm8k_grpo_cka_only_20_seed123
  eval_gsm8k_grpo_cka_only_20_seed456_full
  eval_gsm8k_grpo_cka_only_20_v2
  eval_gsm8k_grpo_cka_only_20_verify
  eval_gsm8k_grpo_cka_only_25_v3
  eval_gsm8k_grpo_depth_first_20
  eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v3
  eval_gsm8k_grpo_random_20_seed123_v2
  eval_gsm8k_grpo_random_20_seed456
  eval_gsm8k_grpo_random_20_v2
  eval_gsm8k_grpo_rasp_20_1p5b
  eval_gsm8k_grpo_rasp_20_fair
  eval_gsm8k_grpo_shortgpt_20
  eval_gsm8k_grpo_standard_15_seed123_v3
  eval_gsm8k_grpo_standard_15_seed456_v3
  eval_gsm8k_grpo_standard_15_v2
  eval_gsm8k_grpo_standard_20_1p5b
  eval_gsm8k_grpo_standard_20_fair_v2
  eval_gsm8k_grpo_standard_20_seed123
  eval_gsm8k_grpo_standard_20_seed123_full
  eval_gsm8k_grpo_standard_20_seed456
  eval_gsm8k_grpo_standard_20_seed456_full
  eval_gsm8k_grpo_standard_25
  eval_gsm8k_grpo_unstructured_20
  eval_gsm8k_sft_alpha0p5_20
  eval_gsm8k_sft_alpha2p0_20
  eval_gsm8k_sft_alpha3p0_20
  eval_gsm8k_sft_alpha4_20_v5
  eval_gsm8k_sft_cka_only_15
  eval_gsm8k_sft_cka_only_20
  eval_gsm8k_sft_cka_only_20_1p5b
  eval_gsm8k_sft_cka_only_25
  eval_gsm8k_sft_depth_first_20
  eval_gsm8k_sft_qwen_cka_only_20
  eval_gsm8k_sft_qwen_standard_20
  eval_gsm8k_sft_random_20
  eval_gsm8k_sft_rasp_20
  eval_gsm8k_sft_rasp_20_1p5b
  eval_gsm8k_sft_shortgpt_20
  eval_gsm8k_sft_standard_15
  eval_gsm8k_sft_standard_20
  eval_gsm8k_sft_standard_20_1p5b
  eval_gsm8k_sft_standard_25
  eval_humaneval_grpo_cka_only_20_1p5b_2048
  eval_humaneval_grpo_cka_only_20_2048
  eval_humaneval_grpo_rasp_20
  eval_humaneval_grpo_rasp_20_2048
  eval_humaneval_grpo_rasp_20_fair_2048
  eval_humaneval_grpo_standard_20
  eval_humaneval_grpo_standard_20_1p5b_2048
  eval_humaneval_grpo_standard_20_2048
  eval_humaneval_grpo_standard_20_fair_2048_v3
  eval_humaneval_sft_cka_only_20_1p5b_2048
  eval_humaneval_sft_cka_only_20_2048_v2
  eval_humaneval_sft_rasp_20
  eval_humaneval_sft_rasp_20_1p5b_2048
  eval_humaneval_sft_rasp_20_2048
  eval_humaneval_sft_rasp_20_2048_v2
  eval_humaneval_sft_standard_20
  eval_humaneval_sft_standard_20_1p5b_2048
  eval_humaneval_sft_standard_20_2048_v2
  eval_humaneval_sft_standard_20_2048_v3
  eval_humaneval_sft_standard_25
  eval_humaneval_unpruned
  eval_humaneval_unpruned_2048
  eval_math500_dense_2048
  eval_math500_dense_unpruned
  eval_math500_grpo_cka_only_20
  eval_math500_grpo_cka_only_20_2048
  eval_math500_grpo_cka_only_20_2048_v2
  eval_math500_grpo_cka_only_20_fixed
  eval_math500_grpo_cka_only_25_fixed
  eval_math500_grpo_cka_only_25_v2
  eval_math500_grpo_random_20_v3
  eval_math500_grpo_rasp_20_fair
  eval_math500_grpo_rasp_alpha0p5_20
  eval_math500_grpo_rasp_alpha1p0_20
  eval_math500_grpo_rasp_alpha1p0_20_fixed
  eval_math500_grpo_rasp_alpha2p0_20
  eval_math500_grpo_rasp_alpha2p0_20_fixed
  eval_math500_grpo_rasp_alpha3p0_20
  eval_math500_grpo_rasp_alpha4p0_20
  eval_math500_grpo_standard_20_fair_2048_v2
  eval_math500_grpo_standard_20_fair_v2
  eval_math500_grpo_standard_20_fixed
  eval_math500_sft_cka_only_20_fixed_v2
  eval_math500_sft_cka_only_20_v4_restart
  eval_math500_sft_cka_only_20_westd
  eval_math500_sft_cka_only_25_v2
  eval_math500_sft_qwen_math_cka_only_20
  eval_math500_sft_random_20_v3
  eval_math500_sft_rasp_20
  eval_math500_sft_rasp_20_2048
  eval_math500_sft_rasp_alpha0p5_20
  eval_math500_sft_rasp_alpha1p0_20_fixed
  eval_math500_sft_rasp_alpha1p0_20_v2
  eval_math500_sft_rasp_alpha2p0_20
  eval_math500_sft_rasp_alpha2p0_20_fixed
  eval_math500_sft_rasp_alpha3p0_20
  eval_math500_sft_rasp_alpha4p0_20
  eval_math500_sft_standard_20
  eval_math500_sft_standard_20_1p5b
  eval_math500_sft_standard_20_2048_v2
  eval_math500_sft_standard_20_2048_v3
  eval_math500_sft_standard_25
  eval_math500_unpruned
  eval_mbpp_dense_unpruned
  eval_mbpp_grpo_cka_only_20
  eval_mbpp_grpo_rasp_20
  eval_mbpp_grpo_shortgpt_20_v2
  eval_mbpp_grpo_standard_20_v3
  eval_mbpp_grpo_standard_20_v4
  eval_mbpp_sft_cka_only_20
  eval_mbpp_sft_rasp_20
  eval_mbpp_sft_shortgpt_20_v2
  eval_mbpp_sft_standard_20_1p5b
  eval_mbpp_sft_standard_20_v4
  eval_pass_k8_rasp_20_grpo_deepseek
  eval_pass_k8_rasp_20_grpo_qwen_math
  eval_pass_k8_rasp_20_sft_qwen_math
  eval_pass_k8_standard_20_grpo_deepseek
  eval_pass_k8_standard_20_grpo_qwen_math_v2
  eval_pass_k8_unpruned_qwen_math
  eval_postprune_qwen_math_cka_only_20
  eval_postprune_qwen_math_standard_20
  eval_postprune_rasp_25
  eval_postprune_rasp_30
  eval_postprune_standard_30
  eval_sft_alpha_2p0
  eval_sft_cka_only_20
  eval_sft_cka_only_20_n1319
  eval_sft_qwen_math_rasp_25
  eval_sft_qwen_math_standard_25
  eval_sft_rasp_20_full
  eval_sft_rasp_20_westd_n100
  eval_sft_rasp_20_westd_n100_v2
  eval_sft_rasp_25
  eval_sft_rasp_full_westd
  eval_sft_rasp_qwen_math_n200
  eval_sft_standard_20_westd_n100
  eval_sft_standard_20_westd_n100_v2
  eval_sft_standard_25
  eval_sft_standard_full_westd
  eval_sft_standard_qwen_math_n200
  eval_sft_unpruned_full
  eval_sft_unpruned_n100
  eval_unstructured_20
  floor_ablation_0p3_cka_only_20_v2
  floor_ablation_0p5_cka_only_20_v2
  floor_ablation_0p6_cka_only_20_v2
  gradient_flow_analysis
  gradient_flow_v3
  gradient_sft_v3
  grasp_baseline_westd
  grpo_alpha4_20
  grpo_cka_only_15_seed123
  grpo_cka_only_15_seed456
  grpo_cka_only_15_v2
  grpo_cka_only_20
  grpo_cka_only_20_1p5b
  grpo_cka_only_20_extended_300
  grpo_cka_only_20_seed123
  grpo_cka_only_20_seed456
  grpo_cka_only_25
  grpo_qwen_math_cka_only_20
  grpo_random_20
  grpo_random_20_retrain_v2
  grpo_random_20_seed123
  grpo_random_20_seed123_v2
  grpo_random_20_seed456
  grpo_rasp_20_1p5b
  grpo_rasp_20_fair
  grpo_rasp_25
  grpo_rasp_alpha3p0_20
  grpo_rasp_alpha3p0_20_v2
  grpo_rasp_qwen_math_v3
  grpo_rasp_rlvr_20_qwen_math
  grpo_stage2_rasp_20_v9
  grpo_standard_15_seed123_v3
  grpo_standard_15_seed456_v3
  grpo_standard_15_v2
  grpo_standard_20_1p5b
  grpo_standard_20_extended_300_v2
  grpo_standard_20_fair
  grpo_standard_20_seed123
  grpo_standard_20_seed456
  grpo_standard_25
  grpo_standard_25_westb
  grpo_unpruned_v2
  inference_bench_cka_only_20_clean
  inference_bench_clean_v2
  inference_speedup_plan016_v2
  multiseed_serial_westb
  prune_cka_only_25
  prune_cka_only_30
  prune_eval_cka_only_30
  prune_eval_standard_30
  prune_rasp_20_qwen_math
  prune_rasp_25
  prune_rasp_25_qwen_math
  prune_rasp_30
  prune_rasp_rlvr_20
  prune_rasp_rlvr_20_qwen_math
  prune_standard_20_qwen_math
  prune_standard_25
  prune_standard_25_qwen_math
  prune_standard_30
  reeval_postprune_definitive
  sft-alpha-1p0
  sft_alpha2_0_westd
  sft_alpha4_0_westd_retry
  sft_cka_only_20
  sft_cka_only_20_1p5b
  sft_cka_only_25
  sft_grasp_20_westd
  sft_qwen_math_cka_only_20_v2
  sft_qwen_math_rasp_25
  sft_qwen_math_standard_25
  sft_random_20
  sft_rasp_20
  sft_rasp_20_1p5b
  sft_rasp_20_qwen_math
  sft_rasp_20_westd_retrain
  sft_rasp_25
  sft_rasp_rlvr_20
  sft_rasp_rlvr_20_qwen_math
  sft_shortgpt_20
  sft_standard_20
  sft_standard_20_1p5b
  sft_standard_20_qwen_math
  sft_standard_20_retrain
  sft_standard_20_retrain_westd
  sft_standard_20_westd_retrain
  sft_standard_25
  sft_standard_25_retrain
  sft_standard_25_westd
  sft_unpruned_baseline
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "3ca733dc-9cde-436d-b311-b7618ab508f0"
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
  "task_id": "a2a92311f30a7bab6",
  "tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "description": "Running Check key experiments for claim #1",
  "usage": {
    "total_tokens": 22215,
    "tool_uses": 5,
    "duration_ms": 30725
  },
  "last_tool_name": "Bash",
  "uuid": "006be737-edf1-42e1-9e24-888cf4d57d84",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db"
}
```

---


### Tool call

_source line 36_

<details open><summary>🔧 Tool call — Bash · `toolu_0168qZgC2VFT8YyVmMMGRGbh`</summary>

```json
{
  "command": "FPATH=\"/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt\"\npython3 << 'EOF'\nimport json\nwith open(FPATH) as f:\n    raw = f.read()\nouter = json.loads(raw)\ndata = json.loads(outer['result'])\nexps = data['data']['experiments']\n\n# For each experiment, show its metrics/results fields\ndef get_metrics(exp):\n    e = exps[exp]\n    result = e.get('result', {})\n    metrics = e.get('metrics', {})\n    return result, metrics\n\n# Check the key experiments for claim #1: GSM8K acc at alpha=2.0, 20% sparsity, GRPO recovery\nkey_ids = [\n    'eval_gsm8k_grpo_alpha2p0_20',\n    'eval_gsm8k_sft_alpha2p0_20',\n    'eval_gsm8k_grpo_rasp_20_fair',\n    'eval_gsm8k_sft_rasp_20',\n]\nfor eid in key_ids:\n    if eid in exps:\n        e = exps[eid]\n        print(f\"\\n=== {eid} ===\")\n        print(f\"  status: {e.get('status')}\")\n        print(f\"  result: {json.dumps(e.get('result', {}), indent=2)[:800]}\")\n        print(f\"  metrics: {json.dumps(e.get('metrics', {}), indent=2)[:400]}\")\nEOF\n",
  "description": "Check key experiments for claim #1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "71c849f8-4852-4d1e-96c6-b92a91a01a5b",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01TVj4pMm3ZkqwCZNkQ5j1E1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4407,
      "cache_read_input_tokens": 17654,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4407,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 34,
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

_source line 37 · 2026-05-24T04:33:42.546Z_

<details><summary>↩ Tool result · reported error · `toolu_0168qZgC2VFT8YyVmMMGRGbh`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;stdin>", line 2, in &lt;module>
NameError: name 'FPATH' is not defined
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "56a4b41e-001c-4b1d-ac2a-9ef7d6d1274d",
  "tool_use_result": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;stdin>\", line 2, in &lt;module>\nNameError: name 'FPATH' is not defined"
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
  "task_id": "a2a92311f30a7bab6",
  "tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "description": "Running Check key GSM8K alpha=2.0 experiments",
  "usage": {
    "total_tokens": 22879,
    "tool_uses": 6,
    "duration_ms": 35561
  },
  "last_tool_name": "Bash",
  "uuid": "d69d26a3-a121-437b-b3ee-39290bda97e2",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db"
}
```

---


### Tool call

_source line 39_

<details open><summary>🔧 Tool call — Bash · `toolu_01NPyT3MUnL5vA6naDFyZFaD`</summary>

```json
{
  "command": "FPATH=\"/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt\"\npython3 -c \"\nimport json\nFPATH='$FPATH'\nwith open(FPATH) as f:\n    raw = f.read()\nouter = json.loads(raw)\ndata = json.loads(outer['result'])\nexps = data['data']['experiments']\n\nkey_ids = [\n    'eval_gsm8k_grpo_alpha2p0_20',\n    'eval_gsm8k_sft_alpha2p0_20',\n    'eval_gsm8k_grpo_rasp_20_fair',\n    'eval_gsm8k_sft_rasp_20',\n]\nfor eid in key_ids:\n    if eid in exps:\n        e = exps[eid]\n        print('=== ' + eid + ' ===')\n        print('  status:', e.get('status'))\n        r = e.get('result', {})\n        m = e.get('metrics', {})\n        print('  result:', json.dumps(r)[:600])\n        print('  metrics:', json.dumps(m)[:400])\n        print()\n\"\n",
  "description": "Check key GSM8K alpha=2.0 experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "e38e36e7-6c36-45de-8a07-b02e0783ce1e",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01TuPq1hztVqNiks4yJx8VP8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 601,
      "cache_read_input_tokens": 22061,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 601,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 63,
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

_source line 40 · 2026-05-24T04:33:47.266Z_

<details><summary>↩ Tool result · `toolu_01NPyT3MUnL5vA6naDFyZFaD`</summary>

```text
=== eval_gsm8k_grpo_alpha2p0_20 ===
  status: DONE
  result: {}
  metrics: {"gsm8k_accuracy": 0.6611, "gsm8k_correct": 872, "gsm8k_total": 1319}

=== eval_gsm8k_sft_alpha2p0_20 ===
  status: DONE
  result: {}
  metrics: {"gsm8k_accuracy": 0.6497, "gsm8k_correct": 857, "gsm8k_total": 1319}

=== eval_gsm8k_grpo_rasp_20_fair ===
  status: DONE
  result: {}
  metrics: {"accuracy": 0.6088, "stderr": 0.0134, "n_correct": 803, "n_total": 1319, "eos_rate": 0.9879, "avg_response_length": 195.7}

=== eval_gsm8k_sft_rasp_20 ===
  status: DONE
  result: {}
  metrics: {"gsm8k_accuracy": 0.6149, "gsm8k_accuracy_ci": 0.0134, "correct": 811, "total": 1319, "eos_rate": 0.9826, "avg_response_length": 216.5}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "2199b4f8-8041-4a2a-8f8a-3ba948c7222f"
}
```

</details>

---


### System

_source line 41_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2a92311f30a7bab6",
  "tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "description": "Running Check westd fine-grained evaluation experiments",
  "usage": {
    "total_tokens": 23690,
    "tool_uses": 7,
    "duration_ms": 43436
  },
  "last_tool_name": "Bash",
  "uuid": "310ab86d-9f51-44dd-9089-1347af34bdb0",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db"
}
```

---


### Tool call

_source line 42_

<details open><summary>🔧 Tool call — Bash · `toolu_01EbNVK9Zorp2TCBdmMXZvWn`</summary>

```json
{
  "command": "FPATH=\"/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt\"\npython3 -c \"\nimport json\nFPATH='$FPATH'\nwith open(FPATH) as f:\n    raw = f.read()\nouter = json.loads(raw)\ndata = json.loads(outer['result'])\nexps = data['data']['experiments']\n\n# Look at ALL experiments related to standard 20% for decoupling analysis\n# Also check if there's a westd eval with fine-grained criteria\nkey_ids = [\n    'eval_sft_standard_20_westd_n100',\n    'eval_sft_standard_20_westd_n100_v2',\n    'eval_sft_rasp_20_westd_n100',\n    'eval_sft_rasp_20_westd_n100_v2',\n    'eval_sft_standard_full_westd',\n    'eval_sft_rasp_full_westd',\n    'eval_sft_rasp_20_full',\n    'eval_sft_alpha_2p0',\n]\nfor eid in key_ids:\n    if eid in exps:\n        e = exps[eid]\n        print('=== ' + eid + ' ===')\n        print('  status:', e.get('status'))\n        r = e.get('result', {})\n        m = e.get('metrics', {})\n        print('  result:', json.dumps(r)[:800])\n        print('  metrics:', json.dumps(m)[:800])\n        print()\n\"\n",
  "description": "Check westd fine-grained evaluation experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "c8f5a143-b32c-41c0-810c-3d64170b2815",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01UFbXu1n17cTzNvzkiVDLdz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 807,
      "cache_read_input_tokens": 22662,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 807,
        "ephemeral_1h_input_tokens": 0
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

_source line 43 · 2026-05-24T04:33:55.144Z_

<details><summary>↩ Tool result · `toolu_01EbNVK9Zorp2TCBdmMXZvWn`</summary>

```text
=== eval_sft_standard_20_westd_n100 ===
  status: DONE
  result: {}
  metrics: {"accuracy": 0.63, "avg_len": 260.57, "eos_rate": 0.97, "n_correct": 63, "n_total": 100, "stderr": 0.048}

=== eval_sft_standard_20_westd_n100_v2 ===
  status: DONE
  result: {}
  metrics: {"accuracy": 0.63, "avg_len": 260.57, "eos_rate": 0.97, "n_correct": 63, "n_total": 100}

=== eval_sft_rasp_20_westd_n100 ===
  status: DONE
  result: {}
  metrics: {"accuracy": 0.67, "avg_len": 182.39, "eos_rate": 0.99, "n_correct": 67, "n_total": 100, "stderr": 0.047}

=== eval_sft_rasp_20_westd_n100_v2 ===
  status: DONE
  result: {}
  metrics: {"accuracy": 0.67, "avg_len": 182.39, "eos_rate": 0.99, "n_correct": 67, "n_total": 100}

=== eval_sft_standard_full_westd ===
  status: DONE
  result: {}
  metrics: {"accuracy": 0.5929, "avg_len": 226.7, "eos_rate": 0.9803, "n_correct": 782, "n_total": 1319, "stderr": 0.01353}

=== eval_sft_rasp_full_westd ===
  status: DONE
  result: {}
  metrics: {"accuracy": 0.6149, "avg_len": 216.5, "eos_rate": 0.9826, "n_correct": 811, "n_total": 1319, "stderr": 0.0134}

=== eval_sft_rasp_20_full ===
  status: DONE
  result: {}
  metrics: {"accuracy": 0.6156, "avg_response_length": 210.95, "eos_rate": 0.9841, "n_correct": 812, "n_samples": 1319, "natural_eos": 1298, "stderr": 0.0134, "truncated": 21}

=== eval_sft_alpha_2p0 ===
  status: DONE
  result: {}
  metrics: {"accuracy": 0.62, "avg_len": 277.41, "eos_rate": 0.97, "n_correct": 62, "n_total": 100, "stderr": 0.0485}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "2170eb5c-8122-4f1d-8a63-562449a4e023"
}
```

</details>

---


### System

_source line 44_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2a92311f30a7bab6",
  "tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "description": "Running Search for fine-grained criteria metrics across all experiments",
  "usage": {
    "total_tokens": 25127,
    "tool_uses": 8,
    "duration_ms": 52278
  },
  "last_tool_name": "Bash",
  "uuid": "cdf802cd-4a24-42f3-8216-b8290795ae77",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db"
}
```

---


### Tool call

_source line 45_

<details open><summary>🔧 Tool call — Bash · `toolu_01HVLBKH4245ekya4qDKgkef`</summary>

```json
{
  "command": "FPATH=\"/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt\"\npython3 -c \"\nimport json\nFPATH='$FPATH'\nwith open(FPATH) as f:\n    raw = f.read()\nouter = json.loads(raw)\ndata = json.loads(outer['result'])\nexps = data['data']['experiments']\n\n# Look for fine-grained criteria: step_validity, formatting, correctness, etc.\n# Check all experiments that might have multi-criteria metrics\nfor eid, e in exps.items():\n    m = e.get('metrics', {})\n    mstr = json.dumps(m)\n    if any(k in mstr.lower() for k in ['step', 'format', 'criterion', 'criteria', 'reasoning', 'precision', 'completeness', 'clarity']):\n        print('=== ' + eid + ' ===')\n        print('  metrics:', mstr[:600])\n        print()\n\"\n",
  "description": "Search for fine-grained criteria metrics across all experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "2127b8da-a4fa-4dab-aa91-33cfbee4f6d6",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01VzSBaQC7htBtJvCUVPquo1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1404,
      "cache_read_input_tokens": 23469,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1404,
        "ephemeral_1h_input_tokens": 0
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

_source line 46 · 2026-05-24T04:34:04.010Z_

<details><summary>↩ Tool result · `toolu_01HVLBKH4245ekya4qDKgkef`</summary>

```text
=== grpo_random_20_retrain_v2 ===
  metrics: {"final_reward": 0.2875, "final_reward_std": 0.4291, "final_loss": 0.06684, "final_kl": 0.004236, "final_entropy": 0.1704, "final_completion_length_mean": 189.1, "final_grad_norm": 5.531, "frac_reward_zero_std": 0.4, "wandb_run_id": "9c16hnf7", "wandb_run_name": "grpo_sft_random_20", "training_steps": 100, "training_time_hours": 3.07}

=== grpo_standard_25 ===
  metrics: {"clipped_ratio": 0.92, "collapse_pattern": "near_total_collapse", "comparison_vs_rasp_25": "worse_than_rasp_25(0.009)", "kl_final": 0.0012, "reward_final": 0.0075, "total_steps": 100, "wall_clock_min": 44, "wandb_run_id": "16vqw4e6"}

=== sft_standard_25_retrain ===
  metrics: {"train_loss": 0.8584, "token_accuracy": 0.8, "steps": 1870, "epochs": 2}

=== grpo_alpha4_20 ===
  metrics: {"final_reward": 0.198, "reward_range": "0.146-0.256", "steps": 100, "final_loss": 0.018, "final_kl": 0.00198}

=== grpo_standard_25_westb ===
  metrics: {"reward": 0.00813, "steps": 100, "collapse_pattern": "near_total_collapse"}

=== sft_random_20 ===
  metrics: {"steps": 1870, "model_size_gb": 12}

=== grpo_random_20 ===
  metrics: {"reward_mean": 0.164, "reward_range": [0.14, 0.19], "reward_peak": 0.19, "reward_peak_step": 70, "frac_zero_std_mean": 0.333, "frac_zero_std_range": [0.3, 0.4], "entropy_mean": 0.221, "entropy_range": [0.2, 0.24], "kl_mean": 0.0045, "steps_captured": 9, "max_step": 90, "pattern": "stable plateau, no collapse", "data_source": "log_file (W&B crashed before sync)"}

=== grpo_cka_only_25 ===
  metrics: {"reward": 0.2875, "steps": 100}

=== grpo_standard_15_v2 ===
  metrics: {"loss": 0.01142, "reward": 0.1375, "reward_std": 0.2778, "kl": 0.004099, "entropy": 0.1932, "grad_norm": 3.547, "total_steps": 100, "training_time": "21m49s"}

=== grpo_cka_only_15_v2 ===
  metrics: {"final_loss": 0.2027, "avg_train_loss": 0.11, "final_reward": 0.4019, "final_kl": 0.0018, "train_steps": 100, "train_runtime_min": 22.5}

=== grpo_cka_only_20_seed456 ===
  metrics: {"final_loss": 0.0999, "avg_train_loss": 0.0881, "final_reward": 0.2925, "final_kl": 0.0017, "train_steps": 100, "train_runtime_min": 21.8}

=== prune_eval_standard_30 ===
  metrics: {"accuracy": 2.8, "note": "N=500 partial result (killed by Director, 30% sparsity = complete collapse, N=500 precision sufficient)", "n_evaluated": 500, "n_total": 1319, "eos_rate": 1.2, "avg_len": 4057}

=== prune_eval_cka_only_30 ===
  metrics: {"accuracy": 1.6, "note": "N=500 partial result (killed by Director, 30% sparsity = complete collapse, N=500 precision sufficient)", "n_evaluated": 500, "n_total": 1319, "eos_rate": 5.6, "avg_len": 4009}

=== grpo_standard_20_seed456 ===
  metrics: {"steps_completed": 100, "runtime_sec": 2745, "peak_reward": 0.0844, "peak_reward_step": 90, "final_reward": 0.06, "final_frac_zero_std": 0.65, "seed": 456, "wandb_run": "wg0iv4oi", "wandb_mode": "offline"}

=== grpo_standard_20_seed123 ===
  metrics: {"steps_completed": 100, "runtime_sec": 2783, "peak_reward": 0.0619, "peak_reward_step": 80, "final_reward": 0.0594, "final_frac_zero_std": 0.6, "seed": 123, "wandb_run": "pgzwv725", "wandb_mode": "offline"}

=== grpo_cka_only_20_seed123 ===
  metrics: {"train_loss": 0.1361, "final_step_loss": 0.05054, "final_reward": 0.2975, "final_reward_std": 0.4097, "train_steps": 100, "train_runtime_hours": 11.63, "wandb_run": "j8kn0sqd"}

=== grpo_standard_20_fair ===
  metrics: {"wandb_run_id": "tyv20u2k", "total_steps": 100, "runtime_seconds": 3017, "reward_trajectory": [0.051, 0.056, 0.067, 0.081, 0.019, 0.043, 0.047, 0.046, 0.031, 0.054], "frac_zero_std_trajectory": [0.5, 0.625, 0.5, 0.5, 0.575, 0.55, 0.575, 0.55, 0.55, 0.55], "peak_reward": 0.081, "peak_reward_step": 40, "final_reward": 0.054, "final_frac_zero_std": 0.55, "dynamics_pattern": "dip_then_partial_recovery", "dip_step": 50, "dip_reward": 0.019}

=== sft_standard_20_retrain_westd ===
  metrics: {"train_loss": 0.758, "mean_token_accuracy": 0.8252, "train_runtime_sec": 1688, "train_samples_per_second": 8.856, "epochs": 2, "total_steps": 1870}

=== grpo_cka_only_20_extended_300 ===
  metrics: {"final_reward": 0.3075, "peak_reward": 0.4444, "peak_reward_step": 280, "reward_step100": 0.354, "reward_step300": 0.3075, "train_loss_final": 0.0349, "global_step": 300, "runtime_seconds": 23004, "gpu_hours": 6.5, "final_frac_zero_std": 0.275, "reward_range": [0.22, 0.44], "pattern": "sustained oscillation, no collapse", "wandb_run_id": "z9f0z901"}

=== grpo_cka_only_20_1p5b ===
  metrics: {"reward_mean": 0.2375, "frac_reward_zero_std": 0.175, "loss": 0.0595, "kl": 0.00215, "grad_norm": 1.445, "global_step": 100, "note": "training completed 100/100 but save_model failed (disk full). checkpoint-100 has complete model."}

=== grpo_standard_20_1p5b ===
  metrics: {"reward_mean": 0.0844, "frac_reward_zero_std": 0.15, "loss": 0.0151, "grad_norm": 4.03125, "kl": 0.0044, "entropy": 0.4617, "final_step": 100, "max_steps": 100, "total_time_min": 53}

=== grpo_standard_20_extended_300_v2 ===
  metrics: {"reward_mean_step300": 0.0562, "loss_step300": 0.0367, "frac_reward_zero_std_step300": 0.525, "kl_step300": 0.00306, "entropy_step300": 0.157, "lr_step300": 3.33e-09, "runtime_min": 48, "reward_decline_after_step260": true}

=== grpo_cka_only_20 ===
  metrics: {"final_step": 100, "final_reward": 0.3444, "peak_reward": 0.3544, "peak_reward_step": 50, "final_frac_zero_std": 0.2, "final_loss": 0.23, "final_kl": 0.001609, "final_entropy": 0.08751, "final_reward_std": 0.444, "runtime_seconds": 40710}

=== grpo_rasp_20_fair ===
  metrics: {"final_completion_length": 963.0, "final_frac_zero_std": 0.85, "final_reward": 0.01, "min_frac_zero_std": 0.675, "peak_reward": 0.061, "total_steps": 100, "training_time_minutes": 62.5, "trend": "stagnation_then_collapse"}

=== grpo_rasp_25 ===
  metrics: {"note": "Restored from previous_failure \u2014 cron false positive, experiment actually completed 100/100 steps successfully", "step_100": {"entropy": 0.04262, "frac_reward_zero_std": 0.875, "grad_norm": 0.05371, "kl": 0.0007035, "loss": 0.01275, "reward": 0.009375, "reward_std": 0.03149}, "wall_clock_min": 57.95, "wandb_run_id": "bc4ojqie"}

=== sft_cka_only_20 ===
  metrics: {"checkpoint_path": "/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20/", "note": "Initial loss 1.958 > RASP 1.86 > Standard 1.70 (CKA-only has most initial damage). Final loss 0.62 comparable to baselines. No greedy eval run yet.", "token_accuracy": 0.8362, "total_steps": 1870, "train_loss_final": 0.6165, "train_loss_initial": 1.958, "train_time_min": 33.4}

=== gradient_sft_v3 ===
  metrics: {"epochs": 2, "final_loss": 0.644, "output_path": "/root/autodl-tmp/recovery_aware_struct_prune/sft_gradient_20", "steps": 1870, "token_accuracy": 0.825}

=== sft_standard_25 ===
  metrics: {"model_keys": 339, "model_params": "5.79B", "note": "optimizer.pt save failed (RuntimeError) but model.safetensors intact", "runtime_seconds": 2130, "total_steps": 1870}

=== sft-alpha-1p0 ===
  metrics: {"post_prune_accuracy": 0.27, "token_accuracy": 0.83, "total_steps": 1870, "train_loss_final": 0.64, "train_time_min": 28}

=== grpo_rasp_rlvr_20_qwen_math ===
  metrics: {"clipped_ratio": 0.54, "comparison_vs_rasp_20": "RLVR reward 0.090 > RASP 0.061 (+48%), entropy 0.275 >> 0.073 (3.8x)", "comparison_vs_standard_20": "RLVR reward 0.090 >> Standard 0.044 (+105%)", "entropy_final": 0.275, "frac_zero_std_final": 0.7, "grad_norm_final": 16.125, "kl_final": 0.00581, "kl_spike_recovery": "immediate", "kl_spike_step70": 5756.85, "loss_final": 0.0793, "reward_final": 0.09, "reward_std_final": 0.234, "total_steps": 100, "wall_clock_min": 45.8, "wandb_run_id": "clzm2cy4"}

=== grpo_rasp_qwen_math_v3 ===
  metrics: {"clipped_ratio_final": 0.975, "clipped_ratio_mean": 0.981, "collapse_onset": "step1", "collapse_pattern": "entropy_length_collapse", "cross_model_match": "partial", "entropy_mean": 0.073, "entropy_vs_standard_ratio": 0.39, "frac_zero_std_final": 0.675, "frac_zero_std_max": 0.7, "frac_zero_std_min": 0.55, "kl_final": 0.009, "llama_pattern": "permanent_reward_collapse", "mean_completion_length": 1010, "recovery": false, "reward_final": 0.061, "reward_min": 0.048, "reward_peak": 0.102, "reward_std_final": 0.2, "total_steps": 100}

=== sft_qwen_math_standard_25 ===
  metrics: {"epochs": 2, "final_loss": 0.6122, "mean_token_accuracy": 0.8607, "throughput_samples_per_sec": 8.973, "total_steps": 1870, "train_runtime_sec": 1666}

=== sft_qwen_math_rasp_25 ===
  metrics: {"epochs": 2, "final_loss": 0.6062, "mean_token_accuracy": 0.8673, "throughput_samples_per_sec": 9.046, "total_steps": 1870, "train_runtime_sec": 1652}

=== grpo_unpruned_v2 ===
  metrics: {"avg_step_time_sec": 23, "checkpoints_available": ["checkpoint-90", "checkpoint-95", "checkpoint-100"], "collapse_onset": "N/A", "final_entropy": 0.194, "final_grad_norm": 6.97, "final_kl": 0.0051, "final_reward": 0.661, "max_steps": 100, "peak_reward": 0.669, "peak_reward_step": 80, "reward_range": "0.425-0.669", "training_seconds": 2660}

=== grpo_stage2_rasp_20_v9 ===
  metrics: {"checkpoints": ["checkpoint-10", "checkpoint-15", "checkpoint-20", "checkpoint-25", "checkpoint-30"], "collapse_note": "frac_zero_std peaked at 95% by step 30, reward dropped from peak 0.039 (step 20) to 0.021 (step 30)", "collapse_status": "COLLAPSED", "final_clipped_ratio": 0.956, "final_frac_zero_std": 0.95, "final_grad_norm": 1.398, "final_kl": 0.00118, "final_loss": 0.00686, "final_mean_length": 996, "final_mean_terminated_length": 176, "final_reward": 0.021, "max_steps": 30, "reward_history": [{"frac_zero_std": 0.875, "reward": 0.015, "step": 10}, {"frac_zero_std": 0.8, "reward": 0.039,

=== sft_unpruned_baseline ===
  metrics: {"epochs": 2, "final_loss": 0.3321, "final_token_accuracy": 0.909, "total_steps": 1870, "train_loss_avg": 0.4253, "train_runtime_sec": 1908, "train_samples_per_second": 7.833}

=== sft_standard_20_westd_retrain ===
  metrics: {"epochs": 2, "final_step_loss": 0.6403, "final_token_accuracy": 0.8258, "total_steps": 1870, "train_loss": 0.7577, "train_runtime_sec": 1679, "train_samples_per_second": 8.902}

=== sft_alpha2_0_westd ===
  metrics: {"epoch": 2, "mean_token_accuracy_final": 0.8354, "post_prune_accuracy": 0.29, "total_steps": 1870, "train_loss": 0.7424, "train_loss_final": 0.6114, "train_runtime_sec": 2422}

=== sft_standard_20 ===
  metrics: {"eos_rate_greedy_100": 0.99, "greedy_accuracy_100": 0.64, "greedy_avg_len": 176.31, "greedy_correct": 64, "greedy_max_len": 4096, "greedy_min_len": 43, "greedy_total": 100, "sampling_eos_rate_5": 1, "token_accuracy": 0.83, "total_steps": 1870, "train_loss_final": 0.64, "train_loss_initial": 1.7, "train_time_min": 37}

=== sft_rasp_20 ===
  metrics: {"eos_rate_greedy_100": 0.99, "greedy_accuracy_100": 0.57, "greedy_avg_len": 179.83, "greedy_correct": 57, "greedy_max_len": 4096, "greedy_min_len": 59, "greedy_total": 100, "sampling_eos_rate_5": 1, "token_accuracy": 0.83, "total_steps": 1870, "train_loss_final": 0.64, "train_loss_initial": 1.86, "train_time_min": 37}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "7322825a-1a98-4118-ad63-e38d875d170f"
}
```

</details>

---


### System

_source line 47_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2a92311f30a7bab6",
  "tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "description": "Running Search for decoupling and delta analysis experiments",
  "usage": {
    "total_tokens": 30427,
    "tool_uses": 9,
    "duration_ms": 65017
  },
  "last_tool_name": "Bash",
  "uuid": "767a3ac3-4a23-42e8-ba99-ccef4b4b7872",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db"
}
```

---


### Tool call

_source line 48_

<details open><summary>🔧 Tool call — Bash · `toolu_01JooBU2ShYqziRj4nTXjVjb`</summary>

```json
{
  "command": "FPATH=\"/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt\"\npython3 -c \"\nimport json\nFPATH='$FPATH'\nwith open(FPATH) as f:\n    raw = f.read()\nouter = json.loads(raw)\ndata = json.loads(outer['result'])\nexps = data['data']['experiments']\n\n# Look for decoupling analysis - fine-grained criteria\n# Terms: step_validity, format, correctness, justification etc.\n# Check all experiments with these types of metrics\ninteresting = []\nfor eid, e in exps.items():\n    m = e.get('metrics', {})\n    r = e.get('result', {})\n    combined = json.dumps(m) + json.dumps(r)\n    if any(k in combined.lower() for k in ['step_val', 'justif', 'decoupl', 'fine_grained', 'notation', 'conciseness', 'concise', 'efficiency']):\n        interesting.append(eid)\n        \nprint('Experiments with fine-grained criteria:', interesting)\nprint()\n\n# Also look for any experiment that contains delta or differential\nfor eid, e in exps.items():\n    m = e.get('metrics', {})\n    r = e.get('result', {})\n    h = e.get('hypothesis', '')\n    combined = json.dumps(m) + json.dumps(r) + h\n    if 'decoupl' in combined.lower() or 'delta' in combined.lower() or 'differential' in combined.lower():\n        print('=== ' + eid + ' (decoupl/delta) ===')\n        print('  hyp:', h[:200])\n        print('  metrics:', json.dumps(m)[:400])\n        print()\n\"\n",
  "description": "Search for decoupling and delta analysis experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "261b6ba1-ec70-42cc-8a78-dc4320b70c06",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01EAdtzPgAokRNBavVSRho6T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5267,
      "cache_read_input_tokens": 24873,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5267,
        "ephemeral_1h_input_tokens": 0
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

_source line 49 · 2026-05-24T04:34:16.723Z_

<details><summary>↩ Tool result · `toolu_01JooBU2ShYqziRj4nTXjVjb`</summary>

```text
Experiments with fine-grained criteria: []

=== eval_gsm8k_sft_depth_first_20 (decoupl/delta) ===
  hyp: MF5 depth-first SFT GSM8K eval. Establishes SFT baseline for depth-first pruning method, paired with GRPO eval to check C1 decoupling for this baseline method.
  metrics: {"accuracy_approx": 0.1, "note": "Early-stopped by Director at ~60-88 samples. Interim accuracy ~10%@50 (SFT). No JSON result file produced.", "early_stopped": true, "result_file_on_westb": false}

=== eval_gsm8k_grpo_random_20_seed123_v2 (decoupl/delta) ===
  hyp: MF2 seed123 v2 GSM8K eval (N=1319, greedy, max_new_tokens=2048). 配对 seed42 (50.57%) 和 seed456 (pending). 验证 C1 decoupling 跨 seed 鲁棒性。v1 因 batch_size=1 配置错误作废。
  metrics: {"accuracy": 0.5072, "n_correct": 669, "n_total": 1319, "stderr": 0.01377, "eos_rate": 0.9939, "avg_response_length": 177.9}

=== eval_math500_sft_qwen_math_cka_only_20 (decoupl/delta) ===
  hyp: Qwen2.5-Math-7B CKA-only 20% SFT MATH-500 eval @2048. Cross-architecture validation: if CKA-only criterion generalizes from DeepSeek-R1-Distill to Qwen-Math on MATH-500. SFT GSM8K = 51.5% (N=200). Pai
  metrics: {"accuracy": 0.216, "stderr": 0.0184, "correct": 108, "total": 500, "natural_eos": 90, "truncated": 410, "avg_response_length": 1745.338}

=== eval_math500_grpo_rasp_alpha0p5_20 (decoupl/delta) ===
  hyp: GRPO RASP α=0.5 MATH-500 eval @2048. C1 decoupling on MATH-500: SFT α=0.5 = 25.4%. GSM8K GRPO α=0.5 = 61.18%. Completes MATH-500 GRPO dose-response curve.
  metrics: {"accuracy": 0.248, "stderr": 0.0193, "correct": 124, "total": 500, "natural_eos": 274, "truncated": 226, "avg_response_length": 1110.462}

=== eval_math500_grpo_rasp_alpha3p0_20 (decoupl/delta) ===
  hyp: GRPO RASP α=3.0 MATH-500 eval @2048. C1 decoupling on MATH-500: SFT α=3.0 = 23.2%. GSM8K GRPO α=3.0 = 63.45%. Completes MATH-500 GRPO dose-response curve for α=3.0 data point.
  metrics: {"accuracy": 0.228, "correct": 114, "total": 500, "stderr": 0.0188, "truncated_ratio": 0.28, "avg_response_length": 745.038}

=== eval_math500_grpo_rasp_alpha4p0_20 (decoupl/delta) ===
  hyp: GRPO RASP α=4.0 MATH-500 eval @2048. C1 decoupling on MATH-500: SFT α=4.0 = 26.6%. If |GRPO - SFT| < 2pp, C1 decoupling holds cross-benchmark for α=4.0. GSM8K GRPO α=4.0 = 62.77%.
  metrics: {"accuracy": 0.262, "stderr": 0.01966, "correct": 131, "total": 500, "truncated": 180, "natural_eos": 320, "avg_response_length": 925.48}

=== eval_math500_grpo_rasp_alpha1p0_20 (decoupl/delta) ===
  hyp: GRPO RASP α=1.0 MATH-500 eval @2048. C1 decoupling on MATH-500: SFT α=1.0 = 21.2%. If |GRPO - SFT| < 2pp, C1 decoupling holds cross-benchmark for α=1.0.
  metrics: {"accuracy": 0.226, "stderr": 0.0187, "n_correct": 113, "n_total": 500, "avg_response_length": 903.536, "natural_eos": 320, "truncated": 180}

=== eval_math500_grpo_rasp_alpha2p0_20 (decoupl/delta) ===
  hyp: GRPO RASP α=2.0 MATH-500 eval @2048. C1 decoupling evidence on MATH-500: SFT α=2.0 = 24.0%, GRPO expected similar (~24%). If |GRPO - SFT| < 1pp, C1 decoupling holds cross-benchmark.
  metrics: {"accuracy": 0.262, "correct": 131, "total": 500, "stderr": 0.0197, "natural_eos": 349, "truncated": 151, "avg_response_length": 785.326}

=== eval_gsm8k_grpo_random_20_seed456 (decoupl/delta) ===
  hyp: MF2 seed456 GSM8K eval (N=1319, greedy, max_new_tokens=2048). Paired with seed42 (50.57%) and seed123 v2 (running, interim 52.40%@1000). Validates C1 decoupling robustness across random seeds.
  metrics: {"gsm8k_accuracy": 0.5087, "gsm8k_accuracy_se": 0.0138, "gsm8k_correct": 671, "gsm8k_total": 1319, "eos_rate": 0.9954, "avg_response_length": 163.5, "truncated": 6}

=== grpo_random_20_seed456 (decoupl/delta) ===
  hyp: MF2 multi-seed validation: Random pruning 20% GRPO with seed456. Third seed for C1 decoupling robustness check. seed42: Δ=-0.68pp, seed123: pending eval. If all seeds show |Δ(GRPO-SFT)| ≤ 2pp, C1 clai
  metrics: {}

=== grpo_random_20_seed123_v2 (decoupl/delta) ===
  hyp: MF2 multi-seed validation v2: Random 20% GRPO with seed123, correct batch_size=2 (matching seed42/seed456). v1 used batch_size=1 (half data per 100 steps), results invalidated. Tests C1 decoupling rob
  metrics: {}

=== eval_gsm8k_sft_alpha3p0_20 (decoupl/delta) ===
  hyp: α=3.0 SFT GSM8K eval (checkpoint-935, 1 epoch). Dose-response 5th SFT data point for C1 decoupling. Paired with α=3.0 GRPO (pending). Completes the 5-point dose-response SFT column.
  metrics: {"gsm8k_accuracy": 0.6414, "gsm8k_correct": 846, "gsm8k_total": 1319, "gsm8k_stderr": 0.0132, "eos_rate": 0.9879, "avg_response_length": 188.63, "natural_eos": 1303, "truncated": 16}

=== grpo_random_20_seed123 (decoupl/delta) ===
  hyp: MF2 multi-seed validation: Random pruning 20% GRPO with seed123. Tests if GRPO decoupling result (C1) is robust across random seeds. If variance across seeds is low (±2pp), C1 claim is strengthened.
  metrics: {}

=== eval_gsm8k_sft_alpha2p0_20 (decoupl/delta) ===
  hyp: α=2.0 SFT GSM8K eval for C1 decoupling. Paired with α=2.0 GRPO (66.11%). Critical: if SFT ~61-62%, Δ ≈ +4-5pp would break C1 universal ±2pp claim. Reviewer-flagged risk.
  metrics: {"gsm8k_accuracy": 0.6497, "gsm8k_correct": 857, "gsm8k_total": 1319}

=== eval_gsm8k_sft_alpha0p5_20 (decoupl/delta) ===
  hyp: α=0.5 SFT GSM8K eval for C1 decoupling. Paired with α=0.5 GRPO (61.18%). Δ(GRPO-SFT) tests whether GRPO benefit is universal ±2pp across α values.
  metrics: {"gsm8k_accuracy": 0.6073, "gsm8k_correct": 801, "gsm8k_total": 1319}

=== eval_gsm8k_sft_alpha4_20_v5 (decoupl/delta) ===
  hyp: α=4.0 SFT GSM8K N=1319 full eval @2048. D100 critical for C1 decoupling universality. v4 lost to westd-29022 outage. Re-run on westd-32935.
  metrics: {"gsm8k_accuracy": 0.6194, "correct": 817, "total": 1319, "stderr": 0.0134, "eos_rate": 0.981, "avg_response_length": 197.85}

=== eval_math500_sft_standard_25 (decoupl/delta) ===
  hyp: Standard 25% SFT model MATH-500 accuracy establishes pre-GRPO baseline for standard pruning at 25% sparsity, enabling SFT→GRPO recovery delta on MATH-500
  metrics: {"math500_accuracy": 0.14, "correct": 70, "n_total": 500, "natural_eos": 185, "truncated": 315, "avg_response_length": 1367.82, "v1_accuracy": 0.13, "v1_correct": 65}

=== eval_gsm8k_sft_standard_25 (decoupl/delta) ===
  hyp: Standard 25% SFT GSM8K accuracy establishes pre-GRPO floor for importance-based pruning at 25% sparsity, enabling SFT→GRPO recovery delta comparison with CKA-only 25%
  metrics: {"gsm8k_accuracy": 0.5087, "stderr": 0.0138, "correct": 671, "n_total": 1319, "eos_rate": 0.953, "avg_response_length": 333.15}

=== eval_gsm8k_sft_cka_only_25 (decoupl/delta) ===
  hyp: CKA-only 25% SFT model retains higher GSM8K accuracy than GRPO-recovered model's SFT baseline, establishing the pre-GRPO accuracy floor for measuring recovery delta at 25% sparsity
  metrics: {"gsm8k_accuracy": 0.6012, "correct": 793, "n_total": 1319, "stderr": 0.0135, "eos_rate": 0.9803, "avg_response_length": 243.6}

=== eval_gsm8k_sft_random_20 (decoupl/delta) ===
  hyp: Random 20% SFT model GSM8K accuracy establishes the pre-GRPO floor for random pruning, enabling SFT→GRPO recovery delta comparison across pruning methods at 20% sparsity
  metrics: {"gsm8k_accuracy": 0.5125, "correct": 676, "n_total": 1319, "stderr": 0.0138, "eos_rate": 0.9932, "avg_response_length": 182.4}

=== eval_gsm8k_sft_standard_20 (decoupl/delta) ===
  hyp: GSM8K N=1319 eval on Standard 20% SFT checkpoint (pre-GRPO). Direct measurement of SFT baseline for Standard 20% — needed for paper Table 2 exact GRPO delta calculation.
  metrics: {"gsm8k_accuracy": 0.5921, "stderr": 0.0135, "correct": 781, "total": 1319, "eos_rate": 0.9848, "avg_response_length": 206.68}

=== eval_gsm8k_sft_cka_only_20 (decoupl/delta) ===
  hyp: GSM8K N=1319 eval on CKA-only 20% SFT checkpoint (pre-GRPO). Direct measurement of SFT baseline for 20% sparsity — needed for paper table to calculate exact GRPO delta. Current estimate ~63.91% from r
  metrics: {"gsm8k_accuracy": 0.6391, "gsm8k_accuracy_ci": 0.0132, "correct": 843, "total": 1319, "eos_rate": 0.9901, "avg_response_length": 198.1, "truncated": 13}

=== eval_gsm8k_sft_standard_15 (decoupl/delta) ===
  hyp: GSM8K N=1319 eval on Standard 15% SFT checkpoint (pre-GRPO). Establishes SFT baseline accuracy for Standard 15% sparsity. Paired with eval_gsm8k_grpo_standard_15_v2 to measure GRPO recovery delta. Com
  metrics: {"gsm8k_accuracy": 0.6649, "correct": 877, "total": 1319, "eos_rate": 0.993, "avg_response_length": 183}

=== eval_math500_grpo_cka_only_20_2048 (decoupl/delta) ===
  hyp: GRPO CKA-only 20% MATH-500 accuracy with explicit max_new_tokens=2048. Re-eval for fair C1 OOD comparison: previous eval (26.6%) did not specify max_new_tokens. SFT CKA-only @2048 = 29.0%. If GRPO < S
  metrics: {"accuracy": 0.292, "n_correct": 146, "n_total": 500}

=== eval_gsm8k_sft_standard_20_1p5b (decoupl/delta) ===
  hyp: 1.5B Standard post-SFT GSM8K accuracy (N=1319). SFT baseline for computing GRPO delta on Standard pruning at 1.5B scale. Compare with GRPO Standard 1.5B (22.29%) to quantify GRPO benefit. Completes 3-
  metrics: {"accuracy": 0.22896133434420016, "n_correct": 302, "n_total": 1319}

=== eval_gsm8k_sft_rasp_20_1p5b (decoupl/delta) ===
  hyp: 1.5B RASP post-SFT GSM8K accuracy (N=1319). SFT baseline for computing GRPO delta on RASP pruning at 1.5B. Compare with GRPO RASP 1.5B (26.16%).
  metrics: {"accuracy": 0.2691, "n_correct": 355, "n_total": 1319, "stderr": 0.0122, "grpo_delta_pp": -0.75}

=== eval_math500_grpo_standard_20_fair_v2 (decoupl/delta) ===
  hyp: Standard 20% post-GRPO (fair v5) MATH-500 accuracy with max_new_tokens=2048. Restart of slow original. Interim Acc@100=36%. Cross-benchmark validation for C1 decoupling claim.
  metrics: {"accuracy": 0.264, "n_correct": 132, "n_total": 500, "stderr": 0.0197}

=== eval_math500_sft_rasp_20_2048 (decoupl/delta) ===
  hyp: SFT RASP 20% MATH-500 accuracy with max_new_tokens=2048. Fair comparison with GRPO RASP @2048 (24.0%) for C1 decoupling on MATH-500. SFT recovery should show lower reasoning capability than GRPO recov
  metrics: {"accuracy": 0.226, "n_correct": 113, "n_total": 500, "stderr": 0.0187, "natural_eos": 314, "truncated": 186, "natural_eos_pct": 0.628, "avg_response_length": 930.58, "median_response_length": 274}

=== eval_math500_grpo_rasp_20_fair (decoupl/delta) ===
  hyp: GRPO RASP 20% pruned model on MATH-500 with max_new_tokens=2048. Fair comparison for C1 decoupling: GRPO recovery on RASP-pruned model should show different accuracy profile compared to SFT recovery, 
  metrics: {"accuracy": 0.24, "n_correct": 120, "n_total": 500, "stderr": 0.0191, "natural_eos_pct": 0.64, "truncated_pct": 0.36, "avg_response_length": 903.5, "median_response_length": 272, "max_new_tokens": 2048}

=== eval_gsm8k_sft_cka_only_20_1p5b (decoupl/delta) ===
  hyp: 1.5B CKA-only post-SFT GSM8K accuracy (N=1319). SFT baseline for computing GRPO delta: if GRPO CKA-only 1.5B GSM8K > SFT CKA-only 1.5B GSM8K, GRPO adds value beyond SFT recovery on 1.5B scale. Complet
  metrics: {"accuracy": 0.3563, "n_correct": 470, "n_total": 1319, "stderr": 0.0132, "eos_rate": 0.9507, "avg_response_length": 336.76}

=== eval_math500_sft_cka_only_20_v4_restart (decoupl/delta) ===
  hyp: CKA-only 20% post-SFT MATH-500 accuracy (restart of v4 which had cuda:2 conflict). Full 500 samples, max_new_tokens=2048. Core C1 evidence for decoupling claim.
  metrics: {"accuracy": 0.29, "n_correct": 145, "n_total": 500, "stderr": 0.0203, "natural_eos": 384, "truncated": 116, "natural_eos_pct": 0.768, "avg_response_length": 673.278, "median_response_length": 242.5}

=== eval_humaneval_sft_rasp_20 (decoupl/delta) ===
  hyp: If SFT (without GRPO) already produces ~10% HumanEval pass@1 on pruned model, then GRPO adds no HumanEval increment, confirming C1 decoupling (reward improves but code generation ability comes from SF
  metrics: {"correct": 12, "failure_modes": "model outputs natural language thinking instead of code (SyntaxError), parenthesis mismatch", "median_response_length": 512, "note": "max_tokens truncation frequent", "pass_at_1": 0.0732, "stderr": 0.0203, "total": 164}

=== eval_grpo_unpruned_v2_step100 (decoupl/delta) ===
  hyp: Unpruned model GRPO step-100 achieves >80% GSM8K accuracy, proving reward-accuracy coupling holds without structural damage and decoupling is pruning-specific (C1 control)
  metrics: {"accuracy": 81.27, "avg_response_length": 209, "correct": 1072, "eos_rate": 99.7, "seed": 42, "total": 1319}

=== eval_grpo_rasp_20_qwen_math (decoupl/delta) ===
  hyp: RASP 20% pruned Qwen Math post-GRPO shows accuracy plateau despite reward improvement, confirming C1 decoupling occurs regardless of pruning method on second model
  metrics: {"accuracy": 0.725, "n_samples": 200, "seed": 42}

=== eval_grpo_standard_20_qwen_math (decoupl/delta) ===
  hyp: Standard 20% pruned Qwen Math post-GRPO shows accuracy plateau below unpruned despite reward improvement, confirming reward-accuracy decoupling is cross-model (C1)
  metrics: {"accuracy": 0.705, "n_samples": 200, "seed": 42}

=== eval_grpo_rasp_25_qwen_math (decoupl/delta) ===
  hyp: RASP 25% pruned Qwen Math post-GRPO shows reward-accuracy decoupling on GSM8K, confirming C1 generalizes to higher sparsity on second model family
  metrics: {"accuracy": 0.625, "n_samples": 200, "seed": 42}

=== eval_grpo_standard_25_qwen_math (decoupl/delta) ===
  hyp: Standard 25% pruned Qwen Math post-GRPO exhibits reward-accuracy decoupling on GSM8K, confirming C1 generalizes across sparsity levels on second model family
  metrics: {"accuracy": 0.635, "n_samples": 200, "seed": 42}

=== eval_grpo_rasp_rlvr_20_qwen_math (decoupl/delta) ===
  hyp: Qwen2.5-Math-7B RASP-RLVR 20% post-GRPO GSM8K eval (N=200, greedy, seed=42). GRPO reward=0.090(最高)，验证 accuracy 是否也改善或依然 decoupling (C1)。对比 pre-GRPO: 73%. Parent: grpo_rasp_rlvr_20_qwen_math.
  metrics: {"accuracy": 0.71, "mode": "greedy", "n_samples": 200, "seed": 42}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "5ae260c3-7af7-4b02-aea5-1d5722df9609"
}
```

</details>

---


### System

_source line 50_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2a92311f30a7bab6",
  "tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "description": "Running Extract dose-response alpha experiments for GRPO and SFT",
  "usage": {
    "total_tokens": 37019,
    "tool_uses": 10,
    "duration_ms": 79168
  },
  "last_tool_name": "Bash",
  "uuid": "ea3442c8-3bcb-4e5d-b871-5932cc6b8e39",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db"
}
```

---


### Tool call

_source line 51_

<details open><summary>🔧 Tool call — Bash · `toolu_014eZsxn6JJqieC2jyj41bto`</summary>

```json
{
  "command": "FPATH=\"/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt\"\npython3 -c \"\nimport json\nFPATH='$FPATH'\nwith open(FPATH) as f:\n    raw = f.read()\nouter = json.loads(raw)\ndata = json.loads(outer['result'])\nexps = data['data']['experiments']\n\n# Get all experiments about dose-response alpha values - both GRPO and SFT - for GSM8K\n# For decoupling: compare GRPO vs SFT accuracy at each alpha\nalpha_exps = {\n    'alpha0p5_GRPO': 'eval_gsm8k_grpo_alpha0p5_20',\n    'alpha0p5_SFT': 'eval_gsm8k_sft_alpha0p5_20',\n    'alpha1p0_GRPO': None,  \n    'alpha1p0_SFT': None,\n    'alpha2p0_GRPO': 'eval_gsm8k_grpo_alpha2p0_20',\n    'alpha2p0_SFT': 'eval_gsm8k_sft_alpha2p0_20',\n    'alpha3p0_GRPO': 'eval_gsm8k_grpo_alpha3p0_20',\n    'alpha3p0_SFT': 'eval_gsm8k_sft_alpha3p0_20',\n    'alpha4p0_GRPO': 'eval_gsm8k_grpo_alpha4_20_v3',\n    'alpha4p0_SFT': 'eval_gsm8k_sft_alpha4_20_v5',\n}\n\n# Also check for alpha1p0 \nfor eid in exps.keys():\n    if 'alpha1' in eid and ('gsm8k' in eid or 'sft' in eid or 'grpo' in eid):\n        print('Found alpha1 exp:', eid)\n        m = exps[eid].get('metrics', {})\n        print('  metrics:', m)\n\nprint()\nprint('=== Dose-response data ===')\nfor name, eid in alpha_exps.items():\n    if eid and eid in exps:\n        m = exps[eid].get('metrics', {})\n        acc = m.get('gsm8k_accuracy', m.get('accuracy', 'N/A'))\n        print(f'{name}: acc={acc} (exp={eid})')\n    elif eid:\n        print(f'{name}: exp {eid} NOT FOUND')\n    else:\n        print(f'{name}: no exp ID provided')\n\"\n",
  "description": "Extract dose-response alpha experiments for GRPO and SFT"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "ce493912-f42e-4d66-9ca7-4124cf7a61ed",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01LMg6T7Q5V7UBsz1eJgATLM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6559,
      "cache_read_input_tokens": 30140,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6559,
        "ephemeral_1h_input_tokens": 0
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

_source line 52 · 2026-05-24T04:34:30.905Z_

<details><summary>↩ Tool result · `toolu_014eZsxn6JJqieC2jyj41bto`</summary>

```text
Found alpha1 exp: eval_math500_grpo_rasp_alpha1p0_20_fixed
  metrics: {'accuracy': 0.23, 'n_correct': 115, 'n_total': 500, 'stderr': 0.0188, 'natural_eos': 320, 'truncated': 180, 'avg_response_length': 903.536}
Found alpha1 exp: eval_math500_sft_rasp_alpha1p0_20_fixed
  metrics: {'accuracy': 0.216, 'num_correct': 108, 'num_total': 500}
Found alpha1 exp: eval_math500_grpo_rasp_alpha1p0_20
  metrics: {'accuracy': 0.226, 'stderr': 0.0187, 'n_correct': 113, 'n_total': 500, 'avg_response_length': 903.536, 'natural_eos': 320, 'truncated': 180}
Found alpha1 exp: eval_math500_sft_rasp_alpha1p0_20_v2
  metrics: {'accuracy': 0.212, 'correct': 106, 'total': 500, 'truncated': 186, 'stderr': 0.0183}

=== Dose-response data ===
alpha0p5_GRPO: acc=0.6118 (exp=eval_gsm8k_grpo_alpha0p5_20)
alpha0p5_SFT: acc=0.6073 (exp=eval_gsm8k_sft_alpha0p5_20)
alpha1p0_GRPO: no exp ID provided
alpha1p0_SFT: no exp ID provided
alpha2p0_GRPO: acc=0.6611 (exp=eval_gsm8k_grpo_alpha2p0_20)
alpha2p0_SFT: acc=0.6497 (exp=eval_gsm8k_sft_alpha2p0_20)
alpha3p0_GRPO: acc=0.6345 (exp=eval_gsm8k_grpo_alpha3p0_20)
alpha3p0_SFT: acc=0.6414 (exp=eval_gsm8k_sft_alpha3p0_20)
alpha4p0_GRPO: acc=0.6277 (exp=eval_gsm8k_grpo_alpha4_20_v3)
alpha4p0_SFT: acc=0.6194 (exp=eval_gsm8k_sft_alpha4_20_v5)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "efafa953-e502-4f6a-bdd8-a47c68b5909d"
}
```

</details>

---


### System

_source line 53_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2a92311f30a7bab6",
  "tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "description": "Running Check for alpha=1.0 GSM8K experiments",
  "usage": {
    "total_tokens": 38544,
    "tool_uses": 11,
    "duration_ms": 90316
  },
  "last_tool_name": "Bash",
  "uuid": "b27b65a0-7b72-4469-b8c3-310ce23be2bd",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db"
}
```

---


### Tool call

_source line 54_

<details open><summary>🔧 Tool call — Bash · `toolu_01Q7R4GJqP3qcAtPWbq6iQjj`</summary>

```json
{
  "command": "FPATH=\"/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt\"\npython3 -c \"\nimport json\nFPATH='$FPATH'\nwith open(FPATH) as f:\n    raw = f.read()\nouter = json.loads(raw)\ndata = json.loads(outer['result'])\nexps = data['data']['experiments']\n\n# alpha1p0 for GSM8K\nfor eid in exps.keys():\n    if '1p0' in eid and 'gsm8k' in eid:\n        print(eid, exps[eid].get('metrics',{}))\n\n# Check eval-sft-alpha-0p0 and eval-sft-alpha-1p0\nfor eid in ['eval-sft-alpha-0p0', 'eval-sft-alpha-1p0', 'sft-alpha-1p0']:\n    if eid in exps:\n        print(eid, exps[eid].get('metrics',{}))\n        print('  hyp:', exps[eid].get('hypothesis','')[:200])\n\"\n",
  "description": "Check for alpha=1.0 GSM8K experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "fdc4cc29-e82a-4ec2-a98b-8a9cef677c71",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RxzfWYdWYkSG9KEwLA4LDX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1492,
      "cache_read_input_tokens": 36699,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1492,
        "ephemeral_1h_input_tokens": 0
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

_source line 55 · 2026-05-24T04:34:42.071Z_

<details><summary>↩ Tool result · `toolu_01Q7R4GJqP3qcAtPWbq6iQjj`</summary>

```text
eval-sft-alpha-0p0 {'accuracy': 0.64, 'avg_len': 257.9, 'eos_rate': 0.97, 'n_correct': 64, 'n_total': 100}
  hyp: Alpha=0.0 (no CKA, pure magnitude) post-SFT matches Standard pruning recovery (~64%), establishing that removing CKA collapses RASP to standard behavior (C2 ablation endpoint)
eval-sft-alpha-1p0 {'accuracy': 0.57, 'avg_len': 224.18, 'eos_rate': 0.98, 'n_correct': 57, 'n_total': 100, 'natural_eos': 98, 'stderr': 0.0495, 'truncated': 2}
  hyp: Alpha=1.0 (full CKA weight) post-SFT accuracy matches RASP default (~57%), confirming alpha=1.0 produces identical pruning structure to standard RASP (C2 ablation endpoint)
sft-alpha-1p0 {'post_prune_accuracy': 0.27, 'token_accuracy': 0.83, 'total_steps': 1870, 'train_loss_final': 0.64, 'train_time_min': 28}
  hyp: SFT on alpha=1.0 pruned model (full CKA weight) recovers to level matching RASP default because alpha=1.0 IS the standard RASP scoring function (C2 ablation consistency)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "aacbd1dc-cf27-46b6-b4f0-eada53e35e0c"
}
```

</details>

---


### System

_source line 56_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2a92311f30a7bab6",
  "tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "description": "Running Check alpha_ablation_sweep experiment details",
  "usage": {
    "total_tokens": 39437,
    "tool_uses": 12,
    "duration_ms": 95276
  },
  "last_tool_name": "Bash",
  "uuid": "b23a4cc9-ec7a-40cc-8537-aa13d73f168e",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db"
}
```

---


### Tool call

_source line 57_

<details open><summary>🔧 Tool call — Bash · `toolu_01BtSHa8GCzQ8DEfhYeZdeZc`</summary>

```json
{
  "command": "FPATH=\"/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt\"\npython3 -c \"\nimport json\nFPATH='$FPATH'\nwith open(FPATH) as f:\n    raw = f.read()\nouter = json.loads(raw)\ndata = json.loads(outer['result'])\nexps = data['data']['experiments']\n\n# Now look for alpha_ablation_sweep which probably contains fine-grained data\ne = exps.get('alpha_ablation_sweep', {})\nprint('=== alpha_ablation_sweep ===')\nprint('status:', e.get('status'))\nprint('hypothesis:', e.get('hypothesis','')[:400])\nprint('result:', json.dumps(e.get('result',{}))[:1500])\nprint('metrics:', json.dumps(e.get('metrics',{}))[:1500])\n\"\n",
  "description": "Check alpha_ablation_sweep experiment details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "94906ccd-0abd-4f25-9f63-d9f7b443ae22",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_018FEkhHTHQRXcq9VEAWB1Mp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 830,
      "cache_read_input_tokens": 38191,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 830,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 63,
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

_source line 58 · 2026-05-24T04:34:47.010Z_

<details><summary>↩ Tool result · `toolu_01BtSHa8GCzQ8DEfhYeZdeZc`</summary>

```text
=== alpha_ablation_sweep ===
status: DONE
hypothesis: plan_015 (Claim 2): α sensitivity ablation on westb (cal=512). Sweep α∈{0, 0.25, 0.5, 1, 2} at 20% sparsity. RASP scoring S(h)=I(h)×(1-F(h))^α. Each α: prune + post-prune GSM8K N=100 eval. Tests whether CKA weight α systematically affects post-prune reasoning retention. Prior westd (cal=256) results: α=0.0→30%, α=0.5→25%, α=1.0→27%, α=4.0→40% (non-monotonic). westb cal=512 may show different patte
result: {}
metrics: {"alpha_0.0": {"accuracy": 0.27, "avg_len": 1192, "eos_rate": 0.8, "n_correct": 27, "n_total": 100}, "alpha_0.25": {"accuracy": 0.23, "avg_len": 1834, "eos_rate": 0.63, "n_correct": 23, "n_total": 100}, "alpha_0.5": {"accuracy": 0.22, "avg_len": 1141, "eos_rate": 0.81, "n_correct": 22, "n_total": 100}, "alpha_1.0": {"accuracy": 0.31, "avg_len": 733, "eos_rate": 0.92, "n_correct": 31, "n_total": 100}, "alpha_2.0": {"accuracy": 0.36, "avg_len": 2130, "eos_rate": 0.59, "n_correct": 36, "n_total": 100}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "f63a470c-fc53-4edd-9e07-f00cb82e9bcb"
}
```

</details>

---


### System

_source line 59_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2a92311f30a7bab6",
  "tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "description": "Running Check GRPO standard and CKA-only 20% accuracy values",
  "usage": {
    "total_tokens": 40325,
    "tool_uses": 13,
    "duration_ms": 106402
  },
  "last_tool_name": "Bash",
  "uuid": "febe3e6f-120a-4cd2-aacf-5af6a4c24737",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db"
}
```

---


### Tool call

_source line 60_

<details open><summary>🔧 Tool call — Bash · `toolu_0151Dn6BkSEhArbnA1RUNDBL`</summary>

```json
{
  "command": "FPATH=\"/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt\"\npython3 -c \"\nimport json\nFPATH='$FPATH'\nwith open(FPATH) as f:\n    raw = f.read()\nouter = json.loads(raw)\ndata = json.loads(outer['result'])\nexps = data['data']['experiments']\n\n# Now let's look at 'tab:decoupling' related experiments - fine-grained criteria\n# The paper claims 4 fine-grained criteria. Let me look at what Table decoupling shows.\n# Perhaps this is the SFT-only gap of 4.62 pp in Table tab:decoupling\n# Check Standard 20% SFT vs Standard 20% GRPO, and CKA-only 20% SFT vs GRPO\n\n# Standard 20%: SFT=59.21% GRPO=?\n# CKA-only 20%: SFT=63.91% GRPO=?\n\n# Let's find GRPO standard 20% (fair)\nkey_ids = [\n    'eval_gsm8k_grpo_standard_20_fair_v2',\n    'eval_gsm8k_grpo_standard_20_fair',  \n    'eval_gsm8k_grpo_standard_20_seed123',\n    'eval_gsm8k_grpo_standard_20_seed456',\n    'eval_gsm8k_grpo_standard_20_seed123_full',\n    'eval_gsm8k_grpo_standard_20_seed456_full',\n    'eval_gsm8k_grpo_cka_only_20_v2',\n    'eval_gsm8k_grpo_cka_only_20_verify',\n    'eval_gsm8k_grpo_cka_only_20_seed123',\n    'eval_gsm8k_grpo_cka_only_20_seed456_full',\n    'eval_gsm8k_grpo_cka_only_20_1p5b',\n]\nfor eid in key_ids:\n    if eid in exps:\n        e = exps[eid]\n        m = e.get('metrics', {})\n        acc = m.get('gsm8k_accuracy', m.get('accuracy', 'N/A'))\n        print(f'{eid}: acc={acc}')\n        print(f'  hyp: {e.get(\\\"hypothesis\\\",\\\"\\\")[:200]}')\n        print(f'  metrics: {json.dumps(m)[:300]}')\n        print()\n\"\n",
  "description": "Check GRPO standard and CKA-only 20% accuracy values"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "382f17fe-ec98-4374-878b-cd4e2e994176",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01T62DZjDwENPCr9i1dCBEKS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 829,
      "cache_read_input_tokens": 39021,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 829,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 59,
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

_source line 61 · 2026-05-24T04:34:58.219Z_

<details><summary>↩ Tool result · `toolu_0151Dn6BkSEhArbnA1RUNDBL`</summary>

```text
eval_gsm8k_grpo_standard_20_fair_v2: acc=59.44
  hyp: 验证 Standard GRPO fair (v5 config: beta=0.01, temp=0.4, maxlen=1024, DAPO, lr=1e-6) 的 GSM8K 准确率。替换 phantom 58.91% (从未被实际验证过的数字)。使用 grpo_stage2_standard_20_fair checkpoint, N=1319。
  metrics: {"accuracy": 59.44, "n_correct": 784, "n_total": 1319}

eval_gsm8k_grpo_standard_20_seed123: acc=0.64
  hyp: GSM8K N=200 quick eval on Standard GRPO seed=123 model. Seed=42 accuracy: 59.44% (N=1319). If seed=123 within ±5pp of seed=42, confirms Standard stagnation pattern produces consistent accuracy across 
  metrics: {"accuracy": 0.64, "n_correct": 128, "n_total": 200, "stderr": 0.0339, "eos_rate": 0.99, "avg_response_length": 187.9}

eval_gsm8k_grpo_standard_20_seed456: acc=0.665
  hyp: GSM8K N=200 quick eval on Standard GRPO seed=456 model. Seed=42 accuracy: 59.44% (N=1319), seed=123 being evaluated. If seed=456 within ±5pp of seed=42, confirms Standard recovery capacity is not seed
  metrics: {"accuracy": 0.665, "n_correct": 133, "n_total": 200, "stderr": 0.0334, "eos_rate": 0.995, "avg_response_length": 166.9}

eval_gsm8k_grpo_standard_20_seed123_full: acc=0.5989
  hyp: GSM8K N=1319 full eval on Standard GRPO seed=123. N=200 quick eval showed 64.00% (128/200). Seed=42 full eval: 59.44% (784/1319). Full eval to determine if seed123's higher accuracy holds or is small-
  metrics: {"accuracy": 0.5989, "n_correct": 790, "n_total": 1319, "stderr": 0.0135, "eos_rate": null}

eval_gsm8k_grpo_standard_20_seed456_full: acc=0.602
  hyp: GSM8K N=1319 full eval on Standard GRPO seed=456. N=200 quick eval showed 66.50% (133/200), exceeding CKA-only's 64.37%. Seed=42 full eval: 59.44% (784/1319). Full eval to determine if seed456's high 
  metrics: {"accuracy": 0.602, "n_correct": 794, "n_total": 1319, "stderr": 0.01348, "eos_rate": 0.9856}

eval_gsm8k_grpo_cka_only_20_v2: acc=0.6437
  hyp: CKA-only GRPO GSM8K accuracy (v2, on westb). Tab2 critical data point: if CKA-only GRPO > SFT (63.91%), GRPO genuinely helps CKA-only recovery. Re-run after westd outage killed v1.
  metrics: {"accuracy": 0.6437, "n_correct": 849, "n_total": 1319, "stderr": 0.0132, "eos_rate": 0.9886, "avg_response_length": 203.43, "truncated": 15, "wall_time_sec": 8921}

eval_gsm8k_grpo_cka_only_20_verify: acc=0.6406
  hyp: Reproducibility verification of core result: CKA-only 20% GRPO GSM8K accuracy=64.39%. Independent rerun on westb (different server from original westd) to confirm the key number used in Tab 1 and Tab 
  metrics: {"accuracy": 0.6406, "n_correct": 845, "n_total": 1319, "stderr": 0.0132, "eos_rate": 0.9894, "avg_response_length": 201.76, "original_accuracy": 0.6437, "accuracy_diff_pp": -0.31}

eval_gsm8k_grpo_cka_only_20_seed123: acc=0.6422
  hyp: GSM8K eval on GRPO CKA-only 20% seed123 checkpoint. Tests reproducibility of CKA-only GRPO GSM8K performance (original seed42 = 64.37%). If seed123 matches closely, confirms CKA-only GRPO advantage is
  metrics: {"accuracy": 0.6422, "stderr": 0.0132, "n_correct": 847, "n_total": 1319, "eos_rate": 0.9909, "avg_response_length": 195.97, "natural_eos": 1307, "truncated": 12}

eval_gsm8k_grpo_cka_only_20_seed456_full: acc=0.6459
  hyp: GSM8K N=1319 full eval on CKA-only GRPO seed=456. Training complete: loss=0.0999, reward=0.2925. Seed=42: 64.37%, seed=123: 64.22%. If seed=456 matches, confirms CKA-only GRPO recovery is consistent a
  metrics: {"gsm8k_accuracy": 0.6459, "gsm8k_accuracy_ci": 0.0132, "correct": 852, "total": 1319, "eos_rate": 0.9886, "avg_response_length": 204.3}

eval_gsm8k_grpo_cka_only_20_1p5b: acc=0.3548
  hyp: 1.5B CKA-only post-GRPO GSM8K accuracy (N=1319). Cross-model generalization: 7B CKA-only GRPO achieved 64.37% GSM8K. If 1.5B CKA-only GRPO also leads among pruning methods, confirms scale-invariant re
  metrics: {"accuracy": 0.3548, "n_correct": 468, "n_total": 1319, "stderr": 0.0132}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "fda9e6d2-6650-4459-8251-6647ffb53a98"
}
```

</details>

---


### System

_source line 62_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2a92311f30a7bab6",
  "tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "description": "Running Check MBPP and shortgpt experiments",
  "usage": {
    "total_tokens": 42827,
    "tool_uses": 14,
    "duration_ms": 119236
  },
  "last_tool_name": "Bash",
  "uuid": "3d753e7c-71db-46e4-9854-855889258f94",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db"
}
```

---


### Tool call

_source line 63_

<details open><summary>🔧 Tool call — Bash · `toolu_0175FhtYqx6xoJ39wPtBheaT`</summary>

```json
{
  "command": "FPATH=\"/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt\"\npython3 -c \"\nimport json\nFPATH='$FPATH'\nwith open(FPATH) as f:\n    raw = f.read()\nouter = json.loads(raw)\ndata = json.loads(outer['result'])\nexps = data['data']['experiments']\n\n# The paper claims 4 fine-grained criteria with mean |Delta(GRPO-SFT)| = 0.54 pp\n# and max = 0.61 pp at 20% sparsity on GSM8K\n# These are likely from a special evaluation with multiple criteria\n# Let me search for anything with multiple sub-scores\n\n# Also check MBPP and ShortGPT\nmbpp_ids = ['eval_mbpp_grpo_standard_20_v4', 'eval_mbpp_grpo_standard_20_v3', \n            'eval_mbpp_sft_standard_20_v4', 'eval_mbpp_grpo_cka_only_20', \n            'eval_mbpp_sft_cka_only_20', 'eval_mbpp_grpo_rasp_20', 'eval_mbpp_sft_rasp_20',\n            'eval_mbpp_grpo_shortgpt_20_v2', 'eval_mbpp_sft_shortgpt_20_v2',\n            'eval_mbpp_dense_unpruned']\n\nfor eid in mbpp_ids:\n    if eid in exps:\n        e = exps[eid]\n        m = e.get('metrics', {})\n        print(f'{eid}: {json.dumps(m)[:400]}')\n        print(f'  hyp: {e.get(\\\"hypothesis\\\",\\\"\\\")[:200]}')\n        print()\n\"\n",
  "description": "Check MBPP and shortgpt experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "9a4058be-3b62-48ac-a21f-8437b9cec75b",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0141sMcAZ2uKjbt8EuXk22S1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2468,
      "cache_read_input_tokens": 39850,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2468,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 34,
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

_source line 64 · 2026-05-24T04:35:10.937Z_

<details><summary>↩ Tool result · `toolu_0175FhtYqx6xoJ39wPtBheaT`</summary>

```text
eval_mbpp_grpo_standard_20_v4: {"pass_at_1": 0.131, "n_correct": 49, "n_total": 374, "stderr": 0.01745, "avg_response_length": 1058.7, "median_response_length": 726}
  hyp: GRPO Standard 20% pruned model should achieve ~13% pass@1 on MBPP, consistent with prior v1 partial results at 335/374 tasks

eval_mbpp_grpo_standard_20_v3: {"pass_at_1": 0.131, "correct": 49, "total": 374, "stderr": 0.0174}
  hyp: 

eval_mbpp_sft_standard_20_v4: {"pass_at_1": 0.1203, "stderr": 0.0168, "n_correct": 45, "n_total": 374, "avg_response_length": 1084.1, "median_response_length": 746.5}
  hyp: MBPP pass@1 eval on SFT Standard 20% @2048. Dense baseline=53.48%. 此为手动 tmux 提交的 orphan 进程补录。目前 85/374 (23%), interim pass@1=0.175。HF_DATASETS_OFFLINE=1。关联 C2。

eval_mbpp_grpo_cka_only_20: {"pass_at_1": 0.1417, "n_correct": 53, "n_total": 374, "stderr": 0.018}
  hyp: MBPP pass@1 eval on GRPO CKA-only 20% model @2048. Dense baseline=53.48% (200/374). CKA-only GRPO showed strongest recovery on GSM8K (64.37%) and HumanEval (20.12%). If MBPP follows same pattern (CKA-

eval_mbpp_sft_cka_only_20: {"pass_at_1": 0.1283, "stderr": 0.0173, "n_correct": 48, "n_total": 374, "dense_baseline_pass_at_1": 0.5348, "degradation_pct": 76.01, "avg_response_length": 643.8, "median_response_length": 363.5}
  hyp: MBPP pass@1 eval on SFT CKA-only 20% model. Dense baseline=53.48% (200/374). CKA-only preserves most code generation capability after pruning. Compare SFT vs GRPO on MBPP to test redistribution hypoth

eval_mbpp_grpo_rasp_20: {"pass_at_1": 0.131, "n_correct": 49, "n_total": 374, "stderr": 0.0174}
  hyp: MBPP pass@1 eval on GRPO RASP 20% model @2048. Dense baseline=53.48% (200/374). RASP GRPO GSM8K=60.88%, HumanEval=10.37%. Tests RASP GRPO code generation on MBPP. Completes MBPP 3×2 matrix. Expected: 

eval_mbpp_sft_rasp_20: {"pass_at_1": 0.1176, "stderr": 0.0167, "n_correct": 44, "n_total": 374, "dense_baseline_pass_at_1": 0.5348, "degradation_pct": 78.01, "avg_response_length": 810.7, "median_response_length": 247}
  hyp: SFT RASP 20% model retains more MBPP code generation capability than CKA-only pruning due to recovery-aware pruning preserving structurally important parameters

eval_mbpp_grpo_shortgpt_20_v2: {"pass_at_1": 0.1444, "stderr": 0.0182, "n_correct": 54, "n_total": 374, "avg_response_length": 1140.8, "median_response_length": 804.5}
  hyp: Retry of eval_mbpp_grpo_shortgpt_20 which failed with EXIT_CODE=127 (missing conda activation). GRPO ShortGPT 20% MBPP pass@1 @2048. ShortGPT GSM8K: SFT=44.73%, GRPO=43.37% (GRPO退化). Depth pruning 在 M

eval_mbpp_sft_shortgpt_20_v2: {"pass_at_1": 0.1043, "stderr": 0.0158, "n_correct": 39, "n_total": 374, "avg_response_length": 1166.4, "median_response_length": 773.5}
  hyp: Retry of eval_mbpp_sft_shortgpt_20 which failed with EXIT_CODE=127 (command not found — missing conda activation). ShortGPT SFT 20% MBPP pass@1 @2048. ShortGPT GSM8K SFT=44.73%, GRPO=43.37%. Depth pru

eval_mbpp_dense_unpruned: {"pass_at_1": 0.5348, "stderr": 0.0258, "n_correct": 200, "n_total": 374}
  hyp: Dense unpruned DeepSeek-R1-Distill-Qwen-7B MBPP pass@1 baseline @2048. Establishes ceiling performance for MBPP code generation. All pruned models' MBPP results will be compared against this baseline.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "d08f8a1b-c927-4715-8243-1106122d46d5"
}
```

</details>

---


### System

_source line 65_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2a92311f30a7bab6",
  "tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "description": "Running Check ShortGPT GSM8K experiments",
  "usage": {
    "total_tokens": 44904,
    "tool_uses": 15,
    "duration_ms": 133085
  },
  "last_tool_name": "Bash",
  "uuid": "457e40ed-c0e2-4ee1-9832-f4ccb140e358",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db"
}
```

---


### Tool call

_source line 66_

<details open><summary>🔧 Tool call — Bash · `toolu_01NcvoSXmUKQqciU874fgAN8`</summary>

```json
{
  "command": "FPATH=\"/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt\"\npython3 -c \"\nimport json\nFPATH='$FPATH'\nwith open(FPATH) as f:\n    raw = f.read()\nouter = json.loads(raw)\ndata = json.loads(outer['result'])\nexps = data['data']['experiments']\n\n# ShortGPT experiments\nshortgpt_ids = [\n    'eval_gsm8k_grpo_shortgpt_20',\n    'eval_gsm8k_sft_shortgpt_20',\n]\nfor eid in shortgpt_ids:\n    if eid in exps:\n        e = exps[eid]\n        m = e.get('metrics', {})\n        print(f'{eid}: {json.dumps(m)}')\n        print(f'  hyp: {e.get(\\\"hypothesis\\\",\\\"\\\")[:300]}')\n        print()\n\n# Also look at all experiments that mention ShortGPT in hypothesis\nfor eid, e in exps.items():\n    h = e.get('hypothesis', '')\n    if 'shortgpt' in h.lower() or 'shortgpt' in eid.lower():\n        m = e.get('metrics', {})\n        acc = m.get('gsm8k_accuracy', m.get('accuracy', None))\n        if acc is not None:\n            print(f'ShortGPT related: {eid}: acc={acc}')\n\"\n",
  "description": "Check ShortGPT GSM8K experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "817fb92e-da8e-4f02-b283-19e2de9f3cf9",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Vep2cTMG3v8TubGzEKQAGQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2044,
      "cache_read_input_tokens": 42318,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2044,
        "ephemeral_1h_input_tokens": 0
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

_source line 67 · 2026-05-24T04:35:24.784Z_

<details><summary>↩ Tool result · `toolu_01NcvoSXmUKQqciU874fgAN8`</summary>

```text
eval_gsm8k_grpo_shortgpt_20: {"gsm8k_accuracy": 43.37, "n_correct": 572, "n_total": 1319, "stderr": 0.0136}
  hyp: GSM8K eval on ShortGPT GRPO checkpoint-100. ShortGPT SFT=44.73%, if GRPO improves significantly it suggests depth-pruned models can still benefit from RL. If minimal improvement or collapse, confirms coarse layer removal limits GRPO recovery capacity vs fine-grained methods (CKA-only 64.37%, Standar

eval_gsm8k_sft_shortgpt_20: {"gsm8k_accuracy": 44.73, "n_correct": 590, "n_total": 1319}
  hyp: ShortGPT SFT checkpoint GSM8K eval. After depth pruning (5/28 layers removed by Block Influence scoring) + SFT warmup (loss=0.62, token_accuracy=0.83), measure GSM8K accuracy. Compare with fine-grained pruning SFT results: CKA-only SFT ~60%, Standard SFT ~64%. ShortGPT expected lower due to coarse l

ShortGPT related: eval_gsm8k_grpo_shortgpt_20: acc=43.37
ShortGPT related: eval_gsm8k_sft_shortgpt_20: acc=44.73
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "4686a5f6-e423-4ab9-a12f-104897d5e74d"
}
```

</details>

---


### System

_source line 68_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2a92311f30a7bab6",
  "tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "description": "Running Check HumanEval scores across methods",
  "usage": {
    "total_tokens": 45867,
    "tool_uses": 16,
    "duration_ms": 141727
  },
  "last_tool_name": "Bash",
  "uuid": "26420f39-10a9-4303-9e94-f971d494d7c0",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db"
}
```

---


### Tool call

_source line 69_

<details open><summary>🔧 Tool call — Bash · `toolu_01A2vtbjm9MSM9P6dJ3jds4Q`</summary>

```json
{
  "command": "FPATH=\"/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt\"\npython3 -c \"\nimport json\nFPATH='$FPATH'\nwith open(FPATH) as f:\n    raw = f.read()\nouter = json.loads(raw)\ndata = json.loads(outer['result'])\nexps = data['data']['experiments']\n\n# Claims 2-4: Fine-grained criteria differentials\n# Paper claims mean |Delta(GRPO-SFT)| = 0.54 pp across four criteria at 20% sparsity on GSM8K\n# I don't see fine-grained criteria in the registry - let me look for any pass_k, HumanEval, MBPP combinations\n# Maybe the 4 criteria are: GSM8K + HumanEval + MBPP + MATH-500 (3 benchmarks are visible)\n# But paper says 'four fine-grained criteria' specifically\n\n# Let me check what HumanEval scores look like\nhumaneval_ids = [\n    'eval_humaneval_grpo_standard_20_2048',\n    'eval_humaneval_sft_standard_20_2048_v2',\n    'eval_humaneval_grpo_cka_only_20_2048',\n    'eval_humaneval_sft_cka_only_20_2048_v2',\n    'eval_humaneval_grpo_rasp_20_2048',\n    'eval_humaneval_sft_rasp_20_2048',\n    'eval_humaneval_unpruned',\n    'eval_humaneval_unpruned_2048',\n]\n\nfor eid in humaneval_ids:\n    if eid in exps:\n        e = exps[eid]\n        m = e.get('metrics', {})\n        print(f'{eid}: {json.dumps(m)[:300]}')\n        print(f'  hyp: {e.get(\\\"hypothesis\\\",\\\"\\\")[:200]}')\n        print()\n\"\n",
  "description": "Check HumanEval scores across methods"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "dc819224-eac1-4a22-8dbf-191013a63886",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_011G5MTZAhoRoQm1nRh4ZrSb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 899,
      "cache_read_input_tokens": 44362,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 899,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 64,
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

_source line 70 · 2026-05-24T04:35:33.425Z_

<details><summary>↩ Tool result · `toolu_01A2vtbjm9MSM9P6dJ3jds4Q`</summary>

```text
eval_humaneval_grpo_standard_20_2048: {"avg_response_length": 1843, "correct": 17, "max_new_tokens": 2048, "median_response_length": 2048, "pass_at_1": 0.1037, "total": 164}
  hyp: HumanEval pass@1 for GRPO Standard 20% with max_new_tokens=2048. 512-token results invalidated due to truncation artifact (RASP shorter outputs biased). Part of complete 4-way HumanEval@2048 compariso

eval_humaneval_sft_standard_20_2048_v2: {"avg_response_length": 1850.7, "correct": 19, "max_new_tokens": 2048, "median_response_length": 2048, "pass_at_1": 0.1159, "total": 164}
  hyp: HumanEval pass@1 for SFT Standard 20% with max_new_tokens=2048. Completes 5-way HumanEval@2048 matrix. Compares SFT Standard vs SFT RASP (10.37%) code generation after recovery.

eval_humaneval_grpo_cka_only_20_2048: {"pass_at_1": 0.2012, "n_correct": 33, "n_total": 164, "stderr": 0.0313, "avg_response_length": 1523.31, "median_response_length": 2048, "wall_clock_seconds": 11933}
  hyp: GRPO recovery training on CKA-only 20% pruned model recovers code generation ability on HumanEval from SFT baseline of 0% pass@1, because CKA-only preserves structural similarity that GRPO can exploit

eval_humaneval_sft_cka_only_20_2048_v2: {"pass_at_1": 20.12, "n_correct": 33, "n_total": 164}
  hyp: SFT CKA-only HumanEval v2 (PATH bug 修复版重跑)，验证 v1 的 0% 是否为假结果。v1 因 eval_humaneval.py 用裸 python 导致 164 题全部 sandbox 失败。修复后用 sys.executable 重跑。

eval_humaneval_grpo_rasp_20_2048: {"correct": 24, "max_new_tokens": 2048, "pass_at_1": 0.1463, "stderr": 0.0276, "total": 164}
  hyp: HumanEval pass@1 for GRPO RASP 20% with max_new_tokens=2048. Completes 4-way HumanEval@2048 matrix. If GRPO RASP > GRPO Standard on code generation, reinforces C3 (RASP preserves transferable structur

eval_humaneval_sft_rasp_20_2048: {"correct": 17, "max_new_tokens": 2048, "median_response_length": 2048, "note": "still truncating at median=2048, main failure mode is thinking chain leaking into code output", "pass_at_1": 0.1037, "stderr": 0.0238, "total": 164, "wall_time_min": 42}
  hyp: HumanEval pass@1 for SFT RASP 20% with max_new_tokens=2048 (previous run used 512 which truncated thinking chain). Tests whether longer generation improves code quality for pruned+recovered model.

eval_humaneval_unpruned: {"n_passed": 3, "n_total": 164, "pass_at_1": 0.0183, "stderr": 0.0105}
  hyp: HumanEval baseline: unpruned DeepSeek-R1-Distill-Qwen-7B pass@1 on HumanEval (164 problems). Establishes dense model ceiling for code generation capability comparison.

eval_humaneval_unpruned_2048: {"avg_response_length": 1771, "correct": 74, "max_new_tokens": 2048, "median_response_length": 2048, "pass_at_1": 0.4512, "stderr": 0.0389, "total": 164, "wall_time_min": 67.6}
  hyp: HumanEval pass@1 for unpruned DeepSeek-R1-Distill-Qwen-7B with max_new_tokens=2048 (previous run used 512 which truncated thinking chain). Establishes dense model ceiling for code generation compariso
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "eb2c322a-53b9-4803-b419-c0e4f45f924e"
}
```

</details>

---


### System

_source line 71_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2a92311f30a7bab6",
  "tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "description": "Running Check gradient flow analysis experiments",
  "usage": {
    "total_tokens": 47745,
    "tool_uses": 17,
    "duration_ms": 154575
  },
  "last_tool_name": "Bash",
  "uuid": "1e67dc92-5f3d-421d-b4e2-3ad797b92b5b",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db"
}
```

---


### Tool call

_source line 72_

<details open><summary>🔧 Tool call — Bash · `toolu_01AWXYRizvVrrdztHENZDGh8`</summary>

```json
{
  "command": "FPATH=\"/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt\"\npython3 -c \"\nimport json\nFPATH='$FPATH'\nwith open(FPATH) as f:\n    raw = f.read()\nouter = json.loads(raw)\ndata = json.loads(outer['result'])\nexps = data['data']['experiments']\n\n# Check gradient flow experiments for claims #5 (peak reward ratio 4.4x) and #11 (gradient magnitude ratio 2.89x)\n# and CKA similarity claims (#9, #10)\nfor eid in ['gradient_flow_analysis', 'gradient_flow_v3', 'gradient_sft_v3']:\n    if eid in exps:\n        e = exps[eid]\n        print(f'=== {eid} ===')\n        print(f'  status: {e.get(\\\"status\\\")}')\n        print(f'  hyp: {e.get(\\\"hypothesis\\\",\\\"\\\")[:400]}')\n        m = e.get('metrics', {})\n        r = e.get('result', {})\n        print(f'  metrics: {json.dumps(m)[:1500]}')\n        print(f'  result: {json.dumps(r)[:500]}')\n        print()\n\"\n",
  "description": "Check gradient flow analysis experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "03f547f0-06a0-48e1-98bf-eea595bd85e1",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01S3M5BagfdEdEK665t2zabP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1845,
      "cache_read_input_tokens": 45261,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1845,
        "ephemeral_1h_input_tokens": 0
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

_source line 73 · 2026-05-24T04:35:46.280Z_

<details><summary>↩ Tool result · `toolu_01AWXYRizvVrrdztHENZDGh8`</summary>

```text
=== gradient_flow_analysis ===
  status: DONE
  hyp: CKA-only pruned models exhibit stronger gradient flow (higher per-layer gradient norms) compared to Standard pruned models, enabling more effective GRPO recovery. Standard pruning creates weaker gradient signals that limit training effectiveness.
  metrics: {"cka_only_attn_grad_mean": 0.3135, "cka_only_attn_grad_cv": 1.2231, "cka_only_mlp_grad_mean": 0.285, "cka_only_mlp_grad_cv": 1.2424, "standard_attn_grad_mean": 0.1316, "standard_attn_grad_cv": 1.1363, "standard_mlp_grad_mean": 0.1222, "standard_mlp_grad_cv": 1.1489, "grad_magnitude_ratio_attn": 2.38, "grad_magnitude_ratio_mlp": 2.33}
  result: {}

=== gradient_flow_v3 ===
  status: DONE
  hyp: CKA-only pruned models exhibit significantly stronger gradient signals (per-layer L2 norm) compared to Standard and RASP, with statistical significance (Wilcoxon p<0.05). This gradient magnitude difference is consistent with CKA-only's superior GRPO recovery capacity.
  metrics: {"cka_only_mean_grad_norm": 0.3229, "standard_mean_grad_norm": 0.1118, "rasp_mean_grad_norm": 0.1431, "cka_vs_standard_ratio": 2.89, "rasp_vs_standard_ratio": 1.28, "cka_vs_standard_significant_layers": "55/56", "cka_vs_rasp_significant_layers": "56/56", "rasp_vs_standard_significant_layers": "45/56", "rasp_vs_standard_nonsig_layers": "layer_18_mlp,layer_19_attn,layer_19_mlp,layer_20_attn,layer_20_mlp,layer_21_attn,layer_21_mlp,layer_22_attn,layer_24_mlp,layer_27_attn,layer_27_mlp", "n_samples": 200, "statistical_test": "Wilcoxon signed-rank, per-layer", "bootstrap_n": 1000, "seed": 42}
  result: {}

=== gradient_sft_v3 ===
  status: DONE
  hyp: SFT recovery on gradient-pruned model (25.5% post-prune acc). If SFT recovers gradient to ~50-60%, gradient scoring is viable but weaker than CKA-aware. If recovery fails or minimal, gradient scoring causes irreversible damage similar to magnitude.
  metrics: {"epochs": 2, "final_loss": 0.644, "output_path": "/root/autodl-tmp/recovery_aware_struct_prune/sft_gradient_20", "steps": 1870, "token_accuracy": 0.825}
  result: {}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "b265e62e-f7d8-4422-a03f-5eb50a7f0f8c"
}
```

</details>

---


### System

_source line 74_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2a92311f30a7bab6",
  "tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "description": "Running Check CKA stability and gradient post-SFT experiments",
  "usage": {
    "total_tokens": 49131,
    "tool_uses": 18,
    "duration_ms": 164613
  },
  "last_tool_name": "Bash",
  "uuid": "5dc145e9-327e-4395-9d45-cf95f1b0709c",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db"
}
```

---


### Tool call

_source line 75_

<details open><summary>🔧 Tool call — Bash · `toolu_01UNTNGYCRgZGj5DPNdJwUen`</summary>

```json
{
  "command": "FPATH=\"/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt\"\npython3 -c \"\nimport json\nFPATH='$FPATH'\nwith open(FPATH) as f:\n    raw = f.read()\nouter = json.loads(raw)\ndata = json.loads(outer['result'])\nexps = data['data']['experiments']\n\n# Check CKA calibration/scoring experiments for CKA similarity claims (#9, #10)\nfor eid in ['cka_calibration_stability_ablation', 'cka_scoring_stability_ablation']:\n    if eid in exps:\n        e = exps[eid]\n        print(f'=== {eid} ===')\n        print(f'  status: {e.get(\\\"status\\\")}')\n        print(f'  hyp: {e.get(\\\"hypothesis\\\",\\\"\\\")[:400]}')\n        m = e.get('metrics', {})\n        print(f'  metrics: {json.dumps(m)[:2000]}')\n        print()\n\n# Check eval_gradient_postsft\ne = exps.get('eval_gradient_postsft', {})\nprint('=== eval_gradient_postsft ===')\nprint('  metrics:', json.dumps(e.get('metrics',{}))[:800])\nprint('  hyp:', e.get('hypothesis','')[:300])\n\"\n",
  "description": "Check CKA stability and gradient post-SFT experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "aef1d62a-152d-4a23-8b60-2f828ac8d201",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01DdUwAzW6Qx3r9N59B1PRTY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1353,
      "cache_read_input_tokens": 47106,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1353,
        "ephemeral_1h_input_tokens": 0
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

_source line 76 · 2026-05-24T04:35:56.308Z_

<details><summary>↩ Tool result · `toolu_01UNTNGYCRgZGj5DPNdJwUen`</summary>

```text
=== cka_calibration_stability_ablation ===
  status: DONE
  hyp: CKA-based functional overlap scores F(h) are stable across calibration sizes (256/512/1024 samples), with Spearman rho > 0.95 between any two sizes. This validates that our pruning criterion is not sensitive to calibration hyperparameter.
  metrics: {"split_half_rho": 0.9932, "n_splits": 5, "size_sensitivity_128": 0.982, "size_sensitivity_256": 0.989, "size_sensitivity_512": 0.995}

=== cka_scoring_stability_ablation ===
  status: DONE
  hyp: CKA scoring stability across calibration sizes (256/512/1024). If Spearman ρ > 0.95 between all pairs, CKA scoring is robust to calibration size — directly answers reviewer concern about scoring sensitivity. Plan_014, C2 mechanism evidence.
  metrics: {"spearman_256v512_attn": 0.989, "spearman_256v512_mlp": 0.9683, "spearman_256v512_combined": 0.9788, "spearman_256v1024_attn": 0.9762, "spearman_256v1024_mlp": 0.9464, "spearman_256v1024_combined": 0.9641, "spearman_512v1024_attn": 0.995, "spearman_512v1024_mlp": 0.9908, "spearman_512v1024_combined": 0.9938, "min_combined_rho": 0.964, "mean_combined_rho": 0.979, "stable": true}

=== eval_gradient_postsft ===
  metrics: {"accuracy": 0.615, "avg_response_length": 167.455, "correct": 123, "eos_rate": 0.995, "stderr": 0.0344, "total": 200}
  hyp: GSM8K accuracy after SFT recovery on gradient-pruned model. Pre-SFT was 25.5%. If post-SFT reaches ~50-60%, gradient scoring is viable but weaker than RASP (~61%). If much lower, gradient scoring causes partially irreversible damage.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "f28def08-54fa-4dca-b16a-03884cb59159"
}
```

</details>

---


### System

_source line 77_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2a92311f30a7bab6",
  "tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "description": "Running Check GRPO training reward ratios and frac_zero_std",
  "usage": {
    "total_tokens": 50254,
    "tool_uses": 19,
    "duration_ms": 177988
  },
  "last_tool_name": "Bash",
  "uuid": "6bcc8fb8-00c1-48df-82be-958241ada2d7",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db"
}
```

---


### Tool call

_source line 78_

<details open><summary>🔧 Tool call — Bash · `toolu_01Qmkbpc9ZwD9CGtGVxAzuMK`</summary>

```json
{
  "command": "FPATH=\"/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt\"\npython3 -c \"\nimport json\nFPATH='$FPATH'\nwith open(FPATH) as f:\n    raw = f.read()\nouter = json.loads(raw)\ndata = json.loads(outer['result'])\nexps = data['data']['experiments']\n\n# Look for CKA similarity mu values (0.62 for CKA-only, >=0.88 for collapsing)\n# and reward ratio 4.4x (CKA-only vs Standard under GRPO)\n# and f_0 (zero-variance batch fraction)\n\n# Check the grpo training experiments for reward trajectories and frac_zero_std\n# CKA-only: grpo_cka_only_20 - reward = 0.3444\n# Standard: what's the peak reward? \n# From grpo_standard_20_fair: peak_reward = 0.081\n\n# Ratio = 0.3444 / 0.081 = 4.25 (close to 4.4x)\n# Or using grpo_cka_only_20_extended_300 peak=0.4444 vs standard peak=0.081 = 5.49x\n\n# Let me check all grpo training experiment rewards\ngrpo_trains = [\n    'grpo_cka_only_20',\n    'grpo_standard_20_fair',\n    'grpo_standard_20_seed123',\n    'grpo_standard_20_seed456',\n]\nfor eid in grpo_trains:\n    if eid in exps:\n        e = exps[eid]\n        m = e.get('metrics', {})\n        print(f'{eid}: {json.dumps(m)[:500]}')\n        print()\n\n# Also check frac_zero_std across all experiments\nprint('\\\\n=== frac_zero_std values ===')\nfor eid, e in exps.items():\n    m = e.get('metrics', {})\n    mstr = json.dumps(m)\n    if 'frac_zero_std' in mstr or 'frac_reward_zero' in mstr:\n        import re\n        vals = re.findall(r'frac[_a-z]*zero[_a-z]*[\\\":]\\\\s*([0-9.]+)', mstr)\n        if vals:\n            print(f'{eid}: frac_zero_std values = {vals}')\n\"\n",
  "description": "Check GRPO training reward ratios and frac_zero_std"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "dfcac774-e4a0-430f-8972-1ebae534d887",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01U1hjcxKGswcL1aZEvNYJtn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1087,
      "cache_read_input_tokens": 48459,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1087,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
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

_source line 79 · 2026-05-24T04:36:09.735Z_

<details><summary>↩ Tool result · `toolu_01Qmkbpc9ZwD9CGtGVxAzuMK`</summary>

```text
grpo_cka_only_20: {"final_step": 100, "final_reward": 0.3444, "peak_reward": 0.3544, "peak_reward_step": 50, "final_frac_zero_std": 0.2, "final_loss": 0.23, "final_kl": 0.001609, "final_entropy": 0.08751, "final_reward_std": 0.444, "runtime_seconds": 40710}

grpo_standard_20_fair: {"wandb_run_id": "tyv20u2k", "total_steps": 100, "runtime_seconds": 3017, "reward_trajectory": [0.051, 0.056, 0.067, 0.081, 0.019, 0.043, 0.047, 0.046, 0.031, 0.054], "frac_zero_std_trajectory": [0.5, 0.625, 0.5, 0.5, 0.575, 0.55, 0.575, 0.55, 0.55, 0.55], "peak_reward": 0.081, "peak_reward_step": 40, "final_reward": 0.054, "final_frac_zero_std": 0.55, "dynamics_pattern": "dip_then_partial_recovery", "dip_step": 50, "dip_reward": 0.019}

grpo_standard_20_seed123: {"steps_completed": 100, "runtime_sec": 2783, "peak_reward": 0.0619, "peak_reward_step": 80, "final_reward": 0.0594, "final_frac_zero_std": 0.6, "seed": 123, "wandb_run": "pgzwv725", "wandb_mode": "offline"}

grpo_standard_20_seed456: {"steps_completed": 100, "runtime_sec": 2745, "peak_reward": 0.0844, "peak_reward_step": 90, "final_reward": 0.06, "final_frac_zero_std": 0.65, "seed": 456, "wandb_run": "wg0iv4oi", "wandb_mode": "offline"}


=== frac_zero_std values ===
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "b049f45d-3742-4503-8e62-1375acd3404e"
}
```

</details>

---


### System

_source line 80_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2a92311f30a7bab6",
  "tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "description": "Running Find all frac_zero_std/zero_var metrics in registry",
  "usage": {
    "total_tokens": 51647,
    "tool_uses": 20,
    "duration_ms": 186245
  },
  "last_tool_name": "Bash",
  "uuid": "096e3156-9c87-4564-9b21-c2700d29cc29",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db"
}
```

---


### Tool call

_source line 81_

<details open><summary>🔧 Tool call — Bash · `toolu_019UQeJojGjr4k5qKCJ9eP6t`</summary>

```json
{
  "command": "FPATH=\"/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt\"\npython3 -c \"\nimport json, re\nFPATH='$FPATH'\nwith open(FPATH) as f:\n    raw = f.read()\nouter = json.loads(raw)\ndata = json.loads(outer['result'])\nexps = data['data']['experiments']\n\n# Search for frac_zero_std and reward ratios in all experiment data\nprint('=== All frac_zero_std values found ===')\nfor eid, e in exps.items():\n    m = e.get('metrics', {})\n    mstr = json.dumps(m)\n    if 'zero_std' in mstr.lower() or 'zero_var' in mstr.lower():\n        print(f'{eid}: relevant metrics = {mstr[:600]}')\n        print()\n\"\n",
  "description": "Find all frac_zero_std/zero_var metrics in registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "2be51576-b606-4344-9d20-884cb7007f0c",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01SGCGEXYYycmX9EPKCUHTbu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1360,
      "cache_read_input_tokens": 49546,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1360,
        "ephemeral_1h_input_tokens": 0
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

_source line 82 · 2026-05-24T04:36:17.945Z_

<details><summary>↩ Tool result · `toolu_019UQeJojGjr4k5qKCJ9eP6t`</summary>

```text
=== All frac_zero_std values found ===
grpo_random_20_retrain_v2: relevant metrics = {"final_reward": 0.2875, "final_reward_std": 0.4291, "final_loss": 0.06684, "final_kl": 0.004236, "final_entropy": 0.1704, "final_completion_length_mean": 189.1, "final_grad_norm": 5.531, "frac_reward_zero_std": 0.4, "wandb_run_id": "9c16hnf7", "wandb_run_name": "grpo_sft_random_20", "training_steps": 100, "training_time_hours": 3.07}

grpo_random_20: relevant metrics = {"reward_mean": 0.164, "reward_range": [0.14, 0.19], "reward_peak": 0.19, "reward_peak_step": 70, "frac_zero_std_mean": 0.333, "frac_zero_std_range": [0.3, 0.4], "entropy_mean": 0.221, "entropy_range": [0.2, 0.24], "kl_mean": 0.0045, "steps_captured": 9, "max_step": 90, "pattern": "stable plateau, no collapse", "data_source": "log_file (W&B crashed before sync)"}

grpo_standard_20_seed456: relevant metrics = {"steps_completed": 100, "runtime_sec": 2745, "peak_reward": 0.0844, "peak_reward_step": 90, "final_reward": 0.06, "final_frac_zero_std": 0.65, "seed": 456, "wandb_run": "wg0iv4oi", "wandb_mode": "offline"}

grpo_standard_20_seed123: relevant metrics = {"steps_completed": 100, "runtime_sec": 2783, "peak_reward": 0.0619, "peak_reward_step": 80, "final_reward": 0.0594, "final_frac_zero_std": 0.6, "seed": 123, "wandb_run": "pgzwv725", "wandb_mode": "offline"}

grpo_standard_20_fair: relevant metrics = {"wandb_run_id": "tyv20u2k", "total_steps": 100, "runtime_seconds": 3017, "reward_trajectory": [0.051, 0.056, 0.067, 0.081, 0.019, 0.043, 0.047, 0.046, 0.031, 0.054], "frac_zero_std_trajectory": [0.5, 0.625, 0.5, 0.5, 0.575, 0.55, 0.575, 0.55, 0.55, 0.55], "peak_reward": 0.081, "peak_reward_step": 40, "final_reward": 0.054, "final_frac_zero_std": 0.55, "dynamics_pattern": "dip_then_partial_recovery", "dip_step": 50, "dip_reward": 0.019}

grpo_cka_only_20_extended_300: relevant metrics = {"final_reward": 0.3075, "peak_reward": 0.4444, "peak_reward_step": 280, "reward_step100": 0.354, "reward_step300": 0.3075, "train_loss_final": 0.0349, "global_step": 300, "runtime_seconds": 23004, "gpu_hours": 6.5, "final_frac_zero_std": 0.275, "reward_range": [0.22, 0.44], "pattern": "sustained oscillation, no collapse", "wandb_run_id": "z9f0z901"}

grpo_rasp_20_1p5b: relevant metrics = {"final_reward": 0.099, "frac_zero_std": 0.175, "clipped_ratio": 0.82}

grpo_cka_only_20_1p5b: relevant metrics = {"reward_mean": 0.2375, "frac_reward_zero_std": 0.175, "loss": 0.0595, "kl": 0.00215, "grad_norm": 1.445, "global_step": 100, "note": "training completed 100/100 but save_model failed (disk full). checkpoint-100 has complete model."}

grpo_standard_20_1p5b: relevant metrics = {"reward_mean": 0.0844, "frac_reward_zero_std": 0.15, "loss": 0.0151, "grad_norm": 4.03125, "kl": 0.0044, "entropy": 0.4617, "final_step": 100, "max_steps": 100, "total_time_min": 53}

grpo_standard_20_extended_300_v2: relevant metrics = {"reward_mean_step300": 0.0562, "loss_step300": 0.0367, "frac_reward_zero_std_step300": 0.525, "kl_step300": 0.00306, "entropy_step300": 0.157, "lr_step300": 3.33e-09, "runtime_min": 48, "reward_decline_after_step260": true}

grpo_cka_only_20: relevant metrics = {"final_step": 100, "final_reward": 0.3444, "peak_reward": 0.3544, "peak_reward_step": 50, "final_frac_zero_std": 0.2, "final_loss": 0.23, "final_kl": 0.001609, "final_entropy": 0.08751, "final_reward_std": 0.444, "runtime_seconds": 40710}

grpo_rasp_20_fair: relevant metrics = {"final_completion_length": 963.0, "final_frac_zero_std": 0.85, "final_reward": 0.01, "min_frac_zero_std": 0.675, "peak_reward": 0.061, "total_steps": 100, "training_time_minutes": 62.5, "trend": "stagnation_then_collapse"}

grpo_rasp_25: relevant metrics = {"note": "Restored from previous_failure \u2014 cron false positive, experiment actually completed 100/100 steps successfully", "step_100": {"entropy": 0.04262, "frac_reward_zero_std": 0.875, "grad_norm": 0.05371, "kl": 0.0007035, "loss": 0.01275, "reward": 0.009375, "reward_std": 0.03149}, "wall_clock_min": 57.95, "wandb_run_id": "bc4ojqie"}

grpo_rasp_rlvr_20_qwen_math: relevant metrics = {"clipped_ratio": 0.54, "comparison_vs_rasp_20": "RLVR reward 0.090 > RASP 0.061 (+48%), entropy 0.275 >> 0.073 (3.8x)", "comparison_vs_standard_20": "RLVR reward 0.090 >> Standard 0.044 (+105%)", "entropy_final": 0.275, "frac_zero_std_final": 0.7, "grad_norm_final": 16.125, "kl_final": 0.00581, "kl_spike_recovery": "immediate", "kl_spike_step70": 5756.85, "loss_final": 0.0793, "reward_final": 0.09, "reward_std_final": 0.234, "total_steps": 100, "wall_clock_min": 45.8, "wandb_run_id": "clzm2cy4"}

grpo_rasp_qwen_math_v3: relevant metrics = {"clipped_ratio_final": 0.975, "clipped_ratio_mean": 0.981, "collapse_onset": "step1", "collapse_pattern": "entropy_length_collapse", "cross_model_match": "partial", "entropy_mean": 0.073, "entropy_vs_standard_ratio": 0.39, "frac_zero_std_final": 0.675, "frac_zero_std_max": 0.7, "frac_zero_std_min": 0.55, "kl_final": 0.009, "llama_pattern": "permanent_reward_collapse", "mean_completion_length": 1010, "recovery": false, "reward_final": 0.061, "reward_min": 0.048, "reward_peak": 0.102, "reward_std_final": 0.2, "total_steps": 100}

grpo_stage2_rasp_20_v9: relevant metrics = {"checkpoints": ["checkpoint-10", "checkpoint-15", "checkpoint-20", "checkpoint-25", "checkpoint-30"], "collapse_note": "frac_zero_std peaked at 95% by step 30, reward dropped from peak 0.039 (step 20) to 0.021 (step 30)", "collapse_status": "COLLAPSED", "final_clipped_ratio": 0.956, "final_frac_zero_std": 0.95, "final_grad_norm": 1.398, "final_kl": 0.00118, "final_loss": 0.00686, "final_mean_length": 996, "final_mean_terminated_length": 176, "final_reward": 0.021, "max_steps": 30, "reward_history": [{"frac_zero_std": 0.875, "reward": 0.015, "step": 10}, {"frac_zero_std": 0.8, "reward": 0.039,
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "8a953802-ba7b-43ff-b3c5-3d4f58cf06eb"
}
```

</details>

---


### System

_source line 83_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2a92311f30a7bab6",
  "tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "description": "Running Search for CKA similarity mu values in registry",
  "usage": {
    "total_tokens": 54574,
    "tool_uses": 21,
    "duration_ms": 198044
  },
  "last_tool_name": "Bash",
  "uuid": "5a18c38d-16cf-4620-9087-08c32ccc4196",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db"
}
```

---


### Tool call

_source line 84_

<details open><summary>🔧 Tool call — Bash · `toolu_01EBAmNrgvkXz97Yy7N1FRyr`</summary>

```json
{
  "command": "FPATH=\"/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt\"\npython3 -c \"\nimport json\nFPATH='$FPATH'\nwith open(FPATH) as f:\n    raw = f.read()\nouter = json.loads(raw)\ndata = json.loads(outer['result'])\nexps = data['data']['experiments']\n\n# Search for CKA similarity values (mu=0.62, mu>=0.88)\n# These may be in the pruning or analysis experiments\nfor eid, e in exps.items():\n    m = e.get('metrics', {})\n    r = e.get('result', {})\n    mstr = json.dumps(m) + json.dumps(r)\n    if 'cka_sim' in mstr.lower() or 'similarity' in mstr.lower() or '0.62' in mstr or '0.88' in mstr:\n        print(f'=== {eid} ===')\n        print(f'  metrics: {json.dumps(m)[:800]}')\n        print(f'  result: {json.dumps(r)[:400]}')\n        print()\n\n# Also search for 'mu' or 'mean_cka' or 'functional_overlap'\nfor eid, e in exps.items():\n    m = e.get('metrics', {})\n    mstr = json.dumps(m)\n    if 'mean_cka' in mstr.lower() or 'functional_overlap' in mstr.lower() or 'overlap' in mstr.lower():\n        print(f'=== {eid} (overlap) ===')\n        print(f'  metrics: {json.dumps(m)[:800]}')\n        print()\n\"\n",
  "description": "Search for CKA similarity mu values in registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "c2119e0a-2a34-4d8d-b030-e66da405a43a",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01UxX16vn8pbaZErdNhXtncr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2893,
      "cache_read_input_tokens": 50906,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2893,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 34,
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

_source line 85 · 2026-05-24T04:36:29.740Z_

<details><summary>↩ Tool result · `toolu_01EBAmNrgvkXz97Yy7N1FRyr`</summary>

```text
=== floor_ablation_0p6_cka_only_20_v2 ===
  metrics: {"gsm8k_accuracy": 0.6202, "gsm8k_correct": 818, "gsm8k_total": 1319, "gsm8k_ci": 0.0134, "eos_rate": 0.9803, "avg_response_length": 252.7, "grpo_train_loss": 0.006503, "grpo_final_reward": 0.2419}
  result: {}

=== eval_gsm8k_grpo_alpha4_20_v3 ===
  metrics: {"gsm8k_accuracy": 0.6277, "gsm8k_accuracy_ci": 0.0133, "gsm8k_correct": 828, "gsm8k_total": 1319, "eos_rate": 0.9856, "avg_response_length": 188.16, "natural_eos": 1300, "truncated": 19}
  result: {}

=== grpo_standard_20_fair ===
  metrics: {"wandb_run_id": "tyv20u2k", "total_steps": 100, "runtime_seconds": 3017, "reward_trajectory": [0.051, 0.056, 0.067, 0.081, 0.019, 0.043, 0.047, 0.046, 0.031, 0.054], "frac_zero_std_trajectory": [0.5, 0.625, 0.5, 0.5, 0.575, 0.55, 0.575, 0.55, 0.55, 0.55], "peak_reward": 0.081, "peak_reward_step": 40, "final_reward": 0.054, "final_frac_zero_std": 0.55, "dynamics_pattern": "dip_then_partial_recovery", "dip_step": 50, "dip_reward": 0.019}
  result: {}

=== eval_math500_sft_rasp_20_2048 ===
  metrics: {"accuracy": 0.226, "n_correct": 113, "n_total": 500, "stderr": 0.0187, "natural_eos": 314, "truncated": 186, "natural_eos_pct": 0.628, "avg_response_length": 930.58, "median_response_length": 274}
  result: {}

=== sft_cka_only_20 ===
  metrics: {"checkpoint_path": "/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20/", "note": "Initial loss 1.958 > RASP 1.86 > Standard 1.70 (CKA-only has most initial damage). Final loss 0.62 comparable to baselines. No greedy eval run yet.", "token_accuracy": 0.8362, "total_steps": 1870, "train_loss_final": 0.6165, "train_loss_initial": 1.958, "train_time_min": 33.4}
  result: {}

=== eval_grpo_rasp_25_qwen_math ===
  metrics: {"accuracy": 0.625, "n_samples": 200, "seed": 42}
  result: {}

=== eval_sft_alpha_2p0 ===
  metrics: {"accuracy": 0.62, "avg_len": 277.41, "eos_rate": 0.97, "n_correct": 62, "n_total": 100, "stderr": 0.0485}
  result: {}

=== sft_alpha4_0_westd_retry ===
  metrics: {"accuracy_stderr": 0.049, "avg_response_length": 238.56, "eos_rate": 0.98, "mean_token_accuracy_final": 0.8368, "n_correct": 62, "n_total": 100, "post_prune_accuracy": 0.4, "post_sft_accuracy_100": 0.62, "sft_recovery_gain_pp": 22, "train_loss_final": 0.7393, "train_loss_last_logged": 0.6106}
  result: {}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "cefd1317-8107-437c-811c-f4b94e82bd87"
}
```

</details>

---


### System

_source line 86_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2a92311f30a7bab6",
  "tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "description": "Running Check post-prune evaluation experiments",
  "usage": {
    "total_tokens": 56286,
    "tool_uses": 22,
    "duration_ms": 208579
  },
  "last_tool_name": "Bash",
  "uuid": "a9373b22-b80e-4b37-892e-b9100f962eb2",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db"
}
```

---


### Tool call

_source line 87_

<details open><summary>🔧 Tool call — Bash · `toolu_01PzxogNAMFUguR3UWjF6HgJ`</summary>

```json
{
  "command": "FPATH=\"/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt\"\npython3 -c \"\nimport json\nFPATH='$FPATH'\nwith open(FPATH) as f:\n    raw = f.read()\nouter = json.loads(raw)\ndata = json.loads(outer['result'])\nexps = data['data']['experiments']\n\n# Check reeval_postprune_definitive which might have CKA similarity values\nkey_ids = [\n    'reeval_postprune_definitive',\n    'eval_postprune_rasp_25',\n    'eval_postprune_rasp_30',\n    'eval_postprune_standard_30',\n    'eval_postprune_qwen_math_cka_only_20',\n    'eval_postprune_qwen_math_standard_20',\n]\nfor eid in key_ids:\n    if eid in exps:\n        e = exps[eid]\n        print(f'=== {eid} ===')\n        print(f'  hyp: {e.get(\\\"hypothesis\\\",\\\"\\\")[:400]}')\n        print(f'  metrics: {json.dumps(e.get(\\\"metrics\\\",{}))[:1000]}')\n        print(f'  result: {json.dumps(e.get(\\\"result\\\",{}))[:500]}')\n        print()\n\"\n",
  "description": "Check post-prune evaluation experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "2119085c-4f33-4572-94db-66f80ef865ce",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017tbVKBpXAngApD87CZNLrM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1678,
      "cache_read_input_tokens": 53799,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1678,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 34,
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

_source line 88 · 2026-05-24T04:36:40.285Z_

<details><summary>↩ Tool result · `toolu_01PzxogNAMFUguR3UWjF6HgJ`</summary>

```text
=== reeval_postprune_definitive ===
  hyp: D023: Definitive re-eval of pruned_standard_20 and pruned_rasp_20 with current eval_gsm8k.py + load_pruned_model. N=100, max_new_tokens=4096, greedy. Validates whether original 1% vs 29% is reproducible with current code.
  metrics: {"conclusion": "Original 29x advantage (29% vs 1%) not reproducible. Actual gap 4pp (31% vs 27% on westb), not statistically significant.", "original_claim_rasp": 0.29, "original_claim_standard": 0.01, "rasp_20_accuracy_westb": 0.31, "rasp_20_accuracy_westd": 0.29, "rasp_vs_standard_gap_pp": 4, "standard_20_accuracy_westb": 0.27}
  result: {}

=== eval_postprune_rasp_25 ===
  hyp: 25% RASP post-prune GSM8K eval (N=100, greedy). 对比 20% post-prune (31%). Parent: pruned_rasp_25.
  metrics: {"accuracy": 21, "avg_response_length": 2032.9, "correct": 21, "eos_rate": 56, "natural_eos": 56, "seed": 42, "stderr": 4.07, "total": 100, "truncated": 44}
  result: {}

=== eval_postprune_rasp_30 ===
  hyp: RASP 30% post-prune GSM8K accuracy (N=200). At 20% RASP post-prune was 29%, at 25% was 21%. 30% should be lower. Establishes degradation curve for multi-sparsity analysis.
  metrics: {"accuracy": 0, "avg_response_length": 3984.31, "eos_rate": 0.03, "n_correct": 0, "n_total": 200, "natural_eos": 6, "truncated_rate": 0.97}
  result: {}

=== eval_postprune_standard_30 ===
  hyp: Standard 30% post-prune GSM8K accuracy (N=200). At 20% Standard post-prune was 17.5%, at 25% was ~15%. 30% should show further degradation. Compared with RASP 30% post-prune (running) to verify RASP advantage persists at higher sparsity. Extends multi-sparsity degradation curve.
  metrics: {"avg_response_length": 3907.875, "correct": 8, "eos_rate": 0.055, "gsm8k_accuracy": 0.04, "natural_eos": 11, "total": 200, "truncated": 189}
  result: {}

=== eval_postprune_qwen_math_cka_only_20 ===
  hyp: Qwen2.5-Math-7B CKA-only 20% post-prune GSM8K accuracy. Tests whether CKA-only pruning generalizes from DeepSeek-R1 to Qwen-Math. Low post-prune accuracy expected; key comparison is CKA-only vs Standard post-prune.
  metrics: {"accuracy": 0.01, "n_correct": 2, "n_total": 200, "stderr": 0.00704, "eos_rate": 0.065, "avg_response_length": 958.3, "note": "Qwen-Math CKA-only 20% post-prune = 1.0%. Severe collapse (repetition, gibberish)."}
  result: {}

=== eval_postprune_qwen_math_standard_20 ===
  hyp: Qwen2.5-Math-7B Standard 20% post-prune GSM8K accuracy. Baseline for comparing CKA-only vs Standard pruning before recovery training on Qwen-Math model.
  metrics: {"accuracy": 0.185, "n_correct": 37, "n_total": 200, "stderr": 0.02746, "eos_rate": 0.69, "avg_response_length": 506.83, "note": "Qwen-Math Standard 20% post-prune = 18.5%. Significantly better than CKA-only (1.0%) at post-prune stage."}
  result: {}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "ab7a3799-6e71-49cd-a828-df63ab17fe47"
}
```

</details>

---


### System

_source line 89_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2a92311f30a7bab6",
  "tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "description": "Running Search for CKA similarity mean values across all experiments",
  "usage": {
    "total_tokens": 57947,
    "tool_uses": 23,
    "duration_ms": 219156
  },
  "last_tool_name": "Bash",
  "uuid": "96a50572-8cfd-4fac-b7c8-bebffdb4dc63",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db"
}
```

---


### Tool call

_source line 90_

<details open><summary>🔧 Tool call — Bash · `toolu_0138stGUmzoGL3cQRtGE2XR1`</summary>

```json
{
  "command": "FPATH=\"/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt\"\npython3 -c \"\nimport json\nFPATH='$FPATH'\nwith open(FPATH) as f:\n    raw = f.read()\nouter = json.loads(outer['result'])\ndata = json.loads(outer['result'])\nexps = data['data']['experiments']\n\n# Search for all experiments containing 'cka_similarity' or 'mu' or 'mean_similarity' or 'F_h' or F(h)\nfor eid, e in exps.items():\n    m = e.get('metrics', {})\n    r = e.get('result', {})\n    h = e.get('hypothesis', '')\n    combined = json.dumps(m) + json.dumps(r) + h\n    if any(term in combined for term in ['cka_similarity', 'mean_sim', 'F_h', 'F(h)', 'mu_cka', 'mean_F', 'overlap_mean', 'cka_mean']):\n        print(f'=== {eid} ===')\n        print(f'  hyp: {h[:200]}')\n        print(f'  metrics: {json.dumps(m)[:600]}')\n        print()\n\"\n",
  "description": "Search for CKA similarity mean values across all experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "08772db1-f357-4897-b7ef-9ba099147db0",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01HiE3mq1bv7qQovLBmFdY4J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1627,
      "cache_read_input_tokens": 55477,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1627,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 34,
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

_source line 91 · 2026-05-24T04:36:50.962Z_

<details><summary>↩ Tool result · reported error · `toolu_0138stGUmzoGL3cQRtGE2XR1`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 6, in &lt;module>
    outer = json.loads(outer['result'])
                       ^^^^^
NameError: name 'outer' is not defined. Did you mean: 'iter'?
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "087fc395-1bbb-481c-b10d-6dd5b70223e9",
  "tool_use_result": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 6, in &lt;module>\n    outer = json.loads(outer['result'])\n                       ^^^^^\nNameError: name 'outer' is not defined. Did you mean: 'iter'?"
}
```

</details>

---


### System

_source line 92_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2a92311f30a7bab6",
  "tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "description": "Running Search for CKA similarity fields across all experiments",
  "usage": {
    "total_tokens": 58567,
    "tool_uses": 24,
    "duration_ms": 228494
  },
  "last_tool_name": "Bash",
  "uuid": "ddc6c4f7-371c-4fd4-9c54-286ac6aaec99",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db"
}
```

---


### Tool call

_source line 93_

<details open><summary>🔧 Tool call — Bash · `toolu_01CGwzrHxWD5B95h6jRWBhvE`</summary>

```json
{
  "command": "FPATH=\"/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt\"\npython3 -c \"\nimport json\nFPATH='$FPATH'\nwith open(FPATH) as f:\n    raw = f.read()\nouter = json.loads(raw)\ndata = json.loads(outer['result'])\nexps = data['data']['experiments']\n\n# Search for all experiments containing CKA similarity related terms\nfor eid, e in exps.items():\n    m = e.get('metrics', {})\n    r = e.get('result', {})\n    h = e.get('hypothesis', '')\n    combined = json.dumps(m) + json.dumps(r) + h\n    if any(term in combined for term in ['cka_similarity', 'mean_sim', 'F_h', 'mu_cka', 'mean_F', 'overlap_mean', 'cka_mean', 'functional_sim']):\n        print('=== ' + eid + ' ===')\n        print('  hyp:', h[:200])\n        print('  metrics:', json.dumps(m)[:600])\n        print()\n\"\n",
  "description": "Search for CKA similarity fields across all experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "6fc6c8c8-e2eb-4098-8346-6ec72ba986a4",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0173HX8rbEmjmqrk2XPF6zUW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 561,
      "cache_read_input_tokens": 57104,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 561,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 59,
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

_source line 94 · 2026-05-24T04:37:00.217Z_

<details><summary>↩ Tool result · `toolu_01CGwzrHxWD5B95h6jRWBhvE`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "9f7cf052-46e3-4e24-91b1-f8f731a2b517"
}
```

</details>

---


### System

_source line 95_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2a92311f30a7bab6",
  "tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "description": "Running Check prune experiments for CKA score tracking",
  "usage": {
    "total_tokens": 59084,
    "tool_uses": 25,
    "duration_ms": 234952
  },
  "last_tool_name": "Bash",
  "uuid": "56af7503-b987-48e5-aaaa-c1002c5f142d",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db"
}
```

---


### Tool call

_source line 96_

<details open><summary>🔧 Tool call — Bash · `toolu_01H4UbPmdrzjwmRLJBsQEQJy`</summary>

```json
{
  "command": "FPATH=\"/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt\"\npython3 -c \"\nimport json\nFPATH='$FPATH'\nwith open(FPATH) as f:\n    raw = f.read()\nouter = json.loads(raw)\ndata = json.loads(outer['result'])\nexps = data['data']['experiments']\n\n# Let me check the 'floor_ablation' experiments and also look broadly for any 0.62 or 0.88 numbers\n# Also look at the prune experiments to see if they track CKA scores\nfor eid in ['prune_rasp_20_qwen_math', 'prune_standard_20_qwen_math', 'prune_rasp_25_qwen_math', \n            'prune_standard_25_qwen_math', 'prune_rasp_rlvr_20', 'prune_rasp_rlvr_20_qwen_math']:\n    if eid in exps:\n        e = exps[eid]\n        print('=== ' + eid + ' ===')\n        print('  hyp:', e.get('hypothesis','')[:300])\n        print('  metrics:', json.dumps(e.get('metrics',{}))[:600])\n        print()\n\"\n",
  "description": "Check prune experiments for CKA score tracking"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "bd0767d9-d675-4be6-bf1b-dfce76701d55",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01LjbPN3nzBnn1zhcW5HJJDX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 454,
      "cache_read_input_tokens": 57665,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 454,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 63,
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

_source line 97 · 2026-05-24T04:37:06.674Z_

<details><summary>↩ Tool result · `toolu_01H4UbPmdrzjwmRLJBsQEQJy`</summary>

```text
=== prune_rasp_20_qwen_math ===
  hyp: Qwen2.5-Math-7B RASP 20% structured pruning. Scope expansion Phase 2: 验证 RASP 在第二个模型上的有效性（CKA-guided pruning preserves reasoning across model families）。使用已计算的 importance_scores_qwen_math.pt + cka_scores_qwen_math.pt。
  metrics: {"alpha": 1, "attn_groups_pruned": 0, "mlp_groups_pruned": 199, "model_keys": 339, "original_params": 7615616512, "pruned_params": 6169214464, "sparsity_actual": 0.1899, "sparsity_target": 0.2}

=== prune_standard_20_qwen_math ===
  hyp: Qwen2.5-Math-7B Standard 20% structured pruning (negative control). Scope expansion Phase 2 对照组。
  metrics: {"attn_groups_pruned": 0, "mlp_groups_pruned": 202, "model_keys": 339, "original_params": 7615616512, "pruned_params": 6147409408, "sparsity_actual": 0.1928, "sparsity_target": 0.2}

=== prune_rasp_25_qwen_math ===
  hyp: RASP CKA-weighted scoring at 25% on Qwen2.5-Math-7B preserves functionally redundant groups, maintaining higher post-prune accuracy than standard at same sparsity (C3 cross-model)
  metrics: {"actual_sparsity": 0.2405, "attn_gqa_groups_pruned": "0/112", "mlp_groups_pruned": "252/784", "params_after": 5783991808, "target_sparsity": 0.25}

=== prune_standard_25_qwen_math ===
  hyp: Standard importance at 25% on Qwen2.5-Math-7B removes groups by magnitude alone, destroying more functional redundancy than RASP at equal sparsity (C3 cross-model baseline)
  metrics: {"actual_sparsity": 0.2396, "attn_gqa_groups_pruned": "0/112", "mlp_groups_pruned": "251/784", "target_sparsity": 0.25}

=== prune_rasp_rlvr_20 ===
  hyp: RASP-RLVR 20% pruning: score = importance * cka^alpha. 反转 CKA scoring——剪掉功能独特的结构（低 CKA overlap），保留冗余结构（高 overlap），使 RLVR 更容易通过冗余路径恢复能力。对比 RASP (1-cka)^alpha 和 Standard (importance only)。
  metrics: {"actual_sparsity": 0.1909, "attn_gqa_groups_pruned": "0/112", "group_selection_diff_vs_rasp": "RASP\u91cd\u526a\u524d6\u5c42+\u540e\u6bb5(19,23-25,27)\u4fdd\u4e2d\u95f4; RLVR\u91cd\u526a\u524d6\u5c42+\u4e2d\u540e\u6bb5(16-26)\u4fddLayer6-7,27", "mlp_groups_pruned": "200/784", "params_after": "6.16B", "target_sparsity": 0.2}

=== prune_rasp_rlvr_20_qwen_math ===
  hyp: RASP-RLVR scoring on Qwen2.5-Math-7B at 20% sparsity preserves RLVR-relevant functional groups, yielding higher post-prune reasoning accuracy than standard importance (C3 cross-model)
  metrics: {"actual_sparsity": 0.1909, "attn_groups_pruned": 0, "attn_groups_total": 112, "mlp_groups_pruned": 200, "mlp_groups_total": 784, "pruned_params": 6161946112}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "27bb08f9-1f88-4cc4-a6e0-5fad91767c9d"
}
```

</details>

---


### System

_source line 98_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2a92311f30a7bab6",
  "tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "description": "Running Search for 0.62 and 0.88 values in hypotheses",
  "usage": {
    "total_tokens": 60712,
    "tool_uses": 26,
    "duration_ms": 244665
  },
  "last_tool_name": "Bash",
  "uuid": "c0cea687-f19d-4927-856f-a92f02b02999",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db"
}
```

---


### Tool call

_source line 99_

<details open><summary>🔧 Tool call — Bash · `toolu_01SmHbPgiRdrE74jJwaXvcKU`</summary>

```json
{
  "command": "FPATH=\"/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt\"\n\n# Search for \"0.62\" and \"0.88\" in the raw file near \"cka\" or \"similarity\" context\npython3 -c \"\nimport json\nFPATH='$FPATH'\nwith open(FPATH) as f:\n    raw = f.read()\nouter = json.loads(raw)\ndata = json.loads(outer['result'])\nexps = data['data']['experiments']\n\n# Print ALL hypothesis text that mentions 0.62 or 0.88 or 'mu'\nfor eid, e in exps.items():\n    h = e.get('hypothesis', '')\n    m = e.get('metrics', {})\n    mstr = json.dumps(m)\n    if '0.62' in h or '0.88' in h or ('mu' in h.lower() and 'cka' in h.lower()):\n        print('=== ' + eid + ' ===')\n        print('  hyp:', h[:400])\n        print('  metrics:', mstr[:400])\n        print()\n\"",
  "description": "Search for 0.62 and 0.88 values in hypotheses"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "4dad8150-2f47-4607-8963-85b1d4db3a32",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01YKhbky6PZ9uZxFQWAg327v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1595,
      "cache_read_input_tokens": 58119,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1595,
        "ephemeral_1h_input_tokens": 0
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

_source line 100 · 2026-05-24T04:37:16.419Z_

<details><summary>↩ Tool result · `toolu_01SmHbPgiRdrE74jJwaXvcKU`</summary>

```text
=== eval_gsm8k_grpo_cka_only_15_seed123 ===
  hyp: GSM8K N=1319 eval on CKA-only 15% GRPO seed123. Multi-seed validation for 15% sparsity gap statistical significance.
  metrics: {"accuracy": 73.09, "n_correct": 964, "n_total": 1319, "stderr": 1.22, "eos_rate": 98.79, "truncated": 16}

=== eval_gsm8k_grpo_cka_only_15_seed456 ===
  hyp: GSM8K N=1319 eval on CKA-only 15% GRPO seed456. Multi-seed validation for 15% sparsity gap statistical significance.
  metrics: {"accuracy": 0.721, "n_correct": 951, "n_total": 1319, "stderr": 0.0123, "eos_rate": 0.9894, "avg_response_length": 201.94}

=== grpo_cka_only_15_seed456 ===
  hyp: Multi-seed validation (seed=456) of CKA-only 15% GRPO training. v5 fair config (100 steps). Seed=42 (grpo_cka_only_15_v2): completed with reward=0.4019. Third seed point for CKA-only 15% recovery consistency and statistical significance.
  metrics: {}

=== grpo_cka_only_15_seed123 ===
  hyp: Multi-seed validation (seed=123) of CKA-only 15% GRPO training. v5 fair config (100 steps). Seed=42 (grpo_cka_only_15_v2): completed with reward=0.4019. Second seed point to establish CKA-only 15% recovery consistency for cross-sparsity significance testing.
  metrics: {}

=== grpo_cka_only_20_seed456 ===
  hyp: Multi-seed validation (seed=456) of CKA-only 20% GRPO training. v5 fair config (100 steps, beta=0.01, loss_type=dapo, temperature=0.4). Seed=42: 64.37%, seed=123: 64.22%. Third seed point to establish CKA-only method's recovery consistency and enable 3-seed parity comparison with Standard (3 seeds: 59.44%, pending, pending). P0 审稿硬需求 W-C4.
  metrics: {"final_loss": 0.0999, "avg_train_loss": 0.0881, "final_reward": 0.2925, "final_kl": 0.0017, "train_steps": 100, "train_runtime_min": 21.8}

=== eval_mbpp_grpo_rasp_20 ===
  hyp: MBPP pass@1 eval on GRPO RASP 20% model @2048. Dense baseline=53.48% (200/374). RASP GRPO GSM8K=60.88%, HumanEval=10.37%. Tests RASP GRPO code generation on MBPP. Completes MBPP 3×2 matrix. Expected: between CKA-only GRPO (14.17%) and Standard GRPO (running). Recovery gradient on MBPP validates C2 capability breadth claim on second code benchmark.
  metrics: {"pass_at_1": 0.131, "n_correct": 49, "n_total": 374, "stderr": 0.0174}

=== eval_gsm8k_sft_shortgpt_20 ===
  hyp: ShortGPT SFT checkpoint GSM8K eval. After depth pruning (5/28 layers removed by Block Influence scoring) + SFT warmup (loss=0.62, token_accuracy=0.83), measure GSM8K accuracy. Compare with fine-grained pruning SFT results: CKA-only SFT ~60%, Standard SFT ~64%. ShortGPT expected lower due to coarse layer removal destroying more representations.
  metrics: {"gsm8k_accuracy": 44.73, "n_correct": 590, "n_total": 1319}

=== sft_shortgpt_20 ===
  hyp: ShortGPT depth pruning (20%, 5/28 layers removed) after SFT warmup will show lower recovery capacity than fine-grained structural pruning methods (Standard/CKA-only/RASP) because coarse layer removal destroys more distributed representations needed for GRPO recovery. Layers removed: [15,16,17,24,25], actual param sparsity 15.30%.
  metrics: {}

=== eval_humaneval_grpo_standard_20_1p5b_2048 ===
  hyp: 1.5B GRPO Standard HumanEval pass@1 @2048. Cross-scale validation baseline. 7B GRPO Standard HumanEval failed (multiple attempts). If 1.5B Standard also shows weak code generation after GRPO (vs CKA-only), strengthens claim that standard pruning loses broader capabilities.
  metrics: {}

=== grpo_cka_only_20_seed123 ===
  hyp: Multi-seed validation (seed=123) of CKA-only 20% GRPO training. If CKA-only advantage holds across seeds, strengthens C1 claim that pruning criteria determine recovery capacity. Seed 42 result: 64.37% GSM8K.
  metrics: {"train_loss": 0.1361, "final_step_loss": 0.05054, "final_reward": 0.2975, "final_reward_std": 0.4097, "train_steps": 100, "train_runtime_hours": 11.63, "wandb_run": "j8kn0sqd"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "32c95dfe-44b6-4194-ad3d-80fa2a19c8f0"
}
```

</details>

---


### System

_source line 101_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2a92311f30a7bab6",
  "tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "description": "Running Compute reward ratio, f_0, and delta calculations",
  "usage": {
    "total_tokens": 62658,
    "tool_uses": 27,
    "duration_ms": 265953
  },
  "last_tool_name": "Bash",
  "uuid": "165d19a7-c8d2-47db-a653-63771e081b16",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db"
}
```

---


### Tool call

_source line 102_

<details open><summary>🔧 Tool call — Bash · `toolu_019V5BtVe5cUEoizEsWBEaMd`</summary>

```json
{
  "command": "FPATH=\"/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt\"\npython3 -c \"\nimport json\nFPATH='$FPATH'\nwith open(FPATH) as f:\n    raw = f.read()\nouter = json.loads(raw)\ndata = json.loads(outer['result'])\nexps = data['data']['experiments']\n\n# Look for the peak reward ratio calculation (4.4x) in all data\n# CKA-only peak reward vs Standard peak reward\n# From data: CKA-only peak = 0.3544 (grpo_cka_only_20), Standard peak = 0.081 (grpo_standard_20_fair)\n# ratio = 0.3544 / 0.081 = 4.374 ~ 4.4x\nprint('CKA-only peak:', 0.3544)\nprint('Standard peak:', 0.081)\nprint('Ratio:', round(0.3544/0.081, 2))\nprint()\n\n# f_0 (zero-variance batch fraction)\n# Standard shows frac_zero_std = 0.55 (final), trajectory: [0.5, 0.625, 0.5, 0.5, 0.575, 0.55, 0.575, 0.55, 0.55, 0.55]\n# All > 0.5? Min = 0.5\nprint('Standard frac_zero_std trajectory:', [0.5, 0.625, 0.5, 0.5, 0.575, 0.55, 0.575, 0.55, 0.55, 0.55])\nprint('Min:', min([0.5, 0.625, 0.5, 0.5, 0.575, 0.55, 0.575, 0.55, 0.55, 0.55]))\nprint('All >= 0.5?', all(x >= 0.5 for x in [0.5, 0.625, 0.5, 0.5, 0.575, 0.55, 0.575, 0.55, 0.55, 0.55]))\nprint()\n\n# Dose-response deltas at each alpha point\nalphas = {\n    '0.5': (0.6118, 0.6073),  # GRPO, SFT\n    '2.0': (0.6611, 0.6497),\n    '3.0': (0.6345, 0.6414),\n    '4.0': (0.6277, 0.6194),\n}\nprint('=== Dose-response |Delta(GRPO-SFT)| per alpha ===')\nfor alpha, (grpo, sft) in alphas.items():\n    delta = abs(grpo - sft) * 100\n    print(f'alpha={alpha}: GRPO={grpo*100:.2f}%, SFT={sft*100:.2f}%, |Delta|={delta:.2f} pp')\nprint()\n\n# SFT vs GRPO gap at 20% sparsity (main metric)\n# Standard: SFT=59.21%, GRPO=59.44% -> delta = +0.23 pp\n# CKA-only: SFT=63.91%, GRPO=64.37% -> delta = +0.46 pp\n# RASP: SFT=61.49%, GRPO=60.88% -> delta = -0.61 pp\nprint('=== Main 20% sparsity SFT->GRPO deltas ===')\nmethods = {\n    'Standard': (0.5921, 0.5944),  # from eval experiments\n    'CKA-only': (0.6391, 0.6437),\n    'RASP': (0.6149, 0.6088),\n}\nfor method, (sft, grpo) in methods.items():\n    delta = (grpo - sft) * 100\n    print(f'{method}: SFT={sft*100:.2f}%, GRPO={grpo*100:.2f}%, Delta={delta:.2f} pp, |Delta|={abs(delta):.2f} pp')\n\"\n",
  "description": "Compute reward ratio, f_0, and delta calculations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "e0d15b33-6684-49ac-b47b-47057b06bc85",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_016DQcUeDtnzLMezSsa6vYeW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1912,
      "cache_read_input_tokens": 59714,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1912,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 34,
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

_source line 103 · 2026-05-24T04:37:37.691Z_

<details><summary>↩ Tool result · `toolu_019V5BtVe5cUEoizEsWBEaMd`</summary>

```text
CKA-only peak: 0.3544
Standard peak: 0.081
Ratio: 4.38

Standard frac_zero_std trajectory: [0.5, 0.625, 0.5, 0.5, 0.575, 0.55, 0.575, 0.55, 0.55, 0.55]
Min: 0.5
All >= 0.5? True

=== Dose-response |Delta(GRPO-SFT)| per alpha ===
alpha=0.5: GRPO=61.18%, SFT=60.73%, |Delta|=0.45 pp
alpha=2.0: GRPO=66.11%, SFT=64.97%, |Delta|=1.14 pp
alpha=3.0: GRPO=63.45%, SFT=64.14%, |Delta|=0.69 pp
alpha=4.0: GRPO=62.77%, SFT=61.94%, |Delta|=0.83 pp

=== Main 20% sparsity SFT->GRPO deltas ===
Standard: SFT=59.21%, GRPO=59.44%, Delta=0.23 pp, |Delta|=0.23 pp
CKA-only: SFT=63.91%, GRPO=64.37%, Delta=0.46 pp, |Delta|=0.46 pp
RASP: SFT=61.49%, GRPO=60.88%, Delta=-0.61 pp, |Delta|=0.61 pp
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "df1531c6-23d2-4db7-b20c-b74af546e3f1"
}
```

</details>

---


### System

_source line 104_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2a92311f30a7bab6",
  "tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "description": "Running Check random pruning GRPO vs SFT delta for 4-criteria computation",
  "usage": {
    "total_tokens": 64400,
    "tool_uses": 28,
    "duration_ms": 283007
  },
  "last_tool_name": "Bash",
  "uuid": "baf18fa6-1cf4-4950-ae1c-fce1308a1d58",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db"
}
```

---


### Tool call

_source line 105_

<details open><summary>🔧 Tool call — Bash · `toolu_017HVDh4BHHo7wAgsVjGTi6F`</summary>

```json
{
  "command": "FPATH=\"/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt\"\npython3 -c \"\nimport json\nFPATH='$FPATH'\nwith open(FPATH) as f:\n    raw = f.read()\nouter = json.loads(raw)\ndata = json.loads(outer['result'])\nexps = data['data']['experiments']\n\n# Claim 2: Mean |Delta(GRPO-SFT)| across four fine-grained criteria at 20% sparsity = 0.54 pp\n# The 'four criteria' appear to be: Standard, CKA-only, RASP, and possibly Random or ShortGPT\n# Or could be FOUR evaluation benchmarks: GSM8K, HumanEval, MBPP, MATH-500\n# Let's check SFT vs GRPO delta across all methods at 20%:\n# Standard: Delta = +0.23 pp\n# CKA-only: Delta = +0.46 pp\n# RASP: Delta = -0.61 pp\n# What's the 4th? Random? ShortGPT?\n# Random: SFT=51.25%, GRPO=50.57% (seed42) -> delta = -0.68 pp\n# ShortGPT: SFT=44.73%, GRPO=43.37% -> delta = -1.36 pp\n\n# But paper claims mean=0.54, max=0.61 which matches CKA-only+Standard+RASP as the 3 criteria\n# 3 criteria: |0.23| + |0.46| + |0.61| = 1.30 / 3 = 0.43 pp (not 0.54)\n\n# But if it's 4 criteria including something else:\n# Maybe 4 pruning methods at 20%: Standard(0.23), CKA-only(0.46), RASP(0.61), Random(?)\n# Random: need to check\n\n# Check random 20% GRPO result\nrandom_grpo = exps.get('eval_gsm8k_grpo_random_20_v2', {})\nrandom_sft = exps.get('eval_gsm8k_sft_random_20', {})\nprint('Random GRPO v2:', random_grpo.get('metrics', {}))\nprint('Random SFT:', random_sft.get('metrics', {}))\n\n# Also check seed42 random grpo\nfor eid in ['eval_gsm8k_grpo_random_20_v2', 'eval_gsm8k_grpo_random_20_seed123_v2', 'eval_gsm8k_grpo_random_20_seed456']:\n    if eid in exps:\n        m = exps[eid].get('metrics',{})\n        print(f'{eid}: {m}')\n\"\n",
  "description": "Check random pruning GRPO vs SFT delta for 4-criteria computation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "5da21c8d-9405-412f-b8a8-a723322507ee",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01EeygmzW97jnzw6pEt2sY6m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1709,
      "cache_read_input_tokens": 61626,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1709,
        "ephemeral_1h_input_tokens": 0
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

_source line 106 · 2026-05-24T04:37:54.730Z_

<details><summary>↩ Tool result · `toolu_017HVDh4BHHo7wAgsVjGTi6F`</summary>

```text
Random GRPO v2: {'gsm8k_accuracy': 0.5057, 'gsm8k_stderr': 0.0138, 'correct': 667, 'total': 1319, 'eos_rate': 0.9954, 'avg_response_length': 173}
Random SFT: {'gsm8k_accuracy': 0.5125, 'correct': 676, 'n_total': 1319, 'stderr': 0.0138, 'eos_rate': 0.9932, 'avg_response_length': 182.4}
eval_gsm8k_grpo_random_20_v2: {'gsm8k_accuracy': 0.5057, 'gsm8k_stderr': 0.0138, 'correct': 667, 'total': 1319, 'eos_rate': 0.9954, 'avg_response_length': 173}
eval_gsm8k_grpo_random_20_seed123_v2: {'accuracy': 0.5072, 'n_correct': 669, 'n_total': 1319, 'stderr': 0.01377, 'eos_rate': 0.9939, 'avg_response_length': 177.9}
eval_gsm8k_grpo_random_20_seed456: {'gsm8k_accuracy': 0.5087, 'gsm8k_accuracy_se': 0.0138, 'gsm8k_correct': 671, 'gsm8k_total': 1319, 'eos_rate': 0.9954, 'avg_response_length': 163.5, 'truncated': 6}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "2a21a64d-de86-477f-9a7e-af117d2333dd"
}
```

</details>

---


### System

_source line 107_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2a92311f30a7bab6",
  "tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "description": "Running Compare SFT vs GRPO deltas across four benchmarks for CKA-only",
  "usage": {
    "total_tokens": 65743,
    "tool_uses": 29,
    "duration_ms": 300588
  },
  "last_tool_name": "Bash",
  "uuid": "465b2f51-b179-48a6-9bfd-60a9d803d600",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db"
}
```

---


### Tool call

_source line 108_

<details open><summary>🔧 Tool call — Bash · `toolu_01QwaPdiru5reFtSGSW4Pmza`</summary>

```json
{
  "command": "FPATH=\"/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt\"\npython3 -c \"\nimport json\nFPATH='$FPATH'\nwith open(FPATH) as f:\n    raw = f.read()\nouter = json.loads(raw)\ndata = json.loads(outer['result'])\nexps = data['data']['experiments']\n\n# Now let's understand the 4 fine-grained criteria\n# Looking at the benchmark evaluations: GSM8K, HumanEval, MBPP, MATH-500 - 4 benchmarks\n# For CKA-only 20%:\n# GSM8K: SFT=63.91%, GRPO=64.37%  -> delta = +0.46 pp\n# HumanEval: SFT=20.12%, GRPO=20.12%  -> delta = 0 pp (actually check this)\n# MBPP: SFT=12.83%, GRPO=14.17%  -> delta = +1.34 pp\n# MATH-500: SFT=29.0%, GRPO=29.2%  -> delta = +0.2 pp\n\n# Let me check HumanEval CKA-only SFT vs GRPO\n# eval_humaneval_sft_cka_only_20_2048_v2: pass_at_1=20.12%  (note: stored as 20.12, not 0.2012)\n# eval_humaneval_grpo_cka_only_20_2048: pass_at_1=0.2012\n\nhe_sft = exps['eval_humaneval_sft_cka_only_20_2048_v2'].get('metrics',{})\nhe_grpo = exps['eval_humaneval_grpo_cka_only_20_2048'].get('metrics',{})\nprint('HumanEval CKA-only SFT:', he_sft)\nprint('HumanEval CKA-only GRPO:', he_grpo)\n\n# For Standard 20%\n# GSM8K: SFT=59.21%, GRPO=59.44%  -> delta = +0.23 pp\n# HumanEval SFT: eval_humaneval_sft_standard_20_2048_v2 = 11.59%\n# HumanEval GRPO: eval_humaneval_grpo_standard_20_2048 = 10.37%\n# MBPP SFT: eval_mbpp_sft_standard_20_v4 = 12.03%\n# MBPP GRPO: eval_mbpp_grpo_standard_20_v4 = 13.10%\n# MATH-500 SFT standard 20: eval_math500_sft_standard_20 \n# MATH-500 GRPO standard 20: eval_math500_grpo_standard_20_fair_v2\n\nmath_sft_std = exps.get('eval_math500_sft_standard_20', {}).get('metrics', {})\nmath_grpo_std = exps.get('eval_math500_grpo_standard_20_fair_v2', {}).get('metrics', {})\nprint()\nprint('MATH-500 Standard SFT:', math_sft_std)\nprint('MATH-500 Standard GRPO:', math_grpo_std)\n\n# For RASP 20%  \nmath_sft_rasp = exps.get('eval_math500_sft_rasp_20', {}).get('metrics', {})\nmath_grpo_rasp = exps.get('eval_math500_grpo_rasp_20_fair', {}).get('metrics', {})\nprint('MATH-500 RASP SFT:', math_sft_rasp)\nprint('MATH-500 RASP GRPO:', math_grpo_rasp)\n\nmath_sft_cka = exps.get('eval_math500_sft_cka_only_20_v4_restart', {}).get('metrics', {})\nmath_grpo_cka = exps.get('eval_math500_grpo_cka_only_20_fixed', {}).get('metrics', {})\nprint('MATH-500 CKA SFT:', math_sft_cka)\nprint('MATH-500 CKA GRPO fixed:', math_grpo_cka)\n\"\n",
  "description": "Compare SFT vs GRPO deltas across four benchmarks for CKA-only"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "0ecf0544-ebf3-40db-859a-5eb10a1f7144",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01265cUGccFwiaDBws86QvNe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1310,
      "cache_read_input_tokens": 63335,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1310,
        "ephemeral_1h_input_tokens": 0
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

_source line 109 · 2026-05-24T04:38:12.330Z_

<details><summary>↩ Tool result · `toolu_01QwaPdiru5reFtSGSW4Pmza`</summary>

```text
HumanEval CKA-only SFT: {'pass_at_1': 20.12, 'n_correct': 33, 'n_total': 164}
HumanEval CKA-only GRPO: {'pass_at_1': 0.2012, 'n_correct': 33, 'n_total': 164, 'stderr': 0.0313, 'avg_response_length': 1523.31, 'median_response_length': 2048, 'wall_clock_seconds': 11933}

MATH-500 Standard SFT: {'correct': 130, 'eos_rate': 0.578, 'math500_acc': 0.26, 'stderr': 0.0196, 'total': 500, 'truncated': 211, 'wall_time_hours': 3.58}
MATH-500 Standard GRPO: {'accuracy': 0.264, 'n_correct': 132, 'n_total': 500, 'stderr': 0.0197}
MATH-500 RASP SFT: {'correct': 121, 'math500_acc': 0.242, 'stderr': 0.0192, 'total': 500, 'wall_time_hours': 2.94}
MATH-500 RASP GRPO: {'accuracy': 0.24, 'n_correct': 120, 'n_total': 500, 'stderr': 0.0191, 'natural_eos_pct': 0.64, 'truncated_pct': 0.36, 'avg_response_length': 903.5, 'median_response_length': 272, 'max_new_tokens': 2048}
MATH-500 CKA SFT: {'accuracy': 0.29, 'n_correct': 145, 'n_total': 500, 'stderr': 0.0203, 'natural_eos': 384, 'truncated': 116, 'natural_eos_pct': 0.768, 'avg_response_length': 673.278, 'median_response_length': 242.5}
MATH-500 CKA GRPO fixed: {'accuracy': 0.276, 'n_correct': 138, 'n_total': 500, 'stderr': 0.02}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "9fd5cf9f-c283-4cd7-9bcb-cedf4502cdbd"
}
```

</details>

---


### System

_source line 110_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2a92311f30a7bab6",
  "tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "description": "Running Compute 4-benchmark delta for each pruning method at 20% sparsity",
  "usage": {
    "total_tokens": 67646,
    "tool_uses": 30,
    "duration_ms": 316925
  },
  "last_tool_name": "Bash",
  "uuid": "a8800b98-85d1-40c1-a758-8c1ee9170e07",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db"
}
```

---


### Tool call

_source line 111_

<details open><summary>🔧 Tool call — Bash · `toolu_01WK3y1vPrGcakQNQmuP7cVU`</summary>

```json
{
  "command": "FPATH=\"/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt\"\npython3 -c \"\nimport json\nFPATH='$FPATH'\nwith open(FPATH) as f:\n    raw = f.read()\nouter = json.loads(raw)\ndata = json.loads(outer['result'])\nexps = data['data']['experiments']\n\n# Now compute 4-criteria delta for each method at 20% sparsity\n# 4 criteria = GSM8K, HumanEval, MBPP, MATH-500\n\n# Method: Standard 20%\nstd = {\n    'GSM8K': (0.5921, 0.5944),  # SFT, GRPO\n    'HumanEval': (0.1159, 0.1037),\n    'MBPP': (0.1203, 0.131),\n    'MATH-500': (0.26, 0.264),\n}\nprint('=== Standard 20% ===')\nfor bench, (sft, grpo) in std.items():\n    delta = (grpo - sft)*100\n    print(f'  {bench}: SFT={sft*100:.2f}%, GRPO={grpo*100:.2f}%, Delta={delta:.2f} pp')\ndeltas_std = [abs((grpo-sft)*100) for sft, grpo in std.values()]\nprint(f'  Mean |Delta|={sum(deltas_std)/len(deltas_std):.2f} pp, Max={max(deltas_std):.2f} pp')\nprint()\n\n# Method: CKA-only 20%\ncka = {\n    'GSM8K': (0.6391, 0.6437),\n    'HumanEval': (0.2012, 0.2012),  # Both 20.12%\n    'MBPP': (0.1283, 0.1417),\n    'MATH-500': (0.29, 0.276),  # using fixed values\n}\nprint('=== CKA-only 20% ===')\nfor bench, (sft, grpo) in cka.items():\n    delta = (grpo - sft)*100\n    print(f'  {bench}: SFT={sft*100:.2f}%, GRPO={grpo*100:.2f}%, Delta={delta:.2f} pp')\ndeltas_cka = [abs((grpo-sft)*100) for sft, grpo in cka.values()]\nprint(f'  Mean |Delta|={sum(deltas_cka)/len(deltas_cka):.2f} pp, Max={max(deltas_cka):.2f} pp')\nprint()\n\n# Method: RASP 20%\nrasp = {\n    'GSM8K': (0.6149, 0.6088),\n    'HumanEval': (0.1037, 0.1463),  # SFT from eval_humaneval_sft_rasp_20_2048, GRPO from eval_humaneval_grpo_rasp_20_2048\n    'MBPP': (0.1176, 0.131),\n    'MATH-500': (0.242, 0.24),\n}\nprint('=== RASP 20% ===')\nfor bench, (sft, grpo) in rasp.items():\n    delta = (grpo - sft)*100\n    print(f'  {bench}: SFT={sft*100:.2f}%, GRPO={grpo*100:.2f}%, Delta={delta:.2f} pp')\ndeltas_rasp = [abs((grpo-sft)*100) for sft, grpo in rasp.values()]\nprint(f'  Mean |Delta|={sum(deltas_rasp)/len(deltas_rasp):.2f} pp, Max={max(deltas_rasp):.2f} pp')\n\"\n",
  "description": "Compute 4-benchmark delta for each pruning method at 20% sparsity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "352d0ee6-ddd9-4f8d-9fe2-f735bd108a01",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01MmDz8hjA3xWUfCvTez3dLX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1870,
      "cache_read_input_tokens": 64645,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1870,
        "ephemeral_1h_input_tokens": 0
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

_source line 112 · 2026-05-24T04:38:28.674Z_

<details><summary>↩ Tool result · `toolu_01WK3y1vPrGcakQNQmuP7cVU`</summary>

```text
=== Standard 20% ===
  GSM8K: SFT=59.21%, GRPO=59.44%, Delta=0.23 pp
  HumanEval: SFT=11.59%, GRPO=10.37%, Delta=-1.22 pp
  MBPP: SFT=12.03%, GRPO=13.10%, Delta=1.07 pp
  MATH-500: SFT=26.00%, GRPO=26.40%, Delta=0.40 pp
  Mean |Delta|=0.73 pp, Max=1.22 pp

=== CKA-only 20% ===
  GSM8K: SFT=63.91%, GRPO=64.37%, Delta=0.46 pp
  HumanEval: SFT=20.12%, GRPO=20.12%, Delta=0.00 pp
  MBPP: SFT=12.83%, GRPO=14.17%, Delta=1.34 pp
  MATH-500: SFT=29.00%, GRPO=27.60%, Delta=-1.40 pp
  Mean |Delta|=0.80 pp, Max=1.40 pp

=== RASP 20% ===
  GSM8K: SFT=61.49%, GRPO=60.88%, Delta=-0.61 pp
  HumanEval: SFT=10.37%, GRPO=14.63%, Delta=4.26 pp
  MBPP: SFT=11.76%, GRPO=13.10%, Delta=1.34 pp
  MATH-500: SFT=24.20%, GRPO=24.00%, Delta=-0.20 pp
  Mean |Delta|=1.60 pp, Max=4.26 pp
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "c135c1a6-5642-46df-8407-9408fc029ec6"
}
```

</details>

---


### System

_source line 113_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2a92311f30a7bab6",
  "tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "description": "Running Check other pruning methods and fixed MATH-500 evaluations",
  "usage": {
    "total_tokens": 69290,
    "tool_uses": 31,
    "duration_ms": 333003
  },
  "last_tool_name": "Bash",
  "uuid": "9f1528d6-a155-4348-8784-144740084fd0",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db"
}
```

---


### Tool call

_source line 114_

<details open><summary>🔧 Tool call — Bash · `toolu_01Nv2EAuNcuRA4rdSjYW8WKJ`</summary>

```json
{
  "command": "FPATH=\"/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt\"\npython3 -c \"\nimport json\nFPATH='$FPATH'\nwith open(FPATH) as f:\n    raw = f.read()\nouter = json.loads(raw)\ndata = json.loads(outer['result'])\nexps = data['data']['experiments']\n\n# The paper claims mean 0.54 pp and max 0.61 pp. These only match the GSM8K-only analysis.\n# The 'four fine-grained criteria' might refer to something different.\n# Let me look at the paper's Table decoupling: SFT-only gap 4.62 pp\n# Maybe 4 criteria are 4 evaluation subsets within GSM8K\n\n# Let me check if there's any experiment with multi-criteria sub-scores within GSM8K\n# or maybe the 4 methods at one benchmark\n# Standard(+0.23), CKA-only(+0.46), RASP(-0.61), Random(-0.68) = ?\n# mean |Delta| = (0.23+0.46+0.61+0.68)/4 = 0.495 pp (not 0.54)\n# max = 0.68 (not 0.61)\n\n# Or maybe: Standard(+0.23), CKA-only(+0.46), RASP(-0.61), then what?\n# Let me check if there's a 'depth-first' or 'unstructured' eval\nfor eid in ['eval_gsm8k_grpo_depth_first_20', 'eval_gsm8k_sft_depth_first_20', \n            'eval_gsm8k_grpo_unstructured_20', 'eval_unstructured_20']:\n    if eid in exps:\n        m = exps[eid].get('metrics', {})\n        h = exps[eid].get('hypothesis', '')\n        print(f'{eid}: {m}')\n        print(f'  hyp: {h[:200]}')\n        print()\n\n# Also check eval_math500 with fixed eval\nfor eid in ['eval_math500_sft_rasp_alpha2p0_20_fixed', 'eval_math500_grpo_rasp_alpha2p0_20_fixed']:\n    if eid in exps:\n        m = exps[eid].get('metrics', {})\n        h = exps[eid].get('hypothesis', '')\n        print(f'{eid}: {m}')\n        print(f'  hyp: {h[:200]}')\n\"\n",
  "description": "Check other pruning methods and fixed MATH-500 evaluations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "f85e8713-bb19-4daa-8a7f-ce285d02ff1e",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BQjPzHxu11h4QygTkTSwL4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1611,
      "cache_read_input_tokens": 66515,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1611,
        "ephemeral_1h_input_tokens": 0
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

_source line 115 · 2026-05-24T04:38:44.740Z_

<details><summary>↩ Tool result · `toolu_01Nv2EAuNcuRA4rdSjYW8WKJ`</summary>

```text
eval_gsm8k_grpo_depth_first_20: {'accuracy_approx': 0.08, 'note': 'Early-stopped by Director at ~60-88 samples. Interim accuracy ~8%@50 (GRPO). Prior log recovery showed ~24.18% from nohup output. No JSON result file produced.', 'early_stopped': True, 'result_file_on_westb': False}
  hyp: MF5 depth-first GRPO GSM8K eval re-run. Previous pipeline_depth_first_20 results lost due to disk-full during JSON write. GRPO checkpoint intact. Re-running eval to get formal JSON result file. Prior 

eval_gsm8k_sft_depth_first_20: {'accuracy_approx': 0.1, 'note': 'Early-stopped by Director at ~60-88 samples. Interim accuracy ~10%@50 (SFT). No JSON result file produced.', 'early_stopped': True, 'result_file_on_westb': False}
  hyp: MF5 depth-first SFT GSM8K eval. Establishes SFT baseline for depth-first pruning method, paired with GRPO eval to check C1 decoupling for this baseline method.

eval_gsm8k_grpo_unstructured_20: {'accuracy': 0.8764, 'n_correct': 1156, 'n_total': 1319, 'stderr': 0.00906, 'eos_rate': 0.9818, 'truncated': 24, 'avg_response_length': 600}
  hyp: GSM8K accuracy for GRPO-recovered unstructured 20% pruned model. Pre-GRPO baseline was 87.87%. Compare with structured GRPO results (CKA-only 64.37%, Standard 58.91%, RASP 56.71%) to quantify structur

eval_unstructured_20: {'avg_response_length': 641, 'correct': 1159, 'eos_rate': 0.9803, 'gsm8k_acc': 0.8787, 'stderr': 0.009, 'total': 1319, 'truncated': 26, 'wall_time_hours': 3.23}
  hyp: Unstructured magnitude pruning at 20% sparsity should retain more accuracy than structured pruning (RASP/Standard) at same sparsity level, since unstructured preserves model architecture. Serves as ca

eval_math500_sft_rasp_alpha2p0_20_fixed: {'accuracy': 0.256, 'n_correct': 128, 'n_total': 500, 'stderr': 0.01952, 'truncated': 155, 'natural_eos': 345, 'truncated_pct': 0.31, 'avg_response_length': 805.754}
  hyp: SFT RASP α=2.0 20% MATH-500 with fixed eval script. Model on westd (sft_rasp_alpha2p0_20). P1 dose-response table.
eval_math500_grpo_rasp_alpha2p0_20_fixed: {'accuracy': 0.274, 'n_correct': 137, 'n_total': 500, 'truncated_pct': 0.302, 'truncated': 151, 'natural_eos': 349}
  hyp: GRPO RASP α=2.0 20% MATH-500 with fixed eval script. Model on westd (grpo_rasp_alpha2p0_20). P1 dose-response table.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "f090a6c4-fff9-4efa-9ac9-b3bf62981074"
}
```

</details>

---


### System

_source line 116_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2a92311f30a7bab6",
  "tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "description": "Running Check random GRPO seed42 for four-criteria computation",
  "usage": {
    "total_tokens": 71047,
    "tool_uses": 32,
    "duration_ms": 354086
  },
  "last_tool_name": "Bash",
  "uuid": "3d73ed10-c31e-4633-aed4-feefab9f179b",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db"
}
```

---


### Tool call

_source line 117_

<details open><summary>🔧 Tool call — Bash · `toolu_01KsF7PAnQjMSisiXjt8NAdg`</summary>

```json
{
  "command": "FPATH=\"/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt\"\npython3 -c \"\nimport json\nFPATH='$FPATH'\nwith open(FPATH) as f:\n    raw = f.read()\nouter = json.loads(raw)\ndata = json.loads(outer['result'])\nexps = data['data']['experiments']\n\n# The paper says 'four fine-grained criteria' with mean=0.54 and max=0.61 pp AT 20% SPARSITY ON GSM8K\n# This must be: 4 pruning methods (Standard, CKA-only, RASP, Random) evaluated on GSM8K at 20% sparsity\n# Standard: delta = +0.23 pp\n# CKA-only: delta = +0.46 pp \n# RASP: delta = -0.61 pp\n# Random: delta = -0.68 pp (seed42)\n# But that gives mean = 0.495, max = 0.68 -- doesn't match\n\n# What if 'four criteria' means 4 alpha points in dose-response?\n# alpha0.5: |0.45|, alpha2.0: |1.14|, alpha3.0: |0.69|, alpha4.0: |0.83|\n# mean = (0.45+1.14+0.69+0.83)/4 = 0.778, max=1.14 -- doesn't match\n\n# OR maybe it's 4 metrics/criteria at 20% for JUST CKA-only:\n# GSM8K: |0.46|, HumanEval: |0|, MBPP: |1.34|, MATH-500: |1.40|\n# mean = (0.46+0+1.34+1.40)/4 = 0.80, max=1.40 -- doesn't match\n\n# What if the 4 criteria are only the main 3 pruning methods + something else?\n# Let me try Standard, CKA-only, RASP, and Random seed42 (50.57% grpo)\n# need seed42 grpo random from somewhere\nfor eid in ['eval_gsm8k_grpo_random_20_v2', 'eval_gsm8k_grpo_random_20_seed123_v2', 'eval_gsm8k_grpo_random_20_seed456']:\n    if eid in exps:\n        m = exps[eid].get('metrics',{})\n        print(f'{eid}: {m}')\n\n# Check if there's a seed42 random grpo\nfor eid, e in exps.items():\n    if 'random' in eid and 'grpo' in eid.lower() and 'eval' in eid:\n        h = e.get('hypothesis', '')\n        if 'seed42' in h or 'seed=42' in h:\n            m = e.get('metrics', {})\n            print(f'Seed42 random grpo: {eid}: {m}')\n            print(f'  hyp: {h[:200]}')\n\"\n",
  "description": "Check random GRPO seed42 for four-criteria computation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "02d132ab-d966-4306-bdaa-fdead3b71f20",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_011QDEuQeJVBvmfh758rKsvG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1723,
      "cache_read_input_tokens": 68126,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1723,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 34,
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

_source line 118 · 2026-05-24T04:39:05.808Z_

<details><summary>↩ Tool result · `toolu_01KsF7PAnQjMSisiXjt8NAdg`</summary>

```text
eval_gsm8k_grpo_random_20_v2: {'gsm8k_accuracy': 0.5057, 'gsm8k_stderr': 0.0138, 'correct': 667, 'total': 1319, 'eos_rate': 0.9954, 'avg_response_length': 173}
eval_gsm8k_grpo_random_20_seed123_v2: {'accuracy': 0.5072, 'n_correct': 669, 'n_total': 1319, 'stderr': 0.01377, 'eos_rate': 0.9939, 'avg_response_length': 177.9}
eval_gsm8k_grpo_random_20_seed456: {'gsm8k_accuracy': 0.5087, 'gsm8k_accuracy_se': 0.0138, 'gsm8k_correct': 671, 'gsm8k_total': 1319, 'eos_rate': 0.9954, 'avg_response_length': 163.5, 'truncated': 6}
Seed42 random grpo: eval_gsm8k_grpo_random_20_seed123_v2: {'accuracy': 0.5072, 'n_correct': 669, 'n_total': 1319, 'stderr': 0.01377, 'eos_rate': 0.9939, 'avg_response_length': 177.9}
  hyp: MF2 seed123 v2 GSM8K eval (N=1319, greedy, max_new_tokens=2048). 配对 seed42 (50.57%) 和 seed456 (pending). 验证 C1 decoupling 跨 seed 鲁棒性。v1 因 batch_size=1 配置错误作废。
Seed42 random grpo: eval_gsm8k_grpo_random_20_seed456: {'gsm8k_accuracy': 0.5087, 'gsm8k_accuracy_se': 0.0138, 'gsm8k_correct': 671, 'gsm8k_total': 1319, 'eos_rate': 0.9954, 'avg_response_length': 163.5, 'truncated': 6}
  hyp: MF2 seed456 GSM8K eval (N=1319, greedy, max_new_tokens=2048). Paired with seed42 (50.57%) and seed123 v2 (running, interim 52.40%@1000). Validates C1 decoupling robustness across random seeds.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "7043865e-1698-4c81-b5cd-e48c0768b185"
}
```

</details>

---


### System

_source line 119_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2a92311f30a7bab6",
  "tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "description": "Running Search for 4.62 pp SFT-only gap value",
  "usage": {
    "total_tokens": 72687,
    "tool_uses": 33,
    "duration_ms": 370869
  },
  "last_tool_name": "Bash",
  "uuid": "cb45c25d-e63f-4288-9a4a-25138550e807",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db"
}
```

---


### Tool call

_source line 120_

<details open><summary>🔧 Tool call — Bash · `toolu_012T5yeUvZj1Km9777kCa9Lv`</summary>

```json
{
  "command": "FPATH=\"/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt\"\npython3 -c \"\nimport json\nFPATH='$FPATH'\nwith open(FPATH) as f:\n    raw = f.read()\nouter = json.loads(raw)\ndata = json.loads(outer['result'])\nexps = data['data']['experiments']\n\n# The paper mentions 'four fine-grained criteria' likely in the context of a specific table or analysis.\n# Let me search the hypothesis texts for mention of 4.62 or SFT-only gap\nfor eid, e in exps.items():\n    h = e.get('hypothesis', '')\n    m = e.get('metrics', {})\n    mstr = json.dumps(m)\n    if '4.62' in h or '4.62' in mstr or 'sft.only' in h.lower() or 'sft-only' in h.lower():\n        print(f'=== {eid} ===')\n        print(f'  hyp: {h[:400]}')\n        print(f'  metrics: {mstr[:400]}')\n        print()\n\n# Also check what the 'SFT-only gap' means - Standard SFT vs CKA-only SFT?\n# Standard 20% SFT = 59.21%, CKA-only 20% SFT = 63.91%\n# Gap = 63.91 - 59.21 = 4.70 pp (not 4.62)\nprint('CKA-SFT - Std-SFT gap:', round((0.6391 - 0.5921)*100, 2), 'pp')\n# Or CKA-GRPO - Std-SFT? 64.37 - 59.21 = 5.16 pp\n# Or is it between criteria/benchmarks?\n# Maybe across methods at SFT: CKA(63.91) - Standard(59.21) = 4.70\n# Or SFT RASP 20% vs Standard 20%: 61.49 - 59.21 = 2.28\n# What gives 4.62?\n\n# Maybe: Standard GRPO 59.44% vs CKA-only SFT 63.91%? No that makes no sense\n# Or dense=87.87% - CKA-only SFT 63.91% = 23.96\n# Let me check if 4.62 appears in any metric at all\nfor eid, e in exps.items():\n    for field in ['metrics', 'result']:\n        mstr = json.dumps(e.get(field, {}))\n        if '4.62' in mstr:\n            print(f'{eid} ({field}): contains 4.62')\n            print(f'  {mstr[:500]}')\n\"\n",
  "description": "Search for 4.62 pp SFT-only gap value"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "0c00e71b-ba02-4b2f-8518-348f1c73412a",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01CfdiifaXp9zM8PwAh4SAGF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1606,
      "cache_read_input_tokens": 69849,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1606,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 34,
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

_source line 121 · 2026-05-24T04:39:22.578Z_

<details><summary>↩ Tool result · `toolu_012T5yeUvZj1Km9777kCa9Lv`</summary>

```text
CKA-SFT - Std-SFT gap: 4.7 pp
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "acd9338d-8e06-4fef-879e-c9abd4175dde"
}
```

</details>

---


### System

_source line 122_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2a92311f30a7bab6",
  "tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "description": "Running Search for 0.54 mean delta value in registry",
  "usage": {
    "total_tokens": 73641,
    "tool_uses": 34,
    "duration_ms": 378638
  },
  "last_tool_name": "Bash",
  "uuid": "6b50ffdb-3984-4c37-a05a-293ce6fab154",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db"
}
```

---


### Tool call

_source line 123_

<details open><summary>🔧 Tool call — Bash · `toolu_01HJWMch5mNKZWvR2uS478BL`</summary>

```json
{
  "command": "FPATH=\"/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt\"\npython3 -c \"\nimport json\nFPATH='$FPATH'\nwith open(FPATH) as f:\n    raw = f.read()\nouter = json.loads(raw)\ndata = json.loads(outer['result'])\nexps = data['data']['experiments']\n\n# 4.62 pp not found in registry. Let me check other combinations\n# Check all SFT evaluation combinations that could give 4.62 pp\n# CKA-only SFT (20%) - Standard SFT (20%) on GSM8K\n# 63.91 - 59.21 = 4.70 (close but not exactly 4.62)\n# Perhaps using RASP SFT? 61.49 - ...?\n# Or maybe 4.62 is from a different eval set (N=100 westd?):\n# eval_sft_rasp_20_westd_n100: 67%, eval_sft_standard_20_westd_n100: 63%\n# gap = 67 - 63 = 4 pp (not 4.62)\n\n# Let me search hypothesis texts for '0.54' to find what the 4 criteria are\nfor eid, e in exps.items():\n    h = e.get('hypothesis', '')\n    m = e.get('metrics', {})\n    mstr = json.dumps(m)\n    if '0.54' in h or '0.54' in mstr:\n        print(f'=== {eid} ===')\n        print(f'  hyp: {h[:400]}')\n        print(f'  metrics: {mstr[:400]}')\n        print()\n\"\n",
  "description": "Search for 0.54 mean delta value in registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "2449cc23-ff71-4048-8af0-7e2a25c8185e",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0126LbNaEYuH9hh9758trdyz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 895,
      "cache_read_input_tokens": 71455,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 895,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 59,
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

_source line 124 · 2026-05-24T04:39:30.350Z_

<details><summary>↩ Tool result · `toolu_01HJWMch5mNKZWvR2uS478BL`</summary>

```text
=== grpo_rasp_rlvr_20_qwen_math ===
  hyp: Qwen2.5-Math-7B RASP-RLVR 20% post-GRPO (100 steps). RLVR 剪枝后 SFT→GRPO 全管线。对比 grpo_rasp_qwen_math_v3 (regular RASP, reward=0.061) 和 grpo_standard_qwen_math_v3 (Standard, reward=0.044)。D050 ablation: RLVR 是否在 Qwen Math 上提供额外 GRPO 恢复能力。Parent: sft_rasp_rlvr_20_qwen_math.
  metrics: {"clipped_ratio": 0.54, "comparison_vs_rasp_20": "RLVR reward 0.090 > RASP 0.061 (+48%), entropy 0.275 >> 0.073 (3.8x)", "comparison_vs_standard_20": "RLVR reward 0.090 >> Standard 0.044 (+105%)", "entropy_final": 0.275, "frac_zero_std_final": 0.7, "grad_norm_final": 16.125, "kl_final": 0.00581, "kl_spike_recovery": "immediate", "kl_spike_step70": 5756.85, "loss_final": 0.0793, "reward_final": 0.0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "9b43e9ff-b21d-40e8-9bab-84463c0afd30"
}
```

</details>

---


### System

_source line 125_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2a92311f30a7bab6",
  "tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "description": "Running Check 15% sparsity experiments for GRPO-SFT differential",
  "usage": {
    "total_tokens": 74690,
    "tool_uses": 35,
    "duration_ms": 388222
  },
  "last_tool_name": "Bash",
  "uuid": "137bdea2-95e0-4584-b45d-d66b33c0dcf5",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db"
}
```

---


### Tool call

_source line 126_

<details open><summary>🔧 Tool call — Bash · `toolu_01EFs37Wrf9ug8tuxNDg65sZ`</summary>

```json
{
  "command": "FPATH=\"/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt\"\npython3 -c \"\nimport json\nFPATH='$FPATH'\nwith open(FPATH) as f:\n    raw = f.read()\nouter = json.loads(raw)\ndata = json.loads(outer['result'])\nexps = data['data']['experiments']\n\n# Let me check the 15% sparsity experiments for claim #8: GRPO-SFT differential +1.51 pp\n# Standard 15%: SFT=66.49%, GRPO=?\n# CKA-only 15%: SFT=?, GRPO=?\n\n# Standard 15% experiments\nstd15_sft = exps.get('eval_gsm8k_sft_standard_15', {}).get('metrics', {})\nstd15_grpo_v2 = exps.get('eval_gsm8k_grpo_standard_15_v2', {}).get('metrics', {})\nstd15_grpo_s123 = exps.get('eval_gsm8k_grpo_standard_15_seed123_v3', {}).get('metrics', {})\nstd15_grpo_s456 = exps.get('eval_gsm8k_grpo_standard_15_seed456_v3', {}).get('metrics', {})\n\nprint('Standard 15% SFT:', std15_sft)\nprint('Standard 15% GRPO v2:', std15_grpo_v2)\nprint('Standard 15% GRPO seed123:', std15_grpo_s123)\nprint('Standard 15% GRPO seed456:', std15_grpo_s456)\nprint()\n\n# CKA-only 15%\ncka15_sft = exps.get('eval_gsm8k_sft_cka_only_15', {}).get('metrics', {})\ncka15_grpo_v2 = exps.get('eval_gsm8k_grpo_cka_only_15_v2', {}).get('metrics', {})\ncka15_grpo_s123 = exps.get('eval_gsm8k_grpo_cka_only_15_seed123', {}).get('metrics', {})\ncka15_grpo_s456 = exps.get('eval_gsm8k_grpo_cka_only_15_seed456', {}).get('metrics', {})\n\nprint('CKA-only 15% SFT:', cka15_sft)\nprint('CKA-only 15% GRPO v2:', cka15_grpo_v2)\nprint('CKA-only 15% GRPO seed123:', cka15_grpo_s123)\nprint('CKA-only 15% GRPO seed456:', cka15_grpo_s456)\n\"\n",
  "description": "Check 15% sparsity experiments for GRPO-SFT differential"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "39d15b4f-1c7b-421b-a95d-3a1352e22a0a",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01JU4G4nE5UVs2Cwo5Hu5Q4o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 985,
      "cache_read_input_tokens": 72350,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 985,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 64,
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

_source line 127 · 2026-05-24T04:39:39.966Z_

<details><summary>↩ Tool result · `toolu_01EFs37Wrf9ug8tuxNDg65sZ`</summary>

```text
Standard 15% SFT: {'gsm8k_accuracy': 0.6649, 'correct': 877, 'total': 1319, 'eos_rate': 0.993, 'avg_response_length': 183}
Standard 15% GRPO v2: {'gsm8k_accuracy': 0.6611, 'correct': 872, 'total': 1319, 'eos_rate': 0.993, 'avg_response_length': 184}
Standard 15% GRPO seed123: {'accuracy': 0.6513, 'accuracy_se': 0.0131, 'n_correct': 859, 'n_total': 1319, 'eos_rate': 0.9932, 'avg_response_length': 183.25}
Standard 15% GRPO seed456: {'gsm8k_accuracy': 0.6543, 'gsm8k_stderr': 0.0131, 'n_correct': 863, 'n_total': 1319, 'eos_rate': 0.9939, 'avg_response_length': 180.23}

CKA-only 15% SFT: {'gsm8k_accuracy': 0.7218, 'correct': 952, 'total': 1319}
CKA-only 15% GRPO v2: {'gsm8k_accuracy': 0.7309, 'gsm8k_accuracy_ci': 0.0122, 'correct': 964, 'total': 1319, 'eos_rate': 0.9894, 'avg_response_length': 202.4}
CKA-only 15% GRPO seed123: {'accuracy': 73.09, 'n_correct': 964, 'n_total': 1319, 'stderr': 1.22, 'eos_rate': 98.79, 'truncated': 16}
CKA-only 15% GRPO seed456: {'accuracy': 0.721, 'n_correct': 951, 'n_total': 1319, 'stderr': 0.0123, 'eos_rate': 0.9894, 'avg_response_length': 201.94}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "99b9ceab-5074-4c8c-ba47-9a123dfa1d16"
}
```

</details>

---


### System

_source line 128_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2a92311f30a7bab6",
  "tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "description": "Running Compute 15% and 25% sparsity GRPO-SFT differentials",
  "usage": {
    "total_tokens": 76167,
    "tool_uses": 36,
    "duration_ms": 406376
  },
  "last_tool_name": "Bash",
  "uuid": "9903c677-9864-4dd3-9f56-2591bc2c069d",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db"
}
```

---


### Tool call

_source line 129_

<details open><summary>🔧 Tool call — Bash · `toolu_01QmDd6CkRao72Uu2xgt5ars`</summary>

```json
{
  "command": "FPATH=\"/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt\"\npython3 -c \"\nimport json\nFPATH='$FPATH'\nwith open(FPATH) as f:\n    raw = f.read()\nouter = json.loads(raw)\ndata = json.loads(outer['result'])\nexps = data['data']['experiments']\n\n# 15% sparsity deltas:\n# Standard: SFT=66.49%, GRPO(v2)=66.11% -> Delta = -0.38 pp\n# CKA-only: SFT=72.18%, GRPO(v2)=73.09% -> Delta = +0.91 pp\n\nprint('=== 15% sparsity deltas ===')\nprint('Standard 15%: SFT=66.49%, GRPO=66.11%, Delta =', round((0.6611-0.6649)*100, 2), 'pp')\nprint('CKA-only 15%: SFT=72.18%, GRPO=73.09%, Delta =', round((0.7309-0.7218)*100, 2), 'pp')\nprint()\n# Paper claims +1.51 pp for CKA-guided at 15% sparsity - let me check if there's a different pair\n# Maybe using seed456: 72.1% GRPO\n# Or v2 grpo vs sft: 73.09 - 72.18 = 0.91 pp\n# Not 1.51 pp from these numbers.\n\n# Let me check: CKA-only 15% GRPO (seed123) = 73.09% vs SFT = 72.18% -> +0.91 pp\n# Is there another CKA-only SFT 15% eval?\nfor eid, e in exps.items():\n    h = e.get('hypothesis', '')\n    if '15' in eid and 'cka' in eid.lower() and 'sft' in eid.lower():\n        m = e.get('metrics', {})\n        print(f'{eid}: {m}')\n        print(f'  hyp: {h[:200]}')\n        print()\n\n# Also check 25% sparsity\nprint('=== 25% sparsity ===')\ncka25_sft = exps.get('eval_gsm8k_sft_cka_only_25', {}).get('metrics', {})\ncka25_grpo = exps.get('eval_gsm8k_grpo_cka_only_25_v3', {}).get('metrics', {})\nstd25_sft = exps.get('eval_gsm8k_sft_standard_25', {}).get('metrics', {})\nstd25_grpo = exps.get('eval_gsm8k_grpo_standard_25', {}).get('metrics', {})\n\nprint('CKA-only 25% SFT:', cka25_sft)\nprint('CKA-only 25% GRPO v3:', cka25_grpo)\nprint('Standard 25% SFT:', std25_sft)\nprint('Standard 25% GRPO:', std25_grpo)\n\"\n",
  "description": "Compute 15% and 25% sparsity GRPO-SFT differentials"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "8ca1548c-991c-4327-8236-8c0460477d65",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01EpCHk1C9DW9ebvAmk9F13T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1444,
      "cache_read_input_tokens": 73335,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1444,
        "ephemeral_1h_input_tokens": 0
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

_source line 130 · 2026-05-24T04:39:58.101Z_

<details><summary>↩ Tool result · `toolu_01QmDd6CkRao72Uu2xgt5ars`</summary>

```text
=== 15% sparsity deltas ===
Standard 15%: SFT=66.49%, GRPO=66.11%, Delta = -0.38 pp
CKA-only 15%: SFT=72.18%, GRPO=73.09%, Delta = 0.91 pp

eval_gsm8k_sft_cka_only_15: {'gsm8k_accuracy': 0.7218, 'correct': 952, 'total': 1319}
  hyp: GSM8K N=1319 eval on CKA-only 15% SFT checkpoint (pre-GRPO). Fills cross-sparsity comparison table: CKA-only 15% SFT baseline. Compare with Standard 15% SFT (eval_gsm8k_sft_standard_15) to quantify pr

=== 25% sparsity ===
CKA-only 25% SFT: {'gsm8k_accuracy': 0.6012, 'correct': 793, 'n_total': 1319, 'stderr': 0.0135, 'eos_rate': 0.9803, 'avg_response_length': 243.6}
CKA-only 25% GRPO v3: {'gsm8k_accuracy': 0.5959, 'correct': 786, 'n_total': 1319, 'eos_rate': 0.9818}
Standard 25% SFT: {'gsm8k_accuracy': 0.5087, 'stderr': 0.0138, 'correct': 671, 'n_total': 1319, 'eos_rate': 0.953, 'avg_response_length': 333.15}
Standard 25% GRPO: {'gsm8k_accuracy': 0.5186, 'stderr': 0.0138, 'correct': 684, 'n_total': 1319, 'eos_rate': 0.9575, 'avg_response_length': 314.47}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "d6deeb80-619f-4219-9366-d58c01208941"
}
```

</details>

---


### System

_source line 131_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2a92311f30a7bab6",
  "tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "description": "Running Compute all 15-25% sparsity deltas and check 1.51 pp claim",
  "usage": {
    "total_tokens": 77685,
    "tool_uses": 37,
    "duration_ms": 425386
  },
  "last_tool_name": "Bash",
  "uuid": "8aa32a46-af06-4a7a-8f3a-1d8844bf7a37",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db"
}
```

---


### Tool call

_source line 132_

<details open><summary>🔧 Tool call — Bash · `toolu_01CiM9yYVtLKGGtB1nKaKseY`</summary>

```json
{
  "command": "FPATH=\"/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt\"\npython3 -c \"\nimport json\nFPATH='$FPATH'\nwith open(FPATH) as f:\n    raw = f.read()\nouter = json.loads(raw)\ndata = json.loads(outer['result'])\nexps = data['data']['experiments']\n\n# Summary: 15-25% sparsity deltas\nprint('=== Cross-sparsity GRPO-SFT deltas (GSM8K) ===')\nprint('15% CKA-only: SFT=72.18%, GRPO=73.09%, Delta =', round((0.7309-0.7218)*100, 2), 'pp')\nprint('15% Standard: SFT=66.49%, GRPO=66.11%, Delta =', round((0.6611-0.6649)*100, 2), 'pp')\nprint('20% CKA-only: SFT=63.91%, GRPO=64.37%, Delta =', round((0.6437-0.6391)*100, 2), 'pp')\nprint('20% Standard: SFT=59.21%, GRPO=59.44%, Delta =', round((0.5944-0.5921)*100, 2), 'pp')\nprint('20% RASP: SFT=61.49%, GRPO=60.88%, Delta =', round((0.6088-0.6149)*100, 2), 'pp')\nprint('25% CKA-only: SFT=60.12%, GRPO=59.59%, Delta =', round((0.5959-0.6012)*100, 2), 'pp')\nprint('25% Standard: SFT=50.87%, GRPO=51.86%, Delta =', round((0.5186-0.5087)*100, 2), 'pp')\nprint()\n\n# All deltas at 15-25%\ndeltas = [\n    abs(0.7309-0.7218)*100,  # 15% CKA\n    abs(0.6611-0.6649)*100,  # 15% Standard\n    abs(0.6437-0.6391)*100,  # 20% CKA\n    abs(0.5944-0.5921)*100,  # 20% Standard\n    abs(0.6088-0.6149)*100,  # 20% RASP\n    abs(0.5959-0.6012)*100,  # 25% CKA\n    abs(0.5186-0.5087)*100,  # 25% Standard\n]\nprint('All |Delta| at 15-25%:', [round(d,2) for d in deltas])\nprint('Max:', max(deltas))\nprint('All <= 1 pp?', all(d <= 1.0 for d in deltas))\nprint()\n\n# Claim #8: 15% sparsity CKA-guided GRPO-SFT = +1.51 pp\n# Registry shows: +0.91 pp (v2) or +0.91 pp (seed123 70.09 vs SFT 72.18)\n# But wait, there are seed discrepancies\n# seed123 accuracy=73.09 (stored as 73.09%), seed456=72.1% -> mean CKA-only GRPO ~ 73.09 or use mean?\n# All 3 seeds: v2=73.09, seed123=73.09, seed456=72.1 -> mean = 72.76%\n# vs SFT = 72.18% -> Delta = +0.58 pp\n\n# Claim: +1.51 pp. Not matching any single point.\n# Let me check if there's a different SFT checkpoint at 15%\nfor eid, e in exps.items():\n    if '15' in eid and ('sft' in eid.lower() or 'SFT' in eid):\n        m = e.get('metrics', {})\n        h = e.get('hypothesis', '')\n        if 'gsm8k' in json.dumps(m).lower() or 'accuracy' in m:\n            print(f'{eid}: acc={m}')\n            print(f'  hyp: {h[:200]}')\n\"\n",
  "description": "Compute all 15-25% sparsity deltas and check 1.51 pp claim"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "9b96e9a3-8733-42ec-b46c-fca4609758a1",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01TePEnmDenRpETErFjg7mht",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1484,
      "cache_read_input_tokens": 74779,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1484,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 34,
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

_source line 133 · 2026-05-24T04:40:17.080Z_

<details><summary>↩ Tool result · `toolu_01CiM9yYVtLKGGtB1nKaKseY`</summary>

```text
=== Cross-sparsity GRPO-SFT deltas (GSM8K) ===
15% CKA-only: SFT=72.18%, GRPO=73.09%, Delta = 0.91 pp
15% Standard: SFT=66.49%, GRPO=66.11%, Delta = -0.38 pp
20% CKA-only: SFT=63.91%, GRPO=64.37%, Delta = 0.46 pp
20% Standard: SFT=59.21%, GRPO=59.44%, Delta = 0.23 pp
20% RASP: SFT=61.49%, GRPO=60.88%, Delta = -0.61 pp
25% CKA-only: SFT=60.12%, GRPO=59.59%, Delta = -0.53 pp
25% Standard: SFT=50.87%, GRPO=51.86%, Delta = 0.99 pp

All |Delta| at 15-25%: [0.91, 0.38, 0.46, 0.23, 0.61, 0.53, 0.99]
Max: 0.9899999999999909
All <= 1 pp? True

eval_gsm8k_sft_cka_only_15: acc={'gsm8k_accuracy': 0.7218, 'correct': 952, 'total': 1319}
  hyp: GSM8K N=1319 eval on CKA-only 15% SFT checkpoint (pre-GRPO). Fills cross-sparsity comparison table: CKA-only 15% SFT baseline. Compare with Standard 15% SFT (eval_gsm8k_sft_standard_15) to quantify pr
eval_gsm8k_sft_standard_15: acc={'gsm8k_accuracy': 0.6649, 'correct': 877, 'total': 1319, 'eos_rate': 0.993, 'avg_response_length': 183}
  hyp: GSM8K N=1319 eval on Standard 15% SFT checkpoint (pre-GRPO). Establishes SFT baseline accuracy for Standard 15% sparsity. Paired with eval_gsm8k_grpo_standard_15_v2 to measure GRPO recovery delta. Com
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "6e43b347-9591-459d-8da1-ebcb3bca6212"
}
```

</details>

---


### System

_source line 134_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2a92311f30a7bab6",
  "tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "description": "Running Check Qwen2.5-Math-7B cross-architecture N=200 experiments",
  "usage": {
    "total_tokens": 79659,
    "tool_uses": 38,
    "duration_ms": 436611
  },
  "last_tool_name": "Bash",
  "uuid": "3a6cd8c2-8235-42fa-bca9-1882d5ee8316",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db"
}
```

---


### Tool call

_source line 135_

<details open><summary>🔧 Tool call — Bash · `toolu_01GNhkzRbuPbhgbxRS3a2m41`</summary>

```json
{
  "command": "FPATH=\"/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt\"\npython3 -c \"\nimport json\nFPATH='$FPATH'\nwith open(FPATH) as f:\n    raw = f.read()\nouter = json.loads(raw)\ndata = json.loads(outer['result'])\nexps = data['data']['experiments']\n\n# Check Qwen cross-architecture N=200 experiments\nqwen_ids = [\n    'eval_sft_qwen_math_rasp_25',\n    'eval_sft_qwen_math_standard_25',\n    'eval_sft_rasp_qwen_math_n200',\n    'eval_sft_standard_qwen_math_n200',\n    'eval_gsm8k_sft_qwen_cka_only_20',\n    'eval_gsm8k_sft_qwen_standard_20',\n    'eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v3',\n    'eval_math500_sft_qwen_math_cka_only_20',\n]\nfor eid in qwen_ids:\n    if eid in exps:\n        e = exps[eid]\n        m = e.get('metrics', {})\n        h = e.get('hypothesis', '')\n        print(f'{eid}: {json.dumps(m)[:300]}')\n        print(f'  hyp: {h[:200]}')\n        print()\n\n# Check the N=200 Qwen experiments more thoroughly\nfor eid, e in exps.items():\n    h = e.get('hypothesis', '')\n    if 'qwen' in eid.lower() and 'n200' in eid.lower():\n        m = e.get('metrics', {})\n        print(f'{eid}: {json.dumps(m)[:300]}')\n        print(f'  hyp: {h[:200]}')\n        print()\n\"\n",
  "description": "Check Qwen2.5-Math-7B cross-architecture N=200 experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "657bf517-77a8-42f4-8441-221fef553140",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_012EGKwHnNrWVVAaFWtj5iST",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1941,
      "cache_read_input_tokens": 76263,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1941,
        "ephemeral_1h_input_tokens": 0
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

_source line 136 · 2026-05-24T04:40:28.318Z_

<details><summary>↩ Tool result · `toolu_01GNhkzRbuPbhgbxRS3a2m41`</summary>

```text
eval_sft_qwen_math_rasp_25: {"accuracy": 64, "correct": 128, "eos_rate": 0.995, "total": 200}
  hyp: Qwen2.5-Math-7B RASP 25% post-SFT GSM8K eval (N=200, greedy, seed=42). 验证 25% sparsity 下 RASP SFT 恢复质量。对比 Standard 25% 和 20% 结果 (RASP 72.5% vs Standard 71.0%)。Parent: sft_qwen_math_rasp_25.

eval_sft_qwen_math_standard_25: {"accuracy": 63, "correct": 126, "eos_rate": 1, "total": 200}
  hyp: Qwen2.5-Math-7B Standard 25% post-SFT GSM8K eval (N=200, greedy, seed=42). Control for eval_sft_qwen_math_rasp_25。对比 20% 结果 (Standard 71.0%)。Parent: sft_qwen_math_standard_25.

eval_sft_rasp_qwen_math_n200: {"accuracy": 0.725, "avg_len": 121.8, "correct": 145, "eos_rate": 1, "n_total": 200, "stderr": 0.0316}
  hyp: Qwen2.5-Math-7B RASP 20% post-SFT GSM8K eval (N=200, greedy, seed=42). EOS fixed (eos_token_id=[151643,151645]). Cross-model validation. Parent: sft_rasp_20_qwen_math.

eval_sft_standard_qwen_math_n200: {"accuracy": 0.71, "avg_len": 127.7, "correct": 142, "eos_rate": 1, "n_total": 200, "stderr": 0.0321}
  hyp: Qwen2.5-Math-7B Standard 20% post-SFT GSM8K eval (N=200, greedy, seed=42). EOS fixed. Control for eval_sft_rasp_qwen_math_n200. Parent: sft_standard_20_qwen_math.

eval_gsm8k_sft_qwen_cka_only_20: {"gsm8k_accuracy": 0.515, "gsm8k_accuracy_ci": 0.0353, "correct": 103, "total": 200, "eos_rate": 0.27, "avg_response_length": 1536, "truncated": 146, "eval_time": "4h00m04s"}
  hyp: GSM8K N=200 eval of Qwen2.5-Math-7B CKA-only 20% SFT epoch 1 (checkpoint-935). Post-prune accuracy was 1.00% (near zero). CKA-only preserves layer diversity but causes severe initial damage. Fair comp

eval_gsm8k_sft_qwen_standard_20: {"gsm8k_accuracy": 0.21, "correct": 42, "total": 200}
  hyp: GSM8K N=200 eval of Qwen2.5-Math-7B Standard 20% SFT epoch 1 (checkpoint-935). Post-prune accuracy was 18.5%. Standard uses importance-based pruning. Fair comparison with CKA-only at same training poi

eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v3: {"accuracy": 0.486, "correct": 243, "total": 500, "stderr": 0.0224, "truncated_pct": 0.838, "natural_eos_pct": 0.162, "avg_response_length": 1766.5}
  hyp: MF3 cross-architecture validation v3 (N=500, max_new_tokens=2048): Qwen2.5-Math-7B CKA-only 20% GRPO GSM8K eval with absolute model_path fix. v2 crashed due to relative path OSError. v1 killed due to 

eval_math500_sft_qwen_math_cka_only_20: {"accuracy": 0.216, "stderr": 0.0184, "correct": 108, "total": 500, "natural_eos": 90, "truncated": 410, "avg_response_length": 1745.338}
  hyp: Qwen2.5-Math-7B CKA-only 20% SFT MATH-500 eval @2048. Cross-architecture validation: if CKA-only criterion generalizes from DeepSeek-R1-Distill to Qwen-Math on MATH-500. SFT GSM8K = 51.5% (N=200). Pai

eval_sft_standard_qwen_math_n200: {"accuracy": 0.71, "avg_len": 127.7, "correct": 142, "eos_rate": 1, "n_total": 200, "stderr": 0.0321}
  hyp: Qwen2.5-Math-7B Standard 20% post-SFT GSM8K eval (N=200, greedy, seed=42). EOS fixed. Control for eval_sft_rasp_qwen_math_n200. Parent: sft_standard_20_qwen_math.

eval_sft_rasp_qwen_math_n200: {"accuracy": 0.725, "avg_len": 121.8, "correct": 145, "eos_rate": 1, "n_total": 200, "stderr": 0.0316}
  hyp: Qwen2.5-Math-7B RASP 20% post-SFT GSM8K eval (N=200, greedy, seed=42). EOS fixed (eos_token_id=[151643,151645]). Cross-model validation. Parent: sft_rasp_20_qwen_math.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "88dda3d3-f8b7-46b3-abff-b5ecf692911c"
}
```

</details>

---


### System

_source line 137_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2a92311f30a7bab6",
  "tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "description": "Running Check 1.5B scale experiments",
  "usage": {
    "total_tokens": 81890,
    "tool_uses": 39,
    "duration_ms": 448644
  },
  "last_tool_name": "Bash",
  "uuid": "f1e08e37-215b-47b8-8f24-b1fc080acc75",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db"
}
```

---


### Tool call

_source line 138_

<details open><summary>🔧 Tool call — Bash · `toolu_017Kp8NcwcoYaabgTN74G2cY`</summary>

```json
{
  "command": "FPATH=\"/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt\"\npython3 -c \"\nimport json\nFPATH='$FPATH'\nwith open(FPATH) as f:\n    raw = f.read()\nouter = json.loads(raw)\ndata = json.loads(outer['result'])\nexps = data['data']['experiments']\n\n# Check 1.5B scale experiments\nscale_ids = [\n    'eval_gsm8k_grpo_rasp_20_1p5b',\n    'eval_gsm8k_sft_rasp_20_1p5b',\n    'eval_gsm8k_grpo_standard_20_1p5b',\n    'eval_gsm8k_sft_standard_20_1p5b',\n    'eval_gsm8k_grpo_cka_only_20_1p5b',\n    'eval_gsm8k_sft_cka_only_20_1p5b',\n    'eval_humaneval_grpo_cka_only_20_1p5b_2048',\n    'eval_humaneval_sft_cka_only_20_1p5b_2048',\n    'eval_humaneval_grpo_standard_20_1p5b_2048',\n    'eval_humaneval_sft_standard_20_1p5b_2048',\n    'eval_humaneval_sft_rasp_20_1p5b_2048',\n    'eval_math500_sft_standard_20_1p5b',\n]\nfor eid in scale_ids:\n    if eid in exps:\n        e = exps[eid]\n        m = e.get('metrics', {})\n        h = e.get('hypothesis', '')\n        print(f'{eid}: {json.dumps(m)[:300]}')\n        print(f'  hyp: {h[:150]}')\n        print()\n\"\n",
  "description": "Check 1.5B scale experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "d113a563-dc3b-41a8-a353-d088fef3ab5c",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_013wmYZGdP2aPQeuntCt1wMy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2198,
      "cache_read_input_tokens": 78204,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2198,
        "ephemeral_1h_input_tokens": 0
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

_source line 139 · 2026-05-24T04:40:40.343Z_

<details><summary>↩ Tool result · `toolu_017Kp8NcwcoYaabgTN74G2cY`</summary>

```text
eval_gsm8k_grpo_rasp_20_1p5b: {"accuracy": 0.2616, "n_correct": 345, "n_total": 1319, "stderr": 0.0121, "eos_rate": 0.9378, "avg_response_length": 392.7}
  hyp: 1.5B RASP post-GRPO GSM8K accuracy (N=1319). Cross-model generalization: 7B RASP GRPO collapsed (reward 0.01), but 1.5B RASP showed reward=0.099 witho

eval_gsm8k_sft_rasp_20_1p5b: {"accuracy": 0.2691, "n_correct": 355, "n_total": 1319, "stderr": 0.0122, "grpo_delta_pp": -0.75}
  hyp: 1.5B RASP post-SFT GSM8K accuracy (N=1319). SFT baseline for computing GRPO delta on RASP pruning at 1.5B. Compare with GRPO RASP 1.5B (26.16%).

eval_gsm8k_grpo_standard_20_1p5b: {"accuracy": 0.2229, "n_correct": 294, "n_total": 1319, "stderr": 0.0115}
  hyp: Standard GRPO 1.5B (100 steps, reward=0.084) on GSM8K eval: expect low accuracy (~5-10%) given minimal training, serving as baseline for pruned model 

eval_gsm8k_sft_standard_20_1p5b: {"accuracy": 0.22896133434420016, "n_correct": 302, "n_total": 1319}
  hyp: 1.5B Standard post-SFT GSM8K accuracy (N=1319). SFT baseline for computing GRPO delta on Standard pruning at 1.5B scale. Compare with GRPO Standard 1.

eval_gsm8k_grpo_cka_only_20_1p5b: {"accuracy": 0.3548, "n_correct": 468, "n_total": 1319, "stderr": 0.0132}
  hyp: 1.5B CKA-only post-GRPO GSM8K accuracy (N=1319). Cross-model generalization: 7B CKA-only GRPO achieved 64.37% GSM8K. If 1.5B CKA-only GRPO also leads 

eval_gsm8k_sft_cka_only_20_1p5b: {"accuracy": 0.3563, "n_correct": 470, "n_total": 1319, "stderr": 0.0132, "eos_rate": 0.9507, "avg_response_length": 336.76}
  hyp: 1.5B CKA-only post-SFT GSM8K accuracy (N=1319). SFT baseline for computing GRPO delta: if GRPO CKA-only 1.5B GSM8K > SFT CKA-only 1.5B GSM8K, GRPO add

eval_humaneval_grpo_cka_only_20_1p5b_2048: {"pass_at_1": 0, "correct": 0, "total": 164, "stderr": 0}
  hyp: 1.5B GRPO CKA-only HumanEval pass@1 @2048. Cross-scale validation of capability breadth claim. 7B result: pass@1=20.12%. If 1.5B CKA-only also shows s

eval_humaneval_sft_cka_only_20_1p5b_2048: {"pass_at_1": 0.0061, "correct": 1, "total": 164, "stderr": 0.0061}
  hyp: 1.5B SFT CKA-only HumanEval pass@1 @2048. Cross-scale validation of capability breadth claim. 7B SFT CKA-only result: failed (pass@1=0). Testing wheth

eval_humaneval_grpo_standard_20_1p5b_2048: {}
  hyp: 1.5B GRPO Standard HumanEval pass@1 @2048. Cross-scale validation baseline. 7B GRPO Standard HumanEval failed (multiple attempts). If 1.5B Standard al

eval_humaneval_sft_standard_20_1p5b_2048: {"pass_at_1": 0.0061, "correct": 1, "total": 164, "stderr": 0.0061}
  hyp: 1.5B SFT Standard HumanEval pass@1 @2048 on westb. Cross-scale validation of capability breadth claim. Running on westb cuda:0 where checkpoints alrea

eval_humaneval_sft_rasp_20_1p5b_2048: {"pass_at_1": 0, "n_correct": 0, "n_total": 164, "note": "1.5B SFT RASP, all truncated at 2048 tokens"}
  hyp: 1.5B SFT RASP HumanEval pass@1 @2048. Cross-scale validation. 7B GRPO RASP: 10.98%. RASP pruning expected between Standard and CKA-only on code genera

eval_math500_sft_standard_20_1p5b: {"math500_accuracy": 0.054, "correct": 27, "total": 500, "truncated": 335}
  hyp: 1.5B Standard 20% SFT MATH-500 @2048. Cross-scale comparison with CKA-only 1.5B (10.6%) to test if CKA-guided pruning advantage is scale-invariant.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "e675fa03-3fe7-402b-baf8-fed7253f9b8d"
}
```

</details>

---


### System

_source line 140_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2a92311f30a7bab6",
  "tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "description": "Running Check MATH-500 fixed eval experiments",
  "usage": {
    "total_tokens": 84055,
    "tool_uses": 40,
    "duration_ms": 460816
  },
  "last_tool_name": "Bash",
  "uuid": "a05aa57d-dd20-4235-9e99-c21a564973a0",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db"
}
```

---


### Tool call

_source line 141_

<details open><summary>🔧 Tool call — Bash · `toolu_019B3DaUsKBPnhuv2HjW98qA`</summary>

```json
{
  "command": "FPATH=\"/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt\"\npython3 -c \"\nimport json\nFPATH='$FPATH'\nwith open(FPATH) as f:\n    raw = f.read()\nouter = json.loads(raw)\ndata = json.loads(outer['result'])\nexps = data['data']['experiments']\n\n# Check MATH-500 fixed eval experiments (claim #17)\nmath500_fixed_ids = [\n    'eval_math500_sft_rasp_alpha2p0_20_fixed',\n    'eval_math500_grpo_rasp_alpha2p0_20_fixed',\n    'eval_math500_grpo_cka_only_20_fixed',\n    'eval_math500_sft_cka_only_20_fixed_v2',\n    'eval_math500_grpo_rasp_alpha1p0_20_fixed',\n    'eval_math500_sft_rasp_alpha1p0_20_fixed',\n    'eval_math500_grpo_standard_20_fixed',\n]\nprint('=== MATH-500 Fixed Eval Experiments ===')\nfor eid in math500_fixed_ids:\n    if eid in exps:\n        e = exps[eid]\n        m = e.get('metrics', {})\n        h = e.get('hypothesis', '')\n        print(f'{eid}: {json.dumps(m)[:300]}')\n        print(f'  hyp: {h[:200]}')\n        print()\n    else:\n        print(f'{eid}: NOT FOUND')\n\n# Also look for any MATH-500 experiments with 'fixed' in the name\nfor eid, e in exps.items():\n    if 'math500' in eid.lower() and 'fixed' in eid.lower():\n        m = e.get('metrics', {})\n        print(f'FIXED: {eid}: {json.dumps(m)[:300]}')\n        print()\n\"\n",
  "description": "Check MATH-500 fixed eval experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "e568641b-8d8f-4baa-b8f5-572986fb55cc",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_016Z3LshDboBkdiAH4vUTcLt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2132,
      "cache_read_input_tokens": 80402,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2132,
        "ephemeral_1h_input_tokens": 0
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

_source line 142 · 2026-05-24T04:40:52.512Z_

<details><summary>↩ Tool result · `toolu_019B3DaUsKBPnhuv2HjW98qA`</summary>

```text
=== MATH-500 Fixed Eval Experiments ===
eval_math500_sft_rasp_alpha2p0_20_fixed: {"accuracy": 0.256, "n_correct": 128, "n_total": 500, "stderr": 0.01952, "truncated": 155, "natural_eos": 345, "truncated_pct": 0.31, "avg_response_length": 805.754}
  hyp: SFT RASP α=2.0 20% MATH-500 with fixed eval script. Model on westd (sft_rasp_alpha2p0_20). P1 dose-response table.

eval_math500_grpo_rasp_alpha2p0_20_fixed: {"accuracy": 0.274, "n_correct": 137, "n_total": 500, "truncated_pct": 0.302, "truncated": 151, "natural_eos": 349}
  hyp: GRPO RASP α=2.0 20% MATH-500 with fixed eval script. Model on westd (grpo_rasp_alpha2p0_20). P1 dose-response table.

eval_math500_grpo_cka_only_20_fixed: {"accuracy": 0.276, "n_correct": 138, "n_total": 500, "stderr": 0.02}
  hyp: GRPO CKA-only 20% MATH-500 with fixed eval script. Model on westb (grpo_cka_only_20/checkpoint-100). P0 method comparison.

eval_math500_sft_cka_only_20_fixed_v2: {"accuracy": 0.274, "num_correct": 137, "num_total": 500, "stderr": 0.02, "truncated_pct": 0.232}
  hyp: SFT CKA-only 20% MATH-500 with fixed eval script. Retry on westb (checkpoint location). Replaces buggy NEW result (26.8%) with consistent scoring.

eval_math500_grpo_rasp_alpha1p0_20_fixed: {"accuracy": 0.23, "n_correct": 115, "n_total": 500, "stderr": 0.0188, "natural_eos": 320, "truncated": 180, "avg_response_length": 903.536}
  hyp: GRPO RASP α=1.0 20% MATH-500 with fixed eval script. Replaces buggy NEW result (22.6%) with consistent scoring.

eval_math500_sft_rasp_alpha1p0_20_fixed: {"accuracy": 0.216, "num_correct": 108, "num_total": 500}
  hyp: SFT RASP α=1.0 20% MATH-500 with fixed eval script. Replaces buggy NEW result (21.2%) with consistent scoring.

eval_math500_grpo_standard_20_fixed: {"math500_acc": 0.27, "math500_correct": 135, "math500_total": 500, "math500_stderr": 0.0199, "natural_eos": 278, "truncated": 222, "avg_response_length": 1127.844}
  hyp: GRPO Standard 20% MATH-500 with fixed eval script. Replaces OLD v2 (26.4%) with consistently-scored result across all methods.

FIXED: eval_math500_sft_rasp_alpha2p0_20_fixed: {"accuracy": 0.256, "n_correct": 128, "n_total": 500, "stderr": 0.01952, "truncated": 155, "natural_eos": 345, "truncated_pct": 0.31, "avg_response_length": 805.754}

FIXED: eval_math500_grpo_rasp_alpha2p0_20_fixed: {"accuracy": 0.274, "n_correct": 137, "n_total": 500, "truncated_pct": 0.302, "truncated": 151, "natural_eos": 349}

FIXED: eval_math500_grpo_cka_only_25_fixed: {"accuracy": 0.176, "n_correct": 88, "n_total": 500, "stderr": 0.017, "natural_eos": 367, "truncated": 133, "truncated_pct": 0.266, "avg_response_length": 719.35}

FIXED: eval_math500_grpo_cka_only_20_fixed: {"accuracy": 0.276, "n_correct": 138, "n_total": 500, "stderr": 0.02}

FIXED: eval_math500_grpo_standard_20_fixed: {"math500_acc": 0.27, "math500_correct": 135, "math500_total": 500, "math500_stderr": 0.0199, "natural_eos": 278, "truncated": 222, "avg_response_length": 1127.844}

FIXED: eval_math500_grpo_rasp_alpha1p0_20_fixed: {"accuracy": 0.23, "n_correct": 115, "n_total": 500, "stderr": 0.0188, "natural_eos": 320, "truncated": 180, "avg_response_length": 903.536}

FIXED: eval_math500_sft_cka_only_20_fixed_v2: {"accuracy": 0.274, "num_correct": 137, "num_total": 500, "stderr": 0.02, "truncated_pct": 0.232}

FIXED: eval_math500_sft_rasp_alpha1p0_20_fixed: {"accuracy": 0.216, "num_correct": 108, "num_total": 500}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "b910dd06-c717-4cce-a6da-5e0f053bf1a1"
}
```

</details>

---


### System

_source line 143_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2a92311f30a7bab6",
  "tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "description": "Running Compare old vs fixed MATH-500 eval values",
  "usage": {
    "total_tokens": 86211,
    "tool_uses": 41,
    "duration_ms": 475856
  },
  "last_tool_name": "Bash",
  "uuid": "0f06c3c5-a56f-4d3b-b61b-896453d1ecf8",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db"
}
```

---


### Tool call

_source line 144_

<details open><summary>🔧 Tool call — Bash · `toolu_01Gj7LE43TuQAQboyB4W8aCS`</summary>

```json
{
  "command": "FPATH=\"/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt\"\npython3 -c \"\nimport json\nFPATH='$FPATH'\nwith open(FPATH) as f:\n    raw = f.read()\nouter = json.loads(raw)\ndata = json.loads(outer['result'])\nexps = data['data']['experiments']\n\n# Check all MATH-500 unfixed vs fixed to show old vs new values (claim #17)\nprint('=== MATH-500 Old vs New (Fixed) Eval ===')\n# CKA-only 20%\nold_cka = exps.get('eval_math500_grpo_cka_only_20_2048', {}).get('metrics', {})\nold_cka_v2 = exps.get('eval_math500_grpo_cka_only_20_2048_v2', {}).get('metrics', {})\nfixed_cka = exps.get('eval_math500_grpo_cka_only_20_fixed', {}).get('metrics', {})\nprint('CKA-only GRPO 20%:')\nprint('  OLD (2048):', old_cka)\nprint('  OLD v2 (2048):', old_cka_v2)\nprint('  FIXED:', fixed_cka)\n\n# Standard 20%\nold_std = exps.get('eval_math500_grpo_standard_20_fair_v2', {}).get('metrics', {})\nfixed_std = exps.get('eval_math500_grpo_standard_20_fixed', {}).get('metrics', {})\nprint('Standard GRPO 20%:')\nprint('  OLD:', old_std)\nprint('  FIXED:', fixed_std)\n\n# SFT CKA-only 20%\nold_sft_cka = exps.get('eval_math500_sft_cka_only_20_v4_restart', {}).get('metrics', {})\nfixed_sft_cka = exps.get('eval_math500_sft_cka_only_20_fixed_v2', {}).get('metrics', {})\nprint('CKA-only SFT 20%:')\nprint('  OLD:', old_sft_cka)\nprint('  FIXED:', fixed_sft_cka)\n\n# RASP alpha=2.0\nold_rasp_a2_sft = exps.get('eval_math500_sft_rasp_alpha2p0_20', {}).get('metrics', {})\nfixed_rasp_a2_sft = exps.get('eval_math500_sft_rasp_alpha2p0_20_fixed', {}).get('metrics', {})\nold_rasp_a2_grpo = exps.get('eval_math500_grpo_rasp_alpha2p0_20', {}).get('metrics', {})\nfixed_rasp_a2_grpo = exps.get('eval_math500_grpo_rasp_alpha2p0_20_fixed', {}).get('metrics', {})\nprint('RASP alpha=2.0 SFT:')\nprint('  OLD:', old_rasp_a2_sft)\nprint('  FIXED:', fixed_rasp_a2_sft)\nprint('RASP alpha=2.0 GRPO:')\nprint('  OLD:', old_rasp_a2_grpo)\nprint('  FIXED:', fixed_rasp_a2_grpo)\n\"\n",
  "description": "Compare old vs fixed MATH-500 eval values"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "d0c258f2-2c06-46dc-bf1f-69067ea7f229",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_013UdsP8vWZCnguyzqwp6CAZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2123,
      "cache_read_input_tokens": 82534,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2123,
        "ephemeral_1h_input_tokens": 0
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

_source line 145 · 2026-05-24T04:41:07.637Z_

<details><summary>↩ Tool result · `toolu_01Gj7LE43TuQAQboyB4W8aCS`</summary>

```text
=== MATH-500 Old vs New (Fixed) Eval ===
CKA-only GRPO 20%:
  OLD (2048): {'accuracy': 0.292, 'n_correct': 146, 'n_total': 500}
  OLD v2 (2048): {'accuracy': 0.274, 'correct': 137, 'total': 500, 'stderr': 0.01995, 'natural_eos': 390, 'truncated': 110, 'avg_response_length': 654.746}
  FIXED: {'accuracy': 0.276, 'n_correct': 138, 'n_total': 500, 'stderr': 0.02}
Standard GRPO 20%:
  OLD: {'accuracy': 0.264, 'n_correct': 132, 'n_total': 500, 'stderr': 0.0197}
  FIXED: {'math500_acc': 0.27, 'math500_correct': 135, 'math500_total': 500, 'math500_stderr': 0.0199, 'natural_eos': 278, 'truncated': 222, 'avg_response_length': 1127.844}
CKA-only SFT 20%:
  OLD: {'accuracy': 0.29, 'n_correct': 145, 'n_total': 500, 'stderr': 0.0203, 'natural_eos': 384, 'truncated': 116, 'natural_eos_pct': 0.768, 'avg_response_length': 673.278, 'median_response_length': 242.5}
  FIXED: {'accuracy': 0.274, 'num_correct': 137, 'num_total': 500, 'stderr': 0.02, 'truncated_pct': 0.232}
RASP alpha=2.0 SFT:
  OLD: {'accuracy': 0.24, 'correct': 120, 'total': 500, 'truncated': 155, 'stderr': 0.0191}
  FIXED: {'accuracy': 0.256, 'n_correct': 128, 'n_total': 500, 'stderr': 0.01952, 'truncated': 155, 'natural_eos': 345, 'truncated_pct': 0.31, 'avg_response_length': 805.754}
RASP alpha=2.0 GRPO:
  OLD: {'accuracy': 0.262, 'correct': 131, 'total': 500, 'stderr': 0.0197, 'natural_eos': 349, 'truncated': 151, 'avg_response_length': 785.326}
  FIXED: {'accuracy': 0.274, 'n_correct': 137, 'n_total': 500, 'truncated_pct': 0.302, 'truncated': 151, 'natural_eos': 349}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "cc170d24-76b4-4cbf-b99f-3ee3aa911e93"
}
```

</details>

---


### System

_source line 146_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2a92311f30a7bab6",
  "tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "description": "Running Search for 1.51 pp claim in registry",
  "usage": {
    "total_tokens": 88034,
    "tool_uses": 42,
    "duration_ms": 486359
  },
  "last_tool_name": "Bash",
  "uuid": "965723bc-5740-4c28-a2da-cdeee066d98e",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db"
}
```

---


### Tool call

_source line 147_

<details open><summary>🔧 Tool call — Bash · `toolu_016k5TmvE9K7g5Y2VnWfkHH5`</summary>

```json
{
  "command": "FPATH=\"/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt\"\npython3 -c \"\nimport json\nFPATH='$FPATH'\nwith open(FPATH) as f:\n    raw = f.read()\nouter = json.loads(raw)\ndata = json.loads(outer['result'])\nexps = data['data']['experiments']\n\n# Let me search for '1.51' in the registry\nfor eid, e in exps.items():\n    h = e.get('hypothesis', '')\n    m = e.get('metrics', {})\n    mstr = json.dumps(m)\n    if '1.51' in h or '1.51' in mstr:\n        print('=== ' + eid + ' ===')\n        print('  hyp:', h[:300])\n        print('  metrics:', mstr[:300])\n        print()\n\n# Also search for any claim about 'CKA-guided' or CKA advantage at 15%\nfor eid, e in exps.items():\n    h = e.get('hypothesis', '')\n    if '15' in h and ('1.51' in h or 'advantage' in h.lower() or 'gap' in h.lower()):\n        print('=== ' + eid + ' ===')\n        print('  hyp:', h[:300])\n\"\n",
  "description": "Search for 1.51 pp claim in registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "4790920f-a3dc-46c4-b97c-d3609b192317",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01XZYFaBbu7MF2Gatk36c99L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1790,
      "cache_read_input_tokens": 84657,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1790,
        "ephemeral_1h_input_tokens": 0
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

_source line 148 · 2026-05-24T04:41:18.063Z_

<details><summary>↩ Tool result · `toolu_016k5TmvE9K7g5Y2VnWfkHH5`</summary>

```text
=== grpo_cka_only_25 ===
  hyp: CKA-only 25% GRPO training (v5 fair config, 100 steps, lr=1e-6, beta=0.01, T=0.4, seed=42). Cross-sparsity comparison: Standard 25%=51.1%, RASP 25%=53.15%. Tests if CKA-guided pruning advantage holds at 25%.
=== eval_gsm8k_grpo_cka_only_15_seed123 ===
  hyp: GSM8K N=1319 eval on CKA-only 15% GRPO seed123. Multi-seed validation for 15% sparsity gap statistical significance.
=== eval_gsm8k_grpo_cka_only_15_seed456 ===
  hyp: GSM8K N=1319 eval on CKA-only 15% GRPO seed456. Multi-seed validation for 15% sparsity gap statistical significance.
=== eval_postprune_standard_30 ===
  hyp: Standard 30% post-prune GSM8K accuracy (N=200). At 20% Standard post-prune was 17.5%, at 25% was ~15%. 30% should show further degradation. Compared with RASP 30% post-prune (running) to verify RASP advantage persists at higher sparsity. Extends multi-sparsity degradation curve.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "090cb5c7-c46f-4b86-8c6c-be84e051af51"
}
```

</details>

---


### System

_source line 149_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2a92311f30a7bab6",
  "tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "description": "Running Investigate the 1.51 pp claim more deeply",
  "usage": {
    "total_tokens": 88945,
    "tool_uses": 43,
    "duration_ms": 508314
  },
  "last_tool_name": "Bash",
  "uuid": "d861596d-52f2-4ad5-85a2-6aab66846d5d",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db"
}
```

---


### Tool call

_source line 150_

<details open><summary>🔧 Tool call — Bash · `toolu_01Jwtcvs4vjFT2uCAN7V83on`</summary>

```json
{
  "command": "FPATH=\"/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt\"\npython3 -c \"\nimport json\nFPATH='$FPATH'\nwith open(FPATH) as f:\n    raw = f.read()\nouter = json.loads(raw)\ndata = json.loads(outer['result'])\nexps = data['data']['experiments']\n\n# Let me look for the Standard 15% GRPO vs CKA-only 15% GRPO gap (not the SFT-GRPO delta but the method gap)\n# This might be the 1.51 pp claim\n# CKA-only 15% GRPO = 73.09% (seed42)\n# Standard 15% GRPO = 66.11% (seed42)\n# Gap = 73.09 - 66.11 = 6.98 pp\n\n# Or perhaps looking at GRPO - SFT for CKA-only: 73.09 - 72.18 = 0.91 pp\n# Or CKA-only GRPO mean (3 seeds): (73.09 + 73.09 + 72.10) / 3 = 72.76\n# SFT = 72.18 -> delta = 72.76 - 72.18 = 0.58 pp\n\n# Or checking if there's a per-seed delta for CKA-only 15%:\n# seed42 GRPO = 73.09% vs SFT = 72.18% -> +0.91\n# seed123 GRPO = 73.09% vs SFT = 72.18% -> +0.91\n# seed456 GRPO = 72.10% vs SFT = 72.18% -> -0.08\n\n# The claim +1.51 doesn't match any single registry value. Let me search for it differently.\n# Maybe it's CKA-only 15% GRPO minus Standard 15% GRPO divided by something\n# Or maybe the decoupling table has a note about 1.51 pp\n\n# Check if there's a pass@k result or something else\nfor eid, e in exps.items():\n    h = e.get('hypothesis', '')\n    if '1.51' in h:\n        print('Found 1.51 in hypothesis of:', eid)\n        print('  hyp:', h[:400])\n        print()\n\n# Check if the experiment for eval_sft_rasp_20_westd_n100 or westd has 1.51\nfor eid in ['eval_sft_rasp_20_westd_n100', 'eval_sft_standard_20_westd_n100']:\n    if eid in exps:\n        m = exps[eid].get('metrics', {})\n        print(eid, m)\nprint()\n\n# OK let me check if maybe 1.51 comes from comparing CKA-only 15% GRPO (73.09) vs Standard GRPO 15% seed42 (66.11)\n# CKA advantage over Standard = +6.98 pp\n# Or CKA-only GRPO - SFT at 15% = +0.91 pp\n# Standard GRPO - SFT at 15% = -0.38 pp\n# CKA - Standard gap in GRPO-SFT deltas: 0.91 - (-0.38) = 1.29 pp? Not 1.51\n\n# Maybe: (CKA-only GRPO delta) - (Standard GRPO delta) = 0.91 - (-0.38) = 1.29 pp\nprint('CKA minus Standard delta at 15%:', 0.91 - (-0.38), 'pp')\n# No. What if using seed means?\n# CKA mean = (0.91 + 0.91 + (-0.08)) / 3 = 0.58 pp\n# Std mean = (v2: -0.38, seed123: ?, seed456: ?)\n# Let me check standard 15% GRPO seed values vs SFT\nstd15_s123 = exps.get('eval_gsm8k_grpo_standard_15_seed123_v3', {}).get('metrics', {})\nstd15_s456 = exps.get('eval_gsm8k_grpo_standard_15_seed456_v3', {}).get('metrics', {})\nprint('Standard 15% GRPO seed123:', std15_s123)\nprint('Standard 15% GRPO seed456:', std15_s456)\n# SFT = 66.49%\nstd15_deltas = [round((0.6611-0.6649)*100,2), round((0.6513-0.6649)*100,2), round((0.6543-0.6649)*100,2)]\ncka15_deltas = [round((0.7309-0.7218)*100,2), round((0.7309-0.7218)*100,2), round((0.7210-0.7218)*100,2)]\nprint('Standard 15% GRPO-SFT deltas per seed:', std15_deltas)\nprint('CKA-only 15% GRPO-SFT deltas per seed:', cka15_deltas)\nprint('Mean CKA delta:', round(sum(cka15_deltas)/3,2))\nprint('Mean Std delta:', round(sum(std15_deltas)/3,2))\nprint('CKA mean - Std mean:', round(sum(cka15_deltas)/3 - sum(std15_deltas)/3, 2))\n\"\n",
  "description": "Investigate the 1.51 pp claim more deeply"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "511ff1d6-182f-468e-be2d-127f9c2745c6",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RcPsz3F2MhY5U4WHfkuarv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 853,
      "cache_read_input_tokens": 86447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 853,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 58,
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

_source line 151 · 2026-05-24T04:41:40.034Z_

<details><summary>↩ Tool result · `toolu_01Jwtcvs4vjFT2uCAN7V83on`</summary>

```text
eval_sft_rasp_20_westd_n100 {'accuracy': 0.67, 'avg_len': 182.39, 'eos_rate': 0.99, 'n_correct': 67, 'n_total': 100, 'stderr': 0.047}
eval_sft_standard_20_westd_n100 {'accuracy': 0.63, 'avg_len': 260.57, 'eos_rate': 0.97, 'n_correct': 63, 'n_total': 100, 'stderr': 0.048}

CKA minus Standard delta at 15%: 1.29 pp
Standard 15% GRPO seed123: {'accuracy': 0.6513, 'accuracy_se': 0.0131, 'n_correct': 859, 'n_total': 1319, 'eos_rate': 0.9932, 'avg_response_length': 183.25}
Standard 15% GRPO seed456: {'gsm8k_accuracy': 0.6543, 'gsm8k_stderr': 0.0131, 'n_correct': 863, 'n_total': 1319, 'eos_rate': 0.9939, 'avg_response_length': 180.23}
Standard 15% GRPO-SFT deltas per seed: [-0.38, -1.36, -1.06]
CKA-only 15% GRPO-SFT deltas per seed: [0.91, 0.91, -0.08]
Mean CKA delta: 0.58
Mean Std delta: -0.93
CKA mean - Std mean: 1.51
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "d292e368-9810-4df8-9e05-e599277e0b9c"
}
```

</details>

---


### System

_source line 152_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2a92311f30a7bab6",
  "tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "description": "Running Investigate different combinations to get mean=0.54 and max=0.61",
  "usage": {
    "total_tokens": 90936,
    "tool_uses": 44,
    "duration_ms": 544522
  },
  "last_tool_name": "Bash",
  "uuid": "9e4d6f4e-739e-4458-b129-d6c6fa5a85c2",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db"
}
```

---


### Tool call

_source line 153_

<details open><summary>🔧 Tool call — Bash · `toolu_01GU62xw4BfotwdYKstbmWd6`</summary>

```json
{
  "command": "FPATH=\"/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt\"\npython3 -c \"\nimport json\nFPATH='$FPATH'\nwith open(FPATH) as f:\n    raw = f.read()\nouter = json.loads(raw)\ndata = json.loads(outer['result'])\nexps = data['data']['experiments']\n\n# Now let's figure out the 'four fine-grained criteria' for claim #2 (mean=0.54 pp)\n# The paper seems to be about the main 20% sparsity result, comparing across 3 main methods\n# Perhaps it's across the 3 main pruning methods on GSM8K:\n# Standard(+0.23), CKA-only(+0.46), RASP(-0.61)\n# But those are only 3, not 4\n# And mean = (0.23+0.46+0.61)/3 = 0.43, max=0.61\n\n# Maybe the 4th is Random: Standard(+0.23), CKA-only(+0.46), RASP(-0.61), Random(-0.68)\n# mean = (0.23+0.46+0.61+0.68)/4 = 0.495, max=0.68\n\n# Or maybe the paper's 'four criteria' refers to Multi-seed analysis:\n# CKA-only seeds: seed42=+0.46, seed123=+0.31 (64.22-63.91), seed456=+0.68 (64.59-63.91)\n# But that's only 3 and about 1 method\n\n# Let me look at it differently. The numbers mean=0.54, max=0.61\n# max=0.61 matches RASP at 20% (Delta=-0.61)\n# For mean to be 0.54: we need values averaging to 0.54\n# If 4 values sum to 4*0.54=2.16\n# max is 0.61 (RASP)\n# So other 3 must sum to 2.16-0.61=1.55 and each <= 0.61\n# Possible: CKA-only seed42(0.46), seed123(0.31), seed456(0.68)? No, seed456=0.68 > 0.61\n# Or maybe using 4 benchmarks for CKA-only method:\n# GSM8K(0.46), HumanEval(0), MBPP(1.34), MATH-500(1.40) -> mean=0.80, max=1.40\n\n# The numbers 0.54 and 0.61 only work cleanly for 3 numbers with max=RASP(0.61):\n# If only Standard, CKA-only, RASP: mean=(0.23+0.46+0.61)/3=0.43 \n# But paper says 'four' -- maybe adding another method like depth-first or unstructured?\n\n# Check if maybe it's SFT-only across 4 methods (without random):\n# Standard SFT alone: 59.21%\n# CKA-only SFT alone: 63.91%\n# RASP SFT alone: 61.49%\n# Random SFT alone: 51.25%\n# 'SFT-only gap' (SFT-only improvement at 20% vs dense 87.87%):\n# Standard: 87.87-59.21=28.66\n# CKA-only: 87.87-63.91=23.96\n# RASP: 87.87-61.49=26.38\n\n# Let me try: the 4 criteria might be the 4 alpha values (dose-response)\n# But we computed those: 0.45, 1.14, 0.69, 0.83 -> mean=0.78, max=1.14\n\n# The most natural reading of 'four fine-grained criteria at 20% sparsity on GSM8K'\n# with mean=0.54 and max=0.61 is:\n# If we use multi-seed for RASP+Standard+CKA-only (but RASP collapses, only fair v2 works)\n# Let me check if there's an averaging that gives 0.54\n\n# Trying: Standard(0.23), CKA-only seed42(0.46), CKA-only seed123(0.31), RASP(0.61)\nvals = [0.23, 0.46, 0.31, 0.61]\nprint('Option A: Std+CKA_s42+CKA_s123+RASP:')\nprint('  values:', vals, '-> mean:', round(sum(vals)/len(vals),2), 'max:', max(vals))\nprint()\n\n# Trying: Std seed42(0.23), CKA seed42(0.46), CKA seed123(0.31), CKA seed456(0.68)\nvals2 = [0.23, 0.46, 0.31, 0.68]\nprint('Option B: Std+CKA_s42+CKA_s123+CKA_s456:')\nprint('  values:', vals2, '-> mean:', round(sum(vals2)/len(vals2),2), 'max:', max(vals2))\nprint()\n\n# Trying: Standard 3 seeds vs CKA-only 1\n# Std s42(+0.23), Std s123(+0.68), Std s456(+1.09), CKA(+0.46)\nstd_s123 = 0.5989 - 0.5921  # 0.0068 -> 0.68 pp\nstd_s456 = 0.6020 - 0.5921  # 0.0099 -> 0.99 pp\ncka_s123 = 0.6422 - 0.6391  # 0.31 pp\ncka_s456 = 0.6459 - 0.6391  # 0.68 pp\nprint('Std s42:', round(0.23,2), 'Std s123:', round(std_s123*100,2), 'Std s456:', round(std_s456*100,2))\nprint('CKA s42:', 0.46, 'CKA s123:', round(cka_s123*100,2), 'CKA s456:', round(cka_s456*100,2))\nprint()\n\n# 4 values: CKA s42(0.46), CKA s123(0.31), CKA s456(0.68), RASP(0.61) -> mean=0.515 \nvals3 = [0.46, 0.31, 0.68, 0.61]\nprint('Option C: CKA 3 seeds + RASP:')\nprint('  values:', vals3, '-> mean:', round(sum(vals3)/len(vals3),2), 'max:', max(vals3))\nprint()\n\n# GSM8K only 4 main methods: Std(0.23), CKA(0.46), RASP(0.61), Random(-0.68)\n# mean = (0.23+0.46+0.61+0.68)/4 = 0.495\n# Not 0.54 either\n\"\n",
  "description": "Investigate different combinations to get mean=0.54 and max=0.61"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "a8d258ae-2f12-48f5-b78a-4d387fb02493",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01PEU5Lmaq4RZaRxnRXRY3UP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1989,
      "cache_read_input_tokens": 87300,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1989,
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

_source line 154 · 2026-05-24T04:42:16.343Z_

<details><summary>↩ Tool result · `toolu_01GU62xw4BfotwdYKstbmWd6`</summary>

```text
Option A: Std+CKA_s42+CKA_s123+RASP:
  values: [0.23, 0.46, 0.31, 0.61] -> mean: 0.4 max: 0.61

Option B: Std+CKA_s42+CKA_s123+CKA_s456:
  values: [0.23, 0.46, 0.31, 0.68] -> mean: 0.42 max: 0.68

Std s42: 0.23 Std s123: 0.68 Std s456: 0.99
CKA s42: 0.46 CKA s123: 0.31 CKA s456: 0.68

Option C: CKA 3 seeds + RASP:
  values: [0.46, 0.31, 0.68, 0.61] -> mean: 0.52 max: 0.68
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "010ad4c6-d8ec-4f6a-93ae-a91cc1841b68"
}
```

</details>

---


### System

_source line 155_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2a92311f30a7bab6",
  "tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "description": "Running Check pass@k8 evaluation experiments",
  "usage": {
    "total_tokens": 93243,
    "tool_uses": 45,
    "duration_ms": 555521
  },
  "last_tool_name": "Bash",
  "uuid": "84413529-c4bd-483a-9a3d-c2f44d06c1e6",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db"
}
```

---


### Tool call

_source line 156_

<details open><summary>🔧 Tool call — Bash · `toolu_01W3vsoVWwmYFkqkjookTikP`</summary>

```json
{
  "command": "FPATH=\"/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt\"\npython3 -c \"\nimport json\nFPATH='$FPATH'\nwith open(FPATH) as f:\n    raw = f.read()\nouter = json.loads(raw)\ndata = json.loads(outer['result'])\nexps = data['data']['experiments']\n\n# Let me check if there's a 'pass_k8' or per-question eval or rubric scoring \nfor eid in ['eval_pass_k8_rasp_20_grpo_deepseek', 'eval_pass_k8_rasp_20_grpo_qwen_math', \n            'eval_pass_k8_rasp_20_sft_qwen_math', 'eval_pass_k8_standard_20_grpo_deepseek',\n            'eval_pass_k8_standard_20_grpo_qwen_math_v2', 'eval_pass_k8_unpruned_qwen_math']:\n    if eid in exps:\n        e = exps[eid]\n        m = e.get('metrics', {})\n        h = e.get('hypothesis', '')\n        print(f'{eid}: {json.dumps(m)[:500]}')\n        print(f'  hyp: {h[:200]}')\n        print()\n\"\n",
  "description": "Check pass@k8 evaluation experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "b93d3d6a-23dd-4c48-8122-dea8e2065199",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01X1xDdsHiSXYgzsszkSXSHN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2274,
      "cache_read_input_tokens": 89289,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2274,
        "ephemeral_1h_input_tokens": 0
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

_source line 157 · 2026-05-24T04:42:27.221Z_

<details><summary>↩ Tool result · `toolu_01W3vsoVWwmYFkqkjookTikP`</summary>

```text
eval_pass_k8_rasp_20_grpo_deepseek: {"n_problems": 200, "pass_k8": 0.89, "temperature": 0.7}
  hyp: DeepSeek-R1-Distill-Qwen-7B RASP 20% post-GRPO pass@k=8 (N=200, T=0.7, seed=42). C1 diversity 验证：RASP collapse 模型的 sampling diversity。构建 pass@k 2×2 矩阵。Parent: grpo_stage2_rasp_20_v9.

eval_pass_k8_rasp_20_grpo_qwen_math: {"accuracy": 0.915, "k": 8, "n_samples": 200, "pass_at_k": 0.915, "stderr": 0.0197, "temperature": 0.7}
  hyp: RASP 20% post-GRPO on Qwen Math shows pass@8 below unpruned baseline, indicating GRPO fails to recover full solution diversity on structurally pruned models (C1 diversity)

eval_pass_k8_rasp_20_sft_qwen_math: {"avg_response_length": 139.86, "eos_rate": 0.99625, "k": 8, "n_problems": 200, "natural_eos": 1594, "pass_at_k": 0.935, "stderr": 0.0174, "temperature": 0.7, "truncated": 6}
  hyp: RASP 20% pruned Qwen Math post-SFT maintains high pass@8 near unpruned level because preserved functional redundancy supports multiple diverse reasoning paths (C1 diversity)

eval_pass_k8_standard_20_grpo_deepseek: {}
  hyp: DeepSeek-R1-Distill-Qwen-7B Standard 20% post-GRPO pass@k=8 (N=200, T=0.7, seed=42). C1 diversity 验证：Standard collapse 模型的 sampling diversity。完成 pass@k 2×2 矩阵。Parent: grpo_stage2_standard_20_v8.

eval_pass_k8_standard_20_grpo_qwen_math_v2: {}
  hyp: Qwen2.5-Math-7B Standard 20% post-GRPO pass@k=8 (N=200, T=0.7, seed=42). C1 diversity 对照：frac_zero=0.85 collapse 模型的 sampling diversity。重跑 v1（僵尸进程被 kill）。Parent: grpo_standard_qwen_math_v3.

eval_pass_k8_unpruned_qwen_math: {"accuracy": 0.965, "k": 8, "n_samples": 200, "pass_at_k": 0.965, "stderr": 0.013, "temperature": 0.7}
  hyp: Unpruned Qwen Math post-GRPO achieves near-ceiling pass@8 on GSM8K, establishing that GRPO preserves solution diversity when no structural pruning damage exists (C1 control)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "e622cefb-dc60-4235-afd0-3f680c54b392"
}
```

</details>

---


### System

_source line 158_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2a92311f30a7bab6",
  "tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "description": "Running Check inference bench and multiseed experiments",
  "usage": {
    "total_tokens": 94582,
    "tool_uses": 46,
    "duration_ms": 569379
  },
  "last_tool_name": "Bash",
  "uuid": "526c8aa4-e326-4b50-ad79-bc0faec2afe2",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db"
}
```

---


### Tool call

_source line 159_

<details open><summary>🔧 Tool call — Bash · `toolu_01CkxrS2Ny6DXr8kHeWweZpC`</summary>

```json
{
  "command": "FPATH=\"/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt\"\npython3 -c \"\nimport json\nFPATH='$FPATH'\nwith open(FPATH) as f:\n    raw = f.read()\nouter = json.loads(raw)\ndata = json.loads(outer['result'])\nexps = data['data']['experiments']\n\n# Let me look at the 'multiseed_serial_westb' experiment and other analysis experiments\n# for the decoupling table CKA similarity claims\nfor eid in ['multiseed_serial_westb', 'inference_bench_cka_only_20_clean', \n            'inference_bench_clean_v2', 'inference_speedup_plan016_v2']:\n    if eid in exps:\n        e = exps[eid]\n        m = e.get('metrics', {})\n        h = e.get('hypothesis', '')\n        print(f'=== {eid} ===')\n        print(f'  hyp: {h[:300]}')\n        print(f'  metrics: {json.dumps(m)[:800]}')\n        print()\n\"\n",
  "description": "Check inference bench and multiseed experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "2124ca2c-24aa-4fea-b055-7af6c1658895",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_015QT5igsmUupwdwiQ1Zpzvv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1306,
      "cache_read_input_tokens": 91563,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1306,
        "ephemeral_1h_input_tokens": 0
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

_source line 160 · 2026-05-24T04:42:41.085Z_

<details><summary>↩ Tool result · `toolu_01CkxrS2Ny6DXr8kHeWweZpC`</summary>

```text
=== multiseed_serial_westb ===
  hyp: Multi-seed variance estimation (westb fallback): 4 serial evals (RASP×2 + Standard×2, seeds 123/456, N=200) to complement seed=42 data. Transferred from failed westd-11672. Results needed for 5-seed statistical significance in Paper Table 1.
  metrics: {"missing": "seed 42 and seed 789 not executed", "note": "2 seeds x 2 methods (not 4 seeds as planned). Script ran RASP+Standard for seeds 123,456.", "rasp_seed123": {"acc": 0.605, "correct": 121, "total": 200}, "rasp_seed456": {"acc": 0.6, "correct": 120, "total": 200}, "standard_seed123": {"acc": 0.645, "correct": 129, "total": 200}, "standard_seed456": {"acc": 0.61, "correct": 122, "total": 200}}

=== inference_bench_cka_only_20_clean ===
  hyp: Clean CKA-only inference benchmark (rerun after GPU contention in v1). Validates CKA-only latency/memory vs dense baseline on clean cuda:0. Dense dummy in rasp slot (rasp model not on westb).
  metrics: {"dense": {"tokens_per_second": 75.73, "avg_latency_sec": 6.729, "peak_memory_gb": 16.22, "total_tokens": 25477, "validation": "PASS (75.73 vs expected 76.25, <1% deviation)"}, "cka_only_20": {"tokens_per_second": 51.86, "avg_latency_sec": 4.078, "peak_memory_gb": 11.6, "total_tokens": 10574, "latency_speedup_vs_dense": "39.4%", "memory_reduction_vs_dense": "28.5%"}, "rasp_20_dummy": {"tokens_per_second": 75.79, "avg_latency_sec": 6.723, "peak_memory_gb": 16.23, "note": "Dense model used as dummy (rasp not on westb)"}}

=== inference_bench_clean_v2 ===
  hyp: Clean inference benchmark (Dense + CKA-only 20% + Standard 20%) on isolated GPU. Previous plan_016 benchmark was polluted by GPU contention. Measures per-token throughput and latency for speedup claims. 50 prompts x 256 max_new_tokens, GSM8K test set.
  metrics: {"original_tps": 72.02, "cka_only_20_tps": 58.28, "standard_20_tps": 58.25, "cka_only_20_speedup": 0.809, "standard_20_speedup": 0.809, "original_first_token_ms": 20.05, "cka_only_20_first_token_ms": 16.35, "standard_20_first_token_ms": 16.4, "original_per_token_ms": 13.89, "cka_only_20_per_token_ms": 16.73, "standard_20_per_token_ms": 16.71, "original_params": 7615616512, "pruned_params": 6161946112, "param_reduction_pct": 19.1}

=== inference_speedup_plan016_v2 ===
  hyp: Inference speedup benchmark v2 (code fix applied): Dense vs RASP 20% vs Standard 20%. 测量 wall-clock latency, tokens/s, memory_peak. 50 GSM8K prompts, batch_size=1, greedy, max_new_tokens=512. Parent: inference_speedup_plan016 (failed due to model loading bug, now fixed with load_pruned_model).
  metrics: {"dense": {"avg_latency_sec": 6.682, "peak_memory_gb": 16.22, "tokens_per_second": 76.25}, "rasp_20": {"avg_latency_sec": 4.156, "latency_speedup_vs_dense": "37.8%", "memory_reduction_vs_dense": "28.5%", "peak_memory_gb": 11.6, "tokens_per_second": 52.07}, "standard_20": {"avg_latency_sec": 6.167, "latency_speedup_vs_dense": "7.7%", "memory_reduction_vs_dense": "28.4%", "peak_memory_gb": 11.61, "tokens_per_second": 49.78}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "6ee36d22-f7a7-4b8c-b426-7405c7c98d1d"
}
```

</details>

---


### System

_source line 161_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2a92311f30a7bab6",
  "tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "description": "Running Check floor ablation and grasp baseline experiments",
  "usage": {
    "total_tokens": 96330,
    "tool_uses": 47,
    "duration_ms": 580075
  },
  "last_tool_name": "Bash",
  "uuid": "79c46e88-1bc9-45a6-beb1-69a64216aac1",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db"
}
```

---


### Tool call

_source line 162_

<details open><summary>🔧 Tool call — Bash · `toolu_01GZehkF8oHXnYzXNoXF1P6Y`</summary>

```json
{
  "command": "FPATH=\"/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt\"\npython3 -c \"\nimport json\nFPATH='$FPATH'\nwith open(FPATH) as f:\n    raw = f.read()\nouter = json.loads(raw)\ndata = json.loads(outer['result'])\nexps = data['data']['experiments']\n\n# Final checks: look for any CKA similarity values in floor_ablation or other experiments\nfor eid in ['floor_ablation_0p3_cka_only_20_v2', 'floor_ablation_0p5_cka_only_20_v2', 'floor_ablation_0p6_cka_only_20_v2']:\n    if eid in exps:\n        e = exps[eid]\n        m = e.get('metrics', {})\n        h = e.get('hypothesis', '')\n        print(f'{eid}: {json.dumps(m)[:500]}')\n        print(f'  hyp: {h[:400]}')\n        print()\n\n# Also check grasp baseline\ne = exps.get('grasp_baseline_westd', {})\nprint('grasp_baseline_westd:', e.get('metrics', {}))\nprint('  hyp:', e.get('hypothesis', '')[:300])\n\"\n",
  "description": "Check floor ablation and grasp baseline experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "c8cb0dcc-3907-4c8c-bfd4-b2ef9adcd3b5",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_013BxPraBhBXb1p55JMhA4fX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1715,
      "cache_read_input_tokens": 92869,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1715,
        "ephemeral_1h_input_tokens": 0
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

_source line 163 · 2026-05-24T04:42:51.771Z_

<details><summary>↩ Tool result · `toolu_01GZehkF8oHXnYzXNoXF1P6Y`</summary>

```text
floor_ablation_0p3_cka_only_20_v2: {"gsm8k_accuracy": 0.6505, "gsm8k_correct": 858, "gsm8k_total": 1319}
  hyp: Floor ratio ablation (retry): floor=0.3, CKA-only 20% pruning on DeepSeek-R1-Distill-Qwen-7B. Pipeline: Prune → SFT(2ep) → GRPO(100 steps) → GSM8K eval. v1 failed at GRPO save due to disk full; v2 resumes from completed Prune+SFT, only reruns GRPO+eval.

floor_ablation_0p5_cka_only_20_v2: {"gsm8k_accuracy": 0.6171, "gsm8k_correct": 814, "gsm8k_total": 1319, "eos_rate": 0.992}
  hyp: Floor ratio ablation (retry): floor=0.5, CKA-only 20% pruning on DeepSeek-R1-Distill-Qwen-7B. Pipeline: Prune → SFT(2ep) → GRPO(100 steps) → GSM8K eval. v1 failed during pruning save due to disk full; v2 reruns full pipeline after disk cleanup.

floor_ablation_0p6_cka_only_20_v2: {"gsm8k_accuracy": 0.6202, "gsm8k_correct": 818, "gsm8k_total": 1319, "gsm8k_ci": 0.0134, "eos_rate": 0.9803, "avg_response_length": 252.7, "grpo_train_loss": 0.006503, "grpo_final_reward": 0.2419}
  hyp: Floor ratio ablation retry: floor=0.6, CKA-only 20% pruning. v1 GRPO completed but save_model crashed (disk full). v2 reruns after disk cleanup (168GB freed). Pipeline SKIP mechanism skips Prune+SFT, only reruns GRPO+eval.

grasp_baseline_westd: {'avg_len': 4018, 'eos_rate': 0.02, 'grasp_20_accuracy_n100': 0.07, 'json_path': 'results/eval_pruned_graspune_20_greedy.json', 'n_correct': 7, 'n_total': 100, 'rasp_20_accuracy_ref': 0.31, 'standard_20_accuracy_ref': 0.27}
  hyp: D027: GraSP baseline on westd — compare GraSP pruning criterion against RASP at 20% sparsity. If RASP > GraSP post-recovery, confirms CKA-aware scoring advantage over gradient-based saliency. Critical for plan_005 and Dream reviewer concern.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "a319f01e-fe9b-4d0e-b581-005e00f515e0"
}
```

</details>

---


### System

_source line 164_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2a92311f30a7bab6",
  "tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "description": "Running Search spec fields for CKA similarity values",
  "usage": {
    "total_tokens": 97594,
    "tool_uses": 48,
    "duration_ms": 592843
  },
  "last_tool_name": "Bash",
  "uuid": "db9eb628-25ef-4536-a200-3d8bb6fb8d04",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db"
}
```

---


### Tool call

_source line 165_

<details open><summary>🔧 Tool call — Bash · `toolu_01VcTSUhB1RwQMRGnCo4J6vJ`</summary>

```json
{
  "command": "FPATH=\"/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt\"\npython3 -c \"\nimport json\nFPATH='$FPATH'\nwith open(FPATH) as f:\n    raw = f.read()\nouter = json.loads(raw)\ndata = json.loads(outer['result'])\nexps = data['data']['experiments']\n\n# Look for CKA similarity scores in the spec/command fields or any other metadata\n# Also look for the collapsing methods CKA similarity claim (mu>=0.88)\n# The claim is about Standard and RASP pruning having high CKA similarity (redundancy)\n# whereas CKA-only has low CKA similarity (diversity preserved)\n# These values may come from the CKA scoring itself, not a separate experiment\n\n# Check if any experiment tracks 'mean_cka_score' or similar at pruning time\nfor eid, e in exps.items():\n    m = e.get('metrics', {})\n    mstr = json.dumps(m)\n    if any(x in mstr for x in ['mean_cka', 'avg_cka', 'cka_score', 'overlap_score', 'similarity_score']):\n        print(f'{eid}: {mstr[:600]}')\n        print()\n\n# Also search in the spec/command for these values\nfor eid, e in exps.items():\n    spec = e.get('spec', {})\n    spec_str = json.dumps(spec)\n    if 'cka_similarity' in spec_str.lower() or '0.62' in spec_str or '0.88' in spec_str:\n        print(f'SPEC: {eid}: has CKA sim or value')\n        print()\n\"\n",
  "description": "Search spec fields for CKA similarity values"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "7993b794-0885-4602-a963-af92bb63bae5",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Y8z3Ag6SKEEEoUsTQr9jhx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1231,
      "cache_read_input_tokens": 94584,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1231,
        "ephemeral_1h_input_tokens": 0
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

_source line 166 · 2026-05-24T04:43:04.553Z_

<details><summary>↩ Tool result · `toolu_01VcTSUhB1RwQMRGnCo4J6vJ`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "1db108e0-5475-4650-9e6b-6c5ed89f284d"
}
```

</details>

---


### System

_source line 167_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2a92311f30a7bab6",
  "tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "description": "Running Search raw file for 0.62 and 0.88 values in context",
  "usage": {
    "total_tokens": 98250,
    "tool_uses": 49,
    "duration_ms": 599289
  },
  "last_tool_name": "Bash",
  "uuid": "54b68fda-ba2c-4ba1-b26e-210a5ec51f06",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db"
}
```

---


### Tool call

_source line 168_

<details open><summary>🔧 Tool call — Bash · `toolu_01XZarYEcSCrbZfep3DeRCQT`</summary>

```json
{
  "command": "FPATH=\"/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt\"\npython3 -c \"\nimport json\nFPATH='$FPATH'\nwith open(FPATH) as f:\n    raw = f.read()\nouter = json.loads(raw)\ndata = json.loads(outer['result'])\nexps = data['data']['experiments']\n\n# Comprehensive search for '0.62' (CKA similarity for CKA-only pruning)\n# In the entire file:\nraw_data = outer['result']\n# Find context around '0.62' mentions that aren't already captured\nimport re\nmatches = [(m.start(), raw_data[max(0,m.start()-100):m.end()+100]) for m in re.finditer(r'\\\"0\\.62\\\"', raw_data)]\nfor start, ctx in matches[:10]:\n    print(f'  context: ...{ctx}...')\n    print()\n\n# Find '0.88' mentions\nmatches88 = [(m.start(), raw_data[max(0,m.start()-100):m.end()+100]) for m in re.finditer(r'0\\.88', raw_data)]\nfor start, ctx in matches88[:5]:\n    print(f'  0.88 context: ...{ctx}...')\n    print()\n\"\n",
  "description": "Search raw file for 0.62 and 0.88 values in context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "7443a1b4-5a41-4059-92eb-88787a4d9b2c",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Wk8zh1dg63wsf32At3p6R7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 598,
      "cache_read_input_tokens": 95815,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 598,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 58,
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

_source line 169 · 2026-05-24T04:43:10.986Z_

<details><summary>↩ Tool result · `toolu_01XZarYEcSCrbZfep3DeRCQT`</summary>

```text
  0.88 context: ...: "MBPP pass@1 eval on GRPO RASP 20% model @2048. Dense baseline=53.48% (200/374). RASP GRPO GSM8K=60.88%, HumanEval=10.37%. Tests RASP GRPO code generation on MBPP. Completes MBPP 3×2 matrix. Expected: b...

  0.88 context: ...879, "avg_response_length": 195.7}, "notes": "Cron false positive: eval脚本不走W&B误判failed。实际 accuracy=60.88% (803/1319)。RASP 介于 Standard (59.44%) 和 CKA-only (64.37%) 之间，更靠近 Standard。RASP-Standard gap=1.44pp,...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "0c61d5e0-2d40-4362-8bf1-bea523a0d123"
}
```

</details>

---


### System

_source line 170_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2a92311f30a7bab6",
  "tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "description": "Running Search for CKA similarity patterns in raw file",
  "usage": {
    "total_tokens": 99024,
    "tool_uses": 50,
    "duration_ms": 604571
  },
  "last_tool_name": "Bash",
  "uuid": "d3cec698-e8c3-4e5e-ba7b-19d10dee28f4",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db"
}
```

---


### Tool call

_source line 171_

<details open><summary>🔧 Tool call — Bash · `toolu_013P6E5injpDGtUUBrENRVr6`</summary>

```json
{
  "command": "FPATH=\"/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt\"\npython3 -c \"\nimport json, re\nFPATH='$FPATH'\nwith open(FPATH) as f:\n    raw = f.read()\nouter = json.loads(raw)\nraw_data = outer['result']\n\n# Search specifically for cka similarity values\nfor pattern in [r'cka.*sim.*0\\.\\d+', r'mu.*0\\.6[0-9]', r'mean.*cka.*0\\.\\d+', r'F\\(h\\).*mean', r'similarity.*mean']:\n    matches = re.finditer(pattern, raw_data, re.IGNORECASE)\n    for m in matches:\n        ctx = raw_data[max(0,m.start()-80):m.end()+80]\n        print(f'Pattern [{pattern}]: {ctx[:200]}')\n        print()\n\"\n",
  "description": "Search for CKA similarity patterns in raw file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "34a0c437-8799-4cb1-b268-eef80b68b8ad",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_018LXUDX1PKgHvFBcB14Lh2K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 710,
      "cache_read_input_tokens": 96413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 710,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 64,
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

_source line 172 · 2026-05-24T04:43:16.280Z_

<details><summary>↩ Tool result · `toolu_013P6E5injpDGtUUBrENRVr6`</summary>

```text
Pattern [cka.*sim.*0\.\d+]: uncated_pct": 0.302, "truncated": 151, "natural_eos": 349}}, "eval_math500_grpo_cka_only_25_fixed": {"status": "DONE", "retry_count": 0, "created_at": "2026-05-23T19:48:08.783Z", "updated_at": "2026-0

Pattern [mu.*0\.6[0-9]]: 2026-05-23T19:35:48.851Z", "submitted_via": "submit_training_job", "backend": "tmux", "account": "root", "wall_clock_seconds": 13096.9, "gpu_hours": 3.64}, "pid": "321423", "log_path": "~/runs/recover

Pattern [mean.*cka.*0\.\d+]: .06684, "final_kl": 0.004236, "final_entropy": 0.1704, "final_completion_length_mean": 189.1, "final_grad_norm": 5.531, "frac_reward_zero_std": 0.4, "wandb_run_id": "9c16hnf7", "wandb_run_name": "grpo

Pattern [F\(h\).*mean]:  "2026-05-19T14:32:43.647Z", "hypothesis": "CKA-based functional overlap scores F(h) are stable across calibration sizes (256/512/1024 samples), with Spearman rho > 0.95 between any two sizes. This va

Pattern [similarity.*mean]: HumanEval from SFT baseline of 0% pass@1, because CKA-only preserves structural similarity that GRPO can exploit for cross-task recovery", "parent": "grpo_cka_only_20", "metrics": {"pass_at_1": 0.2012
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "d8bbd5b7-f054-4f80-9e7f-a94be29d1f6e"
}
```

</details>

---


### System

_source line 173_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2a92311f30a7bab6",
  "tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "description": "Running Verify Qwen N=200 sample size claim and other eval details",
  "usage": {
    "total_tokens": 99954,
    "tool_uses": 51,
    "duration_ms": 616645
  },
  "last_tool_name": "Bash",
  "uuid": "6c32bcf1-ffbd-48d8-ad99-2ae90418dd7b",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db"
}
```

---


### Tool call

_source line 174_

<details open><summary>🔧 Tool call — Bash · `toolu_01SaihCoVLqvUSvxrS8grgR9`</summary>

```json
{
  "command": "FPATH=\"/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt\"\npython3 -c \"\nimport json\nFPATH='$FPATH'\nwith open(FPATH) as f:\n    raw = f.read()\nouter = json.loads(raw)\ndata = json.loads(outer['result'])\nexps = data['data']['experiments']\n\n# Now check the eval_sft_cka_only_20 with N=1319 (not the n100 or n1319 versions)\n# Also check all eval_sft_* experiments with fine-grained sub-scores\nfor eid in ['eval_sft_cka_only_20', 'eval_sft_cka_only_20_n1319', 'eval_sft_alpha_2p0',\n            'eval_sft_rasp_25', 'eval_sft_standard_25']:\n    if eid in exps:\n        e = exps[eid]\n        m = e.get('metrics', {})\n        h = e.get('hypothesis', '')\n        print(f'{eid}: {json.dumps(m)[:400]}')\n        print(f'  hyp: {h[:200]}')\n        print()\n\n# Check the Qwen cross-arch N=200 sample size claim\n# eval_grpo_rasp_20_qwen_math: n_samples=200, accuracy=72.5%\n# eval_grpo_standard_20_qwen_math: n_samples=200, accuracy=70.5%\n# These are N=200 GRPO results for cross-architecture validation\n# Claim #15: N=200 sample size for Qwen2.5-Math-7B\nqwen_evals = ['eval_grpo_rasp_20_qwen_math', 'eval_grpo_standard_20_qwen_math', \n              'eval_sft_rasp_qwen_math_n200', 'eval_sft_standard_qwen_math_n200',\n              'eval_sft_qwen_math_rasp_25', 'eval_sft_qwen_math_standard_25']\nprint('=== Qwen N=200 evals ===')\nfor eid in qwen_evals:\n    if eid in exps:\n        m = exps[eid].get('metrics', {})\n        print(f'{eid}: n_samples={m.get(\\\"n_samples\\\", m.get(\\\"n_total\\\", m.get(\\\"total\\\", \\\"?\\\")))} acc={m.get(\\\"accuracy\\\", m.get(\\\"acc\\\", \\\"?\\\"))}')\n\"\n",
  "description": "Verify Qwen N=200 sample size claim and other eval details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "b6afcbc8-3031-4dee-95a3-b067e5f6b1b8",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01WBp8cSAQFPttPYwMgq5m4m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 865,
      "cache_read_input_tokens": 97123,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 865,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
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

_source line 175 · 2026-05-24T04:43:28.366Z_

<details><summary>↩ Tool result · `toolu_01SaihCoVLqvUSvxrS8grgR9`</summary>

```text
eval_sft_cka_only_20: {"avg_response_length": 182.73, "eos_rate": 0.995, "gsm8k_accuracy": 0.64, "gsm8k_stderr": 0.0339, "mode": "greedy", "n_correct": 128, "n_total": 200, "seed": 42, "truncated": 1}
  hyp: CKA-only 20% post-SFT GSM8K accuracy (N=200). Post-prune was 38.5% (highest among all methods). If post-SFT >> 60%, CKA-only scoring is superior for SFT recovery. If ~60% like RASP/Standard/Random, co

eval_sft_cka_only_20_n1319: {"avg_response_length": 198.1, "correct": 843, "eos_rate": 0.9901, "gsm8k_accuracy": 0.6391, "stderr": 0.0132, "total": 1319}
  hyp: CKA-only pruning preserves more recoverable structure than RASP/Standard, so post-SFT accuracy should be highest among all 20% pruning methods on full GSM8K (N=1319).

eval_sft_alpha_2p0: {"accuracy": 0.62, "avg_len": 277.41, "eos_rate": 0.97, "n_correct": 62, "n_total": 100, "stderr": 0.0485}
  hyp: α=2.0 post-SFT GSM8K eval (N=100, greedy). Post-prune 29%, post-SFT loss=0.61, token_acc=0.84. Completes α ablation sweep: α=0.0 (64%), α=1.0 (57%), α=4.0 (62%), α=2.0 (?). Parent: sft_alpha2_0_westd.

eval_sft_rasp_25: {"accuracy": 0.5299, "eos_rate": 0.918, "n_correct": 699, "n_samples": 1319, "seed": 42, "stderr": 0.0137, "truncated": 108}
  hyp: RASP 25% post-SFT GSM8K eval (N=1319, greedy, seed=42). sft_rasp_25 刚完成 (loss=0.8498, token_acc=0.8073)，对比 sft_standard_25 (待完成) 和 20% sparsity 结果 (RASP 57% vs Standard 64%)。Parent: sft_rasp_25.

eval_sft_standard_25: {"accuracy": 0.5125, "avg_len": 326.26, "eos_rate": 0.9545, "n_correct": 676, "n_total": 1319, "stderr": 0.0138}
  hyp: Standard 25% post-SFT GSM8K eval (N=1319, greedy, seed=42). 对比 eval_sft_rasp_25 (同时在 westd 运行)，25% sparsity 下 RASP vs Standard post-SFT recovery 对比。20% 结果: Standard 64% > RASP 57%。Parent: sft_standard

=== Qwen N=200 evals ===
eval_grpo_rasp_20_qwen_math: n_samples=200 acc=0.725
eval_grpo_standard_20_qwen_math: n_samples=200 acc=0.705
eval_sft_rasp_qwen_math_n200: n_samples=200 acc=0.725
eval_sft_standard_qwen_math_n200: n_samples=200 acc=0.71
eval_sft_qwen_math_rasp_25: n_samples=200 acc=64
eval_sft_qwen_math_standard_25: n_samples=200 acc=63
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "21e2c2ee-d41a-48e6-8f51-4b02d5986b2b"
}
```

</details>

---


### System

_source line 176_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2a92311f30a7bab6",
  "tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "description": "Running Generate comprehensive claim verification summary part 1",
  "usage": {
    "total_tokens": 101829,
    "tool_uses": 52,
    "duration_ms": 644901
  },
  "last_tool_name": "Bash",
  "uuid": "19076f48-baca-48e8-bb53-f633c2963ece",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db"
}
```

---


### Tool call

_source line 177_

<details open><summary>🔧 Tool call — Bash · `toolu_01SvJQDFbJCxA5kb65DuYKdN`</summary>

```json
{
  "command": "FPATH=\"/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt\"\npython3 -c \"\nimport json\nFPATH='$FPATH'\nwith open(FPATH) as f:\n    raw = f.read()\nouter = json.loads(raw)\ndata = json.loads(outer['result'])\nexps = data['data']['experiments']\n\n# Final summary computation: let me pull together all numbers\nprint('='*70)\nprint('CLAIM VERIFICATION SUMMARY')\nprint('='*70)\nprint()\n\n# Claim #1: GSM8K accuracy at alpha=2.0, 20% sparsity, GRPO recovery = 66.11%\ngrpo_a2 = exps['eval_gsm8k_grpo_alpha2p0_20']['metrics']['gsm8k_accuracy']\nprint(f'Claim 1: paper=66.11%, registry={grpo_a2*100:.2f}%, exp=eval_gsm8k_grpo_alpha2p0_20')\nprint(f'  GRPO acc: {grpo_a2}, matches: {abs(grpo_a2*100 - 66.11) < 0.01}')\nprint()\n\n# Claim #2: Mean |Delta(GRPO-SFT)| across four criteria at 20% sparsity = 0.54 pp\n# From analysis: 4 criteria = GSM8K for Standard/CKA-only/RASP only gives 0.43 pp\n# The registry doesn't have a pre-computed 0.54 pp value\nprint('Claim 2: paper=0.54 pp mean |Delta|')\n# Three main methods at 20%: Standard(0.23), CKA-only(0.46), RASP(0.61)\n# Mean = 0.43 pp -- not matching\n# No direct registry source for exactly 0.54 pp across 4 named criteria\nprint('  Computed from registry: 3 methods (Std 0.23, CKA 0.46, RASP 0.61) mean=0.43')\nprint('  Cannot reproduce 0.54 pp from 4 criteria -- no direct registry source found')\nprint()\n\n# Claim #3: Max |Delta(GRPO-SFT)| across four criteria at 20% sparsity = 0.61 pp\nprint('Claim 3: paper=0.61 pp max |Delta|')\nprint('  From registry: max across Std(0.23), CKA(0.46), RASP(0.61) = 0.61 pp')\nprint('  RASP 20% GSM8K: SFT=61.49%, GRPO=60.88%, |Delta|=0.61 pp - MATCH')\nprint()\n\n# Claim #4: Max including dose-response and MBPP = 1.34 pp\nprint('Claim 4: paper=1.34 pp max |Delta| including dose-response and MBPP')\nprint('  MBPP CKA-only: SFT=12.83%, GRPO=14.17%, |Delta|=1.34 pp - MATCH')\nprint('  exp: eval_mbpp_sft_cka_only_20 (12.83%), eval_mbpp_grpo_cka_only_20 (14.17%)')\nprint()\n\n# Claim #5: Peak reward ratio CKA-only vs Standard GRPO = 4.4x\nprint('Claim 5: paper=4.4x peak reward ratio CKA-only vs Standard')\ncka_peak = 0.3544  # grpo_cka_only_20\nstd_peak = 0.081   # grpo_standard_20_fair\nratio = cka_peak / std_peak\nprint(f'  CKA-only peak={cka_peak}, Standard peak={std_peak}, ratio={ratio:.2f}x')\nprint(f'  exp: grpo_cka_only_20 (peak_reward=0.3544), grpo_standard_20_fair (peak_reward=0.081)')\nprint(f'  Registry ratio={ratio:.2f}x, paper claims 4.4x: CLOSE but not exact (diff={abs(ratio-4.4):.2f})')\nprint()\n\n# Claim #6: ShortGPT |Delta(GRPO-SFT)| = -1.36 pp\nshortgpt_sft = 44.73  # eval_gsm8k_sft_shortgpt_20\nshortgpt_grpo = 43.37  # eval_gsm8k_grpo_shortgpt_20\nshortgpt_delta = shortgpt_grpo - shortgpt_sft\nprint(f'Claim 6: paper=-1.36 pp ShortGPT |Delta(GRPO-SFT)|')\nprint(f'  ShortGPT SFT={shortgpt_sft}%, GRPO={shortgpt_grpo}%, Delta={shortgpt_delta:.2f} pp')\nprint(f'  exp: eval_gsm8k_sft_shortgpt_20 (44.73%), eval_gsm8k_grpo_shortgpt_20 (43.37%)')\nprint(f'  MATCH: Delta=-1.36 pp')\nprint()\n\n# Claim #7: |Delta(GRPO-SFT)| at each dose-response alpha <= 1.14 pp\nprint('Claim 7: |Delta| <= 1.14 pp at every dose-response alpha point')\nalphas = {\n    '0.5': (0.6118, 0.6073),\n    '2.0': (0.6611, 0.6497),\n    '3.0': (0.6345, 0.6414),\n    '4.0': (0.6277, 0.6194),\n}\nfor alpha, (grpo, sft) in alphas.items():\n    delta = abs(grpo-sft)*100\n    print(f'  alpha={alpha}: |Delta|={delta:.2f} pp, <= 1.14? {delta <= 1.14}')\nprint(f'  Max = 1.14 pp at alpha=2.0 - MATCHES claim')\nprint()\n\"\n",
  "description": "Generate comprehensive claim verification summary part 1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "cc9c4ad4-c626-40f3-8d9a-4865021eb44f",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01H77JUvE3aeXqjcPGUkrzRc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1842,
      "cache_read_input_tokens": 97988,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1842,
        "ephemeral_1h_input_tokens": 0
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

_source line 178 · 2026-05-24T04:43:56.601Z_

<details><summary>↩ Tool result · `toolu_01SvJQDFbJCxA5kb65DuYKdN`</summary>

```text
======================================================================
CLAIM VERIFICATION SUMMARY
======================================================================

Claim 1: paper=66.11%, registry=66.11%, exp=eval_gsm8k_grpo_alpha2p0_20
  GRPO acc: 0.6611, matches: True

Claim 2: paper=0.54 pp mean |Delta|
  Computed from registry: 3 methods (Std 0.23, CKA 0.46, RASP 0.61) mean=0.43
  Cannot reproduce 0.54 pp from 4 criteria -- no direct registry source found

Claim 3: paper=0.61 pp max |Delta|
  From registry: max across Std(0.23), CKA(0.46), RASP(0.61) = 0.61 pp
  RASP 20% GSM8K: SFT=61.49%, GRPO=60.88%, |Delta|=0.61 pp - MATCH

Claim 4: paper=1.34 pp max |Delta| including dose-response and MBPP
  MBPP CKA-only: SFT=12.83%, GRPO=14.17%, |Delta|=1.34 pp - MATCH
  exp: eval_mbpp_sft_cka_only_20 (12.83%), eval_mbpp_grpo_cka_only_20 (14.17%)

Claim 5: paper=4.4x peak reward ratio CKA-only vs Standard
  CKA-only peak=0.3544, Standard peak=0.081, ratio=4.38x
  exp: grpo_cka_only_20 (peak_reward=0.3544), grpo_standard_20_fair (peak_reward=0.081)
  Registry ratio=4.38x, paper claims 4.4x: CLOSE but not exact (diff=0.02)

Claim 6: paper=-1.36 pp ShortGPT |Delta(GRPO-SFT)|
  ShortGPT SFT=44.73%, GRPO=43.37%, Delta=-1.36 pp
  exp: eval_gsm8k_sft_shortgpt_20 (44.73%), eval_gsm8k_grpo_shortgpt_20 (43.37%)
  MATCH: Delta=-1.36 pp

Claim 7: |Delta| <= 1.14 pp at every dose-response alpha point
  alpha=0.5: |Delta|=0.45 pp, <= 1.14? True
  alpha=2.0: |Delta|=1.14 pp, <= 1.14? True
  alpha=3.0: |Delta|=0.69 pp, <= 1.14? True
  alpha=4.0: |Delta|=0.83 pp, <= 1.14? True
  Max = 1.14 pp at alpha=2.0 - MATCHES claim
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "304977ed-a41f-4ed0-beb2-ba7e2a63f705"
}
```

</details>

---


### System

_source line 179_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2a92311f30a7bab6",
  "tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "description": "Running Generate claim verification summary part 2",
  "usage": {
    "total_tokens": 104316,
    "tool_uses": 53,
    "duration_ms": 666654
  },
  "last_tool_name": "Bash",
  "uuid": "e5ee8712-91cc-4a9d-926d-4506223f6783",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db"
}
```

---


### Tool call

_source line 180_

<details open><summary>🔧 Tool call — Bash · `toolu_01FmNUge3qkn3uqCroMt5XWx`</summary>

```json
{
  "command": "FPATH=\"/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt\"\npython3 -c \"\nimport json\nFPATH='$FPATH'\nwith open(FPATH) as f:\n    raw = f.read()\nouter = json.loads(raw)\ndata = json.loads(outer['result'])\nexps = data['data']['experiments']\n\nprint('Continued verification...')\nprint()\n\n# Claim #8: 15% sparsity CKA-guided GRPO-SFT differential = +1.51 pp\n# Computed: mean(CKA-only 3 seeds GRPO-SFT) - mean(Standard 3 seeds GRPO-SFT)\n# CKA: seed42(+0.91), seed123(+0.91), seed456(-0.08) -> mean = +0.58 pp\n# Std: seed42(-0.38), seed123(-1.36), seed456(-1.06) -> mean = -0.93 pp\n# Differential = 0.58 - (-0.93) = 1.51 pp\nprint('Claim 8: paper=+1.51 pp CKA-guided GRPO-SFT differential at 15%')\ncka15_mean = (0.91 + 0.91 + (-0.08)) / 3\nstd15_mean = (-0.38 + (-1.36) + (-1.06)) / 3\ndiff = cka15_mean - std15_mean\nprint(f'  CKA-only 15% per-seed: +0.91, +0.91, -0.08 -> mean={cka15_mean:.2f} pp')\nprint(f'  Standard 15% per-seed: -0.38, -1.36, -1.06 -> mean={std15_mean:.2f} pp')\nprint(f'  Differential = {diff:.2f} pp')\nprint(f'  exp: eval_gsm8k_grpo_cka_only_15_{{v2,seed123,seed456}}, eval_gsm8k_grpo_standard_15_{{v2,seed123_v3,seed456_v3}}')\nprint(f'  MATCH: {abs(diff - 1.51) < 0.01}')\nprint()\n\n# Claim #9: CKA similarity mean for CKA-only pruning = mu=0.62\nprint('Claim 9: paper=mu=0.62 CKA similarity for CKA-only pruning')\nprint('  NO DIRECT REGISTRY SOURCE FOUND')\nprint('  No experiment tracks per-layer CKA similarity scores as a metric')\nprint()\n\n# Claim #10: CKA similarity mean for collapsing methods = mu>=0.88\nprint('Claim 10: paper=mu>=0.88 CKA similarity for collapsing methods')\nprint('  NO DIRECT REGISTRY SOURCE FOUND')\nprint('  No experiment tracks per-layer CKA similarity scores as a metric')\nprint()\n\n# Claim #11: Gradient magnitude ratio CKA-only vs Standard = 2.89x\nm_grad = exps['gradient_flow_v3']['metrics']\nratio_grad = m_grad['cka_vs_standard_ratio']\nprint(f'Claim 11: paper=2.89x gradient magnitude ratio')\nprint(f'  Registry: cka_vs_standard_ratio={ratio_grad}')\nprint(f'  CKA mean grad norm={m_grad[\\\"cka_only_mean_grad_norm\\\"]}, Standard={m_grad[\\\"standard_mean_grad_norm\\\"]}')\nprint(f'  exp: gradient_flow_v3 - MATCH: {ratio_grad == 2.89}')\nprint()\n\n# Claim #12: f_0 (zero-variance batch fraction) > 0.5 for Standard\nprint('Claim 12: paper=> 0.5 f_0 for Standard under GRPO')\nm_std_fair = exps['grpo_standard_20_fair']['metrics']\ntraj = m_std_fair['frac_zero_std_trajectory']\nprint(f'  Standard frac_zero_std trajectory: {traj}')\nprint(f'  Min = {min(traj)}, All >= 0.5? {all(x >= 0.5 for x in traj)}')\nprint(f'  exp: grpo_standard_20_fair - MATCH (all >= 0.5)')\nprint()\n\"\n",
  "description": "Generate claim verification summary part 2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "641ca22a-d777-45d4-b118-610494ee876f",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01FR8w7QaaPtLqTXSTCMBZT8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2454,
      "cache_read_input_tokens": 99830,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2454,
        "ephemeral_1h_input_tokens": 0
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

_source line 181 · 2026-05-24T04:44:18.357Z_

<details><summary>↩ Tool result · `toolu_01FmNUge3qkn3uqCroMt5XWx`</summary>

```text
Continued verification...

Claim 8: paper=+1.51 pp CKA-guided GRPO-SFT differential at 15%
  CKA-only 15% per-seed: +0.91, +0.91, -0.08 -> mean=0.58 pp
  Standard 15% per-seed: -0.38, -1.36, -1.06 -> mean=-0.93 pp
  Differential = 1.51 pp
  exp: eval_gsm8k_grpo_cka_only_15_{v2,seed123,seed456}, eval_gsm8k_grpo_standard_15_{v2,seed123_v3,seed456_v3}
  MATCH: True

Claim 9: paper=mu=0.62 CKA similarity for CKA-only pruning
  NO DIRECT REGISTRY SOURCE FOUND
  No experiment tracks per-layer CKA similarity scores as a metric

Claim 10: paper=mu>=0.88 CKA similarity for collapsing methods
  NO DIRECT REGISTRY SOURCE FOUND
  No experiment tracks per-layer CKA similarity scores as a metric

Claim 11: paper=2.89x gradient magnitude ratio
  Registry: cka_vs_standard_ratio=2.89
  CKA mean grad norm=0.3229, Standard=0.1118
  exp: gradient_flow_v3 - MATCH: True

Claim 12: paper=> 0.5 f_0 for Standard under GRPO
  Standard frac_zero_std trajectory: [0.5, 0.625, 0.5, 0.5, 0.575, 0.55, 0.575, 0.55, 0.55, 0.55]
  Min = 0.5, All >= 0.5? True
  exp: grpo_standard_20_fair - MATCH (all >= 0.5)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "fe478317-fc46-4098-96d7-4164e56b29e9"
}
```

</details>

---


### System

_source line 182_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2a92311f30a7bab6",
  "tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "description": "Running Generate claim verification summary part 3",
  "usage": {
    "total_tokens": 106097,
    "tool_uses": 54,
    "duration_ms": 695752
  },
  "last_tool_name": "Bash",
  "uuid": "b1688344-e6f7-4771-b410-fe158fc9b8e6",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db"
}
```

---


### Tool call

_source line 183_

<details open><summary>🔧 Tool call — Bash · `toolu_013uWu6YjhjoZcunmcfaoPgs`</summary>

```json
{
  "command": "FPATH=\"/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/4eec3ba0-e9d5-4e01-970e-75b659b505db/tool-results/mcp-agent-ml-research-read_registry-1779597152351.txt\"\npython3 -c \"\nimport json\nFPATH='$FPATH'\nwith open(FPATH) as f:\n    raw = f.read()\nouter = json.loads(raw)\ndata = json.loads(outer['result'])\nexps = data['data']['experiments']\n\nprint('Final claims...')\nprint()\n\n# Claim #13: SFT-only gap across criteria = 4.62 pp (in Table tab:decoupling)\n# Not found directly. Let's try: CKA-only SFT (63.91) - Standard SFT (59.21) = 4.70 pp\n# Or RASP SFT (61.49) - Standard SFT (59.21) = 2.28 pp\n# Or max SFT - min SFT across methods? max=CKA(63.91), min=Standard(59.21) -> 4.70\n# Or maybe it's from the westd N=100: RASP SFT=67%, Standard SFT=63% -> gap=4 pp\n# The claimed 4.62 doesn't exactly match any derived value\nprint('Claim 13: paper=4.62 pp SFT-only gap across criteria (tab:decoupling)')\nprint('  Derived from registry:')\nprint('  CKA-only SFT (20%)=63.91%, Standard SFT (20%)=59.21% -> gap=4.70 pp')\nprint(f'  {round((0.6391-0.5921)*100,2)} pp (CKA-SFT minus Std-SFT)')\nprint('  4.62 pp NOT found in any registry metric -- MISMATCH')\nprint('  Closest: 4.70 pp from eval_gsm8k_sft_cka_only_20 and eval_gsm8k_sft_standard_20')\nprint()\n\n# Claim #14: |Delta(GRPO-SFT)| at 15-25% sparsity <= 1 pp\nprint('Claim 14: paper=<= 1 pp |Delta| at 15-25% sparsity')\ndeltas = {\n    '15% CKA': abs(0.7309-0.7218)*100,\n    '15% Std': abs(0.6611-0.6649)*100,\n    '20% CKA': abs(0.6437-0.6391)*100,\n    '20% Std': abs(0.5944-0.5921)*100,\n    '20% RASP': abs(0.6088-0.6149)*100,\n    '25% CKA': abs(0.5959-0.6012)*100,\n    '25% Std': abs(0.5186-0.5087)*100,\n}\nfor name, d in deltas.items():\n    print(f'  {name}: |Delta|={d:.2f} pp, <= 1 pp? {d <= 1.0}')\nprint(f'  Max = {max(deltas.values()):.2f} pp -- MATCH: all <= 1 pp (just barely)')\nprint()\n\n# Claim #15: Qwen2.5-Math-7B cross-architecture N=200 sample size\nprint('Claim 15: Qwen2.5-Math-7B N=200 sample size')\nprint('  RASP GRPO Qwen: n_samples=200 acc=72.5% (eval_grpo_rasp_20_qwen_math)')\nprint('  Standard GRPO Qwen: n_samples=200 acc=70.5% (eval_grpo_standard_20_qwen_math)')\nprint('  SFT RASP Qwen: n_total=200 acc=72.5% (eval_sft_rasp_qwen_math_n200)')\nprint('  SFT Standard Qwen: n_total=200 acc=71.0% (eval_sft_standard_qwen_math_n200)')\nprint('  N=200 CONFIRMED for main Qwen cross-arch eval')\nprint()\n\n# Claim #16: 1.5B scale experiment exists\nprint('Claim 16: 1.5B scale experiment existence')\nprint('  CONFIRMED - multiple 1.5B experiments found:')\nprint('  grpo_cka_only_20_1p5b, grpo_standard_20_1p5b, grpo_rasp_20_1p5b')\nprint('  eval_gsm8k_grpo_cka_only_20_1p5b: acc=35.48%')\nprint('  eval_gsm8k_grpo_standard_20_1p5b: acc=22.29%')\nprint('  eval_gsm8k_grpo_rasp_20_1p5b: acc=26.16%')\nprint()\n\n# Claim #17: MATH-500 fixed eval - old vs new values\nprint('Claim 17: MATH-500 fixed eval versions')\nprint('  CKA-only 20% GRPO:')\nprint('    OLD (2048): 29.2% (eval_math500_grpo_cka_only_20_2048)')\nprint('    FIXED: 27.6% (eval_math500_grpo_cka_only_20_fixed)')\nprint('  Standard 20% GRPO:')\nprint('    OLD (fair_v2): 26.4% (eval_math500_grpo_standard_20_fair_v2)')\nprint('    FIXED: 27.0% (eval_math500_grpo_standard_20_fixed)')\nprint('  CKA-only 20% SFT:')\nprint('    OLD: 29.0% (eval_math500_sft_cka_only_20_v4_restart)')\nprint('    FIXED: 27.4% (eval_math500_sft_cka_only_20_fixed_v2)')\nprint('  RASP alpha=2.0 SFT:')\nprint('    OLD: 24.0% (eval_math500_sft_rasp_alpha2p0_20)')\nprint('    FIXED: 25.6% (eval_math500_sft_rasp_alpha2p0_20_fixed)')\nprint('  RASP alpha=2.0 GRPO:')\nprint('    OLD: 26.2% (eval_math500_grpo_rasp_alpha2p0_20)')\nprint('    FIXED: 27.4% (eval_math500_grpo_rasp_alpha2p0_20_fixed)')\n\"\n",
  "description": "Generate claim verification summary part 3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "5860f3f0-2d25-49e3-9461-86a4970bf49a",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01CT22GfVVC8NHF5jezLbkuF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1748,
      "cache_read_input_tokens": 102284,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1748,
        "ephemeral_1h_input_tokens": 0
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

_source line 184 · 2026-05-24T04:44:47.468Z_

<details><summary>↩ Tool result · `toolu_013uWu6YjhjoZcunmcfaoPgs`</summary>

```text
Final claims...

Claim 13: paper=4.62 pp SFT-only gap across criteria (tab:decoupling)
  Derived from registry:
  CKA-only SFT (20%)=63.91%, Standard SFT (20%)=59.21% -> gap=4.70 pp
  4.7 pp (CKA-SFT minus Std-SFT)
  4.62 pp NOT found in any registry metric -- MISMATCH
  Closest: 4.70 pp from eval_gsm8k_sft_cka_only_20 and eval_gsm8k_sft_standard_20

Claim 14: paper=<= 1 pp |Delta| at 15-25% sparsity
  15% CKA: |Delta|=0.91 pp, <= 1 pp? True
  15% Std: |Delta|=0.38 pp, <= 1 pp? True
  20% CKA: |Delta|=0.46 pp, <= 1 pp? True
  20% Std: |Delta|=0.23 pp, <= 1 pp? True
  20% RASP: |Delta|=0.61 pp, <= 1 pp? True
  25% CKA: |Delta|=0.53 pp, <= 1 pp? True
  25% Std: |Delta|=0.99 pp, <= 1 pp? True
  Max = 0.99 pp -- MATCH: all <= 1 pp (just barely)

Claim 15: Qwen2.5-Math-7B N=200 sample size
  RASP GRPO Qwen: n_samples=200 acc=72.5% (eval_grpo_rasp_20_qwen_math)
  Standard GRPO Qwen: n_samples=200 acc=70.5% (eval_grpo_standard_20_qwen_math)
  SFT RASP Qwen: n_total=200 acc=72.5% (eval_sft_rasp_qwen_math_n200)
  SFT Standard Qwen: n_total=200 acc=71.0% (eval_sft_standard_qwen_math_n200)
  N=200 CONFIRMED for main Qwen cross-arch eval

Claim 16: 1.5B scale experiment existence
  CONFIRMED - multiple 1.5B experiments found:
  grpo_cka_only_20_1p5b, grpo_standard_20_1p5b, grpo_rasp_20_1p5b
  eval_gsm8k_grpo_cka_only_20_1p5b: acc=35.48%
  eval_gsm8k_grpo_standard_20_1p5b: acc=22.29%
  eval_gsm8k_grpo_rasp_20_1p5b: acc=26.16%

Claim 17: MATH-500 fixed eval versions
  CKA-only 20% GRPO:
    OLD (2048): 29.2% (eval_math500_grpo_cka_only_20_2048)
    FIXED: 27.6% (eval_math500_grpo_cka_only_20_fixed)
  Standard 20% GRPO:
    OLD (fair_v2): 26.4% (eval_math500_grpo_standard_20_fair_v2)
    FIXED: 27.0% (eval_math500_grpo_standard_20_fixed)
  CKA-only 20% SFT:
    OLD: 29.0% (eval_math500_sft_cka_only_20_v4_restart)
    FIXED: 27.4% (eval_math500_sft_cka_only_20_fixed_v2)
  RASP alpha=2.0 SFT:
    OLD: 24.0% (eval_math500_sft_rasp_alpha2p0_20)
    FIXED: 25.6% (eval_math500_sft_rasp_alpha2p0_20_fixed)
  RASP alpha=2.0 GRPO:
    OLD: 26.2% (eval_math500_grpo_rasp_alpha2p0_20)
    FIXED: 27.4% (eval_math500_grpo_rasp_alpha2p0_20_fixed)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db",
  "uuid": "8aac2b07-2496-493c-a344-7c41bc6026f7"
}
```

</details>

---


### System

_source line 185_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2a92311f30a7bab6",
  "tool_use_id": "toolu_01DqLXKVyB8HFXo9RAjWmpwT",
  "description": "Running Final investigation of claim 2 mean delta computation",
  "usage": {
    "total_tokens": 109064,
    "tool_uses": 55,
    "duration_ms": 728537
  },
  "last_tool_name": "Bash",
  "uuid": "d565ffe6-b1c3-4da2-a807-b57fa02750c6",
  "session_id": "4eec3ba0-e9d5-4e01-970e-75b659b505db"
}
```

---
