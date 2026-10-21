# research bibtex 8 papers

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 0
- **Tool calls:** 18
- **Original source:** `logs/chats/worker_research_bibtex_8_papers_20260519T020011.jsonl`
- **Structured JSON:** [`73774243e19889ccc526.json`](../../sessions/73/73774243e19889ccc526.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

37 recorded events

### Tool call

_source line 1 · 2026-05-19T02:02:38.476116+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebFetch,WebSearch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_bibtex_8_papers_20260519T020011",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebFetch,WebSearch",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-19T02:02:38.476507+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_bibtex_8_papers_20260519T020011",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T02:02:38.476713+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2511.18950",
  "prompt": "Extract the full paper title, complete author list (all authors), year, and any venue/conference information. Also check if there's a BibTeX export link."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_bibtex_8_papers_20260519T020011",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2511.18950",
    "prompt": "Extract the full paper title, complete author list (all authors), year, and any venue/conference information. Also check if there's a BibTeX export link."
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-19T02:02:38.476853+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2509.05614",
  "prompt": "Extract the full paper title, complete author list (all authors), year, and any venue/conference information."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_bibtex_8_papers_20260519T020011",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2509.05614",
    "prompt": "Extract the full paper title, complete author list (all authors), year, and any venue/conference information."
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T02:02:38.476980+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2509.12594",
  "prompt": "Extract the full paper title, complete author list (all authors), year, and any venue/conference information."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_bibtex_8_papers_20260519T020011",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2509.12594",
    "prompt": "Extract the full paper title, complete author list (all authors), year, and any venue/conference information."
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-19T02:02:38.477102+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.08464",
  "prompt": "Extract the full paper title, complete author list (all authors), year, and any venue/conference information."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_bibtex_8_papers_20260519T020011",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2510.08464",
    "prompt": "Extract the full paper title, complete author list (all authors), year, and any venue/conference information."
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T02:02:38.477301+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2410.04417",
  "prompt": "Extract the full paper title, complete author list (all authors), year, and any venue/conference information."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_bibtex_8_papers_20260519T020011",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2410.04417",
    "prompt": "Extract the full paper title, complete author list (all authors), year, and any venue/conference information."
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-19T02:02:38.477433+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.17777",
  "prompt": "Extract the full paper title, complete author list (all authors), year, and any venue/conference information."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_bibtex_8_papers_20260519T020011",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2510.17777",
    "prompt": "Extract the full paper title, complete author list (all authors), year, and any venue/conference information."
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T02:02:38.477553+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2311.01378",
  "prompt": "Extract the full paper title, complete author list (all authors), year, and any venue/conference information."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_bibtex_8_papers_20260519T020011",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2311.01378",
    "prompt": "Extract the full paper title, complete author list (all authors), year, and any venue/conference information."
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T02:02:38.477684+00:00_

# Paper Details

**Full Title:** "SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning"

**Authors:** Hanzhen Wang, Jiaming Xu, Yushun Xiang, Jiayi Pan, Yongkang Zhou, Yong-Lu Li, Guohao Dai

**Year:** 2025 (submitted September 6, 2025; revised February 9, 2026)

**Venue/Conference Information:** No specific conference or venue is mentioned. The paper is categorized under Computer Vision and Pattern Recognition (cs.CV), Artificial Intelligence (cs.AI), and Robotics (cs.RO) on arXiv, but it appears to be a preprint without conference assignment details provided on this page.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_bibtex_8_papers_20260519T020011",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-19T02:02:38.477814+00:00_

# Paper Information

**Title:** "Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation"

**Authors:** Juntao Gao, Feiyang Ye, Jing Zhang, Wenjing Qian

**Year:** 2025 (submitted November 24, 2025)

**Venue/Conference:** No specific conference listed; this is a preprint on arXiv (identifier: 2511.18950)

**BibTeX Export:** Yes, a BibTeX export option is available on the page, though the actual formatted citation was not fully rendered in the content provided.

**Key Details:** The paper addresses computational efficiency in Vision-Language-Action (VLA) models for robotics, proposing a framework that "reduces FLOPs by 59% and the visual token count by over 3x" compared to baseline approaches while maintaining performance on benchmark tasks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_bibtex_8_papers_20260519T020011",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-19T02:02:38.477957+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "See What Matters Differentiable Grid Sample Pruning VLA arXiv 2605.11817"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_bibtex_8_papers_20260519T020011",
  "tool": "WebSearch",
  "tool_args": {
    "query": "See What Matters Differentiable Grid Sample Pruning VLA arXiv 2605.11817"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-19T02:02:38.478082+00:00_

# Paper Information

**Full Title:** "The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning"

**Complete Author List:** Titong Jiang, Xuefeng Jiang, Yuan Ma, Xin Wen, Bailin Li, Kun Zhan, Peng Jia, Yahui Liu, Sheng Sun, Xianpeng Lang

**Year:** 2025 (submitted September 16, 2025; revised September 21, 2025)

**Venue/Conference Information:** The paper is currently "Under review" with no specified conference. It is hosted on arXiv as preprint 2509.12594. The authors note a project site is available, though specific venue details are not listed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_bibtex_8_papers_20260519T020011",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T02:02:38.478265+00:00_

# Paper Information

**Full Title:** "Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered"

**Authors:** Jason Jabbour, Dong-Ki Kim, Max Smith, Jay Patrikar, Radhika Ghosal, Youhui Wang, Ali Agha, Vijay Janapa Reddi, Shayegan Omidshafiei

**Year:** 2025

**Venue/Conference Information:** Not specified. The paper was submitted to arXiv on October 9, 2025 (arXiv:2510.08464) and is categorized under Computer Science > Robotics and Machine Learning subdisciplines.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_bibtex_8_papers_20260519T020011",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-19T02:02:38.478433+00:00_

# Paper Information

**Full Title:** "SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference"

**Complete Author List:**
Yuan Zhang, Chun-Kai Fan, Junpeng Ma, Wenzhao Zheng, Tao Huang, Kuan Cheng, Denis Gudovskiy, Tomoyuki Okuno, Yohei Nakata, Kurt Keutzer, and Shanghang Zhang

**Year:** 2024 (submitted October 6, 2024; last revised June 3, 2025)

**Venue/Conference:** Accepted by ICML 2025 (International Conference on Machine Learning)

**arXiv Identifier:** arXiv:2410.04417

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_bibtex_8_papers_20260519T020011",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T02:02:38.478565+00:00_

# Paper Information

**Full Title:** "SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference"

**Complete Author List:**
1. Samir Khaki
2. Junxian Guo
3. Jiaming Tang
4. Shang Yang
5. Yukang Chen
6. Konstantinos N. Plataniotis
7. Yao Lu
8. Song Han
9. Zhijian Liu

**Year:** 2025 (submitted October 20, 2025)

**Venue/Conference Information:** No specific conference or venue is mentioned. The paper is classified under Computer Science > Computer Vision and Pattern Recognition (cs.CV) on arXiv, with identifier arXiv:2510.17777.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_bibtex_8_papers_20260519T020011",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-19T02:02:38.478689+00:00_

# Paper Details

**Full Title:** "Vision-Language Foundation Models as Effective Robot Imitators"

**Complete Author List:** Xinghang Li, Minghuan Liu, Hanbo Zhang, Cunjun Yu, Jie Xu, Hongtao Wu, Chilam Cheang, Ya Jing, Weinan Zhang, Huaping Liu, Hang Li, Tao Kong

**Year:** 2023 (submitted November 2, 2023; final revision February 5, 2024)

**Venue/Conference Information:** No specific conference venue is listed. This is an arXiv preprint (arXiv:2311.01378) in the Robotics (cs.RO) category with cross-listings in Artificial Intelligence and Machine Learning.

The abstract describes RoboFlamingo, a framework that "utilizes pre-trained VLMs for single-step vision-language comprehension, models sequential history information with an explicit policy head" for robot manipulation tasks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_bibtex_8_papers_20260519T020011",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T02:02:38.478839+00:00_

Web search results for query: "See What Matters Differentiable Grid Sample Pruning VLA arXiv 2605.11817"

Links: [{"title":"ICML Poster See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model","url":"https://icml.cc/virtual/2026/poster/65010"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/html/2509.12594v1"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/pdf/2509.12594"},{"title":"[2509.12594] The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/abs/2509.12594"},{"title":"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/pdf/2511.16449"}]

Based on the search results, I found information about the paper you're looking for:

"See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model" proposes the Differentiable Grid Sampler (GridS), a plug-and-play module that performs task-aware, continuous resampling of visual tokens in VLA models.

The paper addresses a fundamental trade-off in existing token pruning methods: aggressive compression using pruning inevitably discards critical geometric details like contact points, leading to severe performance degradation.

By adaptively predicting a minimal set of salient coordinates and extracting features via differentiable interpolation, GridS preserves essential spatial information while achieving drastic compression.

The paper was featured as an ICML 2026 poster presentation, addressing the challenge of high computational costs in Vision-Language-Action models that hinder real-time deployment in robotics applications.


REMINDER: You MUS
…[truncated 83 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_bibtex_8_papers_20260519T020011",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-19T02:02:38.479119+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://icml.cc/virtual/2026/poster/65010",
  "prompt": "Extract the full paper title, complete author list (all authors), and any arXiv ID or paper link for \"See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_bibtex_8_papers_20260519T020011",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://icml.cc/virtual/2026/poster/65010",
    "prompt": "Extract the full paper title, complete author list (all authors), and any arXiv ID or paper link for \"See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model\""
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-19T02:02:38.479378+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"See What Matters\" \"Differentiable Grid Sample Pruning\" arXiv authors complete list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_bibtex_8_papers_20260519T020011",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"See What Matters\" \"Differentiable Grid Sample Pruning\" arXiv authors complete list"
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-19T02:02:38.479568+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "RoboFlamingo \"Vision-Language Foundation Models as Effective Robot Imitators\" ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_bibtex_8_papers_20260519T020011",
  "tool": "WebSearch",
  "tool_args": {
    "query": "RoboFlamingo \"Vision-Language Foundation Models as Effective Robot Imitators\" ICLR 2024"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-19T02:02:38.479755+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SparseVILA \"Decoupling Visual Sparsity\" ICCV 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_bibtex_8_papers_20260519T020011",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SparseVILA \"Decoupling Visual Sparsity\" ICCV 2025"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-19T02:02:38.479917+00:00_

# Paper Information

**Full Title:** "See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model"

**Authors:** Yixu Feng, Zinan Zhao, Yanxiang Ma, Chenghao Xia, Chengbin Du, Yunke Wang, Chang Xu

**Paper Link:** A project page is available at https://fediory.github.io/Grid-Sampler/

**ArXiv ID:** Not provided in the webpage content

**Note:** The webpage indicates this is an ICML 2026 poster presentation, but no direct arXiv identifier or full paper PDF link is included in the available content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_bibtex_8_papers_20260519T020011",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-19T02:02:38.480082+00:00_

Web search results for query: "RoboFlamingo "Vision-Language Foundation Models as Effective Robot Imitators" ICLR 2024"

Links: [{"title":"Vision-Language Foundation Models as Effective Robot Imitators | OpenReview","url":"https://openreview.net/forum?id=lFYj0oibGR"},{"title":"[Quick Review] Vision-Language Foundation Models as Effective Robot Imitators","url":"https://liner.com/review/visionlanguage-foundation-models-as-effective-robot-imitators"},{"title":"ICLR Poster Vision-Language Foundation Models as Effective Robot Imitators","url":"https://iclr.cc/virtual/2024/poster/17943"},{"title":"[2311.01378] Vision-Language Foundation Models as Effective Robot Imitators","url":"https://arxiv.org/abs/2311.01378"},{"title":"RoboFlamingo | Vision-Language Foundation Models as Effective Robot Imitators","url":"https://roboflamingo.github.io/"},{"title":"RoboFlamingo: Enabling Vision-Language Models for Effective Robot Imitation","url":"https://www.azoai.com/news/20231108/RoboFlamingo-Enabling-Vision-Language-Models-for-Effective-Robot-Imitation.aspx"},{"title":"GitHub - RoboFlamingo/RoboFlamingo: Code for RoboFlamingo · GitHub","url":"https://github.com/RoboFlamingo/RoboFlamingo"},{"title":"Vision-Language Foundation Models as Effective Robot Imitators | alphaXiv","url":"https://www.alphaxiv.org/hi/overview/2311.01378v3"}]

Based on the search results, here's what I found about RoboFlamingo:

## Overview

RoboFlamingo is a vision-language manipulation framework built upon the open-source VLM OpenFlamingo, and it was presented as a poster at ICLR 2024.

## Key Features

RoboFlamingo utilizes pre-trained VLMs for single-step vision-language comprehension, models sequential history information with an explicit policy head, and is fine-tuned by imitation learning only on language-conditioned manipulation datasets. This decomposition provides RoboFlamingo flexibility for open-loop control and deployment on low-performance platforms.

## Performance

RoboFlamingo exceeds state-o
…[truncated 629 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_bibtex_8_papers_20260519T020011",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-19T02:02:38.480312+00:00_

Web search results for query: "SparseVILA "Decoupling Visual Sparsity" ICCV 2025"

Links: [{"title":"ICCV Poster SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference","url":"https://iccv.thecvf.com/virtual/2025/poster/1739"},{"title":"SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference","url":"https://arxiv.org/html/2510.17777v1"},{"title":"2025-10-21 SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference","url":"https://arxiv.org/pdf/2510.17777"},{"title":"[Literature Review] SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference","url":"https://www.themoonlight.io/en/review/sparsevila-decoupling-visual-sparsity-for-efficient-vlm-inference"},{"title":"SparseVILA: Decoupling Visual Sparsity for Efﬁcient VLM Inference Samir Khaki4","url":"https://www.openaccess.thecvf.com/content/ICCV2025/papers/Khaki_SparseVILA_Decoupling_Visual_Sparsity_for_Efficient_VLM_Inference_ICCV_2025_paper.pdf"},{"title":"Zhijian Liu","url":"https://zhijianliu.com/"},{"title":"[2510.17777] SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference","url":"https://arxiv.org/abs/2510.17777"},{"title":"SparseVILA-R1: Decoupling Visual Sparsity for Efficient VLM Reasoning","url":"https://openreview.net/pdf/6597aa03e44118e07d8bbbe91433da250c6beb33.pdf"}]

Here are the search results for SparseVILA "Decoupling Visual Sparsity" ICCV 2025:

## Overview

SparseVILA is a new paradigm for efficient VLM inference that decouples visual sparsity across the prefilling and decoding stages. Vision Language Models (VLMs) have rapidly advanced in integrating visual and textual reasoning, but their scalability remains limited by the growing number of visual tokens that dominate inference latency.

## Key Approach

SparseVILA distributes sparsity across stages by pruning redundant visual tokens during prefill and retrieving only query-relevant tokens during decoding. This decoupled design matches leading prefill pruning methods while preserving multi-t
…[truncated 748 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_bibtex_8_papers_20260519T020011",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-19T02:02:38.480563+00:00_

Web search results for query: ""See What Matters" "Differentiable Grid Sample Pruning" arXiv authors complete list"

Links: [{"title":"ICML Poster See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model","url":"https://icml.cc/virtual/2026/poster/65010"},{"title":"S2HPruner: Soft-to-Hard Distillation Bridges the Discretization Gap in   Pruning","url":"https://arxiv.org/pdf/2410.07046"},{"title":"Differentiable Network Pruning via Polarization of Probabilistic Channelwise Soft Masks","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9098282/"},{"title":"GridPrune: From \"Where to Look\" to \"What to Select\" in Visual Token Pruning for MLLMs","url":"https://arxiv.org/pdf/2511.10081"},{"title":"Differentiable Mask for Pruning Convolutional and Recurrent Networks","url":"https://arxiv.org/pdf/1909.04567"}]

The first result mentions "See What Matters: Differentiable Grid Sample Pruning" but doesn't provide the arXiv link or complete author list. Let me search more specifically for the arXiv paper.

Links: [{"title":"Determinantal point process attention over grid cell code supports out of distribution generalization","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11293867/"},{"title":"[2501.14143] An Extensive and Methodical Review of Smart Grids for Sustainable Energy Management-Addressing Challenges with AI, Renewable Energy Integration and Leading-edge Technologies","url":"https://arxiv.org/abs/2501.14143"},{"title":"[2509.16397] GRID: Graph-based Reasoning for Intervention and Discovery in Built Environments","url":"https://arxiv.org/abs/2509.16397"},{"title":"[2501.14143v1] An Extensive and Methodical Review of Smart Grids for Sustainable Energy Management-Addressing Challenges with AI, Renewable Energy Integration and Leading-edge Technologies","url":"https://arxiv.org/abs/2501.14143v1"},{"title":"GRIDSS: sensitive and specific genomic rearrangement detection using positional de Bruijn graph assembly","url":"http
…[truncated 5822 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_bibtex_8_papers_20260519T020011",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-19T02:02:38.480769+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.11817",
  "prompt": "Extract the full paper title, complete author list (all authors), year, submission date, and any venue/conference information."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_bibtex_8_papers_20260519T020011",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2605.11817",
    "prompt": "Extract the full paper title, complete author list (all authors), year, submission date, and any venue/conference information."
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-19T02:02:38.480905+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://fediory.github.io/Grid-Sampler/",
  "prompt": "Extract the full paper title, complete author list (all authors), arXiv ID, and any venue/conference information for \"See What Matters\"."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_bibtex_8_papers_20260519T020011",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://fediory.github.io/Grid-Sampler/",
    "prompt": "Extract the full paper title, complete author list (all authors), arXiv ID, and any venue/conference information for \"See What Matters\"."
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-19T02:02:38.481041+00:00_

# Paper Information

**Full Title:** "See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model"

**Authors:** Yixu Feng, Zinan Zhao, Yanxiang Ma, Chenghao Xia, Chengbin Du, Yunke Wang, Chang Xu

**Year:** 2026

**Submission Date:** May 12, 2026 (v1); revised May 17, 2026 (v2)

**Venue/Conference:** Proceedings of the Forty-third International Conference on Machine Learning, 2026

**arXiv Identifier:** 2605.11817

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_bibtex_8_papers_20260519T020011",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-19T02:02:38.481220+00:00_

# Paper Information: "See What Matters"

**Full Title:** "See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model"

**Complete Author List:**
Yixu Feng, Zinan Zhao, Yanxiang Ma, Chenghao Xia, Chengbin Du, Yunke Wang, Chang Xu

**ArXiv ID:** 2605.11817

**Venue/Conference:** Forty-Third International Conference on Machine Learning (ICML) 2026

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_bibtex_8_papers_20260519T020011",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-19T02:02:38.481410+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LightVLA arXiv 2509.12594 \"ICRA 2026\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_bibtex_8_papers_20260519T020011",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LightVLA arXiv 2509.12594 \"ICRA 2026\""
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-19T02:02:38.481539+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2511.18950",
  "prompt": "Extract ALL authors listed on this paper. I need the complete author list, not abbreviated. List every single author name."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_bibtex_8_papers_20260519T020011",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2511.18950",
    "prompt": "Extract ALL authors listed on this paper. I need the complete author list, not abbreviated. List every single author name."
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-19T02:02:38.481664+00:00_

# Authors of arXiv:2511.18950

Based on the paper content, the complete author list is:

1. Juntao Gao
2. Feiyang Ye
3. Jing Zhang
4. Wenjing Qian

The paper indicates "by Juntao Gao and 3 other authors," and these four names are the only individual authors explicitly identified in the document.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_bibtex_8_papers_20260519T020011",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-19T02:02:38.481814+00:00_

Web search results for query: "LightVLA arXiv 2509.12594 "ICRA 2026""

Links: [{"title":"GitHub - LiAutoAD/LightVLA: Official Code for LightVLA (ICRA 2026)","url":"https://github.com/LiAutoAD/LightVLA"},{"title":"[2509.12594] The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/abs/2509.12594"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/pdf/2509.12594"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/html/2509.12594"},{"title":"Beyond Training-Free Pruning: LightVLA Introduces Differentiable Token Pruning and Achieves a Dual Breakthrough in the Performance and Efficiency of VLA Models for the First Time | by Beck Moulton | Medium","url":"https://beckmoulton.medium.com/beyond-training-free-pruning-lightvla-introduces-differentiable-token-pruning-and-achieves-a-dual-7b2f562b0ab8"},{"title":"LightVLA/LIBERO.md at main · LiAutoAD/LightVLA","url":"https://github.com/LiAutoAD/LightVLA/blob/main/LIBERO.md"}]

Based on the search results, here's what I found about LightVLA:

LightVLA is a simple yet effective differentiable token pruning framework for vision-language-action (VLA) models. While VLA models have shown impressive capability in executing real-world robotic tasks, their deployment on resource-constrained platforms is often bottlenecked by the heavy attention-based computation over large sets of visual tokens.

LightVLA addresses this challenge through adaptive, performance-driven pruning of visual tokens by generating dynamic queries to evaluate visual token importance and adopting Gumbel softmax to enable differentiable token selection, learning to preserve the most informative visual tokens while pruning tokens which do not contribute 
…[truncated 474 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_bibtex_8_papers_20260519T020011",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-19T02:02:38.481994+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2511.18950",
  "prompt": "Extract the COMPLETE author list with ALL author names. I need every single author, their full names and affiliations if available."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_bibtex_8_papers_20260519T020011",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2511.18950",
    "prompt": "Extract the COMPLETE author list with ALL author names. I need every single author, their full names and affiliations if available."
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-19T02:02:38.482149+00:00_

# Complete Author List for Compressor-VLA

Based on the document provided, here are all listed authors:

**Primary Authors:**
1. Juntao Gao (School of Information Science and Technology, Beijing University of Technology; LiAuto Inc.)
2. Feiyang Ye (LiAuto Inc.)
3. Jing Zhang (School of Information Science and Technology, Beijing University of Technology; Beijing Key Laboratory of Computational Intelligence and Intelligent System)
4. Wenjing Qian (School of Information Science and Technology, Beijing University of Technology)

The document notes that Jing Zhang is the corresponding author. The paper explicitly lists these four individuals by name with their institutional affiliations clearly provided in the header section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_bibtex_8_papers_20260519T020011",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-19T02:02:38.482386+00:00_

All data collected. Here's the complete BibTeX block:

```bibtex
@article{gao2025compressorvla,
  title={Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation},
  author={Gao, Juntao and Ye, Feiyang and Zhang, Jing and Qian, Wenjing},
  journal={arXiv preprint arXiv:2511.18950},
  year={2025},
  eprint={2511.18950},
  archivePrefix={arXiv},
  url={https://arxiv.org/abs/2511.18950}
}

@article{wang2025specprunevla,
  title={SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning},
  author={Wang, Hanzhen and Xu, Jiaming and Xiang, Yushun and Pan, Jiayi and Zhou, Yongkang and Li, Yong-Lu and Dai, Guohao},
  journal={arXiv preprint arXiv:2509.05614},
  year={2025},
  eprint={2509.05614},
  archivePrefix={arXiv},
  url={https://arxiv.org/abs/2509.05614}
}

@inproceedings{jiang2026lightvla,
  title={The Better You Learn, The Smarter You Prune: Towards Efficient Vision-Language-Action Models via Differentiable Token Pruning},
  author={Jiang, Titong and Jiang, Xuefeng and Ma, Yuan and Wen, Xin and Li, Bailin and Zhan, Kun and Jia, Peng and Liu, Yahui and Sun, Sheng and Lang, Xianpeng},
  booktitle={Proceedings of the IEEE International Conference on Robotics and Automation (ICRA)},
  year={2026},
  eprint={2509.12594},
  archivePrefix={arXiv},
  url={https://arxiv.org/abs/2509.12594}
}

@inproceedings{feng2026seewhatmatters,
  title={See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model},
  author={Feng, Yixu and Zhao, Zinan and Ma, Yanxiang and Xia, Chenghao and Du, Chengbin and Wang, Yunke and Xu, Chang},
  booktitle={Proceedings of the Forty-Third International Conference on Machine Learning (ICML)},
  year={2026},
  eprint={2605.11817},
  archivePrefix={arXiv},
  url={https://arxiv.org/abs/2605.11817}
}

@article{jabbour2025dontrun,
  title={Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered},
  author={Jabbour, Jason and Kim, Dong-Ki and Smith, Max and Patrikar, Jay and Ghosal, Radhika and Wang, Youhui and Agha, Ali and Janapa Reddi, Vijay and Omidshafiei, Shayegan},
  journal={arXiv preprint arXiv:2510.08464},
  year={2025},
  eprint={2510.08464},
  archivePrefix={arXiv},
  url={https://arxiv.org/abs/2510.08464}
}

@inproceedings{zhang2025sparsevlm,
  title={SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference},
  author={Zhang, Yuan and Fan, Chun-Kai and Ma, Junpeng and Zheng, Wenzhao and Huang, Tao and Cheng, Kuan and Gudovskiy, Denis and Okuno, Tomoyuki and Nakata, Yohei and Keutzer, Kurt and Zhang, Shanghang},
  booktitle={Proceedings of the Forty-Second International Conference on Machine Learning (ICML)},
  year={2025},
  eprint={2410.04417},
  archivePrefix={arXiv},
  url={https://arxiv.org/abs/2410.04417}
}

@inproceedings{khaki2025sparsevila,
  title={SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference},
  author={Khaki, Samir and Guo, Junxian and Tang, Jiaming and Yang, Shang and Chen, Yukang and Plataniotis, Konstantinos N. and Lu, Yao and Han, Song and Liu, Zhijian},
  booktitle={Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)},
  year={2025},
  eprint={2510.17777},
  archivePrefix={arXiv},
  url={https://arxiv.org/abs/2510.17777}
}

@inproceedings{li2024roboflamingo,
  title={Vision-Language Foundation Models as Effective Robot Imitators},
  author={Li, Xinghang and Liu, Minghuan and Zhang, Hanbo and Yu, Cunjun and Xu, Jie and Wu, Hongtao and Cheang, Chilam and Jing, Ya and Zhang, Weinan and Liu, Huaping and Li, Hang and Kong, Tao},
  booktitle={Proceedings of the Twelfth International Conference on Learning Representations (ICLR)},
  year={2024},
  eprint={2311.01378},
  archivePrefix={arXiv},
  url={https://arxiv.org/abs/2311.01378}
}
```

数据来源汇总:
- 6 篇直接从 arXiv abs 页面获取完整作者列表
- SparseVILA ICCV 2025 确认来自 [CVF proceedings](https://www.openaccess.thecvf.com/content/ICCV2025/papers/Khaki_SparseVILA_Decoupling_Visual_Sparsity_for_Efficient_VLM_Inference_ICCV_2025_paper.pdf)
- RoboFlamingo ICLR 2024 确认来自 [OpenReview](https://openreview.net/forum?id=lFYj0oibGR) 和 [ICLR virtual](https://iclr.cc/virtual/2024/poster/17943)
- LightVLA ICRA 2026 确认来自 [GitHub repo](https://github.com/LiAutoAD/LightVLA)
- See What Matters 从 [arXiv 2605.11817](https://arxiv.org/abs/2605.11817) 和 [ICML poster](https://icml.cc/virtual/2026/poster/65010) 获取

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_bibtex_8_papers_20260519T020011"
}
```

</details>

---
