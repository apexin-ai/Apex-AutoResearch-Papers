# paper abstract intro headline

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/chats/worker_paper_abstract-intro-headline_20260515T190436.jsonl`
- **Structured JSON:** [`126e34c5998dcf854391.json`](../../sessions/12/126e34c5998dcf854391.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

15 recorded events

### Tool call

_source line 1 · 2026-05-15T19:05:28.971664+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__edit_paper_section",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_abstract-intro-headline_20260515T190436",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__edit_paper_section",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T19:05:28.971934+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_abstract-intro-headline_20260515T190436",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T19:05:28.972122+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "file": "paper_framing.md",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_abstract-intro-headline_20260515T190436",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "gen-depth-fingerprint",
    "file": "paper_framing.md",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T19:05:28.972352+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/paper_framing.md\", \"content\": \"# Paper Framing — gen-depth-fingerprint\\n\\n## Target Venue\\n- **Primary: EMNLP 2026 ARR (deadline: May 25, 2026)** — D012\\n- Fallback: ICLR 2027 (Sep 24), NAACL 2027 ARR (Oct 16)\\n\\n## Core Insight\\nNon-paraphrastic LLM generation chains exhibit **differential depth response**: **central-tendency/diversity features** (entropy_mean, TTR, hapax ratio) drift monotonically with depth, while **distributional shape features** (entropy_std, tail_decay) remain near-stationary. This differential response is consistent with recursive generation inducing a **location shift** in the NLL distribution — the text becomes progressively more predictable (mean shifts) while the functional form of the distribution is preserved (shape is invariant). The genuine novelty is not the drift/stationarity split per se (which follows from location-shift properties), but: (a) the **task formulation** (ordinal depth estimation beyond binary detection), (b) **empirical validation** across 6 generators / 3 model families (including 7B+ scale) showing this pattern is robust, (c) the practical consequence that combining both feature types yields **complementary signal** for depth classification. **Primary metric (D017)**: binary LOGO F1 = 0.723 (gen-1 vs gen-2+, excluding gen-0 due to shared-seed leakage). 3-class LOGO F1 = 0.789 reported as supplementary with gen-0 caveat. Per-generator held-out F1: 0.68–0.86 (std=0.058). Key finding: in binary evaluation (no gen-0 leakage), 7-feature (0.723) > 4-baseline ensemble (0.712) — baseline advantage in 3-class was entirely from gen-0 classification. Depth signal is scale-invariant as a phenomenon, though cross-scale classifier transfer shows a moderate gap (8B held-out F1=0.69 vs ≤2.8B 0.76-0.85).\\n\\n## Core Claims (3 条，均可证伪)\\n\\n**Claim 1 — Depth Discriminability**: Distributiona
…[truncated 10559 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_abstract-intro-headline_20260515T190436",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T19:05:28.972507+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_abstract-intro-headline_20260515T190436",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T19:05:28.972690+00:00_

1	% Abstract — Depth Fingerprinting of Recursive LLM Generation Chains
2	\begin{abstract}
3	As LLM outputs accumulate on the web, training corpora increasingly contain recursively generated text of unknown provenance depth.
4	We formulate \emph{ordinal depth estimation}---classifying text as human-written (gen-0), first-generation synthetic (gen-1), or deeper (gen-2+)---beyond binary detection.
5	We characterize a \emph{differential depth response}: central-tendency and diversity features drift monotonically with generation depth, while distributional shape features remain near-stationary.
6	A 7-feature ensemble exploiting this complementarity achieves binary macro-F1 of 0.723 (95\% CI: [0.717, 0.729]) for gen-1 vs.\ gen-2+ depth discrimination---excluding gen-0 to avoid shared-seed overlap---($p < 0.001$ vs.\ all baselines) across 6 base-model generators from 3 model families (0.6B--8.2B parameters), with per-generator consistency (std\,=\,0.051).
7	In our setting, depth-aware data curation does not outperform random subsampling, positioning depth fingerprinting as a diagnostic tool for provenance characterization.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_abstract-intro-headline_20260515T190436",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T19:05:28.972864+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_abstract-intro-headline_20260515T190436",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T19:05:28.973024+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Web-crawled corpora are the dominant source of pretraining data for large language models (LLMs), yet an increasing fraction of this data is itself LLM-generated.
5	Estimates suggest that 7--17\% of recent scientific papers and peer reviews contain substantial LLM-modified content \cite{mapping_llm_science,monitoring_ai_review}, and this proportion continues to grow as generated text enters the web and becomes seed material for subsequent generation.
6	The result is recursive generation chains whose outputs progressively diverge from human-written text---a problem that current detection methods are ill-equipped to address.
7	
8	Existing detectors \cite{fast_detectgpt,binoculars,ld_score,detectgpt} provide binary real-vs-synthetic classification, forcing an all-or-nothing filtering decision: discard everything flagged as synthetic, losing potentially useful first-generation content, or retain everything, admitting text with compounding distributional drift.
9	This conflates qualitatively different material.
10	A first-generation continuation---an LLM expanding a human-written passage---retains much of the source distribution's lexical and structural properties.
11	A third- or fourth-generation text, conditioned recursively on prior LLM outputs, exhibits measurably reduced vocabulary diversity, compressed perplexity, and narrower token probability distributions.
12	Treating these as a single ``synthetic'' category discards provenance information that could inform risk-stratified curation decisions.
13	
14	We argue that a finer-grained characterization is needed: \emph{ordinal depth estimation}, the task of classifying text into generation depth classes (gen-0\,/\,gen-1\,/\,gen-2+) rather than producing a binary label.
15	We refer to the overall framework---features, classifier, and evaluation protocol---as \emph{depth fingerprinting}, distinguishing the method from the task it addresses.
16	No existing method ad
…[truncated 3974 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_abstract-intro-headline_20260515T190436",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T19:05:28.973161+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_abstract-intro-headline_20260515T190436",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T19:05:28.973283+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We introduced ordinal generation depth estimation as a task beyond binary synthetic text detection, providing a framework for characterizing the provenance of web-crawled text at finer granularity.
5	Across six generators from three model families (0.6B--8.2B parameters), we documented differential depth response: central-tendency and diversity features drift monotonically with generation depth, while distributional shape features remain near-stationary.
6	A 7-feature ensemble combining both feature types achieves binary macro-F1 of 0.723 (95\% CI: [0.717, 0.729]) for leak-free depth discrimination across six base-model generators, with per-generator std of 0.051.
7	We also reported that depth-aware data curation does not improve downstream language model quality over random subsampling, establishing that, in our experimental setting, depth fingerprinting functions as a diagnostic tool for provenance characterization rather than a curative tool for data selection.
8	
9	Future work should extend evaluation to instruction-tuned and RLHF models, frontier-scale generators (70B+), mixed-generator chains that better approximate real-world contamination, and multilingual settings.
10	All code, data, and trained models will be released upon publication to facilitate reproducibility.
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_abstract-intro-headline_20260515T190436",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T19:05:28.973453+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0\\.789|0\\.768|3-class|three-class|7-gen",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_abstract-intro-headline_20260515T190436",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0\\.789|0\\.768|3-class|three-class|7-gen",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T19:05:28.973658+00:00_

artifacts/_project/paper/appendix_confusion_matrix.tex:15:\caption{Aggregated 3-class confusion matrix from 6-generator LOGO evaluation ($N=27{,}529$). Each cell shows count and row-normalized percentage. Gen-0 is near-perfectly identified. Gen-1 errors are asymmetric: misclassification as gen-2+ (18.8\%) is 3$\times$ more frequent than as gen-0 (6.2\%), indicating that gen-1 text already carries detectable recursive distortion.}
artifacts/_project/paper/appendix_lofo.tex:1:We complement the permutation importance analysis (\S\ref{sec:results-differential}) with a leave-one-feature-out ablation. Each row drops one of the seven features and re-evaluates the full 6-gen LOGO protocol; $\Delta$ is the change relative to the full 7-feature ensemble (F1\,=\,0.789).
artifacts/_project/paper/appendix_lofo.tex:16:entropy\_min    & 0.789 & $+$0.01\,pp \\
artifacts/_project/paper/appendix_lofo.tex:18:Full (7 features) & 0.789 & --- \\
artifacts/_project/paper/discussion.tex:22:Finer-grained depth distinctions may be achievable for non-paraphrastic chains (unlike paraphrastic chains, which converge within $\sim$3 steps \cite{broken_telephone}), but the three-class scheme already captures the practically relevant boundaries.
artifacts/_project/paper/discussion.tex:44:In 3-class evaluation, multi-detector ensembles achieve marginally higher F1 (0.805 with surface features added vs.\ 0.789).
artifacts/_project/paper/discussion.tex:54:Preliminary experiments with instruction-tuned models show substantially weaker depth fingerprints: OLMo-2-1B-Instruct achieves 3-class LOGO F1\,=\,0.338 (vs.\ 0.763 for base OLMo-2-1B), and Qwen3-0.6B with chat template yields F1\,=\,0.667 (vs.\ 0.816 for the base model).
artifacts/_project/paper/method.tex:75:LOGO F1 is stable across random seeds (mean\,=\,0.789, std\,=\,0.0009 over 5 seeds), confirming that results are not sensitive to classifier initialization.
artifacts/_project/paper/method.tex:77:We evaluated two ordinal-specific methods (CORAL
…[truncated 9049 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_abstract-intro-headline_20260515T190436",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T19:05:28.973842+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0\\.768",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_abstract-intro-headline_20260515T190436",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0\\.768",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T19:05:28.973967+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_abstract-intro-headline_20260515T190436",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-15T19:05:28.974117+00:00_

三个文件（abstract.tex、introduction.tex、conclusion.tex）的 headline 数字**已经是 binary F1=0.723**，无需修改。

具体现状：
- **abstract.tex L6**: `binary macro-F1 of 0.723 (95\% CI: [0.717, 0.729])` — 已是 binary metric
- **introduction.tex L25, L34**: 同上，均为 binary F1=0.723
- **conclusion.tex L6**: 同上

检查项：
- 无 7-gen aggregate 数字（0.768）残留 ✓
- 3-class 0.789 仅出现在 results.tex、method.tex、appendix 等正文/附录中，作为 supplementary metric 并附有 gen-0 leakage caveat ✓
- abstract 中未提及 3-class 0.789（空间紧凑，合理） ✓

这三个文件的 D017 更新已完成，不需要额外改动。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_abstract-intro-headline_20260515T190436"
}
```

</details>

---
