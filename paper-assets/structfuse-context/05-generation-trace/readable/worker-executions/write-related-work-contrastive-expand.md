# write related work contrastive expand

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 94
- **Recorded user turns:** 0
- **Tool calls:** 33
- **Original source:** `logs/workers/worker_write_related-work-contrastive-expand_20260515T051038.log`
- **Structured JSON:** [`35c6b4db626db04a8310.json`](../../sessions/35/35c6b4db626db04a8310.json)

## Before a recorded user message

94 recorded events

### Log line

_source line 1_

Warning: no stdin data received in 3s, proceeding without it. If piping from a slow command, redirect stdin explicitly: < /dev/null to skip, or wait longer.

---

### System

_source line 2_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
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
  "uuid": "2c7920e4-8e63-4dd0-aa50-f0f069261822",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-structfuse-context/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Runtime record

_source line 3_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1778836200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "33c9ca94-8803-48e0-bfaf-78d61a15fe82",
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me break down this task:

1. Read existing literature map and related work drafts
2. WebSearch to verify each recommended paper
3. Write supplementary paragraphs for weak areas
4. Generate BibTeX entries
5. Output to specific files

Let me start by reading the existing files and searching for papers in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "4d8730e2-0bbc-404a-8d59-d3df1b1a2868",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JKvpNwSa46SrDAbhvekvYK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11707,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11707
      },
      "output_tokens": 33,
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

_source line 5_

开始执行。先读取现有文献和草稿。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "2f630600-9c30-43a2-b1de-771e45b60824",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JKvpNwSa46SrDAbhvekvYK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11707,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11707
      },
      "output_tokens": 33,
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

_source line 6_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Au4KpZ1ehbxdPxt6nrvFtb`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__append_idea,WebSearch,WebFetch",
  "max_results": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "003a204e-bfb3-4673-b583-ecde766bab71",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JKvpNwSa46SrDAbhvekvYK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11707,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11707
      },
      "output_tokens": 33,
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

_source line 7 · 2026-05-15T05:10:54.765Z_

<details><summary>↩ Tool result · `toolu_01Au4KpZ1ehbxdPxt6nrvFtb`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
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
  "tool_name": "mcp__agent-ml-research__append_idea"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
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
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "ac22db43-a767-4d96-9293-20d78dc56068",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__append_idea",
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__append_idea,WebSearch,WebFetch",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 8_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the existing literature map and find related work drafts in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "352a776b-821b-4ccd-9398-fe9c1a190861",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JB3Hb8XcuX1rcw8wJJHAH2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1997,
      "cache_read_input_tokens": 23548,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1997
      },
      "output_tokens": 41,
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_012rxBynKzFSCBmuvAGHc221`</summary>

```json
{
  "project": "structfuse-context",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "bfb4278d-8c1c-42a1-8a5b-731cd8e2334f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JB3Hb8XcuX1rcw8wJJHAH2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1997,
      "cache_read_input_tokens": 23548,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1997
      },
      "output_tokens": 41,
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

_source line 10 · 2026-05-15T05:10:58.400Z_

<details><summary>↩ Tool result · `toolu_012rxBynKzFSCBmuvAGHc221`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml\", \"content\": \"# StructFuse — Related Work Literature Map\\n# 最后更新: 2026-05-14\\n# 说明: 只收录已验证存在的论文。每篇均经 WebSearch 确认标题/venue/year。\\n# 总计: 39 entries (含 2 个软件工具引用)\\n\\ncategories:\\n\\n  # ==========================================================================\\n  # Category 1: Code Retrieval for Bug Fixing / SWE-bench Ecosystem\\n  # ==========================================================================\\n  code_retrieval_bug_fixing:\\n    description: \\\"SWE-bench 及相关 repo-level 自动修复系统中的代码检索方法\\\"\\n    papers:\\n\\n      - title: \\\"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?\\\"\\n        authors: \\\"Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan\\\"\\n        venue: ICLR\\n        year: 2024\\n        relation: baseline\\n        summary: \\\"从 GitHub issues 构建 repo-level bug fixing benchmark，成为自动修复领域标准评估集。\\\"\\n\\n      - title: \\\"SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering\\\"\\n        authors: \\\"John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press\\\"\\n        venue: NeurIPS\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"基于 LLM agent 的交互式 bug fixing 系统，定义了 ACI 接口范式。\\\"\\n\\n      - title: \\\"AutoCodeRover: Autonomous Program Improvement\\\"\\n        authors: \\\"Yuntong Zhang, Haifeng Ruan, Zhiyu Fan, Abhik Roychoudhury\\\"\\n        venue: ISSTA\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"结合代码搜索与 spectrum-based fault localization，利用程序分析缩小修复范围。\\\"\\n\\n      - title: \\\"Agentless: Demystifying LLM-based Software Engineering Agents\\\"\\n        authors: \\\"Chunqiu Steven Xia, Yinlin Deng, Soren Dunn, Lingming Zhang\\\"\\n        venue: arXiv\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"无 agent 架构的 two-phase localize-then-repair 方法，在 SWE-bench 上取得强 baseline。\\\"\\n\\n      - title: \\\"SWE-smith: Scaling Data for Software Engineering Agents\\\"\\n        authors: \\\"John Yang, Kilian Lieret, Carlos E. Jimenez, Alexander Wettig, Kabir Khandpur, Yanzhe Zhang, Binyuan Hui, Ofir Press, Ludwig Schmidt, Diyi Yang\\\"\\n        venue: \\\"NeurIPS (Datasets & Benchmarks, Spotlight)\\\"\\n        year: 2025\\n        relation: building-block\\n        summary: \\\"自动从 GitHub 生成大规模 SWE-bench 风格训练数据，StructFuse 用其 repos 做 data-flow 提取。\\\"\\n\\n      - title: \\\"RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems\\\"\\n        authors: \\\"Tianyang Liu, Canwen Xu, Julian McAuley\\\"\\n        venue: ICLR\\n        year: 2024\\n        relation: baseline\\n        summary: \\\"Repo-level 代码补全/检索 benchmark，含 RepoBench-R 检索子任务。\\\"\\n\\n      - title: \\\"SweRank: Software Issue Localization with Code Ranking\\\"\\n        authors: \\\"Revanth Gangi Reddy, Tarun Suresh, JaeHyeok Doo, Ye Liu, Xuan Phi Nguyen, Yingbo Zhou, Semih Yavuz, Caiming Xiong, Heng Ji, Shafiq Joty\\\"\\n        venue: arXiv\\n        year: 2025\\n        relation: competitor\\n        summary: \\\"Retrieve-and-rerank 框架用于 software issue localization，在 SWE-Bench-Lite 和 LocBench 上 SOTA，text-based retrieval baseline。\\\"\\n\\n      - title: \\\"SWE-Fixer: Training Open-Source LLMs for Effective and Efficient GitHub Issue Resolution\\\"\\n        authors: \\\"Chengxing Xie, Bowen Li, Chang Gao, He Du, Wai Lam, Difan Zou, Kai Chen\\\"\\n        venue: \\\"ACL (Findings)\\\"\\n        year: 2025\\n        relation: competitor\\n        summary: \\\"BM25 + LLM retriever 的 coarse-to-fine file retrieval pipeline，在 SWE-Bench Verified 上 30.2%。\\\"\\n\\n  # ==========================================================================\\n  # Category 2: Hard Negative Mining in Contrastive Learning\\n  # ==========================================================================\\n  hard_negative_mining:\\n    description: \\\"对比学习中 hard negative 挖掘策略，以及密集检索中的负样本选择\\\"\\n    papers:\\n\\n      - title: \\\"Dense Passage Retrieval for Open-Domain Question Answering\\\"\\n        authors: \\\"Vladimir Karpukhin, Barlas Oguz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, Wen-tau Yih\\\"\\n        venue: EMNLP\\n        year: 2020\\n        relation: background\\n        summary: \\\"DPR 开创了 in-batch negatives + BM25 hard negatives 的双塔检索范式。\\\"\\n\\n      - title: \\\"Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval\\\"\\n        authors: \\\"Lee Xiong, Chenyan Xiong, Ye Li, Kwok-Fung Tang, Jialin Liu, Paul Bennett, Junaid Ahmed, Arnold Overwijk\\\"\\n        venue: ICLR\\n        year: 2021\\n        relation: background\\n        summary: \\\"ANCE 用 ANN index 动态挖掘 embedding-distance hard negatives，StructFuse 的 baseline negative 策略之一。\\\"\\n\\n      - title: \\\"A Simple Framework for Contrastive Learning of Visual Representations\\\"\\n        authors: \\\"Ting Chen, Simon Kornblith, Mohammad Norouzi, Geoffrey Hinton\\\"\\n        venue: ICML\\n        year: 2020\\n        relation: background\\n        summary: \\\"SimCLR 视觉对比学习奠基工作，证明 hard negatives 和大 batch size 对对比学习的重要性。\\\"\\n\\n      - title: \\\"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\\\"\\n        authors: \\\"Nils Reimers, Iryna Gurevych\\\"\\n        venue: EMNLP\\n        year: 2019\\n        relation: background\\n        summary: \\\"Siamese/triplet 网络训练句子嵌入，StructFuse 的对比训练框架与其类似。\\\"\\n\\n      - title: \\\"Curriculum Learning for Dense Retrieval Distillation\\\"\\n        authors: \\\"Hansi Zeng, Hamed Zamani, Vishwa Vinay\\\"\\n        venue: \\\"SIGIR (Best Short Paper)\\\"\\n        year: 2022\\n        relation: background\\n        summary: \\\"CL-DRD: 课程学习式知识蒸馏用于密集检索，从粗粒度到细粒度逐步增加训练难度。\\\"\\n\\n      - title: \\\"Effective Hard Negative Mining for Contrastive Learning-Based Code Search\\\"\\n        authors: \\\"Fan Y., Li C., Ge J., Huang L., Luo B.\\\"\\n        venue: \\\"ACM TOSEM\\\"\\n        year: 2025\\n        relation: contrast-target\\n        summary: \\\"CoCoHaNeRe: 提出可微分 hard negative 机制用于代码搜索对比学习。其对 hard negative 机制的处理与 StructFuse 的发现形成关键对照——StructFuse 证明 true embedding-distance mining 即可持续提升性能。\\\"\\n        note: \\\"关键引用：StructFuse Claim 1 的 correction target。CoCoHaNeRe 论点是非可微 embedding negatives 学习'slow and ineffective'，StructFuse 证明用 true embedding distance mining 仍然有效。\\\"\\n\\n  # ==========================================================================\\n  # Category 3: Contrastive Learning for Code\\n  # ==========================================================================\\n  contrastive_code_learning:\\n    description: \\\"代码领域的对比学习方法，训练时利用代码特性构建正负样本\\\"\\n    papers:\\n\\n      - title: \\\"Contrastive Code Representation Learning\\\"\\n        authors: \\\"Paras Jain, Ajay Jain, Tianjun Zhang, Pieter Abbeel, Joseph Gonzalez, Ion Stoica\\\"\\n        venue: EMNLP\\n        year: 2021\\n        relation: background\\n        summary: \\\"ContraCode: 自监督对比预训练，通过编译器变换生成功能等价的程序变体，学习代码功能而非表面形式。\\\"\\n\\n      - title: \\\"CodeRetriever: A Large Scale Contrastive Pre-Training Method for Code Search\\\"\\n        authors: \\\"Xiaonan Li, Yeyun Gong, Yelong Shen, Xipeng Qiu, Hang Zhang, Bolun Yao, Weizhen Qi, Daxin Jiang, Weizhu Chen, Nan Duan\\\"\\n        venue: EMNLP\\n        year: 2022\\n        relation: background\\n        summary: \\\"结合 unimodal (code-code) 和 bimodal (code-text) 对比学习预训练代码表示，在 11 个代码搜索 benchmark 上 SOTA。\\\"\\n\\n      - title: \\\"Towards Learning (Dis)-Similarity of Source Code from Program Contrasts\\\"\\n        authors: \\\"Yangruibo Ding, Luca Buratti, Saurabh Pujar, Alessandro Morari, Baishakhi Ray, Saikat Chakraborty\\\"\\n        venue: \\\"ACL (Long Papers)\\\"\\n        year: 2022\\n        relation: background\\n        summary: \\\"利用程序结构和功能属性构建对比样本对，学习代码相似性/差异性表示。\\\"\\n\\n  # ==========================================================================\\n  # Category 4: Program Analysis for ML\\n  # ==========================================================================\\n  program_analysis_for_ml:\\n    description: \\\"静态分析辅助 ML，结构信息在代码表示学习中的应用\\\"\\n    papers:\\n\\n      - title: \\\"CodeQL: Semantic Code Analysis Engine\\\"\\n        authors: \\\"GitHub / Semmle\\\"\\n        venue: \\\"Tool (open-source)\\\"\\n        year: 2019\\n        relation: building-block\\n        summary: \\\"基于 Datalog 的代码查询引擎，支持 inter-procedural data-flow 分析。StructFuse 用它提取 scope-bounded data-flow graph。\\\"\\n\\n      - title: \\\"code2vec: Learning Distributed Representations of Code\\\"\\n        authors: \\\"Uri Alon, Meital Zilberstein, Omer Levy, Eran Yahav\\\"\\n        venue: POPL\\n        year: 2019\\n        relation: background\\n        summary: \\\"用 AST path 学习代码向量表示，首次大规模证明结构信息对代码表示学习的价值。\\\"\\n\\n      - title: \\\"code2seq: Generating Sequences from Structured Representations of Code\\\"\\n        authors: \\\"Uri Alon, Shaked Brody, Omer Levy, Eran Yahav\\\"\\n        venue: ICLR\\n        year: 2019\\n        relation: background\\n        summary: \\\"code2vec 的序列生成扩展，用 AST path attention 生成方法名摘要。\\\"\\n\\n      - title: \\\"Detecting Code Clones with Graph Neural Network and Flow-Augmented Abstract Syntax Tree\\\"\\n        authors: \\\"Wenhan Wang, Ge Li, Bo Ma, Xin Xia, Zhi Jin\\\"\\n        venue: SANER\\n        year: 2020\\n        relation: background\\n        summary: \\\"FA-AST: 用 data-flow 增强 AST 进行代码克隆检测，与 StructFuse 用 data-flow 做 hard negative 挖掘思路相关。\\\"\\n\\n      - title: \\\"GraphCodeBERT: Pre-training Code Representations with Data Flow\\\"\\n        authors: \\\"Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan, Alexey Svyatkovskiy, Shengyu Fu, Michele Tufano, Shao Kun Deng, Colin Clement, Dawn Drain, Neel Sundaresan, Jian Yin, Daxin Jiang, Ming Zhou\\\"\\n        venue: ICLR\\n        year: 2021\\n        relation: background\\n        summary: \\\"在预训练中引入 data-flow edge，证明 data-flow 信息提升代码理解任务。StructFuse 的 insight 与此相关但用途不同（hard negative mining vs pre-training）。\\\"\\n\\n      - title: \\\"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair\\\"\\n        authors: \\\"Shahd Seddik, Fatemeh Fard\\\"\\n        venue: arXiv\\n        year: 2026\\n        relation: contrast\\n        summary: \\\"用 multi-granularity program graph（含 intra-procedural def-use edges）辅助 LLM agent 做 fault localization。仅 intra-procedural + runtime tool calls，与 StructFuse 的 inter-procedural static mining 互补。\\\"\\n\\n  # ==========================================================================\\n  # Category 5: Code Embeddings / Code Search\\n  # ==========================================================================\\n  code_embeddings_search:\\n    description: \\\"代码嵌入模型和代码搜索方法\\\"\\n    papers:\\n\\n      - title: \\\"CodeSearchNet Challenge: Evaluating the State of Semantic Code Search\\\"\\n        authors: \\\"Hamel Husain, Ho-Hsiang Wu, Tiferet Gazit, Miltiadis Allamanis, Marc Brockschmidt\\\"\\n        venue: arXiv\\n        year: 2019\\n        relation: background\\n        summary: \\\"代码语义搜索 benchmark 和数据集，推动了代码嵌入模型的发展。\\\"\\n\\n      - title: \\\"CodeBERT: A Pre-Trained Model for Programming and Natural Languages\\\"\\n        authors: \\\"Zhangyin Feng, Daya Guo, Duyu Tang, Nan Duan, Xiaocheng Feng, Ming Gong, Lixin Zou, Bing Qin, Ting Liu, Daxin Jiang, Ming Zhou\\\"\\n        venue: \\\"EMNLP (Findings)\\\"\\n        year: 2020\\n        relation: background\\n        summary: \\\"首个编程语言-自然语言双模态预训练模型，代码嵌入的早期里程碑。\\\"\\n\\n      - title: \\\"UniXcoder: Unified Cross-Modal Pre-training for Code Representation\\\"\\n        authors: \\\"Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou, Jian Yin\\\"\\n        venue: ACL\\n        year: 2022\\n        relation: background\\n        summary: \\\"统一跨模态代码预训练，在代码搜索等任务上取得 SOTA。\\\"\\n\\n      - title: \\\"StarCoder: May the Source Be with You!\\\"\\n        authors: \\\"Raymond Li, Loubna Ben Allal, et al. (BigCode)\\\"\\n        venue: TMLR\\n        year: 2023\\n        relation: building-block\\n        summary: \\\"大规模开源代码 LLM，StructFuse 用 StarCoder2-3B 作为对比学习检索器的 backbone 之一。\\\"\\n\\n      - title: \\\"Code Llama: Open Foundation Models for Code\\\"\\n        authors: \\\"Baptiste Roziere, Jonas Gehring, Fabian Gloeckle, et al. (Meta AI)\\\"\\n        venue: arXiv\\n        year: 2023\\n        relation: background\\n        summary: \\\"Meta 的代码大模型系列，基于 Llama 2 微调。\\\"\\n\\n      - title: \\\"Qwen2.5-Coder Technical Report\\\"\\n        authors: \\\"Binyuan Hui, Jian Yang, Zeyu Cui, et al. (Qwen Team, Alibaba)\\\"\\n        venue: arXiv\\n        year: 2024\\n        relation: building-block\\n        summary: \\\"Qwen 代码模型系列，StructFuse 用 Qwen2.5-Coder-3B 作为对比学习检索器的 backbone。\\\"\\n\\n      - title: \\\"DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence\\\"\\n        authors: \\\"Daya Guo, Qihao Zhu, Dejian Yang, Zhenda Xie, Kai Dong, Wentao Zhang, Guanting Chen, Xiao Bi, Yu Wu, Y.K. Li, Fuli Luo, Yingfei Xiong, Wenfeng Liang\\\"\\n        venue: arXiv\\n        year: 2024\\n        relation: background\\n        summary: \\\"开源代码 LLM 系列 (1.3B-33B)，project-level 代码训练 + 16K context + fill-in-the-blank 预训练。\\\"\\n\\n      - title: \\\"RepoFusion: Training Code Models to Understand Your Repository\\\"\\n        authors: \\\"Disha Shrivastava, Denis Kocetkov, Harm de Vries, Dzmitry Bahdanau, Torsten Scholak\\\"\\n        venue: arXiv\\n        year: 2023\\n        relation: background\\n        summary: \\\"训练代码模型融合多个 cross-file repo context 进行代码补全，小模型 + repo context 可匹配大模型性能。\\\"\\n\\n      - title: \\\"BM25\\\"\\n        authors: \\\"Stephen Robertson, Hugo Zaragoza\\\"\\n        venue: \\\"Foundations and Trends in Information Retrieval\\\"\\n        year: 2009\\n        relation: baseline\\n        summary: \\\"经典稀疏检索方法，StructFuse 的 baseline 之一。\\\"\\n\\n  # ==========================================================================\\n  # Category 6: Graph-Guided Code Navigation (Inference-Time)\\n  # ==========================================================================\\n  graph_guided_inference:\\n    description: \\\"推理时利用代码结构图辅助导航/检索的方法（与 StructFuse 的训练时结构信号互补）\\\"\\n    papers:\\n\\n      - title: \\\"LocAgent: Graph-Guided LLM Agents for Code Localization\\\"\\n        authors: \\\"Zhaoling Chen, Robert Tang, Gangda Deng, Fang Wu, Jialong Wu, Zhiwei Jiang, Viktor Prasanna, Arman Cohan, Xingyao Wang\\\"\\n        venue: ACL\\n        year: 2025\\n        relation: contrast\\n        summary: \\\"将代码库解析为有向异构图，LLM agent 通过 multi-hop 推理在图上导航做代码定位。推理时用结构图，StructFuse 训练时用。\\\"\\n\\n      - title: \\\"CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases\\\"\\n        authors: \\\"Xiangyan Liu, Bo Lan, Zhiyuan Hu, Yang Liu, Zhicheng Zhang, Fei Wang, Michael Qizhe Shieh, Wenmeng Zhou\\\"\\n        venue: NAACL\\n        year: 2025\\n        relation: contrast\\n        summary: \\\"将代码库索引到图数据库，LLM agent 通过 graph query 接口检索结构化上下文。\\\"\\n\\n      - title: \\\"RANGER: Repository-Level Agent for Graph-Enhanced Retrieval\\\"\\n        authors: \\\"Pratik Shah, Rajat Ghosh, Aryan Singhal, Debojyoti Dutta\\\"\\n        venue: arXiv\\n        year: 2025\\n        relation: contrast\\n        summary: \\\"构建 repo 知识图（含 variable-level 节点），dual-stage retrieval: Cypher lookup + MCTS-guided graph exploration。\\\"\\n\\n      - title: \\\"RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph\\\"\\n        authors: \\\"Siru Ouyang, Wenhao Yu, Kaixin Ma, Zilin Xiao, Zhihan Zhang, Mengzhao Jia, Jiawei Han, Hongming Zhang, Dong Yu\\\"\\n        venue: ICLR\\n        year: 2025\\n        relation: contrast\\n        summary: \\\"以代码行为节点构建 repo-level 代码图，作为 SE agent 的 plug-in 导航模块。推理时逐行图导航，与 StructFuse 训练时批量提取结构信号互补。\\\"\\n\\n      - title: \\\"GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph\\\"\\n        authors: \\\"Wei Liu, Ailun Yu, Daoguang Zan, Bo Shen, Wei Zhang, Haiyan Zhao, Zhi Jin, Qianxiang Wang\\\"\\n        venue: ASE\\n        year: 2024\\n        relation: contrast\\n        summary: \\\"构建 code context graph（含 control-flow 和 data-dependence edges）进行 coarse-to-fine 检索辅助代码补全。使用 intra-procedural data-flow，与 StructFuse 的 inter-procedural scope 形成对比。\\\"\\n\\n  # ==========================================================================\\n  # Category 7: Infrastructure / Tools\\n  # ==========================================================================\\n  infrastructure:\\n    description: \\\"StructFuse 依赖的核心基础设施和工具\\\"\\n    papers:\\n\\n      - title: \\\"Billion-Scale Similarity Search with GPUs\\\"\\n        authors: \\\"Jeff Johnson, Matthijs Douze, Herve Jegou\\\"\\n        venue: \\\"IEEE Transactions on Big Data\\\"\\n        year: 2021\\n        relation: building-block\\n        summary: \\\"FAISS: GPU 加速的大规模向量相似度搜索库，StructFuse 用于 ANN-based hard negative mining。\\\"\\n\\n      - title: \\\"Tree-sitter: An Incremental Parsing System for Programming Tools\\\"\\n        authors: \\\"Max Brunsfeld et al.\\\"\\n        venue: \\\"Software (Zenodo DOI: 10.5281/zenodo.13375512)\\\"\\n        year: 2018\\n        relation: building-block\\n        summary: \\\"增量解析库，高效构建和更新 concrete syntax trees。与 CodeQL 互补用于代码结构提取。\\\"\\n        note: \\\"软件工具，无正式论文。引用 Zenodo DOI 或 GitHub repo。\\\"\\n\", \"total_chars\": 15999, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "d49e0577-c19a-4491-b18a-68fc20bd9695",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml\\\", \\\"content\\\": \\\"# StructFuse — Related Work Literature Map\\\\n# 最后更新: 2026-05-14\\\\n# 说明: 只收录已验证存在的论文。每篇均经 WebSearch 确认标题/venue/year。\\\\n# 总计: 39 entries (含 2 个软件工具引用)\\\\n\\\\ncategories:\\\\n\\\\n  # ==========================================================================\\\\n  # Category 1: Code Retrieval for Bug Fixing / SWE-bench Ecosystem\\\\n  # ==========================================================================\\\\n  code_retrieval_bug_fixing:\\\\n    description: \\\\\\\"SWE-bench 及相关 repo-level 自动修复系统中的代码检索方法\\\\\\\"\\\\n    papers:\\\\n\\\\n      - title: \\\\\\\"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?\\\\\\\"\\\\n        authors: \\\\\\\"Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan\\\\\\\"\\\\n        venue: ICLR\\\\n        year: 2024\\\\n        relation: baseline\\\\n        summary: \\\\\\\"从 GitHub issues 构建 repo-level bug fixing benchmark，成为自动修复领域标准评估集。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering\\\\\\\"\\\\n        authors: \\\\\\\"John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press\\\\\\\"\\\\n        venue: NeurIPS\\\\n        year: 2024\\\\n        relation: competitor\\\\n        summary: \\\\\\\"基于 LLM agent 的交互式 bug fixing 系统，定义了 ACI 接口范式。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"AutoCodeRover: Autonomous Program Improvement\\\\\\\"\\\\n        authors: \\\\\\\"Yuntong Zhang, Haifeng Ruan, Zhiyu Fan, Abhik Roychoudhury\\\\\\\"\\\\n        venue: ISSTA\\\\n        year: 2024\\\\n        relation: competitor\\\\n        summary: \\\\\\\"结合代码搜索与 spectrum-based fault localization，利用程序分析缩小修复范围。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Agentless: Demystifying LLM-based Software Engineering Agents\\\\\\\"\\\\n        authors: \\\\\\\"Chunqiu Steven Xia, Yinlin Deng, Soren Dunn, Lingming Zhang\\\\\\\"\\\\n        venue: arXiv\\\\n        year: 2024\\\\n        relation: competitor\\\\n        summary: \\\\\\\"无 agent 架构的 two-phase localize-then-repair 方法，在 SWE-bench 上取得强 baseline。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"SWE-smith: Scaling Data for Software Engineering Agents\\\\\\\"\\\\n        authors: \\\\\\\"John Yang, Kilian Lieret, Carlos E. Jimenez, Alexander Wettig, Kabir Khandpur, Yanzhe Zhang, Binyuan Hui, Ofir Press, Ludwig Schmidt, Diyi Yang\\\\\\\"\\\\n        venue: \\\\\\\"NeurIPS (Datasets & Benchmarks, Spotlight)\\\\\\\"\\\\n        year: 2025\\\\n        relation: building-block\\\\n        summary: \\\\\\\"自动从 GitHub 生成大规模 SWE-bench 风格训练数据，StructFuse 用其 repos 做 data-flow 提取。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems\\\\\\\"\\\\n        authors: \\\\\\\"Tianyang Liu, Canwen Xu, Julian McAuley\\\\\\\"\\\\n        venue: ICLR\\\\n        year: 2024\\\\n        relation: baseline\\\\n        summary: \\\\\\\"Repo-level 代码补全/检索 benchmark，含 RepoBench-R 检索子任务。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"SweRank: Software Issue Localization with Code Ranking\\\\\\\"\\\\n        authors: \\\\\\\"Revanth Gangi Reddy, Tarun Suresh, JaeHyeok Doo, Ye Liu, Xuan Phi Nguyen, Yingbo Zhou, Semih Yavuz, Caiming Xiong, Heng Ji, Shafiq Joty\\\\\\\"\\\\n        venue: arXiv\\\\n        year: 2025\\\\n        relation: competitor\\\\n        summary: \\\\\\\"Retrieve-and-rerank 框架用于 software issue localization，在 SWE-Bench-Lite 和 LocBench 上 SOTA，text-based retrieval baseline。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"SWE-Fixer: Training Open-Source LLMs for Effective and Efficient GitHub Issue Resolution\\\\\\\"\\\\n        authors: \\\\\\\"Chengxing Xie, Bowen Li, Chang Gao, He Du, Wai Lam, Difan Zou, Kai Chen\\\\\\\"\\\\n        venue: \\\\\\\"ACL (Findings)\\\\\\\"\\\\n        year: 2025\\\\n        relation: competitor\\\\n        summary: \\\\\\\"BM25 + LLM retriever 的 coarse-to-fine file retrieval pipeline，在 SWE-Bench Verified 上 30.2%。\\\\\\\"\\\\n\\\\n  # ==========================================================================\\\\n  # Category 2: Hard Negative Mining in Contrastive Learning\\\\n  # ==========================================================================\\\\n  hard_negative_mining:\\\\n    description: \\\\\\\"对比学习中 hard negative 挖掘策略，以及密集检索中的负样本选择\\\\\\\"\\\\n    papers:\\\\n\\\\n      - title: \\\\\\\"Dense Passage Retrieval for Open-Domain Question Answering\\\\\\\"\\\\n        authors: \\\\\\\"Vladimir Karpukhin, Barlas Oguz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, Wen-tau Yih\\\\\\\"\\\\n        venue: EMNLP\\\\n        year: 2020\\\\n        relation: background\\\\n        summary: \\\\\\\"DPR 开创了 in-batch negatives + BM25 hard negatives 的双塔检索范式。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval\\\\\\\"\\\\n        authors: \\\\\\\"Lee Xiong, Chenyan Xiong, Ye Li, Kwok-Fung Tang, Jialin Liu, Paul Bennett, Junaid Ahmed, Arnold Overwijk\\\\\\\"\\\\n        venue: ICLR\\\\n        year: 2021\\\\n        relation: background\\\\n        summary: \\\\\\\"ANCE 用 ANN index 动态挖掘 embedding-distance hard negatives，StructFuse 的 baseline negative 策略之一。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"A Simple Framework for Contrastive Learning of Visual Representations\\\\\\\"\\\\n        authors: \\\\\\\"Ting Chen, Simon Kornblith, Mohammad Norouzi, Geoffrey Hinton\\\\\\\"\\\\n        venue: ICML\\\\n        year: 2020\\\\n        relation: background\\\\n        summary: \\\\\\\"SimCLR 视觉对比学习奠基工作，证明 hard negatives 和大 batch size 对对比学习的重要性。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\\\\\\\"\\\\n        authors: \\\\\\\"Nils Reimers, Iryna Gurevych\\\\\\\"\\\\n        venue: EMNLP\\\\n        year: 2019\\\\n        relation: background\\\\n        summary: \\\\\\\"Siamese/triplet 网络训练句子嵌入，StructFuse 的对比训练框架与其类似。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Curriculum Learning for Dense Retrieval Distillation\\\\\\\"\\\\n        authors: \\\\\\\"Hansi Zeng, Hamed Zamani, Vishwa Vinay\\\\\\\"\\\\n        venue: \\\\\\\"SIGIR (Best Short Paper)\\\\\\\"\\\\n        year: 2022\\\\n        relation: background\\\\n        summary: \\\\\\\"CL-DRD: 课程学习式知识蒸馏用于密集检索，从粗粒度到细粒度逐步增加训练难度。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Effective Hard Negative Mining for Contrastive Learning-Based Code Search\\\\\\\"\\\\n        authors: \\\\\\\"Fan Y., Li C., Ge J., Huang L., Luo B.\\\\\\\"\\\\n        venue: \\\\\\\"ACM TOSEM\\\\\\\"\\\\n        year: 2025\\\\n        relation: contrast-target\\\\n        summary: \\\\\\\"CoCoHaNeRe: 提出可微分 hard negative 机制用于代码搜索对比学习。其对 hard negative 机制的处理与 StructFuse 的发现形成关键对照——StructFuse 证明 true embedding-distance mining 即可持续提升性能。\\\\\\\"\\\\n        note: \\\\\\\"关键引用：StructFuse Claim 1 的 correction target。CoCoHaNeRe 论点是非可微 embedding negatives 学习'slow and ineffective'，StructFuse 证明用 true embedding distance mining 仍然有效。\\\\\\\"\\\\n\\\\n  # ==========================================================================\\\\n  # Category 3: Contrastive Learning for Code\\\\n  # ==========================================================================\\\\n  contrastive_code_learning:\\\\n    description: \\\\\\\"代码领域的对比学习方法，训练时利用代码特性构建正负样本\\\\\\\"\\\\n    papers:\\\\n\\\\n      - title: \\\\\\\"Contrastive Code Representation Learning\\\\\\\"\\\\n        authors: \\\\\\\"Paras Jain, Ajay Jain, Tianjun Zhang, Pieter Abbeel, Joseph Gonzalez, Ion Stoica\\\\\\\"\\\\n        venue: EMNLP\\\\n        year: 2021\\\\n        relation: background\\\\n        summary: \\\\\\\"ContraCode: 自监督对比预训练，通过编译器变换生成功能等价的程序变体，学习代码功能而非表面形式。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"CodeRetriever: A Large Scale Contrastive Pre-Training Method for Code Search\\\\\\\"\\\\n        authors: \\\\\\\"Xiaonan Li, Yeyun Gong, Yelong Shen, Xipeng Qiu, Hang Zhang, Bolun Yao, Weizhen Qi, Daxin Jiang, Weizhu Chen, Nan Duan\\\\\\\"\\\\n        venue: EMNLP\\\\n        year: 2022\\\\n        relation: background\\\\n        summary: \\\\\\\"结合 unimodal (code-code) 和 bimodal (code-text) 对比学习预训练代码表示，在 11 个代码搜索 benchmark 上 SOTA。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Towards Learning (Dis)-Similarity of Source Code from Program Contrasts\\\\\\\"\\\\n        authors: \\\\\\\"Yangruibo Ding, Luca Buratti, Saurabh Pujar, Alessandro Morari, Baishakhi Ray, Saikat Chakraborty\\\\\\\"\\\\n        venue: \\\\\\\"ACL (Long Papers)\\\\\\\"\\\\n        year: 2022\\\\n        relation: background\\\\n        summary: \\\\\\\"利用程序结构和功能属性构建对比样本对，学习代码相似性/差异性表示。\\\\\\\"\\\\n\\\\n  # ==========================================================================\\\\n  # Category 4: Program Analysis for ML\\\\n  # ==========================================================================\\\\n  program_analysis_for_ml:\\\\n    description: \\\\\\\"静态分析辅助 ML，结构信息在代码表示学习中的应用\\\\\\\"\\\\n    papers:\\\\n\\\\n      - title: \\\\\\\"CodeQL: Semantic Code Analysis Engine\\\\\\\"\\\\n        authors: \\\\\\\"GitHub / Semmle\\\\\\\"\\\\n        venue: \\\\\\\"Tool (open-source)\\\\\\\"\\\\n        year: 2019\\\\n        relation: building-block\\\\n        summary: \\\\\\\"基于 Datalog 的代码查询引擎，支持 inter-procedural data-flow 分析。StructFuse 用它提取 scope-bounded data-flow graph。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"code2vec: Learning Distributed Representations of Code\\\\\\\"\\\\n        authors: \\\\\\\"Uri Alon, Meital Zilberstein, Omer Levy, Eran Yahav\\\\\\\"\\\\n        venue: POPL\\\\n        year: 2019\\\\n        relation: background\\\\n        summary: \\\\\\\"用 AST path 学习代码向量表示，首次大规模证明结构信息对代码表示学习的价值。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"code2seq: Generating Sequences from Structured Representations of Code\\\\\\\"\\\\n        authors: \\\\\\\"Uri Alon, Shaked Brody, Omer Levy, Eran Yahav\\\\\\\"\\\\n        venue: ICLR\\\\n        year: 2019\\\\n        relation: background\\\\n        summary: \\\\\\\"code2vec 的序列生成扩展，用 AST path attention 生成方法名摘要。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Detecting Code Clones with Graph Neural Network and Flow-Augmented Abstract Syntax Tree\\\\\\\"\\\\n        authors: \\\\\\\"Wenhan Wang, Ge Li, Bo Ma, Xin Xia, Zhi Jin\\\\\\\"\\\\n        venue: SANER\\\\n        year: 2020\\\\n        relation: background\\\\n        summary: \\\\\\\"FA-AST: 用 data-flow 增强 AST 进行代码克隆检测，与 StructFuse 用 data-flow 做 hard negative 挖掘思路相关。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"GraphCodeBERT: Pre-training Code Representations with Data Flow\\\\\\\"\\\\n        authors: \\\\\\\"Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan, Alexey Svyatkovskiy, Shengyu Fu, Michele Tufano, Shao Kun Deng, Colin Clement, Dawn Drain, Neel Sundaresan, Jian Yin, Daxin Jiang, Ming Zhou\\\\\\\"\\\\n        venue: ICLR\\\\n        year: 2021\\\\n        relation: background\\\\n        summary: \\\\\\\"在预训练中引入 data-flow edge，证明 data-flow 信息提升代码理解任务。StructFuse 的 insight 与此相关但用途不同（hard negative mining vs pre-training）。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair\\\\\\\"\\\\n        authors: \\\\\\\"Shahd Seddik, Fatemeh Fard\\\\\\\"\\\\n        venue: arXiv\\\\n        year: 2026\\\\n        relation: contrast\\\\n        summary: \\\\\\\"用 multi-granularity program graph（含 intra-procedural def-use edges）辅助 LLM agent 做 fault localization。仅 intra-procedural + runtime tool calls，与 StructFuse 的 inter-procedural static mining 互补。\\\\\\\"\\\\n\\\\n  # ==========================================================================\\\\n  # Category 5: Code Embeddings / Code Search\\\\n  # ==========================================================================\\\\n  code_embeddings_search:\\\\n    description: \\\\\\\"代码嵌入模型和代码搜索方法\\\\\\\"\\\\n    papers:\\\\n\\\\n      - title: \\\\\\\"CodeSearchNet Challenge: Evaluating the State of Semantic Code Search\\\\\\\"\\\\n        authors: \\\\\\\"Hamel Husain, Ho-Hsiang Wu, Tiferet Gazit, Miltiadis Allamanis, Marc Brockschmidt\\\\\\\"\\\\n        venue: arXiv\\\\n        year: 2019\\\\n        relation: background\\\\n        summary: \\\\\\\"代码语义搜索 benchmark 和数据集，推动了代码嵌入模型的发展。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"CodeBERT: A Pre-Trained Model for Programming and Natural Languages\\\\\\\"\\\\n        authors: \\\\\\\"Zhangyin Feng, Daya Guo, Duyu Tang, Nan Duan, Xiaocheng Feng, Ming Gong, Lixin Zou, Bing Qin, Ting Liu, Daxin Jiang, Ming Zhou\\\\\\\"\\\\n        venue: \\\\\\\"EMNLP (Findings)\\\\\\\"\\\\n        year: 2020\\\\n        relation: background\\\\n        summary: \\\\\\\"首个编程语言-自然语言双模态预训练模型，代码嵌入的早期里程碑。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"UniXcoder: Unified Cross-Modal Pre-training for Code Representation\\\\\\\"\\\\n        authors: \\\\\\\"Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou, Jian Yin\\\\\\\"\\\\n        venue: ACL\\\\n        year: 2022\\\\n        relation: background\\\\n        summary: \\\\\\\"统一跨模态代码预训练，在代码搜索等任务上取得 SOTA。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"StarCoder: May the Source Be with You!\\\\\\\"\\\\n        authors: \\\\\\\"Raymond Li, Loubna Ben Allal, et al. (BigCode)\\\\\\\"\\\\n        venue: TMLR\\\\n        year: 2023\\\\n        relation: building-block\\\\n        summary: \\\\\\\"大规模开源代码 LLM，StructFuse 用 StarCoder2-3B 作为对比学习检索器的 backbone 之一。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Code Llama: Open Foundation Models for Code\\\\\\\"\\\\n        authors: \\\\\\\"Baptiste Roziere, Jonas Gehring, Fabian Gloeckle, et al. (Meta AI)\\\\\\\"\\\\n        venue: arXiv\\\\n        year: 2023\\\\n        relation: background\\\\n        summary: \\\\\\\"Meta 的代码大模型系列，基于 Llama 2 微调。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Qwen2.5-Coder Technical Report\\\\\\\"\\\\n        authors: \\\\\\\"Binyuan Hui, Jian Yang, Zeyu Cui, et al. (Qwen Team, Alibaba)\\\\\\\"\\\\n        venue: arXiv\\\\n        year: 2024\\\\n        relation: building-block\\\\n        summary: \\\\\\\"Qwen 代码模型系列，StructFuse 用 Qwen2.5-Coder-3B 作为对比学习检索器的 backbone。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence\\\\\\\"\\\\n        authors: \\\\\\\"Daya Guo, Qihao Zhu, Dejian Yang, Zhenda Xie, Kai Dong, Wentao Zhang, Guanting Chen, Xiao Bi, Yu Wu, Y.K. Li, Fuli Luo, Yingfei Xiong, Wenfeng Liang\\\\\\\"\\\\n        venue: arXiv\\\\n        year: 2024\\\\n        relation: background\\\\n        summary: \\\\\\\"开源代码 LLM 系列 (1.3B-33B)，project-level 代码训练 + 16K context + fill-in-the-blank 预训练。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"RepoFusion: Training Code Models to Understand Your Repository\\\\\\\"\\\\n        authors: \\\\\\\"Disha Shrivastava, Denis Kocetkov, Harm de Vries, Dzmitry Bahdanau, Torsten Scholak\\\\\\\"\\\\n        venue: arXiv\\\\n        year: 2023\\\\n        relation: background\\\\n        summary: \\\\\\\"训练代码模型融合多个 cross-file repo context 进行代码补全，小模型 + repo context 可匹配大模型性能。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"BM25\\\\\\\"\\\\n        authors: \\\\\\\"Stephen Robertson, Hugo Zaragoza\\\\\\\"\\\\n        venue: \\\\\\\"Foundations and Trends in Information Retrieval\\\\\\\"\\\\n        year: 2009\\\\n        relation: baseline\\\\n        summary: \\\\\\\"经典稀疏检索方法，StructFuse 的 baseline 之一。\\\\\\\"\\\\n\\\\n  # ==========================================================================\\\\n  # Category 6: Graph-Guided Code Navigation (Inference-Time)\\\\n  # ==========================================================================\\\\n  graph_guided_inference:\\\\n    description: \\\\\\\"推理时利用代码结构图辅助导航/检索的方法（与 StructFuse 的训练时结构信号互补）\\\\\\\"\\\\n    papers:\\\\n\\\\n      - title: \\\\\\\"LocAgent: Graph-Guided LLM Agents for Code Localization\\\\\\\"\\\\n        authors: \\\\\\\"Zhaoling Chen, Robert Tang, Gangda Deng, Fang Wu, Jialong Wu, Zhiwei Jiang, Viktor Prasanna, Arman Cohan, Xingyao Wang\\\\\\\"\\\\n        venue: ACL\\\\n        year: 2025\\\\n        relation: contrast\\\\n        summary: \\\\\\\"将代码库解析为有向异构图，LLM agent 通过 multi-hop 推理在图上导航做代码定位。推理时用结构图，StructFuse 训练时用。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases\\\\\\\"\\\\n        authors: \\\\\\\"Xiangyan Liu, Bo Lan, Zhiyuan Hu, Yang Liu, Zhicheng Zhang, Fei Wang, Michael Qizhe Shieh, Wenmeng Zhou\\\\\\\"\\\\n        venue: NAACL\\\\n        year: 2025\\\\n        relation: contrast\\\\n        summary: \\\\\\\"将代码库索引到图数据库，LLM agent 通过 graph query 接口检索结构化上下文。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"RANGER: Repository-Level Agent for Graph-Enhanced Retrieval\\\\\\\"\\\\n        authors: \\\\\\\"Pratik Shah, Rajat Ghosh, Aryan Singhal, Debojyoti Dutta\\\\\\\"\\\\n        venue: arXiv\\\\n        year: 2025\\\\n        relation: contrast\\\\n        summary: \\\\\\\"构建 repo 知识图（含 variable-level 节点），dual-stage retrieval: Cypher lookup + MCTS-guided graph exploration。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph\\\\\\\"\\\\n        authors: \\\\\\\"Siru Ouyang, Wenhao Yu, Kaixin Ma, Zilin Xiao, Zhihan Zhang, Mengzhao Jia, Jiawei Han, Hongming Zhang, Dong Yu\\\\\\\"\\\\n        venue: ICLR\\\\n        year: 2025\\\\n        relation: contrast\\\\n        summary: \\\\\\\"以代码行为节点构建 repo-level 代码图，作为 SE agent 的 plug-in 导航模块。推理时逐行图导航，与 StructFuse 训练时批量提取结构信号互补。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph\\\\\\\"\\\\n        authors: \\\\\\\"Wei Liu, Ailun Yu, Daoguang Zan, Bo Shen, Wei Zhang, Haiyan Zhao, Zhi Jin, Qianxiang Wang\\\\\\\"\\\\n        venue: ASE\\\\n        year: 2024\\\\n        relation: contrast\\\\n        summary: \\\\\\\"构建 code context graph（含 control-flow 和 data-dependence edges）进行 coarse-to-fine 检索辅助代码补全。使用 intra-procedural data-flow，与 StructFuse 的 inter-procedural scope 形成对比。\\\\\\\"\\\\n\\\\n  # ==========================================================================\\\\n  # Category 7: Infrastructure / Tools\\\\n  # ==========================================================================\\\\n  infrastructure:\\\\n    description: \\\\\\\"StructFuse 依赖的核心基础设施和工具\\\\\\\"\\\\n    papers:\\\\n\\\\n      - title: \\\\\\\"Billion-Scale Similarity Search with GPUs\\\\\\\"\\\\n        authors: \\\\\\\"Jeff Johnson, Matthijs Douze, Herve Jegou\\\\\\\"\\\\n        venue: \\\\\\\"IEEE Transactions on Big Data\\\\\\\"\\\\n        year: 2021\\\\n        relation: building-block\\\\n        summary: \\\\\\\"FAISS: GPU 加速的大规模向量相似度搜索库，StructFuse 用于 ANN-based hard negative mining。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Tree-sitter: An Incremental Parsing System for Programming Tools\\\\\\\"\\\\n        authors: \\\\\\\"Max Brunsfeld et al.\\\\\\\"\\\\n        venue: \\\\\\\"Software (Zenodo DOI: 10.5281/zenodo.13375512)\\\\\\\"\\\\n        year: 2018\\\\n        relation: building-block\\\\n        summary: \\\\\\\"增量解析库，高效构建和更新 concrete syntax trees。与 CodeQL 互补用于代码结构提取。\\\\\\\"\\\\n        note: \\\\\\\"软件工具，无正式论文。引用 Zenodo DOI 或 GitHub repo。\\\\\\\"\\\\n\\\", \\\"total_chars\\\": 15999, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml\", \"content\": \"# StructFuse — Related Work Literature Map\\n# 最后更新: 2026-05-14\\n# 说明: 只收录已验证存在的论文。每篇均经 WebSearch 确认标题/venue/year。\\n# 总计: 39 entries (含 2 个软件工具引用)\\n\\ncategories:\\n\\n  # ==========================================================================\\n  # Category 1: Code Retrieval for Bug Fixing / SWE-bench Ecosystem\\n  # ==========================================================================\\n  code_retrieval_bug_fixing:\\n    description: \\\"SWE-bench 及相关 repo-level 自动修复系统中的代码检索方法\\\"\\n    papers:\\n\\n      - title: \\\"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?\\\"\\n        authors: \\\"Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan\\\"\\n        venue: ICLR\\n        year: 2024\\n        relation: baseline\\n        summary: \\\"从 GitHub issues 构建 repo-level bug fixing benchmark，成为自动修复领域标准评估集。\\\"\\n\\n      - title: \\\"SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering\\\"\\n        authors: \\\"John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press\\\"\\n        venue: NeurIPS\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"基于 LLM agent 的交互式 bug fixing 系统，定义了 ACI 接口范式。\\\"\\n\\n      - title: \\\"AutoCodeRover: Autonomous Program Improvement\\\"\\n        authors: \\\"Yuntong Zhang, Haifeng Ruan, Zhiyu Fan, Abhik Roychoudhury\\\"\\n        venue: ISSTA\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"结合代码搜索与 spectrum-based fault localization，利用程序分析缩小修复范围。\\\"\\n\\n      - title: \\\"Agentless: Demystifying LLM-based Software Engineering Agents\\\"\\n        authors: \\\"Chunqiu Steven Xia, Yinlin Deng, Soren Dunn, Lingming Zhang\\\"\\n        venue: arXiv\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"无 agent 架构的 two-phase localize-then-repair 方法，在 SWE-bench 上取得强 baseline。\\\"\\n\\n      - title: \\\"SWE-smith: Scaling Data for Software Engineering Agents\\\"\\n        authors: \\\"John Yang, Kilian Lieret, Carlos E. Jimenez, Alexander Wettig, Kabir Khandpur, Yanzhe Zhang, Binyuan Hui, Ofir Press, Ludwig Schmidt, Diyi Yang\\\"\\n        venue: \\\"NeurIPS (Datasets & Benchmarks, Spotlight)\\\"\\n        year: 2025\\n        relation: building-block\\n        summary: \\\"自动从 GitHub 生成大规模 SWE-bench 风格训练数据，StructFuse 用其 repos 做 data-flow 提取。\\\"\\n\\n      - title: \\\"RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems\\\"\\n        authors: \\\"Tianyang Liu, Canwen Xu, Julian McAuley\\\"\\n        venue: ICLR\\n        year: 2024\\n        relation: baseline\\n        summary: \\\"Repo-level 代码补全/检索 benchmark，含 RepoBench-R 检索子任务。\\\"\\n\\n      - title: \\\"SweRank: Software Issue Localization with Code Ranking\\\"\\n        authors: \\\"Revanth Gangi Reddy, Tarun Suresh, JaeHyeok Doo, Ye Liu, Xuan Phi Nguyen, Yingbo Zhou, Semih Yavuz, Caiming Xiong, Heng Ji, Shafiq Joty\\\"\\n        venue: arXiv\\n        year: 2025\\n        relation: competitor\\n        summary: \\\"Retrieve-and-rerank 框架用于 software issue localization，在 SWE-Bench-Lite 和 LocBench 上 SOTA，text-based retrieval baseline。\\\"\\n\\n      - title: \\\"SWE-Fixer: Training Open-Source LLMs for Effective and Efficient GitHub Issue Resolution\\\"\\n        authors: \\\"Chengxing Xie, Bowen Li, Chang Gao, He Du, Wai Lam, Difan Zou, Kai Chen\\\"\\n        venue: \\\"ACL (Findings)\\\"\\n        year: 2025\\n        relation: competitor\\n        summary: \\\"BM25 + LLM retriever 的 coarse-to-fine file retrieval pipeline，在 SWE-Bench Verified 上 30.2%。\\\"\\n\\n  # ==========================================================================\\n  # Category 2: Hard Negative Mining in Contrastive Learning\\n  # ==========================================================================\\n  hard_negative_mining:\\n    description: \\\"对比学习中 hard negative 挖掘策略，以及密集检索中的负样本选择\\\"\\n    papers:\\n\\n      - title: \\\"Dense Passage Retrieval for Open-Domain Question Answering\\\"\\n        authors: \\\"Vladimir Karpukhin, Barlas Oguz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, Wen-tau Yih\\\"\\n        venue: EMNLP\\n        year: 2020\\n        relation: background\\n        summary: \\\"DPR 开创了 in-batch negatives + BM25 hard negatives 的双塔检索范式。\\\"\\n\\n      - title: \\\"Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval\\\"\\n        authors: \\\"Lee Xiong, Chenyan Xiong, Ye Li, Kwok-Fung Tang, Jialin Liu, Paul Bennett, Junaid Ahmed, Arnold Overwijk\\\"\\n        venue: ICLR\\n        year: 2021\\n        relation: background\\n        summary: \\\"ANCE 用 ANN index 动态挖掘 embedding-distance hard negatives，StructFuse 的 baseline negative 策略之一。\\\"\\n\\n      - title: \\\"A Simple Framework for Contrastive Learning of Visual Representations\\\"\\n        authors: \\\"Ting Chen, Simon Kornblith, Mohammad Norouzi, Geoffrey Hinton\\\"\\n        venue: ICML\\n        year: 2020\\n        relation: background\\n        summary: \\\"SimCLR 视觉对比学习奠基工作，证明 hard negatives 和大 batch size 对对比学习的重要性。\\\"\\n\\n      - title: \\\"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\\\"\\n        authors: \\\"Nils Reimers, Iryna Gurevych\\\"\\n        venue: EMNLP\\n        year: 2019\\n        relation: background\\n        summary: \\\"Siamese/triplet 网络训练句子嵌入，StructFuse 的对比训练框架与其类似。\\\"\\n\\n      - title: \\\"Curriculum Learning for Dense Retrieval Distillation\\\"\\n        authors: \\\"Hansi Zeng, Hamed Zamani, Vishwa Vinay\\\"\\n        venue: \\\"SIGIR (Best Short Paper)\\\"\\n        year: 2022\\n        relation: background\\n        summary: \\\"CL-DRD: 课程学习式知识蒸馏用于密集检索，从粗粒度到细粒度逐步增加训练难度。\\\"\\n\\n      - title: \\\"Effective Hard Negative Mining for Contrastive Learning-Based Code Search\\\"\\n        authors: \\\"Fan Y., Li C., Ge J., Huang L., Luo B.\\\"\\n        venue: \\\"ACM TOSEM\\\"\\n        year: 2025\\n        relation: contrast-target\\n        summary: \\\"CoCoHaNeRe: 提出可微分 hard negative 机制用于代码搜索对比学习。其对 hard negative 机制的处理与 StructFuse 的发现形成关键对照——StructFuse 证明 true embedding-distance mining 即可持续提升性能。\\\"\\n        note: \\\"关键引用：StructFuse Claim 1 的 correction target。CoCoHaNeRe 论点是非可微 embedding negatives 学习'slow and ineffective'，StructFuse 证明用 true embedding distance mining 仍然有效。\\\"\\n\\n  # ==========================================================================\\n  # Category 3: Contrastive Learning for Code\\n  # ==========================================================================\\n  contrastive_code_learning:\\n    description: \\\"代码领域的对比学习方法，训练时利用代码特性构建正负样本\\\"\\n    papers:\\n\\n      - title: \\\"Contrastive Code Representation Learning\\\"\\n        authors: \\\"Paras Jain, Ajay Jain, Tianjun Zhang, Pieter Abbeel, Joseph Gonzalez, Ion Stoica\\\"\\n        venue: EMNLP\\n        year: 2021\\n        relation: background\\n        summary: \\\"ContraCode: 自监督对比预训练，通过编译器变换生成功能等价的程序变体，学习代码功能而非表面形式。\\\"\\n\\n      - title: \\\"CodeRetriever: A Large Scale Contrastive Pre-Training Method for Code Search\\\"\\n        authors: \\\"Xiaonan Li, Yeyun Gong, Yelong Shen, Xipeng Qiu, Hang Zhang, Bolun Yao, Weizhen Qi, Daxin Jiang, Weizhu Chen, Nan Duan\\\"\\n        venue: EMNLP\\n        year: 2022\\n        relation: background\\n        summary: \\\"结合 unimodal (code-code) 和 bimodal (code-text) 对比学习预训练代码表示，在 11 个代码搜索 benchmark 上 SOTA。\\\"\\n\\n      - title: \\\"Towards Learning (Dis)-Similarity of Source Code from Program Contrasts\\\"\\n        authors: \\\"Yangruibo Ding, Luca Buratti, Saurabh Pujar, Alessandro Morari, Baishakhi Ray, Saikat Chakraborty\\\"\\n        venue: \\\"ACL (Long Papers)\\\"\\n        year: 2022\\n        relation: background\\n        summary: \\\"利用程序结构和功能属性构建对比样本对，学习代码相似性/差异性表示。\\\"\\n\\n  # ==========================================================================\\n  # Category 4: Program Analysis for ML\\n  # ==========================================================================\\n  program_analysis_for_ml:\\n    description: \\\"静态分析辅助 ML，结构信息在代码表示学习中的应用\\\"\\n    papers:\\n\\n      - title: \\\"CodeQL: Semantic Code Analysis Engine\\\"\\n        authors: \\\"GitHub / Semmle\\\"\\n        venue: \\\"Tool (open-source)\\\"\\n        year: 2019\\n        relation: building-block\\n        summary: \\\"基于 Datalog 的代码查询引擎，支持 inter-procedural data-flow 分析。StructFuse 用它提取 scope-bounded data-flow graph。\\\"\\n\\n      - title: \\\"code2vec: Learning Distributed Representations of Code\\\"\\n        authors: \\\"Uri Alon, Meital Zilberstein, Omer Levy, Eran Yahav\\\"\\n        venue: POPL\\n        year: 2019\\n        relation: background\\n        summary: \\\"用 AST path 学习代码向量表示，首次大规模证明结构信息对代码表示学习的价值。\\\"\\n\\n      - title: \\\"code2seq: Generating Sequences from Structured Representations of Code\\\"\\n        authors: \\\"Uri Alon, Shaked Brody, Omer Levy, Eran Yahav\\\"\\n        venue: ICLR\\n        year: 2019\\n        relation: background\\n        summary: \\\"code2vec 的序列生成扩展，用 AST path attention 生成方法名摘要。\\\"\\n\\n      - title: \\\"Detecting Code Clones with Graph Neural Network and Flow-Augmented Abstract Syntax Tree\\\"\\n        authors: \\\"Wenhan Wang, Ge Li, Bo Ma, Xin Xia, Zhi Jin\\\"\\n        venue: SANER\\n        year: 2020\\n        relation: background\\n        summary: \\\"FA-AST: 用 data-flow 增强 AST 进行代码克隆检测，与 StructFuse 用 data-flow 做 hard negative 挖掘思路相关。\\\"\\n\\n      - title: \\\"GraphCodeBERT: Pre-training Code Representations with Data Flow\\\"\\n        authors: \\\"Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan, Alexey Svyatkovskiy, Shengyu Fu, Michele Tufano, Shao Kun Deng, Colin Clement, Dawn Drain, Neel Sundaresan, Jian Yin, Daxin Jiang, Ming Zhou\\\"\\n        venue: ICLR\\n        year: 2021\\n        relation: background\\n        summary: \\\"在预训练中引入 data-flow edge，证明 data-flow 信息提升代码理解任务。StructFuse 的 insight 与此相关但用途不同（hard negative mining vs pre-training）。\\\"\\n\\n      - title: \\\"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair\\\"\\n        authors: \\\"Shahd Seddik, Fatemeh Fard\\\"\\n        venue: arXiv\\n        year: 2026\\n        relation: contrast\\n        summary: \\\"用 multi-granularity program graph（含 intra-procedural def-use edges）辅助 LLM agent 做 fault localization。仅 intra-procedural + runtime tool calls，与 StructFuse 的 inter-procedural static mining 互补。\\\"\\n\\n  # ==========================================================================\\n  # Category 5: Code Embeddings / Code Search\\n  # ==========================================================================\\n  code_embeddings_search:\\n    description: \\\"代码嵌入模型和代码搜索方法\\\"\\n    papers:\\n\\n      - title: \\\"CodeSearchNet Challenge: Evaluating the State of Semantic Code Search\\\"\\n        authors: \\\"Hamel Husain, Ho-Hsiang Wu, Tiferet Gazit, Miltiadis Allamanis, Marc Brockschmidt\\\"\\n        venue: arXiv\\n        year: 2019\\n        relation: background\\n        summary: \\\"代码语义搜索 benchmark 和数据集，推动了代码嵌入模型的发展。\\\"\\n\\n      - title: \\\"CodeBERT: A Pre-Trained Model for Programming and Natural Languages\\\"\\n        authors: \\\"Zhangyin Feng, Daya Guo, Duyu Tang, Nan Duan, Xiaocheng Feng, Ming Gong, Lixin Zou, Bing Qin, Ting Liu, Daxin Jiang, Ming Zhou\\\"\\n        venue: \\\"EMNLP (Findings)\\\"\\n        year: 2020\\n        relation: background\\n        summary: \\\"首个编程语言-自然语言双模态预训练模型，代码嵌入的早期里程碑。\\\"\\n\\n      - title: \\\"UniXcoder: Unified Cross-Modal Pre-training for Code Representation\\\"\\n        authors: \\\"Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou, Jian Yin\\\"\\n        venue: ACL\\n        year: 2022\\n        relation: background\\n        summary: \\\"统一跨模态代码预训练，在代码搜索等任务上取得 SOTA。\\\"\\n\\n      - title: \\\"StarCoder: May the Source Be with You!\\\"\\n        authors: \\\"Raymond Li, Loubna Ben Allal, et al. (BigCode)\\\"\\n        venue: TMLR\\n        year: 2023\\n        relation: building-block\\n        summary: \\\"大规模开源代码 LLM，StructFuse 用 StarCoder2-3B 作为对比学习检索器的 backbone 之一。\\\"\\n\\n      - title: \\\"Code Llama: Open Foundation Models for Code\\\"\\n        authors: \\\"Baptiste Roziere, Jonas Gehring, Fabian Gloeckle, et al. (Meta AI)\\\"\\n        venue: arXiv\\n        year: 2023\\n        relation: background\\n        summary: \\\"Meta 的代码大模型系列，基于 Llama 2 微调。\\\"\\n\\n      - title: \\\"Qwen2.5-Coder Technical Report\\\"\\n        authors: \\\"Binyuan Hui, Jian Yang, Zeyu Cui, et al. (Qwen Team, Alibaba)\\\"\\n        venue: arXiv\\n        year: 2024\\n        relation: building-block\\n        summary: \\\"Qwen 代码模型系列，StructFuse 用 Qwen2.5-Coder-3B 作为对比学习检索器的 backbone。\\\"\\n\\n      - title: \\\"DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence\\\"\\n        authors: \\\"Daya Guo, Qihao Zhu, Dejian Yang, Zhenda Xie, Kai Dong, Wentao Zhang, Guanting Chen, Xiao Bi, Yu Wu, Y.K. Li, Fuli Luo, Yingfei Xiong, Wenfeng Liang\\\"\\n        venue: arXiv\\n        year: 2024\\n        relation: background\\n        summary: \\\"开源代码 LLM 系列 (1.3B-33B)，project-level 代码训练 + 16K context + fill-in-the-blank 预训练。\\\"\\n\\n      - title: \\\"RepoFusion: Training Code Models to Understand Your Repository\\\"\\n        authors: \\\"Disha Shrivastava, Denis Kocetkov, Harm de Vries, Dzmitry Bahdanau, Torsten Scholak\\\"\\n        venue: arXiv\\n        year: 2023\\n        relation: background\\n        summary: \\\"训练代码模型融合多个 cross-file repo context 进行代码补全，小模型 + repo context 可匹配大模型性能。\\\"\\n\\n      - title: \\\"BM25\\\"\\n        authors: \\\"Stephen Robertson, Hugo Zaragoza\\\"\\n        venue: \\\"Foundations and Trends in Information Retrieval\\\"\\n        year: 2009\\n        relation: baseline\\n        summary: \\\"经典稀疏检索方法，StructFuse 的 baseline 之一。\\\"\\n\\n  # ==========================================================================\\n  # Category 6: Graph-Guided Code Navigation (Inference-Time)\\n  # ==========================================================================\\n  graph_guided_inference:\\n    description: \\\"推理时利用代码结构图辅助导航/检索的方法（与 StructFuse 的训练时结构信号互补）\\\"\\n    papers:\\n\\n      - title: \\\"LocAgent: Graph-Guided LLM Agents for Code Localization\\\"\\n        authors: \\\"Zhaoling Chen, Robert Tang, Gangda Deng, Fang Wu, Jialong Wu, Zhiwei Jiang, Viktor Prasanna, Arman Cohan, Xingyao Wang\\\"\\n        venue: ACL\\n        year: 2025\\n        relation: contrast\\n        summary: \\\"将代码库解析为有向异构图，LLM agent 通过 multi-hop 推理在图上导航做代码定位。推理时用结构图，StructFuse 训练时用。\\\"\\n\\n      - title: \\\"CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases\\\"\\n        authors: \\\"Xiangyan Liu, Bo Lan, Zhiyuan Hu, Yang Liu, Zhicheng Zhang, Fei Wang, Michael Qizhe Shieh, Wenmeng Zhou\\\"\\n        venue: NAACL\\n        year: 2025\\n        relation: contrast\\n        summary: \\\"将代码库索引到图数据库，LLM agent 通过 graph query 接口检索结构化上下文。\\\"\\n\\n      - title: \\\"RANGER: Repository-Level Agent for Graph-Enhanced Retrieval\\\"\\n        authors: \\\"Pratik Shah, Rajat Ghosh, Aryan Singhal, Debojyoti Dutta\\\"\\n        venue: arXiv\\n        year: 2025\\n        relation: contrast\\n        summary: \\\"构建 repo 知识图（含 variable-level 节点），dual-stage retrieval: Cypher lookup + MCTS-guided graph exploration。\\\"\\n\\n      - title: \\\"RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph\\\"\\n        authors: \\\"Siru Ouyang, Wenhao Yu, Kaixin Ma, Zilin Xiao, Zhihan Zhang, Mengzhao Jia, Jiawei Han, Hongming Zhang, Dong Yu\\\"\\n        venue: ICLR\\n        year: 2025\\n        relation: contrast\\n        summary: \\\"以代码行为节点构建 repo-level 代码图，作为 SE agent 的 plug-in 导航模块。推理时逐行图导航，与 StructFuse 训练时批量提取结构信号互补。\\\"\\n\\n      - title: \\\"GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph\\\"\\n        authors: \\\"Wei Liu, Ailun Yu, Daoguang Zan, Bo Shen, Wei Zhang, Haiyan Zhao, Zhi Jin, Qianxiang Wang\\\"\\n        venue: ASE\\n        year: 2024\\n        relation: contrast\\n        summary: \\\"构建 code context graph（含 control-flow 和 data-dependence edges）进行 coarse-to-fine 检索辅助代码补全。使用 intra-procedural data-flow，与 StructFuse 的 inter-procedural scope 形成对比。\\\"\\n\\n  # ==========================================================================\\n  # Category 7: Infrastructure / Tools\\n  # ==========================================================================\\n  infrastructure:\\n    description: \\\"StructFuse 依赖的核心基础设施和工具\\\"\\n    papers:\\n\\n      - title: \\\"Billion-Scale Similarity Search with GPUs\\\"\\n        authors: \\\"Jeff Johnson, Matthijs Douze, Herve Jegou\\\"\\n        venue: \\\"IEEE Transactions on Big Data\\\"\\n        year: 2021\\n        relation: building-block\\n        summary: \\\"FAISS: GPU 加速的大规模向量相似度搜索库，StructFuse 用于 ANN-based hard negative mining。\\\"\\n\\n      - title: \\\"Tree-sitter: An Incremental Parsing System for Programming Tools\\\"\\n        authors: \\\"Max Brunsfeld et al.\\\"\\n        venue: \\\"Software (Zenodo DOI: 10.5281/zenodo.13375512)\\\"\\n        year: 2018\\n        relation: building-block\\n        summary: \\\"增量解析库，高效构建和更新 concrete syntax trees。与 CodeQL 互补用于代码结构提取。\\\"\\n        note: \\\"软件工具，无正式论文。引用 Zenodo DOI 或 GitHub repo。\\\"\\n\", \"total_chars\": 15999, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Glob · `toolu_01FAwTudvUsxE4uPHyPJkCGS`</summary>

```json
{
  "pattern": "**/*related_work*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "4dba861c-18b9-42e4-9b70-35d756297374",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JB3Hb8XcuX1rcw8wJJHAH2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1997,
      "cache_read_input_tokens": 23548,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1997
      },
      "output_tokens": 41,
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

_source line 12 · 2026-05-15T05:10:59.364Z_

<details><summary>↩ Tool result · `toolu_01FAwTudvUsxE4uPHyPJkCGS`</summary>

```text
artifacts/_project/report/related_work_expansion_report.md
artifacts/literature/related_work_expansion_report.md
artifacts/_project/paper/related_work_v1_dc54a3.md
artifacts/_project/paper/related_work_v1.md
artifacts/paper_drafts/related_work_v1.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "0a888191-8c39-44e0-a06c-8f58fbacb119",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/report/related_work_expansion_report.md",
      "artifacts/literature/related_work_expansion_report.md",
      "artifacts/_project/paper/related_work_v1_dc54a3.md",
      "artifacts/_project/paper/related_work_v1.md",
      "artifacts/paper_drafts/related_work_v1.md"
    ],
    "durationMs": 17,
    "numFiles": 5,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Glob · `toolu_01D2i17qDG2E12WcpamhD4Kb`</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "f70b29d7-469d-4fc2-96ac-c7cdfe300d11",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JB3Hb8XcuX1rcw8wJJHAH2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1997,
      "cache_read_input_tokens": 23548,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1997
      },
      "output_tokens": 41,
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

_source line 14 · 2026-05-15T05:10:59.635Z_

<details><summary>↩ Tool result · `toolu_01D2i17qDG2E12WcpamhD4Kb`</summary>

```text
artifacts/paper_drafts/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "981e671c-95ef-4e0f-95b9-989a98a827bf",
  "tool_use_result": {
    "filenames": [
      "artifacts/paper_drafts/references.bib"
    ],
    "durationMs": 11,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 15_

<details><summary>Logged reasoning block</summary>

```text
Let me read the existing related work draft and references.bib to understand what's already there, then I'll search for each paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "6b7b52cf-d9bf-422d-a35e-041ea8beb990",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EJfePhVwNEghgR1YqNJ95L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7344,
      "cache_read_input_tokens": 25545,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7344
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

_source line 16_

读取已有 related work 草稿和 bib 文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "f3693cda-ecf3-4412-ae1c-489c2fecc87f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EJfePhVwNEghgR1YqNJ95L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7344,
      "cache_read_input_tokens": 25545,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7344
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

_source line 17_

<details open><summary>🔧 Tool call — Read · `toolu_01X7kBGPKc7pvyXJMCAvSevS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "ff9d26c7-8aed-4503-af28-e9448e122467",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EJfePhVwNEghgR1YqNJ95L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7344,
      "cache_read_input_tokens": 25545,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7344
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

_source line 18 · 2026-05-15T05:11:05.494Z_

<details><summary>↩ Tool result · `toolu_01X7kBGPKc7pvyXJMCAvSevS`</summary>

```text
1	# 2. Related Work
2	
3	## 2.1 Code Retrieval Methods
4	
5	Repo-level code retrieval aims to identify relevant files or code spans from large codebases given a bug report or issue description. Classical sparse retrieval via BM25 \cite{robertson2009bm25} remains a competitive baseline in this setting. The dense retrieval paradigm, pioneered by DPR \cite{karpukhin2020dpr} for open-domain question answering, has been increasingly adopted for code. SweRank \cite{reddy2025swerank} trains a retrieve-and-rerank pipeline for software issue localization, achieving state-of-the-art results on SWE-Bench-Lite and LocBench through text-based retrieval. SWE-Fixer \cite{xie2025swefixer} combines BM25 with a learned retriever in a coarse-to-fine file retrieval pipeline, demonstrating that sparse and dense retrieval are complementary. Both systems, however, treat code files as flat text and do not exploit structural relationships between files during training.
6	
7	A parallel line of work leverages code structure graphs at inference time to guide code navigation. LocAgent \cite{chen2025locagent} parses codebases into directed heterogeneous graphs and employs LLM agents for multi-hop graph reasoning during fault localization. RANGER \cite{shah2025ranger} constructs repository knowledge graphs with variable-level nodes and applies MCTS-guided graph exploration for retrieval. CodexGraph \cite{liu2025codexgraph} indexes codebases into graph databases queried via Cypher, while RepoGraph \cite{ouyang2025repograph} provides line-level code graph navigation as a plug-in module for software engineering agents. GraphCoder \cite{liu2024graphcoder} incorporates control-flow and data-dependence edges into code context graphs for coarse-to-fine retrieval, and ARISE \cite{seddik2026arise} exposes statement-level def-use edges for agentic fault localization---though both are limited to intra-procedural scope. These methods demonstrate the value of structural information for code retrieval, yet they incur per-query computational costs and, for agent-based systems, require multiple LLM calls per retrieval step.
8	
9	Critically, these graph-guided methods apply structural information exclusively at inference time; the underlying retrieval encoder is trained without structural signal. The encoder's embedding space is therefore optimized solely on textual similarity, potentially conflating lexically similar but structurally unrelated code. Our work addresses this gap by incorporating inter-procedural data-flow information into the training process through structure-grounded hard negative mining.
10	
11	## 2.2 Pre-trained Code Representations and Contrastive Learning
12	
13	Pre-trained code models have evolved rapidly in both architecture and training objectives. CodeBERT \cite{feng2020codebert} introduced bimodal pre-training on natural language--programming language pairs using masked language modeling and replaced token detection, establishing that cross-modal pre-training improves downstream code search and documentation generation. GraphCodeBERT \cite{guo2021graphcodebert} extended this by incorporating data-flow edges into pre-training, showing that intra-procedural data-flow information improves code understanding tasks. UniXcoder \cite{guo2022unixcoder} unified encoder-only, decoder-only, and encoder-decoder modes in a single framework with cross-modal pre-training, achieving strong results across code understanding and generation benchmarks. code2vec \cite{alon2019code2vec} demonstrated that AST path-based representations capture meaningful program properties at scale, complementing token-level approaches. More recently, CodeSage \cite{zhang2024codesage} scaled bidirectional code encoders with a two-stage pipeline combining identifier deobfuscation and bimodal contrastive learning, achieving state-of-the-art code retrieval performance. However, GraphCodeBERT uses data-flow as an auxiliary pre-training signal over individual functions, whereas our work uses inter-procedural data-flow to construct hard negatives for contrastive fine-tuning---a fundamentally different application of structural information that operates at the repository level rather than the function level.
14	
15	Building on the success of Sentence-BERT \cite{reimers2019sentencebert} in learning dense representations via siamese contrastive objectives, contrastive learning has proven effective for learning code representations that capture functional semantics beyond surface-level patterns. ContraCode \cite{jain2021contracode} applies compiler-driven transformations to generate functionally equivalent program variants as positive pairs, training the encoder to be invariant to syntactic variation. CodeRetriever \cite{li2022coderetriever} combines unimodal (code-code) and bimodal (code-text) contrastive objectives, achieving strong results across code search benchmarks. SCodeR \cite{li2022scoder} introduces soft-labeled contrastive pre-training that uses a teacher model to assign continuous similarity scores rather than binary labels, capturing graded code similarity. \citet{ding2022programcontrasts} leverage program structure and functional attributes to construct contrastive pairs for learning code (dis)similarity representations. InferCode \cite{bui2021infercode} takes a complementary self-supervised approach, learning code representations by predicting AST subtrees without requiring labeled pairs.
16	
17	The recent shift toward decoder-only architectures has produced models such as StarCoder2 \cite{lozhkov2024starcoder2} and Qwen2.5-Coder \cite{hui2024qwen25coder}, which achieve strong performance across code generation and understanding tasks. These models are increasingly adopted as backbone encoders for contrastive fine-tuning in code retrieval, though their pretrained representation geometries differ substantially from encoder-only predecessors---a factor that, as we show, interacts with negative mining strategy effectiveness.
18	
19	Despite the progress in pre-trained code representations and contrastive learning, these methods share a common dependency on negative sampling strategy yet few systematically investigate which negatives yield the best representations for code retrieval. Most approaches rely on in-batch negatives \cite{karpukhin2020dpr} or random sampling, leaving the interaction between negative selection strategy and encoder representation geometry unexplored. Our work addresses this gap with a controlled comparison across negative mining strategies on modern decoder-only code encoders.
20	
21	## 2.3 Hard Negative Mining
22	
23	Hard negative mining---selecting negative examples that are challenging for the current model---is well established for improving contrastive learning. In visual representation learning, SimCLR \cite{chen2020simclr} demonstrates the importance of large batch sizes and hard negatives for learning discriminative features. In dense text retrieval, DPR \cite{karpukhin2020dpr} shows that BM25-retrieved passages serve as effective hard negatives beyond in-batch sampling. ANCE \cite{xiong2021ance} advances this by mining negatives from the model's own embedding space via approximate nearest neighbor search, achieving substantial gains over static BM25 negatives. STAR \cite{zhan2021star} addresses the training instability of dynamic mining by jointly training the retriever with periodically refreshed hard negatives and a random negative stabilization mechanism. RocketQA \cite{qu2021rocketqa} introduces a cross-encoder as a denoiser to filter false negatives from hard negative candidates, demonstrating that the quality of hard negatives matters as much as their difficulty. Curriculum-based approaches such as CL-DRD \cite{zeng2022cldrd} progressively increase negative difficulty during training through knowledge distillation.
24	
25	In the code domain, hard negative mining has received comparatively less systematic attention. CoCoHaNeRe \cite{fan2025cocohanere} proposes a differentiable hard negative mechanism for code search contrastive learning, arguing that gradient-based methods yield faster and more effective training than non-differentiable embedding-based negative selection. While CoCoHaNeRe demonstrates the advantages of its gradient-based approach within its experimental setting, it does not evaluate simple static embedding-distance mining in structural code retrieval settings.
26	
27	Our work provides a systematic comparison that challenges the assumption that expensive gradient-based or dynamic hard negative methods are necessary for effective code retrieval. We show that simple static embedding-distance mining consistently improves retrieval performance across two decoder-only encoders with distinct representation geometries, without requiring differentiable negative generation or periodic re-mining. Furthermore, we introduce structure-grounded negatives derived from inter-procedural data-flow analysis and observe that the relative effectiveness of mining strategies depends on the encoder's pretrained representation geometry---an interaction that existing work does not examine.
28	
29	## 2.4 Code Structure Analysis
30	
31	Our structure-grounded negative mining pipeline builds upon established foundations in program analysis. The program dependence graph \cite{ferrante1987pdg}, representing both control and data dependencies between program statements, provides the theoretical basis for inter-procedural data-flow analysis. Yamaguchi et al.\ \cite{yamaguchi2014cpg} introduced the code property graph, merging ASTs, control-flow graphs, and program dependence graphs into a unified queryable representation implemented in the Joern platform, primarily for vulnerability detection. Our pipeline leverages CodeQL \cite{avgustinov2016ql}, which models codebases as relational databases queryable via a declarative object-oriented language, enabling scalable inter-procedural taint tracking across repository-scale codebases. While these tools have been primarily applied to vulnerability detection and program optimization, we repurpose inter-procedural data-flow analysis for a novel application: constructing structure-grounded hard negatives for contrastive code retrieval training.
32	
33	Together, these four lines of work---code retrieval, contrastive code representation learning, hard negative mining, and code structure analysis---converge in our approach, which uses structural signals from program analysis to improve contrastive training for code retrieval, distinct from methods that apply structure at inference time or during pre-training.
34	
35	&lt;!-- Claim 2 wording fix: 2026-05-15 -->
36	&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->
37	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "86cd97cf-d0ae-475e-a61c-9fa2f662a3c1",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md",
      "content": "# 2. Related Work\n\n## 2.1 Code Retrieval Methods\n\nRepo-level code retrieval aims to identify relevant files or code spans from large codebases given a bug report or issue description. Classical sparse retrieval via BM25 \\cite{robertson2009bm25} remains a competitive baseline in this setting. The dense retrieval paradigm, pioneered by DPR \\cite{karpukhin2020dpr} for open-domain question answering, has been increasingly adopted for code. SweRank \\cite{reddy2025swerank} trains a retrieve-and-rerank pipeline for software issue localization, achieving state-of-the-art results on SWE-Bench-Lite and LocBench through text-based retrieval. SWE-Fixer \\cite{xie2025swefixer} combines BM25 with a learned retriever in a coarse-to-fine file retrieval pipeline, demonstrating that sparse and dense retrieval are complementary. Both systems, however, treat code files as flat text and do not exploit structural relationships between files during training.\n\nA parallel line of work leverages code structure graphs at inference time to guide code navigation. LocAgent \\cite{chen2025locagent} parses codebases into directed heterogeneous graphs and employs LLM agents for multi-hop graph reasoning during fault localization. RANGER \\cite{shah2025ranger} constructs repository knowledge graphs with variable-level nodes and applies MCTS-guided graph exploration for retrieval. CodexGraph \\cite{liu2025codexgraph} indexes codebases into graph databases queried via Cypher, while RepoGraph \\cite{ouyang2025repograph} provides line-level code graph navigation as a plug-in module for software engineering agents. GraphCoder \\cite{liu2024graphcoder} incorporates control-flow and data-dependence edges into code context graphs for coarse-to-fine retrieval, and ARISE \\cite{seddik2026arise} exposes statement-level def-use edges for agentic fault localization---though both are limited to intra-procedural scope. These methods demonstrate the value of structural information for code retrieval, yet they incur per-query computational costs and, for agent-based systems, require multiple LLM calls per retrieval step.\n\nCritically, these graph-guided methods apply structural information exclusively at inference time; the underlying retrieval encoder is trained without structural signal. The encoder's embedding space is therefore optimized solely on textual similarity, potentially conflating lexically similar but structurally unrelated code. Our work addresses this gap by incorporating inter-procedural data-flow information into the training process through structure-grounded hard negative mining.\n\n## 2.2 Pre-trained Code Representations and Contrastive Learning\n\nPre-trained code models have evolved rapidly in both architecture and training objectives. CodeBERT \\cite{feng2020codebert} introduced bimodal pre-training on natural language--programming language pairs using masked language modeling and replaced token detection, establishing that cross-modal pre-training improves downstream code search and documentation generation. GraphCodeBERT \\cite{guo2021graphcodebert} extended this by incorporating data-flow edges into pre-training, showing that intra-procedural data-flow information improves code understanding tasks. UniXcoder \\cite{guo2022unixcoder} unified encoder-only, decoder-only, and encoder-decoder modes in a single framework with cross-modal pre-training, achieving strong results across code understanding and generation benchmarks. code2vec \\cite{alon2019code2vec} demonstrated that AST path-based representations capture meaningful program properties at scale, complementing token-level approaches. More recently, CodeSage \\cite{zhang2024codesage} scaled bidirectional code encoders with a two-stage pipeline combining identifier deobfuscation and bimodal contrastive learning, achieving state-of-the-art code retrieval performance. However, GraphCodeBERT uses data-flow as an auxiliary pre-training signal over individual functions, whereas our work uses inter-procedural data-flow to construct hard negatives for contrastive fine-tuning---a fundamentally different application of structural information that operates at the repository level rather than the function level.\n\nBuilding on the success of Sentence-BERT \\cite{reimers2019sentencebert} in learning dense representations via siamese contrastive objectives, contrastive learning has proven effective for learning code representations that capture functional semantics beyond surface-level patterns. ContraCode \\cite{jain2021contracode} applies compiler-driven transformations to generate functionally equivalent program variants as positive pairs, training the encoder to be invariant to syntactic variation. CodeRetriever \\cite{li2022coderetriever} combines unimodal (code-code) and bimodal (code-text) contrastive objectives, achieving strong results across code search benchmarks. SCodeR \\cite{li2022scoder} introduces soft-labeled contrastive pre-training that uses a teacher model to assign continuous similarity scores rather than binary labels, capturing graded code similarity. \\citet{ding2022programcontrasts} leverage program structure and functional attributes to construct contrastive pairs for learning code (dis)similarity representations. InferCode \\cite{bui2021infercode} takes a complementary self-supervised approach, learning code representations by predicting AST subtrees without requiring labeled pairs.\n\nThe recent shift toward decoder-only architectures has produced models such as StarCoder2 \\cite{lozhkov2024starcoder2} and Qwen2.5-Coder \\cite{hui2024qwen25coder}, which achieve strong performance across code generation and understanding tasks. These models are increasingly adopted as backbone encoders for contrastive fine-tuning in code retrieval, though their pretrained representation geometries differ substantially from encoder-only predecessors---a factor that, as we show, interacts with negative mining strategy effectiveness.\n\nDespite the progress in pre-trained code representations and contrastive learning, these methods share a common dependency on negative sampling strategy yet few systematically investigate which negatives yield the best representations for code retrieval. Most approaches rely on in-batch negatives \\cite{karpukhin2020dpr} or random sampling, leaving the interaction between negative selection strategy and encoder representation geometry unexplored. Our work addresses this gap with a controlled comparison across negative mining strategies on modern decoder-only code encoders.\n\n## 2.3 Hard Negative Mining\n\nHard negative mining---selecting negative examples that are challenging for the current model---is well established for improving contrastive learning. In visual representation learning, SimCLR \\cite{chen2020simclr} demonstrates the importance of large batch sizes and hard negatives for learning discriminative features. In dense text retrieval, DPR \\cite{karpukhin2020dpr} shows that BM25-retrieved passages serve as effective hard negatives beyond in-batch sampling. ANCE \\cite{xiong2021ance} advances this by mining negatives from the model's own embedding space via approximate nearest neighbor search, achieving substantial gains over static BM25 negatives. STAR \\cite{zhan2021star} addresses the training instability of dynamic mining by jointly training the retriever with periodically refreshed hard negatives and a random negative stabilization mechanism. RocketQA \\cite{qu2021rocketqa} introduces a cross-encoder as a denoiser to filter false negatives from hard negative candidates, demonstrating that the quality of hard negatives matters as much as their difficulty. Curriculum-based approaches such as CL-DRD \\cite{zeng2022cldrd} progressively increase negative difficulty during training through knowledge distillation.\n\nIn the code domain, hard negative mining has received comparatively less systematic attention. CoCoHaNeRe \\cite{fan2025cocohanere} proposes a differentiable hard negative mechanism for code search contrastive learning, arguing that gradient-based methods yield faster and more effective training than non-differentiable embedding-based negative selection. While CoCoHaNeRe demonstrates the advantages of its gradient-based approach within its experimental setting, it does not evaluate simple static embedding-distance mining in structural code retrieval settings.\n\nOur work provides a systematic comparison that challenges the assumption that expensive gradient-based or dynamic hard negative methods are necessary for effective code retrieval. We show that simple static embedding-distance mining consistently improves retrieval performance across two decoder-only encoders with distinct representation geometries, without requiring differentiable negative generation or periodic re-mining. Furthermore, we introduce structure-grounded negatives derived from inter-procedural data-flow analysis and observe that the relative effectiveness of mining strategies depends on the encoder's pretrained representation geometry---an interaction that existing work does not examine.\n\n## 2.4 Code Structure Analysis\n\nOur structure-grounded negative mining pipeline builds upon established foundations in program analysis. The program dependence graph \\cite{ferrante1987pdg}, representing both control and data dependencies between program statements, provides the theoretical basis for inter-procedural data-flow analysis. Yamaguchi et al.\\ \\cite{yamaguchi2014cpg} introduced the code property graph, merging ASTs, control-flow graphs, and program dependence graphs into a unified queryable representation implemented in the Joern platform, primarily for vulnerability detection. Our pipeline leverages CodeQL \\cite{avgustinov2016ql}, which models codebases as relational databases queryable via a declarative object-oriented language, enabling scalable inter-procedural taint tracking across repository-scale codebases. While these tools have been primarily applied to vulnerability detection and program optimization, we repurpose inter-procedural data-flow analysis for a novel application: constructing structure-grounded hard negatives for contrastive code retrieval training.\n\nTogether, these four lines of work---code retrieval, contrastive code representation learning, hard negative mining, and code structure analysis---converge in our approach, which uses structural signals from program analysis to improve contrastive training for code retrieval, distinct from methods that apply structure at inference time or during pre-training.\n\n&lt;!-- Claim 2 wording fix: 2026-05-15 -->\n&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->\n",
      "numLines": 37,
      "startLine": 1,
      "totalLines": 37
    }
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Read · `toolu_01NwFCKcWtftW5p8vqJJgfXZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "963be2b9-b762-4d12-b29b-64e528d1a547",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EJfePhVwNEghgR1YqNJ95L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7344,
      "cache_read_input_tokens": 25545,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7344
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

_source line 20 · 2026-05-15T05:11:05.575Z_

<details><summary>↩ Tool result · `toolu_01NwFCKcWtftW5p8vqJJgfXZ`</summary>

```text
1	% =============================================================================
2	% Section 2.1: Code Retrieval Methods
3	% =============================================================================
4	
5	@article{robertson2009bm25,
6	  title={The Probabilistic Relevance Framework: {BM25} and Beyond},
7	  author={Robertson, Stephen and Zaragoza, Hugo},
8	  journal={Foundations and Trends in Information Retrieval},
9	  volume={3},
10	  number={4},
11	  pages={333--389},
12	  year={2009},
13	  publisher={Now Publishers}
14	}
15	
16	@inproceedings{karpukhin2020dpr,
17	  title={Dense Passage Retrieval for Open-Domain Question Answering},
18	  author={Karpukhin, Vladimir and O{\u{g}}uz, Barlas and Min, Sewon and Lewis, Patrick and Wu, Ledell and Edunov, Sergey and Chen, Danqi and Yih, Wen-tau},
19	  booktitle={Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
20	  pages={6769--6781},
21	  year={2020}
22	}
23	
24	@article{reddy2025swerank,
25	  title={{SweRank}: Software Issue Localization with Code Ranking},
26	  author={Gangi Reddy, Revanth and Suresh, Tarun and Doo, JaeHyeok and Liu, Ye and Nguyen, Xuan Phi and Zhou, Yingbo and Yavuz, Semih and Xiong, Caiming and Ji, Heng and Joty, Shafiq},
27	  journal={arXiv preprint arXiv:2505.07849},
28	  year={2025}
29	}
30	
31	@inproceedings{xie2025swefixer,
32	  title={{SWE-Fixer}: Training Open-Source {LLM}s for Effective and Efficient {GitHub} Issue Resolution},
33	  author={Xie, Chengxing and Li, Bowen and Gao, Chang and Du, He and Lam, Wai and Zou, Difan and Chen, Kai},
34	  booktitle={Findings of the Association for Computational Linguistics: ACL 2025},
35	  pages={1123--1139},
36	  year={2025}
37	}
38	
39	@inproceedings{chen2025locagent,
40	  title={{LocAgent}: Graph-Guided {LLM} Agents for Code Localization},
41	  author={Chen, Zhaoling and Tang, Robert and Deng, Gangda and Wu, Fang and Wu, Jialong and Jiang, Zhiwei and Prasanna, Viktor and Cohan, Arman and Wang, Xingyao},
42	  booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL)},
43	  pages={8697--8727},
44	  year={2025}
45	}
46	
47	@article{shah2025ranger,
48	  title={{RANGER}: Repository-Level Agent for Graph-Enhanced Retrieval},
49	  author={Shah, Pratik and Ghosh, Rajat and Singhal, Aryan and Dutta, Debojyoti},
50	  journal={arXiv preprint arXiv:2509.25257},
51	  year={2025}
52	}
53	
54	@inproceedings{liu2025codexgraph,
55	  title={{CodexGraph}: Bridging Large Language Models and Code Repositories via Code Graph Databases},
56	  author={Liu, Xiangyan and Lan, Bo and Hu, Zhiyuan and Liu, Yang and Zhang, Zhicheng and Wang, Fei and Shieh, Michael Qizhe and Zhou, Wenmeng},
57	  booktitle={Proceedings of the 2025 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},
58	  pages={142--160},
59	  year={2025}
60	}
61	
62	@inproceedings{ouyang2025repograph,
63	  title={{RepoGraph}: Enhancing {AI} Software Engineering with Repository-level Code Graph},
64	  author={Ouyang, Siru and Yu, Wenhao and Ma, Kaixin and Xiao, Zilin and Zhang, Zhihan and Jia, Mengzhao and Han, Jiawei and Zhang, Hongming and Yu, Dong},
65	  booktitle={Proceedings of the Thirteenth International Conference on Learning Representations (ICLR)},
66	  year={2025}
67	}
68	
69	@inproceedings{liu2024graphcoder,
70	  title={{GraphCoder}: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model},
71	  author={Liu, Wei and Hu, Ailun and Li, Yixuan and Li, Yichen and Liu, Haoyu and Yang, Leyi},
72	  booktitle={Proceedings of the 39th IEEE/ACM International Conference on Automated Software Engineering (ASE)},
73	  year={2024}
74	}
75	
76	@article{seddik2026arise,
77	  title={{ARISE}: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair},
78	  author={Seddik, Shahd and Fard, Fatemeh},
79	  journal={arXiv preprint arXiv:2605.03117},
80	  year={2026}
81	}
82	
83	% =============================================================================
84	% Section 2.2: Pre-trained Code Representations and Contrastive Learning
85	% =============================================================================
86	
87	@inproceedings{feng2020codebert,
88	  title={{CodeBERT}: A Pre-Trained Model for Programming and Natural Languages},
89	  author={Feng, Zhangyin and Guo, Daya and Tang, Duyu and Duan, Nan and Feng, Xiaocheng and Gong, Ming and Shou, Linjun and Qin, Bing and Liu, Ting and Jiang, Daxin and Zhou, Ming},
90	  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2020},
91	  pages={1536--1547},
92	  year={2020}
93	}
94	
95	@inproceedings{guo2021graphcodebert,
96	  title={{GraphCodeBERT}: Pre-training Code Representations with Data Flow},
97	  author={Guo, Daya and Ren, Shuo and Lu, Shuai and Feng, Zhangyin and Tang, Duyu and Liu, Shujie and Zhou, Long and Duan, Nan and Svyatkovskiy, Alexey and Fu, Shengyu and Tufano, Michele and Deng, Shuai Kim and Clement, Colin and Drain, Dawn and Sundaresan, Neel and Yin, Jian and Jiang, Daxin and Zhou, Ming},
98	  booktitle={Proceedings of the Ninth International Conference on Learning Representations (ICLR)},
99	  year={2021}
100	}
101	
102	@inproceedings{guo2022unixcoder,
103	  title={{UniXcoder}: Unified Cross-Modal Pre-training for Code Representation},
104	  author={Guo, Daya and Lu, Shuai and Duan, Nan and Wang, Yanlin and Zhou, Ming and Yin, Jian},
105	  booktitle={Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (ACL)},
106	  pages={7212--7225},
107	  year={2022}
108	}
109	
110	@inproceedings{alon2019code2vec,
111	  title={code2vec: Learning Distributed Representations of Code},
112	  author={Alon, Uri and Zilberstein, Meital and Levy, Omer and Yahav, Eran},
113	  booktitle={Proceedings of the ACM on Programming Languages (POPL)},
114	  volume={3},
115	  pages={1--29},
116	  year={2019}
117	}
118	
119	@inproceedings{zhang2024codesage,
120	  title={Code Representation Learning At Scale},
121	  author={Zhang, Dejiao and Ahmad, Wasi Uddin and Tan, Ming and Ding, Hantian and Nallapati, Ramesh and Roth, Dan and Ma, Xiaofei and Xiang, Bing},
122	  booktitle={Proceedings of the Twelfth International Conference on Learning Representations (ICLR)},
123	  year={2024}
124	}
125	
126	@inproceedings{reimers2019sentencebert,
127	  title={Sentence-{BERT}: Sentence Embeddings using Siamese {BERT}-Networks},
128	  author={Reimers, Nils and Gurevych, Iryna},
129	  booktitle={Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
130	  pages={3982--3992},
131	  year={2019}
132	}
133	
134	@inproceedings{jain2021contracode,
135	  title={Contrastive Code Representation Learning},
136	  author={Jain, Paras and Jain, Ajil and Zhang, Tianjun and Abbeel, Pieter and Gonzalez, Joseph and Stoica, Ion},
137	  booktitle={Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
138	  pages={5954--5971},
139	  year={2021}
140	}
141	
142	@inproceedings{li2022coderetriever,
143	  title={{CodeRetriever}: A Large Scale Contrastive Pre-Training Method for Code Search},
144	  author={Li, Xiaonan and Gong, Yeyun and Shen, Yelong and Qiu, Xipeng and Zhang, Hang and Yao, Bolun and Qi, Weizhen and Jiang, Daxin and Chen, Weizhu and Duan, Nan},
145	  booktitle={Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
146	  pages={2898--2910},
147	  year={2022}
148	}
149	
150	@inproceedings{li2022scoder,
151	  title={Soft-Labeled Contrastive Pre-training for Function-level Code Representation},
152	  author={Li, Xiaonan and Guo, Daya and Gong, Yeyun and Lin, Yun and Shen, Yelong and Qiu, Xipeng and Jiang, Daxin and Chen, Weizhu and Duan, Nan},
153	  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2022},
154	  year={2022}
155	}
156	
157	@inproceedings{ding2022programcontrasts,
158	  title={Towards Learning (Dis)-Similarity of Source Code from Program Contrasts},
159	  author={Ding, Yangruibo and Buratti, Luca and Pujar, Saurabh and Morari, Alessandro and Ray, Baishakhi and Parthasarathy, Saikat},
160	  booktitle={Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (ACL)},
161	  pages={6300--6312},
162	  year={2022}
163	}
164	
165	@inproceedings{bui2021infercode,
166	  title={{InferCode}: Self-Supervised Learning of Code Representations by Predicting Subtrees},
167	  author={Bui, Nghi D. Q. and Yu, Yijun and Jiang, Lingxiao},
168	  booktitle={Proceedings of the 43rd IEEE/ACM International Conference on Software Engineering (ICSE)},
169	  pages={1186--1197},
170	  year={2021}
171	}
172	
173	@article{lozhkov2024starcoder2,
174	  title={{StarCoder} 2 and {The Stack} v2: The Next Generation},
175	  author={Lozhkov, Anton and Li, Raymond and Ben Allal, Loubna and Cassano, Federico and Lamy-Poirier, Joel and Tazi, Nouamane and Tang, Ao and Pykhtar, Dmytro and Liu, Jiawei and Wei, Yuxiang and others},
176	  journal={arXiv preprint arXiv:2402.19173},
177	  year={2024}
178	}
179	
180	@article{hui2024qwen25coder,
181	  title={{Qwen2.5-Coder} Technical Report},
182	  author={Hui, Binyuan and Yang, Jian and Cui, Zeyu and Yang, Jiaxi and Liu, Dayiheng and Zhang, Lei and Liu, Tianyu and Zhang, Jiajun and Yu, Bowen and Lu, Keming and Dang, Kai and Fan, Yang and Zhang, Yichang and Yang, An and Men, Rui and Huang, Fei and Zheng, Bo and others},
183	  journal={arXiv preprint arXiv:2409.12186},
184	  year={2024}
185	}
186	
187	% =============================================================================
188	% Section 2.3: Hard Negative Mining
189	% =============================================================================
190	
191	@inproceedings{chen2020simclr,
192	  title={A Simple Framework for Contrastive Learning of Visual Representations},
193	  author={Chen, Ting and Kornblith, Simon and Norouzi, Mohammad and Hinton, Geoffrey},
194	  booktitle={Proceedings of the 37th International Conference on Machine Learning (ICML)},
195	  pages={1597--1607},
196	  year={2020}
197	}
198	
199	@inproceedings{xiong2021ance,
200	  title={Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval},
201	  author={Xiong, Lee and Xiong, Chenyan and Li, Ye and Tang, Kwok-Fung and Liu, Jialin and Bennett, Paul and Ahmed, Junaid and Overwijk, Arnold},
202	  booktitle={Proceedings of the Ninth International Conference on Learning Representations (ICLR)},
203	  year={2021}
204	}
205	
206	@inproceedings{zhan2021star,
207	  title={Optimizing Dense Retrieval Model Training with Hard Negatives},
208	  author={Zhan, Jingtao and Mao, Jiaxin and Liu, Yiqun and Guo, Jiafeng and Zhang, Min and Ma, Shaoping},
209	  booktitle={Proceedings of the 44th International ACM SIGIR Conference on Research and Development in Information Retrieval},
210	  pages={1503--1512},
211	  year={2021}
212	}
213	
214	@inproceedings{qu2021rocketqa,
215	  title={{RocketQA}: An Optimized Training Approach to Dense Passage Retrieval for Open-Domain Question Answering},
216	  author={Qu, Yingqi and Ding, Yuchen and Liu, Jing and Liu, Kai and Ren, Ruiyang and Zhao, Wayne Xin and Dong, Daxiang and Wu, Hua and Wang, Haifeng},
217	  booktitle={Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL-HLT)},
218	  pages={5835--5847},
219	  year={2021}
220	}
221	
222	@inproceedings{zeng2022cldrd,
223	  title={Curriculum Learning for Dense Retrieval Distillation},
224	  author={Zeng, Hansi and Zamani, Hamed and Vinay, Vishwa},
225	  booktitle={Proceedings of the 45th International ACM SIGIR Conference on Research and Development in Information Retrieval},
226	  pages={1979--1983},
227	  year={2022}
228	}
229	
230	@article{fan2025cocohanere,
231	  title={Effective Hard Negative Mining for Contrastive Learning-Based Code Search},
232	  author={Fan, Ye and Li, Chuanyi and Ge, Jidong and Huang, LiGuo and Luo, Bin},
233	  journal={ACM Transactions on Software Engineering and Methodology},
234	  volume={34},
235	  number={3},
236	  year={2025},
237	  publisher={ACM}
238	}
239	
240	% =============================================================================
241	% Section 2.4: Code Structure Analysis
242	% =============================================================================
243	
244	@article{ferrante1987pdg,
245	  title={The Program Dependence Graph and Its Use in Optimization},
246	  author={Ferrante, Jeanne and Ottenstein, Karl J. and Warren, Joe D.},
247	  journal={ACM Transactions on Programming Languages and Systems},
248	  volume={9},
249	  number={3},
250	  pages={319--349},
251	  year={1987},
252	  publisher={ACM}
253	}
254	
255	@inproceedings{yamaguchi2014cpg,
256	  title={Modeling and Discovering Vulnerabilities with Code Property Graphs},
257	  author={Yamaguchi, Fabian and Golde, Nico and Arp, Daniel and Rieck, Konrad},
258	  booktitle={Proceedings of the 2014 IEEE Symposium on Security and Privacy (S\&P)},
259	  pages={590--604},
260	  year={2014},
261	  publisher={IEEE}
262	}
263	
264	@inproceedings{avgustinov2016ql,
265	  title={{QL}: Object-oriented Queries on Relational Data},
266	  author={Avgustinov, Pavel and de Moor, Oege and Jones, Michael Peyton and Sch{\"a}fer, Max},
267	  booktitle={30th European Conference on Object-Oriented Programming (ECOOP)},
268	  series={LIPIcs},
269	  volume={56},
270	  pages={2:1--2:25},
271	  year={2016}
272	}
273	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "451e85b7-f201-4d30-aae1-e905b643ec24",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/references.bib",
      "content": "% =============================================================================\n% Section 2.1: Code Retrieval Methods\n% =============================================================================\n\n@article{robertson2009bm25,\n  title={The Probabilistic Relevance Framework: {BM25} and Beyond},\n  author={Robertson, Stephen and Zaragoza, Hugo},\n  journal={Foundations and Trends in Information Retrieval},\n  volume={3},\n  number={4},\n  pages={333--389},\n  year={2009},\n  publisher={Now Publishers}\n}\n\n@inproceedings{karpukhin2020dpr,\n  title={Dense Passage Retrieval for Open-Domain Question Answering},\n  author={Karpukhin, Vladimir and O{\\u{g}}uz, Barlas and Min, Sewon and Lewis, Patrick and Wu, Ledell and Edunov, Sergey and Chen, Danqi and Yih, Wen-tau},\n  booktitle={Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages={6769--6781},\n  year={2020}\n}\n\n@article{reddy2025swerank,\n  title={{SweRank}: Software Issue Localization with Code Ranking},\n  author={Gangi Reddy, Revanth and Suresh, Tarun and Doo, JaeHyeok and Liu, Ye and Nguyen, Xuan Phi and Zhou, Yingbo and Yavuz, Semih and Xiong, Caiming and Ji, Heng and Joty, Shafiq},\n  journal={arXiv preprint arXiv:2505.07849},\n  year={2025}\n}\n\n@inproceedings{xie2025swefixer,\n  title={{SWE-Fixer}: Training Open-Source {LLM}s for Effective and Efficient {GitHub} Issue Resolution},\n  author={Xie, Chengxing and Li, Bowen and Gao, Chang and Du, He and Lam, Wai and Zou, Difan and Chen, Kai},\n  booktitle={Findings of the Association for Computational Linguistics: ACL 2025},\n  pages={1123--1139},\n  year={2025}\n}\n\n@inproceedings{chen2025locagent,\n  title={{LocAgent}: Graph-Guided {LLM} Agents for Code Localization},\n  author={Chen, Zhaoling and Tang, Robert and Deng, Gangda and Wu, Fang and Wu, Jialong and Jiang, Zhiwei and Prasanna, Viktor and Cohan, Arman and Wang, Xingyao},\n  booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL)},\n  pages={8697--8727},\n  year={2025}\n}\n\n@article{shah2025ranger,\n  title={{RANGER}: Repository-Level Agent for Graph-Enhanced Retrieval},\n  author={Shah, Pratik and Ghosh, Rajat and Singhal, Aryan and Dutta, Debojyoti},\n  journal={arXiv preprint arXiv:2509.25257},\n  year={2025}\n}\n\n@inproceedings{liu2025codexgraph,\n  title={{CodexGraph}: Bridging Large Language Models and Code Repositories via Code Graph Databases},\n  author={Liu, Xiangyan and Lan, Bo and Hu, Zhiyuan and Liu, Yang and Zhang, Zhicheng and Wang, Fei and Shieh, Michael Qizhe and Zhou, Wenmeng},\n  booktitle={Proceedings of the 2025 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  pages={142--160},\n  year={2025}\n}\n\n@inproceedings{ouyang2025repograph,\n  title={{RepoGraph}: Enhancing {AI} Software Engineering with Repository-level Code Graph},\n  author={Ouyang, Siru and Yu, Wenhao and Ma, Kaixin and Xiao, Zilin and Zhang, Zhihan and Jia, Mengzhao and Han, Jiawei and Zhang, Hongming and Yu, Dong},\n  booktitle={Proceedings of the Thirteenth International Conference on Learning Representations (ICLR)},\n  year={2025}\n}\n\n@inproceedings{liu2024graphcoder,\n  title={{GraphCoder}: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model},\n  author={Liu, Wei and Hu, Ailun and Li, Yixuan and Li, Yichen and Liu, Haoyu and Yang, Leyi},\n  booktitle={Proceedings of the 39th IEEE/ACM International Conference on Automated Software Engineering (ASE)},\n  year={2024}\n}\n\n@article{seddik2026arise,\n  title={{ARISE}: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair},\n  author={Seddik, Shahd and Fard, Fatemeh},\n  journal={arXiv preprint arXiv:2605.03117},\n  year={2026}\n}\n\n% =============================================================================\n% Section 2.2: Pre-trained Code Representations and Contrastive Learning\n% =============================================================================\n\n@inproceedings{feng2020codebert,\n  title={{CodeBERT}: A Pre-Trained Model for Programming and Natural Languages},\n  author={Feng, Zhangyin and Guo, Daya and Tang, Duyu and Duan, Nan and Feng, Xiaocheng and Gong, Ming and Shou, Linjun and Qin, Bing and Liu, Ting and Jiang, Daxin and Zhou, Ming},\n  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2020},\n  pages={1536--1547},\n  year={2020}\n}\n\n@inproceedings{guo2021graphcodebert,\n  title={{GraphCodeBERT}: Pre-training Code Representations with Data Flow},\n  author={Guo, Daya and Ren, Shuo and Lu, Shuai and Feng, Zhangyin and Tang, Duyu and Liu, Shujie and Zhou, Long and Duan, Nan and Svyatkovskiy, Alexey and Fu, Shengyu and Tufano, Michele and Deng, Shuai Kim and Clement, Colin and Drain, Dawn and Sundaresan, Neel and Yin, Jian and Jiang, Daxin and Zhou, Ming},\n  booktitle={Proceedings of the Ninth International Conference on Learning Representations (ICLR)},\n  year={2021}\n}\n\n@inproceedings{guo2022unixcoder,\n  title={{UniXcoder}: Unified Cross-Modal Pre-training for Code Representation},\n  author={Guo, Daya and Lu, Shuai and Duan, Nan and Wang, Yanlin and Zhou, Ming and Yin, Jian},\n  booktitle={Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  pages={7212--7225},\n  year={2022}\n}\n\n@inproceedings{alon2019code2vec,\n  title={code2vec: Learning Distributed Representations of Code},\n  author={Alon, Uri and Zilberstein, Meital and Levy, Omer and Yahav, Eran},\n  booktitle={Proceedings of the ACM on Programming Languages (POPL)},\n  volume={3},\n  pages={1--29},\n  year={2019}\n}\n\n@inproceedings{zhang2024codesage,\n  title={Code Representation Learning At Scale},\n  author={Zhang, Dejiao and Ahmad, Wasi Uddin and Tan, Ming and Ding, Hantian and Nallapati, Ramesh and Roth, Dan and Ma, Xiaofei and Xiang, Bing},\n  booktitle={Proceedings of the Twelfth International Conference on Learning Representations (ICLR)},\n  year={2024}\n}\n\n@inproceedings{reimers2019sentencebert,\n  title={Sentence-{BERT}: Sentence Embeddings using Siamese {BERT}-Networks},\n  author={Reimers, Nils and Gurevych, Iryna},\n  booktitle={Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages={3982--3992},\n  year={2019}\n}\n\n@inproceedings{jain2021contracode,\n  title={Contrastive Code Representation Learning},\n  author={Jain, Paras and Jain, Ajil and Zhang, Tianjun and Abbeel, Pieter and Gonzalez, Joseph and Stoica, Ion},\n  booktitle={Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages={5954--5971},\n  year={2021}\n}\n\n@inproceedings{li2022coderetriever,\n  title={{CodeRetriever}: A Large Scale Contrastive Pre-Training Method for Code Search},\n  author={Li, Xiaonan and Gong, Yeyun and Shen, Yelong and Qiu, Xipeng and Zhang, Hang and Yao, Bolun and Qi, Weizhen and Jiang, Daxin and Chen, Weizhu and Duan, Nan},\n  booktitle={Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages={2898--2910},\n  year={2022}\n}\n\n@inproceedings{li2022scoder,\n  title={Soft-Labeled Contrastive Pre-training for Function-level Code Representation},\n  author={Li, Xiaonan and Guo, Daya and Gong, Yeyun and Lin, Yun and Shen, Yelong and Qiu, Xipeng and Jiang, Daxin and Chen, Weizhu and Duan, Nan},\n  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2022},\n  year={2022}\n}\n\n@inproceedings{ding2022programcontrasts,\n  title={Towards Learning (Dis)-Similarity of Source Code from Program Contrasts},\n  author={Ding, Yangruibo and Buratti, Luca and Pujar, Saurabh and Morari, Alessandro and Ray, Baishakhi and Parthasarathy, Saikat},\n  booktitle={Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  pages={6300--6312},\n  year={2022}\n}\n\n@inproceedings{bui2021infercode,\n  title={{InferCode}: Self-Supervised Learning of Code Representations by Predicting Subtrees},\n  author={Bui, Nghi D. Q. and Yu, Yijun and Jiang, Lingxiao},\n  booktitle={Proceedings of the 43rd IEEE/ACM International Conference on Software Engineering (ICSE)},\n  pages={1186--1197},\n  year={2021}\n}\n\n@article{lozhkov2024starcoder2,\n  title={{StarCoder} 2 and {The Stack} v2: The Next Generation},\n  author={Lozhkov, Anton and Li, Raymond and Ben Allal, Loubna and Cassano, Federico and Lamy-Poirier, Joel and Tazi, Nouamane and Tang, Ao and Pykhtar, Dmytro and Liu, Jiawei and Wei, Yuxiang and others},\n  journal={arXiv preprint arXiv:2402.19173},\n  year={2024}\n}\n\n@article{hui2024qwen25coder,\n  title={{Qwen2.5-Coder} Technical Report},\n  author={Hui, Binyuan and Yang, Jian and Cui, Zeyu and Yang, Jiaxi and Liu, Dayiheng and Zhang, Lei and Liu, Tianyu and Zhang, Jiajun and Yu, Bowen and Lu, Keming and Dang, Kai and Fan, Yang and Zhang, Yichang and Yang, An and Men, Rui and Huang, Fei and Zheng, Bo and others},\n  journal={arXiv preprint arXiv:2409.12186},\n  year={2024}\n}\n\n% =============================================================================\n% Section 2.3: Hard Negative Mining\n% =============================================================================\n\n@inproceedings{chen2020simclr,\n  title={A Simple Framework for Contrastive Learning of Visual Representations},\n  author={Chen, Ting and Kornblith, Simon and Norouzi, Mohammad and Hinton, Geoffrey},\n  booktitle={Proceedings of the 37th International Conference on Machine Learning (ICML)},\n  pages={1597--1607},\n  year={2020}\n}\n\n@inproceedings{xiong2021ance,\n  title={Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval},\n  author={Xiong, Lee and Xiong, Chenyan and Li, Ye and Tang, Kwok-Fung and Liu, Jialin and Bennett, Paul and Ahmed, Junaid and Overwijk, Arnold},\n  booktitle={Proceedings of the Ninth International Conference on Learning Representations (ICLR)},\n  year={2021}\n}\n\n@inproceedings{zhan2021star,\n  title={Optimizing Dense Retrieval Model Training with Hard Negatives},\n  author={Zhan, Jingtao and Mao, Jiaxin and Liu, Yiqun and Guo, Jiafeng and Zhang, Min and Ma, Shaoping},\n  booktitle={Proceedings of the 44th International ACM SIGIR Conference on Research and Development in Information Retrieval},\n  pages={1503--1512},\n  year={2021}\n}\n\n@inproceedings{qu2021rocketqa,\n  title={{RocketQA}: An Optimized Training Approach to Dense Passage Retrieval for Open-Domain Question Answering},\n  author={Qu, Yingqi and Ding, Yuchen and Liu, Jing and Liu, Kai and Ren, Ruiyang and Zhao, Wayne Xin and Dong, Daxiang and Wu, Hua and Wang, Haifeng},\n  booktitle={Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL-HLT)},\n  pages={5835--5847},\n  year={2021}\n}\n\n@inproceedings{zeng2022cldrd,\n  title={Curriculum Learning for Dense Retrieval Distillation},\n  author={Zeng, Hansi and Zamani, Hamed and Vinay, Vishwa},\n  booktitle={Proceedings of the 45th International ACM SIGIR Conference on Research and Development in Information Retrieval},\n  pages={1979--1983},\n  year={2022}\n}\n\n@article{fan2025cocohanere,\n  title={Effective Hard Negative Mining for Contrastive Learning-Based Code Search},\n  author={Fan, Ye and Li, Chuanyi and Ge, Jidong and Huang, LiGuo and Luo, Bin},\n  journal={ACM Transactions on Software Engineering and Methodology},\n  volume={34},\n  number={3},\n  year={2025},\n  publisher={ACM}\n}\n\n% =============================================================================\n% Section 2.4: Code Structure Analysis\n% =============================================================================\n\n@article{ferrante1987pdg,\n  title={The Program Dependence Graph and Its Use in Optimization},\n  author={Ferrante, Jeanne and Ottenstein, Karl J. and Warren, Joe D.},\n  journal={ACM Transactions on Programming Languages and Systems},\n  volume={9},\n  number={3},\n  pages={319--349},\n  year={1987},\n  publisher={ACM}\n}\n\n@inproceedings{yamaguchi2014cpg,\n  title={Modeling and Discovering Vulnerabilities with Code Property Graphs},\n  author={Yamaguchi, Fabian and Golde, Nico and Arp, Daniel and Rieck, Konrad},\n  booktitle={Proceedings of the 2014 IEEE Symposium on Security and Privacy (S\\&P)},\n  pages={590--604},\n  year={2014},\n  publisher={IEEE}\n}\n\n@inproceedings{avgustinov2016ql,\n  title={{QL}: Object-oriented Queries on Relational Data},\n  author={Avgustinov, Pavel and de Moor, Oege and Jones, Michael Peyton and Sch{\\\"a}fer, Max},\n  booktitle={30th European Conference on Object-Oriented Programming (ECOOP)},\n  series={LIPIcs},\n  volume={56},\n  pages={2:1--2:25},\n  year={2016}\n}\n",
      "numLines": 273,
      "startLine": 1,
      "totalLines": 273
    }
  }
}
```

</details>

---

### Assistant

_source line 21_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear picture. The existing related work already mentions RocketQA and STAR (in section 2.3). Let me check which papers from the recommended list are already cited:

Already in related work:
- RocketQA ✓ (already cited in 2.3)
- DPR ✓
- ANCE ✓
- STAR ✓
- SimCLR ✓
- CL-DRD ✓
- CodeBERT ✓
- UniXcoder ✓


- ContraCode ✓
- CodeRetriever ✓
- GraphCodeBERT ✓

So I still need to add ContraBERT, ProGraML, CrossCodeEval, SynCoBERT, CAPSTONE, and CoSQA to the related work section. I'm verifying each of these papers through a web search to confirm they exist and are relevant to the research.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "739d3504-2a1d-47e5-93f9-1823dab5c869",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013T4aBApzVBUmGVHnsqMUMh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7630,
      "cache_read_input_tokens": 32889,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7630
      },
      "output_tokens": 9,
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

_source line 22_

已有 related work 已覆盖 RocketQA、ANCE、STAR 等。需新增验证的论文：ContraBERT、ProGraML、CrossCodeEval、SynCoBERT、CAPSTONE、CoSQA。开始 WebSearch 验证。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "c0e005bc-efea-45f8-a33a-518a464414ba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013T4aBApzVBUmGVHnsqMUMh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7630,
      "cache_read_input_tokens": 32889,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7630
      },
      "output_tokens": 9,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LUMViPRrgaQYomVbGAAJR6`</summary>

```json
{
  "query": "ContraBERT ICSE 2023 contrastive pre-training code understanding adversarial"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "fa97c9cf-889c-4722-a0af-f4cb5f7ee452",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013T4aBApzVBUmGVHnsqMUMh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7630,
      "cache_read_input_tokens": 32889,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7630
      },
      "output_tokens": 9,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SjmXyqESgXwu8KnCxEkkdn`</summary>

```json
{
  "query": "ProGraML ICML 2021 program graph machine learning Chris Cummins"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "9d9b3198-d818-4ace-bfa1-5c9f37435ebc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013T4aBApzVBUmGVHnsqMUMh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7630,
      "cache_read_input_tokens": 32889,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7630
      },
      "output_tokens": 9,
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

_source line 25_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NygSVfnrrcWgVkEgyZtGzB`</summary>

```json
{
  "query": "CrossCodeEval NeurIPS 2023 cross-file context code completion benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "f474be99-498a-4116-801d-c386af44d621",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013T4aBApzVBUmGVHnsqMUMh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7630,
      "cache_read_input_tokens": 32889,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7630
      },
      "output_tokens": 9,
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

_source line 26_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01X9PdsBpXRTLs3MWpNXBQUt`</summary>

```json
{
  "query": "SynCoBERT 2021 syntax contrastive pre-training code representation arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "0929c33b-46bc-4e75-9c7e-4c9285787d7c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013T4aBApzVBUmGVHnsqMUMh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7630,
      "cache_read_input_tokens": 32889,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7630
      },
      "output_tokens": 9,
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

_source line 27_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NGMnio7CEnA2sitXArPrXX`</summary>

```json
{
  "query": "CAPSTONE EMNLP 2023 code representation learning AST probing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "52b33223-81dc-41c5-bb69-c951478c6e6d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013T4aBApzVBUmGVHnsqMUMh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7630,
      "cache_read_input_tokens": 32889,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7630
      },
      "output_tokens": 9,
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

_source line 28_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QxAn5rxDDvmFinwAwFZqVd`</summary>

```json
{
  "query": "CoSQA ACL 2021 code search question answering web query dataset"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "18feff80-7d68-454e-8ebc-d603b962f63b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013T4aBApzVBUmGVHnsqMUMh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7630,
      "cache_read_input_tokens": 32889,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7630
      },
      "output_tokens": 9,
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

_source line 29 · 2026-05-15T05:11:24.802Z_

<details><summary>↩ Tool result · `toolu_01LUMViPRrgaQYomVbGAAJR6`</summary>

```text
Web search results for query: "ContraBERT ICSE 2023 contrastive pre-training code understanding adversarial"

Links: [{"title":"ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning - Singapore Management University","url":"https://smusg.elsevierpure.com/en/publications/contrabert-enhancing-code-pre-trained-models-via-contrastive-lear"},{"title":"ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning","url":"https://arxiv.org/pdf/2301.09072"},{"title":"[PDF] ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/ContraBERT:-Enhancing-Code-Pre-trained-Models-via-Liu-Wu/f6572fccea70e5023cc38cb33ebd0f520d7b22e2"},{"title":"[2301.09072] ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning","url":"https://arxiv.org/abs/2301.09072"},{"title":"ContraBERT: Enhancing Code Pre-Trained Models via Contrastive Learning | Proceedings of the 45th International Conference on Software Engineering","url":"https://dl.acm.org/doi/abs/10.1109/ICSE48619.2023.00207"},{"title":"ContraBERT: Enhancing Code Pre-trained Models via ...","url":"https://www.computer.org/csdl/proceedings-article/icse/2023/570100c476/1OM4OrPPiNy"},{"title":"ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning | Request PDF","url":"https://www.researchgate.net/publication/372385658_ContraBERT_Enhancing_Code_Pre-trained_Models_via_Contrastive_Learning"},{"title":"About me - Shangqing Liu’s Homepage","url":"https://shangqing-liu.github.io/"},{"title":"(PDF) ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning","url":"https://www.researchgate.net/publication/367359448_ContraBERT_Enhancing_Code_Pre-trained_Models_via_Contrastive_Learning"},{"title":"GitHub - saltudelft/ml4se: A curated list of papers, theses, datasets, and tools related to the application of Machine Learning for Software Engineering · GitHub","url":"https://github.com/saltudelft/ml4se"}]

Based on the web search results, here's what I found about ContraBERT:

## Overview

ContraBERT is an approach that aims to improve the robustness of pre-trained models via contrastive learning. The paper was published at the 45th IEEE/ACM International Conference on Software Engineering (ICSE 2023) by authors Shangqing Liu, Bozhi Wu, Xiaofei Xie, Guozhu Meng, and Yang Liu.

## Problem Being Addressed

State-of-the-art pre-trained models such as CodeBERT and GraphCodeBERT are susceptible to adversarial attacks, with performance dropping significantly with simple perturbations such as renaming variable names.

## Approach

The method designs nine kinds of simple and complex data augmentation operators on the programming language (PL) and natural language (NL) data to construct different variants. The existing pre-trained models are further trained by masked language modeling (MLM) and contrastive pre-training tasks on the original samples with their augmented variants to enhance robustness.

## Results

The experiments demonstrate that ContraBERT can effectively improve the robustness of existing pre-trained models, with robustness-enhanced models providing improvements over four popular downstream tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "0a1e3b10-db9e-4c5e-8a85-3fd400b8772e",
  "tool_use_result": {
    "query": "ContraBERT ICSE 2023 contrastive pre-training code understanding adversarial",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VLkaE4c8uYKqCdoZ7sUvWC",
        "content": [
          {
            "title": "ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning - Singapore Management University",
            "url": "https://smusg.elsevierpure.com/en/publications/contrabert-enhancing-code-pre-trained-models-via-contrastive-lear"
          },
          {
            "title": "ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning",
            "url": "https://arxiv.org/pdf/2301.09072"
          },
          {
            "title": "[PDF] ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/ContraBERT:-Enhancing-Code-Pre-trained-Models-via-Liu-Wu/f6572fccea70e5023cc38cb33ebd0f520d7b22e2"
          },
          {
            "title": "[2301.09072] ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning",
            "url": "https://arxiv.org/abs/2301.09072"
          },
          {
            "title": "ContraBERT: Enhancing Code Pre-Trained Models via Contrastive Learning | Proceedings of the 45th International Conference on Software Engineering",
            "url": "https://dl.acm.org/doi/abs/10.1109/ICSE48619.2023.00207"
          },
          {
            "title": "ContraBERT: Enhancing Code Pre-trained Models via ...",
            "url": "https://www.computer.org/csdl/proceedings-article/icse/2023/570100c476/1OM4OrPPiNy"
          },
          {
            "title": "ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning | Request PDF",
            "url": "https://www.researchgate.net/publication/372385658_ContraBERT_Enhancing_Code_Pre-trained_Models_via_Contrastive_Learning"
          },
          {
            "title": "About me - Shangqing Liu’s Homepage",
            "url": "https://shangqing-liu.github.io/"
          },
          {
            "title": "(PDF) ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning",
            "url": "https://www.researchgate.net/publication/367359448_ContraBERT_Enhancing_Code_Pre-trained_Models_via_Contrastive_Learning"
          },
          {
            "title": "GitHub - saltudelft/ml4se: A curated list of papers, theses, datasets, and tools related to the application of Machine Learning for Software Engineering · GitHub",
            "url": "https://github.com/saltudelft/ml4se"
          }
        ]
      },
      "Based on the web search results, here's what I found about ContraBERT:\n\n## Overview\n\nContraBERT is an approach that aims to improve the robustness of pre-trained models via contrastive learning. The paper was published at the 45th IEEE/ACM International Conference on Software Engineering (ICSE 2023) by authors Shangqing Liu, Bozhi Wu, Xiaofei Xie, Guozhu Meng, and Yang Liu.\n\n## Problem Being Addressed\n\nState-of-the-art pre-trained models such as CodeBERT and GraphCodeBERT are susceptible to adversarial attacks, with performance dropping significantly with simple perturbations such as renaming variable names.\n\n## Approach\n\nThe method designs nine kinds of simple and complex data augmentation operators on the programming language (PL) and natural language (NL) data to construct different variants. The existing pre-trained models are further trained by masked language modeling (MLM) and contrastive pre-training tasks on the original samples with their augmented variants to enhance robustness.\n\n## Results\n\nThe experiments demonstrate that ContraBERT can effectively improve the robustness of existing pre-trained models, with robustness-enhanced models providing improvements over four popular downstream tasks."
    ],
    "durationSeconds": 6.4474945890000015
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-15T05:11:24.817Z_

<details><summary>↩ Tool result · `toolu_01NygSVfnrrcWgVkEgyZtGzB`</summary>

```text
Web search results for query: "CrossCodeEval NeurIPS 2023 cross-file context code completion benchmark"

Links: [{"title":"GitHub - amazon-science/cceval: CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion (NeurIPS 2023)","url":"https://github.com/amazon-science/cceval"},{"title":"NeurIPS Poster CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion","url":"https://neurips.cc/virtual/2023/poster/73423"},{"title":"A Diverse and Multilingual Benchmark for Cross-File Code ...","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/920f2dced7d32ab2ba2f1970bc306af6-Paper-Datasets_and_Benchmarks.pdf"},{"title":"CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion","url":"https://proceedings.neurips.cc/paper_files/paper/2023/hash/920f2dced7d32ab2ba2f1970bc306af6-Abstract-Datasets_and_Benchmarks.html"},{"title":"cceval/README.md at a11b8a6c71cf1fe99881dd22d14871c6f01bd30f · amazon-science/cceval","url":"https://github.com/amazon-science/cceval/blob/a11b8a6c71cf1fe99881dd22d14871c6f01bd30f/README.md"},{"title":"CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion | OpenReview","url":"https://openreview.net/forum?id=wgDcbBMSfh"},{"title":"cceval/README.md at main · amazon-science/cceval","url":"https://github.com/amazon-science/cceval/blob/main/README.md"},{"title":"CrossCodeEval","url":"https://crosscodeeval.github.io/"},{"title":"A Diverse and Multilingual Benchmark for Cross-File Code ...","url":"https://neurips.cc/media/neurips-2023/Slides/73423.pdf"},{"title":"[2310.11248] CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion","url":"https://arxiv.org/abs/2310.11248"}]

I've found comprehensive information about CrossCodeEval. Here are the key findings:

## Overview

CrossCodeEval is a NeurIPS 2023 (Datasets and Benchmarks track) paper on "CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion."

## Purpose and Motivation

Current popular evaluation datasets like HumanEval and MBPP focus on code completion within a single file, which falls short of representing real-world software development where repositories span multiple files with cross-file dependencies. CrossCodeEval addresses this gap as a diverse and multilingual code completion benchmark that necessitates in-depth cross-file contextual understanding.

## Dataset Composition

CrossCodeEval is built on real-world, open-sourced, permissively-licensed repositories in four popular programming languages: Python, Java, TypeScript, and C#. The dataset is composed of 10k examples from 1k repositories in 4 languages.

## Key Methodology

To create examples that strictly require cross-file context for accurate completion, they propose a straightforward yet efficient static-analysis-based approach to pinpoint the use of cross-file context within the current file.

## Experimental Results

Experiments on state-of-the-art code language models like CodeGen and StarCoder demonstrate that CrossCodeEval is extremely challenging when cross-file context is absent, with clear improvements when adding this context into the prompt. Despite improvements, the pinnacle of performance remains unattained even with the highest-performing model, indicating CrossCodeEval can assess models' capability in leveraging extensive context.

CrossCodeEval can also be used to measure the capability of code retrievers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "d5cabb53-ee6e-4acd-9c87-2f9cb40b31c2",
  "tool_use_result": {
    "query": "CrossCodeEval NeurIPS 2023 cross-file context code completion benchmark",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KGNB9y1GCNMY3eESiH7vAr",
        "content": [
          {
            "title": "GitHub - amazon-science/cceval: CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion (NeurIPS 2023)",
            "url": "https://github.com/amazon-science/cceval"
          },
          {
            "title": "NeurIPS Poster CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion",
            "url": "https://neurips.cc/virtual/2023/poster/73423"
          },
          {
            "title": "A Diverse and Multilingual Benchmark for Cross-File Code ...",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2023/file/920f2dced7d32ab2ba2f1970bc306af6-Paper-Datasets_and_Benchmarks.pdf"
          },
          {
            "title": "CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2023/hash/920f2dced7d32ab2ba2f1970bc306af6-Abstract-Datasets_and_Benchmarks.html"
          },
          {
            "title": "cceval/README.md at a11b8a6c71cf1fe99881dd22d14871c6f01bd30f · amazon-science/cceval",
            "url": "https://github.com/amazon-science/cceval/blob/a11b8a6c71cf1fe99881dd22d14871c6f01bd30f/README.md"
          },
          {
            "title": "CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion | OpenReview",
            "url": "https://openreview.net/forum?id=wgDcbBMSfh"
          },
          {
            "title": "cceval/README.md at main · amazon-science/cceval",
            "url": "https://github.com/amazon-science/cceval/blob/main/README.md"
          },
          {
            "title": "CrossCodeEval",
            "url": "https://crosscodeeval.github.io/"
          },
          {
            "title": "A Diverse and Multilingual Benchmark for Cross-File Code ...",
            "url": "https://neurips.cc/media/neurips-2023/Slides/73423.pdf"
          },
          {
            "title": "[2310.11248] CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion",
            "url": "https://arxiv.org/abs/2310.11248"
          }
        ]
      },
      "I've found comprehensive information about CrossCodeEval. Here are the key findings:\n\n## Overview\n\nCrossCodeEval is a NeurIPS 2023 (Datasets and Benchmarks track) paper on \"CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion.\"\n\n## Purpose and Motivation\n\nCurrent popular evaluation datasets like HumanEval and MBPP focus on code completion within a single file, which falls short of representing real-world software development where repositories span multiple files with cross-file dependencies. CrossCodeEval addresses this gap as a diverse and multilingual code completion benchmark that necessitates in-depth cross-file contextual understanding.\n\n## Dataset Composition\n\nCrossCodeEval is built on real-world, open-sourced, permissively-licensed repositories in four popular programming languages: Python, Java, TypeScript, and C#. The dataset is composed of 10k examples from 1k repositories in 4 languages.\n\n## Key Methodology\n\nTo create examples that strictly require cross-file context for accurate completion, they propose a straightforward yet efficient static-analysis-based approach to pinpoint the use of cross-file context within the current file.\n\n## Experimental Results\n\nExperiments on state-of-the-art code language models like CodeGen and StarCoder demonstrate that CrossCodeEval is extremely challenging when cross-file context is absent, with clear improvements when adding this context into the prompt. Despite improvements, the pinnacle of performance remains unattained even with the highest-performing model, indicating CrossCodeEval can assess models' capability in leveraging extensive context.\n\nCrossCodeEval can also be used to measure the capability of code retrievers."
    ],
    "durationSeconds": 5.516935644999998
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-15T05:11:25.473Z_

<details><summary>↩ Tool result · `toolu_01NGMnio7CEnA2sitXArPrXX`</summary>

```text
Web search results for query: "CAPSTONE EMNLP 2023 code representation learning AST probing"

Links: [{"title":"3RD MULTILINGUAL REPRESENTATION LEARNING (MRL) WORKSHOP @EMNLP 2023","url":"https://sigtyp.github.io/ws2023-mrl.html"},{"title":"Syntax-Aware Retrieval Augmented Code Generation","url":"https://aclanthology.org/2023.findings-emnlp.90.pdf"},{"title":"Evaluating and Enhancing the Robustness of Code Pre- ...","url":"https://aclanthology.org/2023.findings-emnlp.991.pdf"},{"title":"The 2023 Conference on Empirical Methods in Natural Language Processing - ACL Anthology","url":"https://aclanthology.org/events/emnlp-2023/"},{"title":"Findings - EMNLP 2023","url":"https://2023.emnlp.org/program/accepted_findings/"},{"title":"Pass-Tuning: Towards Structure-Aware Parameter-Efficient ...","url":"https://aclanthology.org/2023.findings-emnlp.42.pdf"},{"title":"Pass-Tuning: Towards Structure-Aware Parameter-Efficient Tuning for Code Representation Learning - ACL Anthology","url":"https://aclanthology.org/2023.findings-emnlp.42/"},{"title":"Larger Probes Tell a Different Story: Extending Psycholinguistic Datasets Via In-Context Learning - ACL Anthology","url":"https://aclanthology.org/2023.emnlp-main.130/"},{"title":"Paper Digest: EMNLP-2023 Highlights (Full List)","url":"https://www.paperdigest.org/data/emnlp-2023-full.html"},{"title":"EMNLP 2023 Primer","url":"https://www.ruder.io/emnlp-2023-primer/"}]

Based on the search results, I found relevant information about code representation learning and AST probing at EMNLP 2023:

**Pass-Tuning** proposes structure-aware parameter-efficient code representation learning using a plug-and-play graph neural network module that learns from Abstract Syntax Trees (AST) as a tunable prefix. The method was evaluated on multiple tasks across eight programming languages, including code understanding and generation, with results demonstrating its effectiveness, robustness, and universality.

However, I should note that the search results do not contain a paper specifically titled "CAPSTONE" from EMNLP 2023. The results show "Pass-Tuning" as a prominent work on code representation learning with AST at EMNLP 2023 Findings. If you're looking for a specific paper called "CAPSTONE," you may want to provide additional details or search directly on the ACL Anthology website.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "585ab053-1b7e-4e19-a9bf-0048f603f45b",
  "tool_use_result": {
    "query": "CAPSTONE EMNLP 2023 code representation learning AST probing",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GmdQoQwaCR4swXNHEJQuf7",
        "content": [
          {
            "title": "3RD MULTILINGUAL REPRESENTATION LEARNING (MRL) WORKSHOP @EMNLP 2023",
            "url": "https://sigtyp.github.io/ws2023-mrl.html"
          },
          {
            "title": "Syntax-Aware Retrieval Augmented Code Generation",
            "url": "https://aclanthology.org/2023.findings-emnlp.90.pdf"
          },
          {
            "title": "Evaluating and Enhancing the Robustness of Code Pre- ...",
            "url": "https://aclanthology.org/2023.findings-emnlp.991.pdf"
          },
          {
            "title": "The 2023 Conference on Empirical Methods in Natural Language Processing - ACL Anthology",
            "url": "https://aclanthology.org/events/emnlp-2023/"
          },
          {
            "title": "Findings - EMNLP 2023",
            "url": "https://2023.emnlp.org/program/accepted_findings/"
          },
          {
            "title": "Pass-Tuning: Towards Structure-Aware Parameter-Efficient ...",
            "url": "https://aclanthology.org/2023.findings-emnlp.42.pdf"
          },
          {
            "title": "Pass-Tuning: Towards Structure-Aware Parameter-Efficient Tuning for Code Representation Learning - ACL Anthology",
            "url": "https://aclanthology.org/2023.findings-emnlp.42/"
          },
          {
            "title": "Larger Probes Tell a Different Story: Extending Psycholinguistic Datasets Via In-Context Learning - ACL Anthology",
            "url": "https://aclanthology.org/2023.emnlp-main.130/"
          },
          {
            "title": "Paper Digest: EMNLP-2023 Highlights (Full List)",
            "url": "https://www.paperdigest.org/data/emnlp-2023-full.html"
          },
          {
            "title": "EMNLP 2023 Primer",
            "url": "https://www.ruder.io/emnlp-2023-primer/"
          }
        ]
      },
      "Based on the search results, I found relevant information about code representation learning and AST probing at EMNLP 2023:\n\n**Pass-Tuning** proposes structure-aware parameter-efficient code representation learning using a plug-and-play graph neural network module that learns from Abstract Syntax Trees (AST) as a tunable prefix. The method was evaluated on multiple tasks across eight programming languages, including code understanding and generation, with results demonstrating its effectiveness, robustness, and universality.\n\nHowever, I should note that the search results do not contain a paper specifically titled \"CAPSTONE\" from EMNLP 2023. The results show \"Pass-Tuning\" as a prominent work on code representation learning with AST at EMNLP 2023 Findings. If you're looking for a specific paper called \"CAPSTONE,\" you may want to provide additional details or search directly on the ACL Anthology website."
    ],
    "durationSeconds": 5.227999647999997
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-15T05:11:26.229Z_

<details><summary>↩ Tool result · `toolu_01X9PdsBpXRTLs3MWpNXBQUt`</summary>

```text
Web search results for query: "SynCoBERT 2021 syntax contrastive pre-training code representation arXiv"

Links: [{"title":"[2108.04556] SynCoBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation","url":"https://arxiv.org/abs/2108.04556"},{"title":"SynCoBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation - ADS","url":"https://ui.adsabs.harvard.edu/abs/2021arXiv210804556W/abstract"},{"title":"[2108.04556] SynCoBERT: Syntax-Enhanced Contrastive Pre-Training for Code Representation","url":"https://ar5iv.labs.arxiv.org/html/2108.04556"},{"title":"[2108.04556v3] SynCoBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation","url":"https://arxiv.org/abs/2108.04556v3"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?title=Syncobert:+syntax-guided+multi-modal+contrastive+pre-training+for+code+representation&amp=&author=X.+Wang&amp=&author=Y.+Wang&amp=&author=F.+Mi&amp=&author=P.+Zhou&amp=&publication_year=2021"},{"title":"[PDF] SynCoBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/SynCoBERT:-Syntax-Guided-Multi-Modal-Contrastive-Wang-Wang/14b104d1a1c0b784e4e74454d809455cc47d0093"},{"title":"SynCoBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation · Machine Learning for Big Code and Naturalness","url":"https://ml4code.github.io/publications/wang2021syncobert/"},{"title":"SYNCOBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for","url":"https://arxiv.org/pdf/2108.04556"},{"title":"(PDF) SynCoBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation","url":"https://www.academia.edu/73281297/SynCoBERT_Syntax_Guided_Multi_Modal_Contrastive_Pre_Training_for_Code_Representation"},{"title":"[PDF] GraphCodeBERT: Pre-training Code Representations with Data Flow | Semantic Scholar","url":"https://www.semanticscholar.org/paper/GraphCodeBERT:-Pre-training-Code-Representations-Guo-Ren/4083958684292f6fa2f5c7fd4f9be975e80145b6"}]

I found information about SynCoBERT for you. Here are the key details:

## Overview

SynCoBERT is a syntax-guided multi-modal contrastive pre-training approach for better code representations. The paper was published on arXiv (paper 2108.04556) with the latest version from September 9, 2021.

## Key Contributions

The paper designs two novel pre-training objectives originating from the symbolic and syntactic properties of source code: Identifier Prediction (IP) and AST Edge Prediction (TEP), which are designed to predict identifiers and edges between two nodes of AST, respectively.

To exploit complementary information in semantically equivalent modalities (code, comment, AST), the authors propose a multi-modal contrastive learning strategy to maximize mutual information among different modalities.

## Performance

Extensive experiments on four downstream tasks related to code intelligence show that SynCoBERT advances the state-of-the-art with the same pre-training corpus and model size.

## Access

The paper is available at:
- **arXiv**: https://arxiv.org/abs/2108.04556
- **PDF**: https://arxiv.org/pdf/2108.04556

The authors listed on the paper are Xin Wang and 9 other collaborators.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "bb330a70-a9f9-426b-8ec6-14ddc17e28a4",
  "tool_use_result": {
    "query": "SynCoBERT 2021 syntax contrastive pre-training code representation arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VSxUjkzhWGHhfU6svrDv9F",
        "content": [
          {
            "title": "[2108.04556] SynCoBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation",
            "url": "https://arxiv.org/abs/2108.04556"
          },
          {
            "title": "SynCoBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2021arXiv210804556W/abstract"
          },
          {
            "title": "[2108.04556] SynCoBERT: Syntax-Enhanced Contrastive Pre-Training for Code Representation",
            "url": "https://ar5iv.labs.arxiv.org/html/2108.04556"
          },
          {
            "title": "[2108.04556v3] SynCoBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation",
            "url": "https://arxiv.org/abs/2108.04556v3"
          },
          {
            "title": "Google Scholar",
            "url": "https://scholar.google.com/scholar_lookup?title=Syncobert:+syntax-guided+multi-modal+contrastive+pre-training+for+code+representation&amp=&author=X.+Wang&amp=&author=Y.+Wang&amp=&author=F.+Mi&amp=&author=P.+Zhou&amp=&publication_year=2021"
          },
          {
            "title": "[PDF] SynCoBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/SynCoBERT:-Syntax-Guided-Multi-Modal-Contrastive-Wang-Wang/14b104d1a1c0b784e4e74454d809455cc47d0093"
          },
          {
            "title": "SynCoBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation · Machine Learning for Big Code and Naturalness",
            "url": "https://ml4code.github.io/publications/wang2021syncobert/"
          },
          {
            "title": "SYNCOBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for",
            "url": "https://arxiv.org/pdf/2108.04556"
          },
          {
            "title": "(PDF) SynCoBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation",
            "url": "https://www.academia.edu/73281297/SynCoBERT_Syntax_Guided_Multi_Modal_Contrastive_Pre_Training_for_Code_Representation"
          },
          {
            "title": "[PDF] GraphCodeBERT: Pre-training Code Representations with Data Flow | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/GraphCodeBERT:-Pre-training-Code-Representations-Guo-Ren/4083958684292f6fa2f5c7fd4f9be975e80145b6"
          }
        ]
      },
      "I found information about SynCoBERT for you. Here are the key details:\n\n## Overview\n\nSynCoBERT is a syntax-guided multi-modal contrastive pre-training approach for better code representations. The paper was published on arXiv (paper 2108.04556) with the latest version from September 9, 2021.\n\n## Key Contributions\n\nThe paper designs two novel pre-training objectives originating from the symbolic and syntactic properties of source code: Identifier Prediction (IP) and AST Edge Prediction (TEP), which are designed to predict identifiers and edges between two nodes of AST, respectively.\n\nTo exploit complementary information in semantically equivalent modalities (code, comment, AST), the authors propose a multi-modal contrastive learning strategy to maximize mutual information among different modalities.\n\n## Performance\n\nExtensive experiments on four downstream tasks related to code intelligence show that SynCoBERT advances the state-of-the-art with the same pre-training corpus and model size.\n\n## Access\n\nThe paper is available at:\n- **arXiv**: https://arxiv.org/abs/2108.04556\n- **PDF**: https://arxiv.org/pdf/2108.04556\n\nThe authors listed on the paper are Xin Wang and 9 other collaborators."
    ],
    "durationSeconds": 6.443835533999998
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-15T05:11:28.152Z_

<details><summary>↩ Tool result · `toolu_01QxAn5rxDDvmFinwAwFZqVd`</summary>

```text
Web search results for query: "CoSQA ACL 2021 code search question answering web query dataset"

Links: [{"title":"CoSQA: 20,000+ Web Queries for Code Search and Question Answering - ACL Anthology","url":"https://aclanthology.org/2021.acl-long.442/"},{"title":"GitHub - Jun-jie-Huang/CoCLR: Source Code for ACL-21 main conference paper \"CoSQA: 20,000+ Web Queries for Code Search and Question Answering\".","url":"https://github.com/Jun-jie-Huang/CoCLR"},{"title":"CoSQA: 20,000+ Web Queries for Code Search and Question Answering - ADS","url":"https://ui.adsabs.harvard.edu/abs/2021arXiv210513239H/abstract"},{"title":"[2105.13239v1] CoSQA: 20,000+ Web Queries for Code Search and Question Answering","url":"https://arxiv.org/abs/2105.13239v1"},{"title":"Contrastive Learning with Keyword-based Data ...","url":"https://aclanthology.org/2023.eacl-main.262.pdf"},{"title":"[Quick Review] CoSQA: 20,000+ Web Queries for Code Search and Question Answering","url":"https://liner.com/review/cosqa-20000-web-queries-for-code-search-and-question-answering"},{"title":"[2105.13239] CoSQA: 20,000+ Web Queries for Code Search and Question Answering","url":"https://arxiv.org/abs/2105.13239"},{"title":"CodeQA: A Question Answering Dataset for Source Code Comprehension - ACL Anthology","url":"https://aclanthology.org/2021.findings-emnlp.223/"},{"title":"CoSQA: 20,000+ Web Queries for Code Search and Question Answering","url":"https://gengo.sotaro.io/2021.acl-long.442"},{"title":"CoSQA: 20,000+ Web Queries for Code Search and Question Answering · Machine Learning for Big Code and Naturalness","url":"https://ml4code.github.io/publications/huang2021cosqa/"}]

I found comprehensive information about the CoSQA dataset. Here are the key details:

## Overview
CoSQA includes 20,604 labels for pairs of natural language queries and codes, each annotated by at least 3 human annotators. The dataset contains real-world web queries and Python functions, specifically designed for code search and question answering.

## Publication
The paper was presented at the Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers) in 2021. The authors are Junjie Huang, Duyu Tang, Linjun Shou, Ming Gong, Ke Xu, Daxin Jiang, Ming Zhou, and Nan Duan.

## Key Contributions
The paper introduces a contrastive learning method dubbed CoCLR to enhance text-code matching, which works as a data augmenter to bring more artificially generated training instances.

## Performance Results
Training on CoSQA improves the accuracy of code question answering by 5.1% and incorporating CoCLR brings a further improvement of 10.5% when evaluated on CodeXGLUE with the CodeBERT model.

## Data Access
The CoSQA data and leaderboard are available at https://github.com/microsoft/CodeXGLUE/tree/main/Text-Code/NL-code-search-WebQuery.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "0c5cec02-f804-4be3-8419-623bce2a7488",
  "tool_use_result": {
    "query": "CoSQA ACL 2021 code search question answering web query dataset",
    "results": [
      {
        "tool_use_id": "srvtoolu_0162CD7pQomKPEK5KwkFi1Jj",
        "content": [
          {
            "title": "CoSQA: 20,000+ Web Queries for Code Search and Question Answering - ACL Anthology",
            "url": "https://aclanthology.org/2021.acl-long.442/"
          },
          {
            "title": "GitHub - Jun-jie-Huang/CoCLR: Source Code for ACL-21 main conference paper \"CoSQA: 20,000+ Web Queries for Code Search and Question Answering\".",
            "url": "https://github.com/Jun-jie-Huang/CoCLR"
          },
          {
            "title": "CoSQA: 20,000+ Web Queries for Code Search and Question Answering - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2021arXiv210513239H/abstract"
          },
          {
            "title": "[2105.13239v1] CoSQA: 20,000+ Web Queries for Code Search and Question Answering",
            "url": "https://arxiv.org/abs/2105.13239v1"
          },
          {
            "title": "Contrastive Learning with Keyword-based Data ...",
            "url": "https://aclanthology.org/2023.eacl-main.262.pdf"
          },
          {
            "title": "[Quick Review] CoSQA: 20,000+ Web Queries for Code Search and Question Answering",
            "url": "https://liner.com/review/cosqa-20000-web-queries-for-code-search-and-question-answering"
          },
          {
            "title": "[2105.13239] CoSQA: 20,000+ Web Queries for Code Search and Question Answering",
            "url": "https://arxiv.org/abs/2105.13239"
          },
          {
            "title": "CodeQA: A Question Answering Dataset for Source Code Comprehension - ACL Anthology",
            "url": "https://aclanthology.org/2021.findings-emnlp.223/"
          },
          {
            "title": "CoSQA: 20,000+ Web Queries for Code Search and Question Answering",
            "url": "https://gengo.sotaro.io/2021.acl-long.442"
          },
          {
            "title": "CoSQA: 20,000+ Web Queries for Code Search and Question Answering · Machine Learning for Big Code and Naturalness",
            "url": "https://ml4code.github.io/publications/huang2021cosqa/"
          }
        ]
      },
      "I found comprehensive information about the CoSQA dataset. Here are the key details:\n\n## Overview\nCoSQA includes 20,604 labels for pairs of natural language queries and codes, each annotated by at least 3 human annotators. The dataset contains real-world web queries and Python functions, specifically designed for code search and question answering.\n\n## Publication\nThe paper was presented at the Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers) in 2021. The authors are Junjie Huang, Duyu Tang, Linjun Shou, Ming Gong, Ke Xu, Daxin Jiang, Ming Zhou, and Nan Duan.\n\n## Key Contributions\nThe paper introduces a contrastive learning method dubbed CoCLR to enhance text-code matching, which works as a data augmenter to bring more artificially generated training instances.\n\n## Performance Results\nTraining on CoSQA improves the accuracy of code question answering by 5.1% and incorporating CoCLR brings a further improvement of 10.5% when evaluated on CodeXGLUE with the CodeBERT model.\n\n## Data Access\nThe CoSQA data and leaderboard are available at https://github.com/microsoft/CodeXGLUE/tree/main/Text-Code/NL-code-search-WebQuery."
    ],
    "durationSeconds": 7.417002628000002
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-15T05:11:29.903Z_

<details><summary>↩ Tool result · `toolu_01SjmXyqESgXwu8KnCxEkkdn`</summary>

```text
Web search results for query: "ProGraML ICML 2021 program graph machine learning Chris Cummins"

Links: [{"title":"GitHub - ChrisCummins/ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations · GitHub","url":"https://github.com/ChrisCummins/ProGraML"},{"title":"PROGRAML: A Graph-based Program Representation for Data Flow Analysis","url":"https://chriscummins.cc/pub/2021-icml.pdf"},{"title":"[PDF] ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations | Semantic Scholar","url":"https://www.semanticscholar.org/paper/ProGraML:-A-Graph-based-Program-Representation-for-Cummins-Fisches/7843876d45f4c6ac751039b198aade0ee9f94342"},{"title":"ICML 2021 ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations Spotlight","url":"https://icml.cc/virtual/2021/spotlight/8886"},{"title":"dblp: Chris Cummins","url":"https://dblp.org/pid/24/997.html"},{"title":"ProGraML: Graph-based Deep Learning for Program Optimization and Analysis.","url":"https://spcl.inf.ethz.ch/Publications/.pdf/programl-icml21-slides.pdf"},{"title":"Machine Learning for Software Engineering papers at ICML 2021 · GitHub","url":"https://gist.github.com/bzz/38cfef2e735393a5ccf59f70ddff77d0"},{"title":"ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations","url":"https://proceedings.mlr.press/v139/cummins21a.html"},{"title":"[2003.10536] ProGraML: Graph-based Deep Learning for Program Optimization and Analysis","url":"https://arxiv.org/abs/2003.10536"},{"title":"PROGRAML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations - University of Edinburgh Research Explorer","url":"https://www.research.ed.ac.uk/en/publications/programl-a-graph-based-program-representation-for-data-flow-analy"}]

I've found comprehensive information about ProGraML from ICML 2021. Here are the key findings:

## ProGraML Overview

ProGraML - Program Graphs for Machine Learning - is a language-independent, portable representation of program semantics. ProGraML is a representation for programs as input to a machine learning model.

## Publication Details

The paper was published at the Thirty-eighth International Conference on Machine Learning (ICML) in 2021, authored by Chris Cummins, Zacharias Fisches, Tal Ben-Nun, Torsten Hoefler, Michael O'Boyle, and Hugh Leather.

## Key Features

The system supports several programming languages (C, C++, LLVM-IR, XLA) and several graph formats (NetworkX, DGL, Graphviz, JSON) out of the box. It captures every control, data, and call relation across entire programs.

## Performance

On a benchmark dataset of 250k LLVM-IR files covering six source programming languages, ProGraML achieves an average 94.0 F1 score, significantly outperforming the state-of-the-art approaches.

## Resources

The tool is available through pip install, requiring no compilation. The project is open source and available on GitHub at https://github.com/ChrisCummins/ProGraML.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "ae342ef7-6ddc-47a5-8802-51436ef788f3",
  "tool_use_result": {
    "query": "ProGraML ICML 2021 program graph machine learning Chris Cummins",
    "results": [
      {
        "tool_use_id": "srvtoolu_014DLr9X765qeibRgt4qWMNN",
        "content": [
          {
            "title": "GitHub - ChrisCummins/ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations · GitHub",
            "url": "https://github.com/ChrisCummins/ProGraML"
          },
          {
            "title": "PROGRAML: A Graph-based Program Representation for Data Flow Analysis",
            "url": "https://chriscummins.cc/pub/2021-icml.pdf"
          },
          {
            "title": "[PDF] ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/ProGraML:-A-Graph-based-Program-Representation-for-Cummins-Fisches/7843876d45f4c6ac751039b198aade0ee9f94342"
          },
          {
            "title": "ICML 2021 ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations Spotlight",
            "url": "https://icml.cc/virtual/2021/spotlight/8886"
          },
          {
            "title": "dblp: Chris Cummins",
            "url": "https://dblp.org/pid/24/997.html"
          },
          {
            "title": "ProGraML: Graph-based Deep Learning for Program Optimization and Analysis.",
            "url": "https://spcl.inf.ethz.ch/Publications/.pdf/programl-icml21-slides.pdf"
          },
          {
            "title": "Machine Learning for Software Engineering papers at ICML 2021 · GitHub",
            "url": "https://gist.github.com/bzz/38cfef2e735393a5ccf59f70ddff77d0"
          },
          {
            "title": "ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations",
            "url": "https://proceedings.mlr.press/v139/cummins21a.html"
          },
          {
            "title": "[2003.10536] ProGraML: Graph-based Deep Learning for Program Optimization and Analysis",
            "url": "https://arxiv.org/abs/2003.10536"
          },
          {
            "title": "PROGRAML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations - University of Edinburgh Research Explorer",
            "url": "https://www.research.ed.ac.uk/en/publications/programl-a-graph-based-program-representation-for-data-flow-analy"
          }
        ]
      },
      "I've found comprehensive information about ProGraML from ICML 2021. Here are the key findings:\n\n## ProGraML Overview\n\nProGraML - Program Graphs for Machine Learning - is a language-independent, portable representation of program semantics. ProGraML is a representation for programs as input to a machine learning model.\n\n## Publication Details\n\nThe paper was published at the Thirty-eighth International Conference on Machine Learning (ICML) in 2021, authored by Chris Cummins, Zacharias Fisches, Tal Ben-Nun, Torsten Hoefler, Michael O'Boyle, and Hugh Leather.\n\n## Key Features\n\nThe system supports several programming languages (C, C++, LLVM-IR, XLA) and several graph formats (NetworkX, DGL, Graphviz, JSON) out of the box. It captures every control, data, and call relation across entire programs.\n\n## Performance\n\nOn a benchmark dataset of 250k LLVM-IR files covering six source programming languages, ProGraML achieves an average 94.0 F1 score, significantly outperforming the state-of-the-art approaches.\n\n## Resources\n\nThe tool is available through pip install, requiring no compilation. The project is open source and available on GitHub at https://github.com/ChrisCummins/ProGraML."
    ],
    "durationSeconds": 11.077083359999996
  }
}
```

</details>

---

### Assistant

_source line 35_

<details><summary>Logged reasoning block</summary>

```text
CAPSTONE didn't come up directly. Let me search more specifically for it.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "24c1d942-8d84-40f7-a74b-9eb7290c0a64",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012AMVs6UsiTtPLvNRNDzBSE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3802,
      "cache_creation_input_tokens": 2965,
      "cache_read_input_tokens": 40519,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2965
      },
      "output_tokens": 31,
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

_source line 36_

CAPSTONE 搜索没命中，需要更精确的搜索。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "70848f31-0ef9-4513-b25f-4d03078eaba9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012AMVs6UsiTtPLvNRNDzBSE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3802,
      "cache_creation_input_tokens": 2965,
      "cache_read_input_tokens": 40519,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2965
      },
      "output_tokens": 31,
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

_source line 37_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TrVTUJepkv1F5cXo1AjR8D`</summary>

```json
{
  "query": "\"CAPSTONE\" code pre-training semantic structure EMNLP 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "9487af81-cd30-4244-865c-590a4d4f09a9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012AMVs6UsiTtPLvNRNDzBSE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3802,
      "cache_creation_input_tokens": 2965,
      "cache_read_input_tokens": 40519,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2965
      },
      "output_tokens": 31,
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

_source line 38 · 2026-05-15T05:11:47.523Z_

<details><summary>↩ Tool result · `toolu_01TrVTUJepkv1F5cXo1AjR8D`</summary>

```text
Web search results for query: ""CAPSTONE" code pre-training semantic structure EMNLP 2023"

Links: [{"title":"Findings - EMNLP 2023","url":"https://2023.emnlp.org/program/accepted_findings/"},{"title":"dblp: EMNLP (Findings) 2023","url":"https://dblp.org/db/conf/emnlp/emnlp2023f.html"},{"title":"EMNLP 2023: Singapore","url":"https://dblp.org/db/conf/emnlp/emnlp2023.html"},{"title":"dblp: EMNLP 2023 - System Demonstrations","url":"https://dblp.org/db/conf/emnlp/emnlp2023d.html"},{"title":"EMNLP 2023 Paraphrase Types for Generation and Detection","url":"https://arxiv.org/html/2310.14863v3"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"},{"title":"Evaluating and Enhancing the Robustness of Code Pre- ...","url":"https://aclanthology.org/2023.findings-emnlp.991.pdf"},{"title":"Code Representation Pre-training with Complements from ...","url":"https://aclanthology.org/2024.emnlp-industry.21.pdf"},{"title":"[PDF] CodeBERT: A Pre-Trained Model for Programming and Natural Languages | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CodeBERT:-A-Pre-Trained-Model-for-Programming-and-Feng-Guo/0fe2636446cd686830da3d971b31a004d6094b3c"},{"title":"Instructions for EMNLP 2023 Proceedings","url":"https://arxiv.org/html/2406.18164"}]

The search results show various papers from EMNLP 2023, but I did not find a specific paper titled "CAPSTONE" about code pre-training with semantic structure. Let me search more specifically for this paper.

Links: [{"title":"Programming with C language – Capstone – The Ultimate Disassembler","url":"https://www.capstone-engine.org/lang_c.html"},{"title":"Building capstone exercises | DataCamp Help Center","url":"https://instructor-support.datacamp.com/en/articles/2360754-building-capstone-exercises"},{"title":"Capstone course - Wikipedia","url":"https://en.wikipedia.org/wiki/Capstone_course"},{"title":"Capstone Projects – Natural Language Processing","url":"https://nlp.ucsc.edu/capstone-projects/"},{"title":"Exploiting the Semantic Knowledge of Pre-trained Text-Encoders for Continual Learning","url":"https://arxiv.org/html/2408.01076"},{"title":"ITWS Capstone: Engineering a Semantic Web (Fall 2022) | PPT","url":"https://www.slideshare.net/olyerickson/itws-capstone-engineering-a-semantic-web-fall-2022"},{"title":"AC 2007-267: A PRE-CAPSTONE COURSE DESIGNED TO IMPROVE STUDENT","url":"https://peer.asee.org/a-pre-capstone-course-designed-to-improve-student-performance-on-open-ended-design-projects.pdf"},{"title":"Pre-Trained LLM is a Semantic-Aware and Generalizable Segmentation Booster","url":"https://arxiv.org/html/2506.18034v1"},{"title":"Capstone Project Week Two","url":"https://rstudio-pubs-static.s3.amazonaws.com/641385_4f70192d1a6a428fbb820f42eace45cd.html"},{"title":"Programming with Python language – Capstone – The Ultimate Disassembler","url":"https://www.capstone-engine.org/lang_python.html"}]

Let me search more specifically for this EMNLP 2023 paper.

Links: [{"title":"Accepted Industry Track Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/ind_papers/"},{"title":"GitHub - kwangyy/capstone-project: Capstone Project for the Machine Learning Engineering course created by Alexey Grigorev.","url":"https://github.com/kwangyy/capstone-project"},{"title":"Machine Learning Capstone | Coursera","url":"https://www.coursera.org/learn/machine-learning-capstone"},{"title":"Capstones - Paul G. Allen School of Computer Science & Engineering","url":"https://www.cs.washington.edu/academics/undergraduate/degree-requirements/capstones/"},{"title":"CPA Professional Education Program: Capstone modules - CPA Canada","url":"https://www.cpacanada.ca/become-a-cpa/CPA-Professional-Education-Program-CPA-PEP/CPA-Professional-Education-Program-Capstone-modules"},{"title":"The University of San Francisco The University of San Francisco","url":"https://repository.usfca.edu/cgi/viewcontent.cgi?article=2376&context=capstone"}]

I found a reference! Let me search more specifically for this paper.

Links: [{"title":"Composable Semantics Using Higher-Order Attribute Grammars A DISSERTATION","url":"https://conservancy.umn.edu/server/api/core/bitstreams/cf8160f1-e3cb-49bb-9e03-680f4661e475/content"},{"title":"CAPSTONE: Composable Attribute‐Prompted Scene Translation for Zero‐Shot Vision–Language Reasoning - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-industry.190/"},{"title":"Semantics | Jetpack Compose | Android Developers","url":"https://developer.android.com/jetpack/compose/semantics"},{"title":"Programming with C language – Capstone – The Ultimate Disassembler","url":"https://www.capstone-engine.org/lang_c.html"},{"title":"Programming with Python language – Capstone – The Ultimate Disassembler","url":"https://www.capstone-engine.org/lang_python.html"},{"title":"HTML Semantic Elements","url":"https://www.w3schools.com/html/html5_semantic_elements.asp"},{"title":"GitHub - webplatformco/project-custom-attributes: Define custom attributes that can be specified on any element · GitHub","url":"https://github.com/webplatformco/project-custom-attributes"},{"title":"Programming with Java language – Capstone – The Ultimate Disassembler","url":"https://www.capstone-engine.org/lang_java.html"},{"title":"Elements | Capstone Project","url":"https://ddc-java.github.io/capstone-project/elements.html"},{"title":"Semantic HTML5 Elements Explained","url":"https://www.freecodecamp.org/news/semantic-html5-elements/"}]

Based on my web search results, I found relevant information about CAPSTONE, but it appears the paper is not about code pre-training with semantic structure as your query suggested.

CAPSTONE: Composable Attribute-Prompted Scene Translation for Zero-Shot Vision-Language Reasoning was published in the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track (not EMNLP 2023, but EMNLP 2025).

Instead of relying on multimodal training or fine-tuning large models, CAPSTONE transforms outputs from off-the-shelf vision models into structured text prompts that can be interpreted by a frozen Large Language Model (LLM). This plug-and-play architecture enables reasoning over visual input without access to raw pixels, dramatically reducing computational cost and complexity.

This paper appears to be focused on vision-language reasoning rather than code pre-training. If you're looking for a different CAPSTONE paper specifically about code pre-training semantic structure from EMNLP 2023, the search results did not return that paper. Could you provide additional context or keywords about the specific paper you're looking for?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "d984db67-6b4f-4f95-ae2d-507a6458db2d",
  "tool_use_result": {
    "query": "\"CAPSTONE\" code pre-training semantic structure EMNLP 2023",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NRxG9ttuowg2zUM1c4DSSf",
        "content": [
          {
            "title": "Findings - EMNLP 2023",
            "url": "https://2023.emnlp.org/program/accepted_findings/"
          },
          {
            "title": "dblp: EMNLP (Findings) 2023",
            "url": "https://dblp.org/db/conf/emnlp/emnlp2023f.html"
          },
          {
            "title": "EMNLP 2023: Singapore",
            "url": "https://dblp.org/db/conf/emnlp/emnlp2023.html"
          },
          {
            "title": "dblp: EMNLP 2023 - System Demonstrations",
            "url": "https://dblp.org/db/conf/emnlp/emnlp2023d.html"
          },
          {
            "title": "EMNLP 2023 Paraphrase Types for Generation and Detection",
            "url": "https://arxiv.org/html/2310.14863v3"
          },
          {
            "title": "EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...",
            "url": "http://www.wikicfp.com/cfp/program?id=883"
          },
          {
            "title": "Evaluating and Enhancing the Robustness of Code Pre- ...",
            "url": "https://aclanthology.org/2023.findings-emnlp.991.pdf"
          },
          {
            "title": "Code Representation Pre-training with Complements from ...",
            "url": "https://aclanthology.org/2024.emnlp-industry.21.pdf"
          },
          {
            "title": "[PDF] CodeBERT: A Pre-Trained Model for Programming and Natural Languages | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/CodeBERT:-A-Pre-Trained-Model-for-Programming-and-Feng-Guo/0fe2636446cd686830da3d971b31a004d6094b3c"
          },
          {
            "title": "Instructions for EMNLP 2023 Proceedings",
            "url": "https://arxiv.org/html/2406.18164"
          }
        ]
      },
      "The search results show various papers from EMNLP 2023, but I did not find a specific paper titled \"CAPSTONE\" about code pre-training with semantic structure. Let me search more specifically for this paper.",
      {
        "tool_use_id": "srvtoolu_01STuhvoiF5fbLTRwaDRvH7d",
        "content": [
          {
            "title": "Programming with C language – Capstone – The Ultimate Disassembler",
            "url": "https://www.capstone-engine.org/lang_c.html"
          },
          {
            "title": "Building capstone exercises | DataCamp Help Center",
            "url": "https://instructor-support.datacamp.com/en/articles/2360754-building-capstone-exercises"
          },
          {
            "title": "Capstone course - Wikipedia",
            "url": "https://en.wikipedia.org/wiki/Capstone_course"
          },
          {
            "title": "Capstone Projects – Natural Language Processing",
            "url": "https://nlp.ucsc.edu/capstone-projects/"
          },
          {
            "title": "Exploiting the Semantic Knowledge of Pre-trained Text-Encoders for Continual Learning",
            "url": "https://arxiv.org/html/2408.01076"
          },
          {
            "title": "ITWS Capstone: Engineering a Semantic Web (Fall 2022) | PPT",
            "url": "https://www.slideshare.net/olyerickson/itws-capstone-engineering-a-semantic-web-fall-2022"
          },
          {
            "title": "AC 2007-267: A PRE-CAPSTONE COURSE DESIGNED TO IMPROVE STUDENT",
            "url": "https://peer.asee.org/a-pre-capstone-course-designed-to-improve-student-performance-on-open-ended-design-projects.pdf"
          },
          {
            "title": "Pre-Trained LLM is a Semantic-Aware and Generalizable Segmentation Booster",
            "url": "https://arxiv.org/html/2506.18034v1"
          },
          {
            "title": "Capstone Project Week Two",
            "url": "https://rstudio-pubs-static.s3.amazonaws.com/641385_4f70192d1a6a428fbb820f42eace45cd.html"
          },
          {
            "title": "Programming with Python language – Capstone – The Ultimate Disassembler",
            "url": "https://www.capstone-engine.org/lang_python.html"
          }
        ]
      },
      "Let me search more specifically for this EMNLP 2023 paper.",
      {
        "tool_use_id": "srvtoolu_01Wir68LNrV8XBHBu8jixgtn",
        "content": [
          {
            "title": "Accepted Industry Track Papers - EMNLP 2025",
            "url": "https://2025.emnlp.org/program/ind_papers/"
          },
          {
            "title": "GitHub - kwangyy/capstone-project: Capstone Project for the Machine Learning Engineering course created by Alexey Grigorev.",
            "url": "https://github.com/kwangyy/capstone-project"
          },
          {
            "title": "Machine Learning Capstone | Coursera",
            "url": "https://www.coursera.org/learn/machine-learning-capstone"
          },
          {
            "title": "Capstones - Paul G. Allen School of Computer Science & Engineering",
            "url": "https://www.cs.washington.edu/academics/undergraduate/degree-requirements/capstones/"
          },
          {
            "title": "CPA Professional Education Program: Capstone modules - CPA Canada",
            "url": "https://www.cpacanada.ca/become-a-cpa/CPA-Professional-Education-Program-CPA-PEP/CPA-Professional-Education-Program-Capstone-modules"
          },
          {
            "title": "The University of San Francisco The University of San Francisco",
            "url": "https://repository.usfca.edu/cgi/viewcontent.cgi?article=2376&context=capstone"
          }
        ]
      },
      "I found a reference! Let me search more specifically for this paper.",
      {
        "tool_use_id": "srvtoolu_01AXTWRfKCwtCLs6omk2Qtzi",
        "content": [
          {
            "title": "Composable Semantics Using Higher-Order Attribute Grammars A DISSERTATION",
            "url": "https://conservancy.umn.edu/server/api/core/bitstreams/cf8160f1-e3cb-49bb-9e03-680f4661e475/content"
          },
          {
            "title": "CAPSTONE: Composable Attribute‐Prompted Scene Translation for Zero‐Shot Vision–Language Reasoning - ACL Anthology",
            "url": "https://aclanthology.org/2025.emnlp-industry.190/"
          },
          {
            "title": "Semantics | Jetpack Compose | Android Developers",
            "url": "https://developer.android.com/jetpack/compose/semantics"
          },
          {
            "title": "Programming with C language – Capstone – The Ultimate Disassembler",
            "url": "https://www.capstone-engine.org/lang_c.html"
          },
          {
            "title": "Programming with Python language – Capstone – The Ultimate Disassembler",
            "url": "https://www.capstone-engine.org/lang_python.html"
          },
          {
            "title": "HTML Semantic Elements",
            "url": "https://www.w3schools.com/html/html5_semantic_elements.asp"
          },
          {
            "title": "GitHub - webplatformco/project-custom-attributes: Define custom attributes that can be specified on any element · GitHub",
            "url": "https://github.com/webplatformco/project-custom-attributes"
          },
          {
            "title": "Programming with Java language – Capstone – The Ultimate Disassembler",
            "url": "https://www.capstone-engine.org/lang_java.html"
          },
          {
            "title": "Elements | Capstone Project",
            "url": "https://ddc-java.github.io/capstone-project/elements.html"
          },
          {
            "title": "Semantic HTML5 Elements Explained",
            "url": "https://www.freecodecamp.org/news/semantic-html5-elements/"
          }
        ]
      },
      "Based on my web search results, I found relevant information about CAPSTONE, but it appears the paper is not about code pre-training with semantic structure as your query suggested.\n\nCAPSTONE: Composable Attribute-Prompted Scene Translation for Zero-Shot Vision-Language Reasoning was published in the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track (not EMNLP 2023, but EMNLP 2025).\n\nInstead of relying on multimodal training or fine-tuning large models, CAPSTONE transforms outputs from off-the-shelf vision models into structured text prompts that can be interpreted by a frozen Large Language Model (LLM). This plug-and-play architecture enables reasoning over visual input without access to raw pixels, dramatically reducing computational cost and complexity.\n\nThis paper appears to be focused on vision-language reasoning rather than code pre-training. If you're looking for a different CAPSTONE paper specifically about code pre-training semantic structure from EMNLP 2023, the search results did not return that paper. Could you provide additional context or keywords about the specific paper you're looking for?"
    ],
    "durationSeconds": 13.88584549
  }
}
```

</details>

---

### Assistant

_source line 39_

<details><summary>Logged reasoning block</summary>

```text
CAPSTONE didn't come up as a code-related paper. Let me search with different terms. Maybe it's about code pre-training with a different name or at a different venue.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "9391b52c-30c9-4bb7-a1e5-d3ed8922ab3e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019eQkAQas5zQDGHXaLaMQEa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5986,
      "cache_read_input_tokens": 43484,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5986
      },
      "output_tokens": 37,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BWk3KQHzp9Lr6GqVz34Jd5`</summary>

```json
{
  "query": "CAPSTONE code pre-trained model prompt-tuning structure-aware 2023 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "65ff2772-5acb-4cb0-bbfe-9959a42a80a3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019eQkAQas5zQDGHXaLaMQEa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5986,
      "cache_read_input_tokens": 43484,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5986
      },
      "output_tokens": 37,
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

_source line 41_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014HNozGheSc4nS3KmygYXe6`</summary>

```json
{
  "query": "SynCoBERT authors full list Xin Wang arXiv 2108.04556"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "ce38a42b-6767-4a45-add9-f5909483954b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019eQkAQas5zQDGHXaLaMQEa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5986,
      "cache_read_input_tokens": 43484,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5986
      },
      "output_tokens": 37,
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

_source line 42 · 2026-05-15T05:11:55.258Z_

<details><summary>↩ Tool result · `toolu_014HNozGheSc4nS3KmygYXe6`</summary>

```text
Web search results for query: "SynCoBERT authors full list Xin Wang arXiv 2108.04556"

Links: [{"title":"[2108.04556] SynCoBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation","url":"https://arxiv.org/abs/2108.04556"},{"title":"[2108.04556] SynCoBERT: Syntax-Enhanced Contrastive Pre-Training for Code Representation","url":"https://ar5iv.labs.arxiv.org/html/2108.04556"},{"title":"[2108.04556v3] SynCoBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation","url":"https://arxiv.org/abs/2108.04556v3"},{"title":"arXiv:2108.04556v3 [cs.CL] 9 Sep 2021","url":"https://arxiv.org/pdf/2108.04556"},{"title":"[PDF] SynCoBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/SynCoBERT:-Syntax-Guided-Multi-Modal-Contrastive-Wang-Wang/14b104d1a1c0b784e4e74454d809455cc47d0093"},{"title":"Yao Wan@Huazhong University of Science and Technology","url":"http://wanyao.me/publication.html"},{"title":"Xin Wang's articles on arXiv","url":"https://arxiv.org/a/wang_x_10.html"},{"title":"SynCoBERT - Dataset - LDM","url":"https://service.tib.eu/ldmservice/dataset/syncobert"},{"title":"SynCoBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation - ADS","url":"https://ui.adsabs.harvard.edu/abs/2021arXiv210804556W/abstract"},{"title":"Xing Wang","url":"https://scholar.google.com/citations?user=6AqRKa0AAAAJ&hl=en"}]

Based on the search results, the full list of authors for SynCoBERT (arXiv 2108.04556) is: Xin Wang, Yasheng Wang, Fei Mi, Pingyi Zhou, Yao Wan, Xiao Liu, Li Li, Hao Wu, Jin Liu, and Xin Jiang.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "c9b74d63-bd89-491e-ac75-b70440296ddf",
  "tool_use_result": {
    "query": "SynCoBERT authors full list Xin Wang arXiv 2108.04556",
    "results": [
      {
        "tool_use_id": "srvtoolu_016oszW8bss7tj8NJHHpzik1",
        "content": [
          {
            "title": "[2108.04556] SynCoBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation",
            "url": "https://arxiv.org/abs/2108.04556"
          },
          {
            "title": "[2108.04556] SynCoBERT: Syntax-Enhanced Contrastive Pre-Training for Code Representation",
            "url": "https://ar5iv.labs.arxiv.org/html/2108.04556"
          },
          {
            "title": "[2108.04556v3] SynCoBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation",
            "url": "https://arxiv.org/abs/2108.04556v3"
          },
          {
            "title": "arXiv:2108.04556v3 [cs.CL] 9 Sep 2021",
            "url": "https://arxiv.org/pdf/2108.04556"
          },
          {
            "title": "[PDF] SynCoBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/SynCoBERT:-Syntax-Guided-Multi-Modal-Contrastive-Wang-Wang/14b104d1a1c0b784e4e74454d809455cc47d0093"
          },
          {
            "title": "Yao Wan@Huazhong University of Science and Technology",
            "url": "http://wanyao.me/publication.html"
          },
          {
            "title": "Xin Wang's articles on arXiv",
            "url": "https://arxiv.org/a/wang_x_10.html"
          },
          {
            "title": "SynCoBERT - Dataset - LDM",
            "url": "https://service.tib.eu/ldmservice/dataset/syncobert"
          },
          {
            "title": "SynCoBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2021arXiv210804556W/abstract"
          },
          {
            "title": "Xing Wang",
            "url": "https://scholar.google.com/citations?user=6AqRKa0AAAAJ&hl=en"
          }
        ]
      },
      "Based on the search results, the full list of authors for SynCoBERT (arXiv 2108.04556) is: Xin Wang, Yasheng Wang, Fei Mi, Pingyi Zhou, Yao Wan, Xiao Liu, Li Li, Hao Wu, Jin Liu, and Xin Jiang."
    ],
    "durationSeconds": 3.4300879580000037
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-15T05:11:58.392Z_

<details><summary>↩ Tool result · `toolu_01BWk3KQHzp9Lr6GqVz34Jd5`</summary>

```text
Web search results for query: "CAPSTONE code pre-trained model prompt-tuning structure-aware 2023 arxiv"

Links: [{"title":"Structure-aware Fine-tuning for Code Pre-trained Models","url":"https://arxiv.org/html/2404.07471v1"},{"title":"Visual Instance-aware Prompt Tuning","url":"https://arxiv.org/html/2507.07796v1"},{"title":"Revisiting the Power of Prompt for Visual Tuning","url":"https://arxiv.org/html/2402.02382v3"},{"title":"Embedded Prompt Tuning: Towards Enhanced Calibration of Pretrained Models for Medical Images","url":"https://arxiv.org/html/2407.01003v4"},{"title":"CGP-Tuning: Structure-Aware Soft Prompt Tuning for Code Vulnerability Detection","url":"https://arxiv.org/html/2501.04510v1"},{"title":"[2306.15706] Approximated Prompt Tuning for Vision-Language Pre-trained Models","url":"https://arxiv.org/abs/2306.15706"},{"title":"A Survey on Prompt Tuning","url":"https://arxiv.org/html/2507.06085v2"},{"title":"PSP: Pre-Training and Structure Prompt Tuning for Graph Neural Networks","url":"https://arxiv.org/html/2310.17394"},{"title":"Structure Pretraining and Prompt Tuning for Knowledge Graph Transfer Wen Zhang∗","url":"https://arxiv.org/pdf/2303.03922"},{"title":"A Systematic Survey of Prompt Engineering in Large Language Models: Techniques and Applications","url":"https://arxiv.org/html/2402.07927v2"}]

Based on the search results, I found several relevant papers related to your query, though the specific "CAPSTONE" model doesn't appear in these results. Here are the most relevant findings:

## Structure-Aware Prompt Tuning for Code

SAT is a structure-aware fine-tuning method for CodePTMs (Code Pre-trained Models). The method parses code into an abstract syntax tree (AST) and constructs a distance matrix by calculating the shortest path between two leaves in AST, then extracts the attention matrix from the Transformer layer of CodePTMs, and introduces the Sinkhorn divergence to compute the difference between the two matrices as a new objective function, namely structure loss.

SAT is a novel multi-task learning method that enhances the absorption of structural knowledge for CodePTMs during the fine-tuning stage, and is the first structure-aware fine-tuning method for CodePTMs.

## Related Work: Graph-based Structure-Aware Prompt Tuning

Another relevant paper is CGP-Tuning, which introduces two trainable, type-aware embeddings to enable the model to capture the rich semantic information of node types and edge types within the code property graph.

If you're looking for a specific paper titled "CAPSTONE" from 2023, it may not have been indexed in these search results. You might want to try searching directly on arXiv or providing additional details about the paper's authors or full title.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "6de6e74b-d7f7-422e-9692-cd36c5015b56",
  "tool_use_result": {
    "query": "CAPSTONE code pre-trained model prompt-tuning structure-aware 2023 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WPjB2N9nNyL9HoCf3GMcac",
        "content": [
          {
            "title": "Structure-aware Fine-tuning for Code Pre-trained Models",
            "url": "https://arxiv.org/html/2404.07471v1"
          },
          {
            "title": "Visual Instance-aware Prompt Tuning",
            "url": "https://arxiv.org/html/2507.07796v1"
          },
          {
            "title": "Revisiting the Power of Prompt for Visual Tuning",
            "url": "https://arxiv.org/html/2402.02382v3"
          },
          {
            "title": "Embedded Prompt Tuning: Towards Enhanced Calibration of Pretrained Models for Medical Images",
            "url": "https://arxiv.org/html/2407.01003v4"
          },
          {
            "title": "CGP-Tuning: Structure-Aware Soft Prompt Tuning for Code Vulnerability Detection",
            "url": "https://arxiv.org/html/2501.04510v1"
          },
          {
            "title": "[2306.15706] Approximated Prompt Tuning for Vision-Language Pre-trained Models",
            "url": "https://arxiv.org/abs/2306.15706"
          },
          {
            "title": "A Survey on Prompt Tuning",
            "url": "https://arxiv.org/html/2507.06085v2"
          },
          {
            "title": "PSP: Pre-Training and Structure Prompt Tuning for Graph Neural Networks",
            "url": "https://arxiv.org/html/2310.17394"
          },
          {
            "title": "Structure Pretraining and Prompt Tuning for Knowledge Graph Transfer Wen Zhang∗",
            "url": "https://arxiv.org/pdf/2303.03922"
          },
          {
            "title": "A Systematic Survey of Prompt Engineering in Large Language Models: Techniques and Applications",
            "url": "https://arxiv.org/html/2402.07927v2"
          }
        ]
      },
      "Based on the search results, I found several relevant papers related to your query, though the specific \"CAPSTONE\" model doesn't appear in these results. Here are the most relevant findings:\n\n## Structure-Aware Prompt Tuning for Code\n\nSAT is a structure-aware fine-tuning method for CodePTMs (Code Pre-trained Models). The method parses code into an abstract syntax tree (AST) and constructs a distance matrix by calculating the shortest path between two leaves in AST, then extracts the attention matrix from the Transformer layer of CodePTMs, and introduces the Sinkhorn divergence to compute the difference between the two matrices as a new objective function, namely structure loss.\n\nSAT is a novel multi-task learning method that enhances the absorption of structural knowledge for CodePTMs during the fine-tuning stage, and is the first structure-aware fine-tuning method for CodePTMs.\n\n## Related Work: Graph-based Structure-Aware Prompt Tuning\n\nAnother relevant paper is CGP-Tuning, which introduces two trainable, type-aware embeddings to enable the model to capture the rich semantic information of node types and edge types within the code property graph.\n\nIf you're looking for a specific paper titled \"CAPSTONE\" from 2023, it may not have been indexed in these search results. You might want to try searching directly on arXiv or providing additional details about the paper's authors or full title."
    ],
    "durationSeconds": 6.9432920059999885
  }
}
```

</details>

---

### Assistant

_source line 44_

<details><summary>Logged reasoning block</summary>

```text
Let me try one more search for CAPSTONE code representation. Maybe it's "CodeSage" or maybe I'm confusing it with something else.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "19f2c788-9ad2-4265-ab82-99a5295dea61",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X6Udk6ypU5cTKXCQViv3S2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 691,
      "cache_creation_input_tokens": 979,
      "cache_read_input_tokens": 49470,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 979
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

_source line 45_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Goa5m7oFagkCSDLpR1uYeb`</summary>

```json
{
  "query": "\"CAPSTONE\" contrastive learning code representation 2023 paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "779284a6-3655-4870-857f-e3f466c42deb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X6Udk6ypU5cTKXCQViv3S2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 691,
      "cache_creation_input_tokens": 979,
      "cache_read_input_tokens": 49470,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 979
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

_source line 46 · 2026-05-15T05:12:11.699Z_

<details><summary>↩ Tool result · `toolu_01Goa5m7oFagkCSDLpR1uYeb`</summary>

```text
Web search results for query: ""CAPSTONE" contrastive learning code representation 2023 paper"

Links: [{"title":"GitHub - ContrastiveSR/Contrastive_Learning_Papers: A list of contrastive Learning papers · GitHub","url":"https://github.com/ContrastiveSR/Contrastive_Learning_Papers"},{"title":"Contrastive Learning","url":"https://paperswithcode.com/task/contrastive-learning"},{"title":"GitHub - davidtellez/contrastive-predictive-coding: Keras implementation of Representation Learning with Contrastive Predictive Coding · GitHub","url":"https://github.com/davidtellez/contrastive-predictive-coding"},{"title":"Contrastive Code Representation Learning | OpenReview","url":"https://openreview.net/forum?id=uV7hcsjqM-"},{"title":"Contrastive Representation Learning | Lil'Log","url":"https://lilianweng.github.io/posts/2021-05-31-contrastive/"},{"title":"[1807.03748] Representation Learning with Contrastive Predictive Coding","url":"https://arxiv.org/abs/1807.03748"},{"title":"Papers with Code - Contrastive Learning","url":"https://paperswithcode.com/task/contrastive-learning/codeless"},{"title":"GitHub - ryanzhumich/Contrastive-Learning-NLP-Papers: Paper List for Contrastive Learning for Natural Language Processing · GitHub","url":"https://github.com/ryanzhumich/Contrastive-Learning-NLP-Papers"},{"title":"Contrastive Code Representation Learning - Paper Detail","url":"https://deeplearn.org/arxiv/144169/contrastive-code-representation-learning"},{"title":"Contrastive Code Representation Learning","url":"https://parasj.github.io/contracode/"}]

I found information about contrastive learning for code representation, but the results primarily show "ContraCode" (a 2020 paper), not "CAPSTONE" from 2023. Let me search more specifically for CAPSTONE.

Links: [{"title":"Capstone Projects 2023 – Natural Language Processing","url":"https://nlp.ucsc.edu/capstone-projects/capstone-projects-2023/"},{"title":"capstone-project · GitHub Topics · GitHub","url":"https://github.com/topics/capstone-project"},{"title":"GitHub - uoa-compsci399-s2-2023/capstone-project-team-34-code-critters: Code Critters: An ML Insect identification Platform","url":"https://github.com/uoa-compsci399-s2-2023/capstone-project-team-34-code-critters"},{"title":"2023-2024 Capstone Projects – College of Science and Engineering","url":"https://cse.aua.am/2023-2024-capstone-projects/"},{"title":"Issues · Capstone-Projects-2023-Fall/project-code-review-chatbot","url":"https://github.com/Capstone-Projects-2023-Fall/project-code-review-chatbot/issues"},{"title":"AI Capstone Project with Deep Learning | Coursera","url":"https://www.coursera.org/learn/ai-deep-learning-capstone"},{"title":"A Complete Reinforcement Learning System (Capstone) | Coursera","url":"https://www.coursera.org/learn/complete-reinforcement-learning-system"},{"title":"Capstone: Retrieving, Processing, and Visualizing Data with Python | Michigan Online","url":"https://online.umich.edu/courses/capstone-retrieving-processing-and-visualizing-data-with-python/"},{"title":"machine-learning-capstone-project/final-report.pdf at master · flaviohenriquecbc/machine-learning-capstone-project","url":"https://github.com/flaviohenriquecbc/machine-learning-capstone-project/blob/master/final-report.pdf"},{"title":"Why and How to Use Capstone Projects in Machine Learning (ML)","url":"https://talentsprint.com/blog/why-and-how-to-use-capstone-projects-in-machine-learning"}]

The results are showing general capstone projects, not a specific research paper. Let me search more directly for the CAPSTONE paper with different keywords.

Links: [{"title":"[2302.13863] Capstone: A Capability-based Foundation for Trustless Secure Memory Access (Extended Version)","url":"https://arxiv.org/abs/2302.13863"},{"title":"[2302.13863v1] Capstone: A Capability-based Foundation for Trustless Secure Memory Access (Extended Version)","url":"https://arxiv.org/abs/2302.13863v1"},{"title":"[2212.09114] CAPSTONE: Curriculum Sampling for Dense Retrieval with Document Expansion","url":"https://arxiv.org/abs/2212.09114"},{"title":"[2302.13863] Capstone: A Capability-based Foundation for Trustless Secure Memory Access (Extended Version)","url":"https://arxiv-export3.library.cornell.edu/abs/2302.13863"},{"title":"[2410.12114] A Software Engineering Capstone Course Facilitated By GitHub Templates","url":"https://arxiv.org/abs/2410.12114"},{"title":"[2303.07104] xASTNN: Improved Code Representations for Industrial Practice","url":"https://arxiv.org/abs/2303.07104"},{"title":"GitHub - sandipanbasu/aiml-capstone-mrc: AI ML Capstone Project on Machine Reading Comprehension SQuAD · GitHub","url":"https://github.com/sandipanbasu/aiml-capstone-mrc"},{"title":"Capstone: Power-Capped Pipelining for Coarse-Grained Reconfigurable Array Compilers","url":"https://arxiv.org/html/2603.00909v1"},{"title":"2023-2024 Capstone Projects – College of Science and Engineering","url":"https://cse.aua.am/2023-2024-capstone-projects/"},{"title":"[2301.03554] A systematic literature review of capstone courses in software engineering","url":"https://arxiv.org/abs/2301.03554"}]

Based on my web search, I was unable to find a specific research paper titled "CAPSTONE" about contrastive learning for code representation from 2023. 

The search results returned several papers with "Capstone" in the title from 2023, but they address different topics:
- One about capability-based memory isolation architecture
- One about curriculum sampling for dense retrieval
- One about code representations using AST-based neural networks

Additionally, my earlier search found "ContraCode," which is a 2020 paper on contrastive code representation learning, but that predates 2023.

It's possible that:
1. The paper title might be slightly different than "CAPSTONE"
2. The paper may be published under a different venue or may not yet be widely indexed
3. It could be an acronym where the full title is different

If you have more specific information about the paper (such as the authors' names, the conference/venue where it was published, or the exact full title), I could perform a more targeted search to locate it.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "5c6b7524-4353-4452-b945-5c7cc367b193",
  "tool_use_result": {
    "query": "\"CAPSTONE\" contrastive learning code representation 2023 paper",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XZrYyfWBYx3ANQ1rkMmsqX",
        "content": [
          {
            "title": "GitHub - ContrastiveSR/Contrastive_Learning_Papers: A list of contrastive Learning papers · GitHub",
            "url": "https://github.com/ContrastiveSR/Contrastive_Learning_Papers"
          },
          {
            "title": "Contrastive Learning",
            "url": "https://paperswithcode.com/task/contrastive-learning"
          },
          {
            "title": "GitHub - davidtellez/contrastive-predictive-coding: Keras implementation of Representation Learning with Contrastive Predictive Coding · GitHub",
            "url": "https://github.com/davidtellez/contrastive-predictive-coding"
          },
          {
            "title": "Contrastive Code Representation Learning | OpenReview",
            "url": "https://openreview.net/forum?id=uV7hcsjqM-"
          },
          {
            "title": "Contrastive Representation Learning | Lil'Log",
            "url": "https://lilianweng.github.io/posts/2021-05-31-contrastive/"
          },
          {
            "title": "[1807.03748] Representation Learning with Contrastive Predictive Coding",
            "url": "https://arxiv.org/abs/1807.03748"
          },
          {
            "title": "Papers with Code - Contrastive Learning",
            "url": "https://paperswithcode.com/task/contrastive-learning/codeless"
          },
          {
            "title": "GitHub - ryanzhumich/Contrastive-Learning-NLP-Papers: Paper List for Contrastive Learning for Natural Language Processing · GitHub",
            "url": "https://github.com/ryanzhumich/Contrastive-Learning-NLP-Papers"
          },
          {
            "title": "Contrastive Code Representation Learning - Paper Detail",
            "url": "https://deeplearn.org/arxiv/144169/contrastive-code-representation-learning"
          },
          {
            "title": "Contrastive Code Representation Learning",
            "url": "https://parasj.github.io/contracode/"
          }
        ]
      },
      "I found information about contrastive learning for code representation, but the results primarily show \"ContraCode\" (a 2020 paper), not \"CAPSTONE\" from 2023. Let me search more specifically for CAPSTONE.",
      {
        "tool_use_id": "srvtoolu_01BbxeMD3n2t5YgJnvz1dg23",
        "content": [
          {
            "title": "Capstone Projects 2023 – Natural Language Processing",
            "url": "https://nlp.ucsc.edu/capstone-projects/capstone-projects-2023/"
          },
          {
            "title": "capstone-project · GitHub Topics · GitHub",
            "url": "https://github.com/topics/capstone-project"
          },
          {
            "title": "GitHub - uoa-compsci399-s2-2023/capstone-project-team-34-code-critters: Code Critters: An ML Insect identification Platform",
            "url": "https://github.com/uoa-compsci399-s2-2023/capstone-project-team-34-code-critters"
          },
          {
            "title": "2023-2024 Capstone Projects – College of Science and Engineering",
            "url": "https://cse.aua.am/2023-2024-capstone-projects/"
          },
          {
            "title": "Issues · Capstone-Projects-2023-Fall/project-code-review-chatbot",
            "url": "https://github.com/Capstone-Projects-2023-Fall/project-code-review-chatbot/issues"
          },
          {
            "title": "AI Capstone Project with Deep Learning | Coursera",
            "url": "https://www.coursera.org/learn/ai-deep-learning-capstone"
          },
          {
            "title": "A Complete Reinforcement Learning System (Capstone) | Coursera",
            "url": "https://www.coursera.org/learn/complete-reinforcement-learning-system"
          },
          {
            "title": "Capstone: Retrieving, Processing, and Visualizing Data with Python | Michigan Online",
            "url": "https://online.umich.edu/courses/capstone-retrieving-processing-and-visualizing-data-with-python/"
          },
          {
            "title": "machine-learning-capstone-project/final-report.pdf at master · flaviohenriquecbc/machine-learning-capstone-project",
            "url": "https://github.com/flaviohenriquecbc/machine-learning-capstone-project/blob/master/final-report.pdf"
          },
          {
            "title": "Why and How to Use Capstone Projects in Machine Learning (ML)",
            "url": "https://talentsprint.com/blog/why-and-how-to-use-capstone-projects-in-machine-learning"
          }
        ]
      },
      "The results are showing general capstone projects, not a specific research paper. Let me search more directly for the CAPSTONE paper with different keywords.",
      {
        "tool_use_id": "srvtoolu_01Urv3RZixaWNavBVhoitd5t",
        "content": [
          {
            "title": "[2302.13863] Capstone: A Capability-based Foundation for Trustless Secure Memory Access (Extended Version)",
            "url": "https://arxiv.org/abs/2302.13863"
          },
          {
            "title": "[2302.13863v1] Capstone: A Capability-based Foundation for Trustless Secure Memory Access (Extended Version)",
            "url": "https://arxiv.org/abs/2302.13863v1"
          },
          {
            "title": "[2212.09114] CAPSTONE: Curriculum Sampling for Dense Retrieval with Document Expansion",
            "url": "https://arxiv.org/abs/2212.09114"
          },
          {
            "title": "[2302.13863] Capstone: A Capability-based Foundation for Trustless Secure Memory Access (Extended Version)",
            "url": "https://arxiv-export3.library.cornell.edu/abs/2302.13863"
          },
          {
            "title": "[2410.12114] A Software Engineering Capstone Course Facilitated By GitHub Templates",
            "url": "https://arxiv.org/abs/2410.12114"
          },
          {
            "title": "[2303.07104] xASTNN: Improved Code Representations for Industrial Practice",
            "url": "https://arxiv.org/abs/2303.07104"
          },
          {
            "title": "GitHub - sandipanbasu/aiml-capstone-mrc: AI ML Capstone Project on Machine Reading Comprehension SQuAD · GitHub",
            "url": "https://github.com/sandipanbasu/aiml-capstone-mrc"
          },
          {
            "title": "Capstone: Power-Capped Pipelining for Coarse-Grained Reconfigurable Array Compilers",
            "url": "https://arxiv.org/html/2603.00909v1"
          },
          {
            "title": "2023-2024 Capstone Projects – College of Science and Engineering",
            "url": "https://cse.aua.am/2023-2024-capstone-projects/"
          },
          {
            "title": "[2301.03554] A systematic literature review of capstone courses in software engineering",
            "url": "https://arxiv.org/abs/2301.03554"
          }
        ]
      },
      "Based on my web search, I was unable to find a specific research paper titled \"CAPSTONE\" about contrastive learning for code representation from 2023. \n\nThe search results returned several papers with \"Capstone\" in the title from 2023, but they address different topics:\n- One about capability-based memory isolation architecture\n- One about curriculum sampling for dense retrieval\n- One about code representations using AST-based neural networks\n\nAdditionally, my earlier search found \"ContraCode,\" which is a 2020 paper on contrastive code representation learning, but that predates 2023.\n\nIt's possible that:\n1. The paper title might be slightly different than \"CAPSTONE\"\n2. The paper may be published under a different venue or may not yet be widely indexed\n3. It could be an acronym where the full title is different\n\nIf you have more specific information about the paper (such as the authors' names, the conference/venue where it was published, or the exact full title), I could perform a more targeted search to locate it."
    ],
    "durationSeconds": 9.967891776999997
  }
}
```

</details>

---

### Assistant

_source line 47_

<details><summary>Logged reasoning block</summary>

```text
Let me try a different approach - searching for CAPSTONE with specific code-related terms.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "8edbe794-2167-4dbf-8253-6cac21d61678",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CTCid36gKxjJNyjpdQZekR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2615,
      "cache_read_input_tokens": 50449,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2615
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

_source line 48_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VJDdgQe8QAsm3Uxc77X2ci`</summary>

```json
{
  "query": "CAPSTONE curriculum sampling dense retrieval document expansion arXiv 2212.09114"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "c150d46e-9344-4746-be1d-d1f788ba2c14",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CTCid36gKxjJNyjpdQZekR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2615,
      "cache_read_input_tokens": 50449,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2615
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

_source line 49_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017umeDp7NXZMkANnff3XMVE`</summary>

```json
{
  "query": "ProGraML ICML 2021 full author list Chris Cummins Zacharias Fisches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "4e74b3a7-d8f4-428f-8da4-8fba2ab40265",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CTCid36gKxjJNyjpdQZekR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2615,
      "cache_read_input_tokens": 50449,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2615
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

_source line 50_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01B9UzeML65b9SxiZqTLSHD2`</summary>

```json
{
  "query": "ContraBERT ICSE 2023 full author list Shangqing Liu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "d09889c7-29d3-4ec5-b3bc-15d5b26bbcbc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CTCid36gKxjJNyjpdQZekR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2615,
      "cache_read_input_tokens": 50449,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2615
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

_source line 51 · 2026-05-15T05:12:19.927Z_

<details><summary>↩ Tool result · `toolu_01B9UzeML65b9SxiZqTLSHD2`</summary>

```text
Web search results for query: "ContraBERT ICSE 2023 full author list Shangqing Liu"

Links: [{"title":"ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning - Singapore Management University","url":"https://smusg.elsevierpure.com/en/publications/contrabert-enhancing-code-pre-trained-models-via-contrastive-lear"},{"title":"[PDF] ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/ContraBERT:-Enhancing-Code-Pre-trained-Models-via-Liu-Wu/f6572fccea70e5023cc38cb33ebd0f520d7b22e2"},{"title":"About me - Shangqing Liu’s Homepage","url":"https://shangqing-liu.github.io/"},{"title":"Publications - Shangqing Liu’s Homepage","url":"https://shangqing-liu.github.io/publications/"},{"title":"Publications - DR. MENG GUOZHU’s HOMEPAGE","url":"https://impillar.github.io/publications/"},{"title":"ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning | Request PDF","url":"https://www.researchgate.net/publication/372385658_ContraBERT_Enhancing_Code_Pre-trained_Models_via_Contrastive_Learning"},{"title":"Publications - Xiaofei Xie’s HOMEPAGE","url":"https://xiaofeixie.bitbucket.io/publications/"},{"title":"GitHub - xinyi-hou/LLM4SE_SLR: Large Language Models for Software Engineering: A Systematic Literature Review · GitHub","url":"https://github.com/xinyi-hou/LLM4SE_SLR"},{"title":"(PDF) ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning","url":"https://www.researchgate.net/publication/367359448_ContraBERT_Enhancing_Code_Pre-trained_Models_via_Contrastive_Learning"},{"title":"shangqing-liu (ShangqingLiu) · GitHub","url":"https://github.com/shangqing-liu"}]

Based on the search results, the full author list for ContraBERT presented at ICSE 2023 is: Shangqing Liu, Bozhi Wu, Xiaofei Xie, Guozhu Meng, and Yang Liu.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "1c03545c-849a-40dd-a096-6df55cf1dc38",
  "tool_use_result": {
    "query": "ContraBERT ICSE 2023 full author list Shangqing Liu",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HD7GLztRD2hS7QTghNKRcN",
        "content": [
          {
            "title": "ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning - Singapore Management University",
            "url": "https://smusg.elsevierpure.com/en/publications/contrabert-enhancing-code-pre-trained-models-via-contrastive-lear"
          },
          {
            "title": "[PDF] ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/ContraBERT:-Enhancing-Code-Pre-trained-Models-via-Liu-Wu/f6572fccea70e5023cc38cb33ebd0f520d7b22e2"
          },
          {
            "title": "About me - Shangqing Liu’s Homepage",
            "url": "https://shangqing-liu.github.io/"
          },
          {
            "title": "Publications - Shangqing Liu’s Homepage",
            "url": "https://shangqing-liu.github.io/publications/"
          },
          {
            "title": "Publications - DR. MENG GUOZHU’s HOMEPAGE",
            "url": "https://impillar.github.io/publications/"
          },
          {
            "title": "ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning | Request PDF",
            "url": "https://www.researchgate.net/publication/372385658_ContraBERT_Enhancing_Code_Pre-trained_Models_via_Contrastive_Learning"
          },
          {
            "title": "Publications - Xiaofei Xie’s HOMEPAGE",
            "url": "https://xiaofeixie.bitbucket.io/publications/"
          },
          {
            "title": "GitHub - xinyi-hou/LLM4SE_SLR: Large Language Models for Software Engineering: A Systematic Literature Review · GitHub",
            "url": "https://github.com/xinyi-hou/LLM4SE_SLR"
          },
          {
            "title": "(PDF) ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning",
            "url": "https://www.researchgate.net/publication/367359448_ContraBERT_Enhancing_Code_Pre-trained_Models_via_Contrastive_Learning"
          },
          {
            "title": "shangqing-liu (ShangqingLiu) · GitHub",
            "url": "https://github.com/shangqing-liu"
          }
        ]
      },
      "Based on the search results, the full author list for ContraBERT presented at ICSE 2023 is: Shangqing Liu, Bozhi Wu, Xiaofei Xie, Guozhu Meng, and Yang Liu."
    ],
    "durationSeconds": 3.4611171849999955
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-15T05:12:21.701Z_

<details><summary>↩ Tool result · `toolu_01VJDdgQe8QAsm3Uxc77X2ci`</summary>

```text
Web search results for query: "CAPSTONE curriculum sampling dense retrieval document expansion arXiv 2212.09114"

Links: [{"title":"[2212.09114] CAPSTONE: Curriculum Sampling for Dense Retrieval with Document Expansion","url":"https://arxiv.org/abs/2212.09114"},{"title":"CAPSTONE: Curriculum Sampling for Dense Retrieval with Document Expansion | OpenReview","url":"https://openreview.net/forum?id=Mefvmgkb9G&noteId=TlRvoprgev"},{"title":"CAPSTONE: Curriculum Sampling for Dense Retrieval with Document Expansion - ACL Anthology","url":"https://aclanthology.org/2023.emnlp-main.651/"},{"title":"Curriculum Sampling for Dense Retrieval with Document Expansion | Request PDF","url":"https://www.researchgate.net/publication/366423521_Curriculum_Sampling_for_Dense_Retrieval_with_Document_Expansion"},{"title":"Computer Science Dec 2022","url":"https://arxiv.org/list/cs/2022-12?skip=3350&show=50"},{"title":"CAPSTONE: Curriculum Sampling for Dense Retrieval with Document Expansion","url":"https://openreview.net/pdf?id=Mefvmgkb9G"},{"title":"Curriculum Sampling for Dense Retrieval with Document ...","url":"https://aclanthology.org/2023.emnlp-main.651.pdf"},{"title":"Curriculum Sampling for Dense Retrieval with Document ...","url":"https://dblp.uni-trier.de/rec/journals/corr/abs-2212-09114.html"},{"title":"Curriculum Sampling for Dense Retrieval with Document ...","url":"https://scholar.xjtlu.edu.cn/en/publications/capstone-curriculum-sampling-for-dense-retrieval-with-document-ex"},{"title":"GitHub - microsoft/SimXNS: SimXNS is a research project for information retrieval. This repo contains official implementations by MSRA NLC team.","url":"https://github.com/microsoft/SimXNS"}]

I found the paper you're searching for! Here's what I can tell you about it:

## CAPSTONE: Curriculum Sampling for Dense Retrieval with Document Expansion

The paper arXiv:2212.09114 was submitted on December 18, 2022 by Xingwei He and 7 other authors.

### Main Contribution

CAPSTONE is a curriculum sampling for dense retrieval with document expansion, to bridge the gap between training and inference for dual-cross-encoder.

### Problem Addressed

The dual-encoder has become the de facto architecture for dense retrieval. Typically, it computes the latent representations of the query and document independently, thus failing to fully capture the interactions between the query and document. During training, it expands the document with a real query, but during inference, it replaces the real query with a generated one. This inconsistency between training and inference causes the dense retrieval model to prioritize query information while disregarding the document when computing the document representation.

### Proposed Solution

The paper proposes a curriculum sampling strategy that utilizes pseudo queries during training and progressively enhances the relevance between generated and real queries.

### Publication

The paper was published in the Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing in 2023. Official code was released on October 29, 2023.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "d5d97cb2-0870-4cc0-aeff-9d18597a874b",
  "tool_use_result": {
    "query": "CAPSTONE curriculum sampling dense retrieval document expansion arXiv 2212.09114",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HbqWgbAd4R94eQLXUMznJN",
        "content": [
          {
            "title": "[2212.09114] CAPSTONE: Curriculum Sampling for Dense Retrieval with Document Expansion",
            "url": "https://arxiv.org/abs/2212.09114"
          },
          {
            "title": "CAPSTONE: Curriculum Sampling for Dense Retrieval with Document Expansion | OpenReview",
            "url": "https://openreview.net/forum?id=Mefvmgkb9G&noteId=TlRvoprgev"
          },
          {
            "title": "CAPSTONE: Curriculum Sampling for Dense Retrieval with Document Expansion - ACL Anthology",
            "url": "https://aclanthology.org/2023.emnlp-main.651/"
          },
          {
            "title": "Curriculum Sampling for Dense Retrieval with Document Expansion | Request PDF",
            "url": "https://www.researchgate.net/publication/366423521_Curriculum_Sampling_for_Dense_Retrieval_with_Document_Expansion"
          },
          {
            "title": "Computer Science Dec 2022",
            "url": "https://arxiv.org/list/cs/2022-12?skip=3350&show=50"
          },
          {
            "title": "CAPSTONE: Curriculum Sampling for Dense Retrieval with Document Expansion",
            "url": "https://openreview.net/pdf?id=Mefvmgkb9G"
          },
          {
            "title": "Curriculum Sampling for Dense Retrieval with Document ...",
            "url": "https://aclanthology.org/2023.emnlp-main.651.pdf"
          },
          {
            "title": "Curriculum Sampling for Dense Retrieval with Document ...",
            "url": "https://dblp.uni-trier.de/rec/journals/corr/abs-2212-09114.html"
          },
          {
            "title": "Curriculum Sampling for Dense Retrieval with Document ...",
            "url": "https://scholar.xjtlu.edu.cn/en/publications/capstone-curriculum-sampling-for-dense-retrieval-with-document-ex"
          },
          {
            "title": "GitHub - microsoft/SimXNS: SimXNS is a research project for information retrieval. This repo contains official implementations by MSRA NLC team.",
            "url": "https://github.com/microsoft/SimXNS"
          }
        ]
      },
      "I found the paper you're searching for! Here's what I can tell you about it:\n\n## CAPSTONE: Curriculum Sampling for Dense Retrieval with Document Expansion\n\nThe paper arXiv:2212.09114 was submitted on December 18, 2022 by Xingwei He and 7 other authors.\n\n### Main Contribution\n\nCAPSTONE is a curriculum sampling for dense retrieval with document expansion, to bridge the gap between training and inference for dual-cross-encoder.\n\n### Problem Addressed\n\nThe dual-encoder has become the de facto architecture for dense retrieval. Typically, it computes the latent representations of the query and document independently, thus failing to fully capture the interactions between the query and document. During training, it expands the document with a real query, but during inference, it replaces the real query with a generated one. This inconsistency between training and inference causes the dense retrieval model to prioritize query information while disregarding the document when computing the document representation.\n\n### Proposed Solution\n\nThe paper proposes a curriculum sampling strategy that utilizes pseudo queries during training and progressively enhances the relevance between generated and real queries.\n\n### Publication\n\nThe paper was published in the Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing in 2023. Official code was released on October 29, 2023."
    ],
    "durationSeconds": 6.745253471000003
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-15T05:12:25.139Z_

<details><summary>↩ Tool result · `toolu_017umeDp7NXZMkANnff3XMVE`</summary>

```text
Web search results for query: "ProGraML ICML 2021 full author list Chris Cummins Zacharias Fisches"

Links: [{"title":"dblp: Chris Cummins","url":"https://dblp.org/pid/24/997.html"},{"title":"[PDF] ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations | Semantic Scholar","url":"https://www.semanticscholar.org/paper/ProGraML:-A-Graph-based-Program-Representation-for-Cummins-Fisches/7843876d45f4c6ac751039b198aade0ee9f94342"},{"title":"dblp: Zacharias V. Fisches","url":"https://dblp.org/pid/226/2595.html"},{"title":"GitHub - ChrisCummins/ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations · GitHub","url":"https://github.com/ChrisCummins/ProGraML"},{"title":"PROGRAML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations - University of Edinburgh Research Explorer","url":"https://www.research.ed.ac.uk/en/publications/programl-a-graph-based-program-representation-for-data-flow-analy"},{"title":"ICML Poster ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations","url":"https://icml.cc/virtual/2021/poster/8885"},{"title":"PROGRAML: A Graph-based Program Representation for Data Flow Analysis","url":"https://chriscummins.cc/pub/2021-icml.pdf"},{"title":"Chris Cummins, Zacharias Fisches, Tal Ben-Nun, Torsten Hoefler, Michael O'Boyle, Hugh Leather · ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations","url":"https://slideslive.com/38958918/programl-a-graphbased-program-representation-for-data-flow-analysis-and-compiler-optimizations"},{"title":"ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations","url":"https://proceedings.mlr.press/v139/cummins21a.html"},{"title":"[PDF] ProGraML: Graph-based Deep Learning for Program Optimization and Analysis | Semantic Scholar","url":"https://www.semanticscholar.org/paper/ProGraML:-Graph-based-Deep-Learning-for-Program-and-Cummins-Fisches/73e8fc4292ecbd271db9c4229c1cc9736b053760"}]

Based on the search results, the full author list for the ProGraML paper presented at ICML 2021 is: Chris Cummins, Zacharias V. Fisches, Tal Ben-Nun, Torsten Hoefler, Michael F P O'Boyle, and Hugh Leather.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "1e4a8571-1078-4215-9cba-21109953fe37",
  "tool_use_result": {
    "query": "ProGraML ICML 2021 full author list Chris Cummins Zacharias Fisches",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Porwuzj75GvPU3BvZKpqeH",
        "content": [
          {
            "title": "dblp: Chris Cummins",
            "url": "https://dblp.org/pid/24/997.html"
          },
          {
            "title": "[PDF] ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/ProGraML:-A-Graph-based-Program-Representation-for-Cummins-Fisches/7843876d45f4c6ac751039b198aade0ee9f94342"
          },
          {
            "title": "dblp: Zacharias V. Fisches",
            "url": "https://dblp.org/pid/226/2595.html"
          },
          {
            "title": "GitHub - ChrisCummins/ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations · GitHub",
            "url": "https://github.com/ChrisCummins/ProGraML"
          },
          {
            "title": "PROGRAML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations - University of Edinburgh Research Explorer",
            "url": "https://www.research.ed.ac.uk/en/publications/programl-a-graph-based-program-representation-for-data-flow-analy"
          },
          {
            "title": "ICML Poster ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations",
            "url": "https://icml.cc/virtual/2021/poster/8885"
          },
          {
            "title": "PROGRAML: A Graph-based Program Representation for Data Flow Analysis",
            "url": "https://chriscummins.cc/pub/2021-icml.pdf"
          },
          {
            "title": "Chris Cummins, Zacharias Fisches, Tal Ben-Nun, Torsten Hoefler, Michael O'Boyle, Hugh Leather · ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations",
            "url": "https://slideslive.com/38958918/programl-a-graphbased-program-representation-for-data-flow-analysis-and-compiler-optimizations"
          },
          {
            "title": "ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations",
            "url": "https://proceedings.mlr.press/v139/cummins21a.html"
          },
          {
            "title": "[PDF] ProGraML: Graph-based Deep Learning for Program Optimization and Analysis | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/ProGraML:-Graph-based-Deep-Learning-for-Program-and-Cummins-Fisches/73e8fc4292ecbd271db9c4229c1cc9736b053760"
          }
        ]
      },
      "Based on the search results, the full author list for the ProGraML paper presented at ICML 2021 is: Chris Cummins, Zacharias V. Fisches, Tal Ben-Nun, Torsten Hoefler, Michael F P O'Boyle, and Hugh Leather."
    ],
    "durationSeconds": 9.285859972000006
  }
}
```

</details>

---

### Assistant

_source line 54_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough information. Let me verify what I have:

1. **ContraBERT** (ICSE 2023): "ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning" by Shangqing Liu, Bozhi Wu, Xiaofei Xie, Guozhu Meng, and Yang Liu. Designs data augmentation operators for PL and NL data, contrastive pre-training to enhance robustness.

2. **ProGraML** (ICML 2021): "ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations" by Chris Cummins, Zacharias V. 

Fisches, Tal Ben-Nun, Torsten Hoefler, Michael F.P. O'Boyle, and Hugh Leather. Language-independent program graph representation capturing control, data, and call relations.

3. **CrossCodeEval** (NeurIPS 2023): "CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion" by Amazon Science team. Benchmark for cross-file code completion in 4 languages.

4. **SynCoBERT** (arXiv 2021): "SynCoBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation" by X

. Multi-modal contrastive pre-training leveraging AST-based objectives.

5. **CAPSTONE** (EMNLP 2023): Dense retrieval work on curriculum sampling for document expansion—not code-specific.

6. **CoSQA** (ACL 2021): A dataset of 20,000+ web queries for code search and question answering tasks.

CAPSTONE fits into the hard negative mining and dense retrieval methodology section, even though it's not code-focused. It's relevant as a curriculum sampling approach for dense retrieval that could inform StructFuse's methodology. Let me track down the complete author lists for CrossCodeEval and CAPSTONE.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "ffa18bfd-34d1-483f-a466-426af06fa815",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015fduNHdpYvd1LbTmYAwpKL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 674,
      "cache_creation_input_tokens": 1883,
      "cache_read_input_tokens": 53064,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1883
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

_source line 55_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MvM8vh3hH5YLpENWrx1vdK`</summary>

```json
{
  "query": "CrossCodeEval NeurIPS 2023 authors Yangruibo Ding full list arXiv 2310.11248"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "dd707e2d-7bba-4061-9c55-9f76a6a2739a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015fduNHdpYvd1LbTmYAwpKL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 674,
      "cache_creation_input_tokens": 1883,
      "cache_read_input_tokens": 53064,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1883
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

_source line 56_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SEzBkvemYdmjoo4x6gveab`</summary>

```json
{
  "query": "CAPSTONE curriculum sampling dense retrieval document expansion EMNLP 2023 authors Xingwei He"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "2b1aee5e-e01f-4827-8293-5909bdbed8f2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015fduNHdpYvd1LbTmYAwpKL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 674,
      "cache_creation_input_tokens": 1883,
      "cache_read_input_tokens": 53064,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1883
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

_source line 57 · 2026-05-15T05:12:48.286Z_

<details><summary>↩ Tool result · `toolu_01MvM8vh3hH5YLpENWrx1vdK`</summary>

```text
Web search results for query: "CrossCodeEval NeurIPS 2023 authors Yangruibo Ding full list arXiv 2310.11248"

Links: [{"title":"[2310.11248] CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion","url":"https://arxiv.org/abs/2310.11248"},{"title":"GitHub - amazon-science/cceval: CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion (NeurIPS 2023)","url":"https://github.com/amazon-science/cceval"},{"title":"cceval/README.md at main · amazon-science/cceval","url":"https://github.com/amazon-science/cceval/blob/main/README.md"},{"title":"cceval/README.md at a11b8a6c71cf1fe99881dd22d14871c6f01bd30f · amazon-science/cceval","url":"https://github.com/amazon-science/cceval/blob/a11b8a6c71cf1fe99881dd22d14871c6f01bd30f/README.md"},{"title":"dblp: CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion.","url":"https://dblp.org/rec/journals/corr/abs-2310-11248.html"},{"title":"NeurIPS Poster CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion","url":"https://nips.cc/virtual/2023/poster/73423"},{"title":"Computer Science Oct 2023","url":"https://arxiv.org/list/cs/2023-10?skip=5150&show=50"},{"title":"Paper page - CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion","url":"https://huggingface.co/papers/2310.11248"},{"title":"CROSSCODEEVAL","url":"https://arxiv.org/pdf/2310.11248"},{"title":"CROSSCODEEVAL: A Diverse and Multilingual","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/920f2dced7d32ab2ba2f1970bc306af6-Paper-Datasets_and_Benchmarks.pdf"}]

Based on the search results, here is the full list of authors for the CrossCodeEval paper (arXiv 2310.11248) that was presented at NeurIPS 2023:

The authors are: Yangruibo Ding, Zijian Wang, Wasi Uddin Ahmad, Hantian Ding, Ming Tan, Nihal Jain, Murali Krishna Ramanathan, Ramesh Nallapati, Parminder Bhatia, Dan Roth, and Bing Xiang.

This paper was published in the NeurIPS 2023 Datasets and Benchmarks track, and CrossCodeEval is built on a diverse set of real-world, open-sourced, permissively-licensed repositories in four popular programming languages: Python, Java, TypeScript, and C#.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "d763b265-faed-4308-9eb2-a8a917c432b0",
  "tool_use_result": {
    "query": "CrossCodeEval NeurIPS 2023 authors Yangruibo Ding full list arXiv 2310.11248",
    "results": [
      {
        "tool_use_id": "srvtoolu_01DDxPAdWF6gZoCS9hNsqPHz",
        "content": [
          {
            "title": "[2310.11248] CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion",
            "url": "https://arxiv.org/abs/2310.11248"
          },
          {
            "title": "GitHub - amazon-science/cceval: CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion (NeurIPS 2023)",
            "url": "https://github.com/amazon-science/cceval"
          },
          {
            "title": "cceval/README.md at main · amazon-science/cceval",
            "url": "https://github.com/amazon-science/cceval/blob/main/README.md"
          },
          {
            "title": "cceval/README.md at a11b8a6c71cf1fe99881dd22d14871c6f01bd30f · amazon-science/cceval",
            "url": "https://github.com/amazon-science/cceval/blob/a11b8a6c71cf1fe99881dd22d14871c6f01bd30f/README.md"
          },
          {
            "title": "dblp: CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion.",
            "url": "https://dblp.org/rec/journals/corr/abs-2310-11248.html"
          },
          {
            "title": "NeurIPS Poster CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion",
            "url": "https://nips.cc/virtual/2023/poster/73423"
          },
          {
            "title": "Computer Science Oct 2023",
            "url": "https://arxiv.org/list/cs/2023-10?skip=5150&show=50"
          },
          {
            "title": "Paper page - CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion",
            "url": "https://huggingface.co/papers/2310.11248"
          },
          {
            "title": "CROSSCODEEVAL",
            "url": "https://arxiv.org/pdf/2310.11248"
          },
          {
            "title": "CROSSCODEEVAL: A Diverse and Multilingual",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2023/file/920f2dced7d32ab2ba2f1970bc306af6-Paper-Datasets_and_Benchmarks.pdf"
          }
        ]
      },
      "Based on the search results, here is the full list of authors for the CrossCodeEval paper (arXiv 2310.11248) that was presented at NeurIPS 2023:\n\nThe authors are: Yangruibo Ding, Zijian Wang, Wasi Uddin Ahmad, Hantian Ding, Ming Tan, Nihal Jain, Murali Krishna Ramanathan, Ramesh Nallapati, Parminder Bhatia, Dan Roth, and Bing Xiang.\n\nThis paper was published in the NeurIPS 2023 Datasets and Benchmarks track, and CrossCodeEval is built on a diverse set of real-world, open-sourced, permissively-licensed repositories in four popular programming languages: Python, Java, TypeScript, and C#."
    ],
    "durationSeconds": 5.7273043590000015
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-15T05:12:49.749Z_

<details><summary>↩ Tool result · `toolu_01SEzBkvemYdmjoo4x6gveab`</summary>

```text
Web search results for query: "CAPSTONE curriculum sampling dense retrieval document expansion EMNLP 2023 authors Xingwei He"

Links: [{"title":"CAPSTONE: Curriculum Sampling for Dense Retrieval with Document Expansion - ACL Anthology","url":"https://aclanthology.org/2023.emnlp-main.651/"},{"title":"[2212.09114] CAPSTONE: Curriculum Sampling for Dense Retrieval with Document Expansion","url":"https://arxiv.org/abs/2212.09114"},{"title":"CAPSTONE: Curriculum Sampling for Dense Retrieval with Document Expansion | OpenReview","url":"https://openreview.net/forum?id=Mefvmgkb9G&noteId=TlRvoprgev"},{"title":"dblp: Anlei Dong","url":"https://dblp.uni-trier.de/pid/28/6385.html"},{"title":"GitHub - microsoft/SimXNS: SimXNS is a research project for information retrieval. This repo contains official implementations by MSRA NLC team.","url":"https://github.com/microsoft/SimXNS"},{"title":"CAPSTONE: Curriculum Sampling for Dense Retrieval with Document Expansion","url":"https://openreview.net/pdf?id=Mefvmgkb9G"},{"title":"Curriculum Sampling for Dense Retrieval with Document ...","url":"https://aclanthology.org/2023.emnlp-main.651.pdf"},{"title":"Paper Digest: EMNLP-2023 Highlights (Full List)","url":"https://www.paperdigest.org/data/emnlp-2023-full.html"},{"title":"dblp: Jian Jiao 0007","url":"https://dblp.org/pid/29/265-7.html"},{"title":"Curriculum Sampling for Dense Retrieval with Document Expansion | Request PDF","url":"https://www.researchgate.net/publication/366423521_Curriculum_Sampling_for_Dense_Retrieval_with_Document_Expansion"}]

I found the paper you're looking for! Here are the search results:

## CAPSTONE: Curriculum Sampling for Dense Retrieval with Document Expansion

The paper "CAPSTONE: Curriculum Sampling for Dense Retrieval with Document Expansion" was authored by Xingwei He, Yeyun Gong, A-Long Jin, Hang Zhang, Anlei Dong, Jian Jiao, Siu Yiu, and Nan Duan at EMNLP 2023.

The paper was published in the Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing, pages 10531–10541, in Singapore.

**Summary of the work:**

The paper addresses the fact that the dual-encoder has become the de facto architecture for dense retrieval, but typically it computes the latent representations of the query and document independently, thus failing to fully capture the interactions between the query and document.

The researchers identified an inconsistency between training and inference: during training, documents are expanded with a real query, but during inference, the real query is replaced with a generated one, which causes the dense retrieval model to prioritize query information while disregarding the document when computing the document representation.

Experimental results on both in-domain and out-of-domain datasets demonstrate that their approach outperforms previous dense retrieval models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "06687349-aba9-45c4-8353-16eab6e31b7e",
  "tool_use_result": {
    "query": "CAPSTONE curriculum sampling dense retrieval document expansion EMNLP 2023 authors Xingwei He",
    "results": [
      {
        "tool_use_id": "srvtoolu_01YMx2cmgKdXUffxd6SK2Y4B",
        "content": [
          {
            "title": "CAPSTONE: Curriculum Sampling for Dense Retrieval with Document Expansion - ACL Anthology",
            "url": "https://aclanthology.org/2023.emnlp-main.651/"
          },
          {
            "title": "[2212.09114] CAPSTONE: Curriculum Sampling for Dense Retrieval with Document Expansion",
            "url": "https://arxiv.org/abs/2212.09114"
          },
          {
            "title": "CAPSTONE: Curriculum Sampling for Dense Retrieval with Document Expansion | OpenReview",
            "url": "https://openreview.net/forum?id=Mefvmgkb9G&noteId=TlRvoprgev"
          },
          {
            "title": "dblp: Anlei Dong",
            "url": "https://dblp.uni-trier.de/pid/28/6385.html"
          },
          {
            "title": "GitHub - microsoft/SimXNS: SimXNS is a research project for information retrieval. This repo contains official implementations by MSRA NLC team.",
            "url": "https://github.com/microsoft/SimXNS"
          },
          {
            "title": "CAPSTONE: Curriculum Sampling for Dense Retrieval with Document Expansion",
            "url": "https://openreview.net/pdf?id=Mefvmgkb9G"
          },
          {
            "title": "Curriculum Sampling for Dense Retrieval with Document ...",
            "url": "https://aclanthology.org/2023.emnlp-main.651.pdf"
          },
          {
            "title": "Paper Digest: EMNLP-2023 Highlights (Full List)",
            "url": "https://www.paperdigest.org/data/emnlp-2023-full.html"
          },
          {
            "title": "dblp: Jian Jiao 0007",
            "url": "https://dblp.org/pid/29/265-7.html"
          },
          {
            "title": "Curriculum Sampling for Dense Retrieval with Document Expansion | Request PDF",
            "url": "https://www.researchgate.net/publication/366423521_Curriculum_Sampling_for_Dense_Retrieval_with_Document_Expansion"
          }
        ]
      },
      "I found the paper you're looking for! Here are the search results:\n\n## CAPSTONE: Curriculum Sampling for Dense Retrieval with Document Expansion\n\nThe paper \"CAPSTONE: Curriculum Sampling for Dense Retrieval with Document Expansion\" was authored by Xingwei He, Yeyun Gong, A-Long Jin, Hang Zhang, Anlei Dong, Jian Jiao, Siu Yiu, and Nan Duan at EMNLP 2023.\n\nThe paper was published in the Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing, pages 10531–10541, in Singapore.\n\n**Summary of the work:**\n\nThe paper addresses the fact that the dual-encoder has become the de facto architecture for dense retrieval, but typically it computes the latent representations of the query and document independently, thus failing to fully capture the interactions between the query and document.\n\nThe researchers identified an inconsistency between training and inference: during training, documents are expanded with a real query, but during inference, the real query is replaced with a generated one, which causes the dense retrieval model to prioritize query information while disregarding the document when computing the document representation.\n\nExperimental results on both in-domain and out-of-domain datasets demonstrate that their approach outperforms previous dense retrieval models."
    ],
    "durationSeconds": 6.848618455000003
  }
}
```

</details>

---

### Assistant

_source line 59_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me also get the CoSQA full author list, and also verify the SynCoBERT publication venue more carefully - was it eventually published at a conference, or just arXiv?

Let me also check the SynCoBERT venue. Looking at the search results earlier, it seems to be published at AAAI 2022 or ACL. Let me check.

Actually, looking back at the search results, I see that SynCoBERT was on arXiv (2108.04556) in 2021. Let me check if it was published at a conference.

Let me also get more detail on CrossCodeEval to make sure the authors are correct.


Now I'm reviewing which papers need to be added to the references. RocketQA is already included, but I need to add ContraBERT, ProGraML, and CrossCodeEval, along with the strongly recommended papers SynCoBERT and CAPSTONE.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "c2c892e7-4b21-4785-9436-db6e3563d221",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X8zKcrWN48Wz3Ji4aHZ21t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3342,
      "cache_read_input_tokens": 54947,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3342
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

_source line 60_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BZxzBbFb2LsuW34uCiKmcE`</summary>

```json
{
  "query": "SynCoBERT published venue conference AAAI 2022 ACL accepted"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "52527c5e-68a8-4644-a492-7ccab907fc17",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X8zKcrWN48Wz3Ji4aHZ21t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3342,
      "cache_read_input_tokens": 54947,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3342
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

_source line 61 · 2026-05-15T05:13:04.962Z_

<details><summary>↩ Tool result · `toolu_01BZxzBbFb2LsuW34uCiKmcE`</summary>

```text
Web search results for query: "SynCoBERT published venue conference AAAI 2022 ACL accepted"

Links: [{"title":"AAAI Conference Proceedings - AAAI","url":"https://aaai.org/aaai-publications/aaai-conference-proceedings/"},{"title":"Yao Wan@Huazhong University of Science and Technology","url":"http://wanyao.me/publication.html"},{"title":"AAAI 2022 Conference - AAAI","url":"https://aaai.org/conference/aaai/aaai-22/"},{"title":"AAAI Conference on Artificial Intelligence - AAAI","url":"https://aaai.org/conference/aaai/"},{"title":"ARTIFICIAL INTELLIGENCE. AAAI CONFERENCE. 36TH 2022, VOLUME 1. (2 PARTS) (AAAI-22) - proceedings.com","url":"https://www.proceedings.com/64787.html"},{"title":"AAAI Conference on Artificial Intelligence - Wikipedia","url":"https://en.wikipedia.org/wiki/AAAI_Conference_on_Artificial_Intelligence"},{"title":"Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/index"},{"title":"AI Conferences & Symposia AAAI Conferences and Symposia -","url":"https://aaai.org/aaai-conferences-and-symposia/"},{"title":"AAAI 2022 - Amazon Science","url":"https://www.amazon.science/conferences-and-events/aaai-2022"},{"title":"Conference List","url":"http://www.conferencelist.info/upcoming.html"}]

Based on the search results, SynCoBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation was published on arXiv in 2021. The search results indicate it was initially posted as a preprint, but do not show that it was published at either AAAI 2022 or ACL. The paper appears to be available on arXiv rather than being accepted to one of those peer-reviewed conference venues.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "0a6ba05e-2b06-4635-b13f-f98e5deefca0",
  "tool_use_result": {
    "query": "SynCoBERT published venue conference AAAI 2022 ACL accepted",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FXf1s5SkReXcrSRUzwxNZy",
        "content": [
          {
            "title": "AAAI Conference Proceedings - AAAI",
            "url": "https://aaai.org/aaai-publications/aaai-conference-proceedings/"
          },
          {
            "title": "Yao Wan@Huazhong University of Science and Technology",
            "url": "http://wanyao.me/publication.html"
          },
          {
            "title": "AAAI 2022 Conference - AAAI",
            "url": "https://aaai.org/conference/aaai/aaai-22/"
          },
          {
            "title": "AAAI Conference on Artificial Intelligence - AAAI",
            "url": "https://aaai.org/conference/aaai/"
          },
          {
            "title": "ARTIFICIAL INTELLIGENCE. AAAI CONFERENCE. 36TH 2022, VOLUME 1. (2 PARTS) (AAAI-22) - proceedings.com",
            "url": "https://www.proceedings.com/64787.html"
          },
          {
            "title": "AAAI Conference on Artificial Intelligence - Wikipedia",
            "url": "https://en.wikipedia.org/wiki/AAAI_Conference_on_Artificial_Intelligence"
          },
          {
            "title": "Proceedings of the AAAI Conference on Artificial Intelligence",
            "url": "https://ojs.aaai.org/index.php/AAAI/index"
          },
          {
            "title": "AI Conferences & Symposia AAAI Conferences and Symposia -",
            "url": "https://aaai.org/aaai-conferences-and-symposia/"
          },
          {
            "title": "AAAI 2022 - Amazon Science",
            "url": "https://www.amazon.science/conferences-and-events/aaai-2022"
          },
          {
            "title": "Conference List",
            "url": "http://www.conferencelist.info/upcoming.html"
          }
        ]
      },
      "Based on the search results, SynCoBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation was published on arXiv in 2021. The search results indicate it was initially posted as a preprint, but do not show that it was published at either AAAI 2022 or ACL. The paper appears to be available on arXiv rather than being accepted to one of those peer-reviewed conference venues."
    ],
    "durationSeconds": 3.567515744000004
  }
}
```

</details>

---

### Assistant

_source line 62_

<details><summary>Logged reasoning block</summary>

```text
Let me check the Yao Wan publication page to see if SynCoBERT was published at a conference.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "987672e9-d797-4a5b-8eeb-e372fbdf0259",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E3TtaTtnhNK2jx5aiV11n7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1106,
      "cache_read_input_tokens": 58289,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1106
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

_source line 63_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WVSbP1ndADrb2ifGPMtSnf`</summary>

```json
{
  "url": "https://arxiv.org/abs/2108.04556",
  "prompt": "What is the full list of authors and is there a note about which conference this paper was published at?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "aa3fa96f-6a65-4a9e-8f25-408c94ec5767",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E3TtaTtnhNK2jx5aiV11n7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1106,
      "cache_read_input_tokens": 58289,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1106
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

_source line 64 · 2026-05-15T05:13:13.241Z_

<details><summary>↩ Tool result · `toolu_01WVSbP1ndADrb2ifGPMtSnf`</summary>

```text
# SynCoBERT Authors and Publication Details

## Full Author List

The paper lists 10 authors:

"Xin Wang, Yasheng Wang, Fei Mi, Pingyi Zhou, Yao Wan, Xiao Liu, Li Li, Hao Wu, Jin Liu, Xin Jiang"

## Conference Publication Note

The webpage does not indicate that this paper was published at a specific conference. The document shows it as an arXiv preprint (arXiv:2108.04556) submitted on August 10, 2021, with revisions through September 9, 2021. There is no mention of a conference venue, proceedings, or journal publication in the provided content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "c93a1ece-ab85-4770-86e1-09d4342b007a",
  "tool_use_result": {
    "bytes": 49354,
    "code": 200,
    "codeText": "OK",
    "result": "# SynCoBERT Authors and Publication Details\n\n## Full Author List\n\nThe paper lists 10 authors:\n\n\"Xin Wang, Yasheng Wang, Fei Mi, Pingyi Zhou, Yao Wan, Xiao Liu, Li Li, Hao Wu, Jin Liu, Xin Jiang\"\n\n## Conference Publication Note\n\nThe webpage does not indicate that this paper was published at a specific conference. The document shows it as an arXiv preprint (arXiv:2108.04556) submitted on August 10, 2021, with revisions through September 9, 2021. There is no mention of a conference venue, proceedings, or journal publication in the provided content.",
    "durationMs": 3507,
    "url": "https://arxiv.org/abs/2108.04556"
  }
}
```

</details>

---

### Assistant

_source line 65_

<details><summary>Logged reasoning block</summary>

```text
OK, so SynCoBERT remains an arXiv preprint. Now I have all the information I need to write the supplement. Let me now compose the output.

Summary of papers to add:

1. **ContraBERT** (ICSE 2023) - Shangqing Liu, Bozhi Wu, Xiaofei Xie, Guozhu Meng, Yang Liu. "ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning". Designs data augmentation operators on PL/NL data, contrastive pre-training to enhance robustness.


2. **ProGraML** (ICML 2021) - Chris Cummins, Zacharias V. Fisches, Tal Ben-Nun, Torsten Hoefler, Michael F.P. O'Boyle, Hugh Leather. "ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations". Introduces a language-independent graph representation that captures control flow, data dependencies, and function calls.
3. **CrossCodeEval** (NeurIPS 2023) - Yangruibo Ding, Zijian Wang, Wasi Uddin Ahmad, Hantian Ding, Ming Tan, Nihal Jain, Murali Krishna Ramanathan, Ram...
4. **SynCoBERT** (arXiv 2021) - Xin Wang, Yasheng Wang, Fei Mi, Pingyi Zhou, Yao Wan, Xiao Liu, Li Li, Hao Wu, Jin Liu, Xin Jiang. Combines syntax-aware guidance with multi-modal contrastive learning for code representation pre-training.
5. **CAPSTONE** (EMNLP 2023) - Xingwei He, Yeyun Gong, A-Long Jin, Hang Zhang, Anlei Dong, Jian Jiao, Siu Ming Yiu, Nan Duan. Proposes a curriculum-based sampling approach for improving dense retrieval through document expansion.
6. **CoSQA** (ACL 2021) - Junjie Huang, Duyu Tang, Linjun Shou, Ming Gong, Ke Xu, Daxin Jiang, Ming Zhou, Nan Duan. Introduces a large-scale dataset of 20,000+ web queries paired with code for search and question answering tasks.

Now I'm thinking about how to expand section 2.2 on contrastive learning approaches. I should integrate ContraBERT and SynCoBERT into the existing progression from CodeBERT through UniXcoder. ContraBERT strengthens robustness by combining adversarial augmentation with contrastive objectives, while SynCoBERT leverages syntactic structure from abstract syntax trees to guide the contrastive pre-training process.

For section 2.3 on dense retrieval, I need to add CAPSTONE, which introduces curriculum-based sampling strategies to progressively increase difficulty during training while maintaining consistency between training and inference phases.

Finally, ProGraML provides a graph-based program representation that captures control flow, data dependencies, and call relationships across entire programs, which could strengthen the discussion around code structure understanding.

Now I'm ready to write the supplementary paragraphs and bibliography entries for these six new papers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "921aba7a-5be3-4c4f-aeba-d705cc0f889f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cj5bKdeXZLUEYShZGHLk1n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 315,
      "cache_read_input_tokens": 59395,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 315
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

_source line 66_

所有论文已验证。RocketQA 已存在于现有草稿中。需新增 6 篇：ContraBERT、SynCoBERT、ProGraML、CrossCodeEval、CAPSTONE、CoSQA。现在撰写补充段落和 bib entries。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "0e499574-26c0-403f-9de0-d8013c14ba5f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cj5bKdeXZLUEYShZGHLk1n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 315,
      "cache_read_input_tokens": 59395,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 315
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

_source line 67_

<details open><summary>🔧 Tool call — Write · `toolu_01JtngKiRfbAUjoYsKcC5EJa`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_supplement.md",
  "content": "# Related Work Supplement: Contrastive Learning for Code & Adjacent Areas\n\n> **Purpose**: Supplementary paragraphs and citations to strengthen weak areas in Related Work v1.\n> Six new papers added; RocketQA already cited in v1.\n> Generated: 2026-05-15\n\n---\n\n## Supplement A: Contrastive Learning for Code (insert into Section 2.2, after the ContraCode/CodeRetriever paragraph)\n\nBeyond learning invariance to syntactic variation, contrastive pre-training has been applied to inject structural and robustness priors into code representations. SynCoBERT \\cite{wang2021syncobert} introduces syntax-guided multi-modal contrastive pre-training that aligns code, natural language, and abstract syntax tree (AST) modalities through identifier prediction and AST edge prediction objectives, demonstrating that explicitly encoding syntactic structure during contrastive pre-training improves downstream code intelligence tasks. ContraBERT \\cite{liu2023contrabert} takes a complementary robustness-oriented approach, designing nine data augmentation operators that generate adversarial code and comment variants---including identifier renaming, dead code insertion, and operand swapping---and further trains existing code models with contrastive objectives on these augmented pairs. ContraBERT shows that contrastive pre-training with targeted perturbations substantially improves model robustness against adversarial attacks while maintaining strong performance on standard benchmarks. These methods enrich the positive pair construction space for code contrastive learning, yet they focus on augmenting the pre-training signal rather than improving the selection of negative examples during fine-tuning. StructFuse addresses a complementary dimension: rather than improving how positive pairs are constructed, it improves which negatives the model trains against by grounding negative selection in inter-procedural data-flow structure.\n\n## Supplement B: Hard Negative Mining in Dense Retrieval (insert into Section 2.3, after the CL-DRD sentence)\n\nThe curriculum learning paradigm for negative sampling has been further developed by CAPSTONE \\cite{he2023capstone}, which addresses the training-inference discrepancy in dual-encoder dense retrieval. CAPSTONE expands documents with pseudo-queries during training and employs a curriculum sampling strategy that progressively improves the relevance between generated and real queries, effectively controlling negative difficulty through the query generation quality. This approach achieves strong results on both in-domain and out-of-domain retrieval benchmarks, reinforcing the finding that curriculum-based difficulty scheduling benefits dense retrieval training. While CAPSTONE focuses on bridging the training-inference gap through document expansion, our structure-grounded negatives provide an orthogonal form of curriculum: negatives that are hard because they share data-flow context with the positive, not because of embedding proximity alone.\n\n## Supplement C: Cross-File Code Understanding and Evaluation (insert into Section 2.4, before the closing paragraph, or as a new subsection bridge)\n\nThe importance of cross-file context for code understanding has been empirically validated by dedicated benchmarks. CrossCodeEval \\cite{ding2023crosscodeeval} constructs a diverse, multilingual benchmark for cross-file code completion across Python, Java, TypeScript, and C\\#, using static analysis to identify completion targets that strictly require cross-file dependencies. Experiments show that even state-of-the-art code LLMs struggle without cross-file context, and that retrieval-augmented approaches yield clear improvements---yet performance remains far below the ceiling, indicating substantial room for better cross-file retrieval. ProGraML \\cite{cummins2021programl} provides a language-independent, graph-based program representation that captures control-flow, data-flow, and call relations across entire programs, achieving strong results on data-flow analysis tasks. ProGraML demonstrates that whole-program structural representations are learnable and informative, providing conceptual grounding for StructFuse's use of inter-procedural data-flow graphs as a training signal. CoSQA \\cite{huang2021cosqa} contributes a large-scale dataset of 20,000+ real web queries paired with Python code, bridging the gap between synthetic code search benchmarks and real-world developer information needs; it also introduces a contrastive learning method (CoCLR) for data augmentation in code search training. Together, these resources underscore that cross-file structural dependencies and realistic query distributions are critical dimensions for advancing code retrieval---precisely the dimensions that StructFuse's structure-grounded training targets.\n\n---\n\n## Summary of New Citations\n\n| Paper | Venue | Year | Area | Relation to StructFuse |\n|-------|-------|------|------|----------------------|\n| SynCoBERT | arXiv | 2021 | Contrastive code pre-training | Syntax-guided contrastive pre-training; StructFuse uses structure for negatives, not positives |\n| ContraBERT | ICSE | 2023 | Contrastive code pre-training | Robustness-oriented augmentation; complementary to StructFuse's negative mining |\n| CAPSTONE | EMNLP | 2023 | Dense retrieval | Curriculum sampling for retrieval; StructFuse provides structure-based curriculum |\n| CrossCodeEval | NeurIPS | 2023 | Benchmark | Validates importance of cross-file context for code tasks |\n| ProGraML | ICML | 2021 | Program graphs for ML | Whole-program graph representation; conceptual grounding for StructFuse's data-flow use |\n| CoSQA | ACL | 2021 | Code search dataset | Real-world query benchmark with contrastive learning augmentation |\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "c1ebffa0-9d62-496a-88e9-392a7763b5f7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cj5bKdeXZLUEYShZGHLk1n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 315,
      "cache_read_input_tokens": 59395,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 315
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

_source line 68 · 2026-05-15T05:14:04.751Z_

<details><summary>↩ Tool result · `toolu_01JtngKiRfbAUjoYsKcC5EJa`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_supplement.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "24a28bb3-e943-4e8b-a192-1aef3f719279",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_supplement.md",
    "content": "# Related Work Supplement: Contrastive Learning for Code & Adjacent Areas\n\n> **Purpose**: Supplementary paragraphs and citations to strengthen weak areas in Related Work v1.\n> Six new papers added; RocketQA already cited in v1.\n> Generated: 2026-05-15\n\n---\n\n## Supplement A: Contrastive Learning for Code (insert into Section 2.2, after the ContraCode/CodeRetriever paragraph)\n\nBeyond learning invariance to syntactic variation, contrastive pre-training has been applied to inject structural and robustness priors into code representations. SynCoBERT \\cite{wang2021syncobert} introduces syntax-guided multi-modal contrastive pre-training that aligns code, natural language, and abstract syntax tree (AST) modalities through identifier prediction and AST edge prediction objectives, demonstrating that explicitly encoding syntactic structure during contrastive pre-training improves downstream code intelligence tasks. ContraBERT \\cite{liu2023contrabert} takes a complementary robustness-oriented approach, designing nine data augmentation operators that generate adversarial code and comment variants---including identifier renaming, dead code insertion, and operand swapping---and further trains existing code models with contrastive objectives on these augmented pairs. ContraBERT shows that contrastive pre-training with targeted perturbations substantially improves model robustness against adversarial attacks while maintaining strong performance on standard benchmarks. These methods enrich the positive pair construction space for code contrastive learning, yet they focus on augmenting the pre-training signal rather than improving the selection of negative examples during fine-tuning. StructFuse addresses a complementary dimension: rather than improving how positive pairs are constructed, it improves which negatives the model trains against by grounding negative selection in inter-procedural data-flow structure.\n\n## Supplement B: Hard Negative Mining in Dense Retrieval (insert into Section 2.3, after the CL-DRD sentence)\n\nThe curriculum learning paradigm for negative sampling has been further developed by CAPSTONE \\cite{he2023capstone}, which addresses the training-inference discrepancy in dual-encoder dense retrieval. CAPSTONE expands documents with pseudo-queries during training and employs a curriculum sampling strategy that progressively improves the relevance between generated and real queries, effectively controlling negative difficulty through the query generation quality. This approach achieves strong results on both in-domain and out-of-domain retrieval benchmarks, reinforcing the finding that curriculum-based difficulty scheduling benefits dense retrieval training. While CAPSTONE focuses on bridging the training-inference gap through document expansion, our structure-grounded negatives provide an orthogonal form of curriculum: negatives that are hard because they share data-flow context with the positive, not because of embedding proximity alone.\n\n## Supplement C: Cross-File Code Understanding and Evaluation (insert into Section 2.4, before the closing paragraph, or as a new subsection bridge)\n\nThe importance of cross-file context for code understanding has been empirically validated by dedicated benchmarks. CrossCodeEval \\cite{ding2023crosscodeeval} constructs a diverse, multilingual benchmark for cross-file code completion across Python, Java, TypeScript, and C\\#, using static analysis to identify completion targets that strictly require cross-file dependencies. Experiments show that even state-of-the-art code LLMs struggle without cross-file context, and that retrieval-augmented approaches yield clear improvements---yet performance remains far below the ceiling, indicating substantial room for better cross-file retrieval. ProGraML \\cite{cummins2021programl} provides a language-independent, graph-based program representation that captures control-flow, data-flow, and call relations across entire programs, achieving strong results on data-flow analysis tasks. ProGraML demonstrates that whole-program structural representations are learnable and informative, providing conceptual grounding for StructFuse's use of inter-procedural data-flow graphs as a training signal. CoSQA \\cite{huang2021cosqa} contributes a large-scale dataset of 20,000+ real web queries paired with Python code, bridging the gap between synthetic code search benchmarks and real-world developer information needs; it also introduces a contrastive learning method (CoCLR) for data augmentation in code search training. Together, these resources underscore that cross-file structural dependencies and realistic query distributions are critical dimensions for advancing code retrieval---precisely the dimensions that StructFuse's structure-grounded training targets.\n\n---\n\n## Summary of New Citations\n\n| Paper | Venue | Year | Area | Relation to StructFuse |\n|-------|-------|------|------|----------------------|\n| SynCoBERT | arXiv | 2021 | Contrastive code pre-training | Syntax-guided contrastive pre-training; StructFuse uses structure for negatives, not positives |\n| ContraBERT | ICSE | 2023 | Contrastive code pre-training | Robustness-oriented augmentation; complementary to StructFuse's negative mining |\n| CAPSTONE | EMNLP | 2023 | Dense retrieval | Curriculum sampling for retrieval; StructFuse provides structure-based curriculum |\n| CrossCodeEval | NeurIPS | 2023 | Benchmark | Validates importance of cross-file context for code tasks |\n| ProGraML | ICML | 2021 | Program graphs for ML | Whole-program graph representation; conceptual grounding for StructFuse's data-flow use |\n| CoSQA | ACL | 2021 | Code search dataset | Real-world query benchmark with contrastive learning augmentation |\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 69_

Now append the 6 new bib entries to references.bib.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "77d471f5-fa72-496c-95dc-2a754929a342",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ai9YfNFcPusyXSMzX4pWPM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2708,
      "cache_read_input_tokens": 59710,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2708
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

### Tool call

_source line 70_

<details open><summary>🔧 Tool call — Read · `toolu_017gjuzoXR5ZFs7HNU4DefJd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/references.bib",
  "offset": 265
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "71e9529e-62d4-4794-b04c-35c6782dee07",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ai9YfNFcPusyXSMzX4pWPM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2708,
      "cache_read_input_tokens": 59710,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2708
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

### Tool result

_source line 71 · 2026-05-15T05:14:07.999Z_

<details><summary>↩ Tool result · `toolu_017gjuzoXR5ZFs7HNU4DefJd`</summary>

```text
265	  title={{QL}: Object-oriented Queries on Relational Data},
266	  author={Avgustinov, Pavel and de Moor, Oege and Jones, Michael Peyton and Sch{\"a}fer, Max},
267	  booktitle={30th European Conference on Object-Oriented Programming (ECOOP)},
268	  series={LIPIcs},
269	  volume={56},
270	  pages={2:1--2:25},
271	  year={2016}
272	}
273	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "cdd9f259-cbb1-4bf1-bd0c-4237b4007e4d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/references.bib",
      "content": "  title={{QL}: Object-oriented Queries on Relational Data},\n  author={Avgustinov, Pavel and de Moor, Oege and Jones, Michael Peyton and Sch{\\\"a}fer, Max},\n  booktitle={30th European Conference on Object-Oriented Programming (ECOOP)},\n  series={LIPIcs},\n  volume={56},\n  pages={2:1--2:25},\n  year={2016}\n}\n",
      "numLines": 9,
      "startLine": 265,
      "totalLines": 273
    }
  }
}
```

</details>

---

### Tool call

_source line 72_

<details open><summary>🔧 Tool call — Edit · `toolu_01BbgVA7PPuuuZkhemvW3rpM`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/references.bib",
  "old_string": "  year={2016}\n}",
  "new_string": "  year={2016}\n}\n\n% =============================================================================\n% Supplement: New citations added 2026-05-15\n% =============================================================================\n\n@article{wang2021syncobert,\n  title={{SynCoBERT}: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation},\n  author={Wang, Xin and Wang, Yasheng and Mi, Fei and Zhou, Pingyi and Wan, Yao and Liu, Xiao and Li, Li and Wu, Hao and Liu, Jin and Jiang, Xin},\n  journal={arXiv preprint arXiv:2108.04556},\n  year={2021}\n}\n\n@inproceedings{liu2023contrabert,\n  title={{ContraBERT}: Enhancing Code Pre-trained Models via Contrastive Learning},\n  author={Liu, Shangqing and Wu, Bozhi and Xie, Xiaofei and Meng, Guozhu and Liu, Yang},\n  booktitle={Proceedings of the 45th IEEE/ACM International Conference on Software Engineering (ICSE)},\n  pages={2476--2487},\n  year={2023}\n}\n\n@inproceedings{he2023capstone,\n  title={{CAPSTONE}: Curriculum Sampling for Dense Retrieval with Document Expansion},\n  author={He, Xingwei and Gong, Yeyun and Jin, A-Long and Zhang, Hang and Dong, Anlei and Jiao, Jian and Yiu, Siu Ming and Duan, Nan},\n  booktitle={Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages={10531--10541},\n  year={2023}\n}\n\n@inproceedings{ding2023crosscodeeval,\n  title={{CrossCodeEval}: A Diverse and Multilingual Benchmark for Cross-File Code Completion},\n  author={Ding, Yangruibo and Wang, Zijian and Ahmad, Wasi Uddin and Ding, Hantian and Tan, Ming and Jain, Nihal and Ramanathan, Murali Krishna and Nallapati, Ramesh and Bhatia, Parminder and Roth, Dan and Xiang, Bing},\n  booktitle={Advances in Neural Information Processing Systems 36 (NeurIPS)},\n  year={2023}\n}\n\n@inproceedings{cummins2021programl,\n  title={{ProGraML}: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations},\n  author={Cummins, Chris and Fisches, Zacharias V. and Ben-Nun, Tal and Hoefler, Torsten and O'Boyle, Michael F. P. and Leather, Hugh},\n  booktitle={Proceedings of the 38th International Conference on Machine Learning (ICML)},\n  pages={2244--2253},\n  year={2021},\n  publisher={PMLR}\n}\n\n@inproceedings{huang2021cosqa,\n  title={{CoSQA}: 20,000+ Web Queries for Code Search and Question Answering},\n  author={Huang, Junjie and Tang, Duyu and Shou, Linjun and Gong, Ming and Xu, Ke and Jiang, Daxin and Zhou, Ming and Duan, Nan},\n  booktitle={Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  pages={5690--5700},\n  year={2021}\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "91720fd0-675e-45d7-978e-a4ef65c7e5c3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MTU65CeVHz3Hmu1HC3c4DP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 270,
      "cache_read_input_tokens": 62418,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 270
      },
      "output_tokens": 69,
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

_source line 73 · 2026-05-15T05:14:19.764Z_

<details><summary>↩ Tool result · `toolu_01BbgVA7PPuuuZkhemvW3rpM`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "64c6e014-6f8a-4dea-a58d-2a04bff64ced",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/references.bib",
    "oldString": "  year={2016}\n}",
    "newString": "  year={2016}\n}\n\n% =============================================================================\n% Supplement: New citations added 2026-05-15\n% =============================================================================\n\n@article{wang2021syncobert,\n  title={{SynCoBERT}: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation},\n  author={Wang, Xin and Wang, Yasheng and Mi, Fei and Zhou, Pingyi and Wan, Yao and Liu, Xiao and Li, Li and Wu, Hao and Liu, Jin and Jiang, Xin},\n  journal={arXiv preprint arXiv:2108.04556},\n  year={2021}\n}\n\n@inproceedings{liu2023contrabert,\n  title={{ContraBERT}: Enhancing Code Pre-trained Models via Contrastive Learning},\n  author={Liu, Shangqing and Wu, Bozhi and Xie, Xiaofei and Meng, Guozhu and Liu, Yang},\n  booktitle={Proceedings of the 45th IEEE/ACM International Conference on Software Engineering (ICSE)},\n  pages={2476--2487},\n  year={2023}\n}\n\n@inproceedings{he2023capstone,\n  title={{CAPSTONE}: Curriculum Sampling for Dense Retrieval with Document Expansion},\n  author={He, Xingwei and Gong, Yeyun and Jin, A-Long and Zhang, Hang and Dong, Anlei and Jiao, Jian and Yiu, Siu Ming and Duan, Nan},\n  booktitle={Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages={10531--10541},\n  year={2023}\n}\n\n@inproceedings{ding2023crosscodeeval,\n  title={{CrossCodeEval}: A Diverse and Multilingual Benchmark for Cross-File Code Completion},\n  author={Ding, Yangruibo and Wang, Zijian and Ahmad, Wasi Uddin and Ding, Hantian and Tan, Ming and Jain, Nihal and Ramanathan, Murali Krishna and Nallapati, Ramesh and Bhatia, Parminder and Roth, Dan and Xiang, Bing},\n  booktitle={Advances in Neural Information Processing Systems 36 (NeurIPS)},\n  year={2023}\n}\n\n@inproceedings{cummins2021programl,\n  title={{ProGraML}: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations},\n  author={Cummins, Chris and Fisches, Zacharias V. and Ben-Nun, Tal and Hoefler, Torsten and O'Boyle, Michael F. P. and Leather, Hugh},\n  booktitle={Proceedings of the 38th International Conference on Machine Learning (ICML)},\n  pages={2244--2253},\n  year={2021},\n  publisher={PMLR}\n}\n\n@inproceedings{huang2021cosqa,\n  title={{CoSQA}: 20,000+ Web Queries for Code Search and Question Answering},\n  author={Huang, Junjie and Tang, Duyu and Shou, Linjun and Gong, Ming and Xu, Ke and Jiang, Daxin and Zhou, Ming and Duan, Nan},\n  booktitle={Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  pages={5690--5700},\n  year={2021}\n}",
    "originalFile": "% =============================================================================\n% Section 2.1: Code Retrieval Methods\n% =============================================================================\n\n@article{robertson2009bm25,\n  title={The Probabilistic Relevance Framework: {BM25} and Beyond},\n  author={Robertson, Stephen and Zaragoza, Hugo},\n  journal={Foundations and Trends in Information Retrieval},\n  volume={3},\n  number={4},\n  pages={333--389},\n  year={2009},\n  publisher={Now Publishers}\n}\n\n@inproceedings{karpukhin2020dpr,\n  title={Dense Passage Retrieval for Open-Domain Question Answering},\n  author={Karpukhin, Vladimir and O{\\u{g}}uz, Barlas and Min, Sewon and Lewis, Patrick and Wu, Ledell and Edunov, Sergey and Chen, Danqi and Yih, Wen-tau},\n  booktitle={Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages={6769--6781},\n  year={2020}\n}\n\n@article{reddy2025swerank,\n  title={{SweRank}: Software Issue Localization with Code Ranking},\n  author={Gangi Reddy, Revanth and Suresh, Tarun and Doo, JaeHyeok and Liu, Ye and Nguyen, Xuan Phi and Zhou, Yingbo and Yavuz, Semih and Xiong, Caiming and Ji, Heng and Joty, Shafiq},\n  journal={arXiv preprint arXiv:2505.07849},\n  year={2025}\n}\n\n@inproceedings{xie2025swefixer,\n  title={{SWE-Fixer}: Training Open-Source {LLM}s for Effective and Efficient {GitHub} Issue Resolution},\n  author={Xie, Chengxing and Li, Bowen and Gao, Chang and Du, He and Lam, Wai and Zou, Difan and Chen, Kai},\n  booktitle={Findings of the Association for Computational Linguistics: ACL 2025},\n  pages={1123--1139},\n  year={2025}\n}\n\n@inproceedings{chen2025locagent,\n  title={{LocAgent}: Graph-Guided {LLM} Agents for Code Localization},\n  author={Chen, Zhaoling and Tang, Robert and Deng, Gangda and Wu, Fang and Wu, Jialong and Jiang, Zhiwei and Prasanna, Viktor and Cohan, Arman and Wang, Xingyao},\n  booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL)},\n  pages={8697--8727},\n  year={2025}\n}\n\n@article{shah2025ranger,\n  title={{RANGER}: Repository-Level Agent for Graph-Enhanced Retrieval},\n  author={Shah, Pratik and Ghosh, Rajat and Singhal, Aryan and Dutta, Debojyoti},\n  journal={arXiv preprint arXiv:2509.25257},\n  year={2025}\n}\n\n@inproceedings{liu2025codexgraph,\n  title={{CodexGraph}: Bridging Large Language Models and Code Repositories via Code Graph Databases},\n  author={Liu, Xiangyan and Lan, Bo and Hu, Zhiyuan and Liu, Yang and Zhang, Zhicheng and Wang, Fei and Shieh, Michael Qizhe and Zhou, Wenmeng},\n  booktitle={Proceedings of the 2025 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  pages={142--160},\n  year={2025}\n}\n\n@inproceedings{ouyang2025repograph,\n  title={{RepoGraph}: Enhancing {AI} Software Engineering with Repository-level Code Graph},\n  author={Ouyang, Siru and Yu, Wenhao and Ma, Kaixin and Xiao, Zilin and Zhang, Zhihan and Jia, Mengzhao and Han, Jiawei and Zhang, Hongming and Yu, Dong},\n  booktitle={Proceedings of the Thirteenth International Conference on Learning Representations (ICLR)},\n  year={2025}\n}\n\n@inproceedings{liu2024graphcoder,\n  title={{GraphCoder}: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model},\n  author={Liu, Wei and Hu, Ailun and Li, Yixuan and Li, Yichen and Liu, Haoyu and Yang, Leyi},\n  booktitle={Proceedings of the 39th IEEE/ACM International Conference on Automated Software Engineering (ASE)},\n  year={2024}\n}\n\n@article{seddik2026arise,\n  title={{ARISE}: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair},\n  author={Seddik, Shahd and Fard, Fatemeh},\n  journal={arXiv preprint arXiv:2605.03117},\n  year={2026}\n}\n\n% =============================================================================\n% Section 2.2: Pre-trained Code Representations and Contrastive Learning\n% =============================================================================\n\n@inproceedings{feng2020codebert,\n  title={{CodeBERT}: A Pre-Trained Model for Programming and Natural Languages},\n  author={Feng, Zhangyin and Guo, Daya and Tang, Duyu and Duan, Nan and Feng, Xiaocheng and Gong, Ming and Shou, Linjun and Qin, Bing and Liu, Ting and Jiang, Daxin and Zhou, Ming},\n  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2020},\n  pages={1536--1547},\n  year={2020}\n}\n\n@inproceedings{guo2021graphcodebert,\n  title={{GraphCodeBERT}: Pre-training Code Representations with Data Flow},\n  author={Guo, Daya and Ren, Shuo and Lu, Shuai and Feng, Zhangyin and Tang, Duyu and Liu, Shujie and Zhou, Long and Duan, Nan and Svyatkovskiy, Alexey and Fu, Shengyu and Tufano, Michele and Deng, Shuai Kim and Clement, Colin and Drain, Dawn and Sundaresan, Neel and Yin, Jian and Jiang, Daxin and Zhou, Ming},\n  booktitle={Proceedings of the Ninth International Conference on Learning Representations (ICLR)},\n  year={2021}\n}\n\n@inproceedings{guo2022unixcoder,\n  title={{UniXcoder}: Unified Cross-Modal Pre-training for Code Representation},\n  author={Guo, Daya and Lu, Shuai and Duan, Nan and Wang, Yanlin and Zhou, Ming and Yin, Jian},\n  booktitle={Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  pages={7212--7225},\n  year={2022}\n}\n\n@inproceedings{alon2019code2vec,\n  title={code2vec: Learning Distributed Representations of Code},\n  author={Alon, Uri and Zilberstein, Meital and Levy, Omer and Yahav, Eran},\n  booktitle={Proceedings of the ACM on Programming Languages (POPL)},\n  volume={3},\n  pages={1--29},\n  year={2019}\n}\n\n@inproceedings{zhang2024codesage,\n  title={Code Representation Learning At Scale},\n  author={Zhang, Dejiao and Ahmad, Wasi Uddin and Tan, Ming and Ding, Hantian and Nallapati, Ramesh and Roth, Dan and Ma, Xiaofei and Xiang, Bing},\n  booktitle={Proceedings of the Twelfth International Conference on Learning Representations (ICLR)},\n  year={2024}\n}\n\n@inproceedings{reimers2019sentencebert,\n  title={Sentence-{BERT}: Sentence Embeddings using Siamese {BERT}-Networks},\n  author={Reimers, Nils and Gurevych, Iryna},\n  booktitle={Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages={3982--3992},\n  year={2019}\n}\n\n@inproceedings{jain2021contracode,\n  title={Contrastive Code Representation Learning},\n  author={Jain, Paras and Jain, Ajil and Zhang, Tianjun and Abbeel, Pieter and Gonzalez, Joseph and Stoica, Ion},\n  booktitle={Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages={5954--5971},\n  year={2021}\n}\n\n@inproceedings{li2022coderetriever,\n  title={{CodeRetriever}: A Large Scale Contrastive Pre-Training Method for Code Search},\n  author={Li, Xiaonan and Gong, Yeyun and Shen, Yelong and Qiu, Xipeng and Zhang, Hang and Yao, Bolun and Qi, Weizhen and Jiang, Daxin and Chen, Weizhu and Duan, Nan},\n  booktitle={Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages={2898--2910},\n  year={2022}\n}\n\n@inproceedings{li2022scoder,\n  title={Soft-Labeled Contrastive Pre-training for Function-level Code Representation},\n  author={Li, Xiaonan and Guo, Daya and Gong, Yeyun and Lin, Yun and Shen, Yelong and Qiu, Xipeng and Jiang, Daxin and Chen, Weizhu and Duan, Nan},\n  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2022},\n  year={2022}\n}\n\n@inproceedings{ding2022programcontrasts,\n  title={Towards Learning (Dis)-Similarity of Source Code from Program Contrasts},\n  author={Ding, Yangruibo and Buratti, Luca and Pujar, Saurabh and Morari, Alessandro and Ray, Baishakhi and Parthasarathy, Saikat},\n  booktitle={Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  pages={6300--6312},\n  year={2022}\n}\n\n@inproceedings{bui2021infercode,\n  title={{InferCode}: Self-Supervised Learning of Code Representations by Predicting Subtrees},\n  author={Bui, Nghi D. Q. and Yu, Yijun and Jiang, Lingxiao},\n  booktitle={Proceedings of the 43rd IEEE/ACM International Conference on Software Engineering (ICSE)},\n  pages={1186--1197},\n  year={2021}\n}\n\n@article{lozhkov2024starcoder2,\n  title={{StarCoder} 2 and {The Stack} v2: The Next Generation},\n  author={Lozhkov, Anton and Li, Raymond and Ben Allal, Loubna and Cassano, Federico and Lamy-Poirier, Joel and Tazi, Nouamane and Tang, Ao and Pykhtar, Dmytro and Liu, Jiawei and Wei, Yuxiang and others},\n  journal={arXiv preprint arXiv:2402.19173},\n  year={2024}\n}\n\n@article{hui2024qwen25coder,\n  title={{Qwen2.5-Coder} Technical Report},\n  author={Hui, Binyuan and Yang, Jian and Cui, Zeyu and Yang, Jiaxi and Liu, Dayiheng and Zhang, Lei and Liu, Tianyu and Zhang, Jiajun and Yu, Bowen and Lu, Keming and Dang, Kai and Fan, Yang and Zhang, Yichang and Yang, An and Men, Rui and Huang, Fei and Zheng, Bo and others},\n  journal={arXiv preprint arXiv:2409.12186},\n  year={2024}\n}\n\n% =============================================================================\n% Section 2.3: Hard Negative Mining\n% =============================================================================\n\n@inproceedings{chen2020simclr,\n  title={A Simple Framework for Contrastive Learning of Visual Representations},\n  author={Chen, Ting and Kornblith, Simon and Norouzi, Mohammad and Hinton, Geoffrey},\n  booktitle={Proceedings of the 37th International Conference on Machine Learning (ICML)},\n  pages={1597--1607},\n  year={2020}\n}\n\n@inproceedings{xiong2021ance,\n  title={Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval},\n  author={Xiong, Lee and Xiong, Chenyan and Li, Ye and Tang, Kwok-Fung and Liu, Jialin and Bennett, Paul and Ahmed, Junaid and Overwijk, Arnold},\n  booktitle={Proceedings of the Ninth International Conference on Learning Representations (ICLR)},\n  year={2021}\n}\n\n@inproceedings{zhan2021star,\n  title={Optimizing Dense Retrieval Model Training with Hard Negatives},\n  author={Zhan, Jingtao and Mao, Jiaxin and Liu, Yiqun and Guo, Jiafeng and Zhang, Min and Ma, Shaoping},\n  booktitle={Proceedings of the 44th International ACM SIGIR Conference on Research and Development in Information Retrieval},\n  pages={1503--1512},\n  year={2021}\n}\n\n@inproceedings{qu2021rocketqa,\n  title={{RocketQA}: An Optimized Training Approach to Dense Passage Retrieval for Open-Domain Question Answering},\n  author={Qu, Yingqi and Ding, Yuchen and Liu, Jing and Liu, Kai and Ren, Ruiyang and Zhao, Wayne Xin and Dong, Daxiang and Wu, Hua and Wang, Haifeng},\n  booktitle={Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL-HLT)},\n  pages={5835--5847},\n  year={2021}\n}\n\n@inproceedings{zeng2022cldrd,\n  title={Curriculum Learning for Dense Retrieval Distillation},\n  author={Zeng, Hansi and Zamani, Hamed and Vinay, Vishwa},\n  booktitle={Proceedings of the 45th International ACM SIGIR Conference on Research and Development in Information Retrieval},\n  pages={1979--1983},\n  year={2022}\n}\n\n@article{fan2025cocohanere,\n  title={Effective Hard Negative Mining for Contrastive Learning-Based Code Search},\n  author={Fan, Ye and Li, Chuanyi and Ge, Jidong and Huang, LiGuo and Luo, Bin},\n  journal={ACM Transactions on Software Engineering and Methodology},\n  volume={34},\n  number={3},\n  year={2025},\n  publisher={ACM}\n}\n\n% =============================================================================\n% Section 2.4: Code Structure Analysis\n% =============================================================================\n\n@article{ferrante1987pdg,\n  title={The Program Dependence Graph and Its Use in Optimization},\n  author={Ferrante, Jeanne and Ottenstein, Karl J. and Warren, Joe D.},\n  journal={ACM Transactions on Programming Languages and Systems},\n  volume={9},\n  number={3},\n  pages={319--349},\n  year={1987},\n  publisher={ACM}\n}\n\n@inproceedings{yamaguchi2014cpg,\n  title={Modeling and Discovering Vulnerabilities with Code Property Graphs},\n  author={Yamaguchi, Fabian and Golde, Nico and Arp, Daniel and Rieck, Konrad},\n  booktitle={Proceedings of the 2014 IEEE Symposium on Security and Privacy (S\\&P)},\n  pages={590--604},\n  year={2014},\n  publisher={IEEE}\n}\n\n@inproceedings{avgustinov2016ql,\n  title={{QL}: Object-oriented Queries on Relational Data},\n  author={Avgustinov, Pavel and de Moor, Oege and Jones, Michael Peyton and Sch{\\\"a}fer, Max},\n  booktitle={30th European Conference on Object-Oriented Programming (ECOOP)},\n  series={LIPIcs},\n  volume={56},\n  pages={2:1--2:25},\n  year={2016}\n}\n",
    "structuredPatch": [
      {
        "oldStart": 270,
        "oldLines": 3,
        "newStart": 270,
        "newLines": 54,
        "lines": [
          "   pages={2:1--2:25},",
          "   year={2016}",
          " }",
          "+",
          "+% =============================================================================",
          "+% Supplement: New citations added 2026-05-15",
          "+% =============================================================================",
          "+",
          "+@article{wang2021syncobert,",
          "+  title={{SynCoBERT}: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation},",
          "+  author={Wang, Xin and Wang, Yasheng and Mi, Fei and Zhou, Pingyi and Wan, Yao and Liu, Xiao and Li, Li and Wu, Hao and Liu, Jin and Jiang, Xin},",
          "+  journal={arXiv preprint arXiv:2108.04556},",
          "+  year={2021}",
          "+}",
          "+",
          "+@inproceedings{liu2023contrabert,",
          "+  title={{ContraBERT}: Enhancing Code Pre-trained Models via Contrastive Learning},",
          "+  author={Liu, Shangqing and Wu, Bozhi and Xie, Xiaofei and Meng, Guozhu and Liu, Yang},",
          "+  booktitle={Proceedings of the 45th IEEE/ACM International Conference on Software Engineering (ICSE)},",
          "+  pages={2476--2487},",
          "+  year={2023}",
          "+}",
          "+",
          "+@inproceedings{he2023capstone,",
          "+  title={{CAPSTONE}: Curriculum Sampling for Dense Retrieval with Document Expansion},",
          "+  author={He, Xingwei and Gong, Yeyun and Jin, A-Long and Zhang, Hang and Dong, Anlei and Jiao, Jian and Yiu, Siu Ming and Duan, Nan},",
          "+  booktitle={Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},",
          "+  pages={10531--10541},",
          "+  year={2023}",
          "+}",
          "+",
          "+@inproceedings{ding2023crosscodeeval,",
          "+  title={{CrossCodeEval}: A Diverse and Multilingual Benchmark for Cross-File Code Completion},",
          "+  author={Ding, Yangruibo and Wang, Zijian and Ahmad, Wasi Uddin and Ding, Hantian and Tan, Ming and Jain, Nihal and Ramanathan, Murali Krishna and Nallapati, Ramesh and Bhatia, Parminder and Roth, Dan and Xiang, Bing},",
          "+  booktitle={Advances in Neural Information Processing Systems 36 (NeurIPS)},",
          "+  year={2023}",
          "+}",
          "+",
          "+@inproceedings{cummins2021programl,",
          "+  title={{ProGraML}: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations},",
          "+  author={Cummins, Chris and Fisches, Zacharias V. and Ben-Nun, Tal and Hoefler, Torsten and O'Boyle, Michael F. P. and Leather, Hugh},",
          "+  booktitle={Proceedings of the 38th International Conference on Machine Learning (ICML)},",
          "+  pages={2244--2253},",
          "+  year={2021},",
          "+  publisher={PMLR}",
          "+}",
          "+",
          "+@inproceedings{huang2021cosqa,",
          "+  title={{CoSQA}: 20,000+ Web Queries for Code Search and Question Answering},",
          "+  author={Huang, Junjie and Tang, Duyu and Shou, Linjun and Gong, Ming and Xu, Ke and Jiang, Daxin and Zhou, Ming and Duan, Nan},",
          "+  booktitle={Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL)},",
          "+  pages={5690--5700},",
          "+  year={2021}",
          "+}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 74_

注册产出。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "279fd704-750b-4d93-89cb-4963ae1d7192",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NqH74mZ4nkEBMfoK89WFzn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1111,
      "cache_read_input_tokens": 62688,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1111
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

### Tool call

_source line 75_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_017YmPBZS9NBKuxQwFXvShhL`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "8d520b4f-9125-49e4-ab58-612b5df3aac1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NqH74mZ4nkEBMfoK89WFzn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1111,
      "cache_read_input_tokens": 62688,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1111
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

### Tool result

_source line 76 · 2026-05-15T05:14:24.296Z_

<details><summary>↩ Tool result · `toolu_017YmPBZS9NBKuxQwFXvShhL`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "e4451016-9359-4aa9-af29-06485af9e5e7",
  "tool_use_result": {
    "matches": [],
    "query": "select:mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Tool call

_source line 77_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01C8TifLMwfzMri7M43LbHhJ`</summary>

```json
{
  "query": "register artifact",
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
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "6a725fb5-8cec-43ff-869b-19ed2daddd96",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SEY5Guckbk32fVAA9JD98M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 109,
      "cache_read_input_tokens": 63799,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 109
      },
      "output_tokens": 57,
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

_source line 78 · 2026-05-15T05:14:27.195Z_

<details><summary>↩ Tool result · `toolu_01C8TifLMwfzMri7M43LbHhJ`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "e72c6eee-e74a-488f-a852-a8f4a9a344db",
  "tool_use_result": {
    "matches": [],
    "query": "register artifact",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Tool call

_source line 79_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01V7yTAPFr8xgw7Nwy8h3zSZ`</summary>

```json
{
  "query": "register artifact save",
  "max_results": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "5620d40b-ceb0-4088-a6ec-e4f26aff515c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BYpt5uSh5QCi2Jppexe99H",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 194,
      "cache_read_input_tokens": 63908,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 194
      },
      "output_tokens": 58,
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

_source line 80 · 2026-05-15T05:14:29.645Z_

<details><summary>↩ Tool result · `toolu_01V7yTAPFr8xgw7Nwy8h3zSZ`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
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
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "4ab8c176-0887-496d-97c6-aaf5eb85aaf2",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "register artifact save",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 81_

<details><summary>Logged reasoning block</summary>

```text
The `register_artifact` tool doesn't seem to be available as a deferred tool. Let me check what tools are available more broadly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "74029920-fa21-42cc-b318-3211438c2d64",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YSTFbHLqXeXK9XqFa8Vy9Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 350,
      "cache_read_input_tokens": 64102,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 350
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

_source line 82_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01RBhQtvA9mMz5XhHyQphyHu`</summary>

```json
{
  "query": "artifact register log",
  "max_results": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "146f4a53-11e7-42ff-a946-7a92c1248dec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YSTFbHLqXeXK9XqFa8Vy9Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 350,
      "cache_read_input_tokens": 64102,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 350
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

_source line 83 · 2026-05-15T05:14:33.109Z_

<details><summary>↩ Tool result · `toolu_01RBhQtvA9mMz5XhHyQphyHu`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "EnterPlanMode"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "Monitor"
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
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "d70c41bd-389f-44fb-9f98-446a5d6318ea",
  "tool_use_result": {
    "matches": [
      "EnterPlanMode",
      "Monitor"
    ],
    "query": "artifact register log",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 84_

<details><summary>Logged reasoning block</summary>

```text
The `register_artifact` tool is not available. Let me check if there's a different way to register artifacts. Let me search more specifically.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "54c90788-e94a-4274-957d-4945daad20c8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0167HNhhQnpwMm6S8HHZifdJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2972,
      "cache_read_input_tokens": 64452,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2972
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

_source line 85_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01QJzXF74wq5djdSS4sszofg`</summary>

```json
{
  "query": "register artifact project output",
  "max_results": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "cd8a1a07-8ee8-4022-8ad0-fcc9511855b8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0167HNhhQnpwMm6S8HHZifdJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2972,
      "cache_read_input_tokens": 64452,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2972
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

_source line 86 · 2026-05-15T05:14:36.860Z_

<details><summary>↩ Tool result · `toolu_01QJzXF74wq5djdSS4sszofg`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "TaskOutput"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
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
  "tool_name": "TodoWrite"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "EnterWorktree"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "Monitor"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__append_idea"
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
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "5c2dee9f-62a9-4be7-87ff-6d708982f260",
  "tool_use_result": {
    "matches": [
      "TaskOutput",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file",
      "TodoWrite",
      "EnterWorktree",
      "Monitor",
      "mcp__agent-ml-research__append_idea"
    ],
    "query": "register artifact project output",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 87_

<details><summary>Logged reasoning block</summary>

```text
`register_artifact` is not available as a tool. Let me just verify the files are written correctly and report the results. The artifacts are already in the artifacts directory.

Let me verify both files are correct.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "0e40b3df-c872-4b3f-9d80-487e6008d052",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KoNGJo3Fd9V2gq3JJWSzuY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6190,
      "cache_read_input_tokens": 67424,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6190
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

_source line 88_

`register_artifact` 工具不可用，产出文件已直接写入 artifacts 目录。验证文件完整性。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "e6d6a8e7-cc96-4aaf-a884-753f9e31a31d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KoNGJo3Fd9V2gq3JJWSzuY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6190,
      "cache_read_input_tokens": 67424,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6190
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

_source line 89_

<details open><summary>🔧 Tool call — Read · `toolu_01Gpj2RoeSV3TDjciBXQC3Ec`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_supplement.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "97cd6218-3eb6-4ddb-8317-4fb27f0c9c2f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KoNGJo3Fd9V2gq3JJWSzuY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6190,
      "cache_read_input_tokens": 67424,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6190
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

_source line 90 · 2026-05-15T05:14:42.916Z_

<details><summary>↩ Tool result · `toolu_01Gpj2RoeSV3TDjciBXQC3Ec`</summary>

```text
1	# Related Work Supplement: Contrastive Learning for Code & Adjacent Areas
2	
3	> **Purpose**: Supplementary paragraphs and citations to strengthen weak areas in Related Work v1.
4	> Six new papers added; RocketQA already cited in v1.
5	> Generated: 2026-05-15
6	
7	---
8	
9	## Supplement A: Contrastive Learning for Code (insert into Section 2.2, after the ContraCode/CodeRetriever paragraph)
10	
11	Beyond learning invariance to syntactic variation, contrastive pre-training has been applied to inject structural and robustness priors into code representations. SynCoBERT \cite{wang2021syncobert} introduces syntax-guided multi-modal contrastive pre-training that aligns code, natural language, and abstract syntax tree (AST) modalities through identifier prediction and AST edge prediction objectives, demonstrating that explicitly encoding syntactic structure during contrastive pre-training improves downstream code intelligence tasks. ContraBERT \cite{liu2023contrabert} takes a complementary robustness-oriented approach, designing nine data augmentation operators that generate adversarial code and comment variants---including identifier renaming, dead code insertion, and operand swapping---and further trains existing code models with contrastive objectives on these augmented pairs. ContraBERT shows that contrastive pre-training with targeted perturbations substantially improves model robustness against adversarial attacks while maintaining strong performance on standard benchmarks. These methods enrich the positive pair construction space for code contrastive learning, yet they focus on augmenting the pre-training signal rather than improving the selection of negative examples during fine-tuning. StructFuse addresses a complementary dimension: rather than improving how positive pairs are constructed, it improves which negatives the model trains against by grounding negative selection in inter-procedural data-flow structure.
12	
13	## Supplement B: Hard Negative Mining in Dense Retrieval (insert into Section 2.3, after the CL-DRD sentence)
14	
15	The curriculum learning paradigm for negative sampling has been further developed by CAPSTONE \cite{he2023capstone}, which addresses the training-inference discrepancy in dual-encoder dense retrieval. CAPSTONE expands documents with pseudo-queries during training and employs a curriculum sampling strategy that progressively improves the relevance between generated and real queries, effectively controlling negative difficulty through the query generation quality. This approach achieves strong results on both in-domain and out-of-domain retrieval benchmarks, reinforcing the finding that curriculum-based difficulty scheduling benefits dense retrieval training. While CAPSTONE focuses on bridging the training-inference gap through document expansion, our structure-grounded negatives provide an orthogonal form of curriculum: negatives that are hard because they share data-flow context with the positive, not because of embedding proximity alone.
16	
17	## Supplement C: Cross-File Code Understanding and Evaluation (insert into Section 2.4, before the closing paragraph, or as a new subsection bridge)
18	
19	The importance of cross-file context for code understanding has been empirically validated by dedicated benchmarks. CrossCodeEval \cite{ding2023crosscodeeval} constructs a diverse, multilingual benchmark for cross-file code completion across Python, Java, TypeScript, and C\#, using static analysis to identify completion targets that strictly require cross-file dependencies. Experiments show that even state-of-the-art code LLMs struggle without cross-file context, and that retrieval-augmented approaches yield clear improvements---yet performance remains far below the ceiling, indicating substantial room for better cross-file retrieval. ProGraML \cite{cummins2021programl} provides a language-independent, graph-based program representation that captures control-flow, data-flow, and call relations across entire programs, achieving strong results on data-flow analysis tasks. ProGraML demonstrates that whole-program structural representations are learnable and informative, providing conceptual grounding for StructFuse's use of inter-procedural data-flow graphs as a training signal. CoSQA \cite{huang2021cosqa} contributes a large-scale dataset of 20,000+ real web queries paired with Python code, bridging the gap between synthetic code search benchmarks and real-world developer information needs; it also introduces a contrastive learning method (CoCLR) for data augmentation in code search training. Together, these resources underscore that cross-file structural dependencies and realistic query distributions are critical dimensions for advancing code retrieval---precisely the dimensions that StructFuse's structure-grounded training targets.
20	
21	---
22	
23	## Summary of New Citations
24	
25	| Paper | Venue | Year | Area | Relation to StructFuse |
26	|-------|-------|------|------|----------------------|
27	| SynCoBERT | arXiv | 2021 | Contrastive code pre-training | Syntax-guided contrastive pre-training; StructFuse uses structure for negatives, not positives |
28	| ContraBERT | ICSE | 2023 | Contrastive code pre-training | Robustness-oriented augmentation; complementary to StructFuse's negative mining |
29	| CAPSTONE | EMNLP | 2023 | Dense retrieval | Curriculum sampling for retrieval; StructFuse provides structure-based curriculum |
30	| CrossCodeEval | NeurIPS | 2023 | Benchmark | Validates importance of cross-file context for code tasks |
31	| ProGraML | ICML | 2021 | Program graphs for ML | Whole-program graph representation; conceptual grounding for StructFuse's data-flow use |
32	| CoSQA | ACL | 2021 | Code search dataset | Real-world query benchmark with contrastive learning augmentation |
33	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "c29b2251-180c-437e-accd-de09b0784a5a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_supplement.md",
      "content": "# Related Work Supplement: Contrastive Learning for Code & Adjacent Areas\n\n> **Purpose**: Supplementary paragraphs and citations to strengthen weak areas in Related Work v1.\n> Six new papers added; RocketQA already cited in v1.\n> Generated: 2026-05-15\n\n---\n\n## Supplement A: Contrastive Learning for Code (insert into Section 2.2, after the ContraCode/CodeRetriever paragraph)\n\nBeyond learning invariance to syntactic variation, contrastive pre-training has been applied to inject structural and robustness priors into code representations. SynCoBERT \\cite{wang2021syncobert} introduces syntax-guided multi-modal contrastive pre-training that aligns code, natural language, and abstract syntax tree (AST) modalities through identifier prediction and AST edge prediction objectives, demonstrating that explicitly encoding syntactic structure during contrastive pre-training improves downstream code intelligence tasks. ContraBERT \\cite{liu2023contrabert} takes a complementary robustness-oriented approach, designing nine data augmentation operators that generate adversarial code and comment variants---including identifier renaming, dead code insertion, and operand swapping---and further trains existing code models with contrastive objectives on these augmented pairs. ContraBERT shows that contrastive pre-training with targeted perturbations substantially improves model robustness against adversarial attacks while maintaining strong performance on standard benchmarks. These methods enrich the positive pair construction space for code contrastive learning, yet they focus on augmenting the pre-training signal rather than improving the selection of negative examples during fine-tuning. StructFuse addresses a complementary dimension: rather than improving how positive pairs are constructed, it improves which negatives the model trains against by grounding negative selection in inter-procedural data-flow structure.\n\n## Supplement B: Hard Negative Mining in Dense Retrieval (insert into Section 2.3, after the CL-DRD sentence)\n\nThe curriculum learning paradigm for negative sampling has been further developed by CAPSTONE \\cite{he2023capstone}, which addresses the training-inference discrepancy in dual-encoder dense retrieval. CAPSTONE expands documents with pseudo-queries during training and employs a curriculum sampling strategy that progressively improves the relevance between generated and real queries, effectively controlling negative difficulty through the query generation quality. This approach achieves strong results on both in-domain and out-of-domain retrieval benchmarks, reinforcing the finding that curriculum-based difficulty scheduling benefits dense retrieval training. While CAPSTONE focuses on bridging the training-inference gap through document expansion, our structure-grounded negatives provide an orthogonal form of curriculum: negatives that are hard because they share data-flow context with the positive, not because of embedding proximity alone.\n\n## Supplement C: Cross-File Code Understanding and Evaluation (insert into Section 2.4, before the closing paragraph, or as a new subsection bridge)\n\nThe importance of cross-file context for code understanding has been empirically validated by dedicated benchmarks. CrossCodeEval \\cite{ding2023crosscodeeval} constructs a diverse, multilingual benchmark for cross-file code completion across Python, Java, TypeScript, and C\\#, using static analysis to identify completion targets that strictly require cross-file dependencies. Experiments show that even state-of-the-art code LLMs struggle without cross-file context, and that retrieval-augmented approaches yield clear improvements---yet performance remains far below the ceiling, indicating substantial room for better cross-file retrieval. ProGraML \\cite{cummins2021programl} provides a language-independent, graph-based program representation that captures control-flow, data-flow, and call relations across entire programs, achieving strong results on data-flow analysis tasks. ProGraML demonstrates that whole-program structural representations are learnable and informative, providing conceptual grounding for StructFuse's use of inter-procedural data-flow graphs as a training signal. CoSQA \\cite{huang2021cosqa} contributes a large-scale dataset of 20,000+ real web queries paired with Python code, bridging the gap between synthetic code search benchmarks and real-world developer information needs; it also introduces a contrastive learning method (CoCLR) for data augmentation in code search training. Together, these resources underscore that cross-file structural dependencies and realistic query distributions are critical dimensions for advancing code retrieval---precisely the dimensions that StructFuse's structure-grounded training targets.\n\n---\n\n## Summary of New Citations\n\n| Paper | Venue | Year | Area | Relation to StructFuse |\n|-------|-------|------|------|----------------------|\n| SynCoBERT | arXiv | 2021 | Contrastive code pre-training | Syntax-guided contrastive pre-training; StructFuse uses structure for negatives, not positives |\n| ContraBERT | ICSE | 2023 | Contrastive code pre-training | Robustness-oriented augmentation; complementary to StructFuse's negative mining |\n| CAPSTONE | EMNLP | 2023 | Dense retrieval | Curriculum sampling for retrieval; StructFuse provides structure-based curriculum |\n| CrossCodeEval | NeurIPS | 2023 | Benchmark | Validates importance of cross-file context for code tasks |\n| ProGraML | ICML | 2021 | Program graphs for ML | Whole-program graph representation; conceptual grounding for StructFuse's data-flow use |\n| CoSQA | ACL | 2021 | Code search dataset | Real-world query benchmark with contrastive learning augmentation |\n",
      "numLines": 33,
      "startLine": 1,
      "totalLines": 33
    }
  }
}
```

</details>

---

### Tool call

_source line 91_

<details open><summary>🔧 Tool call — Read · `toolu_015Pf6rpDHVHVhwjNzMEDGe1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/references.bib",
  "offset": 273
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "ae7df131-c1ce-4cdc-b200-a8b0bf3350ed",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KoNGJo3Fd9V2gq3JJWSzuY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6190,
      "cache_read_input_tokens": 67424,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6190
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

_source line 92 · 2026-05-15T05:14:43.322Z_

<details><summary>↩ Tool result · `toolu_015Pf6rpDHVHVhwjNzMEDGe1`</summary>

```text
273	
274	% =============================================================================
275	% Supplement: New citations added 2026-05-15
276	% =============================================================================
277	
278	@article{wang2021syncobert,
279	  title={{SynCoBERT}: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation},
280	  author={Wang, Xin and Wang, Yasheng and Mi, Fei and Zhou, Pingyi and Wan, Yao and Liu, Xiao and Li, Li and Wu, Hao and Liu, Jin and Jiang, Xin},
281	  journal={arXiv preprint arXiv:2108.04556},
282	  year={2021}
283	}
284	
285	@inproceedings{liu2023contrabert,
286	  title={{ContraBERT}: Enhancing Code Pre-trained Models via Contrastive Learning},
287	  author={Liu, Shangqing and Wu, Bozhi and Xie, Xiaofei and Meng, Guozhu and Liu, Yang},
288	  booktitle={Proceedings of the 45th IEEE/ACM International Conference on Software Engineering (ICSE)},
289	  pages={2476--2487},
290	  year={2023}
291	}
292	
293	@inproceedings{he2023capstone,
294	  title={{CAPSTONE}: Curriculum Sampling for Dense Retrieval with Document Expansion},
295	  author={He, Xingwei and Gong, Yeyun and Jin, A-Long and Zhang, Hang and Dong, Anlei and Jiao, Jian and Yiu, Siu Ming and Duan, Nan},
296	  booktitle={Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
297	  pages={10531--10541},
298	  year={2023}
299	}
300	
301	@inproceedings{ding2023crosscodeeval,
302	  title={{CrossCodeEval}: A Diverse and Multilingual Benchmark for Cross-File Code Completion},
303	  author={Ding, Yangruibo and Wang, Zijian and Ahmad, Wasi Uddin and Ding, Hantian and Tan, Ming and Jain, Nihal and Ramanathan, Murali Krishna and Nallapati, Ramesh and Bhatia, Parminder and Roth, Dan and Xiang, Bing},
304	  booktitle={Advances in Neural Information Processing Systems 36 (NeurIPS)},
305	  year={2023}
306	}
307	
308	@inproceedings{cummins2021programl,
309	  title={{ProGraML}: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations},
310	  author={Cummins, Chris and Fisches, Zacharias V. and Ben-Nun, Tal and Hoefler, Torsten and O'Boyle, Michael F. P. and Leather, Hugh},
311	  booktitle={Proceedings of the 38th International Conference on Machine Learning (ICML)},
312	  pages={2244--2253},
313	  year={2021},
314	  publisher={PMLR}
315	}
316	
317	@inproceedings{huang2021cosqa,
318	  title={{CoSQA}: 20,000+ Web Queries for Code Search and Question Answering},
319	  author={Huang, Junjie and Tang, Duyu and Shou, Linjun and Gong, Ming and Xu, Ke and Jiang, Daxin and Zhou, Ming and Duan, Nan},
320	  booktitle={Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL)},
321	  pages={5690--5700},
322	  year={2021}
323	}
324	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "325b0e99-a06a-4747-8cf4-653b5550fdb9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/references.bib",
      "content": "\n% =============================================================================\n% Supplement: New citations added 2026-05-15\n% =============================================================================\n\n@article{wang2021syncobert,\n  title={{SynCoBERT}: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation},\n  author={Wang, Xin and Wang, Yasheng and Mi, Fei and Zhou, Pingyi and Wan, Yao and Liu, Xiao and Li, Li and Wu, Hao and Liu, Jin and Jiang, Xin},\n  journal={arXiv preprint arXiv:2108.04556},\n  year={2021}\n}\n\n@inproceedings{liu2023contrabert,\n  title={{ContraBERT}: Enhancing Code Pre-trained Models via Contrastive Learning},\n  author={Liu, Shangqing and Wu, Bozhi and Xie, Xiaofei and Meng, Guozhu and Liu, Yang},\n  booktitle={Proceedings of the 45th IEEE/ACM International Conference on Software Engineering (ICSE)},\n  pages={2476--2487},\n  year={2023}\n}\n\n@inproceedings{he2023capstone,\n  title={{CAPSTONE}: Curriculum Sampling for Dense Retrieval with Document Expansion},\n  author={He, Xingwei and Gong, Yeyun and Jin, A-Long and Zhang, Hang and Dong, Anlei and Jiao, Jian and Yiu, Siu Ming and Duan, Nan},\n  booktitle={Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages={10531--10541},\n  year={2023}\n}\n\n@inproceedings{ding2023crosscodeeval,\n  title={{CrossCodeEval}: A Diverse and Multilingual Benchmark for Cross-File Code Completion},\n  author={Ding, Yangruibo and Wang, Zijian and Ahmad, Wasi Uddin and Ding, Hantian and Tan, Ming and Jain, Nihal and Ramanathan, Murali Krishna and Nallapati, Ramesh and Bhatia, Parminder and Roth, Dan and Xiang, Bing},\n  booktitle={Advances in Neural Information Processing Systems 36 (NeurIPS)},\n  year={2023}\n}\n\n@inproceedings{cummins2021programl,\n  title={{ProGraML}: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations},\n  author={Cummins, Chris and Fisches, Zacharias V. and Ben-Nun, Tal and Hoefler, Torsten and O'Boyle, Michael F. P. and Leather, Hugh},\n  booktitle={Proceedings of the 38th International Conference on Machine Learning (ICML)},\n  pages={2244--2253},\n  year={2021},\n  publisher={PMLR}\n}\n\n@inproceedings{huang2021cosqa,\n  title={{CoSQA}: 20,000+ Web Queries for Code Search and Question Answering},\n  author={Huang, Junjie and Tang, Duyu and Shou, Linjun and Gong, Ming and Xu, Ke and Jiang, Daxin and Zhou, Ming and Duan, Nan},\n  booktitle={Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  pages={5690--5700},\n  year={2021}\n}\n",
      "numLines": 52,
      "startLine": 273,
      "totalLines": 324
    }
  }
}
```

</details>

---

### Assistant

_source line 93_

完成。产出总结：

**新增 6 篇引用**（全部经 WebSearch 验证）：

| 论文 | Venue | 插入位置 |
|------|-------|---------|
| SynCoBERT | arXiv 2021 | §2.2 Contrastive Learning for Code |
| ContraBERT | ICSE 2023 | §2.2 Contrastive Learning for Code |
| CAPSTONE | EMNLP 2023 | §2.3 Hard Negative Mining |
| CrossCodeEval | NeurIPS 2023 | §2.4 Code Structure / Evaluation |
| ProGraML | ICML 2021 | §2.4 Code Structure / Evaluation |
| CoSQA | ACL 2021 | §2.4 Code Structure / Evaluation |

**注意**：任务中推荐的 RocketQA 已在 v1 草稿中引用，无需重复添加。

**产出文件**：
- 段落草稿：`artifacts/paper_drafts/related_work_supplement.md` — 3 个补充段落，含插入位置标注和 StructFuse 定位说明
- BibTeX entries：追加到 `artifacts/paper_drafts/references.bib`（6 条新 entry）

**段落逻辑**：
- **Supplement A**：SynCoBERT（语法引导）+ ContraBERT（鲁棒性增强）→ 这些方法改进正样本构造，StructFuse 改进负样本选择
- **Supplement B**：CAPSTONE 课程学习式采样 → StructFuse 的结构化负样本提供正交的难度来源
- **Supplement C**：CrossCodeEval 验证跨文件上下文重要性 + ProGraML 全程序图表示 + CoSQA 真实查询分布 → 支撑 StructFuse 的跨文件结构训练目标

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "uuid": "f5b760dc-be0e-4182-b594-4a65e9de3c8c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BsmBNh1EqyfGnjKppzjyuV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2715,
      "cache_read_input_tokens": 73614,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2715
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

_source line 94_

完成。产出总结：

**新增 6 篇引用**（全部经 WebSearch 验证）：

| 论文 | Venue | 插入位置 |
|------|-------|---------|
| SynCoBERT | arXiv 2021 | §2.2 Contrastive Learning for Code |
| ContraBERT | ICSE 2023 | §2.2 Contrastive Learning for Code |
| CAPSTONE | EMNLP 2023 | §2.3 Hard Negative Mining |
| CrossCodeEval | NeurIPS 2023 | §2.4 Code Structure / Evaluation |
| ProGraML | ICML 2021 | §2.4 Code Structure / Evaluation |
| CoSQA | ACL 2021 | §2.4 Code Structure / Evaluation |

**注意**：任务中推荐的 RocketQA 已在 v1 草稿中引用，无需重复添加。

**产出文件**：
- 段落草稿：`artifacts/paper_drafts/related_work_supplement.md` — 3 个补充段落，含插入位置标注和 StructFuse 定位说明
- BibTeX entries：追加到 `artifacts/paper_drafts/references.bib`（6 条新 entry）

**段落逻辑**：
- **Supplement A**：SynCoBERT（语法引导）+ ContraBERT（鲁棒性增强）→ 这些方法改进正样本构造，StructFuse 改进负样本选择
- **Supplement B**：CAPSTONE 课程学习式采样 → StructFuse 的结构化负样本提供正交的难度来源
- **Supplement C**：CrossCodeEval 验证跨文件上下文重要性 + ProGraML 全程序图表示 + CoSQA 真实查询分布 → 支撑 StructFuse 的跨文件结构训练目标

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 246169,
  "duration_api_ms": 300386,
  "num_turns": 34,
  "stop_reason": "end_turn",
  "session_id": "d353a78f-ca44-4be5-b2db-20fe6af79042",
  "total_cost_usd": 1.9156404999999999,
  "usage": {
    "input_tokens": 5195,
    "cache_creation_input_tokens": 64488,
    "cache_read_input_tokens": 1085555,
    "output_tokens": 9011,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 64488,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 544,
        "cache_read_input_tokens": 73614,
        "cache_creation_input_tokens": 2715,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2715
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 477023,
      "outputTokens": 6308,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 21,
      "costUSD": 0.7185630000000001,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 5195,
      "outputTokens": 9011,
      "cacheReadInputTokens": 1085555,
      "cacheCreationInputTokens": 64488,
      "webSearchRequests": 0,
      "costUSD": 1.1970775000000002,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "653adf43-1a0b-4d33-a467-8976d7331720"
}
```

</details>

---
