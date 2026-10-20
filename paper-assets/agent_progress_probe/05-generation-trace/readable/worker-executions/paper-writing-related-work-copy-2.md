# paper writing related work

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 26
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/workers/worker_paper_writing_related_work_20260514T220345.log`
- **Structured JSON:** [`cad46bd6d7cb53319aee.json`](../../sessions/ca/cad46bd6d7cb53319aee.json)

## Before a recorded user message

26 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe",
  "session_id": "1311e2e5-9af4-44d3-8961-4a2f79dde730",
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
    "mcp__agent-ml-research__register_artifact",
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
  "uuid": "5c8a87ae-6a18-435e-88e9-9ca5d3088298",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-projects-agent-progress-probe/memory/"
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
    "resetsAt": 1778800200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "cb8127d5-2d66-4ce6-b126-a873adf52d85",
  "session_id": "1311e2e5-9af4-44d3-8961-4a2f79dde730"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by gathering all the necessary context: the literature map, paper framing, introduction, and bib file. I'll read these in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1311e2e5-9af4-44d3-8961-4a2f79dde730",
  "uuid": "e00cd1dc-0bdb-4fa1-8a72-d54ea1614bd6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HV9ZarHBurnY844V3vd5d5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11722,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11722
      },
      "output_tokens": 35,
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

Let me gather all the reference materials first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1311e2e5-9af4-44d3-8961-4a2f79dde730",
  "uuid": "1f66b73f-51bc-41a2-b3ac-492b136334bf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HV9ZarHBurnY844V3vd5d5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11722,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11722
      },
      "output_tokens": 35,
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01TQzfKvqPfkzU2MsqPSN63V`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1311e2e5-9af4-44d3-8961-4a2f79dde730",
  "uuid": "71077cec-335d-4716-80e1-d43abef8b239",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HV9ZarHBurnY844V3vd5d5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11722,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11722
      },
      "output_tokens": 35,
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

_source line 7 · 2026-05-14T22:03:58.726Z_

<details><summary>↩ Tool result · `toolu_01TQzfKvqPfkzU2MsqPSN63V`</summary>

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
  "tool_name": "mcp__agent-ml-research__register_artifact"
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
  "session_id": "1311e2e5-9af4-44d3-8961-4a2f79dde730",
  "uuid": "f4d47790-7b52-4db0-9280-808e6a1b576b",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01NuCGHJ2hk2M6jzRvRW7xhV`</summary>

```json
{
  "project": "agent_progress_probe",
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
  "session_id": "1311e2e5-9af4-44d3-8961-4a2f79dde730",
  "uuid": "ae48220c-e841-4033-bc2d-609fbe2be368",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016iV8ChfDzEdb5s2Z8CUR1E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1105,
      "cache_read_input_tokens": 23563,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1105
      },
      "output_tokens": 73,
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

_source line 9 · 2026-05-14T22:04:01.831Z_

<details><summary>↩ Tool result · `toolu_01NuCGHJ2hk2M6jzRvRW7xhV`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/literature_map.yaml\", \"content\": \"# Literature Map for Agent Progress Probe (EMNLP 2026 ARR)\\n# Generated: 2026-05-14\\n# Paper: Structural Signal Analysis for Progress Stagnation Detection in LLM Agents\\n#\\n# D039 Pivot: Empirical analysis paper. Central finding: stagnation signals are\\n# fundamentally structural (30 features → 0.995 in-domain, 0.967 cross-agent F1),\\n# decisively surpassing NL embeddings (0.906/0.751) and LLM-as-judge (+24.3pp).\\n# TLM is a well-motivated negative finding (3 implementations all fail to beat MV).\\n\\npapers:\\n\\n  # ============================================================\\n  # CATEGORY: direct-competitor\\n  # ============================================================\\n\\n  - id: \\\"xi2025agentprm\\\"\\n    title: \\\"AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress\\\"\\n    authors: \\\"Zhiheng Xi, Chenyang Liao, Guanyu Li, Yajie Yang, Wenxiang Chen, Zhihao Zhang, Binghai Wang, Senjie Jin, Yuhao Zhou, Jian Guan, Wei Wu, Tao Ji, Tao Gui, Qi Zhang, Xuanjing Huang\\\"\\n    venue: \\\"arXiv preprint\\\"\\n    year: 2025\\n    arxiv: \\\"2511.08325\\\"\\n    category: \\\"direct-competitor\\\"\\n    role: \\\"主要竞争者：step-level PRM for agent guidance\\\"\\n    key_finding: \\\"用 promise（长期潜力）和 progress（即时进展）两个维度评估 agent 每步决策，实现 8x 计算效率提升\\\"\\n    our_differentiation: \\\"我们是 window-level monitoring（不是 step-level guidance），不需要 outcome labels，目标是 stagnation detection 不是 reward shaping\\\"\\n\\n  - id: \\\"choudhury2025prm\\\"\\n    title: \\\"Process Reward Models for LLM Agents: Practical Framework and Directions\\\"\\n    authors: \\\"Sanjiban Choudhury\\\"\\n    venue: \\\"arXiv preprint\\\"\\n    year: 2025\\n    arxiv: \\\"2502.10325\\\"\\n    category: \\\"direct-competitor\\\"\\n    role: \\\"PRM 框架综述 + InversePRM 方法\\\"\\n    key_finding: \\\"提出 AgentPRM（Monte Carlo rollout actor-critic）和 InversePRM（从 demonstrations 学习 process reward），3B 模型超越 GPT-4o\\\"\\n    our_differentiation: \\\"InversePRM 仍需 demonstration trajectories，我们用 programmatic LFs 替代人工标注；我们关注 monitoring 而非 training signal\\\"\\n\\n  - id: \\\"li2026toolprmbench\\\"\\n    title: \\\"ToolPRMBench: Evaluating and Advancing Process Reward Models for Tool-using Agents\\\"\\n    authors: \\\"Dawei Li, Yuguang Yao, Zhen Tan, Huan Liu, Ruocheng Guo\\\"\\n    venue: \\\"arXiv preprint\\\"\\n    year: 2026\\n    arxiv: \\\"2601.12294\\\"\\n    category: \\\"direct-competitor\\\"\\n    role: \\\"Tool-use PRM 评测基准\\\"\\n    key_finding: \\\"大规模 benchmark 评测 PRM 在 tool-use 场景的效果，发现专用 PRM 显著优于通用 PRM\\\"\\n    our_differentiation: \\\"我们的 empirical analysis 揭示 structural features 足以检测 stagnation（0.995 F1），无需 step-level reward labels；关注 stagnation pattern 而非 step correctness\\\"\\n\\n  - id: \\\"wang2026planrewardbench\\\"\\n    title: \\\"Aligning Agents via Planning: A Benchmark for Trajectory-Level Reward Modeling\\\"\\n    authors: \\\"Jiaxuan Wang, Yulan Hu, Wenjin Yang, Zheng Pan, Xin Li, Lan-Zhe Guo\\\"\\n    venue: \\\"arXiv preprint\\\"\\n    year: 2026\\n    arxiv: \\\"2604.08178\\\"\\n    category: \\\"direct-competitor\\\"\\n    role: \\\"Trajectory-level reward model 评测\\\"\\n    key_finding: \\\"所有 reward model 类别（generative, discriminative, LLM-as-Judge）在长 horizon trajectory 上性能显著下降\\\"\\n    our_differentiation: \\\"验证了长 trajectory 评估的难度——我们的 window-level 方法通过局部化避免了这个问题\\\"\\n\\n  - id: \\\"chen2025monitoring\\\"\\n    title: \\\"Monitoring LLM Agents for Sequentially Contextual Harm\\\"\\n    authors: \\\"Yueh-Han Chen, Neelay Joshi, Yulin Chen, He He, Rico Angell\\\"\\n    venue: \\\"ICLR 2025 Workshop on Building Trust in Language Models and Applications\\\"\\n    year: 2025\\n    arxiv: null\\n    openreview: \\\"LC0XQ6ufbr\\\"\\n    category: \\\"direct-competitor\\\"\\n    role: \\\"Agent monitoring 安全方向\\\"\\n    key_finding: \\\"将有害任务分解为单独无害的子任务可将 refusal rate 从 50% 降至 10%，现有 monitor 难以检测 sequentially contextual harm\\\"\\n    our_differentiation: \\\"他们关注 safety monitoring（harmful behavior），我们关注 progress monitoring（stagnation）；互补方向\\\"\\n\\n  - id: \\\"kale2025weaktostrong\\\"\\n    title: \\\"Reliable Weak-to-Strong Monitoring of LLM Agents\\\"\\n    authors: \\\"Neil Kale, Chen Bo Calvin Zhang, Kevin Zhu, Ankit Aich, Paula Rodriguez, Scale Red Team, Christina Q. Knight, Zifan Wang\\\"\\n    venue: \\\"arXiv preprint\\\"\\n    year: 2025\\n    arxiv: \\\"2508.19461\\\"\\n    category: \\\"direct-competitor\\\"\\n    role: \\\"Weak-to-strong agent monitoring 方法论\\\"\\n    key_finding: \\\"Monitor scaffolding 比 monitor 能力更重要，弱模型可以可靠监控强模型；targeted human-in-the-loop 提升 TPR ~15%\\\"\\n    our_differentiation: \\\"他们用 LLM 作为 monitor，我们发现 30 个 structural features 即可达 0.967 跨域 F1，不依赖另一个 LLM；更轻量（<5ms）且可解释\\\"\\n\\n  - id: \\\"fan2026agentrm\\\"\\n    title: \\\"Exploring Reasoning Reward Model for Agents\\\"\\n    authors: \\\"Kaixuan Fan, Kaituo Feng, Manyuan Zhang, Tianshuo Peng, Zhixun Li, Yilei Jiang, Shuang Chen, Peng Pei, Xunliang Cai, Xiangyu Yue\\\"\\n    venue: \\\"arXiv preprint\\\"\\n    year: 2026\\n    arxiv: \\\"2601.22154\\\"\\n    category: \\\"direct-competitor\\\"\\n    verified: true\\n    role: \\\"Agent trajectory 的多维度 reasoning reward model\\\"\\n    key_finding: \\\"Agent-RRM 通过 reasoning trace + critique + overall score 三维结构化反馈评估 agent trajectory，在 12 个 benchmark 上显著提升（GAIA 43.7%, WebWalkerQA 46.2%）\\\"\\n    our_differentiation: \\\"他们用 LLM-based reward model 生成结构化反馈用于 agent 改进，我们的 empirical analysis 表明轻量 structural features 即可高精度检测 stagnation（0.995 F1），不依赖大模型推理\\\"\\n\\n  - id: \\\"qiu2026dataprm\\\"\\n    title: \\\"Rewarding the Scientific Process: Process-Level Reward Modeling for Agentic Data Analysis\\\"\\n    authors: \\\"Zhisong Qiu, Shuofei Qiao, Kewei Xu, Yuqi Zhu, Lun Du, Ningyu Zhang, Huajun Chen\\\"\\n    venue: \\\"arXiv preprint\\\"\\n    year: 2026\\n    arxiv: \\\"2604.24198\\\"\\n    category: \\\"direct-competitor\\\"\\n    verified: true\\n    role: \\\"Agentic data analysis 场景的 process-level reward model\\\"\\n    key_finding: \\\"传统 PRM 无法检测 silent errors 且误判 exploratory steps；DataPRM 通过 environment-aware probing + ternary reward 策略在 ScienceAgentBench 提升 7.21%\\\"\\n    our_differentiation: \\\"DataPRM 针对数据分析 agent 的 step correctness，我们针对通用 agent 的 stagnation pattern；他们需要 execution state probing，我们用 structural LFs 无需环境交互\\\"\\n\\n  # ============================================================\\n  # CATEGORY: method-component\\n  # ============================================================\\n\\n  - id: \\\"ratner2016dataprogramming\\\"\\n    title: \\\"Data Programming: Creating Large Training Sets, Quickly\\\"\\n    authors: \\\"Alexander Ratner, Christopher De Sa, Sen Wu, Daniel Selsam, Christopher Re\\\"\\n    venue: \\\"NeurIPS 2016\\\"\\n    year: 2016\\n    arxiv: \\\"1605.07723\\\"\\n    category: \\\"method-component\\\"\\n    role: \\\"核心方法论基础：data programming 范式\\\"\\n    key_finding: \\\"用户编写 labeling functions（噪声启发式），generative model 学习 LF 准确率生成概率训练标签\\\"\\n    our_differentiation: \\\"我们在 agent trajectory 上应用 data programming，发现 structural features 主导检测能力；同时揭示 LFs 的时序动态和 temporal label model 的负面结果\\\"\\n\\n  - id: \\\"ratner2017snorkel\\\"\\n    title: \\\"Snorkel: Rapid Training Data Creation with Weak Supervision\\\"\\n    authors: \\\"Alexander Ratner, Stephen H. Bach, Henry Ehrenberg, Jason Fries, Sen Wu, Christopher Re\\\"\\n    venue: \\\"VLDB 2018\\\"\\n    year: 2018\\n    arxiv: \\\"1711.10160\\\"\\n    category: \\\"method-component\\\"\\n    role: \\\"Data programming 系统实现，label model 基础\\\"\\n    key_finding: \\\"端到端弱监督系统：LFs → generative label model（建模 LF dependency）→ discriminative end model\\\"\\n    our_differentiation: \\\"Snorkel 假设数据点 i.i.d.，我们发现 agent trajectory 上 LFs 展现系统性时序动态（violating i.i.d.），但 temporal label model 未能超越 MV（negative finding）\\\"\\n\\n  - id: \\\"fu2020flyingsquid\\\"\\n    title: \\\"Fast and Three-rious: Speeding Up Weak Supervision with Triplet Methods\\\"\\n    authors: \\\"Daniel Y. Fu, Mayee F. Chen, Frederic Sala, Sarah M. Hooper, Kayvon Fatahalian, Christopher Re\\\"\\n    venue: \\\"ICML 2020\\\"\\n    year: 2020\\n    arxiv: \\\"2002.11955\\\"\\n    category: \\\"method-component\\\"\\n    role: \\\"快速 label model，triplet method of moments\\\"\\n    key_finding: \\\"用 triplet method 闭式求解 label model 参数，比 SGD 快 170x\\\"\\n    our_differentiation: \\\"FlyingSquid 同样假设 i.i.d.；我们的 empirical analysis 揭示 i.i.d. violation 虽系统性存在，但 temporal correction 在低冲突 regime 下无收益（negative finding）\\\"\\n\\n  - id: \\\"zhang2021wrench\\\"\\n    title: \\\"WRENCH: A Comprehensive Benchmark for Weak Supervision\\\"\\n    authors: \\\"Jieyu Zhang, Yue Yu, Yinghao Li, Yujing Wang, Yaming Yang, Mao Yang, Alexander Ratner\\\"\\n    venue: \\\"NeurIPS 2021 Datasets and Benchmarks Track\\\"\\n    year: 2021\\n    arxiv: \\\"2109.11377\\\"\\n    category: \\\"method-component\\\"\\n    role: \\\"弱监督评测基准\\\"\\n    key_finding: \\\"22 个真实数据集 + 120+ 方法变体评测，标准化弱监督研究\\\"\\n    our_differentiation: \\\"WRENCH 数据集全是 i.i.d. 分类/序列标注，没有 temporal stagnation detection 任务\\\"\\n\\n  - id: \\\"safranchik2020linkedhmm\\\"\\n    title: \\\"Weakly Supervised Sequence Tagging from Noisy Rules\\\"\\n    authors: \\\"Esteban Safranchik, Shiying Luo, Stephen H. Bach\\\"\\n    venue: \\\"AAAI 2020\\\"\\n    year: 2020\\n    arxiv: null\\n    category: \\\"method-component\\\"\\n    role: \\\"最近的方法论前驱：linked HMM for sequence tagging weak supervision\\\"\\n    key_finding: \\\"将 HMM 引入弱监督序列标注（NER），加入 linking rules 建模 span 结构，比 i.i.d. label model +7 F1\\\"\\n    our_differentiation: \\\"他们是 token-level NER（BIO 约束），我们是 window-level temporal classification；我们建模的是 stagnation temporal dynamics 而非 entity boundary\\\"\\n\\n  - id: \\\"sala2019multiresolution\\\"\\n    title: \\\"Multi-Resolution Weak Supervision for Sequential Data\\\"\\n    authors: \\\"Frederic Sala, Paroma Varma, Jason Fries, Daniel Y. Fu, Stefano Sagawa, Christopher Re\\\"\\n    venue: \\\"NeurIPS 2019\\\"\\n    year: 2019\\n    arxiv: \\\"1910.09505\\\"\\n    category: \\\"method-component\\\"\\n    role: \\\"最近的方法论前驱：multi-resolution WS for sequential data\\\"\\n    key_finding: \\\"处理不同时间分辨率的 LFs（如 frame-level vs span-level），建模 multi-resolution LF correlations\\\"\\n    our_differentiation: \\\"他们关注 resolution mismatch，我们关注 temporal label transitions；互补视角\\\"\\n\\n  - id: \\\"dawid1979em\\\"\\n    title: \\\"Maximum Likelihood Estimation of Observer Error-Rates Using the EM Algorithm\\\"\\n    authors: \\\"A. P. Dawid, A. M. Skene\\\"\\n    venue: \\\"Journal of the Royal Statistical Society, Series C\\\"\\n    year: 1979\\n    arxiv: null\\n    category: \\\"method-component\\\"\\n    role: \\\"Label aggregation 奠基工作\\\"\\n    key_finding: \\\"用 EM 算法估计标注者混淆矩阵，无需 ground truth\\\"\\n    our_differentiation: \\\"经典 i.i.d. 假设；我们测试了 temporal extension（HMM-TLM, lag-aware HMM）但发现在 3-LF 低冲突 regime 下未超越 MV——约束未来 temporal label model 研究\\\"\\n\\n  - id: \\\"nguyen2017hmmcrowd\\\"\\n    title: \\\"Aggregating and Predicting Sequence Labels from Crowd Annotations\\\"\\n    authors: \\\"An Thanh Nguyen, Byron C. Wallace, Junyi Jessy Li, Ani Nenkova, Matthew Lease\\\"\\n    venue: \\\"ACL 2017\\\"\\n    year: 2017\\n    arxiv: null\\n    category: \\\"method-component\\\"\\n    role: \\\"HMM + crowdsourcing label aggregation\\\"\\n    key_finding: \\\"HMM-Crowd：扩展 Dawid-Skene 到序列数据，加入 one-step Markov structure over true labels\\\"\\n    our_differentiation: \\\"他们用于 crowdsourcing（人类标注者），我们用于 programmatic LFs（自动化）；他们是 NER/IE，我们是 agent progress monitoring\\\"\\n\\n  # ============================================================\\n  # CATEGORY: evaluation\\n  # ============================================================\\n\\n  - id: \\\"orlanski2026slopcodebench\\\"\\n    title: \\\"SlopCodeBench: Benchmarking How Coding Agents Degrade Over Long-Horizon Iterative Tasks\\\"\\n    authors: \\\"Gabriel Orlanski, Devjeet Roy, Alexander Yun, Changho Shin, Alex Gu, Albert Ge, Dyah Adila, Nicholas Roberts, Frederic Sala, Aws Albarghouthi\\\"\\n    venue: \\\"arXiv preprint\\\"\\n    year: 2026\\n    arxiv: \\\"2603.24755\\\"\\n    category: \\\"evaluation\\\"\\n    role: \\\"Agent degradation 基准——直接支持我们的 problem motivation\\\"\\n    key_finding: \\\"Agent 代码质量在迭代任务中持续退化：比人类代码 2.3x 更冗余、2.0x 更结构侵蚀，75-77% trajectory 呈现退化趋势\\\"\\n    our_differentiation: \\\"SlopCodeBench 量化了 degradation 现象，我们提供了检测方法；他们是 post-hoc 评测，我们是 online monitoring\\\"\\n\\n  - id: \\\"jimenez2024swebench\\\"\\n    title: \\\"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?\\\"\\n    authors: \\\"Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan\\\"\\n    venue: \\\"ICLR 2024\\\"\\n    year: 2024\\n    arxiv: \\\"2310.06770\\\"\\n    category: \\\"evaluation\\\"\\n    role: \\\"Agent 数据来源之一\\\"\\n    key_finding: \\\"2294 个真实 GitHub issue 任务，标准化 agent 评测\\\"\\n    our_differentiation: \\\"我们使用 SWE-bench agent trajectories 作为实验数据源之一\\\"\\n\\n  - id: \\\"yang2024sweagent\\\"\\n    title: \\\"SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering\\\"\\n    authors: \\\"John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press\\\"\\n    venue: \\\"NeurIPS 2024\\\"\\n    year: 2024\\n    arxiv: \\\"2405.15793\\\"\\n    category: \\\"evaluation\\\"\\n    role: \\\"Agent 系统——trajectory 数据来源\\\"\\n    key_finding: \\\"提出 agent-computer interface (ACI)，GPT-4 Turbo 在 SWE-bench 达 12.47% resolve rate\\\"\\n    our_differentiation: \\\"SWE-agent trajectories 是我们分析 stagnation 的数据来源之一\\\"\\n\\n  - id: \\\"wang2025openhands\\\"\\n    title: \\\"OpenHands: An Open Platform for AI Software Developers as Generalist Agents\\\"\\n    authors: \\\"Xingyao Wang, Boxuan Li, Yufan Song, Frank F. Xu, Xiangru Tang, et al.\\\"\\n    venue: \\\"ICLR 2025\\\"\\n    year: 2025\\n    arxiv: \\\"2407.16741\\\"\\n    category: \\\"evaluation\\\"\\n    role: \\\"Agent 平台——主要数据来源\\\"\\n    key_finding: \\\"开源 agent 平台，sandbox 执行环境，15+ benchmarks 评测\\\"\\n    our_differentiation: \\\"OpenHands trajectories 是我们的主要实验数据来源\\\"\\n\\n  - id: \\\"zhou2024webarena\\\"\\n    title: \\\"WebArena: A Realistic Web Environment for Building Autonomous Agents\\\"\\n    authors: \\\"Shuyan Zhou, Frank F. Xu, Hao Zhu, Xuhui Zhou, Robert Lo, Abishek Sridhar, Xianyi Cheng, Tianyue Ou, Yonatan Bisk, Daniel Fried, Uri Alon, Graham Neubig\\\"\\n    venue: \\\"ICLR 2024\\\"\\n    year: 2024\\n    arxiv: \\\"2307.13854\\\"\\n    category: \\\"evaluation\\\"\\n    verified: true\\n    role: \\\"Web agent 评测基准——long-horizon 任务评估\\\"\\n    key_finding: \\\"812 个真实网站上的 long-horizon 任务，GPT-4 agent 仅 14.41% 成功率 vs 人类 78.24%，揭示 agent 在复杂任务上的巨大差距\\\"\\n    our_differentiation: \\\"WebArena 的 long-horizon 任务正是 stagnation 高发场景；我们的 monitor 可作为此类任务的早期终止/干预信号\\\"\\n\\n  - id: \\\"wang2024mint\\\"\\n    title: \\\"MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback\\\"\\n    authors: \\\"Xingyao Wang, Zihan Wang, Jiateng Liu, Yangyi Chen, Lifan Yuan, Hao Peng, Heng Ji\\\"\\n    venue: \\\"ICLR 2024\\\"\\n    year: 2024\\n    arxiv: \\\"2309.10691\\\"\\n    category: \\\"evaluation\\\"\\n    verified: true\\n    role: \\\"Multi-turn agent 评测基准——tool use + feedback 交互评估\\\"\\n    key_finding: \\\"评估 LLM 在多轮交互中使用工具和接收自然语言反馈的能力，每轮 tool use 提升 1-8%，NL feedback 提升 2-17%\\\"\\n    our_differentiation: \\\"MINT 量化了 multi-turn 交互中的性能变化，我们的 stagnation detection 关注多轮交互中进展停滞的检测；MINT 的 multi-turn 设定与我们的 window-level 分析天然对齐\\\"\\n\\n  # ============================================================\\n  # CATEGORY: background\\n  # ============================================================\\n\\n  - id: \\\"shinn2023reflexion\\\"\\n    title: \\\"Reflexion: Language Agents with Verbal Reinforcement Learning\\\"\\n    authors: \\\"Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao\\\"\\n    venue: \\\"NeurIPS 2023\\\"\\n    year: 2023\\n    arxiv: \\\"2303.11366\\\"\\n    category: \\\"background\\\"\\n    role: \\\"Agent self-reflection 代表工作\\\"\\n    key_finding: \\\"通过 verbal feedback 强化 agent，反思文本存入 episodic memory 用于后续 trial\\\"\\n    our_differentiation: \\\"Reflexion 是 agent 自我改进机制，我们是外部 monitoring；self-reflection 可能失效时我们的 monitor 仍能检测 stagnation\\\"\\n\\n  - id: \\\"zhou2024lats\\\"\\n    title: \\\"Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models\\\"\\n    authors: \\\"Andy Zhou, Kai Yan, Michal Shlapentokh-Rothman, Haohan Wang, Yu-Xiong Wang\\\"\\n    venue: \\\"ICML 2024\\\"\\n    year: 2024\\n    arxiv: \\\"2310.04406\\\"\\n    category: \\\"background\\\"\\n    role: \\\"Agent planning + self-reflection\\\"\\n    key_finding: \\\"结合 MCTS 与 LM value function 和 self-reflection，支持 backtracking\\\"\\n    our_differentiation: \\\"LATS 通过搜索避免 stagnation，但计算开销大；我们的 monitor 可作为 LATS 的早期终止信号\\\"\\n\\n  - id: \\\"yao2023tot\\\"\\n    title: \\\"Tree of Thoughts: Deliberate Problem Solving with Large Language Models\\\"\\n    authors: \\\"Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Thomas L. Griffiths, Yuan Cao, Karthik Narasimhan\\\"\\n    venue: \\\"NeurIPS 2023\\\"\\n    year: 2023\\n    arxiv: \\\"2305.10601\\\"\\n    category: \\\"background\\\"\\n    role: \\\"Deliberate reasoning 框架\\\"\\n    key_finding: \\\"将 CoT 泛化为树结构，LM 自我评估中间 thought 并 backtrack\\\"\\n    our_differentiation: \\\"ToT 的自评估是 single-step 的；我们捕捉 multi-step temporal patterns\\\"\\n\\n  - id: \\\"cemri2025multiagentfail\\\"\\n    title: \\\"Why Do Multi-Agent LLM Systems Fail?\\\"\\n    authors: \\\"Mert Cemri, Melissa Z. Pan, Shuyi Yang, Lakshya A. Agrawal, et al.\\\"\\n    venue: \\\"arXiv preprint\\\"\\n    year: 2025\\n    arxiv: \\\"2503.13657\\\"\\n    category: \\\"background\\\"\\n    role: \\\"Agent failure taxonomy——problem motivation\\\"\\n    key_finding: \\\"MAST taxonomy：14 种失败模式，其中 Step Repetition 被识别为具体失败症状\\\"\\n    our_differentiation: \\\"他们提供 taxonomy（what fails），我们提供 detection method（how to detect）\\\"\\n\\n  - id: \\\"zhu2025agentfail\\\"\\n    title: \\\"Where LLM Agents Fail and How They Can Learn From Failures\\\"\\n    authors: \\\"Kunlun Zhu, Zijia Liu, Bingxuan Li, et al.\\\"\\n    venue: \\\"arXiv preprint\\\"\\n    year: 2025\\n    arxiv: \\\"2509.25370\\\"\\n    category: \\\"background\\\"\\n    role: \\\"Agent failure 分析 + cascading failure 发现\\\"\\n    key_finding: \\\"Cascading failures（单一 root cause 传播到后续决策）是长 horizon 任务的主要失败模式\\\"\\n    our_differentiation: \\\"Cascading failure 正是我们 temporal model 可以捕捉的 pattern——stagnation 往往是 cascade 的表现\\\"\\n\\n  - id: \\\"george2025cycledetection\\\"\\n    title: \\\"Unsupervised Cycle Detection in Agentic Applications\\\"\\n    authors: \\\"Felix George, Harshit Kumar, Divya Pathak, Kaustabha Ray, Mudit Verma, Pratibha Moogi\\\"\\n    venue: \\\"arXiv preprint (IBM Research)\\\"\\n    year: 2025\\n    arxiv: \\\"2511.10650\\\"\\n    category: \\\"background\\\"\\n    role: \\\"Cycle detection——最相关的 stagnation detection 前驱\\\"\\n    key_finding: \\\"混合方法：call-stack 分析（结构重复）+ embedding 语义相似度确认\\\"\\n    our_differentiation: \\\"他们只检测 exact/near-exact cycles，我们检测更广义的 stagnation（包括非重复性的停滞）；我们的 empirical analysis 表明 30 个 structural features（含但不限于 cycle 特征）即可达 0.995 F1\\\"\\n\\n  - id: \\\"pipis2025reasoningloop\\\"\\n    title: \\\"Wait, Wait, Wait... Why Do Reasoning Models Loop?\\\"\\n    authors: \\\"Charilaos Pipis, Shivam Garg, Vasilis Kontonis, Vaishnavi Shrivastava, Akshay Krishnamurthy, Dimitris Papailiopoulos\\\"\\n    venue: \\\"arXiv preprint\\\"\\n    year: 2025\\n    arxiv: \\\"2512.12895\\\"\\n    category: \\\"background\\\"\\n    role: \\\"Reasoning model looping 分析\\\"\\n    key_finding: \\\"Looping 是 risk-aversion 的表现：模型选择简单循环动作而非推进；用 30-gram 重复检测\\\"\\n    our_differentiation: \\\"他们分析 reasoning model 内部循环的原因，我们检测 agent trajectory 级别的 stagnation；n-gram 是我们 LFs 之一\\\"\\n\\n  - id: \\\"huang2024selfcorrect\\\"\\n    title: \\\"Large Language Models Cannot Self-Correct Reasoning Yet\\\"\\n    authors: \\\"Jie Huang, Xinyun Chen, Swaroop Mishra, Huaixiu Steven Zheng, Adams Wei Yu, Xinying Song, Denny Zhou\\\"\\n    venue: \\\"ICLR 2024\\\"\\n    year: 2024\\n    arxiv: \\\"2310.01798\\\"\\n    category: \\\"background\\\"\\n    verified: true\\n    role: \\\"Self-correction 失败的关键证据——支持 external monitoring 必要性\\\"\\n    key_finding: \\\"LLM 在无外部反馈时无法自我纠错推理错误，intrinsic self-correction 甚至导致性能下降\\\"\\n    our_differentiation: \\\"直接支持我们的核心论点：agent 不能可靠地自我检测 stagnation，需要外部 monitor；我们的 structural features 提供了轻量（<5ms）且高精度（0.995 F1）的外部检测方案\\\"\\n\\n  - id: \\\"kamoi2024selfcorrection\\\"\\n    title: \\\"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs\\\"\\n    authors: \\\"Ryo Kamoi, Yusen Zhang, Nan Zhang, Jiawei Han, Rui Zhang\\\"\\n    venue: \\\"TACL 2024\\\"\\n    year: 2024\\n    arxiv: \\\"2406.01297\\\"\\n    category: \\\"background\\\"\\n    verified: true\\n    role: \\\"Self-correction 条件的系统性综述——外部反馈是成功的必要条件\\\"\\n    key_finding: \\\"无外部反馈的 prompted self-correction 均未成功；self-correction 仅在有可靠外部反馈或大规模微调时有效\\\"\\n    our_differentiation: \\\"综述证实 self-correction 需要外部信号，我们的 empirical analysis 表明 structural features 即可提供高精度外部 stagnation 信号，无需复杂的语义理解\\\"\\n\\n  - id: \\\"liu2026trajad\\\"\\n    title: \\\"TrajAD: Trajectory Anomaly Detection for Trustworthy LLM Agents\\\"\\n    authors: \\\"Yibing Liu, Chong Zhang, Zhongyi Han, Hansong Liu, Yong Wang, Yang Yu, Xiaoyan Wang, Yilong Yin\\\"\\n    venue: \\\"arXiv preprint\\\"\\n    year: 2026\\n    arxiv: \\\"2602.06443\\\"\\n    category: \\\"background\\\"\\n    verified: true\\n    role: \\\"Agent trajectory 异常检测——stagnation detection 的直接前驱\\\"\\n    key_finding: \\\"TrajAD 通过 fine-grained process supervision 训练 verifier 检测 agent trajectory 中的异常（task failure, process inefficiency, unwarranted continuation），通用 LLM zero-shot 表现差\\\"\\n    our_differentiation: \\\"TrajAD 需要训练专用 verifier + 合成数据（perturb-and-complete），我们用 30 个 structural features 无需训练即达 0.995 F1；他们覆盖多种异常类型，我们专注 stagnation pattern 的深度分析\\\"\\n\\n  # ============================================================\\n  # CATEGORY: technique\\n  # ============================================================\\n\\n  - id: \\\"cho2014gru\\\"\\n    title: \\\"Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation\\\"\\n    authors: \\\"Kyunghyun Cho, Bart van Merrienboer, Caglar Gulcehre, Dzmitry Bahdanau, Fethi Bougares, Holger Schwenk, Yoshua Bengio\\\"\\n    venue: \\\"EMNLP 2014\\\"\\n    year: 2014\\n    arxiv: \\\"1406.1078\\\"\\n    category: \\\"technique\\\"\\n    role: \\\"GRU 原始论文——我们 probe model 的序列编码器\\\"\\n    key_finding: \\\"提出 GRU hidden unit，自适应门控信息流\\\"\\n\\n  - id: \\\"bahdanau2015attention\\\"\\n    title: \\\"Neural Machine Translation by Jointly Learning to Align and Translate\\\"\\n    authors: \\\"Dzmitry Bahdanau, Kyunghyun Cho, Yoshua Bengio\\\"\\n    venue: \\\"ICLR 2015\\\"\\n    year: 2015\\n    arxiv: \\\"1409.0473\\\"\\n    category: \\\"technique\\\"\\n    role: \\\"Attention mechanism——我们 probe model 的 attention 组件\\\"\\n    key_finding: \\\"注意力机制允许 decoder 选择性关注输入序列不同位置\\\"\\n\\n  - id: \\\"khosla2020supcon\\\"\\n    title: \\\"Supervised Contrastive Learning\\\"\\n    authors: \\\"Prannay Khosla, Piotr Teterwak, Chen Wang, Aaron Sarna, Yonglong Tian, Phillip Isola, Aaron Maschinot, Ce Liu, Dilip Krishnan\\\"\\n    venue: \\\"NeurIPS 2020\\\"\\n    year: 2020\\n    arxiv: \\\"2004.11362\\\"\\n    category: \\\"technique\\\"\\n    role: \\\"SupCon loss——我们的辅助训练目标\\\"\\n    key_finding: \\\"扩展自监督对比学习到有监督设置，同类样本拉近、异类推远，提升鲁棒性\\\"\\n\\n  - id: \\\"zhang2025qwen3embedding\\\"\\n    title: \\\"Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models\\\"\\n    authors: \\\"Yanzhao Zhang, Mingxin Li, Dingkun Long, Xin Zhang, Huan Lin, Baosong Yang, Pengjun Xie, An Yang, Dayiheng Liu, Junyang Lin, Fei Huang, Jingren Zhou\\\"\\n    venue: \\\"arXiv preprint\\\"\\n    year: 2025\\n    arxiv: \\\"2506.05176\\\"\\n    category: \\\"technique\\\"\\n    role: \\\"Embedding model——我们用于生成 trajectory window embeddings\\\"\\n    key_finding: \\\"基于 Qwen3 的 embedding 模型（0.6B/4B/8B），多阶段训练，MTEB 多语言 SOTA\\\"\\n\\n  - id: \\\"wang2024e5\\\"\\n    title: \\\"Multilingual E5 Text Embeddings: A Technical Report\\\"\\n    authors: \\\"Liang Wang, Nan Yang, Xiaolong Huang, Linjun Yang, Rangan Majumder, Furu Wei\\\"\\n    venue: \\\"arXiv preprint\\\"\\n    year: 2024\\n    arxiv: \\\"2402.05672\\\"\\n    category: \\\"technique\\\"\\n    verified: true\\n    role: \\\"Encoder ablation 中使用的 embedding model\\\"\\n    key_finding: \\\"基于 XLM-R 的多语言 text embedding，混合多语言数据训练，跨语言检索和语义相似度任务上性能强劲\\\"\\n\\n  - id: \\\"chen2024bgem3\\\"\\n    title: \\\"BGE M3-Embedding: Multi-Linguality, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation\\\"\\n    authors: \\\"Jianlv Chen, Shitao Xiao, Peitian Zhang, Kun Luo, Defu Lian, Zheng Liu\\\"\\n    venue: \\\"arXiv preprint\\\"\\n    year: 2024\\n    arxiv: \\\"2402.03216\\\"\\n    category: \\\"technique\\\"\\n    verified: true\\n    role: \\\"Encoder ablation 中使用的 embedding model\\\"\\n    key_finding: \\\"统一 dense/sparse/multi-vec 三种检索功能于单一模型，通过 self-knowledge distillation 训练，支持 8192 token 长文本和 100+ 语言\\\"\\n\\n# ============================================================\\n# NOVELTY ANALYSIS SUMMARY (D039 Pivot — Empirical Analysis)\\n# ============================================================\\n#\\n# Primary novelty: 首次系统性实证分析 agent stagnation 检测中 structural vs\\n# semantic signal 的有效性。30 个结构特征达 0.995 in-domain / 0.967 cross-agent F1，\\n# 全面优于 NL embedding (0.906/0.751) 和 LLM-as-judge (+24.3pp)。\\n#\\n# 三层贡献：\\n# 1. Structural Signal Discovery (primary) — 改变社区对 agent monitoring 方法选型认知\\n# 2. LF Temporal Dynamics Analysis — 量化 LFs 时序角色 + agent-specific 迁移分析\\n# 3. TLM Negative Finding — 3 种实现 (TWV/HMM/lag-aware HMM) 均未超越 MV\\n#\\n# 方法论前驱（TLM negative finding 的参照）：\\n# 1. Safranchik AAAI 2020 (linked HMM) — NER-specific，BIO 约束，token-level\\n# 2. Sala NeurIPS 2019 (multi-resolution WS) — 处理分辨率不匹配，不建模 label transition\\n# 3. Nguyen ACL 2017 (HMM-Crowd) — crowdsourcing 场景，不是 programmatic LFs\\n#\\n# 核心差异化：不是 \\\"method paper proposing TLM\\\"，而是 \\\"empirical study revealing\\n# structural signals dominate stagnation detection, with temporal modeling as\\n# well-motivated negative finding\\\".\\n\", \"total_chars\": 23431, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1311e2e5-9af4-44d3-8961-4a2f79dde730",
  "uuid": "374a393c-af50-482a-ae82-40b7ff490089",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/literature_map.yaml\\\", \\\"content\\\": \\\"# Literature Map for Agent Progress Probe (EMNLP 2026 ARR)\\\\n# Generated: 2026-05-14\\\\n# Paper: Structural Signal Analysis for Progress Stagnation Detection in LLM Agents\\\\n#\\\\n# D039 Pivot: Empirical analysis paper. Central finding: stagnation signals are\\\\n# fundamentally structural (30 features → 0.995 in-domain, 0.967 cross-agent F1),\\\\n# decisively surpassing NL embeddings (0.906/0.751) and LLM-as-judge (+24.3pp).\\\\n# TLM is a well-motivated negative finding (3 implementations all fail to beat MV).\\\\n\\\\npapers:\\\\n\\\\n  # ============================================================\\\\n  # CATEGORY: direct-competitor\\\\n  # ============================================================\\\\n\\\\n  - id: \\\\\\\"xi2025agentprm\\\\\\\"\\\\n    title: \\\\\\\"AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress\\\\\\\"\\\\n    authors: \\\\\\\"Zhiheng Xi, Chenyang Liao, Guanyu Li, Yajie Yang, Wenxiang Chen, Zhihao Zhang, Binghai Wang, Senjie Jin, Yuhao Zhou, Jian Guan, Wei Wu, Tao Ji, Tao Gui, Qi Zhang, Xuanjing Huang\\\\\\\"\\\\n    venue: \\\\\\\"arXiv preprint\\\\\\\"\\\\n    year: 2025\\\\n    arxiv: \\\\\\\"2511.08325\\\\\\\"\\\\n    category: \\\\\\\"direct-competitor\\\\\\\"\\\\n    role: \\\\\\\"主要竞争者：step-level PRM for agent guidance\\\\\\\"\\\\n    key_finding: \\\\\\\"用 promise（长期潜力）和 progress（即时进展）两个维度评估 agent 每步决策，实现 8x 计算效率提升\\\\\\\"\\\\n    our_differentiation: \\\\\\\"我们是 window-level monitoring（不是 step-level guidance），不需要 outcome labels，目标是 stagnation detection 不是 reward shaping\\\\\\\"\\\\n\\\\n  - id: \\\\\\\"choudhury2025prm\\\\\\\"\\\\n    title: \\\\\\\"Process Reward Models for LLM Agents: Practical Framework and Directions\\\\\\\"\\\\n    authors: \\\\\\\"Sanjiban Choudhury\\\\\\\"\\\\n    venue: \\\\\\\"arXiv preprint\\\\\\\"\\\\n    year: 2025\\\\n    arxiv: \\\\\\\"2502.10325\\\\\\\"\\\\n    category: \\\\\\\"direct-competitor\\\\\\\"\\\\n    role: \\\\\\\"PRM 框架综述 + InversePRM 方法\\\\\\\"\\\\n    key_finding: \\\\\\\"提出 AgentPRM（Monte Carlo rollout actor-critic）和 InversePRM（从 demonstrations 学习 process reward），3B 模型超越 GPT-4o\\\\\\\"\\\\n    our_differentiation: \\\\\\\"InversePRM 仍需 demonstration trajectories，我们用 programmatic LFs 替代人工标注；我们关注 monitoring 而非 training signal\\\\\\\"\\\\n\\\\n  - id: \\\\\\\"li2026toolprmbench\\\\\\\"\\\\n    title: \\\\\\\"ToolPRMBench: Evaluating and Advancing Process Reward Models for Tool-using Agents\\\\\\\"\\\\n    authors: \\\\\\\"Dawei Li, Yuguang Yao, Zhen Tan, Huan Liu, Ruocheng Guo\\\\\\\"\\\\n    venue: \\\\\\\"arXiv preprint\\\\\\\"\\\\n    year: 2026\\\\n    arxiv: \\\\\\\"2601.12294\\\\\\\"\\\\n    category: \\\\\\\"direct-competitor\\\\\\\"\\\\n    role: \\\\\\\"Tool-use PRM 评测基准\\\\\\\"\\\\n    key_finding: \\\\\\\"大规模 benchmark 评测 PRM 在 tool-use 场景的效果，发现专用 PRM 显著优于通用 PRM\\\\\\\"\\\\n    our_differentiation: \\\\\\\"我们的 empirical analysis 揭示 structural features 足以检测 stagnation（0.995 F1），无需 step-level reward labels；关注 stagnation pattern 而非 step correctness\\\\\\\"\\\\n\\\\n  - id: \\\\\\\"wang2026planrewardbench\\\\\\\"\\\\n    title: \\\\\\\"Aligning Agents via Planning: A Benchmark for Trajectory-Level Reward Modeling\\\\\\\"\\\\n    authors: \\\\\\\"Jiaxuan Wang, Yulan Hu, Wenjin Yang, Zheng Pan, Xin Li, Lan-Zhe Guo\\\\\\\"\\\\n    venue: \\\\\\\"arXiv preprint\\\\\\\"\\\\n    year: 2026\\\\n    arxiv: \\\\\\\"2604.08178\\\\\\\"\\\\n    category: \\\\\\\"direct-competitor\\\\\\\"\\\\n    role: \\\\\\\"Trajectory-level reward model 评测\\\\\\\"\\\\n    key_finding: \\\\\\\"所有 reward model 类别（generative, discriminative, LLM-as-Judge）在长 horizon trajectory 上性能显著下降\\\\\\\"\\\\n    our_differentiation: \\\\\\\"验证了长 trajectory 评估的难度——我们的 window-level 方法通过局部化避免了这个问题\\\\\\\"\\\\n\\\\n  - id: \\\\\\\"chen2025monitoring\\\\\\\"\\\\n    title: \\\\\\\"Monitoring LLM Agents for Sequentially Contextual Harm\\\\\\\"\\\\n    authors: \\\\\\\"Yueh-Han Chen, Neelay Joshi, Yulin Chen, He He, Rico Angell\\\\\\\"\\\\n    venue: \\\\\\\"ICLR 2025 Workshop on Building Trust in Language Models and Applications\\\\\\\"\\\\n    year: 2025\\\\n    arxiv: null\\\\n    openreview: \\\\\\\"LC0XQ6ufbr\\\\\\\"\\\\n    category: \\\\\\\"direct-competitor\\\\\\\"\\\\n    role: \\\\\\\"Agent monitoring 安全方向\\\\\\\"\\\\n    key_finding: \\\\\\\"将有害任务分解为单独无害的子任务可将 refusal rate 从 50% 降至 10%，现有 monitor 难以检测 sequentially contextual harm\\\\\\\"\\\\n    our_differentiation: \\\\\\\"他们关注 safety monitoring（harmful behavior），我们关注 progress monitoring（stagnation）；互补方向\\\\\\\"\\\\n\\\\n  - id: \\\\\\\"kale2025weaktostrong\\\\\\\"\\\\n    title: \\\\\\\"Reliable Weak-to-Strong Monitoring of LLM Agents\\\\\\\"\\\\n    authors: \\\\\\\"Neil Kale, Chen Bo Calvin Zhang, Kevin Zhu, Ankit Aich, Paula Rodriguez, Scale Red Team, Christina Q. Knight, Zifan Wang\\\\\\\"\\\\n    venue: \\\\\\\"arXiv preprint\\\\\\\"\\\\n    year: 2025\\\\n    arxiv: \\\\\\\"2508.19461\\\\\\\"\\\\n    category: \\\\\\\"direct-competitor\\\\\\\"\\\\n    role: \\\\\\\"Weak-to-strong agent monitoring 方法论\\\\\\\"\\\\n    key_finding: \\\\\\\"Monitor scaffolding 比 monitor 能力更重要，弱模型可以可靠监控强模型；targeted human-in-the-loop 提升 TPR ~15%\\\\\\\"\\\\n    our_differentiation: \\\\\\\"他们用 LLM 作为 monitor，我们发现 30 个 structural features 即可达 0.967 跨域 F1，不依赖另一个 LLM；更轻量（<5ms）且可解释\\\\\\\"\\\\n\\\\n  - id: \\\\\\\"fan2026agentrm\\\\\\\"\\\\n    title: \\\\\\\"Exploring Reasoning Reward Model for Agents\\\\\\\"\\\\n    authors: \\\\\\\"Kaixuan Fan, Kaituo Feng, Manyuan Zhang, Tianshuo Peng, Zhixun Li, Yilei Jiang, Shuang Chen, Peng Pei, Xunliang Cai, Xiangyu Yue\\\\\\\"\\\\n    venue: \\\\\\\"arXiv preprint\\\\\\\"\\\\n    year: 2026\\\\n    arxiv: \\\\\\\"2601.22154\\\\\\\"\\\\n    category: \\\\\\\"direct-competitor\\\\\\\"\\\\n    verified: true\\\\n    role: \\\\\\\"Agent trajectory 的多维度 reasoning reward model\\\\\\\"\\\\n    key_finding: \\\\\\\"Agent-RRM 通过 reasoning trace + critique + overall score 三维结构化反馈评估 agent trajectory，在 12 个 benchmark 上显著提升（GAIA 43.7%, WebWalkerQA 46.2%）\\\\\\\"\\\\n    our_differentiation: \\\\\\\"他们用 LLM-based reward model 生成结构化反馈用于 agent 改进，我们的 empirical analysis 表明轻量 structural features 即可高精度检测 stagnation（0.995 F1），不依赖大模型推理\\\\\\\"\\\\n\\\\n  - id: \\\\\\\"qiu2026dataprm\\\\\\\"\\\\n    title: \\\\\\\"Rewarding the Scientific Process: Process-Level Reward Modeling for Agentic Data Analysis\\\\\\\"\\\\n    authors: \\\\\\\"Zhisong Qiu, Shuofei Qiao, Kewei Xu, Yuqi Zhu, Lun Du, Ningyu Zhang, Huajun Chen\\\\\\\"\\\\n    venue: \\\\\\\"arXiv preprint\\\\\\\"\\\\n    year: 2026\\\\n    arxiv: \\\\\\\"2604.24198\\\\\\\"\\\\n    category: \\\\\\\"direct-competitor\\\\\\\"\\\\n    verified: true\\\\n    role: \\\\\\\"Agentic data analysis 场景的 process-level reward model\\\\\\\"\\\\n    key_finding: \\\\\\\"传统 PRM 无法检测 silent errors 且误判 exploratory steps；DataPRM 通过 environment-aware probing + ternary reward 策略在 ScienceAgentBench 提升 7.21%\\\\\\\"\\\\n    our_differentiation: \\\\\\\"DataPRM 针对数据分析 agent 的 step correctness，我们针对通用 agent 的 stagnation pattern；他们需要 execution state probing，我们用 structural LFs 无需环境交互\\\\\\\"\\\\n\\\\n  # ============================================================\\\\n  # CATEGORY: method-component\\\\n  # ============================================================\\\\n\\\\n  - id: \\\\\\\"ratner2016dataprogramming\\\\\\\"\\\\n    title: \\\\\\\"Data Programming: Creating Large Training Sets, Quickly\\\\\\\"\\\\n    authors: \\\\\\\"Alexander Ratner, Christopher De Sa, Sen Wu, Daniel Selsam, Christopher Re\\\\\\\"\\\\n    venue: \\\\\\\"NeurIPS 2016\\\\\\\"\\\\n    year: 2016\\\\n    arxiv: \\\\\\\"1605.07723\\\\\\\"\\\\n    category: \\\\\\\"method-component\\\\\\\"\\\\n    role: \\\\\\\"核心方法论基础：data programming 范式\\\\\\\"\\\\n    key_finding: \\\\\\\"用户编写 labeling functions（噪声启发式），generative model 学习 LF 准确率生成概率训练标签\\\\\\\"\\\\n    our_differentiation: \\\\\\\"我们在 agent trajectory 上应用 data programming，发现 structural features 主导检测能力；同时揭示 LFs 的时序动态和 temporal label model 的负面结果\\\\\\\"\\\\n\\\\n  - id: \\\\\\\"ratner2017snorkel\\\\\\\"\\\\n    title: \\\\\\\"Snorkel: Rapid Training Data Creation with Weak Supervision\\\\\\\"\\\\n    authors: \\\\\\\"Alexander Ratner, Stephen H. Bach, Henry Ehrenberg, Jason Fries, Sen Wu, Christopher Re\\\\\\\"\\\\n    venue: \\\\\\\"VLDB 2018\\\\\\\"\\\\n    year: 2018\\\\n    arxiv: \\\\\\\"1711.10160\\\\\\\"\\\\n    category: \\\\\\\"method-component\\\\\\\"\\\\n    role: \\\\\\\"Data programming 系统实现，label model 基础\\\\\\\"\\\\n    key_finding: \\\\\\\"端到端弱监督系统：LFs → generative label model（建模 LF dependency）→ discriminative end model\\\\\\\"\\\\n    our_differentiation: \\\\\\\"Snorkel 假设数据点 i.i.d.，我们发现 agent trajectory 上 LFs 展现系统性时序动态（violating i.i.d.），但 temporal label model 未能超越 MV（negative finding）\\\\\\\"\\\\n\\\\n  - id: \\\\\\\"fu2020flyingsquid\\\\\\\"\\\\n    title: \\\\\\\"Fast and Three-rious: Speeding Up Weak Supervision with Triplet Methods\\\\\\\"\\\\n    authors: \\\\\\\"Daniel Y. Fu, Mayee F. Chen, Frederic Sala, Sarah M. Hooper, Kayvon Fatahalian, Christopher Re\\\\\\\"\\\\n    venue: \\\\\\\"ICML 2020\\\\\\\"\\\\n    year: 2020\\\\n    arxiv: \\\\\\\"2002.11955\\\\\\\"\\\\n    category: \\\\\\\"method-component\\\\\\\"\\\\n    role: \\\\\\\"快速 label model，triplet method of moments\\\\\\\"\\\\n    key_finding: \\\\\\\"用 triplet method 闭式求解 label model 参数，比 SGD 快 170x\\\\\\\"\\\\n    our_differentiation: \\\\\\\"FlyingSquid 同样假设 i.i.d.；我们的 empirical analysis 揭示 i.i.d. violation 虽系统性存在，但 temporal correction 在低冲突 regime 下无收益（negative finding）\\\\\\\"\\\\n\\\\n  - id: \\\\\\\"zhang2021wrench\\\\\\\"\\\\n    title: \\\\\\\"WRENCH: A Comprehensive Benchmark for Weak Supervision\\\\\\\"\\\\n    authors: \\\\\\\"Jieyu Zhang, Yue Yu, Yinghao Li, Yujing Wang, Yaming Yang, Mao Yang, Alexander Ratner\\\\\\\"\\\\n    venue: \\\\\\\"NeurIPS 2021 Datasets and Benchmarks Track\\\\\\\"\\\\n    year: 2021\\\\n    arxiv: \\\\\\\"2109.11377\\\\\\\"\\\\n    category: \\\\\\\"method-component\\\\\\\"\\\\n    role: \\\\\\\"弱监督评测基准\\\\\\\"\\\\n    key_finding: \\\\\\\"22 个真实数据集 + 120+ 方法变体评测，标准化弱监督研究\\\\\\\"\\\\n    our_differentiation: \\\\\\\"WRENCH 数据集全是 i.i.d. 分类/序列标注，没有 temporal stagnation detection 任务\\\\\\\"\\\\n\\\\n  - id: \\\\\\\"safranchik2020linkedhmm\\\\\\\"\\\\n    title: \\\\\\\"Weakly Supervised Sequence Tagging from Noisy Rules\\\\\\\"\\\\n    authors: \\\\\\\"Esteban Safranchik, Shiying Luo, Stephen H. Bach\\\\\\\"\\\\n    venue: \\\\\\\"AAAI 2020\\\\\\\"\\\\n    year: 2020\\\\n    arxiv: null\\\\n    category: \\\\\\\"method-component\\\\\\\"\\\\n    role: \\\\\\\"最近的方法论前驱：linked HMM for sequence tagging weak supervision\\\\\\\"\\\\n    key_finding: \\\\\\\"将 HMM 引入弱监督序列标注（NER），加入 linking rules 建模 span 结构，比 i.i.d. label model +7 F1\\\\\\\"\\\\n    our_differentiation: \\\\\\\"他们是 token-level NER（BIO 约束），我们是 window-level temporal classification；我们建模的是 stagnation temporal dynamics 而非 entity boundary\\\\\\\"\\\\n\\\\n  - id: \\\\\\\"sala2019multiresolution\\\\\\\"\\\\n    title: \\\\\\\"Multi-Resolution Weak Supervision for Sequential Data\\\\\\\"\\\\n    authors: \\\\\\\"Frederic Sala, Paroma Varma, Jason Fries, Daniel Y. Fu, Stefano Sagawa, Christopher Re\\\\\\\"\\\\n    venue: \\\\\\\"NeurIPS 2019\\\\\\\"\\\\n    year: 2019\\\\n    arxiv: \\\\\\\"1910.09505\\\\\\\"\\\\n    category: \\\\\\\"method-component\\\\\\\"\\\\n    role: \\\\\\\"最近的方法论前驱：multi-resolution WS for sequential data\\\\\\\"\\\\n    key_finding: \\\\\\\"处理不同时间分辨率的 LFs（如 frame-level vs span-level），建模 multi-resolution LF correlations\\\\\\\"\\\\n    our_differentiation: \\\\\\\"他们关注 resolution mismatch，我们关注 temporal label transitions；互补视角\\\\\\\"\\\\n\\\\n  - id: \\\\\\\"dawid1979em\\\\\\\"\\\\n    title: \\\\\\\"Maximum Likelihood Estimation of Observer Error-Rates Using the EM Algorithm\\\\\\\"\\\\n    authors: \\\\\\\"A. P. Dawid, A. M. Skene\\\\\\\"\\\\n    venue: \\\\\\\"Journal of the Royal Statistical Society, Series C\\\\\\\"\\\\n    year: 1979\\\\n    arxiv: null\\\\n    category: \\\\\\\"method-component\\\\\\\"\\\\n    role: \\\\\\\"Label aggregation 奠基工作\\\\\\\"\\\\n    key_finding: \\\\\\\"用 EM 算法估计标注者混淆矩阵，无需 ground truth\\\\\\\"\\\\n    our_differentiation: \\\\\\\"经典 i.i.d. 假设；我们测试了 temporal extension（HMM-TLM, lag-aware HMM）但发现在 3-LF 低冲突 regime 下未超越 MV——约束未来 temporal label model 研究\\\\\\\"\\\\n\\\\n  - id: \\\\\\\"nguyen2017hmmcrowd\\\\\\\"\\\\n    title: \\\\\\\"Aggregating and Predicting Sequence Labels from Crowd Annotations\\\\\\\"\\\\n    authors: \\\\\\\"An Thanh Nguyen, Byron C. Wallace, Junyi Jessy Li, Ani Nenkova, Matthew Lease\\\\\\\"\\\\n    venue: \\\\\\\"ACL 2017\\\\\\\"\\\\n    year: 2017\\\\n    arxiv: null\\\\n    category: \\\\\\\"method-component\\\\\\\"\\\\n    role: \\\\\\\"HMM + crowdsourcing label aggregation\\\\\\\"\\\\n    key_finding: \\\\\\\"HMM-Crowd：扩展 Dawid-Skene 到序列数据，加入 one-step Markov structure over true labels\\\\\\\"\\\\n    our_differentiation: \\\\\\\"他们用于 crowdsourcing（人类标注者），我们用于 programmatic LFs（自动化）；他们是 NER/IE，我们是 agent progress monitoring\\\\\\\"\\\\n\\\\n  # ============================================================\\\\n  # CATEGORY: evaluation\\\\n  # ============================================================\\\\n\\\\n  - id: \\\\\\\"orlanski2026slopcodebench\\\\\\\"\\\\n    title: \\\\\\\"SlopCodeBench: Benchmarking How Coding Agents Degrade Over Long-Horizon Iterative Tasks\\\\\\\"\\\\n    authors: \\\\\\\"Gabriel Orlanski, Devjeet Roy, Alexander Yun, Changho Shin, Alex Gu, Albert Ge, Dyah Adila, Nicholas Roberts, Frederic Sala, Aws Albarghouthi\\\\\\\"\\\\n    venue: \\\\\\\"arXiv preprint\\\\\\\"\\\\n    year: 2026\\\\n    arxiv: \\\\\\\"2603.24755\\\\\\\"\\\\n    category: \\\\\\\"evaluation\\\\\\\"\\\\n    role: \\\\\\\"Agent degradation 基准——直接支持我们的 problem motivation\\\\\\\"\\\\n    key_finding: \\\\\\\"Agent 代码质量在迭代任务中持续退化：比人类代码 2.3x 更冗余、2.0x 更结构侵蚀，75-77% trajectory 呈现退化趋势\\\\\\\"\\\\n    our_differentiation: \\\\\\\"SlopCodeBench 量化了 degradation 现象，我们提供了检测方法；他们是 post-hoc 评测，我们是 online monitoring\\\\\\\"\\\\n\\\\n  - id: \\\\\\\"jimenez2024swebench\\\\\\\"\\\\n    title: \\\\\\\"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?\\\\\\\"\\\\n    authors: \\\\\\\"Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan\\\\\\\"\\\\n    venue: \\\\\\\"ICLR 2024\\\\\\\"\\\\n    year: 2024\\\\n    arxiv: \\\\\\\"2310.06770\\\\\\\"\\\\n    category: \\\\\\\"evaluation\\\\\\\"\\\\n    role: \\\\\\\"Agent 数据来源之一\\\\\\\"\\\\n    key_finding: \\\\\\\"2294 个真实 GitHub issue 任务，标准化 agent 评测\\\\\\\"\\\\n    our_differentiation: \\\\\\\"我们使用 SWE-bench agent trajectories 作为实验数据源之一\\\\\\\"\\\\n\\\\n  - id: \\\\\\\"yang2024sweagent\\\\\\\"\\\\n    title: \\\\\\\"SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering\\\\\\\"\\\\n    authors: \\\\\\\"John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press\\\\\\\"\\\\n    venue: \\\\\\\"NeurIPS 2024\\\\\\\"\\\\n    year: 2024\\\\n    arxiv: \\\\\\\"2405.15793\\\\\\\"\\\\n    category: \\\\\\\"evaluation\\\\\\\"\\\\n    role: \\\\\\\"Agent 系统——trajectory 数据来源\\\\\\\"\\\\n    key_finding: \\\\\\\"提出 agent-computer interface (ACI)，GPT-4 Turbo 在 SWE-bench 达 12.47% resolve rate\\\\\\\"\\\\n    our_differentiation: \\\\\\\"SWE-agent trajectories 是我们分析 stagnation 的数据来源之一\\\\\\\"\\\\n\\\\n  - id: \\\\\\\"wang2025openhands\\\\\\\"\\\\n    title: \\\\\\\"OpenHands: An Open Platform for AI Software Developers as Generalist Agents\\\\\\\"\\\\n    authors: \\\\\\\"Xingyao Wang, Boxuan Li, Yufan Song, Frank F. Xu, Xiangru Tang, et al.\\\\\\\"\\\\n    venue: \\\\\\\"ICLR 2025\\\\\\\"\\\\n    year: 2025\\\\n    arxiv: \\\\\\\"2407.16741\\\\\\\"\\\\n    category: \\\\\\\"evaluation\\\\\\\"\\\\n    role: \\\\\\\"Agent 平台——主要数据来源\\\\\\\"\\\\n    key_finding: \\\\\\\"开源 agent 平台，sandbox 执行环境，15+ benchmarks 评测\\\\\\\"\\\\n    our_differentiation: \\\\\\\"OpenHands trajectories 是我们的主要实验数据来源\\\\\\\"\\\\n\\\\n  - id: \\\\\\\"zhou2024webarena\\\\\\\"\\\\n    title: \\\\\\\"WebArena: A Realistic Web Environment for Building Autonomous Agents\\\\\\\"\\\\n    authors: \\\\\\\"Shuyan Zhou, Frank F. Xu, Hao Zhu, Xuhui Zhou, Robert Lo, Abishek Sridhar, Xianyi Cheng, Tianyue Ou, Yonatan Bisk, Daniel Fried, Uri Alon, Graham Neubig\\\\\\\"\\\\n    venue: \\\\\\\"ICLR 2024\\\\\\\"\\\\n    year: 2024\\\\n    arxiv: \\\\\\\"2307.13854\\\\\\\"\\\\n    category: \\\\\\\"evaluation\\\\\\\"\\\\n    verified: true\\\\n    role: \\\\\\\"Web agent 评测基准——long-horizon 任务评估\\\\\\\"\\\\n    key_finding: \\\\\\\"812 个真实网站上的 long-horizon 任务，GPT-4 agent 仅 14.41% 成功率 vs 人类 78.24%，揭示 agent 在复杂任务上的巨大差距\\\\\\\"\\\\n    our_differentiation: \\\\\\\"WebArena 的 long-horizon 任务正是 stagnation 高发场景；我们的 monitor 可作为此类任务的早期终止/干预信号\\\\\\\"\\\\n\\\\n  - id: \\\\\\\"wang2024mint\\\\\\\"\\\\n    title: \\\\\\\"MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback\\\\\\\"\\\\n    authors: \\\\\\\"Xingyao Wang, Zihan Wang, Jiateng Liu, Yangyi Chen, Lifan Yuan, Hao Peng, Heng Ji\\\\\\\"\\\\n    venue: \\\\\\\"ICLR 2024\\\\\\\"\\\\n    year: 2024\\\\n    arxiv: \\\\\\\"2309.10691\\\\\\\"\\\\n    category: \\\\\\\"evaluation\\\\\\\"\\\\n    verified: true\\\\n    role: \\\\\\\"Multi-turn agent 评测基准——tool use + feedback 交互评估\\\\\\\"\\\\n    key_finding: \\\\\\\"评估 LLM 在多轮交互中使用工具和接收自然语言反馈的能力，每轮 tool use 提升 1-8%，NL feedback 提升 2-17%\\\\\\\"\\\\n    our_differentiation: \\\\\\\"MINT 量化了 multi-turn 交互中的性能变化，我们的 stagnation detection 关注多轮交互中进展停滞的检测；MINT 的 multi-turn 设定与我们的 window-level 分析天然对齐\\\\\\\"\\\\n\\\\n  # ============================================================\\\\n  # CATEGORY: background\\\\n  # ============================================================\\\\n\\\\n  - id: \\\\\\\"shinn2023reflexion\\\\\\\"\\\\n    title: \\\\\\\"Reflexion: Language Agents with Verbal Reinforcement Learning\\\\\\\"\\\\n    authors: \\\\\\\"Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao\\\\\\\"\\\\n    venue: \\\\\\\"NeurIPS 2023\\\\\\\"\\\\n    year: 2023\\\\n    arxiv: \\\\\\\"2303.11366\\\\\\\"\\\\n    category: \\\\\\\"background\\\\\\\"\\\\n    role: \\\\\\\"Agent self-reflection 代表工作\\\\\\\"\\\\n    key_finding: \\\\\\\"通过 verbal feedback 强化 agent，反思文本存入 episodic memory 用于后续 trial\\\\\\\"\\\\n    our_differentiation: \\\\\\\"Reflexion 是 agent 自我改进机制，我们是外部 monitoring；self-reflection 可能失效时我们的 monitor 仍能检测 stagnation\\\\\\\"\\\\n\\\\n  - id: \\\\\\\"zhou2024lats\\\\\\\"\\\\n    title: \\\\\\\"Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models\\\\\\\"\\\\n    authors: \\\\\\\"Andy Zhou, Kai Yan, Michal Shlapentokh-Rothman, Haohan Wang, Yu-Xiong Wang\\\\\\\"\\\\n    venue: \\\\\\\"ICML 2024\\\\\\\"\\\\n    year: 2024\\\\n    arxiv: \\\\\\\"2310.04406\\\\\\\"\\\\n    category: \\\\\\\"background\\\\\\\"\\\\n    role: \\\\\\\"Agent planning + self-reflection\\\\\\\"\\\\n    key_finding: \\\\\\\"结合 MCTS 与 LM value function 和 self-reflection，支持 backtracking\\\\\\\"\\\\n    our_differentiation: \\\\\\\"LATS 通过搜索避免 stagnation，但计算开销大；我们的 monitor 可作为 LATS 的早期终止信号\\\\\\\"\\\\n\\\\n  - id: \\\\\\\"yao2023tot\\\\\\\"\\\\n    title: \\\\\\\"Tree of Thoughts: Deliberate Problem Solving with Large Language Models\\\\\\\"\\\\n    authors: \\\\\\\"Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Thomas L. Griffiths, Yuan Cao, Karthik Narasimhan\\\\\\\"\\\\n    venue: \\\\\\\"NeurIPS 2023\\\\\\\"\\\\n    year: 2023\\\\n    arxiv: \\\\\\\"2305.10601\\\\\\\"\\\\n    category: \\\\\\\"background\\\\\\\"\\\\n    role: \\\\\\\"Deliberate reasoning 框架\\\\\\\"\\\\n    key_finding: \\\\\\\"将 CoT 泛化为树结构，LM 自我评估中间 thought 并 backtrack\\\\\\\"\\\\n    our_differentiation: \\\\\\\"ToT 的自评估是 single-step 的；我们捕捉 multi-step temporal patterns\\\\\\\"\\\\n\\\\n  - id: \\\\\\\"cemri2025multiagentfail\\\\\\\"\\\\n    title: \\\\\\\"Why Do Multi-Agent LLM Systems Fail?\\\\\\\"\\\\n    authors: \\\\\\\"Mert Cemri, Melissa Z. Pan, Shuyi Yang, Lakshya A. Agrawal, et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv preprint\\\\\\\"\\\\n    year: 2025\\\\n    arxiv: \\\\\\\"2503.13657\\\\\\\"\\\\n    category: \\\\\\\"background\\\\\\\"\\\\n    role: \\\\\\\"Agent failure taxonomy——problem motivation\\\\\\\"\\\\n    key_finding: \\\\\\\"MAST taxonomy：14 种失败模式，其中 Step Repetition 被识别为具体失败症状\\\\\\\"\\\\n    our_differentiation: \\\\\\\"他们提供 taxonomy（what fails），我们提供 detection method（how to detect）\\\\\\\"\\\\n\\\\n  - id: \\\\\\\"zhu2025agentfail\\\\\\\"\\\\n    title: \\\\\\\"Where LLM Agents Fail and How They Can Learn From Failures\\\\\\\"\\\\n    authors: \\\\\\\"Kunlun Zhu, Zijia Liu, Bingxuan Li, et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv preprint\\\\\\\"\\\\n    year: 2025\\\\n    arxiv: \\\\\\\"2509.25370\\\\\\\"\\\\n    category: \\\\\\\"background\\\\\\\"\\\\n    role: \\\\\\\"Agent failure 分析 + cascading failure 发现\\\\\\\"\\\\n    key_finding: \\\\\\\"Cascading failures（单一 root cause 传播到后续决策）是长 horizon 任务的主要失败模式\\\\\\\"\\\\n    our_differentiation: \\\\\\\"Cascading failure 正是我们 temporal model 可以捕捉的 pattern——stagnation 往往是 cascade 的表现\\\\\\\"\\\\n\\\\n  - id: \\\\\\\"george2025cycledetection\\\\\\\"\\\\n    title: \\\\\\\"Unsupervised Cycle Detection in Agentic Applications\\\\\\\"\\\\n    authors: \\\\\\\"Felix George, Harshit Kumar, Divya Pathak, Kaustabha Ray, Mudit Verma, Pratibha Moogi\\\\\\\"\\\\n    venue: \\\\\\\"arXiv preprint (IBM Research)\\\\\\\"\\\\n    year: 2025\\\\n    arxiv: \\\\\\\"2511.10650\\\\\\\"\\\\n    category: \\\\\\\"background\\\\\\\"\\\\n    role: \\\\\\\"Cycle detection——最相关的 stagnation detection 前驱\\\\\\\"\\\\n    key_finding: \\\\\\\"混合方法：call-stack 分析（结构重复）+ embedding 语义相似度确认\\\\\\\"\\\\n    our_differentiation: \\\\\\\"他们只检测 exact/near-exact cycles，我们检测更广义的 stagnation（包括非重复性的停滞）；我们的 empirical analysis 表明 30 个 structural features（含但不限于 cycle 特征）即可达 0.995 F1\\\\\\\"\\\\n\\\\n  - id: \\\\\\\"pipis2025reasoningloop\\\\\\\"\\\\n    title: \\\\\\\"Wait, Wait, Wait... Why Do Reasoning Models Loop?\\\\\\\"\\\\n    authors: \\\\\\\"Charilaos Pipis, Shivam Garg, Vasilis Kontonis, Vaishnavi Shrivastava, Akshay Krishnamurthy, Dimitris Papailiopoulos\\\\\\\"\\\\n    venue: \\\\\\\"arXiv preprint\\\\\\\"\\\\n    year: 2025\\\\n    arxiv: \\\\\\\"2512.12895\\\\\\\"\\\\n    category: \\\\\\\"background\\\\\\\"\\\\n    role: \\\\\\\"Reasoning model looping 分析\\\\\\\"\\\\n    key_finding: \\\\\\\"Looping 是 risk-aversion 的表现：模型选择简单循环动作而非推进；用 30-gram 重复检测\\\\\\\"\\\\n    our_differentiation: \\\\\\\"他们分析 reasoning model 内部循环的原因，我们检测 agent trajectory 级别的 stagnation；n-gram 是我们 LFs 之一\\\\\\\"\\\\n\\\\n  - id: \\\\\\\"huang2024selfcorrect\\\\\\\"\\\\n    title: \\\\\\\"Large Language Models Cannot Self-Correct Reasoning Yet\\\\\\\"\\\\n    authors: \\\\\\\"Jie Huang, Xinyun Chen, Swaroop Mishra, Huaixiu Steven Zheng, Adams Wei Yu, Xinying Song, Denny Zhou\\\\\\\"\\\\n    venue: \\\\\\\"ICLR 2024\\\\\\\"\\\\n    year: 2024\\\\n    arxiv: \\\\\\\"2310.01798\\\\\\\"\\\\n    category: \\\\\\\"background\\\\\\\"\\\\n    verified: true\\\\n    role: \\\\\\\"Self-correction 失败的关键证据——支持 external monitoring 必要性\\\\\\\"\\\\n    key_finding: \\\\\\\"LLM 在无外部反馈时无法自我纠错推理错误，intrinsic self-correction 甚至导致性能下降\\\\\\\"\\\\n    our_differentiation: \\\\\\\"直接支持我们的核心论点：agent 不能可靠地自我检测 stagnation，需要外部 monitor；我们的 structural features 提供了轻量（<5ms）且高精度（0.995 F1）的外部检测方案\\\\\\\"\\\\n\\\\n  - id: \\\\\\\"kamoi2024selfcorrection\\\\\\\"\\\\n    title: \\\\\\\"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs\\\\\\\"\\\\n    authors: \\\\\\\"Ryo Kamoi, Yusen Zhang, Nan Zhang, Jiawei Han, Rui Zhang\\\\\\\"\\\\n    venue: \\\\\\\"TACL 2024\\\\\\\"\\\\n    year: 2024\\\\n    arxiv: \\\\\\\"2406.01297\\\\\\\"\\\\n    category: \\\\\\\"background\\\\\\\"\\\\n    verified: true\\\\n    role: \\\\\\\"Self-correction 条件的系统性综述——外部反馈是成功的必要条件\\\\\\\"\\\\n    key_finding: \\\\\\\"无外部反馈的 prompted self-correction 均未成功；self-correction 仅在有可靠外部反馈或大规模微调时有效\\\\\\\"\\\\n    our_differentiation: \\\\\\\"综述证实 self-correction 需要外部信号，我们的 empirical analysis 表明 structural features 即可提供高精度外部 stagnation 信号，无需复杂的语义理解\\\\\\\"\\\\n\\\\n  - id: \\\\\\\"liu2026trajad\\\\\\\"\\\\n    title: \\\\\\\"TrajAD: Trajectory Anomaly Detection for Trustworthy LLM Agents\\\\\\\"\\\\n    authors: \\\\\\\"Yibing Liu, Chong Zhang, Zhongyi Han, Hansong Liu, Yong Wang, Yang Yu, Xiaoyan Wang, Yilong Yin\\\\\\\"\\\\n    venue: \\\\\\\"arXiv preprint\\\\\\\"\\\\n    year: 2026\\\\n    arxiv: \\\\\\\"2602.06443\\\\\\\"\\\\n    category: \\\\\\\"background\\\\\\\"\\\\n    verified: true\\\\n    role: \\\\\\\"Agent trajectory 异常检测——stagnation detection 的直接前驱\\\\\\\"\\\\n    key_finding: \\\\\\\"TrajAD 通过 fine-grained process supervision 训练 verifier 检测 agent trajectory 中的异常（task failure, process inefficiency, unwarranted continuation），通用 LLM zero-shot 表现差\\\\\\\"\\\\n    our_differentiation: \\\\\\\"TrajAD 需要训练专用 verifier + 合成数据（perturb-and-complete），我们用 30 个 structural features 无需训练即达 0.995 F1；他们覆盖多种异常类型，我们专注 stagnation pattern 的深度分析\\\\\\\"\\\\n\\\\n  # ============================================================\\\\n  # CATEGORY: technique\\\\n  # ============================================================\\\\n\\\\n  - id: \\\\\\\"cho2014gru\\\\\\\"\\\\n    title: \\\\\\\"Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation\\\\\\\"\\\\n    authors: \\\\\\\"Kyunghyun Cho, Bart van Merrienboer, Caglar Gulcehre, Dzmitry Bahdanau, Fethi Bougares, Holger Schwenk, Yoshua Bengio\\\\\\\"\\\\n    venue: \\\\\\\"EMNLP 2014\\\\\\\"\\\\n    year: 2014\\\\n    arxiv: \\\\\\\"1406.1078\\\\\\\"\\\\n    category: \\\\\\\"technique\\\\\\\"\\\\n    role: \\\\\\\"GRU 原始论文——我们 probe model 的序列编码器\\\\\\\"\\\\n    key_finding: \\\\\\\"提出 GRU hidden unit，自适应门控信息流\\\\\\\"\\\\n\\\\n  - id: \\\\\\\"bahdanau2015attention\\\\\\\"\\\\n    title: \\\\\\\"Neural Machine Translation by Jointly Learning to Align and Translate\\\\\\\"\\\\n    authors: \\\\\\\"Dzmitry Bahdanau, Kyunghyun Cho, Yoshua Bengio\\\\\\\"\\\\n    venue: \\\\\\\"ICLR 2015\\\\\\\"\\\\n    year: 2015\\\\n    arxiv: \\\\\\\"1409.0473\\\\\\\"\\\\n    category: \\\\\\\"technique\\\\\\\"\\\\n    role: \\\\\\\"Attention mechanism——我们 probe model 的 attention 组件\\\\\\\"\\\\n    key_finding: \\\\\\\"注意力机制允许 decoder 选择性关注输入序列不同位置\\\\\\\"\\\\n\\\\n  - id: \\\\\\\"khosla2020supcon\\\\\\\"\\\\n    title: \\\\\\\"Supervised Contrastive Learning\\\\\\\"\\\\n    authors: \\\\\\\"Prannay Khosla, Piotr Teterwak, Chen Wang, Aaron Sarna, Yonglong Tian, Phillip Isola, Aaron Maschinot, Ce Liu, Dilip Krishnan\\\\\\\"\\\\n    venue: \\\\\\\"NeurIPS 2020\\\\\\\"\\\\n    year: 2020\\\\n    arxiv: \\\\\\\"2004.11362\\\\\\\"\\\\n    category: \\\\\\\"technique\\\\\\\"\\\\n    role: \\\\\\\"SupCon loss——我们的辅助训练目标\\\\\\\"\\\\n    key_finding: \\\\\\\"扩展自监督对比学习到有监督设置，同类样本拉近、异类推远，提升鲁棒性\\\\\\\"\\\\n\\\\n  - id: \\\\\\\"zhang2025qwen3embedding\\\\\\\"\\\\n    title: \\\\\\\"Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models\\\\\\\"\\\\n    authors: \\\\\\\"Yanzhao Zhang, Mingxin Li, Dingkun Long, Xin Zhang, Huan Lin, Baosong Yang, Pengjun Xie, An Yang, Dayiheng Liu, Junyang Lin, Fei Huang, Jingren Zhou\\\\\\\"\\\\n    venue: \\\\\\\"arXiv preprint\\\\\\\"\\\\n    year: 2025\\\\n    arxiv: \\\\\\\"2506.05176\\\\\\\"\\\\n    category: \\\\\\\"technique\\\\\\\"\\\\n    role: \\\\\\\"Embedding model——我们用于生成 trajectory window embeddings\\\\\\\"\\\\n    key_finding: \\\\\\\"基于 Qwen3 的 embedding 模型（0.6B/4B/8B），多阶段训练，MTEB 多语言 SOTA\\\\\\\"\\\\n\\\\n  - id: \\\\\\\"wang2024e5\\\\\\\"\\\\n    title: \\\\\\\"Multilingual E5 Text Embeddings: A Technical Report\\\\\\\"\\\\n    authors: \\\\\\\"Liang Wang, Nan Yang, Xiaolong Huang, Linjun Yang, Rangan Majumder, Furu Wei\\\\\\\"\\\\n    venue: \\\\\\\"arXiv preprint\\\\\\\"\\\\n    year: 2024\\\\n    arxiv: \\\\\\\"2402.05672\\\\\\\"\\\\n    category: \\\\\\\"technique\\\\\\\"\\\\n    verified: true\\\\n    role: \\\\\\\"Encoder ablation 中使用的 embedding model\\\\\\\"\\\\n    key_finding: \\\\\\\"基于 XLM-R 的多语言 text embedding，混合多语言数据训练，跨语言检索和语义相似度任务上性能强劲\\\\\\\"\\\\n\\\\n  - id: \\\\\\\"chen2024bgem3\\\\\\\"\\\\n    title: \\\\\\\"BGE M3-Embedding: Multi-Linguality, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation\\\\\\\"\\\\n    authors: \\\\\\\"Jianlv Chen, Shitao Xiao, Peitian Zhang, Kun Luo, Defu Lian, Zheng Liu\\\\\\\"\\\\n    venue: \\\\\\\"arXiv preprint\\\\\\\"\\\\n    year: 2024\\\\n    arxiv: \\\\\\\"2402.03216\\\\\\\"\\\\n    category: \\\\\\\"technique\\\\\\\"\\\\n    verified: true\\\\n    role: \\\\\\\"Encoder ablation 中使用的 embedding model\\\\\\\"\\\\n    key_finding: \\\\\\\"统一 dense/sparse/multi-vec 三种检索功能于单一模型，通过 self-knowledge distillation 训练，支持 8192 token 长文本和 100+ 语言\\\\\\\"\\\\n\\\\n# ============================================================\\\\n# NOVELTY ANALYSIS SUMMARY (D039 Pivot — Empirical Analysis)\\\\n# ============================================================\\\\n#\\\\n# Primary novelty: 首次系统性实证分析 agent stagnation 检测中 structural vs\\\\n# semantic signal 的有效性。30 个结构特征达 0.995 in-domain / 0.967 cross-agent F1，\\\\n# 全面优于 NL embedding (0.906/0.751) 和 LLM-as-judge (+24.3pp)。\\\\n#\\\\n# 三层贡献：\\\\n# 1. Structural Signal Discovery (primary) — 改变社区对 agent monitoring 方法选型认知\\\\n# 2. LF Temporal Dynamics Analysis — 量化 LFs 时序角色 + agent-specific 迁移分析\\\\n# 3. TLM Negative Finding — 3 种实现 (TWV/HMM/lag-aware HMM) 均未超越 MV\\\\n#\\\\n# 方法论前驱（TLM negative finding 的参照）：\\\\n# 1. Safranchik AAAI 2020 (linked HMM) — NER-specific，BIO 约束，token-level\\\\n# 2. Sala NeurIPS 2019 (multi-resolution WS) — 处理分辨率不匹配，不建模 label transition\\\\n# 3. Nguyen ACL 2017 (HMM-Crowd) — crowdsourcing 场景，不是 programmatic LFs\\\\n#\\\\n# 核心差异化：不是 \\\\\\\"method paper proposing TLM\\\\\\\"，而是 \\\\\\\"empirical study revealing\\\\n# structural signals dominate stagnation detection, with temporal modeling as\\\\n# well-motivated negative finding\\\\\\\".\\\\n\\\", \\\"total_chars\\\": 23431, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/literature_map.yaml\", \"content\": \"# Literature Map for Agent Progress Probe (EMNLP 2026 ARR)\\n# Generated: 2026-05-14\\n# Paper: Structural Signal Analysis for Progress Stagnation Detection in LLM Agents\\n#\\n# D039 Pivot: Empirical analysis paper. Central finding: stagnation signals are\\n# fundamentally structural (30 features → 0.995 in-domain, 0.967 cross-agent F1),\\n# decisively surpassing NL embeddings (0.906/0.751) and LLM-as-judge (+24.3pp).\\n# TLM is a well-motivated negative finding (3 implementations all fail to beat MV).\\n\\npapers:\\n\\n  # ============================================================\\n  # CATEGORY: direct-competitor\\n  # ============================================================\\n\\n  - id: \\\"xi2025agentprm\\\"\\n    title: \\\"AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress\\\"\\n    authors: \\\"Zhiheng Xi, Chenyang Liao, Guanyu Li, Yajie Yang, Wenxiang Chen, Zhihao Zhang, Binghai Wang, Senjie Jin, Yuhao Zhou, Jian Guan, Wei Wu, Tao Ji, Tao Gui, Qi Zhang, Xuanjing Huang\\\"\\n    venue: \\\"arXiv preprint\\\"\\n    year: 2025\\n    arxiv: \\\"2511.08325\\\"\\n    category: \\\"direct-competitor\\\"\\n    role: \\\"主要竞争者：step-level PRM for agent guidance\\\"\\n    key_finding: \\\"用 promise（长期潜力）和 progress（即时进展）两个维度评估 agent 每步决策，实现 8x 计算效率提升\\\"\\n    our_differentiation: \\\"我们是 window-level monitoring（不是 step-level guidance），不需要 outcome labels，目标是 stagnation detection 不是 reward shaping\\\"\\n\\n  - id: \\\"choudhury2025prm\\\"\\n    title: \\\"Process Reward Models for LLM Agents: Practical Framework and Directions\\\"\\n    authors: \\\"Sanjiban Choudhury\\\"\\n    venue: \\\"arXiv preprint\\\"\\n    year: 2025\\n    arxiv: \\\"2502.10325\\\"\\n    category: \\\"direct-competitor\\\"\\n    role: \\\"PRM 框架综述 + InversePRM 方法\\\"\\n    key_finding: \\\"提出 AgentPRM（Monte Carlo rollout actor-critic）和 InversePRM（从 demonstrations 学习 process reward），3B 模型超越 GPT-4o\\\"\\n    our_differentiation: \\\"InversePRM 仍需 demonstration trajectories，我们用 programmatic LFs 替代人工标注；我们关注 monitoring 而非 training signal\\\"\\n\\n  - id: \\\"li2026toolprmbench\\\"\\n    title: \\\"ToolPRMBench: Evaluating and Advancing Process Reward Models for Tool-using Agents\\\"\\n    authors: \\\"Dawei Li, Yuguang Yao, Zhen Tan, Huan Liu, Ruocheng Guo\\\"\\n    venue: \\\"arXiv preprint\\\"\\n    year: 2026\\n    arxiv: \\\"2601.12294\\\"\\n    category: \\\"direct-competitor\\\"\\n    role: \\\"Tool-use PRM 评测基准\\\"\\n    key_finding: \\\"大规模 benchmark 评测 PRM 在 tool-use 场景的效果，发现专用 PRM 显著优于通用 PRM\\\"\\n    our_differentiation: \\\"我们的 empirical analysis 揭示 structural features 足以检测 stagnation（0.995 F1），无需 step-level reward labels；关注 stagnation pattern 而非 step correctness\\\"\\n\\n  - id: \\\"wang2026planrewardbench\\\"\\n    title: \\\"Aligning Agents via Planning: A Benchmark for Trajectory-Level Reward Modeling\\\"\\n    authors: \\\"Jiaxuan Wang, Yulan Hu, Wenjin Yang, Zheng Pan, Xin Li, Lan-Zhe Guo\\\"\\n    venue: \\\"arXiv preprint\\\"\\n    year: 2026\\n    arxiv: \\\"2604.08178\\\"\\n    category: \\\"direct-competitor\\\"\\n    role: \\\"Trajectory-level reward model 评测\\\"\\n    key_finding: \\\"所有 reward model 类别（generative, discriminative, LLM-as-Judge）在长 horizon trajectory 上性能显著下降\\\"\\n    our_differentiation: \\\"验证了长 trajectory 评估的难度——我们的 window-level 方法通过局部化避免了这个问题\\\"\\n\\n  - id: \\\"chen2025monitoring\\\"\\n    title: \\\"Monitoring LLM Agents for Sequentially Contextual Harm\\\"\\n    authors: \\\"Yueh-Han Chen, Neelay Joshi, Yulin Chen, He He, Rico Angell\\\"\\n    venue: \\\"ICLR 2025 Workshop on Building Trust in Language Models and Applications\\\"\\n    year: 2025\\n    arxiv: null\\n    openreview: \\\"LC0XQ6ufbr\\\"\\n    category: \\\"direct-competitor\\\"\\n    role: \\\"Agent monitoring 安全方向\\\"\\n    key_finding: \\\"将有害任务分解为单独无害的子任务可将 refusal rate 从 50% 降至 10%，现有 monitor 难以检测 sequentially contextual harm\\\"\\n    our_differentiation: \\\"他们关注 safety monitoring（harmful behavior），我们关注 progress monitoring（stagnation）；互补方向\\\"\\n\\n  - id: \\\"kale2025weaktostrong\\\"\\n    title: \\\"Reliable Weak-to-Strong Monitoring of LLM Agents\\\"\\n    authors: \\\"Neil Kale, Chen Bo Calvin Zhang, Kevin Zhu, Ankit Aich, Paula Rodriguez, Scale Red Team, Christina Q. Knight, Zifan Wang\\\"\\n    venue: \\\"arXiv preprint\\\"\\n    year: 2025\\n    arxiv: \\\"2508.19461\\\"\\n    category: \\\"direct-competitor\\\"\\n    role: \\\"Weak-to-strong agent monitoring 方法论\\\"\\n    key_finding: \\\"Monitor scaffolding 比 monitor 能力更重要，弱模型可以可靠监控强模型；targeted human-in-the-loop 提升 TPR ~15%\\\"\\n    our_differentiation: \\\"他们用 LLM 作为 monitor，我们发现 30 个 structural features 即可达 0.967 跨域 F1，不依赖另一个 LLM；更轻量（<5ms）且可解释\\\"\\n\\n  - id: \\\"fan2026agentrm\\\"\\n    title: \\\"Exploring Reasoning Reward Model for Agents\\\"\\n    authors: \\\"Kaixuan Fan, Kaituo Feng, Manyuan Zhang, Tianshuo Peng, Zhixun Li, Yilei Jiang, Shuang Chen, Peng Pei, Xunliang Cai, Xiangyu Yue\\\"\\n    venue: \\\"arXiv preprint\\\"\\n    year: 2026\\n    arxiv: \\\"2601.22154\\\"\\n    category: \\\"direct-competitor\\\"\\n    verified: true\\n    role: \\\"Agent trajectory 的多维度 reasoning reward model\\\"\\n    key_finding: \\\"Agent-RRM 通过 reasoning trace + critique + overall score 三维结构化反馈评估 agent trajectory，在 12 个 benchmark 上显著提升（GAIA 43.7%, WebWalkerQA 46.2%）\\\"\\n    our_differentiation: \\\"他们用 LLM-based reward model 生成结构化反馈用于 agent 改进，我们的 empirical analysis 表明轻量 structural features 即可高精度检测 stagnation（0.995 F1），不依赖大模型推理\\\"\\n\\n  - id: \\\"qiu2026dataprm\\\"\\n    title: \\\"Rewarding the Scientific Process: Process-Level Reward Modeling for Agentic Data Analysis\\\"\\n    authors: \\\"Zhisong Qiu, Shuofei Qiao, Kewei Xu, Yuqi Zhu, Lun Du, Ningyu Zhang, Huajun Chen\\\"\\n    venue: \\\"arXiv preprint\\\"\\n    year: 2026\\n    arxiv: \\\"2604.24198\\\"\\n    category: \\\"direct-competitor\\\"\\n    verified: true\\n    role: \\\"Agentic data analysis 场景的 process-level reward model\\\"\\n    key_finding: \\\"传统 PRM 无法检测 silent errors 且误判 exploratory steps；DataPRM 通过 environment-aware probing + ternary reward 策略在 ScienceAgentBench 提升 7.21%\\\"\\n    our_differentiation: \\\"DataPRM 针对数据分析 agent 的 step correctness，我们针对通用 agent 的 stagnation pattern；他们需要 execution state probing，我们用 structural LFs 无需环境交互\\\"\\n\\n  # ============================================================\\n  # CATEGORY: method-component\\n  # ============================================================\\n\\n  - id: \\\"ratner2016dataprogramming\\\"\\n    title: \\\"Data Programming: Creating Large Training Sets, Quickly\\\"\\n    authors: \\\"Alexander Ratner, Christopher De Sa, Sen Wu, Daniel Selsam, Christopher Re\\\"\\n    venue: \\\"NeurIPS 2016\\\"\\n    year: 2016\\n    arxiv: \\\"1605.07723\\\"\\n    category: \\\"method-component\\\"\\n    role: \\\"核心方法论基础：data programming 范式\\\"\\n    key_finding: \\\"用户编写 labeling functions（噪声启发式），generative model 学习 LF 准确率生成概率训练标签\\\"\\n    our_differentiation: \\\"我们在 agent trajectory 上应用 data programming，发现 structural features 主导检测能力；同时揭示 LFs 的时序动态和 temporal label model 的负面结果\\\"\\n\\n  - id: \\\"ratner2017snorkel\\\"\\n    title: \\\"Snorkel: Rapid Training Data Creation with Weak Supervision\\\"\\n    authors: \\\"Alexander Ratner, Stephen H. Bach, Henry Ehrenberg, Jason Fries, Sen Wu, Christopher Re\\\"\\n    venue: \\\"VLDB 2018\\\"\\n    year: 2018\\n    arxiv: \\\"1711.10160\\\"\\n    category: \\\"method-component\\\"\\n    role: \\\"Data programming 系统实现，label model 基础\\\"\\n    key_finding: \\\"端到端弱监督系统：LFs → generative label model（建模 LF dependency）→ discriminative end model\\\"\\n    our_differentiation: \\\"Snorkel 假设数据点 i.i.d.，我们发现 agent trajectory 上 LFs 展现系统性时序动态（violating i.i.d.），但 temporal label model 未能超越 MV（negative finding）\\\"\\n\\n  - id: \\\"fu2020flyingsquid\\\"\\n    title: \\\"Fast and Three-rious: Speeding Up Weak Supervision with Triplet Methods\\\"\\n    authors: \\\"Daniel Y. Fu, Mayee F. Chen, Frederic Sala, Sarah M. Hooper, Kayvon Fatahalian, Christopher Re\\\"\\n    venue: \\\"ICML 2020\\\"\\n    year: 2020\\n    arxiv: \\\"2002.11955\\\"\\n    category: \\\"method-component\\\"\\n    role: \\\"快速 label model，triplet method of moments\\\"\\n    key_finding: \\\"用 triplet method 闭式求解 label model 参数，比 SGD 快 170x\\\"\\n    our_differentiation: \\\"FlyingSquid 同样假设 i.i.d.；我们的 empirical analysis 揭示 i.i.d. violation 虽系统性存在，但 temporal correction 在低冲突 regime 下无收益（negative finding）\\\"\\n\\n  - id: \\\"zhang2021wrench\\\"\\n    title: \\\"WRENCH: A Comprehensive Benchmark for Weak Supervision\\\"\\n    authors: \\\"Jieyu Zhang, Yue Yu, Yinghao Li, Yujing Wang, Yaming Yang, Mao Yang, Alexander Ratner\\\"\\n    venue: \\\"NeurIPS 2021 Datasets and Benchmarks Track\\\"\\n    year: 2021\\n    arxiv: \\\"2109.11377\\\"\\n    category: \\\"method-component\\\"\\n    role: \\\"弱监督评测基准\\\"\\n    key_finding: \\\"22 个真实数据集 + 120+ 方法变体评测，标准化弱监督研究\\\"\\n    our_differentiation: \\\"WRENCH 数据集全是 i.i.d. 分类/序列标注，没有 temporal stagnation detection 任务\\\"\\n\\n  - id: \\\"safranchik2020linkedhmm\\\"\\n    title: \\\"Weakly Supervised Sequence Tagging from Noisy Rules\\\"\\n    authors: \\\"Esteban Safranchik, Shiying Luo, Stephen H. Bach\\\"\\n    venue: \\\"AAAI 2020\\\"\\n    year: 2020\\n    arxiv: null\\n    category: \\\"method-component\\\"\\n    role: \\\"最近的方法论前驱：linked HMM for sequence tagging weak supervision\\\"\\n    key_finding: \\\"将 HMM 引入弱监督序列标注（NER），加入 linking rules 建模 span 结构，比 i.i.d. label model +7 F1\\\"\\n    our_differentiation: \\\"他们是 token-level NER（BIO 约束），我们是 window-level temporal classification；我们建模的是 stagnation temporal dynamics 而非 entity boundary\\\"\\n\\n  - id: \\\"sala2019multiresolution\\\"\\n    title: \\\"Multi-Resolution Weak Supervision for Sequential Data\\\"\\n    authors: \\\"Frederic Sala, Paroma Varma, Jason Fries, Daniel Y. Fu, Stefano Sagawa, Christopher Re\\\"\\n    venue: \\\"NeurIPS 2019\\\"\\n    year: 2019\\n    arxiv: \\\"1910.09505\\\"\\n    category: \\\"method-component\\\"\\n    role: \\\"最近的方法论前驱：multi-resolution WS for sequential data\\\"\\n    key_finding: \\\"处理不同时间分辨率的 LFs（如 frame-level vs span-level），建模 multi-resolution LF correlations\\\"\\n    our_differentiation: \\\"他们关注 resolution mismatch，我们关注 temporal label transitions；互补视角\\\"\\n\\n  - id: \\\"dawid1979em\\\"\\n    title: \\\"Maximum Likelihood Estimation of Observer Error-Rates Using the EM Algorithm\\\"\\n    authors: \\\"A. P. Dawid, A. M. Skene\\\"\\n    venue: \\\"Journal of the Royal Statistical Society, Series C\\\"\\n    year: 1979\\n    arxiv: null\\n    category: \\\"method-component\\\"\\n    role: \\\"Label aggregation 奠基工作\\\"\\n    key_finding: \\\"用 EM 算法估计标注者混淆矩阵，无需 ground truth\\\"\\n    our_differentiation: \\\"经典 i.i.d. 假设；我们测试了 temporal extension（HMM-TLM, lag-aware HMM）但发现在 3-LF 低冲突 regime 下未超越 MV——约束未来 temporal label model 研究\\\"\\n\\n  - id: \\\"nguyen2017hmmcrowd\\\"\\n    title: \\\"Aggregating and Predicting Sequence Labels from Crowd Annotations\\\"\\n    authors: \\\"An Thanh Nguyen, Byron C. Wallace, Junyi Jessy Li, Ani Nenkova, Matthew Lease\\\"\\n    venue: \\\"ACL 2017\\\"\\n    year: 2017\\n    arxiv: null\\n    category: \\\"method-component\\\"\\n    role: \\\"HMM + crowdsourcing label aggregation\\\"\\n    key_finding: \\\"HMM-Crowd：扩展 Dawid-Skene 到序列数据，加入 one-step Markov structure over true labels\\\"\\n    our_differentiation: \\\"他们用于 crowdsourcing（人类标注者），我们用于 programmatic LFs（自动化）；他们是 NER/IE，我们是 agent progress monitoring\\\"\\n\\n  # ============================================================\\n  # CATEGORY: evaluation\\n  # ============================================================\\n\\n  - id: \\\"orlanski2026slopcodebench\\\"\\n    title: \\\"SlopCodeBench: Benchmarking How Coding Agents Degrade Over Long-Horizon Iterative Tasks\\\"\\n    authors: \\\"Gabriel Orlanski, Devjeet Roy, Alexander Yun, Changho Shin, Alex Gu, Albert Ge, Dyah Adila, Nicholas Roberts, Frederic Sala, Aws Albarghouthi\\\"\\n    venue: \\\"arXiv preprint\\\"\\n    year: 2026\\n    arxiv: \\\"2603.24755\\\"\\n    category: \\\"evaluation\\\"\\n    role: \\\"Agent degradation 基准——直接支持我们的 problem motivation\\\"\\n    key_finding: \\\"Agent 代码质量在迭代任务中持续退化：比人类代码 2.3x 更冗余、2.0x 更结构侵蚀，75-77% trajectory 呈现退化趋势\\\"\\n    our_differentiation: \\\"SlopCodeBench 量化了 degradation 现象，我们提供了检测方法；他们是 post-hoc 评测，我们是 online monitoring\\\"\\n\\n  - id: \\\"jimenez2024swebench\\\"\\n    title: \\\"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?\\\"\\n    authors: \\\"Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan\\\"\\n    venue: \\\"ICLR 2024\\\"\\n    year: 2024\\n    arxiv: \\\"2310.06770\\\"\\n    category: \\\"evaluation\\\"\\n    role: \\\"Agent 数据来源之一\\\"\\n    key_finding: \\\"2294 个真实 GitHub issue 任务，标准化 agent 评测\\\"\\n    our_differentiation: \\\"我们使用 SWE-bench agent trajectories 作为实验数据源之一\\\"\\n\\n  - id: \\\"yang2024sweagent\\\"\\n    title: \\\"SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering\\\"\\n    authors: \\\"John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press\\\"\\n    venue: \\\"NeurIPS 2024\\\"\\n    year: 2024\\n    arxiv: \\\"2405.15793\\\"\\n    category: \\\"evaluation\\\"\\n    role: \\\"Agent 系统——trajectory 数据来源\\\"\\n    key_finding: \\\"提出 agent-computer interface (ACI)，GPT-4 Turbo 在 SWE-bench 达 12.47% resolve rate\\\"\\n    our_differentiation: \\\"SWE-agent trajectories 是我们分析 stagnation 的数据来源之一\\\"\\n\\n  - id: \\\"wang2025openhands\\\"\\n    title: \\\"OpenHands: An Open Platform for AI Software Developers as Generalist Agents\\\"\\n    authors: \\\"Xingyao Wang, Boxuan Li, Yufan Song, Frank F. Xu, Xiangru Tang, et al.\\\"\\n    venue: \\\"ICLR 2025\\\"\\n    year: 2025\\n    arxiv: \\\"2407.16741\\\"\\n    category: \\\"evaluation\\\"\\n    role: \\\"Agent 平台——主要数据来源\\\"\\n    key_finding: \\\"开源 agent 平台，sandbox 执行环境，15+ benchmarks 评测\\\"\\n    our_differentiation: \\\"OpenHands trajectories 是我们的主要实验数据来源\\\"\\n\\n  - id: \\\"zhou2024webarena\\\"\\n    title: \\\"WebArena: A Realistic Web Environment for Building Autonomous Agents\\\"\\n    authors: \\\"Shuyan Zhou, Frank F. Xu, Hao Zhu, Xuhui Zhou, Robert Lo, Abishek Sridhar, Xianyi Cheng, Tianyue Ou, Yonatan Bisk, Daniel Fried, Uri Alon, Graham Neubig\\\"\\n    venue: \\\"ICLR 2024\\\"\\n    year: 2024\\n    arxiv: \\\"2307.13854\\\"\\n    category: \\\"evaluation\\\"\\n    verified: true\\n    role: \\\"Web agent 评测基准——long-horizon 任务评估\\\"\\n    key_finding: \\\"812 个真实网站上的 long-horizon 任务，GPT-4 agent 仅 14.41% 成功率 vs 人类 78.24%，揭示 agent 在复杂任务上的巨大差距\\\"\\n    our_differentiation: \\\"WebArena 的 long-horizon 任务正是 stagnation 高发场景；我们的 monitor 可作为此类任务的早期终止/干预信号\\\"\\n\\n  - id: \\\"wang2024mint\\\"\\n    title: \\\"MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback\\\"\\n    authors: \\\"Xingyao Wang, Zihan Wang, Jiateng Liu, Yangyi Chen, Lifan Yuan, Hao Peng, Heng Ji\\\"\\n    venue: \\\"ICLR 2024\\\"\\n    year: 2024\\n    arxiv: \\\"2309.10691\\\"\\n    category: \\\"evaluation\\\"\\n    verified: true\\n    role: \\\"Multi-turn agent 评测基准——tool use + feedback 交互评估\\\"\\n    key_finding: \\\"评估 LLM 在多轮交互中使用工具和接收自然语言反馈的能力，每轮 tool use 提升 1-8%，NL feedback 提升 2-17%\\\"\\n    our_differentiation: \\\"MINT 量化了 multi-turn 交互中的性能变化，我们的 stagnation detection 关注多轮交互中进展停滞的检测；MINT 的 multi-turn 设定与我们的 window-level 分析天然对齐\\\"\\n\\n  # ============================================================\\n  # CATEGORY: background\\n  # ============================================================\\n\\n  - id: \\\"shinn2023reflexion\\\"\\n    title: \\\"Reflexion: Language Agents with Verbal Reinforcement Learning\\\"\\n    authors: \\\"Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao\\\"\\n    venue: \\\"NeurIPS 2023\\\"\\n    year: 2023\\n    arxiv: \\\"2303.11366\\\"\\n    category: \\\"background\\\"\\n    role: \\\"Agent self-reflection 代表工作\\\"\\n    key_finding: \\\"通过 verbal feedback 强化 agent，反思文本存入 episodic memory 用于后续 trial\\\"\\n    our_differentiation: \\\"Reflexion 是 agent 自我改进机制，我们是外部 monitoring；self-reflection 可能失效时我们的 monitor 仍能检测 stagnation\\\"\\n\\n  - id: \\\"zhou2024lats\\\"\\n    title: \\\"Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models\\\"\\n    authors: \\\"Andy Zhou, Kai Yan, Michal Shlapentokh-Rothman, Haohan Wang, Yu-Xiong Wang\\\"\\n    venue: \\\"ICML 2024\\\"\\n    year: 2024\\n    arxiv: \\\"2310.04406\\\"\\n    category: \\\"background\\\"\\n    role: \\\"Agent planning + self-reflection\\\"\\n    key_finding: \\\"结合 MCTS 与 LM value function 和 self-reflection，支持 backtracking\\\"\\n    our_differentiation: \\\"LATS 通过搜索避免 stagnation，但计算开销大；我们的 monitor 可作为 LATS 的早期终止信号\\\"\\n\\n  - id: \\\"yao2023tot\\\"\\n    title: \\\"Tree of Thoughts: Deliberate Problem Solving with Large Language Models\\\"\\n    authors: \\\"Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Thomas L. Griffiths, Yuan Cao, Karthik Narasimhan\\\"\\n    venue: \\\"NeurIPS 2023\\\"\\n    year: 2023\\n    arxiv: \\\"2305.10601\\\"\\n    category: \\\"background\\\"\\n    role: \\\"Deliberate reasoning 框架\\\"\\n    key_finding: \\\"将 CoT 泛化为树结构，LM 自我评估中间 thought 并 backtrack\\\"\\n    our_differentiation: \\\"ToT 的自评估是 single-step 的；我们捕捉 multi-step temporal patterns\\\"\\n\\n  - id: \\\"cemri2025multiagentfail\\\"\\n    title: \\\"Why Do Multi-Agent LLM Systems Fail?\\\"\\n    authors: \\\"Mert Cemri, Melissa Z. Pan, Shuyi Yang, Lakshya A. Agrawal, et al.\\\"\\n    venue: \\\"arXiv preprint\\\"\\n    year: 2025\\n    arxiv: \\\"2503.13657\\\"\\n    category: \\\"background\\\"\\n    role: \\\"Agent failure taxonomy——problem motivation\\\"\\n    key_finding: \\\"MAST taxonomy：14 种失败模式，其中 Step Repetition 被识别为具体失败症状\\\"\\n    our_differentiation: \\\"他们提供 taxonomy（what fails），我们提供 detection method（how to detect）\\\"\\n\\n  - id: \\\"zhu2025agentfail\\\"\\n    title: \\\"Where LLM Agents Fail and How They Can Learn From Failures\\\"\\n    authors: \\\"Kunlun Zhu, Zijia Liu, Bingxuan Li, et al.\\\"\\n    venue: \\\"arXiv preprint\\\"\\n    year: 2025\\n    arxiv: \\\"2509.25370\\\"\\n    category: \\\"background\\\"\\n    role: \\\"Agent failure 分析 + cascading failure 发现\\\"\\n    key_finding: \\\"Cascading failures（单一 root cause 传播到后续决策）是长 horizon 任务的主要失败模式\\\"\\n    our_differentiation: \\\"Cascading failure 正是我们 temporal model 可以捕捉的 pattern——stagnation 往往是 cascade 的表现\\\"\\n\\n  - id: \\\"george2025cycledetection\\\"\\n    title: \\\"Unsupervised Cycle Detection in Agentic Applications\\\"\\n    authors: \\\"Felix George, Harshit Kumar, Divya Pathak, Kaustabha Ray, Mudit Verma, Pratibha Moogi\\\"\\n    venue: \\\"arXiv preprint (IBM Research)\\\"\\n    year: 2025\\n    arxiv: \\\"2511.10650\\\"\\n    category: \\\"background\\\"\\n    role: \\\"Cycle detection——最相关的 stagnation detection 前驱\\\"\\n    key_finding: \\\"混合方法：call-stack 分析（结构重复）+ embedding 语义相似度确认\\\"\\n    our_differentiation: \\\"他们只检测 exact/near-exact cycles，我们检测更广义的 stagnation（包括非重复性的停滞）；我们的 empirical analysis 表明 30 个 structural features（含但不限于 cycle 特征）即可达 0.995 F1\\\"\\n\\n  - id: \\\"pipis2025reasoningloop\\\"\\n    title: \\\"Wait, Wait, Wait... Why Do Reasoning Models Loop?\\\"\\n    authors: \\\"Charilaos Pipis, Shivam Garg, Vasilis Kontonis, Vaishnavi Shrivastava, Akshay Krishnamurthy, Dimitris Papailiopoulos\\\"\\n    venue: \\\"arXiv preprint\\\"\\n    year: 2025\\n    arxiv: \\\"2512.12895\\\"\\n    category: \\\"background\\\"\\n    role: \\\"Reasoning model looping 分析\\\"\\n    key_finding: \\\"Looping 是 risk-aversion 的表现：模型选择简单循环动作而非推进；用 30-gram 重复检测\\\"\\n    our_differentiation: \\\"他们分析 reasoning model 内部循环的原因，我们检测 agent trajectory 级别的 stagnation；n-gram 是我们 LFs 之一\\\"\\n\\n  - id: \\\"huang2024selfcorrect\\\"\\n    title: \\\"Large Language Models Cannot Self-Correct Reasoning Yet\\\"\\n    authors: \\\"Jie Huang, Xinyun Chen, Swaroop Mishra, Huaixiu Steven Zheng, Adams Wei Yu, Xinying Song, Denny Zhou\\\"\\n    venue: \\\"ICLR 2024\\\"\\n    year: 2024\\n    arxiv: \\\"2310.01798\\\"\\n    category: \\\"background\\\"\\n    verified: true\\n    role: \\\"Self-correction 失败的关键证据——支持 external monitoring 必要性\\\"\\n    key_finding: \\\"LLM 在无外部反馈时无法自我纠错推理错误，intrinsic self-correction 甚至导致性能下降\\\"\\n    our_differentiation: \\\"直接支持我们的核心论点：agent 不能可靠地自我检测 stagnation，需要外部 monitor；我们的 structural features 提供了轻量（<5ms）且高精度（0.995 F1）的外部检测方案\\\"\\n\\n  - id: \\\"kamoi2024selfcorrection\\\"\\n    title: \\\"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs\\\"\\n    authors: \\\"Ryo Kamoi, Yusen Zhang, Nan Zhang, Jiawei Han, Rui Zhang\\\"\\n    venue: \\\"TACL 2024\\\"\\n    year: 2024\\n    arxiv: \\\"2406.01297\\\"\\n    category: \\\"background\\\"\\n    verified: true\\n    role: \\\"Self-correction 条件的系统性综述——外部反馈是成功的必要条件\\\"\\n    key_finding: \\\"无外部反馈的 prompted self-correction 均未成功；self-correction 仅在有可靠外部反馈或大规模微调时有效\\\"\\n    our_differentiation: \\\"综述证实 self-correction 需要外部信号，我们的 empirical analysis 表明 structural features 即可提供高精度外部 stagnation 信号，无需复杂的语义理解\\\"\\n\\n  - id: \\\"liu2026trajad\\\"\\n    title: \\\"TrajAD: Trajectory Anomaly Detection for Trustworthy LLM Agents\\\"\\n    authors: \\\"Yibing Liu, Chong Zhang, Zhongyi Han, Hansong Liu, Yong Wang, Yang Yu, Xiaoyan Wang, Yilong Yin\\\"\\n    venue: \\\"arXiv preprint\\\"\\n    year: 2026\\n    arxiv: \\\"2602.06443\\\"\\n    category: \\\"background\\\"\\n    verified: true\\n    role: \\\"Agent trajectory 异常检测——stagnation detection 的直接前驱\\\"\\n    key_finding: \\\"TrajAD 通过 fine-grained process supervision 训练 verifier 检测 agent trajectory 中的异常（task failure, process inefficiency, unwarranted continuation），通用 LLM zero-shot 表现差\\\"\\n    our_differentiation: \\\"TrajAD 需要训练专用 verifier + 合成数据（perturb-and-complete），我们用 30 个 structural features 无需训练即达 0.995 F1；他们覆盖多种异常类型，我们专注 stagnation pattern 的深度分析\\\"\\n\\n  # ============================================================\\n  # CATEGORY: technique\\n  # ============================================================\\n\\n  - id: \\\"cho2014gru\\\"\\n    title: \\\"Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation\\\"\\n    authors: \\\"Kyunghyun Cho, Bart van Merrienboer, Caglar Gulcehre, Dzmitry Bahdanau, Fethi Bougares, Holger Schwenk, Yoshua Bengio\\\"\\n    venue: \\\"EMNLP 2014\\\"\\n    year: 2014\\n    arxiv: \\\"1406.1078\\\"\\n    category: \\\"technique\\\"\\n    role: \\\"GRU 原始论文——我们 probe model 的序列编码器\\\"\\n    key_finding: \\\"提出 GRU hidden unit，自适应门控信息流\\\"\\n\\n  - id: \\\"bahdanau2015attention\\\"\\n    title: \\\"Neural Machine Translation by Jointly Learning to Align and Translate\\\"\\n    authors: \\\"Dzmitry Bahdanau, Kyunghyun Cho, Yoshua Bengio\\\"\\n    venue: \\\"ICLR 2015\\\"\\n    year: 2015\\n    arxiv: \\\"1409.0473\\\"\\n    category: \\\"technique\\\"\\n    role: \\\"Attention mechanism——我们 probe model 的 attention 组件\\\"\\n    key_finding: \\\"注意力机制允许 decoder 选择性关注输入序列不同位置\\\"\\n\\n  - id: \\\"khosla2020supcon\\\"\\n    title: \\\"Supervised Contrastive Learning\\\"\\n    authors: \\\"Prannay Khosla, Piotr Teterwak, Chen Wang, Aaron Sarna, Yonglong Tian, Phillip Isola, Aaron Maschinot, Ce Liu, Dilip Krishnan\\\"\\n    venue: \\\"NeurIPS 2020\\\"\\n    year: 2020\\n    arxiv: \\\"2004.11362\\\"\\n    category: \\\"technique\\\"\\n    role: \\\"SupCon loss——我们的辅助训练目标\\\"\\n    key_finding: \\\"扩展自监督对比学习到有监督设置，同类样本拉近、异类推远，提升鲁棒性\\\"\\n\\n  - id: \\\"zhang2025qwen3embedding\\\"\\n    title: \\\"Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models\\\"\\n    authors: \\\"Yanzhao Zhang, Mingxin Li, Dingkun Long, Xin Zhang, Huan Lin, Baosong Yang, Pengjun Xie, An Yang, Dayiheng Liu, Junyang Lin, Fei Huang, Jingren Zhou\\\"\\n    venue: \\\"arXiv preprint\\\"\\n    year: 2025\\n    arxiv: \\\"2506.05176\\\"\\n    category: \\\"technique\\\"\\n    role: \\\"Embedding model——我们用于生成 trajectory window embeddings\\\"\\n    key_finding: \\\"基于 Qwen3 的 embedding 模型（0.6B/4B/8B），多阶段训练，MTEB 多语言 SOTA\\\"\\n\\n  - id: \\\"wang2024e5\\\"\\n    title: \\\"Multilingual E5 Text Embeddings: A Technical Report\\\"\\n    authors: \\\"Liang Wang, Nan Yang, Xiaolong Huang, Linjun Yang, Rangan Majumder, Furu Wei\\\"\\n    venue: \\\"arXiv preprint\\\"\\n    year: 2024\\n    arxiv: \\\"2402.05672\\\"\\n    category: \\\"technique\\\"\\n    verified: true\\n    role: \\\"Encoder ablation 中使用的 embedding model\\\"\\n    key_finding: \\\"基于 XLM-R 的多语言 text embedding，混合多语言数据训练，跨语言检索和语义相似度任务上性能强劲\\\"\\n\\n  - id: \\\"chen2024bgem3\\\"\\n    title: \\\"BGE M3-Embedding: Multi-Linguality, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation\\\"\\n    authors: \\\"Jianlv Chen, Shitao Xiao, Peitian Zhang, Kun Luo, Defu Lian, Zheng Liu\\\"\\n    venue: \\\"arXiv preprint\\\"\\n    year: 2024\\n    arxiv: \\\"2402.03216\\\"\\n    category: \\\"technique\\\"\\n    verified: true\\n    role: \\\"Encoder ablation 中使用的 embedding model\\\"\\n    key_finding: \\\"统一 dense/sparse/multi-vec 三种检索功能于单一模型，通过 self-knowledge distillation 训练，支持 8192 token 长文本和 100+ 语言\\\"\\n\\n# ============================================================\\n# NOVELTY ANALYSIS SUMMARY (D039 Pivot — Empirical Analysis)\\n# ============================================================\\n#\\n# Primary novelty: 首次系统性实证分析 agent stagnation 检测中 structural vs\\n# semantic signal 的有效性。30 个结构特征达 0.995 in-domain / 0.967 cross-agent F1，\\n# 全面优于 NL embedding (0.906/0.751) 和 LLM-as-judge (+24.3pp)。\\n#\\n# 三层贡献：\\n# 1. Structural Signal Discovery (primary) — 改变社区对 agent monitoring 方法选型认知\\n# 2. LF Temporal Dynamics Analysis — 量化 LFs 时序角色 + agent-specific 迁移分析\\n# 3. TLM Negative Finding — 3 种实现 (TWV/HMM/lag-aware HMM) 均未超越 MV\\n#\\n# 方法论前驱（TLM negative finding 的参照）：\\n# 1. Safranchik AAAI 2020 (linked HMM) — NER-specific，BIO 约束，token-level\\n# 2. Sala NeurIPS 2019 (multi-resolution WS) — 处理分辨率不匹配，不建模 label transition\\n# 3. Nguyen ACL 2017 (HMM-Crowd) — crowdsourcing 场景，不是 programmatic LFs\\n#\\n# 核心差异化：不是 \\\"method paper proposing TLM\\\"，而是 \\\"empirical study revealing\\n# structural signals dominate stagnation detection, with temporal modeling as\\n# well-motivated negative finding\\\".\\n\", \"total_chars\": 23431, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01422VfevMQborSVbGVNceeT`</summary>

```json
{
  "project": "agent_progress_probe",
  "file": "paper_framing.md",
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
  "session_id": "1311e2e5-9af4-44d3-8961-4a2f79dde730",
  "uuid": "31166d16-7e8e-4439-86f0-bea96720971a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016iV8ChfDzEdb5s2Z8CUR1E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1105,
      "cache_read_input_tokens": 23563,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1105
      },
      "output_tokens": 73,
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

_source line 11 · 2026-05-14T22:04:02.735Z_

<details><summary>↩ Tool result · `toolu_01422VfevMQborSVbGVNceeT`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/paper_framing.md\", \"content\": \"# Paper Framing — agent_progress_probe\\n\\n## Target Venue\\n- Primary: EMNLP 2026 ARR (submission deadline: May 25, 2026; commitment: August 2, 2026)\\n- Format: Long paper (8 pages + appendix)\\n- Track: LLM Agents\\n- Paper type: **Empirical analysis paper**（D039 pivot: 从 method paper 转 empirical study）\\n- Fallback: ACL 2026 ARR August cycle (~August 15 deadline)\\n\\n## Core Claims (3 条) — D039 Pivot\\n\\n1. **Stagnation Signals Are Structural, Not Semantic (primary contribution)**: 系统性对比发现 agent stagnation 信号本质是结构性的——30 个结构特征（命令重复率、唯一命令比、文件 diff 频率等）在 in-domain (RF 0.9951) 和 cross-agent (GB 0.967) 都近完美预测停滞，全面优于 NL embedding probe (in-domain 0.906, cross-domain 0.751) 和 LLM-as-judge (+24.3pp)。Encoder-agnostic（3 个 encoder 均 >0.90）；最优窗口 k=5 (0.9309)；data scaling 10%→100% 单调递增。这揭示：(a) stagnation detection 不需要语义理解——简单结构特征已足够；(b) 结构特征天然跨 agent 迁移（不依赖 embedding domain adaptation）；(c) NL embedding 对 stagnation detection 无增量价值。**改变社区对 agent monitoring 方法选型的认知：从昂贵的表示学习转向轻量结构监控。** Gold set 验证 structural features 是否检测到真实 stagnation（非仅 circular eval artifact）是论文成立的关键。\\n\\n2. **LF Temporal Dynamics Are Systematic but Agent-Specific (analytical contribution)**: LFs 在 trajectory 上展现**系统性但 agent-specific 的**时序角色。SWE-Agent 上：cmd_rep leading (-1.87步)、file_diff concurrent (-1.2步)、OB lagging (+6.7步)。**OH 上 cmd_rep 角色反转**（从 leading 变 lagging +3.32步），而 file_diff（leading, -4.9步）和 OB（lagging, +18.1步）跨域一致。**消融验证：去掉 cmd_rep 后 OH F1 从 0.7512 飙升到 0.9272（+21.6pp）**，证明 cmd_rep 在 OH 上是噪声源而非信号。根因：cmd_rep 在 OH 上 92.3% firing rate + 71% FP，失去区分性。这揭示 LF 行为与 agent 架构之间的交互效应——为 weak supervision pipeline 在 sequential agent data 上的设计提供实证指导。同时量化 circular evaluation 问题：structural features 以 0.9951 F1 逆向工程 LF 标签，证明 LF-derived labels 上的高分不等于真实检测能力。\\n\\n3. **Temporal Label Model: A Well-Motivated Negative Finding (D039 negative result)**: 标准 data programming（majority vote）在 agent trajectory 上违反 i.i.d. 假设——LFs 产生系统性时序动态，这 motivate 了 temporal label model（TLM）的开发。然而，三种 TLM 实现**均未能超越简单 MV**：(a) **TWV（时序加权投票）**：绝大多数 σ 下有害（twv-ablation）；唯一微弱正向的 σ=2 训练的下游分类器全面劣化（in-domain -4.9pp, cross-agent -21.7pp, conf≥2 -1.8pp）(structural-on-twv)；(b) **HMM-TLM**：stagnation class overpredict；(c) **Lag-aware HMM**：仅追平 MV（0.8936）。**结论**：在当前 3-LF、低冲突（conf≥2 一致率 95.1%）的 regime 下，temporal alignment 的收益被噪声引入抵消。TWV 改变的主要是低置信标签，但改变方向是错的。这是对 \\\"i.i.d. violation → temporal model must help\\\" 这一直觉的重要否定，为未来 temporal label model 研究提供了关键约束条件。\\n\\n## Story Spine\\n\\n- **Problem**: LLM agents 在长期任务中频繁\\\"语义停滞\\\"——执行看似合理但集体无效的动作序列。每个动作可能非重复、局部合理，但整个窗口缺乏 goal-directed progress。现有方法要么检测结构性循环（漏掉语义多样的停滞），要么做 step-level scoring（丢失窗口内的时序动态），要么依赖 LLM 自我评估（高开销 + 受困模型的判断力受限）。\\n\\n- **Existing approaches & gaps**: (a) Cycle detectors（CDCS+CDSA, SpecRA, TrajAD）捕获重复/异常但漏掉语义多样的停滞；(b) Process Reward Models — **AgentPRM (Xi et al., ACM Web 2026, arxiv 2511.08325)** 是最直接的竞争者：用 TD/GAE 训练 step-level PRM 评估 \\\"promise and progress\\\"，但需要 outcome labels + RL pipeline，是 training signal 而非 monitoring tool。另有 PRM framework (arxiv 2502.10325)、ToolPRMBench (arxiv 2601.12294)、trajectory-level reward modeling (arxiv 2604.08178)。PRM 方向在 2025-2026 非常拥挤，我们的差异：**不需要 outcome labels**、**window-level 捕获 temporal dynamics**、**monitoring 而非 training**；(c) Self-reflection（Reflexion, LATS, Tree of Thoughts）依赖被困模型的自我评估，且是 intervention 而非 monitoring；(d) RL value functions (CodeRL) 需要 reward shaping；(e) **Agent monitoring 新方向**：\\\"Monitoring LLM Agents for Sequentially Contextual Harm\\\" (ICLR 2025 Workshop) 论证了 sequence-level monitoring 的必要性（单步分析不够）；\\\"Reliable Weak-to-Strong Monitoring\\\" (arxiv 2508.19461) 研究了弱模型监控强 agent，但关注 safety 而非 progress；(f) **Agent degradation benchmark**：SlopCodeBench (arxiv 2603.24755, 2026) 量化了 coding agent 在长期任务中的退化——verbosity 90% 轨迹上升、erosion 80%——为我们的 problem motivation 提供了最新实证。\\n\\n- **Our framing (D039 Pivot)**: Progress stagnation detection 的系统性实证研究。**三层贡献**：(1) **Structural Signal Discovery (primary)** — 系统性对比揭示 stagnation 信号本质是结构性的（结构特征 in-domain 0.9951, cross-domain 0.967），NL embedding 和 LLM-as-judge 均无增量——改变社区对 agent monitoring 方法选型的认知，从表示学习转向轻量结构监控；(2) **LF Temporal Dynamics Analysis** — 量化 LFs 在 agent trajectory 上的时序角色 + 跨 agent 迁移分析 + circular evaluation 问题的方法论贡献——为 sequential data 上的 weak supervision 提供实证指导；(3) **TLM Negative Finding** — 系统性测试三种 temporal label model 实现，均未超越 MV，提供重要的负面结果和 failure analysis——约束未来研究方向。\\n\\n- **Headline result template**: \\\"We present a systematic empirical study of progress stagnation detection in LLM agents through weak supervision. Our central finding is that stagnation signals are fundamentally structural: simple features (command repetition ratio, file diff frequency) achieve 0.995 in-domain and 0.967 cross-agent F1, decisively surpassing both neural embedding approaches (0.906/0.751) and LLM-as-judge baselines. We further discover that labeling functions exhibit systematic temporal dynamics — command_repetition leads stagnation onset by ~1.87 steps while outcome_backpropagation lags by +6.7 steps — but these temporal roles are agent-specific (cmd_rep reverses from leading to lagging on OpenHands; removing it improves OH F1 by +21.6pp). Despite these well-characterized temporal patterns motivating a temporal label model, three implementations (TWV, HMM, lag-aware HMM) all fail to improve over simple majority vote — with TWV labels actually degrading downstream classifiers by up to 21.7pp. This negative finding reveals that in the low-conflict regime of current LF frameworks, temporal alignment introduces more noise than signal. Our results redirect agent monitoring from expensive representation learning and complex label models toward lightweight structural approaches.\\\"\\n\\n## Venue Fit Risks\\n\\n- **EMNLP vs ICSE**: 核心 LFs 和数据 100% 来自 SE 领域。贴合 NLP venue 的策略：(a) weak supervision on sequential data 是通用方法论，适用于任何有时序结构的标注场景——data programming / Snorkel 出自 NLP 社区；(b) structural vs semantic signal 的发现对任何 agent monitoring 系统有指导意义；(c) circular evaluation 问题是 weak supervision 评估的通用挑战；(d) TLM negative finding 对 sequential label model 研究有方法论价值。\\n- **Reviewer lottery**: 遇到 SE-skeptical 的 NLP reviewer 可能被判 \\\"more suitable for ICSE/FSE\\\"——通过强化方法论洞见的跨域普适性和 LLM agent 社区的 NLP 属性来降低风险。\\n- **\\\"Negative finding paper 不够 novel\\\"**: 论文不是纯 negative finding——structural signal discovery (Claim 1) 是强正面结果；TLM negative finding (Claim 3) 附带详细 failure analysis 和对未来研究的约束条件。EMNLP 接受 analysis paper 和 well-motivated negative results。\\n- **vs PRMs（2025-2026 最拥挤的方向）**: Related Work 加专门小节。核心定位差异：PRM 需要 outcome labels + RL pipeline（昂贵），我们是 monitoring tool + weak supervision pipeline（轻量）；PRM 是 step-level training signal，我们是 window-level detection。\\n- **\\\"Why not LLM-as-judge?\\\"**: 已有 baseline 对比——structural approach <5ms inference vs LLM 高开销，且 structural +24.3pp。\\n\\n## Anticipated Reviewer Concerns & Countermeasures\\n\\n| Concern | 应对 |\\n|---------|------|\\n| Circular evaluation（训练和评估都在自动标签上） | 多层防御：(1) 明确声明 F1 = LF consensus fidelity；(2) structural baseline 0.9951 量化 circularity 上界（逆向工程 LF 规则）；(3) Cross-domain OH 是 non-circular 评估；(4) **Gold set 人工标注**（650 窗口，关键路径） |\\n| Structural features outperform everything — so what's the point of the probe? | 诚实报告 + 解读：structural features 在 LF-derived labels 上的 0.9951 是 circularity 上界（features ≈ LF inputs, labels = LF outputs）。Probe 的独立价值在 non-circular 维度：real-time inference、end-to-end deployment、gold set 上的对比。Gold set 是最终裁判 |\\n| TLM negative finding 不够有 contribution | Failure analysis 详细到足以约束未来研究：(1) 3-LF 低冲突 regime（conf≥2 一致率 95.1%）限制了 temporal alignment 的改进空间；(2) TWV 在低置信区改变标签方向错误；(3) 三种不同实现排除了实现偏差。论文同时有强正面结果（Claim 1, 2） |\\n| 跨 agent 迁移只测了两个 SE agent | Two-agent scope 在 Limitations 讨论 + structural features 跨域 0.967 的强迁移证据。Future work 包含 non-SE agents |\\n| 为什么不直接用 LLM | LLM-as-judge baseline 已对比：structural RF +33.3pp、probe +24.3pp vs LLM、<5ms vs LLM 高开销 |\\n| outcome_backpropagation 信息泄露 | 3-seed holdout：移除 OB 后 f1_stag=0.641±0.034（-22pp），7.1pp 为纯信号贡献。OB 作为 \\\"Privileged Distant Supervision\\\"，在 3-LF 框架中不可替代 |\\n| Probe 只学了 LF 启发式 | LF oracle baseline（All-Agreement 0.854, probe +5.1pp）+ 错误分析（FP 65% = LF 未覆盖的语义多样停滞）+ gold set 最终验证 |\\n| Architecture novelty 不足 | 论文定位为 empirical analysis paper，novelty 在发现和方法论洞见，不在架构 |\\n| \\\"Semantic stagnation\\\" rebrands existing concepts | 明确映射到现有 agent failure mode taxonomy + window-level formulation 的特殊性论证 |\\n| Related work incomplete | 扩展到 30+ references：PRMs / agent self-reflection / weak supervision / agent degradation benchmarks |\\n| Embedding model unspecified | 具名 Qwen3-Embedding-0.6B + encoder ablation（BGE/E5/GTE，三者均 >0.90） |\\n| LF hold-one-out ablation 解读 | **禁止 \\\"去掉 X 后 F1 更高\\\" 的 claim**（test set 偏移假象）。正确框架：覆盖率贡献 + 跨集泛化 + 标签一致性 |\\n| Structural data scaling 不能表述为 \\\"robustness to data scarcity\\\" | Circular eval 框架下正确解读：结构特征 ≈ LF 输入，10% 数据即可学会 LF→label 映射（RF 0.991）。这是 LF 重建的简单性证据，不是检测鲁棒性。论文呈现时标注 $^\\\\dagger$ circular caveat，与 probe 的 data scaling（0.805→0.906，真正的学习曲线）对比呈现 |\\n| OB 移除后 f1_stag 数字来源 | ✅ **已闭环**：outcome-bp-3seed 3-seed mean f1_stag=0.641±0.034（seeds 42/123/456: 0.600/0.640/0.683）。\\\"0.000\\\" 来源已溯清：woob 模型在 OB-only 窗口子集（687w）上全预测 progress 导致子集 f1_stag=0.000，非完整测试集结果。D025/D026 已正确撤回。 |\\n\\n## D039 Pivot 变更记录\\n- D034 → D039: Claim 1 TLM（原\\\"论文最强 claim\\\"）降级为 Claim 3 negative finding\\n- D034 → D039: Claim 2 structural signal 升级为 Claim 1 primary contribution\\n- D034 → D039: Claim 3 LF temporal → Claim 2，加入 circular eval methodology\\n- D039 新增: TLM 三种实现全败的 failure analysis 作为独立贡献\\n- D039 触发实验: structural-on-twv (TWV labels degrade downstream -4.9pp ~ -21.7pp) + twv-ablation (TWV harmful for most σ) + temporal-label-model (HMM/lag-aware HMM failed)\", \"total_chars\": 9408, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1311e2e5-9af4-44d3-8961-4a2f79dde730",
  "uuid": "2cee02d6-c44b-4503-b738-7b114e7a2e00",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing — agent_progress_probe\\\\n\\\\n## Target Venue\\\\n- Primary: EMNLP 2026 ARR (submission deadline: May 25, 2026; commitment: August 2, 2026)\\\\n- Format: Long paper (8 pages + appendix)\\\\n- Track: LLM Agents\\\\n- Paper type: **Empirical analysis paper**（D039 pivot: 从 method paper 转 empirical study）\\\\n- Fallback: ACL 2026 ARR August cycle (~August 15 deadline)\\\\n\\\\n## Core Claims (3 条) — D039 Pivot\\\\n\\\\n1. **Stagnation Signals Are Structural, Not Semantic (primary contribution)**: 系统性对比发现 agent stagnation 信号本质是结构性的——30 个结构特征（命令重复率、唯一命令比、文件 diff 频率等）在 in-domain (RF 0.9951) 和 cross-agent (GB 0.967) 都近完美预测停滞，全面优于 NL embedding probe (in-domain 0.906, cross-domain 0.751) 和 LLM-as-judge (+24.3pp)。Encoder-agnostic（3 个 encoder 均 >0.90）；最优窗口 k=5 (0.9309)；data scaling 10%→100% 单调递增。这揭示：(a) stagnation detection 不需要语义理解——简单结构特征已足够；(b) 结构特征天然跨 agent 迁移（不依赖 embedding domain adaptation）；(c) NL embedding 对 stagnation detection 无增量价值。**改变社区对 agent monitoring 方法选型的认知：从昂贵的表示学习转向轻量结构监控。** Gold set 验证 structural features 是否检测到真实 stagnation（非仅 circular eval artifact）是论文成立的关键。\\\\n\\\\n2. **LF Temporal Dynamics Are Systematic but Agent-Specific (analytical contribution)**: LFs 在 trajectory 上展现**系统性但 agent-specific 的**时序角色。SWE-Agent 上：cmd_rep leading (-1.87步)、file_diff concurrent (-1.2步)、OB lagging (+6.7步)。**OH 上 cmd_rep 角色反转**（从 leading 变 lagging +3.32步），而 file_diff（leading, -4.9步）和 OB（lagging, +18.1步）跨域一致。**消融验证：去掉 cmd_rep 后 OH F1 从 0.7512 飙升到 0.9272（+21.6pp）**，证明 cmd_rep 在 OH 上是噪声源而非信号。根因：cmd_rep 在 OH 上 92.3% firing rate + 71% FP，失去区分性。这揭示 LF 行为与 agent 架构之间的交互效应——为 weak supervision pipeline 在 sequential agent data 上的设计提供实证指导。同时量化 circular evaluation 问题：structural features 以 0.9951 F1 逆向工程 LF 标签，证明 LF-derived labels 上的高分不等于真实检测能力。\\\\n\\\\n3. **Temporal Label Model: A Well-Motivated Negative Finding (D039 negative result)**: 标准 data programming（majority vote）在 agent trajectory 上违反 i.i.d. 假设——LFs 产生系统性时序动态，这 motivate 了 temporal label model（TLM）的开发。然而，三种 TLM 实现**均未能超越简单 MV**：(a) **TWV（时序加权投票）**：绝大多数 σ 下有害（twv-ablation）；唯一微弱正向的 σ=2 训练的下游分类器全面劣化（in-domain -4.9pp, cross-agent -21.7pp, conf≥2 -1.8pp）(structural-on-twv)；(b) **HMM-TLM**：stagnation class overpredict；(c) **Lag-aware HMM**：仅追平 MV（0.8936）。**结论**：在当前 3-LF、低冲突（conf≥2 一致率 95.1%）的 regime 下，temporal alignment 的收益被噪声引入抵消。TWV 改变的主要是低置信标签，但改变方向是错的。这是对 \\\\\\\"i.i.d. violation → temporal model must help\\\\\\\" 这一直觉的重要否定，为未来 temporal label model 研究提供了关键约束条件。\\\\n\\\\n## Story Spine\\\\n\\\\n- **Problem**: LLM agents 在长期任务中频繁\\\\\\\"语义停滞\\\\\\\"——执行看似合理但集体无效的动作序列。每个动作可能非重复、局部合理，但整个窗口缺乏 goal-directed progress。现有方法要么检测结构性循环（漏掉语义多样的停滞），要么做 step-level scoring（丢失窗口内的时序动态），要么依赖 LLM 自我评估（高开销 + 受困模型的判断力受限）。\\\\n\\\\n- **Existing approaches & gaps**: (a) Cycle detectors（CDCS+CDSA, SpecRA, TrajAD）捕获重复/异常但漏掉语义多样的停滞；(b) Process Reward Models — **AgentPRM (Xi et al., ACM Web 2026, arxiv 2511.08325)** 是最直接的竞争者：用 TD/GAE 训练 step-level PRM 评估 \\\\\\\"promise and progress\\\\\\\"，但需要 outcome labels + RL pipeline，是 training signal 而非 monitoring tool。另有 PRM framework (arxiv 2502.10325)、ToolPRMBench (arxiv 2601.12294)、trajectory-level reward modeling (arxiv 2604.08178)。PRM 方向在 2025-2026 非常拥挤，我们的差异：**不需要 outcome labels**、**window-level 捕获 temporal dynamics**、**monitoring 而非 training**；(c) Self-reflection（Reflexion, LATS, Tree of Thoughts）依赖被困模型的自我评估，且是 intervention 而非 monitoring；(d) RL value functions (CodeRL) 需要 reward shaping；(e) **Agent monitoring 新方向**：\\\\\\\"Monitoring LLM Agents for Sequentially Contextual Harm\\\\\\\" (ICLR 2025 Workshop) 论证了 sequence-level monitoring 的必要性（单步分析不够）；\\\\\\\"Reliable Weak-to-Strong Monitoring\\\\\\\" (arxiv 2508.19461) 研究了弱模型监控强 agent，但关注 safety 而非 progress；(f) **Agent degradation benchmark**：SlopCodeBench (arxiv 2603.24755, 2026) 量化了 coding agent 在长期任务中的退化——verbosity 90% 轨迹上升、erosion 80%——为我们的 problem motivation 提供了最新实证。\\\\n\\\\n- **Our framing (D039 Pivot)**: Progress stagnation detection 的系统性实证研究。**三层贡献**：(1) **Structural Signal Discovery (primary)** — 系统性对比揭示 stagnation 信号本质是结构性的（结构特征 in-domain 0.9951, cross-domain 0.967），NL embedding 和 LLM-as-judge 均无增量——改变社区对 agent monitoring 方法选型的认知，从表示学习转向轻量结构监控；(2) **LF Temporal Dynamics Analysis** — 量化 LFs 在 agent trajectory 上的时序角色 + 跨 agent 迁移分析 + circular evaluation 问题的方法论贡献——为 sequential data 上的 weak supervision 提供实证指导；(3) **TLM Negative Finding** — 系统性测试三种 temporal label model 实现，均未超越 MV，提供重要的负面结果和 failure analysis——约束未来研究方向。\\\\n\\\\n- **Headline result template**: \\\\\\\"We present a systematic empirical study of progress stagnation detection in LLM agents through weak supervision. Our central finding is that stagnation signals are fundamentally structural: simple features (command repetition ratio, file diff frequency) achieve 0.995 in-domain and 0.967 cross-agent F1, decisively surpassing both neural embedding approaches (0.906/0.751) and LLM-as-judge baselines. We further discover that labeling functions exhibit systematic temporal dynamics — command_repetition leads stagnation onset by ~1.87 steps while outcome_backpropagation lags by +6.7 steps — but these temporal roles are agent-specific (cmd_rep reverses from leading to lagging on OpenHands; removing it improves OH F1 by +21.6pp). Despite these well-characterized temporal patterns motivating a temporal label model, three implementations (TWV, HMM, lag-aware HMM) all fail to improve over simple majority vote — with TWV labels actually degrading downstream classifiers by up to 21.7pp. This negative finding reveals that in the low-conflict regime of current LF frameworks, temporal alignment introduces more noise than signal. Our results redirect agent monitoring from expensive representation learning and complex label models toward lightweight structural approaches.\\\\\\\"\\\\n\\\\n## Venue Fit Risks\\\\n\\\\n- **EMNLP vs ICSE**: 核心 LFs 和数据 100% 来自 SE 领域。贴合 NLP venue 的策略：(a) weak supervision on sequential data 是通用方法论，适用于任何有时序结构的标注场景——data programming / Snorkel 出自 NLP 社区；(b) structural vs semantic signal 的发现对任何 agent monitoring 系统有指导意义；(c) circular evaluation 问题是 weak supervision 评估的通用挑战；(d) TLM negative finding 对 sequential label model 研究有方法论价值。\\\\n- **Reviewer lottery**: 遇到 SE-skeptical 的 NLP reviewer 可能被判 \\\\\\\"more suitable for ICSE/FSE\\\\\\\"——通过强化方法论洞见的跨域普适性和 LLM agent 社区的 NLP 属性来降低风险。\\\\n- **\\\\\\\"Negative finding paper 不够 novel\\\\\\\"**: 论文不是纯 negative finding——structural signal discovery (Claim 1) 是强正面结果；TLM negative finding (Claim 3) 附带详细 failure analysis 和对未来研究的约束条件。EMNLP 接受 analysis paper 和 well-motivated negative results。\\\\n- **vs PRMs（2025-2026 最拥挤的方向）**: Related Work 加专门小节。核心定位差异：PRM 需要 outcome labels + RL pipeline（昂贵），我们是 monitoring tool + weak supervision pipeline（轻量）；PRM 是 step-level training signal，我们是 window-level detection。\\\\n- **\\\\\\\"Why not LLM-as-judge?\\\\\\\"**: 已有 baseline 对比——structural approach <5ms inference vs LLM 高开销，且 structural +24.3pp。\\\\n\\\\n## Anticipated Reviewer Concerns & Countermeasures\\\\n\\\\n| Concern | 应对 |\\\\n|---------|------|\\\\n| Circular evaluation（训练和评估都在自动标签上） | 多层防御：(1) 明确声明 F1 = LF consensus fidelity；(2) structural baseline 0.9951 量化 circularity 上界（逆向工程 LF 规则）；(3) Cross-domain OH 是 non-circular 评估；(4) **Gold set 人工标注**（650 窗口，关键路径） |\\\\n| Structural features outperform everything — so what's the point of the probe? | 诚实报告 + 解读：structural features 在 LF-derived labels 上的 0.9951 是 circularity 上界（features ≈ LF inputs, labels = LF outputs）。Probe 的独立价值在 non-circular 维度：real-time inference、end-to-end deployment、gold set 上的对比。Gold set 是最终裁判 |\\\\n| TLM negative finding 不够有 contribution | Failure analysis 详细到足以约束未来研究：(1) 3-LF 低冲突 regime（conf≥2 一致率 95.1%）限制了 temporal alignment 的改进空间；(2) TWV 在低置信区改变标签方向错误；(3) 三种不同实现排除了实现偏差。论文同时有强正面结果（Claim 1, 2） |\\\\n| 跨 agent 迁移只测了两个 SE agent | Two-agent scope 在 Limitations 讨论 + structural features 跨域 0.967 的强迁移证据。Future work 包含 non-SE agents |\\\\n| 为什么不直接用 LLM | LLM-as-judge baseline 已对比：structural RF +33.3pp、probe +24.3pp vs LLM、<5ms vs LLM 高开销 |\\\\n| outcome_backpropagation 信息泄露 | 3-seed holdout：移除 OB 后 f1_stag=0.641±0.034（-22pp），7.1pp 为纯信号贡献。OB 作为 \\\\\\\"Privileged Distant Supervision\\\\\\\"，在 3-LF 框架中不可替代 |\\\\n| Probe 只学了 LF 启发式 | LF oracle baseline（All-Agreement 0.854, probe +5.1pp）+ 错误分析（FP 65% = LF 未覆盖的语义多样停滞）+ gold set 最终验证 |\\\\n| Architecture novelty 不足 | 论文定位为 empirical analysis paper，novelty 在发现和方法论洞见，不在架构 |\\\\n| \\\\\\\"Semantic stagnation\\\\\\\" rebrands existing concepts | 明确映射到现有 agent failure mode taxonomy + window-level formulation 的特殊性论证 |\\\\n| Related work incomplete | 扩展到 30+ references：PRMs / agent self-reflection / weak supervision / agent degradation benchmarks |\\\\n| Embedding model unspecified | 具名 Qwen3-Embedding-0.6B + encoder ablation（BGE/E5/GTE，三者均 >0.90） |\\\\n| LF hold-one-out ablation 解读 | **禁止 \\\\\\\"去掉 X 后 F1 更高\\\\\\\" 的 claim**（test set 偏移假象）。正确框架：覆盖率贡献 + 跨集泛化 + 标签一致性 |\\\\n| Structural data scaling 不能表述为 \\\\\\\"robustness to data scarcity\\\\\\\" | Circular eval 框架下正确解读：结构特征 ≈ LF 输入，10% 数据即可学会 LF→label 映射（RF 0.991）。这是 LF 重建的简单性证据，不是检测鲁棒性。论文呈现时标注 $^\\\\\\\\dagger$ circular caveat，与 probe 的 data scaling（0.805→0.906，真正的学习曲线）对比呈现 |\\\\n| OB 移除后 f1_stag 数字来源 | ✅ **已闭环**：outcome-bp-3seed 3-seed mean f1_stag=0.641±0.034（seeds 42/123/456: 0.600/0.640/0.683）。\\\\\\\"0.000\\\\\\\" 来源已溯清：woob 模型在 OB-only 窗口子集（687w）上全预测 progress 导致子集 f1_stag=0.000，非完整测试集结果。D025/D026 已正确撤回。 |\\\\n\\\\n## D039 Pivot 变更记录\\\\n- D034 → D039: Claim 1 TLM（原\\\\\\\"论文最强 claim\\\\\\\"）降级为 Claim 3 negative finding\\\\n- D034 → D039: Claim 2 structural signal 升级为 Claim 1 primary contribution\\\\n- D034 → D039: Claim 3 LF temporal → Claim 2，加入 circular eval methodology\\\\n- D039 新增: TLM 三种实现全败的 failure analysis 作为独立贡献\\\\n- D039 触发实验: structural-on-twv (TWV labels degrade downstream -4.9pp ~ -21.7pp) + twv-ablation (TWV harmful for most σ) + temporal-label-model (HMM/lag-aware HMM failed)\\\", \\\"total_chars\\\": 9408, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/paper_framing.md\", \"content\": \"# Paper Framing — agent_progress_probe\\n\\n## Target Venue\\n- Primary: EMNLP 2026 ARR (submission deadline: May 25, 2026; commitment: August 2, 2026)\\n- Format: Long paper (8 pages + appendix)\\n- Track: LLM Agents\\n- Paper type: **Empirical analysis paper**（D039 pivot: 从 method paper 转 empirical study）\\n- Fallback: ACL 2026 ARR August cycle (~August 15 deadline)\\n\\n## Core Claims (3 条) — D039 Pivot\\n\\n1. **Stagnation Signals Are Structural, Not Semantic (primary contribution)**: 系统性对比发现 agent stagnation 信号本质是结构性的——30 个结构特征（命令重复率、唯一命令比、文件 diff 频率等）在 in-domain (RF 0.9951) 和 cross-agent (GB 0.967) 都近完美预测停滞，全面优于 NL embedding probe (in-domain 0.906, cross-domain 0.751) 和 LLM-as-judge (+24.3pp)。Encoder-agnostic（3 个 encoder 均 >0.90）；最优窗口 k=5 (0.9309)；data scaling 10%→100% 单调递增。这揭示：(a) stagnation detection 不需要语义理解——简单结构特征已足够；(b) 结构特征天然跨 agent 迁移（不依赖 embedding domain adaptation）；(c) NL embedding 对 stagnation detection 无增量价值。**改变社区对 agent monitoring 方法选型的认知：从昂贵的表示学习转向轻量结构监控。** Gold set 验证 structural features 是否检测到真实 stagnation（非仅 circular eval artifact）是论文成立的关键。\\n\\n2. **LF Temporal Dynamics Are Systematic but Agent-Specific (analytical contribution)**: LFs 在 trajectory 上展现**系统性但 agent-specific 的**时序角色。SWE-Agent 上：cmd_rep leading (-1.87步)、file_diff concurrent (-1.2步)、OB lagging (+6.7步)。**OH 上 cmd_rep 角色反转**（从 leading 变 lagging +3.32步），而 file_diff（leading, -4.9步）和 OB（lagging, +18.1步）跨域一致。**消融验证：去掉 cmd_rep 后 OH F1 从 0.7512 飙升到 0.9272（+21.6pp）**，证明 cmd_rep 在 OH 上是噪声源而非信号。根因：cmd_rep 在 OH 上 92.3% firing rate + 71% FP，失去区分性。这揭示 LF 行为与 agent 架构之间的交互效应——为 weak supervision pipeline 在 sequential agent data 上的设计提供实证指导。同时量化 circular evaluation 问题：structural features 以 0.9951 F1 逆向工程 LF 标签，证明 LF-derived labels 上的高分不等于真实检测能力。\\n\\n3. **Temporal Label Model: A Well-Motivated Negative Finding (D039 negative result)**: 标准 data programming（majority vote）在 agent trajectory 上违反 i.i.d. 假设——LFs 产生系统性时序动态，这 motivate 了 temporal label model（TLM）的开发。然而，三种 TLM 实现**均未能超越简单 MV**：(a) **TWV（时序加权投票）**：绝大多数 σ 下有害（twv-ablation）；唯一微弱正向的 σ=2 训练的下游分类器全面劣化（in-domain -4.9pp, cross-agent -21.7pp, conf≥2 -1.8pp）(structural-on-twv)；(b) **HMM-TLM**：stagnation class overpredict；(c) **Lag-aware HMM**：仅追平 MV（0.8936）。**结论**：在当前 3-LF、低冲突（conf≥2 一致率 95.1%）的 regime 下，temporal alignment 的收益被噪声引入抵消。TWV 改变的主要是低置信标签，但改变方向是错的。这是对 \\\"i.i.d. violation → temporal model must help\\\" 这一直觉的重要否定，为未来 temporal label model 研究提供了关键约束条件。\\n\\n## Story Spine\\n\\n- **Problem**: LLM agents 在长期任务中频繁\\\"语义停滞\\\"——执行看似合理但集体无效的动作序列。每个动作可能非重复、局部合理，但整个窗口缺乏 goal-directed progress。现有方法要么检测结构性循环（漏掉语义多样的停滞），要么做 step-level scoring（丢失窗口内的时序动态），要么依赖 LLM 自我评估（高开销 + 受困模型的判断力受限）。\\n\\n- **Existing approaches & gaps**: (a) Cycle detectors（CDCS+CDSA, SpecRA, TrajAD）捕获重复/异常但漏掉语义多样的停滞；(b) Process Reward Models — **AgentPRM (Xi et al., ACM Web 2026, arxiv 2511.08325)** 是最直接的竞争者：用 TD/GAE 训练 step-level PRM 评估 \\\"promise and progress\\\"，但需要 outcome labels + RL pipeline，是 training signal 而非 monitoring tool。另有 PRM framework (arxiv 2502.10325)、ToolPRMBench (arxiv 2601.12294)、trajectory-level reward modeling (arxiv 2604.08178)。PRM 方向在 2025-2026 非常拥挤，我们的差异：**不需要 outcome labels**、**window-level 捕获 temporal dynamics**、**monitoring 而非 training**；(c) Self-reflection（Reflexion, LATS, Tree of Thoughts）依赖被困模型的自我评估，且是 intervention 而非 monitoring；(d) RL value functions (CodeRL) 需要 reward shaping；(e) **Agent monitoring 新方向**：\\\"Monitoring LLM Agents for Sequentially Contextual Harm\\\" (ICLR 2025 Workshop) 论证了 sequence-level monitoring 的必要性（单步分析不够）；\\\"Reliable Weak-to-Strong Monitoring\\\" (arxiv 2508.19461) 研究了弱模型监控强 agent，但关注 safety 而非 progress；(f) **Agent degradation benchmark**：SlopCodeBench (arxiv 2603.24755, 2026) 量化了 coding agent 在长期任务中的退化——verbosity 90% 轨迹上升、erosion 80%——为我们的 problem motivation 提供了最新实证。\\n\\n- **Our framing (D039 Pivot)**: Progress stagnation detection 的系统性实证研究。**三层贡献**：(1) **Structural Signal Discovery (primary)** — 系统性对比揭示 stagnation 信号本质是结构性的（结构特征 in-domain 0.9951, cross-domain 0.967），NL embedding 和 LLM-as-judge 均无增量——改变社区对 agent monitoring 方法选型的认知，从表示学习转向轻量结构监控；(2) **LF Temporal Dynamics Analysis** — 量化 LFs 在 agent trajectory 上的时序角色 + 跨 agent 迁移分析 + circular evaluation 问题的方法论贡献——为 sequential data 上的 weak supervision 提供实证指导；(3) **TLM Negative Finding** — 系统性测试三种 temporal label model 实现，均未超越 MV，提供重要的负面结果和 failure analysis——约束未来研究方向。\\n\\n- **Headline result template**: \\\"We present a systematic empirical study of progress stagnation detection in LLM agents through weak supervision. Our central finding is that stagnation signals are fundamentally structural: simple features (command repetition ratio, file diff frequency) achieve 0.995 in-domain and 0.967 cross-agent F1, decisively surpassing both neural embedding approaches (0.906/0.751) and LLM-as-judge baselines. We further discover that labeling functions exhibit systematic temporal dynamics — command_repetition leads stagnation onset by ~1.87 steps while outcome_backpropagation lags by +6.7 steps — but these temporal roles are agent-specific (cmd_rep reverses from leading to lagging on OpenHands; removing it improves OH F1 by +21.6pp). Despite these well-characterized temporal patterns motivating a temporal label model, three implementations (TWV, HMM, lag-aware HMM) all fail to improve over simple majority vote — with TWV labels actually degrading downstream classifiers by up to 21.7pp. This negative finding reveals that in the low-conflict regime of current LF frameworks, temporal alignment introduces more noise than signal. Our results redirect agent monitoring from expensive representation learning and complex label models toward lightweight structural approaches.\\\"\\n\\n## Venue Fit Risks\\n\\n- **EMNLP vs ICSE**: 核心 LFs 和数据 100% 来自 SE 领域。贴合 NLP venue 的策略：(a) weak supervision on sequential data 是通用方法论，适用于任何有时序结构的标注场景——data programming / Snorkel 出自 NLP 社区；(b) structural vs semantic signal 的发现对任何 agent monitoring 系统有指导意义；(c) circular evaluation 问题是 weak supervision 评估的通用挑战；(d) TLM negative finding 对 sequential label model 研究有方法论价值。\\n- **Reviewer lottery**: 遇到 SE-skeptical 的 NLP reviewer 可能被判 \\\"more suitable for ICSE/FSE\\\"——通过强化方法论洞见的跨域普适性和 LLM agent 社区的 NLP 属性来降低风险。\\n- **\\\"Negative finding paper 不够 novel\\\"**: 论文不是纯 negative finding——structural signal discovery (Claim 1) 是强正面结果；TLM negative finding (Claim 3) 附带详细 failure analysis 和对未来研究的约束条件。EMNLP 接受 analysis paper 和 well-motivated negative results。\\n- **vs PRMs（2025-2026 最拥挤的方向）**: Related Work 加专门小节。核心定位差异：PRM 需要 outcome labels + RL pipeline（昂贵），我们是 monitoring tool + weak supervision pipeline（轻量）；PRM 是 step-level training signal，我们是 window-level detection。\\n- **\\\"Why not LLM-as-judge?\\\"**: 已有 baseline 对比——structural approach <5ms inference vs LLM 高开销，且 structural +24.3pp。\\n\\n## Anticipated Reviewer Concerns & Countermeasures\\n\\n| Concern | 应对 |\\n|---------|------|\\n| Circular evaluation（训练和评估都在自动标签上） | 多层防御：(1) 明确声明 F1 = LF consensus fidelity；(2) structural baseline 0.9951 量化 circularity 上界（逆向工程 LF 规则）；(3) Cross-domain OH 是 non-circular 评估；(4) **Gold set 人工标注**（650 窗口，关键路径） |\\n| Structural features outperform everything — so what's the point of the probe? | 诚实报告 + 解读：structural features 在 LF-derived labels 上的 0.9951 是 circularity 上界（features ≈ LF inputs, labels = LF outputs）。Probe 的独立价值在 non-circular 维度：real-time inference、end-to-end deployment、gold set 上的对比。Gold set 是最终裁判 |\\n| TLM negative finding 不够有 contribution | Failure analysis 详细到足以约束未来研究：(1) 3-LF 低冲突 regime（conf≥2 一致率 95.1%）限制了 temporal alignment 的改进空间；(2) TWV 在低置信区改变标签方向错误；(3) 三种不同实现排除了实现偏差。论文同时有强正面结果（Claim 1, 2） |\\n| 跨 agent 迁移只测了两个 SE agent | Two-agent scope 在 Limitations 讨论 + structural features 跨域 0.967 的强迁移证据。Future work 包含 non-SE agents |\\n| 为什么不直接用 LLM | LLM-as-judge baseline 已对比：structural RF +33.3pp、probe +24.3pp vs LLM、<5ms vs LLM 高开销 |\\n| outcome_backpropagation 信息泄露 | 3-seed holdout：移除 OB 后 f1_stag=0.641±0.034（-22pp），7.1pp 为纯信号贡献。OB 作为 \\\"Privileged Distant Supervision\\\"，在 3-LF 框架中不可替代 |\\n| Probe 只学了 LF 启发式 | LF oracle baseline（All-Agreement 0.854, probe +5.1pp）+ 错误分析（FP 65% = LF 未覆盖的语义多样停滞）+ gold set 最终验证 |\\n| Architecture novelty 不足 | 论文定位为 empirical analysis paper，novelty 在发现和方法论洞见，不在架构 |\\n| \\\"Semantic stagnation\\\" rebrands existing concepts | 明确映射到现有 agent failure mode taxonomy + window-level formulation 的特殊性论证 |\\n| Related work incomplete | 扩展到 30+ references：PRMs / agent self-reflection / weak supervision / agent degradation benchmarks |\\n| Embedding model unspecified | 具名 Qwen3-Embedding-0.6B + encoder ablation（BGE/E5/GTE，三者均 >0.90） |\\n| LF hold-one-out ablation 解读 | **禁止 \\\"去掉 X 后 F1 更高\\\" 的 claim**（test set 偏移假象）。正确框架：覆盖率贡献 + 跨集泛化 + 标签一致性 |\\n| Structural data scaling 不能表述为 \\\"robustness to data scarcity\\\" | Circular eval 框架下正确解读：结构特征 ≈ LF 输入，10% 数据即可学会 LF→label 映射（RF 0.991）。这是 LF 重建的简单性证据，不是检测鲁棒性。论文呈现时标注 $^\\\\dagger$ circular caveat，与 probe 的 data scaling（0.805→0.906，真正的学习曲线）对比呈现 |\\n| OB 移除后 f1_stag 数字来源 | ✅ **已闭环**：outcome-bp-3seed 3-seed mean f1_stag=0.641±0.034（seeds 42/123/456: 0.600/0.640/0.683）。\\\"0.000\\\" 来源已溯清：woob 模型在 OB-only 窗口子集（687w）上全预测 progress 导致子集 f1_stag=0.000，非完整测试集结果。D025/D026 已正确撤回。 |\\n\\n## D039 Pivot 变更记录\\n- D034 → D039: Claim 1 TLM（原\\\"论文最强 claim\\\"）降级为 Claim 3 negative finding\\n- D034 → D039: Claim 2 structural signal 升级为 Claim 1 primary contribution\\n- D034 → D039: Claim 3 LF temporal → Claim 2，加入 circular eval methodology\\n- D039 新增: TLM 三种实现全败的 failure analysis 作为独立贡献\\n- D039 触发实验: structural-on-twv (TWV labels degrade downstream -4.9pp ~ -21.7pp) + twv-ablation (TWV harmful for most σ) + temporal-label-model (HMM/lag-aware HMM failed)\", \"total_chars\": 9408, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_01D7yvxdVn9WBtM6KTK8rtpk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1311e2e5-9af4-44d3-8961-4a2f79dde730",
  "uuid": "4f1341ac-59d8-47fc-96b3-88c9ee386e62",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016iV8ChfDzEdb5s2Z8CUR1E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1105,
      "cache_read_input_tokens": 23563,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1105
      },
      "output_tokens": 73,
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

_source line 13 · 2026-05-14T22:04:03.454Z_

<details><summary>↩ Tool result · `toolu_01D7yvxdVn9WBtM6KTK8rtpk`</summary>

```text
1	% Introduction: Structural stagnation detection in LLM coding agents (EMNLP 2026 ARR)
2	\section{Introduction}
3	\label{sec:introduction}
4	
5	Large language model (LLM) agents are increasingly deployed for complex, long-horizon software engineering tasks---resolving GitHub issues, debugging production systems, and iterating on code across multiple rounds of edits \citep{jimenez2024swebench,yang2024sweagent,wang2025openhands}.
6	As task complexity grows, a critical failure mode emerges that is qualitatively different from crashes or syntax errors: the agent \emph{stagnates}---continuing to produce actions that appear diverse on the surface while making no meaningful progress toward the task goal.
7	\citet{orlanski2026slopcodebench} systematically document this degradation in long-horizon coding tasks, finding structural erosion in 77\% of agent trajectories and verbosity increases in 75.5\%, with no agent fully solving any benchmark problem end-to-end.
8	Unlike overt loops, stagnation is insidious: the agent issues varied commands, edits different files, and generates plausible-looking outputs, yet its behavior is functionally stuck.
9	Detecting when an agent has entered this regime is essential for reliable deployment---enabling interventions such as early termination, strategy switching, or human escalation---yet identifying \emph{what signals} carry stagnation information, and whether complex language understanding is necessary to extract them, remains an open question.
10	
11	Prior approaches to monitoring agent behavior address aspects of this problem but none systematically investigate what information is needed for detection.
12	\emph{Repetition detectors} identify exact or near-exact loops in action sequences, catching the simplest failure mode but missing semantically diverse stagnation where the agent varies its surface behavior while remaining functionally stuck.
13	\emph{Process reward models} \citep{xi2025agentprm} assign quality scores to individual actions, enabling search-time guidance, but step-level granularity cannot capture temporal patterns that distinguish transient setbacks from sustained stagnation---a distinction that requires reasoning over windows of consecutive actions \textcolor{red}{[CITE: ICLR 2025 Workshop, Monitoring LLM Agents for Sequentially Contextual Harm]}.
14	\emph{Self-reflection} frameworks \citep{shinn2023reflexion,yao2023tot,zhou2024lats} rely on the agent itself to diagnose and recover from failures, but when the agent is genuinely stuck, self-diagnosis amounts to querying the failing model about its own failure---a circularity that limits reliability.
15	More fundamentally, all three lines of work prescribe detection \emph{methods} without first asking what kinds of signals actually carry stagnation information: does detecting subtle agent failure require sophisticated semantic understanding, or do simpler structural patterns suffice?
16	
17	We present an empirical analysis that addresses this gap.
18	Using a weak supervision framework \citep{ratner2016dataprogramming,ratner2017snorkel}, we construct silver-labeled datasets from trajectories of two architecturally distinct agents: SWE-Agent \citep{yang2024sweagent} on SWE-bench \citep{jimenez2024swebench} (54,809 windows) and OpenHands \citep{wang2025openhands} (150,652 windows).
19	Three labeling functions (LFs)---targeting command repetition, file modification patterns, and task outcome---provide noisy votes that are aggregated via majority vote into window-level binary labels.
20	Against these silver labels, we systematically compare three detection paradigms: hand-crafted structural features, neural embedding probes, and LLM-as-judge evaluation.
21	
22	Our central finding is that \textbf{stagnation signals are fundamentally structural, not semantic}.
23	Thirty hand-crafted features capturing command repetition rates, file operation counts, and edit distances achieve 0.9951 macro-F1 in-domain and 0.967 on zero-shot cross-agent transfer, exceeding the LLM judge by 33.3 percentage points (pp).
24	A GRU-based neural probe \citep{cho2014gru} over sentence embeddings reaches 0.906 in-domain but collapses to 0.528 on zero-shot transfer and recovers only to 0.751 after full fine-tuning on the target agent.
25	The structural advantage is encoder-agnostic: swapping the probe's embedding backbone across three encoders (Qwen3-0.6B, BGE-M3, E5-large-v2) yields probe F1 consistently above 0.90 \citep{zhang2025qwen3embedding,chen2024bgem3,wang2024e5}, confirming that the temporal architecture rather than a specific pretrained encoder drives embedding-based performance.
26	Critically, the gap between structural features and learned representations persists across agents with substantially different action distributions (28.5\% vs.\ 6.6\% stagnation rates), suggesting that stagnation manifests in action-level structure that generalizes without adaptation.
27	This challenges the prevailing intuition that detecting subtle agent failures requires complex language understanding, and suggests that lightweight structural monitoring---requiring no GPU and running in under 5\,ms per window---may be more practical than neural or LLM-based approaches for real-time agent oversight.
28	
29	Beyond static detection, we analyze the temporal dynamics of the labeling functions that generate silver labels.
30	On SWE-Agent, command repetition ($\lambda_1$) leads stagnation onset by 1.87 steps on average, serving as an early warning signal, while outcome backpropagation ($\lambda_3$) lags by 6.70 steps (Kruskal-Wallis $H{=}274.3$, $p{<}10^{-59}$).
31	However, this temporal structure is agent-specific: on OpenHands, $\lambda_1$ reverses from leading to lagging ($+3.32$ steps), firing on 92.3\% of windows with a 71\% false positive rate on progress windows.
32	Removing $\lambda_1$ from the OpenHands labeling pipeline improves fine-tuned probe F1 by 17.6\,pp, demonstrating that labeling functions validated on one agent architecture can become adversarial on another.
33	This finding establishes that LF temporal roles must be re-validated per agent and motivates the circular evaluation methodology we develop to surface such pathologies (\S\ref{sec:cmd_rep_ablation}).
34	
35	We further investigate whether encoding this temporal structure into label aggregation can improve over simple majority vote.
36	Three temporal label models---time-varying weights (TWV), Hidden Markov Models \citep{safranchik2020linkedhmm}, and lag-aware HMMs---all fail to surpass majority vote on downstream stagnation detection.
37	TWV achieves marginally higher self-evaluated F1 (+0.57\,pp) but degrades downstream probe performance by 2.57\,pp; the standard HMM overpredicts stagnation, dropping downstream F1 to 0.656.
38	This negative result demonstrates that temporal sophistication in label aggregation does not translate to better silver labels when base agreement among LFs is already high.
39	
40	Our contributions are:
41	\begin{enumerate}[leftmargin=*,itemsep=2pt]
42	    \item \textbf{Structural signal discovery.} We show that 30 structural features achieve near-perfect stagnation detection (0.9951 in-domain, 0.967 cross-agent macro-F1), outperforming neural probes and LLM judges by wide margins (+33.3\,pp over LLM-as-judge). To our knowledge, this is the first systematic comparison demonstrating that stagnation information resides in action-level structure rather than semantic content.
43	    \item \textbf{Labeling function temporal dynamics.} We reveal that LFs occupy statistically distinct temporal niches relative to stagnation onset, with agent-specific reversals that corrupt silver labels. We develop a circular evaluation methodology to identify and quantify these cross-agent pathologies.
44	    \item \textbf{Temporal label model negative finding.} We show that three temporal label models fail to improve over majority vote for downstream detection, despite clear temporal structure in LF firing patterns. This informs future weak supervision design for sequential agent data.
45	\end{enumerate}
46	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1311e2e5-9af4-44d3-8961-4a2f79dde730",
  "uuid": "8b77f7cc-691d-43f5-bbaf-ee51606a1bad",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/introduction.tex",
      "content": "% Introduction: Structural stagnation detection in LLM coding agents (EMNLP 2026 ARR)\n\\section{Introduction}\n\\label{sec:introduction}\n\nLarge language model (LLM) agents are increasingly deployed for complex, long-horizon software engineering tasks---resolving GitHub issues, debugging production systems, and iterating on code across multiple rounds of edits \\citep{jimenez2024swebench,yang2024sweagent,wang2025openhands}.\nAs task complexity grows, a critical failure mode emerges that is qualitatively different from crashes or syntax errors: the agent \\emph{stagnates}---continuing to produce actions that appear diverse on the surface while making no meaningful progress toward the task goal.\n\\citet{orlanski2026slopcodebench} systematically document this degradation in long-horizon coding tasks, finding structural erosion in 77\\% of agent trajectories and verbosity increases in 75.5\\%, with no agent fully solving any benchmark problem end-to-end.\nUnlike overt loops, stagnation is insidious: the agent issues varied commands, edits different files, and generates plausible-looking outputs, yet its behavior is functionally stuck.\nDetecting when an agent has entered this regime is essential for reliable deployment---enabling interventions such as early termination, strategy switching, or human escalation---yet identifying \\emph{what signals} carry stagnation information, and whether complex language understanding is necessary to extract them, remains an open question.\n\nPrior approaches to monitoring agent behavior address aspects of this problem but none systematically investigate what information is needed for detection.\n\\emph{Repetition detectors} identify exact or near-exact loops in action sequences, catching the simplest failure mode but missing semantically diverse stagnation where the agent varies its surface behavior while remaining functionally stuck.\n\\emph{Process reward models} \\citep{xi2025agentprm} assign quality scores to individual actions, enabling search-time guidance, but step-level granularity cannot capture temporal patterns that distinguish transient setbacks from sustained stagnation---a distinction that requires reasoning over windows of consecutive actions \\textcolor{red}{[CITE: ICLR 2025 Workshop, Monitoring LLM Agents for Sequentially Contextual Harm]}.\n\\emph{Self-reflection} frameworks \\citep{shinn2023reflexion,yao2023tot,zhou2024lats} rely on the agent itself to diagnose and recover from failures, but when the agent is genuinely stuck, self-diagnosis amounts to querying the failing model about its own failure---a circularity that limits reliability.\nMore fundamentally, all three lines of work prescribe detection \\emph{methods} without first asking what kinds of signals actually carry stagnation information: does detecting subtle agent failure require sophisticated semantic understanding, or do simpler structural patterns suffice?\n\nWe present an empirical analysis that addresses this gap.\nUsing a weak supervision framework \\citep{ratner2016dataprogramming,ratner2017snorkel}, we construct silver-labeled datasets from trajectories of two architecturally distinct agents: SWE-Agent \\citep{yang2024sweagent} on SWE-bench \\citep{jimenez2024swebench} (54,809 windows) and OpenHands \\citep{wang2025openhands} (150,652 windows).\nThree labeling functions (LFs)---targeting command repetition, file modification patterns, and task outcome---provide noisy votes that are aggregated via majority vote into window-level binary labels.\nAgainst these silver labels, we systematically compare three detection paradigms: hand-crafted structural features, neural embedding probes, and LLM-as-judge evaluation.\n\nOur central finding is that \\textbf{stagnation signals are fundamentally structural, not semantic}.\nThirty hand-crafted features capturing command repetition rates, file operation counts, and edit distances achieve 0.9951 macro-F1 in-domain and 0.967 on zero-shot cross-agent transfer, exceeding the LLM judge by 33.3 percentage points (pp).\nA GRU-based neural probe \\citep{cho2014gru} over sentence embeddings reaches 0.906 in-domain but collapses to 0.528 on zero-shot transfer and recovers only to 0.751 after full fine-tuning on the target agent.\nThe structural advantage is encoder-agnostic: swapping the probe's embedding backbone across three encoders (Qwen3-0.6B, BGE-M3, E5-large-v2) yields probe F1 consistently above 0.90 \\citep{zhang2025qwen3embedding,chen2024bgem3,wang2024e5}, confirming that the temporal architecture rather than a specific pretrained encoder drives embedding-based performance.\nCritically, the gap between structural features and learned representations persists across agents with substantially different action distributions (28.5\\% vs.\\ 6.6\\% stagnation rates), suggesting that stagnation manifests in action-level structure that generalizes without adaptation.\nThis challenges the prevailing intuition that detecting subtle agent failures requires complex language understanding, and suggests that lightweight structural monitoring---requiring no GPU and running in under 5\\,ms per window---may be more practical than neural or LLM-based approaches for real-time agent oversight.\n\nBeyond static detection, we analyze the temporal dynamics of the labeling functions that generate silver labels.\nOn SWE-Agent, command repetition ($\\lambda_1$) leads stagnation onset by 1.87 steps on average, serving as an early warning signal, while outcome backpropagation ($\\lambda_3$) lags by 6.70 steps (Kruskal-Wallis $H{=}274.3$, $p{<}10^{-59}$).\nHowever, this temporal structure is agent-specific: on OpenHands, $\\lambda_1$ reverses from leading to lagging ($+3.32$ steps), firing on 92.3\\% of windows with a 71\\% false positive rate on progress windows.\nRemoving $\\lambda_1$ from the OpenHands labeling pipeline improves fine-tuned probe F1 by 17.6\\,pp, demonstrating that labeling functions validated on one agent architecture can become adversarial on another.\nThis finding establishes that LF temporal roles must be re-validated per agent and motivates the circular evaluation methodology we develop to surface such pathologies (\\S\\ref{sec:cmd_rep_ablation}).\n\nWe further investigate whether encoding this temporal structure into label aggregation can improve over simple majority vote.\nThree temporal label models---time-varying weights (TWV), Hidden Markov Models \\citep{safranchik2020linkedhmm}, and lag-aware HMMs---all fail to surpass majority vote on downstream stagnation detection.\nTWV achieves marginally higher self-evaluated F1 (+0.57\\,pp) but degrades downstream probe performance by 2.57\\,pp; the standard HMM overpredicts stagnation, dropping downstream F1 to 0.656.\nThis negative result demonstrates that temporal sophistication in label aggregation does not translate to better silver labels when base agreement among LFs is already high.\n\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n    \\item \\textbf{Structural signal discovery.} We show that 30 structural features achieve near-perfect stagnation detection (0.9951 in-domain, 0.967 cross-agent macro-F1), outperforming neural probes and LLM judges by wide margins (+33.3\\,pp over LLM-as-judge). To our knowledge, this is the first systematic comparison demonstrating that stagnation information resides in action-level structure rather than semantic content.\n    \\item \\textbf{Labeling function temporal dynamics.} We reveal that LFs occupy statistically distinct temporal niches relative to stagnation onset, with agent-specific reversals that corrupt silver labels. We develop a circular evaluation methodology to identify and quantify these cross-agent pathologies.\n    \\item \\textbf{Temporal label model negative finding.} We show that three temporal label models fail to improve over majority vote for downstream detection, despite clear temporal structure in LF firing patterns. This informs future weak supervision design for sequential agent data.\n\\end{enumerate}\n",
      "numLines": 46,
      "startLine": 1,
      "totalLines": 46
    }
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Read · `toolu_01JYawCHsVKdqXdSQzBC8Ex8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1311e2e5-9af4-44d3-8961-4a2f79dde730",
  "uuid": "18bda965-54fe-4119-8fa3-4d6b652c277a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016iV8ChfDzEdb5s2Z8CUR1E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1105,
      "cache_read_input_tokens": 23563,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1105
      },
      "output_tokens": 73,
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

_source line 15 · 2026-05-14T22:04:03.598Z_

<details><summary>↩ Tool result · `toolu_01JYawCHsVKdqXdSQzBC8Ex8`</summary>

```text
1	% ==============================================================
2	% CATEGORY: direct-competitor
3	% ==============================================================
4	
5	@article{xi2025agentprm,
6	  title   = {AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress},
7	  author  = {Zhiheng Xi and Chenyang Liao and Guanyu Li and others},
8	  journal = {arXiv preprint arXiv:2511.08325},
9	  year    = {2025},
10	}
11	
12	@article{choudhury2025prm,
13	  title   = {Process Reward Models for LLM Agents: Practical Framework and Directions},
14	  author  = {Sanjiban Choudhury},
15	  journal = {arXiv preprint arXiv:2502.10325},
16	  year    = {2025},
17	}
18	
19	@article{li2026toolprmbench,
20	  title   = {ToolPRMBench: Evaluating and Advancing Process Reward Models for Tool-using Agents},
21	  author  = {Dawei Li and Yuguang Yao and Zhen Tan and Huan Liu and Ruocheng Guo},
22	  journal = {arXiv preprint arXiv:2601.12294},
23	  year    = {2026},
24	}
25	
26	@article{wang2026planrewardbench,
27	  title   = {Aligning Agents via Planning: A Benchmark for Trajectory-Level Reward Modeling},
28	  author  = {Jiaxuan Wang and Yulan Hu and Wenjin Yang and others},
29	  journal = {arXiv preprint arXiv:2604.08178},
30	  year    = {2026},
31	}
32	
33	@inproceedings{chen2025monitoring,
34	  title     = {Monitoring LLM Agents for Sequentially Contextual Harm},
35	  author    = {Yueh-Han Chen and Neelay Joshi and Yulin Chen and He He and Rico Angell},
36	  booktitle = {ICLR 2025 Workshop on Building Trust in Language Models and Applications},
37	  year      = {2025},
38	}
39	
40	@article{kale2025weaktostrong,
41	  title   = {Reliable Weak-to-Strong Monitoring of LLM Agents},
42	  author  = {Neil Kale and Chen Bo Calvin Zhang and Kevin Zhu and others},
43	  journal = {arXiv preprint arXiv:2508.19461},
44	  year    = {2025},
45	}
46	
47	@article{fan2026agentrm,
48	  title   = {Exploring Reasoning Reward Model for Agents},
49	  author  = {Kaixuan Fan and Kaituo Feng and Manyuan Zhang and others},
50	  journal = {arXiv preprint arXiv:2601.22154},
51	  year    = {2026},
52	}
53	
54	@article{qiu2026dataprm,
55	  title   = {Rewarding the Scientific Process: Process-Level Reward Modeling for Agentic Data Analysis},
56	  author  = {Zhisong Qiu and Shuofei Qiao and Kewei Xu and others},
57	  journal = {arXiv preprint arXiv:2604.24198},
58	  year    = {2026},
59	}
60	
61	% ==============================================================
62	% CATEGORY: method-component
63	% ==============================================================
64	
65	@inproceedings{ratner2016dataprogramming,
66	  title     = {Data Programming: Creating Large Training Sets, Quickly},
67	  author    = {Alexander Ratner and Christopher De Sa and Sen Wu and Daniel Selsam and Christopher Re},
68	  booktitle = {Advances in Neural Information Processing Systems},
69	  year      = {2016},
70	}
71	
72	@article{ratner2017snorkel,
73	  title   = {Snorkel: Rapid Training Data Creation with Weak Supervision},
74	  author  = {Alexander Ratner and Stephen H. Bach and Henry Ehrenberg and others},
75	  journal = {Proceedings of the VLDB Endowment},
76	  year    = {2018},
77	}
78	
79	@inproceedings{fu2020flyingsquid,
80	  title     = {Fast and Three-rious: Speeding Up Weak Supervision with Triplet Methods},
81	  author    = {Daniel Y. Fu and Mayee F. Chen and Frederic Sala and others},
82	  booktitle = {International Conference on Machine Learning},
83	  year      = {2020},
84	}
85	
86	@inproceedings{zhang2021wrench,
87	  title     = {WRENCH: A Comprehensive Benchmark for Weak Supervision},
88	  author    = {Jieyu Zhang and Yue Yu and Yinghao Li and others},
89	  booktitle = {Advances in Neural Information Processing Systems},
90	  year      = {2021},
91	}
92	
93	@inproceedings{safranchik2020linkedhmm,
94	  title     = {Weakly Supervised Sequence Tagging from Noisy Rules},
95	  author    = {Esteban Safranchik and Shiying Luo and Stephen H. Bach},
96	  booktitle = {AAAI Conference on Artificial Intelligence},
97	  year      = {2020},
98	}
99	
100	@inproceedings{sala2019multiresolution,
101	  title     = {Multi-Resolution Weak Supervision for Sequential Data},
102	  author    = {Frederic Sala and Paroma Varma and Jason Fries and others},
103	  booktitle = {Advances in Neural Information Processing Systems},
104	  year      = {2019},
105	}
106	
107	@article{dawid1979em,
108	  title   = {Maximum Likelihood Estimation of Observer Error-Rates Using the EM Algorithm},
109	  author  = {A. P. Dawid and A. M. Skene},
110	  journal = {Journal of the Royal Statistical Society, Series C},
111	  year    = {1979},
112	}
113	
114	@inproceedings{nguyen2017hmmcrowd,
115	  title     = {Aggregating and Predicting Sequence Labels from Crowd Annotations},
116	  author    = {An Thanh Nguyen and Byron C. Wallace and Junyi Jessy Li and Ani Nenkova and Matthew Lease},
117	  booktitle = {Annual Meeting of the Association for Computational Linguistics},
118	  year      = {2017},
119	}
120	
121	% ==============================================================
122	% CATEGORY: evaluation
123	% ==============================================================
124	
125	@article{orlanski2026slopcodebench,
126	  title   = {SlopCodeBench: Benchmarking How Coding Agents Degrade Over Long-Horizon Iterative Tasks},
127	  author  = {Gabriel Orlanski and Devjeet Roy and Alexander Yun and others},
128	  journal = {arXiv preprint arXiv:2603.24755},
129	  year    = {2026},
130	}
131	
132	@inproceedings{jimenez2024swebench,
133	  title     = {SWE-bench: Can Language Models Resolve Real-World GitHub Issues?},
134	  author    = {Carlos E. Jimenez and John Yang and Alexander Wettig and others},
135	  booktitle = {International Conference on Learning Representations},
136	  year      = {2024},
137	}
138	
139	@inproceedings{yang2024sweagent,
140	  title     = {SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering},
141	  author    = {John Yang and Carlos E. Jimenez and Alexander Wettig and others},
142	  booktitle = {Advances in Neural Information Processing Systems},
143	  year      = {2024},
144	}
145	
146	@inproceedings{wang2025openhands,
147	  title     = {OpenHands: An Open Platform for AI Software Developers as Generalist Agents},
148	  author    = {Xingyao Wang and Boxuan Li and Yufan Song and others},
149	  booktitle = {International Conference on Learning Representations},
150	  year      = {2025},
151	}
152	
153	@inproceedings{zhou2024webarena,
154	  title     = {WebArena: A Realistic Web Environment for Building Autonomous Agents},
155	  author    = {Shuyan Zhou and Frank F. Xu and Hao Zhu and others},
156	  booktitle = {International Conference on Learning Representations},
157	  year      = {2024},
158	}
159	
160	@inproceedings{wang2024mint,
161	  title     = {MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback},
162	  author    = {Xingyao Wang and Zihan Wang and Jiateng Liu and others},
163	  booktitle = {International Conference on Learning Representations},
164	  year      = {2024},
165	}
166	
167	% ==============================================================
168	% CATEGORY: background
169	% ==============================================================
170	
171	@inproceedings{shinn2023reflexion,
172	  title     = {Reflexion: Language Agents with Verbal Reinforcement Learning},
173	  author    = {Noah Shinn and Federico Cassano and Ashwin Gopinath and Karthik Narasimhan and Shunyu Yao},
174	  booktitle = {Advances in Neural Information Processing Systems},
175	  year      = {2023},
176	}
177	
178	@inproceedings{zhou2024lats,
179	  title     = {Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models},
180	  author    = {Andy Zhou and Kai Yan and Michal Shlapentokh-Rothman and Haohan Wang and Yu-Xiong Wang},
181	  booktitle = {International Conference on Machine Learning},
182	  year      = {2024},
183	}
184	
185	@inproceedings{yao2023tot,
186	  title     = {Tree of Thoughts: Deliberate Problem Solving with Large Language Models},
187	  author    = {Shunyu Yao and Dian Yu and Jeffrey Zhao and others},
188	  booktitle = {Advances in Neural Information Processing Systems},
189	  year      = {2023},
190	}
191	
192	@article{cemri2025multiagentfail,
193	  title   = {Why Do Multi-Agent LLM Systems Fail?},
194	  author  = {Mert Cemri and Melissa Z. Pan and Shuyi Yang and others},
195	  journal = {arXiv preprint arXiv:2503.13657},
196	  year    = {2025},
197	}
198	
199	@article{zhu2025agentfail,
200	  title   = {Where LLM Agents Fail and How They Can Learn From Failures},
201	  author  = {Kunlun Zhu and Zijia Liu and Bingxuan Li and others},
202	  journal = {arXiv preprint arXiv:2509.25370},
203	  year    = {2025},
204	}
205	
206	@article{george2025cycledetection,
207	  title   = {Unsupervised Cycle Detection in Agentic Applications},
208	  author  = {Felix George and Harshit Kumar and Divya Pathak and others},
209	  journal = {arXiv preprint arXiv:2511.10650},
210	  year    = {2025},
211	}
212	
213	@article{pipis2025reasoningloop,
214	  title   = {Wait, Wait, Wait... Why Do Reasoning Models Loop?},
215	  author  = {Charilaos Pipis and Shivam Garg and Vasilis Kontonis and others},
216	  journal = {arXiv preprint arXiv:2512.12895},
217	  year    = {2025},
218	}
219	
220	@inproceedings{huang2024selfcorrect,
221	  title     = {Large Language Models Cannot Self-Correct Reasoning Yet},
222	  author    = {Jie Huang and Xinyun Chen and Swaroop Mishra and others},
223	  booktitle = {International Conference on Learning Representations},
224	  year      = {2024},
225	}
226	
227	@article{kamoi2024selfcorrection,
228	  title   = {When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs},
229	  author  = {Ryo Kamoi and Yusen Zhang and Nan Zhang and Jiawei Han and Rui Zhang},
230	  journal = {Transactions of the Association for Computational Linguistics},
231	  year    = {2024},
232	}
233	
234	@article{liu2026trajad,
235	  title   = {TrajAD: Trajectory Anomaly Detection for Trustworthy LLM Agents},
236	  author  = {Yibing Liu and Chong Zhang and Zhongyi Han and others},
237	  journal = {arXiv preprint arXiv:2602.06443},
238	  year    = {2026},
239	}
240	
241	% ==============================================================
242	% CATEGORY: technique
243	% ==============================================================
244	
245	@inproceedings{cho2014gru,
246	  title     = {Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation},
247	  author    = {Kyunghyun Cho and Bart van Merrienboer and Caglar Gulcehre and others},
248	  booktitle = {Conference on Empirical Methods in Natural Language Processing},
249	  year      = {2014},
250	}
251	
252	@inproceedings{bahdanau2015attention,
253	  title     = {Neural Machine Translation by Jointly Learning to Align and Translate},
254	  author    = {Dzmitry Bahdanau and Kyunghyun Cho and Yoshua Bengio},
255	  booktitle = {International Conference on Learning Representations},
256	  year      = {2015},
257	}
258	
259	@inproceedings{khosla2020supcon,
260	  title     = {Supervised Contrastive Learning},
261	  author    = {Prannay Khosla and Piotr Teterwak and Chen Wang and others},
262	  booktitle = {Advances in Neural Information Processing Systems},
263	  year      = {2020},
264	}
265	
266	@article{zhang2025qwen3embedding,
267	  title   = {Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models},
268	  author  = {Yanzhao Zhang and Mingxin Li and Dingkun Long and others},
269	  journal = {arXiv preprint arXiv:2506.05176},
270	  year    = {2025},
271	}
272	
273	@article{wang2024e5,
274	  title   = {Multilingual E5 Text Embeddings: A Technical Report},
275	  author  = {Liang Wang and Nan Yang and Xiaolong Huang and others},
276	  journal = {arXiv preprint arXiv:2402.05672},
277	  year    = {2024},
278	}
279	
280	@article{chen2024bgem3,
281	  title   = {BGE M3-Embedding: Multi-Linguality, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation},
282	  author  = {Jianlv Chen and Shitao Xiao and Peitian Zhang and others},
283	  journal = {arXiv preprint arXiv:2402.03216},
284	  year    = {2024},
285	}
286	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1311e2e5-9af4-44d3-8961-4a2f79dde730",
  "uuid": "896f7937-9bbe-4fb2-a989-7a6eb3a6771f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/references.bib",
      "content": "% ==============================================================\n% CATEGORY: direct-competitor\n% ==============================================================\n\n@article{xi2025agentprm,\n  title   = {AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress},\n  author  = {Zhiheng Xi and Chenyang Liao and Guanyu Li and others},\n  journal = {arXiv preprint arXiv:2511.08325},\n  year    = {2025},\n}\n\n@article{choudhury2025prm,\n  title   = {Process Reward Models for LLM Agents: Practical Framework and Directions},\n  author  = {Sanjiban Choudhury},\n  journal = {arXiv preprint arXiv:2502.10325},\n  year    = {2025},\n}\n\n@article{li2026toolprmbench,\n  title   = {ToolPRMBench: Evaluating and Advancing Process Reward Models for Tool-using Agents},\n  author  = {Dawei Li and Yuguang Yao and Zhen Tan and Huan Liu and Ruocheng Guo},\n  journal = {arXiv preprint arXiv:2601.12294},\n  year    = {2026},\n}\n\n@article{wang2026planrewardbench,\n  title   = {Aligning Agents via Planning: A Benchmark for Trajectory-Level Reward Modeling},\n  author  = {Jiaxuan Wang and Yulan Hu and Wenjin Yang and others},\n  journal = {arXiv preprint arXiv:2604.08178},\n  year    = {2026},\n}\n\n@inproceedings{chen2025monitoring,\n  title     = {Monitoring LLM Agents for Sequentially Contextual Harm},\n  author    = {Yueh-Han Chen and Neelay Joshi and Yulin Chen and He He and Rico Angell},\n  booktitle = {ICLR 2025 Workshop on Building Trust in Language Models and Applications},\n  year      = {2025},\n}\n\n@article{kale2025weaktostrong,\n  title   = {Reliable Weak-to-Strong Monitoring of LLM Agents},\n  author  = {Neil Kale and Chen Bo Calvin Zhang and Kevin Zhu and others},\n  journal = {arXiv preprint arXiv:2508.19461},\n  year    = {2025},\n}\n\n@article{fan2026agentrm,\n  title   = {Exploring Reasoning Reward Model for Agents},\n  author  = {Kaixuan Fan and Kaituo Feng and Manyuan Zhang and others},\n  journal = {arXiv preprint arXiv:2601.22154},\n  year    = {2026},\n}\n\n@article{qiu2026dataprm,\n  title   = {Rewarding the Scientific Process: Process-Level Reward Modeling for Agentic Data Analysis},\n  author  = {Zhisong Qiu and Shuofei Qiao and Kewei Xu and others},\n  journal = {arXiv preprint arXiv:2604.24198},\n  year    = {2026},\n}\n\n% ==============================================================\n% CATEGORY: method-component\n% ==============================================================\n\n@inproceedings{ratner2016dataprogramming,\n  title     = {Data Programming: Creating Large Training Sets, Quickly},\n  author    = {Alexander Ratner and Christopher De Sa and Sen Wu and Daniel Selsam and Christopher Re},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2016},\n}\n\n@article{ratner2017snorkel,\n  title   = {Snorkel: Rapid Training Data Creation with Weak Supervision},\n  author  = {Alexander Ratner and Stephen H. Bach and Henry Ehrenberg and others},\n  journal = {Proceedings of the VLDB Endowment},\n  year    = {2018},\n}\n\n@inproceedings{fu2020flyingsquid,\n  title     = {Fast and Three-rious: Speeding Up Weak Supervision with Triplet Methods},\n  author    = {Daniel Y. Fu and Mayee F. Chen and Frederic Sala and others},\n  booktitle = {International Conference on Machine Learning},\n  year      = {2020},\n}\n\n@inproceedings{zhang2021wrench,\n  title     = {WRENCH: A Comprehensive Benchmark for Weak Supervision},\n  author    = {Jieyu Zhang and Yue Yu and Yinghao Li and others},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2021},\n}\n\n@inproceedings{safranchik2020linkedhmm,\n  title     = {Weakly Supervised Sequence Tagging from Noisy Rules},\n  author    = {Esteban Safranchik and Shiying Luo and Stephen H. Bach},\n  booktitle = {AAAI Conference on Artificial Intelligence},\n  year      = {2020},\n}\n\n@inproceedings{sala2019multiresolution,\n  title     = {Multi-Resolution Weak Supervision for Sequential Data},\n  author    = {Frederic Sala and Paroma Varma and Jason Fries and others},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2019},\n}\n\n@article{dawid1979em,\n  title   = {Maximum Likelihood Estimation of Observer Error-Rates Using the EM Algorithm},\n  author  = {A. P. Dawid and A. M. Skene},\n  journal = {Journal of the Royal Statistical Society, Series C},\n  year    = {1979},\n}\n\n@inproceedings{nguyen2017hmmcrowd,\n  title     = {Aggregating and Predicting Sequence Labels from Crowd Annotations},\n  author    = {An Thanh Nguyen and Byron C. Wallace and Junyi Jessy Li and Ani Nenkova and Matthew Lease},\n  booktitle = {Annual Meeting of the Association for Computational Linguistics},\n  year      = {2017},\n}\n\n% ==============================================================\n% CATEGORY: evaluation\n% ==============================================================\n\n@article{orlanski2026slopcodebench,\n  title   = {SlopCodeBench: Benchmarking How Coding Agents Degrade Over Long-Horizon Iterative Tasks},\n  author  = {Gabriel Orlanski and Devjeet Roy and Alexander Yun and others},\n  journal = {arXiv preprint arXiv:2603.24755},\n  year    = {2026},\n}\n\n@inproceedings{jimenez2024swebench,\n  title     = {SWE-bench: Can Language Models Resolve Real-World GitHub Issues?},\n  author    = {Carlos E. Jimenez and John Yang and Alexander Wettig and others},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2024},\n}\n\n@inproceedings{yang2024sweagent,\n  title     = {SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering},\n  author    = {John Yang and Carlos E. Jimenez and Alexander Wettig and others},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2024},\n}\n\n@inproceedings{wang2025openhands,\n  title     = {OpenHands: An Open Platform for AI Software Developers as Generalist Agents},\n  author    = {Xingyao Wang and Boxuan Li and Yufan Song and others},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2025},\n}\n\n@inproceedings{zhou2024webarena,\n  title     = {WebArena: A Realistic Web Environment for Building Autonomous Agents},\n  author    = {Shuyan Zhou and Frank F. Xu and Hao Zhu and others},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2024},\n}\n\n@inproceedings{wang2024mint,\n  title     = {MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback},\n  author    = {Xingyao Wang and Zihan Wang and Jiateng Liu and others},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2024},\n}\n\n% ==============================================================\n% CATEGORY: background\n% ==============================================================\n\n@inproceedings{shinn2023reflexion,\n  title     = {Reflexion: Language Agents with Verbal Reinforcement Learning},\n  author    = {Noah Shinn and Federico Cassano and Ashwin Gopinath and Karthik Narasimhan and Shunyu Yao},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2023},\n}\n\n@inproceedings{zhou2024lats,\n  title     = {Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models},\n  author    = {Andy Zhou and Kai Yan and Michal Shlapentokh-Rothman and Haohan Wang and Yu-Xiong Wang},\n  booktitle = {International Conference on Machine Learning},\n  year      = {2024},\n}\n\n@inproceedings{yao2023tot,\n  title     = {Tree of Thoughts: Deliberate Problem Solving with Large Language Models},\n  author    = {Shunyu Yao and Dian Yu and Jeffrey Zhao and others},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2023},\n}\n\n@article{cemri2025multiagentfail,\n  title   = {Why Do Multi-Agent LLM Systems Fail?},\n  author  = {Mert Cemri and Melissa Z. Pan and Shuyi Yang and others},\n  journal = {arXiv preprint arXiv:2503.13657},\n  year    = {2025},\n}\n\n@article{zhu2025agentfail,\n  title   = {Where LLM Agents Fail and How They Can Learn From Failures},\n  author  = {Kunlun Zhu and Zijia Liu and Bingxuan Li and others},\n  journal = {arXiv preprint arXiv:2509.25370},\n  year    = {2025},\n}\n\n@article{george2025cycledetection,\n  title   = {Unsupervised Cycle Detection in Agentic Applications},\n  author  = {Felix George and Harshit Kumar and Divya Pathak and others},\n  journal = {arXiv preprint arXiv:2511.10650},\n  year    = {2025},\n}\n\n@article{pipis2025reasoningloop,\n  title   = {Wait, Wait, Wait... Why Do Reasoning Models Loop?},\n  author  = {Charilaos Pipis and Shivam Garg and Vasilis Kontonis and others},\n  journal = {arXiv preprint arXiv:2512.12895},\n  year    = {2025},\n}\n\n@inproceedings{huang2024selfcorrect,\n  title     = {Large Language Models Cannot Self-Correct Reasoning Yet},\n  author    = {Jie Huang and Xinyun Chen and Swaroop Mishra and others},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2024},\n}\n\n@article{kamoi2024selfcorrection,\n  title   = {When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs},\n  author  = {Ryo Kamoi and Yusen Zhang and Nan Zhang and Jiawei Han and Rui Zhang},\n  journal = {Transactions of the Association for Computational Linguistics},\n  year    = {2024},\n}\n\n@article{liu2026trajad,\n  title   = {TrajAD: Trajectory Anomaly Detection for Trustworthy LLM Agents},\n  author  = {Yibing Liu and Chong Zhang and Zhongyi Han and others},\n  journal = {arXiv preprint arXiv:2602.06443},\n  year    = {2026},\n}\n\n% ==============================================================\n% CATEGORY: technique\n% ==============================================================\n\n@inproceedings{cho2014gru,\n  title     = {Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation},\n  author    = {Kyunghyun Cho and Bart van Merrienboer and Caglar Gulcehre and others},\n  booktitle = {Conference on Empirical Methods in Natural Language Processing},\n  year      = {2014},\n}\n\n@inproceedings{bahdanau2015attention,\n  title     = {Neural Machine Translation by Jointly Learning to Align and Translate},\n  author    = {Dzmitry Bahdanau and Kyunghyun Cho and Yoshua Bengio},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2015},\n}\n\n@inproceedings{khosla2020supcon,\n  title     = {Supervised Contrastive Learning},\n  author    = {Prannay Khosla and Piotr Teterwak and Chen Wang and others},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2020},\n}\n\n@article{zhang2025qwen3embedding,\n  title   = {Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models},\n  author  = {Yanzhao Zhang and Mingxin Li and Dingkun Long and others},\n  journal = {arXiv preprint arXiv:2506.05176},\n  year    = {2025},\n}\n\n@article{wang2024e5,\n  title   = {Multilingual E5 Text Embeddings: A Technical Report},\n  author  = {Liang Wang and Nan Yang and Xiaolong Huang and others},\n  journal = {arXiv preprint arXiv:2402.05672},\n  year    = {2024},\n}\n\n@article{chen2024bgem3,\n  title   = {BGE M3-Embedding: Multi-Linguality, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation},\n  author  = {Jianlv Chen and Shitao Xiao and Peitian Zhang and others},\n  journal = {arXiv preprint arXiv:2402.03216},\n  year    = {2024},\n}\n",
      "numLines": 286,
      "startLine": 1,
      "totalLines": 286
    }
  }
}
```

</details>

---

### Assistant

_source line 16_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the context needed. Let me write the Related Work section. Let me organize it into the suggested 4 subsections and make sure I only use bib keys that exist in the references.bib file.

Available bib keys from references.bib:
- xi2025agentprm, choudhury2025prm, li2026toolprmbench, wang2026planrewardbench, chen2025monitoring, kale2025weaktostrong, fan2026agentrm, qiu2026dataprm


- orlanski2026slopcodebench, jimenez2024swebench, yang2024sweagent, wang2025openhands, zhou2024webarena, wang2024mint
- shinn2023reflexion, zhou2024lats, yao2023tot, cemri2025multiagentfail, zhu2025agentfail, george2025cycledetection, pipis2025reasoningloop, huang2024selfcorrect, kamoi2024selfcorrection

I notice many of the bib keys I was considering don't exist in the available references, so I need to focus on the ones that are actually available and structure the subsections around those papers instead.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1311e2e5-9af4-44d3-8961-4a2f79dde730",
  "uuid": "6cf50d18-a20f-4cf6-b753-f240405a075b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SziXuvbdcRUjfLoRbx1sKZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22815,
      "cache_read_input_tokens": 24668,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 22815
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

_source line 17_

Now I have all context. Let me write the Related Work section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1311e2e5-9af4-44d3-8961-4a2f79dde730",
  "uuid": "66db7f42-8193-4873-8c8f-7a958edaf69c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SziXuvbdcRUjfLoRbx1sKZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22815,
      "cache_read_input_tokens": 24668,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 22815
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

_source line 18_

<details open><summary>🔧 Tool call — Write · `toolu_01YXpFFaUVLV3XXEi93PsfyD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/related_work.tex",
  "content": "% Related Work: Structural stagnation detection in LLM coding agents (EMNLP 2026 ARR)\n\\section{Related Work}\n\\label{sec:related_work}\n\n\\subsection{LLM Agent Monitoring and Evaluation}\n\nAs LLM agents tackle increasingly complex tasks \\citep{jimenez2024swebench,yang2024sweagent,wang2025openhands,zhou2024webarena,wang2024mint}, understanding and monitoring their failure modes has become critical.\nTaxonomic studies reveal that agent failures are often systematic: \\citet{cemri2025multiagentfail} identify 14 failure modes in multi-agent systems, including step repetition as a concrete symptom, while \\citet{zhu2025agentfail} show that cascading failures---where a single root cause propagates across subsequent decisions---dominate long-horizon tasks.\n\\citet{orlanski2026slopcodebench} provide the most direct evidence of agent degradation, documenting structural erosion in 77\\% of coding agent trajectories with no agent fully solving any benchmark task end-to-end.\n\nExisting monitoring approaches span several paradigms.\n\\emph{Self-reflection} methods \\citep{shinn2023reflexion,yao2023tot,zhou2024lats} rely on the agent to diagnose its own failures, but \\citet{huang2024selfcorrect} and \\citet{kamoi2024selfcorrection} demonstrate that LLMs cannot reliably self-correct without external feedback, motivating external monitoring.\n\\citet{george2025cycledetection} propose unsupervised cycle detection combining call-stack analysis with embedding similarity, while \\citet{pipis2025reasoningloop} analyze why reasoning models loop, using $n$-gram repetition as a detection heuristic.\nOn the external monitoring front, \\citet{chen2025monitoring} show that sequence-level context is necessary---single-step analysis misses sequentially contextual harm---and \\citet{kale2025weaktostrong} demonstrate that monitor scaffolding matters more than monitor capability, with weak models reliably monitoring stronger agents.\n\nOur work differs from all of the above in its central question: rather than proposing a new monitoring \\emph{method}, we conduct an empirical study asking what \\emph{signals} carry stagnation information.\nWe show that 30 structural features suffice for near-perfect detection (0.995 F1), without requiring another LLM, self-reflection, or embedding-based similarity.\n\n\\subsection{Process Reward Models for Agents}\n\nProcess reward models (PRMs) assign quality scores to individual agent steps, enabling search-time guidance and trajectory selection.\n\\citet{xi2025agentprm} introduce AgentPRM, training step-level reward models via TD/GAE that evaluate both ``promise'' (long-term potential) and ``progress'' (immediate advancement), achieving 8$\\times$ compute efficiency gains.\n\\citet{choudhury2025prm} formalize the PRM framework and propose InversePRM, learning process rewards from expert demonstrations without outcome labels, with a 3B model surpassing GPT-4o.\nEvaluation benchmarks have emerged in parallel: \\citet{li2026toolprmbench} benchmark PRMs on tool-use scenarios, finding that specialized PRMs substantially outperform general-purpose ones, while \\citet{wang2026planrewardbench} evaluate trajectory-level reward models and reveal that all model categories---generative, discriminative, and LLM-as-judge---degrade significantly on long-horizon trajectories.\n\\citet{fan2026agentrm} extend PRMs with structured reasoning traces and multi-dimensional critiques (Agent-RRM), and \\citet{qiu2026dataprm} address data analysis agents specifically, introducing environment-aware probing to detect silent errors that standard PRMs miss.\n\nOur work is complementary to the PRM line but differs in three fundamental ways: (1)~we operate at window level rather than step level, capturing temporal patterns across consecutive actions; (2)~we require no outcome labels or reward annotations---our labeling functions use only observable structural signals; and (3)~our goal is real-time \\emph{monitoring} (stagnation detection in $<$5\\,ms), not \\emph{training signal} generation for agent improvement.\nThe degradation of trajectory-level reward models on long horizons reported by \\citet{wang2026planrewardbench} further motivates our window-level approach, which avoids full-trajectory reasoning by design.\n\n\\subsection{Data Programming and Weak Supervision}\n\nData programming \\citep{ratner2016dataprogramming} enables rapid training set creation through user-defined labeling functions (LFs), with a generative model learning LF accuracies to produce probabilistic labels.\nSnorkel \\citep{ratner2017snorkel} operationalizes this into an end-to-end system with dependency-aware label models, and \\citet{fu2020flyingsquid} accelerate label model inference via closed-form triplet methods.\n\\citet{zhang2021wrench} provide a comprehensive benchmark spanning 22 datasets, though all assume i.i.d.\\ data points.\n\nExtensions to sequential data relax this assumption.\n\\citet{safranchik2020linkedhmm} introduce a linked HMM for weakly supervised sequence tagging (NER), incorporating linking rules that model span structure and improving over i.i.d.\\ label models by 7~F1 points.\n\\citet{sala2019multiresolution} handle multi-resolution LFs operating at different temporal granularities.\nIn crowdsourcing, \\citet{nguyen2017hmmcrowd} extend \\citeauthor{dawid1979em}'s EM-based annotator model \\citep{dawid1979em} with HMM structure for sequential label aggregation.\n\nWe apply data programming to agent trajectory data, a novel domain where LFs exhibit systematic temporal dynamics (e.g., command repetition leads stagnation onset by 1.87 steps on SWE-Agent).\nUnlike prior sequential extensions that target token-level NER or multi-resolution alignment, our setting involves window-level binary classification with agent-specific LF role reversals.\nCritically, we test whether temporal label models---motivated by the clear i.i.d.\\ violations we observe---can improve over majority vote, and report a negative finding: three implementations (TWV, HMM, lag-aware HMM) all fail to surpass simple voting in the low-conflict regime of our 3-LF framework.\n\n\\subsection{Anomaly Detection in Agent Trajectories}\n\nDetecting anomalous behavior in sequential agent data connects to the broader literature on time-series anomaly detection.\n\\citet{liu2026trajad} propose TrajAD, training a fine-grained verifier through synthetic perturbations (perturb-and-complete) to detect trajectory anomalies including task failure, process inefficiency, and unwarranted continuation.\nThey show that general-purpose LLMs perform poorly at zero-shot trajectory anomaly detection, motivating specialized approaches.\n\nOur work differs from anomaly detection in both formulation and methodology.\nWe frame stagnation as a binary classification problem over sliding windows rather than identifying rare deviations from a normal distribution.\nStagnation is not anomalous in the statistical sense---it occurs in 28.5\\% of SWE-Agent windows and 6.6\\% of OpenHands windows---but rather represents a persistent behavioral regime that an agent enters and may not exit without intervention.\nWhere TrajAD requires training a specialized verifier on synthetic data, our empirical analysis reveals that hand-crafted structural features achieve 0.995 F1 without any learned components, and our probe model uses a lightweight GRU \\citep{cho2014gru} with attention \\citep{bahdanau2015attention} rather than a full LLM verifier.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1311e2e5-9af4-44d3-8961-4a2f79dde730",
  "uuid": "fc483e2b-0c92-45c3-a168-76a9206a66f8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SziXuvbdcRUjfLoRbx1sKZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22815,
      "cache_read_input_tokens": 24668,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 22815
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

_source line 19 · 2026-05-14T22:05:02.000Z_

<details><summary>↩ Tool result · `toolu_01YXpFFaUVLV3XXEi93PsfyD`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1311e2e5-9af4-44d3-8961-4a2f79dde730",
  "uuid": "0f05d061-0948-4274-b4fd-08bd540c7460",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/related_work.tex",
    "content": "% Related Work: Structural stagnation detection in LLM coding agents (EMNLP 2026 ARR)\n\\section{Related Work}\n\\label{sec:related_work}\n\n\\subsection{LLM Agent Monitoring and Evaluation}\n\nAs LLM agents tackle increasingly complex tasks \\citep{jimenez2024swebench,yang2024sweagent,wang2025openhands,zhou2024webarena,wang2024mint}, understanding and monitoring their failure modes has become critical.\nTaxonomic studies reveal that agent failures are often systematic: \\citet{cemri2025multiagentfail} identify 14 failure modes in multi-agent systems, including step repetition as a concrete symptom, while \\citet{zhu2025agentfail} show that cascading failures---where a single root cause propagates across subsequent decisions---dominate long-horizon tasks.\n\\citet{orlanski2026slopcodebench} provide the most direct evidence of agent degradation, documenting structural erosion in 77\\% of coding agent trajectories with no agent fully solving any benchmark task end-to-end.\n\nExisting monitoring approaches span several paradigms.\n\\emph{Self-reflection} methods \\citep{shinn2023reflexion,yao2023tot,zhou2024lats} rely on the agent to diagnose its own failures, but \\citet{huang2024selfcorrect} and \\citet{kamoi2024selfcorrection} demonstrate that LLMs cannot reliably self-correct without external feedback, motivating external monitoring.\n\\citet{george2025cycledetection} propose unsupervised cycle detection combining call-stack analysis with embedding similarity, while \\citet{pipis2025reasoningloop} analyze why reasoning models loop, using $n$-gram repetition as a detection heuristic.\nOn the external monitoring front, \\citet{chen2025monitoring} show that sequence-level context is necessary---single-step analysis misses sequentially contextual harm---and \\citet{kale2025weaktostrong} demonstrate that monitor scaffolding matters more than monitor capability, with weak models reliably monitoring stronger agents.\n\nOur work differs from all of the above in its central question: rather than proposing a new monitoring \\emph{method}, we conduct an empirical study asking what \\emph{signals} carry stagnation information.\nWe show that 30 structural features suffice for near-perfect detection (0.995 F1), without requiring another LLM, self-reflection, or embedding-based similarity.\n\n\\subsection{Process Reward Models for Agents}\n\nProcess reward models (PRMs) assign quality scores to individual agent steps, enabling search-time guidance and trajectory selection.\n\\citet{xi2025agentprm} introduce AgentPRM, training step-level reward models via TD/GAE that evaluate both ``promise'' (long-term potential) and ``progress'' (immediate advancement), achieving 8$\\times$ compute efficiency gains.\n\\citet{choudhury2025prm} formalize the PRM framework and propose InversePRM, learning process rewards from expert demonstrations without outcome labels, with a 3B model surpassing GPT-4o.\nEvaluation benchmarks have emerged in parallel: \\citet{li2026toolprmbench} benchmark PRMs on tool-use scenarios, finding that specialized PRMs substantially outperform general-purpose ones, while \\citet{wang2026planrewardbench} evaluate trajectory-level reward models and reveal that all model categories---generative, discriminative, and LLM-as-judge---degrade significantly on long-horizon trajectories.\n\\citet{fan2026agentrm} extend PRMs with structured reasoning traces and multi-dimensional critiques (Agent-RRM), and \\citet{qiu2026dataprm} address data analysis agents specifically, introducing environment-aware probing to detect silent errors that standard PRMs miss.\n\nOur work is complementary to the PRM line but differs in three fundamental ways: (1)~we operate at window level rather than step level, capturing temporal patterns across consecutive actions; (2)~we require no outcome labels or reward annotations---our labeling functions use only observable structural signals; and (3)~our goal is real-time \\emph{monitoring} (stagnation detection in $<$5\\,ms), not \\emph{training signal} generation for agent improvement.\nThe degradation of trajectory-level reward models on long horizons reported by \\citet{wang2026planrewardbench} further motivates our window-level approach, which avoids full-trajectory reasoning by design.\n\n\\subsection{Data Programming and Weak Supervision}\n\nData programming \\citep{ratner2016dataprogramming} enables rapid training set creation through user-defined labeling functions (LFs), with a generative model learning LF accuracies to produce probabilistic labels.\nSnorkel \\citep{ratner2017snorkel} operationalizes this into an end-to-end system with dependency-aware label models, and \\citet{fu2020flyingsquid} accelerate label model inference via closed-form triplet methods.\n\\citet{zhang2021wrench} provide a comprehensive benchmark spanning 22 datasets, though all assume i.i.d.\\ data points.\n\nExtensions to sequential data relax this assumption.\n\\citet{safranchik2020linkedhmm} introduce a linked HMM for weakly supervised sequence tagging (NER), incorporating linking rules that model span structure and improving over i.i.d.\\ label models by 7~F1 points.\n\\citet{sala2019multiresolution} handle multi-resolution LFs operating at different temporal granularities.\nIn crowdsourcing, \\citet{nguyen2017hmmcrowd} extend \\citeauthor{dawid1979em}'s EM-based annotator model \\citep{dawid1979em} with HMM structure for sequential label aggregation.\n\nWe apply data programming to agent trajectory data, a novel domain where LFs exhibit systematic temporal dynamics (e.g., command repetition leads stagnation onset by 1.87 steps on SWE-Agent).\nUnlike prior sequential extensions that target token-level NER or multi-resolution alignment, our setting involves window-level binary classification with agent-specific LF role reversals.\nCritically, we test whether temporal label models---motivated by the clear i.i.d.\\ violations we observe---can improve over majority vote, and report a negative finding: three implementations (TWV, HMM, lag-aware HMM) all fail to surpass simple voting in the low-conflict regime of our 3-LF framework.\n\n\\subsection{Anomaly Detection in Agent Trajectories}\n\nDetecting anomalous behavior in sequential agent data connects to the broader literature on time-series anomaly detection.\n\\citet{liu2026trajad} propose TrajAD, training a fine-grained verifier through synthetic perturbations (perturb-and-complete) to detect trajectory anomalies including task failure, process inefficiency, and unwarranted continuation.\nThey show that general-purpose LLMs perform poorly at zero-shot trajectory anomaly detection, motivating specialized approaches.\n\nOur work differs from anomaly detection in both formulation and methodology.\nWe frame stagnation as a binary classification problem over sliding windows rather than identifying rare deviations from a normal distribution.\nStagnation is not anomalous in the statistical sense---it occurs in 28.5\\% of SWE-Agent windows and 6.6\\% of OpenHands windows---but rather represents a persistent behavioral regime that an agent enters and may not exit without intervention.\nWhere TrajAD requires training a specialized verifier on synthetic data, our empirical analysis reveals that hand-crafted structural features achieve 0.995 F1 without any learned components, and our probe model uses a lightweight GRU \\citep{cho2014gru} with attention \\citep{bahdanau2015attention} rather than a full LLM verifier.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 20_

Now let me copy to artifacts and register.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1311e2e5-9af4-44d3-8961-4a2f79dde730",
  "uuid": "becd4764-8ad4-4a35-9a76-1f8fd5dcfc10",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017wLbHD8RSuQhtmqW4GMo4j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2479,
      "cache_read_input_tokens": 47483,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2479
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

_source line 21_

<details open><summary>🔧 Tool call — Bash · `toolu_01K8QL6zJ58VJvg14y2x8ay5`</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/_project/paper && cp /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/related_work.tex /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/_project/paper/related_work.tex",
  "description": "Copy related_work.tex to artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1311e2e5-9af4-44d3-8961-4a2f79dde730",
  "uuid": "f15c3a22-9a9a-46ae-97e0-6fb70681fedc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017wLbHD8RSuQhtmqW4GMo4j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2479,
      "cache_read_input_tokens": 47483,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2479
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

_source line 22 · 2026-05-14T22:05:06.875Z_

<details><summary>↩ Tool result · `toolu_01K8QL6zJ58VJvg14y2x8ay5`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1311e2e5-9af4-44d3-8961-4a2f79dde730",
  "uuid": "36fc450a-185c-4060-944d-7f0c1a0f697d",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  }
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01WL2jyXcUFDY7mSxVrF3fxf`</summary>

```json
{
  "name": "related_work_section",
  "type": "paper",
  "description": "EMNLP 2026 ARR Related Work section (4 subsections: Agent Monitoring, PRMs, Data Programming/Weak Supervision, Anomaly Detection). ~750 words, 30+ citations.",
  "project": "agent_progress_probe",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/_project/paper/related_work.tex",
  "tags": [
    "paper",
    "related-work",
    "emnlp2026"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1311e2e5-9af4-44d3-8961-4a2f79dde730",
  "uuid": "12f0b93e-e2f3-4c12-8ef4-cb545cae4b42",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011fN5NbabvzEqkyA6pdinMR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 318,
      "cache_read_input_tokens": 49962,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 318
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

_source line 24 · 2026-05-14T22:05:12.165Z_

<details><summary>↩ Tool result · `toolu_01WL2jyXcUFDY7mSxVrF3fxf`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_60e275\", \"name\": \"related_work_section\", \"type\": \"paper\", \"description\": \"EMNLP 2026 ARR Related Work section (4 subsections: Agent Monitoring, PRMs, Data Programming/Weak Supervision, Anomaly Detection). ~750 words, 30+ citations.\", \"path\": \"projects/agent_progress_probe/artifacts/_project/paper/related_work_60e275.tex\", \"url\": null, \"project\": \"agent_progress_probe\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-14T22:05:11.916403+00:00\", \"tags\": [\"paper\", \"related-work\", \"emnlp2026\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1311e2e5-9af4-44d3-8961-4a2f79dde730",
  "uuid": "c057a98e-0b5a-4e09-9c89-0dc4f1d02674",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260514_60e275\\\", \\\"name\\\": \\\"related_work_section\\\", \\\"type\\\": \\\"paper\\\", \\\"description\\\": \\\"EMNLP 2026 ARR Related Work section (4 subsections: Agent Monitoring, PRMs, Data Programming/Weak Supervision, Anomaly Detection). ~750 words, 30+ citations.\\\", \\\"path\\\": \\\"projects/agent_progress_probe/artifacts/_project/paper/related_work_60e275.tex\\\", \\\"url\\\": null, \\\"project\\\": \\\"agent_progress_probe\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-14T22:05:11.916403+00:00\\\", \\\"tags\\\": [\\\"paper\\\", \\\"related-work\\\", \\\"emnlp2026\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_60e275\", \"name\": \"related_work_section\", \"type\": \"paper\", \"description\": \"EMNLP 2026 ARR Related Work section (4 subsections: Agent Monitoring, PRMs, Data Programming/Weak Supervision, Anomaly Detection). ~750 words, 30+ citations.\", \"path\": \"projects/agent_progress_probe/artifacts/_project/paper/related_work_60e275.tex\", \"url\": null, \"project\": \"agent_progress_probe\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-14T22:05:11.916403+00:00\", \"tags\": [\"paper\", \"related-work\", \"emnlp2026\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 25_

Related Work 已写入 `docs/paper/sections/related_work.tex` 并注册。

**结构**（4 subsections，~750 词）：

1. **LLM Agent Monitoring and Evaluation** — failure taxonomies (Cemri, Zhu), degradation benchmarks (SlopCodeBench), self-reflection 的局限性 (Reflexion/ToT/LATS + self-correction 负面证据), cycle detection, weak-to-strong monitoring。定位：我们问的是 *what signals*，不是提新 method。

2. **Process Reward Models for Agents** — AgentPRM, InversePRM, ToolPRMBench, PlanRewardBench, Agent-RRM, DataPRM 全覆盖。三点差异：window-level vs step-level、无需 outcome labels、monitoring vs training signal。

3. **Data Programming and Weak Supervision** — Snorkel 体系 (data programming → Snorkel → FlyingSquid → WRENCH) + sequential extensions (linked HMM, multi-resolution WS, HMM-Crowd/Dawid-Skene)。定位：novel domain (agent trajectories) + TLM negative finding。

4. **Anomaly Detection in Agent Trajectories** — TrajAD 对比。定位：stagnation 是 persistent regime (28.5% prevalence)，不是 rare anomaly；structural features 无需训练即达 0.995 F1。

所有引用均取自现有 `references.bib`，无编造条目。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1311e2e5-9af4-44d3-8961-4a2f79dde730",
  "uuid": "48343e6c-c4b3-420e-9644-a830bfdb95f5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WmnETPFS5yp4Jt2DZ81JJx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 546,
      "cache_read_input_tokens": 50280,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 546
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

_source line 26_

Related Work 已写入 `docs/paper/sections/related_work.tex` 并注册。

**结构**（4 subsections，~750 词）：

1. **LLM Agent Monitoring and Evaluation** — failure taxonomies (Cemri, Zhu), degradation benchmarks (SlopCodeBench), self-reflection 的局限性 (Reflexion/ToT/LATS + self-correction 负面证据), cycle detection, weak-to-strong monitoring。定位：我们问的是 *what signals*，不是提新 method。

2. **Process Reward Models for Agents** — AgentPRM, InversePRM, ToolPRMBench, PlanRewardBench, Agent-RRM, DataPRM 全覆盖。三点差异：window-level vs step-level、无需 outcome labels、monitoring vs training signal。

3. **Data Programming and Weak Supervision** — Snorkel 体系 (data programming → Snorkel → FlyingSquid → WRENCH) + sequential extensions (linked HMM, multi-resolution WS, HMM-Crowd/Dawid-Skene)。定位：novel domain (agent trajectories) + TLM negative finding。

4. **Anomaly Detection in Agent Trajectories** — TrajAD 对比。定位：stagnation 是 persistent regime (28.5% prevalence)，不是 rare anomaly；structural features 无需训练即达 0.995 F1。

所有引用均取自现有 `references.bib`，无编造条目。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 90587,
  "duration_api_ms": 91104,
  "num_turns": 9,
  "stop_reason": "end_turn",
  "session_id": "1311e2e5-9af4-44d3-8961-4a2f79dde730",
  "total_cost_usd": 0.44374775,
  "usage": {
    "input_tokens": 10,
    "cache_creation_input_tokens": 38985,
    "cache_read_input_tokens": 207797,
    "output_tokens": 3778,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 38985,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 400,
        "cache_read_input_tokens": 50280,
        "cache_creation_input_tokens": 546,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 546
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1598,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001693,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 10,
      "outputTokens": 3778,
      "cacheReadInputTokens": 207797,
      "cacheCreationInputTokens": 38985,
      "webSearchRequests": 0,
      "costUSD": 0.44205474999999994,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "634100d2-c075-474f-8243-7cba41559fd0"
}
```

</details>

---
