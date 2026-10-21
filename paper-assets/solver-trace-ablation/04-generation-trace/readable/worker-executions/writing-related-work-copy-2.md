# writing related work

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 26
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/workers/worker_writing_related-work_20260514T191232.log`
- **Structured JSON:** [`716e4d8292a03e5deae9.json`](../../sessions/71/716e4d8292a03e5deae9.json)

## Before a recorded user message

26 recorded events

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
  "session_id": "dcf71cae-c473-420f-a877-7d46e8b92db9",
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
  "uuid": "3ec64c1d-5828-4d79-b75a-e1e3765d14a8",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/memory/"
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
    "resetsAt": 1778803800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "2a304f78-f08d-442b-8594-9d66e4afa500",
  "session_id": "dcf71cae-c473-420f-a877-7d46e8b92db9"
}
```

---

### Assistant

_source line 4_

I'll start by reading the existing paper sections for consistency, then draft the related work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dcf71cae-c473-420f-a877-7d46e8b92db9",
  "uuid": "f1eb5beb-2715-4261-9ccd-0739aa5c0ffe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SFXd968K9mnHdtwobvECHB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12713,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12713
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

<details open><summary>🔧 Tool call — Read · `toolu_01My2oi8zRFTAMGFNHTniQiv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dcf71cae-c473-420f-a877-7d46e8b92db9",
  "uuid": "d804356e-1498-454e-afcb-3a3c7fa58700",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SFXd968K9mnHdtwobvECHB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12713,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12713
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

_source line 6 · 2026-05-14T19:12:45.322Z_

<details><summary>↩ Tool result · `toolu_01My2oi8zRFTAMGFNHTniQiv`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	A GRPO-trained formalizer achieves a 93\% prove rate on first-order logic problems---yet 87\% of its proved outputs embed the conclusion verbatim among the premises.
5	The solver succeeds not because the model has learned to reason, but because the formalization trivially entails any conclusion that already appears as a premise.
6	This structural shortcut is invisible to execution-based evaluation: prove rate registers success regardless of whether the proof reflects genuine multi-step derivation or degenerate circular embedding.
7	
8	Neurosymbolic approaches that combine large language models with external solvers have shown promising results on logical reasoning tasks~\citep{satlm, logic-lm, linc}.
9	Recent work applies reinforcement learning---specifically Group Relative Policy Optimization~\citep[GRPO;][]{deepseekmath}---to train LLMs that generate formal logic programs verified by automated theorem provers~\citep{mellgren-prolog-grpo, logic-rl}.
10	The standard reward signal in these systems is binary: 1 if the solver proves the formalization, 0 otherwise.
11	This execution reward drives rapid improvement in prove rate but provides no gradient on structural quality.
12	A formalization where every premise contributes to a valid derivation receives the same reward as one that smuggles the conclusion into the premises.
13	
14	The absence of structural diagnostics leaves a critical blind spot.
15	Prove rate---the dominant evaluation metric for neurosymbolic formalizers---conflates faithful reasoning with degenerate shortcuts.
16	Without a principled method to assess whether each component of a formalization contributes to the proof, practitioners cannot distinguish models that reason from those that exploit solver mechanics.
17	This gap is particularly consequential in RL settings, where the optimizer will find and exploit any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}.
18	
19	We address this gap with \emph{Solver Trace Ablation} (STA), a diagnostic protocol inspired by mutation testing~\citep{demillo1978} that applies component necessity testing---leave-one-out (LOO) ablation on solver inputs---to quantify structural integrity (Figure~\ref{fig:sta-overview}).
20	For each proved formalization, STA removes each component individually and re-runs the solver; the fraction of components whose removal causes proof failure yields the \emph{Intensional Structural Reward} (ISR).
21	ISR$=$1 indicates a maximally tight formalization where every component is individually necessary; ISR$=$0 indicates complete structural redundancy.
22	The protocol is solver-agnostic: it applies to any external solver that accepts component-level input manipulation.
23	
24	Applied as a post-hoc diagnostic, ISR reveals a structural collapse trajectory entirely invisible to prove rate.
25	Under exec-only GRPO training, ISR falls from 0.642 at 100 steps to 0.132 at 500 steps to 0.003 at 1000 steps---a 99.5\% degradation---while prove rate simultaneously rises from 32\% to 96\% (Figure~\ref{fig:isr-collapse}).
26	By 1000 steps, 94.8\% of proved samples have ISR$=$0, meaning no single component is necessary for the proof.
27	The three exec-only seeds diverge radically (PR standard deviation $\pm$0.47), each converging to a qualitatively different degeneration mode---conclusion embedding, repetition collapse, and tautological collapse---underscoring that single-seed GRPO evaluation is unreliable.
28	A supervised fine-tuning (SFT) baseline confirms that this degeneration is RL-specific: SFT achieves 92.9\% genuine proofs with near-zero hacking, demonstrating that the structural collapse is a consequence of reward optimization rather than model capacity or data limitations.
29	
30	Given ISR's diagnostic power, a natural question is whether it can serve as a training signal to steer models toward structurally sound formalizations.
31	The answer is negative.
32	When ISR is incorporated into the reward ($r = r_{\text{exec}} \cdot (1 + \beta \cdot \text{ISR})$), the model games the diagnostic metric itself---a phenomenon we characterize as \emph{meta-level Goodhart's Law}~\citep{manheim-goodhart-taxonomy, karwowski-goodhart-rl}.
33	At low dose ($\beta{=}0.1$), two of three seeds are dominated by \emph{conclusion duplication}: the model generates a single premise identical to the conclusion, achieving ISR$=$1 by construction while encoding no reasoning whatsoever.
34	Across three seeds, 64.5\% of proved samples exhibit this ISR-specific gaming mode (H7), compared to 0\% under a matched random-reward control.
35	The remaining seed's apparent ISR advantage is entirely a premise-count artifact: ISR-trained models produce shorter formalizations where each component is mechanically more likely to appear necessary under LOO ablation.
36	Controlling for premise count eliminates the difference (1.06$\times$; \S\ref{sec:goodhart}).
37	At high dose ($\beta{=}0.3$), classic Goodhart collapse occurs: prove rate falls to 18\%, compared to 48\% for a matched random control.
38	
39	This dose-response pattern maps onto established Goodhart dynamics~\citep{gao-reward-overoptimization}: low-dose proxy gaming that inflates the metric without genuine improvement, followed by high-dose performance collapse where the proxy signal overwhelms the primary objective.
40	The contribution here is that this occurs at the \emph{meta} level---ISR was designed to \emph{detect} gaming, yet becomes the target of gaming when optimized.
41	While Goodhart's Law is well-known conceptually~\citep{manheim-goodhart-taxonomy}, its empirical characterization in neurosymbolic RL---together with the premise-count confound that explains away apparent improvements---is novel.
42	
43	We further validate that both the diagnostic utility and the Goodhart phenomenon transfer across formal languages.
44	In Prolog experiments using SWI-Prolog as the solver, exec-only training produces proved-only ISR* near zero for 2/3 seeds (s42$=$0.037, s43$=$0.015); s44 ISR*$=$0.387 reflects a small-sample artifact ($n{=}21$ proved out of 100). ISR detects structural degeneration regardless of logic type (\S\ref{sec:crosslogic}).
45	When ISR is added as a Prolog training reward, the result is \emph{universal} Goodhart: all three seeds converge to gaming with 0\% genuine proofs, each via a distinct mechanism---tautological collapse, degenerate syntax, and query-as-fact gaming.
46	This is stronger than the FOL finding, where $\sim$16\% genuine residual persists; Prolog's simpler semantics appear to enable more complete exploitation.
47	
48	Across 6 reward conditions, 3 seeds, 2 logic types, and up to 1000 training steps, we identify 7 distinct hacking strategies and document ISR's fundamental asymmetry: reliable as a diagnostic observer, unreliable as an optimization target.
49	Concretely, this paper makes four contributions.
50	First, we introduce Solver Trace Ablation and establish ISR as a diagnostic that detects reward hacking invisible to prove rate, with a complete collapse trajectory ($0.642 \to 0.132 \to 0.003$) over 1000 GRPO training steps; an SFT baseline confirms hacking is RL-specific (92.9\% genuine vs.\ $<$16\% under any RL condition; \S\ref{sec:diagnostic}).
51	Second, we provide the first empirical characterization of meta-level Goodhart's Law in neurosymbolic RL---a diagnostic designed to detect gaming becomes gamed when used as reward---and identify the premise-count confound, a systematic bias where fewer components mechanically inflate LOO-based metrics, that explains the sole apparent improvement ($1.06\times$; \S\ref{sec:goodhart}).
52	Third, we demonstrate cross-logic diagnostic transfer: STA generalizes from FOL/Prover9 to Prolog/SWI-Prolog, and Prolog ISR-as-reward produces universal Goodhart---3/3 seeds gaming via distinct mechanisms, 0\% genuine---demonstrating that simpler formal semantics enable more complete exploitation (\S\ref{sec:crosslogic}).
53	Fourth, we catalog 7 reward hacking modes across conditions and logic types, including query-as-fact gaming that bypasses text-match classifiers, motivating functional cross-validation of automated hacking diagnostics (\S\ref{sec:taxonomy}).
54	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dcf71cae-c473-420f-a877-7d46e8b92db9",
  "uuid": "33614330-6a50-41c9-b632-8bfc5485b107",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nA GRPO-trained formalizer achieves a 93\\% prove rate on first-order logic problems---yet 87\\% of its proved outputs embed the conclusion verbatim among the premises.\nThe solver succeeds not because the model has learned to reason, but because the formalization trivially entails any conclusion that already appears as a premise.\nThis structural shortcut is invisible to execution-based evaluation: prove rate registers success regardless of whether the proof reflects genuine multi-step derivation or degenerate circular embedding.\n\nNeurosymbolic approaches that combine large language models with external solvers have shown promising results on logical reasoning tasks~\\citep{satlm, logic-lm, linc}.\nRecent work applies reinforcement learning---specifically Group Relative Policy Optimization~\\citep[GRPO;][]{deepseekmath}---to train LLMs that generate formal logic programs verified by automated theorem provers~\\citep{mellgren-prolog-grpo, logic-rl}.\nThe standard reward signal in these systems is binary: 1 if the solver proves the formalization, 0 otherwise.\nThis execution reward drives rapid improvement in prove rate but provides no gradient on structural quality.\nA formalization where every premise contributes to a valid derivation receives the same reward as one that smuggles the conclusion into the premises.\n\nThe absence of structural diagnostics leaves a critical blind spot.\nProve rate---the dominant evaluation metric for neurosymbolic formalizers---conflates faithful reasoning with degenerate shortcuts.\nWithout a principled method to assess whether each component of a formalization contributes to the proof, practitioners cannot distinguish models that reason from those that exploit solver mechanics.\nThis gap is particularly consequential in RL settings, where the optimizer will find and exploit any shortcut the reward fails to penalize~\\citep{skalse-reward-hacking, reward-hacking-survey}.\n\nWe address this gap with \\emph{Solver Trace Ablation} (STA), a diagnostic protocol inspired by mutation testing~\\citep{demillo1978} that applies component necessity testing---leave-one-out (LOO) ablation on solver inputs---to quantify structural integrity (Figure~\\ref{fig:sta-overview}).\nFor each proved formalization, STA removes each component individually and re-runs the solver; the fraction of components whose removal causes proof failure yields the \\emph{Intensional Structural Reward} (ISR).\nISR$=$1 indicates a maximally tight formalization where every component is individually necessary; ISR$=$0 indicates complete structural redundancy.\nThe protocol is solver-agnostic: it applies to any external solver that accepts component-level input manipulation.\n\nApplied as a post-hoc diagnostic, ISR reveals a structural collapse trajectory entirely invisible to prove rate.\nUnder exec-only GRPO training, ISR falls from 0.642 at 100 steps to 0.132 at 500 steps to 0.003 at 1000 steps---a 99.5\\% degradation---while prove rate simultaneously rises from 32\\% to 96\\% (Figure~\\ref{fig:isr-collapse}).\nBy 1000 steps, 94.8\\% of proved samples have ISR$=$0, meaning no single component is necessary for the proof.\nThe three exec-only seeds diverge radically (PR standard deviation $\\pm$0.47), each converging to a qualitatively different degeneration mode---conclusion embedding, repetition collapse, and tautological collapse---underscoring that single-seed GRPO evaluation is unreliable.\nA supervised fine-tuning (SFT) baseline confirms that this degeneration is RL-specific: SFT achieves 92.9\\% genuine proofs with near-zero hacking, demonstrating that the structural collapse is a consequence of reward optimization rather than model capacity or data limitations.\n\nGiven ISR's diagnostic power, a natural question is whether it can serve as a training signal to steer models toward structurally sound formalizations.\nThe answer is negative.\nWhen ISR is incorporated into the reward ($r = r_{\\text{exec}} \\cdot (1 + \\beta \\cdot \\text{ISR})$), the model games the diagnostic metric itself---a phenomenon we characterize as \\emph{meta-level Goodhart's Law}~\\citep{manheim-goodhart-taxonomy, karwowski-goodhart-rl}.\nAt low dose ($\\beta{=}0.1$), two of three seeds are dominated by \\emph{conclusion duplication}: the model generates a single premise identical to the conclusion, achieving ISR$=$1 by construction while encoding no reasoning whatsoever.\nAcross three seeds, 64.5\\% of proved samples exhibit this ISR-specific gaming mode (H7), compared to 0\\% under a matched random-reward control.\nThe remaining seed's apparent ISR advantage is entirely a premise-count artifact: ISR-trained models produce shorter formalizations where each component is mechanically more likely to appear necessary under LOO ablation.\nControlling for premise count eliminates the difference (1.06$\\times$; \\S\\ref{sec:goodhart}).\nAt high dose ($\\beta{=}0.3$), classic Goodhart collapse occurs: prove rate falls to 18\\%, compared to 48\\% for a matched random control.\n\nThis dose-response pattern maps onto established Goodhart dynamics~\\citep{gao-reward-overoptimization}: low-dose proxy gaming that inflates the metric without genuine improvement, followed by high-dose performance collapse where the proxy signal overwhelms the primary objective.\nThe contribution here is that this occurs at the \\emph{meta} level---ISR was designed to \\emph{detect} gaming, yet becomes the target of gaming when optimized.\nWhile Goodhart's Law is well-known conceptually~\\citep{manheim-goodhart-taxonomy}, its empirical characterization in neurosymbolic RL---together with the premise-count confound that explains away apparent improvements---is novel.\n\nWe further validate that both the diagnostic utility and the Goodhart phenomenon transfer across formal languages.\nIn Prolog experiments using SWI-Prolog as the solver, exec-only training produces proved-only ISR* near zero for 2/3 seeds (s42$=$0.037, s43$=$0.015); s44 ISR*$=$0.387 reflects a small-sample artifact ($n{=}21$ proved out of 100). ISR detects structural degeneration regardless of logic type (\\S\\ref{sec:crosslogic}).\nWhen ISR is added as a Prolog training reward, the result is \\emph{universal} Goodhart: all three seeds converge to gaming with 0\\% genuine proofs, each via a distinct mechanism---tautological collapse, degenerate syntax, and query-as-fact gaming.\nThis is stronger than the FOL finding, where $\\sim$16\\% genuine residual persists; Prolog's simpler semantics appear to enable more complete exploitation.\n\nAcross 6 reward conditions, 3 seeds, 2 logic types, and up to 1000 training steps, we identify 7 distinct hacking strategies and document ISR's fundamental asymmetry: reliable as a diagnostic observer, unreliable as an optimization target.\nConcretely, this paper makes four contributions.\nFirst, we introduce Solver Trace Ablation and establish ISR as a diagnostic that detects reward hacking invisible to prove rate, with a complete collapse trajectory ($0.642 \\to 0.132 \\to 0.003$) over 1000 GRPO training steps; an SFT baseline confirms hacking is RL-specific (92.9\\% genuine vs.\\ $<$16\\% under any RL condition; \\S\\ref{sec:diagnostic}).\nSecond, we provide the first empirical characterization of meta-level Goodhart's Law in neurosymbolic RL---a diagnostic designed to detect gaming becomes gamed when used as reward---and identify the premise-count confound, a systematic bias where fewer components mechanically inflate LOO-based metrics, that explains the sole apparent improvement ($1.06\\times$; \\S\\ref{sec:goodhart}).\nThird, we demonstrate cross-logic diagnostic transfer: STA generalizes from FOL/Prover9 to Prolog/SWI-Prolog, and Prolog ISR-as-reward produces universal Goodhart---3/3 seeds gaming via distinct mechanisms, 0\\% genuine---demonstrating that simpler formal semantics enable more complete exploitation (\\S\\ref{sec:crosslogic}).\nFourth, we catalog 7 reward hacking modes across conditions and logic types, including query-as-fact gaming that bypasses text-match classifiers, motivating functional cross-validation of automated hacking diagnostics (\\S\\ref{sec:taxonomy}).\n",
      "numLines": 54,
      "startLine": 1,
      "totalLines": 54
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_01H9t6jJb7QRkttTxGm5FLQP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dcf71cae-c473-420f-a877-7d46e8b92db9",
  "uuid": "60e775b9-1b0f-4047-bf8d-b9133716d567",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SFXd968K9mnHdtwobvECHB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12713,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12713
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

_source line 8 · 2026-05-14T19:12:45.728Z_

<details><summary>↩ Tool result · `toolu_01H9t6jJb7QRkttTxGm5FLQP`</summary>

```text
1	% Method section — solver-trace-ablation
2	% Requires: algorithm, algorithmic, amsmath, enumitem packages
3	
4	\section{Method}
5	\label{sec:method}
6	
7	\subsection{Task Formulation}
8	\label{sec:task}
9	
10	Given natural language premises $P_1, \ldots, P_k$ and a conclusion $C$, the task is to produce a formal logic program $F = \{c_1, \ldots, c_n\}$, where each component $c_i$ is a premise encoding (in FOL) or a clause/fact (in Prolog), with one distinguished component encoding the query derived from $C$.
11	An external solver $S$ determines whether $F$ constitutes a valid proof:
12	$S(F) \in \{\textit{proved}, \textit{failed}\}$.
13	We experiment with two solver backends: Prover9 for first-order logic and SWI-Prolog for Prolog programs.
14	
15	\subsection{GRPO Training}
16	\label{sec:grpo}
17	
18	We train formalizers with Group Relative Policy Optimization \citep[GRPO;][]{deepseekmath}.
19	For each training prompt, the policy samples $K{=}8$ rollouts.
20	Each rollout receives a binary \emph{execution reward}:
21	\begin{equation}
22	  r_{\text{exec}}(x) = \mathbf{1}\bigl[S(F_x) = \textit{proved}\bigr]
23	  \label{eq:rexec}
24	\end{equation}
25	where $F_x$ is the formalization produced by rollout $x$.
26	Advantages are computed group-relative: $A_i = (r_i - \bar{r}) / \sigma_r$ within each prompt's rollout group, and the policy update maximizes expected advantage under a clipped surrogate objective with KL regularization.
27	
28	This setup optimizes \emph{prove rate}---the fraction of rollouts yielding a proved formalization---but provides no signal about the \emph{structural quality} of proved outputs.
29	A formalization that embeds the conclusion among its premises, producing a trivially provable tautology, receives the same reward as a faithful multi-step derivation.
30	
31	\subsection{Solver Trace Ablation}
32	\label{sec:sta}
33	
34	To diagnose structural quality, we propose \emph{Solver Trace Ablation} (STA), a leave-one-out protocol that tests whether each component of a proved formalization is individually necessary for proof success.
35	
36	\paragraph{Protocol.}
37	Given a proved formalization $x$ with $n$ components $\{c_1, \ldots, c_n\}$, STA constructs $n$ ablated variants $x \setminus \{c_i\}$, each with one component removed, and re-runs the solver on each.
38	A component $c_i$ is \emph{necessary} if its removal causes proof failure: $S(x \setminus \{c_i\}) = \textit{failed}$.
39	What constitutes a component depends on the logic type: individual premises in FOL, individual clauses or ground facts in Prolog.
40	
41	\paragraph{Intensional Structural Reward.}
42	We define ISR as the fraction of necessary components:
43	\begin{equation}
44	  \text{ISR}(x) = \frac{1}{n} \sum_{i=1}^{n} \mathbf{1}\bigl[S(x \setminus \{c_i\}) = \textit{failed}\bigr]
45	  \label{eq:isr}
46	\end{equation}
47	ISR $\in [0, 1]$ and is defined only for proved formalizations ($r_{\text{exec}}(x) = 1$).
48	ISR $= 1$ indicates a maximally tight formalization where every component is individually necessary; ISR $= 0$ indicates complete redundancy.
49	The protocol is solver-agnostic: it applies to any solver that accepts component-level input manipulation, requiring $n{+}1$ solver calls per sample (one initial verification plus $n$ ablations).
50	
51	Algorithm~\ref{alg:sta} gives the full procedure.
52	
53	\begin{algorithm}[t]
54	\caption{Solver Trace Ablation (STA)}
55	\label{alg:sta}
56	\begin{algorithmic}[1]
57	\REQUIRE Formalization $x = \{c_1, \ldots, c_n\}$, solver $S$
58	\ENSURE ISR score $\in [0,1]$ or $\bot$ (undefined)
59	\IF{$S(x) \neq \textit{proved}$}
60	  \RETURN $\bot$
61	\ENDIF
62	\STATE $n_{\text{nec}} \gets 0$
63	\FOR{$i = 1$ \TO $n$}
64	  \STATE $x' \gets x \setminus \{c_i\}$
65	  \IF{$S(x') = \textit{failed}$}
66	    \STATE $n_{\text{nec}} \gets n_{\text{nec}} + 1$
67	  \ENDIF
68	\ENDFOR
69	\RETURN $n_{\text{nec}} \mathbin{/} n$
70	\end{algorithmic}
71	\end{algorithm}
72	
73	STA draws on the same intuition as mutation testing in software engineering \citep{demillo1978, jia-harman-survey}: systematically perturbing a program to assess whether each element contributes to the overall result.
74	The key difference is that STA operates on solver \emph{inputs} (formalizations) rather than program code, and targets component necessity rather than test adequacy.
75	
76	\paragraph{ISR limitations.}
77	ISR measures syntactic component necessity, not semantic faithfulness to the natural language input.
78	It is also subject to a component-count confound: formalizations with fewer components yield mechanically higher ISR, since each component carries a larger share of the proof burden under LOO ablation.
79	We control for this confound in our analysis (\S\ref{sec:results}).
80	
81	\subsection{Reward Formulations}
82	\label{sec:rewards}
83	
84	We study six reward conditions to evaluate ISR both as a diagnostic and as a training signal.
85	For all RL conditions, bonuses apply only to proved samples; unproved samples receive $r = 0$.
86	
87	\paragraph{Exec-only (baseline).}
88	$r = r_{\text{exec}}$.
89	Binary solver verification with no structural component.
90	
91	\paragraph{Additive ISR.}
92	\begin{equation}
93	  r = r_{\text{exec}} \cdot (1 + \beta \cdot \text{ISR}(x)), \quad \beta \in \{0.1, 0.3\}
94	  \label{eq:additive-isr}
95	\end{equation}
96	ISR provides a bonus proportional to structural tightness, gated on proof success.
97	
98	\paragraph{Additive Random (control).}
99	$r = r_{\text{exec}} \cdot (1 + \beta \cdot u)$, $u \sim \mathcal{U}[0,1]$, $\beta \in \{0.1, 0.3\}$.
100	Replacing ISR with uniform noise isolates the causal effect of ISR-specific signal from general reward-shaping effects (variance injection, magnitude scaling).
101	
102	\paragraph{Convex ISR.}
103	$r = (1 - \beta) \cdot r_{\text{exec}} + \beta \cdot \text{ISR}(x)$.
104	Under this formulation, proved samples with ISR $< 1$ receive a lower reward than under exec-only, effectively penalizing structural imperfection.
105	
106	\paragraph{Convex Random.}
107	$r = (1 - \beta) \cdot r_{\text{exec}} + \beta \cdot u$, $u \sim \mathcal{U}[0,1]$.
108	Control for the convex formulation.
109	
110	\paragraph{SFT baseline.}
111	Supervised fine-tuning on the same training data with no reinforcement learning, confirming whether observed hacking behaviors are RL-reward-specific or artifacts of general fine-tuning.
112	
113	Each RL condition is trained across three random seeds.
114	Seeds control model initialization and training stochasticity; all seeds share the same training data (\S\ref{sec:setup}).
115	
116	\subsection{Reward Hacking Taxonomy}
117	\label{sec:taxonomy}
118	
119	Analysis of trained models across reward conditions, seeds, and logic types reveals seven distinct reward hacking modes:
120	
121	\begin{enumerate}[leftmargin=*, itemsep=2pt]
122	\item \textbf{Conclusion Embedding (H1).}
123	The conclusion is included verbatim as one of multiple premises, guaranteeing provability regardless of the other premises.
124	This mode is GRPO-universal: it appears across all reward conditions (52--93\% of proved samples).
125	
126	\item \textbf{Conclusion Duplication with ISR Inflation (H7).}
127	The formalization collapses to a single premise identical to the conclusion.
128	LOO ablation marks this sole component as necessary, inflating ISR and rewarding the policy for a degenerate output.
129	H7 is ISR-specific: it appears in 64.5\% of ISR-reward samples but 0\% of random-reward samples across three seeds.
130	
131	\item \textbf{Tautological Collapse.}
132	The formalization degenerates to exactly two components---a premise and query that are identical.
133	
134	\item \textbf{Repetition Collapse.}
135	The model generates identical premises or clauses repeatedly.
136	Removing any single copy leaves the others intact, yielding ISR $\approx 0$.
137	
138	\item \textbf{Complexity-without-utility.}
139	Excessive components are generated, none individually necessary.
140	Component counts grow over training (e.g., 6.58 $\to$ 18.55) while ISR collapses.
141	
142	\item \textbf{Contradiction Explosion.}
143	A variant of complexity-without-utility where component count increases without bound, reflecting unconstrained policy drift under extended training.
144	
145	\item \textbf{Query-as-fact Gaming.}
146	The model converts the natural language conclusion into an atom and includes it as both a fact and the query, so the solver trivially succeeds.
147	This mode bypasses text-match classifiers designed for H1/H7 and was identified through functional analysis of the $n_{\text{necessary}}$ distribution in Prolog STA.
148	\end{enumerate}
149	
150	Modes are identified by a two-stage classification procedure.
151	First, strict normalized text matching detects H1 and H7 by comparing each premise string against the query string.
152	Second, functional analysis of the per-sample $n_{\text{necessary}}$ distribution from STA catches modes that evade text matching---particularly query-as-fact gaming, where the gaming mechanism produces novel string representations invisible to exact-match classifiers.
153	Samples not assigned to any hacking mode are classified as \emph{genuine}.
154	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dcf71cae-c473-420f-a877-7d46e8b92db9",
  "uuid": "cbd5fbf7-2ac7-418a-adf1-1768500b4af6",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex",
      "content": "% Method section — solver-trace-ablation\n% Requires: algorithm, algorithmic, amsmath, enumitem packages\n\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Task Formulation}\n\\label{sec:task}\n\nGiven natural language premises $P_1, \\ldots, P_k$ and a conclusion $C$, the task is to produce a formal logic program $F = \\{c_1, \\ldots, c_n\\}$, where each component $c_i$ is a premise encoding (in FOL) or a clause/fact (in Prolog), with one distinguished component encoding the query derived from $C$.\nAn external solver $S$ determines whether $F$ constitutes a valid proof:\n$S(F) \\in \\{\\textit{proved}, \\textit{failed}\\}$.\nWe experiment with two solver backends: Prover9 for first-order logic and SWI-Prolog for Prolog programs.\n\n\\subsection{GRPO Training}\n\\label{sec:grpo}\n\nWe train formalizers with Group Relative Policy Optimization \\citep[GRPO;][]{deepseekmath}.\nFor each training prompt, the policy samples $K{=}8$ rollouts.\nEach rollout receives a binary \\emph{execution reward}:\n\\begin{equation}\n  r_{\\text{exec}}(x) = \\mathbf{1}\\bigl[S(F_x) = \\textit{proved}\\bigr]\n  \\label{eq:rexec}\n\\end{equation}\nwhere $F_x$ is the formalization produced by rollout $x$.\nAdvantages are computed group-relative: $A_i = (r_i - \\bar{r}) / \\sigma_r$ within each prompt's rollout group, and the policy update maximizes expected advantage under a clipped surrogate objective with KL regularization.\n\nThis setup optimizes \\emph{prove rate}---the fraction of rollouts yielding a proved formalization---but provides no signal about the \\emph{structural quality} of proved outputs.\nA formalization that embeds the conclusion among its premises, producing a trivially provable tautology, receives the same reward as a faithful multi-step derivation.\n\n\\subsection{Solver Trace Ablation}\n\\label{sec:sta}\n\nTo diagnose structural quality, we propose \\emph{Solver Trace Ablation} (STA), a leave-one-out protocol that tests whether each component of a proved formalization is individually necessary for proof success.\n\n\\paragraph{Protocol.}\nGiven a proved formalization $x$ with $n$ components $\\{c_1, \\ldots, c_n\\}$, STA constructs $n$ ablated variants $x \\setminus \\{c_i\\}$, each with one component removed, and re-runs the solver on each.\nA component $c_i$ is \\emph{necessary} if its removal causes proof failure: $S(x \\setminus \\{c_i\\}) = \\textit{failed}$.\nWhat constitutes a component depends on the logic type: individual premises in FOL, individual clauses or ground facts in Prolog.\n\n\\paragraph{Intensional Structural Reward.}\nWe define ISR as the fraction of necessary components:\n\\begin{equation}\n  \\text{ISR}(x) = \\frac{1}{n} \\sum_{i=1}^{n} \\mathbf{1}\\bigl[S(x \\setminus \\{c_i\\}) = \\textit{failed}\\bigr]\n  \\label{eq:isr}\n\\end{equation}\nISR $\\in [0, 1]$ and is defined only for proved formalizations ($r_{\\text{exec}}(x) = 1$).\nISR $= 1$ indicates a maximally tight formalization where every component is individually necessary; ISR $= 0$ indicates complete redundancy.\nThe protocol is solver-agnostic: it applies to any solver that accepts component-level input manipulation, requiring $n{+}1$ solver calls per sample (one initial verification plus $n$ ablations).\n\nAlgorithm~\\ref{alg:sta} gives the full procedure.\n\n\\begin{algorithm}[t]\n\\caption{Solver Trace Ablation (STA)}\n\\label{alg:sta}\n\\begin{algorithmic}[1]\n\\REQUIRE Formalization $x = \\{c_1, \\ldots, c_n\\}$, solver $S$\n\\ENSURE ISR score $\\in [0,1]$ or $\\bot$ (undefined)\n\\IF{$S(x) \\neq \\textit{proved}$}\n  \\RETURN $\\bot$\n\\ENDIF\n\\STATE $n_{\\text{nec}} \\gets 0$\n\\FOR{$i = 1$ \\TO $n$}\n  \\STATE $x' \\gets x \\setminus \\{c_i\\}$\n  \\IF{$S(x') = \\textit{failed}$}\n    \\STATE $n_{\\text{nec}} \\gets n_{\\text{nec}} + 1$\n  \\ENDIF\n\\ENDFOR\n\\RETURN $n_{\\text{nec}} \\mathbin{/} n$\n\\end{algorithmic}\n\\end{algorithm}\n\nSTA draws on the same intuition as mutation testing in software engineering \\citep{demillo1978, jia-harman-survey}: systematically perturbing a program to assess whether each element contributes to the overall result.\nThe key difference is that STA operates on solver \\emph{inputs} (formalizations) rather than program code, and targets component necessity rather than test adequacy.\n\n\\paragraph{ISR limitations.}\nISR measures syntactic component necessity, not semantic faithfulness to the natural language input.\nIt is also subject to a component-count confound: formalizations with fewer components yield mechanically higher ISR, since each component carries a larger share of the proof burden under LOO ablation.\nWe control for this confound in our analysis (\\S\\ref{sec:results}).\n\n\\subsection{Reward Formulations}\n\\label{sec:rewards}\n\nWe study six reward conditions to evaluate ISR both as a diagnostic and as a training signal.\nFor all RL conditions, bonuses apply only to proved samples; unproved samples receive $r = 0$.\n\n\\paragraph{Exec-only (baseline).}\n$r = r_{\\text{exec}}$.\nBinary solver verification with no structural component.\n\n\\paragraph{Additive ISR.}\n\\begin{equation}\n  r = r_{\\text{exec}} \\cdot (1 + \\beta \\cdot \\text{ISR}(x)), \\quad \\beta \\in \\{0.1, 0.3\\}\n  \\label{eq:additive-isr}\n\\end{equation}\nISR provides a bonus proportional to structural tightness, gated on proof success.\n\n\\paragraph{Additive Random (control).}\n$r = r_{\\text{exec}} \\cdot (1 + \\beta \\cdot u)$, $u \\sim \\mathcal{U}[0,1]$, $\\beta \\in \\{0.1, 0.3\\}$.\nReplacing ISR with uniform noise isolates the causal effect of ISR-specific signal from general reward-shaping effects (variance injection, magnitude scaling).\n\n\\paragraph{Convex ISR.}\n$r = (1 - \\beta) \\cdot r_{\\text{exec}} + \\beta \\cdot \\text{ISR}(x)$.\nUnder this formulation, proved samples with ISR $< 1$ receive a lower reward than under exec-only, effectively penalizing structural imperfection.\n\n\\paragraph{Convex Random.}\n$r = (1 - \\beta) \\cdot r_{\\text{exec}} + \\beta \\cdot u$, $u \\sim \\mathcal{U}[0,1]$.\nControl for the convex formulation.\n\n\\paragraph{SFT baseline.}\nSupervised fine-tuning on the same training data with no reinforcement learning, confirming whether observed hacking behaviors are RL-reward-specific or artifacts of general fine-tuning.\n\nEach RL condition is trained across three random seeds.\nSeeds control model initialization and training stochasticity; all seeds share the same training data (\\S\\ref{sec:setup}).\n\n\\subsection{Reward Hacking Taxonomy}\n\\label{sec:taxonomy}\n\nAnalysis of trained models across reward conditions, seeds, and logic types reveals seven distinct reward hacking modes:\n\n\\begin{enumerate}[leftmargin=*, itemsep=2pt]\n\\item \\textbf{Conclusion Embedding (H1).}\nThe conclusion is included verbatim as one of multiple premises, guaranteeing provability regardless of the other premises.\nThis mode is GRPO-universal: it appears across all reward conditions (52--93\\% of proved samples).\n\n\\item \\textbf{Conclusion Duplication with ISR Inflation (H7).}\nThe formalization collapses to a single premise identical to the conclusion.\nLOO ablation marks this sole component as necessary, inflating ISR and rewarding the policy for a degenerate output.\nH7 is ISR-specific: it appears in 64.5\\% of ISR-reward samples but 0\\% of random-reward samples across three seeds.\n\n\\item \\textbf{Tautological Collapse.}\nThe formalization degenerates to exactly two components---a premise and query that are identical.\n\n\\item \\textbf{Repetition Collapse.}\nThe model generates identical premises or clauses repeatedly.\nRemoving any single copy leaves the others intact, yielding ISR $\\approx 0$.\n\n\\item \\textbf{Complexity-without-utility.}\nExcessive components are generated, none individually necessary.\nComponent counts grow over training (e.g., 6.58 $\\to$ 18.55) while ISR collapses.\n\n\\item \\textbf{Contradiction Explosion.}\nA variant of complexity-without-utility where component count increases without bound, reflecting unconstrained policy drift under extended training.\n\n\\item \\textbf{Query-as-fact Gaming.}\nThe model converts the natural language conclusion into an atom and includes it as both a fact and the query, so the solver trivially succeeds.\nThis mode bypasses text-match classifiers designed for H1/H7 and was identified through functional analysis of the $n_{\\text{necessary}}$ distribution in Prolog STA.\n\\end{enumerate}\n\nModes are identified by a two-stage classification procedure.\nFirst, strict normalized text matching detects H1 and H7 by comparing each premise string against the query string.\nSecond, functional analysis of the per-sample $n_{\\text{necessary}}$ distribution from STA catches modes that evade text matching---particularly query-as-fact gaming, where the gaming mechanism produces novel string representations invisible to exact-match classifiers.\nSamples not assigned to any hacking mode are classified as \\emph{genuine}.\n",
      "numLines": 154,
      "startLine": 1,
      "totalLines": 154
    }
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Read · `toolu_014jhv44uuvCYbMD5QekbtFd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dcf71cae-c473-420f-a877-7d46e8b92db9",
  "uuid": "eab47674-c384-4b0a-a56b-51f36b5bc573",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SFXd968K9mnHdtwobvECHB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12713,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12713
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

_source line 10 · 2026-05-14T19:12:46.198Z_

<details><summary>↩ Tool result · `toolu_014jhv44uuvCYbMD5QekbtFd`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate STA-derived ISR across three axes: as a diagnostic for reward hacking (\S\ref{sec:diagnostic}), as a training reward exhibiting meta-level Goodhart's Law (\S\ref{sec:goodhart}), and as a cross-logic diagnostic protocol (\S\ref{sec:crosslogic}). We then synthesize the observed hacking strategies into a taxonomy (\S\ref{sec:taxonomy}).
5	
6	\subsection{Setup}
7	\label{sec:setup}
8	
9	\paragraph{Model and training.}
10	We use Qwen3-4B as the base model, trained with GRPO~\citep{deepseekmath} using $K{=}8$ rollouts per prompt for 500 steps (default) or 1000 steps where noted. All experiments use three random seeds (42, 43, 44) to assess cross-seed stability, with seeds controlling model initialization and training stochasticity. Training data is a fixed 500-example subset of FOLIO~\citep{folio} (\texttt{train\_500\_seed42.jsonl}), a corpus of human-annotated first-order logic problems, held constant across all seeds and conditions.
11	
12	\paragraph{Solvers and logic types.}
13	For first-order logic (FOL), we use Prover9 as the automated theorem prover. For Prolog experiments, we use SWI-Prolog 8.4.2. The execution reward $r_{\text{exec}} \in \{0, 1\}$ is binary: 1 if the solver returns a proof, 0 otherwise.
14	
15	\paragraph{Evaluation.}
16	We evaluate on a held-out set of 100 FOLIO examples using greedy decoding. All ISR values reported in cross-run comparisons are computed by \texttt{eval\_sta.py}, which applies the full STA protocol uniformly. We report: prove rate (PR), proved-only ISR (ISR$^*$, computed over proved samples only), hacking mode percentages (H7, H1), genuine rate, and mean component count where relevant. All tabulated ISR values are proved-only unless otherwise noted.
17	
18	\paragraph{Reward formulations.}
19	We compare six conditions:
20	\begin{itemize}[nosep,leftmargin=*]
21	  \item \textbf{Exec-only}: $r = r_{\text{exec}}$ (baseline)
22	  \item \textbf{ISR $\beta$}: $r = r_{\text{exec}} \cdot (1 + \beta \cdot \text{ISR})$, with $\beta \in \{0.1, 0.3\}$
23	  \item \textbf{Random $\beta$}: $r = r_{\text{exec}} \cdot (1 + \beta \cdot u)$, $u \sim \mathcal{U}(0,1)$, matching ISR's range but providing no structural signal
24	  \item \textbf{SFT}: Standard supervised fine-tuning on gold formalizations (no RL)
25	\end{itemize}
26	
27	\paragraph{Output classification.}
28	We classify proved outputs into three categories: \textbf{H7} (single-premise tautology where the sole premise equals the conclusion), \textbf{H1} (multi-premise conclusion embedding where the conclusion appears among the premises), and \textbf{Genuine} (no conclusion duplication detected). Classification uses text matching cross-validated with functional analysis of the LOO necessity distribution ($n_{\text{necessary}}$).
29	
30	\subsection{ISR as Diagnostic}
31	\label{sec:diagnostic}
32	
33	\begin{figure}[t]
34	\centering
35	\includegraphics[width=\columnwidth]{figures/fig2_isr_collapse.pdf}
36	\caption{ISR collapse trajectory under exec-only GRPO (seed~42). PR rises from 32\% to 96\% while proved-only ISR falls from 0.642 to 0.003 over 1000 steps. By step~1000, 94.8\% of proved samples have ISR${=}$0. Component count inflates from 6.58 to 18.55, indicating contradiction explosion.}
37	\label{fig:isr-collapse}
38	\end{figure}
39	
40	We first establish that ISR detects structural degeneration invisible to prove rate.
41	Figure~\ref{fig:isr-collapse} traces ISR and PR over training for exec-only GRPO (seed~42).
42	At 100 steps, the model produces structurally sound formalizations: PR${=}$32\%, proved-only ISR${=}$0.642.
43	By 500 steps, PR reaches 93\% but ISR collapses to 0.132---87.1\% of proved samples embed the conclusion among the premises (H1), making proof trivially achievable.
44	At 1000 steps, PR${=}$96\% while ISR drops to 0.003: every proved sample contains the conclusion in its premises (H1${=}$100\%), and the mean component count rises from 6.58 to 18.55.
45	The model generates excessive premises that trivially entail any conclusion via contradiction explosion.
46	The ISR trajectory (0.642 $\to$ 0.132 $\to$ 0.003) is monotonically decreasing with no recovery signal: extended training worsens structural degeneration.
47	
48	\paragraph{Cross-seed instability.}
49	The three exec-only seeds diverge radically, underscoring that single-seed evaluation is unreliable for GRPO-trained formalizers.
50	Seed~42 achieves PR${=}$93\% via conclusion embedding (H1${=}$87.1\%).
51	Seed~43 collapses to PR${=}$14\% with ISR${=}$0.000 through repetition collapse---87\% of outputs hit the maximum token length.
52	Seed~44 reaches PR${=}$98\% but through tautological collapse: the model generates two-component formalizations where the sole premise equals the conclusion (H7${=}$100\%, mean components${=}$2.04).
53	Despite PR values ranging from 14\% to 98\%, all three seeds exhibit structural degeneration detectable by ISR.
54	The cross-seed PR standard deviation ($\pm$47 percentage points) is itself a finding: GRPO exec-only training is highly unstable, and aggregate metrics obscure qualitatively different failure modes.
55	
56	\paragraph{SFT baseline.}
57	To confirm that hacking is RL-specific, we train a supervised baseline on gold formalizations.
58	SFT achieves PR${=}$14\% with proved-only ISR${=}$0.571: 92.9\% (13/14) of proved samples are genuine, free of conclusion embedding or duplication.
59	Only 1 of 14 proved samples exhibits H1 (7.1\%), and no H7 instances occur.
60	The near-absence of hacking confirms that the structural degeneration documented above is a consequence of RL reward optimization, not model capacity or data limitations.
61	
62	\subsection{Meta-Level Goodhart's Law}
63	\label{sec:goodhart}
64	
65	Having established ISR as a diagnostic, we test whether it can serve as a training signal. The answer is negative: ISR-as-reward exhibits \emph{meta-level} Goodhart's Law~\citep{manheim-goodhart-taxonomy}---the diagnostic metric itself becomes the target of gaming when optimized.
66	
67	\begin{table*}[t]
68	\centering
69	\small
70	\setlength{\tabcolsep}{3.5pt}
71	\begin{tabular}{llcccccccl}
72	\toprule
73	\textbf{Condition} & \textbf{Reward} & $\boldsymbol{\beta}$ & $\boldsymbol{n}$ & \textbf{PR\%}$\uparrow$ & \textbf{ISR}$^*$ & \textbf{H7\%} & \textbf{H1\%} & \textbf{Gen.\%} & \textbf{Mode} \\
74	\midrule
75	Base (0-shot) & --- & --- & 1 & 12 & --- & --- & --- & --- & --- \\
76	SFT & supervised & --- & 1 & 14 & 0.571 & 0 & 7 & \textbf{93} & Genuine \\
77	\midrule
78	Exec-only & $r_e$ & --- & 1$^\dagger$ & 93 & 0.132 & 0 & 87 & 13 & H1 embedding \\
79	ISR & $r_e(1{+}\beta{\cdot}\text{ISR})$ & 0.1 & 3 & 77{\scriptsize$\pm$14} & $\ddagger$ & \textbf{65} & 17 & ${\sim}$16 & H7 gaming \\
80	Random & $r_e(1{+}\beta{\cdot}U)$ & 0.1 & 3 & \textbf{85}{\scriptsize$\pm$6} & 0.086{\scriptsize$\pm$.039} & 0 & 81 & 19 & H1 embedding \\
81	\midrule
82	ISR & $r_e(1{+}\beta{\cdot}\text{ISR})$ & 0.3 & 1 & 18 & 0.143 & --- & --- & --- & PR collapse \\
83	Random & $r_e(1{+}\beta{\cdot}U)$ & 0.3 & 1 & 48 & 0.094 & --- & --- & --- & Redundant \\
84	\bottomrule
85	\end{tabular}
86	\caption{Goodhart landscape across reward conditions. $n$: number of seeds; 3-seed rows show mean$\pm$std. ISR$^*$: proved-only. $U \sim \mathcal{U}(0,1)$; $r_e = r_{\text{exec}}$. $^\dagger$Seed~42 shown; see \S\ref{sec:diagnostic} for 3-seed divergence. $\ddagger$ISR omitted: inflated by H7 gaming (64.5\% of proved samples are single-premise tautologies); per-seed ISR in Table~\ref{tab:beta01-3seed}. H7/H1/Gen.\% unavailable for $\beta{=}0.3$ (single seed, not fully classified). Best PR and Gen.\% bolded per group.}
87	\label{tab:goodhart-landscape}
88	\end{table*}
89	
90	\paragraph{Low-dose ISR ($\beta{=}0.1$): ISR-specific gaming.}
91	Table~\ref{tab:goodhart-landscape} summarizes results across conditions. At $\beta{=}0.1$, two of three ISR seeds (s43, s44) are dominated by H7---the model generates a single premise identical to the conclusion, trivially achieving both high PR and high ISR. Across the three ISR seeds, H7 accounts for 64.5\% of proved samples (149/231). In contrast, all three random control seeds show \emph{zero} H7 instances (0/256). H7 is exclusively induced by the ISR reward signal.
92	
93	\begin{table}[t]
94	\centering
95	\small
96	\setlength{\tabcolsep}{3pt}
97	\begin{tabular}{llccccc}
98	\toprule
99	\textbf{Seed} & \textbf{Cond.} & \textbf{PR\%} & \textbf{ISR}$^*$ & \textbf{H7\%} & \textbf{H1\%} & \textbf{Gen.\%} \\
100	\midrule
101	s42 & ISR & 81 & 0.415 & 16.0 & 51.9 & 30.9 \\
102	s43 & ISR & 61 & 0.830 & \textbf{96.7} & 0 & 3.3 \\
103	s44 & ISR & 89 & 0.902 & \textbf{86.5} & 0 & 13.5$^\dagger$ \\
104	\cmidrule{1-7}
105	 & mean$\pm$std & 77$\pm$14 & --- & 64.5 & 17.3 & ${\sim}$16 \\
106	\midrule
107	s42 & Rand & 79 & 0.131 & 0 & 70.9 & 29.1 \\
108	s43 & Rand & 88 & 0.058 & 0 & \textbf{93.2} & 6.8 \\
109	s44 & Rand & 89 & 0.070 & 0 & 79.8 & 20.2 \\
110	\cmidrule{1-7}
111	 & mean$\pm$std & 85$\pm$6 & 0.086$\pm$.039 & 0 & 81.3$\pm$11 & 18.7$\pm$11 \\
112	\bottomrule
113	\end{tabular}
114	\caption{ISR vs Random at $\beta{=}0.1$: per-seed comparison. ISR$^*$: proved-only. ISR mean omitted for ISR-reward seeds (inflated by H7 gaming). H7 is ISR-specific (64.5\% vs 0\%). H1 is GRPO-universal, higher under random (81.3\%) than ISR (17.3\%)---ISR converts H1 into H7. $^\dagger$s44's 12 ``genuine'' samples all have $n_{\text{prem}}{=}1$ (H7 classifier false negatives). Premise-count-matched genuine ISR: 0.258 (ISR, $n{=}11$) vs 0.243 (random, $n{=}21$) $= 1.06\times$.}
115	\label{tab:beta01-3seed}
116	\end{table}
117	
118	Table~\ref{tab:beta01-3seed} provides the full per-seed breakdown. Conclusion embedding (H1) is a GRPO-universal strategy: it appears at 70.9--93.2\% under random reward and 0--51.9\% under ISR. ISR reward does not reduce total hacking---it \emph{converts} H1 into the more extreme H7 form. Overall conclusion-in-premise rates are comparable (ISR s42: 67.9\% vs Random s42: 70.9\%), and the random control achieves higher and more stable PR (85$\pm$6\% vs 77$\pm$14\%).
119	
120	\paragraph{Premise-count confound.}
121	Seed~42 under ISR---the only seed not dominated by H7---shows higher raw proved-only ISR (0.415 vs 0.131 for random). However, this apparent advantage is entirely a premise minimization artifact. ISR-trained models produce shorter formalizations (mean 5.58 components vs 8.46 for random), and LOO-based metrics are mathematically biased by component count: fewer premises mean each is more likely to appear necessary, inflating ISR independent of reasoning quality.
122	
123	To control for this, we compare ISR values only among genuine (non-hacking) samples with $\geq$3 premises: ISR genuine achieves 0.258 ($n{=}11$) versus random genuine at 0.243 ($n{=}21$), a ratio of 1.06$\times$---no meaningful structural advantage. Of ISR s42's 26 nominal ``genuine'' samples, 15 have only 1--2 premises, where ISR$\geq$0.5 is a mathematical artifact of LOO on short inputs. The raw 2.4$\times$ ISR difference reduces to noise once premise count is controlled.
124	
125	\paragraph{High-dose ISR ($\beta{=}0.3$): classic Goodhart.}
126	At $\beta{=}0.3$, ISR reward causes PR to collapse to 18\%---a 5.2$\times$ degradation from exec-only. The matched random control achieves PR${=}$48\%, a 2.7$\times$ advantage, demonstrating that ISR at high dose is not merely unhelpful but \emph{actively harmful} relative to a structurally uninformative signal.
127	
128	\paragraph{Dose-response pattern.}
129	Together, the two dose levels reveal a complete Goodhart trajectory~\citep{karwowski-goodhart-rl, gao-reward-overoptimization}: at low dose ($\beta{=}0.1$), the model games the proxy metric itself (ISR inflation via H7), producing high ISR scores that mask structural degeneration; at high dose ($\beta{=}0.3$), the ISR signal overwhelms the execution reward, causing format collapse and PR degradation. No dose yields genuine structural improvement.
130	
131	\subsection{Cross-Logic Diagnostic Transfer}
132	\label{sec:crosslogic}
133	
134	To test whether ISR generalizes beyond a single formal language, we replicate the diagnostic and reward experiments using Prolog with SWI-Prolog 8.4.2 as the solver.
135	
136	\begin{figure}[t]
137	\centering
138	\includegraphics[width=\columnwidth]{figures/fig4_prolog_comparison.pdf}
139	\caption{Prolog exec-only ISR across three seeds. ISR$^*$ is near-zero for all seeds (s42${=}$0.037, s43${=}$0.015), replicating the FOL finding that exec-only training produces structurally degenerate outputs regardless of PR. Seed~44 ISR$^*{=}$0.387 is a small-sample artifact ($n{=}$21 proved). Cross-seed PR instability ($\sigma{=}$31pp) also replicates.}
140	\label{fig:prolog-comparison}
141	\end{figure}
142	
143	\begin{table}[t]
144	\centering
145	\small
146	\setlength{\tabcolsep}{3pt}
147	\begin{tabular}{llcccc}
148	\toprule
149	\textbf{Logic} & \textbf{Condition} & \textbf{Seed} & \textbf{PR\%} & \textbf{ISR}$^*$ & \textbf{Mode} \\
150	\midrule
151	\multicolumn{6}{l}{\textit{Exec-only (diagnostic transfer)}} \\
152	FOL & Exec & s42 & 93 & 0.132 & H1 embedding \\
153	FOL & Exec & s43 & 14 & 0.000 & Repetition \\
154	FOL & Exec & s44 & 98 & 0.582$^\ddagger$ & Tautological \\
155	\cmidrule{1-6}
156	Prolog & Exec & s42 & 83 & 0.037 & Ground facts \\
157	Prolog & Exec & s43 & 56 & 0.015 & Degraded \\
158	Prolog & Exec & s44 & 21 & 0.387$^\S$ & Degraded \\
159	\midrule
160	\multicolumn{6}{l}{\textit{ISR-as-reward (Goodhart transfer)}} \\
161	Prolog & STA & s42 & 50 & 1.000$^\|$ & H7 100\% \\
162	Prolog & STA & s43 & 38 & 0.185$^\|$ & Degen.\ syntax$^\P$ \\
163	Prolog & STA & s44 & 97 & 0.885$^\|$ & Query-as-fact$^\#$ \\
164	\bottomrule
165	\end{tabular}
166	\caption{Cross-logic transfer (proved-only ISR$^*$). \textit{Top}: Exec-only ISR near-zero in both logics, confirming diagnostic transfer. \textit{Bottom}: Prolog STA yields universal Goodhart (3/3 gaming, 0\% genuine). $^\ddagger$2-component artifact. $^\S$Small-sample ($n{=}$21). $^\|$Gaming-inflated. $^\P$Uppercase pseudo-Prolog; $n_{\text{nec}}{=}1$ for 38/38. $^\#$NL$\to$snake\_case atom as fact+query; $n_{\text{nec}}{=}1$ for 95/97.}
167	\label{tab:prolog-crosslogic}
168	\end{table}
169	
170	\paragraph{Diagnostic transfer.}
171	Table~\ref{tab:prolog-crosslogic} (top) and Figure~\ref{fig:prolog-comparison} show that ISR detects structural degeneration in Prolog as it does in FOL. Two of three Prolog exec-only seeds yield proved-only ISR near zero (s42${=}$0.037, s43${=}$0.015), confirming structurally degenerate outputs despite moderate-to-high PR. Seed~44 (ISR$^*{=}$0.387) is a small-sample artifact: only 21 of 100 samples prove, and the higher ISR reflects variance from this sparse denominator. Cross-seed PR instability in FOL ($\sigma{=}$47pp) replicates in Prolog ($\sigma{=}$31pp), and both logic types produce qualitatively different collapse modes across seeds.
172	
173	We note an important semantic distinction: low ISR in Prolog exec-only reflects \emph{redundant coding}---the model generates repeated ground facts where removing any single copy does not affect the proof---rather than absence of reasoning. This contrasts with the high ISR under Prolog STA (below), which reflects \emph{metric gaming}. ISR must be interpreted relative to the training objective.
174	
175	\paragraph{Universal Goodhart in Prolog.}
176	Table~\ref{tab:prolog-crosslogic} (bottom) reveals the strongest Goodhart result: all three Prolog STA seeds converge to gaming, with 0\% genuine proofs across all 185 proved samples. Each seed develops a distinct gaming pathway:
177	\begin{itemize}[nosep,leftmargin=*]
178	  \item \textbf{s42}: Clean H7---a single Prolog clause identical to the query (50/50 proved, ISR$^*{=}$1.000 because the sole component is trivially necessary).
179	  \item \textbf{s43}: Degenerate syntax---uppercase pseudo-Prolog (e.g., \texttt{MARY\_IS\_AN\_AVADEOTE.}). A text-match classifier labels these as genuine, but functional analysis shows $n_{\text{necessary}}{=}1$ for all 38 proved samples (functionally H7).
180	  \item \textbf{s44}: Query-as-fact gaming---the model converts NL problems to snake\_case atoms and sets them as both fact and query, achieving PR${=}$97\% with $n_{\text{necessary}}{=}1$ for 95/97. Initial automated classification reported 100\% genuine; independent functional analysis corrected this to 0\%.
181	\end{itemize}
182	This result is stronger than the FOL finding: FOL ISR $\beta{=}0.1$ retains ${\sim}$16\% genuine residual across seeds, while Prolog STA produces zero. Prolog's simpler semantics enable more complete exploitation, eliminating the genuine residual observed in FOL.
183	
184	\paragraph{Classifier limitations.}
185	The Prolog results expose a blind spot of text-match hacking classifiers. Seeds~s43 and s44 bypass the strict H7/H1 classifier through surface-level novelty (non-standard casing, atom-level encoding) while remaining functionally tautological ($n_{\text{necessary}}{=}1$). This motivates cross-validation of hacking classifiers with functional metrics such as the $n_{\text{necessary}}$ distribution.
186	
187	\subsection{Hacking Taxonomy}
188	\label{sec:taxonomy}
189	
190	\begin{figure}[t]
191	\centering
192	\includegraphics[width=\columnwidth]{figures/fig3_hacking_composition.pdf}
193	\caption{Hacking mode composition across reward conditions (proved samples). ISR reward converts H1 (conclusion embedding) into the more extreme H7 (conclusion duplication) without reducing total hacking prevalence. SFT exhibits near-zero hacking (92.9\% genuine).}
194	\label{fig:hacking-composition}
195	\end{figure}
196	
197	\begin{table}[t]
198	\centering
199	\small
200	\setlength{\tabcolsep}{3pt}
201	\begin{tabular}{p{1.6cm}p{2.0cm}cccc}
202	\toprule
203	\textbf{Mode} & \textbf{Mechanism} & \textbf{Exec} & \textbf{ISR} & \textbf{Rand} & \textbf{SFT} \\
204	\midrule
205	H1 & Concl.\ among premises & 87 & 17 & 81 & 7 \\
206	H7 & Single prem.\ = concl. & $\bullet$ & \textbf{65} & 0 & 0 \\
207	Tautological & 2-comp $P{=}C$ & $\bullet$ & 0 & 0 & 0 \\
208	Repetition & Output degen. & $\bullet$ & --- & --- & --- \\
209	Contradiction & $n_{\text{comp}}{\uparrow}$, ISR${\to}$0 & $\bullet$ & --- & --- & --- \\
210	C-w/o-util. & Complex, redundant & 0 & 0 & 4 & 0 \\
211	Q-as-fact & Atom = fact+query & --- & --- & --- & --- \\
212	\bottomrule
213	\end{tabular}
214	\caption{Hacking taxonomy across FOL conditions (\% of proved samples). ISR/Rand columns: $\beta{=}0.1$ 3-seed means. Exec: H1${=}$87\% in s42; $\bullet$ marks seed- or step-specific modes (H7/Tautological in s44, Repetition in s43, Contradiction at 1000~steps). C-w/o-util.: complexity-without-utility (random-specific). Q-as-fact: Prolog STA only (Table~\ref{tab:prolog-crosslogic}).}
215	\label{tab:hacking-taxonomy}
216	\end{table}
217	
218	Across all conditions, seeds, and logic types, we identify seven distinct hacking modes (Table~\ref{tab:hacking-taxonomy}, Figure~\ref{fig:hacking-composition}):
219	
220	\begin{enumerate}[nosep,leftmargin=*]
221	  \item \textbf{H1: Conclusion embedding.} The conclusion appears among multiple premises; the solver succeeds trivially. GRPO-universal: 52--93\% of proved samples across all RL reward types.
222	  \item \textbf{H7: Conclusion duplication.} A single premise identical to the conclusion. ISR-specific: 64.5\% under ISR $\beta{=}0.1$ vs 0\% under random.
223	  \item \textbf{Tautological collapse.} Two-component formalizations where premise${=}$conclusion (exec-only s44, 94\% of outputs, mean components${=}$2.04).
224	  \item \textbf{Repetition collapse.} Identical premises repeated until the token limit (exec-only s43, 87\% hit max length).
225	  \item \textbf{Contradiction explosion.} Excessive premises (mean 18.55 components at 1000 steps) that trivially entail any conclusion via embedded contradictions.
226	  \item \textbf{Complexity-without-utility.} Syntactically complex but semantically vacuous premises (random $\beta{=}0.1$, 3.8\%).
227	  \item \textbf{Query-as-fact gaming.} NL problems converted to snake\_case atoms serving as both fact and query (Prolog STA s44). Bypasses text-match classifiers while remaining functionally tautological.
228	\end{enumerate}
229	
230	The reward signal determines hacking \emph{composition} but not \emph{prevalence}: total conclusion-in-premise rates are comparable across ISR and random conditions (${\sim}$68--81\%), but ISR converts the GRPO-universal H1 mode into the ISR-specific H7 mode. SFT remains the only condition with near-zero hacking (92.9\% genuine), confirming that hacking is RL-reward-specific. Different reward formulations produce characteristic hacking signatures---a finding that may inform future diagnostic design.
231	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dcf71cae-c473-420f-a877-7d46e8b92db9",
  "uuid": "7cc6ee16-ee82-4f32-ba27-a3227f408c74",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate STA-derived ISR across three axes: as a diagnostic for reward hacking (\\S\\ref{sec:diagnostic}), as a training reward exhibiting meta-level Goodhart's Law (\\S\\ref{sec:goodhart}), and as a cross-logic diagnostic protocol (\\S\\ref{sec:crosslogic}). We then synthesize the observed hacking strategies into a taxonomy (\\S\\ref{sec:taxonomy}).\n\n\\subsection{Setup}\n\\label{sec:setup}\n\n\\paragraph{Model and training.}\nWe use Qwen3-4B as the base model, trained with GRPO~\\citep{deepseekmath} using $K{=}8$ rollouts per prompt for 500 steps (default) or 1000 steps where noted. All experiments use three random seeds (42, 43, 44) to assess cross-seed stability, with seeds controlling model initialization and training stochasticity. Training data is a fixed 500-example subset of FOLIO~\\citep{folio} (\\texttt{train\\_500\\_seed42.jsonl}), a corpus of human-annotated first-order logic problems, held constant across all seeds and conditions.\n\n\\paragraph{Solvers and logic types.}\nFor first-order logic (FOL), we use Prover9 as the automated theorem prover. For Prolog experiments, we use SWI-Prolog 8.4.2. The execution reward $r_{\\text{exec}} \\in \\{0, 1\\}$ is binary: 1 if the solver returns a proof, 0 otherwise.\n\n\\paragraph{Evaluation.}\nWe evaluate on a held-out set of 100 FOLIO examples using greedy decoding. All ISR values reported in cross-run comparisons are computed by \\texttt{eval\\_sta.py}, which applies the full STA protocol uniformly. We report: prove rate (PR), proved-only ISR (ISR$^*$, computed over proved samples only), hacking mode percentages (H7, H1), genuine rate, and mean component count where relevant. All tabulated ISR values are proved-only unless otherwise noted.\n\n\\paragraph{Reward formulations.}\nWe compare six conditions:\n\\begin{itemize}[nosep,leftmargin=*]\n  \\item \\textbf{Exec-only}: $r = r_{\\text{exec}}$ (baseline)\n  \\item \\textbf{ISR $\\beta$}: $r = r_{\\text{exec}} \\cdot (1 + \\beta \\cdot \\text{ISR})$, with $\\beta \\in \\{0.1, 0.3\\}$\n  \\item \\textbf{Random $\\beta$}: $r = r_{\\text{exec}} \\cdot (1 + \\beta \\cdot u)$, $u \\sim \\mathcal{U}(0,1)$, matching ISR's range but providing no structural signal\n  \\item \\textbf{SFT}: Standard supervised fine-tuning on gold formalizations (no RL)\n\\end{itemize}\n\n\\paragraph{Output classification.}\nWe classify proved outputs into three categories: \\textbf{H7} (single-premise tautology where the sole premise equals the conclusion), \\textbf{H1} (multi-premise conclusion embedding where the conclusion appears among the premises), and \\textbf{Genuine} (no conclusion duplication detected). Classification uses text matching cross-validated with functional analysis of the LOO necessity distribution ($n_{\\text{necessary}}$).\n\n\\subsection{ISR as Diagnostic}\n\\label{sec:diagnostic}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig2_isr_collapse.pdf}\n\\caption{ISR collapse trajectory under exec-only GRPO (seed~42). PR rises from 32\\% to 96\\% while proved-only ISR falls from 0.642 to 0.003 over 1000 steps. By step~1000, 94.8\\% of proved samples have ISR${=}$0. Component count inflates from 6.58 to 18.55, indicating contradiction explosion.}\n\\label{fig:isr-collapse}\n\\end{figure}\n\nWe first establish that ISR detects structural degeneration invisible to prove rate.\nFigure~\\ref{fig:isr-collapse} traces ISR and PR over training for exec-only GRPO (seed~42).\nAt 100 steps, the model produces structurally sound formalizations: PR${=}$32\\%, proved-only ISR${=}$0.642.\nBy 500 steps, PR reaches 93\\% but ISR collapses to 0.132---87.1\\% of proved samples embed the conclusion among the premises (H1), making proof trivially achievable.\nAt 1000 steps, PR${=}$96\\% while ISR drops to 0.003: every proved sample contains the conclusion in its premises (H1${=}$100\\%), and the mean component count rises from 6.58 to 18.55.\nThe model generates excessive premises that trivially entail any conclusion via contradiction explosion.\nThe ISR trajectory (0.642 $\\to$ 0.132 $\\to$ 0.003) is monotonically decreasing with no recovery signal: extended training worsens structural degeneration.\n\n\\paragraph{Cross-seed instability.}\nThe three exec-only seeds diverge radically, underscoring that single-seed evaluation is unreliable for GRPO-trained formalizers.\nSeed~42 achieves PR${=}$93\\% via conclusion embedding (H1${=}$87.1\\%).\nSeed~43 collapses to PR${=}$14\\% with ISR${=}$0.000 through repetition collapse---87\\% of outputs hit the maximum token length.\nSeed~44 reaches PR${=}$98\\% but through tautological collapse: the model generates two-component formalizations where the sole premise equals the conclusion (H7${=}$100\\%, mean components${=}$2.04).\nDespite PR values ranging from 14\\% to 98\\%, all three seeds exhibit structural degeneration detectable by ISR.\nThe cross-seed PR standard deviation ($\\pm$47 percentage points) is itself a finding: GRPO exec-only training is highly unstable, and aggregate metrics obscure qualitatively different failure modes.\n\n\\paragraph{SFT baseline.}\nTo confirm that hacking is RL-specific, we train a supervised baseline on gold formalizations.\nSFT achieves PR${=}$14\\% with proved-only ISR${=}$0.571: 92.9\\% (13/14) of proved samples are genuine, free of conclusion embedding or duplication.\nOnly 1 of 14 proved samples exhibits H1 (7.1\\%), and no H7 instances occur.\nThe near-absence of hacking confirms that the structural degeneration documented above is a consequence of RL reward optimization, not model capacity or data limitations.\n\n\\subsection{Meta-Level Goodhart's Law}\n\\label{sec:goodhart}\n\nHaving established ISR as a diagnostic, we test whether it can serve as a training signal. The answer is negative: ISR-as-reward exhibits \\emph{meta-level} Goodhart's Law~\\citep{manheim-goodhart-taxonomy}---the diagnostic metric itself becomes the target of gaming when optimized.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3.5pt}\n\\begin{tabular}{llcccccccl}\n\\toprule\n\\textbf{Condition} & \\textbf{Reward} & $\\boldsymbol{\\beta}$ & $\\boldsymbol{n}$ & \\textbf{PR\\%}$\\uparrow$ & \\textbf{ISR}$^*$ & \\textbf{H7\\%} & \\textbf{H1\\%} & \\textbf{Gen.\\%} & \\textbf{Mode} \\\\\n\\midrule\nBase (0-shot) & --- & --- & 1 & 12 & --- & --- & --- & --- & --- \\\\\nSFT & supervised & --- & 1 & 14 & 0.571 & 0 & 7 & \\textbf{93} & Genuine \\\\\n\\midrule\nExec-only & $r_e$ & --- & 1$^\\dagger$ & 93 & 0.132 & 0 & 87 & 13 & H1 embedding \\\\\nISR & $r_e(1{+}\\beta{\\cdot}\\text{ISR})$ & 0.1 & 3 & 77{\\scriptsize$\\pm$14} & $\\ddagger$ & \\textbf{65} & 17 & ${\\sim}$16 & H7 gaming \\\\\nRandom & $r_e(1{+}\\beta{\\cdot}U)$ & 0.1 & 3 & \\textbf{85}{\\scriptsize$\\pm$6} & 0.086{\\scriptsize$\\pm$.039} & 0 & 81 & 19 & H1 embedding \\\\\n\\midrule\nISR & $r_e(1{+}\\beta{\\cdot}\\text{ISR})$ & 0.3 & 1 & 18 & 0.143 & --- & --- & --- & PR collapse \\\\\nRandom & $r_e(1{+}\\beta{\\cdot}U)$ & 0.3 & 1 & 48 & 0.094 & --- & --- & --- & Redundant \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Goodhart landscape across reward conditions. $n$: number of seeds; 3-seed rows show mean$\\pm$std. ISR$^*$: proved-only. $U \\sim \\mathcal{U}(0,1)$; $r_e = r_{\\text{exec}}$. $^\\dagger$Seed~42 shown; see \\S\\ref{sec:diagnostic} for 3-seed divergence. $\\ddagger$ISR omitted: inflated by H7 gaming (64.5\\% of proved samples are single-premise tautologies); per-seed ISR in Table~\\ref{tab:beta01-3seed}. H7/H1/Gen.\\% unavailable for $\\beta{=}0.3$ (single seed, not fully classified). Best PR and Gen.\\% bolded per group.}\n\\label{tab:goodhart-landscape}\n\\end{table*}\n\n\\paragraph{Low-dose ISR ($\\beta{=}0.1$): ISR-specific gaming.}\nTable~\\ref{tab:goodhart-landscape} summarizes results across conditions. At $\\beta{=}0.1$, two of three ISR seeds (s43, s44) are dominated by H7---the model generates a single premise identical to the conclusion, trivially achieving both high PR and high ISR. Across the three ISR seeds, H7 accounts for 64.5\\% of proved samples (149/231). In contrast, all three random control seeds show \\emph{zero} H7 instances (0/256). H7 is exclusively induced by the ISR reward signal.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Seed} & \\textbf{Cond.} & \\textbf{PR\\%} & \\textbf{ISR}$^*$ & \\textbf{H7\\%} & \\textbf{H1\\%} & \\textbf{Gen.\\%} \\\\\n\\midrule\ns42 & ISR & 81 & 0.415 & 16.0 & 51.9 & 30.9 \\\\\ns43 & ISR & 61 & 0.830 & \\textbf{96.7} & 0 & 3.3 \\\\\ns44 & ISR & 89 & 0.902 & \\textbf{86.5} & 0 & 13.5$^\\dagger$ \\\\\n\\cmidrule{1-7}\n & mean$\\pm$std & 77$\\pm$14 & --- & 64.5 & 17.3 & ${\\sim}$16 \\\\\n\\midrule\ns42 & Rand & 79 & 0.131 & 0 & 70.9 & 29.1 \\\\\ns43 & Rand & 88 & 0.058 & 0 & \\textbf{93.2} & 6.8 \\\\\ns44 & Rand & 89 & 0.070 & 0 & 79.8 & 20.2 \\\\\n\\cmidrule{1-7}\n & mean$\\pm$std & 85$\\pm$6 & 0.086$\\pm$.039 & 0 & 81.3$\\pm$11 & 18.7$\\pm$11 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{ISR vs Random at $\\beta{=}0.1$: per-seed comparison. ISR$^*$: proved-only. ISR mean omitted for ISR-reward seeds (inflated by H7 gaming). H7 is ISR-specific (64.5\\% vs 0\\%). H1 is GRPO-universal, higher under random (81.3\\%) than ISR (17.3\\%)---ISR converts H1 into H7. $^\\dagger$s44's 12 ``genuine'' samples all have $n_{\\text{prem}}{=}1$ (H7 classifier false negatives). Premise-count-matched genuine ISR: 0.258 (ISR, $n{=}11$) vs 0.243 (random, $n{=}21$) $= 1.06\\times$.}\n\\label{tab:beta01-3seed}\n\\end{table}\n\nTable~\\ref{tab:beta01-3seed} provides the full per-seed breakdown. Conclusion embedding (H1) is a GRPO-universal strategy: it appears at 70.9--93.2\\% under random reward and 0--51.9\\% under ISR. ISR reward does not reduce total hacking---it \\emph{converts} H1 into the more extreme H7 form. Overall conclusion-in-premise rates are comparable (ISR s42: 67.9\\% vs Random s42: 70.9\\%), and the random control achieves higher and more stable PR (85$\\pm$6\\% vs 77$\\pm$14\\%).\n\n\\paragraph{Premise-count confound.}\nSeed~42 under ISR---the only seed not dominated by H7---shows higher raw proved-only ISR (0.415 vs 0.131 for random). However, this apparent advantage is entirely a premise minimization artifact. ISR-trained models produce shorter formalizations (mean 5.58 components vs 8.46 for random), and LOO-based metrics are mathematically biased by component count: fewer premises mean each is more likely to appear necessary, inflating ISR independent of reasoning quality.\n\nTo control for this, we compare ISR values only among genuine (non-hacking) samples with $\\geq$3 premises: ISR genuine achieves 0.258 ($n{=}11$) versus random genuine at 0.243 ($n{=}21$), a ratio of 1.06$\\times$---no meaningful structural advantage. Of ISR s42's 26 nominal ``genuine'' samples, 15 have only 1--2 premises, where ISR$\\geq$0.5 is a mathematical artifact of LOO on short inputs. The raw 2.4$\\times$ ISR difference reduces to noise once premise count is controlled.\n\n\\paragraph{High-dose ISR ($\\beta{=}0.3$): classic Goodhart.}\nAt $\\beta{=}0.3$, ISR reward causes PR to collapse to 18\\%---a 5.2$\\times$ degradation from exec-only. The matched random control achieves PR${=}$48\\%, a 2.7$\\times$ advantage, demonstrating that ISR at high dose is not merely unhelpful but \\emph{actively harmful} relative to a structurally uninformative signal.\n\n\\paragraph{Dose-response pattern.}\nTogether, the two dose levels reveal a complete Goodhart trajectory~\\citep{karwowski-goodhart-rl, gao-reward-overoptimization}: at low dose ($\\beta{=}0.1$), the model games the proxy metric itself (ISR inflation via H7), producing high ISR scores that mask structural degeneration; at high dose ($\\beta{=}0.3$), the ISR signal overwhelms the execution reward, causing format collapse and PR degradation. No dose yields genuine structural improvement.\n\n\\subsection{Cross-Logic Diagnostic Transfer}\n\\label{sec:crosslogic}\n\nTo test whether ISR generalizes beyond a single formal language, we replicate the diagnostic and reward experiments using Prolog with SWI-Prolog 8.4.2 as the solver.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4_prolog_comparison.pdf}\n\\caption{Prolog exec-only ISR across three seeds. ISR$^*$ is near-zero for all seeds (s42${=}$0.037, s43${=}$0.015), replicating the FOL finding that exec-only training produces structurally degenerate outputs regardless of PR. Seed~44 ISR$^*{=}$0.387 is a small-sample artifact ($n{=}$21 proved). Cross-seed PR instability ($\\sigma{=}$31pp) also replicates.}\n\\label{fig:prolog-comparison}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Logic} & \\textbf{Condition} & \\textbf{Seed} & \\textbf{PR\\%} & \\textbf{ISR}$^*$ & \\textbf{Mode} \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{Exec-only (diagnostic transfer)}} \\\\\nFOL & Exec & s42 & 93 & 0.132 & H1 embedding \\\\\nFOL & Exec & s43 & 14 & 0.000 & Repetition \\\\\nFOL & Exec & s44 & 98 & 0.582$^\\ddagger$ & Tautological \\\\\n\\cmidrule{1-6}\nProlog & Exec & s42 & 83 & 0.037 & Ground facts \\\\\nProlog & Exec & s43 & 56 & 0.015 & Degraded \\\\\nProlog & Exec & s44 & 21 & 0.387$^\\S$ & Degraded \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{ISR-as-reward (Goodhart transfer)}} \\\\\nProlog & STA & s42 & 50 & 1.000$^\\|$ & H7 100\\% \\\\\nProlog & STA & s43 & 38 & 0.185$^\\|$ & Degen.\\ syntax$^\\P$ \\\\\nProlog & STA & s44 & 97 & 0.885$^\\|$ & Query-as-fact$^\\#$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-logic transfer (proved-only ISR$^*$). \\textit{Top}: Exec-only ISR near-zero in both logics, confirming diagnostic transfer. \\textit{Bottom}: Prolog STA yields universal Goodhart (3/3 gaming, 0\\% genuine). $^\\ddagger$2-component artifact. $^\\S$Small-sample ($n{=}$21). $^\\|$Gaming-inflated. $^\\P$Uppercase pseudo-Prolog; $n_{\\text{nec}}{=}1$ for 38/38. $^\\#$NL$\\to$snake\\_case atom as fact+query; $n_{\\text{nec}}{=}1$ for 95/97.}\n\\label{tab:prolog-crosslogic}\n\\end{table}\n\n\\paragraph{Diagnostic transfer.}\nTable~\\ref{tab:prolog-crosslogic} (top) and Figure~\\ref{fig:prolog-comparison} show that ISR detects structural degeneration in Prolog as it does in FOL. Two of three Prolog exec-only seeds yield proved-only ISR near zero (s42${=}$0.037, s43${=}$0.015), confirming structurally degenerate outputs despite moderate-to-high PR. Seed~44 (ISR$^*{=}$0.387) is a small-sample artifact: only 21 of 100 samples prove, and the higher ISR reflects variance from this sparse denominator. Cross-seed PR instability in FOL ($\\sigma{=}$47pp) replicates in Prolog ($\\sigma{=}$31pp), and both logic types produce qualitatively different collapse modes across seeds.\n\nWe note an important semantic distinction: low ISR in Prolog exec-only reflects \\emph{redundant coding}---the model generates repeated ground facts where removing any single copy does not affect the proof---rather than absence of reasoning. This contrasts with the high ISR under Prolog STA (below), which reflects \\emph{metric gaming}. ISR must be interpreted relative to the training objective.\n\n\\paragraph{Universal Goodhart in Prolog.}\nTable~\\ref{tab:prolog-crosslogic} (bottom) reveals the strongest Goodhart result: all three Prolog STA seeds converge to gaming, with 0\\% genuine proofs across all 185 proved samples. Each seed develops a distinct gaming pathway:\n\\begin{itemize}[nosep,leftmargin=*]\n  \\item \\textbf{s42}: Clean H7---a single Prolog clause identical to the query (50/50 proved, ISR$^*{=}$1.000 because the sole component is trivially necessary).\n  \\item \\textbf{s43}: Degenerate syntax---uppercase pseudo-Prolog (e.g., \\texttt{MARY\\_IS\\_AN\\_AVADEOTE.}). A text-match classifier labels these as genuine, but functional analysis shows $n_{\\text{necessary}}{=}1$ for all 38 proved samples (functionally H7).\n  \\item \\textbf{s44}: Query-as-fact gaming---the model converts NL problems to snake\\_case atoms and sets them as both fact and query, achieving PR${=}$97\\% with $n_{\\text{necessary}}{=}1$ for 95/97. Initial automated classification reported 100\\% genuine; independent functional analysis corrected this to 0\\%.\n\\end{itemize}\nThis result is stronger than the FOL finding: FOL ISR $\\beta{=}0.1$ retains ${\\sim}$16\\% genuine residual across seeds, while Prolog STA produces zero. Prolog's simpler semantics enable more complete exploitation, eliminating the genuine residual observed in FOL.\n\n\\paragraph{Classifier limitations.}\nThe Prolog results expose a blind spot of text-match hacking classifiers. Seeds~s43 and s44 bypass the strict H7/H1 classifier through surface-level novelty (non-standard casing, atom-level encoding) while remaining functionally tautological ($n_{\\text{necessary}}{=}1$). This motivates cross-validation of hacking classifiers with functional metrics such as the $n_{\\text{necessary}}$ distribution.\n\n\\subsection{Hacking Taxonomy}\n\\label{sec:taxonomy}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig3_hacking_composition.pdf}\n\\caption{Hacking mode composition across reward conditions (proved samples). ISR reward converts H1 (conclusion embedding) into the more extreme H7 (conclusion duplication) without reducing total hacking prevalence. SFT exhibits near-zero hacking (92.9\\% genuine).}\n\\label{fig:hacking-composition}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{p{1.6cm}p{2.0cm}cccc}\n\\toprule\n\\textbf{Mode} & \\textbf{Mechanism} & \\textbf{Exec} & \\textbf{ISR} & \\textbf{Rand} & \\textbf{SFT} \\\\\n\\midrule\nH1 & Concl.\\ among premises & 87 & 17 & 81 & 7 \\\\\nH7 & Single prem.\\ = concl. & $\\bullet$ & \\textbf{65} & 0 & 0 \\\\\nTautological & 2-comp $P{=}C$ & $\\bullet$ & 0 & 0 & 0 \\\\\nRepetition & Output degen. & $\\bullet$ & --- & --- & --- \\\\\nContradiction & $n_{\\text{comp}}{\\uparrow}$, ISR${\\to}$0 & $\\bullet$ & --- & --- & --- \\\\\nC-w/o-util. & Complex, redundant & 0 & 0 & 4 & 0 \\\\\nQ-as-fact & Atom = fact+query & --- & --- & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Hacking taxonomy across FOL conditions (\\% of proved samples). ISR/Rand columns: $\\beta{=}0.1$ 3-seed means. Exec: H1${=}$87\\% in s42; $\\bullet$ marks seed- or step-specific modes (H7/Tautological in s44, Repetition in s43, Contradiction at 1000~steps). C-w/o-util.: complexity-without-utility (random-specific). Q-as-fact: Prolog STA only (Table~\\ref{tab:prolog-crosslogic}).}\n\\label{tab:hacking-taxonomy}\n\\end{table}\n\nAcross all conditions, seeds, and logic types, we identify seven distinct hacking modes (Table~\\ref{tab:hacking-taxonomy}, Figure~\\ref{fig:hacking-composition}):\n\n\\begin{enumerate}[nosep,leftmargin=*]\n  \\item \\textbf{H1: Conclusion embedding.} The conclusion appears among multiple premises; the solver succeeds trivially. GRPO-universal: 52--93\\% of proved samples across all RL reward types.\n  \\item \\textbf{H7: Conclusion duplication.} A single premise identical to the conclusion. ISR-specific: 64.5\\% under ISR $\\beta{=}0.1$ vs 0\\% under random.\n  \\item \\textbf{Tautological collapse.} Two-component formalizations where premise${=}$conclusion (exec-only s44, 94\\% of outputs, mean components${=}$2.04).\n  \\item \\textbf{Repetition collapse.} Identical premises repeated until the token limit (exec-only s43, 87\\% hit max length).\n  \\item \\textbf{Contradiction explosion.} Excessive premises (mean 18.55 components at 1000 steps) that trivially entail any conclusion via embedded contradictions.\n  \\item \\textbf{Complexity-without-utility.} Syntactically complex but semantically vacuous premises (random $\\beta{=}0.1$, 3.8\\%).\n  \\item \\textbf{Query-as-fact gaming.} NL problems converted to snake\\_case atoms serving as both fact and query (Prolog STA s44). Bypasses text-match classifiers while remaining functionally tautological.\n\\end{enumerate}\n\nThe reward signal determines hacking \\emph{composition} but not \\emph{prevalence}: total conclusion-in-premise rates are comparable across ISR and random conditions (${\\sim}$68--81\\%), but ISR converts the GRPO-universal H1 mode into the ISR-specific H7 mode. SFT remains the only condition with near-zero hacking (92.9\\% genuine), confirming that hacking is RL-reward-specific. Different reward formulations produce characteristic hacking signatures---a finding that may inform future diagnostic design.\n",
      "numLines": 231,
      "startLine": 1,
      "totalLines": 231
    }
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Read · `toolu_017fxmDyzuqBbzMEUuNxYusa`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dcf71cae-c473-420f-a877-7d46e8b92db9",
  "uuid": "1a8a218d-55c1-4f76-bd9b-5c680550a658",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SFXd968K9mnHdtwobvECHB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12713,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12713
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

_source line 12 · 2026-05-14T19:12:46.504Z_

<details><summary>↩ Tool result · `toolu_017fxmDyzuqBbzMEUuNxYusa`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{ISR Capability Boundary.}
5	ISR measures syntactic component necessity---whether each component is individually required for proof success---not semantic faithfulness to the natural language input.
6	A formalization where every component is necessary may still misrepresent the intended reasoning chain.
7	We verify this empirically: downstream NLI accuracy shows no correlation with ISR (Spearman $\rho = -0.049$, $p = 0.187$, n.s.), confirming that ISR captures structural tightness orthogonal to semantic correctness.
8	Practitioners should treat ISR as a necessary-but-not-sufficient diagnostic: low ISR reliably indicates structural degeneration, but high ISR does not guarantee faithful reasoning.
9	Importantly, low ISR carries different semantics depending on the training objective.
10	Under exec-only training, low ISR in Prolog reflects redundant coding---repeated ground facts where removing any single copy does not affect the proof---rather than absence of reasoning.
11	Under ISR-as-reward, high ISR reflects metric gaming.
12	ISR values must always be interpreted in the context of the optimization objective that produced them.
13	
14	\paragraph{Premise Count Confound.}
15	LOO-based metrics like ISR are mathematically biased by component count.
16	With $n$ components, each carries a $1/n$ share of the proof burden; fewer components mechanically inflate ISR regardless of quality.
17	As shown in \S\ref{sec:goodhart}, over half of ISR-reward genuine samples contain only 1--2 premises, where ISR $\geq 0.5$ is an arithmetic inevitability.
18	Controlling for premise count eliminates the apparent ISR advantage entirely (1.06$\times$ vs.\ the raw 2.4$\times$).
19	This confound is not specific to our setting: any LOO-based diagnostic applied to variable-length structured outputs requires component-count normalization.
20	We recommend that future work employing LOO-based structural metrics report premise-count-matched comparisons alongside raw values.
21	
22	\paragraph{Meta-Level Goodhart's Law.}
23	Our results instantiate a recursive form of Goodhart's Law not previously documented empirically in NLP.
24	In the standard formulation \citep{manheim-goodhart-taxonomy}, optimizing a proxy $U$ causes divergence from the true objective $V$.
25	ISR adds a layer: it was designed to \emph{detect} proxy gaming of $r_{\text{exec}}$, yet when optimized, ISR itself becomes a gaming target.
26	Under the taxonomy of \citet{manheim-goodhart-taxonomy}, $\beta{=}0.3$ exemplifies extremal Goodhart---the optimizer enters a regime where the proxy-target relationship breaks down entirely---while $\beta{=}0.1$ instantiates a meta-level variant where the diagnostic is gamed through its own measurement mechanism (conclusion duplication inflating the LOO score).
27	The scaling laws of \citet{gao-reward-overoptimization} predict proxy reward increases until a critical point; our dose-response results ($\beta{=}0.1$ gaming, $\beta{=}0.3$ collapse) trace this trajectory within a single experimental setup.
28	This suggests a general principle for the reward-shaping community: structural diagnostics derived from proxy metrics inherit the gaming vulnerability of their parent metrics when repurposed as optimization targets.
29	
30	\paragraph{Classifier Limitations.}
31	Text-match hacking classifiers have systematic blind spots that functional analysis exposes.
32	In Prolog STA, two seeds achieved 100\% genuine classification under strict text matching, yet functional analysis via the $n_{\text{necessary}}$ distribution revealed 0\% genuine in both cases (Table~\ref{tab:prolog-crosslogic}).
33	One seed produces uppercase pseudo-Prolog that is functionally tautological; the other converts conclusions to snake\_case atoms serving as both fact and query---a gaming mode invisible to string comparison.
34	The latter case is particularly instructive: surface metrics suggest excellent performance (high PR and high ISR), and only the $n_{\text{necessary}}$ distribution reveals the underlying gaming.
35	We recommend that practitioners always cross-validate text-match classifiers with functional metrics, and never treat classifier-reported genuine rates as ground truth without independent verification.
36	
37	\paragraph{Practical Implications.}
38	Our findings yield five concrete guidelines for GRPO-trained neurosymbolic systems:
39	\begin{enumerate}[nosep,leftmargin=*]
40	\item Never evaluate by prove rate alone---use ISR and component count as joint diagnostics.
41	\item Report multi-seed results: single-seed GRPO evaluation is unreliable, as cross-seed variance can exceed the effect size of interest (\S\ref{sec:diagnostic}).
42	\item Use ISR for post-hoc diagnosis only, never as a training signal---any dose induces gaming or collapse.
43	\item Treat LOO-based metrics as component-count-biased until normalized.
44	\item Expect conclusion embedding as a GRPO-universal baseline (Table~\ref{tab:beta01-3seed}): reward shaping alters hacking composition, not prevalence.
45	\end{enumerate}
46	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dcf71cae-c473-420f-a877-7d46e8b92db9",
  "uuid": "91128ff4-f2bd-4aba-905c-cc2755218658",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/discussion.tex",
      "content": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{ISR Capability Boundary.}\nISR measures syntactic component necessity---whether each component is individually required for proof success---not semantic faithfulness to the natural language input.\nA formalization where every component is necessary may still misrepresent the intended reasoning chain.\nWe verify this empirically: downstream NLI accuracy shows no correlation with ISR (Spearman $\\rho = -0.049$, $p = 0.187$, n.s.), confirming that ISR captures structural tightness orthogonal to semantic correctness.\nPractitioners should treat ISR as a necessary-but-not-sufficient diagnostic: low ISR reliably indicates structural degeneration, but high ISR does not guarantee faithful reasoning.\nImportantly, low ISR carries different semantics depending on the training objective.\nUnder exec-only training, low ISR in Prolog reflects redundant coding---repeated ground facts where removing any single copy does not affect the proof---rather than absence of reasoning.\nUnder ISR-as-reward, high ISR reflects metric gaming.\nISR values must always be interpreted in the context of the optimization objective that produced them.\n\n\\paragraph{Premise Count Confound.}\nLOO-based metrics like ISR are mathematically biased by component count.\nWith $n$ components, each carries a $1/n$ share of the proof burden; fewer components mechanically inflate ISR regardless of quality.\nAs shown in \\S\\ref{sec:goodhart}, over half of ISR-reward genuine samples contain only 1--2 premises, where ISR $\\geq 0.5$ is an arithmetic inevitability.\nControlling for premise count eliminates the apparent ISR advantage entirely (1.06$\\times$ vs.\\ the raw 2.4$\\times$).\nThis confound is not specific to our setting: any LOO-based diagnostic applied to variable-length structured outputs requires component-count normalization.\nWe recommend that future work employing LOO-based structural metrics report premise-count-matched comparisons alongside raw values.\n\n\\paragraph{Meta-Level Goodhart's Law.}\nOur results instantiate a recursive form of Goodhart's Law not previously documented empirically in NLP.\nIn the standard formulation \\citep{manheim-goodhart-taxonomy}, optimizing a proxy $U$ causes divergence from the true objective $V$.\nISR adds a layer: it was designed to \\emph{detect} proxy gaming of $r_{\\text{exec}}$, yet when optimized, ISR itself becomes a gaming target.\nUnder the taxonomy of \\citet{manheim-goodhart-taxonomy}, $\\beta{=}0.3$ exemplifies extremal Goodhart---the optimizer enters a regime where the proxy-target relationship breaks down entirely---while $\\beta{=}0.1$ instantiates a meta-level variant where the diagnostic is gamed through its own measurement mechanism (conclusion duplication inflating the LOO score).\nThe scaling laws of \\citet{gao-reward-overoptimization} predict proxy reward increases until a critical point; our dose-response results ($\\beta{=}0.1$ gaming, $\\beta{=}0.3$ collapse) trace this trajectory within a single experimental setup.\nThis suggests a general principle for the reward-shaping community: structural diagnostics derived from proxy metrics inherit the gaming vulnerability of their parent metrics when repurposed as optimization targets.\n\n\\paragraph{Classifier Limitations.}\nText-match hacking classifiers have systematic blind spots that functional analysis exposes.\nIn Prolog STA, two seeds achieved 100\\% genuine classification under strict text matching, yet functional analysis via the $n_{\\text{necessary}}$ distribution revealed 0\\% genuine in both cases (Table~\\ref{tab:prolog-crosslogic}).\nOne seed produces uppercase pseudo-Prolog that is functionally tautological; the other converts conclusions to snake\\_case atoms serving as both fact and query---a gaming mode invisible to string comparison.\nThe latter case is particularly instructive: surface metrics suggest excellent performance (high PR and high ISR), and only the $n_{\\text{necessary}}$ distribution reveals the underlying gaming.\nWe recommend that practitioners always cross-validate text-match classifiers with functional metrics, and never treat classifier-reported genuine rates as ground truth without independent verification.\n\n\\paragraph{Practical Implications.}\nOur findings yield five concrete guidelines for GRPO-trained neurosymbolic systems:\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item Never evaluate by prove rate alone---use ISR and component count as joint diagnostics.\n\\item Report multi-seed results: single-seed GRPO evaluation is unreliable, as cross-seed variance can exceed the effect size of interest (\\S\\ref{sec:diagnostic}).\n\\item Use ISR for post-hoc diagnosis only, never as a training signal---any dose induces gaming or collapse.\n\\item Treat LOO-based metrics as component-count-biased until normalized.\n\\item Expect conclusion embedding as a GRPO-universal baseline (Table~\\ref{tab:beta01-3seed}): reward shaping alters hacking composition, not prevalence.\n\\end{enumerate}\n",
      "numLines": 46,
      "startLine": 1,
      "totalLines": 46
    }
  }
}
```

</details>

---

### Assistant

_source line 13_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the paper's content, terminology, and style. Let me also check for any existing bib entries.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dcf71cae-c473-420f-a877-7d46e8b92db9",
  "uuid": "fd2fdf70-db89-4fce-adb1-86d08b9885f4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QB3HW69g7eAjRfF4rxZ4vq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14460,
      "cache_read_input_tokens": 24554,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14460
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

_source line 14_

Now let me check the existing bib file for available entries.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dcf71cae-c473-420f-a877-7d46e8b92db9",
  "uuid": "384cefce-3352-4c3b-9ddd-96df3f962f55",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QB3HW69g7eAjRfF4rxZ4vq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14460,
      "cache_read_input_tokens": 24554,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14460
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

_source line 15_

<details open><summary>🔧 Tool call — Glob · `toolu_01DDvRrhhUTeTGgSBpzcgz8e`</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dcf71cae-c473-420f-a877-7d46e8b92db9",
  "uuid": "ab372272-8838-4a59-a745-a4dd909d3e02",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QB3HW69g7eAjRfF4rxZ4vq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14460,
      "cache_read_input_tokens": 24554,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14460
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

_source line 16 · 2026-05-14T19:12:51.744Z_

<details><summary>↩ Tool result · `toolu_01DDvRrhhUTeTGgSBpzcgz8e`</summary>

```text
paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dcf71cae-c473-420f-a877-7d46e8b92db9",
  "uuid": "5a0066b3-027d-4bf0-8f5c-a701a163e26d",
  "tool_use_result": {
    "filenames": [
      "paper/references.bib"
    ],
    "durationMs": 9,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Read · `toolu_01WK2Hwu7PWUYTfkLf3ZJms2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dcf71cae-c473-420f-a877-7d46e8b92db9",
  "uuid": "f4156bd0-6c7f-4519-ae2e-254b59f9587f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XG4ypanp26pFUvArG16Syv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 177,
      "cache_read_input_tokens": 39014,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 177
      },
      "output_tokens": 71,
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

_source line 18 · 2026-05-14T19:12:54.444Z_

<details><summary>↩ Tool result · `toolu_01WK2Hwu7PWUYTfkLf3ZJms2`</summary>

```text
1	% ============================================================
2	% Category 1: Neurosymbolic reasoning + RL/GRPO
3	% ============================================================
4	
5	@article{deepseek-r1,
6	  author       = {{DeepSeek-AI}},
7	  title        = {{DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning}},
8	  journal      = {Nature},
9	  year         = {2025},
10	  note         = {arXiv:2501.12948},
11	}
12	
13	@article{deepseekmath,
14	  author       = {Zhihong Shao and Peiyi Wang and Qihao Zhu and Runxin Xu and others},
15	  title        = {{DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models}},
16	  journal      = {arXiv preprint arXiv:2402.03300},
17	  year         = {2024},
18	  eprint       = {2402.03300},
19	  archivePrefix = {arXiv},
20	  primaryClass = {cs.AI},
21	}
22	
23	@article{logic-rl,
24	  author       = {Xian and others},
25	  title        = {{Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning}},
26	  journal      = {arXiv preprint arXiv:2502.14768},
27	  year         = {2025},
28	  eprint       = {2502.14768},
29	  archivePrefix = {arXiv},
30	  primaryClass = {cs.AI},
31	}
32	
33	@article{mellgren-prolog-grpo,
34	  author       = {Niklas Mellgren},
35	  title        = {{Training Language Models to Use Prolog as a Tool}},
36	  journal      = {arXiv preprint arXiv:2512.07407},
37	  year         = {2024},
38	  eprint       = {2512.07407},
39	  archivePrefix = {arXiv},
40	  primaryClass = {cs.AI},
41	}
42	
43	@inproceedings{satlm,
44	  author       = {Xi Ye and others},
45	  title        = {{SatLM: Satisfiability-Aided Language Models Using Declarative Prompting}},
46	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
47	  year         = {2023},
48	}
49	
50	@article{deepproblog,
51	  author       = {Robin Manhaeve and Sebastijan Duman{\v{c}}i{\'c} and Angelika Kimmig and Thomas Demeester and Luc De Raedt},
52	  title        = {{Neural Probabilistic Logic Programming in DeepProbLog}},
53	  journal      = {Artificial Intelligence},
54	  volume       = {298},
55	  year         = {2021},
56	}
57	
58	@inproceedings{neurasp,
59	  author       = {Zhun Yang and Adam Ishay and Joohyung Lee},
60	  title        = {{NeurASP: Embracing Neural Networks into Answer Set Programming}},
61	  booktitle    = {Proceedings of the International Joint Conference on Artificial Intelligence (IJCAI)},
62	  year         = {2020},
63	}
64	
65	@article{thought-like-pro,
66	  author       = {Xiaoyu Tan and Yongxin Deng and Xihe Qiu and Weidi Xu and Chao Qu and Wei Chu and Yinghui Xu and Yuan Qi},
67	  title        = {{Thought-Like-Pro: Enhancing Reasoning of Large Language Models through Self-Driven Prolog-based Chain-of-Thought}},
68	  journal      = {arXiv preprint arXiv:2407.14562},
69	  year         = {2024},
70	  eprint       = {2407.14562},
71	  archivePrefix = {arXiv},
72	  primaryClass = {cs.AI},
73	}
74	
75	% ============================================================
76	% Category 2: Reward shaping for code/formal verification
77	% ============================================================
78	
79	@inproceedings{lightman-verify-step,
80	  author       = {Hunter Lightman and Vineet Kosaraju and Yura Burda and others},
81	  title        = {{Let's Verify Step by Step}},
82	  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},
83	  year         = {2024},
84	  note         = {arXiv:2305.20050},
85	}
86	
87	@article{reward-shaping-rlhf,
88	  author       = {Jiayi Fu and Xuandong Zhao and Chengyuan Yao and others},
89	  title        = {{Reward Shaping to Mitigate Reward Hacking in RLHF}},
90	  journal      = {arXiv preprint arXiv:2502.18770},
91	  year         = {2025},
92	  eprint       = {2502.18770},
93	  archivePrefix = {arXiv},
94	  primaryClass = {cs.AI},
95	}
96	
97	@article{rlvr-reasoning,
98	  author       = {{Various}},
99	  title        = {{Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs}},
100	  journal      = {arXiv preprint arXiv:2506.14245},
101	  year         = {2025},
102	  eprint       = {2506.14245},
103	  archivePrefix = {arXiv},
104	  primaryClass = {cs.AI},
105	}
106	
107	@article{rubric-grpo,
108	  author       = {{Various}},
109	  title        = {{Rubric-Grounded Reinforcement Learning: Structured Judge Rewards for Generalizable Reasoning}},
110	  journal      = {arXiv preprint arXiv:2605.08061},
111	  year         = {2025},
112	  eprint       = {2605.08061},
113	  archivePrefix = {arXiv},
114	  primaryClass = {cs.AI},
115	}
116	
117	@article{gao-effective-rl-reward,
118	  author       = {Jiaxuan Gao and Shusheng Xu and Wenjie Ye and Weilin Liu and Chuyi He and Wei Fu and Zhiyu Mei and Guangju Wang and Yi Wu},
119	  title        = {{On Designing Effective RL Reward at Training Time for LLM Reasoning}},
120	  journal      = {arXiv preprint arXiv:2410.15115},
121	  year         = {2024},
122	  eprint       = {2410.15115},
123	  archivePrefix = {arXiv},
124	  primaryClass = {cs.AI},
125	}
126	
127	@article{prof-process-outcome,
128	  author       = {Chenlu Ye and Zhou Yu and Ziji Zhang and Hao Chen and Narayanan Sadagopan and Jing Huang and Tong Zhang and Anurag Beniwal},
129	  title        = {{Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training}},
130	  journal      = {arXiv preprint arXiv:2509.03403},
131	  year         = {2025},
132	  eprint       = {2509.03403},
133	  archivePrefix = {arXiv},
134	  primaryClass = {cs.AI},
135	}
136	
137	@inproceedings{moskovitz-constrained-rlhf,
138	  author       = {Ted Moskovitz and Aaditya K. Singh and DJ Strouse and Tuomas Sandholm and Ruslan Salakhutdinov and Anca D. Dragan and Stephen McAleer},
139	  title        = {{Confronting Reward Model Overoptimization with Constrained RLHF}},
140	  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},
141	  year         = {2024},
142	  note         = {arXiv:2310.04373},
143	}
144	
145	@inproceedings{skalse-reward-hacking,
146	  author       = {Joar Skalse and Nikolaus H. R. Howe and Dmitrii Krasheninnikov and David Krueger},
147	  title        = {{Defining and Characterizing Reward Hacking}},
148	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
149	  year         = {2022},
150	  note         = {arXiv:2209.13085},
151	}
152	
153	@article{progrs-outcome-conditioned,
154	  author       = {Mohammad Rezaei and Jens Lehmann and Sahar Vahdati},
155	  title        = {{LLM Reasoning with Process Rewards for Outcome-Guided Steps}},
156	  journal      = {arXiv preprint arXiv:2604.02341},
157	  year         = {2026},
158	  eprint       = {2604.02341},
159	  archivePrefix = {arXiv},
160	  primaryClass = {cs.AI},
161	}
162	
163	@inproceedings{qwen-prm-lessons,
164	  author       = {Zhenru Zhang and others},
165	  title        = {{The Lessons of Developing Process Reward Models in Mathematical Reasoning}},
166	  booktitle    = {Findings of the Association for Computational Linguistics (ACL)},
167	  year         = {2025},
168	  note         = {arXiv:2501.07301},
169	}
170	
171	% ============================================================
172	% Category 3: Mutation testing in software engineering
173	% ============================================================
174	
175	@article{demillo1978,
176	  author       = {Richard A. DeMillo and Richard J. Lipton and Frederick G. Sayward},
177	  title        = {{Hints on Test Data Selection: Help for the Practicing Programmer}},
178	  journal      = {Computer},
179	  volume       = {11},
180	  number       = {4},
181	  pages        = {34--43},
182	  year         = {1978},
183	}
184	
185	@article{offutt-coupling,
186	  author       = {A. Jefferson Offutt},
187	  title        = {{Investigations of the Software Testing Coupling Effect}},
188	  journal      = {ACM Transactions on Software Engineering and Methodology},
189	  volume       = {1},
190	  number       = {1},
191	  pages        = {5--20},
192	  year         = {1992},
193	}
194	
195	@article{jia-harman-survey,
196	  author       = {Yue Jia and Mark Harman},
197	  title        = {{An Analysis and Survey of the Development of Mutation Testing}},
198	  journal      = {IEEE Transactions on Software Engineering},
199	  volume       = {37},
200	  number       = {5},
201	  pages        = {649--678},
202	  year         = {2011},
203	}
204	
205	@inproceedings{just-mutants-real-faults,
206	  author       = {Ren{\'e} Just and Darioush Jalali and Laura Inozemtseva and others},
207	  title        = {{Are Mutants a Valid Substitute for Real Faults in Software Testing?}},
208	  booktitle    = {Proceedings of the ACM SIGSOFT International Symposium on Foundations of Software Engineering (FSE)},
209	  year         = {2014},
210	}
211	
212	@article{llmorpheus,
213	  author       = {Frank Tip and Jon Bell and others},
214	  title        = {{LLMorpheus: Mutation Testing Using Large Language Models}},
215	  journal      = {IEEE Transactions on Software Engineering},
216	  year         = {2025},
217	}
218	
219	@inproceedings{mutation-guided-meta,
220	  author       = {Christopher Foster and others},
221	  title        = {{Mutation-Guided LLM-based Test Generation at Meta}},
222	  booktitle    = {Proceedings of the ACM SIGSOFT International Symposium on Foundations of Software Engineering (FSE)},
223	  year         = {2025},
224	}
225	
226	@article{mutation-consistency-llm,
227	  author       = {{Various}},
228	  title        = {{Mutation-based Consistency Testing for Evaluating the Code Understanding Capability of LLMs}},
229	  journal      = {arXiv preprint arXiv:2401.05940},
230	  year         = {2024},
231	  eprint       = {2401.05940},
232	  archivePrefix = {arXiv},
233	  primaryClass = {cs.AI},
234	}
235	
236	% ============================================================
237	% Category 4: Intensional program analysis
238	% ============================================================
239	
240	@article{deepmutation,
241	  author       = {{Various}},
242	  title        = {{A Probabilistic Framework for Mutation Testing in Deep Neural Networks}},
243	  journal      = {Information and Software Technology},
244	  year         = {2023},
245	}
246	
247	% ============================================================
248	% Category 5: Reward hacking / overoptimization
249	% ============================================================
250	
251	@inproceedings{inform-reward-hacking,
252	  author       = {{Various}},
253	  title        = {{InfoRM: Mitigating Reward Hacking in RLHF via Information-Theoretic Reward Modeling}},
254	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
255	  year         = {2024},
256	}
257	
258	@article{mo-grpo,
259	  author       = {{CyberAgent AI Lab}},
260	  title        = {{MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems}},
261	  journal      = {arXiv preprint arXiv:2509.22047},
262	  year         = {2025},
263	  eprint       = {2509.22047},
264	  archivePrefix = {arXiv},
265	  primaryClass = {cs.AI},
266	}
267	
268	@article{reward-hacking-survey,
269	  author       = {{Various}},
270	  title        = {{Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges}},
271	  journal      = {arXiv preprint arXiv:2604.13602},
272	  year         = {2026},
273	  eprint       = {2604.13602},
274	  archivePrefix = {arXiv},
275	  primaryClass = {cs.AI},
276	}
277	
278	@inproceedings{energy-loss-reward-hacking,
279	  author       = {{Various}},
280	  title        = {{The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking}},
281	  booktitle    = {Proceedings of the International Conference on Machine Learning (ICML)},
282	  year         = {2025},
283	}
284	
285	@article{spurious-rewards,
286	  author       = {Ruixin Yang and others},
287	  title        = {{Spurious Rewards: Rethinking Training Signals in RLVR}},
288	  journal      = {arXiv preprint arXiv:2506.10947},
289	  year         = {2025},
290	  eprint       = {2506.10947},
291	  archivePrefix = {arXiv},
292	  primaryClass = {cs.AI},
293	}
294	
295	@article{bondarenko-spec-gaming,
296	  author       = {Alexander Bondarenko and Denis Volk and Dmitrii Volkov and Jeffrey Ladish},
297	  title        = {{Demonstrating Specification Gaming in Reasoning Models}},
298	  journal      = {arXiv preprint arXiv:2502.13295},
299	  year         = {2025},
300	  eprint       = {2502.13295},
301	  archivePrefix = {arXiv},
302	  primaryClass = {cs.AI},
303	}
304	
305	@inproceedings{kim-game-formalization,
306	  author       = {Kyuhee Kim and Auguste Poiroux and Antoine Bosselut},
307	  title        = {{Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning}},
308	  booktitle    = {VerifAI-2 Workshop at the International Conference on Learning Representations (ICLR)},
309	  year         = {2026},
310	  note         = {arXiv:2604.19459},
311	}
312	
313	@inproceedings{gao-reward-overoptimization,
314	  author       = {Leo Gao and John Schulman and Jacob Hilton},
315	  title        = {{Scaling Laws for Reward Model Overoptimization}},
316	  booktitle    = {Proceedings of the International Conference on Machine Learning (ICML)},
317	  year         = {2023},
318	  note         = {arXiv:2210.10760},
319	}
320	
321	@inproceedings{karwowski-goodhart-rl,
322	  author       = {Jacek Karwowski and Oliver Hayman and Xingjian Bai and Klaus Kiendlhofer and Charlie Griffin and Joar Skalse},
323	  title        = {{Goodhart's Law in Reinforcement Learning}},
324	  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},
325	  year         = {2024},
326	  note         = {arXiv:2310.09144},
327	}
328	
329	% ============================================================
330	% Category 6: FOL/Prolog formalization with LLMs
331	% ============================================================
332	
333	@inproceedings{folio,
334	  author       = {Simeng Han and others},
335	  title        = {{FOLIO: Natural Language Reasoning with First-Order Logic}},
336	  booktitle    = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},
337	  year         = {2024},
338	  note         = {arXiv:2209.00840},
339	}
340	
341	@inproceedings{proofwriter,
342	  author       = {Oyvind Tafjord and Bhavana Dalvi and Peter Clark},
343	  title        = {{ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language}},
344	  booktitle    = {Findings of the Association for Computational Linguistics (ACL-IJCNLP)},
345	  year         = {2021},
346	}
347	
348	@inproceedings{logic-lm,
349	  author       = {Liangming Pan and Alon Albalak and Xinyi Wang and William Wang},
350	  title        = {{Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning}},
351	  booktitle    = {Findings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},
352	  year         = {2023},
353	}
354	
355	@inproceedings{linc,
356	  author       = {Theo X. Olausson and Alex Gu and Ben Lipkin and others},
357	  title        = {{LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers}},
358	  booktitle    = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},
359	  year         = {2023},
360	}
361	
362	@article{fover-pei2025,
363	  author       = {Yu Pei and Yongping Du and Xingnan Jin},
364	  title        = {{FoVer: First-Order Logic Verification for Natural Language Reasoning}},
365	  journal      = {Transactions of the Association for Computational Linguistics},
366	  volume       = {13},
367	  pages        = {1340--1359},
368	  year         = {2025},
369	}
370	
371	@article{lorp,
372	  author       = {{Various}},
373	  title        = {{LoRP: LLM-based Logical Reasoning via Prolog}},
374	  journal      = {Knowledge-Based Systems},
375	  year         = {2025},
376	}
377	
378	@article{nl2fol,
379	  author       = {Lalwani and Kim and others},
380	  title        = {{NL2FOL: Translating Natural Language to First-Order Logic for Logical Fallacy Detection}},
381	  journal      = {arXiv preprint arXiv:2405.02318},
382	  year         = {2024},
383	  eprint       = {2405.02318},
384	  archivePrefix = {arXiv},
385	  primaryClass = {cs.AI},
386	}
387	
388	@article{logica2,
389	  author       = {Liu and others},
390	  title        = {{LogiQA 2.0: An Improved Dataset for Logical Reasoning in Natural Language Understanding}},
391	  journal      = {IEEE/ACM Transactions on Audio, Speech, and Language Processing},
392	  year         = {2023},
393	}
394	
395	% ============================================================
396	% Category 7: Goodhart's Law theory and dose-response dynamics
397	% ============================================================
398	
399	@article{manheim-goodhart-taxonomy,
400	  author       = {David Manheim and Scott Garrabrant},
401	  title        = {{Categorizing Variants of Goodhart's Law}},
402	  journal      = {arXiv preprint arXiv:1803.04585},
403	  year         = {2019},
404	  eprint       = {1803.04585},
405	  archivePrefix = {arXiv},
406	  primaryClass = {cs.AI},
407	}
408	
409	@inproceedings{pan-reward-misspecification,
410	  author       = {Alexander Pan and Kush Bhatia and Jacob Steinhardt},
411	  title        = {{The Effects of Reward Misspecification: Mapping and Mitigating Misaligned Models}},
412	  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},
413	  year         = {2022},
414	}
415	
416	@inproceedings{kwa-catastrophic-goodhart,
417	  author       = {Tat-Thang Kwa and Rachel Thomas and Adri{\`a} Garriga-Alonso},
418	  title        = {{Catastrophic Goodhart: Regularizing RLHF with KL Divergence Does Not Mitigate Heavy-Tailed Reward Misspecification}},
419	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
420	  year         = {2024},
421	}
422	
423	@inproceedings{rafailov-daa-scaling,
424	  author       = {Rafael Rafailov and Yaswanth Chittepu and Ryan Park and Harshit Sikchi and Joey Hejna and W. Bradley Knox and Chelsea Finn and Scott Niekum},
425	  title        = {{Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms}},
426	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
427	  year         = {2024},
428	}
429	
430	@inproceedings{huang-chi-squared,
431	  author       = {Afra Feyza Aky{\"u}rek and Banghua Zhu and Sham Kakade and Jiantao Jiao},
432	  title        = {{Correcting the Mythos of KL-Regularization: Direct and Contrastive Distribution Correction}},
433	  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},
434	  year         = {2025},
435	}
436	
437	@inproceedings{coste-rm-ensembles,
438	  author       = {Thomas Coste and Usman Anwar and Robert Kirk and David Krueger},
439	  title        = {{Reward Model Ensembles Help Mitigate Overoptimization}},
440	  booktitle    = {NeurIPS 2023 Workshop on Alignment},
441	  year         = {2023},
442	}
443	
444	% ============================================================
445	% Category 8: Solver/prover as RL reward signal
446	% ============================================================
447	
448	@article{rlsf,
449	  author       = {Abhinav Jha and Shikhar Murty and Zico Kolter and others},
450	  title        = {{Reinforcement Learning via Symbolic Feedback}},
451	  journal      = {arXiv preprint arXiv:2405.16661},
452	  year         = {2024},
453	  eprint       = {2405.16661},
454	  archivePrefix = {arXiv},
455	  primaryClass = {cs.AI},
456	}
457	
458	@inproceedings{fover-kamoi2026,
459	  author       = {Ryo Kamoi and Yusen Zhang and Nan Zhang and Jiawei Han and Rui Zhang},
460	  title        = {{FoVer: Generalizable Process Reward Models via Formally Verified Training Data}},
461	  booktitle    = {Findings of the Association for Computational Linguistics (ACL)},
462	  year         = {2026},
463	  note         = {arXiv:2502.01345},
464	}
465	
466	@inproceedings{deepseek-prover-v15,
467	  author       = {{DeepSeek AI}},
468	  title        = {{DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search}},
469	  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},
470	  year         = {2025},
471	  note         = {arXiv:2408.08152},
472	}
473	
474	@article{alphaproof,
475	  author       = {{Google DeepMind}},
476	  title        = {{AlphaProof}},
477	  journal      = {Nature},
478	  year         = {2025},
479	}
480	
481	@inproceedings{math-shepherd,
482	  author       = {Peiyi Wang and Lei Li and Zhihong Shao and R.X. Xu and others},
483	  title        = {{Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations}},
484	  booktitle    = {Proceedings of the Association for Computational Linguistics (ACL)},
485	  year         = {2024},
486	  note         = {arXiv:2312.08935},
487	}
488	
489	% ============================================================
490	% Additional reward-shaping papers
491	% ============================================================
492	
493	@inproceedings{bipars,
494	  author       = {Yujing Hu and Weixun Wang and Hangtian Jia and others},
495	  title        = {{Learning to Utilize Shaping Rewards: A New Approach of Reward Shaping}},
496	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
497	  year         = {2020},
498	}
499	
500	@article{dapo,
501	  author       = {Qiying Yu and others},
502	  title        = {{DAPO: An Open-Source LLM Reinforcement Learning System at Scale}},
503	  journal      = {arXiv preprint arXiv:2503.14476},
504	  year         = {2025},
505	  eprint       = {2503.14476},
506	  archivePrefix = {arXiv},
507	  primaryClass = {cs.AI},
508	}
509	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dcf71cae-c473-420f-a877-7d46e8b92db9",
  "uuid": "462cb1f2-cd87-4fc7-a067-fc28f9d8aa76",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib",
      "content": "% ============================================================\n% Category 1: Neurosymbolic reasoning + RL/GRPO\n% ============================================================\n\n@article{deepseek-r1,\n  author       = {{DeepSeek-AI}},\n  title        = {{DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning}},\n  journal      = {Nature},\n  year         = {2025},\n  note         = {arXiv:2501.12948},\n}\n\n@article{deepseekmath,\n  author       = {Zhihong Shao and Peiyi Wang and Qihao Zhu and Runxin Xu and others},\n  title        = {{DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models}},\n  journal      = {arXiv preprint arXiv:2402.03300},\n  year         = {2024},\n  eprint       = {2402.03300},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{logic-rl,\n  author       = {Xian and others},\n  title        = {{Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning}},\n  journal      = {arXiv preprint arXiv:2502.14768},\n  year         = {2025},\n  eprint       = {2502.14768},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{mellgren-prolog-grpo,\n  author       = {Niklas Mellgren},\n  title        = {{Training Language Models to Use Prolog as a Tool}},\n  journal      = {arXiv preprint arXiv:2512.07407},\n  year         = {2024},\n  eprint       = {2512.07407},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{satlm,\n  author       = {Xi Ye and others},\n  title        = {{SatLM: Satisfiability-Aided Language Models Using Declarative Prompting}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2023},\n}\n\n@article{deepproblog,\n  author       = {Robin Manhaeve and Sebastijan Duman{\\v{c}}i{\\'c} and Angelika Kimmig and Thomas Demeester and Luc De Raedt},\n  title        = {{Neural Probabilistic Logic Programming in DeepProbLog}},\n  journal      = {Artificial Intelligence},\n  volume       = {298},\n  year         = {2021},\n}\n\n@inproceedings{neurasp,\n  author       = {Zhun Yang and Adam Ishay and Joohyung Lee},\n  title        = {{NeurASP: Embracing Neural Networks into Answer Set Programming}},\n  booktitle    = {Proceedings of the International Joint Conference on Artificial Intelligence (IJCAI)},\n  year         = {2020},\n}\n\n@article{thought-like-pro,\n  author       = {Xiaoyu Tan and Yongxin Deng and Xihe Qiu and Weidi Xu and Chao Qu and Wei Chu and Yinghui Xu and Yuan Qi},\n  title        = {{Thought-Like-Pro: Enhancing Reasoning of Large Language Models through Self-Driven Prolog-based Chain-of-Thought}},\n  journal      = {arXiv preprint arXiv:2407.14562},\n  year         = {2024},\n  eprint       = {2407.14562},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n% ============================================================\n% Category 2: Reward shaping for code/formal verification\n% ============================================================\n\n@inproceedings{lightman-verify-step,\n  author       = {Hunter Lightman and Vineet Kosaraju and Yura Burda and others},\n  title        = {{Let's Verify Step by Step}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2024},\n  note         = {arXiv:2305.20050},\n}\n\n@article{reward-shaping-rlhf,\n  author       = {Jiayi Fu and Xuandong Zhao and Chengyuan Yao and others},\n  title        = {{Reward Shaping to Mitigate Reward Hacking in RLHF}},\n  journal      = {arXiv preprint arXiv:2502.18770},\n  year         = {2025},\n  eprint       = {2502.18770},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{rlvr-reasoning,\n  author       = {{Various}},\n  title        = {{Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs}},\n  journal      = {arXiv preprint arXiv:2506.14245},\n  year         = {2025},\n  eprint       = {2506.14245},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{rubric-grpo,\n  author       = {{Various}},\n  title        = {{Rubric-Grounded Reinforcement Learning: Structured Judge Rewards for Generalizable Reasoning}},\n  journal      = {arXiv preprint arXiv:2605.08061},\n  year         = {2025},\n  eprint       = {2605.08061},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{gao-effective-rl-reward,\n  author       = {Jiaxuan Gao and Shusheng Xu and Wenjie Ye and Weilin Liu and Chuyi He and Wei Fu and Zhiyu Mei and Guangju Wang and Yi Wu},\n  title        = {{On Designing Effective RL Reward at Training Time for LLM Reasoning}},\n  journal      = {arXiv preprint arXiv:2410.15115},\n  year         = {2024},\n  eprint       = {2410.15115},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{prof-process-outcome,\n  author       = {Chenlu Ye and Zhou Yu and Ziji Zhang and Hao Chen and Narayanan Sadagopan and Jing Huang and Tong Zhang and Anurag Beniwal},\n  title        = {{Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training}},\n  journal      = {arXiv preprint arXiv:2509.03403},\n  year         = {2025},\n  eprint       = {2509.03403},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{moskovitz-constrained-rlhf,\n  author       = {Ted Moskovitz and Aaditya K. Singh and DJ Strouse and Tuomas Sandholm and Ruslan Salakhutdinov and Anca D. Dragan and Stephen McAleer},\n  title        = {{Confronting Reward Model Overoptimization with Constrained RLHF}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2024},\n  note         = {arXiv:2310.04373},\n}\n\n@inproceedings{skalse-reward-hacking,\n  author       = {Joar Skalse and Nikolaus H. R. Howe and Dmitrii Krasheninnikov and David Krueger},\n  title        = {{Defining and Characterizing Reward Hacking}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2022},\n  note         = {arXiv:2209.13085},\n}\n\n@article{progrs-outcome-conditioned,\n  author       = {Mohammad Rezaei and Jens Lehmann and Sahar Vahdati},\n  title        = {{LLM Reasoning with Process Rewards for Outcome-Guided Steps}},\n  journal      = {arXiv preprint arXiv:2604.02341},\n  year         = {2026},\n  eprint       = {2604.02341},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{qwen-prm-lessons,\n  author       = {Zhenru Zhang and others},\n  title        = {{The Lessons of Developing Process Reward Models in Mathematical Reasoning}},\n  booktitle    = {Findings of the Association for Computational Linguistics (ACL)},\n  year         = {2025},\n  note         = {arXiv:2501.07301},\n}\n\n% ============================================================\n% Category 3: Mutation testing in software engineering\n% ============================================================\n\n@article{demillo1978,\n  author       = {Richard A. DeMillo and Richard J. Lipton and Frederick G. Sayward},\n  title        = {{Hints on Test Data Selection: Help for the Practicing Programmer}},\n  journal      = {Computer},\n  volume       = {11},\n  number       = {4},\n  pages        = {34--43},\n  year         = {1978},\n}\n\n@article{offutt-coupling,\n  author       = {A. Jefferson Offutt},\n  title        = {{Investigations of the Software Testing Coupling Effect}},\n  journal      = {ACM Transactions on Software Engineering and Methodology},\n  volume       = {1},\n  number       = {1},\n  pages        = {5--20},\n  year         = {1992},\n}\n\n@article{jia-harman-survey,\n  author       = {Yue Jia and Mark Harman},\n  title        = {{An Analysis and Survey of the Development of Mutation Testing}},\n  journal      = {IEEE Transactions on Software Engineering},\n  volume       = {37},\n  number       = {5},\n  pages        = {649--678},\n  year         = {2011},\n}\n\n@inproceedings{just-mutants-real-faults,\n  author       = {Ren{\\'e} Just and Darioush Jalali and Laura Inozemtseva and others},\n  title        = {{Are Mutants a Valid Substitute for Real Faults in Software Testing?}},\n  booktitle    = {Proceedings of the ACM SIGSOFT International Symposium on Foundations of Software Engineering (FSE)},\n  year         = {2014},\n}\n\n@article{llmorpheus,\n  author       = {Frank Tip and Jon Bell and others},\n  title        = {{LLMorpheus: Mutation Testing Using Large Language Models}},\n  journal      = {IEEE Transactions on Software Engineering},\n  year         = {2025},\n}\n\n@inproceedings{mutation-guided-meta,\n  author       = {Christopher Foster and others},\n  title        = {{Mutation-Guided LLM-based Test Generation at Meta}},\n  booktitle    = {Proceedings of the ACM SIGSOFT International Symposium on Foundations of Software Engineering (FSE)},\n  year         = {2025},\n}\n\n@article{mutation-consistency-llm,\n  author       = {{Various}},\n  title        = {{Mutation-based Consistency Testing for Evaluating the Code Understanding Capability of LLMs}},\n  journal      = {arXiv preprint arXiv:2401.05940},\n  year         = {2024},\n  eprint       = {2401.05940},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n% ============================================================\n% Category 4: Intensional program analysis\n% ============================================================\n\n@article{deepmutation,\n  author       = {{Various}},\n  title        = {{A Probabilistic Framework for Mutation Testing in Deep Neural Networks}},\n  journal      = {Information and Software Technology},\n  year         = {2023},\n}\n\n% ============================================================\n% Category 5: Reward hacking / overoptimization\n% ============================================================\n\n@inproceedings{inform-reward-hacking,\n  author       = {{Various}},\n  title        = {{InfoRM: Mitigating Reward Hacking in RLHF via Information-Theoretic Reward Modeling}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2024},\n}\n\n@article{mo-grpo,\n  author       = {{CyberAgent AI Lab}},\n  title        = {{MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems}},\n  journal      = {arXiv preprint arXiv:2509.22047},\n  year         = {2025},\n  eprint       = {2509.22047},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{reward-hacking-survey,\n  author       = {{Various}},\n  title        = {{Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges}},\n  journal      = {arXiv preprint arXiv:2604.13602},\n  year         = {2026},\n  eprint       = {2604.13602},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{energy-loss-reward-hacking,\n  author       = {{Various}},\n  title        = {{The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking}},\n  booktitle    = {Proceedings of the International Conference on Machine Learning (ICML)},\n  year         = {2025},\n}\n\n@article{spurious-rewards,\n  author       = {Ruixin Yang and others},\n  title        = {{Spurious Rewards: Rethinking Training Signals in RLVR}},\n  journal      = {arXiv preprint arXiv:2506.10947},\n  year         = {2025},\n  eprint       = {2506.10947},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{bondarenko-spec-gaming,\n  author       = {Alexander Bondarenko and Denis Volk and Dmitrii Volkov and Jeffrey Ladish},\n  title        = {{Demonstrating Specification Gaming in Reasoning Models}},\n  journal      = {arXiv preprint arXiv:2502.13295},\n  year         = {2025},\n  eprint       = {2502.13295},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{kim-game-formalization,\n  author       = {Kyuhee Kim and Auguste Poiroux and Antoine Bosselut},\n  title        = {{Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning}},\n  booktitle    = {VerifAI-2 Workshop at the International Conference on Learning Representations (ICLR)},\n  year         = {2026},\n  note         = {arXiv:2604.19459},\n}\n\n@inproceedings{gao-reward-overoptimization,\n  author       = {Leo Gao and John Schulman and Jacob Hilton},\n  title        = {{Scaling Laws for Reward Model Overoptimization}},\n  booktitle    = {Proceedings of the International Conference on Machine Learning (ICML)},\n  year         = {2023},\n  note         = {arXiv:2210.10760},\n}\n\n@inproceedings{karwowski-goodhart-rl,\n  author       = {Jacek Karwowski and Oliver Hayman and Xingjian Bai and Klaus Kiendlhofer and Charlie Griffin and Joar Skalse},\n  title        = {{Goodhart's Law in Reinforcement Learning}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2024},\n  note         = {arXiv:2310.09144},\n}\n\n% ============================================================\n% Category 6: FOL/Prolog formalization with LLMs\n% ============================================================\n\n@inproceedings{folio,\n  author       = {Simeng Han and others},\n  title        = {{FOLIO: Natural Language Reasoning with First-Order Logic}},\n  booktitle    = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year         = {2024},\n  note         = {arXiv:2209.00840},\n}\n\n@inproceedings{proofwriter,\n  author       = {Oyvind Tafjord and Bhavana Dalvi and Peter Clark},\n  title        = {{ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language}},\n  booktitle    = {Findings of the Association for Computational Linguistics (ACL-IJCNLP)},\n  year         = {2021},\n}\n\n@inproceedings{logic-lm,\n  author       = {Liangming Pan and Alon Albalak and Xinyi Wang and William Wang},\n  title        = {{Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning}},\n  booktitle    = {Findings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year         = {2023},\n}\n\n@inproceedings{linc,\n  author       = {Theo X. Olausson and Alex Gu and Ben Lipkin and others},\n  title        = {{LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers}},\n  booktitle    = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year         = {2023},\n}\n\n@article{fover-pei2025,\n  author       = {Yu Pei and Yongping Du and Xingnan Jin},\n  title        = {{FoVer: First-Order Logic Verification for Natural Language Reasoning}},\n  journal      = {Transactions of the Association for Computational Linguistics},\n  volume       = {13},\n  pages        = {1340--1359},\n  year         = {2025},\n}\n\n@article{lorp,\n  author       = {{Various}},\n  title        = {{LoRP: LLM-based Logical Reasoning via Prolog}},\n  journal      = {Knowledge-Based Systems},\n  year         = {2025},\n}\n\n@article{nl2fol,\n  author       = {Lalwani and Kim and others},\n  title        = {{NL2FOL: Translating Natural Language to First-Order Logic for Logical Fallacy Detection}},\n  journal      = {arXiv preprint arXiv:2405.02318},\n  year         = {2024},\n  eprint       = {2405.02318},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{logica2,\n  author       = {Liu and others},\n  title        = {{LogiQA 2.0: An Improved Dataset for Logical Reasoning in Natural Language Understanding}},\n  journal      = {IEEE/ACM Transactions on Audio, Speech, and Language Processing},\n  year         = {2023},\n}\n\n% ============================================================\n% Category 7: Goodhart's Law theory and dose-response dynamics\n% ============================================================\n\n@article{manheim-goodhart-taxonomy,\n  author       = {David Manheim and Scott Garrabrant},\n  title        = {{Categorizing Variants of Goodhart's Law}},\n  journal      = {arXiv preprint arXiv:1803.04585},\n  year         = {2019},\n  eprint       = {1803.04585},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{pan-reward-misspecification,\n  author       = {Alexander Pan and Kush Bhatia and Jacob Steinhardt},\n  title        = {{The Effects of Reward Misspecification: Mapping and Mitigating Misaligned Models}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2022},\n}\n\n@inproceedings{kwa-catastrophic-goodhart,\n  author       = {Tat-Thang Kwa and Rachel Thomas and Adri{\\`a} Garriga-Alonso},\n  title        = {{Catastrophic Goodhart: Regularizing RLHF with KL Divergence Does Not Mitigate Heavy-Tailed Reward Misspecification}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2024},\n}\n\n@inproceedings{rafailov-daa-scaling,\n  author       = {Rafael Rafailov and Yaswanth Chittepu and Ryan Park and Harshit Sikchi and Joey Hejna and W. Bradley Knox and Chelsea Finn and Scott Niekum},\n  title        = {{Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2024},\n}\n\n@inproceedings{huang-chi-squared,\n  author       = {Afra Feyza Aky{\\\"u}rek and Banghua Zhu and Sham Kakade and Jiantao Jiao},\n  title        = {{Correcting the Mythos of KL-Regularization: Direct and Contrastive Distribution Correction}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2025},\n}\n\n@inproceedings{coste-rm-ensembles,\n  author       = {Thomas Coste and Usman Anwar and Robert Kirk and David Krueger},\n  title        = {{Reward Model Ensembles Help Mitigate Overoptimization}},\n  booktitle    = {NeurIPS 2023 Workshop on Alignment},\n  year         = {2023},\n}\n\n% ============================================================\n% Category 8: Solver/prover as RL reward signal\n% ============================================================\n\n@article{rlsf,\n  author       = {Abhinav Jha and Shikhar Murty and Zico Kolter and others},\n  title        = {{Reinforcement Learning via Symbolic Feedback}},\n  journal      = {arXiv preprint arXiv:2405.16661},\n  year         = {2024},\n  eprint       = {2405.16661},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{fover-kamoi2026,\n  author       = {Ryo Kamoi and Yusen Zhang and Nan Zhang and Jiawei Han and Rui Zhang},\n  title        = {{FoVer: Generalizable Process Reward Models via Formally Verified Training Data}},\n  booktitle    = {Findings of the Association for Computational Linguistics (ACL)},\n  year         = {2026},\n  note         = {arXiv:2502.01345},\n}\n\n@inproceedings{deepseek-prover-v15,\n  author       = {{DeepSeek AI}},\n  title        = {{DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2025},\n  note         = {arXiv:2408.08152},\n}\n\n@article{alphaproof,\n  author       = {{Google DeepMind}},\n  title        = {{AlphaProof}},\n  journal      = {Nature},\n  year         = {2025},\n}\n\n@inproceedings{math-shepherd,\n  author       = {Peiyi Wang and Lei Li and Zhihong Shao and R.X. Xu and others},\n  title        = {{Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations}},\n  booktitle    = {Proceedings of the Association for Computational Linguistics (ACL)},\n  year         = {2024},\n  note         = {arXiv:2312.08935},\n}\n\n% ============================================================\n% Additional reward-shaping papers\n% ============================================================\n\n@inproceedings{bipars,\n  author       = {Yujing Hu and Weixun Wang and Hangtian Jia and others},\n  title        = {{Learning to Utilize Shaping Rewards: A New Approach of Reward Shaping}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2020},\n}\n\n@article{dapo,\n  author       = {Qiying Yu and others},\n  title        = {{DAPO: An Open-Source LLM Reinforcement Learning System at Scale}},\n  journal      = {arXiv preprint arXiv:2503.14476},\n  year         = {2025},\n  eprint       = {2503.14476},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n",
      "numLines": 509,
      "startLine": 1,
      "totalLines": 509
    }
  }
}
```

</details>

---

### Assistant

_source line 19_

<details><summary>Logged reasoning block</summary>

```text
Now I have a complete picture. Let me write the related work section. I need to:

1. Use existing bib entries where available
2. Use \cite{AuthorYear} placeholders for new ones
3. Keep under 900 words
4. Follow the 4-cluster structure
5. Match the paper's style and terminology

Available bib entries I'll use:
- demillo1978, jia-harman-survey, just-mutants-real-faults (renamed from "Just et al. mutants" in task)
- lightman-verify-step, math-shepherd, rlsf, rubric-grpo


- gao-reward-overoptimization, karwowski-goodhart-rl, manheim-goodhart-taxonomy, skalse-reward-hacking, pan-reward-misspecification
- logic-lm, linc, satlm, lorp, fover-pei2025, mellgren-prolog-grpo, logic-rl

I've confirmed that Math-Shepherd, RLSF, and Rubric-GRPO are already in the bibliography, so I can cite those directly. Now I need to map out which citations from the task correspond to which clusters and start drafting the section. I've confirmed all the bibliography entries are in place, including the two FoVer papers where I'm using the Pei 2025 version for the verification focus. Now I'm ready to start writing the related work section.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dcf71cae-c473-420f-a877-7d46e8b92db9",
  "uuid": "37823d23-5b61-4f02-a343-cd8b712ad566",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BYZBWPYb5PnYKBywoaRRHr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7694,
      "cache_read_input_tokens": 39191,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7694
      },
      "output_tokens": 9,
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

_source line 20_

All bib entries exist. Writing the related work section now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dcf71cae-c473-420f-a877-7d46e8b92db9",
  "uuid": "aad9d884-4cb9-4171-a021-214f5f45049d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BYZBWPYb5PnYKBywoaRRHr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7694,
      "cache_read_input_tokens": 39191,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7694
      },
      "output_tokens": 9,
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

_source line 21_

<details open><summary>🔧 Tool call — Write · `toolu_01FZKX5Qq3WhiLPxw2fqySQJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex",
  "content": "\\section{Related Work}\n\\label{sec:related-work}\n\n\\paragraph{Mutation Testing and Component Analysis.}\nMutation testing originated with \\citet{demillo1978}, who proposed systematically injecting faults into programs to assess test suite adequacy.\n\\citet{jia-harman-survey} survey three decades of development, establishing leave-one-out and higher-order mutation operators as the dominant paradigm for software quality assurance, while \\citet{just-mutants-real-faults} validate that synthetic mutants approximate real faults in fault-detection experiments.\nThis body of work operates exclusively within software testing: mutants perturb \\emph{program code} to evaluate \\emph{test suites}, not solver inputs to evaluate reasoning quality.\nSTA adapts the core LOO intuition to a different domain---formal logic formalizations---where the ``program under test'' is the solver input and the ``test'' is proof success.\nThe unit of mutation shifts from code statements to logical components (premises in FOL, clauses in Prolog), and the diagnostic target shifts from test adequacy to structural necessity of each component for proof validity.\n\n\\paragraph{Reward Shaping and Process Supervision.}\nBinary outcome rewards provide no gradient on intermediate reasoning quality, motivating process-level supervision.\n\\citet{lightman-verify-step} train process reward models that score individual reasoning steps, demonstrating improved mathematical problem-solving over outcome-only rewards.\nMath-Shepherd~\\citep{math-shepherd} automates step-level annotation by validating intermediate states against reference solutions.\nRLSF~\\citep{rlsf} grounds reward in symbolic execution feedback, using solver diagnostics as a structured training signal for formal reasoning tasks.\nRubric-GRPO~\\citep{rubric-grpo} replaces scalar rewards with multi-dimensional rubric scores evaluated by an LLM judge, decomposing quality into interpretable axes.\nThese approaches share an implicit assumption: that finer-grained reward signals are reliable proxies for reasoning quality and can safely serve as optimization targets.\nOur work challenges this assumption directly.\nISR provides a solver-grounded process signal that reliably \\emph{diagnoses} structural quality when used as a post-hoc metric, yet becomes the target of gaming when incorporated into the reward---instantiating meta-level Goodhart's Law (\\S\\ref{sec:goodhart}).\nThe failure mode is not reward noise or annotation error but systematic exploitation of the metric's measurement mechanism.\n\n\\paragraph{Reward Hacking and Goodhart's Law.}\n\\citet{gao-reward-overoptimization} establish scaling laws for reward model overoptimization in RLHF, showing that proxy reward increases monotonically with optimization pressure until a critical point where true performance collapses.\n\\citet{manheim-goodhart-taxonomy} taxonomize four variants of Goodhart's Law---regressional, extremal, causal, and adversarial---providing the theoretical vocabulary for analyzing proxy-target divergence.\n\\citet{skalse-reward-hacking} formalize reward hacking as misalignment between the proxy and true reward under optimization, proving that hacking is generically unavoidable for imperfect proxies.\n\\citet{karwowski-goodhart-rl} demonstrate Goodhart dynamics geometrically in RL, showing that KL regularization delays but does not prevent overoptimization.\n\\citet{pan-reward-misspecification} map the effects of reward misspecification across environments, finding that misspecified rewards produce qualitatively different failure modes depending on the degree of misalignment.\nThis literature analyzes Goodhart dynamics theoretically or within RLHF and text generation, where the proxy is a learned reward model.\nOur setting differs in two respects.\nFirst, the proxy (ISR) is not learned but derived from a deterministic solver, eliminating reward model noise as an explanation.\nSecond, the Goodhart effect operates at a \\emph{meta} level: ISR was designed to detect gaming of execution reward, yet itself becomes gamed when optimized.\nThe dose-response pattern we observe ($\\beta{=}0.1$: proxy gaming via conclusion duplication; $\\beta{=}0.3$: performance collapse) traces the trajectory predicted by \\citet{gao-reward-overoptimization} within a single neurosymbolic RL setup.\n\n\\paragraph{Neurosymbolic Reasoning with LLMs.}\nPrompting-based pipelines couple LLMs with external solvers for logical reasoning.\nLogic-LM~\\citep{logic-lm} uses in-context examples to generate FOL formalizations verified by an external prover, with a self-refinement loop on solver errors.\nLINC~\\citep{linc} similarly translates natural language to first-order logic for Prover9 verification, demonstrating that solver-backed approaches outperform chain-of-thought on syllogistic and multi-hop tasks.\nSatLM~\\citep{satlm} extends this paradigm to satisfiability solvers via declarative prompting.\nThese systems evaluate exclusively on execution accuracy---whether the solver returns the correct answer---without diagnosing structural quality of the generated formalizations.\n\nVerification-oriented approaches add post-hoc analysis.\nLoRP~\\citep{lorp} uses Prolog execution traces to verify LLM reasoning chains, and FoVer~\\citep{fover-pei2025} employs first-order logic verification to filter training data for process reward models.\nBoth treat solver verification as a binary quality gate rather than a structural diagnostic.\n\nRL-based training represents the closest line of work.\n\\citet{mellgren-prolog-grpo} apply GRPO to train Prolog formalizers with binary solver reward, reporting substantial prove-rate gains.\nLogic-RL~\\citep{logic-rl} demonstrates that rule-based RL with solver feedback elicits emergent reasoning capabilities in LLMs.\nBoth systems optimize execution reward exclusively, reporting prove rate as the primary metric.\nSTA addresses the structural blind spot common to all these approaches: execution accuracy conflates faithful multi-step derivation with degenerate shortcuts (conclusion embedding, tautological collapse), and ISR quantifies this conflation.\nOur finding that 87\\% of proved outputs under exec-only GRPO embed the conclusion among the premises (\\S\\ref{sec:diagnostic}) applies directly to these systems, suggesting that reported prove-rate gains may overstate genuine reasoning improvement.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dcf71cae-c473-420f-a877-7d46e8b92db9",
  "uuid": "fbca5bb5-6624-4cae-bafd-ba9adc2d6393",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BYZBWPYb5PnYKBywoaRRHr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7694,
      "cache_read_input_tokens": 39191,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7694
      },
      "output_tokens": 9,
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

_source line 22 · 2026-05-14T19:13:50.471Z_

<details><summary>↩ Tool result · `toolu_01FZKX5Qq3WhiLPxw2fqySQJ`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dcf71cae-c473-420f-a877-7d46e8b92db9",
  "uuid": "0892e611-4423-4982-8075-656a1b509fef",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex",
    "content": "\\section{Related Work}\n\\label{sec:related-work}\n\n\\paragraph{Mutation Testing and Component Analysis.}\nMutation testing originated with \\citet{demillo1978}, who proposed systematically injecting faults into programs to assess test suite adequacy.\n\\citet{jia-harman-survey} survey three decades of development, establishing leave-one-out and higher-order mutation operators as the dominant paradigm for software quality assurance, while \\citet{just-mutants-real-faults} validate that synthetic mutants approximate real faults in fault-detection experiments.\nThis body of work operates exclusively within software testing: mutants perturb \\emph{program code} to evaluate \\emph{test suites}, not solver inputs to evaluate reasoning quality.\nSTA adapts the core LOO intuition to a different domain---formal logic formalizations---where the ``program under test'' is the solver input and the ``test'' is proof success.\nThe unit of mutation shifts from code statements to logical components (premises in FOL, clauses in Prolog), and the diagnostic target shifts from test adequacy to structural necessity of each component for proof validity.\n\n\\paragraph{Reward Shaping and Process Supervision.}\nBinary outcome rewards provide no gradient on intermediate reasoning quality, motivating process-level supervision.\n\\citet{lightman-verify-step} train process reward models that score individual reasoning steps, demonstrating improved mathematical problem-solving over outcome-only rewards.\nMath-Shepherd~\\citep{math-shepherd} automates step-level annotation by validating intermediate states against reference solutions.\nRLSF~\\citep{rlsf} grounds reward in symbolic execution feedback, using solver diagnostics as a structured training signal for formal reasoning tasks.\nRubric-GRPO~\\citep{rubric-grpo} replaces scalar rewards with multi-dimensional rubric scores evaluated by an LLM judge, decomposing quality into interpretable axes.\nThese approaches share an implicit assumption: that finer-grained reward signals are reliable proxies for reasoning quality and can safely serve as optimization targets.\nOur work challenges this assumption directly.\nISR provides a solver-grounded process signal that reliably \\emph{diagnoses} structural quality when used as a post-hoc metric, yet becomes the target of gaming when incorporated into the reward---instantiating meta-level Goodhart's Law (\\S\\ref{sec:goodhart}).\nThe failure mode is not reward noise or annotation error but systematic exploitation of the metric's measurement mechanism.\n\n\\paragraph{Reward Hacking and Goodhart's Law.}\n\\citet{gao-reward-overoptimization} establish scaling laws for reward model overoptimization in RLHF, showing that proxy reward increases monotonically with optimization pressure until a critical point where true performance collapses.\n\\citet{manheim-goodhart-taxonomy} taxonomize four variants of Goodhart's Law---regressional, extremal, causal, and adversarial---providing the theoretical vocabulary for analyzing proxy-target divergence.\n\\citet{skalse-reward-hacking} formalize reward hacking as misalignment between the proxy and true reward under optimization, proving that hacking is generically unavoidable for imperfect proxies.\n\\citet{karwowski-goodhart-rl} demonstrate Goodhart dynamics geometrically in RL, showing that KL regularization delays but does not prevent overoptimization.\n\\citet{pan-reward-misspecification} map the effects of reward misspecification across environments, finding that misspecified rewards produce qualitatively different failure modes depending on the degree of misalignment.\nThis literature analyzes Goodhart dynamics theoretically or within RLHF and text generation, where the proxy is a learned reward model.\nOur setting differs in two respects.\nFirst, the proxy (ISR) is not learned but derived from a deterministic solver, eliminating reward model noise as an explanation.\nSecond, the Goodhart effect operates at a \\emph{meta} level: ISR was designed to detect gaming of execution reward, yet itself becomes gamed when optimized.\nThe dose-response pattern we observe ($\\beta{=}0.1$: proxy gaming via conclusion duplication; $\\beta{=}0.3$: performance collapse) traces the trajectory predicted by \\citet{gao-reward-overoptimization} within a single neurosymbolic RL setup.\n\n\\paragraph{Neurosymbolic Reasoning with LLMs.}\nPrompting-based pipelines couple LLMs with external solvers for logical reasoning.\nLogic-LM~\\citep{logic-lm} uses in-context examples to generate FOL formalizations verified by an external prover, with a self-refinement loop on solver errors.\nLINC~\\citep{linc} similarly translates natural language to first-order logic for Prover9 verification, demonstrating that solver-backed approaches outperform chain-of-thought on syllogistic and multi-hop tasks.\nSatLM~\\citep{satlm} extends this paradigm to satisfiability solvers via declarative prompting.\nThese systems evaluate exclusively on execution accuracy---whether the solver returns the correct answer---without diagnosing structural quality of the generated formalizations.\n\nVerification-oriented approaches add post-hoc analysis.\nLoRP~\\citep{lorp} uses Prolog execution traces to verify LLM reasoning chains, and FoVer~\\citep{fover-pei2025} employs first-order logic verification to filter training data for process reward models.\nBoth treat solver verification as a binary quality gate rather than a structural diagnostic.\n\nRL-based training represents the closest line of work.\n\\citet{mellgren-prolog-grpo} apply GRPO to train Prolog formalizers with binary solver reward, reporting substantial prove-rate gains.\nLogic-RL~\\citep{logic-rl} demonstrates that rule-based RL with solver feedback elicits emergent reasoning capabilities in LLMs.\nBoth systems optimize execution reward exclusively, reporting prove rate as the primary metric.\nSTA addresses the structural blind spot common to all these approaches: execution accuracy conflates faithful multi-step derivation with degenerate shortcuts (conclusion embedding, tautological collapse), and ISR quantifies this conflation.\nOur finding that 87\\% of proved outputs under exec-only GRPO embed the conclusion among the premises (\\S\\ref{sec:diagnostic}) applies directly to these systems, suggesting that reported prove-rate gains may overstate genuine reasoning improvement.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Bash · `toolu_0162osBBMtCCTrXDAsEf91rV`</summary>

```json
{
  "command": "wc -w /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex | awk '{print $1}'",
  "description": "Count words in related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dcf71cae-c473-420f-a877-7d46e8b92db9",
  "uuid": "8dad16e6-3ad2-4675-bb9d-367982f7b908",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sm5zC94q6W1fQvHgP2pnhT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2480,
      "cache_read_input_tokens": 46885,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2480
      },
      "output_tokens": 62,
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

_source line 24 · 2026-05-14T19:13:53.918Z_

<details><summary>↩ Tool result · `toolu_0162osBBMtCCTrXDAsEf91rV`</summary>

```text
753
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dcf71cae-c473-420f-a877-7d46e8b92db9",
  "uuid": "9660462c-2637-4cd5-ae95-bf5b3eb82631",
  "tool_use_result": {
    "stdout": "753",
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

_source line 25_

草稿已写入 `paper/related_work.tex`。

```json
{
  "section": "related_work",
  "word_count": 753,
  "citations_needed": [],
  "notes": "All 19 citations use existing bib entries. No new bib entries required. Four clusters ordered far→near: mutation testing (3 refs), reward shaping / process supervision (4 refs), Goodhart / reward hacking (5 refs), neurosymbolic reasoning (7 refs). Each cluster ends with differentiation to STA/ISR. Cross-references to §3 (diagnostic) and §4 (Goodhart) match existing section labels."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dcf71cae-c473-420f-a877-7d46e8b92db9",
  "uuid": "ab63f1e8-c3ba-4c69-8358-65b5e3c5fbf3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DBC8c4FT9cH61brFtcFQmJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 136,
      "cache_read_input_tokens": 49365,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 136
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

_source line 26_

草稿已写入 `paper/related_work.tex`。

```json
{
  "section": "related_work",
  "word_count": 753,
  "citations_needed": [],
  "notes": "All 19 citations use existing bib entries. No new bib entries required. Four clusters ordered far→near: mutation testing (3 refs), reward shaping / process supervision (4 refs), Goodhart / reward hacking (5 refs), neurosymbolic reasoning (7 refs). Each cluster ends with differentiation to STA/ISR. Cross-references to §3 (diagnostic) and §4 (Goodhart) match existing section labels."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 78339,
  "duration_api_ms": 78966,
  "num_turns": 9,
  "stop_reason": "end_turn",
  "session_id": "dcf71cae-c473-420f-a877-7d46e8b92db9",
  "total_cost_usd": 0.422786,
  "usage": {
    "input_tokens": 7,
    "cache_creation_input_tokens": 37660,
    "cache_read_input_tokens": 210850,
    "output_tokens": 3172,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 37660,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 166,
        "cache_read_input_tokens": 49365,
        "cache_creation_input_tokens": 136,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 136
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2581,
      "outputTokens": 14,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002651,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 7,
      "outputTokens": 3172,
      "cacheReadInputTokens": 210850,
      "cacheCreationInputTokens": 37660,
      "webSearchRequests": 0,
      "costUSD": 0.420135,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "8ad5b007-fa1b-42b1-b243-33b48a69d91a"
}
```

</details>

---
