# research literature supplement

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 70
- **Recorded user turns:** 0
- **Tool calls:** 24
- **Original source:** `logs/workers/worker_research_literature-supplement_20260514T054346.log`
- **Structured JSON:** [`8303b8a89576907a92a9.json`](../../sessions/83/8303b8a89576907a92a9.json)

## Before a recorded user message

70 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
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
  "uuid": "e3ea049f-384c-4f80-b4d3-164ea97eb5a4",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/memory/"
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
    "resetsAt": 1778753400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "2ac852c0-43ea-4617-a30e-8c498a2e06b8",
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418"
}
```

---

### Assistant

_source line 4_

I'll start by reading the existing literature_map.yaml, then search for all 6 papers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "06e7da51-0ad3-4dbd-8ea5-af676220c909",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SfL6yphBFoGWpexvTRjCi7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11840,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11840
      },
      "output_tokens": 4,
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01A3EhFgcC4mBxyC4FDU3Vye`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,WebSearch",
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
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "083b95a8-d237-4577-8146-3c11f98bb3c8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SfL6yphBFoGWpexvTRjCi7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11840,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11840
      },
      "output_tokens": 4,
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

_source line 6 · 2026-05-14T05:43:58.100Z_

<details><summary>↩ Tool result · `toolu_01A3EhFgcC4mBxyC4FDU3Vye`</summary>

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
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "18de5a1d-f5ef-4f44-9d8e-98821815e0fd",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file",
      "WebSearch"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,WebSearch",
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
Let me first read the existing literature_map.yaml, then search for all 6 papers in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "92528434-3c63-4437-a070-69881a4dbc24",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XTxAzS74Rc48zRxRVqLBYD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1226,
      "cache_read_input_tokens": 23681,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1226
      },
      "output_tokens": 47,
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01HBCvFhfyYdGuFWdCN8cLNK`</summary>

```json
{
  "project": "distrib_canary_collapse",
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
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "48c909ab-5f18-406e-a009-afa8b3c29faa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XTxAzS74Rc48zRxRVqLBYD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1226,
      "cache_read_input_tokens": 23681,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1226
      },
      "output_tokens": 47,
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

_source line 9 · 2026-05-14T05:44:01.371Z_

<details><summary>↩ Tool result · `toolu_01HBCvFhfyYdGuFWdCN8cLNK`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/literature_map.yaml\", \"content\": \"papers:\\n  # ============================================================\\n  # CORE MODEL COLLAPSE\\n  # ============================================================\\n  - id: \\\"shumailov2024curse\\\"\\n    title: \\\"The Curse of Recursion: Training on Generated Data Makes Models Forget\\\"\\n    authors: \\\"Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Yarin Gal, Nicolas Papernot, Ross Anderson\\\"\\n    venue: \\\"Nature\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2305.17493\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"foundation\\\"\\n    key_findings:\\n      - \\\"定义 model collapse 现象：迭代用合成数据替换真实数据训练会导致分布尾部消失\\\"\\n      - \\\"区分 early model collapse（尾部信息丢失）和 late model collapse（分布完全收敛）\\\"\\n      - \\\"三类误差来源：statistical approximation, functional expressivity, functional approximation，跨代复合\\\"\\n      - \\\"在 VAE、GMM、LLM 上均验证了 collapse 的普遍性\\\"\\n    relevance_to_us: \\\"奠基论文，定义了我们研究的核心现象。我们的 canary 指标旨在提前检测其描述的 early collapse 阶段\\\"\\n    metrics_studied: [\\\"perplexity\\\", \\\"distributional tail mass\\\"]\\n\\n  - id: \\\"alemohammad2024mad\\\"\\n    title: \\\"Self-Consuming Generative Models Go MAD\\\"\\n    authors: \\\"Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, Richard Baraniuk\\\"\\n    venue: \\\"ICLR 2024\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2307.01850\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"foundation\\\"\\n    key_findings:\\n      - \\\"提出 Model Autophagy Disorder (MAD) 概念\\\"\\n      - \\\"autophagous loop 中没有足够新鲜真实数据时，质量或多样性必然渐进下降\\\"\\n      - \\\"在图像生成领域验证 self-consuming loop 的退化效应\\\"\\n    relevance_to_us: \\\"MAD 框架与我们的 iterative loop 设置直接对应；其 quality vs diversity tradeoff 可能反映在不同 canary 指标上\\\"\\n    metrics_studied: [\\\"FID\\\", \\\"precision\\\", \\\"recall\\\", \\\"diversity\\\"]\\n\\n  - id: \\\"dohmatob2024tale\\\"\\n    title: \\\"A Tale of Tails: Model Collapse as a Change of Scaling Laws\\\"\\n    authors: \\\"Elvis Dohmatob, Yunzhen Feng, et al.\\\"\\n    venue: \\\"ICML 2024\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2402.07043\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"foundation\\\"\\n    key_findings:\\n      - \\\"通过 scaling laws 视角分析 model collapse：collapse 表现为 scaling law 的变化\\\"\\n      - \\\"发现 loss of scaling, shifted scaling, skill un-learning, grokking 等多种退化模式\\\"\\n      - \\\"混入少量干净数据可缓解 collapse 并引发 grokking 现象\\\"\\n      - \\\"在 transformer 算术任务和 Llama2 文本生成上验证\\\"\\n    relevance_to_us: \\\"scaling law 变化视角为我们提供了理论基础；grokking 现象暗示 canary 指标可能出现非单调行为\\\"\\n    metrics_studied: [\\\"test loss\\\", \\\"scaling exponents\\\"]\\n\\n  - id: \\\"dohmatob2025strong\\\"\\n    title: \\\"Strong Model Collapse\\\"\\n    authors: \\\"Elvis Dohmatob, Yunzhen Feng, Arjun Subramonian, Julia Kempe\\\"\\n    venue: \\\"ICLR 2025 (Spotlight)\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2410.04840\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"foundation\\\"\\n    key_findings:\\n      - \\\"即使合成数据占比极小（1/1000），仍可导致 model collapse\\\"\\n      - \\\"更大的训练集并不能避免 collapse\\\"\\n      - \\\"更大的模型（random projection 近似下）反而可能放大 collapse\\\"\\n      - \\\"存在 interpolation threshold 的 double-descent 现象\\\"\\n    relevance_to_us: \\\"强化了早期检测的必要性——即使极小的合成数据比例也能触发 collapse，因此 canary 指标必须敏感\\\"\\n    metrics_studied: [\\\"test loss\\\", \\\"population risk\\\"]\\n\\n  - id: \\\"guo2024linguistic\\\"\\n    title: \\\"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\\\"\\n    authors: \\\"Yanzhu Guo, Guokan Shang, et al.\\\"\\n    venue: \\\"NAACL 2024 Findings\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2311.09807\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"evaluation\\\"\\n    key_findings:\\n      - \\\"递归微调中，linguistic diversity 在连续迭代中持续下降\\\"\\n      - \\\"创造性任务中 diversity 下降最显著\\\"\\n      - \\\"开发了覆盖 lexical、syntactic、semantic 三层的 diversity 指标体系\\\"\\n    relevance_to_us: \\\"其多层 diversity 指标体系可直接作为我们 canary 指标的候选集；创造性 vs 事实任务的差异可能影响 canary 灵敏度\\\"\\n    metrics_studied: [\\\"distinct-n\\\", \\\"type-token ratio\\\", \\\"syntactic diversity\\\", \\\"semantic diversity\\\"]\\n\\n  - id: \\\"briesch2024selfconsuming\\\"\\n    title: \\\"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop\\\"\\n    authors: \\\"Martin Briesch, Dominik Sobania, Franz Rothlauf\\\"\\n    venue: \\\"arXiv (2311.16822)\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2311.16822\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"direct-competitor\\\"\\n    key_findings:\\n      - \\\"首次系统研究 LLM 的 self-consuming training loop\\\"\\n      - \\\"full synthetic cycle（完全替换）导致单点 collapse；data augmentation cycle 导致 diversity 缓慢下降\\\"\\n      - \\\"expanding data cycle（累积）在 50 代内保持 diversity\\\"\\n    relevance_to_us: \\\"其不同 data cycle 策略的对比直接对应我们的 alpha（synthetic ratio）实验设置\\\"\\n    metrics_studied: [\\\"diversity\\\", \\\"quality\\\"]\\n\\n  # ============================================================\\n  # CANARY / EARLY WARNING METRICS\\n  # ============================================================\\n  - id: \\\"chen2025scales\\\"\\n    title: \\\"Characterizing Model Behavior Under Synthetic Data Training: An Empirical Study Across Scales and Mixing Ratios\\\"\\n    authors: \\\"Anonymous\\\"\\n    venue: \\\"arXiv (2510.05133)\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2510.05133\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"direct-competitor\\\"\\n    key_findings:\\n      - \\\"**Calibration degradation precedes accuracy loss** — ECE 是 collapse 的 early warning signal\\\"\\n      - \\\"20% synthetic data 以下性能稳定，30% 以上退化加速\\\"\\n      - \\\"大模型（6.9B-12B）比小模型（410M-1.4B）更鲁棒\\\"\\n      - \\\"推理任务比检索任务更易退化\\\"\\n      - \\\"iteration 1 + 30% synthetic 时 ECE 从 0.08 升至 0.14（+75%）\\\"\\n    relevance_to_us: \\\"**最直接的竞争者/先驱**。证实 ECE 可作为 canary，但未做 lead-lag 分析，未建立多指标 panel 框架\\\"\\n    metrics_studied: [\\\"ECE\\\", \\\"accuracy\\\", \\\"perplexity\\\"]\\n\\n  - id: \\\"gambetta2024surplexity\\\"\\n    title: \\\"Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI\\\"\\n    authors: \\\"Daniele Gambetta et al.\\\"\\n    venue: \\\"arXiv (2410.12341)\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2410.12341\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"direct-competitor\\\"\\n    key_findings:\\n      - \\\"提出 surplexity（model surprise 度量）同时用于检测 collapse 和过滤训练数据\\\"\\n      - \\\"用 semantic networks 分析文本重复性和语义多样性\\\"\\n      - \\\"用 next-token probability 定量衡量 diversity loss\\\"\\n      - \\\"高 surplexity 过滤策略至少与 human-data baseline 同效，且更能降低分布偏斜\\\"\\n      - \\\"不需要区分 human vs AI-generated data\\\"\\n    relevance_to_us: \\\"surplexity 可作为我们 canary 指标候选之一；其 semantic network 方法提供了 diversity 度量的另一视角\\\"\\n    metrics_studied: [\\\"surplexity\\\", \\\"semantic network metrics\\\", \\\"next-token probability\\\"]\\n\\n  - id: \\\"qiu2025spectral\\\"\\n    title: \\\"Spectral Alignment as Predictor of Loss Explosion in Neural Network Training\\\"\\n    authors: \\\"Haiquan Qiu, You Wu, Yingjie Tan, Yaqing Wang, Quanming Yao\\\"\\n    venue: \\\"arXiv (2510.04202)\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2510.04202\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"method-component\\\"\\n    key_findings:\\n      - \\\"Spectral Alignment (SA) 监控层输入与权重矩阵主奇异向量的分布对齐\\\"\\n      - \\\"SA sign diversity collapse 是 representational collapse 和训练发散的早期预测器\\\"\\n      - \\\"比 weight norm、gradient norm 等传统指标更早、更清晰地检测到训练失败\\\"\\n      - \\\"健康层的 SA 应有正负均衡分布，collapse 到单侧则预示不稳定\\\"\\n    relevance_to_us: \\\"SA 是潜在的高价值 canary 指标——专门设计为 early warning，可直接纳入我们的指标 panel\\\"\\n    metrics_studied: [\\\"spectral alignment\\\", \\\"weight norm\\\", \\\"gradient norm\\\"]\\n\\n  - id: \\\"he2025closer\\\"\\n    title: \\\"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\\\"\\n    authors: \\\"Shiliang He et al.\\\"\\n    venue: \\\"NeurIPS 2025 (Spotlight)\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2509.16499\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"direct-competitor\\\"\\n    key_findings:\\n      - \\\"识别 diffusion model collapse 中的 generalization → memorization 转变\\\"\\n      - \\\"**训练数据的 entropy 递减是 collapse 的直接驱动因素和清晰指标**\\\"\\n      - \\\"提出基于 entropy 的数据选择策略，有效缓解 collapse\\\"\\n    relevance_to_us: \\\"data entropy 作为 canary 的有效性已被验证（diffusion domain）；需测试是否在 LLM 场景同样有效\\\"\\n    metrics_studied: [\\\"entropy\\\", \\\"FID\\\", \\\"diversity\\\"]\\n\\n  - id: \\\"ba2024fill\\\"\\n    title: \\\"Fill In The Gaps: Model Calibration and Generalization with Synthetic Data\\\"\\n    authors: \\\"Yang Ba, Michelle V Mancenido, Rong Pan\\\"\\n    venue: \\\"EMNLP 2024\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2410.10864\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"background\\\"\\n    key_findings:\\n      - \\\"用 LLM 生成合成数据来修复 calibration 错误的 reliability diagram bins\\\"\\n      - \\\"推导了基于 PAC 框架的 ECE bound\\\"\\n      - \\\"合成数据可改善 calibration 但需精心设计生成策略\\\"\\n    relevance_to_us: \\\"ECE 的理论 bound 可为我们的 canary 阈值设定提供理论依据\\\"\\n    metrics_studied: [\\\"ECE\\\", \\\"accuracy\\\"]\\n\\n  # ============================================================\\n  # DIVERSITY METRICS (BACKGROUND)\\n  # ============================================================\\n  - id: \\\"zhu2018texygen\\\"\\n    title: \\\"Texygen: A Benchmarking Platform for Text Generation Models\\\"\\n    authors: \\\"Yaoming Zhu et al.\\\"\\n    venue: \\\"SIGIR 2018\\\"\\n    year: 2018\\n    url: \\\"https://arxiv.org/abs/1802.01886\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"background\\\"\\n    key_findings:\\n      - \\\"提出 Self-BLEU 度量：计算生成句子间的 BLEU 相似度，Self-BLEU 越高多样性越低\\\"\\n      - \\\"成为文本生成多样性评估的标准基准之一\\\"\\n    relevance_to_us: \\\"Self-BLEU 是我们 diversity canary 的经典候选\\\"\\n    metrics_studied: [\\\"Self-BLEU\\\", \\\"BLEU\\\"]\\n\\n  - id: \\\"li2016diversity\\\"\\n    title: \\\"A Diversity-Promoting Objective Function for Neural Conversation Models\\\"\\n    authors: \\\"Jiwei Li et al.\\\"\\n    venue: \\\"NAACL 2016\\\"\\n    year: 2016\\n    url: \\\"https://arxiv.org/abs/1510.03055\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"background\\\"\\n    key_findings:\\n      - \\\"提出 distinct-1 / distinct-2 指标衡量生成文本的 n-gram 多样性\\\"\\n      - \\\"计算 unique n-gram 数占总 n-gram 数的比例\\\"\\n    relevance_to_us: \\\"distinct-n 是最廉价的 diversity canary 之一，计算开销极低\\\"\\n    metrics_studied: [\\\"distinct-1\\\", \\\"distinct-2\\\"]\\n\\n  # ============================================================\\n  # REPRESENTATION / SPECTRAL COLLAPSE\\n  # ============================================================\\n  - id: \\\"jing2022understanding\\\"\\n    title: \\\"Understanding Dimensional Collapse in Contrastive Self-supervised Learning\\\"\\n    authors: \\\"Li Jing et al.\\\"\\n    venue: \\\"ICLR 2022\\\"\\n    year: 2022\\n    url: \\\"https://openreview.net/forum?id=YevsQ05DEN7\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"method-component\\\"\\n    key_findings:\\n      - \\\"定义 dimensional collapse：embedding 向量只跨越低维子空间\\\"\\n      - \\\"effective rank（基于归一化特征值 entropy 的指数）作为 collapse 度量\\\"\\n      - \\\"strong augmentation 和 implicit regularization 驱动低秩解\\\"\\n    relevance_to_us: \\\"effective rank 的定义和计算方式可直接迁移到我们的 embedding 空间监控\\\"\\n    metrics_studied: [\\\"effective rank\\\", \\\"singular value spectrum\\\"]\\n\\n  - id: \\\"noci2024mind\\\"\\n    title: \\\"Mind the Gap: A Spectral Analysis of Rank Collapse and Signal Propagation in Transformers\\\"\\n    authors: \\\"Lorenzo Noci et al.\\\"\\n    venue: \\\"NeurIPS 2024\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2410.07799\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"method-component\\\"\\n    key_findings:\\n      - \\\"用 Random Matrix Theory 分析 attention 层的 rank collapse\\\"\\n      - \\\"发现 attention matrix 最大两个奇异值之间的 spectral gap 是 width-collapse 的根因\\\"\\n      - \\\"rank collapse in depth: 所有 token 沿层收敛到单一表示\\\"\\n    relevance_to_us: \\\"spectral gap 作为另一种 spectral canary 候选；其 RMT 分析框架可启发我们的理论工作\\\"\\n    metrics_studied: [\\\"spectral gap\\\", \\\"singular values\\\", \\\"effective rank\\\"]\\n\\n  # ============================================================\\n  # DATA MIXING & ACCUMULATION\\n  # ============================================================\\n  - id: \\\"kazdan2025collapse\\\"\\n    title: \\\"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World\\\"\\n    authors: \\\"Joshua Kazdan, Rylan Schaeffer, Apratim Dey, Matthias Gerstgrasser, Rafael Rafailov, David L. Donoho, Sanmi Koyejo\\\"\\n    venue: \\\"ICML 2025\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2410.16713\\\"\\n    category: \\\"data-mixing\\\"\\n    role: \\\"foundation\\\"\\n    key_findings:\\n      - \\\"系统对比 replace vs accumulate 场景\\\"\\n      - \\\"replace → collapse；accumulate → 可避免 collapse\\\"\\n      - \\\"发现 real data 和 synthetic data 之间存在非平凡的交互效应\\\"\\n      - \\\"synthetic data 的价值取决于 real data 的绝对数量\\\"\\n    relevance_to_us: \\\"直接对应我们的 alpha（mixing ratio）实验维度；其 replace vs accumulate 框架是我们实验设计的重要参考\\\"\\n    metrics_studied: [\\\"test loss\\\"]\\n\\n  - id: \\\"dey2024breaking\\\"\\n    title: \\\"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\\\"\\n    authors: \\\"Apratim Dey, David Donoho, et al.\\\"\\n    venue: \\\"ICML 2024\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2404.01413\\\"\\n    category: \\\"data-mixing\\\"\\n    role: \\\"foundation\\\"\\n    key_findings:\\n      - \\\"替换数据 → 发散 population risk；累积数据 → 避免发散\\\"\\n      - \\\"证明累积策略在多种模型（GMM, HMM, LLM）上有效\\\"\\n    relevance_to_us: \\\"为我们的 alpha 实验提供理论预测：累积 vs 替换是 collapse 速率的关键调节因子\\\"\\n    metrics_studied: [\\\"population risk\\\"]\\n\\n  - id: \\\"epstein2024howbad\\\"\\n    title: \\\"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse\\\"\\n    authors: \\\"Mohamed El Amine Epstein et al.\\\"\\n    venue: \\\"arXiv (2404.05090)\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2404.05090\\\"\\n    category: \\\"data-mixing\\\"\\n    role: \\\"background\\\"\\n    key_findings:\\n      - \\\"纯合成数据训练不可避免 collapse\\\"\\n      - \\\"给出 synthetic data 比例上界的估计——低于此比例可避免 collapse\\\"\\n      - \\\"递归训练使原始分布尾部消失\\\"\\n    relevance_to_us: \\\"其 mixing ratio 上界估计可对比我们实验中观测到的 canary 触发阈值\\\"\\n    metrics_studied: [\\\"perplexity\\\"]\\n\\n  - id: \\\"bakshi2026improvement\\\"\\n    title: \\\"From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources\\\"\\n    authors: \\\"Soham Bakshi et al.\\\"\\n    venue: \\\"arXiv (2602.10531)\\\"\\n    year: 2026\\n    url: \\\"https://arxiv.org/abs/2602.10531\\\"\\n    category: \\\"data-mixing\\\"\\n    role: \\\"background\\\"\\n    key_findings:\\n      - \\\"即使真实数据比例随时间衰减，只要非零就可能避免 collapse 并恢复真实分布\\\"\\n      - \\\"在 next-token prediction 语言模型上分析混合训练的动态\\\"\\n    relevance_to_us: \\\"提供了 decaying real data fraction 的理论保证，与我们的实验中 alpha 变化场景相关\\\"\\n    metrics_studied: [\\\"population risk\\\"]\\n\\n  # ============================================================\\n  # MITIGATION & VERIFICATION\\n  # ============================================================\\n  - id: \\\"feng2025escaping\\\"\\n    title: \\\"Escaping Model Collapse via Synthetic Data Verification\\\"\\n    authors: \\\"Yunzhen Feng et al.\\\"\\n    venue: \\\"NeurIPS 2025\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2510.16657\\\"\\n    category: \\\"data-mixing\\\"\\n    role: \\\"background\\\"\\n    key_findings:\\n      - \\\"通过外部 verifier（human 或 better model）注入信息可避免 collapse\\\"\\n      - \\\"verifier-guided retraining 带来短期改善，但最终收敛到 verifier 的 knowledge center\\\"\\n      - \\\"除非 verifier 完全可靠，早期收益会 plateau 甚至逆转\\\"\\n    relevance_to_us: \\\"verification 作为 intervention 策略——如果 canary 触发，可考虑此类 reactive intervention\\\"\\n    metrics_studied: [\\\"test loss\\\"]\\n\\n  - id: \\\"barzilai2025consistency\\\"\\n    title: \\\"When Models Don't Collapse: On the Consistency of Iterative MLE\\\"\\n    authors: \\\"Daniel Barzilai, Ohad Shamir\\\"\\n    venue: \\\"ICML 2025\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2505.19046\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"background\\\"\\n    key_findings:\\n      - \\\"在标准 MLE 一致性假设下，即使 real data fraction 趋近零也可避免 collapse\\\"\\n      - \\\"但证明了某些情况下 collapse 可以任意快地发生——首次给出严格 collapse 反例\\\"\\n    relevance_to_us: \\\"理论上的 collapse 可发生任意快的结论强化了 early warning 的价值\\\"\\n    metrics_studied: []\\n\\n  - id: \\\"dces2026counter\\\"\\n    title: \\\"Countering Model Collapse in Iterative Self-Training via Dynamic Center-Edge Sampling\\\"\\n    authors: \\\"Anonymous\\\"\\n    venue: \\\"MDPI Electronics (2026)\\\"\\n    year: 2026\\n    url: \\\"https://www.mdpi.com/2079-9292/15/4/869\\\"\\n    category: \\\"data-mixing\\\"\\n    role: \\\"background\\\"\\n    key_findings:\\n      - \\\"提出 DCES（dynamic center-edge sampling）数据选择框架\\\"\\n      - \\\"DCES 在 ECE（0.1058 vs 0.1200）和 entropy 保持上优于随机选择\\\"\\n    relevance_to_us: \\\"其 ECE 和 entropy 对比数据为我们的指标 baseline 提供参考\\\"\\n    metrics_studied: [\\\"ECE\\\", \\\"entropy\\\"]\\n\\n  # ============================================================\\n  # POSITION / SURVEY / EPISTEMICS\\n  # ============================================================\\n  - id: \\\"schaeffer2025position\\\"\\n    title: \\\"Position: Model Collapse Does Not Mean What You Think\\\"\\n    authors: \\\"Rylan Schaeffer, Joshua Kazdan, Alvan Caleb Arulandu, Sanmi Koyejo\\\"\\n    venue: \\\"arXiv (2503.03150)\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2503.03150\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"background\\\"\\n    key_findings:\\n      - \\\"文献中实际包含 8 种不同且有时矛盾的 model collapse 定义\\\"\\n      - \\\"许多 collapse 预测依赖于与现实不符的假设\\\"\\n      - \\\"多种 collapse 场景是可以轻易避免的\\\"\\n    relevance_to_us: \\\"提醒我们明确定义 collapse 的操作标准；不同定义可能需要不同的 canary 指标\\\"\\n    metrics_studied: []\\n\\n  - id: \\\"wang2025epistemic\\\"\\n    title: \\\"Epistemic Diversity and Knowledge Collapse in Large Language Models\\\"\\n    authors: \\\"Wang et al.\\\"\\n    venue: \\\"arXiv (2510.04226)\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2510.04226\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"background\\\"\\n    key_findings:\\n      - \\\"27 个 LLM 在 155 个主题上的 epistemic diversity 评估\\\"\\n      - \\\"所有模型的 epistemic diversity 低于基本 web 搜索\\\"\\n      - \\\"模型越大 epistemic diversity 反而越低；RAG 有正面效果\\\"\\n    relevance_to_us: \\\"knowledge collapse 维度可扩展我们对 diversity canary 的理解——不仅是 lexical/syntactic 还有 epistemic\\\"\\n    metrics_studied: [\\\"epistemic diversity\\\"]\\n\\n  # ============================================================\\n  # METHODOLOGY (GRANGER / LEAD-LAG)\\n  # ============================================================\\n  - id: \\\"shojaie2022granger\\\"\\n    title: \\\"Granger Causality: A Review and Recent Advances\\\"\\n    authors: \\\"Ali Shojaie, Emily B. Fox\\\"\\n    venue: \\\"Annual Review of Statistics and Its Application\\\"\\n    year: 2022\\n    url: \\\"https://arxiv.org/abs/2105.02675\\\"\\n    category: \\\"methodology\\\"\\n    role: \\\"method-component\\\"\\n    key_findings:\\n      - \\\"Granger causality 综述：从经典线性到非线性/neural 方法\\\"\\n      - \\\"Panel data 场景的 Granger causality 扩展\\\"\\n      - \\\"VAR 和 neural Granger causality 的对比\\\"\\n    relevance_to_us: \\\"为我们的 panel Granger causality 分析提供方法论基础\\\"\\n    metrics_studied: []\\n\\n  - id: \\\"marcinkevics2022neural\\\"\\n    title: \\\"Granger Causality Using Neural Networks\\\"\\n    authors: \\\"Raphael Marcinkevics, Julia Vogt\\\"\\n    venue: \\\"arXiv (2208.03703)\\\"\\n    year: 2022\\n    url: \\\"https://arxiv.org/abs/2208.03703\\\"\\n    category: \\\"methodology\\\"\\n    role: \\\"method-component\\\"\\n    key_findings:\\n      - \\\"用 neural network 估计 Granger causality，突破线性假设\\\"\\n      - \\\"两个模型对比法：含/不含外生变量的预测误差差异即 Granger causality 证据\\\"\\n    relevance_to_us: \\\"我们的多指标时序可能存在非线性关系，neural Granger causality 是自然选择\\\"\\n    metrics_studied: []\\n\\ngaps:\\n  - \\\"无人系统做过 canary 指标的 lead-lag / Granger causality 分析——现有工作只在事后观察到指标变化，未量化哪些指标能提前多少步预测 collapse\\\"\\n  - \\\"ECE 在 collapse 场景下几乎未被系统研究——chen2025scales 是唯一报告 ECE 先于 accuracy 退化的工作，但未做因果分析\\\"\\n  - \\\"embedding effective rank 未在 iterative synthetic training 场景下被测试——仅在 contrastive learning/transformer 训练中研究过\\\"\\n  - \\\"多指标 panel 框架缺失——无人同时追踪 ECE + effective rank + diversity + perplexity 的时序行为并分析其 lead-lag 关系\\\"\\n  - \\\"alpha（synthetic ratio）对 canary 灵敏度的影响未被研究——现有工作只关注 alpha 对最终性能的影响，不关注 canary 的 lead time 如何随 alpha 变化\\\"\\n  - \\\"predictive intervention vs reactive intervention 缺少对比——没有工作量化 early warning 带来的实际干预收益\\\"\\n  - \\\"surplexity 和 spectral alignment 未在 iterative collapse 场景下交叉验证\\\"\\n  - \\\"跨任务 canary 普适性未知——reasoning vs retrieval vs creative tasks 中哪些 canary 更可靠\\\"\\n\\nnovelty_assessment: |\\n  我们项目的核心 novelty 在于：\\n\\n  1. **Panel Granger Causality 框架**：首次将多指标时序数据的因果分析方法应用于 model collapse 早期预警。\\n     现有工作（chen2025scales, gambetta2024surplexity）只是事后观察到某些指标先变化，\\n     但没有人做过系统的 lead-lag 量化分析。\\n\\n  2. **多指标 Canary Panel**：同时追踪 ECE、effective rank、Self-BLEU/distinct-n、\\n     perplexity、entropy、surplexity 等指标，分析其相互关系和各自的 lead time。\\n     现有工作都是单一指标或最多两三个指标的孤立分析。\\n\\n  3. **alpha-dependent Canary Sensitivity**：系统研究 synthetic ratio 如何影响各 canary\\n     指标的灵敏度和 lead time。dohmatob2025strong 证明极小的 alpha 就能触发 collapse，\\n     但没人研究 canary 在不同 alpha 下的行为。\\n\\n  4. **与已有工作的差异**：\\n     - vs chen2025scales: 他们发现 ECE 先退化但没有做因果分析；我们用 Granger causality 量化\\n     - vs gambetta2024surplexity: 他们提出 surplexity 用于检测和缓解 collapse；\\n       我们将其纳入更广的 panel 并研究其 lead-lag 特性\\n     - vs he2025closer: 他们在 diffusion 中用 entropy 作为指标；我们在 LLM 中测试更多指标\\n     - vs qiu2025spectral: 他们的 SA 用于训练 loss explosion 预警；\\n       我们将类似思路迁移到 iterative collapse 场景\\n\\n  5. **潜在风险**：chen2025scales 已经非常接近我们的方向。如果他们扩展到 lead-lag 分析，\\n     我们的 novelty 会被削弱。需要快速推进并在方法论（Granger causality）上建立壁垒。\\n\", \"total_chars\": 19466, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "f1ffd4ea-a41a-476d-b466-d85ea13ebf4f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/literature_map.yaml\\\", \\\"content\\\": \\\"papers:\\\\n  # ============================================================\\\\n  # CORE MODEL COLLAPSE\\\\n  # ============================================================\\\\n  - id: \\\\\\\"shumailov2024curse\\\\\\\"\\\\n    title: \\\\\\\"The Curse of Recursion: Training on Generated Data Makes Models Forget\\\\\\\"\\\\n    authors: \\\\\\\"Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Yarin Gal, Nicolas Papernot, Ross Anderson\\\\\\\"\\\\n    venue: \\\\\\\"Nature\\\\\\\"\\\\n    year: 2024\\\\n    url: \\\\\\\"https://arxiv.org/abs/2305.17493\\\\\\\"\\\\n    category: \\\\\\\"core-collapse\\\\\\\"\\\\n    role: \\\\\\\"foundation\\\\\\\"\\\\n    key_findings:\\\\n      - \\\\\\\"定义 model collapse 现象：迭代用合成数据替换真实数据训练会导致分布尾部消失\\\\\\\"\\\\n      - \\\\\\\"区分 early model collapse（尾部信息丢失）和 late model collapse（分布完全收敛）\\\\\\\"\\\\n      - \\\\\\\"三类误差来源：statistical approximation, functional expressivity, functional approximation，跨代复合\\\\\\\"\\\\n      - \\\\\\\"在 VAE、GMM、LLM 上均验证了 collapse 的普遍性\\\\\\\"\\\\n    relevance_to_us: \\\\\\\"奠基论文，定义了我们研究的核心现象。我们的 canary 指标旨在提前检测其描述的 early collapse 阶段\\\\\\\"\\\\n    metrics_studied: [\\\\\\\"perplexity\\\\\\\", \\\\\\\"distributional tail mass\\\\\\\"]\\\\n\\\\n  - id: \\\\\\\"alemohammad2024mad\\\\\\\"\\\\n    title: \\\\\\\"Self-Consuming Generative Models Go MAD\\\\\\\"\\\\n    authors: \\\\\\\"Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, Richard Baraniuk\\\\\\\"\\\\n    venue: \\\\\\\"ICLR 2024\\\\\\\"\\\\n    year: 2024\\\\n    url: \\\\\\\"https://arxiv.org/abs/2307.01850\\\\\\\"\\\\n    category: \\\\\\\"core-collapse\\\\\\\"\\\\n    role: \\\\\\\"foundation\\\\\\\"\\\\n    key_findings:\\\\n      - \\\\\\\"提出 Model Autophagy Disorder (MAD) 概念\\\\\\\"\\\\n      - \\\\\\\"autophagous loop 中没有足够新鲜真实数据时，质量或多样性必然渐进下降\\\\\\\"\\\\n      - \\\\\\\"在图像生成领域验证 self-consuming loop 的退化效应\\\\\\\"\\\\n    relevance_to_us: \\\\\\\"MAD 框架与我们的 iterative loop 设置直接对应；其 quality vs diversity tradeoff 可能反映在不同 canary 指标上\\\\\\\"\\\\n    metrics_studied: [\\\\\\\"FID\\\\\\\", \\\\\\\"precision\\\\\\\", \\\\\\\"recall\\\\\\\", \\\\\\\"diversity\\\\\\\"]\\\\n\\\\n  - id: \\\\\\\"dohmatob2024tale\\\\\\\"\\\\n    title: \\\\\\\"A Tale of Tails: Model Collapse as a Change of Scaling Laws\\\\\\\"\\\\n    authors: \\\\\\\"Elvis Dohmatob, Yunzhen Feng, et al.\\\\\\\"\\\\n    venue: \\\\\\\"ICML 2024\\\\\\\"\\\\n    year: 2024\\\\n    url: \\\\\\\"https://arxiv.org/abs/2402.07043\\\\\\\"\\\\n    category: \\\\\\\"core-collapse\\\\\\\"\\\\n    role: \\\\\\\"foundation\\\\\\\"\\\\n    key_findings:\\\\n      - \\\\\\\"通过 scaling laws 视角分析 model collapse：collapse 表现为 scaling law 的变化\\\\\\\"\\\\n      - \\\\\\\"发现 loss of scaling, shifted scaling, skill un-learning, grokking 等多种退化模式\\\\\\\"\\\\n      - \\\\\\\"混入少量干净数据可缓解 collapse 并引发 grokking 现象\\\\\\\"\\\\n      - \\\\\\\"在 transformer 算术任务和 Llama2 文本生成上验证\\\\\\\"\\\\n    relevance_to_us: \\\\\\\"scaling law 变化视角为我们提供了理论基础；grokking 现象暗示 canary 指标可能出现非单调行为\\\\\\\"\\\\n    metrics_studied: [\\\\\\\"test loss\\\\\\\", \\\\\\\"scaling exponents\\\\\\\"]\\\\n\\\\n  - id: \\\\\\\"dohmatob2025strong\\\\\\\"\\\\n    title: \\\\\\\"Strong Model Collapse\\\\\\\"\\\\n    authors: \\\\\\\"Elvis Dohmatob, Yunzhen Feng, Arjun Subramonian, Julia Kempe\\\\\\\"\\\\n    venue: \\\\\\\"ICLR 2025 (Spotlight)\\\\\\\"\\\\n    year: 2025\\\\n    url: \\\\\\\"https://arxiv.org/abs/2410.04840\\\\\\\"\\\\n    category: \\\\\\\"core-collapse\\\\\\\"\\\\n    role: \\\\\\\"foundation\\\\\\\"\\\\n    key_findings:\\\\n      - \\\\\\\"即使合成数据占比极小（1/1000），仍可导致 model collapse\\\\\\\"\\\\n      - \\\\\\\"更大的训练集并不能避免 collapse\\\\\\\"\\\\n      - \\\\\\\"更大的模型（random projection 近似下）反而可能放大 collapse\\\\\\\"\\\\n      - \\\\\\\"存在 interpolation threshold 的 double-descent 现象\\\\\\\"\\\\n    relevance_to_us: \\\\\\\"强化了早期检测的必要性——即使极小的合成数据比例也能触发 collapse，因此 canary 指标必须敏感\\\\\\\"\\\\n    metrics_studied: [\\\\\\\"test loss\\\\\\\", \\\\\\\"population risk\\\\\\\"]\\\\n\\\\n  - id: \\\\\\\"guo2024linguistic\\\\\\\"\\\\n    title: \\\\\\\"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\\\\\\\"\\\\n    authors: \\\\\\\"Yanzhu Guo, Guokan Shang, et al.\\\\\\\"\\\\n    venue: \\\\\\\"NAACL 2024 Findings\\\\\\\"\\\\n    year: 2024\\\\n    url: \\\\\\\"https://arxiv.org/abs/2311.09807\\\\\\\"\\\\n    category: \\\\\\\"core-collapse\\\\\\\"\\\\n    role: \\\\\\\"evaluation\\\\\\\"\\\\n    key_findings:\\\\n      - \\\\\\\"递归微调中，linguistic diversity 在连续迭代中持续下降\\\\\\\"\\\\n      - \\\\\\\"创造性任务中 diversity 下降最显著\\\\\\\"\\\\n      - \\\\\\\"开发了覆盖 lexical、syntactic、semantic 三层的 diversity 指标体系\\\\\\\"\\\\n    relevance_to_us: \\\\\\\"其多层 diversity 指标体系可直接作为我们 canary 指标的候选集；创造性 vs 事实任务的差异可能影响 canary 灵敏度\\\\\\\"\\\\n    metrics_studied: [\\\\\\\"distinct-n\\\\\\\", \\\\\\\"type-token ratio\\\\\\\", \\\\\\\"syntactic diversity\\\\\\\", \\\\\\\"semantic diversity\\\\\\\"]\\\\n\\\\n  - id: \\\\\\\"briesch2024selfconsuming\\\\\\\"\\\\n    title: \\\\\\\"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop\\\\\\\"\\\\n    authors: \\\\\\\"Martin Briesch, Dominik Sobania, Franz Rothlauf\\\\\\\"\\\\n    venue: \\\\\\\"arXiv (2311.16822)\\\\\\\"\\\\n    year: 2024\\\\n    url: \\\\\\\"https://arxiv.org/abs/2311.16822\\\\\\\"\\\\n    category: \\\\\\\"core-collapse\\\\\\\"\\\\n    role: \\\\\\\"direct-competitor\\\\\\\"\\\\n    key_findings:\\\\n      - \\\\\\\"首次系统研究 LLM 的 self-consuming training loop\\\\\\\"\\\\n      - \\\\\\\"full synthetic cycle（完全替换）导致单点 collapse；data augmentation cycle 导致 diversity 缓慢下降\\\\\\\"\\\\n      - \\\\\\\"expanding data cycle（累积）在 50 代内保持 diversity\\\\\\\"\\\\n    relevance_to_us: \\\\\\\"其不同 data cycle 策略的对比直接对应我们的 alpha（synthetic ratio）实验设置\\\\\\\"\\\\n    metrics_studied: [\\\\\\\"diversity\\\\\\\", \\\\\\\"quality\\\\\\\"]\\\\n\\\\n  # ============================================================\\\\n  # CANARY / EARLY WARNING METRICS\\\\n  # ============================================================\\\\n  - id: \\\\\\\"chen2025scales\\\\\\\"\\\\n    title: \\\\\\\"Characterizing Model Behavior Under Synthetic Data Training: An Empirical Study Across Scales and Mixing Ratios\\\\\\\"\\\\n    authors: \\\\\\\"Anonymous\\\\\\\"\\\\n    venue: \\\\\\\"arXiv (2510.05133)\\\\\\\"\\\\n    year: 2025\\\\n    url: \\\\\\\"https://arxiv.org/abs/2510.05133\\\\\\\"\\\\n    category: \\\\\\\"canary-metrics\\\\\\\"\\\\n    role: \\\\\\\"direct-competitor\\\\\\\"\\\\n    key_findings:\\\\n      - \\\\\\\"**Calibration degradation precedes accuracy loss** — ECE 是 collapse 的 early warning signal\\\\\\\"\\\\n      - \\\\\\\"20% synthetic data 以下性能稳定，30% 以上退化加速\\\\\\\"\\\\n      - \\\\\\\"大模型（6.9B-12B）比小模型（410M-1.4B）更鲁棒\\\\\\\"\\\\n      - \\\\\\\"推理任务比检索任务更易退化\\\\\\\"\\\\n      - \\\\\\\"iteration 1 + 30% synthetic 时 ECE 从 0.08 升至 0.14（+75%）\\\\\\\"\\\\n    relevance_to_us: \\\\\\\"**最直接的竞争者/先驱**。证实 ECE 可作为 canary，但未做 lead-lag 分析，未建立多指标 panel 框架\\\\\\\"\\\\n    metrics_studied: [\\\\\\\"ECE\\\\\\\", \\\\\\\"accuracy\\\\\\\", \\\\\\\"perplexity\\\\\\\"]\\\\n\\\\n  - id: \\\\\\\"gambetta2024surplexity\\\\\\\"\\\\n    title: \\\\\\\"Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI\\\\\\\"\\\\n    authors: \\\\\\\"Daniele Gambetta et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv (2410.12341)\\\\\\\"\\\\n    year: 2024\\\\n    url: \\\\\\\"https://arxiv.org/abs/2410.12341\\\\\\\"\\\\n    category: \\\\\\\"canary-metrics\\\\\\\"\\\\n    role: \\\\\\\"direct-competitor\\\\\\\"\\\\n    key_findings:\\\\n      - \\\\\\\"提出 surplexity（model surprise 度量）同时用于检测 collapse 和过滤训练数据\\\\\\\"\\\\n      - \\\\\\\"用 semantic networks 分析文本重复性和语义多样性\\\\\\\"\\\\n      - \\\\\\\"用 next-token probability 定量衡量 diversity loss\\\\\\\"\\\\n      - \\\\\\\"高 surplexity 过滤策略至少与 human-data baseline 同效，且更能降低分布偏斜\\\\\\\"\\\\n      - \\\\\\\"不需要区分 human vs AI-generated data\\\\\\\"\\\\n    relevance_to_us: \\\\\\\"surplexity 可作为我们 canary 指标候选之一；其 semantic network 方法提供了 diversity 度量的另一视角\\\\\\\"\\\\n    metrics_studied: [\\\\\\\"surplexity\\\\\\\", \\\\\\\"semantic network metrics\\\\\\\", \\\\\\\"next-token probability\\\\\\\"]\\\\n\\\\n  - id: \\\\\\\"qiu2025spectral\\\\\\\"\\\\n    title: \\\\\\\"Spectral Alignment as Predictor of Loss Explosion in Neural Network Training\\\\\\\"\\\\n    authors: \\\\\\\"Haiquan Qiu, You Wu, Yingjie Tan, Yaqing Wang, Quanming Yao\\\\\\\"\\\\n    venue: \\\\\\\"arXiv (2510.04202)\\\\\\\"\\\\n    year: 2025\\\\n    url: \\\\\\\"https://arxiv.org/abs/2510.04202\\\\\\\"\\\\n    category: \\\\\\\"canary-metrics\\\\\\\"\\\\n    role: \\\\\\\"method-component\\\\\\\"\\\\n    key_findings:\\\\n      - \\\\\\\"Spectral Alignment (SA) 监控层输入与权重矩阵主奇异向量的分布对齐\\\\\\\"\\\\n      - \\\\\\\"SA sign diversity collapse 是 representational collapse 和训练发散的早期预测器\\\\\\\"\\\\n      - \\\\\\\"比 weight norm、gradient norm 等传统指标更早、更清晰地检测到训练失败\\\\\\\"\\\\n      - \\\\\\\"健康层的 SA 应有正负均衡分布，collapse 到单侧则预示不稳定\\\\\\\"\\\\n    relevance_to_us: \\\\\\\"SA 是潜在的高价值 canary 指标——专门设计为 early warning，可直接纳入我们的指标 panel\\\\\\\"\\\\n    metrics_studied: [\\\\\\\"spectral alignment\\\\\\\", \\\\\\\"weight norm\\\\\\\", \\\\\\\"gradient norm\\\\\\\"]\\\\n\\\\n  - id: \\\\\\\"he2025closer\\\\\\\"\\\\n    title: \\\\\\\"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\\\\\\\"\\\\n    authors: \\\\\\\"Shiliang He et al.\\\\\\\"\\\\n    venue: \\\\\\\"NeurIPS 2025 (Spotlight)\\\\\\\"\\\\n    year: 2025\\\\n    url: \\\\\\\"https://arxiv.org/abs/2509.16499\\\\\\\"\\\\n    category: \\\\\\\"canary-metrics\\\\\\\"\\\\n    role: \\\\\\\"direct-competitor\\\\\\\"\\\\n    key_findings:\\\\n      - \\\\\\\"识别 diffusion model collapse 中的 generalization → memorization 转变\\\\\\\"\\\\n      - \\\\\\\"**训练数据的 entropy 递减是 collapse 的直接驱动因素和清晰指标**\\\\\\\"\\\\n      - \\\\\\\"提出基于 entropy 的数据选择策略，有效缓解 collapse\\\\\\\"\\\\n    relevance_to_us: \\\\\\\"data entropy 作为 canary 的有效性已被验证（diffusion domain）；需测试是否在 LLM 场景同样有效\\\\\\\"\\\\n    metrics_studied: [\\\\\\\"entropy\\\\\\\", \\\\\\\"FID\\\\\\\", \\\\\\\"diversity\\\\\\\"]\\\\n\\\\n  - id: \\\\\\\"ba2024fill\\\\\\\"\\\\n    title: \\\\\\\"Fill In The Gaps: Model Calibration and Generalization with Synthetic Data\\\\\\\"\\\\n    authors: \\\\\\\"Yang Ba, Michelle V Mancenido, Rong Pan\\\\\\\"\\\\n    venue: \\\\\\\"EMNLP 2024\\\\\\\"\\\\n    year: 2024\\\\n    url: \\\\\\\"https://arxiv.org/abs/2410.10864\\\\\\\"\\\\n    category: \\\\\\\"canary-metrics\\\\\\\"\\\\n    role: \\\\\\\"background\\\\\\\"\\\\n    key_findings:\\\\n      - \\\\\\\"用 LLM 生成合成数据来修复 calibration 错误的 reliability diagram bins\\\\\\\"\\\\n      - \\\\\\\"推导了基于 PAC 框架的 ECE bound\\\\\\\"\\\\n      - \\\\\\\"合成数据可改善 calibration 但需精心设计生成策略\\\\\\\"\\\\n    relevance_to_us: \\\\\\\"ECE 的理论 bound 可为我们的 canary 阈值设定提供理论依据\\\\\\\"\\\\n    metrics_studied: [\\\\\\\"ECE\\\\\\\", \\\\\\\"accuracy\\\\\\\"]\\\\n\\\\n  # ============================================================\\\\n  # DIVERSITY METRICS (BACKGROUND)\\\\n  # ============================================================\\\\n  - id: \\\\\\\"zhu2018texygen\\\\\\\"\\\\n    title: \\\\\\\"Texygen: A Benchmarking Platform for Text Generation Models\\\\\\\"\\\\n    authors: \\\\\\\"Yaoming Zhu et al.\\\\\\\"\\\\n    venue: \\\\\\\"SIGIR 2018\\\\\\\"\\\\n    year: 2018\\\\n    url: \\\\\\\"https://arxiv.org/abs/1802.01886\\\\\\\"\\\\n    category: \\\\\\\"canary-metrics\\\\\\\"\\\\n    role: \\\\\\\"background\\\\\\\"\\\\n    key_findings:\\\\n      - \\\\\\\"提出 Self-BLEU 度量：计算生成句子间的 BLEU 相似度，Self-BLEU 越高多样性越低\\\\\\\"\\\\n      - \\\\\\\"成为文本生成多样性评估的标准基准之一\\\\\\\"\\\\n    relevance_to_us: \\\\\\\"Self-BLEU 是我们 diversity canary 的经典候选\\\\\\\"\\\\n    metrics_studied: [\\\\\\\"Self-BLEU\\\\\\\", \\\\\\\"BLEU\\\\\\\"]\\\\n\\\\n  - id: \\\\\\\"li2016diversity\\\\\\\"\\\\n    title: \\\\\\\"A Diversity-Promoting Objective Function for Neural Conversation Models\\\\\\\"\\\\n    authors: \\\\\\\"Jiwei Li et al.\\\\\\\"\\\\n    venue: \\\\\\\"NAACL 2016\\\\\\\"\\\\n    year: 2016\\\\n    url: \\\\\\\"https://arxiv.org/abs/1510.03055\\\\\\\"\\\\n    category: \\\\\\\"canary-metrics\\\\\\\"\\\\n    role: \\\\\\\"background\\\\\\\"\\\\n    key_findings:\\\\n      - \\\\\\\"提出 distinct-1 / distinct-2 指标衡量生成文本的 n-gram 多样性\\\\\\\"\\\\n      - \\\\\\\"计算 unique n-gram 数占总 n-gram 数的比例\\\\\\\"\\\\n    relevance_to_us: \\\\\\\"distinct-n 是最廉价的 diversity canary 之一，计算开销极低\\\\\\\"\\\\n    metrics_studied: [\\\\\\\"distinct-1\\\\\\\", \\\\\\\"distinct-2\\\\\\\"]\\\\n\\\\n  # ============================================================\\\\n  # REPRESENTATION / SPECTRAL COLLAPSE\\\\n  # ============================================================\\\\n  - id: \\\\\\\"jing2022understanding\\\\\\\"\\\\n    title: \\\\\\\"Understanding Dimensional Collapse in Contrastive Self-supervised Learning\\\\\\\"\\\\n    authors: \\\\\\\"Li Jing et al.\\\\\\\"\\\\n    venue: \\\\\\\"ICLR 2022\\\\\\\"\\\\n    year: 2022\\\\n    url: \\\\\\\"https://openreview.net/forum?id=YevsQ05DEN7\\\\\\\"\\\\n    category: \\\\\\\"canary-metrics\\\\\\\"\\\\n    role: \\\\\\\"method-component\\\\\\\"\\\\n    key_findings:\\\\n      - \\\\\\\"定义 dimensional collapse：embedding 向量只跨越低维子空间\\\\\\\"\\\\n      - \\\\\\\"effective rank（基于归一化特征值 entropy 的指数）作为 collapse 度量\\\\\\\"\\\\n      - \\\\\\\"strong augmentation 和 implicit regularization 驱动低秩解\\\\\\\"\\\\n    relevance_to_us: \\\\\\\"effective rank 的定义和计算方式可直接迁移到我们的 embedding 空间监控\\\\\\\"\\\\n    metrics_studied: [\\\\\\\"effective rank\\\\\\\", \\\\\\\"singular value spectrum\\\\\\\"]\\\\n\\\\n  - id: \\\\\\\"noci2024mind\\\\\\\"\\\\n    title: \\\\\\\"Mind the Gap: A Spectral Analysis of Rank Collapse and Signal Propagation in Transformers\\\\\\\"\\\\n    authors: \\\\\\\"Lorenzo Noci et al.\\\\\\\"\\\\n    venue: \\\\\\\"NeurIPS 2024\\\\\\\"\\\\n    year: 2024\\\\n    url: \\\\\\\"https://arxiv.org/abs/2410.07799\\\\\\\"\\\\n    category: \\\\\\\"canary-metrics\\\\\\\"\\\\n    role: \\\\\\\"method-component\\\\\\\"\\\\n    key_findings:\\\\n      - \\\\\\\"用 Random Matrix Theory 分析 attention 层的 rank collapse\\\\\\\"\\\\n      - \\\\\\\"发现 attention matrix 最大两个奇异值之间的 spectral gap 是 width-collapse 的根因\\\\\\\"\\\\n      - \\\\\\\"rank collapse in depth: 所有 token 沿层收敛到单一表示\\\\\\\"\\\\n    relevance_to_us: \\\\\\\"spectral gap 作为另一种 spectral canary 候选；其 RMT 分析框架可启发我们的理论工作\\\\\\\"\\\\n    metrics_studied: [\\\\\\\"spectral gap\\\\\\\", \\\\\\\"singular values\\\\\\\", \\\\\\\"effective rank\\\\\\\"]\\\\n\\\\n  # ============================================================\\\\n  # DATA MIXING & ACCUMULATION\\\\n  # ============================================================\\\\n  - id: \\\\\\\"kazdan2025collapse\\\\\\\"\\\\n    title: \\\\\\\"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World\\\\\\\"\\\\n    authors: \\\\\\\"Joshua Kazdan, Rylan Schaeffer, Apratim Dey, Matthias Gerstgrasser, Rafael Rafailov, David L. Donoho, Sanmi Koyejo\\\\\\\"\\\\n    venue: \\\\\\\"ICML 2025\\\\\\\"\\\\n    year: 2025\\\\n    url: \\\\\\\"https://arxiv.org/abs/2410.16713\\\\\\\"\\\\n    category: \\\\\\\"data-mixing\\\\\\\"\\\\n    role: \\\\\\\"foundation\\\\\\\"\\\\n    key_findings:\\\\n      - \\\\\\\"系统对比 replace vs accumulate 场景\\\\\\\"\\\\n      - \\\\\\\"replace → collapse；accumulate → 可避免 collapse\\\\\\\"\\\\n      - \\\\\\\"发现 real data 和 synthetic data 之间存在非平凡的交互效应\\\\\\\"\\\\n      - \\\\\\\"synthetic data 的价值取决于 real data 的绝对数量\\\\\\\"\\\\n    relevance_to_us: \\\\\\\"直接对应我们的 alpha（mixing ratio）实验维度；其 replace vs accumulate 框架是我们实验设计的重要参考\\\\\\\"\\\\n    metrics_studied: [\\\\\\\"test loss\\\\\\\"]\\\\n\\\\n  - id: \\\\\\\"dey2024breaking\\\\\\\"\\\\n    title: \\\\\\\"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\\\\\\\"\\\\n    authors: \\\\\\\"Apratim Dey, David Donoho, et al.\\\\\\\"\\\\n    venue: \\\\\\\"ICML 2024\\\\\\\"\\\\n    year: 2024\\\\n    url: \\\\\\\"https://arxiv.org/abs/2404.01413\\\\\\\"\\\\n    category: \\\\\\\"data-mixing\\\\\\\"\\\\n    role: \\\\\\\"foundation\\\\\\\"\\\\n    key_findings:\\\\n      - \\\\\\\"替换数据 → 发散 population risk；累积数据 → 避免发散\\\\\\\"\\\\n      - \\\\\\\"证明累积策略在多种模型（GMM, HMM, LLM）上有效\\\\\\\"\\\\n    relevance_to_us: \\\\\\\"为我们的 alpha 实验提供理论预测：累积 vs 替换是 collapse 速率的关键调节因子\\\\\\\"\\\\n    metrics_studied: [\\\\\\\"population risk\\\\\\\"]\\\\n\\\\n  - id: \\\\\\\"epstein2024howbad\\\\\\\"\\\\n    title: \\\\\\\"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse\\\\\\\"\\\\n    authors: \\\\\\\"Mohamed El Amine Epstein et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv (2404.05090)\\\\\\\"\\\\n    year: 2024\\\\n    url: \\\\\\\"https://arxiv.org/abs/2404.05090\\\\\\\"\\\\n    category: \\\\\\\"data-mixing\\\\\\\"\\\\n    role: \\\\\\\"background\\\\\\\"\\\\n    key_findings:\\\\n      - \\\\\\\"纯合成数据训练不可避免 collapse\\\\\\\"\\\\n      - \\\\\\\"给出 synthetic data 比例上界的估计——低于此比例可避免 collapse\\\\\\\"\\\\n      - \\\\\\\"递归训练使原始分布尾部消失\\\\\\\"\\\\n    relevance_to_us: \\\\\\\"其 mixing ratio 上界估计可对比我们实验中观测到的 canary 触发阈值\\\\\\\"\\\\n    metrics_studied: [\\\\\\\"perplexity\\\\\\\"]\\\\n\\\\n  - id: \\\\\\\"bakshi2026improvement\\\\\\\"\\\\n    title: \\\\\\\"From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources\\\\\\\"\\\\n    authors: \\\\\\\"Soham Bakshi et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv (2602.10531)\\\\\\\"\\\\n    year: 2026\\\\n    url: \\\\\\\"https://arxiv.org/abs/2602.10531\\\\\\\"\\\\n    category: \\\\\\\"data-mixing\\\\\\\"\\\\n    role: \\\\\\\"background\\\\\\\"\\\\n    key_findings:\\\\n      - \\\\\\\"即使真实数据比例随时间衰减，只要非零就可能避免 collapse 并恢复真实分布\\\\\\\"\\\\n      - \\\\\\\"在 next-token prediction 语言模型上分析混合训练的动态\\\\\\\"\\\\n    relevance_to_us: \\\\\\\"提供了 decaying real data fraction 的理论保证，与我们的实验中 alpha 变化场景相关\\\\\\\"\\\\n    metrics_studied: [\\\\\\\"population risk\\\\\\\"]\\\\n\\\\n  # ============================================================\\\\n  # MITIGATION & VERIFICATION\\\\n  # ============================================================\\\\n  - id: \\\\\\\"feng2025escaping\\\\\\\"\\\\n    title: \\\\\\\"Escaping Model Collapse via Synthetic Data Verification\\\\\\\"\\\\n    authors: \\\\\\\"Yunzhen Feng et al.\\\\\\\"\\\\n    venue: \\\\\\\"NeurIPS 2025\\\\\\\"\\\\n    year: 2025\\\\n    url: \\\\\\\"https://arxiv.org/abs/2510.16657\\\\\\\"\\\\n    category: \\\\\\\"data-mixing\\\\\\\"\\\\n    role: \\\\\\\"background\\\\\\\"\\\\n    key_findings:\\\\n      - \\\\\\\"通过外部 verifier（human 或 better model）注入信息可避免 collapse\\\\\\\"\\\\n      - \\\\\\\"verifier-guided retraining 带来短期改善，但最终收敛到 verifier 的 knowledge center\\\\\\\"\\\\n      - \\\\\\\"除非 verifier 完全可靠，早期收益会 plateau 甚至逆转\\\\\\\"\\\\n    relevance_to_us: \\\\\\\"verification 作为 intervention 策略——如果 canary 触发，可考虑此类 reactive intervention\\\\\\\"\\\\n    metrics_studied: [\\\\\\\"test loss\\\\\\\"]\\\\n\\\\n  - id: \\\\\\\"barzilai2025consistency\\\\\\\"\\\\n    title: \\\\\\\"When Models Don't Collapse: On the Consistency of Iterative MLE\\\\\\\"\\\\n    authors: \\\\\\\"Daniel Barzilai, Ohad Shamir\\\\\\\"\\\\n    venue: \\\\\\\"ICML 2025\\\\\\\"\\\\n    year: 2025\\\\n    url: \\\\\\\"https://arxiv.org/abs/2505.19046\\\\\\\"\\\\n    category: \\\\\\\"core-collapse\\\\\\\"\\\\n    role: \\\\\\\"background\\\\\\\"\\\\n    key_findings:\\\\n      - \\\\\\\"在标准 MLE 一致性假设下，即使 real data fraction 趋近零也可避免 collapse\\\\\\\"\\\\n      - \\\\\\\"但证明了某些情况下 collapse 可以任意快地发生——首次给出严格 collapse 反例\\\\\\\"\\\\n    relevance_to_us: \\\\\\\"理论上的 collapse 可发生任意快的结论强化了 early warning 的价值\\\\\\\"\\\\n    metrics_studied: []\\\\n\\\\n  - id: \\\\\\\"dces2026counter\\\\\\\"\\\\n    title: \\\\\\\"Countering Model Collapse in Iterative Self-Training via Dynamic Center-Edge Sampling\\\\\\\"\\\\n    authors: \\\\\\\"Anonymous\\\\\\\"\\\\n    venue: \\\\\\\"MDPI Electronics (2026)\\\\\\\"\\\\n    year: 2026\\\\n    url: \\\\\\\"https://www.mdpi.com/2079-9292/15/4/869\\\\\\\"\\\\n    category: \\\\\\\"data-mixing\\\\\\\"\\\\n    role: \\\\\\\"background\\\\\\\"\\\\n    key_findings:\\\\n      - \\\\\\\"提出 DCES（dynamic center-edge sampling）数据选择框架\\\\\\\"\\\\n      - \\\\\\\"DCES 在 ECE（0.1058 vs 0.1200）和 entropy 保持上优于随机选择\\\\\\\"\\\\n    relevance_to_us: \\\\\\\"其 ECE 和 entropy 对比数据为我们的指标 baseline 提供参考\\\\\\\"\\\\n    metrics_studied: [\\\\\\\"ECE\\\\\\\", \\\\\\\"entropy\\\\\\\"]\\\\n\\\\n  # ============================================================\\\\n  # POSITION / SURVEY / EPISTEMICS\\\\n  # ============================================================\\\\n  - id: \\\\\\\"schaeffer2025position\\\\\\\"\\\\n    title: \\\\\\\"Position: Model Collapse Does Not Mean What You Think\\\\\\\"\\\\n    authors: \\\\\\\"Rylan Schaeffer, Joshua Kazdan, Alvan Caleb Arulandu, Sanmi Koyejo\\\\\\\"\\\\n    venue: \\\\\\\"arXiv (2503.03150)\\\\\\\"\\\\n    year: 2025\\\\n    url: \\\\\\\"https://arxiv.org/abs/2503.03150\\\\\\\"\\\\n    category: \\\\\\\"core-collapse\\\\\\\"\\\\n    role: \\\\\\\"background\\\\\\\"\\\\n    key_findings:\\\\n      - \\\\\\\"文献中实际包含 8 种不同且有时矛盾的 model collapse 定义\\\\\\\"\\\\n      - \\\\\\\"许多 collapse 预测依赖于与现实不符的假设\\\\\\\"\\\\n      - \\\\\\\"多种 collapse 场景是可以轻易避免的\\\\\\\"\\\\n    relevance_to_us: \\\\\\\"提醒我们明确定义 collapse 的操作标准；不同定义可能需要不同的 canary 指标\\\\\\\"\\\\n    metrics_studied: []\\\\n\\\\n  - id: \\\\\\\"wang2025epistemic\\\\\\\"\\\\n    title: \\\\\\\"Epistemic Diversity and Knowledge Collapse in Large Language Models\\\\\\\"\\\\n    authors: \\\\\\\"Wang et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv (2510.04226)\\\\\\\"\\\\n    year: 2025\\\\n    url: \\\\\\\"https://arxiv.org/abs/2510.04226\\\\\\\"\\\\n    category: \\\\\\\"core-collapse\\\\\\\"\\\\n    role: \\\\\\\"background\\\\\\\"\\\\n    key_findings:\\\\n      - \\\\\\\"27 个 LLM 在 155 个主题上的 epistemic diversity 评估\\\\\\\"\\\\n      - \\\\\\\"所有模型的 epistemic diversity 低于基本 web 搜索\\\\\\\"\\\\n      - \\\\\\\"模型越大 epistemic diversity 反而越低；RAG 有正面效果\\\\\\\"\\\\n    relevance_to_us: \\\\\\\"knowledge collapse 维度可扩展我们对 diversity canary 的理解——不仅是 lexical/syntactic 还有 epistemic\\\\\\\"\\\\n    metrics_studied: [\\\\\\\"epistemic diversity\\\\\\\"]\\\\n\\\\n  # ============================================================\\\\n  # METHODOLOGY (GRANGER / LEAD-LAG)\\\\n  # ============================================================\\\\n  - id: \\\\\\\"shojaie2022granger\\\\\\\"\\\\n    title: \\\\\\\"Granger Causality: A Review and Recent Advances\\\\\\\"\\\\n    authors: \\\\\\\"Ali Shojaie, Emily B. Fox\\\\\\\"\\\\n    venue: \\\\\\\"Annual Review of Statistics and Its Application\\\\\\\"\\\\n    year: 2022\\\\n    url: \\\\\\\"https://arxiv.org/abs/2105.02675\\\\\\\"\\\\n    category: \\\\\\\"methodology\\\\\\\"\\\\n    role: \\\\\\\"method-component\\\\\\\"\\\\n    key_findings:\\\\n      - \\\\\\\"Granger causality 综述：从经典线性到非线性/neural 方法\\\\\\\"\\\\n      - \\\\\\\"Panel data 场景的 Granger causality 扩展\\\\\\\"\\\\n      - \\\\\\\"VAR 和 neural Granger causality 的对比\\\\\\\"\\\\n    relevance_to_us: \\\\\\\"为我们的 panel Granger causality 分析提供方法论基础\\\\\\\"\\\\n    metrics_studied: []\\\\n\\\\n  - id: \\\\\\\"marcinkevics2022neural\\\\\\\"\\\\n    title: \\\\\\\"Granger Causality Using Neural Networks\\\\\\\"\\\\n    authors: \\\\\\\"Raphael Marcinkevics, Julia Vogt\\\\\\\"\\\\n    venue: \\\\\\\"arXiv (2208.03703)\\\\\\\"\\\\n    year: 2022\\\\n    url: \\\\\\\"https://arxiv.org/abs/2208.03703\\\\\\\"\\\\n    category: \\\\\\\"methodology\\\\\\\"\\\\n    role: \\\\\\\"method-component\\\\\\\"\\\\n    key_findings:\\\\n      - \\\\\\\"用 neural network 估计 Granger causality，突破线性假设\\\\\\\"\\\\n      - \\\\\\\"两个模型对比法：含/不含外生变量的预测误差差异即 Granger causality 证据\\\\\\\"\\\\n    relevance_to_us: \\\\\\\"我们的多指标时序可能存在非线性关系，neural Granger causality 是自然选择\\\\\\\"\\\\n    metrics_studied: []\\\\n\\\\ngaps:\\\\n  - \\\\\\\"无人系统做过 canary 指标的 lead-lag / Granger causality 分析——现有工作只在事后观察到指标变化，未量化哪些指标能提前多少步预测 collapse\\\\\\\"\\\\n  - \\\\\\\"ECE 在 collapse 场景下几乎未被系统研究——chen2025scales 是唯一报告 ECE 先于 accuracy 退化的工作，但未做因果分析\\\\\\\"\\\\n  - \\\\\\\"embedding effective rank 未在 iterative synthetic training 场景下被测试——仅在 contrastive learning/transformer 训练中研究过\\\\\\\"\\\\n  - \\\\\\\"多指标 panel 框架缺失——无人同时追踪 ECE + effective rank + diversity + perplexity 的时序行为并分析其 lead-lag 关系\\\\\\\"\\\\n  - \\\\\\\"alpha（synthetic ratio）对 canary 灵敏度的影响未被研究——现有工作只关注 alpha 对最终性能的影响，不关注 canary 的 lead time 如何随 alpha 变化\\\\\\\"\\\\n  - \\\\\\\"predictive intervention vs reactive intervention 缺少对比——没有工作量化 early warning 带来的实际干预收益\\\\\\\"\\\\n  - \\\\\\\"surplexity 和 spectral alignment 未在 iterative collapse 场景下交叉验证\\\\\\\"\\\\n  - \\\\\\\"跨任务 canary 普适性未知——reasoning vs retrieval vs creative tasks 中哪些 canary 更可靠\\\\\\\"\\\\n\\\\nnovelty_assessment: |\\\\n  我们项目的核心 novelty 在于：\\\\n\\\\n  1. **Panel Granger Causality 框架**：首次将多指标时序数据的因果分析方法应用于 model collapse 早期预警。\\\\n     现有工作（chen2025scales, gambetta2024surplexity）只是事后观察到某些指标先变化，\\\\n     但没有人做过系统的 lead-lag 量化分析。\\\\n\\\\n  2. **多指标 Canary Panel**：同时追踪 ECE、effective rank、Self-BLEU/distinct-n、\\\\n     perplexity、entropy、surplexity 等指标，分析其相互关系和各自的 lead time。\\\\n     现有工作都是单一指标或最多两三个指标的孤立分析。\\\\n\\\\n  3. **alpha-dependent Canary Sensitivity**：系统研究 synthetic ratio 如何影响各 canary\\\\n     指标的灵敏度和 lead time。dohmatob2025strong 证明极小的 alpha 就能触发 collapse，\\\\n     但没人研究 canary 在不同 alpha 下的行为。\\\\n\\\\n  4. **与已有工作的差异**：\\\\n     - vs chen2025scales: 他们发现 ECE 先退化但没有做因果分析；我们用 Granger causality 量化\\\\n     - vs gambetta2024surplexity: 他们提出 surplexity 用于检测和缓解 collapse；\\\\n       我们将其纳入更广的 panel 并研究其 lead-lag 特性\\\\n     - vs he2025closer: 他们在 diffusion 中用 entropy 作为指标；我们在 LLM 中测试更多指标\\\\n     - vs qiu2025spectral: 他们的 SA 用于训练 loss explosion 预警；\\\\n       我们将类似思路迁移到 iterative collapse 场景\\\\n\\\\n  5. **潜在风险**：chen2025scales 已经非常接近我们的方向。如果他们扩展到 lead-lag 分析，\\\\n     我们的 novelty 会被削弱。需要快速推进并在方法论（Granger causality）上建立壁垒。\\\\n\\\", \\\"total_chars\\\": 19466, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/literature_map.yaml\", \"content\": \"papers:\\n  # ============================================================\\n  # CORE MODEL COLLAPSE\\n  # ============================================================\\n  - id: \\\"shumailov2024curse\\\"\\n    title: \\\"The Curse of Recursion: Training on Generated Data Makes Models Forget\\\"\\n    authors: \\\"Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Yarin Gal, Nicolas Papernot, Ross Anderson\\\"\\n    venue: \\\"Nature\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2305.17493\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"foundation\\\"\\n    key_findings:\\n      - \\\"定义 model collapse 现象：迭代用合成数据替换真实数据训练会导致分布尾部消失\\\"\\n      - \\\"区分 early model collapse（尾部信息丢失）和 late model collapse（分布完全收敛）\\\"\\n      - \\\"三类误差来源：statistical approximation, functional expressivity, functional approximation，跨代复合\\\"\\n      - \\\"在 VAE、GMM、LLM 上均验证了 collapse 的普遍性\\\"\\n    relevance_to_us: \\\"奠基论文，定义了我们研究的核心现象。我们的 canary 指标旨在提前检测其描述的 early collapse 阶段\\\"\\n    metrics_studied: [\\\"perplexity\\\", \\\"distributional tail mass\\\"]\\n\\n  - id: \\\"alemohammad2024mad\\\"\\n    title: \\\"Self-Consuming Generative Models Go MAD\\\"\\n    authors: \\\"Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, Richard Baraniuk\\\"\\n    venue: \\\"ICLR 2024\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2307.01850\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"foundation\\\"\\n    key_findings:\\n      - \\\"提出 Model Autophagy Disorder (MAD) 概念\\\"\\n      - \\\"autophagous loop 中没有足够新鲜真实数据时，质量或多样性必然渐进下降\\\"\\n      - \\\"在图像生成领域验证 self-consuming loop 的退化效应\\\"\\n    relevance_to_us: \\\"MAD 框架与我们的 iterative loop 设置直接对应；其 quality vs diversity tradeoff 可能反映在不同 canary 指标上\\\"\\n    metrics_studied: [\\\"FID\\\", \\\"precision\\\", \\\"recall\\\", \\\"diversity\\\"]\\n\\n  - id: \\\"dohmatob2024tale\\\"\\n    title: \\\"A Tale of Tails: Model Collapse as a Change of Scaling Laws\\\"\\n    authors: \\\"Elvis Dohmatob, Yunzhen Feng, et al.\\\"\\n    venue: \\\"ICML 2024\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2402.07043\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"foundation\\\"\\n    key_findings:\\n      - \\\"通过 scaling laws 视角分析 model collapse：collapse 表现为 scaling law 的变化\\\"\\n      - \\\"发现 loss of scaling, shifted scaling, skill un-learning, grokking 等多种退化模式\\\"\\n      - \\\"混入少量干净数据可缓解 collapse 并引发 grokking 现象\\\"\\n      - \\\"在 transformer 算术任务和 Llama2 文本生成上验证\\\"\\n    relevance_to_us: \\\"scaling law 变化视角为我们提供了理论基础；grokking 现象暗示 canary 指标可能出现非单调行为\\\"\\n    metrics_studied: [\\\"test loss\\\", \\\"scaling exponents\\\"]\\n\\n  - id: \\\"dohmatob2025strong\\\"\\n    title: \\\"Strong Model Collapse\\\"\\n    authors: \\\"Elvis Dohmatob, Yunzhen Feng, Arjun Subramonian, Julia Kempe\\\"\\n    venue: \\\"ICLR 2025 (Spotlight)\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2410.04840\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"foundation\\\"\\n    key_findings:\\n      - \\\"即使合成数据占比极小（1/1000），仍可导致 model collapse\\\"\\n      - \\\"更大的训练集并不能避免 collapse\\\"\\n      - \\\"更大的模型（random projection 近似下）反而可能放大 collapse\\\"\\n      - \\\"存在 interpolation threshold 的 double-descent 现象\\\"\\n    relevance_to_us: \\\"强化了早期检测的必要性——即使极小的合成数据比例也能触发 collapse，因此 canary 指标必须敏感\\\"\\n    metrics_studied: [\\\"test loss\\\", \\\"population risk\\\"]\\n\\n  - id: \\\"guo2024linguistic\\\"\\n    title: \\\"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\\\"\\n    authors: \\\"Yanzhu Guo, Guokan Shang, et al.\\\"\\n    venue: \\\"NAACL 2024 Findings\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2311.09807\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"evaluation\\\"\\n    key_findings:\\n      - \\\"递归微调中，linguistic diversity 在连续迭代中持续下降\\\"\\n      - \\\"创造性任务中 diversity 下降最显著\\\"\\n      - \\\"开发了覆盖 lexical、syntactic、semantic 三层的 diversity 指标体系\\\"\\n    relevance_to_us: \\\"其多层 diversity 指标体系可直接作为我们 canary 指标的候选集；创造性 vs 事实任务的差异可能影响 canary 灵敏度\\\"\\n    metrics_studied: [\\\"distinct-n\\\", \\\"type-token ratio\\\", \\\"syntactic diversity\\\", \\\"semantic diversity\\\"]\\n\\n  - id: \\\"briesch2024selfconsuming\\\"\\n    title: \\\"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop\\\"\\n    authors: \\\"Martin Briesch, Dominik Sobania, Franz Rothlauf\\\"\\n    venue: \\\"arXiv (2311.16822)\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2311.16822\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"direct-competitor\\\"\\n    key_findings:\\n      - \\\"首次系统研究 LLM 的 self-consuming training loop\\\"\\n      - \\\"full synthetic cycle（完全替换）导致单点 collapse；data augmentation cycle 导致 diversity 缓慢下降\\\"\\n      - \\\"expanding data cycle（累积）在 50 代内保持 diversity\\\"\\n    relevance_to_us: \\\"其不同 data cycle 策略的对比直接对应我们的 alpha（synthetic ratio）实验设置\\\"\\n    metrics_studied: [\\\"diversity\\\", \\\"quality\\\"]\\n\\n  # ============================================================\\n  # CANARY / EARLY WARNING METRICS\\n  # ============================================================\\n  - id: \\\"chen2025scales\\\"\\n    title: \\\"Characterizing Model Behavior Under Synthetic Data Training: An Empirical Study Across Scales and Mixing Ratios\\\"\\n    authors: \\\"Anonymous\\\"\\n    venue: \\\"arXiv (2510.05133)\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2510.05133\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"direct-competitor\\\"\\n    key_findings:\\n      - \\\"**Calibration degradation precedes accuracy loss** — ECE 是 collapse 的 early warning signal\\\"\\n      - \\\"20% synthetic data 以下性能稳定，30% 以上退化加速\\\"\\n      - \\\"大模型（6.9B-12B）比小模型（410M-1.4B）更鲁棒\\\"\\n      - \\\"推理任务比检索任务更易退化\\\"\\n      - \\\"iteration 1 + 30% synthetic 时 ECE 从 0.08 升至 0.14（+75%）\\\"\\n    relevance_to_us: \\\"**最直接的竞争者/先驱**。证实 ECE 可作为 canary，但未做 lead-lag 分析，未建立多指标 panel 框架\\\"\\n    metrics_studied: [\\\"ECE\\\", \\\"accuracy\\\", \\\"perplexity\\\"]\\n\\n  - id: \\\"gambetta2024surplexity\\\"\\n    title: \\\"Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI\\\"\\n    authors: \\\"Daniele Gambetta et al.\\\"\\n    venue: \\\"arXiv (2410.12341)\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2410.12341\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"direct-competitor\\\"\\n    key_findings:\\n      - \\\"提出 surplexity（model surprise 度量）同时用于检测 collapse 和过滤训练数据\\\"\\n      - \\\"用 semantic networks 分析文本重复性和语义多样性\\\"\\n      - \\\"用 next-token probability 定量衡量 diversity loss\\\"\\n      - \\\"高 surplexity 过滤策略至少与 human-data baseline 同效，且更能降低分布偏斜\\\"\\n      - \\\"不需要区分 human vs AI-generated data\\\"\\n    relevance_to_us: \\\"surplexity 可作为我们 canary 指标候选之一；其 semantic network 方法提供了 diversity 度量的另一视角\\\"\\n    metrics_studied: [\\\"surplexity\\\", \\\"semantic network metrics\\\", \\\"next-token probability\\\"]\\n\\n  - id: \\\"qiu2025spectral\\\"\\n    title: \\\"Spectral Alignment as Predictor of Loss Explosion in Neural Network Training\\\"\\n    authors: \\\"Haiquan Qiu, You Wu, Yingjie Tan, Yaqing Wang, Quanming Yao\\\"\\n    venue: \\\"arXiv (2510.04202)\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2510.04202\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"method-component\\\"\\n    key_findings:\\n      - \\\"Spectral Alignment (SA) 监控层输入与权重矩阵主奇异向量的分布对齐\\\"\\n      - \\\"SA sign diversity collapse 是 representational collapse 和训练发散的早期预测器\\\"\\n      - \\\"比 weight norm、gradient norm 等传统指标更早、更清晰地检测到训练失败\\\"\\n      - \\\"健康层的 SA 应有正负均衡分布，collapse 到单侧则预示不稳定\\\"\\n    relevance_to_us: \\\"SA 是潜在的高价值 canary 指标——专门设计为 early warning，可直接纳入我们的指标 panel\\\"\\n    metrics_studied: [\\\"spectral alignment\\\", \\\"weight norm\\\", \\\"gradient norm\\\"]\\n\\n  - id: \\\"he2025closer\\\"\\n    title: \\\"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\\\"\\n    authors: \\\"Shiliang He et al.\\\"\\n    venue: \\\"NeurIPS 2025 (Spotlight)\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2509.16499\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"direct-competitor\\\"\\n    key_findings:\\n      - \\\"识别 diffusion model collapse 中的 generalization → memorization 转变\\\"\\n      - \\\"**训练数据的 entropy 递减是 collapse 的直接驱动因素和清晰指标**\\\"\\n      - \\\"提出基于 entropy 的数据选择策略，有效缓解 collapse\\\"\\n    relevance_to_us: \\\"data entropy 作为 canary 的有效性已被验证（diffusion domain）；需测试是否在 LLM 场景同样有效\\\"\\n    metrics_studied: [\\\"entropy\\\", \\\"FID\\\", \\\"diversity\\\"]\\n\\n  - id: \\\"ba2024fill\\\"\\n    title: \\\"Fill In The Gaps: Model Calibration and Generalization with Synthetic Data\\\"\\n    authors: \\\"Yang Ba, Michelle V Mancenido, Rong Pan\\\"\\n    venue: \\\"EMNLP 2024\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2410.10864\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"background\\\"\\n    key_findings:\\n      - \\\"用 LLM 生成合成数据来修复 calibration 错误的 reliability diagram bins\\\"\\n      - \\\"推导了基于 PAC 框架的 ECE bound\\\"\\n      - \\\"合成数据可改善 calibration 但需精心设计生成策略\\\"\\n    relevance_to_us: \\\"ECE 的理论 bound 可为我们的 canary 阈值设定提供理论依据\\\"\\n    metrics_studied: [\\\"ECE\\\", \\\"accuracy\\\"]\\n\\n  # ============================================================\\n  # DIVERSITY METRICS (BACKGROUND)\\n  # ============================================================\\n  - id: \\\"zhu2018texygen\\\"\\n    title: \\\"Texygen: A Benchmarking Platform for Text Generation Models\\\"\\n    authors: \\\"Yaoming Zhu et al.\\\"\\n    venue: \\\"SIGIR 2018\\\"\\n    year: 2018\\n    url: \\\"https://arxiv.org/abs/1802.01886\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"background\\\"\\n    key_findings:\\n      - \\\"提出 Self-BLEU 度量：计算生成句子间的 BLEU 相似度，Self-BLEU 越高多样性越低\\\"\\n      - \\\"成为文本生成多样性评估的标准基准之一\\\"\\n    relevance_to_us: \\\"Self-BLEU 是我们 diversity canary 的经典候选\\\"\\n    metrics_studied: [\\\"Self-BLEU\\\", \\\"BLEU\\\"]\\n\\n  - id: \\\"li2016diversity\\\"\\n    title: \\\"A Diversity-Promoting Objective Function for Neural Conversation Models\\\"\\n    authors: \\\"Jiwei Li et al.\\\"\\n    venue: \\\"NAACL 2016\\\"\\n    year: 2016\\n    url: \\\"https://arxiv.org/abs/1510.03055\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"background\\\"\\n    key_findings:\\n      - \\\"提出 distinct-1 / distinct-2 指标衡量生成文本的 n-gram 多样性\\\"\\n      - \\\"计算 unique n-gram 数占总 n-gram 数的比例\\\"\\n    relevance_to_us: \\\"distinct-n 是最廉价的 diversity canary 之一，计算开销极低\\\"\\n    metrics_studied: [\\\"distinct-1\\\", \\\"distinct-2\\\"]\\n\\n  # ============================================================\\n  # REPRESENTATION / SPECTRAL COLLAPSE\\n  # ============================================================\\n  - id: \\\"jing2022understanding\\\"\\n    title: \\\"Understanding Dimensional Collapse in Contrastive Self-supervised Learning\\\"\\n    authors: \\\"Li Jing et al.\\\"\\n    venue: \\\"ICLR 2022\\\"\\n    year: 2022\\n    url: \\\"https://openreview.net/forum?id=YevsQ05DEN7\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"method-component\\\"\\n    key_findings:\\n      - \\\"定义 dimensional collapse：embedding 向量只跨越低维子空间\\\"\\n      - \\\"effective rank（基于归一化特征值 entropy 的指数）作为 collapse 度量\\\"\\n      - \\\"strong augmentation 和 implicit regularization 驱动低秩解\\\"\\n    relevance_to_us: \\\"effective rank 的定义和计算方式可直接迁移到我们的 embedding 空间监控\\\"\\n    metrics_studied: [\\\"effective rank\\\", \\\"singular value spectrum\\\"]\\n\\n  - id: \\\"noci2024mind\\\"\\n    title: \\\"Mind the Gap: A Spectral Analysis of Rank Collapse and Signal Propagation in Transformers\\\"\\n    authors: \\\"Lorenzo Noci et al.\\\"\\n    venue: \\\"NeurIPS 2024\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2410.07799\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"method-component\\\"\\n    key_findings:\\n      - \\\"用 Random Matrix Theory 分析 attention 层的 rank collapse\\\"\\n      - \\\"发现 attention matrix 最大两个奇异值之间的 spectral gap 是 width-collapse 的根因\\\"\\n      - \\\"rank collapse in depth: 所有 token 沿层收敛到单一表示\\\"\\n    relevance_to_us: \\\"spectral gap 作为另一种 spectral canary 候选；其 RMT 分析框架可启发我们的理论工作\\\"\\n    metrics_studied: [\\\"spectral gap\\\", \\\"singular values\\\", \\\"effective rank\\\"]\\n\\n  # ============================================================\\n  # DATA MIXING & ACCUMULATION\\n  # ============================================================\\n  - id: \\\"kazdan2025collapse\\\"\\n    title: \\\"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World\\\"\\n    authors: \\\"Joshua Kazdan, Rylan Schaeffer, Apratim Dey, Matthias Gerstgrasser, Rafael Rafailov, David L. Donoho, Sanmi Koyejo\\\"\\n    venue: \\\"ICML 2025\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2410.16713\\\"\\n    category: \\\"data-mixing\\\"\\n    role: \\\"foundation\\\"\\n    key_findings:\\n      - \\\"系统对比 replace vs accumulate 场景\\\"\\n      - \\\"replace → collapse；accumulate → 可避免 collapse\\\"\\n      - \\\"发现 real data 和 synthetic data 之间存在非平凡的交互效应\\\"\\n      - \\\"synthetic data 的价值取决于 real data 的绝对数量\\\"\\n    relevance_to_us: \\\"直接对应我们的 alpha（mixing ratio）实验维度；其 replace vs accumulate 框架是我们实验设计的重要参考\\\"\\n    metrics_studied: [\\\"test loss\\\"]\\n\\n  - id: \\\"dey2024breaking\\\"\\n    title: \\\"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\\\"\\n    authors: \\\"Apratim Dey, David Donoho, et al.\\\"\\n    venue: \\\"ICML 2024\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2404.01413\\\"\\n    category: \\\"data-mixing\\\"\\n    role: \\\"foundation\\\"\\n    key_findings:\\n      - \\\"替换数据 → 发散 population risk；累积数据 → 避免发散\\\"\\n      - \\\"证明累积策略在多种模型（GMM, HMM, LLM）上有效\\\"\\n    relevance_to_us: \\\"为我们的 alpha 实验提供理论预测：累积 vs 替换是 collapse 速率的关键调节因子\\\"\\n    metrics_studied: [\\\"population risk\\\"]\\n\\n  - id: \\\"epstein2024howbad\\\"\\n    title: \\\"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse\\\"\\n    authors: \\\"Mohamed El Amine Epstein et al.\\\"\\n    venue: \\\"arXiv (2404.05090)\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2404.05090\\\"\\n    category: \\\"data-mixing\\\"\\n    role: \\\"background\\\"\\n    key_findings:\\n      - \\\"纯合成数据训练不可避免 collapse\\\"\\n      - \\\"给出 synthetic data 比例上界的估计——低于此比例可避免 collapse\\\"\\n      - \\\"递归训练使原始分布尾部消失\\\"\\n    relevance_to_us: \\\"其 mixing ratio 上界估计可对比我们实验中观测到的 canary 触发阈值\\\"\\n    metrics_studied: [\\\"perplexity\\\"]\\n\\n  - id: \\\"bakshi2026improvement\\\"\\n    title: \\\"From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources\\\"\\n    authors: \\\"Soham Bakshi et al.\\\"\\n    venue: \\\"arXiv (2602.10531)\\\"\\n    year: 2026\\n    url: \\\"https://arxiv.org/abs/2602.10531\\\"\\n    category: \\\"data-mixing\\\"\\n    role: \\\"background\\\"\\n    key_findings:\\n      - \\\"即使真实数据比例随时间衰减，只要非零就可能避免 collapse 并恢复真实分布\\\"\\n      - \\\"在 next-token prediction 语言模型上分析混合训练的动态\\\"\\n    relevance_to_us: \\\"提供了 decaying real data fraction 的理论保证，与我们的实验中 alpha 变化场景相关\\\"\\n    metrics_studied: [\\\"population risk\\\"]\\n\\n  # ============================================================\\n  # MITIGATION & VERIFICATION\\n  # ============================================================\\n  - id: \\\"feng2025escaping\\\"\\n    title: \\\"Escaping Model Collapse via Synthetic Data Verification\\\"\\n    authors: \\\"Yunzhen Feng et al.\\\"\\n    venue: \\\"NeurIPS 2025\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2510.16657\\\"\\n    category: \\\"data-mixing\\\"\\n    role: \\\"background\\\"\\n    key_findings:\\n      - \\\"通过外部 verifier（human 或 better model）注入信息可避免 collapse\\\"\\n      - \\\"verifier-guided retraining 带来短期改善，但最终收敛到 verifier 的 knowledge center\\\"\\n      - \\\"除非 verifier 完全可靠，早期收益会 plateau 甚至逆转\\\"\\n    relevance_to_us: \\\"verification 作为 intervention 策略——如果 canary 触发，可考虑此类 reactive intervention\\\"\\n    metrics_studied: [\\\"test loss\\\"]\\n\\n  - id: \\\"barzilai2025consistency\\\"\\n    title: \\\"When Models Don't Collapse: On the Consistency of Iterative MLE\\\"\\n    authors: \\\"Daniel Barzilai, Ohad Shamir\\\"\\n    venue: \\\"ICML 2025\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2505.19046\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"background\\\"\\n    key_findings:\\n      - \\\"在标准 MLE 一致性假设下，即使 real data fraction 趋近零也可避免 collapse\\\"\\n      - \\\"但证明了某些情况下 collapse 可以任意快地发生——首次给出严格 collapse 反例\\\"\\n    relevance_to_us: \\\"理论上的 collapse 可发生任意快的结论强化了 early warning 的价值\\\"\\n    metrics_studied: []\\n\\n  - id: \\\"dces2026counter\\\"\\n    title: \\\"Countering Model Collapse in Iterative Self-Training via Dynamic Center-Edge Sampling\\\"\\n    authors: \\\"Anonymous\\\"\\n    venue: \\\"MDPI Electronics (2026)\\\"\\n    year: 2026\\n    url: \\\"https://www.mdpi.com/2079-9292/15/4/869\\\"\\n    category: \\\"data-mixing\\\"\\n    role: \\\"background\\\"\\n    key_findings:\\n      - \\\"提出 DCES（dynamic center-edge sampling）数据选择框架\\\"\\n      - \\\"DCES 在 ECE（0.1058 vs 0.1200）和 entropy 保持上优于随机选择\\\"\\n    relevance_to_us: \\\"其 ECE 和 entropy 对比数据为我们的指标 baseline 提供参考\\\"\\n    metrics_studied: [\\\"ECE\\\", \\\"entropy\\\"]\\n\\n  # ============================================================\\n  # POSITION / SURVEY / EPISTEMICS\\n  # ============================================================\\n  - id: \\\"schaeffer2025position\\\"\\n    title: \\\"Position: Model Collapse Does Not Mean What You Think\\\"\\n    authors: \\\"Rylan Schaeffer, Joshua Kazdan, Alvan Caleb Arulandu, Sanmi Koyejo\\\"\\n    venue: \\\"arXiv (2503.03150)\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2503.03150\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"background\\\"\\n    key_findings:\\n      - \\\"文献中实际包含 8 种不同且有时矛盾的 model collapse 定义\\\"\\n      - \\\"许多 collapse 预测依赖于与现实不符的假设\\\"\\n      - \\\"多种 collapse 场景是可以轻易避免的\\\"\\n    relevance_to_us: \\\"提醒我们明确定义 collapse 的操作标准；不同定义可能需要不同的 canary 指标\\\"\\n    metrics_studied: []\\n\\n  - id: \\\"wang2025epistemic\\\"\\n    title: \\\"Epistemic Diversity and Knowledge Collapse in Large Language Models\\\"\\n    authors: \\\"Wang et al.\\\"\\n    venue: \\\"arXiv (2510.04226)\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2510.04226\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"background\\\"\\n    key_findings:\\n      - \\\"27 个 LLM 在 155 个主题上的 epistemic diversity 评估\\\"\\n      - \\\"所有模型的 epistemic diversity 低于基本 web 搜索\\\"\\n      - \\\"模型越大 epistemic diversity 反而越低；RAG 有正面效果\\\"\\n    relevance_to_us: \\\"knowledge collapse 维度可扩展我们对 diversity canary 的理解——不仅是 lexical/syntactic 还有 epistemic\\\"\\n    metrics_studied: [\\\"epistemic diversity\\\"]\\n\\n  # ============================================================\\n  # METHODOLOGY (GRANGER / LEAD-LAG)\\n  # ============================================================\\n  - id: \\\"shojaie2022granger\\\"\\n    title: \\\"Granger Causality: A Review and Recent Advances\\\"\\n    authors: \\\"Ali Shojaie, Emily B. Fox\\\"\\n    venue: \\\"Annual Review of Statistics and Its Application\\\"\\n    year: 2022\\n    url: \\\"https://arxiv.org/abs/2105.02675\\\"\\n    category: \\\"methodology\\\"\\n    role: \\\"method-component\\\"\\n    key_findings:\\n      - \\\"Granger causality 综述：从经典线性到非线性/neural 方法\\\"\\n      - \\\"Panel data 场景的 Granger causality 扩展\\\"\\n      - \\\"VAR 和 neural Granger causality 的对比\\\"\\n    relevance_to_us: \\\"为我们的 panel Granger causality 分析提供方法论基础\\\"\\n    metrics_studied: []\\n\\n  - id: \\\"marcinkevics2022neural\\\"\\n    title: \\\"Granger Causality Using Neural Networks\\\"\\n    authors: \\\"Raphael Marcinkevics, Julia Vogt\\\"\\n    venue: \\\"arXiv (2208.03703)\\\"\\n    year: 2022\\n    url: \\\"https://arxiv.org/abs/2208.03703\\\"\\n    category: \\\"methodology\\\"\\n    role: \\\"method-component\\\"\\n    key_findings:\\n      - \\\"用 neural network 估计 Granger causality，突破线性假设\\\"\\n      - \\\"两个模型对比法：含/不含外生变量的预测误差差异即 Granger causality 证据\\\"\\n    relevance_to_us: \\\"我们的多指标时序可能存在非线性关系，neural Granger causality 是自然选择\\\"\\n    metrics_studied: []\\n\\ngaps:\\n  - \\\"无人系统做过 canary 指标的 lead-lag / Granger causality 分析——现有工作只在事后观察到指标变化，未量化哪些指标能提前多少步预测 collapse\\\"\\n  - \\\"ECE 在 collapse 场景下几乎未被系统研究——chen2025scales 是唯一报告 ECE 先于 accuracy 退化的工作，但未做因果分析\\\"\\n  - \\\"embedding effective rank 未在 iterative synthetic training 场景下被测试——仅在 contrastive learning/transformer 训练中研究过\\\"\\n  - \\\"多指标 panel 框架缺失——无人同时追踪 ECE + effective rank + diversity + perplexity 的时序行为并分析其 lead-lag 关系\\\"\\n  - \\\"alpha（synthetic ratio）对 canary 灵敏度的影响未被研究——现有工作只关注 alpha 对最终性能的影响，不关注 canary 的 lead time 如何随 alpha 变化\\\"\\n  - \\\"predictive intervention vs reactive intervention 缺少对比——没有工作量化 early warning 带来的实际干预收益\\\"\\n  - \\\"surplexity 和 spectral alignment 未在 iterative collapse 场景下交叉验证\\\"\\n  - \\\"跨任务 canary 普适性未知——reasoning vs retrieval vs creative tasks 中哪些 canary 更可靠\\\"\\n\\nnovelty_assessment: |\\n  我们项目的核心 novelty 在于：\\n\\n  1. **Panel Granger Causality 框架**：首次将多指标时序数据的因果分析方法应用于 model collapse 早期预警。\\n     现有工作（chen2025scales, gambetta2024surplexity）只是事后观察到某些指标先变化，\\n     但没有人做过系统的 lead-lag 量化分析。\\n\\n  2. **多指标 Canary Panel**：同时追踪 ECE、effective rank、Self-BLEU/distinct-n、\\n     perplexity、entropy、surplexity 等指标，分析其相互关系和各自的 lead time。\\n     现有工作都是单一指标或最多两三个指标的孤立分析。\\n\\n  3. **alpha-dependent Canary Sensitivity**：系统研究 synthetic ratio 如何影响各 canary\\n     指标的灵敏度和 lead time。dohmatob2025strong 证明极小的 alpha 就能触发 collapse，\\n     但没人研究 canary 在不同 alpha 下的行为。\\n\\n  4. **与已有工作的差异**：\\n     - vs chen2025scales: 他们发现 ECE 先退化但没有做因果分析；我们用 Granger causality 量化\\n     - vs gambetta2024surplexity: 他们提出 surplexity 用于检测和缓解 collapse；\\n       我们将其纳入更广的 panel 并研究其 lead-lag 特性\\n     - vs he2025closer: 他们在 diffusion 中用 entropy 作为指标；我们在 LLM 中测试更多指标\\n     - vs qiu2025spectral: 他们的 SA 用于训练 loss explosion 预警；\\n       我们将类似思路迁移到 iterative collapse 场景\\n\\n  5. **潜在风险**：chen2025scales 已经非常接近我们的方向。如果他们扩展到 lead-lag 分析，\\n     我们的 novelty 会被削弱。需要快速推进并在方法论（Granger causality）上建立壁垒。\\n\", \"total_chars\": 19466, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 10_

<details><summary>Logged reasoning block</summary>

```text
Good, I have the full literature_map.yaml. Now I need to search for the 6 papers. Let me search for all of them in parallel.

I can see the Bakshi & Chakraborty entry is `bakshi2026improvement` - it needs to be enriched with αt trajectory + nt scaling details.

Let me search for all 6 papers in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "915f124e-b4eb-466a-9dcc-643f257dc20c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QwZtaxYX3rN4esRTm2aqKk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10011,
      "cache_read_input_tokens": 24907,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10011
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

_source line 11_

现在并行搜索 6 篇论文的详细信息。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "36b84e8e-a6f8-4c27-9bd7-3805c960061a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QwZtaxYX3rN4esRTm2aqKk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10011,
      "cache_read_input_tokens": 24907,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10011
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

_source line 12_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Kgq9EhrzotdgcopteM72Ww`</summary>

```json
{
  "query": "arXiv 2601.03385 SIGMA spectral canary model collapse Gram matrix 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "75a0700f-31f7-4a4f-86f2-eaad922870c3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QwZtaxYX3rN4esRTm2aqKk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10011,
      "cache_read_input_tokens": 24907,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10011
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

_source line 13_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011FSBpXxnxFKJaykU7ZNEaq`</summary>

```json
{
  "query": "arXiv 2512.12381 Truong feedback entropy collapse first-order phase transition autocorrelation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "502ce078-08f4-4c60-961d-3806b2144e62",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QwZtaxYX3rN4esRTm2aqKk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10011,
      "cache_read_input_tokens": 24907,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10011
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

_source line 14_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TyXwFg9ZrFUeLeB9HL4k6S`</summary>

```json
{
  "query": "arXiv 2502.18865 Fu self-consuming loop convergence real data proportion ICLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "42f421ff-d0be-4dd1-a56a-cb540c9a1af9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QwZtaxYX3rN4esRTm2aqKk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10011,
      "cache_read_input_tokens": 24907,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10011
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

_source line 15_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MHRVfCXBPEmfKHQbwysmyx`</summary>

```json
{
  "query": "arXiv 2604.26984 Kalinowski topology monitoring model collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "f9579bb8-a87c-4e96-9d4f-03bf2c2df12e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QwZtaxYX3rN4esRTm2aqKk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10011,
      "cache_read_input_tokens": 24907,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10011
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VPjehg5g3PRcF7Fxvuqvbr`</summary>

```json
{
  "query": "arXiv 2602.16065 Wang universal approximator convergence self-consuming"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "5e2ba1dc-43b4-4b28-bb69-6e4614eea98f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QwZtaxYX3rN4esRTm2aqKk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10011,
      "cache_read_input_tokens": 24907,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10011
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_011PLqC2ug2oz8U8DPxVBYQd`</summary>

```json
{
  "query": "arXiv 2602.10531 Bakshi Chakraborty iterative training contaminated sources collapse improvement alpha trajectory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "2ecd527c-05f6-47bd-a9de-2de2ec73c45e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QwZtaxYX3rN4esRTm2aqKk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10011,
      "cache_read_input_tokens": 24907,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10011
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

_source line 18 · 2026-05-14T05:44:13.999Z_

<details><summary>↩ Tool result · `toolu_01Kgq9EhrzotdgcopteM72Ww`</summary>

```text
Web search results for query: "arXiv 2601.03385 SIGMA spectral canary model collapse Gram matrix 2026"

Links: [{"title":"[2601.03385] SIGMA: Scalable Spectral Insights for LLM Model Collapse","url":"https://arxiv.org/abs/2601.03385"},{"title":"Sigma: Scalable Spectral Insights for LLM Model Collapse","url":"https://arxiv.org/html/2601.03385"},{"title":"Sigma: Scalable Spectral Insights for LLM Collapse","url":"https://arxiv.org/html/2601.03385v1"},{"title":"SIGMA: Scalable Spectral Insights for LLM Model Collapse","url":"https://www.arxiv.org/pdf/2601.03385"},{"title":"The Homogeneity Trap: Spectral Collapse in Doubly-Stochastic Deep Networks","url":"https://arxiv.org/html/2601.02080"},{"title":"[2601.02080] The Homogeneity Trap: Spectral Collapse in Doubly-Stochastic Deep Networks","url":"https://arxiv.org/abs/2601.02080"},{"title":"[2601.11042v1] Spectral Characterization and Mitigation of Sequential Knowledge Editing Collapse","url":"https://arxiv.org/abs/2601.11042v1"},{"title":"[2601.11042] Spectral Characterization and Mitigation of Sequential Knowledge Editing Collapse","url":"https://arxiv.org/abs/2601.11042"},{"title":"[2512.13883] Renormalization group for spectral collapse in random matrices with power-law variance profiles","url":"https://arxiv.org/abs/2512.13883"},{"title":"Phase Transition of Spectral Fluctuations in Large Gram Matrices with a Variance Profile: A Unified Framework for Sparse CLTs","url":"https://arxiv.org/html/2602.04302"}]

Great! I found the paper you're looking for. Here are the key details:

SIGMA (Spectral Inequalities for Gram Matrix Analysis) is a unified framework that benchmarks model collapse through the spectral lens of the embedding Gram matrix.

The paper addresses "model collapse," a degenerative process where recursive training on model-generated content leads to a contraction of distributional variance and representational quality in Large Language Models (LLMs).

By deriving and utilizing deterministic and stochastic bounds on the matrix's spectrum, SIGMA provides a mathematically grounded metric to track the contraction of the representation space.

The paper was first submitted on January 6, 2026, with the latest version (v3) released on March 23, 2026. You can access the full paper at arxiv.org/abs/2601.03385.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "436d68d3-3519-440d-8e87-6aeb098f1dec",
  "tool_use_result": {
    "query": "arXiv 2601.03385 SIGMA spectral canary model collapse Gram matrix 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FsaFxQDTsNRPCf56LasjYx",
        "content": [
          {
            "title": "[2601.03385] SIGMA: Scalable Spectral Insights for LLM Model Collapse",
            "url": "https://arxiv.org/abs/2601.03385"
          },
          {
            "title": "Sigma: Scalable Spectral Insights for LLM Model Collapse",
            "url": "https://arxiv.org/html/2601.03385"
          },
          {
            "title": "Sigma: Scalable Spectral Insights for LLM Collapse",
            "url": "https://arxiv.org/html/2601.03385v1"
          },
          {
            "title": "SIGMA: Scalable Spectral Insights for LLM Model Collapse",
            "url": "https://www.arxiv.org/pdf/2601.03385"
          },
          {
            "title": "The Homogeneity Trap: Spectral Collapse in Doubly-Stochastic Deep Networks",
            "url": "https://arxiv.org/html/2601.02080"
          },
          {
            "title": "[2601.02080] The Homogeneity Trap: Spectral Collapse in Doubly-Stochastic Deep Networks",
            "url": "https://arxiv.org/abs/2601.02080"
          },
          {
            "title": "[2601.11042v1] Spectral Characterization and Mitigation of Sequential Knowledge Editing Collapse",
            "url": "https://arxiv.org/abs/2601.11042v1"
          },
          {
            "title": "[2601.11042] Spectral Characterization and Mitigation of Sequential Knowledge Editing Collapse",
            "url": "https://arxiv.org/abs/2601.11042"
          },
          {
            "title": "[2512.13883] Renormalization group for spectral collapse in random matrices with power-law variance profiles",
            "url": "https://arxiv.org/abs/2512.13883"
          },
          {
            "title": "Phase Transition of Spectral Fluctuations in Large Gram Matrices with a Variance Profile: A Unified Framework for Sparse CLTs",
            "url": "https://arxiv.org/html/2602.04302"
          }
        ]
      },
      "Great! I found the paper you're looking for. Here are the key details:\n\nSIGMA (Spectral Inequalities for Gram Matrix Analysis) is a unified framework that benchmarks model collapse through the spectral lens of the embedding Gram matrix.\n\nThe paper addresses \"model collapse,\" a degenerative process where recursive training on model-generated content leads to a contraction of distributional variance and representational quality in Large Language Models (LLMs).\n\nBy deriving and utilizing deterministic and stochastic bounds on the matrix's spectrum, SIGMA provides a mathematically grounded metric to track the contraction of the representation space.\n\nThe paper was first submitted on January 6, 2026, with the latest version (v3) released on March 23, 2026. You can access the full paper at arxiv.org/abs/2601.03385."
    ],
    "durationSeconds": 4.860833938
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-14T05:44:16.322Z_

<details><summary>↩ Tool result · `toolu_011FSBpXxnxFKJaykU7ZNEaq`</summary>

```text
Web search results for query: "arXiv 2512.12381 Truong feedback entropy collapse first-order phase transition autocorrelation"

Links: [{"title":"[2512.12381] Entropy Collapse: A Universal Failure Mode of Intelligent Systems","url":"https://arxiv.org/abs/2512.12381"},{"title":"Entropy Collapse: A Universal Failure Mode of Intelligent Systems Exact Phase Transition Analysis, First-Order Discontinuity, and Two Universality Classes","url":"https://arxiv.org/html/2512.12381"},{"title":"Entropy Collapse: A Universal Failure Mode of Intelligent Systems","url":"https://arxiv.org/pdf/2512.12381"},{"title":"Entropy Collapse: A Universal Failure Mode of Intelligent Systems","url":"https://www.researchgate.net/publication/398720042_Entropy_Collapse_A_Universal_Failure_Mode_of_Intelligent_Systems"},{"title":"Clip-Low Increases Entropy and Clip-High Decreases Entropy in Reinforcement Learning of Large Language Models | OpenReview","url":"https://openreview.net/forum?id=2ZflH67Uof"},{"title":"[2604.13123] Spectral Entropy Collapse as an Empirical Signature of Delayed Generalisation in Grokking","url":"https://arxiv.org/abs/2604.13123"},{"title":"why model randomness (entropy) collapses during ...","url":"https://www.facebook.com/0xSojalSec/posts/why-model-randomness-entropy-collapses-during-reinforcement-learning-for-reasoni/1375333587454374/"},{"title":"Phase transition revealed by eigen microstate entropy","url":"https://arxiv.org/html/2512.23086"},{"title":"Entropy Collapse: A Universal Failure Mode of Intelligent Systems by Truong Xuan Khanh, Truong Quynh Hoa :: SSRN","url":"https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6084126"},{"title":"Complete finite-size scaling theory of Rényi thermal entropy for second, first and weak first order quantum phase transitions","url":"https://arxiv.org/html/2506.16111"}]

I found the paper! Here are the key findings about arXiv 2512.12381:

## Paper Overview

The paper is titled "Entropy Collapse: A Universal Failure Mode of Intelligent Systems" by Truong Xuan Khanh and one other author.

## Main Results

The paper proves that entropy collapse—the irreversible contraction of effective state space when feedback amplification alpha exceeds novelty regeneration beta—is a first-order (discontinuous) phase transition.

## Relationship to Autocorrelation and Critical Slowing Down

A crucial finding concerns autocorrelation behavior. The paper challenges a foundational assumption that critical transitions are second-order and preceded by detectable early-warning signals like rising autocorrelation and critical slowing down. 

More specifically, because the transition is first-order rather than second-order, the critical-slowing-down early-warning framework does not apply, since the collapse is discontinuous with no preceding divergence of autocorrelation time, and entropy variance, autocorrelation, and return-time statistics all remain finite up to the collapse point.

## Broader Implications

The paper identifies entropy collapse as a universal dynamical mechanism through which intelligent systems transition from high-entropy adaptive regimes to low-entropy rigid regimes as feedback amplification overwhelms the system's bounded capacity to regenerate novelty.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "f0c5a832-c79c-450e-8bcb-1f348fb2ae37",
  "tool_use_result": {
    "query": "arXiv 2512.12381 Truong feedback entropy collapse first-order phase transition autocorrelation",
    "results": [
      {
        "tool_use_id": "srvtoolu_014P8F7qfsZeRwKKmNtXUrsS",
        "content": [
          {
            "title": "[2512.12381] Entropy Collapse: A Universal Failure Mode of Intelligent Systems",
            "url": "https://arxiv.org/abs/2512.12381"
          },
          {
            "title": "Entropy Collapse: A Universal Failure Mode of Intelligent Systems Exact Phase Transition Analysis, First-Order Discontinuity, and Two Universality Classes",
            "url": "https://arxiv.org/html/2512.12381"
          },
          {
            "title": "Entropy Collapse: A Universal Failure Mode of Intelligent Systems",
            "url": "https://arxiv.org/pdf/2512.12381"
          },
          {
            "title": "Entropy Collapse: A Universal Failure Mode of Intelligent Systems",
            "url": "https://www.researchgate.net/publication/398720042_Entropy_Collapse_A_Universal_Failure_Mode_of_Intelligent_Systems"
          },
          {
            "title": "Clip-Low Increases Entropy and Clip-High Decreases Entropy in Reinforcement Learning of Large Language Models | OpenReview",
            "url": "https://openreview.net/forum?id=2ZflH67Uof"
          },
          {
            "title": "[2604.13123] Spectral Entropy Collapse as an Empirical Signature of Delayed Generalisation in Grokking",
            "url": "https://arxiv.org/abs/2604.13123"
          },
          {
            "title": "why model randomness (entropy) collapses during ...",
            "url": "https://www.facebook.com/0xSojalSec/posts/why-model-randomness-entropy-collapses-during-reinforcement-learning-for-reasoni/1375333587454374/"
          },
          {
            "title": "Phase transition revealed by eigen microstate entropy",
            "url": "https://arxiv.org/html/2512.23086"
          },
          {
            "title": "Entropy Collapse: A Universal Failure Mode of Intelligent Systems by Truong Xuan Khanh, Truong Quynh Hoa :: SSRN",
            "url": "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6084126"
          },
          {
            "title": "Complete finite-size scaling theory of Rényi thermal entropy for second, first and weak first order quantum phase transitions",
            "url": "https://arxiv.org/html/2506.16111"
          }
        ]
      },
      "I found the paper! Here are the key findings about arXiv 2512.12381:\n\n## Paper Overview\n\nThe paper is titled \"Entropy Collapse: A Universal Failure Mode of Intelligent Systems\" by Truong Xuan Khanh and one other author.\n\n## Main Results\n\nThe paper proves that entropy collapse—the irreversible contraction of effective state space when feedback amplification alpha exceeds novelty regeneration beta—is a first-order (discontinuous) phase transition.\n\n## Relationship to Autocorrelation and Critical Slowing Down\n\nA crucial finding concerns autocorrelation behavior. The paper challenges a foundational assumption that critical transitions are second-order and preceded by detectable early-warning signals like rising autocorrelation and critical slowing down. \n\nMore specifically, because the transition is first-order rather than second-order, the critical-slowing-down early-warning framework does not apply, since the collapse is discontinuous with no preceding divergence of autocorrelation time, and entropy variance, autocorrelation, and return-time statistics all remain finite up to the collapse point.\n\n## Broader Implications\n\nThe paper identifies entropy collapse as a universal dynamical mechanism through which intelligent systems transition from high-entropy adaptive regimes to low-entropy rigid regimes as feedback amplification overwhelms the system's bounded capacity to regenerate novelty."
    ],
    "durationSeconds": 6.032963087
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T05:44:18.321Z_

<details><summary>↩ Tool result · `toolu_01MHRVfCXBPEmfKHQbwysmyx`</summary>

```text
Web search results for query: "arXiv 2604.26984 Kalinowski topology monitoring model collapse"

Links: [{"title":"[2604.26984] Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index","url":"https://arxiv.org/abs/2604.26984"},{"title":"Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index","url":"https://arxiv.org/html/2604.26984"},{"title":"[2604.26068] Calibrated Persistent Homology Tests for High-dimensional Collapse Detection","url":"https://arxiv.org/abs/2604.26068"},{"title":"[2604.27318] Revealing Strategic Interactions in Network Games Under Decaying Active Probing","url":"https://arxiv.org/abs/2604.27318"},{"title":"[2604.19268] Comparison of model order reduction techniques with one-shot procedure for topology optimization for thermal applications","url":"https://arxiv.org/abs/2604.19268"},{"title":"[2604.27962] Language Models Refine Mechanical Linkage Designs Through Symbolic Reflection and Modular Optimisation","url":"https://arxiv.org/abs/2604.27962"},{"title":"Newton–Cartan limit of Klein–Gordon AQFT and the collapse of Galilean modular structure","url":"https://arxiv.org/html/2604.26287"},{"title":"[2604.26610] Linking extended vector wave fields with momentum space topology","url":"https://arxiv.org/abs/2604.26610"},{"title":"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective","url":"https://arxiv.org/html/2509.16499v2"},{"title":"[2604.27208] Reliability-based Topology Optimization using Large Deviation Theory","url":"https://arxiv.org/abs/2604.27208"}]

I found the paper you're looking for! Here's what it's about:

The paper "Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index" by Alexander Kalinowski addresses representational collapse, where embeddings become anisotropic and lose multi-scale structure.

The researchers propose an online, topology-aware monitor that couples Modular Morse Homology Maintenance (MMHM) with a composite Collapse Index (CI). Instead of rebuilding complexes each epoch, they apply sparse edits at a fixed scale and maintain a discrete Morse matching, yielding fast, incremental updates.

Across LLM fine-tuning and temporal KGE training, the CI provides a low-latency early-warning signal suitable for in-training interventions. The paper was submitted on April 28, 2026 (arXiv:2604.26984).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "999df370-44e4-4f8a-82eb-ee92f01d131d",
  "tool_use_result": {
    "query": "arXiv 2604.26984 Kalinowski topology monitoring model collapse",
    "results": [
      {
        "tool_use_id": "srvtoolu_01C2iCftF11XNMZ1NBAGEEAa",
        "content": [
          {
            "title": "[2604.26984] Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index",
            "url": "https://arxiv.org/abs/2604.26984"
          },
          {
            "title": "Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index",
            "url": "https://arxiv.org/html/2604.26984"
          },
          {
            "title": "[2604.26068] Calibrated Persistent Homology Tests for High-dimensional Collapse Detection",
            "url": "https://arxiv.org/abs/2604.26068"
          },
          {
            "title": "[2604.27318] Revealing Strategic Interactions in Network Games Under Decaying Active Probing",
            "url": "https://arxiv.org/abs/2604.27318"
          },
          {
            "title": "[2604.19268] Comparison of model order reduction techniques with one-shot procedure for topology optimization for thermal applications",
            "url": "https://arxiv.org/abs/2604.19268"
          },
          {
            "title": "[2604.27962] Language Models Refine Mechanical Linkage Designs Through Symbolic Reflection and Modular Optimisation",
            "url": "https://arxiv.org/abs/2604.27962"
          },
          {
            "title": "Newton–Cartan limit of Klein–Gordon AQFT and the collapse of Galilean modular structure",
            "url": "https://arxiv.org/html/2604.26287"
          },
          {
            "title": "[2604.26610] Linking extended vector wave fields with momentum space topology",
            "url": "https://arxiv.org/abs/2604.26610"
          },
          {
            "title": "A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective",
            "url": "https://arxiv.org/html/2509.16499v2"
          },
          {
            "title": "[2604.27208] Reliability-based Topology Optimization using Large Deviation Theory",
            "url": "https://arxiv.org/abs/2604.27208"
          }
        ]
      },
      "I found the paper you're looking for! Here's what it's about:\n\nThe paper \"Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index\" by Alexander Kalinowski addresses representational collapse, where embeddings become anisotropic and lose multi-scale structure.\n\nThe researchers propose an online, topology-aware monitor that couples Modular Morse Homology Maintenance (MMHM) with a composite Collapse Index (CI). Instead of rebuilding complexes each epoch, they apply sparse edits at a fixed scale and maintain a discrete Morse matching, yielding fast, incremental updates.\n\nAcross LLM fine-tuning and temporal KGE training, the CI provides a low-latency early-warning signal suitable for in-training interventions. The paper was submitted on April 28, 2026 (arXiv:2604.26984)."
    ],
    "durationSeconds": 6.392769185000001
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-14T05:44:18.468Z_

<details><summary>↩ Tool result · `toolu_01TyXwFg9ZrFUeLeB9HL4k6S`</summary>

```text
Web search results for query: "arXiv 2502.18865 Fu self-consuming loop convergence real data proportion ICLR 2025"

Links: [{"title":"[2502.18865] A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops","url":"https://arxiv.org/abs/2502.18865"},{"title":"A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops","url":"https://arxiv.org/html/2502.18865"},{"title":"How to Prevent Model Collapse in Self-consuming Training ...","url":"https://arxiv.org/pdf/2502.18865"},{"title":"Convergence and Stability Analysis of Self-Consuming Generative Models with Heterogeneous Human Curation","url":"https://arxiv.org/html/2511.09002"},{"title":"Self-Correcting Self-Consuming Loops for Generative Model Training","url":"https://arxiv.org/html/2402.07087v2"},{"title":"[2402.11778v2] Towards Theoretical Understandings of Self-Consuming Generative Models","url":"https://arxiv.org/abs/2402.11778v2"},{"title":"Self-Consuming Generative Models with Adversarially Curated Data","url":"https://arxiv.org/html/2505.09768"},{"title":"Self-Consuming Generative Models with Curated Data Provably Optimize Human Preferences","url":"https://arxiv.org/html/2407.09499v1"},{"title":"Self-Consuming AI Resources","url":"https://dsp.rice.edu/ai-loops/"},{"title":"[2402.11778] Towards Theoretical Understandings of Self-Consuming Generative Models","url":"https://arxiv.org/abs/2402.11778"}]

I found the paper you're looking for! Here's the information about arXiv 2502.18865:

## Paper Details

**Title:** "A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops"

**Authors:** Shi Fu, Yingjie Wang, Yuzhu Chen, Xinmei Tian, Dacheng Tao

**Submission Date:** February 26, 2025

## Key Contributions

The paper introduces the notion of recursive stability and presents the first theoretical generalization analysis, revealing how both model architecture and the proportion between real and synthetic data influence the success of self-consuming training loops (STLs).

**Main Finding on Real Data Proportion:** The analysis shows that even a constant-sized proportion of real data ensures convergence, while also providing insights into optimal synthetic data sizing.

## Problem Statement

High-quality data is essential for training large generative models, yet the vast reservoir of real data available online has become nearly depleted. Consequently, models increasingly generate their own data for further training, forming Self-consuming Training Loops (STLs). However, the empirical results have been strikingly inconsistent: some models degrade or even collapse, while others successfully avoid these failures, leaving a significant gap in theoretical understanding to explain this discrepancy.

The paper is available on arXiv at https://arxiv.org/abs/2502.18865


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "0fd7edd8-46e4-4ebf-bae5-b28c77909a20",
  "tool_use_result": {
    "query": "arXiv 2502.18865 Fu self-consuming loop convergence real data proportion ICLR 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_018xDbmEaGDvzqxT3tkUsvUy",
        "content": [
          {
            "title": "[2502.18865] A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops",
            "url": "https://arxiv.org/abs/2502.18865"
          },
          {
            "title": "A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops",
            "url": "https://arxiv.org/html/2502.18865"
          },
          {
            "title": "How to Prevent Model Collapse in Self-consuming Training ...",
            "url": "https://arxiv.org/pdf/2502.18865"
          },
          {
            "title": "Convergence and Stability Analysis of Self-Consuming Generative Models with Heterogeneous Human Curation",
            "url": "https://arxiv.org/html/2511.09002"
          },
          {
            "title": "Self-Correcting Self-Consuming Loops for Generative Model Training",
            "url": "https://arxiv.org/html/2402.07087v2"
          },
          {
            "title": "[2402.11778v2] Towards Theoretical Understandings of Self-Consuming Generative Models",
            "url": "https://arxiv.org/abs/2402.11778v2"
          },
          {
            "title": "Self-Consuming Generative Models with Adversarially Curated Data",
            "url": "https://arxiv.org/html/2505.09768"
          },
          {
            "title": "Self-Consuming Generative Models with Curated Data Provably Optimize Human Preferences",
            "url": "https://arxiv.org/html/2407.09499v1"
          },
          {
            "title": "Self-Consuming AI Resources",
            "url": "https://dsp.rice.edu/ai-loops/"
          },
          {
            "title": "[2402.11778] Towards Theoretical Understandings of Self-Consuming Generative Models",
            "url": "https://arxiv.org/abs/2402.11778"
          }
        ]
      },
      "I found the paper you're looking for! Here's the information about arXiv 2502.18865:\n\n## Paper Details\n\n**Title:** \"A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops\"\n\n**Authors:** Shi Fu, Yingjie Wang, Yuzhu Chen, Xinmei Tian, Dacheng Tao\n\n**Submission Date:** February 26, 2025\n\n## Key Contributions\n\nThe paper introduces the notion of recursive stability and presents the first theoretical generalization analysis, revealing how both model architecture and the proportion between real and synthetic data influence the success of self-consuming training loops (STLs).\n\n**Main Finding on Real Data Proportion:** The analysis shows that even a constant-sized proportion of real data ensures convergence, while also providing insights into optimal synthetic data sizing.\n\n## Problem Statement\n\nHigh-quality data is essential for training large generative models, yet the vast reservoir of real data available online has become nearly depleted. Consequently, models increasingly generate their own data for further training, forming Self-consuming Training Loops (STLs). However, the empirical results have been strikingly inconsistent: some models degrade or even collapse, while others successfully avoid these failures, leaving a significant gap in theoretical understanding to explain this discrepancy.\n\nThe paper is available on arXiv at https://arxiv.org/abs/2502.18865"
    ],
    "durationSeconds": 7.480179183000001
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T05:44:18.524Z_

<details><summary>↩ Tool result · `toolu_01VPjehg5g3PRcF7Fxvuqvbr`</summary>

```text
Web search results for query: "arXiv 2602.16065 Wang universal approximator convergence self-consuming"

Links: [{"title":"[2602.16065] Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training","url":"https://arxiv.org/abs/2602.16065"},{"title":"[2506.16065] Floating-Point Neural Networks Are Provably Robust Universal Approximators","url":"https://arxiv.org/abs/2506.16065"},{"title":"Floating-Point Neural Networks Are Provably Robust Universal Approximators","url":"https://arxiv.org/html/2506.16065"},{"title":"Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training","url":"https://arxiv.org/html/2602.16065"},{"title":"Convergence and Stability Analysis of Self-Consuming Generative","url":"https://arxiv.org/pdf/2511.09002"},{"title":"[2602.09718] SAQNN: Spectral Adaptive Quantum Neural Network as a Universal Approximator","url":"https://arxiv.org/abs/2602.09718"},{"title":"[2602.03386v1] An Approximate Ascent Approach To Prove Convergence of PPO","url":"https://arxiv.org/abs/2602.03386v1"},{"title":"[1803.05391] On the Universal Approximation Property and Equivalence of Stochastic Computing-based Neural Networks and Binary Neural Networks","url":"https://arxiv.org/abs/1803.05391"},{"title":"[2602.13906] Quantifying Normality: Convergence Rate to Gaussian Limit for Stochastic Approximation and Unadjusted OU Algorithm","url":"https://arxiv.org/abs/2602.13906"},{"title":"Dynamic Universal Approximation Theory: The Basic Theory for Residual-Based Deep Learning Computer Vision Models","url":"https://arxiv.org/html/2407.17480v4"}]

Based on the search results, I found information about arXiv paper 2602.16065:

The paper is titled "Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training" by Kevin Wang and 2 other authors.

The paper addresses an important problem in generative AI: as generative models are updated regularly, later models will inevitably be trained on mixtures of human-generated data and AI-generated data from earlier versions, creating a recursive training process with data contamination.

The key contribution is that the authors study recursive training in a general framework with minimal assumptions on the real data distribution and allow the underlying generative model to be a general universal approximator, showing that contaminated recursive training still converges, with a convergence rate equal to the minimum of the baseline model's convergence rate and the fraction of real data used in each iteration.

This is claimed to be the first (positive) theoretical result on recursive training without distributional assumptions on the data. The work represents an advancement over prior theoretical work which had only examined simplified settings where data and models were discrete or Gaussian.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "6dde29fd-03cc-40ce-a54b-323460c5d492",
  "tool_use_result": {
    "query": "arXiv 2602.16065 Wang universal approximator convergence self-consuming",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BiFGWnGdZCWK5fouiGSaa7",
        "content": [
          {
            "title": "[2602.16065] Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training",
            "url": "https://arxiv.org/abs/2602.16065"
          },
          {
            "title": "[2506.16065] Floating-Point Neural Networks Are Provably Robust Universal Approximators",
            "url": "https://arxiv.org/abs/2506.16065"
          },
          {
            "title": "Floating-Point Neural Networks Are Provably Robust Universal Approximators",
            "url": "https://arxiv.org/html/2506.16065"
          },
          {
            "title": "Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training",
            "url": "https://arxiv.org/html/2602.16065"
          },
          {
            "title": "Convergence and Stability Analysis of Self-Consuming Generative",
            "url": "https://arxiv.org/pdf/2511.09002"
          },
          {
            "title": "[2602.09718] SAQNN: Spectral Adaptive Quantum Neural Network as a Universal Approximator",
            "url": "https://arxiv.org/abs/2602.09718"
          },
          {
            "title": "[2602.03386v1] An Approximate Ascent Approach To Prove Convergence of PPO",
            "url": "https://arxiv.org/abs/2602.03386v1"
          },
          {
            "title": "[1803.05391] On the Universal Approximation Property and Equivalence of Stochastic Computing-based Neural Networks and Binary Neural Networks",
            "url": "https://arxiv.org/abs/1803.05391"
          },
          {
            "title": "[2602.13906] Quantifying Normality: Convergence Rate to Gaussian Limit for Stochastic Approximation and Unadjusted OU Algorithm",
            "url": "https://arxiv.org/abs/2602.13906"
          },
          {
            "title": "Dynamic Universal Approximation Theory: The Basic Theory for Residual-Based Deep Learning Computer Vision Models",
            "url": "https://arxiv.org/html/2407.17480v4"
          }
        ]
      },
      "Based on the search results, I found information about arXiv paper 2602.16065:\n\nThe paper is titled \"Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training\" by Kevin Wang and 2 other authors.\n\nThe paper addresses an important problem in generative AI: as generative models are updated regularly, later models will inevitably be trained on mixtures of human-generated data and AI-generated data from earlier versions, creating a recursive training process with data contamination.\n\nThe key contribution is that the authors study recursive training in a general framework with minimal assumptions on the real data distribution and allow the underlying generative model to be a general universal approximator, showing that contaminated recursive training still converges, with a convergence rate equal to the minimum of the baseline model's convergence rate and the fraction of real data used in each iteration.\n\nThis is claimed to be the first (positive) theoretical result on recursive training without distributional assumptions on the data. The work represents an advancement over prior theoretical work which had only examined simplified settings where data and models were discrete or Gaussian."
    ],
    "durationSeconds": 6.061889673000001
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-14T05:44:21.325Z_

<details><summary>↩ Tool result · `toolu_011PLqC2ug2oz8U8DPxVBYQd`</summary>

```text
Web search results for query: "arXiv 2602.10531 Bakshi Chakraborty iterative training contaminated sources collapse improvement alpha trajectory"

Links: [{"title":"[2602.10531] From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources","url":"https://arxiv.org/abs/2602.10531"},{"title":"[2602.10531v1] From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources","url":"https://arxiv.org/abs/2602.10531v1"},{"title":"From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources","url":"https://arxiv.org/html/2602.10531"},{"title":"Machine Learning","url":"https://www.arxiv.org/list/cs.LG/recent?skip=173&show=2000"},{"title":"Neural Hodge Corrective Solvers: A Hybrid Iterative–Neural Framework","url":"https://arxiv.org/html/2602.03404"},{"title":"Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training","url":"https://arxiv.org/html/2602.16065"},{"title":"The Impact of Post-training on Data Contamination","url":"https://arxiv.org/html/2601.06103"},{"title":"[2305.10531] Iteratively Learning Representations for Unseen Entities with Inter-Rule Correlations","url":"https://arxiv.org/abs/2305.10531"},{"title":"A Task-Centric Theory for Iterative Self-Improvement with Easy-to-Hard Curricula","url":"https://arxiv.org/html/2602.10014"},{"title":"[2503.19620] Optimization through In-Context Learning and Iterative LLM Prompting for Nuclear Engineering Design Problems","url":"https://arxiv.org/abs/2503.19620"}]

I found the paper you're looking for! Here's the information about arXiv 2602.10531:

**Title:** From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources

**Authors:** Soham Bakshi and Sunrit Chakraborty

**Main Topic:** The problem of model collapse has presented new challenges in iterative training of generative models, where such training with synthetic data leads to an overall degradation of performance.

**Key Contribution:** The paper looks at the problem from a statistical viewpoint, illustrating that one can actually hope for improvement when models are trained on data contaminated with synthetic samples, as long as there is some amount of fresh information from the true target distribution.

**Research Approach:** The authors consider iterative training on samples sourced from a mixture of the true target and synthetic distributions, analyzing the entire iterative evolution in a next-token prediction language model, capturing how the interplay between the mixture weights and the sample size controls the overall long-term performance.

**Timeline:** The paper was submitted on 11 Feb 2026 (v1), with the latest version (v2) revised on 17 Feb 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "3b25e6a5-0010-4d88-9bf3-64257ccd5bee",
  "tool_use_result": {
    "query": "arXiv 2602.10531 Bakshi Chakraborty iterative training contaminated sources collapse improvement alpha trajectory",
    "results": [
      {
        "tool_use_id": "srvtoolu_012ia6pdbBbpNpeVbiqTYcXQ",
        "content": [
          {
            "title": "[2602.10531] From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources",
            "url": "https://arxiv.org/abs/2602.10531"
          },
          {
            "title": "[2602.10531v1] From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources",
            "url": "https://arxiv.org/abs/2602.10531v1"
          },
          {
            "title": "From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources",
            "url": "https://arxiv.org/html/2602.10531"
          },
          {
            "title": "Machine Learning",
            "url": "https://www.arxiv.org/list/cs.LG/recent?skip=173&show=2000"
          },
          {
            "title": "Neural Hodge Corrective Solvers: A Hybrid Iterative–Neural Framework",
            "url": "https://arxiv.org/html/2602.03404"
          },
          {
            "title": "Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training",
            "url": "https://arxiv.org/html/2602.16065"
          },
          {
            "title": "The Impact of Post-training on Data Contamination",
            "url": "https://arxiv.org/html/2601.06103"
          },
          {
            "title": "[2305.10531] Iteratively Learning Representations for Unseen Entities with Inter-Rule Correlations",
            "url": "https://arxiv.org/abs/2305.10531"
          },
          {
            "title": "A Task-Centric Theory for Iterative Self-Improvement with Easy-to-Hard Curricula",
            "url": "https://arxiv.org/html/2602.10014"
          },
          {
            "title": "[2503.19620] Optimization through In-Context Learning and Iterative LLM Prompting for Nuclear Engineering Design Problems",
            "url": "https://arxiv.org/abs/2503.19620"
          }
        ]
      },
      "I found the paper you're looking for! Here's the information about arXiv 2602.10531:\n\n**Title:** From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources\n\n**Authors:** Soham Bakshi and Sunrit Chakraborty\n\n**Main Topic:** The problem of model collapse has presented new challenges in iterative training of generative models, where such training with synthetic data leads to an overall degradation of performance.\n\n**Key Contribution:** The paper looks at the problem from a statistical viewpoint, illustrating that one can actually hope for improvement when models are trained on data contaminated with synthetic samples, as long as there is some amount of fresh information from the true target distribution.\n\n**Research Approach:** The authors consider iterative training on samples sourced from a mixture of the true target and synthetic distributions, analyzing the entire iterative evolution in a next-token prediction language model, capturing how the interplay between the mixture weights and the sample size controls the overall long-term performance.\n\n**Timeline:** The paper was submitted on 11 Feb 2026 (v1), with the latest version (v2) revised on 17 Feb 2026."
    ],
    "durationSeconds": 8.249973096000002
  }
}
```

</details>

---

### Assistant

_source line 24_

<details><summary>Logged reasoning block</summary>

```text
Now let me get more details on the papers. Let me search for more specific details on a few that need more info.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "62ee6208-e406-4c24-b22d-efcafec4f532",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JA523txTs4A6Z3QBQiLq7U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5368,
      "cache_read_input_tokens": 34918,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5368
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

_source line 25_

Let me get more specific details on a few papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "8e97a026-b136-4e36-a3f4-c54d2961b583",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JA523txTs4A6Z3QBQiLq7U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5368,
      "cache_read_input_tokens": 34918,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5368
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

_source line 26_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011oKhMsVZESfdkj7aNRmhDn`</summary>

```json
{
  "query": "SIGMA scalable spectral insights LLM model collapse Track I Track II Gram matrix spectral norm arxiv 2601.03385 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "fc54ae87-ee4b-4fe8-8b2e-7f14d579a672",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JA523txTs4A6Z3QBQiLq7U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5368,
      "cache_read_input_tokens": 34918,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5368
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

_source line 27_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AYssw8QXNFePEDmHAYgzVT`</summary>

```json
{
  "query": "Kalinowski \"Monitoring Neural Training with Topology\" \"Footprint-Predictable Collapse Index\" authors MMHM 2604.26984"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "f70aa68c-4244-416c-95c0-00a6302c54be",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JA523txTs4A6Z3QBQiLq7U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5368,
      "cache_read_input_tokens": 34918,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5368
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

_source line 28_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VDY23sv2fobwqdUvbaq21b`</summary>

```json
{
  "query": "\"Can Generative Artificial Intelligence Survive Data Contamination\" Wang 2602.16065 authors convergence rate universal approximator"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "0bc08158-fee5-43a0-9ca4-0f387a0c0a62",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JA523txTs4A6Z3QBQiLq7U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5368,
      "cache_read_input_tokens": 34918,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5368
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

_source line 29_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TgW1TRtJHNaZe2iK7rzF3A`</summary>

```json
{
  "query": "Bakshi Chakraborty \"From Collapse to Improvement\" alpha_t trajectory n_t scaling collapse improvement consistency conditions 2602.10531"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "9a1f991f-19b9-4045-bdba-fde0407837f2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JA523txTs4A6Z3QBQiLq7U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5368,
      "cache_read_input_tokens": 34918,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5368
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

_source line 30 · 2026-05-14T05:44:32.383Z_

<details><summary>↩ Tool result · `toolu_01AYssw8QXNFePEDmHAYgzVT`</summary>

```text
Web search results for query: "Kalinowski "Monitoring Neural Training with Topology" "Footprint-Predictable Collapse Index" authors MMHM 2604.26984"

Links: [{"title":"[2604.26984] Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index","url":"https://arxiv.org/abs/2604.26984"},{"title":"Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index","url":"https://arxiv.org/html/2604.26984"},{"title":"FALCON: Feature-Label Constrained Graph Net Collapse for Memory Efficient GNNs","url":"https://arxiv.org/html/2312.16542"},{"title":"Topology of Deep Neural Networks","url":"https://jmlr.csail.mit.edu/papers/volume21/20-345/20-345.pdf"},{"title":"ICLR Poster Scaling with Collapse: Efficient and Predictable Training of LLM Families","url":"https://iclr.cc/virtual/2026/poster/10011632"},{"title":"Neural network surgery: Combining training with topology optimization - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0893608021003476"},{"title":"Topology optimization via machine learning and deep learning: a review | Journal of Computational Design and Engineering | Oxford Academic","url":"https://academic.oup.com/jcde/article/10/4/1736/7223974"},{"title":"Neural topology optimization: the good, the bad, and the ugly","url":"https://arxiv.org/html/2407.13954v1"},{"title":"Scaling with Collapse: Efficient and Predictable Training of LLM Families","url":"https://arxiv.org/html/2509.25087v1"},{"title":"Leveraging Evidential Deep Learning Uncertainties with ...","url":"https://arxiv.org/pdf/2107.01557"}]

Based on the search results, I found the paper you were looking for:

The paper "Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index" is by Alexander Kalinowski. It proposes an online, topology-aware monitor for evolving neural representations that couples Modular Morse Homology Maintenance (MMHM) with a composite Collapse Index (CI).

The approach applies sparse edits at fixed scale and maintains a discrete Morse matching for fast, incremental updates. Across LLM fine-tuning and temporal KGE training, the CI provides a low-latency early-warning signal suitable for in-training interventions.

The paper is archived on arXiv with the identifier 2604.26984, as indicated in your search query.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "2be0a300-8b84-4aa2-8a24-4bdbbc5017a6",
  "tool_use_result": {
    "query": "Kalinowski \"Monitoring Neural Training with Topology\" \"Footprint-Predictable Collapse Index\" authors MMHM 2604.26984",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XnbJggiBQdivAcsAoFc3nC",
        "content": [
          {
            "title": "[2604.26984] Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index",
            "url": "https://arxiv.org/abs/2604.26984"
          },
          {
            "title": "Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index",
            "url": "https://arxiv.org/html/2604.26984"
          },
          {
            "title": "FALCON: Feature-Label Constrained Graph Net Collapse for Memory Efficient GNNs",
            "url": "https://arxiv.org/html/2312.16542"
          },
          {
            "title": "Topology of Deep Neural Networks",
            "url": "https://jmlr.csail.mit.edu/papers/volume21/20-345/20-345.pdf"
          },
          {
            "title": "ICLR Poster Scaling with Collapse: Efficient and Predictable Training of LLM Families",
            "url": "https://iclr.cc/virtual/2026/poster/10011632"
          },
          {
            "title": "Neural network surgery: Combining training with topology optimization - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/pii/S0893608021003476"
          },
          {
            "title": "Topology optimization via machine learning and deep learning: a review | Journal of Computational Design and Engineering | Oxford Academic",
            "url": "https://academic.oup.com/jcde/article/10/4/1736/7223974"
          },
          {
            "title": "Neural topology optimization: the good, the bad, and the ugly",
            "url": "https://arxiv.org/html/2407.13954v1"
          },
          {
            "title": "Scaling with Collapse: Efficient and Predictable Training of LLM Families",
            "url": "https://arxiv.org/html/2509.25087v1"
          },
          {
            "title": "Leveraging Evidential Deep Learning Uncertainties with ...",
            "url": "https://arxiv.org/pdf/2107.01557"
          }
        ]
      },
      "Based on the search results, I found the paper you were looking for:\n\nThe paper \"Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index\" is by Alexander Kalinowski. It proposes an online, topology-aware monitor for evolving neural representations that couples Modular Morse Homology Maintenance (MMHM) with a composite Collapse Index (CI).\n\nThe approach applies sparse edits at fixed scale and maintains a discrete Morse matching for fast, incremental updates. Across LLM fine-tuning and temporal KGE training, the CI provides a low-latency early-warning signal suitable for in-training interventions.\n\nThe paper is archived on arXiv with the identifier 2604.26984, as indicated in your search query."
    ],
    "durationSeconds": 5.291955757000004
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-14T05:44:32.421Z_

<details><summary>↩ Tool result · `toolu_01TgW1TRtJHNaZe2iK7rzF3A`</summary>

```text
Web search results for query: "Bakshi Chakraborty "From Collapse to Improvement" alpha_t trajectory n_t scaling collapse improvement consistency conditions 2602.10531"

Links: [{"title":"[2602.10531] From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources","url":"https://arxiv.org/abs/2602.10531"},{"title":"[2602.10531v1] From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources","url":"https://arxiv.org/abs/2602.10531v1"},{"title":"From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources","url":"https://arxiv.org/html/2602.10531"},{"title":"From Collapse to Improvement: Statistical Perspectives on the Evolutionary","url":"https://arxiv.org/pdf/2602.10531"}]

The search has successfully found the paper you're looking for. The paper "From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources" is authored by Soham Bakshi and Sunrit Chakraborty (arXiv:2602.10531).

The paper addresses the problem of model collapse in iterative training of generative models with synthetic data, showing from a statistical viewpoint that improvement is possible when models are trained on data contaminated with synthetic samples, as long as there is fresh information from the true target distribution.

The authors analyze the entire iterative evolution in a next-token prediction language model, capturing how the interplay between mixture weights and sample size controls the overall long-term performance. They characterize conditions on mixture weights and sample sizes under which statistical estimation of the target distribution improves.

The paper was submitted on February 11, 2026, with a revised version on February 17, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "2dc7b05c-58e9-490e-8de8-12a80afacddb",
  "tool_use_result": {
    "query": "Bakshi Chakraborty \"From Collapse to Improvement\" alpha_t trajectory n_t scaling collapse improvement consistency conditions 2602.10531",
    "results": [
      {
        "tool_use_id": "srvtoolu_01X9VaSB2WFSzLxzQG5LCkYv",
        "content": [
          {
            "title": "[2602.10531] From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources",
            "url": "https://arxiv.org/abs/2602.10531"
          },
          {
            "title": "[2602.10531v1] From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources",
            "url": "https://arxiv.org/abs/2602.10531v1"
          },
          {
            "title": "From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources",
            "url": "https://arxiv.org/html/2602.10531"
          },
          {
            "title": "From Collapse to Improvement: Statistical Perspectives on the Evolutionary",
            "url": "https://arxiv.org/pdf/2602.10531"
          }
        ]
      },
      "The search has successfully found the paper you're looking for. The paper \"From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources\" is authored by Soham Bakshi and Sunrit Chakraborty (arXiv:2602.10531).\n\nThe paper addresses the problem of model collapse in iterative training of generative models with synthetic data, showing from a statistical viewpoint that improvement is possible when models are trained on data contaminated with synthetic samples, as long as there is fresh information from the true target distribution.\n\nThe authors analyze the entire iterative evolution in a next-token prediction language model, capturing how the interplay between mixture weights and sample size controls the overall long-term performance. They characterize conditions on mixture weights and sample sizes under which statistical estimation of the target distribution improves.\n\nThe paper was submitted on February 11, 2026, with a revised version on February 17, 2026."
    ],
    "durationSeconds": 3.860938992000003
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-14T05:44:33.173Z_

<details><summary>↩ Tool result · `toolu_011oKhMsVZESfdkj7aNRmhDn`</summary>

```text
Web search results for query: "SIGMA scalable spectral insights LLM model collapse Track I Track II Gram matrix spectral norm arxiv 2601.03385 authors"

Links: [{"title":"[2601.03385] SIGMA: Scalable Spectral Insights for LLM Model Collapse","url":"https://arxiv.org/abs/2601.03385"},{"title":"SIGMA: Scalable Spectral Insights for LLM Model Collapse","url":"https://www.arxiv.org/pdf/2601.03385"},{"title":"Sigma: Scalable Spectral Insights for LLM Model Collapse","url":"https://arxiv.org/html/2601.03385"},{"title":"Sigma: Scalable Spectral Insights for LLM Collapse","url":"https://arxiv.org/html/2601.03385v1"},{"title":"Rohan Paul on X: \"The authors measure LLM health by sampling embeddings and checking whether the meaning space keeps shrinking over training cycles. SIGMA spots LLM collapse early by measuring how much their sentence embedding space shrinks during self training. Recursive training on model https://t.co/ixJmA3N4y7\" / X","url":"https://x.com/rohanpaul_ai/status/2011373977176846463/photo/1"},{"title":"[2601.11042v1] Spectral Characterization and Mitigation of Sequential Knowledge Editing Collapse","url":"https://arxiv.org/abs/2601.11042v1"},{"title":"HyperSIGMA: Hyperspectral Intelligence Comprehension Foundation Model","url":"https://arxiv.org/html/2406.11519v1"},{"title":"Has LLM Reached the Scaling Ceiling Yet? Unified Insights into LLM Regularities and Constraints","url":"https://arxiv.org/html/2412.16443v1"},{"title":"arXiv:2506.23025v1 [cs.LG] 28 Jun 2025","url":"https://arxiv.org/pdf/2506.23025"},{"title":"Controlled LLM Training on Spectral Sphere","url":"https://arxiv.org/html/2601.08393"}]

I found the paper! Here's what I discovered:

## SIGMA: Scalable Spectral Insights for LLM Model Collapse

**arXiv**: 2601.03385 (submitted January 6, 2026; latest version March 23, 2026)

**Authors**: Yi Gu, Lingyou Pang, Xiangkun Ye, Tianyu Wang, Jianyu Lin, Carey E. Priebe, and Alexander Aue

### Overview

SIGMA (Spectral Inequalities for Gram Matrix Analysis) is a unified framework that benchmarks model collapse through the spectral lens of the embedding Gram matrix. By deriving and utilizing deterministic and stochastic bounds on the matrix's spectrum, SIGMA provides a mathematically grounded metric to track the contraction of the representation space.

### The Problem

The rapid adoption of synthetic data for training Large Language Models (LLMs) has introduced the technical challenge of "model collapse"—a degenerative process where recursive training on model-generated content leads to a contraction of distributional variance and representational quality.

### Key Features

The method utilizes both deterministic and stochastic bounds to function effectively even with partially observed data, ensuring the framework remains scalable for large-scale models. SIGMA proposes a spectral analysis framework that rigorously links the decay of the Gram matrix eigenspectrum to the phenomenon of model collapse.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "8de6e401-12f3-44b8-a1ad-ba9d94696d83",
  "tool_use_result": {
    "query": "SIGMA scalable spectral insights LLM model collapse Track I Track II Gram matrix spectral norm arxiv 2601.03385 authors",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FypV6wopyxnikaE2y6ZHDM",
        "content": [
          {
            "title": "[2601.03385] SIGMA: Scalable Spectral Insights for LLM Model Collapse",
            "url": "https://arxiv.org/abs/2601.03385"
          },
          {
            "title": "SIGMA: Scalable Spectral Insights for LLM Model Collapse",
            "url": "https://www.arxiv.org/pdf/2601.03385"
          },
          {
            "title": "Sigma: Scalable Spectral Insights for LLM Model Collapse",
            "url": "https://arxiv.org/html/2601.03385"
          },
          {
            "title": "Sigma: Scalable Spectral Insights for LLM Collapse",
            "url": "https://arxiv.org/html/2601.03385v1"
          },
          {
            "title": "Rohan Paul on X: \"The authors measure LLM health by sampling embeddings and checking whether the meaning space keeps shrinking over training cycles. SIGMA spots LLM collapse early by measuring how much their sentence embedding space shrinks during self training. Recursive training on model https://t.co/ixJmA3N4y7\" / X",
            "url": "https://x.com/rohanpaul_ai/status/2011373977176846463/photo/1"
          },
          {
            "title": "[2601.11042v1] Spectral Characterization and Mitigation of Sequential Knowledge Editing Collapse",
            "url": "https://arxiv.org/abs/2601.11042v1"
          },
          {
            "title": "HyperSIGMA: Hyperspectral Intelligence Comprehension Foundation Model",
            "url": "https://arxiv.org/html/2406.11519v1"
          },
          {
            "title": "Has LLM Reached the Scaling Ceiling Yet? Unified Insights into LLM Regularities and Constraints",
            "url": "https://arxiv.org/html/2412.16443v1"
          },
          {
            "title": "arXiv:2506.23025v1 [cs.LG] 28 Jun 2025",
            "url": "https://arxiv.org/pdf/2506.23025"
          },
          {
            "title": "Controlled LLM Training on Spectral Sphere",
            "url": "https://arxiv.org/html/2601.08393"
          }
        ]
      },
      "I found the paper! Here's what I discovered:\n\n## SIGMA: Scalable Spectral Insights for LLM Model Collapse\n\n**arXiv**: 2601.03385 (submitted January 6, 2026; latest version March 23, 2026)\n\n**Authors**: Yi Gu, Lingyou Pang, Xiangkun Ye, Tianyu Wang, Jianyu Lin, Carey E. Priebe, and Alexander Aue\n\n### Overview\n\nSIGMA (Spectral Inequalities for Gram Matrix Analysis) is a unified framework that benchmarks model collapse through the spectral lens of the embedding Gram matrix. By deriving and utilizing deterministic and stochastic bounds on the matrix's spectrum, SIGMA provides a mathematically grounded metric to track the contraction of the representation space.\n\n### The Problem\n\nThe rapid adoption of synthetic data for training Large Language Models (LLMs) has introduced the technical challenge of \"model collapse\"—a degenerative process where recursive training on model-generated content leads to a contraction of distributional variance and representational quality.\n\n### Key Features\n\nThe method utilizes both deterministic and stochastic bounds to function effectively even with partially observed data, ensuring the framework remains scalable for large-scale models. SIGMA proposes a spectral analysis framework that rigorously links the decay of the Gram matrix eigenspectrum to the phenomenon of model collapse."
    ],
    "durationSeconds": 6.966683295000003
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-14T05:44:34.002Z_

<details><summary>↩ Tool result · `toolu_01VDY23sv2fobwqdUvbaq21b`</summary>

```text
Web search results for query: ""Can Generative Artificial Intelligence Survive Data Contamination" Wang 2602.16065 authors convergence rate universal approximator"

Links: [{"title":"[2602.16065] Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training","url":"https://arxiv.org/abs/2602.16065"},{"title":"Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training","url":"https://arxiv.org/html/2602.16065"},{"title":"Can Generative Artificial Intelligence Survive Data ...","url":"https://arxiv.org/pdf/2602.16065"},{"title":"Rethinking Data Protection in the (Generative) Artificial Intelligence Era","url":"https://arxiv.org/html/2507.03034v4"},{"title":"AI-generated data contamination erodes pathological variability and diagnostic reliability | alphaXiv","url":"https://www.alphaxiv.org/abs/2601.12946"},{"title":"Model collapse explained: How synthetic training data breaks AI","url":"https://www.techtarget.com/whatis/feature/Model-collapse-explained-How-synthetic-training-data-breaks-AI"},{"title":"Protecting AI From Training Data Contamination | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/11459343/"},{"title":"AI-generated data contamination erodes pathological variability and diagnostic reliability | medRxiv","url":"https://www.medrxiv.org/content/10.64898/2026.01.19.26344383v3"},{"title":"AI-generated data contamination erodes pathological variability and diagnostic reliability | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2601.12946"},{"title":"A Closer Look at the Existing Risks of Generative AI: Mapping the Who, What, and How of Real-World Incidents","url":"https://arxiv.org/html/2505.22073v2"}]

Based on the search results, I found the paper you're looking for:

The paper "Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training" is authored by Kevin Wang, Hongqian Niu, and Didong Li, with the arXiv identifier 2602.16065.

The authors are affiliated with the Department of Biostatistics, University of North Carolina at Chapel Hill.

The paper addresses a theoretical problem: As generative models are updated regularly, later models will inevitably be trained on mixtures of human-generated data and AI-generated data from earlier versions, creating a recursive training process with data contamination. 

Existing theoretical work has examined only highly simplified settings, where both the real data and the generative model are discrete or Gaussian, where it has been shown that such recursive training leads to model collapse. The paper extends this analysis to more complex and realistic settings.

You can access the full paper at https://arxiv.org/abs/2602.16065 to find detailed information about convergence rates, universal approximator properties, and the theoretical guarantees discussed in the paper.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "64472529-339b-4138-862d-7646db254e7e",
  "tool_use_result": {
    "query": "\"Can Generative Artificial Intelligence Survive Data Contamination\" Wang 2602.16065 authors convergence rate universal approximator",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HrhArXhyrQ6kYesPXPhEJ2",
        "content": [
          {
            "title": "[2602.16065] Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training",
            "url": "https://arxiv.org/abs/2602.16065"
          },
          {
            "title": "Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training",
            "url": "https://arxiv.org/html/2602.16065"
          },
          {
            "title": "Can Generative Artificial Intelligence Survive Data ...",
            "url": "https://arxiv.org/pdf/2602.16065"
          },
          {
            "title": "Rethinking Data Protection in the (Generative) Artificial Intelligence Era",
            "url": "https://arxiv.org/html/2507.03034v4"
          },
          {
            "title": "AI-generated data contamination erodes pathological variability and diagnostic reliability | alphaXiv",
            "url": "https://www.alphaxiv.org/abs/2601.12946"
          },
          {
            "title": "Model collapse explained: How synthetic training data breaks AI",
            "url": "https://www.techtarget.com/whatis/feature/Model-collapse-explained-How-synthetic-training-data-breaks-AI"
          },
          {
            "title": "Protecting AI From Training Data Contamination | IEEE Journals & Magazine | IEEE Xplore",
            "url": "https://ieeexplore.ieee.org/document/11459343/"
          },
          {
            "title": "AI-generated data contamination erodes pathological variability and diagnostic reliability | medRxiv",
            "url": "https://www.medrxiv.org/content/10.64898/2026.01.19.26344383v3"
          },
          {
            "title": "AI-generated data contamination erodes pathological variability and diagnostic reliability | Cool Papers - Immersive Paper Discovery",
            "url": "https://papers.cool/arxiv/2601.12946"
          },
          {
            "title": "A Closer Look at the Existing Risks of Generative AI: Mapping the Who, What, and How of Real-World Incidents",
            "url": "https://arxiv.org/html/2505.22073v2"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\nThe paper \"Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training\" is authored by Kevin Wang, Hongqian Niu, and Didong Li, with the arXiv identifier 2602.16065.\n\nThe authors are affiliated with the Department of Biostatistics, University of North Carolina at Chapel Hill.\n\nThe paper addresses a theoretical problem: As generative models are updated regularly, later models will inevitably be trained on mixtures of human-generated data and AI-generated data from earlier versions, creating a recursive training process with data contamination. \n\nExisting theoretical work has examined only highly simplified settings, where both the real data and the generative model are discrete or Gaussian, where it has been shown that such recursive training leads to model collapse. The paper extends this analysis to more complex and realistic settings.\n\nYou can access the full paper at https://arxiv.org/abs/2602.16065 to find detailed information about convergence rates, universal approximator properties, and the theoretical guarantees discussed in the paper."
    ],
    "durationSeconds": 6.375086218999997
  }
}
```

</details>

---

### Assistant

_source line 34_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough information to construct all 6 entries. Let me also get more details about the Truong & Truong paper authors and the SIGMA paper's Track I/II structure.

Let me also search for the exact author list of some papers I'm not sure about.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "7d825afc-22c5-455e-8adb-e8cfe1225712",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KZjBG8KNt2QVC1LREeoVgB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 506,
      "cache_creation_input_tokens": 2766,
      "cache_read_input_tokens": 40286,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2766
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

Now I have enough information to construct the entries. Let me also get specific details on SIGMA's Track I/II and Truong's universality classes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "78b38533-9ac6-4151-84ad-1cfbf1282732",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KZjBG8KNt2QVC1LREeoVgB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 506,
      "cache_creation_input_tokens": 2766,
      "cache_read_input_tokens": 40286,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2766
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_0123zSju1ettBQ5trcYFPRgQ`</summary>

```json
{
  "query": "arxiv 2601.03385 SIGMA \"Track I\" \"Track II\" spectral monitoring deterministic stochastic bounds eigenspectrum"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "edc9c74e-56c0-4800-b59d-504451a636d7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KZjBG8KNt2QVC1LREeoVgB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 506,
      "cache_creation_input_tokens": 2766,
      "cache_read_input_tokens": 40286,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2766
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

_source line 37_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ELEZUxj34BkRw4au3Ds348`</summary>

```json
{
  "query": "Truong Truong \"Entropy Collapse\" \"Class 1\" \"Class 2\" universality classes feedback amplification novelty regeneration 2512.12381"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "3945c9b8-e2e1-4597-913c-ea37f0cd58b0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KZjBG8KNt2QVC1LREeoVgB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 506,
      "cache_creation_input_tokens": 2766,
      "cache_read_input_tokens": 40286,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2766
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

_source line 38 · 2026-05-14T05:44:45.740Z_

<details><summary>↩ Tool result · `toolu_0123zSju1ettBQ5trcYFPRgQ`</summary>

```text
Web search results for query: "arxiv 2601.03385 SIGMA "Track I" "Track II" spectral monitoring deterministic stochastic bounds eigenspectrum"

Links: [{"title":"[2601.03385] SIGMA: Scalable Spectral Insights for LLM Model Collapse","url":"https://arxiv.org/abs/2601.03385"},{"title":"SIGMA: Scalable Spectral Insights for LLM Model Collapse","url":"https://www.arxiv.org/pdf/2601.03385"},{"title":"Sigma: Scalable Spectral Insights for LLM Model Collapse","url":"https://arxiv.org/html/2601.03385"},{"title":"Sigma: Scalable Spectral Insights for LLM Collapse","url":"https://arxiv.org/html/2601.03385v1"},{"title":"SIGMA-PPG: Statistical-prior Informed Generative Masking Architecture for PPG Foundation Model","url":"https://arxiv.org/html/2601.21031"},{"title":"[2601.00791] Geometry of Reason: Spectral Signatures of Valid Mathematical Reasoning","url":"https://arxiv.org/abs/2601.00791"},{"title":"The Short-spacing Interferometer Array for Global 21-cm Signal Detection (SIGMA): Design of the Antennas and Layout","url":"https://arxiv.org/html/2504.04955"},{"title":"[2601.11603] The use of spectral indices in environmental monitoring of smouldering coal-waste dumps","url":"https://arxiv.org/abs/2601.11603"},{"title":"HyperSIGMA: Hyperspectral Intelligence Comprehension Foundation Model","url":"https://arxiv.org/html/2406.11519v1"},{"title":"[2601.21031] SIGMA-PPG: Statistical-prior Informed Generative Masking Architecture for PPG Foundation Model","url":"https://arxiv.org/abs/2601.21031"}]

Based on my search for arxiv 2601.03385, I found the paper you're referring to. Here's what I discovered:

## SIGMA: Scalable Spectral Insights for LLM Model Collapse

SIGMA (Spectral Inequalities for Gram Matrix Analysis) is a unified framework that benchmarks model collapse through the spectral lens of the embedding Gram matrix.

### Key Methodology

The framework derives and utilizes deterministic and stochastic bounds on the matrix's spectrum to provide a mathematically grounded metric to track the contraction of the representation space. The stochastic formulation enables scalable estimation of these bounds, making the framework applicable to large-scale foundation models where full eigendecomposition is intractable.

### Track I and Track II Monitoring

The divergence between the conservative deterministic envelope (Track I) and the sensitive stochastic scaling metric (Track II) serves as a diagnostic signature for early-stage collapse, often preceding surface-level repetition artifacts.

### Eigenspectrum Analysis

The SIGMA framework focuses on representation geometry by tracking collapse via the eigenspectrum of embedding Gram matrices and developing deterministic and stochastic spectral inequalities that enable scalable, one-sided monitoring when only partial Gram information is available.

The paper was submitted on January 6, 2026, and was last revised on March 23, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "e85bb84c-959b-4111-a81d-8ffeaa545d33",
  "tool_use_result": {
    "query": "arxiv 2601.03385 SIGMA \"Track I\" \"Track II\" spectral monitoring deterministic stochastic bounds eigenspectrum",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BBmFymytKVg2UP4ehvfWoL",
        "content": [
          {
            "title": "[2601.03385] SIGMA: Scalable Spectral Insights for LLM Model Collapse",
            "url": "https://arxiv.org/abs/2601.03385"
          },
          {
            "title": "SIGMA: Scalable Spectral Insights for LLM Model Collapse",
            "url": "https://www.arxiv.org/pdf/2601.03385"
          },
          {
            "title": "Sigma: Scalable Spectral Insights for LLM Model Collapse",
            "url": "https://arxiv.org/html/2601.03385"
          },
          {
            "title": "Sigma: Scalable Spectral Insights for LLM Collapse",
            "url": "https://arxiv.org/html/2601.03385v1"
          },
          {
            "title": "SIGMA-PPG: Statistical-prior Informed Generative Masking Architecture for PPG Foundation Model",
            "url": "https://arxiv.org/html/2601.21031"
          },
          {
            "title": "[2601.00791] Geometry of Reason: Spectral Signatures of Valid Mathematical Reasoning",
            "url": "https://arxiv.org/abs/2601.00791"
          },
          {
            "title": "The Short-spacing Interferometer Array for Global 21-cm Signal Detection (SIGMA): Design of the Antennas and Layout",
            "url": "https://arxiv.org/html/2504.04955"
          },
          {
            "title": "[2601.11603] The use of spectral indices in environmental monitoring of smouldering coal-waste dumps",
            "url": "https://arxiv.org/abs/2601.11603"
          },
          {
            "title": "HyperSIGMA: Hyperspectral Intelligence Comprehension Foundation Model",
            "url": "https://arxiv.org/html/2406.11519v1"
          },
          {
            "title": "[2601.21031] SIGMA-PPG: Statistical-prior Informed Generative Masking Architecture for PPG Foundation Model",
            "url": "https://arxiv.org/abs/2601.21031"
          }
        ]
      },
      "Based on my search for arxiv 2601.03385, I found the paper you're referring to. Here's what I discovered:\n\n## SIGMA: Scalable Spectral Insights for LLM Model Collapse\n\nSIGMA (Spectral Inequalities for Gram Matrix Analysis) is a unified framework that benchmarks model collapse through the spectral lens of the embedding Gram matrix.\n\n### Key Methodology\n\nThe framework derives and utilizes deterministic and stochastic bounds on the matrix's spectrum to provide a mathematically grounded metric to track the contraction of the representation space. The stochastic formulation enables scalable estimation of these bounds, making the framework applicable to large-scale foundation models where full eigendecomposition is intractable.\n\n### Track I and Track II Monitoring\n\nThe divergence between the conservative deterministic envelope (Track I) and the sensitive stochastic scaling metric (Track II) serves as a diagnostic signature for early-stage collapse, often preceding surface-level repetition artifacts.\n\n### Eigenspectrum Analysis\n\nThe SIGMA framework focuses on representation geometry by tracking collapse via the eigenspectrum of embedding Gram matrices and developing deterministic and stochastic spectral inequalities that enable scalable, one-sided monitoring when only partial Gram information is available.\n\nThe paper was submitted on January 6, 2026, and was last revised on March 23, 2026."
    ],
    "durationSeconds": 6.4056201099999965
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-14T05:44:47.768Z_

<details><summary>↩ Tool result · `toolu_01ELEZUxj34BkRw4au3Ds348`</summary>

```text
Web search results for query: "Truong Truong "Entropy Collapse" "Class 1" "Class 2" universality classes feedback amplification novelty regeneration 2512.12381"

Links: [{"title":"[2512.12381] Entropy Collapse: A Universal Failure Mode of Intelligent Systems","url":"https://arxiv.org/abs/2512.12381"},{"title":"Entropy Collapse: A Universal Failure Mode of Intelligent Systems Exact Phase Transition Analysis, First-Order Discontinuity, and Two Universality Classes","url":"https://arxiv.org/html/2512.12381"},{"title":"Entropy Collapse: A Universal Failure Mode of Intelligent Systems","url":"https://arxiv.org/html/2512.12381v1"},{"title":"Entropy Collapse: A Universal Failure Mode of Intelligent Systems","url":"https://www.researchgate.net/publication/398720042_Entropy_Collapse_A_Universal_Failure_Mode_of_Intelligent_Systems"},{"title":"(PDF) Entropy Game Theory: Entropy-Conditioned Incentives, Threshold Collapse, and the Governance of Strategic Diversity","url":"https://www.researchgate.net/publication/398929807_Entropy_Game_Theory_Entropy-Conditioned_Incentives_Threshold_Collapse_and_the_Governance_of_Strategic_Diversity"},{"title":"Entropy Collapse: A Universal Failure Mode of Intelligent Systems | alphaXiv","url":"https://www.alphaxiv.org/overview/2512.12381v1"},{"title":"Entropy Collapse: A Universal Failure Mode of Intelligent Systems by Truong Xuan Khanh, Truong Quynh Hoa :: SSRN","url":"https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6084126"},{"title":"Clip-Low Increases Entropy and Clip-High Decreases Entropy in Reinforcement Learning of Large Language Models | OpenReview","url":"https://openreview.net/forum?id=2ZflH67Uof"},{"title":"Universality Classes and Information-Theoretic Measures of Complexity via Group Entropies | Scientific Reports","url":"https://www.nature.com/articles/s41598-020-60188-y"},{"title":"why model randomness (entropy) collapses during ...","url":"https://www.facebook.com/0xSojalSec/posts/why-model-randomness-entropy-collapses-during-reinforcement-learning-for-reasoni/1375333587454374/"}]

I found the paper! Here are the key findings from the research:

## "Entropy Collapse: A Universal Failure Mode of Intelligent Systems"

**Authors:** Truong Xuan Khanh and Truong Quynh Hoa from H&K Research Studio, Clevix LLC, Hanoi, Vietnam

**Main Contribution:** The research shows that feedback-amplified adaptive systems fail, and proves entropy collapse—the irreversible contraction of effective state space when feedback amplification alpha exceeds novelty regeneration beta—is a first-order (discontinuous) phase transition.

**Four Key Results:**

1. Exact threshold: alpha_c(beta) = 1/(1-beta), derived from the Jacobian spectrum of the Multiplicative-Weights operator

2. The entropy order parameter jumps by 0.698 at the critical point, with hysteresis between 2.73 and 3.9 nats, with no pre-transition warning

3. Relaxation exponent nu = 1, from transcritical bifurcation, showing universality across update mechanisms

4. **Two Universality Classes:** Class 1 (convex feedback, e.g., power-law) is irreversible with nu = 1; Class 2 (linear feedback) is reversible with nu = 1/2

**Applications:** The framework unifies AI model collapse, economic institutional sclerosis, and evolutionary genetic bottlenecks as first-order entropy-driven processes, evading standard early-warning monitoring.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "ada6a8d0-03c6-422e-ac47-5c2eea7f0f7c",
  "tool_use_result": {
    "query": "Truong Truong \"Entropy Collapse\" \"Class 1\" \"Class 2\" universality classes feedback amplification novelty regeneration 2512.12381",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RN22MXJ7SKdRTLxhtBrKhE",
        "content": [
          {
            "title": "[2512.12381] Entropy Collapse: A Universal Failure Mode of Intelligent Systems",
            "url": "https://arxiv.org/abs/2512.12381"
          },
          {
            "title": "Entropy Collapse: A Universal Failure Mode of Intelligent Systems Exact Phase Transition Analysis, First-Order Discontinuity, and Two Universality Classes",
            "url": "https://arxiv.org/html/2512.12381"
          },
          {
            "title": "Entropy Collapse: A Universal Failure Mode of Intelligent Systems",
            "url": "https://arxiv.org/html/2512.12381v1"
          },
          {
            "title": "Entropy Collapse: A Universal Failure Mode of Intelligent Systems",
            "url": "https://www.researchgate.net/publication/398720042_Entropy_Collapse_A_Universal_Failure_Mode_of_Intelligent_Systems"
          },
          {
            "title": "(PDF) Entropy Game Theory: Entropy-Conditioned Incentives, Threshold Collapse, and the Governance of Strategic Diversity",
            "url": "https://www.researchgate.net/publication/398929807_Entropy_Game_Theory_Entropy-Conditioned_Incentives_Threshold_Collapse_and_the_Governance_of_Strategic_Diversity"
          },
          {
            "title": "Entropy Collapse: A Universal Failure Mode of Intelligent Systems | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2512.12381v1"
          },
          {
            "title": "Entropy Collapse: A Universal Failure Mode of Intelligent Systems by Truong Xuan Khanh, Truong Quynh Hoa :: SSRN",
            "url": "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6084126"
          },
          {
            "title": "Clip-Low Increases Entropy and Clip-High Decreases Entropy in Reinforcement Learning of Large Language Models | OpenReview",
            "url": "https://openreview.net/forum?id=2ZflH67Uof"
          },
          {
            "title": "Universality Classes and Information-Theoretic Measures of Complexity via Group Entropies | Scientific Reports",
            "url": "https://www.nature.com/articles/s41598-020-60188-y"
          },
          {
            "title": "why model randomness (entropy) collapses during ...",
            "url": "https://www.facebook.com/0xSojalSec/posts/why-model-randomness-entropy-collapses-during-reinforcement-learning-for-reasoni/1375333587454374/"
          }
        ]
      },
      "I found the paper! Here are the key findings from the research:\n\n## \"Entropy Collapse: A Universal Failure Mode of Intelligent Systems\"\n\n**Authors:** Truong Xuan Khanh and Truong Quynh Hoa from H&K Research Studio, Clevix LLC, Hanoi, Vietnam\n\n**Main Contribution:** The research shows that feedback-amplified adaptive systems fail, and proves entropy collapse—the irreversible contraction of effective state space when feedback amplification alpha exceeds novelty regeneration beta—is a first-order (discontinuous) phase transition.\n\n**Four Key Results:**\n\n1. Exact threshold: alpha_c(beta) = 1/(1-beta), derived from the Jacobian spectrum of the Multiplicative-Weights operator\n\n2. The entropy order parameter jumps by 0.698 at the critical point, with hysteresis between 2.73 and 3.9 nats, with no pre-transition warning\n\n3. Relaxation exponent nu = 1, from transcritical bifurcation, showing universality across update mechanisms\n\n4. **Two Universality Classes:** Class 1 (convex feedback, e.g., power-law) is irreversible with nu = 1; Class 2 (linear feedback) is reversible with nu = 1/2\n\n**Applications:** The framework unifies AI model collapse, economic institutional sclerosis, and evolutionary genetic bottlenecks as first-order entropy-driven processes, evading standard early-warning monitoring."
    ],
    "durationSeconds": 7.4628917729999955
  }
}
```

</details>

---

### Assistant

_source line 40_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me construct the updated YAML. I need to:

1. Add 5 new entries (SIGMA, Truong & Truong, Fu et al., Kalinowski, Wang et al.)
2. Update the existing Bakshi & Chakraborty entry

Let me construct the full updated YAML content. I'll keep the existing entries intact and add the new ones in their appropriate sections.

For the Bakshi entry, I need to enrich it with:
- αt trajectory + nt scaling determines collapse/improvement/consistency conditions

Let me construct the YAML carefully.

Now let me prepare the full updated content. 

I need to be careful with YAML formatting as I update the Bakshi entry and add the new references.

Updating YAML structure... I'm organizing the literature map by adding these new entries to their respective sections—SIGMA and Kalinowski go into canary-metrics, Truong & Truong and Wang et al. into core-collapse, and Fu et al. into data-mixing, while updating Bakshi & Chakraborty with the new author. Now I need to save this through the project file tool, but I should verify that literature_map.yaml is actually writable since the tool description only lists memory.md, writing_plan.yaml, and paper_framing.md as writable files. I'm realizing the YAML file is quite extensive, so rather than trying to manually construct the entire thing, I should read it directly from disk first to preserve the exact formatting, then make targeted edits to the specific sections that need updating.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "2ba28074-7abe-43af-8b08-462fd126604d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qq8SZcCUTB1oMNTJjGv85v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2644,
      "cache_read_input_tokens": 43052,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2644
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

_source line 41_

Got all the details. Let me read the file from disk to make precise edits.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "cdfa73b8-0b2b-428c-9420-975a29bedaa7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qq8SZcCUTB1oMNTJjGv85v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2644,
      "cache_read_input_tokens": 43052,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2644
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

_source line 42_

<details open><summary>🔧 Tool call — Read · `toolu_01VRRa2pRFFbkwNCY6ZPKyaq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "12b5a119-a0e2-464f-82fd-800abc3de960",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qq8SZcCUTB1oMNTJjGv85v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2644,
      "cache_read_input_tokens": 43052,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2644
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

_source line 43 · 2026-05-14T05:45:15.036Z_

<details><summary>↩ Tool result · `toolu_01VRRa2pRFFbkwNCY6ZPKyaq`</summary>

```text
1	papers:
2	  # ============================================================
3	  # CORE MODEL COLLAPSE
4	  # ============================================================
5	  - id: "shumailov2024curse"
6	    title: "The Curse of Recursion: Training on Generated Data Makes Models Forget"
7	    authors: "Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Yarin Gal, Nicolas Papernot, Ross Anderson"
8	    venue: "Nature"
9	    year: 2024
10	    url: "https://arxiv.org/abs/2305.17493"
11	    category: "core-collapse"
12	    role: "foundation"
13	    key_findings:
14	      - "定义 model collapse 现象：迭代用合成数据替换真实数据训练会导致分布尾部消失"
15	      - "区分 early model collapse（尾部信息丢失）和 late model collapse（分布完全收敛）"
16	      - "三类误差来源：statistical approximation, functional expressivity, functional approximation，跨代复合"
17	      - "在 VAE、GMM、LLM 上均验证了 collapse 的普遍性"
18	    relevance_to_us: "奠基论文，定义了我们研究的核心现象。我们的 canary 指标旨在提前检测其描述的 early collapse 阶段"
19	    metrics_studied: ["perplexity", "distributional tail mass"]
20	
21	  - id: "alemohammad2024mad"
22	    title: "Self-Consuming Generative Models Go MAD"
23	    authors: "Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, Richard Baraniuk"
24	    venue: "ICLR 2024"
25	    year: 2024
26	    url: "https://arxiv.org/abs/2307.01850"
27	    category: "core-collapse"
28	    role: "foundation"
29	    key_findings:
30	      - "提出 Model Autophagy Disorder (MAD) 概念"
31	      - "autophagous loop 中没有足够新鲜真实数据时，质量或多样性必然渐进下降"
32	      - "在图像生成领域验证 self-consuming loop 的退化效应"
33	    relevance_to_us: "MAD 框架与我们的 iterative loop 设置直接对应；其 quality vs diversity tradeoff 可能反映在不同 canary 指标上"
34	    metrics_studied: ["FID", "precision", "recall", "diversity"]
35	
36	  - id: "dohmatob2024tale"
37	    title: "A Tale of Tails: Model Collapse as a Change of Scaling Laws"
38	    authors: "Elvis Dohmatob, Yunzhen Feng, et al."
39	    venue: "ICML 2024"
40	    year: 2024
41	    url: "https://arxiv.org/abs/2402.07043"
42	    category: "core-collapse"
43	    role: "foundation"
44	    key_findings:
45	      - "通过 scaling laws 视角分析 model collapse：collapse 表现为 scaling law 的变化"
46	      - "发现 loss of scaling, shifted scaling, skill un-learning, grokking 等多种退化模式"
47	      - "混入少量干净数据可缓解 collapse 并引发 grokking 现象"
48	      - "在 transformer 算术任务和 Llama2 文本生成上验证"
49	    relevance_to_us: "scaling law 变化视角为我们提供了理论基础；grokking 现象暗示 canary 指标可能出现非单调行为"
50	    metrics_studied: ["test loss", "scaling exponents"]
51	
52	  - id: "dohmatob2025strong"
53	    title: "Strong Model Collapse"
54	    authors: "Elvis Dohmatob, Yunzhen Feng, Arjun Subramonian, Julia Kempe"
55	    venue: "ICLR 2025 (Spotlight)"
56	    year: 2025
57	    url: "https://arxiv.org/abs/2410.04840"
58	    category: "core-collapse"
59	    role: "foundation"
60	    key_findings:
61	      - "即使合成数据占比极小（1/1000），仍可导致 model collapse"
62	      - "更大的训练集并不能避免 collapse"
63	      - "更大的模型（random projection 近似下）反而可能放大 collapse"
64	      - "存在 interpolation threshold 的 double-descent 现象"
65	    relevance_to_us: "强化了早期检测的必要性——即使极小的合成数据比例也能触发 collapse，因此 canary 指标必须敏感"
66	    metrics_studied: ["test loss", "population risk"]
67	
68	  - id: "guo2024linguistic"
69	    title: "The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text"
70	    authors: "Yanzhu Guo, Guokan Shang, et al."
71	    venue: "NAACL 2024 Findings"
72	    year: 2024
73	    url: "https://arxiv.org/abs/2311.09807"
74	    category: "core-collapse"
75	    role: "evaluation"
76	    key_findings:
77	      - "递归微调中，linguistic diversity 在连续迭代中持续下降"
78	      - "创造性任务中 diversity 下降最显著"
79	      - "开发了覆盖 lexical、syntactic、semantic 三层的 diversity 指标体系"
80	    relevance_to_us: "其多层 diversity 指标体系可直接作为我们 canary 指标的候选集；创造性 vs 事实任务的差异可能影响 canary 灵敏度"
81	    metrics_studied: ["distinct-n", "type-token ratio", "syntactic diversity", "semantic diversity"]
82	
83	  - id: "briesch2024selfconsuming"
84	    title: "Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop"
85	    authors: "Martin Briesch, Dominik Sobania, Franz Rothlauf"
86	    venue: "arXiv (2311.16822)"
87	    year: 2024
88	    url: "https://arxiv.org/abs/2311.16822"
89	    category: "core-collapse"
90	    role: "direct-competitor"
91	    key_findings:
92	      - "首次系统研究 LLM 的 self-consuming training loop"
93	      - "full synthetic cycle（完全替换）导致单点 collapse；data augmentation cycle 导致 diversity 缓慢下降"
94	      - "expanding data cycle（累积）在 50 代内保持 diversity"
95	    relevance_to_us: "其不同 data cycle 策略的对比直接对应我们的 alpha（synthetic ratio）实验设置"
96	    metrics_studied: ["diversity", "quality"]
97	
98	  # ============================================================
99	  # CANARY / EARLY WARNING METRICS
100	  # ============================================================
101	  - id: "chen2025scales"
102	    title: "Characterizing Model Behavior Under Synthetic Data Training: An Empirical Study Across Scales and Mixing Ratios"
103	    authors: "Anonymous"
104	    venue: "arXiv (2510.05133)"
105	    year: 2025
106	    url: "https://arxiv.org/abs/2510.05133"
107	    category: "canary-metrics"
108	    role: "direct-competitor"
109	    key_findings:
110	      - "**Calibration degradation precedes accuracy loss** — ECE 是 collapse 的 early warning signal"
111	      - "20% synthetic data 以下性能稳定，30% 以上退化加速"
112	      - "大模型（6.9B-12B）比小模型（410M-1.4B）更鲁棒"
113	      - "推理任务比检索任务更易退化"
114	      - "iteration 1 + 30% synthetic 时 ECE 从 0.08 升至 0.14（+75%）"
115	    relevance_to_us: "**最直接的竞争者/先驱**。证实 ECE 可作为 canary，但未做 lead-lag 分析，未建立多指标 panel 框架"
116	    metrics_studied: ["ECE", "accuracy", "perplexity"]
117	
118	  - id: "gambetta2024surplexity"
119	    title: "Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI"
120	    authors: "Daniele Gambetta et al."
121	    venue: "arXiv (2410.12341)"
122	    year: 2024
123	    url: "https://arxiv.org/abs/2410.12341"
124	    category: "canary-metrics"
125	    role: "direct-competitor"
126	    key_findings:
127	      - "提出 surplexity（model surprise 度量）同时用于检测 collapse 和过滤训练数据"
128	      - "用 semantic networks 分析文本重复性和语义多样性"
129	      - "用 next-token probability 定量衡量 diversity loss"
130	      - "高 surplexity 过滤策略至少与 human-data baseline 同效，且更能降低分布偏斜"
131	      - "不需要区分 human vs AI-generated data"
132	    relevance_to_us: "surplexity 可作为我们 canary 指标候选之一；其 semantic network 方法提供了 diversity 度量的另一视角"
133	    metrics_studied: ["surplexity", "semantic network metrics", "next-token probability"]
134	
135	  - id: "qiu2025spectral"
136	    title: "Spectral Alignment as Predictor of Loss Explosion in Neural Network Training"
137	    authors: "Haiquan Qiu, You Wu, Yingjie Tan, Yaqing Wang, Quanming Yao"
138	    venue: "arXiv (2510.04202)"
139	    year: 2025
140	    url: "https://arxiv.org/abs/2510.04202"
141	    category: "canary-metrics"
142	    role: "method-component"
143	    key_findings:
144	      - "Spectral Alignment (SA) 监控层输入与权重矩阵主奇异向量的分布对齐"
145	      - "SA sign diversity collapse 是 representational collapse 和训练发散的早期预测器"
146	      - "比 weight norm、gradient norm 等传统指标更早、更清晰地检测到训练失败"
147	      - "健康层的 SA 应有正负均衡分布，collapse 到单侧则预示不稳定"
148	    relevance_to_us: "SA 是潜在的高价值 canary 指标——专门设计为 early warning，可直接纳入我们的指标 panel"
149	    metrics_studied: ["spectral alignment", "weight norm", "gradient norm"]
150	
151	  - id: "he2025closer"
152	    title: "A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective"
153	    authors: "Shiliang He et al."
154	    venue: "NeurIPS 2025 (Spotlight)"
155	    year: 2025
156	    url: "https://arxiv.org/abs/2509.16499"
157	    category: "canary-metrics"
158	    role: "direct-competitor"
159	    key_findings:
160	      - "识别 diffusion model collapse 中的 generalization → memorization 转变"
161	      - "**训练数据的 entropy 递减是 collapse 的直接驱动因素和清晰指标**"
162	      - "提出基于 entropy 的数据选择策略，有效缓解 collapse"
163	    relevance_to_us: "data entropy 作为 canary 的有效性已被验证（diffusion domain）；需测试是否在 LLM 场景同样有效"
164	    metrics_studied: ["entropy", "FID", "diversity"]
165	
166	  - id: "ba2024fill"
167	    title: "Fill In The Gaps: Model Calibration and Generalization with Synthetic Data"
168	    authors: "Yang Ba, Michelle V Mancenido, Rong Pan"
169	    venue: "EMNLP 2024"
170	    year: 2024
171	    url: "https://arxiv.org/abs/2410.10864"
172	    category: "canary-metrics"
173	    role: "background"
174	    key_findings:
175	      - "用 LLM 生成合成数据来修复 calibration 错误的 reliability diagram bins"
176	      - "推导了基于 PAC 框架的 ECE bound"
177	      - "合成数据可改善 calibration 但需精心设计生成策略"
178	    relevance_to_us: "ECE 的理论 bound 可为我们的 canary 阈值设定提供理论依据"
179	    metrics_studied: ["ECE", "accuracy"]
180	
181	  # ============================================================
182	  # DIVERSITY METRICS (BACKGROUND)
183	  # ============================================================
184	  - id: "zhu2018texygen"
185	    title: "Texygen: A Benchmarking Platform for Text Generation Models"
186	    authors: "Yaoming Zhu et al."
187	    venue: "SIGIR 2018"
188	    year: 2018
189	    url: "https://arxiv.org/abs/1802.01886"
190	    category: "canary-metrics"
191	    role: "background"
192	    key_findings:
193	      - "提出 Self-BLEU 度量：计算生成句子间的 BLEU 相似度，Self-BLEU 越高多样性越低"
194	      - "成为文本生成多样性评估的标准基准之一"
195	    relevance_to_us: "Self-BLEU 是我们 diversity canary 的经典候选"
196	    metrics_studied: ["Self-BLEU", "BLEU"]
197	
198	  - id: "li2016diversity"
199	    title: "A Diversity-Promoting Objective Function for Neural Conversation Models"
200	    authors: "Jiwei Li et al."
201	    venue: "NAACL 2016"
202	    year: 2016
203	    url: "https://arxiv.org/abs/1510.03055"
204	    category: "canary-metrics"
205	    role: "background"
206	    key_findings:
207	      - "提出 distinct-1 / distinct-2 指标衡量生成文本的 n-gram 多样性"
208	      - "计算 unique n-gram 数占总 n-gram 数的比例"
209	    relevance_to_us: "distinct-n 是最廉价的 diversity canary 之一，计算开销极低"
210	    metrics_studied: ["distinct-1", "distinct-2"]
211	
212	  # ============================================================
213	  # REPRESENTATION / SPECTRAL COLLAPSE
214	  # ============================================================
215	  - id: "jing2022understanding"
216	    title: "Understanding Dimensional Collapse in Contrastive Self-supervised Learning"
217	    authors: "Li Jing et al."
218	    venue: "ICLR 2022"
219	    year: 2022
220	    url: "https://openreview.net/forum?id=YevsQ05DEN7"
221	    category: "canary-metrics"
222	    role: "method-component"
223	    key_findings:
224	      - "定义 dimensional collapse：embedding 向量只跨越低维子空间"
225	      - "effective rank（基于归一化特征值 entropy 的指数）作为 collapse 度量"
226	      - "strong augmentation 和 implicit regularization 驱动低秩解"
227	    relevance_to_us: "effective rank 的定义和计算方式可直接迁移到我们的 embedding 空间监控"
228	    metrics_studied: ["effective rank", "singular value spectrum"]
229	
230	  - id: "noci2024mind"
231	    title: "Mind the Gap: A Spectral Analysis of Rank Collapse and Signal Propagation in Transformers"
232	    authors: "Lorenzo Noci et al."
233	    venue: "NeurIPS 2024"
234	    year: 2024
235	    url: "https://arxiv.org/abs/2410.07799"
236	    category: "canary-metrics"
237	    role: "method-component"
238	    key_findings:
239	      - "用 Random Matrix Theory 分析 attention 层的 rank collapse"
240	      - "发现 attention matrix 最大两个奇异值之间的 spectral gap 是 width-collapse 的根因"
241	      - "rank collapse in depth: 所有 token 沿层收敛到单一表示"
242	    relevance_to_us: "spectral gap 作为另一种 spectral canary 候选；其 RMT 分析框架可启发我们的理论工作"
243	    metrics_studied: ["spectral gap", "singular values", "effective rank"]
244	
245	  # ============================================================
246	  # DATA MIXING & ACCUMULATION
247	  # ============================================================
248	  - id: "kazdan2025collapse"
249	    title: "Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World"
250	    authors: "Joshua Kazdan, Rylan Schaeffer, Apratim Dey, Matthias Gerstgrasser, Rafael Rafailov, David L. Donoho, Sanmi Koyejo"
251	    venue: "ICML 2025"
252	    year: 2025
253	    url: "https://arxiv.org/abs/2410.16713"
254	    category: "data-mixing"
255	    role: "foundation"
256	    key_findings:
257	      - "系统对比 replace vs accumulate 场景"
258	      - "replace → collapse；accumulate → 可避免 collapse"
259	      - "发现 real data 和 synthetic data 之间存在非平凡的交互效应"
260	      - "synthetic data 的价值取决于 real data 的绝对数量"
261	    relevance_to_us: "直接对应我们的 alpha（mixing ratio）实验维度；其 replace vs accumulate 框架是我们实验设计的重要参考"
262	    metrics_studied: ["test loss"]
263	
264	  - id: "dey2024breaking"
265	    title: "Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data"
266	    authors: "Apratim Dey, David Donoho, et al."
267	    venue: "ICML 2024"
268	    year: 2024
269	    url: "https://arxiv.org/abs/2404.01413"
270	    category: "data-mixing"
271	    role: "foundation"
272	    key_findings:
273	      - "替换数据 → 发散 population risk；累积数据 → 避免发散"
274	      - "证明累积策略在多种模型（GMM, HMM, LLM）上有效"
275	    relevance_to_us: "为我们的 alpha 实验提供理论预测：累积 vs 替换是 collapse 速率的关键调节因子"
276	    metrics_studied: ["population risk"]
277	
278	  - id: "epstein2024howbad"
279	    title: "How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse"
280	    authors: "Mohamed El Amine Epstein et al."
281	    venue: "arXiv (2404.05090)"
282	    year: 2024
283	    url: "https://arxiv.org/abs/2404.05090"
284	    category: "data-mixing"
285	    role: "background"
286	    key_findings:
287	      - "纯合成数据训练不可避免 collapse"
288	      - "给出 synthetic data 比例上界的估计——低于此比例可避免 collapse"
289	      - "递归训练使原始分布尾部消失"
290	    relevance_to_us: "其 mixing ratio 上界估计可对比我们实验中观测到的 canary 触发阈值"
291	    metrics_studied: ["perplexity"]
292	
293	  - id: "bakshi2026improvement"
294	    title: "From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources"
295	    authors: "Soham Bakshi et al."
296	    venue: "arXiv (2602.10531)"
297	    year: 2026
298	    url: "https://arxiv.org/abs/2602.10531"
299	    category: "data-mixing"
300	    role: "background"
301	    key_findings:
302	      - "即使真实数据比例随时间衰减，只要非零就可能避免 collapse 并恢复真实分布"
303	      - "在 next-token prediction 语言模型上分析混合训练的动态"
304	    relevance_to_us: "提供了 decaying real data fraction 的理论保证，与我们的实验中 alpha 变化场景相关"
305	    metrics_studied: ["population risk"]
306	
307	  # ============================================================
308	  # MITIGATION & VERIFICATION
309	  # ============================================================
310	  - id: "feng2025escaping"
311	    title: "Escaping Model Collapse via Synthetic Data Verification"
312	    authors: "Yunzhen Feng et al."
313	    venue: "NeurIPS 2025"
314	    year: 2025
315	    url: "https://arxiv.org/abs/2510.16657"
316	    category: "data-mixing"
317	    role: "background"
318	    key_findings:
319	      - "通过外部 verifier（human 或 better model）注入信息可避免 collapse"
320	      - "verifier-guided retraining 带来短期改善，但最终收敛到 verifier 的 knowledge center"
321	      - "除非 verifier 完全可靠，早期收益会 plateau 甚至逆转"
322	    relevance_to_us: "verification 作为 intervention 策略——如果 canary 触发，可考虑此类 reactive intervention"
323	    metrics_studied: ["test loss"]
324	
325	  - id: "barzilai2025consistency"
326	    title: "When Models Don't Collapse: On the Consistency of Iterative MLE"
327	    authors: "Daniel Barzilai, Ohad Shamir"
328	    venue: "ICML 2025"
329	    year: 2025
330	    url: "https://arxiv.org/abs/2505.19046"
331	    category: "core-collapse"
332	    role: "background"
333	    key_findings:
334	      - "在标准 MLE 一致性假设下，即使 real data fraction 趋近零也可避免 collapse"
335	      - "但证明了某些情况下 collapse 可以任意快地发生——首次给出严格 collapse 反例"
336	    relevance_to_us: "理论上的 collapse 可发生任意快的结论强化了 early warning 的价值"
337	    metrics_studied: []
338	
339	  - id: "dces2026counter"
340	    title: "Countering Model Collapse in Iterative Self-Training via Dynamic Center-Edge Sampling"
341	    authors: "Anonymous"
342	    venue: "MDPI Electronics (2026)"
343	    year: 2026
344	    url: "https://www.mdpi.com/2079-9292/15/4/869"
345	    category: "data-mixing"
346	    role: "background"
347	    key_findings:
348	      - "提出 DCES（dynamic center-edge sampling）数据选择框架"
349	      - "DCES 在 ECE（0.1058 vs 0.1200）和 entropy 保持上优于随机选择"
350	    relevance_to_us: "其 ECE 和 entropy 对比数据为我们的指标 baseline 提供参考"
351	    metrics_studied: ["ECE", "entropy"]
352	
353	  # ============================================================
354	  # POSITION / SURVEY / EPISTEMICS
355	  # ============================================================
356	  - id: "schaeffer2025position"
357	    title: "Position: Model Collapse Does Not Mean What You Think"
358	    authors: "Rylan Schaeffer, Joshua Kazdan, Alvan Caleb Arulandu, Sanmi Koyejo"
359	    venue: "arXiv (2503.03150)"
360	    year: 2025
361	    url: "https://arxiv.org/abs/2503.03150"
362	    category: "core-collapse"
363	    role: "background"
364	    key_findings:
365	      - "文献中实际包含 8 种不同且有时矛盾的 model collapse 定义"
366	      - "许多 collapse 预测依赖于与现实不符的假设"
367	      - "多种 collapse 场景是可以轻易避免的"
368	    relevance_to_us: "提醒我们明确定义 collapse 的操作标准；不同定义可能需要不同的 canary 指标"
369	    metrics_studied: []
370	
371	  - id: "wang2025epistemic"
372	    title: "Epistemic Diversity and Knowledge Collapse in Large Language Models"
373	    authors: "Wang et al."
374	    venue: "arXiv (2510.04226)"
375	    year: 2025
376	    url: "https://arxiv.org/abs/2510.04226"
377	    category: "core-collapse"
378	    role: "background"
379	    key_findings:
380	      - "27 个 LLM 在 155 个主题上的 epistemic diversity 评估"
381	      - "所有模型的 epistemic diversity 低于基本 web 搜索"
382	      - "模型越大 epistemic diversity 反而越低；RAG 有正面效果"
383	    relevance_to_us: "knowledge collapse 维度可扩展我们对 diversity canary 的理解——不仅是 lexical/syntactic 还有 epistemic"
384	    metrics_studied: ["epistemic diversity"]
385	
386	  # ============================================================
387	  # METHODOLOGY (GRANGER / LEAD-LAG)
388	  # ============================================================
389	  - id: "shojaie2022granger"
390	    title: "Granger Causality: A Review and Recent Advances"
391	    authors: "Ali Shojaie, Emily B. Fox"
392	    venue: "Annual Review of Statistics and Its Application"
393	    year: 2022
394	    url: "https://arxiv.org/abs/2105.02675"
395	    category: "methodology"
396	    role: "method-component"
397	    key_findings:
398	      - "Granger causality 综述：从经典线性到非线性/neural 方法"
399	      - "Panel data 场景的 Granger causality 扩展"
400	      - "VAR 和 neural Granger causality 的对比"
401	    relevance_to_us: "为我们的 panel Granger causality 分析提供方法论基础"
402	    metrics_studied: []
403	
404	  - id: "marcinkevics2022neural"
405	    title: "Granger Causality Using Neural Networks"
406	    authors: "Raphael Marcinkevics, Julia Vogt"
407	    venue: "arXiv (2208.03703)"
408	    year: 2022
409	    url: "https://arxiv.org/abs/2208.03703"
410	    category: "methodology"
411	    role: "method-component"
412	    key_findings:
413	      - "用 neural network 估计 Granger causality，突破线性假设"
414	      - "两个模型对比法：含/不含外生变量的预测误差差异即 Granger causality 证据"
415	    relevance_to_us: "我们的多指标时序可能存在非线性关系，neural Granger causality 是自然选择"
416	    metrics_studied: []
417	
418	gaps:
419	  - "无人系统做过 canary 指标的 lead-lag / Granger causality 分析——现有工作只在事后观察到指标变化，未量化哪些指标能提前多少步预测 collapse"
420	  - "ECE 在 collapse 场景下几乎未被系统研究——chen2025scales 是唯一报告 ECE 先于 accuracy 退化的工作，但未做因果分析"
421	  - "embedding effective rank 未在 iterative synthetic training 场景下被测试——仅在 contrastive learning/transformer 训练中研究过"
422	  - "多指标 panel 框架缺失——无人同时追踪 ECE + effective rank + diversity + perplexity 的时序行为并分析其 lead-lag 关系"
423	  - "alpha（synthetic ratio）对 canary 灵敏度的影响未被研究——现有工作只关注 alpha 对最终性能的影响，不关注 canary 的 lead time 如何随 alpha 变化"
424	  - "predictive intervention vs reactive intervention 缺少对比——没有工作量化 early warning 带来的实际干预收益"
425	  - "surplexity 和 spectral alignment 未在 iterative collapse 场景下交叉验证"
426	  - "跨任务 canary 普适性未知——reasoning vs retrieval vs creative tasks 中哪些 canary 更可靠"
427	
428	novelty_assessment: |
429	  我们项目的核心 novelty 在于：
430	
431	  1. **Panel Granger Causality 框架**：首次将多指标时序数据的因果分析方法应用于 model collapse 早期预警。
432	     现有工作（chen2025scales, gambetta2024surplexity）只是事后观察到某些指标先变化，
433	     但没有人做过系统的 lead-lag 量化分析。
434	
435	  2. **多指标 Canary Panel**：同时追踪 ECE、effective rank、Self-BLEU/distinct-n、
436	     perplexity、entropy、surplexity 等指标，分析其相互关系和各自的 lead time。
437	     现有工作都是单一指标或最多两三个指标的孤立分析。
438	
439	  3. **alpha-dependent Canary Sensitivity**：系统研究 synthetic ratio 如何影响各 canary
440	     指标的灵敏度和 lead time。dohmatob2025strong 证明极小的 alpha 就能触发 collapse，
441	     但没人研究 canary 在不同 alpha 下的行为。
442	
443	  4. **与已有工作的差异**：
444	     - vs chen2025scales: 他们发现 ECE 先退化但没有做因果分析；我们用 Granger causality 量化
445	     - vs gambetta2024surplexity: 他们提出 surplexity 用于检测和缓解 collapse；
446	       我们将其纳入更广的 panel 并研究其 lead-lag 特性
447	     - vs he2025closer: 他们在 diffusion 中用 entropy 作为指标；我们在 LLM 中测试更多指标
448	     - vs qiu2025spectral: 他们的 SA 用于训练 loss explosion 预警；
449	       我们将类似思路迁移到 iterative collapse 场景
450	
451	  5. **潜在风险**：chen2025scales 已经非常接近我们的方向。如果他们扩展到 lead-lag 分析，
452	     我们的 novelty 会被削弱。需要快速推进并在方法论（Granger causality）上建立壁垒。
453	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "2a116353-533a-4fe4-bea6-2445b0b09e06",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/literature_map.yaml",
      "content": "papers:\n  # ============================================================\n  # CORE MODEL COLLAPSE\n  # ============================================================\n  - id: \"shumailov2024curse\"\n    title: \"The Curse of Recursion: Training on Generated Data Makes Models Forget\"\n    authors: \"Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Yarin Gal, Nicolas Papernot, Ross Anderson\"\n    venue: \"Nature\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2305.17493\"\n    category: \"core-collapse\"\n    role: \"foundation\"\n    key_findings:\n      - \"定义 model collapse 现象：迭代用合成数据替换真实数据训练会导致分布尾部消失\"\n      - \"区分 early model collapse（尾部信息丢失）和 late model collapse（分布完全收敛）\"\n      - \"三类误差来源：statistical approximation, functional expressivity, functional approximation，跨代复合\"\n      - \"在 VAE、GMM、LLM 上均验证了 collapse 的普遍性\"\n    relevance_to_us: \"奠基论文，定义了我们研究的核心现象。我们的 canary 指标旨在提前检测其描述的 early collapse 阶段\"\n    metrics_studied: [\"perplexity\", \"distributional tail mass\"]\n\n  - id: \"alemohammad2024mad\"\n    title: \"Self-Consuming Generative Models Go MAD\"\n    authors: \"Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, Richard Baraniuk\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2307.01850\"\n    category: \"core-collapse\"\n    role: \"foundation\"\n    key_findings:\n      - \"提出 Model Autophagy Disorder (MAD) 概念\"\n      - \"autophagous loop 中没有足够新鲜真实数据时，质量或多样性必然渐进下降\"\n      - \"在图像生成领域验证 self-consuming loop 的退化效应\"\n    relevance_to_us: \"MAD 框架与我们的 iterative loop 设置直接对应；其 quality vs diversity tradeoff 可能反映在不同 canary 指标上\"\n    metrics_studied: [\"FID\", \"precision\", \"recall\", \"diversity\"]\n\n  - id: \"dohmatob2024tale\"\n    title: \"A Tale of Tails: Model Collapse as a Change of Scaling Laws\"\n    authors: \"Elvis Dohmatob, Yunzhen Feng, et al.\"\n    venue: \"ICML 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2402.07043\"\n    category: \"core-collapse\"\n    role: \"foundation\"\n    key_findings:\n      - \"通过 scaling laws 视角分析 model collapse：collapse 表现为 scaling law 的变化\"\n      - \"发现 loss of scaling, shifted scaling, skill un-learning, grokking 等多种退化模式\"\n      - \"混入少量干净数据可缓解 collapse 并引发 grokking 现象\"\n      - \"在 transformer 算术任务和 Llama2 文本生成上验证\"\n    relevance_to_us: \"scaling law 变化视角为我们提供了理论基础；grokking 现象暗示 canary 指标可能出现非单调行为\"\n    metrics_studied: [\"test loss\", \"scaling exponents\"]\n\n  - id: \"dohmatob2025strong\"\n    title: \"Strong Model Collapse\"\n    authors: \"Elvis Dohmatob, Yunzhen Feng, Arjun Subramonian, Julia Kempe\"\n    venue: \"ICLR 2025 (Spotlight)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2410.04840\"\n    category: \"core-collapse\"\n    role: \"foundation\"\n    key_findings:\n      - \"即使合成数据占比极小（1/1000），仍可导致 model collapse\"\n      - \"更大的训练集并不能避免 collapse\"\n      - \"更大的模型（random projection 近似下）反而可能放大 collapse\"\n      - \"存在 interpolation threshold 的 double-descent 现象\"\n    relevance_to_us: \"强化了早期检测的必要性——即使极小的合成数据比例也能触发 collapse，因此 canary 指标必须敏感\"\n    metrics_studied: [\"test loss\", \"population risk\"]\n\n  - id: \"guo2024linguistic\"\n    title: \"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\"\n    authors: \"Yanzhu Guo, Guokan Shang, et al.\"\n    venue: \"NAACL 2024 Findings\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2311.09807\"\n    category: \"core-collapse\"\n    role: \"evaluation\"\n    key_findings:\n      - \"递归微调中，linguistic diversity 在连续迭代中持续下降\"\n      - \"创造性任务中 diversity 下降最显著\"\n      - \"开发了覆盖 lexical、syntactic、semantic 三层的 diversity 指标体系\"\n    relevance_to_us: \"其多层 diversity 指标体系可直接作为我们 canary 指标的候选集；创造性 vs 事实任务的差异可能影响 canary 灵敏度\"\n    metrics_studied: [\"distinct-n\", \"type-token ratio\", \"syntactic diversity\", \"semantic diversity\"]\n\n  - id: \"briesch2024selfconsuming\"\n    title: \"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop\"\n    authors: \"Martin Briesch, Dominik Sobania, Franz Rothlauf\"\n    venue: \"arXiv (2311.16822)\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2311.16822\"\n    category: \"core-collapse\"\n    role: \"direct-competitor\"\n    key_findings:\n      - \"首次系统研究 LLM 的 self-consuming training loop\"\n      - \"full synthetic cycle（完全替换）导致单点 collapse；data augmentation cycle 导致 diversity 缓慢下降\"\n      - \"expanding data cycle（累积）在 50 代内保持 diversity\"\n    relevance_to_us: \"其不同 data cycle 策略的对比直接对应我们的 alpha（synthetic ratio）实验设置\"\n    metrics_studied: [\"diversity\", \"quality\"]\n\n  # ============================================================\n  # CANARY / EARLY WARNING METRICS\n  # ============================================================\n  - id: \"chen2025scales\"\n    title: \"Characterizing Model Behavior Under Synthetic Data Training: An Empirical Study Across Scales and Mixing Ratios\"\n    authors: \"Anonymous\"\n    venue: \"arXiv (2510.05133)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.05133\"\n    category: \"canary-metrics\"\n    role: \"direct-competitor\"\n    key_findings:\n      - \"**Calibration degradation precedes accuracy loss** — ECE 是 collapse 的 early warning signal\"\n      - \"20% synthetic data 以下性能稳定，30% 以上退化加速\"\n      - \"大模型（6.9B-12B）比小模型（410M-1.4B）更鲁棒\"\n      - \"推理任务比检索任务更易退化\"\n      - \"iteration 1 + 30% synthetic 时 ECE 从 0.08 升至 0.14（+75%）\"\n    relevance_to_us: \"**最直接的竞争者/先驱**。证实 ECE 可作为 canary，但未做 lead-lag 分析，未建立多指标 panel 框架\"\n    metrics_studied: [\"ECE\", \"accuracy\", \"perplexity\"]\n\n  - id: \"gambetta2024surplexity\"\n    title: \"Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI\"\n    authors: \"Daniele Gambetta et al.\"\n    venue: \"arXiv (2410.12341)\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2410.12341\"\n    category: \"canary-metrics\"\n    role: \"direct-competitor\"\n    key_findings:\n      - \"提出 surplexity（model surprise 度量）同时用于检测 collapse 和过滤训练数据\"\n      - \"用 semantic networks 分析文本重复性和语义多样性\"\n      - \"用 next-token probability 定量衡量 diversity loss\"\n      - \"高 surplexity 过滤策略至少与 human-data baseline 同效，且更能降低分布偏斜\"\n      - \"不需要区分 human vs AI-generated data\"\n    relevance_to_us: \"surplexity 可作为我们 canary 指标候选之一；其 semantic network 方法提供了 diversity 度量的另一视角\"\n    metrics_studied: [\"surplexity\", \"semantic network metrics\", \"next-token probability\"]\n\n  - id: \"qiu2025spectral\"\n    title: \"Spectral Alignment as Predictor of Loss Explosion in Neural Network Training\"\n    authors: \"Haiquan Qiu, You Wu, Yingjie Tan, Yaqing Wang, Quanming Yao\"\n    venue: \"arXiv (2510.04202)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.04202\"\n    category: \"canary-metrics\"\n    role: \"method-component\"\n    key_findings:\n      - \"Spectral Alignment (SA) 监控层输入与权重矩阵主奇异向量的分布对齐\"\n      - \"SA sign diversity collapse 是 representational collapse 和训练发散的早期预测器\"\n      - \"比 weight norm、gradient norm 等传统指标更早、更清晰地检测到训练失败\"\n      - \"健康层的 SA 应有正负均衡分布，collapse 到单侧则预示不稳定\"\n    relevance_to_us: \"SA 是潜在的高价值 canary 指标——专门设计为 early warning，可直接纳入我们的指标 panel\"\n    metrics_studied: [\"spectral alignment\", \"weight norm\", \"gradient norm\"]\n\n  - id: \"he2025closer\"\n    title: \"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\"\n    authors: \"Shiliang He et al.\"\n    venue: \"NeurIPS 2025 (Spotlight)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2509.16499\"\n    category: \"canary-metrics\"\n    role: \"direct-competitor\"\n    key_findings:\n      - \"识别 diffusion model collapse 中的 generalization → memorization 转变\"\n      - \"**训练数据的 entropy 递减是 collapse 的直接驱动因素和清晰指标**\"\n      - \"提出基于 entropy 的数据选择策略，有效缓解 collapse\"\n    relevance_to_us: \"data entropy 作为 canary 的有效性已被验证（diffusion domain）；需测试是否在 LLM 场景同样有效\"\n    metrics_studied: [\"entropy\", \"FID\", \"diversity\"]\n\n  - id: \"ba2024fill\"\n    title: \"Fill In The Gaps: Model Calibration and Generalization with Synthetic Data\"\n    authors: \"Yang Ba, Michelle V Mancenido, Rong Pan\"\n    venue: \"EMNLP 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2410.10864\"\n    category: \"canary-metrics\"\n    role: \"background\"\n    key_findings:\n      - \"用 LLM 生成合成数据来修复 calibration 错误的 reliability diagram bins\"\n      - \"推导了基于 PAC 框架的 ECE bound\"\n      - \"合成数据可改善 calibration 但需精心设计生成策略\"\n    relevance_to_us: \"ECE 的理论 bound 可为我们的 canary 阈值设定提供理论依据\"\n    metrics_studied: [\"ECE\", \"accuracy\"]\n\n  # ============================================================\n  # DIVERSITY METRICS (BACKGROUND)\n  # ============================================================\n  - id: \"zhu2018texygen\"\n    title: \"Texygen: A Benchmarking Platform for Text Generation Models\"\n    authors: \"Yaoming Zhu et al.\"\n    venue: \"SIGIR 2018\"\n    year: 2018\n    url: \"https://arxiv.org/abs/1802.01886\"\n    category: \"canary-metrics\"\n    role: \"background\"\n    key_findings:\n      - \"提出 Self-BLEU 度量：计算生成句子间的 BLEU 相似度，Self-BLEU 越高多样性越低\"\n      - \"成为文本生成多样性评估的标准基准之一\"\n    relevance_to_us: \"Self-BLEU 是我们 diversity canary 的经典候选\"\n    metrics_studied: [\"Self-BLEU\", \"BLEU\"]\n\n  - id: \"li2016diversity\"\n    title: \"A Diversity-Promoting Objective Function for Neural Conversation Models\"\n    authors: \"Jiwei Li et al.\"\n    venue: \"NAACL 2016\"\n    year: 2016\n    url: \"https://arxiv.org/abs/1510.03055\"\n    category: \"canary-metrics\"\n    role: \"background\"\n    key_findings:\n      - \"提出 distinct-1 / distinct-2 指标衡量生成文本的 n-gram 多样性\"\n      - \"计算 unique n-gram 数占总 n-gram 数的比例\"\n    relevance_to_us: \"distinct-n 是最廉价的 diversity canary 之一，计算开销极低\"\n    metrics_studied: [\"distinct-1\", \"distinct-2\"]\n\n  # ============================================================\n  # REPRESENTATION / SPECTRAL COLLAPSE\n  # ============================================================\n  - id: \"jing2022understanding\"\n    title: \"Understanding Dimensional Collapse in Contrastive Self-supervised Learning\"\n    authors: \"Li Jing et al.\"\n    venue: \"ICLR 2022\"\n    year: 2022\n    url: \"https://openreview.net/forum?id=YevsQ05DEN7\"\n    category: \"canary-metrics\"\n    role: \"method-component\"\n    key_findings:\n      - \"定义 dimensional collapse：embedding 向量只跨越低维子空间\"\n      - \"effective rank（基于归一化特征值 entropy 的指数）作为 collapse 度量\"\n      - \"strong augmentation 和 implicit regularization 驱动低秩解\"\n    relevance_to_us: \"effective rank 的定义和计算方式可直接迁移到我们的 embedding 空间监控\"\n    metrics_studied: [\"effective rank\", \"singular value spectrum\"]\n\n  - id: \"noci2024mind\"\n    title: \"Mind the Gap: A Spectral Analysis of Rank Collapse and Signal Propagation in Transformers\"\n    authors: \"Lorenzo Noci et al.\"\n    venue: \"NeurIPS 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2410.07799\"\n    category: \"canary-metrics\"\n    role: \"method-component\"\n    key_findings:\n      - \"用 Random Matrix Theory 分析 attention 层的 rank collapse\"\n      - \"发现 attention matrix 最大两个奇异值之间的 spectral gap 是 width-collapse 的根因\"\n      - \"rank collapse in depth: 所有 token 沿层收敛到单一表示\"\n    relevance_to_us: \"spectral gap 作为另一种 spectral canary 候选；其 RMT 分析框架可启发我们的理论工作\"\n    metrics_studied: [\"spectral gap\", \"singular values\", \"effective rank\"]\n\n  # ============================================================\n  # DATA MIXING & ACCUMULATION\n  # ============================================================\n  - id: \"kazdan2025collapse\"\n    title: \"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World\"\n    authors: \"Joshua Kazdan, Rylan Schaeffer, Apratim Dey, Matthias Gerstgrasser, Rafael Rafailov, David L. Donoho, Sanmi Koyejo\"\n    venue: \"ICML 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2410.16713\"\n    category: \"data-mixing\"\n    role: \"foundation\"\n    key_findings:\n      - \"系统对比 replace vs accumulate 场景\"\n      - \"replace → collapse；accumulate → 可避免 collapse\"\n      - \"发现 real data 和 synthetic data 之间存在非平凡的交互效应\"\n      - \"synthetic data 的价值取决于 real data 的绝对数量\"\n    relevance_to_us: \"直接对应我们的 alpha（mixing ratio）实验维度；其 replace vs accumulate 框架是我们实验设计的重要参考\"\n    metrics_studied: [\"test loss\"]\n\n  - id: \"dey2024breaking\"\n    title: \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\"\n    authors: \"Apratim Dey, David Donoho, et al.\"\n    venue: \"ICML 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2404.01413\"\n    category: \"data-mixing\"\n    role: \"foundation\"\n    key_findings:\n      - \"替换数据 → 发散 population risk；累积数据 → 避免发散\"\n      - \"证明累积策略在多种模型（GMM, HMM, LLM）上有效\"\n    relevance_to_us: \"为我们的 alpha 实验提供理论预测：累积 vs 替换是 collapse 速率的关键调节因子\"\n    metrics_studied: [\"population risk\"]\n\n  - id: \"epstein2024howbad\"\n    title: \"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse\"\n    authors: \"Mohamed El Amine Epstein et al.\"\n    venue: \"arXiv (2404.05090)\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2404.05090\"\n    category: \"data-mixing\"\n    role: \"background\"\n    key_findings:\n      - \"纯合成数据训练不可避免 collapse\"\n      - \"给出 synthetic data 比例上界的估计——低于此比例可避免 collapse\"\n      - \"递归训练使原始分布尾部消失\"\n    relevance_to_us: \"其 mixing ratio 上界估计可对比我们实验中观测到的 canary 触发阈值\"\n    metrics_studied: [\"perplexity\"]\n\n  - id: \"bakshi2026improvement\"\n    title: \"From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources\"\n    authors: \"Soham Bakshi et al.\"\n    venue: \"arXiv (2602.10531)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2602.10531\"\n    category: \"data-mixing\"\n    role: \"background\"\n    key_findings:\n      - \"即使真实数据比例随时间衰减，只要非零就可能避免 collapse 并恢复真实分布\"\n      - \"在 next-token prediction 语言模型上分析混合训练的动态\"\n    relevance_to_us: \"提供了 decaying real data fraction 的理论保证，与我们的实验中 alpha 变化场景相关\"\n    metrics_studied: [\"population risk\"]\n\n  # ============================================================\n  # MITIGATION & VERIFICATION\n  # ============================================================\n  - id: \"feng2025escaping\"\n    title: \"Escaping Model Collapse via Synthetic Data Verification\"\n    authors: \"Yunzhen Feng et al.\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.16657\"\n    category: \"data-mixing\"\n    role: \"background\"\n    key_findings:\n      - \"通过外部 verifier（human 或 better model）注入信息可避免 collapse\"\n      - \"verifier-guided retraining 带来短期改善，但最终收敛到 verifier 的 knowledge center\"\n      - \"除非 verifier 完全可靠，早期收益会 plateau 甚至逆转\"\n    relevance_to_us: \"verification 作为 intervention 策略——如果 canary 触发，可考虑此类 reactive intervention\"\n    metrics_studied: [\"test loss\"]\n\n  - id: \"barzilai2025consistency\"\n    title: \"When Models Don't Collapse: On the Consistency of Iterative MLE\"\n    authors: \"Daniel Barzilai, Ohad Shamir\"\n    venue: \"ICML 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2505.19046\"\n    category: \"core-collapse\"\n    role: \"background\"\n    key_findings:\n      - \"在标准 MLE 一致性假设下，即使 real data fraction 趋近零也可避免 collapse\"\n      - \"但证明了某些情况下 collapse 可以任意快地发生——首次给出严格 collapse 反例\"\n    relevance_to_us: \"理论上的 collapse 可发生任意快的结论强化了 early warning 的价值\"\n    metrics_studied: []\n\n  - id: \"dces2026counter\"\n    title: \"Countering Model Collapse in Iterative Self-Training via Dynamic Center-Edge Sampling\"\n    authors: \"Anonymous\"\n    venue: \"MDPI Electronics (2026)\"\n    year: 2026\n    url: \"https://www.mdpi.com/2079-9292/15/4/869\"\n    category: \"data-mixing\"\n    role: \"background\"\n    key_findings:\n      - \"提出 DCES（dynamic center-edge sampling）数据选择框架\"\n      - \"DCES 在 ECE（0.1058 vs 0.1200）和 entropy 保持上优于随机选择\"\n    relevance_to_us: \"其 ECE 和 entropy 对比数据为我们的指标 baseline 提供参考\"\n    metrics_studied: [\"ECE\", \"entropy\"]\n\n  # ============================================================\n  # POSITION / SURVEY / EPISTEMICS\n  # ============================================================\n  - id: \"schaeffer2025position\"\n    title: \"Position: Model Collapse Does Not Mean What You Think\"\n    authors: \"Rylan Schaeffer, Joshua Kazdan, Alvan Caleb Arulandu, Sanmi Koyejo\"\n    venue: \"arXiv (2503.03150)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2503.03150\"\n    category: \"core-collapse\"\n    role: \"background\"\n    key_findings:\n      - \"文献中实际包含 8 种不同且有时矛盾的 model collapse 定义\"\n      - \"许多 collapse 预测依赖于与现实不符的假设\"\n      - \"多种 collapse 场景是可以轻易避免的\"\n    relevance_to_us: \"提醒我们明确定义 collapse 的操作标准；不同定义可能需要不同的 canary 指标\"\n    metrics_studied: []\n\n  - id: \"wang2025epistemic\"\n    title: \"Epistemic Diversity and Knowledge Collapse in Large Language Models\"\n    authors: \"Wang et al.\"\n    venue: \"arXiv (2510.04226)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.04226\"\n    category: \"core-collapse\"\n    role: \"background\"\n    key_findings:\n      - \"27 个 LLM 在 155 个主题上的 epistemic diversity 评估\"\n      - \"所有模型的 epistemic diversity 低于基本 web 搜索\"\n      - \"模型越大 epistemic diversity 反而越低；RAG 有正面效果\"\n    relevance_to_us: \"knowledge collapse 维度可扩展我们对 diversity canary 的理解——不仅是 lexical/syntactic 还有 epistemic\"\n    metrics_studied: [\"epistemic diversity\"]\n\n  # ============================================================\n  # METHODOLOGY (GRANGER / LEAD-LAG)\n  # ============================================================\n  - id: \"shojaie2022granger\"\n    title: \"Granger Causality: A Review and Recent Advances\"\n    authors: \"Ali Shojaie, Emily B. Fox\"\n    venue: \"Annual Review of Statistics and Its Application\"\n    year: 2022\n    url: \"https://arxiv.org/abs/2105.02675\"\n    category: \"methodology\"\n    role: \"method-component\"\n    key_findings:\n      - \"Granger causality 综述：从经典线性到非线性/neural 方法\"\n      - \"Panel data 场景的 Granger causality 扩展\"\n      - \"VAR 和 neural Granger causality 的对比\"\n    relevance_to_us: \"为我们的 panel Granger causality 分析提供方法论基础\"\n    metrics_studied: []\n\n  - id: \"marcinkevics2022neural\"\n    title: \"Granger Causality Using Neural Networks\"\n    authors: \"Raphael Marcinkevics, Julia Vogt\"\n    venue: \"arXiv (2208.03703)\"\n    year: 2022\n    url: \"https://arxiv.org/abs/2208.03703\"\n    category: \"methodology\"\n    role: \"method-component\"\n    key_findings:\n      - \"用 neural network 估计 Granger causality，突破线性假设\"\n      - \"两个模型对比法：含/不含外生变量的预测误差差异即 Granger causality 证据\"\n    relevance_to_us: \"我们的多指标时序可能存在非线性关系，neural Granger causality 是自然选择\"\n    metrics_studied: []\n\ngaps:\n  - \"无人系统做过 canary 指标的 lead-lag / Granger causality 分析——现有工作只在事后观察到指标变化，未量化哪些指标能提前多少步预测 collapse\"\n  - \"ECE 在 collapse 场景下几乎未被系统研究——chen2025scales 是唯一报告 ECE 先于 accuracy 退化的工作，但未做因果分析\"\n  - \"embedding effective rank 未在 iterative synthetic training 场景下被测试——仅在 contrastive learning/transformer 训练中研究过\"\n  - \"多指标 panel 框架缺失——无人同时追踪 ECE + effective rank + diversity + perplexity 的时序行为并分析其 lead-lag 关系\"\n  - \"alpha（synthetic ratio）对 canary 灵敏度的影响未被研究——现有工作只关注 alpha 对最终性能的影响，不关注 canary 的 lead time 如何随 alpha 变化\"\n  - \"predictive intervention vs reactive intervention 缺少对比——没有工作量化 early warning 带来的实际干预收益\"\n  - \"surplexity 和 spectral alignment 未在 iterative collapse 场景下交叉验证\"\n  - \"跨任务 canary 普适性未知——reasoning vs retrieval vs creative tasks 中哪些 canary 更可靠\"\n\nnovelty_assessment: |\n  我们项目的核心 novelty 在于：\n\n  1. **Panel Granger Causality 框架**：首次将多指标时序数据的因果分析方法应用于 model collapse 早期预警。\n     现有工作（chen2025scales, gambetta2024surplexity）只是事后观察到某些指标先变化，\n     但没有人做过系统的 lead-lag 量化分析。\n\n  2. **多指标 Canary Panel**：同时追踪 ECE、effective rank、Self-BLEU/distinct-n、\n     perplexity、entropy、surplexity 等指标，分析其相互关系和各自的 lead time。\n     现有工作都是单一指标或最多两三个指标的孤立分析。\n\n  3. **alpha-dependent Canary Sensitivity**：系统研究 synthetic ratio 如何影响各 canary\n     指标的灵敏度和 lead time。dohmatob2025strong 证明极小的 alpha 就能触发 collapse，\n     但没人研究 canary 在不同 alpha 下的行为。\n\n  4. **与已有工作的差异**：\n     - vs chen2025scales: 他们发现 ECE 先退化但没有做因果分析；我们用 Granger causality 量化\n     - vs gambetta2024surplexity: 他们提出 surplexity 用于检测和缓解 collapse；\n       我们将其纳入更广的 panel 并研究其 lead-lag 特性\n     - vs he2025closer: 他们在 diffusion 中用 entropy 作为指标；我们在 LLM 中测试更多指标\n     - vs qiu2025spectral: 他们的 SA 用于训练 loss explosion 预警；\n       我们将类似思路迁移到 iterative collapse 场景\n\n  5. **潜在风险**：chen2025scales 已经非常接近我们的方向。如果他们扩展到 lead-lag 分析，\n     我们的 novelty 会被削弱。需要快速推进并在方法论（Granger causality）上建立壁垒。\n",
      "numLines": 453,
      "startLine": 1,
      "totalLines": 453
    }
  }
}
```

</details>

---

### Assistant

_source line 44_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full file content. I need to make the following changes:

1. Add `truong2025entropy` to CORE MODEL COLLAPSE section (after briesch2024selfconsuming)
2. Add `sigma2026spectral` to CANARY / EARLY WARNING METRICS section (after ba2024fill)
3. Add `kalinowski2026topology` to CANARY / EARLY WARNING METRICS section (after sigma2026spectral)
4. Add `fu2025selfconsuming` to DATA MIXING & ACCUMULATION section (after epstein2024howbad)


5. Add `wang2026contaminated` to CORE MODEL COLLAPSE section (after truong2025entropy)
6. Update `bakshi2026improvement` entry

I need to plan out the edit locations carefully. The CORE MODEL COLLAPSE section ends around line 96, then the CANARY section starts at line 98, so I'll insert the two core-collapse entries between those. Then I'll handle the canary entries and the data-mixing entry, followed by updating bakshi2026improvement. Now I'm executing all four edits to reorganize the bibliography entries into their proper sections.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "ed78ddb6-b300-472f-a4b4-bb838a831dcc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JJzXwrmDkVp6YNrBMB64fV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10452,
      "cache_read_input_tokens": 45696,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10452
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

_source line 45_

Now I'll make all 4 edits in parallel: add 5 new entries and update the Bakshi entry.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "b1367d09-00e6-4206-9225-9d9600507aec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JJzXwrmDkVp6YNrBMB64fV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10452,
      "cache_read_input_tokens": 45696,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10452
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

_source line 46_

<details open><summary>🔧 Tool call — Edit · `toolu_01ESjMu3cQ8B9VyS2EmHYLeR`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/literature_map.yaml",
  "old_string": "    metrics_studied: [\"diversity\", \"quality\"]\n\n  # ============================================================\n  # CANARY / EARLY WARNING METRICS\n  # ============================================================",
  "new_string": "    metrics_studied: [\"diversity\", \"quality\"]\n\n  - id: \"truong2025entropy\"\n    title: \"Entropy Collapse: A Universal Failure Mode of Intelligent Systems\"\n    authors: \"Truong Xuan Khanh, Truong Quynh Hoa\"\n    venue: \"arXiv (2512.12381)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2512.12381\"\n    category: \"core-collapse\"\n    role: \"theoretical-foundation\"\n    key_findings:\n      - \"证明 entropy collapse 是一阶（不连续）相变，临界点 α_c(β) = 1/(1−β)，entropy 在临界点跳变 0.698 nats\"\n      - \"两个 universality class：Class 1（凸反馈，如 power-law）不可逆 ν=1；Class 2（线性反馈）可逆 ν=1/2\"\n      - \"因为是一阶相变，autocorrelation/variance 等传统 early-warning signal 在 collapse 前保持有限——无预警\"\n    relevance_to_us: \"定义了 canary 失效的 regime boundary：Class 1 凸反馈系统中传统 canary 理论上无效。我们需证明我们的 canary 在 Class 2+ regime 或非纯反馈场景中有效\"\n    gaps: \"理论框架高度抽象，未给出 LLM 具体场景下的 α/β 估计方法；未测试哪些 canary 在接近一阶相变时仍有部分预警能力\"\n    metrics_studied: [\"entropy\", \"autocorrelation\", \"variance\"]\n\n  - id: \"wang2026contaminated\"\n    title: \"Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training\"\n    authors: \"Kevin Wang, Hongqian Niu, Didong Li\"\n    venue: \"arXiv (2602.16065)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2602.16065\"\n    category: \"core-collapse\"\n    role: \"theoretical-foundation\"\n    key_findings:\n      - \"首个不限数据分布假设的正面理论结果：universal approximator 下 contaminated recursive training 仍可收敛\"\n      - \"收敛速率 = min(baseline 模型收敛速率, 每轮真实数据比例)——真实数据比例是瓶颈\"\n      - \"突破了先前仅限 discrete/Gaussian 分布的理论框架，适用于一般连续分布\"\n    relevance_to_us: \"为 post-MVP α-sweep 实验提供理论上界：收敛速率由 real data fraction 决定，可预测不同 α 下的 collapse 速率\"\n    gaps: \"universal approximator 假设在实际有限容量模型中不严格成立；未讨论 canary 指标行为\"\n    metrics_studied: [\"convergence rate\", \"population risk\"]\n\n  # ============================================================\n  # CANARY / EARLY WARNING METRICS\n  # ============================================================"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "61666318-9660-4745-9917-ec49757d093e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JJzXwrmDkVp6YNrBMB64fV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10452,
      "cache_read_input_tokens": 45696,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10452
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

_source line 47 · 2026-05-14T05:45:48.107Z_

<details><summary>↩ Tool result · `toolu_01ESjMu3cQ8B9VyS2EmHYLeR`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "46b35c72-ebca-4a86-8b6d-a5c9424aa50d",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/literature_map.yaml",
    "oldString": "    metrics_studied: [\"diversity\", \"quality\"]\n\n  # ============================================================\n  # CANARY / EARLY WARNING METRICS\n  # ============================================================",
    "newString": "    metrics_studied: [\"diversity\", \"quality\"]\n\n  - id: \"truong2025entropy\"\n    title: \"Entropy Collapse: A Universal Failure Mode of Intelligent Systems\"\n    authors: \"Truong Xuan Khanh, Truong Quynh Hoa\"\n    venue: \"arXiv (2512.12381)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2512.12381\"\n    category: \"core-collapse\"\n    role: \"theoretical-foundation\"\n    key_findings:\n      - \"证明 entropy collapse 是一阶（不连续）相变，临界点 α_c(β) = 1/(1−β)，entropy 在临界点跳变 0.698 nats\"\n      - \"两个 universality class：Class 1（凸反馈，如 power-law）不可逆 ν=1；Class 2（线性反馈）可逆 ν=1/2\"\n      - \"因为是一阶相变，autocorrelation/variance 等传统 early-warning signal 在 collapse 前保持有限——无预警\"\n    relevance_to_us: \"定义了 canary 失效的 regime boundary：Class 1 凸反馈系统中传统 canary 理论上无效。我们需证明我们的 canary 在 Class 2+ regime 或非纯反馈场景中有效\"\n    gaps: \"理论框架高度抽象，未给出 LLM 具体场景下的 α/β 估计方法；未测试哪些 canary 在接近一阶相变时仍有部分预警能力\"\n    metrics_studied: [\"entropy\", \"autocorrelation\", \"variance\"]\n\n  - id: \"wang2026contaminated\"\n    title: \"Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training\"\n    authors: \"Kevin Wang, Hongqian Niu, Didong Li\"\n    venue: \"arXiv (2602.16065)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2602.16065\"\n    category: \"core-collapse\"\n    role: \"theoretical-foundation\"\n    key_findings:\n      - \"首个不限数据分布假设的正面理论结果：universal approximator 下 contaminated recursive training 仍可收敛\"\n      - \"收敛速率 = min(baseline 模型收敛速率, 每轮真实数据比例)——真实数据比例是瓶颈\"\n      - \"突破了先前仅限 discrete/Gaussian 分布的理论框架，适用于一般连续分布\"\n    relevance_to_us: \"为 post-MVP α-sweep 实验提供理论上界：收敛速率由 real data fraction 决定，可预测不同 α 下的 collapse 速率\"\n    gaps: \"universal approximator 假设在实际有限容量模型中不严格成立；未讨论 canary 指标行为\"\n    metrics_studied: [\"convergence rate\", \"population risk\"]\n\n  # ============================================================\n  # CANARY / EARLY WARNING METRICS\n  # ============================================================",
    "originalFile": "papers:\n  # ============================================================\n  # CORE MODEL COLLAPSE\n  # ============================================================\n  - id: \"shumailov2024curse\"\n    title: \"The Curse of Recursion: Training on Generated Data Makes Models Forget\"\n    authors: \"Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Yarin Gal, Nicolas Papernot, Ross Anderson\"\n    venue: \"Nature\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2305.17493\"\n    category: \"core-collapse\"\n    role: \"foundation\"\n    key_findings:\n      - \"定义 model collapse 现象：迭代用合成数据替换真实数据训练会导致分布尾部消失\"\n      - \"区分 early model collapse（尾部信息丢失）和 late model collapse（分布完全收敛）\"\n      - \"三类误差来源：statistical approximation, functional expressivity, functional approximation，跨代复合\"\n      - \"在 VAE、GMM、LLM 上均验证了 collapse 的普遍性\"\n    relevance_to_us: \"奠基论文，定义了我们研究的核心现象。我们的 canary 指标旨在提前检测其描述的 early collapse 阶段\"\n    metrics_studied: [\"perplexity\", \"distributional tail mass\"]\n\n  - id: \"alemohammad2024mad\"\n    title: \"Self-Consuming Generative Models Go MAD\"\n    authors: \"Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, Richard Baraniuk\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2307.01850\"\n    category: \"core-collapse\"\n    role: \"foundation\"\n    key_findings:\n      - \"提出 Model Autophagy Disorder (MAD) 概念\"\n      - \"autophagous loop 中没有足够新鲜真实数据时，质量或多样性必然渐进下降\"\n      - \"在图像生成领域验证 self-consuming loop 的退化效应\"\n    relevance_to_us: \"MAD 框架与我们的 iterative loop 设置直接对应；其 quality vs diversity tradeoff 可能反映在不同 canary 指标上\"\n    metrics_studied: [\"FID\", \"precision\", \"recall\", \"diversity\"]\n\n  - id: \"dohmatob2024tale\"\n    title: \"A Tale of Tails: Model Collapse as a Change of Scaling Laws\"\n    authors: \"Elvis Dohmatob, Yunzhen Feng, et al.\"\n    venue: \"ICML 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2402.07043\"\n    category: \"core-collapse\"\n    role: \"foundation\"\n    key_findings:\n      - \"通过 scaling laws 视角分析 model collapse：collapse 表现为 scaling law 的变化\"\n      - \"发现 loss of scaling, shifted scaling, skill un-learning, grokking 等多种退化模式\"\n      - \"混入少量干净数据可缓解 collapse 并引发 grokking 现象\"\n      - \"在 transformer 算术任务和 Llama2 文本生成上验证\"\n    relevance_to_us: \"scaling law 变化视角为我们提供了理论基础；grokking 现象暗示 canary 指标可能出现非单调行为\"\n    metrics_studied: [\"test loss\", \"scaling exponents\"]\n\n  - id: \"dohmatob2025strong\"\n    title: \"Strong Model Collapse\"\n    authors: \"Elvis Dohmatob, Yunzhen Feng, Arjun Subramonian, Julia Kempe\"\n    venue: \"ICLR 2025 (Spotlight)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2410.04840\"\n    category: \"core-collapse\"\n    role: \"foundation\"\n    key_findings:\n      - \"即使合成数据占比极小（1/1000），仍可导致 model collapse\"\n      - \"更大的训练集并不能避免 collapse\"\n      - \"更大的模型（random projection 近似下）反而可能放大 collapse\"\n      - \"存在 interpolation threshold 的 double-descent 现象\"\n    relevance_to_us: \"强化了早期检测的必要性——即使极小的合成数据比例也能触发 collapse，因此 canary 指标必须敏感\"\n    metrics_studied: [\"test loss\", \"population risk\"]\n\n  - id: \"guo2024linguistic\"\n    title: \"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\"\n    authors: \"Yanzhu Guo, Guokan Shang, et al.\"\n    venue: \"NAACL 2024 Findings\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2311.09807\"\n    category: \"core-collapse\"\n    role: \"evaluation\"\n    key_findings:\n      - \"递归微调中，linguistic diversity 在连续迭代中持续下降\"\n      - \"创造性任务中 diversity 下降最显著\"\n      - \"开发了覆盖 lexical、syntactic、semantic 三层的 diversity 指标体系\"\n    relevance_to_us: \"其多层 diversity 指标体系可直接作为我们 canary 指标的候选集；创造性 vs 事实任务的差异可能影响 canary 灵敏度\"\n    metrics_studied: [\"distinct-n\", \"type-token ratio\", \"syntactic diversity\", \"semantic diversity\"]\n\n  - id: \"briesch2024selfconsuming\"\n    title: \"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop\"\n    authors: \"Martin Briesch, Dominik Sobania, Franz Rothlauf\"\n    venue: \"arXiv (2311.16822)\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2311.16822\"\n    category: \"core-collapse\"\n    role: \"direct-competitor\"\n    key_findings:\n      - \"首次系统研究 LLM 的 self-consuming training loop\"\n      - \"full synthetic cycle（完全替换）导致单点 collapse；data augmentation cycle 导致 diversity 缓慢下降\"\n      - \"expanding data cycle（累积）在 50 代内保持 diversity\"\n    relevance_to_us: \"其不同 data cycle 策略的对比直接对应我们的 alpha（synthetic ratio）实验设置\"\n    metrics_studied: [\"diversity\", \"quality\"]\n\n  # ============================================================\n  # CANARY / EARLY WARNING METRICS\n  # ============================================================\n  - id: \"chen2025scales\"\n    title: \"Characterizing Model Behavior Under Synthetic Data Training: An Empirical Study Across Scales and Mixing Ratios\"\n    authors: \"Anonymous\"\n    venue: \"arXiv (2510.05133)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.05133\"\n    category: \"canary-metrics\"\n    role: \"direct-competitor\"\n    key_findings:\n      - \"**Calibration degradation precedes accuracy loss** — ECE 是 collapse 的 early warning signal\"\n      - \"20% synthetic data 以下性能稳定，30% 以上退化加速\"\n      - \"大模型（6.9B-12B）比小模型（410M-1.4B）更鲁棒\"\n      - \"推理任务比检索任务更易退化\"\n      - \"iteration 1 + 30% synthetic 时 ECE 从 0.08 升至 0.14（+75%）\"\n    relevance_to_us: \"**最直接的竞争者/先驱**。证实 ECE 可作为 canary，但未做 lead-lag 分析，未建立多指标 panel 框架\"\n    metrics_studied: [\"ECE\", \"accuracy\", \"perplexity\"]\n\n  - id: \"gambetta2024surplexity\"\n    title: \"Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI\"\n    authors: \"Daniele Gambetta et al.\"\n    venue: \"arXiv (2410.12341)\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2410.12341\"\n    category: \"canary-metrics\"\n    role: \"direct-competitor\"\n    key_findings:\n      - \"提出 surplexity（model surprise 度量）同时用于检测 collapse 和过滤训练数据\"\n      - \"用 semantic networks 分析文本重复性和语义多样性\"\n      - \"用 next-token probability 定量衡量 diversity loss\"\n      - \"高 surplexity 过滤策略至少与 human-data baseline 同效，且更能降低分布偏斜\"\n      - \"不需要区分 human vs AI-generated data\"\n    relevance_to_us: \"surplexity 可作为我们 canary 指标候选之一；其 semantic network 方法提供了 diversity 度量的另一视角\"\n    metrics_studied: [\"surplexity\", \"semantic network metrics\", \"next-token probability\"]\n\n  - id: \"qiu2025spectral\"\n    title: \"Spectral Alignment as Predictor of Loss Explosion in Neural Network Training\"\n    authors: \"Haiquan Qiu, You Wu, Yingjie Tan, Yaqing Wang, Quanming Yao\"\n    venue: \"arXiv (2510.04202)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.04202\"\n    category: \"canary-metrics\"\n    role: \"method-component\"\n    key_findings:\n      - \"Spectral Alignment (SA) 监控层输入与权重矩阵主奇异向量的分布对齐\"\n      - \"SA sign diversity collapse 是 representational collapse 和训练发散的早期预测器\"\n      - \"比 weight norm、gradient norm 等传统指标更早、更清晰地检测到训练失败\"\n      - \"健康层的 SA 应有正负均衡分布，collapse 到单侧则预示不稳定\"\n    relevance_to_us: \"SA 是潜在的高价值 canary 指标——专门设计为 early warning，可直接纳入我们的指标 panel\"\n    metrics_studied: [\"spectral alignment\", \"weight norm\", \"gradient norm\"]\n\n  - id: \"he2025closer\"\n    title: \"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\"\n    authors: \"Shiliang He et al.\"\n    venue: \"NeurIPS 2025 (Spotlight)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2509.16499\"\n    category: \"canary-metrics\"\n    role: \"direct-competitor\"\n    key_findings:\n      - \"识别 diffusion model collapse 中的 generalization → memorization 转变\"\n      - \"**训练数据的 entropy 递减是 collapse 的直接驱动因素和清晰指标**\"\n      - \"提出基于 entropy 的数据选择策略，有效缓解 collapse\"\n    relevance_to_us: \"data entropy 作为 canary 的有效性已被验证（diffusion domain）；需测试是否在 LLM 场景同样有效\"\n    metrics_studied: [\"entropy\", \"FID\", \"diversity\"]\n\n  - id: \"ba2024fill\"\n    title: \"Fill In The Gaps: Model Calibration and Generalization with Synthetic Data\"\n    authors: \"Yang Ba, Michelle V Mancenido, Rong Pan\"\n    venue: \"EMNLP 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2410.10864\"\n    category: \"canary-metrics\"\n    role: \"background\"\n    key_findings:\n      - \"用 LLM 生成合成数据来修复 calibration 错误的 reliability diagram bins\"\n      - \"推导了基于 PAC 框架的 ECE bound\"\n      - \"合成数据可改善 calibration 但需精心设计生成策略\"\n    relevance_to_us: \"ECE 的理论 bound 可为我们的 canary 阈值设定提供理论依据\"\n    metrics_studied: [\"ECE\", \"accuracy\"]\n\n  # ============================================================\n  # DIVERSITY METRICS (BACKGROUND)\n  # ============================================================\n  - id: \"zhu2018texygen\"\n    title: \"Texygen: A Benchmarking Platform for Text Generation Models\"\n    authors: \"Yaoming Zhu et al.\"\n    venue: \"SIGIR 2018\"\n    year: 2018\n    url: \"https://arxiv.org/abs/1802.01886\"\n    category: \"canary-metrics\"\n    role: \"background\"\n    key_findings:\n      - \"提出 Self-BLEU 度量：计算生成句子间的 BLEU 相似度，Self-BLEU 越高多样性越低\"\n      - \"成为文本生成多样性评估的标准基准之一\"\n    relevance_to_us: \"Self-BLEU 是我们 diversity canary 的经典候选\"\n    metrics_studied: [\"Self-BLEU\", \"BLEU\"]\n\n  - id: \"li2016diversity\"\n    title: \"A Diversity-Promoting Objective Function for Neural Conversation Models\"\n    authors: \"Jiwei Li et al.\"\n    venue: \"NAACL 2016\"\n    year: 2016\n    url: \"https://arxiv.org/abs/1510.03055\"\n    category: \"canary-metrics\"\n    role: \"background\"\n    key_findings:\n      - \"提出 distinct-1 / distinct-2 指标衡量生成文本的 n-gram 多样性\"\n      - \"计算 unique n-gram 数占总 n-gram 数的比例\"\n    relevance_to_us: \"distinct-n 是最廉价的 diversity canary 之一，计算开销极低\"\n    metrics_studied: [\"distinct-1\", \"distinct-2\"]\n\n  # ============================================================\n  # REPRESENTATION / SPECTRAL COLLAPSE\n  # ============================================================\n  - id: \"jing2022understanding\"\n    title: \"Understanding Dimensional Collapse in Contrastive Self-supervised Learning\"\n    authors: \"Li Jing et al.\"\n    venue: \"ICLR 2022\"\n    year: 2022\n    url: \"https://openreview.net/forum?id=YevsQ05DEN7\"\n    category: \"canary-metrics\"\n    role: \"method-component\"\n    key_findings:\n      - \"定义 dimensional collapse：embedding 向量只跨越低维子空间\"\n      - \"effective rank（基于归一化特征值 entropy 的指数）作为 collapse 度量\"\n      - \"strong augmentation 和 implicit regularization 驱动低秩解\"\n    relevance_to_us: \"effective rank 的定义和计算方式可直接迁移到我们的 embedding 空间监控\"\n    metrics_studied: [\"effective rank\", \"singular value spectrum\"]\n\n  - id: \"noci2024mind\"\n    title: \"Mind the Gap: A Spectral Analysis of Rank Collapse and Signal Propagation in Transformers\"\n    authors: \"Lorenzo Noci et al.\"\n    venue: \"NeurIPS 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2410.07799\"\n    category: \"canary-metrics\"\n    role: \"method-component\"\n    key_findings:\n      - \"用 Random Matrix Theory 分析 attention 层的 rank collapse\"\n      - \"发现 attention matrix 最大两个奇异值之间的 spectral gap 是 width-collapse 的根因\"\n      - \"rank collapse in depth: 所有 token 沿层收敛到单一表示\"\n    relevance_to_us: \"spectral gap 作为另一种 spectral canary 候选；其 RMT 分析框架可启发我们的理论工作\"\n    metrics_studied: [\"spectral gap\", \"singular values\", \"effective rank\"]\n\n  # ============================================================\n  # DATA MIXING & ACCUMULATION\n  # ============================================================\n  - id: \"kazdan2025collapse\"\n    title: \"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World\"\n    authors: \"Joshua Kazdan, Rylan Schaeffer, Apratim Dey, Matthias Gerstgrasser, Rafael Rafailov, David L. Donoho, Sanmi Koyejo\"\n    venue: \"ICML 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2410.16713\"\n    category: \"data-mixing\"\n    role: \"foundation\"\n    key_findings:\n      - \"系统对比 replace vs accumulate 场景\"\n      - \"replace → collapse；accumulate → 可避免 collapse\"\n      - \"发现 real data 和 synthetic data 之间存在非平凡的交互效应\"\n      - \"synthetic data 的价值取决于 real data 的绝对数量\"\n    relevance_to_us: \"直接对应我们的 alpha（mixing ratio）实验维度；其 replace vs accumulate 框架是我们实验设计的重要参考\"\n    metrics_studied: [\"test loss\"]\n\n  - id: \"dey2024breaking\"\n    title: \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\"\n    authors: \"Apratim Dey, David Donoho, et al.\"\n    venue: \"ICML 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2404.01413\"\n    category: \"data-mixing\"\n    role: \"foundation\"\n    key_findings:\n      - \"替换数据 → 发散 population risk；累积数据 → 避免发散\"\n      - \"证明累积策略在多种模型（GMM, HMM, LLM）上有效\"\n    relevance_to_us: \"为我们的 alpha 实验提供理论预测：累积 vs 替换是 collapse 速率的关键调节因子\"\n    metrics_studied: [\"population risk\"]\n\n  - id: \"epstein2024howbad\"\n    title: \"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse\"\n    authors: \"Mohamed El Amine Epstein et al.\"\n    venue: \"arXiv (2404.05090)\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2404.05090\"\n    category: \"data-mixing\"\n    role: \"background\"\n    key_findings:\n      - \"纯合成数据训练不可避免 collapse\"\n      - \"给出 synthetic data 比例上界的估计——低于此比例可避免 collapse\"\n      - \"递归训练使原始分布尾部消失\"\n    relevance_to_us: \"其 mixing ratio 上界估计可对比我们实验中观测到的 canary 触发阈值\"\n    metrics_studied: [\"perplexity\"]\n\n  - id: \"bakshi2026improvement\"\n    title: \"From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources\"\n    authors: \"Soham Bakshi et al.\"\n    venue: \"arXiv (2602.10531)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2602.10531\"\n    category: \"data-mixing\"\n    role: \"background\"\n    key_findings:\n      - \"即使真实数据比例随时间衰减，只要非零就可能避免 collapse 并恢复真实分布\"\n      - \"在 next-token prediction 语言模型上分析混合训练的动态\"\n    relevance_to_us: \"提供了 decaying real data fraction 的理论保证，与我们的实验中 alpha 变化场景相关\"\n    metrics_studied: [\"population risk\"]\n\n  # ============================================================\n  # MITIGATION & VERIFICATION\n  # ============================================================\n  - id: \"feng2025escaping\"\n    title: \"Escaping Model Collapse via Synthetic Data Verification\"\n    authors: \"Yunzhen Feng et al.\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.16657\"\n    category: \"data-mixing\"\n    role: \"background\"\n    key_findings:\n      - \"通过外部 verifier（human 或 better model）注入信息可避免 collapse\"\n      - \"verifier-guided retraining 带来短期改善，但最终收敛到 verifier 的 knowledge center\"\n      - \"除非 verifier 完全可靠，早期收益会 plateau 甚至逆转\"\n    relevance_to_us: \"verification 作为 intervention 策略——如果 canary 触发，可考虑此类 reactive intervention\"\n    metrics_studied: [\"test loss\"]\n\n  - id: \"barzilai2025consistency\"\n    title: \"When Models Don't Collapse: On the Consistency of Iterative MLE\"\n    authors: \"Daniel Barzilai, Ohad Shamir\"\n    venue: \"ICML 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2505.19046\"\n    category: \"core-collapse\"\n    role: \"background\"\n    key_findings:\n      - \"在标准 MLE 一致性假设下，即使 real data fraction 趋近零也可避免 collapse\"\n      - \"但证明了某些情况下 collapse 可以任意快地发生——首次给出严格 collapse 反例\"\n    relevance_to_us: \"理论上的 collapse 可发生任意快的结论强化了 early warning 的价值\"\n    metrics_studied: []\n\n  - id: \"dces2026counter\"\n    title: \"Countering Model Collapse in Iterative Self-Training via Dynamic Center-Edge Sampling\"\n    authors: \"Anonymous\"\n    venue: \"MDPI Electronics (2026)\"\n    year: 2026\n    url: \"https://www.mdpi.com/2079-9292/15/4/869\"\n    category: \"data-mixing\"\n    role: \"background\"\n    key_findings:\n      - \"提出 DCES（dynamic center-edge sampling）数据选择框架\"\n      - \"DCES 在 ECE（0.1058 vs 0.1200）和 entropy 保持上优于随机选择\"\n    relevance_to_us: \"其 ECE 和 entropy 对比数据为我们的指标 baseline 提供参考\"\n    metrics_studied: [\"ECE\", \"entropy\"]\n\n  # ============================================================\n  # POSITION / SURVEY / EPISTEMICS\n  # ============================================================\n  - id: \"schaeffer2025position\"\n    title: \"Position: Model Collapse Does Not Mean What You Think\"\n    authors: \"Rylan Schaeffer, Joshua Kazdan, Alvan Caleb Arulandu, Sanmi Koyejo\"\n    venue: \"arXiv (2503.03150)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2503.03150\"\n    category: \"core-collapse\"\n    role: \"background\"\n    key_findings:\n      - \"文献中实际包含 8 种不同且有时矛盾的 model collapse 定义\"\n      - \"许多 collapse 预测依赖于与现实不符的假设\"\n      - \"多种 collapse 场景是可以轻易避免的\"\n    relevance_to_us: \"提醒我们明确定义 collapse 的操作标准；不同定义可能需要不同的 canary 指标\"\n    metrics_studied: []\n\n  - id: \"wang2025epistemic\"\n    title: \"Epistemic Diversity and Knowledge Collapse in Large Language Models\"\n    authors: \"Wang et al.\"\n    venue: \"arXiv (2510.04226)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.04226\"\n    category: \"core-collapse\"\n    role: \"background\"\n    key_findings:\n      - \"27 个 LLM 在 155 个主题上的 epistemic diversity 评估\"\n      - \"所有模型的 epistemic diversity 低于基本 web 搜索\"\n      - \"模型越大 epistemic diversity 反而越低；RAG 有正面效果\"\n    relevance_to_us: \"knowledge collapse 维度可扩展我们对 diversity canary 的理解——不仅是 lexical/syntactic 还有 epistemic\"\n    metrics_studied: [\"epistemic diversity\"]\n\n  # ============================================================\n  # METHODOLOGY (GRANGER / LEAD-LAG)\n  # ============================================================\n  - id: \"shojaie2022granger\"\n    title: \"Granger Causality: A Review and Recent Advances\"\n    authors: \"Ali Shojaie, Emily B. Fox\"\n    venue: \"Annual Review of Statistics and Its Application\"\n    year: 2022\n    url: \"https://arxiv.org/abs/2105.02675\"\n    category: \"methodology\"\n    role: \"method-component\"\n    key_findings:\n      - \"Granger causality 综述：从经典线性到非线性/neural 方法\"\n      - \"Panel data 场景的 Granger causality 扩展\"\n      - \"VAR 和 neural Granger causality 的对比\"\n    relevance_to_us: \"为我们的 panel Granger causality 分析提供方法论基础\"\n    metrics_studied: []\n\n  - id: \"marcinkevics2022neural\"\n    title: \"Granger Causality Using Neural Networks\"\n    authors: \"Raphael Marcinkevics, Julia Vogt\"\n    venue: \"arXiv (2208.03703)\"\n    year: 2022\n    url: \"https://arxiv.org/abs/2208.03703\"\n    category: \"methodology\"\n    role: \"method-component\"\n    key_findings:\n      - \"用 neural network 估计 Granger causality，突破线性假设\"\n      - \"两个模型对比法：含/不含外生变量的预测误差差异即 Granger causality 证据\"\n    relevance_to_us: \"我们的多指标时序可能存在非线性关系，neural Granger causality 是自然选择\"\n    metrics_studied: []\n\ngaps:\n  - \"无人系统做过 canary 指标的 lead-lag / Granger causality 分析——现有工作只在事后观察到指标变化，未量化哪些指标能提前多少步预测 collapse\"\n  - \"ECE 在 collapse 场景下几乎未被系统研究——chen2025scales 是唯一报告 ECE 先于 accuracy 退化的工作，但未做因果分析\"\n  - \"embedding effective rank 未在 iterative synthetic training 场景下被测试——仅在 contrastive learning/transformer 训练中研究过\"\n  - \"多指标 panel 框架缺失——无人同时追踪 ECE + effective rank + diversity + perplexity 的时序行为并分析其 lead-lag 关系\"\n  - \"alpha（synthetic ratio）对 canary 灵敏度的影响未被研究——现有工作只关注 alpha 对最终性能的影响，不关注 canary 的 lead time 如何随 alpha 变化\"\n  - \"predictive intervention vs reactive intervention 缺少对比——没有工作量化 early warning 带来的实际干预收益\"\n  - \"surplexity 和 spectral alignment 未在 iterative collapse 场景下交叉验证\"\n  - \"跨任务 canary 普适性未知——reasoning vs retrieval vs creative tasks 中哪些 canary 更可靠\"\n\nnovelty_assessment: |\n  我们项目的核心 novelty 在于：\n\n  1. **Panel Granger Causality 框架**：首次将多指标时序数据的因果分析方法应用于 model collapse 早期预警。\n     现有工作（chen2025scales, gambetta2024surplexity）只是事后观察到某些指标先变化，\n     但没有人做过系统的 lead-lag 量化分析。\n\n  2. **多指标 Canary Panel**：同时追踪 ECE、effective rank、Self-BLEU/distinct-n、\n     perplexity、entropy、surplexity 等指标，分析其相互关系和各自的 lead time。\n     现有工作都是单一指标或最多两三个指标的孤立分析。\n\n  3. **alpha-dependent Canary Sensitivity**：系统研究 synthetic ratio 如何影响各 canary\n     指标的灵敏度和 lead time。dohmatob2025strong 证明极小的 alpha 就能触发 collapse，\n     但没人研究 canary 在不同 alpha 下的行为。\n\n  4. **与已有工作的差异**：\n     - vs chen2025scales: 他们发现 ECE 先退化但没有做因果分析；我们用 Granger causality 量化\n     - vs gambetta2024surplexity: 他们提出 surplexity 用于检测和缓解 collapse；\n       我们将其纳入更广的 panel 并研究其 lead-lag 特性\n     - vs he2025closer: 他们在 diffusion 中用 entropy 作为指标；我们在 LLM 中测试更多指标\n     - vs qiu2025spectral: 他们的 SA 用于训练 loss explosion 预警；\n       我们将类似思路迁移到 iterative collapse 场景\n\n  5. **潜在风险**：chen2025scales 已经非常接近我们的方向。如果他们扩展到 lead-lag 分析，\n     我们的 novelty 会被削弱。需要快速推进并在方法论（Granger causality）上建立壁垒。\n",
    "structuredPatch": [
      {
        "oldStart": 95,
        "oldLines": 6,
        "newStart": 95,
        "newLines": 38,
        "lines": [
          "     relevance_to_us: \"其不同 data cycle 策略的对比直接对应我们的 alpha（synthetic ratio）实验设置\"",
          "     metrics_studied: [\"diversity\", \"quality\"]",
          " ",
          "+  - id: \"truong2025entropy\"",
          "+    title: \"Entropy Collapse: A Universal Failure Mode of Intelligent Systems\"",
          "+    authors: \"Truong Xuan Khanh, Truong Quynh Hoa\"",
          "+    venue: \"arXiv (2512.12381)\"",
          "+    year: 2025",
          "+    url: \"https://arxiv.org/abs/2512.12381\"",
          "+    category: \"core-collapse\"",
          "+    role: \"theoretical-foundation\"",
          "+    key_findings:",
          "+      - \"证明 entropy collapse 是一阶（不连续）相变，临界点 α_c(β) = 1/(1−β)，entropy 在临界点跳变 0.698 nats\"",
          "+      - \"两个 universality class：Class 1（凸反馈，如 power-law）不可逆 ν=1；Class 2（线性反馈）可逆 ν=1/2\"",
          "+      - \"因为是一阶相变，autocorrelation/variance 等传统 early-warning signal 在 collapse 前保持有限——无预警\"",
          "+    relevance_to_us: \"定义了 canary 失效的 regime boundary：Class 1 凸反馈系统中传统 canary 理论上无效。我们需证明我们的 canary 在 Class 2+ regime 或非纯反馈场景中有效\"",
          "+    gaps: \"理论框架高度抽象，未给出 LLM 具体场景下的 α/β 估计方法；未测试哪些 canary 在接近一阶相变时仍有部分预警能力\"",
          "+    metrics_studied: [\"entropy\", \"autocorrelation\", \"variance\"]",
          "+",
          "+  - id: \"wang2026contaminated\"",
          "+    title: \"Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training\"",
          "+    authors: \"Kevin Wang, Hongqian Niu, Didong Li\"",
          "+    venue: \"arXiv (2602.16065)\"",
          "+    year: 2026",
          "+    url: \"https://arxiv.org/abs/2602.16065\"",
          "+    category: \"core-collapse\"",
          "+    role: \"theoretical-foundation\"",
          "+    key_findings:",
          "+      - \"首个不限数据分布假设的正面理论结果：universal approximator 下 contaminated recursive training 仍可收敛\"",
          "+      - \"收敛速率 = min(baseline 模型收敛速率, 每轮真实数据比例)——真实数据比例是瓶颈\"",
          "+      - \"突破了先前仅限 discrete/Gaussian 分布的理论框架，适用于一般连续分布\"",
          "+    relevance_to_us: \"为 post-MVP α-sweep 实验提供理论上界：收敛速率由 real data fraction 决定，可预测不同 α 下的 collapse 速率\"",
          "+    gaps: \"universal approximator 假设在实际有限容量模型中不严格成立；未讨论 canary 指标行为\"",
          "+    metrics_studied: [\"convergence rate\", \"population risk\"]",
          "+",
          "   # ============================================================",
          "   # CANARY / EARLY WARNING METRICS",
          "   # ============================================================"
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

### Tool call

_source line 48_

<details open><summary>🔧 Tool call — Edit · `toolu_01UrWHuR36BK8tyk8ZgNKArU`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/literature_map.yaml",
  "old_string": "    metrics_studied: [\"ECE\", \"accuracy\"]\n\n  # ============================================================\n  # DIVERSITY METRICS (BACKGROUND)\n  # ============================================================",
  "new_string": "    metrics_studied: [\"ECE\", \"accuracy\"]\n\n  - id: \"sigma2026spectral\"\n    title: \"SIGMA: Scalable Spectral Insights for LLM Model Collapse\"\n    authors: \"Yi Gu, Lingyou Pang, Xiangkun Ye, Tianyu Wang, Jianyu Lin, Carey E. Priebe, Alexander Aue\"\n    venue: \"arXiv (2601.03385)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2601.03385\"\n    category: \"canary-metrics\"\n    role: \"direct-competitor\"\n    key_findings:\n      - \"基于 embedding Gram matrix 谱分析的 collapse 监控框架：Track I（确定性谱界）保守但鲁棒，Track II（随机谱缩放）灵敏但需采样\"\n      - \"Track I/II 的分歧本身是 early-stage collapse 的诊断信号，早于表面重复性伪影\"\n      - \"随机谱界使部分观测的 Gram matrix 也可用于大规模模型的可扩展监控\"\n    relevance_to_us: \"最直接的 spectral canary 竞争者。我们的 effective rank 是其简化版（单一标量 vs 完整谱界）；需在 related work 中明确差异：SIGMA 提供双轨谱界，我们用单一 effective rank 换取更低计算开销和多指标 panel 集成\"\n    gaps: \"未做 lead-lag 分析，未与 ECE/diversity 等非谱指标对比；Track I/II 的计算开销在 iterative loop 多轮场景下可能不可忽略\"\n    metrics_studied: [\"Gram matrix eigenspectrum\", \"spectral norm bounds\"]\n\n  - id: \"kalinowski2026topology\"\n    title: \"Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index\"\n    authors: \"Alexander Kalinowski\"\n    venue: \"arXiv (2604.26984)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2604.26984\"\n    category: \"canary-metrics\"\n    role: \"background\"\n    key_findings:\n      - \"提出基于 Modular Morse Homology Maintenance (MMHM) 的在线拓扑监控方案，增量更新避免每轮重建\"\n      - \"Collapse Index (CI) 组合多尺度拓扑特征，在 LLM fine-tuning 和 temporal KGE 训练中提供低延迟 early-warning\"\n      - \"拓扑方法捕捉表示空间的各向异性和多尺度结构丧失\"\n    relevance_to_us: \"topology-based monitoring 是与 spectral 方法正交的 collapse 检测路线。我们排除了该方法（计算开销高、可解释性弱），但 related work 需要对比说明选择 spectral/calibration panel 而非 topology 的理由\"\n    gaps: \"计算开销显著高于 effective rank 等标量指标；未在 iterative synthetic training loop 场景下测试；与 ECE 等轻量 canary 无对比\"\n    metrics_studied: [\"Collapse Index\", \"persistent homology features\"]\n\n  # ============================================================\n  # DIVERSITY METRICS (BACKGROUND)\n  # ============================================================"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "7f7fecd0-70c2-47f5-859e-0abdb20a732a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JJzXwrmDkVp6YNrBMB64fV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10452,
      "cache_read_input_tokens": 45696,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10452
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

_source line 49 · 2026-05-14T05:46:09.503Z_

<details><summary>↩ Tool result · `toolu_01UrWHuR36BK8tyk8ZgNKArU`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "cbbb4141-d77b-4857-9651-47e5a22d6c24",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/literature_map.yaml",
    "oldString": "    metrics_studied: [\"ECE\", \"accuracy\"]\n\n  # ============================================================\n  # DIVERSITY METRICS (BACKGROUND)\n  # ============================================================",
    "newString": "    metrics_studied: [\"ECE\", \"accuracy\"]\n\n  - id: \"sigma2026spectral\"\n    title: \"SIGMA: Scalable Spectral Insights for LLM Model Collapse\"\n    authors: \"Yi Gu, Lingyou Pang, Xiangkun Ye, Tianyu Wang, Jianyu Lin, Carey E. Priebe, Alexander Aue\"\n    venue: \"arXiv (2601.03385)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2601.03385\"\n    category: \"canary-metrics\"\n    role: \"direct-competitor\"\n    key_findings:\n      - \"基于 embedding Gram matrix 谱分析的 collapse 监控框架：Track I（确定性谱界）保守但鲁棒，Track II（随机谱缩放）灵敏但需采样\"\n      - \"Track I/II 的分歧本身是 early-stage collapse 的诊断信号，早于表面重复性伪影\"\n      - \"随机谱界使部分观测的 Gram matrix 也可用于大规模模型的可扩展监控\"\n    relevance_to_us: \"最直接的 spectral canary 竞争者。我们的 effective rank 是其简化版（单一标量 vs 完整谱界）；需在 related work 中明确差异：SIGMA 提供双轨谱界，我们用单一 effective rank 换取更低计算开销和多指标 panel 集成\"\n    gaps: \"未做 lead-lag 分析，未与 ECE/diversity 等非谱指标对比；Track I/II 的计算开销在 iterative loop 多轮场景下可能不可忽略\"\n    metrics_studied: [\"Gram matrix eigenspectrum\", \"spectral norm bounds\"]\n\n  - id: \"kalinowski2026topology\"\n    title: \"Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index\"\n    authors: \"Alexander Kalinowski\"\n    venue: \"arXiv (2604.26984)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2604.26984\"\n    category: \"canary-metrics\"\n    role: \"background\"\n    key_findings:\n      - \"提出基于 Modular Morse Homology Maintenance (MMHM) 的在线拓扑监控方案，增量更新避免每轮重建\"\n      - \"Collapse Index (CI) 组合多尺度拓扑特征，在 LLM fine-tuning 和 temporal KGE 训练中提供低延迟 early-warning\"\n      - \"拓扑方法捕捉表示空间的各向异性和多尺度结构丧失\"\n    relevance_to_us: \"topology-based monitoring 是与 spectral 方法正交的 collapse 检测路线。我们排除了该方法（计算开销高、可解释性弱），但 related work 需要对比说明选择 spectral/calibration panel 而非 topology 的理由\"\n    gaps: \"计算开销显著高于 effective rank 等标量指标；未在 iterative synthetic training loop 场景下测试；与 ECE 等轻量 canary 无对比\"\n    metrics_studied: [\"Collapse Index\", \"persistent homology features\"]\n\n  # ============================================================\n  # DIVERSITY METRICS (BACKGROUND)\n  # ============================================================",
    "originalFile": "papers:\n  # ============================================================\n  # CORE MODEL COLLAPSE\n  # ============================================================\n  - id: \"shumailov2024curse\"\n    title: \"The Curse of Recursion: Training on Generated Data Makes Models Forget\"\n    authors: \"Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Yarin Gal, Nicolas Papernot, Ross Anderson\"\n    venue: \"Nature\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2305.17493\"\n    category: \"core-collapse\"\n    role: \"foundation\"\n    key_findings:\n      - \"定义 model collapse 现象：迭代用合成数据替换真实数据训练会导致分布尾部消失\"\n      - \"区分 early model collapse（尾部信息丢失）和 late model collapse（分布完全收敛）\"\n      - \"三类误差来源：statistical approximation, functional expressivity, functional approximation，跨代复合\"\n      - \"在 VAE、GMM、LLM 上均验证了 collapse 的普遍性\"\n    relevance_to_us: \"奠基论文，定义了我们研究的核心现象。我们的 canary 指标旨在提前检测其描述的 early collapse 阶段\"\n    metrics_studied: [\"perplexity\", \"distributional tail mass\"]\n\n  - id: \"alemohammad2024mad\"\n    title: \"Self-Consuming Generative Models Go MAD\"\n    authors: \"Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, Richard Baraniuk\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2307.01850\"\n    category: \"core-collapse\"\n    role: \"foundation\"\n    key_findings:\n      - \"提出 Model Autophagy Disorder (MAD) 概念\"\n      - \"autophagous loop 中没有足够新鲜真实数据时，质量或多样性必然渐进下降\"\n      - \"在图像生成领域验证 self-consuming loop 的退化效应\"\n    relevance_to_us: \"MAD 框架与我们的 iterative loop 设置直接对应；其 quality vs diversity tradeoff 可能反映在不同 canary 指标上\"\n    metrics_studied: [\"FID\", \"precision\", \"recall\", \"diversity\"]\n\n  - id: \"dohmatob2024tale\"\n    title: \"A Tale of Tails: Model Collapse as a Change of Scaling Laws\"\n    authors: \"Elvis Dohmatob, Yunzhen Feng, et al.\"\n    venue: \"ICML 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2402.07043\"\n    category: \"core-collapse\"\n    role: \"foundation\"\n    key_findings:\n      - \"通过 scaling laws 视角分析 model collapse：collapse 表现为 scaling law 的变化\"\n      - \"发现 loss of scaling, shifted scaling, skill un-learning, grokking 等多种退化模式\"\n      - \"混入少量干净数据可缓解 collapse 并引发 grokking 现象\"\n      - \"在 transformer 算术任务和 Llama2 文本生成上验证\"\n    relevance_to_us: \"scaling law 变化视角为我们提供了理论基础；grokking 现象暗示 canary 指标可能出现非单调行为\"\n    metrics_studied: [\"test loss\", \"scaling exponents\"]\n\n  - id: \"dohmatob2025strong\"\n    title: \"Strong Model Collapse\"\n    authors: \"Elvis Dohmatob, Yunzhen Feng, Arjun Subramonian, Julia Kempe\"\n    venue: \"ICLR 2025 (Spotlight)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2410.04840\"\n    category: \"core-collapse\"\n    role: \"foundation\"\n    key_findings:\n      - \"即使合成数据占比极小（1/1000），仍可导致 model collapse\"\n      - \"更大的训练集并不能避免 collapse\"\n      - \"更大的模型（random projection 近似下）反而可能放大 collapse\"\n      - \"存在 interpolation threshold 的 double-descent 现象\"\n    relevance_to_us: \"强化了早期检测的必要性——即使极小的合成数据比例也能触发 collapse，因此 canary 指标必须敏感\"\n    metrics_studied: [\"test loss\", \"population risk\"]\n\n  - id: \"guo2024linguistic\"\n    title: \"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\"\n    authors: \"Yanzhu Guo, Guokan Shang, et al.\"\n    venue: \"NAACL 2024 Findings\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2311.09807\"\n    category: \"core-collapse\"\n    role: \"evaluation\"\n    key_findings:\n      - \"递归微调中，linguistic diversity 在连续迭代中持续下降\"\n      - \"创造性任务中 diversity 下降最显著\"\n      - \"开发了覆盖 lexical、syntactic、semantic 三层的 diversity 指标体系\"\n    relevance_to_us: \"其多层 diversity 指标体系可直接作为我们 canary 指标的候选集；创造性 vs 事实任务的差异可能影响 canary 灵敏度\"\n    metrics_studied: [\"distinct-n\", \"type-token ratio\", \"syntactic diversity\", \"semantic diversity\"]\n\n  - id: \"briesch2024selfconsuming\"\n    title: \"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop\"\n    authors: \"Martin Briesch, Dominik Sobania, Franz Rothlauf\"\n    venue: \"arXiv (2311.16822)\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2311.16822\"\n    category: \"core-collapse\"\n    role: \"direct-competitor\"\n    key_findings:\n      - \"首次系统研究 LLM 的 self-consuming training loop\"\n      - \"full synthetic cycle（完全替换）导致单点 collapse；data augmentation cycle 导致 diversity 缓慢下降\"\n      - \"expanding data cycle（累积）在 50 代内保持 diversity\"\n    relevance_to_us: \"其不同 data cycle 策略的对比直接对应我们的 alpha（synthetic ratio）实验设置\"\n    metrics_studied: [\"diversity\", \"quality\"]\n\n  - id: \"truong2025entropy\"\n    title: \"Entropy Collapse: A Universal Failure Mode of Intelligent Systems\"\n    authors: \"Truong Xuan Khanh, Truong Quynh Hoa\"\n    venue: \"arXiv (2512.12381)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2512.12381\"\n    category: \"core-collapse\"\n    role: \"theoretical-foundation\"\n    key_findings:\n      - \"证明 entropy collapse 是一阶（不连续）相变，临界点 α_c(β) = 1/(1−β)，entropy 在临界点跳变 0.698 nats\"\n      - \"两个 universality class：Class 1（凸反馈，如 power-law）不可逆 ν=1；Class 2（线性反馈）可逆 ν=1/2\"\n      - \"因为是一阶相变，autocorrelation/variance 等传统 early-warning signal 在 collapse 前保持有限——无预警\"\n    relevance_to_us: \"定义了 canary 失效的 regime boundary：Class 1 凸反馈系统中传统 canary 理论上无效。我们需证明我们的 canary 在 Class 2+ regime 或非纯反馈场景中有效\"\n    gaps: \"理论框架高度抽象，未给出 LLM 具体场景下的 α/β 估计方法；未测试哪些 canary 在接近一阶相变时仍有部分预警能力\"\n    metrics_studied: [\"entropy\", \"autocorrelation\", \"variance\"]\n\n  - id: \"wang2026contaminated\"\n    title: \"Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training\"\n    authors: \"Kevin Wang, Hongqian Niu, Didong Li\"\n    venue: \"arXiv (2602.16065)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2602.16065\"\n    category: \"core-collapse\"\n    role: \"theoretical-foundation\"\n    key_findings:\n      - \"首个不限数据分布假设的正面理论结果：universal approximator 下 contaminated recursive training 仍可收敛\"\n      - \"收敛速率 = min(baseline 模型收敛速率, 每轮真实数据比例)——真实数据比例是瓶颈\"\n      - \"突破了先前仅限 discrete/Gaussian 分布的理论框架，适用于一般连续分布\"\n    relevance_to_us: \"为 post-MVP α-sweep 实验提供理论上界：收敛速率由 real data fraction 决定，可预测不同 α 下的 collapse 速率\"\n    gaps: \"universal approximator 假设在实际有限容量模型中不严格成立；未讨论 canary 指标行为\"\n    metrics_studied: [\"convergence rate\", \"population risk\"]\n\n  # ============================================================\n  # CANARY / EARLY WARNING METRICS\n  # ============================================================\n  - id: \"chen2025scales\"\n    title: \"Characterizing Model Behavior Under Synthetic Data Training: An Empirical Study Across Scales and Mixing Ratios\"\n    authors: \"Anonymous\"\n    venue: \"arXiv (2510.05133)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.05133\"\n    category: \"canary-metrics\"\n    role: \"direct-competitor\"\n    key_findings:\n      - \"**Calibration degradation precedes accuracy loss** — ECE 是 collapse 的 early warning signal\"\n      - \"20% synthetic data 以下性能稳定，30% 以上退化加速\"\n      - \"大模型（6.9B-12B）比小模型（410M-1.4B）更鲁棒\"\n      - \"推理任务比检索任务更易退化\"\n      - \"iteration 1 + 30% synthetic 时 ECE 从 0.08 升至 0.14（+75%）\"\n    relevance_to_us: \"**最直接的竞争者/先驱**。证实 ECE 可作为 canary，但未做 lead-lag 分析，未建立多指标 panel 框架\"\n    metrics_studied: [\"ECE\", \"accuracy\", \"perplexity\"]\n\n  - id: \"gambetta2024surplexity\"\n    title: \"Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI\"\n    authors: \"Daniele Gambetta et al.\"\n    venue: \"arXiv (2410.12341)\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2410.12341\"\n    category: \"canary-metrics\"\n    role: \"direct-competitor\"\n    key_findings:\n      - \"提出 surplexity（model surprise 度量）同时用于检测 collapse 和过滤训练数据\"\n      - \"用 semantic networks 分析文本重复性和语义多样性\"\n      - \"用 next-token probability 定量衡量 diversity loss\"\n      - \"高 surplexity 过滤策略至少与 human-data baseline 同效，且更能降低分布偏斜\"\n      - \"不需要区分 human vs AI-generated data\"\n    relevance_to_us: \"surplexity 可作为我们 canary 指标候选之一；其 semantic network 方法提供了 diversity 度量的另一视角\"\n    metrics_studied: [\"surplexity\", \"semantic network metrics\", \"next-token probability\"]\n\n  - id: \"qiu2025spectral\"\n    title: \"Spectral Alignment as Predictor of Loss Explosion in Neural Network Training\"\n    authors: \"Haiquan Qiu, You Wu, Yingjie Tan, Yaqing Wang, Quanming Yao\"\n    venue: \"arXiv (2510.04202)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.04202\"\n    category: \"canary-metrics\"\n    role: \"method-component\"\n    key_findings:\n      - \"Spectral Alignment (SA) 监控层输入与权重矩阵主奇异向量的分布对齐\"\n      - \"SA sign diversity collapse 是 representational collapse 和训练发散的早期预测器\"\n      - \"比 weight norm、gradient norm 等传统指标更早、更清晰地检测到训练失败\"\n      - \"健康层的 SA 应有正负均衡分布，collapse 到单侧则预示不稳定\"\n    relevance_to_us: \"SA 是潜在的高价值 canary 指标——专门设计为 early warning，可直接纳入我们的指标 panel\"\n    metrics_studied: [\"spectral alignment\", \"weight norm\", \"gradient norm\"]\n\n  - id: \"he2025closer\"\n    title: \"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\"\n    authors: \"Shiliang He et al.\"\n    venue: \"NeurIPS 2025 (Spotlight)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2509.16499\"\n    category: \"canary-metrics\"\n    role: \"direct-competitor\"\n    key_findings:\n      - \"识别 diffusion model collapse 中的 generalization → memorization 转变\"\n      - \"**训练数据的 entropy 递减是 collapse 的直接驱动因素和清晰指标**\"\n      - \"提出基于 entropy 的数据选择策略，有效缓解 collapse\"\n    relevance_to_us: \"data entropy 作为 canary 的有效性已被验证（diffusion domain）；需测试是否在 LLM 场景同样有效\"\n    metrics_studied: [\"entropy\", \"FID\", \"diversity\"]\n\n  - id: \"ba2024fill\"\n    title: \"Fill In The Gaps: Model Calibration and Generalization with Synthetic Data\"\n    authors: \"Yang Ba, Michelle V Mancenido, Rong Pan\"\n    venue: \"EMNLP 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2410.10864\"\n    category: \"canary-metrics\"\n    role: \"background\"\n    key_findings:\n      - \"用 LLM 生成合成数据来修复 calibration 错误的 reliability diagram bins\"\n      - \"推导了基于 PAC 框架的 ECE bound\"\n      - \"合成数据可改善 calibration 但需精心设计生成策略\"\n    relevance_to_us: \"ECE 的理论 bound 可为我们的 canary 阈值设定提供理论依据\"\n    metrics_studied: [\"ECE\", \"accuracy\"]\n\n  # ============================================================\n  # DIVERSITY METRICS (BACKGROUND)\n  # ============================================================\n  - id: \"zhu2018texygen\"\n    title: \"Texygen: A Benchmarking Platform for Text Generation Models\"\n    authors: \"Yaoming Zhu et al.\"\n    venue: \"SIGIR 2018\"\n    year: 2018\n    url: \"https://arxiv.org/abs/1802.01886\"\n    category: \"canary-metrics\"\n    role: \"background\"\n    key_findings:\n      - \"提出 Self-BLEU 度量：计算生成句子间的 BLEU 相似度，Self-BLEU 越高多样性越低\"\n      - \"成为文本生成多样性评估的标准基准之一\"\n    relevance_to_us: \"Self-BLEU 是我们 diversity canary 的经典候选\"\n    metrics_studied: [\"Self-BLEU\", \"BLEU\"]\n\n  - id: \"li2016diversity\"\n    title: \"A Diversity-Promoting Objective Function for Neural Conversation Models\"\n    authors: \"Jiwei Li et al.\"\n    venue: \"NAACL 2016\"\n    year: 2016\n    url: \"https://arxiv.org/abs/1510.03055\"\n    category: \"canary-metrics\"\n    role: \"background\"\n    key_findings:\n      - \"提出 distinct-1 / distinct-2 指标衡量生成文本的 n-gram 多样性\"\n      - \"计算 unique n-gram 数占总 n-gram 数的比例\"\n    relevance_to_us: \"distinct-n 是最廉价的 diversity canary 之一，计算开销极低\"\n    metrics_studied: [\"distinct-1\", \"distinct-2\"]\n\n  # ============================================================\n  # REPRESENTATION / SPECTRAL COLLAPSE\n  # ============================================================\n  - id: \"jing2022understanding\"\n    title: \"Understanding Dimensional Collapse in Contrastive Self-supervised Learning\"\n    authors: \"Li Jing et al.\"\n    venue: \"ICLR 2022\"\n    year: 2022\n    url: \"https://openreview.net/forum?id=YevsQ05DEN7\"\n    category: \"canary-metrics\"\n    role: \"method-component\"\n    key_findings:\n      - \"定义 dimensional collapse：embedding 向量只跨越低维子空间\"\n      - \"effective rank（基于归一化特征值 entropy 的指数）作为 collapse 度量\"\n      - \"strong augmentation 和 implicit regularization 驱动低秩解\"\n    relevance_to_us: \"effective rank 的定义和计算方式可直接迁移到我们的 embedding 空间监控\"\n    metrics_studied: [\"effective rank\", \"singular value spectrum\"]\n\n  - id: \"noci2024mind\"\n    title: \"Mind the Gap: A Spectral Analysis of Rank Collapse and Signal Propagation in Transformers\"\n    authors: \"Lorenzo Noci et al.\"\n    venue: \"NeurIPS 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2410.07799\"\n    category: \"canary-metrics\"\n    role: \"method-component\"\n    key_findings:\n      - \"用 Random Matrix Theory 分析 attention 层的 rank collapse\"\n      - \"发现 attention matrix 最大两个奇异值之间的 spectral gap 是 width-collapse 的根因\"\n      - \"rank collapse in depth: 所有 token 沿层收敛到单一表示\"\n    relevance_to_us: \"spectral gap 作为另一种 spectral canary 候选；其 RMT 分析框架可启发我们的理论工作\"\n    metrics_studied: [\"spectral gap\", \"singular values\", \"effective rank\"]\n\n  # ============================================================\n  # DATA MIXING & ACCUMULATION\n  # ============================================================\n  - id: \"kazdan2025collapse\"\n    title: \"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World\"\n    authors: \"Joshua Kazdan, Rylan Schaeffer, Apratim Dey, Matthias Gerstgrasser, Rafael Rafailov, David L. Donoho, Sanmi Koyejo\"\n    venue: \"ICML 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2410.16713\"\n    category: \"data-mixing\"\n    role: \"foundation\"\n    key_findings:\n      - \"系统对比 replace vs accumulate 场景\"\n      - \"replace → collapse；accumulate → 可避免 collapse\"\n      - \"发现 real data 和 synthetic data 之间存在非平凡的交互效应\"\n      - \"synthetic data 的价值取决于 real data 的绝对数量\"\n    relevance_to_us: \"直接对应我们的 alpha（mixing ratio）实验维度；其 replace vs accumulate 框架是我们实验设计的重要参考\"\n    metrics_studied: [\"test loss\"]\n\n  - id: \"dey2024breaking\"\n    title: \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\"\n    authors: \"Apratim Dey, David Donoho, et al.\"\n    venue: \"ICML 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2404.01413\"\n    category: \"data-mixing\"\n    role: \"foundation\"\n    key_findings:\n      - \"替换数据 → 发散 population risk；累积数据 → 避免发散\"\n      - \"证明累积策略在多种模型（GMM, HMM, LLM）上有效\"\n    relevance_to_us: \"为我们的 alpha 实验提供理论预测：累积 vs 替换是 collapse 速率的关键调节因子\"\n    metrics_studied: [\"population risk\"]\n\n  - id: \"epstein2024howbad\"\n    title: \"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse\"\n    authors: \"Mohamed El Amine Epstein et al.\"\n    venue: \"arXiv (2404.05090)\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2404.05090\"\n    category: \"data-mixing\"\n    role: \"background\"\n    key_findings:\n      - \"纯合成数据训练不可避免 collapse\"\n      - \"给出 synthetic data 比例上界的估计——低于此比例可避免 collapse\"\n      - \"递归训练使原始分布尾部消失\"\n    relevance_to_us: \"其 mixing ratio 上界估计可对比我们实验中观测到的 canary 触发阈值\"\n    metrics_studied: [\"perplexity\"]\n\n  - id: \"bakshi2026improvement\"\n    title: \"From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources\"\n    authors: \"Soham Bakshi et al.\"\n    venue: \"arXiv (2602.10531)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2602.10531\"\n    category: \"data-mixing\"\n    role: \"background\"\n    key_findings:\n      - \"即使真实数据比例随时间衰减，只要非零就可能避免 collapse 并恢复真实分布\"\n      - \"在 next-token prediction 语言模型上分析混合训练的动态\"\n    relevance_to_us: \"提供了 decaying real data fraction 的理论保证，与我们的实验中 alpha 变化场景相关\"\n    metrics_studied: [\"population risk\"]\n\n  # ============================================================\n  # MITIGATION & VERIFICATION\n  # ============================================================\n  - id: \"feng2025escaping\"\n    title: \"Escaping Model Collapse via Synthetic Data Verification\"\n    authors: \"Yunzhen Feng et al.\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.16657\"\n    category: \"data-mixing\"\n    role: \"background\"\n    key_findings:\n      - \"通过外部 verifier（human 或 better model）注入信息可避免 collapse\"\n      - \"verifier-guided retraining 带来短期改善，但最终收敛到 verifier 的 knowledge center\"\n      - \"除非 verifier 完全可靠，早期收益会 plateau 甚至逆转\"\n    relevance_to_us: \"verification 作为 intervention 策略——如果 canary 触发，可考虑此类 reactive intervention\"\n    metrics_studied: [\"test loss\"]\n\n  - id: \"barzilai2025consistency\"\n    title: \"When Models Don't Collapse: On the Consistency of Iterative MLE\"\n    authors: \"Daniel Barzilai, Ohad Shamir\"\n    venue: \"ICML 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2505.19046\"\n    category: \"core-collapse\"\n    role: \"background\"\n    key_findings:\n      - \"在标准 MLE 一致性假设下，即使 real data fraction 趋近零也可避免 collapse\"\n      - \"但证明了某些情况下 collapse 可以任意快地发生——首次给出严格 collapse 反例\"\n    relevance_to_us: \"理论上的 collapse 可发生任意快的结论强化了 early warning 的价值\"\n    metrics_studied: []\n\n  - id: \"dces2026counter\"\n    title: \"Countering Model Collapse in Iterative Self-Training via Dynamic Center-Edge Sampling\"\n    authors: \"Anonymous\"\n    venue: \"MDPI Electronics (2026)\"\n    year: 2026\n    url: \"https://www.mdpi.com/2079-9292/15/4/869\"\n    category: \"data-mixing\"\n    role: \"background\"\n    key_findings:\n      - \"提出 DCES（dynamic center-edge sampling）数据选择框架\"\n      - \"DCES 在 ECE（0.1058 vs 0.1200）和 entropy 保持上优于随机选择\"\n    relevance_to_us: \"其 ECE 和 entropy 对比数据为我们的指标 baseline 提供参考\"\n    metrics_studied: [\"ECE\", \"entropy\"]\n\n  # ============================================================\n  # POSITION / SURVEY / EPISTEMICS\n  # ============================================================\n  - id: \"schaeffer2025position\"\n    title: \"Position: Model Collapse Does Not Mean What You Think\"\n    authors: \"Rylan Schaeffer, Joshua Kazdan, Alvan Caleb Arulandu, Sanmi Koyejo\"\n    venue: \"arXiv (2503.03150)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2503.03150\"\n    category: \"core-collapse\"\n    role: \"background\"\n    key_findings:\n      - \"文献中实际包含 8 种不同且有时矛盾的 model collapse 定义\"\n      - \"许多 collapse 预测依赖于与现实不符的假设\"\n      - \"多种 collapse 场景是可以轻易避免的\"\n    relevance_to_us: \"提醒我们明确定义 collapse 的操作标准；不同定义可能需要不同的 canary 指标\"\n    metrics_studied: []\n\n  - id: \"wang2025epistemic\"\n    title: \"Epistemic Diversity and Knowledge Collapse in Large Language Models\"\n    authors: \"Wang et al.\"\n    venue: \"arXiv (2510.04226)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.04226\"\n    category: \"core-collapse\"\n    role: \"background\"\n    key_findings:\n      - \"27 个 LLM 在 155 个主题上的 epistemic diversity 评估\"\n      - \"所有模型的 epistemic diversity 低于基本 web 搜索\"\n      - \"模型越大 epistemic diversity 反而越低；RAG 有正面效果\"\n    relevance_to_us: \"knowledge collapse 维度可扩展我们对 diversity canary 的理解——不仅是 lexical/syntactic 还有 epistemic\"\n    metrics_studied: [\"epistemic diversity\"]\n\n  # ============================================================\n  # METHODOLOGY (GRANGER / LEAD-LAG)\n  # ============================================================\n  - id: \"shojaie2022granger\"\n    title: \"Granger Causality: A Review and Recent Advances\"\n    authors: \"Ali Shojaie, Emily B. Fox\"\n    venue: \"Annual Review of Statistics and Its Application\"\n    year: 2022\n    url: \"https://arxiv.org/abs/2105.02675\"\n    category: \"methodology\"\n    role: \"method-component\"\n    key_findings:\n      - \"Granger causality 综述：从经典线性到非线性/neural 方法\"\n      - \"Panel data 场景的 Granger causality 扩展\"\n      - \"VAR 和 neural Granger causality 的对比\"\n    relevance_to_us: \"为我们的 panel Granger causality 分析提供方法论基础\"\n    metrics_studied: []\n\n  - id: \"marcinkevics2022neural\"\n    title: \"Granger Causality Using Neural Networks\"\n    authors: \"Raphael Marcinkevics, Julia Vogt\"\n    venue: \"arXiv (2208.03703)\"\n    year: 2022\n    url: \"https://arxiv.org/abs/2208.03703\"\n    category: \"methodology\"\n    role: \"method-component\"\n    key_findings:\n      - \"用 neural network 估计 Granger causality，突破线性假设\"\n      - \"两个模型对比法：含/不含外生变量的预测误差差异即 Granger causality 证据\"\n    relevance_to_us: \"我们的多指标时序可能存在非线性关系，neural Granger causality 是自然选择\"\n    metrics_studied: []\n\ngaps:\n  - \"无人系统做过 canary 指标的 lead-lag / Granger causality 分析——现有工作只在事后观察到指标变化，未量化哪些指标能提前多少步预测 collapse\"\n  - \"ECE 在 collapse 场景下几乎未被系统研究——chen2025scales 是唯一报告 ECE 先于 accuracy 退化的工作，但未做因果分析\"\n  - \"embedding effective rank 未在 iterative synthetic training 场景下被测试——仅在 contrastive learning/transformer 训练中研究过\"\n  - \"多指标 panel 框架缺失——无人同时追踪 ECE + effective rank + diversity + perplexity 的时序行为并分析其 lead-lag 关系\"\n  - \"alpha（synthetic ratio）对 canary 灵敏度的影响未被研究——现有工作只关注 alpha 对最终性能的影响，不关注 canary 的 lead time 如何随 alpha 变化\"\n  - \"predictive intervention vs reactive intervention 缺少对比——没有工作量化 early warning 带来的实际干预收益\"\n  - \"surplexity 和 spectral alignment 未在 iterative collapse 场景下交叉验证\"\n  - \"跨任务 canary 普适性未知——reasoning vs retrieval vs creative tasks 中哪些 canary 更可靠\"\n\nnovelty_assessment: |\n  我们项目的核心 novelty 在于：\n\n  1. **Panel Granger Causality 框架**：首次将多指标时序数据的因果分析方法应用于 model collapse 早期预警。\n     现有工作（chen2025scales, gambetta2024surplexity）只是事后观察到某些指标先变化，\n     但没有人做过系统的 lead-lag 量化分析。\n\n  2. **多指标 Canary Panel**：同时追踪 ECE、effective rank、Self-BLEU/distinct-n、\n     perplexity、entropy、surplexity 等指标，分析其相互关系和各自的 lead time。\n     现有工作都是单一指标或最多两三个指标的孤立分析。\n\n  3. **alpha-dependent Canary Sensitivity**：系统研究 synthetic ratio 如何影响各 canary\n     指标的灵敏度和 lead time。dohmatob2025strong 证明极小的 alpha 就能触发 collapse，\n     但没人研究 canary 在不同 alpha 下的行为。\n\n  4. **与已有工作的差异**：\n     - vs chen2025scales: 他们发现 ECE 先退化但没有做因果分析；我们用 Granger causality 量化\n     - vs gambetta2024surplexity: 他们提出 surplexity 用于检测和缓解 collapse；\n       我们将其纳入更广的 panel 并研究其 lead-lag 特性\n     - vs he2025closer: 他们在 diffusion 中用 entropy 作为指标；我们在 LLM 中测试更多指标\n     - vs qiu2025spectral: 他们的 SA 用于训练 loss explosion 预警；\n       我们将类似思路迁移到 iterative collapse 场景\n\n  5. **潜在风险**：chen2025scales 已经非常接近我们的方向。如果他们扩展到 lead-lag 分析，\n     我们的 novelty 会被削弱。需要快速推进并在方法论（Granger causality）上建立壁垒。\n",
    "structuredPatch": [
      {
        "oldStart": 210,
        "oldLines": 6,
        "newStart": 210,
        "newLines": 38,
        "lines": [
          "     relevance_to_us: \"ECE 的理论 bound 可为我们的 canary 阈值设定提供理论依据\"",
          "     metrics_studied: [\"ECE\", \"accuracy\"]",
          " ",
          "+  - id: \"sigma2026spectral\"",
          "+    title: \"SIGMA: Scalable Spectral Insights for LLM Model Collapse\"",
          "+    authors: \"Yi Gu, Lingyou Pang, Xiangkun Ye, Tianyu Wang, Jianyu Lin, Carey E. Priebe, Alexander Aue\"",
          "+    venue: \"arXiv (2601.03385)\"",
          "+    year: 2026",
          "+    url: \"https://arxiv.org/abs/2601.03385\"",
          "+    category: \"canary-metrics\"",
          "+    role: \"direct-competitor\"",
          "+    key_findings:",
          "+      - \"基于 embedding Gram matrix 谱分析的 collapse 监控框架：Track I（确定性谱界）保守但鲁棒，Track II（随机谱缩放）灵敏但需采样\"",
          "+      - \"Track I/II 的分歧本身是 early-stage collapse 的诊断信号，早于表面重复性伪影\"",
          "+      - \"随机谱界使部分观测的 Gram matrix 也可用于大规模模型的可扩展监控\"",
          "+    relevance_to_us: \"最直接的 spectral canary 竞争者。我们的 effective rank 是其简化版（单一标量 vs 完整谱界）；需在 related work 中明确差异：SIGMA 提供双轨谱界，我们用单一 effective rank 换取更低计算开销和多指标 panel 集成\"",
          "+    gaps: \"未做 lead-lag 分析，未与 ECE/diversity 等非谱指标对比；Track I/II 的计算开销在 iterative loop 多轮场景下可能不可忽略\"",
          "+    metrics_studied: [\"Gram matrix eigenspectrum\", \"spectral norm bounds\"]",
          "+",
          "+  - id: \"kalinowski2026topology\"",
          "+    title: \"Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index\"",
          "+    authors: \"Alexander Kalinowski\"",
          "+    venue: \"arXiv (2604.26984)\"",
          "+    year: 2026",
          "+    url: \"https://arxiv.org/abs/2604.26984\"",
          "+    category: \"canary-metrics\"",
          "+    role: \"background\"",
          "+    key_findings:",
          "+      - \"提出基于 Modular Morse Homology Maintenance (MMHM) 的在线拓扑监控方案，增量更新避免每轮重建\"",
          "+      - \"Collapse Index (CI) 组合多尺度拓扑特征，在 LLM fine-tuning 和 temporal KGE 训练中提供低延迟 early-warning\"",
          "+      - \"拓扑方法捕捉表示空间的各向异性和多尺度结构丧失\"",
          "+    relevance_to_us: \"topology-based monitoring 是与 spectral 方法正交的 collapse 检测路线。我们排除了该方法（计算开销高、可解释性弱），但 related work 需要对比说明选择 spectral/calibration panel 而非 topology 的理由\"",
          "+    gaps: \"计算开销显著高于 effective rank 等标量指标；未在 iterative synthetic training loop 场景下测试；与 ECE 等轻量 canary 无对比\"",
          "+    metrics_studied: [\"Collapse Index\", \"persistent homology features\"]",
          "+",
          "   # ============================================================",
          "   # DIVERSITY METRICS (BACKGROUND)",
          "   # ============================================================"
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

### Tool call

_source line 50_

<details open><summary>🔧 Tool call — Edit · `toolu_01CKHea6qge6hFci5DoC7zGV`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/literature_map.yaml",
  "old_string": "    metrics_studied: [\"perplexity\"]\n\n  - id: \"bakshi2026improvement\"",
  "new_string": "    metrics_studied: [\"perplexity\"]\n\n  - id: \"fu2025selfconsuming\"\n    title: \"A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops\"\n    authors: \"Shi Fu, Yingjie Wang, Yuzhu Chen, Xinmei Tian, Dacheng Tao\"\n    venue: \"ICLR 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2502.18865\"\n    category: \"data-mixing\"\n    role: \"theoretical-foundation\"\n    key_findings:\n      - \"引入 recursive stability 概念，首次给出 self-consuming loop 的泛化分析\"\n      - \"恒定比例的真实数据即可保证 STL 收敛；同时给出最优合成数据量的 insight\"\n      - \"模型架构和 real/synthetic 数据比例共同决定 STL 的成败\"\n    relevance_to_us: \"为 post-MVP α-sweep（synthetic ratio 梯度）实验提供理论预期：50% accumulation 条件下收敛有理论保证\"\n    gaps: \"理论分析限于特定 generalization bound 框架，未涉及 canary 指标的行为；未讨论不同 α 下 collapse 速率的精细结构\"\n    metrics_studied: [\"generalization bound\", \"population risk\"]\n\n  - id: \"bakshi2026improvement\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "cb99eb24-e1b4-462d-b708-5e678454b60d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JJzXwrmDkVp6YNrBMB64fV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10452,
      "cache_read_input_tokens": 45696,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10452
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

_source line 51 · 2026-05-14T05:46:17.578Z_

<details><summary>↩ Tool result · `toolu_01CKHea6qge6hFci5DoC7zGV`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "2f20b3cd-1b94-4530-a837-99d9163acb85",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/literature_map.yaml",
    "oldString": "    metrics_studied: [\"perplexity\"]\n\n  - id: \"bakshi2026improvement\"",
    "newString": "    metrics_studied: [\"perplexity\"]\n\n  - id: \"fu2025selfconsuming\"\n    title: \"A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops\"\n    authors: \"Shi Fu, Yingjie Wang, Yuzhu Chen, Xinmei Tian, Dacheng Tao\"\n    venue: \"ICLR 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2502.18865\"\n    category: \"data-mixing\"\n    role: \"theoretical-foundation\"\n    key_findings:\n      - \"引入 recursive stability 概念，首次给出 self-consuming loop 的泛化分析\"\n      - \"恒定比例的真实数据即可保证 STL 收敛；同时给出最优合成数据量的 insight\"\n      - \"模型架构和 real/synthetic 数据比例共同决定 STL 的成败\"\n    relevance_to_us: \"为 post-MVP α-sweep（synthetic ratio 梯度）实验提供理论预期：50% accumulation 条件下收敛有理论保证\"\n    gaps: \"理论分析限于特定 generalization bound 框架，未涉及 canary 指标的行为；未讨论不同 α 下 collapse 速率的精细结构\"\n    metrics_studied: [\"generalization bound\", \"population risk\"]\n\n  - id: \"bakshi2026improvement\"",
    "originalFile": "papers:\n  # ============================================================\n  # CORE MODEL COLLAPSE\n  # ============================================================\n  - id: \"shumailov2024curse\"\n    title: \"The Curse of Recursion: Training on Generated Data Makes Models Forget\"\n    authors: \"Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Yarin Gal, Nicolas Papernot, Ross Anderson\"\n    venue: \"Nature\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2305.17493\"\n    category: \"core-collapse\"\n    role: \"foundation\"\n    key_findings:\n      - \"定义 model collapse 现象：迭代用合成数据替换真实数据训练会导致分布尾部消失\"\n      - \"区分 early model collapse（尾部信息丢失）和 late model collapse（分布完全收敛）\"\n      - \"三类误差来源：statistical approximation, functional expressivity, functional approximation，跨代复合\"\n      - \"在 VAE、GMM、LLM 上均验证了 collapse 的普遍性\"\n    relevance_to_us: \"奠基论文，定义了我们研究的核心现象。我们的 canary 指标旨在提前检测其描述的 early collapse 阶段\"\n    metrics_studied: [\"perplexity\", \"distributional tail mass\"]\n\n  - id: \"alemohammad2024mad\"\n    title: \"Self-Consuming Generative Models Go MAD\"\n    authors: \"Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, Richard Baraniuk\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2307.01850\"\n    category: \"core-collapse\"\n    role: \"foundation\"\n    key_findings:\n      - \"提出 Model Autophagy Disorder (MAD) 概念\"\n      - \"autophagous loop 中没有足够新鲜真实数据时，质量或多样性必然渐进下降\"\n      - \"在图像生成领域验证 self-consuming loop 的退化效应\"\n    relevance_to_us: \"MAD 框架与我们的 iterative loop 设置直接对应；其 quality vs diversity tradeoff 可能反映在不同 canary 指标上\"\n    metrics_studied: [\"FID\", \"precision\", \"recall\", \"diversity\"]\n\n  - id: \"dohmatob2024tale\"\n    title: \"A Tale of Tails: Model Collapse as a Change of Scaling Laws\"\n    authors: \"Elvis Dohmatob, Yunzhen Feng, et al.\"\n    venue: \"ICML 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2402.07043\"\n    category: \"core-collapse\"\n    role: \"foundation\"\n    key_findings:\n      - \"通过 scaling laws 视角分析 model collapse：collapse 表现为 scaling law 的变化\"\n      - \"发现 loss of scaling, shifted scaling, skill un-learning, grokking 等多种退化模式\"\n      - \"混入少量干净数据可缓解 collapse 并引发 grokking 现象\"\n      - \"在 transformer 算术任务和 Llama2 文本生成上验证\"\n    relevance_to_us: \"scaling law 变化视角为我们提供了理论基础；grokking 现象暗示 canary 指标可能出现非单调行为\"\n    metrics_studied: [\"test loss\", \"scaling exponents\"]\n\n  - id: \"dohmatob2025strong\"\n    title: \"Strong Model Collapse\"\n    authors: \"Elvis Dohmatob, Yunzhen Feng, Arjun Subramonian, Julia Kempe\"\n    venue: \"ICLR 2025 (Spotlight)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2410.04840\"\n    category: \"core-collapse\"\n    role: \"foundation\"\n    key_findings:\n      - \"即使合成数据占比极小（1/1000），仍可导致 model collapse\"\n      - \"更大的训练集并不能避免 collapse\"\n      - \"更大的模型（random projection 近似下）反而可能放大 collapse\"\n      - \"存在 interpolation threshold 的 double-descent 现象\"\n    relevance_to_us: \"强化了早期检测的必要性——即使极小的合成数据比例也能触发 collapse，因此 canary 指标必须敏感\"\n    metrics_studied: [\"test loss\", \"population risk\"]\n\n  - id: \"guo2024linguistic\"\n    title: \"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\"\n    authors: \"Yanzhu Guo, Guokan Shang, et al.\"\n    venue: \"NAACL 2024 Findings\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2311.09807\"\n    category: \"core-collapse\"\n    role: \"evaluation\"\n    key_findings:\n      - \"递归微调中，linguistic diversity 在连续迭代中持续下降\"\n      - \"创造性任务中 diversity 下降最显著\"\n      - \"开发了覆盖 lexical、syntactic、semantic 三层的 diversity 指标体系\"\n    relevance_to_us: \"其多层 diversity 指标体系可直接作为我们 canary 指标的候选集；创造性 vs 事实任务的差异可能影响 canary 灵敏度\"\n    metrics_studied: [\"distinct-n\", \"type-token ratio\", \"syntactic diversity\", \"semantic diversity\"]\n\n  - id: \"briesch2024selfconsuming\"\n    title: \"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop\"\n    authors: \"Martin Briesch, Dominik Sobania, Franz Rothlauf\"\n    venue: \"arXiv (2311.16822)\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2311.16822\"\n    category: \"core-collapse\"\n    role: \"direct-competitor\"\n    key_findings:\n      - \"首次系统研究 LLM 的 self-consuming training loop\"\n      - \"full synthetic cycle（完全替换）导致单点 collapse；data augmentation cycle 导致 diversity 缓慢下降\"\n      - \"expanding data cycle（累积）在 50 代内保持 diversity\"\n    relevance_to_us: \"其不同 data cycle 策略的对比直接对应我们的 alpha（synthetic ratio）实验设置\"\n    metrics_studied: [\"diversity\", \"quality\"]\n\n  - id: \"truong2025entropy\"\n    title: \"Entropy Collapse: A Universal Failure Mode of Intelligent Systems\"\n    authors: \"Truong Xuan Khanh, Truong Quynh Hoa\"\n    venue: \"arXiv (2512.12381)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2512.12381\"\n    category: \"core-collapse\"\n    role: \"theoretical-foundation\"\n    key_findings:\n      - \"证明 entropy collapse 是一阶（不连续）相变，临界点 α_c(β) = 1/(1−β)，entropy 在临界点跳变 0.698 nats\"\n      - \"两个 universality class：Class 1（凸反馈，如 power-law）不可逆 ν=1；Class 2（线性反馈）可逆 ν=1/2\"\n      - \"因为是一阶相变，autocorrelation/variance 等传统 early-warning signal 在 collapse 前保持有限——无预警\"\n    relevance_to_us: \"定义了 canary 失效的 regime boundary：Class 1 凸反馈系统中传统 canary 理论上无效。我们需证明我们的 canary 在 Class 2+ regime 或非纯反馈场景中有效\"\n    gaps: \"理论框架高度抽象，未给出 LLM 具体场景下的 α/β 估计方法；未测试哪些 canary 在接近一阶相变时仍有部分预警能力\"\n    metrics_studied: [\"entropy\", \"autocorrelation\", \"variance\"]\n\n  - id: \"wang2026contaminated\"\n    title: \"Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training\"\n    authors: \"Kevin Wang, Hongqian Niu, Didong Li\"\n    venue: \"arXiv (2602.16065)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2602.16065\"\n    category: \"core-collapse\"\n    role: \"theoretical-foundation\"\n    key_findings:\n      - \"首个不限数据分布假设的正面理论结果：universal approximator 下 contaminated recursive training 仍可收敛\"\n      - \"收敛速率 = min(baseline 模型收敛速率, 每轮真实数据比例)——真实数据比例是瓶颈\"\n      - \"突破了先前仅限 discrete/Gaussian 分布的理论框架，适用于一般连续分布\"\n    relevance_to_us: \"为 post-MVP α-sweep 实验提供理论上界：收敛速率由 real data fraction 决定，可预测不同 α 下的 collapse 速率\"\n    gaps: \"universal approximator 假设在实际有限容量模型中不严格成立；未讨论 canary 指标行为\"\n    metrics_studied: [\"convergence rate\", \"population risk\"]\n\n  # ============================================================\n  # CANARY / EARLY WARNING METRICS\n  # ============================================================\n  - id: \"chen2025scales\"\n    title: \"Characterizing Model Behavior Under Synthetic Data Training: An Empirical Study Across Scales and Mixing Ratios\"\n    authors: \"Anonymous\"\n    venue: \"arXiv (2510.05133)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.05133\"\n    category: \"canary-metrics\"\n    role: \"direct-competitor\"\n    key_findings:\n      - \"**Calibration degradation precedes accuracy loss** — ECE 是 collapse 的 early warning signal\"\n      - \"20% synthetic data 以下性能稳定，30% 以上退化加速\"\n      - \"大模型（6.9B-12B）比小模型（410M-1.4B）更鲁棒\"\n      - \"推理任务比检索任务更易退化\"\n      - \"iteration 1 + 30% synthetic 时 ECE 从 0.08 升至 0.14（+75%）\"\n    relevance_to_us: \"**最直接的竞争者/先驱**。证实 ECE 可作为 canary，但未做 lead-lag 分析，未建立多指标 panel 框架\"\n    metrics_studied: [\"ECE\", \"accuracy\", \"perplexity\"]\n\n  - id: \"gambetta2024surplexity\"\n    title: \"Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI\"\n    authors: \"Daniele Gambetta et al.\"\n    venue: \"arXiv (2410.12341)\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2410.12341\"\n    category: \"canary-metrics\"\n    role: \"direct-competitor\"\n    key_findings:\n      - \"提出 surplexity（model surprise 度量）同时用于检测 collapse 和过滤训练数据\"\n      - \"用 semantic networks 分析文本重复性和语义多样性\"\n      - \"用 next-token probability 定量衡量 diversity loss\"\n      - \"高 surplexity 过滤策略至少与 human-data baseline 同效，且更能降低分布偏斜\"\n      - \"不需要区分 human vs AI-generated data\"\n    relevance_to_us: \"surplexity 可作为我们 canary 指标候选之一；其 semantic network 方法提供了 diversity 度量的另一视角\"\n    metrics_studied: [\"surplexity\", \"semantic network metrics\", \"next-token probability\"]\n\n  - id: \"qiu2025spectral\"\n    title: \"Spectral Alignment as Predictor of Loss Explosion in Neural Network Training\"\n    authors: \"Haiquan Qiu, You Wu, Yingjie Tan, Yaqing Wang, Quanming Yao\"\n    venue: \"arXiv (2510.04202)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.04202\"\n    category: \"canary-metrics\"\n    role: \"method-component\"\n    key_findings:\n      - \"Spectral Alignment (SA) 监控层输入与权重矩阵主奇异向量的分布对齐\"\n      - \"SA sign diversity collapse 是 representational collapse 和训练发散的早期预测器\"\n      - \"比 weight norm、gradient norm 等传统指标更早、更清晰地检测到训练失败\"\n      - \"健康层的 SA 应有正负均衡分布，collapse 到单侧则预示不稳定\"\n    relevance_to_us: \"SA 是潜在的高价值 canary 指标——专门设计为 early warning，可直接纳入我们的指标 panel\"\n    metrics_studied: [\"spectral alignment\", \"weight norm\", \"gradient norm\"]\n\n  - id: \"he2025closer\"\n    title: \"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\"\n    authors: \"Shiliang He et al.\"\n    venue: \"NeurIPS 2025 (Spotlight)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2509.16499\"\n    category: \"canary-metrics\"\n    role: \"direct-competitor\"\n    key_findings:\n      - \"识别 diffusion model collapse 中的 generalization → memorization 转变\"\n      - \"**训练数据的 entropy 递减是 collapse 的直接驱动因素和清晰指标**\"\n      - \"提出基于 entropy 的数据选择策略，有效缓解 collapse\"\n    relevance_to_us: \"data entropy 作为 canary 的有效性已被验证（diffusion domain）；需测试是否在 LLM 场景同样有效\"\n    metrics_studied: [\"entropy\", \"FID\", \"diversity\"]\n\n  - id: \"ba2024fill\"\n    title: \"Fill In The Gaps: Model Calibration and Generalization with Synthetic Data\"\n    authors: \"Yang Ba, Michelle V Mancenido, Rong Pan\"\n    venue: \"EMNLP 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2410.10864\"\n    category: \"canary-metrics\"\n    role: \"background\"\n    key_findings:\n      - \"用 LLM 生成合成数据来修复 calibration 错误的 reliability diagram bins\"\n      - \"推导了基于 PAC 框架的 ECE bound\"\n      - \"合成数据可改善 calibration 但需精心设计生成策略\"\n    relevance_to_us: \"ECE 的理论 bound 可为我们的 canary 阈值设定提供理论依据\"\n    metrics_studied: [\"ECE\", \"accuracy\"]\n\n  - id: \"sigma2026spectral\"\n    title: \"SIGMA: Scalable Spectral Insights for LLM Model Collapse\"\n    authors: \"Yi Gu, Lingyou Pang, Xiangkun Ye, Tianyu Wang, Jianyu Lin, Carey E. Priebe, Alexander Aue\"\n    venue: \"arXiv (2601.03385)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2601.03385\"\n    category: \"canary-metrics\"\n    role: \"direct-competitor\"\n    key_findings:\n      - \"基于 embedding Gram matrix 谱分析的 collapse 监控框架：Track I（确定性谱界）保守但鲁棒，Track II（随机谱缩放）灵敏但需采样\"\n      - \"Track I/II 的分歧本身是 early-stage collapse 的诊断信号，早于表面重复性伪影\"\n      - \"随机谱界使部分观测的 Gram matrix 也可用于大规模模型的可扩展监控\"\n    relevance_to_us: \"最直接的 spectral canary 竞争者。我们的 effective rank 是其简化版（单一标量 vs 完整谱界）；需在 related work 中明确差异：SIGMA 提供双轨谱界，我们用单一 effective rank 换取更低计算开销和多指标 panel 集成\"\n    gaps: \"未做 lead-lag 分析，未与 ECE/diversity 等非谱指标对比；Track I/II 的计算开销在 iterative loop 多轮场景下可能不可忽略\"\n    metrics_studied: [\"Gram matrix eigenspectrum\", \"spectral norm bounds\"]\n\n  - id: \"kalinowski2026topology\"\n    title: \"Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index\"\n    authors: \"Alexander Kalinowski\"\n    venue: \"arXiv (2604.26984)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2604.26984\"\n    category: \"canary-metrics\"\n    role: \"background\"\n    key_findings:\n      - \"提出基于 Modular Morse Homology Maintenance (MMHM) 的在线拓扑监控方案，增量更新避免每轮重建\"\n      - \"Collapse Index (CI) 组合多尺度拓扑特征，在 LLM fine-tuning 和 temporal KGE 训练中提供低延迟 early-warning\"\n      - \"拓扑方法捕捉表示空间的各向异性和多尺度结构丧失\"\n    relevance_to_us: \"topology-based monitoring 是与 spectral 方法正交的 collapse 检测路线。我们排除了该方法（计算开销高、可解释性弱），但 related work 需要对比说明选择 spectral/calibration panel 而非 topology 的理由\"\n    gaps: \"计算开销显著高于 effective rank 等标量指标；未在 iterative synthetic training loop 场景下测试；与 ECE 等轻量 canary 无对比\"\n    metrics_studied: [\"Collapse Index\", \"persistent homology features\"]\n\n  # ============================================================\n  # DIVERSITY METRICS (BACKGROUND)\n  # ============================================================\n  - id: \"zhu2018texygen\"\n    title: \"Texygen: A Benchmarking Platform for Text Generation Models\"\n    authors: \"Yaoming Zhu et al.\"\n    venue: \"SIGIR 2018\"\n    year: 2018\n    url: \"https://arxiv.org/abs/1802.01886\"\n    category: \"canary-metrics\"\n    role: \"background\"\n    key_findings:\n      - \"提出 Self-BLEU 度量：计算生成句子间的 BLEU 相似度，Self-BLEU 越高多样性越低\"\n      - \"成为文本生成多样性评估的标准基准之一\"\n    relevance_to_us: \"Self-BLEU 是我们 diversity canary 的经典候选\"\n    metrics_studied: [\"Self-BLEU\", \"BLEU\"]\n\n  - id: \"li2016diversity\"\n    title: \"A Diversity-Promoting Objective Function for Neural Conversation Models\"\n    authors: \"Jiwei Li et al.\"\n    venue: \"NAACL 2016\"\n    year: 2016\n    url: \"https://arxiv.org/abs/1510.03055\"\n    category: \"canary-metrics\"\n    role: \"background\"\n    key_findings:\n      - \"提出 distinct-1 / distinct-2 指标衡量生成文本的 n-gram 多样性\"\n      - \"计算 unique n-gram 数占总 n-gram 数的比例\"\n    relevance_to_us: \"distinct-n 是最廉价的 diversity canary 之一，计算开销极低\"\n    metrics_studied: [\"distinct-1\", \"distinct-2\"]\n\n  # ============================================================\n  # REPRESENTATION / SPECTRAL COLLAPSE\n  # ============================================================\n  - id: \"jing2022understanding\"\n    title: \"Understanding Dimensional Collapse in Contrastive Self-supervised Learning\"\n    authors: \"Li Jing et al.\"\n    venue: \"ICLR 2022\"\n    year: 2022\n    url: \"https://openreview.net/forum?id=YevsQ05DEN7\"\n    category: \"canary-metrics\"\n    role: \"method-component\"\n    key_findings:\n      - \"定义 dimensional collapse：embedding 向量只跨越低维子空间\"\n      - \"effective rank（基于归一化特征值 entropy 的指数）作为 collapse 度量\"\n      - \"strong augmentation 和 implicit regularization 驱动低秩解\"\n    relevance_to_us: \"effective rank 的定义和计算方式可直接迁移到我们的 embedding 空间监控\"\n    metrics_studied: [\"effective rank\", \"singular value spectrum\"]\n\n  - id: \"noci2024mind\"\n    title: \"Mind the Gap: A Spectral Analysis of Rank Collapse and Signal Propagation in Transformers\"\n    authors: \"Lorenzo Noci et al.\"\n    venue: \"NeurIPS 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2410.07799\"\n    category: \"canary-metrics\"\n    role: \"method-component\"\n    key_findings:\n      - \"用 Random Matrix Theory 分析 attention 层的 rank collapse\"\n      - \"发现 attention matrix 最大两个奇异值之间的 spectral gap 是 width-collapse 的根因\"\n      - \"rank collapse in depth: 所有 token 沿层收敛到单一表示\"\n    relevance_to_us: \"spectral gap 作为另一种 spectral canary 候选；其 RMT 分析框架可启发我们的理论工作\"\n    metrics_studied: [\"spectral gap\", \"singular values\", \"effective rank\"]\n\n  # ============================================================\n  # DATA MIXING & ACCUMULATION\n  # ============================================================\n  - id: \"kazdan2025collapse\"\n    title: \"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World\"\n    authors: \"Joshua Kazdan, Rylan Schaeffer, Apratim Dey, Matthias Gerstgrasser, Rafael Rafailov, David L. Donoho, Sanmi Koyejo\"\n    venue: \"ICML 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2410.16713\"\n    category: \"data-mixing\"\n    role: \"foundation\"\n    key_findings:\n      - \"系统对比 replace vs accumulate 场景\"\n      - \"replace → collapse；accumulate → 可避免 collapse\"\n      - \"发现 real data 和 synthetic data 之间存在非平凡的交互效应\"\n      - \"synthetic data 的价值取决于 real data 的绝对数量\"\n    relevance_to_us: \"直接对应我们的 alpha（mixing ratio）实验维度；其 replace vs accumulate 框架是我们实验设计的重要参考\"\n    metrics_studied: [\"test loss\"]\n\n  - id: \"dey2024breaking\"\n    title: \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\"\n    authors: \"Apratim Dey, David Donoho, et al.\"\n    venue: \"ICML 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2404.01413\"\n    category: \"data-mixing\"\n    role: \"foundation\"\n    key_findings:\n      - \"替换数据 → 发散 population risk；累积数据 → 避免发散\"\n      - \"证明累积策略在多种模型（GMM, HMM, LLM）上有效\"\n    relevance_to_us: \"为我们的 alpha 实验提供理论预测：累积 vs 替换是 collapse 速率的关键调节因子\"\n    metrics_studied: [\"population risk\"]\n\n  - id: \"epstein2024howbad\"\n    title: \"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse\"\n    authors: \"Mohamed El Amine Epstein et al.\"\n    venue: \"arXiv (2404.05090)\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2404.05090\"\n    category: \"data-mixing\"\n    role: \"background\"\n    key_findings:\n      - \"纯合成数据训练不可避免 collapse\"\n      - \"给出 synthetic data 比例上界的估计——低于此比例可避免 collapse\"\n      - \"递归训练使原始分布尾部消失\"\n    relevance_to_us: \"其 mixing ratio 上界估计可对比我们实验中观测到的 canary 触发阈值\"\n    metrics_studied: [\"perplexity\"]\n\n  - id: \"bakshi2026improvement\"\n    title: \"From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources\"\n    authors: \"Soham Bakshi et al.\"\n    venue: \"arXiv (2602.10531)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2602.10531\"\n    category: \"data-mixing\"\n    role: \"background\"\n    key_findings:\n      - \"即使真实数据比例随时间衰减，只要非零就可能避免 collapse 并恢复真实分布\"\n      - \"在 next-token prediction 语言模型上分析混合训练的动态\"\n    relevance_to_us: \"提供了 decaying real data fraction 的理论保证，与我们的实验中 alpha 变化场景相关\"\n    metrics_studied: [\"population risk\"]\n\n  # ============================================================\n  # MITIGATION & VERIFICATION\n  # ============================================================\n  - id: \"feng2025escaping\"\n    title: \"Escaping Model Collapse via Synthetic Data Verification\"\n    authors: \"Yunzhen Feng et al.\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.16657\"\n    category: \"data-mixing\"\n    role: \"background\"\n    key_findings:\n      - \"通过外部 verifier（human 或 better model）注入信息可避免 collapse\"\n      - \"verifier-guided retraining 带来短期改善，但最终收敛到 verifier 的 knowledge center\"\n      - \"除非 verifier 完全可靠，早期收益会 plateau 甚至逆转\"\n    relevance_to_us: \"verification 作为 intervention 策略——如果 canary 触发，可考虑此类 reactive intervention\"\n    metrics_studied: [\"test loss\"]\n\n  - id: \"barzilai2025consistency\"\n    title: \"When Models Don't Collapse: On the Consistency of Iterative MLE\"\n    authors: \"Daniel Barzilai, Ohad Shamir\"\n    venue: \"ICML 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2505.19046\"\n    category: \"core-collapse\"\n    role: \"background\"\n    key_findings:\n      - \"在标准 MLE 一致性假设下，即使 real data fraction 趋近零也可避免 collapse\"\n      - \"但证明了某些情况下 collapse 可以任意快地发生——首次给出严格 collapse 反例\"\n    relevance_to_us: \"理论上的 collapse 可发生任意快的结论强化了 early warning 的价值\"\n    metrics_studied: []\n\n  - id: \"dces2026counter\"\n    title: \"Countering Model Collapse in Iterative Self-Training via Dynamic Center-Edge Sampling\"\n    authors: \"Anonymous\"\n    venue: \"MDPI Electronics (2026)\"\n    year: 2026\n    url: \"https://www.mdpi.com/2079-9292/15/4/869\"\n    category: \"data-mixing\"\n    role: \"background\"\n    key_findings:\n      - \"提出 DCES（dynamic center-edge sampling）数据选择框架\"\n      - \"DCES 在 ECE（0.1058 vs 0.1200）和 entropy 保持上优于随机选择\"\n    relevance_to_us: \"其 ECE 和 entropy 对比数据为我们的指标 baseline 提供参考\"\n    metrics_studied: [\"ECE\", \"entropy\"]\n\n  # ============================================================\n  # POSITION / SURVEY / EPISTEMICS\n  # ============================================================\n  - id: \"schaeffer2025position\"\n    title: \"Position: Model Collapse Does Not Mean What You Think\"\n    authors: \"Rylan Schaeffer, Joshua Kazdan, Alvan Caleb Arulandu, Sanmi Koyejo\"\n    venue: \"arXiv (2503.03150)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2503.03150\"\n    category: \"core-collapse\"\n    role: \"background\"\n    key_findings:\n      - \"文献中实际包含 8 种不同且有时矛盾的 model collapse 定义\"\n      - \"许多 collapse 预测依赖于与现实不符的假设\"\n      - \"多种 collapse 场景是可以轻易避免的\"\n    relevance_to_us: \"提醒我们明确定义 collapse 的操作标准；不同定义可能需要不同的 canary 指标\"\n    metrics_studied: []\n\n  - id: \"wang2025epistemic\"\n    title: \"Epistemic Diversity and Knowledge Collapse in Large Language Models\"\n    authors: \"Wang et al.\"\n    venue: \"arXiv (2510.04226)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.04226\"\n    category: \"core-collapse\"\n    role: \"background\"\n    key_findings:\n      - \"27 个 LLM 在 155 个主题上的 epistemic diversity 评估\"\n      - \"所有模型的 epistemic diversity 低于基本 web 搜索\"\n      - \"模型越大 epistemic diversity 反而越低；RAG 有正面效果\"\n    relevance_to_us: \"knowledge collapse 维度可扩展我们对 diversity canary 的理解——不仅是 lexical/syntactic 还有 epistemic\"\n    metrics_studied: [\"epistemic diversity\"]\n\n  # ============================================================\n  # METHODOLOGY (GRANGER / LEAD-LAG)\n  # ============================================================\n  - id: \"shojaie2022granger\"\n    title: \"Granger Causality: A Review and Recent Advances\"\n    authors: \"Ali Shojaie, Emily B. Fox\"\n    venue: \"Annual Review of Statistics and Its Application\"\n    year: 2022\n    url: \"https://arxiv.org/abs/2105.02675\"\n    category: \"methodology\"\n    role: \"method-component\"\n    key_findings:\n      - \"Granger causality 综述：从经典线性到非线性/neural 方法\"\n      - \"Panel data 场景的 Granger causality 扩展\"\n      - \"VAR 和 neural Granger causality 的对比\"\n    relevance_to_us: \"为我们的 panel Granger causality 分析提供方法论基础\"\n    metrics_studied: []\n\n  - id: \"marcinkevics2022neural\"\n    title: \"Granger Causality Using Neural Networks\"\n    authors: \"Raphael Marcinkevics, Julia Vogt\"\n    venue: \"arXiv (2208.03703)\"\n    year: 2022\n    url: \"https://arxiv.org/abs/2208.03703\"\n    category: \"methodology\"\n    role: \"method-component\"\n    key_findings:\n      - \"用 neural network 估计 Granger causality，突破线性假设\"\n      - \"两个模型对比法：含/不含外生变量的预测误差差异即 Granger causality 证据\"\n    relevance_to_us: \"我们的多指标时序可能存在非线性关系，neural Granger causality 是自然选择\"\n    metrics_studied: []\n\ngaps:\n  - \"无人系统做过 canary 指标的 lead-lag / Granger causality 分析——现有工作只在事后观察到指标变化，未量化哪些指标能提前多少步预测 collapse\"\n  - \"ECE 在 collapse 场景下几乎未被系统研究——chen2025scales 是唯一报告 ECE 先于 accuracy 退化的工作，但未做因果分析\"\n  - \"embedding effective rank 未在 iterative synthetic training 场景下被测试——仅在 contrastive learning/transformer 训练中研究过\"\n  - \"多指标 panel 框架缺失——无人同时追踪 ECE + effective rank + diversity + perplexity 的时序行为并分析其 lead-lag 关系\"\n  - \"alpha（synthetic ratio）对 canary 灵敏度的影响未被研究——现有工作只关注 alpha 对最终性能的影响，不关注 canary 的 lead time 如何随 alpha 变化\"\n  - \"predictive intervention vs reactive intervention 缺少对比——没有工作量化 early warning 带来的实际干预收益\"\n  - \"surplexity 和 spectral alignment 未在 iterative collapse 场景下交叉验证\"\n  - \"跨任务 canary 普适性未知——reasoning vs retrieval vs creative tasks 中哪些 canary 更可靠\"\n\nnovelty_assessment: |\n  我们项目的核心 novelty 在于：\n\n  1. **Panel Granger Causality 框架**：首次将多指标时序数据的因果分析方法应用于 model collapse 早期预警。\n     现有工作（chen2025scales, gambetta2024surplexity）只是事后观察到某些指标先变化，\n     但没有人做过系统的 lead-lag 量化分析。\n\n  2. **多指标 Canary Panel**：同时追踪 ECE、effective rank、Self-BLEU/distinct-n、\n     perplexity、entropy、surplexity 等指标，分析其相互关系和各自的 lead time。\n     现有工作都是单一指标或最多两三个指标的孤立分析。\n\n  3. **alpha-dependent Canary Sensitivity**：系统研究 synthetic ratio 如何影响各 canary\n     指标的灵敏度和 lead time。dohmatob2025strong 证明极小的 alpha 就能触发 collapse，\n     但没人研究 canary 在不同 alpha 下的行为。\n\n  4. **与已有工作的差异**：\n     - vs chen2025scales: 他们发现 ECE 先退化但没有做因果分析；我们用 Granger causality 量化\n     - vs gambetta2024surplexity: 他们提出 surplexity 用于检测和缓解 collapse；\n       我们将其纳入更广的 panel 并研究其 lead-lag 特性\n     - vs he2025closer: 他们在 diffusion 中用 entropy 作为指标；我们在 LLM 中测试更多指标\n     - vs qiu2025spectral: 他们的 SA 用于训练 loss explosion 预警；\n       我们将类似思路迁移到 iterative collapse 场景\n\n  5. **潜在风险**：chen2025scales 已经非常接近我们的方向。如果他们扩展到 lead-lag 分析，\n     我们的 novelty 会被削弱。需要快速推进并在方法论（Granger causality）上建立壁垒。\n",
    "structuredPatch": [
      {
        "oldStart": 354,
        "oldLines": 6,
        "newStart": 354,
        "newLines": 22,
        "lines": [
          "     relevance_to_us: \"其 mixing ratio 上界估计可对比我们实验中观测到的 canary 触发阈值\"",
          "     metrics_studied: [\"perplexity\"]",
          " ",
          "+  - id: \"fu2025selfconsuming\"",
          "+    title: \"A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops\"",
          "+    authors: \"Shi Fu, Yingjie Wang, Yuzhu Chen, Xinmei Tian, Dacheng Tao\"",
          "+    venue: \"ICLR 2025\"",
          "+    year: 2025",
          "+    url: \"https://arxiv.org/abs/2502.18865\"",
          "+    category: \"data-mixing\"",
          "+    role: \"theoretical-foundation\"",
          "+    key_findings:",
          "+      - \"引入 recursive stability 概念，首次给出 self-consuming loop 的泛化分析\"",
          "+      - \"恒定比例的真实数据即可保证 STL 收敛；同时给出最优合成数据量的 insight\"",
          "+      - \"模型架构和 real/synthetic 数据比例共同决定 STL 的成败\"",
          "+    relevance_to_us: \"为 post-MVP α-sweep（synthetic ratio 梯度）实验提供理论预期：50% accumulation 条件下收敛有理论保证\"",
          "+    gaps: \"理论分析限于特定 generalization bound 框架，未涉及 canary 指标的行为；未讨论不同 α 下 collapse 速率的精细结构\"",
          "+    metrics_studied: [\"generalization bound\", \"population risk\"]",
          "+",
          "   - id: \"bakshi2026improvement\"",
          "     title: \"From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources\"",
          "     authors: \"Soham Bakshi et al.\""
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

### Tool call

_source line 52_

<details open><summary>🔧 Tool call — Edit · `toolu_01X9f1qGUytPhpvR9iwkDfmw`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/literature_map.yaml",
  "old_string": "  - id: \"bakshi2026improvement\"\n    title: \"From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources\"\n    authors: \"Soham Bakshi et al.\"\n    venue: \"arXiv (2602.10531)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2602.10531\"\n    category: \"data-mixing\"\n    role: \"background\"\n    key_findings:\n      - \"即使真实数据比例随时间衰减，只要非零就可能避免 collapse 并恢复真实分布\"\n      - \"在 next-token prediction 语言模型上分析混合训练的动态\"\n    relevance_to_us: \"提供了 decaying real data fraction 的理论保证，与我们的实验中 alpha 变化场景相关\"\n    metrics_studied: [\"population risk\"]",
  "new_string": "  - id: \"bakshi2026improvement\"\n    title: \"From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources\"\n    authors: \"Soham Bakshi, Sunrit Chakraborty\"\n    venue: \"arXiv (2602.10531)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2602.10531\"\n    category: \"data-mixing\"\n    role: \"theoretical-foundation\"\n    key_findings:\n      - \"αt（每轮混合权重）trajectory 和 nt（每轮样本量）scaling 的交互决定三种 regime：collapse / improvement / consistency\"\n      - \"当 αt 衰减足够快且 nt 增长足够快时，迭代估计可收敛到真实分布（improvement regime）\"\n      - \"αt 衰减不足或 nt 增长不足则进入 collapse regime；边界条件给出 consistency regime\"\n      - \"在 next-token prediction 语言模型上分析完整迭代演化动态\"\n    relevance_to_us: \"αt/nt 条件直接对应我们 α-sweep 实验的理论预期：不同 synthetic ratio 衰减曲线下 canary 应呈现不同时序模式\"\n    gaps: \"理论结果基于渐近分析，有限代数下的 transient behavior 未充分刻画；未讨论哪些指标能区分三种 regime\"\n    metrics_studied: [\"population risk\", \"total variation distance\"]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "dd57d029-6d36-489f-8df5-369499cb8f4f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JJzXwrmDkVp6YNrBMB64fV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10452,
      "cache_read_input_tokens": 45696,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10452
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

_source line 53 · 2026-05-14T05:46:27.794Z_

<details><summary>↩ Tool result · `toolu_01X9f1qGUytPhpvR9iwkDfmw`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "e1024711-b79a-4bc1-9d5d-45a291e3d3ed",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/literature_map.yaml",
    "oldString": "  - id: \"bakshi2026improvement\"\n    title: \"From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources\"\n    authors: \"Soham Bakshi et al.\"\n    venue: \"arXiv (2602.10531)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2602.10531\"\n    category: \"data-mixing\"\n    role: \"background\"\n    key_findings:\n      - \"即使真实数据比例随时间衰减，只要非零就可能避免 collapse 并恢复真实分布\"\n      - \"在 next-token prediction 语言模型上分析混合训练的动态\"\n    relevance_to_us: \"提供了 decaying real data fraction 的理论保证，与我们的实验中 alpha 变化场景相关\"\n    metrics_studied: [\"population risk\"]",
    "newString": "  - id: \"bakshi2026improvement\"\n    title: \"From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources\"\n    authors: \"Soham Bakshi, Sunrit Chakraborty\"\n    venue: \"arXiv (2602.10531)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2602.10531\"\n    category: \"data-mixing\"\n    role: \"theoretical-foundation\"\n    key_findings:\n      - \"αt（每轮混合权重）trajectory 和 nt（每轮样本量）scaling 的交互决定三种 regime：collapse / improvement / consistency\"\n      - \"当 αt 衰减足够快且 nt 增长足够快时，迭代估计可收敛到真实分布（improvement regime）\"\n      - \"αt 衰减不足或 nt 增长不足则进入 collapse regime；边界条件给出 consistency regime\"\n      - \"在 next-token prediction 语言模型上分析完整迭代演化动态\"\n    relevance_to_us: \"αt/nt 条件直接对应我们 α-sweep 实验的理论预期：不同 synthetic ratio 衰减曲线下 canary 应呈现不同时序模式\"\n    gaps: \"理论结果基于渐近分析，有限代数下的 transient behavior 未充分刻画；未讨论哪些指标能区分三种 regime\"\n    metrics_studied: [\"population risk\", \"total variation distance\"]",
    "originalFile": "papers:\n  # ============================================================\n  # CORE MODEL COLLAPSE\n  # ============================================================\n  - id: \"shumailov2024curse\"\n    title: \"The Curse of Recursion: Training on Generated Data Makes Models Forget\"\n    authors: \"Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Yarin Gal, Nicolas Papernot, Ross Anderson\"\n    venue: \"Nature\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2305.17493\"\n    category: \"core-collapse\"\n    role: \"foundation\"\n    key_findings:\n      - \"定义 model collapse 现象：迭代用合成数据替换真实数据训练会导致分布尾部消失\"\n      - \"区分 early model collapse（尾部信息丢失）和 late model collapse（分布完全收敛）\"\n      - \"三类误差来源：statistical approximation, functional expressivity, functional approximation，跨代复合\"\n      - \"在 VAE、GMM、LLM 上均验证了 collapse 的普遍性\"\n    relevance_to_us: \"奠基论文，定义了我们研究的核心现象。我们的 canary 指标旨在提前检测其描述的 early collapse 阶段\"\n    metrics_studied: [\"perplexity\", \"distributional tail mass\"]\n\n  - id: \"alemohammad2024mad\"\n    title: \"Self-Consuming Generative Models Go MAD\"\n    authors: \"Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, Richard Baraniuk\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2307.01850\"\n    category: \"core-collapse\"\n    role: \"foundation\"\n    key_findings:\n      - \"提出 Model Autophagy Disorder (MAD) 概念\"\n      - \"autophagous loop 中没有足够新鲜真实数据时，质量或多样性必然渐进下降\"\n      - \"在图像生成领域验证 self-consuming loop 的退化效应\"\n    relevance_to_us: \"MAD 框架与我们的 iterative loop 设置直接对应；其 quality vs diversity tradeoff 可能反映在不同 canary 指标上\"\n    metrics_studied: [\"FID\", \"precision\", \"recall\", \"diversity\"]\n\n  - id: \"dohmatob2024tale\"\n    title: \"A Tale of Tails: Model Collapse as a Change of Scaling Laws\"\n    authors: \"Elvis Dohmatob, Yunzhen Feng, et al.\"\n    venue: \"ICML 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2402.07043\"\n    category: \"core-collapse\"\n    role: \"foundation\"\n    key_findings:\n      - \"通过 scaling laws 视角分析 model collapse：collapse 表现为 scaling law 的变化\"\n      - \"发现 loss of scaling, shifted scaling, skill un-learning, grokking 等多种退化模式\"\n      - \"混入少量干净数据可缓解 collapse 并引发 grokking 现象\"\n      - \"在 transformer 算术任务和 Llama2 文本生成上验证\"\n    relevance_to_us: \"scaling law 变化视角为我们提供了理论基础；grokking 现象暗示 canary 指标可能出现非单调行为\"\n    metrics_studied: [\"test loss\", \"scaling exponents\"]\n\n  - id: \"dohmatob2025strong\"\n    title: \"Strong Model Collapse\"\n    authors: \"Elvis Dohmatob, Yunzhen Feng, Arjun Subramonian, Julia Kempe\"\n    venue: \"ICLR 2025 (Spotlight)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2410.04840\"\n    category: \"core-collapse\"\n    role: \"foundation\"\n    key_findings:\n      - \"即使合成数据占比极小（1/1000），仍可导致 model collapse\"\n      - \"更大的训练集并不能避免 collapse\"\n      - \"更大的模型（random projection 近似下）反而可能放大 collapse\"\n      - \"存在 interpolation threshold 的 double-descent 现象\"\n    relevance_to_us: \"强化了早期检测的必要性——即使极小的合成数据比例也能触发 collapse，因此 canary 指标必须敏感\"\n    metrics_studied: [\"test loss\", \"population risk\"]\n\n  - id: \"guo2024linguistic\"\n    title: \"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\"\n    authors: \"Yanzhu Guo, Guokan Shang, et al.\"\n    venue: \"NAACL 2024 Findings\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2311.09807\"\n    category: \"core-collapse\"\n    role: \"evaluation\"\n    key_findings:\n      - \"递归微调中，linguistic diversity 在连续迭代中持续下降\"\n      - \"创造性任务中 diversity 下降最显著\"\n      - \"开发了覆盖 lexical、syntactic、semantic 三层的 diversity 指标体系\"\n    relevance_to_us: \"其多层 diversity 指标体系可直接作为我们 canary 指标的候选集；创造性 vs 事实任务的差异可能影响 canary 灵敏度\"\n    metrics_studied: [\"distinct-n\", \"type-token ratio\", \"syntactic diversity\", \"semantic diversity\"]\n\n  - id: \"briesch2024selfconsuming\"\n    title: \"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop\"\n    authors: \"Martin Briesch, Dominik Sobania, Franz Rothlauf\"\n    venue: \"arXiv (2311.16822)\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2311.16822\"\n    category: \"core-collapse\"\n    role: \"direct-competitor\"\n    key_findings:\n      - \"首次系统研究 LLM 的 self-consuming training loop\"\n      - \"full synthetic cycle（完全替换）导致单点 collapse；data augmentation cycle 导致 diversity 缓慢下降\"\n      - \"expanding data cycle（累积）在 50 代内保持 diversity\"\n    relevance_to_us: \"其不同 data cycle 策略的对比直接对应我们的 alpha（synthetic ratio）实验设置\"\n    metrics_studied: [\"diversity\", \"quality\"]\n\n  - id: \"truong2025entropy\"\n    title: \"Entropy Collapse: A Universal Failure Mode of Intelligent Systems\"\n    authors: \"Truong Xuan Khanh, Truong Quynh Hoa\"\n    venue: \"arXiv (2512.12381)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2512.12381\"\n    category: \"core-collapse\"\n    role: \"theoretical-foundation\"\n    key_findings:\n      - \"证明 entropy collapse 是一阶（不连续）相变，临界点 α_c(β) = 1/(1−β)，entropy 在临界点跳变 0.698 nats\"\n      - \"两个 universality class：Class 1（凸反馈，如 power-law）不可逆 ν=1；Class 2（线性反馈）可逆 ν=1/2\"\n      - \"因为是一阶相变，autocorrelation/variance 等传统 early-warning signal 在 collapse 前保持有限——无预警\"\n    relevance_to_us: \"定义了 canary 失效的 regime boundary：Class 1 凸反馈系统中传统 canary 理论上无效。我们需证明我们的 canary 在 Class 2+ regime 或非纯反馈场景中有效\"\n    gaps: \"理论框架高度抽象，未给出 LLM 具体场景下的 α/β 估计方法；未测试哪些 canary 在接近一阶相变时仍有部分预警能力\"\n    metrics_studied: [\"entropy\", \"autocorrelation\", \"variance\"]\n\n  - id: \"wang2026contaminated\"\n    title: \"Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training\"\n    authors: \"Kevin Wang, Hongqian Niu, Didong Li\"\n    venue: \"arXiv (2602.16065)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2602.16065\"\n    category: \"core-collapse\"\n    role: \"theoretical-foundation\"\n    key_findings:\n      - \"首个不限数据分布假设的正面理论结果：universal approximator 下 contaminated recursive training 仍可收敛\"\n      - \"收敛速率 = min(baseline 模型收敛速率, 每轮真实数据比例)——真实数据比例是瓶颈\"\n      - \"突破了先前仅限 discrete/Gaussian 分布的理论框架，适用于一般连续分布\"\n    relevance_to_us: \"为 post-MVP α-sweep 实验提供理论上界：收敛速率由 real data fraction 决定，可预测不同 α 下的 collapse 速率\"\n    gaps: \"universal approximator 假设在实际有限容量模型中不严格成立；未讨论 canary 指标行为\"\n    metrics_studied: [\"convergence rate\", \"population risk\"]\n\n  # ============================================================\n  # CANARY / EARLY WARNING METRICS\n  # ============================================================\n  - id: \"chen2025scales\"\n    title: \"Characterizing Model Behavior Under Synthetic Data Training: An Empirical Study Across Scales and Mixing Ratios\"\n    authors: \"Anonymous\"\n    venue: \"arXiv (2510.05133)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.05133\"\n    category: \"canary-metrics\"\n    role: \"direct-competitor\"\n    key_findings:\n      - \"**Calibration degradation precedes accuracy loss** — ECE 是 collapse 的 early warning signal\"\n      - \"20% synthetic data 以下性能稳定，30% 以上退化加速\"\n      - \"大模型（6.9B-12B）比小模型（410M-1.4B）更鲁棒\"\n      - \"推理任务比检索任务更易退化\"\n      - \"iteration 1 + 30% synthetic 时 ECE 从 0.08 升至 0.14（+75%）\"\n    relevance_to_us: \"**最直接的竞争者/先驱**。证实 ECE 可作为 canary，但未做 lead-lag 分析，未建立多指标 panel 框架\"\n    metrics_studied: [\"ECE\", \"accuracy\", \"perplexity\"]\n\n  - id: \"gambetta2024surplexity\"\n    title: \"Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI\"\n    authors: \"Daniele Gambetta et al.\"\n    venue: \"arXiv (2410.12341)\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2410.12341\"\n    category: \"canary-metrics\"\n    role: \"direct-competitor\"\n    key_findings:\n      - \"提出 surplexity（model surprise 度量）同时用于检测 collapse 和过滤训练数据\"\n      - \"用 semantic networks 分析文本重复性和语义多样性\"\n      - \"用 next-token probability 定量衡量 diversity loss\"\n      - \"高 surplexity 过滤策略至少与 human-data baseline 同效，且更能降低分布偏斜\"\n      - \"不需要区分 human vs AI-generated data\"\n    relevance_to_us: \"surplexity 可作为我们 canary 指标候选之一；其 semantic network 方法提供了 diversity 度量的另一视角\"\n    metrics_studied: [\"surplexity\", \"semantic network metrics\", \"next-token probability\"]\n\n  - id: \"qiu2025spectral\"\n    title: \"Spectral Alignment as Predictor of Loss Explosion in Neural Network Training\"\n    authors: \"Haiquan Qiu, You Wu, Yingjie Tan, Yaqing Wang, Quanming Yao\"\n    venue: \"arXiv (2510.04202)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.04202\"\n    category: \"canary-metrics\"\n    role: \"method-component\"\n    key_findings:\n      - \"Spectral Alignment (SA) 监控层输入与权重矩阵主奇异向量的分布对齐\"\n      - \"SA sign diversity collapse 是 representational collapse 和训练发散的早期预测器\"\n      - \"比 weight norm、gradient norm 等传统指标更早、更清晰地检测到训练失败\"\n      - \"健康层的 SA 应有正负均衡分布，collapse 到单侧则预示不稳定\"\n    relevance_to_us: \"SA 是潜在的高价值 canary 指标——专门设计为 early warning，可直接纳入我们的指标 panel\"\n    metrics_studied: [\"spectral alignment\", \"weight norm\", \"gradient norm\"]\n\n  - id: \"he2025closer\"\n    title: \"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\"\n    authors: \"Shiliang He et al.\"\n    venue: \"NeurIPS 2025 (Spotlight)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2509.16499\"\n    category: \"canary-metrics\"\n    role: \"direct-competitor\"\n    key_findings:\n      - \"识别 diffusion model collapse 中的 generalization → memorization 转变\"\n      - \"**训练数据的 entropy 递减是 collapse 的直接驱动因素和清晰指标**\"\n      - \"提出基于 entropy 的数据选择策略，有效缓解 collapse\"\n    relevance_to_us: \"data entropy 作为 canary 的有效性已被验证（diffusion domain）；需测试是否在 LLM 场景同样有效\"\n    metrics_studied: [\"entropy\", \"FID\", \"diversity\"]\n\n  - id: \"ba2024fill\"\n    title: \"Fill In The Gaps: Model Calibration and Generalization with Synthetic Data\"\n    authors: \"Yang Ba, Michelle V Mancenido, Rong Pan\"\n    venue: \"EMNLP 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2410.10864\"\n    category: \"canary-metrics\"\n    role: \"background\"\n    key_findings:\n      - \"用 LLM 生成合成数据来修复 calibration 错误的 reliability diagram bins\"\n      - \"推导了基于 PAC 框架的 ECE bound\"\n      - \"合成数据可改善 calibration 但需精心设计生成策略\"\n    relevance_to_us: \"ECE 的理论 bound 可为我们的 canary 阈值设定提供理论依据\"\n    metrics_studied: [\"ECE\", \"accuracy\"]\n\n  - id: \"sigma2026spectral\"\n    title: \"SIGMA: Scalable Spectral Insights for LLM Model Collapse\"\n    authors: \"Yi Gu, Lingyou Pang, Xiangkun Ye, Tianyu Wang, Jianyu Lin, Carey E. Priebe, Alexander Aue\"\n    venue: \"arXiv (2601.03385)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2601.03385\"\n    category: \"canary-metrics\"\n    role: \"direct-competitor\"\n    key_findings:\n      - \"基于 embedding Gram matrix 谱分析的 collapse 监控框架：Track I（确定性谱界）保守但鲁棒，Track II（随机谱缩放）灵敏但需采样\"\n      - \"Track I/II 的分歧本身是 early-stage collapse 的诊断信号，早于表面重复性伪影\"\n      - \"随机谱界使部分观测的 Gram matrix 也可用于大规模模型的可扩展监控\"\n    relevance_to_us: \"最直接的 spectral canary 竞争者。我们的 effective rank 是其简化版（单一标量 vs 完整谱界）；需在 related work 中明确差异：SIGMA 提供双轨谱界，我们用单一 effective rank 换取更低计算开销和多指标 panel 集成\"\n    gaps: \"未做 lead-lag 分析，未与 ECE/diversity 等非谱指标对比；Track I/II 的计算开销在 iterative loop 多轮场景下可能不可忽略\"\n    metrics_studied: [\"Gram matrix eigenspectrum\", \"spectral norm bounds\"]\n\n  - id: \"kalinowski2026topology\"\n    title: \"Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index\"\n    authors: \"Alexander Kalinowski\"\n    venue: \"arXiv (2604.26984)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2604.26984\"\n    category: \"canary-metrics\"\n    role: \"background\"\n    key_findings:\n      - \"提出基于 Modular Morse Homology Maintenance (MMHM) 的在线拓扑监控方案，增量更新避免每轮重建\"\n      - \"Collapse Index (CI) 组合多尺度拓扑特征，在 LLM fine-tuning 和 temporal KGE 训练中提供低延迟 early-warning\"\n      - \"拓扑方法捕捉表示空间的各向异性和多尺度结构丧失\"\n    relevance_to_us: \"topology-based monitoring 是与 spectral 方法正交的 collapse 检测路线。我们排除了该方法（计算开销高、可解释性弱），但 related work 需要对比说明选择 spectral/calibration panel 而非 topology 的理由\"\n    gaps: \"计算开销显著高于 effective rank 等标量指标；未在 iterative synthetic training loop 场景下测试；与 ECE 等轻量 canary 无对比\"\n    metrics_studied: [\"Collapse Index\", \"persistent homology features\"]\n\n  # ============================================================\n  # DIVERSITY METRICS (BACKGROUND)\n  # ============================================================\n  - id: \"zhu2018texygen\"\n    title: \"Texygen: A Benchmarking Platform for Text Generation Models\"\n    authors: \"Yaoming Zhu et al.\"\n    venue: \"SIGIR 2018\"\n    year: 2018\n    url: \"https://arxiv.org/abs/1802.01886\"\n    category: \"canary-metrics\"\n    role: \"background\"\n    key_findings:\n      - \"提出 Self-BLEU 度量：计算生成句子间的 BLEU 相似度，Self-BLEU 越高多样性越低\"\n      - \"成为文本生成多样性评估的标准基准之一\"\n    relevance_to_us: \"Self-BLEU 是我们 diversity canary 的经典候选\"\n    metrics_studied: [\"Self-BLEU\", \"BLEU\"]\n\n  - id: \"li2016diversity\"\n    title: \"A Diversity-Promoting Objective Function for Neural Conversation Models\"\n    authors: \"Jiwei Li et al.\"\n    venue: \"NAACL 2016\"\n    year: 2016\n    url: \"https://arxiv.org/abs/1510.03055\"\n    category: \"canary-metrics\"\n    role: \"background\"\n    key_findings:\n      - \"提出 distinct-1 / distinct-2 指标衡量生成文本的 n-gram 多样性\"\n      - \"计算 unique n-gram 数占总 n-gram 数的比例\"\n    relevance_to_us: \"distinct-n 是最廉价的 diversity canary 之一，计算开销极低\"\n    metrics_studied: [\"distinct-1\", \"distinct-2\"]\n\n  # ============================================================\n  # REPRESENTATION / SPECTRAL COLLAPSE\n  # ============================================================\n  - id: \"jing2022understanding\"\n    title: \"Understanding Dimensional Collapse in Contrastive Self-supervised Learning\"\n    authors: \"Li Jing et al.\"\n    venue: \"ICLR 2022\"\n    year: 2022\n    url: \"https://openreview.net/forum?id=YevsQ05DEN7\"\n    category: \"canary-metrics\"\n    role: \"method-component\"\n    key_findings:\n      - \"定义 dimensional collapse：embedding 向量只跨越低维子空间\"\n      - \"effective rank（基于归一化特征值 entropy 的指数）作为 collapse 度量\"\n      - \"strong augmentation 和 implicit regularization 驱动低秩解\"\n    relevance_to_us: \"effective rank 的定义和计算方式可直接迁移到我们的 embedding 空间监控\"\n    metrics_studied: [\"effective rank\", \"singular value spectrum\"]\n\n  - id: \"noci2024mind\"\n    title: \"Mind the Gap: A Spectral Analysis of Rank Collapse and Signal Propagation in Transformers\"\n    authors: \"Lorenzo Noci et al.\"\n    venue: \"NeurIPS 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2410.07799\"\n    category: \"canary-metrics\"\n    role: \"method-component\"\n    key_findings:\n      - \"用 Random Matrix Theory 分析 attention 层的 rank collapse\"\n      - \"发现 attention matrix 最大两个奇异值之间的 spectral gap 是 width-collapse 的根因\"\n      - \"rank collapse in depth: 所有 token 沿层收敛到单一表示\"\n    relevance_to_us: \"spectral gap 作为另一种 spectral canary 候选；其 RMT 分析框架可启发我们的理论工作\"\n    metrics_studied: [\"spectral gap\", \"singular values\", \"effective rank\"]\n\n  # ============================================================\n  # DATA MIXING & ACCUMULATION\n  # ============================================================\n  - id: \"kazdan2025collapse\"\n    title: \"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World\"\n    authors: \"Joshua Kazdan, Rylan Schaeffer, Apratim Dey, Matthias Gerstgrasser, Rafael Rafailov, David L. Donoho, Sanmi Koyejo\"\n    venue: \"ICML 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2410.16713\"\n    category: \"data-mixing\"\n    role: \"foundation\"\n    key_findings:\n      - \"系统对比 replace vs accumulate 场景\"\n      - \"replace → collapse；accumulate → 可避免 collapse\"\n      - \"发现 real data 和 synthetic data 之间存在非平凡的交互效应\"\n      - \"synthetic data 的价值取决于 real data 的绝对数量\"\n    relevance_to_us: \"直接对应我们的 alpha（mixing ratio）实验维度；其 replace vs accumulate 框架是我们实验设计的重要参考\"\n    metrics_studied: [\"test loss\"]\n\n  - id: \"dey2024breaking\"\n    title: \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\"\n    authors: \"Apratim Dey, David Donoho, et al.\"\n    venue: \"ICML 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2404.01413\"\n    category: \"data-mixing\"\n    role: \"foundation\"\n    key_findings:\n      - \"替换数据 → 发散 population risk；累积数据 → 避免发散\"\n      - \"证明累积策略在多种模型（GMM, HMM, LLM）上有效\"\n    relevance_to_us: \"为我们的 alpha 实验提供理论预测：累积 vs 替换是 collapse 速率的关键调节因子\"\n    metrics_studied: [\"population risk\"]\n\n  - id: \"epstein2024howbad\"\n    title: \"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse\"\n    authors: \"Mohamed El Amine Epstein et al.\"\n    venue: \"arXiv (2404.05090)\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2404.05090\"\n    category: \"data-mixing\"\n    role: \"background\"\n    key_findings:\n      - \"纯合成数据训练不可避免 collapse\"\n      - \"给出 synthetic data 比例上界的估计——低于此比例可避免 collapse\"\n      - \"递归训练使原始分布尾部消失\"\n    relevance_to_us: \"其 mixing ratio 上界估计可对比我们实验中观测到的 canary 触发阈值\"\n    metrics_studied: [\"perplexity\"]\n\n  - id: \"fu2025selfconsuming\"\n    title: \"A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops\"\n    authors: \"Shi Fu, Yingjie Wang, Yuzhu Chen, Xinmei Tian, Dacheng Tao\"\n    venue: \"ICLR 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2502.18865\"\n    category: \"data-mixing\"\n    role: \"theoretical-foundation\"\n    key_findings:\n      - \"引入 recursive stability 概念，首次给出 self-consuming loop 的泛化分析\"\n      - \"恒定比例的真实数据即可保证 STL 收敛；同时给出最优合成数据量的 insight\"\n      - \"模型架构和 real/synthetic 数据比例共同决定 STL 的成败\"\n    relevance_to_us: \"为 post-MVP α-sweep（synthetic ratio 梯度）实验提供理论预期：50% accumulation 条件下收敛有理论保证\"\n    gaps: \"理论分析限于特定 generalization bound 框架，未涉及 canary 指标的行为；未讨论不同 α 下 collapse 速率的精细结构\"\n    metrics_studied: [\"generalization bound\", \"population risk\"]\n\n  - id: \"bakshi2026improvement\"\n    title: \"From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources\"\n    authors: \"Soham Bakshi et al.\"\n    venue: \"arXiv (2602.10531)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2602.10531\"\n    category: \"data-mixing\"\n    role: \"background\"\n    key_findings:\n      - \"即使真实数据比例随时间衰减，只要非零就可能避免 collapse 并恢复真实分布\"\n      - \"在 next-token prediction 语言模型上分析混合训练的动态\"\n    relevance_to_us: \"提供了 decaying real data fraction 的理论保证，与我们的实验中 alpha 变化场景相关\"\n    metrics_studied: [\"population risk\"]\n\n  # ============================================================\n  # MITIGATION & VERIFICATION\n  # ============================================================\n  - id: \"feng2025escaping\"\n    title: \"Escaping Model Collapse via Synthetic Data Verification\"\n    authors: \"Yunzhen Feng et al.\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.16657\"\n    category: \"data-mixing\"\n    role: \"background\"\n    key_findings:\n      - \"通过外部 verifier（human 或 better model）注入信息可避免 collapse\"\n      - \"verifier-guided retraining 带来短期改善，但最终收敛到 verifier 的 knowledge center\"\n      - \"除非 verifier 完全可靠，早期收益会 plateau 甚至逆转\"\n    relevance_to_us: \"verification 作为 intervention 策略——如果 canary 触发，可考虑此类 reactive intervention\"\n    metrics_studied: [\"test loss\"]\n\n  - id: \"barzilai2025consistency\"\n    title: \"When Models Don't Collapse: On the Consistency of Iterative MLE\"\n    authors: \"Daniel Barzilai, Ohad Shamir\"\n    venue: \"ICML 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2505.19046\"\n    category: \"core-collapse\"\n    role: \"background\"\n    key_findings:\n      - \"在标准 MLE 一致性假设下，即使 real data fraction 趋近零也可避免 collapse\"\n      - \"但证明了某些情况下 collapse 可以任意快地发生——首次给出严格 collapse 反例\"\n    relevance_to_us: \"理论上的 collapse 可发生任意快的结论强化了 early warning 的价值\"\n    metrics_studied: []\n\n  - id: \"dces2026counter\"\n    title: \"Countering Model Collapse in Iterative Self-Training via Dynamic Center-Edge Sampling\"\n    authors: \"Anonymous\"\n    venue: \"MDPI Electronics (2026)\"\n    year: 2026\n    url: \"https://www.mdpi.com/2079-9292/15/4/869\"\n    category: \"data-mixing\"\n    role: \"background\"\n    key_findings:\n      - \"提出 DCES（dynamic center-edge sampling）数据选择框架\"\n      - \"DCES 在 ECE（0.1058 vs 0.1200）和 entropy 保持上优于随机选择\"\n    relevance_to_us: \"其 ECE 和 entropy 对比数据为我们的指标 baseline 提供参考\"\n    metrics_studied: [\"ECE\", \"entropy\"]\n\n  # ============================================================\n  # POSITION / SURVEY / EPISTEMICS\n  # ============================================================\n  - id: \"schaeffer2025position\"\n    title: \"Position: Model Collapse Does Not Mean What You Think\"\n    authors: \"Rylan Schaeffer, Joshua Kazdan, Alvan Caleb Arulandu, Sanmi Koyejo\"\n    venue: \"arXiv (2503.03150)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2503.03150\"\n    category: \"core-collapse\"\n    role: \"background\"\n    key_findings:\n      - \"文献中实际包含 8 种不同且有时矛盾的 model collapse 定义\"\n      - \"许多 collapse 预测依赖于与现实不符的假设\"\n      - \"多种 collapse 场景是可以轻易避免的\"\n    relevance_to_us: \"提醒我们明确定义 collapse 的操作标准；不同定义可能需要不同的 canary 指标\"\n    metrics_studied: []\n\n  - id: \"wang2025epistemic\"\n    title: \"Epistemic Diversity and Knowledge Collapse in Large Language Models\"\n    authors: \"Wang et al.\"\n    venue: \"arXiv (2510.04226)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.04226\"\n    category: \"core-collapse\"\n    role: \"background\"\n    key_findings:\n      - \"27 个 LLM 在 155 个主题上的 epistemic diversity 评估\"\n      - \"所有模型的 epistemic diversity 低于基本 web 搜索\"\n      - \"模型越大 epistemic diversity 反而越低；RAG 有正面效果\"\n    relevance_to_us: \"knowledge collapse 维度可扩展我们对 diversity canary 的理解——不仅是 lexical/syntactic 还有 epistemic\"\n    metrics_studied: [\"epistemic diversity\"]\n\n  # ============================================================\n  # METHODOLOGY (GRANGER / LEAD-LAG)\n  # ============================================================\n  - id: \"shojaie2022granger\"\n    title: \"Granger Causality: A Review and Recent Advances\"\n    authors: \"Ali Shojaie, Emily B. Fox\"\n    venue: \"Annual Review of Statistics and Its Application\"\n    year: 2022\n    url: \"https://arxiv.org/abs/2105.02675\"\n    category: \"methodology\"\n    role: \"method-component\"\n    key_findings:\n      - \"Granger causality 综述：从经典线性到非线性/neural 方法\"\n      - \"Panel data 场景的 Granger causality 扩展\"\n      - \"VAR 和 neural Granger causality 的对比\"\n    relevance_to_us: \"为我们的 panel Granger causality 分析提供方法论基础\"\n    metrics_studied: []\n\n  - id: \"marcinkevics2022neural\"\n    title: \"Granger Causality Using Neural Networks\"\n    authors: \"Raphael Marcinkevics, Julia Vogt\"\n    venue: \"arXiv (2208.03703)\"\n    year: 2022\n    url: \"https://arxiv.org/abs/2208.03703\"\n    category: \"methodology\"\n    role: \"method-component\"\n    key_findings:\n      - \"用 neural network 估计 Granger causality，突破线性假设\"\n      - \"两个模型对比法：含/不含外生变量的预测误差差异即 Granger causality 证据\"\n    relevance_to_us: \"我们的多指标时序可能存在非线性关系，neural Granger causality 是自然选择\"\n    metrics_studied: []\n\ngaps:\n  - \"无人系统做过 canary 指标的 lead-lag / Granger causality 分析——现有工作只在事后观察到指标变化，未量化哪些指标能提前多少步预测 collapse\"\n  - \"ECE 在 collapse 场景下几乎未被系统研究——chen2025scales 是唯一报告 ECE 先于 accuracy 退化的工作，但未做因果分析\"\n  - \"embedding effective rank 未在 iterative synthetic training 场景下被测试——仅在 contrastive learning/transformer 训练中研究过\"\n  - \"多指标 panel 框架缺失——无人同时追踪 ECE + effective rank + diversity + perplexity 的时序行为并分析其 lead-lag 关系\"\n  - \"alpha（synthetic ratio）对 canary 灵敏度的影响未被研究——现有工作只关注 alpha 对最终性能的影响，不关注 canary 的 lead time 如何随 alpha 变化\"\n  - \"predictive intervention vs reactive intervention 缺少对比——没有工作量化 early warning 带来的实际干预收益\"\n  - \"surplexity 和 spectral alignment 未在 iterative collapse 场景下交叉验证\"\n  - \"跨任务 canary 普适性未知——reasoning vs retrieval vs creative tasks 中哪些 canary 更可靠\"\n\nnovelty_assessment: |\n  我们项目的核心 novelty 在于：\n\n  1. **Panel Granger Causality 框架**：首次将多指标时序数据的因果分析方法应用于 model collapse 早期预警。\n     现有工作（chen2025scales, gambetta2024surplexity）只是事后观察到某些指标先变化，\n     但没有人做过系统的 lead-lag 量化分析。\n\n  2. **多指标 Canary Panel**：同时追踪 ECE、effective rank、Self-BLEU/distinct-n、\n     perplexity、entropy、surplexity 等指标，分析其相互关系和各自的 lead time。\n     现有工作都是单一指标或最多两三个指标的孤立分析。\n\n  3. **alpha-dependent Canary Sensitivity**：系统研究 synthetic ratio 如何影响各 canary\n     指标的灵敏度和 lead time。dohmatob2025strong 证明极小的 alpha 就能触发 collapse，\n     但没人研究 canary 在不同 alpha 下的行为。\n\n  4. **与已有工作的差异**：\n     - vs chen2025scales: 他们发现 ECE 先退化但没有做因果分析；我们用 Granger causality 量化\n     - vs gambetta2024surplexity: 他们提出 surplexity 用于检测和缓解 collapse；\n       我们将其纳入更广的 panel 并研究其 lead-lag 特性\n     - vs he2025closer: 他们在 diffusion 中用 entropy 作为指标；我们在 LLM 中测试更多指标\n     - vs qiu2025spectral: 他们的 SA 用于训练 loss explosion 预警；\n       我们将类似思路迁移到 iterative collapse 场景\n\n  5. **潜在风险**：chen2025scales 已经非常接近我们的方向。如果他们扩展到 lead-lag 分析，\n     我们的 novelty 会被削弱。需要快速推进并在方法论（Granger causality）上建立壁垒。\n",
    "structuredPatch": [
      {
        "oldStart": 372,
        "oldLines": 17,
        "newStart": 372,
        "newLines": 20,
        "lines": [
          " ",
          "   - id: \"bakshi2026improvement\"",
          "     title: \"From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources\"",
          "-    authors: \"Soham Bakshi et al.\"",
          "+    authors: \"Soham Bakshi, Sunrit Chakraborty\"",
          "     venue: \"arXiv (2602.10531)\"",
          "     year: 2026",
          "     url: \"https://arxiv.org/abs/2602.10531\"",
          "     category: \"data-mixing\"",
          "-    role: \"background\"",
          "+    role: \"theoretical-foundation\"",
          "     key_findings:",
          "-      - \"即使真实数据比例随时间衰减，只要非零就可能避免 collapse 并恢复真实分布\"",
          "-      - \"在 next-token prediction 语言模型上分析混合训练的动态\"",
          "-    relevance_to_us: \"提供了 decaying real data fraction 的理论保证，与我们的实验中 alpha 变化场景相关\"",
          "-    metrics_studied: [\"population risk\"]",
          "+      - \"αt（每轮混合权重）trajectory 和 nt（每轮样本量）scaling 的交互决定三种 regime：collapse / improvement / consistency\"",
          "+      - \"当 αt 衰减足够快且 nt 增长足够快时，迭代估计可收敛到真实分布（improvement regime）\"",
          "+      - \"αt 衰减不足或 nt 增长不足则进入 collapse regime；边界条件给出 consistency regime\"",
          "+      - \"在 next-token prediction 语言模型上分析完整迭代演化动态\"",
          "+    relevance_to_us: \"αt/nt 条件直接对应我们 α-sweep 实验的理论预期：不同 synthetic ratio 衰减曲线下 canary 应呈现不同时序模式\"",
          "+    gaps: \"理论结果基于渐近分析，有限代数下的 transient behavior 未充分刻画；未讨论哪些指标能区分三种 regime\"",
          "+    metrics_studied: [\"population risk\", \"total variation distance\"]",
          " ",
          "   # ============================================================",
          "   # MITIGATION & VERIFICATION"
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

_source line 54_

<details><summary>Logged reasoning block</summary>

```text
All 4 edits succeeded. Now I need to save the file using the MCP tool. Let me first verify the file is correct by reading it, then save it.

Actually, the file was edited directly on disk. The `save_project_file` tool might be needed to save it to the MCP project system, but since I already edited the file directly, it should be fine. Let me verify the YAML is valid by checking a few key sections.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "9281b71e-e15d-4700-9c68-420832a0206b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C9UZJFDFt1sJb8eg4VahH1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4254,
      "cache_read_input_tokens": 56148,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4254
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

_source line 55_

验证 YAML 格式正确。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "b77c9203-1104-4b89-80b8-e9dfde461551",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C9UZJFDFt1sJb8eg4VahH1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4254,
      "cache_read_input_tokens": 56148,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4254
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

<details open><summary>🔧 Tool call — Bash · `toolu_01DXDvYAn555ooUHLAUPpBvw`</summary>

```json
{
  "command": "python3 -c \"import yaml; yaml.safe_load(open('/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/literature_map.yaml')); print('YAML valid')\" 2>&1",
  "description": "Validate YAML syntax"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "3f9cac37-fa81-431f-aab1-37424a494bd4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C9UZJFDFt1sJb8eg4VahH1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4254,
      "cache_read_input_tokens": 56148,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4254
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

_source line 57 · 2026-05-14T05:46:34.444Z_

<details><summary>↩ Tool result · `toolu_01DXDvYAn555ooUHLAUPpBvw`</summary>

```text
YAML valid
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "6efb5bf5-2ca1-4892-9f36-925968a3d0f6",
  "tool_use_result": {
    "stdout": "YAML valid",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 58_

<details open><summary>🔧 Tool call — Bash · `toolu_01Kht6LZVowKZNcbPZry8LhU`</summary>

```json
{
  "command": "python3 -c \"\nimport yaml\ndata = yaml.safe_load(open('/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/literature_map.yaml'))\npapers = data['papers']\nprint(f'Total papers: {len(papers)}')\nnew_ids = ['truong2025entropy', 'wang2026contaminated', 'sigma2026spectral', 'kalinowski2026topology', 'fu2025selfconsuming', 'bakshi2026improvement']\nfor pid in new_ids:\n    p = next((x for x in papers if x['id'] == pid), None)\n    if p:\n        print(f\\\"  {p['id']}: {p['category']} / {p['role']} — {p['title'][:60]}\\\")\n    else:\n        print(f'  MISSING: {pid}')\n\"",
  "description": "Verify new entries exist and count total papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "38827fc9-c24a-4510-8604-aa0b28aa0c34",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TfyT7UFR7MdMwqM3cMkVK7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 277,
      "cache_read_input_tokens": 60402,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 277
      },
      "output_tokens": 64,
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

_source line 59 · 2026-05-14T05:46:39.470Z_

<details><summary>↩ Tool result · `toolu_01Kht6LZVowKZNcbPZry8LhU`</summary>

```text
Total papers: 31
  truong2025entropy: core-collapse / theoretical-foundation — Entropy Collapse: A Universal Failure Mode of Intelligent Sy
  wang2026contaminated: core-collapse / theoretical-foundation — Can Generative Artificial Intelligence Survive Data Contamin
  sigma2026spectral: canary-metrics / direct-competitor — SIGMA: Scalable Spectral Insights for LLM Model Collapse
  kalinowski2026topology: canary-metrics / background — Monitoring Neural Training with Topology: A Footprint-Predic
  fu2025selfconsuming: data-mixing / theoretical-foundation — A Theoretical Perspective: How to Prevent Model Collapse in 
  bakshi2026improvement: data-mixing / theoretical-foundation — From Collapse to Improvement: Statistical Perspectives on th
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "ac11e069-a58d-4c35-8e21-c12e4fb5df7b",
  "tool_use_result": {
    "stdout": "Total papers: 31\n  truong2025entropy: core-collapse / theoretical-foundation — Entropy Collapse: A Universal Failure Mode of Intelligent Sy\n  wang2026contaminated: core-collapse / theoretical-foundation — Can Generative Artificial Intelligence Survive Data Contamin\n  sigma2026spectral: canary-metrics / direct-competitor — SIGMA: Scalable Spectral Insights for LLM Model Collapse\n  kalinowski2026topology: canary-metrics / background — Monitoring Neural Training with Topology: A Footprint-Predic\n  fu2025selfconsuming: data-mixing / theoretical-foundation — A Theoretical Perspective: How to Prevent Model Collapse in \n  bakshi2026improvement: data-mixing / theoretical-foundation — From Collapse to Improvement: Statistical Perspectives on th",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 60_

<details><summary>Logged reasoning block</summary>

```text
Now let me also save the file through the MCP tool to ensure it's properly synced. Actually, looking at the save_project_file tool description, it says "Writable: memory.md, writing_plan.yaml, paper_framing.md." - so literature_map.yaml might not be writable through the MCP tool. But since I already edited the file directly on disk, it should be fine. The MCP read tool reads from the same disk path.

Let me try saving it anyway - if it fails, the direct edit already worked.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "cfc80063-ab3c-46d2-b077-656434bd89e8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SjNYRFQAve4tfKA2ZdEXHm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 503,
      "cache_read_input_tokens": 60679,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 503
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

_source line 61_

Now save via MCP to ensure sync.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "57ea72b6-e895-44ad-92ac-a5d015133d35",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SjNYRFQAve4tfKA2ZdEXHm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 503,
      "cache_read_input_tokens": 60679,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 503
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

_source line 62_

<details open><summary>🔧 Tool call — Bash · `toolu_01VmpEdqm4pm9KghNDCbdo3d`</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/literature_map.yaml | wc -l",
  "description": "Count lines in updated file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "3ce854fe-bf48-45ee-a5e1-f21ff37ee74c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SjNYRFQAve4tfKA2ZdEXHm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 503,
      "cache_read_input_tokens": 60679,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 503
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

_source line 63 · 2026-05-14T05:46:46.330Z_

<details><summary>↩ Tool result · `toolu_01VmpEdqm4pm9KghNDCbdo3d`</summary>

```text
535
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "2ed23126-21da-4c81-bf33-6539aebf1b45",
  "tool_use_result": {
    "stdout": "535",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 64_

<details open><summary>🔧 Tool call — Read · `toolu_016WJEjci1BKM33Uzgds3Sfo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/literature_map.yaml",
  "limit": 10,
  "offset": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "b43a7ccc-3509-408b-9a52-0390a288e322",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DLyiABdchLgtTf5Sd4NvPu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 374,
      "cache_read_input_tokens": 61182,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 374
      },
      "output_tokens": 65,
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

_source line 65 · 2026-05-14T05:46:49.545Z_

<details><summary>↩ Tool result · `toolu_016WJEjci1BKM33Uzgds3Sfo`</summary>

```text
0	papers:
1	  # ============================================================
2	  # CORE MODEL COLLAPSE
3	  # ============================================================
4	  - id: "shumailov2024curse"
5	    title: "The Curse of Recursion: Training on Generated Data Makes Models Forget"
6	    authors: "Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Yarin Gal, Nicolas Papernot, Ross Anderson"
7	    venue: "Nature"
8	    year: 2024
9	    url: "https://arxiv.org/abs/2305.17493"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "531932fe-2d35-4149-a2b8-e702a4e45ed3",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/literature_map.yaml",
      "content": "papers:\n  # ============================================================\n  # CORE MODEL COLLAPSE\n  # ============================================================\n  - id: \"shumailov2024curse\"\n    title: \"The Curse of Recursion: Training on Generated Data Makes Models Forget\"\n    authors: \"Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Yarin Gal, Nicolas Papernot, Ross Anderson\"\n    venue: \"Nature\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2305.17493\"",
      "numLines": 10,
      "startLine": 0,
      "totalLines": 536
    }
  }
}
```

</details>

---

### Tool call

_source line 66_

<details open><summary>🔧 Tool call — Bash · `toolu_014t5S9dGxTDc1Va4APHXWwB`</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/literature_map.yaml",
  "description": "Read full file for MCP save",
  "timeout": 10000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "35491b68-d594-41f6-b7ba-495a7a16b7b4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019XaYpwnDzrESfXhbj5Uu6w",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 290,
      "cache_read_input_tokens": 61556,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 290
      },
      "output_tokens": 65,
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

_source line 67 · 2026-05-14T05:46:53.434Z_

<details><summary>↩ Tool result · `toolu_014t5S9dGxTDc1Va4APHXWwB`</summary>

```text
&lt;persisted-output>
Output too large (29.5KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/59a4bfdb-56db-43ec-b510-aabb3d2cc418/tool-results/bmpnc51p7.txt

Preview (first 2KB):
papers:
  # ============================================================
  # CORE MODEL COLLAPSE
  # ============================================================
  - id: "shumailov2024curse"
    title: "The Curse of Recursion: Training on Generated Data Makes Models Forget"
    authors: "Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Yarin Gal, Nicolas Papernot, Ross Anderson"
    venue: "Nature"
    year: 2024
    url: "https://arxiv.org/abs/2305.17493"
    category: "core-collapse"
    role: "foundation"
    key_findings:
      - "定义 model collapse 现象：迭代用合成数据替换真实数据训练会导致分布尾部消失"
      - "区分 early model collapse（尾部信息丢失）和 late model collapse（分布完全收敛）"
      - "三类误差来源：statistical approximation, functional expressivity, functional approximation，跨代复合"
      - "在 VAE、GMM、LLM 上均验证了 collapse 的普遍性"
    relevance_to_us: "奠基论文，定义了我们研究的核心现象。我们的 canary 指标旨在提前检测其描述的 early collapse 阶段"
    metrics_studied: ["perplexity", "distributional tail mass"]

  - id: "alemohammad2024mad"
    title: "Self-Consuming Generative Models Go MAD"
    authors: "Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, Richard Baraniuk"
    venue: "ICLR 2024"
    year: 2024
    url: "https://arxiv.org/abs/2307.01850"
    category: "core-collapse"
    role: "foundation"
    key_findings:
      - "提出 Model Autophagy Disorder (MAD) 概念"
      - "autophagous loop 中没有足够新鲜真实数据时，质量或多样性必然渐进下降"
      - "在图像生成领域验证 self-consuming loop 的退化效应"
    relevance_to_us: "MAD 框架与我们的 iterative loop 设置直接对应；其 quality vs diversity tradeoff 可能反映在不同 canary 指标上"
    metrics_studied: ["FID", "precision", "recall", "diversity"]

  - id: "dohmatob2024tale"
    title: "A Tale of Tails: Model Collapse as a Change of Scaling Laws"
    authors: "Elvis Dohmatob, Yunzhen Feng, et al."
    venue: "ICML 2024"
    year: 2024
    url: "https://arxiv.org/abs/2402.07043"
    category: "core-collapse"
    role: "foundation"
    key_findings:
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "03a7a739-10f1-41a7-b583-51ed2399bfd2",
  "tool_use_result": {
    "stdout": "papers:\n  # ============================================================\n  # CORE MODEL COLLAPSE\n  # ============================================================\n  - id: \"shumailov2024curse\"\n    title: \"The Curse of Recursion: Training on Generated Data Makes Models Forget\"\n    authors: \"Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Yarin Gal, Nicolas Papernot, Ross Anderson\"\n    venue: \"Nature\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2305.17493\"\n    category: \"core-collapse\"\n    role: \"foundation\"\n    key_findings:\n      - \"定义 model collapse 现象：迭代用合成数据替换真实数据训练会导致分布尾部消失\"\n      - \"区分 early model collapse（尾部信息丢失）和 late model collapse（分布完全收敛）\"\n      - \"三类误差来源：statistical approximation, functional expressivity, functional approximation，跨代复合\"\n      - \"在 VAE、GMM、LLM 上均验证了 collapse 的普遍性\"\n    relevance_to_us: \"奠基论文，定义了我们研究的核心现象。我们的 canary 指标旨在提前检测其描述的 early collapse 阶段\"\n    metrics_studied: [\"perplexity\", \"distributional tail mass\"]\n\n  - id: \"alemohammad2024mad\"\n    title: \"Self-Consuming Generative Models Go MAD\"\n    authors: \"Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, Richard Baraniuk\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2307.01850\"\n    category: \"core-collapse\"\n    role: \"foundation\"\n    key_findings:\n      - \"提出 Model Autophagy Disorder (MAD) 概念\"\n      - \"autophagous loop 中没有足够新鲜真实数据时，质量或多样性必然渐进下降\"\n      - \"在图像生成领域验证 self-consuming loop 的退化效应\"\n    relevance_to_us: \"MAD 框架与我们的 iterative loop 设置直接对应；其 quality vs diversity tradeoff 可能反映在不同 canary 指标上\"\n    metrics_studied: [\"FID\", \"precision\", \"recall\", \"diversity\"]\n\n  - id: \"dohmatob2024tale\"\n    title: \"A Tale of Tails: Model Collapse as a Change of Scaling Laws\"\n    authors: \"Elvis Dohmatob, Yunzhen Feng, et al.\"\n    venue: \"ICML 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2402.07043\"\n    category: \"core-collapse\"\n    role: \"foundation\"\n    key_findings:\n      - \"通过 scaling laws 视角分析 model collapse：collapse 表现为 scaling law 的变化\"\n      - \"发现 loss of scaling, shifted scaling, skill un-learning, grokking 等多种退化模式\"\n      - \"混入少量干净数据可缓解 collapse 并引发 grokking 现象\"\n      - \"在 transformer 算术任务和 Llama2 文本生成上验证\"\n    relevance_to_us: \"scaling law 变化视角为我们提供了理论基础；grokking 现象暗示 canary 指标可能出现非单调行为\"\n    metrics_studied: [\"test loss\", \"scaling exponents\"]\n\n  - id: \"dohmatob2025strong\"\n    title: \"Strong Model Collapse\"\n    authors: \"Elvis Dohmatob, Yunzhen Feng, Arjun Subramonian, Julia Kempe\"\n    venue: \"ICLR 2025 (Spotlight)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2410.04840\"\n    category: \"core-collapse\"\n    role: \"foundation\"\n    key_findings:\n      - \"即使合成数据占比极小（1/1000），仍可导致 model collapse\"\n      - \"更大的训练集并不能避免 collapse\"\n      - \"更大的模型（random projection 近似下）反而可能放大 collapse\"\n      - \"存在 interpolation threshold 的 double-descent 现象\"\n    relevance_to_us: \"强化了早期检测的必要性——即使极小的合成数据比例也能触发 collapse，因此 canary 指标必须敏感\"\n    metrics_studied: [\"test loss\", \"population risk\"]\n\n  - id: \"guo2024linguistic\"\n    title: \"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\"\n    authors: \"Yanzhu Guo, Guokan Shang, et al.\"\n    venue: \"NAACL 2024 Findings\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2311.09807\"\n    category: \"core-collapse\"\n    role: \"evaluation\"\n    key_findings:\n      - \"递归微调中，linguistic diversity 在连续迭代中持续下降\"\n      - \"创造性任务中 diversity 下降最显著\"\n      - \"开发了覆盖 lexical、syntactic、semantic 三层的 diversity 指标体系\"\n    relevance_to_us: \"其多层 diversity 指标体系可直接作为我们 canary 指标的候选集；创造性 vs 事实任务的差异可能影响 canary 灵敏度\"\n    metrics_studied: [\"distinct-n\", \"type-token ratio\", \"syntactic diversity\", \"semantic diversity\"]\n\n  - id: \"briesch2024selfconsuming\"\n    title: \"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop\"\n    authors: \"Martin Briesch, Dominik Sobania, Franz Rothlauf\"\n    venue: \"arXiv (2311.16822)\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2311.16822\"\n    category: \"core-collapse\"\n    role: \"direct-competitor\"\n    key_findings:\n      - \"首次系统研究 LLM 的 self-consuming training loop\"\n      - \"full synthetic cycle（完全替换）导致单点 collapse；data augmentation cycle 导致 diversity 缓慢下降\"\n      - \"expanding data cycle（累积）在 50 代内保持 diversity\"\n    relevance_to_us: \"其不同 data cycle 策略的对比直接对应我们的 alpha（synthetic ratio）实验设置\"\n    metrics_studied: [\"diversity\", \"quality\"]\n\n  - id: \"truong2025entropy\"\n    title: \"Entropy Collapse: A Universal Failure Mode of Intelligent Systems\"\n    authors: \"Truong Xuan Khanh, Truong Quynh Hoa\"\n    venue: \"arXiv (2512.12381)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2512.12381\"\n    category: \"core-collapse\"\n    role: \"theoretical-foundation\"\n    key_findings:\n      - \"证明 entropy collapse 是一阶（不连续）相变，临界点 α_c(β) = 1/(1−β)，entropy 在临界点跳变 0.698 nats\"\n      - \"两个 universality class：Class 1（凸反馈，如 power-law）不可逆 ν=1；Class 2（线性反馈）可逆 ν=1/2\"\n      - \"因为是一阶相变，autocorrelation/variance 等传统 early-warning signal 在 collapse 前保持有限——无预警\"\n    relevance_to_us: \"定义了 canary 失效的 regime boundary：Class 1 凸反馈系统中传统 canary 理论上无效。我们需证明我们的 canary 在 Class 2+ regime 或非纯反馈场景中有效\"\n    gaps: \"理论框架高度抽象，未给出 LLM 具体场景下的 α/β 估计方法；未测试哪些 canary 在接近一阶相变时仍有部分预警能力\"\n    metrics_studied: [\"entropy\", \"autocorrelation\", \"variance\"]\n\n  - id: \"wang2026contaminated\"\n    title: \"Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training\"\n    authors: \"Kevin Wang, Hongqian Niu, Didong Li\"\n    venue: \"arXiv (2602.16065)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2602.16065\"\n    category: \"core-collapse\"\n    role: \"theoretical-foundation\"\n    key_findings:\n      - \"首个不限数据分布假设的正面理论结果：universal approximator 下 contaminated recursive training 仍可收敛\"\n      - \"收敛速率 = min(baseline 模型收敛速率, 每轮真实数据比例)——真实数据比例是瓶颈\"\n      - \"突破了先前仅限 discrete/Gaussian 分布的理论框架，适用于一般连续分布\"\n    relevance_to_us: \"为 post-MVP α-sweep 实验提供理论上界：收敛速率由 real data fraction 决定，可预测不同 α 下的 collapse 速率\"\n    gaps: \"universal approximator 假设在实际有限容量模型中不严格成立；未讨论 canary 指标行为\"\n    metrics_studied: [\"convergence rate\", \"population risk\"]\n\n  # ============================================================\n  # CANARY / EARLY WARNING METRICS\n  # ============================================================\n  - id: \"chen2025scales\"\n    title: \"Characterizing Model Behavior Under Synthetic Data Training: An Empirical Study Across Scales and Mixing Ratios\"\n    authors: \"Anonymous\"\n    venue: \"arXiv (2510.05133)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.05133\"\n    category: \"canary-metrics\"\n    role: \"direct-competitor\"\n    key_findings:\n      - \"**Calibration degradation precedes accuracy loss** — ECE 是 collapse 的 early warning signal\"\n      - \"20% synthetic data 以下性能稳定，30% 以上退化加速\"\n      - \"大模型（6.9B-12B）比小模型（410M-1.4B）更鲁棒\"\n      - \"推理任务比检索任务更易退化\"\n      - \"iteration 1 + 30% synthetic 时 ECE 从 0.08 升至 0.14（+75%）\"\n    relevance_to_us: \"**最直接的竞争者/先驱**。证实 ECE 可作为 canary，但未做 lead-lag 分析，未建立多指标 panel 框架\"\n    metrics_studied: [\"ECE\", \"accuracy\", \"perplexity\"]\n\n  - id: \"gambetta2024surplexity\"\n    title: \"Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI\"\n    authors: \"Daniele Gambetta et al.\"\n    venue: \"arXiv (2410.12341)\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2410.12341\"\n    category: \"canary-metrics\"\n    role: \"direct-competitor\"\n    key_findings:\n      - \"提出 surplexity（model surprise 度量）同时用于检测 collapse 和过滤训练数据\"\n      - \"用 semantic networks 分析文本重复性和语义多样性\"\n      - \"用 next-token probability 定量衡量 diversity loss\"\n      - \"高 surplexity 过滤策略至少与 human-data baseline 同效，且更能降低分布偏斜\"\n      - \"不需要区分 human vs AI-generated data\"\n    relevance_to_us: \"surplexity 可作为我们 canary 指标候选之一；其 semantic network 方法提供了 diversity 度量的另一视角\"\n    metrics_studied: [\"surplexity\", \"semantic network metrics\", \"next-token probability\"]\n\n  - id: \"qiu2025spectral\"\n    title: \"Spectral Alignment as Predictor of Loss Explosion in Neural Network Training\"\n    authors: \"Haiquan Qiu, You Wu, Yingjie Tan, Yaqing Wang, Quanming Yao\"\n    venue: \"arXiv (2510.04202)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.04202\"\n    category: \"canary-metrics\"\n    role: \"method-component\"\n    key_findings:\n      - \"Spectral Alignment (SA) 监控层输入与权重矩阵主奇异向量的分布对齐\"\n      - \"SA sign diversity collapse 是 representational collapse 和训练发散的早期预测器\"\n      - \"比 weight norm、gradient norm 等传统指标更早、更清晰地检测到训练失败\"\n      - \"健康层的 SA 应有正负均衡分布，collapse 到单侧则预示不稳定\"\n    relevance_to_us: \"SA 是潜在的高价值 canary 指标——专门设计为 early warning，可直接纳入我们的指标 panel\"\n    metrics_studied: [\"spectral alignment\", \"weight norm\", \"gradient norm\"]\n\n  - id: \"he2025closer\"\n    title: \"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\"\n    authors: \"Shiliang He et al.\"\n    venue: \"NeurIPS 2025 (Spotlight)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2509.16499\"\n    category: \"canary-metrics\"\n    role: \"direct-competitor\"\n    key_findings:\n      - \"识别 diffusion model collapse 中的 generalization → memorization 转变\"\n      - \"**训练数据的 entropy 递减是 collapse 的直接驱动因素和清晰指标**\"\n      - \"提出基于 entropy 的数据选择策略，有效缓解 collapse\"\n    relevance_to_us: \"data entropy 作为 canary 的有效性已被验证（diffusion domain）；需测试是否在 LLM 场景同样有效\"\n    metrics_studied: [\"entropy\", \"FID\", \"diversity\"]\n\n  - id: \"ba2024fill\"\n    title: \"Fill In The Gaps: Model Calibration and Generalization with Synthetic Data\"\n    authors: \"Yang Ba, Michelle V Mancenido, Rong Pan\"\n    venue: \"EMNLP 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2410.10864\"\n    category: \"canary-metrics\"\n    role: \"background\"\n    key_findings:\n      - \"用 LLM 生成合成数据来修复 calibration 错误的 reliability diagram bins\"\n      - \"推导了基于 PAC 框架的 ECE bound\"\n      - \"合成数据可改善 calibration 但需精心设计生成策略\"\n    relevance_to_us: \"ECE 的理论 bound 可为我们的 canary 阈值设定提供理论依据\"\n    metrics_studied: [\"ECE\", \"accuracy\"]\n\n  - id: \"sigma2026spectral\"\n    title: \"SIGMA: Scalable Spectral Insights for LLM Model Collapse\"\n    authors: \"Yi Gu, Lingyou Pang, Xiangkun Ye, Tianyu Wang, Jianyu Lin, Carey E. Priebe, Alexander Aue\"\n    venue: \"arXiv (2601.03385)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2601.03385\"\n    category: \"canary-metrics\"\n    role: \"direct-competitor\"\n    key_findings:\n      - \"基于 embedding Gram matrix 谱分析的 collapse 监控框架：Track I（确定性谱界）保守但鲁棒，Track II（随机谱缩放）灵敏但需采样\"\n      - \"Track I/II 的分歧本身是 early-stage collapse 的诊断信号，早于表面重复性伪影\"\n      - \"随机谱界使部分观测的 Gram matrix 也可用于大规模模型的可扩展监控\"\n    relevance_to_us: \"最直接的 spectral canary 竞争者。我们的 effective rank 是其简化版（单一标量 vs 完整谱界）；需在 related work 中明确差异：SIGMA 提供双轨谱界，我们用单一 effective rank 换取更低计算开销和多指标 panel 集成\"\n    gaps: \"未做 lead-lag 分析，未与 ECE/diversity 等非谱指标对比；Track I/II 的计算开销在 iterative loop 多轮场景下可能不可忽略\"\n    metrics_studied: [\"Gram matrix eigenspectrum\", \"spectral norm bounds\"]\n\n  - id: \"kalinowski2026topology\"\n    title: \"Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index\"\n    authors: \"Alexander Kalinowski\"\n    venue: \"arXiv (2604.26984)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2604.26984\"\n    category: \"canary-metrics\"\n    role: \"background\"\n    key_findings:\n      - \"提出基于 Modular Morse Homology Maintenance (MMHM) 的在线拓扑监控方案，增量更新避免每轮重建\"\n      - \"Collapse Index (CI) 组合多尺度拓扑特征，在 LLM fine-tuning 和 temporal KGE 训练中提供低延迟 early-warning\"\n      - \"拓扑方法捕捉表示空间的各向异性和多尺度结构丧失\"\n    relevance_to_us: \"topology-based monitoring 是与 spectral 方法正交的 collapse 检测路线。我们排除了该方法（计算开销高、可解释性弱），但 related work 需要对比说明选择 spectral/calibration panel 而非 topology 的理由\"\n    gaps: \"计算开销显著高于 effective rank 等标量指标；未在 iterative synthetic training loop 场景下测试；与 ECE 等轻量 canary 无对比\"\n    metrics_studied: [\"Collapse Index\", \"persistent homology features\"]\n\n  # ============================================================\n  # DIVERSITY METRICS (BACKGROUND)\n  # ============================================================\n  - id: \"zhu2018texygen\"\n    title: \"Texygen: A Benchmarking Platform for Text Generation Models\"\n    authors: \"Yaoming Zhu et al.\"\n    venue: \"SIGIR 2018\"\n    year: 2018\n    url: \"https://arxiv.org/abs/1802.01886\"\n    category: \"canary-metrics\"\n    role: \"background\"\n    key_findings:\n      - \"提出 Self-BLEU 度量：计算生成句子间的 BLEU 相似度，Self-BLEU 越高多样性越低\"\n      - \"成为文本生成多样性评估的标准基准之一\"\n    relevance_to_us: \"Self-BLEU 是我们 diversity canary 的经典候选\"\n    metrics_studied: [\"Self-BLEU\", \"BLEU\"]\n\n  - id: \"li2016diversity\"\n    title: \"A Diversity-Promoting Objective Function for Neural Conversation Models\"\n    authors: \"Jiwei Li et al.\"\n    venue: \"NAACL 2016\"\n    year: 2016\n    url: \"https://arxiv.org/abs/1510.03055\"\n    category: \"canary-metrics\"\n    role: \"background\"\n    key_findings:\n      - \"提出 distinct-1 / distinct-2 指标衡量生成文本的 n-gram 多样性\"\n      - \"计算 unique n-gram 数占总 n-gram 数的比例\"\n    relevance_to_us: \"distinct-n 是最廉价的 diversity canary 之一，计算开销极低\"\n    metrics_studied: [\"distinct-1\", \"distinct-2\"]\n\n  # ============================================================\n  # REPRESENTATION / SPECTRAL COLLAPSE\n  # ============================================================\n  - id: \"jing2022understanding\"\n    title: \"Understanding Dimensional Collapse in Contrastive Self-supervised Learning\"\n    authors: \"Li Jing et al.\"\n    venue: \"ICLR 2022\"\n    year: 2022\n    url: \"https://openreview.net/forum?id=YevsQ05DEN7\"\n    category: \"canary-metrics\"\n    role: \"method-component\"\n    key_findings:\n      - \"定义 dimensional collapse：embedding 向量只跨越低维子空间\"\n      - \"effective rank（基于归一化特征值 entropy 的指数）作为 collapse 度量\"\n      - \"strong augmentation 和 implicit regularization 驱动低秩解\"\n    relevance_to_us: \"effective rank 的定义和计算方式可直接迁移到我们的 embedding 空间监控\"\n    metrics_studied: [\"effective rank\", \"singular value spectrum\"]\n\n  - id: \"noci2024mind\"\n    title: \"Mind the Gap: A Spectral Analysis of Rank Collapse and Signal Propagation in Transformers\"\n    authors: \"Lorenzo Noci et al.\"\n    venue: \"NeurIPS 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2410.07799\"\n    category: \"canary-metrics\"\n    role: \"method-component\"\n    key_findings:\n      - \"用 Random Matrix Theory 分析 attention 层的 rank collapse\"\n      - \"发现 attention matrix 最大两个奇异值之间的 spectral gap 是 width-collapse 的根因\"\n      - \"rank collapse in depth: 所有 token 沿层收敛到单一表示\"\n    relevance_to_us: \"spectral gap 作为另一种 spectral canary 候选；其 RMT 分析框架可启发我们的理论工作\"\n    metrics_studied: [\"spectral gap\", \"singular values\", \"effective rank\"]\n\n  # ============================================================\n  # DATA MIXING & ACCUMULATION\n  # ============================================================\n  - id: \"kazdan2025collapse\"\n    title: \"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World\"\n    authors: \"Joshua Kazdan, Rylan Schaeffer, Apratim Dey, Matthias Gerstgrasser, Rafael Rafailov, David L. Donoho, Sanmi Koyejo\"\n    venue: \"ICML 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2410.16713\"\n    category: \"data-mixing\"\n    role: \"foundation\"\n    key_findings:\n      - \"系统对比 replace vs accumulate 场景\"\n      - \"replace → collapse；accumulate → 可避免 collapse\"\n      - \"发现 real data 和 synthetic data 之间存在非平凡的交互效应\"\n      - \"synthetic data 的价值取决于 real data 的绝对数量\"\n    relevance_to_us: \"直接对应我们的 alpha（mixing ratio）实验维度；其 replace vs accumulate 框架是我们实验设计的重要参考\"\n    metrics_studied: [\"test loss\"]\n\n  - id: \"dey2024breaking\"\n    title: \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\"\n    authors: \"Apratim Dey, David Donoho, et al.\"\n    venue: \"ICML 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2404.01413\"\n    category: \"data-mixing\"\n    role: \"foundation\"\n    key_findings:\n      - \"替换数据 → 发散 population risk；累积数据 → 避免发散\"\n      - \"证明累积策略在多种模型（GMM, HMM, LLM）上有效\"\n    relevance_to_us: \"为我们的 alpha 实验提供理论预测：累积 vs 替换是 collapse 速率的关键调节因子\"\n    metrics_studied: [\"population risk\"]\n\n  - id: \"epstein2024howbad\"\n    title: \"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse\"\n    authors: \"Mohamed El Amine Epstein et al.\"\n    venue: \"arXiv (2404.05090)\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2404.05090\"\n    category: \"data-mixing\"\n    role: \"background\"\n    key_findings:\n      - \"纯合成数据训练不可避免 collapse\"\n      - \"给出 synthetic data 比例上界的估计——低于此比例可避免 collapse\"\n      - \"递归训练使原始分布尾部消失\"\n    relevance_to_us: \"其 mixing ratio 上界估计可对比我们实验中观测到的 canary 触发阈值\"\n    metrics_studied: [\"perplexity\"]\n\n  - id: \"fu2025selfconsuming\"\n    title: \"A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops\"\n    authors: \"Shi Fu, Yingjie Wang, Yuzhu Chen, Xinmei Tian, Dacheng Tao\"\n    venue: \"ICLR 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2502.18865\"\n    category: \"data-mixing\"\n    role: \"theoretical-foundation\"\n    key_findings:\n      - \"引入 recursive stability 概念，首次给出 self-consuming loop 的泛化分析\"\n      - \"恒定比例的真实数据即可保证 STL 收敛；同时给出最优合成数据量的 insight\"\n      - \"模型架构和 real/synthetic 数据比例共同决定 STL 的成败\"\n    relevance_to_us: \"为 post-MVP α-sweep（synthetic ratio 梯度）实验提供理论预期：50% accumulation 条件下收敛有理论保证\"\n    gaps: \"理论分析限于特定 generalization bound 框架，未涉及 canary 指标的行为；未讨论不同 α 下 collapse 速率的精细结构\"\n    metrics_studied: [\"generalization bound\", \"population risk\"]\n\n  - id: \"bakshi2026improvement\"\n    title: \"From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources\"\n    authors: \"Soham Bakshi, Sunrit Chakraborty\"\n    venue: \"arXiv (2602.10531)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2602.10531\"\n    category: \"data-mixing\"\n    role: \"theoretical-foundation\"\n    key_findings:\n      - \"αt（每轮混合权重）trajectory 和 nt（每轮样本量）scaling 的交互决定三种 regime：collapse / improvement / consistency\"\n      - \"当 αt 衰减足够快且 nt 增长足够快时，迭代估计可收敛到真实分布（improvement regime）\"\n      - \"αt 衰减不足或 nt 增长不足则进入 collapse regime；边界条件给出 consistency regime\"\n      - \"在 next-token prediction 语言模型上分析完整迭代演化动态\"\n    relevance_to_us: \"αt/nt 条件直接对应我们 α-sweep 实验的理论预期：不同 synthetic ratio 衰减曲线下 canary 应呈现不同时序模式\"\n    gaps: \"理论结果基于渐近分析，有限代数下的 transient behavior 未充分刻画；未讨论哪些指标能区分三种 regime\"\n    metrics_studied: [\"population risk\", \"total variation distance\"]\n\n  # ============================================================\n  # MITIGATION & VERIFICATION\n  # ============================================================\n  - id: \"feng2025escaping\"\n    title: \"Escaping Model Collapse via Synthetic Data Verification\"\n    authors: \"Yunzhen Feng et al.\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.16657\"\n    category: \"data-mixing\"\n    role: \"background\"\n    key_findings:\n      - \"通过外部 verifier（human 或 better model）注入信息可避免 collapse\"\n      - \"verifier-guided retraining 带来短期改善，但最终收敛到 verifier 的 knowledge center\"\n      - \"除非 verifier 完全可靠，早期收益会 plateau 甚至逆转\"\n    relevance_to_us: \"verification 作为 intervention 策略——如果 canary 触发，可考虑此类 reactive intervention\"\n    metrics_studied: [\"test loss\"]\n\n  - id: \"barzilai2025consistency\"\n    title: \"When Models Don't Collapse: On the Consistency of Iterative MLE\"\n    authors: \"Daniel Barzilai, Ohad Shamir\"\n    venue: \"ICML 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2505.19046\"\n    category: \"core-collapse\"\n    role: \"background\"\n    key_findings:\n      - \"在标准 MLE 一致性假设下，即使 real data fraction 趋近零也可避免 collapse\"\n      - \"但证明了某些情况下 collapse 可以任意快地发生——首次给出严格 collapse 反例\"\n    relevance_to_us: \"理论上的 collapse 可发生任意快的结论强化了 early warning 的价值\"\n    metrics_studied: []\n\n  - id: \"dces2026counter\"\n    title: \"Countering Model Collapse in Iterative Self-Training via Dynamic Center-Edge Sampling\"\n    authors: \"Anonymous\"\n    venue: \"MDPI Electronics (2026)\"\n    year: 2026\n    url: \"https://www.mdpi.com/2079-9292/15/4/869\"\n    category: \"data-mixing\"\n    role: \"background\"\n    key_findings:\n      - \"提出 DCES（dynamic center-edge sampling）数据选择框架\"\n      - \"DCES 在 ECE（0.1058 vs 0.1200）和 entropy 保持上优于随机选择\"\n    relevance_to_us: \"其 ECE 和 entropy 对比数据为我们的指标 baseline 提供参考\"\n    metrics_studied: [\"ECE\", \"entropy\"]\n\n  # ============================================================\n  # POSITION / SURVEY / EPISTEMICS\n  # ============================================================\n  - id: \"schaeffer2025position\"\n    title: \"Position: Model Collapse Does Not Mean What You Think\"\n    authors: \"Rylan Schaeffer, Joshua Kazdan, Alvan Caleb Arulandu, Sanmi Koyejo\"\n    venue: \"arXiv (2503.03150)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2503.03150\"\n    category: \"core-collapse\"\n    role: \"background\"\n    key_findings:\n      - \"文献中实际包含 8 种不同且有时矛盾的 model collapse 定义\"\n      - \"许多 collapse 预测依赖于与现实不符的假设\"\n      - \"多种 collapse 场景是可以轻易避免的\"\n    relevance_to_us: \"提醒我们明确定义 collapse 的操作标准；不同定义可能需要不同的 canary 指标\"\n    metrics_studied: []\n\n  - id: \"wang2025epistemic\"\n    title: \"Epistemic Diversity and Knowledge Collapse in Large Language Models\"\n    authors: \"Wang et al.\"\n    venue: \"arXiv (2510.04226)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.04226\"\n    category: \"core-collapse\"\n    role: \"background\"\n    key_findings:\n      - \"27 个 LLM 在 155 个主题上的 epistemic diversity 评估\"\n      - \"所有模型的 epistemic diversity 低于基本 web 搜索\"\n      - \"模型越大 epistemic diversity 反而越低；RAG 有正面效果\"\n    relevance_to_us: \"knowledge collapse 维度可扩展我们对 diversity canary 的理解——不仅是 lexical/syntactic 还有 epistemic\"\n    metrics_studied: [\"epistemic diversity\"]\n\n  # ============================================================\n  # METHODOLOGY (GRANGER / LEAD-LAG)\n  # ============================================================\n  - id: \"shojaie2022granger\"\n    title: \"Granger Causality: A Review and Recent Advances\"\n    authors: \"Ali Shojaie, Emily B. Fox\"\n    venue: \"Annual Review of Statistics and Its Application\"\n    year: 2022\n    url: \"https://arxiv.org/abs/2105.02675\"\n    category: \"methodology\"\n    role: \"method-component\"\n    key_findings:\n      - \"Granger causality 综述：从经典线性到非线性/neural 方法\"\n      - \"Panel data 场景的 Granger causality 扩展\"\n      - \"VAR 和 neural Granger causality 的对比\"\n    relevance_to_us: \"为我们的 panel Granger causality 分析提供方法论基础\"\n    metrics_studied: []\n\n  - id: \"marcinkevics2022neural\"\n    title: \"Granger Causality Using Neural Networks\"\n    authors: \"Raphael Marcinkevics, Julia Vogt\"\n    venue: \"arXiv (2208.03703)\"\n    year: 2022\n    url: \"https://arxiv.org/abs/2208.03703\"\n    category: \"methodology\"\n    role: \"method-component\"\n    key_findings:\n      - \"用 neural network 估计 Granger causality，突破线性假设\"\n      - \"两个模型对比法：含/不含外生变量的预测误差差异即 Granger causality 证据\"\n    relevance_to_us: \"我们的多指标时序可能存在非线性关系，neural Granger causality 是自然选择\"\n    metrics_studied: []\n\ngaps:\n  - \"无人系统做过 canary 指标的 lead-lag / Granger causality 分析——现有工作只在事后观察到指标变化，未量化哪些指标能提前多少步预测 collapse\"\n  - \"ECE 在 collapse 场景下几乎未被系统研究——chen2025scales 是唯一报告 ECE 先于 accuracy 退化的工作，但未做因果分析\"\n  - \"embedding effective rank 未在 iterative synthetic training 场景下被测试——仅在 contrastive learning/transformer 训练中研究过\"\n  - \"多指标 panel 框架缺失——无人同时追踪 ECE + effective rank + diversity + perplexity 的时序行为并分析其 lead-lag 关系\"\n  - \"alpha（synthetic ratio）对 canary 灵敏度的影响未被研究——现有工作只关注 alpha 对最终性能的影响，不关注 canary 的 lead time 如何随 alpha 变化\"\n  - \"predictive intervention vs reactive intervention 缺少对比——没有工作量化 early warning 带来的实际干预收益\"\n  - \"surplexity 和 spectral alignment 未在 iterative collapse 场景下交叉验证\"\n  - \"跨任务 canary 普适性未知——reasoning vs retrieval vs creative tasks 中哪些 canary 更可靠\"\n\nnovelty_assessment: |\n  我们项目的核心 novelty 在于：\n\n  1. **Panel Granger Causality 框架**：首次将多指标时序数据的因果分析方法应用于 model collapse 早期预警。\n     现有工作（chen2025scales, gambetta2024surplexity）只是事后观察到某些指标先变化，\n     但没有人做过系统的 lead-lag 量化分析。\n\n  2. **多指标 Canary Panel**：同时追踪 ECE、effective rank、Self-BLEU/distinct-n、\n     perplexity、entropy、surplexity 等指标，分析其相互关系和各自的 lead time。\n     现有工作都是单一指标或最多两三个指标的孤立分析。\n\n  3. **alpha-dependent Canary Sensitivity**：系统研究 synthetic ratio 如何影响各 canary\n     指标的灵敏度和 lead time。dohmatob2025strong 证明极小的 alpha 就能触发 collapse，\n     但没人研究 canary 在不同 alpha 下的行为。\n\n  4. **与已有工作的差异**：\n     - vs chen2025scales: 他们发现 ECE 先退化但没有做因果分析；我们用 Granger causality 量化\n     - vs gambetta2024surplexity: 他们提出 surplexity 用于检测和缓解 collapse；\n       我们将其纳入更广的 panel 并研究其 lead-lag 特性\n     - vs he2025closer: 他们在 diffusion 中用 entropy 作为指标；我们在 LLM 中测试更多指标\n     - vs qiu2025spectral: 他们的 SA 用于训练 loss explosion 预警；\n       我们将类似思路迁移到 iterative collapse 场景\n\n  5. **潜在风险**：chen2025scales 已经非�",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false,
    "persistedOutputPath": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/59a4bfdb-56db-43ec-b510-aabb3d2cc418/tool-results/bmpnc51p7.txt",
    "persistedOutputSize": 30179
  }
}
```

</details>

---

### Assistant

_source line 68_

<details><summary>Logged reasoning block</summary>

```text
The file is too large to read in full via bash, but that's okay — I already verified the YAML is valid and all entries are present. The file was edited directly on disk, so the MCP read_project_file tool will read the updated version. Let me try saving it via MCP anyway - if it fails, the edits are already in place.

Actually, looking at the save_project_file tool description again: "Writable: memory.md, writing_plan.yaml, paper_framing.md. Other files have dedicated tools"

literature_map.yaml is NOT in the writable list. 

Since I can't save it through MCP, but the changes are already persisted to disk, I can move forward with summarizing what I've done for the user.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "400d5141-7e4e-4319-9a75-084bc44aa788",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YMx4FFZnJLMnhsoGG22u5V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1061,
      "cache_read_input_tokens": 61846,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1061
      },
      "output_tokens": 10,
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

_source line 69_

完成。literature_map.yaml 从 26 篇扩充到 31 篇（5 新增 + 1 充实），YAML 验证通过。

## 补全结果

| # | key | title | category | role | 与本项目核心关系 |
|---|-----|-------|----------|------|----------------|
| 1 | `sigma2026spectral` | SIGMA: Scalable Spectral Insights for LLM Model Collapse | canary-metrics | direct-competitor | 最直接的 spectral canary 竞争者；Track I/II 双轨 Gram matrix 谱界 vs 我们的单标量 effective rank——我们用更低计算开销换取多指标 panel 集成 |
| 2 | `truong2025entropy` | Entropy Collapse: A Universal Failure Mode of Intelligent Systems | core-collapse | theoretical-foundation | 证明 Class 1 凸反馈系统 entropy collapse 是一阶相变，autocorrelation/variance 无预警。定义了 canary 失效的 regime boundary，我们需证明 canary 在 Class 2+ 中有效 |
| 3 | `fu2025selfconsuming` | A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops | data-mixing | theoretical-foundation | 恒定 real data 比例保证 STL 收敛，为 α-sweep 50% accumulation 条件提供理论基础 |
| 4 | `kalinowski2026topology` | Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index | canary-metrics | background | topology-based monitoring 正交路线，related work 需对比说明我们选择 spectral/calibration panel 的理由 |
| 5 | `wang2026contaminated` | Can Generative AI Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training | core-collapse | theoretical-foundation | 首个 universal approximator 下的正面收敛结果：收敛速率 = min(baseline rate, real data fraction)，为 α-sweep 提供理论上界 |
| 6 | `bakshi2026improvement` (充实) | From Collapse to Improvement | data-mixing | theoretical-foundation (升级自 background) | 补充 αt trajectory + nt scaling 决定 collapse/improvement/consistency 三 regime 的条件；新增 gaps 和 TV distance 指标 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "uuid": "920a5a98-65e2-48fe-a98b-3a48c236e486",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YMx4FFZnJLMnhsoGG22u5V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1061,
      "cache_read_input_tokens": 61846,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1061
      },
      "output_tokens": 10,
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

_source line 70_

完成。literature_map.yaml 从 26 篇扩充到 31 篇（5 新增 + 1 充实），YAML 验证通过。

## 补全结果

| # | key | title | category | role | 与本项目核心关系 |
|---|-----|-------|----------|------|----------------|
| 1 | `sigma2026spectral` | SIGMA: Scalable Spectral Insights for LLM Model Collapse | canary-metrics | direct-competitor | 最直接的 spectral canary 竞争者；Track I/II 双轨 Gram matrix 谱界 vs 我们的单标量 effective rank——我们用更低计算开销换取多指标 panel 集成 |
| 2 | `truong2025entropy` | Entropy Collapse: A Universal Failure Mode of Intelligent Systems | core-collapse | theoretical-foundation | 证明 Class 1 凸反馈系统 entropy collapse 是一阶相变，autocorrelation/variance 无预警。定义了 canary 失效的 regime boundary，我们需证明 canary 在 Class 2+ 中有效 |
| 3 | `fu2025selfconsuming` | A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops | data-mixing | theoretical-foundation | 恒定 real data 比例保证 STL 收敛，为 α-sweep 50% accumulation 条件提供理论基础 |
| 4 | `kalinowski2026topology` | Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index | canary-metrics | background | topology-based monitoring 正交路线，related work 需对比说明我们选择 spectral/calibration panel 的理由 |
| 5 | `wang2026contaminated` | Can Generative AI Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training | core-collapse | theoretical-foundation | 首个 universal approximator 下的正面收敛结果：收敛速率 = min(baseline rate, real data fraction)，为 α-sweep 提供理论上界 |
| 6 | `bakshi2026improvement` (充实) | From Collapse to Improvement | data-mixing | theoretical-foundation (升级自 background) | 补充 αt trajectory + nt scaling 决定 collapse/improvement/consistency 三 regime 的条件；新增 gaps 和 TV distance 指标 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 198273,
  "duration_api_ms": 253542,
  "num_turns": 25,
  "stop_reason": "end_turn",
  "session_id": "59a4bfdb-56db-43ec-b510-aabb3d2cc418",
  "total_cost_usd": 1.1225625000000004,
  "usage": {
    "input_tokens": 521,
    "cache_creation_input_tokens": 51066,
    "cache_read_input_tokens": 586194,
    "output_tokens": 8411,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 51066,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 859,
        "cache_read_input_tokens": 61846,
        "cache_creation_input_tokens": 1061,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1061
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 153748,
      "outputTokens": 4735,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 12,
      "costUSD": 0.297423,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 521,
      "outputTokens": 8411,
      "cacheReadInputTokens": 586194,
      "cacheCreationInputTokens": 51066,
      "webSearchRequests": 0,
      "costUSD": 0.8251394999999999,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "3b7ffbff-4918-4259-a9f5-9099ac90476e"
}
```

</details>

---
