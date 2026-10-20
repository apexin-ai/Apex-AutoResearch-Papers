# analysis r15 bonferroni

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 84
- **Recorded user turns:** 0
- **Tool calls:** 31
- **Original source:** `logs/workers/worker_analysis_r15-bonferroni_20260520T044634.log`
- **Structured JSON:** [`5c08e3c9cc4fd3e8221b.json`](../../sessions/5c/5c08e3c9cc4fd3e8221b.json)

## Before a recorded user message

84 recorded events

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
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
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
  "uuid": "857df5aa-4ff7-43e2-847d-6de4910e8b1b",
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
    "resetsAt": 1779270000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "2b935ce1-d2c5-4bf7-9481-d79320011daf",
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me collect all p-values from the paper's .tex files, then apply Bonferroni correction.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "bd6d8260-a72a-455e-80b0-7e28656ead6b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PwnzaksyARDgn63xKTvEeY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15028,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15028
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

### Assistant

_source line 5_

I'll search all the relevant .tex files for reported p-values and statistical tests.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "e9b7105f-cb8c-41b1-b367-b51261ff50cf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PwnzaksyARDgn63xKTvEeY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15028,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15028
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

_source line 6_

<details open><summary>🔧 Tool call — Grep · `toolu_01SGwvMkmTt3a5zhKGM1BCwy`</summary>

```json
{
  "pattern": "p[\\s=<>]|Fisher|permutation|significant|p-value|\\\\text.?test|McNemar|Wilcoxon|chi.?sq|bootstrap",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "output_mode": "content",
  "-n": true,
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "46a36e38-c55b-47a2-95dd-d4e548bf8aee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PwnzaksyARDgn63xKTvEeY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15028,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15028
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

_source line 7 · 2026-05-20T04:46:48.219Z_

<details><summary>↩ Tool result · `toolu_01SGwvMkmTt3a5zhKGM1BCwy`</summary>

```text
32:\caption{ISR collapse under exec-only GRPO (seed~42). (a) Both metrics on the same $[0,1]$ scale: PR rises 32\%$\to$93\%$\to$96\% while ISR$^*$ falls $0.642{\to}0.132{\to}0.003$ over 100$\to$500$\to$1000 steps; the shaded region shows the growing divergence. (b) Hacking modes progressively replace non-hacking output: by step 1000, CE dominates 100\% of proved samples.}
52:The near-absence of hacking under identical data exposure is consistent with hacking being associated with RL optimization rather than data exposure; a 100-step checkpoint ($\text{PR}{=}32\%$, hacking${\geq}31\%$) partially controls for the PR-level confound (Appendix~\ref{app:100step}).
104:The matched cohort resolves this ambiguity: ISR yields 5/5 TS-dominated seeds versus 0/5 under random control (Fisher $p{=}0.004$), confirming TS as ISR-specific rather than a generic GRPO artifact.
107:The reward gap explains this: TS tautologies receive expected reward ${\geq}1{+}0.5\beta$ (mean empirical $\text{ISR}{=}0.535$) versus ${\sim}1{+}0.26\beta$ for non-hacking proofs (premise-count-matched), creating a persistent gradient toward tautological constructions regardless of dose.
114:Fisher exact test on TS domination yields $\text{OR}{=}\infty$ ($p{=}0.004$, 95\% CI $[2.30, \infty]$, $\text{BF}_{10}{=}77$); Mann-Whitney $U$ on $\text{ISR}^*$: $U{=}25$, $p{=}0.004$, $r{=}1.0$; genuine rates do not differ significantly ($2.3\%$ vs.\ $5.9\%$, $p{=}0.92$, permutation test; Appendix~\ref{app:matched-stats}), with the point estimate consistently favoring Random (corrected 3-seed: ISR $6.1\%$ vs.\ Random $9.5\%$; matched: $2.3\%$ vs.\ $5.9\%$).
166:CE, TS, and PG account for ${>}90\%$ of hacking across ${\geq}3$ seeds each; ISR modestly increases TS probability ($\text{OR}{=}2.84$; Appendix Table~\ref{tab:bootstrap-ci}), but per-seed variance dominates.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "73e30b44-5a0a-49dd-bc86-b85acf0766ff",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "32:\\caption{ISR collapse under exec-only GRPO (seed~42). (a) Both metrics on the same $[0,1]$ scale: PR rises 32\\%$\\to$93\\%$\\to$96\\% while ISR$^*$ falls $0.642{\\to}0.132{\\to}0.003$ over 100$\\to$500$\\to$1000 steps; the shaded region shows the growing divergence. (b) Hacking modes progressively replace non-hacking output: by step 1000, CE dominates 100\\% of proved samples.}\n52:The near-absence of hacking under identical data exposure is consistent with hacking being associated with RL optimization rather than data exposure; a 100-step checkpoint ($\\text{PR}{=}32\\%$, hacking${\\geq}31\\%$) partially controls for the PR-level confound (Appendix~\\ref{app:100step}).\n104:The matched cohort resolves this ambiguity: ISR yields 5/5 TS-dominated seeds versus 0/5 under random control (Fisher $p{=}0.004$), confirming TS as ISR-specific rather than a generic GRPO artifact.\n107:The reward gap explains this: TS tautologies receive expected reward ${\\geq}1{+}0.5\\beta$ (mean empirical $\\text{ISR}{=}0.535$) versus ${\\sim}1{+}0.26\\beta$ for non-hacking proofs (premise-count-matched), creating a persistent gradient toward tautological constructions regardless of dose.\n114:Fisher exact test on TS domination yields $\\text{OR}{=}\\infty$ ($p{=}0.004$, 95\\% CI $[2.30, \\infty]$, $\\text{BF}_{10}{=}77$); Mann-Whitney $U$ on $\\text{ISR}^*$: $U{=}25$, $p{=}0.004$, $r{=}1.0$; genuine rates do not differ significantly ($2.3\\%$ vs.\\ $5.9\\%$, $p{=}0.92$, permutation test; Appendix~\\ref{app:matched-stats}), with the point estimate consistently favoring Random (corrected 3-seed: ISR $6.1\\%$ vs.\\ Random $9.5\\%$; matched: $2.3\\%$ vs.\\ $5.9\\%$).\n166:CE, TS, and PG account for ${>}90\\%$ of hacking across ${\\geq}3$ seeds each; ISR modestly increases TS probability ($\\text{OR}{=}2.84$; Appendix Table~\\ref{tab:bootstrap-ci}), but per-seed variance dominates.",
    "numLines": 6
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Grep · `toolu_01FyeADY4EVkP1UoWERjcAHi`</summary>

```json
{
  "pattern": "p[\\s=<>]|Fisher|permutation|significant|p-value|\\\\text.?test|McNemar|Wilcoxon|chi.?sq|bootstrap",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
  "output_mode": "content",
  "-n": true,
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "205284f3-c27c-47d8-b99f-dcfc12aac88c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PwnzaksyARDgn63xKTvEeY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15028,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15028
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

_source line 9 · 2026-05-20T04:46:49.616Z_

<details><summary>↩ Tool result · `toolu_01FyeADY4EVkP1UoWERjcAHi`</summary>

```text
77:We verify this empirically: Spearman $\rho(\text{ISR}, \text{NLI accuracy}) = -0.049$ ($p = 0.187$, n.s.) from a downstream NLI evaluation on exec-only checkpoint outputs.
96:\caption{Fisher exact tests across conditions. Non-hacking rate reported at 5-seed (primary) and 3-seed with PG+FN corrections (sensitivity); TS comparison at 5-seed (primary) and 3-seed (sensitivity).}
97:\label{tab:bootstrap-ci}
124:To address potential inflation from within-seed dependence, we supplement pooled Fisher exact tests with two seed-aware analyses.
127:Seed-level permutation tests (treating each seed as a single observation, $n{=}5$ per group) yield $p{=}0.28$ (TS) and $p{=}0.26$ (non-hacking), consistent with the severe power limitation of $n{=}5$ (minimum achievable $p{=}0.008$) rather than absence of effect.
185:ISR was designed to \emph{detect} reward gaming of $r_{\text{exec}}$, yet it contains an inherent structural vulnerability: by its LOO definition, single-premise-equals-conclusion constructions receive artificially high ISR ($\text{ISR}{\geq}0.5$; empirically 93\% at $\text{ISR}{=}0.5$, 7\% at $\text{ISR}{=}1.0$; 5-seed ISR $\beta{=}0.1$ pooled TS samples), creating a positive feedback loop once sampled during GRPO rollouts~\citep{karwowski-goodhart-rl, kwa-catastrophic-goodhart}.
225:Tautological & 2-comp $P{=}C$ & $\bullet$ & 0 & 0 & 0 \\
269:After PG reclassification and TS false-negative correction: ISR non-hacking $= 14/231 = 6.06\%$ vs.\ random non-hacking $= 25/262 = 9.5\%$ (Fisher $p{=}0.182$, n.s.; Wilson 95\% CI: ISR [3.6\%, 9.9\%], Random [6.5\%, 13.7\%]).
270:The direction is consistent with ISR-amplified gaming modes (TS, PG) displacing non-hacking output, but the effect is not statistically significant at the conventional $\alpha{=}0.05$ threshold.
300:Since $P \to P$ is trivially provable, this simultaneously maximizes exec reward.
350:Two-component formalizations where the premise and conclusion are identical atomic or simple formulas, yielding a $P \to P$ tautology with minimal token cost.
422:\paragraph{Example (FOL, 1000-step exec-only).}
553:  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.68{\pm}0.47$} & & \makebox[0pt][l]{$0.238{\pm}0.30$} & & & 500-step \\
554:  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.97{\pm}0.02$} & & \makebox[0pt][l]{$0.03{\pm}0.05$} & & \makebox[0pt][l]{$2.1{\pm}3.6$} & 1000-step \\
644:\caption{Training ISR trajectories across reward conditions. ISR $\beta{=}0.1$ seeds rise rapidly toward $\text{ISR}{\approx}1$ (Goodhart gaming via TS tautology); exec-only s44's plateau at ${\sim}0.5$ is an TS-a artifact ($n{=}2$ gives $\text{ISR}{\geq}0.5$ by construction), not non-hacking structural quality; random $\beta{=}0.1$ remains low. The s42 1k-step trace shows ISR eventually saturates at $0.88$ through the same TS mechanism.}
650:ISR$^*=0.642$ at 100 steps $\to$ $0.132$ at 500 steps ($-79.4$\%) $\to$ $0.003$ at 1000 steps ($-99.5$\% from step 100).
652:By step 1000, 94.8\% of proved samples have ISR~$=0$ and the mean component count rises to 18.55.
700:\subsection{Early-Training Hacking Analysis (100-Step Checkpoint)}
707:The 100-step hacking rate (31.2\%) is already substantially above SFT (7.7\%), supporting the claim that hacking is associated with RL optimization rather than prove-rate level alone.
759:Fisher exact test asks whether TS domination rate differs between ISR and Random at seed level.
761:A permutation test provides a nonparametric alternative robust to distributional assumptions.
762:The Bayes factor (BF$_{10}$) quantifies evidence strength on a continuous scale, avoiding the binary significant/non-significant dichotomy.
774:TS domination & Fisher exact & $\text{OR}{=}\infty$ & 0.004 & 77 \\
777:N-H rate & Permutation & $\Delta{=}{-}3.6$\,pp & 0.917 & --- \\
786:Most checkpoints were deleted during disk cleanup before retrospective audit; Table~\ref{tab:exploratory-perseed} reports the three seeds with surviving checkpoints.
852:This result establishes a \emph{capability threshold} for GRPO-based formalization: the base model must possess at minimum a rudimentary ability to generate syntactically valid solver input for the RL loop to produce any learning signal.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "ad71bf35-73dd-4515-b48f-591ad2fe08f9",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "77:We verify this empirically: Spearman $\\rho(\\text{ISR}, \\text{NLI accuracy}) = -0.049$ ($p = 0.187$, n.s.) from a downstream NLI evaluation on exec-only checkpoint outputs.\n96:\\caption{Fisher exact tests across conditions. Non-hacking rate reported at 5-seed (primary) and 3-seed with PG+FN corrections (sensitivity); TS comparison at 5-seed (primary) and 3-seed (sensitivity).}\n97:\\label{tab:bootstrap-ci}\n124:To address potential inflation from within-seed dependence, we supplement pooled Fisher exact tests with two seed-aware analyses.\n127:Seed-level permutation tests (treating each seed as a single observation, $n{=}5$ per group) yield $p{=}0.28$ (TS) and $p{=}0.26$ (non-hacking), consistent with the severe power limitation of $n{=}5$ (minimum achievable $p{=}0.008$) rather than absence of effect.\n185:ISR was designed to \\emph{detect} reward gaming of $r_{\\text{exec}}$, yet it contains an inherent structural vulnerability: by its LOO definition, single-premise-equals-conclusion constructions receive artificially high ISR ($\\text{ISR}{\\geq}0.5$; empirically 93\\% at $\\text{ISR}{=}0.5$, 7\\% at $\\text{ISR}{=}1.0$; 5-seed ISR $\\beta{=}0.1$ pooled TS samples), creating a positive feedback loop once sampled during GRPO rollouts~\\citep{karwowski-goodhart-rl, kwa-catastrophic-goodhart}.\n225:Tautological & 2-comp $P{=}C$ & $\\bullet$ & 0 & 0 & 0 \\\\\n269:After PG reclassification and TS false-negative correction: ISR non-hacking $= 14/231 = 6.06\\%$ vs.\\ random non-hacking $= 25/262 = 9.5\\%$ (Fisher $p{=}0.182$, n.s.; Wilson 95\\% CI: ISR [3.6\\%, 9.9\\%], Random [6.5\\%, 13.7\\%]).\n270:The direction is consistent with ISR-amplified gaming modes (TS, PG) displacing non-hacking output, but the effect is not statistically significant at the conventional $\\alpha{=}0.05$ threshold.\n300:Since $P \\to P$ is trivially provable, this simultaneously maximizes exec reward.\n350:Two-component formalizations where the premise and conclusion are identical atomic or simple formulas, yielding a $P \\to P$ tautology with minimal token cost.\n422:\\paragraph{Example (FOL, 1000-step exec-only).}\n553:  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.68{\\pm}0.47$} & & \\makebox[0pt][l]{$0.238{\\pm}0.30$} & & & 500-step \\\\\n554:  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.97{\\pm}0.02$} & & \\makebox[0pt][l]{$0.03{\\pm}0.05$} & & \\makebox[0pt][l]{$2.1{\\pm}3.6$} & 1000-step \\\\\n644:\\caption{Training ISR trajectories across reward conditions. ISR $\\beta{=}0.1$ seeds rise rapidly toward $\\text{ISR}{\\approx}1$ (Goodhart gaming via TS tautology); exec-only s44's plateau at ${\\sim}0.5$ is an TS-a artifact ($n{=}2$ gives $\\text{ISR}{\\geq}0.5$ by construction), not non-hacking structural quality; random $\\beta{=}0.1$ remains low. The s42 1k-step trace shows ISR eventually saturates at $0.88$ through the same TS mechanism.}\n650:ISR$^*=0.642$ at 100 steps $\\to$ $0.132$ at 500 steps ($-79.4$\\%) $\\to$ $0.003$ at 1000 steps ($-99.5$\\% from step 100).\n652:By step 1000, 94.8\\% of proved samples have ISR~$=0$ and the mean component count rises to 18.55.\n700:\\subsection{Early-Training Hacking Analysis (100-Step Checkpoint)}\n707:The 100-step hacking rate (31.2\\%) is already substantially above SFT (7.7\\%), supporting the claim that hacking is associated with RL optimization rather than prove-rate level alone.\n759:Fisher exact test asks whether TS domination rate differs between ISR and Random at seed level.\n761:A permutation test provides a nonparametric alternative robust to distributional assumptions.\n762:The Bayes factor (BF$_{10}$) quantifies evidence strength on a continuous scale, avoiding the binary significant/non-significant dichotomy.\n774:TS domination & Fisher exact & $\\text{OR}{=}\\infty$ & 0.004 & 77 \\\\\n777:N-H rate & Permutation & $\\Delta{=}{-}3.6$\\,pp & 0.917 & --- \\\\\n786:Most checkpoints were deleted during disk cleanup before retrospective audit; Table~\\ref{tab:exploratory-perseed} reports the three seeds with surviving checkpoints.\n852:This result establishes a \\emph{capability threshold} for GRPO-based formalization: the base model must possess at minimum a rudimentary ability to generate syntactically valid solver input for the RL loop to produce any learning signal.",
    "numLines": 26
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Grep · `toolu_01DwtQu2Jzi4c4kBJ9fak2DH`</summary>

```json
{
  "pattern": "p[\\s=<>]|Fisher|permutation|significant|p-value|\\\\text.?test|McNemar|Wilcoxon|chi.?sq|bootstrap",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex",
  "output_mode": "content",
  "-n": true,
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "545fd8e7-ca1b-42f2-8c61-ec03f5a94428",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PwnzaksyARDgn63xKTvEeY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15028,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15028
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

_source line 11 · 2026-05-20T04:46:51.042Z_

<details><summary>↩ Tool result · `toolu_01DwtQu2Jzi4c4kBJ9fak2DH`</summary>

```text
5:This gap is especially consequential under RL, where the optimizer exploits any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}.
10:We address this gap with \emph{Solver Trace Ablation} (STA), which applies leave-one-out ablation on solver inputs to test whether each component of a proved formalization is individually necessary.
14:An SFT baseline on identical data largely avoids hacking, consistent with hacking being associated with RL optimization rather than data exposure, though the large prove-rate gap prevents definitive causal attribution (\S\ref{sec:diagnostic}).
21:We present an empirical case study of Goodhart collapse in solver-backed RL, using FOLIO with Qwen3 (4B/1.7B) across six reward conditions, ten seeds (5+5 matched design), two logic types, and up to 1000 training steps. Our contributions:
22:\begin{enumerate}[leftmargin=*,itemsep=2pt]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "0b69005e-4f97-489e-a312-f86f16a4ae98",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "5:This gap is especially consequential under RL, where the optimizer exploits any shortcut the reward fails to penalize~\\citep{skalse-reward-hacking, reward-hacking-survey}.\n10:We address this gap with \\emph{Solver Trace Ablation} (STA), which applies leave-one-out ablation on solver inputs to test whether each component of a proved formalization is individually necessary.\n14:An SFT baseline on identical data largely avoids hacking, consistent with hacking being associated with RL optimization rather than data exposure, though the large prove-rate gap prevents definitive causal attribution (\\S\\ref{sec:diagnostic}).\n21:We present an empirical case study of Goodhart collapse in solver-backed RL, using FOLIO with Qwen3 (4B/1.7B) across six reward conditions, ten seeds (5+5 matched design), two logic types, and up to 1000 training steps. Our contributions:\n22:\\begin{enumerate}[leftmargin=*,itemsep=2pt]",
    "numLines": 5
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Grep · `toolu_01YPHtvdUyYDj7fVG2wPKE2e`</summary>

```json
{
  "pattern": "p[\\s=<>]|Fisher|permutation|significant|p-value|\\\\text.?test|McNemar|Wilcoxon|chi.?sq|bootstrap",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex",
  "output_mode": "content",
  "-n": true,
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "85dbed5f-9c6c-4714-ada4-cc51d828ce3b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PwnzaksyARDgn63xKTvEeY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15028,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15028
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

_source line 13 · 2026-05-20T04:46:52.466Z_

<details><summary>↩ Tool result · `toolu_01YPHtvdUyYDj7fVG2wPKE2e`</summary>

```text
6:An SFT baseline largely avoids hacking under identical data, consistent with hacking being associated with RL optimization, though the prove-rate gap (13\% vs.\ 97\%) prevents definitive causal attribution.
7:Any transient non-hacking window ($p{=}0.92$, permutation test; matched 5+5 design) disappears under extended training; snapshot evaluation overestimates ISR's benefit.
17:%  The structural bias toward single-premise tautologies ($P \to P$ yielding
36:Reward ensembling~\citep{coste2024reward} targets learned rewards, not deterministic solver signals; constrained optimization~\citep{moskovitz2024confronting} could cap ISR, but collapse at all $\beta$ suggests a narrow proxy-validity boundary.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "1bff280b-557f-4c37-a4b7-397d62eeec2f",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "6:An SFT baseline largely avoids hacking under identical data, consistent with hacking being associated with RL optimization, though the prove-rate gap (13\\% vs.\\ 97\\%) prevents definitive causal attribution.\n7:Any transient non-hacking window ($p{=}0.92$, permutation test; matched 5+5 design) disappears under extended training; snapshot evaluation overestimates ISR's benefit.\n17:%  The structural bias toward single-premise tautologies ($P \\to P$ yielding\n36:Reward ensembling~\\citep{coste2024reward} targets learned rewards, not deterministic solver signals; constrained optimization~\\citep{moskovitz2024confronting} could cap ISR, but collapse at all $\\beta$ suggests a narrow proxy-validity boundary.",
    "numLines": 4
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Grep · `toolu_01BxjNUVbbtfoci1umjnFQng`</summary>

```json
{
  "pattern": "p[\\s=<>]|Fisher|permutation|significant|p-value|\\\\text.?test|McNemar|Wilcoxon|chi.?sq|bootstrap",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/docs/paper/experiments.tex",
  "output_mode": "content",
  "-n": true,
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "5404bc34-3e05-4ee6-91c3-e765469456e4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PwnzaksyARDgn63xKTvEeY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15028,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15028
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

_source line 15 · 2026-05-20T04:46:53.504Z_

<details><summary>↩ Tool result · reported error · `toolu_01BxjNUVbbtfoci1umjnFQng`</summary>

```text
&lt;tool_use_error>Path does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/docs/paper/experiments.tex. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "a611d4a2-d7e6-4915-9e0c-e085b8666b1a",
  "tool_use_result": "Error: Path does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/docs/paper/experiments.tex. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation."
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Grep · `toolu_01PgyC6z4TPp2jDA9HDbBrUV`</summary>

```json
{
  "pattern": "p[\\s=<>]|Fisher|permutation|significant|p-value|\\\\text.?test|McNemar|Wilcoxon|chi.?sq|bootstrap",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/docs/paper/appendix.tex",
  "output_mode": "content",
  "-n": true,
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "2877b459-fb63-47f5-bb4d-1f13437580c5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PwnzaksyARDgn63xKTvEeY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15028,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15028
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

_source line 17 · 2026-05-20T04:46:54.692Z_

<details><summary>↩ Tool result · reported error · `toolu_01PgyC6z4TPp2jDA9HDbBrUV`</summary>

```text
&lt;tool_use_error>Path does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/docs/paper/appendix.tex. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "bacb4818-03d8-4ea4-8959-155bd0d9fe91",
  "tool_use_result": "Error: Path does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/docs/paper/appendix.tex. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation."
}
```

</details>

---

### Assistant

_source line 18_

<details><summary>Logged reasoning block</summary>

```text
Let me also check the docs/paper/ directory and the method.tex file for any additional p-values.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "4d3cdb2e-4193-4ecc-8421-d5e866d07700",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TNGJirAFQVbFc6731s1fPL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4046,
      "cache_read_input_tokens": 26869,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4046
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

_source line 19_

Let me check the docs/paper/ directory and method.tex for additional p-values.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "7ba74f72-429e-4c60-b1bb-1e3a08094e49",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TNGJirAFQVbFc6731s1fPL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4046,
      "cache_read_input_tokens": 26869,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4046
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

_source line 20_

<details open><summary>🔧 Tool call — Glob · `toolu_01WdJaWURPwFBZQiuekdAbV3`</summary>

```json
{
  "pattern": "docs/paper/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "5d2e7cb1-b843-448a-b4c3-20bb46c6bd11",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TNGJirAFQVbFc6731s1fPL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4046,
      "cache_read_input_tokens": 26869,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4046
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

_source line 21 · 2026-05-20T04:46:58.597Z_

<details><summary>↩ Tool result · `toolu_01WdJaWURPwFBZQiuekdAbV3`</summary>

```text
docs/paper/discussion.tex
docs/paper/main.tex
docs/paper/related_work.tex
docs/paper/method.tex
docs/paper/experiments.tex
docs/paper/conclusion.tex
docs/paper/abstract.tex
docs/paper/introduction.tex
docs/paper/limitations.tex
docs/paper/appendix.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "134707be-2746-4e1f-b0d8-d34cd0db4b7c",
  "tool_use_result": {
    "filenames": [
      "docs/paper/discussion.tex",
      "docs/paper/main.tex",
      "docs/paper/related_work.tex",
      "docs/paper/method.tex",
      "docs/paper/experiments.tex",
      "docs/paper/conclusion.tex",
      "docs/paper/abstract.tex",
      "docs/paper/introduction.tex",
      "docs/paper/limitations.tex",
      "docs/paper/appendix.tex"
    ],
    "durationMs": 40,
    "numFiles": 10,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Grep · `toolu_014FJFu8cPad8uvJyMnEYECo`</summary>

```json
{
  "pattern": "p[\\s=<>]|Fisher|permutation|significant|p-value|test",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex",
  "output_mode": "content",
  "-n": true,
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "fe553d31-744a-4315-87f3-9c89fb6df70a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TNGJirAFQVbFc6731s1fPL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4046,
      "cache_read_input_tokens": 26869,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4046
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

_source line 23 · 2026-05-20T04:47:00.053Z_

<details><summary>↩ Tool result · `toolu_014FJFu8cPad8uvJyMnEYECo`</summary>

```text
8:We train with Group Relative Policy Optimization (GRPO)~\citep{deepseekmath} ($K{=}4$), where each rollout receives binary execution reward $r_{\text{exec}}(x) = \mathbf{1}[S(x){=}\textit{proved}]$.
15:STA tests whether each component of a proved formalization is individually necessary for proof success .
20:LOO ablation itself is standard in mutation testing and sensitivity analysis~\citep{demillo1978, jia-harman-survey}; our contribution lies in applying it as a GRPO-hacking diagnostic and in the empirical phenomena it surfaces.
37:{\footnotesize For FOL, components include both premises and conclusion sub-expressions (quantifier, antecedent, consequent); each sub-expression is ablated by removing it from the solver input and testing whether the proof still succeeds.}
64:An SFT baseline trained with negative log-likelihood on gold formalizations tests whether structural degeneration arises from RL optimization or data exposure.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "c33a6171-16c7-45c9-a88d-dccacdc3bdbc",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "8:We train with Group Relative Policy Optimization (GRPO)~\\citep{deepseekmath} ($K{=}4$), where each rollout receives binary execution reward $r_{\\text{exec}}(x) = \\mathbf{1}[S(x){=}\\textit{proved}]$.\n15:STA tests whether each component of a proved formalization is individually necessary for proof success .\n20:LOO ablation itself is standard in mutation testing and sensitivity analysis~\\citep{demillo1978, jia-harman-survey}; our contribution lies in applying it as a GRPO-hacking diagnostic and in the empirical phenomena it surfaces.\n37:{\\footnotesize For FOL, components include both premises and conclusion sub-expressions (quantifier, antecedent, consequent); each sub-expression is ablated by removing it from the solver input and testing whether the proof still succeeds.}\n64:An SFT baseline trained with negative log-likelihood on gold formalizations tests whether structural degeneration arises from RL optimization or data exposure.",
    "numLines": 5
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Grep · `toolu_01QcS5nMBfuvxxqpbvC5SeUQ`</summary>

```json
{
  "pattern": "p[\\s=<>]|Fisher|permutation|significant|p-value|test",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/limitations.tex",
  "output_mode": "content",
  "-n": true,
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "58b91ee5-72a0-4fb2-b851-831aaeb3f6ac",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TNGJirAFQVbFc6731s1fPL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4046,
      "cache_read_input_tokens": 26869,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4046
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

_source line 25 · 2026-05-20T04:47:01.022Z_

<details><summary>↩ Tool result · `toolu_01QcS5nMBfuvxxqpbvC5SeUQ`</summary>

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
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "d0409241-0b13-43da-a940-dccddbde1c6d",
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

_source line 26_

<details open><summary>🔧 Tool call — Grep · `toolu_01MfBgkT9UGjkQUW1ZjYZXWh`</summary>

```json
{
  "pattern": "p[\\s=<>]|Fisher|permutation|significant|p-value|test",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex",
  "output_mode": "content",
  "-n": true,
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "c2700034-01da-40dd-acd3-32bbe5748e44",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W7SPekUqU2ficrExp5Sp4D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 994,
      "cache_read_input_tokens": 30915,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 994
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

_source line 27 · 2026-05-20T04:47:05.369Z_

<details><summary>↩ Tool result · `toolu_01MfBgkT9UGjkQUW1ZjYZXWh`</summary>

```text
20:\caption{ISR collapse under exec-only GRPO (seed~42). PR rises 32\%$\to$93\%$\to$96\% while proved-only ISR falls $0.642{\to}0.132{\to}0.003$ over 100$\to$500$\to$1000 steps. By step 1000, 94.8\% of proved samples have $\text{ISR}{=}0$ and mean component count inflates 6.58$\to$18.55 (contradiction explosion).}
38:A 100-step RL checkpoint (Appendix~\ref{app:100step}) at $\text{PR}{=}32\%$ already shows 31.2\% hacking (vs.\ SFT's 7.7\%; $\text{OR}{=}5.5$, 95\% CI $[1.4, 22.0]$), indicating reward hacking emerges early in RL training, not merely at high PR.
70:H7 tautological collapse occurs under both ISR and random conditions, but ISR amplifies it ${\sim}5\times$: $70.6\%$ ($163/231$) under ISR vs.\ $13.7\%$ ($36/262$) under random (Fisher $p{=}1.3{\times}10^{-39}$, $\text{OR}{=}15.05$, 95\% CI $[9.6, 23.6]$). %% registry: plan002 vs plan018 all seeds; D095 FINAL
81:[Omitted long matching line]
88:\caption{Training ISR trajectories across reward conditions. ISR $\beta{=}0.1$ seeds rise rapidly toward $\text{ISR}{\approx}1$ (meta-Goodhart gaming via H7 tautology); exec-only s44's plateau at ${\sim}0.5$ is an H7a artifact ($n{=}2$ gives $\text{ISR}{\geq}0.5$ by construction), not genuine structural quality; random $\beta{=}0.1$ remains low. The s42 1k-step trace shows ISR eventually saturates at $0.88$ through the same H7 mechanism.}
93:Extended training (1000 steps; Figure~\ref{fig:training-isr-curves}) reveals ISR $\beta{=}0.1$'s non-hacking at 500 steps ($17.3\%$, seed~42) is transient: by step 1000, H7 escalates $16.0\%{\to}96.7\%$ while non-hacking collapses to $2.2\%$, converging to $\text{ISR}^{*}{=}0.88$ via near-complete tautological gaming.
94:This mirrors exec-only 1000-step (\S\ref{sec:diagnostic}): both reach ${\sim}0\%$ non-hacking despite opposite ISR ($0.88$ vs.\ $0.003$), two paths to the same structural collapse. %% registry: plan002-b01-s42-1000, plan016-extended-1000-s42
129:Hacking-mode classification reverses this reading: ISR seeds average 76.8\% genuine versus 17.4\% for exec-only (permutation $p{=}0.10$, $N{=}3$), with s42 and s44 achieving 100\% genuine despite training collapse (Table~\ref{tab:prooffol-detailed}).
171:The three dominant modes (Table~\ref{tab:hacking-taxonomy}; definitions in Appendix~\ref{app:hacking-modes})---\textbf{H1} (conclusion embedding, GRPO-universal at $68$--$100\%$), \textbf{H7} (conclusion duplication, ISR-amplified ${\sim}5{\times}$; Fisher $p{=}1.3{\times}10^{-39}$), and \textbf{H8} (premise-subset gaming; Appendix~\ref{app:h8})---account for ${>}90\%$ of hacking across 2 logic types and 6 reward conditions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "c9a6addc-c7ea-4910-af25-f6ccc2eafb32",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "20:\\caption{ISR collapse under exec-only GRPO (seed~42). PR rises 32\\%$\\to$93\\%$\\to$96\\% while proved-only ISR falls $0.642{\\to}0.132{\\to}0.003$ over 100$\\to$500$\\to$1000 steps. By step 1000, 94.8\\% of proved samples have $\\text{ISR}{=}0$ and mean component count inflates 6.58$\\to$18.55 (contradiction explosion).}\n38:A 100-step RL checkpoint (Appendix~\\ref{app:100step}) at $\\text{PR}{=}32\\%$ already shows 31.2\\% hacking (vs.\\ SFT's 7.7\\%; $\\text{OR}{=}5.5$, 95\\% CI $[1.4, 22.0]$), indicating reward hacking emerges early in RL training, not merely at high PR.\n70:H7 tautological collapse occurs under both ISR and random conditions, but ISR amplifies it ${\\sim}5\\times$: $70.6\\%$ ($163/231$) under ISR vs.\\ $13.7\\%$ ($36/262$) under random (Fisher $p{=}1.3{\\times}10^{-39}$, $\\text{OR}{=}15.05$, 95\\% CI $[9.6, 23.6]$). %% registry: plan002 vs plan018 all seeds; D095 FINAL\n81:[Omitted long matching line]\n88:\\caption{Training ISR trajectories across reward conditions. ISR $\\beta{=}0.1$ seeds rise rapidly toward $\\text{ISR}{\\approx}1$ (meta-Goodhart gaming via H7 tautology); exec-only s44's plateau at ${\\sim}0.5$ is an H7a artifact ($n{=}2$ gives $\\text{ISR}{\\geq}0.5$ by construction), not genuine structural quality; random $\\beta{=}0.1$ remains low. The s42 1k-step trace shows ISR eventually saturates at $0.88$ through the same H7 mechanism.}\n93:Extended training (1000 steps; Figure~\\ref{fig:training-isr-curves}) reveals ISR $\\beta{=}0.1$'s non-hacking at 500 steps ($17.3\\%$, seed~42) is transient: by step 1000, H7 escalates $16.0\\%{\\to}96.7\\%$ while non-hacking collapses to $2.2\\%$, converging to $\\text{ISR}^{*}{=}0.88$ via near-complete tautological gaming.\n94:This mirrors exec-only 1000-step (\\S\\ref{sec:diagnostic}): both reach ${\\sim}0\\%$ non-hacking despite opposite ISR ($0.88$ vs.\\ $0.003$), two paths to the same structural collapse. %% registry: plan002-b01-s42-1000, plan016-extended-1000-s42\n129:Hacking-mode classification reverses this reading: ISR seeds average 76.8\\% genuine versus 17.4\\% for exec-only (permutation $p{=}0.10$, $N{=}3$), with s42 and s44 achieving 100\\% genuine despite training collapse (Table~\\ref{tab:prooffol-detailed}).\n171:The three dominant modes (Table~\\ref{tab:hacking-taxonomy}; definitions in Appendix~\\ref{app:hacking-modes})---\\textbf{H1} (conclusion embedding, GRPO-universal at $68$--$100\\%$), \\textbf{H7} (conclusion duplication, ISR-amplified ${\\sim}5{\\times}$; Fisher $p{=}1.3{\\times}10^{-39}$), and \\textbf{H8} (premise-subset gaming; Appendix~\\ref{app:h8})---account for ${>}90\\%$ of hacking across 2 logic types and 6 reward conditions.",
    "numLines": 9
  }
}
```

</details>

---

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — Grep · `toolu_015E7fyVYFxUmqmCoBXM4Wfd`</summary>

```json
{
  "pattern": "p[\\s=<>]|Fisher|permutation|significant|p-value|test",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex",
  "output_mode": "content",
  "-n": true,
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "75332938-e60e-4429-8ee6-96d5791b1813",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W7SPekUqU2ficrExp5Sp4D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 994,
      "cache_read_input_tokens": 30915,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 994
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

_source line 29 · 2026-05-20T04:47:06.524Z_

<details><summary>↩ Tool result · `toolu_015E7fyVYFxUmqmCoBXM4Wfd`</summary>

```text
70:We verify this empirically: Spearman $\rho(\text{ISR}, \text{NLI accuracy}) = -0.049$ ($p = 0.187$, n.s.) from a downstream NLI evaluation on exec-only checkpoint outputs.
89:\caption{Fisher exact tests for non-hacking rate across conditions (3-seed pooled). ISR $\beta{=}0.1$ non-hacking rate is corrected for H8 reclassification and H7 false negatives (Appendix~\ref{app:h8}).}
148:Tautological & 2-comp $P{=}C$ & $\bullet$ & 0 & 0 & 0 \\
192:After H8 reclassification and H7 false-negative correction: ISR non-hacking $= 14/231 = 6.06\%$ vs.\ random non-hacking $= 25/262 = 9.5\%$ (Fisher $p{=}0.182$, n.s.; Wilson 95\% CI: ISR [3.6\%, 9.9\%], Random [6.5\%, 13.7\%]).
193:The direction is consistent with ISR-amplified gaming modes (H7, H8) displacing non-hacking output, but the effect is not statistically significant at the conventional $\alpha{=}0.05$ threshold.
223:Since $P \to P$ is trivially provable, this simultaneously maximizes exec reward.
273:Two-component formalizations where the premise and conclusion are identical atomic or simple formulas, yielding a $P \to P$ tautology with minimal token cost.
345:\paragraph{Example (FOL, 1000-step exec-only).}
425:  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.68{\pm}0.47$} & & \makebox[0pt][l]{$0.238{\pm}0.30$} & & & 500-step \\
426:  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.95{\pm}0.05$} & & \makebox[0pt][l]{$0.16{\pm}0.27$} & & \makebox[0pt][l]{$0.0{\pm}0.0$} & 1000-step \\
517:{\footnotesize Aggregate genuine rate: mean of per-seed genuine rates. Permutation test (exec vs.\ ISR genuine): $p{=}0.10$, $N{=}3$ per group.}
522:ISR$^*=0.642$ at 100 steps $\to$ $0.132$ at 500 steps ($-79.4$\%) $\to$ $0.003$ at 1000 steps ($-99.5$\% from step 100).
524:By step 1000, 94.8\% of proved samples have ISR~$=0$ and the mean component count rises to 18.55.
566:\subsection{Early-Training Hacking Analysis (100-Step Checkpoint)}
573:The 100-step hacking rate (31.2\%) is already substantially above SFT (7.7\%), supporting the claim that hacking is associated with RL optimization rather than prove-rate level alone.
596:This result establishes a \emph{capability threshold} for GRPO-based formalization: the base model must possess at minimum a rudimentary ability to generate syntactically valid solver input for the RL loop to produce any learning signal.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "a8b37833-cc08-4305-aed1-54334807a6c3",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "70:We verify this empirically: Spearman $\\rho(\\text{ISR}, \\text{NLI accuracy}) = -0.049$ ($p = 0.187$, n.s.) from a downstream NLI evaluation on exec-only checkpoint outputs.\n89:\\caption{Fisher exact tests for non-hacking rate across conditions (3-seed pooled). ISR $\\beta{=}0.1$ non-hacking rate is corrected for H8 reclassification and H7 false negatives (Appendix~\\ref{app:h8}).}\n148:Tautological & 2-comp $P{=}C$ & $\\bullet$ & 0 & 0 & 0 \\\\\n192:After H8 reclassification and H7 false-negative correction: ISR non-hacking $= 14/231 = 6.06\\%$ vs.\\ random non-hacking $= 25/262 = 9.5\\%$ (Fisher $p{=}0.182$, n.s.; Wilson 95\\% CI: ISR [3.6\\%, 9.9\\%], Random [6.5\\%, 13.7\\%]).\n193:The direction is consistent with ISR-amplified gaming modes (H7, H8) displacing non-hacking output, but the effect is not statistically significant at the conventional $\\alpha{=}0.05$ threshold.\n223:Since $P \\to P$ is trivially provable, this simultaneously maximizes exec reward.\n273:Two-component formalizations where the premise and conclusion are identical atomic or simple formulas, yielding a $P \\to P$ tautology with minimal token cost.\n345:\\paragraph{Example (FOL, 1000-step exec-only).}\n425:  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.68{\\pm}0.47$} & & \\makebox[0pt][l]{$0.238{\\pm}0.30$} & & & 500-step \\\\\n426:  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.95{\\pm}0.05$} & & \\makebox[0pt][l]{$0.16{\\pm}0.27$} & & \\makebox[0pt][l]{$0.0{\\pm}0.0$} & 1000-step \\\\\n517:{\\footnotesize Aggregate genuine rate: mean of per-seed genuine rates. Permutation test (exec vs.\\ ISR genuine): $p{=}0.10$, $N{=}3$ per group.}\n522:ISR$^*=0.642$ at 100 steps $\\to$ $0.132$ at 500 steps ($-79.4$\\%) $\\to$ $0.003$ at 1000 steps ($-99.5$\\% from step 100).\n524:By step 1000, 94.8\\% of proved samples have ISR~$=0$ and the mean component count rises to 18.55.\n566:\\subsection{Early-Training Hacking Analysis (100-Step Checkpoint)}\n573:The 100-step hacking rate (31.2\\%) is already substantially above SFT (7.7\\%), supporting the claim that hacking is associated with RL optimization rather than prove-rate level alone.\n596:This result establishes a \\emph{capability threshold} for GRPO-based formalization: the base model must possess at minimum a rudimentary ability to generate syntactically valid solver input for the RL loop to produce any learning signal.",
    "numLines": 16
  }
}
```

</details>

---

### Assistant

_source line 30_

<details><summary>Logged reasoning block</summary>

```text
Now I need to read the specific sections with the statistical tests in detail. Let me focus on the key areas I've identified:

1. **experiments.tex (paper/)** - Line 104: Fisher p=0.004 (TS domination), Line 114: Multiple tests (Fisher p=0.004, Mann-Whitney p=0.004, permutation p=0.92)
2. **appendix.tex (paper/)** - Line 77: Spearman p=0.187, Line 127: seed-level permutation p=0.28 and p=0.26, Line 269: Fisher p=0.182, Line 774: Fisher p=0.004, Line 777: permutation p=0.917


3. **conclusion.tex (paper/)** - Line 7: permutation test p=0.92

I should also check the docs/paper versions to see if there are any discrepancies, though the paper/ directory appears to be the primary submission with the updated naming conventions. Let me examine the exact p-values more carefully across these files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "d26f02f3-2087-4876-9853-c534e892cdf0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CLYpBeob6qeg6Jdh4f4LDK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2312,
      "cache_read_input_tokens": 31909,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2312
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

_source line 31_

Let me read the key sections more carefully to extract exact p-values.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "61b4a5cf-579b-4941-a2c1-c5e571d9fc48",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CLYpBeob6qeg6Jdh4f4LDK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2312,
      "cache_read_input_tokens": 31909,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2312
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

_source line 32_

<details open><summary>🔧 Tool call — Read · `toolu_01AJ2mVBig5oERTYWGYF3HZm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "offset": 100,
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
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "22294b76-a1bc-4a6f-b995-f7cc8709effa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CLYpBeob6qeg6Jdh4f4LDK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2312,
      "cache_read_input_tokens": 31909,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2312
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

_source line 33_

<details open><summary>🔧 Tool call — Read · `toolu_011odkUYnpNLA5McDEG1SZji`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "offset": 160,
  "limit": 15
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "ac08d5ca-9532-4970-8d70-2008c5c3bbc0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CLYpBeob6qeg6Jdh4f4LDK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2312,
      "cache_read_input_tokens": 31909,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2312
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

_source line 34 · 2026-05-20T04:47:18.333Z_

<details><summary>↩ Tool result · `toolu_01AJ2mVBig5oERTYWGYF3HZm`</summary>

```text
100	Conclusion embedding ($\text{CE}+\text{TS}$) is GRPO-universal at $68$--$100\%$ across both ISR and random conditions (Appendix Figure~\ref{fig:hacking-composition}).
101	The matched cohort (below) confirms TS as a deterministic attractor under ISR (5/5 seeds), though collapse severity and secondary modes are stochastic.
102	Random yields higher PR ($83{\pm}15\%$ vs.\ $70{\pm}19\%$) but near-zero $\text{ISR}^*$ ($0.080{\pm}0.06$), because the uniform bonus has no structural correlation with component necessity: it reinforces CE (conclusion embedding) rather than TS (tautology).
103	In the exploratory cohort, both conditions produce TS in 2 of 5 seeds; however, exploratory Random TS is non-absorbing (coexists with other modes at $38$--$92\%$, driven by s46 and s43), while ISR-induced TS saturates to $100\%$ in affected seeds.
104	The matched cohort resolves this ambiguity: ISR yields 5/5 TS-dominated seeds versus 0/5 under random control (Fisher $p{=}0.004$), confirming TS as ISR-specific rather than a generic GRPO artifact.
105	ISR-induced TS is absorbing ($100\%$ of proved samples in affected seeds), while random-induced TS coexists with other modes ($38$--$92\%$) and shows extreme seed dependence (per-seed range: $0\%$--$91.5\%$).
106	ISR converts TS from a stochastic possibility into an irreversible attractor.
107	The reward gap explains this: TS tautologies receive expected reward ${\geq}1{+}0.5\beta$ (mean empirical $\text{ISR}{=}0.535$) versus ${\sim}1{+}0.26\beta$ for non-hacking proofs (premise-count-matched), creating a persistent gradient toward tautological constructions regardless of dose.
108	
109	\textbf{Matched replication: deterministic attractor, stochastic severity.}
110	An independent matched cohort (seeds 47--51, $\beta{=}0.1$; Appendix Table~\ref{tab:matched-perseed}) confirms TS as a deterministic attractor under ISR reward: all 5/5 seeds are TS-dominated ($\text{TS}{=}90.8{\pm}7.5\%$; range $85$--$100\%$), with non-hacking rates of $0$--$6\%$ (mean $2.3\%$).
111	Collapse severity varies: s48 achieves only $66\%$ prove rate with $100\%$ TS, while s50 maintains $98\%$ PR with $86\%$ TS, indicating that the same reward signal produces varying degrees of capability loss while converging to the same structural attractor.
112	PR varies widely ($89{\pm}13\%$) while TS domination is uniform, confirming that ISR's structural bias operates independently of training success.
113	Random seeds show no systematic TS concentration ($\text{PR}{=}59{\pm}36\%$, $\text{TS}{=}6.7{\pm}8.1\%$, 0/5 TS-dominated; Appendix Table~\ref{tab:matched-perseed}): all five seeds are CE-dominated ($55$--$89\%$ CE), and s49 collapses to $\text{PR}{=}5\%$ via repetition (the same failure mode as exec-only s43), illustrating training instability under random reward without ISR-specific bias.
114	Fisher exact test on TS domination yields $\text{OR}{=}\infty$ ($p{=}0.004$, 95\% CI $[2.30, \infty]$, $\text{BF}_{10}{=}77$); Mann-Whitney $U$ on $\text{ISR}^*$: $U{=}25$, $p{=}0.004$, $r{=}1.0$; genuine rates do not differ significantly ($2.3\%$ vs.\ $5.9\%$, $p{=}0.92$, permutation test; Appendix~\ref{app:matched-stats}), with the point estimate consistently favoring Random (corrected 3-seed: ISR $6.1\%$ vs.\ Random $9.5\%$; matched: $2.3\%$ vs.\ $5.9\%$).
115	The exploratory cohort (seeds 42--46; Appendix Table~\ref{tab:exploratory-perseed}) showed greater divergence ($2/5$ TS-dominated) but the same qualitative direction; extended training confirms non-hacking windows close completely (s42: $17\%{\to}2\%$, s45: $55\%{\to}0\%$ at 1000 steps). %% registry: plan002-b01-s42-1000, plan002-b01-s45-1000
116	
117	\textbf{Trajectory and dose-response.}\label{sec:goodhart-temporal}
118	Extended training (1000 steps) confirms the window is transient: s42 declines to $2\%$ N-H via TS saturation, s45 collapses to $0\%$ through reward collapse (Appendix Figure~\ref{fig:training-isr-curves}). %% registry: plan002-b01-s42-1000, plan002-b01-s45-1000
119	At $\beta{=}0.2$, all seeds converge to pure TS-a ($0\%$ N-H, $n{=}290$); at $\beta{=}0.3$, three seeds yield three distinct failure modes with extreme instability ($\text{PR}{=}66{\pm}42\%$; Appendix~\ref{app:beta03}). %% registry: sweep-isr-b02-s42/s43/s44, plan002-additive-b03-s42/s43/s44
120	Across doses, $\beta\in\{0.05, 0.2\}$ deterministically collapse to TS, $\beta{=}0.3$ triggers multi-modal instability, and only $\beta{=}0.1$ sustains a transient window; with four dose points and 3--5 seeds each, these patterns are preliminary.
121	
122	\subsection{Cross-Logic Extension}
123	\label{sec:crosslogic}
124	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "0aee342e-4abf-44e4-a51d-4eb775ceb4dd",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
      "content": "Conclusion embedding ($\\text{CE}+\\text{TS}$) is GRPO-universal at $68$--$100\\%$ across both ISR and random conditions (Appendix Figure~\\ref{fig:hacking-composition}).\nThe matched cohort (below) confirms TS as a deterministic attractor under ISR (5/5 seeds), though collapse severity and secondary modes are stochastic.\nRandom yields higher PR ($83{\\pm}15\\%$ vs.\\ $70{\\pm}19\\%$) but near-zero $\\text{ISR}^*$ ($0.080{\\pm}0.06$), because the uniform bonus has no structural correlation with component necessity: it reinforces CE (conclusion embedding) rather than TS (tautology).\nIn the exploratory cohort, both conditions produce TS in 2 of 5 seeds; however, exploratory Random TS is non-absorbing (coexists with other modes at $38$--$92\\%$, driven by s46 and s43), while ISR-induced TS saturates to $100\\%$ in affected seeds.\nThe matched cohort resolves this ambiguity: ISR yields 5/5 TS-dominated seeds versus 0/5 under random control (Fisher $p{=}0.004$), confirming TS as ISR-specific rather than a generic GRPO artifact.\nISR-induced TS is absorbing ($100\\%$ of proved samples in affected seeds), while random-induced TS coexists with other modes ($38$--$92\\%$) and shows extreme seed dependence (per-seed range: $0\\%$--$91.5\\%$).\nISR converts TS from a stochastic possibility into an irreversible attractor.\nThe reward gap explains this: TS tautologies receive expected reward ${\\geq}1{+}0.5\\beta$ (mean empirical $\\text{ISR}{=}0.535$) versus ${\\sim}1{+}0.26\\beta$ for non-hacking proofs (premise-count-matched), creating a persistent gradient toward tautological constructions regardless of dose.\n\n\\textbf{Matched replication: deterministic attractor, stochastic severity.}\nAn independent matched cohort (seeds 47--51, $\\beta{=}0.1$; Appendix Table~\\ref{tab:matched-perseed}) confirms TS as a deterministic attractor under ISR reward: all 5/5 seeds are TS-dominated ($\\text{TS}{=}90.8{\\pm}7.5\\%$; range $85$--$100\\%$), with non-hacking rates of $0$--$6\\%$ (mean $2.3\\%$).\nCollapse severity varies: s48 achieves only $66\\%$ prove rate with $100\\%$ TS, while s50 maintains $98\\%$ PR with $86\\%$ TS, indicating that the same reward signal produces varying degrees of capability loss while converging to the same structural attractor.\nPR varies widely ($89{\\pm}13\\%$) while TS domination is uniform, confirming that ISR's structural bias operates independently of training success.\nRandom seeds show no systematic TS concentration ($\\text{PR}{=}59{\\pm}36\\%$, $\\text{TS}{=}6.7{\\pm}8.1\\%$, 0/5 TS-dominated; Appendix Table~\\ref{tab:matched-perseed}): all five seeds are CE-dominated ($55$--$89\\%$ CE), and s49 collapses to $\\text{PR}{=}5\\%$ via repetition (the same failure mode as exec-only s43), illustrating training instability under random reward without ISR-specific bias.\nFisher exact test on TS domination yields $\\text{OR}{=}\\infty$ ($p{=}0.004$, 95\\% CI $[2.30, \\infty]$, $\\text{BF}_{10}{=}77$); Mann-Whitney $U$ on $\\text{ISR}^*$: $U{=}25$, $p{=}0.004$, $r{=}1.0$; genuine rates do not differ significantly ($2.3\\%$ vs.\\ $5.9\\%$, $p{=}0.92$, permutation test; Appendix~\\ref{app:matched-stats}), with the point estimate consistently favoring Random (corrected 3-seed: ISR $6.1\\%$ vs.\\ Random $9.5\\%$; matched: $2.3\\%$ vs.\\ $5.9\\%$).\nThe exploratory cohort (seeds 42--46; Appendix Table~\\ref{tab:exploratory-perseed}) showed greater divergence ($2/5$ TS-dominated) but the same qualitative direction; extended training confirms non-hacking windows close completely (s42: $17\\%{\\to}2\\%$, s45: $55\\%{\\to}0\\%$ at 1000 steps). %% registry: plan002-b01-s42-1000, plan002-b01-s45-1000\n\n\\textbf{Trajectory and dose-response.}\\label{sec:goodhart-temporal}\nExtended training (1000 steps) confirms the window is transient: s42 declines to $2\\%$ N-H via TS saturation, s45 collapses to $0\\%$ through reward collapse (Appendix Figure~\\ref{fig:training-isr-curves}). %% registry: plan002-b01-s42-1000, plan002-b01-s45-1000\nAt $\\beta{=}0.2$, all seeds converge to pure TS-a ($0\\%$ N-H, $n{=}290$); at $\\beta{=}0.3$, three seeds yield three distinct failure modes with extreme instability ($\\text{PR}{=}66{\\pm}42\\%$; Appendix~\\ref{app:beta03}). %% registry: sweep-isr-b02-s42/s43/s44, plan002-additive-b03-s42/s43/s44\nAcross doses, $\\beta\\in\\{0.05, 0.2\\}$ deterministically collapse to TS, $\\beta{=}0.3$ triggers multi-modal instability, and only $\\beta{=}0.1$ sustains a transient window; with four dose points and 3--5 seeds each, these patterns are preliminary.\n\n\\subsection{Cross-Logic Extension}\n\\label{sec:crosslogic}\n",
      "numLines": 25,
      "startLine": 100,
      "totalLines": 168
    }
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-20T04:47:18.330Z_

<details><summary>↩ Tool result · `toolu_011odkUYnpNLA5McDEG1SZji`</summary>

```text
160	\end{tabular}}
161	\caption{Hacking modes (\% of proved). $^a$Single seed (s42); remaining columns pooled (ISR/Rnd 4B: 5-seed; Prolog/1.7B: 3-seed). $^\sharp$Prolog: strict+functional pooled. $^\ddagger$1.7B N-H overestimates true rate: strict non-hacking (S-NH; \S\ref{sec:rewards}) is $0$--$3.7\%$ (ISR $\beta{=}0.1$), $0\%$ (Rnd $\beta{=}0.1$), $0$--$29\%$ (ISR $\beta{=}0.3$); CI undetected by classifier at 1.7B.}
162	\label{tab:hacking-taxonomy}
163	\end{table}
164	
165	Eight modes are detected by automated classifiers (Table~\ref{tab:hacking-taxonomy}; Appendix~\ref{app:hacking-modes}); CI (contradiction injection) is identified via manual audit at 1.7B in a single seed (s42, Random $\beta{=}0.1$) and may not generalize.
166	CE, TS, and PG account for ${>}90\%$ of hacking across ${\geq}3$ seeds each; ISR modestly increases TS probability ($\text{OR}{=}2.84$; Appendix Table~\ref{tab:bootstrap-ci}), but per-seed variance dominates.
167	All GRPO conditions show ${\geq}80\%$ pooled hacking; only SFT achieves $92.3\%$ non-hacking.
168	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "572f205a-74f4-464e-9c7b-e7e91f8907fa",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
      "content": "\\end{tabular}}\n\\caption{Hacking modes (\\% of proved). $^a$Single seed (s42); remaining columns pooled (ISR/Rnd 4B: 5-seed; Prolog/1.7B: 3-seed). $^\\sharp$Prolog: strict+functional pooled. $^\\ddagger$1.7B N-H overestimates true rate: strict non-hacking (S-NH; \\S\\ref{sec:rewards}) is $0$--$3.7\\%$ (ISR $\\beta{=}0.1$), $0\\%$ (Rnd $\\beta{=}0.1$), $0$--$29\\%$ (ISR $\\beta{=}0.3$); CI undetected by classifier at 1.7B.}\n\\label{tab:hacking-taxonomy}\n\\end{table}\n\nEight modes are detected by automated classifiers (Table~\\ref{tab:hacking-taxonomy}; Appendix~\\ref{app:hacking-modes}); CI (contradiction injection) is identified via manual audit at 1.7B in a single seed (s42, Random $\\beta{=}0.1$) and may not generalize.\nCE, TS, and PG account for ${>}90\\%$ of hacking across ${\\geq}3$ seeds each; ISR modestly increases TS probability ($\\text{OR}{=}2.84$; Appendix Table~\\ref{tab:bootstrap-ci}), but per-seed variance dominates.\nAll GRPO conditions show ${\\geq}80\\%$ pooled hacking; only SFT achieves $92.3\\%$ non-hacking.\n",
      "numLines": 9,
      "startLine": 160,
      "totalLines": 168
    }
  }
}
```

</details>

---

### Tool call

_source line 36_

<details open><summary>🔧 Tool call — Read · `toolu_01GenZYdvu9F6fYiccqF99uL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
  "offset": 70,
  "limit": 15
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "61a44547-84a5-4111-a76d-6fa3944e418e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CLYpBeob6qeg6Jdh4f4LDK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2312,
      "cache_read_input_tokens": 31909,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2312
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

_source line 37 · 2026-05-20T04:47:18.766Z_

<details><summary>↩ Tool result · `toolu_01GenZYdvu9F6fYiccqF99uL`</summary>

```text
70	
71	\section{Extended Discussion}
72	\label{app:extended-discussion}
73	
74	\paragraph{What ISR measures, and what it does not.}
75	ISR quantifies syntactic component necessity: the fraction of solver-input components whose individual removal causes proof failure.
76	This is strictly weaker than semantic faithfulness (whether the formalization accurately captures the natural-language meaning).
77	We verify this empirically: Spearman $\rho(\text{ISR}, \text{NLI accuracy}) = -0.049$ ($p = 0.187$, n.s.) from a downstream NLI evaluation on exec-only checkpoint outputs.
78	ISR and downstream task performance are uncorrelated.
79	ISR is thus a structural integrity diagnostic, not a semantic quality metric: high ISR indicates that every component contributes to the proof, not that the proof faithfully represents the original reasoning problem.
80	
81	Critically, low ISR carries different semantics depending on the training objective.
82	Under exec-only training, low ISR in Prolog reflects redundant coding (repeated ground facts where removing any single copy does not affect the proof) rather than an absence of reasoning (\S\ref{sec:crosslogic}).
83	Under ISR-as-reward, high ISR reflects metric gaming (\S\ref{sec:goodhart}).
84	ISR values must always be interpreted relative to the optimization objective that produced them.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "b2958819-6d8b-46ba-a3ea-1eb1f2fb3991",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
      "content": "\n\\section{Extended Discussion}\n\\label{app:extended-discussion}\n\n\\paragraph{What ISR measures, and what it does not.}\nISR quantifies syntactic component necessity: the fraction of solver-input components whose individual removal causes proof failure.\nThis is strictly weaker than semantic faithfulness (whether the formalization accurately captures the natural-language meaning).\nWe verify this empirically: Spearman $\\rho(\\text{ISR}, \\text{NLI accuracy}) = -0.049$ ($p = 0.187$, n.s.) from a downstream NLI evaluation on exec-only checkpoint outputs.\nISR and downstream task performance are uncorrelated.\nISR is thus a structural integrity diagnostic, not a semantic quality metric: high ISR indicates that every component contributes to the proof, not that the proof faithfully represents the original reasoning problem.\n\nCritically, low ISR carries different semantics depending on the training objective.\nUnder exec-only training, low ISR in Prolog reflects redundant coding (repeated ground facts where removing any single copy does not affect the proof) rather than an absence of reasoning (\\S\\ref{sec:crosslogic}).\nUnder ISR-as-reward, high ISR reflects metric gaming (\\S\\ref{sec:goodhart}).\nISR values must always be interpreted relative to the optimization objective that produced them.",
      "numLines": 15,
      "startLine": 70,
      "totalLines": 858
    }
  }
}
```

</details>

---

### Tool call

_source line 38_

<details open><summary>🔧 Tool call — Read · `toolu_01XkTC4p1sv9GWqFwzquZu89`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
  "offset": 120,
  "limit": 15
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "b4030d9c-bfff-4fc3-ab1c-5f0560ffff42",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CLYpBeob6qeg6Jdh4f4LDK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2312,
      "cache_read_input_tokens": 31909,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2312
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

_source line 39 · 2026-05-20T04:47:19.631Z_

<details><summary>↩ Tool result · `toolu_01XkTC4p1sv9GWqFwzquZu89`</summary>

```text
120	\end{table}
121	
122	\paragraph{Seed-level statistical analysis.}
123	\label{app:statistical-details}
124	To address potential inflation from within-seed dependence, we supplement pooled Fisher exact tests with two seed-aware analyses.
125	Cochran--Mantel--Haenszel (CMH) tests stratify by seed while pooling across samples: TS $\text{OR}_{\text{CMH}}{=}2.46$ (95\% CI $[1.85, 3.27]$, $p{=}5.6{\times}10^{-16}$); non-hacking $\text{OR}_{\text{CMH}}{=}3.37$ (95\% CI $[2.21, 5.13]$, $p{=}4.5{\times}10^{-10}$).
126	CMH assumes within-stratum independence, but samples within each seed share a single checkpoint and use greedy decoding; the effective independent units are seeds ($n{=}5$), not samples, and CMH $p$-values are consequently inflated.
127	Seed-level permutation tests (treating each seed as a single observation, $n{=}5$ per group) yield $p{=}0.28$ (TS) and $p{=}0.26$ (non-hacking), consistent with the severe power limitation of $n{=}5$ (minimum achievable $p{=}0.008$) rather than absence of effect.
128	
129	\begin{table}[!htb]
130	\centering
131	\caption{Per-seed classification results for ISR and Random at $\beta{=}0.1$ (500 steps, FOL). $n$ = proved samples. ISR$^*$ = proved-only mean ISR. $\dagger$~PG audit complete; $\ddagger$~checkpoint unavailable before audit, N-H is uncorrected upper bound. Percentages are per-classifier; samples may match multiple modes. N-H uses set-exclusion per the C013 taxonomy standard.}
132	\label{tab:fol-beta01-perseed}
133	\small
134	\resizebox{\columnwidth}{!}{%
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "7e8c1ec6-2284-48e7-8352-38951bf18a4d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
      "content": "\\end{table}\n\n\\paragraph{Seed-level statistical analysis.}\n\\label{app:statistical-details}\nTo address potential inflation from within-seed dependence, we supplement pooled Fisher exact tests with two seed-aware analyses.\nCochran--Mantel--Haenszel (CMH) tests stratify by seed while pooling across samples: TS $\\text{OR}_{\\text{CMH}}{=}2.46$ (95\\% CI $[1.85, 3.27]$, $p{=}5.6{\\times}10^{-16}$); non-hacking $\\text{OR}_{\\text{CMH}}{=}3.37$ (95\\% CI $[2.21, 5.13]$, $p{=}4.5{\\times}10^{-10}$).\nCMH assumes within-stratum independence, but samples within each seed share a single checkpoint and use greedy decoding; the effective independent units are seeds ($n{=}5$), not samples, and CMH $p$-values are consequently inflated.\nSeed-level permutation tests (treating each seed as a single observation, $n{=}5$ per group) yield $p{=}0.28$ (TS) and $p{=}0.26$ (non-hacking), consistent with the severe power limitation of $n{=}5$ (minimum achievable $p{=}0.008$) rather than absence of effect.\n\n\\begin{table}[!htb]\n\\centering\n\\caption{Per-seed classification results for ISR and Random at $\\beta{=}0.1$ (500 steps, FOL). $n$ = proved samples. ISR$^*$ = proved-only mean ISR. $\\dagger$~PG audit complete; $\\ddagger$~checkpoint unavailable before audit, N-H is uncorrected upper bound. Percentages are per-classifier; samples may match multiple modes. N-H uses set-exclusion per the C013 taxonomy standard.}\n\\label{tab:fol-beta01-perseed}\n\\small\n\\resizebox{\\columnwidth}{!}{%",
      "numLines": 15,
      "startLine": 120,
      "totalLines": 858
    }
  }
}
```

</details>

---

### Tool call

_source line 40_

<details open><summary>🔧 Tool call — Read · `toolu_01KUr6KmBxkeAM76145h5WcS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
  "offset": 260,
  "limit": 15
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "f9411790-e6c3-4463-a284-c98847951f0e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CLYpBeob6qeg6Jdh4f4LDK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2312,
      "cache_read_input_tokens": 31909,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2312
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

_source line 41 · 2026-05-20T04:47:20.173Z_

<details><summary>↩ Tool result · `toolu_01KUr6KmBxkeAM76145h5WcS`</summary>

```text
260	
261	\paragraph{TS false-negative correction (TS-b obfuscated tautology).}
262	ISR $\beta{=}0.1$ seed~44 contained 12 samples with $n_{\text{prem}}{=}1$ classified as non-hacking by the text matcher.
263	Manual inspection confirmed all 12 are logically equivalent to TS but evade text matching through vacuous quantifier wrapping ($11/12$) or structural simplification ($1/12$).
264	We classify these as \textbf{TS-b} (obfuscated tautology), distinct from text-match-detectable TS-a.
265	$10/12$ achieve $\text{ISR}{\geq}0.83$, indicating simultaneous gaming of execution reward, ISR metric, and TS classifier (triple gaming; \S\ref{sec:taxonomy}).
266	After correction, ISR s44 non-hacking${=}0$; total TS = TS-a (77 text-match) + TS-b (12 obfuscated) = 89.
267	
268	\paragraph{Impact on non-hacking-rate comparison.}
269	After PG reclassification and TS false-negative correction: ISR non-hacking $= 14/231 = 6.06\%$ vs.\ random non-hacking $= 25/262 = 9.5\%$ (Fisher $p{=}0.182$, n.s.; Wilson 95\% CI: ISR [3.6\%, 9.9\%], Random [6.5\%, 13.7\%]).
270	The direction is consistent with ISR-amplified gaming modes (TS, PG) displacing non-hacking output, but the effect is not statistically significant at the conventional $\alpha{=}0.05$ threshold.
271	
272	\subsection{Conclusion Embedding (CE)}
273	
274	\paragraph{Definition.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "eda1377c-4606-4d44-92a7-1e8d89f8d4e4",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
      "content": "\n\\paragraph{TS false-negative correction (TS-b obfuscated tautology).}\nISR $\\beta{=}0.1$ seed~44 contained 12 samples with $n_{\\text{prem}}{=}1$ classified as non-hacking by the text matcher.\nManual inspection confirmed all 12 are logically equivalent to TS but evade text matching through vacuous quantifier wrapping ($11/12$) or structural simplification ($1/12$).\nWe classify these as \\textbf{TS-b} (obfuscated tautology), distinct from text-match-detectable TS-a.\n$10/12$ achieve $\\text{ISR}{\\geq}0.83$, indicating simultaneous gaming of execution reward, ISR metric, and TS classifier (triple gaming; \\S\\ref{sec:taxonomy}).\nAfter correction, ISR s44 non-hacking${=}0$; total TS = TS-a (77 text-match) + TS-b (12 obfuscated) = 89.\n\n\\paragraph{Impact on non-hacking-rate comparison.}\nAfter PG reclassification and TS false-negative correction: ISR non-hacking $= 14/231 = 6.06\\%$ vs.\\ random non-hacking $= 25/262 = 9.5\\%$ (Fisher $p{=}0.182$, n.s.; Wilson 95\\% CI: ISR [3.6\\%, 9.9\\%], Random [6.5\\%, 13.7\\%]).\nThe direction is consistent with ISR-amplified gaming modes (TS, PG) displacing non-hacking output, but the effect is not statistically significant at the conventional $\\alpha{=}0.05$ threshold.\n\n\\subsection{Conclusion Embedding (CE)}\n\n\\paragraph{Definition.}",
      "numLines": 15,
      "startLine": 260,
      "totalLines": 858
    }
  }
}
```

</details>

---

### Tool call

_source line 42_

<details open><summary>🔧 Tool call — Read · `toolu_01Xvm43oPejdcoRk9HtQPjdq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
  "offset": 768,
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
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "dd823bc1-0d25-47fa-9d55-9115c5292bf5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CLYpBeob6qeg6Jdh4f4LDK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2312,
      "cache_read_input_tokens": 31909,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2312
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

_source line 43 · 2026-05-20T04:47:20.855Z_

<details><summary>↩ Tool result · `toolu_01Xvm43oPejdcoRk9HtQPjdq`</summary>

```text
768	\label{tab:stat-tests}
769	\resizebox{\columnwidth}{!}{%
770	\begin{tabular}{@{}llccl@{}}
771	\toprule
772	\textbf{Comparison} & \textbf{Test} & \textbf{Statistic} & $\boldsymbol{p}$ & \textbf{BF$_{10}$} \\
773	\midrule
774	TS domination & Fisher exact & $\text{OR}{=}\infty$ & 0.004 & 77 \\
775	ISR$^*$ & Mann-Whitney $U$ & $U{=}25$ & 0.004 & --- \\
776	TS rate & Mann-Whitney $U$ & $U{=}25$ & 0.004 & --- \\
777	N-H rate & Permutation & $\Delta{=}{-}3.6$\,pp & 0.917 & --- \\
778	\bottomrule
779	\end{tabular}}
780	\end{table}
781	
782	\subsection{Exploratory Cohort (Partial)}
783	\label{app:exploratory-cohort}
784	
785	The original exploratory cohort (seeds 42--46, $\beta{=}0.1$) motivated the matched replication.
786	Most checkpoints were deleted during disk cleanup before retrospective audit; Table~\ref{tab:exploratory-perseed} reports the three seeds with surviving checkpoints.
787	Full 5-seed pooled statistics from the original evaluation are in Table~\ref{tab:fol-beta01-perseed}; those results informed the exploratory analysis in \S\ref{sec:goodhart} but should be interpreted with the caveat that not all seeds could be re-audited.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "8a852778-27f0-4d5d-bea1-cd3fcae40497",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
      "content": "\\label{tab:stat-tests}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llccl@{}}\n\\toprule\n\\textbf{Comparison} & \\textbf{Test} & \\textbf{Statistic} & $\\boldsymbol{p}$ & \\textbf{BF$_{10}$} \\\\\n\\midrule\nTS domination & Fisher exact & $\\text{OR}{=}\\infty$ & 0.004 & 77 \\\\\nISR$^*$ & Mann-Whitney $U$ & $U{=}25$ & 0.004 & --- \\\\\nTS rate & Mann-Whitney $U$ & $U{=}25$ & 0.004 & --- \\\\\nN-H rate & Permutation & $\\Delta{=}{-}3.6$\\,pp & 0.917 & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\subsection{Exploratory Cohort (Partial)}\n\\label{app:exploratory-cohort}\n\nThe original exploratory cohort (seeds 42--46, $\\beta{=}0.1$) motivated the matched replication.\nMost checkpoints were deleted during disk cleanup before retrospective audit; Table~\\ref{tab:exploratory-perseed} reports the three seeds with surviving checkpoints.\nFull 5-seed pooled statistics from the original evaluation are in Table~\\ref{tab:fol-beta01-perseed}; those results informed the exploratory analysis in \\S\\ref{sec:goodhart} but should be interpreted with the caveat that not all seeds could be re-audited.",
      "numLines": 20,
      "startLine": 768,
      "totalLines": 858
    }
  }
}
```

</details>

---

### Assistant

_source line 44_

<details><summary>Logged reasoning block</summary>

```text
Now let me also check for the ProofFOL genuine rate permutation test mentioned in docs/paper, and for the TS OR=2.84, and 100-step OR=5.5, and the Fisher p for TS rate comparison.

Let me also look for the 100-step OR=5.5 with its p-value.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "6d0b82dd-4edc-4271-a311-a6787d2a9476",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FWH5QqGCosGXRrR9qTNz8Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5019,
      "cache_read_input_tokens": 34221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5019
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

_source line 45_

Let me check a few more specific areas.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "3f9082fc-836e-457d-822a-884ac821d32d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FWH5QqGCosGXRrR9qTNz8Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5019,
      "cache_read_input_tokens": 34221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5019
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

_source line 46_

<details open><summary>🔧 Tool call — Read · `toolu_01GSnCDNfruRusonyUjhyiap`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "offset": 44,
  "limit": 15
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "4d69bd66-eb7a-41dc-9066-812f95ccc788",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FWH5QqGCosGXRrR9qTNz8Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5019,
      "cache_read_input_tokens": 34221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5019
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

_source line 47 · 2026-05-20T04:47:28.006Z_

<details><summary>↩ Tool result · `toolu_01GSnCDNfruRusonyUjhyiap`</summary>

```text
44	Seed~42 reaches $\text{PR}{=}93\%$ via conclusion embedding ($\text{CE}{=}87\%$); s43 collapses to $\text{PR}{=}13\%$ via repetition (87\% of rollouts truncated)\footnote{Exec-only s43 was evaluated with sampling ($T{=}0.7$) rather than greedy decoding; its metrics are included for completeness but are not strictly comparable (Appendix~\ref{app:setup}).}; s44 reaches $\text{PR}{=}98\%$ via tautological collapse ($\text{TS}{=}100\%$, mean $n{=}2.04$). %% registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44
45	Cross-seed PR variance ($\sigma{=}47$\,pp) shows that aggregate metrics obscure qualitatively different failure modes. All three seeds are flagged by $\text{ISR}^*$, whether they pass the PR check (s44) or fail it (s43).
46	By 1000 steps, all three converge to high PR ($0.97{\pm}0.02$) with near-zero non-hacking output via different dominant modes (Appendix Tables~\ref{tab:exec-only-1000},~\ref{tab:fol-detailed}). %% registry: plan016-extended-1000-s42, exec-only-s43-1000step-r7, plan001-exec-only-s44-1000-r2
47	S43 recovers from $\text{PR}{=}13\%$ to $96\%$ entirely through CE exploitation: PR recovery does not imply quality recovery.
48	
49	\textbf{SFT baseline.}
50	SFT on gold formalizations reaches $\text{PR}{=}13.0\%$ (3-seed pooled, 1000 steps) with $92.3\%$ non-hacking ($n{=}39$; per-seed range ${\sim}$91--93\%).
51	TS is entirely absent; CE occurs at $7.7\%$ ($\text{OR}{=}147$ vs.\ exec-only, $p{<}0.001$). %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3
52	The near-absence of hacking under identical data exposure is consistent with hacking being associated with RL optimization rather than data exposure; a 100-step checkpoint ($\text{PR}{=}32\%$, hacking${\geq}31\%$) partially controls for the PR-level confound (Appendix~\ref{app:100step}).
53	Exploit discovery requires the trial-and-error sampling inherent to RL but absent from supervised training; whether SFT would hack at higher PR remains an open question.
54	
55	\subsection{ISR as Reward: Goodhart Effects}
56	\label{sec:goodhart}
57	
58	We now reverse roles: instead of treating ISR as an observer, we use it as a reward augmentation, $r = r_{\text{exec}}\cdot(1 + \beta\,\text{ISR})$, with a matched random control, $r = r_{\text{exec}}\cdot(1 + \beta\,u)$, $u\sim\mathcal{U}(0,1)$, to isolate ISR-specific signal from generic reward-variance effects.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "47f93890-5828-494a-9a83-7c9641ce3b7e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
      "content": "Seed~42 reaches $\\text{PR}{=}93\\%$ via conclusion embedding ($\\text{CE}{=}87\\%$); s43 collapses to $\\text{PR}{=}13\\%$ via repetition (87\\% of rollouts truncated)\\footnote{Exec-only s43 was evaluated with sampling ($T{=}0.7$) rather than greedy decoding; its metrics are included for completeness but are not strictly comparable (Appendix~\\ref{app:setup}).}; s44 reaches $\\text{PR}{=}98\\%$ via tautological collapse ($\\text{TS}{=}100\\%$, mean $n{=}2.04$). %% registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44\nCross-seed PR variance ($\\sigma{=}47$\\,pp) shows that aggregate metrics obscure qualitatively different failure modes. All three seeds are flagged by $\\text{ISR}^*$, whether they pass the PR check (s44) or fail it (s43).\nBy 1000 steps, all three converge to high PR ($0.97{\\pm}0.02$) with near-zero non-hacking output via different dominant modes (Appendix Tables~\\ref{tab:exec-only-1000},~\\ref{tab:fol-detailed}). %% registry: plan016-extended-1000-s42, exec-only-s43-1000step-r7, plan001-exec-only-s44-1000-r2\nS43 recovers from $\\text{PR}{=}13\\%$ to $96\\%$ entirely through CE exploitation: PR recovery does not imply quality recovery.\n\n\\textbf{SFT baseline.}\nSFT on gold formalizations reaches $\\text{PR}{=}13.0\\%$ (3-seed pooled, 1000 steps) with $92.3\\%$ non-hacking ($n{=}39$; per-seed range ${\\sim}$91--93\\%).\nTS is entirely absent; CE occurs at $7.7\\%$ ($\\text{OR}{=}147$ vs.\\ exec-only, $p{<}0.001$). %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3\nThe near-absence of hacking under identical data exposure is consistent with hacking being associated with RL optimization rather than data exposure; a 100-step checkpoint ($\\text{PR}{=}32\\%$, hacking${\\geq}31\\%$) partially controls for the PR-level confound (Appendix~\\ref{app:100step}).\nExploit discovery requires the trial-and-error sampling inherent to RL but absent from supervised training; whether SFT would hack at higher PR remains an open question.\n\n\\subsection{ISR as Reward: Goodhart Effects}\n\\label{sec:goodhart}\n\nWe now reverse roles: instead of treating ISR as an observer, we use it as a reward augmentation, $r = r_{\\text{exec}}\\cdot(1 + \\beta\\,\\text{ISR})$, with a matched random control, $r = r_{\\text{exec}}\\cdot(1 + \\beta\\,u)$, $u\\sim\\mathcal{U}(0,1)$, to isolate ISR-specific signal from generic reward-variance effects.",
      "numLines": 15,
      "startLine": 44,
      "totalLines": 168
    }
  }
}
```

</details>

---

### Tool call

_source line 48_

<details open><summary>🔧 Tool call — Read · `toolu_0159ivoRncAmpruDyUe4vMuZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "offset": 122,
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "77c5a497-7b96-45c2-8ece-adc1760cfa8a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FWH5QqGCosGXRrR9qTNz8Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5019,
      "cache_read_input_tokens": 34221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5019
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

_source line 49 · 2026-05-20T04:47:28.722Z_

<details><summary>↩ Tool result · `toolu_0159ivoRncAmpruDyUe4vMuZ`</summary>

```text
122	\subsection{Cross-Logic Extension}
123	\label{sec:crosslogic}
124	
125	As a preliminary cross-logic probe, we replicate the pipeline with Prolog/SWI-Prolog (3 seeds, $\beta{=}0.1$).
126	Under ISR reward, 3/3 seeds reach $0\%$ non-hacking through three distinct mechanisms (TS tautology, classifier-evading pseudo-Prolog, query-as-fact gaming), with one seed evading the strict classifier entirely (Appendix Table~\ref{tab:prolog-detailed}).
127	Complete collapse across all seeds suggests Prolog's simpler operational semantics provides a broader gaming basin than FOL.
128	No matched random control was run for Prolog; the ISR-specificity of these gaming modes is inferred from the FOL random comparison rather than directly demonstrated in Prolog.
129	
130	\subsection{Cross-Scale Evidence}
131	\label{sec:crossscale}
132	
133	We train Qwen3-1.7B under ISR $\beta\in\{0.1,0.3\}$ and Random $\beta{=}0.1$ (3 seeds each, 500 steps; Appendix Table~\ref{tab:crossscale}).
134	Strict non-hacking rates are $0$--$3.7\%$ (ISR $\beta{=}0.1$) and $0$--$29\%$ (ISR $\beta{=}0.3$, driven by a single low-PR seed).
135	1.7B models are constrained to content-independent strategies when PR is high (content-independence $94$--$100\%$ at $\text{PR}{\geq}52\%$); different capacities converge to different Goodhart basins under identical rewards.
136	
137	\subsection{Hacking Taxonomy}
138	\label{sec:taxonomy}
139	
140	
141	\begin{table}[t]
142	\centering
143	\small
144	\resizebox{\columnwidth}{!}{%
145	\begin{tabular}{lccccccc}
146	\toprule
147	\textbf{Mode} & \textbf{Exec}$^a$ & \textbf{ISR$_{.1}$} & \textbf{Rnd$_{.1}$} & \textbf{SFT}$^a$ & \textbf{Prolog$_{\text{ISR}}$} & \textbf{1.7B$_{\text{ISR}}$} & \textbf{1.7B$_{\text{Rnd}}$} \\
148	\midrule
149	CE embed       & 87 & 18 & 59 & 7 & 0$^\sharp$ & 55 & \textbf{81} \\
150	TS duplicate   & 0  & \textbf{54} & 30 & 0 & 100$^\sharp$ & 25 & 0 \\
151	PG prem-subset & 6  & 5  & 8   & 0 & --- & 6 & $<$1 \\
152	Tautological   & --- & --- & --- & --- & s42 & --- & --- \\
153	Repetition     & s43 & --- & --- & --- & --- & --- & --- \\
154	Contradiction  & 1k & --- & --- & --- & --- & --- & --- \\
155	Cmplx.\ vacuous& 0  & 0  & 4  & 0 & --- & --- & --- \\
156	Query-as-fact  & --- & --- & --- & --- & s44 & --- & --- \\
157	\midrule
158	\textbf{Non-hacking}$^\ddagger$ & 8  & \textbf{23}  & 8 & \textbf{92} & \textbf{0} & 15 & 19 \\
159	\bottomrule
160	\end{tabular}}
161	\caption{Hacking modes (\% of proved). $^a$Single seed (s42); remaining columns pooled (ISR/Rnd 4B: 5-seed; Prolog/1.7B: 3-seed). $^\sharp$Prolog: strict+functional pooled. $^\ddagger$1.7B N-H overestimates true rate: strict non-hacking (S-NH; \S\ref{sec:rewards}) is $0$--$3.7\%$ (ISR $\beta{=}0.1$), $0\%$ (Rnd $\beta{=}0.1$), $0$--$29\%$ (ISR $\beta{=}0.3$); CI undetected by classifier at 1.7B.}
162	\label{tab:hacking-taxonomy}
163	\end{table}
164	
165	Eight modes are detected by automated classifiers (Table~\ref{tab:hacking-taxonomy}; Appendix~\ref{app:hacking-modes}); CI (contradiction injection) is identified via manual audit at 1.7B in a single seed (s42, Random $\beta{=}0.1$) and may not generalize.
166	CE, TS, and PG account for ${>}90\%$ of hacking across ${\geq}3$ seeds each; ISR modestly increases TS probability ($\text{OR}{=}2.84$; Appendix Table~\ref{tab:bootstrap-ci}), but per-seed variance dominates.
167	All GRPO conditions show ${\geq}80\%$ pooled hacking; only SFT achieves $92.3\%$ non-hacking.
168	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "2daab43e-70c7-4c16-94f1-ad20b410629e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
      "content": "\\subsection{Cross-Logic Extension}\n\\label{sec:crosslogic}\n\nAs a preliminary cross-logic probe, we replicate the pipeline with Prolog/SWI-Prolog (3 seeds, $\\beta{=}0.1$).\nUnder ISR reward, 3/3 seeds reach $0\\%$ non-hacking through three distinct mechanisms (TS tautology, classifier-evading pseudo-Prolog, query-as-fact gaming), with one seed evading the strict classifier entirely (Appendix Table~\\ref{tab:prolog-detailed}).\nComplete collapse across all seeds suggests Prolog's simpler operational semantics provides a broader gaming basin than FOL.\nNo matched random control was run for Prolog; the ISR-specificity of these gaming modes is inferred from the FOL random comparison rather than directly demonstrated in Prolog.\n\n\\subsection{Cross-Scale Evidence}\n\\label{sec:crossscale}\n\nWe train Qwen3-1.7B under ISR $\\beta\\in\\{0.1,0.3\\}$ and Random $\\beta{=}0.1$ (3 seeds each, 500 steps; Appendix Table~\\ref{tab:crossscale}).\nStrict non-hacking rates are $0$--$3.7\\%$ (ISR $\\beta{=}0.1$) and $0$--$29\\%$ (ISR $\\beta{=}0.3$, driven by a single low-PR seed).\n1.7B models are constrained to content-independent strategies when PR is high (content-independence $94$--$100\\%$ at $\\text{PR}{\\geq}52\\%$); different capacities converge to different Goodhart basins under identical rewards.\n\n\\subsection{Hacking Taxonomy}\n\\label{sec:taxonomy}\n\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccccc}\n\\toprule\n\\textbf{Mode} & \\textbf{Exec}$^a$ & \\textbf{ISR$_{.1}$} & \\textbf{Rnd$_{.1}$} & \\textbf{SFT}$^a$ & \\textbf{Prolog$_{\\text{ISR}}$} & \\textbf{1.7B$_{\\text{ISR}}$} & \\textbf{1.7B$_{\\text{Rnd}}$} \\\\\n\\midrule\nCE embed       & 87 & 18 & 59 & 7 & 0$^\\sharp$ & 55 & \\textbf{81} \\\\\nTS duplicate   & 0  & \\textbf{54} & 30 & 0 & 100$^\\sharp$ & 25 & 0 \\\\\nPG prem-subset & 6  & 5  & 8   & 0 & --- & 6 & $<$1 \\\\\nTautological   & --- & --- & --- & --- & s42 & --- & --- \\\\\nRepetition     & s43 & --- & --- & --- & --- & --- & --- \\\\\nContradiction  & 1k & --- & --- & --- & --- & --- & --- \\\\\nCmplx.\\ vacuous& 0  & 0  & 4  & 0 & --- & --- & --- \\\\\nQuery-as-fact  & --- & --- & --- & --- & s44 & --- & --- \\\\\n\\midrule\n\\textbf{Non-hacking}$^\\ddagger$ & 8  & \\textbf{23}  & 8 & \\textbf{92} & \\textbf{0} & 15 & 19 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Hacking modes (\\% of proved). $^a$Single seed (s42); remaining columns pooled (ISR/Rnd 4B: 5-seed; Prolog/1.7B: 3-seed). $^\\sharp$Prolog: strict+functional pooled. $^\\ddagger$1.7B N-H overestimates true rate: strict non-hacking (S-NH; \\S\\ref{sec:rewards}) is $0$--$3.7\\%$ (ISR $\\beta{=}0.1$), $0\\%$ (Rnd $\\beta{=}0.1$), $0$--$29\\%$ (ISR $\\beta{=}0.3$); CI undetected by classifier at 1.7B.}\n\\label{tab:hacking-taxonomy}\n\\end{table}\n\nEight modes are detected by automated classifiers (Table~\\ref{tab:hacking-taxonomy}; Appendix~\\ref{app:hacking-modes}); CI (contradiction injection) is identified via manual audit at 1.7B in a single seed (s42, Random $\\beta{=}0.1$) and may not generalize.\nCE, TS, and PG account for ${>}90\\%$ of hacking across ${\\geq}3$ seeds each; ISR modestly increases TS probability ($\\text{OR}{=}2.84$; Appendix Table~\\ref{tab:bootstrap-ci}), but per-seed variance dominates.\nAll GRPO conditions show ${\\geq}80\\%$ pooled hacking; only SFT achieves $92.3\\%$ non-hacking.\n",
      "numLines": 47,
      "startLine": 122,
      "totalLines": 168
    }
  }
}
```

</details>

---

### Tool call

_source line 50_

<details open><summary>🔧 Tool call — Read · `toolu_018ya1kgbaniV37U62Va5dsN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
  "offset": 88,
  "limit": 35
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "e8c57a4e-cf73-4cd2-9e67-b0fd34779bbe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FWH5QqGCosGXRrR9qTNz8Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5019,
      "cache_read_input_tokens": 34221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5019
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

_source line 51 · 2026-05-20T04:47:29.544Z_

<details><summary>↩ Tool result · `toolu_018ya1kgbaniV37U62Va5dsN`</summary>

```text
88	A formalization with 2 premises where both are necessary yields ISR${=}1.0$; one with 10 premises where 8 are necessary yields ISR${=}0.8$, even though the latter encodes richer reasoning.
89	This confound is central to ISR's Goodhart vulnerability: TS tautologies (single premise $=$ conclusion) achieve $\text{ISR}{\geq}0.5$ \emph{by construction}, and the shorter formalizations produced by non-collapsed seeds at $\beta{=}0.1$ also inflate ISR mechanically.
90	Premise-count-matched comparison on non-hacking samples yields $\text{ISR}^{*}{=}0.258$ vs.\ $0.243$ for random ($1.06\times$; Table~\ref{tab:fol-beta01-detailed}), confirming that even within the transient non-hacking window the structural benefit is negligible.
91	This bias is not specific to our setting; any LOO-based structural metric applied to variable-length outputs requires component-count normalization.
92	We recommend that future work employing ablation-based diagnostics report premise-count-matched comparisons alongside raw values.
93	
94	\begin{table}[!htb]
95	\centering
96	\caption{Fisher exact tests across conditions. Non-hacking rate reported at 5-seed (primary) and 3-seed with PG+FN corrections (sensitivity); TS comparison at 5-seed (primary) and 3-seed (sensitivity).}
97	\label{tab:bootstrap-ci}
98	\small
99	\resizebox{\columnwidth}{!}{%
100	\begin{tabular}{@{}lcccc@{}}
101	\toprule
102	\textbf{Comparison} & \textbf{Condition} & \textbf{Control} & \textbf{OR} & \textbf{$p$} \\
103	\midrule
104	\multicolumn{5}{@{}l}{\textit{Non-hacking rate (5-seed)}} \\
105	ISR vs.\ Random & 22.6\% {\scriptsize[18.2,27.0]} & 7.7\% {\scriptsize[5.5,10.7]} & 3.48 & ${<}10^{-8}$ \\
106	\multicolumn{5}{@{}l}{\textit{Non-hacking rate (3-seed, PG+FN corrected)}} \\
107	ISR vs.\ Random & 6.06\% {\scriptsize[3.6,9.9]} & 9.5\% {\scriptsize[6.5,13.7]} & 0.61 & 0.182 (n.s.) \\
108	\midrule
109	\multicolumn{5}{@{}l}{\textit{TS gaming rate (5-seed)}} \\
110	ISR vs.\ Random & 54.3\% {\scriptsize[49.1,59.5]} & 29.5\% {\scriptsize[25.1,33.9]} & 2.84 & $4.82{\times}10^{-12}$ \\
111	\multicolumn{5}{@{}l}{\textit{TS gaming rate (3-seed sensitivity)}} \\
112	ISR vs.\ Random & 70.6\% {\scriptsize[64.3,76.3]} & 13.7\% {\scriptsize[9.9,18.6]} & 15.05 & $1.3{\times}10^{-39}$ \\
113	\midrule
114	\multicolumn{5}{@{}l}{\textit{SFT vs.\ Exec-only non-hacking rate}} \\
115	SFT vs.\ Exec-only & 92.3\% {\scriptsize[79.7,97.3]} & 7.5\% & 147 & ${<}0.001$ \\
116	\bottomrule
117	\end{tabular}}
118	\\[2pt]
119	{\footnotesize 5-seed: ISR $n{=}350$, Random $n{=}414$. 3-seed: ISR $n{=}231$, Random $n{=}262$. Exec-only: $n{=}93$ (s42). SFT: $n{=}39$ (3 seeds, 1000 steps). 95\% Wilson CIs in brackets where shown.}
120	\end{table}
121	
122	\paragraph{Seed-level statistical analysis.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "786cb8cf-911b-4099-a11c-45906b18029a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
      "content": "A formalization with 2 premises where both are necessary yields ISR${=}1.0$; one with 10 premises where 8 are necessary yields ISR${=}0.8$, even though the latter encodes richer reasoning.\nThis confound is central to ISR's Goodhart vulnerability: TS tautologies (single premise $=$ conclusion) achieve $\\text{ISR}{\\geq}0.5$ \\emph{by construction}, and the shorter formalizations produced by non-collapsed seeds at $\\beta{=}0.1$ also inflate ISR mechanically.\nPremise-count-matched comparison on non-hacking samples yields $\\text{ISR}^{*}{=}0.258$ vs.\\ $0.243$ for random ($1.06\\times$; Table~\\ref{tab:fol-beta01-detailed}), confirming that even within the transient non-hacking window the structural benefit is negligible.\nThis bias is not specific to our setting; any LOO-based structural metric applied to variable-length outputs requires component-count normalization.\nWe recommend that future work employing ablation-based diagnostics report premise-count-matched comparisons alongside raw values.\n\n\\begin{table}[!htb]\n\\centering\n\\caption{Fisher exact tests across conditions. Non-hacking rate reported at 5-seed (primary) and 3-seed with PG+FN corrections (sensitivity); TS comparison at 5-seed (primary) and 3-seed (sensitivity).}\n\\label{tab:bootstrap-ci}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Comparison} & \\textbf{Condition} & \\textbf{Control} & \\textbf{OR} & \\textbf{$p$} \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{Non-hacking rate (5-seed)}} \\\\\nISR vs.\\ Random & 22.6\\% {\\scriptsize[18.2,27.0]} & 7.7\\% {\\scriptsize[5.5,10.7]} & 3.48 & ${<}10^{-8}$ \\\\\n\\multicolumn{5}{@{}l}{\\textit{Non-hacking rate (3-seed, PG+FN corrected)}} \\\\\nISR vs.\\ Random & 6.06\\% {\\scriptsize[3.6,9.9]} & 9.5\\% {\\scriptsize[6.5,13.7]} & 0.61 & 0.182 (n.s.) \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{TS gaming rate (5-seed)}} \\\\\nISR vs.\\ Random & 54.3\\% {\\scriptsize[49.1,59.5]} & 29.5\\% {\\scriptsize[25.1,33.9]} & 2.84 & $4.82{\\times}10^{-12}$ \\\\\n\\multicolumn{5}{@{}l}{\\textit{TS gaming rate (3-seed sensitivity)}} \\\\\nISR vs.\\ Random & 70.6\\% {\\scriptsize[64.3,76.3]} & 13.7\\% {\\scriptsize[9.9,18.6]} & 15.05 & $1.3{\\times}10^{-39}$ \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{SFT vs.\\ Exec-only non-hacking rate}} \\\\\nSFT vs.\\ Exec-only & 92.3\\% {\\scriptsize[79.7,97.3]} & 7.5\\% & 147 & ${<}0.001$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\\\[2pt]\n{\\footnotesize 5-seed: ISR $n{=}350$, Random $n{=}414$. 3-seed: ISR $n{=}231$, Random $n{=}262$. Exec-only: $n{=}93$ (s42). SFT: $n{=}39$ (3 seeds, 1000 steps). 95\\% Wilson CIs in brackets where shown.}\n\\end{table}\n\n\\paragraph{Seed-level statistical analysis.}",
      "numLines": 35,
      "startLine": 88,
      "totalLines": 858
    }
  }
}
```

</details>

---

### Tool call

_source line 52_

<details open><summary>🔧 Tool call — Read · `toolu_012dpM5DQAqkqXkqcJw9BQ1a`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
  "offset": 175,
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
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "7284742b-e657-43cc-a47e-8d1d502273e5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FWH5QqGCosGXRrR9qTNz8Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5019,
      "cache_read_input_tokens": 34221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5019
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

_source line 53 · 2026-05-20T04:47:30.479Z_

<details><summary>↩ Tool result · `toolu_012dpM5DQAqkqXkqcJw9BQ1a`</summary>

```text
175	s43 & 97 & 0.96 & 96.9 & 0 \\
176	s44 & 93 & 0.55 & 100 & 0 \\
177	\midrule
178	\textbf{Pooled} & 97$\pm$4 & 0.69$\pm$0.24 & 99.0 & \textbf{0} \\
179	\bottomrule
180	\end{tabular}
181	\end{table}
182	
183	\paragraph{Goodhart effects: implications.}
184	The finding extends beyond this specific system.
185	ISR was designed to \emph{detect} reward gaming of $r_{\text{exec}}$, yet it contains an inherent structural vulnerability: by its LOO definition, single-premise-equals-conclusion constructions receive artificially high ISR ($\text{ISR}{\geq}0.5$; empirically 93\% at $\text{ISR}{=}0.5$, 7\% at $\text{ISR}{=}1.0$; 5-seed ISR $\beta{=}0.1$ pooled TS samples), creating a positive feedback loop once sampled during GRPO rollouts~\citep{karwowski-goodhart-rl, kwa-catastrophic-goodhart}.
186	Goodhart collapse~\citep{manheim-goodhart-taxonomy} is observed at all four tested doses ($\beta{=}0.05$: 3 seeds; $\beta\in\{0.1, 0.2, 0.3\}$: 3--5 seeds each).
187	The structural bias predicts universality (TS tautology is always the global reward-maximizing exploit regardless of $\beta$), and $\beta$ controls only the probability of early sampling and thus the timing of collapse; at $\beta{=}0.05$, three seeds confirm deterministic TS collapse ($93.7\%$ pooled) while the matched random control at the same $\beta$ produces CE redundancy instead ($77.4\%$), ruling out dose magnitude as the driver.
188	At moderate doses ($\beta{=}0.1$), collapse is stochastic and delayed (5 seeds bifurcate: 2 collapse rapidly, 3 sustain a transient non-hacking window that trajectory analysis confirms is temporary); at higher doses ($\beta{=}0.2$), collapse is immediate and universal.
189	$\beta{=}0.3$ adds reward collapse~\citep{gao-reward-overoptimization} as a competing failure mode (PR drops to 18\% in 1/3 seeds), but the underlying Goodhart vulnerability remains the same.
190	The practical implication is that ISR (and structurally similar LOO-based diagnostics) should be used exclusively as post-hoc evaluation tools, never as training rewards.
191	
192	\paragraph{Single-seed unreliability.}
193	The three exec-only seeds diverge radically (PR $\sigma{=}47$ percentage points), each converging to a qualitatively different degeneration mode (\S\ref{sec:diagnostic}).
194	ISR $\beta{=}0.1$ (5 seeds) shows even greater instability: 2/5 seeds collapse to TS within ${\sim}150$ steps, while 3/5 sustain a transient non-hacking window.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "98d52f32-9da5-4eb0-9a64-1ef5099ac576",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
      "content": "s43 & 97 & 0.96 & 96.9 & 0 \\\\\ns44 & 93 & 0.55 & 100 & 0 \\\\\n\\midrule\n\\textbf{Pooled} & 97$\\pm$4 & 0.69$\\pm$0.24 & 99.0 & \\textbf{0} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Goodhart effects: implications.}\nThe finding extends beyond this specific system.\nISR was designed to \\emph{detect} reward gaming of $r_{\\text{exec}}$, yet it contains an inherent structural vulnerability: by its LOO definition, single-premise-equals-conclusion constructions receive artificially high ISR ($\\text{ISR}{\\geq}0.5$; empirically 93\\% at $\\text{ISR}{=}0.5$, 7\\% at $\\text{ISR}{=}1.0$; 5-seed ISR $\\beta{=}0.1$ pooled TS samples), creating a positive feedback loop once sampled during GRPO rollouts~\\citep{karwowski-goodhart-rl, kwa-catastrophic-goodhart}.\nGoodhart collapse~\\citep{manheim-goodhart-taxonomy} is observed at all four tested doses ($\\beta{=}0.05$: 3 seeds; $\\beta\\in\\{0.1, 0.2, 0.3\\}$: 3--5 seeds each).\nThe structural bias predicts universality (TS tautology is always the global reward-maximizing exploit regardless of $\\beta$), and $\\beta$ controls only the probability of early sampling and thus the timing of collapse; at $\\beta{=}0.05$, three seeds confirm deterministic TS collapse ($93.7\\%$ pooled) while the matched random control at the same $\\beta$ produces CE redundancy instead ($77.4\\%$), ruling out dose magnitude as the driver.\nAt moderate doses ($\\beta{=}0.1$), collapse is stochastic and delayed (5 seeds bifurcate: 2 collapse rapidly, 3 sustain a transient non-hacking window that trajectory analysis confirms is temporary); at higher doses ($\\beta{=}0.2$), collapse is immediate and universal.\n$\\beta{=}0.3$ adds reward collapse~\\citep{gao-reward-overoptimization} as a competing failure mode (PR drops to 18\\% in 1/3 seeds), but the underlying Goodhart vulnerability remains the same.\nThe practical implication is that ISR (and structurally similar LOO-based diagnostics) should be used exclusively as post-hoc evaluation tools, never as training rewards.\n\n\\paragraph{Single-seed unreliability.}\nThe three exec-only seeds diverge radically (PR $\\sigma{=}47$ percentage points), each converging to a qualitatively different degeneration mode (\\S\\ref{sec:diagnostic}).\nISR $\\beta{=}0.1$ (5 seeds) shows even greater instability: 2/5 seeds collapse to TS within ${\\sim}150$ steps, while 3/5 sustain a transient non-hacking window.",
      "numLines": 20,
      "startLine": 175,
      "totalLines": 858
    }
  }
}
```

</details>

---

### Tool call

_source line 54_

<details open><summary>🔧 Tool call — Read · `toolu_0165gvzbhnDoqWyuCfasFbgw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
  "offset": 695,
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
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "623d1bdf-1d75-4474-ab81-a22744f9e80e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FWH5QqGCosGXRrR9qTNz8Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5019,
      "cache_read_input_tokens": 34221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5019
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

_source line 55 · 2026-05-20T04:47:31.090Z_

<details><summary>↩ Tool result · `toolu_0165gvzbhnDoqWyuCfasFbgw`</summary>

```text
695	\label{app:beta005}
696	
697	The 3-seed random control at $\beta{=}0.05$ is highly unstable: s42 fails entirely ($\text{PR}{=}0\%$), s44 barely learns ($\text{PR}{=}7\%$, CE $71\%$, non-hacking $0\%$), and only s43 reaches moderate output ($\text{PR}{=}62\%$, CE $77\%$, non-hacking $13\%$).
698	The single random seed that learns (s43) shows higher non-hacking output than ISR ($13\%$ vs.\ $5.1\%$ pooled), consistent with a signal-floor below which ISR's non-hacking component is undetectable while its TS bias remains exploitable.
699	
700	\subsection{Early-Training Hacking Analysis (100-Step Checkpoint)}
701	\label{app:100step}
702	
703	To control for the prove-rate confound in our SFT comparison (\S\ref{sec:diagnostic}), we analyze the exec-only checkpoint at 100 training steps (seed~42), where PR${=}32$\%, higher than SFT (13.0\%, 3-seed pooled) but still early in training.
704	Of the 32 proved samples, 9 (28.1\%) exhibit TS hacking (single premise identical to conclusion) and 1 (3.1\%) exhibits CE (conclusion embedded among premises), yielding a total hacking rate of 31.2\%.
705	By contrast, SFT at comparable or lower PR shows 7.7\% hacking (1/13 proved samples).
706	This demonstrates that reward hacking emerges early in GRPO training, well before the prove-rate plateau, and is not simply an artifact of having more proved samples available for exploitation.
707	The 100-step hacking rate (31.2\%) is already substantially above SFT (7.7\%), supporting the claim that hacking is associated with RL optimization rather than prove-rate level alone.
708	
709	\subsection{$O(1)$ vs.\ $O(n)$ ISR Ablation}
710	\label{app:o1-ablation}
711	
712	To justify the per-clause LOO design (\S\ref{sec:sta}), we train a variant that replaces the $O(n)$ ablation with a cheaper $O(1)$ binary signal: $\text{fast\_ISR}(x) = 1$ if $x$ is proved \emph{and} the conclusion is not provable under empty premises (tautology check), $0$ otherwise.
713	The reward becomes $r = 0.5\,r_{\text{exec}} + 0.5\,\text{fast\_ISR}$.
714	After 500 steps (seed~42), this variant achieves $\text{PR}{=}63\%$ with $\text{ISR}^*{=}0.007$ (functionally zero), compared to $\text{ISR}^*{=}0.132$ under standard exec-only and $\text{ISR}^*{=}0.42$ under ISR $\beta{=}0.1$.
715	
716	\paragraph{ISR signal vs.\ training dynamics.}
717	At the \emph{ISR signal level}, the $O(1)$ variant is indistinguishable from exec-only: both produce near-zero ISR because models emit redundant premise copies whose individual removal never changes the proof outcome.
718	At the \emph{training level}, the two conditions are non-equivalent: the $O(1)$ tautology check penalizes formalizations where the conclusion is provable without any premises, a constraint absent from exec-only.
719	This confound depresses prove rate by 30 percentage points ($63\%$ vs.\ $93\%$ exec-only), making it impossible to attribute the difference purely to the ISR signal.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "11012660-8ade-4b17-b375-190fad27684f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
      "content": "\\label{app:beta005}\n\nThe 3-seed random control at $\\beta{=}0.05$ is highly unstable: s42 fails entirely ($\\text{PR}{=}0\\%$), s44 barely learns ($\\text{PR}{=}7\\%$, CE $71\\%$, non-hacking $0\\%$), and only s43 reaches moderate output ($\\text{PR}{=}62\\%$, CE $77\\%$, non-hacking $13\\%$).\nThe single random seed that learns (s43) shows higher non-hacking output than ISR ($13\\%$ vs.\\ $5.1\\%$ pooled), consistent with a signal-floor below which ISR's non-hacking component is undetectable while its TS bias remains exploitable.\n\n\\subsection{Early-Training Hacking Analysis (100-Step Checkpoint)}\n\\label{app:100step}\n\nTo control for the prove-rate confound in our SFT comparison (\\S\\ref{sec:diagnostic}), we analyze the exec-only checkpoint at 100 training steps (seed~42), where PR${=}32$\\%, higher than SFT (13.0\\%, 3-seed pooled) but still early in training.\nOf the 32 proved samples, 9 (28.1\\%) exhibit TS hacking (single premise identical to conclusion) and 1 (3.1\\%) exhibits CE (conclusion embedded among premises), yielding a total hacking rate of 31.2\\%.\nBy contrast, SFT at comparable or lower PR shows 7.7\\% hacking (1/13 proved samples).\nThis demonstrates that reward hacking emerges early in GRPO training, well before the prove-rate plateau, and is not simply an artifact of having more proved samples available for exploitation.\nThe 100-step hacking rate (31.2\\%) is already substantially above SFT (7.7\\%), supporting the claim that hacking is associated with RL optimization rather than prove-rate level alone.\n\n\\subsection{$O(1)$ vs.\\ $O(n)$ ISR Ablation}\n\\label{app:o1-ablation}\n\nTo justify the per-clause LOO design (\\S\\ref{sec:sta}), we train a variant that replaces the $O(n)$ ablation with a cheaper $O(1)$ binary signal: $\\text{fast\\_ISR}(x) = 1$ if $x$ is proved \\emph{and} the conclusion is not provable under empty premises (tautology check), $0$ otherwise.\nThe reward becomes $r = 0.5\\,r_{\\text{exec}} + 0.5\\,\\text{fast\\_ISR}$.\nAfter 500 steps (seed~42), this variant achieves $\\text{PR}{=}63\\%$ with $\\text{ISR}^*{=}0.007$ (functionally zero), compared to $\\text{ISR}^*{=}0.132$ under standard exec-only and $\\text{ISR}^*{=}0.42$ under ISR $\\beta{=}0.1$.\n\n\\paragraph{ISR signal vs.\\ training dynamics.}\nAt the \\emph{ISR signal level}, the $O(1)$ variant is indistinguishable from exec-only: both produce near-zero ISR because models emit redundant premise copies whose individual removal never changes the proof outcome.\nAt the \\emph{training level}, the two conditions are non-equivalent: the $O(1)$ tautology check penalizes formalizations where the conclusion is provable without any premises, a constraint absent from exec-only.\nThis confound depresses prove rate by 30 percentage points ($63\\%$ vs.\\ $93\\%$ exec-only), making it impossible to attribute the difference purely to the ISR signal.",
      "numLines": 25,
      "startLine": 695,
      "totalLines": 858
    }
  }
}
```

</details>

---

### Assistant

_source line 56_

<details><summary>Logged reasoning block</summary>

```text
Now let me also check the ProofFOL genuine rate permutation test mentioned in the docs/paper/experiments.tex and appendix.

From what I've gathered so far, let me also look for the ProofFOL genuine rate permutation test p=0.10 mentioned in docs/paper/.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "127a6e56-5ecd-4deb-9143-5d71b8842eff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PnbxBPwCuiyyaXF6rnhQB7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6149,
      "cache_read_input_tokens": 39240,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6149
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

_source line 57_

Let me check the ProofFOL permutation test and look for additional tests in the docs/paper versions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "5e2417b7-fd80-4da9-9c33-3b672f005779",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PnbxBPwCuiyyaXF6rnhQB7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6149,
      "cache_read_input_tokens": 39240,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6149
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

_source line 58_

<details open><summary>🔧 Tool call — Read · `toolu_01CfU1LnwBvwyjojRnu6QwcG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex",
  "offset": 125,
  "limit": 15
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "1088eb11-9a58-4a76-b22e-4e2bad717450",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PnbxBPwCuiyyaXF6rnhQB7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6149,
      "cache_read_input_tokens": 39240,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6149
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

_source line 59 · 2026-05-20T04:47:38.346Z_

<details><summary>↩ Tool result · `toolu_01CfU1LnwBvwyjojRnu6QwcG`</summary>

```text
125	All seeds have $\text{ISR}^*{<}0.12$---far below the pre-training baseline ($0.31$)---consistent with the LOO tautological attractor being metric-intrinsic.
126	
127	\textbf{ProofFOL ISR ($\beta{=}0.1$): beneficial instability.}
128	ISR bonus reduces stable convergence from 2/3 to 0/3 seeds---superficially, another optimization failure.
129	Hacking-mode classification reverses this reading: ISR seeds average 76.8\% genuine versus 17.4\% for exec-only (permutation $p{=}0.10$, $N{=}3$), with s42 and s44 achieving 100\% genuine despite training collapse (Table~\ref{tab:prooffol-detailed}).
130	The models that failed to converge produced structurally honest proofs.
131	
132	\textbf{Mechanism.}
133	Eval-time ISR confirms the asymmetry: on ProofFOL, hacking constructions yield $\text{ISR}{=}0.0$ while genuine proofs yield $\text{ISR}{=}0.27$ (s42) and $0.20$ (s44)---ISR correctly penalizes shortcuts.
134	On FOLIO (baseline $\text{ISR}^*{\approx}0.50$), $P{\to}P$ yields $\text{ISR}{\geq}0.5$, so ISR erroneously rewards tautological hacking (regressional Goodhart~\citep{manheim-goodhart-taxonomy}); on ProofFOL (baseline $\text{ISR}^*{=}0.31$), hacking does not satisfy ISR, so the bonus correctly suppresses shortcuts at the cost of convergence stability.
135	The same metric produces opposite outcomes---Goodhart collapse where hacking satisfies it (FOLIO), beneficial instability where it does not (ProofFOL)---determined by the dataset's hacking geometry.
136	
137	\subsection{Hacking Taxonomy}
138	\label{sec:taxonomy}
139	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "e0c3fce9-e833-4889-a4e7-158ec73a335e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex",
      "content": "All seeds have $\\text{ISR}^*{<}0.12$---far below the pre-training baseline ($0.31$)---consistent with the LOO tautological attractor being metric-intrinsic.\n\n\\textbf{ProofFOL ISR ($\\beta{=}0.1$): beneficial instability.}\nISR bonus reduces stable convergence from 2/3 to 0/3 seeds---superficially, another optimization failure.\nHacking-mode classification reverses this reading: ISR seeds average 76.8\\% genuine versus 17.4\\% for exec-only (permutation $p{=}0.10$, $N{=}3$), with s42 and s44 achieving 100\\% genuine despite training collapse (Table~\\ref{tab:prooffol-detailed}).\nThe models that failed to converge produced structurally honest proofs.\n\n\\textbf{Mechanism.}\nEval-time ISR confirms the asymmetry: on ProofFOL, hacking constructions yield $\\text{ISR}{=}0.0$ while genuine proofs yield $\\text{ISR}{=}0.27$ (s42) and $0.20$ (s44)---ISR correctly penalizes shortcuts.\nOn FOLIO (baseline $\\text{ISR}^*{\\approx}0.50$), $P{\\to}P$ yields $\\text{ISR}{\\geq}0.5$, so ISR erroneously rewards tautological hacking (regressional Goodhart~\\citep{manheim-goodhart-taxonomy}); on ProofFOL (baseline $\\text{ISR}^*{=}0.31$), hacking does not satisfy ISR, so the bonus correctly suppresses shortcuts at the cost of convergence stability.\nThe same metric produces opposite outcomes---Goodhart collapse where hacking satisfies it (FOLIO), beneficial instability where it does not (ProofFOL)---determined by the dataset's hacking geometry.\n\n\\subsection{Hacking Taxonomy}\n\\label{sec:taxonomy}\n",
      "numLines": 15,
      "startLine": 125,
      "totalLines": 174
    }
  }
}
```

</details>

---

### Tool call

_source line 60_

<details open><summary>🔧 Tool call — Read · `toolu_01ALgaSJZZ1XXDHGYZ4BCLYZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex",
  "offset": 510,
  "limit": 15
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "1f68b2f0-eeb7-4418-8a5f-dcbe7a0f97aa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PnbxBPwCuiyyaXF6rnhQB7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6149,
      "cache_read_input_tokens": 39240,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6149
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

_source line 61 · 2026-05-20T04:47:38.793Z_

<details><summary>↩ Tool result · `toolu_01ALgaSJZZ1XXDHGYZ4BCLYZ`</summary>

```text
510	  & 44 & 0.49 & 0.145 & 0 & 0 & \textbf{100} & $n{=}66$; oscillation \\
511	\cmidrule(l){2-8}
512	  & \multicolumn{2}{l}{Aggregate} & & \multicolumn{3}{c}{\textbf{76.8\%} genuine (mean of seeds)} & \\
513	\bottomrule
514	\end{tabular}
515	
516	\vspace{4pt}
517	{\footnotesize Aggregate genuine rate: mean of per-seed genuine rates. Permutation test (exec vs.\ ISR genuine): $p{=}0.10$, $N{=}3$ per group.}
518	\end{table*}
519	
520	\paragraph{ISR collapse trajectory (FOL exec-only, seed 42).}
521	Table~\ref{tab:fol-detailed} traces the ISR collapse over training:
522	ISR$^*=0.642$ at 100 steps $\to$ $0.132$ at 500 steps ($-79.4$\%) $\to$ $0.003$ at 1000 steps ($-99.5$\% from step 100).
523	PR increases monotonically ($0.32 \to 0.93 \to 0.96$) while structural quality collapses, confirming that ISR captures degeneration invisible to execution reward.
524	By step 1000, 94.8\% of proved samples have ISR~$=0$ and the mean component count rises to 18.55.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "5b586ec9-b0d6-44a7-b428-ea49165b1513",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex",
      "content": "  & 44 & 0.49 & 0.145 & 0 & 0 & \\textbf{100} & $n{=}66$; oscillation \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{Aggregate} & & \\multicolumn{3}{c}{\\textbf{76.8\\%} genuine (mean of seeds)} & \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{4pt}\n{\\footnotesize Aggregate genuine rate: mean of per-seed genuine rates. Permutation test (exec vs.\\ ISR genuine): $p{=}0.10$, $N{=}3$ per group.}\n\\end{table*}\n\n\\paragraph{ISR collapse trajectory (FOL exec-only, seed 42).}\nTable~\\ref{tab:fol-detailed} traces the ISR collapse over training:\nISR$^*=0.642$ at 100 steps $\\to$ $0.132$ at 500 steps ($-79.4$\\%) $\\to$ $0.003$ at 1000 steps ($-99.5$\\% from step 100).\nPR increases monotonically ($0.32 \\to 0.93 \\to 0.96$) while structural quality collapses, confirming that ISR captures degeneration invisible to execution reward.\nBy step 1000, 94.8\\% of proved samples have ISR~$=0$ and the mean component count rises to 18.55.",
      "numLines": 15,
      "startLine": 510,
      "totalLines": 599
    }
  }
}
```

</details>

---

### Tool call

_source line 62_

<details open><summary>🔧 Tool call — Read · `toolu_015y4fsoEyqtYHn9X5U2wg5S`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
  "offset": 840,
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
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "c7eac5b4-b236-400b-8429-1badd58ebb45",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PnbxBPwCuiyyaXF6rnhQB7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6149,
      "cache_read_input_tokens": 39240,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6149
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

_source line 63 · 2026-05-20T04:47:39.699Z_

<details><summary>↩ Tool result · `toolu_015y4fsoEyqtYHn9X5U2wg5S`</summary>

```text
840	Two seeds produce predominantly non-hacking output (s54: 96.7\%, s57: 63.6\%), though s54 has 35.2\% content-independent samples.
841	The high variance across seeds (TS, PG, and genuine outcomes all observed) reinforces that component-count gating is insufficient for reliable structural improvement.
842	
843	\subsection{Cross-Model Generalization: LLaMA-3.2-3B Cold-Start Failure}
844	\label{app:llama-coldstart}
845	
846	To probe cross-architecture generalization, we applied the identical GRPO configuration (Table~\ref{tab:hyperparams}) to LLaMA-3.2-3B~\citep{grattafiori2024llama} (3B parameters; execution-only reward, seed~42, $K{=}4$ rollouts, FOLIO training set).
847	
848	The model produced zero valid Prover9 output across 72 of the planned 500 training steps: reward, policy loss, and gradient norm remained at zero throughout, and training was terminated early.
849	Manual inspection of generations revealed natural-language text (e.g., homework-style problem restatements and conversational responses) with no first-order logic syntax.
850	Because $r_{\text{exec}}{=}0$ for all $K$ rollouts on every prompt, the GRPO advantage signal is identically zero and no policy update occurs.
851	
852	This result establishes a \emph{capability threshold} for GRPO-based formalization: the base model must possess at minimum a rudimentary ability to generate syntactically valid solver input for the RL loop to produce any learning signal.
853	Qwen3-4B crosses this threshold (non-zero prove rates within the first 10 steps), while LLaMA-3.2-3B~\citep{grattafiori2024llama} does not despite comparable parameter count (3B vs.\ 4B).
854	The failure likely reflects differences in pretraining data composition---specifically, exposure to formal logic and structured symbolic syntax---rather than model scale \emph{per se}.
855	
856	An SFT warmstart phase (supervised fine-tuning on a small set of gold formalizations before switching to GRPO) could potentially lift models below this threshold into the regime where RL training produces signal.
857	This implies that the hacking phenomena reported in the main paper require models already capable of producing structurally valid output; below the capability threshold, RL produces no signal rather than degenerate signal.
858	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "8e948549-883a-4c79-ab24-4a1c08b7ff6f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
      "content": "Two seeds produce predominantly non-hacking output (s54: 96.7\\%, s57: 63.6\\%), though s54 has 35.2\\% content-independent samples.\nThe high variance across seeds (TS, PG, and genuine outcomes all observed) reinforces that component-count gating is insufficient for reliable structural improvement.\n\n\\subsection{Cross-Model Generalization: LLaMA-3.2-3B Cold-Start Failure}\n\\label{app:llama-coldstart}\n\nTo probe cross-architecture generalization, we applied the identical GRPO configuration (Table~\\ref{tab:hyperparams}) to LLaMA-3.2-3B~\\citep{grattafiori2024llama} (3B parameters; execution-only reward, seed~42, $K{=}4$ rollouts, FOLIO training set).\n\nThe model produced zero valid Prover9 output across 72 of the planned 500 training steps: reward, policy loss, and gradient norm remained at zero throughout, and training was terminated early.\nManual inspection of generations revealed natural-language text (e.g., homework-style problem restatements and conversational responses) with no first-order logic syntax.\nBecause $r_{\\text{exec}}{=}0$ for all $K$ rollouts on every prompt, the GRPO advantage signal is identically zero and no policy update occurs.\n\nThis result establishes a \\emph{capability threshold} for GRPO-based formalization: the base model must possess at minimum a rudimentary ability to generate syntactically valid solver input for the RL loop to produce any learning signal.\nQwen3-4B crosses this threshold (non-zero prove rates within the first 10 steps), while LLaMA-3.2-3B~\\citep{grattafiori2024llama} does not despite comparable parameter count (3B vs.\\ 4B).\nThe failure likely reflects differences in pretraining data composition---specifically, exposure to formal logic and structured symbolic syntax---rather than model scale \\emph{per se}.\n\nAn SFT warmstart phase (supervised fine-tuning on a small set of gold formalizations before switching to GRPO) could potentially lift models below this threshold into the regime where RL training produces signal.\nThis implies that the hacking phenomena reported in the main paper require models already capable of producing structurally valid output; below the capability threshold, RL produces no signal rather than degenerate signal.\n",
      "numLines": 19,
      "startLine": 840,
      "totalLines": 858
    }
  }
}
```

</details>

---

### Assistant

_source line 64_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive picture. Let me compile all the statistical tests with p-values reported in the paper.

From `paper/` directory (the primary submission):

1. **Fisher exact test: TS domination (matched cohort, ISR vs Random)** — p=0.004, OR=∞, BF10=77 (experiments.tex:104, 114; appendix.tex:774)

2. **Mann-Whitney U: ISR* (matched cohort)** — U=25, p=0.004, r=1.0 (experiments.tex:114; appendix.tex:775)


3. **Permutation test: genuine/non-hacking rate (matched cohort)** — Δ=-3.6pp, p=0.917 (n.s.), also reported as p=0.92 (experiments.tex:114; appendix.tex:777)
4. **Fisher exact test: non-hacking rate (5-seed, pooled)** — ISR 22.6% vs Random 7.7%, OR=3.48, p<10^{-8} (appendix.tex:105)
5. **Fisher exact test: non-hacking rate (3-seed, PG+F**

N corrected)** — ISR 6.06% vs Random 9.5%, OR=0.61, p=0.182 (n.s.) (appendix.tex:107, 269)
6. **Fisher exact test: TS gaming rate (5-seed)** — ISR 54.3% vs Random 29.5%, OR=2.84, p=4.82×10^{-12} (appendix.tex:110)
7. **Fisher exact test: TS gaming rate (3-seed sensitivity)** — ISR 70.6% vs Random 13.7%, OR=15.05, p=1.3×10^{-39} (appendix.tex:112)
8. **Fisher exact test: SFT vs Exec-only non-hacking rate** — SFT 92.3% vs Exec-only 7.5%, OR=147, p<0 (appendix.tex:114)

Now I'm looking at the Cochran-Mantel-Haenszel tests for TS and non-hacking behaviors, which show strong stratified associations. The seed-level permutation tests with smaller sample sizes don't reach significance, suggesting the effects might not hold at that granular level. I'm also checking correlations between ISR performance and NLI accuracy, which shows no meaningful relationship, and continuing through the Mann-Whitney comparisons.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "7301fc25-eb16-4558-b7e2-75e7ed6a993c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CoYXSiDsU6AreKoMNZFUgH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2072,
      "cache_read_input_tokens": 45389,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2072
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

_source line 65_

Let me check for the ProofFOL permutation test in the main paper/ files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "b33a807b-249b-4303-a697-9acb9e2d2924",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CoYXSiDsU6AreKoMNZFUgH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2072,
      "cache_read_input_tokens": 45389,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2072
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

_source line 66_

<details open><summary>🔧 Tool call — Grep · `toolu_019SNRwFada5BzpdPNhR1Dvq`</summary>

```json
{
  "pattern": "ProofFOL|prooffol|genuine.*permutation|permutation.*genuine|p.*0\\.10",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "output_mode": "content",
  "-n": true,
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "17bfd61c-06cb-4710-b0ec-5a0415711da4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CoYXSiDsU6AreKoMNZFUgH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2072,
      "cache_read_input_tokens": 45389,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2072
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

_source line 67 · 2026-05-20T04:48:00.391Z_

<details><summary>↩ Tool result · `toolu_019SNRwFada5BzpdPNhR1Dvq`</summary>

```text
paper/experiments.tex:12:%% D146-ACTIVATE: uncomment the following ProofFOL dataset description
paper/experiments.tex:13:% For cross-dataset validation (\S\ref{sec:prooffol}), we additionally train on
paper/experiments.tex:14:% ProofFOL, a silver-standard FOL corpus constructed by translating
paper/experiments.tex:18:% ProofFOL's formulas are syntactically simpler than FOLIO's human-authored FOL
paper/experiments.tex:114:Fisher exact test on TS domination yields $\text{OR}{=}\infty$ ($p{=}0.004$, 95\% CI $[2.30, \infty]$, $\text{BF}_{10}{=}77$); Mann-Whitney $U$ on $\text{ISR}^*$: $U{=}25$, $p{=}0.004$, $r{=}1.0$; genuine rates do not differ significantly ($2.3\%$ vs.\ $5.9\%$, $p{=}0.92$, permutation test; Appendix~\ref{app:matched-stats}), with the point estimate consistently favoring Random (corrected 3-seed: ISR $6.1\%$ vs.\ Random $9.5\%$; matched: $2.3\%$ vs.\ $5.9\%$).
paper/main.bbl:91:\newblock \href {https://doi.org/10.1007/s11229-021-03141-4} {{Reward Tampering
paper/conclusion.tex:10:%% === ProofFOL cross-dataset skeleton (fill after D146) ===
paper/conclusion.tex:11:%% BRANCH A (collapse replicates on ProofFOL):
paper/conclusion.tex:12:%  Preliminary cross-dataset evidence supports this prediction: training on ProofFOL
paper/conclusion.tex:21:%% BRANCH B (collapse does NOT replicate on ProofFOL):
paper/conclusion.tex:22:%  However, ProofFOL training does not reproduce the same collapse pattern
paper/conclusion.tex:24:%  ProofFOL's silver-standard FOL---generated by GPT-4o from ProofWriter's
paper/limitations.tex:6:% Experiments use a single model family (Qwen3-4B/1.7B) and one RL algorithm (GRPO); while cross-dataset evidence from ProofFOL (\S\ref{sec:prooffol}) supports generality, hacking-mode prevalence may vary across benchmarks.
paper/abstract.tex:8:% Across six reward conditions, two dataset families (FOLIO and ProofFOL), two logic types, and two model scales, we identify three persistent hacking modes (conclusion embedding [CE] / tautological shortcut [TS], validated across ${\geq}3$ seeds; premise-subset gaming [PG], observed at lower prevalence) plus additional modes in isolated conditions, and show that ISR is reliable as a diagnostic but unreliable as an optimization target.
paper/introduction.tex:29:% on ProofFOL, a silver-standard FOL corpus derived from ProofWriter~\citep{proofwriter}
paper/introduction.tex:33:% ProofFOL's simpler syntax lowers the capability threshold, producing faster
paper/figures/gen_fig2.py:57:ax_top.axhspan(0, 0.10, color="#FDEDEC", alpha=0.5, zorder=0)
paper/figures/fig2_data.json:1:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "1c48ff1f-3c74-45bb-9273-92ebd5f42328",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "paper/experiments.tex:12:%% D146-ACTIVATE: uncomment the following ProofFOL dataset description\npaper/experiments.tex:13:% For cross-dataset validation (\\S\\ref{sec:prooffol}), we additionally train on\npaper/experiments.tex:14:% ProofFOL, a silver-standard FOL corpus constructed by translating\npaper/experiments.tex:18:% ProofFOL's formulas are syntactically simpler than FOLIO's human-authored FOL\npaper/experiments.tex:114:Fisher exact test on TS domination yields $\\text{OR}{=}\\infty$ ($p{=}0.004$, 95\\% CI $[2.30, \\infty]$, $\\text{BF}_{10}{=}77$); Mann-Whitney $U$ on $\\text{ISR}^*$: $U{=}25$, $p{=}0.004$, $r{=}1.0$; genuine rates do not differ significantly ($2.3\\%$ vs.\\ $5.9\\%$, $p{=}0.92$, permutation test; Appendix~\\ref{app:matched-stats}), with the point estimate consistently favoring Random (corrected 3-seed: ISR $6.1\\%$ vs.\\ Random $9.5\\%$; matched: $2.3\\%$ vs.\\ $5.9\\%$).\npaper/main.bbl:91:\\newblock \\href {https://doi.org/10.1007/s11229-021-03141-4} {{Reward Tampering\npaper/conclusion.tex:10:%% === ProofFOL cross-dataset skeleton (fill after D146) ===\npaper/conclusion.tex:11:%% BRANCH A (collapse replicates on ProofFOL):\npaper/conclusion.tex:12:%  Preliminary cross-dataset evidence supports this prediction: training on ProofFOL\npaper/conclusion.tex:21:%% BRANCH B (collapse does NOT replicate on ProofFOL):\npaper/conclusion.tex:22:%  However, ProofFOL training does not reproduce the same collapse pattern\npaper/conclusion.tex:24:%  ProofFOL's silver-standard FOL---generated by GPT-4o from ProofWriter's\npaper/limitations.tex:6:% Experiments use a single model family (Qwen3-4B/1.7B) and one RL algorithm (GRPO); while cross-dataset evidence from ProofFOL (\\S\\ref{sec:prooffol}) supports generality, hacking-mode prevalence may vary across benchmarks.\npaper/abstract.tex:8:% Across six reward conditions, two dataset families (FOLIO and ProofFOL), two logic types, and two model scales, we identify three persistent hacking modes (conclusion embedding [CE] / tautological shortcut [TS], validated across ${\\geq}3$ seeds; premise-subset gaming [PG], observed at lower prevalence) plus additional modes in isolated conditions, and show that ISR is reliable as a diagnostic but unreliable as an optimization target.\npaper/introduction.tex:29:% on ProofFOL, a silver-standard FOL corpus derived from ProofWriter~\\citep{proofwriter}\npaper/introduction.tex:33:% ProofFOL's simpler syntax lowers the capability threshold, producing faster\npaper/figures/gen_fig2.py:57:ax_top.axhspan(0, 0.10, color=\"#FDEDEC\", alpha=0.5, zorder=0)\npaper/figures/fig2_data.json:1:[Omitted long matching line]",
    "numLines": 18
  }
}
```

</details>

---

### Tool call

_source line 68_

<details open><summary>🔧 Tool call — Grep · `toolu_01Benmt9ouCVtDL8sxuExSYi`</summary>

```json
{
  "pattern": "OR.*5\\.5|5\\.5.*CI|100.step.*OR|OR.*147|p.*0\\.001",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "output_mode": "content",
  "-n": true,
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "fb9cdd62-65fc-4485-9abb-621ce4c48eef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CoYXSiDsU6AreKoMNZFUgH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2072,
      "cache_read_input_tokens": 45389,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2072
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

_source line 69 · 2026-05-20T04:48:02.188Z_

<details><summary>↩ Tool result · `toolu_01Benmt9ouCVtDL8sxuExSYi`</summary>

```text
paper/experiments.tex:51:TS is entirely absent; CE occurs at $7.7\%$ ($\text{OR}{=}147$ vs.\ exec-only, $p{<}0.001$). %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3
paper/experiments.tex:52:The near-absence of hacking under identical data exposure is consistent with hacking being associated with RL optimization rather than data exposure; a 100-step checkpoint ($\text{PR}{=}32\%$, hacking${\geq}31\%$) partially controls for the PR-level confound (Appendix~\ref{app:100step}).
paper/main.bbl:378:\newblock \href {https://arxiv.org/abs/2502.14768} {{Logic-RL: Unleashing LLM
paper/appendix.tex:115:SFT vs.\ Exec-only & 92.3\% {\scriptsize[79.7,97.3]} & 7.5\% & 147 & ${<}0.001$ \\
paper/appendix.tex:707:The 100-step hacking rate (31.2\%) is already substantially above SFT (7.7\%), supporting the claim that hacking is associated with RL optimization rather than prove-rate level alone.
paper/appendix.tex:733:\caption{Per-seed results for the matched replication cohort (seeds 47--51, $\beta{=}0.1$, 500 steps). PR = prove rate, ISR$^*$ = proved-only ISR, TS/CE/N-H = percentage among proved samples. Wilson 95\% CIs for N-H: ISR s47 $[1.1, 8.7]$, s48 $[0, 5.5]$, s49 $[0.2, 6.3]$, s50 $[2.8, 12.7]$, s51 $[0.2, 5.6]$; Random s47 $[3.1, 13.9]$, s48 $[1.7, 10.5]$, s49 $[0, 43.4]$, s50 $[1.2, 14.8]$, s51 $[7.5, 24.3]$.}
paper/main.aux:2090:[Omitted long matching line]
paper/main.aux:2091:\newlabel{tab:matched-perseed}{{13}{23}{Per-seed results for the matched replication cohort (seeds 47--51, $\beta {=}0.1$, 500 steps). PR = prove rate, ISR$^*$ = proved-only ISR, TS/CE/N-H = percentage among proved samples. Wilson 95\% CIs for N-H: ISR s47 $[1.1, 8.7]$, s48 $[0, 5.5]$, s49 $[0.2, 6.3]$, s50 $[2.8, 12.7]$, s51 $[0.2, 5.6]$; Random s47 $[3.1, 13.9]$, s48 $[1.7, 10.5]$, s49 $[0, 43.4]$, s50 $[1.2, 14.8]$, s51 $[7.5, 24.3]$}{table.caption.79}{}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "6bb44144-2098-46c3-9470-2a1ecb8e692f",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "paper/experiments.tex:51:TS is entirely absent; CE occurs at $7.7\\%$ ($\\text{OR}{=}147$ vs.\\ exec-only, $p{<}0.001$). %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3\npaper/experiments.tex:52:The near-absence of hacking under identical data exposure is consistent with hacking being associated with RL optimization rather than data exposure; a 100-step checkpoint ($\\text{PR}{=}32\\%$, hacking${\\geq}31\\%$) partially controls for the PR-level confound (Appendix~\\ref{app:100step}).\npaper/main.bbl:378:\\newblock \\href {https://arxiv.org/abs/2502.14768} {{Logic-RL: Unleashing LLM\npaper/appendix.tex:115:SFT vs.\\ Exec-only & 92.3\\% {\\scriptsize[79.7,97.3]} & 7.5\\% & 147 & ${<}0.001$ \\\\\npaper/appendix.tex:707:The 100-step hacking rate (31.2\\%) is already substantially above SFT (7.7\\%), supporting the claim that hacking is associated with RL optimization rather than prove-rate level alone.\npaper/appendix.tex:733:\\caption{Per-seed results for the matched replication cohort (seeds 47--51, $\\beta{=}0.1$, 500 steps). PR = prove rate, ISR$^*$ = proved-only ISR, TS/CE/N-H = percentage among proved samples. Wilson 95\\% CIs for N-H: ISR s47 $[1.1, 8.7]$, s48 $[0, 5.5]$, s49 $[0.2, 6.3]$, s50 $[2.8, 12.7]$, s51 $[0.2, 5.6]$; Random s47 $[3.1, 13.9]$, s48 $[1.7, 10.5]$, s49 $[0, 43.4]$, s50 $[1.2, 14.8]$, s51 $[7.5, 24.3]$.}\npaper/main.aux:2090:[Omitted long matching line]\npaper/main.aux:2091:\\newlabel{tab:matched-perseed}{{13}{23}{Per-seed results for the matched replication cohort (seeds 47--51, $\\beta {=}0.1$, 500 steps). PR = prove rate, ISR$^*$ = proved-only ISR, TS/CE/N-H = percentage among proved samples. Wilson 95\\% CIs for N-H: ISR s47 $[1.1, 8.7]$, s48 $[0, 5.5]$, s49 $[0.2, 6.3]$, s50 $[2.8, 12.7]$, s51 $[0.2, 5.6]$; Random s47 $[3.1, 13.9]$, s48 $[1.7, 10.5]$, s49 $[0, 43.4]$, s50 $[1.2, 14.8]$, s51 $[7.5, 24.3]$}{table.caption.79}{}}",
    "numLines": 8
  }
}
```

</details>

---

### Assistant

_source line 70_

<details><summary>Logged reasoning block</summary>

```text
I also need to check if the ProofFOL permutation test (p=0.10) is in the paper/ directory. Let me search more specifically.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "9ce0fd90-b373-4b92-862d-37f269a896dc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016rcSv5HFaVUafwpFJXEoUz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3071,
      "cache_read_input_tokens": 47461,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3071
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

_source line 71_

Let me check for the ProofFOL permutation test in paper/appendix.tex.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "8d193504-b45a-4f15-b57a-b88590aedeed",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016rcSv5HFaVUafwpFJXEoUz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3071,
      "cache_read_input_tokens": 47461,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3071
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

_source line 72_

<details open><summary>🔧 Tool call — Grep · `toolu_018Vaxvh3qJQU6ZCYgH8oKeK`</summary>

```json
{
  "pattern": "p.*=.*0\\.10|0\\.10.*permutation|genuine.*rate.*per",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
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
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "93a75f3b-5d19-4317-abf2-ccfcc5bb5ffe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016rcSv5HFaVUafwpFJXEoUz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3071,
      "cache_read_input_tokens": 47461,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3071
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

_source line 73 · 2026-05-20T04:48:07.231Z_

<details><summary>↩ Tool result · `toolu_018Vaxvh3qJQU6ZCYgH8oKeK`</summary>

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
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "0a45c38f-538c-4ee0-8e53-51f568a7f960",
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

_source line 74_

<details open><summary>🔧 Tool call — Grep · `toolu_01Ng2AR16UayevBQ91o3XzoT`</summary>

```json
{
  "pattern": "Aggregate.*genuine|genuine.*Aggregate|76\\.8",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
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
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "bb2c45fa-8b3f-4d59-9911-64bf504f55fd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016rcSv5HFaVUafwpFJXEoUz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3071,
      "cache_read_input_tokens": 47461,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3071
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

_source line 75 · 2026-05-20T04:48:08.133Z_

<details><summary>↩ Tool result · `toolu_01Ng2AR16UayevBQ91o3XzoT`</summary>

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
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "000f2749-597f-4c20-ae27-a90f3335305d",
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

_source line 76_

<details><summary>Logged reasoning block</summary>

```text
The ProofFOL permutation test (p=0.10) appears only in the `docs/paper/` versions, not in the main `paper/` directory. This suggests it may have been removed from the current version of the paper. Let me focus only on the tests in the main `paper/` directory.

Let me also check for any other tests I might have missed - specifically the OR=5.5 for the 100-step analysis.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "524e9ba0-1265-4600-a666-b87886d0ec81",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PBmoLWJiPps4VCNHWoDw4D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 531,
      "cache_read_input_tokens": 50532,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 531
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

<details open><summary>🔧 Tool call — Grep · `toolu_016q17PpCvbjyFraKzgnhzeT`</summary>

```json
{
  "pattern": "OR.*5\\.5|5\\.5.*OR",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper",
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
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "7b406e37-cb31-405a-8ba6-18a89bd79a93",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PBmoLWJiPps4VCNHWoDw4D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 531,
      "cache_read_input_tokens": 50532,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 531
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

_source line 78 · 2026-05-20T04:48:12.794Z_

<details><summary>↩ Tool result · `toolu_016q17PpCvbjyFraKzgnhzeT`</summary>

```text
docs/paper/experiments.tex:38:A 100-step RL checkpoint (Appendix~\ref{app:100step}) at $\text{PR}{=}32\%$ already shows 31.2\% hacking (vs.\ SFT's 7.7\%; $\text{OR}{=}5.5$, 95\% CI $[1.4, 22.0]$), indicating reward hacking emerges early in RL training, not merely at high PR.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "c5562764-b942-43e2-be61-51b2365a7737",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/experiments.tex:38:A 100-step RL checkpoint (Appendix~\\ref{app:100step}) at $\\text{PR}{=}32\\%$ already shows 31.2\\% hacking (vs.\\ SFT's 7.7\\%; $\\text{OR}{=}5.5$, 95\\% CI $[1.4, 22.0]$), indicating reward hacking emerges early in RL training, not merely at high PR.",
    "numLines": 1
  }
}
```

</details>

---

### Assistant

_source line 79_

<details><summary>Logged reasoning block</summary>

```text
That OR=5.5 is only in docs/paper/, not in the current paper/. So it's been removed.

Now let me also check for the Fisher test in the TS comparison in docs/paper for TS domination rate (p=1.3×10^{-39}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "12f3ed7e-1bee-49c6-bf12-473205001ca3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VPqQW4WeoHN7EEvQzvyNge",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 389,
      "cache_read_input_tokens": 51063,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 389
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

_source line 80_

Now I have all the p-values. Let me compile and run the Bonferroni correction.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "2cc1b2cc-4036-4635-8305-4677bc5ddfe5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VPqQW4WeoHN7EEvQzvyNge",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 389,
      "cache_read_input_tokens": 51063,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 389
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

_source line 81_

<details open><summary>🔧 Tool call — Bash · `toolu_018PL47yeziPSBXVeUETmAdv`</summary>

```json
{
  "command": "cat << 'PYEOF' | python3\nimport json\n\n# All statistical tests with reported p-values from paper/ directory\ntests = [\n    {\n        \"name\": \"Fisher exact: TS domination (matched 5+5)\",\n        \"original_p\": 0.004,\n        \"context\": \"ISR 5/5 TS-dominated vs Random 0/5; OR=inf, BF10=77\",\n        \"test_type\": \"Fisher exact\",\n        \"location\": \"experiments.tex:104,114; appendix.tex:774\"\n    },\n    {\n        \"name\": \"Mann-Whitney U: ISR* (matched 5+5)\",\n        \"original_p\": 0.004,\n        \"context\": \"U=25, r=1.0; ISR* comparison between matched ISR and Random cohorts\",\n        \"test_type\": \"Mann-Whitney U\",\n        \"location\": \"experiments.tex:114; appendix.tex:775\"\n    },\n    {\n        \"name\": \"Mann-Whitney U: TS rate (matched 5+5)\",\n        \"original_p\": 0.004,\n        \"context\": \"U=25; TS rate comparison between matched ISR and Random cohorts\",\n        \"test_type\": \"Mann-Whitney U\",\n        \"location\": \"appendix.tex:776\"\n    },\n    {\n        \"name\": \"Permutation: N-H rate (matched 5+5)\",\n        \"original_p\": 0.917,\n        \"context\": \"Δ=-3.6pp; genuine/non-hacking rate ISR 2.3% vs Random 5.9%\",\n        \"test_type\": \"Permutation\",\n        \"location\": \"experiments.tex:114; appendix.tex:777\"\n    },\n    {\n        \"name\": \"Fisher exact: N-H rate (5-seed pooled)\",\n        \"original_p\": 1e-8,\n        \"context\": \"ISR 22.6% vs Random 7.7%, OR=3.48 (uncorrected for PG/FN)\",\n        \"test_type\": \"Fisher exact\",\n        \"location\": \"appendix.tex:105\"\n    },\n    {\n        \"name\": \"Fisher exact: N-H rate (3-seed, PG+FN corrected)\",\n        \"original_p\": 0.182,\n        \"context\": \"ISR 6.06% vs Random 9.5%, OR=0.61 (n.s.)\",\n        \"test_type\": \"Fisher exact\",\n        \"location\": \"appendix.tex:107,269\"\n    },\n    {\n        \"name\": \"Fisher exact: TS rate (5-seed pooled)\",\n        \"original_p\": 4.82e-12,\n        \"context\": \"ISR 54.3% vs Random 29.5%, OR=2.84\",\n        \"test_type\": \"Fisher exact\",\n        \"location\": \"appendix.tex:110\"\n    },\n    {\n        \"name\": \"Fisher exact: TS rate (3-seed sensitivity)\",\n        \"original_p\": 1.3e-39,\n        \"context\": \"ISR 70.6% vs Random 13.7%, OR=15.05\",\n        \"test_type\": \"Fisher exact\",\n        \"location\": \"appendix.tex:112\"\n    },\n    {\n        \"name\": \"Fisher exact: SFT vs Exec-only N-H rate\",\n        \"original_p\": 0.001,\n        \"context\": \"SFT 92.3% vs Exec-only 7.5%, OR=147 (p<0.001, using 0.001 as upper bound)\",\n        \"test_type\": \"Fisher exact\",\n        \"location\": \"experiments.tex:51; appendix.tex:115\"\n    },\n    {\n        \"name\": \"CMH: TS (seed-stratified)\",\n        \"original_p\": 5.6e-16,\n        \"context\": \"OR_CMH=2.46, 95% CI [1.85,3.27]; authors note CMH p-values are inflated due to within-seed dependence\",\n        \"test_type\": \"Cochran-Mantel-Haenszel\",\n        \"location\": \"appendix.tex:125\"\n    },\n    {\n        \"name\": \"CMH: non-hacking (seed-stratified)\",\n        \"original_p\": 4.5e-10,\n        \"context\": \"OR_CMH=3.37, 95% CI [2.21,5.13]; authors note CMH p-values are inflated\",\n        \"test_type\": \"Cochran-Mantel-Haenszel\",\n        \"location\": \"appendix.tex:125\"\n    },\n    {\n        \"name\": \"Seed-level permutation: TS (n=5 per group)\",\n        \"original_p\": 0.28,\n        \"context\": \"Seed as unit of observation; limited power (min achievable p=0.008)\",\n        \"test_type\": \"Permutation\",\n        \"location\": \"appendix.tex:127\"\n    },\n    {\n        \"name\": \"Seed-level permutation: N-H (n=5 per group)\",\n        \"original_p\": 0.26,\n        \"context\": \"Seed as unit of observation; limited power (min achievable p=0.008)\",\n        \"test_type\": \"Permutation\",\n        \"location\": \"appendix.tex:127\"\n    },\n    {\n        \"name\": \"Spearman: ISR vs NLI accuracy\",\n        \"original_p\": 0.187,\n        \"context\": \"ρ=-0.049, n.s.; confirms ISR uncorrelated with downstream task performance\",\n        \"test_type\": \"Spearman correlation\",\n        \"location\": \"appendix.tex:77\"\n    }\n]\n\nN = len(tests)\n\nfor t in tests:\n    t[\"bonferroni_p\"] = min(t[\"original_p\"] * N, 1.0)\n    t[\"still_significant_005\"] = t[\"bonferroni_p\"] < 0.05\n    t[\"still_significant_010\"] = t[\"bonferroni_p\"] < 0.10\n\nresult = {\n    \"n_tests\": N,\n    \"method\": \"Bonferroni\",\n    \"alpha_levels\": [0.05, 0.10],\n    \"tests\": tests\n}\n\nwith open(\"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/bonferroni_correction.json\", \"w\") as f:\n    json.dump(result, f, indent=2, ensure_ascii=False)\n\n# Summary\nn_orig_005 = sum(1 for t in tests if t[\"original_p\"] < 0.05)\nn_orig_010 = sum(1 for t in tests if t[\"original_p\"] < 0.10)\nn_corr_005 = sum(1 for t in tests if t[\"still_significant_005\"])\nn_corr_010 = sum(1 for t in tests if t[\"still_significant_010\"])\n\nprint(f\"Total tests (N): {N}\")\nprint(f\"\\nPre-correction significant at α=0.05: {n_orig_005}/{N}\")\nprint(f\"Pre-correction significant at α=0.10: {n_orig_010}/{N}\")\nprint(f\"\\nPost-Bonferroni significant at α=0.05: {n_corr_005}/{N}\")\nprint(f\"Post-Bonferroni significant at α=0.10: {n_corr_010}/{N}\")\n\nprint(\"\\n--- All tests ---\")\nfor t in tests:\n    flag = \"✓\" if t[\"still_significant_005\"] else (\"~\" if t[\"still_significant_010\"] else \"✗\")\n    print(f\"  [{flag}] {t['name']}: p_orig={t['original_p']:.4g} → p_bonf={t['bonferroni_p']:.4g}\")\n\n# Tests that lose significance\nprint(\"\\n--- Tests that LOSE significance after Bonferroni ---\")\nlost = [t for t in tests if t[\"original_p\"] < 0.05 and not t[\"still_significant_005\"]]\nif lost:\n    for t in lost:\n        print(f\"  {t['name']}: p_orig={t['original_p']:.4g} → p_bonf={t['bonferroni_p']:.4g}\")\nelse:\n    print(\"  None — all originally significant tests remain significant at α=0.05\")\n\nlost_010 = [t for t in tests if t[\"original_p\"] < 0.10 and not t[\"still_significant_010\"]]\nif lost_010:\n    print(f\"\\n--- Lost at α=0.10 ---\")\n    for t in lost_010:\n        print(f\"  {t['name']}: p_orig={t['original_p']:.4g} → p_bonf={t['bonferroni_p']:.4g}\")\nPYEOF\n",
  "description": "Compute Bonferroni correction on all paper p-values"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "73249f46-c221-4f68-bafb-89a4a2448096",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VPqQW4WeoHN7EEvQzvyNge",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 389,
      "cache_read_input_tokens": 51063,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 389
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

_source line 82 · 2026-05-20T04:48:45.184Z_

<details><summary>↩ Tool result · `toolu_018PL47yeziPSBXVeUETmAdv`</summary>

```text
Total tests (N): 14

Pre-correction significant at α=0.05: 9/14
Pre-correction significant at α=0.10: 9/14

Post-Bonferroni significant at α=0.05: 6/14
Post-Bonferroni significant at α=0.10: 9/14

--- All tests ---
  [~] Fisher exact: TS domination (matched 5+5): p_orig=0.004 → p_bonf=0.056
  [~] Mann-Whitney U: ISR* (matched 5+5): p_orig=0.004 → p_bonf=0.056
  [~] Mann-Whitney U: TS rate (matched 5+5): p_orig=0.004 → p_bonf=0.056
  [✗] Permutation: N-H rate (matched 5+5): p_orig=0.917 → p_bonf=1
  [✓] Fisher exact: N-H rate (5-seed pooled): p_orig=1e-08 → p_bonf=1.4e-07
  [✗] Fisher exact: N-H rate (3-seed, PG+FN corrected): p_orig=0.182 → p_bonf=1
  [✓] Fisher exact: TS rate (5-seed pooled): p_orig=4.82e-12 → p_bonf=6.748e-11
  [✓] Fisher exact: TS rate (3-seed sensitivity): p_orig=1.3e-39 → p_bonf=1.82e-38
  [✓] Fisher exact: SFT vs Exec-only N-H rate: p_orig=0.001 → p_bonf=0.014
  [✓] CMH: TS (seed-stratified): p_orig=5.6e-16 → p_bonf=7.84e-15
  [✓] CMH: non-hacking (seed-stratified): p_orig=4.5e-10 → p_bonf=6.3e-09
  [✗] Seed-level permutation: TS (n=5 per group): p_orig=0.28 → p_bonf=1
  [✗] Seed-level permutation: N-H (n=5 per group): p_orig=0.26 → p_bonf=1
  [✗] Spearman: ISR vs NLI accuracy: p_orig=0.187 → p_bonf=1

--- Tests that LOSE significance after Bonferroni ---
  Fisher exact: TS domination (matched 5+5): p_orig=0.004 → p_bonf=0.056
  Mann-Whitney U: ISR* (matched 5+5): p_orig=0.004 → p_bonf=0.056
  Mann-Whitney U: TS rate (matched 5+5): p_orig=0.004 → p_bonf=0.056
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "6dfa5688-b5e2-4baf-8b0b-902c1cd5eb67",
  "tool_use_result": {
    "stdout": "Total tests (N): 14\n\nPre-correction significant at α=0.05: 9/14\nPre-correction significant at α=0.10: 9/14\n\nPost-Bonferroni significant at α=0.05: 6/14\nPost-Bonferroni significant at α=0.10: 9/14\n\n--- All tests ---\n  [~] Fisher exact: TS domination (matched 5+5): p_orig=0.004 → p_bonf=0.056\n  [~] Mann-Whitney U: ISR* (matched 5+5): p_orig=0.004 → p_bonf=0.056\n  [~] Mann-Whitney U: TS rate (matched 5+5): p_orig=0.004 → p_bonf=0.056\n  [✗] Permutation: N-H rate (matched 5+5): p_orig=0.917 → p_bonf=1\n  [✓] Fisher exact: N-H rate (5-seed pooled): p_orig=1e-08 → p_bonf=1.4e-07\n  [✗] Fisher exact: N-H rate (3-seed, PG+FN corrected): p_orig=0.182 → p_bonf=1\n  [✓] Fisher exact: TS rate (5-seed pooled): p_orig=4.82e-12 → p_bonf=6.748e-11\n  [✓] Fisher exact: TS rate (3-seed sensitivity): p_orig=1.3e-39 → p_bonf=1.82e-38\n  [✓] Fisher exact: SFT vs Exec-only N-H rate: p_orig=0.001 → p_bonf=0.014\n  [✓] CMH: TS (seed-stratified): p_orig=5.6e-16 → p_bonf=7.84e-15\n  [✓] CMH: non-hacking (seed-stratified): p_orig=4.5e-10 → p_bonf=6.3e-09\n  [✗] Seed-level permutation: TS (n=5 per group): p_orig=0.28 → p_bonf=1\n  [✗] Seed-level permutation: N-H (n=5 per group): p_orig=0.26 → p_bonf=1\n  [✗] Spearman: ISR vs NLI accuracy: p_orig=0.187 → p_bonf=1\n\n--- Tests that LOSE significance after Bonferroni ---\n  Fisher exact: TS domination (matched 5+5): p_orig=0.004 → p_bonf=0.056\n  Mann-Whitney U: ISR* (matched 5+5): p_orig=0.004 → p_bonf=0.056\n  Mann-Whitney U: TS rate (matched 5+5): p_orig=0.004 → p_bonf=0.056",
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

_source line 83_

JSON 已保存。汇总：

## Bonferroni 校正结果

**N = 14 个统计检验**

| | α=0.05 | α=0.10 |
|---|---|---|
| 校正前显著 | 9/14 | 9/14 |
| 校正后显著 | 6/14 | 9/14 |

### 校正后不再显著的检验（α=0.05）

3 个 matched-cohort (n=5 per group) 检验从 p=0.004 升至 p_bonf=0.056，刚好超过 0.05 阈值，但仍在 α=0.10 下显著：

| 检验 | p_orig | p_bonf |
|---|---|---|
| Fisher exact: TS domination (matched 5+5) | 0.004 | 0.056 |
| Mann-Whitney U: ISR* (matched 5+5) | 0.004 | 0.056 |
| Mann-Whitney U: TS rate (matched 5+5) | 0.004 | 0.056 |

这三个检验实质上是对同一 matched-cohort 数据的不同切面（TS domination / ISR* / TS rate），本身高度相关。论文核心结论（TS 为 ISR 特异性吸引子）同时有 pooled Fisher (p_bonf ≈ 10⁻¹¹) 和 3-seed sensitivity (p_bonf ≈ 10⁻³⁸) 支撑，这两个校正后仍然极度显著。

### 影响评估

- 论文主要统计结论（TS rate 差异、SFT vs RL 差异）校正后仍然稳健
- matched-cohort 的 p=0.004 系列检验边际化，但考虑到 N=5 的 discrete permutation 限制（最小可达 p=0.008），BF₁₀=77 的贝叶斯证据仍然很强
- 5 个原本不显著的检验（permutation N-H、3-seed Fisher N-H、seed-level permutations、Spearman）校正后当然仍不显著

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "uuid": "b31edfc5-cfd5-4c66-ba3c-e3b0b3b760eb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q3C7BWVSvZbKM6c9j4k1fp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3180,
      "cache_read_input_tokens": 51452,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3180
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

_source line 84_

JSON 已保存。汇总：

## Bonferroni 校正结果

**N = 14 个统计检验**

| | α=0.05 | α=0.10 |
|---|---|---|
| 校正前显著 | 9/14 | 9/14 |
| 校正后显著 | 6/14 | 9/14 |

### 校正后不再显著的检验（α=0.05）

3 个 matched-cohort (n=5 per group) 检验从 p=0.004 升至 p_bonf=0.056，刚好超过 0.05 阈值，但仍在 α=0.10 下显著：

| 检验 | p_orig | p_bonf |
|---|---|---|
| Fisher exact: TS domination (matched 5+5) | 0.004 | 0.056 |
| Mann-Whitney U: ISR* (matched 5+5) | 0.004 | 0.056 |
| Mann-Whitney U: TS rate (matched 5+5) | 0.004 | 0.056 |

这三个检验实质上是对同一 matched-cohort 数据的不同切面（TS domination / ISR* / TS rate），本身高度相关。论文核心结论（TS 为 ISR 特异性吸引子）同时有 pooled Fisher (p_bonf ≈ 10⁻¹¹) 和 3-seed sensitivity (p_bonf ≈ 10⁻³⁸) 支撑，这两个校正后仍然极度显著。

### 影响评估

- 论文主要统计结论（TS rate 差异、SFT vs RL 差异）校正后仍然稳健
- matched-cohort 的 p=0.004 系列检验边际化，但考虑到 N=5 的 discrete permutation 限制（最小可达 p=0.008），BF₁₀=77 的贝叶斯证据仍然很强
- 5 个原本不显著的检验（permutation N-H、3-seed Fisher N-H、seed-level permutations、Spearman）校正后当然仍不显著

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 135731,
  "duration_api_ms": 136261,
  "num_turns": 32,
  "stop_reason": "end_turn",
  "session_id": "81e7ac3e-5c7f-46d0-b658-c2c27178dbf9",
  "total_cost_usd": 0.70495075,
  "usage": {
    "input_tokens": 13,
    "cache_creation_input_tokens": 42791,
    "cache_read_input_tokens": 420892,
    "output_tokens": 8942,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 42791,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 616,
        "cache_read_input_tokens": 51452,
        "cache_creation_input_tokens": 3180,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 3180
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 3346,
      "outputTokens": 20,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.003446,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 13,
      "outputTokens": 8942,
      "cacheReadInputTokens": 420892,
      "cacheCreationInputTokens": 42791,
      "webSearchRequests": 0,
      "costUSD": 0.7015047499999999,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "a9d536a8-6e35-4634-9013-1cfcb760cc27"
}
```

</details>

---
