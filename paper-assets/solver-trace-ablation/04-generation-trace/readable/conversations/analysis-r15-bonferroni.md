# analysis r15 bonferroni

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 63
- **Recorded user turns:** 0
- **Tool calls:** 31
- **Original source:** `logs/chats/worker_analysis_r15-bonferroni_20260520T044634.jsonl`
- **Structured JSON:** [`81ac9e3c30191570e987.json`](../../sessions/81/81ac9e3c30191570e987.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

63 recorded events

### Tool call

_source line 1 · 2026-05-20T04:48:59.331610+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "p[\\s=<>]|Fisher|permutation|significant|p-value|\\\\text.?test|McNemar|Wilcoxon|chi.?sq|bootstrap",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "output_mode": "content",
  "-n": "True",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Grep",
  "tool_args": {
    "pattern": "p[\\s=<>]|Fisher|permutation|significant|p-value|\\\\text.?test|McNemar|Wilcoxon|chi.?sq|bootstrap",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
    "output_mode": "content",
    "-n": "True",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-20T04:48:59.332063+00:00_

32:\caption{ISR collapse under exec-only GRPO (seed~42). (a) Both metrics on the same $[0,1]$ scale: PR rises 32\%$\to$93\%$\to$96\% while ISR$^*$ falls $0.642{\to}0.132{\to}0.003$ over 100$\to$500$\to$1000 steps; the shaded region shows the growing divergence. (b) Hacking modes progressively replace non-hacking output: by step 1000, CE dominates 100\% of proved samples.}
52:The near-absence of hacking under identical data exposure is consistent with hacking being associated with RL optimization rather than data exposure; a 100-step checkpoint ($\text{PR}{=}32\%$, hacking${\geq}31\%$) partially controls for the PR-level confound (Appendix~\ref{app:100step}).
104:The matched cohort resolves this ambiguity: ISR yields 5/5 TS-dominated seeds versus 0/5 under random control (Fisher $p{=}0.004$), confirming TS as ISR-specific rather than a generic GRPO artifact.
107:The reward gap explains this: TS tautologies receive expected reward ${\geq}1{+}0.5\beta$ (mean empirical $\text{ISR}{=}0.535$) versus ${\sim}1{+}0.26\beta$ for non-hacking proofs (premise-count-matched), creating a persistent gradient toward tautological constructions regardless of dose.
114:Fisher exact test on TS domination yields $\text{OR}{=}\infty$ ($p{=}0.004$, 95\% CI $[2.30, \infty]$, $\text{BF}_{10}{=}77$); Mann-Whitney $U$ on $\text{ISR}^*$: $U{=}25$, $p{=}0.004$, $r{=}1.0$; genuine rates do not differ significantly ($2.3\%$ vs.\ $5.9\%$, $p{=}0.92$, permutation test; Appendix~\ref{app:matched-stats}), with the point estimate consistently favoring Random (corrected 3-seed: ISR $6.1\%$ vs.\ Random $9.5\%$; matched: $2.3\%$ vs.\ $5.9\%$).
166:CE, TS, and PG account for ${>}90\%$ of hacking across ${\geq}3$ seeds each; ISR modestly increases TS probability ($\text{OR}{=}2.84$; Appendix Table~\ref{tab:bootstrap-ci}), but per-seed variance dominates.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T04:48:59.332264+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "p[\\s=<>]|Fisher|permutation|significant|p-value|\\\\text.?test|McNemar|Wilcoxon|chi.?sq|bootstrap",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
  "output_mode": "content",
  "-n": "True",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Grep",
  "tool_args": {
    "pattern": "p[\\s=<>]|Fisher|permutation|significant|p-value|\\\\text.?test|McNemar|Wilcoxon|chi.?sq|bootstrap",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
    "output_mode": "content",
    "-n": "True",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T04:48:59.332432+00:00_

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
350:Two-component formalizations where the premise and conclusion are identical atomic or simple formulas, yielding a $P \
…[truncated 2233 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T04:48:59.332600+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "p[\\s=<>]|Fisher|permutation|significant|p-value|\\\\text.?test|McNemar|Wilcoxon|chi.?sq|bootstrap",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex",
  "output_mode": "content",
  "-n": "True",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Grep",
  "tool_args": {
    "pattern": "p[\\s=<>]|Fisher|permutation|significant|p-value|\\\\text.?test|McNemar|Wilcoxon|chi.?sq|bootstrap",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex",
    "output_mode": "content",
    "-n": "True",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T04:48:59.332760+00:00_

5:This gap is especially consequential under RL, where the optimizer exploits any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}.
10:We address this gap with \emph{Solver Trace Ablation} (STA), which applies leave-one-out ablation on solver inputs to test whether each component of a proved formalization is individually necessary.
14:An SFT baseline on identical data largely avoids hacking, consistent with hacking being associated with RL optimization rather than data exposure, though the large prove-rate gap prevents definitive causal attribution (\S\ref{sec:diagnostic}).
21:We present an empirical case study of Goodhart collapse in solver-backed RL, using FOLIO with Qwen3 (4B/1.7B) across six reward conditions, ten seeds (5+5 matched design), two logic types, and up to 1000 training steps. Our contributions:
22:\begin{enumerate}[leftmargin=*,itemsep=2pt]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T04:48:59.332898+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "p[\\s=<>]|Fisher|permutation|significant|p-value|\\\\text.?test|McNemar|Wilcoxon|chi.?sq|bootstrap",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex",
  "output_mode": "content",
  "-n": "True",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Grep",
  "tool_args": {
    "pattern": "p[\\s=<>]|Fisher|permutation|significant|p-value|\\\\text.?test|McNemar|Wilcoxon|chi.?sq|bootstrap",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex",
    "output_mode": "content",
    "-n": "True",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T04:48:59.333030+00:00_

6:An SFT baseline largely avoids hacking under identical data, consistent with hacking being associated with RL optimization, though the prove-rate gap (13\% vs.\ 97\%) prevents definitive causal attribution.
7:Any transient non-hacking window ($p{=}0.92$, permutation test; matched 5+5 design) disappears under extended training; snapshot evaluation overestimates ISR's benefit.
17:%  The structural bias toward single-premise tautologies ($P \to P$ yielding
36:Reward ensembling~\citep{coste2024reward} targets learned rewards, not deterministic solver signals; constrained optimization~\citep{moskovitz2024confronting} could cap ISR, but collapse at all $\beta$ suggests a narrow proxy-validity boundary.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T04:48:59.333154+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "p[\\s=<>]|Fisher|permutation|significant|p-value|\\\\text.?test|McNemar|Wilcoxon|chi.?sq|bootstrap",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/docs/paper/experiments.tex",
  "output_mode": "content",
  "-n": "True",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Grep",
  "tool_args": {
    "pattern": "p[\\s=<>]|Fisher|permutation|significant|p-value|\\\\text.?test|McNemar|Wilcoxon|chi.?sq|bootstrap",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/docs/paper/experiments.tex",
    "output_mode": "content",
    "-n": "True",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T04:48:59.333280+00:00_

&lt;tool_use_error>Path does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/docs/paper/experiments.tex. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T04:48:59.333401+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "p[\\s=<>]|Fisher|permutation|significant|p-value|\\\\text.?test|McNemar|Wilcoxon|chi.?sq|bootstrap",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/docs/paper/appendix.tex",
  "output_mode": "content",
  "-n": "True",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Grep",
  "tool_args": {
    "pattern": "p[\\s=<>]|Fisher|permutation|significant|p-value|\\\\text.?test|McNemar|Wilcoxon|chi.?sq|bootstrap",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/docs/paper/appendix.tex",
    "output_mode": "content",
    "-n": "True",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T04:48:59.333515+00:00_

&lt;tool_use_error>Path does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/docs/paper/appendix.tex. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T04:48:59.333651+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

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
  "recorded_role": "tool",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Glob",
  "tool_args": {
    "pattern": "docs/paper/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-20T04:48:59.333795+00:00_

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

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T04:48:59.333913+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "p[\\s=<>]|Fisher|permutation|significant|p-value|test",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex",
  "output_mode": "content",
  "-n": "True",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Grep",
  "tool_args": {
    "pattern": "p[\\s=<>]|Fisher|permutation|significant|p-value|test",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex",
    "output_mode": "content",
    "-n": "True",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T04:48:59.334033+00:00_

8:We train with Group Relative Policy Optimization (GRPO)~\citep{deepseekmath} ($K{=}4$), where each rollout receives binary execution reward $r_{\text{exec}}(x) = \mathbf{1}[S(x){=}\textit{proved}]$.
15:STA tests whether each component of a proved formalization is individually necessary for proof success .
20:LOO ablation itself is standard in mutation testing and sensitivity analysis~\citep{demillo1978, jia-harman-survey}; our contribution lies in applying it as a GRPO-hacking diagnostic and in the empirical phenomena it surfaces.
37:{\footnotesize For FOL, components include both premises and conclusion sub-expressions (quantifier, antecedent, consequent); each sub-expression is ablated by removing it from the solver input and testing whether the proof still succeeds.}
64:An SFT baseline trained with negative log-likelihood on gold formalizations tests whether structural degeneration arises from RL optimization or data exposure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T04:48:59.334153+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "p[\\s=<>]|Fisher|permutation|significant|p-value|test",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/limitations.tex",
  "output_mode": "content",
  "-n": "True",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Grep",
  "tool_args": {
    "pattern": "p[\\s=<>]|Fisher|permutation|significant|p-value|test",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/limitations.tex",
    "output_mode": "content",
    "-n": "True",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T04:48:59.334271+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T04:48:59.334383+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "p[\\s=<>]|Fisher|permutation|significant|p-value|test",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex",
  "output_mode": "content",
  "-n": "True",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Grep",
  "tool_args": {
    "pattern": "p[\\s=<>]|Fisher|permutation|significant|p-value|test",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex",
    "output_mode": "content",
    "-n": "True",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T04:48:59.334521+00:00_

20:\caption{ISR collapse under exec-only GRPO (seed~42). PR rises 32\%$\to$93\%$\to$96\% while proved-only ISR falls $0.642{\to}0.132{\to}0.003$ over 100$\to$500$\to$1000 steps. By step 1000, 94.8\% of proved samples have $\text{ISR}{=}0$ and mean component count inflates 6.58$\to$18.55 (contradiction explosion).}
38:A 100-step RL checkpoint (Appendix~\ref{app:100step}) at $\text{PR}{=}32\%$ already shows 31.2\% hacking (vs.\ SFT's 7.7\%; $\text{OR}{=}5.5$, 95\% CI $[1.4, 22.0]$), indicating reward hacking emerges early in RL training, not merely at high PR.
70:H7 tautological collapse occurs under both ISR and random conditions, but ISR amplifies it ${\sim}5\times$: $70.6\%$ ($163/231$) under ISR vs.\ $13.7\%$ ($36/262$) under random (Fisher $p{=}1.3{\times}10^{-39}$, $\text{OR}{=}15.05$, 95\% CI $[9.6, 23.6]$). %% registry: plan002 vs plan018 all seeds; D095 FINAL
81:[Omitted long matching line]
88:\caption{Training ISR trajectories across reward conditions. ISR $\beta{=}0.1$ seeds rise rapidly toward $\text{ISR}{\approx}1$ (meta-Goodhart gaming via H7 tautology); exec-only s44's plateau at ${\sim}0.5$ is an H7a artifact ($n{=}2$ gives $\text{ISR}{\geq}0.5$ by construction), not genuine structural quality; random $\beta{=}0.1$ remains low. The s42 1k-step trace shows ISR eventually saturates at $0.88$ through the same H7 mechanism.}
93:Extended training (1000 steps; Figure~\ref{fig:training-isr-curves}) reveals ISR $\beta{=}0.1$'s non-hacking at 500 steps ($17.3\%$, seed~42) is transient: by step 1000, H7 escalates $16.0\%{\to}96.7\%$ while non-hacking collapses to $2.2\%$, converging to $\text{ISR}^{*}{=}0.88$ via near-complete tautological gaming.
94:This mirrors exec-only 1000-step (\S\ref{sec:diagnostic}): both reach ${\sim}0\%$ non-hacking despite opposite ISR ($0.88$ vs.\ $0.003$), two paths to the same structural collapse. %% registry: plan002-b01-s42-1000, plan016-extended-1000-s42
129:Hacking-mode classification reverses this reading: ISR seeds average 76
…[truncated 612 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-20T04:48:59.334660+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "p[\\s=<>]|Fisher|permutation|significant|p-value|test",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex",
  "output_mode": "content",
  "-n": "True",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Grep",
  "tool_args": {
    "pattern": "p[\\s=<>]|Fisher|permutation|significant|p-value|test",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex",
    "output_mode": "content",
    "-n": "True",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-20T04:48:59.334824+00:00_

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
573:The 100-step hacking rate (31.2\%) is already substantially 
…[truncated 365 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-20T04:48:59.335000+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "offset": "100",
  "limit": "25"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
    "offset": "100",
    "limit": "25"
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-20T04:48:59.335125+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "offset": "160",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
    "offset": "160",
    "limit": "15"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-20T04:48:59.335275+00:00_

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
110	An independent matched cohort (seeds 47--51, $\beta{=}0.1$; Appendix Table~\ref{tab:matched-perseed}) confirms TS as a deterministic attractor under ISR reward: all 5/5 seeds are TS-dominated ($\text{TS}{=}90.8{\pm}7.5\%$; range $85$--$100\%$), with non-hacking rates of $0$--$6
…[truncated 2616 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-20T04:48:59.335430+00:00_

160	\end{tabular}}
161	\caption{Hacking modes (\% of proved). $^a$Single seed (s42); remaining columns pooled (ISR/Rnd 4B: 5-seed; Prolog/1.7B: 3-seed). $^\sharp$Prolog: strict+functional pooled. $^\ddagger$1.7B N-H overestimates true rate: strict non-hacking (S-NH; \S\ref{sec:rewards}) is $0$--$3.7\%$ (ISR $\beta{=}0.1$), $0\%$ (Rnd $\beta{=}0.1$), $0$--$29\%$ (ISR $\beta{=}0.3$); CI undetected by classifier at 1.7B.}
162	\label{tab:hacking-taxonomy}
163	\end{table}
164	
165	Eight modes are detected by automated classifiers (Table~\ref{tab:hacking-taxonomy}; Appendix~\ref{app:hacking-modes}); CI (contradiction injection) is identified via manual audit at 1.7B in a single seed (s42, Random $\beta{=}0.1$) and may not generalize.
166	CE, TS, and PG account for ${>}90\%$ of hacking across ${\geq}3$ seeds each; ISR modestly increases TS probability ($\text{OR}{=}2.84$; Appendix Table~\ref{tab:bootstrap-ci}), but per-seed variance dominates.
167	All GRPO conditions show ${\geq}80\%$ pooled hacking; only SFT achieves $92.3\%$ non-hacking.
168	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T04:48:59.335602+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
  "offset": "70",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
    "offset": "70",
    "limit": "15"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-20T04:48:59.335769+00:00_

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

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-20T04:48:59.335901+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
  "offset": "120",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
    "offset": "120",
    "limit": "15"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-20T04:48:59.336028+00:00_

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

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-20T04:48:59.336162+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
  "offset": "260",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
    "offset": "260",
    "limit": "15"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-20T04:48:59.336290+00:00_

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

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-20T04:48:59.336415+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
  "offset": "768",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
    "offset": "768",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-20T04:48:59.336541+00:00_

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

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-20T04:48:59.336719+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "offset": "44",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
    "offset": "44",
    "limit": "15"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-20T04:48:59.336873+00:00_

44	Seed~42 reaches $\text{PR}{=}93\%$ via conclusion embedding ($\text{CE}{=}87\%$); s43 collapses to $\text{PR}{=}13\%$ via repetition (87\% of rollouts truncated)\footnote{Exec-only s43 was evaluated with sampling ($T{=}0.7$) rather than greedy decoding; its metrics are included for completeness but are not strictly comparable (Appendix~\ref{app:setup}).}; s44 reaches $\text{PR}{=}98\%$ via tautological collapse ($\text{TS}{=}100\%$, mean $n{=}2.04$). %% registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44
45	Cross-seed PR variance ($\sigma{=}47$\,pp) shows that aggregate metrics obscure qualitatively different failure modes. All three seeds are flagged by $\text{ISR}^*$, whether they pass the PR check (s44) or fail it (s43).
46	By 1000 steps, all three converge to high PR ($0.97{\pm}0.02$) with near-zero non-hacking output via different dominant modes (Appendix Tables~\ref{tab:exec-only-1000},~\ref{tab:fol-detailed}). %% registry: plan016-extended-1000-s42, exec-only-s43-1000step-r7, plan001-exec-only-s44-1000-r2
47	S43 recovers from $\text{PR}{=}13\%$ to $96\%$ entirely through CE exploitation: PR recovery does not imply quality recovery.
48	
49	\textbf{SFT baseline.}
50	SFT on gold formalizations reaches $\text{PR}{=}13.0\%$ (3-seed pooled, 1000 steps) with $92.3\%$ non-hacking ($n{=}39$; per-seed range ${\sim}$91--93\%).
51	TS is entirely absent; CE occurs at $7.7\%$ ($\text{OR}{=}147$ vs.\ exec-only, $p{<}0.001$). %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3
52	The near-absence of hacking under identical data exposure is consistent with hacking being associated with RL optimization rather than data exposure; a 100-step checkpoint ($\text{PR}{=}32\%$, hacking${\geq}31\%$) partially controls for the PR-level confound (Appendix~\ref{app:100step}).
53	Exploit discovery requires the trial-and-error sampling inherent to RL but absent from supervised training; whether SFT would hack at higher PR remains an open quest
…[truncated 403 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-20T04:48:59.337012+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "offset": "122",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
    "offset": "122",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-20T04:48:59.337157+00:00_

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
152	Tautological   & --- & --- & --- & --- & s
…[truncated 1450 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-20T04:48:59.337303+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
  "offset": "88",
  "limit": "35"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
    "offset": "88",
    "limit": "35"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-20T04:48:59.337447+00:00_

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
110	ISR vs.\ Random & 54.3\% {\scriptsize[49.1,59.5]} & 29.5\% {\sc
…[truncated 751 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-20T04:48:59.337605+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
  "offset": "175",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
    "offset": "175",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-20T04:48:59.337768+00:00_

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
190	The practical implication is that ISR (and structurally similar LOO-based diagnostics) should be used exclusively as pos
…[truncated 438 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-20T04:48:59.337915+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
  "offset": "695",
  "limit": "25"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
    "offset": "695",
    "limit": "25"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-20T04:48:59.338058+00:00_

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
713	The reward becomes $r = 0.5\,r_{\text{exec}} +
…[truncated 920 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-20T04:48:59.338228+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex",
  "offset": "125",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex",
    "offset": "125",
    "limit": "15"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-20T04:48:59.338367+00:00_

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

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-20T04:48:59.338613+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex",
  "offset": "510",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex",
    "offset": "510",
    "limit": "15"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-20T04:48:59.339073+00:00_

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

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-20T04:48:59.339268+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
  "offset": "840",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
    "offset": "840",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-20T04:48:59.339444+00:00_

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
856	An SFT warmstart phase (supervised fine-tuning on a small set of gold formalizations before switching to GRPO) could potentially lift models below this threshold
…[truncated 283 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-20T04:48:59.339837+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ProofFOL|prooffol|genuine.*permutation|permutation.*genuine|p.*0\\.10",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "output_mode": "content",
  "-n": "True",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ProofFOL|prooffol|genuine.*permutation|permutation.*genuine|p.*0\\.10",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
    "output_mode": "content",
    "-n": "True",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-20T04:48:59.340041+00:00_

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
paper/abstract.tex:8:% Across six reward conditions, two dataset families (FOLIO and ProofFOL), two logic types, and two model scales, we identify three persistent hacking modes (conclusion embedding [CE] / tautological sho
…[truncated 607 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-20T04:48:59.340202+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "OR.*5\\.5|5\\.5.*CI|100.step.*OR|OR.*147|p.*0\\.001",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "output_mode": "content",
  "-n": "True",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Grep",
  "tool_args": {
    "pattern": "OR.*5\\.5|5\\.5.*CI|100.step.*OR|OR.*147|p.*0\\.001",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
    "output_mode": "content",
    "-n": "True",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-20T04:48:59.340347+00:00_

paper/experiments.tex:51:TS is entirely absent; CE occurs at $7.7\%$ ($\text{OR}{=}147$ vs.\ exec-only, $p{<}0.001$). %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3
paper/experiments.tex:52:The near-absence of hacking under identical data exposure is consistent with hacking being associated with RL optimization rather than data exposure; a 100-step checkpoint ($\text{PR}{=}32\%$, hacking${\geq}31\%$) partially controls for the PR-level confound (Appendix~\ref{app:100step}).
paper/main.bbl:378:\newblock \href {https://arxiv.org/abs/2502.14768} {{Logic-RL: Unleashing LLM
paper/appendix.tex:115:SFT vs.\ Exec-only & 92.3\% {\scriptsize[79.7,97.3]} & 7.5\% & 147 & ${<}0.001$ \\
paper/appendix.tex:707:The 100-step hacking rate (31.2\%) is already substantially above SFT (7.7\%), supporting the claim that hacking is associated with RL optimization rather than prove-rate level alone.
paper/appendix.tex:733:\caption{Per-seed results for the matched replication cohort (seeds 47--51, $\beta{=}0.1$, 500 steps). PR = prove rate, ISR$^*$ = proved-only ISR, TS/CE/N-H = percentage among proved samples. Wilson 95\% CIs for N-H: ISR s47 $[1.1, 8.7]$, s48 $[0, 5.5]$, s49 $[0.2, 6.3]$, s50 $[2.8, 12.7]$, s51 $[0.2, 5.6]$; Random s47 $[3.1, 13.9]$, s48 $[1.7, 10.5]$, s49 $[0, 43.4]$, s50 $[1.2, 14.8]$, s51 $[7.5, 24.3]$.}
paper/main.aux:2090:[Omitted long matching line]
paper/main.aux:2091:\newlabel{tab:matched-perseed}{{13}{23}{Per-seed results for the matched replication cohort (seeds 47--51, $\beta {=}0.1$, 500 steps). PR = prove rate, ISR$^*$ = proved-only ISR, TS/CE/N-H = percentage among proved samples. Wilson 95\% CIs for N-H: ISR s47 $[1.1, 8.7]$, s48 $[0, 5.5]$, s49 $[0.2, 6.3]$, s50 $[2.8, 12.7]$, s51 $[0.2, 5.6]$; Random s47 $[3.1, 13.9]$, s48 $[1.7, 10.5]$, s49 $[0, 43.4]$, s50 $[1.2, 14.8]$, s51 $[7.5, 24.3]$}{table.caption.79}{}}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-20T04:48:59.340516+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "p.*=.*0\\.10|0\\.10.*permutation|genuine.*rate.*per",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Grep",
  "tool_args": {
    "pattern": "p.*=.*0\\.10|0\\.10.*permutation|genuine.*rate.*per",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-20T04:48:59.340644+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-20T04:48:59.340870+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Aggregate.*genuine|genuine.*Aggregate|76\\.8",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Aggregate.*genuine|genuine.*Aggregate|76\\.8",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-20T04:48:59.341015+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-20T04:48:59.341152+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "OR.*5\\.5|5\\.5.*OR",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Grep",
  "tool_args": {
    "pattern": "OR.*5\\.5|5\\.5.*OR",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-20T04:48:59.341276+00:00_

docs/paper/experiments.tex:38:A 100-step RL checkpoint (Appendix~\ref{app:100step}) at $\text{PR}{=}32\%$ already shows 31.2\% hacking (vs.\ SFT's 7.7\%; $\text{OR}{=}5.5$, 95\% CI $[1.4, 22.0]$), indicating reward hacking emerges early in RL training, not merely at high PR.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-20T04:48:59.341472+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

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
  "recorded_role": "tool",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Bash",
  "tool_args": {
    "command": "cat << 'PYEOF' | python3\nimport json\n\n# All statistical tests with reported p-values from paper/ directory\ntests = [\n    {\n        \"name\": \"Fisher exact: TS domination (matched 5+5)\",\n        \"original_p\": 0.004,\n        \"context\": \"ISR 5/5 TS-dominated vs Random 0/5; OR=inf, BF10=77\",\n        \"test_type\": \"Fisher exact\",\n        \"location\": \"experiments.tex:104,114; appendix.tex:774\"\n    },\n    {\n        \"name\": \"Mann-Whitney U: ISR* (matched 5+5)\",\n        \"original_p\": 0.004,\n        \"context\": \"U=25, r=1.0; ISR* comparison between matched ISR and Random cohorts\",\n        \"test_type\": \"Mann-Whitney U\",\n        \"location\": \"experiments.tex:114; appendix.tex:775\"\n    },\n    {\n        \"name\": \"Mann-Whitney U: TS rate (matched 5+5)\",\n        \"original_p\": 0.004,\n        \"context\": \"U=25; TS rate comparison between matched ISR and Random cohorts\",\n        \"test_type\": \"Mann-Whitney U\",\n        \"location\": \"appendix.tex:776\"\n    },\n    {\n        \"name\": \"Permutation: N-H rate (matched 5+5)\",\n        \"original_p\": 0.917,\n        \"context\": \"Δ=-3.6pp; genuine/non-hacking rate ISR 2.3% vs Random 5.9%\",\n        \"test_type\": \"Permutation\",\n        \"location\": \"experiments.tex:114; appendix.tex:777\"\n    },\n    {\n        \"name\": \"Fisher exact: N-H rate (5-seed pooled)\",\n        \"original_p\": 1e-8,\n        \"context\": \"ISR 22.6% vs Random 7.7%, OR=3.48 (uncorrected for PG/FN)\",\n        \"test_type\": \"Fisher exact\",\n        \"location\": \"appendix.tex:105\"\n    },\n    {\n        \"name\": \"Fisher exact: N-H rate (3-seed, PG+FN corrected)\",\n        \"original_p\": 0.182,\n        \"context\": \"ISR 6.06% vs Random 9.5%, OR=0.61 (n.s.)\",\n        \"test_type\": \"Fisher exact\",\n        \"location\": \"appendix.tex:107,269\"\n    },\n    {\n        \"name\": \"Fisher exact: TS rate (5-seed pooled)\",\n        \"original_p\": 4.82e-12,\n        \"context\": \"ISR 54.3% vs Random 29.5%, OR=2.84\",\n        \"test_type\": \"Fisher exact\",\n        \"location\": \"appendix.tex:110\"\n    },\n    {\n        \"name\": \"Fisher exact: TS rate (3-seed sensitivity)\",\n        \"original_p\": 1.3e-39,\n        \"context\": \"ISR 70.6% vs Random 13.7%, OR=15.05\",\n        \"test_type\": \"Fisher exact\",\n        \"location\": \"appendix.tex:112\"\n    },\n    {\n        \"name\": \"Fisher exact: SFT vs Exec-only N-H rate\",\n        \"original_p\": 0.001,\n        \"context\": \"SFT 92.3% vs Exec-only 7.5%, OR=147 (p<0.001, using 0.001 as upper bound)\",\n        \"test_type\": \"Fisher exact\",\n        \"location\": \"experiments.tex:51; appendix.tex:115\"\n    },\n    {\n        \"name\": \"CMH: TS (seed-stratified)\",\n        \"original_p\": 5.6e-16,\n        \"context\": \"OR_CMH=2.46, 95% CI [1.85,3.27]; authors note CMH p-values are inflated due to within-seed dependence\",\n        \"test_type\": \"Cochran-Mantel-Haenszel\",\n        \"location\": \"appendix.tex:125\"\n    },\n    {\n        \"name\": \"CMH: non-hacking (seed-stratified)\",\n        \"original_p\": 4.5e-10,\n        \"context\": \"OR_CMH=3.37, 95% CI [2.21,5.13]; authors note CMH p-values are inflated\",\n        \"test_type\": \"Cochran-Mantel-Haenszel\",\n        \"location\": \"appendix.tex:125\"\n    },\n    {\n        \"name\": \"Seed-level permutation: TS (n=5 per group)\",\n        \"original_p\": 0.28,\n        \"context\": \"Seed as unit of observation; limited power (min achievable p=0.008)\",\n        \"test_type\": \"Permutation\",\n        \"location\": \"appendix.tex:127\"\n    },\n    {\n        \"name\": \"Seed-level permutation: N-H (n=5 per group)\",\n        \"original_p\": 0.26,\n        \"context\": \"Seed as unit of observation; limited power (min achievable p=0.008)\",\n        \"test_type\": \"Permutation\",\n        \"location\": \"appendix.tex:127\"\n    },\n    {\n        \"name\": \"Spearman: ISR vs NLI accuracy\",\n        \"original_p\": 0.187,\n        \"context\": \"ρ=-0.049, n.s.; confirms ISR uncorrelated with downstream task performance\",\n        \"test_type\": \"Spearman correlation\",\n        \"location\": \"appendix.tex:77\"\n    }\n]\n\nN = len(tests)\n\nfor t in tests:\n    t[\"bonferroni_p\"] = min(t[\"original_p\"] * N, 1.0)\n    t[\"still_significant_005\"] = t[\"bonferroni_p\"] < 0.05\n    t[\"still_significant_010\"] = t[\"bonferroni_p\"] < 0.10\n\nresult = {\n    \"n_tests\": N,\n    \"method\": \"Bonferroni\",\n    \"alpha_levels\": [0.05, 0.10],\n    \"tests\": tests\n}\n\nwith open(\"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/bonferroni_correction.json\", \"w\") as f:\n    json.dump(result, f, indent=2, ensure_ascii=False)\n\n# Summary\nn_orig_005 = sum(1 for t in tests if t[\"original_p\"] < 0.05)\nn_orig_010 = sum(1 for t in tests if t[\"original_p\"] < 0.10)\nn_corr_005 = sum(1 for t in tests if t[\"still_significant_005\"])\nn_corr_010 = sum(1 for t in tests if t[\"still_significant_010\"])\n\nprint(f\"Total tests (N): {N}\")\nprint(f\"\\nPre-correction significant at α=0.05: {n_orig_005}/{N}\")\nprint(f\"Pre-correction significant at α=0.10: {n_orig_010}/{N}\")\nprint(f\"\\nPost-Bonferroni significant at α=0.05: {n_corr_005}/{N}\")\nprint(f\"Post-Bonferroni significant at α=0.10: {n_corr_010}/{N}\")\n\nprint(\"\\n--- All tests ---\")\nfor t in tests:\n    flag = \"✓\" if t[\"still_significant_005\"] else (\"~\" if t[\"still_significant_010\"] else \"✗\")\n    print(f\"  [{flag}] {t['name']}: p_orig={t['original_p']:.4g} → p_bonf={t['bonferroni_p']:.4g}\")\n\n# Tests that lose significance\nprint(\"\\n--- Tests that LOSE significance after Bonferroni ---\")\nlost = [t for t in tests if t[\"original_p\"] < 0.05 and not t[\"still_significant_005\"]]\nif lost:\n    for t in lost:\n        print(f\"  {t['name']}: p_orig={t['original_p']:.4g} → p_bonf={t['bonferroni_p']:.4g}\")\nelse:\n    print(\"  None — all originally significant tests remain significant at α=0.05\")\n\nlost_010 = [t for t in tests if t[\"original_p\"] < 0.10 and not t[\"still_significant_010\"]]\nif lost_010:\n    print(f\"\\n--- Lost at α=0.10 ---\")\n    for t in lost_010:\n        print(f\"  {t['name']}: p_orig={t['original_p']:.4g} → p_bonf={t['bonferroni_p']:.4g}\")\nPYEOF\n",
    "description": "Compute Bonferroni correction on all paper p-values"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-20T04:48:59.341734+00:00_

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

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r15-bonferroni_20260520T044634",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 63 · 2026-05-20T04:48:59.341962+00:00_

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
  "session": "worker_analysis_r15-bonferroni_20260520T044634"
}
```

</details>

---
