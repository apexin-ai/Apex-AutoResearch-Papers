# writing analysis skeleton

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 36
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/workers/worker_writing_analysis-skeleton_20260514T054050.log`
- **Structured JSON:** [`1008647b26d32097603e.json`](../../sessions/10/1008647b26d32097603e.json)

## Before a recorded user message

36 recorded events

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
  "session_id": "4ff71685-85e8-4572-b90c-68572f81a6a0",
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
    "mcp__agent-ml-research__edit_paper_section",
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
  "uuid": "b1952ff5-e0ce-4f59-a2cb-cbb113f946dc",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/memory/"
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
    "resetsAt": 1778742000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "3f2139a5-1eab-46c5-9de9-a761af6f9fef",
  "session_id": "4ff71685-85e8-4572-b90c-68572f81a6a0"
}
```

---

### Assistant

_source line 4_

I'll start by reading the paper framing document and checking existing paper sections for style/notation consistency.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4ff71685-85e8-4572-b90c-68572f81a6a0",
  "uuid": "a5e90f7c-feeb-46b1-965f-f3c244e75ed5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U6hhXUkz6g62nBtJzf1UNN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12280,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12280
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_014YtarjZJcfDkucMzCdjGKu`</summary>

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
  "session_id": "4ff71685-85e8-4572-b90c-68572f81a6a0",
  "uuid": "23655490-5c39-4443-936d-eb5110be60e3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U6hhXUkz6g62nBtJzf1UNN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12280,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12280
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

_source line 6 · 2026-05-14T05:41:02.417Z_

<details><summary>↩ Tool result · `toolu_014YtarjZJcfDkucMzCdjGKu`</summary>

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
  "session_id": "4ff71685-85e8-4572-b90c-68572f81a6a0",
  "uuid": "8b5b12f7-7aa7-47a2-93f5-a041a928f894",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__write_paper_section"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__write_paper_section",
    "total_deferred_tools": 24
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Let me read the paper framing document and check existing paper sections for style consistency.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4ff71685-85e8-4572-b90c-68572f81a6a0",
  "uuid": "7759b4f0-256c-4923-a3c9-65a763c16a8b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QXJZfDk1LKCTn535AzSL2R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 869,
      "cache_read_input_tokens": 23727,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 869
      },
      "output_tokens": 42,
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01QkDHJkWkXqHRQrzDpmWi25`</summary>

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
  "session_id": "4ff71685-85e8-4572-b90c-68572f81a6a0",
  "uuid": "133167fb-f2e4-447e-b313-fdbf7cecd3f4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QXJZfDk1LKCTn535AzSL2R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 869,
      "cache_read_input_tokens": 23727,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 869
      },
      "output_tokens": 42,
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

_source line 9 · 2026-05-14T05:41:08.675Z_

<details><summary>↩ Tool result · `toolu_01QkDHJkWkXqHRQrzDpmWi25`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper_framing.md\", \"content\": \"# Paper Framing — Phase-Gated Compound Sparsity\\n\\n> 最后更新: 2026-05-14 | 维护者: Director\\n\\n## Core Insight\\n\\nCompound sparsity（attention head pruning + KV cache eviction）的 severity 不是固定常数——它是 eviction strategy 和 reasoning phase 交互的涌现属性。Importance-based eviction 在 low-sparsity reasoning phase 产生 12-75× severity amplification，而 random eviction 保持 ~1× 平坦。这一发现挑战了 compound degradation 均匀分布的隐含假设。\\n\\n## Narrative Arc\\n\\nCompound sparsity 是高效 LLM 推理的实用部署需求，但 prior work（SparK, Ada-KV, SLiM）将 compound interaction 视为均匀超可加。我们发现 severity 是 strategy × phase 交互的涌现属性：importance eviction 在 distributed-attention phase 剧烈放大 compound degradation（gradient 12-75×），而 random eviction 在所有 phase 保持平坦（~1×）。我们通过 entropy-discrimination collapse 机制解释这一现象：head pruning → attention 重分布 → importance score 的判别力崩塌 → importance eviction 退化为有偏伪随机。这一发现为 phase-aware sparsity allocation 提供了动机。\\n\\n**Framing 硬约束（D015）**：\\n- MUST: \\\"emergent phase-strategy interaction\\\"\\n- MUST NOT: \\\"importance metric limitation / importance is broken\\\"\\n\\n## Core Claims\\n\\n| ID | Claim | Status | Key Evidence |\\n|----|-------|--------|-------------|\\n| C1 | Compound sparsity severity is strategy-dependent | confirmed | importance gradient 12-75× vs random ~1× |\\n| C2 | Severity is phase-modulated (amplified in low-sparsity phase) | confirmed | low phase >> high phase at all 4 sparsity levels; monotonic increase 12.8→28.7→52.9→74.9 |\\n| C3 | Phase-strategy crossover exists | confirmed | s=0.25: importance high_phase=0.584 < random=3.002, importance low_phase=30.903 > random=2.915 |\\n| C4 | Entropy-discrimination collapse explains the mechanism | partially_confirmed | Conceptual argument solid; empirical attention entropy data not yet collected |\\n| C5 | Finding generalizes across model families | pending | Qwen2.5-7B-Instruct experiments in progress |\\n| C6 | Severity gradient is sub-exponential | confirmed | Growth rate decreasing: 2.24×→1.84×→1.42× |\\n\\n## Anticipated Reviewer Concerns\\n\\n### RC1: Generalizability — 7B models only, single benchmark\\n- **预期质疑**: \\\"Results on two 7B models and MATH-500 only. How do we know this generalizes to larger models or other reasoning tasks?\\\"\\n- **应对**: Cross-model replication (DeepSeek + Qwen, 不同架构血统) 是第一层防御。MATH-500 是 standard benchmark。Limitations 明确声明 scale 限制。机制解释 (entropy-discrimination collapse) 是 architecture-agnostic 的，原则上适用于任何 attention-based model。\\n- **实验支撑**: C5 (Qwen cross-model), 若需加强可扩展到更多模型\\n\\n### RC2: Mechanism — entropy-discrimination collapse 缺乏直接测量\\n- **预期质疑**: \\\"The mechanism is conceptual. Where is the empirical evidence for entropy increase and discrimination collapse?\\\"\\n- **应对**: 如果有 GPU 预算，可以直接测量 pruned vs unpruned 的 attention entropy 和 importance score 分布。目前 C4 status = partially_confirmed，需要决定是否投入 GPU 时间做 direct measurement。\\n- **实验支撑**: 可选 ablation：测量 attention entropy pre/post pruning × phase\\n\\n### RC3: Practical impact — 没有 throughput 数据\\n- **预期质疑**: \\\"No wall-clock or throughput measurements. Is the severity amplification reflected in actual inference speed?\\\"\\n- **应对**: 本文定位是 empirical finding paper（发现 + 机制解释），不是 method paper。Throughput 不是 claim 的一部分。Discussion 中明确 phase-gated controller 作为 future direction。\\n- **实验支撑**: 不需要额外实验\\n\\n### RC4: Statistical rigor — bootstrap 是否足够\\n- **预期质疑**: \\\"Per-problem bootstrap with 50 problems — sufficient sample size?\\\"\\n- **应对**: B=10000 iterations, all p=0.0000, CI 不跨零。50 problems 的 paired bootstrap 统计效力已充分。可在 appendix 补充 per-problem 分布图。\\n- **实验支撑**: 已完成，fig4_bootstrap\\n\\n### RC5: Novelty — prior work 是否已覆盖 phase-dependent sparsity\\n- **预期质疑**: \\\"ThinKV and phase-aware methods already consider phase. What's new?\\\"\\n- **应对**: Prior work 在单轴上分析 phase（ThinKV: phase-aware eviction）或 compound（SparK: joint compression）。没有工作同时分析 compound × phase × strategy 的三维交互。Crossover 现象（同一 strategy 在不同 phase 方向反转）是全新发现。\\n- **实验支撑**: C3 (crossover), Related Work §2 的 gap 分析\\n\\n## Paper Positioning\\n\\n**类型**: Empirical finding paper（非 method paper）\\n**核心贡献**:\\n1. 发现 compound sparsity severity 的 strategy × phase 交互\\n2. 量化 severity gradient（12-75×）和 crossover 现象\\n3. 提出 entropy-discrimination collapse 机制解释\\n4. Cross-model replication 验证泛化性\\n\\n**投稿目标**: EMNLP 2026 ARR, deadline 2026-05-25\\n\", \"total_chars\": 4119, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4ff71685-85e8-4572-b90c-68572f81a6a0",
  "uuid": "1f896524-cb62-43b5-ab6a-9b1d4224b265",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing — Phase-Gated Compound Sparsity\\\\n\\\\n> 最后更新: 2026-05-14 | 维护者: Director\\\\n\\\\n## Core Insight\\\\n\\\\nCompound sparsity（attention head pruning + KV cache eviction）的 severity 不是固定常数——它是 eviction strategy 和 reasoning phase 交互的涌现属性。Importance-based eviction 在 low-sparsity reasoning phase 产生 12-75× severity amplification，而 random eviction 保持 ~1× 平坦。这一发现挑战了 compound degradation 均匀分布的隐含假设。\\\\n\\\\n## Narrative Arc\\\\n\\\\nCompound sparsity 是高效 LLM 推理的实用部署需求，但 prior work（SparK, Ada-KV, SLiM）将 compound interaction 视为均匀超可加。我们发现 severity 是 strategy × phase 交互的涌现属性：importance eviction 在 distributed-attention phase 剧烈放大 compound degradation（gradient 12-75×），而 random eviction 在所有 phase 保持平坦（~1×）。我们通过 entropy-discrimination collapse 机制解释这一现象：head pruning → attention 重分布 → importance score 的判别力崩塌 → importance eviction 退化为有偏伪随机。这一发现为 phase-aware sparsity allocation 提供了动机。\\\\n\\\\n**Framing 硬约束（D015）**：\\\\n- MUST: \\\\\\\"emergent phase-strategy interaction\\\\\\\"\\\\n- MUST NOT: \\\\\\\"importance metric limitation / importance is broken\\\\\\\"\\\\n\\\\n## Core Claims\\\\n\\\\n| ID | Claim | Status | Key Evidence |\\\\n|----|-------|--------|-------------|\\\\n| C1 | Compound sparsity severity is strategy-dependent | confirmed | importance gradient 12-75× vs random ~1× |\\\\n| C2 | Severity is phase-modulated (amplified in low-sparsity phase) | confirmed | low phase >> high phase at all 4 sparsity levels; monotonic increase 12.8→28.7→52.9→74.9 |\\\\n| C3 | Phase-strategy crossover exists | confirmed | s=0.25: importance high_phase=0.584 < random=3.002, importance low_phase=30.903 > random=2.915 |\\\\n| C4 | Entropy-discrimination collapse explains the mechanism | partially_confirmed | Conceptual argument solid; empirical attention entropy data not yet collected |\\\\n| C5 | Finding generalizes across model families | pending | Qwen2.5-7B-Instruct experiments in progress |\\\\n| C6 | Severity gradient is sub-exponential | confirmed | Growth rate decreasing: 2.24×→1.84×→1.42× |\\\\n\\\\n## Anticipated Reviewer Concerns\\\\n\\\\n### RC1: Generalizability — 7B models only, single benchmark\\\\n- **预期质疑**: \\\\\\\"Results on two 7B models and MATH-500 only. How do we know this generalizes to larger models or other reasoning tasks?\\\\\\\"\\\\n- **应对**: Cross-model replication (DeepSeek + Qwen, 不同架构血统) 是第一层防御。MATH-500 是 standard benchmark。Limitations 明确声明 scale 限制。机制解释 (entropy-discrimination collapse) 是 architecture-agnostic 的，原则上适用于任何 attention-based model。\\\\n- **实验支撑**: C5 (Qwen cross-model), 若需加强可扩展到更多模型\\\\n\\\\n### RC2: Mechanism — entropy-discrimination collapse 缺乏直接测量\\\\n- **预期质疑**: \\\\\\\"The mechanism is conceptual. Where is the empirical evidence for entropy increase and discrimination collapse?\\\\\\\"\\\\n- **应对**: 如果有 GPU 预算，可以直接测量 pruned vs unpruned 的 attention entropy 和 importance score 分布。目前 C4 status = partially_confirmed，需要决定是否投入 GPU 时间做 direct measurement。\\\\n- **实验支撑**: 可选 ablation：测量 attention entropy pre/post pruning × phase\\\\n\\\\n### RC3: Practical impact — 没有 throughput 数据\\\\n- **预期质疑**: \\\\\\\"No wall-clock or throughput measurements. Is the severity amplification reflected in actual inference speed?\\\\\\\"\\\\n- **应对**: 本文定位是 empirical finding paper（发现 + 机制解释），不是 method paper。Throughput 不是 claim 的一部分。Discussion 中明确 phase-gated controller 作为 future direction。\\\\n- **实验支撑**: 不需要额外实验\\\\n\\\\n### RC4: Statistical rigor — bootstrap 是否足够\\\\n- **预期质疑**: \\\\\\\"Per-problem bootstrap with 50 problems — sufficient sample size?\\\\\\\"\\\\n- **应对**: B=10000 iterations, all p=0.0000, CI 不跨零。50 problems 的 paired bootstrap 统计效力已充分。可在 appendix 补充 per-problem 分布图。\\\\n- **实验支撑**: 已完成，fig4_bootstrap\\\\n\\\\n### RC5: Novelty — prior work 是否已覆盖 phase-dependent sparsity\\\\n- **预期质疑**: \\\\\\\"ThinKV and phase-aware methods already consider phase. What's new?\\\\\\\"\\\\n- **应对**: Prior work 在单轴上分析 phase（ThinKV: phase-aware eviction）或 compound（SparK: joint compression）。没有工作同时分析 compound × phase × strategy 的三维交互。Crossover 现象（同一 strategy 在不同 phase 方向反转）是全新发现。\\\\n- **实验支撑**: C3 (crossover), Related Work §2 的 gap 分析\\\\n\\\\n## Paper Positioning\\\\n\\\\n**类型**: Empirical finding paper（非 method paper）\\\\n**核心贡献**:\\\\n1. 发现 compound sparsity severity 的 strategy × phase 交互\\\\n2. 量化 severity gradient（12-75×）和 crossover 现象\\\\n3. 提出 entropy-discrimination collapse 机制解释\\\\n4. Cross-model replication 验证泛化性\\\\n\\\\n**投稿目标**: EMNLP 2026 ARR, deadline 2026-05-25\\\\n\\\", \\\"total_chars\\\": 4119, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper_framing.md\", \"content\": \"# Paper Framing — Phase-Gated Compound Sparsity\\n\\n> 最后更新: 2026-05-14 | 维护者: Director\\n\\n## Core Insight\\n\\nCompound sparsity（attention head pruning + KV cache eviction）的 severity 不是固定常数——它是 eviction strategy 和 reasoning phase 交互的涌现属性。Importance-based eviction 在 low-sparsity reasoning phase 产生 12-75× severity amplification，而 random eviction 保持 ~1× 平坦。这一发现挑战了 compound degradation 均匀分布的隐含假设。\\n\\n## Narrative Arc\\n\\nCompound sparsity 是高效 LLM 推理的实用部署需求，但 prior work（SparK, Ada-KV, SLiM）将 compound interaction 视为均匀超可加。我们发现 severity 是 strategy × phase 交互的涌现属性：importance eviction 在 distributed-attention phase 剧烈放大 compound degradation（gradient 12-75×），而 random eviction 在所有 phase 保持平坦（~1×）。我们通过 entropy-discrimination collapse 机制解释这一现象：head pruning → attention 重分布 → importance score 的判别力崩塌 → importance eviction 退化为有偏伪随机。这一发现为 phase-aware sparsity allocation 提供了动机。\\n\\n**Framing 硬约束（D015）**：\\n- MUST: \\\"emergent phase-strategy interaction\\\"\\n- MUST NOT: \\\"importance metric limitation / importance is broken\\\"\\n\\n## Core Claims\\n\\n| ID | Claim | Status | Key Evidence |\\n|----|-------|--------|-------------|\\n| C1 | Compound sparsity severity is strategy-dependent | confirmed | importance gradient 12-75× vs random ~1× |\\n| C2 | Severity is phase-modulated (amplified in low-sparsity phase) | confirmed | low phase >> high phase at all 4 sparsity levels; monotonic increase 12.8→28.7→52.9→74.9 |\\n| C3 | Phase-strategy crossover exists | confirmed | s=0.25: importance high_phase=0.584 < random=3.002, importance low_phase=30.903 > random=2.915 |\\n| C4 | Entropy-discrimination collapse explains the mechanism | partially_confirmed | Conceptual argument solid; empirical attention entropy data not yet collected |\\n| C5 | Finding generalizes across model families | pending | Qwen2.5-7B-Instruct experiments in progress |\\n| C6 | Severity gradient is sub-exponential | confirmed | Growth rate decreasing: 2.24×→1.84×→1.42× |\\n\\n## Anticipated Reviewer Concerns\\n\\n### RC1: Generalizability — 7B models only, single benchmark\\n- **预期质疑**: \\\"Results on two 7B models and MATH-500 only. How do we know this generalizes to larger models or other reasoning tasks?\\\"\\n- **应对**: Cross-model replication (DeepSeek + Qwen, 不同架构血统) 是第一层防御。MATH-500 是 standard benchmark。Limitations 明确声明 scale 限制。机制解释 (entropy-discrimination collapse) 是 architecture-agnostic 的，原则上适用于任何 attention-based model。\\n- **实验支撑**: C5 (Qwen cross-model), 若需加强可扩展到更多模型\\n\\n### RC2: Mechanism — entropy-discrimination collapse 缺乏直接测量\\n- **预期质疑**: \\\"The mechanism is conceptual. Where is the empirical evidence for entropy increase and discrimination collapse?\\\"\\n- **应对**: 如果有 GPU 预算，可以直接测量 pruned vs unpruned 的 attention entropy 和 importance score 分布。目前 C4 status = partially_confirmed，需要决定是否投入 GPU 时间做 direct measurement。\\n- **实验支撑**: 可选 ablation：测量 attention entropy pre/post pruning × phase\\n\\n### RC3: Practical impact — 没有 throughput 数据\\n- **预期质疑**: \\\"No wall-clock or throughput measurements. Is the severity amplification reflected in actual inference speed?\\\"\\n- **应对**: 本文定位是 empirical finding paper（发现 + 机制解释），不是 method paper。Throughput 不是 claim 的一部分。Discussion 中明确 phase-gated controller 作为 future direction。\\n- **实验支撑**: 不需要额外实验\\n\\n### RC4: Statistical rigor — bootstrap 是否足够\\n- **预期质疑**: \\\"Per-problem bootstrap with 50 problems — sufficient sample size?\\\"\\n- **应对**: B=10000 iterations, all p=0.0000, CI 不跨零。50 problems 的 paired bootstrap 统计效力已充分。可在 appendix 补充 per-problem 分布图。\\n- **实验支撑**: 已完成，fig4_bootstrap\\n\\n### RC5: Novelty — prior work 是否已覆盖 phase-dependent sparsity\\n- **预期质疑**: \\\"ThinKV and phase-aware methods already consider phase. What's new?\\\"\\n- **应对**: Prior work 在单轴上分析 phase（ThinKV: phase-aware eviction）或 compound（SparK: joint compression）。没有工作同时分析 compound × phase × strategy 的三维交互。Crossover 现象（同一 strategy 在不同 phase 方向反转）是全新发现。\\n- **实验支撑**: C3 (crossover), Related Work §2 的 gap 分析\\n\\n## Paper Positioning\\n\\n**类型**: Empirical finding paper（非 method paper）\\n**核心贡献**:\\n1. 发现 compound sparsity severity 的 strategy × phase 交互\\n2. 量化 severity gradient（12-75×）和 crossover 现象\\n3. 提出 entropy-discrimination collapse 机制解释\\n4. Cross-model replication 验证泛化性\\n\\n**投稿目标**: EMNLP 2026 ARR, deadline 2026-05-25\\n\", \"total_chars\": 4119, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Glob · `toolu_018U2QGvWqBibpVFQSxxoJGu`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4ff71685-85e8-4572-b90c-68572f81a6a0",
  "uuid": "666402b5-a902-405e-bf85-45c7295e3e4c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QXJZfDk1LKCTn535AzSL2R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 869,
      "cache_read_input_tokens": 23727,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 869
      },
      "output_tokens": 42,
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

_source line 11 · 2026-05-14T05:41:09.209Z_

<details><summary>↩ Tool result · `toolu_018U2QGvWqBibpVFQSxxoJGu`</summary>

```text
artifacts/_project/paper/related_work_46fb53.tex
artifacts/_project/paper/background_fc6d1d.tex
artifacts/_project/paper/methodology.tex
artifacts/_project/paper/methodology_4cc5f3.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/background.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4ff71685-85e8-4572-b90c-68572f81a6a0",
  "uuid": "50df5367-45cc-4365-8bbd-e7bc81e2d219",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/paper/related_work_46fb53.tex",
      "artifacts/_project/paper/background_fc6d1d.tex",
      "artifacts/_project/paper/methodology.tex",
      "artifacts/_project/paper/methodology_4cc5f3.tex",
      "artifacts/_project/paper/related_work.tex",
      "artifacts/_project/paper/background.tex"
    ],
    "durationMs": 16,
    "numFiles": 6,
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
Let me read existing paper sections to match style and notation conventions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4ff71685-85e8-4572-b90c-68572f81a6a0",
  "uuid": "ec7c3eaa-b80a-48bd-9479-61b3f828bd2b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FvemzcmpvDFWSyLuPYwTTX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2175,
      "cache_read_input_tokens": 24596,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2175
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

Let me check existing sections for style/notation conventions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4ff71685-85e8-4572-b90c-68572f81a6a0",
  "uuid": "ffba6b79-f56e-4220-95c6-2fc0025cf0cb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FvemzcmpvDFWSyLuPYwTTX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2175,
      "cache_read_input_tokens": 24596,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2175
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

<details open><summary>🔧 Tool call — Read · `toolu_013Etp4kHBJdKvoCYdFPFvBK`</summary>

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
  "session_id": "4ff71685-85e8-4572-b90c-68572f81a6a0",
  "uuid": "a56ea71c-539f-420b-938a-efe7fd37f3e8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FvemzcmpvDFWSyLuPYwTTX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2175,
      "cache_read_input_tokens": 24596,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2175
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

_source line 15 · 2026-05-14T05:41:14.778Z_

<details><summary>↩ Tool result · `toolu_013Etp4kHBJdKvoCYdFPFvBK`</summary>

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
11	\paragraph{Qwen2.5-7B-Instruct} \cite{qwen2.5} provides a cross-architecture replication. Although it shares the same backbone family, its instruction tuning does not enforce explicit reasoning delimiters, producing a different distribution of attention sparsity across the generation trajectory. Replication on this model tests whether our findings generalize beyond distillation-induced phase structure.
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
50	We segment each generated sequence into three \emph{reasoning phases} based on the local attention sparsity of each token position. For each query position $i$, we compute per-head sparsity as the fraction of attention weights falling below $0.01 \times \max_j a_{i,h,j}$, then average across heads to obtain a scalar sparsity value per position. The resulting sparsity trajectory is partitioned into terciles via quantile boundaries: \emph{low-sparsity} (bottom third, corresponding to focused attention during structured computation), \emph{mid-sparsity}, and \emph{high-sparsity} (top third, corresponding to diffuse attention during exploratory reasoning). Contiguous segments shorter than $\texttt{min\_phase\_length}=10$ tokens are merged into adjacent phases to suppress noise.
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
86	All tests yield $p < 0.0001$ at every sparsity level, confirming that the observed phase--strategy interactions are not artifacts of sampling variability.\footnote{Experiments were conducted on a server with 4$\times$ NVIDIA RTX 6000 Ada 96\,GB GPUs, with one model--sparsity configuration per GPU.}
87	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4ff71685-85e8-4572-b90c-68572f81a6a0",
  "uuid": "e90a86e3-8d2a-469e-bebe-be56c1e59780",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex",
      "content": "\\section{Experimental Setup}\n\\label{sec:experimental-setup}\n\n\\subsection{Models}\n\\label{sec:models}\n\nWe conduct experiments on two 7B-parameter instruction-tuned models that share the Qwen2 backbone architecture (28 Transformer layers, 28 attention heads with 4-group GQA):\n\n\\paragraph{DeepSeek-R1-Distill-Qwen-7B} serves as our primary evaluation target. This model was distilled from DeepSeek-R1 \\cite{deepseek-r1} and produces explicit chain-of-thought traces delimited by \\texttt{&lt;think>}$\\cdots$\\texttt{&lt;/think>} tags, yielding sequences with pronounced phase structure---extended reasoning followed by a concise solution. The structured generation pattern makes it well-suited for studying how sparsity interacts with distinct reasoning phases.\n\n\\paragraph{Qwen2.5-7B-Instruct} \\cite{qwen2.5} provides a cross-architecture replication. Although it shares the same backbone family, its instruction tuning does not enforce explicit reasoning delimiters, producing a different distribution of attention sparsity across the generation trajectory. Replication on this model tests whether our findings generalize beyond distillation-induced phase structure.\n\nBoth models are loaded in \\texttt{bfloat16} precision with eager attention (i.e., without FlashAttention) to permit direct manipulation of attention weight matrices during sparsity intervention.\\footnote{An earlier \\texttt{float16} configuration produced sporadic NaN values in Layer~27 of DeepSeek-R1-Distill-Qwen-7B, affecting ${\\sim}$8\\% of logit positions. Switching to \\texttt{bfloat16} eliminated all NaN occurrences; we additionally apply NaN-guarded filtering as a safety net.}\n\n\n\\subsection{Dataset}\n\\label{sec:dataset}\n\nWe evaluate on a 50-problem stratified subset of the MATH-500 benchmark \\cite{math500}, sampling uniformly across problem categories (algebra, geometry, number theory, combinatorics, etc.) with a fixed seed for reproducibility. Mathematical reasoning tasks are a natural testbed for our study: they elicit long chain-of-thought sequences (up to 2048 tokens) in which the model alternates between exploratory reasoning and structured computation---phases that differ markedly in attention sparsity. Each problem is decoded greedily (\\texttt{max\\_new\\_tokens}$=$2048) to eliminate sampling variance.\n\n\n\\subsection{Compound Sparsity Configuration}\n\\label{sec:sparsity-config}\n\nWe apply \\emph{symmetric} compound sparsity: for a given sparsity level $s$, we prune the same fraction $s$ of attention heads and evict the same fraction $s$ of KV cache entries. We evaluate four sparsity levels $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$, spanning from mild to aggressive compression.\n\n\\paragraph{Sparsity conditions.} For each problem and each sparsity level, we compute perplexity under four conditions: (i)~\\emph{dense}---no intervention; (ii)~\\emph{attn-only}---head pruning without KV eviction; (iii)~\\emph{kv-only}---KV eviction without head pruning; and (iv)~\\emph{both}---simultaneous head pruning and KV eviction.\n\n\\paragraph{Eviction strategies.} We compare two KV cache eviction strategies:\n\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\textbf{Importance-based.} Each KV position receives a score equal to its cumulative attention weight summed over all query positions and heads. To correct for the inherent causal bias---earlier positions accumulate more attention simply because they are attended to by more queries---we apply position normalization:\n\\begin{equation}\n\\label{eq:importance}\n    \\alpha_j = \\frac{\\sum_{i,h} a_{i,h,j}}{\\texttt{seq\\_len} - j}, \\quad j \\in \\{1, \\dots, T\\},\n\\end{equation}\nwhere $a_{i,h,j}$ is the attention weight from query~$i$, head~$h$ to key~$j$, and the denominator counts the number of queries that can attend to position~$j$ under causal masking. Position~0 (BOS) is always retained. The $T \\cdot s$ positions with the lowest normalized scores are evicted.\n\nDuring masked forward passes, we guard against numerical instability from the interaction of head masking and KV eviction: zeroed-out heads that would otherwise produce $\\infty \\times 0 = \\text{NaN}$ are handled via selective replacement (\\texttt{torch.where}) prior to the softmax, and any layer producing NaN outputs is skipped from the sparsity loss computation.\n\n\\item \\textbf{Random.} KV positions (excluding BOS) are evicted uniformly at random, providing a strategy-agnostic baseline. Head pruning under the random condition selects heads via \\texttt{torch.randperm} rather than by importance.\n\\end{itemize}\n\n\\paragraph{Head pruning.} Under importance-based eviction, heads are ranked by their Frobenius norm across the full attention matrix $\\mathbf{A}_\\ell \\in \\mathbb{R}^{H \\times T \\times T}$ per layer $\\ell$, and the bottom-$s$ fraction is masked. Under random eviction, heads are selected uniformly at random.\n\n\n\\subsection{Phase Segmentation}\n\\label{sec:phase-seg}\n\nWe segment each generated sequence into three \\emph{reasoning phases} based on the local attention sparsity of each token position. For each query position $i$, we compute per-head sparsity as the fraction of attention weights falling below $0.01 \\times \\max_j a_{i,h,j}$, then average across heads to obtain a scalar sparsity value per position. The resulting sparsity trajectory is partitioned into terciles via quantile boundaries: \\emph{low-sparsity} (bottom third, corresponding to focused attention during structured computation), \\emph{mid-sparsity}, and \\emph{high-sparsity} (top third, corresponding to diffuse attention during exploratory reasoning). Contiguous segments shorter than $\\texttt{min\\_phase\\_length}=10$ tokens are merged into adjacent phases to suppress noise.\n\n\n\\subsection{Metrics}\n\\label{sec:metrics}\n\n\\paragraph{Perplexity.} For each sparsity condition $c \\in \\{d, a, k, b\\}$ and each phase, we compute segment-level perplexity as\n$\\text{PPL}_c = \\exp\\!\\bigl(\\tfrac{1}{|I|}\\sum_{i \\in I} \\mathcal{L}_c(x_i)\\bigr)$,\nwhere $I$ is the set of token indices belonging to the phase and $\\mathcal{L}_c(x_i)$ is the per-token cross-entropy loss under condition $c$.\n\n\\paragraph{Interaction Index.} The interaction index quantifies the synergistic (super-additive) effect of compound sparsity beyond the sum of individual interventions:\n\\begin{equation}\n\\label{eq:ii}\n    \\mathrm{II} = \\frac{\\text{PPL}_b}{\\text{PPL}_d} - \\frac{\\text{PPL}_a}{\\text{PPL}_d} - \\frac{\\text{PPL}_k}{\\text{PPL}_d} + 1.\n\\end{equation}\nWhen $\\mathrm{II} > 0$, the two sparsity mechanisms amplify each other; $\\mathrm{II} = 0$ indicates additive (independent) degradation.\n\n\\paragraph{Severity Gradient.} To measure how the interaction varies across reasoning phases, we define the severity gradient:\n\\begin{equation}\n\\label{eq:gradient}\n    G = \\frac{\\widetilde{\\mathrm{II}}_{\\,\\textit{low}}}{\\widetilde{\\mathrm{II}}_{\\,\\textit{high}}},\n\\end{equation}\nwhere $\\widetilde{\\mathrm{II}}_{\\,\\textit{low}}$ and $\\widetilde{\\mathrm{II}}_{\\,\\textit{high}}$ are the median interaction indices over the low-sparsity and high-sparsity phases, respectively. We report medians rather than means because the II distribution is heavily right-skewed (mean/median ratios up to 43:1 at $s{=}0.30$), making the median a more robust central tendency estimator.\n\n\n\\subsection{Statistical Analysis}\n\\label{sec:stats}\n\nAll confidence intervals and significance tests are computed via the nonparametric bootstrap with $B = 10{,}000$ resamples \\cite{efron1993bootstrap}.\n\n\\paragraph{Per-problem bootstrap.} For each sparsity level and strategy, we resample the 50 per-problem II values with replacement and compute the mean of each resample, yielding a 95\\% percentile confidence interval for the population mean II.\n\n\\paragraph{Paired bootstrap.} To test whether the severity gradient differs between importance-based and random eviction, we pair observations by problem (same problem, same sparsity level) and bootstrap the difference in gradients. This controls for problem-level variance in difficulty and sequence length.\n\n\\paragraph{Unpaired bootstrap.} We additionally compute per-strategy gradient confidence intervals without pairing, to verify that the importance-based gradient is significantly greater than 1 (i.e., phase modulation exists) independently of the random baseline.\n\nAll tests yield $p < 0.0001$ at every sparsity level, confirming that the observed phase--strategy interactions are not artifacts of sampling variability.\\footnote{Experiments were conducted on a server with 4$\\times$ NVIDIA RTX 6000 Ada 96\\,GB GPUs, with one model--sparsity configuration per GPU.}\n",
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

_source line 16_

<details open><summary>🔧 Tool call — Read · `toolu_01Fg6VHDk5M9j6DYXFk7VHrL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4ff71685-85e8-4572-b90c-68572f81a6a0",
  "uuid": "da117d96-1746-4a71-a5bb-a58af1363ce9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FvemzcmpvDFWSyLuPYwTTX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2175,
      "cache_read_input_tokens": 24596,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2175
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

_source line 17 · 2026-05-14T05:41:15.092Z_

<details><summary>↩ Tool result · `toolu_01Fg6VHDk5M9j6DYXFk7VHrL`</summary>

```text
1	% Section 3: Background and Problem Setup
2	% Phase-Modulated Compound Sparsity
3	
4	\section{Background and Problem Setup}
5	\label{sec:background}
6	
7	We formalize compound sparsity as the simultaneous application of attention head pruning and KV cache eviction, define the Interaction Index to measure their non-additive interaction, and introduce phase segmentation to localize the analysis across reasoning stages.
8	
9	\subsection{Compound Sparsity Formulation}
10	\label{sec:compound-sparsity}
11	
12	Consider a transformer language model $\mathcal{M}$ with $L$ layers, each containing $H$ attention heads.
13	Let $s \in (0,1)$ denote a unified sparsity budget applied to both compression axes.
14	
15	\paragraph{Attention head pruning.}
16	Given per-head importance scores $\mathbf{w}^{(l)} \in \mathbb{R}^H$ for layer $l$, we construct a binary mask $\mathbf{m}_h^{(l)} \in \{0,1\}^H$ that retains the top-$(1{-}s) \cdot H$ heads by importance.
17	For head $j$ in layer $l$, the masked attention output becomes:
18	\begin{equation}
19	    \tilde{\mathbf{o}}_j^{(l)} = m_{h,j}^{(l)} \cdot \mathbf{o}_j^{(l)}
20	    \label{eq:head-mask}
21	\end{equation}
22	where $\mathbf{o}_j^{(l)}$ is the original head output.
23	Head importance is computed as the Frobenius norm of the attention weight matrix: $w_j^{(l)} = \|\mathbf{A}_j^{(l)}\|_F$, where $\mathbf{A}_j^{(l)} \in \mathbb{R}^{T \times T}$ is the attention probability matrix for head $j$ at layer $l$ over a calibration input of length $T$.
24	
25	\paragraph{KV cache eviction.}
26	For a sequence of length $T$, we construct a position mask $\mathbf{m}_k \in \{0,1\}^T$ that retains the top-$(1{-}s) \cdot T$ positions by importance, with position $0$ (BOS) always retained.
27	Evicted positions are blocked by setting their attention mask entries to zero:
28	\begin{equation}
29	    \tilde{a}_{ij} = a_{ij} \cdot m_{k,j}, \quad \forall i,j
30	    \label{eq:kv-mask}
31	\end{equation}
32	We evaluate two eviction strategies:
33	\begin{itemize}[nosep,leftmargin=*]
34	    \item \textbf{Importance-based:} Position importance is the cumulative attention mass received across all heads and query positions, with position normalization to correct for causal attention bias:
35	    \begin{equation}
36	        \mathrm{imp}(j) = \frac{\sum_{l,h,i} a^{(l,h)}_{ij}}{T - j}
37	        \label{eq:kv-importance}
38	    \end{equation}
39	    where the denominator $(T - j)$ compensates for the fact that later positions can attend to fewer future tokens under causal masking \cite{thinkv2026}.
40	    \item \textbf{Random:} Positions (excluding BOS) are evicted uniformly at random.
41	\end{itemize}
42	
43	\paragraph{Compound sparsity.}
44	Applying both compressions simultaneously yields a model $\mathcal{M}(s)$ where fraction $s$ of heads are pruned per layer \emph{and} fraction $s$ of KV positions are evicted.
45	The two axes interact: head pruning alters the attention distribution over surviving heads, which in turn changes the importance ranking used for KV eviction.
46	
47	\subsection{Interaction Index}
48	\label{sec:interaction-index}
49	
50	To quantify whether compound sparsity degrades performance more (or less) than the sum of its components, we define the \emph{Interaction Index} (II) following the factorial interaction framework from experimental design.
51	
52	Let $\mathrm{PPL}_d$, $\mathrm{PPL}_h$, $\mathrm{PPL}_k$, and $\mathrm{PPL}_b$ denote the perplexity of the dense model, head-pruning only, KV-eviction only, and both applied simultaneously, respectively.
53	Perplexity is computed as $\mathrm{PPL} = \exp\!\bigl(\frac{1}{|S|}\sum_{t \in S} \mathcal{L}_t\bigr)$ where $\mathcal{L}_t$ is the per-token cross-entropy loss and $S$ is the set of evaluated positions.
54	
55	We define the relative degradation ratios $R_h = \mathrm{PPL}_h / \mathrm{PPL}_d$, $R_k = \mathrm{PPL}_k / \mathrm{PPL}_d$, $R_b = \mathrm{PPL}_b / \mathrm{PPL}_d$, and the Interaction Index:
56	\begin{equation}
57	    \mathrm{II} = R_b - R_h - R_k + 1
58	    \label{eq:ii}
59	\end{equation}
60	Under additive independence, $R_b \approx R_h + R_k - 1$, giving $\mathrm{II} \approx 0$.
61	\begin{itemize}[nosep,leftmargin=*]
62	    \item $\mathrm{II} > 0$: \textbf{super-additive} — compound sparsity degrades more than the sum of individual effects.
63	    \item $\mathrm{II} < 0$: \textbf{sub-additive} — compound sparsity is less harmful than expected.
64	    \item $\mathrm{II} = 0$: \textbf{additive} — no interaction between the two axes.
65	\end{itemize}
66	
67	\paragraph{Choice of additive null.}
68	Eq.~\ref{eq:ii} posits an additive null $R_b = R_h + R_k - 1$, but one could equally assume multiplicative independence $R_b = R_h \cdot R_k$, treating the two axes as independent survival probabilities.
69	We adopt the additive form because head pruning and KV eviction operate on disjoint model dimensions---structural (which heads to keep) versus positional (which tokens to retain).
70	When the two mechanisms act independently, each contributes an additive increment $\Delta R$ to the perplexity ratio: the heads removed by pruning and the positions removed by eviction affect non-overlapping information pathways, so their degradations sum rather than multiply.
71	At the sparsity levels studied ($s \leq 0.30$), this non-overlap assumption holds empirically (\S\ref{sec:experiments}).
72	We report the multiplicative residual $R_b / (R_h \cdot R_k)$ alongside II in Appendix~\ref{app:multiplicative-null}; the qualitative conclusions are unchanged under either null model.
73	
74	We evaluate II on 50 problems from MATH-500 \cite{hendrycks2021math}, stratified across difficulty levels.
75	Per-problem II values are aggregated via the median (rather than the mean) due to heavy-tailed distributions---e.g., the mean/median ratio reaches $33.5\times$ for the low-sparsity phase at $s{=}0.30$ (\S\ref{sec:experiments})---where a single outlier can dominate the mean.
76	Bootstrap confidence intervals ($B=10{,}000$ resamples) are computed at the problem level.
77	
78	\paragraph{Severity gradient.}
79	To capture how II varies across reasoning phases, we define the \emph{severity gradient}:
80	\begin{equation}
81	    G = \frac{\widetilde{\mathrm{II}}_{\mathrm{low}}}{\widetilde{\mathrm{II}}_{\mathrm{high}}}
82	    \label{eq:gradient}
83	\end{equation}
84	where $\widetilde{\mathrm{II}}_{\mathrm{low}}$ and $\widetilde{\mathrm{II}}_{\mathrm{high}}$ are the median II in the low-sparsity and high-sparsity phases respectively.
85	$G \gg 1$ indicates that compound degradation concentrates in low-sparsity phases; $G \approx 1$ indicates uniform degradation.
86	$G$ is defined only when $\widetilde{\mathrm{II}}_{\mathrm{high}} > \varepsilon$ for a small threshold $\varepsilon > 0$; when $\widetilde{\mathrm{II}}_{\mathrm{high}} \approx 0$ (ceiling effect, where head pruning alone causes negligible degradation in high-sparsity phases), we report $G = \infty$.
87	
88	\subsection{Phase Segmentation}
89	\label{sec:phase-segmentation}
90	
91	Reasoning-capable LLMs produce token sequences with heterogeneous attention patterns: some segments exhibit concentrated attention (few tokens dominate), while others distribute attention broadly.
92	We partition each generation into three phases based on the \emph{attention sparsity profile}, following the methodology of ThinKV \cite{thinkv2026}.
93	
94	\paragraph{Attention sparsity.}
95	For each query position $i$ and head $h$, we compute the fraction of key positions receiving attention below $1\%$ of the row maximum:
96	\begin{equation}
97	    \sigma_i^{(h)} = \frac{1}{T}\sum_{j=1}^{T} \mathbf{1}\!\left[a_{ij}^{(h)} < 0.01 \cdot \max_k a_{ik}^{(h)}\right]
98	    \label{eq:sparsity}
99	\end{equation}
100	The per-token sparsity $\sigma_i = \frac{1}{H}\sum_h \sigma_i^{(h)}$ averages across heads.
101	
102	\paragraph{Quantile-based segmentation.}
103	We partition tokens into three equal-sized groups by the quantiles of $\{\sigma_i\}_{i=1}^{T}$:
104	\begin{itemize}[nosep,leftmargin=*]
105	    \item \textbf{High-sparsity phase} (top tercile): attention concentrates on a few tokens; heads are highly redundant, and pruning incurs minimal information loss.
106	    \item \textbf{Mid-sparsity phase} (middle tercile): intermediate attention patterns.
107	    \item \textbf{Low-sparsity phase} (bottom tercile): attention distributes broadly across many tokens; each head carries non-redundant information, making pruning costly.
108	\end{itemize}
109	
110	This segmentation is purely data-driven and does not require access to model internals beyond attention weights.
111	It captures the heterogeneity in attention structure that arises naturally during extended reasoning, where the model alternates between focused retrieval (high sparsity) and exploratory cross-token integration (low sparsity) \cite{thinkingmi2025}.
112	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4ff71685-85e8-4572-b90c-68572f81a6a0",
  "uuid": "9a03df1c-1244-4b64-888a-012ad3e5b7bc",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex",
      "content": "% Section 3: Background and Problem Setup\n% Phase-Modulated Compound Sparsity\n\n\\section{Background and Problem Setup}\n\\label{sec:background}\n\nWe formalize compound sparsity as the simultaneous application of attention head pruning and KV cache eviction, define the Interaction Index to measure their non-additive interaction, and introduce phase segmentation to localize the analysis across reasoning stages.\n\n\\subsection{Compound Sparsity Formulation}\n\\label{sec:compound-sparsity}\n\nConsider a transformer language model $\\mathcal{M}$ with $L$ layers, each containing $H$ attention heads.\nLet $s \\in (0,1)$ denote a unified sparsity budget applied to both compression axes.\n\n\\paragraph{Attention head pruning.}\nGiven per-head importance scores $\\mathbf{w}^{(l)} \\in \\mathbb{R}^H$ for layer $l$, we construct a binary mask $\\mathbf{m}_h^{(l)} \\in \\{0,1\\}^H$ that retains the top-$(1{-}s) \\cdot H$ heads by importance.\nFor head $j$ in layer $l$, the masked attention output becomes:\n\\begin{equation}\n    \\tilde{\\mathbf{o}}_j^{(l)} = m_{h,j}^{(l)} \\cdot \\mathbf{o}_j^{(l)}\n    \\label{eq:head-mask}\n\\end{equation}\nwhere $\\mathbf{o}_j^{(l)}$ is the original head output.\nHead importance is computed as the Frobenius norm of the attention weight matrix: $w_j^{(l)} = \\|\\mathbf{A}_j^{(l)}\\|_F$, where $\\mathbf{A}_j^{(l)} \\in \\mathbb{R}^{T \\times T}$ is the attention probability matrix for head $j$ at layer $l$ over a calibration input of length $T$.\n\n\\paragraph{KV cache eviction.}\nFor a sequence of length $T$, we construct a position mask $\\mathbf{m}_k \\in \\{0,1\\}^T$ that retains the top-$(1{-}s) \\cdot T$ positions by importance, with position $0$ (BOS) always retained.\nEvicted positions are blocked by setting their attention mask entries to zero:\n\\begin{equation}\n    \\tilde{a}_{ij} = a_{ij} \\cdot m_{k,j}, \\quad \\forall i,j\n    \\label{eq:kv-mask}\n\\end{equation}\nWe evaluate two eviction strategies:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{Importance-based:} Position importance is the cumulative attention mass received across all heads and query positions, with position normalization to correct for causal attention bias:\n    \\begin{equation}\n        \\mathrm{imp}(j) = \\frac{\\sum_{l,h,i} a^{(l,h)}_{ij}}{T - j}\n        \\label{eq:kv-importance}\n    \\end{equation}\n    where the denominator $(T - j)$ compensates for the fact that later positions can attend to fewer future tokens under causal masking \\cite{thinkv2026}.\n    \\item \\textbf{Random:} Positions (excluding BOS) are evicted uniformly at random.\n\\end{itemize}\n\n\\paragraph{Compound sparsity.}\nApplying both compressions simultaneously yields a model $\\mathcal{M}(s)$ where fraction $s$ of heads are pruned per layer \\emph{and} fraction $s$ of KV positions are evicted.\nThe two axes interact: head pruning alters the attention distribution over surviving heads, which in turn changes the importance ranking used for KV eviction.\n\n\\subsection{Interaction Index}\n\\label{sec:interaction-index}\n\nTo quantify whether compound sparsity degrades performance more (or less) than the sum of its components, we define the \\emph{Interaction Index} (II) following the factorial interaction framework from experimental design.\n\nLet $\\mathrm{PPL}_d$, $\\mathrm{PPL}_h$, $\\mathrm{PPL}_k$, and $\\mathrm{PPL}_b$ denote the perplexity of the dense model, head-pruning only, KV-eviction only, and both applied simultaneously, respectively.\nPerplexity is computed as $\\mathrm{PPL} = \\exp\\!\\bigl(\\frac{1}{|S|}\\sum_{t \\in S} \\mathcal{L}_t\\bigr)$ where $\\mathcal{L}_t$ is the per-token cross-entropy loss and $S$ is the set of evaluated positions.\n\nWe define the relative degradation ratios $R_h = \\mathrm{PPL}_h / \\mathrm{PPL}_d$, $R_k = \\mathrm{PPL}_k / \\mathrm{PPL}_d$, $R_b = \\mathrm{PPL}_b / \\mathrm{PPL}_d$, and the Interaction Index:\n\\begin{equation}\n    \\mathrm{II} = R_b - R_h - R_k + 1\n    \\label{eq:ii}\n\\end{equation}\nUnder additive independence, $R_b \\approx R_h + R_k - 1$, giving $\\mathrm{II} \\approx 0$.\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item $\\mathrm{II} > 0$: \\textbf{super-additive} — compound sparsity degrades more than the sum of individual effects.\n    \\item $\\mathrm{II} < 0$: \\textbf{sub-additive} — compound sparsity is less harmful than expected.\n    \\item $\\mathrm{II} = 0$: \\textbf{additive} — no interaction between the two axes.\n\\end{itemize}\n\n\\paragraph{Choice of additive null.}\nEq.~\\ref{eq:ii} posits an additive null $R_b = R_h + R_k - 1$, but one could equally assume multiplicative independence $R_b = R_h \\cdot R_k$, treating the two axes as independent survival probabilities.\nWe adopt the additive form because head pruning and KV eviction operate on disjoint model dimensions---structural (which heads to keep) versus positional (which tokens to retain).\nWhen the two mechanisms act independently, each contributes an additive increment $\\Delta R$ to the perplexity ratio: the heads removed by pruning and the positions removed by eviction affect non-overlapping information pathways, so their degradations sum rather than multiply.\nAt the sparsity levels studied ($s \\leq 0.30$), this non-overlap assumption holds empirically (\\S\\ref{sec:experiments}).\nWe report the multiplicative residual $R_b / (R_h \\cdot R_k)$ alongside II in Appendix~\\ref{app:multiplicative-null}; the qualitative conclusions are unchanged under either null model.\n\nWe evaluate II on 50 problems from MATH-500 \\cite{hendrycks2021math}, stratified across difficulty levels.\nPer-problem II values are aggregated via the median (rather than the mean) due to heavy-tailed distributions---e.g., the mean/median ratio reaches $33.5\\times$ for the low-sparsity phase at $s{=}0.30$ (\\S\\ref{sec:experiments})---where a single outlier can dominate the mean.\nBootstrap confidence intervals ($B=10{,}000$ resamples) are computed at the problem level.\n\n\\paragraph{Severity gradient.}\nTo capture how II varies across reasoning phases, we define the \\emph{severity gradient}:\n\\begin{equation}\n    G = \\frac{\\widetilde{\\mathrm{II}}_{\\mathrm{low}}}{\\widetilde{\\mathrm{II}}_{\\mathrm{high}}}\n    \\label{eq:gradient}\n\\end{equation}\nwhere $\\widetilde{\\mathrm{II}}_{\\mathrm{low}}$ and $\\widetilde{\\mathrm{II}}_{\\mathrm{high}}$ are the median II in the low-sparsity and high-sparsity phases respectively.\n$G \\gg 1$ indicates that compound degradation concentrates in low-sparsity phases; $G \\approx 1$ indicates uniform degradation.\n$G$ is defined only when $\\widetilde{\\mathrm{II}}_{\\mathrm{high}} > \\varepsilon$ for a small threshold $\\varepsilon > 0$; when $\\widetilde{\\mathrm{II}}_{\\mathrm{high}} \\approx 0$ (ceiling effect, where head pruning alone causes negligible degradation in high-sparsity phases), we report $G = \\infty$.\n\n\\subsection{Phase Segmentation}\n\\label{sec:phase-segmentation}\n\nReasoning-capable LLMs produce token sequences with heterogeneous attention patterns: some segments exhibit concentrated attention (few tokens dominate), while others distribute attention broadly.\nWe partition each generation into three phases based on the \\emph{attention sparsity profile}, following the methodology of ThinKV \\cite{thinkv2026}.\n\n\\paragraph{Attention sparsity.}\nFor each query position $i$ and head $h$, we compute the fraction of key positions receiving attention below $1\\%$ of the row maximum:\n\\begin{equation}\n    \\sigma_i^{(h)} = \\frac{1}{T}\\sum_{j=1}^{T} \\mathbf{1}\\!\\left[a_{ij}^{(h)} < 0.01 \\cdot \\max_k a_{ik}^{(h)}\\right]\n    \\label{eq:sparsity}\n\\end{equation}\nThe per-token sparsity $\\sigma_i = \\frac{1}{H}\\sum_h \\sigma_i^{(h)}$ averages across heads.\n\n\\paragraph{Quantile-based segmentation.}\nWe partition tokens into three equal-sized groups by the quantiles of $\\{\\sigma_i\\}_{i=1}^{T}$:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{High-sparsity phase} (top tercile): attention concentrates on a few tokens; heads are highly redundant, and pruning incurs minimal information loss.\n    \\item \\textbf{Mid-sparsity phase} (middle tercile): intermediate attention patterns.\n    \\item \\textbf{Low-sparsity phase} (bottom tercile): attention distributes broadly across many tokens; each head carries non-redundant information, making pruning costly.\n\\end{itemize}\n\nThis segmentation is purely data-driven and does not require access to model internals beyond attention weights.\nIt captures the heterogeneity in attention structure that arises naturally during extended reasoning, where the model alternates between focused retrieval (high sparsity) and exploratory cross-token integration (low sparsity) \\cite{thinkingmi2025}.\n",
      "numLines": 112,
      "startLine": 1,
      "totalLines": 112
    }
  }
}
```

</details>

---

### Assistant

_source line 18_

<details><summary>Logged reasoning block</summary>

```text
Now I have a good understanding of the style and notation conventions. Let me also read the related work to understand cross-referencing patterns.

Key notation and conventions I observe:
- Uses `\paragraph{}` for sub-subsection level headings
- Uses `\cite{}` references
- Uses `\mathrm{II}` for Interaction Index
- Uses `$s$` for sparsity level
- Uses `\widetilde{\mathrm{II}}` for median II
- Uses `$G$` for severity gradient


- Phase names: low-sparsity, mid-sparsity, high-sparsity
- Uses `\emph{}` for first use of key terms
- Uses `\textbf{}` for bold emphasis in inline text
- Uses `\begin{itemize}[nosep,leftmargin=*]` for lists
- References sections with `\S\ref{}` and labels follow `sec:xxx` convention

Now I'm ready to write the Analysis section, which needs to cover the entropy-discrimination collapse phenomenon, starting with attention redistribution under head pruning, then moving into the subsequent subsections.

I need to check whether `\placeholder{}` is already defined in the preamble, or if I should define it myself. The framing should emphasize this as an emergent phase-strategy interaction rather than just a limitation of the importance metric. Since the C4 status is partially confirmed, I'll use tentative language like "we hypothesize" and "this suggests" rather than making definitive claims.

I'm drafting the opening section now, which should establish why importance-based eviction shows such a dramatic severity gradient—12 to 75 times amplification in low-sparsity phases compared to the flat behavior of random eviction—and then build toward explaining the underlying mechanism.

Defining the attention entropy equation and explaining how head pruning forces surviving heads to redistribute attention mass in ways that degrade the discriminative power of importance scores... I'm looking at empirical measurements of how attention entropy changes across different sparsity phases when heads are pruned, showing that the entropy increase varies depending on the phase. This asymmetry stems from phase-dependent head redundancy—high-sparsity phases have more overlapping attention patterns that can absorb pruning, while low-sparsity phases have more unique contributions per head. Now I'm moving into how this affects importance scoring for key-value positions, where increased attention entropy from pruning starts to degrade the discrimination between important and unimportant positions. ulates to random selection. I'm visualizing how importance score concentration metrics like the Gini coefficient shift across different sparsity phases, showing where discrimination breaks down most severely. This directly explains the crossover: high-sparsity phases preserve attention concentration so importance-based eviction works well, but low-sparsity phases amplify entropy and collapse discrimination, causing importance-based methods to inadvertently remove critical positions and perform worse than random eviction.

Random eviction avoids this trap entirely because it's independent of attention patterns and unaffected by the redistribution caused by head pruning, which is why its severity stays flat across sparsity levels. The entropy-discrimination collapse mechanism extends beyond these specific configurations—it applies to any method using attention-mass-based importance scoring combined with heterogeneous attention entropy across reasoning phases, which covers the major KV cache compression approaches like H₂O, SnapKV, and Pyramid.

This predicts that any importance metric tied to attention mass will show discrimination collapse in broadly distributed attention phases, with severity scaling to the entropy increase from pruning, while metrics based on activation magnitude or gradient sensitivity would remain unaffected. The flat gradient from random eviction reveals that the phase-modulated amplification under importance-based methods isn't inherent to compound sparsity itself. I'm aiming for roughly 600-800 words of body text to fit a single page in EMNLP's two-column format, so I need to tighten the writing while maintaining the same level of detail as the methodology section.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4ff71685-85e8-4572-b90c-68572f81a6a0",
  "uuid": "6f3a90a9-2c7b-43eb-832d-69df1790b246",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Z7wd5xLxBQWrFyJRGjHpj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5889,
      "cache_read_input_tokens": 26771,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5889
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

_source line 19_

Now I have a clear picture of the notation and style. Let me also quickly check for any existing analysis section and the `\placeholder` command definition.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4ff71685-85e8-4572-b90c-68572f81a6a0",
  "uuid": "9f0a1b7f-e11f-40d0-980b-7938d8fd63c9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Z7wd5xLxBQWrFyJRGjHpj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5889,
      "cache_read_input_tokens": 26771,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5889
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

_source line 20_

<details open><summary>🔧 Tool call — Grep · `toolu_01CbPV5eexdvUNz6tK3cRsnp`</summary>

```json
{
  "pattern": "\\\\placeholder",
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
  "session_id": "4ff71685-85e8-4572-b90c-68572f81a6a0",
  "uuid": "0f5cb2c8-8a6c-4f76-b9c1-85e0bc099428",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Z7wd5xLxBQWrFyJRGjHpj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5889,
      "cache_read_input_tokens": 26771,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5889
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

_source line 21 · 2026-05-14T05:42:12.620Z_

<details><summary>↩ Tool result · `toolu_01CbPV5eexdvUNz6tK3cRsnp`</summary>

```text
Found 5 files
logs/workers/worker_writing_analysis-skeleton_20260514T054050.log
logs/chats/feishu_group_oc_fdc656be1c7fe17c11ab639cdbce3710_director.jsonl
logs/workers/worker_writing_results-skeleton_20260514T054026.log
logs/chats/feishu_group_oc_b6401b894d32f1aac1ce3e54ce0d0bd4.jsonl
artifacts/_project/paper/results.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4ff71685-85e8-4572-b90c-68572f81a6a0",
  "uuid": "7bbb3199-1eb7-4e43-bfb0-f4e766266fb9",
  "tool_use_result": {
    "mode": "files_with_matches",
    "filenames": [
      "logs/workers/worker_writing_analysis-skeleton_20260514T054050.log",
      "logs/chats/feishu_group_oc_fdc656be1c7fe17c11ab639cdbce3710_director.jsonl",
      "logs/workers/worker_writing_results-skeleton_20260514T054026.log",
      "logs/chats/feishu_group_oc_b6401b894d32f1aac1ce3e54ce0d0bd4.jsonl",
      "artifacts/_project/paper/results.tex"
    ],
    "numFiles": 5
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Grep · `toolu_014v1vpmekAh8WYgD4et4ZD9`</summary>

```json
{
  "pattern": "analysis",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4ff71685-85e8-4572-b90c-68572f81a6a0",
  "uuid": "bf4baacd-50a4-4f4b-a5b8-7855bbb5af8b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Z7wd5xLxBQWrFyJRGjHpj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5889,
      "cache_read_input_tokens": 26771,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5889
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

_source line 23 · 2026-05-14T05:42:13.412Z_

<details><summary>↩ Tool result · `toolu_014v1vpmekAh8WYgD4et4ZD9`</summary>

```text
Found 3 files
artifacts/_project/paper/results.tex
artifacts/_project/paper/background.tex
artifacts/_project/paper/background_fc6d1d.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4ff71685-85e8-4572-b90c-68572f81a6a0",
  "uuid": "b16ce0ed-2ab5-4a07-a19a-307708d5db1b",
  "tool_use_result": {
    "mode": "files_with_matches",
    "filenames": [
      "artifacts/_project/paper/results.tex",
      "artifacts/_project/paper/background.tex",
      "artifacts/_project/paper/background_fc6d1d.tex"
    ],
    "numFiles": 3
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Grep · `toolu_017ncKev2kXFY39GeL1RDkVz`</summary>

```json
{
  "pattern": "\\\\placeholder",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex",
  "output_mode": "content",
  "-C": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4ff71685-85e8-4572-b90c-68572f81a6a0",
  "uuid": "dce61b30-763f-43ec-9662-b3bf6ab14ec7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017mMbEARdDTXr46gBYQSqy2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2786,
      "cache_read_input_tokens": 32660,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2786
      },
      "output_tokens": 72,
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

_source line 25 · 2026-05-14T05:42:17.504Z_

<details><summary>↩ Tool result · `toolu_017ncKev2kXFY39GeL1RDkVz`</summary>

```text
11-% Evidence: v5_importance_segment, v5_random_segment
12:[Omitted long matching line]
13-
--
22-\midrule
23:0.15 & Importance & \placeholder{} & \placeholder{} & \placeholder{} & [\placeholder{}, \placeholder{}] \\
24:0.15 & Random     & \placeholder{} & \placeholder{} & \placeholder{} & [\placeholder{}, \placeholder{}] \\
25-\addlinespace
26:0.20 & Importance & \placeholder{} & \placeholder{} & \placeholder{} & [\placeholder{}, \placeholder{}] \\
27:0.20 & Random     & \placeholder{} & \placeholder{} & \placeholder{} & [\placeholder{}, \placeholder{}] \\
28-\addlinespace
29:0.25 & Importance & \placeholder{} & \placeholder{} & \placeholder{} & [\placeholder{}, \placeholder{}] \\
30:0.25 & Random     & \placeholder{} & \placeholder{} & \placeholder{} & [\placeholder{}, \placeholder{}] \\
31-\addlinespace
32:0.30 & Importance & \placeholder{} & \placeholder{} & \placeholder{} & [\placeholder{}, \placeholder{}] \\
33:0.30 & Random     & \placeholder{} & \placeholder{} & \placeholder{} & [\placeholder{}, \placeholder{}] \\
34-\bottomrule
--
38-% Evidence: v5_importance_segment
39:The gradient growth is sub-exponential: successive ratios between adjacent sparsity levels are \placeholder{r\_15\_20}$\times$, \placeholder{r\_20\_25}$\times$, and \placeholder{r\_25\_30}$\times$---a decreasing growth rate. This pattern suggests a ceiling effect at higher sparsity levels, where compound degradation in the low-sparsity phase saturates. Figure~\ref{fig:hero} visualizes this trajectory, contrasting the steep importance-based curve against the flat random baseline.
40-
--
43-\includegraphics[width=\columnwidth]{figures/fig1_hero.pdf}
44:\caption{Severity gradient ($G$) as a function of sparsity level $s$. Importance-based eviction (solid) exhibits a monotonically increasing gradient from \placeholder{} to \placeholder{}$\times$, while random eviction (dashed) remains flat near $1\times$. Shaded regions denote 95\% bootstrap confidence intervals.}
45-\label{fig:hero}
--
59-\midrule
60:0.15 & \placeholder{} & [\placeholder{}, \placeholder{}] & \placeholder{} & [\placeholder{}, \placeholder{}] \\
61:0.20 & \placeholder{} & [\placeholder{}, \placeholder{}] & \placeholder{} & [\placeholder{}, \placeholder{}] \\
62:0.25 & \placeholder{} & [\placeholder{}, \placeholder{}] & \placeholder{} & [\placeholder{}, \placeholder{}] \\
63:0.30 & \placeholder{} & [\placeholder{}, \placeholder{}] & \placeholder{} & [\placeholder{}, \placeholder{}] \\
64-\bottomrule
--
74-
75:We report medians throughout because the II distribution is heavily right-skewed: mean/median ratios reach \placeholder{skew\_ratio}:1 at $s{=}0.30$ under importance-based eviction. A small number of problems with exceptionally long reasoning traces produce outsized II values; the median resists this influence while the bootstrap CI accounts for it via the resampling distribution.
76-
--
81-% Evidence: v5_importance_segment, v5_random_segment
82:[Omitted long matching line]
83-
--
88-\includegraphics[width=\columnwidth]{figures/fig2_crossover.pdf}
89:\caption{Strategy-dependent crossover. Heatmap of median II by eviction strategy (rows) and reasoning phase (columns) at $s{=}$\placeholder{}. Importance-based eviction outperforms random in the high-sparsity phase but produces \placeholder{}$\times$ higher II in the low-sparsity phase, reversing the strategy ranking.}
90-\label{fig:crossover}
--
92-
93:The crossover is observable at $s \geq$ \placeholder{s\_onset}: at lower sparsity levels, importance-based eviction maintains an advantage (or comparable performance) in both phases. The onset of crossover thus marks a phase transition in the compound interaction---the point at which sparsity is sufficient for head pruning to degrade the importance metric's phase-specific discriminability.
94-
--
101-
102:Table~\ref{tab:cross-model} compares the severity gradient across both models. Qwen2.5-7B-Instruct produces a gradient of \placeholder{G\_qwen\_s15} at $s{=}0.15$, rising to \placeholder{G\_qwen\_s30} at $s{=}0.30$, qualitatively reproducing the monotonic increase observed in DeepSeek. The absolute gradient magnitudes \placeholder{differ\_or\_match}: \placeholder{cross\_model\_detail}.
103-
--
112-\midrule
113:DeepSeek-R1-Distill-Qwen-7B & \placeholder{} & \placeholder{} & \placeholder{} & \placeholder{} \\
114:Qwen2.5-7B-Instruct         & \placeholder{} & \placeholder{} & \placeholder{} & \placeholder{} \\
115-\bottomrule
--
121-\includegraphics[width=\columnwidth]{figures/fig5_crossmodel.pdf}
122:\caption{Cross-model comparison of the severity gradient. Both DeepSeek (solid) and Qwen (dashed) exhibit monotonically increasing gradients under importance-based eviction, though the absolute magnitudes \placeholder{differ\_or\_match}.}
123-\label{fig:cross-model}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4ff71685-85e8-4572-b90c-68572f81a6a0",
  "uuid": "b1af95eb-73d4-4252-a05d-258551f4ba2f",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "11-% Evidence: v5_importance_segment, v5_random_segment\n12:[Omitted long matching line]\n13-\n--\n22-\\midrule\n23:0.15 & Importance & \\placeholder{} & \\placeholder{} & \\placeholder{} & [\\placeholder{}, \\placeholder{}] \\\\\n24:0.15 & Random     & \\placeholder{} & \\placeholder{} & \\placeholder{} & [\\placeholder{}, \\placeholder{}] \\\\\n25-\\addlinespace\n26:0.20 & Importance & \\placeholder{} & \\placeholder{} & \\placeholder{} & [\\placeholder{}, \\placeholder{}] \\\\\n27:0.20 & Random     & \\placeholder{} & \\placeholder{} & \\placeholder{} & [\\placeholder{}, \\placeholder{}] \\\\\n28-\\addlinespace\n29:0.25 & Importance & \\placeholder{} & \\placeholder{} & \\placeholder{} & [\\placeholder{}, \\placeholder{}] \\\\\n30:0.25 & Random     & \\placeholder{} & \\placeholder{} & \\placeholder{} & [\\placeholder{}, \\placeholder{}] \\\\\n31-\\addlinespace\n32:0.30 & Importance & \\placeholder{} & \\placeholder{} & \\placeholder{} & [\\placeholder{}, \\placeholder{}] \\\\\n33:0.30 & Random     & \\placeholder{} & \\placeholder{} & \\placeholder{} & [\\placeholder{}, \\placeholder{}] \\\\\n34-\\bottomrule\n--\n38-% Evidence: v5_importance_segment\n39:The gradient growth is sub-exponential: successive ratios between adjacent sparsity levels are \\placeholder{r\\_15\\_20}$\\times$, \\placeholder{r\\_20\\_25}$\\times$, and \\placeholder{r\\_25\\_30}$\\times$---a decreasing growth rate. This pattern suggests a ceiling effect at higher sparsity levels, where compound degradation in the low-sparsity phase saturates. Figure~\\ref{fig:hero} visualizes this trajectory, contrasting the steep importance-based curve against the flat random baseline.\n40-\n--\n43-\\includegraphics[width=\\columnwidth]{figures/fig1_hero.pdf}\n44:\\caption{Severity gradient ($G$) as a function of sparsity level $s$. Importance-based eviction (solid) exhibits a monotonically increasing gradient from \\placeholder{} to \\placeholder{}$\\times$, while random eviction (dashed) remains flat near $1\\times$. Shaded regions denote 95\\% bootstrap confidence intervals.}\n45-\\label{fig:hero}\n--\n59-\\midrule\n60:0.15 & \\placeholder{} & [\\placeholder{}, \\placeholder{}] & \\placeholder{} & [\\placeholder{}, \\placeholder{}] \\\\\n61:0.20 & \\placeholder{} & [\\placeholder{}, \\placeholder{}] & \\placeholder{} & [\\placeholder{}, \\placeholder{}] \\\\\n62:0.25 & \\placeholder{} & [\\placeholder{}, \\placeholder{}] & \\placeholder{} & [\\placeholder{}, \\placeholder{}] \\\\\n63:0.30 & \\placeholder{} & [\\placeholder{}, \\placeholder{}] & \\placeholder{} & [\\placeholder{}, \\placeholder{}] \\\\\n64-\\bottomrule\n--\n74-\n75:We report medians throughout because the II distribution is heavily right-skewed: mean/median ratios reach \\placeholder{skew\\_ratio}:1 at $s{=}0.30$ under importance-based eviction. A small number of problems with exceptionally long reasoning traces produce outsized II values; the median resists this influence while the bootstrap CI accounts for it via the resampling distribution.\n76-\n--\n81-% Evidence: v5_importance_segment, v5_random_segment\n82:[Omitted long matching line]\n83-\n--\n88-\\includegraphics[width=\\columnwidth]{figures/fig2_crossover.pdf}\n89:\\caption{Strategy-dependent crossover. Heatmap of median II by eviction strategy (rows) and reasoning phase (columns) at $s{=}$\\placeholder{}. Importance-based eviction outperforms random in the high-sparsity phase but produces \\placeholder{}$\\times$ higher II in the low-sparsity phase, reversing the strategy ranking.}\n90-\\label{fig:crossover}\n--\n92-\n93:The crossover is observable at $s \\geq$ \\placeholder{s\\_onset}: at lower sparsity levels, importance-based eviction maintains an advantage (or comparable performance) in both phases. The onset of crossover thus marks a phase transition in the compound interaction---the point at which sparsity is sufficient for head pruning to degrade the importance metric's phase-specific discriminability.\n94-\n--\n101-\n102:Table~\\ref{tab:cross-model} compares the severity gradient across both models. Qwen2.5-7B-Instruct produces a gradient of \\placeholder{G\\_qwen\\_s15} at $s{=}0.15$, rising to \\placeholder{G\\_qwen\\_s30} at $s{=}0.30$, qualitatively reproducing the monotonic increase observed in DeepSeek. The absolute gradient magnitudes \\placeholder{differ\\_or\\_match}: \\placeholder{cross\\_model\\_detail}.\n103-\n--\n112-\\midrule\n113:DeepSeek-R1-Distill-Qwen-7B & \\placeholder{} & \\placeholder{} & \\placeholder{} & \\placeholder{} \\\\\n114:Qwen2.5-7B-Instruct         & \\placeholder{} & \\placeholder{} & \\placeholder{} & \\placeholder{} \\\\\n115-\\bottomrule\n--\n121-\\includegraphics[width=\\columnwidth]{figures/fig5_crossmodel.pdf}\n122:\\caption{Cross-model comparison of the severity gradient. Both DeepSeek (solid) and Qwen (dashed) exhibit monotonically increasing gradients under importance-based eviction, though the absolute magnitudes \\placeholder{differ\\_or\\_match}.}\n123-\\label{fig:cross-model}",
    "numLines": 61
  }
}
```

</details>

---

### Assistant

_source line 26_

<details><summary>Logged reasoning block</summary>

```text
Good - `\placeholder{}` is used extensively in the results section. Let me check if it's defined somewhere as a LaTeX command.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4ff71685-85e8-4572-b90c-68572f81a6a0",
  "uuid": "8da9dd23-2322-4487-bba4-2897e3d99f5c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SPKcDVsMfAdjVbAPKLZNBo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1640,
      "cache_read_input_tokens": 35446,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1640
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

_source line 27_

Good, `\placeholder{}` is already in use. Now I have everything needed. Let me write the analysis section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4ff71685-85e8-4572-b90c-68572f81a6a0",
  "uuid": "d971a9a5-5127-4f4f-a8b6-c8f149a78ac7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SPKcDVsMfAdjVbAPKLZNBo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1640,
      "cache_read_input_tokens": 35446,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1640
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__write_paper_section · `toolu_01X4khxBvkipRrCXP75ESDFT`</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "section": "analysis",
  "content": "\n\\section{Analysis: Entropy-Discrimination Collapse}\n\\label{sec:analysis}\n\nThe results in \\S\\ref{sec:experiments} reveal a striking asymmetry: importance-based eviction exhibits $12$--$75\\times$ severity amplification in low-sparsity phases, while random eviction remains flat at ${\\sim}1\\times$ across all phases. Why is compound severity phase-modulated for one strategy but not the other? We propose \\emph{entropy-discrimination collapse} as an explanatory mechanism: head pruning redistributes attention mass in a phase-dependent manner, degrading the discriminative power of importance scores precisely in phases where attention is already broadly distributed.\n\n\\subsection{Attention Redistribution Under Head Pruning}\n\\label{sec:attn-redistribution}\n\nWhen a fraction $s$ of attention heads are pruned, the surviving heads must compensate for the lost information pathways. We characterize this compensation through the attention entropy of a surviving head $h$ at query position $i$:\n\\begin{equation}\n    \\mathcal{H}_i^{(h)} = -\\sum_{j=1}^{T} a_{ij}^{(h)} \\log a_{ij}^{(h)}\n    \\label{eq:attn-entropy}\n\\end{equation}\nHigher $\\mathcal{H}$ indicates more uniformly distributed attention. The effect of pruning on $\\mathcal{H}$ depends critically on the reasoning phase.\n\nIn the \\textbf{high-sparsity phase}, attention is already concentrated on a few key positions ($\\mathcal{H}$ is low). Head redundancy is high---concentrated attention patterns are likely to overlap across heads---so pruning removes largely redundant capacity. The surviving heads continue to attend to the same narrow set of positions, and $\\mathcal{H}$ changes minimally.\n\nIn the \\textbf{low-sparsity phase}, attention distributes broadly across many positions ($\\mathcal{H}$ is already elevated). Head redundancy is low: each head captures partially non-overlapping information. Pruning forces surviving heads to broaden their attention further to compensate for the lost coverage, pushing $\\mathcal{H}$ above its already high baseline.\n\n\\placeholder{Empirical attention entropy: mean $\\mathcal{H}$ per phase, pre- and post-pruning at $s \\in \\{0.15, 0.25\\}$, showing differential entropy increase concentrated in the low-sparsity phase.}\n\n\\subsection{Discrimination Collapse in Importance Scoring}\n\\label{sec:discrimination-collapse}\n\nThe KV importance score (Eq.~\\ref{eq:kv-importance}) aggregates attention mass across all surviving heads. When pruning increases the attention entropy of these heads, the cumulative importance scores become more uniform: the gap between the most-attended and least-attended positions shrinks. We hypothesize that this uniformity degrades the \\emph{discriminative power} of importance-based eviction---the ability to reliably distinguish positions critical for the model's computation from those that can be safely removed.\n\nWhen the importance distribution has low entropy (a few positions dominate), thresholding the bottom-$s$ fraction removes genuinely unimportant positions. When the distribution is near-uniform, the same thresholding becomes noise-sensitive: small perturbations change which positions cross the eviction boundary. In the limit of perfectly uniform importance scores, importance-based eviction degenerates into an arbitrary selection functionally equivalent to biased random eviction.\n\n\\placeholder{Importance score concentration (Gini coefficient or max-to-median ratio) across phases, pre- and post-pruning, showing discrimination collapse predominantly in the low-sparsity phase.}\n\nThis mechanism directly accounts for the crossover phenomenon (\\S\\ref{sec:crossover}). In high-sparsity phases, pruning preserves attention concentration, importance scores remain discriminative, and importance-based eviction removes genuinely less critical positions---achieving lower compound severity than random eviction. In low-sparsity phases, pruning amplifies attention entropy, importance discrimination collapses, and importance-based eviction devolves into a biased pseudo-random process that can inadvertently remove critical positions---producing \\emph{higher} compound severity than the explicitly random baseline. The severity inversion is thus not a failure of the importance metric in isolation, but an emergent consequence of the interaction between head pruning and importance scoring conditioned on the phase-dependent attention structure.\n\nRandom eviction is immune to this mechanism: its decisions are independent of attention patterns and invariant to the redistribution caused by head pruning. This explains the flat severity gradient ($G \\approx 1$) observed under random eviction at all sparsity levels.\n\n\\subsection{Implications for Compound Sparsity}\n\\label{sec:analysis-implications}\n\nThe entropy-discrimination collapse mechanism suggests several broader conclusions.\n\n\\paragraph{Architecture generality.} The mechanism depends on two properties: (i)~attention-mass-based importance scoring for KV eviction, and (ii)~heterogeneous attention entropy across reasoning phases. Both are shared by the major KV cache compression methods---H$_2$O \\cite{h2o2024}, SnapKV \\cite{snapkv2024}, PyramidKV \\cite{pyramidkv2024}---and by any autoregressive transformer producing extended reasoning traces. We therefore expect phase-modulated compound severity to emerge whenever head pruning is combined with attention-based cache eviction, regardless of specific model architecture.\n\n\\paragraph{Testable prediction.} Any importance metric derived from attention mass should exhibit discrimination collapse in phases where attention is broadly distributed, with the severity gradient scaling with the pruning-induced entropy increase. Metrics that derive importance from sources independent of attention---such as activation magnitude or gradient-based saliency---would not be subject to the same collapse and should produce flatter severity gradients. This prediction is directly testable in future work.\n\n\\paragraph{Reframing compound severity.} The flat random baseline ($G \\approx 1$) demonstrates that phase-modulated severity amplification is not an inherent cost of compound sparsity \\emph{per se}. Rather, it is an emergent interaction between the eviction strategy and the phase-dependent structure of attention. This reframes compound severity as a \\emph{strategy-phase interaction}---one that a phase-aware sparsity controller could, in principle, mitigate by adjusting the eviction budget or strategy per phase.\n",
  "claims": [
    {
      "text": "Head pruning causes phase-dependent attention redistribution: entropy increases more in low-sparsity phases due to lower head redundancy",
      "type": "mechanistic_hypothesis",
      "evidence": [
        "conceptual_argument"
      ],
      "decisions": [
        "D015"
      ]
    },
    {
      "text": "Attention redistribution degrades discriminative power of importance scores, causing importance-based eviction to degenerate toward biased random eviction in low-sparsity phases",
      "type": "mechanistic_hypothesis",
      "evidence": [
        "conceptual_argument",
        "crossover_phenomenon_C3"
      ],
      "decisions": [
        "D015"
      ]
    },
    {
      "text": "Random eviction is immune to entropy-discrimination collapse because its decisions are independent of attention patterns",
      "type": "explanatory",
      "evidence": [
        "flat_gradient_C1"
      ],
      "decisions": []
    },
    {
      "text": "The mechanism is architecture-general: any attention-mass-based importance metric combined with head pruning should exhibit phase-modulated compound severity",
      "type": "prediction",
      "evidence": [
        "conceptual_argument"
      ],
      "decisions": [
        "D015"
      ]
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
  "session_id": "4ff71685-85e8-4572-b90c-68572f81a6a0",
  "uuid": "be294e43-9e26-493b-84c9-577224316b78",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SPKcDVsMfAdjVbAPKLZNBo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1640,
      "cache_read_input_tokens": 35446,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1640
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

_source line 29 · 2026-05-14T05:43:06.433Z_

<details><summary>↩ Tool result · `toolu_01X4khxBvkipRrCXP75ESDFT`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"section_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/analysis.tex\", \"provenance_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper_provenance.yaml\", \"version\": 8, \"coverage\": \"6/6\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4ff71685-85e8-4572-b90c-68572f81a6a0",
  "uuid": "499a8f9b-2af8-4a4e-8456-78c5dbb5f698",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"section_path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/analysis.tex\\\", \\\"provenance_path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper_provenance.yaml\\\", \\\"version\\\": 8, \\\"coverage\\\": \\\"6/6\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"section_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/analysis.tex\", \"provenance_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper_provenance.yaml\", \"version\": 8, \"coverage\": \"6/6\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 30_

Also writing a copy to the artifacts path specified in the task.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4ff71685-85e8-4572-b90c-68572f81a6a0",
  "uuid": "a07fd0a3-dd75-4c4a-808c-5c75b1dc11b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bmaw6NndoMf2XPNbjYeUKN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2068,
      "cache_read_input_tokens": 37086,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2068
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

_source line 31_

<details open><summary>🔧 Tool call — Bash · `toolu_01RoZXpHjPzGRRsc1hcUYxkZ`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/",
  "description": "List paper artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4ff71685-85e8-4572-b90c-68572f81a6a0",
  "uuid": "4467208b-650a-4a0c-9cef-3516ff599fbc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bmaw6NndoMf2XPNbjYeUKN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2068,
      "cache_read_input_tokens": 37086,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2068
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

_source line 32 · 2026-05-14T05:43:11.058Z_

<details><summary>↩ Tool result · `toolu_01RoZXpHjPzGRRsc1hcUYxkZ`</summary>

```text
analysis.tex
background.tex
background_fc6d1d.tex
methodology.tex
methodology_4cc5f3.tex
related_work.tex
related_work_46fb53.tex
results.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4ff71685-85e8-4572-b90c-68572f81a6a0",
  "uuid": "c714c225-4c9d-4b40-a96b-e72dc009fa11",
  "tool_use_result": {
    "stdout": "analysis.tex\nbackground.tex\nbackground_fc6d1d.tex\nmethodology.tex\nmethodology_4cc5f3.tex\nrelated_work.tex\nrelated_work_46fb53.tex\nresults.tex",
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

_source line 33_

<details open><summary>🔧 Tool call — Read · `toolu_01DxRG6Buk12meQcuaEFUqX8`</summary>

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
  "session_id": "4ff71685-85e8-4572-b90c-68572f81a6a0",
  "uuid": "b7c2ea65-e225-4def-ad24-730a53733d53",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WTfQBaMpB9ngAQmF277gt8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 186,
      "cache_read_input_tokens": 39154,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 186
      },
      "output_tokens": 51,
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

_source line 34 · 2026-05-14T05:43:14.559Z_

<details><summary>↩ Tool result · `toolu_01DxRG6Buk12meQcuaEFUqX8`</summary>

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
  "session_id": "4ff71685-85e8-4572-b90c-68572f81a6a0",
  "uuid": "2b9fb1fe-f6fc-402a-8f7f-a7322802008e",
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

### Assistant

_source line 35_

Section written and registered. The file is at both `docs/paper/analysis.tex` (via `write_paper_section`) and `artifacts/_project/paper/analysis.tex`.

**Structure delivered:**
- **Opening paragraph**: poses the question (why phase-modulated for importance but not random?), introduces entropy-discrimination collapse
- **§6.1 Attention Redistribution**: defines attention entropy $\mathcal{H}$, argues pruning increases $\mathcal{H}$ asymmetrically across phases due to differential head redundancy; `\placeholder{}` for empirical entropy measurements
- **§6.2 Discrimination Collapse**: links entropy increase → uniform importance scores → noise-sensitive eviction → degeneracy to biased random; `\placeholder{}` for Gini/concentration metrics; explains crossover via the mechanism; notes random's immunity
- **§6.3 Implications**: architecture generality (H₂O/SnapKV/PyramidKV all affected), testable prediction (attention-independent metrics should be immune), reframing compound severity as strategy-phase interaction

**Framing constraints respected**: consistently frames as "emergent phase-strategy interaction," explicitly states the severity inversion is "not a failure of the importance metric in isolation" (line 32). Uses "we hypothesize" / "we propose" for unverified claims. Two `\placeholder{}` blocks mark where empirical data (C4) should go.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4ff71685-85e8-4572-b90c-68572f81a6a0",
  "uuid": "5178dc5f-e37f-427a-b96a-3a3d8ebcd2e1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Usijx8A5WEiAkCAf4XJcfM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1703,
      "cache_read_input_tokens": 39340,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1703
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

_source line 36_

Section written and registered. The file is at both `docs/paper/analysis.tex` (via `write_paper_section`) and `artifacts/_project/paper/analysis.tex`.

**Structure delivered:**
- **Opening paragraph**: poses the question (why phase-modulated for importance but not random?), introduces entropy-discrimination collapse
- **§6.1 Attention Redistribution**: defines attention entropy $\mathcal{H}$, argues pruning increases $\mathcal{H}$ asymmetrically across phases due to differential head redundancy; `\placeholder{}` for empirical entropy measurements
- **§6.2 Discrimination Collapse**: links entropy increase → uniform importance scores → noise-sensitive eviction → degeneracy to biased random; `\placeholder{}` for Gini/concentration metrics; explains crossover via the mechanism; notes random's immunity
- **§6.3 Implications**: architecture generality (H₂O/SnapKV/PyramidKV all affected), testable prediction (attention-independent metrics should be immune), reframing compound severity as strategy-phase interaction

**Framing constraints respected**: consistently frames as "emergent phase-strategy interaction," explicitly states the severity inversion is "not a failure of the importance metric in isolation" (line 32). Uses "we hypothesize" / "we propose" for unverified claims. Two `\placeholder{}` blocks mark where empirical data (C4) should go.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 148708,
  "duration_api_ms": 149102,
  "num_turns": 12,
  "stop_reason": "end_turn",
  "session_id": "4ff71685-85e8-4572-b90c-68572f81a6a0",
  "total_cost_usd": 0.4634785,
  "usage": {
    "input_tokens": 13,
    "cache_creation_input_tokens": 29596,
    "cache_read_input_tokens": 270227,
    "output_tokens": 5661,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 29596,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 331,
        "cache_read_input_tokens": 39340,
        "cache_creation_input_tokens": 1703,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1703
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1695,
      "outputTokens": 21,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0018,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 13,
      "outputTokens": 5661,
      "cacheReadInputTokens": 270227,
      "cacheCreationInputTokens": 29596,
      "webSearchRequests": 0,
      "costUSD": 0.4616785,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "83b1f77e-1641-431d-a4e8-c3a2897417b8"
}
```

</details>

---
