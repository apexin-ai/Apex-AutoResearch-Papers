# paper final intro tighten

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/workers/worker_paper_final-intro-tighten_20260522T184655.log`
- **Structured JSON:** [`1670b805792723646633.json`](../../sessions/16/1670b805792723646633.json)

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "session_id": "0cf4b583-8eb2-4877-b24a-53b049f91d88",
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
  "uuid": "1e2f5646-f97b-4d40-9f40-20d600bc1cd1",
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
    "resetsAt": 1779489600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "88c6806c-61ff-4023-b0d5-895d9474a998",
  "session_id": "0cf4b583-8eb2-4877-b24a-53b049f91d88"
}
```

---

### Assistant

_source line 4_

I'll read the introduction file first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0cf4b583-8eb2-4877-b24a-53b049f91d88",
  "uuid": "8c328954-1877-467a-847b-be4af402ea34",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YEbGo37WiXKNaK3ekoDgY1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14938,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14938
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

<details open><summary>🔧 Tool call — Read · `toolu_01Vtai6WdkBiV6qsM966GqR8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0cf4b583-8eb2-4877-b24a-53b049f91d88",
  "uuid": "7778f51a-0a7d-419d-a22e-4539989ae14c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YEbGo37WiXKNaK3ekoDgY1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14938,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14938
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

_source line 6 · 2026-05-22T18:47:12.575Z_

<details><summary>↩ Tool result · `toolu_01Vtai6WdkBiV6qsM966GqR8`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Neurosymbolic reasoning pipelines evaluate success by a single criterion: whether the generated formalization proves under a formal solver.
5	This treats all proofs as equal: a formalization that embeds the conclusion verbatim among its premises receives the same reward as one that derives it through genuine reasoning.
6	Under reinforcement learning, this indifference becomes an active vulnerability~\citep{geirhos2020shortcut}. The optimizer exploits any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}, and execution feedback provides no signal against structural shortcuts.
7	
8	\paragraph{The evaluation gap.}
9	Neurosymbolic formalizers~\citep{logic-lm, linc, satlm} and RL-trained variants~\citep{mellgren-prolog-grpo, logic-rl, deepseekmath} rely on execution accuracy alone, with no diagnostic for whether individual components contribute to the proof.
10	Process reward models~\citep{lightman-verify-step, math-shepherd} offer finer granularity but require expensive step-level annotations that do not transfer to arbitrary solver-backed settings.
11	Inference-time gaming detection~\citep{kim-game-formalization, bondarenko-spec-gaming} addresses a complementary problem but offers no training-time diagnostic.
12	What is missing is an annotation-free method for testing \emph{component necessity} in neurosymbolic outputs.
13	
14	\paragraph{Component necessity testing.}
15	We address this gap with \emph{Solver Trace Ablation} (STA), a diagnostic that tests whether each component of a formalization is necessary for proof success.
16	For each proved output, STA removes components one at a time and re-runs the solver; the fraction whose removal breaks the proof yields the \emph{Intensional Structural Reward} (ISR).
17	A formalization where every component is necessary receives $\text{ISR}{=}1$; one that proves regardless of which component is removed receives $\text{ISR}{=}0$.
18	Leave-one-out ablation itself is standard~\citep{demillo1978, jia-harman-survey}; our contribution is the empirical finding that the same structure making ISR informative as a diagnostic also makes it gameable as a reward.
19	
20	\begin{figure}[t]
21	\centering
22	\includegraphics[width=0.95\columnwidth]{figures/fig5_training_isr_curves.pdf}
23	\caption{ISR training trajectories across reward conditions (proved samples only, rolling $w{=}20$). Exec-only collapses to $\text{ISR}{\approx}0$, confirming structural degeneration (\S\ref{sec:diagnostic}); the ${\sim}0.5$ plateau is an $n{=}2$ artifact. ISR $\beta{=}0.1$ seeds rise toward $\text{ISR}{\approx}1$ via TS gaming (Goodhart effect, \S\ref{sec:goodhart}); random remains low.}
24	\label{fig:training-isr-curves}
25	\end{figure}
26	
27	\paragraph{The observe-vs-optimize asymmetry.}
28	Applied post-hoc, ISR exposes a structural collapse hidden from prove rate (Figure~\ref{fig:training-isr-curves}): as execution scores climb, component necessity collapses (per-sample mode classification, rather than the aggregate ISR scalar, provides the primary diagnostic evidence; \S\ref{sec:method}), revealing that high prove rate coexists with near-complete structural degeneration.
29	Yet the same LOO structure that makes ISR diagnostic also creates a Goodhart vulnerability~\citep{manheim-goodhart-taxonomy, karwowski-goodhart-rl, gao-reward-overoptimization}: tautological formalizations ($P{\to}P$) satisfy the necessity criterion by construction, so when ISR is repurposed as a training reward, the model learns to game the diagnostic rather than the task.
30	In this setting, the asymmetry persists across logic types, dataset families, reward doses, and random seeds: structural proxies for reasoning quality are easier to observe than to optimize.
31	
32	\paragraph{Contributions.}
33	In this Qwen3-4B case study across two logic types, two dataset families, and multiple reward conditions, we contribute:
34	(\textbf{C1})~STA as a diagnostic framework for neurosymbolic reasoning, including the ISR metric, an eight-mode hacking taxonomy, and a cross-domain evaluation protocol (\S\ref{sec:diagnostic});
35	(\textbf{C2})~empirical characterization of a Goodhart effect when ISR is repurposed as a training reward, with controls ruling out confounds (\S\ref{sec:goodhart});
36	(\textbf{C3})~cross-logic and cross-dataset evidence documenting the observe-vs-optimize asymmetry (\S\ref{sec:crossdomain}).
37	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0cf4b583-8eb2-4877-b24a-53b049f91d88",
  "uuid": "83ed70e8-57c8-4dd7-a4ef-939698f03193",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nNeurosymbolic reasoning pipelines evaluate success by a single criterion: whether the generated formalization proves under a formal solver.\nThis treats all proofs as equal: a formalization that embeds the conclusion verbatim among its premises receives the same reward as one that derives it through genuine reasoning.\nUnder reinforcement learning, this indifference becomes an active vulnerability~\\citep{geirhos2020shortcut}. The optimizer exploits any shortcut the reward fails to penalize~\\citep{skalse-reward-hacking, reward-hacking-survey}, and execution feedback provides no signal against structural shortcuts.\n\n\\paragraph{The evaluation gap.}\nNeurosymbolic formalizers~\\citep{logic-lm, linc, satlm} and RL-trained variants~\\citep{mellgren-prolog-grpo, logic-rl, deepseekmath} rely on execution accuracy alone, with no diagnostic for whether individual components contribute to the proof.\nProcess reward models~\\citep{lightman-verify-step, math-shepherd} offer finer granularity but require expensive step-level annotations that do not transfer to arbitrary solver-backed settings.\nInference-time gaming detection~\\citep{kim-game-formalization, bondarenko-spec-gaming} addresses a complementary problem but offers no training-time diagnostic.\nWhat is missing is an annotation-free method for testing \\emph{component necessity} in neurosymbolic outputs.\n\n\\paragraph{Component necessity testing.}\nWe address this gap with \\emph{Solver Trace Ablation} (STA), a diagnostic that tests whether each component of a formalization is necessary for proof success.\nFor each proved output, STA removes components one at a time and re-runs the solver; the fraction whose removal breaks the proof yields the \\emph{Intensional Structural Reward} (ISR).\nA formalization where every component is necessary receives $\\text{ISR}{=}1$; one that proves regardless of which component is removed receives $\\text{ISR}{=}0$.\nLeave-one-out ablation itself is standard~\\citep{demillo1978, jia-harman-survey}; our contribution is the empirical finding that the same structure making ISR informative as a diagnostic also makes it gameable as a reward.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.95\\columnwidth]{figures/fig5_training_isr_curves.pdf}\n\\caption{ISR training trajectories across reward conditions (proved samples only, rolling $w{=}20$). Exec-only collapses to $\\text{ISR}{\\approx}0$, confirming structural degeneration (\\S\\ref{sec:diagnostic}); the ${\\sim}0.5$ plateau is an $n{=}2$ artifact. ISR $\\beta{=}0.1$ seeds rise toward $\\text{ISR}{\\approx}1$ via TS gaming (Goodhart effect, \\S\\ref{sec:goodhart}); random remains low.}\n\\label{fig:training-isr-curves}\n\\end{figure}\n\n\\paragraph{The observe-vs-optimize asymmetry.}\nApplied post-hoc, ISR exposes a structural collapse hidden from prove rate (Figure~\\ref{fig:training-isr-curves}): as execution scores climb, component necessity collapses (per-sample mode classification, rather than the aggregate ISR scalar, provides the primary diagnostic evidence; \\S\\ref{sec:method}), revealing that high prove rate coexists with near-complete structural degeneration.\nYet the same LOO structure that makes ISR diagnostic also creates a Goodhart vulnerability~\\citep{manheim-goodhart-taxonomy, karwowski-goodhart-rl, gao-reward-overoptimization}: tautological formalizations ($P{\\to}P$) satisfy the necessity criterion by construction, so when ISR is repurposed as a training reward, the model learns to game the diagnostic rather than the task.\nIn this setting, the asymmetry persists across logic types, dataset families, reward doses, and random seeds: structural proxies for reasoning quality are easier to observe than to optimize.\n\n\\paragraph{Contributions.}\nIn this Qwen3-4B case study across two logic types, two dataset families, and multiple reward conditions, we contribute:\n(\\textbf{C1})~STA as a diagnostic framework for neurosymbolic reasoning, including the ISR metric, an eight-mode hacking taxonomy, and a cross-domain evaluation protocol (\\S\\ref{sec:diagnostic});\n(\\textbf{C2})~empirical characterization of a Goodhart effect when ISR is repurposed as a training reward, with controls ruling out confounds (\\S\\ref{sec:goodhart});\n(\\textbf{C3})~cross-logic and cross-dataset evidence documenting the observe-vs-optimize asymmetry (\\S\\ref{sec:crossdomain}).\n",
      "numLines": 37,
      "startLine": 1,
      "totalLines": 37
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
Let me analyze the introduction against the four criteria:

1. **Opening hook**: The current opening talks about neurosymbolic reasoning pipelines and execution-based evaluation. It's technically sound but not punchy. It doesn't immediately highlight the counterintuitive finding (high PR but structural degeneration). The hook could be stronger by leading with the paradox.

2. **Story spine**: problem → gap → STA contribution → key findings. Let me trace:
   - L4-6: Problem (execution-only evaluation misses structural shortcuts)
   - L8-12: Gap (no annotation-free method for component necessity)
   - L14-18: STA contribution
   - L20-25: Figure
   - L27-30: Observe-vs-optimize asymmetry (key finding)
   - L32-36: Contributions

The flow works overall, but there's an awkward transition from component necessity testing straight to the figure, then jumping to the asymmetry finding. The figure caption also packs too much information.

3. **Redundancy**: Lines 4-5 and 28 both hit the same point about high prove rates masking structural degeneration. Line 12 starts introducing the annotation-free method concept but the thought cuts off.

4. **Case study framing**: Line 33 anchors things nicely with "In this Qwen3-4B case study," but line 30 makes a broad generalization claim about the asymmetry persisting across logic types, datasets, and random seeds. The opening also feels procedural rather than leading with the counterintuitive finding.

I should strengthen the opening hook to lead with the paradox instead of the procedure, tighten the redundancies, and clarify what's a case study observation versus a general claim. I'm working through how to strengthen the opening by leading with the paradox rather than a dry definitional statement. The core insight is that the evaluation criterion treats all proofs equally, creating a vulnerability the optimizer can exploit—so I should front-load that tension instead of burying it. Let me refine the phrasing to make the contradiction more immediate while keeping the citations and core claims intact. I'm restructuring the opening to lead with the paradox—a neurosymbolic reasoner can achieve near-perfect proof rates even when every component is dispensable. Then I'll explain how execution-based evaluation misses this structural collapse, treating trivial formalizations that embed the conclusion the same as genuine derivations. Under reinforcement learning, this blind spot becomes exploitable, letting the optimizer find shortcuts the reward signal can't catch. I'm adding a counterintuitive hook at the start to emphasize the key finding—that proof rates can climb while the reasoning structure simultaneously degenerates—before explaining how the reward mechanism creates this vulnerability.

Now I'm reviewing the narrative flow and noticing the transition between the methodology section and the key finding feels abrupt. I need to strengthen that bridge.

I'm also catching some redundancy—the point about component necessity collapsing gets echoed across paragraphs, and there's a long parenthetical in the middle of a sentence that's breaking up the readability. I should tighten the language there and consider whether that citation reference needs to stay inline or could move elsewhere.

The bigger issue is that line 18 and line 29 are saying essentially the same thing about how the LOO structure creates both diagnostic value and Goodhart vulnerability. Since line 18 is already in the contribution statement, I can trim it there and let line 29 carry the full explanation later. That way the opening stays punchy and the elaboration happens when it's needed for the argument. I'm trimming the redundancy by having L18 reference the later sections rather than spelling out the Goodhart vulnerability details, since L29 already covers that thoroughly.

Now looking at the case study scoping issue — L30 makes a broad claim about asymmetry persisting across multiple conditions, but it's only demonstrated in the Qwen3-4B experiment. I should add a qualifier like "In our case study" to make clear this isn't a universal finding, just what we observed in this particular setting. I'm recognizing that the long parenthetical about per-sample mode classification is a methodological detail that clutters the introduction—it belongs in the methods section. I'll strip it out and tighten the sentence to avoid redundancy: the phrase "structural collapse hidden from prove rate" already conveys what "high prove rate coexists with near-complete structural degeneration" repeats, so I can compress this to a single, cleaner statement about what ISR reveals. I'm working through the edits to tighten the argument, starting with strengthening the hook by leading with the paradox itself—that prove rates can climb while proof structure deteriorates—before explaining why this happens through the lens of a flawed reward signal that treats all successful proofs identically. I'm tightening the sentence structure by using a semicolon instead of a period to connect related clauses more smoothly. For the ablation section, I'm refocusing the contribution statement to emphasize the systematic application and consequences rather than pre-announcing the Goodhart finding—letting that land with more impact later in the paper.

Now I'm compressing the ISR exposure paragraph by cutting the long parenthetical about per-sample classification and moving the methodological reference to a cleaner citation. The core finding stays: as execution scores rise, component necessity collapses, which contradicts the prove rate signal.

For the scope edit, I'm narrowing the generalization claim to avoid overreaching while still showing the asymmetry holds across multiple experimental conditions.

Checking the other potential over-generalizations: the neurosymbolic formalizers claim is properly cited, and the annotation-free method gap statement is backed by the preceding context, so those are fine.

The logical fact about tautological formalizations is mathematically sound, and the inference-time gaming detection statement, while slightly awkward in phrasing, still conveys the intended meaning without being misleading.

The eight-mode hacking taxonomy is a specific detail that's appropriately grounded, so no issues there either.

Let me finalize these edits and move forward.

Actually, I should reconsider the observe-versus-optimize asymmetry section more carefully. The core insight is that ISR works well as a post-hoc diagnostic because it reveals structural collapse that execution scores mask, but when repurposed as a training objective, the same mechanism becomes exploitable—models learn to satisfy the necessity criterion through tautological shortcuts rather than genuine reasoning. This asymmetry holds across different logic types, datasets, and training configurations, suggesting that structural proxies for reasoning quality are fundamentally vulnerable to gaming when optimized directly. I need to verify which section label is correct for the ISR collapse finding—the diagnostic section seems to be the right reference based on how it's cited elsewhere in the paper, so I should use \S\ref{sec:diagnostic} rather than \S\ref{sec:method}.

Now I'm reconsidering whether to mention GRPO explicitly in the hook. The task emphasizes highlighting the counterintuitive finding about GRPO's high performance despite structural degradation, but the introduction currently uses generic language about reinforcement learning. Adding GRPO to the opening would be more specific and directly address the task requirement, though it might narrow the scope too much for an introductory sentence.

My revised hook captures the core paradox—a neurosymbolic reasoner achieving rising proof rates while its internal proof structure deteriorates—which implicitly conveys the RL/GRPO finding without naming it outright. This feels like the right balance for the paper's opening.

Now I'm going back to reconsider Edit 2 at line 18, where I need to think through how to compress the statement about leave-one-out ablation being standard versus our novel empirical contribution. I'm trying to strike the right balance here—acknowledging that leave-one-out ablation is established work while clarifying what's novel about applying it to neurosymbolic systems. The challenge is avoiding pre-stating the findings about reward gaming while still hinting at the empirical contribution. Let me refocus the sentence on the systematic application itself and let the later sections carry the implications. I'm seeing how a neurosymbolic reasoner can improve its proof rate while the actual reasoning structure degrades—the problem is that evaluation relies on a single metric: whether the formalization proves. This treats all successful proofs identically, so a shortcut that embeds the conclusion directly gets rewarded the same as genuine derivation. Under reinforcement learning, this becomes exploitable; the optimizer finds any loophole the reward doesn't explicitly penalize, and execution feedback won't catch structural shortcuts.

For the second edit, I'm noting that leave-one-out ablation is well-established in the literature, but the key insight here is empirical—the same structural property that makes it useful as a diagnostic tool also makes it vulnerable to gaming when used as a reward signal. Applied post-hoc, ISR exposes a structural collapse hidden from prove rate: as execution scores climb, component necessity drops to near zero (Figure~\ref{fig:training-isr-curves}; \S\ref{sec:diagnostic}). The asymmetry persists across logic types, dataset families, reward doses, and random seeds in our Qwen3-4B experiments, suggesting that structural proxies for reasoning quality are easier to diagnose than to optimize. The problem is that execution feedback alone can't distinguish between genuine reasoning and shortcuts—a formalization that just copies the conclusion gets the same reward as one that actually derives it. Under reinforcement learning, this becomes a real vulnerability that optimizers will exploit. Current neurosymbolic systems and their RL variants only check if proofs execute correctly, with no way to diagnose whether individual components actually contribute to the reasoning, and while process reward models offer more granularity, they still require...

I'm proposing Solver Trace Ablation as an annotation-free diagnostic that tests component necessity by removing each part of a formalization one at a time and checking if the proof still succeeds—the fraction of components whose removal breaks the proof becomes the Intensional Structural Reward, ranging from 1 (every component necessary) to 0 (proof works regardless of what's removed).

While leave-one-out ablation itself is well-established, the key insight is applying it systematically to neurosymbolic systems, which exposes a diagnostic-optimization mismatch. Looking at the training curves across different reward conditions, I can see that the execution-only baseline collapses to near-zero ISR, confirming that the formalization degenerates structurally, though the plateau around 0.5 appears to be an artifact of the two-component setup.

The interesting tension emerges when I examine what happens with the ISR metric itself: when applied post-hoc, it reveals a collapse in component necessity that the prove rate alone would miss—as execution scores improve, the individual components become nearly redundant. But this same leave-one-out structure that makes ISR diagnostic also creates a vulnerability to Goodhart's law, where optimizing directly on the metric causes it to lose its meaning through gaming behavior.

Across my Qwen3-4B experiments with different logic types, datasets, and reward configurations, I'm seeing this asymmetry hold consistently: it's much easier to observe structural proxies for reasoning quality than to actually optimize toward them without the metric collapsing. The core contributions here are establishing STA as a diagnostic framework with the ISR metric and a taxonomy of failure modes, plus empirically demonstrating how the Goodhart effect manifests when ISR shifts from observation to optimization. I'm fixing the em-dash formatting in LaTeX and adjusting the punctuation between related clauses—using a semicolon instead of a period to tighten the connection between the optimizer's behavior and the vulnerability it creates. Now I need to carefully match the exact strings in the file to apply these edits correctly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0cf4b583-8eb2-4877-b24a-53b049f91d88",
  "uuid": "05bc6cf5-ed7e-45d3-935d-2490d31464ec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016t6ZLCYEeF9hFAkMpbnAqC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1359,
      "cache_read_input_tokens": 26779,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1359
      },
      "output_tokens": 10,
      "service_tier": "standard",
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

Now let me apply the four edits to tighten the introduction.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0cf4b583-8eb2-4877-b24a-53b049f91d88",
  "uuid": "221dce8a-9840-40b7-8818-59c6d94157fc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016t6ZLCYEeF9hFAkMpbnAqC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1359,
      "cache_read_input_tokens": 26779,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1359
      },
      "output_tokens": 10,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Edit · `toolu_014KZ9jWjS1pJB38JEkkwe2c`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex",
  "old_string": "Neurosymbolic reasoning pipelines evaluate success by a single criterion: whether the generated formalization proves under a formal solver.\nThis treats all proofs as equal: a formalization that embeds the conclusion verbatim among its premises receives the same reward as one that derives it through genuine reasoning.\nUnder reinforcement learning, this indifference becomes an active vulnerability~\\citep{geirhos2020shortcut}. The optimizer exploits any shortcut the reward fails to penalize~\\citep{skalse-reward-hacking, reward-hacking-survey}, and execution feedback provides no signal against structural shortcuts.",
  "new_string": "A neurosymbolic reasoner can achieve rising prove rate while the internal structure of its proofs collapses entirely.\nThe root cause is evaluation by a single criterion---whether the generated formalization proves under a formal solver---which treats all proofs as equal: a formalization that embeds the conclusion verbatim among its premises receives the same reward as one that derives it through genuine reasoning.\nUnder reinforcement learning, this indifference becomes an active vulnerability~\\citep{geirhos2020shortcut}; the optimizer exploits any shortcut the reward fails to penalize~\\citep{skalse-reward-hacking, reward-hacking-survey}, and execution feedback provides no signal against structural shortcuts."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0cf4b583-8eb2-4877-b24a-53b049f91d88",
  "uuid": "8009087c-620a-4f30-945f-af580f560046",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016t6ZLCYEeF9hFAkMpbnAqC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1359,
      "cache_read_input_tokens": 26779,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1359
      },
      "output_tokens": 10,
      "service_tier": "standard",
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

_source line 10 · 2026-05-22T18:50:00.430Z_

<details><summary>↩ Tool result · `toolu_014KZ9jWjS1pJB38JEkkwe2c`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0cf4b583-8eb2-4877-b24a-53b049f91d88",
  "uuid": "448c2a72-eff1-46ca-bdf7-ecfbd4506d75",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex",
    "oldString": "Neurosymbolic reasoning pipelines evaluate success by a single criterion: whether the generated formalization proves under a formal solver.\nThis treats all proofs as equal: a formalization that embeds the conclusion verbatim among its premises receives the same reward as one that derives it through genuine reasoning.\nUnder reinforcement learning, this indifference becomes an active vulnerability~\\citep{geirhos2020shortcut}. The optimizer exploits any shortcut the reward fails to penalize~\\citep{skalse-reward-hacking, reward-hacking-survey}, and execution feedback provides no signal against structural shortcuts.",
    "newString": "A neurosymbolic reasoner can achieve rising prove rate while the internal structure of its proofs collapses entirely.\nThe root cause is evaluation by a single criterion---whether the generated formalization proves under a formal solver---which treats all proofs as equal: a formalization that embeds the conclusion verbatim among its premises receives the same reward as one that derives it through genuine reasoning.\nUnder reinforcement learning, this indifference becomes an active vulnerability~\\citep{geirhos2020shortcut}; the optimizer exploits any shortcut the reward fails to penalize~\\citep{skalse-reward-hacking, reward-hacking-survey}, and execution feedback provides no signal against structural shortcuts.",
    "originalFile": "\\section{Introduction}\n\\label{sec:introduction}\n\nNeurosymbolic reasoning pipelines evaluate success by a single criterion: whether the generated formalization proves under a formal solver.\nThis treats all proofs as equal: a formalization that embeds the conclusion verbatim among its premises receives the same reward as one that derives it through genuine reasoning.\nUnder reinforcement learning, this indifference becomes an active vulnerability~\\citep{geirhos2020shortcut}. The optimizer exploits any shortcut the reward fails to penalize~\\citep{skalse-reward-hacking, reward-hacking-survey}, and execution feedback provides no signal against structural shortcuts.\n\n\\paragraph{The evaluation gap.}\nNeurosymbolic formalizers~\\citep{logic-lm, linc, satlm} and RL-trained variants~\\citep{mellgren-prolog-grpo, logic-rl, deepseekmath} rely on execution accuracy alone, with no diagnostic for whether individual components contribute to the proof.\nProcess reward models~\\citep{lightman-verify-step, math-shepherd} offer finer granularity but require expensive step-level annotations that do not transfer to arbitrary solver-backed settings.\nInference-time gaming detection~\\citep{kim-game-formalization, bondarenko-spec-gaming} addresses a complementary problem but offers no training-time diagnostic.\nWhat is missing is an annotation-free method for testing \\emph{component necessity} in neurosymbolic outputs.\n\n\\paragraph{Component necessity testing.}\nWe address this gap with \\emph{Solver Trace Ablation} (STA), a diagnostic that tests whether each component of a formalization is necessary for proof success.\nFor each proved output, STA removes components one at a time and re-runs the solver; the fraction whose removal breaks the proof yields the \\emph{Intensional Structural Reward} (ISR).\nA formalization where every component is necessary receives $\\text{ISR}{=}1$; one that proves regardless of which component is removed receives $\\text{ISR}{=}0$.\nLeave-one-out ablation itself is standard~\\citep{demillo1978, jia-harman-survey}; our contribution is the empirical finding that the same structure making ISR informative as a diagnostic also makes it gameable as a reward.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.95\\columnwidth]{figures/fig5_training_isr_curves.pdf}\n\\caption{ISR training trajectories across reward conditions (proved samples only, rolling $w{=}20$). Exec-only collapses to $\\text{ISR}{\\approx}0$, confirming structural degeneration (\\S\\ref{sec:diagnostic}); the ${\\sim}0.5$ plateau is an $n{=}2$ artifact. ISR $\\beta{=}0.1$ seeds rise toward $\\text{ISR}{\\approx}1$ via TS gaming (Goodhart effect, \\S\\ref{sec:goodhart}); random remains low.}\n\\label{fig:training-isr-curves}\n\\end{figure}\n\n\\paragraph{The observe-vs-optimize asymmetry.}\nApplied post-hoc, ISR exposes a structural collapse hidden from prove rate (Figure~\\ref{fig:training-isr-curves}): as execution scores climb, component necessity collapses (per-sample mode classification, rather than the aggregate ISR scalar, provides the primary diagnostic evidence; \\S\\ref{sec:method}), revealing that high prove rate coexists with near-complete structural degeneration.\nYet the same LOO structure that makes ISR diagnostic also creates a Goodhart vulnerability~\\citep{manheim-goodhart-taxonomy, karwowski-goodhart-rl, gao-reward-overoptimization}: tautological formalizations ($P{\\to}P$) satisfy the necessity criterion by construction, so when ISR is repurposed as a training reward, the model learns to game the diagnostic rather than the task.\nIn this setting, the asymmetry persists across logic types, dataset families, reward doses, and random seeds: structural proxies for reasoning quality are easier to observe than to optimize.\n\n\\paragraph{Contributions.}\nIn this Qwen3-4B case study across two logic types, two dataset families, and multiple reward conditions, we contribute:\n(\\textbf{C1})~STA as a diagnostic framework for neurosymbolic reasoning, including the ISR metric, an eight-mode hacking taxonomy, and a cross-domain evaluation protocol (\\S\\ref{sec:diagnostic});\n(\\textbf{C2})~empirical characterization of a Goodhart effect when ISR is repurposed as a training reward, with controls ruling out confounds (\\S\\ref{sec:goodhart});\n(\\textbf{C3})~cross-logic and cross-dataset evidence documenting the observe-vs-optimize asymmetry (\\S\\ref{sec:crossdomain}).\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 9,
        "newStart": 1,
        "newLines": 9,
        "lines": [
          " \\section{Introduction}",
          " \\label{sec:introduction}",
          " ",
          "-Neurosymbolic reasoning pipelines evaluate success by a single criterion: whether the generated formalization proves under a formal solver.",
          "-This treats all proofs as equal: a formalization that embeds the conclusion verbatim among its premises receives the same reward as one that derives it through genuine reasoning.",
          "-Under reinforcement learning, this indifference becomes an active vulnerability~\\citep{geirhos2020shortcut}. The optimizer exploits any shortcut the reward fails to penalize~\\citep{skalse-reward-hacking, reward-hacking-survey}, and execution feedback provides no signal against structural shortcuts.",
          "+A neurosymbolic reasoner can achieve rising prove rate while the internal structure of its proofs collapses entirely.",
          "+The root cause is evaluation by a single criterion---whether the generated formalization proves under a formal solver---which treats all proofs as equal: a formalization that embeds the conclusion verbatim among its premises receives the same reward as one that derives it through genuine reasoning.",
          "+Under reinforcement learning, this indifference becomes an active vulnerability~\\citep{geirhos2020shortcut}; the optimizer exploits any shortcut the reward fails to penalize~\\citep{skalse-reward-hacking, reward-hacking-survey}, and execution feedback provides no signal against structural shortcuts.",
          " ",
          " \\paragraph{The evaluation gap.}",
          " Neurosymbolic formalizers~\\citep{logic-lm, linc, satlm} and RL-trained variants~\\citep{mellgren-prolog-grpo, logic-rl, deepseekmath} rely on execution accuracy alone, with no diagnostic for whether individual components contribute to the proof."
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

_source line 11_

<details open><summary>🔧 Tool call — Edit · `toolu_01TJGyijfU71ueRh51Y7fJXd`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex",
  "old_string": "Leave-one-out ablation itself is standard~\\citep{demillo1978, jia-harman-survey}; our contribution is the empirical finding that the same structure making ISR informative as a diagnostic also makes it gameable as a reward.",
  "new_string": "Leave-one-out ablation itself is standard~\\citep{demillo1978, jia-harman-survey}; our contribution is its systematic application to neurosymbolic outputs, where it reveals a diagnostic--optimization asymmetry (\\S\\ref{sec:diagnostic}--\\ref{sec:goodhart})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0cf4b583-8eb2-4877-b24a-53b049f91d88",
  "uuid": "1eccb569-9506-4cca-87b5-82f1cb6d7181",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ArMszDbSWdyV8wH1Gyb4p7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10065,
      "cache_read_input_tokens": 28138,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10065
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

_source line 12 · 2026-05-22T18:50:10.157Z_

<details><summary>↩ Tool result · `toolu_01TJGyijfU71ueRh51Y7fJXd`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0cf4b583-8eb2-4877-b24a-53b049f91d88",
  "uuid": "68dec65d-8574-4165-b2fa-f7fe5d1f6466",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex",
    "oldString": "Leave-one-out ablation itself is standard~\\citep{demillo1978, jia-harman-survey}; our contribution is the empirical finding that the same structure making ISR informative as a diagnostic also makes it gameable as a reward.",
    "newString": "Leave-one-out ablation itself is standard~\\citep{demillo1978, jia-harman-survey}; our contribution is its systematic application to neurosymbolic outputs, where it reveals a diagnostic--optimization asymmetry (\\S\\ref{sec:diagnostic}--\\ref{sec:goodhart}).",
    "originalFile": "\\section{Introduction}\n\\label{sec:introduction}\n\nA neurosymbolic reasoner can achieve rising prove rate while the internal structure of its proofs collapses entirely.\nThe root cause is evaluation by a single criterion---whether the generated formalization proves under a formal solver---which treats all proofs as equal: a formalization that embeds the conclusion verbatim among its premises receives the same reward as one that derives it through genuine reasoning.\nUnder reinforcement learning, this indifference becomes an active vulnerability~\\citep{geirhos2020shortcut}; the optimizer exploits any shortcut the reward fails to penalize~\\citep{skalse-reward-hacking, reward-hacking-survey}, and execution feedback provides no signal against structural shortcuts.\n\n\\paragraph{The evaluation gap.}\nNeurosymbolic formalizers~\\citep{logic-lm, linc, satlm} and RL-trained variants~\\citep{mellgren-prolog-grpo, logic-rl, deepseekmath} rely on execution accuracy alone, with no diagnostic for whether individual components contribute to the proof.\nProcess reward models~\\citep{lightman-verify-step, math-shepherd} offer finer granularity but require expensive step-level annotations that do not transfer to arbitrary solver-backed settings.\nInference-time gaming detection~\\citep{kim-game-formalization, bondarenko-spec-gaming} addresses a complementary problem but offers no training-time diagnostic.\nWhat is missing is an annotation-free method for testing \\emph{component necessity} in neurosymbolic outputs.\n\n\\paragraph{Component necessity testing.}\nWe address this gap with \\emph{Solver Trace Ablation} (STA), a diagnostic that tests whether each component of a formalization is necessary for proof success.\nFor each proved output, STA removes components one at a time and re-runs the solver; the fraction whose removal breaks the proof yields the \\emph{Intensional Structural Reward} (ISR).\nA formalization where every component is necessary receives $\\text{ISR}{=}1$; one that proves regardless of which component is removed receives $\\text{ISR}{=}0$.\nLeave-one-out ablation itself is standard~\\citep{demillo1978, jia-harman-survey}; our contribution is the empirical finding that the same structure making ISR informative as a diagnostic also makes it gameable as a reward.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.95\\columnwidth]{figures/fig5_training_isr_curves.pdf}\n\\caption{ISR training trajectories across reward conditions (proved samples only, rolling $w{=}20$). Exec-only collapses to $\\text{ISR}{\\approx}0$, confirming structural degeneration (\\S\\ref{sec:diagnostic}); the ${\\sim}0.5$ plateau is an $n{=}2$ artifact. ISR $\\beta{=}0.1$ seeds rise toward $\\text{ISR}{\\approx}1$ via TS gaming (Goodhart effect, \\S\\ref{sec:goodhart}); random remains low.}\n\\label{fig:training-isr-curves}\n\\end{figure}\n\n\\paragraph{The observe-vs-optimize asymmetry.}\nApplied post-hoc, ISR exposes a structural collapse hidden from prove rate (Figure~\\ref{fig:training-isr-curves}): as execution scores climb, component necessity collapses (per-sample mode classification, rather than the aggregate ISR scalar, provides the primary diagnostic evidence; \\S\\ref{sec:method}), revealing that high prove rate coexists with near-complete structural degeneration.\nYet the same LOO structure that makes ISR diagnostic also creates a Goodhart vulnerability~\\citep{manheim-goodhart-taxonomy, karwowski-goodhart-rl, gao-reward-overoptimization}: tautological formalizations ($P{\\to}P$) satisfy the necessity criterion by construction, so when ISR is repurposed as a training reward, the model learns to game the diagnostic rather than the task.\nIn this setting, the asymmetry persists across logic types, dataset families, reward doses, and random seeds: structural proxies for reasoning quality are easier to observe than to optimize.\n\n\\paragraph{Contributions.}\nIn this Qwen3-4B case study across two logic types, two dataset families, and multiple reward conditions, we contribute:\n(\\textbf{C1})~STA as a diagnostic framework for neurosymbolic reasoning, including the ISR metric, an eight-mode hacking taxonomy, and a cross-domain evaluation protocol (\\S\\ref{sec:diagnostic});\n(\\textbf{C2})~empirical characterization of a Goodhart effect when ISR is repurposed as a training reward, with controls ruling out confounds (\\S\\ref{sec:goodhart});\n(\\textbf{C3})~cross-logic and cross-dataset evidence documenting the observe-vs-optimize asymmetry (\\S\\ref{sec:crossdomain}).\n",
    "structuredPatch": [
      {
        "oldStart": 15,
        "oldLines": 7,
        "newStart": 15,
        "newLines": 7,
        "lines": [
          " We address this gap with \\emph{Solver Trace Ablation} (STA), a diagnostic that tests whether each component of a formalization is necessary for proof success.",
          " For each proved output, STA removes components one at a time and re-runs the solver; the fraction whose removal breaks the proof yields the \\emph{Intensional Structural Reward} (ISR).",
          " A formalization where every component is necessary receives $\\text{ISR}{=}1$; one that proves regardless of which component is removed receives $\\text{ISR}{=}0$.",
          "-Leave-one-out ablation itself is standard~\\citep{demillo1978, jia-harman-survey}; our contribution is the empirical finding that the same structure making ISR informative as a diagnostic also makes it gameable as a reward.",
          "+Leave-one-out ablation itself is standard~\\citep{demillo1978, jia-harman-survey}; our contribution is its systematic application to neurosymbolic outputs, where it reveals a diagnostic--optimization asymmetry (\\S\\ref{sec:diagnostic}--\\ref{sec:goodhart}).",
          " ",
          " \\begin{figure}[t]",
          " \\centering"
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

_source line 13_

<details open><summary>🔧 Tool call — Edit · `toolu_014GAvxyjjMZvALAryw6JyTa`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex",
  "old_string": "Applied post-hoc, ISR exposes a structural collapse hidden from prove rate (Figure~\\ref{fig:training-isr-curves}): as execution scores climb, component necessity collapses (per-sample mode classification, rather than the aggregate ISR scalar, provides the primary diagnostic evidence; \\S\\ref{sec:method}), revealing that high prove rate coexists with near-complete structural degeneration.",
  "new_string": "Applied post-hoc, ISR exposes a collapse hidden from prove rate: as execution scores climb, component necessity drops to near zero (Figure~\\ref{fig:training-isr-curves}; \\S\\ref{sec:diagnostic})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0cf4b583-8eb2-4877-b24a-53b049f91d88",
  "uuid": "21e08a1c-d0bb-4cf3-ab59-ffcea715c748",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SuzSVPB64XgS6NLepgYvfX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 325,
      "cache_read_input_tokens": 38203,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 325
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

_source line 14 · 2026-05-22T18:50:17.041Z_

<details><summary>↩ Tool result · `toolu_014GAvxyjjMZvALAryw6JyTa`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0cf4b583-8eb2-4877-b24a-53b049f91d88",
  "uuid": "bb990713-4190-4d1d-a61b-87483116221f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex",
    "oldString": "Applied post-hoc, ISR exposes a structural collapse hidden from prove rate (Figure~\\ref{fig:training-isr-curves}): as execution scores climb, component necessity collapses (per-sample mode classification, rather than the aggregate ISR scalar, provides the primary diagnostic evidence; \\S\\ref{sec:method}), revealing that high prove rate coexists with near-complete structural degeneration.",
    "newString": "Applied post-hoc, ISR exposes a collapse hidden from prove rate: as execution scores climb, component necessity drops to near zero (Figure~\\ref{fig:training-isr-curves}; \\S\\ref{sec:diagnostic}).",
    "originalFile": "\\section{Introduction}\n\\label{sec:introduction}\n\nA neurosymbolic reasoner can achieve rising prove rate while the internal structure of its proofs collapses entirely.\nThe root cause is evaluation by a single criterion---whether the generated formalization proves under a formal solver---which treats all proofs as equal: a formalization that embeds the conclusion verbatim among its premises receives the same reward as one that derives it through genuine reasoning.\nUnder reinforcement learning, this indifference becomes an active vulnerability~\\citep{geirhos2020shortcut}; the optimizer exploits any shortcut the reward fails to penalize~\\citep{skalse-reward-hacking, reward-hacking-survey}, and execution feedback provides no signal against structural shortcuts.\n\n\\paragraph{The evaluation gap.}\nNeurosymbolic formalizers~\\citep{logic-lm, linc, satlm} and RL-trained variants~\\citep{mellgren-prolog-grpo, logic-rl, deepseekmath} rely on execution accuracy alone, with no diagnostic for whether individual components contribute to the proof.\nProcess reward models~\\citep{lightman-verify-step, math-shepherd} offer finer granularity but require expensive step-level annotations that do not transfer to arbitrary solver-backed settings.\nInference-time gaming detection~\\citep{kim-game-formalization, bondarenko-spec-gaming} addresses a complementary problem but offers no training-time diagnostic.\nWhat is missing is an annotation-free method for testing \\emph{component necessity} in neurosymbolic outputs.\n\n\\paragraph{Component necessity testing.}\nWe address this gap with \\emph{Solver Trace Ablation} (STA), a diagnostic that tests whether each component of a formalization is necessary for proof success.\nFor each proved output, STA removes components one at a time and re-runs the solver; the fraction whose removal breaks the proof yields the \\emph{Intensional Structural Reward} (ISR).\nA formalization where every component is necessary receives $\\text{ISR}{=}1$; one that proves regardless of which component is removed receives $\\text{ISR}{=}0$.\nLeave-one-out ablation itself is standard~\\citep{demillo1978, jia-harman-survey}; our contribution is its systematic application to neurosymbolic outputs, where it reveals a diagnostic--optimization asymmetry (\\S\\ref{sec:diagnostic}--\\ref{sec:goodhart}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.95\\columnwidth]{figures/fig5_training_isr_curves.pdf}\n\\caption{ISR training trajectories across reward conditions (proved samples only, rolling $w{=}20$). Exec-only collapses to $\\text{ISR}{\\approx}0$, confirming structural degeneration (\\S\\ref{sec:diagnostic}); the ${\\sim}0.5$ plateau is an $n{=}2$ artifact. ISR $\\beta{=}0.1$ seeds rise toward $\\text{ISR}{\\approx}1$ via TS gaming (Goodhart effect, \\S\\ref{sec:goodhart}); random remains low.}\n\\label{fig:training-isr-curves}\n\\end{figure}\n\n\\paragraph{The observe-vs-optimize asymmetry.}\nApplied post-hoc, ISR exposes a structural collapse hidden from prove rate (Figure~\\ref{fig:training-isr-curves}): as execution scores climb, component necessity collapses (per-sample mode classification, rather than the aggregate ISR scalar, provides the primary diagnostic evidence; \\S\\ref{sec:method}), revealing that high prove rate coexists with near-complete structural degeneration.\nYet the same LOO structure that makes ISR diagnostic also creates a Goodhart vulnerability~\\citep{manheim-goodhart-taxonomy, karwowski-goodhart-rl, gao-reward-overoptimization}: tautological formalizations ($P{\\to}P$) satisfy the necessity criterion by construction, so when ISR is repurposed as a training reward, the model learns to game the diagnostic rather than the task.\nIn this setting, the asymmetry persists across logic types, dataset families, reward doses, and random seeds: structural proxies for reasoning quality are easier to observe than to optimize.\n\n\\paragraph{Contributions.}\nIn this Qwen3-4B case study across two logic types, two dataset families, and multiple reward conditions, we contribute:\n(\\textbf{C1})~STA as a diagnostic framework for neurosymbolic reasoning, including the ISR metric, an eight-mode hacking taxonomy, and a cross-domain evaluation protocol (\\S\\ref{sec:diagnostic});\n(\\textbf{C2})~empirical characterization of a Goodhart effect when ISR is repurposed as a training reward, with controls ruling out confounds (\\S\\ref{sec:goodhart});\n(\\textbf{C3})~cross-logic and cross-dataset evidence documenting the observe-vs-optimize asymmetry (\\S\\ref{sec:crossdomain}).\n",
    "structuredPatch": [
      {
        "oldStart": 25,
        "oldLines": 7,
        "newStart": 25,
        "newLines": 7,
        "lines": [
          " \\end{figure}",
          " ",
          " \\paragraph{The observe-vs-optimize asymmetry.}",
          "-Applied post-hoc, ISR exposes a structural collapse hidden from prove rate (Figure~\\ref{fig:training-isr-curves}): as execution scores climb, component necessity collapses (per-sample mode classification, rather than the aggregate ISR scalar, provides the primary diagnostic evidence; \\S\\ref{sec:method}), revealing that high prove rate coexists with near-complete structural degeneration.",
          "+Applied post-hoc, ISR exposes a collapse hidden from prove rate: as execution scores climb, component necessity drops to near zero (Figure~\\ref{fig:training-isr-curves}; \\S\\ref{sec:diagnostic}).",
          " Yet the same LOO structure that makes ISR diagnostic also creates a Goodhart vulnerability~\\citep{manheim-goodhart-taxonomy, karwowski-goodhart-rl, gao-reward-overoptimization}: tautological formalizations ($P{\\to}P$) satisfy the necessity criterion by construction, so when ISR is repurposed as a training reward, the model learns to game the diagnostic rather than the task.",
          " In this setting, the asymmetry persists across logic types, dataset families, reward doses, and random seeds: structural proxies for reasoning quality are easier to observe than to optimize.",
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

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Edit · `toolu_01TgtWewa7H2HN1XLnkrmHmZ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex",
  "old_string": "In this setting, the asymmetry persists across logic types, dataset families, reward doses, and random seeds: structural proxies for reasoning quality are easier to observe than to optimize.",
  "new_string": "In our Qwen3-4B experiments, the asymmetry persists across logic types, dataset families, reward doses, and random seeds, suggesting that structural proxies for reasoning quality are easier to observe than to optimize."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0cf4b583-8eb2-4877-b24a-53b049f91d88",
  "uuid": "29f1cdc1-8e68-49b1-897d-a42eeb2b70f0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011Xea9M4jZ5ByL82Q9eGJgg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 340,
      "cache_read_input_tokens": 38528,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 340
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

_source line 16 · 2026-05-22T18:50:22.081Z_

<details><summary>↩ Tool result · `toolu_01TgtWewa7H2HN1XLnkrmHmZ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0cf4b583-8eb2-4877-b24a-53b049f91d88",
  "uuid": "af7de99b-14c7-4f66-bb80-178ec0e49661",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex",
    "oldString": "In this setting, the asymmetry persists across logic types, dataset families, reward doses, and random seeds: structural proxies for reasoning quality are easier to observe than to optimize.",
    "newString": "In our Qwen3-4B experiments, the asymmetry persists across logic types, dataset families, reward doses, and random seeds, suggesting that structural proxies for reasoning quality are easier to observe than to optimize.",
    "originalFile": "\\section{Introduction}\n\\label{sec:introduction}\n\nA neurosymbolic reasoner can achieve rising prove rate while the internal structure of its proofs collapses entirely.\nThe root cause is evaluation by a single criterion---whether the generated formalization proves under a formal solver---which treats all proofs as equal: a formalization that embeds the conclusion verbatim among its premises receives the same reward as one that derives it through genuine reasoning.\nUnder reinforcement learning, this indifference becomes an active vulnerability~\\citep{geirhos2020shortcut}; the optimizer exploits any shortcut the reward fails to penalize~\\citep{skalse-reward-hacking, reward-hacking-survey}, and execution feedback provides no signal against structural shortcuts.\n\n\\paragraph{The evaluation gap.}\nNeurosymbolic formalizers~\\citep{logic-lm, linc, satlm} and RL-trained variants~\\citep{mellgren-prolog-grpo, logic-rl, deepseekmath} rely on execution accuracy alone, with no diagnostic for whether individual components contribute to the proof.\nProcess reward models~\\citep{lightman-verify-step, math-shepherd} offer finer granularity but require expensive step-level annotations that do not transfer to arbitrary solver-backed settings.\nInference-time gaming detection~\\citep{kim-game-formalization, bondarenko-spec-gaming} addresses a complementary problem but offers no training-time diagnostic.\nWhat is missing is an annotation-free method for testing \\emph{component necessity} in neurosymbolic outputs.\n\n\\paragraph{Component necessity testing.}\nWe address this gap with \\emph{Solver Trace Ablation} (STA), a diagnostic that tests whether each component of a formalization is necessary for proof success.\nFor each proved output, STA removes components one at a time and re-runs the solver; the fraction whose removal breaks the proof yields the \\emph{Intensional Structural Reward} (ISR).\nA formalization where every component is necessary receives $\\text{ISR}{=}1$; one that proves regardless of which component is removed receives $\\text{ISR}{=}0$.\nLeave-one-out ablation itself is standard~\\citep{demillo1978, jia-harman-survey}; our contribution is its systematic application to neurosymbolic outputs, where it reveals a diagnostic--optimization asymmetry (\\S\\ref{sec:diagnostic}--\\ref{sec:goodhart}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.95\\columnwidth]{figures/fig5_training_isr_curves.pdf}\n\\caption{ISR training trajectories across reward conditions (proved samples only, rolling $w{=}20$). Exec-only collapses to $\\text{ISR}{\\approx}0$, confirming structural degeneration (\\S\\ref{sec:diagnostic}); the ${\\sim}0.5$ plateau is an $n{=}2$ artifact. ISR $\\beta{=}0.1$ seeds rise toward $\\text{ISR}{\\approx}1$ via TS gaming (Goodhart effect, \\S\\ref{sec:goodhart}); random remains low.}\n\\label{fig:training-isr-curves}\n\\end{figure}\n\n\\paragraph{The observe-vs-optimize asymmetry.}\nApplied post-hoc, ISR exposes a collapse hidden from prove rate: as execution scores climb, component necessity drops to near zero (Figure~\\ref{fig:training-isr-curves}; \\S\\ref{sec:diagnostic}).\nYet the same LOO structure that makes ISR diagnostic also creates a Goodhart vulnerability~\\citep{manheim-goodhart-taxonomy, karwowski-goodhart-rl, gao-reward-overoptimization}: tautological formalizations ($P{\\to}P$) satisfy the necessity criterion by construction, so when ISR is repurposed as a training reward, the model learns to game the diagnostic rather than the task.\nIn this setting, the asymmetry persists across logic types, dataset families, reward doses, and random seeds: structural proxies for reasoning quality are easier to observe than to optimize.\n\n\\paragraph{Contributions.}\nIn this Qwen3-4B case study across two logic types, two dataset families, and multiple reward conditions, we contribute:\n(\\textbf{C1})~STA as a diagnostic framework for neurosymbolic reasoning, including the ISR metric, an eight-mode hacking taxonomy, and a cross-domain evaluation protocol (\\S\\ref{sec:diagnostic});\n(\\textbf{C2})~empirical characterization of a Goodhart effect when ISR is repurposed as a training reward, with controls ruling out confounds (\\S\\ref{sec:goodhart});\n(\\textbf{C3})~cross-logic and cross-dataset evidence documenting the observe-vs-optimize asymmetry (\\S\\ref{sec:crossdomain}).\n",
    "structuredPatch": [
      {
        "oldStart": 27,
        "oldLines": 7,
        "newStart": 27,
        "newLines": 7,
        "lines": [
          " \\paragraph{The observe-vs-optimize asymmetry.}",
          " Applied post-hoc, ISR exposes a collapse hidden from prove rate: as execution scores climb, component necessity drops to near zero (Figure~\\ref{fig:training-isr-curves}; \\S\\ref{sec:diagnostic}).",
          " Yet the same LOO structure that makes ISR diagnostic also creates a Goodhart vulnerability~\\citep{manheim-goodhart-taxonomy, karwowski-goodhart-rl, gao-reward-overoptimization}: tautological formalizations ($P{\\to}P$) satisfy the necessity criterion by construction, so when ISR is repurposed as a training reward, the model learns to game the diagnostic rather than the task.",
          "-In this setting, the asymmetry persists across logic types, dataset families, reward doses, and random seeds: structural proxies for reasoning quality are easier to observe than to optimize.",
          "+In our Qwen3-4B experiments, the asymmetry persists across logic types, dataset families, reward doses, and random seeds, suggesting that structural proxies for reasoning quality are easier to observe than to optimize.",
          " ",
          " \\paragraph{Contributions.}",
          " In this Qwen3-4B case study across two logic types, two dataset families, and multiple reward conditions, we contribute:"
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

_source line 17_

Now copy to the paper/ directory and verify.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0cf4b583-8eb2-4877-b24a-53b049f91d88",
  "uuid": "44f3a102-6877-4ae3-b66e-3ff2ebf945bb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AimGBx47Uu1FS2c2WkVUdZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 280,
      "cache_read_input_tokens": 38868,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 280
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

_source line 18_

<details open><summary>🔧 Tool call — Bash · `toolu_01ScKV8tKJBcqHWci2Vf6UvB`</summary>

```json
{
  "command": "cp /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex",
  "description": "Copy introduction.tex to paper/ directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0cf4b583-8eb2-4877-b24a-53b049f91d88",
  "uuid": "fbe88cf7-5632-4d9d-9fe5-d9b9d8f6ea8e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AimGBx47Uu1FS2c2WkVUdZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 280,
      "cache_read_input_tokens": 38868,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 280
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

_source line 19 · 2026-05-22T18:50:26.515Z_

<details><summary>↩ Tool result · `toolu_01ScKV8tKJBcqHWci2Vf6UvB`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0cf4b583-8eb2-4877-b24a-53b049f91d88",
  "uuid": "ea706bea-53bc-4b25-9c86-19035d1e9373",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Bash · `toolu_012wiKTM2yFDowAUPFe2FRow`</summary>

```json
{
  "command": "diff /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex",
  "description": "Verify two introduction.tex files are identical"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0cf4b583-8eb2-4877-b24a-53b049f91d88",
  "uuid": "1eea8949-5791-464d-8cd7-4d05627f3e9c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J1fKkx9MYz19rWYpYeJKUy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 175,
      "cache_read_input_tokens": 39148,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 175
      },
      "output_tokens": 70,
      "service_tier": "standard",
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

_source line 21 · 2026-05-22T18:50:29.828Z_

<details><summary>↩ Tool result · `toolu_012wiKTM2yFDowAUPFe2FRow`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0cf4b583-8eb2-4877-b24a-53b049f91d88",
  "uuid": "1d471793-3eff-4aa1-8f93-02ac864feef0",
  "tool_use_result": {
    "stdout": "",
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

_source line 22_

<details><summary>Logged reasoning block</summary>

```text
Files are identical. Let me verify the final result by reading the edited file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0cf4b583-8eb2-4877-b24a-53b049f91d88",
  "uuid": "cff9ed5e-15d4-41f6-bda7-155a68880bb1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TqEnAMZ47dwtY8mtu92VFW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 269,
      "cache_read_input_tokens": 39323,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 269
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

_source line 23_

两文件完全一致。验证最终结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0cf4b583-8eb2-4877-b24a-53b049f91d88",
  "uuid": "058861f8-1147-4185-a701-3030941dbca3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TqEnAMZ47dwtY8mtu92VFW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 269,
      "cache_read_input_tokens": 39323,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 269
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

_source line 24_

<details open><summary>🔧 Tool call — Read · `toolu_017DyLDCFe1vw1wXFcnx8J59`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0cf4b583-8eb2-4877-b24a-53b049f91d88",
  "uuid": "d9004918-766a-4778-8d6b-a516af0ca94f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TqEnAMZ47dwtY8mtu92VFW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 269,
      "cache_read_input_tokens": 39323,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 269
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

_source line 25 · 2026-05-22T18:50:33.321Z_

<details><summary>↩ Tool result · `toolu_017DyLDCFe1vw1wXFcnx8J59`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	A neurosymbolic reasoner can achieve rising prove rate while the internal structure of its proofs collapses entirely.
5	The root cause is evaluation by a single criterion---whether the generated formalization proves under a formal solver---which treats all proofs as equal: a formalization that embeds the conclusion verbatim among its premises receives the same reward as one that derives it through genuine reasoning.
6	Under reinforcement learning, this indifference becomes an active vulnerability~\citep{geirhos2020shortcut}; the optimizer exploits any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}, and execution feedback provides no signal against structural shortcuts.
7	
8	\paragraph{The evaluation gap.}
9	Neurosymbolic formalizers~\citep{logic-lm, linc, satlm} and RL-trained variants~\citep{mellgren-prolog-grpo, logic-rl, deepseekmath} rely on execution accuracy alone, with no diagnostic for whether individual components contribute to the proof.
10	Process reward models~\citep{lightman-verify-step, math-shepherd} offer finer granularity but require expensive step-level annotations that do not transfer to arbitrary solver-backed settings.
11	Inference-time gaming detection~\citep{kim-game-formalization, bondarenko-spec-gaming} addresses a complementary problem but offers no training-time diagnostic.
12	What is missing is an annotation-free method for testing \emph{component necessity} in neurosymbolic outputs.
13	
14	\paragraph{Component necessity testing.}
15	We address this gap with \emph{Solver Trace Ablation} (STA), a diagnostic that tests whether each component of a formalization is necessary for proof success.
16	For each proved output, STA removes components one at a time and re-runs the solver; the fraction whose removal breaks the proof yields the \emph{Intensional Structural Reward} (ISR).
17	A formalization where every component is necessary receives $\text{ISR}{=}1$; one that proves regardless of which component is removed receives $\text{ISR}{=}0$.
18	Leave-one-out ablation itself is standard~\citep{demillo1978, jia-harman-survey}; our contribution is its systematic application to neurosymbolic outputs, where it reveals a diagnostic--optimization asymmetry (\S\ref{sec:diagnostic}--\ref{sec:goodhart}).
19	
20	\begin{figure}[t]
21	\centering
22	\includegraphics[width=0.95\columnwidth]{figures/fig5_training_isr_curves.pdf}
23	\caption{ISR training trajectories across reward conditions (proved samples only, rolling $w{=}20$). Exec-only collapses to $\text{ISR}{\approx}0$, confirming structural degeneration (\S\ref{sec:diagnostic}); the ${\sim}0.5$ plateau is an $n{=}2$ artifact. ISR $\beta{=}0.1$ seeds rise toward $\text{ISR}{\approx}1$ via TS gaming (Goodhart effect, \S\ref{sec:goodhart}); random remains low.}
24	\label{fig:training-isr-curves}
25	\end{figure}
26	
27	\paragraph{The observe-vs-optimize asymmetry.}
28	Applied post-hoc, ISR exposes a collapse hidden from prove rate: as execution scores climb, component necessity drops to near zero (Figure~\ref{fig:training-isr-curves}; \S\ref{sec:diagnostic}).
29	Yet the same LOO structure that makes ISR diagnostic also creates a Goodhart vulnerability~\citep{manheim-goodhart-taxonomy, karwowski-goodhart-rl, gao-reward-overoptimization}: tautological formalizations ($P{\to}P$) satisfy the necessity criterion by construction, so when ISR is repurposed as a training reward, the model learns to game the diagnostic rather than the task.
30	In our Qwen3-4B experiments, the asymmetry persists across logic types, dataset families, reward doses, and random seeds, suggesting that structural proxies for reasoning quality are easier to observe than to optimize.
31	
32	\paragraph{Contributions.}
33	In this Qwen3-4B case study across two logic types, two dataset families, and multiple reward conditions, we contribute:
34	(\textbf{C1})~STA as a diagnostic framework for neurosymbolic reasoning, including the ISR metric, an eight-mode hacking taxonomy, and a cross-domain evaluation protocol (\S\ref{sec:diagnostic});
35	(\textbf{C2})~empirical characterization of a Goodhart effect when ISR is repurposed as a training reward, with controls ruling out confounds (\S\ref{sec:goodhart});
36	(\textbf{C3})~cross-logic and cross-dataset evidence documenting the observe-vs-optimize asymmetry (\S\ref{sec:crossdomain}).
37	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0cf4b583-8eb2-4877-b24a-53b049f91d88",
  "uuid": "8bd30d1c-15f4-4217-a42a-9b32dfa7a44a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nA neurosymbolic reasoner can achieve rising prove rate while the internal structure of its proofs collapses entirely.\nThe root cause is evaluation by a single criterion---whether the generated formalization proves under a formal solver---which treats all proofs as equal: a formalization that embeds the conclusion verbatim among its premises receives the same reward as one that derives it through genuine reasoning.\nUnder reinforcement learning, this indifference becomes an active vulnerability~\\citep{geirhos2020shortcut}; the optimizer exploits any shortcut the reward fails to penalize~\\citep{skalse-reward-hacking, reward-hacking-survey}, and execution feedback provides no signal against structural shortcuts.\n\n\\paragraph{The evaluation gap.}\nNeurosymbolic formalizers~\\citep{logic-lm, linc, satlm} and RL-trained variants~\\citep{mellgren-prolog-grpo, logic-rl, deepseekmath} rely on execution accuracy alone, with no diagnostic for whether individual components contribute to the proof.\nProcess reward models~\\citep{lightman-verify-step, math-shepherd} offer finer granularity but require expensive step-level annotations that do not transfer to arbitrary solver-backed settings.\nInference-time gaming detection~\\citep{kim-game-formalization, bondarenko-spec-gaming} addresses a complementary problem but offers no training-time diagnostic.\nWhat is missing is an annotation-free method for testing \\emph{component necessity} in neurosymbolic outputs.\n\n\\paragraph{Component necessity testing.}\nWe address this gap with \\emph{Solver Trace Ablation} (STA), a diagnostic that tests whether each component of a formalization is necessary for proof success.\nFor each proved output, STA removes components one at a time and re-runs the solver; the fraction whose removal breaks the proof yields the \\emph{Intensional Structural Reward} (ISR).\nA formalization where every component is necessary receives $\\text{ISR}{=}1$; one that proves regardless of which component is removed receives $\\text{ISR}{=}0$.\nLeave-one-out ablation itself is standard~\\citep{demillo1978, jia-harman-survey}; our contribution is its systematic application to neurosymbolic outputs, where it reveals a diagnostic--optimization asymmetry (\\S\\ref{sec:diagnostic}--\\ref{sec:goodhart}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.95\\columnwidth]{figures/fig5_training_isr_curves.pdf}\n\\caption{ISR training trajectories across reward conditions (proved samples only, rolling $w{=}20$). Exec-only collapses to $\\text{ISR}{\\approx}0$, confirming structural degeneration (\\S\\ref{sec:diagnostic}); the ${\\sim}0.5$ plateau is an $n{=}2$ artifact. ISR $\\beta{=}0.1$ seeds rise toward $\\text{ISR}{\\approx}1$ via TS gaming (Goodhart effect, \\S\\ref{sec:goodhart}); random remains low.}\n\\label{fig:training-isr-curves}\n\\end{figure}\n\n\\paragraph{The observe-vs-optimize asymmetry.}\nApplied post-hoc, ISR exposes a collapse hidden from prove rate: as execution scores climb, component necessity drops to near zero (Figure~\\ref{fig:training-isr-curves}; \\S\\ref{sec:diagnostic}).\nYet the same LOO structure that makes ISR diagnostic also creates a Goodhart vulnerability~\\citep{manheim-goodhart-taxonomy, karwowski-goodhart-rl, gao-reward-overoptimization}: tautological formalizations ($P{\\to}P$) satisfy the necessity criterion by construction, so when ISR is repurposed as a training reward, the model learns to game the diagnostic rather than the task.\nIn our Qwen3-4B experiments, the asymmetry persists across logic types, dataset families, reward doses, and random seeds, suggesting that structural proxies for reasoning quality are easier to observe than to optimize.\n\n\\paragraph{Contributions.}\nIn this Qwen3-4B case study across two logic types, two dataset families, and multiple reward conditions, we contribute:\n(\\textbf{C1})~STA as a diagnostic framework for neurosymbolic reasoning, including the ISR metric, an eight-mode hacking taxonomy, and a cross-domain evaluation protocol (\\S\\ref{sec:diagnostic});\n(\\textbf{C2})~empirical characterization of a Goodhart effect when ISR is repurposed as a training reward, with controls ruling out confounds (\\S\\ref{sec:goodhart});\n(\\textbf{C3})~cross-logic and cross-dataset evidence documenting the observe-vs-optimize asymmetry (\\S\\ref{sec:crossdomain}).\n",
      "numLines": 37,
      "startLine": 1,
      "totalLines": 37
    }
  }
}
```

</details>

---

### Assistant

_source line 26_

---

## 修改清单

### Edit 1: 开篇 hook（L4-6）
**目的**：以反直觉发现开场，而非程序性定义

| | 内容 |
|---|---|
| **Before** | `Neurosymbolic reasoning pipelines evaluate success by a single criterion: whether the generated formalization proves under a formal solver.` / `This treats all proofs as equal: ...` / `Under RL, this indifference becomes an active vulnerability. The optimizer exploits...` |
| **After** | `A neurosymbolic reasoner can achieve rising prove rate while the internal structure of its proofs collapses entirely.` / `The root cause is evaluation by a single criterion---...---which treats all proofs as equal: ...` / `Under RL, this indifference becomes an active vulnerability; the optimizer exploits...` |

变更点：(a) 新增 hook 句直述悖论；(b) 原两句合并为一句用 em-dash 嵌入；(c) 句号改分号连接更紧凑。

### Edit 2: 去冗余——L18 与 L29 重复陈述 Goodhart 发现
**目的**：L18 原文预述了"diagnostic → gameable"，与 ¶4 L29 完全重复。改为 forward reference，让 ¶4 首次揭示该发现。

| | 内容 |
|---|---|
| **Before** | `...our contribution is the empirical finding that the same structure making ISR informative as a diagnostic also makes it gameable as a reward.` |
| **After** | `...our contribution is its systematic application to neurosymbolic outputs, where it reveals a diagnostic--optimization asymmetry (§3--§4).` |

### Edit 3: 压缩 L28——删除冗长括注和三重同义
**目的**：原句有嵌套括注 + "structural collapse"/"component necessity collapses"/"near-complete structural degeneration" 三次说同一件事。

| | 内容 |
|---|---|
| **Before** | `Applied post-hoc, ISR exposes a structural collapse hidden from prove rate (Figure 1): as execution scores climb, component necessity collapses (per-sample mode classification, rather than the aggregate ISR scalar, provides the primary diagnostic evidence; §3), revealing that high prove rate coexists with near-complete structural degeneration.` |
| **After** | `Applied post-hoc, ISR exposes a collapse hidden from prove rate: as execution scores climb, component necessity drops to near zero (Figure 1; §3).` |

### Edit 4: Case study scoping——L30 泛化声明加限定
**目的**：原文 "In this setting" 模糊，末尾断言 "are easier to observe than to optimize" 读起来像普遍定律。

| | 内容 |
|---|---|
| **Before** | `In this setting, the asymmetry persists across logic types, dataset families, reward doses, and random seeds: structural proxies for reasoning quality are easier to observe than to optimize.` |
| **After** | `In our Qwen3-4B experiments, the asymmetry persists across logic types, dataset families, reward doses, and random seeds, suggesting that structural proxies for reasoning quality are easier to observe than to optimize.` |

---

## 未修改的可选改进建议（供 Director 判断）

1. **L11 "complementary problem" 措辞**：`addresses a complementary problem but offers no training-time diagnostic` 中 "complementary problem" 含义模糊（互补的什么 problem？），可改为 `detects gaming at inference time but offers no training-time diagnostic`，更直接。未改是因为现有措辞不影响理解。

2. **Figure caption 密度**：L23-24 的 caption 信息量很大（4 个观察点 + 2 个 section 引用），在 intro 首图中可能让读者 overwhelm。可考虑只保留核心信息（exec-only collapse + ISR gaming），细节留给正文。未改是因为 caption 不在本次任务的 4 项检查范围内。

3. **L4 hook 的 scope 问题**：新 hook "A neurosymbolic reasoner can achieve rising prove rate while..." 是泛指，理论上应说 "In our experiments, a neurosymbolic reasoner..."。但开篇第一句加 scoping 会杀死 hook 效果，且该现象的逻辑基础（execution-only reward 不区分 shortcut）确实是通用的，不只限于 Qwen3-4B。保留为通用表述，让后文（L30, L33）做具体 scoping。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0cf4b583-8eb2-4877-b24a-53b049f91d88",
  "uuid": "1539539e-2d67-432d-b7cd-0e4cd1e42e5d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WHg8fFPwv5Q22sUyoSHTCD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1401,
      "cache_read_input_tokens": 39592,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1401
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

_source line 27_

---

## 修改清单

### Edit 1: 开篇 hook（L4-6）
**目的**：以反直觉发现开场，而非程序性定义

| | 内容 |
|---|---|
| **Before** | `Neurosymbolic reasoning pipelines evaluate success by a single criterion: whether the generated formalization proves under a formal solver.` / `This treats all proofs as equal: ...` / `Under RL, this indifference becomes an active vulnerability. The optimizer exploits...` |
| **After** | `A neurosymbolic reasoner can achieve rising prove rate while the internal structure of its proofs collapses entirely.` / `The root cause is evaluation by a single criterion---...---which treats all proofs as equal: ...` / `Under RL, this indifference becomes an active vulnerability; the optimizer exploits...` |

变更点：(a) 新增 hook 句直述悖论；(b) 原两句合并为一句用 em-dash 嵌入；(c) 句号改分号连接更紧凑。

### Edit 2: 去冗余——L18 与 L29 重复陈述 Goodhart 发现
**目的**：L18 原文预述了"diagnostic → gameable"，与 ¶4 L29 完全重复。改为 forward reference，让 ¶4 首次揭示该发现。

| | 内容 |
|---|---|
| **Before** | `...our contribution is the empirical finding that the same structure making ISR informative as a diagnostic also makes it gameable as a reward.` |
| **After** | `...our contribution is its systematic application to neurosymbolic outputs, where it reveals a diagnostic--optimization asymmetry (§3--§4).` |

### Edit 3: 压缩 L28——删除冗长括注和三重同义
**目的**：原句有嵌套括注 + "structural collapse"/"component necessity collapses"/"near-complete structural degeneration" 三次说同一件事。

| | 内容 |
|---|---|
| **Before** | `Applied post-hoc, ISR exposes a structural collapse hidden from prove rate (Figure 1): as execution scores climb, component necessity collapses (per-sample mode classification, rather than the aggregate ISR scalar, provides the primary diagnostic evidence; §3), revealing that high prove rate coexists with near-complete structural degeneration.` |
| **After** | `Applied post-hoc, ISR exposes a collapse hidden from prove rate: as execution scores climb, component necessity drops to near zero (Figure 1; §3).` |

### Edit 4: Case study scoping——L30 泛化声明加限定
**目的**：原文 "In this setting" 模糊，末尾断言 "are easier to observe than to optimize" 读起来像普遍定律。

| | 内容 |
|---|---|
| **Before** | `In this setting, the asymmetry persists across logic types, dataset families, reward doses, and random seeds: structural proxies for reasoning quality are easier to observe than to optimize.` |
| **After** | `In our Qwen3-4B experiments, the asymmetry persists across logic types, dataset families, reward doses, and random seeds, suggesting that structural proxies for reasoning quality are easier to observe than to optimize.` |

---

## 未修改的可选改进建议（供 Director 判断）

1. **L11 "complementary problem" 措辞**：`addresses a complementary problem but offers no training-time diagnostic` 中 "complementary problem" 含义模糊（互补的什么 problem？），可改为 `detects gaming at inference time but offers no training-time diagnostic`，更直接。未改是因为现有措辞不影响理解。

2. **Figure caption 密度**：L23-24 的 caption 信息量很大（4 个观察点 + 2 个 section 引用），在 intro 首图中可能让读者 overwhelm。可考虑只保留核心信息（exec-only collapse + ISR gaming），细节留给正文。未改是因为 caption 不在本次任务的 4 项检查范围内。

3. **L4 hook 的 scope 问题**：新 hook "A neurosymbolic reasoner can achieve rising prove rate while..." 是泛指，理论上应说 "In our experiments, a neurosymbolic reasoner..."。但开篇第一句加 scoping 会杀死 hook 效果，且该现象的逻辑基础（execution-only reward 不区分 shortcut）确实是通用的，不只限于 Qwen3-4B。保留为通用表述，让后文（L30, L33）做具体 scoping。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 239375,
  "duration_api_ms": 240166,
  "num_turns": 9,
  "stop_reason": "end_turn",
  "session_id": "0cf4b583-8eb2-4877-b24a-53b049f91d88",
  "total_cost_usd": 0.649063,
  "usage": {
    "input_tokens": 11,
    "cache_creation_input_tokens": 29152,
    "cache_read_input_tokens": 300420,
    "output_tokens": 12543,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 29152,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 1234,
        "cache_read_input_tokens": 39592,
        "cache_creation_input_tokens": 1401,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1401
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2948,
      "outputTokens": 15,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.003023,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 11,
      "outputTokens": 12543,
      "cacheReadInputTokens": 300420,
      "cacheCreationInputTokens": 29152,
      "webSearchRequests": 0,
      "costUSD": 0.64604,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "f3f38160-cae6-4852-badb-45fb8653e193"
}
```

</details>

---
