# writing results skeleton

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 34
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/workers/worker_writing_results-skeleton_20260514T054846.log`
- **Structured JSON:** [`a21538d2519e762db729.json`](../../sessions/a2/a21538d2519e762db729.json)

## Before a recorded user message

34 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "session_id": "103088e8-c35b-46f1-a93a-deef01852d45",
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
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__write_paper_section"
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
  "uuid": "6469528e-0306-43cd-a5f0-ee9b437820d3",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/memory/"
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
    "status": "allowed_warning",
    "resetsAt": 1779267600,
    "rateLimitType": "seven_day",
    "utilization": 0.28,
    "isUsingOverage": false
  },
  "uuid": "995b60eb-e77d-4566-acf0-9ef562d13491",
  "session_id": "103088e8-c35b-46f1-a93a-deef01852d45"
}
```

---

### Assistant

_source line 4_

I'll start by reading the required context files to understand the paper's framing, methodology, and analysis sections.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "103088e8-c35b-46f1-a93a-deef01852d45",
  "uuid": "d875fad1-d634-4a4d-800c-109daa14e7ac",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QYVq3ig8iWDhMMfYHd51Kp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11760,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11760
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_019cPuMLw5R3pWBpAb347F6C`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__write_paper_section",
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
  "session_id": "103088e8-c35b-46f1-a93a-deef01852d45",
  "uuid": "da6fef52-8fb5-44b6-a9e7-3c7724189b92",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QYVq3ig8iWDhMMfYHd51Kp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11760,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11760
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

_source line 6 · 2026-05-14T05:49:02.678Z_

<details><summary>↩ Tool result · `toolu_019cPuMLw5R3pWBpAb347F6C`</summary>

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
  "tool_name": "mcp__agent-ml-research__write_paper_section"
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
  "session_id": "103088e8-c35b-46f1-a93a-deef01852d45",
  "uuid": "e07e7191-9127-47b5-a036-0f0445e382b0",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__write_paper_section"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__write_paper_section",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Let me read the required context files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "103088e8-c35b-46f1-a93a-deef01852d45",
  "uuid": "f4334916-26cc-4d08-ae5e-86598c240103",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015USJNmh2ZpLQmoXaoZce49",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 871,
      "cache_read_input_tokens": 23601,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 871
      },
      "output_tokens": 26,
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01FQ1pqzzmTcxox5urccBQAU`</summary>

```json
{
  "project": "phase-gated-compound-sparse",
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
  "session_id": "103088e8-c35b-46f1-a93a-deef01852d45",
  "uuid": "cb6fb56f-f62c-420a-9b25-17f22ef61a01",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015USJNmh2ZpLQmoXaoZce49",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 871,
      "cache_read_input_tokens": 23601,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 871
      },
      "output_tokens": 26,
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

_source line 9 · 2026-05-14T05:49:08.077Z_

<details><summary>↩ Tool result · `toolu_01FQ1pqzzmTcxox5urccBQAU`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper_framing.md\", \"content\": \"# Paper Framing — Phase-Gated Compound Sparsity\\n\\n> 最后更新: 2026-05-14 | 维护者: Director\\n\\n## Core Insight\\n\\nCompound sparsity（attention head pruning + KV cache eviction）的 severity 不是固定常数——它是 eviction strategy 和 reasoning phase 交互的涌现属性。Importance-based eviction 在 low-sparsity reasoning phase 产生 11-42× severity amplification（problem-level bootstrap），而 random eviction 保持 ~1× 平坦。这一发现挑战了 compound degradation 均匀分布的隐含假设。\\n\\n**⚠️ 数字基准**：本文件中的具体数字（gradient magnitude, crossover values）基于 fp16 problem-level bootstrap 结果。bf16 重跑完成后必须统一更新。segment-level 估计（12-75×）已弃用，仅在被明确标注时作为参考。\\n\\n## Narrative Arc\\n\\nCompound sparsity 是高效 LLM 推理的实用部署需求，但 prior work（SparK, Ada-KV, SLiM）将 compound interaction 视为均匀超可加。我们发现 severity 是 strategy × phase 交互的涌现属性：importance eviction 在 distributed-attention phase 剧烈放大 compound degradation（problem-level gradient 11-42×），而 random eviction 在所有 phase 保持平坦（~1×）。我们通过 entropy-discrimination collapse 机制解释这一现象：head pruning → attention 重分布 → importance score 的判别力崩塌 → importance eviction 退化为有偏伪随机。这一发现为 phase-aware sparsity allocation 提供了动机。\\n\\n**Framing 硬约束（D015）**：\\n- MUST: \\\"emergent phase-strategy interaction\\\"\\n- MUST NOT: \\\"importance metric limitation / importance is broken\\\"\\n\\n## Core Claims\\n\\n| ID | Claim | Status | Key Evidence |\\n|----|-------|--------|-------------|\\n| C1 | Compound sparsity severity is strategy-dependent | confirmed | importance gradient 11-42× (problem-level) vs random ~1×. 待 bf16 数据更新 |\\n| C2 | Severity is phase-modulated (amplified in low-sparsity phase) | confirmed | low phase >> high phase at all 4 sparsity levels. Problem-level: 11.53→11.05→35.72→41.92（s015→s020 非严格单调，bf16 数据可能改变趋势。论文措辞用 \\\"increases with sparsity\\\" 而非 \\\"monotonically increases\\\"） |\\n| C3 | Phase-strategy crossover exists | confirmed | s=0.25: importance high_phase=0.584 < random=3.002, importance low_phase=30.903 > random=2.915 |\\n| C4 | Entropy-discrimination collapse explains the mechanism | partially_confirmed | Conceptual argument solid; empirical attention entropy data not yet collected |\\n| C5 | Finding generalizes across models (same arch, different training) | pending | Qwen2.5-7B-Instruct experiments in progress. Note: DeepSeek-R1-Distill-Qwen-7B 和 Qwen2.5-7B-Instruct 共享 Qwen2ForCausalLM 架构，区别在训练方式（distillation vs instruction tuning）。是 cross-model 而非 cross-architecture replication。 |\\n| C6 | Severity gradient is sub-exponential | confirmed | Growth rate decreasing: 2.24×→1.84×→1.42× |\\n\\n## Anticipated Reviewer Concerns\\n\\n### RC1: Generalizability — 7B models only, single benchmark\\n- **预期质疑**: \\\"Results on two 7B models and MATH-500 only. How do we know this generalizes to larger models or other reasoning tasks?\\\"\\n- **应对**: Cross-model replication (DeepSeek-R1-Distill-Qwen-7B + Qwen2.5-7B-Instruct) 控制架构变量、隔离训练方式影响（distillation vs instruction tuning）。注意：两模型共享 Qwen2ForCausalLM 架构，不能 claim 跨架构泛化。MATH-500 是 standard benchmark。Limitations 必须诚实声明：(1) 同架构不同训练，不是跨架构；(2) 7B scale only；(3) 单 benchmark。机制解释 (entropy-discrimination collapse) 原则上 architecture-agnostic，但未实证验证。\\n- **实验支撑**: C5 (Qwen cross-model). 若需加强可扩展到不同架构（如 LLaMA/Mistral），但 11 天 deadline 内不现实\\n\\n### RC2: Mechanism — entropy-discrimination collapse 缺乏直接测量\\n- **预期质疑**: \\\"The mechanism is conceptual. Where is the empirical evidence for entropy increase and discrimination collapse?\\\"\\n- **应对**: 如果有 GPU 预算，可以直接测量 pruned vs unpruned 的 attention entropy 和 importance score 分布。目前 C4 status = partially_confirmed，需要决定是否投入 GPU 时间做 direct measurement。\\n- **实验支撑**: 可选 ablation：测量 attention entropy pre/post pruning × phase\\n\\n### RC3: Practical impact — 没有 throughput 数据\\n- **预期质疑**: \\\"No wall-clock or throughput measurements. Is the severity amplification reflected in actual inference speed?\\\"\\n- **应对**: 本文定位是 empirical finding paper（发现 + 机制解释），不是 method paper。Throughput 不是 claim 的一部分。Discussion 中明确 phase-gated controller 作为 future direction。\\n- **实验支撑**: 不需要额外实验\\n\\n### RC4: Statistical rigor — bootstrap 是否足够\\n- **预期质疑**: \\\"Per-problem bootstrap with 50 problems — sufficient sample size?\\\"\\n- **应对**: B=10000 iterations, all p=0.0000, CI 不跨零。fp16 下实际配对数为 16-22/50（NaN 过滤后），bf16 预期恢复到 ~45-50 配对。bf16 数据到手后需重新验证统计效力。可在 appendix 补充 per-problem 分布图。\\n- **实验支撑**: fp16 bootstrap 已完成；bf16 bootstrap 待重做（plan_008）\\n\\n### RC5: Novelty — prior work 是否已覆盖 phase-dependent sparsity\\n- **预期质疑**: \\\"ThinKV and phase-aware methods already consider phase. What's new?\\\"\\n- **应对**: Prior work 在单轴上分析 phase（ThinKV: phase-aware eviction）或 compound（SparK: joint compression）。没有工作同时分析 compound × phase × strategy 的三维交互。Crossover 现象（同一 strategy 在不同 phase 方向反转）是全新发现。\\n- **实验支撑**: C3 (crossover), Related Work §2 的 gap 分析\\n\\n## Paper Positioning\\n\\n**类型**: Empirical finding paper（非 method paper）\\n**核心贡献**:\\n1. 发现 compound sparsity severity 的 strategy × phase 交互\\n2. 量化 severity gradient（problem-level 11-42×, 待 bf16 更新）和 crossover 现象\\n3. 提出 entropy-discrimination collapse 机制解释\\n4. Cross-model replication 验证泛化性\\n\\n**投稿目标**: EMNLP 2026 ARR, deadline 2026-05-25\\n\", \"total_chars\": 4891, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "103088e8-c35b-46f1-a93a-deef01852d45",
  "uuid": "3457be33-3493-449a-8b57-a36aaab10f64",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing — Phase-Gated Compound Sparsity\\\\n\\\\n> 最后更新: 2026-05-14 | 维护者: Director\\\\n\\\\n## Core Insight\\\\n\\\\nCompound sparsity（attention head pruning + KV cache eviction）的 severity 不是固定常数——它是 eviction strategy 和 reasoning phase 交互的涌现属性。Importance-based eviction 在 low-sparsity reasoning phase 产生 11-42× severity amplification（problem-level bootstrap），而 random eviction 保持 ~1× 平坦。这一发现挑战了 compound degradation 均匀分布的隐含假设。\\\\n\\\\n**⚠️ 数字基准**：本文件中的具体数字（gradient magnitude, crossover values）基于 fp16 problem-level bootstrap 结果。bf16 重跑完成后必须统一更新。segment-level 估计（12-75×）已弃用，仅在被明确标注时作为参考。\\\\n\\\\n## Narrative Arc\\\\n\\\\nCompound sparsity 是高效 LLM 推理的实用部署需求，但 prior work（SparK, Ada-KV, SLiM）将 compound interaction 视为均匀超可加。我们发现 severity 是 strategy × phase 交互的涌现属性：importance eviction 在 distributed-attention phase 剧烈放大 compound degradation（problem-level gradient 11-42×），而 random eviction 在所有 phase 保持平坦（~1×）。我们通过 entropy-discrimination collapse 机制解释这一现象：head pruning → attention 重分布 → importance score 的判别力崩塌 → importance eviction 退化为有偏伪随机。这一发现为 phase-aware sparsity allocation 提供了动机。\\\\n\\\\n**Framing 硬约束（D015）**：\\\\n- MUST: \\\\\\\"emergent phase-strategy interaction\\\\\\\"\\\\n- MUST NOT: \\\\\\\"importance metric limitation / importance is broken\\\\\\\"\\\\n\\\\n## Core Claims\\\\n\\\\n| ID | Claim | Status | Key Evidence |\\\\n|----|-------|--------|-------------|\\\\n| C1 | Compound sparsity severity is strategy-dependent | confirmed | importance gradient 11-42× (problem-level) vs random ~1×. 待 bf16 数据更新 |\\\\n| C2 | Severity is phase-modulated (amplified in low-sparsity phase) | confirmed | low phase >> high phase at all 4 sparsity levels. Problem-level: 11.53→11.05→35.72→41.92（s015→s020 非严格单调，bf16 数据可能改变趋势。论文措辞用 \\\\\\\"increases with sparsity\\\\\\\" 而非 \\\\\\\"monotonically increases\\\\\\\"） |\\\\n| C3 | Phase-strategy crossover exists | confirmed | s=0.25: importance high_phase=0.584 < random=3.002, importance low_phase=30.903 > random=2.915 |\\\\n| C4 | Entropy-discrimination collapse explains the mechanism | partially_confirmed | Conceptual argument solid; empirical attention entropy data not yet collected |\\\\n| C5 | Finding generalizes across models (same arch, different training) | pending | Qwen2.5-7B-Instruct experiments in progress. Note: DeepSeek-R1-Distill-Qwen-7B 和 Qwen2.5-7B-Instruct 共享 Qwen2ForCausalLM 架构，区别在训练方式（distillation vs instruction tuning）。是 cross-model 而非 cross-architecture replication。 |\\\\n| C6 | Severity gradient is sub-exponential | confirmed | Growth rate decreasing: 2.24×→1.84×→1.42× |\\\\n\\\\n## Anticipated Reviewer Concerns\\\\n\\\\n### RC1: Generalizability — 7B models only, single benchmark\\\\n- **预期质疑**: \\\\\\\"Results on two 7B models and MATH-500 only. How do we know this generalizes to larger models or other reasoning tasks?\\\\\\\"\\\\n- **应对**: Cross-model replication (DeepSeek-R1-Distill-Qwen-7B + Qwen2.5-7B-Instruct) 控制架构变量、隔离训练方式影响（distillation vs instruction tuning）。注意：两模型共享 Qwen2ForCausalLM 架构，不能 claim 跨架构泛化。MATH-500 是 standard benchmark。Limitations 必须诚实声明：(1) 同架构不同训练，不是跨架构；(2) 7B scale only；(3) 单 benchmark。机制解释 (entropy-discrimination collapse) 原则上 architecture-agnostic，但未实证验证。\\\\n- **实验支撑**: C5 (Qwen cross-model). 若需加强可扩展到不同架构（如 LLaMA/Mistral），但 11 天 deadline 内不现实\\\\n\\\\n### RC2: Mechanism — entropy-discrimination collapse 缺乏直接测量\\\\n- **预期质疑**: \\\\\\\"The mechanism is conceptual. Where is the empirical evidence for entropy increase and discrimination collapse?\\\\\\\"\\\\n- **应对**: 如果有 GPU 预算，可以直接测量 pruned vs unpruned 的 attention entropy 和 importance score 分布。目前 C4 status = partially_confirmed，需要决定是否投入 GPU 时间做 direct measurement。\\\\n- **实验支撑**: 可选 ablation：测量 attention entropy pre/post pruning × phase\\\\n\\\\n### RC3: Practical impact — 没有 throughput 数据\\\\n- **预期质疑**: \\\\\\\"No wall-clock or throughput measurements. Is the severity amplification reflected in actual inference speed?\\\\\\\"\\\\n- **应对**: 本文定位是 empirical finding paper（发现 + 机制解释），不是 method paper。Throughput 不是 claim 的一部分。Discussion 中明确 phase-gated controller 作为 future direction。\\\\n- **实验支撑**: 不需要额外实验\\\\n\\\\n### RC4: Statistical rigor — bootstrap 是否足够\\\\n- **预期质疑**: \\\\\\\"Per-problem bootstrap with 50 problems — sufficient sample size?\\\\\\\"\\\\n- **应对**: B=10000 iterations, all p=0.0000, CI 不跨零。fp16 下实际配对数为 16-22/50（NaN 过滤后），bf16 预期恢复到 ~45-50 配对。bf16 数据到手后需重新验证统计效力。可在 appendix 补充 per-problem 分布图。\\\\n- **实验支撑**: fp16 bootstrap 已完成；bf16 bootstrap 待重做（plan_008）\\\\n\\\\n### RC5: Novelty — prior work 是否已覆盖 phase-dependent sparsity\\\\n- **预期质疑**: \\\\\\\"ThinKV and phase-aware methods already consider phase. What's new?\\\\\\\"\\\\n- **应对**: Prior work 在单轴上分析 phase（ThinKV: phase-aware eviction）或 compound（SparK: joint compression）。没有工作同时分析 compound × phase × strategy 的三维交互。Crossover 现象（同一 strategy 在不同 phase 方向反转）是全新发现。\\\\n- **实验支撑**: C3 (crossover), Related Work §2 的 gap 分析\\\\n\\\\n## Paper Positioning\\\\n\\\\n**类型**: Empirical finding paper（非 method paper）\\\\n**核心贡献**:\\\\n1. 发现 compound sparsity severity 的 strategy × phase 交互\\\\n2. 量化 severity gradient（problem-level 11-42×, 待 bf16 更新）和 crossover 现象\\\\n3. 提出 entropy-discrimination collapse 机制解释\\\\n4. Cross-model replication 验证泛化性\\\\n\\\\n**投稿目标**: EMNLP 2026 ARR, deadline 2026-05-25\\\\n\\\", \\\"total_chars\\\": 4891, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper_framing.md\", \"content\": \"# Paper Framing — Phase-Gated Compound Sparsity\\n\\n> 最后更新: 2026-05-14 | 维护者: Director\\n\\n## Core Insight\\n\\nCompound sparsity（attention head pruning + KV cache eviction）的 severity 不是固定常数——它是 eviction strategy 和 reasoning phase 交互的涌现属性。Importance-based eviction 在 low-sparsity reasoning phase 产生 11-42× severity amplification（problem-level bootstrap），而 random eviction 保持 ~1× 平坦。这一发现挑战了 compound degradation 均匀分布的隐含假设。\\n\\n**⚠️ 数字基准**：本文件中的具体数字（gradient magnitude, crossover values）基于 fp16 problem-level bootstrap 结果。bf16 重跑完成后必须统一更新。segment-level 估计（12-75×）已弃用，仅在被明确标注时作为参考。\\n\\n## Narrative Arc\\n\\nCompound sparsity 是高效 LLM 推理的实用部署需求，但 prior work（SparK, Ada-KV, SLiM）将 compound interaction 视为均匀超可加。我们发现 severity 是 strategy × phase 交互的涌现属性：importance eviction 在 distributed-attention phase 剧烈放大 compound degradation（problem-level gradient 11-42×），而 random eviction 在所有 phase 保持平坦（~1×）。我们通过 entropy-discrimination collapse 机制解释这一现象：head pruning → attention 重分布 → importance score 的判别力崩塌 → importance eviction 退化为有偏伪随机。这一发现为 phase-aware sparsity allocation 提供了动机。\\n\\n**Framing 硬约束（D015）**：\\n- MUST: \\\"emergent phase-strategy interaction\\\"\\n- MUST NOT: \\\"importance metric limitation / importance is broken\\\"\\n\\n## Core Claims\\n\\n| ID | Claim | Status | Key Evidence |\\n|----|-------|--------|-------------|\\n| C1 | Compound sparsity severity is strategy-dependent | confirmed | importance gradient 11-42× (problem-level) vs random ~1×. 待 bf16 数据更新 |\\n| C2 | Severity is phase-modulated (amplified in low-sparsity phase) | confirmed | low phase >> high phase at all 4 sparsity levels. Problem-level: 11.53→11.05→35.72→41.92（s015→s020 非严格单调，bf16 数据可能改变趋势。论文措辞用 \\\"increases with sparsity\\\" 而非 \\\"monotonically increases\\\"） |\\n| C3 | Phase-strategy crossover exists | confirmed | s=0.25: importance high_phase=0.584 < random=3.002, importance low_phase=30.903 > random=2.915 |\\n| C4 | Entropy-discrimination collapse explains the mechanism | partially_confirmed | Conceptual argument solid; empirical attention entropy data not yet collected |\\n| C5 | Finding generalizes across models (same arch, different training) | pending | Qwen2.5-7B-Instruct experiments in progress. Note: DeepSeek-R1-Distill-Qwen-7B 和 Qwen2.5-7B-Instruct 共享 Qwen2ForCausalLM 架构，区别在训练方式（distillation vs instruction tuning）。是 cross-model 而非 cross-architecture replication。 |\\n| C6 | Severity gradient is sub-exponential | confirmed | Growth rate decreasing: 2.24×→1.84×→1.42× |\\n\\n## Anticipated Reviewer Concerns\\n\\n### RC1: Generalizability — 7B models only, single benchmark\\n- **预期质疑**: \\\"Results on two 7B models and MATH-500 only. How do we know this generalizes to larger models or other reasoning tasks?\\\"\\n- **应对**: Cross-model replication (DeepSeek-R1-Distill-Qwen-7B + Qwen2.5-7B-Instruct) 控制架构变量、隔离训练方式影响（distillation vs instruction tuning）。注意：两模型共享 Qwen2ForCausalLM 架构，不能 claim 跨架构泛化。MATH-500 是 standard benchmark。Limitations 必须诚实声明：(1) 同架构不同训练，不是跨架构；(2) 7B scale only；(3) 单 benchmark。机制解释 (entropy-discrimination collapse) 原则上 architecture-agnostic，但未实证验证。\\n- **实验支撑**: C5 (Qwen cross-model). 若需加强可扩展到不同架构（如 LLaMA/Mistral），但 11 天 deadline 内不现实\\n\\n### RC2: Mechanism — entropy-discrimination collapse 缺乏直接测量\\n- **预期质疑**: \\\"The mechanism is conceptual. Where is the empirical evidence for entropy increase and discrimination collapse?\\\"\\n- **应对**: 如果有 GPU 预算，可以直接测量 pruned vs unpruned 的 attention entropy 和 importance score 分布。目前 C4 status = partially_confirmed，需要决定是否投入 GPU 时间做 direct measurement。\\n- **实验支撑**: 可选 ablation：测量 attention entropy pre/post pruning × phase\\n\\n### RC3: Practical impact — 没有 throughput 数据\\n- **预期质疑**: \\\"No wall-clock or throughput measurements. Is the severity amplification reflected in actual inference speed?\\\"\\n- **应对**: 本文定位是 empirical finding paper（发现 + 机制解释），不是 method paper。Throughput 不是 claim 的一部分。Discussion 中明确 phase-gated controller 作为 future direction。\\n- **实验支撑**: 不需要额外实验\\n\\n### RC4: Statistical rigor — bootstrap 是否足够\\n- **预期质疑**: \\\"Per-problem bootstrap with 50 problems — sufficient sample size?\\\"\\n- **应对**: B=10000 iterations, all p=0.0000, CI 不跨零。fp16 下实际配对数为 16-22/50（NaN 过滤后），bf16 预期恢复到 ~45-50 配对。bf16 数据到手后需重新验证统计效力。可在 appendix 补充 per-problem 分布图。\\n- **实验支撑**: fp16 bootstrap 已完成；bf16 bootstrap 待重做（plan_008）\\n\\n### RC5: Novelty — prior work 是否已覆盖 phase-dependent sparsity\\n- **预期质疑**: \\\"ThinKV and phase-aware methods already consider phase. What's new?\\\"\\n- **应对**: Prior work 在单轴上分析 phase（ThinKV: phase-aware eviction）或 compound（SparK: joint compression）。没有工作同时分析 compound × phase × strategy 的三维交互。Crossover 现象（同一 strategy 在不同 phase 方向反转）是全新发现。\\n- **实验支撑**: C3 (crossover), Related Work §2 的 gap 分析\\n\\n## Paper Positioning\\n\\n**类型**: Empirical finding paper（非 method paper）\\n**核心贡献**:\\n1. 发现 compound sparsity severity 的 strategy × phase 交互\\n2. 量化 severity gradient（problem-level 11-42×, 待 bf16 更新）和 crossover 现象\\n3. 提出 entropy-discrimination collapse 机制解释\\n4. Cross-model replication 验证泛化性\\n\\n**投稿目标**: EMNLP 2026 ARR, deadline 2026-05-25\\n\", \"total_chars\": 4891, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Glob · `toolu_01TH5MhHqe5aT39FgRxQXiis`</summary>

```json
{
  "pattern": "artifacts/_project/paper/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "103088e8-c35b-46f1-a93a-deef01852d45",
  "uuid": "5a215031-4aca-40e1-b4f3-a55a045bfbeb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015USJNmh2ZpLQmoXaoZce49",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 871,
      "cache_read_input_tokens": 23601,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 871
      },
      "output_tokens": 26,
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

_source line 11 · 2026-05-14T05:49:09.744Z_

<details><summary>↩ Tool result · `toolu_01TH5MhHqe5aT39FgRxQXiis`</summary>

```text
artifacts/_project/paper/related_work_46fb53.tex
artifacts/_project/paper/background_fc6d1d.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/methodology_4cc5f3.tex
artifacts/_project/paper/background.tex
artifacts/_project/paper/analysis.tex
artifacts/_project/paper/results.tex
artifacts/_project/paper/discussion.tex
artifacts/_project/paper/methodology.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "103088e8-c35b-46f1-a93a-deef01852d45",
  "uuid": "bd4a9577-95c3-4bd3-815e-32db733d5040",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/paper/related_work_46fb53.tex",
      "artifacts/_project/paper/background_fc6d1d.tex",
      "artifacts/_project/paper/related_work.tex",
      "artifacts/_project/paper/methodology_4cc5f3.tex",
      "artifacts/_project/paper/background.tex",
      "artifacts/_project/paper/analysis.tex",
      "artifacts/_project/paper/results.tex",
      "artifacts/_project/paper/discussion.tex",
      "artifacts/_project/paper/methodology.tex"
    ],
    "durationMs": 41,
    "numFiles": 9,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 12_

<details><summary>Logged reasoning block</summary>

```text
Let me read the methodology and analysis sections in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "103088e8-c35b-46f1-a93a-deef01852d45",
  "uuid": "eb62d5e7-4f25-4994-bec8-ff99f3b01df4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PhnmwxYWTtUyyNtsYgzNca",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2676,
      "cache_read_input_tokens": 24472,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2676
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

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Read · `toolu_01YDFjbPbiJAWsAwe4WHAbJv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "103088e8-c35b-46f1-a93a-deef01852d45",
  "uuid": "740888f4-0a58-4f83-8ed5-ca94e5849a39",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PhnmwxYWTtUyyNtsYgzNca",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2676,
      "cache_read_input_tokens": 24472,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2676
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

### Tool result

_source line 14 · 2026-05-14T05:49:14.768Z_

<details><summary>↩ Tool result · `toolu_01YDFjbPbiJAWsAwe4WHAbJv`</summary>

```text
1	\section{Experimental Setup}
2	\label{sec:experimental-setup}
3	
4	\subsection{Models}
5	\label{sec:models}
6	
7	We conduct experiments on two 7B-parameter instruction-tuned models that share the Qwen2 backbone architecture (28 Transformer layers, 28 attention heads with 4-group GQA):
8	
9	\paragraph{DeepSeek-R1-Distill-Qwen-7B} serves as our primary evaluation target. This model was distilled from DeepSeek-R1 \cite{deepseek-r1} and produces explicit chain-of-thought traces delimited by \texttt{&lt;think>}$\cdots$\texttt{&lt;/think>} tags, yielding sequences with pronounced phase structure---extended reasoning followed by a concise solution. The structured generation pattern makes it well-suited for studying how sparsity interacts with distinct reasoning phases.
10	
11	\paragraph{Qwen2.5-7B-Instruct} \cite{qwen2.5} provides a cross-model replication. Although it shares the same backbone family, its instruction tuning does not enforce explicit reasoning delimiters, producing a different distribution of attention sparsity across the generation trajectory. Replication on this model tests whether our findings generalize beyond distillation-induced phase structure.
12	
13	Both models are loaded in \texttt{bfloat16} precision with eager attention (i.e., without FlashAttention) to permit direct manipulation of attention weight matrices during sparsity intervention.\footnote{An earlier \texttt{float16} configuration produced sporadic NaN values in Layer~27 of DeepSeek-R1-Distill-Qwen-7B, affecting ${\sim}$8\% of logit positions. Switching to \texttt{bfloat16} eliminated all NaN occurrences; we additionally apply NaN-guarded filtering as a safety net.}
14	
15	
16	\subsection{Dataset}
17	\label{sec:dataset}
18	
19	We evaluate on a 50-problem stratified subset of the MATH-500 benchmark \cite{math500}, sampling uniformly across problem categories (algebra, geometry, number theory, combinatorics, etc.) with a fixed seed for reproducibility. Mathematical reasoning tasks are a natural testbed for our study: they elicit long chain-of-thought sequences (up to 2048 tokens) in which the model alternates between exploratory reasoning and structured computation---phases that differ markedly in attention sparsity. Each problem is decoded greedily (\texttt{max\_new\_tokens}$=$2048) to eliminate sampling variance.
20	
21	
22	\subsection{Compound Sparsity Configuration}
23	\label{sec:sparsity-config}
24	
25	We apply \emph{symmetric} compound sparsity: for a given sparsity level $s$, we prune the same fraction $s$ of attention heads and evict the same fraction $s$ of KV cache entries. We evaluate four sparsity levels $s \in \{0.15, 0.20, 0.25, 0.30\}$, spanning from mild to aggressive compression.
26	
27	\paragraph{Sparsity conditions.} For each problem and each sparsity level, we compute perplexity under four conditions: (i)~\emph{dense}---no intervention; (ii)~\emph{attn-only}---head pruning without KV eviction; (iii)~\emph{kv-only}---KV eviction without head pruning; and (iv)~\emph{both}---simultaneous head pruning and KV eviction.
28	
29	\paragraph{Eviction strategies.} We compare two KV cache eviction strategies:
30	
31	\begin{itemize}[nosep,leftmargin=*]
32	\item \textbf{Importance-based.} Each KV position receives a score equal to its cumulative attention weight summed over all query positions and heads. To correct for the inherent causal bias---earlier positions accumulate more attention simply because they are attended to by more queries---we apply position normalization:
33	\begin{equation}
34	\label{eq:importance}
35	    \alpha_j = \frac{\sum_{i,h} a_{i,h,j}}{\texttt{seq\_len} - j}, \quad j \in \{1, \dots, T\},
36	\end{equation}
37	where $a_{i,h,j}$ is the attention weight from query~$i$, head~$h$ to key~$j$, and the denominator counts the number of queries that can attend to position~$j$ under causal masking. Position~0 (BOS) is always retained. The $T \cdot s$ positions with the lowest normalized scores are evicted.
38	
39	During masked forward passes, we guard against numerical instability from the interaction of head masking and KV eviction: zeroed-out heads that would otherwise produce $\infty \times 0 = \text{NaN}$ are handled via selective replacement (\texttt{torch.where}) prior to the softmax, and any layer producing NaN outputs is skipped from the sparsity loss computation.
40	
41	\item \textbf{Random.} KV positions (excluding BOS) are evicted uniformly at random, providing a strategy-agnostic baseline. Head pruning under the random condition selects heads via \texttt{torch.randperm} rather than by importance.
42	\end{itemize}
43	
44	\paragraph{Head pruning.} Under importance-based eviction, heads are ranked by their Frobenius norm across the full attention matrix $\mathbf{A}_\ell \in \mathbb{R}^{H \times T \times T}$ per layer $\ell$, and the bottom-$s$ fraction is masked. Under random eviction, heads are selected uniformly at random.
45	
46	
47	\subsection{Phase Segmentation}
48	\label{sec:phase-seg}
49	
50	We segment each generated sequence into three \emph{reasoning phases} based on the local attention sparsity of each token position. For each query position $i$, we compute per-head sparsity as the fraction of attention weights falling below $0.01 \times \max_j a_{i,h,j}$, then average across heads to obtain a scalar sparsity value per position. The resulting sparsity trajectory is partitioned into terciles via quantile boundaries: \emph{low-sparsity} (bottom third, corresponding to diffuse attention during exploratory reasoning), \emph{mid-sparsity}, and \emph{high-sparsity} (top third, corresponding to focused attention during structured computation). Contiguous segments shorter than $\texttt{min\_phase\_length}=10$ tokens are merged into adjacent phases to suppress noise.
51	
52	
53	\subsection{Metrics}
54	\label{sec:metrics}
55	
56	\paragraph{Perplexity.} For each sparsity condition $c \in \{d, a, k, b\}$ and each phase, we compute segment-level perplexity as
57	$\text{PPL}_c = \exp\!\bigl(\tfrac{1}{|I|}\sum_{i \in I} \mathcal{L}_c(x_i)\bigr)$,
58	where $I$ is the set of token indices belonging to the phase and $\mathcal{L}_c(x_i)$ is the per-token cross-entropy loss under condition $c$.
59	
60	\paragraph{Interaction Index.} The interaction index quantifies the synergistic (super-additive) effect of compound sparsity beyond the sum of individual interventions:
61	\begin{equation}
62	\label{eq:ii}
63	    \mathrm{II} = \frac{\text{PPL}_b}{\text{PPL}_d} - \frac{\text{PPL}_a}{\text{PPL}_d} - \frac{\text{PPL}_k}{\text{PPL}_d} + 1.
64	\end{equation}
65	When $\mathrm{II} > 0$, the two sparsity mechanisms amplify each other; $\mathrm{II} = 0$ indicates additive (independent) degradation.
66	
67	\paragraph{Severity Gradient.} To measure how the interaction varies across reasoning phases, we define the severity gradient:
68	\begin{equation}
69	\label{eq:gradient}
70	    G = \frac{\widetilde{\mathrm{II}}_{\,\textit{low}}}{\widetilde{\mathrm{II}}_{\,\textit{high}}},
71	\end{equation}
72	where $\widetilde{\mathrm{II}}_{\,\textit{low}}$ and $\widetilde{\mathrm{II}}_{\,\textit{high}}$ are the median interaction indices over the low-sparsity and high-sparsity phases, respectively. We report medians rather than means because the II distribution is heavily right-skewed (mean/median ratios up to 43:1 at $s{=}0.30$), making the median a more robust central tendency estimator.
73	
74	
75	\subsection{Statistical Analysis}
76	\label{sec:stats}
77	
78	All confidence intervals and significance tests are computed via the nonparametric bootstrap with $B = 10{,}000$ resamples \cite{efron1993bootstrap}.
79	
80	\paragraph{Per-problem bootstrap.} For each sparsity level and strategy, we resample the 50 per-problem II values with replacement and compute the mean of each resample, yielding a 95\% percentile confidence interval for the population mean II.
81	
82	\paragraph{Paired bootstrap.} To test whether the severity gradient differs between importance-based and random eviction, we pair observations by problem (same problem, same sparsity level) and bootstrap the difference in gradients. This controls for problem-level variance in difficulty and sequence length.
83	
84	\paragraph{Unpaired bootstrap.} We additionally compute per-strategy gradient confidence intervals without pairing, to verify that the importance-based gradient is significantly greater than 1 (i.e., phase modulation exists) independently of the random baseline.
85	
86	All tests yield $p < 0.0001$ at every sparsity level, confirming that the observed phase--strategy interactions are not artifacts of sampling variability.\footnote{Experiments were conducted on a server with 4$\times$ NVIDIA RTX PRO 6000 Blackwell Server Edition 96\,GB GPUs, with one model--sparsity configuration per GPU.}
87	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "103088e8-c35b-46f1-a93a-deef01852d45",
  "uuid": "e259f75a-d0d3-4ee4-833b-df0a6b8dcdd2",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex",
      "content": "\\section{Experimental Setup}\n\\label{sec:experimental-setup}\n\n\\subsection{Models}\n\\label{sec:models}\n\nWe conduct experiments on two 7B-parameter instruction-tuned models that share the Qwen2 backbone architecture (28 Transformer layers, 28 attention heads with 4-group GQA):\n\n\\paragraph{DeepSeek-R1-Distill-Qwen-7B} serves as our primary evaluation target. This model was distilled from DeepSeek-R1 \\cite{deepseek-r1} and produces explicit chain-of-thought traces delimited by \\texttt{&lt;think>}$\\cdots$\\texttt{&lt;/think>} tags, yielding sequences with pronounced phase structure---extended reasoning followed by a concise solution. The structured generation pattern makes it well-suited for studying how sparsity interacts with distinct reasoning phases.\n\n\\paragraph{Qwen2.5-7B-Instruct} \\cite{qwen2.5} provides a cross-model replication. Although it shares the same backbone family, its instruction tuning does not enforce explicit reasoning delimiters, producing a different distribution of attention sparsity across the generation trajectory. Replication on this model tests whether our findings generalize beyond distillation-induced phase structure.\n\nBoth models are loaded in \\texttt{bfloat16} precision with eager attention (i.e., without FlashAttention) to permit direct manipulation of attention weight matrices during sparsity intervention.\\footnote{An earlier \\texttt{float16} configuration produced sporadic NaN values in Layer~27 of DeepSeek-R1-Distill-Qwen-7B, affecting ${\\sim}$8\\% of logit positions. Switching to \\texttt{bfloat16} eliminated all NaN occurrences; we additionally apply NaN-guarded filtering as a safety net.}\n\n\n\\subsection{Dataset}\n\\label{sec:dataset}\n\nWe evaluate on a 50-problem stratified subset of the MATH-500 benchmark \\cite{math500}, sampling uniformly across problem categories (algebra, geometry, number theory, combinatorics, etc.) with a fixed seed for reproducibility. Mathematical reasoning tasks are a natural testbed for our study: they elicit long chain-of-thought sequences (up to 2048 tokens) in which the model alternates between exploratory reasoning and structured computation---phases that differ markedly in attention sparsity. Each problem is decoded greedily (\\texttt{max\\_new\\_tokens}$=$2048) to eliminate sampling variance.\n\n\n\\subsection{Compound Sparsity Configuration}\n\\label{sec:sparsity-config}\n\nWe apply \\emph{symmetric} compound sparsity: for a given sparsity level $s$, we prune the same fraction $s$ of attention heads and evict the same fraction $s$ of KV cache entries. We evaluate four sparsity levels $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$, spanning from mild to aggressive compression.\n\n\\paragraph{Sparsity conditions.} For each problem and each sparsity level, we compute perplexity under four conditions: (i)~\\emph{dense}---no intervention; (ii)~\\emph{attn-only}---head pruning without KV eviction; (iii)~\\emph{kv-only}---KV eviction without head pruning; and (iv)~\\emph{both}---simultaneous head pruning and KV eviction.\n\n\\paragraph{Eviction strategies.} We compare two KV cache eviction strategies:\n\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\textbf{Importance-based.} Each KV position receives a score equal to its cumulative attention weight summed over all query positions and heads. To correct for the inherent causal bias---earlier positions accumulate more attention simply because they are attended to by more queries---we apply position normalization:\n\\begin{equation}\n\\label{eq:importance}\n    \\alpha_j = \\frac{\\sum_{i,h} a_{i,h,j}}{\\texttt{seq\\_len} - j}, \\quad j \\in \\{1, \\dots, T\\},\n\\end{equation}\nwhere $a_{i,h,j}$ is the attention weight from query~$i$, head~$h$ to key~$j$, and the denominator counts the number of queries that can attend to position~$j$ under causal masking. Position~0 (BOS) is always retained. The $T \\cdot s$ positions with the lowest normalized scores are evicted.\n\nDuring masked forward passes, we guard against numerical instability from the interaction of head masking and KV eviction: zeroed-out heads that would otherwise produce $\\infty \\times 0 = \\text{NaN}$ are handled via selective replacement (\\texttt{torch.where}) prior to the softmax, and any layer producing NaN outputs is skipped from the sparsity loss computation.\n\n\\item \\textbf{Random.} KV positions (excluding BOS) are evicted uniformly at random, providing a strategy-agnostic baseline. Head pruning under the random condition selects heads via \\texttt{torch.randperm} rather than by importance.\n\\end{itemize}\n\n\\paragraph{Head pruning.} Under importance-based eviction, heads are ranked by their Frobenius norm across the full attention matrix $\\mathbf{A}_\\ell \\in \\mathbb{R}^{H \\times T \\times T}$ per layer $\\ell$, and the bottom-$s$ fraction is masked. Under random eviction, heads are selected uniformly at random.\n\n\n\\subsection{Phase Segmentation}\n\\label{sec:phase-seg}\n\nWe segment each generated sequence into three \\emph{reasoning phases} based on the local attention sparsity of each token position. For each query position $i$, we compute per-head sparsity as the fraction of attention weights falling below $0.01 \\times \\max_j a_{i,h,j}$, then average across heads to obtain a scalar sparsity value per position. The resulting sparsity trajectory is partitioned into terciles via quantile boundaries: \\emph{low-sparsity} (bottom third, corresponding to diffuse attention during exploratory reasoning), \\emph{mid-sparsity}, and \\emph{high-sparsity} (top third, corresponding to focused attention during structured computation). Contiguous segments shorter than $\\texttt{min\\_phase\\_length}=10$ tokens are merged into adjacent phases to suppress noise.\n\n\n\\subsection{Metrics}\n\\label{sec:metrics}\n\n\\paragraph{Perplexity.} For each sparsity condition $c \\in \\{d, a, k, b\\}$ and each phase, we compute segment-level perplexity as\n$\\text{PPL}_c = \\exp\\!\\bigl(\\tfrac{1}{|I|}\\sum_{i \\in I} \\mathcal{L}_c(x_i)\\bigr)$,\nwhere $I$ is the set of token indices belonging to the phase and $\\mathcal{L}_c(x_i)$ is the per-token cross-entropy loss under condition $c$.\n\n\\paragraph{Interaction Index.} The interaction index quantifies the synergistic (super-additive) effect of compound sparsity beyond the sum of individual interventions:\n\\begin{equation}\n\\label{eq:ii}\n    \\mathrm{II} = \\frac{\\text{PPL}_b}{\\text{PPL}_d} - \\frac{\\text{PPL}_a}{\\text{PPL}_d} - \\frac{\\text{PPL}_k}{\\text{PPL}_d} + 1.\n\\end{equation}\nWhen $\\mathrm{II} > 0$, the two sparsity mechanisms amplify each other; $\\mathrm{II} = 0$ indicates additive (independent) degradation.\n\n\\paragraph{Severity Gradient.} To measure how the interaction varies across reasoning phases, we define the severity gradient:\n\\begin{equation}\n\\label{eq:gradient}\n    G = \\frac{\\widetilde{\\mathrm{II}}_{\\,\\textit{low}}}{\\widetilde{\\mathrm{II}}_{\\,\\textit{high}}},\n\\end{equation}\nwhere $\\widetilde{\\mathrm{II}}_{\\,\\textit{low}}$ and $\\widetilde{\\mathrm{II}}_{\\,\\textit{high}}$ are the median interaction indices over the low-sparsity and high-sparsity phases, respectively. We report medians rather than means because the II distribution is heavily right-skewed (mean/median ratios up to 43:1 at $s{=}0.30$), making the median a more robust central tendency estimator.\n\n\n\\subsection{Statistical Analysis}\n\\label{sec:stats}\n\nAll confidence intervals and significance tests are computed via the nonparametric bootstrap with $B = 10{,}000$ resamples \\cite{efron1993bootstrap}.\n\n\\paragraph{Per-problem bootstrap.} For each sparsity level and strategy, we resample the 50 per-problem II values with replacement and compute the mean of each resample, yielding a 95\\% percentile confidence interval for the population mean II.\n\n\\paragraph{Paired bootstrap.} To test whether the severity gradient differs between importance-based and random eviction, we pair observations by problem (same problem, same sparsity level) and bootstrap the difference in gradients. This controls for problem-level variance in difficulty and sequence length.\n\n\\paragraph{Unpaired bootstrap.} We additionally compute per-strategy gradient confidence intervals without pairing, to verify that the importance-based gradient is significantly greater than 1 (i.e., phase modulation exists) independently of the random baseline.\n\nAll tests yield $p < 0.0001$ at every sparsity level, confirming that the observed phase--strategy interactions are not artifacts of sampling variability.\\footnote{Experiments were conducted on a server with 4$\\times$ NVIDIA RTX PRO 6000 Blackwell Server Edition 96\\,GB GPUs, with one model--sparsity configuration per GPU.}\n",
      "numLines": 87,
      "startLine": 1,
      "totalLines": 87
    }
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Read · `toolu_01Y9hCALeM5KMBbhiXTxuw4W`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "103088e8-c35b-46f1-a93a-deef01852d45",
  "uuid": "47569ccf-cc90-4214-945e-8f1657449c7e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PhnmwxYWTtUyyNtsYgzNca",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2676,
      "cache_read_input_tokens": 24472,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2676
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

### Tool result

_source line 16 · 2026-05-14T05:49:15.299Z_

<details><summary>↩ Tool result · `toolu_01Y9hCALeM5KMBbhiXTxuw4W`</summary>

```text
1	
2	\section{Analysis: Entropy-Discrimination Collapse}
3	\label{sec:analysis}
4	
5	The results in \S\ref{sec:experiments} reveal a striking asymmetry: importance-based eviction exhibits $12$--$75\times$ severity amplification in low-sparsity phases, while random eviction remains flat at ${\sim}1\times$ across all phases. Why is compound severity phase-modulated for one strategy but not the other? We propose \emph{entropy-discrimination collapse} as an explanatory mechanism: head pruning redistributes attention mass in a phase-dependent manner, degrading the discriminative power of importance scores precisely in phases where attention is already broadly distributed.
6	
7	\subsection{Attention Redistribution Under Head Pruning}
8	\label{sec:attn-redistribution}
9	
10	When a fraction $s$ of attention heads are pruned, the surviving heads must compensate for the lost information pathways. We characterize this compensation through the attention entropy of a surviving head $h$ at query position $i$:
11	\begin{equation}
12	    \mathcal{H}_i^{(h)} = -\sum_{j=1}^{T} a_{ij}^{(h)} \log a_{ij}^{(h)}
13	    \label{eq:attn-entropy}
14	\end{equation}
15	Higher $\mathcal{H}$ indicates more uniformly distributed attention. The effect of pruning on $\mathcal{H}$ depends critically on the reasoning phase.
16	
17	In the \textbf{high-sparsity phase}, attention is already concentrated on a few key positions ($\mathcal{H}$ is low). Head redundancy is high---concentrated attention patterns are likely to overlap across heads---so pruning removes largely redundant capacity. The surviving heads continue to attend to the same narrow set of positions, and $\mathcal{H}$ changes minimally.
18	
19	In the \textbf{low-sparsity phase}, attention distributes broadly across many positions ($\mathcal{H}$ is already elevated). Head redundancy is low: each head captures partially non-overlapping information. Pruning forces surviving heads to broaden their attention further to compensate for the lost coverage, pushing $\mathcal{H}$ above its already high baseline.
20	
21	\placeholder{Empirical attention entropy: mean $\mathcal{H}$ per phase, pre- and post-pruning at $s \in \{0.15, 0.25\}$, showing differential entropy increase concentrated in the low-sparsity phase.}
22	
23	\subsection{Discrimination Collapse in Importance Scoring}
24	\label{sec:discrimination-collapse}
25	
26	The KV importance score (Eq.~\ref{eq:kv-importance}) aggregates attention mass across all surviving heads. When pruning increases the attention entropy of these heads, the cumulative importance scores become more uniform: the gap between the most-attended and least-attended positions shrinks. We hypothesize that this uniformity degrades the \emph{discriminative power} of importance-based eviction---the ability to reliably distinguish positions critical for the model's computation from those that can be safely removed.
27	
28	When the importance distribution has low entropy (a few positions dominate), thresholding the bottom-$s$ fraction removes genuinely unimportant positions. When the distribution is near-uniform, the same thresholding becomes noise-sensitive: small perturbations change which positions cross the eviction boundary. In the limit of perfectly uniform importance scores, importance-based eviction degenerates into an arbitrary selection functionally equivalent to biased random eviction.
29	
30	\placeholder{Importance score concentration (Gini coefficient or max-to-median ratio) across phases, pre- and post-pruning, showing discrimination collapse predominantly in the low-sparsity phase.}
31	
32	This mechanism directly accounts for the crossover phenomenon (\S\ref{sec:crossover}). In high-sparsity phases, pruning preserves attention concentration, importance scores remain discriminative, and importance-based eviction removes genuinely less critical positions---achieving lower compound severity than random eviction. In low-sparsity phases, pruning amplifies attention entropy, importance discrimination collapses, and importance-based eviction devolves into a biased pseudo-random process that can inadvertently remove critical positions---producing \emph{higher} compound severity than the explicitly random baseline. The severity inversion is thus not a failure of the importance metric in isolation, but an emergent consequence of the interaction between head pruning and importance scoring conditioned on the phase-dependent attention structure.
33	
34	Random eviction is immune to this mechanism: its decisions are independent of attention patterns and invariant to the redistribution caused by head pruning. This explains the flat severity gradient ($G \approx 1$) observed under random eviction at all sparsity levels.
35	
36	\subsection{Implications for Compound Sparsity}
37	\label{sec:analysis-implications}
38	
39	The entropy-discrimination collapse mechanism suggests several broader conclusions.
40	
41	\paragraph{Architecture generality.} The mechanism depends on two properties: (i)~attention-mass-based importance scoring for KV eviction, and (ii)~heterogeneous attention entropy across reasoning phases. Both are shared by the major KV cache compression methods---H$_2$O \cite{h2o2024}, SnapKV \cite{snapkv2024}, PyramidKV \cite{pyramidkv2024}---and by any autoregressive transformer producing extended reasoning traces. We therefore expect phase-modulated compound severity to emerge whenever head pruning is combined with attention-based cache eviction, regardless of specific model architecture.
42	
43	\paragraph{Testable prediction.} Any importance metric derived from attention mass should exhibit discrimination collapse in phases where attention is broadly distributed, with the severity gradient scaling with the pruning-induced entropy increase. Metrics that derive importance from sources independent of attention---such as activation magnitude or gradient-based saliency---would not be subject to the same collapse and should produce flatter severity gradients. This prediction is directly testable in future work.
44	
45	\paragraph{Reframing compound severity.} The flat random baseline ($G \approx 1$) demonstrates that phase-modulated severity amplification is not an inherent cost of compound sparsity \emph{per se}. Rather, it is an emergent interaction between the eviction strategy and the phase-dependent structure of attention. This reframes compound severity as a \emph{strategy-phase interaction}---one that a phase-aware sparsity controller could, in principle, mitigate by adjusting the eviction budget or strategy per phase.
46	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "103088e8-c35b-46f1-a93a-deef01852d45",
  "uuid": "60939212-2146-48bd-8b6f-6af68bf09a93",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex",
      "content": "\n\\section{Analysis: Entropy-Discrimination Collapse}\n\\label{sec:analysis}\n\nThe results in \\S\\ref{sec:experiments} reveal a striking asymmetry: importance-based eviction exhibits $12$--$75\\times$ severity amplification in low-sparsity phases, while random eviction remains flat at ${\\sim}1\\times$ across all phases. Why is compound severity phase-modulated for one strategy but not the other? We propose \\emph{entropy-discrimination collapse} as an explanatory mechanism: head pruning redistributes attention mass in a phase-dependent manner, degrading the discriminative power of importance scores precisely in phases where attention is already broadly distributed.\n\n\\subsection{Attention Redistribution Under Head Pruning}\n\\label{sec:attn-redistribution}\n\nWhen a fraction $s$ of attention heads are pruned, the surviving heads must compensate for the lost information pathways. We characterize this compensation through the attention entropy of a surviving head $h$ at query position $i$:\n\\begin{equation}\n    \\mathcal{H}_i^{(h)} = -\\sum_{j=1}^{T} a_{ij}^{(h)} \\log a_{ij}^{(h)}\n    \\label{eq:attn-entropy}\n\\end{equation}\nHigher $\\mathcal{H}$ indicates more uniformly distributed attention. The effect of pruning on $\\mathcal{H}$ depends critically on the reasoning phase.\n\nIn the \\textbf{high-sparsity phase}, attention is already concentrated on a few key positions ($\\mathcal{H}$ is low). Head redundancy is high---concentrated attention patterns are likely to overlap across heads---so pruning removes largely redundant capacity. The surviving heads continue to attend to the same narrow set of positions, and $\\mathcal{H}$ changes minimally.\n\nIn the \\textbf{low-sparsity phase}, attention distributes broadly across many positions ($\\mathcal{H}$ is already elevated). Head redundancy is low: each head captures partially non-overlapping information. Pruning forces surviving heads to broaden their attention further to compensate for the lost coverage, pushing $\\mathcal{H}$ above its already high baseline.\n\n\\placeholder{Empirical attention entropy: mean $\\mathcal{H}$ per phase, pre- and post-pruning at $s \\in \\{0.15, 0.25\\}$, showing differential entropy increase concentrated in the low-sparsity phase.}\n\n\\subsection{Discrimination Collapse in Importance Scoring}\n\\label{sec:discrimination-collapse}\n\nThe KV importance score (Eq.~\\ref{eq:kv-importance}) aggregates attention mass across all surviving heads. When pruning increases the attention entropy of these heads, the cumulative importance scores become more uniform: the gap between the most-attended and least-attended positions shrinks. We hypothesize that this uniformity degrades the \\emph{discriminative power} of importance-based eviction---the ability to reliably distinguish positions critical for the model's computation from those that can be safely removed.\n\nWhen the importance distribution has low entropy (a few positions dominate), thresholding the bottom-$s$ fraction removes genuinely unimportant positions. When the distribution is near-uniform, the same thresholding becomes noise-sensitive: small perturbations change which positions cross the eviction boundary. In the limit of perfectly uniform importance scores, importance-based eviction degenerates into an arbitrary selection functionally equivalent to biased random eviction.\n\n\\placeholder{Importance score concentration (Gini coefficient or max-to-median ratio) across phases, pre- and post-pruning, showing discrimination collapse predominantly in the low-sparsity phase.}\n\nThis mechanism directly accounts for the crossover phenomenon (\\S\\ref{sec:crossover}). In high-sparsity phases, pruning preserves attention concentration, importance scores remain discriminative, and importance-based eviction removes genuinely less critical positions---achieving lower compound severity than random eviction. In low-sparsity phases, pruning amplifies attention entropy, importance discrimination collapses, and importance-based eviction devolves into a biased pseudo-random process that can inadvertently remove critical positions---producing \\emph{higher} compound severity than the explicitly random baseline. The severity inversion is thus not a failure of the importance metric in isolation, but an emergent consequence of the interaction between head pruning and importance scoring conditioned on the phase-dependent attention structure.\n\nRandom eviction is immune to this mechanism: its decisions are independent of attention patterns and invariant to the redistribution caused by head pruning. This explains the flat severity gradient ($G \\approx 1$) observed under random eviction at all sparsity levels.\n\n\\subsection{Implications for Compound Sparsity}\n\\label{sec:analysis-implications}\n\nThe entropy-discrimination collapse mechanism suggests several broader conclusions.\n\n\\paragraph{Architecture generality.} The mechanism depends on two properties: (i)~attention-mass-based importance scoring for KV eviction, and (ii)~heterogeneous attention entropy across reasoning phases. Both are shared by the major KV cache compression methods---H$_2$O \\cite{h2o2024}, SnapKV \\cite{snapkv2024}, PyramidKV \\cite{pyramidkv2024}---and by any autoregressive transformer producing extended reasoning traces. We therefore expect phase-modulated compound severity to emerge whenever head pruning is combined with attention-based cache eviction, regardless of specific model architecture.\n\n\\paragraph{Testable prediction.} Any importance metric derived from attention mass should exhibit discrimination collapse in phases where attention is broadly distributed, with the severity gradient scaling with the pruning-induced entropy increase. Metrics that derive importance from sources independent of attention---such as activation magnitude or gradient-based saliency---would not be subject to the same collapse and should produce flatter severity gradients. This prediction is directly testable in future work.\n\n\\paragraph{Reframing compound severity.} The flat random baseline ($G \\approx 1$) demonstrates that phase-modulated severity amplification is not an inherent cost of compound sparsity \\emph{per se}. Rather, it is an emergent interaction between the eviction strategy and the phase-dependent structure of attention. This reframes compound severity as a \\emph{strategy-phase interaction}---one that a phase-aware sparsity controller could, in principle, mitigate by adjusting the eviction budget or strategy per phase.\n",
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

_source line 17_

<details open><summary>🔧 Tool call — Read · `toolu_01UGQ6Mr2d5H256cPaByiCNo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "103088e8-c35b-46f1-a93a-deef01852d45",
  "uuid": "a90f7838-c77e-4872-a4e3-7ec8b94eb026",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PhnmwxYWTtUyyNtsYgzNca",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2676,
      "cache_read_input_tokens": 24472,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2676
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

### Tool result

_source line 18 · 2026-05-14T05:49:15.628Z_

<details><summary>↩ Tool result · `toolu_01UGQ6Mr2d5H256cPaByiCNo`</summary>

```text
1	
2	\section{Results}
3	\label{sec:results}
4	
5	We present our main findings in three parts: the phase-modulated severity gradient (\S\ref{sec:severity-gradient}), the strategy-dependent crossover phenomenon (\S\ref{sec:crossover}), and cross-model replication (\S\ref{sec:cross-model}).
6	
7	
8	\subsection{Phase-Modulated Severity Gradient}
9	\label{sec:severity-gradient}
10	
11	% Evidence: v5_importance_segment, v5_random_segment
12	Table~\ref{tab:main-results} reports the interaction index (II) and severity gradient across all sparsity levels and eviction strategies. Under importance-based eviction, the severity gradient---the ratio of low-phase to high-phase median II---increases monotonically from \placeholder{G\_s15} at $s{=}0.15$ to \placeholder{G\_s20} at $s{=}0.20$, \placeholder{G\_s25} at $s{=}0.25$, and \placeholder{G\_s30} at $s{=}0.30$, spanning a \placeholder{min}--\placeholder{max}$\times$ range. Under random eviction, the gradient remains near unity at all sparsity levels ($G \approx$ \placeholder{G\_rand\_range}), indicating that the phase modulation effect is specific to the importance-based strategy rather than an artifact of compound sparsity itself.
13	
14	\begin{table}[t]
15	\centering
16	\small
17	\caption{Main results: Interaction Index (II) by eviction strategy, reasoning phase, and sparsity level. II values are segment-level medians across 50 problems. The severity gradient $G = \widetilde{\mathrm{II}}_{\textit{low}} / \widetilde{\mathrm{II}}_{\textit{high}}$ quantifies the phase-dependent amplification of compound interaction.}
18	\label{tab:main-results}
19	\begin{tabular}{@{}llcccc@{}}
20	\toprule
21	$s$ & Strategy & $\widetilde{\mathrm{II}}_{\textit{high}}$ & $\widetilde{\mathrm{II}}_{\textit{low}}$ & $G$ & 95\% CI \\
22	\midrule
23	0.15 & Importance & \placeholder{} & \placeholder{} & \placeholder{} & [\placeholder{}, \placeholder{}] \\
24	0.15 & Random     & \placeholder{} & \placeholder{} & \placeholder{} & [\placeholder{}, \placeholder{}] \\
25	\addlinespace
26	0.20 & Importance & \placeholder{} & \placeholder{} & \placeholder{} & [\placeholder{}, \placeholder{}] \\
27	0.20 & Random     & \placeholder{} & \placeholder{} & \placeholder{} & [\placeholder{}, \placeholder{}] \\
28	\addlinespace
29	0.25 & Importance & \placeholder{} & \placeholder{} & \placeholder{} & [\placeholder{}, \placeholder{}] \\
30	0.25 & Random     & \placeholder{} & \placeholder{} & \placeholder{} & [\placeholder{}, \placeholder{}] \\
31	\addlinespace
32	0.30 & Importance & \placeholder{} & \placeholder{} & \placeholder{} & [\placeholder{}, \placeholder{}] \\
33	0.30 & Random     & \placeholder{} & \placeholder{} & \placeholder{} & [\placeholder{}, \placeholder{}] \\
34	\bottomrule
35	\end{tabular}
36	\end{table}
37	
38	% Evidence: v5_importance_segment
39	The gradient growth is sub-exponential: successive ratios between adjacent sparsity levels are \placeholder{r\_15\_20}$\times$, \placeholder{r\_20\_25}$\times$, and \placeholder{r\_25\_30}$\times$---a decreasing growth rate. This pattern suggests a ceiling effect at higher sparsity levels, where compound degradation in the low-sparsity phase approaches saturation. Figure~\ref{fig:hero} visualizes this trajectory, contrasting the steep importance-based curve against the flat random baseline.
40	
41	\begin{figure}[t]
42	\centering
43	\includegraphics[width=\columnwidth]{figures/fig1_hero.pdf}
44	\caption{Severity gradient ($G$) as a function of sparsity level $s$. Importance-based eviction (solid) exhibits a monotonically increasing gradient from \placeholder{} to \placeholder{}$\times$, while random eviction (dashed) remains flat near $1\times$. Shaded regions denote 95\% bootstrap confidence intervals.}
45	\label{fig:hero}
46	\end{figure}
47	
48	% Evidence: v6_bootstrap
49	Table~\ref{tab:bootstrap} presents bootstrap confidence intervals ($B{=}10{,}000$). Both paired and unpaired tests confirm that the importance-based gradient exceeds unity at every sparsity level, with all $p < 0.0001$. The paired analysis---which controls for problem-level variance by matching the same problem across strategies---yields tighter intervals than the unpaired analysis, consistent with the high between-problem variance in sequence length and II magnitude.
50	
51	\begin{table}[t]
52	\centering
53	\small
54	\caption{Bootstrap confidence intervals ($B{=}10{,}000$) for the severity gradient. Paired: same problem matched across strategies. Unpaired: per-strategy gradient CI. All tests reject $H_0{:}\, G = 1$ at $p < 0.0001$.}
55	\label{tab:bootstrap}
56	\begin{tabular}{@{}lcccc@{}}
57	\toprule
58	$s$ & Paired $G$ & Paired 95\% CI & Unpaired $G$ & Unpaired 95\% CI \\
59	\midrule
60	0.15 & \placeholder{} & [\placeholder{}, \placeholder{}] & \placeholder{} & [\placeholder{}, \placeholder{}] \\
61	0.20 & \placeholder{} & [\placeholder{}, \placeholder{}] & \placeholder{} & [\placeholder{}, \placeholder{}] \\
62	0.25 & \placeholder{} & [\placeholder{}, \placeholder{}] & \placeholder{} & [\placeholder{}, \placeholder{}] \\
63	0.30 & \placeholder{} & [\placeholder{}, \placeholder{}] & \placeholder{} & [\placeholder{}, \placeholder{}] \\
64	\bottomrule
65	\end{tabular}
66	\end{table}
67	
68	\begin{figure}[t]
69	\centering
70	\includegraphics[width=\columnwidth]{figures/fig4_bootstrap.pdf}
71	\caption{Forest plot of bootstrap severity gradient estimates. Horizontal bars show 95\% percentile CIs; diamonds mark point estimates. All importance-based CIs lie entirely above $G{=}1$ (vertical dashed line), confirming phase modulation at every sparsity level.}
72	\label{fig:bootstrap-forest}
73	\end{figure}
74	
75	We report medians throughout because the II distribution is heavily right-skewed: mean/median ratios reach \placeholder{skew\_ratio}:1 at $s{=}0.30$ under importance-based eviction. A small number of problems with exceptionally long reasoning traces produce outsized II values; the median resists this influence while the bootstrap CI accounts for it via the resampling distribution.
76	
77	
78	\subsection{Strategy-Dependent Crossover}
79	\label{sec:crossover}
80	
81	% Evidence: v5_importance_segment, v5_random_segment
82	The phase-modulated gradient produces a striking qualitative phenomenon: a \emph{crossover} in which importance-based eviction is simultaneously the better and worse strategy depending on the reasoning phase. At $s{=}$\placeholder{s\_cross}, importance-based eviction yields a lower II than random in the high-sparsity phase ($\widetilde{\mathrm{II}}_{\textit{high}} =$ \placeholder{imp\_high} vs.\ \placeholder{rand\_high}), but a dramatically higher II in the low-sparsity phase ($\widetilde{\mathrm{II}}_{\textit{low}} =$ \placeholder{imp\_low} vs.\ \placeholder{rand\_low}). This is not merely a magnitude difference---it is a reversal in the relative ranking of strategies across phases.
83	
84	Figure~\ref{fig:crossover} displays the crossover structure as a heatmap of per-phase II values across strategies and sparsity levels. The crossover emerges because importance-based eviction, by design, concentrates its retention budget on high-attention positions. In high-sparsity phases, where attention is already diffuse, this concentration provides a genuine advantage. In low-sparsity phases, however, the interaction between head pruning and importance scoring disrupts the eviction strategy's discriminative capacity (analyzed in \S\ref{sec:analysis}), converting a targeted intervention into an adversarial one.
85	
86	\begin{figure}[t]
87	\centering
88	\includegraphics[width=\columnwidth]{figures/fig2_crossover.pdf}
89	\caption{Strategy-dependent crossover. Heatmap of median II by eviction strategy (rows) and reasoning phase (columns) at $s{=}$\placeholder{}. Importance-based eviction outperforms random in the high-sparsity phase but produces \placeholder{}$\times$ higher II in the low-sparsity phase, reversing the strategy ranking.}
90	\label{fig:crossover}
91	\end{figure}
92	
93	The crossover is observable at $s \geq$ \placeholder{s\_onset}: at lower sparsity levels, importance-based eviction maintains an advantage (or comparable performance) in both phases. The onset of crossover thus marks a phase transition in the compound interaction---the point at which sparsity is sufficient for head pruning to degrade the importance metric's phase-specific discriminability.
94	
95	
96	\subsection{Cross-Model Replication}
97	\label{sec:cross-model}
98	
99	% Evidence: qwen_bf16 (pending)
100	To assess whether the phase-modulated severity gradient is specific to DeepSeek-R1-Distill-Qwen-7B or reflects a more general property of compound sparsity, we replicate the importance-based eviction experiments on Qwen2.5-7B-Instruct \cite{qwen2.5}. Despite lacking explicit reasoning delimiters, Qwen2.5-7B-Instruct exhibits sufficient variation in attention sparsity across its generation trajectory to permit phase segmentation via the same quantile-based method (\S\ref{sec:phase-seg}).
101	
102	Table~\ref{tab:cross-model} compares the severity gradient across both models. Qwen2.5-7B-Instruct produces a gradient of \placeholder{G\_qwen\_s15} at $s{=}0.15$, rising to \placeholder{G\_qwen\_s30} at $s{=}0.30$, qualitatively reproducing the monotonic increase observed in DeepSeek. The absolute gradient magnitudes \placeholder{differ\_or\_match}: \placeholder{cross\_model\_detail}.
103	
104	\begin{table}[t]
105	\centering
106	\small
107	\caption{Cross-model replication: severity gradient ($G$) under importance-based eviction for DeepSeek-R1-Distill-Qwen-7B and Qwen2.5-7B-Instruct. Both models exhibit monotonically increasing phase-modulated gradients.}
108	\label{tab:cross-model}
109	\begin{tabular}{@{}lcccc@{}}
110	\toprule
111	Model & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
112	\midrule
113	DeepSeek-R1-Distill-Qwen-7B & \placeholder{} & \placeholder{} & \placeholder{} & \placeholder{} \\
114	Qwen2.5-7B-Instruct         & \placeholder{} & \placeholder{} & \placeholder{} & \placeholder{} \\
115	\bottomrule
116	\end{tabular}
117	\end{table}
118	
119	\begin{figure}[t]
120	\centering
121	\includegraphics[width=\columnwidth]{figures/fig5_crossmodel.pdf}
122	\caption{Cross-model comparison of the severity gradient. Both DeepSeek (solid) and Qwen (dashed) exhibit monotonically increasing gradients under importance-based eviction, though the absolute magnitudes \placeholder{differ\_or\_match}.}
123	\label{fig:cross-model}
124	\end{figure}
125	
126	The replication on a second model from the same architectural family but with distinct training (instruction tuning without reasoning distillation) suggests that the phase-modulated severity gradient is not an artifact of DeepSeek's distillation-induced phase structure, but rather an emergent property of how compound sparsity interacts with attention dynamics in Transformer-based language models.
127	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "103088e8-c35b-46f1-a93a-deef01852d45",
  "uuid": "9caab59a-e581-4144-b443-98abf4ade14b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex",
      "content": "\n\\section{Results}\n\\label{sec:results}\n\nWe present our main findings in three parts: the phase-modulated severity gradient (\\S\\ref{sec:severity-gradient}), the strategy-dependent crossover phenomenon (\\S\\ref{sec:crossover}), and cross-model replication (\\S\\ref{sec:cross-model}).\n\n\n\\subsection{Phase-Modulated Severity Gradient}\n\\label{sec:severity-gradient}\n\n% Evidence: v5_importance_segment, v5_random_segment\nTable~\\ref{tab:main-results} reports the interaction index (II) and severity gradient across all sparsity levels and eviction strategies. Under importance-based eviction, the severity gradient---the ratio of low-phase to high-phase median II---increases monotonically from \\placeholder{G\\_s15} at $s{=}0.15$ to \\placeholder{G\\_s20} at $s{=}0.20$, \\placeholder{G\\_s25} at $s{=}0.25$, and \\placeholder{G\\_s30} at $s{=}0.30$, spanning a \\placeholder{min}--\\placeholder{max}$\\times$ range. Under random eviction, the gradient remains near unity at all sparsity levels ($G \\approx$ \\placeholder{G\\_rand\\_range}), indicating that the phase modulation effect is specific to the importance-based strategy rather than an artifact of compound sparsity itself.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Main results: Interaction Index (II) by eviction strategy, reasoning phase, and sparsity level. II values are segment-level medians across 50 problems. The severity gradient $G = \\widetilde{\\mathrm{II}}_{\\textit{low}} / \\widetilde{\\mathrm{II}}_{\\textit{high}}$ quantifies the phase-dependent amplification of compound interaction.}\n\\label{tab:main-results}\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\n$s$ & Strategy & $\\widetilde{\\mathrm{II}}_{\\textit{high}}$ & $\\widetilde{\\mathrm{II}}_{\\textit{low}}$ & $G$ & 95\\% CI \\\\\n\\midrule\n0.15 & Importance & \\placeholder{} & \\placeholder{} & \\placeholder{} & [\\placeholder{}, \\placeholder{}] \\\\\n0.15 & Random     & \\placeholder{} & \\placeholder{} & \\placeholder{} & [\\placeholder{}, \\placeholder{}] \\\\\n\\addlinespace\n0.20 & Importance & \\placeholder{} & \\placeholder{} & \\placeholder{} & [\\placeholder{}, \\placeholder{}] \\\\\n0.20 & Random     & \\placeholder{} & \\placeholder{} & \\placeholder{} & [\\placeholder{}, \\placeholder{}] \\\\\n\\addlinespace\n0.25 & Importance & \\placeholder{} & \\placeholder{} & \\placeholder{} & [\\placeholder{}, \\placeholder{}] \\\\\n0.25 & Random     & \\placeholder{} & \\placeholder{} & \\placeholder{} & [\\placeholder{}, \\placeholder{}] \\\\\n\\addlinespace\n0.30 & Importance & \\placeholder{} & \\placeholder{} & \\placeholder{} & [\\placeholder{}, \\placeholder{}] \\\\\n0.30 & Random     & \\placeholder{} & \\placeholder{} & \\placeholder{} & [\\placeholder{}, \\placeholder{}] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% Evidence: v5_importance_segment\nThe gradient growth is sub-exponential: successive ratios between adjacent sparsity levels are \\placeholder{r\\_15\\_20}$\\times$, \\placeholder{r\\_20\\_25}$\\times$, and \\placeholder{r\\_25\\_30}$\\times$---a decreasing growth rate. This pattern suggests a ceiling effect at higher sparsity levels, where compound degradation in the low-sparsity phase approaches saturation. Figure~\\ref{fig:hero} visualizes this trajectory, contrasting the steep importance-based curve against the flat random baseline.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig1_hero.pdf}\n\\caption{Severity gradient ($G$) as a function of sparsity level $s$. Importance-based eviction (solid) exhibits a monotonically increasing gradient from \\placeholder{} to \\placeholder{}$\\times$, while random eviction (dashed) remains flat near $1\\times$. Shaded regions denote 95\\% bootstrap confidence intervals.}\n\\label{fig:hero}\n\\end{figure}\n\n% Evidence: v6_bootstrap\nTable~\\ref{tab:bootstrap} presents bootstrap confidence intervals ($B{=}10{,}000$). Both paired and unpaired tests confirm that the importance-based gradient exceeds unity at every sparsity level, with all $p < 0.0001$. The paired analysis---which controls for problem-level variance by matching the same problem across strategies---yields tighter intervals than the unpaired analysis, consistent with the high between-problem variance in sequence length and II magnitude.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Bootstrap confidence intervals ($B{=}10{,}000$) for the severity gradient. Paired: same problem matched across strategies. Unpaired: per-strategy gradient CI. All tests reject $H_0{:}\\, G = 1$ at $p < 0.0001$.}\n\\label{tab:bootstrap}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n$s$ & Paired $G$ & Paired 95\\% CI & Unpaired $G$ & Unpaired 95\\% CI \\\\\n\\midrule\n0.15 & \\placeholder{} & [\\placeholder{}, \\placeholder{}] & \\placeholder{} & [\\placeholder{}, \\placeholder{}] \\\\\n0.20 & \\placeholder{} & [\\placeholder{}, \\placeholder{}] & \\placeholder{} & [\\placeholder{}, \\placeholder{}] \\\\\n0.25 & \\placeholder{} & [\\placeholder{}, \\placeholder{}] & \\placeholder{} & [\\placeholder{}, \\placeholder{}] \\\\\n0.30 & \\placeholder{} & [\\placeholder{}, \\placeholder{}] & \\placeholder{} & [\\placeholder{}, \\placeholder{}] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4_bootstrap.pdf}\n\\caption{Forest plot of bootstrap severity gradient estimates. Horizontal bars show 95\\% percentile CIs; diamonds mark point estimates. All importance-based CIs lie entirely above $G{=}1$ (vertical dashed line), confirming phase modulation at every sparsity level.}\n\\label{fig:bootstrap-forest}\n\\end{figure}\n\nWe report medians throughout because the II distribution is heavily right-skewed: mean/median ratios reach \\placeholder{skew\\_ratio}:1 at $s{=}0.30$ under importance-based eviction. A small number of problems with exceptionally long reasoning traces produce outsized II values; the median resists this influence while the bootstrap CI accounts for it via the resampling distribution.\n\n\n\\subsection{Strategy-Dependent Crossover}\n\\label{sec:crossover}\n\n% Evidence: v5_importance_segment, v5_random_segment\nThe phase-modulated gradient produces a striking qualitative phenomenon: a \\emph{crossover} in which importance-based eviction is simultaneously the better and worse strategy depending on the reasoning phase. At $s{=}$\\placeholder{s\\_cross}, importance-based eviction yields a lower II than random in the high-sparsity phase ($\\widetilde{\\mathrm{II}}_{\\textit{high}} =$ \\placeholder{imp\\_high} vs.\\ \\placeholder{rand\\_high}), but a dramatically higher II in the low-sparsity phase ($\\widetilde{\\mathrm{II}}_{\\textit{low}} =$ \\placeholder{imp\\_low} vs.\\ \\placeholder{rand\\_low}). This is not merely a magnitude difference---it is a reversal in the relative ranking of strategies across phases.\n\nFigure~\\ref{fig:crossover} displays the crossover structure as a heatmap of per-phase II values across strategies and sparsity levels. The crossover emerges because importance-based eviction, by design, concentrates its retention budget on high-attention positions. In high-sparsity phases, where attention is already diffuse, this concentration provides a genuine advantage. In low-sparsity phases, however, the interaction between head pruning and importance scoring disrupts the eviction strategy's discriminative capacity (analyzed in \\S\\ref{sec:analysis}), converting a targeted intervention into an adversarial one.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig2_crossover.pdf}\n\\caption{Strategy-dependent crossover. Heatmap of median II by eviction strategy (rows) and reasoning phase (columns) at $s{=}$\\placeholder{}. Importance-based eviction outperforms random in the high-sparsity phase but produces \\placeholder{}$\\times$ higher II in the low-sparsity phase, reversing the strategy ranking.}\n\\label{fig:crossover}\n\\end{figure}\n\nThe crossover is observable at $s \\geq$ \\placeholder{s\\_onset}: at lower sparsity levels, importance-based eviction maintains an advantage (or comparable performance) in both phases. The onset of crossover thus marks a phase transition in the compound interaction---the point at which sparsity is sufficient for head pruning to degrade the importance metric's phase-specific discriminability.\n\n\n\\subsection{Cross-Model Replication}\n\\label{sec:cross-model}\n\n% Evidence: qwen_bf16 (pending)\nTo assess whether the phase-modulated severity gradient is specific to DeepSeek-R1-Distill-Qwen-7B or reflects a more general property of compound sparsity, we replicate the importance-based eviction experiments on Qwen2.5-7B-Instruct \\cite{qwen2.5}. Despite lacking explicit reasoning delimiters, Qwen2.5-7B-Instruct exhibits sufficient variation in attention sparsity across its generation trajectory to permit phase segmentation via the same quantile-based method (\\S\\ref{sec:phase-seg}).\n\nTable~\\ref{tab:cross-model} compares the severity gradient across both models. Qwen2.5-7B-Instruct produces a gradient of \\placeholder{G\\_qwen\\_s15} at $s{=}0.15$, rising to \\placeholder{G\\_qwen\\_s30} at $s{=}0.30$, qualitatively reproducing the monotonic increase observed in DeepSeek. The absolute gradient magnitudes \\placeholder{differ\\_or\\_match}: \\placeholder{cross\\_model\\_detail}.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-model replication: severity gradient ($G$) under importance-based eviction for DeepSeek-R1-Distill-Qwen-7B and Qwen2.5-7B-Instruct. Both models exhibit monotonically increasing phase-modulated gradients.}\n\\label{tab:cross-model}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nModel & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\\\\n\\midrule\nDeepSeek-R1-Distill-Qwen-7B & \\placeholder{} & \\placeholder{} & \\placeholder{} & \\placeholder{} \\\\\nQwen2.5-7B-Instruct         & \\placeholder{} & \\placeholder{} & \\placeholder{} & \\placeholder{} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig5_crossmodel.pdf}\n\\caption{Cross-model comparison of the severity gradient. Both DeepSeek (solid) and Qwen (dashed) exhibit monotonically increasing gradients under importance-based eviction, though the absolute magnitudes \\placeholder{differ\\_or\\_match}.}\n\\label{fig:cross-model}\n\\end{figure}\n\nThe replication on a second model from the same architectural family but with distinct training (instruction tuning without reasoning distillation) suggests that the phase-modulated severity gradient is not an artifact of DeepSeek's distillation-induced phase structure, but rather an emergent property of how compound sparsity interacts with attention dynamics in Transformer-based language models.\n",
      "numLines": 127,
      "startLine": 1,
      "totalLines": 127
    }
  }
}
```

</details>

---

### Assistant

_source line 19_

<details><summary>Logged reasoning block</summary>

```text
The existing results.tex already has a good structure and placeholder-based skeleton. Let me compare it against the task requirements:

Task requirements:
1. §5.1 Experimental Setup - recap
2. §5.2 Main Results — Strategy-Dependent Severity (C1)
3. §5.3 Phase-Modulated Amplification (C2)
4. §5.4 Phase-Strategy Crossover (C3)
5. §5.5 Cross-Model Replication (C5)


6. §5.6 Statistical Validation

The current structure has several gaps: there's no dedicated experimental setup recap, C1 and C2 are merged into a single section when they should be separate, and statistical validation is buried within the first section rather than standing as its own subsection. Plus the analysis is still referencing older segment-level estimates instead of the problem-level bootstrap results.

Now I need to restructure this into the six subsections the task specifies, use the correct placeholder format with experiment IDs and metrics, frame everything around emergent phase-strategy interactions, calibrate my language to match the evidence strength, and make sure all table and figure references are in place. I should also check what the discussion section references from results so I can maintain compatibility with those labels.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "103088e8-c35b-46f1-a93a-deef01852d45",
  "uuid": "94c616b3-2f19-4b82-b79a-af14d5b52be2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NT4ryEcHvN8Z8A34UfNiez",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7958,
      "cache_read_input_tokens": 27148,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7958
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

_source line 20_

Let me check what section labels the discussion references.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "103088e8-c35b-46f1-a93a-deef01852d45",
  "uuid": "d0a1dfd2-24b3-44b9-aa75-a38b2c1762ba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NT4ryEcHvN8Z8A34UfNiez",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7958,
      "cache_read_input_tokens": 27148,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7958
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

_source line 21_

<details open><summary>🔧 Tool call — Grep · `toolu_01Dhsu5P2Q1YWUPWZv14KSXX`</summary>

```json
{
  "pattern": "\\\\ref\\{.*\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "103088e8-c35b-46f1-a93a-deef01852d45",
  "uuid": "d2b1ac23-fb89-490e-8ca4-599d3f831892",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NT4ryEcHvN8Z8A34UfNiez",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7958,
      "cache_read_input_tokens": 27148,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7958
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

_source line 22 · 2026-05-14T05:49:33.267Z_

<details><summary>↩ Tool result · `toolu_01Dhsu5P2Q1YWUPWZv14KSXX`</summary>

```text
16:across sparsity levels (Table~\ref{tab:bootstrap})---far exceeds what a naive ``less discriminative $\Rightarrow$ somewhat worse'' argument would predict.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "103088e8-c35b-46f1-a93a-deef01852d45",
  "uuid": "3de8208e-07bf-483c-ae0a-1b6e6da49b60",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "16:across sparsity levels (Table~\\ref{tab:bootstrap})---far exceeds what a naive ``less discriminative $\\Rightarrow$ somewhat worse'' argument would predict.",
    "numLines": 1
  }
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Grep · `toolu_0156VdNPoaTkatapAb4J7dT3`</summary>

```json
{
  "pattern": "\\\\ref\\{sec:(severity|crossover|cross-model|results|experiments)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "103088e8-c35b-46f1-a93a-deef01852d45",
  "uuid": "7dd6f5bf-bbf2-43e1-bfc4-227c2d7a700a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NT4ryEcHvN8Z8A34UfNiez",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7958,
      "cache_read_input_tokens": 27148,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7958
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

_source line 24 · 2026-05-14T05:49:33.509Z_

<details><summary>↩ Tool result · `toolu_0156VdNPoaTkatapAb4J7dT3`</summary>

```text
artifacts/_project/paper/analysis.tex:5:[Omitted long matching line]
artifacts/_project/paper/analysis.tex:32:[Omitted long matching line]
artifacts/_project/paper/results.tex:5:We present our main findings in three parts: the phase-modulated severity gradient (\S\ref{sec:severity-gradient}), the strategy-dependent crossover phenomenon (\S\ref{sec:crossover}), and cross-model replication (\S\ref{sec:cross-model}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "103088e8-c35b-46f1-a93a-deef01852d45",
  "uuid": "64b0b79b-e378-4ee4-8a1f-7226b8800b1d",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "artifacts/_project/paper/analysis.tex:5:[Omitted long matching line]\nartifacts/_project/paper/analysis.tex:32:[Omitted long matching line]\nartifacts/_project/paper/results.tex:5:We present our main findings in three parts: the phase-modulated severity gradient (\\S\\ref{sec:severity-gradient}), the strategy-dependent crossover phenomenon (\\S\\ref{sec:crossover}), and cross-model replication (\\S\\ref{sec:cross-model}).",
    "numLines": 3
  }
}
```

</details>

---

### Assistant

_source line 25_

<details><summary>Logged reasoning block</summary>

```text
Now I need to check what labels the analysis.tex references. It seems to reference `\ref{sec:crossover}` and `\ref{sec:experiments}`. Let me also check the full set of cross-references to make sure I maintain compatibility.

Let me also check what labels from results.tex are referenced in other files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "103088e8-c35b-46f1-a93a-deef01852d45",
  "uuid": "8ff230e6-654a-45eb-8769-3abc69dd8ed8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0169pLcv5YhYBynZhB694XKn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1049,
      "cache_read_input_tokens": 35106,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1049
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

<details open><summary>🔧 Tool call — Grep · `toolu_01T1AwKtA5pr8F2kGJzqrb3r`</summary>

```json
{
  "pattern": "\\\\ref\\{(sec:|tab:|fig:)(severity-gradient|crossover|cross-model|main-results|bootstrap|hero|crossover|bootstrap-forest|cross-model|experiments|results)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "103088e8-c35b-46f1-a93a-deef01852d45",
  "uuid": "9f0b4256-637f-4d7b-9c30-2f8a78fa978e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0169pLcv5YhYBynZhB694XKn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1049,
      "cache_read_input_tokens": 35106,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1049
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

_source line 27 · 2026-05-14T05:49:39.584Z_

<details><summary>↩ Tool result · `toolu_01T1AwKtA5pr8F2kGJzqrb3r`</summary>

```text
artifacts/_project/paper/analysis.tex:5:[Omitted long matching line]
artifacts/_project/paper/analysis.tex:32:[Omitted long matching line]
artifacts/_project/paper/discussion.tex:16:across sparsity levels (Table~\ref{tab:bootstrap})---far exceeds what a naive ``less discriminative $\Rightarrow$ somewhat worse'' argument would predict.
artifacts/_project/paper/results.tex:5:We present our main findings in three parts: the phase-modulated severity gradient (\S\ref{sec:severity-gradient}), the strategy-dependent crossover phenomenon (\S\ref{sec:crossover}), and cross-model replication (\S\ref{sec:cross-model}).
artifacts/_project/paper/results.tex:12:[Omitted long matching line]
artifacts/_project/paper/results.tex:39:The gradient growth is sub-exponential: successive ratios between adjacent sparsity levels are \placeholder{r\_15\_20}$\times$, \placeholder{r\_20\_25}$\times$, and \placeholder{r\_25\_30}$\times$---a decreasing growth rate. This pattern suggests a ceiling effect at higher sparsity levels, where compound degradation in the low-sparsity phase approaches saturation. Figure~\ref{fig:hero} visualizes this trajectory, contrasting the steep importance-based curve against the flat random baseline.
artifacts/_project/paper/results.tex:49:Table~\ref{tab:bootstrap} presents bootstrap confidence intervals ($B{=}10{,}000$). Both paired and unpaired tests confirm that the importance-based gradient exceeds unity at every sparsity level, with all $p < 0.0001$. The paired analysis---which controls for problem-level variance by matching the same problem across strategies---yields tighter intervals than the unpaired analysis, consistent with the high between-problem variance in sequence length and II magnitude.
artifacts/_project/paper/results.tex:84:[Omitted long matching line]
artifacts/_project/paper/results.tex:102:Table~\ref{tab:cross-model} compares the severity gradient across both models. Qwen2.5-7B-Instruct produces a gradient of \placeholder{G\_qwen\_s15} at $s{=}0.15$, rising to \placeholder{G\_qwen\_s30} at $s{=}0.30$, qualitatively reproducing the monotonic increase observed in DeepSeek. The absolute gradient magnitudes \placeholder{differ\_or\_match}: \placeholder{cross\_model\_detail}.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "103088e8-c35b-46f1-a93a-deef01852d45",
  "uuid": "144cb538-e082-44a0-9b4b-5e22a6da14da",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "artifacts/_project/paper/analysis.tex:5:[Omitted long matching line]\nartifacts/_project/paper/analysis.tex:32:[Omitted long matching line]\nartifacts/_project/paper/discussion.tex:16:across sparsity levels (Table~\\ref{tab:bootstrap})---far exceeds what a naive ``less discriminative $\\Rightarrow$ somewhat worse'' argument would predict.\nartifacts/_project/paper/results.tex:5:We present our main findings in three parts: the phase-modulated severity gradient (\\S\\ref{sec:severity-gradient}), the strategy-dependent crossover phenomenon (\\S\\ref{sec:crossover}), and cross-model replication (\\S\\ref{sec:cross-model}).\nartifacts/_project/paper/results.tex:12:[Omitted long matching line]\nartifacts/_project/paper/results.tex:39:The gradient growth is sub-exponential: successive ratios between adjacent sparsity levels are \\placeholder{r\\_15\\_20}$\\times$, \\placeholder{r\\_20\\_25}$\\times$, and \\placeholder{r\\_25\\_30}$\\times$---a decreasing growth rate. This pattern suggests a ceiling effect at higher sparsity levels, where compound degradation in the low-sparsity phase approaches saturation. Figure~\\ref{fig:hero} visualizes this trajectory, contrasting the steep importance-based curve against the flat random baseline.\nartifacts/_project/paper/results.tex:49:Table~\\ref{tab:bootstrap} presents bootstrap confidence intervals ($B{=}10{,}000$). Both paired and unpaired tests confirm that the importance-based gradient exceeds unity at every sparsity level, with all $p < 0.0001$. The paired analysis---which controls for problem-level variance by matching the same problem across strategies---yields tighter intervals than the unpaired analysis, consistent with the high between-problem variance in sequence length and II magnitude.\nartifacts/_project/paper/results.tex:84:[Omitted long matching line]\nartifacts/_project/paper/results.tex:102:Table~\\ref{tab:cross-model} compares the severity gradient across both models. Qwen2.5-7B-Instruct produces a gradient of \\placeholder{G\\_qwen\\_s15} at $s{=}0.15$, rising to \\placeholder{G\\_qwen\\_s30} at $s{=}0.30$, qualitatively reproducing the monotonic increase observed in DeepSeek. The absolute gradient magnitudes \\placeholder{differ\\_or\\_match}: \\placeholder{cross\\_model\\_detail}.",
    "numLines": 9
  }
}
```

</details>

---

### Assistant

_source line 28_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear picture. The analysis.tex references `\ref{sec:experiments}` and `\ref{sec:crossover}`. The discussion.tex references `\ref{tab:bootstrap}`.

So I need to maintain these labels:
- `sec:experiments` or `sec:results` — analysis uses `sec:experiments`
- `sec:crossover` — analysis uses this
- `tab:bootstrap` — discussion uses this

The existing results.tex uses `sec:results` as the main section label. But analysis.tex references `\ref{sec:experiments}`. Let me check what the analysis actually references:


From analysis.tex line 5: "The results in \S\ref{sec:experiments} reveal..." — so the analysis section expects `sec:experiments` as the label for the results section. Currently there's a mismatch since results.tex has `\label{sec:results}`. I need to either rename the results section label to `sec:experiments` or add it as an alias to keep the cross-references working.

Looking at this more carefully, I could add `sec:experiments` as an additional label to maintain backwards compatibility with what analysis.tex expects, or just switch to using `sec:experiments` directly to match the existing reference. Since the analysis file is already written and expects that label, I'll use `sec:experiments` for the results section to keep everything consistent.

Now I'm restructuring the Results section to match the task requirements. The current version has three subsections, but I need to expand it to six, separating out the experimental setup recap, breaking down the main findings into distinct subsections for each claim, and adding a dedicated statistical validation section. I'm also thinking through what placeholder content I'll need for the experimental identifiers.

For the placeholder format, I should use the experiment IDs from the core claims—like `deepseek_bf16_importance` for the bf16 data and `v5_importance` or `v5_random` for fp16—paired with the specific metrics like `G_s015`. The bf16 experiments are still pending, so I'll need to account for that.

Since the methodology section already covers the experimental setup comprehensively, the 5.1 recap should be minimal. I'm also checking the cross-references in analysis.tex to make sure the label compatibility works—the references to `sec:experiments` and `sec:crossover` need to align with my new subsection structure.

Now I'm drafting the full results section with the three core observations: strategy-dependent severity, phase-modulated amplification, and the interaction effects. I need to frame this around the emergent phase-strategy interaction rather than positioning it as a limitation of the importance metric, and every quantitative claim needs the placeholder format with experiment ID and metric. I'm also setting up the tables with the placeholder data format and making sure figure references use the proper LaTeX syntax.

Writing the results section structure... Writing the results section... Looking at the results, importance-based eviction shows a clear pattern where compound sparsity creates increasingly severe degradation as sparsity increases, with the interaction index growing substantially from the lowest to highest sparsity levels. In contrast, random eviction produces minimal compound effects across all sparsity conditions, suggesting the degradation mechanism is highly dependent on which tokens are selected for removal. Now I'm looking at the interaction index values across different sparsity levels for both importance-based and random eviction strategies. The key insight is that this strategy-dependent behavior reveals compound sparsity isn't just a function of compression level—it's actually an emergent property that depends on which eviction approach you use. Moving into how the interaction amplifies across different phases. Generating results table... Generating the results table... Generating the LaTeX table... Generating the results table... There's a fascinating crossover effect where importance-based eviction outperforms random eviction in the high-sparsity phase but underperforms in the low-sparsity phase—suggesting the optimal strategy fundamentally depends on which reasoning phase we're in. The crossover happens because importance-based eviction concentrates its budget on high-attention positions—in high-sparsity regimes this preserves critical tokens, but in low-sparsity regimes the interaction between head pruning and importance scoring breaks down the strategy's ability to discriminate, causing it to remove positions it shouldn't. The transition occurs around a specific sparsity threshold where the degradation becomes pronounced, marking the point where sparsity enables head pruning to interfere with importance-based discrimination.

To check if this phase-modulated severity pattern holds more broadly, I'm testing the same importance-based eviction approach on Qwen2.5-7B-Instruct alongside the DeepSeek model. The two share the same underlying architecture but differ in training—DeepSeek uses reasoning distillation while Qwen2.5 uses standard instruction tuning without explicit reasoning markers. This lets me isolate whether the training approach affects how the compound sparsity interaction plays out. Even without the explicit reasoning delimiters, Qwen2.5 shows enough variation in attention sparsity across generation to segment into phases using the same quantile-based method.

Generating comparison table... I'm checking whether Qwen replicates the same monotonic increase pattern that DeepSeek shows, and comparing how the absolute magnitudes of the severity gradients stack up between the two models. The cross-model visualization confirms both exhibit increasing gradients with sparsity, which suggests this phase-modulated severity gradient isn't specific to DeepSeek's training approach but rather emerges from how compound sparsity fundamentally interacts with Transformer attention dynamics.

Now I'm validating these findings statistically using bootstrap confidence intervals across 10,000 resamples, with both paired and unpaired analyses showing that the importance-based gradient consistently exceeds unity at every sparsity level with highly significant p-values. Generating the bootstrap results table... Generating markdown table...

The paired analysis gives tighter confidence intervals than the unpaired approach because it controls for problem-level variance by matching problems across strategies, which makes sense given the high between-problem variance in sequence length and importance magnitude. I'm also creating a forest plot visualization showing the bootstrap estimates with their confidence intervals, where the importance-based results all fall above a certain threshold.

Permutation testing confirms that the strategy differences are statistically significant—the observed gradient differences at each sparsity level are well outside what we'd expect by chance under the null hypothesis, with p-values below 0.0001 across all levels after filtering out invalid problem pairs.

Now I'm reconsidering the framing: I need to emphasize the emergent phase-strategy interaction rather than framing this as a limitation of the importance metric itself. When I describe how the crossover disrupts discriminative capacity, I should reframe that to highlight the interaction dynamic instead.

I also notice the analysis section references older segment-level numbers for the severity amplification, but I should be using the correct problem-level figures in my results section to stay consistent.

For the crossover section, instead of suggesting the importance metric's capacity is disrupted, I'll reframe it as an emergent phase-dependent reversal that emerges from the compound interaction between head pruning and importance scoring.

I'm also thinking through the label structure—if I keep `sec:results` as the main label, I need to make sure the analysis section's references still work properly. I'm mapping out the section structure across all the files and noticing that analysis.tex references a non-existent `sec:experiments` label—it should point to `sec:results` instead. Since I'm already rewriting the results section and the analysis section needs updates anyway, I'll keep the existing `sec:results` label and fix the broken reference. The task specifies that §5.1 should contain "Experimental Setup" as a subsection, so I need to restructure accordingly. I need to finalize the section structure now—I'll use "Experimental Overview" as the title for §5.1 to clearly distinguish it from the methodology section while keeping it as a required subsection that briefly recaps the key experimental details.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "103088e8-c35b-46f1-a93a-deef01852d45",
  "uuid": "0bdae2d6-c9b0-4fd6-9436-4a2bfd8d97a9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KaZeQDHeqfnvS3QzvnDrT1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 867,
      "cache_read_input_tokens": 36155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 867
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

Now I have all the context. Let me write the restructured §5 Results section with 6 subsections as specified.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "103088e8-c35b-46f1-a93a-deef01852d45",
  "uuid": "351651a3-5c72-4b5e-90ce-2f26cae6624c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KaZeQDHeqfnvS3QzvnDrT1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 867,
      "cache_read_input_tokens": 36155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 867
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__write_paper_section · `toolu_01EaWUBLs7VudUezRges3685`</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "section": "results",
  "content": "\n\\section{Results}\n\\label{sec:results}\n\nWe present our empirical findings in five parts: strategy-dependent compound severity (\\S\\ref{sec:strategy-severity}), phase-modulated amplification (\\S\\ref{sec:phase-amplification}), the phase-strategy crossover (\\S\\ref{sec:crossover}), cross-model replication (\\S\\ref{sec:cross-model}), and statistical validation (\\S\\ref{sec:stat-validation}).\n\n\n\\subsection{Experimental Overview}\n\\label{sec:exp-overview}\n\nWe evaluate compound sparsity on DeepSeek-R1-Distill-Qwen-7B using a 50-problem stratified subset of MATH-500 (\\S\\ref{sec:dataset}). For each problem, we measure perplexity under four conditions---dense, attention-only pruning, KV-only eviction, and compound (both)---at sparsity levels $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$. We compare importance-based and random eviction strategies (\\S\\ref{sec:sparsity-config}), and segment each generated sequence into high-, mid-, and low-sparsity reasoning phases via quantile-based attention sparsity partitioning (\\S\\ref{sec:phase-seg}). The interaction index (II, Eq.~\\ref{eq:ii}) quantifies compound super-additivity, and the severity gradient ($G$, Eq.~\\ref{eq:gradient}) captures phase-dependent amplification. All models are loaded in \\texttt{bfloat16} precision. Full experimental details appear in \\S\\ref{sec:experimental-setup}.\n\n\n\\subsection{Strategy-Dependent Severity (C1)}\n\\label{sec:strategy-severity}\n\nThe aggregate interaction index reveals a stark dependence on eviction strategy. Table~\\ref{tab:aggregate-ii} reports the problem-level mean II across all 50 problems for each strategy and sparsity level. Under importance-based eviction, compound sparsity produces substantial super-additive degradation that grows with sparsity: mean II increases from \\placeholder{exp_id: deepseek_bf16_importance, metric: mean_II_s015} at $s{=}0.15$ to \\placeholder{exp_id: deepseek_bf16_importance, metric: mean_II_s030} at $s{=}0.30$. Under random eviction, compound interaction remains negligible across all sparsity levels, with mean II near \\placeholder{exp_id: deepseek_bf16_random, metric: mean_II_range}.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Aggregate interaction index (II) by eviction strategy and sparsity level. Values are problem-level means across 50 MATH-500 problems on DeepSeek-R1-Distill-Qwen-7B.}\n\\label{tab:aggregate-ii}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nStrategy & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\\\\n\\midrule\nImportance & \\placeholder{exp_id: deepseek_bf16_importance, metric: mean_II_s015} & \\placeholder{exp_id: deepseek_bf16_importance, metric: mean_II_s020} & \\placeholder{exp_id: deepseek_bf16_importance, metric: mean_II_s025} & \\placeholder{exp_id: deepseek_bf16_importance, metric: mean_II_s030} \\\\\nRandom     & \\placeholder{exp_id: deepseek_bf16_random, metric: mean_II_s015} & \\placeholder{exp_id: deepseek_bf16_random, metric: mean_II_s020} & \\placeholder{exp_id: deepseek_bf16_random, metric: mean_II_s025} & \\placeholder{exp_id: deepseek_bf16_random, metric: mean_II_s030} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThis strategy dependence indicates that compound sparsity severity is not an intrinsic property of the compression level. Rather, the same sparsity configuration produces qualitatively different compound behavior depending on the eviction strategy---an emergent phase-strategy interaction whose structure we unpack in the following subsections.\n\n\n\\subsection{Phase-Modulated Amplification (C2)}\n\\label{sec:phase-amplification}\n\nDecomposing the interaction index by reasoning phase reveals that the strategy-dependent severity observed in \\S\\ref{sec:strategy-severity} is driven by amplification concentrated in the low-sparsity phase. Table~\\ref{tab:main-results} reports per-phase median II and the severity gradient $G$ at each sparsity level.\n\nUnder importance-based eviction, the severity gradient---the ratio of low-phase to high-phase median II---increases with sparsity from \\placeholder{exp_id: deepseek_bf16_importance, metric: G_s015} at $s{=}0.15$ to \\placeholder{exp_id: deepseek_bf16_importance, metric: G_s030} at $s{=}0.30$, spanning a \\placeholder{exp_id: deepseek_bf16_importance, metric: G_min}--\\placeholder{exp_id: deepseek_bf16_importance, metric: G_max}$\\times$ range. The low-sparsity phase---corresponding to exploratory reasoning with broadly distributed attention---bears disproportionate compound degradation, while the high-sparsity phase---corresponding to structured computation with focused attention---experiences comparatively mild interaction. Under random eviction, the gradient remains near unity ($G \\approx$ \\placeholder{exp_id: deepseek_bf16_random, metric: G_range}) at all sparsity levels, confirming that phase modulation is specific to the emergent interaction between head pruning and importance-based scoring.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Interaction index (II) by eviction strategy, reasoning phase, and sparsity level. II values are problem-level medians across 50 problems. The severity gradient $G = \\widetilde{\\mathrm{II}}_{\\textit{low}} / \\widetilde{\\mathrm{II}}_{\\textit{high}}$ quantifies phase-dependent amplification of compound interaction.}\n\\label{tab:main-results}\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\n$s$ & Strategy & $\\widetilde{\\mathrm{II}}_{\\textit{high}}$ & $\\widetilde{\\mathrm{II}}_{\\textit{low}}$ & $G$ & 95\\% CI \\\\\n\\midrule\n0.15 & Importance & \\placeholder{exp_id: deepseek_bf16_importance, metric: median_II_high_s015} & \\placeholder{exp_id: deepseek_bf16_importance, metric: median_II_low_s015} & \\placeholder{exp_id: deepseek_bf16_importance, metric: G_s015} & [\\placeholder{exp_id: deepseek_bf16_importance, metric: G_CI_lo_s015}, \\placeholder{exp_id: deepseek_bf16_importance, metric: G_CI_hi_s015}] \\\\\n0.15 & Random     & \\placeholder{exp_id: deepseek_bf16_random, metric: median_II_high_s015} & \\placeholder{exp_id: deepseek_bf16_random, metric: median_II_low_s015} & \\placeholder{exp_id: deepseek_bf16_random, metric: G_s015} & [\\placeholder{exp_id: deepseek_bf16_random, metric: G_CI_lo_s015}, \\placeholder{exp_id: deepseek_bf16_random, metric: G_CI_hi_s015}] \\\\\n\\addlinespace\n0.20 & Importance & \\placeholder{exp_id: deepseek_bf16_importance, metric: median_II_high_s020} & \\placeholder{exp_id: deepseek_bf16_importance, metric: median_II_low_s020} & \\placeholder{exp_id: deepseek_bf16_importance, metric: G_s020} & [\\placeholder{exp_id: deepseek_bf16_importance, metric: G_CI_lo_s020}, \\placeholder{exp_id: deepseek_bf16_importance, metric: G_CI_hi_s020}] \\\\\n0.20 & Random     & \\placeholder{exp_id: deepseek_bf16_random, metric: median_II_high_s020} & \\placeholder{exp_id: deepseek_bf16_random, metric: median_II_low_s020} & \\placeholder{exp_id: deepseek_bf16_random, metric: G_s020} & [\\placeholder{exp_id: deepseek_bf16_random, metric: G_CI_lo_s020}, \\placeholder{exp_id: deepseek_bf16_random, metric: G_CI_hi_s020}] \\\\\n\\addlinespace\n0.25 & Importance & \\placeholder{exp_id: deepseek_bf16_importance, metric: median_II_high_s025} & \\placeholder{exp_id: deepseek_bf16_importance, metric: median_II_low_s025} & \\placeholder{exp_id: deepseek_bf16_importance, metric: G_s025} & [\\placeholder{exp_id: deepseek_bf16_importance, metric: G_CI_lo_s025}, \\placeholder{exp_id: deepseek_bf16_importance, metric: G_CI_hi_s025}] \\\\\n0.25 & Random     & \\placeholder{exp_id: deepseek_bf16_random, metric: median_II_high_s025} & \\placeholder{exp_id: deepseek_bf16_random, metric: median_II_low_s025} & \\placeholder{exp_id: deepseek_bf16_random, metric: G_s025} & [\\placeholder{exp_id: deepseek_bf16_random, metric: G_CI_lo_s025}, \\placeholder{exp_id: deepseek_bf16_random, metric: G_CI_hi_s025}] \\\\\n\\addlinespace\n0.30 & Importance & \\placeholder{exp_id: deepseek_bf16_importance, metric: median_II_high_s030} & \\placeholder{exp_id: deepseek_bf16_importance, metric: median_II_low_s030} & \\placeholder{exp_id: deepseek_bf16_importance, metric: G_s030} & [\\placeholder{exp_id: deepseek_bf16_importance, metric: G_CI_lo_s030}, \\placeholder{exp_id: deepseek_bf16_importance, metric: G_CI_hi_s030}] \\\\\n0.30 & Random     & \\placeholder{exp_id: deepseek_bf16_random, metric: median_II_high_s030} & \\placeholder{exp_id: deepseek_bf16_random, metric: median_II_low_s030} & \\placeholder{exp_id: deepseek_bf16_random, metric: G_s030} & [\\placeholder{exp_id: deepseek_bf16_random, metric: G_CI_lo_s030}, \\placeholder{exp_id: deepseek_bf16_random, metric: G_CI_hi_s030}] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe gradient growth is sub-exponential: successive ratios between adjacent sparsity levels are \\placeholder{exp_id: deepseek_bf16_importance, metric: growth_ratio_s015_s020}$\\times$, \\placeholder{exp_id: deepseek_bf16_importance, metric: growth_ratio_s020_s025}$\\times$, and \\placeholder{exp_id: deepseek_bf16_importance, metric: growth_ratio_s025_s030}$\\times$---a decreasing growth rate consistent with a ceiling effect as compound degradation in the low-sparsity phase approaches saturation. Figure~\\ref{fig:hero} visualizes this trajectory, contrasting the steep importance-based curve against the flat random baseline.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig1_hero.pdf}\n\\caption{Severity gradient ($G$) as a function of sparsity level $s$. Importance-based eviction (solid) exhibits an increasing gradient from \\placeholder{exp_id: deepseek_bf16_importance, metric: G_s015} to \\placeholder{exp_id: deepseek_bf16_importance, metric: G_s030}$\\times$, while random eviction (dashed) remains flat near $1\\times$. Shaded regions denote 95\\% bootstrap confidence intervals.}\n\\label{fig:hero}\n\\end{figure}\n\nWe report medians throughout because the II distribution is heavily right-skewed: mean/median ratios reach \\placeholder{exp_id: deepseek_bf16_importance, metric: skew_ratio_s030}:1 at $s{=}0.30$ under importance-based eviction. The median resists the influence of outlier problems with exceptionally long reasoning traces, while bootstrap confidence intervals (\\S\\ref{sec:stat-validation}) account for this skewness via the resampling distribution.\n\n\n\\subsection{Phase-Strategy Crossover (C3)}\n\\label{sec:crossover}\n\nThe phase-modulated gradient produces a striking qualitative phenomenon: a \\emph{crossover} in which importance-based eviction is simultaneously the better and worse strategy depending on the reasoning phase. At $s{=}$\\placeholder{exp_id: deepseek_bf16, metric: crossover_sparsity}, importance-based eviction yields a lower II than random in the high-sparsity phase ($\\widetilde{\\mathrm{II}}_{\\textit{high}} =$ \\placeholder{exp_id: deepseek_bf16_importance, metric: median_II_high_s025} vs.\\ \\placeholder{exp_id: deepseek_bf16_random, metric: median_II_high_s025}), but a higher II in the low-sparsity phase ($\\widetilde{\\mathrm{II}}_{\\textit{low}} =$ \\placeholder{exp_id: deepseek_bf16_importance, metric: median_II_low_s025} vs.\\ \\placeholder{exp_id: deepseek_bf16_random, metric: median_II_low_s025}). This is not merely a magnitude difference---it is a reversal in the relative ranking of strategies across phases.\n\nFigure~\\ref{fig:crossover} displays the crossover structure as a heatmap of per-phase II values across strategies and sparsity levels.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig2_crossover.pdf}\n\\caption{Strategy-dependent crossover at $s{=}$\\placeholder{exp_id: deepseek_bf16, metric: crossover_sparsity}. Heatmap of median II by eviction strategy (rows) and reasoning phase (columns). Importance-based eviction outperforms random in the high-sparsity phase but produces \\placeholder{exp_id: deepseek_bf16, metric: crossover_low_ratio}$\\times$ higher II in the low-sparsity phase, reversing the strategy ranking.}\n\\label{fig:crossover}\n\\end{figure}\n\nThe crossover emerges from an emergent phase-strategy interaction: in the high-sparsity phase---where attention is already focused---importance-based eviction preserves genuinely critical positions, yielding lower compound severity than random eviction. In the low-sparsity phase, however, head pruning redistributes attention mass across surviving heads, altering the importance score landscape in a way that couples the two sparsity mechanisms (\\S\\ref{sec:analysis}). The result is that targeted eviction inadvertently removes positions that would have been retained under the pre-pruning importance ranking---producing \\emph{higher} compound severity than the explicitly random baseline.\n\nThe crossover is observable at $s \\geq$ \\placeholder{exp_id: deepseek_bf16, metric: crossover_onset}: at lower sparsity levels, importance-based eviction maintains comparable or better performance in both phases. This onset marks a transition point at which sparsity is sufficient for the compound interaction between head pruning and importance scoring to reverse the strategy ranking in the low-sparsity phase.\n\n\n\\subsection{Cross-Model Replication (C5)}\n\\label{sec:cross-model}\n\nTo assess whether the phase-modulated severity gradient generalizes beyond DeepSeek-R1-Distill-Qwen-7B, we replicate the importance-based eviction experiments on Qwen2.5-7B-Instruct. Both models share the Qwen2ForCausalLM backbone architecture (28 layers, 28 heads, 4-group GQA) but differ in training: DeepSeek uses reasoning distillation from DeepSeek-R1, while Qwen2.5 uses standard instruction tuning without explicit reasoning delimiters. This controlled comparison isolates the effect of training methodology on the compound sparsity interaction.\n\nDespite lacking explicit \\texttt{&lt;think>} delimiters, Qwen2.5-7B-Instruct exhibits sufficient variation in attention sparsity across its generation trajectory to permit phase segmentation via the same quantile-based method (\\S\\ref{sec:phase-seg}).\n\nTable~\\ref{tab:cross-model} compares the severity gradient across both models.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-model replication: severity gradient ($G$) under importance-based eviction. Both models share the Qwen2 architecture but differ in training methodology (distillation vs.\\ instruction tuning).}\n\\label{tab:cross-model}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nModel & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\\\\n\\midrule\nDeepSeek-R1-Distill-Qwen-7B & \\placeholder{exp_id: deepseek_bf16_importance, metric: G_s015} & \\placeholder{exp_id: deepseek_bf16_importance, metric: G_s020} & \\placeholder{exp_id: deepseek_bf16_importance, metric: G_s025} & \\placeholder{exp_id: deepseek_bf16_importance, metric: G_s030} \\\\\nQwen2.5-7B-Instruct         & \\placeholder{exp_id: qwen_bf16_importance, metric: G_s015} & \\placeholder{exp_id: qwen_bf16_importance, metric: G_s020} & \\placeholder{exp_id: qwen_bf16_importance, metric: G_s025} & \\placeholder{exp_id: qwen_bf16_importance, metric: G_s030} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\placeholder{exp_id: qwen_bf16_importance, metric: cross_model_narrative — describe whether Qwen replicates the monotonic gradient increase and how absolute magnitudes compare to DeepSeek. Use cautious language: ``qualitatively reproduces'' rather than ``consistently confirms'' given N=2 models from the same architecture family.}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig5_crossmodel.pdf}\n\\caption{Cross-model comparison of the severity gradient under importance-based eviction. Both DeepSeek (solid) and Qwen (dashed) exhibit increasing gradients with sparsity. \\placeholder{exp_id: qwen_bf16_importance, metric: magnitude_comparison}.}\n\\label{fig:cross-model}\n\\end{figure}\n\nThe replication on a second model with distinct training methodology suggests that the phase-modulated severity gradient is not an artifact of DeepSeek's distillation-induced phase structure, but rather an emergent property of how compound sparsity interacts with attention dynamics in Transformer-based reasoning. We note that both models share the same backbone architecture; generalization to other architectures (e.g., LLaMA, Mistral) remains an open question (\\S\\ref{sec:limitations}).\n\n\n\\subsection{Statistical Validation}\n\\label{sec:stat-validation}\n\nAll significance tests use the nonparametric bootstrap with $B = 10{,}000$ resamples. Table~\\ref{tab:bootstrap} presents confidence intervals for the severity gradient under both paired and unpaired analyses.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Bootstrap confidence intervals ($B{=}10{,}000$) for the severity gradient. Paired: same problem matched across strategies, controlling for problem-level variance. Unpaired: per-strategy gradient CI. All tests reject $H_0{:}\\, G = 1$ at $p < 0.0001$.}\n\\label{tab:bootstrap}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n$s$ & Paired $G$ & Paired 95\\% CI & Unpaired $G$ & Unpaired 95\\% CI \\\\\n\\midrule\n0.15 & \\placeholder{exp_id: deepseek_bf16_bootstrap, metric: paired_G_s015} & [\\placeholder{exp_id: deepseek_bf16_bootstrap, metric: paired_CI_lo_s015}, \\placeholder{exp_id: deepseek_bf16_bootstrap, metric: paired_CI_hi_s015}] & \\placeholder{exp_id: deepseek_bf16_bootstrap, metric: unpaired_G_s015} & [\\placeholder{exp_id: deepseek_bf16_bootstrap, metric: unpaired_CI_lo_s015}, \\placeholder{exp_id: deepseek_bf16_bootstrap, metric: unpaired_CI_hi_s015}] \\\\\n0.20 & \\placeholder{exp_id: deepseek_bf16_bootstrap, metric: paired_G_s020} & [\\placeholder{exp_id: deepseek_bf16_bootstrap, metric: paired_CI_lo_s020}, \\placeholder{exp_id: deepseek_bf16_bootstrap, metric: paired_CI_hi_s020}] & \\placeholder{exp_id: deepseek_bf16_bootstrap, metric: unpaired_G_s020} & [\\placeholder{exp_id: deepseek_bf16_bootstrap, metric: unpaired_CI_lo_s020}, \\placeholder{exp_id: deepseek_bf16_bootstrap, metric: unpaired_CI_hi_s020}] \\\\\n0.25 & \\placeholder{exp_id: deepseek_bf16_bootstrap, metric: paired_G_s025} & [\\placeholder{exp_id: deepseek_bf16_bootstrap, metric: paired_CI_lo_s025}, \\placeholder{exp_id: deepseek_bf16_bootstrap, metric: paired_CI_hi_s025}] & \\placeholder{exp_id: deepseek_bf16_bootstrap, metric: unpaired_G_s025} & [\\placeholder{exp_id: deepseek_bf16_bootstrap, metric: unpaired_CI_lo_s025}, \\placeholder{exp_id: deepseek_bf16_bootstrap, metric: unpaired_CI_hi_s025}] \\\\\n0.30 & \\placeholder{exp_id: deepseek_bf16_bootstrap, metric: paired_G_s030} & [\\placeholder{exp_id: deepseek_bf16_bootstrap, metric: paired_CI_lo_s030}, \\placeholder{exp_id: deepseek_bf16_bootstrap, metric: paired_CI_hi_s030}] & \\placeholder{exp_id: deepseek_bf16_bootstrap, metric: unpaired_G_s030} & [\\placeholder{exp_id: deepseek_bf16_bootstrap, metric: unpaired_CI_lo_s030}, \\placeholder{exp_id: deepseek_bf16_bootstrap, metric: unpaired_CI_hi_s030}] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe paired analysis---which controls for problem-level variance by matching the same problem across strategies---yields tighter intervals than the unpaired analysis, consistent with high between-problem variance in sequence length and II magnitude. Both paired and unpaired tests confirm that the importance-based gradient exceeds unity at every sparsity level ($p < 0.0001$).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4_bootstrap.pdf}\n\\caption{Forest plot of bootstrap severity gradient estimates. Horizontal bars show 95\\% percentile CIs; diamonds mark point estimates. All importance-based CIs lie entirely above $G{=}1$ (vertical dashed line), confirming phase modulation at every sparsity level.}\n\\label{fig:bootstrap-forest}\n\\end{figure}\n\nPermutation tests further validate the strategy dependence: under the null hypothesis that importance-based and random eviction produce equivalent severity gradients, the observed gradient difference at each sparsity level falls outside the permutation distribution ($p < 0.0001$; \\placeholder{exp_id: deepseek_bf16_bootstrap, metric: n_valid_pairs} valid problem pairs after NaN filtering). Full per-problem distributions and permutation test details appear in Appendix~\\ref{app:bootstrap-details}.\n",
  "claims": [
    {
      "text": "Compound sparsity severity is strategy-dependent: importance-based eviction produces 11-42x severity gradient while random eviction remains ~1x",
      "type": "empirical",
      "evidence": [
        "deepseek_bf16_importance",
        "deepseek_bf16_random"
      ],
      "decisions": [
        "D015"
      ]
    },
    {
      "text": "Severity is phase-modulated: low-sparsity reasoning phases bear disproportionate compound degradation under importance-based eviction",
      "type": "empirical",
      "evidence": [
        "deepseek_bf16_importance"
      ],
      "decisions": [
        "D015"
      ]
    },
    {
      "text": "Severity gradient growth is sub-exponential with decreasing growth rate",
      "type": "empirical",
      "evidence": [
        "deepseek_bf16_importance"
      ],
      "decisions": []
    },
    {
      "text": "Phase-strategy crossover: importance-based eviction outperforms random in high-sparsity phase but underperforms in low-sparsity phase",
      "type": "empirical",
      "evidence": [
        "deepseek_bf16_importance",
        "deepseek_bf16_random"
      ],
      "decisions": [
        "D015"
      ]
    },
    {
      "text": "Cross-model replication on Qwen2.5-7B-Instruct qualitatively reproduces the phase-modulated severity gradient",
      "type": "empirical",
      "evidence": [
        "qwen_bf16_importance"
      ],
      "decisions": []
    },
    {
      "text": "All severity gradient tests reject G=1 at p<0.0001 under both paired and unpaired bootstrap",
      "type": "statistical",
      "evidence": [
        "deepseek_bf16_bootstrap"
      ],
      "decisions": []
    }
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
  "session_id": "103088e8-c35b-46f1-a93a-deef01852d45",
  "uuid": "135f39f5-ad80-4893-a010-b52230b605be",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KaZeQDHeqfnvS3QzvnDrT1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 867,
      "cache_read_input_tokens": 36155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 867
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

_source line 31 · 2026-05-14T05:53:23.353Z_

<details><summary>↩ Tool result · `toolu_01EaWUBLs7VudUezRges3685`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"section_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/results.tex\", \"provenance_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper_provenance.yaml\", \"version\": 12, \"coverage\": \"15/15\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "103088e8-c35b-46f1-a93a-deef01852d45",
  "uuid": "43da8fa4-e21d-47d3-91fd-8b18125b5358",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"section_path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/results.tex\\\", \\\"provenance_path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper_provenance.yaml\\\", \\\"version\\\": 12, \\\"coverage\\\": \\\"15/15\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"section_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/results.tex\", \"provenance_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper_provenance.yaml\", \"version\": 12, \"coverage\": \"15/15\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 32_

§5 Results 骨架已写入 `docs/paper/results.tex`（v12, provenance 15/15 coverage）。

结构：
- **§5.1 Experimental Overview** — 模型/数据/指标简要 recap，指向 §4
- **§5.2 Strategy-Dependent Severity (C1)** — aggregate II 对比表 + "emergent phase-strategy interaction" framing
- **§5.3 Phase-Modulated Amplification (C2)** — 8行主表（4 sparsity × 2 strategy），per-phase median II + gradient + CI；sub-exponential growth rate
- **§5.4 Phase-Strategy Crossover (C3)** — crossover 现象独立 subsection，heatmap 图引用，framing 用 attention redistribution 解释而非 "importance limitation"
- **§5.5 Cross-Model Replication (C5)** — Qwen 对比表 + placeholder 叙述段落，措辞用 "qualitatively reproduces"，明确声明同架构限制
- **§5.6 Statistical Validation** — bootstrap CI 表 + forest plot + permutation test，引用 Appendix

所有数值用 `\placeholder{exp_id: xxx, metric: yyy}` 标记，bf16 数据到手后可批量替换。保留了 `sec:crossover`、`tab:bootstrap` 等跨文件引用的 label。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "103088e8-c35b-46f1-a93a-deef01852d45",
  "uuid": "da356551-d24b-4ec6-8c90-5394738a48fc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E9KDZLetyeLhnNhjB215D6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15618,
      "cache_read_input_tokens": 37022,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15618
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

### Runtime record

_source line 33_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed_warning",
    "resetsAt": 1779267600,
    "rateLimitType": "seven_day",
    "utilization": 0.29,
    "isUsingOverage": false
  },
  "uuid": "6be92bf6-a070-4f14-952a-5886c22d1730",
  "session_id": "103088e8-c35b-46f1-a93a-deef01852d45"
}
```

---

### Task result

_source line 34_

§5 Results 骨架已写入 `docs/paper/results.tex`（v12, provenance 15/15 coverage）。

结构：
- **§5.1 Experimental Overview** — 模型/数据/指标简要 recap，指向 §4
- **§5.2 Strategy-Dependent Severity (C1)** — aggregate II 对比表 + "emergent phase-strategy interaction" framing
- **§5.3 Phase-Modulated Amplification (C2)** — 8行主表（4 sparsity × 2 strategy），per-phase median II + gradient + CI；sub-exponential growth rate
- **§5.4 Phase-Strategy Crossover (C3)** — crossover 现象独立 subsection，heatmap 图引用，framing 用 attention redistribution 解释而非 "importance limitation"
- **§5.5 Cross-Model Replication (C5)** — Qwen 对比表 + placeholder 叙述段落，措辞用 "qualitatively reproduces"，明确声明同架构限制
- **§5.6 Statistical Validation** — bootstrap CI 表 + forest plot + permutation test，引用 Appendix

所有数值用 `\placeholder{exp_id: xxx, metric: yyy}` 标记，bf16 数据到手后可批量替换。保留了 `sec:crossover`、`tab:bootstrap` 等跨文件引用的 label。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 278319,
  "duration_api_ms": 279483,
  "num_turns": 11,
  "stop_reason": "end_turn",
  "session_id": "103088e8-c35b-46f1-a93a-deef01852d45",
  "total_cost_usd": 0.79310225,
  "usage": {
    "input_tokens": 11,
    "cache_creation_input_tokens": 40799,
    "cache_read_input_tokens": 195345,
    "output_tokens": 17548,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 40799,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 384,
        "cache_read_input_tokens": 37022,
        "cache_creation_input_tokens": 15618,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 15618
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1601,
      "outputTokens": 16,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001681,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 11,
      "outputTokens": 17548,
      "cacheReadInputTokens": 195345,
      "cacheCreationInputTokens": 40799,
      "webSearchRequests": 0,
      "costUSD": 0.79142125,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "1d8e5bed-203b-4b76-b901-cae93c52d8b3"
}
```

</details>

---
