# paper abstract intro binary f1

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/chats/worker_paper_abstract-intro-binary-f1_20260516T011952.jsonl`
- **Structured JSON:** [`d8dfd09a32b07b6b5397.json`](../../sessions/d8/d8dfd09a32b07b6b5397.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

11 recorded events

### Tool call

_source line 1 · 2026-05-16T01:20:37.633958+00:00_

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
  "session": "worker_paper_abstract-intro-binary-f1_20260516T011952",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T01:20:37.634229+00:00_

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
  "session": "worker_paper_abstract-intro-binary-f1_20260516T011952",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T01:20:37.634393+00:00_

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
  "session": "worker_paper_abstract-intro-binary-f1_20260516T011952",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T01:20:37.634554+00:00_

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
  "session": "worker_paper_abstract-intro-binary-f1_20260516T011952",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T01:20:37.634791+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0\\.\\d{2,3}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_abstract-intro-binary-f1_20260516T011952",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0\\.\\d{2,3}",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T01:20:37.634926+00:00_

6:A 7-feature ensemble exploiting this complementarity achieves binary macro-F1 of 0.723 (95\% CI: [0.717, 0.729]) for gen-1 vs.\ gen-2+ depth discrimination---excluding gen-0 to avoid shared-seed overlap---($p < 0.001$ vs.\ all baselines) across 6 base-model generators from 3 model families (0.6B--8.2B parameters), with per-generator consistency (std\,=\,0.051).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_abstract-intro-binary-f1_20260516T011952",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T01:20:37.635044+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0\\.\\d{2,3}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_abstract-intro-binary-f1_20260516T011952",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0\\.\\d{2,3}",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T01:20:37.635162+00:00_

17:When repurposed as ordinal depth predictors, individual detection scores exhibit high cross-generator variance---per-generator F1 ranging from 0.42 to 0.81 (\S\ref{sec:results-baselines})---making any single detector unreliable across unknown generators.
25:The combination of drifting and stationary features yields a 7-feature ensemble that achieves binary macro-F1 of 0.723 (95\% CI: [0.717, 0.729]) for leak-free depth discrimination (gen-1 vs.\ gen-2+), with per-generator consistency (std\,=\,0.051).
34:    \item \textbf{Empirical characterization.} We characterize differential depth response across six base-model generators spanning three model families (0.6B--8.2B): a 7-feature ensemble combining drifting and stationary features achieves binary F1\,=\,0.723 (95\% CI: [0.717, 0.729]) for leak-free depth discrimination (gen-1 vs.\ gen-2+), outperforming all individual detection baselines ($p < 0.001$), with per-generator consistency (std\,=\,0.051).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_abstract-intro-binary-f1_20260516T011952",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T01:20:37.635277+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "consistently",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_abstract-intro-binary-f1_20260516T011952",
  "tool": "Grep",
  "tool_args": {
    "pattern": "consistently",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T01:20:37.635389+00:00_

artifacts/_project/paper/related_work.tex:14:Even when detection scores correlate with generation depth, they exhibit high cross-generator variance when repurposed as ordinal predictors (binary F1 from 0.52 to 0.71 across individual baselines; Table~\ref{tab:baselines}), because each score captures a single distributional property that generalizes inconsistently.
artifacts/_project/paper/discussion.tex:63:Overall LOGO F1 varies by only 0.013 across three cross-family reference models (0.803--0.816; Table~\ref{tab:cross-ref}), and entropy drift direction is consistently negative for all three, confirming that the differential depth response is a property of recursive generation itself.
artifacts/_project/paper/limitations.tex:8:By contrast, entropy-based depth signals consistently reverse sign across all three instruct models (partial $\rho$ ranging from +0.103 to +0.364), suggesting a genuine behavioral change that persists after controlling for output length.
artifacts/_project/paper/results.tex:93:Entropy drift direction is consistently negative across all reference models (Table~\ref{tab:cross-ref}), confirming that the differential depth response is a property of recursive generation, not of the specific reference model used.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_abstract-intro-binary-f1_20260516T011952",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-16T01:20:37.635567+00:00_

Both files are already correct:

- **abstract.tex**: Headline is binary F1=0.723 with CI [0.717, 0.729], std=0.051. No old numbers.
- **introduction.tex**: Binary F1=0.723 appears in both the main text (line 25) and contributions (line 34), both with CI and std. No old numbers.
- No "consistently" in either file.
- Per-gen consistency uses std format (0.051), not raw range.
- No residual 0.82, 0.80, or 0.789 as headline numbers.
- The 0.42–0.81 range on intro line 17 correctly describes baseline detector weakness, not our ensemble.

No changes needed — both files already reflect the D017 decision with binary F1=0.723 as primary metric.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_abstract-intro-binary-f1_20260516T011952"
}
```

</details>

---
