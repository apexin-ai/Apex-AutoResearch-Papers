# research plan 017 graph methods

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 43
- **Recorded user turns:** 0
- **Tool calls:** 14
- **Original source:** `logs/workers/worker_research_plan_017_graph_methods_20260513T212612.log`
- **Structured JSON:** [`a96054a60ec05dd81513.json`](../../sessions/a9/a96054a60ec05dd81513.json)

## Before a recorded user message

43 recorded events

### System

_source line 1_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "session_id": "d5364903-a4a1-4087-97e3-e23bdd6044c8",
  "tools": [
    "Task",
    "AskUserQuestion",
    "Bash",
    "CronCreate",
    "CronDelete",
    "CronList",
    "Edit",
    "EnterPlanMode",
    "EnterWorktree",
    "ExitPlanMode",
    "ExitWorktree",
    "Glob",
    "Grep",
    "ListMcpResourcesTool",
    "Monitor",
    "NotebookEdit",
    "PushNotification",
    "Read",
    "ReadMcpResourceTool",
    "RemoteTrigger",
    "ScheduleWakeup",
    "Skill",
    "TaskOutput",
    "TaskStop",
    "TodoWrite",
    "ToolSearch",
    "WebFetch",
    "WebSearch",
    "Write",
    "mcp__agent-ml-research__append_idea",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__save_project_file"
  ],
  "mcp_servers": [
    {
      "name": "agent-ml-research",
      "status": "connected"
    }
  ],
  "model": "claude-opus-4-6",
  "permissionMode": "bypassPermissions",
  "slash_commands": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api",
    "clear",
    "compact",
    "context",
    "heapdump",
    "init",
    "review",
    "security-review",
    "extra-usage",
    "usage",
    "insights",
    "team-onboarding"
  ],
  "apiKeySource": "none",
  "claude_code_version": "2.1.126",
  "output_style": "default",
  "agents": [
    "claude",
    "Explore",
    "general-purpose",
    "Plan",
    "statusline-setup"
  ],
  "skills": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api"
  ],
  "plugins": [],
  "analytics_disabled": false,
  "uuid": "17633a1e-c58e-47d8-84c8-4d8998015865",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-structfuse-context/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Runtime record

_source line 2_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1778725200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "7f250373-a958-4fdb-a794-bc4cd85c86d2",
  "session_id": "d5364903-a4a1-4087-97e3-e23bdd6044c8"
}
```

---

### Assistant

_source line 3_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to do a literature survey on inference-time graph-based code retrieval/localization methods and compare them with StructFuse. Let me break this down:

1. Search for papers: CodexGraph, LocAgent, RANGER, RepoGraph, GraphCoder, and others
2. Create a comparison table
3. Write discussion points
4. Write a Related Work paragraph draft
5. Save to project knowledge file

Let me start by searching for these papers. I'll use WebSearch for this. Let me first load the tools I need.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d5364903-a4a1-4087-97e3-e23bdd6044c8",
  "uuid": "53b0e87d-785f-40f2-bd69-83223abad35c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UVbVomvbEGTLstwKQKveDL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11454,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11454
      },
      "output_tokens": 50,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 4_

我来搜索这些 inference-time graph methods 的论文信息，然后整理对比表和写作素材。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d5364903-a4a1-4087-97e3-e23bdd6044c8",
  "uuid": "a9af3c27-6855-4bdd-afed-7c62e44e0cf6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UVbVomvbEGTLstwKQKveDL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11454,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11454
      },
      "output_tokens": 50,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 5_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01YUxTDrjci8ahP92PxuHVVW`</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__read_project_file",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d5364903-a4a1-4087-97e3-e23bdd6044c8",
  "uuid": "c34cf7cc-232b-4be7-91b9-ed369a3c0dbd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UVbVomvbEGTLstwKQKveDL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11454,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11454
      },
      "output_tokens": 50,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-13T21:45:45.883Z_

<details><summary>↩ Tool result · `toolu_01YUxTDrjci8ahP92PxuHVVW`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d5364903-a4a1-4087-97e3-e23bdd6044c8",
  "uuid": "1dd74fe7-2db6-4ce0-b12e-4d446771605d",
  "tool_use_result": {
    "matches": [
      "WebSearch",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__read_project_file"
    ],
    "query": "select:WebSearch,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__read_project_file",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Now let me search for each of these papers. I'll do multiple searches in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d5364903-a4a1-4087-97e3-e23bdd6044c8",
  "uuid": "892c2539-7586-4376-b0f4-2e7f29cab8e5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WS9srecx9g9EC4YNVE762J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1373,
      "cache_read_input_tokens": 23295,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1373
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0184yqwDh36T8u4Afw9hpKwt`</summary>

```json
{
  "query": "CodexGraph code graph LLM agent repository-level coding 2024 paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d5364903-a4a1-4087-97e3-e23bdd6044c8",
  "uuid": "ee4b74dd-7cd0-45ec-a0be-0d2bf1d428c8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WS9srecx9g9EC4YNVE762J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1373,
      "cache_read_input_tokens": 23295,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1373
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GjLMuidnpg9yxC6jGWVya1`</summary>

```json
{
  "query": "LocAgent fault localization graph-based agent code 2024 2025 paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d5364903-a4a1-4087-97e3-e23bdd6044c8",
  "uuid": "1994332a-6b96-430f-8ad7-dea4bb1fe9e3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WS9srecx9g9EC4YNVE762J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1373,
      "cache_read_input_tokens": 23295,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1373
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SAhFJUbkyaWm2za41JN1cj`</summary>

```json
{
  "query": "RANGER retrieval augmented graph code retrieval 2024 paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d5364903-a4a1-4087-97e3-e23bdd6044c8",
  "uuid": "eb25a7ec-2c99-4949-a3a1-d510987e1f8e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WS9srecx9g9EC4YNVE762J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1373,
      "cache_read_input_tokens": 23295,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1373
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-13T21:45:58.329Z_

<details><summary>↩ Tool result · `toolu_01SAhFJUbkyaWm2za41JN1cj`</summary>

```text
Web search results for query: "RANGER retrieval augmented graph code retrieval 2024 paper"

Links: [{"title":"[2501.00309] Retrieval-Augmented Generation with Graphs (GraphRAG)","url":"https://arxiv.org/abs/2501.00309"},{"title":"Graph Retrieval-Augmented Generation: A Survey | ACM Transactions on Information Systems","url":"https://dl.acm.org/doi/10.1145/3777378"},{"title":"[2408.08921] Graph Retrieval-Augmented Generation: A Survey","url":"https://arxiv.org/abs/2408.08921"},{"title":"Graph Retrieval-Augmented Generation: A Survey","url":"https://arxiv.org/pdf/2408.08921"},{"title":"Retrieval Augmented Generation Research: 2017-2024","url":"https://scalingknowledge.substack.com/p/rag"},{"title":"A Survey of Graph Retrieval-Augmented Generation for ...","url":"https://openreview.net/pdf?id=9FJiOMuZkr"},{"title":"GitHub - Graph-RAG/GraphRAG · GitHub","url":"https://github.com/Graph-RAG/GraphRAG"},{"title":"GitHub - DEEP-PolyU/Awesome-GraphRAG: Awesome-GraphRAG: A curated list of resources (surveys, papers, benchmarks, and opensource projects) on graph-based retrieval-augmented generation. · GitHub","url":"https://github.com/DEEP-PolyU/Awesome-GraphRAG"},{"title":"G-Retriever: Retrieval-Augmented Generation for Textual Graph Understanding and Question Answering","url":"https://proceedings.neurips.cc//paper_files/paper/2024/hash/efaf1c9726648c8ba363a5c927440529-Abstract-Conference.html"},{"title":"GitHub - XiaoxinHe/G-Retriever: Official Implementation of NeurIPS 2024 paper \"G-Retriever: Retrieval-Augmented Generation for Textual Graph Understanding and Question Answering\"\" · GitHub","url":"https://github.com/XiaoxinHe/G-Retriever"}]

Based on the search results, I found information about retrieval-augmented generation with graphs and code retrieval, though I didn't find a paper specifically titled "RANGER" in the 2024 papers. However, I found several highly relevant 2024 papers on graph-based retrieval-augmented generation and code retrieval:

## Graph Retrieval-Augmented Generation (GraphRAG) Surveys (2024)

Graph Retrieval-Augmented Generation: A Survey by Boci Peng and colleagues was published in September 2024 on arXiv, providing a comprehensive review of GraphRAG systems. GraphRAG leverages structural information across entities to enable more precise and comprehensive retrieval, capturing relational knowledge and facilitating more accurate, context-aware responses.

## Code-Specific Graph RAG (CodeGRAG)

For code retrieval specifically, CodeGRAG (2024) extracts and summarizes control flow and data flow information from code blocks to create a composed syntax graph that serves as a bridge between natural language and various programming languages. The approach combines Abstract Syntax Tree (AST), Data Flow Graph (DFG), and Control Flow Graph (CFG) information.

If you're looking for a specific paper called "RANGER," it's possible it may use a different title or acronym. Would you like me to search more specifically for this paper, or would you like more information about the GraphRAG and code retrieval papers I found?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d5364903-a4a1-4087-97e3-e23bdd6044c8",
  "uuid": "55b589d9-f058-4d19-a4b7-d5e3dfd71d9a",
  "tool_use_result": {
    "query": "RANGER retrieval augmented graph code retrieval 2024 paper",
    "results": [
      {
        "tool_use_id": "srvtoolu_01YVj6QQCJS9tSURQsa5D9Tz",
        "content": [
          {
            "title": "[2501.00309] Retrieval-Augmented Generation with Graphs (GraphRAG)",
            "url": "https://arxiv.org/abs/2501.00309"
          },
          {
            "title": "Graph Retrieval-Augmented Generation: A Survey | ACM Transactions on Information Systems",
            "url": "https://dl.acm.org/doi/10.1145/3777378"
          },
          {
            "title": "[2408.08921] Graph Retrieval-Augmented Generation: A Survey",
            "url": "https://arxiv.org/abs/2408.08921"
          },
          {
            "title": "Graph Retrieval-Augmented Generation: A Survey",
            "url": "https://arxiv.org/pdf/2408.08921"
          },
          {
            "title": "Retrieval Augmented Generation Research: 2017-2024",
            "url": "https://scalingknowledge.substack.com/p/rag"
          },
          {
            "title": "A Survey of Graph Retrieval-Augmented Generation for ...",
            "url": "https://openreview.net/pdf?id=9FJiOMuZkr"
          },
          {
            "title": "GitHub - Graph-RAG/GraphRAG · GitHub",
            "url": "https://github.com/Graph-RAG/GraphRAG"
          },
          {
            "title": "GitHub - DEEP-PolyU/Awesome-GraphRAG: Awesome-GraphRAG: A curated list of resources (surveys, papers, benchmarks, and opensource projects) on graph-based retrieval-augmented generation. · GitHub",
            "url": "https://github.com/DEEP-PolyU/Awesome-GraphRAG"
          },
          {
            "title": "G-Retriever: Retrieval-Augmented Generation for Textual Graph Understanding and Question Answering",
            "url": "https://proceedings.neurips.cc//paper_files/paper/2024/hash/efaf1c9726648c8ba363a5c927440529-Abstract-Conference.html"
          },
          {
            "title": "GitHub - XiaoxinHe/G-Retriever: Official Implementation of NeurIPS 2024 paper \"G-Retriever: Retrieval-Augmented Generation for Textual Graph Understanding and Question Answering\"\" · GitHub",
            "url": "https://github.com/XiaoxinHe/G-Retriever"
          }
        ]
      },
      "Based on the search results, I found information about retrieval-augmented generation with graphs and code retrieval, though I didn't find a paper specifically titled \"RANGER\" in the 2024 papers. However, I found several highly relevant 2024 papers on graph-based retrieval-augmented generation and code retrieval:\n\n## Graph Retrieval-Augmented Generation (GraphRAG) Surveys (2024)\n\nGraph Retrieval-Augmented Generation: A Survey by Boci Peng and colleagues was published in September 2024 on arXiv, providing a comprehensive review of GraphRAG systems. GraphRAG leverages structural information across entities to enable more precise and comprehensive retrieval, capturing relational knowledge and facilitating more accurate, context-aware responses.\n\n## Code-Specific Graph RAG (CodeGRAG)\n\nFor code retrieval specifically, CodeGRAG (2024) extracts and summarizes control flow and data flow information from code blocks to create a composed syntax graph that serves as a bridge between natural language and various programming languages. The approach combines Abstract Syntax Tree (AST), Data Flow Graph (DFG), and Control Flow Graph (CFG) information.\n\nIf you're looking for a specific paper called \"RANGER,\" it's possible it may use a different title or acronym. Would you like me to search more specifically for this paper, or would you like more information about the GraphRAG and code retrieval papers I found?"
    ],
    "durationSeconds": 6.189829700000119
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-13T21:45:58.471Z_

<details><summary>↩ Tool result · `toolu_01GjLMuidnpg9yxC6jGWVya1`</summary>

```text
Web search results for query: "LocAgent fault localization graph-based agent code 2024 2025 paper"

Links: [{"title":"GitHub - gersteinlab/LocAgent: [ACL 2025] Graph-guided agentic framework for code localization https://arxiv.org/abs/2503.09089 · GitHub","url":"https://github.com/gersteinlab/LocAgent"},{"title":"LocAgent: Graph-Guided LLM Agents for Code Localization","url":"https://arxiv.org/pdf/2503.09089"},{"title":"[2503.09089] LocAgent: Graph-Guided LLM Agents for Code Localization","url":"https://arxiv.org/abs/2503.09089"},{"title":"LocAgent: Graph-Guided LLM Agents for Code Localization - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.426/"},{"title":"LocAgent: Graph-Guided LLM Agents for Code Localization","url":"https://aclanthology.org/2025.acl-long.426.pdf"},{"title":"(PDF) LocAgent: Graph-Guided LLM Agents for Code Localization","url":"https://www.researchgate.net/publication/389786036_LocAgent_Graph-Guided_LLM_Agents_for_Code_Localization"},{"title":"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/html/2605.03117"},{"title":"Paper page - LocAgent: Graph-Guided LLM Agents for Code Localization","url":"https://huggingface.co/papers/2503.09089"},{"title":"LocAgent: Graph-Guided LLM Agents for Code Localization | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/locagent-graph-guided-llm-agents-code-localization"},{"title":"A Multi-Agent Approach to Fault Localization via Graph-Based Retrieval and Reflexion","url":"https://arxiv.org/html/2409.13642v2"}]

I found relevant information about LocAgent. Here's what I found:

## LocAgent: Graph-Guided LLM Agents for Code Localization

LocAgent is a framework that addresses code localization through graph-based representation. By parsing codebases into directed heterogeneous graphs, LocAgent creates a lightweight representation that captures code structures and their dependencies, enabling LLM agents to effectively search and locate relevant entities through powerful multi-hop reasoning.

### Publication Details
The paper was published as "LocAgent: Graph-Guided LLM Agents for Code Localization" in the Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 8697–8727, Vienna, Austria in 2025.

### Performance Results
The fine-tuned Qwen-2.5-Coder-Instruct-32B model achieves comparable results to state-of-the-art proprietary models at greatly reduced cost (approximately 86% reduction), reaching up to 92.7% accuracy on file-level localization while improving downstream GitHub issue resolution success rates by 12% for multiple attempts (Pass@10).

### Resources
The code is available at https://github.com/gersteinlab/LocAgent, and the paper is available on arXiv as paper 2503.09089.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d5364903-a4a1-4087-97e3-e23bdd6044c8",
  "uuid": "d032e4df-3373-4885-9401-8306d909ad15",
  "tool_use_result": {
    "query": "LocAgent fault localization graph-based agent code 2024 2025 paper",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GNqU2pgJ9A8RakWkcdZkft",
        "content": [
          {
            "title": "GitHub - gersteinlab/LocAgent: [ACL 2025] Graph-guided agentic framework for code localization https://arxiv.org/abs/2503.09089 · GitHub",
            "url": "https://github.com/gersteinlab/LocAgent"
          },
          {
            "title": "LocAgent: Graph-Guided LLM Agents for Code Localization",
            "url": "https://arxiv.org/pdf/2503.09089"
          },
          {
            "title": "[2503.09089] LocAgent: Graph-Guided LLM Agents for Code Localization",
            "url": "https://arxiv.org/abs/2503.09089"
          },
          {
            "title": "LocAgent: Graph-Guided LLM Agents for Code Localization - ACL Anthology",
            "url": "https://aclanthology.org/2025.acl-long.426/"
          },
          {
            "title": "LocAgent: Graph-Guided LLM Agents for Code Localization",
            "url": "https://aclanthology.org/2025.acl-long.426.pdf"
          },
          {
            "title": "(PDF) LocAgent: Graph-Guided LLM Agents for Code Localization",
            "url": "https://www.researchgate.net/publication/389786036_LocAgent_Graph-Guided_LLM_Agents_for_Code_Localization"
          },
          {
            "title": "ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair",
            "url": "https://arxiv.org/html/2605.03117"
          },
          {
            "title": "Paper page - LocAgent: Graph-Guided LLM Agents for Code Localization",
            "url": "https://huggingface.co/papers/2503.09089"
          },
          {
            "title": "LocAgent: Graph-Guided LLM Agents for Code Localization | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/locagent-graph-guided-llm-agents-code-localization"
          },
          {
            "title": "A Multi-Agent Approach to Fault Localization via Graph-Based Retrieval and Reflexion",
            "url": "https://arxiv.org/html/2409.13642v2"
          }
        ]
      },
      "I found relevant information about LocAgent. Here's what I found:\n\n## LocAgent: Graph-Guided LLM Agents for Code Localization\n\nLocAgent is a framework that addresses code localization through graph-based representation. By parsing codebases into directed heterogeneous graphs, LocAgent creates a lightweight representation that captures code structures and their dependencies, enabling LLM agents to effectively search and locate relevant entities through powerful multi-hop reasoning.\n\n### Publication Details\nThe paper was published as \"LocAgent: Graph-Guided LLM Agents for Code Localization\" in the Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 8697–8727, Vienna, Austria in 2025.\n\n### Performance Results\nThe fine-tuned Qwen-2.5-Coder-Instruct-32B model achieves comparable results to state-of-the-art proprietary models at greatly reduced cost (approximately 86% reduction), reaching up to 92.7% accuracy on file-level localization while improving downstream GitHub issue resolution success rates by 12% for multiple attempts (Pass@10).\n\n### Resources\nThe code is available at https://github.com/gersteinlab/LocAgent, and the paper is available on arXiv as paper 2503.09089."
    ],
    "durationSeconds": 6.446974723000079
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-13T21:45:58.977Z_

<details><summary>↩ Tool result · `toolu_0184yqwDh36T8u4Afw9hpKwt`</summary>

```text
Web search results for query: "CodexGraph code graph LLM agent repository-level coding 2024 paper"

Links: [{"title":"[2408.03910] CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases","url":"https://arxiv.org/abs/2408.03910"},{"title":"CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases","url":"https://arxiv.org/html/2408.03910v2"},{"title":"CODEXGRAPH: Bridging Large Language Models and ...","url":"https://aclanthology.org/2025.naacl-long.7.pdf"},{"title":"CODEXGRAPH: Bridging Large Language Models and Code Repositories","url":"https://openreview.net/pdf/165bbc76cbb447f2ea74ed1b1a4bb3531ee87e6d.pdf"},{"title":"CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240803910L/abstract"},{"title":"CodexGraph","url":"https://laptype.github.io/CodexGraph-page/"},{"title":"Paper page - CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases","url":"https://huggingface.co/papers/2408.03910"},{"title":"CODEXGRAPH: Bridging Large Language Models","url":"https://arxiv.org/pdf/2408.03910v2"},{"title":"GitHub - YerbaPage/Awesome-Repo-Level-Code-Generation: Must-read papers on Repository-level Code Generation & Issue Resolution 🔥","url":"https://github.com/YerbaPage/Awesome-Repo-Level-Code-Generation"},{"title":"[PDF] CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CodexGraph:-Bridging-Large-Language-Models-and-Code-Liu-Lan/514e4e91e0fbddaa85857760d4f206a18228d614"}]

Based on the search results, I found comprehensive information about the CodexGraph paper. Here's what I found:

## CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases

CodexGraph is a system that integrates LLM agents with graph database interfaces extracted from code repositories, enabling the LLM agent to construct and execute queries for precise, code structure-aware context retrieval and code navigation.

### Problem Statement

While Large Language Models excel in stand-alone code tasks like HumanEval and MBPP, they struggle with handling entire code repositories, prompting research on enhancing LLM-codebase interaction at a repository scale. Current solutions rely on similarity-based retrieval or manual tools and APIs, with similarity-based retrieval often having low recall in complex tasks, while manual tools and APIs are typically task-specific and require expert knowledge.

### Technical Approach

CodexGraph utilizes static analysis to extract code graphs from repositories using a task-agnostic schema that defines nodes and edges, where nodes represent source code symbols such as MODULE, CLASS, and FUNCTION, and edges represent relationships among these symbols, such as CONTAINS, INHERITS, and USES.

### Evaluation

The system was assessed using three benchmarks: CrossCodeEval, SWE-bench, and EvoCodeBench, with five real-world coding applications developed, demonstrating competitive performance with a unified graph database schema in both academic and real-world environments.

**Paper Details:** The paper was submitted to arXiv on August 7, 2024 (arXiv:2408.03910) and was later accepted to the 2025 NAACL conference.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d5364903-a4a1-4087-97e3-e23bdd6044c8",
  "uuid": "fd875fd4-23ad-4cb8-bdf0-37d5483b1f3e",
  "tool_use_result": {
    "query": "CodexGraph code graph LLM agent repository-level coding 2024 paper",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RCP75HmpNgFv3LxVWPXRgK",
        "content": [
          {
            "title": "[2408.03910] CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases",
            "url": "https://arxiv.org/abs/2408.03910"
          },
          {
            "title": "CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases",
            "url": "https://arxiv.org/html/2408.03910v2"
          },
          {
            "title": "CODEXGRAPH: Bridging Large Language Models and ...",
            "url": "https://aclanthology.org/2025.naacl-long.7.pdf"
          },
          {
            "title": "CODEXGRAPH: Bridging Large Language Models and Code Repositories",
            "url": "https://openreview.net/pdf/165bbc76cbb447f2ea74ed1b1a4bb3531ee87e6d.pdf"
          },
          {
            "title": "CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2024arXiv240803910L/abstract"
          },
          {
            "title": "CodexGraph",
            "url": "https://laptype.github.io/CodexGraph-page/"
          },
          {
            "title": "Paper page - CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases",
            "url": "https://huggingface.co/papers/2408.03910"
          },
          {
            "title": "CODEXGRAPH: Bridging Large Language Models",
            "url": "https://arxiv.org/pdf/2408.03910v2"
          },
          {
            "title": "GitHub - YerbaPage/Awesome-Repo-Level-Code-Generation: Must-read papers on Repository-level Code Generation & Issue Resolution 🔥",
            "url": "https://github.com/YerbaPage/Awesome-Repo-Level-Code-Generation"
          },
          {
            "title": "[PDF] CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/CodexGraph:-Bridging-Large-Language-Models-and-Code-Liu-Lan/514e4e91e0fbddaa85857760d4f206a18228d614"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about the CodexGraph paper. Here's what I found:\n\n## CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases\n\nCodexGraph is a system that integrates LLM agents with graph database interfaces extracted from code repositories, enabling the LLM agent to construct and execute queries for precise, code structure-aware context retrieval and code navigation.\n\n### Problem Statement\n\nWhile Large Language Models excel in stand-alone code tasks like HumanEval and MBPP, they struggle with handling entire code repositories, prompting research on enhancing LLM-codebase interaction at a repository scale. Current solutions rely on similarity-based retrieval or manual tools and APIs, with similarity-based retrieval often having low recall in complex tasks, while manual tools and APIs are typically task-specific and require expert knowledge.\n\n### Technical Approach\n\nCodexGraph utilizes static analysis to extract code graphs from repositories using a task-agnostic schema that defines nodes and edges, where nodes represent source code symbols such as MODULE, CLASS, and FUNCTION, and edges represent relationships among these symbols, such as CONTAINS, INHERITS, and USES.\n\n### Evaluation\n\nThe system was assessed using three benchmarks: CrossCodeEval, SWE-bench, and EvoCodeBench, with five real-world coding applications developed, demonstrating competitive performance with a unified graph database schema in both academic and real-world environments.\n\n**Paper Details:** The paper was submitted to arXiv on August 7, 2024 (arXiv:2408.03910) and was later accepted to the 2025 NAACL conference."
    ],
    "durationSeconds": 7.440040400000056
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018pZ8FyyC7gw2Guqt9RSem7`</summary>

```json
{
  "query": "RepoGraph repository-level graph code understanding 2024 paper arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d5364903-a4a1-4087-97e3-e23bdd6044c8",
  "uuid": "d9b171d2-2612-4d9c-8b78-7646d7b0816f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VHJiFQS3KDXPWShJfaUNWb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1814,
      "cache_creation_input_tokens": 1163,
      "cache_read_input_tokens": 24668,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1163
      },
      "output_tokens": 38,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PsSbUtEQYqByuMhLs6a8r9`</summary>

```json
{
  "query": "GraphCoder graph-based code retrieval generation 2024 paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d5364903-a4a1-4087-97e3-e23bdd6044c8",
  "uuid": "3d1077bf-5fa1-46bc-8bcb-0ce89feca740",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VHJiFQS3KDXPWShJfaUNWb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1814,
      "cache_creation_input_tokens": 1163,
      "cache_read_input_tokens": 24668,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1163
      },
      "output_tokens": 38,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017eJMoXkKF8WyTx1Fi2PBUv`</summary>

```json
{
  "query": "RANGER code retrieval graph neural network repository 2024 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d5364903-a4a1-4087-97e3-e23bdd6044c8",
  "uuid": "540f4730-2a62-4c07-9c4b-fefc865a9869",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VHJiFQS3KDXPWShJfaUNWb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1814,
      "cache_creation_input_tokens": 1163,
      "cache_read_input_tokens": 24668,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1163
      },
      "output_tokens": 38,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-13T21:46:08.556Z_

<details><summary>↩ Tool result · `toolu_018pZ8FyyC7gw2Guqt9RSem7`</summary>

```text
Web search results for query: "RepoGraph repository-level graph code understanding 2024 paper arXiv"

Links: [{"title":"[2410.14684] RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph","url":"https://arxiv.org/abs/2410.14684"},{"title":"RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph","url":"https://arxiv.org/html/2410.14684v2"},{"title":"Enhancing Repository-Level Software Repair via Repository-Aware Knowledge Graphs","url":"https://arxiv.org/html/2503.21710v1"},{"title":"GitHub - YerbaPage/Awesome-Repo-Level-Code-Generation: Must-read papers on Repository-level Code Generation & Issue Resolution 🔥","url":"https://github.com/YerbaPage/Awesome-Repo-Level-Code-Generation"},{"title":"RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/repograph-enhancing-ai-software-engineering-repository-level"},{"title":"(PDF) RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph","url":"https://www.researchgate.net/publication/385108343_RepoGraph_Enhancing_AI_Software_Engineering_with_Repository-level_Code_Graph"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/4a4a3c197deac042461c677219efd36c-Paper-Conference.pdf"},{"title":"RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph | OpenReview","url":"https://openreview.net/forum?id=dw9VUsSHGB"},{"title":"Knowledge Graph Based Repository-Level Code Generation","url":"https://arxiv.org/html/2505.14394v1"},{"title":"Paper page - RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph","url":"https://huggingface.co/papers/2410.14684"}]

I found the RepoGraph paper for you. Here are the key details:

## Paper Overview

**RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph** is a 2024 paper available on arXiv as paper 2410.14684.

## What is RepoGraph?

RepoGraph is a plug-in module that manages a repository-level structure for modern AI software engineering solutions and offers guidance and repository-wide navigation for AI software engineers.

## Key Motivation

Large Language Models (LLMs) excel in code generation yet struggle with modern AI software engineering tasks. Unlike traditional function-level or file-level coding tasks, AI software engineering requires not only basic coding proficiency but also advanced skills in managing and interacting with code repositories. However, existing methods often overlook the need for repository-level code understanding, which is crucial for accurately grasping the broader context and developing effective solutions.

## Evaluation Results

RepoGraph was evaluated on the SWE-bench by plugging it into four different methods of two lines of approaches, where RepoGraph substantially boosts the performance of all systems, leading to a new state-of-the-art among open-source frameworks. The analyses also demonstrate the extensibility and flexibility of RepoGraph by testing on another repo-level coding benchmark, CrossCodeEval.

## Availability

The code is available at https://github.com/ozyyshr/RepoGraph.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d5364903-a4a1-4087-97e3-e23bdd6044c8",
  "uuid": "a20684d8-469b-40dc-98bb-76be5cca4505",
  "tool_use_result": {
    "query": "RepoGraph repository-level graph code understanding 2024 paper arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01N5cQq3HYZrDFMN4N837D8j",
        "content": [
          {
            "title": "[2410.14684] RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph",
            "url": "https://arxiv.org/abs/2410.14684"
          },
          {
            "title": "RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph",
            "url": "https://arxiv.org/html/2410.14684v2"
          },
          {
            "title": "Enhancing Repository-Level Software Repair via Repository-Aware Knowledge Graphs",
            "url": "https://arxiv.org/html/2503.21710v1"
          },
          {
            "title": "GitHub - YerbaPage/Awesome-Repo-Level-Code-Generation: Must-read papers on Repository-level Code Generation & Issue Resolution 🔥",
            "url": "https://github.com/YerbaPage/Awesome-Repo-Level-Code-Generation"
          },
          {
            "title": "RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/repograph-enhancing-ai-software-engineering-repository-level"
          },
          {
            "title": "(PDF) RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph",
            "url": "https://www.researchgate.net/publication/385108343_RepoGraph_Enhancing_AI_Software_Engineering_with_Repository-level_Code_Graph"
          },
          {
            "title": "Published as a conference paper at ICLR 2025",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/4a4a3c197deac042461c677219efd36c-Paper-Conference.pdf"
          },
          {
            "title": "RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph | OpenReview",
            "url": "https://openreview.net/forum?id=dw9VUsSHGB"
          },
          {
            "title": "Knowledge Graph Based Repository-Level Code Generation",
            "url": "https://arxiv.org/html/2505.14394v1"
          },
          {
            "title": "Paper page - RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph",
            "url": "https://huggingface.co/papers/2410.14684"
          }
        ]
      },
      "I found the RepoGraph paper for you. Here are the key details:\n\n## Paper Overview\n\n**RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph** is a 2024 paper available on arXiv as paper 2410.14684.\n\n## What is RepoGraph?\n\nRepoGraph is a plug-in module that manages a repository-level structure for modern AI software engineering solutions and offers guidance and repository-wide navigation for AI software engineers.\n\n## Key Motivation\n\nLarge Language Models (LLMs) excel in code generation yet struggle with modern AI software engineering tasks. Unlike traditional function-level or file-level coding tasks, AI software engineering requires not only basic coding proficiency but also advanced skills in managing and interacting with code repositories. However, existing methods often overlook the need for repository-level code understanding, which is crucial for accurately grasping the broader context and developing effective solutions.\n\n## Evaluation Results\n\nRepoGraph was evaluated on the SWE-bench by plugging it into four different methods of two lines of approaches, where RepoGraph substantially boosts the performance of all systems, leading to a new state-of-the-art among open-source frameworks. The analyses also demonstrate the extensibility and flexibility of RepoGraph by testing on another repo-level coding benchmark, CrossCodeEval.\n\n## Availability\n\nThe code is available at https://github.com/ozyyshr/RepoGraph."
    ],
    "durationSeconds": 5.081995344999945
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-13T21:46:09.344Z_

<details><summary>↩ Tool result · `toolu_01PsSbUtEQYqByuMhLs6a8r9`</summary>

```text
Web search results for query: "GraphCoder graph-based code retrieval generation 2024 paper"

Links: [{"title":"GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph | Proceedings of the 39th IEEE/ACM International Conference on Automated Software Engineering","url":"https://dl.acm.org/doi/10.1145/3691620.3695054"},{"title":"[2406.07003] GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model","url":"https://arxiv.org/abs/2406.07003"},{"title":"GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph (ASE 2024 - Research Papers) - ASE 2024","url":"https://conf.researchr.org/details/ase-2024/ase-2024-research/46/GraphCoder-Enhancing-Repository-Level-Code-Completion-via-Coarse-to-fine-Retrieval-B"},{"title":"GitHub - DEEP-PolyU/Awesome-GraphRAG: Awesome-GraphRAG: A curated list of resources (surveys, papers, benchmarks, and opensource projects) on graph-based retrieval-augmented generation. · GitHub","url":"https://github.com/DEEP-PolyU/Awesome-GraphRAG"},{"title":"[PDF] GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model | Semantic Scholar","url":"https://www.semanticscholar.org/paper/GraphCoder:-Enhancing-Repository-Level-Code-via-and-Liu-Yu/793bbb3c70d4bac3908bd8f2ecc309f1bfdf5f52"},{"title":"GitHub - oceaneLIU/GraphCoder","url":"https://github.com/oceaneLIU/GraphCoder"},{"title":"GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph | Request PDF","url":"https://www.researchgate.net/publication/385287286_GraphCoder_Enhancing_Repository-Level_Code_Completion_via_Coarse-to-fine_Retrieval_Based_on_Code_Context_Graph"},{"title":"[2501.00309] Retrieval-Augmented Generation with Graphs (GraphRAG)","url":"https://arxiv.org/abs/2501.00309"},{"title":"GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model","url":"https://arxiv.org/html/2406.07003v2"},{"title":"GitHub - YerbaPage/Awesome-Repo-Level-Code-Generation: Must-read papers on Repository-level Code Generation & Issue Resolution 🔥","url":"https://github.com/YerbaPage/Awesome-Repo-Level-Code-Generation"}]

Based on the search results, here's what I found about the GraphCoder paper:

## Overview

GraphCoder is a retrieval-augmented code completion framework that leverages LLMs' general code knowledge and repository-specific knowledge via a graph-based retrieval-generation process.

## Key Technical Approach

GraphCoder captures the context of completion target through a code context graph (CCG) that consists of control-flow, data- and control-dependence between code statements, and employs a coarse-to-fine retrieval process to locate context-similar code snippets with the completion target from the current repository.

## Performance Results

Compared to baseline retrieval-augmented methods, GraphCoder achieves higher exact match (EM) on average, with increases of +6.06 in code match and +6.23 in identifier match, while using less time and space.

## Publication

The paper was published on arXiv on June 11, 2024, and was presented at ASE 2024 (the 39th IEEE/ACM International Conference on Automated Software Engineering). The code and data are available on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d5364903-a4a1-4087-97e3-e23bdd6044c8",
  "uuid": "7967c7df-ec00-4aed-8276-54ed3b5b0688",
  "tool_use_result": {
    "query": "GraphCoder graph-based code retrieval generation 2024 paper",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NRxzB2FGcaDw3A2BVo4dVe",
        "content": [
          {
            "title": "GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph | Proceedings of the 39th IEEE/ACM International Conference on Automated Software Engineering",
            "url": "https://dl.acm.org/doi/10.1145/3691620.3695054"
          },
          {
            "title": "[2406.07003] GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model",
            "url": "https://arxiv.org/abs/2406.07003"
          },
          {
            "title": "GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph (ASE 2024 - Research Papers) - ASE 2024",
            "url": "https://conf.researchr.org/details/ase-2024/ase-2024-research/46/GraphCoder-Enhancing-Repository-Level-Code-Completion-via-Coarse-to-fine-Retrieval-B"
          },
          {
            "title": "GitHub - DEEP-PolyU/Awesome-GraphRAG: Awesome-GraphRAG: A curated list of resources (surveys, papers, benchmarks, and opensource projects) on graph-based retrieval-augmented generation. · GitHub",
            "url": "https://github.com/DEEP-PolyU/Awesome-GraphRAG"
          },
          {
            "title": "[PDF] GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/GraphCoder:-Enhancing-Repository-Level-Code-via-and-Liu-Yu/793bbb3c70d4bac3908bd8f2ecc309f1bfdf5f52"
          },
          {
            "title": "GitHub - oceaneLIU/GraphCoder",
            "url": "https://github.com/oceaneLIU/GraphCoder"
          },
          {
            "title": "GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph | Request PDF",
            "url": "https://www.researchgate.net/publication/385287286_GraphCoder_Enhancing_Repository-Level_Code_Completion_via_Coarse-to-fine_Retrieval_Based_on_Code_Context_Graph"
          },
          {
            "title": "[2501.00309] Retrieval-Augmented Generation with Graphs (GraphRAG)",
            "url": "https://arxiv.org/abs/2501.00309"
          },
          {
            "title": "GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model",
            "url": "https://arxiv.org/html/2406.07003v2"
          },
          {
            "title": "GitHub - YerbaPage/Awesome-Repo-Level-Code-Generation: Must-read papers on Repository-level Code Generation & Issue Resolution 🔥",
            "url": "https://github.com/YerbaPage/Awesome-Repo-Level-Code-Generation"
          }
        ]
      },
      "Based on the search results, here's what I found about the GraphCoder paper:\n\n## Overview\n\nGraphCoder is a retrieval-augmented code completion framework that leverages LLMs' general code knowledge and repository-specific knowledge via a graph-based retrieval-generation process.\n\n## Key Technical Approach\n\nGraphCoder captures the context of completion target through a code context graph (CCG) that consists of control-flow, data- and control-dependence between code statements, and employs a coarse-to-fine retrieval process to locate context-similar code snippets with the completion target from the current repository.\n\n## Performance Results\n\nCompared to baseline retrieval-augmented methods, GraphCoder achieves higher exact match (EM) on average, with increases of +6.06 in code match and +6.23 in identifier match, while using less time and space.\n\n## Publication\n\nThe paper was published on arXiv on June 11, 2024, and was presented at ASE 2024 (the 39th IEEE/ACM International Conference on Automated Software Engineering). The code and data are available on GitHub."
    ],
    "durationSeconds": 5.724386216999963
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-13T21:46:11.149Z_

<details><summary>↩ Tool result · `toolu_017eJMoXkKF8WyTx1Fi2PBUv`</summary>

```text
Web search results for query: "RANGER code retrieval graph neural network repository 2024 arXiv"

Links: [{"title":"RANGER -- Repository-Level Agent for Graph-Enhanced ...","url":"https://arxiv.org/pdf/2509.25257"},{"title":"[2509.25257] RANGER -- Repository-Level Agent for Graph-Enhanced Retrieval","url":"https://arxiv.org/abs/2509.25257"},{"title":"RANGER: Repository‑level Agent for Graph‑Enhanced Retrieval","url":"https://arxiv.org/html/2509.25257v1"},{"title":"CodeRAG: Supportive Code Retrieval on Bigraph for Real-World Code Generation","url":"https://arxiv.org/html/2504.10046v1"},{"title":"Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches","url":"https://arxiv.org/html/2510.04905v1"},{"title":"Gnn-Rag: Graph Neural Retrieval for Large Language Model Reasoning","url":"https://arxiv.org/html/2405.20139v1"},{"title":"[2501.00309] Retrieval-Augmented Generation with Graphs (GraphRAG)","url":"https://arxiv.org/abs/2501.00309"},{"title":"[2405.20139] GNN-RAG: Graph Neural Retrieval for Large Language Model Reasoning","url":"https://arxiv.org/abs/2405.20139"},{"title":"[2406.06572] Graph Neural Network Enhanced Retrieval for Question Answering of LLMs","url":"https://arxiv.org/abs/2406.06572"},{"title":"Repository-level Code Search with Neural Retrieval Methods","url":"https://arxiv.org/html/2502.07067"}]

I found relevant information about RANGER. Here are the key results:

## RANGER: Repository-Level Agent for Graph-Enhanced Retrieval

RANGER is a repository-level code retrieval agent designed to address both code-entity queries and natural language queries. The paper is titled "RANGER -- Repository-Level Agent for Graph-Enhanced Retrieval" and was posted on arXiv on September 27, 2025 (arXiv:2509.25257).

### Key Features:

The system includes an efficient knowledge graph construction procedure together with a Monte Carlo Tree Search (MCTS)-based graph traversal algorithm. RANGER operates on this graph through a dual-stage retrieval pipeline where entity-based queries are answered through fast Cypher lookups, while natural language queries are handled by MCTS-guided graph exploration.

### Evaluation:

RANGER was evaluated across four diverse benchmarks that represent core ASE tasks including code search, question answering, cross-file dependency retrieval, and repository-level code completion. On CodeSearchNet and RepoQA it outperforms retrieval baselines that use embeddings from strong models such as Qwen3-8B. On RepoBench, it achieves superior cross-file dependency retrieval over baselines, and on CrossCodeEval, pairing RANGER with BM25 delivers the highest exact match rate in code completion compared to other RAG methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d5364903-a4a1-4087-97e3-e23bdd6044c8",
  "uuid": "9556b523-648e-419c-9da8-fc0834110ea1",
  "tool_use_result": {
    "query": "RANGER code retrieval graph neural network repository 2024 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VfMzNJwoJeQ4zduFXCBy9N",
        "content": [
          {
            "title": "RANGER -- Repository-Level Agent for Graph-Enhanced ...",
            "url": "https://arxiv.org/pdf/2509.25257"
          },
          {
            "title": "[2509.25257] RANGER -- Repository-Level Agent for Graph-Enhanced Retrieval",
            "url": "https://arxiv.org/abs/2509.25257"
          },
          {
            "title": "RANGER: Repository‑level Agent for Graph‑Enhanced Retrieval",
            "url": "https://arxiv.org/html/2509.25257v1"
          },
          {
            "title": "CodeRAG: Supportive Code Retrieval on Bigraph for Real-World Code Generation",
            "url": "https://arxiv.org/html/2504.10046v1"
          },
          {
            "title": "Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches",
            "url": "https://arxiv.org/html/2510.04905v1"
          },
          {
            "title": "Gnn-Rag: Graph Neural Retrieval for Large Language Model Reasoning",
            "url": "https://arxiv.org/html/2405.20139v1"
          },
          {
            "title": "[2501.00309] Retrieval-Augmented Generation with Graphs (GraphRAG)",
            "url": "https://arxiv.org/abs/2501.00309"
          },
          {
            "title": "[2405.20139] GNN-RAG: Graph Neural Retrieval for Large Language Model Reasoning",
            "url": "https://arxiv.org/abs/2405.20139"
          },
          {
            "title": "[2406.06572] Graph Neural Network Enhanced Retrieval for Question Answering of LLMs",
            "url": "https://arxiv.org/abs/2406.06572"
          },
          {
            "title": "Repository-level Code Search with Neural Retrieval Methods",
            "url": "https://arxiv.org/html/2502.07067"
          }
        ]
      },
      "I found relevant information about RANGER. Here are the key results:\n\n## RANGER: Repository-Level Agent for Graph-Enhanced Retrieval\n\nRANGER is a repository-level code retrieval agent designed to address both code-entity queries and natural language queries. The paper is titled \"RANGER -- Repository-Level Agent for Graph-Enhanced Retrieval\" and was posted on arXiv on September 27, 2025 (arXiv:2509.25257).\n\n### Key Features:\n\nThe system includes an efficient knowledge graph construction procedure together with a Monte Carlo Tree Search (MCTS)-based graph traversal algorithm. RANGER operates on this graph through a dual-stage retrieval pipeline where entity-based queries are answered through fast Cypher lookups, while natural language queries are handled by MCTS-guided graph exploration.\n\n### Evaluation:\n\nRANGER was evaluated across four diverse benchmarks that represent core ASE tasks including code search, question answering, cross-file dependency retrieval, and repository-level code completion. On CodeSearchNet and RepoQA it outperforms retrieval baselines that use embeddings from strong models such as Qwen3-8B. On RepoBench, it achieves superior cross-file dependency retrieval over baselines, and on CrossCodeEval, pairing RANGER with BM25 delivers the highest exact match rate in code completion compared to other RAG methods."
    ],
    "durationSeconds": 7.026503458000021
  }
}
```

</details>

---

### Assistant

_source line 20_

<details><summary>Logged reasoning block</summary>

```text
Good, I found all the main papers. Let me now search for a few more related methods to have a comprehensive survey. Let me also search for more details on some of these papers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d5364903-a4a1-4087-97e3-e23bdd6044c8",
  "uuid": "9a480e8f-d9af-49b7-8315-b0982637e087",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018khTSC3rq9j69AqCuumnSG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4699,
      "cache_read_input_tokens": 25831,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4699
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 21_

找到了所有主要论文。再搜索一些补充信息和额外相关方法。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d5364903-a4a1-4087-97e3-e23bdd6044c8",
  "uuid": "25236981-7e1b-4ac3-852a-ed78d3b34e57",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018khTSC3rq9j69AqCuumnSG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4699,
      "cache_read_input_tokens": 25831,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4699
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EXVgAaetZi8CSHbJ8jV4Hp`</summary>

```json
{
  "query": "CodeRAG code retrieval graph bigraph repository-level 2025 paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d5364903-a4a1-4087-97e3-e23bdd6044c8",
  "uuid": "aa8f7f8c-f8c9-4e78-9070-b3eace815e67",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018khTSC3rq9j69AqCuumnSG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4699,
      "cache_read_input_tokens": 25831,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4699
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018sKD5iDriv6PnLBsPf6JEi`</summary>

```json
{
  "query": "ARISE repository graph agentic fault localization program repair 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d5364903-a4a1-4087-97e3-e23bdd6044c8",
  "uuid": "77555ff7-33a9-4e15-9587-4f08f63ca5ba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018khTSC3rq9j69AqCuumnSG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4699,
      "cache_read_input_tokens": 25831,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4699
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01C65xpX2J33X44XeVFbf6dW`</summary>

```json
{
  "query": "GraphCoder code context graph control flow data dependence details ASE 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d5364903-a4a1-4087-97e3-e23bdd6044c8",
  "uuid": "567b8953-1907-4fb0-881f-c3066e990565",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018khTSC3rq9j69AqCuumnSG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4699,
      "cache_read_input_tokens": 25831,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4699
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-13T21:46:26.445Z_

<details><summary>↩ Tool result · `toolu_01EXVgAaetZi8CSHbJ8jV4Hp`</summary>

```text
Web search results for query: "CodeRAG code retrieval graph bigraph repository-level 2025 paper"

Links: [{"title":"CodeRAG: Supportive Code Retrieval on Bigraph for Real-World Code Generation","url":"https://arxiv.org/html/2504.10046v1"},{"title":"CodeRAG: Supportive Code Retrieval on Bigraph for Real-World Code Generation | Request PDF","url":"https://www.researchgate.net/publication/390772757_CodeRAG_Supportive_Code_Retrieval_on_Bigraph_for_Real-World_Code_Generation"},{"title":"[2504.10046v1] CodeRAG: Supportive Code Retrieval on Bigraph for Real-World Code Generation","url":"https://arxiv.org/abs/2504.10046v1"},{"title":"CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases","url":"https://www.researchgate.net/publication/392505894_CodexGraph_Bridging_Large_Language_Models_and_Code_Repositories_via_Code_Graph_Databases"},{"title":"CodeRAG: Supportive Code Retrieval on Bigraph for Real-World Code Generation | Scilit","url":"https://www.scilit.com/publications/f42dab08436be314eaa54e5785940d9b"},{"title":"[Literature Review] CodeRAG: Supportive Code Retrieval on Bigraph for Real-World Code Generation","url":"https://www.themoonlight.io/en/review/coderag-supportive-code-retrieval-on-bigraph-for-real-world-code-generation"},{"title":"GitHub - YerbaPage/Awesome-Repo-Level-Code-Generation: Must-read papers on Repository-level Code Generation & Issue Resolution 🔥","url":"https://github.com/YerbaPage/Awesome-Repo-Level-Code-Generation"},{"title":"CodeRAG: Finding Relevant and Necessary Knowledge ...","url":"https://aclanthology.org/2025.emnlp-main.1187.pdf"},{"title":"[PDF] GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model | Semantic Scholar","url":"https://www.semanticscholar.org/paper/GraphCoder:-Enhancing-Repository-Level-Code-via-and-Liu-Yu/793bbb3c70d4bac3908bd8f2ecc309f1bfdf5f52"},{"title":"CodeRAG: Finding Relevant and Necessary Knowledge for Retrieval-Augmented Repository-Level Code Completion","url":"https://arxiv.org/html/2509.16112"}]

Based on the search results, I found comprehensive information about CodeRAG. Here's what the research reveals:

## CodeRAG: Supportive Code Retrieval on Bigraph for Real-World Code Generation

CodeRAG is a retrieval-augmented code generation (RAG) framework to comprehensively retrieve supportive codes for real-world code generation.

### Key Approach

CodeRAG constructs a requirement graph for the current repository and retrieves relevant requirement nodes of the target requirement node. Meanwhile, it models a DS-code graph, and maps relevant requirement nodes into their corresponding code nodes, successfully finding supportive codes.

### Core Components

The framework has four main innovations:

1. **Requirement Graph Construction**: The framework begins by constructing a requirement graph for the current repository. The nodes in this graph represent functional descriptions (requirements) of functions or classes within the repository. Edges denote relationships between these requirements, such as parent-child or semantic similarity.

2. **DS-Code Graph Modeling**: Different from existing code graphs, DS-code graph not only models dependency relationships but also introduces semantic relationships among nodes.

3. **Bigraph Mapping**: CodeRAG maps the relevant requirement nodes (sub-requirements and similar requirements) from the requirement graph to corresponding code nodes in the DS-code graph. These mapped code nodes are then treated as "anchors" to guide LLM reasoning.

4. **Agentic Reasoning**: CodeRAG introduces an agentic process, which allows LLMs to adaptively adjust reasoning strategy and search for the supportive knowledge which LLMs need in repo-level code generation.

### Experimental Results

Experiments show that CodeRAG achieves significant improvements (i.e., increasing 40.90 and 37.79 Pass@1 on GPT-4o and Gemini-Pro on DevEval) compared to no RAG scenarios. Additionally, CodeRAG outperforms commercial programming products such as Copilit and Cursor, and demonstrates CodeRAG's potential in solving real-world repo-level coding challenges.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d5364903-a4a1-4087-97e3-e23bdd6044c8",
  "uuid": "9427c825-a544-448d-b4b7-fe43e49096f2",
  "tool_use_result": {
    "query": "CodeRAG code retrieval graph bigraph repository-level 2025 paper",
    "results": [
      {
        "tool_use_id": "srvtoolu_01D4LMNQA7AzpBuvADH6VCyT",
        "content": [
          {
            "title": "CodeRAG: Supportive Code Retrieval on Bigraph for Real-World Code Generation",
            "url": "https://arxiv.org/html/2504.10046v1"
          },
          {
            "title": "CodeRAG: Supportive Code Retrieval on Bigraph for Real-World Code Generation | Request PDF",
            "url": "https://www.researchgate.net/publication/390772757_CodeRAG_Supportive_Code_Retrieval_on_Bigraph_for_Real-World_Code_Generation"
          },
          {
            "title": "[2504.10046v1] CodeRAG: Supportive Code Retrieval on Bigraph for Real-World Code Generation",
            "url": "https://arxiv.org/abs/2504.10046v1"
          },
          {
            "title": "CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases",
            "url": "https://www.researchgate.net/publication/392505894_CodexGraph_Bridging_Large_Language_Models_and_Code_Repositories_via_Code_Graph_Databases"
          },
          {
            "title": "CodeRAG: Supportive Code Retrieval on Bigraph for Real-World Code Generation | Scilit",
            "url": "https://www.scilit.com/publications/f42dab08436be314eaa54e5785940d9b"
          },
          {
            "title": "[Literature Review] CodeRAG: Supportive Code Retrieval on Bigraph for Real-World Code Generation",
            "url": "https://www.themoonlight.io/en/review/coderag-supportive-code-retrieval-on-bigraph-for-real-world-code-generation"
          },
          {
            "title": "GitHub - YerbaPage/Awesome-Repo-Level-Code-Generation: Must-read papers on Repository-level Code Generation & Issue Resolution 🔥",
            "url": "https://github.com/YerbaPage/Awesome-Repo-Level-Code-Generation"
          },
          {
            "title": "CodeRAG: Finding Relevant and Necessary Knowledge ...",
            "url": "https://aclanthology.org/2025.emnlp-main.1187.pdf"
          },
          {
            "title": "[PDF] GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/GraphCoder:-Enhancing-Repository-Level-Code-via-and-Liu-Yu/793bbb3c70d4bac3908bd8f2ecc309f1bfdf5f52"
          },
          {
            "title": "CodeRAG: Finding Relevant and Necessary Knowledge for Retrieval-Augmented Repository-Level Code Completion",
            "url": "https://arxiv.org/html/2509.16112"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about CodeRAG. Here's what the research reveals:\n\n## CodeRAG: Supportive Code Retrieval on Bigraph for Real-World Code Generation\n\nCodeRAG is a retrieval-augmented code generation (RAG) framework to comprehensively retrieve supportive codes for real-world code generation.\n\n### Key Approach\n\nCodeRAG constructs a requirement graph for the current repository and retrieves relevant requirement nodes of the target requirement node. Meanwhile, it models a DS-code graph, and maps relevant requirement nodes into their corresponding code nodes, successfully finding supportive codes.\n\n### Core Components\n\nThe framework has four main innovations:\n\n1. **Requirement Graph Construction**: The framework begins by constructing a requirement graph for the current repository. The nodes in this graph represent functional descriptions (requirements) of functions or classes within the repository. Edges denote relationships between these requirements, such as parent-child or semantic similarity.\n\n2. **DS-Code Graph Modeling**: Different from existing code graphs, DS-code graph not only models dependency relationships but also introduces semantic relationships among nodes.\n\n3. **Bigraph Mapping**: CodeRAG maps the relevant requirement nodes (sub-requirements and similar requirements) from the requirement graph to corresponding code nodes in the DS-code graph. These mapped code nodes are then treated as \"anchors\" to guide LLM reasoning.\n\n4. **Agentic Reasoning**: CodeRAG introduces an agentic process, which allows LLMs to adaptively adjust reasoning strategy and search for the supportive knowledge which LLMs need in repo-level code generation.\n\n### Experimental Results\n\nExperiments show that CodeRAG achieves significant improvements (i.e., increasing 40.90 and 37.79 Pass@1 on GPT-4o and Gemini-Pro on DevEval) compared to no RAG scenarios. Additionally, CodeRAG outperforms commercial programming products such as Copilit and Cursor, and demonstrates CodeRAG's potential in solving real-world repo-level coding challenges."
    ],
    "durationSeconds": 8.514294486999978
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-13T21:46:26.575Z_

<details><summary>↩ Tool result · `toolu_018sKD5iDriv6PnLBsPf6JEi`</summary>

```text
Web search results for query: "ARISE repository graph agentic fault localization program repair 2025"

Links: [{"title":"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/html/2605.03117"},{"title":"[2605.03117] ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/abs/2605.03117"},{"title":"A Study on the Impact of Fault localization Granularity for Repository-Scale Code Repair Tasks","url":"https://arxiv.org/html/2604.00167"},{"title":"A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/html/2506.23749v1"},{"title":"HAFixAgent: History-Aware Program Repair Agent","url":"https://arxiv.org/html/2511.01047"},{"title":"Enhancing Repository-Level Software Repair via Repository-Aware Knowledge Graphs","url":"https://arxiv.org/html/2503.21710v1"},{"title":"Agent-Based Program Repair","url":"https://www.emergentmind.com/topics/agent-based-program-repair"},{"title":"Evaluating Agent-based Program Repair at Google","url":"https://arxiv.org/html/2501.07531v1"},{"title":"HAFixAgent: History-Aware Automated Program Repair Agent","url":"https://arxiv.org/pdf/2511.01047"},{"title":"Agentic Software Issue Resolution","url":"https://www.emergentmind.com/topics/agentic-software-issue-resolution"}]

Based on the search results, I found detailed information about ARISE:

ARISE (Agentic Repository-level Issue Solving Engine) augments an LLM-based agent with a multi-granularity program graph that extends structural relationships down to statement-level nodes connected by intra-procedural definition-use edges, and exposes this graph through a three-tier tool API that brings data-flow slicing as a first-class, queryable agent primitive allowing the model to trace which statements define or consume a variable of interest.

**Key Features:**

ARISE extends the graph to statement granularity and adds intra-procedural def-use edges, which enable the get_dataflow_slice tool to answer the localization question "which statements affect this variable?" in a single call.

**Evaluation Results:**

Compared to the unmodified SWE-agent baseline, ARISE improves Function Recall@1 by 17.0 points and Line Recall@1 by 15.0 points. These localization gains translate directly into repair success, with ARISE achieving 22.0% Pass@1 (66/300), a 4.7 percentage-point improvement over SWE-agent.

**Methodology:**

The system was evaluated on SWE-bench Lite (300 real GitHub issues, 11 Python repositories) using Qwen2.5-Coder-32B-Instruct as the backbone.

The paper was recently published and represents a significant advance in agentic fault localization and program repair by providing more precise data-flow semantic information to the repair agent.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d5364903-a4a1-4087-97e3-e23bdd6044c8",
  "uuid": "23d172dd-afa7-4a61-b4fc-2bec9e348e14",
  "tool_use_result": {
    "query": "ARISE repository graph agentic fault localization program repair 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PMkQsQS2PDroW4fJoJ5dhk",
        "content": [
          {
            "title": "ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair",
            "url": "https://arxiv.org/html/2605.03117"
          },
          {
            "title": "[2605.03117] ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair",
            "url": "https://arxiv.org/abs/2605.03117"
          },
          {
            "title": "A Study on the Impact of Fault localization Granularity for Repository-Scale Code Repair Tasks",
            "url": "https://arxiv.org/html/2604.00167"
          },
          {
            "title": "A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications",
            "url": "https://arxiv.org/html/2506.23749v1"
          },
          {
            "title": "HAFixAgent: History-Aware Program Repair Agent",
            "url": "https://arxiv.org/html/2511.01047"
          },
          {
            "title": "Enhancing Repository-Level Software Repair via Repository-Aware Knowledge Graphs",
            "url": "https://arxiv.org/html/2503.21710v1"
          },
          {
            "title": "Agent-Based Program Repair",
            "url": "https://www.emergentmind.com/topics/agent-based-program-repair"
          },
          {
            "title": "Evaluating Agent-based Program Repair at Google",
            "url": "https://arxiv.org/html/2501.07531v1"
          },
          {
            "title": "HAFixAgent: History-Aware Automated Program Repair Agent",
            "url": "https://arxiv.org/pdf/2511.01047"
          },
          {
            "title": "Agentic Software Issue Resolution",
            "url": "https://www.emergentmind.com/topics/agentic-software-issue-resolution"
          }
        ]
      },
      "Based on the search results, I found detailed information about ARISE:\n\nARISE (Agentic Repository-level Issue Solving Engine) augments an LLM-based agent with a multi-granularity program graph that extends structural relationships down to statement-level nodes connected by intra-procedural definition-use edges, and exposes this graph through a three-tier tool API that brings data-flow slicing as a first-class, queryable agent primitive allowing the model to trace which statements define or consume a variable of interest.\n\n**Key Features:**\n\nARISE extends the graph to statement granularity and adds intra-procedural def-use edges, which enable the get_dataflow_slice tool to answer the localization question \"which statements affect this variable?\" in a single call.\n\n**Evaluation Results:**\n\nCompared to the unmodified SWE-agent baseline, ARISE improves Function Recall@1 by 17.0 points and Line Recall@1 by 15.0 points. These localization gains translate directly into repair success, with ARISE achieving 22.0% Pass@1 (66/300), a 4.7 percentage-point improvement over SWE-agent.\n\n**Methodology:**\n\nThe system was evaluated on SWE-bench Lite (300 real GitHub issues, 11 Python repositories) using Qwen2.5-Coder-32B-Instruct as the backbone.\n\nThe paper was recently published and represents a significant advance in agentic fault localization and program repair by providing more precise data-flow semantic information to the repair agent."
    ],
    "durationSeconds": 7.649711651999969
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-13T21:46:29.022Z_

<details><summary>↩ Tool result · `toolu_01C65xpX2J33X44XeVFbf6dW`</summary>

```text
Web search results for query: "GraphCoder code context graph control flow data dependence details ASE 2024"

Links: [{"title":"GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph (ASE 2024 - Research Papers) - ASE 2024","url":"https://conf.researchr.org/details/ase-2024/ase-2024-research/46/GraphCoder-Enhancing-Repository-Level-Code-Completion-via-Coarse-to-fine-Retrieval-B"},{"title":"[2406.07003] GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model","url":"https://arxiv.org/abs/2406.07003"},{"title":"GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240607003L/abstract"},{"title":"GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph | Request PDF","url":"https://www.researchgate.net/publication/385287286_GraphCoder_Enhancing_Repository-Level_Code_Completion_via_Coarse-to-fine_Retrieval_Based_on_Code_Context_Graph"},{"title":"GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model","url":"https://arxiv.org/html/2406.07003v2"},{"title":"GitHub - oceaneLIU/GraphCoder","url":"https://github.com/oceaneLIU/GraphCoder"},{"title":"GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph - Consensus","url":"https://consensus.app/papers/graphcoder-enhancing-repositorylevel-code-completion-wang-jin/b4870512e370577aa2ee9b8b4aee9bfd/"},{"title":"GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph | Proceedings of the 39th IEEE/ACM International Conference on Automated Software Engineering","url":"https://dl.acm.org/doi/10.1145/3691620.3695054"},{"title":"GraphCoder: Enhancing Repository-Level Code Completion via Code","url":"https://openreview.net/pdf/7a92572e89daf427869cbb262f97920e5f6f35a3.pdf"},{"title":"GraphCoder | NL2Code","url":"https://nl2code.github.io/posts/GraphCoder/"}]

Based on the web search results, here's detailed information about GraphCoder presented at ASE 2024:

## Overview

GraphCoder is a retrieval-augmented code completion framework that leverages LLMs' general code knowledge and repository-specific knowledge via a graph-based retrieval-generation process.

## Code Context Graph (CCG) Details

A code context graph is the superimposition of three kinds of graphs about code: control flow graph (CFG), control dependence graph (CDG), and data dependence graph (DDG). More specifically, GraphCoder captures the context of completion target more accurately through code context graph (CCG) that consists of control-flow, data- and control-dependence between code statements, a more structured way to capture the completion target context than the sequence-based context used in existing retrieval-augmented approaches.

## Key Components

The approach includes two main technical contributions:

1. **Graph-based Representation**: A graph-based representation CCG (code context graph) of source code to capture relevant long-distance context for predicting the semantics of code completion target instead of the widely adopted sequence-based one.

2. **Retrieval Process**: Based on CCG, GraphCoder further employs a coarse-to-fine retrieval process to locate context-similar code snippets with the completion target from the current repository.

## Experimental Results

Compared to baseline retrieval-augmented methods, GraphCoder achieves higher exact match (EM) on average, with increases of +6.06 in code match and +6.23 in identifier match, while using less time and space.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d5364903-a4a1-4087-97e3-e23bdd6044c8",
  "uuid": "3f6e2d7e-52dd-48e0-bffe-3de6a7468b7d",
  "tool_use_result": {
    "query": "GraphCoder code context graph control flow data dependence details ASE 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_01DrYivGMKaZkxhfdVborVdm",
        "content": [
          {
            "title": "GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph (ASE 2024 - Research Papers) - ASE 2024",
            "url": "https://conf.researchr.org/details/ase-2024/ase-2024-research/46/GraphCoder-Enhancing-Repository-Level-Code-Completion-via-Coarse-to-fine-Retrieval-B"
          },
          {
            "title": "[2406.07003] GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model",
            "url": "https://arxiv.org/abs/2406.07003"
          },
          {
            "title": "GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2024arXiv240607003L/abstract"
          },
          {
            "title": "GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph | Request PDF",
            "url": "https://www.researchgate.net/publication/385287286_GraphCoder_Enhancing_Repository-Level_Code_Completion_via_Coarse-to-fine_Retrieval_Based_on_Code_Context_Graph"
          },
          {
            "title": "GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model",
            "url": "https://arxiv.org/html/2406.07003v2"
          },
          {
            "title": "GitHub - oceaneLIU/GraphCoder",
            "url": "https://github.com/oceaneLIU/GraphCoder"
          },
          {
            "title": "GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph - Consensus",
            "url": "https://consensus.app/papers/graphcoder-enhancing-repositorylevel-code-completion-wang-jin/b4870512e370577aa2ee9b8b4aee9bfd/"
          },
          {
            "title": "GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph | Proceedings of the 39th IEEE/ACM International Conference on Automated Software Engineering",
            "url": "https://dl.acm.org/doi/10.1145/3691620.3695054"
          },
          {
            "title": "GraphCoder: Enhancing Repository-Level Code Completion via Code",
            "url": "https://openreview.net/pdf/7a92572e89daf427869cbb262f97920e5f6f35a3.pdf"
          },
          {
            "title": "GraphCoder | NL2Code",
            "url": "https://nl2code.github.io/posts/GraphCoder/"
          }
        ]
      },
      "Based on the web search results, here's detailed information about GraphCoder presented at ASE 2024:\n\n## Overview\n\nGraphCoder is a retrieval-augmented code completion framework that leverages LLMs' general code knowledge and repository-specific knowledge via a graph-based retrieval-generation process.\n\n## Code Context Graph (CCG) Details\n\nA code context graph is the superimposition of three kinds of graphs about code: control flow graph (CFG), control dependence graph (CDG), and data dependence graph (DDG). More specifically, GraphCoder captures the context of completion target more accurately through code context graph (CCG) that consists of control-flow, data- and control-dependence between code statements, a more structured way to capture the completion target context than the sequence-based context used in existing retrieval-augmented approaches.\n\n## Key Components\n\nThe approach includes two main technical contributions:\n\n1. **Graph-based Representation**: A graph-based representation CCG (code context graph) of source code to capture relevant long-distance context for predicting the semantics of code completion target instead of the widely adopted sequence-based one.\n\n2. **Retrieval Process**: Based on CCG, GraphCoder further employs a coarse-to-fine retrieval process to locate context-similar code snippets with the completion target from the current repository.\n\n## Experimental Results\n\nCompared to baseline retrieval-augmented methods, GraphCoder achieves higher exact match (EM) on average, with increases of +6.06 in code match and +6.23 in identifier match, while using less time and space."
    ],
    "durationSeconds": 9.61730145899998
  }
}
```

</details>

---

### Assistant

_source line 28_

<details><summary>Logged reasoning block</summary>

```text
Now let me also search for CodeGRAG and any other training-time graph methods to round out the comparison, and look for more specific details about data-flow usage in these methods.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d5364903-a4a1-4087-97e3-e23bdd6044c8",
  "uuid": "beb402bf-5b03-4171-a35c-0cfb3a35947f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018GqCrZg7NTKnTCqg7n6r9z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3449,
      "cache_read_input_tokens": 30530,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3449
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 29_

搜索补充方法和更多细节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d5364903-a4a1-4087-97e3-e23bdd6044c8",
  "uuid": "5e0f3887-dc0d-40bf-9031-13c628735a5d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018GqCrZg7NTKnTCqg7n6r9z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3449,
      "cache_read_input_tokens": 30530,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3449
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017D9sRHLBTHQjZswsJRfPtY`</summary>

```json
{
  "query": "CodeGRAG code graph retrieval augmented generation control flow data flow 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d5364903-a4a1-4087-97e3-e23bdd6044c8",
  "uuid": "e0ecb816-e53c-456c-be06-7b053d520a62",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018GqCrZg7NTKnTCqg7n6r9z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3449,
      "cache_read_input_tokens": 30530,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3449
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Pc7fb2MyCsvBRiaQ4btmXj`</summary>

```json
{
  "query": "graph-based code retrieval training-time contrastive learning code search structure 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d5364903-a4a1-4087-97e3-e23bdd6044c8",
  "uuid": "09bcb890-e57b-4603-8aab-61ca2e1d5911",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018GqCrZg7NTKnTCqg7n6r9z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3449,
      "cache_read_input_tokens": 30530,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3449
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-13T21:46:40.522Z_

<details><summary>↩ Tool result · `toolu_017D9sRHLBTHQjZswsJRfPtY`</summary>

```text
Web search results for query: "CodeGRAG code graph retrieval augmented generation control flow data flow 2024"

Links: [{"title":"CodeGRAG: Extracting Composed Syntax Graphs for Retrieval Augmented Cross-Lingual Code Generation","url":"https://arxiv.org/html/2405.02355v1"},{"title":"[2405.02355] CodeGRAG: Bridging the Gap between Natural Language and Programming Language via Graphical Retrieval Augmented Generation","url":"https://arxiv.org/abs/2405.02355"},{"title":"CodeGRAG: Bridging the Gap between Natural Language and Programming Language via Graphical Retrieval Augmented Generation","url":"https://arxiv.org/html/2405.02355"},{"title":"[2405.02355v1] CodeGRAG: Extracting Composed Syntax Graphs for Retrieval Augmented Cross-Lingual Code Generation","url":"https://arxiv.org/abs/2405.02355v1"},{"title":"[2405.02355v3] CodeGRAG: Bridging the Gap between Natural Language and Programming Language via Graphical Retrieval Augmented Generation","url":"https://arxiv.org/abs/2405.02355v3"},{"title":"[Literature Review] CodeGRAG: Bridging the Gap between Natural Language and Programming Language via Graphical Retrieval Augmented Generation","url":"https://www.themoonlight.io/en/review/codegrag-bridging-the-gap-between-natural-language-and-programming-language-via-graphical-retrieval-augmented-generation"},{"title":"CodeGRAG: Bridging the Gap between Natural Language and Programming Language via Graphical Retrieval Augmented Generation | PromptLayer","url":"https://www.promptlayer.com/research-papers/codegrag-bridging-the-gap-between-natural-language-and-programming-language-via-graphical-retrieval-augmented-generation"},{"title":"CodeGRAG: Bridging the Gap between Natural Language and Programming Language via Graphical Retrieval Augmented Generation - Paper Detail","url":"https://deeplearn.org/arxiv/547019/codegrag:-bridging-the-gap-between-natural-language-and-programming-language-via-graphical-retrieval-augmented-generation"},{"title":"CodeGRAG: Extracting Composed Syntax Graphs for Retrieval Augmented Cross-Lingual Code Generation | OpenReview","url":"https://openreview.net/forum?id=IasbwEo0tH"},{"title":"CodeGRAG: Extracting Composed Syntax Graphs for Retrieval Augmented Cross-Lingual Code Generation | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/codegrag-bridging-gap-between-natural-language-programming"}]

I've found comprehensive information about CodeGRAG from the web search. Here's what the research shows:

## Overview

CodeGRAG is a Graphical Retrieval Augmented Code Generation framework that bridges the gap between natural language and programming languages to enhance the performance of LLMs.

## Core Technology

CodeGRAG extracts and summarizes the control flow and data flow of code blocks to fill the gap between programming languages and natural language. The approach represents code blocks with composed syntax graphs based on data-flow graphs and control-flow graphs, which extracts both semantic level and logical level information of code blocks.

## Implementation Approaches

The framework proposes 1) a hard meta-graph prompt template to transform the challenging syntax graph into informative graphical view for tuning-free models and 2) a soft prompting technique that injects the domain knowledge of programming languages into model parameters via finetuning the models with soft signals encoded by GNN expert model.

## Key Features

- The generation process requires only one calling of LLMs and can offer cross-lingual enhancement.
- CodeGRAG significantly improves the code generation ability of LLMs and can even offer performance gain for cross-lingual code generation.

## Publication

The paper was initially submitted on May 3, 2024. The research has gone through multiple revisions, with the latest version submitted in May 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d5364903-a4a1-4087-97e3-e23bdd6044c8",
  "uuid": "69e2d1b1-6fd8-4549-91ec-7940b82f37bf",
  "tool_use_result": {
    "query": "CodeGRAG code graph retrieval augmented generation control flow data flow 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_01AFHCW4ykLittYmRnLQDmPR",
        "content": [
          {
            "title": "CodeGRAG: Extracting Composed Syntax Graphs for Retrieval Augmented Cross-Lingual Code Generation",
            "url": "https://arxiv.org/html/2405.02355v1"
          },
          {
            "title": "[2405.02355] CodeGRAG: Bridging the Gap between Natural Language and Programming Language via Graphical Retrieval Augmented Generation",
            "url": "https://arxiv.org/abs/2405.02355"
          },
          {
            "title": "CodeGRAG: Bridging the Gap between Natural Language and Programming Language via Graphical Retrieval Augmented Generation",
            "url": "https://arxiv.org/html/2405.02355"
          },
          {
            "title": "[2405.02355v1] CodeGRAG: Extracting Composed Syntax Graphs for Retrieval Augmented Cross-Lingual Code Generation",
            "url": "https://arxiv.org/abs/2405.02355v1"
          },
          {
            "title": "[2405.02355v3] CodeGRAG: Bridging the Gap between Natural Language and Programming Language via Graphical Retrieval Augmented Generation",
            "url": "https://arxiv.org/abs/2405.02355v3"
          },
          {
            "title": "[Literature Review] CodeGRAG: Bridging the Gap between Natural Language and Programming Language via Graphical Retrieval Augmented Generation",
            "url": "https://www.themoonlight.io/en/review/codegrag-bridging-the-gap-between-natural-language-and-programming-language-via-graphical-retrieval-augmented-generation"
          },
          {
            "title": "CodeGRAG: Bridging the Gap between Natural Language and Programming Language via Graphical Retrieval Augmented Generation | PromptLayer",
            "url": "https://www.promptlayer.com/research-papers/codegrag-bridging-the-gap-between-natural-language-and-programming-language-via-graphical-retrieval-augmented-generation"
          },
          {
            "title": "CodeGRAG: Bridging the Gap between Natural Language and Programming Language via Graphical Retrieval Augmented Generation - Paper Detail",
            "url": "https://deeplearn.org/arxiv/547019/codegrag:-bridging-the-gap-between-natural-language-and-programming-language-via-graphical-retrieval-augmented-generation"
          },
          {
            "title": "CodeGRAG: Extracting Composed Syntax Graphs for Retrieval Augmented Cross-Lingual Code Generation | OpenReview",
            "url": "https://openreview.net/forum?id=IasbwEo0tH"
          },
          {
            "title": "CodeGRAG: Extracting Composed Syntax Graphs for Retrieval Augmented Cross-Lingual Code Generation | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/codegrag-bridging-gap-between-natural-language-programming"
          }
        ]
      },
      "I've found comprehensive information about CodeGRAG from the web search. Here's what the research shows:\n\n## Overview\n\nCodeGRAG is a Graphical Retrieval Augmented Code Generation framework that bridges the gap between natural language and programming languages to enhance the performance of LLMs.\n\n## Core Technology\n\nCodeGRAG extracts and summarizes the control flow and data flow of code blocks to fill the gap between programming languages and natural language. The approach represents code blocks with composed syntax graphs based on data-flow graphs and control-flow graphs, which extracts both semantic level and logical level information of code blocks.\n\n## Implementation Approaches\n\nThe framework proposes 1) a hard meta-graph prompt template to transform the challenging syntax graph into informative graphical view for tuning-free models and 2) a soft prompting technique that injects the domain knowledge of programming languages into model parameters via finetuning the models with soft signals encoded by GNN expert model.\n\n## Key Features\n\n- The generation process requires only one calling of LLMs and can offer cross-lingual enhancement.\n- CodeGRAG significantly improves the code generation ability of LLMs and can even offer performance gain for cross-lingual code generation.\n\n## Publication\n\nThe paper was initially submitted on May 3, 2024. The research has gone through multiple revisions, with the latest version submitted in May 2025."
    ],
    "durationSeconds": 6.831950808999827
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-13T21:46:41.511Z_

<details><summary>↩ Tool result · `toolu_01Pc7fb2MyCsvBRiaQ4btmXj`</summary>

```text
Web search results for query: "graph-based code retrieval training-time contrastive learning code search structure 2024 2025"

Links: [{"title":"GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph | Proceedings of the 39th IEEE/ACM International Conference on Automated Software Engineering","url":"https://dl.acm.org/doi/10.1145/3691620.3695054"},{"title":"SCodeSearcher: soft contrastive learning for code search | Empirical Software Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10664-024-10603-z"},{"title":"Code Representation Based on Hybrid Graph Modelling | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-030-92307-5_35"},{"title":"[2406.07003] GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model","url":"https://arxiv.org/abs/2406.07003"},{"title":"CODEXGRAPH: Bridging Large Language Models and ...","url":"https://aclanthology.org/2025.naacl-long.7.pdf"},{"title":"GCL-ALG: graph contrastive learning with adaptive ...","url":"https://peerj.com/articles/cs-3101.pdf"},{"title":"ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning","url":"https://arxiv.org/pdf/2301.09072"},{"title":"[PDF] GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model | Semantic Scholar","url":"https://www.semanticscholar.org/paper/GraphCoder:-Enhancing-Repository-Level-Code-via-and-Liu-Yu/793bbb3c70d4bac3908bd8f2ecc309f1bfdf5f52"},{"title":"SCL-CVD: Supervised contrastive learning for code vulnerability detection via GraphCodeBERT - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0167404824002992"},{"title":"GitHub - LIANGKE23/Awesome-Knowledge-Graph-Reasoning: AKGR: Awesome Knowledge Graph Reasoning is a collection of knowledge graph reasoning works, including papers, codes and datasets · GitHub","url":"https://github.com/LIANGKE23/Awesome-Knowledge-Graph-Reasoning"}]

Based on the web search results, I found several relevant papers and research works on graph-based code retrieval with contrastive learning. Here are the key findings:

## Recent Works (2024-2025)

**GraphCoder (2024)**: GraphCoder is a retrieval-augmented code completion framework that leverages LLMs' general code knowledge and repository-specific knowledge via a graph-based retrieval-generation process. It captures the context of completion targets through a code context graph (CCG) consisting of control-flow, data- and control-dependence between code statements.

**SCodeSearcher (2025)**: Many researchers have applied contrastive learning to learn semantic relationships between queries and code snippets for code search, with SCodeSearcher introducing soft contrastive learning for code search published in 2025.

**CODEXGRAPH**: This recent work addresses repository-level code tasks through graph-based retrieval approaches, demonstrating the importance of graph-aware retrieval augmentation for code-related tasks.

## Key Research Directions

Code search tools should retrieve all code snippets that meet given queries and are implemented in diverse manners to satisfy different programming styles of developers. Approaches like SCL-CVD leverage supervised contrastive learning with graph-based models like GraphCodeBERT, representing source code as data flow graphs processed by pre-trained models fine-tuned using supervised contrastive loss functions.

These works collectively demonstrate an active research area combining graph representations of code structure with contrastive learning methods for improved code retrieval and understanding tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d5364903-a4a1-4087-97e3-e23bdd6044c8",
  "uuid": "7ba7b819-8ade-4f33-96b1-47da05df8387",
  "tool_use_result": {
    "query": "graph-based code retrieval training-time contrastive learning code search structure 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RdFF5KGnqonoKu2SymALdY",
        "content": [
          {
            "title": "GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph | Proceedings of the 39th IEEE/ACM International Conference on Automated Software Engineering",
            "url": "https://dl.acm.org/doi/10.1145/3691620.3695054"
          },
          {
            "title": "SCodeSearcher: soft contrastive learning for code search | Empirical Software Engineering | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s10664-024-10603-z"
          },
          {
            "title": "Code Representation Based on Hybrid Graph Modelling | Springer Nature Link",
            "url": "https://link.springer.com/chapter/10.1007/978-3-030-92307-5_35"
          },
          {
            "title": "[2406.07003] GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model",
            "url": "https://arxiv.org/abs/2406.07003"
          },
          {
            "title": "CODEXGRAPH: Bridging Large Language Models and ...",
            "url": "https://aclanthology.org/2025.naacl-long.7.pdf"
          },
          {
            "title": "GCL-ALG: graph contrastive learning with adaptive ...",
            "url": "https://peerj.com/articles/cs-3101.pdf"
          },
          {
            "title": "ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning",
            "url": "https://arxiv.org/pdf/2301.09072"
          },
          {
            "title": "[PDF] GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/GraphCoder:-Enhancing-Repository-Level-Code-via-and-Liu-Yu/793bbb3c70d4bac3908bd8f2ecc309f1bfdf5f52"
          },
          {
            "title": "SCL-CVD: Supervised contrastive learning for code vulnerability detection via GraphCodeBERT - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/abs/pii/S0167404824002992"
          },
          {
            "title": "GitHub - LIANGKE23/Awesome-Knowledge-Graph-Reasoning: AKGR: Awesome Knowledge Graph Reasoning is a collection of knowledge graph reasoning works, including papers, codes and datasets · GitHub",
            "url": "https://github.com/LIANGKE23/Awesome-Knowledge-Graph-Reasoning"
          }
        ]
      },
      "Based on the web search results, I found several relevant papers and research works on graph-based code retrieval with contrastive learning. Here are the key findings:\n\n## Recent Works (2024-2025)\n\n**GraphCoder (2024)**: GraphCoder is a retrieval-augmented code completion framework that leverages LLMs' general code knowledge and repository-specific knowledge via a graph-based retrieval-generation process. It captures the context of completion targets through a code context graph (CCG) consisting of control-flow, data- and control-dependence between code statements.\n\n**SCodeSearcher (2025)**: Many researchers have applied contrastive learning to learn semantic relationships between queries and code snippets for code search, with SCodeSearcher introducing soft contrastive learning for code search published in 2025.\n\n**CODEXGRAPH**: This recent work addresses repository-level code tasks through graph-based retrieval approaches, demonstrating the importance of graph-aware retrieval augmentation for code-related tasks.\n\n## Key Research Directions\n\nCode search tools should retrieve all code snippets that meet given queries and are implemented in diverse manners to satisfy different programming styles of developers. Approaches like SCL-CVD leverage supervised contrastive learning with graph-based models like GraphCodeBERT, representing source code as data flow graphs processed by pre-trained models fine-tuned using supervised contrastive loss functions.\n\nThese works collectively demonstrate an active research area combining graph representations of code structure with contrastive learning methods for improved code retrieval and understanding tasks."
    ],
    "durationSeconds": 7.167971999000059
  }
}
```

</details>

---

### Assistant

_source line 34_

<details><summary>Logged reasoning block</summary>

```text
I now have sufficient information about all the main methods. Let me also check for the RepoGraph paper details - specifically whether it was published at ICLR 2025. Let me search for one more paper to see if there's anything else significant I should include, like the Knowledge Graph based approach for code.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d5364903-a4a1-4087-97e3-e23bdd6044c8",
  "uuid": "08f411ca-9632-47ec-8f5e-fafbb57562d1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DnVbA1nHZFLfmQZpdUetSF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2266,
      "cache_read_input_tokens": 33979,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2266
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 35_

现在我有足够的信息来编写对比表和分析。让我再确认一下 RepoGraph 的会议信息。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d5364903-a4a1-4087-97e3-e23bdd6044c8",
  "uuid": "12a5c3d5-5f96-463d-b1ec-a3401a54b8f6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DnVbA1nHZFLfmQZpdUetSF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2266,
      "cache_read_input_tokens": 33979,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2266
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 36_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012pY8TSmYNEgBm8eJBATJ1q`</summary>

```json
{
  "query": "RepoGraph ICLR 2025 SWE-bench code graph arXiv 2410.14684"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d5364903-a4a1-4087-97e3-e23bdd6044c8",
  "uuid": "e6c1a713-705d-427c-9e8a-6c02d44321b3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DnVbA1nHZFLfmQZpdUetSF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2266,
      "cache_read_input_tokens": 33979,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2266
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-13T21:46:55.061Z_

<details><summary>↩ Tool result · `toolu_012pY8TSmYNEgBm8eJBATJ1q`</summary>

```text
Web search results for query: "RepoGraph ICLR 2025 SWE-bench code graph arXiv 2410.14684"

Links: [{"title":"[2410.14684] RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph","url":"https://arxiv.org/abs/2410.14684"},{"title":"Enhancing AI Software Engineering with Repository-level Code Graph RepoGraph:","url":"https://iclr.cc/media/iclr-2025/Slides/28957.pdf"},{"title":"Published as a conference paper at ICLR 2025","url":"https://arxiv.org/pdf/2410.14684"},{"title":"RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph","url":"https://arxiv.org/html/2410.14684"},{"title":"RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph | OpenReview","url":"https://openreview.net/forum?id=dw9VUsSHGB"},{"title":"RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph | alphaXiv","url":"https://www.alphaxiv.org/overview/2410.14684v1"},{"title":"GitHub - YerbaPage/Awesome-Repo-Level-Code-Generation: Must-read papers on Repository-level Code Generation & Issue Resolution 🔥","url":"https://github.com/YerbaPage/Awesome-Repo-Level-Code-Generation"},{"title":"arXiv:2502.18465v1 [cs.SE] 29 Jan 2025","url":"https://arxiv.org/pdf/2502.18465"},{"title":"REPOGRAPH: ENHANCING AI SOFTWARE ENGINEERING WITH REPOSITORY-LEVEL CODE GRAPH - Illinois Experts","url":"https://experts.illinois.edu/en/publications/repograph-enhancing-ai-software-engineering-with-repository-level/"},{"title":"Dissecting the SWE-Bench Leaderboards: Profiling Submitters and Architectures of LLM- and Agent-Based Repair Systems","url":"https://arxiv.org/html/2506.17208v2"}]

Based on the search results, here's what I found about RepoGraph:

## Overview

RepoGraph is a plug-in module that manages a repository-level structure for modern AI software engineering solutions and offers the desired guidance and serves as a repository-wide navigation for AI software engineers.

## Paper Details

The paper was published by Ouyang, S., Yu, W., Ma, K., and others at the 13th International Conference on Learning Representations, ICLR 2025, pages 30361-30384. The latest version was updated on March 18, 2025.

## Key Problem and Solution

Large Language Models (LLMs) excel in code generation yet struggle with modern AI software engineering tasks. Unlike traditional function-level or file-level coding tasks, AI software engineering requires not only basic coding proficiency but also advanced skills in managing and interacting with code repositories. However, existing methods often overlook the need for repository-level code understanding, which is crucial for accurately grasping the broader context and developing effective solutions.

## Performance Results

RepoGraph boosts the success rate of existing methods for both agent and procedural frameworks by achieving an average relative improvement of 32.8%. When evaluated on the SWE-bench by plugging it into four different methods of two lines of approaches, RepoGraph substantially boosts the performance of all systems, leading to a new state-of-the-art among open-source frameworks.

## Code and Resources

The code is available at https://github.com/ozyyshr/RepoGraph.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d5364903-a4a1-4087-97e3-e23bdd6044c8",
  "uuid": "0cad7d70-ce4f-43b2-b7f1-225c0973c518",
  "tool_use_result": {
    "query": "RepoGraph ICLR 2025 SWE-bench code graph arXiv 2410.14684",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CBWWBjztCwMzWRNkyAvJmp",
        "content": [
          {
            "title": "[2410.14684] RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph",
            "url": "https://arxiv.org/abs/2410.14684"
          },
          {
            "title": "Enhancing AI Software Engineering with Repository-level Code Graph RepoGraph:",
            "url": "https://iclr.cc/media/iclr-2025/Slides/28957.pdf"
          },
          {
            "title": "Published as a conference paper at ICLR 2025",
            "url": "https://arxiv.org/pdf/2410.14684"
          },
          {
            "title": "RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph",
            "url": "https://arxiv.org/html/2410.14684"
          },
          {
            "title": "RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph | OpenReview",
            "url": "https://openreview.net/forum?id=dw9VUsSHGB"
          },
          {
            "title": "RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2410.14684v1"
          },
          {
            "title": "GitHub - YerbaPage/Awesome-Repo-Level-Code-Generation: Must-read papers on Repository-level Code Generation & Issue Resolution 🔥",
            "url": "https://github.com/YerbaPage/Awesome-Repo-Level-Code-Generation"
          },
          {
            "title": "arXiv:2502.18465v1 [cs.SE] 29 Jan 2025",
            "url": "https://arxiv.org/pdf/2502.18465"
          },
          {
            "title": "REPOGRAPH: ENHANCING AI SOFTWARE ENGINEERING WITH REPOSITORY-LEVEL CODE GRAPH - Illinois Experts",
            "url": "https://experts.illinois.edu/en/publications/repograph-enhancing-ai-software-engineering-with-repository-level/"
          },
          {
            "title": "Dissecting the SWE-Bench Leaderboards: Profiling Submitters and Architectures of LLM- and Agent-Based Repair Systems",
            "url": "https://arxiv.org/html/2506.17208v2"
          }
        ]
      },
      "Based on the search results, here's what I found about RepoGraph:\n\n## Overview\n\nRepoGraph is a plug-in module that manages a repository-level structure for modern AI software engineering solutions and offers the desired guidance and serves as a repository-wide navigation for AI software engineers.\n\n## Paper Details\n\nThe paper was published by Ouyang, S., Yu, W., Ma, K., and others at the 13th International Conference on Learning Representations, ICLR 2025, pages 30361-30384. The latest version was updated on March 18, 2025.\n\n## Key Problem and Solution\n\nLarge Language Models (LLMs) excel in code generation yet struggle with modern AI software engineering tasks. Unlike traditional function-level or file-level coding tasks, AI software engineering requires not only basic coding proficiency but also advanced skills in managing and interacting with code repositories. However, existing methods often overlook the need for repository-level code understanding, which is crucial for accurately grasping the broader context and developing effective solutions.\n\n## Performance Results\n\nRepoGraph boosts the success rate of existing methods for both agent and procedural frameworks by achieving an average relative improvement of 32.8%. When evaluated on the SWE-bench by plugging it into four different methods of two lines of approaches, RepoGraph substantially boosts the performance of all systems, leading to a new state-of-the-art among open-source frameworks.\n\n## Code and Resources\n\nThe code is available at https://github.com/ozyyshr/RepoGraph."
    ],
    "durationSeconds": 7.3265207059998065
  }
}
```

</details>

---

### Assistant

_source line 38_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me compile the comparison table, discussion points, and related work paragraph. Let me organize the data:

1. **CodexGraph** (NAACL 2025, arXiv 2408.03910)
   - Graph type: Code graph database (nodes: MODULE, CLASS, FUNCTION; edges: CONTAINS, INHERITS, USES)
   - Usage stage: Inference-time (agent queries graph database at runtime)
   - Data-flow support: No inter-procedural data-flow, static analysis for symbol relationships
   - Task: General repository-level coding (code completion, issue resolution)
   - Scalability: Evaluated on CrossCodeEval, SWE-bench, EvoCodeBench
   - Key difference: Inference-time graph database querying, task-agnostic schema

2. **LocAgent** (ACL 2025, arXiv 2503.09089)
   - Graph type: Directed heterogeneous graph (code entities + dependencies)
   - Usage stage: Inference-time (agent traverses graph for localization)
   - Data-flow support: Not explicit inter-procedural data-flow, but captures dependency edges
   - Task: Fault localization / code localization
   - Scalability: File-level 92.7% accuracy on benchmarks fine-tuned with Qwen-2.5-Coder-32B
   - Key difference: Agent-based multi-hop reasoning on graph at inference time

3. **RANGER** (arXiv 2509.25257, Sep 2025)
   - Graph type: Knowledge graph with MCTS-based traversal
   - Usage stage: Inference-time (MCTS graph exploration at query time)
   - Data-flow support: Not explicitly inter-procedural data-flow
   - Task: Code search, QA, cross-file dependency retrieval, code completion
   - Scalability: CodeSearchNet, RepoQA, RepoBench, CrossCodeEval
   - Key difference: MCTS-guided graph exploration, dual-stage retrieval

4. **RepoGraph** (ICLR 2025, arXiv 2410.14684)
   - Graph type: Repository-level code graph (class hierarchy, call graph, file structure)
   - Usage stage: Inference-time (plug-in module for SE agents)
   - Data-flow support: No inter-procedural data-flow, focuses on structural relationships
   - Task: Software engineering / issue resolution (SWE-bench)
   - Scalability: SWE-bench, CrossCodeEval, 32.8% relative improvement
   - Key difference: Plug-in module for existing agents, repo-wide navigation

5. **GraphCoder** (ASE 2024, arXiv 2406.07003)
   - Graph type: Code Context Graph (CCG) = CFG + CDG + DDG
   - Usage stage: Inference-time (graph built and queried per completion)
   - Data-flow support: Yes - data dependence graph (DDG), but intra-procedural
   - Task: Repository-level code completion
   - Scalability: Repository

-level benchmarks
   - Key difference: Coarse-to-fine retrieval using CCG with intra-procedural data and control flow

6. **CodeRAG** (arXiv 2504.10046, 2025)
   - Graph type: Bigraph (requirement graph + DS-code graph with dependency + semantic edges)
   - Usage stage: Inference-time (graph construction + agentic reasoning)
   - Data-flow support: Dependency relationships, not explicit inter-procedural data-flow analysis
   - Task: Repository-level code generation
   - Scalability: DevEval, +40.90 Pass@1 with GPT-4o
   - Key difference: Dual-graph approach combining requirements and code with agentic reasoning

7. **ARISE** (arXiv 2605.03117, 2025)
   - Graph type: Multi-granularity program graph with statement-level details and def-use edges
   - Usage stage: Inference-time where agents query the graph API
   - Data-flow support: Intra-procedural def-use edges enabling data-flow slicing
   - Task: Fault localization and program repair
   - Scalability: SWE-bench Lite with 300 issues
   - Key difference: Statement-level granularity with def-use edges that agents can leverage as tools

8. **CodeGRAG** (arXiv 2405.02355, 2024)
   - Graph type: Composed syntax graph combining AST, DFG, and CFG
   - Usage stage: Both training and inference—GNN expert generates soft prompts during training, graph prompts at inference
   - Data-flow support: Full data flow graph extraction
   - Task: Cross-lingual code generation
   - Key difference: Soft prompting approach with GNN expert enabling multi-language support

Now I'm organizing this into a comprehensive structured document.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d5364903-a4a1-4087-97e3-e23bdd6044c8",
  "uuid": "a2a6ee6c-64fb-4892-b7c9-f234e9defb45",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0149B6Uw1pPJKBGtj7TfSCzf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1091,
      "cache_read_input_tokens": 36245,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1091
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 39_

信息收集完成。现在编写对比表、discussion 要点和 related work 段落。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d5364903-a4a1-4087-97e3-e23bdd6044c8",
  "uuid": "7340c55f-b51b-4bca-804b-adb35f7987d5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0149B6Uw1pPJKBGtj7TfSCzf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1091,
      "cache_read_input_tokens": 36245,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1091
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 40_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file · `toolu_013Hbd8RTd1uDuorZH81Pcbf`</summary>

```json
{
  "project": "structfuse-context",
  "file": "memory.md",
  "content": "# Inference-Time Graph Methods 文献对比\n\n## 对比表\n\n| Method | Paper | Venue | Graph Type | Usage Stage | Inter-proc Data-Flow | Task | Scalability | Key Diff from StructFuse |\n|--------|-------|-------|-----------|-------------|---------------------|------|-------------|--------------------------|\n| **CodexGraph** | Bridging LLMs and Code Repositories via Code Graph Databases | NAACL 2025 (arXiv:2408.03910) | Code graph DB (MODULE/CLASS/FUNCTION nodes; CONTAINS/INHERITS/USES edges) | Inference-time | No. Static analysis for symbol relations only | General repo-level coding (completion, issue resolution) | CrossCodeEval, SWE-bench, EvoCodeBench | Agent queries graph DB at inference; task-agnostic schema but no data-flow semantics |\n| **LocAgent** | Graph-Guided LLM Agents for Code Localization | ACL 2025 (arXiv:2503.09089) | Directed heterogeneous graph (code entities + dependency edges) | Inference-time | No. Dependency edges, not data-flow | Fault localization | 92.7% file-level accuracy; SWE-bench +12% Pass@10 | Agent multi-hop graph reasoning at inference; needs fine-tuned 32B model |\n| **RANGER** | Repository-Level Agent for Graph-Enhanced Retrieval | arXiv:2509.25257 (Sep 2025) | Knowledge graph + MCTS traversal | Inference-time | No | Code search, QA, cross-file retrieval, completion | CodeSearchNet, RepoQA, RepoBench, CrossCodeEval | MCTS-guided graph exploration; dual-stage (Cypher + MCTS); heavy inference cost |\n| **RepoGraph** | Enhancing AI SE with Repository-level Code Graph | ICLR 2025 (arXiv:2410.14684) | Repo-level code graph (class hierarchy, call graph, file structure) | Inference-time | No. Structural relations only | Software engineering / issue resolution | SWE-bench (+32.8% relative); CrossCodeEval | Plug-in module for existing agents; repo-wide navigation; no semantic analysis |\n| **GraphCoder** | Enhancing Repo-Level Code Completion via Code Context Graph | ASE 2024 (arXiv:2406.07003) | Code Context Graph (CFG + CDG + DDG) | Inference-time | Partial. Data dependence graph but **intra-procedural** only | Code completion | Repository-level benchmarks | Coarse-to-fine retrieval with CCG; closest to StructFuse in using data/control flow, but intra-proc and at inference-time |\n| **CodeRAG** | Supportive Code Retrieval on Bigraph for Real-World Code Generation | arXiv:2504.10046 (Apr 2025) | Bigraph (requirement graph + DS-code graph) | Inference-time | No. Dependency + semantic edges | Repo-level code generation | DevEval (+40.90 Pass@1 w/ GPT-4o) | Dual-graph (requirements + code); agentic reasoning; high inference overhead |\n| **ARISE** | Repository-level Graph for Agentic Fault Localization and Program Repair | arXiv:2605.03117 (May 2025) | Multi-granularity program graph (statement nodes + def-use edges) | Inference-time | Partial. **Intra-procedural** def-use edges + data-flow slicing tool | Fault localization + repair | SWE-bench Lite (300 issues); +17.0 Function Recall@1 | Closest to StructFuse in data-flow usage; but intra-proc only, agent queries at inference |\n| **CodeGRAG** | Bridging NL and PL via Graphical RAG | arXiv:2405.02355 (2024) | Composed syntax graph (AST + DFG + CFG) | Both (GNN training + graph prompt at inference) | Partial. DFG extraction but function-level | Code generation (cross-lingual) | Multiple PLs | Only method with training-time component (GNN soft prompts); but graph also used at inference |\n| **StructFuse** (Ours) | Structure-Grounded Hard Negatives via CodeQL Data-Flow | — | Inter-procedural data-flow graph (CodeQL taint tracking) | **Training-time only** | **Yes. Full inter-procedural** (source→sink across call boundaries) | Code retrieval (contrastive training) | Large-scale repos with CodeQL | Zero inference overhead; graph used offline for negative mining; inter-proc data-flow |\n\n## Discussion 要点\n\n### StructFuse vs Inference-Time Graph Methods: 互补性与差异性\n\n1. **Cost-accuracy tradeoff**: Inference-time methods (CodexGraph, RANGER, RepoGraph) achieve high precision by constructing and querying graphs per request, but incur significant latency (graph construction + traversal + LLM calls). StructFuse amortizes all graph computation to training time—once the encoder is trained with structure-grounded negatives, inference is a single embedding lookup with zero graph overhead. This makes StructFuse suitable for latency-sensitive production retrieval where inference-time graph methods are impractical.\n\n2. **Data-flow depth**: Most inference-time methods use structural graphs (call graphs, class hierarchies, file dependencies). Only GraphCoder and ARISE incorporate data/control flow, but limited to **intra-procedural** scope. StructFuse uniquely leverages **inter-procedural** data-flow via CodeQL's taint tracking, capturing cross-function semantic relationships (e.g., a sanitizer function that transforms data between source and sink across call boundaries). This deeper semantic signal generates harder, more informative negatives.\n\n3. **Complementarity**: StructFuse and inference-time methods are orthogonal and composable. A StructFuse-trained encoder can serve as the embedding backbone for systems like RANGER or CodexGraph, providing better initial retrieval that reduces the graph agent's search space. Conversely, inference-time graph methods can provide reranking on top of StructFuse retrieval for tasks requiring maximum precision.\n\n4. **Scalability model**: Inference-time methods scale linearly with query volume (each query triggers graph operations). StructFuse's cost is front-loaded: CodeQL analysis runs once per repository update, and the resulting negatives improve the encoder permanently. For high-QPS code search services, this one-time investment yields compounding returns.\n\n5. **Task generality vs specialization**: Inference-time graph agents (CodexGraph, RepoGraph) are task-agnostic but require powerful LLMs as backends. StructFuse produces a specialized retrieval encoder that excels at the code search task without LLM inference, making it deployable as a lightweight, efficient first-stage retriever in multi-stage pipelines.\n\n## Related Work 段落草稿 (~200 words)\n\n**Graph-Based Methods for Code Understanding.**\nRecent work has explored leveraging code graphs to enhance LLM-based software engineering. Inference-time approaches construct and query graphs during each interaction: CodexGraph (Liu et al., NAACL 2025) builds a code graph database that LLM agents query via structured interfaces; RepoGraph (Ouyang et al., ICLR 2025) provides repository-level navigation as a plug-in module for SE agents; LocAgent (ACL 2025) and RANGER (2025) employ graph-guided multi-hop reasoning and MCTS-based traversal for code localization and retrieval, respectively. GraphCoder (ASE 2024) incorporates intra-procedural control-flow and data-dependence graphs for code completion retrieval, while ARISE (2025) extends this with statement-level def-use edges for fault localization. CodeGRAG (2024) bridges training and inference by using GNN-encoded graph prompts.\n\nThese methods achieve strong results but impose substantial inference-time costs—graph construction, traversal, and often multiple LLM calls per query. Moreover, their data-flow analysis remains intra-procedural. StructFuse takes a fundamentally different approach: we leverage CodeQL's inter-procedural taint tracking to generate structure-grounded hard negatives at **training time**, producing an encoder that captures cross-function data-flow semantics without any graph overhead at inference. This positions StructFuse as complementary to inference-time graph methods—it can serve as an efficient first-stage retriever whose embeddings already encode deep structural relationships that other methods must compute on-the-fly.\n\n---\n\n## 参考文献\n\n- CodexGraph: arXiv:2408.03910, NAACL 2025\n- LocAgent: arXiv:2503.09089, ACL 2025\n- RANGER: arXiv:2509.25257, 2025\n- RepoGraph: arXiv:2410.14684, ICLR 2025\n- GraphCoder: arXiv:2406.07003, ASE 2024\n- CodeRAG: arXiv:2504.10046, 2025\n- ARISE: arXiv:2605.03117, 2025\n- CodeGRAG: arXiv:2405.02355, 2024\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d5364903-a4a1-4087-97e3-e23bdd6044c8",
  "uuid": "f7ddfff1-06c0-408a-b787-7a98baada51c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0149B6Uw1pPJKBGtj7TfSCzf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1091,
      "cache_read_input_tokens": 36245,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1091
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-13T21:48:10.774Z_

<details><summary>↩ Tool result · `toolu_013Hbd8RTd1uDuorZH81Pcbf`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/memory.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d5364903-a4a1-4087-97e3-e23bdd6044c8",
  "uuid": "f2e1f842-c09e-43d7-972d-7612f25cbd21",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/memory.md\\\", \\\"saved\\\": true}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/memory.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 42_

已完成。产出已保存到项目 `memory.md`，包含：

**1. 对比表** — 覆盖 8 个方法 + StructFuse，对比维度包括 graph type、usage stage、inter-proc data-flow support、task、scalability、key difference。

**2. Discussion 要点（5 点）**：
- Cost-accuracy tradeoff：StructFuse 零推理开销 vs 其他方法每次查询都要建图/遍历
- Data-flow depth：其他方法最多 intra-procedural，StructFuse 是唯一做 inter-procedural 的
- Complementarity：StructFuse encoder 可作为 inference-time 方法的 embedding backbone
- Scalability model：前置一次性投入 vs 随 QPS 线性增长
- Task generality：轻量 first-stage retriever vs 依赖 LLM 的 task-agnostic agent

**3. Related Work 段落** — ~200 words，定位 StructFuse 在 graph-based code understanding 中的独特位置（training-time + inter-procedural + zero inference cost）。

核心发现：ARISE 和 GraphCoder 是最接近 StructFuse 的工作（都用了 data/control flow），但它们都局限于 intra-procedural 且在 inference-time 使用图。这是 StructFuse 的两个关键区分点。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d5364903-a4a1-4087-97e3-e23bdd6044c8",
  "uuid": "94fa995b-fec3-45d4-b0f7-3dd4c72c5f15",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0191mtbEGfvzBWNxmdMsJTyP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3648,
      "cache_read_input_tokens": 37336,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3648
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Task result

_source line 43_

已完成。产出已保存到项目 `memory.md`，包含：

**1. 对比表** — 覆盖 8 个方法 + StructFuse，对比维度包括 graph type、usage stage、inter-proc data-flow support、task、scalability、key difference。

**2. Discussion 要点（5 点）**：
- Cost-accuracy tradeoff：StructFuse 零推理开销 vs 其他方法每次查询都要建图/遍历
- Data-flow depth：其他方法最多 intra-procedural，StructFuse 是唯一做 inter-procedural 的
- Complementarity：StructFuse encoder 可作为 inference-time 方法的 embedding backbone
- Scalability model：前置一次性投入 vs 随 QPS 线性增长
- Task generality：轻量 first-stage retriever vs 依赖 LLM 的 task-agnostic agent

**3. Related Work 段落** — ~200 words，定位 StructFuse 在 graph-based code understanding 中的独特位置（training-time + inter-procedural + zero inference cost）。

核心发现：ARISE 和 GraphCoder 是最接近 StructFuse 的工作（都用了 data/control flow），但它们都局限于 intra-procedural 且在 inference-time 使用图。这是 StructFuse 的两个关键区分点。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 161607,
  "duration_api_ms": 209870,
  "num_turns": 15,
  "stop_reason": "end_turn",
  "session_id": "d5364903-a4a1-4087-97e3-e23bdd6044c8",
  "total_cost_usd": 0.79945625,
  "usage": {
    "input_tokens": 1824,
    "cache_creation_input_tokens": 29143,
    "cache_read_input_tokens": 223725,
    "output_tokens": 5246,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 29143,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 390,
        "cache_read_input_tokens": 37336,
        "cache_creation_input_tokens": 3648,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 3648
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 215635,
      "outputTokens": 5909,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 12,
      "costUSD": 0.36518000000000006,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 1824,
      "outputTokens": 5246,
      "cacheReadInputTokens": 223725,
      "cacheCreationInputTokens": 29143,
      "webSearchRequests": 0,
      "costUSD": 0.43427625000000003,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "389e5aa3-0125-4538-84fc-60b1639b3b43"
}
```

</details>

---
