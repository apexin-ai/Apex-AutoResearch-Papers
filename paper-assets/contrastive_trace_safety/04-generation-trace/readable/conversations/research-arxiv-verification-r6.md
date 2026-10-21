# research arxiv verification r6

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/chats/worker_research_arxiv_verification_r6_20260518T015913.jsonl`
- **Structured JSON:** [`dbd236cb3058d797bf8d.json`](../../sessions/db/dbd236cb3058d797bf8d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

15 recorded events

### Tool call

_source line 1 · 2026-05-18T02:00:24.294428+00:00_

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
  "session": "worker_research_arxiv_verification_r6_20260518T015913",
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

_source line 2 · 2026-05-18T02:00:24.294989+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_arxiv_verification_r6_20260518T015913",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T02:00:24.295167+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:arxiv.org 2504.05419"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_arxiv_verification_r6_20260518T015913",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:arxiv.org 2504.05419"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-18T02:00:24.295301+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:arxiv.org 2510.21285"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_arxiv_verification_r6_20260518T015913",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:arxiv.org 2510.21285"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-18T02:00:24.295423+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:arxiv.org 2605.13772"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_arxiv_verification_r6_20260518T015913",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:arxiv.org 2605.13772"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-18T02:00:24.295577+00:00_

Web search results for query: "site:arxiv.org 2510.21285"

Links: [{"title":"[2510.21285] When Models Outthink Their Safety: Unveiling and Mitigating Self-Jailbreak in Large Reasoning Models","url":"https://arxiv.org/abs/2510.21285"},{"title":"When Models Outthink Their Safety: Unveiling and Mitigating Self-Jailbreak in Large Reasoning Models","url":"https://arxiv.org/html/2510.21285"},{"title":"Diffusion Transformers with Representation Autoencoders","url":"https://arxiv.org/html/2510.11690v1"},{"title":"[2509.21285] Decaying superfluid turbulence near an anomalous non-thermal fixed point","url":"https://arxiv.org/abs/2509.21285"},{"title":"[2510.15089] Stability of the spatially homogeneous Landau equation in relative entropy and applications to score-based numerical methods","url":"https://arxiv.org/abs/2510.15089"},{"title":"Arxiv","url":"https://arxiv.org/pdf/2407.21285"},{"title":"Mathematics Oct 2025","url":"https://arxiv.org/list/math/2025-10?skip=2300&show=100"},{"title":"[2511.21285] PEFT-Bench: A Parameter-Efficient Fine-Tuning Methods Benchmark","url":"https://arxiv.org/abs/2511.21285"},{"title":"[2502.21285] Power sum expansions for Kromatic symmetric functions using Lyndon heaps","url":"https://arxiv.org/abs/2502.21285"},{"title":"Contents","url":"https://arxiv.org/html/2510.02782"}]

Based on the search results, the arXiv paper **2510.21285** is titled "When Models Outthink Their Safety: Unveiling and Mitigating Self-Jailbreak in Large Reasoning Models."

The paper addresses safety issues in Large Reasoning Models (LRMs). The authors uncover a failure mode called "Self-Jailbreak," where models initially recognize the harmful intent of a query, but override this judgment during subsequent reasoning steps, ultimately generating unsafe outputs. They propose Chain-of-Guardrail (CoG), a trajectory-level training framework that mitigates Self-Jailbreak via targeted, step-level interventions while maintaining reasoning ability.


REMINDER: You MUST include t
…[truncated 72 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_arxiv_verification_r6_20260518T015913",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-18T02:00:24.295802+00:00_

Web search results for query: "site:arxiv.org 2504.05419"

Links: [{"title":"[2504.05419] Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification","url":"https://arxiv.org/abs/2504.05419"},{"title":"Reasoning Models Know When They’re Right: Probing Hidden States for Self-Verification","url":"https://arxiv.org/html/2504.05419"},{"title":"[2505.05419] A new time-dependent quantum theory based on Tsallis' distribution","url":"https://arxiv.org/abs/2505.05419"},{"title":"[2502.05419] The non-conservative compressible two-fluid system with common pressure: Global existence and sharp time asymptotics","url":"https://arxiv.org/abs/2502.05419"},{"title":"[2501.05419] Caroli-de Gennes-Matricon Analogs in Full-Shell Hybrid Nanowires","url":"https://arxiv.org/abs/2501.05419"},{"title":"arXiv:2406.05419v1 [math.CO] 8 Jun 2024 FOUNDATIONS OF ITERATED STAR MAPS","url":"https://arxiv.org/pdf/2406.05419"},{"title":"1 Introduction","url":"https://arxiv.org/html/2505.05419"},{"title":"Caroli–de Gennes–Matricon Analogs in Full-Shell Hybrid Nanowires","url":"https://arxiv.org/html/2501.05419"},{"title":"[2507.05419] Motion Generation: A Survey of Generative Approaches and Benchmarks","url":"https://arxiv.org/abs/2507.05419"},{"title":"[2511.05419] Crossing the veil of the brightest radio relic in the sky MACS J0717.6+3745","url":"https://arxiv.org/abs/2511.05419"}]

Based on the search results, I found the paper you're looking for:

**Title:** "Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification"

**Key Information:**
- The paper addresses how reasoning models have achieved remarkable performance on math and logical reasoning tasks, but still suffer from overthinking, often performing unnecessary reasoning steps even after reaching the correct answer.

- The work studies whether reasoning models encode information about answer correctness through probing the model's hidden states, and the resulting probe can verify interme
…[truncated 630 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_arxiv_verification_r6_20260518T015913",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-18T02:00:24.296001+00:00_

Web search results for query: "site:arxiv.org 2605.13772"

Links: [{"title":"[2605.13772] Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry","url":"https://arxiv.org/abs/2605.13772"},{"title":"[2605.01172] A Theory of Generalization in Deep Learning","url":"https://arxiv.org/abs/2605.01172"},{"title":"[2601.13772] A Blockchain-Oriented Software Engineering Architecture for Carbon Credit Certification Systems","url":"https://arxiv.org/abs/2601.13772"},{"title":"Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry","url":"https://arxiv.org/html/2605.13772"},{"title":"[2605.12832] Digital Twins as Synthetic Controls in Single-Arm Trials","url":"https://arxiv.org/abs/2605.12832"},{"title":"HDPO: Hybrid Distillation Policy Optimization via Privileged Self-Distillation","url":"https://arxiv.org/pdf/2603.23871"},{"title":"Machine Learning","url":"https://arxiv.org/list/cs.LG/recent?skip=149&show=1000"},{"title":"[2605.05242] Beyond Semantic Similarity: Rethinking Retrieval for Agentic Search via Direct Corpus Interaction","url":"https://arxiv.org/abs/2605.05242"},{"title":"[2603.07952] VisualAD: Language-Free Zero-Shot Anomaly Detection via Vision Transformer","url":"https://arxiv.org/abs/2603.07952"},{"title":"[2603.23871] HDPO: Hybrid Distillation Policy Optimization via Privileged Self-Distillation","url":"https://arxiv.org/abs/2603.23871"}]

Based on the search results, I found the paper you're looking for:

**Title:** "Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry"

**arXiv ID:** 2605.13772

**Authors:** Tyler Alvarez and Ali Baheri

**Key Findings:**

Large language models hallucinate during multi-step reasoning, but most existing detectors operate at the trace level: they assign one confidence score to a full output, fail to localize the first error, and often require multiple sampled completions.

The paper proposes a n
…[truncated 750 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_arxiv_verification_r6_20260518T015913",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-18T02:00:24.296200+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2504.05419 \"Reasoning Models Know When They're Right\" authors Stechly"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_arxiv_verification_r6_20260518T015913",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2504.05419 \"Reasoning Models Know When They're Right\" authors Stechly"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-18T02:00:24.296342+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2510.21285 \"When Models Outthink Their Safety\" authors Mao"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_arxiv_verification_r6_20260518T015913",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2510.21285 \"When Models Outthink Their Safety\" authors Mao"
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T02:00:24.296466+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2605.13772 \"Where Does Reasoning Break\" authors 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_arxiv_verification_r6_20260518T015913",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2605.13772 \"Where Does Reasoning Break\" authors 2026"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-18T02:00:24.296674+00:00_

Web search results for query: "arxiv 2504.05419 "Reasoning Models Know When They're Right" authors Stechly"

Links: [{"title":"[2504.05419] Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification","url":"https://arxiv.org/abs/2504.05419"},{"title":"Reasoning Models Know When They’re Right: Probing Hidden States for Self-Verification","url":"https://arxiv.org/html/2504.05419v1"},{"title":"[2504.05419v1] Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification","url":"https://arxiv.org/abs/2504.05419v1"},{"title":"Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification - ADS","url":"https://ui.adsabs.harvard.edu/abs/arXiv:2504.05419"},{"title":"Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification | alphaXiv","url":"https://www.alphaxiv.org/resources/2504.05419"},{"title":"arXiv:2504.05419v1 [cs.AI] 7 Apr 2025","url":"https://arxiv.org/pdf/2504.05419"},{"title":"dblp: Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification.","url":"https://dblp.org/rec/journals/corr/abs-2504-05419.html"},{"title":"The Geometry of Self-Verification in a Task-Specific Reasoning Model","url":"https://arxiv.org/html/2504.14379v1"},{"title":"Reasoning Models Better Express Their Confidence","url":"https://arxiv.org/html/2505.14489v2"},{"title":"Thinking Out Loud: Do Reasoning Models Know When They're Right? - ADS","url":"https://ui.adsabs.harvard.edu/abs/arXiv:2504.06564"}]

I found the paper arxiv 2504.05419 "Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification."

However, I should note that the authors listed for this paper are Anqi Zhang, Yulin Chen, Jane Pan, Chen Zhao, Aurojit Panda, Jinyang Li, and He He. There is no author named Stechly on this paper according to the search results.

Here's what the paper is about:

The work studies whether reasoning models encode information about answer correctness t
…[truncated 747 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_arxiv_verification_r6_20260518T015913",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-18T02:00:24.296854+00:00_

Web search results for query: "arxiv 2605.13772 "Where Does Reasoning Break" authors 2026"

Links: [{"title":"[2605.13772] Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry","url":"https://arxiv.org/abs/2605.13772"},{"title":"Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry","url":"https://arxiv.org/html/2605.13772"}]

Based on the search results, here's what I found about arxiv paper 2605.13772:

**Paper Title:** Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry

**Authors:** Tyler Alvarez and Ali Baheri

**Submission Date:** 13 May 2026

**Summary:** Large language models hallucinate during multi-step reasoning, but most existing detectors operate at the trace level: they assign one confidence score to a full output, fail to localize the first error, and often require multiple sampled completions. The paper proposes a novel approach that frames correct reasoning as moving through a stable manifold of locally coherent transitions, where a first error appears as a localized excursion in transport cost away from this manifold.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_arxiv_verification_r6_20260518T015913",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-18T02:00:24.297033+00:00_

Web search results for query: "arxiv 2510.21285 "When Models Outthink Their Safety" authors Mao"

Links: [{"title":"[2510.21285] When Models Outthink Their Safety: Unveiling and Mitigating Self-Jailbreak in Large Reasoning Models","url":"https://arxiv.org/abs/2510.21285"},{"title":"[2510.21285v1] When Models Outthink Their Safety: Mitigating Self-Jailbreak in Large Reasoning Models with Chain-of-Guardrails","url":"https://arxiv.org/abs/2510.21285v1"},{"title":"When Models Outthink Their Safety: Unveiling and Mitigating Self-Jailbreak in Large Reasoning Models","url":"https://arxiv.org/html/2510.21285"},{"title":"When Models Outthink Their Safety: Mitigating Self-Jailbreak in Large Reasoning Models with Chain-of-Guardrails","url":"https://arxiv.org/html/2510.21285v1"},{"title":"Paper page - When Models Outthink Their Safety: Mitigating Self-Jailbreak in Large Reasoning Models with Chain-of-Guardrails","url":"https://huggingface.co/papers/2510.21285"},{"title":"WHEN MODELS OUTTHINK THEIR SAFETY: MITIGATING SELF-JAILBREAK IN LARGE REASONING","url":"https://arxiv.org/pdf/2510.21285v1"},{"title":"When Models Outthink Their Safety:","url":"https://arxiv.org/pdf/2510.21285"},{"title":"When Models Outthink Their Safety: Mitigating Self-Jailbreak in Large Reasoning Models with Chain-of-Guardrails | alphaXiv","url":"https://www.alphaxiv.org/overview/2510.21285v1"},{"title":"Artificial Intelligence Jun 2025","url":"https://www.arxiv.org/list/cs.AI/2025-06?skip=0&show=2000"},{"title":"Safety in Large Reasoning Models: A Survey","url":"https://arxiv.org/html/2504.17704v1"}]

I found the paper! Here are the details about arxiv paper 2510.21285:

**Title:** "When Models Outthink Their Safety: Unveiling and Mitigating Self-Jailbreak in Large Reasoning Models"

**Authors:** Yingzhi Mao, Chunkang Zhang, Junxiang Wang, Xinyan Guan, Boxi Cao, Yaojie Lu, Hongyu Lin, Xianpei Han, Le Sun

**Main Contribution:** The paper uncovers a previously underexplored failure mode in Large Reasoning 
…[truncated 653 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_arxiv_verification_r6_20260518T015913",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-18T02:00:24.297266+00:00_

## 验证结果

---

### 论文 1: `2504.05419`

| 项目 | 结果 |
|------|------|
| **存在性** | 存在 |
| **真实标题** | "Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification" |
| **标题匹配** | 部分匹配 — 声称标题是完整标题的前半部分，省略了副标题 |
| **真实作者** | Anqi Zhang, Yulin Chen, Jane Pan, Chen Zhao, Aurojit Panda, Jinyang Li, He He |
| **作者匹配** | **不匹配** — 声称 "Stechly et al."，实际第一作者为 Anqi Zhang，作者列表中无 Stechly |
| **相关性** | **高度相关** — 直接研究 reasoning model hidden states 中的 correctness probing，用于 self-verification |
| **结论** | **MISMATCH** — ID 和标题真实，但作者归属错误 |

---

### 论文 2: `2510.21285`

| 项目 | 结果 |
|------|------|
| **存在性** | 存在 |
| **真实标题** | "When Models Outthink Their Safety: Unveiling and Mitigating Self-Jailbreak in Large Reasoning Models" |
| **标题匹配** | 匹配 — 声称标题是完整标题的主标题部分 |
| **真实作者** | Yingzhi Mao, Chunkang Zhang, Junxiang Wang, Xinyan Guan, Boxi Cao, Yaojie Lu, Hongyu Lin, Xianpei Han, Le Sun |
| **作者匹配** | **匹配** — 第一作者确为 Mao，提交于 2025 年 10 月 |
| **相关性** | **相关** — 研究 reasoning model 的安全失败模式（Self-Jailbreak），提出 Chain-of-Guardrail 框架 |
| **结论** | **VERIFIED** |

---

### 论文 3: `2605.13772`（2026 年 5 月）

| 项目 | 结果 |
|------|------|
| **存在性** | 存在 — 提交于 2026-05-13（5 天前） |
| **真实标题** | "Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry" |
| **标题匹配** | 匹配 — 声称标题是完整标题的主标题部分 |
| **真实作者** | Tyler Alvarez, Ali Baheri |
| **作者匹配** | 声称中未提供具体作者，无法判断匹配性 |
| **相关性** | **极高相关** — 用 hidden-state transport geometry 做 step-level hallucination detection，与 contrastive trace safety 直接相关（contrastive PCA lens + geometric transition features） |
| **结论** | **VERIFIED** |

---

### 汇总

| 论文 | ID | 结论 | 问题 |
|------|-----|------|------|
| 1 | 2504.05419 | **MISMATCH** | 作者错误：实际为 Zhang et al.，非 Stechly et al. |
| 2 | 2510.21285 | **VERIFIED** | — |
| 3 | 2605.13772 | **VERIFIED** | 2026 年本月论文，确实存在 |

Sources:
- [2504.05419 - Reasoning Models Know When They're Right](https://arxiv.org/abs/2504.05419)
- [2510.21285 - When Models Outthink Their Safety](https://arxiv.org/abs/2510.21285)
- [2605.13772 - Where Does Reasoning Break?](https://arxiv.org/abs/2605.13772)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_arxiv_verification_r6_20260518T015913"
}
```

</details>

---
