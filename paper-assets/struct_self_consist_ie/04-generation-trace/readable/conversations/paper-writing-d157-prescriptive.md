# paper writing d157 prescriptive

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 7
- **Recorded user turns:** 0
- **Tool calls:** 3
- **Original source:** `logs/chats/worker_paper_writing_d157_prescriptive_20260519T022603.jsonl`
- **Structured JSON:** [`6f8901eae4d40481eccc.json`](../../sessions/6f/6f8901eae4d40481eccc.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

7 recorded events

### Tool call

_source line 1 · 2026-05-19T02:27:26.349962+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_d157_prescriptive_20260519T022603",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-19T02:27:26.350463+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on four English NER benchmarks spanning a difficulty gradient, each serving a distinct role.
9	\textbf{SciERC} \cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed where models achieve ${\approx}$65\% F1.
10	\textbf{Few-NERD} \cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\approx}$75\% F1) provides a low-degeneracy contrast where LP selection succeeds (\S\ref{sec:fewnerd}).
11	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\approx}$91\% F1) serves as a ceiling-effect control where limited oracle headroom constrains selection gains.
12	\textbf{WNUT-17} \cite{derczynski2017wnut} (1{,}287 social media instances, 52\% zero F1) probes the signal-collapse boundary where model capability is insufficient.
13	
14	\paragraph{Models and sampling.}
15	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures, except Few-NERD models which use 3 epochs (early stopping at the best validation checkpoint; a 5-epoch control confirms LP selection remains positive though gains are halved; Appendix~\ref{app:epoch_confound}).
16	Qwen3-8B's SciERC checkpoint has a minor train--test mismatch (empty thinking tokens); a quantitative analysis rules out this confound (Appendix~\ref{app:thinking_token}).
17	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments (ranking stability $\sigma{\leq}0.026$, Table~\ref{tab:multiseed}; sublinear gains beyond $N{=}8$, Appendix~\ref{app:n_scaling}).
18	Inference uses vLLM with constrained decoding \cite{willard2023guided} (seed protocol: Appendix~\ref{app:multiseed}).
19	
20	%% ===================================
…[truncated 17091 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_d157_prescriptive_20260519T022603",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T02:27:26.350671+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/skills/paper-writing-norms.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_d157_prescriptive_20260519T022603",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/skills/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-19T02:27:26.350960+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_d157_prescriptive_20260519T022603",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T02:27:26.351176+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/_draft_prescriptive.tex",
  "content": "%% ============================================================\n\\subsection{Prescriptive Results}\n\\label{sec:prescriptive}\n\nThe preceding sections establish that instance-level selection fails for structured IE. We now present two approaches that extract value from multi-sample generation without relying on sample ranking.\n\n\\paragraph{Entity-level construction.}\nRather than selecting one of $N$ complete outputs, we aggregate entities across all samples. For each unique entity mention, we compute its frequency across $N$ samples and retain those exceeding a threshold $\\theta$ tuned via 5-fold cross-validation (reporting inner-fold F1 means; $\\theta{=}0.5$ majority baseline in Appendix~\\ref{app:entity_merge}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Entity-level construction vs.\\ greedy decoding (macro F1; $N{=}8$, $T{=}1.0$, Qwen3-8B). Threshold $\\theta$ tuned via 5-fold CV (inner-fold means). $p$: paired bootstrap vs.\\ greedy ($n{=}10{,}000$).}\n\\label{tab:entity_construction}\n\\begin{tabular}{@{}lrcccc@{}}\n\\toprule\nDataset & $n$ & Greedy & Constr. & $\\Delta$ & $p$ \\\\\n\\midrule\nSciERC & 529 & .644 & \\textbf{.658} & $+$1.35\\,pp & .018 \\\\\nFew-NERD & 32{,}565 & .748 & \\textbf{.761} & $+$1.32\\,pp & ${<}.001$ \\\\\nCoNLL & 2{,}756 & .908 & .909 & $+$0.10\\,pp & n.s. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nConstruction significantly improves on SciERC ($+1.35$\\,pp, $p{=}0.018$) and Few-NERD ($+1.32$\\,pp, $p{<}0.001$). CoNLL shows no significant gain ($+0.10$\\,pp), consistent with ceiling-regime degeneracy. The mechanism is recall-driven: aggregating low-frequency correct entities across samples recovers mentions that no single sample captures. LP-weighted aggregation shows no advantage over uniform weighting.\n\n\\paragraph{Construction and LP selection are complementary.}\nUnder matched 5-fold CV evaluation, construction dominates on SciERC ($+1.35$\\,pp vs.\\ LP $+0.23$\\,pp), where LP-quality alignment is weak (within-instance $\\rho{\\approx}0.2$).\nOn Few-NERD, where alignment is strong ($\\rho{\\approx}0.5$--$0.7$), LP selection outperforms construction ($+1.88$\\,pp vs.\\ $+1.32$\\,pp).\nThe choice is governed by LP-quality alignment: when LP tracks entity-level F1 within instances, per-sample ranking succeeds; when alignment is weak, entity aggregation bypasses ranking entirely.\n\n\\paragraph{LP-alignment gating.}\nA simple gating protocol probes 50 held-out validation instances to estimate within-instance $\\rho(\\text{LP}, \\text{F1})$. Above a threshold, LP selection is applied; below it, entity construction is used instead. This protocol correctly identifies the better method on all three evaluated datasets, and the threshold is stable across $[0.2, 0.4]$. Three caveats apply: (a) the probe uses validation data, not test data; (b) threshold stability is evaluated on only three datasets; (c) this is a proof of concept that requires broader validation.\n\n\\paragraph{Selective prediction.}\nOrthogonal to construction, QE signals support selective prediction: retaining the top-$k$\\% highest-confidence instances. At 80\\% coverage, selective prediction yields $+5$--$8$\\,pp F1 gain (AUPRC 0.70--0.92), with VC as the strongest signal across all datasets. For practitioners, when selection fails, QE scores can route low-confidence instances to human review rather than sample $N$ candidates to identify the best output.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_d157_prescriptive_20260519T022603",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/_draft_prescriptive.tex",
    "content": "%% ============================================================\n\\subsection{Prescriptive Results}\n\\label{sec:prescriptive}\n\nThe preceding sections establish that instance-level selection fails for structured IE. We now present two approaches that extract value from multi-sample generation without relying on sample ranking.\n\n\\paragraph{Entity-level construction.}\nRather than selecting one of $N$ complete outputs, we aggregate entities across all samples. For each unique entity mention, we compute its frequency across $N$ samples and retain those exceeding a threshold $\\theta$ tuned via 5-fold cross-validation (reporting inner-fold F1 means; $\\theta{=}0.5$ majority baseline in Appendix~\\ref{app:entity_merge}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Entity-level construction vs.\\ greedy decoding (macro F1; $N{=}8$, $T{=}1.0$, Qwen3-8B). Threshold $\\theta$ tuned via 5-fold CV (inner-fold means). $p$: paired bootstrap vs.\\ greedy ($n{=}10{,}000$).}\n\\label{tab:entity_construction}\n\\begin{tabular}{@{}lrcccc@{}}\n\\toprule\nDataset & $n$ & Greedy & Constr. & $\\Delta$ & $p$ \\\\\n\\midrule\nSciERC & 529 & .644 & \\textbf{.658} & $+$1.35\\,pp & .018 \\\\\nFew-NERD & 32{,}565 & .748 & \\textbf{.761} & $+$1.32\\,pp & ${<}.001$ \\\\\nCoNLL & 2{,}756 & .908 & .909 & $+$0.10\\,pp & n.s. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nConstruction significantly improves on SciERC ($+1.35$\\,pp, $p{=}0.018$) and Few-NERD ($+1.32$\\,pp, $p{<}0.001$). CoNLL shows no significant gain ($+0.10$\\,pp), consistent with ceiling-regime degeneracy. The mechanism is recall-driven: aggregating low-frequency correct entities across samples recovers mentions that no single sample captures. LP-weighted aggregation shows no advantage over uniform weighting.\n\n\\paragraph{Construction and LP selection are complementary.}\nUnder matched 5-fold CV evaluation, construction dominates on SciERC ($+1.35$\\,pp vs.\\ LP $+0.23$\\,pp), where LP-quality alignment is weak (within-instance $\\rho{\\approx}0.2$).\nOn Few-NERD, where alignment is strong ($\\rho{\\approx}0.5$--$0.7$), LP selection outperforms construction ($+1.88$\\,pp vs.\\ $+1.32$\\,pp).\nThe choice is governed by LP-quality alignment: when LP tracks entity-level F1 within instances, per-sample ranking succeeds; when alignment is weak, entity aggregation bypasses ranking entirely.\n\n\\paragraph{LP-alignment gating.}\nA simple gating protocol probes 50 held-out validation instances to estimate within-instance $\\rho(\\text{LP}, \\text{F1})$. Above a threshold, LP selection is applied; below it, entity construction is used instead. This protocol correctly identifies the better method on all three evaluated datasets, and the threshold is stable across $[0.2, 0.4]$. Three caveats apply: (a) the probe uses validation data, not test data; (b) threshold stability is evaluated on only three datasets; (c) this is a proof of concept that requires broader validation.\n\n\\paragraph{Selective prediction.}\nOrthogonal to construction, QE signals support selective prediction: retaining the top-$k$\\% highest-confidence instances. At 80\\% coverage, selective prediction yields $+5$--$8$\\,pp F1 gain (AUPRC 0.70--0.92), with VC as the strongest signal across all datasets. For practitioners, when selection fails, QE scores can route low-confidence instances to human review rather than sample $N$ candidates to identify the best output.\n"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T02:27:26.351364+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/_draft_prescriptive.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_d157_prescriptive_20260519T022603",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-19T02:27:26.351516+00:00_

Draft written to `docs/paper/sections/_draft_prescriptive.tex`. Four paragraphs plus one table, matching the existing `experiments.tex` formatting (column padding, booktabs, `\,pp` notation, bold best values). No em-dashes, no -ing endings, no banned words. All numbers from the provided data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_d157_prescriptive_20260519T022603"
}
```

</details>

---
