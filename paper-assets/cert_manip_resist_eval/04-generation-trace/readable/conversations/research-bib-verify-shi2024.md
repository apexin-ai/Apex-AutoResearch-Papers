# research bib verify shi2024

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/chats/worker_research_bib-verify-shi2024_20260523T123030.jsonl`
- **Structured JSON:** [`143020bd0ed88457e72e.json`](../../sessions/14/143020bd0ed88457e72e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

11 recorded events

### Tool call

_source line 1 · 2026-05-23T12:31:10.639599+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_bib-verify-shi2024_20260523T123030",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-23T12:31:10.640173+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_bib-verify-shi2024_20260523T123030",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T12:31:10.640487+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2402.14016"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_bib-verify-shi2024_20260523T123030",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2402.14016"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-23T12:31:10.641687+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "shi2024judgerobust",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/references.bib",
  "output_mode": "content",
  "-A": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_bib-verify-shi2024_20260523T123030",
  "tool": "Grep",
  "tool_args": {
    "pattern": "shi2024judgerobust",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/references.bib",
    "output_mode": "content",
    "-A": "15"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-23T12:31:10.641991+00:00_

366:@article{shi2024judgerobust,
367-  author    = {Kaijie Shi and Fuwen Luo and Yew Ken Chia and Lidong Bing},
368-  title     = {Judging {LLM}-as-a-Judge with {MT-Bench} and {Chatbot Arena}},
369-  journal   = {arXiv preprint arXiv:2402.14016},
370-  year      = {2024},
371-  url       = {https://arxiv.org/abs/2402.14016},
372-  note      = {arXiv:2402.14016}
373-}
374-
375-@article{ladha1992condorcet,
376-  author    = {Krishna K. Ladha},
377-  title     = {The {Condorcet} Jury Theorem, Free Speech, and Correlated Votes},
378-  journal   = {American Journal of Political Science},
379-  volume    = {36},
380-  number    = {3},
381-  pages     = {617--634},

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_bib-verify-shi2024_20260523T123030",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-23T12:31:10.642262+00:00_

Web search results for query: "arXiv 2402.14016"

Links: [{"title":"Performance of o1 pro and GPT-4 in self-assessment questions for nephrology board renewal","url":"https://www.medrxiv.org/content/10.1101/2025.01.14.25320525.full.pdf"},{"title":"Rectifiability and Minkowski bounds for the zero loci of $\\mathbb{Z}/2$   harmonic spinors in dimension 4","url":"https://arxiv.org/pdf/1712.06254"},{"title":"Distinguishing GPT-4-generated Radiology Abstracts from Original Abstracts: Performance of Blinded Human Observers and AI Content Detector","url":"https://www.medrxiv.org/content/10.1101/2023.04.28.23289283.full.pdf"},{"title":"Modulator and modulation method using non-uniform 16-symbol signal constellation for low-density parity check codeword having 4/15 code rate","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12095477"},{"title":"arXiv:2402.14016v1 [cs.CL] 21 Feb 2024","url":"https://arxiv.org/pdf/2402.14016"}]

Based on the search results, I found the arXiv paper 2402.14016. 

This work is the first to propose adversarial attacks targeting zero-shot LLM assessment. The paper addresses how adversarial techniques could deceive large language models into predicting high scores regardless of text quality, which poses challenges for model evaluation and raises concerns about academic integrity. The research considers practical adversarial scenarios where the attacker may have limited knowledge of the target models or limited query access, and proposes learning attack phrases using a surrogate model to transfer universal attack phrases.

The paper was submitted on February 21, 2024, with a revised version dated July 4, 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_bib-verify-shi2024_20260523T123030",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T12:31:10.642535+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_bib-verify-shi2024_20260523T123030",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebFetch",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-23T12:31:10.642793+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_bib-verify-shi2024_20260523T123030",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T12:31:10.643005+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2402.14016",
  "prompt": "Extract the exact paper title, full list of all authors, and publication year/date for this arXiv paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_bib-verify-shi2024_20260523T123030",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2402.14016",
    "prompt": "Extract the exact paper title, full list of all authors, and publication year/date for this arXiv paper."
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-23T12:31:10.643216+00:00_

# Paper Information

**Title:** "Is LLM-as-a-Judge Robust? Investigating Universal Adversarial Attacks on Zero-shot LLM Assessment"

**Authors:** Vyas Raina, Adian Liusie, Mark Gales

**Publication Date:** February 21, 2024 (submitted); last revised July 4, 2024

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_bib-verify-shi2024_20260523T123030",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-23T12:31:10.643495+00:00_

核实完成。以下是对比结果：

### arXiv:2402.14016 真实信息

- **标题**: Is LLM-as-a-Judge Robust? Investigating Universal Adversarial Attacks on Zero-shot LLM Assessment
- **作者**: Vyas Raina, Adian Liusie, Mark Gales
- **年份**: 2024

### 当前 bib 条目问题

`shi2024judgerobust` 条目存在 **严重错误**：

| 字段 | 当前 bib 值 | 正确值 |
|------|-----------|--------|
| author | Kaijie Shi, Fuwen Luo, Yew Ken Chia, Lidong Bing | **Vyas Raina, Adian Liusie, Mark Gales** |
| title | Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena | **Is LLM-as-a-Judge Robust? Investigating Universal Adversarial Attacks on Zero-shot LLM Assessment** |

作者和标题完全错误，是另一篇论文的信息被错误关联到了这个 arXiv ID。

### 修正后的完整 bib 条目

```bibtex
@article{raina2024judgerobust,
  author    = {Vyas Raina and Adian Liusie and Mark Gales},
  title     = {Is {LLM}-as-a-Judge Robust? {Investigating} Universal Adversarial Attacks on Zero-shot {LLM} Assessment},
  journal   = {arXiv preprint arXiv:2402.14016},
  year      = {2024},
  url       = {https://arxiv.org/abs/2402.14016},
  note      = {arXiv:2402.14016}
}
```

注意 cite key 也应从 `shi2024judgerobust` 改为 `raina2024judgerobust`，需同步更新所有 `.tex` 文件中的 `\cite{shi2024judgerobust}` 引用。是否需要我直接修改？

Sources:
- [arXiv:2402.14016](https://arxiv.org/abs/2402.14016)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_bib-verify-shi2024_20260523T123030"
}
```

</details>

---
