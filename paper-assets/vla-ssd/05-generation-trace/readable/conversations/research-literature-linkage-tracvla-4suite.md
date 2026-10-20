# research literature linkage tracvla 4suite

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 0
- **Tool calls:** 18
- **Original source:** `logs/chats/worker_research_literature-linkage-tracvla-4suite_20260521T204054.jsonl`
- **Structured JSON:** [`b2280e217c80fafb3a1c.json`](../../sessions/b2/b2280e217c80fafb3a1c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

37 recorded events

### Tool call

_source line 1 · 2026-05-21T20:43:42.940905+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__append_idea,WebSearch,WebFetch",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-linkage-tracvla-4suite_20260521T204054",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__append_idea,WebSearch,WebFetch",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-21T20:43:42.941262+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-linkage-tracvla-4suite_20260521T204054",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T20:43:42.941528+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "vla-ssd",
  "file": "literature_map.yaml",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-linkage-tracvla-4suite_20260521T204054",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "vla-ssd",
    "file": "literature_map.yaml",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-21T20:43:42.942019+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/literature_map.yaml\", \"content\": \"papers:\\n  # ============================================================\\n  # DIRECT COMPETITORS — VLA Representation Analysis / Interpretability\\n  # ============================================================\\n  - id: grant2026\\n    title: \\\"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models\\\"\\n    authors: \\\"Bryce Grant, Xijia Zhao, Peng Wang\\\"\\n    year: 2026\\n    venue: \\\"arXiv preprint (under review)\\\"\\n    arxiv_id: \\\"2603.19233\\\"\\n    category: direct-competitor\\n    role: competitor\\n    key_findings: >\\n      Visual pathway dominates action generation across all 6 tested VLA architectures (80M–7B params, 394K+ rollout episodes, 4 benchmarks).\\n      Language sensitivity depends on task structure: when visual context uniquely specifies the task, language is IGNORED;\\n      when multiple goals share a scene, language becomes essential (\\\"encoded but not used\\\").\\n      Cross-task activation injection steers robots toward source-task positions (99.8% trajectory alignment with source in X-VLA).\\n      Multi-pathway architectures (pi0.5, SmolVLA, GR00T) separate motor programs (expert pathway) from goal semantics (VLM pathway).\\n    relevance_to_us: >\\n      Most direct competitor. Behavioral intervention (activation injection, SAE, probing) reveals vision dominance + language encoded but not used.\\n      Uses OpenVLA-OFT checkpoint; we use standard fine-tuning — must qualify this difference in Related Work.\\n    novelty_gap: >\\n      No trained vs untrained representation analysis. They compare different model architectures,\\n      we compare trained vs untrained representation structure within the same architecture.\\n      Their \\\"encoded but not used\\\" is a behavioral-level conclusion; we demonstrate at the represent
…[truncated 29682 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-linkage-tracvla-4suite_20260521T204054",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T20:43:42.942218+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "attention head consistency across tasks universal attention patterns fine-tuning transformer 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-linkage-tracvla-4suite_20260521T204054",
  "tool": "WebSearch",
  "tool_args": {
    "query": "attention head consistency across tasks universal attention patterns fine-tuning transformer 2025 2026"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-21T20:43:42.942362+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "task-independent attention specialization VLA vision-language-action model attention routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-linkage-tracvla-4suite_20260521T204054",
  "tool": "WebSearch",
  "tool_args": {
    "query": "task-independent attention specialization VLA vision-language-action model attention routing"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T20:43:42.942484+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "specific attention head indices consistent across tasks transformer interpretability \"head identity\" preservation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-linkage-tracvla-4suite_20260521T204054",
  "tool": "WebSearch",
  "tool_args": {
    "query": "specific attention head indices consistent across tasks transformer interpretability \"head identity\" preservation"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-21T20:43:42.942640+00:00_

Web search results for query: "attention head consistency across tasks universal attention patterns fine-tuning transformer 2025 2026"

Links: [{"title":"[2510.21518] Head Pursuit: Probing Attention Specialization in Multimodal Transformers","url":"https://arxiv.org/abs/2510.21518"},{"title":"Published as a conference paper at ICLR 2026 WHY ATTENTION PATTERNS EXIST:","url":"https://arxiv.org/pdf/2601.21709"},{"title":"Quantifying LLM Attention-Head Stability: Implications for Circuit Universality","url":"https://arxiv.org/pdf/2602.16740"},{"title":"2026-01-13 Interpreting Transformers Through Attention Head Intervention","url":"https://www.arxiv.org/pdf/2601.04398v3"},{"title":"2026-01-12 Interpreting Transformers Through Attention Head Intervention","url":"https://www.arxiv.org/pdf/2601.04398v2"},{"title":"2026-01-09 Interpreting Transformers Through Attention Head Intervention","url":"https://www.arxiv.org/pdf/2601.04398"}]

Based on the web search results, here are the key findings related to attention head consistency across tasks and universal attention patterns in transformers:

## Attention Head Specialization and Consistency

Research shows consistent patterns of specialization at the head level across both unimodal and multimodal transformers. Editing as few as 1% of the heads, selected using specialized methods, can reliably suppress or enhance targeted concepts in model output.

## Universal Patterns Framework

Computing attention from queries, keys, and RoPE is a common design in transformer-based models, and TAPPA (a recently developed framework) both unifies diverse attention patterns and is broadly applicable across LLMs. Attention patterns are closely linked to a model's representational capacity and can guide compression.

## The Universality Hypothesis

A key research question in 2025-2026 involves the "universality hypothesis," which asserts that models learn the same or similar representational features and circuits across different models when t
…[truncated 600 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-linkage-tracvla-4suite_20260521T204054",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-21T20:43:42.942809+00:00_

Web search results for query: "task-independent attention specialization VLA vision-language-action model attention routing"

Links: [{"title":"GuidedVLA: Specifying Task-Relevant Factors via Plug-and-Play Action Attention Specialization","url":"https://arxiv.org/html/2605.12369v1"},{"title":"[2605.12369v1] GuidedVLA: Specifying Task-Relevant Factors via Plug-and-Play Action Attention Specialization","url":"https://arxiv.org/abs/2605.12369v1"},{"title":"FocusVLA: Focused Visual Utilization for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2603.28740"},{"title":"AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention","url":"https://arxiv.org/pdf/2511.18960"},{"title":"CogVLA: Cognition-Aligned Vision-Language-Action Model via Instruction-Driven Routing & Sparsification","url":"https://arxiv.org/pdf/2508.21046"},{"title":"AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention","url":"https://arxiv.org/html/2511.18960v1"},{"title":"Task adaptation of Vision-Language-Action model: 1st Place Solution for the 2025 BEHAVIOR Challenge","url":"https://arxiv.org/html/2512.06951v1"}]

I found several relevant results about attention mechanisms in Vision-Language-Action (VLA) models. Here are the key findings:

## GuidedVLA: Task-Relevant Attention Specialization

GuidedVLA is a framework designed to guide action generation to focus on task-relevant factors by supervising individual attention heads with manually defined auxiliary signals to capture distinct factors, instantiating this with three specialized heads: object grounding, spatial geometry, and temporal skill logic. Across simulation and real-robot experiments, GuidedVLA improves success rates in both in-domain and out-of-domain settings compared to strong VLA baselines.

## FocusVLA: Task-Aligned Attention

FocusVLA uses Modality Cascaded Attention to enforce sequential modality interaction and proposes Focus Attention to suppress task-irrelevant information,
…[truncated 926 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-linkage-tracvla-4suite_20260521T204054",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T20:43:42.943008+00:00_

Web search results for query: "specific attention head indices consistent across tasks transformer interpretability "head identity" preservation"

Links: [{"title":"2026-01-09 Interpreting Transformers Through Attention Head Intervention","url":"https://www.arxiv.org/pdf/2601.04398"},{"title":"Interpreting Transformers Through Attention Head Intervention","url":"https://arxiv.org/html/2601.04398v3"},{"title":"Mechanistic Interpretability of Fine-Tuned Vision Transformers on   Distorted Images: Decoding Attention Head Behavior for Transparent and   Trustworthy AI","url":"https://arxiv.org/pdf/2503.18762"},{"title":"Head Pursuit: Probing Attention Specialization in Multimodal Transformers","url":"https://arxiv.org/pdf/2510.21518"},{"title":"GMAR: Gradient-Driven Multi-Head Attention Rollout for Vision Transformer Interpretability","url":"https://arxiv.org/html/2504.19414v1"},{"title":"Head Pursuit: Probing Attention Specialization in Multimodal Transformers","url":"https://arxiv.org/html/2510.21518"},{"title":"GitHub - IAAR-Shanghai/Awesome-Attention-Heads: An awesome repository & A comprehensive survey on interpretability of LLM attention heads. · GitHub","url":"https://github.com/IAAR-Shanghai/Awesome-Attention-Heads"},{"title":"Interpreting Context Look-ups in Transformers: Investigating Attention-MLP Interactions","url":"https://arxiv.org/html/2402.15055v1"},{"title":"Quantifying LLM Attention-Head Stability: Implications for Circuit Universality","url":"https://arxiv.org/pdf/2602.16740"}]

I found relevant research on attention head consistency and interpretability in transformers. Here are the key findings from my search:

## Head Specialization Across Tasks

Consistent patterns of specialization exist at the head level across both unimodal and multimodal transformers. Individual attention heads specialize in specific semantic or visual attributes, and research has uncovered specialized model components with consistent roles for attention heads, such as handling
…[truncated 1328 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-linkage-tracvla-4suite_20260521T204054",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T20:43:42.943197+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.16740",
  "prompt": "Extract: title, authors, year, venue, key findings about attention head stability across training runs, whether specific head indices are consistent, and any findings about \"universal\" vs \"idiosyncratic\" circuits. Also extract whether they study fine-tuned models or just pre-trained ones."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-linkage-tracvla-4suite_20260521T204054",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2602.16740",
    "prompt": "Extract: title, authors, year, venue, key findings about attention head stability across training runs, whether specific head indices are consistent, and any findings about \"universal\" vs \"idiosyncratic\" circuits. Also extract whether they study fine-tuned models or just pre-trained ones."
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-21T20:43:42.943326+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.21518",
  "prompt": "Extract: title, authors, year, venue, key findings about attention head specialization in multimodal transformers, whether specific heads are found to have consistent roles across tasks/inputs, and any findings about head identity preservation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-linkage-tracvla-4suite_20260521T204054",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2510.21518",
    "prompt": "Extract: title, authors, year, venue, key findings about attention head specialization in multimodal transformers, whether specific heads are found to have consistent roles across tasks/inputs, and any findings about head identity preservation."
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T20:43:42.943447+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.21709",
  "prompt": "Extract: title, authors, year, venue, key findings about why attention patterns exist and their relationship to representational capacity and task consistency."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-linkage-tracvla-4suite_20260521T204054",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2601.21709",
    "prompt": "Extract: title, authors, year, venue, key findings about why attention patterns exist and their relationship to representational capacity and task consistency."
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-21T20:43:42.943642+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.12369",
  "prompt": "Extract: title, authors, year, key findings about attention specialization in VLA models, whether they find natural attention head specialization patterns, and whether specific heads are assigned specific roles across tasks."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-linkage-tracvla-4suite_20260521T204054",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2605.12369",
    "prompt": "Extract: title, authors, year, key findings about attention specialization in VLA models, whether they find natural attention head specialization patterns, and whether specific heads are assigned specific roles across tasks."
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-21T20:43:42.943793+00:00_

# Paper Summary

**Title:** Quantifying LLM Attention-Head Stability: Implications for Circuit Universality

**Authors:** Karan Bali, Jack Stanley, Praneet Suresh, Danilo Bzdok

**Year:** 2026 (submitted February 17, 2026)

**Venue:** arXiv (cs.LG - Computer Science/Machine Learning)

## Key Findings on Attention Head Stability

The researchers systematically examined whether transformer circuits remain consistent across independent training runs:

**Stability Patterns:**
- "Middle-layer heads are the least stable yet the most representationally distinct"
- Deeper models show stronger mid-depth divergence in attention head learning
- The residual stream exhibits comparative stability across refits
- Weight decay optimization substantially improves stability across random initializations

**Universal vs. Idiosyncratic Circuits:**
The paper directly addresses this distinction, noting that circuits are "rarely acid-tested for their stability across different instances," raising questions about whether circuits "emerge universally across labs or turn out to be idiosyncratic to a particular estimation instance."

**Head Indices:**
The research does not specifically address whether particular attention head indices remain consistent across runs.

**Model Types:**
The study focuses on "independently initialized training runs" of transformer language models, examining pre-trained instances rather than fine-tuned variants.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-linkage-tracvla-4suite_20260521T204054",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-21T20:43:42.943956+00:00_

# Paper Summary: Head Pursuit

**Title:** Head Pursuit: Probing Attention Specialization in Multimodal Transformers

**Authors:** Lorenzo Basile, Valentino Maiorca, Diego Doimo, Francesco Locatello, Alberto Cazzaniga

**Year:** 2025

**Venue:** NeurIPS 2025 (spotlight presentation)

## Key Findings on Attention Head Specialization

The research demonstrates that individual attention heads exhibit specialized behavior across both unimodal and multimodal transformers. The authors developed a signal processing-based interpretability method to analyze how heads focus on particular semantic or visual attributes.

**Primary Discovery:** The study found "consistent patterns of specialization at the head level across both unimodal and multimodal transformers." This indicates that heads develop consistent functional roles within the network architecture.

**Practical Impact:** Remarkably, the researchers discovered that "editing as few as 1% of the heads...can reliably suppress or enhance targeted concepts in the model output." This demonstrates both the importance and manipulability of specialized heads.

## Head Identity and Task Consistency

The research validated its approach across diverse tasks—language-based (question answering, toxicity mitigation) and vision-language (image classification, captioning)—suggesting that head specialization patterns show stability across different task domains. The findings indicate an "interpretable and controllable structure within attention layers," suggesting heads maintain identifiable functional roles across contexts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-linkage-tracvla-4suite_20260521T204054",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-21T20:43:42.944114+00:00_

# Paper Summary

**Title:** Why Attention Patterns Exist: A Unifying Temporal Perspective Analysis

**Authors:** Qingyue Yang, Jie Wang, Xing Li, Yinqi Bai, Xialiang Tong, Huiling Zhen, Jianye Hao, Mingxuan Yuan, Bin Li

**Year:** 2026

**Venue:** ICLR 2026

## Key Findings

The research introduces TAPPA (Temporal Attention Pattern Predictability Analysis), a framework that unifies understanding of diverse attention mechanisms in large language models. The authors categorize attention patterns into two groups: "predictable patterns with clear regularities and unpredictable patterns that appear effectively random."

A central discovery is that this distinction correlates with "the degree of query self-similarity along the temporal dimension." The framework explains previously fragmented observations—such as retrieval heads, sink heads, and diagonal traces—through a mathematically coherent lens examining how queries, keys, and Rotary Positional Embeddings interact.

The research validates these theoretical insights by applying them to practical tasks including KV cache compression and LLM pruning, demonstrating that metrics derived from TAPPA consistently outperform baseline approaches in these optimization contexts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-linkage-tracvla-4suite_20260521T204054",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-21T20:43:42.944254+00:00_

# GuidedVLA Paper Summary

**Title:** GuidedVLA: Specifying Task-Relevant Factors via Plug-and-Play Action Attention Specialization

**Authors:** Xiaosong Jia, Bowen Yang, Zuhao Ge, Xian Nie, Yuchen Zhou, Cunxin Fan, Yufeng Li, Yilin Chai, Chao Jing, Zijian Liang, Qingwen Bu, Haidong Cao, Chao Wu, Qifeng Li, Zhenjie Yang, Chenhe Zhang, Hongyang Li, Zuxuan Wu, Junchi Yan, Yu-Gang Jiang

**Year:** 2026 (submitted May 12, 2026)

## Key Findings on Attention Specialization

**Core Approach:** Rather than relying on end-to-end learning, the framework treats "the action decoder not as a monolithic learner, but as an assembly of functional components." Individual attention heads receive supervision through manually defined auxiliary signals.

**Assigned Head Roles:** The paper instantiates three specialized heads with explicit functions:
- Object grounding
- Spatial geometry  
- Temporal skill logic

**Results:** The framework demonstrates improved success rates across both in-domain and out-of-domain settings compared to baseline VLA models. The authors establish that "the quality of these specialized factors correlates positively with task performance" and produce "decoupled, high-quality features."

The research treats attention head specialization as a deliberate design choice requiring external guidance rather than an emergent natural property.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-linkage-tracvla-4suite_20260521T204054",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-21T20:43:42.944413+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"universal attention heads\" transformer fine-tuning same head indices persistent specialization 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-linkage-tracvla-4suite_20260521T204054",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"universal attention heads\" transformer fine-tuning same head indices persistent specialization 2024 2025 2026"
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-21T20:43:42.944534+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "attention head function preserved after fine-tuning transformer \"same heads\" across models architectures 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-linkage-tracvla-4suite_20260521T204054",
  "tool": "WebSearch",
  "tool_args": {
    "query": "attention head function preserved after fine-tuning transformer \"same heads\" across models architectures 2025 2026"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-21T20:43:42.944676+00:00_

Web search results for query: ""universal attention heads" transformer fine-tuning same head indices persistent specialization 2024 2025 2026"

Links: [{"title":"Attention Head Specialization","url":"https://www.emergentmind.com/topics/attention-head-specialization"},{"title":"Reasoning-Focus Heads (RFHs) in Transformers","url":"https://www.emergentmind.com/topics/reasoning-focus-heads-rfhs"},{"title":"Mechanistic Interpretability of Fine-Tuned Vision Transformers on   Distorted Images: Decoding Attention Head Behavior for Transparent and   Trustworthy AI","url":"https://arxiv.org/pdf/2503.18762"},{"title":"Head Pursuit: Probing Attention Specialization in Multimodal Transformers","url":"https://arxiv.org/pdf/2510.21518"},{"title":"ResiDual Transformer Alignment with Spectral Decomposition","url":"https://arxiv.org/pdf/2411.00246"},{"title":"Multi-Head Softmax Attention Transformer","url":"https://www.emergentmind.com/topics/multi-head-softmax-attention-transformer"},{"title":"Augmenting Self-attention with Persistent Memory","url":"https://arxiv.org/pdf/1907.01470"}]

I found several relevant results about attention head specialization in transformers. Here's what the search revealed:

## Key Findings

Specialization has been observed to emerge in attention heads in both large language models and visual branches of CLIP models. Specialization appears to be a by-product related to large-scale training, though it's unclear exactly why it emerges and whether this is a systematic property.

### Recent Research (2024-2025)

Recent work includes "Differentiation and Specialization of Attention Heads via the Refined Local Learning Coefficient (2024)" and "Mechanistic Interpretability of Fine-Tuned Vision Transformers on Distorted Images: Decoding Attention Head Behavior for Transparent and Trustworthy AI (2025)".

A 2025 study examined individual attention heads in vision transformers fine-tuned on distorted images and revealed functional specialization in ViTs, showing h
…[truncated 775 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-linkage-tracvla-4suite_20260521T204054",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-21T20:43:42.944863+00:00_

Web search results for query: "attention head function preserved after fine-tuning transformer "same heads" across models architectures 2025 2026"

Links: [{"title":"Frontiers | Adaptive noise-augmented attention for enhancing Transformer fine-tuning on longitudinal medical data","url":"https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1663484/full"},{"title":"2026-01-13 Interpreting Transformers Through Attention Head Intervention","url":"https://www.arxiv.org/pdf/2601.04398v3"},{"title":"Self-Attention Heads in Transformers","url":"https://www.emergentmind.com/topics/self-attention-heads"},{"title":"Inside Transformers: Attention, Scaling Tricks & Emerging Alternatives in 2025","url":"https://www.gocodeo.com/post/inside-transformers-attention-scaling-tricks-emerging-alternatives-in-2025"},{"title":"2026-01-12 Interpreting Transformers Through Attention Head Intervention","url":"https://www.arxiv.org/pdf/2601.04398v2"},{"title":"2026-01-09 Interpreting Transformers Through Attention Head Intervention","url":"https://www.arxiv.org/pdf/2601.04398"},{"title":"All-or-Here Attention in Transformers","url":"https://www.emergentmind.com/papers/2512.22562"},{"title":"The Effect of Attention Head Count on Transformer Approximation","url":"https://arxiv.org/pdf/2510.06662"}]

Based on the web search results, I found relevant information about attention head functions and their properties in transformer models:

## Key Findings on Attention Head Specialization and Function

Recent work by Basile et al. (2025) introduced a method for identifying and manipulating attention heads specialized for semantic properties in both language and vision-language models using Simultaneous Orthogonal Matching Pursuit (SOMP) to discover which vocabulary directions best explain each head's outputs.

Individual heads in Mistral-7B specialize for different semantic categories, with each head's top-attended tokens clustering coherently around its semantic cat
…[truncated 1105 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-linkage-tracvla-4suite_20260521T204054",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-21T20:43:42.945068+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Olsson \"induction heads\" universal across models transformer mechanistic interpretability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-linkage-tracvla-4suite_20260521T204054",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Olsson \"induction heads\" universal across models transformer mechanistic interpretability"
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-21T20:43:42.945192+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2503.18762",
  "prompt": "Extract: title, authors, year, key findings about attention head specialization in fine-tuned Vision Transformers. Do specific head indices maintain their function after fine-tuning? Is there cross-task head consistency?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-linkage-tracvla-4suite_20260521T204054",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2503.18762",
    "prompt": "Extract: title, authors, year, key findings about attention head specialization in fine-tuned Vision Transformers. Do specific head indices maintain their function after fine-tuning? Is there cross-task head consistency?"
  }
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-21T20:43:42.945312+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"convergent\" attention heads across architectures \"same layer\" \"same head\" transformer universality circuit 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-linkage-tracvla-4suite_20260521T204054",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"convergent\" attention heads across architectures \"same layer\" \"same head\" transformer universality circuit 2025 2026"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-21T20:43:42.945437+00:00_

# Paper Summary

**Title:** Mechanistic Interpretability of Fine-Tuned Vision Transformers on Distorted Images: Decoding Attention Head Behavior for Transparent and Trustworthy AI

**Author:** Nooshin Bahador

**Year:** 2025 (submitted March 24, 2025)

## Key Findings on Attention Head Specialization

The research reveals functional stratification across transformer layers:

- **Early layers (1-3):** Minimal task relevance with "ablation increased MSE loss slightly" (approximately 0.11% mean increase)
- **Deeper layers (6+):** Substantially greater importance, causing "threefold higher loss increase" (~0.34% mean)
- **Intermediate layers (6-11):** Demonstrated "monosemantic behavior, attending exclusively to chirp regions"
- **Mixed early heads:** Some heads in layers 1-4 were monosemantic but task-irrelevant, functioning as "text detectors, edge or corner detectors"

## Regarding Cross-Task Consistency

The paper does not address whether specific head indices maintain function across different tasks or whether there is cross-task consistency. The study focuses exclusively on Vision Transformers fine-tuned on distorted spectrogram images, examining behavior within a single task context rather than comparing head functionality across multiple tasks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-linkage-tracvla-4suite_20260521T204054",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-21T20:43:42.945587+00:00_

Web search results for query: "Olsson "induction heads" universal across models transformer mechanistic interpretability"

Links: [{"title":"Induction Heads & In-Context Learning","url":"https://www.emergentmind.com/papers/2209.11895"},{"title":"Induction Head in Transformers","url":"https://www.emergentmind.com/topics/induction-head-ih"},{"title":"Mechanistic Interpretability: Part 7 - Induction Heads: The Mechanics of In-Context Learning | To Chin Yu","url":"https://ytcs.github.io/machine-learning/2025/05/25/mechanistic-interpretability-part-7.html"},{"title":"Induction Heads in Transformers","url":"https://www.emergentmind.com/topics/induction-heads-ihs"},{"title":"[2209.11895] In-context Learning and Induction Heads","url":"https://arxiv.org/abs/2209.11895"},{"title":"SELECTIVE INDUCTION HEADS: HOW TRANSFORM","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/d7ed243b13831bdd468f35039936bcef-Paper-Conference.pdf"},{"title":"(PDF) Mechanistic Interpretability of Induction Heads in Transformer Architectures","url":"https://www.researchgate.net/publication/392552787_Mechanistic_Interpretability_of_Induction_Heads_in_Transformer_Architectures"},{"title":"Induction Heads as an Essential Mechanism for Pattern ...","url":"https://aclanthology.org/2025.findings-naacl.283.pdf"}]

Based on the search results, here's what I found about Olsson's work on induction heads:

## Key Findings

Olsson and colleagues present evidence that induction heads may be the mechanistic source of general in-context learning in transformer models of any size. 

Induction heads are attention heads that implement a simple algorithm to complete token sequences like [A][B] ... [A] -> [B]. They are specialized attention heads in transformer architectures that implement a match-and-copy mechanism, enabling transformers to perform in-context learning by identifying token or sequence patterns in a prompt.

## Universality Across Models

The research confirms that mechanisms identified in 
…[truncated 844 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-linkage-tracvla-4suite_20260521T204054",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-21T20:43:42.945759+00:00_

Web search results for query: ""convergent" attention heads across architectures "same layer" "same head" transformer universality circuit 2025 2026"

Links: [{"title":"Quantifying LLM Attention-Head Stability: Implications for Circuit Universality","url":"https://arxiv.org/html/2602.16740"},{"title":"[2602.16740] Quantifying LLM Attention-Head Stability: Implications for Circuit Universality","url":"https://arxiv.org/abs/2602.16740"},{"title":"Quantifying LLM Attention-Head Stability: Implications for Circuit Universality","url":"https://arxiv.org/pdf/2602.16740"},{"title":"Multi-Head Attention Layer in Transformers","url":"https://www.facebook.com/groups/DeepNetGroup/posts/2397145477344987/"},{"title":"On the Universality of Transformer Architectures; How Much Attention Is Enough?","url":"https://arxiv.org/pdf/2512.18445"}]

I found a highly relevant paper from February 2026 that directly addresses your query. Here are the key findings:

Recent mechanistic interpretability work scrutinizes transformer "circuits"—sparse, mono or multi-layer sub-computations that may reflect human-understandable functions. However, these network circuits are rarely tested for their stability across different instances of the same deep learning architecture.

The research investigates whether models converge to the requisite representational space—alignment of the attention head's induced representation, that is, the subspace it attends to and writes into—and therefore to the same functional behavior.

The study quantifies, layer by layer, how similarly attention heads learn representations across independently initialized training runs. The rigorous experiments show that: (1) middle-layer heads are the least stable yet the most representationally distinct; (2) deeper models exhibit stronger mid-depth divergence; (3) unstable heads in deeper layers become more functionally important than their peers from the same layer; (4) applying weight decay optimization substantially improves at
…[truncated 452 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-linkage-tracvla-4suite_20260521T204054",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-21T20:43:42.945966+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-linkage-tracvla-4suite_20260521T204054",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/",
    "description": "List artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-21T20:43:42.946126+00:00_

_project
ablation_narrative_playbook.md
action_metrics_extended
action_probe_design.md
analyze_ablation_50demos.py
attention
attention_decomposition
attention_decomposition_and_r2.py
attention_normalization_entropy
attention_normalization_entropy.py
behavioral_pilot_w4_diagnosis.md
bootstrap_task_ratio.json
branch_split_rsa_results.md
citation_verification_2026.md
closedloop_diagnosis.md
controlb_analysis
counterfactual_10tasks
counterfactual_instruction.py
counterfactual_spatial
counterfactual_spatial.py
counterfactual_token_overlap
cross_inst_extract_phase2
cross_instruction
definitive_rsa_results.md
demo_sensitivity.py
demo_standardized_rsa.md
dinov2_baseline
dream_reports
extract_fused_backbone.py
fig2_cross_instruction_heatmap.pdf
fig_cross_architecture_attention.pdf
fig_cross_architecture_attention.png
fig_cross_architecture_attention.py
fig_ood_diagnostics.png
fig_rsa_perlayer_curve.pdf
fig_rsa_perlayer_curve.png
fig_specificity_bootstrap_30seeds.pdf
fig_specificity_bootstrap_30seeds.png
figures
fix_dryrun.py
fulllayer_action_probe.py
groundtruth_action_error
kendall_w_cross_task.json
l1_ablation_action_probe_50demos.py
layer_stability_analysis.md
libero_finetuned_attention
libero_finetuned_probe_profile.json
libero_goal_feasibility.md
libero_object_full_pipeline.py
literature_map.yaml
literature_map_probing.md
literature_survey_instruction_probing.md
llama2base_action_probe.py
manifest.yaml
matched_ablation_controls.py
matched_ablation_controls_diagnosis.md
mvp_controlb_trained
mvp_probe_trained
nora_analysis_report.md
openvla_libero_goal_compat.md
paper_consistency_report.md
patch_probes.py
patch_rsa.py
pca_linear_probe_gc.py
pca_linear_probe_perlayer.py
permutation_10k
permutation_test_I2.py
phi3v_attention_profile
phi3v_attention_trained_10tasks
phi3v_attention_untrained
phi3v_probe_untrained
phi3v_r2_action_probe
phi3v_r2_seed_expansion
phi3v_r2_untrained_probe
phi3v_untrained_cross_inst_probe.py
phi3v_untrained_seed_expansion
pipeline_audit_libero_goal.
…[truncated 825 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-linkage-tracvla-4suite_20260521T204054",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-21T20:43:42.946271+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:TodoWrite",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-linkage-tracvla-4suite_20260521T204054",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:TodoWrite",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-21T20:43:42.946391+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-linkage-tracvla-4suite_20260521T204054",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-21T20:43:42.946519+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "register_artifact",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-linkage-tracvla-4suite_20260521T204054",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "register_artifact",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-21T20:43:42.946632+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-linkage-tracvla-4suite_20260521T204054",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-21T20:43:42.946770+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/literature_linkage_4suite_consistency.md",
  "content": "# TracVLA 4-Suite Consistency: Literature Linkage Report\n\n**Date**: 2026-05-21\n\n---\n\n## Summary (< 200 words)\n\n**No direct competitor** reports cross-task/cross-suite attention head consistency in VLA models. The existing literature map (Grant 2026, Swann 2026, Haon 2025 等) focuses on behavioral intervention, SAE features, or activation steering — none tracks specific head indices across task suites.\n\n**h13/h22 universal mixed heads** lack direct precedent. The closest references are: (1) **Olsson et al. 2022** — induction heads as universal circuits across model scales, but these are algorithmic (pattern-matching), not routing-functional; (2) **Basile et al. 2025** (Head Pursuit, NeurIPS 2025 spotlight) — shows consistent head specialization in multimodal transformers, editing 1% of heads controls output, but does not track same-index heads across tasks; (3) **Bali et al. 2026** — finds middle-layer heads are *least* stable across independent training runs, which actually *strengthens* our claim: h13/h22 consistency is a training-induced convergent property within a model, not a trivial artifact of initialization.\n\n**3 papers recommended for literature_map.yaml** (see below). No paper discovers convergent routing with head identity preservation across task suites — this remains our unique contribution.\n\n---\n\n## Detailed Analysis\n\n### 1. Direct Competitor Check\n\nScanned all 9 direct-competitor entries in literature_map.yaml. None reports:\n- Cross-suite attention pattern consistency\n- Specific head indices with consistent function across tasks\n- Convergent routing (CF ordering, R² inverted-U, exit collapse) across suites\n\n**GuidedVLA (Jia et al., May 2026)** is the only VLA paper explicitly about attention head specialization, but they *engineer* it (supervised auxiliary signals for object/spatial/temporal heads), not *discover* it emergently. This is a useful contrast: we show VLA training naturally produces convergent routing without explicit supervision.\n\n### 2. h13/h22 Head Identity Preservation — Literature Support\n\n| Reference | Finding | Relation to h13/h22 |\n|-----------|---------|---------------------|\n| Olsson et al. 2022 | Induction heads are universal circuits across model scales | Precedent for functional universality at head level, but algorithmic (copy mechanism), not routing |\n| Basile et al. 2025 (Head Pursuit) | Consistent head specialization in multimodal transformers; 1% head editing controls output | Supports head-level functional specialization as real phenomenon; no same-index tracking across tasks |\n| Bali et al. 2026 | Middle-layer heads least stable across training runs, most representationally distinct | **Key contrast**: instability across runs ≠ instability across tasks within a run. Our h13/h22 consistency is *within-model cross-task*, a distinct (stronger) claim |\n| Bahador 2025 | ViT fine-tuning: deeper heads more important, intermediate heads monosemantic | Layer-level stratification consistent with our L1 instruction-dominant finding |\n| Yang et al. 2026 (TAPPA, ICLR 2026) | Unifies attention patterns via temporal predictability; predictable vs unpredictable patterns | Theoretical framework for *why* certain heads develop consistent patterns |\n\n**Bottom line**: Head specialization is well-established. Head identity preservation *across task suites within a fine-tuned VLA* is not. Our h13/h22 finding sits in a gap between \"heads specialize\" (known) and \"the same heads specialize the same way across diverse tasks\" (novel).\n\n### 3. Convergent Routing Pattern — Novelty Position\n\nThe full convergent routing pattern (CF ordering + R² inverted-U + exit collapse + L1 instruction dominance) across 3 architectures × 4 suites has no precedent. The closest work:\n- **Grant 2026**: Cross-architecture comparison but of *different* properties (vision dominance, language ignoring), not routing convergence\n- **Bali 2026**: Cross-run stability, not cross-task consistency\n- **Head Pursuit**: Cross-task head specialization in VLMs, not VLAs, and no routing pattern analysis\n\n---\n\n## Suggested literature_map.yaml Entries\n\n### Entry 1: bali2026\n\n```yaml\n- id: bali2026\n  title: \"Quantifying LLM Attention-Head Stability: Implications for Circuit Universality\"\n  authors: \"Karan Bali, Jack Stanley, Praneet Suresh, Danilo Bzdok\"\n  year: 2026\n  venue: \"arXiv preprint\"\n  arxiv_id: \"2602.16740\"\n  category: method-component\n  role: context\n  key_findings: >\n    Systematically quantifies attention head stability across independently initialized training runs.\n    Middle-layer heads are least stable yet most representationally distinct. Deeper models show\n    stronger mid-depth divergence. Weight decay improves stability. Residual stream comparatively stable.\n  relevance_to_us: >\n    Key contrast paper for h13/h22 universality claim. Their finding that heads are unstable across\n    training runs strengthens our claim: h13/h22 cross-task consistency is a training-induced convergent\n    property, not a trivial initialization artifact. Cross-run instability ≠ cross-task instability.\n  novelty_gap: >\n    Studies pre-trained LLMs across random seeds, not fine-tuned VLAs across task suites.\n    No cross-task consistency analysis within a single trained model.\n```\n\n### Entry 2: basile2025_headpursuit\n\n```yaml\n- id: basile2025_headpursuit\n  title: \"Head Pursuit: Probing Attention Specialization in Multimodal Transformers\"\n  authors: \"Lorenzo Basile, Valentino Maiorca, Diego Doimo, Francesco Locatello, Alberto Cazzaniga\"\n  year: 2025\n  venue: \"NeurIPS 2025 (Spotlight)\"\n  arxiv_id: \"2510.21518\"\n  category: method-component\n  role: methodology\n  key_findings: >\n    Consistent head specialization patterns in unimodal and multimodal transformers.\n    Signal processing-based method (SOMP) identifies semantic specialization per head.\n    Editing 1% of heads reliably suppresses/enhances targeted concepts.\n    Validated across QA, toxicity, image classification, captioning.\n  relevance_to_us: >\n    Strongest methodological support for head-level specialization as real phenomenon.\n    Their cross-task validation (QA + toxicity + vision tasks) parallels our cross-suite validation.\n    However they do not track same-index heads across tasks — our h13/h22 identity preservation goes further.\n  novelty_gap: >\n    VLM focus, not VLA. No routing pattern analysis. No trained vs untrained comparison.\n    Does not track whether same head indices serve same function across tasks.\n```\n\n### Entry 3: olsson2022_induction\n\n```yaml\n- id: olsson2022_induction\n  title: \"In-context Learning and Induction Heads\"\n  authors: \"Catherine Olsson, Nelson Elhage, Neel Nanda, et al.\"\n  year: 2022\n  venue: \"arXiv preprint (Anthropic)\"\n  arxiv_id: \"2209.11895\"\n  category: method-component\n  role: context\n  key_findings: >\n    Induction heads implement match-and-copy ([A][B]...[A]→[B]) and are mechanistic source of\n    in-context learning. Emerge at same training point as ICL ability phase transition.\n    Universal across model scales — canonical example of circuit-level universality.\n  relevance_to_us: >\n    Classic precedent for \"specific heads with universal function across contexts.\"\n    Our h13/h22 mixed heads are analogous: specific heads with consistent routing function across\n    task suites. Induction heads = algorithmic universality; our finding = routing universality in VLAs.\n  novelty_gap: >\n    Purely LLM, not VLA. Induction is a copying mechanism, not multimodal routing.\n    No cross-task consistency analysis in the fine-tuning setting.\n```\n\n---\n\n## Action Items\n\n1. **Add 3 entries above to literature_map.yaml** under appropriate categories (bali2026 + basile2025 → method-component; olsson2022 → method-component)\n2. **Update categories index** to include new papers\n3. **Paper framing**: The h13/h22 finding can be positioned as \"convergent routing heads\" — extending the induction head universality concept (Olsson 2022) from algorithmic circuits to multimodal routing in VLAs, with the Bali 2026 cross-run instability result as a foil that highlights the within-model cross-task nature of our claim\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-linkage-tracvla-4suite_20260521T204054",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/literature_linkage_4suite_consistency.md",
    "content": "# TracVLA 4-Suite Consistency: Literature Linkage Report\n\n**Date**: 2026-05-21\n\n---\n\n## Summary (< 200 words)\n\n**No direct competitor** reports cross-task/cross-suite attention head consistency in VLA models. The existing literature map (Grant 2026, Swann 2026, Haon 2025 等) focuses on behavioral intervention, SAE features, or activation steering — none tracks specific head indices across task suites.\n\n**h13/h22 universal mixed heads** lack direct precedent. The closest references are: (1) **Olsson et al. 2022** — induction heads as universal circuits across model scales, but these are algorithmic (pattern-matching), not routing-functional; (2) **Basile et al. 2025** (Head Pursuit, NeurIPS 2025 spotlight) — shows consistent head specialization in multimodal transformers, editing 1% of heads controls output, but does not track same-index heads across tasks; (3) **Bali et al. 2026** — finds middle-layer heads are *least* stable across independent training runs, which actually *strengthens* our claim: h13/h22 consistency is a training-induced convergent property within a model, not a trivial artifact of initialization.\n\n**3 papers recommended for literature_map.yaml** (see below). No paper discovers convergent routing with head identity preservation across task suites — this remains our unique contribution.\n\n---\n\n## Detailed Analysis\n\n### 1. Direct Competitor Check\n\nScanned all 9 direct-competitor entries in literature_map.yaml. None reports:\n- Cross-suite attention pattern consistency\n- Specific head indices with consistent function across tasks\n- Convergent routing (CF ordering, R² inverted-U, exit collapse) across suites\n\n**GuidedVLA (Jia et al., May 2026)** is the only VLA paper explicitly about attention head specialization, but they *engineer* it (supervised auxiliary signals for object/spatial/temporal heads), not *discover* it emergently. This is a useful contrast: we show VLA training naturally produces convergent routing without explicit supervision.\n\n### 2. h13/h22 Head Identity Preservation — Literature Support\n\n| Reference | Finding | Relation to h13/h22 |\n|-----------|---------|---------------------|\n| Olsson et al. 2022 | Induction heads are universal circuits across model scales | Precedent for functional universality at head level, but algorithmic (copy mechanism), not routing |\n| Basile et al. 2025 (Head Pursuit) | Consistent head specialization in multimodal transformers; 1% head editing controls output | Supports head-level functional specialization as real phenomenon; no same-index tracking across tasks |\n| Bali et al. 2026 | Middle-layer heads least stable across training runs, most representationally distinct | **Key contrast**: instability across runs ≠ instability across tasks within a run. Our h13/h22 consistency is *within-model cross-task*, a distinct (stronger) claim |\n| Bahador 2025 | ViT fine-tuning: deeper heads more important, intermediate heads monosemantic | Layer-level stratification consistent with our L1 instruction-dominant finding |\n| Yang et al. 2026 (TAPPA, ICLR 2026) | Unifies attention patterns via temporal predictability; predictable vs unpredictable patterns | Theoretical framework for *why* certain heads develop consistent patterns |\n\n**Bottom line**: Head specialization is well-established. Head identity preservation *across task suites within a fine-tuned VLA* is not. Our h13/h22 finding sits in a gap between \"heads specialize\" (known) and \"the same heads specialize the same way across diverse tasks\" (novel).\n\n### 3. Convergent Routing Pattern — Novelty Position\n\nThe full convergent routing pattern (CF ordering + R² inverted-U + exit collapse + L1 instruction dominance) across 3 architectures × 4 suites has no precedent. The closest work:\n- **Grant 2026**: Cross-architecture comparison but of *different* properties (vision dominance, language ignoring), not routing convergence\n- **Bali 2026**: Cross-run stability, not cross-task consistency\n- **Head Pursuit**: Cross-task head specialization in VLMs, not VLAs, and no routing pattern analysis\n\n---\n\n## Suggested literature_map.yaml Entries\n\n### Entry 1: bali2026\n\n```yaml\n- id: bali2026\n  title: \"Quantifying LLM Attention-Head Stability: Implications for Circuit Universality\"\n  authors: \"Karan Bali, Jack Stanley, Praneet Suresh, Danilo Bzdok\"\n  year: 2026\n  venue: \"arXiv preprint\"\n  arxiv_id: \"2602.16740\"\n  category: method-component\n  role: context\n  key_findings: >\n    Systematically quantifies attention head stability across independently initialized training runs.\n    Middle-layer heads are least stable yet most representationally distinct. Deeper models show\n    stronger mid-depth divergence. Weight decay improves stability. Residual stream comparatively stable.\n  relevance_to_us: >\n    Key contrast paper for h13/h22 universality claim. Their finding that heads are unstable across\n    training runs strengthens our claim: h13/h22 cross-task consistency is a training-induced convergent\n    property, not a trivial initialization artifact. Cross-run instability ≠ cross-task instability.\n  novelty_gap: >\n    Studies pre-trained LLMs across random seeds, not fine-tuned VLAs across task suites.\n    No cross-task consistency analysis within a single trained model.\n```\n\n### Entry 2: basile2025_headpursuit\n\n```yaml\n- id: basile2025_headpursuit\n  title: \"Head Pursuit: Probing Attention Specialization in Multimodal Transformers\"\n  authors: \"Lorenzo Basile, Valentino Maiorca, Diego Doimo, Francesco Locatello, Alberto Cazzaniga\"\n  year: 2025\n  venue: \"NeurIPS 2025 (Spotlight)\"\n  arxiv_id: \"2510.21518\"\n  category: method-component\n  role: methodology\n  key_findings: >\n    Consistent head specialization patterns in unimodal and multimodal transformers.\n    Signal processing-based method (SOMP) identifies semantic specialization per head.\n    Editing 1% of heads reliably suppresses/enhances targeted concepts.\n    Validated across QA, toxicity, image classification, captioning.\n  relevance_to_us: >\n    Strongest methodological support for head-level specialization as real phenomenon.\n    Their cross-task validation (QA + toxicity + vision tasks) parallels our cross-suite validation.\n    However they do not track same-index heads across tasks — our h13/h22 identity preservation goes further.\n  novelty_gap: >\n    VLM focus, not VLA. No routing pattern analysis. No trained vs untrained comparison.\n    Does not track whether same head indices serve same function across tasks.\n```\n\n### Entry 3: olsson2022_induction\n\n```yaml\n- id: olsson2022_induction\n  title: \"In-context Learning and Induction Heads\"\n  authors: \"Catherine Olsson, Nelson Elhage, Neel Nanda, et al.\"\n  year: 2022\n  venue: \"arXiv preprint (Anthropic)\"\n  arxiv_id: \"2209.11895\"\n  category: method-component\n  role: context\n  key_findings: >\n    Induction heads implement match-and-copy ([A][B]...[A]→[B]) and are mechanistic source of\n    in-context learning. Emerge at same training point as ICL ability phase transition.\n    Universal across model scales — canonical example of circuit-level universality.\n  relevance_to_us: >\n    Classic precedent for \"specific heads with universal function across contexts.\"\n    Our h13/h22 mixed heads are analogous: specific heads with consistent routing function across\n    task suites. Induction heads = algorithmic universality; our finding = routing universality in VLAs.\n  novelty_gap: >\n    Purely LLM, not VLA. Induction is a copying mechanism, not multimodal routing.\n    No cross-task consistency analysis in the fine-tuning setting.\n```\n\n---\n\n## Action Items\n\n1. **Add 3 entries above to literature_map.yaml** under appropriate categories (bali2026 + basile2025 → method-component; olsson2022 → method-component)\n2. **Update categories index** to include new papers\n3. **Paper framing**: The h13/h22 finding can be positioned as \"convergent routing heads\" — extending the induction head universality concept (Olsson 2022) from algorithmic circuits to multimodal routing in VLAs, with the Bali 2026 cross-run instability result as a foil that highlights the within-model cross-task nature of our claim\n"
  }
}
````

</details>

---

### Tool result

_source line 36 · 2026-05-21T20:43:42.947019+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/literature_linkage_4suite_consistency.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-linkage-tracvla-4suite_20260521T204054",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-21T20:43:42.947189+00:00_

产出文件已写入 `artifacts/literature_linkage_4suite_consistency.md`。核心结论：

**无直接竞品论文**报告过跨 task suite 的 attention head consistency pattern。现有 VLA 解释性文献（Grant/Swann/Haon/Rizzardo）全部聚焦行为干预或 SAE 特征，无人追踪 specific head indices 的跨任务一致性。

**h13/h22 head identity preservation 无直接先例**，但有三层文献支撑：
- **Olsson et al. 2022**（induction heads）：head 级功能普遍性的经典范例，但机制是 algorithmic copy，非 routing
- **Basile et al. 2025**（Head Pursuit, NeurIPS spotlight）：多模态 transformer 中 head 专化一致且可操控，但未追踪 same-index cross-task
- **Bali et al. 2026**：中间层 head 跨训练 run 最不稳定——这反而加强我们的 claim：h13/h22 的 cross-task 一致性是 training-induced convergent property，非初始化 artifact

**建议添加 3 条文献到 literature_map.yaml**（bali2026, basile2025_headpursuit, olsson2022_induction），详细条目见产出文件。

**GuidedVLA（Jia et al., 2026.05）**是唯一涉及 VLA attention head specialization 的论文，但它是人工监督强制的，非 emergent——可作为对照引用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_literature-linkage-tracvla-4suite_20260521T204054"
}
```

</details>

---
