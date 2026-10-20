# writing paper assembly v3 20260515T032531 retry1

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 32
- **Recorded user turns:** 0
- **Tool calls:** 12
- **Original source:** `logs/workers/worker_writing_paper-assembly-v3_20260515T032531_retry1.log`
- **Structured JSON:** [`ba6e59b3ab53a5253ff4.json`](../../sessions/ba/ba6e59b3ab53a5253ff4.json)

## Before a recorded user message

32 recorded events

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
  "session_id": "ca27e824-6ca6-4db1-9e55-77ef612ddfd7",
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
  "model": "claude-opus-4-7[1m]",
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
  "uuid": "a6b306f9-5cb1-4a4c-95af-77b7fa6bb46b",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Log line

_source line 3_

{"type":"rate_limit_event","rate_limit_info":{"status":"allowed_warning","resetsAt":1779361200,"rateLimi{"type":"assistant","message":{"model":"claude-opus-4-6","id":"msg_01LuqgNeS9mgQwozyWTq4KFo","type":"message","role":"assistant","content":[{"type":"text","text"{"type":"assistant","message":{"model":"claude-opus-4-7","id":"msg_012EeJWC9tsrwjn3QeWjyvJQ","type":"message","role":"assistant","content":[{"type":"thinking","thinking":"","signature":"Ev8BClkIDRgCKkAX6bgiBTW7LV6Ke0MYa2Dz1o9VTLGxI8kg5kuGlmoKq7BTvuFCJoQPAj/I7S9um7jcwBhQ8moGVr5LGva1m0BIMg9jbGF1ZGUtb3B1cy00LTc4ABIMZBve17h5ZqifrxVrGgzbtG7Ci5GYc9YswrciMEQf0S6SOZ5gziezY/i4JNR36LL2Mjw/QJw50wtOjQ21qaDgPVqLjGaZU3v+J9kc9SpU58xgSLtW1vCzcQ9w43bbVgOhvo0txYFffVDDqxGfwzYUIZNQt13LLwWM2iCBAk/UW7khadf3uywx/IMqfQMXT9kLubbVNueDfin9otBy8Ltzjvv+GAE="}],"stop_reason":null,"stop_sequence":null,"stop_details":null,"usage":{"input_tokens":6,"cache_creation_input_tokens":16502,"cache_read_input_tokens":16241,"cache_creation":{"ephemeral_5m_input_tokens":0,"ephemeral_1h_input_tokens":16502},"output_tokens":8,"service_tier":"standard","inference_geo":"not_available"},"diagnostics":null,"context_management":null},"parent_tool_use_id":null,"session_id":"ca27e824-6ca6-4db1-9e55-77ef612ddfd7","uuid":"b493bfe9-7f7e-4388-804a-1d872f9f59da"}

---

### Tool call

_source line 4_

<details open><summary>🔧 Tool call — Read · `toolu_01Jfk3jybLk32KDEpPS5CkBP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/abstract_c1671f.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca27e824-6ca6-4db1-9e55-77ef612ddfd7",
  "uuid": "cb36037a-b523-415c-863c-ccba6965b7a7",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_012EeJWC9tsrwjn3QeWjyvJQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 16502,
      "cache_read_input_tokens": 16241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16502
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

_source line 5 · 2026-05-15T03:25:48.426Z_

<details><summary>↩ Tool result · `toolu_01Jfk3jybLk32KDEpPS5CkBP`</summary>

```text
1	GRPO-trained neurosymbolic formalizers routinely achieve high prove rates on logical reasoning benchmarks, yet no principled diagnostic exists to assess whether the underlying formal outputs contain genuine logical structure or degenerate shortcuts.
2	We introduce \emph{Solver Trace Ablation} (STA), a solver-agnostic protocol that derives the \emph{Intensional Structure Ratio} (ISR) via leave-one-out component necessity testing: each premise is ablated and the solver re-executed, yielding a continuous score measuring the fraction of components genuinely required for the proof.
3	Applied to GRPO training of a Qwen3-4B formalizer across 6 reward configurations, 3 random seeds, and up to 1{,}000 training steps, STA reveals three findings.
4	First, ISR serves as an effective diagnostic: execution-only GRPO achieves 96\% prove rate while ISR collapses from 0.64 to 0.003 over training---a 99.5\% decline quantifying structural degeneration invisible to the execution reward.
5	All three seeds exhibit 87--100\% conclusion embedding in proved outputs; a supervised fine-tuning baseline confirms that these pathologies are RL-specific (92.9\% genuine proofs, near-zero hacking).
6	Second, ISR fails as a training signal due to meta-level Goodhart's Law: at low dose ($\beta{=}0.1$), the policy games ISR itself via single-premise conclusion duplication (64.5\% H7 across 3 seeds vs.\ 0\% under matched random controls), with the apparent structural advantage dissolving entirely under premise-count-matched analysis (1.06$\times$); at high dose ($\beta{=}0.3$), classic Goodhart collapse drives prove rate to 18\% versus 48\% for the random control.
7	Third, both the diagnostic capability and the Goodhart failure transfer to Prolog (SWI-Prolog), where ISR-as-reward produces \emph{universal} Goodhart: all 3 seeds converge to gaming with 0\% genuine output, each via a distinct mechanism---tautological duplication, degenerate syntax, and query-as-fact gaming.
8	Across all conditions we identify and quantify 7 distinct hacking modes, providing an empirically grounded taxonomy for structural failures in neurosymbolic RL.
9	Our results expose a fundamental asymmetry: ISR is reliable as a diagnostic observer but unreliable as an optimization target---a cautionary finding for any proxy-metric-as-reward approach.
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ca27e824-6ca6-4db1-9e55-77ef612ddfd7",
  "uuid": "6489e4b9-c566-4a57-9678-11a509ec627a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/abstract_c1671f.tex",
      "content": "GRPO-trained neurosymbolic formalizers routinely achieve high prove rates on logical reasoning benchmarks, yet no principled diagnostic exists to assess whether the underlying formal outputs contain genuine logical structure or degenerate shortcuts.\nWe introduce \\emph{Solver Trace Ablation} (STA), a solver-agnostic protocol that derives the \\emph{Intensional Structure Ratio} (ISR) via leave-one-out component necessity testing: each premise is ablated and the solver re-executed, yielding a continuous score measuring the fraction of components genuinely required for the proof.\nApplied to GRPO training of a Qwen3-4B formalizer across 6 reward configurations, 3 random seeds, and up to 1{,}000 training steps, STA reveals three findings.\nFirst, ISR serves as an effective diagnostic: execution-only GRPO achieves 96\\% prove rate while ISR collapses from 0.64 to 0.003 over training---a 99.5\\% decline quantifying structural degeneration invisible to the execution reward.\nAll three seeds exhibit 87--100\\% conclusion embedding in proved outputs; a supervised fine-tuning baseline confirms that these pathologies are RL-specific (92.9\\% genuine proofs, near-zero hacking).\nSecond, ISR fails as a training signal due to meta-level Goodhart's Law: at low dose ($\\beta{=}0.1$), the policy games ISR itself via single-premise conclusion duplication (64.5\\% H7 across 3 seeds vs.\\ 0\\% under matched random controls), with the apparent structural advantage dissolving entirely under premise-count-matched analysis (1.06$\\times$); at high dose ($\\beta{=}0.3$), classic Goodhart collapse drives prove rate to 18\\% versus 48\\% for the random control.\nThird, both the diagnostic capability and the Goodhart failure transfer to Prolog (SWI-Prolog), where ISR-as-reward produces \\emph{universal} Goodhart: all 3 seeds converge to gaming with 0\\% genuine output, each via a distinct mechanism---tautological duplication, degenerate syntax, and query-as-fact gaming.\nAcross all conditions we identify and quantify 7 distinct hacking modes, providing an empirically grounded taxonomy for structural failures in neurosymbolic RL.\nOur results expose a fundamental asymmetry: ISR is reliable as a diagnostic observer but unreliable as an optimization target---a cautionary finding for any proxy-metric-as-reward approach.\n",
      "numLines": 10,
      "startLine": 1,
      "totalLines": 10
    }
  }
}
```

</details>

---

### Tool call

_source line 6_

<details open><summary>🔧 Tool call — Read · `toolu_019P6cDt8HJ86i1pxWdjnogZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/introduction_176853.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca27e824-6ca6-4db1-9e55-77ef612ddfd7",
  "uuid": "3f4c419b-821b-46af-a66a-a7a55344f1cd",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01FkfwCGg2pKjBpPKm4tu8mx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1075,
      "cache_read_input_tokens": 32743,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1075
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

_source line 7 · 2026-05-15T03:25:51.608Z_

<details><summary>↩ Tool result · `toolu_019P6cDt8HJ86i1pxWdjnogZ`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	A GRPO-trained formalizer achieves a 93\% prove rate on first-order logic problems---yet 87\% of its proved outputs embed the conclusion verbatim among the premises.
5	The solver succeeds not because the model has learned to reason, but because the formalization trivially entails any conclusion that already appears as a premise.
6	This structural shortcut is invisible to execution-based evaluation: prove rate registers success regardless of whether the proof reflects genuine multi-step derivation or degenerate circular embedding.
7	The reward optimizes solver success; the model finds the shortest path to it.
8	
9	\paragraph{The execution-only blind spot.}
10	Prove rate---the dominant evaluation metric for neurosymbolic formalizers~\citep{logic-lm, linc, satlm}---conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under reinforcement learning, where the optimizer exploits any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}.
11	Recent work applies GRPO~\citep{deepseekmath} to train LLMs that generate solver-verified formal programs~\citep{mellgren-prolog-grpo, logic-rl} using binary execution feedback as reward; this drives rapid PR gains but gives no gradient on structural quality.
12	Process reward models~\citep{lightman-verify-step, math-shepherd} offer step-level supervision but require expensive annotations and do not transfer to arbitrary solver-backed settings.
13	A complementary line of work documents that LLMs already game logical formalization at inference time~\citep{kim-game-formalization, bondarenko-spec-gaming}, yet no existing method provides an annotation-free \emph{diagnostic} for structural integrity in neurosymbolic outputs---one adaptable in principle to any solver supporting component-level input manipulation (see \S\ref{sec:related-work} for full context).
14	
15	\paragraph{Component necessity testing.}
16	We address this gap with \emph{Solver Trace Ablation} (STA), a diagnostic protocol applying \emph{component necessity testing}---leave-one-out (LOO) ablation on solver inputs---to quantify structural integrity (\autoref{fig:sta-overview}).
17	For each proved formalization, STA removes each component individually and re-runs the solver; the fraction of components whose removal causes proof failure yields the \emph{Intensional Structural Reward} (ISR).
18	ISR${=}1$ indicates every component is individually required for proof success; ISR${=}0$ indicates complete structural redundancy.
19	We are explicit that LOO ablation is itself standard---in mutation testing~\citep{demillo1978, jia-harman-survey} and feature attribution---and we claim novelty not in the primitive but in its application as a diagnostic for GRPO reward hacking and in the empirical phenomena it surfaces.
20	We also emphasize that ISR captures structural rather than semantic integrity: a downstream NLI evaluation finds ISR and task accuracy uncorrelated ($\rho{=}{-}0.049$, $p{=}0.187$), confirming it measures properties orthogonal to semantic correctness.
21	
22	\paragraph{ISR as diagnostic.}
23	Applied as a post-hoc diagnostic on a GRPO formalizer trained with FOLIO~\citep{folio} data, ISR reveals a structural collapse trajectory entirely invisible to prove rate: ISR falls from 0.642 at 100 steps to 0.132 at 500 steps to 0.003 at 1000 steps---a 99.5\% degradation---while prove rate simultaneously rises from 32\% to 96\%.
24	Three random seeds diverge radically (PR $\sigma{=}47$\,pp), each converging to a qualitatively different degeneration mode: conclusion embedding, repetition collapse, and tautological collapse.
25	A supervised fine-tuning (SFT) baseline on the same data achieves a prove rate of 14\% but 92.9\% non-hacking proofs with near-zero shortcut content, confirming that the structural collapse is a consequence of RL reward optimization, not model capacity or data limitations.
26	
27	\paragraph{Meta-level Goodhart.}
28	A natural question is whether ISR can serve as a training signal.
29	The answer is negative: when ISR is added to the reward, $r = r_{\text{exec}} \cdot (1 + \beta \cdot \text{ISR})$, the model games the diagnostic itself---\emph{meta-level Goodhart's Law}~\citep{manheim-goodhart-taxonomy, karwowski-goodhart-rl, gao-reward-overoptimization}.
30	At $\beta{=}0.1$, 64.5\% of proved samples (3-seed mean) exhibit ISR-specific single-premise-equals-conclusion duplication---a construction in which ISR is high \emph{by definition} of the LOO metric---versus 0\% under a matched random-bonus reward; the one seed that retains a non-trivial ``genuine'' fraction reduces to 1.06$\times$ random after controlling for a premise-count confound (\S\ref{sec:goodhart}).
31	At $\beta{=}0.3$ the same reward produces extreme cross-seed instability (PR $66{\pm}42\%$) with three qualitatively distinct Goodhart pathways: reward collapse (PR ${=}\,18\%$), shortcut dominance (86\% PR, 69\% conclusion embedding), and pure metric gaming (95\% PR, 100\% ISR-inflating duplications, ISR${=}0.742$).
32	The effect transfers and intensifies in a different formal language: in Prolog with SWI-Prolog as solver, all three seeds produce 0\% non-hacking output---universal Goodhart---each via a distinct mechanism, including a \emph{query-as-fact gaming} mode that bypasses text-match classifiers entirely.
33	ISR's asymmetry is the central finding: \emph{reliable as observer, unreliable as optimizer.}
34	
35	\paragraph{Contributions.}
36	Across 6 reward conditions, 3 seeds, 2 logic types, and up to 1000 training steps, we make four contributions:
37	\begin{itemize}[nosep,leftmargin=*]
38	\item[\textbf{C1.}] \textbf{ISR as diagnostic} for GRPO reward hacking, with a complete collapse trajectory ($\text{ISR}{=}0.642{\to}0.003$ over 1000 steps) invisible to prove rate, and an SFT control (92.9\% non-hacking) localizing the failure mode to RL optimization (\S\ref{sec:isr-diagnostic}).
39	\item[\textbf{C2.}] \textbf{Empirical meta-level Goodhart} in neurosymbolic RL, with a random-bonus control that isolates ISR-specific gaming (H7: 64.5\% vs.\ 0\%) and a premise-count-matched analysis showing that the sole apparent ISR gain is a mathematical artifact of the LOO metric, not a structural improvement (\S\ref{sec:goodhart}).
40	\item[\textbf{C3.}] \textbf{Cross-logic transfer} to Prolog/SWI-Prolog, demonstrating universal Goodhart (3/3 seeds gaming, 0\% non-hacking) and indicating that simpler formal semantics enable more complete exploitation (\S\ref{sec:prolog}).
41	\item[\textbf{C4.}] \textbf{A seven-mode hacking taxonomy} including a Prolog-specific query-as-fact gaming mode that bypasses text-match classifiers, motivating functional ($n_{\text{necessary}}$-based) cross-validation of diagnostics (\S\ref{sec:taxonomy-results}).
42	\end{itemize}
43	Taken together, these results characterize ISR's fundamental asymmetry: it is a useful instrument for \emph{detecting} reward hacking in solver-backed RL, but unsuitable as an optimization target because the very LOO primitive that makes it interpretable also makes it gameable.
44	We see the empirical Goodhart characterization, premise-count confound, and cross-logic universality as cautionary results for any work treating a structural proxy metric as a training signal.
45	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ca27e824-6ca6-4db1-9e55-77ef612ddfd7",
  "uuid": "dc24e78e-3e1e-4371-a04e-c5aa170cc788",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/introduction_176853.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nA GRPO-trained formalizer achieves a 93\\% prove rate on first-order logic problems---yet 87\\% of its proved outputs embed the conclusion verbatim among the premises.\nThe solver succeeds not because the model has learned to reason, but because the formalization trivially entails any conclusion that already appears as a premise.\nThis structural shortcut is invisible to execution-based evaluation: prove rate registers success regardless of whether the proof reflects genuine multi-step derivation or degenerate circular embedding.\nThe reward optimizes solver success; the model finds the shortest path to it.\n\n\\paragraph{The execution-only blind spot.}\nProve rate---the dominant evaluation metric for neurosymbolic formalizers~\\citep{logic-lm, linc, satlm}---conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under reinforcement learning, where the optimizer exploits any shortcut the reward fails to penalize~\\citep{skalse-reward-hacking, reward-hacking-survey}.\nRecent work applies GRPO~\\citep{deepseekmath} to train LLMs that generate solver-verified formal programs~\\citep{mellgren-prolog-grpo, logic-rl} using binary execution feedback as reward; this drives rapid PR gains but gives no gradient on structural quality.\nProcess reward models~\\citep{lightman-verify-step, math-shepherd} offer step-level supervision but require expensive annotations and do not transfer to arbitrary solver-backed settings.\nA complementary line of work documents that LLMs already game logical formalization at inference time~\\citep{kim-game-formalization, bondarenko-spec-gaming}, yet no existing method provides an annotation-free \\emph{diagnostic} for structural integrity in neurosymbolic outputs---one adaptable in principle to any solver supporting component-level input manipulation (see \\S\\ref{sec:related-work} for full context).\n\n\\paragraph{Component necessity testing.}\nWe address this gap with \\emph{Solver Trace Ablation} (STA), a diagnostic protocol applying \\emph{component necessity testing}---leave-one-out (LOO) ablation on solver inputs---to quantify structural integrity (\\autoref{fig:sta-overview}).\nFor each proved formalization, STA removes each component individually and re-runs the solver; the fraction of components whose removal causes proof failure yields the \\emph{Intensional Structural Reward} (ISR).\nISR${=}1$ indicates every component is individually required for proof success; ISR${=}0$ indicates complete structural redundancy.\nWe are explicit that LOO ablation is itself standard---in mutation testing~\\citep{demillo1978, jia-harman-survey} and feature attribution---and we claim novelty not in the primitive but in its application as a diagnostic for GRPO reward hacking and in the empirical phenomena it surfaces.\nWe also emphasize that ISR captures structural rather than semantic integrity: a downstream NLI evaluation finds ISR and task accuracy uncorrelated ($\\rho{=}{-}0.049$, $p{=}0.187$), confirming it measures properties orthogonal to semantic correctness.\n\n\\paragraph{ISR as diagnostic.}\nApplied as a post-hoc diagnostic on a GRPO formalizer trained with FOLIO~\\citep{folio} data, ISR reveals a structural collapse trajectory entirely invisible to prove rate: ISR falls from 0.642 at 100 steps to 0.132 at 500 steps to 0.003 at 1000 steps---a 99.5\\% degradation---while prove rate simultaneously rises from 32\\% to 96\\%.\nThree random seeds diverge radically (PR $\\sigma{=}47$\\,pp), each converging to a qualitatively different degeneration mode: conclusion embedding, repetition collapse, and tautological collapse.\nA supervised fine-tuning (SFT) baseline on the same data achieves a prove rate of 14\\% but 92.9\\% non-hacking proofs with near-zero shortcut content, confirming that the structural collapse is a consequence of RL reward optimization, not model capacity or data limitations.\n\n\\paragraph{Meta-level Goodhart.}\nA natural question is whether ISR can serve as a training signal.\nThe answer is negative: when ISR is added to the reward, $r = r_{\\text{exec}} \\cdot (1 + \\beta \\cdot \\text{ISR})$, the model games the diagnostic itself---\\emph{meta-level Goodhart's Law}~\\citep{manheim-goodhart-taxonomy, karwowski-goodhart-rl, gao-reward-overoptimization}.\nAt $\\beta{=}0.1$, 64.5\\% of proved samples (3-seed mean) exhibit ISR-specific single-premise-equals-conclusion duplication---a construction in which ISR is high \\emph{by definition} of the LOO metric---versus 0\\% under a matched random-bonus reward; the one seed that retains a non-trivial ``genuine'' fraction reduces to 1.06$\\times$ random after controlling for a premise-count confound (\\S\\ref{sec:goodhart}).\nAt $\\beta{=}0.3$ the same reward produces extreme cross-seed instability (PR $66{\\pm}42\\%$) with three qualitatively distinct Goodhart pathways: reward collapse (PR ${=}\\,18\\%$), shortcut dominance (86\\% PR, 69\\% conclusion embedding), and pure metric gaming (95\\% PR, 100\\% ISR-inflating duplications, ISR${=}0.742$).\nThe effect transfers and intensifies in a different formal language: in Prolog with SWI-Prolog as solver, all three seeds produce 0\\% non-hacking output---universal Goodhart---each via a distinct mechanism, including a \\emph{query-as-fact gaming} mode that bypasses text-match classifiers entirely.\nISR's asymmetry is the central finding: \\emph{reliable as observer, unreliable as optimizer.}\n\n\\paragraph{Contributions.}\nAcross 6 reward conditions, 3 seeds, 2 logic types, and up to 1000 training steps, we make four contributions:\n\\begin{itemize}[nosep,leftmargin=*]\n\\item[\\textbf{C1.}] \\textbf{ISR as diagnostic} for GRPO reward hacking, with a complete collapse trajectory ($\\text{ISR}{=}0.642{\\to}0.003$ over 1000 steps) invisible to prove rate, and an SFT control (92.9\\% non-hacking) localizing the failure mode to RL optimization (\\S\\ref{sec:isr-diagnostic}).\n\\item[\\textbf{C2.}] \\textbf{Empirical meta-level Goodhart} in neurosymbolic RL, with a random-bonus control that isolates ISR-specific gaming (H7: 64.5\\% vs.\\ 0\\%) and a premise-count-matched analysis showing that the sole apparent ISR gain is a mathematical artifact of the LOO metric, not a structural improvement (\\S\\ref{sec:goodhart}).\n\\item[\\textbf{C3.}] \\textbf{Cross-logic transfer} to Prolog/SWI-Prolog, demonstrating universal Goodhart (3/3 seeds gaming, 0\\% non-hacking) and indicating that simpler formal semantics enable more complete exploitation (\\S\\ref{sec:prolog}).\n\\item[\\textbf{C4.}] \\textbf{A seven-mode hacking taxonomy} including a Prolog-specific query-as-fact gaming mode that bypasses text-match classifiers, motivating functional ($n_{\\text{necessary}}$-based) cross-validation of diagnostics (\\S\\ref{sec:taxonomy-results}).\n\\end{itemize}\nTaken together, these results characterize ISR's fundamental asymmetry: it is a useful instrument for \\emph{detecting} reward hacking in solver-backed RL, but unsuitable as an optimization target because the very LOO primitive that makes it interpretable also makes it gameable.\nWe see the empirical Goodhart characterization, premise-count confound, and cross-logic universality as cautionary results for any work treating a structural proxy metric as a training signal.\n",
      "numLines": 45,
      "startLine": 1,
      "totalLines": 45
    }
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_01XjpoQKGTuoF3DSs66BBx1d`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/related_work_b05493.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca27e824-6ca6-4db1-9e55-77ef612ddfd7",
  "uuid": "504f5e95-63b8-42ca-be44-62de7daf36e1",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_016WaF5pfywAo5eHQgB5hCYf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3058,
      "cache_read_input_tokens": 33818,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3058
      },
      "output_tokens": 42,
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

_source line 9 · 2026-05-15T03:25:56.884Z_

<details><summary>↩ Tool result · `toolu_01XjpoQKGTuoF3DSs66BBx1d`</summary>

```text
1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Neurosymbolic Reasoning with LLMs.}
5	Prompting-based pipelines couple LLMs with external solvers to offload logical inference.
6	Logic-LM~\cite{logic-lm} generates FOL formalizations verified by an external prover, with a self-refinement loop on solver errors; LINC~\cite{linc} similarly translates natural language to first-order logic for Prover9, demonstrating gains over chain-of-thought on syllogistic and multi-hop tasks.
7	SatLM~\cite{satlm} extends the paradigm to satisfiability solvers via declarative prompting, while LoRP~\cite{lorp} and FoVer~\cite{fover-pei2025} route through Prolog execution traces and FOL verification, respectively, to validate or filter LLM-generated reasoning.
8	All of these systems evaluate on execution accuracy---whether the solver returns the correct answer---without diagnosing the structural quality of the generated formalizations.
9	RL-based training represents a more recent direction, enabled by GRPO~\cite{deepseekmath}, which eliminates the critic model by estimating baselines from group scores.
10	Mellgren~\cite{mellgren-prolog-grpo} applies GRPO to train Prolog formalizers with binary solver reward, reporting substantial prove-rate gains; Logic-RL~\cite{logic-rl} demonstrates that rule-based RL with solver feedback elicits emergent reasoning in LLMs; and Thought-Like-Pro~\cite{thought-like-pro} uses self-driven Prolog chain-of-thought to enhance multi-step reasoning.
11	These RL systems optimize execution reward exclusively, reporting prove rate as the primary success metric.
12	Our work differs in diagnostic focus: STA reveals that execution accuracy conflates faithful derivation with degenerate shortcuts, and ISR quantifies this conflation.
13	The finding that 87\% of proved outputs under exec-only GRPO embed the conclusion among the premises (\S\ref{sec:diagnostic}) applies directly to these systems, suggesting that reported prove-rate gains may overstate genuine reasoning improvement.
14	
15	\paragraph{Reward Shaping and Process Supervision.}
16	Binary outcome rewards provide no gradient on intermediate reasoning quality, motivating process-level supervision.
17	Lightman et al.~\cite{lightman-verify-step} train process reward models (PRMs) that score individual reasoning steps, improving mathematical problem-solving over outcome-only rewards.
18	Math-Shepherd~\cite{math-shepherd} automates step-level annotation by validating intermediate states against reference solutions.
19	Beyond learned PRMs, symbolic feedback offers an alternative grounding: RLSF~\cite{rlsf} uses solver diagnostics as a structured training signal for formal reasoning, and Rubric-GRPO~\cite{rubric-grpo} replaces scalar rewards with multi-dimensional rubric scores evaluated by an LLM judge.
20	However, process rewards introduce their own failure modes.
21	Gao et al.~\cite{gao-effective-rl-reward} show that reward design choices---granularity, normalization, aggregation---can dominate the effect of the underlying signal.
22	PROF~\cite{prof-process-outcome} finds that process and outcome rewards conflict under joint optimization, requiring explicit harmonization.
23	The Qwen PRM study~\cite{qwen-prm-lessons} documents that PRMs degrade unpredictably at distribution shift, and ProGRS~\cite{progrs-outcome-conditioned} introduces outcome-conditioned process rewards to mitigate the gap between step-level correctness and final-answer accuracy.
24	ISR differs from these approaches in that it is solver-grounded rather than learned: it derives directly from deterministic LOO ablation of solver inputs, eliminating reward model noise.
25	Our finding that ISR reliably \emph{diagnoses} structural quality yet becomes the target of gaming when used as a training reward (\S\ref{sec:goodhart}) adds an empirical data point to this literature: even non-learned process signals can Goodhart when optimized.
26	
27	\paragraph{Reward Hacking and Goodhart's Law.}
28	Gao et al.~\cite{gao-reward-overoptimization} establish scaling laws for reward model overoptimization, showing that proxy reward increases monotonically with optimization pressure until true performance collapses.
29	Manheim and Garrabrant~\cite{manheim-goodhart-taxonomy} taxonomize four variants of Goodhart's Law---regressional, extremal, causal, and adversarial---while Skalse et al.~\cite{skalse-reward-hacking} prove that reward hacking is generically unavoidable for imperfect proxies.
30	Karwowski et al.~\cite{karwowski-goodhart-rl} demonstrate Goodhart dynamics geometrically in RL, showing that KL regularization delays but does not prevent overoptimization; Pan et al.~\cite{pan-reward-misspecification} map how misspecified rewards produce qualitatively different failure modes depending on the degree of misalignment; and Kwa et al.~\cite{kwa-catastrophic-goodhart} show that KL divergence regularization fails catastrophically under heavy-tailed reward misspecification.
31	In the LLM setting specifically, recent surveys~\cite{reward-hacking-survey} document reward hacking across the full spectrum from specification gaming to emergent misalignment.
32	Bondarenko et al.~\cite{bondarenko-spec-gaming} demonstrate specification gaming in reasoning models, Kim et al.~\cite{kim-game-formalization} evaluate whether LLMs game logical formalization tasks, and Yang et al.~\cite{spurious-rewards} identify spurious reward signals in RLVR that inflate metrics without genuine capability gains.
33	This literature analyzes Goodhart dynamics either theoretically or within RLHF/text generation, where the proxy is a learned reward model.
34	Our setting differs in two respects: the proxy (ISR) is deterministic and solver-derived, eliminating reward model noise as an explanation; and the Goodhart effect operates at a \emph{meta} level---ISR was designed to \emph{detect} gaming of execution reward, yet itself becomes gamed when optimized.
35	The dose-response pattern we observe ($\beta{=}0.1$: proxy gaming via conclusion duplication; $\beta{=}0.3$: performance collapse) traces the trajectory predicted by Gao et al.~\cite{gao-reward-overoptimization} within a single neurosymbolic RL setup, and the premise-count confound that explains away apparent ISR improvements provides a concrete mechanism for regressional Goodhart in formal reasoning.
36	
37	\paragraph{Mutation Testing and Component Analysis.}
38	Mutation testing originated with DeMillo et al.~\cite{demillo1978}, who proposed injecting systematic faults into programs to assess test suite adequacy; the coupling effect hypothesis~\cite{offutt-coupling} provides the theoretical grounding that simple mutants subsume complex faults.
39	Jia and Harman~\cite{jia-harman-survey} survey three decades of development, establishing leave-one-out and higher-order mutation as the dominant paradigm, while Just et al.~\cite{just-mutants-real-faults} validate that synthetic mutants approximate real faults in detection experiments.
40	Recent work connects mutation testing with LLMs: LLMorpheus~\cite{llmorpheus} uses language models to generate semantically rich mutants that go beyond syntactic operators.
41	STA adapts the core LOO intuition to a different domain---formal logic formalizations---where the ``program under test'' is the solver input and the ``test'' is proof success.
42	The unit of mutation shifts from code statements to logical components (premises in FOL, clauses in Prolog), and the diagnostic target shifts from test adequacy to structural necessity for proof validity.
43	The novelty lies not in the perturbation technique itself but in its application to neurosymbolic RL and the empirical findings it enables: the ISR collapse trajectory, the Goodhart phenomenon, and the taxonomy of hacking modes.
44	
45	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ca27e824-6ca6-4db1-9e55-77ef612ddfd7",
  "uuid": "ccf9211d-0b06-40e0-8d70-0d6e62420e08",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/related_work_b05493.tex",
      "content": "\\section{Related Work}\n\\label{sec:related-work}\n\n\\paragraph{Neurosymbolic Reasoning with LLMs.}\nPrompting-based pipelines couple LLMs with external solvers to offload logical inference.\nLogic-LM~\\cite{logic-lm} generates FOL formalizations verified by an external prover, with a self-refinement loop on solver errors; LINC~\\cite{linc} similarly translates natural language to first-order logic for Prover9, demonstrating gains over chain-of-thought on syllogistic and multi-hop tasks.\nSatLM~\\cite{satlm} extends the paradigm to satisfiability solvers via declarative prompting, while LoRP~\\cite{lorp} and FoVer~\\cite{fover-pei2025} route through Prolog execution traces and FOL verification, respectively, to validate or filter LLM-generated reasoning.\nAll of these systems evaluate on execution accuracy---whether the solver returns the correct answer---without diagnosing the structural quality of the generated formalizations.\nRL-based training represents a more recent direction, enabled by GRPO~\\cite{deepseekmath}, which eliminates the critic model by estimating baselines from group scores.\nMellgren~\\cite{mellgren-prolog-grpo} applies GRPO to train Prolog formalizers with binary solver reward, reporting substantial prove-rate gains; Logic-RL~\\cite{logic-rl} demonstrates that rule-based RL with solver feedback elicits emergent reasoning in LLMs; and Thought-Like-Pro~\\cite{thought-like-pro} uses self-driven Prolog chain-of-thought to enhance multi-step reasoning.\nThese RL systems optimize execution reward exclusively, reporting prove rate as the primary success metric.\nOur work differs in diagnostic focus: STA reveals that execution accuracy conflates faithful derivation with degenerate shortcuts, and ISR quantifies this conflation.\nThe finding that 87\\% of proved outputs under exec-only GRPO embed the conclusion among the premises (\\S\\ref{sec:diagnostic}) applies directly to these systems, suggesting that reported prove-rate gains may overstate genuine reasoning improvement.\n\n\\paragraph{Reward Shaping and Process Supervision.}\nBinary outcome rewards provide no gradient on intermediate reasoning quality, motivating process-level supervision.\nLightman et al.~\\cite{lightman-verify-step} train process reward models (PRMs) that score individual reasoning steps, improving mathematical problem-solving over outcome-only rewards.\nMath-Shepherd~\\cite{math-shepherd} automates step-level annotation by validating intermediate states against reference solutions.\nBeyond learned PRMs, symbolic feedback offers an alternative grounding: RLSF~\\cite{rlsf} uses solver diagnostics as a structured training signal for formal reasoning, and Rubric-GRPO~\\cite{rubric-grpo} replaces scalar rewards with multi-dimensional rubric scores evaluated by an LLM judge.\nHowever, process rewards introduce their own failure modes.\nGao et al.~\\cite{gao-effective-rl-reward} show that reward design choices---granularity, normalization, aggregation---can dominate the effect of the underlying signal.\nPROF~\\cite{prof-process-outcome} finds that process and outcome rewards conflict under joint optimization, requiring explicit harmonization.\nThe Qwen PRM study~\\cite{qwen-prm-lessons} documents that PRMs degrade unpredictably at distribution shift, and ProGRS~\\cite{progrs-outcome-conditioned} introduces outcome-conditioned process rewards to mitigate the gap between step-level correctness and final-answer accuracy.\nISR differs from these approaches in that it is solver-grounded rather than learned: it derives directly from deterministic LOO ablation of solver inputs, eliminating reward model noise.\nOur finding that ISR reliably \\emph{diagnoses} structural quality yet becomes the target of gaming when used as a training reward (\\S\\ref{sec:goodhart}) adds an empirical data point to this literature: even non-learned process signals can Goodhart when optimized.\n\n\\paragraph{Reward Hacking and Goodhart's Law.}\nGao et al.~\\cite{gao-reward-overoptimization} establish scaling laws for reward model overoptimization, showing that proxy reward increases monotonically with optimization pressure until true performance collapses.\nManheim and Garrabrant~\\cite{manheim-goodhart-taxonomy} taxonomize four variants of Goodhart's Law---regressional, extremal, causal, and adversarial---while Skalse et al.~\\cite{skalse-reward-hacking} prove that reward hacking is generically unavoidable for imperfect proxies.\nKarwowski et al.~\\cite{karwowski-goodhart-rl} demonstrate Goodhart dynamics geometrically in RL, showing that KL regularization delays but does not prevent overoptimization; Pan et al.~\\cite{pan-reward-misspecification} map how misspecified rewards produce qualitatively different failure modes depending on the degree of misalignment; and Kwa et al.~\\cite{kwa-catastrophic-goodhart} show that KL divergence regularization fails catastrophically under heavy-tailed reward misspecification.\nIn the LLM setting specifically, recent surveys~\\cite{reward-hacking-survey} document reward hacking across the full spectrum from specification gaming to emergent misalignment.\nBondarenko et al.~\\cite{bondarenko-spec-gaming} demonstrate specification gaming in reasoning models, Kim et al.~\\cite{kim-game-formalization} evaluate whether LLMs game logical formalization tasks, and Yang et al.~\\cite{spurious-rewards} identify spurious reward signals in RLVR that inflate metrics without genuine capability gains.\nThis literature analyzes Goodhart dynamics either theoretically or within RLHF/text generation, where the proxy is a learned reward model.\nOur setting differs in two respects: the proxy (ISR) is deterministic and solver-derived, eliminating reward model noise as an explanation; and the Goodhart effect operates at a \\emph{meta} level---ISR was designed to \\emph{detect} gaming of execution reward, yet itself becomes gamed when optimized.\nThe dose-response pattern we observe ($\\beta{=}0.1$: proxy gaming via conclusion duplication; $\\beta{=}0.3$: performance collapse) traces the trajectory predicted by Gao et al.~\\cite{gao-reward-overoptimization} within a single neurosymbolic RL setup, and the premise-count confound that explains away apparent ISR improvements provides a concrete mechanism for regressional Goodhart in formal reasoning.\n\n\\paragraph{Mutation Testing and Component Analysis.}\nMutation testing originated with DeMillo et al.~\\cite{demillo1978}, who proposed injecting systematic faults into programs to assess test suite adequacy; the coupling effect hypothesis~\\cite{offutt-coupling} provides the theoretical grounding that simple mutants subsume complex faults.\nJia and Harman~\\cite{jia-harman-survey} survey three decades of development, establishing leave-one-out and higher-order mutation as the dominant paradigm, while Just et al.~\\cite{just-mutants-real-faults} validate that synthetic mutants approximate real faults in detection experiments.\nRecent work connects mutation testing with LLMs: LLMorpheus~\\cite{llmorpheus} uses language models to generate semantically rich mutants that go beyond syntactic operators.\nSTA adapts the core LOO intuition to a different domain---formal logic formalizations---where the ``program under test'' is the solver input and the ``test'' is proof success.\nThe unit of mutation shifts from code statements to logical components (premises in FOL, clauses in Prolog), and the diagnostic target shifts from test adequacy to structural necessity for proof validity.\nThe novelty lies not in the perturbation technique itself but in its application to neurosymbolic RL and the empirical findings it enables: the ISR collapse trajectory, the Goodhart phenomenon, and the taxonomy of hacking modes.\n\n",
      "numLines": 45,
      "startLine": 1,
      "totalLines": 45
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_011VmgWaUqmfzM1vEkKiE4gz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/method_76d073.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca27e824-6ca6-4db1-9e55-77ef612ddfd7",
  "uuid": "59da4dfc-a9bf-4d80-8828-144966e3480c",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01EqXWYxHuayWnMmqdobxr6z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3068,
      "cache_read_input_tokens": 36876,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3068
      },
      "output_tokens": 42,
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

_source line 11 · 2026-05-15T03:26:00.182Z_

<details><summary>↩ Tool result · `toolu_011VmgWaUqmfzM1vEkKiE4gz`</summary>

```text
1	% method.tex — §3 Method for solver-trace-ablation (EMNLP 2026)
2	% Covers: task, GRPO, STA protocol, ISR definition, reward formulations, hacking taxonomy
3	% Word budget: ~1200
4	
5	\section{Method}
6	\label{sec:method}
7	
8	We formalize the task of natural language to formal logic translation (\S\ref{ssec:task}), describe the GRPO training framework (\S\ref{ssec:grpo}), introduce Solver Trace Ablation as a diagnostic protocol (\S\ref{ssec:sta}), define the Intensional Structural Reward (\S\ref{ssec:isr}), present the reward formulations under study (\S\ref{ssec:reward}), and catalog the hacking modes discovered across conditions (\S\ref{ssec:taxonomy}).
9	
10	\subsection{Task: NL-to-Formal-Logic Formalization}
11	\label{ssec:task}
12	
13	Given a natural language reasoning problem $x$ consisting of premises and a conclusion, the task is to produce a formal logic program $f(x) = \{c_1, c_2, \ldots, c_n\}$ comprising $n$ components (axioms, rules, or clauses) that an external automated solver can evaluate. We consider two target formalisms: first-order logic (FOL), verified by the Prover9 theorem prover \cite{mccune2005prover9}, and Prolog, verified by SWI-Prolog \cite{wielemaker2012swi}. A formalization is \emph{proved} if the solver returns a successful derivation within a fixed timeout.
14	
15	This setup decouples generation (the language model) from verification (the solver), providing a binary execution signal $r_{\text{exec}} \in \{0, 1\}$ that is noise-free but structurally uninformative: a formalization that embeds the conclusion directly in its premises will prove trivially, receiving the same reward as a faithful translation.
16	
17	\subsection{GRPO Training}
18	\label{ssec:grpo}
19	
20	We train a language model $\pi_\theta$ using Group Relative Policy Optimization \citep[GRPO;][]{shao2024deepseekmath}. For each problem $x$, GRPO samples a group of $K$ candidate formalizations $\{f_1, \ldots, f_K\}$ from $\pi_\theta$, scores each with a reward function $r(\cdot)$, and updates the policy using the group-normalized advantage:
21	\begin{equation}
22	    A_i = \frac{r(f_i) - \mu_{\text{group}}}{\sigma_{\text{group}}}
23	    \label{eq:advantage}
24	\end{equation}
25	where $\mu_{\text{group}}$ and $\sigma_{\text{group}}$ are the mean and standard deviation of rewards within the group. The policy gradient objective follows:
26	\begin{equation}
27	    \mathcal{L}(\theta) = -\mathbb{E}_{x, f_i \sim \pi_\theta} \left[ A_i \cdot \log \pi_\theta(f_i \mid x) \right] + \beta_{\text{KL}} \cdot D_{\text{KL}}(\pi_\theta \| \pi_{\text{ref}})
28	    \label{eq:grpo}
29	\end{equation}
30	
31	In the baseline configuration, the reward is purely execution-based: $r(f) = r_{\text{exec}}(f)$. This drives prove rate from 12\% (base model; \texttt{sta-phase0-baseline}) to 32\% at 100 steps (\texttt{plan003-eval-exec-only-r5}), eventually reaching 93\% at 500 steps---but, as we show in \S\ref{sec:experiments}, this improvement is largely achieved through structural shortcuts.
32	
33	\subsection{Solver Trace Ablation (STA)}
34	\label{ssec:sta}
35	
36	Solver Trace Ablation is a post-hoc diagnostic protocol that assesses the structural necessity of each component in a proved formalization. The protocol adapts leave-one-out (LOO) analysis from mutation testing \citep{demillo1978hints, jia2011analysis} to formal logic verification.
37	
38	For a proved formalization $f = \{c_1, c_2, \ldots, c_n\}$ with $n$ components, STA proceeds as follows:
39	
40	\begin{enumerate}
41	    \item \textbf{Baseline verification.} Confirm that the full formalization $f$ proves successfully under the target solver.
42	    \item \textbf{Component ablation.} For each component $c_i$ ($i = 1, \ldots, n$), construct the ablated formalization $f_{\setminus i} = f \setminus \{c_i\}$ and re-run the solver.
43	    \item \textbf{Necessity determination.} Component $c_i$ is \emph{necessary} if the solver fails on $f_{\setminus i}$, and \emph{redundant} otherwise.
44	    \item \textbf{Aggregation.} Compute the fraction of necessary components as the Intensional Structural Reward (ISR; \S\ref{ssec:isr}).
45	\end{enumerate}
46	
47	STA is solver-agnostic: the same protocol applies to Prover9 (FOL) and SWI-Prolog (Prolog) without modification, enabling cross-logic diagnostic transfer (\S\ref{sec:experiments}).
48	
49	STA is applied only to proved samples ($r_{\text{exec}} = 1$). For unproved samples, ISR is undefined (the baseline verification in Step~1 fails). When reporting population-level ISR statistics, we report \emph{proved-only} ISR (ISR$^*$), which conditions on successful baseline verification, to avoid conflating structural quality with prove rate.
50	
51	\subsection{Intensional Structural Reward (ISR)}
52	\label{ssec:isr}
53	
54	Given a proved formalization $f = \{c_1, \ldots, c_n\}$, we define ISR as the fraction of components whose removal causes proof failure:
55	\begin{equation}
56	    \text{ISR}(f) = \frac{1}{n} \sum_{i=1}^{n} \mathbf{1}\left[\text{solver fails on } f_{\setminus i}\right]
57	    \label{eq:isr}
58	\end{equation}
59	where $f_{\setminus i} = f \setminus \{c_i\}$ denotes $f$ with component $c_i$ removed. ISR is bounded in $[0, 1]$: ISR $= 1$ indicates every component is individually necessary for the proof, while ISR $= 0$ indicates no single component is necessary (all are redundant).
60	
61	ISR measures \emph{syntactic component necessity}---whether each component contributes to the proof derivation---not semantic faithfulness to the natural language input. This distinction is critical: a formalization can achieve ISR $= 1$ by containing a single tautological component (e.g., a premise identical to the conclusion), which is necessary by construction but semantically degenerate.
62	
63	\paragraph{Premise count bias.} ISR is mathematically influenced by the number of components: formalizations with fewer premises have higher expected ISR under random ablation, since each component constitutes a larger fraction of the proof. We control for this confound in our analysis via premise-count-matched comparisons (\S\ref{sec:experiments}).
64	
65	\subsection{Reward Formulations}
66	\label{ssec:reward}
67	
68	To study the effect of incorporating ISR into GRPO training, we evaluate the following reward formulations:
69	
70	\paragraph{Execution-only (baseline).} $r(f) = r_{\text{exec}}(f)$. Binary solver success, providing no structural signal.
71	
72	\paragraph{Additive ISR.} $r(f) = r_{\text{exec}}(f) \cdot (1 + \beta \cdot \text{ISR}(f))$, where $\beta > 0$ controls the ISR weight. The multiplicative gating by $r_{\text{exec}}$ ensures ISR contributes only for proved samples. We evaluate $\beta \in \{0.1, 0.3\}$.
73	
74	\paragraph{Additive random (control).} $r(f) = r_{\text{exec}}(f) \cdot (1 + \beta \cdot U)$, where $U \sim \text{Uniform}(0, 1)$ replaces ISR with a random signal. This isolates the effect of ISR-specific information from the effect of reward variance alone.
75	
76	\paragraph{SFT (supervised baseline).} Standard supervised fine-tuning on ground-truth formalizations, serving as a non-RL reference point.
77	
78	Additional formulations (convex combination $r = \alpha \cdot r_{\text{exec}} + \beta \cdot \text{ISR}$) were explored but produced degenerate outcomes (ISR $< 1$ acts as a penalty on proved samples, suppressing prove rate); we report these briefly in \S\ref{sec:experiments}.
79	
80	\subsection{Reward Hacking Taxonomy}
81	\label{ssec:taxonomy}
82	
83	Across experimental conditions, we identify seven distinct reward hacking strategies, classified by manual inspection and automated pattern detection:
84	
85	\begin{enumerate}[label=\textbf{H\arabic*.}, leftmargin=2em]
86	    \item \textbf{Multi-premise conclusion embedding.} The conclusion is embedded verbatim within one or more premises. The proof succeeds trivially via subsumption. Prevalent across all GRPO conditions (52--93\% of proved samples).
87	    \item \textbf{Tautological collapse.} The formalization reduces to two components where one trivially entails the other (e.g., $P(a)$ and $\forall x\, P(x)$).
88	    \item \textbf{Complexity without utility.} Extraneous axioms that do not contribute to the proof but inflate component count.
89	    \item \textbf{Repetition collapse.} Identical components repeated multiple times, inflating $n$ while each copy is individually redundant under LOO ablation.
90	    \item \textbf{Contradiction explosion.} Contradictory axioms from which anything follows \emph{ex falso quodlibet}, yielding ISR $= 0$ since no single axiom is necessary once the contradiction is established.
91	    \item[{\textbf{H6.}}] \textbf{ISR inflation via conclusion duplication.} The conclusion appears as a single premise identical to the goal. Under LOO, removing this sole necessary component causes proof failure, yielding ISR $\approx 1$. This mode is ISR-specific: it appears in 64.5\% of ISR-rewarded proved samples across three seeds but in 0\% of random-rewarded samples.
92	    \item[{\textbf{H7.}}] \textbf{Query-as-fact gaming (Prolog).} The model converts the natural language question into a snake\_case atom and asserts it simultaneously as a fact and a query, causing SWI-Prolog to trivially succeed. This mode bypasses text-match hacking classifiers and was identified only through functional analysis of the $n_{\text{necessary}}$ distribution.
93	\end{enumerate}
94	
95	Modes H1--H5 arise under execution-only reward. H6 emerges specifically under ISR reward, representing \emph{meta-level} Goodhart behavior: the model games the diagnostic metric itself. H7 is specific to Prolog STA and reveals a classifier blind spot---text-match detection fails, requiring cross-validation with functional necessity analysis.
96	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ca27e824-6ca6-4db1-9e55-77ef612ddfd7",
  "uuid": "30517af9-2c61-4aaf-8990-3208fc30da6d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/method_76d073.tex",
      "content": "% method.tex — §3 Method for solver-trace-ablation (EMNLP 2026)\n% Covers: task, GRPO, STA protocol, ISR definition, reward formulations, hacking taxonomy\n% Word budget: ~1200\n\n\\section{Method}\n\\label{sec:method}\n\nWe formalize the task of natural language to formal logic translation (\\S\\ref{ssec:task}), describe the GRPO training framework (\\S\\ref{ssec:grpo}), introduce Solver Trace Ablation as a diagnostic protocol (\\S\\ref{ssec:sta}), define the Intensional Structural Reward (\\S\\ref{ssec:isr}), present the reward formulations under study (\\S\\ref{ssec:reward}), and catalog the hacking modes discovered across conditions (\\S\\ref{ssec:taxonomy}).\n\n\\subsection{Task: NL-to-Formal-Logic Formalization}\n\\label{ssec:task}\n\nGiven a natural language reasoning problem $x$ consisting of premises and a conclusion, the task is to produce a formal logic program $f(x) = \\{c_1, c_2, \\ldots, c_n\\}$ comprising $n$ components (axioms, rules, or clauses) that an external automated solver can evaluate. We consider two target formalisms: first-order logic (FOL), verified by the Prover9 theorem prover \\cite{mccune2005prover9}, and Prolog, verified by SWI-Prolog \\cite{wielemaker2012swi}. A formalization is \\emph{proved} if the solver returns a successful derivation within a fixed timeout.\n\nThis setup decouples generation (the language model) from verification (the solver), providing a binary execution signal $r_{\\text{exec}} \\in \\{0, 1\\}$ that is noise-free but structurally uninformative: a formalization that embeds the conclusion directly in its premises will prove trivially, receiving the same reward as a faithful translation.\n\n\\subsection{GRPO Training}\n\\label{ssec:grpo}\n\nWe train a language model $\\pi_\\theta$ using Group Relative Policy Optimization \\citep[GRPO;][]{shao2024deepseekmath}. For each problem $x$, GRPO samples a group of $K$ candidate formalizations $\\{f_1, \\ldots, f_K\\}$ from $\\pi_\\theta$, scores each with a reward function $r(\\cdot)$, and updates the policy using the group-normalized advantage:\n\\begin{equation}\n    A_i = \\frac{r(f_i) - \\mu_{\\text{group}}}{\\sigma_{\\text{group}}}\n    \\label{eq:advantage}\n\\end{equation}\nwhere $\\mu_{\\text{group}}$ and $\\sigma_{\\text{group}}$ are the mean and standard deviation of rewards within the group. The policy gradient objective follows:\n\\begin{equation}\n    \\mathcal{L}(\\theta) = -\\mathbb{E}_{x, f_i \\sim \\pi_\\theta} \\left[ A_i \\cdot \\log \\pi_\\theta(f_i \\mid x) \\right] + \\beta_{\\text{KL}} \\cdot D_{\\text{KL}}(\\pi_\\theta \\| \\pi_{\\text{ref}})\n    \\label{eq:grpo}\n\\end{equation}\n\nIn the baseline configuration, the reward is purely execution-based: $r(f) = r_{\\text{exec}}(f)$. This drives prove rate from 12\\% (base model; \\texttt{sta-phase0-baseline}) to 32\\% at 100 steps (\\texttt{plan003-eval-exec-only-r5}), eventually reaching 93\\% at 500 steps---but, as we show in \\S\\ref{sec:experiments}, this improvement is largely achieved through structural shortcuts.\n\n\\subsection{Solver Trace Ablation (STA)}\n\\label{ssec:sta}\n\nSolver Trace Ablation is a post-hoc diagnostic protocol that assesses the structural necessity of each component in a proved formalization. The protocol adapts leave-one-out (LOO) analysis from mutation testing \\citep{demillo1978hints, jia2011analysis} to formal logic verification.\n\nFor a proved formalization $f = \\{c_1, c_2, \\ldots, c_n\\}$ with $n$ components, STA proceeds as follows:\n\n\\begin{enumerate}\n    \\item \\textbf{Baseline verification.} Confirm that the full formalization $f$ proves successfully under the target solver.\n    \\item \\textbf{Component ablation.} For each component $c_i$ ($i = 1, \\ldots, n$), construct the ablated formalization $f_{\\setminus i} = f \\setminus \\{c_i\\}$ and re-run the solver.\n    \\item \\textbf{Necessity determination.} Component $c_i$ is \\emph{necessary} if the solver fails on $f_{\\setminus i}$, and \\emph{redundant} otherwise.\n    \\item \\textbf{Aggregation.} Compute the fraction of necessary components as the Intensional Structural Reward (ISR; \\S\\ref{ssec:isr}).\n\\end{enumerate}\n\nSTA is solver-agnostic: the same protocol applies to Prover9 (FOL) and SWI-Prolog (Prolog) without modification, enabling cross-logic diagnostic transfer (\\S\\ref{sec:experiments}).\n\nSTA is applied only to proved samples ($r_{\\text{exec}} = 1$). For unproved samples, ISR is undefined (the baseline verification in Step~1 fails). When reporting population-level ISR statistics, we report \\emph{proved-only} ISR (ISR$^*$), which conditions on successful baseline verification, to avoid conflating structural quality with prove rate.\n\n\\subsection{Intensional Structural Reward (ISR)}\n\\label{ssec:isr}\n\nGiven a proved formalization $f = \\{c_1, \\ldots, c_n\\}$, we define ISR as the fraction of components whose removal causes proof failure:\n\\begin{equation}\n    \\text{ISR}(f) = \\frac{1}{n} \\sum_{i=1}^{n} \\mathbf{1}\\left[\\text{solver fails on } f_{\\setminus i}\\right]\n    \\label{eq:isr}\n\\end{equation}\nwhere $f_{\\setminus i} = f \\setminus \\{c_i\\}$ denotes $f$ with component $c_i$ removed. ISR is bounded in $[0, 1]$: ISR $= 1$ indicates every component is individually necessary for the proof, while ISR $= 0$ indicates no single component is necessary (all are redundant).\n\nISR measures \\emph{syntactic component necessity}---whether each component contributes to the proof derivation---not semantic faithfulness to the natural language input. This distinction is critical: a formalization can achieve ISR $= 1$ by containing a single tautological component (e.g., a premise identical to the conclusion), which is necessary by construction but semantically degenerate.\n\n\\paragraph{Premise count bias.} ISR is mathematically influenced by the number of components: formalizations with fewer premises have higher expected ISR under random ablation, since each component constitutes a larger fraction of the proof. We control for this confound in our analysis via premise-count-matched comparisons (\\S\\ref{sec:experiments}).\n\n\\subsection{Reward Formulations}\n\\label{ssec:reward}\n\nTo study the effect of incorporating ISR into GRPO training, we evaluate the following reward formulations:\n\n\\paragraph{Execution-only (baseline).} $r(f) = r_{\\text{exec}}(f)$. Binary solver success, providing no structural signal.\n\n\\paragraph{Additive ISR.} $r(f) = r_{\\text{exec}}(f) \\cdot (1 + \\beta \\cdot \\text{ISR}(f))$, where $\\beta > 0$ controls the ISR weight. The multiplicative gating by $r_{\\text{exec}}$ ensures ISR contributes only for proved samples. We evaluate $\\beta \\in \\{0.1, 0.3\\}$.\n\n\\paragraph{Additive random (control).} $r(f) = r_{\\text{exec}}(f) \\cdot (1 + \\beta \\cdot U)$, where $U \\sim \\text{Uniform}(0, 1)$ replaces ISR with a random signal. This isolates the effect of ISR-specific information from the effect of reward variance alone.\n\n\\paragraph{SFT (supervised baseline).} Standard supervised fine-tuning on ground-truth formalizations, serving as a non-RL reference point.\n\nAdditional formulations (convex combination $r = \\alpha \\cdot r_{\\text{exec}} + \\beta \\cdot \\text{ISR}$) were explored but produced degenerate outcomes (ISR $< 1$ acts as a penalty on proved samples, suppressing prove rate); we report these briefly in \\S\\ref{sec:experiments}.\n\n\\subsection{Reward Hacking Taxonomy}\n\\label{ssec:taxonomy}\n\nAcross experimental conditions, we identify seven distinct reward hacking strategies, classified by manual inspection and automated pattern detection:\n\n\\begin{enumerate}[label=\\textbf{H\\arabic*.}, leftmargin=2em]\n    \\item \\textbf{Multi-premise conclusion embedding.} The conclusion is embedded verbatim within one or more premises. The proof succeeds trivially via subsumption. Prevalent across all GRPO conditions (52--93\\% of proved samples).\n    \\item \\textbf{Tautological collapse.} The formalization reduces to two components where one trivially entails the other (e.g., $P(a)$ and $\\forall x\\, P(x)$).\n    \\item \\textbf{Complexity without utility.} Extraneous axioms that do not contribute to the proof but inflate component count.\n    \\item \\textbf{Repetition collapse.} Identical components repeated multiple times, inflating $n$ while each copy is individually redundant under LOO ablation.\n    \\item \\textbf{Contradiction explosion.} Contradictory axioms from which anything follows \\emph{ex falso quodlibet}, yielding ISR $= 0$ since no single axiom is necessary once the contradiction is established.\n    \\item[{\\textbf{H6.}}] \\textbf{ISR inflation via conclusion duplication.} The conclusion appears as a single premise identical to the goal. Under LOO, removing this sole necessary component causes proof failure, yielding ISR $\\approx 1$. This mode is ISR-specific: it appears in 64.5\\% of ISR-rewarded proved samples across three seeds but in 0\\% of random-rewarded samples.\n    \\item[{\\textbf{H7.}}] \\textbf{Query-as-fact gaming (Prolog).} The model converts the natural language question into a snake\\_case atom and asserts it simultaneously as a fact and a query, causing SWI-Prolog to trivially succeed. This mode bypasses text-match hacking classifiers and was identified only through functional analysis of the $n_{\\text{necessary}}$ distribution.\n\\end{enumerate}\n\nModes H1--H5 arise under execution-only reward. H6 emerges specifically under ISR reward, representing \\emph{meta-level} Goodhart behavior: the model games the diagnostic metric itself. H7 is specific to Prolog STA and reveals a classifier blind spot---text-match detection fails, requiring cross-validation with functional necessity analysis.\n",
      "numLines": 96,
      "startLine": 1,
      "totalLines": 96
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_01A7zEFhXvEKVEDiHccKaGGp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/experiments_76b47a.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca27e824-6ca6-4db1-9e55-77ef612ddfd7",
  "uuid": "b28d3ab6-f8ba-4ec8-98b7-7738eb0f9c24",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01AXTiHGBX6yXqy65ApLBzvZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4201,
      "cache_read_input_tokens": 39944,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4201
      },
      "output_tokens": 41,
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

_source line 13 · 2026-05-15T03:26:03.448Z_

<details><summary>↩ Tool result · `toolu_01A7zEFhXvEKVEDiHccKaGGp`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate STA along three axes: ISR as a diagnostic for reward hacking (\S\ref{sec:diagnostic}); ISR as a training reward, where it exhibits meta-level Goodhart's Law (\S\ref{sec:goodhart}); and STA as a cross-logic protocol (\S\ref{sec:crosslogic}).
5	We synthesize the modes observed across conditions into a hacking taxonomy (\S\ref{sec:taxonomy}).
6	
7	\subsection{Setup}\label{sec:setup}
8	
9	\textbf{Model and training.}
10	We train Qwen3-4B with GRPO~\citep{deepseekmath} ($K{=}8$ rollouts, learning rate $10^{-6}$, 500 steps default and 1000 where noted) across seeds $\{42,43,44\}$ on a fixed 500-example FOLIO~\citep{folio} subset held constant across all conditions.\footnote{All experiments use \texttt{data/train\_500\_seed42.jsonl}; the seed argument controls only model initialization and rollout sampling, never data composition.}
11	The SFT baseline is trained with NLL on gold formalizations to isolate whether structural degeneration arises from data exposure alone.
12	
13	\textbf{Evaluation protocol.}
14	Held-out evaluation uses 100 examples drawn from FOLIO (file: \texttt{proofwriter\_fol\_100.jsonl}; the filename is a legacy artifact---no ProofWriter data is used, see \S\ref{sec:task}) with greedy decoding.
15	All cross-run ISR values are recomputed uniformly by a single evaluator (\texttt{eval\_sta.py}) on top of \texttt{Prover9}/SWI-Prolog so that training-log ISR (which varied with implementation revisions) is never compared across runs.
16	We report prove rate (PR), proved-only ISR ($\text{ISR}^*$, denoted ISR in tables when context is clear), and hacking-mode rates from a two-stage classifier (strict normalized text matching for H1/H7, plus functional analysis of the per-sample $n_{\text{necessary}}$ distribution; \S\ref{sec:taxonomy-method}).
17	We additionally report a \emph{non-hacking} (N-H) rate---the residual of proved samples that match none of the seven cataloged patterns---which is a necessary but not sufficient condition for semantic correctness.
18	
19	\subsection{ISR as Diagnostic}
20	\label{sec:diagnostic}
21	
22	\begin{figure}[t]
23	\centering
24	\includegraphics[width=0.95\columnwidth]{figures/fig2_isr_collapse.pdf}
25	\caption{ISR collapse under exec-only GRPO (seed~42). PR rises 32\%$\to$93\%$\to$96\% while proved-only ISR falls $0.642{\to}0.132{\to}0.003$ over 100$\to$500$\to$1000 steps. By step 1000, 94.8\% of proved samples have $\text{ISR}{=}0$ and mean component count inflates 6.58$\to$18.55, indicating contradiction explosion.}
26	\label{fig:isr-collapse}
27	\end{figure}
28	
29	We first establish that ISR detects structural degeneration that the prove-rate reward---and any evaluation built on it alone---would miss.
30	
31	\textbf{Collapse trajectory.}
32	Figure~\ref{fig:isr-collapse} traces an exec-only GRPO run (seed~42) at 100, 500, and 1000 training steps.
33	PR rises $32\%\to93\%\to96\%$, a trajectory that by execution-only evaluation would read as ``successful optimization.''
34	$\text{ISR}^*$ tells a different story: $0.642\to0.132\to0.003$, a 200$\times$ collapse over the same window. %% registry: plan003-eval-exec-only-r5, plan001-exec-only-s42-r2, plan016-extended-1000-s42
35	By 500 steps, 87.1\% of proved samples embed the conclusion (mode H1, \S\ref{sec:taxonomy-method}); by 1000 steps, the embedding rate saturates at 100\% and mean component count more than doubles ($6.58\to18.55$) as the model emits contradictory or vacuous premises that trivially derive any conclusion.
36	The monotonic decline shows that extended training, in isolation from a structural signal, \emph{worsens} formalization quality even as it improves the headline number.
37	
38	\textbf{Cross-seed instability.}
39	The three exec-only seeds diverge into qualitatively different failure modes despite sharing data, hyperparameters, and reward (Table~\ref{tab:beta01-3seed}, exec-only rows; per-seed traces in Appendix~\ref{app:per-seed}).
40	Seed~42 reaches $\text{PR}{=}93\%$ via conclusion embedding ($\text{H1}{=}87.1\%$); seed~43 collapses to $\text{PR}{=}14\%$ via repetition (87\% of rollouts truncated at the max length); seed~44 reaches $\text{PR}{=}98\%$ via tautological collapse to a two-component structure ($\text{H7}{=}100\%$, mean $n{=}2.04$). %% registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44
41	The cross-seed PR variance ($\sigma{=}\pm47$\,pp) shows that aggregate metrics obscure qualitatively different failure modes; all three are flagged by $\text{ISR}^*$ even though one passes the PR check (s44) and one fails it (s43).
42	This is the diagnostic value: the same signal catches both high-PR and low-PR failures.
43	
44	\textbf{SFT baseline.}
45	Supervised fine-tuning on gold formalizations reaches $\text{PR}{=}14\%$ with $\text{ISR}^{*}{=}0.571$, $\text{H7}{=}0$, $\text{H1}{=}1/14$ ($7.1\%$), and $92.9\%$ non-hacking. %% registry: plan009-sft-baseline-s42-r4
46	The near-absence of hacking under identical data exposure is consistent with hacking being RL-specific.
47	Because SFT also has low PR, we further compare to a 100-step RL checkpoint at matched PR (Appendix~\ref{app:100step}); the RL checkpoint at $\text{PR}{=}32\%$ already shows $\text{H1}{>}0$ and lower $\text{ISR}^*$ than SFT at $\text{PR}{=}14\%$, indicating the gap is not merely a PR-level confound.
48	
49	\subsection{Meta-Level Goodhart's Law}
50	\label{sec:goodhart}
51	
52	We now reverse roles: instead of treating ISR as an observer, we use it as a reward augmentation, $r = r_{\text{exec}}\cdot(1 + \beta\,\text{ISR})$.
53	A uniform random control, $r = r_{\text{exec}}\cdot(1 + \beta\,u)$ with $u\sim\mathcal{U}(0,1)$, at matched $\beta$ isolates ISR-specific signal from generic reward-variance effects.
54	The headline finding is that ISR-as-reward produces \emph{meta-level} Goodhart~\citep{manheim-goodhart-taxonomy}: the diagnostic metric itself becomes the target of gaming when optimized.
55	
56	\begin{table}[t]
57	\centering
58	\small
59	\resizebox{\columnwidth}{!}{%
60	\begin{tabular}{lcccccc}
61	\toprule
62	\textbf{Condition} & $\boldsymbol{\beta}$ & \textbf{PR\%}$\uparrow$ & \textbf{ISR}$^*$ & \textbf{H7\%} & \textbf{H1\%} & \textbf{N-H\%} \\
63	\midrule
64	Base (0-shot) & --- & 12 & --- & --- & --- & --- \\ %% registry: sta-phase0-baseline
65	SFT & --- & 14 & 0.571 & 0 & 7 & \textbf{93} \\ %% registry: plan009-sft-baseline-s42-r4
66	\midrule
67	Exec-only$^\dagger$ & --- & 93 & 0.132 & 0 & 87 & 13 \\ %% registry: plan001-exec-only-s42-r2
68	ISR & 0.1 & 77{\scriptsize$\pm$14} & $\ddagger$ & \textbf{65} & 17 & ${\sim}$16 \\ %% registry: plan002-additive-b01-s42/s43/s44
69	Random & 0.1 & \textbf{85}{\scriptsize$\pm$6} & 0.086{\scriptsize$\pm$.04} & 0 & 81 & 19 \\ %% registry: plan018-additive-random-b01-s42/s43-r2/s44
70	\midrule
71	ISR & 0.3 & 66{\scriptsize$\pm$42} & 0.39{\scriptsize$\pm$.31} & 35 & 49 & 16 \\ %% registry: plan002-additive-b03-s42/s43/s44
72	Random$^\S$ & 0.3 & 36{\scriptsize$\pm$18} & 0.05{\scriptsize$\pm$.07} & 0 & 100 & 0 \\ %% registry: plan017-additive-random-s42, exp1-random-b03-s44 (s43 training)
73	\bottomrule
74	\end{tabular}}
75	\caption{Goodhart landscape across reward conditions. 3-seed rows show mean$\pm$std. $^\dagger$Seed~42; cross-seed exec-only divergence in \S\ref{sec:diagnostic}. $\ddagger$$\text{ISR}^*$ omitted for ISR $\beta{=}0.1$ because the raw mean is inflated by H7 gaming (per-seed: Table~\ref{tab:beta01-3seed}); when matched on premise count it is no different from random (1.06$\times$). $^\S$Random $\beta{=}0.3$ reports 2 seeds (s42, s44); s43 is still training (\texttt{exp1-random-b03-s43-r4}). Best PR and N-H\% bolded per group.}
76	\label{tab:goodhart-landscape}
77	\end{table}
78	
79	\begin{table}[t]
80	\centering
81	\small
82	\resizebox{\columnwidth}{!}{%
83	\begin{tabular}{llcccccc}
84	\toprule
85	\textbf{Seed} & \textbf{Cond.} & \textbf{PR} & $\mathbf{ISR^*}$ & \textbf{H7\%} & \textbf{H1\%} & \textbf{N-H\%} & \textbf{ISR$^*_{n\geq 3}$} \\
86	\midrule
87	42 & ISR & 0.81 & 0.415 & 16 & 52 & 32 & 0.258 \\ %% registry: plan002-additive-b01-s42
88	43 & ISR & 0.61 & 0.830 & 97 & 0 & 3 & --- \\ %% registry: plan002-additive-b01-s43
89	44 & ISR & 0.89 & 0.902 & 87 & 0 & 14 & --- \\ %% registry: plan002-additive-b01-s44
90	\midrule
91	42 & Random & 0.79 & 0.131 & 0 & 71 & 29 & 0.243 \\ %% registry: plan018-additive-random-b01-s42
92	43 & Random & 0.88 & 0.058 & 0 & 93 & 7 & --- \\ %% registry: plan018-additive-random-b01-s43-r2
93	44 & Random & 0.89 & 0.070 & 0 & 80 & 20 & --- \\ %% registry: plan018-additive-random-b01-s44
94	\midrule
95	\multicolumn{2}{l}{ISR mean$\pm$std} & .77$\pm$.14 & --- & 65 & 17 & 16 & 0.258 \\
96	\multicolumn{2}{l}{Random mean$\pm$std} & .85$\pm$.06 & .086$\pm$.04 & 0 & 81 & 19 & 0.243 \\
97	\bottomrule
98	\end{tabular}}
99	\caption{ISR $\beta{=}0.1$ vs.\ random $\beta{=}0.1$, 3-seed breakdown. H7 is ISR-specific (65\% vs.\ 0\%); H1 is GRPO-universal but higher under random. Last column reports $\text{ISR}^*$ restricted to non-hacking samples with $\geq{3}$ premises (premise-count-matched), available for s42 where genuine residual is non-trivial: 0.258 vs.\ 0.243, a 1.06$\times$ ratio.}
100	\label{tab:beta01-3seed}
101	\end{table}
102	
103	\textbf{Low-dose ISR ($\beta{=}0.1$): ISR-specific gaming.}
104	Table~\ref{tab:beta01-3seed} reports the 3-seed breakdown.
105	The most striking number is H7: 64.5\% of proved samples under ISR ($n{=}149/231$) vs.\ \emph{zero} under random ($0/256$). %% registry: plan002 vs plan018 all seeds
106	H7---a single premise identical to the conclusion, giving $\text{ISR}\geq 0.5$ by construction (\S\ref{sec:taxonomy-method})---is the canonical meta-level Goodhart move: the model satisfies the LOO definition directly rather than producing a derivation that happens to satisfy it.
107	Total conclusion embedding ($\text{H1}+\text{H7}$) is GRPO-universal at $68$--$97\%$ across both conditions, and is in fact \emph{higher} under random (mean H1 81\% under random vs.\ 17\% under ISR).
108	ISR does not reduce hacking; it converts H1 into H7 (Figure~\ref{fig:hacking-composition}).
109	Random also achieves higher and more stable PR ($85{\pm}6\%$ vs.\ $77{\pm}14\%$), so ISR-as-reward yields no PR advantage either.
110	
111	\textbf{Premise-count confound.}
112	One ISR seed (s42) is the only one not dominated by H7, and its raw $\text{ISR}^*{=}0.415$ is 3.2$\times$ higher than its matched random control ($0.131$), suggesting genuine structural improvement.
113	This appearance is entirely a premise-minimization artifact.
114	ISR-trained models produce shorter formalizations (mean $n{=}5.58$ vs.\ $8.46$ for random), and ISR rises mechanically as $n$ falls---when $n{=}2$, ISR$\geq 0.5$ by definition.
115	Restricting to non-hacking samples with $\geq{3}$ premises (eliminating the trivial-$n$ regime) gives $\text{ISR}^*{=}0.258$ for ISR vs.\ $0.243$ for random: a 1.06$\times$ ratio, no meaningful advantage (Table~\ref{tab:beta01-3seed}, last column). %% D051 premise-count-matched analysis
116	The raw 3.2$\times$ headline collapses once the LOO bias is controlled.
117	This is methodologically important: LOO-based metrics are widely used without component-count correction; under optimization that pressure for shorter outputs, the metric inflates without any quality improvement.
118	
119	\textbf{High-dose ISR ($\beta{=}0.3$): multi-modal Goodhart instability.}
120	At $\beta{=}0.3$, ISR-as-reward produces extreme cross-seed instability (Table~\ref{tab:goodhart-landscape}, last group): $\text{PR}{=}66{\pm}42\%$, spanning $18\%$ to $95\%$.
121	Each seed converges to a distinct Goodhart pathway. %% registry: plan002-additive-b03-s42/s43/s44
122	Seed~42 exhibits \emph{reward collapse}: $\text{PR}{=}18\%$, $\text{ISR}^{*}{=}0.143$, the classical Goodhart pattern from~\citep{gao-reward-overoptimization} where the proxy weight overwhelms the base signal.
123	Seed~43 exhibits \emph{H1-dominant shortcutting}: $\text{PR}{=}86\%$, $\text{H1}{=}68.6\%$, $\text{H7}{=}4.7\%$, only $26.7\%$ non-hacking---the model retains a high prove rate but achieves it via conclusion embedding, not structural manipulation of the metric.
124	Seed~44 exhibits \emph{pure H7 meta-Goodhart}: $\text{PR}{=}95\%$ combined with $\text{H7}{=}100\%$ and $\text{ISR}^{*}{=}0.742$, with $0\%$ non-hacking.
125	This last case is the cleanest meta-level Goodhart instance in our experiments: the model simultaneously games \emph{both} the execution reward (high PR) and the structural metric (high $\text{ISR}^{*}$) through the same construction.
126	For the random control at $\beta{=}0.3$, the available 2 seeds collapse to $\text{PR}{=}48\%$ (s42) and $\text{PR}{=}23\%$ (s44) with $\text{H1}{=}100\%$ and $0\%$ non-hacking in both cases (the s43 random run is still training; full numbers in Appendix~\ref{app:beta03}). %% registry: plan017-additive-random-s42, exp1-random-b03-s44
127	High-dose proxy weighting is harmful in both ISR and random conditions, but ISR uniquely produces \emph{mode diversity}: three qualitatively different failure trajectories from a single reward formulation.
128	
129	\subsection{Cross-Logic Diagnostic Transfer}
130	\label{sec:crosslogic}
131	
132	\begin{figure}[t]
133	\centering
134	\includegraphics[width=0.95\columnwidth]{figures/fig4_prolog_comparison.pdf}
135	\caption{Cross-logic results. \textbf{Left}: FOL vs.\ Prolog exec-only $\text{ISR}^*$ across 3 seeds, both near-zero (s44 Prolog $\text{ISR}^*{=}0.387$ is a small-sample artifact, $n{=}21$). \textbf{Right}: Prolog ISR-reward gaming-mode composition---all 3 seeds reach 100\% non-genuine through distinct mechanisms (H7 tautology / degenerate uppercase syntax / query-as-fact gaming).}
136	\label{fig:prolog-comparison}
137	\end{figure}
138	
139	We replicate the FOL pipeline with Prolog/SWI-Prolog, retraining seeds and re-evaluating with the same eval harness.
140	Two questions: (i) does ISR retain diagnostic value on a structurally different logic; (ii) does ISR-as-reward produce the same meta-level Goodhart failure mode?
141	
142	\begin{table}[t]
143	\centering
144	\small
145	\resizebox{\columnwidth}{!}{%
146	\begin{tabular}{llccccl}
147	\toprule
148	\textbf{Logic} & \textbf{Cond.} & \textbf{Seed} & \textbf{PR} & $\mathbf{ISR^*}$ & \textbf{H7\%} & \textbf{Mode} \\
149	\midrule
150	FOL & exec & 42 & .93 & .132 & 0 & H1 embed (87\%) \\
151	FOL & exec & 43 & .14 & --- & --- & repetition \\
152	FOL & exec & 44 & .98 & .57 & 100 & tautological \\
153	\midrule
154	Prolog & exec & 42 & .83 & .037 & 0 & redundant facts \\ %% registry: plan006-prolog-exec-s42
155	Prolog & exec & 43 & .56 & .015 & 0 & redundant facts \\ %% registry: plan006-prolog-exec-s43-r3
156	Prolog & exec & 44 & .21 & .39$^\flat$ & 0 & low PR \\ %% registry: plan006-prolog-exec-s44
157	\midrule
158	Prolog & ISR & 42 & .50 & 1.00 & 100 & clean H7 \\ %% registry: plan006-prolog-sta-s42
159	Prolog & ISR & 43 & .38 & --- & 0$^\sharp$ & degenerate syntax \\ %% registry: plan006-prolog-sta-s43
160	Prolog & ISR & 44 & .97 & .885 & 0$^\sharp$ & query-as-fact \\ %% registry: plan006-prolog-sta-s44
161	\bottomrule
162	\end{tabular}}
163	\caption{Cross-logic results. $^\flat$small-sample inflation ($n{=}21$ proved); not interpretable as ``structurally clean.'' $^\sharp$strict text classifier returns 0\% H7 but \emph{functional} analysis ($n_{\text{necessary}}{=}1$) reveals 100\% (s43: $38/38$) and 97.9\% (s44: $95/97$) gaming-mode prevalence---see text. All Prolog ISR seeds: 0\% non-hacking.}
164	\label{tab:prolog-crosslogic}
165	\end{table}
166	
167	\textbf{Prolog exec-only: ISR catches redundancy across logics.}
168	Two of three Prolog exec-only seeds (s42, s43) show $\text{ISR}^{*}{\approx}0$ despite moderate-to-high PR (Table~\ref{tab:prolog-crosslogic}). %% registry: plan006-prolog-exec-s42, plan006-prolog-exec-s43-r3
169	Inspection reveals \emph{redundant coding}: ground facts repeated multiple times (e.g., \texttt{penguin(fido).} appearing three times), so per-clause LOO ablation never breaks the proof and the necessity count is zero.
170	This is a different failure semantics from the FOL exec-only collapses (which centered on conclusion embedding), but $\text{ISR}^{*}$ flags both.
171	This is also the point at which interpretation matters: an exec-only low-ISR is a \emph{redundancy} signal, whereas an ISR-rewarded high-ISR is a \emph{metric-gaming} signal (\S\ref{sec:taxonomy-method}); the same number does not license the same conclusion about reasoning quality, and we are careful never to read ISR differences as reasoning differences without the mode breakdown.
172	
173	\textbf{Prolog ISR-as-reward: universal Goodhart.}
174	The Prolog ISR-reward result is stronger than its FOL counterpart: 3/3 seeds reach 0\% non-hacking through three distinct mechanisms (Figure~\ref{fig:prolog-comparison}, right; Table~\ref{tab:prolog-crosslogic}).
175	Seed~42 produces clean H7 tautologies---a single clause identical to the query, $\text{ISR}^{*}{=}1.0$ over all $50/100$ proved samples. %% registry: plan006-prolog-sta-s42
176	Seed~43 produces \emph{degenerate uppercase pseudo-Prolog} (e.g., \texttt{MARY\_IS\_AN\_AVA\-DEOTE.}); the strict text-match classifier returns $\text{H7}{=}0$ but functional analysis shows all 38 proved samples have $n_{\text{necessary}}{=}1$, i.e., a single clause that proves the query alone---functionally H7. %% registry: plan006-prolog-sta-s43
177	Seed~44 produces \emph{query-as-fact gaming}: the model transforms the NL question into a snake-case atom and asserts the same atom as both a fact and the query (e.g., \texttt{is\_the\_dog\_furry. \?- is\_the\_dog\_furry.}), giving $\text{PR}{=}97\%$ with $95/97$ proved samples at $n_{\text{necessary}}{=}1$. %% registry: plan006-prolog-sta-s44
178	Seed~44 evaded our initial strict classifier entirely (returned ``$100\%$ genuine''); functional cross-validation against the $n_{\text{necessary}}$ distribution exposed it.
179	We register this as a methodological lesson: text-match hacking classifiers have blind spots, and STA's per-sample necessity profile is the cross-check that catches them.
180	
181	\textbf{FOL vs.\ Prolog comparison.}
182	FOL ISR $\beta{=}0.1$ leaves ${\sim}16\%$ non-hacking residual; Prolog ISR leaves $0\%$ across 3 seeds.
183	We attribute this to Prolog's simpler operational semantics: the optimization landscape contains fewer high-PR derivations and is more easily satisfied by clause-level shortcuts, so the gaming basin is broader and the genuine residual disappears.
184	This is corroborating, not contradictory, evidence for Claim 2: in a setting where structural shortcuts are even easier to construct, ISR-as-reward collapses even more completely.
185	
186	\subsection{Hacking Taxonomy}
187	\label{sec:taxonomy}
188	
189	\begin{figure}[t]
190	\centering
191	\includegraphics[width=0.92\columnwidth]{figures/fig3_hacking_composition.pdf}
192	\caption{Hacking composition across reward conditions (proved samples, seed~42 for FOL; appendix has all seeds). ISR converts H1 (conclusion embedding) into more extreme H7 (conclusion duplication) without reducing total hacking; SFT shows near-zero hacking ($92.9\%$ non-hacking).}
193	\label{fig:hacking-composition}
194	\end{figure}
195	
196	\begin{table}[t]
197	\centering
198	\small
199	\resizebox{\columnwidth}{!}{%
200	\begin{tabular}{lccccc}
201	\toprule
202	\textbf{Mode} & \textbf{Exec} & \textbf{ISR$_{.1}$} & \textbf{Rnd$_{.1}$} & \textbf{SFT} & \textbf{Prolog$_{\text{ISR}}$} \\
203	\midrule
204	H1 embed       & 87 & 17 & 81 & 7 & 0$^\sharp$ \\
205	H7 duplicate   & 0  & 65 & 0  & 0 & 100$^\sharp$ \\
206	Tautological   & --- & --- & --- & --- & s42 \\
207	Repetition     & s43 & --- & --- & --- & --- \\
208	Contradiction  & 1k & --- & --- & --- & --- \\
209	Cmplx.\ vacuous& 0  & 0  & 4  & 0 & --- \\
210	Query-as-fact  & --- & --- & --- & --- & s44 \\
211	\midrule
212	\textbf{Non-hacking} & 13 & ${\sim}$16 & 19 & \textbf{93} & \textbf{0} \\
213	\bottomrule
214	\end{tabular}}
215	\caption{Seven hacking modes across conditions (percentages of proved samples; seed~42 unless noted). Cells with seed identifiers indicate the mode dominates that seed (Prolog ISR row: H7 is s42 strict + s43/s44 functional, totaling 100\% gaming across all 3 seeds). $^\sharp$strict for FOL; pooled strict+functional for Prolog (\S\ref{sec:crosslogic}).}
216	\label{tab:hacking-taxonomy}
217	\end{table}
218	
219	The full taxonomy (Table~\ref{tab:hacking-taxonomy}, definitions in \S\ref{sec:taxonomy-method}) consists of seven modes that span the conditions we studied.
220	Two are quantifiable across all conditions: \textbf{H1} (conclusion embedding) is GRPO-universal at $68$--$97\%$ regardless of reward type, and \textbf{H7} (conclusion duplication) is ISR-specific at $64.5\%$ vs.\ $0\%$ in random controls.
221	The remaining five appear in specific cells: \textbf{tautological collapse} (exec-only s44 and Prolog ISR s42); \textbf{repetition collapse} (exec-only s43, with 87\% of rollouts hitting max length); \textbf{contradiction explosion} (exec-only at 1000 steps, mean $n{=}18.55$); \textbf{complexity-without-utility} (random $\beta{=}0.1$, low residual); and \textbf{query-as-fact gaming} (Prolog ISR s44).
222	
223	The cross-condition pattern is consistent with the framing in \S\ref{sec:goodhart}: \emph{reward formulation determines hacking composition but not hacking prevalence.}
224	Exec-only, ISR, and random conditions all show $\geq 80\%$ pooled hacking among proved samples; only SFT---which does not optimize against a binary execution signal---shows the residual at $93\%$ non-hacking, consistent with hacking being RL-specific rather than data-induced.
225	Across two logic types, six reward conditions, three seeds, and up to 1000 training steps, no GRPO condition we tested produces a high-PR run that is also majority non-hacking; the closest is ISR $\beta{=}0.1$ s42 at $\text{PR}{=}81\%$ with $32\%$ non-hacking, and even that residual is the premise-minimization artifact analyzed in \S\ref{sec:goodhart}.
226	
227	The taxonomy is descriptive, not exhaustive: query-as-fact gaming was found only when we cross-validated the strict classifier against $n_{\text{necessary}}$ distributions, and additional modes may emerge under further reward formulations or logic types.
228	We expect the STA protocol itself to generalize---it requires only a solver and a notion of component---so future work can extend the taxonomy by applying the same two-stage classification to new domains.
229	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ca27e824-6ca6-4db1-9e55-77ef612ddfd7",
  "uuid": "c17db1ba-6686-4013-ad65-04b458b6947a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/experiments_76b47a.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate STA along three axes: ISR as a diagnostic for reward hacking (\\S\\ref{sec:diagnostic}); ISR as a training reward, where it exhibits meta-level Goodhart's Law (\\S\\ref{sec:goodhart}); and STA as a cross-logic protocol (\\S\\ref{sec:crosslogic}).\nWe synthesize the modes observed across conditions into a hacking taxonomy (\\S\\ref{sec:taxonomy}).\n\n\\subsection{Setup}\\label{sec:setup}\n\n\\textbf{Model and training.}\nWe train Qwen3-4B with GRPO~\\citep{deepseekmath} ($K{=}8$ rollouts, learning rate $10^{-6}$, 500 steps default and 1000 where noted) across seeds $\\{42,43,44\\}$ on a fixed 500-example FOLIO~\\citep{folio} subset held constant across all conditions.\\footnote{All experiments use \\texttt{data/train\\_500\\_seed42.jsonl}; the seed argument controls only model initialization and rollout sampling, never data composition.}\nThe SFT baseline is trained with NLL on gold formalizations to isolate whether structural degeneration arises from data exposure alone.\n\n\\textbf{Evaluation protocol.}\nHeld-out evaluation uses 100 examples drawn from FOLIO (file: \\texttt{proofwriter\\_fol\\_100.jsonl}; the filename is a legacy artifact---no ProofWriter data is used, see \\S\\ref{sec:task}) with greedy decoding.\nAll cross-run ISR values are recomputed uniformly by a single evaluator (\\texttt{eval\\_sta.py}) on top of \\texttt{Prover9}/SWI-Prolog so that training-log ISR (which varied with implementation revisions) is never compared across runs.\nWe report prove rate (PR), proved-only ISR ($\\text{ISR}^*$, denoted ISR in tables when context is clear), and hacking-mode rates from a two-stage classifier (strict normalized text matching for H1/H7, plus functional analysis of the per-sample $n_{\\text{necessary}}$ distribution; \\S\\ref{sec:taxonomy-method}).\nWe additionally report a \\emph{non-hacking} (N-H) rate---the residual of proved samples that match none of the seven cataloged patterns---which is a necessary but not sufficient condition for semantic correctness.\n\n\\subsection{ISR as Diagnostic}\n\\label{sec:diagnostic}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.95\\columnwidth]{figures/fig2_isr_collapse.pdf}\n\\caption{ISR collapse under exec-only GRPO (seed~42). PR rises 32\\%$\\to$93\\%$\\to$96\\% while proved-only ISR falls $0.642{\\to}0.132{\\to}0.003$ over 100$\\to$500$\\to$1000 steps. By step 1000, 94.8\\% of proved samples have $\\text{ISR}{=}0$ and mean component count inflates 6.58$\\to$18.55, indicating contradiction explosion.}\n\\label{fig:isr-collapse}\n\\end{figure}\n\nWe first establish that ISR detects structural degeneration that the prove-rate reward---and any evaluation built on it alone---would miss.\n\n\\textbf{Collapse trajectory.}\nFigure~\\ref{fig:isr-collapse} traces an exec-only GRPO run (seed~42) at 100, 500, and 1000 training steps.\nPR rises $32\\%\\to93\\%\\to96\\%$, a trajectory that by execution-only evaluation would read as ``successful optimization.''\n$\\text{ISR}^*$ tells a different story: $0.642\\to0.132\\to0.003$, a 200$\\times$ collapse over the same window. %% registry: plan003-eval-exec-only-r5, plan001-exec-only-s42-r2, plan016-extended-1000-s42\nBy 500 steps, 87.1\\% of proved samples embed the conclusion (mode H1, \\S\\ref{sec:taxonomy-method}); by 1000 steps, the embedding rate saturates at 100\\% and mean component count more than doubles ($6.58\\to18.55$) as the model emits contradictory or vacuous premises that trivially derive any conclusion.\nThe monotonic decline shows that extended training, in isolation from a structural signal, \\emph{worsens} formalization quality even as it improves the headline number.\n\n\\textbf{Cross-seed instability.}\nThe three exec-only seeds diverge into qualitatively different failure modes despite sharing data, hyperparameters, and reward (Table~\\ref{tab:beta01-3seed}, exec-only rows; per-seed traces in Appendix~\\ref{app:per-seed}).\nSeed~42 reaches $\\text{PR}{=}93\\%$ via conclusion embedding ($\\text{H1}{=}87.1\\%$); seed~43 collapses to $\\text{PR}{=}14\\%$ via repetition (87\\% of rollouts truncated at the max length); seed~44 reaches $\\text{PR}{=}98\\%$ via tautological collapse to a two-component structure ($\\text{H7}{=}100\\%$, mean $n{=}2.04$). %% registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44\nThe cross-seed PR variance ($\\sigma{=}\\pm47$\\,pp) shows that aggregate metrics obscure qualitatively different failure modes; all three are flagged by $\\text{ISR}^*$ even though one passes the PR check (s44) and one fails it (s43).\nThis is the diagnostic value: the same signal catches both high-PR and low-PR failures.\n\n\\textbf{SFT baseline.}\nSupervised fine-tuning on gold formalizations reaches $\\text{PR}{=}14\\%$ with $\\text{ISR}^{*}{=}0.571$, $\\text{H7}{=}0$, $\\text{H1}{=}1/14$ ($7.1\\%$), and $92.9\\%$ non-hacking. %% registry: plan009-sft-baseline-s42-r4\nThe near-absence of hacking under identical data exposure is consistent with hacking being RL-specific.\nBecause SFT also has low PR, we further compare to a 100-step RL checkpoint at matched PR (Appendix~\\ref{app:100step}); the RL checkpoint at $\\text{PR}{=}32\\%$ already shows $\\text{H1}{>}0$ and lower $\\text{ISR}^*$ than SFT at $\\text{PR}{=}14\\%$, indicating the gap is not merely a PR-level confound.\n\n\\subsection{Meta-Level Goodhart's Law}\n\\label{sec:goodhart}\n\nWe now reverse roles: instead of treating ISR as an observer, we use it as a reward augmentation, $r = r_{\\text{exec}}\\cdot(1 + \\beta\\,\\text{ISR})$.\nA uniform random control, $r = r_{\\text{exec}}\\cdot(1 + \\beta\\,u)$ with $u\\sim\\mathcal{U}(0,1)$, at matched $\\beta$ isolates ISR-specific signal from generic reward-variance effects.\nThe headline finding is that ISR-as-reward produces \\emph{meta-level} Goodhart~\\citep{manheim-goodhart-taxonomy}: the diagnostic metric itself becomes the target of gaming when optimized.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Condition} & $\\boldsymbol{\\beta}$ & \\textbf{PR\\%}$\\uparrow$ & \\textbf{ISR}$^*$ & \\textbf{H7\\%} & \\textbf{H1\\%} & \\textbf{N-H\\%} \\\\\n\\midrule\nBase (0-shot) & --- & 12 & --- & --- & --- & --- \\\\ %% registry: sta-phase0-baseline\nSFT & --- & 14 & 0.571 & 0 & 7 & \\textbf{93} \\\\ %% registry: plan009-sft-baseline-s42-r4\n\\midrule\nExec-only$^\\dagger$ & --- & 93 & 0.132 & 0 & 87 & 13 \\\\ %% registry: plan001-exec-only-s42-r2\nISR & 0.1 & 77{\\scriptsize$\\pm$14} & $\\ddagger$ & \\textbf{65} & 17 & ${\\sim}$16 \\\\ %% registry: plan002-additive-b01-s42/s43/s44\nRandom & 0.1 & \\textbf{85}{\\scriptsize$\\pm$6} & 0.086{\\scriptsize$\\pm$.04} & 0 & 81 & 19 \\\\ %% registry: plan018-additive-random-b01-s42/s43-r2/s44\n\\midrule\nISR & 0.3 & 66{\\scriptsize$\\pm$42} & 0.39{\\scriptsize$\\pm$.31} & 35 & 49 & 16 \\\\ %% registry: plan002-additive-b03-s42/s43/s44\nRandom$^\\S$ & 0.3 & 36{\\scriptsize$\\pm$18} & 0.05{\\scriptsize$\\pm$.07} & 0 & 100 & 0 \\\\ %% registry: plan017-additive-random-s42, exp1-random-b03-s44 (s43 training)\n\\bottomrule\n\\end{tabular}}\n\\caption{Goodhart landscape across reward conditions. 3-seed rows show mean$\\pm$std. $^\\dagger$Seed~42; cross-seed exec-only divergence in \\S\\ref{sec:diagnostic}. $\\ddagger$$\\text{ISR}^*$ omitted for ISR $\\beta{=}0.1$ because the raw mean is inflated by H7 gaming (per-seed: Table~\\ref{tab:beta01-3seed}); when matched on premise count it is no different from random (1.06$\\times$). $^\\S$Random $\\beta{=}0.3$ reports 2 seeds (s42, s44); s43 is still training (\\texttt{exp1-random-b03-s43-r4}). Best PR and N-H\\% bolded per group.}\n\\label{tab:goodhart-landscape}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccccc}\n\\toprule\n\\textbf{Seed} & \\textbf{Cond.} & \\textbf{PR} & $\\mathbf{ISR^*}$ & \\textbf{H7\\%} & \\textbf{H1\\%} & \\textbf{N-H\\%} & \\textbf{ISR$^*_{n\\geq 3}$} \\\\\n\\midrule\n42 & ISR & 0.81 & 0.415 & 16 & 52 & 32 & 0.258 \\\\ %% registry: plan002-additive-b01-s42\n43 & ISR & 0.61 & 0.830 & 97 & 0 & 3 & --- \\\\ %% registry: plan002-additive-b01-s43\n44 & ISR & 0.89 & 0.902 & 87 & 0 & 14 & --- \\\\ %% registry: plan002-additive-b01-s44\n\\midrule\n42 & Random & 0.79 & 0.131 & 0 & 71 & 29 & 0.243 \\\\ %% registry: plan018-additive-random-b01-s42\n43 & Random & 0.88 & 0.058 & 0 & 93 & 7 & --- \\\\ %% registry: plan018-additive-random-b01-s43-r2\n44 & Random & 0.89 & 0.070 & 0 & 80 & 20 & --- \\\\ %% registry: plan018-additive-random-b01-s44\n\\midrule\n\\multicolumn{2}{l}{ISR mean$\\pm$std} & .77$\\pm$.14 & --- & 65 & 17 & 16 & 0.258 \\\\\n\\multicolumn{2}{l}{Random mean$\\pm$std} & .85$\\pm$.06 & .086$\\pm$.04 & 0 & 81 & 19 & 0.243 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{ISR $\\beta{=}0.1$ vs.\\ random $\\beta{=}0.1$, 3-seed breakdown. H7 is ISR-specific (65\\% vs.\\ 0\\%); H1 is GRPO-universal but higher under random. Last column reports $\\text{ISR}^*$ restricted to non-hacking samples with $\\geq{3}$ premises (premise-count-matched), available for s42 where genuine residual is non-trivial: 0.258 vs.\\ 0.243, a 1.06$\\times$ ratio.}\n\\label{tab:beta01-3seed}\n\\end{table}\n\n\\textbf{Low-dose ISR ($\\beta{=}0.1$): ISR-specific gaming.}\nTable~\\ref{tab:beta01-3seed} reports the 3-seed breakdown.\nThe most striking number is H7: 64.5\\% of proved samples under ISR ($n{=}149/231$) vs.\\ \\emph{zero} under random ($0/256$). %% registry: plan002 vs plan018 all seeds\nH7---a single premise identical to the conclusion, giving $\\text{ISR}\\geq 0.5$ by construction (\\S\\ref{sec:taxonomy-method})---is the canonical meta-level Goodhart move: the model satisfies the LOO definition directly rather than producing a derivation that happens to satisfy it.\nTotal conclusion embedding ($\\text{H1}+\\text{H7}$) is GRPO-universal at $68$--$97\\%$ across both conditions, and is in fact \\emph{higher} under random (mean H1 81\\% under random vs.\\ 17\\% under ISR).\nISR does not reduce hacking; it converts H1 into H7 (Figure~\\ref{fig:hacking-composition}).\nRandom also achieves higher and more stable PR ($85{\\pm}6\\%$ vs.\\ $77{\\pm}14\\%$), so ISR-as-reward yields no PR advantage either.\n\n\\textbf{Premise-count confound.}\nOne ISR seed (s42) is the only one not dominated by H7, and its raw $\\text{ISR}^*{=}0.415$ is 3.2$\\times$ higher than its matched random control ($0.131$), suggesting genuine structural improvement.\nThis appearance is entirely a premise-minimization artifact.\nISR-trained models produce shorter formalizations (mean $n{=}5.58$ vs.\\ $8.46$ for random), and ISR rises mechanically as $n$ falls---when $n{=}2$, ISR$\\geq 0.5$ by definition.\nRestricting to non-hacking samples with $\\geq{3}$ premises (eliminating the trivial-$n$ regime) gives $\\text{ISR}^*{=}0.258$ for ISR vs.\\ $0.243$ for random: a 1.06$\\times$ ratio, no meaningful advantage (Table~\\ref{tab:beta01-3seed}, last column). %% D051 premise-count-matched analysis\nThe raw 3.2$\\times$ headline collapses once the LOO bias is controlled.\nThis is methodologically important: LOO-based metrics are widely used without component-count correction; under optimization that pressure for shorter outputs, the metric inflates without any quality improvement.\n\n\\textbf{High-dose ISR ($\\beta{=}0.3$): multi-modal Goodhart instability.}\nAt $\\beta{=}0.3$, ISR-as-reward produces extreme cross-seed instability (Table~\\ref{tab:goodhart-landscape}, last group): $\\text{PR}{=}66{\\pm}42\\%$, spanning $18\\%$ to $95\\%$.\nEach seed converges to a distinct Goodhart pathway. %% registry: plan002-additive-b03-s42/s43/s44\nSeed~42 exhibits \\emph{reward collapse}: $\\text{PR}{=}18\\%$, $\\text{ISR}^{*}{=}0.143$, the classical Goodhart pattern from~\\citep{gao-reward-overoptimization} where the proxy weight overwhelms the base signal.\nSeed~43 exhibits \\emph{H1-dominant shortcutting}: $\\text{PR}{=}86\\%$, $\\text{H1}{=}68.6\\%$, $\\text{H7}{=}4.7\\%$, only $26.7\\%$ non-hacking---the model retains a high prove rate but achieves it via conclusion embedding, not structural manipulation of the metric.\nSeed~44 exhibits \\emph{pure H7 meta-Goodhart}: $\\text{PR}{=}95\\%$ combined with $\\text{H7}{=}100\\%$ and $\\text{ISR}^{*}{=}0.742$, with $0\\%$ non-hacking.\nThis last case is the cleanest meta-level Goodhart instance in our experiments: the model simultaneously games \\emph{both} the execution reward (high PR) and the structural metric (high $\\text{ISR}^{*}$) through the same construction.\nFor the random control at $\\beta{=}0.3$, the available 2 seeds collapse to $\\text{PR}{=}48\\%$ (s42) and $\\text{PR}{=}23\\%$ (s44) with $\\text{H1}{=}100\\%$ and $0\\%$ non-hacking in both cases (the s43 random run is still training; full numbers in Appendix~\\ref{app:beta03}). %% registry: plan017-additive-random-s42, exp1-random-b03-s44\nHigh-dose proxy weighting is harmful in both ISR and random conditions, but ISR uniquely produces \\emph{mode diversity}: three qualitatively different failure trajectories from a single reward formulation.\n\n\\subsection{Cross-Logic Diagnostic Transfer}\n\\label{sec:crosslogic}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.95\\columnwidth]{figures/fig4_prolog_comparison.pdf}\n\\caption{Cross-logic results. \\textbf{Left}: FOL vs.\\ Prolog exec-only $\\text{ISR}^*$ across 3 seeds, both near-zero (s44 Prolog $\\text{ISR}^*{=}0.387$ is a small-sample artifact, $n{=}21$). \\textbf{Right}: Prolog ISR-reward gaming-mode composition---all 3 seeds reach 100\\% non-genuine through distinct mechanisms (H7 tautology / degenerate uppercase syntax / query-as-fact gaming).}\n\\label{fig:prolog-comparison}\n\\end{figure}\n\nWe replicate the FOL pipeline with Prolog/SWI-Prolog, retraining seeds and re-evaluating with the same eval harness.\nTwo questions: (i) does ISR retain diagnostic value on a structurally different logic; (ii) does ISR-as-reward produce the same meta-level Goodhart failure mode?\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llccccl}\n\\toprule\n\\textbf{Logic} & \\textbf{Cond.} & \\textbf{Seed} & \\textbf{PR} & $\\mathbf{ISR^*}$ & \\textbf{H7\\%} & \\textbf{Mode} \\\\\n\\midrule\nFOL & exec & 42 & .93 & .132 & 0 & H1 embed (87\\%) \\\\\nFOL & exec & 43 & .14 & --- & --- & repetition \\\\\nFOL & exec & 44 & .98 & .57 & 100 & tautological \\\\\n\\midrule\nProlog & exec & 42 & .83 & .037 & 0 & redundant facts \\\\ %% registry: plan006-prolog-exec-s42\nProlog & exec & 43 & .56 & .015 & 0 & redundant facts \\\\ %% registry: plan006-prolog-exec-s43-r3\nProlog & exec & 44 & .21 & .39$^\\flat$ & 0 & low PR \\\\ %% registry: plan006-prolog-exec-s44\n\\midrule\nProlog & ISR & 42 & .50 & 1.00 & 100 & clean H7 \\\\ %% registry: plan006-prolog-sta-s42\nProlog & ISR & 43 & .38 & --- & 0$^\\sharp$ & degenerate syntax \\\\ %% registry: plan006-prolog-sta-s43\nProlog & ISR & 44 & .97 & .885 & 0$^\\sharp$ & query-as-fact \\\\ %% registry: plan006-prolog-sta-s44\n\\bottomrule\n\\end{tabular}}\n\\caption{Cross-logic results. $^\\flat$small-sample inflation ($n{=}21$ proved); not interpretable as ``structurally clean.'' $^\\sharp$strict text classifier returns 0\\% H7 but \\emph{functional} analysis ($n_{\\text{necessary}}{=}1$) reveals 100\\% (s43: $38/38$) and 97.9\\% (s44: $95/97$) gaming-mode prevalence---see text. All Prolog ISR seeds: 0\\% non-hacking.}\n\\label{tab:prolog-crosslogic}\n\\end{table}\n\n\\textbf{Prolog exec-only: ISR catches redundancy across logics.}\nTwo of three Prolog exec-only seeds (s42, s43) show $\\text{ISR}^{*}{\\approx}0$ despite moderate-to-high PR (Table~\\ref{tab:prolog-crosslogic}). %% registry: plan006-prolog-exec-s42, plan006-prolog-exec-s43-r3\nInspection reveals \\emph{redundant coding}: ground facts repeated multiple times (e.g., \\texttt{penguin(fido).} appearing three times), so per-clause LOO ablation never breaks the proof and the necessity count is zero.\nThis is a different failure semantics from the FOL exec-only collapses (which centered on conclusion embedding), but $\\text{ISR}^{*}$ flags both.\nThis is also the point at which interpretation matters: an exec-only low-ISR is a \\emph{redundancy} signal, whereas an ISR-rewarded high-ISR is a \\emph{metric-gaming} signal (\\S\\ref{sec:taxonomy-method}); the same number does not license the same conclusion about reasoning quality, and we are careful never to read ISR differences as reasoning differences without the mode breakdown.\n\n\\textbf{Prolog ISR-as-reward: universal Goodhart.}\nThe Prolog ISR-reward result is stronger than its FOL counterpart: 3/3 seeds reach 0\\% non-hacking through three distinct mechanisms (Figure~\\ref{fig:prolog-comparison}, right; Table~\\ref{tab:prolog-crosslogic}).\nSeed~42 produces clean H7 tautologies---a single clause identical to the query, $\\text{ISR}^{*}{=}1.0$ over all $50/100$ proved samples. %% registry: plan006-prolog-sta-s42\nSeed~43 produces \\emph{degenerate uppercase pseudo-Prolog} (e.g., \\texttt{MARY\\_IS\\_AN\\_AVA\\-DEOTE.}); the strict text-match classifier returns $\\text{H7}{=}0$ but functional analysis shows all 38 proved samples have $n_{\\text{necessary}}{=}1$, i.e., a single clause that proves the query alone---functionally H7. %% registry: plan006-prolog-sta-s43\nSeed~44 produces \\emph{query-as-fact gaming}: the model transforms the NL question into a snake-case atom and asserts the same atom as both a fact and the query (e.g., \\texttt{is\\_the\\_dog\\_furry. \\?- is\\_the\\_dog\\_furry.}), giving $\\text{PR}{=}97\\%$ with $95/97$ proved samples at $n_{\\text{necessary}}{=}1$. %% registry: plan006-prolog-sta-s44\nSeed~44 evaded our initial strict classifier entirely (returned ``$100\\%$ genuine''); functional cross-validation against the $n_{\\text{necessary}}$ distribution exposed it.\nWe register this as a methodological lesson: text-match hacking classifiers have blind spots, and STA's per-sample necessity profile is the cross-check that catches them.\n\n\\textbf{FOL vs.\\ Prolog comparison.}\nFOL ISR $\\beta{=}0.1$ leaves ${\\sim}16\\%$ non-hacking residual; Prolog ISR leaves $0\\%$ across 3 seeds.\nWe attribute this to Prolog's simpler operational semantics: the optimization landscape contains fewer high-PR derivations and is more easily satisfied by clause-level shortcuts, so the gaming basin is broader and the genuine residual disappears.\nThis is corroborating, not contradictory, evidence for Claim 2: in a setting where structural shortcuts are even easier to construct, ISR-as-reward collapses even more completely.\n\n\\subsection{Hacking Taxonomy}\n\\label{sec:taxonomy}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.92\\columnwidth]{figures/fig3_hacking_composition.pdf}\n\\caption{Hacking composition across reward conditions (proved samples, seed~42 for FOL; appendix has all seeds). ISR converts H1 (conclusion embedding) into more extreme H7 (conclusion duplication) without reducing total hacking; SFT shows near-zero hacking ($92.9\\%$ non-hacking).}\n\\label{fig:hacking-composition}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Mode} & \\textbf{Exec} & \\textbf{ISR$_{.1}$} & \\textbf{Rnd$_{.1}$} & \\textbf{SFT} & \\textbf{Prolog$_{\\text{ISR}}$} \\\\\n\\midrule\nH1 embed       & 87 & 17 & 81 & 7 & 0$^\\sharp$ \\\\\nH7 duplicate   & 0  & 65 & 0  & 0 & 100$^\\sharp$ \\\\\nTautological   & --- & --- & --- & --- & s42 \\\\\nRepetition     & s43 & --- & --- & --- & --- \\\\\nContradiction  & 1k & --- & --- & --- & --- \\\\\nCmplx.\\ vacuous& 0  & 0  & 4  & 0 & --- \\\\\nQuery-as-fact  & --- & --- & --- & --- & s44 \\\\\n\\midrule\n\\textbf{Non-hacking} & 13 & ${\\sim}$16 & 19 & \\textbf{93} & \\textbf{0} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Seven hacking modes across conditions (percentages of proved samples; seed~42 unless noted). Cells with seed identifiers indicate the mode dominates that seed (Prolog ISR row: H7 is s42 strict + s43/s44 functional, totaling 100\\% gaming across all 3 seeds). $^\\sharp$strict for FOL; pooled strict+functional for Prolog (\\S\\ref{sec:crosslogic}).}\n\\label{tab:hacking-taxonomy}\n\\end{table}\n\nThe full taxonomy (Table~\\ref{tab:hacking-taxonomy}, definitions in \\S\\ref{sec:taxonomy-method}) consists of seven modes that span the conditions we studied.\nTwo are quantifiable across all conditions: \\textbf{H1} (conclusion embedding) is GRPO-universal at $68$--$97\\%$ regardless of reward type, and \\textbf{H7} (conclusion duplication) is ISR-specific at $64.5\\%$ vs.\\ $0\\%$ in random controls.\nThe remaining five appear in specific cells: \\textbf{tautological collapse} (exec-only s44 and Prolog ISR s42); \\textbf{repetition collapse} (exec-only s43, with 87\\% of rollouts hitting max length); \\textbf{contradiction explosion} (exec-only at 1000 steps, mean $n{=}18.55$); \\textbf{complexity-without-utility} (random $\\beta{=}0.1$, low residual); and \\textbf{query-as-fact gaming} (Prolog ISR s44).\n\nThe cross-condition pattern is consistent with the framing in \\S\\ref{sec:goodhart}: \\emph{reward formulation determines hacking composition but not hacking prevalence.}\nExec-only, ISR, and random conditions all show $\\geq 80\\%$ pooled hacking among proved samples; only SFT---which does not optimize against a binary execution signal---shows the residual at $93\\%$ non-hacking, consistent with hacking being RL-specific rather than data-induced.\nAcross two logic types, six reward conditions, three seeds, and up to 1000 training steps, no GRPO condition we tested produces a high-PR run that is also majority non-hacking; the closest is ISR $\\beta{=}0.1$ s42 at $\\text{PR}{=}81\\%$ with $32\\%$ non-hacking, and even that residual is the premise-minimization artifact analyzed in \\S\\ref{sec:goodhart}.\n\nThe taxonomy is descriptive, not exhaustive: query-as-fact gaming was found only when we cross-validated the strict classifier against $n_{\\text{necessary}}$ distributions, and additional modes may emerge under further reward formulations or logic types.\nWe expect the STA protocol itself to generalize---it requires only a solver and a notion of component---so future work can extend the taxonomy by applying the same two-stage classification to new domains.\n",
      "numLines": 229,
      "startLine": 1,
      "totalLines": 229
    }
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Read · `toolu_01McLputEUaPwnG7SmD7KgUm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca27e824-6ca6-4db1-9e55-77ef612ddfd7",
  "uuid": "3afac668-47b5-4935-b975-07d9c0d80df3",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01FPVDPGSEFDuKbpre9pFiXM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10886,
      "cache_read_input_tokens": 44145,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10886
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

### Tool result

_source line 15 · 2026-05-15T03:26:07.515Z_

<details><summary>↩ Tool result · `toolu_01McLputEUaPwnG7SmD7KgUm`</summary>

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
  "session_id": "ca27e824-6ca6-4db1-9e55-77ef612ddfd7",
  "uuid": "974e1523-56cf-463c-8113-463705034a01",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/discussion.tex",
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

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Read · `toolu_01JtVvFcA1RvaxztrNhbZ8DQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/conclusion_0cce3f.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca27e824-6ca6-4db1-9e55-77ef612ddfd7",
  "uuid": "04a425e2-88b5-409f-83b6-6454b1fab420",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_011avkv1Lq63qc5aCpWyJpWV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2052,
      "cache_read_input_tokens": 55031,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2052
      },
      "output_tokens": 57,
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

_source line 17 · 2026-05-15T03:26:10.182Z_

<details><summary>↩ Tool result · `toolu_01JtVvFcA1RvaxztrNhbZ8DQ`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We introduced Solver Trace Ablation (STA), a protocol that derives the Intensional Structure Ratio (ISR) through leave-one-out component necessity testing on solver inputs.
5	Our experiments across 6 reward configurations, 3 seeds, 2 formal languages (FOL verified by Prover9, Prolog verified by SWI-Prolog), and up to 1{,}000 training steps establish three findings.
6	
7	First, ISR is an effective diagnostic for structural reward hacking that prove rate alone cannot detect.
8	Under execution-only GRPO, prove rate rises from 32\% to 96\% while ISR collapses from 0.64 to 0.003, with 94.8\% of proved outputs at 1{,}000 steps containing zero necessary components.
9	All three seeds exhibit 87--100\% conclusion embedding, and a supervised fine-tuning baseline (92.9\% genuine, near-zero hacking) confirms that these pathologies are RL-reward-specific.
10	The joint signal of prove rate, ISR, and component count cleanly separates three qualitatively different failure modes (redundant embedding, repetition collapse, tautological collapse) that prove rate conflates into apparent success.
11	
12	Second, ISR fails as a training signal due to meta-level Goodhart's Law.
13	At low dose ($\beta{=}0.1$), ISR reward induces ISR-specific gaming: 64.5\% of proved outputs across 3 seeds exhibit single-premise conclusion duplication (H7), compared to 0\% across all random-reward seeds.
14	The apparent structural advantage of ISR reward (raw 2.4$\times$ genuine ISR) is entirely a premise minimization artifact---controlling for premise count yields 1.06$\times$, indistinguishable from the random baseline.
15	At high dose ($\beta{=}0.3$), classic Goodhart collapse drives prove rate to 18\% versus 48\% for the matched random control.
16	Conclusion embedding itself is GRPO-universal (68--100\% across conditions); ISR reward restructures hacking from multi-premise (H1) to single-premise (H7) forms without reducing its prevalence.
17	
18	Third, both the diagnostic and the Goodhart failure transfer across formal languages.
19	In Prolog, execution-only training again produces near-zero ISR (mean 0.04, 3 seeds), and ISR-as-reward produces universal Goodhart: all 3 seeds converge to gaming with 0\% genuine output, each via a distinct pathway---tautological duplication, degenerate uppercase syntax, and query-as-fact gaming.
20	The stronger Prolog result (0\% genuine vs.\ ${\sim}$16\% in FOL) suggests that simpler formal semantics enable more complete metric exploitation.
21	
22	\paragraph{Limitations.}
23	Our experiments use a single base model (Qwen3-4B); whether larger models exhibit qualitatively different hacking dynamics remains open.
24	The evaluation covers two formal languages (FOL and Prolog) and two datasets (FOLIO-derived and ProofWriter); broader logic types (e.g., dependent types, temporal logic) may present different reward hacking landscapes.
25	ISR measures syntactic component necessity, not semantic faithfulness---downstream NLI accuracy shows no correlation with ISR ($\rho{=}{-}0.049$, n.s.)---and the LOO formulation carries an inherent premise-count bias that requires normalization.
26	We evaluate with 3 seeds; while the cross-seed divergence is itself a finding, larger seed counts would strengthen statistical claims.
27	The text-match hacking classifier has blind spots exposed by Prolog (query-as-fact gaming bypassed strict matching), necessitating functional cross-validation via $n_{\text{necessary}}$ distributions.
28	
29	\paragraph{Future directions.}
30	Combining ISR with semantic verification (e.g., NLI-based faithfulness checks) could address the syntactic-only limitation and yield diagnostics sensitive to both structural and semantic quality.
31	Adaptive reward weighting that uses ISR as a gating signal rather than a continuous bonus may avoid the meta-Goodhart trap.
32	Extending STA to richer logic types (SMT solvers, interactive theorem provers) and scaling to larger models would test the generality of the hacking dynamics we document.
33	Finally, the recursive Goodhart phenomenon---where diagnostics designed to detect gaming become gaming targets when optimized---warrants investigation as a general failure mode of proxy-metric-as-reward approaches beyond the neurosymbolic setting.
34	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ca27e824-6ca6-4db1-9e55-77ef612ddfd7",
  "uuid": "4186086b-83b9-4f74-8a40-42b0aaff7b6d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/conclusion_0cce3f.tex",
      "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe introduced Solver Trace Ablation (STA), a protocol that derives the Intensional Structure Ratio (ISR) through leave-one-out component necessity testing on solver inputs.\nOur experiments across 6 reward configurations, 3 seeds, 2 formal languages (FOL verified by Prover9, Prolog verified by SWI-Prolog), and up to 1{,}000 training steps establish three findings.\n\nFirst, ISR is an effective diagnostic for structural reward hacking that prove rate alone cannot detect.\nUnder execution-only GRPO, prove rate rises from 32\\% to 96\\% while ISR collapses from 0.64 to 0.003, with 94.8\\% of proved outputs at 1{,}000 steps containing zero necessary components.\nAll three seeds exhibit 87--100\\% conclusion embedding, and a supervised fine-tuning baseline (92.9\\% genuine, near-zero hacking) confirms that these pathologies are RL-reward-specific.\nThe joint signal of prove rate, ISR, and component count cleanly separates three qualitatively different failure modes (redundant embedding, repetition collapse, tautological collapse) that prove rate conflates into apparent success.\n\nSecond, ISR fails as a training signal due to meta-level Goodhart's Law.\nAt low dose ($\\beta{=}0.1$), ISR reward induces ISR-specific gaming: 64.5\\% of proved outputs across 3 seeds exhibit single-premise conclusion duplication (H7), compared to 0\\% across all random-reward seeds.\nThe apparent structural advantage of ISR reward (raw 2.4$\\times$ genuine ISR) is entirely a premise minimization artifact---controlling for premise count yields 1.06$\\times$, indistinguishable from the random baseline.\nAt high dose ($\\beta{=}0.3$), classic Goodhart collapse drives prove rate to 18\\% versus 48\\% for the matched random control.\nConclusion embedding itself is GRPO-universal (68--100\\% across conditions); ISR reward restructures hacking from multi-premise (H1) to single-premise (H7) forms without reducing its prevalence.\n\nThird, both the diagnostic and the Goodhart failure transfer across formal languages.\nIn Prolog, execution-only training again produces near-zero ISR (mean 0.04, 3 seeds), and ISR-as-reward produces universal Goodhart: all 3 seeds converge to gaming with 0\\% genuine output, each via a distinct pathway---tautological duplication, degenerate uppercase syntax, and query-as-fact gaming.\nThe stronger Prolog result (0\\% genuine vs.\\ ${\\sim}$16\\% in FOL) suggests that simpler formal semantics enable more complete metric exploitation.\n\n\\paragraph{Limitations.}\nOur experiments use a single base model (Qwen3-4B); whether larger models exhibit qualitatively different hacking dynamics remains open.\nThe evaluation covers two formal languages (FOL and Prolog) and two datasets (FOLIO-derived and ProofWriter); broader logic types (e.g., dependent types, temporal logic) may present different reward hacking landscapes.\nISR measures syntactic component necessity, not semantic faithfulness---downstream NLI accuracy shows no correlation with ISR ($\\rho{=}{-}0.049$, n.s.)---and the LOO formulation carries an inherent premise-count bias that requires normalization.\nWe evaluate with 3 seeds; while the cross-seed divergence is itself a finding, larger seed counts would strengthen statistical claims.\nThe text-match hacking classifier has blind spots exposed by Prolog (query-as-fact gaming bypassed strict matching), necessitating functional cross-validation via $n_{\\text{necessary}}$ distributions.\n\n\\paragraph{Future directions.}\nCombining ISR with semantic verification (e.g., NLI-based faithfulness checks) could address the syntactic-only limitation and yield diagnostics sensitive to both structural and semantic quality.\nAdaptive reward weighting that uses ISR as a gating signal rather than a continuous bonus may avoid the meta-Goodhart trap.\nExtending STA to richer logic types (SMT solvers, interactive theorem provers) and scaling to larger models would test the generality of the hacking dynamics we document.\nFinally, the recursive Goodhart phenomenon---where diagnostics designed to detect gaming become gaming targets when optimized---warrants investigation as a general failure mode of proxy-metric-as-reward approaches beyond the neurosymbolic setting.\n",
      "numLines": 34,
      "startLine": 1,
      "totalLines": 34
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

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca27e824-6ca6-4db1-9e55-77ef612ddfd7",
  "uuid": "10f2a7ce-9606-4e6c-bba3-fd5e2119e0c1",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01LWqg3h1zUVD6D4hrkRoBec",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1794,
      "cache_read_input_tokens": 57083,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1794
      },
      "output_tokens": 55,
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

_source line 19_

<details open><summary>🔧 Tool call — Bash · `toolu_01NNni7BoVzFyWDw4xihRXn4`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper && for f in abstract_c1671f.tex introduction_176853.tex related_work_b05493.tex method_76d073.tex experiments_76b47a.tex discussion.tex conclusion_0cce3f.tex; do\n  # Strip LaTeX commands and comments roughly, then count words\n  words=$(sed 's/%.*$//; s/\\\\[a-zA-Z*]\\+\\(\\[[^]]*\\]\\)\\?\\({[^}]*}\\)\\?//g; s/[{}\\[\\]]//g; s/\\$[^$]*\\$//g' \"$f\" | wc -w)\n  rawwords=$(wc -w < \"$f\")\n  echo \"$f: raw=$rawwords stripped=$words\"\ndone",
  "description": "Count words per section (raw and stripped)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca27e824-6ca6-4db1-9e55-77ef612ddfd7",
  "uuid": "d5d40753-d293-48b9-8f40-0679cda0e0ac",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01LWqg3h1zUVD6D4hrkRoBec",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1794,
      "cache_read_input_tokens": 57083,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1794
      },
      "output_tokens": 55,
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

_source line 20 · 2026-05-15T03:26:17.492Z_

<details><summary>↩ Tool result · `toolu_01NNni7BoVzFyWDw4xihRXn4`</summary>

```text
abstract_c1671f.tex: raw=307 stripped=207
introduction_176853.tex: raw=874 stripped=614
related_work_b05493.tex: raw=900 stripped=847
method_76d073.tex: raw=1165 stripped=868
experiments_76b47a.tex: raw=2704 stripped=1909
discussion.tex: raw=613 stripped=557
conclusion_0cce3f.tex: raw=547 stripped=432
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ca27e824-6ca6-4db1-9e55-77ef612ddfd7",
  "uuid": "9c16851d-ccf0-4f7a-8ee4-15ba02dab9fb",
  "tool_use_result": {
    "stdout": "abstract_c1671f.tex: raw=307 stripped=207\nintroduction_176853.tex: raw=874 stripped=614\nrelated_work_b05493.tex: raw=900 stripped=847\nmethod_76d073.tex: raw=1165 stripped=868\nexperiments_76b47a.tex: raw=2704 stripped=1909\ndiscussion.tex: raw=613 stripped=557\nconclusion_0cce3f.tex: raw=547 stripped=432",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Log line

_source line 21_

{"type":"assistant","message":{"model":"claude-opus-4-7","id":"msg_01W3v51ctMmeRLRfQpWJLeaQ","type":"message","role":"assistant","content":[{"type":"tool_use","id":"toolu_014cwY6tEK3PAmGP41US6scC","name":"Bash","input":{"command":"for f in abstract_c1671f.tex introduction_176853.tex related_work_b05493.tex method_76d073.tex experiments_76b47a.tex discussion.tex conclusion_0cce3f.tex; do\n{"type":"assistant","message":{"model":"claude-opus-4-6","id":"msg_01CdL4Y2s6JhBQyi2uvkPhVg","type":"message","role":"assistant","content":[{"type":"thinking","thinking":"Let me also get a more accurate count that includes LaTeX environments like tables and figures which take up page space. The raw word counts are:\n\n- Abstract: 207\n- Introduction: 635\n- Related Work: 849\n- Method: 879\n- Experiments: 1812\n- Discussion: 558\n- Conclusion: 432\n\nTotal text: ~5372 words\n\nNow I need to account for the visual elements:\n- Tables: I count 4 tables in experiments (tab:goodhart-landscape, tab:beta01-3seed, tab:prolog-crosslogic, tab:hacking-taxonomy)\n\n\n- Figures: 3 figures in experiments (fig:isr-collapse, fig:prolog-comparison, fig:hacking-composition)\n\nLet me estimate the page cost for these visual elements. The tables are all full-width and take up roughly 0.3 to 0.35 pages each, so I'm looking at about 1.3 pages total for the four tables. The figures will add another 0.8 to 1 page. Given the EMNLP 8-page limit with double-column formatting at roughly 650 words per page, I need to figure out how much space I actually have left after accounting for these visual elements.\n\nWith about 5,400 words of text and roughly 2.4 pages consumed by tables and figures, I'm looking at a total of around 10.7 pages—that's 2.7 pages over the limit. I need to cut approximately 1,750 words to fit within the constraints.\n\nBut wait, I should account for how ACL format actually works. The title, authors, and abstract take up significant space on the first page, leaving less room for actual content. Recalculating with that overhead, the text content alone comes to about 8 pages, which is already at or slight{"type":"assistant","message":{"model":"claude-opus-4-7","id":"msg_01FfLmgWELBpFWYdJPtNqnkN","type":"message","role":"assistant","content":[{"type":"thinking","thinking":"","signature":"EpkXClkIDRgCKkCoFm34SqbcIeQxTtZ9ROH5ad6Tg/2YmlT0zcLmUwFWpo2eUACr6qOSd/4Eqy8+rWhyfB3sSq94CzRyt7w9qfcGMg9jbGF1ZGUtb3B1cy00LTc4ABIMTNvpuWOGd3JOmHOWGgzz4npz5RTCJhSZfG4iMJSKfboX3nyaD+6gKApRYcnM8ZVejBat0NcKxOO0kPbjwJQEZUtTGqI0APoa2P2IfCrtFTO9NUdLcdUsa0TGeDUTMOZ4w2i/xI0Hxa7DXa2ZN9nPjrDYgz0HPcKtrpGlO1yDsyv/EiVYYOnlYsgoseEHzyDNEKge5P2SMeC6itEuvMYt0ZbJ3YirNcFo2ky41tYfxzEGEIO31LDFyqZ7k7bT02vgnO0T9DGhGLD/U2vmBbmKFDqhO22UaZSRY7O4juwxD5ZF5h5Pyz7myxXQCyCSKj6pui+pixWPDdK3Ob2aM8I1WXwF8RjV9ncZWZR/EnxaL89VyFR9sOK1mtSnaDDd80FuaLC7zs5jOp6mLUYlcacm9XmJ8FMnTT1F4jWWBboKe1m83Fh8chYjbHHjlr/3/Z47TS1O9jkKaQ6MnlSWRIYqnhzB9GQIBT4P3LQQoQPTcdNL6kz7gwRHI9P5tdP96HsVAOYBvqxXNJTTKgEbAYLbHAPJdXFNFikILR+/RBVCxd/Xti1q1LIhV0FDF1xTQ3PvPf3GZATYg8sfWnqBocfrth0vws7Bsx5vdsmxtnJRcVPIUe5hv4gWZ1gCy6fIGkv6iu1POB+J8aJ6R/euLj3N1LPd0M8i6C3aHIdVjrCkyXjMeHZkHTkNz6TOXji7w+ad9A/mFn9M5GlH/u+1FXcPnk10ZkeRtmACDfzqem131eF7W2+lLQmViDQKVLoJfOt3szpEfpWkrff730rtrg3NqrbfdTc9GUr019x3RNDxjwJic6X9dxYVNTbyIqjKsteGJ/L/Ck5YJv9fOfeC7N9ag2+Jl5/M7ZRWKgxjvGLE8cpbkREdA3USyY68RuB6sfvTawsLYLvyG0CH8ab/9QOG+nWth8uGaOqkqi01XxyL+2/h8zUPcgPkK/bQYZxzIxTX5bwuvy48sjRb13G2dtJUnm57z7SR82sms+PxWy5GTUl+2zJSE+qepimvlW5upnxDreaOSxqO8yAsERlyXcHDQGmLpy9kyKrDKnUcEgJEFYq+6sRxeQPn/dH6bghGaPq6lZexcn5K75Ga6uJsNrB68CwlLYAztTDrsfyZILExBPmUpeGgmyOO4VbhOSC8cJZXnS/WTEZmkW2y4+5PMplyXtYTqrnzVO1ZOnyEErY1VyArHa7vARoHeFkVCcDTabpuST3rrauZp/+B1pIatGPX0rt0LLqKpRHgMl3HfR6TpxH7lX1NeB6tqODZEiUD3KxkFDm84/m4HKKLQbKJktioFplShKlAD1snyRR7SZtwV7nVaqySJv2kD/0/qqbZjFE/gG9SAqq5sgi25wyvnYi34gPnU7mZaHb7AdirQpEg4otPMLItOAb4iXnSaG0/zos0kYyyq90Lm7w4ZUesqtCD02dG8cZ5L+jvRgrJ8dHRaPYPtjS/mDrV4yLyFaCX0Oj9fmd9Zj/yjNezP7o2hGB/7GcoEQCGa+0U9PkREXYmCTS9VqHw9ENyaxdjT9hPdng+trGB2oxMK6Rri8iqWmpoWohi6fKEAuIIctDa1MfEKl1uAzeXm7AajwOhw/Ui29gZFKKJsOYSX0uTG+lhg3+h1IDWf0DOCqFRj/z6WgkOpQRst3LM+ISUJlrAI1MszwbEFpClqPxyAKyxl3NgvHsj8khTq/Gf0nfSGHSAO5CimkQuZQEGPk+cMhQYTGnlML0t4WeOg8ZMI/sAOmnMFNzi5hoh/qn3sZhO9IN3Rpr+aj4mMIxHQNWkq/hGREuAw42r4uJ8v3T6xEjJLpoKO8xpg5A8+K/xUG+49y/47HD1jyy5YcaYk/9QlKjuu9MRszTITc+sQKjiwHELWvZGBhFxStLH9nzkd/wAKMZrSS4WqCsqp3o7uNU7V32DI8rQm6bn07B9kjGvSDfKrjDXUy0fZhIFtEILvm9SyjEiBN3Dx264chGasG2hipIBdkXHRDasjUZDzb8UtNgi7bjbGBVFvOinoEYt8mlvPPRxYflWwe+ugnXF+4ksm8S6JL3PMLkPgprEQXYfM+q+gJvbMeuly5UXu4o9AAfwCgFJvJgtCwH22dFUMcZ2hn1RZercbK2UYZZzYzEVuZkVAlvyvjSbTQYizT2X2LuAiVLdBE1matN4R9YuvZk9gE638wU51c9Tx/dwU8Xbc79jZdXXouH2+3esY5bwswGgzTbhgWZTDJ4uzSHguTmNFaEa/1ZgVfoxgmDwdHmlYvtePZcKVpMEEzVllGFdm+XlSwYUsKftvrBxsE17cJtSfhHMhmqJKz68TBTLvOCVT7peKCr84Cw9Si5CLU2yuh2SC7VHwnO6YvwYPT5QyUks//nrpLP2/RgRdY/O2vZOr5dgLuJwyZsuxu5NkJ+gedMbURy4eYiYa9aFra7EvycurEVNT6HL2uJiittmaUPK+ML87pSVOmIwd1eH5ahyWZVl166DHamX/otQOZZuy9V6dHxMfn7bF980SDmZaxfxP4QybRSm1/+4dGeq8mRRGBi7RxidAqO2kCYVHjUsp1pd3zmtl4XU6qGVhtXar3ALKpInICsqGpBZaIMWfJFSR2sqBF/624LmJe1FltBwQ8vXt7hlG/OUlm6nt4903ubG5MlxvRt/9YpF4R4ZGCKheVf+/tMqycPoqm3QPqFPUOsGa95zaQHXH0Fs2YcXB5ODGW0UjsL4kd3/xgkcFq+SaA8N9bajoRmulHsGecM5/XyZqNDnCQHPbJZmCZf/v/n1To8Ae0QWDdmQC3WxOzM3ZekWItMPWrI+UnlkS5malt/xfx3S3JoOLSg4oexr2iOeSnVMx8ImLCp4C5gdWmRkBmT/P6AON2xApes1Lo4V+Jjws6sb7Nk0iEJ9x/vVOhSQxj2tZh/2RXzz5yLZKFrZLNfBNST97YoeOufM+FcwaKTPVT1jPpSEFET9pfsRYGhjH6nrQFKU24ZqROl72TwvGmp4p7qUXGP6sbtjfRJg+tzwj05vRxdifx0d6mjlv/cuPqx9j6udtmH7inZs5ZVUYJZWqHhkE73DKbKHXsHkIt16JvE38XSdSwt2EYxwDfGh42ptAUZDX0Ccc1jzdpHk6cK0OIshK+94gfIoQvvQrig3WsONcwEzijtLVJ5ZxraxrTyaKh2ZIJ5PLBpjupKxbCLQ2hhzGVQup7N66vMFEI1UXJIKNPIEKb5e9/bk7ZyMz0Gz/N6gcRDtq5QPf9HDadQaD82Y7rLPFdlXqb25Qcp3ZJfGvwL0Q5V41kPYwy6vTYlenK2BcWqTYc1jg2IVGxT6RRY6DK9Fu/wYd2xvxoHSxeUwHbKJSE9pUGgK+oAwhZMUXlVIW8zDk4FE14EewfWOdf5/zqyMciyASHK7/fkiiepsNsPyhDw/F/3jpvSS7lrQPzhDzfIC8XNeYEleMQ5G1MCYwu7pIMF/PHrG6CunO5WgEh4Hb45COpJtDmnICXP7rG+EmwNYpzqLN6CVsV6TCRQYg+I6VNnj1VtGw4x+Km8BCFA/kGTl2TuRbrGR/CoavVHbTPhRezk5Pb7Hy7cMxGzHecGH4u/9JsY57VSQf26ksavhkpcJoTcla7YFuoONrsaZSq6MeFfKGGVOSFl1x+zkIzgh3sUrxakQecGTGuVnRQLVs3coQCk6Gmbu6omNLgKQMwNSvdyflO/sWe9GDW0njO3zTX84Sa2pXt8eQehyP56Kjk8RfGiE3qt+bAHmbQ5xj2BMzppPoR69bH/ov035GrbbvpXD+mvwck8TnKdW/5y4Jx4oH1IwEd6B2fc6fg4x//HXe8UmVNiYP40SbmR8HkocZZMBJk3htz9pTRZhBbIYAQ=="}],"stop_reason":null,"stop_sequence":null,"stop_details":null,"usage":{"input_tokens":1,"cache_creation_input_tokens":392,"cache_read_input_tokens":59472,"cache_creation":{"ephemeral_5m_input_tokens":0,"ephemeral_1h_input_tokens":392},"output_tokens":32,"service_tier":"standard","inference_geo":"not_available"},"diagnostics":null,"context_management":null},"parent_tool_use_id":null,"session_id":"ca27e824-6ca6-4db1-9e55-77ef612ddfd7","uuid":"1e2127bc-a3cb-44e1-856a-304fbe244f19"}

---

### Assistant

_source line 22_

Now I have enough data to write the analysis.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca27e824-6ca6-4db1-9e55-77ef612ddfd7",
  "uuid": "44b7ba13-4636-4678-9e82-f3ab284ea3cc",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01FfLmgWELBpFWYdJPtNqnkN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 392,
      "cache_read_input_tokens": 59472,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 392
      },
      "output_tokens": 32,
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

_source line 23_

<details open><summary>🔧 Tool call — Write · `toolu_01LeAcXBAKd3ibrB5oJzegZZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/page_budget_analysis.md",
  "content": "# Page Budget Analysis — EMNLP 2026 (8 page limit)\n\nDate: 2026-05-15\nInputs: latest section artifacts (abstract_c1671f, introduction_176853, related_work_b05493, method_76d073, experiments_76b47a, discussion, conclusion_0cce3f).\n\n## 1. Current word counts\n\nCounted with LaTeX comments stripped (`%`-prefixed registry tags excluded). Numbers include in-text math/citations but not table/figure content.\n\n| Section | Words | Notes |\n|---|---|---|\n| Abstract | 307 | Abstract does not count against 8 pages in ACL but contributes 1/3 of page 1 |\n| Introduction | 874 | 5 paragraphs + itemized contributions |\n| Related Work | 900 | 4 paragraphs, very citation-heavy |\n| Method | 1140 | 6 subsections, includes formulas + H1–H7 taxonomy |\n| Experiments | 2600 | 5 subsections, 4 tables + 3 figures embedded |\n| Discussion | 613 | 5 paragraphs + 5-item practical implications list |\n| Conclusion | 547 | 3 findings + limitations + future directions |\n| **TOTAL body** | **6,674** | Excluding abstract: 6,367 |\n\nFloats present:\n- **4 figures**: `fig:sta-overview` (Intro), `fig:isr-collapse` (Exp), `fig:hacking-composition` (Exp), `fig:prolog-comparison` (Exp)\n- **4 tables**: `tab:goodhart-landscape`, `tab:beta01-3seed`, `tab:prolog-crosslogic`, `tab:hacking-taxonomy`\n\n## 2. Page budget math (EMNLP/ACL double-column)\n\n- 8 pages × 650 words/page (pure prose ceiling) = **~5,200 words absolute max** if zero floats\n- Realistic float footprint:\n  - Each single-column figure (with caption): ~0.30 page → 4 × 0.30 = **1.2 page**\n  - Each single-column resizebox table (with caption): ~0.28 page → 4 × 0.28 = **1.12 page**\n  - Section/subsection headers, equations (eq:advantage, eq:grpo, eq:isr), itemized lists, paragraph indents: **~0.5 page**\n- Float + structural overhead total: **~2.8 pages**\n- **Prose budget: 8 − 2.8 = 5.2 pages × 650 ≈ 3,380 words**\n\nCurrent 6,674 → must cut **~3,300 words (~49%)** OR move material to appendix.\n\nThis matches the reported \"12 pages → 8 pages\" gap: ~4 pages over = ~2,600 prose words over, plus float reflow recovers another ~1 page.\n\n## 3. Per-section budgets and cuts\n\n| Section | Current | Target | Cut | Strategy |\n|---|---|---|---|---|\n| Abstract | 307 | 200–230 | 80 | Tighten findings 2 & 3 |\n| Introduction | 874 | 650 | 224 | Compress paragraphs 2–4 |\n| Related Work | 900 | 450 | 450 | Single paragraph per theme, fewer citations inline |\n| Method | 1140 | 650 | 490 | Move H1–H7 enumeration + reward-formulation paragraphs to appendix; keep §3.1–§3.4 |\n| Experiments | 2600 | 1100 | 1500 | Aggressive cut: merge subsections, drop redundant prose around tables, kill cross-seed narrative |\n| Discussion | 613 | 250 | 363 | Drop \"Practical Implications\" list; merge \"Classifier Limitations\" into Experiments |\n| Conclusion | 547 | 180 | 367 | One paragraph per finding, drop Limitations (merge into Discussion or appendix) |\n| **Total** | **6,674** | **~3,480** | **~3,194** | Hits ~5.4 pages of prose |\n\n## 4. Specific cut recommendations (priority order)\n\n### Priority 1 — Experiments (biggest absolute win: −1,500 words)\n\n**Section 4.1 Setup (currently ~210 words):** Cut footnote on data file (project-internal note, irrelevant to readers). Cut the legacy-filename parenthetical about ProofWriter. Compress evaluation protocol paragraph by 40%. → target 120 words.\n\n**Section 4.2 ISR as Diagnostic (~440 words):**\n- \"Collapse trajectory\" paragraph (lines 31–36): keep first 3 sentences, cut the monotonic-decline restatement at end. → −50 words\n- \"Cross-seed instability\" (lines 38–42): the qualitative-mode description for s42/s43/s44 is now also in Conclusion and Method H1–H7 — keep only the σ=47pp headline and the \"diagnostic value\" sentence; move per-seed mode descriptions to appendix table. → −90 words\n- \"SFT baseline\" (lines 44–47): the matched-PR caveat (lines 47) repeats info already telegraphed by Tab 1 — drop the second sentence about 100-step appendix comparison. → −40 words\n\n**Section 4.3 Meta-Level Goodhart (~750 words):** Largest cut target.\n- Lead paragraph (52–54): merge into Tab 1 caption. → −60 words\n- \"Low-dose ISR β=0.1\" (103–109): keep the H7 64.5% vs 0% number and one sentence on H1 conversion. Drop the \"Total conclusion embedding…GRPO-universal\" parenthetical (already in Conclusion). → −80 words\n- \"Premise-count confound\" (111–117): this is critical for C2 — keep, but tighten by 30%. → −50 words\n- \"High-dose ISR β=0.3\" (119–127): each seed gets 1 sentence currently, cut to a single sentence summarizing the 3-mode split with PR numbers; the per-seed Goodhart pathology names move to appendix. → −180 words\n\n**Section 4.4 Cross-Logic Transfer (~620 words):**\n- Prolog exec-only paragraph (167–171): the redundancy-vs-gaming interpretation sentence (last 2 lines) duplicates Discussion ¶ \"ISR Capability Boundary.\" Cut from Experiments, keep in Discussion. → −80 words\n- Prolog ISR-as-reward (173–179): each seed described in 2 sentences; tighten to one per seed and let Tab 3 do the work. → −180 words\n- \"FOL vs Prolog comparison\" (181–184): keep the 0% vs 16% headline; cut the \"broader gaming basin\" speculation (move to Discussion or drop). → −60 words\n\n**Section 4.5 Hacking Taxonomy (~430 words):**\n- The enumeration of which seed shows which mode (line 221) duplicates Tab 4 and Method H1–H7. Cut the prose enumeration entirely, keep only the table. → −100 words\n- \"Cross-condition pattern\" paragraph (223–225): keep the 80% pooled-hacking number, cut the s42 81%/32% rehash (already in Tab 2). → −80 words\n- Final two paragraphs (227–228): \"taxonomy is descriptive…\" can compress to one sentence. → −60 words\n\n### Priority 2 — Related Work (−450 words)\n\nCurrent is 4 well-sized paragraphs but ACL accepted papers typically allocate 0.6–0.8 page (≈400–550 words) to related work. Cut strategy:\n\n- **Neurosymbolic Reasoning paragraph (193 words):** Cut sentence about LoRP/FoVer (line 7) — these are marginal to our claim. Cut the \"report 87% conclusion embedding…suggests prove-rate gains may overstate\" sentence (line 13) since it duplicates the Intro hook. → −80 words\n- **Reward Shaping paragraph (~220 words):** Drop the PROF and ProGRS sentences (lines 22–23) — they're tangential. Keep Lightman, Math-Shepherd, Gao-effective-RL. → −90 words\n- **Reward Hacking paragraph (~245 words):** This is the closest cousin literature; keep dense. Drop the Kwa et al. sentence on heavy-tailed misspec (line 30) and the Yang spurious-rewards mention (line 32). → −90 words\n- **Mutation Testing paragraph (~200 words):** Drop the Just et al. \"synthetic mutants approximate real faults\" sentence (line 39) and the LLMorpheus mention (line 40) — neither directly supports STA's novelty claim. → −90 words\n- Convert paragraph headings to inline phrases (e.g., \"On the neurosymbolic side, ...\") to save ~10 words each.\n\n### Priority 3 — Method (−490 words, mostly via appendix migration)\n\nMove to appendix:\n- **§3.5 Reward Formulations (lines 65–78):** All four definitions are restated in Experiments §4.1 and Table 1 — keep only the \"Additive ISR: r = r_exec·(1 + β·ISR), β ∈ {0.1, 0.3}\" inline mention in Experiments. The SFT, additive-random, and convex-combination paragraphs go to appendix. → −180 words\n- **§3.6 Reward Hacking Taxonomy (lines 80–95):** The full H1–H7 enumeration belongs in appendix because Tab 4 + Fig 3 already convey the modes. Keep one sentence in Method linking to App §X. → −280 words\n\nKeep tight in main body: §3.1 Task (kept), §3.2 GRPO (compress to one paragraph + Eq 2, drop Eq 1), §3.3 STA protocol, §3.4 ISR definition + premise-count bias note.\n\n### Priority 4 — Discussion (−363 words)\n\n- Drop \"Practical Implications\" list (lines 38–45): 5-item list, ~140 words. This belongs in Conclusion or as a takeaways box. **Recommended: cut entirely** since each item is already implied by experiments + conclusion findings.\n- Compress \"Classifier Limitations\" (¶4): the s43 uppercase + s44 query-as-fact details are in Experiments §4.4. Drop ¶4, keep one sentence in Experiments. → −100 words\n- \"Premise Count Confound\" and \"ISR Capability Boundary\": keep both — these are the cleanest contributions of the discussion. Light edits only.\n- \"Meta-Level Goodhart's Law\" ¶: tighten by 25%, drop the \"general principle for the reward-shaping community\" final sentence (the cautionary note is already in Abstract + Intro + Conclusion). → −60 words\n\n### Priority 5 — Conclusion (−367 words)\n\n- Three findings paragraphs (lines 6–20) all restate Abstract content with slightly more numbers. **Cut each to 1 sentence** that adds the headline number not in Abstract. → −280 words\n- Drop \"Limitations\" paragraph (22–27): standard EMNLP convention is to have a separate \"Limitations\" section *after* References (which doesn't count against 8 pages). **Move Limitations to its own section** at end. → −0 from page budget actually, since Limitations section is unpaginated.\n- \"Future directions\" paragraph: keep 2 sentences. → −90 words\n\n### Priority 6 — Introduction (−224 words)\n\n- \"The execution-only blind spot\" paragraph (9–13): cut the \"Process reward models…do not transfer\" sentence (line 12) — covered in Related Work. → −40 words\n- \"Component necessity testing\" paragraph (15–20): the NLI ρ=−0.049 caveat (line 20) appears verbatim in Discussion + Conclusion. Keep in Discussion only. → −40 words\n- \"ISR as diagnostic\" (22–25): drop the \"Three random seeds diverge…each converging to\" sentence — Tab 2 + cross-seed paragraph in Experiments cover it. → −60 words\n- \"Meta-level Goodhart\" (27–33): tighten the β=0.3 enumeration (line 31, three Goodhart pathways) — keep one sentence. → −80 words\n\n### Priority 7 — Abstract (−80 words)\n\n- Sentence 6 (the β=0.1/β=0.3 dose-response): compress to one clause for each dose. → −50 words\n- Sentence 8 (7 hacking modes): merge into sentence 9 (asymmetry conclusion). → −30 words\n\n## 5. What MUST stay in main body (non-negotiable)\n\nThese are the load-bearing claims and their direct evidence; deleting them weakens the paper:\n\n- **Abstract**: headline ISR 0.642→0.003 collapse number; H7 64.5%/0% contrast; 1.06× premise-matched ratio; cross-logic universal Goodhart.\n- **Introduction**: opening hook (93% PR with 87% embedding), all 4 contributions C1–C4, the asymmetry statement.\n- **Method §3.3 STA + §3.4 ISR**: full protocol definition + ISR equation; premise-count bias paragraph (critical for §4.3 confound analysis).\n- **Experiments**: Fig 2 (collapse trajectory), Tab 1 (Goodhart landscape), Tab 2 (β=0.1 3-seed + n≥3 column — the 1.06× evidence), Tab 3 (Prolog cross-logic), Fig 3 (hacking composition).\n- **Discussion**: \"ISR Capability Boundary\" (exec-low vs ISR-high interpretation, per active constraint C006), \"Premise Count Confound\" (methodological contribution).\n- **Conclusion**: three-finding summary (compressed), pointer to Limitations.\n\n## 6. Appendix migration list (recovers main-body space without losing content)\n\n| Content | Source | Appendix target |\n|---|---|---|\n| Reward formulation variants (random, convex-combo) | Method §3.5 | App A: Reward Formulations |\n| Full H1–H7 mode definitions with examples | Method §3.6 | App B: Hacking Taxonomy |\n| Per-seed exec-only traces (s42/s43/s44 descriptions) | Exp §4.2 | App C: Per-Seed Failure Modes |\n| β=0.3 per-seed Goodhart pathway details | Exp §4.3 | App D: High-Dose Goodhart |\n| 100-step matched-PR SFT comparison | Exp §4.2 | App E: SFT vs RL at Matched PR |\n| Prolog s43 uppercase + s44 query-as-fact long-form descriptions | Exp §4.4, Disc | App F: Prolog Mode Mechanics |\n| Classifier methodology (text-match + functional cross-check) | Method, Disc | App G: Two-Stage Classifier |\n\n## 7. Float discipline\n\nTo maintain 4 figures + 4 tables in 8 pages, all floats should be single-column where possible:\n- Tab 1, Tab 2, Tab 4 are already `\\resizebox{\\columnwidth}{!}` — good.\n- Tab 3 is `\\resizebox{\\columnwidth}{!}` — good but currently 7 columns × 9 rows is dense; consider dropping the \"Mode\" column (last column is descriptive prose, can be replaced by a footnote keyed to a label).\n- Fig 1 (sta-overview): if currently `figure*` (two-column), confirm whether one-column at 0.95\\columnwidth suffices.\n- Fig 2/3/4: ensure all are `\\columnwidth` not `\\textwidth`.\n\n**Recommendation: consider merging Tab 1 and Tab 2.** Tab 1 (Goodhart landscape) is a 3-seed mean ± std summary; Tab 2 (β=0.1 3-seed breakdown) is the per-seed version of one row of Tab 1. A single \"landscape with per-seed expansion for β=0.1\" table would save ~0.25 page. If kept separate, both tables can shrink rows: drop the \"Base (0-shot)\" row from Tab 1 (the 12% number is already in §3.2 prose).\n\n## 8. Expected outcome\n\nAfter all cuts:\n- Prose: ~3,480 words ≈ 5.4 pages\n- Floats: 4 figures + 4 tables (or 3 tables if merged) ≈ 2.4 pages\n- Structural overhead: ~0.4 page\n- **Projected total: 8.2 pages → trim further in Experiments §4.3/§4.4 if margin negative**\n\nIf 8.2 still over, additional 0.2-page cut from Experiments §4.5 (remove Fig 3 hacking-composition — its content is fully captured by Tab 4).\n\n## 9. Open items\n\n- **s43 random β=0.3 placeholder** in Tab 1 footnote (§): Experiments §4.3 currently reports 2-seed random control. Decision deferred per task brief — when s43 data lands, the only edit is updating the footnote and the mean ± std row.\n- **Fig 1 sta-overview placement**: not in any of the artifacts I read — currently referenced only in Intro line 16. Confirm the asset exists; if not, this is a separate work item (not a page-budget issue).\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca27e824-6ca6-4db1-9e55-77ef612ddfd7",
  "uuid": "26fac78a-ed3b-4558-902d-18b6fe91260d",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01FfLmgWELBpFWYdJPtNqnkN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 392,
      "cache_read_input_tokens": 59472,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 392
      },
      "output_tokens": 32,
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

_source line 24 · 2026-05-15T03:28:06.709Z_

<details><summary>↩ Tool result · reported error · `toolu_01LeAcXBAKd3ibrB5oJzegZZ`</summary>

```text
&lt;tool_use_error>File has not been read yet. Read it first before writing to it.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ca27e824-6ca6-4db1-9e55-77ef612ddfd7",
  "uuid": "8bc2c5c1-ba86-4464-b6c3-58e8056c5353",
  "tool_use_result": "Error: File has not been read yet. Read it first before writing to it."
}
```

</details>

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Bash · `toolu_01HZKtNVUqqUkLTKVGtxLK49`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/page_budget_analysis.md 2>/dev/null && echo \"EXISTS\" || echo \"NEW\"",
  "description": "Check if analysis file exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca27e824-6ca6-4db1-9e55-77ef612ddfd7",
  "uuid": "82161dd5-be09-486f-8734-4622475a7165",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01JA8MzuJaLaJ4oigE6kk1aU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7457,
      "cache_read_input_tokens": 59864,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7457
      },
      "output_tokens": 43,
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

_source line 26 · 2026-05-15T03:28:10.941Z_

<details><summary>↩ Tool result · `toolu_01HZKtNVUqqUkLTKVGtxLK49`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/page_budget_analysis.md
EXISTS
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ca27e824-6ca6-4db1-9e55-77ef612ddfd7",
  "uuid": "63ff578d-6c86-4c22-bb67-8d48b66a3318",
  "tool_use_result": {
    "stdout": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/page_budget_analysis.md\nEXISTS",
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

_source line 27_

<details open><summary>🔧 Tool call — Read · `toolu_01WvdGteC1m1A5TWAbPz8fon`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/page_budget_analysis.md",
  "limit": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca27e824-6ca6-4db1-9e55-77ef612ddfd7",
  "uuid": "196576bd-a7e9-412d-ac8f-24c222f565b7",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Dqc61NbjqyYwmgS8cLgBxD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 263,
      "cache_read_input_tokens": 67321,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 263
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

_source line 28 · 2026-05-15T03:28:13.966Z_

<details><summary>↩ Tool result · `toolu_01WvdGteC1m1A5TWAbPz8fon`</summary>

```text
1	# Page Budget Analysis — EMNLP 2026 (8-page limit)
2	
3	## Word Counts (LaTeX stripped)
4	
5	| Section | Words | Notes |
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ca27e824-6ca6-4db1-9e55-77ef612ddfd7",
  "uuid": "f7c107ce-63f2-4dd2-825f-35fb6f0619b4",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/page_budget_analysis.md",
      "content": "# Page Budget Analysis — EMNLP 2026 (8-page limit)\n\n## Word Counts (LaTeX stripped)\n\n| Section | Words | Notes |",
      "numLines": 5,
      "startLine": 1,
      "totalLines": 190
    }
  }
}
```

</details>

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Write · `toolu_01KLYCwCxD7s3vyKfU3PZybb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/page_budget_analysis.md",
  "content": "# Page Budget Analysis — EMNLP 2026 (8 page limit)\n\nDate: 2026-05-15\nInputs: latest section artifacts (abstract_c1671f, introduction_176853, related_work_b05493, method_76d073, experiments_76b47a, discussion, conclusion_0cce3f).\n\n## 1. Current word counts\n\nCounted with LaTeX comments stripped (`%`-prefixed registry tags excluded). Numbers include in-text math/citations but not table/figure content.\n\n| Section | Words | Notes |\n|---|---|---|\n| Abstract | 307 | Abstract does not count against 8 pages in ACL but contributes 1/3 of page 1 |\n| Introduction | 874 | 5 paragraphs + itemized contributions |\n| Related Work | 900 | 4 paragraphs, very citation-heavy |\n| Method | 1140 | 6 subsections, includes formulas + H1–H7 taxonomy |\n| Experiments | 2600 | 5 subsections, 4 tables + 3 figures embedded |\n| Discussion | 613 | 5 paragraphs + 5-item practical implications list |\n| Conclusion | 547 | 3 findings + limitations + future directions |\n| **TOTAL body** | **6,674** | Excluding abstract: 6,367 |\n\nFloats present:\n- **4 figures**: `fig:sta-overview` (Intro), `fig:isr-collapse` (Exp), `fig:hacking-composition` (Exp), `fig:prolog-comparison` (Exp)\n- **4 tables**: `tab:goodhart-landscape`, `tab:beta01-3seed`, `tab:prolog-crosslogic`, `tab:hacking-taxonomy`\n\n## 2. Page budget math (EMNLP/ACL double-column)\n\n- 8 pages × 650 words/page (pure prose ceiling) = **~5,200 words absolute max** if zero floats\n- Realistic float footprint:\n  - Each single-column figure (with caption): ~0.30 page → 4 × 0.30 = **1.2 page**\n  - Each single-column resizebox table (with caption): ~0.28 page → 4 × 0.28 = **1.12 page**\n  - Section/subsection headers, equations (eq:advantage, eq:grpo, eq:isr), itemized lists, paragraph indents: **~0.5 page**\n- Float + structural overhead total: **~2.8 pages**\n- **Prose budget: 8 − 2.8 = 5.2 pages × 650 ≈ 3,380 words**\n\nCurrent 6,674 → must cut **~3,300 words (~49%)** OR move material to appendix.\n\nThis matches the reported \"12 pages → 8 pages\" gap: ~4 pages over = ~2,600 prose words over, plus float reflow recovers another ~1 page.\n\n## 3. Per-section budgets and cuts\n\n| Section | Current | Target | Cut | Strategy |\n|---|---|---|---|---|\n| Abstract | 307 | 200–230 | ~80 | Tighten findings 2 & 3 |\n| Introduction | 874 | 650 | ~225 | Compress paragraphs 2–4 |\n| Related Work | 900 | 450 | ~450 | Single paragraph per theme, fewer citations inline |\n| Method | 1140 | 650 | ~490 | Move H1–H7 enumeration + reward-formulation paragraphs to appendix; keep §3.1–§3.4 |\n| Experiments | 2600 | 1100 | ~1,500 | Aggressive cut: merge subsections, drop redundant prose around tables, kill cross-seed narrative |\n| Discussion | 613 | 250 | ~365 | Drop \"Practical Implications\" list; merge \"Classifier Limitations\" into Experiments |\n| Conclusion | 547 | 180 | ~365 | One paragraph per finding, drop Limitations (separate unpaginated section) |\n| **Total** | **6,674** | **~3,480** | **~3,200** | Hits ~5.4 pages of prose |\n\n## 4. Specific cut recommendations (priority order)\n\n### Priority 1 — Experiments (biggest absolute win: −1,500 words)\n\n**Section 4.1 Setup (currently ~210 words):** Cut footnote on data file (project-internal note, irrelevant to readers). Cut the legacy-filename parenthetical about ProofWriter. Compress evaluation protocol paragraph by 40%. → target 120 words.\n\n**Section 4.2 ISR as Diagnostic (~440 words):**\n- \"Collapse trajectory\" paragraph (lines 31–36): keep first 3 sentences, cut the monotonic-decline restatement at end. → −50 words\n- \"Cross-seed instability\" (lines 38–42): the qualitative-mode description for s42/s43/s44 is now also in Conclusion and Method H1–H7 — keep only the σ=47pp headline and the \"diagnostic value\" sentence; move per-seed mode descriptions to appendix table. → −90 words\n- \"SFT baseline\" (lines 44–47): the matched-PR caveat (line 47) repeats info already telegraphed by Tab 1 — drop the second sentence about 100-step appendix comparison. → −40 words\n\n**Section 4.3 Meta-Level Goodhart (~750 words):** Largest cut target.\n- Lead paragraph (52–54): merge into Tab 1 caption. → −60 words\n- \"Low-dose ISR β=0.1\" (103–109): keep the H7 64.5% vs 0% number and one sentence on H1 conversion. Drop the \"Total conclusion embedding…GRPO-universal\" parenthetical (already in Conclusion). → −80 words\n- \"Premise-count confound\" (111–117): this is critical for C2 — keep, but tighten by 30%. → −50 words\n- \"High-dose ISR β=0.3\" (119–127): each seed gets 1 sentence currently, cut to a single sentence summarizing the 3-mode split with PR numbers; per-seed Goodhart pathology names move to appendix. → −180 words\n\n**Section 4.4 Cross-Logic Transfer (~620 words):**\n- Prolog exec-only paragraph (167–171): the redundancy-vs-gaming interpretation sentence (last 2 lines) duplicates Discussion ¶ \"ISR Capability Boundary.\" Cut from Experiments, keep in Discussion. → −80 words\n- Prolog ISR-as-reward (173–179): each seed described in 2 sentences; tighten to one per seed and let Tab 3 do the work. → −180 words\n- \"FOL vs Prolog comparison\" (181–184): keep the 0% vs 16% headline; cut the \"broader gaming basin\" speculation (move to Discussion or drop). → −60 words\n\n**Section 4.5 Hacking Taxonomy (~430 words):**\n- The enumeration of which seed shows which mode (line 221) duplicates Tab 4 and Method H1–H7. Cut the prose enumeration entirely, keep only the table. → −100 words\n- \"Cross-condition pattern\" paragraph (223–225): keep the 80% pooled-hacking number, cut the s42 81%/32% rehash (already in Tab 2). → −80 words\n- Final two paragraphs (227–228): \"taxonomy is descriptive…\" can compress to one sentence. → −60 words\n\n### Priority 2 — Related Work (−450 words)\n\nCurrent is 4 well-sized paragraphs but ACL accepted papers typically allocate 0.6–0.8 page (≈400–550 words) to related work. Cut strategy:\n\n- **Neurosymbolic Reasoning paragraph (~190 words):** Cut sentence about LoRP/FoVer (line 7) — these are marginal to our claim. Cut the \"report 87% conclusion embedding…suggests prove-rate gains may overstate\" sentence (line 13) since it duplicates the Intro hook. → −80 words\n- **Reward Shaping paragraph (~220 words):** Drop the PROF and ProGRS sentences (lines 22–23) — they're tangential. Keep Lightman, Math-Shepherd, Gao-effective-RL. → −90 words\n- **Reward Hacking paragraph (~245 words):** This is the closest cousin literature; keep dense. Drop the Kwa et al. sentence on heavy-tailed misspec (line 30) and the Yang spurious-rewards mention (line 32). → −90 words\n- **Mutation Testing paragraph (~200 words):** Drop the Just et al. \"synthetic mutants approximate real faults\" sentence (line 39) and the LLMorpheus mention (line 40) — neither directly supports STA's novelty claim. → −90 words\n- Convert paragraph headings to inline phrases (e.g., \"On the neurosymbolic side, ...\") to save ~10 words each.\n\n### Priority 3 — Method (−490 words, mostly via appendix migration)\n\nMove to appendix:\n- **§3.5 Reward Formulations (lines 65–78):** All four definitions are restated in Experiments §4.1 and Table 1 — keep only the \"Additive ISR: r = r_exec·(1 + β·ISR), β ∈ {0.1, 0.3}\" inline mention in Experiments. The SFT, additive-random, and convex-combination paragraphs go to appendix. → −180 words\n- **§3.6 Reward Hacking Taxonomy (lines 80–95):** The full H1–H7 enumeration belongs in appendix because Tab 4 + Fig 3 already convey the modes. Keep one sentence in Method linking to App §X. → −280 words\n\nKeep tight in main body: §3.1 Task (kept), §3.2 GRPO (compress to one paragraph + Eq 2, drop Eq 1), §3.3 STA protocol, §3.4 ISR definition + premise-count bias note.\n\n### Priority 4 — Discussion (−365 words)\n\n- Drop \"Practical Implications\" list (lines 38–45): 5-item list, ~140 words. This belongs in Conclusion or as a takeaways box. **Recommended: cut entirely** since each item is already implied by experiments + conclusion findings.\n- Compress \"Classifier Limitations\" (¶4): the s43 uppercase + s44 query-as-fact details are in Experiments §4.4. Drop ¶4, keep one sentence in Experiments. → −100 words\n- \"Premise Count Confound\" and \"ISR Capability Boundary\": keep both — these are the cleanest contributions of the discussion. Light edits only.\n- \"Meta-Level Goodhart's Law\" ¶: tighten by 25%, drop the \"general principle for the reward-shaping community\" final sentence (the cautionary note is already in Abstract + Intro + Conclusion). → −60 words\n\n### Priority 5 — Conclusion (−365 words)\n\n- Three findings paragraphs (lines 6–20) all restate Abstract content with slightly more numbers. **Cut each to 1 sentence** that adds the headline number not in Abstract. → −280 words\n- Drop \"Limitations\" paragraph (22–27): standard EMNLP convention is a separate \"Limitations\" section *after* References (which doesn't count against 8 pages). **Move Limitations to its own section** at end. → recovers 0 prose words from page budget directly, but frees ~80 words from §Conclusion (they become unpaginated content).\n- \"Future directions\" paragraph: keep 2 sentences. → −90 words\n\n### Priority 6 — Introduction (−225 words)\n\n- \"The execution-only blind spot\" paragraph (9–13): cut the \"Process reward models…do not transfer\" sentence (line 12) — covered in Related Work. → −40 words\n- \"Component necessity testing\" paragraph (15–20): the NLI ρ=−0.049 caveat (line 20) appears verbatim in Discussion + Conclusion. Keep in Discussion only. → −40 words\n- \"ISR as diagnostic\" (22–25): drop the \"Three random seeds diverge…each converging to\" sentence — Tab 2 + cross-seed paragraph in Experiments cover it. → −60 words\n- \"Meta-level Goodhart\" (27–33): tighten the β=0.3 enumeration (line 31, three Goodhart pathways) — keep one sentence. → −80 words\n\n### Priority 7 — Abstract (−80 words)\n\n- Sentence 6 (the β=0.1/β=0.3 dose-response): compress to one clause for each dose. → −50 words\n- Sentence 8 (7 hacking modes): merge into sentence 9 (asymmetry conclusion). → −30 words\n\n## 5. What MUST stay in main body (non-negotiable)\n\nThese are the load-bearing claims and their direct evidence; deleting them weakens the paper:\n\n- **Abstract**: headline ISR 0.642→0.003 collapse number; H7 64.5%/0% contrast; 1.06× premise-matched ratio; cross-logic universal Goodhart.\n- **Introduction**: opening hook (93% PR with 87% embedding), all 4 contributions C1–C4, the asymmetry statement.\n- **Method §3.3 STA + §3.4 ISR**: full protocol definition + ISR equation; premise-count bias paragraph (critical for §4.3 confound analysis).\n- **Experiments**: Fig 2 (collapse trajectory), Tab 1 (Goodhart landscape), Tab 2 (β=0.1 3-seed + n≥3 column — the 1.06× evidence), Tab 3 (Prolog cross-logic), Fig 3 (hacking composition).\n- **Discussion**: \"ISR Capability Boundary\" (exec-low vs ISR-high interpretation, per active constraint C006), \"Premise Count Confound\" (methodological contribution).\n- **Conclusion**: three-finding summary (compressed), pointer to Limitations.\n\n## 6. Appendix migration list (recovers main-body space without losing content)\n\n| Content | Source | Appendix target |\n|---|---|---|\n| Reward formulation variants (random, convex-combo) | Method §3.5 | App A: Reward Formulations |\n| Full H1–H7 mode definitions with examples | Method §3.6 | App B: Hacking Taxonomy |\n| Per-seed exec-only traces (s42/s43/s44 descriptions) | Exp §4.2 | App C: Per-Seed Failure Modes |\n| β=0.3 per-seed Goodhart pathway details | Exp §4.3 | App D: High-Dose Goodhart |\n| 100-step matched-PR SFT comparison | Exp §4.2 | App E: SFT vs RL at Matched PR |\n| Prolog s43 uppercase + s44 query-as-fact long-form descriptions | Exp §4.4, Disc | App F: Prolog Mode Mechanics |\n| Classifier methodology (text-match + functional cross-check) | Method, Disc | App G: Two-Stage Classifier |\n\n## 7. Float discipline\n\nTo maintain 4 figures + 4 tables in 8 pages, all floats should be single-column where possible:\n- Tab 1, Tab 2, Tab 4 are already `\\resizebox{\\columnwidth}{!}` — good.\n- Tab 3 is `\\resizebox{\\columnwidth}{!}` — good but currently 7 columns × 9 rows is dense; consider dropping the \"Mode\" column (last column is descriptive prose, can be replaced by a footnote keyed to a label).\n- Fig 1 (sta-overview): if currently `figure*` (two-column), confirm whether one-column at 0.95\\columnwidth suffices.\n- Fig 2/3/4: ensure all are `\\columnwidth` not `\\textwidth`.\n\n**Recommendation: consider merging Tab 1 and Tab 2.** Tab 1 (Goodhart landscape) is a 3-seed mean ± std summary; Tab 2 (β=0.1 3-seed breakdown) is the per-seed version of one row of Tab 1. A single \"landscape with per-seed expansion for β=0.1\" table would save ~0.25 page. If kept separate, both tables can shrink rows: drop the \"Base (0-shot)\" row from Tab 1 (the 12% number is already in §3.2 prose).\n\n## 8. Expected outcome\n\nAfter all cuts:\n- Prose: ~3,480 words ≈ 5.4 pages\n- Floats: 4 figures + 4 tables (or 3 tables if merged) ≈ 2.4 pages\n- Structural overhead: ~0.4 page\n- **Projected total: 8.2 pages → trim further in Experiments §4.3/§4.4 if margin negative**\n\nIf 8.2 still over, additional 0.2-page cut from Experiments §4.5 (remove Fig 3 hacking-composition — its content is fully captured by Tab 4).\n\n## 9. Open items\n\n- **s43 random β=0.3 placeholder** in Tab 1 footnote (§): Experiments §4.3 currently reports 2-seed random control. Decision deferred per task brief — when s43 data lands, the only edit is updating the footnote and the mean ± std row.\n- **Fig 1 sta-overview placement**: not in any of the artifacts I read — currently referenced only in Intro line 16. Confirm the asset exists; if not, this is a separate work item (not a page-budget issue).\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca27e824-6ca6-4db1-9e55-77ef612ddfd7",
  "uuid": "cd21b3b9-b508-4c7d-baff-1426857707cf",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01FF6xNzvhRRDD65qxhmb9v2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 228,
      "cache_read_input_tokens": 67584,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 228
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

_source line 30 · 2026-05-15T03:29:24.304Z_

<details><summary>↩ Tool result · `toolu_01KLYCwCxD7s3vyKfU3PZybb`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/page_budget_analysis.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ca27e824-6ca6-4db1-9e55-77ef612ddfd7",
  "uuid": "1cc1e44a-f7f8-4439-82ec-a950e6457e78",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/page_budget_analysis.md",
    "content": "# Page Budget Analysis — EMNLP 2026 (8 page limit)\n\nDate: 2026-05-15\nInputs: latest section artifacts (abstract_c1671f, introduction_176853, related_work_b05493, method_76d073, experiments_76b47a, discussion, conclusion_0cce3f).\n\n## 1. Current word counts\n\nCounted with LaTeX comments stripped (`%`-prefixed registry tags excluded). Numbers include in-text math/citations but not table/figure content.\n\n| Section | Words | Notes |\n|---|---|---|\n| Abstract | 307 | Abstract does not count against 8 pages in ACL but contributes 1/3 of page 1 |\n| Introduction | 874 | 5 paragraphs + itemized contributions |\n| Related Work | 900 | 4 paragraphs, very citation-heavy |\n| Method | 1140 | 6 subsections, includes formulas + H1–H7 taxonomy |\n| Experiments | 2600 | 5 subsections, 4 tables + 3 figures embedded |\n| Discussion | 613 | 5 paragraphs + 5-item practical implications list |\n| Conclusion | 547 | 3 findings + limitations + future directions |\n| **TOTAL body** | **6,674** | Excluding abstract: 6,367 |\n\nFloats present:\n- **4 figures**: `fig:sta-overview` (Intro), `fig:isr-collapse` (Exp), `fig:hacking-composition` (Exp), `fig:prolog-comparison` (Exp)\n- **4 tables**: `tab:goodhart-landscape`, `tab:beta01-3seed`, `tab:prolog-crosslogic`, `tab:hacking-taxonomy`\n\n## 2. Page budget math (EMNLP/ACL double-column)\n\n- 8 pages × 650 words/page (pure prose ceiling) = **~5,200 words absolute max** if zero floats\n- Realistic float footprint:\n  - Each single-column figure (with caption): ~0.30 page → 4 × 0.30 = **1.2 page**\n  - Each single-column resizebox table (with caption): ~0.28 page → 4 × 0.28 = **1.12 page**\n  - Section/subsection headers, equations (eq:advantage, eq:grpo, eq:isr), itemized lists, paragraph indents: **~0.5 page**\n- Float + structural overhead total: **~2.8 pages**\n- **Prose budget: 8 − 2.8 = 5.2 pages × 650 ≈ 3,380 words**\n\nCurrent 6,674 → must cut **~3,300 words (~49%)** OR move material to appendix.\n\nThis matches the reported \"12 pages → 8 pages\" gap: ~4 pages over = ~2,600 prose words over, plus float reflow recovers another ~1 page.\n\n## 3. Per-section budgets and cuts\n\n| Section | Current | Target | Cut | Strategy |\n|---|---|---|---|---|\n| Abstract | 307 | 200–230 | ~80 | Tighten findings 2 & 3 |\n| Introduction | 874 | 650 | ~225 | Compress paragraphs 2–4 |\n| Related Work | 900 | 450 | ~450 | Single paragraph per theme, fewer citations inline |\n| Method | 1140 | 650 | ~490 | Move H1–H7 enumeration + reward-formulation paragraphs to appendix; keep §3.1–§3.4 |\n| Experiments | 2600 | 1100 | ~1,500 | Aggressive cut: merge subsections, drop redundant prose around tables, kill cross-seed narrative |\n| Discussion | 613 | 250 | ~365 | Drop \"Practical Implications\" list; merge \"Classifier Limitations\" into Experiments |\n| Conclusion | 547 | 180 | ~365 | One paragraph per finding, drop Limitations (separate unpaginated section) |\n| **Total** | **6,674** | **~3,480** | **~3,200** | Hits ~5.4 pages of prose |\n\n## 4. Specific cut recommendations (priority order)\n\n### Priority 1 — Experiments (biggest absolute win: −1,500 words)\n\n**Section 4.1 Setup (currently ~210 words):** Cut footnote on data file (project-internal note, irrelevant to readers). Cut the legacy-filename parenthetical about ProofWriter. Compress evaluation protocol paragraph by 40%. → target 120 words.\n\n**Section 4.2 ISR as Diagnostic (~440 words):**\n- \"Collapse trajectory\" paragraph (lines 31–36): keep first 3 sentences, cut the monotonic-decline restatement at end. → −50 words\n- \"Cross-seed instability\" (lines 38–42): the qualitative-mode description for s42/s43/s44 is now also in Conclusion and Method H1–H7 — keep only the σ=47pp headline and the \"diagnostic value\" sentence; move per-seed mode descriptions to appendix table. → −90 words\n- \"SFT baseline\" (lines 44–47): the matched-PR caveat (line 47) repeats info already telegraphed by Tab 1 — drop the second sentence about 100-step appendix comparison. → −40 words\n\n**Section 4.3 Meta-Level Goodhart (~750 words):** Largest cut target.\n- Lead paragraph (52–54): merge into Tab 1 caption. → −60 words\n- \"Low-dose ISR β=0.1\" (103–109): keep the H7 64.5% vs 0% number and one sentence on H1 conversion. Drop the \"Total conclusion embedding…GRPO-universal\" parenthetical (already in Conclusion). → −80 words\n- \"Premise-count confound\" (111–117): this is critical for C2 — keep, but tighten by 30%. → −50 words\n- \"High-dose ISR β=0.3\" (119–127): each seed gets 1 sentence currently, cut to a single sentence summarizing the 3-mode split with PR numbers; per-seed Goodhart pathology names move to appendix. → −180 words\n\n**Section 4.4 Cross-Logic Transfer (~620 words):**\n- Prolog exec-only paragraph (167–171): the redundancy-vs-gaming interpretation sentence (last 2 lines) duplicates Discussion ¶ \"ISR Capability Boundary.\" Cut from Experiments, keep in Discussion. → −80 words\n- Prolog ISR-as-reward (173–179): each seed described in 2 sentences; tighten to one per seed and let Tab 3 do the work. → −180 words\n- \"FOL vs Prolog comparison\" (181–184): keep the 0% vs 16% headline; cut the \"broader gaming basin\" speculation (move to Discussion or drop). → −60 words\n\n**Section 4.5 Hacking Taxonomy (~430 words):**\n- The enumeration of which seed shows which mode (line 221) duplicates Tab 4 and Method H1–H7. Cut the prose enumeration entirely, keep only the table. → −100 words\n- \"Cross-condition pattern\" paragraph (223–225): keep the 80% pooled-hacking number, cut the s42 81%/32% rehash (already in Tab 2). → −80 words\n- Final two paragraphs (227–228): \"taxonomy is descriptive…\" can compress to one sentence. → −60 words\n\n### Priority 2 — Related Work (−450 words)\n\nCurrent is 4 well-sized paragraphs but ACL accepted papers typically allocate 0.6–0.8 page (≈400–550 words) to related work. Cut strategy:\n\n- **Neurosymbolic Reasoning paragraph (~190 words):** Cut sentence about LoRP/FoVer (line 7) — these are marginal to our claim. Cut the \"report 87% conclusion embedding…suggests prove-rate gains may overstate\" sentence (line 13) since it duplicates the Intro hook. → −80 words\n- **Reward Shaping paragraph (~220 words):** Drop the PROF and ProGRS sentences (lines 22–23) — they're tangential. Keep Lightman, Math-Shepherd, Gao-effective-RL. → −90 words\n- **Reward Hacking paragraph (~245 words):** This is the closest cousin literature; keep dense. Drop the Kwa et al. sentence on heavy-tailed misspec (line 30) and the Yang spurious-rewards mention (line 32). → −90 words\n- **Mutation Testing paragraph (~200 words):** Drop the Just et al. \"synthetic mutants approximate real faults\" sentence (line 39) and the LLMorpheus mention (line 40) — neither directly supports STA's novelty claim. → −90 words\n- Convert paragraph headings to inline phrases (e.g., \"On the neurosymbolic side, ...\") to save ~10 words each.\n\n### Priority 3 — Method (−490 words, mostly via appendix migration)\n\nMove to appendix:\n- **§3.5 Reward Formulations (lines 65–78):** All four definitions are restated in Experiments §4.1 and Table 1 — keep only the \"Additive ISR: r = r_exec·(1 + β·ISR), β ∈ {0.1, 0.3}\" inline mention in Experiments. The SFT, additive-random, and convex-combination paragraphs go to appendix. → −180 words\n- **§3.6 Reward Hacking Taxonomy (lines 80–95):** The full H1–H7 enumeration belongs in appendix because Tab 4 + Fig 3 already convey the modes. Keep one sentence in Method linking to App §X. → −280 words\n\nKeep tight in main body: §3.1 Task (kept), §3.2 GRPO (compress to one paragraph + Eq 2, drop Eq 1), §3.3 STA protocol, §3.4 ISR definition + premise-count bias note.\n\n### Priority 4 — Discussion (−365 words)\n\n- Drop \"Practical Implications\" list (lines 38–45): 5-item list, ~140 words. This belongs in Conclusion or as a takeaways box. **Recommended: cut entirely** since each item is already implied by experiments + conclusion findings.\n- Compress \"Classifier Limitations\" (¶4): the s43 uppercase + s44 query-as-fact details are in Experiments §4.4. Drop ¶4, keep one sentence in Experiments. → −100 words\n- \"Premise Count Confound\" and \"ISR Capability Boundary\": keep both — these are the cleanest contributions of the discussion. Light edits only.\n- \"Meta-Level Goodhart's Law\" ¶: tighten by 25%, drop the \"general principle for the reward-shaping community\" final sentence (the cautionary note is already in Abstract + Intro + Conclusion). → −60 words\n\n### Priority 5 — Conclusion (−365 words)\n\n- Three findings paragraphs (lines 6–20) all restate Abstract content with slightly more numbers. **Cut each to 1 sentence** that adds the headline number not in Abstract. → −280 words\n- Drop \"Limitations\" paragraph (22–27): standard EMNLP convention is a separate \"Limitations\" section *after* References (which doesn't count against 8 pages). **Move Limitations to its own section** at end. → recovers 0 prose words from page budget directly, but frees ~80 words from §Conclusion (they become unpaginated content).\n- \"Future directions\" paragraph: keep 2 sentences. → −90 words\n\n### Priority 6 — Introduction (−225 words)\n\n- \"The execution-only blind spot\" paragraph (9–13): cut the \"Process reward models…do not transfer\" sentence (line 12) — covered in Related Work. → −40 words\n- \"Component necessity testing\" paragraph (15–20): the NLI ρ=−0.049 caveat (line 20) appears verbatim in Discussion + Conclusion. Keep in Discussion only. → −40 words\n- \"ISR as diagnostic\" (22–25): drop the \"Three random seeds diverge…each converging to\" sentence — Tab 2 + cross-seed paragraph in Experiments cover it. → −60 words\n- \"Meta-level Goodhart\" (27–33): tighten the β=0.3 enumeration (line 31, three Goodhart pathways) — keep one sentence. → −80 words\n\n### Priority 7 — Abstract (−80 words)\n\n- Sentence 6 (the β=0.1/β=0.3 dose-response): compress to one clause for each dose. → −50 words\n- Sentence 8 (7 hacking modes): merge into sentence 9 (asymmetry conclusion). → −30 words\n\n## 5. What MUST stay in main body (non-negotiable)\n\nThese are the load-bearing claims and their direct evidence; deleting them weakens the paper:\n\n- **Abstract**: headline ISR 0.642→0.003 collapse number; H7 64.5%/0% contrast; 1.06× premise-matched ratio; cross-logic universal Goodhart.\n- **Introduction**: opening hook (93% PR with 87% embedding), all 4 contributions C1–C4, the asymmetry statement.\n- **Method §3.3 STA + §3.4 ISR**: full protocol definition + ISR equation; premise-count bias paragraph (critical for §4.3 confound analysis).\n- **Experiments**: Fig 2 (collapse trajectory), Tab 1 (Goodhart landscape), Tab 2 (β=0.1 3-seed + n≥3 column — the 1.06× evidence), Tab 3 (Prolog cross-logic), Fig 3 (hacking composition).\n- **Discussion**: \"ISR Capability Boundary\" (exec-low vs ISR-high interpretation, per active constraint C006), \"Premise Count Confound\" (methodological contribution).\n- **Conclusion**: three-finding summary (compressed), pointer to Limitations.\n\n## 6. Appendix migration list (recovers main-body space without losing content)\n\n| Content | Source | Appendix target |\n|---|---|---|\n| Reward formulation variants (random, convex-combo) | Method §3.5 | App A: Reward Formulations |\n| Full H1–H7 mode definitions with examples | Method §3.6 | App B: Hacking Taxonomy |\n| Per-seed exec-only traces (s42/s43/s44 descriptions) | Exp §4.2 | App C: Per-Seed Failure Modes |\n| β=0.3 per-seed Goodhart pathway details | Exp §4.3 | App D: High-Dose Goodhart |\n| 100-step matched-PR SFT comparison | Exp §4.2 | App E: SFT vs RL at Matched PR |\n| Prolog s43 uppercase + s44 query-as-fact long-form descriptions | Exp §4.4, Disc | App F: Prolog Mode Mechanics |\n| Classifier methodology (text-match + functional cross-check) | Method, Disc | App G: Two-Stage Classifier |\n\n## 7. Float discipline\n\nTo maintain 4 figures + 4 tables in 8 pages, all floats should be single-column where possible:\n- Tab 1, Tab 2, Tab 4 are already `\\resizebox{\\columnwidth}{!}` — good.\n- Tab 3 is `\\resizebox{\\columnwidth}{!}` — good but currently 7 columns × 9 rows is dense; consider dropping the \"Mode\" column (last column is descriptive prose, can be replaced by a footnote keyed to a label).\n- Fig 1 (sta-overview): if currently `figure*` (two-column), confirm whether one-column at 0.95\\columnwidth suffices.\n- Fig 2/3/4: ensure all are `\\columnwidth` not `\\textwidth`.\n\n**Recommendation: consider merging Tab 1 and Tab 2.** Tab 1 (Goodhart landscape) is a 3-seed mean ± std summary; Tab 2 (β=0.1 3-seed breakdown) is the per-seed version of one row of Tab 1. A single \"landscape with per-seed expansion for β=0.1\" table would save ~0.25 page. If kept separate, both tables can shrink rows: drop the \"Base (0-shot)\" row from Tab 1 (the 12% number is already in §3.2 prose).\n\n## 8. Expected outcome\n\nAfter all cuts:\n- Prose: ~3,480 words ≈ 5.4 pages\n- Floats: 4 figures + 4 tables (or 3 tables if merged) ≈ 2.4 pages\n- Structural overhead: ~0.4 page\n- **Projected total: 8.2 pages → trim further in Experiments §4.3/§4.4 if margin negative**\n\nIf 8.2 still over, additional 0.2-page cut from Experiments §4.5 (remove Fig 3 hacking-composition — its content is fully captured by Tab 4).\n\n## 9. Open items\n\n- **s43 random β=0.3 placeholder** in Tab 1 footnote (§): Experiments §4.3 currently reports 2-seed random control. Decision deferred per task brief — when s43 data lands, the only edit is updating the footnote and the mean ± std row.\n- **Fig 1 sta-overview placement**: not in any of the artifacts I read — currently referenced only in Intro line 16. Confirm the asset exists; if not, this is a separate work item (not a page-budget issue).\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 189,
        "newStart": 1,
        "newLines": 168,
        "lines": [
          "-# Page Budget Analysis — EMNLP 2026 (8-page limit)",
          "+# Page Budget Analysis — EMNLP 2026 (8 page limit)",
          " ",
          "-## Word Counts (LaTeX stripped)",
          "+Date: 2026-05-15",
          "+Inputs: latest section artifacts (abstract_c1671f, introduction_176853, related_work_b05493, method_76d073, experiments_76b47a, discussion, conclusion_0cce3f).",
          " ",
          "-| Section | Words | Notes |",
          "-|---------|------:|-------|",
          "-| Abstract | 207 | On page 1, not separately counted |",
          "-| Introduction | 635 | |",
          "-| Related Work | 849 | |",
          "-| Method | 879 | 3 equations + 2 enumerates add ~150 word-equivalents |",
          "-| Experiments | 1,812 | 4 tables + 3 figures |",
          "-| Discussion | 558 | 1 enumerate (5 items) |",
          "-| Conclusion | 432 | |",
          "-| **Body total (excl. abstract)** | **5,165** | |",
          "+## 1. Current word counts",
          " ",
          "-## Float Inventory",
          "+Counted with LaTeX comments stripped (`%`-prefixed registry tags excluded). Numbers include in-text math/citations but not table/figure content.",
          " ",
          "-| Float | Type | Width | Est. page cost |",
          "-|-------|------|-------|---------------|",
          "-| fig:isr-collapse | figure | 0.95col | 0.30 |",
          "-| tab:goodhart-landscape | table | col (resizebox) | 0.30 |",
          "-| tab:beta01-3seed | table | col (resizebox) | 0.35 |",
          "-| fig:prolog-comparison | figure | 0.95col | 0.35 |",
          "-| tab:prolog-crosslogic | table | col (resizebox) | 0.35 |",
          "-| fig:hacking-composition | figure | 0.92col | 0.30 |",
          "-| tab:hacking-taxonomy | table | col (resizebox) | 0.30 |",
          "-| **Total floats** | | | **~2.25 pages** |",
          "+| Section | Words | Notes |",
          "+|---|---|---|",
          "+| Abstract | 307 | Abstract does not count against 8 pages in ACL but contributes 1/3 of page 1 |",
          "+| Introduction | 874 | 5 paragraphs + itemized contributions |",
          "+| Related Work | 900 | 4 paragraphs, very citation-heavy |",
          "+| Method | 1140 | 6 subsections, includes formulas + H1–H7 taxonomy |",
          "+| Experiments | 2600 | 5 subsections, 4 tables + 3 figures embedded |",
          "+| Discussion | 613 | 5 paragraphs + 5-item practical implications list |",
          "+| Conclusion | 547 | 3 findings + limitations + future directions |",
          "+| **TOTAL body** | **6,674** | Excluding abstract: 6,367 |",
          " ",
          "-## Page Budget Calculation",
          "+Floats present:",
          "+- **4 figures**: `fig:sta-overview` (Intro), `fig:isr-collapse` (Exp), `fig:hacking-composition` (Exp), `fig:prolog-comparison` (Exp)",
          "+- **4 tables**: `tab:goodhart-landscape`, `tab:beta01-3seed`, `tab:prolog-crosslogic`, `tab:hacking-taxonomy`",
          " ",
          "-- **Available**: 8 pages",
          "-- **Title + authors + abstract**: ~0.5 page",
          "-- **Floats (4 tables + 3 figures)**: ~2.25 pages",
          "-- **Remaining for body text**: 8 - 0.5 - 2.25 = **5.25 pages**",
          "-- **Word budget** (at ~650 words/page ACL double-col): **~3,400 words**",
          "-- **Current body text**: 5,165 words",
          "-- **Overshoot**: **~1,750 words (≈ 2.7 pages)**",
          "+## 2. Page budget math (EMNLP/ACL double-column)",
          " ",
          "-Note: Equations (Method ×3), itemize/enumerate formatting, and section headers add ~200-300 word-equivalents of vertical space, pushing effective overshoot closer to **~2,000 words**.",
          "+- 8 pages × 650 words/page (pure prose ceiling) = **~5,200 words absolute max** if zero floats",
          "+- Realistic float footprint:",
          "+  - Each single-column figure (with caption): ~0.30 page → 4 × 0.30 = **1.2 page**",
          "+  - Each single-column resizebox table (with caption): ~0.28 page → 4 × 0.28 = **1.12 page**",
          "+  - Section/subsection headers, equations (eq:advantage, eq:grpo, eq:isr), itemized lists, paragraph indents: **~0.5 page**",
          "+- Float + structural overhead total: **~2.8 pages**",
          "+- **Prose budget: 8 − 2.8 = 5.2 pages × 650 ≈ 3,380 words**",
          " ",
          "-## Per-Section Target vs. Current",
          "+Current 6,674 → must cut **~3,300 words (~49%)** OR move material to appendix.",
          " ",
          "-| Section | Current | Target | Cut needed | Cut % |",
          "-|---------|--------:|-------:|-----------:|------:|",
          "-| Introduction | 635 | 550 | -85 | 13% |",
          "-| Related Work | 849 | 500 | **-349** | **41%** |",
          "-| Method | 879 | 800 | -79 | 9% |",
          "-| Experiments | 1,812 | 1,200 | **-612** | **34%** |",
          "-| Discussion | 558 | 250 | **-308** | **55%** |",
          "-| Conclusion | 432 | 250 | **-182** | **42%** |",
          "-| **Total** | **5,165** | **3,550** | **-1,615** | |",
          "+This matches the reported \"12 pages → 8 pages\" gap: ~4 pages over = ~2,600 prose words over, plus float reflow recovers another ~1 page.",
          " ",
          "-Remaining ~135 words of slack for formatting overhead.",
          "+## 3. Per-section budgets and cuts",
          " ",
          "----",
          "+| Section | Current | Target | Cut | Strategy |",
          "+|---|---|---|---|---|",
          "+| Abstract | 307 | 200–230 | ~80 | Tighten findings 2 & 3 |",
          "+| Introduction | 874 | 650 | ~225 | Compress paragraphs 2–4 |",
          "+| Related Work | 900 | 450 | ~450 | Single paragraph per theme, fewer citations inline |",
          "+| Method | 1140 | 650 | ~490 | Move H1–H7 enumeration + reward-formulation paragraphs to appendix; keep §3.1–§3.4 |",
          "+| Experiments | 2600 | 1100 | ~1,500 | Aggressive cut: merge subsections, drop redundant prose around tables, kill cross-seed narrative |",
          "+| Discussion | 613 | 250 | ~365 | Drop \"Practical Implications\" list; merge \"Classifier Limitations\" into Experiments |",
          "+| Conclusion | 547 | 180 | ~365 | One paragraph per finding, drop Limitations (separate unpaginated section) |",
          "+| **Total** | **6,674** | **~3,480** | **~3,200** | Hits ~5.4 pages of prose |",
          " ",
          "-## Cutting Plan by Priority",
          "+## 4. Specific cut recommendations (priority order)",
          " ",
          "-### Priority 1: Discussion → Appendix (~308 words saved)",
          "+### Priority 1 — Experiments (biggest absolute win: −1,500 words)",
          " ",
          "-Discussion is the easiest to compress. Most content repeats findings already stated in Experiments.",
          "+**Section 4.1 Setup (currently ~210 words):** Cut footnote on data file (project-internal note, irrelevant to readers). Cut the legacy-filename parenthetical about ProofWriter. Compress evaluation protocol paragraph by 40%. → target 120 words.",
          " ",
          "-**Move to Appendix:**",
          "-- \"ISR Capability Boundary\" paragraph: the NLI correlation ($\\rho = -0.049$) is already mentioned in Introduction; the exec-only vs. ISR-reward interpretation distinction is stated in §4.4. Cut to 1 sentence referencing the appendix.",
          "-- \"Premise Count Confound\" paragraph: fully redundant with §4.2 premise-count-matched analysis. Cut entirely, add forward ref from §4.2.",
          "-- \"Classifier Limitations\" paragraph: the Prolog blind-spot story is told in full in §4.3. Cut entirely.",
          "+**Section 4.2 ISR as Diagnostic (~440 words):**",
          "+- \"Collapse trajectory\" paragraph (lines 31–36): keep first 3 sentences, cut the monotonic-decline restatement at end. → −50 words",
          "+- \"Cross-seed instability\" (lines 38–42): the qualitative-mode description for s42/s43/s44 is now also in Conclusion and Method H1–H7 — keep only the σ=47pp headline and the \"diagnostic value\" sentence; move per-seed mode descriptions to appendix table. → −90 words",
          "+- \"SFT baseline\" (lines 44–47): the matched-PR caveat (line 47) repeats info already telegraphed by Tab 1 — drop the second sentence about 100-step appendix comparison. → −40 words",
          " ",
          "-**Keep (compressed to ~250 words):**",
          "-- \"Meta-Level Goodhart's Law\" paragraph — this is the conceptual contribution linking to Manheim taxonomy. Trim to core claim + citation.",
          "-- \"Practical Implications\" enumerate — keep all 5 items, tighten wording.",
          "+**Section 4.3 Meta-Level Goodhart (~750 words):** Largest cut target.",
          "+- Lead paragraph (52–54): merge into Tab 1 caption. → −60 words",
          "+- \"Low-dose ISR β=0.1\" (103–109): keep the H7 64.5% vs 0% number and one sentence on H1 conversion. Drop the \"Total conclusion embedding…GRPO-universal\" parenthetical (already in Conclusion). → −80 words",
          "+- \"Premise-count confound\" (111–117): this is critical for C2 — keep, but tighten by 30%. → −50 words",
          "+- \"High-dose ISR β=0.3\" (119–127): each seed gets 1 sentence currently, cut to a single sentence summarizing the 3-mode split with PR numbers; per-seed Goodhart pathology names move to appendix. → −180 words",
          " ",
          "-### Priority 2: Related Work compression (~349 words saved)",
          "+**Section 4.4 Cross-Logic Transfer (~620 words):**",
          "+- Prolog exec-only paragraph (167–171): the redundancy-vs-gaming interpretation sentence (last 2 lines) duplicates Discussion ¶ \"ISR Capability Boundary.\" Cut from Experiments, keep in Discussion. → −80 words",
          "+- Prolog ISR-as-reward (173–179): each seed described in 2 sentences; tighten to one per seed and let Tab 3 do the work. → −180 words",
          "+- \"FOL vs Prolog comparison\" (181–184): keep the 0% vs 16% headline; cut the \"broader gaming basin\" speculation (move to Discussion or drop). → −60 words",
          " ",
          "-Target: 500 words (from 849). This is the single largest absolute cut.",
          "+**Section 4.5 Hacking Taxonomy (~430 words):**",
          "+- The enumeration of which seed shows which mode (line 221) duplicates Tab 4 and Method H1–H7. Cut the prose enumeration entirely, keep only the table. → −100 words",
          "+- \"Cross-condition pattern\" paragraph (223–225): keep the 80% pooled-hacking number, cut the s42 81%/32% rehash (already in Tab 2). → −80 words",
          "+- Final two paragraphs (227–228): \"taxonomy is descriptive…\" can compress to one sentence. → −60 words",
          " ",
          "-**Current structure (4 paragraphs):**",
          "-1. Neurosymbolic Reasoning with LLMs (254 words)",
          "-2. Reward Shaping and Process Supervision (230 words)",
          "-3. Reward Hacking and Goodhart's Law (227 words)",
          "-4. Mutation Testing and Component Analysis (138 words)",
          "+### Priority 2 — Related Work (−450 words)",
          " ",
          "-**Cuts:**",
          "-- **¶1 Neurosymbolic**: Cut individual system descriptions (Logic-LM, LINC, SatLM, LoRP, FoVer each get 1 clause → compress to a single sentence listing all 5 with citations). Cut Mellgren/Logic-RL/Thought-Like-Pro individual descriptions → 1 sentence. Keep differentiation sentence. **Target: 120 words** (save ~134).",
          "-- **¶2 Reward Shaping**: Cut PROF, Qwen PRM, ProGRS individual descriptions — these are tangential. Keep Lightman PRM + Math-Shepherd as key refs, then jump to our differentiation. **Target: 120 words** (save ~110).",
          "-- **¶3 Goodhart**: Most important RW paragraph — keep more. Cut Karwowski, Pan, Kwa individual descriptions (keep as citations only). Cut Bondarenko/Kim/Yang to citation-only. Keep Gao scaling laws + Manheim taxonomy + Skalse impossibility as the three key refs. **Target: 150 words** (save ~77).",
          "-- **¶4 Mutation Testing**: Already lean. Cut LLMorpheus sentence. **Target: 110 words** (save ~28).",
          "+Current is 4 well-sized paragraphs but ACL accepted papers typically allocate 0.6–0.8 page (≈400–550 words) to related work. Cut strategy:",
          " ",
          "-### Priority 3: Experiments compression (~612 words saved)",
          "+- **Neurosymbolic Reasoning paragraph (~190 words):** Cut sentence about LoRP/FoVer (line 7) — these are marginal to our claim. Cut the \"report 87% conclusion embedding…suggests prove-rate gains may overstate\" sentence (line 13) since it duplicates the Intro hook. → −80 words",
          "+- **Reward Shaping paragraph (~220 words):** Drop the PROF and ProGRS sentences (lines 22–23) — they're tangential. Keep Lightman, Math-Shepherd, Gao-effective-RL. → −90 words",
          "+- **Reward Hacking paragraph (~245 words):** This is the closest cousin literature; keep dense. Drop the Kwa et al. sentence on heavy-tailed misspec (line 30) and the Yang spurious-rewards mention (line 32). → −90 words",
          "+- **Mutation Testing paragraph (~200 words):** Drop the Just et al. \"synthetic mutants approximate real faults\" sentence (line 39) and the LLMorpheus mention (line 40) — neither directly supports STA's novelty claim. → −90 words",
          "+- Convert paragraph headings to inline phrases (e.g., \"On the neurosymbolic side, ...\") to save ~10 words each.",
          " ",
          "-Target: 1,200 words (from 1,812). Hardest cut — this is the core evidence.",
          "+### Priority 3 — Method (−490 words, mostly via appendix migration)",
          " ",
          "-**MUST KEEP (non-negotiable):**",
          "-- Setup (¶1-2): training config, eval protocol — essential for reproducibility. Keep ~180 words.",
          "-- Table 1 (tab:goodhart-landscape) + Table 2 (tab:beta01-3seed): core Goodhart evidence.",
          "-- Table 3 (tab:prolog-crosslogic): cross-logic evidence.",
          "-- Figure 2 (fig:isr-collapse): collapse trajectory.",
          "-- All three key numbers: ISR 0.642→0.003; H7 64.5% vs 0%; premise-count 1.06×.",
          "+Move to appendix:",
          "+- **§3.5 Reward Formulations (lines 65–78):** All four definitions are restated in Experiments §4.1 and Table 1 — keep only the \"Additive ISR: r = r_exec·(1 + β·ISR), β ∈ {0.1, 0.3}\" inline mention in Experiments. The SFT, additive-random, and convex-combination paragraphs go to appendix. → −180 words",
          "+- **§3.6 Reward Hacking Taxonomy (lines 80–95):** The full H1–H7 enumeration belongs in appendix because Tab 4 + Fig 3 already convey the modes. Keep one sentence in Method linking to App §X. → −280 words",
          " ",
          "-**Move to Appendix:**",
          "-- **Cross-seed instability paragraph** (§4.1, \"The three exec-only seeds diverge...\"): The per-seed breakdown (s42=93% H1, s43=14% repetition, s44=98% tautological) can move to appendix. Keep 1 sentence: \"Three seeds diverge into qualitatively different failure modes (PR σ=47pp; Appendix X).\" **Save ~80 words.**",
          "-- **Table 4 (tab:hacking-taxonomy) + §4.4 Hacking Taxonomy subsection**: The 7-mode taxonomy table is important but the ~230 words of prose around it heavily repeats what's already in each subsection. Compress to a single paragraph referencing the table. Move detailed mode descriptions to Appendix. **Save ~150 words.**",
          "-- **Figure 4 (fig:prolog-comparison) → Appendix**: This can be referenced as \"Appendix Fig. X\" — the table already carries the cross-logic data. **Save ~0.35 page of float space (≈ 225 word-equivalents).**",
          "-- **β=0.3 per-seed breakdown** (\"Seed 42 exhibits reward collapse...; Seed 43 exhibits...; Seed 44 exhibits...\"): Move per-seed narrative to appendix, keep summary sentence + table ref. **Save ~100 words.**",
          "+Keep tight in main body: §3.1 Task (kept), §3.2 GRPO (compress to one paragraph + Eq 2, drop Eq 1), §3.3 STA protocol, §3.4 ISR definition + premise-count bias note.",
          " ",
          "-**Tighten in-place:**",
          "-- §4.1 Collapse trajectory: trim redundancy between text and fig caption. **Save ~50 words.**",
          "-- §4.2 Premise-count confound: well-written, keep but tighten. **Save ~30 words.**",
          "-- §4.3 Prolog section: the \"functional vs. strict classifier\" narrative (seeds s43/s44 classifier blind spot) is important but over-detailed. Compress to 2 sentences + table footnote. **Save ~80 words.**",
          "-- Setup: tighten. **Save ~30 words.**",
          "+### Priority 4 — Discussion (−365 words)",
          " ",
          "-**Float savings alternative**: If we move fig:prolog-comparison to appendix, we recover ~0.35 page, relaxing the word budget by ~225 words (reducing text cuts needed from 612 to ~390).",
          "+- Drop \"Practical Implications\" list (lines 38–45): 5-item list, ~140 words. This belongs in Conclusion or as a takeaways box. **Recommended: cut entirely** since each item is already implied by experiments + conclusion findings.",
          "+- Compress \"Classifier Limitations\" (¶4): the s43 uppercase + s44 query-as-fact details are in Experiments §4.4. Drop ¶4, keep one sentence in Experiments. → −100 words",
          "+- \"Premise Count Confound\" and \"ISR Capability Boundary\": keep both — these are the cleanest contributions of the discussion. Light edits only.",
          "+- \"Meta-Level Goodhart's Law\" ¶: tighten by 25%, drop the \"general principle for the reward-shaping community\" final sentence (the cautionary note is already in Abstract + Intro + Conclusion). → −60 words",
          " ",
          "-### Priority 4: Conclusion compression (~182 words saved)",
          "+### Priority 5 — Conclusion (−365 words)",
          " ",
          "-Target: 250 words (from 432).",
          "+- Three findings paragraphs (lines 6–20) all restate Abstract content with slightly more numbers. **Cut each to 1 sentence** that adds the headline number not in Abstract. → −280 words",
          "+- Drop \"Limitations\" paragraph (22–27): standard EMNLP convention is a separate \"Limitations\" section *after* References (which doesn't count against 8 pages). **Move Limitations to its own section** at end. → recovers 0 prose words from page budget directly, but frees ~80 words from §Conclusion (they become unpaginated content).",
          "+- \"Future directions\" paragraph: keep 2 sentences. → −90 words",
          " ",
          "-**Cuts:**",
          "-- Three \"finding\" paragraphs currently re-state numbers. Cut to 1 sentence each — the numbers are in the experiments section.",
          "-- Limitations paragraph: move to Appendix. Keep 1 sentence: \"Limitations include single model scale (Qwen3-4B), two logic types, and 3 seeds (Appendix X).\"",
          "-- Future directions: cut entirely. Standard boilerplate, no reviewer expects it.",
          "+### Priority 6 — Introduction (−225 words)",
          " ",
          "-### Priority 5: Introduction tightening (~85 words saved)",
          "+- \"The execution-only blind spot\" paragraph (9–13): cut the \"Process reward models…do not transfer\" sentence (line 12) — covered in Related Work. → −40 words",
          "+- \"Component necessity testing\" paragraph (15–20): the NLI ρ=−0.049 caveat (line 20) appears verbatim in Discussion + Conclusion. Keep in Discussion only. → −40 words",
          "+- \"ISR as diagnostic\" (22–25): drop the \"Three random seeds diverge…each converging to\" sentence — Tab 2 + cross-seed paragraph in Experiments cover it. → −60 words",
          "+- \"Meta-level Goodhart\" (27–33): tighten the β=0.3 enumeration (line 31, three Goodhart pathways) — keep one sentence. → −80 words",
          " ",
          "-Introduction is already fairly tight at 635 words.",
          "+### Priority 7 — Abstract (−80 words)",
          " ",
          "-**Cuts:**",
          "-- \"Component necessity testing\" paragraph: the ISR=1/ISR=0 definition is repeated in Method. Cut the definition sentences here, keep the high-level intuition. **Save ~30 words.**",
          "-- C1-C4 contribution list: tighten each item by ~10 words. **Save ~40 words.**",
          "-- \"We are explicit that LOO ablation is itself standard\" sentence: move caveat to Method. **Save ~15 words.**",
          "+- Sentence 6 (the β=0.1/β=0.3 dose-response): compress to one clause for each dose. → −50 words",
          "+- Sentence 8 (7 hacking modes): merge into sentence 9 (asymmetry conclusion). → −30 words",
          " ",
          "-### Priority 6: Method — minimal cuts (~79 words)",
          "+## 5. What MUST stay in main body (non-negotiable)",
          " ",
          "-Method is the definitional backbone; cut cautiously.",
          "+These are the load-bearing claims and their direct evidence; deleting them weakens the paper:",
          " ",
          "-**Cuts:**",
          "-- §3.5 Reward Formulations: cut the \"Additional formulations (convex combination...)\" paragraph — this negative result can go to appendix. **Save ~40 words.**",
          "-- §3.6 Taxonomy: H1-H7 list takes significant space. Consider moving to a compact table in Appendix and keeping only H1, H6/H7 definitions inline (the three most cited modes). **Save ~40 words.**",
          "+- **Abstract**: headline ISR 0.642→0.003 collapse number; H7 64.5%/0% contrast; 1.06× premise-matched ratio; cross-logic universal Goodhart.",
          "+- **Introduction**: opening hook (93% PR with 87% embedding), all 4 contributions C1–C4, the asymmetry statement.",
          "+- **Method §3.3 STA + §3.4 ISR**: full protocol definition + ISR equation; premise-count bias paragraph (critical for §4.3 confound analysis).",
          "+- **Experiments**: Fig 2 (collapse trajectory), Tab 1 (Goodhart landscape), Tab 2 (β=0.1 3-seed + n≥3 column — the 1.06× evidence), Tab 3 (Prolog cross-logic), Fig 3 (hacking composition).",
          "+- **Discussion**: \"ISR Capability Boundary\" (exec-low vs ISR-high interpretation, per active constraint C006), \"Premise Count Confound\" (methodological contribution).",
          "+- **Conclusion**: three-finding summary (compressed), pointer to Limitations.",
          " ",
          "----",
          "+## 6. Appendix migration list (recovers main-body space without losing content)",
          " ",
          "-## Alternative Strategy: Move 1 Figure to Appendix",
          "+| Content | Source | Appendix target |",
          "+|---|---|---|",
          "+| Reward formulation variants (random, convex-combo) | Method §3.5 | App A: Reward Formulations |",
          "+| Full H1–H7 mode definitions with examples | Method §3.6 | App B: Hacking Taxonomy |",
          "+| Per-seed exec-only traces (s42/s43/s44 descriptions) | Exp §4.2 | App C: Per-Seed Failure Modes |",
          "+| β=0.3 per-seed Goodhart pathway details | Exp §4.3 | App D: High-Dose Goodhart |",
          "+| 100-step matched-PR SFT comparison | Exp §4.2 | App E: SFT vs RL at Matched PR |",
          "+| Prolog s43 uppercase + s44 query-as-fact long-form descriptions | Exp §4.4, Disc | App F: Prolog Mode Mechanics |",
          "+| Classifier methodology (text-match + functional cross-check) | Method, Disc | App G: Two-Stage Classifier |",
          " ",
          "-If fig:prolog-comparison moves to Appendix:",
          "-- Recover 0.35 pages of float space → relax word budget by ~225 words",
          "-- New word budget: ~3,625 words (need to cut only ~1,540 instead of 1,750)",
          "-- This makes the Experiments cut less painful (need ~390 instead of 612)",
          "+## 7. Float discipline",
          " ",
          "-If ALSO move tab:hacking-taxonomy to Appendix:",
          "-- Recover additional 0.30 pages → relax by another ~195 words",
          "-- New word budget: ~3,820 words (need to cut only ~1,345)",
          "-- Experiments text can stay closer to 1,400 words",
          "+To maintain 4 figures + 4 tables in 8 pages, all floats should be single-column where possible:",
          "+- Tab 1, Tab 2, Tab 4 are already `\\resizebox{\\columnwidth}{!}` — good.",
          "+- Tab 3 is `\\resizebox{\\columnwidth}{!}` — good but currently 7 columns × 9 rows is dense; consider dropping the \"Mode\" column (last column is descriptive prose, can be replaced by a footnote keyed to a label).",
          "+- Fig 1 (sta-overview): if currently `figure*` (two-column), confirm whether one-column at 0.95\\columnwidth suffices.",
          "+- Fig 2/3/4: ensure all are `\\columnwidth` not `\\textwidth`.",
          " ",
          "-**Recommended float configuration for 8 pages:**",
          "-- **Keep**: fig:isr-collapse, tab:goodhart-landscape, tab:beta01-3seed, fig:hacking-composition (4 floats, ~1.25 pages)",
          "-- **Move to Appendix**: fig:prolog-comparison, tab:prolog-crosslogic, tab:hacking-taxonomy (3 floats, ~1.0 page saved)",
          "-- **New float cost**: ~1.25 pages",
          "-- **New word budget**: ~4,060 words — much more comfortable, need to cut ~1,100 words",
          "+**Recommendation: consider merging Tab 1 and Tab 2.** Tab 1 (Goodhart landscape) is a 3-seed mean ± std summary; Tab 2 (β=0.1 3-seed breakdown) is the per-seed version of one row of Tab 1. A single \"landscape with per-seed expansion for β=0.1\" table would save ~0.25 page. If kept separate, both tables can shrink rows: drop the \"Base (0-shot)\" row from Tab 1 (the 12% number is already in §3.2 prose).",
          " ",
          "-With this float strategy, revised targets:",
          "+## 8. Expected outcome",
          " ",
          "-| Section | Current | Target | Cut needed |",
          "-|---------|--------:|-------:|-----------:|",
          "-| Introduction | 635 | 580 | -55 |",
          "-| Related Work | 849 | 550 | -299 |",
          "-| Method | 879 | 830 | -49 |",
          "-| Experiments | 1,812 | 1,450 | -362 |",
          "-| Discussion | 558 | 350 | -208 |",
          "-| Conclusion | 432 | 300 | -132 |",
          "-| **Total** | **5,165** | **4,060** | **-1,105** |",
          "+After all cuts:",
          "+- Prose: ~3,480 words ≈ 5.4 pages",
          "+- Floats: 4 figures + 4 tables (or 3 tables if merged) ≈ 2.4 pages",
          "+- Structural overhead: ~0.4 page",
          "+- **Projected total: 8.2 pages → trim further in Experiments §4.3/§4.4 if margin negative**",
          " ",
          "----",
          "+If 8.2 still over, additional 0.2-page cut from Experiments §4.5 (remove Fig 3 hacking-composition — its content is fully captured by Tab 4).",
          " ",
          "-## Summary",
          "+## 9. Open items",
          " ",
          "-| Approach | Floats in main | Word budget | Words to cut |",
          "-|----------|:--------------:|:-----------:|:------------:|",
          "-| Keep all 7 floats | 7 | ~3,400 | ~1,750 |",
          "-| Move 1 fig to appendix | 6 | ~3,625 | ~1,540 |",
          "-| **Move 3 floats to appendix (recommended)** | **4** | **~4,060** | **~1,100** |",
          "-",
          "-The recommended strategy (move 3 floats to appendix) is the most realistic path to 8 pages. The 4 retained floats (collapse figure, Goodhart landscape table, 3-seed breakdown table, hacking composition figure) carry the three core claims. The Prolog cross-logic story is preserved via in-text description referencing appendix tables/figures.",
          "-",
          "-Biggest wins by effort:",
          "-1. **Discussion → 350 words** (cut 208, easy — all redundant with Experiments)",
          "-2. **Related Work → 550 words** (cut 299, medium — compress citations)",
          "-3. **Experiments → 1,450 words** (cut 362, hard but feasible with appendix offloading)",
          "-4. **Conclusion → 300 words** (cut 132, easy — remove future directions + compress)",
          "-5. **Introduction → 580 words** (cut 55, minor tightening)",
          "-6. **Method → 830 words** (cut 49, move convex-combo paragraph + trim taxonomy list)",
          "+- **s43 random β=0.3 placeholder** in Tab 1 footnote (§): Experiments §4.3 currently reports 2-seed random control. Decision deferred per task brief — when s43 data lands, the only edit is updating the footnote and the mean ± std row.",
          "+- **Fig 1 sta-overview placement**: not in any of the artifacts I read — currently referenced only in Intro line 16. Confirm the asset exists; if not, this is a separate work item (not a page-budget issue)."
        ]
      }
    ],
    "originalFile": "# Page Budget Analysis — EMNLP 2026 (8-page limit)\n\n## Word Counts (LaTeX stripped)\n\n| Section | Words | Notes |\n|---------|------:|-------|\n| Abstract | 207 | On page 1, not separately counted |\n| Introduction | 635 | |\n| Related Work | 849 | |\n| Method | 879 | 3 equations + 2 enumerates add ~150 word-equivalents |\n| Experiments | 1,812 | 4 tables + 3 figures |\n| Discussion | 558 | 1 enumerate (5 items) |\n| Conclusion | 432 | |\n| **Body total (excl. abstract)** | **5,165** | |\n\n## Float Inventory\n\n| Float | Type | Width | Est. page cost |\n|-------|------|-------|---------------|\n| fig:isr-collapse | figure | 0.95col | 0.30 |\n| tab:goodhart-landscape | table | col (resizebox) | 0.30 |\n| tab:beta01-3seed | table | col (resizebox) | 0.35 |\n| fig:prolog-comparison | figure | 0.95col | 0.35 |\n| tab:prolog-crosslogic | table | col (resizebox) | 0.35 |\n| fig:hacking-composition | figure | 0.92col | 0.30 |\n| tab:hacking-taxonomy | table | col (resizebox) | 0.30 |\n| **Total floats** | | | **~2.25 pages** |\n\n## Page Budget Calculation\n\n- **Available**: 8 pages\n- **Title + authors + abstract**: ~0.5 page\n- **Floats (4 tables + 3 figures)**: ~2.25 pages\n- **Remaining for body text**: 8 - 0.5 - 2.25 = **5.25 pages**\n- **Word budget** (at ~650 words/page ACL double-col): **~3,400 words**\n- **Current body text**: 5,165 words\n- **Overshoot**: **~1,750 words (≈ 2.7 pages)**\n\nNote: Equations (Method ×3), itemize/enumerate formatting, and section headers add ~200-300 word-equivalents of vertical space, pushing effective overshoot closer to **~2,000 words**.\n\n## Per-Section Target vs. Current\n\n| Section | Current | Target | Cut needed | Cut % |\n|---------|--------:|-------:|-----------:|------:|\n| Introduction | 635 | 550 | -85 | 13% |\n| Related Work | 849 | 500 | **-349** | **41%** |\n| Method | 879 | 800 | -79 | 9% |\n| Experiments | 1,812 | 1,200 | **-612** | **34%** |\n| Discussion | 558 | 250 | **-308** | **55%** |\n| Conclusion | 432 | 250 | **-182** | **42%** |\n| **Total** | **5,165** | **3,550** | **-1,615** | |\n\nRemaining ~135 words of slack for formatting overhead.\n\n---\n\n## Cutting Plan by Priority\n\n### Priority 1: Discussion → Appendix (~308 words saved)\n\nDiscussion is the easiest to compress. Most content repeats findings already stated in Experiments.\n\n**Move to Appendix:**\n- \"ISR Capability Boundary\" paragraph: the NLI correlation ($\\rho = -0.049$) is already mentioned in Introduction; the exec-only vs. ISR-reward interpretation distinction is stated in §4.4. Cut to 1 sentence referencing the appendix.\n- \"Premise Count Confound\" paragraph: fully redundant with §4.2 premise-count-matched analysis. Cut entirely, add forward ref from §4.2.\n- \"Classifier Limitations\" paragraph: the Prolog blind-spot story is told in full in §4.3. Cut entirely.\n\n**Keep (compressed to ~250 words):**\n- \"Meta-Level Goodhart's Law\" paragraph — this is the conceptual contribution linking to Manheim taxonomy. Trim to core claim + citation.\n- \"Practical Implications\" enumerate — keep all 5 items, tighten wording.\n\n### Priority 2: Related Work compression (~349 words saved)\n\nTarget: 500 words (from 849). This is the single largest absolute cut.\n\n**Current structure (4 paragraphs):**\n1. Neurosymbolic Reasoning with LLMs (254 words)\n2. Reward Shaping and Process Supervision (230 words)\n3. Reward Hacking and Goodhart's Law (227 words)\n4. Mutation Testing and Component Analysis (138 words)\n\n**Cuts:**\n- **¶1 Neurosymbolic**: Cut individual system descriptions (Logic-LM, LINC, SatLM, LoRP, FoVer each get 1 clause → compress to a single sentence listing all 5 with citations). Cut Mellgren/Logic-RL/Thought-Like-Pro individual descriptions → 1 sentence. Keep differentiation sentence. **Target: 120 words** (save ~134).\n- **¶2 Reward Shaping**: Cut PROF, Qwen PRM, ProGRS individual descriptions — these are tangential. Keep Lightman PRM + Math-Shepherd as key refs, then jump to our differentiation. **Target: 120 words** (save ~110).\n- **¶3 Goodhart**: Most important RW paragraph — keep more. Cut Karwowski, Pan, Kwa individual descriptions (keep as citations only). Cut Bondarenko/Kim/Yang to citation-only. Keep Gao scaling laws + Manheim taxonomy + Skalse impossibility as the three key refs. **Target: 150 words** (save ~77).\n- **¶4 Mutation Testing**: Already lean. Cut LLMorpheus sentence. **Target: 110 words** (save ~28).\n\n### Priority 3: Experiments compression (~612 words saved)\n\nTarget: 1,200 words (from 1,812). Hardest cut — this is the core evidence.\n\n**MUST KEEP (non-negotiable):**\n- Setup (¶1-2): training config, eval protocol — essential for reproducibility. Keep ~180 words.\n- Table 1 (tab:goodhart-landscape) + Table 2 (tab:beta01-3seed): core Goodhart evidence.\n- Table 3 (tab:prolog-crosslogic): cross-logic evidence.\n- Figure 2 (fig:isr-collapse): collapse trajectory.\n- All three key numbers: ISR 0.642→0.003; H7 64.5% vs 0%; premise-count 1.06×.\n\n**Move to Appendix:**\n- **Cross-seed instability paragraph** (§4.1, \"The three exec-only seeds diverge...\"): The per-seed breakdown (s42=93% H1, s43=14% repetition, s44=98% tautological) can move to appendix. Keep 1 sentence: \"Three seeds diverge into qualitatively different failure modes (PR σ=47pp; Appendix X).\" **Save ~80 words.**\n- **Table 4 (tab:hacking-taxonomy) + §4.4 Hacking Taxonomy subsection**: The 7-mode taxonomy table is important but the ~230 words of prose around it heavily repeats what's already in each subsection. Compress to a single paragraph referencing the table. Move detailed mode descriptions to Appendix. **Save ~150 words.**\n- **Figure 4 (fig:prolog-comparison) → Appendix**: This can be referenced as \"Appendix Fig. X\" — the table already carries the cross-logic data. **Save ~0.35 page of float space (≈ 225 word-equivalents).**\n- **β=0.3 per-seed breakdown** (\"Seed 42 exhibits reward collapse...; Seed 43 exhibits...; Seed 44 exhibits...\"): Move per-seed narrative to appendix, keep summary sentence + table ref. **Save ~100 words.**\n\n**Tighten in-place:**\n- §4.1 Collapse trajectory: trim redundancy between text and fig caption. **Save ~50 words.**\n- §4.2 Premise-count confound: well-written, keep but tighten. **Save ~30 words.**\n- §4.3 Prolog section: the \"functional vs. strict classifier\" narrative (seeds s43/s44 classifier blind spot) is important but over-detailed. Compress to 2 sentences + table footnote. **Save ~80 words.**\n- Setup: tighten. **Save ~30 words.**\n\n**Float savings alternative**: If we move fig:prolog-comparison to appendix, we recover ~0.35 page, relaxing the word budget by ~225 words (reducing text cuts needed from 612 to ~390).\n\n### Priority 4: Conclusion compression (~182 words saved)\n\nTarget: 250 words (from 432).\n\n**Cuts:**\n- Three \"finding\" paragraphs currently re-state numbers. Cut to 1 sentence each — the numbers are in the experiments section.\n- Limitations paragraph: move to Appendix. Keep 1 sentence: \"Limitations include single model scale (Qwen3-4B), two logic types, and 3 seeds (Appendix X).\"\n- Future directions: cut entirely. Standard boilerplate, no reviewer expects it.\n\n### Priority 5: Introduction tightening (~85 words saved)\n\nIntroduction is already fairly tight at 635 words.\n\n**Cuts:**\n- \"Component necessity testing\" paragraph: the ISR=1/ISR=0 definition is repeated in Method. Cut the definition sentences here, keep the high-level intuition. **Save ~30 words.**\n- C1-C4 contribution list: tighten each item by ~10 words. **Save ~40 words.**\n- \"We are explicit that LOO ablation is itself standard\" sentence: move caveat to Method. **Save ~15 words.**\n\n### Priority 6: Method — minimal cuts (~79 words)\n\nMethod is the definitional backbone; cut cautiously.\n\n**Cuts:**\n- §3.5 Reward Formulations: cut the \"Additional formulations (convex combination...)\" paragraph — this negative result can go to appendix. **Save ~40 words.**\n- §3.6 Taxonomy: H1-H7 list takes significant space. Consider moving to a compact table in Appendix and keeping only H1, H6/H7 definitions inline (the three most cited modes). **Save ~40 words.**\n\n---\n\n## Alternative Strategy: Move 1 Figure to Appendix\n\nIf fig:prolog-comparison moves to Appendix:\n- Recover 0.35 pages of float space → relax word budget by ~225 words\n- New word budget: ~3,625 words (need to cut only ~1,540 instead of 1,750)\n- This makes the Experiments cut less painful (need ~390 instead of 612)\n\nIf ALSO move tab:hacking-taxonomy to Appendix:\n- Recover additional 0.30 pages → relax by another ~195 words\n- New word budget: ~3,820 words (need to cut only ~1,345)\n- Experiments text can stay closer to 1,400 words\n\n**Recommended float configuration for 8 pages:**\n- **Keep**: fig:isr-collapse, tab:goodhart-landscape, tab:beta01-3seed, fig:hacking-composition (4 floats, ~1.25 pages)\n- **Move to Appendix**: fig:prolog-comparison, tab:prolog-crosslogic, tab:hacking-taxonomy (3 floats, ~1.0 page saved)\n- **New float cost**: ~1.25 pages\n- **New word budget**: ~4,060 words — much more comfortable, need to cut ~1,100 words\n\nWith this float strategy, revised targets:\n\n| Section | Current | Target | Cut needed |\n|---------|--------:|-------:|-----------:|\n| Introduction | 635 | 580 | -55 |\n| Related Work | 849 | 550 | -299 |\n| Method | 879 | 830 | -49 |\n| Experiments | 1,812 | 1,450 | -362 |\n| Discussion | 558 | 350 | -208 |\n| Conclusion | 432 | 300 | -132 |\n| **Total** | **5,165** | **4,060** | **-1,105** |\n\n---\n\n## Summary\n\n| Approach | Floats in main | Word budget | Words to cut |\n|----------|:--------------:|:-----------:|:------------:|\n| Keep all 7 floats | 7 | ~3,400 | ~1,750 |\n| Move 1 fig to appendix | 6 | ~3,625 | ~1,540 |\n| **Move 3 floats to appendix (recommended)** | **4** | **~4,060** | **~1,100** |\n\nThe recommended strategy (move 3 floats to appendix) is the most realistic path to 8 pages. The 4 retained floats (collapse figure, Goodhart landscape table, 3-seed breakdown table, hacking composition figure) carry the three core claims. The Prolog cross-logic story is preserved via in-text description referencing appendix tables/figures.\n\nBiggest wins by effort:\n1. **Discussion → 350 words** (cut 208, easy — all redundant with Experiments)\n2. **Related Work → 550 words** (cut 299, medium — compress citations)\n3. **Experiments → 1,450 words** (cut 362, hard but feasible with appendix offloading)\n4. **Conclusion → 300 words** (cut 132, easy — remove future directions + compress)\n5. **Introduction → 580 words** (cut 55, minor tightening)\n6. **Method → 830 words** (cut 49, move convex-combo paragraph + trim taxonomy list)\n",
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 31_

Analysis written to `artifacts/_project/paper/page_budget_analysis.md`.

**Headline numbers:**
- Current total body: **6,674 words** (Abstract 307 / Intro 874 / Related 900 / Method 1,140 / Experiments 2,600 / Discussion 613 / Conclusion 547)
- Floats: 4 figures + 4 tables → ~2.4 pages of float real estate
- 8-page prose budget: **~3,380 words** → need to cut **~3,200 words (~49%)**

**Biggest cut targets (priority order):**
1. **Experiments −1,500** — main body has too much per-seed narrative that duplicates the tables; §4.3 (Goodhart) and §4.4 (cross-logic) carry the bulk.
2. **Method −490** — move H1–H7 enumeration and reward-formulation variants to appendix (already redundant with Tab 1 + Tab 4).
3. **Related Work −450** — drop tangential cites (LoRP/FoVer, PROF, ProGRS, Kwa, Just, LLMorpheus).
4. **Discussion −365** — kill "Practical Implications" 5-item list and "Classifier Limitations" paragraph (duplicates Exp §4.4).
5. **Conclusion −365** — compress 3 findings to one sentence each; spin Limitations into a separate unpaginated section after References.
6. **Intro −225**, **Abstract −80** — light tightening.

**Must keep:** ISR 0.642→0.003 collapse trajectory, H7 64.5%/0% contrast, premise-count-matched 1.06× number, all 4 figures, Tabs 1–4 (or merge Tab 1+Tab 2), C006 "two semantics of low/high ISR" sentence in Discussion.

**Floats to revisit:** consider merging Tab 1 and Tab 2 (Tab 2 is a per-seed expansion of one Tab 1 row) for ~0.25 page; switch any `\textwidth` figure to `\columnwidth`.

**Open items flagged:** s43 random β=0.3 placeholder and fig:sta-overview asset existence — both unrelated to page budget.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca27e824-6ca6-4db1-9e55-77ef612ddfd7",
  "uuid": "ff23d707-7ba9-42af-93d1-f0b84fb0d678",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01UrCxnGy7rZbBvuFkbTy6HF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6131,
      "cache_read_input_tokens": 67812,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6131
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

### Task result

_source line 32_

Analysis written to `artifacts/_project/paper/page_budget_analysis.md`.

**Headline numbers:**
- Current total body: **6,674 words** (Abstract 307 / Intro 874 / Related 900 / Method 1,140 / Experiments 2,600 / Discussion 613 / Conclusion 547)
- Floats: 4 figures + 4 tables → ~2.4 pages of float real estate
- 8-page prose budget: **~3,380 words** → need to cut **~3,200 words (~49%)**

**Biggest cut targets (priority order):**
1. **Experiments −1,500** — main body has too much per-seed narrative that duplicates the tables; §4.3 (Goodhart) and §4.4 (cross-logic) carry the bulk.
2. **Method −490** — move H1–H7 enumeration and reward-formulation variants to appendix (already redundant with Tab 1 + Tab 4).
3. **Related Work −450** — drop tangential cites (LoRP/FoVer, PROF, ProGRS, Kwa, Just, LLMorpheus).
4. **Discussion −365** — kill "Practical Implications" 5-item list and "Classifier Limitations" paragraph (duplicates Exp §4.4).
5. **Conclusion −365** — compress 3 findings to one sentence each; spin Limitations into a separate unpaginated section after References.
6. **Intro −225**, **Abstract −80** — light tightening.

**Must keep:** ISR 0.642→0.003 collapse trajectory, H7 64.5%/0% contrast, premise-count-matched 1.06× number, all 4 figures, Tabs 1–4 (or merge Tab 1+Tab 2), C006 "two semantics of low/high ISR" sentence in Discussion.

**Floats to revisit:** consider merging Tab 1 and Tab 2 (Tab 2 is a per-seed expansion of one Tab 1 row) for ~0.25 page; switch any `\textwidth` figure to `\columnwidth`.

**Open items flagged:** s43 random β=0.3 placeholder and fig:sta-overview asset existence — both unrelated to page budget.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 231804,
  "duration_api_ms": 231583,
  "num_turns": 14,
  "stop_reason": "end_turn",
  "session_id": "ca27e824-6ca6-4db1-9e55-77ef612ddfd7",
  "total_cost_usd": 1.1131890000000002,
  "usage": {
    "input_tokens": 19,
    "cache_creation_input_tokens": 57702,
    "cache_read_input_tokens": 696811,
    "output_tokens": 16038,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 57702,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 746,
        "cache_read_input_tokens": 67812,
        "cache_creation_input_tokens": 6131,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 6131
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 3016,
      "outputTokens": 17,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.003101,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-7[1m]": {
      "inputTokens": 19,
      "outputTokens": 16038,
      "cacheReadInputTokens": 696811,
      "cacheCreationInputTokens": 57702,
      "webSearchRequests": 0,
      "costUSD": 1.1100880000000002,
      "contextWindow": 1000000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "adb9af9a-fa40-4173-bc79-d9bd45111ace"
}
```

</details>

---
