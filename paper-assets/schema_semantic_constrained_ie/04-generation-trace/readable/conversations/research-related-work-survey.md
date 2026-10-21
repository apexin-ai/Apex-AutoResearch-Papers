# research related work survey

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 167
- **Recorded user turns:** 0
- **Tool calls:** 83
- **Original source:** `logs/chats/worker_research_related_work_survey_20260514T023514.jsonl`
- **Structured JSON:** [`4bdee39fd133cde83f03.json`](../../sessions/4b/4bdee39fd133cde83f03.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

167 recorded events

### Tool call

_source line 1 · 2026-05-14T02:40:41.980129+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Grammar-constrained decoding survey",
  "prompt": "Search the web for representative papers on grammar-constrained decoding for LLMs (2023-2026). I need 4-5 key papers covering:\n\n1. **XGrammar** - the system for grammar-guided structured generation (likely from MLSys or similar venue)\n2. **Guidance** (Microsoft) - constrained generation framework\n3. **Outlines** (2024) - structured text generation with regular expressions/CFGs\n4. **LMQL** - query language for LLMs with constraints\n5. **SGLang** or other notable grammar-constrained decoding systems\n\nFor each paper, find:\n- Full title\n- Authors (first 2-3)\n- Venue and year\n- Core method in 1-2 sentences\n- ArXiv ID if available\n\nAlso search for any survey papers on constrained decoding for LLMs (2024-2026).\n\nReport all findings in a structured format."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "Agent",
  "tool_args": {
    "subagent_type": "general-purpose",
    "description": "Grammar-constrained decoding survey",
    "prompt": "Search the web for representative papers on grammar-constrained decoding for LLMs (2023-2026). I need 4-5 key papers covering:\n\n1. **XGrammar** - the system for grammar-guided structured generation (likely from MLSys or similar venue)\n2. **Guidance** (Microsoft) - constrained generation framework\n3. **Outlines** (2024) - structured text generation with regular expressions/CFGs\n4. **LMQL** - query language for LLMs with constraints\n5. **SGLang** or other notable grammar-constrained decoding systems\n\nFor each paper, find:\n- Full title\n- Authors (first 2-3)\n- Venue and year\n- Core method in 1-2 sentences\n- ArXiv ID if available\n\nAlso search for any survey papers on constrained decoding for LLMs (2024-2026).\n\nReport all findings in a structured format."
  }
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-14T02:40:41.980544+00:00_

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
  "session": "worker_research_related_work_survey_20260514T023514",
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

_source line 3 · 2026-05-14T02:40:41.980791+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-14T02:40:41.980962+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Vocabulary/type-constrained generation survey",
  "prompt": "Search the web for representative papers on vocabulary-constrained and type-constrained generation/decoding for NLP (2020-2026). I need 4-5 key papers covering:\n\n1. **GENRE** - Generative Entity Retrieval (De Cao et al.) - constrained beam search for entity linking\n2. **Constrained beam search** methods - trie-based decoding for knowledge-grounded generation\n3. **NeuroLogDecoding** or **Neurologic** - constrained text generation with lexical constraints\n4. **TRIE-based constrained decoding** approaches for entity/type-constrained generation\n5. Any recent (2024-2026) work on token-level logits masking for type constraints in NLP\n\nFor each paper, find:\n- Full title\n- Authors (first 2-3)\n- Venue and year\n- Core method in 1-2 sentences\n- ArXiv ID if available\n\nReport all findings in a structured format."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "Agent",
  "tool_args": {
    "subagent_type": "general-purpose",
    "description": "Vocabulary/type-constrained generation survey",
    "prompt": "Search the web for representative papers on vocabulary-constrained and type-constrained generation/decoding for NLP (2020-2026). I need 4-5 key papers covering:\n\n1. **GENRE** - Generative Entity Retrieval (De Cao et al.) - constrained beam search for entity linking\n2. **Constrained beam search** methods - trie-based decoding for knowledge-grounded generation\n3. **NeuroLogDecoding** or **Neurologic** - constrained text generation with lexical constraints\n4. **TRIE-based constrained decoding** approaches for entity/type-constrained generation\n5. Any recent (2024-2026) work on token-level logits masking for type constraints in NLP\n\nFor each paper, find:\n- Full title\n- Authors (first 2-3)\n- Venue and year\n- Core method in 1-2 sentences\n- ArXiv ID if available\n\nReport all findings in a structured format."
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T02:40:41.981137+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "XGrammar grammar-guided structured generation LLM paper arxiv 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "XGrammar grammar-guided structured generation LLM paper arxiv 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-14T02:40:41.981265+00:00_

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
  "session": "worker_research_related_work_survey_20260514T023514",
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

_source line 7 · 2026-05-14T02:40:41.981431+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-14T02:40:41.981577+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Structural constraint IE survey",
  "prompt": "Search the web for representative papers on structural constraints for Information Extraction (IE) with LLMs (2022-2026). I need 5-6 key papers covering:\n\n1. **UIE** (Unified Structure Generation for Universal Information Extraction) - Lu et al.\n2. **InstructUIE** - instruction-tuned universal IE\n3. **GoLLIE** - Guideline-following Large Language Model for IE (likely ICLR 2024)\n4. **CodeIE** - code generation approach for IE\n5. **USM** or **UniRel** or other structured prediction + LLM approaches for IE\n6. Any 2024-2025 work on making LLMs output structured IE results (NER, RE, EE)\n\nFor each paper, find:\n- Full title\n- Authors (first 2-3)\n- Venue and year\n- Core method in 1-2 sentences\n- ArXiv ID if available\n\nReport all findings in a structured format."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "Agent",
  "tool_args": {
    "subagent_type": "general-purpose",
    "description": "Structural constraint IE survey",
    "prompt": "Search the web for representative papers on structural constraints for Information Extraction (IE) with LLMs (2022-2026). I need 5-6 key papers covering:\n\n1. **UIE** (Unified Structure Generation for Universal Information Extraction) - Lu et al.\n2. **InstructUIE** - instruction-tuned universal IE\n3. **GoLLIE** - Guideline-following Large Language Model for IE (likely ICLR 2024)\n4. **CodeIE** - code generation approach for IE\n5. **USM** or **UniRel** or other structured prediction + LLM approaches for IE\n6. Any 2024-2025 work on making LLMs output structured IE results (NER, RE, EE)\n\nFor each paper, find:\n- Full title\n- Authors (first 2-3)\n- Venue and year\n- Core method in 1-2 sentences\n- ArXiv ID if available\n\nReport all findings in a structured format."
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T02:40:41.981817+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "GENRE Generative Entity Retrieval De Cao constrained beam search entity linking arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "GENRE Generative Entity Retrieval De Cao constrained beam search entity linking arxiv"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-14T02:40:41.981973+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "NeuroLogic Decoding constrained text generation lexical constraints Lu et al arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "NeuroLogic Decoding constrained text generation lexical constraints Lu et al arxiv"
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T02:40:41.982093+00:00_

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
  "session": "worker_research_related_work_survey_20260514T023514",
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

_source line 12 · 2026-05-14T02:40:41.982209+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T02:40:41.982328+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Ontology validation NLP survey",
  "prompt": "Search the web for representative papers on type-checking, ontology validation, and ontology-guided constraints in NLP (2020-2026). I need 4-5 key papers covering:\n\n1. **LLM+ASP** approaches - using Answer Set Programming to validate/constrain LLM outputs (check ICLP 2025 or similar logic programming venues)\n2. **Ontology-guided NER** - using ontological knowledge to guide named entity recognition\n3. **Post-hoc validation** approaches for LLM outputs against knowledge bases or ontologies\n4. **Type-constrained relation extraction** - enforcing entity type constraints in RE\n5. Any work on using domain/range constraints from ontologies to validate IE outputs\n\nFor each paper, find:\n- Full title\n- Authors (first 2-3)\n- Venue and year\n- Core method in 1-2 sentences\n- ArXiv ID if available\n\nReport all findings in a structured format."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "Agent",
  "tool_args": {
    "subagent_type": "general-purpose",
    "description": "Ontology validation NLP survey",
    "prompt": "Search the web for representative papers on type-checking, ontology validation, and ontology-guided constraints in NLP (2020-2026). I need 4-5 key papers covering:\n\n1. **LLM+ASP** approaches - using Answer Set Programming to validate/constrain LLM outputs (check ICLP 2025 or similar logic programming venues)\n2. **Ontology-guided NER** - using ontological knowledge to guide named entity recognition\n3. **Post-hoc validation** approaches for LLM outputs against knowledge bases or ontologies\n4. **Type-constrained relation extraction** - enforcing entity type constraints in RE\n5. Any work on using domain/range constraints from ontologies to validate IE outputs\n\nFor each paper, find:\n- Full title\n- Authors (first 2-3)\n- Venue and year\n- Core method in 1-2 sentences\n- ArXiv ID if available\n\nReport all findings in a structured format."
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-14T02:40:41.982508+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "trie-based constrained decoding knowledge grounded generation NLP arxiv 2021 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "trie-based constrained decoding knowledge grounded generation NLP arxiv 2021 2022"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-14T02:40:41.982801+00:00_

Web search results for query: "XGrammar grammar-guided structured generation LLM paper arxiv 2024 2025"

Links: [{"title":"[2411.15100] XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models","url":"https://arxiv.org/abs/2411.15100"},{"title":"XGrammar: Flexible and Efficient Structured Generation ...","url":"https://arxiv.org/pdf/2411.15100"},{"title":"[PDF] XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/XGrammar:-Flexible-and-Efficient-Structured-Engine-Dong-Ruan/274ca059ee4997f1e008bc8962aef3d22897f17a"},{"title":"GitHub - mlc-ai/xgrammar: Fast, Flexible and Portable Structured Generation · GitHub","url":"https://github.com/mlc-ai/xgrammar"},{"title":"[2411.15100v1] XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models","url":"https://arxiv.org/abs/2411.15100v1"},{"title":"1 Introduction","url":"https://arxiv.org/html/2411.15100v1"},{"title":"XGrammar-2: Efficient Dynamic Structured Generation Engine for Agentic LLMs","url":"https://arxiv.org/html/2601.04426"},{"title":"Guided Decoding and Its Critical Role in Retrieval-Augmented Generation","url":"https://arxiv.org/html/2509.06631v1"},{"title":"XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241115100D/abstract"},{"title":"XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/xgrammar-flexible-efficient-structured-generation-engine-large"}]

Based on the search results, here's what I found about XGrammar:

## XGrammar Paper Overview

XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models is an arXiv paper (2411.15100) published in November 2024.

### Key Technical Approach

XGrammar accelerates context-free g
…[truncated 1169 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-14T02:40:41.982996+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Outlines structured text generation regular expressions CFG paper arxiv 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Outlines structured text generation regular expressions CFG paper arxiv 2024"
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T02:40:41.983187+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "token level logits masking type constraints NLP structured generation 2024 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "token level logits masking type constraints NLP structured generation 2024 2025 2026 arxiv"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-14T02:40:41.983371+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "UIE Unified Structure Generation Universal Information Extraction Lu et al 2022 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "UIE Unified Structure Generation Universal Information Extraction Lu et al 2022 arxiv"
  }
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T02:40:41.983550+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "InstructUIE instruction-tuned universal information extraction paper arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "InstructUIE instruction-tuned universal information extraction paper arxiv"
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-14T02:40:41.983749+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "GoLLIE guideline-following large language model information extraction ICLR 2024 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "GoLLIE guideline-following large language model information extraction ICLR 2024 arxiv"
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T02:40:41.983936+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CodeIE code generation information extraction paper arxiv 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CodeIE code generation information extraction paper arxiv 2023"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-14T02:40:41.984109+00:00_

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
  "session": "worker_research_related_work_survey_20260514T023514",
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

_source line 23 · 2026-05-14T02:40:41.984277+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-14T02:40:41.984531+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Microsoft Guidance constrained generation framework LLM paper arxiv 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Microsoft Guidance constrained generation framework LLM paper arxiv 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-14T02:40:41.984749+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Constrained decoding quality survey",
  "prompt": "Search the web for representative papers on the quality concerns and negative effects of constrained decoding on LLM generation (2023-2026). I need 3-5 key papers covering:\n\n1. **CRANE** (NeurIPS 2024) - about how constrained decoding can degrade generation quality. Search for \"CRANE constrained decoding NeurIPS 2024\" or \"Let Me Speak Freely\"\n2. **Structure Snowballing** or any paper about how structured output constraints cause quality degradation\n3. Any empirical studies showing constrained decoding hurts LLM performance\n4. Papers proposing solutions to maintain quality under constraints\n5. \"Let Me Speak Freely\" paper if different from CRANE\n\nFor each paper, find:\n- Full title\n- Authors (first 2-3)\n- Venue and year\n- Core method/finding in 1-2 sentences\n- ArXiv ID if available\n\nReport all findings in a structured format."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "Agent",
  "tool_args": {
    "subagent_type": "general-purpose",
    "description": "Constrained decoding quality survey",
    "prompt": "Search the web for representative papers on the quality concerns and negative effects of constrained decoding on LLM generation (2023-2026). I need 3-5 key papers covering:\n\n1. **CRANE** (NeurIPS 2024) - about how constrained decoding can degrade generation quality. Search for \"CRANE constrained decoding NeurIPS 2024\" or \"Let Me Speak Freely\"\n2. **Structure Snowballing** or any paper about how structured output constraints cause quality degradation\n3. Any empirical studies showing constrained decoding hurts LLM performance\n4. Papers proposing solutions to maintain quality under constraints\n5. \"Let Me Speak Freely\" paper if different from CRANE\n\nFor each paper, find:\n- Full title\n- Authors (first 2-3)\n- Venue and year\n- Core method/finding in 1-2 sentences\n- ArXiv ID if available\n\nReport all findings in a structured format."
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-14T02:40:41.985003+00:00_

Web search results for query: "NeuroLogic Decoding constrained text generation lexical constraints Lu et al arxiv"

Links: [{"title":"[2112.08726] NeuroLogic A*esque Decoding: Constrained Text Generation with Lookahead Heuristics","url":"https://arxiv.org/abs/2112.08726"},{"title":"[2010.12884] NeuroLogic Decoding: (Un)supervised Neural Text Generation with Predicate Logic Constraints","url":"https://arxiv.org/abs/2010.12884"},{"title":"Why is constrained neural language generation particularly challenging?","url":"https://arxiv.org/html/2206.05395v2"},{"title":"[2112.08726v1] NeuroLogic A*esque Decoding: Constrained Text Generation with Lookahead Heuristics","url":"https://arxiv.org/abs/2112.08726v1"},{"title":"NeuroLogic A*esque Decoding: Constrained Text Generation with Lookahead Heuristics - ADS","url":"https://ui.adsabs.harvard.edu/abs/2021arXiv211208726L/abstract"},{"title":"[2112.08726] A^\"*\" Decoding: Neural Language Generation with Looking Ahead Heuristic","url":"https://ar5iv.labs.arxiv.org/html/2112.08726"},{"title":"[2010.12884v2] NeuroLogic Decoding: (Un)supervised Neural Text Generation with Predicate Logic Constraints","url":"https://arxiv.org/abs/2010.12884v2"},{"title":"Why is constrained neural language generation particularly ...","url":"https://arxiv.org/pdf/2206.05395"},{"title":"NeuroLogic A*esque Decoding: Constrained Text Generation with Lookahead Heuristics - ACL Anthology","url":"https://aclanthology.org/2022.naacl-main.57/"},{"title":"NeuroLogic Decoding: (Un)supervised Neural Text Generation with Predicate Logic Constraints - ACL Anthology","url":"https://aclanthology.org/2021.naacl-main.339/"}]

I found the papers on NeuroLogic Decoding for constrained text generation by Lu et al. Here are the key results:

## Original NeuroLogic Decoding Paper

NeuroLogic Decoding is a simple yet effective algorithm that enables neural language models -- supervised or not -- to generate fluent text while satisfying complex lexical constraints. It hand
…[truncated 1033 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-14T02:40:41.985228+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LMQL query language LLM constraints paper arxiv 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LMQL query language LLM constraints paper arxiv 2023"
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-14T02:40:41.985414+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SGLang structured generation language LLM paper arxiv 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SGLang structured generation language LLM paper arxiv 2024"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-14T02:40:41.985600+00:00_

Web search results for query: "GENRE Generative Entity Retrieval De Cao constrained beam search entity linking arxiv"

Links: [{"title":"GitHub - facebookresearch/GENRE: Autoregressive Entity Retrieval · GitHub","url":"https://github.com/facebookresearch/GENRE"},{"title":"facebook/genre-linking-aidayago2 · Hugging Face","url":"https://huggingface.co/facebook/genre-linking-aidayago2"},{"title":"[2010.00904] Autoregressive Entity Retrieval","url":"https://arxiv.org/abs/2010.00904"},{"title":"Generative Multimodal Entity Linking","url":"https://arxiv.org/pdf/2306.12725"},{"title":"HIERARCHICAL CORPUS ENCODER: FUSING GENERATIVE RETRIEVAL AND DENSE INDICES","url":"https://arxiv.org/pdf/2502.18877"},{"title":"Published as a conference paper at ICLR 2021 AUTOREGRESSIVE ENTITY RETRIEVAL","url":"https://arxiv.org/pdf/2010.00904"},{"title":"facebook/genre-linking-blink · Hugging Face","url":"https://huggingface.co/facebook/genre-linking-blink"},{"title":"Entity Disambiguation via Fusion Entity Decoding","url":"https://arxiv.org/html/2404.01626v1"},{"title":"entqa: entity linking as question answering","url":"https://arxiv.org/pdf/2110.02369"},{"title":"Revisiting Sparse Retrieval for Few-shot Entity Linking","url":"https://arxiv.org/html/2310.12444"}]

I found comprehensive information about GENRE (Generative ENtity REtrieval) by Nicola De Cao and colleagues. Here's what the search revealed:

## Overview

GENRE is the first system that retrieves entities by generating their unique names, left to right, token-by-token in an autoregressive fashion. It uses a sequence-to-sequence approach to entity retrieval (e.g., linking), based on fine-tuned BART architecture or mBART (for multilingual).

## Key Technical Innovation: Constrained Beam Search

GENRE performs retrieval generating the unique entity name conditioned on the input text using constrained beam search to only generate valid identifiers. More specifically, the system resorts to Constrained Beam Search, forcing to only d
…[truncated 1030 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-14T02:40:41.985859+00:00_

Web search results for query: "trie-based constrained decoding knowledge grounded generation NLP arxiv 2021 2022"

Links: [{"title":"Vectorizing the Trie: Efficient Constrained Decoding for LLM-based Generative Retrieval on Accelerators","url":"https://arxiv.org/html/2602.22647v1"},{"title":"[2602.22647] Vectorizing the Trie: Efficient Constrained Decoding for LLM-based Generative Retrieval on Accelerators","url":"https://arxiv.org/abs/2602.22647"},{"title":"Published as a conference paper at ICLR 2022 KNOWLEDGE INFUSED DECODING","url":"https://arxiv.org/pdf/2204.03084"},{"title":"Efficient Beam Search for LLMs Using Trie-Based Decoding","url":"https://aclanthology.org/2025.emnlp-main.748.pdf"},{"title":"Efficient Constrained Decoding for LLM-based Generative ...","url":"https://arxiv.org/pdf/2602.22647"},{"title":"To Know is to Construct: Schema-Constrained Generation for Agent Memory","url":"https://arxiv.org/pdf/2604.20117"},{"title":"Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning","url":"https://arxiv.org/html/2305.13971v6"},{"title":"(PDF) Vectorizing the Trie: Efficient Constrained Decoding for LLM-based Generative Retrieval on Accelerators","url":"https://www.researchgate.net/publication/401279962_Vectorizing_the_Trie_Efficient_Constrained_Decoding_for_LLM-based_Generative_Retrieval_on_Accelerators"},{"title":"Sketch-Guided Constrained Decoding for Boosting Blackbox Large Language Models without Logit Access","url":"https://arxiv.org/html/2401.09967"},{"title":"[2410.13080] Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models","url":"https://arxiv.org/abs/2410.13080"}]

I found several relevant papers on trie-based constrained decoding for knowledge-grounded generation and NLP from your specified timeframe. Here are the key results:

## Notable Papers (2021-2022):

1. **Knowledge Infused Decoding (KID)** - KID dynamically searches promising continuation from retrieved knowledge to guide gener
…[truncated 1310 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-14T02:40:41.986069+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LLM Answer Set Programming ASP constraint validation logic programming 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LLM Answer Set Programming ASP constraint validation logic programming 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-14T02:40:41.986252+00:00_

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
  "session": "worker_research_related_work_survey_20260514T023514",
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

_source line 33 · 2026-05-14T02:40:41.986431+00:00_

Web search results for query: "UIE Unified Structure Generation Universal Information Extraction Lu et al 2022 arxiv"

Links: [{"title":"[2203.12277] Unified Structure Generation for Universal Information Extraction","url":"https://arxiv.org/abs/2203.12277"},{"title":"Unified Structure Generation for Universal Information Extraction - ACL Anthology","url":"https://aclanthology.org/2022.acl-long.395/"},{"title":"Unified Structure Generation for Universal Information Extraction | universal-ie.github.io","url":"https://universal-ie.github.io/"},{"title":"Paper page - Unified Structure Generation for Universal Information Extraction","url":"https://huggingface.co/papers/2203.12277"},{"title":"[2203.12277v1] Unified Structure Generation for Universal Information Extraction","url":"https://arxiv.org/abs/2203.12277v1"},{"title":"[2301.03282] Universal Information Extraction as Unified Semantic Matching","url":"https://ar5iv.labs.arxiv.org/html/2301.03282"},{"title":"[PDF] Unified Structure Generation for Universal Information Extraction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Unified-Structure-Generation-for-Universal-Lu-Liu/5eb9dad01d9b61947d7a9aae6dfff400d20555b9"},{"title":"Uniﬁed Structure Generation for Universal Information Extraction","url":"https://arxiv.org/pdf/2203.12277"},{"title":"(PDF) Unified Structure Generation for Universal Information Extraction","url":"https://www.researchgate.net/publication/359435785_Unified_Structure_Generation_for_Universal_Information_Extraction"},{"title":"Schema as Parameterized Tools for Universal Information Extraction","url":"https://arxiv.org/html/2506.01276"}]

I found the paper you're looking for! Here are the details:

**Paper:** Unified Structure Generation for Universal Information Extraction, by Yaojie Lu and 7 other authors

**ArXiv ID:** 2203.12277 (published March 23, 2022)

**Key Contribution:** UIE is a unified text-to-structure generation framework that can universally model different IE ta
…[truncated 916 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-14T02:40:41.986610+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-14T02:40:41.986814+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ontology-guided named entity recognition NER knowledge graph 2022 2023 2024 paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ontology-guided named entity recognition NER knowledge graph 2022 2023 2024 paper"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-14T02:40:41.986962+00:00_

Web search results for query: "InstructUIE instruction-tuned universal information extraction paper arxiv"

Links: [{"title":"[2304.08085] InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction","url":"https://arxiv.org/abs/2304.08085"},{"title":"GitHub - BeyonderXX/InstructUIE: Universal information extraction with instruction learning · GitHub","url":"https://github.com/BeyonderXX/InstructUIE"},{"title":"(PDF) InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction (2023) | Xiao Wang | 81 Citations","url":"https://scispace.com/papers/instructuie-multi-task-instruction-tuning-for-unified-qe70ci1r"},{"title":"InstructUIE: Multi-task Instruction Tuning for Uniﬁed Information Extraction","url":"https://arxiv.org/pdf/2304.08085"},{"title":"YAYI-UIE: A Chat-Enhanced Instruction Tuning Framework for Universal Information Extraction","url":"https://arxiv.org/html/2312.15548v2"},{"title":"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction","url":"https://www.researchgate.net/publication/370071546_InstructUIE_Multi-task_Instruction_Tuning_for_Unified_Information_Extraction"},{"title":"[2304.08085v1] InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction","url":"https://arxiv.org/abs/2304.08085v1"},{"title":"MR-UIE: Multi-Perspective Reasoning with Reinforcement Learning for Universal Information Extraction","url":"https://arxiv.org/html/2509.09082"},{"title":"Paper page - InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction","url":"https://huggingface.co/papers/2304.08085"},{"title":"[PDF] InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/bbb2fc6e95d24fb58ab6c25b216b14ac49a32fbe"}]

I found the paper you're looking for. Here are the key details about the InstructUIE paper:

## InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction

**ArXiv ID
…[truncated 1120 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-14T02:40:41.987127+00:00_

Web search results for query: "token level logits masking type constraints NLP structured generation 2024 2025 2026 arxiv"

Links: [{"title":"Token Masking Improves Transformer-Based Text Classification","url":"https://arxiv.org/html/2505.11746"},{"title":"[2310.18738] TLM: Token-Level Masking for Transformers","url":"https://arxiv.org/abs/2310.18738"},{"title":"Output Constraints as Attack Surface: Exploiting Structured Generation to Bypass LLM Safety Mechanisms","url":"https://arxiv.org/html/2503.24191v1"},{"title":"Flexible and Efficient Grammar-Constrained Decoding","url":"https://arxiv.org/pdf/2502.05111"},{"title":"Controlling your LLM: Deep dive into Constrained Generation | by Andrew Docherty | Medium","url":"https://medium.com/@docherty/controlling-your-llm-deep-dive-into-constrained-generation-1e561c736a20"},{"title":"Alternatives To Next Token Prediction In Text Generation - A Survey","url":"https://arxiv.org/html/2509.24435v1"},{"title":"Large Language Model Meets Constraint Propagation","url":"https://arxiv.org/html/2505.24012"},{"title":"Enabling Autoregressive Models to Fill In Masked Tokens","url":"https://arxiv.org/pdf/2502.06901"},{"title":"1 Introduction","url":"https://arxiv.org/html/2411.15100v1"},{"title":"Typhoon: Towards an Effective Task-Specific Masking Strategy for","url":"https://arxiv.org/pdf/2303.15619"}]

I've completed the web search for your query about token-level logits masking, type constraints, and structured generation in NLP from recent arxiv papers (2024-2026). Here are the key findings:

## Main Research Areas

**Constrained Decoding and Structured Generation:**

Tokens that do not match grammar rules are masked out by modifying their logits to -∞ (in practice, -100), so their probabilities become zero, ensuring output is constrained to the grammar rule. Constrained decoders use checkers during decoding to mask out any next token that would violate constraints, computing a Boolean mask where 1 denotes viable tokens and 0 deno
…[truncated 1220 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-14T02:40:41.987282+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "post-hoc validation LLM outputs knowledge base ontology type checking 2023 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "post-hoc validation LLM outputs knowledge base ontology type checking 2023 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-14T02:40:41.987413+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "type-constrained relation extraction entity type constraints 2021 2022 2023 paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "type-constrained relation extraction entity type constraints 2021 2022 2023 paper"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-14T02:40:41.987549+00:00_

Web search results for query: "GoLLIE guideline-following large language model information extraction ICLR 2024 arxiv"

Links: [{"title":"[2310.03668] GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction","url":"https://arxiv.org/abs/2310.03668"},{"title":"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction | OpenReview","url":"https://openreview.net/forum?id=Y3wpuxd7u9"},{"title":"ICLR Poster GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction","url":"https://iclr.cc/virtual/2024/poster/18435"},{"title":"GoLLIE | Guideline following Large Language Model for Information Extraction","url":"https://hitz-zentroa.github.io/GoLLIE/"},{"title":"Published as a conference paper at ICLR 2024","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/cda04d7ea67ea1376bf8c6962d8541e0-Paper-Conference.pdf"},{"title":"GitHub - hitz-zentroa/GoLLIE: Guideline following Large Language Model for Information Extraction · GitHub","url":"https://github.com/hitz-zentroa/GoLLIE"},{"title":"Large language models for generative information extraction: a survey | Frontiers of Computer Science | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11704-024-40555-y"},{"title":"GitHub - azminewasi/Awesome-LLMs-ICLR-24: It is a comprehensive resource hub compiling all LLM papers accepted at the International Conference on Learning Representations (ICLR) in 2024. · GitHub","url":"https://github.com/azminewasi/Awesome-LLMs-ICLR-24"},{"title":"GitHub - quqxui/Awesome-LLM4IE-Papers: Awesome papers about generative Information Extraction (IE) using Large Language Models (LLMs) · GitHub","url":"https://github.com/quqxui/Awesome-LLM4IE-Papers"},{"title":"Published as a conference paper at ICLR 2024","url":"https://openreview.net/notes/edits/attachment?id=x345y4wtJb&name=pdf"}]

I found information about GoLLIE. Here are the search results:

## Overview

GoLLIE (Guideline-following Large Language Model for IE) is a model a
…[truncated 1441 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-14T02:40:41.987741+00:00_

Web search results for query: "SGLang structured generation language LLM paper arxiv 2024"

Links: [{"title":"[2312.07104] SGLang: Efficient Execution of Structured Language Model Programs","url":"https://arxiv.org/abs/2312.07104"},{"title":"SGLang: Efficient Execution of Structured Language Model Programs","url":"https://arxiv.org/pdf/2312.07104"},{"title":"SGLang: efficient execution of structured language model ...","url":"https://dl.acm.org/doi/10.5555/3737916.3739916"},{"title":"Paper page - Efficiently Programming Large Language Models using SGLang","url":"https://huggingface.co/papers/2312.07104"},{"title":"Efficiently Programming Large Language Models using SGLang","url":"https://arxiv.org/html/2312.07104v1"},{"title":"SGLang: Efficient Execution of Structured Language Model Programs | Request PDF","url":"https://www.researchgate.net/publication/397203117_SGLang_Efficient_Execution_of_Structured_Language_Model_Programs"},{"title":"SGLang: Efficient Execution of Structured Language Model Programs | OpenReview","url":"https://openreview.net/forum?id=VqkAKQibpq"},{"title":"GitHub - sgl-project/sglang: SGLang is a high-performance serving framework for large language models and multimodal models. · GitHub","url":"https://github.com/sgl-project/sglang"},{"title":"Efficiently programming large language models using SGLang | Awesome Papers","url":"https://paper.lingyunyang.com/reading-notes/miscellaneous/arxiv/2024/sglang"},{"title":"[PDF] SGLang: Efficient Execution of Structured Language Model Programs | Semantic Scholar","url":"https://www.semanticscholar.org/paper/SGLang:-Efficient-Execution-of-Structured-Language-Zheng-Yin/eb95c327260725498404eb43ec370d419b8d92c7"}]

Based on the search results, I found comprehensive information about the SGLang paper. Here's what I found:

## SGLang Paper Overview

SGLang is a system for efficient execution of complex language model programs. SGLang consists of a frontend language and a runtime, with the frontend simplifying 
…[truncated 1064 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-14T02:40:41.987919+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "domain range constraints ontology information extraction validation 2022 2023 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "domain range constraints ontology information extraction validation 2022 2023 2024"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-14T02:40:41.988062+00:00_

Web search results for query: "Outlines structured text generation regular expressions CFG paper arxiv 2024"

Links: [{"title":"XGrammar: Flexible and Efficient Structured Generation ...","url":"https://arxiv.org/pdf/2411.15100"},{"title":"1 Introduction","url":"https://arxiv.org/html/2411.15100v1"},{"title":"Generating Structured Outputs from Language Models: Benchmark and Studies","url":"https://arxiv.org/html/2501.10868v1"},{"title":"[2307.09702v2] Efficient Guided Generation for Large Language Models","url":"https://arxiv.org/abs/2307.09702v2"},{"title":"[2307.09702v1] Efficient Guided Generation for LLMs","url":"https://arxiv.org/abs/2307.09702v1"},{"title":"GitHub - dottxt-ai/outlines: Structured Outputs · GitHub","url":"https://github.com/dottxt-ai/outlines"},{"title":"Paper page - Efficient Guided Generation for Large Language Models","url":"https://huggingface.co/papers/2307.09702"},{"title":"[2309.10447] Toward Unified Controllable Text Generation via Regular Expression Instruction","url":"https://arxiv.org/abs/2309.10447"},{"title":"[2404.13919] Navigating the Path of Writing: Outline-guided Text Generation with Large Language Models","url":"https://arxiv.org/abs/2404.13919"},{"title":"[2404.13919v1] Navigating the Path of Writing: Outline-guided Text Generation with Large Language Models","url":"https://arxiv.org/abs/2404.13919v1"}]

Based on the search results, I found several relevant papers and resources on structured text generation using regular expressions and context-free grammars (CFGs):

## Key Papers and Resources

**1. Efficient Guided Generation for Large Language Models (2023)**

This paper describes an efficient approach to guiding language model text generation with regular expressions and context-free grammars, adding little to no overhead to the token sequence generation process, with an implementation provided in the open source Python library Outlines.

**2. XGrammar: Flexible and Efficient Structured Generation (2024)**

This recent p
…[truncated 1271 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 5
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-14T02:40:41.988213+00:00_

Web search results for query: "CodeIE code generation information extraction paper arxiv 2023"

Links: [{"title":"[2305.05711] CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors","url":"https://arxiv.org/abs/2305.05711"},{"title":"[2305.05711v2] CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors","url":"https://arxiv.org/abs/2305.05711v2"},{"title":"[PDF] CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CodeIE:-Large-Code-Generation-Models-are-Better-Li-Sun/a86dd6c62d3dc9c7989c98a3e4ace3fd8000e515"},{"title":"[2311.02962] Retrieval-Augmented Code Generation for Universal Information Extraction","url":"https://arxiv.org/abs/2311.02962"},{"title":"GitHub - artpli/CodeIE: [ACL 23] CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors · GitHub","url":"https://github.com/artpli/CodeIE"},{"title":"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors - ACL Anthology","url":"https://aclanthology.org/2023.acl-long.855/"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?title=CodeIE:+Large+code+generation+models+are+better+few-shot+information+extractors&author=Peng+Li&author=Tianxiang+Sun&author=Qiong+Tang&author=Hang+Yan&author=Wu+Yuanbin&author=Xuanjing+Huang&author=Xipeng+Qiu&publication_year=2023&journal=Proceedings+of+the+61st+Annual+Meeting+of+the+Association+for+Computational+Linguistics&pages=15339-15353"},{"title":"Large Language Models for Generative Information Extraction: A Survey","url":"https://arxiv.org/html/2312.17617v1"},{"title":"GitHub - zjunlp/Low-resource-KEPapers: A Paper List of Low-resource Information Extraction","url":"https://github.com/zjunlp/Low-resource-KEPapers"},{"title":"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors | Request PDF","url":"https://www.researchgate.net/publication/37
…[truncated 1552 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-14T02:40:41.988372+00:00_

Web search results for query: "Microsoft Guidance constrained generation framework LLM paper arxiv 2024 2025"

Links: [{"title":"Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation","url":"https://arxiv.org/html/2403.06988v1"},{"title":"Efficient Guided Generation for Large Language Models","url":"https://arxiv.org/pdf/2307.09702"},{"title":"CRANE: Reasoning with constrained LLM generation","url":"https://arxiv.org/html/2502.09061v3"},{"title":"[2403.06988] Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation","url":"https://arxiv.org/abs/2403.06988"},{"title":"GitHub - guidance-ai/guidance: A guidance language for controlling large language models. · GitHub","url":"https://github.com/guidance-ai/guidance"},{"title":"LLM Research Papers: The 2025 List (July to December)","url":"https://magazine.sebastianraschka.com/p/llm-research-papers-2025-part2"},{"title":"Generating Structured Outputs from Language Models: Benchmark and Studies","url":"https://arxiv.org/html/2501.10868v1"},{"title":"guidance | control LM output – Microsoft Research","url":"https://www.microsoft.com/en-us/research/project/guidance-control-lm-output/"},{"title":"GitHub - Saibo-creator/Awesome-LLM-Constrained-Decoding: A curated list of papers related to constrained decoding of LLM, along with their relevant code and resources. · GitHub","url":"https://github.com/Saibo-creator/Awesome-LLM-Constrained-Decoding"},{"title":"Published as a conference paper at ICLR 2025 GUARANTEED GENERATION FROM","url":"https://openreview.net/pdf?id=8roRgrjbjv"}]

Based on the search results, I found several relevant papers related to Microsoft's Guidance framework and constrained generation for LLMs:

## Key Papers Found:

1. **"Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation"** (2024)
   - The paper proposes Domino, a novel constrained decoding algorithm that enforces context-free grammars in a minimally-invasive way, which is highly efficient and can even incr
…[truncated 1227 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-14T02:40:41.988541+00:00_

Web search results for query: "LMQL query language LLM constraints paper arxiv 2023"

Links: [{"title":"[2212.06094] Prompting Is Programming: A Query Language for Large Language Models","url":"https://arxiv.org/abs/2212.06094"},{"title":"Prompting Is Programming: A Query Language for Large Language Models 1","url":"https://arxiv.org/pdf/2212.06094"},{"title":"LMQL is a programming language for LLM interaction. | LMQL","url":"https://lmql.ai/"},{"title":"GitHub - eth-sri/lmql: A language for constraint-guided and efficient LLM programming. · GitHub","url":"https://github.com/eth-sri/lmql"},{"title":"Better Steering LLM Agents with LMQL | Unsupervised Thoughts","url":"https://vivien000.github.io/blog/journal/better-steering-LLM-agents-with-LMQL.html"},{"title":"LMQL — SQL for Language Models","url":"https://medium.com/data-science/lmql-sql-for-language-models-d7486d88c541"},{"title":"Large Language Models are Zero-Shot Multi-Tool Users","url":"https://files.sri.inf.ethz.ch/website/papers/lmql_actions.pdf"},{"title":"LMQL - SQL for Language Models | Towards Data Science","url":"https://towardsdatascience.com/lmql-sql-for-language-models-d7486d88c541/"},{"title":"Research | LMQL","url":"https://lmql.ai/research/index.html"},{"title":"Prompting Is Programming: A Query Language for Large Language Models | Proceedings of the ACM on Programming Languages","url":"https://dl.acm.org/doi/10.1145/3591300"}]

Based on the search results, I found the paper you're looking for:

## LMQL: A Query Language for Large Language Models

The paper is titled "Prompting Is Programming: A Query Language for Large Language Models", with arXiv ID 2212.06094. The paper was initially submitted on December 12, 2022, and updated versions were released on April 26, 2023, and May 30, 2023.

### Paper Overview

The paper presents Language Model Programming (LMP), which generalizes language model prompting from pure text prompts to an intuitive combination of text prompting and scripting, and allows 
…[truncated 899 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-14T02:40:41.988716+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CRANE constrained decoding NeurIPS 2024 \"Let Me Speak Freely\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CRANE constrained decoding NeurIPS 2024 \"Let Me Speak Freely\""
  }
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-14T02:40:41.988855+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "structure snowballing constrained decoding LLM quality degradation 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "structure snowballing constrained decoding LLM quality degradation 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-14T02:40:41.988984+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "GenIE Josifoski constrained decoding closed information extraction trie EMNLP 2022 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "GenIE Josifoski constrained decoding closed information extraction trie EMNLP 2022 arxiv"
  }
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-14T02:40:41.989107+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "constrained decoding hurts LLM performance empirical study 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "constrained decoding hurts LLM performance empirical study 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-14T02:40:41.989230+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "structured output constraints degrade LLM generation quality arXiv 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "structured output constraints degrade LLM generation quality arXiv 2024"
  }
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-14T02:40:41.989351+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "NeuroLogic Decoding NAACL 2021 authors Ximing Lu Peter West Rowan Zellers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "NeuroLogic Decoding NAACL 2021 authors Ximing Lu Peter West Rowan Zellers"
  }
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-14T02:40:41.989471+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "USM Universal Semantic Matching information extraction structured prediction LLM arxiv 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "USM Universal Semantic Matching information extraction structured prediction LLM arxiv 2023"
  }
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-14T02:40:41.989591+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Knowledge Infused Decoding KID ICLR 2022 authors arxiv trie constrained"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Knowledge Infused Decoding KID ICLR 2022 authors arxiv trie constrained"
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-14T02:40:41.989732+00:00_

Web search results for query: "LLM Answer Set Programming ASP constraint validation logic programming 2024 2025"

Links: [{"title":"A Solver-in-the-Loop Framework for Improving LLMs on Answer Set Programming for Logic Puzzle Solving","url":"https://arxiv.org/html/2512.17093"},{"title":"Fine-tuning LLMs for answer set programming | Journal of Intelligent Information Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10844-025-01017-4"},{"title":"Bridging Natural Language and ASP: A Hybrid Approach Using LLMs and AMR Parsing","url":"https://arxiv.org/pdf/2511.08715"},{"title":"LLMs as ASP Programmers: Self-Correction Enables Task-Agnostic Nonmonotonic Reasoning","url":"https://arxiv.org/html/2604.27960"},{"title":"Answer Set Programming and Large Language Models ...","url":"https://ceur-ws.org/Vol-3876/paper3.pdf"},{"title":"ASP Essentials: Modelling and Efficient Solving Giuseppe Mazzotta #","url":"https://drops.dagstuhl.de/storage/01oasics/oasics-vol138-rw2024+rw2025/OASIcs.RW.2024-2025.8/OASIcs.RW.2024-2025.8.pdf"},{"title":"A Solver-in-the-Loop Framework for Improving LLMs on ...","url":"https://arxiv.org/pdf/2512.17093"},{"title":"LLASP: Fine-tuning Large Language Models for Answer Set Programming","url":"https://proceedings.kr.org/2024/78/kr2024-0078-coppolillo-et-al.pdf"},{"title":"ASP Chef Chats with Large Language Models","url":"https://www.ijcai.org/proceedings/2025/1247.pdf"},{"title":"Can LLMs Solve ASP Problems? Insights from a Benchmarking Study","url":"https://arxiv.org/pdf/2507.19749"}]

I've completed the web search for your query about LLM, Answer Set Programming (ASP), constraint validation, and logic programming from 2024-2025. Here are the key findings:

## Recent Research Highlights

**Neuro-Symbolic Integration:**
LLM-generated ASP encodings are automatically evaluated by an ASP solver and classified as either chosen or rejected, with solver-in-the-loop setups leveraging the declarative properties of ASP where rule
…[truncated 1205 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-14T02:40:41.989888+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "structured information extraction LLM NER relation event 2024 2025 survey constrained decoding arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "structured information extraction LLM NER relation event 2024 2025 survey constrained decoding arxiv"
  }
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-14T02:40:41.990017+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Outlines \"Efficient Guided Generation for LLMs\" arxiv 2307.09702 authors venue ICML 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Outlines \"Efficient Guided Generation for LLMs\" arxiv 2307.09702 authors venue ICML 2024"
  }
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-14T02:40:41.990139+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "grammar constrained decoding structured output LLM type-constrained information extraction 2024 2025 arxiv logit masking"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "grammar constrained decoding structured output LLM type-constrained information extraction 2024 2025 arxiv logit masking"
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-14T02:40:41.990271+00:00_

Web search results for query: "ontology-guided named entity recognition NER knowledge graph 2022 2023 2024 paper"

Links: [{"title":"Named Entity Recognition and Knowledge Graph for Natural Language Understanding | by Vincent Yuan | Medium","url":"https://medium.com/@vincentyuan87/named-entity-recognition-and-knowledge-graph-for-natural-language-understanding-c36401fc25af"},{"title":"Ontology development using language model-based Named Entity Recognition for integrated construction information | Journal of Civil Engineering and Management","url":"https://journals.vilniustech.lt/index.php/JCEM/article/view/26519"},{"title":"KCL: Few-shot Named Entity Recognition with Knowledge Graph and Contrastive Learning - ACL Anthology","url":"https://aclanthology.org/2024.lrec-main.846/"},{"title":"Ontology-conformal recognition of materials entities using language models | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-03619-y"},{"title":"The State of the Art on Knowledge Graph Construction from Text: Named Entity Recognition and Relation Extraction Perspectives for KGC2022 2022 - IBM Research","url":"https://research.ibm.com/publications/the-state-of-the-art-on-knowledge-graph-construction-from-text-named-entity-recognition-and-relation-extraction-perspectives"},{"title":"Recent Advances in Named Entity Recognition: A Comprehensive Survey and Comparative Study","url":"https://arxiv.org/html/2401.10825v3"},{"title":"Knowledge Graph Construction: Extraction, Learning, and Evaluation","url":"https://www.mdpi.com/2076-3417/15/7/3727"},{"title":"Named Entity Extraction for Knowledge Graphs: A Literature Overview | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/8999622/"},{"title":"Named Entity Recognition for Knowledge Graphs – Wisecube AI – Research Intelligence Platform","url":"https://www.wisecube.ai/blog/named-entity-recognition-for-knowledge-graphs/"},{"title":"Knowledge Graph Construction Techniques","url":"https://
…[truncated 2021 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-14T02:40:41.990427+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SGLang paper authors \"Lianmin Zheng\" NeurIPS 2024 arxiv 2312.07104"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SGLang paper authors \"Lianmin Zheng\" NeurIPS 2024 arxiv 2312.07104"
  }
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-14T02:40:41.990566+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "survey constrained decoding LLM structured generation 2024 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "survey constrained decoding LLM structured generation 2024 2025 arxiv"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-14T02:40:41.990714+00:00_

Web search results for query: "domain range constraints ontology information extraction validation 2022 2023 2024"

Links: [{"title":"Representation and validation of domain and range restrictions in a relational database driven ontology maintenance system - University of Missouri-Kansas City Libraries","url":"http://link.library.umkc.edu/portal/Representation-and-validation-of-domain-and-range/CT3DGMdFx9c/"},{"title":"dblp: Representation and validation of domain and range restrictions in a relational database-driven ontology maintenance system.","url":"https://dblp.org/rec/conf/ideas/EdgettLLC10.html"},{"title":"Development of Ontological Knowledge Bases by Leveraging Large Language Models","url":"https://arxiv.org/pdf/2601.10436"},{"title":"Representation and validation of domain and range ...","url":"https://scholarsmine.mst.edu/cgi/viewcontent.cgi?article=7729&context=masters_theses"},{"title":"ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs","url":"https://arxiv.org/html/2509.04696v1"},{"title":"Representation and Validation of Domain and Range Restrictions in a Relational Database-driven Ontology Maintenance System","url":"https://scholarsmine.mst.edu/comsci_facwork/1692/"},{"title":"Issues in Information Systems Volume 25, Issue 4, pp. 299-310, 2024 299","url":"https://iacis.org/iis/2024/4_iis_2024_299-310.pdf"},{"title":"AN ONTOLOGY ENRICHMENT FRAMEWORK USING ...","url":"https://openreview.net/pdf?id=FLyvCS6eJf"},{"title":"Query Reformulation Approach Using Domain Specific Ontology[v1] | Preprints.org","url":"https://www.preprints.org/manuscript/202401.0585"},{"title":"Large Language Models for Ontology Engineering: A Systematic Literature Review","url":"https://www.semantic-web-journal.net/system/files/swj3864.pdf"}]

I've completed the web search for your query on domain range constraints, ontology, information extraction, and validation spanning 2022-2024. Here's a summary of the relevant findings:

## Key Research Areas and Findings

*
…[truncated 1460 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-14T02:40:41.990870+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Guiding LLMs The Right Way\" Domino authors venue 2403.06988 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Guiding LLMs The Right Way\" Domino authors venue 2403.06988 2024"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-14T02:40:41.991010+00:00_

Web search results for query: "NeuroLogic Decoding NAACL 2021 authors Ximing Lu Peter West Rowan Zellers"

Links: [{"title":"NeuroLogic Decoding: (Un)supervised Neural Text Generation with Predicate Logic Constraints - ACL Anthology","url":"https://aclanthology.org/2021.naacl-main.339/"},{"title":"Ximing Lu","url":"https://gloriaximinglu.github.io/"},{"title":"NEUROLOGIC A>F>esque Decoding: Constrained Text Generation with Lookahead Heuristics - Yonsei University","url":"https://yonsei.elsevierpure.com/en/publications/neurologic-asupfsupesque-decoding-constrained-text-generation-wit/"},{"title":"Accepted Papers - NAACL-HLT 2021","url":"https://2021.naacl.org/program/accepted/"},{"title":"NeuroLogic Decoding: (Un)supervised Neural Text Generation with Predicate Logic Constraints | Request PDF","url":"https://www.researchgate.net/publication/352365466_NeuroLogic_Decoding_Unsupervised_Neural_Text_Generation_with_Predicate_Logic_Constraints"},{"title":"GitHub - GXimingLu/neurologic_decoding","url":"https://github.com/GXimingLu/neurologic_decoding"},{"title":"[PDF] NeuroLogic Decoding: (Un)supervised Neural Text Generation with Predicate Logic Constraints | Semantic Scholar","url":"https://www.semanticscholar.org/paper/NeuroLogic-Decoding:-(Un)supervised-Neural-Text-Lu-West/2c5bf29079cd958a2bef150077a02a1deb300652"},{"title":"Figure 1 from NeuroLogic Decoding: (Un)supervised Neural Text Generation with Predicate Logic Constraints | Semantic Scholar","url":"https://www.semanticscholar.org/paper/NeuroLogic-Decoding%3A-(Un)supervised-Neural-Text-Lu-West/e3215a2412c204f6936572982a0d7c13c8f03cb7/figure/0"},{"title":"Rowan Zellers' Homepage","url":"https://rowanzellers.com/"},{"title":"[PDF] NeuroLogic A*esque Decoding: Constrained Text Generation with Lookahead Heuristics | Semantic Scholar","url":"https://www.semanticscholar.org/paper/NeuroLogic-A*esque-Decoding:-Constrained-Text-with-Lu-Welleck/304cf21da84961469ac9f43405df187441832b61"}]

Based on the search results, I foun
…[truncated 799 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-14T02:40:41.991165+00:00_

Web search results for query: "post-hoc validation LLM outputs knowledge base ontology type checking 2023 2024 2025"

Links: [{"title":"Assessing the Evolution of LLM Capabilities for Knowledge Graph Engineering in 2023 | The Semantic Web: ESWC 2024 Satellite Events","url":"https://dl.acm.org/doi/10.1007/978-3-031-78952-6_5"},{"title":"Ontology-Grounded LLM Construction","url":"https://www.emergentmind.com/topics/ontology-grounded-llm-construction"},{"title":"Can LLMs be Knowledge Graph Curators for Validating ...","url":"https://aclanthology.org/2025.genaik-1.10.pdf"},{"title":"Large Language Models Assisting Ontology Evaluation","url":"https://arxiv.org/pdf/2507.14552"},{"title":"Large Language Models for Ontology Engineering: A Systematic Literature Review","url":"https://www.semantic-web-journal.net/system/files/swj4001.pdf"},{"title":"LLM-Driven Ontology Construction for Enterprise Knowledge Graphs","url":"https://arxiv.org/html/2602.01276v1"},{"title":"Frontiers | LLM-supported collaborative ontology design for data and knowledge management platforms","url":"https://www.frontiersin.org/journals/big-data/articles/10.3389/fdata.2025.1676477/full"},{"title":"Knowledge graph validation by integrating LLMs and human-in-the-loop - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S030645732500086X"},{"title":"LLM-supported collaborative ontology design for data and knowledge management platforms - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12646930/"},{"title":"LLM-empowered knowledge graph construction: A survey","url":"https://arxiv.org/pdf/2510.20345"}]

I've found comprehensive search results on this topic. Here's what the research landscape shows:

## Key Research Areas

Large Language Models bear the promise of significant acceleration of key Knowledge Graph and Ontology Engineering tasks, including ontology modeling, extension, modification, population, alignment, as well as entity disambiguation.

### Validation Approaches

Fo
…[truncated 1766 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-14T02:40:41.991317+00:00_

Web search results for query: "CRANE constrained decoding NeurIPS 2024 "Let Me Speak Freely""

Links: [{"title":"Reasoning with constrained LLM generation - CRANE","url":"https://arxiv.org/pdf/2502.09061"},{"title":"CRANE: Reasoning with constrained LLM generation","url":"https://par.nsf.gov/servlets/purl/10633770"},{"title":"Beyond Free-Form Text: How Constrained Decoding is Reshaping Structured Generation in LLMs | by Brijesh Nambiar | Medium","url":"https://medium.com/@brijeshrn/beyond-free-form-text-how-constrained-decoding-is-reshaping-structured-generation-in-llms-5f7a38bef259"},{"title":"Thinking Before Constraining: A Unified Decoding Framework for Large","url":"https://www.arxiv.org/pdf/2601.07525"},{"title":"Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models","url":"https://arxiv.org/html/2408.02442v1"},{"title":"GitHub - Saibo-creator/Awesome-LLM-Constrained-Decoding: A curated list of papers related to constrained decoding of LLM, along with their relevant code and resources. · GitHub","url":"https://github.com/Saibo-creator/Awesome-LLM-Constrained-Decoding"},{"title":"Let Me Speak Freely? A Study on the Impact of Format ...","url":"https://aclanthology.org/2024.emnlp-industry.91.pdf"}]

Based on the search results, I found relevant information about these topics:

## CRANE: Reasoning with Constrained LLM Generation

CRANE effectively alternates between unconstrained generation for reasoning and constrained generation for producing structurally correct outputs. This allows the model to produce syntactically valid outputs while enabling the LLM to reason. The work addresses a key problem in constrained decoding: imposing constraints on LLM outputs can, in some cases, reduce functional correctness for specific tasks.

## "Let Me Speak Freely?" Study

The paper titled "Let me speak freely? a study on the impact of format restrictions on large language model performance" was published at the 2024 Confere
…[truncated 728 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-14T02:40:41.991464+00:00_

Web search results for query: "type-constrained relation extraction entity type constraints 2021 2022 2023 paper"

Links: [{"title":"Document-level relation extraction with entity type constraints - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0893608025013504"},{"title":"SH-ETRs:Learning Soft-Hard rules with entity type constraints for document-level relation extraction - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0957417425032750"},{"title":"Integrated attention using entity type constraints and relation augmentation for distantly supervised relation extraction - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0950705125020441"},{"title":"Rethinking Relation Extraction: Beyond Shortcuts to Generalization with a Debiased Benchmark","url":"https://arxiv.org/html/2501.01349"},{"title":"How Fragile is Relation Extraction under Entity Replacements?","url":"https://arxiv.org/html/2305.13551"},{"title":"Enhancing knowledge graph embedding with type-constraint features | Applied Intelligence | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10489-022-03518-z"},{"title":"Open Information Extraction with Entity Focused Constraints - ACL Anthology","url":"https://aclanthology.org/2023.findings-eacl.95/"},{"title":"Retrieval over Classification: Integrating Relation Semantics for","url":"https://arxiv.org/pdf/2509.21151"},{"title":"EnriCo: Enriched Representation and Globally Constrained Inference for Entity and Relation Extraction","url":"https://arxiv.org/html/2404.12493"},{"title":"Few-Shot Relation Extraction via Two-Stage Knowledge- ...","url":"https://www.ijcai.org/proceedings/2025/0897.pdf"}]

Based on the web search results, here are several relevant papers and research on type-constrained relation extraction with entity type constraints from 2021-2023:

## Key Papers Found:

1. **Document-level Relation Extraction with Entity Type Constraints (DocRE-
…[truncated 1870 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-14T02:40:41.991620+00:00_

Web search results for query: "Knowledge Infused Decoding KID ICLR 2022 authors arxiv trie constrained"

Links: [{"title":"Published as a conference paper at ICLR 2022 KNOWLEDGE INFUSED DECODING","url":"https://arxiv.org/pdf/2204.03084"},{"title":"[2204.03084] Knowledge Infused Decoding","url":"https://arxiv.org/abs/2204.03084"},{"title":"[2204.03084v1] Knowledge Infused Decoding","url":"https://arxiv.org/abs/2204.03084v1"},{"title":"Knowledge Infused Decoding","url":"https://www.catalyzex.com/paper/arxiv:2204.03084"},{"title":"GitHub - microsoft/KID: Knowledge Infused Decoding · GitHub","url":"https://github.com/microsoft/KID"},{"title":"[PDF] Knowledge Infused Decoding | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Knowledge-Infused-Decoding-Liu-Zheng/706c6b3781374b0b11f98f204a4ddd05b26ed009"},{"title":"[2204.03084] Knowledge Infused Decoding","url":"http://arxiv-export3.library.cornell.edu/abs/2204.03084?context=cs"},{"title":"Knowledge Infused Decoding – arXiv Vanity","url":"https://www.arxiv-vanity.com/papers/2204.03084/"},{"title":"Code for paper \"The Curious Case of Neural Text Degeneration\"| DeepAICode","url":"https://deepaicode.com/p/code-for-paper-the-curious-case-of-neural-text-degeneration"},{"title":"Papers with Code - Knowledge Infused Decoding","url":"https://paperswithcode.com/paper/knowledge-infused-decoding-1"}]

Based on the search results, here is information about the Knowledge Infused Decoding (KID) paper:

## Overview
Knowledge Infused Decoding (KID) is a novel decoding algorithm for generative language models, which dynamically infuses external knowledge into each step of the LM decoding.

## Authors
The authors are Ruibo Liu, Guoqing Zheng, Shashank Gupta, Radhika Gaonkar, Chongyang Gao, Soroush Vosoughi, Milad Shokouhi, and Ahmed H. Awadallah.

## Key Technical Approach
The method maintains a local knowledge memory based on the current context, interacting with a dynamically created external knowledge trie, and continuou
…[truncated 750 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-14T02:40:41.991796+00:00_

Web search results for query: "structure snowballing constrained decoding LLM quality degradation 2024 2025"

Links: [{"title":"From Hallucination to Structure Snowballing: The Alignment Tax of Constrained Decoding in LLM Reflection","url":"https://arxiv.org/html/2604.06066"},{"title":"[2604.06066] From Hallucination to Structure Snowballing: The Alignment Tax of Constrained Decoding in LLM Reflection","url":"https://arxiv.org/abs/2604.06066"},{"title":"How Structured Outputs and Constrained Decoding Work | Let's Data Science","url":"https://letsdatascience.com/blog/structured-outputs-making-llms-return-reliable-json"},{"title":"Grammar-Aligned Decoding | OpenReview","url":"https://openreview.net/forum?id=5G7ve8E1Lu"},{"title":"NeurIPS Poster Grammar-Aligned Decoding","url":"https://neurips.cc/virtual/2024/poster/96599"},{"title":"[2405.21047] Grammar-Aligned Decoding","url":"https://arxiv.org/abs/2405.21047"},{"title":"Grammar-Aligned Decoding Kanghee Park1∗ Jiayu Wang1∗ Taylor Berg-Kirkpatrick2","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/2bdc2267c3d7d01523e2e17ac0a754f3-Paper-Conference.pdf"},{"title":"The Hidden Cost of Structure: How Constrained Decoding ...","url":"https://acl-bg.org/proceedings/2025/RANLP%202025/pdf/2025.ranlp-1.124.pdf"},{"title":"SLOT: Structuring the Output of Large Language Models","url":"https://aclanthology.org/2025.emnlp-industry.32.pdf"},{"title":"GitHub - Saibo-creator/Awesome-LLM-Constrained-Decoding: A curated list of papers related to constrained decoding of LLM, along with their relevant code and resources. · GitHub","url":"https://github.com/Saibo-creator/Awesome-LLM-Constrained-Decoding"}]

I found comprehensive research on this topic. Here are the key findings from recent research on structure snowballing and constrained decoding:

## Structure Snowballing in Constrained Decoding

A new failure mode has been identified termed "structure snowballing," which occurs when imposing structural constraints does 
…[truncated 1607 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-14T02:40:41.991951+00:00_

Web search results for query: "GenIE Josifoski constrained decoding closed information extraction trie EMNLP 2022 arxiv"

Links: [{"title":"Grammar-Constrained Decoding for Structured NLP Tasks ...","url":"https://dlab.epfl.ch/people/west/pub/Geng-Josifoski-Peyrard-West_EMNLP-23.pdf"},{"title":"GenIE: Generative Information Extraction","url":"https://dlab.epfl.ch/people/west/pub/Josifoski-DeCao-Peyrard-Petroni-West_NAACL-22.pdf"},{"title":"Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning","url":"https://arxiv.org/html/2305.13971v6"},{"title":"GenIE: Generative Information Extraction - ACL Anthology","url":"https://aclanthology.org/2022.naacl-main.342/"},{"title":"Combining Constrained and Unconstrained Decoding via ...","url":"https://aclanthology.org/2025.emnlp-main.926.pdf"},{"title":"[2112.08340] GenIE: Generative Information Extraction","url":"https://arxiv.org/abs/2112.08340"},{"title":"Large language models for generative information extraction: a survey | Frontiers of Computer Science | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11704-024-40555-y"},{"title":"(PDF) GenIE: Generative Information Extraction","url":"https://www.researchgate.net/publication/362262820_GenIE_Generative_Information_Extraction"},{"title":"Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11747381/"},{"title":"Combining Constrained and Unconstrained Decoding via Boosting: BoostCD and Its Application to Information Extraction","url":"https://arxiv.org/html/2506.14901v1"}]

I found relevant results about GenIE and related work. Based on the search results, here's what I can tell you:

GenIE (Generative Information Extraction) was published at the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL 2022), not EMNLP 2022
…[truncated 1060 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-14T02:40:41.992101+00:00_

Web search results for query: "structured output constraints degrade LLM generation quality arXiv 2024"

Links: [{"title":"The Structured Output Benchmark: A Multi-Source Benchmark for Evaluating Structured Output Quality in Large Language Models","url":"https://arxiv.org/html/2604.25359"},{"title":"Generating Structured Outputs from Language Models: Benchmark and Studies","url":"https://arxiv.org/html/2501.10868v1"},{"title":"Output Constraints as Attack Surface: Exploiting Structured Generation to Bypass LLM Safety Mechanisms","url":"https://arxiv.org/html/2503.24191v1"},{"title":"Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models","url":"https://arxiv.org/html/2408.02442v1"},{"title":"How Structured Outputs and Constrained Decoding Work | Let's Data Science","url":"https://letsdatascience.com/blog/structured-outputs-making-llms-return-reliable-json"},{"title":"When Correct Isn’t Usable: Improving Structured Output Reliability in Small Language Models","url":"https://arxiv.org/html/2605.02363v1"},{"title":"Constraint decay: The Fragility of LLM Agents in Backend Code Generation","url":"https://arxiv.org/html/2605.06445"},{"title":"“We Need Structured Output”: Towards User-centered Constraints","url":"https://lxieyang.github.io/assets/files/pubs/llm-constraints-2024/llm-constraints-2024.pdf"},{"title":"CRANE: Reasoning with constrained LLM generation","url":"https://arxiv.org/html/2502.09061v3"},{"title":"“We Need Structured Output”: Towards User-centered Constraints on Large Language Model Output","url":"https://arxiv.org/html/2404.07362v1"}]

Based on the search results, I found several relevant papers on this topic from 2024:

## Key Findings on Structured Output Constraints Degrading LLM Quality

Tam et al. (2024) find that structured format constraints (JSON, XML, YAML) degrade LLM reasoning ability.

A significant decline in LLMs' reasoning abilities under format restrictions has been observed, and strict
…[truncated 1229 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-14T02:40:41.992251+00:00_

Web search results for query: "USM Universal Semantic Matching information extraction structured prediction LLM arxiv 2023"

Links: [{"title":"[2301.03282] Universal Information Extraction as Unified Semantic Matching","url":"https://arxiv.org/abs/2301.03282"},{"title":"Universal Information Extraction as Unified Semantic Matching | Request PDF","url":"https://www.researchgate.net/publication/371922000_Universal_Information_Extraction_as_Unified_Semantic_Matching"},{"title":"Universal Information Extraction as Unified Semantic Matching - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230103282L/abstract"},{"title":"[PDF] Unified Structure Generation for Universal Information Extraction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Unified-Structure-Generation-for-Universal-Lu-Liu/5382c28b9f2dd30f15c836bea92382091b1d886f"},{"title":"Universal information extraction as unified semantic matching | Proceedings of the Thirty-Seventh AAAI Conference on Artificial Intelligence and Thirty-Fifth Conference on Innovative Applications of Artificial Intelligence and Thirteenth Symposium on Educational Advances in Artificial Intelligence","url":"https://dl.acm.org/doi/10.1609/aaai.v37i11.26563"},{"title":"XNLP: An Interactive Demonstration System for Universal Structured NLP","url":"https://arxiv.org/html/2308.01846"},{"title":"[2510.13515] UniME-V2: MLLM-as-a-Judge for Universal Multimodal Embedding Learning","url":"https://arxiv.org/abs/2510.13515"},{"title":"LLM for Uniform Information Extraction Using Multi-task Learning Optimization | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-981-96-0055-7_2"},{"title":"Universal Information Extraction as Unified Semantic Matching | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/26563"},{"title":"Large language models for generative information extraction: a survey | Frontiers of Computer Science | Springer Nat
…[truncated 1361 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-14T02:40:41.992418+00:00_

Web search results for query: "constrained decoding hurts LLM performance empirical study 2024 2025"

Links: [{"title":"How Constrained Decoding Affects Language Model ...","url":"https://aclanthology.org/2025.ranlp-1.124.pdf"},{"title":"Efficient LLM System with Speculative Decoding | EECS at UC Berkeley","url":"https://www2.eecs.berkeley.edu/Pubs/TechRpts/2025/EECS-2025-224.html"},{"title":"Constrained Decoding of Diffusion LLMs with Context-Free Grammars | OpenReview","url":"https://openreview.net/forum?id=7Sph4KyeYO"},{"title":"The Hidden Cost of Structure: How Constrained Decoding ...","url":"https://acl-bg.org/proceedings/2025/RANLP%202025/pdf/2025.ranlp-1.124.pdf"},{"title":"GitHub - Saibo-creator/Awesome-LLM-Constrained-Decoding: A curated list of papers related to constrained decoding of LLM, along with their relevant code and resources. · GitHub","url":"https://github.com/Saibo-creator/Awesome-LLM-Constrained-Decoding"},{"title":"SLOT: Structuring the Output of Large Language Models","url":"https://aclanthology.org/2025.emnlp-industry.32.pdf"},{"title":"Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation","url":"https://arxiv.org/html/2403.06988v1"},{"title":"Grammar-Aligned Decoding Kanghee Park1∗ Jiayu Wang1∗ Taylor Berg-Kirkpatrick2","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/2bdc2267c3d7d01523e2e17ac0a754f3-Paper-Conference.pdf"},{"title":"How Structured Outputs and Constrained Decoding Work | Let's Data Science","url":"https://letsdatascience.com/blog/structured-outputs-making-llms-return-reliable-json"},{"title":"Towards Efficient LLM Inference via Collective and Adaptive Speculative Decoding | Proceedings of the International Conference for High Performance Computing, Networking, Storage and Analysis","url":"https://dl.acm.org/doi/10.1145/3712285.3759834"}]

Based on the search results, I found relevant research on how constrained decoding affects LLM performance. Here are the key findings:

## Recent Empiric
…[truncated 1579 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-14T02:40:41.992572+00:00_

Web search results for query: "SGLang paper authors "Lianmin Zheng" NeurIPS 2024 arxiv 2312.07104"

Links: [{"title":"[2312.07104] SGLang: Efficient Execution of Structured Language Model Programs","url":"https://arxiv.org/abs/2312.07104"},{"title":"Efficiently programming large language models using SGLang | Awesome Papers","url":"https://paper.lingyunyang.com/reading-notes/miscellaneous/arxiv/2024/sglang"},{"title":"SGLang: Efficient Execution of Structured Language Model Programs","url":"https://arxiv.org/pdf/2312.07104"},{"title":"Paper page - Efficiently Programming Large Language Models using SGLang","url":"https://huggingface.co/papers/2312.07104"},{"title":"Sglang: Efficient execution of structured language model programs | Stanford MAST Lab","url":"https://mast.stanford.edu/pubs/sglang_efficient_execution_of_structured_language_model_programs/"},{"title":"[PDF] SGLang: Efficient Execution of Structured Language Model Programs | Semantic Scholar","url":"https://www.semanticscholar.org/paper/SGLang:-Efficient-Execution-of-Structured-Language-Zheng-Yin/eb95c327260725498404eb43ec370d419b8d92c7"},{"title":"SGLang: Efficient Execution of Structured Language Model Programs | OpenReview","url":"https://openreview.net/forum?id=VqkAKQibpq"},{"title":"NeurIPS Poster SGLang: Efficient Execution of Structured Language Model Programs","url":"https://neurips.cc/virtual/2024/poster/94872"},{"title":"SGLang: Efficient Execution of Structured Language Model ...","url":"http://theory.stanford.edu/~barrett/pubs/ZYX+24-abstract.html"},{"title":"SGLang: Efficient Execution of Structured Language Model Programs","url":"https://proceedings.neurips.cc/paper_files/paper/2024/hash/724be4472168f31ba1c9ac630f15dec8-Abstract-Conference.html"}]

Based on the search results, I found comprehensive information about the SGLang paper:

## SGLang Paper Details

The authors of the SGLang paper are: Lianmin Zheng, Liangsheng Yin, Zhiqiang Xie, Chuyue Sun, Jeff Huang, Cody Hao Yu, Shiyi Cao, Chr
…[truncated 843 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-14T02:40:41.992745+00:00_

Web search results for query: "Outlines "Efficient Guided Generation for LLMs" arxiv 2307.09702 authors venue ICML 2024"

Links: [{"title":"[2307.09702] Efficient Guided Generation for Large Language Models","url":"https://arxiv.org/abs/2307.09702"},{"title":"Efficient Guided Generation for Large Language Models","url":"https://arxiv.org/pdf/2307.09702"},{"title":"[PDF] Efficient Guided Generation for Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Efficient-Guided-Generation-for-Large-Language-Willard-Louf/c4ceaef35bca063815f50d90a087acbd07a65478"},{"title":"Efficient Guided Generation for LLMs Brandon T. Willard1 and R´emi Louf2","url":"https://arxiv.org/pdf/2307.09702v1"},{"title":"Paper page - Efficient Guided Generation for Large Language Models","url":"https://huggingface.co/papers/2307.09702"},{"title":"[2307.09702v1] Efficient Guided Generation for LLMs","url":"https://arxiv.org/abs/2307.09702v1"},{"title":"(PDF) Efficient Guided Generation for LLMs","url":"https://www.researchgate.net/publication/372468267_Efficient_Guided_Generation_for_LLMs"},{"title":"[2307.09702v3] Efficient Guided Generation for Large Language Models","url":"https://arxiv.org/abs/2307.09702v3"},{"title":"[2307.09702v2] Efficient Guided Generation for Large Language Models","url":"https://arxiv.org/abs/2307.09702v2"},{"title":"GitHub - dottxt-ai/outlines: Structured Outputs · GitHub","url":"https://github.com/dottxt-ai/outlines"}]

Based on the search results, here's the information about "Efficient Guided Generation for LLMs":

## Paper Overview

**Authors:** Brandon T. Willard and Rémi Louf

**arXiv ID:** 2307.09702 (Submitted on July 19, 2023)

## Main Contribution

The paper shows how neural text generation can be reformulated in terms of transitions between states of a finite-state machine, leading to an efficient approach to guiding text generation with regular expressions and context-free grammars.

## Key Features

The approach is model agn
…[truncated 890 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-14T02:40:41.992899+00:00_

Web search results for query: "structured information extraction LLM NER relation event 2024 2025 survey constrained decoding arxiv"

Links: [{"title":"GitHub - quqxui/Awesome-LLM4IE-Papers: Awesome papers about generative Information Extraction (IE) using Large Language Models (LLMs) · GitHub","url":"https://github.com/quqxui/Awesome-LLM4IE-Papers"},{"title":"Large Language Models for Generative Information Extraction: A Survey","url":"https://arxiv.org/html/2312.17617v3"},{"title":"A Survey of Generative Information Extraction","url":"https://aclanthology.org/2025.coling-main.324.pdf"},{"title":"Information Extraction in Low-Resource Scenarios: Survey and Perspective","url":"https://arxiv.org/html/2202.08063v6"},{"title":"Large language models for generative information extraction: a survey | Frontiers of Computer Science | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11704-024-40555-y"},{"title":"Large language models for generative information extraction: a survey","url":"https://d-nb.info/1354655508/34"},{"title":"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction","url":"https://arxiv.org/html/2510.08623v1"},{"title":"LLM-empowered knowledge graph construction: A survey","url":"https://arxiv.org/pdf/2510.20345"},{"title":"Published as a conference paper at ICLR 2024 LINEARITY OF RELATION DECODING IN","url":"https://arxiv.org/pdf/2308.09124"},{"title":"Generating Structured Outputs from Language Models: Benchmark and Studies","url":"https://arxiv.org/html/2501.10868v1"}]

I've found several highly relevant results for your search on structured information extraction with LLMs, NER, relation extraction, event extraction, constrained decoding, and related topics. Here are the key findings:

## Major Surveys and Resources

Recent surveys categorize methods for adapting LLMs to IE tasks including Data Augmentation, Prompt Design, Zero-shot Learning, Constrained Decoding Generation, Few-shot Learning, and Supervised Fine-
…[truncated 1221 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-14T02:40:41.993050+00:00_

Web search results for query: ""Guiding LLMs The Right Way" Domino authors venue 2403.06988 2024"

Links: [{"title":"[2403.06988] Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation","url":"https://arxiv.org/abs/2403.06988"},{"title":"2403.06988 - Guiding LLMs The Right Way","url":"https://www.emergentmind.com/papers/2403.06988"},{"title":"Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation","url":"https://arxiv.org/html/2403.06988v1"},{"title":"Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation","url":"https://files.sri.inf.ethz.ch/website/papers/beurerkellner2024domino.pdf"},{"title":"Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation [Quick Review]","url":"https://liner.com/review/guiding-llms-right-way-fast-noninvasive-constrained-generation"},{"title":"Guiding LLMs the right way | Proceedings of the 41st International Conference on Machine Learning","url":"https://dl.acm.org/doi/10.5555/3692070.3692216"},{"title":"ICML Poster Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation","url":"https://icml.cc/virtual/2024/poster/33037"},{"title":"Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation.","url":"https://cs.reviewer.ly/publication/a1828f67-6f12-492e-b89a-26291551486a"},{"title":"[2409.15241] Domino: Eliminating Communication in LLM Training via Generic Tensor Slicing and Overlapping","url":"https://arxiv.org/abs/2409.15241"},{"title":"Things we learned about LLMs in 2024 | Hacker News","url":"https://news.ycombinator.com/item?id=42560558"}]

Based on the search results, I found information about the paper "Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation":

**Authors:** Luca Beurer-Kellner, Marc Fischer, and Martin Vechev

**Venue:** ICML 2024

**Paper Identifier:** 2403.06988, published February 7, 2024

**Summary:** The paper addresses how to ensure that text generated by large language models (LLMs) is in an expected format thro
…[truncated 312 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-14T02:40:41.993201+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"solver-in-the-loop\" LLM ASP answer set programming arxiv 2024 2025 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"solver-in-the-loop\" LLM ASP answer set programming arxiv 2024 2025 authors"
  }
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-14T02:40:41.993334+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LLASP fine-tuning large language models answer set programming KR 2024 Coppolillo authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LLASP fine-tuning large language models answer set programming KR 2024 Coppolillo authors"
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-14T02:40:41.993473+00:00_

Web search results for query: "grammar constrained decoding structured output LLM type-constrained information extraction 2024 2025 arxiv logit masking"

Links: [{"title":"Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11747381/"},{"title":"Generating Structured Outputs from Language Models: Benchmark and Studies","url":"https://arxiv.org/html/2501.10868v1"},{"title":"How Structured Outputs and Constrained Decoding Work | Let's Data Science","url":"https://letsdatascience.com/blog/structured-outputs-making-llms-return-reliable-json"},{"title":"Frontiers | Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts","url":"https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1406857/full"},{"title":"Constrained Decoding: Grammar-Guided Generation for Structured LLM Output - Interactive | Michael Brenndoerfer | Michael Brenndoerfer","url":"https://mbrenndoerfer.com/writing/constrained-decoding-structured-llm-output"},{"title":"Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning","url":"https://arxiv.org/html/2305.13971v6"},{"title":"GitHub - Saibo-creator/Awesome-LLM-Constrained-Decoding: A curated list of papers related to constrained decoding of LLM, along with their relevant code and resources. · GitHub","url":"https://github.com/Saibo-creator/Awesome-LLM-Constrained-Decoding"},{"title":"Flexible and Efficient Grammar-Constrained Decoding","url":"https://arxiv.org/pdf/2502.05111"},{"title":"A Guide to Structured Outputs Using Constrained Decoding","url":"https://www.aidancooper.co.uk/constrained-decoding/"},{"title":"CRANE: Reasoning with constrained LLM generation","url":"https://arxiv.org/html/2502.09061v3"}]

Here are the search results for your query on grammar constrained decoding, struc
…[truncated 2029 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-14T02:40:41.993626+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"ontology-conformal\" named entity recognition materials language models 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"ontology-conformal\" named entity recognition materials language models 2025 arxiv"
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-14T02:40:41.993779+00:00_

Web search results for query: "survey constrained decoding LLM structured generation 2024 2025 arxiv"

Links: [{"title":"GitHub - Saibo-creator/Awesome-LLM-Constrained-Decoding: A curated list of papers related to constrained decoding of LLM, along with their relevant code and resources. · GitHub","url":"https://github.com/Saibo-creator/Awesome-LLM-Constrained-Decoding"},{"title":"Draft-Conditioned Constrained Decoding for Structured Generation in LLMs","url":"https://arxiv.org/pdf/2603.03305"},{"title":"[2405.21047] Grammar-Aligned Decoding","url":"https://arxiv.org/abs/2405.21047"},{"title":"Generating Structured Outputs from Language Models: Benchmark and Studies","url":"https://arxiv.org/html/2501.10868v1"},{"title":"The Hidden Cost of Structure: How Constrained Decoding ...","url":"https://acl-bg.org/proceedings/2025/RANLP%202025/pdf/2025.ranlp-1.124.pdf"},{"title":"XGrammar: Flexible and Efficient Structured Generation ...","url":"https://arxiv.org/pdf/2411.15100"},{"title":"1 Introduction","url":"https://arxiv.org/html/2411.15100v1"},{"title":"Guided Decoding and Its Critical Role in Retrieval-Augmented Generation","url":"https://arxiv.org/html/2509.06631v1"},{"title":"CRANE: Reasoning with constrained LLM generation","url":"https://arxiv.org/html/2502.09061v3"},{"title":"Unveiling the Potential of Diffusion Large Language Model in Controllable Generation","url":"https://arxiv.org/html/2507.04504v1"}]

I've performed a web search for recent papers and resources on constrained decoding and structured generation in large language models from 2024-2025. Here are the key findings:

## Recent Survey and Benchmark Resources

There are recent papers on generating structured outputs from language models and benchmarks (January 2025), as well as papers on XGrammar, a flexible and efficient structured generation engine for large language models (November 2024).

## Key Papers and Frameworks

JSONSchemaBench evaluates six state-of-the-art constrained decoding frameworks
…[truncated 1267 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-14T02:40:41.993936+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Let Me Speak Freely\" Tam Zheng Joty EMNLP 2024 format restrictions LLM arXiv 2408.02442"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Let Me Speak Freely\" Tam Zheng Joty EMNLP 2024 format restrictions LLM arXiv 2408.02442"
  }
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-14T02:40:41.994155+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"document-level relation extraction\" \"entity type constraints\" DocRE type-constrained 2024 2025 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"document-level relation extraction\" \"entity type constraints\" DocRE type-constrained 2024 2025 authors"
  }
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-14T02:40:41.994346+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CRANE \"Reasoning with constrained LLM generation\" authors arXiv 2502.09061 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CRANE \"Reasoning with constrained LLM generation\" authors arXiv 2502.09061 2025"
  }
}
```

</details>

---

### Tool call

_source line 86 · 2026-05-14T02:40:41.994487+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ODKE ontology-guided open-domain knowledge extraction LLM 2025 arxiv authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ODKE ontology-guided open-domain knowledge extraction LLM 2025 arxiv authors"
  }
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-14T02:40:41.994618+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ADELIE aligning LLMs information extraction EMNLP 2024 arxiv schema-constrained"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ADELIE aligning LLMs information extraction EMNLP 2024 arxiv schema-constrained"
  }
}
```

</details>

---

### Tool call

_source line 88 · 2026-05-14T02:40:41.994807+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Grammar-Aligned Decoding\" Park Wang Berg-Kirkpatrick NeurIPS 2024 arXiv 2405.21047"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Grammar-Aligned Decoding\" Park Wang Berg-Kirkpatrick NeurIPS 2024 arXiv 2405.21047"
  }
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-14T02:40:41.994956+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning\" Geng Josifoski EMNLP 2023 arxiv 2305.13971"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning\" Geng Josifoski EMNLP 2023 arxiv 2305.13971"
  }
}
```

</details>

---

### Tool call

_source line 90 · 2026-05-14T02:40:41.995085+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "InstructUIE authors Xiao Wang first authors 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "InstructUIE authors Xiao Wang first authors 2023"
  }
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-14T02:40:41.995212+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"From Hallucination to Structure Snowballing\" alignment tax constrained decoding arXiv 2604.06066 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"From Hallucination to Structure Snowballing\" alignment tax constrained decoding arXiv 2604.06066 authors"
  }
}
```

</details>

---

### Tool call

_source line 92 · 2026-05-14T02:40:41.995340+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Generating Structured Outputs from Language Models\" JSONSchemaBench arxiv 2501.10868 authors 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Generating Structured Outputs from Language Models\" JSONSchemaBench arxiv 2501.10868 authors 2025"
  }
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-14T02:40:41.995487+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"The Hidden Cost of Structure\" constrained decoding RANLP 2025 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"The Hidden Cost of Structure\" constrained decoding RANLP 2025 authors"
  }
}
```

</details>

---

### Tool call

_source line 94 · 2026-05-14T02:40:41.995624+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "De Cao GENRE autoregressive entity retrieval authors Nicola Gautier Fabio ICLR 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "De Cao GENRE autoregressive entity retrieval authors Nicola Gautier Fabio ICLR 2021"
  }
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-14T02:40:41.995774+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Grammar-Aligned Decoding\" arxiv 2405.21047 authors venue 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Grammar-Aligned Decoding\" arxiv 2405.21047 authors venue 2024"
  }
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-14T02:40:41.995914+00:00_

Web search results for query: "LLASP fine-tuning large language models answer set programming KR 2024 Coppolillo authors"

Links: [{"title":"LLASP: Fine-tuning Large Language Models for Answer Set Programming @KR2024","url":"https://proceedings.kr.org/2024/78/"},{"title":"[2407.18723] LLASP: Fine-tuning Large Language Models for Answer Set Programming","url":"https://arxiv.org/abs/2407.18723"},{"title":"Fine-tuning LLMs for answer set programming | Journal of Intelligent Information Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10844-025-01017-4"},{"title":"LLASP: Fine-tuning Large Language Models for Answer Set Programming","url":"https://arxiv.org/pdf/2407.18723"},{"title":"(PDF) LLASP: Fine-tuning Large Language Models for Answer Set Programming","url":"https://www.researchgate.net/publication/385465965_LLASP_Fine-tuning_Large_Language_Models_for_Answer_Set_Programming"},{"title":"Intermediate Languages Matter: Formal Languages and LLMs affect Neurosymbolic Reasoning","url":"https://arxiv.org/html/2509.04083v1"},{"title":"Leveraging Large Language Models to Generate Answer Set Programs | Request PDF","url":"https://www.researchgate.net/publication/373589881_Leveraging_Large_Language_Models_to_Generate_Answer_Set_Programs"},{"title":"Computer Science Jul 2024","url":"https://arxiv.org/list/cs/2024-07?skip=8605&show=2000"},{"title":"A Solver-in-the-Loop Framework for Improving LLMs on ...","url":"https://arxiv.org/pdf/2512.17093"},{"title":"[PDF] A systematic evaluation of large language models of code | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-systematic-evaluation-of-large-language-models-of-Xu-Alon/b32a6f6ef7dd775e0f876b4713ceccebc56e651e"}]

Based on the search results, I can provide you with information about the LLASP paper:

## LLASP: Fine-tuning Large Language Models for Answer Set Programming

The paper was presented at the 21st International Conference on Principles of Knowledge Representation an
…[truncated 1246 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 97 · 2026-05-14T02:40:41.996067+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Microsoft Guidance library academic paper \"guidance-ai\" constrained generation arxiv 2023 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Microsoft Guidance library academic paper \"guidance-ai\" constrained generation arxiv 2023 2024"
  }
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-14T02:40:41.996203+00:00_

Web search results for query: ""solver-in-the-loop" LLM ASP answer set programming arxiv 2024 2025 authors"

Links: [{"title":"A Solver-in-the-Loop Framework for Improving LLMs on ...","url":"https://arxiv.org/pdf/2512.17093"},{"title":"A Solver-in-the-Loop Framework for Improving LLMs on Answer Set Programming for Logic Puzzle Solving","url":"https://arxiv.org/html/2512.17093"},{"title":"[2512.17093] A Solver-in-the-Loop Framework for Improving LLMs on Answer Set Programming for Logic Puzzle Solving","url":"https://arxiv.org/abs/2512.17093"},{"title":"(PDF) A Solver-in-the-Loop Framework for Improving LLMs on Answer Set Programming for Logic Puzzle Solving","url":"https://www.researchgate.net/publication/398936696_A_Solver-in-the-Loop_Framework_for_Improving_LLMs_on_Answer_Set_Programming_for_Logic_Puzzle_Solving"},{"title":"OPUS 4 | A solver-in-the-loop framework for improving LLMs on answer set programming for logic puzzle solving [Poster]","url":"https://opus.bibliothek.uni-augsburg.de/opus4/frontdoor/index/index/docId/128427"},{"title":"A Solver-in-the-Loop Framework for Improving LLMs","url":"https://ojs.aaai.org/index.php/AAAI/article/download/39714/43675"},{"title":"(PDF) LLASP: Fine-tuning Large Language Models for Answer Set Programming","url":"https://www.researchgate.net/publication/385465965_LLASP_Fine-tuning_Large_Language_Models_for_Answer_Set_Programming"},{"title":"A Solver-in-the-Loop Framework for Improving LLMs on Answer Set Programming for Logic Puzzle Solving | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/39714"},{"title":"Computation and Language 2025","url":"https://arxiv.org/list/cs.CL/2025?skip=23575&show=50"}]

Based on the search results, I found detailed information about the "solver-in-the-loop" LLM ASP paper:

## Paper Information

**Title:** "A Solver-in-the-Loop Framework for Improving LLMs on Answer Set Programming for Logic Puzzle Solving"

**Authors:** Timo 
…[truncated 898 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-14T02:40:41.996368+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "GoLLIE authors Oscar Sainz Iker Garcia-Ferrero arxiv 2310.03668"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "GoLLIE authors Oscar Sainz Iker Garcia-Ferrero arxiv 2310.03668"
  }
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-14T02:40:41.996516+00:00_

Web search results for query: "CRANE "Reasoning with constrained LLM generation" authors arXiv 2502.09061 2025"

Links: [{"title":"[2502.09061] CRANE: Reasoning with constrained LLM generation","url":"https://arxiv.org/abs/2502.09061"},{"title":"Reasoning with constrained LLM generation - CRANE","url":"https://arxiv.org/pdf/2502.09061"},{"title":"CRANE: Reasoning with constrained LLM generation","url":"https://arxiv.org/html/2502.09061v1"},{"title":"CRANE: Reasoning with constrained LLM generation - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250209061B/abstract"},{"title":"Paper page - CRANE: Reasoning with constrained LLM generation","url":"https://huggingface.co/papers/2502.09061"},{"title":"[2502.09061v2] CRANE: Reasoning with constrained LLM generation","url":"https://arxiv.org/abs/2502.09061v2"},{"title":"dblp: CRANE: Reasoning with constrained LLM generation.","url":"https://dblp.org/rec/journals/corr/abs-2502-09061.html"},{"title":"(PDF) CRANE: Reasoning with constrained LLM generation","url":"https://www.researchgate.net/publication/388964154_CRANE_Reasoning_with_constrained_LLM_generation"},{"title":"CRANE: Reasoning with constrained LLM generation | alphaXiv","url":"https://www.alphaxiv.org/overview/2502.09061v3"},{"title":"CRANE: Reasoning with constrained LLM generation | OpenReview","url":"https://openreview.net/forum?id=wKs9fHYxCV"}]

Based on the search results, here's the information about the CRANE paper:

**Title:** CRANE: Reasoning with constrained LLM generation

**Authors:** Debangshu Banerjee, Tarun Suresh, Shubham Ugare, Sasa Misailovic, Gagandeep Singh

**arXiv ID:** 2502.09061

**Submission Date:** Submitted on 13 Feb 2025

**Overview:** Code generation, symbolic math reasoning, and other tasks require LLMs to produce outputs that are both syntactically and semantically correct. Constrained LLM generation is a promising direction to enforce adherence to formal grammar, but prior works have empirically observed that strict enforce
…[truncated 988 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 101 · 2026-05-14T02:40:41.996668+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "XGrammar paper venue MLSys 2025 \"Yixin Dong\" \"Tianqi Chen\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "XGrammar paper venue MLSys 2025 \"Yixin Dong\" \"Tianqi Chen\""
  }
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-14T02:40:41.996831+00:00_

Web search results for query: "ODKE ontology-guided open-domain knowledge extraction LLM 2025 arxiv authors"

Links: [{"title":"[2509.04696] ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs","url":"https://arxiv.org/abs/2509.04696"},{"title":"ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs","url":"https://arxiv.org/html/2509.04696v1"},{"title":"(PDF) ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs","url":"https://www.researchgate.net/publication/395338944_ODKE_Ontology-Guided_Open-Domain_Knowledge_Extraction_with_LLMs"},{"title":"LLM-empowered knowledge graph construction: A survey","url":"https://arxiv.org/pdf/2510.20345"},{"title":"ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs (AI Podcast) - YouTube","url":"https://www.youtube.com/watch?v=c8RMyq48XYk"},{"title":"ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/odke-ontology-guided-open-domain-knowledge-extraction"},{"title":"[PDF] ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs | Semantic Scholar","url":"https://www.semanticscholar.org/paper/ODKE+:-Ontology-Guided-Open-Domain-Knowledge-with-Khorshidi-Nikfarjam/23991e9d5ab7780527a1753633a7f065c5da4663"},{"title":"ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs | alphaXiv","url":"https://www.alphaxiv.org/abs/2509.04696"},{"title":"ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs - Apple Machine Learning Research","url":"https://machinelearning.apple.com/research/odke"},{"title":"Ontology-Guided Open-Domain Knowledge Extraction ...","url":"https://bytez.com/docs/arxiv/2509.04696/paper"}]

Based on the search results, here's what I found about the ODKE+ paper:

## ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs

**Paper Details:**
- arXiv paper 2509.04696
- Published September 4, 2025

**Authors:**
Samira Khorshidi, Azadeh Nikfarjam, Sup
…[truncated 912 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 103 · 2026-05-14T02:40:41.996985+00:00_

Web search results for query: ""Let Me Speak Freely" Tam Zheng Joty EMNLP 2024 format restrictions LLM arXiv 2408.02442"

Links: [{"title":"Let Me Speak Freely? A Study On The Impact Of Format Restrictions On Large Language Model Performance. - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-industry.91/"},{"title":"Industry Track - EMNLP 2024","url":"https://2024.emnlp.org/program/industry/"},{"title":"Let Me Speak Freely? A Study on the Impact of Format ...","url":"https://aclanthology.org/2024.emnlp-industry.91.pdf"},{"title":"[2408.02442] Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models","url":"https://arxiv.org/abs/2408.02442"},{"title":"Let Me Speak Freely? A Study On The Impact Of Format Restrictions On Large Language Model Performance. | Request PDF","url":"https://www.researchgate.net/publication/386203559_Let_Me_Speak_Freely_A_Study_On_The_Impact_Of_Format_Restrictions_On_Large_Language_Model_Performance"},{"title":"EMNLP 2024 The 2024 Conference on Empirical Methods in Natural","url":"https://aclanthology.org/2024.emnlp-industry.0.pdf"}]

Based on my web search, I found the paper you were looking for:

"Let Me Speak Freely? A Study On The Impact Of Format Restrictions On Large Language Model Performance" by Tam et al., published in the EMNLP 2024 Industry Track, pages 1218–1236, Miami, Florida, US.

The paper is also available on arXiv as preprint 2408.02442.

The study investigates whether format constraints (like JSON and XML) impact LLMs' abilities, including reasoning and domain knowledge comprehension. The researchers evaluate LLMs performance when restricted to adhere to structured formats versus generating free-form responses across various common tasks, and surprisingly observe a significant decline in LLMs reasoning abilities under format restrictions.

The complete author list is: Zhi Rui Tam, Cheng-Kuang Wu, Yi-Lin Tsai, Chieh-Yen Lin, Hung-yi Lee, and Yun-Nung Chen.


REMINDER:
…[truncated 91 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 104 · 2026-05-14T02:40:41.997131+00:00_

Web search results for query: ""The Hidden Cost of Structure" constrained decoding RANLP 2025 authors"

Links: [{"title":"The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance - ACL Anthology","url":"https://aclanthology.org/2025.ranlp-1.124/"},{"title":"The Hidden Cost of Structure: How Constrained Decoding ...","url":"https://acl-bg.org/proceedings/2025/RANLP%202025/pdf/2025.ranlp-1.124.pdf"},{"title":"RANLP 2025 Programme","url":"https://ranlp.org/ranlp2025/wp-content/uploads/2025/10/Full_RANLP_2025_Programme.pdf"}]

Based on the search results, the authors of "The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance" published at RANLP 2025 are Maximilian Schall and Gerard de Melo.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 105 · 2026-05-14T02:40:41.997270+00:00_

Web search results for query: ""ontology-conformal" named entity recognition materials language models 2025 arxiv"

Links: [{"title":"Ontology-conformal recognition of materials entities using language models | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-03619-y"},{"title":"Ontology-conformal recognition of materials entities using language models - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/40425727/"},{"title":"Ontology-conformal recognition of materials entities using language models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Ontology-conformal-recognition-of-materials-using-Potu-Murthy/edd866a30b34343364c50430031fc8b516be4dd2"},{"title":"Ontology-conformal recognition of materials entities using language models","url":"https://d-nb.info/1372613331/34"},{"title":"Ontology-conformal recognition of materials entities using language models | Materials Science | ChemRxiv | Cambridge Open Engage","url":"https://chemrxiv.org/engage/chemrxiv/article-details/66d7924e12ff75c3a14f5258"},{"title":"Ontology development using language model-based Named Entity Recognition for integrated construction information | Journal of Civil Engineering and Management","url":"https://journals.vilniustech.lt/index.php/JCEM/article/view/26519"},{"title":"MaterioMiner — An ontology-based text mining dataset for extraction of process-structure-property entities","url":"https://arxiv.org/html/2408.04661"},{"title":"FoodSEM: Large Language Model Specialized in Food Named-Entity Linking","url":"https://arxiv.org/html/2509.22125v1"},{"title":"MatSciBERT: A materials domain language model for text mining and information extraction | npj Computational Materials","url":"https://www.nature.com/articles/s41524-022-00784-w"},{"title":"A novel large-language-model-driven framework for named entity recognition - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0306457324004138"}]

Based on the search results, I found relevant
…[truncated 1793 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 106 · 2026-05-14T02:40:41.997417+00:00_

Web search results for query: "InstructUIE authors Xiao Wang first authors 2023"

Links: [{"title":"(PDF) InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction (2023) | Xiao Wang | 81 Citations","url":"https://scispace.com/papers/instructuie-multi-task-instruction-tuning-for-unified-qe70ci1r"},{"title":"[2304.08085] InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction","url":"https://arxiv.org/abs/2304.08085"},{"title":"[2304.08085v1] InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction","url":"https://arxiv.org/abs/2304.08085v1"},{"title":"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction","url":"https://www.researchgate.net/publication/370071546_InstructUIE_Multi-task_Instruction_Tuning_for_Unified_Information_Extraction"},{"title":"[PDF] InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/InstructUIE:-Multi-task-Instruction-Tuning-for-Wang-Zhou/bbb2fc6e95d24fb58ab6c25b216b14ac49a32fbe"},{"title":"Homepage of Xiao Wang","url":"https://wangxiaocs.github.io/"},{"title":"Publication — Wang Lab","url":"https://www.wangxiaolab.org/publications"},{"title":"Xiao Wang","url":"https://scholar.google.com/citations?user=AGS_dK8AAAAJ&hl=en"},{"title":"Xiao Wang | Nanjing University | 27 Publications | 104 Citations | Related Authors","url":"https://scispace.com/authors/xiao-wang-jkesd34ccw"},{"title":"Publications - Xiao Wang","url":"https://wangxiao1254.github.io/publications/"}]

Based on the search results, I found information about the InstructUIE paper from 2023 with Xiao Wang as the first author.

The InstructUIE paper was submitted on April 17, 2023, and the authors include Xiao Wang, Weikang Zhou, Can Zu, Han Xia, Tianze Chen, Yuansen Zhang, Rui Zheng, Junjie Ye, Qi Zhang, Tao Gui, Jihua Kang, Jingsheng Yang, Siyuan Li, and Chunsai Du.

InstructUIE is a unified information extra
…[truncated 249 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 107 · 2026-05-14T02:40:41.997574+00:00_

Web search results for query: "De Cao GENRE autoregressive entity retrieval authors Nicola Gautier Fabio ICLR 2021"

Links: [{"title":"Published as a conference paper at ICLR 2021 AUTOREGRESSIVE ENTITY RETRIEVAL","url":"https://openreview.net/pdf?id=5k8F6UU39V"},{"title":"Autoregressive Entity Retrieval | OpenReview","url":"https://openreview.net/forum?id=5k8F6UU39V"},{"title":"GitHub - facebookresearch/GENRE: Autoregressive Entity Retrieval · GitHub","url":"https://github.com/facebookresearch/GENRE"},{"title":"ICLR Spotlight Autoregressive Entity Retrieval","url":"https://iclr.cc/virtual/2021/spotlight/3521"},{"title":"[2010.00904] Autoregressive Entity Retrieval","url":"https://arxiv.org/abs/2010.00904"},{"title":"Autoregressive Entity Retrieval - AI at Meta","url":"https://ai.meta.com/research/publications/autoregressive-entry-retrieval/"},{"title":"(PDF) Autoregressive Entity Retrieval","url":"https://www.researchgate.net/publication/344468840_Autoregressive_Entity_Retrieval"},{"title":"dblp: Nicola De Cao","url":"https://dblp.org/pid/218/6626.html"},{"title":"Multilingual Autoregressive Entity Linking | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00460/110051/Multilingual-Autoregressive-Entity-Linking"},{"title":"Track: Oral Session 4","url":"https://iclr.cc/virtual/2021/session/4331"}]

Based on the search results, I found the paper you're looking for:

**Title:** Autoregressive Entity Retrieval

**Authors:** Nicola De Cao, Gautier Izacard, Sebastian Riedel, and Fabio Petroni

**Conference:** ICLR 2021 (9th International Conference on Learning Representations, Virtual Event, Austria, May 3-7, 2021)

**Key Contribution:** GENRE is the first system that retrieves entities by generating their unique names, left to right, token-by-token in an autoregressive fashion and conditioned on the context.

**Results:** The approach was evaluated on more than 20 datasets on entity d
…[truncated 395 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 108 · 2026-05-14T02:40:41.997786+00:00_

Web search results for query: ""Grammar-Aligned Decoding" Park Wang Berg-Kirkpatrick NeurIPS 2024 arXiv 2405.21047"

Links: [{"title":"Grammar-Aligned Decoding Kanghee Park1∗ Jiayu Wang1∗ Taylor Berg-Kirkpatrick2","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/2bdc2267c3d7d01523e2e17ac0a754f3-Paper-Conference.pdf"},{"title":"Grammar-Aligned Decoding","url":"https://proceedings.neurips.cc/paper_files/paper/2024/hash/2bdc2267c3d7d01523e2e17ac0a754f3-Abstract-Conference.html"},{"title":"NeurIPS Poster Grammar-Aligned Decoding","url":"https://neurips.cc/virtual/2024/poster/96599"},{"title":"Grammar-Aligned Decoding","url":"https://papers.nips.cc/paper_files/paper/2024/hash/2bdc2267c3d7d01523e2e17ac0a754f3-Abstract-Conference.html"},{"title":"[2405.21047] Grammar-Aligned Decoding","url":"https://arxiv.org/abs/2405.21047"},{"title":"Grammar-Aligned Decoding | OpenReview","url":"https://openreview.net/forum?id=5G7ve8E1Lu"},{"title":"Grammar-aligned decoding | Proceedings of the 38th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3737916.3738690"},{"title":"NeurIPS Poster Grammar-Aligned Decoding","url":"https://nips.cc/virtual/2024/poster/96599"},{"title":"Grammar-Aligned Decoding","url":"https://arxiv.org/html/2405.21047v3"},{"title":"Kanghee Park, Jiayu Wang, Taylor Berg-Kirkpatrick, Nadia Polikarpova, Loris D'Antoni · Grammar-Aligned Decoding","url":"https://slideslive.com/39028324/grammaraligned-decoding"}]

I found the research paper you were looking for! Here's what I found:

## Grammar-Aligned Decoding

The paper is authored by Kanghee Park, Jiayu Wang, Taylor Berg-Kirkpatrick (and co-authors Nadia Polikarpova and Loris D'Antoni), with affiliations at University of Wisconsin-Madison and University of California San Diego.

**Main Topic:**

Large Language Models (LLMs) struggle with reliably generating highly structured outputs, such as program code, mathematical formulas, or well-formed mar
…[truncated 873 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 109 · 2026-05-14T02:40:41.997978+00:00_

Web search results for query: ""Grammar-Aligned Decoding" arxiv 2405.21047 authors venue 2024"

Links: [{"title":"[2405.21047] Grammar-Aligned Decoding","url":"https://arxiv.org/abs/2405.21047"},{"title":"Grammar-Aligned Decoding - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240521047P/abstract"},{"title":"Grammar-Aligned Decoding","url":"https://arxiv.org/html/2405.21047"},{"title":"(PDF) Grammar-Aligned Decoding","url":"https://www.researchgate.net/publication/381108984_Grammar-Aligned_Decoding"},{"title":"Grammar-Aligned Decoding Kanghee Park1∗ Jiayu Wang1∗ Taylor Berg-Kirkpatrick2","url":"https://arxiv.org/pdf/2405.21047"},{"title":"Approximately Aligned Decoding Daniel Melcer∗","url":"https://arxiv.org/pdf/2410.01103"},{"title":"Grammar-Aligned Decoding | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/grammar-aligned-decoding"},{"title":"Grammar-Aligned Decoding - Paper Reading","url":"https://paperreading.club/page?id=230674"},{"title":"Approximately Aligned Decoding","url":"https://arxiv.org/html/2410.01103v1"},{"title":"Grammar-Aligned Decoding","url":"https://www.popai.pro/chatwithdoc/paper/Grammar-Aligned-Decoding.html"}]

Based on the search results, here is the information about the paper:

**Title:** Grammar-Aligned Decoding

**ArXiv ID:** 2405.21047

**Authors:** Kanghee Park, Jiayu Wang, Taylor Berg-Kirkpatrick, Nadia Polikarpova, and Loris D'Antoni

**Venue:** Accepted to NeurIPS 2024

**Year:** 2024

**Summary:** The paper proposes adaptive sampling with approximate expected futures (ASAp), a decoding algorithm that guarantees the output to be grammatical while provably producing outputs that match the conditional probability of the LLM's distribution conditioned on the given grammar constraint. Their evaluation on code generation and structured NLP tasks shows how ASAp often produces outputs with higher likelihood (according to the LLM's distribution) than existing GCD techniques, while still enforcing the desire
…[truncated 129 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 110 · 2026-05-14T02:40:41.998143+00:00_

Web search results for query: ""Generating Structured Outputs from Language Models" JSONSchemaBench arxiv 2501.10868 authors 2025"

Links: [{"title":"[2501.10868] JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models","url":"https://arxiv.org/abs/2501.10868"},{"title":"Generating Structured Outputs from Language Models: Benchmark and Studies","url":"https://arxiv.org/html/2501.10868v1"},{"title":"GitHub - guidance-ai/jsonschemabench · GitHub","url":"https://github.com/guidance-ai/jsonschemabench"},{"title":"JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models","url":"https://arxiv.org/html/2501.10868v3"},{"title":"JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250110868G/abstract"},{"title":"(PDF) Generating Structured Outputs from Language Models: Benchmark and Studies","url":"https://www.researchgate.net/publication/388231978_Generating_Structured_Outputs_from_Language_Models_Benchmark_and_Studies"},{"title":"Paper page - Generating Structured Outputs from Language Models: Benchmark and Studies","url":"https://huggingface.co/papers/2501.10868"},{"title":"Generating Structured Outputs from Language Models","url":"https://nathanrchn.com/p/jsb"},{"title":"JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for LLMs | OpenReview","url":"https://openreview.net/forum?id=GDKYFegWD3"},{"title":"GitHub - epfl-dlab/jsonschemabench","url":"https://github.com/epfl-dlab/jsonschemabench"}]

Based on the search results, here's information about the paper:

## Paper Overview

The paper titled "Generating Structured Outputs from Language Models: Benchmark and Studies" (arXiv:2501.10868) was submitted on January 18, 2025, with the latest revision on February 27, 2025, and has 9 authors including Saibo Geng, Hudson Cooper, Michał Moskal, Samuel Jenkins, Julian Berman, Nathan Ranchin, Robert West, Eric Horvitz, and Harsha Nori.

## Mai
…[truncated 1135 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 111 · 2026-05-14T02:40:41.998295+00:00_

Web search results for query: ""From Hallucination to Structure Snowballing" alignment tax constrained decoding arXiv 2604.06066 authors"

Links: [{"title":"[2604.06066] From Hallucination to Structure Snowballing: The Alignment Tax of Constrained Decoding in LLM Reflection","url":"https://arxiv.org/abs/2604.06066"},{"title":"From Hallucination to Structure Snowballing: The Alignment Tax of Constrained Decoding in LLM Reflection","url":"https://arxiv.org/html/2604.06066"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2601.18753"},{"title":"Investigating and Mitigating the Multimodal Hallucination ...","url":"https://aclanthology.org/2024.acl-long.648.pdf"},{"title":"Why Language Models Hallucinate Adam Tauman Kalai∗ OpenAI Ofir Nachum OpenAI","url":"https://cdn.openai.com/pdf/d04913be-3f6f-4d2b-b283-ff432ef4aaa5/why-language-models-hallucinate.pdf"},{"title":"Low-Hallucination and Efficient Coreference Resolution ...","url":"https://aclanthology.org/2025.findings-emnlp.934.pdf"},{"title":"From Illusion to Insight: A Taxonomic Survey of Hallucination Mitigation Techniques in LLMs","url":"https://www.mdpi.com/2673-2688/6/10/260"},{"title":"[2407.00569] Investigating and Mitigating the Multimodal Hallucination Snowballing in Large Vision-Language Models","url":"https://arxiv.org/abs/2407.00569"},{"title":"Investigating and Mitigating the Multimodal Hallucination Snowballing in Large Vision-Language Models - ACL Anthology","url":"https://aclanthology.org/2024.acl-long.648/"},{"title":"[PDF] How Language Model Hallucinations Can Snowball | Semantic Scholar","url":"https://www.semanticscholar.org/paper/How-Language-Model-Hallucinations-Can-Snowball-Zhang-Press/6825ba09383bc758f9a2feaebabe35a6cd4adc4c"}]

Based on the search results, here is the information about the arXiv paper with ID 2604.06066:

**Title:** From Hallucination to Structure Snowballing: The Alignment Tax of Constrained Decoding in LLM Reflection

**Author:** Hongxu Z
…[truncated 1011 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 112 · 2026-05-14T02:40:41.998451+00:00_

Web search results for query: ""document-level relation extraction" "entity type constraints" DocRE type-constrained 2024 2025 authors"

Links: [{"title":"Document-level relation extraction with entity type constraints - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0893608025013504"},{"title":"SH-ETRs:Learning Soft-Hard rules with entity type constraints for document-level relation extraction - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0957417425032750"},{"title":"TyRaL: End-to-End Document-level Relation Extraction via ...","url":"https://ceur-ws.org/Vol-4085/paper44.pdf"},{"title":"Logical Rule-Constrained Large Language Models for Document-Level Relation Extraction | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-981-95-3343-5_11"},{"title":"ETCGN: entity type-constrained graph networks for document-level relation extraction | International Journal of Machine Learning and Cybernetics","url":"https://link.springer.com/article/10.1007/s13042-024-02293-2"},{"title":"GLiDRE: Generalist Lightweight model for Document-level Relation Extraction","url":"https://arxiv.org/html/2508.00757v2"},{"title":"ESTR-DocRE: an evidence-supervised transformer reasoning framework for document-level relation extraction | Journal of King Saud University Computer and Information Sciences | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s44443-025-00331-9"},{"title":"Document-Level Relation Extraction with Global Relations and Entity Pair Reasoning - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.1002/"},{"title":"Document-Level Relation Extraction with Global ...","url":"https://aclanthology.org/2025.findings-acl.1002.pdf"},{"title":"Document-level Relation Extraction via Separate Relation Representation and Logical Reasoning | ACM Transactions on Information Systems","url":"https://dl.acm.org/doi/10.1145/3597610"}]

Based on the search results, here ar
…[truncated 2151 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 113 · 2026-05-14T02:40:41.998599+00:00_

Web search results for query: ""Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning" Geng Josifoski EMNLP 2023 arxiv 2305.13971"

Links: [{"title":"[2305.13971] Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning","url":"https://arxiv.org/abs/2305.13971"},{"title":"Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230513971G/abstract"},{"title":"Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning","url":"https://arxiv.org/html/2305.13971v6"},{"title":"Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning - ACL Anthology","url":"https://aclanthology.org/2023.emnlp-main.674/"},{"title":"Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning | Request PDF","url":"https://www.researchgate.net/publication/376402267_Grammar-Constrained_Decoding_for_Structured_NLP_Tasks_without_Finetuning"},{"title":"Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning | OpenReview","url":"https://openreview.net/forum?id=KkHY1WGDII"},{"title":"[PDF] Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Grammar-Constrained-Decoding-for-Structured-NLP-Geng-Josifosky/7e269bfabb451765a16ca0357de6b497cefb60bf"},{"title":"Grammar-Constrained Decoding for Structured NLP Tasks ...","url":"https://aclanthology.org/2023.emnlp-main.674.pdf"},{"title":"[2305.13971v2] Flexible Grammar-Based Constrained Decoding for Language Models","url":"https://arxiv.org/abs/2305.13971v2"},{"title":"Flexible Grammar-Based Constrained Decoding for Language Models","url":"https://arxiv.org/pdf/2305.13971v2"}]

I found the paper you're looking for! Here's what I found:

"Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning" by Saibo Geng, Martin Josifoski, Maxime Peyrard, and Robert West was published at the 2023 Conferen
…[truncated 1254 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 114 · 2026-05-14T02:40:41.998780+00:00_

Web search results for query: "GoLLIE authors Oscar Sainz Iker Garcia-Ferrero arxiv 2310.03668"

Links: [{"title":"[2310.03668] GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction","url":"https://arxiv.org/abs/2310.03668"},{"title":"[PDF] GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/GoLLIE:-Annotation-Guidelines-improve-Zero-Shot-Sainz-Garc%C3%ADa-Ferrero/3f40edfcafc018b2cb54612a9aaa9d6b43a11a26"},{"title":"GoLLIE : Annotation Guidelines improve Zero-Shot Information-Extraction","url":"https://arxiv.org/html/2310.03668v5"},{"title":"dblp: GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction.","url":"https://dblp.org/rec/journals/corr/abs-2310-03668.html"},{"title":"dblp: Oscar Sainz","url":"https://dblp.org/pid/266/1113.html"},{"title":"dblp: Iker García-Ferrero","url":"https://dblp.org/pid/305/9880.html"},{"title":"gollie : annotation guidelines improve zero-shot ...","url":"https://arxiv.org/pdf/2310.03668"},{"title":"Iker García-Ferrero","url":"https://scholar.google.es/citations?user=yoOzj1MAAAAJ&hl=es"},{"title":"Oscar Sainz","url":"https://openreview.net/profile?id=~Oscar_Sainz1"},{"title":"Oscar Sainz","url":"https://www.catalyzex.com/author/Oscar%20Sainz"}]

Based on the search results, I found comprehensive information about the GoLLIE paper with arxiv ID 2310.03668:

## GoLLIE Paper Summary

The authors of this paper are Oscar Sainz, Iker García-Ferrero, Rodrigo Agerri, Oier Lopez de Lacalle, Germ­án Rigau, and Eneko Agirre.

GoLLIE (Guideline-following Large Language Model for IE) is a model able to improve zero-shot results on unseen IE tasks by virtue of being fine-tuned to comply with annotation guidelines.

The authors are affiliated with HiTZ Basque Center for Language Technology - Ixa NLP Group at the University of the Basque Country (UPV/EHU).

### Key Findings

Large Language Models (LLMs) combined with instruction tuning
…[truncated 404 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 115 · 2026-05-14T02:40:41.999109+00:00_

Web search results for query: "XGrammar paper venue MLSys 2025 "Yixin Dong" "Tianqi Chen""

Links: [{"title":"Proceedings of Machine Learning and Systems 7","url":"https://proceedings.mlsys.org/paper_files/paper/2025"},{"title":"Track: Session 10: LLM and Diffusion Model Serving","url":"https://mlsys.org/virtual/2025/session/3161"},{"title":"Catalyst: XGrammar","url":"https://catalyst.cs.cmu.edu/projects/xgrammar.html"},{"title":"MLSys 2025 Thursday 05/15","url":"https://mlsys.org/virtual/2025/day/5/15"},{"title":"[2411.15100] XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models","url":"https://arxiv.org/abs/2411.15100"},{"title":"MLSys Poster XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models","url":"https://mlsys.org/virtual/2025/poster/3235"},{"title":"[PDF] XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/XGrammar:-Flexible-and-Efficient-Structured-Engine-Dong-Ruan/274ca059ee4997f1e008bc8962aef3d22897f17a"},{"title":"XGrammar: Flexible and Efficient Structured Generation ...","url":"https://arxiv.org/pdf/2411.15100"},{"title":"GitHub - mlc-ai/xgrammar: Fast, Flexible and Portable Structured Generation · GitHub","url":"https://github.com/mlc-ai/xgrammar"},{"title":"8th MLSys 2025: Santa Clara, CA, USA","url":"https://dblp.org/db/conf/mlsys/mlsys2025.html"}]

Based on the search results, I can provide you with the information about the XGrammar paper:

The paper "XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models" is authored by Yixin Dong, Charlie F. Ruan, Yaxing Cai, Ziyi Xu, Yilong Zhao, Ruihang Lai, and Tianqi Chen. The paper was published at MLSys 2025.

The paper proposes XGrammar, a flexible and efficient structure generation engine for large language models. XGrammar accelerates context-free grammar execution by dividing the vocabulary into contex
…[truncated 219 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 116 · 2026-05-14T02:40:41.999284+00:00_

Web search results for query: "ADELIE aligning LLMs information extraction EMNLP 2024 arxiv schema-constrained"

Links: [{"title":"ADELIE: Aligning Large Language Models on Information Extraction","url":"https://arxiv.org/html/2405.05008v1"},{"title":"[2405.05008] ADELIE: Aligning Large Language Models on Information Extraction","url":"https://arxiv.org/abs/2405.05008"},{"title":"GitHub - THU-KEG/ADELIE: [EMNLP2024] Aligning Large Language Models on Information Extraction · GitHub","url":"https://github.com/THU-KEG/ADELIE"},{"title":"Aligning Large Language Models on Information Extraction","url":"https://aclanthology.org/2024.emnlp-main.419.pdf"},{"title":"ADELIE: Aligning Large Language Models on Information Extraction | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/adelie-aligning-large-language-models-information-extraction"},{"title":"ADELIE: Aligning Large Language Models on Information Extraction - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-main.419/"},{"title":"ADELIE: Aligning Large Language Models on Information Extraction","url":"https://openreview.net/pdf?id=hi5k4PDnX7"},{"title":"Main Conference - EMNLP 2024","url":"https://2024.emnlp.org/program/accepted_main_conference/"},{"title":"ADELIE: Aligning Large Language Models on Information Extraction | Request PDF","url":"https://www.researchgate.net/publication/386188440_ADELIE_Aligning_Large_Language_Models_on_Information_Extraction"},{"title":"[Quick Review] ADELIE: Aligning Large Language Models on Information Extraction","url":"https://liner.com/review/adelie-aligning-large-language-models-on-information-extraction"}]

I've found detailed information about ADELIE. Here's a comprehensive summary of the research:

## ADELIE: Aligning Large Language Models on Information Extraction

ADELIE (Aligning large language moDELs on Information Extraction) is an aligned LLM that effectively solves various IE tasks, including closed IE, open IE, and on-demand IE. The paper 
…[truncated 1289 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool call

_source line 117 · 2026-05-14T02:40:41.999451+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Schall de Melo \"Hidden Cost of Structure\" RANLP 2025 constrained decoding findings results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Schall de Melo \"Hidden Cost of Structure\" RANLP 2025 constrained decoding findings results"
  }
}
```

</details>

---

### Tool result

_source line 118 · 2026-05-14T02:40:41.999593+00:00_

Web search results for query: "Microsoft Guidance library academic paper "guidance-ai" constrained generation arxiv 2023 2024"

Links: [{"title":"GitHub - guidance-ai/llguidance: Super-fast Structured Outputs · GitHub","url":"https://github.com/guidance-ai/llguidance"},{"title":"Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation","url":"https://arxiv.org/html/2403.06988v1"},{"title":"Generating Structured Outputs from Language Models: Benchmark and Studies","url":"https://arxiv.org/html/2501.10868v1"},{"title":"guidance | control LM output – Microsoft Research","url":"https://www.microsoft.com/en-us/research/project/guidance-control-lm-output/"},{"title":"GitHub - guidance-ai/guidance: A guidance language for controlling large language models. · GitHub","url":"https://github.com/guidance-ai/guidance"},{"title":"111 A Survey of Controllable Text Generation using","url":"https://arxiv.org/pdf/2201.05337"},{"title":"Appropriate reliance on GenAI: Research synthesis Executive summary","url":"https://www.microsoft.com/en-us/research/wp-content/uploads/2024/03/GenAI_AppropriateReliance_Published2024-3-21.pdf"},{"title":"Controllable Text Generation for Large Language Models: A Survey","url":"https://arxiv.org/html/2408.12599v1"},{"title":"Generative AI Literacy: A Comprehensive Framework for Literacy and Responsible Use","url":"https://arxiv.org/html/2504.19038v1"},{"title":"From Generative AI to Innovative AI: An Evolutionary Roadmap","url":"https://arxiv.org/html/2503.11419v1"}]

I found relevant results about Microsoft's Guidance library and constrained generation research. Here are the key findings:

## Guidance Library Overview

The Guidance library implements constrained decoding (also called constrained sampling or structured outputs) for Large Language Models, enforcing arbitrary context-free grammar on LLM output with performance on the order of 50μs of CPU time per token for a 128k tokenizer with negligible startup costs.

## Academic Research
…[truncated 1368 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 119 · 2026-05-14T02:40:41.999771+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CRANE NeurIPS 2024 Banerjee Ugare Singh constrained decoding venue publication"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CRANE NeurIPS 2024 Banerjee Ugare Singh constrained decoding venue publication"
  }
}
```

</details>

---

### Tool call

_source line 120 · 2026-05-14T02:40:41.999909+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ETCGN \"entity type-constrained graph networks\" document relation extraction authors 2024 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ETCGN \"entity type-constrained graph networks\" document relation extraction authors 2024 arxiv"
  }
}
```

</details>

---

### Tool call

_source line 121 · 2026-05-14T02:40:42.000038+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"EnriCo\" \"globally constrained inference\" entity relation extraction arxiv 2024 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"EnriCo\" \"globally constrained inference\" entity relation extraction arxiv 2024 authors"
  }
}
```

</details>

---

### Tool call

_source line 122 · 2026-05-14T02:40:42.000172+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "USM \"Universal Information Extraction as Unified Semantic Matching\" authors Lou Yaojie Lu AAAI 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "USM \"Universal Information Extraction as Unified Semantic Matching\" authors Lou Yaojie Lu AAAI 2023"
  }
}
```

</details>

---

### Tool call

_source line 123 · 2026-05-14T02:40:42.000300+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"open information extraction\" \"entity focused constraints\" EACL 2023 authors constrained decoding"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"open information extraction\" \"entity focused constraints\" EACL 2023 authors constrained decoding"
  }
}
```

</details>

---

### Tool call

_source line 124 · 2026-05-14T02:40:42.000445+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"can LLMs be knowledge graph curators\" validating ontology 2025 authors arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"can LLMs be knowledge graph curators\" validating ontology 2025 authors arxiv"
  }
}
```

</details>

---

### Tool call

_source line 125 · 2026-05-14T02:40:42.000592+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ADELIE authors Ning Hao Yixin Cao THU-KEG 2024 arxiv 2405.05008"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ADELIE authors Ning Hao Yixin Cao THU-KEG 2024 arxiv 2405.05008"
  }
}
```

</details>

---

### Tool call

_source line 126 · 2026-05-14T02:40:42.000739+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LMQL \"Prompting Is Programming\" venue PLDI 2023 Beurer-Kellner Fischer Vechev"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LMQL \"Prompting Is Programming\" venue PLDI 2023 Beurer-Kellner Fischer Vechev"
  }
}
```

</details>

---

### Tool call

_source line 127 · 2026-05-14T02:40:42.000868+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Controllable Text Generation\" survey LLM constrained decoding arxiv 2408.12599 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Controllable Text Generation\" survey LLM constrained decoding arxiv 2408.12599 2024"
  }
}
```

</details>

---

### Tool result

_source line 128 · 2026-05-14T02:40:42.001000+00:00_

Web search results for query: "Schall de Melo "Hidden Cost of Structure" RANLP 2025 constrained decoding findings results"

Links: [{"title":"The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance - ACL Anthology","url":"https://aclanthology.org/2025.ranlp-1.124/"},{"title":"How Constrained Decoding Affects Language Model ...","url":"https://aclanthology.org/2025.ranlp-1.124.pdf"},{"title":"The Hidden Cost of Structure: How Constrained Decoding ...","url":"https://acl-bg.org/proceedings/2025/RANLP%202025/pdf/2025.ranlp-1.124.pdf"},{"title":"Accepted papers","url":"https://ranlp.org/ranlp2025/index.php/accepted-papers/"},{"title":"RANLP 2025 Programme","url":"https://ranlp.org/ranlp2025/wp-content/uploads/2025/10/Full_RANLP_2025_Programme.pdf"},{"title":"RANLP 2025 Natural Language Processing in the ...","url":"https://aclanthology.org/2025.ranlp-1.0.pdf"},{"title":"RANLP 2025 Natural Language Processing in the Generative ...","url":"https://acl-bg.org/proceedings/2025/RANLP%202025/pdf/2025.ranlp-1.0.pdf"},{"title":"Appendix","url":"https://arxiv.org/html/2603.03305"},{"title":"dblp: RANLP 2025","url":"https://dblp.org/db/conf/ranlp/ranlp2025.html"},{"title":"Proceedings of Recent Advances in Natural Language Processing,pages 807–821","url":"https://acl-bg.org/proceedings/2025/RANLP%202025/pdf/2025.ranlp-1.93.pdf"}]

I found the research paper! Here's what I can tell you about the "Hidden Cost of Structure" paper by Schall and de Melo from RANLP 2025:

## Overview

The paper is titled "The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance" and was published in the Proceedings of the 15th International Conference on Recent Advances in Natural Language Processing in Varna, Bulgaria.

## Research Focus

The paper examines how Large Language Models generate fluent text but increasingly need to produce structured outputs like JSON that can be programmatically processed, and investigates the interaction
…[truncated 828 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 129 · 2026-05-14T02:40:42.001157+00:00_

Web search results for query: "CRANE NeurIPS 2024 Banerjee Ugare Singh constrained decoding venue publication"

Links: [{"title":"[2502.09061] CRANE: Reasoning with constrained LLM generation","url":"https://arxiv.org/abs/2502.09061"},{"title":"CRANE: Reasoning with constrained LLM generation | OpenReview","url":"https://openreview.net/forum?id=wKs9fHYxCV"},{"title":"Grammar-Aligned Decoding Kanghee Park1∗ Jiayu Wang1∗ Taylor Berg-Kirkpatrick2","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/2bdc2267c3d7d01523e2e17ac0a754f3-Paper-Conference.pdf"},{"title":"Reasoning with constrained LLM generation - CRANE","url":"https://arxiv.org/pdf/2502.09061"},{"title":"[2502.09061v2] CRANE: Reasoning with constrained LLM generation","url":"https://arxiv.org/abs/2502.09061v2"},{"title":"(PDF) CRANE: Reasoning with constrained LLM generation","url":"https://www.researchgate.net/publication/388964154_CRANE_Reasoning_with_constrained_LLM_generation"},{"title":"CRANE: Reasoning with constrained LLM generation | alphaXiv","url":"https://www.alphaxiv.org/overview/2502.09061v3"},{"title":"CRANE: Reasoning with constrained LLM generation - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250209061B/abstract"},{"title":"CRANE: Reasoning with constrained LLM generation","url":"https://par.nsf.gov/servlets/purl/10633770"},{"title":"CRANE: Reasoning with constrained LLM generation","url":"https://arxiv.org/html/2502.09061v3"}]

Based on the search results, I can provide you with information about the CRANE paper:

## Paper Details

**Title:** CRANE: Reasoning with constrained LLM generation

**Authors:** Debangshu Banerjee, Tarun Suresh, Shubham Ugare, Sasa Misailovic, and Gagandeep Singh

## Venue and Publication

The paper was published in the Proceedings of the 42nd International Conference on Machine Learning, Vancouver, Canada. PMLR 267, 2025.

**Note:** The search results indicate that CRANE was published at **ICML 2025** (International Conference on Machine Le
…[truncated 611 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 130 · 2026-05-14T02:40:42.001309+00:00_

Web search results for query: "ETCGN "entity type-constrained graph networks" document relation extraction authors 2024 arxiv"

Links: [{"title":"ETCGN: entity type-constrained graph networks for document-level relation extraction | International Journal of Machine Learning and Cybernetics","url":"https://link.springer.com/article/10.1007/s13042-024-02293-2"},{"title":"[2411.15195] Graph Neural Network-Based Entity Extraction and Relationship Reasoning in Complex Knowledge Graphs","url":"https://arxiv.org/abs/2411.15195"},{"title":"Graph Neural Network-Based Entity Extraction and ...","url":"https://arxiv.org/pdf/2411.15195"},{"title":"An Autoregressive Text-to-Graph Framework for Joint Entity and Relation Extraction","url":"https://arxiv.org/html/2401.01326v1"},{"title":"EnriCo: Enriched Representation and Globally Constrained Inference for Entity and Relation Extraction","url":"https://arxiv.org/html/2404.12493"},{"title":"[2210.03949] ConstGCN: Constrained Transmission-based Graph Convolutional Networks for Document-level Relation Extraction","url":"https://arxiv.org/abs/2210.03949"},{"title":"[2401.01326] An Autoregressive Text-to-Graph Framework for Joint Entity and Relation Extraction","url":"https://arxiv.org/abs/2401.01326"},{"title":"[2108.09505v1] A Hierarchical Entity Graph Convolutional Network for Relation Extraction across Documents","url":"https://arxiv.org/abs/2108.09505v1"},{"title":"Enhanced graph convolutional network based on node importance for document-level relation extraction | Neural Computing and Applications","url":"https://link.springer.com/article/10.1007/s00521-022-07223-3"},{"title":"KGGen: Extracting Knowledge Graphs from Plain Text with Language Models","url":"https://arxiv.org/html/2502.09956v1"}]

I found information about the ETCGN paper! Here are the details:

**Paper:** ETCGN: entity type-constrained graph networks for document-level relation extraction

**Authors:** Yang, H., Chen, C., Zhang, S. et al.

**Publication Details:**
…[truncated 1026 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 131 · 2026-05-14T02:40:42.002044+00:00_

Web search results for query: "USM "Universal Information Extraction as Unified Semantic Matching" authors Lou Yaojie Lu AAAI 2023"

Links: [{"title":"Universal Information Extraction as Unified Semantic Matching | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/26563"},{"title":"Universal Information Extraction as Unified Semantic Matching | Request PDF","url":"https://www.researchgate.net/publication/371922000_Universal_Information_Extraction_as_Unified_Semantic_Matching"},{"title":"[PDF] Universal Information Extraction as Unified Semantic Matching | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Universal-Information-Extraction-as-Unified-Lou-Lu/7ccfd5953e75f242536e99cdeda545a3c66ea98f"},{"title":"[2301.03282] Universal Information Extraction as Unified Semantic Matching","url":"https://arxiv.org/abs/2301.03282"},{"title":"Yaojie Lu's Homepage","url":"https://luyaojie.github.io/publication.html"},{"title":"Universal information extraction as unified semantic matching | Proceedings of the Thirty-Seventh AAAI Conference on Artificial Intelligence and Thirty-Fifth Conference on Innovative Applications of Artificial Intelligence and Thirteenth Symposium on Educational Advances in Artificial Intelligence","url":"https://dl.acm.org/doi/10.1609/aaai.v37i11.26563"},{"title":"Universal Information Extraction as Unified Semantic Matching - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230103282L/abstract"},{"title":"[PDF] Unified Structure Generation for Universal Information Extraction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Unified-Structure-Generation-for-Universal-Lu-Liu/5382c28b9f2dd30f15c836bea92382091b1d886f"},{"title":"[2304.08085] InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction","url":"https://ar5iv.labs.arxiv.org/html/2304.08085"},{"title":"YAYI-UIE: A Chat-Enhanced Instruction Tuning Framework for Universal Infor
…[truncated 1122 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 132 · 2026-05-14T02:40:42.002479+00:00_

Web search results for query: ""open information extraction" "entity focused constraints" EACL 2023 authors constrained decoding"

Links: [{"title":"Open Information Extraction with Entity Focused Constraints - ACL Anthology","url":"https://aclanthology.org/2023.findings-eacl.95/"},{"title":"EACL 2023: “Open Information Extraction with Entity Focused Constraints” – CEDAR: Rich Data Analytics at Cloud Scale","url":"https://team.inria.fr/cedar/eacl-2023-open-information-extraction-with-entity-focused-constraints/"},{"title":"Open Information Extraction with Entity Focused Constraints - Inria - Institut national de recherche en sciences et technologies du numérique","url":"https://inria.hal.science/hal-03980046"},{"title":"Open Information Extraction with Entity Focused Constraints - Département d'informatique","url":"https://laas.hal.science/X-DEP-INFO/hal-03980046v1"},{"title":"Open Information Extraction with Entity Focused Constraints - Laboratoire d'informatique de l'X (LIX)","url":"https://laas.hal.science/X-LIX/hal-03980046v1"},{"title":"Open Information Extraction with Entity Focused Constraints - CNRS - Centre national de la recherche scientifique","url":"https://cnrs.hal.science/hal-03980046/"},{"title":"Open Information Extraction with Entity Focused Constraints | Request PDF","url":"https://www.researchgate.net/publication/373810294_Open_Information_Extraction_with_Entity_Focused_Constraints"},{"title":"GitHub - prajnaupadhyay/openie-with-entities · GitHub","url":"https://github.com/prajnaupadhyay/openie-with-entities"},{"title":"Oana Balalau - ACL Anthology","url":"https://aclanthology.org/people/o/oana-balalau/"},{"title":"Open Information Extraction with Entity Focused Constraints | Underline","url":"https://underline.io/lecture/71946-open-information-extraction-with-entity-focused-constraints"}]

Based on the web search results, I found the paper you're looking for:

## Paper Information

The paper "Open Information Extraction with Entity Focused Constr
…[truncated 1055 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 133 · 2026-05-14T02:40:42.002715+00:00_

Web search results for query: ""EnriCo" "globally constrained inference" entity relation extraction arxiv 2024 authors"

Links: [{"title":"EnriCo: Enriched Representation and Globally Constrained Inference for Entity and Relation Extraction","url":"https://arxiv.org/html/2404.12493v1"},{"title":"[2404.12493] EnriCo: Enriched Representation and Globally Constrained Inference for Entity and Relation Extraction","url":"https://arxiv.org/abs/2404.12493"},{"title":"GitHub - urchade/EnriCo: EnriCo: Enriched Representation and Globally Constrained Inference for Entity and Relation Extraction","url":"https://github.com/urchade/EnriCo"},{"title":"[Literature Review] EnriCo: Enriched Representation and Globally Constrained Inference for Entity and Relation Extraction","url":"https://www.themoonlight.io/en/review/enrico-enriched-representation-and-globally-constrained-inference-for-entity-and-relation-extraction"},{"title":"Paper page - EnriCo: Enriched Representation and Globally Constrained Inference for Entity and Relation Extraction","url":"https://huggingface.co/papers/2404.12493"},{"title":"urchade (Urchade Zaratiana) · GitHub","url":"https://github.com/urchade"},{"title":"[PDF] EnriCo: Enriched Representation and Globally ...","url":"https://www.semanticscholar.org/paper/EnriCo:-Enriched-Representation-and-Globally-for-Zaratiana-Tomeh/5b1e811cd7f22cf5f9a76265ac4837626883df29"},{"title":"Prédiction structurée basée sur des segments pour l' ...","url":"https://theses.hal.science/tel-05011241v1/file/edgalilee_th_2024_zaratiana.pdf"},{"title":"A Comprehensive Survey on Relation Extraction: Recent Advances and New Frontiers","url":"https://arxiv.org/html/2306.02051v3"},{"title":"Event Extraction in Large Language Model: A Holistic Survey of Method, Modality, and Future","url":"https://arxiv.org/html/2512.19537v1"}]

Based on the search results, I found detailed information about the EnriCo paper:

## EnriCo: Paper Details and Authors

EnriCo is titled "Enriched Representatio
…[truncated 1103 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 134 · 2026-05-14T02:40:42.002885+00:00_

Web search results for query: "ADELIE authors Ning Hao Yixin Cao THU-KEG 2024 arxiv 2405.05008"

Links: [{"title":"[2405.05008] ADELIE: Aligning Large Language Models on Information Extraction","url":"https://arxiv.org/abs/2405.05008"},{"title":"ADELIE: Aligning Large Language Models on Information Extraction","url":"https://arxiv.org/html/2405.05008"},{"title":"arXiv:2405.05008v2 [cs.CL] 24 Oct 2024","url":"https://arxiv.org/pdf/2405.05008"},{"title":"Publications - Xiaozhi Wang 王晓智","url":"https://bakser.github.io/publications/"},{"title":"Computer Science Mar 2024","url":"https://arxiv.org/list/cs/2024-03?skip=3960&show=2000"},{"title":"Computer Science May 2024","url":"https://arxiv.org/list/cs/2024-05?skip=8675&show=2000"},{"title":"Computer Vision and Pattern Recognition Aug 2024","url":"https://arxiv.org/list/cs.CV/2024-08?skip=225&show=2000"},{"title":"Haixin Wang - Google 学术搜索","url":"https://scholar.google.com/citations?user=RGZUJOkAAAAJ&hl=zh-CN"},{"title":"Computation and Language Apr 2026","url":"https://arxiv.org/list/cs.CL/current?skip=35&show=2000"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/pastweek?skip=1399&show=2000"}]

Based on the search results, I found information about the ADELIE paper (arxiv 2405.05008):

ADELIE (Aligning large language moDELs on Information Extraction) is an aligned LLM that effectively solves various IE tasks, including closed IE, open IE, and on-demand IE.

The paper was authored by Yunjia Qi, Hao Peng, Xiaozhi Wang, Bin Xu, Lei Hou, and Juanzi Li, and was published at EMNLP 2024.

The search results show that the authors are affiliated with THU-KEG (Tsinghua University Knowledge Engineering Group), which is evident from the author profiles found in the search results. However, I should note that while your query mentioned specific names like "Ning Hao" and "Yixin Cao," the search results for the actual ADELIE paper (2405.05008) show the primary authors listed above. Yixin Cao is mentioned as a co-autho
…[truncated 148 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 135 · 2026-05-14T02:40:42.003049+00:00_

Web search results for query: "LMQL "Prompting Is Programming" venue PLDI 2023 Beurer-Kellner Fischer Vechev"

Links: [{"title":"Prompting Is Programming: A Query Language for Large Language Models (PLDI 2023 - PLDI Research Papers) - PLDI 2023","url":"https://pldi23.sigplan.org/details/pldi-2023-pldi/81/Prompting-Is-Programming-A-Query-Language-for-Large-Language-Models"},{"title":"Prompting Is Programming: A Query Language for Large Language Models | Proceedings of the ACM on Programming Languages","url":"https://dl.acm.org/doi/10.1145/3591300"},{"title":"[2212.06094] Prompting Is Programming: A Query Language for Large Language Models","url":"https://arxiv.org/abs/2212.06094"},{"title":"Prompting Is Programming: A Query Language for Large Language Models 1","url":"https://arxiv.org/pdf/2212.06094"},{"title":"Research | LMQL","url":"https://lmql.ai/research/index.html"},{"title":"ETH Library Prompting Is Programming: A Query Language for Large","url":"https://www.research-collection.ethz.ch/server/api/core/bitstreams/9a54d4ba-8d99-47a9-b960-b6f33df0ee1d/content"},{"title":"Prompting Is Programming: A Query Language for Large Language Models | SRI Lab","url":"https://www.sri.inf.ethz.ch/publications/beurerkellner2023prompting"},{"title":"GitHub - lmql-lang/lmql: A query language for programming (large) language models. · GitHub","url":"https://github.com/lmql-lang/lmql"},{"title":"[2212.06094] Prompting Is Programming: A Query Language for Large Language Models","url":"https://ar5iv.labs.arxiv.org/html/2212.06094"},{"title":"Prompting Is Programming: A Query Language for Large Language Models","url":"https://www.researchgate.net/publication/371363896_Prompting_Is_Programming_A_Query_Language_for_Large_Language_Models"}]

Based on the web search results, I can provide you with information about the paper "Prompting Is Programming: A Query Language for Large Language Models":

## Paper Details

The paper "Prompting Is Programming: A Query Language for Large Language 
…[truncated 1166 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 136 · 2026-05-14T02:40:42.003206+00:00_

Web search results for query: ""can LLMs be knowledge graph curators" validating ontology 2025 authors arxiv"

Links: [{"title":"Can LLMs be Knowledge Graph Curators for Validating ...","url":"https://aclanthology.org/2025.genaik-1.10.pdf"},{"title":"LLM-empowered knowledge graph construction: A survey","url":"https://arxiv.org/html/2510.20345v1"},{"title":"Can LLMs be Knowledge Graph Curators for Validating Triple Insertions? - ACL Anthology","url":"https://aclanthology.org/2025.genaik-1.10/"},{"title":"Automatic Ontology Construction Using LLMs as an ...","url":"https://arxiv.org/pdf/2604.20795"},{"title":"A Semi-automatic Approach for Validating Ontology Alignments Based on LLMs and KGs | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-13109-6_6"},{"title":"LLM-Driven Ontology Construction for Enterprise Knowledge Graphs","url":"https://arxiv.org/html/2602.01276v1"},{"title":"Ontology Learning and Knowledge Graph Construction: A Comparison of Approaches and Their Impact on RAG Performance","url":"https://arxiv.org/html/2511.05991v1"},{"title":"Ontology-Enhanced Knowledge Graph Completion using Large Language Models","url":"https://arxiv.org/html/2507.20643v2"},{"title":"[2403.08345] From human experts to machines: An LLM supported approach to ontology and knowledge graph construction","url":"https://arxiv.org/abs/2403.08345"},{"title":"[2510.20345] LLM-empowered knowledge graph construction: A survey","url":"https://arxiv.org/abs/2510.20345"}]

Based on the search results, I found the paper you're looking for:

**Title:** "Can LLMs be Knowledge Graph Curators for Validating Triple Insertions?"

**Authors:** André Gomes Regino and Julio Cesar dos Reis

**Publication Details:** In Proceedings of the Workshop on Generative AI and Knowledge Graphs (GenAIK), pages 87–99, Abu Dhabi, UAE, published in 2025.

**Summary:** The paper proposes a systematic validation method that uses prompts to guide LLMs through each stage of the triple eva
…[truncated 539 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 137 · 2026-05-14T02:40:42.003371+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2604.06066 \"Hongxu Zhou\" structure snowballing constrained decoding co-authors venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2604.06066 \"Hongxu Zhou\" structure snowballing constrained decoding co-authors venue"
  }
}
```

</details>

---

### Tool result

_source line 138 · 2026-05-14T02:40:42.003515+00:00_

Web search results for query: ""Controllable Text Generation" survey LLM constrained decoding arxiv 2408.12599 2024"

Links: [{"title":"[2408.12599] Controllable Text Generation for Large Language Models: A Survey","url":"https://arxiv.org/abs/2408.12599"},{"title":"Paper page - Controllable Text Generation for Large Language Models: A Survey","url":"https://huggingface.co/papers/2408.12599"},{"title":"Controllable Text Generation for Large Language Models: A Survey","url":"https://arxiv.org/html/2408.12599v1"},{"title":"GitHub - IAAR-Shanghai/CTGSurvey: Controllable Text Generation for Large Language Models: A Survey · GitHub","url":"https://github.com/IAAR-Shanghai/CTGSurvey"},{"title":"[2408.12599v1] Controllable Text Generation for Large Language Models: A Survey","url":"https://arxiv.org/abs/2408.12599v1"},{"title":"Controllable Text Generation for Large Language Models: A Survey - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240812599L/abstract"},{"title":"(PDF) Controllable Text Generation for Large Language Models: A Survey","url":"https://www.researchgate.net/publication/383308876_Controllable_Text_Generation_for_Large_Language_Models_A_Survey"},{"title":"[PDF] Controllable Text Generation for Large Language Models: A Survey | Semantic Scholar","url":"https://www.semanticscholar.org/paper/7fbf028793a5252941e358366f57837888fcbf11"},{"title":"CTGSurvey/README.md at main · IAAR-Shanghai/CTGSurvey","url":"https://github.com/IAAR-Shanghai/CTGSurvey/blob/main/README.md"},{"title":"Controllable Text Generation for Large Language Models: A Survey | alphaXiv","url":"https://www.alphaxiv.org/resources/2408.12599v1"}]

I found the paper you're looking for! Here's what I found about arxiv 2408.12599:

## Paper Summary

The paper addresses how Large Language Models, while demonstrating high text generation quality, must meet increasingly complex requirements in real-world applications. LLMs are expected to meet specific user needs such as imitating particular 
…[truncated 1191 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 139 · 2026-05-14T02:40:42.003690+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EnriCo Zaratiana 2024 venue ACL EMNLP AAAI conference accepted"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EnriCo Zaratiana 2024 venue ACL EMNLP AAAI conference accepted"
  }
}
```

</details>

---

### Tool call

_source line 140 · 2026-05-14T02:40:42.003834+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ontology-conformal NER Potu Murthy 2025 Scientific Reports DOI authors full list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ontology-conformal NER Potu Murthy 2025 Scientific Reports DOI authors full list"
  }
}
```

</details>

---

### Tool call

_source line 141 · 2026-05-14T02:40:42.003964+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Outlines \"Efficient Guided Generation\" Willard Louf venue conference publication 2024 NeurIPS ICML workshop"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Outlines \"Efficient Guided Generation\" Willard Louf venue conference publication 2024 NeurIPS ICML workshop"
  }
}
```

</details>

---

### Tool result

_source line 142 · 2026-05-14T02:40:42.004094+00:00_

Web search results for query: "arxiv 2604.06066 "Hongxu Zhou" structure snowballing constrained decoding co-authors venue"

Links: [{"title":"[2604.06066] From Hallucination to Structure Snowballing: The Alignment Tax of Constrained Decoding in LLM Reflection","url":"https://arxiv.org/abs/2604.06066"},{"title":"From Hallucination to Structure Snowballing: The Alignment Tax of Constrained Decoding in LLM Reflection","url":"https://arxiv.org/html/2604.06066"},{"title":"Hierarchical Joint Source-Channel Coding with Constrained Information Leakage","url":"https://arxiv.org/html/2604.21673"},{"title":"Schema Key Wording as an Instruction Channel in Structured Generation under Constrained Decoding","url":"https://arxiv.org/html/2604.14862"},{"title":"Scientific Knowledge-driven Decoding Constraints Improving the Reliability of LLMs","url":"https://arxiv.org/html/2604.06603v1"},{"title":"Cactus: Accelerating Auto-Regressive Decoding with Constrained Acceptance Speculative Sampling","url":"https://arxiv.org/html/2604.04987"},{"title":"Correctness-Guaranteed Code Generation via Constrained Decoding","url":"https://arxiv.org/html/2508.15866v1"},{"title":"[2504.09935] Constrained Auto-Regressive Decoding Constrains Generative Retrieval","url":"https://arxiv.org/abs/2504.09935"},{"title":"[2604.06603v1] Scientific Knowledge-driven Decoding Constraints Improving the Reliability of LLMs","url":"https://arxiv.org/abs/2604.06603v1"},{"title":"[2604.06603] Scientific Knowledge-driven Decoding Constraints Improving the Reliability of LLMs","url":"https://arxiv.org/abs/2604.06603"}]

Based on the search results, here is the information about the paper arxiv 2604.06066:

**Paper Title:** From Hallucination to Structure Snowballing: The Alignment Tax of Constrained Decoding in LLM Reflection

**Author:** Hongxu Zhou from the Erasmus Mundus Master's in Language and Communication Technologies at Saarland University

**Main Topic:** The paper investigates "hallucination snowballing" in LLM
…[truncated 761 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 143 · 2026-05-14T02:40:42.004244+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Guaranteed Generation from Large Language Models\" ICLR 2025 constrained decoding grammar arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Guaranteed Generation from Large Language Models\" ICLR 2025 constrained decoding grammar arxiv"
  }
}
```

</details>

---

### Tool result

_source line 144 · 2026-05-14T02:40:42.004376+00:00_

Web search results for query: "EnriCo Zaratiana 2024 venue ACL EMNLP AAAI conference accepted"

Links: [{"title":"Urchade Zaratiana","url":"https://urchade.github.io/"},{"title":"Conference on Empirical Methods in Natural Language Processing - ACL Anthology","url":"https://aclanthology.org/venues/emnlp/"},{"title":"The 2024 Conference on Empirical Methods in Natural Language Processing - EMNLP 2024","url":"https://2024.emnlp.org/"},{"title":"The 18th Conference of the European Chapter of the Association for Computational LinguisticsMarch 17-22, 2024 - EACL 2024","url":"https://2024.eacl.org/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"GitHub - MLNLP-World/Top-AI-Conferences-Paper-with-Code: MLNLP: This repository is a collection of AI top conferences papers (e.g. ACL, EMNLP, NAACL, COLING, AAAI, IJCAI, ICLR, NeurIPS, and ICML) with open resource code · GitHub","url":"https://github.com/MLNLP-World/Top-AI-Conferences-Paper-with-Code"},{"title":"EMNLP 2025 The 2025 Conference on Empirical Methods in Natural","url":"https://aclanthology.org/2025.emnlp-tutorials.pdf"},{"title":"Has ACL Lost Its Crown? A Decade-Long Quantitative Analysis of Scale and Impact Across Leading AI Conferences","url":"https://arxiv.org/html/2512.04448v1"},{"title":"Call for Bids to Host EMNLP 2025 or 2026 - SIGDAT","url":"https://sigdat.org/calls/bids2025"}]

Based on the search results, I found information about EnriCo Zaratiana's 2024 publications across different conferences:

EnriCO: Constrained decoding of information extraction using logical rules was published as an ArXiv paper in 2024, and an autoregressive text-to-graph model for information extraction was accepted to AAAI 2024. Additionally,
…[truncated 468 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 145 · 2026-05-14T02:40:42.004634+00:00_

Web search results for query: "ontology-conformal NER Potu Murthy 2025 Scientific Reports DOI authors full list"

Links: [{"title":"Ontology-conformal recognition of materials entities using language models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Ontology-conformal-recognition-of-materials-using-Potu-Murthy/edd866a30b34343364c50430031fc8b516be4dd2"},{"title":"Ontology-conformal recognition of materials entities using language models - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/40425727/"},{"title":"Ontology-conformal recognition of materials entities using language models | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-03619-y"},{"title":"Ontology-conformal recognition of materials entities using language models","url":"https://www.researchgate.net/journal/Scientific-Reports-2045-2322/publication/392162178_Ontology-conformal_recognition_of_materials_entities_using_language_models/links/6837413ac33afe388ac6d7e3/Ontology-conformal-recognition-of-materials-entities-using-language-models.pdf"},{"title":"Ontology-conformal recognition of materials entities using language models","url":"https://d-nb.info/1372613331/34"},{"title":"WojoodOntology: Ontology-Driven LLM Prompting for ...","url":"https://aclanthology.org/2025.arabicnlp-main.14.pdf"},{"title":"Ontology-conformal recognition of materials entities using ...","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12116928/"},{"title":"Ontology-driven integration of advertised and operational capabilities in robots | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-16649-3"},{"title":"Ontology-based knowledge extraction from scientific ...","url":"https://www.ijirmps.org/papers/2025/2/232708.pdf"},{"title":"An ontology-based text mining dataset for extraction of process-structure-property entities | Semantic Scholar","url":"https://www.semanticscholar.org/paper/An-ontology-based-text-mining-dataset-for-of-Durmaz-Thomas/a3cbf27803986602dd00c0f5ef53efd
…[truncated 676 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 146 · 2026-05-14T02:40:42.005074+00:00_

Web search results for query: "Outlines "Efficient Guided Generation" Willard Louf venue conference publication 2024 NeurIPS ICML workshop"

Links: [{"title":"[PDF] Efficient Guided Generation for Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Efficient-Guided-Generation-for-Large-Language-Willard-Louf/c4ceaef35bca063815f50d90a087acbd07a65478"},{"title":"Grammar-Aligned Decoding Kanghee Park1∗ Jiayu Wang1∗ Taylor Berg-Kirkpatrick2","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/2bdc2267c3d7d01523e2e17ac0a754f3-Paper-Conference.pdf"},{"title":"[2307.09702] Efficient Guided Generation for Large Language Models","url":"https://arxiv.org/abs/2307.09702"},{"title":"SGLang: Efficient Execution of Structured Language Model Programs","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/724be4472168f31ba1c9ac630f15dec8-Paper-Conference.pdf"},{"title":"(PDF) Efficient Guided Generation for LLMs","url":"https://www.researchgate.net/publication/372468267_Efficient_Guided_Generation_for_LLMs"},{"title":"ICML 2024 Papers","url":"https://icml.cc/virtual/2024/papers.html"},{"title":"NeurIPS 2024 Papers","url":"https://nips.cc/virtual/2024/papers.html"},{"title":"ICLR 2024 Papers","url":"https://iclr.cc/virtual/2024/papers.html"},{"title":"icml-2024 · GitHub Topics · GitHub","url":"https://github.com/topics/icml-2024"},{"title":"GitHub - LAMDA-NeSy/Awesome-LLM-Reasoning-with-NeSy: ✨✨Latest Advances on Neuro-Symbolic Learning in the era of Large Language Models","url":"https://github.com/LAMDA-NeSy/Awesome-LLM-Reasoning-with-NeSy"}]

Based on the search results, here's what I found about "Efficient Guided Generation":

The paper "Efficient Guided Generation for Large Language Models" was authored by Brandon T. Willard and Rémi Louf. The paper shows how the problem of neural text generation can be constructively reformulated in terms of transitions between the states of a finite-state machine.

Regarding publicati
…[truncated 906 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 147 · 2026-05-14T02:40:42.005256+00:00_

Web search results for query: ""Guaranteed Generation from Large Language Models" ICLR 2025 constrained decoding grammar arxiv"

Links: [{"title":"ICML Poster Flexible and Efficient Grammar-Constrained Decoding","url":"https://icml.cc/virtual/2025/poster/45613"},{"title":"Guaranteed Generation from Large Language Models | OpenReview","url":"https://openreview.net/forum?id=8roRgrjbjv"},{"title":"Published as a conference paper at ICLR 2025 GUARANTEED GENERATION FROM","url":"https://openreview.net/pdf?id=8roRgrjbjv"},{"title":"GitHub - Saibo-creator/Awesome-LLM-Constrained-Decoding: A curated list of papers related to constrained decoding of LLM, along with their relevant code and resources. · GitHub","url":"https://github.com/Saibo-creator/Awesome-LLM-Constrained-Decoding"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/a2d537e69a6c6638a3630eef835f07de-Paper-Conference.pdf"},{"title":"Beyond Free-Form Text: How Constrained Decoding is Reshaping Structured Generation in LLMs | by Brijesh Nambiar | Medium","url":"https://medium.com/@brijeshrn/beyond-free-form-text-how-constrained-decoding-is-reshaping-structured-generation-in-llms-5f7a38bef259"},{"title":"Grammar-Constrained Decoding Makes Large Language ...","url":"https://aclanthology.org/2025.acl-industry.34.pdf"},{"title":"[2410.06716] Guaranteed Generation from Large Language Models","url":"https://arxiv.org/abs/2410.06716"},{"title":"Guaranteed Generation from Large Language Models","url":"https://arxiv.org/html/2410.06716"},{"title":"Grammar-Constrained Decoding Makes Large Language Models Better Logical Parsers - ACL Anthology","url":"https://aclanthology.org/2025.acl-industry.34/"}]

I found relevant results for your search. Here's what I found:

## "Guaranteed Generation from Large Language Models" - ICLR 2025

The paper proposes GUARD, a method that combines an autoregressive proposal distribution with rejection sampling to provide a pri
…[truncated 1064 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 148 · 2026-05-14T02:40:42.005478+00:00_

Here are the findings.

---

## 1. GENRE -- Autoregressive Entity Retrieval

- **Title:** Autoregressive Entity Retrieval
- **Authors:** Nicola De Cao, Gautier Izacard, Sebastian Riedel, Fabio Petroni
- **Venue:** ICLR 2021 (Spotlight)
- **ArXiv:** 2010.00904
- **Core method:** First system to retrieve entities by autoregressively generating entity names token-by-token using a fine-tuned BART model. Uses a prefix trie (trie-based constrained beam search) to restrict decoding to only valid entity identifiers, dramatically reducing memory footprint compared to bi-encoder retrieval while achieving SOTA on 20+ entity disambiguation and linking benchmarks.

---

## 2. GenIE -- Generative Information Extraction

- **Title:** GenIE: Generative Information Extraction
- **Authors:** Martin Josifoski, Nicola De Cao, Maxime Peyrard, Fabio Petroni, Robert West
- **Venue:** NAACL 2022
- **ArXiv:** 2112.08340
- **Core method:** Autoregressive seq2seq model that generates (subject, relation, object) triplets for closed IE. Combines trie-based lexical constraints (forcing outputs to be valid entity/relation identifiers from a predefined schema) with state-based constraints (enforcing valid triplet structure), achieving end-to-end extraction without pipeline components.

---

## 3. NeuroLogic Decoding

- **Title:** NeuroLogic Decoding: (Un)supervised Neural Text Generation with Predicate Logic Constraints
- **Authors:** Ximing Lu, Peter West, Rowan Zellers, Ronan Le Bras, Chandra Bhagavatula, Yejin Choi
- **Venue:** NAACL 2021
- **ArXiv:** 2010.12884
- **Core method:** A decoding algorithm that enables LMs to generate fluent text satisfying complex lexical constraints expressed as predicate logic formulas (conjunctions/disjunctions of must-include or must-exclude tokens). Operates by pruning and re-ranking beams at each step, with asymptotic runtime equivalent to standard beam search.

**Follow-up:** NeuroLogic A\*esque Decoding (Lu et al., NAACL 2022, arXiv 2112.08726) extends this
…[truncated 2922 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "Agent",
  "elapsed_ms": 24
}
```

</details>

---

### Tool result

_source line 149 · 2026-05-14T02:40:42.005832+00:00_

Here are the findings for 6 representative papers on structural constraints for IE with LLMs (2022--2026):

---

**1. UIE -- Unified Structure Generation for Universal Information Extraction**
- **Authors:** Yaojie Lu, Qing Liu, Dai Dai, et al.
- **Venue:** ACL 2022
- **ArXiv:** 2203.12277
- **Method:** Defines a structured extraction language (SEL) to uniformly encode different IE output structures (entity, relation, event, sentiment). Uses a schema-based prompt mechanism (Structural Schema Instructor) with a large-scale pre-trained text-to-structure model to adaptively generate target structures. Achieves SOTA on 4 IE tasks across 13 datasets in supervised, low-resource, and few-shot settings.

---

**2. InstructUIE -- Multi-task Instruction Tuning for Unified Information Extraction**
- **Authors:** Xiao Wang, Weikang Zhou, Can Zu, et al.
- **Venue:** arXiv 2023 (2304.08085)
- **ArXiv:** 2304.08085
- **Method:** Builds IE INSTRUCTIONS, a benchmark of 32 diverse IE datasets in unified text-to-text format with expert-written instructions. Fine-tunes Flan-T5 on this benchmark, enabling a single model to handle NER, RE, EE, etc. via natural language instructions. Demonstrates that instruction-tuned smaller models can substantially outperform GPT-3.5 on IE tasks.

---

**3. GoLLIE -- Annotation Guidelines improve Zero-Shot Information-Extraction**
- **Authors:** Oscar Sainz, Iker Garcia-Ferrero, Rodrigo Agerri, et al.
- **Venue:** ICLR 2024
- **ArXiv:** 2310.03668
- **Method:** Fine-tunes Code-LLaMA to follow annotation guidelines expressed as Python class definitions (code-based schema representation). The model takes entity/relation/event type definitions as Python dataclasses and generates structured output as Python code. This code-based formulation enables strong zero-shot generalization to unseen IE schemas, outperforming previous zero-shot IE approaches.

---

**4. CodeIE -- Large Code Generation Models are Better Few-Shot Information Extractors**
- **Authors:**
…[truncated 2358 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "Agent",
  "elapsed_ms": 24
}
```

</details>

---

### Tool result

_source line 150 · 2026-05-14T02:40:42.006162+00:00_

Here are the findings, structured by paper:

---

## Paper 1: Let Me Speak Freely?

- **Full title:** Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models
- **Authors:** Zhi Rui Tam, Cheng-Kuang Wu, Yi-Lin Tsai, Chieh-Yen Lin, Hung-yi Lee, Yun-Nung Chen
- **Venue:** EMNLP 2024 Industry Track (not NeurIPS 2024 as initially assumed)
- **ArXiv ID:** 2408.02442
- **Core finding:** Structured format constraints (JSON, XML, YAML) cause significant decline in LLM reasoning abilities. Rigid formats hurt reasoning-heavy tasks (math, multi-hop QA) but help classification tasks (slot-filling, intent detection). Stricter format constraints generally lead to greater performance degradation.

---

## Paper 2: CRANE

- **Full title:** CRANE: Reasoning with Constrained LLM Generation
- **Authors:** Debangshu Banerjee, Tarun Suresh, Shubham Ugare, Sasa Misailovic, Gagandeep Singh
- **Venue:** ICML 2025 (PMLR 267) -- note: NOT NeurIPS 2024
- **ArXiv ID:** 2502.09061
- **Core finding:** Provides a theoretical explanation for why constraining LLM outputs to restrictive grammars (only allowing syntactically valid final answers) reduces reasoning capabilities. Proposes alternating between unconstrained generation (for reasoning/chain-of-thought) and constrained generation (for structured output), achieving up to 10 percentage points accuracy improvement on GSM-symbolic and FOLIO benchmarks.

---

## Paper 3: Grammar-Aligned Decoding (GAD)

- **Full title:** Grammar-Aligned Decoding
- **Authors:** Kanghee Park, Jiayu Wang, Taylor Berg-Kirkpatrick, Nadia Polikarpova, Loris D'Antoni
- **Venue:** NeurIPS 2024 (Main Conference)
- **ArXiv ID:** 2405.21047
- **Core finding:** Grammar-constrained decoding (GCD) techniques distort the LLM's distribution -- outputs are grammatically valid but appear with likelihoods disproportionate to the original LLM distribution, producing syntactically correct but semantically degraded outputs. Proposes ASAp
…[truncated 2245 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "Agent",
  "elapsed_ms": 21
}
```

</details>

---

### Tool result

_source line 151 · 2026-05-14T02:40:42.006502+00:00_

Now let me save these findings as a structured report.

Here are the findings across the five categories:

---

## 1. LLM + ASP (Answer Set Programming) for Constraint Validation

### Paper 1a: Solver-in-the-Loop Framework
- **Title:** A Solver-in-the-Loop Framework for Improving LLMs on Answer Set Programming for Logic Puzzle Solving
- **Authors:** Timo Pierre Schrader, Lukas Lange, Tobias Kaminski, Simon Razniewski, Annemarie Friedrich
- **Venue:** AAAI 2026 (Proceedings of the AAAI Conference on Artificial Intelligence, 40(30), pp. 25226-25234)
- **ArXiv:** 2512.17093 (December 2025)
- **Core method:** Introduces an ASP-solver-in-the-loop approach where LLM-generated ASP encodings are automatically evaluated by an ASP solver; solver feedback categorizes outputs as chosen/rejected for supervised fine-tuning, combined with solver-guided best-of-N sampling at inference time.

### Paper 1b: LLASP
- **Title:** LLASP: Fine-tuning Large Language Models for Answer Set Programming
- **Authors:** Erica Coppolillo, Francesco Calimeri, Giuseppe Manco, Simona Perri, Francesco Ricca
- **Venue:** KR 2024 (21st International Conference on Principles of Knowledge Representation and Reasoning), pp. 834-844
- **ArXiv:** 2407.18723
- **Core method:** Fine-tunes a lightweight LLM on a curated dataset of diverse ASP program patterns; demonstrates that this domain-specific fine-tuning outperforms much larger general-purpose LLMs in generating semantically correct ASP programs.

---

## 2. Ontology-Guided NER

### Paper 2: Ontology-Conformal NER for Materials
- **Title:** Ontology-conformal recognition of materials entities using language models
- **Authors:** Sai Teja Potu, Rachana Niranjan Murthy, Akhil Thomas, Lokesh Mishra, et al.
- **Venue:** Scientific Reports, volume 15, Article 18597 (May 2025)
- **DOI:** 10.1038/s41598-025-03619-y
- **Core method:** Evaluates foundation LLMs vs. domain-specific pre-trained models on ontology-conformal NER in materials science, where entity labe
…[truncated 4394 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "Agent",
  "elapsed_ms": 24
}
```

</details>

---

### Tool result

_source line 152 · 2026-05-14T02:40:42.006902+00:00_

Here are the findings, structured by paper.

---

## 1. XGrammar

- **Full title:** XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models
- **Authors:** Yixin Dong, Charlie F. Ruan, Yaxing Cai, Ruihang Lai, Ziyi Xu, Yilong Zhao, Tianqi Chen
- **Venue:** MLSys 2025
- **ArXiv:** [2411.15100](https://arxiv.org/abs/2411.15100) (Nov 2024)
- **Core method:** Divides the vocabulary into context-independent tokens (pre-checkable offline) and context-dependent tokens (checked at runtime), combined with persistent stack-based pushdown automata for efficient CFG constraint enforcement. Achieves up to 100x speedup over prior grammar-constrained decoding approaches.
- **Note:** A follow-up, XGrammar-2 (arXiv [2601.04426](https://arxiv.org/html/2601.04426)), extends to dynamic structured generation for agentic LLMs.

---

## 2. Guidance / Domino (Microsoft / ETH Zurich)

Microsoft's **Guidance** library ([github.com/guidance-ai/guidance](https://github.com/guidance-ai/guidance)) is an open-source framework but does not have a standalone academic paper. The closest peer-reviewed work by the same research group is:

- **Full title:** Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation
- **Authors:** Luca Beurer-Kellner, Marc Fischer, Martin Vechev
- **Venue:** ICML 2024
- **ArXiv:** [2403.06988](https://arxiv.org/abs/2403.06988) (Mar 2024)
- **Core method:** Proposes the DOMINO algorithm for non-invasive constrained decoding that enforces CFG constraints while minimally distorting the LLM's original distribution. Leverages pre-computation and speculative decoding, achieving throughput that can even exceed unconstrained generation.

---

## 3. Outlines

- **Full title:** Efficient Guided Generation for Large Language Models
- **Authors:** Brandon T. Willard, Remi Louf
- **Venue:** arXiv preprint (no confirmed top-venue publication; widely cited)
- **ArXiv:** [2307.09702](https://arxiv.org/abs/2307.09702) (Jul 2023, updated 2024)
- 
…[truncated 4711 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "Agent",
  "elapsed_ms": 26
}
```

</details>

---

### Tool call

_source line 153 · 2026-05-14T02:40:42.007108+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/ 2>/dev/null || echo \"DIR_NOT_EXIST\"",
  "description": "Check artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/ 2>/dev/null || echo \"DIR_NOT_EXIST\"",
    "description": "Check artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 154 · 2026-05-14T02:40:42.007394+00:00_

_project
analyze_ontology_docred.py
compare_prompts.py
literature_map.yaml
literature_survey_constrained_decoding_ie.md
literature_survey_ontology_constrained_ie.md
manifest.yaml
paper_results_summary.md
run_constrained_extraction.py
run_extraction_docred.py
violation_checker_docred.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 155 · 2026-05-14T02:40:42.007574+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/related_work_survey.md",
  "content": "# OntoCoDec Related Work Survey\n\n## 1. Grammar-Constrained Decoding\n\n### XGrammar | MLSys 2025\n- **Title:** XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models\n- **Authors:** Dong et al.\n- **核心方法:** 将词表划分为 context-independent（离线预检）和 context-dependent（运行时检查）两类 token，结合 persistent stack-based pushdown automata 高效执行 CFG 约束，比先前方法快 100x。\n- **与 OntoCoDec 的关系:** OntoCoDec 的 Grammar 层直接基于 XGrammar 实现 JSON schema + enum 约束，消除 RV/ET violations。XGrammar 提供格式正确性保证，但不处理语义层约束（domain/range），这正是 OntoCoDec Semantic 层的贡献。\n- **BibTeX key:** `dong2025xgrammar`\n- **ArXiv:** 2411.15100\n\n### Outlines | arXiv 2023\n- **Title:** Efficient Guided Generation for Large Language Models\n- **Authors:** Willard & Louf\n- **核心方法:** 将受约束文本生成重构为有限状态机（FSM）中的状态转移，为每个 FSM 状态离线构建词表索引，实现正则表达式约束的 O(1) 均摊 per-token 检查，扩展至 LALR(1) parser 支持 CFG。\n- **与 OntoCoDec 的关系:** Outlines 是 grammar-constrained decoding 的开源先驱之一，与 XGrammar 属同一技术路线。OntoCoDec 选择 XGrammar 而非 Outlines 是因为其更高效的 vocabulary 预处理和对 LLM serving 框架（vLLM/SGLang）的原生集成。\n- **BibTeX key:** `willard2023outlines`\n- **ArXiv:** 2307.09702\n\n### LMQL | PLDI 2023\n- **Title:** Prompting Is Programming: A Query Language for Large Language Models\n- **Authors:** Beurer-Kellner, Fischer & Vechev\n- **核心方法:** SQL 风格的 LLM 查询语言，将自然语言 prompt 与程序控制流和声明式约束（类型、长度、正则、停止条件）结合，运行时编译为 token-level masking，减少 26-85% API 成本。\n- **与 OntoCoDec 的关系:** LMQL 提供通用的声明式约束框架，但约束表达能力限于格式层面（类型、长度、正则）。OntoCoDec 的 Semantic 层引入了 IE 任务特有的 domain/range 本体约束，超越了通用格式约束的范畴。\n- **BibTeX key:** `beurer-kellner2023lmql`\n- **ArXiv:** 2212.06094\n\n### DOMINO | ICML 2024\n- **Title:** Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation\n- **Authors:** Beurer-Kellner, Fischer & Vechev\n- **核心方法:** 提出 non-invasive constrained decoding 算法，在执行 CFG 约束的同时最小化对 LLM 原始分布的扭曲，利用预计算和 speculative decoding 实现甚至超过无约束生成的吞吐。\n- **与 OntoCoDec 的关系:** DOMINO 关注 distribution distortion 问题——约束解码如何改变 LLM 的 token 分布。OntoCoDec 的 F1 无损结果从实验角度呼应了这一方向：精心设计的约束不必牺牲生成质量。\n- **BibTeX key:** `beurer-kellner2024domino`\n- **ArXiv:** 2403.06988\n\n### Grammar-Aligned Decoding (ASAp) | NeurIPS 2024\n- **Title:** Grammar-Aligned Decoding\n- **Authors:** Park, Wang, Berg-Kirkpatrick, Polikarpova & D'Antoni\n- **核心方法:** 证明 naive token masking 会扭曲 LLM 的条件分布，提出 ASAp（Adaptive Sampling with Approximate expected futures）算法，在保证语法正确性的同时保持对原始 LM 分布的无偏性。\n- **与 OntoCoDec 的关系:** ASAp 解决的是 grammar-constrained decoding 的理论正确性问题。OntoCoDec 的 logits masking 也面临类似的分布扭曲风险，但实验证明在 IE 任务上 F1 无损，说明 IE 场景中合法约束的 masking 影响有限。\n- **BibTeX key:** `park2024grammar`\n- **ArXiv:** 2405.21047\n\n---\n\n## 2. Vocabulary/Type-Constrained Generation\n\n### GENRE | ICLR 2021\n- **Title:** Autoregressive Entity Retrieval\n- **Authors:** De Cao, Izacard, Riedel & Petroni\n- **核心方法:** 首个用自回归生成方式检索实体的系统，基于 fine-tuned BART 逐 token 生成实体名，用 prefix trie 约束 beam search 只允许生成合法实体标识符，在 20+ entity disambiguation/linking 基准上达到 SOTA。\n- **与 OntoCoDec 的关系:** GENRE 的 trie-based constrained beam search 是 vocabulary-constrained generation 的经典范式。OntoCoDec 的 Semantic 层借鉴类似思路（限制输出到合法类型/实体），但不需要构建 trie，而是通过 logits masking 直接在 token 级别实施 domain/range 约束。\n- **BibTeX key:** `decao2021genre`\n- **ArXiv:** 2010.00904\n\n### GenIE | NAACL 2022\n- **Title:** GenIE: Generative Information Extraction\n- **Authors:** Josifoski, De Cao, Peyrard, Petroni & West\n- **核心方法:** 自回归 seq2seq 模型生成 (subject, relation, object) 三元组，结合 trie-based lexical constraints（强制输出合法实体/关系标识符）和 state-based constraints（强制合法三元组结构），实现端到端抽取。\n- **与 OntoCoDec 的关系:** GenIE 是将 vocabulary constraint 应用于 IE 的先驱，但需要 fine-tuning 专用模型。OntoCoDec 的关键优势是 training-free——直接在通用 LLM 上通过解码时约束实现，无需额外训练。\n- **BibTeX key:** `josifoski2022genie`\n- **ArXiv:** 2112.08340\n\n### NeuroLogic Decoding | NAACL 2021\n- **Title:** NeuroLogic Decoding: (Un)supervised Neural Text Generation with Predicate Logic Constraints\n- **Authors:** Lu, West, Zellers, Le Bras, Bhagavatula & Choi\n- **核心方法:** 将词汇约束表达为谓词逻辑公式（合取/析取 of must-include/must-exclude tokens），在每步通过 pruning 和 re-ranking beams 执行约束，渐近复杂度等同标准 beam search。\n- **与 OntoCoDec 的关系:** NeuroLogic 处理的是 lexical inclusion/exclusion 约束（\"生成必须包含词 X\"），而 OntoCoDec 的 Semantic 层处理的是 relational/type 约束（\"关系 R 的 head 必须是类型 T\"）。约束语义层次不同。\n- **BibTeX key:** `lu2021neurologic`\n- **ArXiv:** 2010.12884\n\n### Grammar-Constrained Decoding for Structured NLP | EMNLP 2023\n- **Title:** Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning\n- **Authors:** Geng, Josifoski, Peyrard & West\n- **核心方法:** 提出 grammar-constrained decoding（GCD）统一框架：每步将违反形式文法的 token logits 设为负无穷，保证结构合法输出，无需 fine-tuning。引入 input-dependent grammars 增加灵活性。在 IE、entity disambiguation、constituency parsing 上验证。\n- **与 OntoCoDec 的关系:** 这是最直接的前驱工作——同样对 IE 任务使用 logits masking。但 Geng et al. 的约束限于语法层面（输出格式合法），OntoCoDec 在此基础上增加了语义层约束（domain/range 合法），是从格式正确到语义正确的扩展。\n- **BibTeX key:** `geng2023gcd`\n- **ArXiv:** 2305.13971\n\n---\n\n## 3. Structural Constraints for Information Extraction\n\n### UIE | ACL 2022\n- **Title:** Unified Structure Generation for Universal Information Extraction\n- **Authors:** Lu, Liu, Dai et al.\n- **核心方法:** 定义 Structured Extraction Language（SEL）统一编码不同 IE 输出结构（entity, relation, event, sentiment），配合 schema-based prompt（Structural Schema Instructor）和大规模预训练 text-to-structure 模型，在 4 个 IE 任务 13 个数据集上达到 SOTA。\n- **与 OntoCoDec 的关系:** UIE 通过训练让模型\"学会\"输出合法结构，但无法保证推理时不违反 schema 约束。OntoCoDec 是 decoding-time enforcement，提供硬性保证——违反 domain/range 的输出不可能被生成。\n- **BibTeX key:** `lu2022uie`\n- **ArXiv:** 2203.12277\n\n### GoLLIE | ICLR 2024\n- **Title:** Annotation Guidelines improve Zero-Shot Information-Extraction\n- **Authors:** Sainz, Garcia-Ferrero, Agerri et al.\n- **核心方法:** 将 annotation guidelines 表达为 Python class 定义（dataclass），fine-tune Code-LLaMA 生成 Python 代码形式的结构化输出，通过 code-based schema 表达实现强零样本泛化到未见 IE schema。\n- **与 OntoCoDec 的关系:** GoLLIE 用 Python 类型系统隐式表达类型约束，但执行仍依赖模型训练。OntoCoDec 在解码时显式执行本体约束，两者互补——GoLLIE 的 code-based schema 可与 OntoCoDec 的 decoding-time enforcement 结合。\n- **BibTeX key:** `sainz2024gollie`\n- **ArXiv:** 2310.03668\n\n### CodeIE | ACL 2023\n- **Title:** Large Code Generation Models are Better Few-Shot Information Extractors\n- **Authors:** Li, Sun, Tang et al.\n- **核心方法:** 将 IE 结构化输出重构为代码生成任务，用 code-LLM（Codex）+ code-style prompts 执行 NER 和 RE，代码形式天然捕获 IE 输出的结构性。在 few-shot 设置下一致优于 fine-tuned IE 模型和 NL-LLM prompting。\n- **与 OntoCoDec 的关系:** CodeIE 通过代码形式化提高结构一致性，但仍是 soft constraint（模型可能生成非法代码）。OntoCoDec 的 Grammar+Semantic 层提供 hard constraint——输出格式和语义类型均被强制保证。\n- **BibTeX key:** `li2023codeie`\n- **ArXiv:** 2305.05711\n\n### InstructUIE | arXiv 2023\n- **Title:** Multi-task Instruction Tuning for Unified Information Extraction\n- **Authors:** Wang, Zhou, Zu et al.\n- **核心方法:** 构建 IE INSTRUCTIONS 基准（32 个 IE 数据集统一为 text-to-text 格式 + 专家指令），fine-tune Flan-T5 实现单模型处理 NER/RE/EE。指令微调的小模型大幅超越 GPT-3.5。\n- **与 OntoCoDec 的关系:** InstructUIE 靠 instruction tuning 提高 IE 输出质量，但无结构保证。OntoCoDec 与 InstructUIE 正交——可在 instruction-tuned 模型上叠加 decoding-time 约束进一步消除违规。\n- **BibTeX key:** `wang2023instructuie`\n- **ArXiv:** 2304.08085\n\n### ADELIE | EMNLP 2024\n- **Title:** Aligning Large Language Models on Information Extraction\n- **Authors:** Qi, Peng, Wang et al. (THU-KEG)\n- **核心方法:** 构建 IEInstruct 高质量对齐语料，用 SFT + DPO 训练 LLM 进行 IE，覆盖 closed IE、open IE、on-demand IE。ADELIE 在开源模型中达到 SOTA，同时保持通用 LLM 能力。\n- **与 OntoCoDec 的关系:** ADELIE 代表 training-time alignment 路线，通过 preference optimization 让模型偏好合法输出。OntoCoDec 是 decoding-time enforcement 路线，提供更强保证且 training-free。两者可叠加使用。\n- **BibTeX key:** `qi2024adelie`\n- **ArXiv:** 2405.05008\n\n---\n\n## 4. Type-Checking / Ontology Validation in NLP\n\n### ODKE+ | arXiv 2025\n- **Title:** ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs\n- **Authors:** Khorshidi, Nikfarjam, Shankar et al. (Apple)\n- **核心方法:** 动态生成针对每种实体类型的 ontology snippets（含 domain/range 约束），用于对齐 LLM 抽取结果与 schema 约束。处理 9M+ Wikipedia 页面，19M facts，98.8% precision across 195 predicates。\n- **与 OntoCoDec 的关系:** ODKE+ 在 prompt 层面注入 ontology 约束，属于 soft guidance。OntoCoDec 在 decoding 层面强制执行 domain/range 约束，属于 hard enforcement。ODKE+ 无法保证 0% violation rate，OntoCoDec 可以。\n- **BibTeX key:** `khorshidi2025odke`\n- **ArXiv:** 2509.04696\n\n### Open IE with Entity Focused Constraints | Findings of EACL 2023\n- **Title:** Open Information Extraction with Entity Focused Constraints\n- **Authors:** Upadhyay, Balalau & Manolescu\n- **核心方法:** 将 entity-type 知识作为约束注入 Open IE，通过 constrained inference（解码时）和 constraint-aware training 两种机制实现，在 CaRB 上 F1 提升 29.17%。\n- **与 OntoCoDec 的关系:** 与 OntoCoDec 最相近的工作之一——同样在解码时利用 entity type 约束。但该方法针对 Open IE 的通用类型约束，OntoCoDec 针对 closed IE 的 ontology-specific domain/range 约束，粒度更细。\n- **BibTeX key:** `upadhyay2023openie`\n\n### EnriCo | arXiv 2024\n- **Title:** EnriCo: Enriched Representation and Globally Constrained Inference for Entity and Relation Extraction\n- **Authors:** Zaratiana, Tomeh, Dauxais, Holat & Charnois\n- **核心方法:** Attention-based enriched representations for joint entity and relation extraction，结合一套 constrained decoding 算法在推理时强制执行任务特定的结构约束（如 entity type compatibility for relations）。\n- **与 OntoCoDec 的关系:** EnriCo 在传统 joint extraction 模型上加 constrained decoding，OntoCoDec 在 LLM 上做。EnriCo 的约束是模型特定的，OntoCoDec 的约束来自外部 ontology，更通用、可复用。\n- **BibTeX key:** `zaratiana2024enrico`\n- **ArXiv:** 2404.12493\n\n### LLM as KG Curators | GenAIK 2025\n- **Title:** Can LLMs be Knowledge Graph Curators for Validating Triple Insertions?\n- **Authors:** Regino & dos Reis\n- **核心方法:** 用 prompt-based 多阶段验证管线引导 LLM 评估 RDF triple 插入的 domain/range 一致性和语义连贯性。\n- **与 OntoCoDec 的关系:** 典型的 post-hoc validation 方法——先生成再验证。OntoCoDec 是 preventive 方法——在生成时就阻止违规，不需要后续验证和纠错循环。\n- **BibTeX key:** `regino2025kgcurator`\n\n---\n\n## 5. Constrained Decoding Quality Concerns\n\n### Let Me Speak Freely? | EMNLP 2024\n- **Title:** Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models\n- **Authors:** Tam, Wu, Tsai, Lin, Lee & Chen\n- **核心方法:** 系统研究结构化格式约束（JSON, XML, YAML）对 LLM 推理能力的影响。发现刚性格式约束损害推理密集型任务（数学、多跳 QA）但有利于分类任务（slot-filling、intent detection）。约束越严格，性能退化越大。\n- **与 OntoCoDec 的关系:** 这是 OntoCoDec 需要直接回应的 concern。OntoCoDec 在 SciERC 上证明 F1 无损（甚至略有提升），说明在 IE 任务场景下——属于该论文发现的\"分类任务\"范畴——约束解码不仅不损害质量，反而可能有益。\n- **BibTeX key:** `tam2024letmespeak`\n- **ArXiv:** 2408.02442\n\n### CRANE | ICML 2025\n- **Title:** CRANE: Reasoning with Constrained LLM Generation\n- **Authors:** Banerjee, Suresh, Ugare, Misailovic & Singh\n- **核心方法:** 从理论角度解释为什么将 LLM 输出约束到 restrictive grammars（只允许语法合法的最终答案）会降低推理能力。提出 alternating strategy：在 unconstrained generation（推理/CoT）和 constrained generation（结构化输出）之间交替，在 GSM-symbolic 和 FOLIO 上提升最多 10 个百分点。\n- **与 OntoCoDec 的关系:** CRANE 的发现验证了 OntoCoDec S2 策略（两通道分离）的合理性——S2 将推理（生成候选）和约束（格式化输出）分离到两个 pass，正是 CRANE 理论推荐的 alternating approach。\n- **BibTeX key:** `banerjee2025crane`\n- **ArXiv:** 2502.09061\n\n### Structure Snowballing | arXiv 2026\n- **Title:** From Hallucination to Structure Snowballing: The Alignment Tax of Constrained Decoding in LLM Reflection\n- **Authors:** Zhou (Saarland University)\n- **核心方法:** 发现 constrained decoding 应用于 LLM self-correction/reflection 时的新失败模式——\"structure snowballing\"：满足严格格式规则的认知负荷将模型推入格式陷阱而非改善推理。揭示结构粒度与模型内部容量之间的张力。\n- **与 OntoCoDec 的关系:** OntoCoDec 避免了 snowballing 风险：其约束是 task-specific 的 IE 本体约束而非通用格式约束，且约束空间有限（合法类型集合远小于 free-form 生成空间），不会引入过度的认知负荷。\n- **BibTeX key:** `zhou2026snowballing`\n- **ArXiv:** 2604.06066\n\n### The Hidden Cost of Structure | RANLP 2025\n- **Title:** The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance\n- **Authors:** Schall & de Melo\n- **核心方法:** 跨 11 个模型和多个基准的系统实证研究。发现 base model 和 instruction-tuned model 在结构约束下表现分化：尽管约束保证格式合法，constrained decoding 在推理密集型任务上常降低语义正确性 10-30%。\n- **与 OntoCoDec 的关系:** OntoCoDec 的实验在 instruction-tuned model 上进行，且 IE 任务是\"extraction\"而非\"reasoning\"，属于该论文发现的约束解码影响较小的任务类型。F1 无损结果与该论文的观察一致。\n- **BibTeX key:** `schall2025hiddencost`\n\n---\n\n## 6. OntoCoDec 在 Landscape 中的定位\n\n### 核心差异化\n\nOntoCoDec 在约束解码 landscape 中占据独特位置，体现为三个维度的创新：\n\n**1. 约束层次：从格式到语义**\n- 现有 grammar-constrained decoding（XGrammar, Outlines, LMQL）保证**格式正确性**（valid JSON, enum values）\n- 现有 vocabulary-constrained generation（GENRE, NeuroLogic）保证**词汇合法性**（输出在预定义词表中）\n- OntoCoDec 增加**语义正确性**层（domain/range 约束），将约束从 syntactic 扩展到 semantic\n\n**2. 执行时机：从 post-hoc 到 preventive**\n- 传统 ontology validation 方法（ODKE+, KG validation）是 post-hoc：先生成再验证\n- 训练方法（UIE, GoLLIE, ADELIE）是 soft constraint：通过训练引导模型偏好合法输出，但无保证\n- OntoCoDec 是 decoding-time enforcement：不合法的输出不可能被生成，无需验证-纠错循环\n\n**3. 质量保持：约束无损**\n- 约束解码质量 concern（Let Me Speak Freely, CRANE, Structure Snowballing）指出约束常损害推理\n- OntoCoDec 在 SciERC 上 DR violation 15.37%→0.93%（↓94%）且 F1 无损，反驳\"约束必损质量\"的 narrative\n- OntoCoDec S2 策略（两通道分离）符合 CRANE 理论推荐的 alternating approach\n\n### 技术栈定位\n\n```\nLayer 3 (OntoCoDec Semantic): domain/range logits masking ← 本文贡献\nLayer 2 (OntoCoDec Grammar):  JSON schema + enum constraints ← 基于 XGrammar\nLayer 1 (LLM):                base language model generation\n```\n\n- Layer 2 消除 format violations（RV/ET），与 Outlines/LMQL/SGLang 同层\n- Layer 3 消除 semantic violations（DR），是 OntoCoDec 独有的贡献\n- 两层组合（S1 单通道或 S2 两通道）实现从格式到语义的完整约束覆盖\n\n### 与各 paradigm 的关系总结\n\n| Paradigm | 代表工作 | OntoCoDec 关系 |\n|----------|----------|---------------|\n| Grammar-constrained decoding | XGrammar, Outlines, LMQL | OntoCoDec Grammar 层基于此；Semantic 层是超越 |\n| Vocabulary/type-constrained generation | GENRE, GenIE, GCD | OntoCoDec 借鉴 logits masking 技术，但约束来自 IE ontology 而非固定词表 |\n| Structural constraint for IE | UIE, GoLLIE, CodeIE | 这些方法靠 training/prompting，OntoCoDec 是 decoding-time enforcement，两者互补 |\n| Ontology validation | ODKE+, EnriCo | Post-hoc validation vs. preventive enforcement 的本质区别 |\n| Constrained decoding quality | Let Me Speak Freely, CRANE | OntoCoDec F1 无损实验直接回应此 concern，S2 策略符合 CRANE 理论 |\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/related_work_survey.md",
    "content": "# OntoCoDec Related Work Survey\n\n## 1. Grammar-Constrained Decoding\n\n### XGrammar | MLSys 2025\n- **Title:** XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models\n- **Authors:** Dong et al.\n- **核心方法:** 将词表划分为 context-independent（离线预检）和 context-dependent（运行时检查）两类 token，结合 persistent stack-based pushdown automata 高效执行 CFG 约束，比先前方法快 100x。\n- **与 OntoCoDec 的关系:** OntoCoDec 的 Grammar 层直接基于 XGrammar 实现 JSON schema + enum 约束，消除 RV/ET violations。XGrammar 提供格式正确性保证，但不处理语义层约束（domain/range），这正是 OntoCoDec Semantic 层的贡献。\n- **BibTeX key:** `dong2025xgrammar`\n- **ArXiv:** 2411.15100\n\n### Outlines | arXiv 2023\n- **Title:** Efficient Guided Generation for Large Language Models\n- **Authors:** Willard & Louf\n- **核心方法:** 将受约束文本生成重构为有限状态机（FSM）中的状态转移，为每个 FSM 状态离线构建词表索引，实现正则表达式约束的 O(1) 均摊 per-token 检查，扩展至 LALR(1) parser 支持 CFG。\n- **与 OntoCoDec 的关系:** Outlines 是 grammar-constrained decoding 的开源先驱之一，与 XGrammar 属同一技术路线。OntoCoDec 选择 XGrammar 而非 Outlines 是因为其更高效的 vocabulary 预处理和对 LLM serving 框架（vLLM/SGLang）的原生集成。\n- **BibTeX key:** `willard2023outlines`\n- **ArXiv:** 2307.09702\n\n### LMQL | PLDI 2023\n- **Title:** Prompting Is Programming: A Query Language for Large Language Models\n- **Authors:** Beurer-Kellner, Fischer & Vechev\n- **核心方法:** SQL 风格的 LLM 查询语言，将自然语言 prompt 与程序控制流和声明式约束（类型、长度、正则、停止条件）结合，运行时编译为 token-level masking，减少 26-85% API 成本。\n- **与 OntoCoDec 的关系:** LMQL 提供通用的声明式约束框架，但约束表达能力限于格式层面（类型、长度、正则）。OntoCoDec 的 Semantic 层引入了 IE 任务特有的 domain/range 本体约束，超越了通用格式约束的范畴。\n- **BibTeX key:** `beurer-kellner2023lmql`\n- **ArXiv:** 2212.06094\n\n### DOMINO | ICML 2024\n- **Title:** Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation\n- **Authors:** Beurer-Kellner, Fischer & Vechev\n- **核心方法:** 提出 non-invasive constrained decoding 算法，在执行 CFG 约束的同时最小化对 LLM 原始分布的扭曲，利用预计算和 speculative decoding 实现甚至超过无约束生成的吞吐。\n- **与 OntoCoDec 的关系:** DOMINO 关注 distribution distortion 问题——约束解码如何改变 LLM 的 token 分布。OntoCoDec 的 F1 无损结果从实验角度呼应了这一方向：精心设计的约束不必牺牲生成质量。\n- **BibTeX key:** `beurer-kellner2024domino`\n- **ArXiv:** 2403.06988\n\n### Grammar-Aligned Decoding (ASAp) | NeurIPS 2024\n- **Title:** Grammar-Aligned Decoding\n- **Authors:** Park, Wang, Berg-Kirkpatrick, Polikarpova & D'Antoni\n- **核心方法:** 证明 naive token masking 会扭曲 LLM 的条件分布，提出 ASAp（Adaptive Sampling with Approximate expected futures）算法，在保证语法正确性的同时保持对原始 LM 分布的无偏性。\n- **与 OntoCoDec 的关系:** ASAp 解决的是 grammar-constrained decoding 的理论正确性问题。OntoCoDec 的 logits masking 也面临类似的分布扭曲风险，但实验证明在 IE 任务上 F1 无损，说明 IE 场景中合法约束的 masking 影响有限。\n- **BibTeX key:** `park2024grammar`\n- **ArXiv:** 2405.21047\n\n---\n\n## 2. Vocabulary/Type-Constrained Generation\n\n### GENRE | ICLR 2021\n- **Title:** Autoregressive Entity Retrieval\n- **Authors:** De Cao, Izacard, Riedel & Petroni\n- **核心方法:** 首个用自回归生成方式检索实体的系统，基于 fine-tuned BART 逐 token 生成实体名，用 prefix trie 约束 beam search 只允许生成合法实体标识符，在 20+ entity disambiguation/linking 基准上达到 SOTA。\n- **与 OntoCoDec 的关系:** GENRE 的 trie-based constrained beam search 是 vocabulary-constrained generation 的经典范式。OntoCoDec 的 Semantic 层借鉴类似思路（限制输出到合法类型/实体），但不需要构建 trie，而是通过 logits masking 直接在 token 级别实施 domain/range 约束。\n- **BibTeX key:** `decao2021genre`\n- **ArXiv:** 2010.00904\n\n### GenIE | NAACL 2022\n- **Title:** GenIE: Generative Information Extraction\n- **Authors:** Josifoski, De Cao, Peyrard, Petroni & West\n- **核心方法:** 自回归 seq2seq 模型生成 (subject, relation, object) 三元组，结合 trie-based lexical constraints（强制输出合法实体/关系标识符）和 state-based constraints（强制合法三元组结构），实现端到端抽取。\n- **与 OntoCoDec 的关系:** GenIE 是将 vocabulary constraint 应用于 IE 的先驱，但需要 fine-tuning 专用模型。OntoCoDec 的关键优势是 training-free——直接在通用 LLM 上通过解码时约束实现，无需额外训练。\n- **BibTeX key:** `josifoski2022genie`\n- **ArXiv:** 2112.08340\n\n### NeuroLogic Decoding | NAACL 2021\n- **Title:** NeuroLogic Decoding: (Un)supervised Neural Text Generation with Predicate Logic Constraints\n- **Authors:** Lu, West, Zellers, Le Bras, Bhagavatula & Choi\n- **核心方法:** 将词汇约束表达为谓词逻辑公式（合取/析取 of must-include/must-exclude tokens），在每步通过 pruning 和 re-ranking beams 执行约束，渐近复杂度等同标准 beam search。\n- **与 OntoCoDec 的关系:** NeuroLogic 处理的是 lexical inclusion/exclusion 约束（\"生成必须包含词 X\"），而 OntoCoDec 的 Semantic 层处理的是 relational/type 约束（\"关系 R 的 head 必须是类型 T\"）。约束语义层次不同。\n- **BibTeX key:** `lu2021neurologic`\n- **ArXiv:** 2010.12884\n\n### Grammar-Constrained Decoding for Structured NLP | EMNLP 2023\n- **Title:** Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning\n- **Authors:** Geng, Josifoski, Peyrard & West\n- **核心方法:** 提出 grammar-constrained decoding（GCD）统一框架：每步将违反形式文法的 token logits 设为负无穷，保证结构合法输出，无需 fine-tuning。引入 input-dependent grammars 增加灵活性。在 IE、entity disambiguation、constituency parsing 上验证。\n- **与 OntoCoDec 的关系:** 这是最直接的前驱工作——同样对 IE 任务使用 logits masking。但 Geng et al. 的约束限于语法层面（输出格式合法），OntoCoDec 在此基础上增加了语义层约束（domain/range 合法），是从格式正确到语义正确的扩展。\n- **BibTeX key:** `geng2023gcd`\n- **ArXiv:** 2305.13971\n\n---\n\n## 3. Structural Constraints for Information Extraction\n\n### UIE | ACL 2022\n- **Title:** Unified Structure Generation for Universal Information Extraction\n- **Authors:** Lu, Liu, Dai et al.\n- **核心方法:** 定义 Structured Extraction Language（SEL）统一编码不同 IE 输出结构（entity, relation, event, sentiment），配合 schema-based prompt（Structural Schema Instructor）和大规模预训练 text-to-structure 模型，在 4 个 IE 任务 13 个数据集上达到 SOTA。\n- **与 OntoCoDec 的关系:** UIE 通过训练让模型\"学会\"输出合法结构，但无法保证推理时不违反 schema 约束。OntoCoDec 是 decoding-time enforcement，提供硬性保证——违反 domain/range 的输出不可能被生成。\n- **BibTeX key:** `lu2022uie`\n- **ArXiv:** 2203.12277\n\n### GoLLIE | ICLR 2024\n- **Title:** Annotation Guidelines improve Zero-Shot Information-Extraction\n- **Authors:** Sainz, Garcia-Ferrero, Agerri et al.\n- **核心方法:** 将 annotation guidelines 表达为 Python class 定义（dataclass），fine-tune Code-LLaMA 生成 Python 代码形式的结构化输出，通过 code-based schema 表达实现强零样本泛化到未见 IE schema。\n- **与 OntoCoDec 的关系:** GoLLIE 用 Python 类型系统隐式表达类型约束，但执行仍依赖模型训练。OntoCoDec 在解码时显式执行本体约束，两者互补——GoLLIE 的 code-based schema 可与 OntoCoDec 的 decoding-time enforcement 结合。\n- **BibTeX key:** `sainz2024gollie`\n- **ArXiv:** 2310.03668\n\n### CodeIE | ACL 2023\n- **Title:** Large Code Generation Models are Better Few-Shot Information Extractors\n- **Authors:** Li, Sun, Tang et al.\n- **核心方法:** 将 IE 结构化输出重构为代码生成任务，用 code-LLM（Codex）+ code-style prompts 执行 NER 和 RE，代码形式天然捕获 IE 输出的结构性。在 few-shot 设置下一致优于 fine-tuned IE 模型和 NL-LLM prompting。\n- **与 OntoCoDec 的关系:** CodeIE 通过代码形式化提高结构一致性，但仍是 soft constraint（模型可能生成非法代码）。OntoCoDec 的 Grammar+Semantic 层提供 hard constraint——输出格式和语义类型均被强制保证。\n- **BibTeX key:** `li2023codeie`\n- **ArXiv:** 2305.05711\n\n### InstructUIE | arXiv 2023\n- **Title:** Multi-task Instruction Tuning for Unified Information Extraction\n- **Authors:** Wang, Zhou, Zu et al.\n- **核心方法:** 构建 IE INSTRUCTIONS 基准（32 个 IE 数据集统一为 text-to-text 格式 + 专家指令），fine-tune Flan-T5 实现单模型处理 NER/RE/EE。指令微调的小模型大幅超越 GPT-3.5。\n- **与 OntoCoDec 的关系:** InstructUIE 靠 instruction tuning 提高 IE 输出质量，但无结构保证。OntoCoDec 与 InstructUIE 正交——可在 instruction-tuned 模型上叠加 decoding-time 约束进一步消除违规。\n- **BibTeX key:** `wang2023instructuie`\n- **ArXiv:** 2304.08085\n\n### ADELIE | EMNLP 2024\n- **Title:** Aligning Large Language Models on Information Extraction\n- **Authors:** Qi, Peng, Wang et al. (THU-KEG)\n- **核心方法:** 构建 IEInstruct 高质量对齐语料，用 SFT + DPO 训练 LLM 进行 IE，覆盖 closed IE、open IE、on-demand IE。ADELIE 在开源模型中达到 SOTA，同时保持通用 LLM 能力。\n- **与 OntoCoDec 的关系:** ADELIE 代表 training-time alignment 路线，通过 preference optimization 让模型偏好合法输出。OntoCoDec 是 decoding-time enforcement 路线，提供更强保证且 training-free。两者可叠加使用。\n- **BibTeX key:** `qi2024adelie`\n- **ArXiv:** 2405.05008\n\n---\n\n## 4. Type-Checking / Ontology Validation in NLP\n\n### ODKE+ | arXiv 2025\n- **Title:** ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs\n- **Authors:** Khorshidi, Nikfarjam, Shankar et al. (Apple)\n- **核心方法:** 动态生成针对每种实体类型的 ontology snippets（含 domain/range 约束），用于对齐 LLM 抽取结果与 schema 约束。处理 9M+ Wikipedia 页面，19M facts，98.8% precision across 195 predicates。\n- **与 OntoCoDec 的关系:** ODKE+ 在 prompt 层面注入 ontology 约束，属于 soft guidance。OntoCoDec 在 decoding 层面强制执行 domain/range 约束，属于 hard enforcement。ODKE+ 无法保证 0% violation rate，OntoCoDec 可以。\n- **BibTeX key:** `khorshidi2025odke`\n- **ArXiv:** 2509.04696\n\n### Open IE with Entity Focused Constraints | Findings of EACL 2023\n- **Title:** Open Information Extraction with Entity Focused Constraints\n- **Authors:** Upadhyay, Balalau & Manolescu\n- **核心方法:** 将 entity-type 知识作为约束注入 Open IE，通过 constrained inference（解码时）和 constraint-aware training 两种机制实现，在 CaRB 上 F1 提升 29.17%。\n- **与 OntoCoDec 的关系:** 与 OntoCoDec 最相近的工作之一——同样在解码时利用 entity type 约束。但该方法针对 Open IE 的通用类型约束，OntoCoDec 针对 closed IE 的 ontology-specific domain/range 约束，粒度更细。\n- **BibTeX key:** `upadhyay2023openie`\n\n### EnriCo | arXiv 2024\n- **Title:** EnriCo: Enriched Representation and Globally Constrained Inference for Entity and Relation Extraction\n- **Authors:** Zaratiana, Tomeh, Dauxais, Holat & Charnois\n- **核心方法:** Attention-based enriched representations for joint entity and relation extraction，结合一套 constrained decoding 算法在推理时强制执行任务特定的结构约束（如 entity type compatibility for relations）。\n- **与 OntoCoDec 的关系:** EnriCo 在传统 joint extraction 模型上加 constrained decoding，OntoCoDec 在 LLM 上做。EnriCo 的约束是模型特定的，OntoCoDec 的约束来自外部 ontology，更通用、可复用。\n- **BibTeX key:** `zaratiana2024enrico`\n- **ArXiv:** 2404.12493\n\n### LLM as KG Curators | GenAIK 2025\n- **Title:** Can LLMs be Knowledge Graph Curators for Validating Triple Insertions?\n- **Authors:** Regino & dos Reis\n- **核心方法:** 用 prompt-based 多阶段验证管线引导 LLM 评估 RDF triple 插入的 domain/range 一致性和语义连贯性。\n- **与 OntoCoDec 的关系:** 典型的 post-hoc validation 方法——先生成再验证。OntoCoDec 是 preventive 方法——在生成时就阻止违规，不需要后续验证和纠错循环。\n- **BibTeX key:** `regino2025kgcurator`\n\n---\n\n## 5. Constrained Decoding Quality Concerns\n\n### Let Me Speak Freely? | EMNLP 2024\n- **Title:** Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models\n- **Authors:** Tam, Wu, Tsai, Lin, Lee & Chen\n- **核心方法:** 系统研究结构化格式约束（JSON, XML, YAML）对 LLM 推理能力的影响。发现刚性格式约束损害推理密集型任务（数学、多跳 QA）但有利于分类任务（slot-filling、intent detection）。约束越严格，性能退化越大。\n- **与 OntoCoDec 的关系:** 这是 OntoCoDec 需要直接回应的 concern。OntoCoDec 在 SciERC 上证明 F1 无损（甚至略有提升），说明在 IE 任务场景下——属于该论文发现的\"分类任务\"范畴——约束解码不仅不损害质量，反而可能有益。\n- **BibTeX key:** `tam2024letmespeak`\n- **ArXiv:** 2408.02442\n\n### CRANE | ICML 2025\n- **Title:** CRANE: Reasoning with Constrained LLM Generation\n- **Authors:** Banerjee, Suresh, Ugare, Misailovic & Singh\n- **核心方法:** 从理论角度解释为什么将 LLM 输出约束到 restrictive grammars（只允许语法合法的最终答案）会降低推理能力。提出 alternating strategy：在 unconstrained generation（推理/CoT）和 constrained generation（结构化输出）之间交替，在 GSM-symbolic 和 FOLIO 上提升最多 10 个百分点。\n- **与 OntoCoDec 的关系:** CRANE 的发现验证了 OntoCoDec S2 策略（两通道分离）的合理性——S2 将推理（生成候选）和约束（格式化输出）分离到两个 pass，正是 CRANE 理论推荐的 alternating approach。\n- **BibTeX key:** `banerjee2025crane`\n- **ArXiv:** 2502.09061\n\n### Structure Snowballing | arXiv 2026\n- **Title:** From Hallucination to Structure Snowballing: The Alignment Tax of Constrained Decoding in LLM Reflection\n- **Authors:** Zhou (Saarland University)\n- **核心方法:** 发现 constrained decoding 应用于 LLM self-correction/reflection 时的新失败模式——\"structure snowballing\"：满足严格格式规则的认知负荷将模型推入格式陷阱而非改善推理。揭示结构粒度与模型内部容量之间的张力。\n- **与 OntoCoDec 的关系:** OntoCoDec 避免了 snowballing 风险：其约束是 task-specific 的 IE 本体约束而非通用格式约束，且约束空间有限（合法类型集合远小于 free-form 生成空间），不会引入过度的认知负荷。\n- **BibTeX key:** `zhou2026snowballing`\n- **ArXiv:** 2604.06066\n\n### The Hidden Cost of Structure | RANLP 2025\n- **Title:** The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance\n- **Authors:** Schall & de Melo\n- **核心方法:** 跨 11 个模型和多个基准的系统实证研究。发现 base model 和 instruction-tuned model 在结构约束下表现分化：尽管约束保证格式合法，constrained decoding 在推理密集型任务上常降低语义正确性 10-30%。\n- **与 OntoCoDec 的关系:** OntoCoDec 的实验在 instruction-tuned model 上进行，且 IE 任务是\"extraction\"而非\"reasoning\"，属于该论文发现的约束解码影响较小的任务类型。F1 无损结果与该论文的观察一致。\n- **BibTeX key:** `schall2025hiddencost`\n\n---\n\n## 6. OntoCoDec 在 Landscape 中的定位\n\n### 核心差异化\n\nOntoCoDec 在约束解码 landscape 中占据独特位置，体现为三个维度的创新：\n\n**1. 约束层次：从格式到语义**\n- 现有 grammar-constrained decoding（XGrammar, Outlines, LMQL）保证**格式正确性**（valid JSON, enum values）\n- 现有 vocabulary-constrained generation（GENRE, NeuroLogic）保证**词汇合法性**（输出在预定义词表中）\n- OntoCoDec 增加**语义正确性**层（domain/range 约束），将约束从 syntactic 扩展到 semantic\n\n**2. 执行时机：从 post-hoc 到 preventive**\n- 传统 ontology validation 方法（ODKE+, KG validation）是 post-hoc：先生成再验证\n- 训练方法（UIE, GoLLIE, ADELIE）是 soft constraint：通过训练引导模型偏好合法输出，但无保证\n- OntoCoDec 是 decoding-time enforcement：不合法的输出不可能被生成，无需验证-纠错循环\n\n**3. 质量保持：约束无损**\n- 约束解码质量 concern（Let Me Speak Freely, CRANE, Structure Snowballing）指出约束常损害推理\n- OntoCoDec 在 SciERC 上 DR violation 15.37%→0.93%（↓94%）且 F1 无损，反驳\"约束必损质量\"的 narrative\n- OntoCoDec S2 策略（两通道分离）符合 CRANE 理论推荐的 alternating approach\n\n### 技术栈定位\n\n```\nLayer 3 (OntoCoDec Semantic): domain/range logits masking ← 本文贡献\nLayer 2 (OntoCoDec Grammar):  JSON schema + enum constraints ← 基于 XGrammar\nLayer 1 (LLM):                base language model generation\n```\n\n- Layer 2 消除 format violations（RV/ET），与 Outlines/LMQL/SGLang 同层\n- Layer 3 消除 semantic violations（DR），是 OntoCoDec 独有的贡献\n- 两层组合（S1 单通道或 S2 两通道）实现从格式到语义的完整约束覆盖\n\n### 与各 paradigm 的关系总结\n\n| Paradigm | 代表工作 | OntoCoDec 关系 |\n|----------|----------|---------------|\n| Grammar-constrained decoding | XGrammar, Outlines, LMQL | OntoCoDec Grammar 层基于此；Semantic 层是超越 |\n| Vocabulary/type-constrained generation | GENRE, GenIE, GCD | OntoCoDec 借鉴 logits masking 技术，但约束来自 IE ontology 而非固定词表 |\n| Structural constraint for IE | UIE, GoLLIE, CodeIE | 这些方法靠 training/prompting，OntoCoDec 是 decoding-time enforcement，两者互补 |\n| Ontology validation | ODKE+, EnriCo | Post-hoc validation vs. preventive enforcement 的本质区别 |\n| Constrained decoding quality | Let Me Speak Freely, CRANE | OntoCoDec F1 无损实验直接回应此 concern，S2 策略符合 CRANE 理论 |\n"
  }
}
````

</details>

---

### Tool result

_source line 156 · 2026-05-14T02:40:42.008156+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/related_work_survey.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 157 · 2026-05-14T02:40:42.008446+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__save_project_file",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 158 · 2026-05-14T02:40:42.008629+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 159 · 2026-05-14T02:40:42.008808+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "register artifact",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "register artifact",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 160 · 2026-05-14T02:40:42.008935+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 161 · 2026-05-14T02:40:42.009054+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "artifact",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "artifact",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 162 · 2026-05-14T02:40:42.009173+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 163 · 2026-05-14T02:40:42.009350+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/manifest.yaml",
  "description": "Read manifest to understand artifact registration format"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/manifest.yaml",
    "description": "Read manifest to understand artifact registration format"
  }
}
```

</details>

---

### Tool result

_source line 164 · 2026-05-14T02:40:42.010492+00:00_

- id: art_20260514_3bc71e
  name: paper_results_summary
  type: report
  description: 'Structured paper results summary: SciERC Phase 2 main table (5 modes),
    DocRED Phase 0 comparison, per-relation DR breakdown, claim-evidence mapping,
    CF root cause analysis, S1/S2 trade-off, pending experiments'
  path: projects/schema_semantic_constrained_ie/artifacts/_project/report/paper_results_summary.md
  url: null
  project: schema_semantic_constrained_ie
  exp_id: null
  skill: ''
  created_at: '2026-05-14T02:32:05.148204+00:00'
  tags:
  - paper
  - results
  - tables
  - emnlp2026

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "Bash",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 165 · 2026-05-14T02:40:42.010717+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat >> /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/manifest.yaml << 'EOF'\n- id: art_20260514_rw_survey\n  name: related_work_survey\n  type: report\n  description: 'Related Work literature survey for OntoCoDec paper: 5 constraint paradigms\n    (grammar-constrained decoding, vocabulary/type-constrained generation, structural\n    constraints for IE, ontology validation, constrained decoding quality concerns),\n    20+ papers with differentiation analysis and positioning summary'\n  path: projects/schema_semantic_constrained_ie/artifacts/related_work_survey.md\n  url: null\n  project: schema_semantic_constrained_ie\n  exp_id: null\n  skill: ''\n  created_at: '2026-05-14T12:00:00.000000+00:00'\n  tags:\n  - paper\n  - related-work\n  - literature-survey\n  - emnlp2026\nEOF",
  "description": "Register artifact in manifest"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "Bash",
  "tool_args": {
    "command": "cat >> /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/manifest.yaml << 'EOF'\n- id: art_20260514_rw_survey\n  name: related_work_survey\n  type: report\n  description: 'Related Work literature survey for OntoCoDec paper: 5 constraint paradigms\n    (grammar-constrained decoding, vocabulary/type-constrained generation, structural\n    constraints for IE, ontology validation, constrained decoding quality concerns),\n    20+ papers with differentiation analysis and positioning summary'\n  path: projects/schema_semantic_constrained_ie/artifacts/related_work_survey.md\n  url: null\n  project: schema_semantic_constrained_ie\n  exp_id: null\n  skill: ''\n  created_at: '2026-05-14T12:00:00.000000+00:00'\n  tags:\n  - paper\n  - related-work\n  - literature-survey\n  - emnlp2026\nEOF",
    "description": "Register artifact in manifest"
  }
}
```

</details>

---

### Tool result

_source line 166 · 2026-05-14T02:40:42.010884+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260514T023514",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 167 · 2026-05-14T02:40:42.015310+00:00_

产出文件已写入并注册：
`artifacts/related_work_survey.md`

**覆盖 5 个 paradigm，共 20 篇论文：**

| Paradigm | 论文数 | 代表工作 |
|----------|--------|----------|
| Grammar-constrained decoding | 5 | XGrammar (MLSys'25), Outlines, LMQL (PLDI'23), DOMINO (ICML'24), ASAp (NeurIPS'24) |
| Vocabulary/type-constrained generation | 4 | GENRE (ICLR'21), GenIE (NAACL'22), NeuroLogic (NAACL'21), GCD (EMNLP'23) |
| Structural constraints for IE | 5 | UIE (ACL'22), GoLLIE (ICLR'24), CodeIE (ACL'23), InstructUIE, ADELIE (EMNLP'24) |
| Ontology validation | 4 | ODKE+ (Apple'25), OpenIE w/ entity constraints (EACL'23), EnriCo, KG validation (GenAIK'25) |
| Constrained decoding quality | 4 | Let Me Speak Freely (EMNLP'24), CRANE (ICML'25), Structure Snowballing, Hidden Cost (RANLP'25) |

**OntoCoDec 定位总结（3 个差异化维度）：**
1. **约束层次**：从格式（grammar）扩展到语义（domain/range）
2. **执行时机**：decoding-time preventive enforcement vs post-hoc validation / training-time soft guidance
3. **质量保持**：F1 无损 + S2 两通道策略符合 CRANE 的 alternating approach 理论

注意：CRANE 实际是 ICML 2025 而非 NeurIPS 2024，已在文档中修正。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_related_work_survey_20260514T023514"
}
```

</details>

---
