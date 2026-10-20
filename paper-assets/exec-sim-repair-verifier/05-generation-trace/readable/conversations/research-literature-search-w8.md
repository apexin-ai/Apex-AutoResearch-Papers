# research literature search w8

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 81
- **Recorded user turns:** 0
- **Tool calls:** 40
- **Original source:** `logs/chats/worker_research_literature-search-w8_20260519T090952.jsonl`
- **Structured JSON:** [`bfe5b14143071a725e4a.json`](../../sessions/bf/bfe5b14143071a725e4a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

81 recorded events

### Tool call

_source line 1 · 2026-05-19T09:12:17.524867+00:00_

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
  "session": "worker_research_literature-search-w8_20260519T090952",
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

_source line 2 · 2026-05-19T09:12:17.525355+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T09:12:17.525660+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Search CodePRM paper",
  "prompt": "Search for the paper \"CodePRM\" published at ACL 2025 Findings, about process-level verification for code generation. I need:\n1. Full title\n2. Complete author list\n3. Venue details (ACL 2025 Findings)\n4. Any available page numbers or DOI\n5. If it's on arXiv, the arXiv ID\n\nUse WebSearch with query \"CodePRM process-level verification code generation ACL 2025\" and also try \"CodePRM ACL 2025 Findings\". Report all details you find.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "Agent",
  "tool_args": {
    "description": "Search CodePRM paper",
    "prompt": "Search for the paper \"CodePRM\" published at ACL 2025 Findings, about process-level verification for code generation. I need:\n1. Full title\n2. Complete author list\n3. Venue details (ACL 2025 Findings)\n4. Any available page numbers or DOI\n5. If it's on arXiv, the arXiv ID\n\nUse WebSearch with query \"CodePRM process-level verification code generation ACL 2025\" and also try \"CodePRM ACL 2025 Findings\". Report all details you find.",
    "subagent_type": "general-purpose"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-19T09:12:17.525974+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Search FunPRM paper",
  "prompt": "Search for the paper with arXiv ID 2601.22249, called \"FunPRM\" about function-as-step process reward model. I need:\n1. Full title\n2. Complete author list\n3. Year (2026 or 2025)\n4. arXiv details\n\nUse WebSearch with queries like \"arxiv 2601.22249 FunPRM\" and \"FunPRM function-as-step PRM code\". Report all details you find.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "Agent",
  "tool_args": {
    "description": "Search FunPRM paper",
    "prompt": "Search for the paper with arXiv ID 2601.22249, called \"FunPRM\" about function-as-step process reward model. I need:\n1. Full title\n2. Complete author list\n3. Year (2026 or 2025)\n4. arXiv details\n\nUse WebSearch with queries like \"arxiv 2601.22249 FunPRM\" and \"FunPRM function-as-step PRM code\". Report all details you find.",
    "subagent_type": "general-purpose"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T09:12:17.526252+00:00_

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
  "session": "worker_research_literature-search-w8_20260519T090952",
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

_source line 6 · 2026-05-19T09:12:17.526482+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T09:12:17.526702+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Search Willard Louf 2023",
  "prompt": "Search for a paper by Willard and Louf from 2023 about constrained decoding or structured output generation, possibly related to a tool called \"Outlines\". I need:\n1. Full title\n2. Complete author list\n3. Venue (conference, journal, or arXiv)\n4. Year\n5. Any arXiv ID or DOI\n\nUse WebSearch with queries like \"Willard Louf 2023 constrained decoding outlines\" and \"Willard Louf efficient guided generation language models\". Report all details you find.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "Agent",
  "tool_args": {
    "description": "Search Willard Louf 2023",
    "prompt": "Search for a paper by Willard and Louf from 2023 about constrained decoding or structured output generation, possibly related to a tool called \"Outlines\". I need:\n1. Full title\n2. Complete author list\n3. Venue (conference, journal, or arXiv)\n4. Year\n5. Any arXiv ID or DOI\n\nUse WebSearch with queries like \"Willard Louf 2023 constrained decoding outlines\" and \"Willard Louf efficient guided generation language models\". Report all details you find.",
    "subagent_type": "general-purpose"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-19T09:12:17.526994+00:00_

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
  "session": "worker_research_literature-search-w8_20260519T090952",
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

_source line 9 · 2026-05-19T09:12:17.527216+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-19T09:12:17.527432+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Search CodeScaler paper",
  "prompt": "Search for the paper with arXiv ID 2602.17684, possibly called \"CodeScaler\" from 2026. I need:\n1. Full title\n2. Complete author list\n3. Year\n4. arXiv details and abstract summary\n\nUse WebSearch with queries like \"arxiv 2602.17684\" and \"CodeScaler arxiv 2026\". Report all details you find.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "Agent",
  "tool_args": {
    "description": "Search CodeScaler paper",
    "prompt": "Search for the paper with arXiv ID 2602.17684, possibly called \"CodeScaler\" from 2026. I need:\n1. Full title\n2. Complete author list\n3. Year\n4. arXiv details and abstract summary\n\nUse WebSearch with queries like \"arxiv 2602.17684\" and \"CodeScaler arxiv 2026\". Report all details you find.",
    "subagent_type": "general-purpose"
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T09:12:17.527707+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CodePRM process-level verification code generation ACL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CodePRM process-level verification code generation ACL 2025"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-19T09:12:17.527980+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CodePRM ACL 2025 Findings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CodePRM ACL 2025 Findings"
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T09:12:17.528210+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Search CodeRL+ paper",
  "prompt": "Search for the paper with arXiv ID 2510.18471, possibly called \"CodeRL+\" from 2025, likely about reinforcement learning for code generation. I need:\n1. Full title\n2. Complete author list\n3. Year\n4. arXiv details and abstract summary\n\nUse WebSearch with queries like \"arxiv 2510.18471\" and \"CodeRL+ arxiv 2025\". Report all details you find.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "Agent",
  "tool_args": {
    "description": "Search CodeRL+ paper",
    "prompt": "Search for the paper with arXiv ID 2510.18471, possibly called \"CodeRL+\" from 2025, likely about reinforcement learning for code generation. I need:\n1. Full title\n2. Complete author list\n3. Year\n4. arXiv details and abstract summary\n\nUse WebSearch with queries like \"arxiv 2510.18471\" and \"CodeRL+ arxiv 2025\". Report all details you find.",
    "subagent_type": "general-purpose"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-19T09:12:17.528545+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2601.22249 FunPRM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2601.22249 FunPRM"
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T09:12:17.528775+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "FunPRM function-as-step process reward model paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "WebSearch",
  "tool_args": {
    "query": "FunPRM function-as-step process reward model paper"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-19T09:12:17.529035+00:00_

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
  "session": "worker_research_literature-search-w8_20260519T090952",
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

_source line 17 · 2026-05-19T09:12:17.529249+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-19T09:12:17.529457+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Willard Louf 2023 constrained decoding outlines efficient guided generation language models"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Willard Louf 2023 constrained decoding outlines efficient guided generation language models"
  }
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-19T09:12:17.529675+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Willard Louf \"outlines\" structured generation 2023 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Willard Louf \"outlines\" structured generation 2023 arXiv"
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-19T09:12:17.529921+00:00_

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
  "session": "worker_research_literature-search-w8_20260519T090952",
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

_source line 21 · 2026-05-19T09:12:17.530136+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-19T09:12:17.530347+00:00_

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
  "session": "worker_research_literature-search-w8_20260519T090952",
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

_source line 23 · 2026-05-19T09:12:17.530557+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-19T09:12:17.530767+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Search mutation-fault coupling",
  "prompt": "Search for the most important meta-analysis or comprehensive empirical studies on mutation testing and real fault coupling. Key researchers in this area include Andrews, Just, Papadakis. I need 1-2 of the most cited/comprehensive papers that establish the \"coupling hypothesis\" - that mutation testing effectiveness correlates with real fault detection.\n\nKey papers to look for:\n1. Andrews et al. \"Using Mutation Testing to Assess Test Suite Quality\" (possibly IEEE TSE)\n2. Just et al. \"Are Mutants a Valid Substitute for Real Faults in Software Testing?\" (FSE 2014?)\n3. Papadakis et al. mutation testing survey or meta-analysis\n\nUse WebSearch with queries like:\n- \"mutation testing real fault coupling meta-analysis empirical\"\n- \"Just mutants valid substitute real faults FSE 2014\"\n- \"Papadakis mutation testing survey\"\n- \"Andrews mutation analysis empirical study\"\n\nFor each paper found, report: full title, complete author list, venue, year, and any DOI. Focus on the 1-2 most comprehensive/cited ones.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "Agent",
  "tool_args": {
    "description": "Search mutation-fault coupling",
    "prompt": "Search for the most important meta-analysis or comprehensive empirical studies on mutation testing and real fault coupling. Key researchers in this area include Andrews, Just, Papadakis. I need 1-2 of the most cited/comprehensive papers that establish the \"coupling hypothesis\" - that mutation testing effectiveness correlates with real fault detection.\n\nKey papers to look for:\n1. Andrews et al. \"Using Mutation Testing to Assess Test Suite Quality\" (possibly IEEE TSE)\n2. Just et al. \"Are Mutants a Valid Substitute for Real Faults in Software Testing?\" (FSE 2014?)\n3. Papadakis et al. mutation testing survey or meta-analysis\n\nUse WebSearch with queries like:\n- \"mutation testing real fault coupling meta-analysis empirical\"\n- \"Just mutants valid substitute real faults FSE 2014\"\n- \"Papadakis mutation testing survey\"\n- \"Andrews mutation analysis empirical study\"\n\nFor each paper found, report: full title, complete author list, venue, year, and any DOI. Focus on the 1-2 most comprehensive/cited ones.",
    "subagent_type": "general-purpose"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-19T09:12:17.531092+00:00_

Web search results for query: "CodePRM process-level verification code generation ACL 2025"

Links: [{"title":"CodePRM: Execution Feedback-enhanced Process Reward Model for Code Generation - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.428/"},{"title":"Process-Supervised Reinforcement Learning for Code Generation - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.719/"},{"title":"CodeRL+: Improving Code Generation via Reinforcement with Execution Semantics Alignment","url":"https://arxiv.org/html/2510.18471v1"},{"title":"Accepted Findings Papers - ACL 2025","url":"https://2025.aclweb.org/program/find_papers/"},{"title":"SecCodePRM: A Process Reward Model for Code Security","url":"https://arxiv.org/pdf/2602.10418"},{"title":"FunPRM: Function-as-Step Process Reward Model with Meta Reward Correction for Code Generation","url":"https://arxiv.org/pdf/2601.22249"}]

Based on the search results, here's what I found about CodePRM:

## CodePRM: Execution Feedback-enhanced Process Reward Model for Code Generation

CodePRM is a paper presented at the ACL 2025 conference (in the Findings track) titled "Execution Feedback-enhanced Process Reward Model for Code Generation."

### Key Approach

During training, CodePRM trains a process reward model (PRM) to take both the reasoning process and code execution feedback as input to score individual thought steps, enabling it to leverage code execution results to distinguish between high-quality and low-quality thought steps.

### Inference Method

For inference, CodePRM develops a Generate-Verify-Refine (GVR) pipeline where the CodePRM serves as a process verifier to dynamically identify and correct errors in the thought process during code search.

### Performance

Experimental results demonstrate that CodePRM with the inference algorithm outperforms strong baselines, significantly enhancing code generation performance.

The paper was authored by Qingyao Li, Xinyi Dai, Xiangyang Li, Weinan Zhang, Yash
…[truncated 139 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-19T09:12:17.531382+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2602.17684"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2602.17684"
  }
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-19T09:12:17.531609+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CodeScaler arxiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CodeScaler arxiv 2026"
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-19T09:12:17.531859+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2510.18471"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2510.18471"
  }
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-19T09:12:17.532096+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CodeRL+ arxiv 2025 reinforcement learning code generation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CodeRL+ arxiv 2025 reinforcement learning code generation"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-19T09:12:17.532340+00:00_

Web search results for query: "CodePRM ACL 2025 Findings"

Links: [{"title":"CodePRM: Execution Feedback-enhanced Process Reward Model for Code Generation - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.428/"},{"title":"Accepted Findings Papers - ACL 2025","url":"https://2025.aclweb.org/program/find_papers/"},{"title":"Execution Feedback-enhanced Process Reward Model for ...","url":"https://aclanthology.org/2025.findings-acl.428.pdf"},{"title":"CodeRL+: Improving Code Generation via Reinforcement with Execution Semantics Alignment","url":"https://arxiv.org/html/2510.18471v1"},{"title":"ACL 2025 - Amazon Science","url":"https://www.amazon.science/conferences-and-events/acl-2025"},{"title":"Paper Digest: ACL 2025 Papers & Highlights – Paper Digest","url":"https://www.paperdigest.org/2025/07/acl-2025-papers-highlights/"}]

Based on the search results, here's what I found about CodePRM at ACL 2025 Findings:

CodePRM: Execution Feedback-enhanced Process Reward Model for Code Generation was published in Findings of the Association for Computational Linguistics: ACL 2025, pages 8169–8182, Vienna, Austria.

The paper was authored by Qingyao Li, Xinyi Dai, Xiangyang Li, Weinan Zhang, Yasheng Wang, Ruiming Tang, and Yong Yu.

**Research Overview:**

Code generation is a critical reasoning task for large language models, with recent advancements focusing on optimizing the thought process of code generation. However, such thought process lacks effective process supervision, making it hard to optimize the thoughts.

Although Process Reward Models (PRMs) have been widely established in mathematical reasoning, building a code PRM is still not trivial for the gap between thoughts to code.

**Methodology:**

The researchers collect data labeled with average pass rates via tree search to train an execution feedback-enhanced PRM. For evaluation, they integrate CodePRM into a Generate-Verify-Refine (GVR) pipeline, where it verifies and refines thought steps.


REMIND
…[truncated 94 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-19T09:12:17.532618+00:00_

Web search results for query: "arxiv 2601.22249 FunPRM"

Links: [{"title":"[2601.22249] FunPRM: Function-as-Step Process Reward Model with Meta Reward Correction for Code Generation","url":"https://arxiv.org/abs/2601.22249"},{"title":"(PDF) FunPRM: Function-as-Step Process Reward Model with Meta Reward Correction for Code Generation","url":"https://www.researchgate.net/publication/400340056_FunPRM_Function-as-Step_Process_Reward_Model_with_Meta_Reward_Correction_for_Code_Generation"},{"title":"FunPRM: Function-as-Step Process Reward Model with Meta Reward","url":"https://www.arxiv.org/pdf/2601.22249"},{"title":"FunPRM: Function-as-Step Process Reward Model with Meta Reward Correction for Code Generation","url":"https://arxiv.org/html/2601.22249"},{"title":"FunPRM: Function-as-Step Process Reward Model with Meta Reward Correction for Code Generation","url":"https://arxiv.org/pdf/2601.22249"}]

Based on the search results, here's information about arxiv paper 2601.22249:

## FunPRM: Function-as-Step Process Reward Model with Meta Reward Correction for Code Generation

Code generation is a core application of large language models (LLMs), yet LLMs still frequently fail on complex programming tasks. Given its success in mathematical reasoning, test-time scaling approaches such as Process Reward Model (PRM)-based Best-of-N selection offer a promising way to improve performance.

However, existing PRMs remain ineffective for code generation due to the lack of meaningful step decomposition in code and the noise of Monte Carlo-estimated partial-solution correctness scores (rewards).

FunPRM prompts LLMs to encourage modular code generation organized into functions, with functions treated as PRM reasoning steps. Additionally, FunPRM introduces a novel meta-learning-based reward correction mechanism that leverages clean final-solution rewards obtained via a unit-test-based evaluation system to purify noisy partial-solution rewards.

Experiments on LiveCodeBench and BigCodeBen
…[truncated 435 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-19T09:12:17.532915+00:00_

Web search results for query: "FunPRM function-as-step process reward model paper"

Links: [{"title":"FunPRM: Function-as-Step Process Reward Model with Meta Reward Correction for Code Generation","url":"https://arxiv.org/pdf/2601.22249"},{"title":"[2601.22249] FunPRM: Function-as-Step Process Reward Model with Meta Reward Correction for Code Generation","url":"https://arxiv.org/abs/2601.22249"},{"title":"FunPRM: Function-as-Step Process Reward Model with Meta Reward Correction for Code Generation","url":"https://arxiv.org/html/2601.22249v1"},{"title":"(PDF) FunPRM: Function-as-Step Process Reward Model with Meta Reward Correction for Code Generation","url":"https://www.researchgate.net/publication/400340056_FunPRM_Function-as-Step_Process_Reward_Model_with_Meta_Reward_Correction_for_Code_Generation"},{"title":"FunPRM: Function-as-Step Process Reward Model with Meta Reward","url":"https://www.arxiv.org/pdf/2601.22249"},{"title":"FunPRM: Function-as-Step Process Reward Model with ...","url":"https://chatpaper.com/chatpaper/paper/231379"}]

I found the paper! Here's what I discovered:

## FunPRM: Function-as-Step Process Reward Model

FunPRM is a process reward model that prompts LLMs to encourage modular code generation organized into functions, with functions treated as PRM reasoning steps.

**Key Problem Addressed:**
Existing PRMs remain ineffective for code generation due to the lack of meaningful step decomposition in code and the noise of Monte Carlo-estimated partial-solution correctness scores (rewards).

**Core Innovation:**
FunPRM prompts LLMs to generate modular code organized into multiple functions with accompanying docstrings, where these functions serve as reasoning steps for the process reward model while simultaneously improving code readability for human developers.

**Reward Correction Mechanism:**
FunPRM introduces a novel meta-learning-based reward correction mechanism that leverages clean final-solution rewards obtained via a unit-test-based eval
…[truncated 476 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-19T09:12:17.533185+00:00_

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
  "session": "worker_research_literature-search-w8_20260519T090952",
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

_source line 34 · 2026-05-19T09:12:17.533401+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-19T09:12:17.533633+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CodePRM arXiv \"Qingyao Li\" execution feedback process reward model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CodePRM arXiv \"Qingyao Li\" execution feedback process reward model"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-19T09:12:17.533893+00:00_

Web search results for query: "Willard Louf 2023 constrained decoding outlines efficient guided generation language models"

Links: [{"title":"[NLG] Outlines — Efficient Guided Generation for Large Language Models (Willard & Louf 2023) | by Youngrok Song | Medium","url":"https://id2thomas.medium.com/nlg-outlines-efficient-guided-generation-for-large-language-models-willard-louf-2023-3c9463543901"},{"title":"GitHub - dottxt-ai/outlines: Structured Outputs · GitHub","url":"https://github.com/dottxt-ai/outlines"},{"title":"[PDF] Efficient Guided Generation for Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Efficient-Guided-Generation-for-Large-Language-Willard-Louf/c4ceaef35bca063815f50d90a087acbd07a65478"},{"title":"Generating Structured Outputs from Language Models: Benchmark and Studies","url":"https://arxiv.org/html/2501.10868v1"},{"title":"Efficient Guided Generation for LLMs Brandon T. Willard1 and R´emi Louf2","url":"https://arxiv.org/pdf/2307.09702v1"},{"title":"Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation","url":"https://arxiv.org/html/2403.06988v1"},{"title":"Efficient Guided Generation for Large Language Models","url":"https://arxiv.org/pdf/2307.09702"},{"title":"Draft-Conditioned Constrained Decoding for Structured Generation in LLMs","url":"https://arxiv.org/pdf/2603.03305"},{"title":"Paper page - Efficient Guided Generation for Large Language Models","url":"https://huggingface.co/papers/2307.09702"}]

I found the research you're looking for! 

The paper is titled "Efficient Guided Generation for Large Language Models" by Brandon T. Willard and Rémi Louf, published in 2023 as arXiv preprint arXiv:2307.09702.

The paper presents an efficient method that guides language model text generation using regular expressions and context-free grammars with minimal overhead. The approach is model agnostic, allows one to enforce domain-specific knowledge and constraints, and enables the construction of re
…[truncated 536 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-19T09:12:17.534171+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2601.22249 FunPRM authors complete list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2601.22249 FunPRM authors complete list"
  }
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-19T09:12:17.534409+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:arxiv.org/abs/2601.22249 FunPRM authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:arxiv.org/abs/2601.22249 FunPRM authors"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-19T09:12:17.534649+00:00_

Web search results for query: "Willard Louf "outlines" structured generation 2023 arXiv"

Links: [{"title":"GitHub - dottxt-ai/outlines: Structured Outputs · GitHub","url":"https://github.com/dottxt-ai/outlines"},{"title":"[2307.09702] Efficient Guided Generation for Large Language Models","url":"https://ar5iv.labs.arxiv.org/html/2307.09702"},{"title":"Efficient Guided Generation for LLMs Brandon T. Willard1 and R´emi Louf2","url":"https://arxiv.org/pdf/2307.09702v1"},{"title":"Efficient Guided Generation for Large Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230709702W/abstract"},{"title":"[PDF] Efficient Guided Generation for Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Efficient-Guided-Generation-for-Large-Language-Willard-Louf/c4ceaef35bca063815f50d90a087acbd07a65478"},{"title":"AI-Powered Paper Summarization about the arXiv paper 2307.09702v3","url":"https://www.summarizepaper.com/en/arxiv-id/2307.09702v3/"},{"title":"XGrammar: Flexible and Efficient Structured Generation ...","url":"https://arxiv.org/pdf/2411.15100"},{"title":"Generating Structured Outputs from Language Models: Benchmark and Studies","url":"https://arxiv.org/html/2501.10868v1"},{"title":"[2307.09702] Efficient Guided Generation for Large Language Models","url":"https://arxiv.org/abs/2307.09702"},{"title":"Paper page - Efficient Guided Generation for Large Language Models","url":"https://huggingface.co/papers/2307.09702"}]

Based on the search results, I found the paper you're looking for. Brandon T. Willard and Rémi Louf published "Efficient Guided Generation for Large Language Models" on arXiv preprint arXiv:2307.09702 in 2023.

The paper shows how the problem of neural text generation can be reformulated in terms of transitions between states of a finite-state machine, which leads to an efficient approach to guiding text generation with regular expressions and context-free grammars by allowing construction of an index over
…[truncated 404 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-19T09:12:17.534976+00:00_

Web search results for query: "arxiv 2602.17684"

Links: [{"title":"[2602.17684] CodeScaler: Scaling Code LLM Training and Test-Time Inference via Execution-Free Reward Models","url":"https://arxiv.org/abs/2602.17684"},{"title":"Performance of o1 pro and GPT-4 in self-assessment questions for nephrology board renewal","url":"https://www.medrxiv.org/content/10.1101/2025.01.14.25320525.full.pdf"},{"title":"Machine Learning","url":"https://arxiv.org/list/cs.LG/recent?skip=651&show=50"},{"title":"The SARS-CoV-2 Omicron sub-variant BA.2.86 is attenuated in hamsters","url":"https://www.biorxiv.org/content/10.1101/2023.11.10.566576.full.pdf"},{"title":"IL10RB as a key regulator of COVID-19 host susceptibility and severity","url":"https://www.medrxiv.org/content/10.1101/2021.05.31.21254851.full.pdf"}]

Based on the search results, arxiv 2602.17684 is a paper titled "CodeScaler: Scaling Code LLM Training and Test-Time Inference via Execution-Free Reward Models" that proposes an execution-free reward model designed to scale both reinforcement learning training and test-time inference for code generation. The paper demonstrates that CodeScaler improves Qwen3-8B-Base by an average of +11.72 points across five coding benchmarks, outperforming binary execution-based RL by +1.82 points, and enables scalable reinforcement learning on synthetic datasets without any test cases. The authors are Xiao Zhu, Xinyu Zhou, Boyu Zhu, Hanxu Hu, Mingzhe Du, Haotian Zhang, Huiming Wang, and Zhijiang Guo.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-19T09:12:17.535247+00:00_

Web search results for query: "arxiv 2510.18471"

Links: [{"title":"[2510.18471] CodeRL+: Improving Code Generation via Reinforcement with Execution Semantics Alignment","url":"https://arxiv.org/abs/2510.18471"},{"title":"CodeRL+: Improving Code Generation via Reinforcement with Execution Semantics Alignment","url":"https://arxiv.org/html/2510.18471"},{"title":"Orchestrated multi agents sustain accuracy under clinical-scale workloads compared to a single agent","url":"https://www.medrxiv.org/content/10.1101/2025.08.22.25334049.full.pdf"},{"title":"Large Language Models for Detecting CONSORT Guideline Compliance in Published Randomized Clinical Trials: A Cross-Sectional Evaluation Study","url":"https://www.medrxiv.org/content/10.1101/2025.10.03.25337291.full.pdf"},{"title":"Assessing accuracy and legitimacy of multimodal large language models on Japan Diagnostic Radiology Board Examination","url":"https://www.medrxiv.org/content/10.1101/2025.06.23.25329534.full.pdf"},{"title":"Performance of reasoning large language models on nephrology multiple-choice questions","url":"https://www.medrxiv.org/content/10.64898/2025.12.03.25341427.full.pdf"},{"title":"Large language models identify causal genes in complex trait GWAS","url":"https://www.medrxiv.org/content/10.1101/2024.05.30.24308179.full.pdf"},{"title":"Development of meta-prompts for Large Language Models to screen titles and abstracts for diagnostic test accuracy reviews","url":"https://www.medrxiv.org/content/10.1101/2023.10.31.23297818.full.pdf"}]

Based on the search results, arxiv paper 2510.18471 is titled "CodeRL+: Improving Code Generation via Reinforcement with Execution Semantics Alignment." The paper proposes CodeRL+, an approach that integrates execution semantics alignment into the RLVR training pipeline for code generation, enabling the model to infer variable-level execution trajectory and providing a direct learning signal of execution semantics.

The paper addresses a fundamental semantic gap in Larg
…[truncated 661 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-19T09:12:17.535500+00:00_

Web search results for query: "arxiv 2601.22249 FunPRM authors complete list"

Links: [{"title":"[2601.22249] FunPRM: Function-as-Step Process Reward Model with Meta Reward Correction for Code Generation","url":"https://arxiv.org/abs/2601.22249"},{"title":"(PDF) FunPRM: Function-as-Step Process Reward Model with Meta Reward Correction for Code Generation","url":"https://www.researchgate.net/publication/400340056_FunPRM_Function-as-Step_Process_Reward_Model_with_Meta_Reward_Correction_for_Code_Generation"},{"title":"FunPRM: Function-as-Step Process Reward Model with Meta Reward","url":"https://www.arxiv.org/pdf/2601.22249"},{"title":"FunPRM: Function-as-Step Process Reward Model with Meta Reward Correction for Code Generation","url":"https://arxiv.org/html/2601.22249"},{"title":"FunPRM: Function-as-Step Process Reward Model with Meta Reward Correction for Code Generation","url":"https://arxiv.org/pdf/2601.22249"}]

The authors of the FunPRM paper (arxiv 2601.22249) are Ruiyi Zhang, Peijia Qin, Qi Cao, Eric Xue, and Pengtao Xie.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-19T09:12:17.535772+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Just et al \"Are Mutants a Valid Substitute for Real Faults in Software Testing\" FSE 2014"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Just et al \"Are Mutants a Valid Substitute for Real Faults in Software Testing\" FSE 2014"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-19T09:12:17.536026+00:00_

Web search results for query: "CodeScaler arxiv 2026"

Links: [{"title":"From articles to code: on-demand generation of core algorithms from scientific publications","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12857569/"},{"title":"Scaling Laws for Code: A More Data-Hungry Regime","url":"https://arxiv.org/pdf/2510.08702"},{"title":"Beyond Quantity: Trajectory Diversity Scaling for Code Agents","url":"https://arxiv.org/pdf/2602.03219"},{"title":"Exploring Representation-Level Augmentation for Code Search","url":"https://arxiv.org/pdf/2210.12285"},{"title":"CodeChemist: Functional Knowledge Transfer for Low-Resource Code Generation via Test-Time Scaling","url":"https://arxiv.org/pdf/2510.00501"},{"title":"Practical Code RAG at Scale: Task-Aware Retrieval Design Choices under Compute Budgets","url":"https://arxiv.org/pdf/2510.20609"}]

The search results don't appear to contain a paper specifically titled "CodeScaler" from arXiv in 2026. The results show several other papers related to code scaling, code agents, and code generation from 2026 and recent years, but none match the exact "CodeScaler" query you requested.

The closest results are:
- "Scaling Laws for Code: A More Data-Hungry Regime" (arxiv 2510.08702)
- "Beyond Quantity: Trajectory Diversity Scaling for Code Agents" (arxiv 2602.03219)
- "CodeChemist: Functional Knowledge Transfer for Low-Resource Code Generation via Test-Time Scaling" (arxiv 2510.00501)

If you're looking for a specific CodeScaler paper, it may not be publicly available yet, or you might want to search arXiv directly with a different query or check if there's an alternative title for the paper you're interested in.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-19T09:12:17.536284+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Andrews et al \"Using Mutation Analysis for Assessing and Comparing Testing Coverage Criteria\" IEEE TSE mutation testing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Andrews et al \"Using Mutation Analysis for Assessing and Comparing Testing Coverage Criteria\" IEEE TSE mutation testing"
  }
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-19T09:12:17.536523+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Papadakis et al mutation testing survey meta-analysis comprehensive"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Papadakis et al mutation testing survey meta-analysis comprehensive"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-19T09:12:17.536752+00:00_

Web search results for query: "site:arxiv.org/abs/2601.22249 FunPRM authors"

Links: [{"title":"[2601.22249] FunPRM: Function-as-Step Process Reward Model with Meta Reward Correction for Code Generation","url":"https://arxiv.org/abs/2601.22249"},{"title":"FunPRM: Function-as-Step Process Reward Model with Meta Reward Correction for Code Generation","url":"https://arxiv.org/pdf/2601.22249"},{"title":"Dual-Model LLM Ensemble via Web Chat Interfaces Reaches Near-Perfect Sensitivity for Systematic-Review Screening: A Multi-Domain Validation with Equivalence to API Access","url":"https://www.medrxiv.org/content/10.1101/2025.11.03.25339455.full.pdf"},{"title":"ToolPRM: Fine-Grained Inference Scaling of Structured Outputs for Function Calling","url":"https://arxiv.org/pdf/2510.14703"},{"title":"An Efficient Motion Planning Method with a Lazy Demonstration Graph for Repetitive Pick-and-Place","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9703960/"}]

Based on the search results, the authors of the FunPRM paper are Ruiyi Zhang, Peijia Qin, Qi Cao, Eric Xue, and Pengtao Xie.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-19T09:12:17.537026+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Efficient Guided Generation for Large Language Models\" Willard Louf NeurIPS ICML workshop conference 2023 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Efficient Guided Generation for Large Language Models\" Willard Louf NeurIPS ICML workshop conference 2023 2024"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-19T09:12:17.537262+00:00_

Web search results for query: "CodeRL+ arxiv 2025 reinforcement learning code generation"

Links: [{"title":"CodeRL+: Improving Code Generation via Reinforcement with Execution Semantics Alignment","url":"https://arxiv.org/pdf/2510.18471"},{"title":"CodeRL+: Improving Code Generation via Reinforcement with Execution Semantics Alignment","url":"https://arxiv.org/html/2510.18471v1"},{"title":"[2510.18471] CodeRL+: Improving Code Generation via Reinforcement with Execution Semantics Alignment","url":"https://arxiv.org/abs/2510.18471"},{"title":"[2412.20367] Enhancing Code LLMs with Reinforcement Learning in Code Generation: A Survey","url":"https://arxiv.org/abs/2412.20367"},{"title":"Preprint, September 2025 CODERL+: Improving Code Generation via Reinforce-","url":"https://www.arxiv.org/pdf/2510.18471"},{"title":"[2207.01780v3] CodeRL: Mastering Code Generation through Pretrained Models and Deep Reinforcement Learning","url":"https://arxiv.org/abs/2207.01780v3"},{"title":"[2207.01780] CodeRL: Mastering Code Generation through Pretrained Models and Deep Reinforcement Learning","url":"https://arxiv.org/abs/2207.01780"}]

I found relevant information about CodeRL+. Here are the key results:

## CodeRL+: Improving Code Generation via Reinforcement with Execution Semantics Alignment

CodeRL+ is a novel approach that integrates execution semantics alignment into the RLVR training pipeline for code generation, enabling the model to infer variable-level execution trajectory and provide a direct learning signal of execution semantics.

### Performance and Generalization

CodeRL+ generalizes effectively to other coding tasks, yielding 15.5% and 4.4% higher accuracy on code-reasoning and test-output-generation benchmarks, respectively. CodeRL+ shows strong applicability across diverse RL algorithms and LLMs.

### Key Findings

Probe analyses provide compelling evidence that CodeRL+ strengthens the alignment between code's textual representations and its underlying execution sema
…[truncated 583 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "WebSearch",
  "elapsed_ms": 5
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-19T09:12:17.537539+00:00_

Web search results for query: "CodePRM arXiv "Qingyao Li" execution feedback process reward model"

Links: [{"title":"CodePRM: Execution Feedback-enhanced Process Reward Model for Code Generation - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.428/"},{"title":"A Survey of Process Reward Models: From Outcome Signals to Process","url":"https://arxiv.org/pdf/2510.08049"},{"title":"CodeRL+: Improving Code Generation via Reinforcement with Execution Semantics Alignment","url":"https://arxiv.org/html/2510.18471v1"},{"title":"Execution Feedback-enhanced Process Reward Model for ...","url":"https://aclanthology.org/2025.findings-acl.428.pdf"},{"title":"Act Like You’re Paying for This: Course-Correcting Code Agents with PRMs","url":"https://arxiv.org/html/2509.02360v1"},{"title":"A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models","url":"https://arxiv.org/html/2510.08049v3"},{"title":"Rewarding the Scientific Process: Process-Level Reward Modeling for Agentic Data Analysis","url":"https://arxiv.org/html/2604.24198v1"},{"title":"FunPRM: Function-as-Step Process Reward Model with Meta Reward Correction for Code Generation","url":"https://arxiv.org/html/2601.22249v1"}]

Based on the search results, I found comprehensive information about CodePRM:

## CodePRM Overview

CodePRM is a novel approach that leverages code execution feedback to build a code PRM (Process Reward Model). The research was authored by Qingyao Li, Xinyi Dai, Xiangyang Li, Weinan Zhang, Yasheng Wang, Ruiming Tang, and Yong Yu.

## Key Methodology

The approach collects a large dataset of thought traces where each thought step is labeled with their derived code pass rates, accompanied by the corresponding code snippet, and trains a PRM to take both the reasoning process and code execution feedback as input to score individual thought steps.

The work addresses the challenge that thought processes in code generation lack effective process
…[truncated 623 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-19T09:12:17.537829+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2602.17684 CodeScaler Xiao Zhu Zhijiang Guo execution-free reward model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2602.17684 CodeScaler Xiao Zhu Zhijiang Guo execution-free reward model"
  }
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-19T09:12:17.538075+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"FunPRM\" \"Ruiyi Zhang\" \"Peijia Qin\" arxiv 2026 code github"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"FunPRM\" \"Ruiyi Zhang\" \"Peijia Qin\" arxiv 2026 code github"
  }
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-19T09:12:17.538303+00:00_

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
  "session": "worker_research_literature-search-w8_20260519T090952",
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

_source line 54 · 2026-05-19T09:12:17.538515+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-19T09:12:17.538754+00:00_

Web search results for query: "Just et al "Are Mutants a Valid Substitute for Real Faults in Software Testing" FSE 2014"

Links: [{"title":"Are mutants a valid substitute for real faults in software testing? | Proceedings of the 22nd ACM SIGSOFT International Symposium on Foundations of Software Engineering","url":"https://dl.acm.org/doi/10.1145/2635868.2635929"},{"title":"Lecture 2 - Just et al FSE 2014 Mutants + Real Faults | CS7580, Fall 2021","url":"https://neu-se.github.io/CS7580-Fall-2021/lecture-notes/2-mutants-just-fse2014/"},{"title":"Are Mutants a Valid Substitute for Real Faults in Software Testing?","url":"https://homes.cs.washington.edu/~rjust/publ/mutants_real_faults_fse_2014.pdf"},{"title":"[PDF] Are mutants a valid substitute for real faults in software testing? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Are-mutants-a-valid-substitute-for-real-faults-in-Just-Jalali/e126c283f2d5b521ed535c2bbd265fe3ccd14d9f"},{"title":"PATPAT: Program analysis, the practice and theory: Are mutants a valid substitute for real faults in software testing?","url":"http://programanalysis.blogspot.com/2014/11/are-mutants-valid-substitute-for-real.html"},{"title":"Are mutants a valid substitute for real faults in software testing?","url":"https://dada.cs.washington.edu/research/tr/2014/02/UW-CSE-14-02-02.PDF"},{"title":"(PDF) Are Mutants a Valid Substitute for Real Faults in Software Testing?","url":"https://www.researchgate.net/publication/277664637_Are_Mutants_a_Valid_Substitute_for_Real_Faults_in_Software_Testing"},{"title":"Are Mutants a Valid Substitute for Real Faults in Software Testing?","url":"https://pdfs.semanticscholar.org/8cd7/9062e6aecee8e1c99471114607c63e54ca4b.pdf"}]

I found the paper you're looking for. Here's what I found:

## Paper Details

"Are Mutants a Valid Substitute for Real Faults in Software Testing?" was published at FSE 2014 (Proceedings of the 22nd ACM SIGSOFT International Symposium on Foundations of Software Engineering) 
…[truncated 1213 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-19T09:12:17.539069+00:00_

Web search results for query: "Andrews et al "Using Mutation Analysis for Assessing and Comparing Testing Coverage Criteria" IEEE TSE mutation testing"

Links: [{"title":"Using Mutation Analysis for Assessing and Comparing Testing Coverage Criteria - ProQuest","url":"https://www.proquest.com/openview/164800d340c644a7a0904701d9228ae1/1?pq-origsite=gscholar&cbl=21418"},{"title":"Practical Mutation Testing at Scale: A view from Google","url":"https://homes.cs.washington.edu/~rjust/publ/practical_mutation_testing_tse_2021.pdf"},{"title":"Searching and generating test inputs for mutation testing - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC3629277/"},{"title":"(PDF) Using mutation analysis for assessing and comparing testing coverage criteria","url":"https://www.academia.edu/11353077/Using_mutation_analysis_for_assessing_and_comparing_testing_coverage_criteria"},{"title":"PAPADAKIS, Mike - ORBilu: Detailed Reference","url":"https://orbilu.uni.lu/handle/10993/34950"},{"title":"(PDF) Using Mutation Analysis for Assessing and Comparing Testing Coverage Criteria","url":"https://www.researchgate.net/publication/3189678_Using_Mutation_Analysis_for_Assessing_and_Comparing_Testing_Coverage_Criteria"},{"title":"How effective are mutation testing tools? An empirical analysis of Java mutation testing tools with manual analysis and real faults | Empirical Software Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10664-017-9582-5"},{"title":"Practical Mutation Testing at Scale: A view from Google | IEEE Transactions on Software Engineering","url":"https://dl.acm.org/doi/abs/10.1109/TSE.2021.3107634"},{"title":"Using Mutation Analysis for Assessing and Comparing Testing Coverage Criteria | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/1703390/"}]

I found the paper you're looking for. Here are the details:

The paper "Using Mutation Analysis for Assessing and Comparing Testing Coverage Criteria" by An
…[truncated 868 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-19T09:12:17.539339+00:00_

Web search results for query: "Papadakis et al mutation testing survey meta-analysis comprehensive"

Links: [{"title":"Mutation Testing Advances: An Analysis and Survey - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0065245818300305"},{"title":"Mutation Testing Advances: An Analysis and Survey | Request PDF","url":"https://www.researchgate.net/publication/325014033_Mutation_Testing_Advances_An_Analysis_and_Survey"},{"title":"Mutation Testing Advances: An Analysis and Survey - UCL Discovery","url":"https://discovery.ucl.ac.uk/10056704/"},{"title":"[PDF] Chapter Six - Mutation Testing Advances: An Analysis and Survey | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Chapter-Six-Mutation-Testing-Advances:-An-Analysis-Papadakis-Kintis/d461ab9482b7fb5eadd7e6cd2c6dffced8ede8b8"},{"title":"Quantitative Metrics for Mutation Testing","url":"https://www.scitepress.org/Papers/2019/78418/78418.pdf"},{"title":"Mutation testing advances: An analysis and survey (chapter 6)","url":"https://alastairreid.github.io/RelatedWork/papers/papadakis:advances:2019/"},{"title":"dblp: Chapter Six - Mutation Testing Advances: An Analysis and Survey.","url":"https://dblp.org/rec/journals/ac/PapadakisK00TH19.html"},{"title":"Mutation Testing Advances: An Analysis and Survey","url":"https://mutationtesting.uni.lu/survey.pdf"}]

Based on the search results, I found information about the Papadakis et al. mutation testing survey:

The work is titled "Chapter Six - Mutation Testing Advances: An Analysis and Survey" by Mike Papadakis, Marinos Kintis, Jie Zhang, Yue Jia, Yves Le Traon, and Mark Harman, published in 2019.

Papadakis et al. summarized 217 papers published from 2008 and 2017 that used mutation testing to perform test assessment.

Mutation testing realizes the idea of using artificial defects to support testing activities, and is typically used as a way to evaluate the adequacy of test suites, to guide the generation of test cases, and to suppo
…[truncated 621 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-19T09:12:17.539613+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.18471",
  "prompt": "Extract the following details from this arXiv paper page: 1) Full title, 2) Complete list of all authors, 3) Submission date and year, 4) Full abstract text, 5) Any subject categories or keywords listed."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2510.18471",
    "prompt": "Extract the following details from this arXiv paper page: 1) Full title, 2) Complete list of all authors, 3) Submission date and year, 4) Full abstract text, 5) Any subject categories or keywords listed."
  }
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-19T09:12:17.539880+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv.org CodePRM \"2502\" OR \"2501\" OR \"2503\" OR \"2504\" execution feedback process reward"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv.org CodePRM \"2502\" OR \"2501\" OR \"2503\" OR \"2504\" execution feedback process reward"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-19T09:12:17.540121+00:00_

Web search results for query: "arxiv 2602.17684 CodeScaler Xiao Zhu Zhijiang Guo execution-free reward model"

Links: [{"title":"[2602.17684] CodeScaler: Scaling Code LLM Training and Test-Time Inference via Execution-Free Reward Models","url":"https://arxiv.org/abs/2602.17684"},{"title":"GitHub - LARK-AI-Lab/CodeScaler: The official repo for \"CodeScaler: Scaling Code LLM Training and Test-Time Inference via Execution-Free Reward Models\" · GitHub","url":"https://github.com/LARK-AI-Lab/CodeScaler"},{"title":"CodeScaler: Scaling Code LLM Training and Test-Time ...","url":"https://arxiv.org/pdf/2602.17684"},{"title":"CodeScaler: Scaling Code LLM Training and Test-Time Inference via Execution-Free Reward Models","url":"https://arxiv.org/html/2602.17684"},{"title":"Machine Learning","url":"https://arxiv.org/list/cs.LG/recent?skip=651&show=50"},{"title":"SWE-RM: Execution-free Feedback For Software Engineering Agents","url":"https://arxiv.org/pdf/2512.21919"}]

I found the paper you're looking for. Here are the key details:

**Paper Title:** CodeScaler: Scaling Code LLM Training and Test-Time Inference via Execution-Free Reward Models

**Authors:** Xiao Zhu, Xinyu Zhou, Boyu Zhu, Hanxu Hu, Mingzhe Du, Haotian Zhang, Huiming Wang, Zhijiang Guo

**arXiv ID:** 2602.17684 (submitted February 4, 2026)

**Overview:** CodeScaler is an execution-free reward model designed to scale both reinforcement learning training and test-time inference for code generation. It is trained on carefully curated preference data derived from verified code problems and incorporates syntax-aware code extraction and validity-preserving reward shaping to ensure stable and robust optimization.

**Key Results:** Across five coding benchmarks, CodeScaler improves Qwen3-8B-Base by an average of +11.72 points, outperforming binary execution-based RL by +1.82 points, and enables scalable reinforcement learning on synthetic datasets without any test cases. Additionally, at inference time, CodeScaler serves
…[truncated 370 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-19T09:12:17.540401+00:00_

Web search results for query: ""Efficient Guided Generation for Large Language Models" Willard Louf NeurIPS ICML workshop conference 2023 2024"

Links: [{"title":"[2307.09702] Efficient Guided Generation for Large Language Models","url":"https://arxiv.org/abs/2307.09702"},{"title":"GUARANTEED GENERATION FROM LARGE LANGUAGE ...","url":"https://openreview.net/pdf?id=8roRgrjbjv"},{"title":"[PDF] Efficient Guided Generation for Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Efficient-Guided-Generation-for-Large-Language-Willard-Louf/c4ceaef35bca063815f50d90a087acbd07a65478"},{"title":"Paper page - Efficient Guided Generation for Large Language Models","url":"https://huggingface.co/papers/2307.09702"},{"title":"Efficient Guided Generation for Large Language Models","url":"https://arxiv.org/pdf/2307.09702"},{"title":"Beyond In-Context Learning: Aligning Long-form Generation of Large Language Models via Task-Inherent Attribute Guidelines","url":"https://arxiv.org/pdf/2506.01265"},{"title":"(PDF) Efficient Guided Generation for LLMs","url":"https://www.researchgate.net/publication/372468267_Efficient_Guided_Generation_for_LLMs"},{"title":"G2: Guided Generation for Enhanced Output Diversity in LLMs","url":"https://arxiv.org/pdf/2511.00432"},{"title":"Efficient Guided Generation for Large Language Models: Discussion, References and Acknowledgments | HackerNoon","url":"https://hackernoon.com/efficient-guided-generation-for-large-language-models-discussion-references-and-acknowledgments"}]

Based on the search results, I found the paper you're looking for:

"Efficient Guided Generation for Large Language Models" is authored by Brandon T. Willard and Rémi Louf. The paper shows how the problem of neural text generation can be constructively reformulated in terms of transitions between the states of a finite-state machine.

The framework leads to an efficient approach to guiding text generation with regular expressions and context-free gramm
…[truncated 695 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-19T09:12:17.540672+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Andrews Briand Labiche Namin \"Using Mutation Analysis for Assessing and Comparing Testing Coverage Criteria\" IEEE TSE 2006 DOI"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Andrews Briand Labiche Namin \"Using Mutation Analysis for Assessing and Comparing Testing Coverage Criteria\" IEEE TSE 2006 DOI"
  }
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-19T09:12:17.540931+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Just Jalali Inozemtseva Ernst Holmes Fraser \"Are Mutants a Valid Substitute\" FSE 2014 DOI 10.1145"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Just Jalali Inozemtseva Ernst Holmes Fraser \"Are Mutants a Valid Substitute\" FSE 2014 DOI 10.1145"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-19T09:12:17.541159+00:00_

# arXiv Paper Details

**1) Full Title:**
"CodeRL+: Improving Code Generation via Reinforcement with Execution Semantics Alignment"

**2) Complete List of Authors:**
Xue Jiang, Yihong Dong, Mengyang Liu, Hongyi Deng, Tian Wang, Yongding Tao, Rongyu Cao, Binhua Li, Zhi Jin, Wenpin Jiao, Fei Huang, Yongbin Li, and Ge Li

**3) Submission Date and Year:**
Initial submission: October 21, 2025 (with revision on April 22, 2026)

**4) Full Abstract:**
The paper addresses how large language models trained on textual patterns can better achieve functional correctness. The authors propose CodeRL+, which "integrates execution semantics alignment into the RLVR training pipeline for code generation." The model infers variable-level execution trajectories to provide direct learning signals. Their method demonstrates a "4.6% average relative improvement in pass@1" compared to post-training baselines and shows strong generalization across other coding tasks.

**5) Subject Categories:**
- Software Engineering (cs.SE)
- Artificial Intelligence (cs.AI)
- Computation and Language (cs.CL)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-19T09:12:17.541437+00:00_

Web search results for query: ""FunPRM" "Ruiyi Zhang" "Peijia Qin" arxiv 2026 code github"

Links: [{"title":"[2601.22249] FunPRM: Function-as-Step Process Reward Model with Meta Reward Correction for Code Generation","url":"https://arxiv.org/abs/2601.22249"},{"title":"(PDF) FunPRM: Function-as-Step Process Reward Model with Meta Reward Correction for Code Generation","url":"https://www.researchgate.net/publication/400340056_FunPRM_Function-as-Step_Process_Reward_Model_with_Meta_Reward_Correction_for_Code_Generation"},{"title":"FunPRM: Function-as-Step Process Reward Model with Meta Reward Correction for Code Generation","url":"https://arxiv.org/pdf/2601.22249"},{"title":"FreePRM: Training Process Reward Models Without Ground Truth Process Labels","url":"https://arxiv.org/pdf/2506.03570"},{"title":"Supervised Principal Component Regression for Functional Responses with   High Dimensional Predictors","url":"https://arxiv.org/pdf/2103.11567"}]

Great! I found the FunPRM paper. Now let me search for the GitHub code repository:

Links: [{"title":"GitHub - hamoid/Fun-Programming: Code from the Fun Programming creative coding tutorials and my own random sketches","url":"https://github.com/hamoid/Fun-Programming"},{"title":"github repositories · GitHub","url":"https://github.com/orgs/github/repositories"},{"title":"Trending repositories on GitHub today · GitHub","url":"https://github.com/trending"},{"title":"fun-project · GitHub Topics","url":"https://github.com/topics/fun-project"},{"title":"15 Most Popular GitHub Repos for Developers in 2026","url":"https://www.hostinger.com/tutorials/most-popular-github-repos"},{"title":"fun-projects · GitHub Topics","url":"https://github.com/topics/fun-projects"},{"title":"repo · GitHub Topics","url":"https://github.com/topics/repo"},{"title":"Fun Coding Projects · GitHub","url":"https://github.com/Fun-Coding-Projects"},{"title":"Add Code on GitHub Repository - GeeksforGeeks","url":"https://www.geeksforgeeks.org/git/how-to-add-code-on-
…[truncated 2712 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-19T09:12:17.541718+00:00_

Web search results for query: "arxiv.org CodePRM "2502" OR "2501" OR "2503" OR "2504" execution feedback process reward"

Links: [{"title":"CodePRM: Execution Feedback-enhanced Process Reward Model for Code Generation - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.428/"},{"title":"DreamPRM-Code: Function-as-Step Process Reward Model with Label","url":"https://arxiv.org/pdf/2512.15000"},{"title":"A Survey of Process Reward Models: From Outcome Signals to Process","url":"https://arxiv.org/pdf/2510.08049"},{"title":"A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models","url":"https://arxiv.org/html/2510.08049v3"},{"title":"Rewarding the Scientific Process: Process-Level Reward Modeling for Agentic Data Analysis","url":"https://arxiv.org/html/2604.24198v1"},{"title":"CodeRL+: Improving Code Generation via Reinforcement with Execution Semantics Alignment","url":"https://arxiv.org/html/2510.18471v1"},{"title":"FunPRM: Function-as-Step Process Reward Model with Meta Reward Correction for Code Generation","url":"https://arxiv.org/html/2601.22249v1"},{"title":"FunPRM: Function-as-Step Process Reward Model with Meta Reward","url":"https://www.arxiv.org/pdf/2601.22249"},{"title":"Act Like You’re Paying for This: Course-Correcting Code Agents with PRMs","url":"https://arxiv.org/html/2509.02360v1"}]

Based on the search results, I found relevant information about CodePRM with execution feedback and process reward models:

## CodePRM: Execution Feedback-Enhanced Process Reward Model

CodePRM is a novel approach that leverages code execution feedback to build a code PRM (Process Reward Model). 

### Key Approach

The method collects a large dataset of thought traces, where each thought step is labeled with their derived code' pass rates, accompanied by the corresponding code snippets, and execution feedback. During training, a PRM is trained to take both the reasoning process and code execution feedback as in
…[truncated 652 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-19T09:12:17.542067+00:00_

Here are the complete details for arXiv paper 2602.17684:

**Full Title:** CodeScaler: Scaling Code LLM Training and Test-Time Inference via Execution-Free Reward Models

**Authors (8 total):** Xiao Zhu, Xinyu Zhou, Boyu Zhu, Hanxu Hu, Mingzhe Du, Haotian Zhang, Huiming Wang, Zhijiang Guo

**Year:** 2026 (submitted February 4, 2026)

**arXiv ID:** 2602.17684

**Abstract Summary:** CodeScaler proposes an execution-free reward model that scales both reinforcement learning (RL) training and test-time inference for code generation. The model is trained on curated preference data derived from verified code problems, incorporating syntax-aware code extraction and validity-preserving reward shaping for stable optimization. Key results:

- Improves Qwen3-8B-Base by an average of **+11.72 points** across five coding benchmarks
- Outperforms binary execution-based RL by **+1.82 points**
- Enables scalable RL on synthetic datasets **without any test cases**
- At inference time, achieves performance comparable to unit-test-based approaches with a **10x reduction in latency**

The official code repository is at `LARK-AI-Lab/CodeScaler` on GitHub.

Sources:
- [CodeScaler on arXiv (abs)](https://arxiv.org/abs/2602.17684)
- [CodeScaler on arXiv (HTML)](https://arxiv.org/html/2602.17684)
- [CodeScaler PDF](https://arxiv.org/pdf/2602.17684)
- [LARK-AI-Lab/CodeScaler GitHub Repository](https://github.com/LARK-AI-Lab/CodeScaler)
agentId: ad3060f9b2a7f21ab (use SendMessage with to: 'ad3060f9b2a7f21ab' to continue this agent)
&lt;usage>total_tokens: 20391
tool_uses: 4
duration_ms: 33032&lt;/usage>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "Agent",
  "elapsed_ms": 14
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-19T09:12:17.542335+00:00_

Web search results for query: "Andrews Briand Labiche Namin "Using Mutation Analysis for Assessing and Comparing Testing Coverage Criteria" IEEE TSE 2006 DOI"

Links: [{"title":"Using Mutation Analysis for Assessing and Comparing Testing Coverage Criteria - ProQuest","url":"https://www.proquest.com/openview/164800d340c644a7a0904701d9228ae1/1?pq-origsite=gscholar&cbl=21418"},{"title":"(PDF) Using Mutation Analysis for Assessing and Comparing Testing Coverage Criteria","url":"https://www.researchgate.net/publication/3189678_Using_Mutation_Analysis_for_Assessing_and_Comparing_Testing_Coverage_Criteria"},{"title":"On the use of commit-relevant mutants - Ojdanic Milos - ORBilu","url":"https://orbilu.uni.lu/handle/10993/53863"},{"title":"How effective are mutation testing tools? An empirical analysis of Java mutation testing tools with manual analysis and real faults | Empirical Software Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10664-017-9582-5"},{"title":"Does choice of mutation tool matter? | Software Quality Journal | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11219-016-9317-7"},{"title":"Mutation Testing Advances: An Analysis and Survey","url":"https://ouci.dntb.gov.ua/en/works/lmGP0m57/"},{"title":"On guiding the augmentation of an automated test suite via mutation analysis | Empirical Software Engineering","url":"https://link.springer.com/article/10.1007/s10664-008-9083-7"},{"title":"Empirical Evaluation on FBD Model-Based Test Coverage Criteria Using Mutation Analysis | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-642-33666-9_30"},{"title":"Assessing the Effectiveness of Coverage-Based Fault Localizations Using Mutants | International Journal of Software Engineering and Knowledge Engineering","url":"https://www.worldscientific.com/doi/abs/10.1142/S0218194018500316"},{"title":"Using Mutation Analysis for Assessing and Comparing Testing Coverage Criteria | IEEE J
…[truncated 753 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-19T09:12:17.542639+00:00_

Here are the details:

1. **Full title:** Efficient Guided Generation for Large Language Models
2. **Complete author list:** Brandon T. Willard and Remi Louf
3. **Venue:** arXiv preprint (no confirmed conference or journal publication found; it remains a preprint)
4. **Year:** 2023 (posted July 19, 2023)
5. **arXiv ID:** 2307.09702

The paper reformulates neural text generation as transitions between states of a finite-state machine, enabling efficient guided generation via regular expressions and context-free grammars. The approach is implemented in the open-source Python library **Outlines** (now maintained under the dottxt-ai GitHub organization). Multiple versions exist on arXiv (v1 through v3).

Sources:
- [arXiv abstract page](https://arxiv.org/abs/2307.09702)
- [Semantic Scholar entry](https://www.semanticscholar.org/paper/Efficient-Guided-Generation-for-Large-Language-Willard-Louf/c4ceaef35bca063815f50d90a087acbd07a65478)
- [HuggingFace paper page](https://huggingface.co/papers/2307.09702)
- [GitHub - dottxt-ai/outlines](https://github.com/dottxt-ai/outlines)
agentId: a5ea363c6bf73c07a (use SendMessage with to: 'a5ea363c6bf73c07a' to continue this agent)
&lt;usage>total_tokens: 20747
tool_uses: 4
duration_ms: 35913&lt;/usage>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "Agent",
  "elapsed_ms": 15
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-19T09:12:17.542935+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:arxiv.org \"CodePRM\" \"Qingyao Li\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:arxiv.org \"CodePRM\" \"Qingyao Li\""
  }
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-19T09:12:17.543196+00:00_

Web search results for query: "Just Jalali Inozemtseva Ernst Holmes Fraser "Are Mutants a Valid Substitute" FSE 2014 DOI 10.1145"

Links: [{"title":"Are mutants a valid substitute for real faults in software testing?","url":"https://homes.cs.washington.edu/~mernst/pubs/mutation-effectiveness-fse2014-abstract.html"},{"title":"[PDF] Are mutants a valid substitute for real faults in software testing? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Are-mutants-a-valid-substitute-for-real-faults-in-Just-Jalali/e126c283f2d5b521ed535c2bbd265fe3ccd14d9f"},{"title":"Are mutants a valid substitute for real faults in software testing? | Proceedings of the 22nd ACM SIGSOFT International Symposium on Foundations of Software Engineering","url":"https://dl.acm.org/doi/10.1145/2635868.2635929"},{"title":"PATPAT: Program analysis, the practice and theory: Are mutants a valid substitute for real faults in software testing?","url":"http://programanalysis.blogspot.com/2014/11/are-mutants-valid-substitute-for-real.html"},{"title":"L20a-mutant-fse-talk-slides - Are Mutants a Valid Substitute for Real Faults in Software Testing Ren Just Darioush Jalali Laura Inozemtseva Michael D","url":"https://www.coursehero.com/file/11367959/L20a-mutant-fse-talk-slides/"},{"title":"(PDF) Are Mutants a Valid Substitute for Real Faults in Software Testing?","url":"https://www.researchgate.net/publication/277664637_Are_Mutants_a_Valid_Substitute_for_Real_Faults_in_Software_Testing"},{"title":"ACM Distinguished Paper Award to CSE's René Just, Darioush Jalali, Michael Ernst - Allen School News","url":"https://news.cs.washington.edu/2014/11/19/acm-distinguished-paper-award-to-cses-rene-just-darioush-jalali-michael-ernst/"},{"title":"Professor Reid Holmes and graduate student Laura Inozemtseva win ACM Distinguished Paper Award | Cheriton School of Computer Science | University of Waterloo","url":"https://uwaterloo.ca/computer-science/news/professor-reid-holmes-and-graduate-student-laura-inoze
…[truncated 1499 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-19T09:12:17.543513+00:00_

Here are the complete details for arXiv paper 2510.18471:

**Full Title:** CodeRL+: Improving Code Generation via Reinforcement with Execution Semantics Alignment

**Authors:** Xue Jiang, Yihong Dong, Mengyang Liu, Hongyi Deng, Tian Wang, Yongding Tao, Rongyu Cao, Binhua Li, Zhi Jin, Wenpin Jiao, Fei Huang, Yongbin Li, and Ge Li

**Year:** 2025 (initially submitted October 21, 2025; revised April 22, 2026)

**arXiv ID:** 2510.18471

**Subject Categories:** Software Engineering (cs.SE), Artificial Intelligence (cs.AI), Computation and Language (cs.CL)

**Abstract Summary:** The paper addresses a fundamental semantic gap in LLM-based code generation: current models learn textual patterns from code corpora but lack grounding in formal execution semantics. While RLVR (Reinforcement Learning with Verifiable Rewards) approaches attempt to bridge this gap using pass/fail test-case outcomes, these binary signals are sparse and insufficient, yielding only marginal improvements (~4% over base models). CodeRL+ integrates execution semantics alignment directly into the RLVR training pipeline by enabling the model to infer variable-level execution trajectories, providing a direct learning signal tied to execution semantics. The method achieves a 4.6% average relative improvement in pass@1 over post-training baselines and generalizes to other coding tasks, with 15.5% and 4.4% higher accuracy on code-reasoning and test-output-generation benchmarks respectively. Probe analyses confirm that CodeRL+ strengthens alignment between code's textual representations and underlying execution semantics.

Sources:
- [CodeRL+: Improving Code Generation via Reinforcement with Execution Semantics Alignment (abs)](https://arxiv.org/abs/2510.18471)
- [CodeRL+ HTML version](https://arxiv.org/html/2510.18471v1)
- [CodeRL+ PDF](https://arxiv.org/pdf/2510.18471)
agentId: acd88a18758eeded9 (use SendMessage with to: 'acd88a18758eeded9' to continue this agent)
&lt;usage>total_tokens: 21126
tool_uses: 5
durat
…[truncated 21 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "Agent",
  "elapsed_ms": 15
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-19T09:12:17.543850+00:00_

Here are the details for arXiv paper 2601.22249:

**Full title:** FunPRM: Function-as-Step Process Reward Model with Meta Reward Correction for Code Generation

**Authors:** Ruiyi Zhang, Peijia Qin, Qi Cao, Eric Xue, Pengtao Xie

**Year:** 2026 (submitted January 29, 2026)

**arXiv ID:** 2601.22249

**arXiv abstract page:** https://arxiv.org/abs/2601.22249

**Key details:**
- FunPRM prompts LLMs to generate modular code organized into functions, treating each function as a PRM reasoning step.
- Introduces a meta-learning-based reward correction mechanism that uses clean final-solution rewards (from unit-test evaluation) to denoise Monte Carlo-estimated partial-solution rewards.
- Evaluated on LiveCodeBench and BigCodeBench across five base LLMs. Achieves state-of-the-art on LiveCodeBench when combined with O4-mini.
- No public GitHub repository was found in my searches. The code may not yet be released or may be linked only within the PDF itself.

Sources:
- [arXiv abstract page](https://arxiv.org/abs/2601.22249)
- [arXiv HTML version](https://arxiv.org/html/2601.22249)
- [ResearchGate page](https://www.researchgate.net/publication/400340056_FunPRM_Function-as-Step_Process_Reward_Model_with_Meta_Reward_Correction_for_Code_Generation)
agentId: a8e0f04f2f2cebf32 (use SendMessage with to: 'a8e0f04f2f2cebf32' to continue this agent)
&lt;usage>total_tokens: 22167
tool_uses: 6
duration_ms: 43062&lt;/usage>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "Agent",
  "elapsed_ms": 17
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-19T09:12:17.544113+00:00_

Web search results for query: "site:arxiv.org "CodePRM" "Qingyao Li""

Links: [{"title":"CodePRM: Execution Feedback-enhanced Process Reward Model for Code Generation - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.428/"},{"title":"Process Supervision-Guided Policy Optimization for Code Generation","url":"https://arxiv.org/pdf/2410.17621"},{"title":"An Optimized Probabilistic Roadmap Algorithm for Path Planning of Mobile Robots in Complex Environments with Narrow Channels","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9699578/"},{"title":"On the Minimum Distance, Minimum Weight Codewords, and the Dimension of   Projective Reed-Muller Codes","url":"https://arxiv.org/pdf/2309.10196"},{"title":"Decoding of Projective Reed-Muller Codes by Dividing a Projective Space   into Affine Spaces","url":"https://arxiv.org/pdf/1412.4365"},{"title":"Conditional quantile sequential estimation for stochastic codes","url":"https://arxiv.org/pdf/1508.06505"}]

Based on the search results, I found relevant information about CodePRM and Qingyao Li:

CodePRM is a paper authored by Qingyao Li, Xinyi Dai, Xiangyang Li, Weinan Zhang, Yasheng Wang, Ruiming Tang, and Yong Yu, published in the Findings of the Association for Computational Linguistics: ACL 2025 in July 2025.

CodePRM is a novel approach that leverages code execution feedback to build a code PRM (Process Reward Model). The paper addresses the challenge that while Process Reward Models have been established in mathematical reasoning, building a code PRM is still not trivial due to the gap between thoughts and code.

The paper appears to be available through the ACL Anthology at: https://aclanthology.org/2025.findings-acl.428/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-19T09:12:17.544377+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "aclanthology.org 2025.findings-acl.428 CodePRM doi arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "WebSearch",
  "tool_args": {
    "query": "aclanthology.org 2025.findings-acl.428 CodePRM doi arxiv"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-19T09:12:17.544664+00:00_

Here are the two most important papers establishing the coupling hypothesis (that mutation testing effectiveness correlates with real fault detection):

---

**Paper 1 (most comprehensive empirical validation):**

- **Title:** Are Mutants a Valid Substitute for Real Faults in Software Testing?
- **Authors:** Rene Just, Darioush Jalali, Laura Inozemtseva, Michael D. Ernst, Reid Holmes, Gordon Fraser
- **Venue:** FSE 2014 (Proceedings of the 22nd ACM SIGSOFT International Symposium on Foundations of Software Engineering), Hong Kong, November 2014, pages 654-665
- **DOI:** 10.1145/2635868.2635929
- **Key finding:** Statistically significant correlation between mutant detection and real fault detection, independently of code coverage. Used 357 real faults across 5 open-source programs (321K LOC total). Won the ACM Distinguished Paper Award.

**Paper 2 (foundational empirical study on mutation as test criterion):**

- **Title:** Using Mutation Analysis for Assessing and Comparing Testing Coverage Criteria
- **Authors:** James H. Andrews, Lionel C. Briand, Yvan Labiche, Akbar Siami Namin
- **Venue:** IEEE Transactions on Software Engineering (TSE), Volume 32, Issue 8, August 2006, pages 608-624
- **DOI:** 10.1109/TSE.2006.83
- **Key finding:** Generated mutants can be used effectively for test assessment; mutation-based criteria are a reliable proxy when evaluating coverage criteria on a mid-size industrial program with known faults.

**Supplementary survey (for broader context):**

- **Title:** Mutation Testing Advances: An Analysis and Survey
- **Authors:** Mike Papadakis, Marinos Kintis, Jie Zhang, Yue Jia, Yves Le Traon, Mark Harman
- **Venue:** Advances in Computers, Volume 112, 2019, pages 275-378
- This is the most comprehensive survey of the field (covers 217 papers from 2008-2017), but it is a survey rather than a primary empirical study.

For a bib entry establishing the coupling hypothesis, **Just et al. (FSE 2014)** is the single most-cited and most direct val
…[truncated 345 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "Agent",
  "elapsed_ms": 13
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-19T09:12:17.544976+00:00_

Web search results for query: "aclanthology.org 2025.findings-acl.428 CodePRM doi arxiv"

Links: [{"title":"CodePRM: Execution Feedback-enhanced Process Reward Model for Code Generation - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.428/"},{"title":"Accepted Findings Papers - ACL 2025","url":"https://2025.aclweb.org/program/find_papers/"},{"title":"Findings of the Association for Computational Linguistics: ACL 2025 - ACL Anthology","url":"https://aclanthology.org/volumes/2025.findings-acl/"},{"title":"DreamPRM-Code: Function-as-Step Process Reward Model with Label Correction for LLM Coding","url":"https://arxiv.org/pdf/2512.15000"},{"title":"Ask in Any Modality: A Comprehensive Survey on Multimodal Retrieval-Augmented Generation - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.861/"},{"title":"FunPRM: Function-as-Step Process Reward Model with Meta Reward Correction for Code Generation","url":"https://arxiv.org/pdf/2601.22249"}]

Based on the search results, here's the information about the paper:

**CodePRM: Execution Feedback-enhanced Process Reward Model for Code Generation** was published in the Findings of the Association for Computational Linguistics: ACL 2025, pages 8169–8182, Vienna, Austria.

**DOI:** 10.18653/v1/2025.findings-acl.428

**Key Details:**
- The paper trains a Process Reward Model (PRM) to take both the reasoning process and code execution feedback as input to score individual thought steps, leveraging code execution results to distinguish between high-quality and low-quality thought steps.
- The authors develop a Generate-Verify-Refine (GVR) pipeline where the CodePRM serves as a process verifier to dynamically identify and correct errors in the thought process during code search.
- Experimental results demonstrate that CodePRM with the inference algorithm outperforms strong baselines, significantly enhancing code generation performance.

The paper is accessible at: https://aclanthology.org/2025.findings-a
…[truncated 110 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-19T09:12:17.545252+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv abs \"CodePRM\" \"Execution Feedback-enhanced Process Reward Model\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv abs \"CodePRM\" \"Execution Feedback-enhanced Process Reward Model\""
  }
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-19T09:12:17.545507+00:00_

Web search results for query: "arxiv abs "CodePRM" "Execution Feedback-enhanced Process Reward Model""

Links: [{"title":"CodePRM: Execution Feedback-enhanced Process Reward Model for Code Generation - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.428/"},{"title":"A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models","url":"https://arxiv.org/html/2510.08049v3"},{"title":"Rewarding the Scientific Process: Process-Level Reward Modeling for Agentic Data Analysis","url":"https://arxiv.org/html/2604.24198v1"},{"title":"DreamPRM-Code: Function-as-Step Process Reward Model with Label","url":"https://arxiv.org/pdf/2512.15000"},{"title":"FunPRM: Function-as-Step Process Reward Model with Meta Reward","url":"https://www.arxiv.org/pdf/2601.22249"},{"title":"FunPRM: Function-as-Step Process Reward Model with Meta Reward Correction for Code Generation","url":"https://arxiv.org/html/2601.22249v1"},{"title":"Act Like You’re Paying for This: Course-Correcting Code Agents with PRMs","url":"https://arxiv.org/html/2509.02360v1"},{"title":"A Survey of Process Reward Models: From Outcome Signals to Process","url":"https://arxiv.org/pdf/2510.08049"},{"title":"CodeRL+: Improving Code Generation via Reinforcement with Execution Semantics Alignment","url":"https://arxiv.org/html/2510.18471v1"}]

I found search results for CodePRM. Here's what the search revealed:

## CodePRM: Execution Feedback-enhanced Process Reward Model

CodePRM is a novel approach that leverages code execution feedback to build a code Process Reward Model (PRM).

### Key Approach

The method collects a large dataset of thought traces where each thought step is labeled with code pass rates, code snippets, and execution feedback. During training, a PRM is trained to take both the reasoning process and code execution feedback as input to score individual thought steps.

### Inference Method

For inference, the researchers developed a Generate-Verify-R
…[truncated 699 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-19T09:12:17.545849+00:00_

Here are the details I found for the CodePRM paper:

**1. Full title:**
CodePRM: Execution Feedback-enhanced Process Reward Model for Code Generation

**2. Complete author list:**
Qingyao Li, Xinyi Dai, Xiangyang Li, Weinan Zhang, Yasheng Wang, Ruiming Tang, Yong Yu

**3. Venue details:**
Findings of the Association for Computational Linguistics: ACL 2025, Vienna, Austria, July 2025

**4. Page numbers and DOI:**
- Pages: 8169--8182
- DOI: `10.18653/v1/2025.findings-acl.428`
- ACL Anthology ID: `2025.findings-acl.428`

**5. arXiv ID:**
I was unable to find a standalone arXiv preprint for this paper across multiple searches. The paper appears to be available only through the ACL Anthology (the PDF is at `https://aclanthology.org/2025.findings-acl.428.pdf`). It is possible the authors did not post an arXiv preprint, or it may exist under a slightly different title that my searches did not surface.

**BibTeX entry (reconstructed from ACL Anthology data):**
```bibtex
@inproceedings{li-etal-2025-codeprm,
    title     = "{CodePRM}: Execution Feedback-enhanced Process Reward Model for Code Generation",
    author    = "Li, Qingyao and Dai, Xinyi and Li, Xiangyang and Zhang, Weinan and Wang, Yasheng and Tang, Ruiming and Yu, Yong",
    booktitle = "Findings of the Association for Computational Linguistics: ACL 2025",
    year      = "2025",
    address   = "Vienna, Austria",
    pages     = "8169--8182",
    doi       = "10.18653/v1/2025.findings-acl.428",
    url       = "https://aclanthology.org/2025.findings-acl.428/",
}
```

Sources:
- [CodePRM: Execution Feedback-enhanced Process Reward Model for Code Generation - ACL Anthology](https://aclanthology.org/2025.findings-acl.428/)
- [Accepted Findings Papers - ACL 2025](https://2025.aclweb.org/program/find_papers/)
- [Findings of ACL 2025 Volume](https://aclanthology.org/volumes/2025.findings-acl/)
agentId: a98c9fd1c3d7e0d9b (use SendMessage with to: 'a98c9fd1c3d7e0d9b' to continue this agent)
&lt;usage>total_tokens: 23647
to
…[truncated 37 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-search-w8_20260519T090952",
  "tool": "Agent",
  "elapsed_ms": 20
}
```

</details>

---

### Assistant

_source line 81 · 2026-05-19T09:12:17.546281+00:00_

全部找到。以下是完整结果。

---

## 1. CodePRM: Execution Feedback-enhanced Process Reward Model for Code Generation

**BibTeX:**
```bibtex
@inproceedings{li2025codeprm,
    title     = {{CodePRM}: Execution Feedback-enhanced Process Reward Model for Code Generation},
    author    = {Li, Qingyao and Dai, Xinyi and Li, Xiangyang and Zhang, Weinan and Wang, Yasheng and Tang, Ruiming and Yu, Yong},
    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},
    year      = {2025},
    address   = {Vienna, Austria},
    pages     = {8169--8182},
    doi       = {10.18653/v1/2025.findings-acl.428},
}
```

**与本文关系：** CodePRM 用 execution feedback 构建 process reward model 来验证 code generation 的中间步骤，与本文的 per-test classification formulation 共享 process supervision 视角，但 CodePRM 依赖 execution feedback 而本文是 execution-free。

**建议引用：** Yes. 直接相关的 process-level verification baseline，且凸显本文 execution-free 的差异化贡献。

---

## 2. FunPRM: Function-as-Step Process Reward Model with Meta Reward Correction for Code Generation

**BibTeX:**
```bibtex
@misc{zhang2026funprm,
    title         = {{FunPRM}: Function-as-Step Process Reward Model with Meta Reward Correction for Code Generation},
    author        = {Zhang, Ruiyi and Qin, Peijia and Cao, Qi and Xue, Eric and Xie, Pengtao},
    year          = {2026},
    eprint        = {2601.22249},
    archivePrefix = {arXiv},
    primaryClass  = {cs.CL},
}
```

**与本文关系：** FunPRM 将函数作为 PRM 的推理步骤粒度，与本文的 function-level verification 思路相近；其 meta-learning reward correction 机制也涉及用 test outcome 去校准 process reward，可作为 function-level granularity 的对照讨论。

**建议引用：** Yes. 同期工作，function-level verification granularity 的直接对照。

---

## 3. Efficient Guided Generation for Large Language Models

**BibTeX:**
```bibtex
@misc{willard2023efficient,
    title         = {Efficient Guided Generation for Large Language Models},
    author        = {Willard, Brandon T. and Louf, R\'{e}mi},
    year          = {2023},
    eprint        = {2307.09702},
    archivePrefix = {arXiv},
    primaryClass  = {cs.CL},
}
```

**与本文关系：** 本文 CWM formulation 使用 constrained decoding 强制输出符合 per-test JSON schema；Willard & Louf 提出的 FSM-guided generation（Outlines 库的理论基础）正是此类 format compliance 的方法论支撑。

**建议引用：** Yes. CWM constrained decoding 的方法论引用，说明 format compliance 有理论保障。

---

## 4. CodeScaler: Scaling Code LLM Training and Test-Time Inference via Execution-Free Reward Models

**BibTeX:**
```bibtex
@misc{zhu2026codescaler,
    title         = {{CodeScaler}: Scaling Code {LLM} Training and Test-Time Inference via Execution-Free Reward Models},
    author        = {Zhu, Xiao and Zhou, Xinyu and Zhu, Boyu and Hu, Hanxu and Du, Mingzhe and Zhang, Haotian and Wang, Huiming and Guo, Zhijiang},
    year          = {2026},
    eprint        = {2602.17684},
    archivePrefix = {arXiv},
    primaryClass  = {cs.CL},
}
```

**与本文关系：** CodeScaler 训练 execution-free reward model 用于 RL 训练和 test-time inference，与本文核心主题（execution-free verification）高度重合。其 syntax-aware code extraction 和 validity-preserving reward shaping 可作为 execution-free 方向的同期工作讨论。关键差异：CodeScaler 侧重 RL 训练 scaling，本文侧重 repair verification formulation 比较。

**建议引用：** Yes. 同期 execution-free verification 工作，强化本文研究方向的时效性和重要性。

---

## 5. CodeRL+: Improving Code Generation via Reinforcement with Execution Semantics Alignment

**BibTeX:**
```bibtex
@misc{jiang2025coderlplus,
    title         = {{CodeRL}+: Improving Code Generation via Reinforcement with Execution Semantics Alignment},
    author        = {Jiang, Xue and Dong, Yihong and Liu, Mengyang and Deng, Hongyi and Wang, Tian and Tao, Yongding and Cao, Rongyu and Li, Binhua and Jin, Zhi and Jiao, Wenpin and Huang, Fei and Li, Yongbin and Li, Ge},
    year          = {2025},
    eprint        = {2510.18471},
    archivePrefix = {arXiv},
    primaryClass  = {cs.SE},
}
```

**与本文关系：** CodeRL+ 将 execution semantics（variable-level execution trajectories）融入 RL 训练，解决 binary pass/fail signal 过于稀疏的问题。与本文的 TRAJ formulation（trajectory-level verification）概念上相关：都试图利用比 binary outcome 更细粒度的 execution 信息。差异在于 CodeRL+ 用于 RL 训练，本文用于 verification。

**建议引用：** Yes. execution semantics alignment 视角支撑本文 TRAJ formulation 的动机。

---

## 6. Mutation-Real Fault Coupling

### 6a. Just et al. (FSE 2014) — 最直接的实证验证

**BibTeX:**
```bibtex
@inproceedings{just2014mutants,
    title     = {Are Mutants a Valid Substitute for Real Faults in Software Testing?},
    author    = {Just, Ren\'{e} and Jalali, Darioush and Inozemtseva, Laura and Ernst, Michael D. and Holmes, Reid and Fraser, Gordon},
    booktitle = {Proceedings of the 22nd ACM SIGSOFT International Symposium on Foundations of Software Engineering},
    series    = {FSE 2014},
    year      = {2014},
    address   = {Hong Kong, China},
    pages     = {654--665},
    doi       = {10.1145/2635868.2635929},
}
```

**与本文关系：** 本文用 synthetic mutations 训练和评测 verifier，coupling hypothesis（mutation detection 与 real fault detection 显著相关）是这一设计选择的理论基础。Just et al. 在 357 个真实缺陷上实证验证了这一假设，是最直接的支撑文献。

**建议引用：** Yes. 支撑本文 synthetic mutation 实验设计的核心理论依据。

### 6b. Andrews et al. (TSE 2006) — 奠基性实证研究

**BibTeX:**
```bibtex
@article{andrews2006mutation,
    title   = {Using Mutation Analysis for Assessing and Comparing Testing Coverage Criteria},
    author  = {Andrews, James H. and Briand, Lionel C. and Labiche, Yvan and Namin, Akbar Siami},
    journal = {IEEE Transactions on Software Engineering},
    volume  = {32},
    number  = {8},
    pages   = {608--624},
    year    = {2006},
    doi     = {10.1109/TSE.2006.83},
}
```

**与本文关系：** 奠基性工作，证明 generated mutants 可有效替代真实缺陷进行测试评估。Just et al. 2014 在此基础上做了更大规模验证。

**建议引用：** Yes（可选）。如果篇幅允许，与 Just et al. 一起引用提供更完整的理论链条；篇幅紧张时只引 Just et al. 即可。

---

## 汇总 BibTeX（可直接复制）

```bibtex
% === 1. CodePRM (ACL 2025 Findings) ===
@inproceedings{li2025codeprm,
    title     = {{CodePRM}: Execution Feedback-enhanced Process Reward Model for Code Generation},
    author    = {Li, Qingyao and Dai, Xinyi and Li, Xiangyang and Zhang, Weinan and Wang, Yasheng and Tang, Ruiming and Yu, Yong},
    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},
    year      = {2025},
    address   = {Vienna, Austria},
    pages     = {8169--8182},
    doi       = {10.18653/v1/2025.findings-acl.428},
}

% === 2. FunPRM (arXiv 2026) ===
@misc{zhang2026funprm,
    title         = {{FunPRM}: Function-as-Step Process Reward Model with Meta Reward Correction for Code Generation},
    author        = {Zhang, Ruiyi and Qin, Peijia and Cao, Qi and Xue, Eric and Xie, Pengtao},
    year          = {2026},
    eprint        = {2601.22249},
    archivePrefix = {arXiv},
    primaryClass  = {cs.CL},
}

% === 3. Willard & Louf (arXiv 2023) ===
@misc{willard2023efficient,
    title         = {Efficient Guided Generation for Large Language Models},
    author        = {Willard, Brandon T. and Louf, R\'{e}mi},
    year          = {2023},
    eprint        = {2307.09702},
    archivePrefix = {arXiv},
    primaryClass  = {cs.CL},
}

% === 4. CodeScaler (arXiv 2026) ===
@misc{zhu2026codescaler,
    title         = {{CodeScaler}: Scaling Code {LLM} Training and Test-Time Inference via Execution-Free Reward Models},
    author        = {Zhu, Xiao and Zhou, Xinyu and Zhu, Boyu and Hu, Hanxu and Du, Mingzhe and Zhang, Haotian and Wang, Huiming and Guo, Zhijiang},
    year          = {2026},
    eprint        = {2602.17684},
    archivePrefix = {arXiv},
    primaryClass  = {cs.CL},
}

% === 5. CodeRL+ (arXiv 2025) ===
@misc{jiang2025coderlplus,
    title         = {{CodeRL}+: Improving Code Generation via Reinforcement with Execution Semantics Alignment},
    author        = {Jiang, Xue and Dong, Yihong and Liu, Mengyang and Deng, Hongyi and Wang, Tian and Tao, Yongding and Cao, Rongyu and Li, Binhua and Jin, Zhi and Jiao, Wenpin and Huang, Fei and Li, Yongbin and Li, Ge},
    year          = {2025},
    eprint        = {2510.18471},
    archivePrefix = {arXiv},
    primaryClass  = {cs.SE},
}

% === 6a. Just et al. (FSE 2014) — mutation-real fault coupling ===
@inproceedings{just2014mutants,
    title     = {Are Mutants a Valid Substitute for Real Faults in Software Testing?},
    author    = {Just, Ren\'{e} and Jalali, Darioush and Inozemtseva, Laura and Ernst, Michael D. and Holmes, Reid and Fraser, Gordon},
    booktitle = {Proceedings of the 22nd ACM SIGSOFT International Symposium on Foundations of Software Engineering},
    series    = {FSE 2014},
    year      = {2014},
    address   = {Hong Kong, China},
    pages     = {654--665},
    doi       = {10.1145/2635868.2635929},
}

% === 6b. Andrews et al. (TSE 2006) — mutation analysis foundations ===
@article{andrews2006mutation,
    title   = {Using Mutation Analysis for Assessing and Comparing Testing Coverage Criteria},
    author  = {Andrews, James H. and Briand, Lionel C. and Labiche, Yvan and Namin, Akbar Siami},
    journal = {IEEE Transactions on Software Engineering},
    volume  = {32},
    number  = {8},
    pages   = {608--624},
    year    = {2006},
    doi     = {10.1109/TSE.2006.83},
}
```

7 篇 BibTeX 全部基于 WebSearch 验证，非幻觉。建议全部引用（Andrews et al. 视篇幅可选）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_literature-search-w8_20260519T090952"
}
```

</details>

---
