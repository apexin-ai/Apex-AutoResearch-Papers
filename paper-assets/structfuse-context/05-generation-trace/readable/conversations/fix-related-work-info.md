# fix related work info

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/chats/worker_fix_related-work-info_20260514T224433.jsonl`
- **Structured JSON:** [`200404ebcc55de8befab.json`](../../sessions/20/200404ebcc55de8befab.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

15 recorded events

### Tool call

_source line 1 · 2026-05-14T22:45:26.271262+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_related-work-info_20260514T224433",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T22:45:26.271639+00:00_

1	# 2. Related Work
2	
3	## 2.1 Code Retrieval Methods
4	
5	Repo-level code retrieval aims to identify relevant files or code spans from large codebases given a bug report or issue description. Classical sparse retrieval via BM25 \cite{robertson2009bm25} remains a competitive baseline in this setting. The dense retrieval paradigm, pioneered by DPR \cite{karpukhin2020dpr} for open-domain question answering, has been increasingly adopted for code. SweRank \cite{reddy2025swerank} trains a retrieve-and-rerank pipeline for software issue localization, achieving state-of-the-art results on SWE-Bench-Lite and LocBench through text-based retrieval. SWE-Fixer \cite{xie2025swefixer} combines BM25 with a learned retriever in a coarse-to-fine file retrieval pipeline, demonstrating that sparse and dense retrieval are complementary. Both systems, however, treat code files as flat text and do not exploit structural relationships between files during training.
6	
7	A parallel line of work leverages code structure graphs at inference time to guide code navigation. LocAgent \cite{chen2025locagent} parses codebases into directed heterogeneous graphs and employs LLM agents for multi-hop graph reasoning during fault localization. RANGER \cite{shah2025ranger} constructs repository knowledge graphs with variable-level nodes and applies MCTS-guided graph exploration for retrieval. CodexGraph \cite{liu2025codexgraph} indexes codebases into graph databases queried via Cypher, while RepoGraph \cite{ouyang2025repograph} provides line-level code graph navigation as a plug-in module for software engineering agents. GraphCoder \cite{liu2024graphcoder} incorporates control-flow and data-dependence edges into code context graphs for coarse-to-fine retrieval, and ARISE \cite{seddik2026arise} exposes statement-level def-use edges for agentic fault localization—though both are limited to intra-procedural scope. These methods demonstrate the value of structural information for code retrieval, yet they 
…[truncated 5159 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_related-work-info_20260514T224433",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T22:45:26.271845+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__read_project_file",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_related-work-info_20260514T224433",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__read_project_file",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T22:45:26.271991+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_related-work-info_20260514T224433",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T22:45:26.272186+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "structfuse-context",
  "file": "literature_map.yaml",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_related-work-info_20260514T224433",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "structfuse-context",
    "file": "literature_map.yaml",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T22:45:26.272495+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml\", \"content\": \"# StructFuse — Related Work Literature Map\\n# 最后更新: 2026-05-14\\n# 说明: 只收录已验证存在的论文。每篇均经 WebSearch 确认标题/venue/year。\\n# 总计: 39 entries (含 2 个软件工具引用)\\n\\ncategories:\\n\\n  # ==========================================================================\\n  # Category 1: Code Retrieval for Bug Fixing / SWE-bench Ecosystem\\n  # ==========================================================================\\n  code_retrieval_bug_fixing:\\n    description: \\\"SWE-bench 及相关 repo-level 自动修复系统中的代码检索方法\\\"\\n    papers:\\n\\n      - title: \\\"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?\\\"\\n        authors: \\\"Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan\\\"\\n        venue: ICLR\\n        year: 2024\\n        relation: baseline\\n        summary: \\\"从 GitHub issues 构建 repo-level bug fixing benchmark，成为自动修复领域标准评估集。\\\"\\n\\n      - title: \\\"SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering\\\"\\n        authors: \\\"John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press\\\"\\n        venue: NeurIPS\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"基于 LLM agent 的交互式 bug fixing 系统，定义了 ACI 接口范式。\\\"\\n\\n      - title: \\\"AutoCodeRover: Autonomous Program Improvement\\\"\\n        authors: \\\"Yuntong Zhang, Haifeng Ruan, Zhiyu Fan, Abhik Roychoudhury\\\"\\n        venue: ISSTA\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"结合代码搜索与 spectrum-based fault localization，利用程序分析缩小修复范围。\\\"\\n\\n      - title: \\\"Agentless: Demystifying LLM-based Software Engineering Agents\\\"\\n        authors: \\\"Chunqiu Steven Xia, Yinlin Deng, Soren Dunn, Lingming Zhang\\\"\\n        venue: arXiv\\n        year: 2024\\n     
…[truncated 15730 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_related-work-info_20260514T224433",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T22:45:26.272731+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md",
  "old_string": "Critically, all graph-guided methods apply structural information exclusively at inference time",
  "new_string": "Critically, these graph-guided methods apply structural information exclusively at inference time"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_related-work-info_20260514T224433",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md",
    "old_string": "Critically, all graph-guided methods apply structural information exclusively at inference time",
    "new_string": "Critically, these graph-guided methods apply structural information exclusively at inference time"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T22:45:26.272905+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_related-work-info_20260514T224433",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T22:45:26.273034+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md",
  "old_string": "Contrastive learning has proven effective for learning code representations that capture functional semantics beyond surface-level patterns.",
  "new_string": "Building on the success of Sentence-BERT \\cite{reimers2019sentencebert} in learning dense sentence representations via siamese contrastive objectives, contrastive learning has proven effective for learning code representations that capture functional semantics beyond surface-level patterns."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_related-work-info_20260514T224433",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md",
    "old_string": "Contrastive learning has proven effective for learning code representations that capture functional semantics beyond surface-level patterns.",
    "new_string": "Building on the success of Sentence-BERT \\cite{reimers2019sentencebert} in learning dense sentence representations via siamese contrastive objectives, contrastive learning has proven effective for learning code representations that capture functional semantics beyond surface-level patterns."
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T22:45:26.273227+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_related-work-info_20260514T224433",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T22:45:26.273413+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md",
  "old_string": "simple static embedding-distance mining consistently improves retrieval performance",
  "new_string": "simple static embedding-distance mining consistently improves (pilot evidence; pending M2 full confirmation) retrieval performance"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_related-work-info_20260514T224433",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md",
    "old_string": "simple static embedding-distance mining consistently improves retrieval performance",
    "new_string": "simple static embedding-distance mining consistently improves (pilot evidence; pending M2 full confirmation) retrieval performance"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T22:45:26.273593+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_related-work-info_20260514T224433",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T22:45:26.273783+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "related_work_v1",
  "type": "paper",
  "description": "Related Work v1 draft — patched: §2.1 \"all→these\" graph-guided, §2.2 added Sentence-BERT citation, §2.3 added pilot evidence caveat to \"consistently improves\"",
  "project": "structfuse-context",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md",
  "tags": "['related-work', 'v1', 'patched']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_related-work-info_20260514T224433",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "related_work_v1",
    "type": "paper",
    "description": "Related Work v1 draft — patched: §2.1 \"all→these\" graph-guided, §2.2 added Sentence-BERT citation, §2.3 added pilot evidence caveat to \"consistently improves\"",
    "project": "structfuse-context",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md",
    "tags": "['related-work', 'v1', 'patched']"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T22:45:26.273944+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_dc54a3\", \"name\": \"related_work_v1\", \"type\": \"paper\", \"description\": \"Related Work v1 draft — patched: §2.1 \\\"all→these\\\" graph-guided, §2.2 added Sentence-BERT citation, §2.3 added pilot evidence caveat to \\\"consistently improves\\\"\", \"path\": \"projects/structfuse-context/artifacts/_project/paper/related_work_v1_dc54a3.md\", \"url\": null, \"project\": \"structfuse-context\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-14T22:45:19.439165+00:00\", \"tags\": [\"related-work\", \"v1\", \"patched\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_related-work-info_20260514T224433",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-14T22:45:26.274116+00:00_

三处修改完成：

1. **§2.1**: "all graph-guided methods" → "these graph-guided methods"
2. **§2.2**: 开头插入 Sentence-BERT 引用（`\cite{reimers2019sentencebert}`），自然衔接到对比学习在代码表示上的应用
3. **§2.3**: "consistently improves" 后加 "(pilot evidence; pending M2 full confirmation)"

注：Sentence-BERT 已在 literature_map.yaml 的 `hard_negative_mining` 类目下（category/role/year/venue/authors 均匹配），无需重复录入。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_fix_related-work-info_20260514T224433"
}
```

</details>

---
