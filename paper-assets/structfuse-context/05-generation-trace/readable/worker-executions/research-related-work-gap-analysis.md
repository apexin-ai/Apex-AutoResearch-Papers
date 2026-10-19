# research related work gap analysis

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 114
- **Recorded user turns:** 1
- **Tool calls:** 35
- **Original source:** `logs/workers/worker_research_related-work-gap-analysis_20260515T041514.log`
- **Structured JSON:** [`4c73059a2adb28934f05.json`](../../sessions/4c/4c73059a2adb28934f05.json)

## Before a recorded user message

17 recorded events

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
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
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
  "uuid": "a4f12b0b-00f0-477e-b37b-e8a177f1f501",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-structfuse-context/memory/"
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
    "resetsAt": 1778825400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "456b35f8-85aa-45ad-9d0d-59a15354823d",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691"
}
```

---

### Assistant

_source line 4_

I'll start by reading the two key files to understand the current citation landscape.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "918fa292-4546-41c7-b812-fcad75be3773",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bm9mWQKweCtaw1YqHpJczk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11900,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11900
      },
      "output_tokens": 2,
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_015QEEdAnUQoEU9fgKtE5FXo`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__append_idea",
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
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "7dfc8c57-f923-47d0-adbe-a2b13de70c11",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bm9mWQKweCtaw1YqHpJczk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11900,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11900
      },
      "output_tokens": 2,
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

_source line 6 · 2026-05-15T04:15:26.283Z_

<details><summary>↩ Tool result · `toolu_015QEEdAnUQoEU9fgKtE5FXo`</summary>

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
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "c3ffb813-1ab3-465d-95cf-4e4c981c3b26",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__append_idea"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__append_idea",
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
Now let me read the two key files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "e80ed288-1844-4a2f-9190-349a8877fd26",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BwEnAAgosYwMBJM4QURBE5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 910,
      "cache_read_input_tokens": 23347,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 910
      },
      "output_tokens": 43,
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01EGEYt1wEkgt4UhRgwLUk9R`</summary>

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
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "fb16cefb-e775-40dc-8c84-65eee8a1337e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BwEnAAgosYwMBJM4QURBE5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 910,
      "cache_read_input_tokens": 23347,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 910
      },
      "output_tokens": 43,
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

_source line 9 · 2026-05-15T04:15:29.619Z_

<details><summary>↩ Tool result · `toolu_01EGEYt1wEkgt4UhRgwLUk9R`</summary>

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
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "289a93b1-5797-4966-a880-0b7332afccb8",
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

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01LjsZXgiW4zqQk3hR4JdnPq`</summary>

```json
{
  "project": "structfuse-context",
  "file": "artifacts/paper_drafts/discussion_v2.md",
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
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "d8b64315-128d-4655-a607-55774a60fa4a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BwEnAAgosYwMBJM4QURBE5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 910,
      "cache_read_input_tokens": 23347,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 910
      },
      "output_tokens": 43,
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

_source line 11 · 2026-05-15T04:15:30.605Z_

<details><summary>↩ Tool result · `toolu_01LjsZXgiW4zqQk3hR4JdnPq`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/paper_drafts/discussion_v2.md'\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "4bb0b371-61ff-4ff5-ad97-23a73fdba20c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/paper_drafts/discussion_v2.md'\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/paper_drafts/discussion_v2.md'\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_012yAee5YQqBDtdLhcKVumz9`</summary>

```json
{
  "project": "structfuse-context",
  "file": "memory.md",
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
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "5ee9090b-04df-414a-aeb0-c9f3cf25a609",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BwEnAAgosYwMBJM4QURBE5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 910,
      "cache_read_input_tokens": 23347,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 910
      },
      "output_tokens": 43,
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

_source line 13 · 2026-05-15T04:15:30.886Z_

<details><summary>↩ Tool result · `toolu_012yAee5YQqBDtdLhcKVumz9`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/memory.md\", \"content\": \"# Inference-Time Graph Methods 文献对比\\n\\n## 对比表\\n\\n| Method | Paper | Venue | Graph Type | Usage Stage | Inter-proc Data-Flow | Task | Scalability | Key Diff from StructFuse |\\n|--------|-------|-------|-----------|-------------|---------------------|------|-------------|--------------------------|\\n| **CodexGraph** | Bridging LLMs and Code Repositories via Code Graph Databases | NAACL 2025 (arXiv:2408.03910) | Code graph DB (MODULE/CLASS/FUNCTION nodes; CONTAINS/INHERITS/USES edges) | Inference-time | No. Static analysis for symbol relations only | General repo-level coding (completion, issue resolution) | CrossCodeEval, SWE-bench, EvoCodeBench | Agent queries graph DB at inference; task-agnostic schema but no data-flow semantics |\\n| **LocAgent** | Graph-Guided LLM Agents for Code Localization | ACL 2025 (arXiv:2503.09089) | Directed heterogeneous graph (code entities + dependency edges) | Inference-time | No. Dependency edges, not data-flow | Fault localization | 92.7% file-level accuracy; SWE-bench +12% Pass@10 | Agent multi-hop graph reasoning at inference; needs fine-tuned 32B model |\\n| **RANGER** | RANGER — Repository-Level Agent for Graph-Enhanced Retrieval | arXiv:2509.25257 (Sep 2025) | Knowledge graph + MCTS traversal | Inference-time | No | Code search, QA, cross-file retrieval, completion | CodeSearchNet, RepoQA, RepoBench, CrossCodeEval | MCTS-guided graph exploration; dual-stage (Cypher + MCTS); higher inference cost due to cross-encoder scoring |\\n| **RepoGraph** | Enhancing AI SE with Repository-level Code Graph | ICLR 2025 (arXiv:2410.14684) | Repo-level code graph (class hierarchy, call graph, file structure) | Inference-time | No. Structural relations only | Software engineering / issue resolution | SWE-bench (+32.8% relative); CrossCodeEval | Plug-in module for existing agents; repo-wide navigation; no semantic analysis |\\n| **GraphCoder** | Enhancing Repo-Level Code Completion via Code Context Graph | ASE 2024 (arXiv:2406.07003) | Code Context Graph (CFG + CDG + DDG) | Inference-time | Partial. Data dependence graph but **intra-procedural** only | Code completion | Repository-level benchmarks | Coarse-to-fine retrieval with CCG; closest to StructFuse in using data/control flow, but intra-proc and at inference-time |\\n| **CodeRAG** | Supportive Code Retrieval on Bigraph for Real-World Code Generation | arXiv:2504.10046 (Apr 2025) | Bigraph (requirement graph + DS-code graph) | Inference-time | No. Dependency + semantic edges | Repo-level code generation | DevEval (+40.90 Pass@1 w/ GPT-4o) | Dual-graph (requirements + code); agentic reasoning; high inference overhead |\\n| **ARISE** | ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair | arXiv:2605.03117 (May 2026), Seddik & Fard | Multi-granularity program graph (statement nodes + def-use edges) | Inference-time | Partial. **Intra-procedural** def-use edges + data-flow slicing tool | Fault localization + repair | SWE-bench Lite (300 issues); +17.0 Function Recall@1 | Closest to StructFuse in data-flow usage; but intra-proc only, agent queries at inference |\\n| **CodeGRAG** | Bridging NL and PL via Graphical RAG | arXiv:2405.02355 (2024) | Composed syntax graph (AST + DFG + CFG) | Both (GNN training + graph prompt at inference) | Partial. DFG extraction but function-level | Code generation (cross-lingual) | Multiple PLs | Only method with training-time component (GNN soft prompts); but graph also used at inference |\\n| **StructFuse** (Ours) | Structure-Grounded Hard Negatives via CodeQL Data-Flow | — | Inter-procedural data-flow graph (CodeQL taint tracking) | **Training-time only** | **Yes. Full inter-procedural** (source→sink across call boundaries) | Code retrieval (contrastive training) | Large-scale repos with CodeQL | Zero inference overhead; graph used offline for negative mining; inter-proc data-flow |\\n\\n## Discussion 要点\\n\\n### StructFuse vs Inference-Time Graph Methods: 互补性与差异性\\n\\n1. **Cost-accuracy tradeoff**: Inference-time methods (CodexGraph, RANGER, RepoGraph) achieve high precision by constructing and querying graphs per request, but incur significant latency (graph construction + traversal + LLM calls). StructFuse amortizes all graph computation to training time—once the encoder is trained with structure-grounded negatives, inference is a single embedding lookup with zero graph overhead. This makes StructFuse suitable for latency-sensitive production retrieval where inference-time graph methods are impractical.\\n\\n2. **Data-flow depth**: Most inference-time methods use structural graphs (call graphs, class hierarchies, file dependencies). Only GraphCoder and ARISE incorporate data/control flow, but limited to **intra-procedural** scope. StructFuse uniquely leverages **inter-procedural** data-flow via CodeQL's taint tracking, capturing cross-function semantic relationships (e.g., a sanitizer function that transforms data between source and sink across call boundaries). This deeper semantic signal generates harder, more informative negatives.\\n\\n3. **Complementarity**: StructFuse and inference-time methods are orthogonal and composable. A StructFuse-trained encoder can serve as the embedding backbone for systems like RANGER or CodexGraph, providing better initial retrieval that reduces the graph agent's search space. Conversely, inference-time graph methods can provide reranking on top of StructFuse retrieval for tasks requiring maximum precision.\\n\\n4. **Scalability model**: Inference-time methods scale linearly with query volume (each query triggers graph operations). StructFuse's cost is front-loaded: CodeQL analysis runs once per repository update, and the resulting negatives improve the encoder permanently. For high-QPS code search services, this one-time investment yields compounding returns.\\n\\n5. **Task generality vs specialization**: Inference-time graph agents (CodexGraph, RepoGraph) are task-agnostic but require powerful LLMs as backends. StructFuse produces a specialized retrieval encoder that excels at the code search task without LLM inference, making it deployable as a lightweight, efficient first-stage retriever in multi-stage pipelines.\\n\\n## Related Work 段落草稿 (~200 words)\\n\\n**Graph-Based Methods for Code Understanding.**\\nRecent work has explored leveraging code graphs to enhance LLM-based software engineering. Inference-time approaches construct and query graphs during each interaction: CodexGraph (Liu et al., NAACL 2025) builds a code graph database that LLM agents query via structured interfaces; RepoGraph (Ouyang et al., ICLR 2025) provides repository-level navigation as a plug-in module for SE agents; LocAgent (ACL 2025) and RANGER (Shah et al., 2025) employ graph-guided multi-hop reasoning and MCTS-based traversal for code localization and retrieval, respectively. GraphCoder (ASE 2024) incorporates intra-procedural control-flow and data-dependence graphs for code completion retrieval, while ARISE (Seddik & Fard, 2026) extends this with statement-level def-use edges for fault localization. CodeGRAG (2024) bridges training and inference by using GNN-encoded graph prompts.\\n\\nThese methods achieve strong results but impose substantial inference-time costs—graph construction, traversal, and often multiple LLM calls per query. Moreover, their data-flow analysis remains intra-procedural. StructFuse takes a fundamentally different approach: we leverage CodeQL's inter-procedural taint tracking to generate structure-grounded hard negatives at **training time**, producing an encoder that captures cross-function data-flow semantics without any graph overhead at inference. This positions StructFuse as complementary to inference-time graph methods—it can serve as an efficient first-stage retriever whose embeddings already encode deep structural relationships that other methods must compute on-the-fly.\\n\\n---\\n\\n## 参考文献（全部已验证 2026-05-14）\\n\\n- CodexGraph: arXiv:2408.03910, Liu et al., NAACL 2025\\n- LocAgent: arXiv:2503.09089, Chen et al., ACL 2025\\n- RANGER: arXiv:2509.25257, Shah et al., 2025 ✅ verified\\n- RepoGraph: arXiv:2410.14684, Ouyang et al., ICLR 2025\\n- GraphCoder: arXiv:2406.07003, Liu et al., ASE 2024\\n- CodeRAG: arXiv:2504.10046, 2025\\n- ARISE: arXiv:2605.03117, Seddik & Fard, 2026 ✅ verified (full title: \\\"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair\\\")\\n- CodeGRAG: arXiv:2405.02355, 2024\\n\\n---\\n\\n## Checkpoint Criterion 与 K 分析 (2026-05-15)\\n\\n**Checkpoint 选择 criterion 分歧率**：4 个完成的 full M2 runs 中，2/4 (50%) val_loss 与 R@1 选中不同 checkpoint。\\n\\n**分歧 pattern**：\\n- Qwen s43: val_loss→step 500, R@1→step 1500, R@1 差 +1.97pp\\n- StarCoder s42: val_loss→step 1000, R@1→step 2500, R@1 差 +0.64pp\\n- Mean delta: +0.65pp (R@1 criterion 优于 val_loss criterion)\\n- StarCoder 步差更大（1500 步 vs 1000 步），与其 pretrained margin 更大的特性一致\\n\\n**论文写作决策**：主表报 best_by_R@1（target metric aligned），ablation 表展示两种 criterion 对比（D036 已决策 R@1 为 primary）。\\n\\n**K=7 无 ablation**：所有正式实验固定 K=7。合理性来源：(1) batch_size=8 对齐（1 positive + 7 negatives = 8）(2) DPR 等文献惯例 (3) hard_negative_ratio=0.5 平衡设计。K 敏感性列为 limitation/future work。\\n\\n---\\n\\n## BM25 Negative Mining 策略洞察 (2026-05-14, updated)\\n\\n**两层重叠率数据（注意区分）**：\\n- **k=50 全候选重叠**（mining worker 报告）：BM25 vs embedding 87.1%, vs random 76.2%, vs dataflow 71.8%\\n- **top-7 Jaccard**（训练实际用的 num_negatives=7，分层分析）：差异远大于全候选\\n\\n**分层 top-7 Jaccard 重叠率**（seed 42, 2920 matched queries / 12290 total）：\\n| 层级 | BM25 vs Embedding | BM25 vs Random | BM25 vs Dataflow |\\n|------|-------------------|----------------|------------------|\\n| Small (<50 files, 39 repos) | 0.668 | 0.411 | 0.667 |\\n| Medium (50-200, 29 repos) | 0.380 | 0.067 | 0.363 |\\n| Large (200+, 15 repos) | 0.297 | 0.007 | 0.405 |\\n\\n**核心修正**：之前基于 87% 预测\\\"Phase 2 中 BM25 R@1 很可能接近 embedding\\\"——这个预测可能不成立。在中大 repo（训练数据主体）上 top-7 Jaccard 仅 30-38%，BM25 和 embedding 选出的训练 negatives 大部分不同。Phase 2 训练结果将真正区分两种策略。\\n\\n**意外发现**：BM25 vs dataflow 在大 repo 上重叠率（0.405）高于 vs embedding（0.297）。词汇相似性信号与数据流依赖有部分对齐，而纯 embedding 距离选择了不同维度的 hard negatives。\\n\\n---\\n\\n## hard_negative_mining.py vs build_m1_training_data.py 实现差异 [2026-05-15]\\n\\n**发现者**：Reviewer\\n**影响**：当前 M2 不受影响（用 pre-mined 数据），plan_015（dynamic negative mining）实施前必须对齐\\n\\n**差异**：\\n\\n### hard_negative_mining.py `DataFlowAwareMiner`（training/hard_negative_mining.py）\\n三步法：\\n1. **Embedding top-K**：调用 `EmbeddingDistanceMiner.mine()` 获取 top-50 cosine similarity 最高的 candidates（从所有 non-positive candidates 中）\\n2. **Dataflow filter**：过滤掉 `_is_reachable(query, fid)` 为 True 的文件——仅检查 `dataflow_graph[src]` 中的直接条目（1-hop 可达性）\\n3. **BM25 re-rank**：如果 `bm25_index` 可用，对剩余 disconnected candidates 按 BM25 分数降序重排\\n4. **Fallback**：如果 disconnected 不足 `num_negatives`，用 random padding 补足\\n\\n### build_m1_training_data.py `build_candidate_pools()`（scripts/build_m1_training_data.py）\\n两步法：\\n1. **Dataflow filter**：从 `non_pos_files` 中排除 `full_connected_set`（= `positive_files ∪ cg_connected`，即 dataflow 直连 + call graph 邻居——比 `DataFlowAwareMiner` 排除范围更广）\\n2. **BM25 sort**：对 disconnected 文件按 BM25 分数降序排序，取 top-K（pool_size=50）\\n3. **无 embedding 步骤**：dataflow pool 完全不使用 embedding 信号\\n\\n额外注意：当 `--model-path` 未提供时，`emb_scores = bm25`（line 317-318），此时 embedding pool 也退化为 BM25 排序，仅在是否排除 `full_connected` 上与 dataflow pool 不同。\\n\\n### 差异总结\\n\\n| 维度 | hard_negative_mining.py | build_m1_training_data.py |\\n|------|------------------------|--------------------------|\\n| Candidate 初筛 | Embedding cosine top-50 | 全部 non-positive（无初筛） |\\n| Dataflow 排除范围 | `dataflow_graph[src]` 直接条目 | `positive_files ∪ cg_connected`（更广） |\\n| 排序信号 | Embedding 为主 → BM25 re-rank | 纯 BM25 排序 |\\n| Embedding 角色 | 主选择器（决定候选池） | 不参与 dataflow pool |\\n| BM25 角色 | 可选的 re-ranker | 唯一排序信号 |\\n\\n### 对齐建议\\nplan_015 实施 dynamic negative mining 时需统一为一种逻辑。建议：\\n1. **排除范围统一**：采用 `build_m1_training_data.py` 的 `full_connected`（dataflow + call graph），因为 call graph 邻居也不应作为 hard negatives\\n2. **选择信号**：dynamic mining 应使用当前 epoch 的 encoder embedding（不是 pretrained），这是 dynamic mining 的核心价值——所以 `DataFlowAwareMiner` 的 embedding→filter→BM25 三步法更合理，但需将排除范围从 1-hop dataflow 扩展到 full_connected\\n3. **具体改动**：修改 `DataFlowAwareMiner._is_reachable()` 使其也排除 call graph 连接，或在 `mine()` 中接受 `full_connected_set` 参数\\n\\n---\\n\\n## 运维经验 (2026-05-14)\\n\\n**Registry 状态机 workaround**：当长链训练（多 run 串行）中途因 cron timeout 或子进程退出导致 registry 状态误标（DONE/failed 或 ANALYZING），而实际训练仍在跑时，不可回退状态。解决方案：创建 `{exp_id}_resumed` / `{exp_id}_continued` 新 entry，步进 PREPARING→QUEUED→ALLOCATED→RUNNING，注册 cron 监控实际 PID。原 entry 保留历史 metrics。\\n\\n**Bash 预读陷阱**：运行中的 bash 脚本已将循环体/数组预读到内存，磁盘上修改脚本文件不影响执行。需要在链外设置独立 tmux watcher 监控链 PID 退出后手动触发后续任务。\\n\\n**BM25 Phase 2 触发机制**：两个 tmux watcher（`bm25_starcoder_watcher`, `bm25_qwen_watcher`）每 5 分钟检查链 PID 存活，退出后自动启动 BM25 脚本。watcher 启动的训练不经过 submit_training_job，需在链完成回调中补注册 cron。\\n\\n---\\n\\n## 关键决策记录\\n\\n**m1_reextract_v2 数据使用决策 (2026-05-14, Director Session 8)**：即使 reextract 将数据从 ~16K 增至 ~44K，不重跑 M2。原因：ARR May 25 DDL 不允许再加 4-5 天重训。处理方式：(1) post-M2 完成后若有 GPU 空档，跑 1-seed pilot (Qwen, embedding, 新数据) 对比当前 M2 baseline；(2) 论文中作为 scalability/data efficiency 讨论点；(3) 全量重训留 camera-ready。\", \"total_chars\": 12963, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "5c276217-bd7d-4447-bbc0-07691a8095ea",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/memory.md\\\", \\\"content\\\": \\\"# Inference-Time Graph Methods 文献对比\\\\n\\\\n## 对比表\\\\n\\\\n| Method | Paper | Venue | Graph Type | Usage Stage | Inter-proc Data-Flow | Task | Scalability | Key Diff from StructFuse |\\\\n|--------|-------|-------|-----------|-------------|---------------------|------|-------------|--------------------------|\\\\n| **CodexGraph** | Bridging LLMs and Code Repositories via Code Graph Databases | NAACL 2025 (arXiv:2408.03910) | Code graph DB (MODULE/CLASS/FUNCTION nodes; CONTAINS/INHERITS/USES edges) | Inference-time | No. Static analysis for symbol relations only | General repo-level coding (completion, issue resolution) | CrossCodeEval, SWE-bench, EvoCodeBench | Agent queries graph DB at inference; task-agnostic schema but no data-flow semantics |\\\\n| **LocAgent** | Graph-Guided LLM Agents for Code Localization | ACL 2025 (arXiv:2503.09089) | Directed heterogeneous graph (code entities + dependency edges) | Inference-time | No. Dependency edges, not data-flow | Fault localization | 92.7% file-level accuracy; SWE-bench +12% Pass@10 | Agent multi-hop graph reasoning at inference; needs fine-tuned 32B model |\\\\n| **RANGER** | RANGER — Repository-Level Agent for Graph-Enhanced Retrieval | arXiv:2509.25257 (Sep 2025) | Knowledge graph + MCTS traversal | Inference-time | No | Code search, QA, cross-file retrieval, completion | CodeSearchNet, RepoQA, RepoBench, CrossCodeEval | MCTS-guided graph exploration; dual-stage (Cypher + MCTS); higher inference cost due to cross-encoder scoring |\\\\n| **RepoGraph** | Enhancing AI SE with Repository-level Code Graph | ICLR 2025 (arXiv:2410.14684) | Repo-level code graph (class hierarchy, call graph, file structure) | Inference-time | No. Structural relations only | Software engineering / issue resolution | SWE-bench (+32.8% relative); CrossCodeEval | Plug-in module for existing agents; repo-wide navigation; no semantic analysis |\\\\n| **GraphCoder** | Enhancing Repo-Level Code Completion via Code Context Graph | ASE 2024 (arXiv:2406.07003) | Code Context Graph (CFG + CDG + DDG) | Inference-time | Partial. Data dependence graph but **intra-procedural** only | Code completion | Repository-level benchmarks | Coarse-to-fine retrieval with CCG; closest to StructFuse in using data/control flow, but intra-proc and at inference-time |\\\\n| **CodeRAG** | Supportive Code Retrieval on Bigraph for Real-World Code Generation | arXiv:2504.10046 (Apr 2025) | Bigraph (requirement graph + DS-code graph) | Inference-time | No. Dependency + semantic edges | Repo-level code generation | DevEval (+40.90 Pass@1 w/ GPT-4o) | Dual-graph (requirements + code); agentic reasoning; high inference overhead |\\\\n| **ARISE** | ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair | arXiv:2605.03117 (May 2026), Seddik & Fard | Multi-granularity program graph (statement nodes + def-use edges) | Inference-time | Partial. **Intra-procedural** def-use edges + data-flow slicing tool | Fault localization + repair | SWE-bench Lite (300 issues); +17.0 Function Recall@1 | Closest to StructFuse in data-flow usage; but intra-proc only, agent queries at inference |\\\\n| **CodeGRAG** | Bridging NL and PL via Graphical RAG | arXiv:2405.02355 (2024) | Composed syntax graph (AST + DFG + CFG) | Both (GNN training + graph prompt at inference) | Partial. DFG extraction but function-level | Code generation (cross-lingual) | Multiple PLs | Only method with training-time component (GNN soft prompts); but graph also used at inference |\\\\n| **StructFuse** (Ours) | Structure-Grounded Hard Negatives via CodeQL Data-Flow | — | Inter-procedural data-flow graph (CodeQL taint tracking) | **Training-time only** | **Yes. Full inter-procedural** (source→sink across call boundaries) | Code retrieval (contrastive training) | Large-scale repos with CodeQL | Zero inference overhead; graph used offline for negative mining; inter-proc data-flow |\\\\n\\\\n## Discussion 要点\\\\n\\\\n### StructFuse vs Inference-Time Graph Methods: 互补性与差异性\\\\n\\\\n1. **Cost-accuracy tradeoff**: Inference-time methods (CodexGraph, RANGER, RepoGraph) achieve high precision by constructing and querying graphs per request, but incur significant latency (graph construction + traversal + LLM calls). StructFuse amortizes all graph computation to training time—once the encoder is trained with structure-grounded negatives, inference is a single embedding lookup with zero graph overhead. This makes StructFuse suitable for latency-sensitive production retrieval where inference-time graph methods are impractical.\\\\n\\\\n2. **Data-flow depth**: Most inference-time methods use structural graphs (call graphs, class hierarchies, file dependencies). Only GraphCoder and ARISE incorporate data/control flow, but limited to **intra-procedural** scope. StructFuse uniquely leverages **inter-procedural** data-flow via CodeQL's taint tracking, capturing cross-function semantic relationships (e.g., a sanitizer function that transforms data between source and sink across call boundaries). This deeper semantic signal generates harder, more informative negatives.\\\\n\\\\n3. **Complementarity**: StructFuse and inference-time methods are orthogonal and composable. A StructFuse-trained encoder can serve as the embedding backbone for systems like RANGER or CodexGraph, providing better initial retrieval that reduces the graph agent's search space. Conversely, inference-time graph methods can provide reranking on top of StructFuse retrieval for tasks requiring maximum precision.\\\\n\\\\n4. **Scalability model**: Inference-time methods scale linearly with query volume (each query triggers graph operations). StructFuse's cost is front-loaded: CodeQL analysis runs once per repository update, and the resulting negatives improve the encoder permanently. For high-QPS code search services, this one-time investment yields compounding returns.\\\\n\\\\n5. **Task generality vs specialization**: Inference-time graph agents (CodexGraph, RepoGraph) are task-agnostic but require powerful LLMs as backends. StructFuse produces a specialized retrieval encoder that excels at the code search task without LLM inference, making it deployable as a lightweight, efficient first-stage retriever in multi-stage pipelines.\\\\n\\\\n## Related Work 段落草稿 (~200 words)\\\\n\\\\n**Graph-Based Methods for Code Understanding.**\\\\nRecent work has explored leveraging code graphs to enhance LLM-based software engineering. Inference-time approaches construct and query graphs during each interaction: CodexGraph (Liu et al., NAACL 2025) builds a code graph database that LLM agents query via structured interfaces; RepoGraph (Ouyang et al., ICLR 2025) provides repository-level navigation as a plug-in module for SE agents; LocAgent (ACL 2025) and RANGER (Shah et al., 2025) employ graph-guided multi-hop reasoning and MCTS-based traversal for code localization and retrieval, respectively. GraphCoder (ASE 2024) incorporates intra-procedural control-flow and data-dependence graphs for code completion retrieval, while ARISE (Seddik & Fard, 2026) extends this with statement-level def-use edges for fault localization. CodeGRAG (2024) bridges training and inference by using GNN-encoded graph prompts.\\\\n\\\\nThese methods achieve strong results but impose substantial inference-time costs—graph construction, traversal, and often multiple LLM calls per query. Moreover, their data-flow analysis remains intra-procedural. StructFuse takes a fundamentally different approach: we leverage CodeQL's inter-procedural taint tracking to generate structure-grounded hard negatives at **training time**, producing an encoder that captures cross-function data-flow semantics without any graph overhead at inference. This positions StructFuse as complementary to inference-time graph methods—it can serve as an efficient first-stage retriever whose embeddings already encode deep structural relationships that other methods must compute on-the-fly.\\\\n\\\\n---\\\\n\\\\n## 参考文献（全部已验证 2026-05-14）\\\\n\\\\n- CodexGraph: arXiv:2408.03910, Liu et al., NAACL 2025\\\\n- LocAgent: arXiv:2503.09089, Chen et al., ACL 2025\\\\n- RANGER: arXiv:2509.25257, Shah et al., 2025 ✅ verified\\\\n- RepoGraph: arXiv:2410.14684, Ouyang et al., ICLR 2025\\\\n- GraphCoder: arXiv:2406.07003, Liu et al., ASE 2024\\\\n- CodeRAG: arXiv:2504.10046, 2025\\\\n- ARISE: arXiv:2605.03117, Seddik & Fard, 2026 ✅ verified (full title: \\\\\\\"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair\\\\\\\")\\\\n- CodeGRAG: arXiv:2405.02355, 2024\\\\n\\\\n---\\\\n\\\\n## Checkpoint Criterion 与 K 分析 (2026-05-15)\\\\n\\\\n**Checkpoint 选择 criterion 分歧率**：4 个完成的 full M2 runs 中，2/4 (50%) val_loss 与 R@1 选中不同 checkpoint。\\\\n\\\\n**分歧 pattern**：\\\\n- Qwen s43: val_loss→step 500, R@1→step 1500, R@1 差 +1.97pp\\\\n- StarCoder s42: val_loss→step 1000, R@1→step 2500, R@1 差 +0.64pp\\\\n- Mean delta: +0.65pp (R@1 criterion 优于 val_loss criterion)\\\\n- StarCoder 步差更大（1500 步 vs 1000 步），与其 pretrained margin 更大的特性一致\\\\n\\\\n**论文写作决策**：主表报 best_by_R@1（target metric aligned），ablation 表展示两种 criterion 对比（D036 已决策 R@1 为 primary）。\\\\n\\\\n**K=7 无 ablation**：所有正式实验固定 K=7。合理性来源：(1) batch_size=8 对齐（1 positive + 7 negatives = 8）(2) DPR 等文献惯例 (3) hard_negative_ratio=0.5 平衡设计。K 敏感性列为 limitation/future work。\\\\n\\\\n---\\\\n\\\\n## BM25 Negative Mining 策略洞察 (2026-05-14, updated)\\\\n\\\\n**两层重叠率数据（注意区分）**：\\\\n- **k=50 全候选重叠**（mining worker 报告）：BM25 vs embedding 87.1%, vs random 76.2%, vs dataflow 71.8%\\\\n- **top-7 Jaccard**（训练实际用的 num_negatives=7，分层分析）：差异远大于全候选\\\\n\\\\n**分层 top-7 Jaccard 重叠率**（seed 42, 2920 matched queries / 12290 total）：\\\\n| 层级 | BM25 vs Embedding | BM25 vs Random | BM25 vs Dataflow |\\\\n|------|-------------------|----------------|------------------|\\\\n| Small (<50 files, 39 repos) | 0.668 | 0.411 | 0.667 |\\\\n| Medium (50-200, 29 repos) | 0.380 | 0.067 | 0.363 |\\\\n| Large (200+, 15 repos) | 0.297 | 0.007 | 0.405 |\\\\n\\\\n**核心修正**：之前基于 87% 预测\\\\\\\"Phase 2 中 BM25 R@1 很可能接近 embedding\\\\\\\"——这个预测可能不成立。在中大 repo（训练数据主体）上 top-7 Jaccard 仅 30-38%，BM25 和 embedding 选出的训练 negatives 大部分不同。Phase 2 训练结果将真正区分两种策略。\\\\n\\\\n**意外发现**：BM25 vs dataflow 在大 repo 上重叠率（0.405）高于 vs embedding（0.297）。词汇相似性信号与数据流依赖有部分对齐，而纯 embedding 距离选择了不同维度的 hard negatives。\\\\n\\\\n---\\\\n\\\\n## hard_negative_mining.py vs build_m1_training_data.py 实现差异 [2026-05-15]\\\\n\\\\n**发现者**：Reviewer\\\\n**影响**：当前 M2 不受影响（用 pre-mined 数据），plan_015（dynamic negative mining）实施前必须对齐\\\\n\\\\n**差异**：\\\\n\\\\n### hard_negative_mining.py `DataFlowAwareMiner`（training/hard_negative_mining.py）\\\\n三步法：\\\\n1. **Embedding top-K**：调用 `EmbeddingDistanceMiner.mine()` 获取 top-50 cosine similarity 最高的 candidates（从所有 non-positive candidates 中）\\\\n2. **Dataflow filter**：过滤掉 `_is_reachable(query, fid)` 为 True 的文件——仅检查 `dataflow_graph[src]` 中的直接条目（1-hop 可达性）\\\\n3. **BM25 re-rank**：如果 `bm25_index` 可用，对剩余 disconnected candidates 按 BM25 分数降序重排\\\\n4. **Fallback**：如果 disconnected 不足 `num_negatives`，用 random padding 补足\\\\n\\\\n### build_m1_training_data.py `build_candidate_pools()`（scripts/build_m1_training_data.py）\\\\n两步法：\\\\n1. **Dataflow filter**：从 `non_pos_files` 中排除 `full_connected_set`（= `positive_files ∪ cg_connected`，即 dataflow 直连 + call graph 邻居——比 `DataFlowAwareMiner` 排除范围更广）\\\\n2. **BM25 sort**：对 disconnected 文件按 BM25 分数降序排序，取 top-K（pool_size=50）\\\\n3. **无 embedding 步骤**：dataflow pool 完全不使用 embedding 信号\\\\n\\\\n额外注意：当 `--model-path` 未提供时，`emb_scores = bm25`（line 317-318），此时 embedding pool 也退化为 BM25 排序，仅在是否排除 `full_connected` 上与 dataflow pool 不同。\\\\n\\\\n### 差异总结\\\\n\\\\n| 维度 | hard_negative_mining.py | build_m1_training_data.py |\\\\n|------|------------------------|--------------------------|\\\\n| Candidate 初筛 | Embedding cosine top-50 | 全部 non-positive（无初筛） |\\\\n| Dataflow 排除范围 | `dataflow_graph[src]` 直接条目 | `positive_files ∪ cg_connected`（更广） |\\\\n| 排序信号 | Embedding 为主 → BM25 re-rank | 纯 BM25 排序 |\\\\n| Embedding 角色 | 主选择器（决定候选池） | 不参与 dataflow pool |\\\\n| BM25 角色 | 可选的 re-ranker | 唯一排序信号 |\\\\n\\\\n### 对齐建议\\\\nplan_015 实施 dynamic negative mining 时需统一为一种逻辑。建议：\\\\n1. **排除范围统一**：采用 `build_m1_training_data.py` 的 `full_connected`（dataflow + call graph），因为 call graph 邻居也不应作为 hard negatives\\\\n2. **选择信号**：dynamic mining 应使用当前 epoch 的 encoder embedding（不是 pretrained），这是 dynamic mining 的核心价值——所以 `DataFlowAwareMiner` 的 embedding→filter→BM25 三步法更合理，但需将排除范围从 1-hop dataflow 扩展到 full_connected\\\\n3. **具体改动**：修改 `DataFlowAwareMiner._is_reachable()` 使其也排除 call graph 连接，或在 `mine()` 中接受 `full_connected_set` 参数\\\\n\\\\n---\\\\n\\\\n## 运维经验 (2026-05-14)\\\\n\\\\n**Registry 状态机 workaround**：当长链训练（多 run 串行）中途因 cron timeout 或子进程退出导致 registry 状态误标（DONE/failed 或 ANALYZING），而实际训练仍在跑时，不可回退状态。解决方案：创建 `{exp_id}_resumed` / `{exp_id}_continued` 新 entry，步进 PREPARING→QUEUED→ALLOCATED→RUNNING，注册 cron 监控实际 PID。原 entry 保留历史 metrics。\\\\n\\\\n**Bash 预读陷阱**：运行中的 bash 脚本已将循环体/数组预读到内存，磁盘上修改脚本文件不影响执行。需要在链外设置独立 tmux watcher 监控链 PID 退出后手动触发后续任务。\\\\n\\\\n**BM25 Phase 2 触发机制**：两个 tmux watcher（`bm25_starcoder_watcher`, `bm25_qwen_watcher`）每 5 分钟检查链 PID 存活，退出后自动启动 BM25 脚本。watcher 启动的训练不经过 submit_training_job，需在链完成回调中补注册 cron。\\\\n\\\\n---\\\\n\\\\n## 关键决策记录\\\\n\\\\n**m1_reextract_v2 数据使用决策 (2026-05-14, Director Session 8)**：即使 reextract 将数据从 ~16K 增至 ~44K，不重跑 M2。原因：ARR May 25 DDL 不允许再加 4-5 天重训。处理方式：(1) post-M2 完成后若有 GPU 空档，跑 1-seed pilot (Qwen, embedding, 新数据) 对比当前 M2 baseline；(2) 论文中作为 scalability/data efficiency 讨论点；(3) 全量重训留 camera-ready。\\\", \\\"total_chars\\\": 12963, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/memory.md\", \"content\": \"# Inference-Time Graph Methods 文献对比\\n\\n## 对比表\\n\\n| Method | Paper | Venue | Graph Type | Usage Stage | Inter-proc Data-Flow | Task | Scalability | Key Diff from StructFuse |\\n|--------|-------|-------|-----------|-------------|---------------------|------|-------------|--------------------------|\\n| **CodexGraph** | Bridging LLMs and Code Repositories via Code Graph Databases | NAACL 2025 (arXiv:2408.03910) | Code graph DB (MODULE/CLASS/FUNCTION nodes; CONTAINS/INHERITS/USES edges) | Inference-time | No. Static analysis for symbol relations only | General repo-level coding (completion, issue resolution) | CrossCodeEval, SWE-bench, EvoCodeBench | Agent queries graph DB at inference; task-agnostic schema but no data-flow semantics |\\n| **LocAgent** | Graph-Guided LLM Agents for Code Localization | ACL 2025 (arXiv:2503.09089) | Directed heterogeneous graph (code entities + dependency edges) | Inference-time | No. Dependency edges, not data-flow | Fault localization | 92.7% file-level accuracy; SWE-bench +12% Pass@10 | Agent multi-hop graph reasoning at inference; needs fine-tuned 32B model |\\n| **RANGER** | RANGER — Repository-Level Agent for Graph-Enhanced Retrieval | arXiv:2509.25257 (Sep 2025) | Knowledge graph + MCTS traversal | Inference-time | No | Code search, QA, cross-file retrieval, completion | CodeSearchNet, RepoQA, RepoBench, CrossCodeEval | MCTS-guided graph exploration; dual-stage (Cypher + MCTS); higher inference cost due to cross-encoder scoring |\\n| **RepoGraph** | Enhancing AI SE with Repository-level Code Graph | ICLR 2025 (arXiv:2410.14684) | Repo-level code graph (class hierarchy, call graph, file structure) | Inference-time | No. Structural relations only | Software engineering / issue resolution | SWE-bench (+32.8% relative); CrossCodeEval | Plug-in module for existing agents; repo-wide navigation; no semantic analysis |\\n| **GraphCoder** | Enhancing Repo-Level Code Completion via Code Context Graph | ASE 2024 (arXiv:2406.07003) | Code Context Graph (CFG + CDG + DDG) | Inference-time | Partial. Data dependence graph but **intra-procedural** only | Code completion | Repository-level benchmarks | Coarse-to-fine retrieval with CCG; closest to StructFuse in using data/control flow, but intra-proc and at inference-time |\\n| **CodeRAG** | Supportive Code Retrieval on Bigraph for Real-World Code Generation | arXiv:2504.10046 (Apr 2025) | Bigraph (requirement graph + DS-code graph) | Inference-time | No. Dependency + semantic edges | Repo-level code generation | DevEval (+40.90 Pass@1 w/ GPT-4o) | Dual-graph (requirements + code); agentic reasoning; high inference overhead |\\n| **ARISE** | ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair | arXiv:2605.03117 (May 2026), Seddik & Fard | Multi-granularity program graph (statement nodes + def-use edges) | Inference-time | Partial. **Intra-procedural** def-use edges + data-flow slicing tool | Fault localization + repair | SWE-bench Lite (300 issues); +17.0 Function Recall@1 | Closest to StructFuse in data-flow usage; but intra-proc only, agent queries at inference |\\n| **CodeGRAG** | Bridging NL and PL via Graphical RAG | arXiv:2405.02355 (2024) | Composed syntax graph (AST + DFG + CFG) | Both (GNN training + graph prompt at inference) | Partial. DFG extraction but function-level | Code generation (cross-lingual) | Multiple PLs | Only method with training-time component (GNN soft prompts); but graph also used at inference |\\n| **StructFuse** (Ours) | Structure-Grounded Hard Negatives via CodeQL Data-Flow | — | Inter-procedural data-flow graph (CodeQL taint tracking) | **Training-time only** | **Yes. Full inter-procedural** (source→sink across call boundaries) | Code retrieval (contrastive training) | Large-scale repos with CodeQL | Zero inference overhead; graph used offline for negative mining; inter-proc data-flow |\\n\\n## Discussion 要点\\n\\n### StructFuse vs Inference-Time Graph Methods: 互补性与差异性\\n\\n1. **Cost-accuracy tradeoff**: Inference-time methods (CodexGraph, RANGER, RepoGraph) achieve high precision by constructing and querying graphs per request, but incur significant latency (graph construction + traversal + LLM calls). StructFuse amortizes all graph computation to training time—once the encoder is trained with structure-grounded negatives, inference is a single embedding lookup with zero graph overhead. This makes StructFuse suitable for latency-sensitive production retrieval where inference-time graph methods are impractical.\\n\\n2. **Data-flow depth**: Most inference-time methods use structural graphs (call graphs, class hierarchies, file dependencies). Only GraphCoder and ARISE incorporate data/control flow, but limited to **intra-procedural** scope. StructFuse uniquely leverages **inter-procedural** data-flow via CodeQL's taint tracking, capturing cross-function semantic relationships (e.g., a sanitizer function that transforms data between source and sink across call boundaries). This deeper semantic signal generates harder, more informative negatives.\\n\\n3. **Complementarity**: StructFuse and inference-time methods are orthogonal and composable. A StructFuse-trained encoder can serve as the embedding backbone for systems like RANGER or CodexGraph, providing better initial retrieval that reduces the graph agent's search space. Conversely, inference-time graph methods can provide reranking on top of StructFuse retrieval for tasks requiring maximum precision.\\n\\n4. **Scalability model**: Inference-time methods scale linearly with query volume (each query triggers graph operations). StructFuse's cost is front-loaded: CodeQL analysis runs once per repository update, and the resulting negatives improve the encoder permanently. For high-QPS code search services, this one-time investment yields compounding returns.\\n\\n5. **Task generality vs specialization**: Inference-time graph agents (CodexGraph, RepoGraph) are task-agnostic but require powerful LLMs as backends. StructFuse produces a specialized retrieval encoder that excels at the code search task without LLM inference, making it deployable as a lightweight, efficient first-stage retriever in multi-stage pipelines.\\n\\n## Related Work 段落草稿 (~200 words)\\n\\n**Graph-Based Methods for Code Understanding.**\\nRecent work has explored leveraging code graphs to enhance LLM-based software engineering. Inference-time approaches construct and query graphs during each interaction: CodexGraph (Liu et al., NAACL 2025) builds a code graph database that LLM agents query via structured interfaces; RepoGraph (Ouyang et al., ICLR 2025) provides repository-level navigation as a plug-in module for SE agents; LocAgent (ACL 2025) and RANGER (Shah et al., 2025) employ graph-guided multi-hop reasoning and MCTS-based traversal for code localization and retrieval, respectively. GraphCoder (ASE 2024) incorporates intra-procedural control-flow and data-dependence graphs for code completion retrieval, while ARISE (Seddik & Fard, 2026) extends this with statement-level def-use edges for fault localization. CodeGRAG (2024) bridges training and inference by using GNN-encoded graph prompts.\\n\\nThese methods achieve strong results but impose substantial inference-time costs—graph construction, traversal, and often multiple LLM calls per query. Moreover, their data-flow analysis remains intra-procedural. StructFuse takes a fundamentally different approach: we leverage CodeQL's inter-procedural taint tracking to generate structure-grounded hard negatives at **training time**, producing an encoder that captures cross-function data-flow semantics without any graph overhead at inference. This positions StructFuse as complementary to inference-time graph methods—it can serve as an efficient first-stage retriever whose embeddings already encode deep structural relationships that other methods must compute on-the-fly.\\n\\n---\\n\\n## 参考文献（全部已验证 2026-05-14）\\n\\n- CodexGraph: arXiv:2408.03910, Liu et al., NAACL 2025\\n- LocAgent: arXiv:2503.09089, Chen et al., ACL 2025\\n- RANGER: arXiv:2509.25257, Shah et al., 2025 ✅ verified\\n- RepoGraph: arXiv:2410.14684, Ouyang et al., ICLR 2025\\n- GraphCoder: arXiv:2406.07003, Liu et al., ASE 2024\\n- CodeRAG: arXiv:2504.10046, 2025\\n- ARISE: arXiv:2605.03117, Seddik & Fard, 2026 ✅ verified (full title: \\\"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair\\\")\\n- CodeGRAG: arXiv:2405.02355, 2024\\n\\n---\\n\\n## Checkpoint Criterion 与 K 分析 (2026-05-15)\\n\\n**Checkpoint 选择 criterion 分歧率**：4 个完成的 full M2 runs 中，2/4 (50%) val_loss 与 R@1 选中不同 checkpoint。\\n\\n**分歧 pattern**：\\n- Qwen s43: val_loss→step 500, R@1→step 1500, R@1 差 +1.97pp\\n- StarCoder s42: val_loss→step 1000, R@1→step 2500, R@1 差 +0.64pp\\n- Mean delta: +0.65pp (R@1 criterion 优于 val_loss criterion)\\n- StarCoder 步差更大（1500 步 vs 1000 步），与其 pretrained margin 更大的特性一致\\n\\n**论文写作决策**：主表报 best_by_R@1（target metric aligned），ablation 表展示两种 criterion 对比（D036 已决策 R@1 为 primary）。\\n\\n**K=7 无 ablation**：所有正式实验固定 K=7。合理性来源：(1) batch_size=8 对齐（1 positive + 7 negatives = 8）(2) DPR 等文献惯例 (3) hard_negative_ratio=0.5 平衡设计。K 敏感性列为 limitation/future work。\\n\\n---\\n\\n## BM25 Negative Mining 策略洞察 (2026-05-14, updated)\\n\\n**两层重叠率数据（注意区分）**：\\n- **k=50 全候选重叠**（mining worker 报告）：BM25 vs embedding 87.1%, vs random 76.2%, vs dataflow 71.8%\\n- **top-7 Jaccard**（训练实际用的 num_negatives=7，分层分析）：差异远大于全候选\\n\\n**分层 top-7 Jaccard 重叠率**（seed 42, 2920 matched queries / 12290 total）：\\n| 层级 | BM25 vs Embedding | BM25 vs Random | BM25 vs Dataflow |\\n|------|-------------------|----------------|------------------|\\n| Small (<50 files, 39 repos) | 0.668 | 0.411 | 0.667 |\\n| Medium (50-200, 29 repos) | 0.380 | 0.067 | 0.363 |\\n| Large (200+, 15 repos) | 0.297 | 0.007 | 0.405 |\\n\\n**核心修正**：之前基于 87% 预测\\\"Phase 2 中 BM25 R@1 很可能接近 embedding\\\"——这个预测可能不成立。在中大 repo（训练数据主体）上 top-7 Jaccard 仅 30-38%，BM25 和 embedding 选出的训练 negatives 大部分不同。Phase 2 训练结果将真正区分两种策略。\\n\\n**意外发现**：BM25 vs dataflow 在大 repo 上重叠率（0.405）高于 vs embedding（0.297）。词汇相似性信号与数据流依赖有部分对齐，而纯 embedding 距离选择了不同维度的 hard negatives。\\n\\n---\\n\\n## hard_negative_mining.py vs build_m1_training_data.py 实现差异 [2026-05-15]\\n\\n**发现者**：Reviewer\\n**影响**：当前 M2 不受影响（用 pre-mined 数据），plan_015（dynamic negative mining）实施前必须对齐\\n\\n**差异**：\\n\\n### hard_negative_mining.py `DataFlowAwareMiner`（training/hard_negative_mining.py）\\n三步法：\\n1. **Embedding top-K**：调用 `EmbeddingDistanceMiner.mine()` 获取 top-50 cosine similarity 最高的 candidates（从所有 non-positive candidates 中）\\n2. **Dataflow filter**：过滤掉 `_is_reachable(query, fid)` 为 True 的文件——仅检查 `dataflow_graph[src]` 中的直接条目（1-hop 可达性）\\n3. **BM25 re-rank**：如果 `bm25_index` 可用，对剩余 disconnected candidates 按 BM25 分数降序重排\\n4. **Fallback**：如果 disconnected 不足 `num_negatives`，用 random padding 补足\\n\\n### build_m1_training_data.py `build_candidate_pools()`（scripts/build_m1_training_data.py）\\n两步法：\\n1. **Dataflow filter**：从 `non_pos_files` 中排除 `full_connected_set`（= `positive_files ∪ cg_connected`，即 dataflow 直连 + call graph 邻居——比 `DataFlowAwareMiner` 排除范围更广）\\n2. **BM25 sort**：对 disconnected 文件按 BM25 分数降序排序，取 top-K（pool_size=50）\\n3. **无 embedding 步骤**：dataflow pool 完全不使用 embedding 信号\\n\\n额外注意：当 `--model-path` 未提供时，`emb_scores = bm25`（line 317-318），此时 embedding pool 也退化为 BM25 排序，仅在是否排除 `full_connected` 上与 dataflow pool 不同。\\n\\n### 差异总结\\n\\n| 维度 | hard_negative_mining.py | build_m1_training_data.py |\\n|------|------------------------|--------------------------|\\n| Candidate 初筛 | Embedding cosine top-50 | 全部 non-positive（无初筛） |\\n| Dataflow 排除范围 | `dataflow_graph[src]` 直接条目 | `positive_files ∪ cg_connected`（更广） |\\n| 排序信号 | Embedding 为主 → BM25 re-rank | 纯 BM25 排序 |\\n| Embedding 角色 | 主选择器（决定候选池） | 不参与 dataflow pool |\\n| BM25 角色 | 可选的 re-ranker | 唯一排序信号 |\\n\\n### 对齐建议\\nplan_015 实施 dynamic negative mining 时需统一为一种逻辑。建议：\\n1. **排除范围统一**：采用 `build_m1_training_data.py` 的 `full_connected`（dataflow + call graph），因为 call graph 邻居也不应作为 hard negatives\\n2. **选择信号**：dynamic mining 应使用当前 epoch 的 encoder embedding（不是 pretrained），这是 dynamic mining 的核心价值——所以 `DataFlowAwareMiner` 的 embedding→filter→BM25 三步法更合理，但需将排除范围从 1-hop dataflow 扩展到 full_connected\\n3. **具体改动**：修改 `DataFlowAwareMiner._is_reachable()` 使其也排除 call graph 连接，或在 `mine()` 中接受 `full_connected_set` 参数\\n\\n---\\n\\n## 运维经验 (2026-05-14)\\n\\n**Registry 状态机 workaround**：当长链训练（多 run 串行）中途因 cron timeout 或子进程退出导致 registry 状态误标（DONE/failed 或 ANALYZING），而实际训练仍在跑时，不可回退状态。解决方案：创建 `{exp_id}_resumed` / `{exp_id}_continued` 新 entry，步进 PREPARING→QUEUED→ALLOCATED→RUNNING，注册 cron 监控实际 PID。原 entry 保留历史 metrics。\\n\\n**Bash 预读陷阱**：运行中的 bash 脚本已将循环体/数组预读到内存，磁盘上修改脚本文件不影响执行。需要在链外设置独立 tmux watcher 监控链 PID 退出后手动触发后续任务。\\n\\n**BM25 Phase 2 触发机制**：两个 tmux watcher（`bm25_starcoder_watcher`, `bm25_qwen_watcher`）每 5 分钟检查链 PID 存活，退出后自动启动 BM25 脚本。watcher 启动的训练不经过 submit_training_job，需在链完成回调中补注册 cron。\\n\\n---\\n\\n## 关键决策记录\\n\\n**m1_reextract_v2 数据使用决策 (2026-05-14, Director Session 8)**：即使 reextract 将数据从 ~16K 增至 ~44K，不重跑 M2。原因：ARR May 25 DDL 不允许再加 4-5 天重训。处理方式：(1) post-M2 完成后若有 GPU 空档，跑 1-seed pilot (Qwen, embedding, 新数据) 对比当前 M2 baseline；(2) 论文中作为 scalability/data efficiency 讨论点；(3) 全量重训留 camera-ready。\", \"total_chars\": 12963, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 14_

<details><summary>Logged reasoning block</summary>

```text
Now I have the literature_map.yaml and memory.md. The discussion_v2.md is not accessible via the project file reader. Let me analyze what I have.

From literature_map.yaml, I can count the citations by category:

1. **code_retrieval_bug_fixing** (8 papers): SWE-bench, SWE-agent, AutoCodeRover, Agentless, SWE-smith, RepoBench, SweRank, SWE-Fixer
2. **hard_negative_mining** (6 papers): DPR, ANCE, SimCLR, Sentence-BERT, CL-DRD, CoCoHaNeRe


3. **contrastive_code_learning** (3 papers): ContraCode, CodeRetriever, Ding et al. ACL 2022
4. **program_analysis_for_ml** (7 papers): CodeQL, code2vec, code2seq, FA-AST, GraphCodeBERT, ARISE
5. **code_embeddings_search** (10 papers): CodeSearchNet, CodeBERT, UniXcoder, StarCoder, Code Llama, Qwen2.5-Coder, DeepSeek-Coder, RepoFusion, BM25
6. **graph_guided_inference** (5 papers): continuing through the remaining categories in the map

. For graph-guided inference, I'm looking at LocAgent, CodexGraph, RANGER, RepoGraph, and GraphCoder. Then infrastructure covers FAISS and Tree-sitter. Let me verify the total count across all eight categories adds up to 41 entries, though I should double-check my arithmetic on the earlier sections to make sure I haven't miscounted. Looking at the additional papers from memory.md that aren't in the YAML file, I'm seeing CodeRAG and CodeGRAG which would bring the total to around 41 references. The task requires 25+ citations and we're well above that, but I should verify whether all entries are proper academic papers versus tools or preprints. Now I'm identifying coverage gaps—contrastive learning methods only have 3 papers which seems thin, and while hard negative mining has decent coverage, there might be room for more code-specific approaches in that area. -specific ones
4. Static analysis / program analysis for ML (CodeQL, data-flow) - 6 papers including CodeQL tool
5. Code representation learning (CodeBERT, UniXcoder, StarCoder, etc.) - Well covered with 9 papers
6. Repository-level code understanding - Partially covered through SWE-bench ecosystem and graph methods
7. SWE-bench / software engineering benchmarks - Well covered with 8 papers
8. Inference-time graph methods - 5 in literature_map + 3 more in memory.md = 8 total

The task says they need 25+ and they already have 39, so the count isn't the issue. The issue is about coverage gaps in specific areas. Let me identify what's missing:

Gaps I can identify:
1. **Contrastive learning for code** - Only 3 papers.

I'm noticing several specific areas where the collection could be strengthened. Contrastive learning approaches like SynCoBERT are underrepresented, and the broader contrastive learning foundations (MoCo, InfoNCE beyond SimCLR) could be more comprehensive. Hard negative mining strategies, particularly techniques like RocketQA for cross-batch negatives, are missing entirely. There are also gaps in newer code representation models like InCoder and SantaCoder, repository-level understanding tools like RepoFormer, and embedding training techniques such as E5. I've identified the main gaps in coverage—contrastive learning for code, hard negative mining, dense retrieval methods for code search, and knowledge distillation for retrieval all need strengthening. Now I'm searching for papers that would fill these specific areas.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "7a0d3d79-59cb-4995-8afd-0941119d5426",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rrn8E3rgUj7R3oJnq51GjC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12628,
      "cache_read_input_tokens": 24257,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12628
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

_source line 15_

Current citation count is already 39 (including 2 tool references). Coverage is uneven across areas — let me search for papers to fill the gaps. Contrastive learning for code (3 papers) and general hard negative mining methodology are the thinnest areas.

Let me search for papers in the gap areas.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "e4ff1b37-6bc5-4439-83d6-d9a454927447",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rrn8E3rgUj7R3oJnq51GjC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12628,
      "cache_read_input_tokens": 24257,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12628
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

_source line 16_

<details open><summary>🔧 Tool call — Agent · `toolu_01JBrYzVEEU9YDuhmDfQg3z3`</summary>

```json
{
  "description": "Search gap area papers",
  "prompt": "I need to find real, verified academic papers to fill citation gaps for a paper about using code structure (call graph / data-flow) for contrastive learning hard negative mining in code retrieval. The paper already has 39 citations but needs better coverage in certain areas.\n\nSearch for the following papers using WebSearch. For each paper, confirm: title, authors, venue, year. Only return papers you can verify exist.\n\n**Area 1: Contrastive Learning for Code (need 2-3 more)**\n- Search: \"contrastive learning code representation 2022 2023 2024 ACL EMNLP ICLR NeurIPS\"\n- Look for: SynCoBERT, DISCO, or other contrastive code learning papers\n- Search: \"self-supervised code understanding contrastive pre-training\"\n\n**Area 2: Hard Negative Mining in Dense Retrieval (need 1-2 more)**\n- Search: \"RocketQA hard negative mining dense retrieval 2021\"\n- Search: \"hard negative mining contrastive learning survey 2023 2024\"\n- Search: \"debiased contrastive learning hard negatives retrieval\"\n\n**Area 3: Code Search / Dense Retrieval for Code (need 1-2)**\n- Search: \"dense code retrieval neural code search 2023 2024 ICSE FSE\"\n- Search: \"CoSQA code search question answering benchmark\"\n\n**Area 4: Repository-level Code Understanding (need 1-2)**\n- Search: \"repository level code understanding cross-file context 2024\"\n- Search: \"CrossCodeEval benchmark cross-file code completion\"\n\n**Area 5: Program Analysis meets Deep Learning (need 1)**\n- Search: \"ProGraML program graph machine learning 2021\"\n- Search: \"learning program semantics graph neural network ICML NeurIPS\"\n\n**Area 6: Training Data Quality / Curriculum for Retrieval (need 1)**\n- Search: \"data quality curriculum learning dense retrieval 2023 2024\"\n\nFor each paper found, provide:\n- Exact title\n- Authors (first 3 + et al.)\n- Venue and year\n- One sentence on why it's relevant to a paper about structure-grounded hard negative mining for code retrieval\n\nReturn a clean list grouped by area. Only include papers you verified via web search.",
  "model": "sonnet"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "95486ad5-6f6b-4c5e-82cb-1ddc83ada61b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rrn8E3rgUj7R3oJnq51GjC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12628,
      "cache_read_input_tokens": 24257,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12628
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

### System

_source line 17_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a7871f5d7a606af87",
  "tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "description": "Search gap area papers",
  "task_type": "local_agent",
  "prompt": "I need to find real, verified academic papers to fill citation gaps for a paper about using code structure (call graph / data-flow) for contrastive learning hard negative mining in code retrieval. The paper already has 39 citations but needs better coverage in certain areas.\n\nSearch for the following papers using WebSearch. For each paper, confirm: title, authors, venue, year. Only return papers you can verify exist.\n\n**Area 1: Contrastive Learning for Code (need 2-3 more)**\n- Search: \"contrastive learning code representation 2022 2023 2024 ACL EMNLP ICLR NeurIPS\"\n- Look for: SynCoBERT, DISCO, or other contrastive code learning papers\n- Search: \"self-supervised code understanding contrastive pre-training\"\n\n**Area 2: Hard Negative Mining in Dense Retrieval (need 1-2 more)**\n- Search: \"RocketQA hard negative mining dense retrieval 2021\"\n- Search: \"hard negative mining contrastive learning survey 2023 2024\"\n- Search: \"debiased contrastive learning hard negatives retrieval\"\n\n**Area 3: Code Search / Dense Retrieval for Code (need 1-2)**\n- Search: \"dense code retrieval neural code search 2023 2024 ICSE FSE\"\n- Search: \"CoSQA code search question answering benchmark\"\n\n**Area 4: Repository-level Code Understanding (need 1-2)**\n- Search: \"repository level code understanding cross-file context 2024\"\n- Search: \"CrossCodeEval benchmark cross-file code completion\"\n\n**Area 5: Program Analysis meets Deep Learning (need 1)**\n- Search: \"ProGraML program graph machine learning 2021\"\n- Search: \"learning program semantics graph neural network ICML NeurIPS\"\n\n**Area 6: Training Data Quality / Curriculum for Retrieval (need 1)**\n- Search: \"data quality curriculum learning dense retrieval 2023 2024\"\n\nFor each paper found, provide:\n- Exact title\n- Authors (first 3 + et al.)\n- Venue and year\n- One sentence on why it's relevant to a paper about structure-grounded hard negative mining for code retrieval\n\nReturn a clean list grouped by area. Only include papers you verified via web search.",
  "uuid": "46c4817a-b670-456a-b0d0-acdaf66f6362",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691"
}
```

---

## Round 1

97 recorded events

### User

_source line 18 · 2026-05-15T04:16:20.002Z_

I need to find real, verified academic papers to fill citation gaps for a paper about using code structure (call graph / data-flow) for contrastive learning hard negative mining in code retrieval. The paper already has 39 citations but needs better coverage in certain areas.

Search for the following papers using WebSearch. For each paper, confirm: title, authors, venue, year. Only return papers you can verify exist.

**Area 1: Contrastive Learning for Code (need 2-3 more)**
- Search: "contrastive learning code representation 2022 2023 2024 ACL EMNLP ICLR NeurIPS"
- Look for: SynCoBERT, DISCO, or other contrastive code learning papers
- Search: "self-supervised code understanding contrastive pre-training"

**Area 2: Hard Negative Mining in Dense Retrieval (need 1-2 more)**
- Search: "RocketQA hard negative mining dense retrieval 2021"
- Search: "hard negative mining contrastive learning survey 2023 2024"
- Search: "debiased contrastive learning hard negatives retrieval"

**Area 3: Code Search / Dense Retrieval for Code (need 1-2)**
- Search: "dense code retrieval neural code search 2023 2024 ICSE FSE"
- Search: "CoSQA code search question answering benchmark"

**Area 4: Repository-level Code Understanding (need 1-2)**
- Search: "repository level code understanding cross-file context 2024"
- Search: "CrossCodeEval benchmark cross-file code completion"

**Area 5: Program Analysis meets Deep Learning (need 1)**
- Search: "ProGraML program graph machine learning 2021"
- Search: "learning program semantics graph neural network ICML NeurIPS"

**Area 6: Training Data Quality / Curriculum for Retrieval (need 1)**
- Search: "data quality curriculum learning dense retrieval 2023 2024"

For each paper found, provide:
- Exact title
- Authors (first 3 + et al.)
- Venue and year
- One sentence on why it's relevant to a paper about structure-grounded hard negative mining for code retrieval

Return a clean list grouped by area. Only include papers you verified via web search.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "130aeb02-c099-4ea4-b155-8d6bcfd48296"
}
```

</details>

---

### System

_source line 19_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a7871f5d7a606af87",
  "tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "description": "Search gap area papers",
  "usage": {
    "total_tokens": 14523,
    "tool_uses": 1,
    "duration_ms": 1958
  },
  "last_tool_name": "ToolSearch",
  "uuid": "b1ece267-16f7-45df-9b00-b4c7a065a5e4",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691"
}
```

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Lp3bdxYp8fWoGyqESbhSK5`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "8bdaba05-4e4d-4876-bf57-852877c330d2",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01CU9qfBXkYHmGY7XvaHhuZj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14453,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14453,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 67,
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

_source line 21 · 2026-05-15T04:16:21.978Z_

<details><summary>↩ Tool result · `toolu_01Lp3bdxYp8fWoGyqESbhSK5`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "cc466e7f-2077-416c-81e8-99465c55e983"
}
```

</details>

---

### System

_source line 22_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a7871f5d7a606af87",
  "tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "description": "Searching for SynCoBERT contrastive learning code representatio…",
  "usage": {
    "total_tokens": 15964,
    "tool_uses": 2,
    "duration_ms": 4637
  },
  "last_tool_name": "WebSearch",
  "uuid": "0045b702-3715-4056-91cd-7678b3d5785f",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691"
}
```

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DdSBdgj9RppuxmeYpFoF6L`</summary>

```json
{
  "query": "SynCoBERT contrastive learning code representation 2022 ACL EMNLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "2842e24b-91f6-4dc6-90df-56586e5c0b9c",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01UFUuP9yvgjvcmK5nyz94nb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 14453,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1439,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 24_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a7871f5d7a606af87",
  "tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "description": "Searching for DISCO contrastive learning code understanding pre…",
  "usage": {
    "total_tokens": 15965,
    "tool_uses": 3,
    "duration_ms": 5021
  },
  "last_tool_name": "WebSearch",
  "uuid": "8b0b482a-4914-46de-8427-b9e47d36ea71",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691"
}
```

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QFbSjDcnS2Ef8eRR8sitRp`</summary>

```json
{
  "query": "DISCO contrastive learning code understanding pre-training 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "ba1839c5-5a5d-4095-98b0-4e03c5af15ee",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01UFUuP9yvgjvcmK5nyz94nb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 14453,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1439,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 26_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a7871f5d7a606af87",
  "tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "description": "Searching for RocketQA hard negative mining dense retrieval 202…",
  "usage": {
    "total_tokens": 15966,
    "tool_uses": 4,
    "duration_ms": 5405
  },
  "last_tool_name": "WebSearch",
  "uuid": "555aea29-13c3-4069-a069-c48adb4f85c5",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691"
}
```

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012V5eUnKcL4Rfa3uERiAyUQ`</summary>

```json
{
  "query": "RocketQA hard negative mining dense retrieval 2021 NAACL"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "14f32dea-bd6d-4a09-b1f4-c9004c737f04",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01UFUuP9yvgjvcmK5nyz94nb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 14453,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1439,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 28_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a7871f5d7a606af87",
  "tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "description": "Searching for CoSQA code search question answering benchmark 20…",
  "usage": {
    "total_tokens": 15967,
    "tool_uses": 5,
    "duration_ms": 5421
  },
  "last_tool_name": "WebSearch",
  "uuid": "90628306-4244-43fd-8135-414202538fab",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691"
}
```

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PgR2DJ7M64LqoprVdfDFdS`</summary>

```json
{
  "query": "CoSQA code search question answering benchmark 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "4581e0a2-4d31-421f-a45d-fc84db28e2ee",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01UFUuP9yvgjvcmK5nyz94nb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 14453,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1439,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 30_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a7871f5d7a606af87",
  "tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "description": "Searching for CrossCodeEval benchmark cross-file code completio…",
  "usage": {
    "total_tokens": 15968,
    "tool_uses": 6,
    "duration_ms": 5786
  },
  "last_tool_name": "WebSearch",
  "uuid": "ec93666c-e782-46eb-86fa-e9d3afaff23f",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691"
}
```

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01H4jckwhCzwARF24rTDGnVx`</summary>

```json
{
  "query": "CrossCodeEval benchmark cross-file code completion 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "79689ad0-b5dd-4aef-926a-62ffdd53ca3a",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01UFUuP9yvgjvcmK5nyz94nb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 14453,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1439,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 32_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a7871f5d7a606af87",
  "tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "description": "Searching for ProGraML program graph machine learning ICML 2021",
  "usage": {
    "total_tokens": 15969,
    "tool_uses": 7,
    "duration_ms": 6071
  },
  "last_tool_name": "WebSearch",
  "uuid": "f04b7f31-9fbf-486b-be80-1868f60a1a8f",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691"
}
```

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EaqbhHE4QzKUF8gm6vVpqd`</summary>

```json
{
  "query": "ProGraML program graph machine learning ICML 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "e5c9e3c1-29be-4822-ab82-e03912492cfd",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01UFUuP9yvgjvcmK5nyz94nb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 14453,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1439,
        "ephemeral_1h_input_tokens": 0
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

_source line 34 · 2026-05-15T04:16:31.276Z_

<details><summary>↩ Tool result · `toolu_01DdSBdgj9RppuxmeYpFoF6L`</summary>

```text
Web search results for query: "SynCoBERT contrastive learning code representation 2022 ACL EMNLP"

Links: [{"title":"[2108.04556] SynCoBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation","url":"https://arxiv.org/abs/2108.04556"},{"title":"[2108.04556] SynCoBERT: Syntax-Enhanced Contrastive Pre-Training for Code Representation","url":"https://ar5iv.labs.arxiv.org/html/2108.04556"},{"title":"[PDF] SynCoBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/SynCoBERT:-Syntax-Guided-Multi-Modal-Contrastive-Wang-Wang/14b104d1a1c0b784e4e74454d809455cc47d0093"},{"title":"[2108.04556v3] SynCoBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation","url":"https://arxiv.org/abs/2108.04556v3"},{"title":"SynCoBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation · Machine Learning for Big Code and Naturalness","url":"https://ml4code.github.io/publications/wang2021syncobert/"},{"title":"(PDF) SynCoBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation","url":"https://www.academia.edu/73281297/SynCoBERT_Syntax_Guided_Multi_Modal_Contrastive_Pre_Training_for_Code_Representation"},{"title":"SynCoBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation - ADS","url":"https://ui.adsabs.harvard.edu/abs/2021arXiv210804556W/abstract"},{"title":"SynCoBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation | DeepAI","url":"https://deepai.org/publication/syncobert-syntax-guided-multi-modal-contrastive-pre-training-for-code-representation"},{"title":"Uncertainty-Aware Contrastive Learning With Hard Negative Sampling for","url":"https://ojs.aaai.org/index.php/AAAI/article/view/34070/36225"},{"title":"SYNCOBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for","url":"https://arxiv.org/pdf/2108.04556"}]

Based on the search results, here's what I found about SynCoBERT:

## Overview

SynCoBERT is a syntax-guided multi-modal contrastive pre-training approach for better code representations.

## Key Components

The approach designs two novel pre-training objectives originating from the symbolic and syntactic properties of source code: Identifier Prediction (IP) and AST Edge Prediction (TEP), which are designed to predict identifiers and edges between two nodes of AST, respectively.

To exploit the complementary information in semantically equivalent modalities (i.e., code, comment, AST), the paper proposes a multi-modal contrastive learning strategy to maximize the mutual information among different modalities.

## Performance

Extensive experiments on four downstream tasks related to code intelligence show that SynCoBERT advances the state-of-the-art with the same pre-training corpus and model size.

## Publication

The paper was published on arXiv in August-September 2021 (preprint version 2108.04556). Note that the search results indicate this is primarily an arXiv paper from 2021. While you mentioned it in relation to 2022 ACL/EMNLP venues, the results show the paper's initial publication was in 2021.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "9fd4ec4f-11b8-49e9-8b83-2271aa806ca9"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-15T04:16:32.407Z_

<details><summary>↩ Tool result · `toolu_01EaqbhHE4QzKUF8gm6vVpqd`</summary>

```text
Web search results for query: "ProGraML program graph machine learning ICML 2021"

Links: [{"title":"GitHub - ChrisCummins/ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations · GitHub","url":"https://github.com/ChrisCummins/ProGraML"},{"title":"ICML 2021 ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations Spotlight","url":"https://icml.cc/virtual/2021/spotlight/8886"},{"title":"PROGRAML: A Graph-based Program Representation for Data Flow Analysis","url":"https://chriscummins.cc/pub/2021-icml.pdf"},{"title":"Downloads 2021","url":"https://icml.cc/Downloads/2021"},{"title":"ICML 2021 Schedule","url":"https://icml.cc/virtual/2021/calendar"},{"title":"Machine Learning for Software Engineering papers at ICML 2021 · GitHub","url":"https://gist.github.com/bzz/38cfef2e735393a5ccf59f70ddff77d0"},{"title":"ProGraML: Graph-based Deep Learning for Program Optimization and Analysis.","url":"https://spcl.inf.ethz.ch/Publications/.pdf/programl-icml21-slides.pdf"},{"title":"[2003.10536] ProGraML: Graph-based Deep Learning for Program Optimization and Analysis","url":"https://arxiv.org/abs/2003.10536"},{"title":"PROGRAML: GRAPH-BASED DEEP LEARNING FOR PROGRAM OPTIMIZATION AND ANALYSIS","url":"https://arxiv.org/pdf/2003.10536"},{"title":"ICML: International Conference on Machine Learning 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=1421"}]

I've found comprehensive information about ProGraML from ICML 2021. Here are the key findings:

## Overview

ProGraML - Program Graphs for Machine Learning - is a language-independent, portable representation of program semantics. ProGraML is a representation for programs as input to a machine learning model.

## Key Features

The system supports several programming languages (C, C++, LLVM-IR, XLA) and several graph formats (NetworkX, DGL, Graphviz, JSON) out of the box. It captures every control, data, and call relation across entire programs.

## Technical Approach

ProGraML is a novel graph-based program representation using a low level, language agnostic, and portable format, and the representation is a directed attributed multigraph that captures control, data, and call relations, and summarizes instruction and operand types and ordering.

## Performance Results

On a benchmark dataset of 250k LLVM-IR files covering six source programming languages, ProGraML achieves an average 94.0 F1 score, significantly outperforming the state-of-the-art approaches.

## Publication Details

The paper was published at the Thirty-eighth International Conference on Machine Learning (ICML) in 2021 by authors Cummins, Chris, Fisches, Zacharias, Ben-Nun, Tal, Hoefler, Torsten, O'Boyle, Michael and Leather, Hugh.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "74af7201-ef3d-4a56-990c-1700e72529b1"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-15T04:16:32.481Z_

<details><summary>↩ Tool result · `toolu_01QFbSjDcnS2Ef8eRR8sitRp`</summary>

```text
Web search results for query: "DISCO contrastive learning code understanding pre-training 2023"

Links: [{"title":"DisCo: Graph-Based Disentangled Contrastive Learning for Cold-Start Cross-Domain Recommendation","url":"https://arxiv.org/html/2412.15005v1"},{"title":"GitHub - xrenaa/DisCo: [ICLR2022] Code for \"Learning Disentangled Representation by Exploiting Pretrained Generative Models: A Contrastive Learning View\"","url":"https://github.com/xrenaa/DisCo"},{"title":"DisCo: Graph-Based Disentangled Contrastive Learning for Cold-Start","url":"https://arxiv.org/pdf/2412.15005"},{"title":"GitHub - KingGugu/DA-CL-4Rec: The latest research progress of Contrastive Learning(CL), Data Augmentation(DA) and Self-Supervised Learning(SSL) in Recommender Systems · GitHub","url":"https://github.com/KingGugu/DA-CL-4Rec"},{"title":"Contrastive Representation Learning | Lil'Log","url":"https://lilianweng.github.io/posts/2021-05-31-contrastive/"},{"title":"[2412.15005] DisCo: Graph-Based Disentangled Contrastive Learning for Cold-Start Cross-Domain Recommendation","url":"https://ar5iv.labs.arxiv.org/html/2412.15005"},{"title":"CONTRASTIVE CODE REPRESENTATION LEARNING","url":"https://openreview.net/pdf?id=uV7hcsjqM-"},{"title":"GitHub - YuanchenBei/Awesome-Cold-Start-Recommendation: [Up-to-date] A curated list of resources on cold-start recommendations. · GitHub","url":"https://github.com/YuanchenBei/Awesome-Cold-Start-Recommendation"},{"title":"Advanced code time complexity prediction approach using contrastive learning - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0952197625006311"},{"title":"DiSCo: Disrupting Semantic Consistency for Transferable Cross-Modal Adversarial Attacks | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-981-95-6957-1_2"}]

Based on the search results, I found relevant information about code-related contrastive learning research. Here are the key findings:

## ContraCode: Contrastive Code Representation Learning

ContraCode is a self-supervised representation learning algorithm that uses source-to-source compiler transformation techniques (e.g., dead code elimination, obfuscation and constant folding) to generate syntactically diverse but functionally equivalent programs, using these equivalent programs to construct a challenging discriminative pretext task.

ContraCode learns representations with contrastive learning by training the network to find equivalent programs among many distractors, encoding semantics into the representation. This work was inspired by the success of pre-training in natural language processing, with recent work using self-supervision to learn code representations.

## Other Code Understanding Approaches

The search also revealed other contrastive learning approaches for code understanding. One approach proposes a training strategy based on contrastive learning, leveraging the observation that solution codes for the same problem typically have similar time complexities, enabling models to capture core algorithmic features such as loops and recursion more accurately.

The search results don't show a specific paper titled "DISCO" focused on code understanding pre-training from 2023, but the ContraCode paper represents a major contribution to contrastive learning for code representation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "f88f2caf-34d1-40e2-b815-c405fa57df27"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-15T04:16:32.492Z_

<details><summary>↩ Tool result · `toolu_01PgR2DJ7M64LqoprVdfDFdS`</summary>

```text
Web search results for query: "CoSQA code search question answering benchmark 2021"

Links: [{"title":"CoSQA: 20,000+ Web Queries for Code Search and Question Answering - ADS","url":"https://ui.adsabs.harvard.edu/abs/2021arXiv210513239H/abstract"},{"title":"CoSQA: 20,000+ Web Queries for Code Search and Question Answering - ACL Anthology","url":"https://aclanthology.org/2021.acl-long.442/"},{"title":"GitHub - Jun-jie-Huang/CoCLR: Source Code for ACL-21 main conference paper \"CoSQA: 20,000+ Web Queries for Code Search and Question Answering\".","url":"https://github.com/Jun-jie-Huang/CoCLR"},{"title":"[2105.13239] CoSQA: 20,000+ Web Queries for Code Search and Question Answering","url":"https://arxiv.org/abs/2105.13239"},{"title":"[2105.13239v1] CoSQA: 20,000+ Web Queries for Code Search and Question Answering","url":"https://arxiv.org/abs/2105.13239v1"},{"title":"CoSQA: 20,000+ Web Queries for Code Search and Question Answering - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/cosqa-20-000-web-queries-for-code-search-and-question-answering/"},{"title":"CoSQA+: Pioneering the Multi-Choice Code Search Benchmark with Test-Driven Agents","url":"https://arxiv.org/html/2406.11589v4"},{"title":"CoSQA: 20,000+ Web Queries for Code Search and Question Answering","url":"https://arxiv.org/pdf/2105.13239"},{"title":"CoSQA: 20,000+ Web Queries for Code Search and Question Answering","url":"https://gengo.sotaro.io/2021.acl-long.442"},{"title":"CoSQA+: Enhancing Code Search Evaluation with a Multi-Choice Benchmark and Test-Driven Agents","url":"https://arxiv.org/html/2406.11589"}]

I found comprehensive information about the CoSQA benchmark. Here are the key details:

## CoSQA: Code Search and Question Answering Benchmark (2021)

CoSQA is titled "20,000+ Web Queries for Code Search and Question Answering" and was published in the Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing in 2021.

### Dataset Overview

The dataset includes 20,604 labels for pairs of natural language queries and codes, each annotated by at least 3 human annotators. The motivation behind this work is that finding codes given natural language query is beneficial to the productivity of software developers, and future progress towards better semantic matching between query and code requires richer supervised training resources.

### Key Contributions

The authors introduced a contrastive learning method dubbed CoCLR to enhance text-code matching, which works as a data augmenter to bring more artificially generated training instances.

### Performance Results

Training on CoSQA improves the accuracy of code question answering by 5.1% when evaluated on CodeXGLUE with the same CodeBERT model, and incorporating CoCLR brings a further improvement of 10.5%.

### Authors

The paper was authored by Junjie Huang, Duyu Tang, Linjun Shou, Ming Gong, Ke Xu, Daxin Jiang, Ming Zhou, and Nan Duan.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "b2492d18-e000-4d94-9763-a035551f98fe"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-15T04:16:32.846Z_

<details><summary>↩ Tool result · `toolu_01H4jckwhCzwARF24rTDGnVx`</summary>

```text
Web search results for query: "CrossCodeEval benchmark cross-file code completion 2024"

Links: [{"title":"[2310.11248] CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion","url":"https://arxiv.org/abs/2310.11248"},{"title":"CrossCodeEval","url":"https://crosscodeeval.github.io/"},{"title":"GitHub - amazon-science/cceval: CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion (NeurIPS 2023)","url":"https://github.com/amazon-science/cceval"},{"title":"NeurIPS Poster CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion","url":"https://neurips.cc/virtual/2023/poster/73423"},{"title":"A Diverse and Multilingual Benchmark for Cross-File Code ...","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/920f2dced7d32ab2ba2f1970bc306af6-Paper-Datasets_and_Benchmarks.pdf"},{"title":"STALL+: Boosting LLM-based Repository-level Code Completion","url":"https://mingwei-liu.github.io/assets/pdf/arxiv2024STALL.pdf"},{"title":"CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion | OpenReview","url":"https://openreview.net/forum?id=wgDcbBMSfh"},{"title":"[PDF] CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CrossCodeEval:-A-Diverse-and-Multilingual-Benchmark-Ding-Wang/f1bd7ea3a63b78a60b5d90d91fdb4a1d7ac0de8e"},{"title":"RepoMasterEval: Evaluating Code Completion via Real-World Repositories","url":"https://arxiv.org/pdf/2408.03519"},{"title":"dblp: CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion.","url":"https://dblp.org/rec/journals/corr/abs-2310-11248.html"}]

Based on the search results, here's what I found about CrossCodeEval:

## Overview

CrossCodeEval is a diverse and multilingual code completion benchmark that necessitates an in-depth cross-file contextual understanding to complete the code accurately.

## Purpose and Design

Current popular evaluation datasets, such as HumanEval and MBPP, predominantly focus on code completion tasks within a single file, falling short of representing the real-world software development scenario where repositories span multiple files with numerous cross-file dependencies.

CrossCodeEval is built on a diverse set of real-world, open-sourced, permissively-licensed repositories in four popular programming languages: Python, Java, TypeScript, and C#.

## Methodology

To create examples that strictly require cross-file context for accurate completion, the benchmark uses a straightforward yet efficient static-analysis-based approach to pinpoint the use of cross-file context within the current file.

## Key Findings

Extensive experiments on state-of-the-art code language models like CodeGen and StarCoder demonstrate that CrossCodeEval is extremely challenging when the relevant cross-file context is absent, with clear improvements when adding this context into the prompt.

However, despite such improvements, the pinnacle of performance remains notably unattained even with the highest-performing model, indicating that CrossCodeEval is also capable of assessing model's capability in leveraging extensive context to make better code completion.

This repository contains the data and inference code of the NeurIPS 2023 (Datasets and Benchmarks track) paper "CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion."


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "7714e933-5322-495a-9a50-25b4d090cc15"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-15T04:16:37.163Z_

<details><summary>↩ Tool result · `toolu_012V5eUnKcL4Rfa3uERiAyUQ`</summary>

```text
Web search results for query: "RocketQA hard negative mining dense retrieval 2021 NAACL"

Links: [{"title":"Research/NLP/NAACL2021-RocketQA at master · PaddlePaddle/Research","url":"https://github.com/PaddlePaddle/Research/tree/master/NLP/NAACL2021-RocketQA"},{"title":"RocketQA/research/RocketQA_NAACL2021 at main · PaddlePaddle/RocketQA","url":"https://github.com/PaddlePaddle/RocketQA/tree/main/research/RocketQA_NAACL2021"},{"title":"RocketQA: An Optimized Training Approach to Dense Passage Retrieval for Open-Domain Question Answering - ACL Anthology","url":"https://aclanthology.org/2021.naacl-main.466/"},{"title":"(PDF) RocketQA: An Optimized Training Approach to Dense Passage Retrieval for Open-Domain Question Answering","url":"https://www.academia.edu/75599741/RocketQA_An_Optimized_Training_Approach_to_Dense_Passage_Retrieval_for_Open_Domain_Question_Answering"},{"title":"Hard Negative Mining for Domain-Specific Retrieval in ...","url":"https://arxiv.org/pdf/2505.18366"},{"title":"RocketQA: An Optimized Training Approach to Dense ...","url":"https://aclanthology.org/2021.naacl-main.466.pdf"},{"title":"RocketQA: An Optimized Training Approach to Dense Passage Retrieval for Open-Domain Question Answering | Request PDF","url":"https://www.researchgate.net/publication/352364344_RocketQA_An_Optimized_Training_Approach_to_Dense_Passage_Retrieval_for_Open-Domain_Question_Answering"},{"title":"RocketQA: An Optimized Training Approach to Dense Passage Retrieval for Open-Domain Question Answering - ADS","url":"https://ui.adsabs.harvard.edu/abs/2020arXiv201008191Q/abstract"},{"title":"GitHub - PaddlePaddle/RocketQA: 🚀 RocketQA, dense retrieval for information retrieval and question answering, including both Chinese and English state-of-the-art models.","url":"https://github.com/PaddlePaddle/RocketQA"},{"title":"Hard Negative Mining for Domain-Specific Retrieval in ...","url":"https://aclanthology.org/2025.acl-industry.72.pdf"}]

Based on the search results, here's what I found about RocketQA:

## Overview
RocketQA is an optimized training approach to dense passage retrieval for open-domain question answering, presented at the 2021 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL).

## Key Technical Contributions
RocketQA makes three major technical contributions: cross-batch negatives, denoised hard negatives, and data augmentation. 

The denoised hard negative sampling is particularly relevant to your query on hard negative mining. RocketQA incorporated cross-batch negatives and a sophisticated "denoised" hard negative filtering technique using a cross-encoder.

## Performance
The experiment results show that RocketQA significantly outperforms previous state-of-the-art models on both MSMARCO and Natural Questions.

## Training Pipeline
In the implementation of training dual-encoder models, each instance contains 1 query with 1 positive passage and 1 hard negative passage.

The paper was authored by Yingqi Qu, Yuchen Ding, Jing Liu, Kai Liu, Ruiyang Ren, Wayne Xin Zhao, Daxiang Dong, Hua Wu, and Haifeng Wang.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "99031b17-212b-4698-8830-5a5a2da6dd7b"
}
```

</details>

---

### System

_source line 40_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a7871f5d7a606af87",
  "tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "description": "Searching for ContraCode contrastive learning code representati…",
  "usage": {
    "total_tokens": 22062,
    "tool_uses": 8,
    "duration_ms": 19372
  },
  "last_tool_name": "WebSearch",
  "uuid": "39fde846-69cd-4591-b87f-f1c28d91eb20",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691"
}
```

---

### Tool call

_source line 41_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018VH3N3VfCyP8tUQL2kmhNi`</summary>

```json
{
  "query": "ContraCode contrastive learning code representation self-supervised 2022 ICLR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "7982fa0b-f802-46ef-b745-c94b2c4e9bdd",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01GEAA2aCF1jqjhwtXhW1evT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2790,
      "cache_creation_input_tokens": 3267,
      "cache_read_input_tokens": 15892,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3267,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
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

### System

_source line 42_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a7871f5d7a606af87",
  "tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "description": "Searching for hard negative mining contrastive learning survey …",
  "usage": {
    "total_tokens": 22101,
    "tool_uses": 9,
    "duration_ms": 19758
  },
  "last_tool_name": "WebSearch",
  "uuid": "47fb2a88-8b8f-4580-b6ae-1f9515a7d218",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691"
}
```

---

### Tool call

_source line 43_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XqFzfPj3UnWnpNVxbQD4vw`</summary>

```json
{
  "query": "hard negative mining contrastive learning survey dense retrieval 2023 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "165f687a-e12c-4c42-8d25-02f7fbc7bb5b",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01GEAA2aCF1jqjhwtXhW1evT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2790,
      "cache_creation_input_tokens": 3267,
      "cache_read_input_tokens": 15892,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3267,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
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

### System

_source line 44_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a7871f5d7a606af87",
  "tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "description": "Searching for repository level code understanding cross-file co…",
  "usage": {
    "total_tokens": 22140,
    "tool_uses": 10,
    "duration_ms": 20552
  },
  "last_tool_name": "WebSearch",
  "uuid": "efc339d2-e79d-4597-9b8b-785b363b4bc6",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691"
}
```

---

### Tool call

_source line 45_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017cVq7SWRXeaztJ1fPey4aL`</summary>

```json
{
  "query": "repository level code understanding cross-file context LLM 2024 ICSE FSE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "48b6f22b-de0c-41c1-a477-c88e998819f7",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01GEAA2aCF1jqjhwtXhW1evT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2790,
      "cache_creation_input_tokens": 3267,
      "cache_read_input_tokens": 15892,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3267,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
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

### System

_source line 46_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a7871f5d7a606af87",
  "tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "description": "Searching for curriculum learning data quality dense retrieval …",
  "usage": {
    "total_tokens": 22179,
    "tool_uses": 11,
    "duration_ms": 21033
  },
  "last_tool_name": "WebSearch",
  "uuid": "084e9616-995d-4a7b-94fd-7c6d8f5a3e21",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691"
}
```

---

### Tool call

_source line 47_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011xNfG559Ja11Fvsn6weXi6`</summary>

```json
{
  "query": "curriculum learning data quality dense retrieval training 2023 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "0a80eefb-5b15-46de-b4d6-217b6c531458",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01GEAA2aCF1jqjhwtXhW1evT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2790,
      "cache_creation_input_tokens": 3267,
      "cache_read_input_tokens": 15892,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3267,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
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

### System

_source line 48_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a7871f5d7a606af87",
  "tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "description": "Searching for dense neural code search retrieval 2023 2024 ICSE…",
  "usage": {
    "total_tokens": 22218,
    "tool_uses": 12,
    "duration_ms": 21513
  },
  "last_tool_name": "WebSearch",
  "uuid": "73af317e-932b-4a41-84ed-9f7f9c1d8bef",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691"
}
```

---

### Tool call

_source line 49_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BW8WFbfP5Agg6jhnHDmZwQ`</summary>

```json
{
  "query": "dense neural code search retrieval 2023 2024 ICSE FSE ASE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "88bf03de-8008-42db-87c9-c4bfbf28565a",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01GEAA2aCF1jqjhwtXhW1evT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2790,
      "cache_creation_input_tokens": 3267,
      "cache_read_input_tokens": 15892,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3267,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
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

_source line 50 · 2026-05-15T04:16:46.127Z_

<details><summary>↩ Tool result · `toolu_018VH3N3VfCyP8tUQL2kmhNi`</summary>

```text
Web search results for query: "ContraCode contrastive learning code representation self-supervised 2022 ICLR"

Links: [{"title":"Contrastive Code Representation Learning | OpenReview","url":"https://openreview.net/forum?id=uV7hcsjqM-"},{"title":"CONTRASTIVE CODE REPRESENTATION LEARNING","url":"https://openreview.net/pdf?id=uV7hcsjqM-"},{"title":"GitHub - parasj/contracode: Contrastive Code Representation Learning: functionality-based JavaScript embeddings through self-supervised learning","url":"https://github.com/parasj/contracode"},{"title":"Contrastive Code Representation Learning","url":"https://parasj.github.io/contracode/"},{"title":"(PDF) Contrastive Code Representation Learning","url":"https://www.researchgate.net/publication/342829858_Contrastive_Code_Representation_Learning"},{"title":"[PDF] Contrastive Code Representation Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Contrastive-Code-Representation-Learning-Jain-Jain/021bbcefc993c389bad6c1daefd8ff92d0fc2441"},{"title":"Contrastive Code Representation Learning · Machine Learning for Big Code and Naturalness","url":"https://ml4code.github.io/publications/jain2020contrastive/"},{"title":"Contrastive Code Representation Learning","url":"https://aclanthology.org/2021.emnlp-main.482.pdf"},{"title":"Contrastive Code Representation Learning","url":"https://arxiv.org/pdf/2007.04973v3"},{"title":"CONTRASTIVE CODE REPRESENTATION LEARNING","url":"https://www.arxiv.org/pdf/2007.04973v2"}]

Based on the search results, here's what I found about ContraCode:

## ContraCode: Contrastive Code Representation Learning

ContraCode is a self-supervised algorithm for learning task-agnostic semantic representations of programs via contrastive learning. The approach learns to represent programs in a self-supervised manner by using compiler transformations as data augmentations.

### Key Methodology

ContraCode optimizes for a representation that is invariant to semantic-preserving code transformations, developing an automated source-to-source compiler that generates textually divergent variants of source programs, then training a neural network to identify variants of anchor programs within a large batch of non-equivalent negatives.

### Training and Results

ContraCode is pre-trained with 1.8M unannotated JavaScript methods mined from GitHub, then transferred to downstream tasks by fine-tuning. Pre-training with ContraCode consistently improves the F1 score of code summarization baselines and top-1 accuracy of type inference baselines by 2% to 13%. ContraCode achieves 9% higher top-1 accuracy than the current state-of-the-art static type analyzer for TypeScript.

**Note:** The search results indicate this work was published at EMNLP 2021, rather than ICLR 2022 as mentioned in your query.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "50bd111d-2769-431a-8b61-dec51df2bf1e"
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-15T04:16:47.809Z_

<details><summary>↩ Tool result · `toolu_011xNfG559Ja11Fvsn6weXi6`</summary>

```text
Web search results for query: "curriculum learning data quality dense retrieval training 2023 2024"

Links: [{"title":"[PDF] Curriculum Learning for Dense Retrieval Distillation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Curriculum-Learning-for-Dense-Retrieval-Zeng-Zamani/58aa3467505e900f76fb2295f2f94d60c70a65e2"},{"title":"Curriculum Learning with Quality-Driven Data Selection","url":"https://arxiv.org/pdf/2407.00102"},{"title":"Curriculum Learning with Quality-Driven Data Selection","url":"https://www.researchgate.net/publication/381882368_Curriculum_Learning_with_Quality-Driven_Data_Selection"},{"title":"[2204.13679] Curriculum Learning for Dense Retrieval Distillation","url":"https://arxiv.org/abs/2204.13679"},{"title":"[2204.13679v1] Curriculum Learning for Dense Retrieval Distillation","url":"https://arxiv.org/abs/2204.13679v1"},{"title":"Learning More Effective Representations for Dense Retrieval through Deliberate Thinking Before Search","url":"https://arxiv.org/html/2502.12974v1"},{"title":"Dense Retrieval: Principles & Applications","url":"https://www.emergentmind.com/topics/dense-retrieval-dr"},{"title":"CAPSTONE: Curriculum Sampling for Dense Retrieval with Document Expansion - ACL Anthology","url":"https://aclanthology.org/2023.emnlp-main.651/"},{"title":"[2407.00102] Curriculum Learning with Quality-Driven Data Selection","url":"https://arxiv.org/abs/2407.00102"},{"title":"Curriculum Learning for Dense Retrieval Distillation Hansi Zeng","url":"https://arxiv.org/pdf/2204.13679"}]

Based on the search results, here are the key findings on curriculum learning, data quality, and dense retrieval training from 2023-2024:

## Curriculum Learning for Dense Retrieval

A curriculum learning framework called CL-DRD controls the difficulty level of training data by iteratively optimizing the dense retrieval (student) model by increasing the difficulty of knowledge distillation data made available to it. The approach initially provides the student model coarse-grained preference pairs between documents in the teacher's ranking and progressively moves towards finer-grained pairwise document ordering requirements.

## Quality-Driven Data Selection

Current methodologies for data selection often rely on single, unreliable scores or use downstream tasks for selection, which is time-consuming. To mitigate these limitations, a novel data selection methodology utilizes image-text correlation and model perplexity to evaluate and select data of varying quality.

## CAPSTONE: Curriculum Sampling Strategy

A curriculum sampling strategy utilizes pseudo queries during training and progressively enhances the relevance between the generated query and the real query, allowing the retrieval model to learn to extend its attention from the document alone to both the document and query, resulting in high-quality query-informed document representations.

## Cross-Domain Enhancement

Enhanced cross-domain transfer through disentanglement, adversarial invariance, meta-learning and curriculum-oriented negative and synthetic data generation has been explored in recent research.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "9ef3a9eb-1954-4479-b73a-179fe032fa2c"
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-15T04:16:47.878Z_

<details><summary>↩ Tool result · `toolu_01XqFzfPj3UnWnpNVxbQD4vw`</summary>

```text
Web search results for query: "hard negative mining contrastive learning survey dense retrieval 2023 2024"

Links: [{"title":"Hard Negative Mining for Domain-Specific Retrieval in ...","url":"https://arxiv.org/pdf/2505.18366"},{"title":"Effective Hard Negative Mining for Contrastive Learning-Based Code Search | ACM Transactions on Software Engineering and Methodology","url":"https://dl.acm.org/doi/10.1145/3695994"},{"title":"Negative Sampling Techniques in Information Retrieval: A Survey","url":"https://arxiv.org/html/2603.18005"},{"title":"Revisiting Hard Negative Mining in Contrastive Learning for Visual Understanding","url":"https://www.mdpi.com/2079-9292/12/23/4884"},{"title":"Negative Sampling Techniques for Dense Passage Retrieval ...","url":"https://staff.fnwi.uva.nl/m.derijke/wp-content/papercite-data/pdf/rajapakse-2024-study.pdf"},{"title":"NV-Retriever: Improving text embedding models with effective","url":"https://arxiv.org/pdf/2407.15831"},{"title":"Hard Negative Mining for Domain-Specific Retrieval in Enterprise Systems","url":"https://arxiv.org/html/2505.18366v1"},{"title":"Positive and Negative Sampling Strategies for Representation Learning in Semantic Search - Sumit's Diary","url":"https://blog.reachsumit.com/posts/2023/03/pairing-for-representation/"},{"title":"A Hard Negatives Mining and Enhancing Method for Multi-Modal Contrastive Learning","url":"https://www.mdpi.com/2079-9292/14/4/767"},{"title":"Towards Expansive and Adaptive Hard Negative Mining: Graph Contrastive Learning via Subspace Preserving | Proceedings of the ACM Web Conference 2024","url":"https://dl.acm.org/doi/10.1145/3589334.3645327"}]

I found several relevant resources on hard negative mining for contrastive learning and dense retrieval from 2023-2024. Here's a summary of what the search revealed:

## Survey and Overview Papers

A recent survey on negative sampling techniques provides systematic analysis of negative sampling for contrastive learning, examining the critical false negative problem and mitigation strategies. This comprehensive survey appears to be from early 2026 and covers multiple approaches.

## Key Techniques in Hard Negative Mining

Cluster-Based sampling mines hard negatives from different semantic clusters to ensure diversity, while TriSampler samples negatives from a quasi-triangular region to ensure uniform gradients.

ANCE (Approximate nearest neighbor negative contrastive estimation) is a technique that aims to improve the effectiveness of dense retrievers by using hard negatives during training.

## Addressing False Negatives

An important challenge in hard negative mining is the false negative problem. Studies found that naive mining of hard negatives may select many false negatives—approximately 70% of passages most similar to queries in the MS-MARCO dataset should be actually labeled as positive.

Mitigation strategies include Top-k Filtering, which assumes the top-k most relevant potential negatives are false negatives and ignores them, and Denoised Hard Negatives, which explicitly filters false negatives using a cross-encoder or LLM.

## Recent Applications (2024)

NV-Retriever improves text embedding models with effective hard-negative mining, and TriSampler provides a better negative sampling principle for dense retrieval.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "aa78bfef-f50d-441e-b966-de137c7f34e1"
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-15T04:16:48.837Z_

<details><summary>↩ Tool result · `toolu_01BW8WFbfP5Agg6jhnHDmZwQ`</summary>

```text
Web search results for query: "dense neural code search retrieval 2023 2024 ICSE FSE ASE"

Links: [{"title":"ESEC/FSE 2023 - Research Papers - ESEC/FSE 2023","url":"https://2023.esec-fse.org/track/fse-2023-research-papers"},{"title":"GitHub - saltudelft/ml4se: A curated list of papers, theses, datasets, and tools related to the application of Machine Learning for Software Engineering · GitHub","url":"https://github.com/saltudelft/ml4se"},{"title":"GitHub - iSEngLab/AwesomeLLM4SE: [SCIS 2025] A Survey on Large Language Models for Software Engineering · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4SE"},{"title":"A Systematic Literature Review on Large Language Models","url":"https://arxiv.org/pdf/2405.01466"},{"title":"A Survey of Model Architectures in Information Retrieval","url":"https://arxiv.org/html/2502.14822v2"},{"title":"FSE 2024 - Research Papers - FSE 2024","url":"https://2024.esec-fse.org/track/fse-2024-research-papers"},{"title":"ICSE Home Page","url":"https://www.icse-conferences.org/"},{"title":"1 Large Language Models for Software Engineering:","url":"https://nzjohng.github.io/publications/papers/tosem2024_5.pdf"},{"title":"Retrieval-based Neural Source Code Summarization (ICSE 2020 - Technical Papers) - ICSE 2020","url":"https://conf.researchr.org/details/icse-2020/icse-2020-papers/90/Retrieval-based-Neural-Source-Code-Summarization"},{"title":"FSE 2025 - Research Papers - FSE 2025 - conf.researchr.org","url":"https://conf.researchr.org/track/fse-2025/fse-2025-research-papers"}]

Based on the web search results, here are relevant papers on dense neural code search and retrieval from 2023-2024 published at ICSE, FSE, and ASE conferences:

## Code Search and Retrieval Papers (2023-2024)

**Efficient Text-to-Code Retrieval with Cascaded Fast and Slow Transformer Models** (2023), FSE'23, by Gotmare, A., et al.

**GraphSearchNet: Enhancing GNNs via capturing global dependencies for semantic code search** (2023), TSE, by Liu, Shangqing, et al.

**KAPE: kNN-based Performance Testing for Deep Code Search** (2023), TOSEM, by Uo, Yuejun, et al.

**Hyperbolic Code Retrieval: A Novel Approach for Efficient Code Search Using Hyperbolic Space Embeddings** (2023), arxiv, by Tang, Xunzhu, et al.

## Related Code Understanding Papers

**ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning** (2023), ICSE, and **Adapter Tuning for Code Search and Summarization** (2023), ICSE

**Rewriting the Code: A Simple Method for Large Language Model Augmented Code Search** (2024), arxiv, by Li, Haochen, et al.

**You Augment Me: Exploring ChatGPT-based Data Augmentation for Semantic Code Search** (2023), ICSME'23, by Wang, Yanlin, et al.

These papers cover various approaches to neural code search, from transformer-based models and graph neural networks to contrastive learning and embedding space techniques.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "f1ee25f2-2b81-4a66-8473-eb945c2e7b55"
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-15T04:16:52.330Z_

<details><summary>↩ Tool result · `toolu_017cVq7SWRXeaztJ1fPey4aL`</summary>

```text
Web search results for query: "repository level code understanding cross-file context LLM 2024 ICSE FSE"

Links: [{"title":"GitHub - allanj/repo-level-codegen-papers: Repo-Level Code generation papers · GitHub","url":"https://github.com/allanj/repo-level-codegen-papers"},{"title":"GitHub - iSEngLab/AwesomeLLM4SE: [SCIS 2025] A Survey on Large Language Models for Software Engineering · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4SE"},{"title":"CodePlan: Repository-level Coding using LLMs and Planning (FSE 2024 - Posters) - FSE 2024","url":"https://2024.esec-fse.org/details/fse-2024-posters/43/CodePlan-Repository-level-Coding-using-LLMs-and-Planning"},{"title":"GitHub - YerbaPage/Awesome-Repo-Level-Code-Generation: Must-read papers on Repository-level Code Generation & Issue Resolution 🔥","url":"https://github.com/YerbaPage/Awesome-Repo-Level-Code-Generation"},{"title":"CodePlan: Repository-level Coding using LLMs and Planning (FSE 2024 - Research Papers) - FSE 2024","url":"https://2024.esec-fse.org/details/fse-2024-research-papers/66/CodePlan-Repository-level-Coding-using-LLMs-and-Planning"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/4a4a3c197deac042461c677219efd36c-Paper-Conference.pdf"},{"title":"In Line with Context: Repository-Level Code Generation via Context Inlining","url":"https://arxiv.org/html/2601.00376v1"},{"title":"Repository-level code completion with adaptive segmentation and fused retrieval | Empirical Software Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10664-025-10762-7"},{"title":"CodePlan: Repository-Level Coding using LLMs and ...","url":"https://dl.acm.org/doi/pdf/10.1145/3643757"},{"title":"On Improving Repository-Level Code QA for Large ...","url":"https://aclanthology.org/2024.acl-srw.28.pdf"}]

Based on the search results, here's what I found regarding repository-level code understanding with cross-file context and LLMs at major conferences in 2024:

## Key Papers and Research

**FSE 2024:**
CodePlan is a task-agnostic, neuro-symbolic framework that synthesizes a multi-step chain-of-edits (plan), where each step results in a call to an LLM on a code location with context derived from the entire repository, combining incremental dependency analysis, change may-impact analysis and an adaptive planning algorithm with neural LLMs.

**ICSE 2024-2025:**
RLCoder: Reinforcement Learning for Repository-Level Code Completion [2024-ICSE] and Automated Code Editing with Search-Generate-Modify [2024-ICSE] are notable recent works in this area.

## Main Research Challenges

Real-world software engineering extends beyond single function or self-contained code files, as applications are typically built as repositories containing multiple interdependent files, modules, and libraries that require a holistic understanding of the entire codebase to perform tasks such as code completion, feature addition, or issue resolving.

Repository-level generation requires reasoning over entire repositories, accounting for coding conventions, API usage, and intricate inter-function dependencies.

## Emerging Approaches

Recent work focuses on various strategies: The most common is retrieval-augmented generation (RAG), which retrieves similar code snippets to the unfinished function. Additionally, more advanced methods incorporate program analysis, such as control-flow or data-flow graphs, to capture semantic dependencies more accurately.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "ef9349b8-2823-4f43-a16d-d602924c3324"
}
```

</details>

---

### System

_source line 55_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a7871f5d7a606af87",
  "tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "description": "Searching for ContraBERT contrastive learning code pre-trained …",
  "usage": {
    "total_tokens": 27182,
    "tool_uses": 13,
    "duration_ms": 34517
  },
  "last_tool_name": "WebSearch",
  "uuid": "c4a2083b-99d7-4879-84ab-ecad8b2805ff",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691"
}
```

---

### Tool call

_source line 56_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WUV8myDhgDEFGcUtuVWXhm`</summary>

```json
{
  "query": "ContraBERT contrastive learning code pre-trained models ICSE 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "383d3b54-7f34-4893-84aa-7717fc79d46d",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01NuSDb7huXYuorYkvxA1ZgY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1812,
      "cache_creation_input_tokens": 5893,
      "cache_read_input_tokens": 19159,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5893,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 49,
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

### System

_source line 57_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a7871f5d7a606af87",
  "tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "description": "Searching for CAPSTONE curriculum sampling dense retrieval EMNL…",
  "usage": {
    "total_tokens": 27231,
    "tool_uses": 14,
    "duration_ms": 34910
  },
  "last_tool_name": "WebSearch",
  "uuid": "a739e548-d74b-4636-aea8-89740a1e4678",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691"
}
```

---

### Tool call

_source line 58_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TsA2BT4gLbQjqTSFykaeSi`</summary>

```json
{
  "query": "CAPSTONE curriculum sampling dense retrieval EMNLP 2023 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "9fa76b6f-9b6f-487b-94c6-16b3f4d06f9c",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01NuSDb7huXYuorYkvxA1ZgY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1812,
      "cache_creation_input_tokens": 5893,
      "cache_read_input_tokens": 19159,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5893,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 49,
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

### System

_source line 59_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a7871f5d7a606af87",
  "tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "description": "Searching for RepoFusion repository level code completion cross…",
  "usage": {
    "total_tokens": 27280,
    "tool_uses": 15,
    "duration_ms": 35982
  },
  "last_tool_name": "WebSearch",
  "uuid": "432d1948-ba20-4469-a7db-e1e8f6d17ac6",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691"
}
```

---

### Tool call

_source line 60_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019c8rcvVTvpRgtBZD3txdEP`</summary>

```json
{
  "query": "RepoFusion repository level code completion cross-file 2024 NeurIPS ICSE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "4aad93fc-9944-4044-b976-2616225faceb",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01NuSDb7huXYuorYkvxA1ZgY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1812,
      "cache_creation_input_tokens": 5893,
      "cache_read_input_tokens": 19159,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5893,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 49,
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

### System

_source line 61_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a7871f5d7a606af87",
  "tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "description": "Searching for \"effective hard negative mining\" code search TOSE…",
  "usage": {
    "total_tokens": 27329,
    "tool_uses": 16,
    "duration_ms": 36405
  },
  "last_tool_name": "WebSearch",
  "uuid": "ef912394-be91-4277-b41a-adc71e44a621",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691"
}
```

---

### Tool call

_source line 62_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Uqop4VMn6hbfLpESa7oMzB`</summary>

```json
{
  "query": "\"effective hard negative mining\" code search TOSEM 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "9a85dd9b-e3fb-40b3-a75d-316f98615815",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01NuSDb7huXYuorYkvxA1ZgY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1812,
      "cache_creation_input_tokens": 5893,
      "cache_read_input_tokens": 19159,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5893,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 49,
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

### System

_source line 63_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a7871f5d7a606af87",
  "tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "description": "Searching for SynCoBERT authors Wang 2022 venue published journ…",
  "usage": {
    "total_tokens": 27378,
    "tool_uses": 17,
    "duration_ms": 36871
  },
  "last_tool_name": "WebSearch",
  "uuid": "eeca7a39-b1cf-4f5d-92de-47593433d080",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691"
}
```

---

### Tool call

_source line 64_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SRUkL9R2HNHXpmex6dhiMX`</summary>

```json
{
  "query": "SynCoBERT authors Wang 2022 venue published journal conference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "e0113f5a-c959-4881-9758-db1da71df80a",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01NuSDb7huXYuorYkvxA1ZgY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1812,
      "cache_creation_input_tokens": 5893,
      "cache_read_input_tokens": 19159,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5893,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 49,
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

_source line 65 · 2026-05-15T04:16:58.860Z_

<details><summary>↩ Tool result · `toolu_01TsA2BT4gLbQjqTSFykaeSi`</summary>

```text
Web search results for query: "CAPSTONE curriculum sampling dense retrieval EMNLP 2023 authors"

Links: [{"title":"CAPSTONE: Curriculum Sampling for Dense Retrieval with Document Expansion - ACL Anthology","url":"https://aclanthology.org/2023.emnlp-main.651/"},{"title":"CAPSTONE: Curriculum Sampling for Dense Retrieval with Document Expansion | OpenReview","url":"https://openreview.net/forum?id=Mefvmgkb9G&noteId=TlRvoprgev"},{"title":"[2212.09114] CAPSTONE: Curriculum Sampling for Dense Retrieval with Document Expansion","url":"https://arxiv.org/abs/2212.09114"},{"title":"Curriculum Sampling for Dense Retrieval with Document ...","url":"https://aclanthology.org/2023.emnlp-main.651.pdf"},{"title":"GitHub - microsoft/SimXNS: SimXNS is a research project for information retrieval. This repo contains official implementations by MSRA NLC team.","url":"https://github.com/microsoft/SimXNS"},{"title":"CAPSTONE: Curriculum Sampling for Dense Retrieval with Document Expansion","url":"https://openreview.net/pdf?id=Mefvmgkb9G"},{"title":"Main Conference - EMNLP 2023","url":"https://2023.emnlp.org/program/accepted_main_conference/"},{"title":"Curriculum Sampling for Dense Retrieval with Document Expansion | Request PDF","url":"https://www.researchgate.net/publication/366423521_Curriculum_Sampling_for_Dense_Retrieval_with_Document_Expansion"},{"title":"Curriculum Sampling For Dense Retrieval With Document ...","url":"https://www.scribd.com/document/835721616/CurriculumSamplingForDenseRetrievalWithDocumentExpansion"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"}]

Based on the search results, I found the information about the CAPSTONE paper from EMNLP 2023.

The authors of CAPSTONE are Xingwei He, Yeyun Gong, A-Long Jin, Hang Zhang, Anlei Dong, Jian Jiao, Siu Ming Yiu, and Nan Duan. The paper is titled "CAPSTONE: Curriculum Sampling for Dense Retrieval with Document Expansion" and was published in the Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing, pages 10531–10541, Singapore.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "9f4aff8a-7ea8-45cb-b624-8adeb91d6e43"
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-15T04:17:00.792Z_

<details><summary>↩ Tool result · `toolu_01WUV8myDhgDEFGcUtuVWXhm`</summary>

```text
Web search results for query: "ContraBERT contrastive learning code pre-trained models ICSE 2023"

Links: [{"title":"ContraBERT: Enhancing Code Pre-trained Models via ...","url":"https://www.computer.org/csdl/proceedings-article/icse/2023/570100c476/1OM4OrPPiNy"},{"title":"ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning - Singapore Management University","url":"https://smusg.elsevierpure.com/en/publications/contrabert-enhancing-code-pre-trained-models-via-contrastive-lear"},{"title":"[2301.09072] ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning","url":"https://arxiv.org/abs/2301.09072"},{"title":"ContraBERT: Enhancing Code Pre-Trained Models via Contrastive Learning | Proceedings of the 45th International Conference on Software Engineering","url":"https://dl.acm.org/doi/abs/10.1109/ICSE48619.2023.00207"},{"title":"[PDF] ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/f6572fccea70e5023cc38cb33ebd0f520d7b22e2"},{"title":"ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning","url":"https://arxiv.org/pdf/2301.09072"},{"title":"About me - Shangqing Liu’s Homepage","url":"https://shangqing-liu.github.io/"},{"title":"ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning | Request PDF","url":"https://www.researchgate.net/publication/372385658_ContraBERT_Enhancing_Code_Pre-trained_Models_via_Contrastive_Learning"},{"title":"Enhancing Code Search Fine-Tuning with Momentum Contrastive Learning and Cross-Modal Matching | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-981-95-0014-7_42"},{"title":"ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10172726/"}]

Based on the search results, here's what I found about ContraBERT:

## ContraBERT Overview

ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning was published in the 2023 IEEE/ACM 45th International Conference on Software Engineering (ICSE 2023).

## Key Contributions

ContraBERT aims to improve the robustness of pre-trained models via contrastive learning. The approach addresses an important problem: state-of-the-art pre-trained models like CodeBERT and GraphCodeBERT are susceptible to adversarial attacks and their performance drops significantly with simple perturbations such as renaming variable names.

## Methodology

The work designs nine kinds of simple and complex data augmentation operators on programming language (PL) and natural language (NL) data to construct different variants, and continues to train existing pre-trained models by masked language modeling (MLM) and contrastive pre-training task on the original samples with their augmented variants to enhance robustness.

## Results

The extensive experiments demonstrate that ContraBERT can effectively improve the robustness of existing pre-trained models, and further study confirms that these robustness-enhanced models provide improvements compared to original models over four popular downstream tasks.

## Authors and Source Code

The paper was authored by Shangqing Liu, Bozhi Wu, Xiaofei Xie, Guozhu Meng, and Yang Liu. The authors provide project details and code at https://sites.google.com/view/contrabert.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "8c01de7a-9bd9-4a30-adf7-76e2234fc0d1"
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-15T04:17:01.195Z_

<details><summary>↩ Tool result · `toolu_01Uqop4VMn6hbfLpESa7oMzB`</summary>

```text
Web search results for query: ""effective hard negative mining" code search TOSEM 2024"

Links: [{"title":"Effective Hard Negative Mining for Contrastive Learning-Based Code Search | ACM Transactions on Software Engineering and Methodology","url":"https://dl.acm.org/doi/full/10.1145/3695994"},{"title":"Effective Hard Negative Mining for Contrastive Learning-Based Code Search | Request PDF","url":"https://www.researchgate.net/publication/384848348_Effective_Hard_Negative_Mining_for_Contrastive_Learning-based_Code_Search"},{"title":"Effective Hard Negative Mining for Contrastive Learning-based Code Search | CoLab","url":"https://colab.ws/articles/10.1145/3695994"},{"title":"NV-Retriever: Improving text embedding models with effective","url":"https://arxiv.org/pdf/2407.15831"},{"title":"Hard Negative Mining for Domain-Specific Retrieval in ...","url":"https://arxiv.org/pdf/2505.18366"},{"title":"Hard Negative Mining for Domain-Specific Retrieval in Enterprise Systems","url":"https://arxiv.org/html/2505.18366v1"},{"title":"Hard Negative Mining for Domain-Specific Retrieval in ...","url":"https://aclanthology.org/2025.acl-industry.72.pdf"},{"title":"A Novel Refactoring and Semantic Aware Abstract Syntax Tree Differencing Tool","url":"https://users.encs.concordia.ca/~nikolaos/publications/TOSEM_2024.pdf"},{"title":"Revisiting Hard Negative Mining in Contrastive Learning for Visual Understanding","url":"https://www.mdpi.com/2079-9292/12/23/4884"},{"title":"Hard Negative Sample Mining for Whole Slide Image Classification | MICCAI 2024 - Open Access","url":"https://papers.miccai.org/miccai-2024/372-Paper3822.html"}]

I found relevant results for your search. The top result is the exact paper you're looking for:

The paper "Effective Hard Negative Mining for Contrastive Learning-Based Code Search" addresses code search, which aims to find the most relevant code snippet in a large codebase based on a given natural language query. An accurate code search engine can increase code reuse and improve programming efficiency.

The state-of-the-art learning method uses the contrastive learning paradigm, with the objective of contrastive learning being to maximize the similarity between matching code and query (positive samples) and minimize the similarity between mismatched pairs (negative samples).

The paper was published in the ACM Transactions on Software Engineering and Methodology (TOSEM) in 2024 and is available at: https://dl.acm.org/doi/full/10.1145/3695994


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "f1946dc8-b52e-407c-b8f7-2b2cb6f0f320"
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-15T04:17:01.217Z_

<details><summary>↩ Tool result · `toolu_01SRUkL9R2HNHXpmex6dhiMX`</summary>

```text
Web search results for query: "SynCoBERT authors Wang 2022 venue published journal conference"

Links: [{"title":"The 2nd Workshop on Recommendation with Generative Models","url":"https://arxiv.org/pdf/2403.04399"},{"title":"Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies - ACL Anthology","url":"https://aclanthology.org/volumes/2022.naacl-main/"},{"title":"Wang research group to present at The ACM Web Conference 2022","url":"https://ischool.illinois.edu/news-events/news/2022/04/wang-research-group-present-acm-web-conference-2022"},{"title":"Yao Wan@Huazhong University of Science and Technology","url":"http://wanyao.me/publication.html"},{"title":"YUYAN WANG (Last updated: Mar 2024)","url":"https://yuyanwang.people.stanford.edu/sites/g/files/sbiybj30946/files/media/file/cv_yuyan_wang_website_0.pdf"},{"title":"Publication | Wayne Wu","url":"https://wywu.github.io/publication/"},{"title":"Jianzong Wang | LLAM | Lab of Large Audio Model","url":"https://largeaudiomodel.com/author/jianzong-wang/"},{"title":"Ge Wang - CSCW '22 - Conference Programs","url":"https://programs.sigchi.org/cscw/2022/authors/86551"},{"title":"Tong Wang","url":"https://scholar.google.com/citations?user=KB6A0esAAAAJ&hl=en"},{"title":"Yin Wang - Conferences","url":"https://sites.google.com/view/yin-wang/conferences"}]

Based on the search results, I found information about SynCoBERT:

SynCoBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation was authored by Xin Wang, Yasheng Wang, Fei Mi, Pingyi Zhou, Yao Wan, Xiao Liu, Li Li, Hao Wu, Jin Liu, and Xin Jiang, and was published on arXiv in 2021.

The paper appears to have been posted to arXiv rather than published in a traditional conference or journal venue.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "449a8c5b-af76-4081-9ee1-a6e5b05bb945"
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-15T04:17:03.124Z_

<details><summary>↩ Tool result · `toolu_019c8rcvVTvpRgtBZD3txdEP`</summary>

```text
Web search results for query: "RepoFusion repository level code completion cross-file 2024 NeurIPS ICSE"

Links: [{"title":"Repository-level code completion with adaptive segmentation and fused retrieval | Empirical Software Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10664-025-10762-7"},{"title":"REPOFUSE: Repository-Level Code Completion with Fused Dual Context","url":"https://arxiv.org/pdf/2402.14323"},{"title":"GitHub - YerbaPage/Awesome-Repo-Level-Code-Generation: Must-read papers on Repository-level Code Generation & Issue Resolution 🔥","url":"https://github.com/YerbaPage/Awesome-Repo-Level-Code-Generation"},{"title":"GitHub - saltudelft/ml4se: A curated list of papers, theses, datasets, and tools related to the application of Machine Learning for Software Engineering · GitHub","url":"https://github.com/saltudelft/ml4se"},{"title":"GitHub - allanj/repo-level-codegen-papers: Repo-Level Code generation papers · GitHub","url":"https://github.com/allanj/repo-level-codegen-papers"},{"title":"REPOFUSION: TRAINING CODE MODELS TO ...","url":"https://openreview.net/pdf?id=2drC319yHQ"},{"title":"RepoFusion: Training Code Models to Understand Your Repository | OpenReview","url":"https://openreview.net/forum?id=2drC319yHQ"},{"title":"Repoformer: Selective Retrieval for Repository-Level Code Completion","url":"https://arxiv.org/html/2403.10059v2"},{"title":"RepoFusion: Training Code Models to Understand Your Repository | alphaXiv","url":"https://www.alphaxiv.org/abs/2306.10998"},{"title":"RepoFusion: Training Code Models to Understand Your Repository | Request PDF","url":"https://www.researchgate.net/publication/371727808_RepoFusion_Training_Code_Models_to_Understand_Your_Repository"}]

Based on the search results, I found information about RepoFusion and related work on repository-level code completion:

## RepoFusion: Training Code Models to Understand Your Repository

RepoFusion is a framework to train models to incorporate relevant repository context. Despite the success of Large Language Models (LLMs) in coding assistants like GitHub Copilot, these models struggle to understand the context present in the repository (e.g., imports, parent classes, files with similar names, etc.), thereby producing inaccurate code completions.

RepoFusion is a framework to train models to incorporate relevant repository context, and experiments on single-line code completion show that models trained with repository context significantly outperform much larger code models as CodeGen-16B-multi (∼73× larger) and closely match the performance of the ∼70× larger StarCoderBase model that was trained with the Fill-in-the-Middle objective.

### Key Technical Aspects

RepoFusion uses the Fusion-in-Decoder (Izacard & Grave, 2021) architecture to combine repository contexts, where each repo context is appended with the surrounding context and encoded separately, and a decoder jointly attends to the concatenated encoded representations to produce a prediction for the target hole.

One crucial finding is that leveraging information from diverse sources within a repository is the key to RepoFusion's effectiveness.

A dataset called Stack-Repo 3 was created and released, consisting of 200 Java repositories with permissive licenses and near-deduplicated files that are augmented with three types of repository contexts.

The search results show RepoFusion was referenced in connection with code completion research, though the specific mention of NeurIPS 2024 or ICSE 2024 publication venues wasn't explicitly confirmed in these results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "abea017d-7c68-4ef2-b5c0-699bfb6b986e"
}
```

</details>

---

### System

_source line 70_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a7871f5d7a606af87",
  "tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "description": "Searching for SynCoBERT \"ACL 2022\" OR \"EMNLP 2022\" OR \"NAACL 20…",
  "usage": {
    "total_tokens": 31763,
    "tool_uses": 18,
    "duration_ms": 45235
  },
  "last_tool_name": "WebSearch",
  "uuid": "447d764e-09fd-425e-9247-458a8d6c2152",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691"
}
```

---

### Tool call

_source line 71_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015XAJxyHc59EjHidhpY3nCv`</summary>

```json
{
  "query": "SynCoBERT \"ACL 2022\" OR \"EMNLP 2022\" OR \"NAACL 2022\" published proceedings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "596baab0-6474-4d7c-92a9-4a6b395d2953",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01LQqgR2xAkSrPTTz3uds71k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1362,
      "cache_creation_input_tokens": 4792,
      "cache_read_input_tokens": 25052,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4792,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 43,
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

### System

_source line 72_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a7871f5d7a606af87",
  "tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "description": "Searching for \"effective hard negative mining\" code search TOSE…",
  "usage": {
    "total_tokens": 31806,
    "tool_uses": 19,
    "duration_ms": 46039
  },
  "last_tool_name": "WebSearch",
  "uuid": "ac932c2c-6a29-4145-b6e0-aca39e484103",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691"
}
```

---

### Tool call

_source line 73_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BddwEsAjjhff5Ge4BaKuY2`</summary>

```json
{
  "query": "\"effective hard negative mining\" code search TOSEM 2024 authors title full"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "a48d57c6-de1b-4f0c-87dc-ec3c7292885e",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01LQqgR2xAkSrPTTz3uds71k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1362,
      "cache_creation_input_tokens": 4792,
      "cache_read_input_tokens": 25052,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4792,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 43,
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

### System

_source line 74_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a7871f5d7a606af87",
  "tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "description": "Searching for CrossCodeEval NeurIPS 2023 authors Ding Wang titl…",
  "usage": {
    "total_tokens": 31849,
    "tool_uses": 20,
    "duration_ms": 46833
  },
  "last_tool_name": "WebSearch",
  "uuid": "e2c9843e-a288-4b04-9f79-118d2e70c647",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691"
}
```

---

### Tool call

_source line 75_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DE72KMaSetp6mun4esMkt4`</summary>

```json
{
  "query": "CrossCodeEval NeurIPS 2023 authors Ding Wang title full"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "dadd0c68-92af-49ab-8dc8-c708efda92e0",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01LQqgR2xAkSrPTTz3uds71k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1362,
      "cache_creation_input_tokens": 4792,
      "cache_read_input_tokens": 25052,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4792,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 43,
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

### System

_source line 76_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a7871f5d7a606af87",
  "tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "description": "Searching for ContraBERT ICSE 2023 Shangqing Liu authors full t…",
  "usage": {
    "total_tokens": 31892,
    "tool_uses": 21,
    "duration_ms": 47339
  },
  "last_tool_name": "WebSearch",
  "uuid": "ed133407-e99f-4c72-a8e8-b8742eafc120",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691"
}
```

---

### Tool call

_source line 77_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Me8uhNAvCk8xisPat5bEko`</summary>

```json
{
  "query": "ContraBERT ICSE 2023 Shangqing Liu authors full title"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "64edd3f5-90c6-446f-a9a2-53d443979548",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01LQqgR2xAkSrPTTz3uds71k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1362,
      "cache_creation_input_tokens": 4792,
      "cache_read_input_tokens": 25052,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4792,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 43,
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

_source line 78 · 2026-05-15T04:17:10.404Z_

<details><summary>↩ Tool result · `toolu_01BddwEsAjjhff5Ge4BaKuY2`</summary>

```text
Web search results for query: ""effective hard negative mining" code search TOSEM 2024 authors title full"

Links: [{"title":"Effective Hard Negative Mining for Contrastive Learning-Based Code Search | ACM Transactions on Software Engineering and Methodology","url":"https://dl.acm.org/doi/full/10.1145/3695994"},{"title":"Effective Hard Negative Mining for Contrastive Learning-Based Code Search | Request PDF","url":"https://www.researchgate.net/publication/384848348_Effective_Hard_Negative_Mining_for_Contrastive_Learning-based_Code_Search"},{"title":"Effective Hard Negative Mining for Contrastive Learning-based Code Search | CoLab","url":"https://colab.ws/articles/10.1145/3695994"},{"title":"NV-Retriever: Improving text embedding models with effective","url":"https://arxiv.org/pdf/2407.15831"},{"title":"Hard Negative Mining for Domain-Specific Retrieval in ...","url":"https://arxiv.org/pdf/2505.18366"},{"title":"Hard Negative Mining for Domain-Specific Retrieval in Enterprise Systems","url":"https://arxiv.org/html/2505.18366v1"},{"title":"Hard Negative Mining for Domain-Specific Retrieval in ...","url":"https://aclanthology.org/2025.acl-industry.72.pdf"},{"title":"A Novel Refactoring and Semantic Aware Abstract Syntax Tree Differencing Tool","url":"https://users.encs.concordia.ca/~nikolaos/publications/TOSEM_2024.pdf"},{"title":"Revisiting Hard Negative Mining in Contrastive Learning for Visual Understanding","url":"https://www.mdpi.com/2079-9292/12/23/4884"},{"title":"Hard Negative Sample Mining for Whole Slide Image Classification | MICCAI 2024 - Open Access","url":"https://papers.miccai.org/miccai-2024/372-Paper3822.html"}]

Based on the search results, I found the paper you're looking for:

**Title:** "Effective Hard Negative Mining for Contrastive Learning-Based Code Search"

**Publication:** ACM Transactions on Software Engineering and Methodology (TOSEM)

**Year:** 2024

The paper was published in ACM TOSEM in 2024 (with a metadata date of October 11, 2024). The research focuses on code search, which aims to find the most relevant code snippet in a large codebase based on a given natural language query.

The full paper is available at: https://dl.acm.org/doi/full/10.1145/3695994

However, the search results provided don't include the complete author names list. For the full author information, you would need to access the paper directly through the ACM Digital Library link above.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "acdaa729-8a86-4718-9944-7e1d6adf5747"
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-15T04:17:10.570Z_

<details><summary>↩ Tool result · `toolu_015XAJxyHc59EjHidhpY3nCv`</summary>

```text
Web search results for query: "SynCoBERT "ACL 2022" OR "EMNLP 2022" OR "NAACL 2022" published proceedings"

Links: [{"title":"ACL 2022 | 60th Annual Meeting of the Association for Computational Linguistics | Ireland","url":"https://www.2022.aclweb.org/papers"},{"title":"The 2022 Conference on Empirical Methods in Natural Language Processing - ACL Anthology","url":"https://aclanthology.org/events/emnlp-2022/"},{"title":"Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing: System Demonstrations - ACL Anthology","url":"https://aclanthology.org/volumes/2022.emnlp-demos/"},{"title":"Conference on Empirical Methods in Natural Language Processing - ACL Anthology","url":"https://aclanthology.org/venues/emnlp/"},{"title":"Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing: Industry Track - ACL Anthology","url":"https://aclanthology.org/volumes/2022.emnlp-industry/"},{"title":"Findings of the Association for Computational Linguistics: EMNLP 2022 - ACL Anthology","url":"https://aclanthology.org/volumes/2022.findings-emnlp/"},{"title":"EMNLP 2022 The 2022 Conference on Empirical Methods in Natural","url":"https://aclanthology.org/2022.emnlp-tutorials.pdf"},{"title":"2022 Annual Conference of the North American Chapter of the Association for Computational Linguistics - NAACL-HLT 2022","url":"https://2022.naacl.org/"},{"title":"Findings of the Association for Computational Linguistics - ACL Anthology","url":"https://aclanthology.org/venues/findings/"},{"title":"Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing - ACL Anthology","url":"https://aclanthology.org/volumes/2022.emnlp-main/"}]

The search results show links to the ACL Anthology pages for EMNLP 2022 and NAACL 2022 proceedings, but do not contain any specific information about SynCoBERT in these proceedings. The results provide general information about the available proceedings from these conferences but don't mention SynCoBERT specifically.

Based on the search results, I found the ACL Anthology pages for the 2022 conferences you mentioned:

- **EMNLP 2022**: The proceedings are available on the ACL Anthology with main conference papers, findings, system demonstrations, and industry track publications.
- **NAACL 2022**: The conference has concluded and proceedings are available.
- **ACL 2022**: The 60th Annual Meeting proceedings are also available.

However, my search did not return specific results showing SynCoBERT as a published paper in these 2022 proceedings. To locate SynCoBERT specifically, you might want to:

1. Visit the ACL Anthology directly (aclanthology.org) and search for "SynCoBERT"
2. Check the conference websites for these events directly
3. Search on academic platforms like arXiv or Google Scholar

If you'd like, I can perform a more targeted search specifically for the SynCoBERT paper itself to determine where it was published.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "fa5b69e9-54de-4326-a231-2fbe3b30b645"
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-15T04:17:11.296Z_

<details><summary>↩ Tool result · `toolu_01DE72KMaSetp6mun4esMkt4`</summary>

```text
Web search results for query: "CrossCodeEval NeurIPS 2023 authors Ding Wang title full"

Links: [{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=Yangruibo+Ding%2C+Zijian+Wang%2C+Wasi+Ahmad%2C+Hantian+Ding%2C+Ming+Tan%2C+Nihal+Jain%2C+Murali+Krishna+Ramanathan%2C+Ramesh+Nallapati%2C+Parminder+Bhatia%2C+Dan+Roth%2C+and+Bing+Xiang.+2023.+CrossCodeEval%3A+A+Diverse+and+Multilingual+Benchmark+for+Cross-File+Code+Completion.+Advances+in+Neural+Information+Processing+Systems+36+%28Dec.+2023%29%2C+46701--46723."},{"title":"GitHub - amazon-science/cceval: CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion (NeurIPS 2023)","url":"https://github.com/amazon-science/cceval"},{"title":"© 2023, Amazon Web Services, Inc. or its affiliates. All rights reserved.","url":"https://neurips.cc/media/neurips-2023/Slides/73423.pdf"},{"title":"CROSSCODEEVAL: A Diverse and Multilingual","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/920f2dced7d32ab2ba2f1970bc306af6-Paper-Datasets_and_Benchmarks.pdf"},{"title":"cceval/README.md at a11b8a6c71cf1fe99881dd22d14871c6f01bd30f · amazon-science/cceval","url":"https://github.com/amazon-science/cceval/blob/a11b8a6c71cf1fe99881dd22d14871c6f01bd30f/README.md"},{"title":"CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion","url":"https://proceedings.neurips.cc/paper_files/paper/2023/hash/920f2dced7d32ab2ba2f1970bc306af6-Abstract-Datasets_and_Benchmarks.html"},{"title":"cceval/README.md at main · amazon-science/cceval","url":"https://github.com/amazon-science/cceval/blob/main/README.md"},{"title":"[Quick Review] CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion","url":"https://liner.com/review/crosscodeeval-a-diverse-and-multilingual-benchmark-for-crossfile-code-completion"},{"title":"CROSSCODEEVAL: A Diverse and Multilingual","url":"https://zijianwang.me/data/NeurIPS_2023__CrossCodeEval.pdf"},{"title":"NeurIPS Poster CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion","url":"https://neurips.cc/virtual/2023/poster/73423"}]

Based on the web search results, here is the information you requested:

**Title:** CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion

**Authors:** Yangruibo Ding, Zijian Wang, Wasi Uddin Ahmad, Hantian Ding, Ming Tan, Nihal Jain, Murali Krishna Ramanathan, Ramesh Nallapati, Parminder Bhatia, Dan Roth, and Bing Xiang

**Conference:** Advances in Neural Information Processing Systems (2023) / NeurIPS 2023 Datasets and Benchmarks Track


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "e65dc0ee-ea27-4cbb-a3c6-16218e2ce049"
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-15T04:17:11.527Z_

<details><summary>↩ Tool result · `toolu_01Me8uhNAvCk8xisPat5bEko`</summary>

```text
Web search results for query: "ContraBERT ICSE 2023 Shangqing Liu authors full title"

Links: [{"title":"About me - Shangqing Liu’s Homepage","url":"https://shangqing-liu.github.io/"},{"title":"ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning - Singapore Management University","url":"https://smusg.elsevierpure.com/en/publications/contrabert-enhancing-code-pre-trained-models-via-contrastive-lear"},{"title":"[PDF] ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/ContraBERT:-Enhancing-Code-Pre-trained-Models-via-Liu-Wu/f6572fccea70e5023cc38cb33ebd0f520d7b22e2"},{"title":"Publications - Shangqing Liu’s Homepage","url":"https://shangqing-liu.github.io/publications/"},{"title":"ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning | Request PDF","url":"https://www.researchgate.net/publication/372385658_ContraBERT_Enhancing_Code_Pre-trained_Models_via_Contrastive_Learning"},{"title":"shangqing-liu (ShangqingLiu) · GitHub","url":"https://github.com/shangqing-liu"},{"title":"Exploring the Potential of ChatGPT in Automated Code Refinement: An Empirical Study | Proceedings of the IEEE/ACM 46th International Conference on Software Engineering","url":"https://dl.acm.org/doi/10.1145/3597503.3623306"},{"title":"GitHub - xinyi-hou/LLM4SE_SLR: Large Language Models for Software Engineering: A Systematic Literature Review · GitHub","url":"https://github.com/xinyi-hou/LLM4SE_SLR"},{"title":"(PDF) ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning","url":"https://www.researchgate.net/publication/367359448_ContraBERT_Enhancing_Code_Pre-trained_Models_via_Contrastive_Learning"},{"title":"Shangqing Liu","url":"https://scholar.google.com/citations?hl=en&user=Rl0-phkAAAAJ"}]

Based on the search results, here is the information about the ContraBERT paper:

**Full Title:** ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning

**Authors:** Shangqing Liu, Bozhi Wu, Xiaofei Xie, Guozhu Meng, Yang Liu

**Conference:** ICSE 2023 - Proceedings of the 45th IEEE/ACM International Conference on Software Engineering

**Pages:** 2476-2487


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "9d7c9d32-7dd3-451c-b87e-8c3d2c2d51dd"
}
```

</details>

---

### System

_source line 82_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a7871f5d7a606af87",
  "tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "description": "Searching for \"effective hard negative mining\" \"contrastive lea…",
  "usage": {
    "total_tokens": 35567,
    "tool_uses": 22,
    "duration_ms": 54287
  },
  "last_tool_name": "WebSearch",
  "uuid": "cadbf569-3de6-404d-a390-634632553c75",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691"
}
```

---

### Tool call

_source line 83_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NZ2yD94jTqPJLzrHtAwffT`</summary>

```json
{
  "query": "\"effective hard negative mining\" \"contrastive learning\" code search 2024 authors arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "90cd3863-5bf3-40bc-b1b7-5cc3e306ff45",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_015U9j7fEvkdZQwf22HJUkL1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4988,
      "cache_read_input_tokens": 29844,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4988,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 48,
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

### System

_source line 84_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a7871f5d7a606af87",
  "tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "description": "Searching for ProGraML ICML 2021 Cummins authors full title \"da…",
  "usage": {
    "total_tokens": 35615,
    "tool_uses": 23,
    "duration_ms": 55583
  },
  "last_tool_name": "WebSearch",
  "uuid": "5914fd0c-f2ec-460f-961b-47e8e9811f96",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691"
}
```

---

### Tool call

_source line 85_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013v558ex2Zpsn4xztfqX21K`</summary>

```json
{
  "query": "ProGraML ICML 2021 Cummins authors full title \"data flow analysis\" \"compiler optimizations\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "acd16a0c-319e-440e-ab01-766717d776e4",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_015U9j7fEvkdZQwf22HJUkL1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4988,
      "cache_read_input_tokens": 29844,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4988,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 48,
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

### System

_source line 86_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a7871f5d7a606af87",
  "tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "description": "Searching for ContraCode \"contrastive code representation learn…",
  "usage": {
    "total_tokens": 35663,
    "tool_uses": 24,
    "duration_ms": 55961
  },
  "last_tool_name": "WebSearch",
  "uuid": "8a7bda5d-3b5a-45ce-8372-f5d2f37075e5",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691"
}
```

---

### Tool call

_source line 87_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JoAtHx38uLz8X1gDT6nShF`</summary>

```json
{
  "query": "ContraCode \"contrastive code representation learning\" EMNLP 2021 Jain authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "a20b760b-631f-45a7-b6a7-5fb291d7d707",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_015U9j7fEvkdZQwf22HJUkL1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4988,
      "cache_read_input_tokens": 29844,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4988,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 48,
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

_source line 88 · 2026-05-15T04:17:20.371Z_

<details><summary>↩ Tool result · `toolu_01NZ2yD94jTqPJLzrHtAwffT`</summary>

```text
Web search results for query: ""effective hard negative mining" "contrastive learning" code search 2024 authors arXiv"

Links: [{"title":"Effective Hard Negative Mining for Contrastive Learning-Based Code Search | ACM Transactions on Software Engineering and Methodology","url":"https://dl.acm.org/doi/full/10.1145/3695994"},{"title":"Effective Hard Negative Mining for Contrastive Learning-based Code Search | CoLab","url":"https://colab.ws/articles/10.1145/3695994"},{"title":"Revisiting Hard Negative Mining in Contrastive Learning for Visual Understanding","url":"https://www.mdpi.com/2079-9292/12/23/4884"},{"title":"Towards Expansive and Adaptive Hard Negative Mining: Graph Contrastive Learning via Subspace Preserving | Proceedings of the ACM Web Conference 2024","url":"https://dl.acm.org/doi/10.1145/3589334.3645327"},{"title":"Effective Hard Negative Mining for Contrastive Learning-Based Code Search | Request PDF","url":"https://www.researchgate.net/publication/384848348_Effective_Hard_Negative_Mining_for_Contrastive_Learning-based_Code_Search"},{"title":"GitHub - mala-lab/AUGCL: Official code for TNNLS paper \"Affinity Uncertainty-based Hard Negative Mining in Graph Contrastive Learning\"","url":"https://github.com/mala-lab/AUGCL"},{"title":"ProGCL: Rethinking Hard Negative Mining in Graph Contrastive Learning","url":"https://proceedings.mlr.press/v162/xia22b.html"},{"title":"Mining negative samples on contrastive learning via curricular weighting strategy - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S002002552400447X"},{"title":"Dynamic Asymmetric Contrastive Learning with Adaptive Hard Negative Mining for Resume-Job Matching | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-981-95-3055-7_26"},{"title":"A Hard Negatives Mining and Enhancing Method for Multi-Modal Contrastive Learning","url":"https://www.mdpi.com/2079-9292/14/4/767"}]

Based on the web search results, I found relevant information about the paper on "Effective Hard Negative Mining for Contrastive Learning-based Code Search."

## Key Findings:

The authors are Fan Y., Li C., Ge J., Huang L., Luo B., and Luo B. The paper was published in ACM Transactions on Software Engineering and Methodology in 2025, Volume 34, No. 3, pages 1-35.

The paper proposes a contrastive learning code search model with hard negative mining called CoCoHaNeRe, which introduces hard negative examples into contrastive training - these are negative examples in the codebase that are most similar to positive examples.

The paper addresses two main problems: due to the random selection of negative samples, existing models cannot distinguish similar codes well, and semantic vectors in the memory bank are reused from previous inference results without gradient descent, preventing the model from effectively learning negative sample semantic information.

The paper appears in the ACM Digital Library and was referenced in academic literature as of October 2024, though the official publication date is listed as 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "23decced-b3c2-4824-89dd-73aac107e3cd"
}
```

</details>

---

### Tool result

_source line 89 · 2026-05-15T04:17:20.736Z_

<details><summary>↩ Tool result · `toolu_013v558ex2Zpsn4xztfqX21K`</summary>

```text
Web search results for query: "ProGraML ICML 2021 Cummins authors full title "data flow analysis" "compiler optimizations""

Links: [{"title":"GitHub - ChrisCummins/ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations · GitHub","url":"https://github.com/ChrisCummins/ProGraML"},{"title":"PROGRAML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations - University of Edinburgh Research Explorer","url":"https://www.research.ed.ac.uk/en/publications/programl-a-graph-based-program-representation-for-data-flow-analy"},{"title":"[PDF] ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations | Semantic Scholar","url":"https://www.semanticscholar.org/paper/ProGraML:-A-Graph-based-Program-Representation-for-Cummins-Fisches/7843876d45f4c6ac751039b198aade0ee9f94342"},{"title":"dblp: ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations.","url":"https://dblp.org/rec/conf/icml/CumminsFBHOL21.html"},{"title":"ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations","url":"https://proceedings.mlr.press/v139/cummins21a.html"},{"title":"ICML 2021 ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations Spotlight","url":"https://icml.cc/virtual/2021/spotlight/8886"},{"title":"PROGRAML: A Graph-based Program Representation for Data Flow Analysis","url":"http://proceedings.mlr.press/v139/cummins21a/cummins21a.pdf"},{"title":"ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations - YouTube","url":"https://www.youtube.com/watch?v=cHElgMSOPFs"},{"title":"The Next 700 ML-Enabled Compiler Optimizations | Proceedings of the 33rd ACM SIGPLAN International Conference on Compiler Construction","url":"https://dl.acm.org/doi/10.1145/3640537.3641580"},{"title":"ProGraML: Graph-based Deep Learning for Program Optimization and Analysis.","url":"https://spcl.inf.ethz.ch/Publications/.pdf/programl-icml21-slides.pdf"}]

Based on the search results, here is the information about the ProGraML paper:

**Full Title:** "ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations"

**Authors:** Chris Cummins, Zacharias Fisches, Tal Ben-Nun, Torsten Hoefler, Michael O'Boyle, and Hugh Leather

**Conference:** Thirty-eighth International Conference on Machine Learning (ICML), 2021

**Publication Details:** Published in Proceedings of the 38th International Conference on Machine Learning, pages 2244-2253

The paper proposes ProGraML - Program Graphs for Machine Learning - a language-independent, portable representation of program semantics and overcomes the limitations of prior works and yields improved performance on downstream optimization tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "32061f3e-2b43-4845-9ae6-4e1497cec0a2"
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-15T04:17:21.142Z_

<details><summary>↩ Tool result · `toolu_01JoAtHx38uLz8X1gDT6nShF`</summary>

```text
Web search results for query: "ContraCode "contrastive code representation learning" EMNLP 2021 Jain authors"

Links: [{"title":"Contrastive Code Representation Learning - ACL Anthology","url":"https://aclanthology.org/2021.emnlp-main.482/"},{"title":"[PDF] Contrastive Code Representation Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Contrastive-Code-Representation-Learning-Jain-Jain/021bbcefc993c389bad6c1daefd8ff92d0fc2441"},{"title":"Contrastive Code Representation Learning","url":"https://aclanthology.org/2021.emnlp-main.482.pdf"},{"title":"dblp: Contrastive Code Representation Learning.","url":"https://dblp.org/rec/conf/emnlp/0001JZA0S21.html"},{"title":"[2007.04973] Contrastive Code Representation Learning","url":"https://arxiv.org/abs/2007.04973"},{"title":"GitHub - parasj/contracode: Contrastive Code Representation Learning: functionality-based JavaScript embeddings through self-supervised learning","url":"https://github.com/parasj/contracode"},{"title":"[EMNLP 2021] Contrastive Code Representation Learning - YouTube","url":"https://www.youtube.com/watch?v=0deUDO6BqYY"},{"title":"(PDF) Contrastive Code Representation Learning","url":"https://www.academia.edu/87692509/Contrastive_Code_Representation_Learning"},{"title":"Contrastive Code Representation Learning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2020arXiv200704973J/abstract"},{"title":"Contrastive Code Representation Learning","url":"https://parasj.github.io/contracode/"}]

Based on the search results, here's what I found about ContraCode:

## Paper Details

ContraCode is authored by Paras Jain, Ajay Jain, Tianjun Zhang, Pieter Abbeel, Joseph Gonzalez, and Ion Stoica, and was published in the Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing (EMNLP).

## Overview

ContraCode is a contrastive pre-training task that learns code functionality, not form. ContraCode pre-trains a neural network to identify functionally similar variants of a program among many non-equivalent distractors. The variants are scalably generated using an automated source-to-source compiler as a form of data augmentation.

## Key Results

Contrastive pre-training outperforms RoBERTa on an adversarial code clone detection benchmark by 39% AUROC. ContraCode improves summarization and TypeScript type inference accuracy by 2 to 13 percentage points over competitive baselines.

All source code is available at https://github.com/parasj/contracode.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "2d708961-4983-4a5a-a8e7-cb3d22be0a64"
}
```

</details>

---

### System

_source line 91_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a7871f5d7a606af87",
  "tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "description": "Searching for CoSQA authors Junjie Huang Duyu Tang ACL 2021 ful…",
  "usage": {
    "total_tokens": 38531,
    "tool_uses": 25,
    "duration_ms": 63580
  },
  "last_tool_name": "WebSearch",
  "uuid": "62eee240-fb04-4337-9dc0-e455cada4be4",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691"
}
```

---

### Tool call

_source line 92_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019bn4XnticyEcBpy5HRaAnQ`</summary>

```json
{
  "query": "CoSQA authors Junjie Huang Duyu Tang ACL 2021 full author list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "f78a59af-1957-4a83-b74f-709ace5164c9",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01KbQEwJVrsqQ81oFWdvzH13",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2831,
      "cache_read_input_tokens": 34832,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2831,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 93_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a7871f5d7a606af87",
  "tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "description": "Searching for RocketQA authors Yingqi Qu NAACL 2021 full citati…",
  "usage": {
    "total_tokens": 38568,
    "tool_uses": 26,
    "duration_ms": 63962
  },
  "last_tool_name": "WebSearch",
  "uuid": "dab6d29a-a7a1-46bd-959d-33fb77ca2908",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691"
}
```

---

### Tool call

_source line 94_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01E5NfYuStEgaKLKto9BGb5S`</summary>

```json
{
  "query": "RocketQA authors Yingqi Qu NAACL 2021 full citation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "3e95bf1b-2e67-4e82-b2dc-cc0177be3365",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01KbQEwJVrsqQ81oFWdvzH13",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2831,
      "cache_read_input_tokens": 34832,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2831,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 95_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a7871f5d7a606af87",
  "tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "description": "Searching for CAPSTONE \"curriculum sampling\" \"dense retrieval\" …",
  "usage": {
    "total_tokens": 38605,
    "tool_uses": 27,
    "duration_ms": 64780
  },
  "last_tool_name": "WebSearch",
  "uuid": "4bc025d2-3cd2-43bc-bfe3-4871d5c58afd",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691"
}
```

---

### Tool call

_source line 96_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01G53ngQr4EKcUdAvMGgnife`</summary>

```json
{
  "query": "CAPSTONE \"curriculum sampling\" \"dense retrieval\" EMNLP 2023 Xingwei He full authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "7ddb45f9-e5c2-470c-8038-925f82733014",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01KbQEwJVrsqQ81oFWdvzH13",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2831,
      "cache_read_input_tokens": 34832,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2831,
        "ephemeral_1h_input_tokens": 0
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

_source line 97 · 2026-05-15T04:17:26.778Z_

<details><summary>↩ Tool result · `toolu_019bn4XnticyEcBpy5HRaAnQ`</summary>

```text
Web search results for query: "CoSQA authors Junjie Huang Duyu Tang ACL 2021 full author list"

Links: [{"title":"GitHub - Jun-jie-Huang/CoCLR: Source Code for ACL-21 main conference paper \"CoSQA: 20,000+ Web Queries for Code Search and Question Answering\".","url":"https://github.com/Jun-jie-Huang/CoCLR"},{"title":"Junjie Huang - Homepage","url":"https://jun-jie-huang.github.io/"},{"title":"CoSQA: 20,000+ Web Queries for Code Search and Question Answering - ACL Anthology","url":"https://aclanthology.org/2021.acl-long.442/"},{"title":"[PDF] CoSQA: 20,000+ Web Queries for Code Search and Question Answering | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CoSQA:-20,000+-Web-Queries-for-Code-Search-and-Huang-Tang/0c21334be0228431d619a180c809b43be0065bdd"},{"title":"ACL-IJCNLP 2021","url":"https://2021.aclweb.org/registration/accept/"},{"title":"Junjie Huang - ACL Anthology","url":"https://aclanthology.org/people/j/junjie-huang/"},{"title":"CoSQA: 20,000+ Web Queries for Code Search and Question Answering - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/cosqa-20-000-web-queries-for-code-search-and-question-answering/"},{"title":"CoSQA: 20,000+ Web Queries for Code Search and Question Answering","url":"https://gengo.sotaro.io/2021.acl-long.442"},{"title":"CoSQA: 20,000+ Web Queries for Code Search and Question Answering | Request PDF","url":"https://www.researchgate.net/publication/351926082_CoSQA_20000_Web_Queries_for_Code_Search_and_Question_Answering"},{"title":"WhiteningBERT: An Easy Unsupervised Sentence Embedding Approach - ACL Anthology","url":"https://aclanthology.org/2021.findings-emnlp.23/"}]

Based on the search results, the full author list for the CoSQA paper published at ACL 2021 is: Junjie Huang, Duyu Tang, Linjun Shou, Ming Gong, Ke Xu, Daxin Jiang, Ming Zhou, and Nan Duan.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "bef46658-143e-47b1-84fe-df9c89aa7d9e"
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-15T04:17:29.495Z_

<details><summary>↩ Tool result · `toolu_01G53ngQr4EKcUdAvMGgnife`</summary>

```text
Web search results for query: "CAPSTONE "curriculum sampling" "dense retrieval" EMNLP 2023 Xingwei He full authors"

Links: [{"title":"CAPSTONE: Curriculum Sampling for Dense Retrieval with Document Expansion - ACL Anthology","url":"https://aclanthology.org/2023.emnlp-main.651/"},{"title":"CAPSTONE: Curriculum Sampling for Dense Retrieval with Document Expansion | OpenReview","url":"https://openreview.net/forum?id=Mefvmgkb9G&noteId=TlRvoprgev"},{"title":"[2212.09114] CAPSTONE: Curriculum Sampling for Dense Retrieval with Document Expansion","url":"https://arxiv.org/abs/2212.09114"},{"title":"GitHub - microsoft/SimXNS: SimXNS is a research project for information retrieval. This repo contains official implementations by MSRA NLC team.","url":"https://github.com/microsoft/SimXNS"},{"title":"dblp: Anlei Dong","url":"https://dblp.org/pid/28/6385.html"},{"title":"CAPSTONE: Curriculum Sampling for Dense Retrieval with Document Expansion","url":"https://openreview.net/pdf?id=Mefvmgkb9G"},{"title":"Curriculum Sampling for Dense Retrieval with Document ...","url":"https://aclanthology.org/2023.emnlp-main.651.pdf"},{"title":"Paper Digest: EMNLP-2023 Highlights (Full List)","url":"https://www.paperdigest.org/data/emnlp-2023-full.html"},{"title":"dblp: Jian Jiao 0007","url":"https://dblp.org/pid/29/265-7.html"},{"title":"Main Conference - EMNLP 2023","url":"https://2023.emnlp.org/program/accepted_main_conference/"}]

Based on the search results, I found the full author information for the CAPSTONE paper at EMNLP 2023:

The full authors are: Xingwei He, Yeyun Gong, A-Long Jin, Hang Zhang, Anlei Dong, Jian Jiao, Siu Yiu, and Nan Duan.

The paper is titled "CAPSTONE: Curriculum Sampling for Dense Retrieval with Document Expansion" and was published in Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing, pages 10531–10541, Singapore.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "894129cf-ecf1-4780-89ee-eaed43dff1ce"
}
```

</details>

---

### Tool result

_source line 99 · 2026-05-15T04:17:29.553Z_

<details><summary>↩ Tool result · `toolu_01E5NfYuStEgaKLKto9BGb5S`</summary>

```text
Web search results for query: "RocketQA authors Yingqi Qu NAACL 2021 full citation"

Links: [{"title":"RocketQA: An Optimized Training Approach to Dense Passage Retrieval for Open-Domain Question Answering - ACL Anthology","url":"https://aclanthology.org/2021.naacl-main.466/"},{"title":"RocketQA: An Optimized Training Approach to Dense Passage Retrieval for Open-Domain Question Answering | Request PDF","url":"https://www.researchgate.net/publication/352364344_RocketQA_An_Optimized_Training_Approach_to_Dense_Passage_Retrieval_for_Open-Domain_Question_Answering"},{"title":"dblp: RocketQA: An Optimized Training Approach to Dense Passage Retrieval for Open-Domain Question Answering.","url":"https://dblp.org/rec/conf/naacl/QuDLLRZDWW21.html"},{"title":"GitHub - PaddlePaddle/RocketQA: 🚀 RocketQA, dense retrieval for information retrieval and question answering, including both Chinese and English state-of-the-art models.","url":"https://github.com/PaddlePaddle/RocketQA"},{"title":"RocketQA/research/RocketQA_NAACL2021 at main · PaddlePaddle/RocketQA","url":"https://github.com/PaddlePaddle/RocketQA/tree/main/research/RocketQA_NAACL2021"},{"title":"Research/NLP/NAACL2021-RocketQA at master · PaddlePaddle/Research","url":"https://github.com/PaddlePaddle/Research/tree/master/NLP/NAACL2021-RocketQA"},{"title":"[PDF] RocketQA: An Optimized Training Approach to Dense Passage Retrieval for Open-Domain Question Answering | Semantic Scholar","url":"https://www.semanticscholar.org/paper/RocketQA:-An-Optimized-Training-Approach-to-Dense-Qu-Ding/f2c1ab4e850ad89bd6b6b9908e12a4151d152070"},{"title":"Google znalac","url":"https://scholar.google.com/scholar?q=Yingqi+Qu%2C+Yuchen+Ding%2C+Jing+Liu%2C+Kai+Liu%2C+Ruiyang+Ren%2C+Xin+Zhao%2C+Daxiang+Dong%2C+Hua+Wu%2C+and+Haifeng+Wang.+2021.+RocketQA%3A+An+Optimized+Training+Approach+to+Dense+Passage+Retrieval+for+Open-Domain+Question+Answering.+NAACL."},{"title":"DL-NLP-Readings/Bibtex/RocketQA - An Optimized Training Approach to Dense Passage Retrieval for Open-Domain Question Answering.bib at master · 26hzhang/DL-NLP-Readings","url":"https://github.com/26hzhang/DL-NLP-Readings/blob/master/Bibtex/RocketQA%20-%20An%20Optimized%20Training%20Approach%20to%20Dense%20Passage%20Retrieval%20for%20Open-Domain%20Question%20Answering.bib"},{"title":"Accepted Papers - NAACL-HLT 2021","url":"https://2021.naacl.org/program/accepted/"}]

Based on the search results, here is the full citation for RocketQA by Yingqi Qu and colleagues at NAACL 2021:

Yingqi Qu, Yuchen Ding, Jing Liu, Kai Liu, Ruiyang Ren, Wayne Xin Zhao, Daxiang Dong, Hua Wu, and Haifeng Wang. 2021. RocketQA: An Optimized Training Approach to Dense Passage Retrieval for Open-Domain Question Answering. In Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, pages 5835–5847, Online. Association for Computational Linguistics.

**BibTeX Format:**
@inproceedings{qu-etal-2021-rocketqa, title = "{R}ocket{QA}: An Optimized Training Approach to Dense Passage Retrieval for Open-Domain Question Answering", author = "Qu, Yingqi and Ding, Yuchen and Liu, Jing and Liu, Kai and Ren, Ruiyang and Zhao, Wayne Xin and Dong, Daxiang and Wu, Hua and Wang, Haifeng", booktitle = "Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies", month = jun, year = "2021", address = "Online", publisher = "Association for Computational Linguistics", url = "https://aclanthology.org/2021.naacl-main.466", doi = "10.18653/v1/2021.naacl-main.466", pages = "5835--5847"}


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "d06ea0d9-75d5-4e2d-9218-94f476d07385"
}
```

</details>

---

### System

_source line 100_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a7871f5d7a606af87",
  "tool_use_id": "toolu_01JBrYzVEEU9YDuhmDfQg3z3",
  "status": "completed",
  "output_file": "",
  "summary": "Search gap area papers",
  "usage": {
    "total_tokens": 41599,
    "tool_uses": 27,
    "duration_ms": 105956
  },
  "uuid": "1369abac-d936-48c0-8a95-92995eda7f2e",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691"
}
```

---

### Tool result

_source line 101 · 2026-05-15T04:18:05.963Z_

<details><summary>↩ Tool result · `toolu_01JBrYzVEEU9YDuhmDfQg3z3`</summary>

```text
Here is the verified list, grouped by area. All papers were confirmed via web search with ACL Anthology, DBLP, proceedings pages, or arXiv records.

---

**Area 1: Contrastive Learning for Code**

**1. ContraCode: Contrastive Code Representation Learning**
- Authors: Paras Jain, Ajay Jain, Tianjun Zhang, et al. (Pieter Abbeel, Joseph Gonzalez, Ion Stoica)
- Venue/Year: EMNLP 2021
- Relevance: Directly precedent work using compiler-based semantic-preserving augmentations for contrastive code pre-training; contrasting functionally equivalent programs is the code-specific analog of structure-guided hard negative construction.

**2. SynCoBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation**
- Authors: Xin Wang, Yasheng Wang, Fei Mi, et al.
- Venue/Year: arXiv 2021 (widely cited preprint; no confirmed top-venue proceedings publication found — treat as arXiv cite)
- Relevance: Uses AST edges and multi-modal contrastive objectives over code/comment/AST triples, making it the closest prior work to structure-aware contrastive learning for code retrieval.

**3. ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning**
- Authors: Shangqing Liu, Bozhi Wu, Xiaofei Xie, Guozhu Meng, Yang Liu
- Venue/Year: ICSE 2023
- Relevance: Applies contrastive learning with nine program-level augmentation operators to improve code pre-trained model robustness; directly related to contrastive objectives for code representation.

---

**Area 2: Hard Negative Mining in Dense Retrieval**

**4. RocketQA: An Optimized Training Approach to Dense Passage Retrieval for Open-Domain Question Answering**
- Authors: Yingqi Qu, Yuchen Ding, Jing Liu, et al. (Kai Liu, Ruiyang Ren, Wayne Xin Zhao, Daxiang Dong, Hua Wu, Haifeng Wang)
- Venue/Year: NAACL 2021
- Relevance: Introduces denoised hard negative sampling (using a cross-encoder to filter false negatives) as a core training technique for dense retrieval; the structural-denoising intuition transfers directly to call-graph-grounded negatives.

**5. Effective Hard Negative Mining for Contrastive Learning-Based Code Search**
- Authors: Fan Y., Li C., Ge J., et al. (Huang L., Luo B.)
- Venue/Year: ACM Transactions on Software Engineering and Methodology (TOSEM), 2024
- Relevance: The most directly related prior work — proposes hard negative mining specifically for contrastive code search, making it a mandatory baseline/contrast point for the paper.

**6. CAPSTONE: Curriculum Sampling for Dense Retrieval with Document Expansion**
- Authors: Xingwei He, Yeyun Gong, A-Long Jin, et al. (Hang Zhang, Anlei Dong, Jian Jiao, Siu Ming Yiu, Nan Duan)
- Venue/Year: EMNLP 2023
- Relevance: Demonstrates progressive difficulty scheduling of training samples for dense retrieval; supports the curriculum/difficulty-graded framing of structure-grounded hard negatives.

---

**Area 3: Code Search / Dense Retrieval for Code**

**7. CoSQA: 20,000+ Web Queries for Code Search and Question Answering**
- Authors: Junjie Huang, Duyu Tang, Linjun Shou, et al. (Ming Gong, Ke Xu, Daxin Jiang, Ming Zhou, Nan Duan)
- Venue/Year: ACL 2021
- Relevance: Standard benchmark for code search evaluation and introduces CoCLR (contrastive learning for code-query matching); a natural evaluation target and citation for the code retrieval problem formulation.

---

**Area 4: Repository-level Code Understanding**

**8. CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion**
- Authors: Yangruibo Ding, Zijian Wang, Wasi Uddin Ahmad, et al. (Hantian Ding, Ming Tan, Nihal Jain, Murali Krishna Ramanathan, Ramesh Nallapati, Parminder Bhatia, Dan Roth, Bing Xiang)
- Venue/Year: NeurIPS 2023 (Datasets & Benchmarks Track)
- Relevance: Establishes the need for cross-file structural understanding in code tasks; motivates call-graph-level context as essential for realistic repository-scale code retrieval.

---

**Area 5: Program Analysis meets Deep Learning**

**9. ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations**
- Authors: Chris Cummins, Zacharias Fisches, Tal Ben-Nun, et al. (Torsten Hoefler, Michael O'Boyle, Hugh Leather)
- Venue/Year: ICML 2021
- Relevance: Canonical work on representing programs as control/data/call-flow graphs for ML; foundational justification for using call graphs and data-flow edges as structural signals in hard negative construction.

---

**Notes on gaps not filled:**
- "DISCO" as a code contrastive learning paper: no paper matching this name and description in code NLP was found — likely does not exist or uses a different title. Not included.
- Area 6 (curriculum for retrieval) is covered by CAPSTONE (Area 2, paper #6) rather than a separate entry, since no additional independently verified paper was found that specifically combines curriculum + data quality + code retrieval.
- SynCoBERT has no confirmed top-venue proceedings page; it remains an arXiv preprint. Include it only if your venue accepts arXiv cites.

Sources:
- [ContraCode — ACL Anthology EMNLP 2021](https://aclanthology.org/2021.emnlp-main.482/)
- [SynCoBERT — arXiv 2108.04556](https://arxiv.org/abs/2108.04556)
- [ContraBERT — ICSE 2023 ACM DL](https://dl.acm.org/doi/abs/10.1109/ICSE48619.2023.00207)
- [RocketQA — ACL Anthology NAACL 2021](https://aclanthology.org/2021.naacl-main.466/)
- [Effective Hard Negative Mining for Code Search — TOSEM 2024](https://dl.acm.org/doi/full/10.1145/3695994)
- [CAPSTONE — ACL Anthology EMNLP 2023](https://aclanthology.org/2023.emnlp-main.651/)
- [CoSQA — ACL Anthology ACL 2021](https://aclanthology.org/2021.acl-long.442/)
- [CrossCodeEval — NeurIPS 2023 Proceedings](https://proceedings.neurips.cc/paper_files/paper/2023/hash/920f2dced7d32ab2ba2f1970bc306af6-Abstract-Datasets_and_Benchmarks.html)
- [ProGraML — ICML 2021 Proceedings](https://proceedings.mlr.press/v139/cummins21a.html)

agentId: a7871f5d7a606af87 (use SendMessage with to: 'a7871f5d7a606af87' to continue this agent)
&lt;usage>total_tokens: 42557
tool_uses: 27
duration_ms: 105964&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "bb134b9d-c732-47b6-b917-1014c340e713",
  "tool_use_result": {
    "status": "completed",
    "prompt": "I need to find real, verified academic papers to fill citation gaps for a paper about using code structure (call graph / data-flow) for contrastive learning hard negative mining in code retrieval. The paper already has 39 citations but needs better coverage in certain areas.\n\nSearch for the following papers using WebSearch. For each paper, confirm: title, authors, venue, year. Only return papers you can verify exist.\n\n**Area 1: Contrastive Learning for Code (need 2-3 more)**\n- Search: \"contrastive learning code representation 2022 2023 2024 ACL EMNLP ICLR NeurIPS\"\n- Look for: SynCoBERT, DISCO, or other contrastive code learning papers\n- Search: \"self-supervised code understanding contrastive pre-training\"\n\n**Area 2: Hard Negative Mining in Dense Retrieval (need 1-2 more)**\n- Search: \"RocketQA hard negative mining dense retrieval 2021\"\n- Search: \"hard negative mining contrastive learning survey 2023 2024\"\n- Search: \"debiased contrastive learning hard negatives retrieval\"\n\n**Area 3: Code Search / Dense Retrieval for Code (need 1-2)**\n- Search: \"dense code retrieval neural code search 2023 2024 ICSE FSE\"\n- Search: \"CoSQA code search question answering benchmark\"\n\n**Area 4: Repository-level Code Understanding (need 1-2)**\n- Search: \"repository level code understanding cross-file context 2024\"\n- Search: \"CrossCodeEval benchmark cross-file code completion\"\n\n**Area 5: Program Analysis meets Deep Learning (need 1)**\n- Search: \"ProGraML program graph machine learning 2021\"\n- Search: \"learning program semantics graph neural network ICML NeurIPS\"\n\n**Area 6: Training Data Quality / Curriculum for Retrieval (need 1)**\n- Search: \"data quality curriculum learning dense retrieval 2023 2024\"\n\nFor each paper found, provide:\n- Exact title\n- Authors (first 3 + et al.)\n- Venue and year\n- One sentence on why it's relevant to a paper about structure-grounded hard negative mining for code retrieval\n\nReturn a clean list grouped by area. Only include papers you verified via web search.",
    "agentId": "a7871f5d7a606af87",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is the verified list, grouped by area. All papers were confirmed via web search with ACL Anthology, DBLP, proceedings pages, or arXiv records.\n\n---\n\n**Area 1: Contrastive Learning for Code**\n\n**1. ContraCode: Contrastive Code Representation Learning**\n- Authors: Paras Jain, Ajay Jain, Tianjun Zhang, et al. (Pieter Abbeel, Joseph Gonzalez, Ion Stoica)\n- Venue/Year: EMNLP 2021\n- Relevance: Directly precedent work using compiler-based semantic-preserving augmentations for contrastive code pre-training; contrasting functionally equivalent programs is the code-specific analog of structure-guided hard negative construction.\n\n**2. SynCoBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation**\n- Authors: Xin Wang, Yasheng Wang, Fei Mi, et al.\n- Venue/Year: arXiv 2021 (widely cited preprint; no confirmed top-venue proceedings publication found — treat as arXiv cite)\n- Relevance: Uses AST edges and multi-modal contrastive objectives over code/comment/AST triples, making it the closest prior work to structure-aware contrastive learning for code retrieval.\n\n**3. ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning**\n- Authors: Shangqing Liu, Bozhi Wu, Xiaofei Xie, Guozhu Meng, Yang Liu\n- Venue/Year: ICSE 2023\n- Relevance: Applies contrastive learning with nine program-level augmentation operators to improve code pre-trained model robustness; directly related to contrastive objectives for code representation.\n\n---\n\n**Area 2: Hard Negative Mining in Dense Retrieval**\n\n**4. RocketQA: An Optimized Training Approach to Dense Passage Retrieval for Open-Domain Question Answering**\n- Authors: Yingqi Qu, Yuchen Ding, Jing Liu, et al. (Kai Liu, Ruiyang Ren, Wayne Xin Zhao, Daxiang Dong, Hua Wu, Haifeng Wang)\n- Venue/Year: NAACL 2021\n- Relevance: Introduces denoised hard negative sampling (using a cross-encoder to filter false negatives) as a core training technique for dense retrieval; the structural-denoising intuition transfers directly to call-graph-grounded negatives.\n\n**5. Effective Hard Negative Mining for Contrastive Learning-Based Code Search**\n- Authors: Fan Y., Li C., Ge J., et al. (Huang L., Luo B.)\n- Venue/Year: ACM Transactions on Software Engineering and Methodology (TOSEM), 2024\n- Relevance: The most directly related prior work — proposes hard negative mining specifically for contrastive code search, making it a mandatory baseline/contrast point for the paper.\n\n**6. CAPSTONE: Curriculum Sampling for Dense Retrieval with Document Expansion**\n- Authors: Xingwei He, Yeyun Gong, A-Long Jin, et al. (Hang Zhang, Anlei Dong, Jian Jiao, Siu Ming Yiu, Nan Duan)\n- Venue/Year: EMNLP 2023\n- Relevance: Demonstrates progressive difficulty scheduling of training samples for dense retrieval; supports the curriculum/difficulty-graded framing of structure-grounded hard negatives.\n\n---\n\n**Area 3: Code Search / Dense Retrieval for Code**\n\n**7. CoSQA: 20,000+ Web Queries for Code Search and Question Answering**\n- Authors: Junjie Huang, Duyu Tang, Linjun Shou, et al. (Ming Gong, Ke Xu, Daxin Jiang, Ming Zhou, Nan Duan)\n- Venue/Year: ACL 2021\n- Relevance: Standard benchmark for code search evaluation and introduces CoCLR (contrastive learning for code-query matching); a natural evaluation target and citation for the code retrieval problem formulation.\n\n---\n\n**Area 4: Repository-level Code Understanding**\n\n**8. CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion**\n- Authors: Yangruibo Ding, Zijian Wang, Wasi Uddin Ahmad, et al. (Hantian Ding, Ming Tan, Nihal Jain, Murali Krishna Ramanathan, Ramesh Nallapati, Parminder Bhatia, Dan Roth, Bing Xiang)\n- Venue/Year: NeurIPS 2023 (Datasets & Benchmarks Track)\n- Relevance: Establishes the need for cross-file structural understanding in code tasks; motivates call-graph-level context as essential for realistic repository-scale code retrieval.\n\n---\n\n**Area 5: Program Analysis meets Deep Learning**\n\n**9. ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations**\n- Authors: Chris Cummins, Zacharias Fisches, Tal Ben-Nun, et al. (Torsten Hoefler, Michael O'Boyle, Hugh Leather)\n- Venue/Year: ICML 2021\n- Relevance: Canonical work on representing programs as control/data/call-flow graphs for ML; foundational justification for using call graphs and data-flow edges as structural signals in hard negative construction.\n\n---\n\n**Notes on gaps not filled:**\n- \"DISCO\" as a code contrastive learning paper: no paper matching this name and description in code NLP was found — likely does not exist or uses a different title. Not included.\n- Area 6 (curriculum for retrieval) is covered by CAPSTONE (Area 2, paper #6) rather than a separate entry, since no additional independently verified paper was found that specifically combines curriculum + data quality + code retrieval.\n- SynCoBERT has no confirmed top-venue proceedings page; it remains an arXiv preprint. Include it only if your venue accepts arXiv cites.\n\nSources:\n- [ContraCode — ACL Anthology EMNLP 2021](https://aclanthology.org/2021.emnlp-main.482/)\n- [SynCoBERT — arXiv 2108.04556](https://arxiv.org/abs/2108.04556)\n- [ContraBERT — ICSE 2023 ACM DL](https://dl.acm.org/doi/abs/10.1109/ICSE48619.2023.00207)\n- [RocketQA — ACL Anthology NAACL 2021](https://aclanthology.org/2021.naacl-main.466/)\n- [Effective Hard Negative Mining for Code Search — TOSEM 2024](https://dl.acm.org/doi/full/10.1145/3695994)\n- [CAPSTONE — ACL Anthology EMNLP 2023](https://aclanthology.org/2023.emnlp-main.651/)\n- [CoSQA — ACL Anthology ACL 2021](https://aclanthology.org/2021.acl-long.442/)\n- [CrossCodeEval — NeurIPS 2023 Proceedings](https://proceedings.neurips.cc/paper_files/paper/2023/hash/920f2dced7d32ab2ba2f1970bc306af6-Abstract-Datasets_and_Benchmarks.html)\n- [ProGraML — ICML 2021 Proceedings](https://proceedings.mlr.press/v139/cummins21a.html)"
      }
    ],
    "totalDurationMs": 105964,
    "totalTokens": 42557,
    "totalToolUseCount": 27,
    "usage": {
      "input_tokens": 688,
      "cache_creation_input_tokens": 2306,
      "cache_read_input_tokens": 37663,
      "output_tokens": 1900,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2306
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 688,
          "output_tokens": 1900,
          "cache_read_input_tokens": 37663,
          "cache_creation_input_tokens": 2306,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2306,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 27
    }
  }
}
```

</details>

---

### Assistant

_source line 102_

<details><summary>Logged reasoning block</summary>

```text
Now I have the gap analysis results. Let me compile the full report.

Current citations by category:
1. code_retrieval_bug_fixing: 8 papers
2. hard_negative_mining: 6 papers (DPR, ANCE, SimCLR, SBERT, CL-DRD, CoCoHaNeRe)
3. contrastive_code_learning: 3 papers (ContraCode, CodeRetriever, Ding et al.)


4. program_analysis_for_ml: 6 papers (CodeQL tool, code2vec, code2seq, FA-AST, GraphCodeBERT, ARISE)
5. code_embeddings_search: 9 papers
6. graph_guided_inference: 8 papers total (5 in the literature map plus CodeRAG and CodeGRAG from memory, with ARISE already counted in category 4)
7. infrastructure: 2 papers (FAISS, Tree-sitter)

That gives me 39 unique papers across the literature map and memory combined.

Now I'm checking the gap analysis. The well-covered areas are clear: SWE-bench ecosystem with 8 papers, code embeddings and search with 9, graph-guided inference with 8 total, and program analysis for ML with 6. But I'm seeing some weak spots that need attention—contrastive learning for code only has 3 papers, so I should look into adding SynCoBERT and other approaches there.

Hard negative mining is thin on recent work, so RocketQA and CAPSTONE would help. I also want to add CrossCodeEval for repository-level understanding, ProGraML for combining program analysis with deep learning, and CoSQA for code search benchmarks. I need to be careful not to duplicate—ContraCode and CoCoHaNeRe are already in the literature map, so those don't need adding. Looking at the new candidates: SynCoBERT from 2021 covers contrastive code learning with syntax, ContraBERT from ICSE 2023 handles contrastive pre-training, and RocketQA from NAACL 2021 addresses hard negative mining.

Adding these papers would expand the collection from 39 to 46 entries, and now I'm ready to put together the report.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "f19fac53-97ad-4ed1-aa7d-642548a573b8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Eyb74KgpC6VFimPNwpMT2C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4349,
      "cache_read_input_tokens": 36885,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4349
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

_source line 103_

Analysis complete. Let me compile the gap report. Current state:

**literature_map.yaml**: 39 entries across 7 categories. Memory.md adds 2 more (CodeRAG, CodeGRAG) = ~41 unique references.

The count (39) already exceeds 25+, but coverage is uneven. Let me write the gap analysis report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "ea5986e7-8ed4-4630-8d48-8b6fbd7a0a4e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Eyb74KgpC6VFimPNwpMT2C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4349,
      "cache_read_input_tokens": 36885,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4349
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

_source line 104_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01T7hGQpha5DUJTPZPzjMwjs`</summary>

```json
{
  "project": "structfuse-context",
  "file": "memory.md",
  "max_chars": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "3a185555-db60-4336-9700-73241b6216bc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Eyb74KgpC6VFimPNwpMT2C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4349,
      "cache_read_input_tokens": 36885,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4349
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

_source line 105 · 2026-05-15T04:18:24.225Z_

<details><summary>↩ Tool result · `toolu_01T7hGQpha5DUJTPZPzjMwjs`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/memory.md\", \"content\": \"# Inference-Time Graph Methods 文献对比\\n\\n## 对比表\\n\\n| Method | Paper | Venue | Graph Type | Usage Stage | Inter-proc Data-Flow | Task | Scalability | Key Diff from StructFuse |\\n|--------|-------|-------|-----------|-------------|---------------------|------|-------------|--------------------------|\\n| **CodexGraph** | Bridging LLMs and Code Repositories via Code Graph Databases | NAACL 2025 (arXiv:2408.03910) | Code graph DB (MODULE/CLASS/FUNCTION nodes; CONTAINS/INHERITS/USES edges) | Inference-time | \\n\\n... [截断: 省略 12463 字符，传 max_chars=0 获取完整内容]\", \"total_chars\": 12963, \"truncated\": true}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "c67b422d-ca21-4f83-8513-e0ee601946a3",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/memory.md\\\", \\\"content\\\": \\\"# Inference-Time Graph Methods 文献对比\\\\n\\\\n## 对比表\\\\n\\\\n| Method | Paper | Venue | Graph Type | Usage Stage | Inter-proc Data-Flow | Task | Scalability | Key Diff from StructFuse |\\\\n|--------|-------|-------|-----------|-------------|---------------------|------|-------------|--------------------------|\\\\n| **CodexGraph** | Bridging LLMs and Code Repositories via Code Graph Databases | NAACL 2025 (arXiv:2408.03910) | Code graph DB (MODULE/CLASS/FUNCTION nodes; CONTAINS/INHERITS/USES edges) | Inference-time | \\\\n\\\\n... [截断: 省略 12463 字符，传 max_chars=0 获取完整内容]\\\", \\\"total_chars\\\": 12963, \\\"truncated\\\": true}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/memory.md\", \"content\": \"# Inference-Time Graph Methods 文献对比\\n\\n## 对比表\\n\\n| Method | Paper | Venue | Graph Type | Usage Stage | Inter-proc Data-Flow | Task | Scalability | Key Diff from StructFuse |\\n|--------|-------|-------|-----------|-------------|---------------------|------|-------------|--------------------------|\\n| **CodexGraph** | Bridging LLMs and Code Repositories via Code Graph Databases | NAACL 2025 (arXiv:2408.03910) | Code graph DB (MODULE/CLASS/FUNCTION nodes; CONTAINS/INHERITS/USES edges) | Inference-time | \\n\\n... [截断: 省略 12463 字符，传 max_chars=0 获取完整内容]\", \"total_chars\": 12963, \"truncated\": true}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 106_

<details><summary>Logged reasoning block</summary>

```text
Now let me write the gap analysis and append it to memory.md. I need to use save_project_file to write the full content. But since save_project_file writes the full file content, I need to read the full memory.md first and then append.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "79a0bf13-f7f5-4d7d-9847-d818e69de85e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EkpJMFSVpYqqUvf68Lj7Lh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1319,
      "cache_read_input_tokens": 41234,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1319
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

_source line 107_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_014rSVYBMdVNxnQTFfTj9P4a`</summary>

```json
{
  "project": "structfuse-context",
  "file": "memory.md",
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
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "55f003b5-ba7b-4be0-93c1-5c4a462017e5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EkpJMFSVpYqqUvf68Lj7Lh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1319,
      "cache_read_input_tokens": 41234,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1319
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

_source line 108 · 2026-05-15T04:18:27.935Z_

<details><summary>↩ Tool result · `toolu_014rSVYBMdVNxnQTFfTj9P4a`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/memory.md\", \"content\": \"# Inference-Time Graph Methods 文献对比\\n\\n## 对比表\\n\\n| Method | Paper | Venue | Graph Type | Usage Stage | Inter-proc Data-Flow | Task | Scalability | Key Diff from StructFuse |\\n|--------|-------|-------|-----------|-------------|---------------------|------|-------------|--------------------------|\\n| **CodexGraph** | Bridging LLMs and Code Repositories via Code Graph Databases | NAACL 2025 (arXiv:2408.03910) | Code graph DB (MODULE/CLASS/FUNCTION nodes; CONTAINS/INHERITS/USES edges) | Inference-time | No. Static analysis for symbol relations only | General repo-level coding (completion, issue resolution) | CrossCodeEval, SWE-bench, EvoCodeBench | Agent queries graph DB at inference; task-agnostic schema but no data-flow semantics |\\n| **LocAgent** | Graph-Guided LLM Agents for Code Localization | ACL 2025 (arXiv:2503.09089) | Directed heterogeneous graph (code entities + dependency edges) | Inference-time | No. Dependency edges, not data-flow | Fault localization | 92.7% file-level accuracy; SWE-bench +12% Pass@10 | Agent multi-hop graph reasoning at inference; needs fine-tuned 32B model |\\n| **RANGER** | RANGER — Repository-Level Agent for Graph-Enhanced Retrieval | arXiv:2509.25257 (Sep 2025) | Knowledge graph + MCTS traversal | Inference-time | No | Code search, QA, cross-file retrieval, completion | CodeSearchNet, RepoQA, RepoBench, CrossCodeEval | MCTS-guided graph exploration; dual-stage (Cypher + MCTS); higher inference cost due to cross-encoder scoring |\\n| **RepoGraph** | Enhancing AI SE with Repository-level Code Graph | ICLR 2025 (arXiv:2410.14684) | Repo-level code graph (class hierarchy, call graph, file structure) | Inference-time | No. Structural relations only | Software engineering / issue resolution | SWE-bench (+32.8% relative); CrossCodeEval | Plug-in module for existing agents; repo-wide navigation; no semantic analysis |\\n| **GraphCoder** | Enhancing Repo-Level Code Completion via Code Context Graph | ASE 2024 (arXiv:2406.07003) | Code Context Graph (CFG + CDG + DDG) | Inference-time | Partial. Data dependence graph but **intra-procedural** only | Code completion | Repository-level benchmarks | Coarse-to-fine retrieval with CCG; closest to StructFuse in using data/control flow, but intra-proc and at inference-time |\\n| **CodeRAG** | Supportive Code Retrieval on Bigraph for Real-World Code Generation | arXiv:2504.10046 (Apr 2025) | Bigraph (requirement graph + DS-code graph) | Inference-time | No. Dependency + semantic edges | Repo-level code generation | DevEval (+40.90 Pass@1 w/ GPT-4o) | Dual-graph (requirements + code); agentic reasoning; high inference overhead |\\n| **ARISE** | ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair | arXiv:2605.03117 (May 2026), Seddik & Fard | Multi-granularity program graph (statement nodes + def-use edges) | Inference-time | Partial. **Intra-procedural** def-use edges + data-flow slicing tool | Fault localization + repair | SWE-bench Lite (300 issues); +17.0 Function Recall@1 | Closest to StructFuse in data-flow usage; but intra-proc only, agent queries at inference |\\n| **CodeGRAG** | Bridging NL and PL via Graphical RAG | arXiv:2405.02355 (2024) | Composed syntax graph (AST + DFG + CFG) | Both (GNN training + graph prompt at inference) | Partial. DFG extraction but function-level | Code generation (cross-lingual) | Multiple PLs | Only method with training-time component (GNN soft prompts); but graph also used at inference |\\n| **StructFuse** (Ours) | Structure-Grounded Hard Negatives via CodeQL Data-Flow | — | Inter-procedural data-flow graph (CodeQL taint tracking) | **Training-time only** | **Yes. Full inter-procedural** (source→sink across call boundaries) | Code retrieval (contrastive training) | Large-scale repos with CodeQL | Zero inference overhead; graph used offline for negative mining; inter-proc data-flow |\\n\\n## Discussion 要点\\n\\n### StructFuse vs Inference-Time Graph Methods: 互补性与差异性\\n\\n1. **Cost-accuracy tradeoff**: Inference-time methods (CodexGraph, RANGER, RepoGraph) achieve high precision by constructing and querying graphs per request, but incur significant latency (graph construction + traversal + LLM calls). StructFuse amortizes all graph computation to training time—once the encoder is trained with structure-grounded negatives, inference is a single embedding lookup with zero graph overhead. This makes StructFuse suitable for latency-sensitive production retrieval where inference-time graph methods are impractical.\\n\\n2. **Data-flow depth**: Most inference-time methods use structural graphs (call graphs, class hierarchies, file dependencies). Only GraphCoder and ARISE incorporate data/control flow, but limited to **intra-procedural** scope. StructFuse uniquely leverages **inter-procedural** data-flow via CodeQL's taint tracking, capturing cross-function semantic relationships (e.g., a sanitizer function that transforms data between source and sink across call boundaries). This deeper semantic signal generates harder, more informative negatives.\\n\\n3. **Complementarity**: StructFuse and inference-time methods are orthogonal and composable. A StructFuse-trained encoder can serve as the embedding backbone for systems like RANGER or CodexGraph, providing better initial retrieval that reduces the graph agent's search space. Conversely, inference-time graph methods can provide reranking on top of StructFuse retrieval for tasks requiring maximum precision.\\n\\n4. **Scalability model**: Inference-time methods scale linearly with query volume (each query triggers graph operations). StructFuse's cost is front-loaded: CodeQL analysis runs once per repository update, and the resulting negatives improve the encoder permanently. For high-QPS code search services, this one-time investment yields compounding returns.\\n\\n5. **Task generality vs specialization**: Inference-time graph agents (CodexGraph, RepoGraph) are task-agnostic but require powerful LLMs as backends. StructFuse produces a specialized retrieval encoder that excels at the code search task without LLM inference, making it deployable as a lightweight, efficient first-stage retriever in multi-stage pipelines.\\n\\n## Related Work 段落草稿 (~200 words)\\n\\n**Graph-Based Methods for Code Understanding.**\\nRecent work has explored leveraging code graphs to enhance LLM-based software engineering. Inference-time approaches construct and query graphs during each interaction: CodexGraph (Liu et al., NAACL 2025) builds a code graph database that LLM agents query via structured interfaces; RepoGraph (Ouyang et al., ICLR 2025) provides repository-level navigation as a plug-in module for SE agents; LocAgent (ACL 2025) and RANGER (Shah et al., 2025) employ graph-guided multi-hop reasoning and MCTS-based traversal for code localization and retrieval, respectively. GraphCoder (ASE 2024) incorporates intra-procedural control-flow and data-dependence graphs for code completion retrieval, while ARISE (Seddik & Fard, 2026) extends this with statement-level def-use edges for fault localization. CodeGRAG (2024) bridges training and inference by using GNN-encoded graph prompts.\\n\\nThese methods achieve strong results but impose substantial inference-time costs—graph construction, traversal, and often multiple LLM calls per query. Moreover, their data-flow analysis remains intra-procedural. StructFuse takes a fundamentally different approach: we leverage CodeQL's inter-procedural taint tracking to generate structure-grounded hard negatives at **training time**, producing an encoder that captures cross-function data-flow semantics without any graph overhead at inference. This positions StructFuse as complementary to inference-time graph methods—it can serve as an efficient first-stage retriever whose embeddings already encode deep structural relationships that other methods must compute on-the-fly.\\n\\n---\\n\\n## 参考文献（全部已验证 2026-05-14）\\n\\n- CodexGraph: arXiv:2408.03910, Liu et al., NAACL 2025\\n- LocAgent: arXiv:2503.09089, Chen et al., ACL 2025\\n- RANGER: arXiv:2509.25257, Shah et al., 2025 ✅ verified\\n- RepoGraph: arXiv:2410.14684, Ouyang et al., ICLR 2025\\n- GraphCoder: arXiv:2406.07003, Liu et al., ASE 2024\\n- CodeRAG: arXiv:2504.10046, 2025\\n- ARISE: arXiv:2605.03117, Seddik & Fard, 2026 ✅ verified (full title: \\\"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair\\\")\\n- CodeGRAG: arXiv:2405.02355, 2024\\n\\n---\\n\\n## Checkpoint Criterion 与 K 分析 (2026-05-15)\\n\\n**Checkpoint 选择 criterion 分歧率**：4 个完成的 full M2 runs 中，2/4 (50%) val_loss 与 R@1 选中不同 checkpoint。\\n\\n**分歧 pattern**：\\n- Qwen s43: val_loss→step 500, R@1→step 1500, R@1 差 +1.97pp\\n- StarCoder s42: val_loss→step 1000, R@1→step 2500, R@1 差 +0.64pp\\n- Mean delta: +0.65pp (R@1 criterion 优于 val_loss criterion)\\n- StarCoder 步差更大（1500 步 vs 1000 步），与其 pretrained margin 更大的特性一致\\n\\n**论文写作决策**：主表报 best_by_R@1（target metric aligned），ablation 表展示两种 criterion 对比（D036 已决策 R@1 为 primary）。\\n\\n**K=7 无 ablation**：所有正式实验固定 K=7。合理性来源：(1) batch_size=8 对齐（1 positive + 7 negatives = 8）(2) DPR 等文献惯例 (3) hard_negative_ratio=0.5 平衡设计。K 敏感性列为 limitation/future work。\\n\\n---\\n\\n## BM25 Negative Mining 策略洞察 (2026-05-14, updated)\\n\\n**两层重叠率数据（注意区分）**：\\n- **k=50 全候选重叠**（mining worker 报告）：BM25 vs embedding 87.1%, vs random 76.2%, vs dataflow 71.8%\\n- **top-7 Jaccard**（训练实际用的 num_negatives=7，分层分析）：差异远大于全候选\\n\\n**分层 top-7 Jaccard 重叠率**（seed 42, 2920 matched queries / 12290 total）：\\n| 层级 | BM25 vs Embedding | BM25 vs Random | BM25 vs Dataflow |\\n|------|-------------------|----------------|------------------|\\n| Small (<50 files, 39 repos) | 0.668 | 0.411 | 0.667 |\\n| Medium (50-200, 29 repos) | 0.380 | 0.067 | 0.363 |\\n| Large (200+, 15 repos) | 0.297 | 0.007 | 0.405 |\\n\\n**核心修正**：之前基于 87% 预测\\\"Phase 2 中 BM25 R@1 很可能接近 embedding\\\"——这个预测可能不成立。在中大 repo（训练数据主体）上 top-7 Jaccard 仅 30-38%，BM25 和 embedding 选出的训练 negatives 大部分不同。Phase 2 训练结果将真正区分两种策略。\\n\\n**意外发现**：BM25 vs dataflow 在大 repo 上重叠率（0.405）高于 vs embedding（0.297）。词汇相似性信号与数据流依赖有部分对齐，而纯 embedding 距离选择了不同维度的 hard negatives。\\n\\n---\\n\\n## hard_negative_mining.py vs build_m1_training_data.py 实现差异 [2026-05-15]\\n\\n**发现者**：Reviewer\\n**影响**：当前 M2 不受影响（用 pre-mined 数据），plan_015（dynamic negative mining）实施前必须对齐\\n\\n**差异**：\\n\\n### hard_negative_mining.py `DataFlowAwareMiner`（training/hard_negative_mining.py）\\n三步法：\\n1. **Embedding top-K**：调用 `EmbeddingDistanceMiner.mine()` 获取 top-50 cosine similarity 最高的 candidates（从所有 non-positive candidates 中）\\n2. **Dataflow filter**：过滤掉 `_is_reachable(query, fid)` 为 True 的文件——仅检查 `dataflow_graph[src]` 中的直接条目（1-hop 可达性）\\n3. **BM25 re-rank**：如果 `bm25_index` 可用，对剩余 disconnected candidates 按 BM25 分数降序重排\\n4. **Fallback**：如果 disconnected 不足 `num_negatives`，用 random padding 补足\\n\\n### build_m1_training_data.py `build_candidate_pools()`（scripts/build_m1_training_data.py）\\n两步法：\\n1. **Dataflow filter**：从 `non_pos_files` 中排除 `full_connected_set`（= `positive_files ∪ cg_connected`，即 dataflow 直连 + call graph 邻居——比 `DataFlowAwareMiner` 排除范围更广）\\n2. **BM25 sort**：对 disconnected 文件按 BM25 分数降序排序，取 top-K（pool_size=50）\\n3. **无 embedding 步骤**：dataflow pool 完全不使用 embedding 信号\\n\\n额外注意：当 `--model-path` 未提供时，`emb_scores = bm25`（line 317-318），此时 embedding pool 也退化为 BM25 排序，仅在是否排除 `full_connected` 上与 dataflow pool 不同。\\n\\n### 差异总结\\n\\n| 维度 | hard_negative_mining.py | build_m1_training_data.py |\\n|------|------------------------|--------------------------|\\n| Candidate 初筛 | Embedding cosine top-50 | 全部 non-positive（无初筛） |\\n| Dataflow 排除范围 | `dataflow_graph[src]` 直接条目 | `positive_files ∪ cg_connected`（更广） |\\n| 排序信号 | Embedding 为主 → BM25 re-rank | 纯 BM25 排序 |\\n| Embedding 角色 | 主选择器（决定候选池） | 不参与 dataflow pool |\\n| BM25 角色 | 可选的 re-ranker | 唯一排序信号 |\\n\\n### 对齐建议\\nplan_015 实施 dynamic negative mining 时需统一为一种逻辑。建议：\\n1. **排除范围统一**：采用 `build_m1_training_data.py` 的 `full_connected`（dataflow + call graph），因为 call graph 邻居也不应作为 hard negatives\\n2. **选择信号**：dynamic mining 应使用当前 epoch 的 encoder embedding（不是 pretrained），这是 dynamic mining 的核心价值——所以 `DataFlowAwareMiner` 的 embedding→filter→BM25 三步法更合理，但需将排除范围从 1-hop dataflow 扩展到 full_connected\\n3. **具体改动**：修改 `DataFlowAwareMiner._is_reachable()` 使其也排除 call graph 连接，或在 `mine()` 中接受 `full_connected_set` 参数\\n\\n---\\n\\n## 运维经验 (2026-05-14)\\n\\n**Registry 状态机 workaround**：当长链训练（多 run 串行）中途因 cron timeout 或子进程退出导致 registry 状态误标（DONE/failed 或 ANALYZING），而实际训练仍在跑时，不可回退状态。解决方案：创建 `{exp_id}_resumed` / `{exp_id}_continued` 新 entry，步进 PREPARING→QUEUED→ALLOCATED→RUNNING，注册 cron 监控实际 PID。原 entry 保留历史 metrics。\\n\\n**Bash 预读陷阱**：运行中的 bash 脚本已将循环体/数组预读到内存，磁盘上修改脚本文件不影响执行。需要在链外设置独立 tmux watcher 监控链 PID 退出后手动触发后续任务。\\n\\n**BM25 Phase 2 触发机制**：两个 tmux watcher（`bm25_starcoder_watcher`, `bm25_qwen_watcher`）每 5 分钟检查链 PID 存活，退出后自动启动 BM25 脚本。watcher 启动的训练不经过 submit_training_job，需在链完成回调中补注册 cron。\\n\\n---\\n\\n## 关键决策记录\\n\\n**m1_reextract_v2 数据使用决策 (2026-05-14, Director Session 8)**：即使 reextract 将数据从 ~16K 增至 ~44K，不重跑 M2。原因：ARR May 25 DDL 不允许再加 4-5 天重训。处理方式：(1) post-M2 完成后若有 GPU 空档，跑 1-seed pilot (Qwen, embedding, 新数据) 对比当前 M2 baseline；(2) 论文中作为 scalability/data efficiency 讨论点；(3) 全量重训留 camera-ready。\", \"total_chars\": 12963, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "bf3fa037-4b01-4432-a709-958d7d74bfe8",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/memory.md\\\", \\\"content\\\": \\\"# Inference-Time Graph Methods 文献对比\\\\n\\\\n## 对比表\\\\n\\\\n| Method | Paper | Venue | Graph Type | Usage Stage | Inter-proc Data-Flow | Task | Scalability | Key Diff from StructFuse |\\\\n|--------|-------|-------|-----------|-------------|---------------------|------|-------------|--------------------------|\\\\n| **CodexGraph** | Bridging LLMs and Code Repositories via Code Graph Databases | NAACL 2025 (arXiv:2408.03910) | Code graph DB (MODULE/CLASS/FUNCTION nodes; CONTAINS/INHERITS/USES edges) | Inference-time | No. Static analysis for symbol relations only | General repo-level coding (completion, issue resolution) | CrossCodeEval, SWE-bench, EvoCodeBench | Agent queries graph DB at inference; task-agnostic schema but no data-flow semantics |\\\\n| **LocAgent** | Graph-Guided LLM Agents for Code Localization | ACL 2025 (arXiv:2503.09089) | Directed heterogeneous graph (code entities + dependency edges) | Inference-time | No. Dependency edges, not data-flow | Fault localization | 92.7% file-level accuracy; SWE-bench +12% Pass@10 | Agent multi-hop graph reasoning at inference; needs fine-tuned 32B model |\\\\n| **RANGER** | RANGER — Repository-Level Agent for Graph-Enhanced Retrieval | arXiv:2509.25257 (Sep 2025) | Knowledge graph + MCTS traversal | Inference-time | No | Code search, QA, cross-file retrieval, completion | CodeSearchNet, RepoQA, RepoBench, CrossCodeEval | MCTS-guided graph exploration; dual-stage (Cypher + MCTS); higher inference cost due to cross-encoder scoring |\\\\n| **RepoGraph** | Enhancing AI SE with Repository-level Code Graph | ICLR 2025 (arXiv:2410.14684) | Repo-level code graph (class hierarchy, call graph, file structure) | Inference-time | No. Structural relations only | Software engineering / issue resolution | SWE-bench (+32.8% relative); CrossCodeEval | Plug-in module for existing agents; repo-wide navigation; no semantic analysis |\\\\n| **GraphCoder** | Enhancing Repo-Level Code Completion via Code Context Graph | ASE 2024 (arXiv:2406.07003) | Code Context Graph (CFG + CDG + DDG) | Inference-time | Partial. Data dependence graph but **intra-procedural** only | Code completion | Repository-level benchmarks | Coarse-to-fine retrieval with CCG; closest to StructFuse in using data/control flow, but intra-proc and at inference-time |\\\\n| **CodeRAG** | Supportive Code Retrieval on Bigraph for Real-World Code Generation | arXiv:2504.10046 (Apr 2025) | Bigraph (requirement graph + DS-code graph) | Inference-time | No. Dependency + semantic edges | Repo-level code generation | DevEval (+40.90 Pass@1 w/ GPT-4o) | Dual-graph (requirements + code); agentic reasoning; high inference overhead |\\\\n| **ARISE** | ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair | arXiv:2605.03117 (May 2026), Seddik & Fard | Multi-granularity program graph (statement nodes + def-use edges) | Inference-time | Partial. **Intra-procedural** def-use edges + data-flow slicing tool | Fault localization + repair | SWE-bench Lite (300 issues); +17.0 Function Recall@1 | Closest to StructFuse in data-flow usage; but intra-proc only, agent queries at inference |\\\\n| **CodeGRAG** | Bridging NL and PL via Graphical RAG | arXiv:2405.02355 (2024) | Composed syntax graph (AST + DFG + CFG) | Both (GNN training + graph prompt at inference) | Partial. DFG extraction but function-level | Code generation (cross-lingual) | Multiple PLs | Only method with training-time component (GNN soft prompts); but graph also used at inference |\\\\n| **StructFuse** (Ours) | Structure-Grounded Hard Negatives via CodeQL Data-Flow | — | Inter-procedural data-flow graph (CodeQL taint tracking) | **Training-time only** | **Yes. Full inter-procedural** (source→sink across call boundaries) | Code retrieval (contrastive training) | Large-scale repos with CodeQL | Zero inference overhead; graph used offline for negative mining; inter-proc data-flow |\\\\n\\\\n## Discussion 要点\\\\n\\\\n### StructFuse vs Inference-Time Graph Methods: 互补性与差异性\\\\n\\\\n1. **Cost-accuracy tradeoff**: Inference-time methods (CodexGraph, RANGER, RepoGraph) achieve high precision by constructing and querying graphs per request, but incur significant latency (graph construction + traversal + LLM calls). StructFuse amortizes all graph computation to training time—once the encoder is trained with structure-grounded negatives, inference is a single embedding lookup with zero graph overhead. This makes StructFuse suitable for latency-sensitive production retrieval where inference-time graph methods are impractical.\\\\n\\\\n2. **Data-flow depth**: Most inference-time methods use structural graphs (call graphs, class hierarchies, file dependencies). Only GraphCoder and ARISE incorporate data/control flow, but limited to **intra-procedural** scope. StructFuse uniquely leverages **inter-procedural** data-flow via CodeQL's taint tracking, capturing cross-function semantic relationships (e.g., a sanitizer function that transforms data between source and sink across call boundaries). This deeper semantic signal generates harder, more informative negatives.\\\\n\\\\n3. **Complementarity**: StructFuse and inference-time methods are orthogonal and composable. A StructFuse-trained encoder can serve as the embedding backbone for systems like RANGER or CodexGraph, providing better initial retrieval that reduces the graph agent's search space. Conversely, inference-time graph methods can provide reranking on top of StructFuse retrieval for tasks requiring maximum precision.\\\\n\\\\n4. **Scalability model**: Inference-time methods scale linearly with query volume (each query triggers graph operations). StructFuse's cost is front-loaded: CodeQL analysis runs once per repository update, and the resulting negatives improve the encoder permanently. For high-QPS code search services, this one-time investment yields compounding returns.\\\\n\\\\n5. **Task generality vs specialization**: Inference-time graph agents (CodexGraph, RepoGraph) are task-agnostic but require powerful LLMs as backends. StructFuse produces a specialized retrieval encoder that excels at the code search task without LLM inference, making it deployable as a lightweight, efficient first-stage retriever in multi-stage pipelines.\\\\n\\\\n## Related Work 段落草稿 (~200 words)\\\\n\\\\n**Graph-Based Methods for Code Understanding.**\\\\nRecent work has explored leveraging code graphs to enhance LLM-based software engineering. Inference-time approaches construct and query graphs during each interaction: CodexGraph (Liu et al., NAACL 2025) builds a code graph database that LLM agents query via structured interfaces; RepoGraph (Ouyang et al., ICLR 2025) provides repository-level navigation as a plug-in module for SE agents; LocAgent (ACL 2025) and RANGER (Shah et al., 2025) employ graph-guided multi-hop reasoning and MCTS-based traversal for code localization and retrieval, respectively. GraphCoder (ASE 2024) incorporates intra-procedural control-flow and data-dependence graphs for code completion retrieval, while ARISE (Seddik & Fard, 2026) extends this with statement-level def-use edges for fault localization. CodeGRAG (2024) bridges training and inference by using GNN-encoded graph prompts.\\\\n\\\\nThese methods achieve strong results but impose substantial inference-time costs—graph construction, traversal, and often multiple LLM calls per query. Moreover, their data-flow analysis remains intra-procedural. StructFuse takes a fundamentally different approach: we leverage CodeQL's inter-procedural taint tracking to generate structure-grounded hard negatives at **training time**, producing an encoder that captures cross-function data-flow semantics without any graph overhead at inference. This positions StructFuse as complementary to inference-time graph methods—it can serve as an efficient first-stage retriever whose embeddings already encode deep structural relationships that other methods must compute on-the-fly.\\\\n\\\\n---\\\\n\\\\n## 参考文献（全部已验证 2026-05-14）\\\\n\\\\n- CodexGraph: arXiv:2408.03910, Liu et al., NAACL 2025\\\\n- LocAgent: arXiv:2503.09089, Chen et al., ACL 2025\\\\n- RANGER: arXiv:2509.25257, Shah et al., 2025 ✅ verified\\\\n- RepoGraph: arXiv:2410.14684, Ouyang et al., ICLR 2025\\\\n- GraphCoder: arXiv:2406.07003, Liu et al., ASE 2024\\\\n- CodeRAG: arXiv:2504.10046, 2025\\\\n- ARISE: arXiv:2605.03117, Seddik & Fard, 2026 ✅ verified (full title: \\\\\\\"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair\\\\\\\")\\\\n- CodeGRAG: arXiv:2405.02355, 2024\\\\n\\\\n---\\\\n\\\\n## Checkpoint Criterion 与 K 分析 (2026-05-15)\\\\n\\\\n**Checkpoint 选择 criterion 分歧率**：4 个完成的 full M2 runs 中，2/4 (50%) val_loss 与 R@1 选中不同 checkpoint。\\\\n\\\\n**分歧 pattern**：\\\\n- Qwen s43: val_loss→step 500, R@1→step 1500, R@1 差 +1.97pp\\\\n- StarCoder s42: val_loss→step 1000, R@1→step 2500, R@1 差 +0.64pp\\\\n- Mean delta: +0.65pp (R@1 criterion 优于 val_loss criterion)\\\\n- StarCoder 步差更大（1500 步 vs 1000 步），与其 pretrained margin 更大的特性一致\\\\n\\\\n**论文写作决策**：主表报 best_by_R@1（target metric aligned），ablation 表展示两种 criterion 对比（D036 已决策 R@1 为 primary）。\\\\n\\\\n**K=7 无 ablation**：所有正式实验固定 K=7。合理性来源：(1) batch_size=8 对齐（1 positive + 7 negatives = 8）(2) DPR 等文献惯例 (3) hard_negative_ratio=0.5 平衡设计。K 敏感性列为 limitation/future work。\\\\n\\\\n---\\\\n\\\\n## BM25 Negative Mining 策略洞察 (2026-05-14, updated)\\\\n\\\\n**两层重叠率数据（注意区分）**：\\\\n- **k=50 全候选重叠**（mining worker 报告）：BM25 vs embedding 87.1%, vs random 76.2%, vs dataflow 71.8%\\\\n- **top-7 Jaccard**（训练实际用的 num_negatives=7，分层分析）：差异远大于全候选\\\\n\\\\n**分层 top-7 Jaccard 重叠率**（seed 42, 2920 matched queries / 12290 total）：\\\\n| 层级 | BM25 vs Embedding | BM25 vs Random | BM25 vs Dataflow |\\\\n|------|-------------------|----------------|------------------|\\\\n| Small (<50 files, 39 repos) | 0.668 | 0.411 | 0.667 |\\\\n| Medium (50-200, 29 repos) | 0.380 | 0.067 | 0.363 |\\\\n| Large (200+, 15 repos) | 0.297 | 0.007 | 0.405 |\\\\n\\\\n**核心修正**：之前基于 87% 预测\\\\\\\"Phase 2 中 BM25 R@1 很可能接近 embedding\\\\\\\"——这个预测可能不成立。在中大 repo（训练数据主体）上 top-7 Jaccard 仅 30-38%，BM25 和 embedding 选出的训练 negatives 大部分不同。Phase 2 训练结果将真正区分两种策略。\\\\n\\\\n**意外发现**：BM25 vs dataflow 在大 repo 上重叠率（0.405）高于 vs embedding（0.297）。词汇相似性信号与数据流依赖有部分对齐，而纯 embedding 距离选择了不同维度的 hard negatives。\\\\n\\\\n---\\\\n\\\\n## hard_negative_mining.py vs build_m1_training_data.py 实现差异 [2026-05-15]\\\\n\\\\n**发现者**：Reviewer\\\\n**影响**：当前 M2 不受影响（用 pre-mined 数据），plan_015（dynamic negative mining）实施前必须对齐\\\\n\\\\n**差异**：\\\\n\\\\n### hard_negative_mining.py `DataFlowAwareMiner`（training/hard_negative_mining.py）\\\\n三步法：\\\\n1. **Embedding top-K**：调用 `EmbeddingDistanceMiner.mine()` 获取 top-50 cosine similarity 最高的 candidates（从所有 non-positive candidates 中）\\\\n2. **Dataflow filter**：过滤掉 `_is_reachable(query, fid)` 为 True 的文件——仅检查 `dataflow_graph[src]` 中的直接条目（1-hop 可达性）\\\\n3. **BM25 re-rank**：如果 `bm25_index` 可用，对剩余 disconnected candidates 按 BM25 分数降序重排\\\\n4. **Fallback**：如果 disconnected 不足 `num_negatives`，用 random padding 补足\\\\n\\\\n### build_m1_training_data.py `build_candidate_pools()`（scripts/build_m1_training_data.py）\\\\n两步法：\\\\n1. **Dataflow filter**：从 `non_pos_files` 中排除 `full_connected_set`（= `positive_files ∪ cg_connected`，即 dataflow 直连 + call graph 邻居——比 `DataFlowAwareMiner` 排除范围更广）\\\\n2. **BM25 sort**：对 disconnected 文件按 BM25 分数降序排序，取 top-K（pool_size=50）\\\\n3. **无 embedding 步骤**：dataflow pool 完全不使用 embedding 信号\\\\n\\\\n额外注意：当 `--model-path` 未提供时，`emb_scores = bm25`（line 317-318），此时 embedding pool 也退化为 BM25 排序，仅在是否排除 `full_connected` 上与 dataflow pool 不同。\\\\n\\\\n### 差异总结\\\\n\\\\n| 维度 | hard_negative_mining.py | build_m1_training_data.py |\\\\n|------|------------------------|--------------------------|\\\\n| Candidate 初筛 | Embedding cosine top-50 | 全部 non-positive（无初筛） |\\\\n| Dataflow 排除范围 | `dataflow_graph[src]` 直接条目 | `positive_files ∪ cg_connected`（更广） |\\\\n| 排序信号 | Embedding 为主 → BM25 re-rank | 纯 BM25 排序 |\\\\n| Embedding 角色 | 主选择器（决定候选池） | 不参与 dataflow pool |\\\\n| BM25 角色 | 可选的 re-ranker | 唯一排序信号 |\\\\n\\\\n### 对齐建议\\\\nplan_015 实施 dynamic negative mining 时需统一为一种逻辑。建议：\\\\n1. **排除范围统一**：采用 `build_m1_training_data.py` 的 `full_connected`（dataflow + call graph），因为 call graph 邻居也不应作为 hard negatives\\\\n2. **选择信号**：dynamic mining 应使用当前 epoch 的 encoder embedding（不是 pretrained），这是 dynamic mining 的核心价值——所以 `DataFlowAwareMiner` 的 embedding→filter→BM25 三步法更合理，但需将排除范围从 1-hop dataflow 扩展到 full_connected\\\\n3. **具体改动**：修改 `DataFlowAwareMiner._is_reachable()` 使其也排除 call graph 连接，或在 `mine()` 中接受 `full_connected_set` 参数\\\\n\\\\n---\\\\n\\\\n## 运维经验 (2026-05-14)\\\\n\\\\n**Registry 状态机 workaround**：当长链训练（多 run 串行）中途因 cron timeout 或子进程退出导致 registry 状态误标（DONE/failed 或 ANALYZING），而实际训练仍在跑时，不可回退状态。解决方案：创建 `{exp_id}_resumed` / `{exp_id}_continued` 新 entry，步进 PREPARING→QUEUED→ALLOCATED→RUNNING，注册 cron 监控实际 PID。原 entry 保留历史 metrics。\\\\n\\\\n**Bash 预读陷阱**：运行中的 bash 脚本已将循环体/数组预读到内存，磁盘上修改脚本文件不影响执行。需要在链外设置独立 tmux watcher 监控链 PID 退出后手动触发后续任务。\\\\n\\\\n**BM25 Phase 2 触发机制**：两个 tmux watcher（`bm25_starcoder_watcher`, `bm25_qwen_watcher`）每 5 分钟检查链 PID 存活，退出后自动启动 BM25 脚本。watcher 启动的训练不经过 submit_training_job，需在链完成回调中补注册 cron。\\\\n\\\\n---\\\\n\\\\n## 关键决策记录\\\\n\\\\n**m1_reextract_v2 数据使用决策 (2026-05-14, Director Session 8)**：即使 reextract 将数据从 ~16K 增至 ~44K，不重跑 M2。原因：ARR May 25 DDL 不允许再加 4-5 天重训。处理方式：(1) post-M2 完成后若有 GPU 空档，跑 1-seed pilot (Qwen, embedding, 新数据) 对比当前 M2 baseline；(2) 论文中作为 scalability/data efficiency 讨论点；(3) 全量重训留 camera-ready。\\\", \\\"total_chars\\\": 12963, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/memory.md\", \"content\": \"# Inference-Time Graph Methods 文献对比\\n\\n## 对比表\\n\\n| Method | Paper | Venue | Graph Type | Usage Stage | Inter-proc Data-Flow | Task | Scalability | Key Diff from StructFuse |\\n|--------|-------|-------|-----------|-------------|---------------------|------|-------------|--------------------------|\\n| **CodexGraph** | Bridging LLMs and Code Repositories via Code Graph Databases | NAACL 2025 (arXiv:2408.03910) | Code graph DB (MODULE/CLASS/FUNCTION nodes; CONTAINS/INHERITS/USES edges) | Inference-time | No. Static analysis for symbol relations only | General repo-level coding (completion, issue resolution) | CrossCodeEval, SWE-bench, EvoCodeBench | Agent queries graph DB at inference; task-agnostic schema but no data-flow semantics |\\n| **LocAgent** | Graph-Guided LLM Agents for Code Localization | ACL 2025 (arXiv:2503.09089) | Directed heterogeneous graph (code entities + dependency edges) | Inference-time | No. Dependency edges, not data-flow | Fault localization | 92.7% file-level accuracy; SWE-bench +12% Pass@10 | Agent multi-hop graph reasoning at inference; needs fine-tuned 32B model |\\n| **RANGER** | RANGER — Repository-Level Agent for Graph-Enhanced Retrieval | arXiv:2509.25257 (Sep 2025) | Knowledge graph + MCTS traversal | Inference-time | No | Code search, QA, cross-file retrieval, completion | CodeSearchNet, RepoQA, RepoBench, CrossCodeEval | MCTS-guided graph exploration; dual-stage (Cypher + MCTS); higher inference cost due to cross-encoder scoring |\\n| **RepoGraph** | Enhancing AI SE with Repository-level Code Graph | ICLR 2025 (arXiv:2410.14684) | Repo-level code graph (class hierarchy, call graph, file structure) | Inference-time | No. Structural relations only | Software engineering / issue resolution | SWE-bench (+32.8% relative); CrossCodeEval | Plug-in module for existing agents; repo-wide navigation; no semantic analysis |\\n| **GraphCoder** | Enhancing Repo-Level Code Completion via Code Context Graph | ASE 2024 (arXiv:2406.07003) | Code Context Graph (CFG + CDG + DDG) | Inference-time | Partial. Data dependence graph but **intra-procedural** only | Code completion | Repository-level benchmarks | Coarse-to-fine retrieval with CCG; closest to StructFuse in using data/control flow, but intra-proc and at inference-time |\\n| **CodeRAG** | Supportive Code Retrieval on Bigraph for Real-World Code Generation | arXiv:2504.10046 (Apr 2025) | Bigraph (requirement graph + DS-code graph) | Inference-time | No. Dependency + semantic edges | Repo-level code generation | DevEval (+40.90 Pass@1 w/ GPT-4o) | Dual-graph (requirements + code); agentic reasoning; high inference overhead |\\n| **ARISE** | ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair | arXiv:2605.03117 (May 2026), Seddik & Fard | Multi-granularity program graph (statement nodes + def-use edges) | Inference-time | Partial. **Intra-procedural** def-use edges + data-flow slicing tool | Fault localization + repair | SWE-bench Lite (300 issues); +17.0 Function Recall@1 | Closest to StructFuse in data-flow usage; but intra-proc only, agent queries at inference |\\n| **CodeGRAG** | Bridging NL and PL via Graphical RAG | arXiv:2405.02355 (2024) | Composed syntax graph (AST + DFG + CFG) | Both (GNN training + graph prompt at inference) | Partial. DFG extraction but function-level | Code generation (cross-lingual) | Multiple PLs | Only method with training-time component (GNN soft prompts); but graph also used at inference |\\n| **StructFuse** (Ours) | Structure-Grounded Hard Negatives via CodeQL Data-Flow | — | Inter-procedural data-flow graph (CodeQL taint tracking) | **Training-time only** | **Yes. Full inter-procedural** (source→sink across call boundaries) | Code retrieval (contrastive training) | Large-scale repos with CodeQL | Zero inference overhead; graph used offline for negative mining; inter-proc data-flow |\\n\\n## Discussion 要点\\n\\n### StructFuse vs Inference-Time Graph Methods: 互补性与差异性\\n\\n1. **Cost-accuracy tradeoff**: Inference-time methods (CodexGraph, RANGER, RepoGraph) achieve high precision by constructing and querying graphs per request, but incur significant latency (graph construction + traversal + LLM calls). StructFuse amortizes all graph computation to training time—once the encoder is trained with structure-grounded negatives, inference is a single embedding lookup with zero graph overhead. This makes StructFuse suitable for latency-sensitive production retrieval where inference-time graph methods are impractical.\\n\\n2. **Data-flow depth**: Most inference-time methods use structural graphs (call graphs, class hierarchies, file dependencies). Only GraphCoder and ARISE incorporate data/control flow, but limited to **intra-procedural** scope. StructFuse uniquely leverages **inter-procedural** data-flow via CodeQL's taint tracking, capturing cross-function semantic relationships (e.g., a sanitizer function that transforms data between source and sink across call boundaries). This deeper semantic signal generates harder, more informative negatives.\\n\\n3. **Complementarity**: StructFuse and inference-time methods are orthogonal and composable. A StructFuse-trained encoder can serve as the embedding backbone for systems like RANGER or CodexGraph, providing better initial retrieval that reduces the graph agent's search space. Conversely, inference-time graph methods can provide reranking on top of StructFuse retrieval for tasks requiring maximum precision.\\n\\n4. **Scalability model**: Inference-time methods scale linearly with query volume (each query triggers graph operations). StructFuse's cost is front-loaded: CodeQL analysis runs once per repository update, and the resulting negatives improve the encoder permanently. For high-QPS code search services, this one-time investment yields compounding returns.\\n\\n5. **Task generality vs specialization**: Inference-time graph agents (CodexGraph, RepoGraph) are task-agnostic but require powerful LLMs as backends. StructFuse produces a specialized retrieval encoder that excels at the code search task without LLM inference, making it deployable as a lightweight, efficient first-stage retriever in multi-stage pipelines.\\n\\n## Related Work 段落草稿 (~200 words)\\n\\n**Graph-Based Methods for Code Understanding.**\\nRecent work has explored leveraging code graphs to enhance LLM-based software engineering. Inference-time approaches construct and query graphs during each interaction: CodexGraph (Liu et al., NAACL 2025) builds a code graph database that LLM agents query via structured interfaces; RepoGraph (Ouyang et al., ICLR 2025) provides repository-level navigation as a plug-in module for SE agents; LocAgent (ACL 2025) and RANGER (Shah et al., 2025) employ graph-guided multi-hop reasoning and MCTS-based traversal for code localization and retrieval, respectively. GraphCoder (ASE 2024) incorporates intra-procedural control-flow and data-dependence graphs for code completion retrieval, while ARISE (Seddik & Fard, 2026) extends this with statement-level def-use edges for fault localization. CodeGRAG (2024) bridges training and inference by using GNN-encoded graph prompts.\\n\\nThese methods achieve strong results but impose substantial inference-time costs—graph construction, traversal, and often multiple LLM calls per query. Moreover, their data-flow analysis remains intra-procedural. StructFuse takes a fundamentally different approach: we leverage CodeQL's inter-procedural taint tracking to generate structure-grounded hard negatives at **training time**, producing an encoder that captures cross-function data-flow semantics without any graph overhead at inference. This positions StructFuse as complementary to inference-time graph methods—it can serve as an efficient first-stage retriever whose embeddings already encode deep structural relationships that other methods must compute on-the-fly.\\n\\n---\\n\\n## 参考文献（全部已验证 2026-05-14）\\n\\n- CodexGraph: arXiv:2408.03910, Liu et al., NAACL 2025\\n- LocAgent: arXiv:2503.09089, Chen et al., ACL 2025\\n- RANGER: arXiv:2509.25257, Shah et al., 2025 ✅ verified\\n- RepoGraph: arXiv:2410.14684, Ouyang et al., ICLR 2025\\n- GraphCoder: arXiv:2406.07003, Liu et al., ASE 2024\\n- CodeRAG: arXiv:2504.10046, 2025\\n- ARISE: arXiv:2605.03117, Seddik & Fard, 2026 ✅ verified (full title: \\\"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair\\\")\\n- CodeGRAG: arXiv:2405.02355, 2024\\n\\n---\\n\\n## Checkpoint Criterion 与 K 分析 (2026-05-15)\\n\\n**Checkpoint 选择 criterion 分歧率**：4 个完成的 full M2 runs 中，2/4 (50%) val_loss 与 R@1 选中不同 checkpoint。\\n\\n**分歧 pattern**：\\n- Qwen s43: val_loss→step 500, R@1→step 1500, R@1 差 +1.97pp\\n- StarCoder s42: val_loss→step 1000, R@1→step 2500, R@1 差 +0.64pp\\n- Mean delta: +0.65pp (R@1 criterion 优于 val_loss criterion)\\n- StarCoder 步差更大（1500 步 vs 1000 步），与其 pretrained margin 更大的特性一致\\n\\n**论文写作决策**：主表报 best_by_R@1（target metric aligned），ablation 表展示两种 criterion 对比（D036 已决策 R@1 为 primary）。\\n\\n**K=7 无 ablation**：所有正式实验固定 K=7。合理性来源：(1) batch_size=8 对齐（1 positive + 7 negatives = 8）(2) DPR 等文献惯例 (3) hard_negative_ratio=0.5 平衡设计。K 敏感性列为 limitation/future work。\\n\\n---\\n\\n## BM25 Negative Mining 策略洞察 (2026-05-14, updated)\\n\\n**两层重叠率数据（注意区分）**：\\n- **k=50 全候选重叠**（mining worker 报告）：BM25 vs embedding 87.1%, vs random 76.2%, vs dataflow 71.8%\\n- **top-7 Jaccard**（训练实际用的 num_negatives=7，分层分析）：差异远大于全候选\\n\\n**分层 top-7 Jaccard 重叠率**（seed 42, 2920 matched queries / 12290 total）：\\n| 层级 | BM25 vs Embedding | BM25 vs Random | BM25 vs Dataflow |\\n|------|-------------------|----------------|------------------|\\n| Small (<50 files, 39 repos) | 0.668 | 0.411 | 0.667 |\\n| Medium (50-200, 29 repos) | 0.380 | 0.067 | 0.363 |\\n| Large (200+, 15 repos) | 0.297 | 0.007 | 0.405 |\\n\\n**核心修正**：之前基于 87% 预测\\\"Phase 2 中 BM25 R@1 很可能接近 embedding\\\"——这个预测可能不成立。在中大 repo（训练数据主体）上 top-7 Jaccard 仅 30-38%，BM25 和 embedding 选出的训练 negatives 大部分不同。Phase 2 训练结果将真正区分两种策略。\\n\\n**意外发现**：BM25 vs dataflow 在大 repo 上重叠率（0.405）高于 vs embedding（0.297）。词汇相似性信号与数据流依赖有部分对齐，而纯 embedding 距离选择了不同维度的 hard negatives。\\n\\n---\\n\\n## hard_negative_mining.py vs build_m1_training_data.py 实现差异 [2026-05-15]\\n\\n**发现者**：Reviewer\\n**影响**：当前 M2 不受影响（用 pre-mined 数据），plan_015（dynamic negative mining）实施前必须对齐\\n\\n**差异**：\\n\\n### hard_negative_mining.py `DataFlowAwareMiner`（training/hard_negative_mining.py）\\n三步法：\\n1. **Embedding top-K**：调用 `EmbeddingDistanceMiner.mine()` 获取 top-50 cosine similarity 最高的 candidates（从所有 non-positive candidates 中）\\n2. **Dataflow filter**：过滤掉 `_is_reachable(query, fid)` 为 True 的文件——仅检查 `dataflow_graph[src]` 中的直接条目（1-hop 可达性）\\n3. **BM25 re-rank**：如果 `bm25_index` 可用，对剩余 disconnected candidates 按 BM25 分数降序重排\\n4. **Fallback**：如果 disconnected 不足 `num_negatives`，用 random padding 补足\\n\\n### build_m1_training_data.py `build_candidate_pools()`（scripts/build_m1_training_data.py）\\n两步法：\\n1. **Dataflow filter**：从 `non_pos_files` 中排除 `full_connected_set`（= `positive_files ∪ cg_connected`，即 dataflow 直连 + call graph 邻居——比 `DataFlowAwareMiner` 排除范围更广）\\n2. **BM25 sort**：对 disconnected 文件按 BM25 分数降序排序，取 top-K（pool_size=50）\\n3. **无 embedding 步骤**：dataflow pool 完全不使用 embedding 信号\\n\\n额外注意：当 `--model-path` 未提供时，`emb_scores = bm25`（line 317-318），此时 embedding pool 也退化为 BM25 排序，仅在是否排除 `full_connected` 上与 dataflow pool 不同。\\n\\n### 差异总结\\n\\n| 维度 | hard_negative_mining.py | build_m1_training_data.py |\\n|------|------------------------|--------------------------|\\n| Candidate 初筛 | Embedding cosine top-50 | 全部 non-positive（无初筛） |\\n| Dataflow 排除范围 | `dataflow_graph[src]` 直接条目 | `positive_files ∪ cg_connected`（更广） |\\n| 排序信号 | Embedding 为主 → BM25 re-rank | 纯 BM25 排序 |\\n| Embedding 角色 | 主选择器（决定候选池） | 不参与 dataflow pool |\\n| BM25 角色 | 可选的 re-ranker | 唯一排序信号 |\\n\\n### 对齐建议\\nplan_015 实施 dynamic negative mining 时需统一为一种逻辑。建议：\\n1. **排除范围统一**：采用 `build_m1_training_data.py` 的 `full_connected`（dataflow + call graph），因为 call graph 邻居也不应作为 hard negatives\\n2. **选择信号**：dynamic mining 应使用当前 epoch 的 encoder embedding（不是 pretrained），这是 dynamic mining 的核心价值——所以 `DataFlowAwareMiner` 的 embedding→filter→BM25 三步法更合理，但需将排除范围从 1-hop dataflow 扩展到 full_connected\\n3. **具体改动**：修改 `DataFlowAwareMiner._is_reachable()` 使其也排除 call graph 连接，或在 `mine()` 中接受 `full_connected_set` 参数\\n\\n---\\n\\n## 运维经验 (2026-05-14)\\n\\n**Registry 状态机 workaround**：当长链训练（多 run 串行）中途因 cron timeout 或子进程退出导致 registry 状态误标（DONE/failed 或 ANALYZING），而实际训练仍在跑时，不可回退状态。解决方案：创建 `{exp_id}_resumed` / `{exp_id}_continued` 新 entry，步进 PREPARING→QUEUED→ALLOCATED→RUNNING，注册 cron 监控实际 PID。原 entry 保留历史 metrics。\\n\\n**Bash 预读陷阱**：运行中的 bash 脚本已将循环体/数组预读到内存，磁盘上修改脚本文件不影响执行。需要在链外设置独立 tmux watcher 监控链 PID 退出后手动触发后续任务。\\n\\n**BM25 Phase 2 触发机制**：两个 tmux watcher（`bm25_starcoder_watcher`, `bm25_qwen_watcher`）每 5 分钟检查链 PID 存活，退出后自动启动 BM25 脚本。watcher 启动的训练不经过 submit_training_job，需在链完成回调中补注册 cron。\\n\\n---\\n\\n## 关键决策记录\\n\\n**m1_reextract_v2 数据使用决策 (2026-05-14, Director Session 8)**：即使 reextract 将数据从 ~16K 增至 ~44K，不重跑 M2。原因：ARR May 25 DDL 不允许再加 4-5 天重训。处理方式：(1) post-M2 完成后若有 GPU 空档，跑 1-seed pilot (Qwen, embedding, 新数据) 对比当前 M2 baseline；(2) 论文中作为 scalability/data efficiency 讨论点；(3) 全量重训留 camera-ready。\", \"total_chars\": 12963, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 109_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full memory.md content. I need to append the gap analysis report to it. Let me compose the report and then use save_project_file to write the full content (existing + new appendix).

Let me organize the report:

**Current citations by category (from literature_map.yaml):**

| Category | Count | Papers |
|----------|-------|--------|
| code_retrieval_bug_fixing | 8 | SWE-bench, SWE-agent, AutoCodeRover, Agentless, SWE-smith, RepoBench, SweRank, SWE-Fixer |


| hard_negative_mining | 6 | DPR, ANCE, SimCLR, SBERT, CL-DRD, CoCoHaNeRe |
| contrastive_code_learning | 3 | ContraCode, CodeRetriever, Ding et al. |
| program_analysis_for_ml | 6 | CodeQL, code2vec, code2seq, FA-AST, GraphCodeBERT, ARISE |
| code_embeddings_search | 9 | CodeSearchNet, CodeBERT, UniXcoder, StarCoder, Code Llama |

Generating markdown table... I've identified a few more gap areas to fill out the literature map—adding papers on contrastive learning, hard negative mining, code search benchmarks, repository-level understanding, program analysis, and CodeEval brings the total to around 46-48 papers depending on how I count them. Now I'm ready to write up the report.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "e65babf7-50e3-4ee3-bc8d-356954e5ba93",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014vNhcEEcd7rC9YXuByWDuf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5474,
      "cache_read_input_tokens": 42553,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5474
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

_source line 110_

Now I'll append the gap analysis to memory.md.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "3e37f8da-fe01-4c85-bbc3-0ad5080b9a11",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014vNhcEEcd7rC9YXuByWDuf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5474,
      "cache_read_input_tokens": 42553,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5474
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

_source line 111_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file · `toolu_01TrRpzEAh61iXd2GXXWfvrr`</summary>

```json
{
  "project": "structfuse-context",
  "file": "memory.md",
  "content": "# Inference-Time Graph Methods 文献对比\n\n## 对比表\n\n| Method | Paper | Venue | Graph Type | Usage Stage | Inter-proc Data-Flow | Task | Scalability | Key Diff from StructFuse |\n|--------|-------|-------|-----------|-------------|---------------------|------|-------------|--------------------------|\n| **CodexGraph** | Bridging LLMs and Code Repositories via Code Graph Databases | NAACL 2025 (arXiv:2408.03910) | Code graph DB (MODULE/CLASS/FUNCTION nodes; CONTAINS/INHERITS/USES edges) | Inference-time | No. Static analysis for symbol relations only | General repo-level coding (completion, issue resolution) | CrossCodeEval, SWE-bench, EvoCodeBench | Agent queries graph DB at inference; task-agnostic schema but no data-flow semantics |\n| **LocAgent** | Graph-Guided LLM Agents for Code Localization | ACL 2025 (arXiv:2503.09089) | Directed heterogeneous graph (code entities + dependency edges) | Inference-time | No. Dependency edges, not data-flow | Fault localization | 92.7% file-level accuracy; SWE-bench +12% Pass@10 | Agent multi-hop graph reasoning at inference; needs fine-tuned 32B model |\n| **RANGER** | RANGER — Repository-Level Agent for Graph-Enhanced Retrieval | arXiv:2509.25257 (Sep 2025) | Knowledge graph + MCTS traversal | Inference-time | No | Code search, QA, cross-file retrieval, completion | CodeSearchNet, RepoQA, RepoBench, CrossCodeEval | MCTS-guided graph exploration; dual-stage (Cypher + MCTS); higher inference cost due to cross-encoder scoring |\n| **RepoGraph** | Enhancing AI SE with Repository-level Code Graph | ICLR 2025 (arXiv:2410.14684) | Repo-level code graph (class hierarchy, call graph, file structure) | Inference-time | No. Structural relations only | Software engineering / issue resolution | SWE-bench (+32.8% relative); CrossCodeEval | Plug-in module for existing agents; repo-wide navigation; no semantic analysis |\n| **GraphCoder** | Enhancing Repo-Level Code Completion via Code Context Graph | ASE 2024 (arXiv:2406.07003) | Code Context Graph (CFG + CDG + DDG) | Inference-time | Partial. Data dependence graph but **intra-procedural** only | Code completion | Repository-level benchmarks | Coarse-to-fine retrieval with CCG; closest to StructFuse in using data/control flow, but intra-proc and at inference-time |\n| **CodeRAG** | Supportive Code Retrieval on Bigraph for Real-World Code Generation | arXiv:2504.10046 (Apr 2025) | Bigraph (requirement graph + DS-code graph) | Inference-time | No. Dependency + semantic edges | Repo-level code generation | DevEval (+40.90 Pass@1 w/ GPT-4o) | Dual-graph (requirements + code); agentic reasoning; high inference overhead |\n| **ARISE** | ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair | arXiv:2605.03117 (May 2026), Seddik & Fard | Multi-granularity program graph (statement nodes + def-use edges) | Inference-time | Partial. **Intra-procedural** def-use edges + data-flow slicing tool | Fault localization + repair | SWE-bench Lite (300 issues); +17.0 Function Recall@1 | Closest to StructFuse in data-flow usage; but intra-proc only, agent queries at inference |\n| **CodeGRAG** | Bridging NL and PL via Graphical RAG | arXiv:2405.02355 (2024) | Composed syntax graph (AST + DFG + CFG) | Both (GNN training + graph prompt at inference) | Partial. DFG extraction but function-level | Code generation (cross-lingual) | Multiple PLs | Only method with training-time component (GNN soft prompts); but graph also used at inference |\n| **StructFuse** (Ours) | Structure-Grounded Hard Negatives via CodeQL Data-Flow | — | Inter-procedural data-flow graph (CodeQL taint tracking) | **Training-time only** | **Yes. Full inter-procedural** (source→sink across call boundaries) | Code retrieval (contrastive training) | Large-scale repos with CodeQL | Zero inference overhead; graph used offline for negative mining; inter-proc data-flow |\n\n## Discussion 要点\n\n### StructFuse vs Inference-Time Graph Methods: 互补性与差异性\n\n1. **Cost-accuracy tradeoff**: Inference-time methods (CodexGraph, RANGER, RepoGraph) achieve high precision by constructing and querying graphs per request, but incur significant latency (graph construction + traversal + LLM calls). StructFuse amortizes all graph computation to training time—once the encoder is trained with structure-grounded negatives, inference is a single embedding lookup with zero graph overhead. This makes StructFuse suitable for latency-sensitive production retrieval where inference-time graph methods are impractical.\n\n2. **Data-flow depth**: Most inference-time methods use structural graphs (call graphs, class hierarchies, file dependencies). Only GraphCoder and ARISE incorporate data/control flow, but limited to **intra-procedural** scope. StructFuse uniquely leverages **inter-procedural** data-flow via CodeQL's taint tracking, capturing cross-function semantic relationships (e.g., a sanitizer function that transforms data between source and sink across call boundaries). This deeper semantic signal generates harder, more informative negatives.\n\n3. **Complementarity**: StructFuse and inference-time methods are orthogonal and composable. A StructFuse-trained encoder can serve as the embedding backbone for systems like RANGER or CodexGraph, providing better initial retrieval that reduces the graph agent's search space. Conversely, inference-time graph methods can provide reranking on top of StructFuse retrieval for tasks requiring maximum precision.\n\n4. **Scalability model**: Inference-time methods scale linearly with query volume (each query triggers graph operations). StructFuse's cost is front-loaded: CodeQL analysis runs once per repository update, and the resulting negatives improve the encoder permanently. For high-QPS code search services, this one-time investment yields compounding returns.\n\n5. **Task generality vs specialization**: Inference-time graph agents (CodexGraph, RepoGraph) are task-agnostic but require powerful LLMs as backends. StructFuse produces a specialized retrieval encoder that excels at the code search task without LLM inference, making it deployable as a lightweight, efficient first-stage retriever in multi-stage pipelines.\n\n## Related Work 段落草稿 (~200 words)\n\n**Graph-Based Methods for Code Understanding.**\nRecent work has explored leveraging code graphs to enhance LLM-based software engineering. Inference-time approaches construct and query graphs during each interaction: CodexGraph (Liu et al., NAACL 2025) builds a code graph database that LLM agents query via structured interfaces; RepoGraph (Ouyang et al., ICLR 2025) provides repository-level navigation as a plug-in module for SE agents; LocAgent (ACL 2025) and RANGER (Shah et al., 2025) employ graph-guided multi-hop reasoning and MCTS-based traversal for code localization and retrieval, respectively. GraphCoder (ASE 2024) incorporates intra-procedural control-flow and data-dependence graphs for code completion retrieval, while ARISE (Seddik & Fard, 2026) extends this with statement-level def-use edges for fault localization. CodeGRAG (2024) bridges training and inference by using GNN-encoded graph prompts.\n\nThese methods achieve strong results but impose substantial inference-time costs—graph construction, traversal, and often multiple LLM calls per query. Moreover, their data-flow analysis remains intra-procedural. StructFuse takes a fundamentally different approach: we leverage CodeQL's inter-procedural taint tracking to generate structure-grounded hard negatives at **training time**, producing an encoder that captures cross-function data-flow semantics without any graph overhead at inference. This positions StructFuse as complementary to inference-time graph methods—it can serve as an efficient first-stage retriever whose embeddings already encode deep structural relationships that other methods must compute on-the-fly.\n\n---\n\n## 参考文献（全部已验证 2026-05-14）\n\n- CodexGraph: arXiv:2408.03910, Liu et al., NAACL 2025\n- LocAgent: arXiv:2503.09089, Chen et al., ACL 2025\n- RANGER: arXiv:2509.25257, Shah et al., 2025 ✅ verified\n- RepoGraph: arXiv:2410.14684, Ouyang et al., ICLR 2025\n- GraphCoder: arXiv:2406.07003, Liu et al., ASE 2024\n- CodeRAG: arXiv:2504.10046, 2025\n- ARISE: arXiv:2605.03117, Seddik & Fard, 2026 ✅ verified (full title: \"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair\")\n- CodeGRAG: arXiv:2405.02355, 2024\n\n---\n\n## Checkpoint Criterion 与 K 分析 (2026-05-15)\n\n**Checkpoint 选择 criterion 分歧率**：4 个完成的 full M2 runs 中，2/4 (50%) val_loss 与 R@1 选中不同 checkpoint。\n\n**分歧 pattern**：\n- Qwen s43: val_loss→step 500, R@1→step 1500, R@1 差 +1.97pp\n- StarCoder s42: val_loss→step 1000, R@1→step 2500, R@1 差 +0.64pp\n- Mean delta: +0.65pp (R@1 criterion 优于 val_loss criterion)\n- StarCoder 步差更大（1500 步 vs 1000 步），与其 pretrained margin 更大的特性一致\n\n**论文写作决策**：主表报 best_by_R@1（target metric aligned），ablation 表展示两种 criterion 对比（D036 已决策 R@1 为 primary）。\n\n**K=7 无 ablation**：所有正式实验固定 K=7。合理性来源：(1) batch_size=8 对齐（1 positive + 7 negatives = 8）(2) DPR 等文献惯例 (3) hard_negative_ratio=0.5 平衡设计。K 敏感性列为 limitation/future work。\n\n---\n\n## BM25 Negative Mining 策略洞察 (2026-05-14, updated)\n\n**两层重叠率数据（注意区分）**：\n- **k=50 全候选重叠**（mining worker 报告）：BM25 vs embedding 87.1%, vs random 76.2%, vs dataflow 71.8%\n- **top-7 Jaccard**（训练实际用的 num_negatives=7，分层分析）：差异远大于全候选\n\n**分层 top-7 Jaccard 重叠率**（seed 42, 2920 matched queries / 12290 total）：\n| 层级 | BM25 vs Embedding | BM25 vs Random | BM25 vs Dataflow |\n|------|-------------------|----------------|------------------|\n| Small (<50 files, 39 repos) | 0.668 | 0.411 | 0.667 |\n| Medium (50-200, 29 repos) | 0.380 | 0.067 | 0.363 |\n| Large (200+, 15 repos) | 0.297 | 0.007 | 0.405 |\n\n**核心修正**：之前基于 87% 预测\"Phase 2 中 BM25 R@1 很可能接近 embedding\"——这个预测可能不成立。在中大 repo（训练数据主体）上 top-7 Jaccard 仅 30-38%，BM25 和 embedding 选出的训练 negatives 大部分不同。Phase 2 训练结果将真正区分两种策略。\n\n**意外发现**：BM25 vs dataflow 在大 repo 上重叠率（0.405）高于 vs embedding（0.297）。词汇相似性信号与数据流依赖有部分对齐，而纯 embedding 距离选择了不同维度的 hard negatives。\n\n---\n\n## hard_negative_mining.py vs build_m1_training_data.py 实现差异 [2026-05-15]\n\n**发现者**：Reviewer\n**影响**：当前 M2 不受影响（用 pre-mined 数据），plan_015（dynamic negative mining）实施前必须对齐\n\n**差异**：\n\n### hard_negative_mining.py `DataFlowAwareMiner`（training/hard_negative_mining.py）\n三步法：\n1. **Embedding top-K**：调用 `EmbeddingDistanceMiner.mine()` 获取 top-50 cosine similarity 最高的 candidates（从所有 non-positive candidates 中）\n2. **Dataflow filter**：过滤掉 `_is_reachable(query, fid)` 为 True 的文件——仅检查 `dataflow_graph[src]` 中的直接条目（1-hop 可达性）\n3. **BM25 re-rank**：如果 `bm25_index` 可用，对剩余 disconnected candidates 按 BM25 分数降序重排\n4. **Fallback**：如果 disconnected 不足 `num_negatives`，用 random padding 补足\n\n### build_m1_training_data.py `build_candidate_pools()`（scripts/build_m1_training_data.py）\n两步法：\n1. **Dataflow filter**：从 `non_pos_files` 中排除 `full_connected_set`（= `positive_files ∪ cg_connected`，即 dataflow 直连 + call graph 邻居——比 `DataFlowAwareMiner` 排除范围更广）\n2. **BM25 sort**：对 disconnected 文件按 BM25 分数降序排序，取 top-K（pool_size=50）\n3. **无 embedding 步骤**：dataflow pool 完全不使用 embedding 信号\n\n额外注意：当 `--model-path` 未提供时，`emb_scores = bm25`（line 317-318），此时 embedding pool 也退化为 BM25 排序，仅在是否排除 `full_connected` 上与 dataflow pool 不同。\n\n### 差异总结\n\n| 维度 | hard_negative_mining.py | build_m1_training_data.py |\n|------|------------------------|--------------------------|\n| Candidate 初筛 | Embedding cosine top-50 | 全部 non-positive（无初筛） |\n| Dataflow 排除范围 | `dataflow_graph[src]` 直接条目 | `positive_files ∪ cg_connected`（更广） |\n| 排序信号 | Embedding 为主 → BM25 re-rank | 纯 BM25 排序 |\n| Embedding 角色 | 主选择器（决定候选池） | 不参与 dataflow pool |\n| BM25 角色 | 可选的 re-ranker | 唯一排序信号 |\n\n### 对齐建议\nplan_015 实施 dynamic negative mining 时需统一为一种逻辑。建议：\n1. **排除范围统一**：采用 `build_m1_training_data.py` 的 `full_connected`（dataflow + call graph），因为 call graph 邻居也不应作为 hard negatives\n2. **选择信号**：dynamic mining 应使用当前 epoch 的 encoder embedding（不是 pretrained），这是 dynamic mining 的核心价值——所以 `DataFlowAwareMiner` 的 embedding→filter→BM25 三步法更合理，但需将排除范围从 1-hop dataflow 扩展到 full_connected\n3. **具体改动**：修改 `DataFlowAwareMiner._is_reachable()` 使其也排除 call graph 连接，或在 `mine()` 中接受 `full_connected_set` 参数\n\n---\n\n## 运维经验 (2026-05-14)\n\n**Registry 状态机 workaround**：当长链训练（多 run 串行）中途因 cron timeout 或子进程退出导致 registry 状态误标（DONE/failed 或 ANALYZING），而实际训练仍在跑时，不可回退状态。解决方案：创建 `{exp_id}_resumed` / `{exp_id}_continued` 新 entry，步进 PREPARING→QUEUED→ALLOCATED→RUNNING，注册 cron 监控实际 PID。原 entry 保留历史 metrics。\n\n**Bash 预读陷阱**：运行中的 bash 脚本已将循环体/数组预读到内存，磁盘上修改脚本文件不影响执行。需要在链外设置独立 tmux watcher 监控链 PID 退出后手动触发后续任务。\n\n**BM25 Phase 2 触发机制**：两个 tmux watcher（`bm25_starcoder_watcher`, `bm25_qwen_watcher`）每 5 分钟检查链 PID 存活，退出后自动启动 BM25 脚本。watcher 启动的训练不经过 submit_training_job，需在链完成回调中补注册 cron。\n\n---\n\n## 关键决策记录\n\n**m1_reextract_v2 数据使用决策 (2026-05-14, Director Session 8)**：即使 reextract 将数据从 ~16K 增至 ~44K，不重跑 M2。原因：ARR May 25 DDL 不允许再加 4-5 天重训。处理方式：(1) post-M2 完成后若有 GPU 空档，跑 1-seed pilot (Qwen, embedding, 新数据) 对比当前 M2 baseline；(2) 论文中作为 scalability/data efficiency 讨论点；(3) 全量重训留 camera-ready。\n\n---\n\n## Related Work Gap Analysis (2026-05-15)\n\n### 当前 Citation 统计 (literature_map.yaml)\n\n| Category | Count | 代表论文 |\n|----------|-------|---------|\n| code_retrieval_bug_fixing | 8 | SWE-bench, SWE-agent, AutoCodeRover, Agentless, SWE-smith, RepoBench, SweRank, SWE-Fixer |\n| hard_negative_mining | 6 | DPR, ANCE, SimCLR, SBERT, CL-DRD, CoCoHaNeRe |\n| contrastive_code_learning | 3 | ContraCode, CodeRetriever, Ding et al. (ACL 2022) |\n| program_analysis_for_ml | 6 | CodeQL (tool), code2vec, code2seq, FA-AST, GraphCodeBERT, ARISE |\n| code_embeddings_search | 9 | CodeSearchNet, CodeBERT, UniXcoder, StarCoder, Code Llama, Qwen2.5-Coder, DeepSeek-Coder, RepoFusion, BM25 |\n| graph_guided_inference | 5 | LocAgent, CodexGraph, RANGER, RepoGraph, GraphCoder |\n| infrastructure | 2 | FAISS, Tree-sitter |\n| **Total (literature_map)** | **39** | 含 2 个软件工具引用 |\n\n另有 memory.md 中 2 篇未入 literature_map：CodeRAG (arXiv 2025), CodeGRAG (arXiv 2024)。\n\n**已超过 25+ 目标**（39-41 篇），核心问题是覆盖均匀性。\n\n### 缺口识别 + 推荐论文\n\n#### Gap 1: Contrastive Learning for Code（当前仅 3 篇，最薄弱）\n\n**推荐添加：**\n\n1. **ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning**\n   - Authors: Shangqing Liu, Bozhi Wu, Xiaofei Xie, Guozhu Meng, Yang Liu\n   - Venue: ICSE 2023\n   - 为什么引：用 9 种程序级变换做对比学习增强代码预训练模型鲁棒性，是 code contrastive learning 的直接前序工作。StructFuse 的结构信号与其 augmentation 策略形成方法论对比。\n   - ✅ WebSearch 确认: ACM DL https://dl.acm.org/doi/abs/10.1109/ICSE48619.2023.00207\n\n2. **SynCoBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation**\n   - Authors: Xin Wang, Yasheng Wang, Fei Mi, et al.\n   - Venue: arXiv 2021 (arXiv:2108.04556, 广泛引用)\n   - 为什么引：用 AST 边 + 多模态（code/comment/AST）对比目标，是最接近\"结构感知对比学习\"的前序工作。与 StructFuse 用 data-flow 做负样本挖掘形成直接技术路线对比。\n   - ✅ WebSearch 确认: arXiv https://arxiv.org/abs/2108.04556\n\n#### Gap 2: Hard Negative Mining — 通用 ML 方法论（需补充 dense retrieval 经典方法）\n\n**推荐添加：**\n\n3. **RocketQA: An Optimized Training Approach to Dense Passage Retrieval for Open-Domain Question Answering**\n   - Authors: Yingqi Qu, Yuchen Ding, Jing Liu, et al.\n   - Venue: NAACL 2021\n   - 为什么引：提出 denoised hard negative sampling（用 cross-encoder 过滤 false negatives），其\"去噪\"直觉与 StructFuse 用 data-flow 结构过滤假阴性负样本的思路高度对应。\n   - ✅ WebSearch 确认: ACL Anthology https://aclanthology.org/2021.naacl-main.466/\n\n4. **CAPSTONE: Curriculum Sampling for Dense Retrieval with Document Expansion**\n   - Authors: Xingwei He, Yeyun Gong, A-Long Jin, et al.\n   - Venue: EMNLP 2023\n   - 为什么引：渐进难度调度训练样本用于密集检索，支持 StructFuse 中 hard_negative_ratio 从简到难的课程学习式解读。与已有的 CL-DRD (SIGIR 2022) 互补。\n   - ✅ WebSearch 确认: ACL Anthology https://aclanthology.org/2023.emnlp-main.651/\n\n#### Gap 3: Code Search Benchmarks（缺标准评测集引用）\n\n**推荐添加：**\n\n5. **CoSQA: 20,000+ Web Queries for Code Search and Question Answering**\n   - Authors: Junjie Huang, Duyu Tang, Linjun Shou, et al.\n   - Venue: ACL 2021\n   - 为什么引：标准代码搜索 benchmark + CoCLR 对比学习方法，是 code retrieval problem formulation 的重要引用。\n   - ✅ WebSearch 确认: ACL Anthology https://aclanthology.org/2021.acl-long.442/\n\n#### Gap 4: Repository-level Code Understanding（当前无专门的 cross-file benchmark 引用）\n\n**推荐添加：**\n\n6. **CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion**\n   - Authors: Yangruibo Ding, Zijian Wang, Wasi Uddin Ahmad, et al.\n   - Venue: NeurIPS 2023 (Datasets & Benchmarks)\n   - 为什么引：建立了 cross-file 结构理解的必要性，直接论证 call-graph 级别上下文对 repo-scale 代码检索的重要性。\n   - ✅ WebSearch 确认: NeurIPS Proceedings 2023\n\n#### Gap 5: Program Analysis + Deep Learning（缺程序图 ML 奠基工作）\n\n**推荐添加：**\n\n7. **ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations**\n   - Authors: Chris Cummins, Zacharias Fisches, Tal Ben-Nun, et al.\n   - Venue: ICML 2021\n   - 为什么引：将程序表示为 control/data/call-flow 三合一图用于 ML，是\"data-flow 信号用于机器学习\"的奠基性正当化引用。与 GraphCodeBERT (ICLR 2021) 互补——GraphCodeBERT 在 NLP 预训练中用 data-flow，ProGraML 在编译优化中用。\n   - ✅ WebSearch 确认: ICML 2021 Proceedings https://proceedings.mlr.press/v139/cummins21a.html\n\n### 已充分覆盖的领域\n\n- **SWE-bench 生态** (8 篇)：SWE-bench, SWE-agent, Agentless, AutoCodeRover, SWE-smith, RepoBench, SweRank, SWE-Fixer — 覆盖 benchmark + 主流 agent/retrieval 方法 ✓\n- **Code embeddings / LLM** (9 篇)：CodeBERT → UniXcoder → StarCoder/Qwen2.5-Coder/DeepSeek-Coder 演进链完整 ✓\n- **Inference-time graph methods** (5+3=8 篇)：覆盖所有主要 2024-2026 graph-guided code 方法 ✓\n- **Infrastructure** (2)：FAISS, Tree-sitter — 作为工具引用足够 ✓\n\n### 达到目标的路径\n\n| 状态 | Count |\n|------|-------|\n| literature_map.yaml 当前 | 39 |\n| memory.md 额外 (CodeRAG, CodeGRAG) | +2 |\n| Gap 1: contrastive_code_learning (+ContraBERT, +SynCoBERT) | +2 |\n| Gap 2: hard_negative_mining (+RocketQA, +CAPSTONE) | +2 |\n| Gap 3: code_search_benchmarks (+CoSQA) | +1 |\n| Gap 4: repo-level understanding (+CrossCodeEval) | +1 |\n| Gap 5: program_analysis_for_ml (+ProGraML) | +1 |\n| **添加后总计** | **48** |\n\n添加 7 篇后达到 48 篇，远超 25+ 目标。每个核心领域至少 5 篇，覆盖均匀。\n\n### 优先级\n\n1. **必须加** (reviewer 会注意到缺失): RocketQA, ContraBERT, ProGraML, CrossCodeEval\n2. **强烈建议** (加厚薄弱领域): SynCoBERT, CAPSTONE\n3. **可选** (锦上添花): CoSQA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "1b5795f4-2648-4930-a604-4ac2d4076a65",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014vNhcEEcd7rC9YXuByWDuf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5474,
      "cache_read_input_tokens": 42553,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5474
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

_source line 112 · 2026-05-15T04:20:34.826Z_

<details><summary>↩ Tool result · `toolu_01TrRpzEAh61iXd2GXXWfvrr`</summary>

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
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "07241d98-dc4c-4a17-9437-0384ed1d468a",
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

_source line 113_

Gap 分析已写入 memory.md。

**摘要**：

- 当前 literature_map.yaml 39 篇，已超 25+ 目标，但覆盖不均
- 最薄弱：contrastive learning for code（仅 3 篇）、通用 hard negative mining 方法论
- 推荐添加 7 篇（全部 WebSearch 验证真实存在）：
  - **必须加**：RocketQA (NAACL 2021)、ContraBERT (ICSE 2023)、ProGraML (ICML 2021)、CrossCodeEval (NeurIPS 2023)
  - **强烈建议**：SynCoBERT (arXiv 2021)、CAPSTONE (EMNLP 2023)
  - **可选**：CoSQA (ACL 2021)
- 添加后总计 48 篇，各领域均 ≥5 篇

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "uuid": "b85c4366-58be-4d1f-af5d-da8b992e94ef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HR33mJdGTAytqt5St43Twy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8219,
      "cache_read_input_tokens": 48027,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8219
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

_source line 114_

Gap 分析已写入 memory.md。

**摘要**：

- 当前 literature_map.yaml 39 篇，已超 25+ 目标，但覆盖不均
- 最薄弱：contrastive learning for code（仅 3 篇）、通用 hard negative mining 方法论
- 推荐添加 7 篇（全部 WebSearch 验证真实存在）：
  - **必须加**：RocketQA (NAACL 2021)、ContraBERT (ICSE 2023)、ProGraML (ICML 2021)、CrossCodeEval (NeurIPS 2023)
  - **强烈建议**：SynCoBERT (arXiv 2021)、CAPSTONE (EMNLP 2023)
  - **可选**：CoSQA (ACL 2021)
- 添加后总计 48 篇，各领域均 ≥5 篇

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 320230,
  "duration_api_ms": 440861,
  "num_turns": 9,
  "stop_reason": "end_turn",
  "session_id": "5aa694bc-55d9-43e1-8a1d-5e86f4052691",
  "total_cost_usd": 1.7498340000000001,
  "usage": {
    "input_tokens": 11,
    "cache_creation_input_tokens": 44799,
    "cache_read_input_tokens": 227750,
    "output_tokens": 12437,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 44799,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 265,
        "cache_read_input_tokens": 48027,
        "cache_creation_input_tokens": 8219,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 8219
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 457788,
      "outputTokens": 10383,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 26,
      "costUSD": 0.769703,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 11,
      "outputTokens": 12437,
      "cacheReadInputTokens": 227750,
      "cacheCreationInputTokens": 44799,
      "webSearchRequests": 0,
      "costUSD": 0.70484875,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    },
    "claude-sonnet-4-6": {
      "inputTokens": 6660,
      "outputTokens": 3490,
      "cacheReadInputTokens": 176895,
      "cacheCreationInputTokens": 39969,
      "webSearchRequests": 0,
      "costUSD": 0.27528225,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "a30968c9-f218-4b47-b083-1eafe7f569b6"
}
```

</details>

---
