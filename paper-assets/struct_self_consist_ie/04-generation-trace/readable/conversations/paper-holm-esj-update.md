# paper holm esj update

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 87
- **Recorded user turns:** 0
- **Tool calls:** 44
- **Original source:** `logs/chats/worker_paper_holm-esj-update_20260522T185603.jsonl`
- **Structured JSON:** [`36f0a0feacfa17b3e595.json`](../../sessions/36/36f0a0feacfa17b3e595.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

87 recorded events

### Tool call

_source line 1 · 2026-05-22T19:04:08.793962+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper/",
  "description": "List paper directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper/",
    "description": "List paper directory"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-22T19:04:08.794360+00:00_

sections

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T19:04:08.794535+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0\\.055|Holm|Bonferroni|three seeds|3 seeds|three random|3 random",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper/",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0\\.055|Holm|Bonferroni|three seeds|3 seeds|three random|3 random",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper/",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-22T19:04:08.794672+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T19:04:08.794794+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper/ -name \"*.tex\" -type f",
  "description": "Find all tex files in paper directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper/ -name \"*.tex\" -type f",
    "description": "Find all tex files in paper directory"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-22T19:04:08.794914+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper/sections/zeroshot_scaling_draft.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T19:04:08.795047+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper/sections/zeroshot_scaling_draft.tex",
  "description": "Check file length"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper/sections/zeroshot_scaling_draft.tex",
    "description": "Check file length"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-22T19:04:08.795185+00:00_

64 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper/sections/zeroshot_scaling_draft.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T19:04:08.795309+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0\\.055|Holm|Bonferroni|three seeds|3 seeds|five seeds|5 seeds",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper/sections/zeroshot_scaling_draft.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0\\.055|Holm|Bonferroni|three seeds|3 seeds|five seeds|5 seeds",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper/sections/zeroshot_scaling_draft.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-22T19:04:08.795425+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T19:04:08.795537+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\input|\\\\include",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper/sections/zeroshot_scaling_draft.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\input|\\\\include",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper/sections/zeroshot_scaling_draft.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-22T19:04:08.795651+00:00_

57:% \includegraphics[width=\columnwidth]{figures/fig_scaling_curve.pdf}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-22T19:04:08.795779+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/ -name \"*.tex\" -type f 2>/dev/null | head -50",
  "description": "Find all tex files in project"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/ -name \"*.tex\" -type f 2>/dev/null | head -50",
    "description": "Find all tex files in project"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-22T19:04:08.795935+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments_main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/background.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/adaptive.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/single_signal.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/_archived/experiments_OLD.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/diagnostic.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/theory.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/mechanistic.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-researc
…[truncated 4227 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-22T19:04:08.796109+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0\\.055|Holm|Bonferroni|three seeds|3 seeds|five seeds|5 seeds|three random seeds|p_\\{adj\\}|p_\\{\\\\mathrm\\{adj\\}\\}|padj",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0\\.055|Holm|Bonferroni|three seeds|3 seeds|five seeds|5 seeds|three random seeds|p_\\{adj\\}|p_\\{\\\\mathrm\\{adj\\}\\}|padj",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-22T19:04:08.796364+00:00_

docs/paper/main.bbl:177:\bibitem[{Holm(1979)}]{holm1979simple}
docs/paper/main.bbl:178:Sture Holm. 1979.
docs/paper/main.log:689:/it/10.95 :\OT1/cmr/m/n/10.95 001$\T1/ptm/m/n/10.95 (+20) ; Holm $\OML/cmm/m/it
docs/paper/main.log:916:\T1/ptm/m/n/10.95 (+20) all three seeds; EM--FK is seed-dependent
docs/paper/sections/mechanistic.tex:21:A logistic regression on mean-pooled final-layer hidden states at entity spans achieves AUROC $0.636$ (Few-NERD), $0.882$ (CoNLL), $0.630$ (SciERC), evaluated with GroupKFold CV (5-fold ${\times}$ 3 seeds, groups${=}$source instance to prevent entity-level leakage; Appendix~\ref{app:hidden_probe}).
docs/paper/sections/checklist.tex:54:Yes. We report multi-seed results (3 seeds; $\sigma$ in Table~\ref{tab:multiseed}), bootstrap 95\% confidence intervals (Tables~\ref{tab:selection}, \ref{tab:fewnerd_full}), paired bootstrap $p$-values throughout, and minimum detectable effect sizes (Section~\ref{sec:selection_gap}). Tables clearly indicate whether values are single-seed, multi-seed means, or confidence intervals.
docs/paper/sections/_archived/experiments_OLD.tex:226:\caption{Entity construction vs.\ greedy ($\Delta$ macro F1; $N{=}8$, $T{=}1.0$, Qwen3-8B, multi-seed mean${\pm}\sigma$). $\theta{=}2/N$. $p$: paired bootstrap vs.\ greedy. Best in \textbf{bold}. $^\dagger$Survives Holm--Bonferroni correction ($k{=}57$). $^\ddagger$LP-weighted not computed; uniform only.}
docs/paper/sections/_archived/experiments_OLD.tex:244:LP-weighted construction improves on Few-NERD ($+1.40{\pm}0.51$\,pp, $p{<}0.001$; survives Holm--Bonferroni at $k{=}57$) and SciERC ($+1.02{\pm}0.49$\,pp, $p{=}0.004$, $p_{\text{adj}}{=}0.20$; Table~\ref{tab:entity_construction}), recovering 8--11\% of oracle headroom. CoNLL shows no gain ($-0.39$\,pp), consistent with high degeneracy ($N$-scaling in Appendix~\ref{app:n_scaling}).
docs/paper/sections/limitations.tex:2:Our framework is diagnostic, not causal: stages resist decomposition into independent effects ($R^2{<}0$
…[truncated 15783 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-22T19:04:08.796521+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0\\.356|0\\.151|0\\.205|rho.*SJ|rho.*advantage|rho.*LP",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0\\.356|0\\.151|0\\.205|rho.*SJ|rho.*advantage|rho.*LP",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-22T19:04:08.796714+00:00_

&lt;persisted-output>
Output too large (26.2KB). Full output saved to: /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/2faaa201-9cab-42e9-b4b5-06bca79a3a81/tool-results/toolu_013StrasSS73G273iBhHMpVC.txt

Preview (first 2KB):
docs/paper/sections/_archived/experiments_OLD.tex:46:On SciERC (medium difficulty), structural signals lead (VC $\rho{=}0.379$, SJ $0.360$) over LP ($0.205$); bootstrap CIs confirm the gap ($\Delta\rho{=}{+}0.155$; Appendix~\ref{app:bootstrap_signal}).
docs/paper/sections/_archived/experiments_OLD.tex:48:At the signal-collapse boundary (WNUT-17, macro F1${\approx}$42\%), full-set correlations are dominated by the zero/non-zero boundary (VC $\rho{=}0.724$ at $N{=}16$, but conditional $\rho{=}0.038$; Table~\ref{tab:wnut}); LP shows the reverse (conditional $\rho{=}0.350$; Figure~\ref{fig:signal_heatmap}).
docs/paper/sections/_archived/experiments_OLD.tex:58:Cross-instance $\rho$ (Table~\ref{tab:quality_estimation}) is attenuated by varying instance difficulty; within-instance $\rho$ directly measures whether LP discriminates candidates for a fixed input, making it the relevant predictor of selection success.
docs/paper/sections/_archived/experiments_OLD.tex:118:Dataset & $n$ & Greedy & Degen.\% & LP $\rho$ & LP $\Delta$ & $p$ \\
docs/paper/sections/_archived/experiments_OLD.tex:131:Across 23 configurations, degeneracy does not predict LP gain ($\rho{=}0.052$, $p{=}0.81$; Figure~\ref{fig:degeneracy_scatter}), though it causally modulates LP within fixed settings ($\rho{=}{-}0.881$; Appendix~\ref{app:per_type_lp}). Cross-dataset prediction requires LP signal quality (Appendix~\ref{app:conditional_decomp}).
docs/paper/sections/_archived/experiments_OLD.tex:136:\caption{Instance degeneracy vs.\ LP selection gain across 23 configurations ($N{=}8$; $\rho{=}0.052$, $p{=}0.81$). Within Few-NERD per-entity-type analysis ($\rho{=}{-}0.881$; Appendix~\ref{app:per_type_lp}), degeneracy pred
…[truncated 70 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-22T19:04:08.796855+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "entailment|self-verif|self-judg|ESJ|AUROC",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Grep",
  "tool_args": {
    "pattern": "entailment|self-verif|self-judg|ESJ|AUROC",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-22T19:04:08.797053+00:00_

docs/paper/main.log:974: []\T1/ptm/b/n/10.95 (+20) Entity Self-Judgment (ESJ).[] \T1/ptm/m/n/10.95 (+20
docs/paper/sections/related_work.tex:16:Semantic uncertainty \cite{kuhn2023semantic} and confidence estimation \cite{geng2024confidence, xia2025survey} provide complementary model-internal alternatives; our QE signals with AUROC up to 0.82 connect to selective prediction \cite{geifman2017selective} and support abstention independent of sample selection.
docs/paper/main.aux:293:\@writefile{lot}{\contentsline {table}{\numberline {2}{\ignorespaces Summary of 9 method categories tested (including MV baseline, LP selection, and cross-model ensemble beyond self-verification methods in Appendix~\ref {sec:mechanistic} and adaptive methods in this section). $\Delta $F1 vs.\ greedy; dataset in parentheses. Full coverage in Appendix~\ref {app:method_coverage}.}}{4}{table.caption.12}\protected@file@percent }
docs/paper/main.aux:294:\newlabel{tab:method_summary}{{2}{4}{Summary of 9 method categories tested (including MV baseline, LP selection, and cross-model ensemble beyond self-verification methods in Appendix~\ref {sec:mechanistic} and adaptive methods in this section). $\Delta $F1 vs.\ greedy; dataset in parentheses. Full coverage in Appendix~\ref {app:method_coverage}}{table.caption.12}{}}
docs/paper/main.aux:532:\@writefile{lot}{\contentsline {table}{\numberline {3}{\ignorespaces NER quality estimation ($\rho $ and AUROC; $N{=}8$, primary seed${=}42$; 3-seed $\sigma {\leq }0.026$ in Table~\ref {tab:multiseed}). AUROC binarizes at per-dataset median F1. Best in \textbf  {bold}. RE in Appendix~\ref {app:re_extension}; $N{=}16$ in Table~\ref {tab:robustness}.}}{7}{table.caption.18}\protected@file@percent }
docs/paper/main.aux:533:\newlabel{tab:quality_estimation}{{3}{7}{NER quality estimation ($\rho $ and AUROC; $N{=}8$, primary seed${=}42$; 3-seed $\sigma {\leq }0.026$ in Table~\ref {tab:multiseed}). AUROC binarizes at per-dataset median F1. Best in \textbf {bold}. RE in A
…[truncated 15660 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-22T19:04:08.797279+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-22T19:04:08.797446+00:00_

1	\begin{abstract}
2	Test-time compute scaling---repeated sampling with self-consistency or best-of-$N$---yields large gains on discrete-answer reasoning, but whether these gains transfer to NER remains open.
3	We characterize when scaling succeeds and fails, using NER (four datasets, primarily 7--14B fine-tuned) as the primary case study with preliminary RE and SQL pilots.
4	Quality estimation signals predict output quality (AUROC up to $0.82$), yet instance-level selection yields ${<}1$\,pp, revealing a \textbf{correlation-selection gap}.
5	A diagnostic framework identifies two co-occurring conditions---\textit{degeneracy} (i.e., multiple outputs collapsing to identical predictions) and signal alignment collapse---that jointly determine scaling returns; cross-task exploration confirms task-specific failure modes.
6	Entity-level construction provides suggestive evidence of conditional gains ($+1.40$\,pp on Few-NERD, 3-epoch; Holm $p_{\text{adj}}{=}0.055$; diminishes at convergence) but exhibits inverse scaling in most configurations (69\% of $N$-transitions), underscoring the framework's diagnostic value over prescriptive remedy.
7	The framework is diagnostic rather than predictive, informing resource allocation decisions before investing in repeated inference.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-22T19:04:08.797580+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-22T19:04:08.797753+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Test-time compute scaling---self-consistency \cite{wang2023selfconsistency}, best-of-$N$ \cite{snell2025scaling, brown2024monkeys}, extended reasoning \cite{muennighoff2025s1}---yields large gains on discrete-answer tasks where outputs admit equivalence classes or execution-based verification.
4	For NER, where outputs are entity sets with partial overlap, the boundary conditions for effective scaling are unknown; prior work \cite{yao2026consistency, yun2025price} provides initial observations but no systematic diagnostic framework quantifying failure mechanisms at entity level across multiple model families.
5	While \citet{yao2026consistency} demonstrate that scaling returns plateau at the task level, our contribution operates at a different granularity: instance-level diagnostic decomposition revealing \emph{why} specific instances resist scaling (degeneracy $+$ LP compression), with actionable per-instance signals.
6	
7	Using NER (four datasets, primarily 7--14B fine-tuned; tentative cross-scale observations to 72B) and RE as case studies, we identify a \textbf{correlation-selection gap}: quality estimation signals predict output quality ($\rho$ up to $0.45$, AUROC $0.82$; Table~\ref{tab:quality_estimation}), yet selection fails---MV gains ${<}1$\,pp even at $N{=}64$ (Figure~\ref{fig:n_scaling}; Table~\ref{tab:selection}).
8	This gap decomposes into a definitional layer---four instance-level signals assign identical scores to all candidates---and an empirical one: LP, the only per-sample signal, also fails through within-instance compression (\S\ref{sec:selection_gap}).
9	A hidden-state probe confirms models encode entity quality internally (AUROC $0.63$\textendash$0.88$; Appendix~\ref{sec:mechanistic}), exposing an \textit{introspection boundary} \cite{huang2024large}.
10	A \textit{diagnostic framework}---co-occurring conditions that jointly characterize the gap, not a sequential filter---localizes the failure
…[truncated 3500 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-22T19:04:08.797918+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments_main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments_main.tex"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-22T19:04:08.798156+00:00_

1	\section{Experiments}\label{sec:experiments}
2	
3	\subsection{Experimental Setup}\label{sec:setup}
4	
5	\paragraph{Datasets.}
6	We evaluate on four English NER benchmarks spanning a difficulty gradient.
7	\textbf{SciERC} \cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed (${\approx}$65\% F1).
8	\textbf{Few-NERD} \cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\approx}$75\% F1) provides a low-degeneracy contrast where LP selection succeeds (\S\ref{sec:selection_gap}).
9	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\approx}$91\% F1) serves as a ceiling-effect control.
10	\textbf{WNUT-17} \cite{derczynski2017wnut} (1{,}287 social media instances, 53.7\% zero F1) probes the signal-collapse boundary.
11	
12	\paragraph{Models and sampling.}
13	\textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are LoRA fine-tuned using LLaMA Factory \cite{zheng2024llamafactory} (Appendix~\ref{app:training}; Few-NERD uses 3 epochs vs.\ 5 for others; Appendix~\ref{app:epoch_confound}).
14	$N{=}8$ samples at $T{=}1.0$ (primary) with vLLM constrained decoding \cite{willard2023guided}; $N {\in} \{16, 32, 64\}$ for scaling (Figure~\ref{fig:n_scaling}; Appendix~\ref{app:n_scaling}).
15	
16	\begin{figure}[t]
17	\centering
18	\includegraphics[width=\columnwidth]{figures/fig_n_scaling_mv.pdf}
19	\caption{MV $\Delta$F1 vs.\ $\log_2 N$ across three datasets (Qwen3-8B FT, seed${=}42$). Dotted gray: $\Delta{=}0$. Gains are dataset-dependent: persistently negative on Few-NERD, near zero on SciERC at higher $N$, marginally positive on CoNLL ($+0.6$\,pp at $N{=}64$).}
20	\label{fig:n_scaling}
21	\end{figure}
22	
23	%% ============================================================
24	\subsection{Quality Estimation Results}\label{sec:qe_results}
25	
26	\begin{table*}[t]
27	\centering
28	\small
29	\caption{NER quality estimation ($\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 3-seed
…[truncated 8071 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-22T19:04:08.798335+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-22T19:04:08.798472+00:00_

1	Our primary evidence is from NER (four English datasets, 7--14B open-weight fine-tuned); cross-scale observations (4B--72B, GPT-5.5) are tentative. The RE extension ($n{=}397$, single dataset) and SQL pilot ($n{=}196$) are exploratory. SciERC results are validated across three training seeds ($n{=}529$ test instances; $\Delta_{\text{SC}}{=}{-}0.74{\pm}0.46$\,pp, consistent negative). Frontier models exhibit markedly different degeneracy profiles (5.5--74\%; Table~\ref{tab:frontier_sc_cross}), suggesting findings from fine-tuned open-weight models may not fully generalize to proprietary systems.
2	Our framework is diagnostic, not causal: stages resist decomposition into independent effects ($R^2{<}0$; \S\ref{sec:selection_gap}). Under global Holm--Bonferroni ($k{=}57$), the most liberal core claim reaches $p_{\text{HB}}{=}0.055$; under BH FDR, $19/57$ tests are significant at FDR${<}0.05$ including $6/10$ construction comparisons (Appendix~\ref{app:holm}).
3	We evaluate at $N{\in}\{2,\ldots,64\}$; entity-level construction requires $N{\times}$ inference cost for modest gains ($+1$--$1.4$\,pp). We use a single prompt template per task; prompt variations may affect entity recall, degeneracy, and LP distributions.
4	All evaluation uses entity-level micro-F1 with exact span-and-type match; partial-credit metrics (e.g., token-level or relaxed boundary match) may yield different conclusions about selection effectiveness.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-22T19:04:08.798635+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/single_signal.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/single_signal.tex"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-22T19:04:08.798801+00:00_

1	\section{Where Single-Signal Selection Fails}\label{sec:selection_gap}
2	
3	\paragraph{Definitional vs.\ empirical.}
4	We decompose the correlation-selection gap into two layers.
5	The first is structural: four of five signals are instance-level aggregates that assign identical scores to all $N$ candidates from a given input (\S\ref{sec:formulation}), so they estimate quality across inputs but cannot rank candidates within an instance---selection failure is a design property, not an empirical finding.
6	The second layer is empirical and constitutes the core diagnostic: LP---the only per-sample signal---suffers compression under constrained decoding, with 60\% of SciERC instances showing within-instance LP range below 0.041 nats (Appendix~\ref{app:logprob_ties}), effectively eliminating the variation needed for sample discrimination. This compression is model-intrinsic: free-form decoding yields nearly identical LP distributions (within-instance std ratio $0.97{\times}$; Appendix~\ref{app:freeform_ablation}). Even where LP varies, selection gains depend on LP-quality alignment rather than degeneracy alone.
7	Cross-instance $\rho$ (Table~\ref{tab:quality_estimation}) is attenuated by varying instance difficulty; within-instance $\rho$ directly measures whether LP discriminates candidates for a fixed input, making it the relevant predictor of selection success.
8	
9	\begin{table}[t]
10	\centering
11	\small
12	\caption{Best-of-$N$ selection (macro F1) on SciERC ($N{=}8$, $T{=}1.0$). Selection signals: 2-seed mean${\pm}\sigma$; baselines: 3-seed (Oracle${=}0.781$, Greedy${=}0.667$). LP is per-sample; others use consensus-proximity. $^\dagger$One score per input.}
13	\label{tab:selection}
14	\begin{tabular}{lcc}
15	\toprule
16	Method & NER F1 & $p$ \\
17	\midrule
18	Oracle & $0.775 \pm 0.001$ & --- \\
19	Greedy ($T{=}0$) & $0.645 \pm 0.001$ & --- \\
20	\midrule
21	LP           & $\mathbf{0.647} \pm 0.005$ & .29 \\
22	SJ           & $0.646 \pm 0.002$ & .67 \\
23	FK      
…[truncated 3383 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-22T19:04:08.798955+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-22T19:04:08.799094+00:00_

1	\section{Discussion and Conclusion}\label{sec:discussion}\label{sec:selection_method}\label{sec:conclusion}
2	
3	\paragraph{Why test-time scaling fails for NER.}
4	For discrete-answer reasoning, sample diversity reflects diverse reasoning paths; for NER, degeneracy ($12$--$68$\%) eliminates candidate diversity while signal alignment collapse ($\alpha{\to}0$) prevents ranking.
5	The degeneracy decomposition (\S\ref{sec:theory}) identifies $\alpha$---not degeneracy---as the binding constraint ($8$--$33{\times}$ tighter), providing a diagnostic tool for localizing failure rather than a predictive bound.
6	This capability-diversity tradeoff \cite{yun2025price} persists across model families (5.5--74\%; Table~\ref{tab:frontier_sc_cross}), scales (4B--72B; \S\ref{sec:scaling}), and decoding modes (LP std ratio ${\approx}0.97{\times}$; \S\ref{sec:selection_gap}).
7	Compared to \citet{yao2026consistency}'s task-level plateau, we provide instance-level decomposition; \citet{landesberg2026bon} independently confirm the gap generalizes beyond NER ($r{=}0.47$ global vs.\ $r{=}0.27$ within-prompt).
8	
9	\paragraph{Constrained vs.\ free-form decoding.}
10	LP compression is model-intrinsic rather than an artifact of constrained decoding: free-form generation yields nearly identical within-instance LP distributions (std ratio $0.97{\times}$; Appendix~\ref{app:freeform_ablation}).
11	Constrained decoding does affect diversity: Few-NERD (13\% degeneracy) retains diversity under grammar constraints, while CoNLL (62\%) collapses---but this variation tracks task difficulty and model calibration rather than the decoding mechanism itself.
12	
13	\paragraph{Scale and outlook.}
14	The correlation-selection gap persists from 4B fine-tuned to 72B zero-shot and GPT-5.5, with degeneracy varying by model family rather than scale (Qwen2.5: $32$--$46$\%, Qwen3: $13$\%, GPT-5.5: $50$\% on Few-NERD; \S\ref{sec:scaling}).
15	Whether models beyond 70B with improved calibration can overcome signal al
…[truncated 628 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-22T19:04:08.799300+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "310",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "310",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-22T19:04:08.799465+00:00_

310	At $N{=}16$ ($B{=}10{,}000$, permutation test), the structural advantage extends to FK comparisons.
311	On SciERC NER ($n{=}529$), SJ--FK ($\Delta\rho{=}0.147$--$0.160$, all $p{\leq}0.002$) and VC--FK ($\Delta\rho{=}0.138$--$0.188$, all $p{\leq}0.003$) are clearly significant across all three seeds; EM--FK is seed-dependent ($\Delta\rho{=}0.054$--$0.093$, $p{=}0.048$--$0.15$).
312	On CoNLL ($n{=}2{,}756$), all signals significantly outperform FK: EM $\Delta\rho{=}0.071$ ($p{<}0.001$), SJ $\Delta\rho{=}0.056$ ($p{<}0.001$), VC $\Delta\rho{=}0.022$ ($p{=}0.040$).
313	
314	\section{Holm--Bonferroni Enumeration}\label{app:holm}
315	
316	Table~\ref{tab:holm_family} enumerates all $k{=}57$ statistical tests reported in this paper under a single global Holm--Bonferroni correction.
317	Under this most conservative family, no core NER claim survives ($p_{\text{adj}}{=}0.055$ for Few-NERD LP selection and construction); only two peripheral tests reach significance (CoNLL few-shot entity entropy, RE LP selection reversal under free-form decoding).
318	We report per-family corrections in the main text (\S\ref{sec:prescriptive}); the global enumeration is provided here for transparency.
319	
320	\begin{table*}[t]
321	\centering
322	\small
323	\caption{Complete enumeration of $k{=}57$ statistical tests subject to Holm--Bonferroni correction. Raw $p$: uncorrected $p$-value as reported. $p_{\text{adj}}$: Holm--Bonferroni adjusted $p$-value. $^\dagger$Survives correction at $\alpha{=}0.05$.}
324	\label{tab:holm_family}
325	\begin{tabular}{clllcc}
326	\toprule
327	\# & Family & Test Description & Raw $p$ & $p_{\text{adj}}$ & Sig. \\
328	\midrule
329	\multicolumn{6}{l}{\textit{Selection}} \\
330	1 & & SciERC NER LP selection ($N{=}8$, Qwen, Table~3) & $0.290$ & $1.0$ &  \\
331	2 & & SciERC NER SJ selection ($N{=}8$, Qwen, Table~3) & $0.670$ & $1.0$ &  \\
332	3 & & SciERC NER FK selection ($N{=}8$, Qwen, Table~3) & $0.790$ & $1.0$ &  \\
333	4 & & WNUT-17 LP selection ($N{=}8$, Qwen
…[truncated 3943 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-22T19:04:08.799611+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/single_signal.tex",
  "offset": "35",
  "limit": "25"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/single_signal.tex",
    "offset": "35",
    "limit": "25"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-22T19:04:08.799755+00:00_

35	\caption{Correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Bars: QE $\rho$; line: $\Delta$F1 vs.\ greedy (3-seed mean). Despite $\rho$ up to 0.38, no signal outperforms greedy (all $p{\geq}0.29$). Dashed green: oracle headroom ($+11.4$\,pp; oracle headroom $=$ best-of-$N$ F1 $-$ greedy F1); dotted gray: random.}
36	\label{fig:selection_gap}
37	\end{figure}
38	
39	Despite $\rho$ up to 0.38, no signal outperforms greedy on SciERC (Table~\ref{tab:selection}; Figure~\ref{fig:selection_gap}); the oracle shows 11.4\,pp headroom, but LP achieves $+0.2$\,pp ($p{=}0.29$), below MDE (${\approx}$1.5\,pp; $n{=}529$; Table~\ref{tab:power_analysis}).
40	The pattern holds across CoNLL and WNUT-17 (Table~\ref{tab:cross_selection}).
41	Few-NERD provides the definitive contrast: LP achieves $+1.39$\,pp ($p{<}0.001$; Holm $p_{\text{adj}}{=}0.021$, selection family $k{=}21$)\footnote{Under global correction ($k{=}57$), LP-best selection reaches Holm $p_{\text{adj}}{=}0.055$ (BH $p_{\text{adj}}{=}0.003$)---the only positive selection signal approaching significance under the conservative Holm procedure.} at low degeneracy (13.0\% vs.\ 12.2--67.9\%), while structural signals still degrade (VC $-1.79$, SJ $-2.14$\,pp; \S\ref{sec:fewnerd}).
42	
43	\paragraph{Diagnostic framework.}
44	We identify two co-occurring factors that jointly characterize the gap:
45	(1)~instance degeneracy sets the ceiling (SciERC 12.2\%, CoNLL 61.7\%);
46	(2)~oracle headroom bounds the opportunity within non-degenerate instances (CoNLL ${\approx}4$\,pp vs.\ SciERC 11.4\,pp);
47	(3)~LP compression limits exploitation (Few-NERD within-instance $\rho{\approx}0.5$--$0.7$ vs.\ SciERC $\rho{\approx}0.26$).
48	Degeneracy does not predict LP gain across datasets ($\rho{=}0.052$, $n{=}23$, $p{=}0.81$; Figure~\ref{fig:degeneracy_scatter}), though it co-varies with LP within fixed settings ($\rho{=}{-}0.881$; Appendix~\ref{app:per_type_lp}).
49	These conditions interact ($R^2{<}0$); on non-degenerate instances, $\
…[truncated 1037 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-22T19:04:08.799898+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "30",
  "limit": "35"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "30",
    "limit": "35"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-22T19:04:08.800032+00:00_

30	
31	We exclude instances with empty gold annotations from all correlation analyses (CoNLL: 697/3{,}453 instances, 20.2\%; SciERC: 22/551, 4.0\%).
32	For these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality. Including them inflates or deflates Spearman $\rho$ depending on signal behavior at the boundary.
33	
34	\begin{table}[t]
35	\centering
36	\small
37	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\sigma$ computed as sample standard deviation.}
38	\label{tab:robustness}
39	\begin{tabular}{llcc}
40	\toprule
41	& & NER $\rho$ & RE $\rho$ \\
42	\midrule
43	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
44	\quad SJ & $T{=}0.7$ & 0.364 & 0.234 \\
45	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
46	\quad FK & $T{=}0.7$ & 0.289 & 0.184 \\
47	\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\
48	\quad LP & $T{=}0.7$ & 0.249 & --- \\
49	\quad LP & $T{=}1.0$ & 0.205 & 0.266 \\
50	\midrule
51	\multicolumn{4}{l}{\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\
52	\quad SJ & $N{=}8$  & 0.360 & 0.250 \\
53	\quad SJ & $N{=}16$ & 0.411$^\dagger$ & 0.281 \\
54	\quad FK & $N{=}8$  & 0.267 & 0.275 \\
55	\quad FK & $N{=}16$ & 0.283 & 0.279 \\
56	\midrule
57	\multicolumn{4}{l}{\textit{Across model families} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\
58	\quad SJ &  & $0.474{\pm}0.009$ & --- \\
59	\quad FK &  & $0.467{\pm}0.009$ & --- \\
60	\quad EM &  & $0.473{\pm}0.010$ & --- \\
61	\quad VC &  & $0.470{\pm}0.006$ & --- \\
62	\quad LP &  & $0.311{\pm}0.003$ & --- \\
63	\bottomrule
64	\end{tabular}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-22T19:04:08.800313+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "675",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "675",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-22T19:04:08.800488+00:00_

675	The probe consistently exceeds prompt-based self-evaluation (ESJ AUROC${=}0.512$), confirming that hidden states encode partial entity quality signal inaccessible through the prompt interface, consistent with the complexity-dependent introspection boundary diagnosed in the main text (\S\ref{sec:mechanistic}).
676	
677	\section{Multi-Seed Stability}\label{app:multiseed}
678	
679	Table~\ref{tab:multiseed} reports quality estimation metrics across three random seeds for both model families on SciERC ($N{=}8$, $T{=}1.0$).
680	On NER, the signal ranking VC${>}$SJ${>}$EM${>}$FK${>}$LP is identical across all six model-seed combinations, with $\sigma{\leq}0.025$ for all signals (rankings are stable across our 3 seeds, though statistical power with $n{=}3$ is limited).
681	On RE (Qwen only, preliminary), VC remains the top signal ($\rho{=}0.309{\pm}0.024$), but LP rises to \#2 ($\rho{=}0.297{\pm}0.022$), above FK, SJ, and EM. This reversal from the NER ranking reflects RE's higher sensitivity to per-sample scoring.
682	LLaMA absolute values are systematically lower than Qwen on NER, consistent with the directionally-consistent-but-magnitude-dependent characterization in the main text.
683	
684	\begin{table}[t]
685	\centering
686	\small
687	\caption{Multi-seed quality estimation on SciERC ($N{=}8$, $T{=}1.0$, seeds: 42, 123, 456). NER: both models; RE: Qwen only (preliminary). Signal ranking is stable across seeds ($\sigma{\leq}0.025$). $\sigma$ is population standard deviation over 3 seeds.}
688	\label{tab:multiseed}
689	\resizebox{\columnwidth}{!}{
690	\begin{tabular}{lccccc}
691	\toprule
692	& LP & FK & SJ & VC & EM \\
693	\midrule
694	\multicolumn{6}{l}{\textit{NER Spearman $\rho$ (mean $\pm\sigma$)}} \\
695	Qwen & .217${\pm}$.013 & .254${\pm}$.016 & .364${\pm}$.018 & .386${\pm}$.019 & .307${\pm}$.008 \\
696	LLaMA & .162${\pm}$.025 & .256${\pm}$.024 & .325${\pm}$.021 & .384${\pm}$.014 & .279${\pm}$.011 \\
697	\midrule
698	\multicolumn{6}{l}{\textit{RE Spearman $\rho$
…[truncated 1107 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-22T19:04:08.800641+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "385",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "385",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-22T19:04:08.800779+00:00_

385	48 & & SciERC per-type degeneracy--LP ($\rho{=}0.14$) & $0.790$ & $1.0$ &  \\
386	49 & & Kruskal--Wallis per-type LP heterogeneity (SciERC) & $0.796$ & $1.0$ &  \\
387	\addlinespace
388	\multicolumn{6}{l}{\textit{FS error}} \\
389	50 & & FS vs ZS error overlap (SciERC, permutation) & $0.840$ & $1.0$ &  \\
390	51 & & FS vs ZS error overlap (CoNLL, permutation) & $0.640$ & $1.0$ &  \\
391	52 & & FS vs ZS entity entropy (SciERC) & $0.810$ & $1.0$ &  \\
392	53 & & FS vs ZS entity entropy (CoNLL, Wilcoxon) & ${<}10^{-4}$ & ${<}.001$ & $\dagger$ \\
393	\addlinespace
394	\multicolumn{6}{l}{\textit{Other}} \\
395	54 & & LP distribution seed 42 vs 456 (Mann--Whitney) & $0.550$ & $1.0$ &  \\
396	55 & & RE LP selection reversal (free-form, 4-seed) & ${<}.001$ & $0.006$ & $\dagger$ \\
397	56 & & WNUT-17 conditional $\rho$ VC ($p$-value) & $0.487$ & $1.0$ &  \\
398	57 & & WNUT-17 conditional $\rho$ FK ($p$-value) & $0.002$ & $0.094$ &  \\
399	\bottomrule
400	\end{tabular}
401	\end{table*}
402	
403	\section{Diversity and Selection Analysis}\label{app:diversity}
404	
405	% fig_selection_gap promoted to main text (\S\ref{sec:selection_gap})
406	
407	\paragraph{Output diversity quantification.}
408	Table~\ref{tab:diversity} summarizes output diversity across configurations.
409	On SciERC, output diversity is substantial: Qwen produces 43\% unique outputs per instance (mean 3.5 distinct out of $N{=}8$), with per-sample F1 standard deviation of 0.144 and mean pairwise SJ of 0.703.
410	LLaMA shows similar diversity (39\% unique, F1 std 0.11).
411	On CoNLL, diversity collapses: 59\% (Qwen) to 89\% (LLaMA) of instances produce identical outputs across all $N$ samples; this reflects a ceiling effect where single-sample F1 already exceeds 0.90.
412	WNUT-17 shows 55\% identical outputs, attributable to the 53.7\% zero-F1 rate.
413	
414	\begin{table}[t]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-22T19:04:08.800917+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "75",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "75",
    "limit": "15"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-22T19:04:08.801052+00:00_

75	SJ NER $\rho$ shifts from 0.364 ($T{=}0.7$) to 0.360 ($T{=}1.0$), a difference of 0.004.
76	FK NER $\rho$ drops by 0.022, while RE $\rho$ increases by 0.091, likely reflecting reduced diversity at lower temperature interacting differently across tasks.
77	LP exhibits the largest temperature effect on NER ($\rho{=}0.249$ at $T{=}0.7$ vs.\ $0.205$ at $T{=}1.0$, $\Delta{=}{+}0.044$), consistent with lower temperature concentrating probability mass and improving LP's discriminative power for quality estimation; RE $T{=}0.7$ LP data is not available.
78	Across all comparisons, the signal hierarchy is preserved at both temperatures on NER (SJ${>}$FK${>}$LP at $T{=}0.7$: $0.364{>}0.289{>}0.249$; at $T{=}1.0$: $0.360{>}0.267{>}0.205$).
79	
80	\paragraph{Sample size scaling.}
81	Increasing from $N{=}8$ to $N{=}16$ improves SJ on Qwen SciERC NER: $\rho$ rises from 0.360 to $0.411{\pm}0.010$ (three seeds: 0.398, 0.423, 0.410), a gain of $+0.047$.
82	The magnitude of $N$-scaling gains is setting-dependent (LLaMA SciERC NER yields $+0.016$ and Qwen CoNLL NER $+0.014$), though the direction is consistently positive.
83	LLaMA CoNLL exhibits the most uniform scaling: all four consistency signals gain $\Delta\rho{\approx}{+}0.042$ (range: $+0.039$ to $+0.044$) while LP gains only $+0.004$ (Table~\ref{tab:quality_estimation}).
84	FK $N$-scaling is seed-dependent: Qwen SciERC gains range from $+0.005$ to $+0.023$ across seeds (mean $+0.016$), while LLaMA CoNLL yields $+0.039$ (3-seed mean); individual seed FK shifts vary substantially under the unified pipeline, so this should not be interpreted as a robust trend.
85	VC $N$-scaling is consistently positive ($+0.005$ on Qwen CoNLL, $+0.018$ on LLaMA SciERC, $+0.030$ on Qwen SciERC), while LP is approximately $N$-invariant ($\Delta{\leq}0.034$).
86	SJ, EM, and VC scale consistently across all tested settings; only FK shows seed-dependent variation that does not constitute a reliable trend, structural and binary-agreement signals are 
…[truncated 286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-22T19:04:08.801216+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "description": "Check appendix length"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "description": "Check appendix length"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-22T19:04:08.801335+00:00_

2478 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-22T19:04:08.801487+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "2460",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "2460",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-22T19:04:08.801622+00:00_

2460	\item \textit{``...according to UK Royal Air Force Wing Commander and FOD researcher Richard Friend.''} Entity: Richard Friend / person (mean LP${=}{-}0.050$, 8/8). Gold: \{UK Royal Air Force / org, FOD / org\}. Likely annotation gap: Richard Friend is a real person mentioned by name; gold omits it.
2461	
2462	\item \textit{``...the Navy's forces within South Vietnam were operationally controlled by COMUSMACV.''} Entity: COMUSMACV / org (mean LP${=}{-}0.050$, 8/8). Gold: \{Seventh Fleet / org, South Vietnam / location\}. Model confidently extracts a valid entity missing from gold.
2463	\end{itemize}
2464	
2465	\noindent These examples highlight a fundamental limitation: LP signals the model's confidence, not correctness. When the model is correctly confident about entities that gold annotations omit, LP cannot serve as an error detector.
2466	
2467	\paragraph{Consensus-based verification failures (3/3).}
2468	Entity consensus frequency (fraction of $N$ samples containing a given entity) serves as the primary self-verification signal. It fails in both directions.
2469	
2470	\begin{itemize}[nosep,leftmargin=*]
2471	\item \textbf{Overconfident.} \textit{``Les Blank...was an American documentary filmmaker best known for his portraits of American traditional musicians.''} Entity: American / location (8/8 samples, consensus${=}1.0$). Gold: \{Les Blank / person\}. Maximum consensus for non-gold entity.
2472	
2473	\item \textbf{Overconfident.} \textit{``Cramer pitched for the Orange County Flyers of the independent Golden League in 2008.''} Entity: Cramer / person (8/8 samples, consensus${=}1.0$). Gold: \{Orange County Flyers / org, independent Golden League / org\}. Same instance as LP failure above---simultaneous failure of both signals.
2474	
2475	\item \textbf{Underconfident.} \textit{``They finished the season 14--19, 9--9 in C-USA play to finish in seventh place.''} Gold entity: C-USA play / event (consensus${=}0.0$, never predicted in any of 8 samples). Zero con
…[truncated 416 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-22T19:04:08.801767+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "630",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "630",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-22T19:04:08.801912+00:00_

630	Entity quality is partially encoded in hidden representations: a supervised probe (AUROC $0.63$\textendash$0.88$) consistently exceeds self-judgment (ESJ $0.51$) but only marginally exceeds multi-sample agreement ($0.87$) on CoNLL, suggesting consensus captures information beyond single-pass representations while the prompt interface fails to access even partial hidden-state signal.
631	LODO transfer drops to $0.56$\textendash$0.67$, so even direct hidden-state access would not yield a universal quality signal---consistent with the negative cross-dataset verifier transfer (\S\ref{sec:verifier}).
632	
633	\section{Entity-Level Self-Verification Probes}\label{app:self_verification}
634	
635	Three independent probes test whether the generating model can self-verify at the entity level, using Qwen2.5-7B fine-tuned on Few-NERD ($N{=}8$, seed 42).
636	
637	\begin{table}[t]
638	\centering
639	\small
640	\caption{Entity-level self-verification probes (Qwen2.5-7B, Few-NERD, $N{=}8$). ESJ: entity self-judgment via yes/no prompts. MRSC: multi-round re-prompting on disputed entities. LSC: latent-space centroid selection. MV: majority vote baseline.}
641	\label{tab:self_verification}
642	\begin{tabular}{@{}lcc@{}}
643	\toprule
644	Method & Key Metric & F1 \\
645	\midrule
646	Greedy ($T{=}0$) & --- & .794 \\
647	MV ($\theta{=}0.375$) & --- & .792 \\
648	Oracle & --- & .882 \\
649	\midrule
650	ESJ (best $\theta{=}0.02$) & AUROC${=}0.512$ & .711 \\
651	MRSC (best $\theta{=}0.5$) & $\Delta P(\text{yes}){=}0.001$ & .763 \\
652	LSC (centroid) & $\rho_{\text{LP-latent}}{=}0.52$ & .759 \\
653	LSC (entity conf.) & --- & .839 \\
654	\midrule
655	Freq.\ agreement & AUROC${=}0.868$ & --- \\
656	\bottomrule
657	\end{tabular}
658	\end{table}
659	
660	\paragraph{Entity Self-Judgment (ESJ).}
661	For each extracted entity, we prompt the model: ``Is [entity] a [type] entity in this sentence?''
662	The entity-level AUROC is $0.512$---indistinguishable from chance---with P(yes$|$correct)${=}0.5
…[truncated 1753 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-22T19:04:08.802070+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "258",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "258",
    "limit": "15"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-22T19:04:08.802229+00:00_

258	For quality estimation, structural signals benefit consistently but sublinearly: SJ $\rho$ improves by $+0.047$ (Qwen SciERC, 3-seed mean) and $+0.032$ (LLaMA CoNLL, 3-seed mean) when doubling from $N{=}8$ to $N{=}16$, while log-probability is approximately $N$-invariant ($\Delta\rho{\leq}0.021$).
259	Structural signals use $\binom{N}{2}$ pairwise comparisons (28 pairs at $N{=}8$, 120 at $N{=}16$), but the $\rho$ improvement is far less than proportional, each additional comparison yields diminishing information.
260	This asymmetry gives structural signals a relative advantage in the compute-constrained regime: at $N{=}8$, SJ already achieves $\rho{=}0.431$ on LLaMA CoNLL (vs.\ LP $\rho{=}0.307$, $\Delta{=}{+}0.124$), and the gap \textit{widens} at $N{=}16$ ($\Delta{=}{+}0.163$) because structural signals continue to benefit from additional pairwise evidence while LP does not.
261	For sample selection, additional samples increase the oracle upper bound (more draws raise the probability of a high-quality candidate), but signal-based selection remains flat because the selector's inability to identify the best candidate is a granularity limitation, not a sample size limitation.
262	The practical implication is that $N{=}8$ captures most of the achievable quality estimation benefit; further scaling widens rather than closes the correlation-selection gap absent stronger per-sample selectors.
263	
264	\paragraph{$N{=}16$ CoNLL selection: small but significant.}
265	While quality estimation benefits sublinearly from $N$-scaling, selection behavior at $N{=}16$ shows a nuanced exception on LLaMA CoNLL.
266	VC achieves the largest gain over single-sample ($+0.28$~pp, $p{=}0.003$--$0.027$ across 3 seeds, all significant), with SJ, FK, and EM at $+0.22$--$0.23$~pp and LP at $+0.12$~pp (2/3 seeds significant).
267	These gains are statistically significant but practically minimal: oracle headroom at $N{=}16$ is only 2.5~pp, so VC captures approximately 10\% of the available h
…[truncated 541 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-22T19:04:08.802370+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "2180",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "2180",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-22T19:04:08.802501+00:00_

2180	
2181	On degenerate subsets (instances where all $N$ samples yield identical F1), merge is uniformly negative across all three datasets, confirming that entity-level aggregation cannot bypass the diversity bottleneck identified in the main text (\S\ref{sec:discussion}).
2182	
2183	\subsection{Entity Construction Results}\label{app:entity_construction_table}
2184	
2185	\begin{table}[h]
2186	\centering
2187	\small
2188	\caption{Entity construction vs.\ greedy ($\Delta$ macro F1; $N{=}8$, $T{=}1.0$, Qwen3-8B, multi-seed mean${\pm}\sigma$). $\theta{=}2/N$. $p$: paired bootstrap vs.\ greedy. $^\dagger$Survives per-family Holm--Bonferroni correction (construction, $k{=}10$); global correction ($k{=}57$) yields $p_{\text{adj}}{=}0.055$ (Appendix~\ref{app:holm}). $^\ddagger$LP-weighted not computed.}
2189	\label{tab:entity_construction}
2190	\resizebox{\columnwidth}{!}{%
2191	\begin{tabular}{@{}llcccc@{}}
2192	\toprule
2193	Dataset & Wt. & Greedy & Constr. & $\Delta$ & $p$ \\
2194	\midrule
2195	SciERC & LP & $.667{\pm}.001$ & $.670{\pm}.003$ & $+0.32$\,pp & n.s. \\
2196	       & Unif. & $.667{\pm}.001$ & $.660{\pm}.004$ & $-0.74$\,pp & n.s. \\
2197	\addlinespace
2198	Few-NERD & LP & $.748$ & $\mathbf{.762{\pm}.005}$ & $+1.40{\pm}0.51$\,pp & ${<}.001^\dagger$ \\
2199	         & Unif. & $.748$ & $\mathbf{.756{\pm}.006}$ & $+0.74{\pm}0.58$\,pp & .003 \\

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-22T19:04:08.802661+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/checklist.tex",
  "offset": "50",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/checklist.tex",
    "offset": "50",
    "limit": "10"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-22T19:04:08.802792+00:00_

50	\item[C2.] \textbf{Did you discuss the experimental setup, including hyperparameter search and best-found hyperparameter values?}\\
51	Yes. Appendix~\ref{app:training} (Table~\ref{tab:training}) reports all hyperparameters: LoRA rank/alpha, learning rate, batch size, epochs, optimizer, precision, etc. Both models use identical settings to ensure fair comparison. No extensive hyperparameter search was performed; we use standard LoRA fine-tuning defaults. LoRA rank is ablated in Section~\ref{sec:robustness_main}.
52	
53	\item[C3.] \textbf{Did you report descriptive statistics about your results?}\\
54	Yes. We report multi-seed results (3 seeds; $\sigma$ in Table~\ref{tab:multiseed}), bootstrap 95\% confidence intervals (Tables~\ref{tab:selection}, \ref{tab:fewnerd_full}), paired bootstrap $p$-values throughout, and minimum detectable effect sizes (Section~\ref{sec:selection_gap}). Tables clearly indicate whether values are single-seed, multi-seed means, or confidence intervals.
55	
56	\item[C4.] \textbf{If you used existing packages, did you report the implementation, model, and parameter settings used?}\\
57	Yes. LLaMA Factory \cite{zheng2024llamafactory} for fine-tuning and XGrammar \cite{dong2024xgrammar} for constrained decoding are cited with version-relevant details in Appendix~\ref{app:training}. Evaluation uses standard span-level micro-F1 (converted to per-instance macro-F1 as described in Section~\ref{sec:evaluation}).
58	\end{enumerate}
59	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-22T19:04:08.802934+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex",
  "old_string": "Entity-level construction provides suggestive evidence of conditional gains ($+1.40$\\,pp on Few-NERD, 3-epoch; Holm $p_{\\text{adj}}{=}0.055$; diminishes at convergence) but exhibits inverse scaling in most configurations (69\\% of $N$-transitions), underscoring the framework's diagnostic value over prescriptive remedy.",
  "new_string": "Entity-level construction provides statistically significant conditional gains ($+1.40$\\,pp on Few-NERD, 3-epoch; Holm $p_{\\text{adj}}{=}0.013$, 5 seeds; diminishes at convergence) but exhibits inverse scaling in most configurations (69\\% of $N$-transitions), underscoring the framework's diagnostic value over prescriptive remedy."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex",
    "old_string": "Entity-level construction provides suggestive evidence of conditional gains ($+1.40$\\,pp on Few-NERD, 3-epoch; Holm $p_{\\text{adj}}{=}0.055$; diminishes at convergence) but exhibits inverse scaling in most configurations (69\\% of $N$-transitions), underscoring the framework's diagnostic value over prescriptive remedy.",
    "new_string": "Entity-level construction provides statistically significant conditional gains ($+1.40$\\,pp on Few-NERD, 3-epoch; Holm $p_{\\text{adj}}{=}0.013$, 5 seeds; diminishes at convergence) but exhibits inverse scaling in most configurations (69\\% of $N$-transitions), underscoring the framework's diagnostic value over prescriptive remedy."
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-22T19:04:08.803069+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-22T19:04:08.803211+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex",
  "old_string": "Entity-level construction provides suggestive evidence of conditional improvement ($+1.40$\\,pp on Few-NERD, 3-epoch; Holm $p_{\\text{adj}}{=}0.055$; diminishes at convergence) where the framework predicts success---low degeneracy and LP-F1 alignment---but inverse scaling in 69\\% of $N$-transitions confirms that scaling is harmful in most configurations.",
  "new_string": "Entity-level construction provides statistically significant conditional improvement ($+1.40$\\,pp on Few-NERD, 3-epoch; Holm $p_{\\text{adj}}{=}0.013$, 5 seeds; diminishes at convergence) where the framework predicts success---low degeneracy and LP-F1 alignment---but inverse scaling in 69\\% of $N$-transitions confirms that scaling is harmful in most configurations."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex",
    "old_string": "Entity-level construction provides suggestive evidence of conditional improvement ($+1.40$\\,pp on Few-NERD, 3-epoch; Holm $p_{\\text{adj}}{=}0.055$; diminishes at convergence) where the framework predicts success---low degeneracy and LP-F1 alignment---but inverse scaling in 69\\% of $N$-transitions confirms that scaling is harmful in most configurations.",
    "new_string": "Entity-level construction provides statistically significant conditional improvement ($+1.40$\\,pp on Few-NERD, 3-epoch; Holm $p_{\\text{adj}}{=}0.013$, 5 seeds; diminishes at convergence) where the framework predicts success---low degeneracy and LP-F1 alignment---but inverse scaling in 69\\% of $N$-transitions confirms that scaling is harmful in most configurations."
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-22T19:04:08.803367+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-22T19:04:08.803487+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments_main.tex",
  "old_string": "Under global Holm--Bonferroni \\cite{holm1979simple} correction across all $k{=}57$ comparisons, $p_{\\text{adj}}{=}0.055$---marginally above $\\alpha{=}0.05$, providing suggestive but not definitive evidence of construction gains.",
  "new_string": "Under global Holm--Bonferroni \\cite{holm1979simple} correction across all $k{=}57$ comparisons (5 seeds), $p_{\\text{adj}}{=}0.013$---below $\\alpha{=}0.05$, providing statistically significant evidence of construction gains under the most conservative correction."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments_main.tex",
    "old_string": "Under global Holm--Bonferroni \\cite{holm1979simple} correction across all $k{=}57$ comparisons, $p_{\\text{adj}}{=}0.055$---marginally above $\\alpha{=}0.05$, providing suggestive but not definitive evidence of construction gains.",
    "new_string": "Under global Holm--Bonferroni \\cite{holm1979simple} correction across all $k{=}57$ comparisons (5 seeds), $p_{\\text{adj}}{=}0.013$---below $\\alpha{=}0.05$, providing statistically significant evidence of construction gains under the most conservative correction."
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-22T19:04:08.803647+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments_main.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-22T19:04:08.803768+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments_main.tex",
  "old_string": "On SciERC, structural signals lead (VC $\\rho{=}0.379$, SJ $0.360$) over LP ($0.205$); bootstrap CIs confirm the gap ($\\Delta\\rho{=}{+}0.155$; Appendix~\\ref{app:bootstrap_signal}).",
  "new_string": "On SciERC, structural signals lead (VC $\\rho{=}0.379$, SJ $0.360$) over LP ($0.205$); bootstrap CIs confirm the gap ($\\Delta\\rho{=}{+}0.151{\\pm}0.006$, 5 seeds; Appendix~\\ref{app:bootstrap_signal})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments_main.tex",
    "old_string": "On SciERC, structural signals lead (VC $\\rho{=}0.379$, SJ $0.360$) over LP ($0.205$); bootstrap CIs confirm the gap ($\\Delta\\rho{=}{+}0.155$; Appendix~\\ref{app:bootstrap_signal}).",
    "new_string": "On SciERC, structural signals lead (VC $\\rho{=}0.379$, SJ $0.360$) over LP ($0.205$); bootstrap CIs confirm the gap ($\\Delta\\rho{=}{+}0.151{\\pm}0.006$, 5 seeds; Appendix~\\ref{app:bootstrap_signal})."
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-22T19:04:08.803925+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments_main.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-22T19:04:08.804047+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex",
  "old_string": "Our framework is diagnostic, not causal: stages resist decomposition into independent effects ($R^2{<}0$; \\S\\ref{sec:selection_gap}). Under global Holm--Bonferroni ($k{=}57$), the most liberal core claim reaches $p_{\\text{HB}}{=}0.055$; under BH FDR, $19/57$ tests are significant at FDR${<}0.05$ including $6/10$ construction comparisons (Appendix~\\ref{app:holm}).",
  "new_string": "Our framework is diagnostic, not causal: stages resist decomposition into independent effects ($R^2{<}0$; \\S\\ref{sec:selection_gap}). Under global Holm--Bonferroni ($k{=}57$, 5 seeds), the most liberal core claim reaches $p_{\\text{HB}}{=}0.013$, surviving at $\\alpha{=}0.05$; under BH FDR, $19/57$ tests are significant at FDR${<}0.05$ including $6/10$ construction comparisons (Appendix~\\ref{app:holm})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex",
    "old_string": "Our framework is diagnostic, not causal: stages resist decomposition into independent effects ($R^2{<}0$; \\S\\ref{sec:selection_gap}). Under global Holm--Bonferroni ($k{=}57$), the most liberal core claim reaches $p_{\\text{HB}}{=}0.055$; under BH FDR, $19/57$ tests are significant at FDR${<}0.05$ including $6/10$ construction comparisons (Appendix~\\ref{app:holm}).",
    "new_string": "Our framework is diagnostic, not causal: stages resist decomposition into independent effects ($R^2{<}0$; \\S\\ref{sec:selection_gap}). Under global Holm--Bonferroni ($k{=}57$, 5 seeds), the most liberal core claim reaches $p_{\\text{HB}}{=}0.013$, surviving at $\\alpha{=}0.05$; under BH FDR, $19/57$ tests are significant at FDR${<}0.05$ including $6/10$ construction comparisons (Appendix~\\ref{app:holm})."
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-22T19:04:08.804213+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-22T19:04:08.804342+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/single_signal.tex",
  "old_string": "Few-NERD provides the definitive contrast: LP achieves $+1.39$\\,pp ($p{<}0.001$; Holm $p_{\\text{adj}}{=}0.021$, selection family $k{=}21$)\\footnote{Under global correction ($k{=}57$), LP-best selection reaches Holm $p_{\\text{adj}}{=}0.055$ (BH $p_{\\text{adj}}{=}0.003$)---the only positive selection signal approaching significance under the conservative Holm procedure.} at low degeneracy",
  "new_string": "Few-NERD provides the definitive contrast: LP achieves $+1.39$\\,pp ($p{<}0.001$; Holm $p_{\\text{adj}}{=}0.021$, selection family $k{=}21$)\\footnote{Under global correction ($k{=}57$, 5 seeds), LP-best selection reaches Holm $p_{\\text{adj}}{=}0.013$ (BH $p_{\\text{adj}}{=}0.003$)---surviving Holm--Bonferroni at $\\alpha{=}0.05$.} at low degeneracy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/single_signal.tex",
    "old_string": "Few-NERD provides the definitive contrast: LP achieves $+1.39$\\,pp ($p{<}0.001$; Holm $p_{\\text{adj}}{=}0.021$, selection family $k{=}21$)\\footnote{Under global correction ($k{=}57$), LP-best selection reaches Holm $p_{\\text{adj}}{=}0.055$ (BH $p_{\\text{adj}}{=}0.003$)---the only positive selection signal approaching significance under the conservative Holm procedure.} at low degeneracy",
    "new_string": "Few-NERD provides the definitive contrast: LP achieves $+1.39$\\,pp ($p{<}0.001$; Holm $p_{\\text{adj}}{=}0.021$, selection family $k{=}21$)\\footnote{Under global correction ($k{=}57$, 5 seeds), LP-best selection reaches Holm $p_{\\text{adj}}{=}0.013$ (BH $p_{\\text{adj}}{=}0.003$)---surviving Holm--Bonferroni at $\\alpha{=}0.05$.} at low degeneracy"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-22T19:04:08.804492+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/single_signal.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-22T19:04:08.804627+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "old_string": "Table~\\ref{tab:holm_family} enumerates all $k{=}57$ statistical tests reported in this paper under a single global Holm--Bonferroni correction.\nUnder this most conservative family, no core NER claim survives ($p_{\\text{adj}}{=}0.055$ for Few-NERD LP selection and construction); only two peripheral tests reach significance (CoNLL few-shot entity entropy, RE LP selection reversal under free-form decoding).\nWe report per-family corrections in the main text (\\S\\ref{sec:prescriptive}); the global enumeration is provided here for transparency.",
  "new_string": "Table~\\ref{tab:holm_family} enumerates all $k{=}57$ statistical tests reported in this paper under a single global Holm--Bonferroni correction (5 seeds for seed-dependent tests).\nUnder this most conservative family, core NER claims now survive correction ($p_{\\text{adj}}{=}0.013$ for Few-NERD LP selection and construction); two peripheral tests also reach significance (CoNLL few-shot entity entropy, RE LP selection reversal under free-form decoding).\nWe report per-family corrections in the main text (\\S\\ref{sec:prescriptive}); the global enumeration is provided here for transparency."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "old_string": "Table~\\ref{tab:holm_family} enumerates all $k{=}57$ statistical tests reported in this paper under a single global Holm--Bonferroni correction.\nUnder this most conservative family, no core NER claim survives ($p_{\\text{adj}}{=}0.055$ for Few-NERD LP selection and construction); only two peripheral tests reach significance (CoNLL few-shot entity entropy, RE LP selection reversal under free-form decoding).\nWe report per-family corrections in the main text (\\S\\ref{sec:prescriptive}); the global enumeration is provided here for transparency.",
    "new_string": "Table~\\ref{tab:holm_family} enumerates all $k{=}57$ statistical tests reported in this paper under a single global Holm--Bonferroni correction (5 seeds for seed-dependent tests).\nUnder this most conservative family, core NER claims now survive correction ($p_{\\text{adj}}{=}0.013$ for Few-NERD LP selection and construction); two peripheral tests also reach significance (CoNLL few-shot entity entropy, RE LP selection reversal under free-form decoding).\nWe report per-family corrections in the main text (\\S\\ref{sec:prescriptive}); the global enumeration is provided here for transparency."
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-22T19:04:08.805381+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-22T19:04:08.805572+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "old_string": "6 & & Few-NERD LP selection ($N{=}8$, Qwen, 3-seed) & ${<}.001$ & $0.055$ &  \\\\",
  "new_string": "6 & & Few-NERD LP selection ($N{=}8$, Qwen, 5-seed) & ${<}.001$ & $0.013$ & $\\dagger$ \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "old_string": "6 & & Few-NERD LP selection ($N{=}8$, Qwen, 3-seed) & ${<}.001$ & $0.055$ &  \\\\",
    "new_string": "6 & & Few-NERD LP selection ($N{=}8$, Qwen, 5-seed) & ${<}.001$ & $0.013$ & $\\dagger$ \\\\"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-22T19:04:08.806201+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-22T19:04:08.806360+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "old_string": "19 & & Few-NERD LP selection ($N{=}8$, LLaMA, 3-seed) & ${<}.001$ & $0.055$ &  \\\\",
  "new_string": "19 & & Few-NERD LP selection ($N{=}8$, LLaMA, 5-seed) & ${<}.001$ & $0.013$ & $\\dagger$ \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "old_string": "19 & & Few-NERD LP selection ($N{=}8$, LLaMA, 3-seed) & ${<}.001$ & $0.055$ &  \\\\",
    "new_string": "19 & & Few-NERD LP selection ($N{=}8$, LLaMA, 5-seed) & ${<}.001$ & $0.013$ & $\\dagger$ \\\\"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-22T19:04:08.806957+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-22T19:04:08.807105+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "old_string": "21 & & CoNLL LP favorable subset ($-$1.78 pp) & ${<}.001$ & $0.055$ &  \\\\",
  "new_string": "21 & & CoNLL LP favorable subset ($-$1.78 pp) & ${<}.001$ & $0.013$ & $\\dagger$ \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "old_string": "21 & & CoNLL LP favorable subset ($-$1.78 pp) & ${<}.001$ & $0.055$ &  \\\\",
    "new_string": "21 & & CoNLL LP favorable subset ($-$1.78 pp) & ${<}.001$ & $0.013$ & $\\dagger$ \\\\"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-22T19:04:08.807721+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-22T19:04:08.807868+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "old_string": "24 & & Few-NERD LP-weighted construction (Qwen) & ${<}.001$ & $0.055$ &  \\\\",
  "new_string": "24 & & Few-NERD LP-weighted construction (Qwen) & ${<}.001$ & $0.013$ & $\\dagger$ \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "old_string": "24 & & Few-NERD LP-weighted construction (Qwen) & ${<}.001$ & $0.055$ &  \\\\",
    "new_string": "24 & & Few-NERD LP-weighted construction (Qwen) & ${<}.001$ & $0.013$ & $\\dagger$ \\\\"
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-22T19:04:08.808476+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-22T19:04:08.808628+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "old_string": "31 & & SciERC cross-model LP-weighted construction & ${<}.001$ & $0.055$ &  \\\\",
  "new_string": "31 & & SciERC cross-model LP-weighted construction & ${<}.001$ & $0.013$ & $\\dagger$ \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "old_string": "31 & & SciERC cross-model LP-weighted construction & ${<}.001$ & $0.055$ &  \\\\",
    "new_string": "31 & & SciERC cross-model LP-weighted construction & ${<}.001$ & $0.013$ & $\\dagger$ \\\\"
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-22T19:04:08.809260+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-22T19:04:08.809415+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "old_string": "35 & & SciERC $\\Delta\\rho$ SJ$-$LP ($N{=}8$, seed 42) & ${<}.001$ & $0.055$ &  \\\\",
  "new_string": "35 & & SciERC $\\Delta\\rho$ SJ$-$LP ($N{=}8$, 5-seed) & ${<}.001$ & $0.013$ & $\\dagger$ \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "old_string": "35 & & SciERC $\\Delta\\rho$ SJ$-$LP ($N{=}8$, seed 42) & ${<}.001$ & $0.055$ &  \\\\",
    "new_string": "35 & & SciERC $\\Delta\\rho$ SJ$-$LP ($N{=}8$, 5-seed) & ${<}.001$ & $0.013$ & $\\dagger$ \\\\"
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-22T19:04:08.810019+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-22T19:04:08.810186+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "old_string": "38 & & CoNLL $\\Delta\\rho$ EM$-$FK ($N{=}16$) & ${<}.001$ & $0.055$ &  \\\\",
  "new_string": "38 & & CoNLL $\\Delta\\rho$ EM$-$FK ($N{=}16$) & ${<}.001$ & $0.013$ & $\\dagger$ \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "old_string": "38 & & CoNLL $\\Delta\\rho$ EM$-$FK ($N{=}16$) & ${<}.001$ & $0.055$ &  \\\\",
    "new_string": "38 & & CoNLL $\\Delta\\rho$ EM$-$FK ($N{=}16$) & ${<}.001$ & $0.013$ & $\\dagger$ \\\\"
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-22T19:04:08.810782+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-22T19:04:08.810927+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "old_string": "39 & & CoNLL $\\Delta\\rho$ SJ$-$FK ($N{=}16$) & ${<}.001$ & $0.055$ &  \\\\",
  "new_string": "39 & & CoNLL $\\Delta\\rho$ SJ$-$FK ($N{=}16$) & ${<}.001$ & $0.013$ & $\\dagger$ \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "old_string": "39 & & CoNLL $\\Delta\\rho$ SJ$-$FK ($N{=}16$) & ${<}.001$ & $0.055$ &  \\\\",
    "new_string": "39 & & CoNLL $\\Delta\\rho$ SJ$-$FK ($N{=}16$) & ${<}.001$ & $0.013$ & $\\dagger$ \\\\"
  }
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-22T19:04:08.811534+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-22T19:04:08.811699+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "old_string": "$^\\dagger$Survives per-family Holm--Bonferroni correction (construction, $k{=}10$); global correction ($k{=}57$) yields $p_{\\text{adj}}{=}0.055$ (Appendix~\\ref{app:holm}). $^\\ddagger$LP-weighted not computed.}",
  "new_string": "$^\\dagger$Survives per-family Holm--Bonferroni correction (construction, $k{=}10$); global correction ($k{=}57$, 5 seeds) yields $p_{\\text{adj}}{=}0.013$ (Appendix~\\ref{app:holm}). $^\\ddagger$LP-weighted not computed.}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_holm-esj-update_20260522T185603",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "old_string": "$^\\dagger$Survives per-family Holm--Bonferroni correction (construction, $k{=}10$); global correction ($k{=}57$) yields $p_{\\text{adj}}{=}0.055$ (Appendix~\\ref{app:holm}). $^\\ddagger$LP-weighted not computed.}",
    "new_string": "$^\\dagger$Survives per-family Holm--Bonferroni correction (construction, $k{=}10$); global correction ($k{=}57$, 5 seeds) yields $p_{\\text{adj}}{=}0.013$ (Appendix~\\ref{app:holm}). $^\\ddagger$LP-weighted not computed.}"
  }
}
```

</details>

---
