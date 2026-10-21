# paper abstract intro headline

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/chats/worker_paper_abstract-intro-headline_20260515T222641.jsonl`
- **Structured JSON:** [`24c148c2d98cd6ae9b0b.json`](../../sessions/24/24c148c2d98cd6ae9b0b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

15 recorded events

### Tool call

_source line 1 · 2026-05-15T22:27:35.904072+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_abstract-intro-headline_20260515T222641",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T22:27:35.904464+00:00_

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
  "session": "worker_paper_abstract-intro-headline_20260515T222641",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T22:27:35.904684+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_abstract-intro-headline_20260515T222641",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T22:27:35.904871+00:00_

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
  "session": "worker_paper_abstract-intro-headline_20260515T222641",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T22:27:35.905078+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/abstract.tex",
  "old_string": "A 7-feature ensemble exploiting this complementarity achieves binary macro-F1 of 0.723 (95\\% CI: [0.717, 0.729]) for gen-1 vs.\\ gen-2+ depth discrimination---excluding gen-0 to avoid shared-seed overlap---($p < 0.001$ vs.\\ all baselines) across 6 base-model generators from 3 model families (0.6B--8.2B parameters), with per-generator consistency (std\\,=\\,0.051).",
  "new_string": "A 7-feature ensemble exploiting this complementarity achieves binary macro-F1 of 0.723 for gen-1 vs.\\ gen-2+ depth discrimination---excluding gen-0 to avoid shared-seed overlap---($p < 0.001$ vs.\\ all baselines) across 6 base-model generators from 3 model families (0.6B--8.2B parameters), with per-generator F1 ranging from 0.68 to 0.86."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_abstract-intro-headline_20260515T222641",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/abstract.tex",
    "old_string": "A 7-feature ensemble exploiting this complementarity achieves binary macro-F1 of 0.723 (95\\% CI: [0.717, 0.729]) for gen-1 vs.\\ gen-2+ depth discrimination---excluding gen-0 to avoid shared-seed overlap---($p < 0.001$ vs.\\ all baselines) across 6 base-model generators from 3 model families (0.6B--8.2B parameters), with per-generator consistency (std\\,=\\,0.051).",
    "new_string": "A 7-feature ensemble exploiting this complementarity achieves binary macro-F1 of 0.723 for gen-1 vs.\\ gen-2+ depth discrimination---excluding gen-0 to avoid shared-seed overlap---($p < 0.001$ vs.\\ all baselines) across 6 base-model generators from 3 model families (0.6B--8.2B parameters), with per-generator F1 ranging from 0.68 to 0.86."
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T22:27:35.905230+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/abstract.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_abstract-intro-headline_20260515T222641",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T22:27:35.905350+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex",
  "old_string": "binary macro-F1 of 0.723 (95\\% CI: [0.717, 0.729]) for leak-free depth discrimination (gen-1 vs.\\ gen-2+), with per-generator consistency (std\\,=\\,0.051).",
  "new_string": "binary macro-F1 of 0.723 for leak-free depth discrimination (gen-1 vs.\\ gen-2+), with per-generator F1 ranging from 0.68 (Qwen3-8B) to 0.86 (Pythia-1B)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_abstract-intro-headline_20260515T222641",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex",
    "old_string": "binary macro-F1 of 0.723 (95\\% CI: [0.717, 0.729]) for leak-free depth discrimination (gen-1 vs.\\ gen-2+), with per-generator consistency (std\\,=\\,0.051).",
    "new_string": "binary macro-F1 of 0.723 for leak-free depth discrimination (gen-1 vs.\\ gen-2+), with per-generator F1 ranging from 0.68 (Qwen3-8B) to 0.86 (Pythia-1B)."
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T22:27:35.905490+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_abstract-intro-headline_20260515T222641",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T22:27:35.905635+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex",
  "old_string": "binary F1\\,=\\,0.723 (95\\% CI: [0.717, 0.729]) for leak-free depth discrimination (gen-1 vs.\\ gen-2+), outperforming all individual detection baselines ($p < 0.001$), with per-generator consistency (std\\,=\\,0.051).",
  "new_string": "binary F1\\,=\\,0.723 for leak-free depth discrimination (gen-1 vs.\\ gen-2+), outperforming all individual detection baselines ($p < 0.001$), with per-generator F1 ranging from 0.68 to 0.86."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_abstract-intro-headline_20260515T222641",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex",
    "old_string": "binary F1\\,=\\,0.723 (95\\% CI: [0.717, 0.729]) for leak-free depth discrimination (gen-1 vs.\\ gen-2+), outperforming all individual detection baselines ($p < 0.001$), with per-generator consistency (std\\,=\\,0.051).",
    "new_string": "binary F1\\,=\\,0.723 for leak-free depth discrimination (gen-1 vs.\\ gen-2+), outperforming all individual detection baselines ($p < 0.001$), with per-generator F1 ranging from 0.68 to 0.86."
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T22:27:35.905802+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_abstract-intro-headline_20260515T222641",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T22:27:35.905930+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_abstract-intro-headline_20260515T222641",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T22:27:35.906053+00:00_

1	% Abstract — Depth Fingerprinting of Recursive LLM Generation Chains
2	\begin{abstract}
3	As LLM outputs accumulate on the web, training corpora increasingly contain recursively generated text of unknown provenance depth.
4	We formulate \emph{ordinal depth estimation}---classifying text as human-written (gen-0), first-generation synthetic (gen-1), or deeper (gen-2+)---beyond binary detection.
5	We characterize a \emph{differential depth response}: central-tendency and diversity features drift monotonically with generation depth, while distributional shape features remain near-stationary.
6	A 7-feature ensemble exploiting this complementarity achieves binary macro-F1 of 0.723 for gen-1 vs.\ gen-2+ depth discrimination---excluding gen-0 to avoid shared-seed overlap---($p < 0.001$ vs.\ all baselines) across 6 base-model generators from 3 model families (0.6B--8.2B parameters), with per-generator F1 ranging from 0.68 to 0.86.
7	In our setting, depth-aware data curation does not outperform random subsampling, positioning depth fingerprinting as a diagnostic tool for provenance characterization.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_abstract-intro-headline_20260515T222641",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T22:27:35.906184+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex",
  "offset": "23",
  "limit": "14"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_abstract-intro-headline_20260515T222641",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex",
    "offset": "23",
    "limit": "14"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T22:27:35.906316+00:00_

23	We characterize a \emph{differential depth response}: central-tendency and diversity features---including reference-model mean entropy (functionally an NLL-based out-of-distribution score \cite{ood_baseline}), type-token ratio, and hapax ratio---drift monotonically with generation depth, while distributional shape features (entropy standard deviation, tail decay) remain near-stationary.
24	This pattern is consistent with recursive generation inducing a location shift in the NLL distribution: text becomes progressively more predictable on average while the functional form of the distribution is preserved.
25	The combination of drifting and stationary features yields a 7-feature ensemble that achieves binary macro-F1 of 0.723 for leak-free depth discrimination (gen-1 vs.\ gen-2+), with per-generator F1 ranging from 0.68 (Qwen3-8B) to 0.86 (Pythia-1B).
26	
27	We also report a negative finding.
28	Depth-aware data curation---selecting training data based on estimated generation depth---does not improve downstream language model quality compared to random subsampling at equal sample count (perplexity: 2.367 random vs.\ 2.387 depth-stratified).
29	In our experimental setting, depth fingerprinting is an effective \emph{diagnostic} tool for characterizing text provenance, not a \emph{curative} tool for data selection.
30	
31	Our contributions are:
32	\begin{enumerate}[nosep,leftmargin=*]
33	    \item \textbf{Task formulation.} We define ordinal generation depth estimation as a task beyond binary detection, providing a framework for finer-grained provenance characterization of web-crawled text.
34	    \item \textbf{Empirical characterization.} We characterize differential depth response across six base-model generators spanning three model families (0.6B--8.2B): a 7-feature ensemble combining drifting and stationary features achieves binary F1\,=\,0.723 for leak-free depth discrimination (gen-1 vs.\ gen-2+), outperforming all individual detection baselines ($p < 0.001$), 
…[truncated 341 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_abstract-intro-headline_20260515T222641",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-15T22:27:35.906484+00:00_

改动汇总：

| 位置 | 改前 | 改后 |
|------|------|------|
| `abstract.tex:6` | `(95\% CI: [0.717, 0.729])...with per-generator consistency (std=0.051)` | 删除 CI，改为 `with per-generator F1 ranging from 0.68 to 0.86` |
| `introduction.tex:25` | `(95\% CI: [0.717, 0.729])...with per-generator consistency (std=0.051)` | 删除 CI，改为 `with per-generator F1 ranging from 0.68 (Qwen3-8B) to 0.86 (Pythia-1B)` |
| `introduction.tex:34` | `(95\% CI: [0.717, 0.729])...with per-generator consistency (std=0.051)` | 删除 CI，改为 `with per-generator F1 ranging from 0.68 to 0.86` |

验证项：
- **Rd2-N1** (CI 误用): 3 处 CI 全部替换为 per-generator F1 range，不再有 ± 格式
- **Rd2-N2** (Gen-0 泄露): headline 已是 binary F1 = 0.723 (gen-1 vs gen-2+)，无需改动
- **D019** (instruct 反转): 两文件均无 "inverted DDR" claim，line 20 仅声明 instruct 模型 untested
- **数字一致性**: abstract 和 intro 三处均为 F1 = 0.723, range 0.68–0.86
- **3-class F1**: 两文件均未出现，无需处理
- **写作规范**: range 同时报 worst (0.68) 和 best (0.86)，intro 正文标注了对应 generator 名

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_abstract-intro-headline_20260515T222641"
}
```

</details>

---
