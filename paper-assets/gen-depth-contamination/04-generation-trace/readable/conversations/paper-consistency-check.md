# paper consistency check

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 0
- **Tool calls:** 22
- **Original source:** `logs/chats/worker_paper_consistency_check_20260523T002253.jsonl`
- **Structured JSON:** [`ebe03db1d84d8e88b382.json`](../../sessions/eb/ebe03db1d84d8e88b382.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

45 recorded events

### Tool call

_source line 1 · 2026-05-23T00:25:56.252428+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "of six|of ten",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "output_mode": "content",
  "-n": "True",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_consistency_check_20260523T002253",
  "tool": "Grep",
  "tool_args": {
    "pattern": "of six|of ten",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
    "output_mode": "content",
    "-n": "True",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-23T00:25:56.252754+00:00_

docs/paper/appendix_extended.tex:155:Seven of ten configurations retain CI lower bounds above $\theta{=}0.60$; three marginal $\Kempirical{=}2$ configurations (Pythia-1.4B, Qwen-cont, LLaMA-8B) see their lower bounds dip below $\theta$ under the stricter criterion ($0.5934$, $0.5976$, and $0.5988$, respectively).
docs/paper/main.tex:71:(3)~\emph{Threshold sensitivity}: $\Kempirical$ varies with the decision threshold $\theta$, ranging from 2--3 at $\theta{=}0.55$ to 1 at $\theta{=}0.70$; two of ten configurations are marginal at our reference $\theta{=}0.60$.
docs/paper/conclusion.tex:9:Under Bonferroni correction for 10 simultaneous comparisons, three of six $\Kempirical{=}2$ configurations retain significance at the 99.5\% level; the remaining three marginal cases preserve point estimates above $\theta$.
docs/paper/experiments_c1.tex:45:[Omitted long matching line]
docs/paper/experiments_c1.tex:46:Under Bonferroni correction for 10 simultaneous comparisons (99.5\% CIs), three of six boundary configurations retain CI lower bounds above $\theta$; the three most marginal cases, Pythia-1.4B (0.593), Qwen-continuation (0.598), and LLaMA-8B (0.599), fall below the widened interval.
docs/paper/experiments_c1.tex:60:\caption{$\Kempirical(\theta)$ sensitivity curve for six configurations. $\Kempirical$: maximum discriminable depth; $\theta$: AUC decision threshold. Five of six configurations yield $\Kempirical{=}2$ at $\theta{=}0.60$ (dashed line); OLMo yields $\Kempirical{=}1$. At $\theta{=}0.70$, all drop to $\Kempirical{=}1$.}
docs/paper/experiments_c1.tex:65:Five of six configurations yield $\Kempirical = 2$ within $\theta \in [0.51, 0.61]$ (OLMo: $\Kempirical = 1$ throughout); at $\theta{=}0.55$, two Qwen configurations reach $\Kempirical = 3$; at $\theta{=}0.70$, all drop to $\Kempirical = 1$.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_consistency_check_20260523T002253",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T00:25:56.252958+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "four of six",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "output_mode": "content",
  "-n": "True",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_consistency_check_20260523T002253",
  "tool": "Grep",
  "tool_args": {
    "pattern": "four of six",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
    "output_mode": "content",
    "-n": "True",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-23T00:25:56.253098+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_consistency_check_20260523T002253",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T00:25:56.253231+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "6539",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "output_mode": "content",
  "-n": "True",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_consistency_check_20260523T002253",
  "tool": "Grep",
  "tool_args": {
    "pattern": "6539",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
    "output_mode": "content",
    "-n": "True",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-23T00:25:56.253358+00:00_

docs/paper/appendix.tex:139:    1v2 & .6955 & [.686,\,.704]\rlap{$^*$} & .6539 & [.645,\,.663]\rlap{$^*$} & .5080 & [.496,\,.519] & .6112 & [.602,\,.621]\rlap{$^*$} & .6168 & [.608,\,.626]\rlap{$^*$} & .626 & [.617,\,.635]\rlap{$^*$} & .6123 & [.603,\,.622]\rlap{$^*$} & .5934 & [.584,\,.603] & .5955 & & .5981 & [.588,\,.608] \\

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_consistency_check_20260523T002253",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T00:25:56.253480+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "6074",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "output_mode": "content",
  "-n": "True",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_consistency_check_20260523T002253",
  "tool": "Grep",
  "tool_args": {
    "pattern": "6074",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
    "output_mode": "content",
    "-n": "True",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-23T00:25:56.253615+00:00_

docs/paper/appendix_extended.tex:170:Pythia-1.4B               & 1v2 & .6074 & .0050 & $[.593,\,.621]$ & $\times$ \\
docs/paper/appendix_extended.tex:196:For Pythia-1.4B (continuation, C4), the 5K and 10K samples agree on $\Kempirical{=}2$: the 0v1 AUC is nearly identical ($0.9722$ vs.\ $0.9712$), and the boundary 1v2 AUC shifts from $0.6074$ to $0.6175$ ($\Delta = +0.010$).
docs/paper/experiments_c1.tex:26:1v2 & .6955 & [.686,\,.704]\rlap{$^*$} & .6074 & [.598,\,.617]\rlap{$^*$} & .5001 & [.496,\,.519] & .6112 & [.602,\,.621]\rlap{$^*$} & .6168 & [.608,\,.626]\rlap{$^*$} \\
docs/paper/experiments_c1.tex:45:[Omitted long matching line]
docs/paper/tables/tab_domain_model_kstar_full.tex:14:Pythia        & 1.4B & \textbf{2} & 0.6074~(1v2) & \textbf{3} & 0.6545~(2v3) & \textbf{1} & 0.975~(0v1) \\

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_consistency_check_20260523T002253",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T00:25:56.253821+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "5080|\\.508",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "output_mode": "content",
  "-n": "True",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_consistency_check_20260523T002253",
  "tool": "Grep",
  "tool_args": {
    "pattern": "5080|\\.508",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
    "output_mode": "content",
    "-n": "True",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-23T00:25:56.253975+00:00_

docs/paper/appendix.tex:139:    1v2 & .6955 & [.686,\,.704]\rlap{$^*$} & .6539 & [.645,\,.663]\rlap{$^*$} & .5080 & [.496,\,.519] & .6112 & [.602,\,.621]\rlap{$^*$} & .6168 & [.608,\,.626]\rlap{$^*$} & .626 & [.617,\,.635]\rlap{$^*$} & .6123 & [.603,\,.622]\rlap{$^*$} & .5934 & [.584,\,.603] & .5955 & & .5981 & [.588,\,.608] \\
docs/paper/appendix.tex:142:    4v5 & .5340 & & .5136 & & .4942 & & .5141 & & .5085 & & .518 & [.508,\,.529] & .5159 & [.505,\,.527] & .5180 & [.507,\,.529] & -- & -- & .5025 & [.492,\,.514] \\
docs/paper/appendix.tex:343:    1v2 & $.696\;[.686,.704]$ & $.654\;[.645,.663]$ & $.508\;[.496,.519]$ & $.611\;[.602,.621]$ \\
docs/paper/experiments_c1.tex:29:4v5 & .5340 & & .5079 & & .4942 & & .5141 & & .5085 & \\
docs/paper/discussion.tex:37:$\Kempirical{=}1$ configurations cluster at 1v2 $\auc$ 0.508--0.598, well separated from the $\Kempirical{=}2$ range (0.611--0.696); $\Kempirical{=}1$ is not a classifier failure but a text property, as these models produce first-generation output so human-like that statistical features cannot distinguish depth~1 from depth~2.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_consistency_check_20260523T002253",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T00:25:56.254108+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "5001|0\\.500",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "output_mode": "content",
  "-n": "True",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_consistency_check_20260523T002253",
  "tool": "Grep",
  "tool_args": {
    "pattern": "5001|0\\.500",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
    "output_mode": "content",
    "-n": "True",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-23T00:25:56.254234+00:00_

docs/paper/appendix_extended.tex:201:OLMo-1B (continuation, C4) is the only configuration that yields $\Kempirical{=}1$ at both 5K and 10K, with virtually identical depth profiles (0v1 $\auc = 0.9871$ vs.\ $0.9860$; 1v2 $\auc = 0.4984$ vs.\ $0.5001$); the 1v2 AUC at random level is consistent with Qwen cross-scoring, which places OLMo well below the discrimination boundary.
docs/paper/experiments_c1.tex:26:1v2 & .6955 & [.686,\,.704]\rlap{$^*$} & .6074 & [.598,\,.617]\rlap{$^*$} & .5001 & [.496,\,.519] & .6112 & [.602,\,.621]\rlap{$^*$} & .6168 & [.608,\,.626]\rlap{$^*$} \\
docs/paper/experiments_c1.tex:45:[Omitted long matching line]
docs/paper/tables/tab_domain_model_kstar_full.tex:17:OLMo          & 1B   & 1 & 0.500~(1v2) & 1\textsuperscript{$*$} & --- & \textbf{1} & 0.993~(0v1) \\

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_consistency_check_20260523T002253",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-23T00:25:56.254378+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "OLMo.*K\\*|K\\*.*OLMo|OLMo.*Kempirical|Kempirical.*OLMo",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "output_mode": "content",
  "-n": "True",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_consistency_check_20260523T002253",
  "tool": "Grep",
  "tool_args": {
    "pattern": "OLMo.*K\\*|K\\*.*OLMo|OLMo.*Kempirical|Kempirical.*OLMo",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
    "output_mode": "content",
    "-n": "True",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-23T00:25:56.254530+00:00_

docs/paper/appendix_extended.tex:17:\captionof{table}{Cross-scorer validation on Qwen-generated text. Alternative scorers (Pythia-1.4B, OLMo-1B) preserve feature ranking ($\rho > 0.90$) and rewrite-mode $\Kempirical = 2$, but reduce continuation-mode $\Kempirical$ from 2 to 1.}
docs/paper/appendix_extended.tex:53:The neural probe yields model-dependent $\Kempirical^{\text{neural}}$: $3$ for Qwen (self-familiarity effect from instruction-tuned representations) but $2$ for Pythia; OLMo yields $\Kempirical^{\text{neural}} = 1$ (1v2 $\auc = 0.5054$), consistent with the 15D LightGBM boundary.
docs/paper/appendix_extended.tex:54:The 15D model-free features yield $\Kempirical = 2$ for Pythia and Qwen, while OLMo yields $\Kempirical = 1$ under the standardized pipeline.
docs/paper/appendix_extended.tex:201:OLMo-1B (continuation, C4) is the only configuration that yields $\Kempirical{=}1$ at both 5K and 10K, with virtually identical depth profiles (0v1 $\auc = 0.9871$ vs.\ $0.9860$; 1v2 $\auc = 0.4984$ vs.\ $0.5001$); the 1v2 AUC at random level is consistent with Qwen cross-scoring, which places OLMo well below the discrimination boundary.
docs/paper/experiments_c1.tex:45:[Omitted long matching line]
docs/paper/experiments_c1.tex:48:By architecture family: Qwen (4/4) and LLaMA (1/1) yield $\Kempirical{\geq}2$ at nominal significance; OLMo (1/1), Mistral (1/1), and Gemma (1/1) yield $\Kempirical{=}1$; Pythia exhibits a scale-dependent split (1.4B: $\Kempirical{=}2$, 6.9B: $\Kempirical{=}1$).
docs/paper/experiments_c1.tex:60:\caption{$\Kempirical(\theta)$ sensitivity curve for six configurations. $\Kempirical$: maximum discriminable depth; $\theta$: AUC decision threshold. Five of six configurations yield $\Kempirical{=}2$ at $\theta{=}0.60$ (dashed line); OLMo yields $\Kempirical{=}1$. At $\theta{=}0.70$, all drop to $\Kempirical{=}1$.}
docs/paper/experiments_c1.tex:65:Five of six configurations yield $\Kempirical = 2$ within $\theta \in [0.51, 0.61]$ (OLMo: $\Kempirical = 
…[truncated 1784 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_consistency_check_20260523T002253",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-23T00:25:56.254675+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "6/10|6 of 10|six of ten|4/10|4 of 10|four of ten",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "output_mode": "content",
  "-n": "True",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_consistency_check_20260523T002253",
  "tool": "Grep",
  "tool_args": {
    "pattern": "6/10|6 of 10|six of ten|4/10|4 of 10|four of ten",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
    "output_mode": "content",
    "-n": "True",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-23T00:25:56.254815+00:00_

docs/paper/experiments_c1.tex:45:[Omitted long matching line]
docs/paper/discussion.tex:17:The 15D features trade one depth level of sensitivity for cross-model consistency (6/10 configurations $\Kempirical{=}2$), making them the preferred operational choice.
docs/paper/appendix.tex:129:  $\Kempirical = 2$ holds for 6/10 conditions at $\theta{=}0.60$ (OLMo-1B, Mistral-7B, Pythia-6.9B, Gemma-2-2B: $\Kempirical{=}1$).}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_consistency_check_20260523T002253",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-23T00:25:56.254948+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "—|–",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "output_mode": "content",
  "-n": "True",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_consistency_check_20260523T002253",
  "tool": "Grep",
  "tool_args": {
    "pattern": "—|–",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
    "output_mode": "content",
    "-n": "True",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-23T00:25:56.255073+00:00_

docs/paper/main.tex:1:% EMNLP 2026 Main — ARR May 2026

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_consistency_check_20260523T002253",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-23T00:25:56.255199+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex",
  "offset": "130",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_consistency_check_20260523T002253",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex",
    "offset": "130",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-23T00:25:56.255347+00:00_

130	  \label{tab:kstar_ci_extended}
131	  \resizebox{\textwidth}{!}{%
132	  \begin{tabular}{lcccccccccccccccccccc}
133	    \toprule
134	     & \multicolumn{2}{c}{Qwen-rw} & \multicolumn{2}{c}{Pythia} & \multicolumn{2}{c}{OLMo} & \multicolumn{2}{c}{Qwen-cont} & \multicolumn{2}{c}{Qwen-7B\rlap{$^\ddagger$}} & \multicolumn{2}{c}{Qwen-base} & \multicolumn{2}{c}{LLaMA-8B} & \multicolumn{2}{c}{Mistral-7B} & \multicolumn{2}{c}{Pythia-6.9B\rlap{$^\S$}} & \multicolumn{2}{c}{Gemma-2B} \\
135	    \cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}\cmidrule(lr){8-9}\cmidrule(lr){10-11}\cmidrule(lr){12-13}\cmidrule(lr){14-15}\cmidrule(lr){16-17}\cmidrule(lr){18-19}\cmidrule(lr){20-21}
136	     & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI \\
137	    \midrule
138	    0v1 & .9956 & & .9932 & & .9860 & & .9971 & & .9638 & [.961,\,.967] & .987 & [.985,\,.989] & .9224 & [.917,\,.927] & .9842 & [.982,\,.986] & .9599 & & .953 & [.949,\,.957] \\
139	    1v2 & .6955 & [.686,\,.704]\rlap{$^*$} & .6539 & [.645,\,.663]\rlap{$^*$} & .5080 & [.496,\,.519] & .6112 & [.602,\,.621]\rlap{$^*$} & .6168 & [.608,\,.626]\rlap{$^*$} & .626 & [.617,\,.635]\rlap{$^*$} & .6123 & [.603,\,.622]\rlap{$^*$} & .5934 & [.584,\,.603] & .5955 & & .5981 & [.588,\,.608] \\
140	    2v3 & .5893 & [.580,\,.599] & .5514 & [.542,\,.563] & .4973 & [.486,\,.509] & .5609 & [.551,\,.571] & .5492 & [.539,\,.559] & .550 & [.540,\,.560] & .5273 & [.517,\,.538] & .5402 & [.530,\,.551] & .5298 & & .534 & [.523,\,.545] \\
141	    3v4 & .5435 & & .5152 & & .5024 & & .5409 & & .5276 & & .529 & [.519,\,.540] & .5168 & [.506,\,.528] & .5233 & [.513,\,.534] & .5135 & & .5033 & [.492,\,.514] \\
142	    4v5 & .5340 & & .5136 & & .4942 & & .5141 & & .5085 & & .518 & [.508,\,.529] & .5159 & [.505,\,.527] & .5180 & [.507,\,.529] & -- & -- & .5025 & [.492,\,.514] \\
143	    \bottomrule
144	    \
…[truncated 439 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_consistency_check_20260523T002253",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-23T00:25:56.255492+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex",
  "offset": "335",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_consistency_check_20260523T002253",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex",
    "offset": "335",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-23T00:25:56.255635+00:00_

335	  \caption{Pairwise AUC with bootstrap 95\% CIs for four model-mode configurations (1{,}000 resamples). All pairs $p < 0.01$ except OLMo 1v2--4v5 ($p > 0.09$).}
336	  \label{tab:s8_cv_folds}
337	  \resizebox{\columnwidth}{!}{%
338	  \begin{tabular}{lcccc}
339	    \toprule
340	    & \textbf{Qwen-rw} & \textbf{Pythia} & \textbf{OLMo} & \textbf{Qwen-cont} \\
341	    \midrule
342	    0v1 & $.996\;[.995,.997]$ & $.993\;[.992,.994]$ & $.986\;[.984,.988]$ & $.997\;[.996,.998]$ \\
343	    1v2 & $.696\;[.686,.704]$ & $.654\;[.645,.663]$ & $.508\;[.496,.519]$ & $.611\;[.602,.621]$ \\
344	    \cmidrule(lr){1-5}
345	    2v3 & $.589\;[.580,.599]$ & $.551\;[.542,.563]$ & $.497\;[.486,.509]$ & $.561\;[.551,.571]$ \\
346	    3v4 & $.544\;[.533,.555]$ & $.515\;[.504,.526]$ & $.502\;[.491,.513]$ & $.541\;[.531,.551]$ \\
347	    4v5 & $.534\;[.524,.545]$ & $.514\;[.502,.525]$ & $.494\;[.483,.506]$ & $.514\;[.504,.526]$ \\
348	    \bottomrule
349	  \end{tabular}}
350	\end{table}
351	
352	%%% Table S9: Binary Detector Spearman ρ (exp-012)
353	\begin{table}[t]
354	  \centering

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_consistency_check_20260523T002253",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-23T00:25:56.255789+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_domain_model_kstar.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_consistency_check_20260523T002253",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_domain_model_kstar.tex"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-23T00:25:56.255942+00:00_

1	\begin{table}[t]
2	\centering
3	\caption{Generative depth $K^*$ across domains and models (scorer: Qwen2.5-1.5B, $\theta{=}0.60$). Bold values indicate the dominant mode per domain. $K^*$ is remarkably consistent within each domain: C4 yields $K^*{=}2$, arXiv yields $K^*{=}3$, and Wikipedia yields $K^*{=}1$, confirming that generative depth is domain-dependent and low-bounded.}
4	\label{tab:domain_model_kstar}
5	{\small
6	\begin{tabular}{llccc}
7	\toprule
8	\textbf{Model} & \textbf{Size} & \textbf{C4}~$K^*$ & \textbf{arXiv}~$K^*$ & \textbf{Wiki}~$K^*$ \\
9	\midrule
10	Qwen2.5       & 1.5B & \textbf{2} & \textbf{3} & \textbf{1}\textsuperscript{$\dagger$} \\
11	Qwen2.5       & 7B   & \textbf{2} & \textbf{3} & \textbf{1}\textsuperscript{$\dagger$} \\
12	Pythia        & 1.4B & \textbf{2} & \textbf{3} & \textbf{1} \\
13	LLaMA-3.1    & 8B   & \textbf{2} & \textbf{3} & \textbf{1} \\
14	Mistral       & 7B   & 1\textsuperscript{$\ddagger$} & \textbf{3} & \textbf{1} \\
15	OLMo          & 1B   & 1 & 1\textsuperscript{$*$} & \textbf{1} \\
16	\midrule
17	\textit{Dominant} & & \textbf{2} & \textbf{3} & \textbf{1} \\
18	\bottomrule
19	\end{tabular}
20	}
21	\vspace{2pt}
22	
23	{\footnotesize
24	\textsuperscript{$\dagger$}Scorer artifact: Qwen-1.5B scorer yields $K^*{=}2$; Pythia scorer yields $K^*{=}1$ (see \S\ref{sec:crossscorer}).\\
25	\textsuperscript{$\ddagger$}Domain-specific one-wash: AUC(1v2)${=}0.594{<}\theta$; arXiv rescues to $K^*{=}3$. Cross-scorer validated: Pythia-1.4B also yields $K^*{=}1$ (AUC${=}0.570$).\\
26	\textsuperscript{$*$}Capacity failure: OLMo-1B generates out-of-domain text on arXiv.
27	}
28	\end{table}
29	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_consistency_check_20260523T002253",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-23T00:25:56.256075+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_domain_model_kstar_full.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_consistency_check_20260523T002253",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_domain_model_kstar_full.tex"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-23T00:25:56.256213+00:00_

1	\begin{table*}[t]
2	\centering
3	\caption{Full generative depth results with AUC at the $K^*$ boundary (scorer: Qwen2.5-1.5B, $\theta{=}0.60$). AUC($k$v$k{+}1$) denotes the area under the ROC curve distinguishing generation $k$ from generation $k{+}1$. Bold indicates the dominant $K^*$ mode per domain. For Wikipedia ($K^*{=}1$), boundary AUC reports 0v1. All AUC values computed on held-out test splits ($n{=}500$ per class).}
4	\label{tab:domain_model_kstar_full}
5	{\small
6	\begin{tabular}{llcccccc}
7	\toprule
8	& & \multicolumn{2}{c}{\textbf{C4}} & \multicolumn{2}{c}{\textbf{arXiv}} & \multicolumn{2}{c}{\textbf{Wikipedia}} \\
9	\cmidrule(lr){3-4} \cmidrule(lr){5-6} \cmidrule(lr){7-8}
10	\textbf{Model} & \textbf{Size} & $K^*$ & AUC(boundary) & $K^*$ & AUC(boundary) & $K^*$ & AUC(boundary) \\
11	\midrule
12	Qwen2.5       & 1.5B & \textbf{2} & 0.6262~(1v2) & \textbf{3} & 0.6427~(2v3) & \textbf{1}\textsuperscript{$\dagger$} & ---\textsuperscript{$\S$} \\
13	Qwen2.5       & 7B   & \textbf{2} & 0.6178~(1v2) & \textbf{3} & 0.6255~(2v3) & \textbf{1}\textsuperscript{$\dagger$} & 0.967~(0v1) \\
14	Pythia        & 1.4B & \textbf{2} & 0.6074~(1v2) & \textbf{3} & 0.6545~(2v3) & \textbf{1} & 0.975~(0v1) \\
15	LLaMA-3.1    & 8B   & \textbf{2} & 0.6123~(1v2) & \textbf{3} & 0.6215~(2v3) & \textbf{1} & 0.932~(0v1) \\
16	Mistral       & 7B   & 1\textsuperscript{$\ddagger$} & 0.594~(1v2) & \textbf{3} & 0.6275~(2v3) & \textbf{1} & 0.961~(0v1) \\
17	OLMo          & 1B   & 1 & 0.500~(1v2) & 1\textsuperscript{$*$} & --- & \textbf{1} & 0.993~(0v1) \\
18	\bottomrule
19	\end{tabular}
20	}
21	\vspace{2pt}
22	
23	{\footnotesize
24	\textsuperscript{$\dagger$}Scorer artifact: Qwen-1.5B scorer yields $K^*{=}2$; cross-family scorer (Pythia-1.4B) yields $K^*{=}1$ ($\Delta = -2.4$\,pp). Controlled value shown (Appendix~\ref{app:crossscorer}).\\
25	\textsuperscript{$\ddagger$}AUC(1v2)${=}0.594{<}\theta{=}0.60$: Mistral exhibits domain-specific one-wash on C4 web text. Cross-scorer validated: Pythia
…[truncated 283 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_consistency_check_20260523T002253",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-23T00:25:56.256393+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex",
  "offset": "40",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_consistency_check_20260523T002253",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex",
    "offset": "40",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-23T00:25:56.256548+00:00_

40	\includegraphics[width=\columnwidth]{figures/fig2_auc_decay.pdf}
41	\caption{Pairwise $\auc$ decay across depth pairs for model-mode configurations (solid) and decoding strategies (dashed); shaded bands show bootstrap 95\% confidence intervals. The horizontal dashed line marks $\theta = 0.60$.}
42	\label{fig:auc_decay}
43	\end{figure}
44	
45	Table~\ref{tab:kstar_ci} and Figure~\ref{fig:auc_decay} show $\Kempirical \leq 2$ across all 10 model configurations: 6/10 configurations yield $\Kempirical{=}2$ (Qwen with 4 configs, LLaMA-8B, and Pythia-1.4B, spanning three of six families) (1v2 $\auc$ range: 0.6074--0.6955; five of six CI lower bounds $> \theta$; permutation $p < 0.001$), while OLMo-1B, Mistral-7B, Pythia-6.9B, and Gemma-2-2B yield $\Kempirical{=}1$ (1v2 $\auc$: 0.500, 0.594, 0.596, and 0.598, all below $\theta$; Section~\ref{sec:boundary_cases}).
46	Under Bonferroni correction for 10 simultaneous comparisons (99.5\% CIs), three of six boundary configurations retain CI lower bounds above $\theta$; the three most marginal cases, Pythia-1.4B (0.593), Qwen-continuation (0.598), and LLaMA-8B (0.599), fall below the widened interval.
47	All three retain point estimates above $\theta$; Qwen-continuation and LLaMA-8B also retain uncorrected CI lower bounds above $\theta$, while Pythia-1.4B (0.598) falls marginally below. The near-misses reflect narrow effect sizes rather than classification failure.
48	By architecture family: Qwen (4/4) and LLaMA (1/1) yield $\Kempirical{\geq}2$ at nominal significance; OLMo (1/1), Mistral (1/1), and Gemma (1/1) yield $\Kempirical{=}1$; Pythia exhibits a scale-dependent split (1.4B: $\Kempirical{=}2$, 6.9B: $\Kempirical{=}1$).
49	LLaMA-3.1-8B confirms $\Kempirical{=}2$ (0v1 $\auc = 0.9225$, 1v2 $\auc = 0.6123\;[0.603,\,0.622]$; CI lower bound above $\theta$; Table~\ref{tab:kstar_ci_extended}).
50	All four decoding strategies likewise yield $\Kempirical{=}2$ (Table~\ref{tab:s2_decoding}).
51	The 1v2 spread due to generation mode (
…[truncated 1876 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_consistency_check_20260523T002253",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-23T00:25:56.256690+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex",
  "offset": "60",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_consistency_check_20260523T002253",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex",
    "offset": "60",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-23T00:25:56.256840+00:00_

60	\input{discussion}
61	
62	% === Section 7: Conclusion ===
63	\input{conclusion}
64	
65	% === Limitations (ACL required, unnumbered) ===
66	\section*{Limitations}
67	
68	Our study has three main limitations.
69	(1)~\emph{Scope}: we evaluate models up to 8B parameters across 6 architecture families, English text only (C4, Wikipedia, arXiv), and prompt-chain generation; retrain-chain dynamics may yield different boundaries.
70	(2)~\emph{Feature set}: the 15 statistical features provide a lower bound on $\Ktheory$; richer representations (e.g., neural probes) can extend $\Kempirical$ by one additional depth for some architectures.
71	(3)~\emph{Threshold sensitivity}: $\Kempirical$ varies with the decision threshold $\theta$, ranging from 2--3 at $\theta{=}0.55$ to 1 at $\theta{=}0.70$; two of ten configurations are marginal at our reference $\theta{=}0.60$.
72	
73	% === Ethics Statement (ACL required, unnumbered) ===
74	\section*{Ethics Statement}
75	
76	Generational depth estimation is intended for data curation and corpus auditing, positive-sum applications that improve training data quality.
77	Our experiments use the publicly available C4 corpus and do not involve personally identifiable information.
78	A potential dual-use concern is that depth estimation techniques could inform adversarial strategies to evade detection (e.g., by calibrating rewriting to mimic earlier-generation statistics); we note that this risk is shared by all detection research and that the binary detection boundary ($\auc \geq 0.96$ at 0v1) remains robust.
79	Code and data will be released upon acceptance.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_consistency_check_20260523T002253",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-23T00:25:56.256981+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex",
  "offset": "30",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_consistency_check_20260523T002253",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex",
    "offset": "30",
    "limit": "15"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-23T00:25:56.257119+00:00_

30	The poor transfer from rewrite-mode classifiers (61--63\%) isolates generation mode, rather than architecture family, as the primary axis of distributional variation.
31	
32	\paragraph{Prompt-chain scope and retrain-chain gap.}
33	Retrain-chain experiments (Pythia-1.4B LoRA) yield $\Kempirical{\geq}4$ (1v2 $\auc = 0.9484$, 3v4 $= 0.7982$), far exceeding the prompt-chain boundary of $\Kempirical{=}2$, because each retrain generation also modifies model parameters, introducing cumulative adaptation artifacts absent from text-only recycling.
34	Prompt-chain $\Kempirical$ isolates text-intrinsic degradation, the operationally relevant quantity for data curation pipelines; our conclusions do not directly transfer to retrain-chain (model collapse) settings.
35	
36	\paragraph{Boundary cases and scale effect.}
37	$\Kempirical{=}1$ configurations cluster at 1v2 $\auc$ 0.508--0.598, well separated from the $\Kempirical{=}2$ range (0.611--0.696); $\Kempirical{=}1$ is not a classifier failure but a text property, as these models produce first-generation output so human-like that statistical features cannot distinguish depth~1 from depth~2.
38	That $\Kempirical \in \{1, 2\}$ for all web text configurations is the core empirical result; larger models reduce 0v1 JSD (0.077 at 8B vs.\ 0.15--0.27 at $\leq$1.5B), suggesting 13B+ may increasingly yield $\Kempirical{=}1$.
39	The $\Kempirical{=}1$ vs.\ $\Kempirical{=}2$ distinction has a direct curation consequence: $\Kempirical{=}1$ generators erase depth signal in one pass, leaving only the binary 0v1 boundary available for filtering.
40	
41	\paragraph{Decoding strategy as confound.}
42	Greedy decoding inflates depth separability: Pythia-6.9B yields $\Kempirical{=}2$ under greedy but $\Kempirical{=}1$ under nucleus sampling ($p{=}0.95$), with the borderline 1v2 score (2 of 5 folds above $\theta$) illustrating that the boundary is continuous rather than a cliff (Table~\ref{tab:s10_pythia_decoding}).
43	Practitioners should calibrate
…[truncated 85 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_consistency_check_20260523T002253",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-23T00:25:56.257266+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_consistency_check_20260523T002253",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-23T00:25:56.257402+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We measure a lower bound on the generational depth discrimination boundary $\Kempirical$ for prompt-chain recursive synthetic text.
5	For general web text, $\Kempirical \leq 2$ regardless of model family or scale (six architecture families, 1B--8B, $\theta{=}0.60$); across all ten configurations, $\Kempirical \leq 3$, with structured academic text (arXiv) reaching $\Kempirical{=}3$ across two independent architectures.
6	This one-wash laundering effect concentrates all exploitable signal at the 0v1 boundary, and the consistency check confirms that binary curation most effectively minimizes MMLU degradation ($-$0.77\,pp vs.\ $-$1.53\,pp for no-filter).
7	For structured domains where $\Kempirical{=}3$, graduated strategies can exploit one additional depth level, so corpus curators should calibrate filtering to the source domain.
8	The 15 statistical features enable deployment across generators without retraining (80--92\% accuracy retention, $\rho > 0.90$), supporting model-agnostic depth estimation for corpora where the generating model is unknown.
9	Under Bonferroni correction for 10 simultaneous comparisons, three of six $\Kempirical{=}2$ configurations retain significance at the 99.5\% level; the remaining three marginal cases preserve point estimates above $\theta$.
10	$\Kempirical$ converts a continuous AUC decay surface into a discrete operating boundary grounded in the Data Processing Inequality, providing a principled basis for curation decisions that replaces heuristic assumptions about synthetic text recyclability.
11	Several directions remain open: tracking $\Kempirical$ as model scale surpasses 13B, where our scale analysis suggests the boundary may shift toward $\Kempirical{=}1$; bridging the prompt-chain and retrain-chain boundaries, given the substantially higher $\Kempirical{\geq}4$ observed under parameter retraining; and extending depth estimation to additional structured domains and multilingual 
…[truncated 9 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_consistency_check_20260523T002253",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-23T00:25:56.257566+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex",
  "offset": "30",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_consistency_check_20260523T002253",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex",
    "offset": "30",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-23T00:25:56.257721+00:00_

30	\begin{document}
31	\maketitle
32	
33	% === Abstract ===
34	\begin{abstract}
35	Web-scale corpora are increasingly contaminated by recursive synthetic content, yet no method estimates a document's generational depth.
36	We measure a lower bound on the generational discrimination boundary, $\Kempirical$ (the maximum depth at which adjacent generations remain distinguishable), using 15 statistical features and an OBD-LightGBM classifier.
37	Under prompt-chain generation across 10 model configurations (6 architecture families, 1B--8B), 3 source domains, and 4 decoding strategies, for web text (C4, Wikipedia), $\Kempirical \leq 2$ regardless of model family or scale ($\theta{=}0.60$); across all ten configurations, $\Kempirical \leq 3$, with structured academic text (arXiv) reaching $\Kempirical{=}3$ across two architectures.
38	Among the six nominal $\Kempirical{=}2$ configurations, three retain significance under Bonferroni correction; the three marginal cases reflect narrow effect sizes rather than classification failure.
39	A single generation pass suffices to render general web text indistinguishable from deeper synthetic content, a \emph{one-wash laundering} effect.
40	Model-free statistical features enable 80--100\% cross-model transfer with scorer-invariant feature rankings ($\rho > 0.90$), supporting depth estimation on corpora from unknown generators without retraining.
41	As a consistency check, domain-appropriate $\Kempirical$ correctly predicts that binary filtering outperforms graduated alternatives for web text when contamination causes detectable quality loss.
42	\end{abstract}
43	
44	% === Section 1: Introduction ===
45	\input{introduction}
46	
47	% === Section 2: Related Work ===
48	\input{related_work}
49	
50	% === Section 3: Method ===
51	\input{method}
52	
53	% === Section 4: Experiments ===
54	\input{experiments_c1}
55	
56	% === Section 5: K*-Aware Data Filtering ===
57	\input{experiments_c3}
58	
59	% === Section 6: Discussion ===

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_consistency_check_20260523T002253",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-23T00:25:56.257893+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "three of six",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "output_mode": "content",
  "-n": "True",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_consistency_check_20260523T002253",
  "tool": "Grep",
  "tool_args": {
    "pattern": "three of six",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
    "output_mode": "content",
    "-n": "True",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-23T00:25:56.258024+00:00_

docs/paper/conclusion.tex:9:Under Bonferroni correction for 10 simultaneous comparisons, three of six $\Kempirical{=}2$ configurations retain significance at the 99.5\% level; the remaining three marginal cases preserve point estimates above $\theta$.
docs/paper/experiments_c1.tex:45:[Omitted long matching line]
docs/paper/experiments_c1.tex:46:Under Bonferroni correction for 10 simultaneous comparisons (99.5\% CIs), three of six boundary configurations retain CI lower bounds above $\theta$; the three most marginal cases, Pythia-1.4B (0.593), Qwen-continuation (0.598), and LLaMA-8B (0.599), fall below the widened interval.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_consistency_check_20260523T002253",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-23T00:25:56.258147+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
  "offset": "145",
  "limit": "35"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_consistency_check_20260523T002253",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
    "offset": "145",
    "limit": "35"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-23T00:25:56.258289+00:00_

145	\bottomrule
146	\multicolumn{6}{l}{\footnotesize $^\dagger$2v3 $\auc = 0.6067$; fold 5 $= 0.595 < \theta$. Marginal boundary.}
147	\end{tabular}}
148	\end{table}
149	
150	\subsection{Bonferroni-Corrected Confidence Intervals}
151	\label{sec:bonferroni_ci}
152	
153	To control the family-wise error rate across all 10 model configurations, we apply Bonferroni correction: $\alpha_{\text{corr}} = 0.05 / 10 = 0.005$, yielding 99.5\% confidence intervals ($z = 2.807$).
154	Table~\ref{tab:bonferroni_ci} reports the corrected intervals for each configuration's $\Kempirical$ boundary pair.
155	Seven of ten configurations retain CI lower bounds above $\theta{=}0.60$; three marginal $\Kempirical{=}2$ configurations (Pythia-1.4B, Qwen-cont, LLaMA-8B) see their lower bounds dip below $\theta$ under the stricter criterion ($0.5934$, $0.5976$, and $0.5988$, respectively).
156	These near-misses reflect narrow effect sizes ($\auc - \theta < 0.013$) rather than classification failure: all three retain point estimates above $\theta$, and Qwen-cont and LLaMA-8B retain uncorrected 95\% CI lower bounds above $\theta$ (Pythia-1.4B falls marginally below at $0.5976$).
157	
158	\begin{table}[h]
159	\centering
160	\footnotesize
161	\caption{Bonferroni-corrected 99.5\% confidence intervals for $\Kempirical$ boundary pairs across all 10 configurations. $\alpha_{\text{corr}} = 0.005$; CI computed as $\auc \pm 2.807 \times \hat{\sigma}_{\text{boot}}$. ``Pass $\theta$'': CI lower bound $> 0.60$.}
162	\label{tab:bonferroni_ci}
163	\resizebox{\columnwidth}{!}{%
164	\begin{tabular}{llcccc}
165	\toprule
166	\textbf{Configuration} & \textbf{Boundary} & $\auc$ & $\hat{\sigma}_{\text{boot}}$ & \textbf{99.5\% CI} & \textbf{Pass $\theta$} \\
167	\midrule
168	\multicolumn{6}{l}{\textit{$\Kempirical = 2$ configurations}} \\
169	Qwen-rw (Instruct)       & 1v2 & .6955 & .0046 & $[.683,\,.708]$ & \checkmark \\
170	Pythia-1.4B               & 1v2 & .6074 & .0050 & $[.593,\,.621]$ & $\times$ \\
171	Qwen-base 
…[truncated 674 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_consistency_check_20260523T002253",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-23T00:25:56.258490+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "---",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "output_mode": "content",
  "-n": "True",
  "glob": "*.tex",
  "head_limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_consistency_check_20260523T002253",
  "tool": "Grep",
  "tool_args": {
    "pattern": "---",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
    "output_mode": "content",
    "-n": "True",
    "glob": "*.tex",
    "head_limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-23T00:25:56.258628+00:00_

docs/paper/tables/tab_domain_model_kstar_full.tex:12:Qwen2.5       & 1.5B & \textbf{2} & 0.6262~(1v2) & \textbf{3} & 0.6427~(2v3) & \textbf{1}\textsuperscript{$\dagger$} & ---\textsuperscript{$\S$} \\
docs/paper/tables/tab_domain_model_kstar_full.tex:17:OLMo          & 1B   & 1 & 0.500~(1v2) & 1\textsuperscript{$*$} & --- & \textbf{1} & 0.993~(0v1) \\
docs/paper/tables/tab_crossscorer.tex:6:% --- Qwen-RW block ---
docs/paper/tables/tab_crossscorer.tex:7:Qwen-1.5B (self) & Qwen-RW & 2 & --- & 0.6955 & --- \\
docs/paper/tables/tab_crossscorer.tex:11:% --- Qwen-cont block ---
docs/paper/tables/tab_crossscorer.tex:12:Qwen-1.5B (self) & Qwen-cont & 2 & --- & 0.6112 & --- \\
docs/paper/tables/tab_crossscorer.tex:16:% --- Qwen-7B cross-scale block ---
docs/paper/tables/tab_crossscorer.tex:17:Qwen-1.5B        & Qwen-7B-cont & 2 & 0.9644 & 0.6178 & --- \\

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_consistency_check_20260523T002253",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-23T00:25:56.258757+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0\\.508[^0-9]",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "output_mode": "content",
  "-n": "True",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_consistency_check_20260523T002253",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0\\.508[^0-9]",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
    "output_mode": "content",
    "-n": "True",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-23T00:25:56.258900+00:00_

docs/paper/discussion.tex:37:$\Kempirical{=}1$ configurations cluster at 1v2 $\auc$ 0.508--0.598, well separated from the $\Kempirical{=}2$ range (0.611--0.696); $\Kempirical{=}1$ is not a classifier failure but a text property, as these models produce first-generation output so human-like that statistical features cannot distinguish depth~1 from depth~2.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_consistency_check_20260523T002253",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-23T00:25:56.259121+00:00_

检查完毕。逐项报告如下：

---

## 检查结果

### 1. "three of six" Bonferroni pass — PASS

- `experiments_c1.tex:46` — "three of six boundary configurations" ✓
- `conclusion.tex:9` — "three of six $\Kempirical{=}2$ configurations" ✓
- `main.tex:38` (abstract) — 等价表述 "Among the six nominal...three retain significance" ✓
- `appendix_extended.tex:155` — 补充描述 "three marginal K*=2 configurations" ✓
- 无 "four of six" 残留 ✓

### 2. Pythia 1v2 AUC = 0.6074 — FAIL

正确值已出现在 experiments_c1.tex:26, tab_domain_model_kstar_full.tex:14, appendix_extended.tex:170, appendix_extended.tex:196。

**旧值 .6539 残留：**

| 文件 | 行 | 当前值 | 应改为 |
|------|-----|--------|--------|
| `appendix.tex` | 139 | `.6539 & [.645,\,.663]\rlap{$^*$}` | `.6074 & [.598,\,.617]\rlap{$^*$}` |
| `appendix.tex` | 343 | `$.654\;[.645,.663]$` | `$.607\;[.598,.617]$` |

### 3. OLMo 1v2 AUC = 0.500/0.5001 — FAIL

正确值已出现在 experiments_c1.tex:26, tab_domain_model_kstar_full.tex:17, appendix_extended.tex:201。

**旧值 .5080/.508 残留：**

| 文件 | 行 | 当前值 | 应改为 |
|------|-----|--------|--------|
| `appendix.tex` | 139 | `.5080` | `.5001` |
| `appendix.tex` | 343 | `$.508\;[.496,.519]$` | `$.500\;[.496,.519]$` |
| `discussion.tex` | 37 | `0.508--0.598` | `0.500--0.598` |

### 4. OLMo K* = 1 — PASS

- `tab_domain_model_kstar.tex:15` — OLMo 1B, K*=1 ✓
- `tab_domain_model_kstar_full.tex:17` — OLMo 1B, K*=1 ✓
- 正文所有引用一致 ✓

### 5. K* 分布描述 (6/10 K*=2, 4/10 K*=1) — PASS

- `experiments_c1.tex:45` — "6/10 configurations yield K*=2 (Qwen ×4, LLaMA-8B, Pythia-1.4B)" ✓
- `discussion.tex:17` — "6/10 configurations K*=2" ✓
- `appendix.tex:129` — "K*=2 holds for 6/10 conditions...OLMo-1B, Mistral-7B, Pythia-6.9B, Gemma-2-2B: K*=1" ✓
- Abstract/conclusion 用等价表述，一致 ✓

### 6. 破折号检查 — PASS

- Unicode em dash (—) 仅出现在注释行 `main.tex:1`（非正文）
- 无 Unicode en dash (–)
- LaTeX `---` 仅用于表格占位符（"not available"）
- LaTeX `--` 仅用于数值范围（标准用法）

---

## 总结

**3 处 FAIL，均在 appendix.tex 和 discussion.tex，涉及 D107 scorer 修正后的旧值残留：**

1. `appendix.tex:139` — Pythia .6539→.6074（含CI），OLMo .5080→.5001
2. `appendix.tex:343` — Pythia .654→.607（含CI），OLMo .508→.500
3. `discussion.tex:37` — OLMo 范围起始值 0.508→0.500

需要修正这 5 个数值点。是否现在修正？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_consistency_check_20260523T002253"
}
```

</details>

---
