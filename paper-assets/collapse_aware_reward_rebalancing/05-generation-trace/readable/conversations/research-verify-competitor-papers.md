# research verify competitor papers

**Does Reward Curation Kill Diversity? Systematic Evidence of Surprising Resilience in Iterative Self-Training** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/chats/worker_research_verify_competitor_papers_20260517T012158.jsonl`
- **Structured JSON:** [`133b61aa282cedc70eaf.json`](../../sessions/13/133b61aa282cedc70eaf.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

13 recorded events

### Tool call

_source line 1 · 2026-05-17T01:22:53.678340+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_verify_competitor_papers_20260517T012158",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-17T01:22:53.678628+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_verify_competitor_papers_20260517T012158",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T01:22:53.678842+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2501.00747 DIVE Diversified Iterative Self-Improvement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_verify_competitor_papers_20260517T012158",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2501.00747 DIVE Diversified Iterative Self-Improvement"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-17T01:22:53.679000+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2509.02534 DARLING Jointly Reinforcing Diversity Quality"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_verify_competitor_papers_20260517T012158",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2509.02534 DARLING Jointly Reinforcing Diversity Quality"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T01:22:53.679131+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2501.11463 CD-RLHF Curiosity-Driven RLHF"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_verify_competitor_papers_20260517T012158",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2501.11463 CD-RLHF Curiosity-Driven RLHF"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-17T01:22:53.679252+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2408.16673 GEM Preserving Diversity Supervised Fine-Tuning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_verify_competitor_papers_20260517T012158",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2408.16673 GEM Preserving Diversity Supervised Fine-Tuning"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T01:22:53.679369+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2310.06452 Kirk Understanding Effects RLHF Diversity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_verify_competitor_papers_20260517T012158",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2310.06452 Kirk Understanding Effects RLHF Diversity"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-17T01:22:53.679528+00:00_

Web search results for query: "arxiv 2509.02534 DARLING Jointly Reinforcing Diversity Quality"

Links: [{"title":"[2509.02534] Jointly Reinforcing Diversity and Quality in Language Model Generations","url":"https://arxiv.org/abs/2509.02534"},{"title":"Jointly Reinforcing Diversity and Quality in Language Model Generations","url":"https://arxiv.org/pdf/2509.02534"},{"title":"Paper page - Jointly Reinforcing Diversity and Quality in Language Model Generations","url":"https://huggingface.co/papers/2509.02534"},{"title":"GitHub - facebookresearch/darling: Official Implementation of the paper \"Jointly Reinforcing Diversity and Quality in Language Model Generations\" · GitHub","url":"https://github.com/facebookresearch/darling"},{"title":"Jointly Reinforcing Diversity and Quality in Language Model Generations","url":"https://arxiviq.substack.com/p/jointly-reinforcing-diversity-and"},{"title":"[Literature Review] Jointly Reinforcing Diversity and Quality in Language Model Generations","url":"https://www.themoonlight.io/en/review/jointly-reinforcing-diversity-and-quality-in-language-model-generations"},{"title":"Quality & Diversity in LLM Generations","url":"https://www.emergentmind.com/papers/2509.02534"},{"title":"Jointly Reinforcing Diversity and Quality in Language Model Generations | Request PDF","url":"https://www.researchgate.net/publication/395213889_Jointly_Reinforcing_Diversity_and_Quality_in_Language_Model_Generations"},{"title":"Jointly Reinforcing Diversity and Quality in Language ...","url":"https://www.alphaxiv.org/overview/2509.02534"},{"title":"RLVR DARLING: Reinforcing Diversity & Quality in LLM Generations (Paper Club Oct 15) - YouTube","url":"https://www.youtube.com/watch?v=OXRxUZ-0XFo"}]

Based on the search results, here's what I found about arxiv paper 2509.02534:

## Paper Overview

The paper introduces Diversity-Aware Reinforcement Learning (DARLING), a framework that jointly optimizes for response quality and semantic diversity.

## The Problem

P
…[truncated 1439 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_verify_competitor_papers_20260517T012158",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-17T01:22:53.679731+00:00_

Web search results for query: "arxiv 2501.00747 DIVE Diversified Iterative Self-Improvement"

Links: [{"title":"[2501.00747] DIVE: Diversified Iterative Self-Improvement","url":"https://arxiv.org/abs/2501.00747"},{"title":"DIVE: Diversified Iterative Self-Improvement","url":"https://arxiv.org/html/2501.00747v1"},{"title":"DIVE: Diversified Iterative Self-Improvement","url":"https://openreview.net/pdf?id=tb0kyytZqF"},{"title":"Diverse, not Short: A Length-Controlled Self-Learning Framework for Improving Response Diversity of Language Models","url":"https://arxiv.org/html/2505.16245v1"},{"title":"DIVER: Reinforced Diffusion Breaks Imitation Bottlenecks in End-to-End Autonomous Driving","url":"https://arxiv.org/html/2507.04049v3"},{"title":"[2303.12743] Diversified and Realistic 3D Augmentation via Iterative Construction, Random Placement, and HPR Occlusion","url":"https://ar5iv.labs.arxiv.org/html/2303.12743"},{"title":"[2501.05707] Multiagent Finetuning: Self Improvement with Diverse Reasoning Chains","url":"https://arxiv.org/abs/2501.05707"},{"title":"Agent-R\\xspace: Training Language Model Agents to Reflect via Iterative Self-Training","url":"https://arxiv.org/html/2501.11425v3"},{"title":"Computer Science Jan 2025","url":"https://www.arxiv.org/list/cs/2025-01?skip=8100&show=2000"},{"title":"[2501.05707v1] Multiagent Finetuning: Self Improvement with Diverse Reasoning Chains","url":"https://arxiv.org/abs/2501.05707v1"}]

Based on the search results, here's what I found about the paper arxiv 2501.00747:

DIVE (Diversified Iterative Self-Improvement) is a novel framework that addresses the challenge of diversity loss in iterative self-improvement through two key components: Sample Pool Expansion for broader solution exploration, and Data Selection for balancing diversity and quality in preference pairs.

The paper identifies that continuous training on self-generated data leads to reduced output diversity, which is particularly critical in reasoning tasks where dive
…[truncated 856 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_verify_competitor_papers_20260517T012158",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T01:22:53.679924+00:00_

Web search results for query: "arxiv 2310.06452 Kirk Understanding Effects RLHF Diversity"

Links: [{"title":"[2310.06452] Understanding the Effects of RLHF on LLM Generalisation and Diversity","url":"https://arxiv.org/abs/2310.06452"},{"title":"[2310.06452] Understanding the Effects of RLHF on LLM Generalisation and Diversity","url":"https://ar5iv.labs.arxiv.org/html/2310.06452"},{"title":"Understanding the Effects of RLHF on LLM Generalisation and Diversity | Trending arXiv papers – Ribbit Ribbit","url":"https://ribbitribbit.co/paper/arxiv.2310.06452-Understanding-the-Effects-of-RLHF-on-LLM-Generalisation"},{"title":"[2310.06452v1] Understanding the Effects of RLHF on LLM Generalisation and Diversity","url":"https://arxiv.org/abs/2310.06452v1"},{"title":"Understanding the Effects of RLHF on LLM Generalisation and Diversity","url":"https://arxiv.org/html/2310.06452v2"},{"title":"Understanding the Effects of RLHF on LLM Generalisation ...","url":"https://arxiv.org/pdf/2310.06452"},{"title":"[PDF] Understanding the Effects of RLHF on LLM Generalisation and Diversity | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Understanding-the-Effects-of-RLHF-on-LLM-and-Kirk-Mediratta/cb3968152f7d93f53d24b00279a90d5071ddc85a"},{"title":"Understanding the Effects of RLHF on LLM Generalisation and - a UCL-DARK Collection","url":"https://huggingface.co/collections/UCL-DARK/understanding-the-effects-of-rlhf-on-llm-generalisation-and"},{"title":"Understanding the Effects of RLHF on LLM Generalisation and Diversity | OpenReview","url":"https://openreview.net/forum?id=PXD3FAVHJT"},{"title":"RLHF Effects on LLM Generalisation & Diversity","url":"https://www.emergentmind.com/papers/2310.06452"}]

Based on the search results, here's information about arxiv 2310.06452:

## Paper Overview

This paper is titled "Understanding the Effects of RLHF on LLM Generalisation and Diversity" and was authored by Robert Kirk, Ishita Mediratta, Christoforos Nalmpantis, Jelena Luketina, Er
…[truncated 1006 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_verify_competitor_papers_20260517T012158",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-17T01:22:53.680100+00:00_

Web search results for query: "arxiv 2501.11463 CD-RLHF Curiosity-Driven RLHF"

Links: [{"title":"[2501.11463] Curiosity-Driven Reinforcement Learning from Human Feedback","url":"https://arxiv.org/abs/2501.11463"},{"title":"GitHub - ernie-research/CD-RLHF: Official code of curiosity-driven RLHF","url":"https://github.com/ernie-research/CD-RLHF"},{"title":"Curiosity-Driven Reinforcement Learning from Human Feedback","url":"https://arxiv.org/html/2501.11463"},{"title":"Curiosity-Driven Reinforcement Learning from Human ...","url":"https://arxiv.org/pdf/2501.11463"},{"title":"Paper page - Curiosity-Driven Reinforcement Learning from Human Feedback","url":"https://huggingface.co/papers/2501.11463"},{"title":"The Hidden Link Between RLHF and Contrastive Learning","url":"https://arxiv.org/html/2506.22578v1"},{"title":"[2504.12501] Reinforcement Learning from Human Feedback","url":"https://arxiv.org/abs/2504.12501"},{"title":"Reinforcement Learning from Human Feedback","url":"https://arxiv.org/html/2504.12501v3"},{"title":"Investigating Curiosity-Driven Behavior in Virtual ...","url":"https://arxiv.org/pdf/2501.04905"},{"title":"[1808.04355] Large-Scale Study of Curiosity-Driven Learning","url":"https://arxiv.org/abs/1808.04355"}]

I found the paper arxiv 2501.11463 "Curiosity-Driven Reinforcement Learning from Human Feedback." Here's what I found:

## Overview

This paper addresses a key challenge in RLHF: while it effectively aligns large language models with human preferences, it often reduces output diversity. This trade-off between diversity and alignment quality is a significant challenge.

## The CD-RLHF Framework

The researchers introduce curiosity-driven RLHF (CD-RLHF), a framework that incorporates intrinsic rewards for novel states, alongside traditional sparse extrinsic rewards, to optimize both output diversity and alignment quality.

Curiosities are implemented as intrinsic rewards and assigned along the trajectory. Combining intrinsic rewards with the extri
…[truncated 894 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_verify_competitor_papers_20260517T012158",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-17T01:22:53.680265+00:00_

Web search results for query: "arxiv 2408.16673 GEM Preserving Diversity Supervised Fine-Tuning"

Links: [{"title":"[2408.16673] Preserving Diversity in Supervised Fine-Tuning of Large Language Models","url":"https://arxiv.org/abs/2408.16673"},{"title":"Preserving Diversity in Supervised Fine-Tuning of Large Language Models","url":"https://arxiv.org/html/2408.16673v2"},{"title":"Preserving Diversity in Supervised Fine-Tuning of Large Language Models | alphaXiv","url":"https://www.alphaxiv.org/abs/2408.16673"},{"title":"GitHub - liziniu/GEM: Code for Paper (Preserving Diversity in Supervised Fine-tuning of Large Language Models)","url":"https://github.com/liziniu/GEM"},{"title":"Entropic Distribution Matching in Supervised Fine-tuning of LLMs: Less Overfitting and Better Diversity","url":"https://arxiv.org/html/2408.16673v1"},{"title":"[2408.16673v1] Entropic Distribution Matching in Supervised Fine-tuning of LLMs: Less Overfitting and Better Diversity","url":"http://www.arxiv.org/abs/2408.16673v1"},{"title":"SED-SFT: Selectively Encouraging Diversity in Supervised Fine-Tuning","url":"https://arxiv.org/html/2602.07464"},{"title":"Preserving Diversity in Supervised Fine-Tuning of Large Language Models | OpenReview","url":"https://openreview.net/forum?id=NQEe7B7bSw"},{"title":"Entropic Distribution Matching in Supervised Fine-tuning of ...","url":"https://arxiv.org/pdf/2408.16673"},{"title":"Proximal Supervised Fine-Tuning","url":"https://arxiv.org/html/2508.17784v1"}]

Based on the search results, I found the arXiv paper you requested. Here's what I found:

## Paper Overview

The paper titled "Preserving Diversity in Supervised Fine-Tuning of Large Language Models" is arXiv paper 2408.16673.

## Key Contributions

Large Language Models (LLMs) typically rely on Supervised Fine-Tuning (SFT) to specialize in downstream tasks, with the Cross Entropy (CE) loss being the de facto choice. However, CE maximizes the likelihood of observed data without accounting for alternativ
…[truncated 1369 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_verify_competitor_papers_20260517T012158",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-17T01:22:53.680484+00:00_

全部 5 篇论文验证完毕，结果如下：

---

## 验证结果

### 1. DIVE: Diversified Iterative Self-Improvement — arXiv 2501.00747
**✅ 真实**

- 实际标题：*DIVE: Diversified Iterative Self-Improvement*（完全匹配）
- 作者：Yiwei Qin, Yixiu Liu, Pengfei Liu
- 日期：2025年1月
- Venue：也见于 OpenReview
- 相关性：直接竞品——解决迭代自改进中多样性丧失问题，通过 Sample Pool Expansion + Data Selection 平衡多样性与质量

### 2. DARLING: Jointly Reinforcing Diversity and Quality — arXiv 2509.02534
**✅ 真实**

- 实际标题：*Jointly Reinforcing Diversity and Quality in Language Model Generations*（DARLING = Diversity-Aware Reinforcement Learning）
- 来源：Facebook Research（有官方 GitHub: facebookresearch/darling）
- 日期：2025年9月（当前2026年5月，时间合理）
- 相关性：**最直接的竞品**——在 online RL 阶段联合优化质量和语义多样性，用 learned partition function 度量多样性

### 3. CD-RLHF: Curiosity-Driven RLHF — arXiv 2501.11463
**✅ 真实**

- 实际标题：*Curiosity-Driven Reinforcement Learning from Human Feedback*（完全匹配）
- 来源：Ernie Research (Baidu)，有官方 GitHub: ernie-research/CD-RLHF
- 日期：2025年1月
- 相关性：直接竞品——用 intrinsic curiosity reward 在 RLHF 中保持多样性，同时维持对齐质量

### 4. GEM: Preserving Diversity in Supervised Fine-Tuning — arXiv 2408.16673
**⚠️ 真实，但标题表述略有出入**

- 实际标题 v2：*Preserving Diversity in Supervised Fine-Tuning of Large Language Models*
- 实际标题 v1：*Entropic Distribution Matching in Supervised Fine-tuning of LLMs: Less Overfitting and Better Diversity*
- GEM 是算法名称，非论文标题的一部分
- 有官方 GitHub: liziniu/GEM
- 日期：2024年8月
- 相关性：高度相关——game-theoretic formulation 用 reverse KL + entropy regularization 在 SFT 阶段保留多样性

### 5. Kirk et al.: Understanding Effects of RLHF on Diversity — arXiv 2310.06452
**✅ 真实**

- 实际标题：*Understanding the Effects of RLHF on LLM Generalisation and Diversity*（完全匹配）
- 作者：Robert Kirk, Ishita Mediratta, Christoforos Nalmpantis, Jelena Luketina, Eric Hambro, Edward Grefenstette, Roberta Raileanu
- 日期：2023年10月，发表于 ICLR（见 OpenReview）
- 相关性：基础性分析论文——实证发现 RLHF 显著降低输出多样性，建立了 generalisation vs. diversity 的 tradeoff，是我们工作的动机来源之一

---

## 总结

5/5 论文均真实存在，无幻觉。仅 GEM 的标题表述需微调（GEM 是算法名而非论文标题的一部分）。DARLING 的 2509 时间戳确认合理（2025年9月，Facebook Research 出品）。

Sources:
- [DIVE](https://arxiv.org/abs/2501.00747)
- [DARLING](https://arxiv.org/abs/2509.02534)
- [CD-RLHF](https://arxiv.org/abs/2501.11463)
- [GEM](https://arxiv.org/abs/2408.16673)
- [Kirk et al.](https://arxiv.org/abs/2310.06452)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_verify_competitor_papers_20260517T012158"
}
```

</details>

---
