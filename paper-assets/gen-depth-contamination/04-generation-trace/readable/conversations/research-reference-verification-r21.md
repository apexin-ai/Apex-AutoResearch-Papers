# research reference verification r21

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/chats/worker_research_reference_verification_r21_20260520T150819.jsonl`
- **Structured JSON:** [`dbe8721826726124c134.json`](../../sessions/db/dbe8721826726124c134.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

11 recorded events

### Tool call

_source line 1 · 2026-05-20T15:09:18.384275+00:00_

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
  "session": "worker_research_reference_verification_r21_20260520T150819",
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

_source line 2 · 2026-05-20T15:09:18.384586+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_verification_r21_20260520T150819",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T15:09:18.384762+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL 2025 Anthology 2025.acl-long.624 \"Unveiling Attractor Cycles\" paraphrasing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_verification_r21_20260520T150819",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL 2025 Anthology 2025.acl-long.624 \"Unveiling Attractor Cycles\" paraphrasing"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-20T15:09:18.384918+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2512.05311 \"The Erosion of LLM Signatures\" Shahriar"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_verification_r21_20260520T150819",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2512.05311 \"The Erosion of LLM Signatures\" Shahriar"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-20T15:09:18.385075+00:00_

Web search results for query: "ACL 2025 Anthology 2025.acl-long.624 "Unveiling Attractor Cycles" paraphrasing"

Links: [{"title":"Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.624/"},{"title":"Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing | Request PDF","url":"https://www.researchgate.net/publication/394299645_Unveiling_Attractor_Cycles_in_Large_Language_Models_A_Dynamical_Systems_View_of_Successive_Paraphrasing"},{"title":"Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing","url":"https://arxiv.org/html/2502.15208v1"},{"title":"Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing","url":"https://arxiv.org/pdf/2502.15208"},{"title":"Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing [Quick Review]","url":"https://liner.com/review/unveiling-attractor-cycles-in-large-language-models-dynamical-systems-view"},{"title":"Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing | OpenReview","url":"https://openreview.net/forum?id=553Utbsoyi"},{"title":"[2502.15208] Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing","url":"https://arxiv.org/abs/2502.15208"}]

I found the paper! Here's information about ACL 2025 Anthology paper 2025.acl-long.624:

**Title:** "Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing"

**Authors:** Wang, Zhilin and Li, Yafu and Yan, Jianhao and Cheng, Yu and Zhang, Yue

**Main Findings:**

While LLMs are expected to explore diverse paraphrases, successive paraphrasing converges to stable periodic states like 2-period attractor cycles, limiting linguistic divers
…[truncated 704 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_verification_r21_20260520T150819",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T15:09:18.385252+00:00_

Web search results for query: "arXiv 2512.05311 "The Erosion of LLM Signatures" Shahriar"

Links: [{"title":"[2512.05311] The Erosion of LLM Signatures: Can We Still Distinguish Human and LLM-Generated Scientific Ideas After Iterative Paraphrasing?","url":"https://arxiv.org/abs/2512.05311"},{"title":"The Erosion of LLM Signatures: Can We Still Distinguish Human and LLM-Generated Scientific Ideas After Iterative Paraphrasing?","url":"https://arxiv.org/html/2512.05311v1"},{"title":"The Erosion of LLM Signatures: Can We Still Distinguish Human and","url":"https://www.arxiv.org/pdf/2512.05311"},{"title":"Representation-Aware Unlearning via Activation Signatures: From Suppression to Knowledge-Signature Erasure","url":"https://arxiv.org/pdf/2601.10566"},{"title":"Exposing Pink Slime Journalism: Linguistic Signatures and Robust Detection Against LLM-Generated Threats","url":"https://arxiv.org/html/2512.05331"},{"title":"Intrinsic Fingerprint of LLMs: Continue Training is NOT All You Need to Steal A Model!","url":"https://arxiv.org/pdf/2507.03014"},{"title":"[2512.05331] Exposing Pink Slime Journalism: Linguistic Signatures and Robust Detection Against LLM-Generated Threats","url":"https://arxiv.org/abs/2512.05331"}]

I found the paper you were looking for! Here are the key details about arXiv paper 2512.05311:

**Title:** "The Erosion of LLM Signatures: Can We Still Distinguish Human and LLM-Generated Scientific Ideas After Iterative Paraphrasing?"

**Authors:** Sadat Shahriar, Navid Ayoobi, and Arjun Mukherjee from the University of Houston, Texas, USA

**Submission Date:** December 4, 2025

**Key Research Focus:** The paper addresses how to distinguish between LLM and human-generated ideas, which remains an unexplored area despite extensive research on detecting LLM-generated text.

**Main Findings:** The researchers found that state-of-the-art models face significant challenges in source attribution, with detection performance declining by an average of 25.4% after five
…[truncated 486 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_verification_r21_20260520T150819",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T15:09:18.385442+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:aclanthology.org 2025.acl-long.624 abstract authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_verification_r21_20260520T150819",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:aclanthology.org 2025.acl-long.624 abstract authors"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-20T15:09:18.385571+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2512.05311 \"Erosion of LLM Signatures\" abstract full authors \"25.4\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_verification_r21_20260520T150819",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2512.05311 \"Erosion of LLM Signatures\" abstract full authors \"25.4\""
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-20T15:09:18.385707+00:00_

Web search results for query: "site:aclanthology.org 2025.acl-long.624 abstract authors"

Links: [{"title":"Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.624/"},{"title":"DeCAP: Context-Adaptive Prompt Generation for Debiasing Zero-shot Question Answering in Large Language Models - ACL Anthology","url":"https://aclanthology.org/2025.naacl-long.624/"},{"title":"Doing Things with Words: Rethinking Theory of Mind Simulation in Large Language Models - ACL Anthology","url":"https://aclanthology.org/2025.clicit-1.59/"},{"title":"Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.0/"},{"title":"Pragmatics in the Era of Large Language Models: A Survey on Datasets, Evaluation, Opportunities and Challenges - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.425/"}]

Based on the search results, I found the paper you're looking for:

**Title:** Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing

**Authors:** Wang, Zhilin and Li, Yafu and Yan, Jianhao and Cheng, Yu and Zhang, Yue

**Abstract:** Dynamical systems theory provides a framework for analyzing iterative processes and evolution over time.

The paper is published in the Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL 2025) and appears on pages 12740-12755.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_verification_r21_20260520T150819",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T15:09:18.385883+00:00_

Web search results for query: "arxiv 2512.05311 "Erosion of LLM Signatures" abstract full authors "25.4""

Links: [{"title":"[2512.05311] The Erosion of LLM Signatures: Can We Still Distinguish Human and LLM-Generated Scientific Ideas After Iterative Paraphrasing?","url":"https://arxiv.org/abs/2512.05311"},{"title":"The Erosion of LLM Signatures: Can We Still Distinguish Human and","url":"https://www.arxiv.org/pdf/2512.05311"},{"title":"The Erosion of LLM Signatures: Can We Still Distinguish Human and LLM-Generated Scientific Ideas After Iterative Paraphrasing?","url":"https://arxiv.org/html/2512.05311"},{"title":"Representation-Aware Unlearning via Activation Signatures: From Suppression to Knowledge-Signature Erasure","url":"https://arxiv.org/pdf/2601.10566"},{"title":"Exposing Pink Slime Journalism: Linguistic Signatures and Robust Detection Against LLM-Generated Threats","url":"https://arxiv.org/html/2512.05331"},{"title":"Intrinsic Fingerprint of LLMs: Continue Training is NOT All You Need to Steal A Model!","url":"https://arxiv.org/pdf/2507.03014"},{"title":"MEraser: An Effective Fingerprint Erasure Approach for Large Language Models","url":"https://arxiv.org/html/2506.12551v1"}]

Based on the search results, here's the information about arXiv paper 2512.05311:

**Title:** The Erosion of LLM Signatures: Can We Still Distinguish Human and LLM-Generated Scientific Ideas After Iterative Paraphrasing?

**Authors:** Sadat Shahriar, Navid Ayoobi, Arjun Mukherjee

**Abstract:** With the increasing reliance on LLMs as research agents, distinguishing between LLM and human-generated ideas has become crucial for understanding the cognitive nuances of LLMs' research capabilities. While detecting LLM-generated text has been extensively studied, distinguishing human vs LLM-generated scientific idea remains an unexplored area. In this work, the researchers systematically evaluate the ability of state-of-the-art machine learning models to differentiate between human and LLM-g
…[truncated 497 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_verification_r21_20260520T150819",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-20T15:09:18.386085+00:00_

## 验证结果

---

### 1. Wang et al. (ACL 2025) — ✅ 验证通过

| 项目 | 结果 |
|------|------|
| **Anthology ID** | `2025.acl-long.624` ✅ 存在 |
| **URL** | https://aclanthology.org/2025.acl-long.624/ |
| **arXiv** | https://arxiv.org/abs/2502.15208 |
| **实际 Title** | "Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing" ✅ 与声称一致 |
| **作者** | Zhilin Wang, Yafu Li, Jianhao Yan, Yu Cheng, Yue Zhang |
| **发表状态** | ACL 2025 (Volume 1: Long Papers), pp. 12740–12755, Vienna, Austria, July 2025 |
| **Abstract 摘要** | 该论文从动力系统理论视角分析 LLM 的连续改写行为。发现 LLM 在反复改写（successive paraphrasing）过程中会收敛到稳定的周期状态（如 2 周期吸引子环），限制了语言多样性。这归因于 LLM 的自我强化特性——在迭代中偏好并放大某些文本形式。即使增加生成随机性或交替使用不同 prompt/模型，这种模式依然存在。 |

---

### 2. Shahriar et al. (2025) — ✅ 验证通过

| 项目 | 结果 |
|------|------|
| **arXiv ID** | `2512.05311` ✅ 存在 |
| **URL** | https://arxiv.org/abs/2512.05311 |
| **实际 Title** | "The Erosion of LLM Signatures: Can We Still Distinguish Human and LLM-Generated Scientific Ideas After Iterative Paraphrasing?" ✅ 与声称一致（声称标题为简写，完整标题含副标题） |
| **作者** | Sadat Shahriar, Navid Ayoobi, Arjun Mukherjee (University of Houston) |
| **发表状态** | arXiv preprint, 2025年12月4日提交 |
| **"25.4%" 数字** | ✅ 确认存在。原文 abstract 明确写道：detection performance declining by an average of **25.4%** after five consecutive paraphrasing stages |
| **Abstract 摘要** | 随着 LLM 日益被用作研究代理，区分 LLM 与人类生成的科学想法变得至关重要。虽然检测 LLM 生成文本已被广泛研究，但区分人类与 LLM 生成的科学**想法**仍是未探索领域。本文系统评估了 SOTA 机器学习模型在连续改写后区分人类与 LLM 生成想法的能力。结果显示：经过 5 轮连续改写后，检测性能平均下降 25.4%；将研究问题作为上下文信息纳入可提升检测性能至多 2.97%。 |

---

两篇论文均 ✅ 验证通过，标题、作者、ID 均与声称一致，关键数字（25.4%）确认存在于原文中。

Sources:
- [Wang et al. - ACL Anthology](https://aclanthology.org/2025.acl-long.624/)
- [Wang et al. - arXiv](https://arxiv.org/abs/2502.15208)
- [Shahriar et al. - arXiv](https://arxiv.org/abs/2512.05311)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_reference_verification_r21_20260520T150819"
}
```

</details>

---
