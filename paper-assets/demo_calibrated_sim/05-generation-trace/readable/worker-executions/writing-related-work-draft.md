# writing related work draft

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 22
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/workers/worker_writing_related-work-draft_20260513T081949.log`
- **Structured JSON:** [`b8c24d071f09de125ab2.json`](../../sessions/b8/b8c24d071f09de125ab2.json)

## Before a recorded user message

22 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl",
  "session_id": "2abdebbe-f3bd-4182-bff6-4d04fba6ecf2",
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
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__update_registry"
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
  "uuid": "f214e99d-5703-4d48-aada-d87b1d054ca3",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-cost-verify-agent-rl/memory/"
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
    "resetsAt": 1778674800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "85f4a11b-fe87-44b6-856e-d3696e93f40c",
  "session_id": "2abdebbe-f3bd-4182-bff6-4d04fba6ecf2"
}
```

---

### Assistant

_source line 4_

I'll start by reading the two source materials.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2abdebbe-f3bd-4182-bff6-4d04fba6ecf2",
  "uuid": "eda297b0-92fe-4a9e-ac8c-6283c9599836",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UVEbFSbpuRjE41A2VQnX9G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11720,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11720
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_016D5j2GEQKv5sLj6jJ6Uhsj`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
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
  "session_id": "2abdebbe-f3bd-4182-bff6-4d04fba6ecf2",
  "uuid": "5e6c3c06-35b5-48d2-9cc7-508be2d047f8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UVEbFSbpuRjE41A2VQnX9G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11720,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11720
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

_source line 6 · 2026-05-13T08:20:01.151Z_

<details><summary>↩ Tool result · `toolu_016D5j2GEQKv5sLj6jJ6Uhsj`</summary>

````text
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
  "session_id": "2abdebbe-f3bd-4182-bff6-4d04fba6ecf2",
  "uuid": "6e0caae1-eb1b-4a6e-b733-479f02c1319f",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file",
    "total_deferred_tools": 25
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Now let me read both source files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2abdebbe-f3bd-4182-bff6-4d04fba6ecf2",
  "uuid": "60aac340-33ee-4fa8-bde6-fbb17fe7ef99",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QZYaGvNpujb38AXZdEfTqP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 445,
      "cache_read_input_tokens": 23561,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 445
      },
      "output_tokens": 34,
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01R7eBJ1UoQ7BSt39jxyednh`</summary>

```json
{
  "project": "cost-verify-agent-rl",
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
  "session_id": "2abdebbe-f3bd-4182-bff6-4d04fba6ecf2",
  "uuid": "776fc50a-ccf3-4714-8a02-eecd63839b31",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QZYaGvNpujb38AXZdEfTqP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 445,
      "cache_read_input_tokens": 23561,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 445
      },
      "output_tokens": 34,
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

_source line 9 · 2026-05-13T08:20:04.911Z_

<details><summary>↩ Tool result · `toolu_01R7eBJ1UoQ7BSt39jxyednh`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml\", \"content\": \"papers:\\n  # ============================================================\\n  # DIRECT-COMPETITOR\\n  # ============================================================\\n  # 未找到直接竞品。没有现有工作专门做\\\"校准 LLM 用户模拟器的方言行为率偏差\\\"。\\n  # 最接近的是 Haq & Saldias 2026（归入 evaluation），但他们只量化偏差，不提出校准方法。\\n  # 这验证了 DemoCalib 的新颖性。\\n\\n  # ============================================================\\n  # FOUNDATION\\n  # ============================================================\\n  - id: seshadri2026lost\\n    title: \\\"Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations\\\"\\n    authors: \\\"Seshadri, Cahyawijaya, Odumakinde, Singh, Goldfarb-Tarrant\\\"\\n    venue: \\\"arXiv 2601.17087\\\"\\n    year: 2026\\n    url: \\\"https://arxiv.org/abs/2601.17087\\\"\\n    category: foundation\\n    role: \\\"Documents that LLM user simulators are differentially effective proxies across demographic groups; AAVE and Indian English speakers get worst calibration\\\"\\n    relevance: high\\n    key_findings:\\n      - \\\"Agent success rates vary up to 9pp across different user simulator LLMs\\\"\\n      - \\\"AAVE speakers experience consistently worse success rates and calibration errors than SAE speakers\\\"\\n      - \\\"Simulated users introduce conversational artifacts absent from real human users\\\"\\n      - \\\"Disparities compound significantly with age for AAVE speakers\\\"\\n    how_we_differ: \\\"They document the problem; we document why both BCP and DPO calibration fail to close the gaps, providing a failure taxonomy\\\"\\n\\n  - id: yao2024taubench\\n    title: \\\"tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains\\\"\\n    authors: \\\"Yao et al.\\\"\\n    venue: \\\"arXiv 2406.12045\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2406.12045\\\"\\n    category: foundation\\n    role: \\\"The agent evaluation framework we build on; provides retail customer service domain with user simulator + tool-calling agent + pass^k metric\\\"\\n    relevance: high\\n    key_findings:\\n      - \\\"Even gpt-4o succeeds on <50% of tasks; pass^8 <25% in retail\\\"\\n      - \\\"Proposes pass^k metric measuring reliability over multiple trials\\\"\\n      - \\\"User simulator is LLM-based, enabling behavioral modification\\\"\\n    how_we_differ: \\\"We extend tau-bench by documenting systematic failure modes when calibrating the user simulator's dialect-specific behavioral rates\\\"\\n\\n  - id: liu2024agentbench\\n    title: \\\"AgentBench: Evaluating LLMs as Agents\\\"\\n    authors: \\\"Liu et al.\\\"\\n    venue: \\\"ICLR 2024\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2308.03688\\\"\\n    category: foundation\\n    role: \\\"Multi-environment agent benchmark; establishes evaluation methodology for LLM agents across 8 environments\\\"\\n    relevance: medium\\n    key_findings:\\n      - \\\"Significant performance gap between commercial and open-source LLMs as agents\\\"\\n      - \\\"Poor long-term reasoning and instruction following are main obstacles\\\"\\n    how_we_differ: \\\"AgentBench evaluates agent capability; we focus on user simulator fidelity and fairness\\\"\\n\\n  - id: wang2024mint\\n    title: \\\"MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback\\\"\\n    authors: \\\"Wang, Wang, Liu, Chen, Yuan, Peng, Ji\\\"\\n    venue: \\\"ICLR 2024\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2309.10691\\\"\\n    category: foundation\\n    role: \\\"Multi-turn agent evaluation benchmark; shows gap between single-turn and multi-turn performance\\\"\\n    relevance: medium\\n    key_findings:\\n      - \\\"LLMs benefit 1-8% per turn from tools, 2-17% from language feedback\\\"\\n      - \\\"Better single-turn performance does not guarantee better multi-turn performance\\\"\\n      - \\\"SIFT and RLHF generally hurt multi-turn capabilities\\\"\\n    how_we_differ: \\\"MINT uses GPT-4 simulated users without demographic variation; we investigate dialect-aware calibration and document its failure modes\\\"\\n\\n  # ============================================================\\n  # METHOD-COMPONENT\\n  # ============================================================\\n  - id: rafailov2023dpo\\n    title: \\\"Direct Preference Optimization: Your Language Model is Secretly a Reward Model\\\"\\n    authors: \\\"Rafailov, Sharma, Mitchell, Manning, Ermon, Finn\\\"\\n    venue: \\\"NeurIPS 2023\\\"\\n    year: 2023\\n    url: \\\"https://arxiv.org/abs/2305.18290\\\"\\n    category: method-component\\n    role: \\\"Core algorithm for our DPO-based behavioral alignment; eliminates need for reward model training\\\"\\n    relevance: high\\n    key_findings:\\n      - \\\"DPO directly optimizes policy from preference pairs without explicit reward model\\\"\\n      - \\\"Computationally lightweight, stable alternative to PPO-based RLHF\\\"\\n      - \\\"Exceeds PPO-based RLHF in controlling sentiment of generations\\\"\\n    how_we_differ: \\\"We apply DPO to attempt dialect behavioral calibration and document its systematic failure modes including calibration reversal\\\"\\n\\n  - id: zhao2021calibrate\\n    title: \\\"Calibrate Before Use: Improving Few-Shot Performance of Language Models\\\"\\n    authors: \\\"Zhao, Wallace, Feng, Klein, Singh\\\"\\n    venue: \\\"ICML 2021\\\"\\n    year: 2021\\n    url: \\\"https://arxiv.org/abs/2102.09690\\\"\\n    category: method-component\\n    role: \\\"Foundational calibration method for LLMs; contextual calibration corrects output distribution biases\\\"\\n    relevance: medium\\n    key_findings:\\n      - \\\"Few-shot accuracy varies from near chance to near SOTA depending on prompt format\\\"\\n      - \\\"Identified majority label bias, recency bias, common token bias\\\"\\n      - \\\"Contextual calibration with content-free inputs improves accuracy up to 30%\\\"\\n    how_we_differ: \\\"They calibrate classification outputs; we attempt to calibrate behavioral rates (question rate, politeness) in generation and document why it fails\\\"\\n\\n  - id: abdulhai2025consistent\\n    title: \\\"Consistently Simulating Human Personas with Multi-Turn Reinforcement Learning\\\"\\n    authors: \\\"Abdulhai, Cheng, Clay, Althoff, Levine, Jaques\\\"\\n    venue: \\\"NeurIPS 2025\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2511.00222\\\"\\n    category: method-component\\n    role: \\\"Multi-turn RL for persona consistency; directly relevant to maintaining calibrated behavior across conversation turns\\\"\\n    relevance: high\\n    key_findings:\\n      - \\\"Off-the-shelf LLMs drift from assigned personas over multi-turn dialogue\\\"\\n      - \\\"Three automatic metrics: prompt-to-line, line-to-line, Q&A consistency\\\"\\n      - \\\"Multi-turn RL reduces inconsistency by >55%\\\"\\n    how_we_differ: \\\"They optimize persona consistency in general; we document failure modes when targeting dialect behavioral rate calibration\\\"\\n\\n  - id: naous2025flipping\\n    title: \\\"Flipping the Dialogue: Training and Evaluating User Language Models\\\"\\n    authors: \\\"Naous, Laban, Xu, Neville\\\"\\n    venue: \\\"arXiv 2510.06552\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2510.06552\\\"\\n    category: method-component\\n    role: \\\"Purpose-built User LMs outperform repurposed assistant LMs as user simulators; validates need for specialized user models\\\"\\n    relevance: high\\n    key_findings:\\n      - \\\"Better assistant LMs yield worse user simulators\\\"\\n      - \\\"UserLM-8b provides more realistic user simulation\\\"\\n      - \\\"GPT-4o performance drops from 74.6% to 57.4% under realistic user simulation\\\"\\n    how_we_differ: \\\"They train general User LMs; we document why calibrating user simulator behavioral rates for specific dialect groups fails\\\"\\n\\n  - id: li2025persona\\n    title: \\\"LLM Generated Persona is a Promise with a Catch\\\"\\n    authors: \\\"Li, Chen et al.\\\"\\n    venue: \\\"NeurIPS 2025\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2503.16527\\\"\\n    category: method-component\\n    role: \\\"Documents systematic biases in LLM-generated personas; explains why naive persona prompting fails for demographic simulation\\\"\\n    relevance: medium\\n    key_findings:\\n      - \\\"LLM-generated personas systematically drift toward socially desirable traits\\\"\\n      - \\\"More LLM-generated content produces more left-leaning, less representative personas\\\"\\n      - \\\"Bias exists in the persona creation step itself, not just model responses\\\"\\n    how_we_differ: \\\"We document failure modes when directly injecting behavioral rate targets via BCP, including persona-like completion collapse\\\"\\n\\n  - id: wang2024alignment\\n    title: \\\"A Comprehensive Survey of LLM Alignment Techniques: RLHF, RLAIF, PPO, DPO and More\\\"\\n    authors: \\\"Wang, Bi, Pentyala et al.\\\"\\n    venue: \\\"arXiv 2407.16216\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2407.16216\\\"\\n    category: method-component\\n    role: \\\"Survey unifying alignment methods under single policy gradient framework; reference for our DPO methodology\\\"\\n    relevance: medium\\n    key_findings:\\n      - \\\"Unified policy gradient framework for pretraining, SFT, RLHF, RLVR\\\"\\n      - \\\"DPO is stable and lightweight but sensitive to preference data quality\\\"\\n      - \\\"Detailed comparison of PPO vs GRPO vs DPO implementation details\\\"\\n    how_we_differ: \\\"Survey provides methodology reference; we apply DPO to user simulator dialect calibration and document its failure modes\\\"\\n\\n  # ============================================================\\n  # EVALUATION\\n  # ============================================================\\n  - id: lin2025redial\\n    title: \\\"Assessing Dialect Fairness and Robustness of Large Language Models in Reasoning Tasks\\\"\\n    authors: \\\"Lin et al.\\\"\\n    venue: \\\"ACL 2025\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2410.11005\\\"\\n    category: evaluation\\n    role: \\\"First human-annotated SE-AAVE parallel benchmark (ReDial); quantifies LLM performance gaps on AAVE\\\"\\n    relevance: high\\n    key_findings:\\n      - \\\"1.2K+ parallel SE-AAVE prompt pairs across reasoning tasks\\\"\\n      - \\\"Almost all models show statistically significant performance drops on AAVE\\\"\\n      - \\\"AAVE performance gaps arise from morphosyntactic features and conversational norms\\\"\\n      - \\\"LLMs struggle more with AAVE than misspelled Standard English\\\"\\n    how_we_differ: \\\"ReDial evaluates reasoning task performance; we evaluate behavioral rates in user simulation and document calibration failure modes\\\"\\n\\n  - id: faisal2024dialectbench\\n    title: \\\"DialectBench: A NLP Benchmark for Dialects, Varieties, and Closely-Related Languages\\\"\\n    authors: \\\"Faisal et al.\\\"\\n    venue: \\\"ACL 2024\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2403.11009\\\"\\n    category: evaluation\\n    role: \\\"Large-scale multi-dialect NLP benchmark; documents performance disparities across 281 language varieties\\\"\\n    relevance: medium\\n    key_findings:\\n      - \\\"10 NLP tasks, 281 varieties, 40 language clusters\\\"\\n      - \\\"Substantial performance disparities between standard and non-standard varieties\\\"\\n      - \\\"Performance gap widens with fine-tuning due to uneven data availability\\\"\\n    how_we_differ: \\\"DialectBench evaluates NLP task performance; we document failure modes in behavioral calibration of user simulators\\\"\\n\\n  - id: gallegos2024bias\\n    title: \\\"Bias and Fairness in Large Language Models: A Survey\\\"\\n    authors: \\\"Gallegos, Rossi, Barrow et al.\\\"\\n    venue: \\\"Computational Linguistics, Vol. 50(3)\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2309.00770\\\"\\n    category: evaluation\\n    role: \\\"Comprehensive survey of LLM bias evaluation and mitigation; provides taxonomy of metrics and datasets\\\"\\n    relevance: medium\\n    key_findings:\\n      - \\\"Taxonomy of bias metrics at embedding, probability, and generated text levels\\\"\\n      - \\\"Mitigation methods categorized by intervention stage: pre/in/intra/post-processing\\\"\\n      - \\\"Consolidated public datasets for bias evaluation\\\"\\n    how_we_differ: \\\"Survey covers general LLM bias; we address a specific bias modality (behavioral rates in user simulation)\\\"\\n\\n  - id: parrish2022bbq\\n    title: \\\"BBQ: A Hand-Built Bias Benchmark for Question Answering\\\"\\n    authors: \\\"Parrish et al.\\\"\\n    venue: \\\"Findings of ACL 2022\\\"\\n    year: 2022\\n    url: \\\"https://aclanthology.org/2022.findings-acl.165/\\\"\\n    category: evaluation\\n    role: \\\"Established bias benchmark for QA; evaluates social biases across multiple demographic categories\\\"\\n    relevance: low\\n    key_findings:\\n      - \\\"58,492 unique examples across multiple bias categories\\\"\\n      - \\\"Evaluates both individual and intersectional biases\\\"\\n      - \\\"Standard benchmark for LLM bias evaluation\\\"\\n    how_we_differ: \\\"BBQ measures representational bias in QA; we measure behavioral bias in interactive dialogue simulation\\\"\\n\\n  - id: haq2026dialect\\n    title: \\\"Dialect vs Demographics: Quantifying LLM Bias from Implicit Linguistic Signals vs. Explicit User Profiles\\\"\\n    authors: \\\"Haq, Saldias\\\"\\n    venue: \\\"arXiv 2604.21152\\\"\\n    year: 2026\\n    url: \\\"https://arxiv.org/abs/2604.21152\\\"\\n    category: evaluation\\n    role: \\\"Closest to direct competitor; quantifies how dialect cues vs explicit identity trigger differential LLM behavior\\\"\\n    relevance: high\\n    key_findings:\\n      - \\\"Dialect cues trigger 'dialect jailbreak' reducing refusal probability to near zero\\\"\\n      - \\\"AAVE/Singlish users receive less sanitized content than SAE users\\\"\\n      - \\\"Safety alignment is brittle, over-indexed on explicit keywords\\\"\\n      - \\\"24,000+ responses analyzed across two LLMs\\\"\\n    how_we_differ: \\\"They characterize the bias mechanism (implicit vs explicit); we document why calibration methods fail to correct behavioral rates\\\"\\n\\n  # ============================================================\\n  # BACKGROUND\\n  # ============================================================\\n  - id: joshi2025dialect_survey\\n    title: \\\"Natural Language Processing for Dialects of a Language: A Survey\\\"\\n    authors: \\\"Joshi, Dabre, Kanojia, Li, Zhan, Haffari, Dippold\\\"\\n    venue: \\\"ACM Computing Surveys, Vol. 57(6)\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2401.05632\\\"\\n    category: background\\n    role: \\\"Comprehensive survey of NLP for dialects; covers datasets, approaches, and performance gaps across dialect varieties\\\"\\n    relevance: medium\\n    key_findings:\\n      - \\\"NLP models show systematic performance degradation on dialectal data\\\"\\n      - \\\"Covers NLU and NLG tasks including dialogue systems\\\"\\n      - \\\"Equity implications of language technology performance gaps\\\"\\n    how_we_differ: \\\"Survey provides broad context; we tackle a specific gap in user simulation fairness\\\"\\n\\n  - id: rickford1999aave\\n    title: \\\"African American Vernacular English: Features, Evolution, Educational Implications\\\"\\n    authors: \\\"Rickford, John Russell\\\"\\n    venue: \\\"Blackwell Publishers (Language in Society series)\\\"\\n    year: 1999\\n    url: \\\"https://www.amazon.com/African-American-Vernacular-English-Implications/dp/0631212450\\\"\\n    category: background\\n    role: \\\"Authoritative reference on AAVE phonological, grammatical, and pragmatic features; grounds our behavioral rate targets\\\"\\n    relevance: medium\\n    key_findings:\\n      - \\\"Systematic documentation of AAVE phonological and grammatical features\\\"\\n      - \\\"AAVE has distinct pragmatic conventions including directness patterns\\\"\\n      - \\\"AAVE is a fully systematic linguistic variety, not deficient English\\\"\\n    how_we_differ: \\\"Provides sociolinguistic grounding for what behavioral patterns we should calibrate toward\\\"\\n\\n  - id: kachru2008cultures\\n    title: \\\"Cultures, Contexts, and World Englishes\\\"\\n    authors: \\\"Kachru, Yamuna; Smith, Cecil\\\"\\n    venue: \\\"Routledge\\\"\\n    year: 2008\\n    url: \\\"https://www.routledge.com/Cultures-Contexts-and-World-Englishes/Kachru-Smith/p/book/9780805847338\\\"\\n    category: background\\n    role: \\\"Framework for Indian English pragmatics; documents politeness strategies and speech act differences in Outer Circle Englishes\\\"\\n    relevance: medium\\n    key_findings:\\n      - \\\"Indian English has distinct politeness strategies rooted in face-saving norms\\\"\\n      - \\\"Requesting and disagreeing strategies differ from Inner Circle varieties\\\"\\n      - \\\"Three Circles model (Inner/Outer/Expanding) for understanding English variation\\\"\\n    how_we_differ: \\\"Provides sociolinguistic grounding for Indian English behavioral patterns we attempt to calibrate\\\"\\n\\n  - id: sekulic2024daus\\n    title: \\\"Reliable LLM-based User Simulator for Task-Oriented Dialogue Systems\\\"\\n    authors: \\\"Sekulic, Terragni, Guimaraes et al.\\\"\\n    venue: \\\"SCI-CHAT Workshop 2024\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2402.13374\\\"\\n    category: background\\n    role: \\\"DAUS: domain-aware user simulator fine-tuned on real dialogues; shows fine-tuning improves goal fulfillment and reduces hallucination\\\"\\n    relevance: medium\\n    key_findings:\\n      - \\\"Fine-tuning LLMs on real dialogue examples improves user goal fulfillment\\\"\\n      - \\\"Mitigates hallucinations in simulator responses\\\"\\n      - \\\"Domain-aware approach outperforms generic prompting\\\"\\n    how_we_differ: \\\"DAUS optimizes task completion; we document failure modes when optimizing demographic behavioral fidelity\\\"\\n\\n  - id: ahmad2025diversity\\n    title: \\\"Simulating User Diversity in Task-Oriented Dialogue Systems using Large Language Models\\\"\\n    authors: \\\"Ahmad, Hillmann, Moller\\\"\\n    venue: \\\"arXiv 2502.12813\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2502.12813\\\"\\n    category: background\\n    role: \\\"Generates diverse user profiles with varied demographics and conversational styles for dialogue evaluation\\\"\\n    relevance: medium\\n    key_findings:\\n      - \\\"GPT-o1 generates more heterogeneous user distributions than GPT-4o\\\"\\n      - \\\"82.46% task success across 57 dialogue sessions with diverse users\\\"\\n      - \\\"Captures variation in language styles, knowledge levels, and objectives\\\"\\n    how_we_differ: \\\"They generate diverse profiles; we document why calibrating specific behavioral rates to match real dialect group distributions fails\\\"\\n\\n  # ============================================================\\n  # NEW ADDITIONS (scan 2026-05-13)\\n  # ============================================================\\n\\n  # --- FOUNDATION (new) ---\\n  - id: sim2real2026gap\\n    title: \\\"Mind the Sim2Real Gap in User Simulation for Agentic Tasks\\\"\\n    authors: \\\"Zhou, Sun, Xu, Chen, Radev\\\"\\n    venue: \\\"arXiv 2603.11245\\\"\\n    year: 2026\\n    url: \\\"https://arxiv.org/abs/2603.11245\\\"\\n    category: foundation\\n    role: \\\"First study running full τ-bench protocol with 451 real humans; introduces USI metric to quantify sim-vs-human behavioral divergence\\\"\\n    relevance: high\\n    key_findings:\\n      - \\\"LLM simulators are excessively cooperative, stylistically uniform, and lack realistic frustration/ambiguity\\\"\\n      - \\\"Simulated users create 'easy mode' that inflates agent success rates above human baseline\\\"\\n      - \\\"Simulated feedback is uniformly positive; humans express calibrated dissatisfaction\\\"\\n      - \\\"Higher model capability does not yield more faithful user simulation\\\"\\n    how_we_differ: \\\"They quantify the sim2real gap but do not propose calibration methods; we attempt BCP and DPO calibration and document why both fail\\\"\\n    scan_date: \\\"2026-05-13\\\"\\n    note: \\\"Near-competitor in problem framing — directly validates our motivation. Not a direct competitor because they diagnose without prescribing a fix.\\\"\\n\\n  # --- METHOD-COMPONENT (new) ---\\n  - id: khan2026decoding\\n    title: \\\"Decoding-Time Debiasing via Process Reward Models: From Controlled Fill-in to Open-Ended Generation\\\"\\n    authors: \\\"Khan, Muneeb Ur Raheem\\\"\\n    venue: \\\"arXiv 2605.02348\\\"\\n    year: 2026\\n    url: \\\"https://arxiv.org/abs/2605.02348\\\"\\n    category: method-component\\n    role: \\\"Decoding-time bias mitigation using Process Reward Model as fairness judge; alternative to our training-time DPO approach\\\"\\n    relevance: medium\\n    key_findings:\\n      - \\\"Sequential debiasing raises bias scores by up to +0.40 over baseline while preserving fluency\\\"\\n      - \\\"No weight changes needed — debiasing happens at inference via PRM scoring\\\"\\n      - \\\"Gate calibration is model-dependent; no one-size-fits-all prompt works\\\"\\n    how_we_differ: \\\"They debias at decoding time for general fairness; we document failure modes of training-time calibration (BCP+DPO), motivating alternative approaches like decoding-time methods\\\"\\n    scan_date: \\\"2026-05-13\\\"\\n\\n  # --- EVALUATION (new) ---\\n  - id: gupta2025endive\\n    title: \\\"EnDive: A Cross-Dialect Benchmark for Fairness and Performance in Large Language Models\\\"\\n    authors: \\\"Gupta, Cheung et al.\\\"\\n    venue: \\\"Findings of EMNLP 2025 (arXiv 2504.07100)\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2504.07100\\\"\\n    category: evaluation\\n    role: \\\"Cross-dialect benchmark covering 5 dialects including AAVE and Indian English — both our target dialects\\\"\\n    relevance: high\\n    key_findings:\\n      - \\\"Covers AAVE (33M speakers), Indian English (250M speakers), Jamaican, Chicano, Singaporean English\\\"\\n      - \\\"Few-shot LLM translation of SE to dialects, validated by native speakers (avg 6.02/7 faithfulness)\\\"\\n      - \\\"LLMs show performance drops on non-standard dialects across understanding, reasoning, math, logic\\\"\\n    how_we_differ: \\\"EnDive evaluates NLP task performance across dialects; we document calibration failure modes for user simulators targeting those same dialect groups\\\"\\n    scan_date: \\\"2026-05-13\\\"\\n\\n  # --- METHOD-COMPONENT (new, Plan B relevant) ---\\n  - id: lee2024dpo_toxicity\\n    title: \\\"A Mechanistic Understanding of Alignment Algorithms: A Case Study on DPO and Toxicity\\\"\\n    authors: \\\"Lee, Panda, Yun, Bansal\\\"\\n    venue: \\\"ICML 2024\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2401.01967\\\"\\n    category: method-component\\n    role: \\\"Shows DPO bypasses rather than removes pre-training capabilities; explains mechanistically why DPO+BCP can reverse calibration direction\\\"\\n    relevance: high\\n    key_findings:\\n      - \\\"DPO does not remove toxic capabilities, only bypasses them at inference\\\"\\n      - \\\"Simple un-alignment can revert model to pre-DPO behavior\\\"\\n      - \\\"Minimal parameter changes allow reversion — alignment is fragile\\\"\\n    how_we_differ: \\\"They study DPO toxicity mechanics; we document DPO+BCP calibration reversal as a specific failure mode\\\"\\n    scan_date: \\\"2026-05-13\\\"\\n    plan_b_relevance: \\\"FM4 — explains why DPO training can reverse BCP calibration effect\\\"\\n\\n  - id: gupta2026intra_fairness\\n    title: \\\"Intra-Fairness Dynamics: The Bias Spillover Effect in Targeted LLM Alignment\\\"\\n    authors: \\\"Paraschou, Heiter, Iosifidis\\\"\\n    venue: \\\"arXiv 2602.16438\\\"\\n    year: 2026\\n    url: \\\"https://arxiv.org/abs/2602.16438\\\"\\n    category: method-component\\n    role: \\\"Documents bias spillover — targeted debiasing on one dimension causes unintended effects on other dimensions; directly parallels our cross-dimension interference\\\"\\n    relevance: high\\n    key_findings:\\n      - \\\"Targeted debiasing can produce unintended negative consequences across other social axes\\\"\\n      - \\\"Bias spillover effect: altering behavior on one dimension when mitigating another\\\"\\n      - \\\"Multi-attribute fairness dynamics must be considered in alignment\\\"\\n    how_we_differ: \\\"They study bias spillover in general alignment; we document the specific cross-dimension interference pattern in BCP-based behavioral calibration\\\"\\n    scan_date: \\\"2026-05-13\\\"\\n    plan_b_relevance: \\\"FM2 + FM4 — directly supports cross-dimension interference and DPO spillover claims\\\"\\n\\n  - id: basil2025playing_pretend\\n    title: \\\"Prompting Science Report 4: Playing Pretend: Expert Personas Don't Improve Factual Accuracy\\\"\\n    authors: \\\"Basil, Shapiro, Shapiro, Mollick, Mollick, Meincke\\\"\\n    venue: \\\"arXiv 2512.05858 (Wharton)\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2512.05858\\\"\\n    category: method-component\\n    role: \\\"Shows persona prompting degrades factual accuracy; BCP is a form of persona/role prompting, explaining completion collapse\\\"\\n    relevance: high\\n    key_findings:\\n      - \\\"Expert personas do not improve factual accuracy across benchmarks\\\"\\n      - \\\"Persona prompting activates instruction-following mode at expense of factual recall\\\"\\n      - \\\"MMLU accuracy drops from 71.6% baseline to 66.3% with detailed persona\\\"\\n    how_we_differ: \\\"They study persona prompting in classification/QA; we document the same mechanism in multi-turn dialogue task completion\\\"\\n    scan_date: \\\"2026-05-13\\\"\\n    plan_b_relevance: \\\"FM1 — explains mechanism behind global behavior suppression\\\"\\n\\n  - id: hu2026expert_persona\\n    title: \\\"Expert Personas Improve LLM Alignment but Damage Accuracy: Bootstrapping Intent-Based Persona Routing with PRISM\\\"\\n    authors: \\\"Hu, Rostami, Thomason\\\"\\n    venue: \\\"arXiv 2603.18507\\\"\\n    year: 2026\\n    url: \\\"https://arxiv.org/abs/2603.18507\\\"\\n    category: method-component\\n    role: \\\"Systematically documents persona prompting trade-off: alignment improves but accuracy degrades up to 30pp; directly explains BCP completion collapse\\\"\\n    relevance: high\\n    key_findings:\\n      - \\\"Persona prompting improves alignment tasks but degrades knowledge/reasoning tasks\\\"\\n      - \\\"Performance drops up to 30pp under persona modifications\\\"\\n      - \\\"More instruction-tuned models are more susceptible to persona-induced accuracy loss\\\"\\n    how_we_differ: \\\"They study general persona-accuracy trade-off; we document the specific completion collapse in agent-user dialogue under behavioral calibration prompts\\\"\\n    scan_date: \\\"2026-05-13\\\"\\n    plan_b_relevance: \\\"FM1 — strongest external evidence for global behavior suppression mechanism\\\"\\n\\n  # --- BACKGROUND (new) ---\\n  - id: nakash2026divert\\n    title: \\\"Efficient Agent Evaluation via Diversity-Guided User Simulation\\\"\\n    authors: \\\"Nakash, Kour, Anaby-Tavor\\\"\\n    venue: \\\"arXiv 2604.21480\\\"\\n    year: 2026\\n    url: \\\"https://arxiv.org/abs/2604.21480\\\"\\n    category: background\\n    role: \\\"DIVERT framework for efficient agent evaluation via branching trajectories; addresses Monte Carlo inefficiency in agent evaluation\\\"\\n    relevance: medium\\n    key_findings:\\n      - \\\"Snapshot-based branching avoids redundant regeneration of early conversation prefixes\\\"\\n      - \\\"Coverage-guided exploration uncovers deep failure modes from rare user behaviors\\\"\\n    how_we_differ: \\\"They optimize evaluation efficiency; we document failure modes in user simulator fidelity calibration for dialect groups\\\"\\n    scan_date: \\\"2026-05-13\\\"\\n\\n# ============================================================\\n# SUMMARY\\n# ============================================================\\n# Total: 28 papers (updated 2026-05-13, +8 new, +4 Plan B scan)\\n# - direct-competitor: 0 (novelty still confirmed — no one has done systematic BCP failure analysis)\\n# - foundation: 5 (+sim2real2026gap)\\n# - method-component: 12 (+khan2026decoding, +lee2024dpo_toxicity, +gupta2026intra_fairness, +basil2025playing_pretend, +hu2026expert_persona)\\n# - evaluation: 6 (+gupta2025endive)\\n# - background: 6 (+nakash2026divert)\\n# - high relevance: 14, medium: 13, low: 1\\n#\\n# Plan B scan notes (2026-05-13):\\n# - 4 new papers added specifically for Plan B empirical analysis framing\\n# - lee2024dpo_toxicity: mechanistic explanation for FM4 (DPO+BCP reversal)\\n# - gupta2026intra_fairness: external evidence for FM2 (cross-dimension interference) + FM4 (spillover)\\n# - basil2025playing_pretend + hu2026expert_persona: external evidence for FM1 (completion collapse via persona prompting)\\n# - No direct competitor found for BCP failure mode analysis — novelty gap confirmed\\n# - Also noted but not added:\\n#   - ϕ-DPO (2602.22601): Fairness DPO for multimodal continual learning, different domain\\n#   - Linguistic Stereotypes (2603.18729): SAE vs AAE bias in multi-agent architectures\\n\", \"total_chars\": 26989, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2abdebbe-f3bd-4182-bff6-4d04fba6ecf2",
  "uuid": "dd32b04b-76d9-406c-b882-a5b688363ced",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml\\\", \\\"content\\\": \\\"papers:\\\\n  # ============================================================\\\\n  # DIRECT-COMPETITOR\\\\n  # ============================================================\\\\n  # 未找到直接竞品。没有现有工作专门做\\\\\\\"校准 LLM 用户模拟器的方言行为率偏差\\\\\\\"。\\\\n  # 最接近的是 Haq & Saldias 2026（归入 evaluation），但他们只量化偏差，不提出校准方法。\\\\n  # 这验证了 DemoCalib 的新颖性。\\\\n\\\\n  # ============================================================\\\\n  # FOUNDATION\\\\n  # ============================================================\\\\n  - id: seshadri2026lost\\\\n    title: \\\\\\\"Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations\\\\\\\"\\\\n    authors: \\\\\\\"Seshadri, Cahyawijaya, Odumakinde, Singh, Goldfarb-Tarrant\\\\\\\"\\\\n    venue: \\\\\\\"arXiv 2601.17087\\\\\\\"\\\\n    year: 2026\\\\n    url: \\\\\\\"https://arxiv.org/abs/2601.17087\\\\\\\"\\\\n    category: foundation\\\\n    role: \\\\\\\"Documents that LLM user simulators are differentially effective proxies across demographic groups; AAVE and Indian English speakers get worst calibration\\\\\\\"\\\\n    relevance: high\\\\n    key_findings:\\\\n      - \\\\\\\"Agent success rates vary up to 9pp across different user simulator LLMs\\\\\\\"\\\\n      - \\\\\\\"AAVE speakers experience consistently worse success rates and calibration errors than SAE speakers\\\\\\\"\\\\n      - \\\\\\\"Simulated users introduce conversational artifacts absent from real human users\\\\\\\"\\\\n      - \\\\\\\"Disparities compound significantly with age for AAVE speakers\\\\\\\"\\\\n    how_we_differ: \\\\\\\"They document the problem; we document why both BCP and DPO calibration fail to close the gaps, providing a failure taxonomy\\\\\\\"\\\\n\\\\n  - id: yao2024taubench\\\\n    title: \\\\\\\"tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains\\\\\\\"\\\\n    authors: \\\\\\\"Yao et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv 2406.12045\\\\\\\"\\\\n    year: 2024\\\\n    url: \\\\\\\"https://arxiv.org/abs/2406.12045\\\\\\\"\\\\n    category: foundation\\\\n    role: \\\\\\\"The agent evaluation framework we build on; provides retail customer service domain with user simulator + tool-calling agent + pass^k metric\\\\\\\"\\\\n    relevance: high\\\\n    key_findings:\\\\n      - \\\\\\\"Even gpt-4o succeeds on <50% of tasks; pass^8 <25% in retail\\\\\\\"\\\\n      - \\\\\\\"Proposes pass^k metric measuring reliability over multiple trials\\\\\\\"\\\\n      - \\\\\\\"User simulator is LLM-based, enabling behavioral modification\\\\\\\"\\\\n    how_we_differ: \\\\\\\"We extend tau-bench by documenting systematic failure modes when calibrating the user simulator's dialect-specific behavioral rates\\\\\\\"\\\\n\\\\n  - id: liu2024agentbench\\\\n    title: \\\\\\\"AgentBench: Evaluating LLMs as Agents\\\\\\\"\\\\n    authors: \\\\\\\"Liu et al.\\\\\\\"\\\\n    venue: \\\\\\\"ICLR 2024\\\\\\\"\\\\n    year: 2024\\\\n    url: \\\\\\\"https://arxiv.org/abs/2308.03688\\\\\\\"\\\\n    category: foundation\\\\n    role: \\\\\\\"Multi-environment agent benchmark; establishes evaluation methodology for LLM agents across 8 environments\\\\\\\"\\\\n    relevance: medium\\\\n    key_findings:\\\\n      - \\\\\\\"Significant performance gap between commercial and open-source LLMs as agents\\\\\\\"\\\\n      - \\\\\\\"Poor long-term reasoning and instruction following are main obstacles\\\\\\\"\\\\n    how_we_differ: \\\\\\\"AgentBench evaluates agent capability; we focus on user simulator fidelity and fairness\\\\\\\"\\\\n\\\\n  - id: wang2024mint\\\\n    title: \\\\\\\"MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback\\\\\\\"\\\\n    authors: \\\\\\\"Wang, Wang, Liu, Chen, Yuan, Peng, Ji\\\\\\\"\\\\n    venue: \\\\\\\"ICLR 2024\\\\\\\"\\\\n    year: 2024\\\\n    url: \\\\\\\"https://arxiv.org/abs/2309.10691\\\\\\\"\\\\n    category: foundation\\\\n    role: \\\\\\\"Multi-turn agent evaluation benchmark; shows gap between single-turn and multi-turn performance\\\\\\\"\\\\n    relevance: medium\\\\n    key_findings:\\\\n      - \\\\\\\"LLMs benefit 1-8% per turn from tools, 2-17% from language feedback\\\\\\\"\\\\n      - \\\\\\\"Better single-turn performance does not guarantee better multi-turn performance\\\\\\\"\\\\n      - \\\\\\\"SIFT and RLHF generally hurt multi-turn capabilities\\\\\\\"\\\\n    how_we_differ: \\\\\\\"MINT uses GPT-4 simulated users without demographic variation; we investigate dialect-aware calibration and document its failure modes\\\\\\\"\\\\n\\\\n  # ============================================================\\\\n  # METHOD-COMPONENT\\\\n  # ============================================================\\\\n  - id: rafailov2023dpo\\\\n    title: \\\\\\\"Direct Preference Optimization: Your Language Model is Secretly a Reward Model\\\\\\\"\\\\n    authors: \\\\\\\"Rafailov, Sharma, Mitchell, Manning, Ermon, Finn\\\\\\\"\\\\n    venue: \\\\\\\"NeurIPS 2023\\\\\\\"\\\\n    year: 2023\\\\n    url: \\\\\\\"https://arxiv.org/abs/2305.18290\\\\\\\"\\\\n    category: method-component\\\\n    role: \\\\\\\"Core algorithm for our DPO-based behavioral alignment; eliminates need for reward model training\\\\\\\"\\\\n    relevance: high\\\\n    key_findings:\\\\n      - \\\\\\\"DPO directly optimizes policy from preference pairs without explicit reward model\\\\\\\"\\\\n      - \\\\\\\"Computationally lightweight, stable alternative to PPO-based RLHF\\\\\\\"\\\\n      - \\\\\\\"Exceeds PPO-based RLHF in controlling sentiment of generations\\\\\\\"\\\\n    how_we_differ: \\\\\\\"We apply DPO to attempt dialect behavioral calibration and document its systematic failure modes including calibration reversal\\\\\\\"\\\\n\\\\n  - id: zhao2021calibrate\\\\n    title: \\\\\\\"Calibrate Before Use: Improving Few-Shot Performance of Language Models\\\\\\\"\\\\n    authors: \\\\\\\"Zhao, Wallace, Feng, Klein, Singh\\\\\\\"\\\\n    venue: \\\\\\\"ICML 2021\\\\\\\"\\\\n    year: 2021\\\\n    url: \\\\\\\"https://arxiv.org/abs/2102.09690\\\\\\\"\\\\n    category: method-component\\\\n    role: \\\\\\\"Foundational calibration method for LLMs; contextual calibration corrects output distribution biases\\\\\\\"\\\\n    relevance: medium\\\\n    key_findings:\\\\n      - \\\\\\\"Few-shot accuracy varies from near chance to near SOTA depending on prompt format\\\\\\\"\\\\n      - \\\\\\\"Identified majority label bias, recency bias, common token bias\\\\\\\"\\\\n      - \\\\\\\"Contextual calibration with content-free inputs improves accuracy up to 30%\\\\\\\"\\\\n    how_we_differ: \\\\\\\"They calibrate classification outputs; we attempt to calibrate behavioral rates (question rate, politeness) in generation and document why it fails\\\\\\\"\\\\n\\\\n  - id: abdulhai2025consistent\\\\n    title: \\\\\\\"Consistently Simulating Human Personas with Multi-Turn Reinforcement Learning\\\\\\\"\\\\n    authors: \\\\\\\"Abdulhai, Cheng, Clay, Althoff, Levine, Jaques\\\\\\\"\\\\n    venue: \\\\\\\"NeurIPS 2025\\\\\\\"\\\\n    year: 2025\\\\n    url: \\\\\\\"https://arxiv.org/abs/2511.00222\\\\\\\"\\\\n    category: method-component\\\\n    role: \\\\\\\"Multi-turn RL for persona consistency; directly relevant to maintaining calibrated behavior across conversation turns\\\\\\\"\\\\n    relevance: high\\\\n    key_findings:\\\\n      - \\\\\\\"Off-the-shelf LLMs drift from assigned personas over multi-turn dialogue\\\\\\\"\\\\n      - \\\\\\\"Three automatic metrics: prompt-to-line, line-to-line, Q&A consistency\\\\\\\"\\\\n      - \\\\\\\"Multi-turn RL reduces inconsistency by >55%\\\\\\\"\\\\n    how_we_differ: \\\\\\\"They optimize persona consistency in general; we document failure modes when targeting dialect behavioral rate calibration\\\\\\\"\\\\n\\\\n  - id: naous2025flipping\\\\n    title: \\\\\\\"Flipping the Dialogue: Training and Evaluating User Language Models\\\\\\\"\\\\n    authors: \\\\\\\"Naous, Laban, Xu, Neville\\\\\\\"\\\\n    venue: \\\\\\\"arXiv 2510.06552\\\\\\\"\\\\n    year: 2025\\\\n    url: \\\\\\\"https://arxiv.org/abs/2510.06552\\\\\\\"\\\\n    category: method-component\\\\n    role: \\\\\\\"Purpose-built User LMs outperform repurposed assistant LMs as user simulators; validates need for specialized user models\\\\\\\"\\\\n    relevance: high\\\\n    key_findings:\\\\n      - \\\\\\\"Better assistant LMs yield worse user simulators\\\\\\\"\\\\n      - \\\\\\\"UserLM-8b provides more realistic user simulation\\\\\\\"\\\\n      - \\\\\\\"GPT-4o performance drops from 74.6% to 57.4% under realistic user simulation\\\\\\\"\\\\n    how_we_differ: \\\\\\\"They train general User LMs; we document why calibrating user simulator behavioral rates for specific dialect groups fails\\\\\\\"\\\\n\\\\n  - id: li2025persona\\\\n    title: \\\\\\\"LLM Generated Persona is a Promise with a Catch\\\\\\\"\\\\n    authors: \\\\\\\"Li, Chen et al.\\\\\\\"\\\\n    venue: \\\\\\\"NeurIPS 2025\\\\\\\"\\\\n    year: 2025\\\\n    url: \\\\\\\"https://arxiv.org/abs/2503.16527\\\\\\\"\\\\n    category: method-component\\\\n    role: \\\\\\\"Documents systematic biases in LLM-generated personas; explains why naive persona prompting fails for demographic simulation\\\\\\\"\\\\n    relevance: medium\\\\n    key_findings:\\\\n      - \\\\\\\"LLM-generated personas systematically drift toward socially desirable traits\\\\\\\"\\\\n      - \\\\\\\"More LLM-generated content produces more left-leaning, less representative personas\\\\\\\"\\\\n      - \\\\\\\"Bias exists in the persona creation step itself, not just model responses\\\\\\\"\\\\n    how_we_differ: \\\\\\\"We document failure modes when directly injecting behavioral rate targets via BCP, including persona-like completion collapse\\\\\\\"\\\\n\\\\n  - id: wang2024alignment\\\\n    title: \\\\\\\"A Comprehensive Survey of LLM Alignment Techniques: RLHF, RLAIF, PPO, DPO and More\\\\\\\"\\\\n    authors: \\\\\\\"Wang, Bi, Pentyala et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv 2407.16216\\\\\\\"\\\\n    year: 2024\\\\n    url: \\\\\\\"https://arxiv.org/abs/2407.16216\\\\\\\"\\\\n    category: method-component\\\\n    role: \\\\\\\"Survey unifying alignment methods under single policy gradient framework; reference for our DPO methodology\\\\\\\"\\\\n    relevance: medium\\\\n    key_findings:\\\\n      - \\\\\\\"Unified policy gradient framework for pretraining, SFT, RLHF, RLVR\\\\\\\"\\\\n      - \\\\\\\"DPO is stable and lightweight but sensitive to preference data quality\\\\\\\"\\\\n      - \\\\\\\"Detailed comparison of PPO vs GRPO vs DPO implementation details\\\\\\\"\\\\n    how_we_differ: \\\\\\\"Survey provides methodology reference; we apply DPO to user simulator dialect calibration and document its failure modes\\\\\\\"\\\\n\\\\n  # ============================================================\\\\n  # EVALUATION\\\\n  # ============================================================\\\\n  - id: lin2025redial\\\\n    title: \\\\\\\"Assessing Dialect Fairness and Robustness of Large Language Models in Reasoning Tasks\\\\\\\"\\\\n    authors: \\\\\\\"Lin et al.\\\\\\\"\\\\n    venue: \\\\\\\"ACL 2025\\\\\\\"\\\\n    year: 2025\\\\n    url: \\\\\\\"https://arxiv.org/abs/2410.11005\\\\\\\"\\\\n    category: evaluation\\\\n    role: \\\\\\\"First human-annotated SE-AAVE parallel benchmark (ReDial); quantifies LLM performance gaps on AAVE\\\\\\\"\\\\n    relevance: high\\\\n    key_findings:\\\\n      - \\\\\\\"1.2K+ parallel SE-AAVE prompt pairs across reasoning tasks\\\\\\\"\\\\n      - \\\\\\\"Almost all models show statistically significant performance drops on AAVE\\\\\\\"\\\\n      - \\\\\\\"AAVE performance gaps arise from morphosyntactic features and conversational norms\\\\\\\"\\\\n      - \\\\\\\"LLMs struggle more with AAVE than misspelled Standard English\\\\\\\"\\\\n    how_we_differ: \\\\\\\"ReDial evaluates reasoning task performance; we evaluate behavioral rates in user simulation and document calibration failure modes\\\\\\\"\\\\n\\\\n  - id: faisal2024dialectbench\\\\n    title: \\\\\\\"DialectBench: A NLP Benchmark for Dialects, Varieties, and Closely-Related Languages\\\\\\\"\\\\n    authors: \\\\\\\"Faisal et al.\\\\\\\"\\\\n    venue: \\\\\\\"ACL 2024\\\\\\\"\\\\n    year: 2024\\\\n    url: \\\\\\\"https://arxiv.org/abs/2403.11009\\\\\\\"\\\\n    category: evaluation\\\\n    role: \\\\\\\"Large-scale multi-dialect NLP benchmark; documents performance disparities across 281 language varieties\\\\\\\"\\\\n    relevance: medium\\\\n    key_findings:\\\\n      - \\\\\\\"10 NLP tasks, 281 varieties, 40 language clusters\\\\\\\"\\\\n      - \\\\\\\"Substantial performance disparities between standard and non-standard varieties\\\\\\\"\\\\n      - \\\\\\\"Performance gap widens with fine-tuning due to uneven data availability\\\\\\\"\\\\n    how_we_differ: \\\\\\\"DialectBench evaluates NLP task performance; we document failure modes in behavioral calibration of user simulators\\\\\\\"\\\\n\\\\n  - id: gallegos2024bias\\\\n    title: \\\\\\\"Bias and Fairness in Large Language Models: A Survey\\\\\\\"\\\\n    authors: \\\\\\\"Gallegos, Rossi, Barrow et al.\\\\\\\"\\\\n    venue: \\\\\\\"Computational Linguistics, Vol. 50(3)\\\\\\\"\\\\n    year: 2024\\\\n    url: \\\\\\\"https://arxiv.org/abs/2309.00770\\\\\\\"\\\\n    category: evaluation\\\\n    role: \\\\\\\"Comprehensive survey of LLM bias evaluation and mitigation; provides taxonomy of metrics and datasets\\\\\\\"\\\\n    relevance: medium\\\\n    key_findings:\\\\n      - \\\\\\\"Taxonomy of bias metrics at embedding, probability, and generated text levels\\\\\\\"\\\\n      - \\\\\\\"Mitigation methods categorized by intervention stage: pre/in/intra/post-processing\\\\\\\"\\\\n      - \\\\\\\"Consolidated public datasets for bias evaluation\\\\\\\"\\\\n    how_we_differ: \\\\\\\"Survey covers general LLM bias; we address a specific bias modality (behavioral rates in user simulation)\\\\\\\"\\\\n\\\\n  - id: parrish2022bbq\\\\n    title: \\\\\\\"BBQ: A Hand-Built Bias Benchmark for Question Answering\\\\\\\"\\\\n    authors: \\\\\\\"Parrish et al.\\\\\\\"\\\\n    venue: \\\\\\\"Findings of ACL 2022\\\\\\\"\\\\n    year: 2022\\\\n    url: \\\\\\\"https://aclanthology.org/2022.findings-acl.165/\\\\\\\"\\\\n    category: evaluation\\\\n    role: \\\\\\\"Established bias benchmark for QA; evaluates social biases across multiple demographic categories\\\\\\\"\\\\n    relevance: low\\\\n    key_findings:\\\\n      - \\\\\\\"58,492 unique examples across multiple bias categories\\\\\\\"\\\\n      - \\\\\\\"Evaluates both individual and intersectional biases\\\\\\\"\\\\n      - \\\\\\\"Standard benchmark for LLM bias evaluation\\\\\\\"\\\\n    how_we_differ: \\\\\\\"BBQ measures representational bias in QA; we measure behavioral bias in interactive dialogue simulation\\\\\\\"\\\\n\\\\n  - id: haq2026dialect\\\\n    title: \\\\\\\"Dialect vs Demographics: Quantifying LLM Bias from Implicit Linguistic Signals vs. Explicit User Profiles\\\\\\\"\\\\n    authors: \\\\\\\"Haq, Saldias\\\\\\\"\\\\n    venue: \\\\\\\"arXiv 2604.21152\\\\\\\"\\\\n    year: 2026\\\\n    url: \\\\\\\"https://arxiv.org/abs/2604.21152\\\\\\\"\\\\n    category: evaluation\\\\n    role: \\\\\\\"Closest to direct competitor; quantifies how dialect cues vs explicit identity trigger differential LLM behavior\\\\\\\"\\\\n    relevance: high\\\\n    key_findings:\\\\n      - \\\\\\\"Dialect cues trigger 'dialect jailbreak' reducing refusal probability to near zero\\\\\\\"\\\\n      - \\\\\\\"AAVE/Singlish users receive less sanitized content than SAE users\\\\\\\"\\\\n      - \\\\\\\"Safety alignment is brittle, over-indexed on explicit keywords\\\\\\\"\\\\n      - \\\\\\\"24,000+ responses analyzed across two LLMs\\\\\\\"\\\\n    how_we_differ: \\\\\\\"They characterize the bias mechanism (implicit vs explicit); we document why calibration methods fail to correct behavioral rates\\\\\\\"\\\\n\\\\n  # ============================================================\\\\n  # BACKGROUND\\\\n  # ============================================================\\\\n  - id: joshi2025dialect_survey\\\\n    title: \\\\\\\"Natural Language Processing for Dialects of a Language: A Survey\\\\\\\"\\\\n    authors: \\\\\\\"Joshi, Dabre, Kanojia, Li, Zhan, Haffari, Dippold\\\\\\\"\\\\n    venue: \\\\\\\"ACM Computing Surveys, Vol. 57(6)\\\\\\\"\\\\n    year: 2025\\\\n    url: \\\\\\\"https://arxiv.org/abs/2401.05632\\\\\\\"\\\\n    category: background\\\\n    role: \\\\\\\"Comprehensive survey of NLP for dialects; covers datasets, approaches, and performance gaps across dialect varieties\\\\\\\"\\\\n    relevance: medium\\\\n    key_findings:\\\\n      - \\\\\\\"NLP models show systematic performance degradation on dialectal data\\\\\\\"\\\\n      - \\\\\\\"Covers NLU and NLG tasks including dialogue systems\\\\\\\"\\\\n      - \\\\\\\"Equity implications of language technology performance gaps\\\\\\\"\\\\n    how_we_differ: \\\\\\\"Survey provides broad context; we tackle a specific gap in user simulation fairness\\\\\\\"\\\\n\\\\n  - id: rickford1999aave\\\\n    title: \\\\\\\"African American Vernacular English: Features, Evolution, Educational Implications\\\\\\\"\\\\n    authors: \\\\\\\"Rickford, John Russell\\\\\\\"\\\\n    venue: \\\\\\\"Blackwell Publishers (Language in Society series)\\\\\\\"\\\\n    year: 1999\\\\n    url: \\\\\\\"https://www.amazon.com/African-American-Vernacular-English-Implications/dp/0631212450\\\\\\\"\\\\n    category: background\\\\n    role: \\\\\\\"Authoritative reference on AAVE phonological, grammatical, and pragmatic features; grounds our behavioral rate targets\\\\\\\"\\\\n    relevance: medium\\\\n    key_findings:\\\\n      - \\\\\\\"Systematic documentation of AAVE phonological and grammatical features\\\\\\\"\\\\n      - \\\\\\\"AAVE has distinct pragmatic conventions including directness patterns\\\\\\\"\\\\n      - \\\\\\\"AAVE is a fully systematic linguistic variety, not deficient English\\\\\\\"\\\\n    how_we_differ: \\\\\\\"Provides sociolinguistic grounding for what behavioral patterns we should calibrate toward\\\\\\\"\\\\n\\\\n  - id: kachru2008cultures\\\\n    title: \\\\\\\"Cultures, Contexts, and World Englishes\\\\\\\"\\\\n    authors: \\\\\\\"Kachru, Yamuna; Smith, Cecil\\\\\\\"\\\\n    venue: \\\\\\\"Routledge\\\\\\\"\\\\n    year: 2008\\\\n    url: \\\\\\\"https://www.routledge.com/Cultures-Contexts-and-World-Englishes/Kachru-Smith/p/book/9780805847338\\\\\\\"\\\\n    category: background\\\\n    role: \\\\\\\"Framework for Indian English pragmatics; documents politeness strategies and speech act differences in Outer Circle Englishes\\\\\\\"\\\\n    relevance: medium\\\\n    key_findings:\\\\n      - \\\\\\\"Indian English has distinct politeness strategies rooted in face-saving norms\\\\\\\"\\\\n      - \\\\\\\"Requesting and disagreeing strategies differ from Inner Circle varieties\\\\\\\"\\\\n      - \\\\\\\"Three Circles model (Inner/Outer/Expanding) for understanding English variation\\\\\\\"\\\\n    how_we_differ: \\\\\\\"Provides sociolinguistic grounding for Indian English behavioral patterns we attempt to calibrate\\\\\\\"\\\\n\\\\n  - id: sekulic2024daus\\\\n    title: \\\\\\\"Reliable LLM-based User Simulator for Task-Oriented Dialogue Systems\\\\\\\"\\\\n    authors: \\\\\\\"Sekulic, Terragni, Guimaraes et al.\\\\\\\"\\\\n    venue: \\\\\\\"SCI-CHAT Workshop 2024\\\\\\\"\\\\n    year: 2024\\\\n    url: \\\\\\\"https://arxiv.org/abs/2402.13374\\\\\\\"\\\\n    category: background\\\\n    role: \\\\\\\"DAUS: domain-aware user simulator fine-tuned on real dialogues; shows fine-tuning improves goal fulfillment and reduces hallucination\\\\\\\"\\\\n    relevance: medium\\\\n    key_findings:\\\\n      - \\\\\\\"Fine-tuning LLMs on real dialogue examples improves user goal fulfillment\\\\\\\"\\\\n      - \\\\\\\"Mitigates hallucinations in simulator responses\\\\\\\"\\\\n      - \\\\\\\"Domain-aware approach outperforms generic prompting\\\\\\\"\\\\n    how_we_differ: \\\\\\\"DAUS optimizes task completion; we document failure modes when optimizing demographic behavioral fidelity\\\\\\\"\\\\n\\\\n  - id: ahmad2025diversity\\\\n    title: \\\\\\\"Simulating User Diversity in Task-Oriented Dialogue Systems using Large Language Models\\\\\\\"\\\\n    authors: \\\\\\\"Ahmad, Hillmann, Moller\\\\\\\"\\\\n    venue: \\\\\\\"arXiv 2502.12813\\\\\\\"\\\\n    year: 2025\\\\n    url: \\\\\\\"https://arxiv.org/abs/2502.12813\\\\\\\"\\\\n    category: background\\\\n    role: \\\\\\\"Generates diverse user profiles with varied demographics and conversational styles for dialogue evaluation\\\\\\\"\\\\n    relevance: medium\\\\n    key_findings:\\\\n      - \\\\\\\"GPT-o1 generates more heterogeneous user distributions than GPT-4o\\\\\\\"\\\\n      - \\\\\\\"82.46% task success across 57 dialogue sessions with diverse users\\\\\\\"\\\\n      - \\\\\\\"Captures variation in language styles, knowledge levels, and objectives\\\\\\\"\\\\n    how_we_differ: \\\\\\\"They generate diverse profiles; we document why calibrating specific behavioral rates to match real dialect group distributions fails\\\\\\\"\\\\n\\\\n  # ============================================================\\\\n  # NEW ADDITIONS (scan 2026-05-13)\\\\n  # ============================================================\\\\n\\\\n  # --- FOUNDATION (new) ---\\\\n  - id: sim2real2026gap\\\\n    title: \\\\\\\"Mind the Sim2Real Gap in User Simulation for Agentic Tasks\\\\\\\"\\\\n    authors: \\\\\\\"Zhou, Sun, Xu, Chen, Radev\\\\\\\"\\\\n    venue: \\\\\\\"arXiv 2603.11245\\\\\\\"\\\\n    year: 2026\\\\n    url: \\\\\\\"https://arxiv.org/abs/2603.11245\\\\\\\"\\\\n    category: foundation\\\\n    role: \\\\\\\"First study running full τ-bench protocol with 451 real humans; introduces USI metric to quantify sim-vs-human behavioral divergence\\\\\\\"\\\\n    relevance: high\\\\n    key_findings:\\\\n      - \\\\\\\"LLM simulators are excessively cooperative, stylistically uniform, and lack realistic frustration/ambiguity\\\\\\\"\\\\n      - \\\\\\\"Simulated users create 'easy mode' that inflates agent success rates above human baseline\\\\\\\"\\\\n      - \\\\\\\"Simulated feedback is uniformly positive; humans express calibrated dissatisfaction\\\\\\\"\\\\n      - \\\\\\\"Higher model capability does not yield more faithful user simulation\\\\\\\"\\\\n    how_we_differ: \\\\\\\"They quantify the sim2real gap but do not propose calibration methods; we attempt BCP and DPO calibration and document why both fail\\\\\\\"\\\\n    scan_date: \\\\\\\"2026-05-13\\\\\\\"\\\\n    note: \\\\\\\"Near-competitor in problem framing — directly validates our motivation. Not a direct competitor because they diagnose without prescribing a fix.\\\\\\\"\\\\n\\\\n  # --- METHOD-COMPONENT (new) ---\\\\n  - id: khan2026decoding\\\\n    title: \\\\\\\"Decoding-Time Debiasing via Process Reward Models: From Controlled Fill-in to Open-Ended Generation\\\\\\\"\\\\n    authors: \\\\\\\"Khan, Muneeb Ur Raheem\\\\\\\"\\\\n    venue: \\\\\\\"arXiv 2605.02348\\\\\\\"\\\\n    year: 2026\\\\n    url: \\\\\\\"https://arxiv.org/abs/2605.02348\\\\\\\"\\\\n    category: method-component\\\\n    role: \\\\\\\"Decoding-time bias mitigation using Process Reward Model as fairness judge; alternative to our training-time DPO approach\\\\\\\"\\\\n    relevance: medium\\\\n    key_findings:\\\\n      - \\\\\\\"Sequential debiasing raises bias scores by up to +0.40 over baseline while preserving fluency\\\\\\\"\\\\n      - \\\\\\\"No weight changes needed — debiasing happens at inference via PRM scoring\\\\\\\"\\\\n      - \\\\\\\"Gate calibration is model-dependent; no one-size-fits-all prompt works\\\\\\\"\\\\n    how_we_differ: \\\\\\\"They debias at decoding time for general fairness; we document failure modes of training-time calibration (BCP+DPO), motivating alternative approaches like decoding-time methods\\\\\\\"\\\\n    scan_date: \\\\\\\"2026-05-13\\\\\\\"\\\\n\\\\n  # --- EVALUATION (new) ---\\\\n  - id: gupta2025endive\\\\n    title: \\\\\\\"EnDive: A Cross-Dialect Benchmark for Fairness and Performance in Large Language Models\\\\\\\"\\\\n    authors: \\\\\\\"Gupta, Cheung et al.\\\\\\\"\\\\n    venue: \\\\\\\"Findings of EMNLP 2025 (arXiv 2504.07100)\\\\\\\"\\\\n    year: 2025\\\\n    url: \\\\\\\"https://arxiv.org/abs/2504.07100\\\\\\\"\\\\n    category: evaluation\\\\n    role: \\\\\\\"Cross-dialect benchmark covering 5 dialects including AAVE and Indian English — both our target dialects\\\\\\\"\\\\n    relevance: high\\\\n    key_findings:\\\\n      - \\\\\\\"Covers AAVE (33M speakers), Indian English (250M speakers), Jamaican, Chicano, Singaporean English\\\\\\\"\\\\n      - \\\\\\\"Few-shot LLM translation of SE to dialects, validated by native speakers (avg 6.02/7 faithfulness)\\\\\\\"\\\\n      - \\\\\\\"LLMs show performance drops on non-standard dialects across understanding, reasoning, math, logic\\\\\\\"\\\\n    how_we_differ: \\\\\\\"EnDive evaluates NLP task performance across dialects; we document calibration failure modes for user simulators targeting those same dialect groups\\\\\\\"\\\\n    scan_date: \\\\\\\"2026-05-13\\\\\\\"\\\\n\\\\n  # --- METHOD-COMPONENT (new, Plan B relevant) ---\\\\n  - id: lee2024dpo_toxicity\\\\n    title: \\\\\\\"A Mechanistic Understanding of Alignment Algorithms: A Case Study on DPO and Toxicity\\\\\\\"\\\\n    authors: \\\\\\\"Lee, Panda, Yun, Bansal\\\\\\\"\\\\n    venue: \\\\\\\"ICML 2024\\\\\\\"\\\\n    year: 2024\\\\n    url: \\\\\\\"https://arxiv.org/abs/2401.01967\\\\\\\"\\\\n    category: method-component\\\\n    role: \\\\\\\"Shows DPO bypasses rather than removes pre-training capabilities; explains mechanistically why DPO+BCP can reverse calibration direction\\\\\\\"\\\\n    relevance: high\\\\n    key_findings:\\\\n      - \\\\\\\"DPO does not remove toxic capabilities, only bypasses them at inference\\\\\\\"\\\\n      - \\\\\\\"Simple un-alignment can revert model to pre-DPO behavior\\\\\\\"\\\\n      - \\\\\\\"Minimal parameter changes allow reversion — alignment is fragile\\\\\\\"\\\\n    how_we_differ: \\\\\\\"They study DPO toxicity mechanics; we document DPO+BCP calibration reversal as a specific failure mode\\\\\\\"\\\\n    scan_date: \\\\\\\"2026-05-13\\\\\\\"\\\\n    plan_b_relevance: \\\\\\\"FM4 — explains why DPO training can reverse BCP calibration effect\\\\\\\"\\\\n\\\\n  - id: gupta2026intra_fairness\\\\n    title: \\\\\\\"Intra-Fairness Dynamics: The Bias Spillover Effect in Targeted LLM Alignment\\\\\\\"\\\\n    authors: \\\\\\\"Paraschou, Heiter, Iosifidis\\\\\\\"\\\\n    venue: \\\\\\\"arXiv 2602.16438\\\\\\\"\\\\n    year: 2026\\\\n    url: \\\\\\\"https://arxiv.org/abs/2602.16438\\\\\\\"\\\\n    category: method-component\\\\n    role: \\\\\\\"Documents bias spillover — targeted debiasing on one dimension causes unintended effects on other dimensions; directly parallels our cross-dimension interference\\\\\\\"\\\\n    relevance: high\\\\n    key_findings:\\\\n      - \\\\\\\"Targeted debiasing can produce unintended negative consequences across other social axes\\\\\\\"\\\\n      - \\\\\\\"Bias spillover effect: altering behavior on one dimension when mitigating another\\\\\\\"\\\\n      - \\\\\\\"Multi-attribute fairness dynamics must be considered in alignment\\\\\\\"\\\\n    how_we_differ: \\\\\\\"They study bias spillover in general alignment; we document the specific cross-dimension interference pattern in BCP-based behavioral calibration\\\\\\\"\\\\n    scan_date: \\\\\\\"2026-05-13\\\\\\\"\\\\n    plan_b_relevance: \\\\\\\"FM2 + FM4 — directly supports cross-dimension interference and DPO spillover claims\\\\\\\"\\\\n\\\\n  - id: basil2025playing_pretend\\\\n    title: \\\\\\\"Prompting Science Report 4: Playing Pretend: Expert Personas Don't Improve Factual Accuracy\\\\\\\"\\\\n    authors: \\\\\\\"Basil, Shapiro, Shapiro, Mollick, Mollick, Meincke\\\\\\\"\\\\n    venue: \\\\\\\"arXiv 2512.05858 (Wharton)\\\\\\\"\\\\n    year: 2025\\\\n    url: \\\\\\\"https://arxiv.org/abs/2512.05858\\\\\\\"\\\\n    category: method-component\\\\n    role: \\\\\\\"Shows persona prompting degrades factual accuracy; BCP is a form of persona/role prompting, explaining completion collapse\\\\\\\"\\\\n    relevance: high\\\\n    key_findings:\\\\n      - \\\\\\\"Expert personas do not improve factual accuracy across benchmarks\\\\\\\"\\\\n      - \\\\\\\"Persona prompting activates instruction-following mode at expense of factual recall\\\\\\\"\\\\n      - \\\\\\\"MMLU accuracy drops from 71.6% baseline to 66.3% with detailed persona\\\\\\\"\\\\n    how_we_differ: \\\\\\\"They study persona prompting in classification/QA; we document the same mechanism in multi-turn dialogue task completion\\\\\\\"\\\\n    scan_date: \\\\\\\"2026-05-13\\\\\\\"\\\\n    plan_b_relevance: \\\\\\\"FM1 — explains mechanism behind global behavior suppression\\\\\\\"\\\\n\\\\n  - id: hu2026expert_persona\\\\n    title: \\\\\\\"Expert Personas Improve LLM Alignment but Damage Accuracy: Bootstrapping Intent-Based Persona Routing with PRISM\\\\\\\"\\\\n    authors: \\\\\\\"Hu, Rostami, Thomason\\\\\\\"\\\\n    venue: \\\\\\\"arXiv 2603.18507\\\\\\\"\\\\n    year: 2026\\\\n    url: \\\\\\\"https://arxiv.org/abs/2603.18507\\\\\\\"\\\\n    category: method-component\\\\n    role: \\\\\\\"Systematically documents persona prompting trade-off: alignment improves but accuracy degrades up to 30pp; directly explains BCP completion collapse\\\\\\\"\\\\n    relevance: high\\\\n    key_findings:\\\\n      - \\\\\\\"Persona prompting improves alignment tasks but degrades knowledge/reasoning tasks\\\\\\\"\\\\n      - \\\\\\\"Performance drops up to 30pp under persona modifications\\\\\\\"\\\\n      - \\\\\\\"More instruction-tuned models are more susceptible to persona-induced accuracy loss\\\\\\\"\\\\n    how_we_differ: \\\\\\\"They study general persona-accuracy trade-off; we document the specific completion collapse in agent-user dialogue under behavioral calibration prompts\\\\\\\"\\\\n    scan_date: \\\\\\\"2026-05-13\\\\\\\"\\\\n    plan_b_relevance: \\\\\\\"FM1 — strongest external evidence for global behavior suppression mechanism\\\\\\\"\\\\n\\\\n  # --- BACKGROUND (new) ---\\\\n  - id: nakash2026divert\\\\n    title: \\\\\\\"Efficient Agent Evaluation via Diversity-Guided User Simulation\\\\\\\"\\\\n    authors: \\\\\\\"Nakash, Kour, Anaby-Tavor\\\\\\\"\\\\n    venue: \\\\\\\"arXiv 2604.21480\\\\\\\"\\\\n    year: 2026\\\\n    url: \\\\\\\"https://arxiv.org/abs/2604.21480\\\\\\\"\\\\n    category: background\\\\n    role: \\\\\\\"DIVERT framework for efficient agent evaluation via branching trajectories; addresses Monte Carlo inefficiency in agent evaluation\\\\\\\"\\\\n    relevance: medium\\\\n    key_findings:\\\\n      - \\\\\\\"Snapshot-based branching avoids redundant regeneration of early conversation prefixes\\\\\\\"\\\\n      - \\\\\\\"Coverage-guided exploration uncovers deep failure modes from rare user behaviors\\\\\\\"\\\\n    how_we_differ: \\\\\\\"They optimize evaluation efficiency; we document failure modes in user simulator fidelity calibration for dialect groups\\\\\\\"\\\\n    scan_date: \\\\\\\"2026-05-13\\\\\\\"\\\\n\\\\n# ============================================================\\\\n# SUMMARY\\\\n# ============================================================\\\\n# Total: 28 papers (updated 2026-05-13, +8 new, +4 Plan B scan)\\\\n# - direct-competitor: 0 (novelty still confirmed — no one has done systematic BCP failure analysis)\\\\n# - foundation: 5 (+sim2real2026gap)\\\\n# - method-component: 12 (+khan2026decoding, +lee2024dpo_toxicity, +gupta2026intra_fairness, +basil2025playing_pretend, +hu2026expert_persona)\\\\n# - evaluation: 6 (+gupta2025endive)\\\\n# - background: 6 (+nakash2026divert)\\\\n# - high relevance: 14, medium: 13, low: 1\\\\n#\\\\n# Plan B scan notes (2026-05-13):\\\\n# - 4 new papers added specifically for Plan B empirical analysis framing\\\\n# - lee2024dpo_toxicity: mechanistic explanation for FM4 (DPO+BCP reversal)\\\\n# - gupta2026intra_fairness: external evidence for FM2 (cross-dimension interference) + FM4 (spillover)\\\\n# - basil2025playing_pretend + hu2026expert_persona: external evidence for FM1 (completion collapse via persona prompting)\\\\n# - No direct competitor found for BCP failure mode analysis — novelty gap confirmed\\\\n# - Also noted but not added:\\\\n#   - ϕ-DPO (2602.22601): Fairness DPO for multimodal continual learning, different domain\\\\n#   - Linguistic Stereotypes (2603.18729): SAE vs AAE bias in multi-agent architectures\\\\n\\\", \\\"total_chars\\\": 26989, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml\", \"content\": \"papers:\\n  # ============================================================\\n  # DIRECT-COMPETITOR\\n  # ============================================================\\n  # 未找到直接竞品。没有现有工作专门做\\\"校准 LLM 用户模拟器的方言行为率偏差\\\"。\\n  # 最接近的是 Haq & Saldias 2026（归入 evaluation），但他们只量化偏差，不提出校准方法。\\n  # 这验证了 DemoCalib 的新颖性。\\n\\n  # ============================================================\\n  # FOUNDATION\\n  # ============================================================\\n  - id: seshadri2026lost\\n    title: \\\"Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations\\\"\\n    authors: \\\"Seshadri, Cahyawijaya, Odumakinde, Singh, Goldfarb-Tarrant\\\"\\n    venue: \\\"arXiv 2601.17087\\\"\\n    year: 2026\\n    url: \\\"https://arxiv.org/abs/2601.17087\\\"\\n    category: foundation\\n    role: \\\"Documents that LLM user simulators are differentially effective proxies across demographic groups; AAVE and Indian English speakers get worst calibration\\\"\\n    relevance: high\\n    key_findings:\\n      - \\\"Agent success rates vary up to 9pp across different user simulator LLMs\\\"\\n      - \\\"AAVE speakers experience consistently worse success rates and calibration errors than SAE speakers\\\"\\n      - \\\"Simulated users introduce conversational artifacts absent from real human users\\\"\\n      - \\\"Disparities compound significantly with age for AAVE speakers\\\"\\n    how_we_differ: \\\"They document the problem; we document why both BCP and DPO calibration fail to close the gaps, providing a failure taxonomy\\\"\\n\\n  - id: yao2024taubench\\n    title: \\\"tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains\\\"\\n    authors: \\\"Yao et al.\\\"\\n    venue: \\\"arXiv 2406.12045\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2406.12045\\\"\\n    category: foundation\\n    role: \\\"The agent evaluation framework we build on; provides retail customer service domain with user simulator + tool-calling agent + pass^k metric\\\"\\n    relevance: high\\n    key_findings:\\n      - \\\"Even gpt-4o succeeds on <50% of tasks; pass^8 <25% in retail\\\"\\n      - \\\"Proposes pass^k metric measuring reliability over multiple trials\\\"\\n      - \\\"User simulator is LLM-based, enabling behavioral modification\\\"\\n    how_we_differ: \\\"We extend tau-bench by documenting systematic failure modes when calibrating the user simulator's dialect-specific behavioral rates\\\"\\n\\n  - id: liu2024agentbench\\n    title: \\\"AgentBench: Evaluating LLMs as Agents\\\"\\n    authors: \\\"Liu et al.\\\"\\n    venue: \\\"ICLR 2024\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2308.03688\\\"\\n    category: foundation\\n    role: \\\"Multi-environment agent benchmark; establishes evaluation methodology for LLM agents across 8 environments\\\"\\n    relevance: medium\\n    key_findings:\\n      - \\\"Significant performance gap between commercial and open-source LLMs as agents\\\"\\n      - \\\"Poor long-term reasoning and instruction following are main obstacles\\\"\\n    how_we_differ: \\\"AgentBench evaluates agent capability; we focus on user simulator fidelity and fairness\\\"\\n\\n  - id: wang2024mint\\n    title: \\\"MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback\\\"\\n    authors: \\\"Wang, Wang, Liu, Chen, Yuan, Peng, Ji\\\"\\n    venue: \\\"ICLR 2024\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2309.10691\\\"\\n    category: foundation\\n    role: \\\"Multi-turn agent evaluation benchmark; shows gap between single-turn and multi-turn performance\\\"\\n    relevance: medium\\n    key_findings:\\n      - \\\"LLMs benefit 1-8% per turn from tools, 2-17% from language feedback\\\"\\n      - \\\"Better single-turn performance does not guarantee better multi-turn performance\\\"\\n      - \\\"SIFT and RLHF generally hurt multi-turn capabilities\\\"\\n    how_we_differ: \\\"MINT uses GPT-4 simulated users without demographic variation; we investigate dialect-aware calibration and document its failure modes\\\"\\n\\n  # ============================================================\\n  # METHOD-COMPONENT\\n  # ============================================================\\n  - id: rafailov2023dpo\\n    title: \\\"Direct Preference Optimization: Your Language Model is Secretly a Reward Model\\\"\\n    authors: \\\"Rafailov, Sharma, Mitchell, Manning, Ermon, Finn\\\"\\n    venue: \\\"NeurIPS 2023\\\"\\n    year: 2023\\n    url: \\\"https://arxiv.org/abs/2305.18290\\\"\\n    category: method-component\\n    role: \\\"Core algorithm for our DPO-based behavioral alignment; eliminates need for reward model training\\\"\\n    relevance: high\\n    key_findings:\\n      - \\\"DPO directly optimizes policy from preference pairs without explicit reward model\\\"\\n      - \\\"Computationally lightweight, stable alternative to PPO-based RLHF\\\"\\n      - \\\"Exceeds PPO-based RLHF in controlling sentiment of generations\\\"\\n    how_we_differ: \\\"We apply DPO to attempt dialect behavioral calibration and document its systematic failure modes including calibration reversal\\\"\\n\\n  - id: zhao2021calibrate\\n    title: \\\"Calibrate Before Use: Improving Few-Shot Performance of Language Models\\\"\\n    authors: \\\"Zhao, Wallace, Feng, Klein, Singh\\\"\\n    venue: \\\"ICML 2021\\\"\\n    year: 2021\\n    url: \\\"https://arxiv.org/abs/2102.09690\\\"\\n    category: method-component\\n    role: \\\"Foundational calibration method for LLMs; contextual calibration corrects output distribution biases\\\"\\n    relevance: medium\\n    key_findings:\\n      - \\\"Few-shot accuracy varies from near chance to near SOTA depending on prompt format\\\"\\n      - \\\"Identified majority label bias, recency bias, common token bias\\\"\\n      - \\\"Contextual calibration with content-free inputs improves accuracy up to 30%\\\"\\n    how_we_differ: \\\"They calibrate classification outputs; we attempt to calibrate behavioral rates (question rate, politeness) in generation and document why it fails\\\"\\n\\n  - id: abdulhai2025consistent\\n    title: \\\"Consistently Simulating Human Personas with Multi-Turn Reinforcement Learning\\\"\\n    authors: \\\"Abdulhai, Cheng, Clay, Althoff, Levine, Jaques\\\"\\n    venue: \\\"NeurIPS 2025\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2511.00222\\\"\\n    category: method-component\\n    role: \\\"Multi-turn RL for persona consistency; directly relevant to maintaining calibrated behavior across conversation turns\\\"\\n    relevance: high\\n    key_findings:\\n      - \\\"Off-the-shelf LLMs drift from assigned personas over multi-turn dialogue\\\"\\n      - \\\"Three automatic metrics: prompt-to-line, line-to-line, Q&A consistency\\\"\\n      - \\\"Multi-turn RL reduces inconsistency by >55%\\\"\\n    how_we_differ: \\\"They optimize persona consistency in general; we document failure modes when targeting dialect behavioral rate calibration\\\"\\n\\n  - id: naous2025flipping\\n    title: \\\"Flipping the Dialogue: Training and Evaluating User Language Models\\\"\\n    authors: \\\"Naous, Laban, Xu, Neville\\\"\\n    venue: \\\"arXiv 2510.06552\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2510.06552\\\"\\n    category: method-component\\n    role: \\\"Purpose-built User LMs outperform repurposed assistant LMs as user simulators; validates need for specialized user models\\\"\\n    relevance: high\\n    key_findings:\\n      - \\\"Better assistant LMs yield worse user simulators\\\"\\n      - \\\"UserLM-8b provides more realistic user simulation\\\"\\n      - \\\"GPT-4o performance drops from 74.6% to 57.4% under realistic user simulation\\\"\\n    how_we_differ: \\\"They train general User LMs; we document why calibrating user simulator behavioral rates for specific dialect groups fails\\\"\\n\\n  - id: li2025persona\\n    title: \\\"LLM Generated Persona is a Promise with a Catch\\\"\\n    authors: \\\"Li, Chen et al.\\\"\\n    venue: \\\"NeurIPS 2025\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2503.16527\\\"\\n    category: method-component\\n    role: \\\"Documents systematic biases in LLM-generated personas; explains why naive persona prompting fails for demographic simulation\\\"\\n    relevance: medium\\n    key_findings:\\n      - \\\"LLM-generated personas systematically drift toward socially desirable traits\\\"\\n      - \\\"More LLM-generated content produces more left-leaning, less representative personas\\\"\\n      - \\\"Bias exists in the persona creation step itself, not just model responses\\\"\\n    how_we_differ: \\\"We document failure modes when directly injecting behavioral rate targets via BCP, including persona-like completion collapse\\\"\\n\\n  - id: wang2024alignment\\n    title: \\\"A Comprehensive Survey of LLM Alignment Techniques: RLHF, RLAIF, PPO, DPO and More\\\"\\n    authors: \\\"Wang, Bi, Pentyala et al.\\\"\\n    venue: \\\"arXiv 2407.16216\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2407.16216\\\"\\n    category: method-component\\n    role: \\\"Survey unifying alignment methods under single policy gradient framework; reference for our DPO methodology\\\"\\n    relevance: medium\\n    key_findings:\\n      - \\\"Unified policy gradient framework for pretraining, SFT, RLHF, RLVR\\\"\\n      - \\\"DPO is stable and lightweight but sensitive to preference data quality\\\"\\n      - \\\"Detailed comparison of PPO vs GRPO vs DPO implementation details\\\"\\n    how_we_differ: \\\"Survey provides methodology reference; we apply DPO to user simulator dialect calibration and document its failure modes\\\"\\n\\n  # ============================================================\\n  # EVALUATION\\n  # ============================================================\\n  - id: lin2025redial\\n    title: \\\"Assessing Dialect Fairness and Robustness of Large Language Models in Reasoning Tasks\\\"\\n    authors: \\\"Lin et al.\\\"\\n    venue: \\\"ACL 2025\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2410.11005\\\"\\n    category: evaluation\\n    role: \\\"First human-annotated SE-AAVE parallel benchmark (ReDial); quantifies LLM performance gaps on AAVE\\\"\\n    relevance: high\\n    key_findings:\\n      - \\\"1.2K+ parallel SE-AAVE prompt pairs across reasoning tasks\\\"\\n      - \\\"Almost all models show statistically significant performance drops on AAVE\\\"\\n      - \\\"AAVE performance gaps arise from morphosyntactic features and conversational norms\\\"\\n      - \\\"LLMs struggle more with AAVE than misspelled Standard English\\\"\\n    how_we_differ: \\\"ReDial evaluates reasoning task performance; we evaluate behavioral rates in user simulation and document calibration failure modes\\\"\\n\\n  - id: faisal2024dialectbench\\n    title: \\\"DialectBench: A NLP Benchmark for Dialects, Varieties, and Closely-Related Languages\\\"\\n    authors: \\\"Faisal et al.\\\"\\n    venue: \\\"ACL 2024\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2403.11009\\\"\\n    category: evaluation\\n    role: \\\"Large-scale multi-dialect NLP benchmark; documents performance disparities across 281 language varieties\\\"\\n    relevance: medium\\n    key_findings:\\n      - \\\"10 NLP tasks, 281 varieties, 40 language clusters\\\"\\n      - \\\"Substantial performance disparities between standard and non-standard varieties\\\"\\n      - \\\"Performance gap widens with fine-tuning due to uneven data availability\\\"\\n    how_we_differ: \\\"DialectBench evaluates NLP task performance; we document failure modes in behavioral calibration of user simulators\\\"\\n\\n  - id: gallegos2024bias\\n    title: \\\"Bias and Fairness in Large Language Models: A Survey\\\"\\n    authors: \\\"Gallegos, Rossi, Barrow et al.\\\"\\n    venue: \\\"Computational Linguistics, Vol. 50(3)\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2309.00770\\\"\\n    category: evaluation\\n    role: \\\"Comprehensive survey of LLM bias evaluation and mitigation; provides taxonomy of metrics and datasets\\\"\\n    relevance: medium\\n    key_findings:\\n      - \\\"Taxonomy of bias metrics at embedding, probability, and generated text levels\\\"\\n      - \\\"Mitigation methods categorized by intervention stage: pre/in/intra/post-processing\\\"\\n      - \\\"Consolidated public datasets for bias evaluation\\\"\\n    how_we_differ: \\\"Survey covers general LLM bias; we address a specific bias modality (behavioral rates in user simulation)\\\"\\n\\n  - id: parrish2022bbq\\n    title: \\\"BBQ: A Hand-Built Bias Benchmark for Question Answering\\\"\\n    authors: \\\"Parrish et al.\\\"\\n    venue: \\\"Findings of ACL 2022\\\"\\n    year: 2022\\n    url: \\\"https://aclanthology.org/2022.findings-acl.165/\\\"\\n    category: evaluation\\n    role: \\\"Established bias benchmark for QA; evaluates social biases across multiple demographic categories\\\"\\n    relevance: low\\n    key_findings:\\n      - \\\"58,492 unique examples across multiple bias categories\\\"\\n      - \\\"Evaluates both individual and intersectional biases\\\"\\n      - \\\"Standard benchmark for LLM bias evaluation\\\"\\n    how_we_differ: \\\"BBQ measures representational bias in QA; we measure behavioral bias in interactive dialogue simulation\\\"\\n\\n  - id: haq2026dialect\\n    title: \\\"Dialect vs Demographics: Quantifying LLM Bias from Implicit Linguistic Signals vs. Explicit User Profiles\\\"\\n    authors: \\\"Haq, Saldias\\\"\\n    venue: \\\"arXiv 2604.21152\\\"\\n    year: 2026\\n    url: \\\"https://arxiv.org/abs/2604.21152\\\"\\n    category: evaluation\\n    role: \\\"Closest to direct competitor; quantifies how dialect cues vs explicit identity trigger differential LLM behavior\\\"\\n    relevance: high\\n    key_findings:\\n      - \\\"Dialect cues trigger 'dialect jailbreak' reducing refusal probability to near zero\\\"\\n      - \\\"AAVE/Singlish users receive less sanitized content than SAE users\\\"\\n      - \\\"Safety alignment is brittle, over-indexed on explicit keywords\\\"\\n      - \\\"24,000+ responses analyzed across two LLMs\\\"\\n    how_we_differ: \\\"They characterize the bias mechanism (implicit vs explicit); we document why calibration methods fail to correct behavioral rates\\\"\\n\\n  # ============================================================\\n  # BACKGROUND\\n  # ============================================================\\n  - id: joshi2025dialect_survey\\n    title: \\\"Natural Language Processing for Dialects of a Language: A Survey\\\"\\n    authors: \\\"Joshi, Dabre, Kanojia, Li, Zhan, Haffari, Dippold\\\"\\n    venue: \\\"ACM Computing Surveys, Vol. 57(6)\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2401.05632\\\"\\n    category: background\\n    role: \\\"Comprehensive survey of NLP for dialects; covers datasets, approaches, and performance gaps across dialect varieties\\\"\\n    relevance: medium\\n    key_findings:\\n      - \\\"NLP models show systematic performance degradation on dialectal data\\\"\\n      - \\\"Covers NLU and NLG tasks including dialogue systems\\\"\\n      - \\\"Equity implications of language technology performance gaps\\\"\\n    how_we_differ: \\\"Survey provides broad context; we tackle a specific gap in user simulation fairness\\\"\\n\\n  - id: rickford1999aave\\n    title: \\\"African American Vernacular English: Features, Evolution, Educational Implications\\\"\\n    authors: \\\"Rickford, John Russell\\\"\\n    venue: \\\"Blackwell Publishers (Language in Society series)\\\"\\n    year: 1999\\n    url: \\\"https://www.amazon.com/African-American-Vernacular-English-Implications/dp/0631212450\\\"\\n    category: background\\n    role: \\\"Authoritative reference on AAVE phonological, grammatical, and pragmatic features; grounds our behavioral rate targets\\\"\\n    relevance: medium\\n    key_findings:\\n      - \\\"Systematic documentation of AAVE phonological and grammatical features\\\"\\n      - \\\"AAVE has distinct pragmatic conventions including directness patterns\\\"\\n      - \\\"AAVE is a fully systematic linguistic variety, not deficient English\\\"\\n    how_we_differ: \\\"Provides sociolinguistic grounding for what behavioral patterns we should calibrate toward\\\"\\n\\n  - id: kachru2008cultures\\n    title: \\\"Cultures, Contexts, and World Englishes\\\"\\n    authors: \\\"Kachru, Yamuna; Smith, Cecil\\\"\\n    venue: \\\"Routledge\\\"\\n    year: 2008\\n    url: \\\"https://www.routledge.com/Cultures-Contexts-and-World-Englishes/Kachru-Smith/p/book/9780805847338\\\"\\n    category: background\\n    role: \\\"Framework for Indian English pragmatics; documents politeness strategies and speech act differences in Outer Circle Englishes\\\"\\n    relevance: medium\\n    key_findings:\\n      - \\\"Indian English has distinct politeness strategies rooted in face-saving norms\\\"\\n      - \\\"Requesting and disagreeing strategies differ from Inner Circle varieties\\\"\\n      - \\\"Three Circles model (Inner/Outer/Expanding) for understanding English variation\\\"\\n    how_we_differ: \\\"Provides sociolinguistic grounding for Indian English behavioral patterns we attempt to calibrate\\\"\\n\\n  - id: sekulic2024daus\\n    title: \\\"Reliable LLM-based User Simulator for Task-Oriented Dialogue Systems\\\"\\n    authors: \\\"Sekulic, Terragni, Guimaraes et al.\\\"\\n    venue: \\\"SCI-CHAT Workshop 2024\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2402.13374\\\"\\n    category: background\\n    role: \\\"DAUS: domain-aware user simulator fine-tuned on real dialogues; shows fine-tuning improves goal fulfillment and reduces hallucination\\\"\\n    relevance: medium\\n    key_findings:\\n      - \\\"Fine-tuning LLMs on real dialogue examples improves user goal fulfillment\\\"\\n      - \\\"Mitigates hallucinations in simulator responses\\\"\\n      - \\\"Domain-aware approach outperforms generic prompting\\\"\\n    how_we_differ: \\\"DAUS optimizes task completion; we document failure modes when optimizing demographic behavioral fidelity\\\"\\n\\n  - id: ahmad2025diversity\\n    title: \\\"Simulating User Diversity in Task-Oriented Dialogue Systems using Large Language Models\\\"\\n    authors: \\\"Ahmad, Hillmann, Moller\\\"\\n    venue: \\\"arXiv 2502.12813\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2502.12813\\\"\\n    category: background\\n    role: \\\"Generates diverse user profiles with varied demographics and conversational styles for dialogue evaluation\\\"\\n    relevance: medium\\n    key_findings:\\n      - \\\"GPT-o1 generates more heterogeneous user distributions than GPT-4o\\\"\\n      - \\\"82.46% task success across 57 dialogue sessions with diverse users\\\"\\n      - \\\"Captures variation in language styles, knowledge levels, and objectives\\\"\\n    how_we_differ: \\\"They generate diverse profiles; we document why calibrating specific behavioral rates to match real dialect group distributions fails\\\"\\n\\n  # ============================================================\\n  # NEW ADDITIONS (scan 2026-05-13)\\n  # ============================================================\\n\\n  # --- FOUNDATION (new) ---\\n  - id: sim2real2026gap\\n    title: \\\"Mind the Sim2Real Gap in User Simulation for Agentic Tasks\\\"\\n    authors: \\\"Zhou, Sun, Xu, Chen, Radev\\\"\\n    venue: \\\"arXiv 2603.11245\\\"\\n    year: 2026\\n    url: \\\"https://arxiv.org/abs/2603.11245\\\"\\n    category: foundation\\n    role: \\\"First study running full τ-bench protocol with 451 real humans; introduces USI metric to quantify sim-vs-human behavioral divergence\\\"\\n    relevance: high\\n    key_findings:\\n      - \\\"LLM simulators are excessively cooperative, stylistically uniform, and lack realistic frustration/ambiguity\\\"\\n      - \\\"Simulated users create 'easy mode' that inflates agent success rates above human baseline\\\"\\n      - \\\"Simulated feedback is uniformly positive; humans express calibrated dissatisfaction\\\"\\n      - \\\"Higher model capability does not yield more faithful user simulation\\\"\\n    how_we_differ: \\\"They quantify the sim2real gap but do not propose calibration methods; we attempt BCP and DPO calibration and document why both fail\\\"\\n    scan_date: \\\"2026-05-13\\\"\\n    note: \\\"Near-competitor in problem framing — directly validates our motivation. Not a direct competitor because they diagnose without prescribing a fix.\\\"\\n\\n  # --- METHOD-COMPONENT (new) ---\\n  - id: khan2026decoding\\n    title: \\\"Decoding-Time Debiasing via Process Reward Models: From Controlled Fill-in to Open-Ended Generation\\\"\\n    authors: \\\"Khan, Muneeb Ur Raheem\\\"\\n    venue: \\\"arXiv 2605.02348\\\"\\n    year: 2026\\n    url: \\\"https://arxiv.org/abs/2605.02348\\\"\\n    category: method-component\\n    role: \\\"Decoding-time bias mitigation using Process Reward Model as fairness judge; alternative to our training-time DPO approach\\\"\\n    relevance: medium\\n    key_findings:\\n      - \\\"Sequential debiasing raises bias scores by up to +0.40 over baseline while preserving fluency\\\"\\n      - \\\"No weight changes needed — debiasing happens at inference via PRM scoring\\\"\\n      - \\\"Gate calibration is model-dependent; no one-size-fits-all prompt works\\\"\\n    how_we_differ: \\\"They debias at decoding time for general fairness; we document failure modes of training-time calibration (BCP+DPO), motivating alternative approaches like decoding-time methods\\\"\\n    scan_date: \\\"2026-05-13\\\"\\n\\n  # --- EVALUATION (new) ---\\n  - id: gupta2025endive\\n    title: \\\"EnDive: A Cross-Dialect Benchmark for Fairness and Performance in Large Language Models\\\"\\n    authors: \\\"Gupta, Cheung et al.\\\"\\n    venue: \\\"Findings of EMNLP 2025 (arXiv 2504.07100)\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2504.07100\\\"\\n    category: evaluation\\n    role: \\\"Cross-dialect benchmark covering 5 dialects including AAVE and Indian English — both our target dialects\\\"\\n    relevance: high\\n    key_findings:\\n      - \\\"Covers AAVE (33M speakers), Indian English (250M speakers), Jamaican, Chicano, Singaporean English\\\"\\n      - \\\"Few-shot LLM translation of SE to dialects, validated by native speakers (avg 6.02/7 faithfulness)\\\"\\n      - \\\"LLMs show performance drops on non-standard dialects across understanding, reasoning, math, logic\\\"\\n    how_we_differ: \\\"EnDive evaluates NLP task performance across dialects; we document calibration failure modes for user simulators targeting those same dialect groups\\\"\\n    scan_date: \\\"2026-05-13\\\"\\n\\n  # --- METHOD-COMPONENT (new, Plan B relevant) ---\\n  - id: lee2024dpo_toxicity\\n    title: \\\"A Mechanistic Understanding of Alignment Algorithms: A Case Study on DPO and Toxicity\\\"\\n    authors: \\\"Lee, Panda, Yun, Bansal\\\"\\n    venue: \\\"ICML 2024\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2401.01967\\\"\\n    category: method-component\\n    role: \\\"Shows DPO bypasses rather than removes pre-training capabilities; explains mechanistically why DPO+BCP can reverse calibration direction\\\"\\n    relevance: high\\n    key_findings:\\n      - \\\"DPO does not remove toxic capabilities, only bypasses them at inference\\\"\\n      - \\\"Simple un-alignment can revert model to pre-DPO behavior\\\"\\n      - \\\"Minimal parameter changes allow reversion — alignment is fragile\\\"\\n    how_we_differ: \\\"They study DPO toxicity mechanics; we document DPO+BCP calibration reversal as a specific failure mode\\\"\\n    scan_date: \\\"2026-05-13\\\"\\n    plan_b_relevance: \\\"FM4 — explains why DPO training can reverse BCP calibration effect\\\"\\n\\n  - id: gupta2026intra_fairness\\n    title: \\\"Intra-Fairness Dynamics: The Bias Spillover Effect in Targeted LLM Alignment\\\"\\n    authors: \\\"Paraschou, Heiter, Iosifidis\\\"\\n    venue: \\\"arXiv 2602.16438\\\"\\n    year: 2026\\n    url: \\\"https://arxiv.org/abs/2602.16438\\\"\\n    category: method-component\\n    role: \\\"Documents bias spillover — targeted debiasing on one dimension causes unintended effects on other dimensions; directly parallels our cross-dimension interference\\\"\\n    relevance: high\\n    key_findings:\\n      - \\\"Targeted debiasing can produce unintended negative consequences across other social axes\\\"\\n      - \\\"Bias spillover effect: altering behavior on one dimension when mitigating another\\\"\\n      - \\\"Multi-attribute fairness dynamics must be considered in alignment\\\"\\n    how_we_differ: \\\"They study bias spillover in general alignment; we document the specific cross-dimension interference pattern in BCP-based behavioral calibration\\\"\\n    scan_date: \\\"2026-05-13\\\"\\n    plan_b_relevance: \\\"FM2 + FM4 — directly supports cross-dimension interference and DPO spillover claims\\\"\\n\\n  - id: basil2025playing_pretend\\n    title: \\\"Prompting Science Report 4: Playing Pretend: Expert Personas Don't Improve Factual Accuracy\\\"\\n    authors: \\\"Basil, Shapiro, Shapiro, Mollick, Mollick, Meincke\\\"\\n    venue: \\\"arXiv 2512.05858 (Wharton)\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2512.05858\\\"\\n    category: method-component\\n    role: \\\"Shows persona prompting degrades factual accuracy; BCP is a form of persona/role prompting, explaining completion collapse\\\"\\n    relevance: high\\n    key_findings:\\n      - \\\"Expert personas do not improve factual accuracy across benchmarks\\\"\\n      - \\\"Persona prompting activates instruction-following mode at expense of factual recall\\\"\\n      - \\\"MMLU accuracy drops from 71.6% baseline to 66.3% with detailed persona\\\"\\n    how_we_differ: \\\"They study persona prompting in classification/QA; we document the same mechanism in multi-turn dialogue task completion\\\"\\n    scan_date: \\\"2026-05-13\\\"\\n    plan_b_relevance: \\\"FM1 — explains mechanism behind global behavior suppression\\\"\\n\\n  - id: hu2026expert_persona\\n    title: \\\"Expert Personas Improve LLM Alignment but Damage Accuracy: Bootstrapping Intent-Based Persona Routing with PRISM\\\"\\n    authors: \\\"Hu, Rostami, Thomason\\\"\\n    venue: \\\"arXiv 2603.18507\\\"\\n    year: 2026\\n    url: \\\"https://arxiv.org/abs/2603.18507\\\"\\n    category: method-component\\n    role: \\\"Systematically documents persona prompting trade-off: alignment improves but accuracy degrades up to 30pp; directly explains BCP completion collapse\\\"\\n    relevance: high\\n    key_findings:\\n      - \\\"Persona prompting improves alignment tasks but degrades knowledge/reasoning tasks\\\"\\n      - \\\"Performance drops up to 30pp under persona modifications\\\"\\n      - \\\"More instruction-tuned models are more susceptible to persona-induced accuracy loss\\\"\\n    how_we_differ: \\\"They study general persona-accuracy trade-off; we document the specific completion collapse in agent-user dialogue under behavioral calibration prompts\\\"\\n    scan_date: \\\"2026-05-13\\\"\\n    plan_b_relevance: \\\"FM1 — strongest external evidence for global behavior suppression mechanism\\\"\\n\\n  # --- BACKGROUND (new) ---\\n  - id: nakash2026divert\\n    title: \\\"Efficient Agent Evaluation via Diversity-Guided User Simulation\\\"\\n    authors: \\\"Nakash, Kour, Anaby-Tavor\\\"\\n    venue: \\\"arXiv 2604.21480\\\"\\n    year: 2026\\n    url: \\\"https://arxiv.org/abs/2604.21480\\\"\\n    category: background\\n    role: \\\"DIVERT framework for efficient agent evaluation via branching trajectories; addresses Monte Carlo inefficiency in agent evaluation\\\"\\n    relevance: medium\\n    key_findings:\\n      - \\\"Snapshot-based branching avoids redundant regeneration of early conversation prefixes\\\"\\n      - \\\"Coverage-guided exploration uncovers deep failure modes from rare user behaviors\\\"\\n    how_we_differ: \\\"They optimize evaluation efficiency; we document failure modes in user simulator fidelity calibration for dialect groups\\\"\\n    scan_date: \\\"2026-05-13\\\"\\n\\n# ============================================================\\n# SUMMARY\\n# ============================================================\\n# Total: 28 papers (updated 2026-05-13, +8 new, +4 Plan B scan)\\n# - direct-competitor: 0 (novelty still confirmed — no one has done systematic BCP failure analysis)\\n# - foundation: 5 (+sim2real2026gap)\\n# - method-component: 12 (+khan2026decoding, +lee2024dpo_toxicity, +gupta2026intra_fairness, +basil2025playing_pretend, +hu2026expert_persona)\\n# - evaluation: 6 (+gupta2025endive)\\n# - background: 6 (+nakash2026divert)\\n# - high relevance: 14, medium: 13, low: 1\\n#\\n# Plan B scan notes (2026-05-13):\\n# - 4 new papers added specifically for Plan B empirical analysis framing\\n# - lee2024dpo_toxicity: mechanistic explanation for FM4 (DPO+BCP reversal)\\n# - gupta2026intra_fairness: external evidence for FM2 (cross-dimension interference) + FM4 (spillover)\\n# - basil2025playing_pretend + hu2026expert_persona: external evidence for FM1 (completion collapse via persona prompting)\\n# - No direct competitor found for BCP failure mode analysis — novelty gap confirmed\\n# - Also noted but not added:\\n#   - ϕ-DPO (2602.22601): Fairness DPO for multimodal continual learning, different domain\\n#   - Linguistic Stereotypes (2603.18729): SAE vs AAE bias in multi-agent architectures\\n\", \"total_chars\": 26989, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01NmfnA8SGJE7pHUq9UYzBjC`</summary>

```json
{
  "project": "cost-verify-agent-rl",
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
  "session_id": "2abdebbe-f3bd-4182-bff6-4d04fba6ecf2",
  "uuid": "d36eae8f-86ba-4537-8de3-2b0337b7761c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QZYaGvNpujb38AXZdEfTqP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 445,
      "cache_read_input_tokens": 23561,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 445
      },
      "output_tokens": 34,
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

_source line 11 · 2026-05-13T08:20:05.478Z_

<details><summary>↩ Tool result · `toolu_01NmfnA8SGJE7pHUq9UYzBjC`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/paper_framing.md\", \"content\": \"# Paper Framing: Calibration Failure Taxonomy for LLM User Simulators\\n\\n> Plan B story — Director approved 2026-05-13\\n> Target: EMNLP 2026 Findings (ARR deadline 2026-05-25)\\n\\n---\\n\\n## Title Candidates\\n\\n1. **\\\"Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation\\\"**\\n   - Pro: 直接点明贡献（taxonomy），关键词覆盖好\\n   - Con: 稍长\\n\\n2. **\\\"The Calibration Trap: Prompt-Based and Training-Based Corrections Both Fail for Dialect Bias in LLM User Simulators\\\"**\\n   - Pro: \\\"trap\\\" 吸引眼球，涵盖两种方法\\n   - Con: 可能暗示过于 negative\\n\\n3. **\\\"Behavioral Calibration Considered Harmful? Systematic Failure Modes in Dialect-Aware User Simulation\\\"**\\n   - Pro: Dijkstra 风格标题引发好奇，问号留余地\\n   - Con: \\\"Considered Harmful\\\" 可能被认为 cliché\\n\\n**推荐**: Title 1 — 最准确传达贡献，reviewer-friendly。\\n\\n---\\n\\n## Core Story\\n\\n**Problem**: LLM user simulators exhibit dialect-dependent behavioral biases — AAVE and Indian English speakers receive systematically different politeness and question-asking patterns compared to Standard American English (sim2real2026gap; seshadri2026lost). These biases propagate into agent evaluation, undermining fairness.\\n\\n**Attempted Solution**: We apply two complementary calibration strategies:\\n- **BCP (Behavioral Calibration Prompting)**: Prompt-level injection of target behavioral rates\\n- **DPO (Direct Preference Optimization)**: Training-level alignment using dialect-calibrated preference pairs\\n\\n**Finding**: Both strategies fail systematically. We document **the first taxonomy of calibration failure modes** for LLM user simulators, identifying four distinct mechanisms that explain why seemingly reasonable calibration interventions produce counterproductive outcomes.\\n\\n**Framing**: This is NOT \\\"we tried and failed.\\\" This is a systematic empirical analysis that (1) identifies previously undocumented failure mechanisms, (2) connects them to known phenomena in persona prompting and alignment, and (3) provides actionable constraints for future calibration research.\\n\\n---\\n\\n## Core Claims\\n\\n### C1: BCP produces three systematic failure mechanisms\\n**Evidence strength**: Moderate (single model, single run, n=19-20 per variant)\\n\\n| Failure Mode | Description | Key Metric | exp_id |\\n|---|---|---|---|\\n| FM1: Global Behavior Suppression | BCP calibration prompts collapse task completion regardless of target dimension | completion retention 52.3% (threshold ≥80%) | mvp-004 |\\n| FM2: Cross-Dimension Interference | Targeting one behavioral dimension perturbs non-targeted dimensions | politeness -25.6% when targeting question_rate; question_rate -52.3% when targeting politeness | mvp-004 |\\n| FM3: Overcorrection Rebound | Requesting extreme behavioral shift causes model to rebound in opposite direction | overcorrected politeness +4.2pp ~ +10.4pp above baseline (4 runs, 4/4 consistent) | hgate-dpo003-merged |\\n\\n**Supporting numbers (mvp-004, Qwen2.5-7B-Instruct, n=19-20)**:\\n- FM1: aave completion 0.100 vs baseline 0.368 (-72.8%); indian 0.150 (-59.2%); mean calibrated 0.193\\n- FM2: single_dim_question politeness drops 25.6% (non-target); single_dim_politeness question_rate drops 52.3% (non-target)\\n  - **Base rate caveat**: question_rate baseline = 0.044 (~0.8 questions/task); 52.3% drop = absolute change from ~0.044 to ~0.021. Paper must report both absolute values and relative changes.\\n- FM3: **[primary]** hgate-dpo003-merged overcorrected politeness mean 0.574 vs baseline 0.502, gap +7.2pp (+14.3% relative), range +4.2pp ~ +10.4pp, 4/4 runs consistent; **[auxiliary]** mvp-004 single run: 0.605 vs 0.559 (+4.6pp, +8.2% relative)\\n\\n**External support**:\\n- FM1: basil2025playing_pretend (persona prompting drops MMLU 71.6%→66.3%); hu2026expert_persona (accuracy degradation up to 30pp under persona)\\n- FM2: gupta2026intra_fairness (bias spillover effect in targeted alignment)\\n- FM3: no direct external parallel — novel observation\\n\\n### C2: DPO+BCP interaction produces calibration reversal\\n**Evidence strength**: Strong (single model, 4 runs × 20 tasks = 80 episodes)\\n\\nDPO training, despite learning effectively (acc 0.75-1.0, loss 0.653), reverses BCP calibration direction when combined:\\n\\n| Metric | Base BCP (mvp-004) | DPO+BCP (hgate-dpo003-merged) |\\n|---|---|---|\\n| AAVE politeness gap | -0.091 (correct direction) | +0.064 (**reversed**) |\\n| Indian politeness gap | -0.099 (correct direction) | +0.063 (**reversed**) |\\n| H2 gap reduction | 25-28% (close to 30% threshold) | **-10.3%** (wrong direction) |\\n| Variant×run checks with gap expansion | — | **10/12** |\\n| Overcorrection rebound | +8.2% | **+14.3%** (amplified) |\\n\\n**Key insight**: DPO-003 training *improved* tool-calling ability (merged completion 60% vs base 40%, diag-lora-merge). The reversal is not a DPO training failure — it's an **interaction effect** between DPO alignment and BCP prompting.\\n\\n**External support**: lee2024dpo_toxicity (DPO bypasses rather than removes capabilities; alignment is fragile and reversible)\\n\\n### C3: Cross-scale validation\\n**Evidence strength**: [PENDING: qwen14b-bcp-001]\\n\\nQwen2.5-14B-Instruct-AWQ BCP evaluation in progress. If FM1-FM3 replicate at 14B scale, this strengthens the claim that failure modes are structural (not capacity-limited).\\n\\n**Current auxiliary evidence**:\\n- Llama-3-8B (llama-bcp-001): Floor effect (completion=5%). Only supports \\\"behavior shift observable at floor completion.\\\" **Cannot claim cross-model generalization** — tool-calling too weak to isolate BCP effect.\\n- Mistral-7B (mistral-bcp-001): completion=0%, model cannot do structured tool_calls with 16 tools. No usable data.\\n\\n**Hedging strategy**: If Qwen14B replicates → \\\"failure modes persist across model scales (7B, 14B).\\\" If not → limit scope to \\\"documented on Qwen2.5-7B; generalizability requires further investigation.\\\"\\n\\n### C4: Implications for future calibration research\\n**Evidence strength**: Analytical (grounded in C1-C3)\\n\\n- **Implication 1**: Prompt-based calibration of behavioral rates in multi-turn agent dialogue is fundamentally limited by the completion-calibration trade-off (FM1). This parallels the persona-accuracy trade-off (basil2025playing_pretend; hu2026expert_persona) but is more severe in agentic settings where tool-calling capability is at stake.\\n- **Implication 2**: Behavioral dimensions are coupled — calibrating politeness rate without affecting question rate (or completion) requires methods that can disentangle dimensions (FM2). Possible direction: per-dimension reward models or constrained decoding (cf. khan2026decoding).\\n- **Implication 3**: DPO alignment and prompt-based calibration can interact adversarially (FM4). Future work must evaluate calibration methods in combination, not in isolation.\\n- **Implication 4**: Overcorrection rebound (FM3) suggests models have an \\\"attractor basin\\\" for default behavioral rates that resists large perturbations. Gradual/iterative calibration may outperform one-shot extreme targets.\\n\\n---\\n\\n## Reviewer Concerns (Pre-empted Attack Surfaces)\\n\\n### RC1: \\\"Single model — how do we know this generalizes?\\\"\\n**Status**: Partially mitigated\\n- Qwen14B data [PENDING: qwen14b-bcp-001] provides cross-scale evidence\\n- Llama-3-8B/Mistral-7B failed due to tool-calling limitations, NOT because BCP worked on them\\n- FM1 aligns with persona-accuracy trade-off documented across GPT-4, Claude, Llama in basil2025playing_pretend and hu2026expert_persona\\n- **Honest hedge**: \\\"We document these failure modes on Qwen2.5-7B; external evidence from persona prompting literature suggests the mechanisms are general, but direct multi-model verification for agent dialogue remains future work.\\\"\\n\\n### RC2: \\\"n=20 tasks, high variance — statistical power?\\\"\\n**Response**:\\n- BCP results (mvp-004): n=19-20 per variant, single run. Variance is a valid concern for absolute numbers.\\n- DPO+BCP results (hgate-dpo003-merged): 4 independent runs × 20 tasks = 80 episodes. Reversal effect consistent across 10/12 variant×run checks — this is not a variance artifact.\\n- FM3 (rebound): consistent direction in 4/4 runs for overcorrected variant.\\n- **Mitigation**: Report all individual run data (no cherry-picking, per memory.md rule). Frame claims around direction and consistency, not precise magnitudes.\\n\\n### RC3: \\\"This is just negative results — where's the contribution?\\\"\\n**Response**:\\n- Negative-results papers exist at top venues (e.g., Findings track). But this is MORE than negative results:\\n  1. **Taxonomy**: First systematic categorization of calibration failure modes (FM1-FM4)\\n  2. **Mechanistic connections**: Link FM1→persona-accuracy trade-off, FM2→bias spillover, FM4→DPO bypass\\n  3. **Actionable implications**: Concrete constraints for future calibration methods\\n  4. **Interaction discovery**: FM4 (DPO+BCP reversal) is novel — no prior work documents this interaction\\n\\n### RC4: \\\"Why not try other calibration methods?\\\"\\n**Response**:\\n- BCP and DPO represent the two main paradigms (prompt-time vs training-time). Covering both provides good coverage.\\n- Paper scope is diagnosis (failure taxonomy), not exhaustive method search.\\n- Implications section points to alternative approaches (constrained decoding, per-dimension reward, iterative calibration).\\n\\n### RC5: \\\"The evaluation framework (tau-bench) is a confound — maybe BCP works on simpler tasks?\\\"\\n**Response**:\\n- tau-bench is the standard benchmark for tool-calling agent evaluation (yao2024taubench; sim2real2026gap uses it too).\\n- FM1 parallels persona-accuracy trade-off found on MMLU/general benchmarks — not tau-bench specific.\\n- But fairly: FM2 and FM3 may be task-dependent. Acknowledged in limitations.\\n\\n---\\n\\n## Evidence Map\\n\\n| Claim | Sub-claim | Primary Experiment | Metric | Value | Secondary Experiment |\\n|---|---|---|---|---|---|\\n| C1 | FM1: completion collapse | mvp-004 | mean completion retention | 52.3% (need ≥80%) | hgate-dpo003-merged (excl. run2: 47-51% drop) |\\n| C1 | FM2: cross-dim interference | mvp-004 | non-target dim shift | politeness -25.6%, qrate -52.3% | — |\\n| C1 | FM3: overcorrection rebound | hgate-dpo003-merged | overcorrected pol vs baseline | +7.2pp mean (+14.3% rel), 4/4 runs consistent | mvp-004 (+4.6pp, single run) |\\n| C2 | FM4: DPO reversal of BCP | hgate-dpo003-merged | H2 gap reduction | -10.3% (wrong direction) | — |\\n| C2 | FM4: gap expansion count | hgate-dpo003-merged | variant×run checks | 10/12 expanded | — |\\n| C2 | DPO training effective | dpo-003 | rewards accuracy | 0.75-1.0 | diag-lora-merge (merged 60% vs base 40%) |\\n| C2 | Direction comparison | mvp-004 vs hgate-dpo003-merged | AAVE pol gap | -0.091 → +0.064 | Indian: -0.099 → +0.063 |\\n| C3 | Cross-scale (7B→14B) | [PENDING: qwen14b-bcp-001] | FM1-FM3 replication | [PENDING] | — |\\n| C3 | Cross-model (auxiliary) | llama-bcp-001 | completion | 5% (floor) | Not usable for generalization |\\n\\n---\\n\\n## Contribution Statement\\n\\nWe present the first systematic taxonomy of calibration failure modes for LLM user simulators in agentic evaluation. Through controlled experiments on Qwen2.5-7B in the tau-bench retail domain, we identify four failure mechanisms — global behavior suppression, cross-dimension interference, overcorrection rebound, and DPO-BCP interaction reversal — that explain why both prompt-based and training-based calibration methods fail to correct dialect-dependent behavioral biases. Our findings establish concrete constraints for future calibration research and connect observed failures to broader phenomena in persona prompting and preference optimization.\\n\\n---\\n\\n## Key Literature Anchors\\n\\n| Role in Paper | Paper | What It Provides |\\n|---|---|---|\\n| Core motivation | sim2real2026gap (arXiv 2603.11245) | Quantifies sim-vs-human gap in τ-bench; diagnoses the problem we attempt to solve |\\n| FM1 mechanism | basil2025playing_pretend (arXiv 2512.05858) | Persona prompting degrades accuracy; explains completion collapse |\\n| FM1 mechanism | hu2026expert_persona (arXiv 2603.18507) | Persona-accuracy trade-off up to 30pp; instruction-tuned models more susceptible |\\n| FM2 mechanism | gupta2026intra_fairness (arXiv 2602.16438) | Bias spillover in targeted alignment; parallel to cross-dim interference |\\n| FM4 mechanism | lee2024dpo_toxicity (ICML 2024) | DPO bypasses rather than removes capabilities; fragile alignment |\\n| Evaluation framework | yao2024taubench (arXiv 2406.12045) | τ-bench retail domain, pass^k metric |\\n| Bias context | seshadri2026lost (arXiv 2601.17087) | AAVE/Indian English speakers get worst simulator calibration |\\n| DPO method | rafailov2023dpo (NeurIPS 2023) | Core DPO algorithm reference |\\n\\n---\\n\\n## Open Items\\n\\n- [ ] **qwen14b-bcp-001 results** — if positive: add C3 cross-scale evidence, strengthen generalizability claims. If negative: restrict scope, add to limitations.\\n- [ ] **Statistical tests** — add bootstrap CI for key comparisons (FM4 reversal direction, FM3 rebound magnitude) once data is finalized.\\n- [ ] **Figure plan** — taxonomy diagram (FM1-FM4), gap reversal visualization (base vs DPO politeness gaps), completion collapse heatmap.\\n\", \"total_chars\": 12943, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2abdebbe-f3bd-4182-bff6-4d04fba6ecf2",
  "uuid": "8847ddbd-8627-4d7a-8bab-3b5cd2f87399",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing: Calibration Failure Taxonomy for LLM User Simulators\\\\n\\\\n> Plan B story — Director approved 2026-05-13\\\\n> Target: EMNLP 2026 Findings (ARR deadline 2026-05-25)\\\\n\\\\n---\\\\n\\\\n## Title Candidates\\\\n\\\\n1. **\\\\\\\"Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation\\\\\\\"**\\\\n   - Pro: 直接点明贡献（taxonomy），关键词覆盖好\\\\n   - Con: 稍长\\\\n\\\\n2. **\\\\\\\"The Calibration Trap: Prompt-Based and Training-Based Corrections Both Fail for Dialect Bias in LLM User Simulators\\\\\\\"**\\\\n   - Pro: \\\\\\\"trap\\\\\\\" 吸引眼球，涵盖两种方法\\\\n   - Con: 可能暗示过于 negative\\\\n\\\\n3. **\\\\\\\"Behavioral Calibration Considered Harmful? Systematic Failure Modes in Dialect-Aware User Simulation\\\\\\\"**\\\\n   - Pro: Dijkstra 风格标题引发好奇，问号留余地\\\\n   - Con: \\\\\\\"Considered Harmful\\\\\\\" 可能被认为 cliché\\\\n\\\\n**推荐**: Title 1 — 最准确传达贡献，reviewer-friendly。\\\\n\\\\n---\\\\n\\\\n## Core Story\\\\n\\\\n**Problem**: LLM user simulators exhibit dialect-dependent behavioral biases — AAVE and Indian English speakers receive systematically different politeness and question-asking patterns compared to Standard American English (sim2real2026gap; seshadri2026lost). These biases propagate into agent evaluation, undermining fairness.\\\\n\\\\n**Attempted Solution**: We apply two complementary calibration strategies:\\\\n- **BCP (Behavioral Calibration Prompting)**: Prompt-level injection of target behavioral rates\\\\n- **DPO (Direct Preference Optimization)**: Training-level alignment using dialect-calibrated preference pairs\\\\n\\\\n**Finding**: Both strategies fail systematically. We document **the first taxonomy of calibration failure modes** for LLM user simulators, identifying four distinct mechanisms that explain why seemingly reasonable calibration interventions produce counterproductive outcomes.\\\\n\\\\n**Framing**: This is NOT \\\\\\\"we tried and failed.\\\\\\\" This is a systematic empirical analysis that (1) identifies previously undocumented failure mechanisms, (2) connects them to known phenomena in persona prompting and alignment, and (3) provides actionable constraints for future calibration research.\\\\n\\\\n---\\\\n\\\\n## Core Claims\\\\n\\\\n### C1: BCP produces three systematic failure mechanisms\\\\n**Evidence strength**: Moderate (single model, single run, n=19-20 per variant)\\\\n\\\\n| Failure Mode | Description | Key Metric | exp_id |\\\\n|---|---|---|---|\\\\n| FM1: Global Behavior Suppression | BCP calibration prompts collapse task completion regardless of target dimension | completion retention 52.3% (threshold ≥80%) | mvp-004 |\\\\n| FM2: Cross-Dimension Interference | Targeting one behavioral dimension perturbs non-targeted dimensions | politeness -25.6% when targeting question_rate; question_rate -52.3% when targeting politeness | mvp-004 |\\\\n| FM3: Overcorrection Rebound | Requesting extreme behavioral shift causes model to rebound in opposite direction | overcorrected politeness +4.2pp ~ +10.4pp above baseline (4 runs, 4/4 consistent) | hgate-dpo003-merged |\\\\n\\\\n**Supporting numbers (mvp-004, Qwen2.5-7B-Instruct, n=19-20)**:\\\\n- FM1: aave completion 0.100 vs baseline 0.368 (-72.8%); indian 0.150 (-59.2%); mean calibrated 0.193\\\\n- FM2: single_dim_question politeness drops 25.6% (non-target); single_dim_politeness question_rate drops 52.3% (non-target)\\\\n  - **Base rate caveat**: question_rate baseline = 0.044 (~0.8 questions/task); 52.3% drop = absolute change from ~0.044 to ~0.021. Paper must report both absolute values and relative changes.\\\\n- FM3: **[primary]** hgate-dpo003-merged overcorrected politeness mean 0.574 vs baseline 0.502, gap +7.2pp (+14.3% relative), range +4.2pp ~ +10.4pp, 4/4 runs consistent; **[auxiliary]** mvp-004 single run: 0.605 vs 0.559 (+4.6pp, +8.2% relative)\\\\n\\\\n**External support**:\\\\n- FM1: basil2025playing_pretend (persona prompting drops MMLU 71.6%→66.3%); hu2026expert_persona (accuracy degradation up to 30pp under persona)\\\\n- FM2: gupta2026intra_fairness (bias spillover effect in targeted alignment)\\\\n- FM3: no direct external parallel — novel observation\\\\n\\\\n### C2: DPO+BCP interaction produces calibration reversal\\\\n**Evidence strength**: Strong (single model, 4 runs × 20 tasks = 80 episodes)\\\\n\\\\nDPO training, despite learning effectively (acc 0.75-1.0, loss 0.653), reverses BCP calibration direction when combined:\\\\n\\\\n| Metric | Base BCP (mvp-004) | DPO+BCP (hgate-dpo003-merged) |\\\\n|---|---|---|\\\\n| AAVE politeness gap | -0.091 (correct direction) | +0.064 (**reversed**) |\\\\n| Indian politeness gap | -0.099 (correct direction) | +0.063 (**reversed**) |\\\\n| H2 gap reduction | 25-28% (close to 30% threshold) | **-10.3%** (wrong direction) |\\\\n| Variant×run checks with gap expansion | — | **10/12** |\\\\n| Overcorrection rebound | +8.2% | **+14.3%** (amplified) |\\\\n\\\\n**Key insight**: DPO-003 training *improved* tool-calling ability (merged completion 60% vs base 40%, diag-lora-merge). The reversal is not a DPO training failure — it's an **interaction effect** between DPO alignment and BCP prompting.\\\\n\\\\n**External support**: lee2024dpo_toxicity (DPO bypasses rather than removes capabilities; alignment is fragile and reversible)\\\\n\\\\n### C3: Cross-scale validation\\\\n**Evidence strength**: [PENDING: qwen14b-bcp-001]\\\\n\\\\nQwen2.5-14B-Instruct-AWQ BCP evaluation in progress. If FM1-FM3 replicate at 14B scale, this strengthens the claim that failure modes are structural (not capacity-limited).\\\\n\\\\n**Current auxiliary evidence**:\\\\n- Llama-3-8B (llama-bcp-001): Floor effect (completion=5%). Only supports \\\\\\\"behavior shift observable at floor completion.\\\\\\\" **Cannot claim cross-model generalization** — tool-calling too weak to isolate BCP effect.\\\\n- Mistral-7B (mistral-bcp-001): completion=0%, model cannot do structured tool_calls with 16 tools. No usable data.\\\\n\\\\n**Hedging strategy**: If Qwen14B replicates → \\\\\\\"failure modes persist across model scales (7B, 14B).\\\\\\\" If not → limit scope to \\\\\\\"documented on Qwen2.5-7B; generalizability requires further investigation.\\\\\\\"\\\\n\\\\n### C4: Implications for future calibration research\\\\n**Evidence strength**: Analytical (grounded in C1-C3)\\\\n\\\\n- **Implication 1**: Prompt-based calibration of behavioral rates in multi-turn agent dialogue is fundamentally limited by the completion-calibration trade-off (FM1). This parallels the persona-accuracy trade-off (basil2025playing_pretend; hu2026expert_persona) but is more severe in agentic settings where tool-calling capability is at stake.\\\\n- **Implication 2**: Behavioral dimensions are coupled — calibrating politeness rate without affecting question rate (or completion) requires methods that can disentangle dimensions (FM2). Possible direction: per-dimension reward models or constrained decoding (cf. khan2026decoding).\\\\n- **Implication 3**: DPO alignment and prompt-based calibration can interact adversarially (FM4). Future work must evaluate calibration methods in combination, not in isolation.\\\\n- **Implication 4**: Overcorrection rebound (FM3) suggests models have an \\\\\\\"attractor basin\\\\\\\" for default behavioral rates that resists large perturbations. Gradual/iterative calibration may outperform one-shot extreme targets.\\\\n\\\\n---\\\\n\\\\n## Reviewer Concerns (Pre-empted Attack Surfaces)\\\\n\\\\n### RC1: \\\\\\\"Single model — how do we know this generalizes?\\\\\\\"\\\\n**Status**: Partially mitigated\\\\n- Qwen14B data [PENDING: qwen14b-bcp-001] provides cross-scale evidence\\\\n- Llama-3-8B/Mistral-7B failed due to tool-calling limitations, NOT because BCP worked on them\\\\n- FM1 aligns with persona-accuracy trade-off documented across GPT-4, Claude, Llama in basil2025playing_pretend and hu2026expert_persona\\\\n- **Honest hedge**: \\\\\\\"We document these failure modes on Qwen2.5-7B; external evidence from persona prompting literature suggests the mechanisms are general, but direct multi-model verification for agent dialogue remains future work.\\\\\\\"\\\\n\\\\n### RC2: \\\\\\\"n=20 tasks, high variance — statistical power?\\\\\\\"\\\\n**Response**:\\\\n- BCP results (mvp-004): n=19-20 per variant, single run. Variance is a valid concern for absolute numbers.\\\\n- DPO+BCP results (hgate-dpo003-merged): 4 independent runs × 20 tasks = 80 episodes. Reversal effect consistent across 10/12 variant×run checks — this is not a variance artifact.\\\\n- FM3 (rebound): consistent direction in 4/4 runs for overcorrected variant.\\\\n- **Mitigation**: Report all individual run data (no cherry-picking, per memory.md rule). Frame claims around direction and consistency, not precise magnitudes.\\\\n\\\\n### RC3: \\\\\\\"This is just negative results — where's the contribution?\\\\\\\"\\\\n**Response**:\\\\n- Negative-results papers exist at top venues (e.g., Findings track). But this is MORE than negative results:\\\\n  1. **Taxonomy**: First systematic categorization of calibration failure modes (FM1-FM4)\\\\n  2. **Mechanistic connections**: Link FM1→persona-accuracy trade-off, FM2→bias spillover, FM4→DPO bypass\\\\n  3. **Actionable implications**: Concrete constraints for future calibration methods\\\\n  4. **Interaction discovery**: FM4 (DPO+BCP reversal) is novel — no prior work documents this interaction\\\\n\\\\n### RC4: \\\\\\\"Why not try other calibration methods?\\\\\\\"\\\\n**Response**:\\\\n- BCP and DPO represent the two main paradigms (prompt-time vs training-time). Covering both provides good coverage.\\\\n- Paper scope is diagnosis (failure taxonomy), not exhaustive method search.\\\\n- Implications section points to alternative approaches (constrained decoding, per-dimension reward, iterative calibration).\\\\n\\\\n### RC5: \\\\\\\"The evaluation framework (tau-bench) is a confound — maybe BCP works on simpler tasks?\\\\\\\"\\\\n**Response**:\\\\n- tau-bench is the standard benchmark for tool-calling agent evaluation (yao2024taubench; sim2real2026gap uses it too).\\\\n- FM1 parallels persona-accuracy trade-off found on MMLU/general benchmarks — not tau-bench specific.\\\\n- But fairly: FM2 and FM3 may be task-dependent. Acknowledged in limitations.\\\\n\\\\n---\\\\n\\\\n## Evidence Map\\\\n\\\\n| Claim | Sub-claim | Primary Experiment | Metric | Value | Secondary Experiment |\\\\n|---|---|---|---|---|---|\\\\n| C1 | FM1: completion collapse | mvp-004 | mean completion retention | 52.3% (need ≥80%) | hgate-dpo003-merged (excl. run2: 47-51% drop) |\\\\n| C1 | FM2: cross-dim interference | mvp-004 | non-target dim shift | politeness -25.6%, qrate -52.3% | — |\\\\n| C1 | FM3: overcorrection rebound | hgate-dpo003-merged | overcorrected pol vs baseline | +7.2pp mean (+14.3% rel), 4/4 runs consistent | mvp-004 (+4.6pp, single run) |\\\\n| C2 | FM4: DPO reversal of BCP | hgate-dpo003-merged | H2 gap reduction | -10.3% (wrong direction) | — |\\\\n| C2 | FM4: gap expansion count | hgate-dpo003-merged | variant×run checks | 10/12 expanded | — |\\\\n| C2 | DPO training effective | dpo-003 | rewards accuracy | 0.75-1.0 | diag-lora-merge (merged 60% vs base 40%) |\\\\n| C2 | Direction comparison | mvp-004 vs hgate-dpo003-merged | AAVE pol gap | -0.091 → +0.064 | Indian: -0.099 → +0.063 |\\\\n| C3 | Cross-scale (7B→14B) | [PENDING: qwen14b-bcp-001] | FM1-FM3 replication | [PENDING] | — |\\\\n| C3 | Cross-model (auxiliary) | llama-bcp-001 | completion | 5% (floor) | Not usable for generalization |\\\\n\\\\n---\\\\n\\\\n## Contribution Statement\\\\n\\\\nWe present the first systematic taxonomy of calibration failure modes for LLM user simulators in agentic evaluation. Through controlled experiments on Qwen2.5-7B in the tau-bench retail domain, we identify four failure mechanisms — global behavior suppression, cross-dimension interference, overcorrection rebound, and DPO-BCP interaction reversal — that explain why both prompt-based and training-based calibration methods fail to correct dialect-dependent behavioral biases. Our findings establish concrete constraints for future calibration research and connect observed failures to broader phenomena in persona prompting and preference optimization.\\\\n\\\\n---\\\\n\\\\n## Key Literature Anchors\\\\n\\\\n| Role in Paper | Paper | What It Provides |\\\\n|---|---|---|\\\\n| Core motivation | sim2real2026gap (arXiv 2603.11245) | Quantifies sim-vs-human gap in τ-bench; diagnoses the problem we attempt to solve |\\\\n| FM1 mechanism | basil2025playing_pretend (arXiv 2512.05858) | Persona prompting degrades accuracy; explains completion collapse |\\\\n| FM1 mechanism | hu2026expert_persona (arXiv 2603.18507) | Persona-accuracy trade-off up to 30pp; instruction-tuned models more susceptible |\\\\n| FM2 mechanism | gupta2026intra_fairness (arXiv 2602.16438) | Bias spillover in targeted alignment; parallel to cross-dim interference |\\\\n| FM4 mechanism | lee2024dpo_toxicity (ICML 2024) | DPO bypasses rather than removes capabilities; fragile alignment |\\\\n| Evaluation framework | yao2024taubench (arXiv 2406.12045) | τ-bench retail domain, pass^k metric |\\\\n| Bias context | seshadri2026lost (arXiv 2601.17087) | AAVE/Indian English speakers get worst simulator calibration |\\\\n| DPO method | rafailov2023dpo (NeurIPS 2023) | Core DPO algorithm reference |\\\\n\\\\n---\\\\n\\\\n## Open Items\\\\n\\\\n- [ ] **qwen14b-bcp-001 results** — if positive: add C3 cross-scale evidence, strengthen generalizability claims. If negative: restrict scope, add to limitations.\\\\n- [ ] **Statistical tests** — add bootstrap CI for key comparisons (FM4 reversal direction, FM3 rebound magnitude) once data is finalized.\\\\n- [ ] **Figure plan** — taxonomy diagram (FM1-FM4), gap reversal visualization (base vs DPO politeness gaps), completion collapse heatmap.\\\\n\\\", \\\"total_chars\\\": 12943, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/paper_framing.md\", \"content\": \"# Paper Framing: Calibration Failure Taxonomy for LLM User Simulators\\n\\n> Plan B story — Director approved 2026-05-13\\n> Target: EMNLP 2026 Findings (ARR deadline 2026-05-25)\\n\\n---\\n\\n## Title Candidates\\n\\n1. **\\\"Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation\\\"**\\n   - Pro: 直接点明贡献（taxonomy），关键词覆盖好\\n   - Con: 稍长\\n\\n2. **\\\"The Calibration Trap: Prompt-Based and Training-Based Corrections Both Fail for Dialect Bias in LLM User Simulators\\\"**\\n   - Pro: \\\"trap\\\" 吸引眼球，涵盖两种方法\\n   - Con: 可能暗示过于 negative\\n\\n3. **\\\"Behavioral Calibration Considered Harmful? Systematic Failure Modes in Dialect-Aware User Simulation\\\"**\\n   - Pro: Dijkstra 风格标题引发好奇，问号留余地\\n   - Con: \\\"Considered Harmful\\\" 可能被认为 cliché\\n\\n**推荐**: Title 1 — 最准确传达贡献，reviewer-friendly。\\n\\n---\\n\\n## Core Story\\n\\n**Problem**: LLM user simulators exhibit dialect-dependent behavioral biases — AAVE and Indian English speakers receive systematically different politeness and question-asking patterns compared to Standard American English (sim2real2026gap; seshadri2026lost). These biases propagate into agent evaluation, undermining fairness.\\n\\n**Attempted Solution**: We apply two complementary calibration strategies:\\n- **BCP (Behavioral Calibration Prompting)**: Prompt-level injection of target behavioral rates\\n- **DPO (Direct Preference Optimization)**: Training-level alignment using dialect-calibrated preference pairs\\n\\n**Finding**: Both strategies fail systematically. We document **the first taxonomy of calibration failure modes** for LLM user simulators, identifying four distinct mechanisms that explain why seemingly reasonable calibration interventions produce counterproductive outcomes.\\n\\n**Framing**: This is NOT \\\"we tried and failed.\\\" This is a systematic empirical analysis that (1) identifies previously undocumented failure mechanisms, (2) connects them to known phenomena in persona prompting and alignment, and (3) provides actionable constraints for future calibration research.\\n\\n---\\n\\n## Core Claims\\n\\n### C1: BCP produces three systematic failure mechanisms\\n**Evidence strength**: Moderate (single model, single run, n=19-20 per variant)\\n\\n| Failure Mode | Description | Key Metric | exp_id |\\n|---|---|---|---|\\n| FM1: Global Behavior Suppression | BCP calibration prompts collapse task completion regardless of target dimension | completion retention 52.3% (threshold ≥80%) | mvp-004 |\\n| FM2: Cross-Dimension Interference | Targeting one behavioral dimension perturbs non-targeted dimensions | politeness -25.6% when targeting question_rate; question_rate -52.3% when targeting politeness | mvp-004 |\\n| FM3: Overcorrection Rebound | Requesting extreme behavioral shift causes model to rebound in opposite direction | overcorrected politeness +4.2pp ~ +10.4pp above baseline (4 runs, 4/4 consistent) | hgate-dpo003-merged |\\n\\n**Supporting numbers (mvp-004, Qwen2.5-7B-Instruct, n=19-20)**:\\n- FM1: aave completion 0.100 vs baseline 0.368 (-72.8%); indian 0.150 (-59.2%); mean calibrated 0.193\\n- FM2: single_dim_question politeness drops 25.6% (non-target); single_dim_politeness question_rate drops 52.3% (non-target)\\n  - **Base rate caveat**: question_rate baseline = 0.044 (~0.8 questions/task); 52.3% drop = absolute change from ~0.044 to ~0.021. Paper must report both absolute values and relative changes.\\n- FM3: **[primary]** hgate-dpo003-merged overcorrected politeness mean 0.574 vs baseline 0.502, gap +7.2pp (+14.3% relative), range +4.2pp ~ +10.4pp, 4/4 runs consistent; **[auxiliary]** mvp-004 single run: 0.605 vs 0.559 (+4.6pp, +8.2% relative)\\n\\n**External support**:\\n- FM1: basil2025playing_pretend (persona prompting drops MMLU 71.6%→66.3%); hu2026expert_persona (accuracy degradation up to 30pp under persona)\\n- FM2: gupta2026intra_fairness (bias spillover effect in targeted alignment)\\n- FM3: no direct external parallel — novel observation\\n\\n### C2: DPO+BCP interaction produces calibration reversal\\n**Evidence strength**: Strong (single model, 4 runs × 20 tasks = 80 episodes)\\n\\nDPO training, despite learning effectively (acc 0.75-1.0, loss 0.653), reverses BCP calibration direction when combined:\\n\\n| Metric | Base BCP (mvp-004) | DPO+BCP (hgate-dpo003-merged) |\\n|---|---|---|\\n| AAVE politeness gap | -0.091 (correct direction) | +0.064 (**reversed**) |\\n| Indian politeness gap | -0.099 (correct direction) | +0.063 (**reversed**) |\\n| H2 gap reduction | 25-28% (close to 30% threshold) | **-10.3%** (wrong direction) |\\n| Variant×run checks with gap expansion | — | **10/12** |\\n| Overcorrection rebound | +8.2% | **+14.3%** (amplified) |\\n\\n**Key insight**: DPO-003 training *improved* tool-calling ability (merged completion 60% vs base 40%, diag-lora-merge). The reversal is not a DPO training failure — it's an **interaction effect** between DPO alignment and BCP prompting.\\n\\n**External support**: lee2024dpo_toxicity (DPO bypasses rather than removes capabilities; alignment is fragile and reversible)\\n\\n### C3: Cross-scale validation\\n**Evidence strength**: [PENDING: qwen14b-bcp-001]\\n\\nQwen2.5-14B-Instruct-AWQ BCP evaluation in progress. If FM1-FM3 replicate at 14B scale, this strengthens the claim that failure modes are structural (not capacity-limited).\\n\\n**Current auxiliary evidence**:\\n- Llama-3-8B (llama-bcp-001): Floor effect (completion=5%). Only supports \\\"behavior shift observable at floor completion.\\\" **Cannot claim cross-model generalization** — tool-calling too weak to isolate BCP effect.\\n- Mistral-7B (mistral-bcp-001): completion=0%, model cannot do structured tool_calls with 16 tools. No usable data.\\n\\n**Hedging strategy**: If Qwen14B replicates → \\\"failure modes persist across model scales (7B, 14B).\\\" If not → limit scope to \\\"documented on Qwen2.5-7B; generalizability requires further investigation.\\\"\\n\\n### C4: Implications for future calibration research\\n**Evidence strength**: Analytical (grounded in C1-C3)\\n\\n- **Implication 1**: Prompt-based calibration of behavioral rates in multi-turn agent dialogue is fundamentally limited by the completion-calibration trade-off (FM1). This parallels the persona-accuracy trade-off (basil2025playing_pretend; hu2026expert_persona) but is more severe in agentic settings where tool-calling capability is at stake.\\n- **Implication 2**: Behavioral dimensions are coupled — calibrating politeness rate without affecting question rate (or completion) requires methods that can disentangle dimensions (FM2). Possible direction: per-dimension reward models or constrained decoding (cf. khan2026decoding).\\n- **Implication 3**: DPO alignment and prompt-based calibration can interact adversarially (FM4). Future work must evaluate calibration methods in combination, not in isolation.\\n- **Implication 4**: Overcorrection rebound (FM3) suggests models have an \\\"attractor basin\\\" for default behavioral rates that resists large perturbations. Gradual/iterative calibration may outperform one-shot extreme targets.\\n\\n---\\n\\n## Reviewer Concerns (Pre-empted Attack Surfaces)\\n\\n### RC1: \\\"Single model — how do we know this generalizes?\\\"\\n**Status**: Partially mitigated\\n- Qwen14B data [PENDING: qwen14b-bcp-001] provides cross-scale evidence\\n- Llama-3-8B/Mistral-7B failed due to tool-calling limitations, NOT because BCP worked on them\\n- FM1 aligns with persona-accuracy trade-off documented across GPT-4, Claude, Llama in basil2025playing_pretend and hu2026expert_persona\\n- **Honest hedge**: \\\"We document these failure modes on Qwen2.5-7B; external evidence from persona prompting literature suggests the mechanisms are general, but direct multi-model verification for agent dialogue remains future work.\\\"\\n\\n### RC2: \\\"n=20 tasks, high variance — statistical power?\\\"\\n**Response**:\\n- BCP results (mvp-004): n=19-20 per variant, single run. Variance is a valid concern for absolute numbers.\\n- DPO+BCP results (hgate-dpo003-merged): 4 independent runs × 20 tasks = 80 episodes. Reversal effect consistent across 10/12 variant×run checks — this is not a variance artifact.\\n- FM3 (rebound): consistent direction in 4/4 runs for overcorrected variant.\\n- **Mitigation**: Report all individual run data (no cherry-picking, per memory.md rule). Frame claims around direction and consistency, not precise magnitudes.\\n\\n### RC3: \\\"This is just negative results — where's the contribution?\\\"\\n**Response**:\\n- Negative-results papers exist at top venues (e.g., Findings track). But this is MORE than negative results:\\n  1. **Taxonomy**: First systematic categorization of calibration failure modes (FM1-FM4)\\n  2. **Mechanistic connections**: Link FM1→persona-accuracy trade-off, FM2→bias spillover, FM4→DPO bypass\\n  3. **Actionable implications**: Concrete constraints for future calibration methods\\n  4. **Interaction discovery**: FM4 (DPO+BCP reversal) is novel — no prior work documents this interaction\\n\\n### RC4: \\\"Why not try other calibration methods?\\\"\\n**Response**:\\n- BCP and DPO represent the two main paradigms (prompt-time vs training-time). Covering both provides good coverage.\\n- Paper scope is diagnosis (failure taxonomy), not exhaustive method search.\\n- Implications section points to alternative approaches (constrained decoding, per-dimension reward, iterative calibration).\\n\\n### RC5: \\\"The evaluation framework (tau-bench) is a confound — maybe BCP works on simpler tasks?\\\"\\n**Response**:\\n- tau-bench is the standard benchmark for tool-calling agent evaluation (yao2024taubench; sim2real2026gap uses it too).\\n- FM1 parallels persona-accuracy trade-off found on MMLU/general benchmarks — not tau-bench specific.\\n- But fairly: FM2 and FM3 may be task-dependent. Acknowledged in limitations.\\n\\n---\\n\\n## Evidence Map\\n\\n| Claim | Sub-claim | Primary Experiment | Metric | Value | Secondary Experiment |\\n|---|---|---|---|---|---|\\n| C1 | FM1: completion collapse | mvp-004 | mean completion retention | 52.3% (need ≥80%) | hgate-dpo003-merged (excl. run2: 47-51% drop) |\\n| C1 | FM2: cross-dim interference | mvp-004 | non-target dim shift | politeness -25.6%, qrate -52.3% | — |\\n| C1 | FM3: overcorrection rebound | hgate-dpo003-merged | overcorrected pol vs baseline | +7.2pp mean (+14.3% rel), 4/4 runs consistent | mvp-004 (+4.6pp, single run) |\\n| C2 | FM4: DPO reversal of BCP | hgate-dpo003-merged | H2 gap reduction | -10.3% (wrong direction) | — |\\n| C2 | FM4: gap expansion count | hgate-dpo003-merged | variant×run checks | 10/12 expanded | — |\\n| C2 | DPO training effective | dpo-003 | rewards accuracy | 0.75-1.0 | diag-lora-merge (merged 60% vs base 40%) |\\n| C2 | Direction comparison | mvp-004 vs hgate-dpo003-merged | AAVE pol gap | -0.091 → +0.064 | Indian: -0.099 → +0.063 |\\n| C3 | Cross-scale (7B→14B) | [PENDING: qwen14b-bcp-001] | FM1-FM3 replication | [PENDING] | — |\\n| C3 | Cross-model (auxiliary) | llama-bcp-001 | completion | 5% (floor) | Not usable for generalization |\\n\\n---\\n\\n## Contribution Statement\\n\\nWe present the first systematic taxonomy of calibration failure modes for LLM user simulators in agentic evaluation. Through controlled experiments on Qwen2.5-7B in the tau-bench retail domain, we identify four failure mechanisms — global behavior suppression, cross-dimension interference, overcorrection rebound, and DPO-BCP interaction reversal — that explain why both prompt-based and training-based calibration methods fail to correct dialect-dependent behavioral biases. Our findings establish concrete constraints for future calibration research and connect observed failures to broader phenomena in persona prompting and preference optimization.\\n\\n---\\n\\n## Key Literature Anchors\\n\\n| Role in Paper | Paper | What It Provides |\\n|---|---|---|\\n| Core motivation | sim2real2026gap (arXiv 2603.11245) | Quantifies sim-vs-human gap in τ-bench; diagnoses the problem we attempt to solve |\\n| FM1 mechanism | basil2025playing_pretend (arXiv 2512.05858) | Persona prompting degrades accuracy; explains completion collapse |\\n| FM1 mechanism | hu2026expert_persona (arXiv 2603.18507) | Persona-accuracy trade-off up to 30pp; instruction-tuned models more susceptible |\\n| FM2 mechanism | gupta2026intra_fairness (arXiv 2602.16438) | Bias spillover in targeted alignment; parallel to cross-dim interference |\\n| FM4 mechanism | lee2024dpo_toxicity (ICML 2024) | DPO bypasses rather than removes capabilities; fragile alignment |\\n| Evaluation framework | yao2024taubench (arXiv 2406.12045) | τ-bench retail domain, pass^k metric |\\n| Bias context | seshadri2026lost (arXiv 2601.17087) | AAVE/Indian English speakers get worst simulator calibration |\\n| DPO method | rafailov2023dpo (NeurIPS 2023) | Core DPO algorithm reference |\\n\\n---\\n\\n## Open Items\\n\\n- [ ] **qwen14b-bcp-001 results** — if positive: add C3 cross-scale evidence, strengthen generalizability claims. If negative: restrict scope, add to limitations.\\n- [ ] **Statistical tests** — add bootstrap CI for key comparisons (FM4 reversal direction, FM3 rebound magnitude) once data is finalized.\\n- [ ] **Figure plan** — taxonomy diagram (FM1-FM4), gap reversal visualization (base vs DPO politeness gaps), completion collapse heatmap.\\n\", \"total_chars\": 12943, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 12_

<details><summary>Logged reasoning block</summary>

```text
Now I have both source files. Let me draft the Related Work section based on the task requirements, organizing by the four subtopics specified, using only citations from literature_map.yaml.

Let me organize the papers by subtopic:

**§2.1 LLM-Based User Simulation for Agent Evaluation**
- yao2024taubench — τ-bench framework
- sim2real2026gap — sim2real gap, USI metric
- nakash2026divert — diversity-guided user simulation
- liu2024agentbench — agent benchmark
- wang2024mint — multi-turn evaluation
- naous2025flipping — User LMs


- sekulic2024daus — DAUS domain-aware user simulator
- ahmad2025diversity — user diversity simulation
- seshadri2026lost — LLM simulators unreliable across demographics

**§2.2 Behavioral Calibration of Language Models**
- zhao2021calibrate — calibrate before use
- basil2025playing_pretend — persona prompting degrades accuracy
- hu2026expert_persona — expert persona accuracy damage
- li2025persona — LLM persona biases
- abdulhai2025consistent — multi-turn RL for persona consistency

**§2.3 Preference Optimization for Bias Mitigation**
- rafailov2023dpo — DPO
- khan2026decoding — decoding-time debiasing
- lee2024dpo_toxicity — DPO bypasses rather than removes bias
- gupta2026intra_fairness — intra-fairness spillover effects
- wang2024alignment — alignment survey

**§2.4 Dialect and Sociolinguistic Bias in NLP**

Now I'm looking at the literature on dialect representation and sociolinguistic variation in NLP systems, covering benchmarks for AAVE and multi-dialect evaluation, cross-dialect generalization, and foundational work on dialect-demographic interactions and linguistic pragmatics across varieties of English.

I need to structure each subsection to be around 100-150 words, drawing on the papers I've mapped, and finish with a clear gap or open question in the literature.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2abdebbe-f3bd-4182-bff6-4d04fba6ecf2",
  "uuid": "fd21102b-994a-4bc5-a494-01efa0f38076",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Du258zBcqFXrgrTyhUDFKZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13668,
      "cache_read_input_tokens": 24006,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13668
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

_source line 13_

Materials loaded. Now drafting the Related Work section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2abdebbe-f3bd-4182-bff6-4d04fba6ecf2",
  "uuid": "04434c5c-1b9f-448e-9891-09b2d66319e9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Du258zBcqFXrgrTyhUDFKZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13668,
      "cache_read_input_tokens": 24006,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13668
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01JvDL3cxTFfTPQdtysZ2iS9`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
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
  "session_id": "2abdebbe-f3bd-4182-bff6-4d04fba6ecf2",
  "uuid": "fd6e3e6e-140d-40d9-af9c-159a17cb4ef1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Du258zBcqFXrgrTyhUDFKZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13668,
      "cache_read_input_tokens": 24006,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13668
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

_source line 15 · 2026-05-13T08:20:22.685Z_

<details><summary>↩ Tool result · `toolu_01JvDL3cxTFfTPQdtysZ2iS9`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
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
  "session_id": "2abdebbe-f3bd-4182-bff6-4d04fba6ecf2",
  "uuid": "679a38dc-a887-4025-a765-5e3fcd6a7480",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 25
  }
}
```

</details>

---

### Assistant

_source line 16_

<details><summary>Logged reasoning block</summary>

```text
Now let me write the Related Work draft. I need to carefully organize papers from the literature_map into the four subtopics, making sure every citation comes from the map.

Let me draft each section:

**§2.1 LLM-Based User Simulation for Agent Evaluation**
Papers to use: yao2024taubench, sim2real2026gap, seshadri2026lost, naous2025flipping, nakash2026divert, sekulic2024daus, ahmad2025diversity, liu2024agentbench, wang2024mint, abdulhai2025consistent
 
Now I'm organizing the remaining three sections with their respective papers: behavioral calibration covering how language models can be adjusted to match specific personas and behaviors, preference optimization methods that address bias through techniques like DPO and decoding strategies, and finally sociolinguistic variation in NLP systems including dialect representation and fairness benchmarks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2abdebbe-f3bd-4182-bff6-4d04fba6ecf2",
  "uuid": "6cee532b-a06a-4955-af7d-f3d396435dee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ViXiBLimRpitsUvW3MsBMd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1549,
      "cache_read_input_tokens": 37674,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1549
      },
      "output_tokens": 24,
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

<details open><summary>🔧 Tool call — Write · `toolu_01TDz8HV4GUtBQQeYirw8qCm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/artifacts/section_related_work_draft.md",
  "content": "# 2 Related Work\n\n## 2.1 LLM-Based User Simulation for Agent Evaluation\n\nLLM-based user simulators have become central to evaluating tool-calling agents. Yao et al. (2024) introduce τ-bench, a benchmark pairing an LLM user simulator with a tool-calling agent in retail and airline domains, and propose the pass^k reliability metric. Liu et al. (2024) and Wang et al. (2024) establish complementary multi-environment and multi-turn evaluation paradigms, though neither incorporates demographic variation in their simulated users. Naous et al. (2025) demonstrate that purpose-built User LMs outperform repurposed assistant models, with GPT-4o success rates dropping from 74.6% to 57.4% under realistic simulation. Sekulić et al. (2024) show that domain-aware fine-tuning improves user goal fulfillment, while Ahmad et al. (2025) generate diverse user profiles with varied demographics and conversational styles. Nakash et al. (2026) address evaluation efficiency through diversity-guided branching trajectories. Most critically, Zhou et al. (2026) conduct the first full τ-bench evaluation with 451 real humans, finding that LLM simulators are excessively cooperative and stylistically uniform, inflating agent success rates. Seshadri et al. (2026) further document that AAVE and Indian English speakers experience the worst calibration errors. However, none of these works attempt to *correct* the identified sim-to-real gaps through behavioral calibration—they diagnose without prescribing, leaving open whether calibration methods can close the fidelity gaps they identify.\n\n## 2.2 Behavioral Calibration of Language Models\n\nPrompt-based calibration has a rich history: Zhao et al. (2021) show that contextual calibration of output distributions can improve few-shot accuracy by up to 30%, but their method targets classification biases, not behavioral rates in generation. In multi-turn settings, Abdulhai et al. (2025) apply multi-turn RL to reduce persona inconsistency by over 55%, demonstrating that off-the-shelf LLMs drift from assigned personas across conversation turns. A growing body of work, however, documents fundamental limitations of persona and role prompting. Basil et al. (2025) find that expert personas *degrade* factual accuracy—MMLU drops from 71.6% to 66.3% with detailed persona instructions—because persona prompting activates instruction-following mode at the expense of factual recall. Hu et al. (2026) systematically confirm this trade-off, reporting accuracy degradation of up to 30 percentage points, with more instruction-tuned models being more susceptible. Li et al. (2025) show that LLM-generated personas drift toward socially desirable traits, introducing bias at the persona creation step itself. Our work extends these findings to a previously unstudied setting: multi-turn agent dialogue with tool-calling requirements, where we find that prompt-based behavioral calibration (BCP) triggers a more severe failure—global suppression of task completion—because the model must simultaneously follow calibration instructions and execute structured tool calls.\n\n## 2.3 Preference Optimization for Bias Mitigation\n\nDirect Preference Optimization (Rafailov et al., 2023) offers a computationally lightweight alternative to PPO-based RLHF by directly optimizing policy from preference pairs without an explicit reward model, and has been widely adopted for alignment tasks (Wang et al., 2024). Recent work applies preference optimization to bias mitigation: Khan (2026) proposes decoding-time debiasing via Process Reward Models, achieving bias score improvements of up to +0.40 without weight changes—a complementary inference-time approach to our training-time DPO strategy. However, DPO's alignment mechanism has known fragility. Lee et al. (2024) provide mechanistic evidence that DPO *bypasses* rather than *removes* pre-training capabilities—toxic behavior can be recovered through simple un-alignment with minimal parameter changes. Paraschou et al. (2026) document a related phenomenon: targeted debiasing on one social dimension causes unintended *bias spillover* on other dimensions, indicating that multi-attribute fairness dynamics must be considered jointly. Our work reveals a failure mode at the intersection of these concerns: when DPO-aligned models are combined with BCP prompting, the calibration direction *reverses*—an interaction effect not predictable from studying either method in isolation.\n\n## 2.4 Dialect and Sociolinguistic Bias in NLP\n\nAAVE and Indian English represent two well-studied but underserved varieties in NLP. Rickford (1999) provides the authoritative description of AAVE phonological and pragmatic features, while Kachru and Smith (2008) document Indian English politeness strategies rooted in distinct face-saving norms. Joshi et al. (2025) survey NLP for dialects comprehensively, noting systematic performance degradation on dialectal data across both NLU and NLG tasks. Several benchmarks quantify these disparities: Faisal et al. (2024) cover 281 language varieties across 10 NLP tasks in DialectBench; Lin et al. (2025) introduce ReDial, the first human-annotated SE–AAVE parallel benchmark, finding that LLMs struggle more with AAVE than with misspelled Standard English; and Gupta et al. (2025) present EnDive, a cross-dialect benchmark covering both our target dialects (AAVE and Indian English) across understanding, reasoning, and math tasks. Haq and Saldias (2026) demonstrate that dialect cues alone trigger differential LLM behavior—a \"dialect jailbreak\" reducing refusal probability to near zero—establishing that bias operates through implicit linguistic signals, not just explicit identity markers. Gallegos et al. (2024) provide a comprehensive taxonomy of bias metrics and mitigation methods across the LLM pipeline. Critically, existing work evaluates dialect bias in classification, QA, and reasoning tasks. No prior study measures *behavioral rate disparities* (e.g., question-asking frequency, politeness levels) in multi-turn agent dialogue, nor documents what happens when calibration methods are applied to correct such disparities.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2abdebbe-f3bd-4182-bff6-4d04fba6ecf2",
  "uuid": "7fb2d8b8-09fb-4773-8288-5ab232df4898",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ViXiBLimRpitsUvW3MsBMd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1549,
      "cache_read_input_tokens": 37674,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1549
      },
      "output_tokens": 24,
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

_source line 18 · 2026-05-13T08:21:08.272Z_

<details><summary>↩ Tool result · `toolu_01TDz8HV4GUtBQQeYirw8qCm`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/artifacts/section_related_work_draft.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2abdebbe-f3bd-4182-bff6-4d04fba6ecf2",
  "uuid": "b3f4b39a-ab1d-4e1c-86a8-e828c006d6a7",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/artifacts/section_related_work_draft.md",
    "content": "# 2 Related Work\n\n## 2.1 LLM-Based User Simulation for Agent Evaluation\n\nLLM-based user simulators have become central to evaluating tool-calling agents. Yao et al. (2024) introduce τ-bench, a benchmark pairing an LLM user simulator with a tool-calling agent in retail and airline domains, and propose the pass^k reliability metric. Liu et al. (2024) and Wang et al. (2024) establish complementary multi-environment and multi-turn evaluation paradigms, though neither incorporates demographic variation in their simulated users. Naous et al. (2025) demonstrate that purpose-built User LMs outperform repurposed assistant models, with GPT-4o success rates dropping from 74.6% to 57.4% under realistic simulation. Sekulić et al. (2024) show that domain-aware fine-tuning improves user goal fulfillment, while Ahmad et al. (2025) generate diverse user profiles with varied demographics and conversational styles. Nakash et al. (2026) address evaluation efficiency through diversity-guided branching trajectories. Most critically, Zhou et al. (2026) conduct the first full τ-bench evaluation with 451 real humans, finding that LLM simulators are excessively cooperative and stylistically uniform, inflating agent success rates. Seshadri et al. (2026) further document that AAVE and Indian English speakers experience the worst calibration errors. However, none of these works attempt to *correct* the identified sim-to-real gaps through behavioral calibration—they diagnose without prescribing, leaving open whether calibration methods can close the fidelity gaps they identify.\n\n## 2.2 Behavioral Calibration of Language Models\n\nPrompt-based calibration has a rich history: Zhao et al. (2021) show that contextual calibration of output distributions can improve few-shot accuracy by up to 30%, but their method targets classification biases, not behavioral rates in generation. In multi-turn settings, Abdulhai et al. (2025) apply multi-turn RL to reduce persona inconsistency by over 55%, demonstrating that off-the-shelf LLMs drift from assigned personas across conversation turns. A growing body of work, however, documents fundamental limitations of persona and role prompting. Basil et al. (2025) find that expert personas *degrade* factual accuracy—MMLU drops from 71.6% to 66.3% with detailed persona instructions—because persona prompting activates instruction-following mode at the expense of factual recall. Hu et al. (2026) systematically confirm this trade-off, reporting accuracy degradation of up to 30 percentage points, with more instruction-tuned models being more susceptible. Li et al. (2025) show that LLM-generated personas drift toward socially desirable traits, introducing bias at the persona creation step itself. Our work extends these findings to a previously unstudied setting: multi-turn agent dialogue with tool-calling requirements, where we find that prompt-based behavioral calibration (BCP) triggers a more severe failure—global suppression of task completion—because the model must simultaneously follow calibration instructions and execute structured tool calls.\n\n## 2.3 Preference Optimization for Bias Mitigation\n\nDirect Preference Optimization (Rafailov et al., 2023) offers a computationally lightweight alternative to PPO-based RLHF by directly optimizing policy from preference pairs without an explicit reward model, and has been widely adopted for alignment tasks (Wang et al., 2024). Recent work applies preference optimization to bias mitigation: Khan (2026) proposes decoding-time debiasing via Process Reward Models, achieving bias score improvements of up to +0.40 without weight changes—a complementary inference-time approach to our training-time DPO strategy. However, DPO's alignment mechanism has known fragility. Lee et al. (2024) provide mechanistic evidence that DPO *bypasses* rather than *removes* pre-training capabilities—toxic behavior can be recovered through simple un-alignment with minimal parameter changes. Paraschou et al. (2026) document a related phenomenon: targeted debiasing on one social dimension causes unintended *bias spillover* on other dimensions, indicating that multi-attribute fairness dynamics must be considered jointly. Our work reveals a failure mode at the intersection of these concerns: when DPO-aligned models are combined with BCP prompting, the calibration direction *reverses*—an interaction effect not predictable from studying either method in isolation.\n\n## 2.4 Dialect and Sociolinguistic Bias in NLP\n\nAAVE and Indian English represent two well-studied but underserved varieties in NLP. Rickford (1999) provides the authoritative description of AAVE phonological and pragmatic features, while Kachru and Smith (2008) document Indian English politeness strategies rooted in distinct face-saving norms. Joshi et al. (2025) survey NLP for dialects comprehensively, noting systematic performance degradation on dialectal data across both NLU and NLG tasks. Several benchmarks quantify these disparities: Faisal et al. (2024) cover 281 language varieties across 10 NLP tasks in DialectBench; Lin et al. (2025) introduce ReDial, the first human-annotated SE–AAVE parallel benchmark, finding that LLMs struggle more with AAVE than with misspelled Standard English; and Gupta et al. (2025) present EnDive, a cross-dialect benchmark covering both our target dialects (AAVE and Indian English) across understanding, reasoning, and math tasks. Haq and Saldias (2026) demonstrate that dialect cues alone trigger differential LLM behavior—a \"dialect jailbreak\" reducing refusal probability to near zero—establishing that bias operates through implicit linguistic signals, not just explicit identity markers. Gallegos et al. (2024) provide a comprehensive taxonomy of bias metrics and mitigation methods across the LLM pipeline. Critically, existing work evaluates dialect bias in classification, QA, and reasoning tasks. No prior study measures *behavioral rate disparities* (e.g., question-asking frequency, politeness levels) in multi-turn agent dialogue, nor documents what happens when calibration methods are applied to correct such disparities.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01GAiK22o7dLAAmQ71ZkHknS`</summary>

```json
{
  "name": "section_related_work_draft",
  "type": "paper",
  "description": "Related Work section draft (4 subsections: user simulation, behavioral calibration, preference optimization, dialect bias) for Plan B EMNLP 2026 paper",
  "project": "cost-verify-agent-rl",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/artifacts/section_related_work_draft.md",
  "tags": [
    "paper",
    "related-work",
    "plan-b",
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
  "session_id": "2abdebbe-f3bd-4182-bff6-4d04fba6ecf2",
  "uuid": "cf162d54-2f59-4aac-af96-b473382e93de",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015V3XrUJ6TvKUvePMUms4VF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1961,
      "cache_read_input_tokens": 39223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1961
      },
      "output_tokens": 63,
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

_source line 20 · 2026-05-13T08:21:15.195Z_

<details><summary>↩ Tool result · `toolu_01GAiK22o7dLAAmQ71ZkHknS`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260513_4cc139\", \"name\": \"section_related_work_draft\", \"type\": \"paper\", \"description\": \"Related Work section draft (4 subsections: user simulation, behavioral calibration, preference optimization, dialect bias) for Plan B EMNLP 2026 paper\", \"path\": \"projects/cost-verify-agent-rl/artifacts/_project/paper/section_related_work_draft.md\", \"url\": null, \"project\": \"cost-verify-agent-rl\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-13T08:21:15.160787+00:00\", \"tags\": [\"paper\", \"related-work\", \"plan-b\", \"emnlp2026\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2abdebbe-f3bd-4182-bff6-4d04fba6ecf2",
  "uuid": "94cd40ac-eac8-4722-bb03-12439dd51478",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260513_4cc139\\\", \\\"name\\\": \\\"section_related_work_draft\\\", \\\"type\\\": \\\"paper\\\", \\\"description\\\": \\\"Related Work section draft (4 subsections: user simulation, behavioral calibration, preference optimization, dialect bias) for Plan B EMNLP 2026 paper\\\", \\\"path\\\": \\\"projects/cost-verify-agent-rl/artifacts/_project/paper/section_related_work_draft.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"cost-verify-agent-rl\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-13T08:21:15.160787+00:00\\\", \\\"tags\\\": [\\\"paper\\\", \\\"related-work\\\", \\\"plan-b\\\", \\\"emnlp2026\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260513_4cc139\", \"name\": \"section_related_work_draft\", \"type\": \"paper\", \"description\": \"Related Work section draft (4 subsections: user simulation, behavioral calibration, preference optimization, dialect bias) for Plan B EMNLP 2026 paper\", \"path\": \"projects/cost-verify-agent-rl/artifacts/_project/paper/section_related_work_draft.md\", \"url\": null, \"project\": \"cost-verify-agent-rl\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-13T08:21:15.160787+00:00\", \"tags\": [\"paper\", \"related-work\", \"plan-b\", \"emnlp2026\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 21_

已写入 `artifacts/section_related_work_draft.md` 并注册。

**覆盖情况**：
- §2.1 引用 8 篇（yao2024taubench, liu2024agentbench, wang2024mint, naous2025flipping, sekulic2024daus, ahmad2025diversity, nakash2026divert, sim2real2026gap, seshadri2026lost）
- §2.2 引用 6 篇（zhao2021calibrate, abdulhai2025consistent, basil2025playing_pretend, hu2026expert_persona, li2025persona）— gap 指向 BCP 在 agent dialogue 中的 completion collapse
- §2.3 引用 5 篇（rafailov2023dpo, wang2024alignment, khan2026decoding, lee2024dpo_toxicity, gupta2026intra_fairness）— gap 指向 DPO+BCP 交互反转
- §2.4 引用 8 篇（rickford1999aave, kachru2008cultures, joshi2025dialect_survey, faisal2024dialectbench, lin2025redial, gupta2025endive, haq2026dialect, gallegos2024bias）— gap 指向无人测量 agent dialogue 中的行为率偏差

28 篇文献中引用 25 篇（未用：parrish2022bbq 低相关性，wang2024alignment 在 §2.3 已用作 survey reference，abdulhai 放在了 §2.2）。每节末尾均以 novelty gap 收尾。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2abdebbe-f3bd-4182-bff6-4d04fba6ecf2",
  "uuid": "3c4fe9f9-dbbc-48d7-9c85-01327a14dd34",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GuBPn2FY7x5WbKjGHY1S44",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 554,
      "cache_read_input_tokens": 41184,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 554
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

_source line 22_

已写入 `artifacts/section_related_work_draft.md` 并注册。

**覆盖情况**：
- §2.1 引用 8 篇（yao2024taubench, liu2024agentbench, wang2024mint, naous2025flipping, sekulic2024daus, ahmad2025diversity, nakash2026divert, sim2real2026gap, seshadri2026lost）
- §2.2 引用 6 篇（zhao2021calibrate, abdulhai2025consistent, basil2025playing_pretend, hu2026expert_persona, li2025persona）— gap 指向 BCP 在 agent dialogue 中的 completion collapse
- §2.3 引用 5 篇（rafailov2023dpo, wang2024alignment, khan2026decoding, lee2024dpo_toxicity, gupta2026intra_fairness）— gap 指向 DPO+BCP 交互反转
- §2.4 引用 8 篇（rickford1999aave, kachru2008cultures, joshi2025dialect_survey, faisal2024dialectbench, lin2025redial, gupta2025endive, haq2026dialect, gallegos2024bias）— gap 指向无人测量 agent dialogue 中的行为率偏差

28 篇文献中引用 25 篇（未用：parrish2022bbq 低相关性，wang2024alignment 在 §2.3 已用作 survey reference，abdulhai 放在了 §2.2）。每节末尾均以 novelty gap 收尾。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 86416,
  "duration_api_ms": 87418,
  "num_turns": 7,
  "stop_reason": "end_turn",
  "session_id": "2abdebbe-f3bd-4182-bff6-4d04fba6ecf2",
  "total_cost_usd": 0.36699475000000004,
  "usage": {
    "input_tokens": 11,
    "cache_creation_input_tokens": 29897,
    "cache_read_input_tokens": 177489,
    "output_tokens": 3589,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 29897,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 423,
        "cache_read_input_tokens": 41184,
        "cache_creation_input_tokens": 554,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 554
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1534,
      "outputTokens": 16,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001614,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 11,
      "outputTokens": 3589,
      "cacheReadInputTokens": 177489,
      "cacheCreationInputTokens": 29897,
      "webSearchRequests": 0,
      "costUSD": 0.36538075000000003,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "b3f9b0cb-1609-483e-ba74-0591e627141f"
}
```

</details>

---
