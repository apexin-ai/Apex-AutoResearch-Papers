# research paper update prep

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 82
- **Recorded user turns:** 0
- **Tool calls:** 29
- **Original source:** `logs/workers/worker_research_paper_update_prep_20260515T013953.log`
- **Structured JSON:** [`9ddf665d178cda9226ff.json`](../../sessions/9d/9ddf665d178cda9226ff.json)

## Before a recorded user message

82 recorded events

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
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
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
  "uuid": "89ad8c65-0352-4dfd-9400-f3dfb4725ee1",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/memory/"
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
    "resetsAt": 1778812800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "992021b6-e934-4cd5-b347-8843302ff2f3",
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the paper framing document and then exploring the paper directory to find all files that need updating.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "e1d58b61-87d7-4383-9bc2-d8b6d0e0242c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FiXzsbRPCpz3VaYNsdQvzX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11773,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11773
      },
      "output_tokens": 27,
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

I'll read the paper framing and explore the paper directory in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "d02484c2-fe41-4c79-b462-d6af0040358e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FiXzsbRPCpz3VaYNsdQvzX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11773,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11773
      },
      "output_tokens": 27,
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01UGpd38NHdDF25UwAJFUoMH`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
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
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "64b3a48f-47b6-41b6-b4f6-77b50e1c7c37",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FiXzsbRPCpz3VaYNsdQvzX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11773,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11773
      },
      "output_tokens": 27,
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

_source line 7 · 2026-05-15T01:40:03.770Z_

<details><summary>↩ Tool result · `toolu_01UGpd38NHdDF25UwAJFUoMH`</summary>

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
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "9430b999-c81b-45f0-b605-86980054d553",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Glob · `toolu_0182MuzyatnU6wckgLbWBxh1`</summary>

```json
{
  "pattern": "**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "24e6a22a-0fb0-4a78-be6b-8d891f7aefb6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FiXzsbRPCpz3VaYNsdQvzX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11773,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11773
      },
      "output_tokens": 27,
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

_source line 9 · 2026-05-15T01:40:04.126Z_

<details><summary>↩ Tool result · reported error · `toolu_0182MuzyatnU6wckgLbWBxh1`</summary>

```text
&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "a31e150b-8ad1-4a98-80db-fde62dd9b41b",
  "tool_use_result": "Error: Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse."
}
```

</details>

---

### Assistant

_source line 10_

<details><summary>Logged reasoning block</summary>

```text
The paper directory doesn't exist at that path. Let me find where the paper files actually are and read the paper framing document.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "3d9ba357-5824-4cb6-a4cc-51ff1021db00",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KemX3tjbVcxshf8u7D5L9H",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 967,
      "cache_read_input_tokens": 23220,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 967
      },
      "output_tokens": 18,
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

Let me find the actual paper directory and read the framing document.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "a62a8861-1c22-493f-be96-59a0fa804628",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KemX3tjbVcxshf8u7D5L9H",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 967,
      "cache_read_input_tokens": 23220,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 967
      },
      "output_tokens": 18,
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01J5xSerJ94aepc4GomRGbL8`</summary>

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
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "e0a52b3b-f40c-418c-9bf6-3d714b0ed44c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KemX3tjbVcxshf8u7D5L9H",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 967,
      "cache_read_input_tokens": 23220,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 967
      },
      "output_tokens": 18,
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

_source line 13 · 2026-05-15T01:40:10.280Z_

<details><summary>↩ Tool result · `toolu_01J5xSerJ94aepc4GomRGbL8`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper_framing.md\", \"content\": \"# Paper Framing — Phase-Gated Compound Sparsity\\n\\n> 最后更新: 2026-05-14 (D060 C8 partially_confirmed; D056 C5b future_work; D059 d_z 分场景) | 维护者: Director\\n\\n## Core Insight\\n\\nCompound sparsity（attention head pruning + KV cache eviction）的 severity 不是固定常数——它是 eviction strategy 和 reasoning phase 交互的涌现属性。Importance-based eviction 的 compound interaction severity（paired median difference: median(II_low_i − II_high_i)）随 sparsity 单调递增（DeepSeek: 0.32→1.15→3.97→9.94; Qwen: 0.048→0.208→1.109→2.619），而 random masking 三相 II 持平（7/8 FAIL; Qwen s030 PASS p=0.012 but d=-0.04 negligible）。Cohen's d（paired d_z, B=10000）从 small-medium 到 large（DeepSeek: 0.44→0.80; Qwen: 0.28→1.02，s015 边缘）。LLaMA 跨架构验证（D060）qualitative direction consistent（within-importance d_z~1.0），但 strategy×phase 交互弱于 Qwen2 架构（imp_vs_rand d_z 0.19→0.34, 仅 s030 显著），且 random 在 LLaMA 上也显示显著 phase gradient（d_z 0.35→0.44），与 DeepSeek/Qwen random 7/8 FAIL 模式定性不同。这一发现挑战了 compound degradation 均匀分布的隐含假设。\\n\\n**数字基准**：所有数字基于 bf16 per-problem paired 统计量（B=10000 bootstrap）。median_diff 定义为 median(II_low_i − II_high_i)（逐 problem 配对差的中位数）。fp16 旧数据已弃用。\\n\\n## Narrative Arc\\n\\nCompound sparsity 是高效 LLM 推理的实用部署需求，但 prior work（SparK, Ada-KV, SLiM）将 compound interaction 视为均匀超可加。我们发现 severity 是 strategy × phase 交互的涌现属性：importance eviction 的 compound interaction 在 low-sparsity phase 远大于 high-sparsity phase（paired median difference 单调递增 0.32→9.94），而 random eviction 在所有 phase 保持平坦（7/8 FAIL; 唯一例外 Qwen s030 p=0.012 效应量可忽略 d=-0.04）。Cross-model replication 方向一致（Qwen magnitude ~1/4 of DeepSeek，onset threshold s≥0.20）。LLaMA 跨架构验证已完成（c3_llama, D060）：qualitative direction consistent（importance phase gradient d_z≈1.0），但 imp_vs_rand 交互弱（d_z 0.19→0.34, 仅 s030 显著），且 random 也显示非平凡 phase gradient（d_z 0.35→0.44），strategy-dependence 强度 architecture-dependent。我们通过 discrimination collapse 机制解释这一现象：head pruning → importance score 的判别力崩塌（Gini/CV 下降跨模型一致）→ importance eviction 退化为有偏伪随机。Attention entropy redistribution 作为 model-dependent secondary effect 在 DeepSeek 上观察到，但在 Qwen 上不稳健（D044）。\\n\\n**Framing 硬约束（D015）**：\\n- MUST: \\\\\\\\\\\\\\\"emergent phase-strategy interaction\\\\\\\\\\\\\\\"\\n- MUST NOT: \\\\\\\\\\\\\\\"importance metric limitation / importance is broken\\\\\\\\\\\\\\\"\\n- MUST NOT: claim \\\\\\\\\\\\\\\"importance masking produces super-additive interaction\\\\\\\\\\\\\\\" without qualifier — random masking also produces positive II. The distinguishing signal is **phase-dependent gradient** (importance: paired median difference 0.32→9.94 单调递增 vs random: 7/8 FAIL), not the existence of super-additivity itself (D023)\\n\\n## Core Claims\\n\\n| ID | Claim | Status | Key Evidence |\\n|----|-------|--------|-------------|\\n| C1 | Compound sparsity severity is strategy-dependent | confirmed | importance paired median diff 0.32→9.94 单调递增 vs random 7/8 FAIL (bf16; Qwen s030 PASS p=0.012 d=-0.04 negligible) |\\n| C2 | Severity is phase-modulated (amplified in low-sparsity phase) | confirmed | bf16 paired median difference 单调递增: 0.32→1.15→3.97→9.94; Bonferroni p<0.005 全 4 水平 (D032)。预注册：n=500 后若 QW s015 CI 仍跨零，叙事改为 'compound effect emerges above threshold sparsity (~s020)' |\\n| C3 | Phase-strategy crossover exists | confirmed | s=0.25: importance high_phase=0.032 < random=0.818, importance low_phase=7.196 > random=1.363 (bf16) |\\n| C4 | Discrimination collapse as primary mechanism; entropy redistribution model-dependent | partially_confirmed | D044: Gini/CV 下降跨模型一致; entropy collapse DeepSeek 一致但 Qwen s025 反转(+0.045) s030≈0。30/30 problems completed. |\\n| C5 | Phase-modulated compound severity generalizes across models | confirmed | DeepSeek + Qwen cross-model replication: 方向一致, Cohen's d ρ=1.0, gradient permutation p=0.043. Qwen magnitude ~1/4 of DeepSeek, onset threshold s≥0.20 (S3→C). |\\n| C5b | Phase-aware mitigation recovers compound degradation | future_work | D056: pilot 完成 gate_failed。Oracle recovery 18% < 30% gate (Wilcoxon p=0.002)，heuristic 32% 但 CI 跨零。方向正确但效应量不足，需更精细 phase boundary estimation → future work |\\n| C6 | Severity gradient is sub-exponential | confirmed | Growth rate decreasing: Δ增长因子 3.8×→4.8×→2.0×（递减） |\\n| C7 | Statistical power at n=500 confirms dose-response | running | c2_n500_deepseek + c2_qw_n500 (n=500, 8 conditions each) |\\n| C8 | Cross-architecture validation (LLaMA) | partially_confirmed | D060: within-importance phase gradient 强(d_z~1.0) ✓，但 imp_vs_rand 交互弱(d_z 0.19→0.34, 仅 s030 Bonferroni p=0.029 显著)。**关键**：random 在 LLaMA 上也显示显著 phase gradient(d_z 0.35→0.44, CI 排除零)，与 DeepSeek/Qwen random 7/8 FAIL 模式定性不同。Qualitative direction consistent, quantitative strategy×phase interaction weaker + architecture-dependent。论文禁用 \\\"confirms\\\"，改用 \\\"suggests\\\"/\\\"provides partial support\\\"。 |\\n| C9 | Differentiation from Lethe/SparK prior work | planned | Related Work §2 引用区分 + SparK gap analysis |\\n| S3→C | Onset threshold is model-dependent (DeepSeek s≥0.15, Qwen s≥0.20) | confirmed | D037/D038: Qwen s015 d=0.28 CI含0, s020+ 显著 |\\n| S7→C | Dose-response monotonicity (Spearman ρ=1.0) | confirmed | D047: 6-point dose-response, 单调递增 |\\n\\n## Anticipated Reviewer Concerns\\n\\n### RC1: Generalizability — 7B models only, single benchmark\\n- **预期质疑**: \\\\\\\"Results on two 7B models and MATH-500 only. How do we know this generalizes to larger models or other reasoning tasks?\\\\\\\"\\n- **应对**: 三层泛化证据：(1) Cross-model: DeepSeek-R1-Distill-Qwen-7B + Qwen2.5-7B-Instruct（同架构不同训练，ρ=1.0）(2) Cross-architecture: c3_llama (DeepSeek-R1-Distill-Llama-8B, LlamaForCausalLM)，qualitative direction consistent，但需加限定——LLaMA 上 random 也显示 phase gradient，strategy × phase 交互弱于 Qwen2 架构（D060）。Limitations 诚实声明：(a) 7B scale only；(b) 单 benchmark (MATH-500)；(c) LLaMA 跨架构验证 n=50 限制功效，交互效应量弱于同架构模型；(d) random phase gradient 行为 architecture-dependent。\\n- **实验支撑**: C5 (cross-model) + C8 (c3_llama cross-architecture, partially_confirmed D060)\\n\\n### RC2: Mechanism — entropy-discrimination collapse 缺乏直接测量\\n- **预期质疑**: \\\\\\\"The mechanism is conceptual. Where is the empirical evidence for entropy increase and discrimination collapse?\\\\\\\"\\n- **应对**: c4_entropy 实验已完成（DeepSeek 30/30 + Qwen 30/30）。D044 结论：Gini/CV 下降跨模型一致（discrimination collapse confirmed）；entropy redistribution 在 DeepSeek 上一致但在 Qwen 上 s025 方向反转、s030 近零（model-dependent）。论文以 discrimination collapse 为主线，entropy 作 DeepSeek 特有的强化因素。\\n- **实验支撑**: c4_entropy (DeepSeek DONE) + qwen_c4_entropy (DONE, negative for entropy universality)\\n\\n### RC3: Practical impact — 没有 throughput 数据\\n- **预期质疑**: \\\\\\\"No wall-clock or throughput measurements. Is the severity amplification reflected in actual inference speed?\\\\\\\"\\n- **应对**: 本文定位是 empirical finding paper（发现 + 机制解释），不是 method paper。Throughput 不是 claim 的一部分。Discussion 中明确 phase-gated controller 作为 future direction。\\n  - C5b pilot 已完成（D056）：oracle recovery 18%（Wilcoxon p=0.002），heuristic recovery 32%（p=0.024），但两者 95% CI 均跨零。方向正确（Wilcoxon 显著）但效应量不足（未达 30% gate），需更精细的 phase boundary estimation。论文 §6 Discussion 诚实报告 pilot 结果 + future work。\\n  - Heuristic > oracle 悖论值得提及：token position ratio 粗粒度划分可能恰好更适合 mitigation 场景，暗示 phase boundary 的最优粒度是开放问题。\\n- **实验支撑**: c5b_pilot (gate_failed, D056)\\n\\n### RC4: Statistical rigor — bootstrap 是否足够\\n- **预期质疑**: \\\\\\\"Per-problem bootstrap with 50 problems — sufficient sample size?\\\\\\\"\\n- **应对**: bf16 使用 B=10000 per-problem paired bootstrap，有效配对数 n=49 (DeepSeek) / n=46 (Qwen)。Permutation test 使用 paired median difference 作为 robust statistic（D032），Bonferroni 校正后全 4 水平 p<0.005。Cohen's d（paired d_z）作为辅助效应量（DeepSeek 0.44→0.80, Qwen 0.28→1.02）。可在 appendix 补充 per-problem 分布图（已生成 fig4_per_problem_dist.pdf）。\\n- **实验支撑**: bf16 permutation test (D032) + Cohen's d per-problem paired (rebootstrap B=10000) 已完成\\n\\n### RC5: Novelty — prior work 是否已覆盖 phase-dependent sparsity\\n- **预期质疑**: \\\"ThinKV and phase-aware methods already consider phase. What's new?\\\"\\n- **应对**: Prior work 在单轴上分析 phase（ThinKV: phase-aware eviction）或 compound（SparK: joint compression）。没有工作同时分析 compound × phase × strategy 的三维交互。Crossover 现象（同一 strategy 在不同 phase 方向反转）是全新发现。Related Work 加 Lethe 引用区分 + SparK 对比。具体区分：\\n  - **ThinKV** (arxiv 2510.01290, Oct 2025): 在 KV cache 单轴上做 phase-aware 压缩（按 CoT 阶段差异化 eviction），但不涉及 pruning × eviction 的 compound interaction。我们研究的是双轴（head pruning × KV eviction）compound interaction 如何随 phase 变化，ThinKV 的单轴 phase-aware 策略是我们分析维度的子集。\\n  - **Physics of KV Cache Compression** (arxiv 2603.01426, Mar 2026): 揭示了单轴 KV 压缩的 phase transition 和 representational rigidity，是机制层面最接近的工作。关键区分：他们刻画的是单一压缩轴上压缩率的 critical threshold（phase transition），我们刻画的是两种压缩方法的 compound interaction severity 如何被 reasoning phase 调制（phase-dependent gradient）——维度正交。\\n  - **HIES** (arxiv 2510.13832, Oct 2025): 发现 importance score collapse 并提出 entropy 补偿，为我们的 discrimination collapse 机制提供独立 supporting evidence——他们在单轴上观察到的 score collapse 正是我们在 compound setting 中发现的 Gini/CV 下降的单轴对应。\\n  - **R-KV** (arxiv 2505.24133, May 2025): 针对 reasoning task 做 KV compression 优化，属于 task-specific method。我们不是提出新方法，而是 mechanistic 分析 compound interaction 的 phase-dependent 行为，二者目标不同（optimization vs understanding）。\\n- **实验支撑**: C3 (crossover), Related Work §2 的 gap 分析\\n\\n### RC6: Novelty vs Lethe/SparK\\n- **预期质疑**: \\\"How does this differ from Lethe (AAAI 2026) which also does layer-time-adaptive KV pruning, or SparK which studies compound compression?\\\"\\n- **应对**: Lethe 和 SparK 都没有分析 phase × strategy 的交互效应。Lethe 是 method paper（提出 adaptive eviction 方法），我们是 empirical finding paper（发现 phase-dependent severity gradient）。SparK 研究 compound compression 但将 interaction 视为均匀超可加，我们发现 interaction severity 随 phase 和 strategy 变化。新近工作进一步确认我们的独特定位：\\n  - **Physics of KV Cache Compression** (arxiv 2603.01426, Mar 2026) 是最近的相关工作，研究单轴压缩的 phase transition 阈值行为。与我们的核心区别：他们的 phase transition 是压缩率维度上的 critical point，我们的 phase-dependent gradient 是 reasoning phase 维度上 compound interaction 的连续调制——两者刻画的 \\\"phase\\\" 语义不同（compression-rate phase vs reasoning phase）。\\n  - **ThinKV** (arxiv 2510.01290, Oct 2025) 和 **R-KV** (arxiv 2505.24133, May 2025) 都在 KV compression 单轴上引入 phase/reasoning awareness，但均未涉及 compound interaction。我们的贡献在于揭示 pruning × eviction 双轴交互如何被 reasoning phase 调制，这是单轴方法无法观察到的涌现现象。\\n  - **HIES** (arxiv 2510.13832, Oct 2025) 的 importance score collapse 发现为我们的 discrimination collapse 机制提供了独立佐证，但 HIES 聚焦于单轴补偿方法，未研究 collapse 在 compound setting 中的放大效应。\\n  - Related Work §2 明确区分三者定位：Lethe/SparK = method/compound method, ThinKV/R-KV = single-axis phase-aware, Physics of KV = single-axis phase transition, HIES = single-axis collapse。我们 = compound × phase × strategy 三维交互分析。\\n- **实验支撑**: 不需要额外实验，仅需 §2 引用区分\\n\\n## Paper Positioning\\n\\n**类型**: Empirical finding paper（非 method paper）\\n**核心贡献**:\\n1. 发现 compound sparsity severity 的 strategy × phase 交互\\n2. 量化 severity gradient（bf16 paired median difference 0.32→9.94, Cohen's d 0.44→0.80）和 crossover 现象\\n3. 提出 discrimination collapse 机制解释（Gini/CV 跨模型一致；entropy redistribution model-dependent）\\n4. Cross-model + cross-architecture (LLaMA) replication 验证泛化性（三模型两架构；LLaMA partially_confirmed，strategy×phase 交互强度 architecture-dependent, D060）\\n\\n**投稿目标**: EMNLP 2026 ARR, deadline 2026-05-25\\n**Rebuttal 准备**: Day 9 (2026-05-23) 预留 rebuttal letter 写作时间\\n**关键时间线**：\\n- Day 9 (2026-05-23): 预留写 rebuttal letter\\n- Day 11 (2026-05-25): EMNLP 2026 ARR 截稿\\n\", \"total_chars\": 10979, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "3aa30d27-62c7-48b9-aabc-7d5f792c5da8",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing — Phase-Gated Compound Sparsity\\\\n\\\\n> 最后更新: 2026-05-14 (D060 C8 partially_confirmed; D056 C5b future_work; D059 d_z 分场景) | 维护者: Director\\\\n\\\\n## Core Insight\\\\n\\\\nCompound sparsity（attention head pruning + KV cache eviction）的 severity 不是固定常数——它是 eviction strategy 和 reasoning phase 交互的涌现属性。Importance-based eviction 的 compound interaction severity（paired median difference: median(II_low_i − II_high_i)）随 sparsity 单调递增（DeepSeek: 0.32→1.15→3.97→9.94; Qwen: 0.048→0.208→1.109→2.619），而 random masking 三相 II 持平（7/8 FAIL; Qwen s030 PASS p=0.012 but d=-0.04 negligible）。Cohen's d（paired d_z, B=10000）从 small-medium 到 large（DeepSeek: 0.44→0.80; Qwen: 0.28→1.02，s015 边缘）。LLaMA 跨架构验证（D060）qualitative direction consistent（within-importance d_z~1.0），但 strategy×phase 交互弱于 Qwen2 架构（imp_vs_rand d_z 0.19→0.34, 仅 s030 显著），且 random 在 LLaMA 上也显示显著 phase gradient（d_z 0.35→0.44），与 DeepSeek/Qwen random 7/8 FAIL 模式定性不同。这一发现挑战了 compound degradation 均匀分布的隐含假设。\\\\n\\\\n**数字基准**：所有数字基于 bf16 per-problem paired 统计量（B=10000 bootstrap）。median_diff 定义为 median(II_low_i − II_high_i)（逐 problem 配对差的中位数）。fp16 旧数据已弃用。\\\\n\\\\n## Narrative Arc\\\\n\\\\nCompound sparsity 是高效 LLM 推理的实用部署需求，但 prior work（SparK, Ada-KV, SLiM）将 compound interaction 视为均匀超可加。我们发现 severity 是 strategy × phase 交互的涌现属性：importance eviction 的 compound interaction 在 low-sparsity phase 远大于 high-sparsity phase（paired median difference 单调递增 0.32→9.94），而 random eviction 在所有 phase 保持平坦（7/8 FAIL; 唯一例外 Qwen s030 p=0.012 效应量可忽略 d=-0.04）。Cross-model replication 方向一致（Qwen magnitude ~1/4 of DeepSeek，onset threshold s≥0.20）。LLaMA 跨架构验证已完成（c3_llama, D060）：qualitative direction consistent（importance phase gradient d_z≈1.0），但 imp_vs_rand 交互弱（d_z 0.19→0.34, 仅 s030 显著），且 random 也显示非平凡 phase gradient（d_z 0.35→0.44），strategy-dependence 强度 architecture-dependent。我们通过 discrimination collapse 机制解释这一现象：head pruning → importance score 的判别力崩塌（Gini/CV 下降跨模型一致）→ importance eviction 退化为有偏伪随机。Attention entropy redistribution 作为 model-dependent secondary effect 在 DeepSeek 上观察到，但在 Qwen 上不稳健（D044）。\\\\n\\\\n**Framing 硬约束（D015）**：\\\\n- MUST: \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"emergent phase-strategy interaction\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"\\\\n- MUST NOT: \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"importance metric limitation / importance is broken\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"\\\\n- MUST NOT: claim \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"importance masking produces super-additive interaction\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\" without qualifier — random masking also produces positive II. The distinguishing signal is **phase-dependent gradient** (importance: paired median difference 0.32→9.94 单调递增 vs random: 7/8 FAIL), not the existence of super-additivity itself (D023)\\\\n\\\\n## Core Claims\\\\n\\\\n| ID | Claim | Status | Key Evidence |\\\\n|----|-------|--------|-------------|\\\\n| C1 | Compound sparsity severity is strategy-dependent | confirmed | importance paired median diff 0.32→9.94 单调递增 vs random 7/8 FAIL (bf16; Qwen s030 PASS p=0.012 d=-0.04 negligible) |\\\\n| C2 | Severity is phase-modulated (amplified in low-sparsity phase) | confirmed | bf16 paired median difference 单调递增: 0.32→1.15→3.97→9.94; Bonferroni p<0.005 全 4 水平 (D032)。预注册：n=500 后若 QW s015 CI 仍跨零，叙事改为 'compound effect emerges above threshold sparsity (~s020)' |\\\\n| C3 | Phase-strategy crossover exists | confirmed | s=0.25: importance high_phase=0.032 < random=0.818, importance low_phase=7.196 > random=1.363 (bf16) |\\\\n| C4 | Discrimination collapse as primary mechanism; entropy redistribution model-dependent | partially_confirmed | D044: Gini/CV 下降跨模型一致; entropy collapse DeepSeek 一致但 Qwen s025 反转(+0.045) s030≈0。30/30 problems completed. |\\\\n| C5 | Phase-modulated compound severity generalizes across models | confirmed | DeepSeek + Qwen cross-model replication: 方向一致, Cohen's d ρ=1.0, gradient permutation p=0.043. Qwen magnitude ~1/4 of DeepSeek, onset threshold s≥0.20 (S3→C). |\\\\n| C5b | Phase-aware mitigation recovers compound degradation | future_work | D056: pilot 完成 gate_failed。Oracle recovery 18% < 30% gate (Wilcoxon p=0.002)，heuristic 32% 但 CI 跨零。方向正确但效应量不足，需更精细 phase boundary estimation → future work |\\\\n| C6 | Severity gradient is sub-exponential | confirmed | Growth rate decreasing: Δ增长因子 3.8×→4.8×→2.0×（递减） |\\\\n| C7 | Statistical power at n=500 confirms dose-response | running | c2_n500_deepseek + c2_qw_n500 (n=500, 8 conditions each) |\\\\n| C8 | Cross-architecture validation (LLaMA) | partially_confirmed | D060: within-importance phase gradient 强(d_z~1.0) ✓，但 imp_vs_rand 交互弱(d_z 0.19→0.34, 仅 s030 Bonferroni p=0.029 显著)。**关键**：random 在 LLaMA 上也显示显著 phase gradient(d_z 0.35→0.44, CI 排除零)，与 DeepSeek/Qwen random 7/8 FAIL 模式定性不同。Qualitative direction consistent, quantitative strategy×phase interaction weaker + architecture-dependent。论文禁用 \\\\\\\"confirms\\\\\\\"，改用 \\\\\\\"suggests\\\\\\\"/\\\\\\\"provides partial support\\\\\\\"。 |\\\\n| C9 | Differentiation from Lethe/SparK prior work | planned | Related Work §2 引用区分 + SparK gap analysis |\\\\n| S3→C | Onset threshold is model-dependent (DeepSeek s≥0.15, Qwen s≥0.20) | confirmed | D037/D038: Qwen s015 d=0.28 CI含0, s020+ 显著 |\\\\n| S7→C | Dose-response monotonicity (Spearman ρ=1.0) | confirmed | D047: 6-point dose-response, 单调递增 |\\\\n\\\\n## Anticipated Reviewer Concerns\\\\n\\\\n### RC1: Generalizability — 7B models only, single benchmark\\\\n- **预期质疑**: \\\\\\\\\\\\\\\"Results on two 7B models and MATH-500 only. How do we know this generalizes to larger models or other reasoning tasks?\\\\\\\\\\\\\\\"\\\\n- **应对**: 三层泛化证据：(1) Cross-model: DeepSeek-R1-Distill-Qwen-7B + Qwen2.5-7B-Instruct（同架构不同训练，ρ=1.0）(2) Cross-architecture: c3_llama (DeepSeek-R1-Distill-Llama-8B, LlamaForCausalLM)，qualitative direction consistent，但需加限定——LLaMA 上 random 也显示 phase gradient，strategy × phase 交互弱于 Qwen2 架构（D060）。Limitations 诚实声明：(a) 7B scale only；(b) 单 benchmark (MATH-500)；(c) LLaMA 跨架构验证 n=50 限制功效，交互效应量弱于同架构模型；(d) random phase gradient 行为 architecture-dependent。\\\\n- **实验支撑**: C5 (cross-model) + C8 (c3_llama cross-architecture, partially_confirmed D060)\\\\n\\\\n### RC2: Mechanism — entropy-discrimination collapse 缺乏直接测量\\\\n- **预期质疑**: \\\\\\\\\\\\\\\"The mechanism is conceptual. Where is the empirical evidence for entropy increase and discrimination collapse?\\\\\\\\\\\\\\\"\\\\n- **应对**: c4_entropy 实验已完成（DeepSeek 30/30 + Qwen 30/30）。D044 结论：Gini/CV 下降跨模型一致（discrimination collapse confirmed）；entropy redistribution 在 DeepSeek 上一致但在 Qwen 上 s025 方向反转、s030 近零（model-dependent）。论文以 discrimination collapse 为主线，entropy 作 DeepSeek 特有的强化因素。\\\\n- **实验支撑**: c4_entropy (DeepSeek DONE) + qwen_c4_entropy (DONE, negative for entropy universality)\\\\n\\\\n### RC3: Practical impact — 没有 throughput 数据\\\\n- **预期质疑**: \\\\\\\\\\\\\\\"No wall-clock or throughput measurements. Is the severity amplification reflected in actual inference speed?\\\\\\\\\\\\\\\"\\\\n- **应对**: 本文定位是 empirical finding paper（发现 + 机制解释），不是 method paper。Throughput 不是 claim 的一部分。Discussion 中明确 phase-gated controller 作为 future direction。\\\\n  - C5b pilot 已完成（D056）：oracle recovery 18%（Wilcoxon p=0.002），heuristic recovery 32%（p=0.024），但两者 95% CI 均跨零。方向正确（Wilcoxon 显著）但效应量不足（未达 30% gate），需更精细的 phase boundary estimation。论文 §6 Discussion 诚实报告 pilot 结果 + future work。\\\\n  - Heuristic > oracle 悖论值得提及：token position ratio 粗粒度划分可能恰好更适合 mitigation 场景，暗示 phase boundary 的最优粒度是开放问题。\\\\n- **实验支撑**: c5b_pilot (gate_failed, D056)\\\\n\\\\n### RC4: Statistical rigor — bootstrap 是否足够\\\\n- **预期质疑**: \\\\\\\\\\\\\\\"Per-problem bootstrap with 50 problems — sufficient sample size?\\\\\\\\\\\\\\\"\\\\n- **应对**: bf16 使用 B=10000 per-problem paired bootstrap，有效配对数 n=49 (DeepSeek) / n=46 (Qwen)。Permutation test 使用 paired median difference 作为 robust statistic（D032），Bonferroni 校正后全 4 水平 p<0.005。Cohen's d（paired d_z）作为辅助效应量（DeepSeek 0.44→0.80, Qwen 0.28→1.02）。可在 appendix 补充 per-problem 分布图（已生成 fig4_per_problem_dist.pdf）。\\\\n- **实验支撑**: bf16 permutation test (D032) + Cohen's d per-problem paired (rebootstrap B=10000) 已完成\\\\n\\\\n### RC5: Novelty — prior work 是否已覆盖 phase-dependent sparsity\\\\n- **预期质疑**: \\\\\\\"ThinKV and phase-aware methods already consider phase. What's new?\\\\\\\"\\\\n- **应对**: Prior work 在单轴上分析 phase（ThinKV: phase-aware eviction）或 compound（SparK: joint compression）。没有工作同时分析 compound × phase × strategy 的三维交互。Crossover 现象（同一 strategy 在不同 phase 方向反转）是全新发现。Related Work 加 Lethe 引用区分 + SparK 对比。具体区分：\\\\n  - **ThinKV** (arxiv 2510.01290, Oct 2025): 在 KV cache 单轴上做 phase-aware 压缩（按 CoT 阶段差异化 eviction），但不涉及 pruning × eviction 的 compound interaction。我们研究的是双轴（head pruning × KV eviction）compound interaction 如何随 phase 变化，ThinKV 的单轴 phase-aware 策略是我们分析维度的子集。\\\\n  - **Physics of KV Cache Compression** (arxiv 2603.01426, Mar 2026): 揭示了单轴 KV 压缩的 phase transition 和 representational rigidity，是机制层面最接近的工作。关键区分：他们刻画的是单一压缩轴上压缩率的 critical threshold（phase transition），我们刻画的是两种压缩方法的 compound interaction severity 如何被 reasoning phase 调制（phase-dependent gradient）——维度正交。\\\\n  - **HIES** (arxiv 2510.13832, Oct 2025): 发现 importance score collapse 并提出 entropy 补偿，为我们的 discrimination collapse 机制提供独立 supporting evidence——他们在单轴上观察到的 score collapse 正是我们在 compound setting 中发现的 Gini/CV 下降的单轴对应。\\\\n  - **R-KV** (arxiv 2505.24133, May 2025): 针对 reasoning task 做 KV compression 优化，属于 task-specific method。我们不是提出新方法，而是 mechanistic 分析 compound interaction 的 phase-dependent 行为，二者目标不同（optimization vs understanding）。\\\\n- **实验支撑**: C3 (crossover), Related Work §2 的 gap 分析\\\\n\\\\n### RC6: Novelty vs Lethe/SparK\\\\n- **预期质疑**: \\\\\\\"How does this differ from Lethe (AAAI 2026) which also does layer-time-adaptive KV pruning, or SparK which studies compound compression?\\\\\\\"\\\\n- **应对**: Lethe 和 SparK 都没有分析 phase × strategy 的交互效应。Lethe 是 method paper（提出 adaptive eviction 方法），我们是 empirical finding paper（发现 phase-dependent severity gradient）。SparK 研究 compound compression 但将 interaction 视为均匀超可加，我们发现 interaction severity 随 phase 和 strategy 变化。新近工作进一步确认我们的独特定位：\\\\n  - **Physics of KV Cache Compression** (arxiv 2603.01426, Mar 2026) 是最近的相关工作，研究单轴压缩的 phase transition 阈值行为。与我们的核心区别：他们的 phase transition 是压缩率维度上的 critical point，我们的 phase-dependent gradient 是 reasoning phase 维度上 compound interaction 的连续调制——两者刻画的 \\\\\\\"phase\\\\\\\" 语义不同（compression-rate phase vs reasoning phase）。\\\\n  - **ThinKV** (arxiv 2510.01290, Oct 2025) 和 **R-KV** (arxiv 2505.24133, May 2025) 都在 KV compression 单轴上引入 phase/reasoning awareness，但均未涉及 compound interaction。我们的贡献在于揭示 pruning × eviction 双轴交互如何被 reasoning phase 调制，这是单轴方法无法观察到的涌现现象。\\\\n  - **HIES** (arxiv 2510.13832, Oct 2025) 的 importance score collapse 发现为我们的 discrimination collapse 机制提供了独立佐证，但 HIES 聚焦于单轴补偿方法，未研究 collapse 在 compound setting 中的放大效应。\\\\n  - Related Work §2 明确区分三者定位：Lethe/SparK = method/compound method, ThinKV/R-KV = single-axis phase-aware, Physics of KV = single-axis phase transition, HIES = single-axis collapse。我们 = compound × phase × strategy 三维交互分析。\\\\n- **实验支撑**: 不需要额外实验，仅需 §2 引用区分\\\\n\\\\n## Paper Positioning\\\\n\\\\n**类型**: Empirical finding paper（非 method paper）\\\\n**核心贡献**:\\\\n1. 发现 compound sparsity severity 的 strategy × phase 交互\\\\n2. 量化 severity gradient（bf16 paired median difference 0.32→9.94, Cohen's d 0.44→0.80）和 crossover 现象\\\\n3. 提出 discrimination collapse 机制解释（Gini/CV 跨模型一致；entropy redistribution model-dependent）\\\\n4. Cross-model + cross-architecture (LLaMA) replication 验证泛化性（三模型两架构；LLaMA partially_confirmed，strategy×phase 交互强度 architecture-dependent, D060）\\\\n\\\\n**投稿目标**: EMNLP 2026 ARR, deadline 2026-05-25\\\\n**Rebuttal 准备**: Day 9 (2026-05-23) 预留 rebuttal letter 写作时间\\\\n**关键时间线**：\\\\n- Day 9 (2026-05-23): 预留写 rebuttal letter\\\\n- Day 11 (2026-05-25): EMNLP 2026 ARR 截稿\\\\n\\\", \\\"total_chars\\\": 10979, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper_framing.md\", \"content\": \"# Paper Framing — Phase-Gated Compound Sparsity\\n\\n> 最后更新: 2026-05-14 (D060 C8 partially_confirmed; D056 C5b future_work; D059 d_z 分场景) | 维护者: Director\\n\\n## Core Insight\\n\\nCompound sparsity（attention head pruning + KV cache eviction）的 severity 不是固定常数——它是 eviction strategy 和 reasoning phase 交互的涌现属性。Importance-based eviction 的 compound interaction severity（paired median difference: median(II_low_i − II_high_i)）随 sparsity 单调递增（DeepSeek: 0.32→1.15→3.97→9.94; Qwen: 0.048→0.208→1.109→2.619），而 random masking 三相 II 持平（7/8 FAIL; Qwen s030 PASS p=0.012 but d=-0.04 negligible）。Cohen's d（paired d_z, B=10000）从 small-medium 到 large（DeepSeek: 0.44→0.80; Qwen: 0.28→1.02，s015 边缘）。LLaMA 跨架构验证（D060）qualitative direction consistent（within-importance d_z~1.0），但 strategy×phase 交互弱于 Qwen2 架构（imp_vs_rand d_z 0.19→0.34, 仅 s030 显著），且 random 在 LLaMA 上也显示显著 phase gradient（d_z 0.35→0.44），与 DeepSeek/Qwen random 7/8 FAIL 模式定性不同。这一发现挑战了 compound degradation 均匀分布的隐含假设。\\n\\n**数字基准**：所有数字基于 bf16 per-problem paired 统计量（B=10000 bootstrap）。median_diff 定义为 median(II_low_i − II_high_i)（逐 problem 配对差的中位数）。fp16 旧数据已弃用。\\n\\n## Narrative Arc\\n\\nCompound sparsity 是高效 LLM 推理的实用部署需求，但 prior work（SparK, Ada-KV, SLiM）将 compound interaction 视为均匀超可加。我们发现 severity 是 strategy × phase 交互的涌现属性：importance eviction 的 compound interaction 在 low-sparsity phase 远大于 high-sparsity phase（paired median difference 单调递增 0.32→9.94），而 random eviction 在所有 phase 保持平坦（7/8 FAIL; 唯一例外 Qwen s030 p=0.012 效应量可忽略 d=-0.04）。Cross-model replication 方向一致（Qwen magnitude ~1/4 of DeepSeek，onset threshold s≥0.20）。LLaMA 跨架构验证已完成（c3_llama, D060）：qualitative direction consistent（importance phase gradient d_z≈1.0），但 imp_vs_rand 交互弱（d_z 0.19→0.34, 仅 s030 显著），且 random 也显示非平凡 phase gradient（d_z 0.35→0.44），strategy-dependence 强度 architecture-dependent。我们通过 discrimination collapse 机制解释这一现象：head pruning → importance score 的判别力崩塌（Gini/CV 下降跨模型一致）→ importance eviction 退化为有偏伪随机。Attention entropy redistribution 作为 model-dependent secondary effect 在 DeepSeek 上观察到，但在 Qwen 上不稳健（D044）。\\n\\n**Framing 硬约束（D015）**：\\n- MUST: \\\\\\\\\\\\\\\"emergent phase-strategy interaction\\\\\\\\\\\\\\\"\\n- MUST NOT: \\\\\\\\\\\\\\\"importance metric limitation / importance is broken\\\\\\\\\\\\\\\"\\n- MUST NOT: claim \\\\\\\\\\\\\\\"importance masking produces super-additive interaction\\\\\\\\\\\\\\\" without qualifier — random masking also produces positive II. The distinguishing signal is **phase-dependent gradient** (importance: paired median difference 0.32→9.94 单调递增 vs random: 7/8 FAIL), not the existence of super-additivity itself (D023)\\n\\n## Core Claims\\n\\n| ID | Claim | Status | Key Evidence |\\n|----|-------|--------|-------------|\\n| C1 | Compound sparsity severity is strategy-dependent | confirmed | importance paired median diff 0.32→9.94 单调递增 vs random 7/8 FAIL (bf16; Qwen s030 PASS p=0.012 d=-0.04 negligible) |\\n| C2 | Severity is phase-modulated (amplified in low-sparsity phase) | confirmed | bf16 paired median difference 单调递增: 0.32→1.15→3.97→9.94; Bonferroni p<0.005 全 4 水平 (D032)。预注册：n=500 后若 QW s015 CI 仍跨零，叙事改为 'compound effect emerges above threshold sparsity (~s020)' |\\n| C3 | Phase-strategy crossover exists | confirmed | s=0.25: importance high_phase=0.032 < random=0.818, importance low_phase=7.196 > random=1.363 (bf16) |\\n| C4 | Discrimination collapse as primary mechanism; entropy redistribution model-dependent | partially_confirmed | D044: Gini/CV 下降跨模型一致; entropy collapse DeepSeek 一致但 Qwen s025 反转(+0.045) s030≈0。30/30 problems completed. |\\n| C5 | Phase-modulated compound severity generalizes across models | confirmed | DeepSeek + Qwen cross-model replication: 方向一致, Cohen's d ρ=1.0, gradient permutation p=0.043. Qwen magnitude ~1/4 of DeepSeek, onset threshold s≥0.20 (S3→C). |\\n| C5b | Phase-aware mitigation recovers compound degradation | future_work | D056: pilot 完成 gate_failed。Oracle recovery 18% < 30% gate (Wilcoxon p=0.002)，heuristic 32% 但 CI 跨零。方向正确但效应量不足，需更精细 phase boundary estimation → future work |\\n| C6 | Severity gradient is sub-exponential | confirmed | Growth rate decreasing: Δ增长因子 3.8×→4.8×→2.0×（递减） |\\n| C7 | Statistical power at n=500 confirms dose-response | running | c2_n500_deepseek + c2_qw_n500 (n=500, 8 conditions each) |\\n| C8 | Cross-architecture validation (LLaMA) | partially_confirmed | D060: within-importance phase gradient 强(d_z~1.0) ✓，但 imp_vs_rand 交互弱(d_z 0.19→0.34, 仅 s030 Bonferroni p=0.029 显著)。**关键**：random 在 LLaMA 上也显示显著 phase gradient(d_z 0.35→0.44, CI 排除零)，与 DeepSeek/Qwen random 7/8 FAIL 模式定性不同。Qualitative direction consistent, quantitative strategy×phase interaction weaker + architecture-dependent。论文禁用 \\\"confirms\\\"，改用 \\\"suggests\\\"/\\\"provides partial support\\\"。 |\\n| C9 | Differentiation from Lethe/SparK prior work | planned | Related Work §2 引用区分 + SparK gap analysis |\\n| S3→C | Onset threshold is model-dependent (DeepSeek s≥0.15, Qwen s≥0.20) | confirmed | D037/D038: Qwen s015 d=0.28 CI含0, s020+ 显著 |\\n| S7→C | Dose-response monotonicity (Spearman ρ=1.0) | confirmed | D047: 6-point dose-response, 单调递增 |\\n\\n## Anticipated Reviewer Concerns\\n\\n### RC1: Generalizability — 7B models only, single benchmark\\n- **预期质疑**: \\\\\\\"Results on two 7B models and MATH-500 only. How do we know this generalizes to larger models or other reasoning tasks?\\\\\\\"\\n- **应对**: 三层泛化证据：(1) Cross-model: DeepSeek-R1-Distill-Qwen-7B + Qwen2.5-7B-Instruct（同架构不同训练，ρ=1.0）(2) Cross-architecture: c3_llama (DeepSeek-R1-Distill-Llama-8B, LlamaForCausalLM)，qualitative direction consistent，但需加限定——LLaMA 上 random 也显示 phase gradient，strategy × phase 交互弱于 Qwen2 架构（D060）。Limitations 诚实声明：(a) 7B scale only；(b) 单 benchmark (MATH-500)；(c) LLaMA 跨架构验证 n=50 限制功效，交互效应量弱于同架构模型；(d) random phase gradient 行为 architecture-dependent。\\n- **实验支撑**: C5 (cross-model) + C8 (c3_llama cross-architecture, partially_confirmed D060)\\n\\n### RC2: Mechanism — entropy-discrimination collapse 缺乏直接测量\\n- **预期质疑**: \\\\\\\"The mechanism is conceptual. Where is the empirical evidence for entropy increase and discrimination collapse?\\\\\\\"\\n- **应对**: c4_entropy 实验已完成（DeepSeek 30/30 + Qwen 30/30）。D044 结论：Gini/CV 下降跨模型一致（discrimination collapse confirmed）；entropy redistribution 在 DeepSeek 上一致但在 Qwen 上 s025 方向反转、s030 近零（model-dependent）。论文以 discrimination collapse 为主线，entropy 作 DeepSeek 特有的强化因素。\\n- **实验支撑**: c4_entropy (DeepSeek DONE) + qwen_c4_entropy (DONE, negative for entropy universality)\\n\\n### RC3: Practical impact — 没有 throughput 数据\\n- **预期质疑**: \\\\\\\"No wall-clock or throughput measurements. Is the severity amplification reflected in actual inference speed?\\\\\\\"\\n- **应对**: 本文定位是 empirical finding paper（发现 + 机制解释），不是 method paper。Throughput 不是 claim 的一部分。Discussion 中明确 phase-gated controller 作为 future direction。\\n  - C5b pilot 已完成（D056）：oracle recovery 18%（Wilcoxon p=0.002），heuristic recovery 32%（p=0.024），但两者 95% CI 均跨零。方向正确（Wilcoxon 显著）但效应量不足（未达 30% gate），需更精细的 phase boundary estimation。论文 §6 Discussion 诚实报告 pilot 结果 + future work。\\n  - Heuristic > oracle 悖论值得提及：token position ratio 粗粒度划分可能恰好更适合 mitigation 场景，暗示 phase boundary 的最优粒度是开放问题。\\n- **实验支撑**: c5b_pilot (gate_failed, D056)\\n\\n### RC4: Statistical rigor — bootstrap 是否足够\\n- **预期质疑**: \\\\\\\"Per-problem bootstrap with 50 problems — sufficient sample size?\\\\\\\"\\n- **应对**: bf16 使用 B=10000 per-problem paired bootstrap，有效配对数 n=49 (DeepSeek) / n=46 (Qwen)。Permutation test 使用 paired median difference 作为 robust statistic（D032），Bonferroni 校正后全 4 水平 p<0.005。Cohen's d（paired d_z）作为辅助效应量（DeepSeek 0.44→0.80, Qwen 0.28→1.02）。可在 appendix 补充 per-problem 分布图（已生成 fig4_per_problem_dist.pdf）。\\n- **实验支撑**: bf16 permutation test (D032) + Cohen's d per-problem paired (rebootstrap B=10000) 已完成\\n\\n### RC5: Novelty — prior work 是否已覆盖 phase-dependent sparsity\\n- **预期质疑**: \\\"ThinKV and phase-aware methods already consider phase. What's new?\\\"\\n- **应对**: Prior work 在单轴上分析 phase（ThinKV: phase-aware eviction）或 compound（SparK: joint compression）。没有工作同时分析 compound × phase × strategy 的三维交互。Crossover 现象（同一 strategy 在不同 phase 方向反转）是全新发现。Related Work 加 Lethe 引用区分 + SparK 对比。具体区分：\\n  - **ThinKV** (arxiv 2510.01290, Oct 2025): 在 KV cache 单轴上做 phase-aware 压缩（按 CoT 阶段差异化 eviction），但不涉及 pruning × eviction 的 compound interaction。我们研究的是双轴（head pruning × KV eviction）compound interaction 如何随 phase 变化，ThinKV 的单轴 phase-aware 策略是我们分析维度的子集。\\n  - **Physics of KV Cache Compression** (arxiv 2603.01426, Mar 2026): 揭示了单轴 KV 压缩的 phase transition 和 representational rigidity，是机制层面最接近的工作。关键区分：他们刻画的是单一压缩轴上压缩率的 critical threshold（phase transition），我们刻画的是两种压缩方法的 compound interaction severity 如何被 reasoning phase 调制（phase-dependent gradient）——维度正交。\\n  - **HIES** (arxiv 2510.13832, Oct 2025): 发现 importance score collapse 并提出 entropy 补偿，为我们的 discrimination collapse 机制提供独立 supporting evidence——他们在单轴上观察到的 score collapse 正是我们在 compound setting 中发现的 Gini/CV 下降的单轴对应。\\n  - **R-KV** (arxiv 2505.24133, May 2025): 针对 reasoning task 做 KV compression 优化，属于 task-specific method。我们不是提出新方法，而是 mechanistic 分析 compound interaction 的 phase-dependent 行为，二者目标不同（optimization vs understanding）。\\n- **实验支撑**: C3 (crossover), Related Work §2 的 gap 分析\\n\\n### RC6: Novelty vs Lethe/SparK\\n- **预期质疑**: \\\"How does this differ from Lethe (AAAI 2026) which also does layer-time-adaptive KV pruning, or SparK which studies compound compression?\\\"\\n- **应对**: Lethe 和 SparK 都没有分析 phase × strategy 的交互效应。Lethe 是 method paper（提出 adaptive eviction 方法），我们是 empirical finding paper（发现 phase-dependent severity gradient）。SparK 研究 compound compression 但将 interaction 视为均匀超可加，我们发现 interaction severity 随 phase 和 strategy 变化。新近工作进一步确认我们的独特定位：\\n  - **Physics of KV Cache Compression** (arxiv 2603.01426, Mar 2026) 是最近的相关工作，研究单轴压缩的 phase transition 阈值行为。与我们的核心区别：他们的 phase transition 是压缩率维度上的 critical point，我们的 phase-dependent gradient 是 reasoning phase 维度上 compound interaction 的连续调制——两者刻画的 \\\"phase\\\" 语义不同（compression-rate phase vs reasoning phase）。\\n  - **ThinKV** (arxiv 2510.01290, Oct 2025) 和 **R-KV** (arxiv 2505.24133, May 2025) 都在 KV compression 单轴上引入 phase/reasoning awareness，但均未涉及 compound interaction。我们的贡献在于揭示 pruning × eviction 双轴交互如何被 reasoning phase 调制，这是单轴方法无法观察到的涌现现象。\\n  - **HIES** (arxiv 2510.13832, Oct 2025) 的 importance score collapse 发现为我们的 discrimination collapse 机制提供了独立佐证，但 HIES 聚焦于单轴补偿方法，未研究 collapse 在 compound setting 中的放大效应。\\n  - Related Work §2 明确区分三者定位：Lethe/SparK = method/compound method, ThinKV/R-KV = single-axis phase-aware, Physics of KV = single-axis phase transition, HIES = single-axis collapse。我们 = compound × phase × strategy 三维交互分析。\\n- **实验支撑**: 不需要额外实验，仅需 §2 引用区分\\n\\n## Paper Positioning\\n\\n**类型**: Empirical finding paper（非 method paper）\\n**核心贡献**:\\n1. 发现 compound sparsity severity 的 strategy × phase 交互\\n2. 量化 severity gradient（bf16 paired median difference 0.32→9.94, Cohen's d 0.44→0.80）和 crossover 现象\\n3. 提出 discrimination collapse 机制解释（Gini/CV 跨模型一致；entropy redistribution model-dependent）\\n4. Cross-model + cross-architecture (LLaMA) replication 验证泛化性（三模型两架构；LLaMA partially_confirmed，strategy×phase 交互强度 architecture-dependent, D060）\\n\\n**投稿目标**: EMNLP 2026 ARR, deadline 2026-05-25\\n**Rebuttal 准备**: Day 9 (2026-05-23) 预留 rebuttal letter 写作时间\\n**关键时间线**：\\n- Day 9 (2026-05-23): 预留写 rebuttal letter\\n- Day 11 (2026-05-25): EMNLP 2026 ARR 截稿\\n\", \"total_chars\": 10979, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Glob · `toolu_01QGcvGBNbBhAoag69iCYSFL`</summary>

```json
{
  "pattern": "**/*.tex",
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
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "dd2d7a9f-820c-4a44-ad2f-748c52163682",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KemX3tjbVcxshf8u7D5L9H",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 967,
      "cache_read_input_tokens": 23220,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 967
      },
      "output_tokens": 18,
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

_source line 15 · 2026-05-15T01:40:11.218Z_

<details><summary>↩ Tool result · `toolu_01QGcvGBNbBhAoag69iCYSFL`</summary>

```text
artifacts/_project/paper/appendix.tex
artifacts/_project/paper/background.tex
artifacts/_project/paper/analysis.tex
artifacts/_project/paper/conclusion.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/results.tex
artifacts/_project/paper/appendix_disc_analysis.tex
artifacts/_project/paper/methodology.tex
artifacts/_project/paper/limitations.tex
artifacts/_project/paper/main.tex
artifacts/_project/paper/appendix_results.tex
artifacts/_project/paper/appendix_moved.tex
artifacts/_project/paper/abstract.tex
artifacts/_project/paper/discussion.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "01f3e468-ebe7-4456-a9f0-9d2b108ae8ca",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/paper/appendix.tex",
      "artifacts/_project/paper/background.tex",
      "artifacts/_project/paper/analysis.tex",
      "artifacts/_project/paper/conclusion.tex",
      "artifacts/_project/paper/introduction.tex",
      "artifacts/_project/paper/related_work.tex",
      "artifacts/_project/paper/results.tex",
      "artifacts/_project/paper/appendix_disc_analysis.tex",
      "artifacts/_project/paper/methodology.tex",
      "artifacts/_project/paper/limitations.tex",
      "artifacts/_project/paper/main.tex",
      "artifacts/_project/paper/appendix_results.tex",
      "artifacts/_project/paper/appendix_moved.tex",
      "artifacts/_project/paper/abstract.tex",
      "artifacts/_project/paper/discussion.tex"
    ],
    "durationMs": 16,
    "numFiles": 15,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Glob · `toolu_018HMcnkUHLPqgrNfdUFV7N7`</summary>

```json
{
  "pattern": "**/paper*/**",
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
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "c20a856a-0ff4-474e-b86a-5564fe04c925",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KemX3tjbVcxshf8u7D5L9H",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 967,
      "cache_read_input_tokens": 23220,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 967
      },
      "output_tokens": 18,
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

_source line 17 · 2026-05-15T01:40:11.644Z_

<details><summary>↩ Tool result · `toolu_018HMcnkUHLPqgrNfdUFV7N7`</summary>

```text
artifacts/_project/paper/citation_audit_report.md
artifacts/_project/paper/acl.sty
artifacts/_project/paper/acl_natbib.bst
artifacts/_project/paper/paper_compilation_note.txt
artifacts/_project/paper/main_00fdd3.pdf
artifacts/_project/paper/main_5d82e3.pdf
artifacts/_project/paper/main_c93d3b.pdf
artifacts/_project/paper/main_9a05ce.pdf
artifacts/_project/paper/main_a1a036.pdf
artifacts/_project/paper/_pdf_images/main_a1a036_p9.png
artifacts/_project/paper/_pdf_images/main_a1a036_p10.png
artifacts/_project/paper/_pdf_images/main_a1a036_p4.png
artifacts/_project/paper/_pdf_images/main_a1a036_p5.png
artifacts/_project/paper/_pdf_images/main_a1a036_p6.png
artifacts/_project/paper/_pdf_images/main_a1a036_p7.png
artifacts/_project/paper/_pdf_images/main_a1a036_p8.png
artifacts/_project/paper/_pdf_images/main_a1a036_p1.png
artifacts/_project/paper/_pdf_images/main_a1a036_p2.png
artifacts/_project/paper/_pdf_images/main_a1a036_p3.png
artifacts/_project/paper/_pdf_images/main_a1a036_p11.png
artifacts/_project/paper/_pdf_images/main_a1a036_p12.png
artifacts/_project/paper/appendix.tex
artifacts/_project/paper/main_bdfc72.pdf
artifacts/_project/paper/figures/fig1_dose_response.pdf
artifacts/_project/paper/figures/fig3_crossover.pdf
artifacts/_project/paper/figures/fig4_bootstrap.pdf
artifacts/_project/paper/figures/fig5_crossmodel.pdf
artifacts/_project/paper/background.tex
artifacts/_project/paper/_pdf_images/main_p8.png
artifacts/_project/paper/_pdf_images/main_p9.png
artifacts/_project/paper/_pdf_images/main_p4.png
artifacts/_project/paper/_pdf_images/main_p5.png
artifacts/_project/paper/_pdf_images/main_p6.png
artifacts/_project/paper/_pdf_images/main_p7.png
artifacts/_project/paper/analysis.tex
artifacts/_project/paper/main.fls
artifacts/_project/paper/main.fdb_latexmk
artifacts/_project/paper/_pdf_images/main_p3.png
artifacts/_project/paper/_pdf_images/main_p1.png
artifacts/_project/paper/_pdf_images/main_p2.png
artifacts/_project/paper/_pdf_images/main_p10.png
artifacts/_project/paper/_pdf_images/main_p11.png
.claude/sessions/paper_agent_9539225d/CLAUDE.md
.claude/sessions/paper_agent_9539225d/AGENTS.md
artifacts/_project/paper/conclusion.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/references.bib
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/main.blg
artifacts/_project/paper/main.bbl
artifacts/_project/paper/main.aux
artifacts/_project/paper/main.out
artifacts/_project/paper/main.log
artifacts/_project/paper/main.pdf
artifacts/_project/paper/numerical_audit_report.md
artifacts/_project/paper/results.tex
artifacts/_project/paper/appendix_disc_analysis.tex
artifacts/_project/paper/methodology.tex
artifacts/_project/paper/limitations.tex
artifacts/_project/paper/main.tex
artifacts/_project/paper/appendix_results.tex
artifacts/_project/paper/appendix_moved.tex
artifacts/_project/paper/abstract.tex
artifacts/_project/paper/discussion.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "28d8048d-91c7-42d0-b54e-6969e39de3fc",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/paper/citation_audit_report.md",
      "artifacts/_project/paper/acl.sty",
      "artifacts/_project/paper/acl_natbib.bst",
      "artifacts/_project/paper/paper_compilation_note.txt",
      "artifacts/_project/paper/main_00fdd3.pdf",
      "artifacts/_project/paper/main_5d82e3.pdf",
      "artifacts/_project/paper/main_c93d3b.pdf",
      "artifacts/_project/paper/main_9a05ce.pdf",
      "artifacts/_project/paper/main_a1a036.pdf",
      "artifacts/_project/paper/_pdf_images/main_a1a036_p9.png",
      "artifacts/_project/paper/_pdf_images/main_a1a036_p10.png",
      "artifacts/_project/paper/_pdf_images/main_a1a036_p4.png",
      "artifacts/_project/paper/_pdf_images/main_a1a036_p5.png",
      "artifacts/_project/paper/_pdf_images/main_a1a036_p6.png",
      "artifacts/_project/paper/_pdf_images/main_a1a036_p7.png",
      "artifacts/_project/paper/_pdf_images/main_a1a036_p8.png",
      "artifacts/_project/paper/_pdf_images/main_a1a036_p1.png",
      "artifacts/_project/paper/_pdf_images/main_a1a036_p2.png",
      "artifacts/_project/paper/_pdf_images/main_a1a036_p3.png",
      "artifacts/_project/paper/_pdf_images/main_a1a036_p11.png",
      "artifacts/_project/paper/_pdf_images/main_a1a036_p12.png",
      "artifacts/_project/paper/appendix.tex",
      "artifacts/_project/paper/main_bdfc72.pdf",
      "artifacts/_project/paper/figures/fig1_dose_response.pdf",
      "artifacts/_project/paper/figures/fig3_crossover.pdf",
      "artifacts/_project/paper/figures/fig4_bootstrap.pdf",
      "artifacts/_project/paper/figures/fig5_crossmodel.pdf",
      "artifacts/_project/paper/background.tex",
      "artifacts/_project/paper/_pdf_images/main_p8.png",
      "artifacts/_project/paper/_pdf_images/main_p9.png",
      "artifacts/_project/paper/_pdf_images/main_p4.png",
      "artifacts/_project/paper/_pdf_images/main_p5.png",
      "artifacts/_project/paper/_pdf_images/main_p6.png",
      "artifacts/_project/paper/_pdf_images/main_p7.png",
      "artifacts/_project/paper/analysis.tex",
      "artifacts/_project/paper/main.fls",
      "artifacts/_project/paper/main.fdb_latexmk",
      "artifacts/_project/paper/_pdf_images/main_p3.png",
      "artifacts/_project/paper/_pdf_images/main_p1.png",
      "artifacts/_project/paper/_pdf_images/main_p2.png",
      "artifacts/_project/paper/_pdf_images/main_p10.png",
      "artifacts/_project/paper/_pdf_images/main_p11.png",
      ".claude/sessions/paper_agent_9539225d/CLAUDE.md",
      ".claude/sessions/paper_agent_9539225d/AGENTS.md",
      "artifacts/_project/paper/conclusion.tex",
      "artifacts/_project/paper/introduction.tex",
      "artifacts/_project/paper/references.bib",
      "artifacts/_project/paper/related_work.tex",
      "artifacts/_project/paper/main.blg",
      "artifacts/_project/paper/main.bbl",
      "artifacts/_project/paper/main.aux",
      "artifacts/_project/paper/main.out",
      "artifacts/_project/paper/main.log",
      "artifacts/_project/paper/main.pdf",
      "artifacts/_project/paper/numerical_audit_report.md",
      "artifacts/_project/paper/results.tex",
      "artifacts/_project/paper/appendix_disc_analysis.tex",
      "artifacts/_project/paper/methodology.tex",
      "artifacts/_project/paper/limitations.tex",
      "artifacts/_project/paper/main.tex",
      "artifacts/_project/paper/appendix_results.tex",
      "artifacts/_project/paper/appendix_moved.tex",
      "artifacts/_project/paper/abstract.tex",
      "artifacts/_project/paper/discussion.tex"
    ],
    "durationMs": 12,
    "numFiles": 64,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 18_

<details><summary>Logged reasoning block</summary>

```text
Now I have the paper directory at `artifacts/_project/paper/`. Let me read all the tex files to find n=50 references, old statistics, and check for C8/C5b/Qwen caveats. I'll search in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "8660b61c-c67b-4ef7-8572-d9ded05707db",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013CqjG6y997QedCGVyPABvg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6811,
      "cache_read_input_tokens": 24187,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6811
      },
      "output_tokens": 11,
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

Found the paper files at `artifacts/_project/paper/`. Now searching for all n=50 references and reading key sections.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "15e2bf2d-0bf3-482b-8ca3-9ac9267b96a5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013CqjG6y997QedCGVyPABvg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6811,
      "cache_read_input_tokens": 24187,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6811
      },
      "output_tokens": 11,
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

<details open><summary>🔧 Tool call — Grep · `toolu_01Ve9ukbwUhLbQ63G42JZRtB`</summary>

```json
{
  "pattern": "n\\s*[=≈]\\s*50|50 problems|fifty",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "-n": true,
  "-C": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "f1750ac8-08a9-4927-9c95-fbc2d956260d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013CqjG6y997QedCGVyPABvg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6811,
      "cache_read_input_tokens": 24187,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6811
      },
      "output_tokens": 11,
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

_source line 21 · 2026-05-15T01:40:20.803Z_

<details><summary>↩ Tool result · `toolu_01Ve9ukbwUhLbQ63G42JZRtB`</summary>

```text
artifacts/_project/paper/appendix_moved.tex-24-Both models share the Qwen2ForCausalLM backbone (28 layers, 28 heads, 4-group GQA) but differ in training: DeepSeek uses reasoning distillation from DeepSeek-R1, while Qwen2.5 uses standard instruction tuning without explicit reasoning delimiters. This controlled comparison isolates the effect of training methodology on the compound sparsity interaction.
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex-25-
artifacts/_project/paper/appendix_moved.tex:26:Despite lacking explicit \texttt{&lt;think>} delimiters, Qwen2.5-7B-Instruct exhibits sufficient variation in attention sparsity to permit phase segmentation via the same quantile-based method (\S\ref{sec:phase-segmentation}). Four of the 50 problems are excluded due to degenerate phase assignments, yielding $n{=}46$ valid problems for Qwen (vs.\ $n{=}49$ for DeepSeek).
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex-27-
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex-28-\paragraph{Per-phase effective sample size.}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex-8-\paragraph{Dataset.}
artifacts/_project/paper/methodology.tex-9-\label{sec:dataset}
artifacts/_project/paper/methodology.tex:10:We use 50 problems stratified from MATH-500~\cite{math500-neurips2021}, sampling uniformly across categories with a fixed seed. Each problem is decoded greedily (\texttt{max\_new\_tokens}$=$2048).
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex-11-
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex-12-\paragraph{Sparsity configuration.}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex-32-\centering
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex-33-\small
artifacts/_project/paper/results.tex:34:\caption{Interaction index (II) by eviction strategy, reasoning phase, and sparsity level. II values are problem-level medians across 50 problems. $\Delta = \widetilde{\mathrm{II}}_{\textit{low}} - \widetilde{\mathrm{II}}_{\textit{high}}$. $G = \widetilde{\mathrm{II}}_{\textit{low}} / \widetilde{\mathrm{II}}_{\textit{high}}$.}
artifacts/_project/paper/results.tex-35-\label{tab:main-results}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex-36-\begin{tabular}{@{}llccccr@{}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "1a3d2f1f-889e-4aa9-abc3-910f9b99cb44",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "artifacts/_project/paper/appendix_moved.tex-24-Both models share the Qwen2ForCausalLM backbone (28 layers, 28 heads, 4-group GQA) but differ in training: DeepSeek uses reasoning distillation from DeepSeek-R1, while Qwen2.5 uses standard instruction tuning without explicit reasoning delimiters. This controlled comparison isolates the effect of training methodology on the compound sparsity interaction.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex-25-\nartifacts/_project/paper/appendix_moved.tex:26:Despite lacking explicit \\texttt{&lt;think>} delimiters, Qwen2.5-7B-Instruct exhibits sufficient variation in attention sparsity to permit phase segmentation via the same quantile-based method (\\S\\ref{sec:phase-segmentation}). Four of the 50 problems are excluded due to degenerate phase assignments, yielding $n{=}46$ valid problems for Qwen (vs.\\ $n{=}49$ for DeepSeek).\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex-27-\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex-28-\\paragraph{Per-phase effective sample size.}\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex-8-\\paragraph{Dataset.}\nartifacts/_project/paper/methodology.tex-9-\\label{sec:dataset}\nartifacts/_project/paper/methodology.tex:10:We use 50 problems stratified from MATH-500~\\cite{math500-neurips2021}, sampling uniformly across categories with a fixed seed. Each problem is decoded greedily (\\texttt{max\\_new\\_tokens}$=$2048).\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex-11-\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex-12-\\paragraph{Sparsity configuration.}\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex-32-\\centering\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex-33-\\small\nartifacts/_project/paper/results.tex:34:\\caption{Interaction index (II) by eviction strategy, reasoning phase, and sparsity level. II values are problem-level medians across 50 problems. $\\Delta = \\widetilde{\\mathrm{II}}_{\\textit{low}} - \\widetilde{\\mathrm{II}}_{\\textit{high}}$. $G = \\widetilde{\\mathrm{II}}_{\\textit{low}} / \\widetilde{\\mathrm{II}}_{\\textit{high}}$.}\nartifacts/_project/paper/results.tex-35-\\label{tab:main-results}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex-36-\\begin{tabular}{@{}llccccr@{}}",
    "numLines": 17
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Grep · `toolu_014tbJXKopLJz5muaHPJs7LX`</summary>

```json
{
  "pattern": "median|CI|d_z|cohen|bootstrap|0\\.\\d{2,3}|[1-9]\\.\\d{2,3}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "-n": true,
  "-i": true,
  "head_limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "11526166-2d98-42d1-b71d-2c76f438be50",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013CqjG6y997QedCGVyPABvg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6811,
      "cache_read_input_tokens": 24187,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6811
      },
      "output_tokens": 11,
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

_source line 23 · 2026-05-15T01:40:23.409Z_

<details><summary>↩ Tool result · `toolu_014tbJXKopLJz5muaHPJs7LX`</summary>

```text
&lt;persisted-output>
Output too large (31.3KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/92d5a500-97ec-4718-a2d5-83296bc1ca35/tool-results/toolu_014tbJXKopLJz5muaHPJs7LX.txt

Preview (first 2KB):
artifacts/_project/paper/analysis.tex:4:[Omitted long matching line]
artifacts/_project/paper/analysis.tex:6:[Omitted long matching line]
artifacts/_project/paper/related_work.tex:6:\cite{spark-aaai2026} report super-additive degradation when combining channel pruning with token eviction; \cite{slim-icml2025} formalize compound error for quantization and sparsity.
artifacts/_project/paper/related_work.tex:7:\cite{unicomp-2026} evaluate compound compression across 40+ benchmarks, revealing that reasoning capabilities degrade disproportionately.
artifacts/_project/paper/related_work.tex:8:\cite{phase-transition-compression-2026} characterize independent phase transition points per compression dimension, implying the joint safe region is the intersection of per-dimension safe zones.
artifacts/_project/paper/related_work.tex:9:GRASPrune~\cite{graspune-acl2026} learns global budget-constrained gates for joint pruning but treats decisions as static across generation.
artifacts/_project/paper/related_work.tex:10:These works establish compound interaction but share an implicit assumption: interaction magnitude is constant across the generation process.
artifacts/_project/paper/related_work.tex:14:Ada-KV~\cite{adakv-neurips2025} introduces per-head adaptive budgets; SnapKV~\cite{snapkv-neurips2024} compresses from a fixed observation window; \cite{defensivekv-iclr2026} show worst-case loss $2.3$--$4.3{\times}$ higher than expected under standard aggregation.
artifacts/_project/paper/related_work.tex:15:\cite{nacl-acl2024} combine proxy-token and random eviction to counter attention bias.
artifacts/_project/paper/related_work.tex:16:RetentiveKV~\cite{retentivekv-2026} identifies deferred importance, and \cite{greedy-bias-kvcache-2026} show that single importance metrics exhibit systematic greedy bias.
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
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "af5a6920-73a0-4850-8848-bd7f2fc3ad6a",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "artifacts/_project/paper/analysis.tex:4:[Omitted long matching line]\nartifacts/_project/paper/analysis.tex:6:[Omitted long matching line]\nartifacts/_project/paper/related_work.tex:6:\\cite{spark-aaai2026} report super-additive degradation when combining channel pruning with token eviction; \\cite{slim-icml2025} formalize compound error for quantization and sparsity.\nartifacts/_project/paper/related_work.tex:7:\\cite{unicomp-2026} evaluate compound compression across 40+ benchmarks, revealing that reasoning capabilities degrade disproportionately.\nartifacts/_project/paper/related_work.tex:8:\\cite{phase-transition-compression-2026} characterize independent phase transition points per compression dimension, implying the joint safe region is the intersection of per-dimension safe zones.\nartifacts/_project/paper/related_work.tex:9:GRASPrune~\\cite{graspune-acl2026} learns global budget-constrained gates for joint pruning but treats decisions as static across generation.\nartifacts/_project/paper/related_work.tex:10:These works establish compound interaction but share an implicit assumption: interaction magnitude is constant across the generation process.\nartifacts/_project/paper/related_work.tex:14:Ada-KV~\\cite{adakv-neurips2025} introduces per-head adaptive budgets; SnapKV~\\cite{snapkv-neurips2024} compresses from a fixed observation window; \\cite{defensivekv-iclr2026} show worst-case loss $2.3$--$4.3{\\times}$ higher than expected under standard aggregation.\nartifacts/_project/paper/related_work.tex:15:\\cite{nacl-acl2024} combine proxy-token and random eviction to counter attention bias.\nartifacts/_project/paper/related_work.tex:16:RetentiveKV~\\cite{retentivekv-2026} identifies deferred importance, and \\cite{greedy-bias-kvcache-2026} show that single importance metrics exhibit systematic greedy bias.\nartifacts/_project/paper/related_work.tex:17:\\cite{hies-2025} independently show that importance-based head discrimination collapses under heavy pruning, further questioning single-metric reliability.\nartifacts/_project/paper/related_work.tex:18:Lethe~\\cite{lethe-aaai2026} introduces temporal adaptivity with layer-wise multi-round pruning, and SparK~\\cite{spark-aaai2026} extends eviction to the channel dimension with recoverable sparsity.\nartifacts/_project/paper/related_work.tex:22:ThinKV~\\cite{thinkv-iclr2026} applies different KV strategies per phase but without compound interaction.\nartifacts/_project/paper/related_work.tex:23:\\cite{decision-repr-transition-2026} find pruning sensitivity depends on ``silent'' vs.\\ ``decisive'' representation phases.\nartifacts/_project/paper/related_work.tex:24:\\cite{doing-more-with-less-2026} show pruning combined with test-time scaling can exceed unpruned baselines; \\cite{sparse-frontier-2025} find no universally optimal sparse attention strategy across generation stages.\nartifacts/_project/paper/related_work.tex:25:\\cite{physics-kvcache-2026} identify a sharp phase transition in single-axis KV cache compression at high sparsity, characterizing the single-dimension failure mode that our compound analysis extends across multiple axes.\nartifacts/_project/paper/related_work.tex:26:R-KV~\\cite{rkv-neurips2025} exploits reasoning-specific redundancy for aggressive cache compression, targeting per-axis optimization rather than characterizing compound degradation.\nartifacts/_project/paper/conclusion.tex:4:[Omitted long matching line]\nartifacts/_project/paper/discussion.tex:5:[Omitted long matching line]\nartifacts/_project/paper/discussion.tex:8:[Omitted long matching line]\nartifacts/_project/paper/discussion.tex:10:[Omitted long matching line]\nartifacts/_project/paper/discussion.tex:15:[Omitted long matching line]\nartifacts/_project/paper/appendix_moved.tex:6:% Main body §6 (analysis.tex) contains a condensed summary referencing these tables.\nartifacts/_project/paper/appendix_moved.tex:11:[Omitted long matching line]\nartifacts/_project/paper/appendix_moved.tex:16:\\caption{Strategy-dependent crossover at $s{=}0.25$. Grouped bar chart of median II by eviction strategy and reasoning phase. Importance-based eviction outperforms random in the high-sparsity phase but produces $5.3{\\times}$ higher II in the low-sparsity phase, reversing the strategy ranking.}\nartifacts/_project/paper/appendix_moved.tex:24:Both models share the Qwen2ForCausalLM backbone (28 layers, 28 heads, 4-group GQA) but differ in training: DeepSeek uses reasoning distillation from DeepSeek-R1, while Qwen2.5 uses standard instruction tuning without explicit reasoning delimiters. This controlled comparison isolates the effect of training methodology on the compound sparsity interaction.\nartifacts/_project/paper/appendix_moved.tex:26:Despite lacking explicit \\texttt{&lt;think>} delimiters, Qwen2.5-7B-Instruct exhibits sufficient variation in attention sparsity to permit phase segmentation via the same quantile-based method (\\S\\ref{sec:phase-segmentation}). Four of the 50 problems are excluded due to degenerate phase assignments, yielding $n{=}46$ valid problems for Qwen (vs.\\ $n{=}49$ for DeepSeek).\nartifacts/_project/paper/appendix_moved.tex:30:Table~\\ref{tab:qwen-effective-n} reports the per-phase effective sample size for Qwen2.5-7B-Instruct, defined as the number of problems with $|\\mathrm{II}| > 0.001$ in each phase. The mid-phase null rate (\\placeholder{NULL\\_PCT}\\%) reflects problems where compound interaction is absent in intermediate phases; this does not affect the low--high contrast ($\\Delta$) used in the primary analysis.\nartifacts/_project/paper/appendix_moved.tex:39:Phase & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\\\\nartifacts/_project/paper/appendix_moved.tex:48:Table~\\ref{tab:cross-model} reports the cross-model comparison. Qwen reproduces the monotonic severity gradient at ${\\sim}1/5$ of DeepSeek's magnitude. Figure~\\ref{fig:cross-model} visualizes this comparison. % exp_id: cross_model_analysis.json; cohens_d_bf16_qwen.json\nartifacts/_project/paper/appendix_moved.tex:53:\\caption{Cross-model comparison of median compound severity difference ($\\Delta$) under importance-based eviction.}\nartifacts/_project/paper/appendix_moved.tex:57:Model & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\\\\nartifacts/_project/paper/appendix_moved.tex:59:DeepSeek-R1-Distill-Qwen-7B & 0.39 & 1.48 & 7.16 & 14.59 \\\\ % exp_id: bf16_importance_s015..s030\nartifacts/_project/paper/appendix_moved.tex:60:Qwen2.5-7B-Instruct         & 0.04 & 0.23 & 1.27 & 2.94 \\\\ % exp_id: bf16_qw_imp_s015..s030\nartifacts/_project/paper/appendix_moved.tex:68:\\caption{Cross-model comparison of the median severity difference under importance-based eviction. Both DeepSeek (solid) and Qwen (dashed) exhibit monotonically increasing $\\Delta$ with sparsity; Qwen's magnitude is approximately one-fifth of DeepSeek's.} % exp_id: bf16_importance_s015..s030, bf16_qw_imp_s015..s030\nartifacts/_project/paper/appendix_moved.tex:73:The per-problem concordance across models is not significant (median $\\rho = \\placeholder{}$, $p = \\placeholder{}$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking. % exp_id: cross_model_analysis.json (spearman_rho=1.0, gradient_permutation_p=0.043, per_problem_concordance_p=0.926, mean_rho=-0.107)\nartifacts/_project/paper/appendix_moved.tex:76:As a control, random eviction on Qwen yields no systematic phase gradient at three of four sparsity levels (3/4 FAIL), mirroring DeepSeek's 4/4 FAIL pattern. At $s{=}0.30$, Qwen random produces a borderline PASS (permutation $p = 0.012$) but with negligible median difference ($\\widetilde{\\Delta} = \\placeholder{}$, CI spans zero), indicating no meaningful phase modulation. % exp_id: bf16_qw_rand_s015..s030; source: experiment_summary_table.json\nartifacts/_project/paper/appendix_moved.tex:82:[Omitted long matching line]\nartifacts/_project/paper/appendix_moved.tex:84:Per-problem distributions of the paired severity difference $\\Delta_i = \\mathrm{II}_{\\textit{low},i} - \\mathrm{II}_{\\textit{high},i}$ under importance-based eviction are right-skewed at all sparsity levels, with mean/median ratios ranging from $1.2{\\times}$ ($s{=}0.15$) to $1.6{\\times}$ ($s{=}0.30$) for DeepSeek and $1.1{\\times}$ to $1.4{\\times}$ for Qwen.\nartifacts/_project/paper/appendix_moved.tex:86:The permutation null distributions are approximately symmetric around zero at all sparsity levels. At $s{=}0.15$, the observed statistic falls at the $99.92$th percentile of the null ($p_{\\text{Bonf}} = 0.0032$); at $s \\geq 0.20$, no permutation exceeds the observed statistic.\nartifacts/_project/paper/appendix_moved.tex:88:[Omitted long matching line]\nartifacts/_project/paper/appendix_moved.tex:97:$s$ & Observed $\\widetilde{\\Delta}$ & 95\\% CI & $p_{\\text{Bonf}}$ \\\\\nartifacts/_project/paper/appendix_moved.tex:99:0.15 & 0.37 & $[0.19,\\; 0.62]$ & 0.0032 \\\\ % exp_id: deepseek_bf16_permtest_s015\nartifacts/_project/paper/appendix_moved.tex:100:0.20 & 0.97 & $[0.69,\\; 1.49]$ & ${<}\\,0.001$ \\\\ % exp_id: deepseek_bf16_permtest_s020\nartifacts/_project/paper/appendix_moved.tex:101:0.25 & 3.34 & $[1.66,\\; 6.64]$ & ${<}\\,0.001$ \\\\ % exp_id: deepseek_bf16_permtest_s025\nartifacts/_project/paper/appendix_moved.tex:102:0.30 & 9.85 & $[6.70,\\; 16.29]$ & ${<}\\,0.001$ \\\\ % exp_id: deepseek_bf16_permtest_s030\nartifacts/_project/paper/appendix_moved.tex:109:\\includegraphics[width=\\columnwidth]{fig4_bootstrap.pdf}\nartifacts/_project/paper/appendix_moved.tex:110:\\caption{Forest plot of permutation test results. Horizontal bars show 95\\% permutation CIs; diamonds mark observed median differences $\\widetilde{\\Delta}$. All CIs lie entirely above zero, confirming significant strategy-dependent severity at every sparsity level.}\nartifacts/_project/paper/appendix_moved.tex:121:[Omitted long matching line]\nartifacts/_project/paper/appendix_moved.tex:132:DeepSeek & $0.15$ & $-0.030$ & $-0.56$ \\\\\nartifacts/_project/paper/appendix_moved.tex:133:DeepSeek & $0.20$ & $-0.040$ & $-0.77$ \\\\\nartifacts/_project/paper/appendix_moved.tex:134:DeepSeek & $0.25$ & $-0.065$ & $-1.29$ \\\\\nartifacts/_project/paper/appendix_moved.tex:135:DeepSeek & $0.30$ & $-0.081$ & $-1.66$ \\\\\nartifacts/_project/paper/appendix_moved.tex:137:Qwen & $0.15$ & $-0.010$ & $-0.05$ \\\\\nartifacts/_project/paper/appendix_moved.tex:138:Qwen & $0.20$ & $-0.012$ & $-0.21$ \\\\\nartifacts/_project/paper/appendix_moved.tex:139:Qwen & $0.25$ & $-0.010$ & $-1.49$ \\\\\nartifacts/_project/paper/appendix_moved.tex:140:Qwen & $0.30$ & $-0.020$ & $-1.14$ \\\\\nartifacts/_project/paper/appendix_moved.tex:145:[Omitted long matching line]\nartifacts/_project/paper/appendix_moved.tex:157:For DeepSeek under importance-based eviction, the entropy delta is consistently negative across all four sparsity levels ($\\Delta\\mathcal{H} \\in [-0.047, -0.040]$; Table~\\ref{tab:entropy-deltas}), indicating that importance-based pruning systematically selects heads whose removal concentrates attention in the surviving heads, reinforcing discrimination collapse. % exp_id: c4_entropy_deepseek\nartifacts/_project/paper/appendix_moved.tex:159:[Omitted long matching line]\nartifacts/_project/paper/appendix_moved.tex:165:\\caption{Attention entropy deltas ($\\Delta\\mathcal{H}$) under importance-based eviction. DeepSeek shows consistent entropy compression; Qwen partially replicates with a reversal at $s{=}0.25$.}\nartifacts/_project/paper/appendix_moved.tex:172:DeepSeek & $0.15$ & $-0.040$ \\\\\nartifacts/_project/paper/appendix_moved.tex:173:DeepSeek & $0.20$ & $-0.047$ \\\\\nartifacts/_project/paper/appendix_moved.tex:174:DeepSeek & $0.25$ & $-0.045$ \\\\\nartifacts/_project/paper/appendix_moved.tex:175:DeepSeek & $0.30$ & $-0.044$ \\\\\nartifacts/_project/paper/appendix_moved.tex:177:Qwen & $0.15$ & $-0.073$ \\\\\nartifacts/_project/paper/appendix_moved.tex:178:Qwen & $0.20$ & $-0.076$ \\\\\nartifacts/_project/paper/appendix_moved.tex:179:Qwen & $0.25$ & $+0.045$ \\\\\nartifacts/_project/paper/appendix_moved.tex:180:Qwen & $0.30$ & $-0.007$ \\\\\nartifacts/_project/paper/appendix_results.tex:7:The per-problem concordance across models is not significant (median $\\rho = \\placeholder{}$, $p = \\placeholder{}$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking. % exp_id: cross_model_analysis.json (spearman_rho=1.0, gradient_permutation_p=0.043, per_problem_concordance_p=0.926, mean_rho=-0.107)\nartifacts/_project/paper/appendix_results.tex:10:As a control, random eviction on Qwen yields no systematic phase gradient at three of four sparsity levels (3/4 FAIL), mirroring DeepSeek's 4/4 FAIL pattern. At $s{=}0.30$, Qwen random produces a borderline PASS (permutation $p = 0.012$) but with negligible median difference ($\\widetilde{\\Delta} = \\placeholder{}$, CI spans zero), indicating no meaningful phase modulation. % exp_id: bf16_qw_rand_s015..s030; source: experiment_summary_table.json\nartifacts/_project/paper/limitations.tex:2:[Omitted long matching line]\nartifacts/_project/paper/limitations.tex:8:The discrimination collapse mechanism is supported by correlational evidence (consistent Gini/CV reduction across all conditions); causal validation through controlled entropy manipulation is needed. The entropy redistribution component replicates on only 2/4 Qwen conditions, suggesting model-specific factors.\nartifacts/_project/paper/limitations.tex:11:Our experiments span $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$. More extreme sparsity ($s > 0.50$) may exhibit qualitatively different interaction dynamics. We do not report inference throughput or latency measurements, which are necessary for a complete deployment analysis but orthogonal to our severity characterization. Extended limitations in Appendix~\\ref{app:limitations}.\nartifacts/_project/paper/methodology.tex:6:[Omitted long matching line]\nartifacts/_project/paper/methodology.tex:10:We use 50 problems stratified from MATH-500~\\cite{math500-neurips2021}, sampling uniformly across categories with a fixed seed. Each problem is decoded greedily (\\texttt{max\\_new\\_tokens}$=$2048).\nartifacts/_project/paper/methodology.tex:14:We apply symmetric compound sparsity at $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$, computing perplexity under four conditions: dense, attention-only, KV-only, and compound. We compare \\emph{importance-based} eviction (position-normalized cumulative attention score, Eq.~\\ref{eq:kv-importance}; BOS always retained) and \\emph{random} eviction (uniform). Heads are pruned per layer by Frobenius norm; under random eviction, both heads and positions are selected uniformly.\nartifacts/_project/paper/methodology.tex:18:Each sequence is segmented into three phases using the quantile-based method (\\S\\ref{sec:phase-segmentation}), with $\\texttt{min\\_phase\\_length}{=}10$. We compute segment-level perplexity, II (Eq.~\\ref{eq:ii}), and $G$ (Eq.~\\ref{eq:gradient}), reporting medians due to heavy right-skew (mean/median ratios up to 43:1).\nartifacts/_project/paper/methodology.tex:22:All reported confidence intervals and significance tests use nonparametric bootstrap ($B{=}10{,}000$)~\\cite{efron-1993}; initial profiling uses $B{=}1{,}000$ for computational efficiency, with all reported statistics recomputed at $B{=}10{,}000$. Paired bootstrap controls for problem-level variance. All tests yield $p_{\\text{Bonf}} < 0.005$ at every sparsity level.\\footnote{Experiments on 4$\\times$ NVIDIA RTX PRO 6000 Blackwell 96\\,GB GPUs.}\nartifacts/_project/paper/background.tex:12:[Omitted long matching line]\nartifacts/_project/paper/background.tex:21:$\\mathrm{II} > 0$ indicates super-additive degradation; $\\mathrm{II} = 0$ indicates additive independence. We adopt the additive null because the two axes operate on disjoint dimensions; qualitative conclusions hold under the multiplicative null (Appendix~\\ref{app:multiplicative-null}). Because the II distribution is heavily right-skewed, we report medians throughout.\nartifacts/_project/paper/background.tex:29:where $\\widetilde{\\mathrm{II}}_{\\,\\textit{low/high}}$ are median II in the low/high-sparsity phases. $G \\gg 1$ indicates phase-concentrated severity.\nartifacts/_project/paper/background.tex:33:Each generated sequence is partitioned into three phases (low-, mid-, high-sparsity) by tercile boundaries of per-position attention sparsity, following ThinKV~\\cite{thinkv-iclr2026}. Low-sparsity phases correspond to broadly distributed attention (exploratory reasoning); high-sparsity phases to concentrated attention (structured computation). Details in Appendix~\\ref{app:formulation-details}.\nartifacts/_project/paper/abstract.tex:2:Compound sparsity---simultaneously pruning attention heads and evicting KV cache entries---is essential for efficient LLM inference but produces super-additive quality degradation whose structure is poorly understood.\nartifacts/_project/paper/abstract.tex:6:We evaluate compound sparsity on three models---DeepSeek-R1-Distill-Qwen-7B, Qwen2.5-7B-Instruct (both Qwen2ForCausalLM), and DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM)---spanning two architectures, using 50 MATH-500 problems, measuring the Interaction Index---a super-additivity metric---across quantile-segmented reasoning phases at sparsity levels $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$.\nartifacts/_project/paper/abstract.tex:7:Under importance-based KV cache eviction, the median Interaction Index difference between low-sparsity and high-sparsity reasoning phases increases monotonically from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired Cohen's $d_z$ growing from $0.44$ (small) to $0.80$ (large); Bonferroni-corrected permutation tests yield $p < 0.005$ at all four sparsity levels.\nartifacts/_project/paper/abstract.tex:8:Random eviction produces no significant phase modulation in 7/8 conditions; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) shows negligible median difference ($\\widetilde{\\Delta} = \\placeholder{}$), confirming that the severity gradient is strategy-specific, not an inherent property of compound sparsity.\nartifacts/_project/paper/abstract.tex:9:At $s{=}0.25$, a crossover emerges: importance-based eviction outperforms random in high-sparsity phases ($\\widetilde{\\mathrm{II}} = 0.032$ vs.\\ $0.818$) yet underperforms in low-sparsity phases ($\\widetilde{\\mathrm{II}} = 7.196$ vs.\\ $1.363$)---a qualitative reversal in strategy ranking.\nartifacts/_project/paper/abstract.tex:10:[Omitted long matching line]\nartifacts/_project/paper/appendix.tex:5:Heads are ranked by Frobenius norm importance $w_j^{(\\ell)} = \\|\\mathbf{A}_j^{(\\ell)}\\|_F$ \\cite{voita-acl2019, michel-neurips2019}; a binary mask $m_j^{(\\ell)} \\in \\{0,1\\}$ retains the top-$(1{-}s)\\cdot H$ heads:\nartifacts/_project/paper/appendix.tex:22:where the denominator compensates for causal bias---earlier positions are attended to by more queries \\cite{thinkv-iclr2026, defensivekv-iclr2026}. Under random eviction, positions (excluding BOS) are evicted uniformly at random.\nartifacts/_project/paper/appendix.tex:25:Applying both mechanisms simultaneously yields compound sparsity. The two axes interact: head pruning redistributes attention mass, altering the importance ranking for KV eviction. Prior work \\cite{spark-aaai2026} reports super-additive joint effects but treats interaction magnitude as a fixed property of $s$.\nartifacts/_project/paper/appendix.tex:30:    \\sigma_i^{(h)} = \\frac{1}{T} \\sum_{j=1}^{T} \\mathbf{1}\\!\\left[a_{ij}^{(h)} < 0.01 \\cdot \\max_k a_{ik}^{(h)}\\right].\nartifacts/_project/paper/appendix.tex:33:The per-position sparsity $\\sigma_i = \\frac{1}{H}\\sum_h \\sigma_i^{(h)}$ averages across all heads. Tokens are partitioned into high-, mid-, and low-sparsity phases by the tercile boundaries of $\\{\\sigma_i\\}$; segments shorter than 10 tokens are merged into adjacent phases.\nartifacts/_project/paper/appendix.tex:38:[Omitted long matching line]\nartifacts/_project/paper/appendix.tex:40:% Bootstrap and permutation details moved to main text \\S\\ref{sec:stat-validation}\nartifacts/_project/paper/appendix_disc_analysis.tex:4:[Omitted long matching line]\nartifacts/_project/paper/appendix_disc_analysis.tex:11:The compound interaction is not uniformly fragile---it is selectively fragile in a phase-dependent manner ($\\widetilde{\\mathrm{II}}_{\\text{high}} < 0.06$ at $s \\leq 0.30$; at $s = 0.35$, high-phase II rises to $0.105$ in a supplementary experiment, indicating onset of compound interaction even in high-sparsity phases at extreme pruning rates). % exp_id: bf16_importance_s015..s030, bf16_ds_imp_s035; high-phase medians: 0.006, 0.015, 0.032, 0.053; s035 II_high=0.1051\nartifacts/_project/paper/appendix_disc_analysis.tex:14:Random eviction fails 7/8 paired permutation tests across both models; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) exhibits negligible effect size ($\\widetilde{\\Delta} = \\placeholder{}$). The absence of a phase gradient under random masking isolates the amplification as strategy-specific. % exp_id: bf16_ds_rand_s015..s030, bf16_qw_rand_s015..s030\nartifacts/_project/paper/appendix_disc_analysis.tex:28:% REBUTTAL: 7B is the most-deployed scale for on-device and cost-constrained serving—exactly where compound sparsity is needed. The mechanism (entropy-discrimination collapse) is scale-agnostic in principle. Scaling experiments are future work.\nartifacts/_project/paper/appendix_disc_analysis.tex:33:[Omitted long matching line]\nartifacts/_project/paper/appendix_disc_analysis.tex:41:% REVIEWER-ATTACK: \"Only MATH-500. How do we know this isn't a math-specific artifact?\"\nartifacts/_project/paper/appendix_disc_analysis.tex:42:% REBUTTAL: The mechanism (entropy-discrimination collapse under head pruning) depends on attention distribution properties, not math-specific features. MATH-500 is a standard benchmark with diverse difficulty. However, different reasoning tasks may induce different phase structures—we state this limitation explicitly rather than overclaiming.\nartifacts/_project/paper/appendix_disc_analysis.tex:45:Bootstrap confidence intervals use $B{=}10{,}000$ resamples (recomputed from initial $B{=}1{,}000$ profiling runs). The paired permutation test yields $n{=}49$ paired problems for DeepSeek (1 excluded) and $n{=}46$ for Qwen (4 excluded). % exp_id: cohens_d_bf16.json, cohens_d_bf16_qwen.json\nartifacts/_project/paper/appendix_disc_analysis.tex:46:The severity difference distribution is right-skewed (mean/median ratio ${\\sim}1.6{:}1$ at $s{=}0.30$), motivating our use of medians and nonparametric tests rather than parametric alternatives. % exp_id: bf16_importance_s030; mean_diff=22.94, median_diff=14.59 (segment-level). Per-problem paired: median_diff=9.9436 at s030\nartifacts/_project/paper/appendix_disc_analysis.tex:47:[Omitted long matching line]\nartifacts/_project/paper/appendix_disc_analysis.tex:49:A notable exception among the random baselines is the Qwen random condition at $s{=}0.30$, which yields a statistically significant result ($p{=}0.012$) despite negligible effect size ($\\widetilde{\\Delta} = \\placeholder{}$, bootstrap CI spanning zero). % exp_id: qw_rand_s030; B=10000, p=0.012, d=-0.035, negligible\nartifacts/_project/paper/appendix_disc_analysis.tex:50:This case illustrates that dichotomous significance testing can flag effects of no practical magnitude---reinforcing the importance of reporting effect sizes and confidence intervals alongside $p$-values.\nartifacts/_project/paper/appendix_disc_analysis.tex:53:Our experiments span $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$, a moderate range representative of practical deployment targets.\nartifacts/_project/paper/appendix_disc_analysis.tex:54:More extreme sparsity ($s > 0.50$) may exhibit qualitatively different interaction dynamics---the sub-exponential growth pattern suggests the severity gradient may plateau, but this remains unverified.\nartifacts/_project/paper/appendix_disc_analysis.tex:56:% REVIEWER-ATTACK: \"Why not test higher sparsity? 0.30 is conservative.\"\nartifacts/_project/paper/appendix_disc_analysis.tex:57:% REBUTTAL: Our focus is on the practically relevant regime where models retain usable quality. At s>0.30 both strategies degrade severely, making II measurement less informative. The sub-exponential growth (C6, $\\Delta$ growth rate $3.8{\\times} \\to 4.8{\\times} \\to 2.0{\\times}$) suggests saturation at higher sparsity, but confirming this is future work.\nartifacts/_project/paper/appendix_disc_analysis.tex:62:% REBUTTAL: This is an empirical finding paper, not a method/system paper. The contribution is characterizing *what happens* (phase-modulated severity) and *why* (entropy-discrimination collapse), not building a system to fix it. Phase-gated controllers are explicitly scoped as future work. The finding is actionable regardless: any compound sparsity deployment should be aware of phase-dependent severity.\nartifacts/_project/paper/introduction.tex:4:Long-context language models place acute pressure on the key--value (KV) cache, which grows linearly with sequence length \\cite{kwon-sosp2023, pope-mlsys2023}.\nartifacts/_project/paper/introduction.tex:5:[Omitted long matching line]\nartifacts/_project/paper/introduction.tex:7:Prior work treats compound interaction magnitude as roughly constant across generation \\cite{spark-aaai2026, unicomp-2026}, despite evidence that pruning sensitivity depends on representational phase \\cite{decision-repr-transition-2026} and that no single sparse attention strategy dominates across generation stages \\cite{sparse-frontier-2025}.\nartifacts/_project/paper/introduction.tex:8:This assumption is problematic for reasoning models, whose generations alternate between broadly distributed attention (exploratory reasoning) and sharply concentrated attention (structured computation) \\cite{thinkv-iclr2026}.\nartifacts/_project/paper/introduction.tex:9:Phase-aware methods like ThinKV \\cite{thinkv-iclr2026} apply different KV strategies per phase but without considering compound interaction, while importance-based eviction itself faces challenges from greedy bias \\cite{greedy-bias-kvcache-2026}, deferred importance \\cite{retentivekv-2026}, and temporal dynamics in long generations \\cite{lethe-aaai2026}. These methods each optimize a single pruning axis; we characterize the interaction when multiple mechanisms are composed.\nartifacts/_project/paper/introduction.tex:14:On DeepSeek-R1-Distill-Qwen-7B, the median phase difference rises from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$ ($d_z$: $0.44 \\to 0.80$; Bonferroni-corrected $p < 0.005$ at all levels).\nartifacts/_project/paper/introduction.tex:15:The pattern replicates at $s \\geq 0.20$ on Qwen2.5-7B-Instruct ($d_z \\geq 0.55$) and partially extends to a distinct architecture (DeepSeek-R1-Distill-Llama-8B, LlamaForCausalLM) with a qualitatively consistent but substantially weaker trend at $\\sim$1/40 the magnitude.\nartifacts/_project/paper/introduction.tex:19:Random eviction is immune because its decisions are independent of attention patterns.\nartifacts/_project/paper/results.tex:8:[Omitted long matching line]\nartifacts/_project/paper/results.tex:13:\\caption{Median compound severity difference ($\\Delta = \\widetilde{\\mathrm{II}}_{\\textit{low}} - \\widetilde{\\mathrm{II}}_{\\textit{high}}$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}50$ MATH-500 problems).}\nartifacts/_project/paper/results.tex:17:Strategy & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\\\\nartifacts/_project/paper/results.tex:19:Importance & 0.39 & 1.48 & 7.16 & 14.59 \\\\ % exp_id: bf16_importance_s015..s030; source: experiment_summary_table.json median_diff\nartifacts/_project/paper/results.tex:20:Random     & 0.01 & $-$0.02 & 0.54 & 1.54 \\\\ % exp_id: bf16_ds_rand_s015..s030; source: experiment_summary_table.json median_diff\nartifacts/_project/paper/results.tex:29:[Omitted long matching line]\nartifacts/_project/paper/results.tex:34:\\caption{Interaction index (II) by eviction strategy, reasoning phase, and sparsity level. II values are problem-level medians across 50 problems. $\\Delta = \\widetilde{\\mathrm{II}}_{\\textit{low}} - \\widetilde{\\mathrm{II}}_{\\textit{high}}$. $G = \\widetilde{\\mathrm{II}}_{\\textit{low}} / \\widetilde{\\mathrm{II}}_{\\textit{high}}$.}\nartifacts/_project/paper/results.tex:40:0.15 & Importance & 0.006 & 0.081 & 0.398 & 0.39 & $\\mathbf{69}$ \\\\\nartifacts/_project/paper/results.tex:41:0.15 & Random     & 0.093 & 0.097 & 0.103 & 0.01 & 1.1 \\\\\nartifacts/_project/paper/results.tex:43:0.20 & Importance & 0.015 & 0.203 & 1.496 & 1.48 & $\\mathbf{103}$ \\\\\nartifacts/_project/paper/results.tex:44:0.20 & Random     & 0.292 & 0.350 & 0.276 & $-$0.02 & 0.9 \\\\\nartifacts/_project/paper/results.tex:46:0.25 & Importance & 0.032 & 1.118 & 7.196 & 7.16 & $\\mathbf{222}$ \\\\\nartifacts/_project/paper/results.tex:47:0.25 & Random     & 0.818 & 0.932 & 1.363 & 0.54 & 1.7 \\\\\nartifacts/_project/paper/results.tex:49:0.30 & Importance & 0.053 & 2.283 & 14.639 & 14.59 & $\\mathbf{274}$ \\\\\nartifacts/_project/paper/results.tex:50:0.30 & Random     & 2.503 & 2.592 & 4.041 & 1.54 & 1.6 \\\\\nartifacts/_project/paper/results.tex:58:\\caption{Severity gradient ($G$) as a function of sparsity level $s$. Importance-based eviction (solid) exhibits an increasing gradient from $69{\\times}$ to $274{\\times}$; random eviction (dashed) remains flat near $1{\\times}$. Shaded regions: 95\\% bootstrap CIs.} % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030\nartifacts/_project/paper/results.tex:66:[Omitted long matching line]\nartifacts/_project/paper/results.tex:71:[Omitted long matching line]\nartifacts/_project/paper/results.tex:79:[Omitted long matching line]\nartifacts/_project/paper/results.tex:81:[Omitted long matching line]\nartifacts/_project/paper/results.tex:86:\\caption{Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM). $\\widetilde{\\Delta}$: median paired difference (importance $-$ random) with bootstrap 95\\% CI ($B{=}10{,}000$); $p$: Bonferroni-corrected Wilcoxon signed-rank $p$ ($k{=}4$). $n{=}\\placeholder{N\\_LLAMA}$ paired problems.}\nartifacts/_project/paper/results.tex:90:$s$ & $\\widetilde{\\Delta}$\\; [95\\% CI] & $p_{\\text{Bonf}}$ \\\\\nartifacts/_project/paper/results.tex:92:0.15 & \\placeholder{}\\; $[\\placeholder{}, \\placeholder{}]$ & \\placeholder{} \\\\\nartifacts/_project/paper/results.tex:93:0.20 & \\placeholder{}\\; $[\\placeholder{}, \\placeholder{}]$ & \\placeholder{} \\\\\nartifacts/_project/paper/results.tex:94:0.25 & \\placeholder{}\\; $[\\placeholder{}, \\placeholder{}]$ & \\placeholder{} \\\\\nartifacts/_project/paper/results.tex:95:0.30 & \\placeholder{}\\; $[\\placeholder{}, \\placeholder{}]$ & $\\mathbf{\\placeholder{}}$ \\\\\nartifacts/_project/paper/results.tex:104:[Omitted long matching line]\nartifacts/_project/paper/results.tex:106:[Omitted long matching line]\nartifacts/_project/paper/results.tex:111:\\caption{Paired $d_z$ for phase-dependent II (low $-$ high) under importance-based eviction. Bootstrap 95\\% CIs ($B{=}10{,}000$).}\nartifacts/_project/paper/results.tex:112:\\label{tab:cohens-d}\nartifacts/_project/paper/results.tex:115:$s$ & DS $d_z$ & $\\widetilde{\\Delta}$ [CI] & QW $d_z$ & $\\widetilde{\\Delta}$ [CI] \\\\\nartifacts/_project/paper/results.tex:117:0.15 & 0.44 & 0.32\\; $[0.20, 0.47]$ & 0.28 & 0.05\\; $[-0.01, 0.11]$\\textsuperscript{ns} \\\\ % exp_id: bf16_ds_imp_s015, bf16_qw_imp_s015\nartifacts/_project/paper/results.tex:118:0.20 & 0.52 & 1.15\\; $[0.66, 1.26]$ & 0.55 & 0.21\\; $[0.07, 0.40]$ \\\\ % exp_id: bf16_ds_imp_s020, bf16_qw_imp_s020\nartifacts/_project/paper/results.tex:119:0.25 & 0.68 & 3.97\\; $[2.83, 5.29]$ & 0.89 & 1.11\\; $[0.61, 1.47]$ \\\\ % exp_id: bf16_ds_imp_s025, bf16_qw_imp_s025\nartifacts/_project/paper/results.tex:120:0.30 & 0.80 & 9.94\\; $[8.39, 16.65]$ & 1.02 & 2.62\\; $[1.72, 3.65]$ \\\\ % exp_id: bf16_ds_imp_s030, bf16_qw_imp_s030\nartifacts/_project/paper/results.tex:122:\\multicolumn{5}{@{}l}{\\footnotesize \\textsuperscript{ns}Marginal at $s{=}0.15$; reliable at $s \\geq 0.20$.}",
    "numLines": 157
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Grep · `toolu_01XDExQWegzhwiwnTSstjFC7`</summary>

```json
{
  "pattern": "partially.confirmed|future.work|C8|C5b|not significant|not.significant|caveat|限定",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "-n": true,
  "-i": true,
  "head_limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "088e11b7-063b-4e22-83eb-4f93d7ee6667",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013CqjG6y997QedCGVyPABvg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6811,
      "cache_read_input_tokens": 24187,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6811
      },
      "output_tokens": 11,
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

_source line 25 · 2026-05-15T01:40:25.025Z_

<details><summary>↩ Tool result · `toolu_01XDExQWegzhwiwnTSstjFC7`</summary>

```text
artifacts/_project/paper/discussion.tex:10:[Omitted long matching line]
artifacts/_project/paper/appendix_moved.tex:73:The per-problem concordance across models is not significant (median $\rho = \placeholder{}$, $p = \placeholder{}$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking. % exp_id: cross_model_analysis.json (spearman_rho=1.0, gradient_permutation_p=0.043, per_problem_concordance_p=0.926, mean_rho=-0.107)
artifacts/_project/paper/appendix_results.tex:7:The per-problem concordance across models is not significant (median $\rho = \placeholder{}$, $p = \placeholder{}$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking. % exp_id: cross_model_analysis.json (spearman_rho=1.0, gradient_permutation_p=0.043, per_problem_concordance_p=0.926, mean_rho=-0.107)
artifacts/_project/paper/appendix_disc_analysis.tex:28:% REBUTTAL: 7B is the most-deployed scale for on-device and cost-constrained serving—exactly where compound sparsity is needed. The mechanism (entropy-discrimination collapse) is scale-agnostic in principle. Scaling experiments are future work.
artifacts/_project/paper/appendix_disc_analysis.tex:57:% REBUTTAL: Our focus is on the practically relevant regime where models retain usable quality. At s>0.30 both strategies degrade severely, making II measurement less informative. The sub-exponential growth (C6, $\Delta$ growth rate $3.8{\times} \to 4.8{\times} \to 2.0{\times}$) suggests saturation at higher sparsity, but confirming this is future work.
artifacts/_project/paper/appendix_disc_analysis.tex:62:% REBUTTAL: This is an empirical finding paper, not a method/system paper. The contribution is characterizing *what happens* (phase-modulated severity) and *why* (entropy-discrimination collapse), not building a system to fix it. Phase-gated controllers are explicitly scoped as future work. The finding is actionable regardless: any compound sparsity deployment should be aware of phase-dependent severity.
artifacts/_project/paper/results.tex:71:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "d208c5f2-a97c-445a-9c63-d460e0623e0e",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "artifacts/_project/paper/discussion.tex:10:[Omitted long matching line]\nartifacts/_project/paper/appendix_moved.tex:73:The per-problem concordance across models is not significant (median $\\rho = \\placeholder{}$, $p = \\placeholder{}$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking. % exp_id: cross_model_analysis.json (spearman_rho=1.0, gradient_permutation_p=0.043, per_problem_concordance_p=0.926, mean_rho=-0.107)\nartifacts/_project/paper/appendix_results.tex:7:The per-problem concordance across models is not significant (median $\\rho = \\placeholder{}$, $p = \\placeholder{}$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking. % exp_id: cross_model_analysis.json (spearman_rho=1.0, gradient_permutation_p=0.043, per_problem_concordance_p=0.926, mean_rho=-0.107)\nartifacts/_project/paper/appendix_disc_analysis.tex:28:% REBUTTAL: 7B is the most-deployed scale for on-device and cost-constrained serving—exactly where compound sparsity is needed. The mechanism (entropy-discrimination collapse) is scale-agnostic in principle. Scaling experiments are future work.\nartifacts/_project/paper/appendix_disc_analysis.tex:57:% REBUTTAL: Our focus is on the practically relevant regime where models retain usable quality. At s>0.30 both strategies degrade severely, making II measurement less informative. The sub-exponential growth (C6, $\\Delta$ growth rate $3.8{\\times} \\to 4.8{\\times} \\to 2.0{\\times}$) suggests saturation at higher sparsity, but confirming this is future work.\nartifacts/_project/paper/appendix_disc_analysis.tex:62:% REBUTTAL: This is an empirical finding paper, not a method/system paper. The contribution is characterizing *what happens* (phase-modulated severity) and *why* (entropy-discrimination collapse), not building a system to fix it. Phase-gated controllers are explicitly scoped as future work. The finding is actionable regardless: any compound sparsity deployment should be aware of phase-dependent severity.\nartifacts/_project/paper/results.tex:71:[Omitted long matching line]",
    "numLines": 7
  }
}
```

</details>

---

### Assistant

_source line 26_

<details><summary>Logged reasoning block</summary>

```text
Now I need to read the full content of each key tex file to understand all numerical values and check for C8, C5b, and Qwen caveats. Let me read the most important files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "7b5edeab-0a80-4d0c-8c71-4761b3b3dfb8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GmXzaPk5xXku3zcbYGLGcA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3090,
      "cache_read_input_tokens": 30998,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3090
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

_source line 27_

Now reading all key tex files in full to catalog every numerical value that needs updating.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "9cee7914-e45b-4d7a-a692-04915fe72a4e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GmXzaPk5xXku3zcbYGLGcA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3090,
      "cache_read_input_tokens": 30998,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3090
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

_source line 28_

<details open><summary>🔧 Tool call — Read · `toolu_0143g2n9FEjvmYzsH3CQBGr7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "f7ff918a-3568-4117-b80b-adc9f2133013",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GmXzaPk5xXku3zcbYGLGcA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3090,
      "cache_read_input_tokens": 30998,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3090
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

_source line 29 · 2026-05-15T01:40:32.176Z_

<details><summary>↩ Tool result · `toolu_0143g2n9FEjvmYzsH3CQBGr7`</summary>

```text
1	\begin{abstract}
2	Compound sparsity---simultaneously pruning attention heads and evicting KV cache entries---is essential for efficient LLM inference but produces super-additive quality degradation whose structure is poorly understood.
3	Prior work treats compound interaction magnitude as approximately constant across the generation process.
4	We show that this assumption is wrong: compound sparsity severity is an emergent phase-strategy interaction that varies by over an order of magnitude across reasoning phases.
5	
6	We evaluate compound sparsity on three models---DeepSeek-R1-Distill-Qwen-7B, Qwen2.5-7B-Instruct (both Qwen2ForCausalLM), and DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM)---spanning two architectures, using 50 MATH-500 problems, measuring the Interaction Index---a super-additivity metric---across quantile-segmented reasoning phases at sparsity levels $s \in \{0.15, 0.20, 0.25, 0.30\}$.
7	Under importance-based KV cache eviction, the median Interaction Index difference between low-sparsity and high-sparsity reasoning phases increases monotonically from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired Cohen's $d_z$ growing from $0.44$ (small) to $0.80$ (large); Bonferroni-corrected permutation tests yield $p < 0.005$ at all four sparsity levels.
8	Random eviction produces no significant phase modulation in 7/8 conditions; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) shows negligible median difference ($\widetilde{\Delta} = \placeholder{}$), confirming that the severity gradient is strategy-specific, not an inherent property of compound sparsity.
9	At $s{=}0.25$, a crossover emerges: importance-based eviction outperforms random in high-sparsity phases ($\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$) yet underperforms in low-sparsity phases ($\widetilde{\mathrm{II}} = 7.196$ vs.\ $1.363$)---a qualitative reversal in strategy ranking.
10	The pattern replicates on Qwen2.5-7B-Instruct at $s \geq 0.20$ ($d_z \geq 0.55$; Spearman $\rho = 1.0$; gradient permutation $p = 0.043$) and on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM), where monotonically increasing median paired differences ($\widetilde{\Delta}$: $0.020 \to 0.356$; $s{=}0.30$ Wilcoxon $p_{\text{Bonf}}{=}0.029$) provide mixed but directionally consistent evidence for cross-architecture generalization, though at ${\sim}$1/40 the absolute magnitude and with substantially weaker interaction than in Qwen2-based architectures. % exp_id: c3_llama
11	
12	We propose entropy-discrimination collapse as an explanatory mechanism: head pruning flattens cumulative importance scores in phases where attention is already broadly distributed, degrading the discriminative power of importance-based eviction in a phase-dependent manner.
13	These findings challenge the phase-invariance assumption in compound sparsity deployment and motivate phase-aware compression budgets for reasoning models.
14	\end{abstract}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "4f970a41-cf91-43ef-a6be-3e8d4c16bde0",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex",
      "content": "\\begin{abstract}\nCompound sparsity---simultaneously pruning attention heads and evicting KV cache entries---is essential for efficient LLM inference but produces super-additive quality degradation whose structure is poorly understood.\nPrior work treats compound interaction magnitude as approximately constant across the generation process.\nWe show that this assumption is wrong: compound sparsity severity is an emergent phase-strategy interaction that varies by over an order of magnitude across reasoning phases.\n\nWe evaluate compound sparsity on three models---DeepSeek-R1-Distill-Qwen-7B, Qwen2.5-7B-Instruct (both Qwen2ForCausalLM), and DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM)---spanning two architectures, using 50 MATH-500 problems, measuring the Interaction Index---a super-additivity metric---across quantile-segmented reasoning phases at sparsity levels $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$.\nUnder importance-based KV cache eviction, the median Interaction Index difference between low-sparsity and high-sparsity reasoning phases increases monotonically from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired Cohen's $d_z$ growing from $0.44$ (small) to $0.80$ (large); Bonferroni-corrected permutation tests yield $p < 0.005$ at all four sparsity levels.\nRandom eviction produces no significant phase modulation in 7/8 conditions; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) shows negligible median difference ($\\widetilde{\\Delta} = \\placeholder{}$), confirming that the severity gradient is strategy-specific, not an inherent property of compound sparsity.\nAt $s{=}0.25$, a crossover emerges: importance-based eviction outperforms random in high-sparsity phases ($\\widetilde{\\mathrm{II}} = 0.032$ vs.\\ $0.818$) yet underperforms in low-sparsity phases ($\\widetilde{\\mathrm{II}} = 7.196$ vs.\\ $1.363$)---a qualitative reversal in strategy ranking.\nThe pattern replicates on Qwen2.5-7B-Instruct at $s \\geq 0.20$ ($d_z \\geq 0.55$; Spearman $\\rho = 1.0$; gradient permutation $p = 0.043$) and on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM), where monotonically increasing median paired differences ($\\widetilde{\\Delta}$: $0.020 \\to 0.356$; $s{=}0.30$ Wilcoxon $p_{\\text{Bonf}}{=}0.029$) provide mixed but directionally consistent evidence for cross-architecture generalization, though at ${\\sim}$1/40 the absolute magnitude and with substantially weaker interaction than in Qwen2-based architectures. % exp_id: c3_llama\n\nWe propose entropy-discrimination collapse as an explanatory mechanism: head pruning flattens cumulative importance scores in phases where attention is already broadly distributed, degrading the discriminative power of importance-based eviction in a phase-dependent manner.\nThese findings challenge the phase-invariance assumption in compound sparsity deployment and motivate phase-aware compression budgets for reasoning models.\n\\end{abstract}",
      "numLines": 14,
      "startLine": 1,
      "totalLines": 14
    }
  }
}
```

</details>

---

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — Read · `toolu_01GYN5WgpQv6tGxDBuqujPZN`</summary>

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
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "252a87c9-d7a1-43e7-9c31-3496b6746f93",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GmXzaPk5xXku3zcbYGLGcA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3090,
      "cache_read_input_tokens": 30998,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3090
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

_source line 31 · 2026-05-15T01:40:32.683Z_

<details><summary>↩ Tool result · `toolu_01GYN5WgpQv6tGxDBuqujPZN`</summary>

```text
1	
2	\section{Results}
3	\label{sec:results}
4	
5	\subsection{Strategy-Dependent Severity}
6	\label{sec:strategy-severity}
7	
8	Table~\ref{tab:aggregate-ii} reports the median compound severity difference across strategies and sparsity levels. Under importance-based eviction, $\Delta$ increases from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$---a $37{\times}$ amplification. Under random eviction, no systematic growth is observed ($-0.02$ to $1.54$), confirming that compound severity depends qualitatively on eviction strategy. % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json
9	
10	\begin{table}[t]
11	\centering
12	\small
13	\caption{Median compound severity difference ($\Delta = \widetilde{\mathrm{II}}_{\textit{low}} - \widetilde{\mathrm{II}}_{\textit{high}}$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}50$ MATH-500 problems).}
14	\label{tab:aggregate-ii}
15	\begin{tabular}{@{}lcccc@{}}
16	\toprule
17	Strategy & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
18	\midrule
19	Importance & 0.39 & 1.48 & 7.16 & 14.59 \\ % exp_id: bf16_importance_s015..s030; source: experiment_summary_table.json median_diff
20	Random     & 0.01 & $-$0.02 & 0.54 & 1.54 \\ % exp_id: bf16_ds_rand_s015..s030; source: experiment_summary_table.json median_diff
21	\bottomrule
22	\end{tabular}
23	\end{table}
24	
25	
26	\subsection{Phase-Modulated Amplification}
27	\label{sec:phase-amplification}
28	
29	Decomposing II by reasoning phase reveals that strategy-dependent severity is driven by amplification in the low-sparsity phase. Table~\ref{tab:main-results} reports the full per-phase breakdown. The severity gradient $G$ increases from $69{\times}$ at $s{=}0.15$ to $274{\times}$ at $s{=}0.30$ under importance-based eviction, while the high-sparsity phase experiences near-zero interaction ($\widetilde{\mathrm{II}}_{\textit{high}}$ ranges from $0.006$ to $0.053$). Under random eviction, $G \approx 0.9$--$1.7{\times}$ at all sparsity levels. Figure~\ref{fig:hero} visualizes this contrast. % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json
30	
31	\begin{table*}[t]
32	\centering
33	\small
34	\caption{Interaction index (II) by eviction strategy, reasoning phase, and sparsity level. II values are problem-level medians across 50 problems. $\Delta = \widetilde{\mathrm{II}}_{\textit{low}} - \widetilde{\mathrm{II}}_{\textit{high}}$. $G = \widetilde{\mathrm{II}}_{\textit{low}} / \widetilde{\mathrm{II}}_{\textit{high}}$.}
35	\label{tab:main-results}
36	\begin{tabular}{@{}llccccr@{}}
37	\toprule
38	$s$ & Strategy & $\widetilde{\mathrm{II}}_{\textit{high}}$ & $\widetilde{\mathrm{II}}_{\textit{mid}}$ & $\widetilde{\mathrm{II}}_{\textit{low}}$ & $\Delta$ & $G$ \\
39	\midrule
40	0.15 & Importance & 0.006 & 0.081 & 0.398 & 0.39 & $\mathbf{69}$ \\
41	0.15 & Random     & 0.093 & 0.097 & 0.103 & 0.01 & 1.1 \\
42	\addlinespace
43	0.20 & Importance & 0.015 & 0.203 & 1.496 & 1.48 & $\mathbf{103}$ \\
44	0.20 & Random     & 0.292 & 0.350 & 0.276 & $-$0.02 & 0.9 \\
45	\addlinespace
46	0.25 & Importance & 0.032 & 1.118 & 7.196 & 7.16 & $\mathbf{222}$ \\
47	0.25 & Random     & 0.818 & 0.932 & 1.363 & 0.54 & 1.7 \\
48	\addlinespace
49	0.30 & Importance & 0.053 & 2.283 & 14.639 & 14.59 & $\mathbf{274}$ \\
50	0.30 & Random     & 2.503 & 2.592 & 4.041 & 1.54 & 1.6 \\
51	\bottomrule
52	\end{tabular}
53	\end{table*}
54	
55	\begin{figure}[t]
56	\centering
57	\includegraphics[width=\columnwidth]{fig1_dose_response.pdf}
58	\caption{Severity gradient ($G$) as a function of sparsity level $s$. Importance-based eviction (solid) exhibits an increasing gradient from $69{\times}$ to $274{\times}$; random eviction (dashed) remains flat near $1{\times}$. Shaded regions: 95\% bootstrap CIs.} % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030
59	\label{fig:hero}
60	\end{figure}
61	
62	
63	\subsection{Phase-Strategy Crossover}
64	\label{sec:crossover}
65	
66	A strategy ranking reversal emerges across all sparsity levels: at $s{=}0.25$, importance-based eviction yields \emph{lower} II than random in the high-sparsity phase ($0.032$ vs.\ $0.818$) but \emph{higher} II in the low-sparsity phase ($7.196$ vs.\ $1.363$---a $5.3{\times}$ reversal), demonstrating that no single strategy dominates uniformly. Full crossover analysis and visualization appear in Appendix~\ref{app:crossover-details}. % exp_id: bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json; 7.196/1.363=5.28
67	
68	\subsection{Cross-Model Replication}
69	\label{sec:cross-model}
70	
71	Qwen2.5-7B-Instruct (standard instruction tuning, same Qwen2 backbone) reproduces the monotonic severity gradient: $\Delta$ increases from $0.04$ at $s{=}0.15$ to $2.94$ at $s{=}0.30$, paralleling DeepSeek at ${\sim}1/5$ the magnitude. Both models yield strictly increasing $d_z$ trajectories (Spearman $\rho = 1.0$; gradient permutation $p = 0.043$). The effect is marginal at $s{=}0.15$ ($d_z{=}0.28$, CI includes zero) but reliable at $s \geq 0.20$ ($d_z \geq 0.55$). A caveat applies to mid-phase comparisons: on Qwen2.5-7B-Instruct, approximately \placeholder{NULL\_PCT}\% of problems yield near-zero Interaction Index in the mid-sparsity phase, where attention patterns exhibit insufficient variation to produce measurable compound interaction. This elevated null rate reduces the effective sample size for mid-phase comparisons; our primary cross-model analysis therefore focuses on the low--high phase contrast ($\Delta$), which is unaffected by this limitation. Per-phase effective sample sizes are reported in Appendix~\ref{app:qwen-null-rate}. Full cross-model tables and figures appear in Appendix~\ref{app:cross-model-details}. % exp_id: cross_model_analysis.json; cohens_d_bf16_qwen.json
72	
73	
74	\subsection{Cross-Architecture Validation}
75	\label{sec:cross-arch}
76	
77	To test whether the phase-modulated severity pattern extends beyond the Qwen2 architecture, we replicate the experiment on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, 8B parameters; $n{=}49$ paired problems). Table~\ref{tab:llama-cross-arch} reports the strategy-dependent severity comparison across sparsity levels.
78	
79	Table~\ref{tab:llama-cross-arch} reports the full results. The evidence for a strategy contrast on LLaMA is mixed: at $s{=}0.15$, the bootstrap CI excludes zero ($[0.002, 0.043]$) but the Bonferroni-corrected Wilcoxon test is non-significant ($p_{\text{Bonf}}{=}0.219$); conversely, at $s{=}0.30$ the CI spans zero ($[-0.069, 0.544]$) while the Wilcoxon test reaches significance ($p_{\text{Bonf}}{=}0.029$). At intermediate levels ($s \in \{0.20, 0.25\}$), neither CI nor Wilcoxon reaches significance. The median paired difference increases monotonically ($\widetilde{\Delta}$: $0.020 \to 0.356$), consistent with a genuine but weak trend---partially confirming the cross-architecture hypothesis while underscoring the substantially weaker interaction on LlamaForCausalLM. % exp_id: c3_llama
80	
81	The absolute magnitude is architecture-dependent: LLaMA severity differences are ${\sim}40{\times}$ smaller than DeepSeek and ${\sim}7{\times}$ smaller than Qwen, and the interaction is substantially weaker---random eviction also shows a non-trivial phase gradient (Wilcoxon $p < \placeholder{}$ at $s{=}0.30$), reducing the strategy contrast observed in Qwen2 models. The directional pattern---importance $>$ random, larger phase gradient under importance---is qualitatively consistent across all three models spanning two architectures (Qwen2ForCausalLM, LlamaForCausalLM), though the interaction magnitude is substantially weaker on LlamaForCausalLM. % exp_id: c3_llama; cross_model_analysis.json
82	
83	\begin{table}[t]
84	\centering
85	\small
86	\caption{Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM). $\widetilde{\Delta}$: median paired difference (importance $-$ random) with bootstrap 95\% CI ($B{=}10{,}000$); $p$: Bonferroni-corrected Wilcoxon signed-rank $p$ ($k{=}4$). $n{=}\placeholder{N\_LLAMA}$ paired problems.}
87	\label{tab:llama-cross-arch}
88	\begin{tabular}{@{}lcc@{}}
89	\toprule
90	$s$ & $\widetilde{\Delta}$\; [95\% CI] & $p_{\text{Bonf}}$ \\
91	\midrule
92	0.15 & \placeholder{}\; $[\placeholder{}, \placeholder{}]$ & \placeholder{} \\
93	0.20 & \placeholder{}\; $[\placeholder{}, \placeholder{}]$ & \placeholder{} \\
94	0.25 & \placeholder{}\; $[\placeholder{}, \placeholder{}]$ & \placeholder{} \\
95	0.30 & \placeholder{}\; $[\placeholder{}, \placeholder{}]$ & $\mathbf{\placeholder{}}$ \\
96	\bottomrule
97	\end{tabular}
98	\end{table}
99	
100	
101	\subsection{Statistical Validation}
102	\label{sec:stat-validation}
103	
104	Paired permutation tests ($10{,}000$ permutations, Bonferroni-corrected) confirm that importance-based eviction produces significantly larger phase-dependent severity than random eviction at all four sparsity levels ($p_{\text{Bonf}} < 0.005$), with observed median differences increasing monotonically from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$. Full permutation test results and forest plot appear in Appendix~\ref{app:permutation-details}. % exp_id: deepseek_bf16_permtest; source: permutation_test_results.json
105	
106	Table~\ref{tab:cohens-d} reports paired Cohen's $d_z$ for both models. For DeepSeek, effect sizes grow from $d_z{=}0.44$ (small) to $d_z{=}0.80$ (large). For Qwen, the effect is marginal at $s{=}0.15$ ($d_z{=}0.28$, CI includes zero), becoming reliable at $s \geq 0.20$ ($d_z \geq 0.55$). At $s \geq 0.25$, Qwen exhibits larger standardized effect sizes ($d_z{=}0.89$/$1.02$ vs.\ $0.68$/$0.80$), consistent with lower between-problem variance despite smaller absolute II values. % exp_id: cohens_d_bf16.json; cohens_d_bf16_qwen.json
107	
108	\begin{table}[t]
109	\centering
110	\small
111	\caption{Paired $d_z$ for phase-dependent II (low $-$ high) under importance-based eviction. Bootstrap 95\% CIs ($B{=}10{,}000$).}
112	\label{tab:cohens-d}
113	\begin{tabular}{@{}lcccc@{}}
114	\toprule
115	$s$ & DS $d_z$ & $\widetilde{\Delta}$ [CI] & QW $d_z$ & $\widetilde{\Delta}$ [CI] \\
116	\midrule
117	0.15 & 0.44 & 0.32\; $[0.20, 0.47]$ & 0.28 & 0.05\; $[-0.01, 0.11]$\textsuperscript{ns} \\ % exp_id: bf16_ds_imp_s015, bf16_qw_imp_s015
118	0.20 & 0.52 & 1.15\; $[0.66, 1.26]$ & 0.55 & 0.21\; $[0.07, 0.40]$ \\ % exp_id: bf16_ds_imp_s020, bf16_qw_imp_s020
119	0.25 & 0.68 & 3.97\; $[2.83, 5.29]$ & 0.89 & 1.11\; $[0.61, 1.47]$ \\ % exp_id: bf16_ds_imp_s025, bf16_qw_imp_s025
120	0.30 & 0.80 & 9.94\; $[8.39, 16.65]$ & 1.02 & 2.62\; $[1.72, 3.65]$ \\ % exp_id: bf16_ds_imp_s030, bf16_qw_imp_s030
121	\bottomrule
122	\multicolumn{5}{@{}l}{\footnotesize \textsuperscript{ns}Marginal at $s{=}0.15$; reliable at $s \geq 0.20$.}
123	\end{tabular}
124	\end{table}
125	
126	We provide a mechanistic analysis in terms of entropy-discrimination collapse in \S\ref{sec:analysis}.
127	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "0a09bf55-4018-4be6-8d5a-f729dea21fad",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex",
      "content": "\n\\section{Results}\n\\label{sec:results}\n\n\\subsection{Strategy-Dependent Severity}\n\\label{sec:strategy-severity}\n\nTable~\\ref{tab:aggregate-ii} reports the median compound severity difference across strategies and sparsity levels. Under importance-based eviction, $\\Delta$ increases from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$---a $37{\\times}$ amplification. Under random eviction, no systematic growth is observed ($-0.02$ to $1.54$), confirming that compound severity depends qualitatively on eviction strategy. % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Median compound severity difference ($\\Delta = \\widetilde{\\mathrm{II}}_{\\textit{low}} - \\widetilde{\\mathrm{II}}_{\\textit{high}}$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}50$ MATH-500 problems).}\n\\label{tab:aggregate-ii}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nStrategy & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\\\\n\\midrule\nImportance & 0.39 & 1.48 & 7.16 & 14.59 \\\\ % exp_id: bf16_importance_s015..s030; source: experiment_summary_table.json median_diff\nRandom     & 0.01 & $-$0.02 & 0.54 & 1.54 \\\\ % exp_id: bf16_ds_rand_s015..s030; source: experiment_summary_table.json median_diff\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Phase-Modulated Amplification}\n\\label{sec:phase-amplification}\n\nDecomposing II by reasoning phase reveals that strategy-dependent severity is driven by amplification in the low-sparsity phase. Table~\\ref{tab:main-results} reports the full per-phase breakdown. The severity gradient $G$ increases from $69{\\times}$ at $s{=}0.15$ to $274{\\times}$ at $s{=}0.30$ under importance-based eviction, while the high-sparsity phase experiences near-zero interaction ($\\widetilde{\\mathrm{II}}_{\\textit{high}}$ ranges from $0.006$ to $0.053$). Under random eviction, $G \\approx 0.9$--$1.7{\\times}$ at all sparsity levels. Figure~\\ref{fig:hero} visualizes this contrast. % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Interaction index (II) by eviction strategy, reasoning phase, and sparsity level. II values are problem-level medians across 50 problems. $\\Delta = \\widetilde{\\mathrm{II}}_{\\textit{low}} - \\widetilde{\\mathrm{II}}_{\\textit{high}}$. $G = \\widetilde{\\mathrm{II}}_{\\textit{low}} / \\widetilde{\\mathrm{II}}_{\\textit{high}}$.}\n\\label{tab:main-results}\n\\begin{tabular}{@{}llccccr@{}}\n\\toprule\n$s$ & Strategy & $\\widetilde{\\mathrm{II}}_{\\textit{high}}$ & $\\widetilde{\\mathrm{II}}_{\\textit{mid}}$ & $\\widetilde{\\mathrm{II}}_{\\textit{low}}$ & $\\Delta$ & $G$ \\\\\n\\midrule\n0.15 & Importance & 0.006 & 0.081 & 0.398 & 0.39 & $\\mathbf{69}$ \\\\\n0.15 & Random     & 0.093 & 0.097 & 0.103 & 0.01 & 1.1 \\\\\n\\addlinespace\n0.20 & Importance & 0.015 & 0.203 & 1.496 & 1.48 & $\\mathbf{103}$ \\\\\n0.20 & Random     & 0.292 & 0.350 & 0.276 & $-$0.02 & 0.9 \\\\\n\\addlinespace\n0.25 & Importance & 0.032 & 1.118 & 7.196 & 7.16 & $\\mathbf{222}$ \\\\\n0.25 & Random     & 0.818 & 0.932 & 1.363 & 0.54 & 1.7 \\\\\n\\addlinespace\n0.30 & Importance & 0.053 & 2.283 & 14.639 & 14.59 & $\\mathbf{274}$ \\\\\n0.30 & Random     & 2.503 & 2.592 & 4.041 & 1.54 & 1.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig1_dose_response.pdf}\n\\caption{Severity gradient ($G$) as a function of sparsity level $s$. Importance-based eviction (solid) exhibits an increasing gradient from $69{\\times}$ to $274{\\times}$; random eviction (dashed) remains flat near $1{\\times}$. Shaded regions: 95\\% bootstrap CIs.} % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030\n\\label{fig:hero}\n\\end{figure}\n\n\n\\subsection{Phase-Strategy Crossover}\n\\label{sec:crossover}\n\nA strategy ranking reversal emerges across all sparsity levels: at $s{=}0.25$, importance-based eviction yields \\emph{lower} II than random in the high-sparsity phase ($0.032$ vs.\\ $0.818$) but \\emph{higher} II in the low-sparsity phase ($7.196$ vs.\\ $1.363$---a $5.3{\\times}$ reversal), demonstrating that no single strategy dominates uniformly. Full crossover analysis and visualization appear in Appendix~\\ref{app:crossover-details}. % exp_id: bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json; 7.196/1.363=5.28\n\n\\subsection{Cross-Model Replication}\n\\label{sec:cross-model}\n\nQwen2.5-7B-Instruct (standard instruction tuning, same Qwen2 backbone) reproduces the monotonic severity gradient: $\\Delta$ increases from $0.04$ at $s{=}0.15$ to $2.94$ at $s{=}0.30$, paralleling DeepSeek at ${\\sim}1/5$ the magnitude. Both models yield strictly increasing $d_z$ trajectories (Spearman $\\rho = 1.0$; gradient permutation $p = 0.043$). The effect is marginal at $s{=}0.15$ ($d_z{=}0.28$, CI includes zero) but reliable at $s \\geq 0.20$ ($d_z \\geq 0.55$). A caveat applies to mid-phase comparisons: on Qwen2.5-7B-Instruct, approximately \\placeholder{NULL\\_PCT}\\% of problems yield near-zero Interaction Index in the mid-sparsity phase, where attention patterns exhibit insufficient variation to produce measurable compound interaction. This elevated null rate reduces the effective sample size for mid-phase comparisons; our primary cross-model analysis therefore focuses on the low--high phase contrast ($\\Delta$), which is unaffected by this limitation. Per-phase effective sample sizes are reported in Appendix~\\ref{app:qwen-null-rate}. Full cross-model tables and figures appear in Appendix~\\ref{app:cross-model-details}. % exp_id: cross_model_analysis.json; cohens_d_bf16_qwen.json\n\n\n\\subsection{Cross-Architecture Validation}\n\\label{sec:cross-arch}\n\nTo test whether the phase-modulated severity pattern extends beyond the Qwen2 architecture, we replicate the experiment on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, 8B parameters; $n{=}49$ paired problems). Table~\\ref{tab:llama-cross-arch} reports the strategy-dependent severity comparison across sparsity levels.\n\nTable~\\ref{tab:llama-cross-arch} reports the full results. The evidence for a strategy contrast on LLaMA is mixed: at $s{=}0.15$, the bootstrap CI excludes zero ($[0.002, 0.043]$) but the Bonferroni-corrected Wilcoxon test is non-significant ($p_{\\text{Bonf}}{=}0.219$); conversely, at $s{=}0.30$ the CI spans zero ($[-0.069, 0.544]$) while the Wilcoxon test reaches significance ($p_{\\text{Bonf}}{=}0.029$). At intermediate levels ($s \\in \\{0.20, 0.25\\}$), neither CI nor Wilcoxon reaches significance. The median paired difference increases monotonically ($\\widetilde{\\Delta}$: $0.020 \\to 0.356$), consistent with a genuine but weak trend---partially confirming the cross-architecture hypothesis while underscoring the substantially weaker interaction on LlamaForCausalLM. % exp_id: c3_llama\n\nThe absolute magnitude is architecture-dependent: LLaMA severity differences are ${\\sim}40{\\times}$ smaller than DeepSeek and ${\\sim}7{\\times}$ smaller than Qwen, and the interaction is substantially weaker---random eviction also shows a non-trivial phase gradient (Wilcoxon $p < \\placeholder{}$ at $s{=}0.30$), reducing the strategy contrast observed in Qwen2 models. The directional pattern---importance $>$ random, larger phase gradient under importance---is qualitatively consistent across all three models spanning two architectures (Qwen2ForCausalLM, LlamaForCausalLM), though the interaction magnitude is substantially weaker on LlamaForCausalLM. % exp_id: c3_llama; cross_model_analysis.json\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM). $\\widetilde{\\Delta}$: median paired difference (importance $-$ random) with bootstrap 95\\% CI ($B{=}10{,}000$); $p$: Bonferroni-corrected Wilcoxon signed-rank $p$ ($k{=}4$). $n{=}\\placeholder{N\\_LLAMA}$ paired problems.}\n\\label{tab:llama-cross-arch}\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n$s$ & $\\widetilde{\\Delta}$\\; [95\\% CI] & $p_{\\text{Bonf}}$ \\\\\n\\midrule\n0.15 & \\placeholder{}\\; $[\\placeholder{}, \\placeholder{}]$ & \\placeholder{} \\\\\n0.20 & \\placeholder{}\\; $[\\placeholder{}, \\placeholder{}]$ & \\placeholder{} \\\\\n0.25 & \\placeholder{}\\; $[\\placeholder{}, \\placeholder{}]$ & \\placeholder{} \\\\\n0.30 & \\placeholder{}\\; $[\\placeholder{}, \\placeholder{}]$ & $\\mathbf{\\placeholder{}}$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Statistical Validation}\n\\label{sec:stat-validation}\n\nPaired permutation tests ($10{,}000$ permutations, Bonferroni-corrected) confirm that importance-based eviction produces significantly larger phase-dependent severity than random eviction at all four sparsity levels ($p_{\\text{Bonf}} < 0.005$), with observed median differences increasing monotonically from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$. Full permutation test results and forest plot appear in Appendix~\\ref{app:permutation-details}. % exp_id: deepseek_bf16_permtest; source: permutation_test_results.json\n\nTable~\\ref{tab:cohens-d} reports paired Cohen's $d_z$ for both models. For DeepSeek, effect sizes grow from $d_z{=}0.44$ (small) to $d_z{=}0.80$ (large). For Qwen, the effect is marginal at $s{=}0.15$ ($d_z{=}0.28$, CI includes zero), becoming reliable at $s \\geq 0.20$ ($d_z \\geq 0.55$). At $s \\geq 0.25$, Qwen exhibits larger standardized effect sizes ($d_z{=}0.89$/$1.02$ vs.\\ $0.68$/$0.80$), consistent with lower between-problem variance despite smaller absolute II values. % exp_id: cohens_d_bf16.json; cohens_d_bf16_qwen.json\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Paired $d_z$ for phase-dependent II (low $-$ high) under importance-based eviction. Bootstrap 95\\% CIs ($B{=}10{,}000$).}\n\\label{tab:cohens-d}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n$s$ & DS $d_z$ & $\\widetilde{\\Delta}$ [CI] & QW $d_z$ & $\\widetilde{\\Delta}$ [CI] \\\\\n\\midrule\n0.15 & 0.44 & 0.32\\; $[0.20, 0.47]$ & 0.28 & 0.05\\; $[-0.01, 0.11]$\\textsuperscript{ns} \\\\ % exp_id: bf16_ds_imp_s015, bf16_qw_imp_s015\n0.20 & 0.52 & 1.15\\; $[0.66, 1.26]$ & 0.55 & 0.21\\; $[0.07, 0.40]$ \\\\ % exp_id: bf16_ds_imp_s020, bf16_qw_imp_s020\n0.25 & 0.68 & 3.97\\; $[2.83, 5.29]$ & 0.89 & 1.11\\; $[0.61, 1.47]$ \\\\ % exp_id: bf16_ds_imp_s025, bf16_qw_imp_s025\n0.30 & 0.80 & 9.94\\; $[8.39, 16.65]$ & 1.02 & 2.62\\; $[1.72, 3.65]$ \\\\ % exp_id: bf16_ds_imp_s030, bf16_qw_imp_s030\n\\bottomrule\n\\multicolumn{5}{@{}l}{\\footnotesize \\textsuperscript{ns}Marginal at $s{=}0.15$; reliable at $s \\geq 0.20$.}\n\\end{tabular}\n\\end{table}\n\nWe provide a mechanistic analysis in terms of entropy-discrimination collapse in \\S\\ref{sec:analysis}.\n",
      "numLines": 127,
      "startLine": 1,
      "totalLines": 127
    }
  }
}
```

</details>

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — Read · `toolu_01GixopVJP4gFHeNWBT9UWWE`</summary>

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
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "6ea0b88b-d8ad-4f4a-934c-630132a2f7d8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GmXzaPk5xXku3zcbYGLGcA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3090,
      "cache_read_input_tokens": 30998,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3090
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

_source line 33 · 2026-05-15T01:40:33.144Z_

<details><summary>↩ Tool result · `toolu_01GixopVJP4gFHeNWBT9UWWE`</summary>

```text
1	\section{Analysis: Entropy-Discrimination Collapse}
2	\label{sec:analysis}
3	
4	We propose \emph{discrimination collapse} as the primary mechanism driving the phase-strategy interaction. Head pruning reduces the number of heads contributing to cumulative importance scores, flattening the score distribution: the Gini coefficient decreases by $0.030$--$0.081$ (DeepSeek) and $0.010$--$0.020$ (Qwen) across all sparsity levels, with consistent negative deltas in all 16 conditions (Appendix~\ref{app:analysis}, Table~\ref{tab:discrimination-metrics-full}). When importance scores lose discriminability, thresholding degenerates into noise-sensitive selection---functionally approaching biased random eviction. This effect is phase-dependent: in low-sparsity phases, attention is already broadly distributed, so pruning-induced flattening has maximum impact; in high-sparsity phases, concentration is preserved. Random eviction is immune because its decisions are independent of score quality, explaining $G \approx 1$. % exp_id: c4_entropy_deepseek, c4_entropy_qwen
5	
6	Beyond discrimination collapse, head pruning redistributes the attention entropy of surviving heads. For DeepSeek, the entropy delta is consistently negative ($\Delta\mathcal{H} \in [-0.047, -0.040]$), indicating that importance-based pruning systematically selects heads whose removal concentrates attention in survivors. For Qwen, the pattern partially replicates at $s \leq 0.20$ but reverses at $s{=}0.25$ ($\Delta\mathcal{H} = +0.045$), suggesting model-specific head specialization patterns (Appendix~\ref{app:analysis}, Table~\ref{tab:entropy-deltas}). We characterize discrimination collapse as the robust, model-independent driver, with entropy redistribution as a secondary, model-dependent amplifier. % exp_id: c4_entropy_deepseek, c4_entropy_qwen
7	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "f33c8d88-a9e9-40c1-a444-9cceb16cd255",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex",
      "content": "\\section{Analysis: Entropy-Discrimination Collapse}\n\\label{sec:analysis}\n\nWe propose \\emph{discrimination collapse} as the primary mechanism driving the phase-strategy interaction. Head pruning reduces the number of heads contributing to cumulative importance scores, flattening the score distribution: the Gini coefficient decreases by $0.030$--$0.081$ (DeepSeek) and $0.010$--$0.020$ (Qwen) across all sparsity levels, with consistent negative deltas in all 16 conditions (Appendix~\\ref{app:analysis}, Table~\\ref{tab:discrimination-metrics-full}). When importance scores lose discriminability, thresholding degenerates into noise-sensitive selection---functionally approaching biased random eviction. This effect is phase-dependent: in low-sparsity phases, attention is already broadly distributed, so pruning-induced flattening has maximum impact; in high-sparsity phases, concentration is preserved. Random eviction is immune because its decisions are independent of score quality, explaining $G \\approx 1$. % exp_id: c4_entropy_deepseek, c4_entropy_qwen\n\nBeyond discrimination collapse, head pruning redistributes the attention entropy of surviving heads. For DeepSeek, the entropy delta is consistently negative ($\\Delta\\mathcal{H} \\in [-0.047, -0.040]$), indicating that importance-based pruning systematically selects heads whose removal concentrates attention in survivors. For Qwen, the pattern partially replicates at $s \\leq 0.20$ but reverses at $s{=}0.25$ ($\\Delta\\mathcal{H} = +0.045$), suggesting model-specific head specialization patterns (Appendix~\\ref{app:analysis}, Table~\\ref{tab:entropy-deltas}). We characterize discrimination collapse as the robust, model-independent driver, with entropy redistribution as a secondary, model-dependent amplifier. % exp_id: c4_entropy_deepseek, c4_entropy_qwen\n",
      "numLines": 7,
      "startLine": 1,
      "totalLines": 7
    }
  }
}
```

</details>

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Read · `toolu_01Vjqbha6WFerRV5jfY3sAE6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "62b928f0-45a3-4f87-be04-55dfe1467058",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GmXzaPk5xXku3zcbYGLGcA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3090,
      "cache_read_input_tokens": 30998,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3090
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

_source line 35 · 2026-05-15T01:40:33.767Z_

<details><summary>↩ Tool result · `toolu_01Vjqbha6WFerRV5jfY3sAE6`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Quantitative surprise.}
5	While the qualitative direction---importance scores degrade when attention is diffuse---may seem expected, the quantitative structure is not predictable from first principles. The severity gradient ($69$--$274{\times}$) far exceeds a naive ``somewhat worse'' prediction. The crossover---where importance-based eviction simultaneously outperforms random in high-sparsity phases ($\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$) and underperforms in low-sparsity phases ($7.196$ vs.\ $1.363$)---cannot be derived from single-axis entropy reasoning. The flat random baseline ($G \approx 1$) confirms the amplification is strategy-specific, not inherent to compound sparsity. % exp_id: bf16_importance_s015..s030, bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json
6	
7	\paragraph{Implications for deployment.}
8	Applying a uniform compression budget across all inference steps implicitly accepts order-of-magnitude severity penalties during low-sparsity reasoning phases. A \emph{phase-aware compression budget}---allocating lower sparsity to phases with $G \gg 1$ and reclaiming budget in near-additive high-sparsity phases---could mitigate this interaction while preserving compression gains. The severity gradient provides a natural signal for such allocation. Discrimination collapse depends on attention-mass-based importance scoring shared by major KV cache methods (H$_2$O \cite{h2o-neurips2023}, SnapKV \cite{snapkv-neurips2024}, PyramidKV \cite{pyramidkv-2024}), suggesting broad applicability.
9	
10	A preliminary pilot experiment explored oracle phase-aware budget reallocation, shifting sparsity budget from high-severity low-sparsity phases to low-severity high-sparsity phases. At $s{=}0.25$, oracle recovery---the fraction of compound interaction eliminated by phase-aware allocation---reached \placeholder{ORACLE\_PCT}\% (Wilcoxon $p = \placeholder{ORACLE\_P}$), below the pre-registered 30\% gate for claiming practical mitigation. A heuristic variant achieved \placeholder{HEUR\_PCT}\% recovery ($p = \placeholder{HEUR\_P}$), but 95\% CIs for both conditions span zero. These results indicate that phase-aware budget reallocation alone is insufficient to neutralize the severity gradient; effective mitigation likely requires joint optimization of budget allocation and eviction strategy selection across phases---a promising direction for future work.
11	
12	Extended discussion in Appendix~\ref{app:extended-discussion}.
13	
14	\paragraph{Architecture-dependent magnitude.}
15	Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM) provides partial support for the qualitative pattern---monotonically increasing severity gradient under importance-based eviction with within-strategy phase gradient $d_z \geq 1.0$---while revealing that absolute severity magnitudes are architecture-dependent (${\sim}40{\times}$ smaller than DeepSeek, ${\sim}7{\times}$ smaller than Qwen) and the strategy--phase interaction is substantially weaker than in Qwen2-based architectures. Notably, random pruning also exhibits a non-trivial phase gradient on LLaMA (Wilcoxon $p < \placeholder{}$), reducing the contrast between strategies. This dissociation between qualitatively consistent directional trends and markedly different magnitudes suggests the phase-strategy interaction may be a general property of compound sparsity on reasoning models, while its quantitative impact---and the degree to which it is strategy-specific---depends on architecture-specific attention distributions and head specialization patterns. % exp_id: c3_llama
16	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "5a09ba35-501c-430f-a9f6-fb6803bba2a4",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex",
      "content": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Quantitative surprise.}\nWhile the qualitative direction---importance scores degrade when attention is diffuse---may seem expected, the quantitative structure is not predictable from first principles. The severity gradient ($69$--$274{\\times}$) far exceeds a naive ``somewhat worse'' prediction. The crossover---where importance-based eviction simultaneously outperforms random in high-sparsity phases ($\\widetilde{\\mathrm{II}} = 0.032$ vs.\\ $0.818$) and underperforms in low-sparsity phases ($7.196$ vs.\\ $1.363$)---cannot be derived from single-axis entropy reasoning. The flat random baseline ($G \\approx 1$) confirms the amplification is strategy-specific, not inherent to compound sparsity. % exp_id: bf16_importance_s015..s030, bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json\n\n\\paragraph{Implications for deployment.}\nApplying a uniform compression budget across all inference steps implicitly accepts order-of-magnitude severity penalties during low-sparsity reasoning phases. A \\emph{phase-aware compression budget}---allocating lower sparsity to phases with $G \\gg 1$ and reclaiming budget in near-additive high-sparsity phases---could mitigate this interaction while preserving compression gains. The severity gradient provides a natural signal for such allocation. Discrimination collapse depends on attention-mass-based importance scoring shared by major KV cache methods (H$_2$O \\cite{h2o-neurips2023}, SnapKV \\cite{snapkv-neurips2024}, PyramidKV \\cite{pyramidkv-2024}), suggesting broad applicability.\n\nA preliminary pilot experiment explored oracle phase-aware budget reallocation, shifting sparsity budget from high-severity low-sparsity phases to low-severity high-sparsity phases. At $s{=}0.25$, oracle recovery---the fraction of compound interaction eliminated by phase-aware allocation---reached \\placeholder{ORACLE\\_PCT}\\% (Wilcoxon $p = \\placeholder{ORACLE\\_P}$), below the pre-registered 30\\% gate for claiming practical mitigation. A heuristic variant achieved \\placeholder{HEUR\\_PCT}\\% recovery ($p = \\placeholder{HEUR\\_P}$), but 95\\% CIs for both conditions span zero. These results indicate that phase-aware budget reallocation alone is insufficient to neutralize the severity gradient; effective mitigation likely requires joint optimization of budget allocation and eviction strategy selection across phases---a promising direction for future work.\n\nExtended discussion in Appendix~\\ref{app:extended-discussion}.\n\n\\paragraph{Architecture-dependent magnitude.}\nCross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM) provides partial support for the qualitative pattern---monotonically increasing severity gradient under importance-based eviction with within-strategy phase gradient $d_z \\geq 1.0$---while revealing that absolute severity magnitudes are architecture-dependent (${\\sim}40{\\times}$ smaller than DeepSeek, ${\\sim}7{\\times}$ smaller than Qwen) and the strategy--phase interaction is substantially weaker than in Qwen2-based architectures. Notably, random pruning also exhibits a non-trivial phase gradient on LLaMA (Wilcoxon $p < \\placeholder{}$), reducing the contrast between strategies. This dissociation between qualitatively consistent directional trends and markedly different magnitudes suggests the phase-strategy interaction may be a general property of compound sparsity on reasoning models, while its quantitative impact---and the degree to which it is strategy-specific---depends on architecture-specific attention distributions and head specialization patterns. % exp_id: c3_llama\n",
      "numLines": 16,
      "startLine": 1,
      "totalLines": 16
    }
  }
}
```

</details>

---

### Tool call

_source line 36_

<details open><summary>🔧 Tool call — Read · `toolu_01Dr91qmYpAfkyjc9gUScAsE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "a1fea1e7-23e0-4f5e-93c2-4881aeadd42c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GmXzaPk5xXku3zcbYGLGcA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3090,
      "cache_read_input_tokens": 30998,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3090
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

_source line 37 · 2026-05-15T01:40:34.600Z_

<details><summary>↩ Tool result · `toolu_01Dr91qmYpAfkyjc9gUScAsE`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Long-context language models place acute pressure on the key--value (KV) cache, which grows linearly with sequence length \cite{kwon-sosp2023, pope-mlsys2023}.
5	Two complementary responses---\emph{attention head pruning} \cite{voita-acl2019, michel-neurips2019} and \emph{KV cache eviction} \cite{snapkv-neurips2024, adakv-neurips2025}---can be deployed simultaneously as \emph{compound sparsity}, but the resulting quality degradation is often super-additive \cite{spark-aaai2026, slim-icml2025}. Recent evaluations confirm that reasoning capabilities degrade disproportionately under compound compression \cite{unicomp-2026}, and that per-dimension safe zones intersect to form a smaller joint safe region \cite{phase-transition-compression-2026}.
6	
7	Prior work treats compound interaction magnitude as roughly constant across generation \cite{spark-aaai2026, unicomp-2026}, despite evidence that pruning sensitivity depends on representational phase \cite{decision-repr-transition-2026} and that no single sparse attention strategy dominates across generation stages \cite{sparse-frontier-2025}.
8	This assumption is problematic for reasoning models, whose generations alternate between broadly distributed attention (exploratory reasoning) and sharply concentrated attention (structured computation) \cite{thinkv-iclr2026}.
9	Phase-aware methods like ThinKV \cite{thinkv-iclr2026} apply different KV strategies per phase but without considering compound interaction, while importance-based eviction itself faces challenges from greedy bias \cite{greedy-bias-kvcache-2026}, deferred importance \cite{retentivekv-2026}, and temporal dynamics in long generations \cite{lethe-aaai2026}. These methods each optimize a single pruning axis; we characterize the interaction when multiple mechanisms are composed.
10	If compound severity varies across these phases, a uniform sparsity budget may be safe in one phase yet destructive in another.
11	
12	We show that compound sparsity severity is strongly modulated by reasoning phase and eviction strategy.
13	Under importance-based KV cache eviction, the Interaction Index---a measure of super-additive degradation---concentrates in low-sparsity phases and is largely absent in high-sparsity phases.
14	On DeepSeek-R1-Distill-Qwen-7B, the median phase difference rises from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$ ($d_z$: $0.44 \to 0.80$; Bonferroni-corrected $p < 0.005$ at all levels).
15	The pattern replicates at $s \geq 0.20$ on Qwen2.5-7B-Instruct ($d_z \geq 0.55$) and partially extends to a distinct architecture (DeepSeek-R1-Distill-Llama-8B, LlamaForCausalLM) with a qualitatively consistent but substantially weaker trend at $\sim$1/40 the magnitude.
16	Critically, random eviction produces no such gradient (7/8 conditions non-significant), confirming the gradient is an emergent phase-strategy interaction.
17	
18	We propose \emph{entropy-discrimination collapse} as a mechanism: head pruning flattens cumulative importance scores in phases where attention is broadly distributed, degrading the discriminative power of importance-based eviction in a phase-dependent manner.
19	Random eviction is immune because its decisions are independent of attention patterns.
20	Our contributions:
21	\begin{enumerate}[nosep,leftmargin=*]
22	    \item We identify a \textbf{phase--strategy interaction}: importance-based eviction exhibits a severity gradient across reasoning phases that is absent under random eviction (\S\ref{sec:results}).
23	    \item We show this gradient \textbf{increases monotonically with sparsity} and replicates across three models spanning two architectures (\S\ref{sec:results}).
24	    \item We propose \textbf{entropy-discrimination collapse} as a mechanistic explanation (\S\ref{sec:analysis}).
25	\end{enumerate}
26	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "24d765ae-6c54-488b-ac29-f4a06dc29a50",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nLong-context language models place acute pressure on the key--value (KV) cache, which grows linearly with sequence length \\cite{kwon-sosp2023, pope-mlsys2023}.\nTwo complementary responses---\\emph{attention head pruning} \\cite{voita-acl2019, michel-neurips2019} and \\emph{KV cache eviction} \\cite{snapkv-neurips2024, adakv-neurips2025}---can be deployed simultaneously as \\emph{compound sparsity}, but the resulting quality degradation is often super-additive \\cite{spark-aaai2026, slim-icml2025}. Recent evaluations confirm that reasoning capabilities degrade disproportionately under compound compression \\cite{unicomp-2026}, and that per-dimension safe zones intersect to form a smaller joint safe region \\cite{phase-transition-compression-2026}.\n\nPrior work treats compound interaction magnitude as roughly constant across generation \\cite{spark-aaai2026, unicomp-2026}, despite evidence that pruning sensitivity depends on representational phase \\cite{decision-repr-transition-2026} and that no single sparse attention strategy dominates across generation stages \\cite{sparse-frontier-2025}.\nThis assumption is problematic for reasoning models, whose generations alternate between broadly distributed attention (exploratory reasoning) and sharply concentrated attention (structured computation) \\cite{thinkv-iclr2026}.\nPhase-aware methods like ThinKV \\cite{thinkv-iclr2026} apply different KV strategies per phase but without considering compound interaction, while importance-based eviction itself faces challenges from greedy bias \\cite{greedy-bias-kvcache-2026}, deferred importance \\cite{retentivekv-2026}, and temporal dynamics in long generations \\cite{lethe-aaai2026}. These methods each optimize a single pruning axis; we characterize the interaction when multiple mechanisms are composed.\nIf compound severity varies across these phases, a uniform sparsity budget may be safe in one phase yet destructive in another.\n\nWe show that compound sparsity severity is strongly modulated by reasoning phase and eviction strategy.\nUnder importance-based KV cache eviction, the Interaction Index---a measure of super-additive degradation---concentrates in low-sparsity phases and is largely absent in high-sparsity phases.\nOn DeepSeek-R1-Distill-Qwen-7B, the median phase difference rises from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$ ($d_z$: $0.44 \\to 0.80$; Bonferroni-corrected $p < 0.005$ at all levels).\nThe pattern replicates at $s \\geq 0.20$ on Qwen2.5-7B-Instruct ($d_z \\geq 0.55$) and partially extends to a distinct architecture (DeepSeek-R1-Distill-Llama-8B, LlamaForCausalLM) with a qualitatively consistent but substantially weaker trend at $\\sim$1/40 the magnitude.\nCritically, random eviction produces no such gradient (7/8 conditions non-significant), confirming the gradient is an emergent phase-strategy interaction.\n\nWe propose \\emph{entropy-discrimination collapse} as a mechanism: head pruning flattens cumulative importance scores in phases where attention is broadly distributed, degrading the discriminative power of importance-based eviction in a phase-dependent manner.\nRandom eviction is immune because its decisions are independent of attention patterns.\nOur contributions:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item We identify a \\textbf{phase--strategy interaction}: importance-based eviction exhibits a severity gradient across reasoning phases that is absent under random eviction (\\S\\ref{sec:results}).\n    \\item We show this gradient \\textbf{increases monotonically with sparsity} and replicates across three models spanning two architectures (\\S\\ref{sec:results}).\n    \\item We propose \\textbf{entropy-discrimination collapse} as a mechanistic explanation (\\S\\ref{sec:analysis}).\n\\end{enumerate}\n",
      "numLines": 26,
      "startLine": 1,
      "totalLines": 26
    }
  }
}
```

</details>

---

### Tool call

_source line 38_

<details open><summary>🔧 Tool call — Read · `toolu_0166aoRa8Vd16pVaBYdzvxCw`</summary>

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
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "560f9d1f-65bf-436a-9bf1-e9afee66cba5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GmXzaPk5xXku3zcbYGLGcA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3090,
      "cache_read_input_tokens": 30998,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3090
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

_source line 39 · 2026-05-15T01:40:34.752Z_

<details><summary>↩ Tool result · `toolu_0166aoRa8Vd16pVaBYdzvxCw`</summary>

```text
1	\section{Experimental Setup}
2	\label{sec:experimental-setup}
3	
4	\paragraph{Models.}
5	\label{sec:models}
6	We evaluate on two 7B-parameter models sharing the Qwen2 backbone (28 layers, 28 heads, 4-group GQA): \textbf{DeepSeek-R1-Distill-Qwen-7B}~\cite{deepseek-r1-2025}, distilled from DeepSeek-R1 with explicit chain-of-thought traces yielding pronounced phase structure; and \textbf{Qwen2.5-7B-Instruct}~\cite{qwen25-2024}, with standard instruction tuning, providing a cross-model replication target. Both are loaded in \texttt{bfloat16} with eager attention.\footnote{An earlier \texttt{float16} configuration produced sporadic NaN values; \texttt{bfloat16} eliminated all occurrences.}
7	
8	\paragraph{Dataset.}
9	\label{sec:dataset}
10	We use 50 problems stratified from MATH-500~\cite{math500-neurips2021}, sampling uniformly across categories with a fixed seed. Each problem is decoded greedily (\texttt{max\_new\_tokens}$=$2048).
11	
12	\paragraph{Sparsity configuration.}
13	\label{sec:sparsity-config}
14	We apply symmetric compound sparsity at $s \in \{0.15, 0.20, 0.25, 0.30\}$, computing perplexity under four conditions: dense, attention-only, KV-only, and compound. We compare \emph{importance-based} eviction (position-normalized cumulative attention score, Eq.~\ref{eq:kv-importance}; BOS always retained) and \emph{random} eviction (uniform). Heads are pruned per layer by Frobenius norm; under random eviction, both heads and positions are selected uniformly.
15	
16	\paragraph{Phase segmentation and metrics.}
17	\label{sec:phase-seg}
18	Each sequence is segmented into three phases using the quantile-based method (\S\ref{sec:phase-segmentation}), with $\texttt{min\_phase\_length}{=}10$. We compute segment-level perplexity, II (Eq.~\ref{eq:ii}), and $G$ (Eq.~\ref{eq:gradient}), reporting medians due to heavy right-skew (mean/median ratios up to 43:1).
19	
20	\paragraph{Statistical analysis.}
21	\label{sec:stats}
22	All reported confidence intervals and significance tests use nonparametric bootstrap ($B{=}10{,}000$)~\cite{efron-1993}; initial profiling uses $B{=}1{,}000$ for computational efficiency, with all reported statistics recomputed at $B{=}10{,}000$. Paired bootstrap controls for problem-level variance. All tests yield $p_{\text{Bonf}} < 0.005$ at every sparsity level.\footnote{Experiments on 4$\times$ NVIDIA RTX PRO 6000 Blackwell 96\,GB GPUs.}
23	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "781973e3-0991-49c0-8024-b46f2fe8d9ec",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex",
      "content": "\\section{Experimental Setup}\n\\label{sec:experimental-setup}\n\n\\paragraph{Models.}\n\\label{sec:models}\nWe evaluate on two 7B-parameter models sharing the Qwen2 backbone (28 layers, 28 heads, 4-group GQA): \\textbf{DeepSeek-R1-Distill-Qwen-7B}~\\cite{deepseek-r1-2025}, distilled from DeepSeek-R1 with explicit chain-of-thought traces yielding pronounced phase structure; and \\textbf{Qwen2.5-7B-Instruct}~\\cite{qwen25-2024}, with standard instruction tuning, providing a cross-model replication target. Both are loaded in \\texttt{bfloat16} with eager attention.\\footnote{An earlier \\texttt{float16} configuration produced sporadic NaN values; \\texttt{bfloat16} eliminated all occurrences.}\n\n\\paragraph{Dataset.}\n\\label{sec:dataset}\nWe use 50 problems stratified from MATH-500~\\cite{math500-neurips2021}, sampling uniformly across categories with a fixed seed. Each problem is decoded greedily (\\texttt{max\\_new\\_tokens}$=$2048).\n\n\\paragraph{Sparsity configuration.}\n\\label{sec:sparsity-config}\nWe apply symmetric compound sparsity at $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$, computing perplexity under four conditions: dense, attention-only, KV-only, and compound. We compare \\emph{importance-based} eviction (position-normalized cumulative attention score, Eq.~\\ref{eq:kv-importance}; BOS always retained) and \\emph{random} eviction (uniform). Heads are pruned per layer by Frobenius norm; under random eviction, both heads and positions are selected uniformly.\n\n\\paragraph{Phase segmentation and metrics.}\n\\label{sec:phase-seg}\nEach sequence is segmented into three phases using the quantile-based method (\\S\\ref{sec:phase-segmentation}), with $\\texttt{min\\_phase\\_length}{=}10$. We compute segment-level perplexity, II (Eq.~\\ref{eq:ii}), and $G$ (Eq.~\\ref{eq:gradient}), reporting medians due to heavy right-skew (mean/median ratios up to 43:1).\n\n\\paragraph{Statistical analysis.}\n\\label{sec:stats}\nAll reported confidence intervals and significance tests use nonparametric bootstrap ($B{=}10{,}000$)~\\cite{efron-1993}; initial profiling uses $B{=}1{,}000$ for computational efficiency, with all reported statistics recomputed at $B{=}10{,}000$. Paired bootstrap controls for problem-level variance. All tests yield $p_{\\text{Bonf}} < 0.005$ at every sparsity level.\\footnote{Experiments on 4$\\times$ NVIDIA RTX PRO 6000 Blackwell 96\\,GB GPUs.}\n",
      "numLines": 23,
      "startLine": 1,
      "totalLines": 23
    }
  }
}
```

</details>

---

### Assistant

_source line 40_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the remaining files: conclusion, limitations, appendices, and the Qwen-specific sections.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "9c74a221-388b-45b8-ad90-86b939e2dd60",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JQN68tPnituvj3EfYDfmKY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9273,
      "cache_read_input_tokens": 34088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9273
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

Now reading the remaining files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "73b7a53b-03e5-442f-b15b-58908068ec00",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JQN68tPnituvj3EfYDfmKY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9273,
      "cache_read_input_tokens": 34088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9273
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

<details open><summary>🔧 Tool call — Read · `toolu_01MtKKgLVGUoirU9Hs1JPnV4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "131c4c32-c2b8-4b0c-be25-59787d4d7235",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JQN68tPnituvj3EfYDfmKY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9273,
      "cache_read_input_tokens": 34088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9273
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

_source line 43 · 2026-05-15T01:40:40.412Z_

<details><summary>↩ Tool result · `toolu_01MtKKgLVGUoirU9Hs1JPnV4`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We showed that compound sparsity severity---the super-additive interaction between head pruning and KV cache eviction---is not phase-invariant but exhibits an emergent phase-strategy interaction spanning over an order of magnitude within a single generation. Under importance-based eviction, the severity gradient grows from $69{\times}$ to $274{\times}$ across sparsity levels ($d_z$: $0.44 \to 0.80$); random eviction shows no such modulation (7/8 conditions non-significant). A crossover at $s{=}0.25$---where importance-based eviction reverses ranking across phases---demonstrates that no single strategy dominates uniformly. The pattern replicates on Qwen2.5-7B-Instruct at $s \geq 0.20$ ($d_z \geq 0.55$) and partially extends cross-architecture to DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM) with a qualitatively consistent but substantially weaker trend at $\sim$1/40 the magnitude. Discrimination collapse provides a mechanistic explanation supported by both Qwen2-based models; LLaMA results are directionally consistent but the interaction is weaker than in Qwen2 architectures.
5	These findings motivate phase-aware sparsity allocation for reasoning model deployment.
6	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "a1ad111d-2f13-46e4-a18a-44fb77b50cb1",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex",
      "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe showed that compound sparsity severity---the super-additive interaction between head pruning and KV cache eviction---is not phase-invariant but exhibits an emergent phase-strategy interaction spanning over an order of magnitude within a single generation. Under importance-based eviction, the severity gradient grows from $69{\\times}$ to $274{\\times}$ across sparsity levels ($d_z$: $0.44 \\to 0.80$); random eviction shows no such modulation (7/8 conditions non-significant). A crossover at $s{=}0.25$---where importance-based eviction reverses ranking across phases---demonstrates that no single strategy dominates uniformly. The pattern replicates on Qwen2.5-7B-Instruct at $s \\geq 0.20$ ($d_z \\geq 0.55$) and partially extends cross-architecture to DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM) with a qualitatively consistent but substantially weaker trend at $\\sim$1/40 the magnitude. Discrimination collapse provides a mechanistic explanation supported by both Qwen2-based models; LLaMA results are directionally consistent but the interaction is weaker than in Qwen2 architectures.\nThese findings motivate phase-aware sparsity allocation for reasoning model deployment.\n",
      "numLines": 6,
      "startLine": 1,
      "totalLines": 6
    }
  }
}
```

</details>

---

### Tool call

_source line 44_

<details open><summary>🔧 Tool call — Read · `toolu_01AEQyuTWfYrXPDnTFx8aAip`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "1f7e3321-c091-4280-ac4e-52c9ce7e049a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JQN68tPnituvj3EfYDfmKY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9273,
      "cache_read_input_tokens": 34088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9273
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

_source line 45 · 2026-05-15T01:40:40.927Z_

<details><summary>↩ Tool result · `toolu_01AEQyuTWfYrXPDnTFx8aAip`</summary>

```text
1	\paragraph{Model scale and architecture.}
2	All experiments are conducted at the 7--8B parameter scale. Whether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested. Preliminary cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \S\ref{sec:cross-arch}) partially confirms the qualitative pattern beyond the Qwen2 architecture---monotonically increasing $d_z$ with within-importance phase gradient $\sim$1.0---but with substantially weaker interaction magnitude ($\sim$1/40 of DeepSeek) and mixed statistical evidence (only $s{=}0.30$ significant after Bonferroni correction). The pattern has been tested on two architecture families (Qwen2ForCausalLM, LlamaForCausalLM); comprehensive validation across more diverse architectures (e.g., Mistral, multi-latent attention) and larger scales is needed for full generalization claims.
3	
4	\paragraph{Task coverage.}
5	We evaluate exclusively on MATH-500, a mathematical reasoning benchmark. Different reasoning tasks---code generation, commonsense reasoning, multi-hop question answering---may induce different phase structures with different sparsity distributions, potentially altering the severity gradient profile.
6	
7	\paragraph{Mechanism.}
8	The discrimination collapse mechanism is supported by correlational evidence (consistent Gini/CV reduction across all conditions); causal validation through controlled entropy manipulation is needed. The entropy redistribution component replicates on only 2/4 Qwen conditions, suggesting model-specific factors.
9	
10	\paragraph{Sparsity range.}
11	Our experiments span $s \in \{0.15, 0.20, 0.25, 0.30\}$. More extreme sparsity ($s > 0.50$) may exhibit qualitatively different interaction dynamics. We do not report inference throughput or latency measurements, which are necessary for a complete deployment analysis but orthogonal to our severity characterization. Extended limitations in Appendix~\ref{app:limitations}.
12	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "ca30faf2-5d89-4704-9b71-a776f23d4dd1",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/limitations.tex",
      "content": "\\paragraph{Model scale and architecture.}\nAll experiments are conducted at the 7--8B parameter scale. Whether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested. Preliminary cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \\S\\ref{sec:cross-arch}) partially confirms the qualitative pattern beyond the Qwen2 architecture---monotonically increasing $d_z$ with within-importance phase gradient $\\sim$1.0---but with substantially weaker interaction magnitude ($\\sim$1/40 of DeepSeek) and mixed statistical evidence (only $s{=}0.30$ significant after Bonferroni correction). The pattern has been tested on two architecture families (Qwen2ForCausalLM, LlamaForCausalLM); comprehensive validation across more diverse architectures (e.g., Mistral, multi-latent attention) and larger scales is needed for full generalization claims.\n\n\\paragraph{Task coverage.}\nWe evaluate exclusively on MATH-500, a mathematical reasoning benchmark. Different reasoning tasks---code generation, commonsense reasoning, multi-hop question answering---may induce different phase structures with different sparsity distributions, potentially altering the severity gradient profile.\n\n\\paragraph{Mechanism.}\nThe discrimination collapse mechanism is supported by correlational evidence (consistent Gini/CV reduction across all conditions); causal validation through controlled entropy manipulation is needed. The entropy redistribution component replicates on only 2/4 Qwen conditions, suggesting model-specific factors.\n\n\\paragraph{Sparsity range.}\nOur experiments span $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$. More extreme sparsity ($s > 0.50$) may exhibit qualitatively different interaction dynamics. We do not report inference throughput or latency measurements, which are necessary for a complete deployment analysis but orthogonal to our severity characterization. Extended limitations in Appendix~\\ref{app:limitations}.\n",
      "numLines": 12,
      "startLine": 1,
      "totalLines": 12
    }
  }
}
```

</details>

---

### Tool call

_source line 46_

<details open><summary>🔧 Tool call — Read · `toolu_01RyAV8DsLhxUmcCXNr7fD8T`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "9c07717f-73cb-4974-a45e-00f1ff4da020",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JQN68tPnituvj3EfYDfmKY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9273,
      "cache_read_input_tokens": 34088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9273
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

_source line 47 · 2026-05-15T01:40:41.395Z_

<details><summary>↩ Tool result · `toolu_01RyAV8DsLhxUmcCXNr7fD8T`</summary>

```text
1	\section{Compound Sparsity Formulation}
2	\label{app:formulation-details}
3	
4	\paragraph{Attention head pruning.}
5	Heads are ranked by Frobenius norm importance $w_j^{(\ell)} = \|\mathbf{A}_j^{(\ell)}\|_F$ \cite{voita-acl2019, michel-neurips2019}; a binary mask $m_j^{(\ell)} \in \{0,1\}$ retains the top-$(1{-}s)\cdot H$ heads:
6	\begin{equation}
7	    \tilde{\mathbf{o}}_j^{(\ell)} = m_j^{(\ell)} \cdot \mathbf{o}_j^{(\ell)}.
8	    \label{eq:head-mask}
9	\end{equation}
10	
11	\paragraph{KV cache eviction.}
12	A position mask $\mathbf{m}_k \in \{0,1\}^T$ retains the top-$(1{-}s)\cdot T$ positions (BOS always preserved):
13	\begin{equation}
14	    \tilde{a}_{ij} = a_{ij} \cdot m_{k,j}, \quad \forall\, i, j.
15	    \label{eq:kv-mask}
16	\end{equation}
17	Under importance-based eviction, each position $j$ is scored by its cumulative attention mass with position normalization:
18	\begin{equation}
19	    \mathrm{imp}(j) = \frac{\sum_{\ell, h, i} a_{ij}^{(\ell,h)}}{T - j},
20	    \label{eq:kv-importance}
21	\end{equation}
22	where the denominator compensates for causal bias---earlier positions are attended to by more queries \cite{thinkv-iclr2026, defensivekv-iclr2026}. Under random eviction, positions (excluding BOS) are evicted uniformly at random.
23	
24	\paragraph{Compound sparsity.}
25	Applying both mechanisms simultaneously yields compound sparsity. The two axes interact: head pruning redistributes attention mass, altering the importance ranking for KV eviction. Prior work \cite{spark-aaai2026} reports super-additive joint effects but treats interaction magnitude as a fixed property of $s$.
26	
27	\paragraph{Attention sparsity metric.}
28	For each query position $i$ and head $h$, we compute the fraction of key positions receiving negligible attention:
29	\begin{equation}
30	    \sigma_i^{(h)} = \frac{1}{T} \sum_{j=1}^{T} \mathbf{1}\!\left[a_{ij}^{(h)} < 0.01 \cdot \max_k a_{ik}^{(h)}\right].
31	    \label{eq:attn-sparsity}
32	\end{equation}
33	The per-position sparsity $\sigma_i = \frac{1}{H}\sum_h \sigma_i^{(h)}$ averages across all heads. Tokens are partitioned into high-, mid-, and low-sparsity phases by the tercile boundaries of $\{\sigma_i\}$; segments shorter than 10 tokens are merged into adjacent phases.
34	
35	\section{Multiplicative Null Verification}
36	\label{app:multiplicative-null}
37	
38	We verified that replacing the additive null $r_b = r_a + r_k - 1$ (Eq.~\ref{eq:ii}) with the multiplicative null $r_b = r_a \cdot r_k$ does not change qualitative conclusions. Under the multiplicative formulation, the interaction index becomes $\mathrm{II}_{\times} = r_b - r_a \cdot r_k$. Across all sparsity levels and both eviction strategies, the sign and relative ordering of $\mathrm{II}_{\times}$ match those of the additive II: importance-based eviction exhibits a monotonically increasing severity gradient ($G_{\times} = 58$--$241{\times}$), while random eviction remains flat ($G_{\times} \approx 1$). The crossover at $s{=}0.25$ is preserved. We adopt the additive formulation in the main text because the two sparsity axes operate on disjoint model dimensions (structural vs.\ positional), making additive independence the more natural null hypothesis at the sparsity levels studied.
39	
40	% Bootstrap and permutation details moved to main text \S\ref{sec:stat-validation}
41	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "aa59d69c-f520-4c41-97f5-73835135526e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex",
      "content": "\\section{Compound Sparsity Formulation}\n\\label{app:formulation-details}\n\n\\paragraph{Attention head pruning.}\nHeads are ranked by Frobenius norm importance $w_j^{(\\ell)} = \\|\\mathbf{A}_j^{(\\ell)}\\|_F$ \\cite{voita-acl2019, michel-neurips2019}; a binary mask $m_j^{(\\ell)} \\in \\{0,1\\}$ retains the top-$(1{-}s)\\cdot H$ heads:\n\\begin{equation}\n    \\tilde{\\mathbf{o}}_j^{(\\ell)} = m_j^{(\\ell)} \\cdot \\mathbf{o}_j^{(\\ell)}.\n    \\label{eq:head-mask}\n\\end{equation}\n\n\\paragraph{KV cache eviction.}\nA position mask $\\mathbf{m}_k \\in \\{0,1\\}^T$ retains the top-$(1{-}s)\\cdot T$ positions (BOS always preserved):\n\\begin{equation}\n    \\tilde{a}_{ij} = a_{ij} \\cdot m_{k,j}, \\quad \\forall\\, i, j.\n    \\label{eq:kv-mask}\n\\end{equation}\nUnder importance-based eviction, each position $j$ is scored by its cumulative attention mass with position normalization:\n\\begin{equation}\n    \\mathrm{imp}(j) = \\frac{\\sum_{\\ell, h, i} a_{ij}^{(\\ell,h)}}{T - j},\n    \\label{eq:kv-importance}\n\\end{equation}\nwhere the denominator compensates for causal bias---earlier positions are attended to by more queries \\cite{thinkv-iclr2026, defensivekv-iclr2026}. Under random eviction, positions (excluding BOS) are evicted uniformly at random.\n\n\\paragraph{Compound sparsity.}\nApplying both mechanisms simultaneously yields compound sparsity. The two axes interact: head pruning redistributes attention mass, altering the importance ranking for KV eviction. Prior work \\cite{spark-aaai2026} reports super-additive joint effects but treats interaction magnitude as a fixed property of $s$.\n\n\\paragraph{Attention sparsity metric.}\nFor each query position $i$ and head $h$, we compute the fraction of key positions receiving negligible attention:\n\\begin{equation}\n    \\sigma_i^{(h)} = \\frac{1}{T} \\sum_{j=1}^{T} \\mathbf{1}\\!\\left[a_{ij}^{(h)} < 0.01 \\cdot \\max_k a_{ik}^{(h)}\\right].\n    \\label{eq:attn-sparsity}\n\\end{equation}\nThe per-position sparsity $\\sigma_i = \\frac{1}{H}\\sum_h \\sigma_i^{(h)}$ averages across all heads. Tokens are partitioned into high-, mid-, and low-sparsity phases by the tercile boundaries of $\\{\\sigma_i\\}$; segments shorter than 10 tokens are merged into adjacent phases.\n\n\\section{Multiplicative Null Verification}\n\\label{app:multiplicative-null}\n\nWe verified that replacing the additive null $r_b = r_a + r_k - 1$ (Eq.~\\ref{eq:ii}) with the multiplicative null $r_b = r_a \\cdot r_k$ does not change qualitative conclusions. Under the multiplicative formulation, the interaction index becomes $\\mathrm{II}_{\\times} = r_b - r_a \\cdot r_k$. Across all sparsity levels and both eviction strategies, the sign and relative ordering of $\\mathrm{II}_{\\times}$ match those of the additive II: importance-based eviction exhibits a monotonically increasing severity gradient ($G_{\\times} = 58$--$241{\\times}$), while random eviction remains flat ($G_{\\times} \\approx 1$). The crossover at $s{=}0.25$ is preserved. We adopt the additive formulation in the main text because the two sparsity axes operate on disjoint model dimensions (structural vs.\\ positional), making additive independence the more natural null hypothesis at the sparsity levels studied.\n\n% Bootstrap and permutation details moved to main text \\S\\ref{sec:stat-validation}\n",
      "numLines": 41,
      "startLine": 1,
      "totalLines": 41
    }
  }
}
```

</details>

---

### Tool call

_source line 48_

<details open><summary>🔧 Tool call — Read · `toolu_014kVaD27rJprzsAfxGWmwv6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "52473580-6cc8-4b3f-8a67-419ef577021c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JQN68tPnituvj3EfYDfmKY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9273,
      "cache_read_input_tokens": 34088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9273
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

_source line 49 · 2026-05-15T01:40:42.353Z_

<details><summary>↩ Tool result · `toolu_014kVaD27rJprzsAfxGWmwv6`</summary>

```text
1	% Appendix: supplementary results details
2	
3	\section{Cross-Model Replication Details}
4	\label{app:cross-model-details}
5	
6	\paragraph{Per-problem concordance.}
7	The per-problem concordance across models is not significant (median $\rho = \placeholder{}$, $p = \placeholder{}$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking. % exp_id: cross_model_analysis.json (spearman_rho=1.0, gradient_permutation_p=0.043, per_problem_concordance_p=0.926, mean_rho=-0.107)
8	
9	\paragraph{Random eviction control.}
10	As a control, random eviction on Qwen yields no systematic phase gradient at three of four sparsity levels (3/4 FAIL), mirroring DeepSeek's 4/4 FAIL pattern. At $s{=}0.30$, Qwen random produces a borderline PASS (permutation $p = 0.012$) but with negligible median difference ($\widetilde{\Delta} = \placeholder{}$, CI spans zero), indicating no meaningful phase modulation. % exp_id: bf16_qw_rand_s015..s030; source: experiment_summary_table.json
11	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "eb982313-784f-4b9a-878b-60bbef58c04a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_results.tex",
      "content": "% Appendix: supplementary results details\n\n\\section{Cross-Model Replication Details}\n\\label{app:cross-model-details}\n\n\\paragraph{Per-problem concordance.}\nThe per-problem concordance across models is not significant (median $\\rho = \\placeholder{}$, $p = \\placeholder{}$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking. % exp_id: cross_model_analysis.json (spearman_rho=1.0, gradient_permutation_p=0.043, per_problem_concordance_p=0.926, mean_rho=-0.107)\n\n\\paragraph{Random eviction control.}\nAs a control, random eviction on Qwen yields no systematic phase gradient at three of four sparsity levels (3/4 FAIL), mirroring DeepSeek's 4/4 FAIL pattern. At $s{=}0.30$, Qwen random produces a borderline PASS (permutation $p = 0.012$) but with negligible median difference ($\\widetilde{\\Delta} = \\placeholder{}$, CI spans zero), indicating no meaningful phase modulation. % exp_id: bf16_qw_rand_s015..s030; source: experiment_summary_table.json\n",
      "numLines": 11,
      "startLine": 1,
      "totalLines": 11
    }
  }
}
```

</details>

---

### Tool call

_source line 50_

<details open><summary>🔧 Tool call — Read · `toolu_01MpfaNPy1xAjFQc8gtLYDD7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "49b45c74-f99e-44b5-b310-98e6f14a1317",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JQN68tPnituvj3EfYDfmKY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9273,
      "cache_read_input_tokens": 34088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9273
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

_source line 51 · 2026-05-15T01:40:42.926Z_

<details><summary>↩ Tool result · `toolu_01MpfaNPy1xAjFQc8gtLYDD7`</summary>

```text
1	% Content moved from main body to appendix:
2	% - Phase-strategy crossover details (from results §5.3)
3	% - Cross-model replication details with tables/figures (from results §5.4)
4	% - Permutation test details with table/forest plot (from results §5.5)
5	% - Full entropy-discrimination collapse analysis with tables (from analysis §6)
6	% Main body §6 (analysis.tex) contains a condensed summary referencing these tables.
7	
8	\section{Phase-Strategy Crossover Details}
9	\label{app:crossover-details}
10	
11	At $s{=}0.25$, a strategy ranking reversal emerges (Figure~\ref{fig:crossover}): importance-based eviction yields \emph{lower} II than random in the high-sparsity phase ($0.032$ vs.\ $0.818$) but \emph{higher} II in the low-sparsity phase ($7.196$ vs.\ $1.363$---a $5.3{\times}$ reversal). This crossover is present at all four sparsity levels, with reversal magnitude of $3.9{\times}$ at $s{=}0.15$, $5.4{\times}$ at $s{=}0.20$, $5.3{\times}$ at $s{=}0.25$, and $3.6{\times}$ at $s{=}0.30$ (as random eviction severity also rises). The reversal arises because head pruning redistributes attention mass, altering importance rankings in a way that couples the two sparsity mechanisms in low-sparsity phases (\S\ref{sec:discrimination-collapse}). % exp_id: bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json; 7.196/1.363=5.28
12	
13	\begin{figure}[t]
14	\centering
15	\includegraphics[width=\columnwidth]{fig3_crossover.pdf}
16	\caption{Strategy-dependent crossover at $s{=}0.25$. Grouped bar chart of median II by eviction strategy and reasoning phase. Importance-based eviction outperforms random in the high-sparsity phase but produces $5.3{\times}$ higher II in the low-sparsity phase, reversing the strategy ranking.}
17	\label{fig:crossover}
18	\end{figure}
19	
20	
21	\section{Cross-Model Replication Details}
22	\label{app:cross-model-details}
23	
24	Both models share the Qwen2ForCausalLM backbone (28 layers, 28 heads, 4-group GQA) but differ in training: DeepSeek uses reasoning distillation from DeepSeek-R1, while Qwen2.5 uses standard instruction tuning without explicit reasoning delimiters. This controlled comparison isolates the effect of training methodology on the compound sparsity interaction.
25	
26	Despite lacking explicit \texttt{&lt;think>} delimiters, Qwen2.5-7B-Instruct exhibits sufficient variation in attention sparsity to permit phase segmentation via the same quantile-based method (\S\ref{sec:phase-segmentation}). Four of the 50 problems are excluded due to degenerate phase assignments, yielding $n{=}46$ valid problems for Qwen (vs.\ $n{=}49$ for DeepSeek).
27	
28	\paragraph{Per-phase effective sample size.}
29	\label{app:qwen-null-rate}
30	Table~\ref{tab:qwen-effective-n} reports the per-phase effective sample size for Qwen2.5-7B-Instruct, defined as the number of problems with $|\mathrm{II}| > 0.001$ in each phase. The mid-phase null rate (\placeholder{NULL\_PCT}\%) reflects problems where compound interaction is absent in intermediate phases; this does not affect the low--high contrast ($\Delta$) used in the primary analysis.
31	
32	\begin{table}[t]
33	\centering
34	\small
35	\caption{Per-phase effective sample size for Qwen2.5-7B-Instruct ($n_{\text{total}} = \placeholder{N\_QW}$).}
36	\label{tab:qwen-effective-n}
37	\begin{tabular}{@{}lcccc@{}}
38	\toprule
39	Phase & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
40	\midrule
41	High & \placeholder{} & \placeholder{} & \placeholder{} & \placeholder{} \\
42	Mid  & \placeholder{} & \placeholder{} & \placeholder{} & \placeholder{} \\
43	Low  & \placeholder{} & \placeholder{} & \placeholder{} & \placeholder{} \\
44	\bottomrule
45	\end{tabular}
46	\end{table}
47	
48	Table~\ref{tab:cross-model} reports the cross-model comparison. Qwen reproduces the monotonic severity gradient at ${\sim}1/5$ of DeepSeek's magnitude. Figure~\ref{fig:cross-model} visualizes this comparison. % exp_id: cross_model_analysis.json; cohens_d_bf16_qwen.json
49	
50	\begin{table}[t]
51	\centering
52	\small
53	\caption{Cross-model comparison of median compound severity difference ($\Delta$) under importance-based eviction.}
54	\label{tab:cross-model}
55	\begin{tabular}{@{}lcccc@{}}
56	\toprule
57	Model & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
58	\midrule
59	DeepSeek-R1-Distill-Qwen-7B & 0.39 & 1.48 & 7.16 & 14.59 \\ % exp_id: bf16_importance_s015..s030
60	Qwen2.5-7B-Instruct         & 0.04 & 0.23 & 1.27 & 2.94 \\ % exp_id: bf16_qw_imp_s015..s030
61	\bottomrule
62	\end{tabular}
63	\end{table}
64	
65	\begin{figure}[t]
66	\centering
67	\includegraphics[width=\columnwidth]{fig5_crossmodel.pdf}
68	\caption{Cross-model comparison of the median severity difference under importance-based eviction. Both DeepSeek (solid) and Qwen (dashed) exhibit monotonically increasing $\Delta$ with sparsity; Qwen's magnitude is approximately one-fifth of DeepSeek's.} % exp_id: bf16_importance_s015..s030, bf16_qw_imp_s015..s030
69	\label{fig:cross-model}
70	\end{figure}
71	
72	\paragraph{Per-problem concordance.}
73	The per-problem concordance across models is not significant (median $\rho = \placeholder{}$, $p = \placeholder{}$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking. % exp_id: cross_model_analysis.json (spearman_rho=1.0, gradient_permutation_p=0.043, per_problem_concordance_p=0.926, mean_rho=-0.107)
74	
75	\paragraph{Random eviction control.}
76	As a control, random eviction on Qwen yields no systematic phase gradient at three of four sparsity levels (3/4 FAIL), mirroring DeepSeek's 4/4 FAIL pattern. At $s{=}0.30$, Qwen random produces a borderline PASS (permutation $p = 0.012$) but with negligible median difference ($\widetilde{\Delta} = \placeholder{}$, CI spans zero), indicating no meaningful phase modulation. % exp_id: bf16_qw_rand_s015..s030; source: experiment_summary_table.json
77	
78	
79	\section{Permutation Test Details}
80	\label{app:permutation-details}
81	
82	For each problem $i$ and sparsity level $s$, we compute the compound severity difference $\Delta_i^{(\text{strat})} = \mathrm{II}_{\textit{low},i} - \mathrm{II}_{\textit{high},i}$ under each eviction strategy. The test statistic is the median of the paired difference $\widetilde{\Delta} = \text{median}_i\!\bigl(\Delta_i^{(\text{imp})} - \Delta_i^{(\text{rand})}\bigr)$, measuring whether importance-based eviction produces systematically larger phase-dependent severity than random eviction. We permute strategy labels $10{,}000$ times to construct the null distribution and apply Bonferroni correction for 4 sparsity-level comparisons.
83	
84	Per-problem distributions of the paired severity difference $\Delta_i = \mathrm{II}_{\textit{low},i} - \mathrm{II}_{\textit{high},i}$ under importance-based eviction are right-skewed at all sparsity levels, with mean/median ratios ranging from $1.2{\times}$ ($s{=}0.15$) to $1.6{\times}$ ($s{=}0.30$) for DeepSeek and $1.1{\times}$ to $1.4{\times}$ for Qwen.
85	
86	The permutation null distributions are approximately symmetric around zero at all sparsity levels. At $s{=}0.15$, the observed statistic falls at the $99.92$th percentile of the null ($p_{\text{Bonf}} = 0.0032$); at $s \geq 0.20$, no permutation exceeds the observed statistic.
87	
88	Table~\ref{tab:permutation} reports the results. All four sparsity levels reject $H_0$ after Bonferroni correction ($p_{\text{Bonf}} < 0.005$), with observed median differences increasing monotonically from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$. The monotonic growth of both the point estimate and the CI lower bound ($0.19 \to 0.69 \to 1.66 \to 6.70$) confirms that compound severity amplification strengthens with sparsity---not merely in central tendency but also in worst-case lower bounds. Figure~\ref{fig:permtest-forest} presents these results as a forest plot. % exp_id: deepseek_bf16_permtest; source: permutation_test_results.json
89	
90	\begin{table}[t]
91	\centering
92	\small
93	\caption{Paired permutation test for compound severity: importance vs.\ random eviction on DeepSeek-R1-Distill-Qwen-7B ($n{=}49$, $10{,}000$ permutations, Bonferroni-corrected).}
94	\label{tab:permutation}
95	\begin{tabular}{@{}rrcl@{}}
96	\toprule
97	$s$ & Observed $\widetilde{\Delta}$ & 95\% CI & $p_{\text{Bonf}}$ \\
98	\midrule
99	0.15 & 0.37 & $[0.19,\; 0.62]$ & 0.0032 \\ % exp_id: deepseek_bf16_permtest_s015
100	0.20 & 0.97 & $[0.69,\; 1.49]$ & ${<}\,0.001$ \\ % exp_id: deepseek_bf16_permtest_s020
101	0.25 & 3.34 & $[1.66,\; 6.64]$ & ${<}\,0.001$ \\ % exp_id: deepseek_bf16_permtest_s025
102	0.30 & 9.85 & $[6.70,\; 16.29]$ & ${<}\,0.001$ \\ % exp_id: deepseek_bf16_permtest_s030
103	\bottomrule
104	\end{tabular}
105	\end{table}
106	
107	\begin{figure}[t]
108	\centering
109	\includegraphics[width=\columnwidth]{fig4_bootstrap.pdf}
110	\caption{Forest plot of permutation test results. Horizontal bars show 95\% permutation CIs; diamonds mark observed median differences $\widetilde{\Delta}$. All CIs lie entirely above zero, confirming significant strategy-dependent severity at every sparsity level.}
111	\label{fig:permtest-forest}
112	\end{figure}
113	
114	
115	\section{Analysis: Entropy-Discrimination Collapse}
116	\label{app:analysis}
117	
118	\subsection{Discrimination Collapse}
119	\label{sec:discrimination-collapse}
120	
121	Head pruning reduces the number of heads contributing to cumulative importance scores, flattening the score distribution. Table~\ref{tab:discrimination-metrics-full} quantifies this effect: the Gini coefficient decreases by $0.030$--$0.081$ (DeepSeek) and $0.010$--$0.020$ (Qwen) after pruning, with consistent negative deltas across all 16 conditions (both models $\times$ 4 sparsity levels $\times$ 2 strategies). The CV delta is likewise negative in all 8 importance-based conditions. The same pattern holds under random eviction, confirming that discrimination collapse is a consequence of head pruning \emph{per se}, not of the eviction strategy. % exp_id: c4_entropy_deepseek, c4_entropy_qwen
122	
123	\begin{table}[t]
124	\centering
125	\caption{Discrimination collapse under importance-based eviction. $\Delta\mathrm{Gini}$ and $\Delta\mathrm{CV}$ are post-pruning minus baseline; negative values indicate reduced discriminative power.}
126	\label{tab:discrimination-metrics-full}
127	\small
128	\begin{tabular}{llrr}
129	\toprule
130	Model & $s$ & $\Delta\mathrm{Gini}$ & $\Delta\mathrm{CV}$ \\
131	\midrule
132	DeepSeek & $0.15$ & $-0.030$ & $-0.56$ \\
133	DeepSeek & $0.20$ & $-0.040$ & $-0.77$ \\
134	DeepSeek & $0.25$ & $-0.065$ & $-1.29$ \\
135	DeepSeek & $0.30$ & $-0.081$ & $-1.66$ \\
136	\midrule
137	Qwen & $0.15$ & $-0.010$ & $-0.05$ \\
138	Qwen & $0.20$ & $-0.012$ & $-0.21$ \\
139	Qwen & $0.25$ & $-0.010$ & $-1.49$ \\
140	Qwen & $0.30$ & $-0.020$ & $-1.14$ \\
141	\bottomrule
142	\end{tabular}
143	\end{table}
144	
145	When importance scores lose discriminability, thresholding degenerates into noise-sensitive selection---functionally approaching biased random eviction. This is phase-dependent: in low-sparsity phases, attention is already broadly distributed, so pruning-induced flattening has maximum impact; in high-sparsity phases, concentration is preserved. Random eviction is immune because its decisions are independent of score quality, explaining $G \approx 1$. % exp_id: c4_entropy_deepseek, c4_entropy_qwen
146	
147	\subsection{Entropy Redistribution}
148	\label{sec:entropy-redistribution}
149	
150	Beyond discrimination collapse, we examine whether head pruning also redistributes the attention entropy of surviving heads. We measure the mean attention entropy per head:
151	\begin{equation}
152	    \mathcal{H}_i^{(h)} = -\sum_{j=1}^{T} a_{ij}^{(h)} \log a_{ij}^{(h)}
153	    \label{eq:attn-entropy}
154	\end{equation}
155	and compute $\Delta\mathcal{H}$ as the change from baseline (no pruning) to the pruned condition.
156	
157	For DeepSeek under importance-based eviction, the entropy delta is consistently negative across all four sparsity levels ($\Delta\mathcal{H} \in [-0.047, -0.040]$; Table~\ref{tab:entropy-deltas}), indicating that importance-based pruning systematically selects heads whose removal concentrates attention in the surviving heads, reinforcing discrimination collapse. % exp_id: c4_entropy_deepseek
158	
159	For Qwen, the entropy pattern only partially replicates. The delta is negative at $s{=}0.15$ ($\Delta\mathcal{H} = -0.073$) and $s{=}0.20$ ($-0.076$), consistent with DeepSeek. However, at $s{=}0.25$, the delta reverses to $+0.045$, with 22 of 30 problems showing positive entropy change. At $s{=}0.30$, the delta is near zero ($-0.007$). The $s{=}0.25$ reversal is systematic rather than a statistical artifact: it is consistent across all three reasoning phases (low: $+0.042$, mid: $+0.034$, high: $+0.017$). We interpret this as a genuine model-specific difference, possibly arising from distinct head specialization patterns: Qwen's instruction tuning (vs.\ DeepSeek's distillation-based training) may produce head configurations where removing 25\% of heads triggers compensatory broadening rather than concentration. % exp_id: c4_entropy_qwen
160	
161	We characterize discrimination collapse as the robust, model-independent driver of the phase-strategy interaction, with entropy redistribution as a secondary amplifier that is consistent in DeepSeek but model-dependent in Qwen.
162	
163	\begin{table}[t]
164	\centering
165	\caption{Attention entropy deltas ($\Delta\mathcal{H}$) under importance-based eviction. DeepSeek shows consistent entropy compression; Qwen partially replicates with a reversal at $s{=}0.25$.}
166	\label{tab:entropy-deltas}
167	\small
168	\begin{tabular}{llr}
169	\toprule
170	Model & $s$ & $\Delta\mathcal{H}$ \\
171	\midrule
172	DeepSeek & $0.15$ & $-0.040$ \\
173	DeepSeek & $0.20$ & $-0.047$ \\
174	DeepSeek & $0.25$ & $-0.045$ \\
175	DeepSeek & $0.30$ & $-0.044$ \\
176	\midrule
177	Qwen & $0.15$ & $-0.073$ \\
178	Qwen & $0.20$ & $-0.076$ \\
179	Qwen & $0.25$ & $+0.045$ \\
180	Qwen & $0.30$ & $-0.007$ \\
181	\bottomrule
182	\end{tabular}
183	\end{table}
184	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "0cafe4a6-1b35-4cef-8eb0-cf2af1815fa4",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex",
      "content": "% Content moved from main body to appendix:\n% - Phase-strategy crossover details (from results §5.3)\n% - Cross-model replication details with tables/figures (from results §5.4)\n% - Permutation test details with table/forest plot (from results §5.5)\n% - Full entropy-discrimination collapse analysis with tables (from analysis §6)\n% Main body §6 (analysis.tex) contains a condensed summary referencing these tables.\n\n\\section{Phase-Strategy Crossover Details}\n\\label{app:crossover-details}\n\nAt $s{=}0.25$, a strategy ranking reversal emerges (Figure~\\ref{fig:crossover}): importance-based eviction yields \\emph{lower} II than random in the high-sparsity phase ($0.032$ vs.\\ $0.818$) but \\emph{higher} II in the low-sparsity phase ($7.196$ vs.\\ $1.363$---a $5.3{\\times}$ reversal). This crossover is present at all four sparsity levels, with reversal magnitude of $3.9{\\times}$ at $s{=}0.15$, $5.4{\\times}$ at $s{=}0.20$, $5.3{\\times}$ at $s{=}0.25$, and $3.6{\\times}$ at $s{=}0.30$ (as random eviction severity also rises). The reversal arises because head pruning redistributes attention mass, altering importance rankings in a way that couples the two sparsity mechanisms in low-sparsity phases (\\S\\ref{sec:discrimination-collapse}). % exp_id: bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json; 7.196/1.363=5.28\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig3_crossover.pdf}\n\\caption{Strategy-dependent crossover at $s{=}0.25$. Grouped bar chart of median II by eviction strategy and reasoning phase. Importance-based eviction outperforms random in the high-sparsity phase but produces $5.3{\\times}$ higher II in the low-sparsity phase, reversing the strategy ranking.}\n\\label{fig:crossover}\n\\end{figure}\n\n\n\\section{Cross-Model Replication Details}\n\\label{app:cross-model-details}\n\nBoth models share the Qwen2ForCausalLM backbone (28 layers, 28 heads, 4-group GQA) but differ in training: DeepSeek uses reasoning distillation from DeepSeek-R1, while Qwen2.5 uses standard instruction tuning without explicit reasoning delimiters. This controlled comparison isolates the effect of training methodology on the compound sparsity interaction.\n\nDespite lacking explicit \\texttt{&lt;think>} delimiters, Qwen2.5-7B-Instruct exhibits sufficient variation in attention sparsity to permit phase segmentation via the same quantile-based method (\\S\\ref{sec:phase-segmentation}). Four of the 50 problems are excluded due to degenerate phase assignments, yielding $n{=}46$ valid problems for Qwen (vs.\\ $n{=}49$ for DeepSeek).\n\n\\paragraph{Per-phase effective sample size.}\n\\label{app:qwen-null-rate}\nTable~\\ref{tab:qwen-effective-n} reports the per-phase effective sample size for Qwen2.5-7B-Instruct, defined as the number of problems with $|\\mathrm{II}| > 0.001$ in each phase. The mid-phase null rate (\\placeholder{NULL\\_PCT}\\%) reflects problems where compound interaction is absent in intermediate phases; this does not affect the low--high contrast ($\\Delta$) used in the primary analysis.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Per-phase effective sample size for Qwen2.5-7B-Instruct ($n_{\\text{total}} = \\placeholder{N\\_QW}$).}\n\\label{tab:qwen-effective-n}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nPhase & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\\\\n\\midrule\nHigh & \\placeholder{} & \\placeholder{} & \\placeholder{} & \\placeholder{} \\\\\nMid  & \\placeholder{} & \\placeholder{} & \\placeholder{} & \\placeholder{} \\\\\nLow  & \\placeholder{} & \\placeholder{} & \\placeholder{} & \\placeholder{} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:cross-model} reports the cross-model comparison. Qwen reproduces the monotonic severity gradient at ${\\sim}1/5$ of DeepSeek's magnitude. Figure~\\ref{fig:cross-model} visualizes this comparison. % exp_id: cross_model_analysis.json; cohens_d_bf16_qwen.json\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-model comparison of median compound severity difference ($\\Delta$) under importance-based eviction.}\n\\label{tab:cross-model}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nModel & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\\\\n\\midrule\nDeepSeek-R1-Distill-Qwen-7B & 0.39 & 1.48 & 7.16 & 14.59 \\\\ % exp_id: bf16_importance_s015..s030\nQwen2.5-7B-Instruct         & 0.04 & 0.23 & 1.27 & 2.94 \\\\ % exp_id: bf16_qw_imp_s015..s030\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig5_crossmodel.pdf}\n\\caption{Cross-model comparison of the median severity difference under importance-based eviction. Both DeepSeek (solid) and Qwen (dashed) exhibit monotonically increasing $\\Delta$ with sparsity; Qwen's magnitude is approximately one-fifth of DeepSeek's.} % exp_id: bf16_importance_s015..s030, bf16_qw_imp_s015..s030\n\\label{fig:cross-model}\n\\end{figure}\n\n\\paragraph{Per-problem concordance.}\nThe per-problem concordance across models is not significant (median $\\rho = \\placeholder{}$, $p = \\placeholder{}$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking. % exp_id: cross_model_analysis.json (spearman_rho=1.0, gradient_permutation_p=0.043, per_problem_concordance_p=0.926, mean_rho=-0.107)\n\n\\paragraph{Random eviction control.}\nAs a control, random eviction on Qwen yields no systematic phase gradient at three of four sparsity levels (3/4 FAIL), mirroring DeepSeek's 4/4 FAIL pattern. At $s{=}0.30$, Qwen random produces a borderline PASS (permutation $p = 0.012$) but with negligible median difference ($\\widetilde{\\Delta} = \\placeholder{}$, CI spans zero), indicating no meaningful phase modulation. % exp_id: bf16_qw_rand_s015..s030; source: experiment_summary_table.json\n\n\n\\section{Permutation Test Details}\n\\label{app:permutation-details}\n\nFor each problem $i$ and sparsity level $s$, we compute the compound severity difference $\\Delta_i^{(\\text{strat})} = \\mathrm{II}_{\\textit{low},i} - \\mathrm{II}_{\\textit{high},i}$ under each eviction strategy. The test statistic is the median of the paired difference $\\widetilde{\\Delta} = \\text{median}_i\\!\\bigl(\\Delta_i^{(\\text{imp})} - \\Delta_i^{(\\text{rand})}\\bigr)$, measuring whether importance-based eviction produces systematically larger phase-dependent severity than random eviction. We permute strategy labels $10{,}000$ times to construct the null distribution and apply Bonferroni correction for 4 sparsity-level comparisons.\n\nPer-problem distributions of the paired severity difference $\\Delta_i = \\mathrm{II}_{\\textit{low},i} - \\mathrm{II}_{\\textit{high},i}$ under importance-based eviction are right-skewed at all sparsity levels, with mean/median ratios ranging from $1.2{\\times}$ ($s{=}0.15$) to $1.6{\\times}$ ($s{=}0.30$) for DeepSeek and $1.1{\\times}$ to $1.4{\\times}$ for Qwen.\n\nThe permutation null distributions are approximately symmetric around zero at all sparsity levels. At $s{=}0.15$, the observed statistic falls at the $99.92$th percentile of the null ($p_{\\text{Bonf}} = 0.0032$); at $s \\geq 0.20$, no permutation exceeds the observed statistic.\n\nTable~\\ref{tab:permutation} reports the results. All four sparsity levels reject $H_0$ after Bonferroni correction ($p_{\\text{Bonf}} < 0.005$), with observed median differences increasing monotonically from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$. The monotonic growth of both the point estimate and the CI lower bound ($0.19 \\to 0.69 \\to 1.66 \\to 6.70$) confirms that compound severity amplification strengthens with sparsity---not merely in central tendency but also in worst-case lower bounds. Figure~\\ref{fig:permtest-forest} presents these results as a forest plot. % exp_id: deepseek_bf16_permtest; source: permutation_test_results.json\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Paired permutation test for compound severity: importance vs.\\ random eviction on DeepSeek-R1-Distill-Qwen-7B ($n{=}49$, $10{,}000$ permutations, Bonferroni-corrected).}\n\\label{tab:permutation}\n\\begin{tabular}{@{}rrcl@{}}\n\\toprule\n$s$ & Observed $\\widetilde{\\Delta}$ & 95\\% CI & $p_{\\text{Bonf}}$ \\\\\n\\midrule\n0.15 & 0.37 & $[0.19,\\; 0.62]$ & 0.0032 \\\\ % exp_id: deepseek_bf16_permtest_s015\n0.20 & 0.97 & $[0.69,\\; 1.49]$ & ${<}\\,0.001$ \\\\ % exp_id: deepseek_bf16_permtest_s020\n0.25 & 3.34 & $[1.66,\\; 6.64]$ & ${<}\\,0.001$ \\\\ % exp_id: deepseek_bf16_permtest_s025\n0.30 & 9.85 & $[6.70,\\; 16.29]$ & ${<}\\,0.001$ \\\\ % exp_id: deepseek_bf16_permtest_s030\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig4_bootstrap.pdf}\n\\caption{Forest plot of permutation test results. Horizontal bars show 95\\% permutation CIs; diamonds mark observed median differences $\\widetilde{\\Delta}$. All CIs lie entirely above zero, confirming significant strategy-dependent severity at every sparsity level.}\n\\label{fig:permtest-forest}\n\\end{figure}\n\n\n\\section{Analysis: Entropy-Discrimination Collapse}\n\\label{app:analysis}\n\n\\subsection{Discrimination Collapse}\n\\label{sec:discrimination-collapse}\n\nHead pruning reduces the number of heads contributing to cumulative importance scores, flattening the score distribution. Table~\\ref{tab:discrimination-metrics-full} quantifies this effect: the Gini coefficient decreases by $0.030$--$0.081$ (DeepSeek) and $0.010$--$0.020$ (Qwen) after pruning, with consistent negative deltas across all 16 conditions (both models $\\times$ 4 sparsity levels $\\times$ 2 strategies). The CV delta is likewise negative in all 8 importance-based conditions. The same pattern holds under random eviction, confirming that discrimination collapse is a consequence of head pruning \\emph{per se}, not of the eviction strategy. % exp_id: c4_entropy_deepseek, c4_entropy_qwen\n\n\\begin{table}[t]\n\\centering\n\\caption{Discrimination collapse under importance-based eviction. $\\Delta\\mathrm{Gini}$ and $\\Delta\\mathrm{CV}$ are post-pruning minus baseline; negative values indicate reduced discriminative power.}\n\\label{tab:discrimination-metrics-full}\n\\small\n\\begin{tabular}{llrr}\n\\toprule\nModel & $s$ & $\\Delta\\mathrm{Gini}$ & $\\Delta\\mathrm{CV}$ \\\\\n\\midrule\nDeepSeek & $0.15$ & $-0.030$ & $-0.56$ \\\\\nDeepSeek & $0.20$ & $-0.040$ & $-0.77$ \\\\\nDeepSeek & $0.25$ & $-0.065$ & $-1.29$ \\\\\nDeepSeek & $0.30$ & $-0.081$ & $-1.66$ \\\\\n\\midrule\nQwen & $0.15$ & $-0.010$ & $-0.05$ \\\\\nQwen & $0.20$ & $-0.012$ & $-0.21$ \\\\\nQwen & $0.25$ & $-0.010$ & $-1.49$ \\\\\nQwen & $0.30$ & $-0.020$ & $-1.14$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWhen importance scores lose discriminability, thresholding degenerates into noise-sensitive selection---functionally approaching biased random eviction. This is phase-dependent: in low-sparsity phases, attention is already broadly distributed, so pruning-induced flattening has maximum impact; in high-sparsity phases, concentration is preserved. Random eviction is immune because its decisions are independent of score quality, explaining $G \\approx 1$. % exp_id: c4_entropy_deepseek, c4_entropy_qwen\n\n\\subsection{Entropy Redistribution}\n\\label{sec:entropy-redistribution}\n\nBeyond discrimination collapse, we examine whether head pruning also redistributes the attention entropy of surviving heads. We measure the mean attention entropy per head:\n\\begin{equation}\n    \\mathcal{H}_i^{(h)} = -\\sum_{j=1}^{T} a_{ij}^{(h)} \\log a_{ij}^{(h)}\n    \\label{eq:attn-entropy}\n\\end{equation}\nand compute $\\Delta\\mathcal{H}$ as the change from baseline (no pruning) to the pruned condition.\n\nFor DeepSeek under importance-based eviction, the entropy delta is consistently negative across all four sparsity levels ($\\Delta\\mathcal{H} \\in [-0.047, -0.040]$; Table~\\ref{tab:entropy-deltas}), indicating that importance-based pruning systematically selects heads whose removal concentrates attention in the surviving heads, reinforcing discrimination collapse. % exp_id: c4_entropy_deepseek\n\nFor Qwen, the entropy pattern only partially replicates. The delta is negative at $s{=}0.15$ ($\\Delta\\mathcal{H} = -0.073$) and $s{=}0.20$ ($-0.076$), consistent with DeepSeek. However, at $s{=}0.25$, the delta reverses to $+0.045$, with 22 of 30 problems showing positive entropy change. At $s{=}0.30$, the delta is near zero ($-0.007$). The $s{=}0.25$ reversal is systematic rather than a statistical artifact: it is consistent across all three reasoning phases (low: $+0.042$, mid: $+0.034$, high: $+0.017$). We interpret this as a genuine model-specific difference, possibly arising from distinct head specialization patterns: Qwen's instruction tuning (vs.\\ DeepSeek's distillation-based training) may produce head configurations where removing 25\\% of heads triggers compensatory broadening rather than concentration. % exp_id: c4_entropy_qwen\n\nWe characterize discrimination collapse as the robust, model-independent driver of the phase-strategy interaction, with entropy redistribution as a secondary amplifier that is consistent in DeepSeek but model-dependent in Qwen.\n\n\\begin{table}[t]\n\\centering\n\\caption{Attention entropy deltas ($\\Delta\\mathcal{H}$) under importance-based eviction. DeepSeek shows consistent entropy compression; Qwen partially replicates with a reversal at $s{=}0.25$.}\n\\label{tab:entropy-deltas}\n\\small\n\\begin{tabular}{llr}\n\\toprule\nModel & $s$ & $\\Delta\\mathcal{H}$ \\\\\n\\midrule\nDeepSeek & $0.15$ & $-0.040$ \\\\\nDeepSeek & $0.20$ & $-0.047$ \\\\\nDeepSeek & $0.25$ & $-0.045$ \\\\\nDeepSeek & $0.30$ & $-0.044$ \\\\\n\\midrule\nQwen & $0.15$ & $-0.073$ \\\\\nQwen & $0.20$ & $-0.076$ \\\\\nQwen & $0.25$ & $+0.045$ \\\\\nQwen & $0.30$ & $-0.007$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
      "numLines": 184,
      "startLine": 1,
      "totalLines": 184
    }
  }
}
```

</details>

---

### Tool call

_source line 52_

<details open><summary>🔧 Tool call — Read · `toolu_01EJ1SiqeHM5hwzgwkJzRvB4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "b1bc81a3-f534-44b8-8e3c-95ce78f39f0e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JQN68tPnituvj3EfYDfmKY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9273,
      "cache_read_input_tokens": 34088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9273
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

_source line 53 · 2026-05-15T01:40:43.633Z_

<details><summary>↩ Tool result · `toolu_01EJ1SiqeHM5hwzgwkJzRvB4`</summary>

```text
1	\section{Discrimination Collapse Details}
2	\label{app:discrimination-collapse-details}
3	
4	This cross-model consistency (Table~\ref{tab:discrimination-metrics-full}) establishes discrimination collapse as a robust consequence of compound sparsity. When importance scores lose discriminative power, thresholding the bottom-$s$ fraction becomes noise-sensitive: small perturbations change which positions cross the eviction boundary. In the limit of perfectly uniform scores, importance-based eviction degenerates into an arbitrary selection functionally equivalent to biased random eviction. The same pattern holds under random eviction (DeepSeek: $-0.031$ to $-0.073$; Qwen: $-0.019$ to $-0.045$), confirming that discrimination collapse is a consequence of head pruning \emph{per se}, not of the eviction strategy. % exp_id: c4_entropy_deepseek, c4_entropy_qwen
5	
6	
7	\section{Extended Discussion}
8	\label{app:extended-discussion}
9	
10	\paragraph{On the predictability of phase-modulated severity.}
11	The compound interaction is not uniformly fragile---it is selectively fragile in a phase-dependent manner ($\widetilde{\mathrm{II}}_{\text{high}} < 0.06$ at $s \leq 0.30$; at $s = 0.35$, high-phase II rises to $0.105$ in a supplementary experiment, indicating onset of compound interaction even in high-sparsity phases at extreme pruning rates). % exp_id: bf16_importance_s015..s030, bf16_ds_imp_s035; high-phase medians: 0.006, 0.015, 0.032, 0.053; s035 II_high=0.1051
12	
13	\paragraph{Random masking as falsification control.}
14	Random eviction fails 7/8 paired permutation tests across both models; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) exhibits negligible effect size ($\widetilde{\Delta} = \placeholder{}$). The absence of a phase gradient under random masking isolates the amplification as strategy-specific. % exp_id: bf16_ds_rand_s015..s030, bf16_qw_rand_s015..s030
15	
16	\paragraph{Entropy mechanism boundary conditions.}
17	Directly measuring per-head entropy shifts across architecturally distinct models---and identifying what training-time properties determine whether entropy concentrates or disperses under head pruning---would clarify the boundary conditions of the full mechanism.
18	
19	
20	\section{Extended Limitations}
21	\label{app:limitations}
22	
23	\paragraph{Model scale.}
24	All experiments are conducted at the 7B parameter scale.
25	Whether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested.
26	Larger models may exhibit different attention redundancy structures that alter the discrimination collapse dynamics (and the model-dependent entropy component may behave differently at scale).
27	% REVIEWER-ATTACK: "7B is too small to be relevant for production."
28	% REBUTTAL: 7B is the most-deployed scale for on-device and cost-constrained serving—exactly where compound sparsity is needed. The mechanism (entropy-discrimination collapse) is scale-agnostic in principle. Scaling experiments are future work.
29	
30	\paragraph{Architectural scope.}
31	Our two models---DeepSeek-R1-Distill-Qwen-7B and Qwen2.5-7B-Instruct---share the Qwen2ForCausalLM architecture.
32	The cross-model replication (\S\ref{sec:cross-model}) establishes that the findings are not artifacts of a single model's weights, though both models share the same Qwen2ForCausalLM architecture.
33	Preliminary cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \S\ref{sec:cross-arch}) shows qualitatively consistent within-importance phase gradients ($d_z \sim 1.0$) but a substantially weaker strategy $\times$ phase interaction than in Qwen2-based architectures; random pruning also exhibits a non-trivial phase gradient on LLaMA, reducing the strategy contrast. This partial confirmation ($s{=}0.30$ Wilcoxon $p_{\text{Bonf}}{=}0.029$; $s \leq 0.25$ non-significant) suggests the qualitative pattern may generalize but quantitative impact is architecture-dependent. Comprehensive cross-architecture validation across more diverse designs (e.g., Mistral, multi-latent attention architectures) and scales remains an important next step.
34	% REVIEWER-ATTACK: "Cross-model ≠ cross-architecture. Both are Qwen2ForCausalLM."
35	% REBUTTAL: We now include cross-architecture validation on LlamaForCausalLM (\S\ref{sec:cross-arch}), which shows a qualitatively consistent but substantially weaker pattern. We use qualified language ("partially supports") rather than claiming full generalization.
36	
37	\paragraph{Task coverage.}
38	We evaluate exclusively on MATH-500, a mathematical reasoning benchmark.
39	Different reasoning tasks---code generation, commonsense reasoning, multi-hop question answering---may induce different phase structures with different sparsity distributions, potentially altering the severity gradient profile.
40	Generalizing the phase-strategy interaction to broader reasoning domains is an important next step.
41	% REVIEWER-ATTACK: "Only MATH-500. How do we know this isn't a math-specific artifact?"
42	% REBUTTAL: The mechanism (entropy-discrimination collapse under head pruning) depends on attention distribution properties, not math-specific features. MATH-500 is a standard benchmark with diverse difficulty. However, different reasoning tasks may induce different phase structures—we state this limitation explicitly rather than overclaiming.
43	
44	\paragraph{Statistical scope.}
45	Bootstrap confidence intervals use $B{=}10{,}000$ resamples (recomputed from initial $B{=}1{,}000$ profiling runs). The paired permutation test yields $n{=}49$ paired problems for DeepSeek (1 excluded) and $n{=}46$ for Qwen (4 excluded). % exp_id: cohens_d_bf16.json, cohens_d_bf16_qwen.json
46	The severity difference distribution is right-skewed (mean/median ratio ${\sim}1.6{:}1$ at $s{=}0.30$), motivating our use of medians and nonparametric tests rather than parametric alternatives. % exp_id: bf16_importance_s030; mean_diff=22.94, median_diff=14.59 (segment-level). Per-problem paired: median_diff=9.9436 at s030
47	All four permutation tests reject $H_0$ after Bonferroni correction ($p_{\text{Bonf}} < 0.005$; Table~\ref{tab:permutation}), with CI lower bounds increasing from $0.19$ to $6.70$---confirming the effect direction at every sparsity level. The permutation CIs at higher sparsity are wider (e.g., $[6.70,\; 16.29]$ at $s{=}0.30$), reflecting genuine variance in per-problem severity amplification. % exp_id: permutation_test_results.json; permutation CIs: s015=[0.19,0.62], s020=[0.69,1.49], s025=[1.66,6.64], s030=[6.70,16.29]
48	
49	A notable exception among the random baselines is the Qwen random condition at $s{=}0.30$, which yields a statistically significant result ($p{=}0.012$) despite negligible effect size ($\widetilde{\Delta} = \placeholder{}$, bootstrap CI spanning zero). % exp_id: qw_rand_s030; B=10000, p=0.012, d=-0.035, negligible
50	This case illustrates that dichotomous significance testing can flag effects of no practical magnitude---reinforcing the importance of reporting effect sizes and confidence intervals alongside $p$-values.
51	
52	\paragraph{Sparsity range.}
53	Our experiments span $s \in \{0.15, 0.20, 0.25, 0.30\}$, a moderate range representative of practical deployment targets.
54	More extreme sparsity ($s > 0.50$) may exhibit qualitatively different interaction dynamics---the sub-exponential growth pattern suggests the severity gradient may plateau, but this remains unverified.
55	Conversely, the lower boundary at which phase-modulated amplification first emerges is not yet characterized.
56	% REVIEWER-ATTACK: "Why not test higher sparsity? 0.30 is conservative."
57	% REBUTTAL: Our focus is on the practically relevant regime where models retain usable quality. At s>0.30 both strategies degrade severely, making II measurement less informative. The sub-exponential growth (C6, $\Delta$ growth rate $3.8{\times} \to 4.8{\times} \to 2.0{\times}$) suggests saturation at higher sparsity, but confirming this is future work.
58	
59	\paragraph{No throughput evaluation.}
60	We do not report inference throughput or latency, which are necessary for deployment analysis but orthogonal to our severity characterization.
61	% REVIEWER-ATTACK: "No system evaluation. How do we know the severity amplification matters for real deployment?"
62	% REBUTTAL: This is an empirical finding paper, not a method/system paper. The contribution is characterizing *what happens* (phase-modulated severity) and *why* (entropy-discrimination collapse), not building a system to fix it. Phase-gated controllers are explicitly scoped as future work. The finding is actionable regardless: any compound sparsity deployment should be aware of phase-dependent severity.
63	
64	% Entropy redistribution analysis moved to main text \S\ref{sec:entropy-redistribution}
65	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "6a9feb22-e7c6-4fa5-9e43-5571833db3f1",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex",
      "content": "\\section{Discrimination Collapse Details}\n\\label{app:discrimination-collapse-details}\n\nThis cross-model consistency (Table~\\ref{tab:discrimination-metrics-full}) establishes discrimination collapse as a robust consequence of compound sparsity. When importance scores lose discriminative power, thresholding the bottom-$s$ fraction becomes noise-sensitive: small perturbations change which positions cross the eviction boundary. In the limit of perfectly uniform scores, importance-based eviction degenerates into an arbitrary selection functionally equivalent to biased random eviction. The same pattern holds under random eviction (DeepSeek: $-0.031$ to $-0.073$; Qwen: $-0.019$ to $-0.045$), confirming that discrimination collapse is a consequence of head pruning \\emph{per se}, not of the eviction strategy. % exp_id: c4_entropy_deepseek, c4_entropy_qwen\n\n\n\\section{Extended Discussion}\n\\label{app:extended-discussion}\n\n\\paragraph{On the predictability of phase-modulated severity.}\nThe compound interaction is not uniformly fragile---it is selectively fragile in a phase-dependent manner ($\\widetilde{\\mathrm{II}}_{\\text{high}} < 0.06$ at $s \\leq 0.30$; at $s = 0.35$, high-phase II rises to $0.105$ in a supplementary experiment, indicating onset of compound interaction even in high-sparsity phases at extreme pruning rates). % exp_id: bf16_importance_s015..s030, bf16_ds_imp_s035; high-phase medians: 0.006, 0.015, 0.032, 0.053; s035 II_high=0.1051\n\n\\paragraph{Random masking as falsification control.}\nRandom eviction fails 7/8 paired permutation tests across both models; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) exhibits negligible effect size ($\\widetilde{\\Delta} = \\placeholder{}$). The absence of a phase gradient under random masking isolates the amplification as strategy-specific. % exp_id: bf16_ds_rand_s015..s030, bf16_qw_rand_s015..s030\n\n\\paragraph{Entropy mechanism boundary conditions.}\nDirectly measuring per-head entropy shifts across architecturally distinct models---and identifying what training-time properties determine whether entropy concentrates or disperses under head pruning---would clarify the boundary conditions of the full mechanism.\n\n\n\\section{Extended Limitations}\n\\label{app:limitations}\n\n\\paragraph{Model scale.}\nAll experiments are conducted at the 7B parameter scale.\nWhether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested.\nLarger models may exhibit different attention redundancy structures that alter the discrimination collapse dynamics (and the model-dependent entropy component may behave differently at scale).\n% REVIEWER-ATTACK: \"7B is too small to be relevant for production.\"\n% REBUTTAL: 7B is the most-deployed scale for on-device and cost-constrained serving—exactly where compound sparsity is needed. The mechanism (entropy-discrimination collapse) is scale-agnostic in principle. Scaling experiments are future work.\n\n\\paragraph{Architectural scope.}\nOur two models---DeepSeek-R1-Distill-Qwen-7B and Qwen2.5-7B-Instruct---share the Qwen2ForCausalLM architecture.\nThe cross-model replication (\\S\\ref{sec:cross-model}) establishes that the findings are not artifacts of a single model's weights, though both models share the same Qwen2ForCausalLM architecture.\nPreliminary cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \\S\\ref{sec:cross-arch}) shows qualitatively consistent within-importance phase gradients ($d_z \\sim 1.0$) but a substantially weaker strategy $\\times$ phase interaction than in Qwen2-based architectures; random pruning also exhibits a non-trivial phase gradient on LLaMA, reducing the strategy contrast. This partial confirmation ($s{=}0.30$ Wilcoxon $p_{\\text{Bonf}}{=}0.029$; $s \\leq 0.25$ non-significant) suggests the qualitative pattern may generalize but quantitative impact is architecture-dependent. Comprehensive cross-architecture validation across more diverse designs (e.g., Mistral, multi-latent attention architectures) and scales remains an important next step.\n% REVIEWER-ATTACK: \"Cross-model ≠ cross-architecture. Both are Qwen2ForCausalLM.\"\n% REBUTTAL: We now include cross-architecture validation on LlamaForCausalLM (\\S\\ref{sec:cross-arch}), which shows a qualitatively consistent but substantially weaker pattern. We use qualified language (\"partially supports\") rather than claiming full generalization.\n\n\\paragraph{Task coverage.}\nWe evaluate exclusively on MATH-500, a mathematical reasoning benchmark.\nDifferent reasoning tasks---code generation, commonsense reasoning, multi-hop question answering---may induce different phase structures with different sparsity distributions, potentially altering the severity gradient profile.\nGeneralizing the phase-strategy interaction to broader reasoning domains is an important next step.\n% REVIEWER-ATTACK: \"Only MATH-500. How do we know this isn't a math-specific artifact?\"\n% REBUTTAL: The mechanism (entropy-discrimination collapse under head pruning) depends on attention distribution properties, not math-specific features. MATH-500 is a standard benchmark with diverse difficulty. However, different reasoning tasks may induce different phase structures—we state this limitation explicitly rather than overclaiming.\n\n\\paragraph{Statistical scope.}\nBootstrap confidence intervals use $B{=}10{,}000$ resamples (recomputed from initial $B{=}1{,}000$ profiling runs). The paired permutation test yields $n{=}49$ paired problems for DeepSeek (1 excluded) and $n{=}46$ for Qwen (4 excluded). % exp_id: cohens_d_bf16.json, cohens_d_bf16_qwen.json\nThe severity difference distribution is right-skewed (mean/median ratio ${\\sim}1.6{:}1$ at $s{=}0.30$), motivating our use of medians and nonparametric tests rather than parametric alternatives. % exp_id: bf16_importance_s030; mean_diff=22.94, median_diff=14.59 (segment-level). Per-problem paired: median_diff=9.9436 at s030\nAll four permutation tests reject $H_0$ after Bonferroni correction ($p_{\\text{Bonf}} < 0.005$; Table~\\ref{tab:permutation}), with CI lower bounds increasing from $0.19$ to $6.70$---confirming the effect direction at every sparsity level. The permutation CIs at higher sparsity are wider (e.g., $[6.70,\\; 16.29]$ at $s{=}0.30$), reflecting genuine variance in per-problem severity amplification. % exp_id: permutation_test_results.json; permutation CIs: s015=[0.19,0.62], s020=[0.69,1.49], s025=[1.66,6.64], s030=[6.70,16.29]\n\nA notable exception among the random baselines is the Qwen random condition at $s{=}0.30$, which yields a statistically significant result ($p{=}0.012$) despite negligible effect size ($\\widetilde{\\Delta} = \\placeholder{}$, bootstrap CI spanning zero). % exp_id: qw_rand_s030; B=10000, p=0.012, d=-0.035, negligible\nThis case illustrates that dichotomous significance testing can flag effects of no practical magnitude---reinforcing the importance of reporting effect sizes and confidence intervals alongside $p$-values.\n\n\\paragraph{Sparsity range.}\nOur experiments span $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$, a moderate range representative of practical deployment targets.\nMore extreme sparsity ($s > 0.50$) may exhibit qualitatively different interaction dynamics---the sub-exponential growth pattern suggests the severity gradient may plateau, but this remains unverified.\nConversely, the lower boundary at which phase-modulated amplification first emerges is not yet characterized.\n% REVIEWER-ATTACK: \"Why not test higher sparsity? 0.30 is conservative.\"\n% REBUTTAL: Our focus is on the practically relevant regime where models retain usable quality. At s>0.30 both strategies degrade severely, making II measurement less informative. The sub-exponential growth (C6, $\\Delta$ growth rate $3.8{\\times} \\to 4.8{\\times} \\to 2.0{\\times}$) suggests saturation at higher sparsity, but confirming this is future work.\n\n\\paragraph{No throughput evaluation.}\nWe do not report inference throughput or latency, which are necessary for deployment analysis but orthogonal to our severity characterization.\n% REVIEWER-ATTACK: \"No system evaluation. How do we know the severity amplification matters for real deployment?\"\n% REBUTTAL: This is an empirical finding paper, not a method/system paper. The contribution is characterizing *what happens* (phase-modulated severity) and *why* (entropy-discrimination collapse), not building a system to fix it. Phase-gated controllers are explicitly scoped as future work. The finding is actionable regardless: any compound sparsity deployment should be aware of phase-dependent severity.\n\n% Entropy redistribution analysis moved to main text \\S\\ref{sec:entropy-redistribution}\n",
      "numLines": 65,
      "startLine": 1,
      "totalLines": 65
    }
  }
}
```

</details>

---

### Assistant

_source line 54_

<details><summary>Logged reasoning block</summary>

```text
Now let me also check the Qwen imp-vs-rand significance issue and search for any \placeholder markers, and check the related_work and background files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "396f15f2-72b5-40fa-917d-669f86638d22",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KtdXajphcpcVn5zAS1x3Ea",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10801,
      "cache_read_input_tokens": 43361,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10801
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

Let me also check for all `\placeholder` markers and read the remaining files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "5e333585-ae14-4fdf-9271-e77ae30446fa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KtdXajphcpcVn5zAS1x3Ea",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10801,
      "cache_read_input_tokens": 43361,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10801
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

<details open><summary>🔧 Tool call — Grep · `toolu_01NRvCt8w9aYqLks7YsFav4G`</summary>

```json
{
  "pattern": "\\\\\\\\placeholder",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "0378616e-8e14-499a-8cf8-11af8c0397de",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KtdXajphcpcVn5zAS1x3Ea",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10801,
      "cache_read_input_tokens": 43361,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10801
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

_source line 57 · 2026-05-15T01:40:52.832Z_

<details><summary>↩ Tool result · `toolu_01NRvCt8w9aYqLks7YsFav4G`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "b5e56cbb-83cc-469c-a83e-d32f536d1fa0",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  }
}
```

</details>

---

### Tool call

_source line 58_

<details open><summary>🔧 Tool call — Read · `toolu_01Wj8FwYP3yZQHQrKFujNzdZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "75173fd1-07d2-4d7b-9c22-120275417b2d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KtdXajphcpcVn5zAS1x3Ea",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10801,
      "cache_read_input_tokens": 43361,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10801
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

_source line 59 · 2026-05-15T01:40:53.318Z_

<details><summary>↩ Tool result · `toolu_01Wj8FwYP3yZQHQrKFujNzdZ`</summary>

```text
1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Compound compression.}
5	Combining multiple compression axes produces non-additive errors.
6	\cite{spark-aaai2026} report super-additive degradation when combining channel pruning with token eviction; \cite{slim-icml2025} formalize compound error for quantization and sparsity.
7	\cite{unicomp-2026} evaluate compound compression across 40+ benchmarks, revealing that reasoning capabilities degrade disproportionately.
8	\cite{phase-transition-compression-2026} characterize independent phase transition points per compression dimension, implying the joint safe region is the intersection of per-dimension safe zones.
9	GRASPrune~\cite{graspune-acl2026} learns global budget-constrained gates for joint pruning but treats decisions as static across generation.
10	These works establish compound interaction but share an implicit assumption: interaction magnitude is constant across the generation process.
11	
12	\paragraph{KV cache eviction.}
13	Most methods rely on importance scoring whose reliability is increasingly questioned.
14	Ada-KV~\cite{adakv-neurips2025} introduces per-head adaptive budgets; SnapKV~\cite{snapkv-neurips2024} compresses from a fixed observation window; \cite{defensivekv-iclr2026} show worst-case loss $2.3$--$4.3{\times}$ higher than expected under standard aggregation.
15	\cite{nacl-acl2024} combine proxy-token and random eviction to counter attention bias.
16	RetentiveKV~\cite{retentivekv-2026} identifies deferred importance, and \cite{greedy-bias-kvcache-2026} show that single importance metrics exhibit systematic greedy bias.
17	\cite{hies-2025} independently show that importance-based head discrimination collapses under heavy pruning, further questioning single-metric reliability.
18	Lethe~\cite{lethe-aaai2026} introduces temporal adaptivity with layer-wise multi-round pruning, and SparK~\cite{spark-aaai2026} extends eviction to the channel dimension with recoverable sparsity.
19	These methods each optimize a single pruning axis---whether aggregation, metric, temporal, or channel---without characterizing compound interactions when multiple mechanisms are simultaneously active.
20	
21	\paragraph{Phase-aware inference.}
22	ThinKV~\cite{thinkv-iclr2026} applies different KV strategies per phase but without compound interaction.
23	\cite{decision-repr-transition-2026} find pruning sensitivity depends on ``silent'' vs.\ ``decisive'' representation phases.
24	\cite{doing-more-with-less-2026} show pruning combined with test-time scaling can exceed unpruned baselines; \cite{sparse-frontier-2025} find no universally optimal sparse attention strategy across generation stages.
25	\cite{physics-kvcache-2026} identify a sharp phase transition in single-axis KV cache compression at high sparsity, characterizing the single-dimension failure mode that our compound analysis extends across multiple axes.
26	R-KV~\cite{rkv-neurips2025} exploits reasoning-specific redundancy for aggressive cache compression, targeting per-axis optimization rather than characterizing compound degradation.
27	These works establish phase-dependent compression tolerance along single axes.
28	Our work bridges this by quantifying how compound severity varies across phases and eviction strategies.
29	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "44db26f1-2f47-4fcd-839b-efd2cc3b61e0",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{Compound compression.}\nCombining multiple compression axes produces non-additive errors.\n\\cite{spark-aaai2026} report super-additive degradation when combining channel pruning with token eviction; \\cite{slim-icml2025} formalize compound error for quantization and sparsity.\n\\cite{unicomp-2026} evaluate compound compression across 40+ benchmarks, revealing that reasoning capabilities degrade disproportionately.\n\\cite{phase-transition-compression-2026} characterize independent phase transition points per compression dimension, implying the joint safe region is the intersection of per-dimension safe zones.\nGRASPrune~\\cite{graspune-acl2026} learns global budget-constrained gates for joint pruning but treats decisions as static across generation.\nThese works establish compound interaction but share an implicit assumption: interaction magnitude is constant across the generation process.\n\n\\paragraph{KV cache eviction.}\nMost methods rely on importance scoring whose reliability is increasingly questioned.\nAda-KV~\\cite{adakv-neurips2025} introduces per-head adaptive budgets; SnapKV~\\cite{snapkv-neurips2024} compresses from a fixed observation window; \\cite{defensivekv-iclr2026} show worst-case loss $2.3$--$4.3{\\times}$ higher than expected under standard aggregation.\n\\cite{nacl-acl2024} combine proxy-token and random eviction to counter attention bias.\nRetentiveKV~\\cite{retentivekv-2026} identifies deferred importance, and \\cite{greedy-bias-kvcache-2026} show that single importance metrics exhibit systematic greedy bias.\n\\cite{hies-2025} independently show that importance-based head discrimination collapses under heavy pruning, further questioning single-metric reliability.\nLethe~\\cite{lethe-aaai2026} introduces temporal adaptivity with layer-wise multi-round pruning, and SparK~\\cite{spark-aaai2026} extends eviction to the channel dimension with recoverable sparsity.\nThese methods each optimize a single pruning axis---whether aggregation, metric, temporal, or channel---without characterizing compound interactions when multiple mechanisms are simultaneously active.\n\n\\paragraph{Phase-aware inference.}\nThinKV~\\cite{thinkv-iclr2026} applies different KV strategies per phase but without compound interaction.\n\\cite{decision-repr-transition-2026} find pruning sensitivity depends on ``silent'' vs.\\ ``decisive'' representation phases.\n\\cite{doing-more-with-less-2026} show pruning combined with test-time scaling can exceed unpruned baselines; \\cite{sparse-frontier-2025} find no universally optimal sparse attention strategy across generation stages.\n\\cite{physics-kvcache-2026} identify a sharp phase transition in single-axis KV cache compression at high sparsity, characterizing the single-dimension failure mode that our compound analysis extends across multiple axes.\nR-KV~\\cite{rkv-neurips2025} exploits reasoning-specific redundancy for aggressive cache compression, targeting per-axis optimization rather than characterizing compound degradation.\nThese works establish phase-dependent compression tolerance along single axes.\nOur work bridges this by quantifying how compound severity varies across phases and eviction strategies.\n",
      "numLines": 29,
      "startLine": 1,
      "totalLines": 29
    }
  }
}
```

</details>

---

### Tool call

_source line 60_

<details open><summary>🔧 Tool call — Read · `toolu_01JAB4ZfKLCYfgZuzV4PmCYM`</summary>

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
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "a6d35849-cf9c-4fdc-b3ec-8861f08dbb15",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KtdXajphcpcVn5zAS1x3Ea",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10801,
      "cache_read_input_tokens": 43361,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10801
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

_source line 61 · 2026-05-15T01:40:53.556Z_

<details><summary>↩ Tool result · `toolu_01JAB4ZfKLCYfgZuzV4PmCYM`</summary>

```text
1	% Section 3: Background and Problem Setup
2	% Note: eq:ii and eq:gradient are the canonical definitions.
3	% Full formulation details in Appendix (app:formulation-details).
4	
5	\section{Background and Problem Setup}
6	\label{sec:background}
7	
8	We formalize compound sparsity, define the Interaction Index, and introduce phase segmentation. Full mathematical details appear in Appendix~\ref{app:formulation-details}.
9	
10	\paragraph{Compound sparsity.}
11	\label{sec:compound-sparsity}
12	Let $s \in (0,1)$ denote a unified sparsity budget. \emph{Attention head pruning} removes the bottom-$s$ fraction of heads per layer by Frobenius norm importance \cite{voita-acl2019, michel-neurips2019}. \emph{KV cache eviction} removes the bottom-$s$ fraction of token positions from the cache. We compare two strategies: \emph{importance-based}, which scores positions by position-normalized cumulative attention mass (Eq.~\ref{eq:kv-importance} in Appendix~\ref{app:formulation-details}), and \emph{random}, which evicts uniformly at random \cite{nacl-acl2024}. Applying both simultaneously yields \emph{compound sparsity}; the two axes interact because head pruning alters the importance ranking used for eviction \cite{spark-aaai2026}. Existing joint-pruning approaches such as GRASPrune \cite{graspune-acl2026} learn global budget-constrained gates but treat decisions as static across generation.
13	
14	\paragraph{Interaction Index.}
15	\label{sec:interaction-index}
16	For a text segment, let $\text{PPL}_c$ denote perplexity under condition $c \in \{d, a, k, b\}$ (dense, attention-only, KV-only, compound). Normalizing by the dense baseline yields $r_c = \text{PPL}_c / \text{PPL}_d$, and:
17	\begin{equation}
18	    \mathrm{II} = r_b - r_a - r_k + 1.
19	    \label{eq:ii}
20	\end{equation}
21	$\mathrm{II} > 0$ indicates super-additive degradation; $\mathrm{II} = 0$ indicates additive independence. We adopt the additive null because the two axes operate on disjoint dimensions; qualitative conclusions hold under the multiplicative null (Appendix~\ref{app:multiplicative-null}). Because the II distribution is heavily right-skewed, we report medians throughout.
22	
23	\paragraph{Severity gradient.}
24	To capture phase variation:
25	\begin{equation}
26	    G = \frac{\widetilde{\mathrm{II}}_{\,\textit{low}}}{\widetilde{\mathrm{II}}_{\,\textit{high}}},
27	    \label{eq:gradient}
28	\end{equation}
29	where $\widetilde{\mathrm{II}}_{\,\textit{low/high}}$ are median II in the low/high-sparsity phases. $G \gg 1$ indicates phase-concentrated severity.
30	
31	\paragraph{Phase segmentation.}
32	\label{sec:phase-segmentation}
33	Each generated sequence is partitioned into three phases (low-, mid-, high-sparsity) by tercile boundaries of per-position attention sparsity, following ThinKV~\cite{thinkv-iclr2026}. Low-sparsity phases correspond to broadly distributed attention (exploratory reasoning); high-sparsity phases to concentrated attention (structured computation). Details in Appendix~\ref{app:formulation-details}.
34	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "d63ec528-64c8-4be1-a45f-da34962d3992",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex",
      "content": "% Section 3: Background and Problem Setup\n% Note: eq:ii and eq:gradient are the canonical definitions.\n% Full formulation details in Appendix (app:formulation-details).\n\n\\section{Background and Problem Setup}\n\\label{sec:background}\n\nWe formalize compound sparsity, define the Interaction Index, and introduce phase segmentation. Full mathematical details appear in Appendix~\\ref{app:formulation-details}.\n\n\\paragraph{Compound sparsity.}\n\\label{sec:compound-sparsity}\nLet $s \\in (0,1)$ denote a unified sparsity budget. \\emph{Attention head pruning} removes the bottom-$s$ fraction of heads per layer by Frobenius norm importance \\cite{voita-acl2019, michel-neurips2019}. \\emph{KV cache eviction} removes the bottom-$s$ fraction of token positions from the cache. We compare two strategies: \\emph{importance-based}, which scores positions by position-normalized cumulative attention mass (Eq.~\\ref{eq:kv-importance} in Appendix~\\ref{app:formulation-details}), and \\emph{random}, which evicts uniformly at random \\cite{nacl-acl2024}. Applying both simultaneously yields \\emph{compound sparsity}; the two axes interact because head pruning alters the importance ranking used for eviction \\cite{spark-aaai2026}. Existing joint-pruning approaches such as GRASPrune \\cite{graspune-acl2026} learn global budget-constrained gates but treat decisions as static across generation.\n\n\\paragraph{Interaction Index.}\n\\label{sec:interaction-index}\nFor a text segment, let $\\text{PPL}_c$ denote perplexity under condition $c \\in \\{d, a, k, b\\}$ (dense, attention-only, KV-only, compound). Normalizing by the dense baseline yields $r_c = \\text{PPL}_c / \\text{PPL}_d$, and:\n\\begin{equation}\n    \\mathrm{II} = r_b - r_a - r_k + 1.\n    \\label{eq:ii}\n\\end{equation}\n$\\mathrm{II} > 0$ indicates super-additive degradation; $\\mathrm{II} = 0$ indicates additive independence. We adopt the additive null because the two axes operate on disjoint dimensions; qualitative conclusions hold under the multiplicative null (Appendix~\\ref{app:multiplicative-null}). Because the II distribution is heavily right-skewed, we report medians throughout.\n\n\\paragraph{Severity gradient.}\nTo capture phase variation:\n\\begin{equation}\n    G = \\frac{\\widetilde{\\mathrm{II}}_{\\,\\textit{low}}}{\\widetilde{\\mathrm{II}}_{\\,\\textit{high}}},\n    \\label{eq:gradient}\n\\end{equation}\nwhere $\\widetilde{\\mathrm{II}}_{\\,\\textit{low/high}}$ are median II in the low/high-sparsity phases. $G \\gg 1$ indicates phase-concentrated severity.\n\n\\paragraph{Phase segmentation.}\n\\label{sec:phase-segmentation}\nEach generated sequence is partitioned into three phases (low-, mid-, high-sparsity) by tercile boundaries of per-position attention sparsity, following ThinKV~\\cite{thinkv-iclr2026}. Low-sparsity phases correspond to broadly distributed attention (exploratory reasoning); high-sparsity phases to concentrated attention (structured computation). Details in Appendix~\\ref{app:formulation-details}.\n",
      "numLines": 34,
      "startLine": 1,
      "totalLines": 34
    }
  }
}
```

</details>

---

### Assistant

_source line 62_

<details><summary>Logged reasoning block</summary>

```text
Let me now search for `\placeholder` with just one backslash, since the grep might have been escaping differently.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "f89e3e56-ac78-45fa-b62b-9336098f5c9c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013KQNU43H6ofMHJNWmd7vrK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2282,
      "cache_read_input_tokens": 54162,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2282
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

<details open><summary>🔧 Tool call — Grep · `toolu_01ChYjC7Kb1eDVupnxE8Diwe`</summary>

```json
{
  "pattern": "placeholder",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "9ff04054-706b-4967-9888-f031606aa812",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013KQNU43H6ofMHJNWmd7vrK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2282,
      "cache_read_input_tokens": 54162,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2282
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

_source line 64 · 2026-05-15T01:41:00.733Z_

<details><summary>↩ Tool result · `toolu_01ChYjC7Kb1eDVupnxE8Diwe`</summary>

```text
artifacts/_project/paper/main.tex:21:\newcommand{\placeholder}[1]{\textcolor{red}{[#1]}}
artifacts/_project/paper/discussion.tex:10:[Omitted long matching line]
artifacts/_project/paper/discussion.tex:15:[Omitted long matching line]
artifacts/_project/paper/appendix_moved.tex:30:Table~\ref{tab:qwen-effective-n} reports the per-phase effective sample size for Qwen2.5-7B-Instruct, defined as the number of problems with $|\mathrm{II}| > 0.001$ in each phase. The mid-phase null rate (\placeholder{NULL\_PCT}\%) reflects problems where compound interaction is absent in intermediate phases; this does not affect the low--high contrast ($\Delta$) used in the primary analysis.
artifacts/_project/paper/appendix_moved.tex:35:\caption{Per-phase effective sample size for Qwen2.5-7B-Instruct ($n_{\text{total}} = \placeholder{N\_QW}$).}
artifacts/_project/paper/appendix_moved.tex:41:High & \placeholder{} & \placeholder{} & \placeholder{} & \placeholder{} \\
artifacts/_project/paper/appendix_moved.tex:42:Mid  & \placeholder{} & \placeholder{} & \placeholder{} & \placeholder{} \\
artifacts/_project/paper/appendix_moved.tex:43:Low  & \placeholder{} & \placeholder{} & \placeholder{} & \placeholder{} \\
artifacts/_project/paper/appendix_moved.tex:73:The per-problem concordance across models is not significant (median $\rho = \placeholder{}$, $p = \placeholder{}$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking. % exp_id: cross_model_analysis.json (spearman_rho=1.0, gradient_permutation_p=0.043, per_problem_concordance_p=0.926, mean_rho=-0.107)
artifacts/_project/paper/appendix_moved.tex:76:As a control, random eviction on Qwen yields no systematic phase gradient at three of four sparsity levels (3/4 FAIL), mirroring DeepSeek's 4/4 FAIL pattern. At $s{=}0.30$, Qwen random produces a borderline PASS (permutation $p = 0.012$) but with negligible median difference ($\widetilde{\Delta} = \placeholder{}$, CI spans zero), indicating no meaningful phase modulation. % exp_id: bf16_qw_rand_s015..s030; source: experiment_summary_table.json
artifacts/_project/paper/abstract.tex:8:Random eviction produces no significant phase modulation in 7/8 conditions; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) shows negligible median difference ($\widetilde{\Delta} = \placeholder{}$), confirming that the severity gradient is strategy-specific, not an inherent property of compound sparsity.
artifacts/_project/paper/appendix_results.tex:7:The per-problem concordance across models is not significant (median $\rho = \placeholder{}$, $p = \placeholder{}$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking. % exp_id: cross_model_analysis.json (spearman_rho=1.0, gradient_permutation_p=0.043, per_problem_concordance_p=0.926, mean_rho=-0.107)
artifacts/_project/paper/appendix_results.tex:10:As a control, random eviction on Qwen yields no systematic phase gradient at three of four sparsity levels (3/4 FAIL), mirroring DeepSeek's 4/4 FAIL pattern. At $s{=}0.30$, Qwen random produces a borderline PASS (permutation $p = 0.012$) but with negligible median difference ($\widetilde{\Delta} = \placeholder{}$, CI spans zero), indicating no meaningful phase modulation. % exp_id: bf16_qw_rand_s015..s030; source: experiment_summary_table.json
artifacts/_project/paper/appendix_disc_analysis.tex:14:Random eviction fails 7/8 paired permutation tests across both models; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) exhibits negligible effect size ($\widetilde{\Delta} = \placeholder{}$). The absence of a phase gradient under random masking isolates the amplification as strategy-specific. % exp_id: bf16_ds_rand_s015..s030, bf16_qw_rand_s015..s030
artifacts/_project/paper/appendix_disc_analysis.tex:49:A notable exception among the random baselines is the Qwen random condition at $s{=}0.30$, which yields a statistically significant result ($p{=}0.012$) despite negligible effect size ($\widetilde{\Delta} = \placeholder{}$, bootstrap CI spanning zero). % exp_id: qw_rand_s030; B=10000, p=0.012, d=-0.035, negligible
artifacts/_project/paper/results.tex:71:[Omitted long matching line]
artifacts/_project/paper/results.tex:81:[Omitted long matching line]
artifacts/_project/paper/results.tex:86:\caption{Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM). $\widetilde{\Delta}$: median paired difference (importance $-$ random) with bootstrap 95\% CI ($B{=}10{,}000$); $p$: Bonferroni-corrected Wilcoxon signed-rank $p$ ($k{=}4$). $n{=}\placeholder{N\_LLAMA}$ paired problems.}
artifacts/_project/paper/results.tex:92:0.15 & \placeholder{}\; $[\placeholder{}, \placeholder{}]$ & \placeholder{} \\
artifacts/_project/paper/results.tex:93:0.20 & \placeholder{}\; $[\placeholder{}, \placeholder{}]$ & \placeholder{} \\
artifacts/_project/paper/results.tex:94:0.25 & \placeholder{}\; $[\placeholder{}, \placeholder{}]$ & \placeholder{} \\
artifacts/_project/paper/results.tex:95:0.30 & \placeholder{}\; $[\placeholder{}, \placeholder{}]$ & $\mathbf{\placeholder{}}$ \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "7c149951-6a2d-464d-947d-4d6898c95c3e",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "artifacts/_project/paper/main.tex:21:\\newcommand{\\placeholder}[1]{\\textcolor{red}{[#1]}}\nartifacts/_project/paper/discussion.tex:10:[Omitted long matching line]\nartifacts/_project/paper/discussion.tex:15:[Omitted long matching line]\nartifacts/_project/paper/appendix_moved.tex:30:Table~\\ref{tab:qwen-effective-n} reports the per-phase effective sample size for Qwen2.5-7B-Instruct, defined as the number of problems with $|\\mathrm{II}| > 0.001$ in each phase. The mid-phase null rate (\\placeholder{NULL\\_PCT}\\%) reflects problems where compound interaction is absent in intermediate phases; this does not affect the low--high contrast ($\\Delta$) used in the primary analysis.\nartifacts/_project/paper/appendix_moved.tex:35:\\caption{Per-phase effective sample size for Qwen2.5-7B-Instruct ($n_{\\text{total}} = \\placeholder{N\\_QW}$).}\nartifacts/_project/paper/appendix_moved.tex:41:High & \\placeholder{} & \\placeholder{} & \\placeholder{} & \\placeholder{} \\\\\nartifacts/_project/paper/appendix_moved.tex:42:Mid  & \\placeholder{} & \\placeholder{} & \\placeholder{} & \\placeholder{} \\\\\nartifacts/_project/paper/appendix_moved.tex:43:Low  & \\placeholder{} & \\placeholder{} & \\placeholder{} & \\placeholder{} \\\\\nartifacts/_project/paper/appendix_moved.tex:73:The per-problem concordance across models is not significant (median $\\rho = \\placeholder{}$, $p = \\placeholder{}$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking. % exp_id: cross_model_analysis.json (spearman_rho=1.0, gradient_permutation_p=0.043, per_problem_concordance_p=0.926, mean_rho=-0.107)\nartifacts/_project/paper/appendix_moved.tex:76:As a control, random eviction on Qwen yields no systematic phase gradient at three of four sparsity levels (3/4 FAIL), mirroring DeepSeek's 4/4 FAIL pattern. At $s{=}0.30$, Qwen random produces a borderline PASS (permutation $p = 0.012$) but with negligible median difference ($\\widetilde{\\Delta} = \\placeholder{}$, CI spans zero), indicating no meaningful phase modulation. % exp_id: bf16_qw_rand_s015..s030; source: experiment_summary_table.json\nartifacts/_project/paper/abstract.tex:8:Random eviction produces no significant phase modulation in 7/8 conditions; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) shows negligible median difference ($\\widetilde{\\Delta} = \\placeholder{}$), confirming that the severity gradient is strategy-specific, not an inherent property of compound sparsity.\nartifacts/_project/paper/appendix_results.tex:7:The per-problem concordance across models is not significant (median $\\rho = \\placeholder{}$, $p = \\placeholder{}$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking. % exp_id: cross_model_analysis.json (spearman_rho=1.0, gradient_permutation_p=0.043, per_problem_concordance_p=0.926, mean_rho=-0.107)\nartifacts/_project/paper/appendix_results.tex:10:As a control, random eviction on Qwen yields no systematic phase gradient at three of four sparsity levels (3/4 FAIL), mirroring DeepSeek's 4/4 FAIL pattern. At $s{=}0.30$, Qwen random produces a borderline PASS (permutation $p = 0.012$) but with negligible median difference ($\\widetilde{\\Delta} = \\placeholder{}$, CI spans zero), indicating no meaningful phase modulation. % exp_id: bf16_qw_rand_s015..s030; source: experiment_summary_table.json\nartifacts/_project/paper/appendix_disc_analysis.tex:14:Random eviction fails 7/8 paired permutation tests across both models; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) exhibits negligible effect size ($\\widetilde{\\Delta} = \\placeholder{}$). The absence of a phase gradient under random masking isolates the amplification as strategy-specific. % exp_id: bf16_ds_rand_s015..s030, bf16_qw_rand_s015..s030\nartifacts/_project/paper/appendix_disc_analysis.tex:49:A notable exception among the random baselines is the Qwen random condition at $s{=}0.30$, which yields a statistically significant result ($p{=}0.012$) despite negligible effect size ($\\widetilde{\\Delta} = \\placeholder{}$, bootstrap CI spanning zero). % exp_id: qw_rand_s030; B=10000, p=0.012, d=-0.035, negligible\nartifacts/_project/paper/results.tex:71:[Omitted long matching line]\nartifacts/_project/paper/results.tex:81:[Omitted long matching line]\nartifacts/_project/paper/results.tex:86:\\caption{Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM). $\\widetilde{\\Delta}$: median paired difference (importance $-$ random) with bootstrap 95\\% CI ($B{=}10{,}000$); $p$: Bonferroni-corrected Wilcoxon signed-rank $p$ ($k{=}4$). $n{=}\\placeholder{N\\_LLAMA}$ paired problems.}\nartifacts/_project/paper/results.tex:92:0.15 & \\placeholder{}\\; $[\\placeholder{}, \\placeholder{}]$ & \\placeholder{} \\\\\nartifacts/_project/paper/results.tex:93:0.20 & \\placeholder{}\\; $[\\placeholder{}, \\placeholder{}]$ & \\placeholder{} \\\\\nartifacts/_project/paper/results.tex:94:0.25 & \\placeholder{}\\; $[\\placeholder{}, \\placeholder{}]$ & \\placeholder{} \\\\\nartifacts/_project/paper/results.tex:95:0.30 & \\placeholder{}\\; $[\\placeholder{}, \\placeholder{}]$ & $\\mathbf{\\placeholder{}}$ \\\\",
    "numLines": 22
  }
}
```

</details>

---

### Assistant

_source line 65_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive picture. Let me also check the main.tex to see how the paper is structured and if there's anything else.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "2d6d875c-f1f9-4226-89f8-1a54a954221e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ji1XD38WjyC22NgSwaTwjG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1872,
      "cache_read_input_tokens": 56444,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1872
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

Now I have all the information needed. Let me also quickly check the Qwen imp-vs-rand significance caveat situation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "b510affd-4d16-4041-9458-d14bcf456476",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ji1XD38WjyC22NgSwaTwjG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1872,
      "cache_read_input_tokens": 56444,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1872
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

<details open><summary>🔧 Tool call — Grep · `toolu_01WqZxqFS5uGC82cnhtsiYcU`</summary>

```json
{
  "pattern": "imp.vs.rand|importance.vs.random|Qwen.*not.*signif|not.*signif.*Qwen",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "-n": true,
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "17ac4dd9-f879-43b4-b7b2-c3faa3721637",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ji1XD38WjyC22NgSwaTwjG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1872,
      "cache_read_input_tokens": 56444,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1872
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

_source line 68 · 2026-05-15T01:41:08.100Z_

<details><summary>↩ Tool result · `toolu_01WqZxqFS5uGC82cnhtsiYcU`</summary>

```text
artifacts/_project/paper/conclusion.tex:4:[Omitted long matching line]
artifacts/_project/paper/limitations.tex:2:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "392cab34-1246-4b28-8d12-68b7f774ba69",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "artifacts/_project/paper/conclusion.tex:4:[Omitted long matching line]\nartifacts/_project/paper/limitations.tex:2:[Omitted long matching line]",
    "numLines": 2
  }
}
```

</details>

---

### Tool call

_source line 69_

<details open><summary>🔧 Tool call — Read · `toolu_01LgLNWD1bfvuVntYsins1Rk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "ddea9751-6090-4fa8-952f-9da9297e54a4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ji1XD38WjyC22NgSwaTwjG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1872,
      "cache_read_input_tokens": 56444,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1872
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

_source line 70 · 2026-05-15T01:41:08.606Z_

<details><summary>↩ Tool result · `toolu_01LgLNWD1bfvuVntYsins1Rk`</summary>

```text
1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{graphicx}
15	\usepackage{booktabs}
16	\usepackage{enumitem}
17	\usepackage{multirow}
18	
19	\graphicspath{{figures/}}
20	
21	\newcommand{\placeholder}[1]{\textcolor{red}{[#1]}}
22	
23	\title{Phase-Modulated Compound Sparsity:\\Strategy-Dependent Severity Gradients in Reasoning Models}
24	
25	\author{Anonymous}
26	
27	\begin{document}
28	
29	\maketitle
30	
31	\input{abstract}
32	
33	\input{introduction}
34	\input{related_work}
35	\input{background}
36	\input{methodology}
37	\input{results}
38	\input{analysis}
39	\input{discussion}
40	\input{conclusion}
41	
42	\bibliography{references}
43	
44	\section*{Limitations}
45	\input{limitations}
46	
47	\appendix
48	\input{appendix}
49	\input{appendix_moved}
50	\input{appendix_disc_analysis}
51	
52	\end{document}
53	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "f17cc857-5ae9-4c38-903d-1a6e7b9c5b2e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{inconsolata}\n\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{enumitem}\n\\usepackage{multirow}\n\n\\graphicspath{{figures/}}\n\n\\newcommand{\\placeholder}[1]{\\textcolor{red}{[#1]}}\n\n\\title{Phase-Modulated Compound Sparsity:\\\\Strategy-Dependent Severity Gradients in Reasoning Models}\n\n\\author{Anonymous}\n\n\\begin{document}\n\n\\maketitle\n\n\\input{abstract}\n\n\\input{introduction}\n\\input{related_work}\n\\input{background}\n\\input{methodology}\n\\input{results}\n\\input{analysis}\n\\input{discussion}\n\\input{conclusion}\n\n\\bibliography{references}\n\n\\section*{Limitations}\n\\input{limitations}\n\n\\appendix\n\\input{appendix}\n\\input{appendix_moved}\n\\input{appendix_disc_analysis}\n\n\\end{document}\n",
      "numLines": 53,
      "startLine": 1,
      "totalLines": 53
    }
  }
}
```

</details>

---

### Assistant

_source line 71_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive picture. Let me also check if the `appendix_results.tex` is actually included or not. It's not referenced in main.tex.

Looking at main.tex line 50: `\input{appendix_disc_analysis}` but no `\input{appendix_results}`. So appendix_results.tex might be an unused/duplicate file. Let me note that.

Now let me compile the full checklist. Here's what I found:

### Files with n=50 or "50 problems" references:
1. **abstract.tex:6** - "using 50 MATH-500 problems"


2. **methodology.tex:10** - "We use 50 problems stratified from MATH-500"
3. **results.tex:13** - "$n{=}50$ MATH-500 problems" (Table 1 caption)
4. **results.tex:34** - "medians across 50 problems" (Table 2 caption)
5. **appendix_moved.tex:26** - "Four of the 50 problems are excluded" → "n=46 valid problems for Qwen (vs. n=49 for DeepSeek)"

Now I'm looking at the numerical values from the n=50 dataset that need to be updated...

I'm noticing there's a discrepancy between the segment-level medians reported in the aggregate table (0.39, 1.48, 7.16, 14.59) and what appears in the abstract (0.39 to 14.59). Let me check whether the abstract is referencing segment-level or paired medians, since the paired values follow a different progression (0.32→1.15→3.97→9.94). I'm seeing that the paired medians from the Cohen's d table (0.32, 1.15, 3.97, 9.94) match what the paper describes as the per-problem paired differences, and these differ from both the segment-level medians and the permutation test values. The Cohen's d_z values are also scattered across multiple sections of the paper (abstract, introduction, results), and all these numbers will need updating when n changes to 500. I'm tracking the severity gradient multipliers across multiple sections, verifying the crossover points where phase II values reverse between conditions, and checking the random eviction and permutation test statistics that support these findings.

Now I'm examining the LLaMA cross-architecture results, which show much smaller effect sizes around 40× reduction compared to the main findings, along with the Gini coefficient and entropy changes that quantify how the distribution shifts across different sampling strategies.

I'm also tracking down the remaining placeholder values scattered throughout the document—there are still quite a few missing statistical values and table entries that need to be filled in, particularly for the Qwen results, LLaMA statistical tests, and the C5b pilot metrics in the discussion section.

I'm checking whether the paper consistently uses appropriately qualified language around its claims, especially phrases like "partially extends" and "partial support" that appear throughout the abstract, results, and limitations sections.

For the future work scope, the pilot experiment results are properly framed as a promising direction, though the placeholder values still need to be filled in. The rebuttal comments also reference this as future work, which seems appropriately bounded.

On the Qwen implementation versus random comparison, I'm not finding an explicit caveat about it being non-significant in the paper itself. The results do show Qwen reproduces the monotonic severity gradient and that the effect size becomes reliable at higher sample sizes, but I need to verify whether the paper explicitly states the imp-vs-rand comparison lacks significance. I'm realizing the Qwen results in the paper only report within-importance phase gradients, not the imp-vs-rand comparison that D058 flags as needing n=500 confirmation. The permutation test showing significance is only for DeepSeek in the appendix, so while the constraint about not claiming Qwen significance before n=500 data exists, the paper doesn't actually make that claim yet. But I should still flag this as a potential risk point to monitor.

For the sample size mixing issue, when I update to n=500 results, DeepSeek and Qwen numbers will shift across all tables while LLaMA stays at n=50 since only the c2 experiments scaled up. The entropy analysis from c4 remains at n=30 and c5b_pilot stays unchanged, so I need to make sure the different sample sizes are explicitly stated to avoid confusion.

Now I'm identifying everything that needs updating with the new sample sizes: all the DeepSeek and Qwen medians, effect sizes, statistical test values, cross-model comparisons, severity gradients, and crossover points, plus the actual sample counts which will shift from around 49 to 490+ for DeepSeek and 46 to 460+ for Qwen after accounting for exclusions.

What stays constant are the LLaMA results, entropy analysis, pilot data, and the underlying formulas. I'm organizing the updates by priority: the headline numbers in the abstract, intro, and main results tables are critical, followed by supporting analyses like the cross-model comparisons and permutation tests, then I'll check whether the Qwen caveats and other conditional sections need revision.

I also need to flag the sample size inconsistencies—keeping LLaMA at n=50 and entropy at n=30 while being explicit about where n=500 applies, and regenerating figures as needed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "bc612bc9-2afc-4e16-a31f-139c1432ba98",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ZG5wyf9hBNeg8NqPbiuca",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 905,
      "cache_read_input_tokens": 58316,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 905
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

_source line 72_

I have all the information needed. Now compiling the checklist.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "dcb74256-bd74-41d3-bd83-06a018ae093e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ZG5wyf9hBNeg8NqPbiuca",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 905,
      "cache_read_input_tokens": 58316,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 905
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

_source line 73_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file · `toolu_01DmuG4fs5LktTTXyLT6H9j2`</summary>

````json
{
  "project": "phase-gated-compound-sparse",
  "file": "artifacts/paper_update_checklist.md",
  "content": "# Paper Update Checklist: n=50 → n=500\n\n> 生成时间: 2026-05-15 | 适用实验: c2_n500_deepseek + c2_qw_n500 (C7)\n> 约束: median + bootstrap CI 为主指标 (D054); d_z 分场景 (D059); Qwen imp-vs-rand 不claim显著直到n=500确认 (D058); C8=partially_confirmed (D060); C5b=future_work (D056)\n\n---\n\n## 优先级说明\n- **P0**: 核心数字，读者第一眼看到，必须同步更新\n- **P1**: 支撑性数字/表格，与 P0 有数据依赖\n- **P2**: 条件性更新（取决于 n=500 结果）\n- **P3**: 一致性检查，防止 n=50/n=500 混用\n\n---\n\n## P0: 核心数字更新\n\n### 1. methodology.tex:10 — 样本量\n```\n当前: \"We use 50 problems stratified from MATH-500\"\n更新: → 500 problems (n=500 的具体描述，包括 stratification 方式)\n```\n\n### 2. abstract.tex:6 — 样本量\n```\n当前: \"using 50 MATH-500 problems\"\n更新: → 500 MATH-500 problems\n```\n\n### 3. abstract.tex:7 — DeepSeek 主指标\n```\n当前: \"median Interaction Index difference...from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired Cohen's $d_z$ growing from $0.44$ (small) to $0.80$ (large)\"\n更新: → 用 n=500 segment-level median diff + paired d_z 替换\n注意: 0.39/14.59 是 segment-level medians；d_z 0.44/0.80 是 paired d_z。两组数据来源不同，都需更新。\n```\n\n### 4. introduction.tex:14 — DeepSeek 主指标（与 abstract 一致）\n```\n当前: \"median phase difference rises from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$ ($d_z$: $0.44 \\to 0.80$)\"\n更新: → 同 abstract\n```\n\n### 5. results.tex:8,13,19-20 — Tab aggregate-ii（DeepSeek segment-level Δ）\n```\n当前 Importance: 0.39, 1.48, 7.16, 14.59\n当前 Random: 0.01, -0.02, 0.54, 1.54\ncaption \"$n{=}50$\" → $n{=}500$ (或实际有效 n)\n更新: → 全部替换为 n=500 值\n```\n\n### 6. results.tex:34,40-50 — Tab main-results（DeepSeek 全 per-phase 分解）\n```\n当前 (importance, 4 sparsity × 3 phases + Δ + G):\n  s015: II_high=0.006, II_mid=0.081, II_low=0.398, Δ=0.39, G=69\n  s020: II_high=0.015, II_mid=0.203, II_low=1.496, Δ=1.48, G=103\n  s025: II_high=0.032, II_mid=1.118, II_low=7.196, Δ=7.16, G=222\n  s030: II_high=0.053, II_mid=2.283, II_low=14.639, Δ=14.59, G=274\n当前 (random, 4 sparsity × 3 phases + Δ + G):\n  s015: 0.093, 0.097, 0.103, 0.01, 1.1\n  s020: 0.292, 0.350, 0.276, -0.02, 0.9\n  s025: 0.818, 0.932, 1.363, 0.54, 1.7\n  s030: 2.503, 2.592, 4.041, 1.54, 1.6\ncaption \"50 problems\" → 500 problems\n更新: → 全部替换为 n=500 值\n```\n\n### 7. results.tex:106,117-120 — Tab cohens-d（DS + QW paired d_z + Δ̃[CI]）\n```\n当前 DS: d_z 0.44/0.52/0.68/0.80; Δ̃ 0.32[0.20,0.47] / 1.15[0.66,1.26] / 3.97[2.83,5.29] / 9.94[8.39,16.65]\n当前 QW: d_z 0.28/0.55/0.89/1.02; Δ̃ 0.05[-0.01,0.11] / 0.21[0.07,0.40] / 1.11[0.61,1.47] / 2.62[1.72,3.65]\n更新: → 全部替换为 n=500 值\n关键: QW s015 CI 当前包含零 → n=500 后检查是否仍包含零（影响 onset threshold 叙事）\n```\n\n### 8. conclusion.tex:4 — 核心数字复述\n```\n当前: \"severity gradient grows from $69{\\times}$ to $274{\\times}$...($d_z$: $0.44 \\to 0.80$)\"\n更新: → 与 results 一致\n```\n\n### 9. discussion.tex:5 — severity gradient + crossover 复述\n```\n当前: \"severity gradient ($69$--$274{\\times}$)\"\n当前: crossover 数字 \"0.032 vs 0.818\", \"7.196 vs 1.363\"\n更新: → 与 results 一致\n```\n\n### 10. results.tex:29 + 58 — G 值 + fig1 caption\n```\n当前: G \"from $69{\\times}$ at $s{=}0.15$ to $274{\\times}$ at $s{=}0.30$\"\n当前 fig1 caption: \"$69{\\times}$ to $274{\\times}$\"\n更新: → n=500 G 值\n```\n\n---\n\n## P1: 支撑性数字更新\n\n### 11. results.tex:66 — Crossover 数字\n```\n当前: \"importance high_phase=0.032 < random=0.818, importance low_phase=7.196 > random=1.363\"\nreversal \"5.3×\"\n更新: → n=500 crossover 值\n```\n\n### 12. results.tex:71 — Qwen cross-model 段落\n```\n当前: \"Δ increases from 0.04 at s=0.15 to 2.94 at s=0.30...d_z ≥ 0.55...d_z=0.28 CI includes zero\"\n更新: → n=500 Qwen 值\n关键: 检查 s015 d_z 是否仍 marginal，onset threshold 是否仍 s≥0.20\n```\n\n### 13. appendix_moved.tex:26 — Qwen/DS 有效 n\n```\n当前: \"Four of the 50 problems...n=46 valid problems for Qwen (vs. n=49 for DeepSeek)\"\n更新: → n=500 的排除数和有效 n\n```\n\n### 14. appendix_moved.tex:59-60 — Tab cross-model Qwen Δ\n```\n当前 DS: 0.39, 1.48, 7.16, 14.59\n当前 QW: 0.04, 0.23, 1.27, 2.94\n更新: → n=500 值\n```\n\n### 15. appendix_moved.tex:88,99-102 — Tab permutation（DeepSeek permutation test）\n```\n当前: n=49; observed Δ̃ 0.37[0.19,0.62], 0.97[0.69,1.49], 3.34[1.66,6.64], 9.85[6.70,16.29]\ncaption \"$n{=}49$\"\n更新: → n=500 permutation test 值\n```\n\n### 16. results.tex:104 — permutation test 段落引用\n```\n当前: \"observed median differences increasing monotonically from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$\"\n更新: → 与 Tab permutation 一致\n```\n\n### 17. appendix_moved.tex:11 — crossover 详细数字\n```\n当前: \"reversal magnitude of $3.9{\\times}$ at $s{=}0.15$, $5.4{\\times}$ at $s{=}0.20$, $5.3{\\times}$ at $s{=}0.25$, and $3.6{\\times}$ at $s{=}0.30$\"\n更新: → n=500 reversal magnitudes\n```\n\n### 18. appendix_disc_analysis.tex:46-47 — permutation CI + skewness 统计\n```\n当前: \"mean/median ratio ~1.6:1 at s=0.30\"\n当前: \"permutation CIs: s015=[0.19,0.62], s020=[0.69,1.49], s025=[1.66,6.64], s030=[6.70,16.29]\"\n更新: → n=500 值\n```\n\n### 19. abstract.tex:10 — LLaMA cross-arch 段落\n```\n当前: \"Δ̃: 0.020→0.356; s=0.30 Wilcoxon p_Bonf=0.029\"\n注意: LLaMA 实验仍为 n=50，数字不变，但需检查措辞是否暗示与 DS/QW 同一 n\n```\n\n### 20. 图表重新生成\n```\nfig1_dose_response.pdf — G vs s 曲线（P0 依赖）\nfig3_crossover.pdf — crossover bar chart\nfig4_bootstrap.pdf — permutation forest plot\nfig5_crossmodel.pdf — cross-model Δ comparison\n所有图需用 n=500 数据重新生成\n```\n\n---\n\n## P2: 条件性更新\n\n### 21. D058: Qwen imp-vs-rand 显著性\n```\n当前状态: 论文未报告 Qwen imp-vs-rand permutation test（只报告了 DeepSeek）\n约束: n=500 前不得 claim Qwen imp-vs-rand 显著\n行动:\n  - 若 n=500 Qwen imp-vs-rand 显著 → 可添加 Qwen permutation test 表格，strengthens C1\n  - 若仍不显著 → 在 cross-model 段落加 caveat，或维持当前策略（只报 within-importance gradient）\n检查文件: results.tex:71, appendix_results.tex:10\n```\n\n### 22. D059: d_z 报告策略\n```\n约束: within-importance d_z 保留; 涉及 random 只报方向\n行动: 检查 n=500 后是否有新的 imp-vs-rand d_z 值需要报告，确保遵守\"只报方向\"规则\n影响文件: results.tex, appendix_moved.tex\n```\n\n### 23. C2 预注册: Qwen s015 onset threshold\n```\n当前: paper_framing 预注册 \"n=500 后若 QW s015 CI 仍跨零，叙事改为 'compound effect emerges above threshold sparsity (~s020)'\"\n检查: results.tex:71 \"marginal at s=0.15\" + Tab cohens-d QW s015 行\n行动:\n  - 若 n=500 QW s015 CI 不跨零 → onset = s≥0.15，更新叙事\n  - 若仍跨零 → 保持 \"emerges above ~s020\" 叙事\n```\n\n### 24. Placeholder 值填充\n以下 \\placeholder{} 标记需用 n=50 或 n=500 数据填充:\n\n| 文件:行 | Placeholder | 数据来源 |\n|---------|-------------|----------|\n| abstract.tex:8 | Qwen rand s030 Δ̃ | bf16_qw_rand_s030 |\n| results.tex:71 | NULL_PCT | Qwen per-phase null rate |\n| results.tex:81 | LLaMA random Wilcoxon p | c3_llama |\n| results.tex:86 | N_LLAMA | c3_llama (n=49?) |\n| results.tex:92-95 | 整个 LLaMA 表格 (12 cells) | c3_llama |\n| discussion.tex:10 | ORACLE_PCT, ORACLE_P, HEUR_PCT, HEUR_P | c5b_pilot |\n| discussion.tex:15 | LLaMA random Wilcoxon p | c3_llama |\n| appendix_moved.tex:30 | NULL_PCT | Qwen null rate |\n| appendix_moved.tex:35 | N_QW | Qwen valid n |\n| appendix_moved.tex:41-43 | Qwen effective n 表格 (12 cells) | Qwen per-phase data |\n| appendix_moved.tex:73 | ρ, p (per-problem concordance) | cross_model_analysis.json |\n| appendix_moved.tex:76 | Qwen rand s030 Δ̃ | bf16_qw_rand_s030 |\n| appendix_results.tex:7 | 同 appendix_moved.tex:73 (重复文件) | cross_model_analysis.json |\n| appendix_results.tex:10 | 同 appendix_moved.tex:76 (重复文件) | bf16_qw_rand_s030 |\n| appendix_disc_analysis.tex:14 | Qwen rand s030 Δ̃ | bf16_qw_rand_s030 |\n| appendix_disc_analysis.tex:49 | Qwen rand s030 Δ̃ | qw_rand_s030 |\n\n注意: appendix_results.tex 未被 main.tex \\input，内容与 appendix_moved.tex 重复。建议清理或统一。\n\n---\n\n## P3: 一致性与混用风险\n\n### 25. n=50 / n=500 混用风险点\n\n| 数据源 | 当前 n | 更新后 n | 风险 |\n|--------|--------|---------|------|\n| DeepSeek importance/random (c2) | 50 | **500** | 主表全部替换 |\n| Qwen importance/random (c2) | 50 | **500** | 主表全部替换 |\n| LLaMA cross-arch (c3_llama) | 50 | **50 不变** | ⚠️ 需在 §5.5/Limitations 明确标注 n=50 |\n| Entropy/discrimination (c4) | 30 | **30 不变** | ⚠️ Analysis §6 数字不变，但样本量不一致需说明 |\n| c5b_pilot | ? | **不变** | Discussion §7 pilot 数字不变 |\n| Permutation test | 49(DS)/46(QW) | **~490/~460** | 替换 |\n| Cross-model comparison | 50 | **500** | 替换 |\n\n### 26. 需要显式声明不同 n 的位置\n```\n- results.tex §5.5 (cross-arch): 已有 \"n=\\placeholder{N_LLAMA}\" → 确保说明这是 n=50\n- analysis.tex §6: 当前未提及 c4 的 n=30 → 建议添加注脚\n- discussion.tex §7 (pilot): 当前未提及 pilot 样本量 → 建议添加\n- limitations.tex: 添加说明 \"LLaMA/mechanism 分析基于 n=50/30 子集\"\n- abstract.tex: \"50 MATH-500 problems\" → 需注明 LLaMA 仍用 50\n  或改为 \"up to 500 MATH-500 problems\"\n```\n\n### 27. C8 partially_confirmed 限定语检查 ✅\n已确认以下位置使用了合格限定语:\n- abstract.tex:10 — \"mixed but directionally consistent evidence\"\n- results.tex:79 — \"partially confirming the cross-architecture hypothesis\"\n- discussion.tex:14-15 — \"partial support...substantially weaker\"\n- conclusion.tex:4 — \"partially extends cross-architecture\"\n- limitations.tex:1-2 — \"partially confirms...substantially weaker\"\n- appendix_disc_analysis.tex:33 — \"partial confirmation\"\n**无需修改（除非 n=500 改变了 DS/QW 数据使 LLaMA 对比幅度变化）**\n\n### 28. C5b future_work 标注检查 ✅\n已确认:\n- discussion.tex:10 — pilot 结果 + \"promising direction for future work\"\n- appendix_disc_analysis.tex:57,62 — REBUTTAL comments 标注 future work\n**无需修改，但 \\placeholder{} 值需填充**\n\n### 29. Qwen random s030 p=0.012 d=-0.04 caveat 检查\n出现在以下位置（均标注为 negligible/no meaningful modulation）:\n- abstract.tex:8 ✅\n- appendix_moved.tex:76 ✅\n- appendix_results.tex:10 ✅\n- appendix_disc_analysis.tex:14,49 ✅\n**n=500 后需检查: Qwen rand s030 是否仍为 borderline/negligible，或变显著 → 影响 \"7/8 FAIL\" 叙事**\n\n---\n\n## 执行顺序建议\n\n1. **等 n=500 数据产出** → 运行统计分析脚本生成新的 experiment_summary_table.json, cohens_d, permutation_test_results 等\n2. **P0 先行**: 更新主表 → abstract → intro → conclusion（确保核心叙事一致）\n3. **P1 跟进**: 更新附录表格 → 重新生成 4 张图\n4. **P2 条件分支**: 根据 QW s015 CI / QW imp-vs-rand 结果决定叙事调整\n5. **P3 最后检查**: 全文搜索 \"n=50\" / \"50 problems\" / \"n=49\" / \"n=46\" 确保无残留\n6. **填充 \\placeholder{}**: LLaMA 表格 + 各处 Qwen rand Δ̃ + pilot 数字 + concordance ρ/p\n7. **LaTeX 编译验证**: 确保无 red placeholder 残留\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "2e842374-63aa-4e82-8035-b1b0ee58b336",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ZG5wyf9hBNeg8NqPbiuca",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 905,
      "cache_read_input_tokens": 58316,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 905
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

_source line 74 · 2026-05-15T01:44:04.861Z_

<details><summary>↩ Tool result · `toolu_01DmuG4fs5LktTTXyLT6H9j2`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"file 'artifacts/paper_update_checklist.md' is not writable via save_project_file. Writable: ['memory.md', 'paper_framing.md', 'writing_plan.yaml'].\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "a6829948-d6e4-4f1f-8e7d-6203f7f8587a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"file 'artifacts/paper_update_checklist.md' is not writable via save_project_file. Writable: ['memory.md', 'paper_framing.md', 'writing_plan.yaml'].\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"file 'artifacts/paper_update_checklist.md' is not writable via save_project_file. Writable: ['memory.md', 'paper_framing.md', 'writing_plan.yaml'].\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 75_

<details><summary>Logged reasoning block</summary>

```text
The MCP tool can't write to artifacts/paper_update_checklist.md. I need to write it directly to disk instead.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "691c8cbf-cb9c-4c7a-97a3-3188ecbf884e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016xxhP4395xafE8ERqgttqp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8889,
      "cache_read_input_tokens": 59221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8889
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

_source line 76_

MCP 工具不支持写 artifacts，直接写文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "b3bb027a-f8d8-48cb-93dd-fecd6978fc79",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016xxhP4395xafE8ERqgttqp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8889,
      "cache_read_input_tokens": 59221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8889
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

_source line 77_

<details open><summary>🔧 Tool call — Bash · `toolu_01LZCiX6MC9zXusx3K5oKMdv`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "f5783449-a525-45f6-99cb-7ac839811971",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016xxhP4395xafE8ERqgttqp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8889,
      "cache_read_input_tokens": 59221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8889
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

_source line 78 · 2026-05-15T01:44:11.462Z_

<details><summary>↩ Tool result · `toolu_01LZCiX6MC9zXusx3K5oKMdv`</summary>

```text
_project
analysis_pipeline_audit.md
analysis_pipeline_readiness.md
analysis_pipeline_verification.md
analyze_c2_n500.py
bf16_qw_imp_failures_diagnosis.md
bf16_qw_rand_s015
bf16_qw_rand_s020
bf16_qw_rand_s025
bf16_qw_rand_s030
bootstrap_phase_gradient.py
c2_n500_deepseek
c2_n500_paper_update_checklist.md
c2_progress_report.md
c2_progress_snapshot.json
c2_qw_n500_investigation.md
c3_llama
c3_llama_results.json
c5b_framing_proposal.md
c5b_pilot
c5b_pilot_design.md
c5b_pilot_diagnosis.md
compute_multiplicative_null.py
consistency_audit_final.md
consistency_audit_report.md
consistency_report.md
dream_reports
gpu_check_loop7.md
literature_scan_20260515.md
literature_scan_phase_adaptive.md
m1_phase_segmentation_analysis.md
m2_m4_code_readiness.md
magnitude_crossover_novelty_check.md
manifest.yaml
mechanistic_explanation.md
mid_sparsity_gap_analysis.md
mvp_ii_analysis.md
mvp_ii_profiling_v2
mvp_ii_profiling_v3
mvp_ii_v3_analysis.md
mvp_interaction_index_profiling
n500_analysis_pipeline_ready.md
n500_paper_patch_plan.md
n500_paper_update_FINAL.md
n500_paper_update_checklist.md
n500_paper_update_plan.md
n500_progress_20260515_0632.md
n500_progress_check.md
n500_update_checklist.md
number_consistency_audit_v2.md
pacs
paper_n500_update_checklist.md
paper_n500_update_plan.md
qwen_kill_investigation.md
qwen_status_check.md
reference_audit.md
reference_audit_report.md
report_analysis_pipeline_ready.md
report_process_check.md
review_issues.yaml
review_reports
v5_status_check.md
w1w5_audit_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "d814b674-83b8-44aa-a6e1-8a6c15f18f46",
  "tool_use_result": {
    "stdout": "_project\nanalysis_pipeline_audit.md\nanalysis_pipeline_readiness.md\nanalysis_pipeline_verification.md\nanalyze_c2_n500.py\nbf16_qw_imp_failures_diagnosis.md\nbf16_qw_rand_s015\nbf16_qw_rand_s020\nbf16_qw_rand_s025\nbf16_qw_rand_s030\nbootstrap_phase_gradient.py\nc2_n500_deepseek\nc2_n500_paper_update_checklist.md\nc2_progress_report.md\nc2_progress_snapshot.json\nc2_qw_n500_investigation.md\nc3_llama\nc3_llama_results.json\nc5b_framing_proposal.md\nc5b_pilot\nc5b_pilot_design.md\nc5b_pilot_diagnosis.md\ncompute_multiplicative_null.py\nconsistency_audit_final.md\nconsistency_audit_report.md\nconsistency_report.md\ndream_reports\ngpu_check_loop7.md\nliterature_scan_20260515.md\nliterature_scan_phase_adaptive.md\nm1_phase_segmentation_analysis.md\nm2_m4_code_readiness.md\nmagnitude_crossover_novelty_check.md\nmanifest.yaml\nmechanistic_explanation.md\nmid_sparsity_gap_analysis.md\nmvp_ii_analysis.md\nmvp_ii_profiling_v2\nmvp_ii_profiling_v3\nmvp_ii_v3_analysis.md\nmvp_interaction_index_profiling\nn500_analysis_pipeline_ready.md\nn500_paper_patch_plan.md\nn500_paper_update_FINAL.md\nn500_paper_update_checklist.md\nn500_paper_update_plan.md\nn500_progress_20260515_0632.md\nn500_progress_check.md\nn500_update_checklist.md\nnumber_consistency_audit_v2.md\npacs\npaper_n500_update_checklist.md\npaper_n500_update_plan.md\nqwen_kill_investigation.md\nqwen_status_check.md\nreference_audit.md\nreference_audit_report.md\nreport_analysis_pipeline_ready.md\nreport_process_check.md\nreview_issues.yaml\nreview_reports\nv5_status_check.md\nw1w5_audit_report.md",
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

_source line 79_

<details open><summary>🔧 Tool call — Write · `toolu_012paCFDcowLaVpDqwq2aJMH`</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/paper_update_checklist.md",
  "content": "# Paper Update Checklist: n=50 → n=500\n\n> 生成时间: 2026-05-15 | 适用实验: c2_n500_deepseek + c2_qw_n500 (C7)\n> 约束: median + bootstrap CI 为主指标 (D054); d_z 分场景 (D059); Qwen imp-vs-rand 不claim显著直到n=500确认 (D058); C8=partially_confirmed (D060); C5b=future_work (D056)\n\n---\n\n## 优先级说明\n- **P0**: 核心数字，读者第一眼看到，必须同步更新\n- **P1**: 支撑性数字/表格，与 P0 有数据依赖\n- **P2**: 条件性更新（取决于 n=500 结果）\n- **P3**: 一致性检查，防止 n=50/n=500 混用\n\n---\n\n## P0: 核心数字更新\n\n### 1. methodology.tex:10 — 样本量\n```\n当前: \"We use 50 problems stratified from MATH-500\"\n更新: → 500 problems (n=500 的具体描述，包括 stratification 方式)\n```\n\n### 2. abstract.tex:6 — 样本量\n```\n当前: \"using 50 MATH-500 problems\"\n更新: → 500 MATH-500 problems\n```\n\n### 3. abstract.tex:7 — DeepSeek 主指标\n```\n当前: \"median Interaction Index difference...from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired Cohen's $d_z$ growing from $0.44$ (small) to $0.80$ (large)\"\n更新: → 用 n=500 segment-level median diff + paired d_z 替换\n注意: 0.39/14.59 是 segment-level medians；d_z 0.44/0.80 是 paired d_z。两组数据来源不同，都需更新。\n```\n\n### 4. introduction.tex:14 — DeepSeek 主指标（与 abstract 一致）\n```\n当前: \"median phase difference rises from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$ ($d_z$: $0.44 \\to 0.80$)\"\n更新: → 同 abstract\n```\n\n### 5. results.tex:8,13,19-20 — Tab aggregate-ii（DeepSeek segment-level Δ）\n```\n当前 Importance: 0.39, 1.48, 7.16, 14.59\n当前 Random: 0.01, -0.02, 0.54, 1.54\ncaption \"$n{=}50$\" → $n{=}500$ (或实际有效 n)\n更新: → 全部替换为 n=500 值\n```\n\n### 6. results.tex:34,40-50 — Tab main-results（DeepSeek 全 per-phase 分解）\n```\n当前 (importance, 4 sparsity × 3 phases + Δ + G):\n  s015: II_high=0.006, II_mid=0.081, II_low=0.398, Δ=0.39, G=69\n  s020: II_high=0.015, II_mid=0.203, II_low=1.496, Δ=1.48, G=103\n  s025: II_high=0.032, II_mid=1.118, II_low=7.196, Δ=7.16, G=222\n  s030: II_high=0.053, II_mid=2.283, II_low=14.639, Δ=14.59, G=274\n当前 (random, 4 sparsity × 3 phases + Δ + G):\n  s015: 0.093, 0.097, 0.103, 0.01, 1.1\n  s020: 0.292, 0.350, 0.276, -0.02, 0.9\n  s025: 0.818, 0.932, 1.363, 0.54, 1.7\n  s030: 2.503, 2.592, 4.041, 1.54, 1.6\ncaption \"50 problems\" → 500 problems\n更新: → 全部替换为 n=500 值\n```\n\n### 7. results.tex:106,117-120 — Tab cohens-d（DS + QW paired d_z + Δ̃[CI]）\n```\n当前 DS: d_z 0.44/0.52/0.68/0.80; Δ̃ 0.32[0.20,0.47] / 1.15[0.66,1.26] / 3.97[2.83,5.29] / 9.94[8.39,16.65]\n当前 QW: d_z 0.28/0.55/0.89/1.02; Δ̃ 0.05[-0.01,0.11] / 0.21[0.07,0.40] / 1.11[0.61,1.47] / 2.62[1.72,3.65]\n更新: → 全部替换为 n=500 值\n关键: QW s015 CI 当前包含零 → n=500 后检查是否仍包含零（影响 onset threshold 叙事）\n```\n\n### 8. conclusion.tex:4 — 核心数字复述\n```\n当前: \"severity gradient grows from $69{\\times}$ to $274{\\times}$...($d_z$: $0.44 \\to 0.80$)\"\n更新: → 与 results 一致\n```\n\n### 9. discussion.tex:5 — severity gradient + crossover 复述\n```\n当前: \"severity gradient ($69$--$274{\\times}$)\"\n当前: crossover 数字 \"0.032 vs 0.818\", \"7.196 vs 1.363\"\n更新: → 与 results 一致\n```\n\n### 10. results.tex:29 + 58 — G 值 + fig1 caption\n```\n当前: G \"from $69{\\times}$ at $s{=}0.15$ to $274{\\times}$ at $s{=}0.30$\"\n当前 fig1 caption: \"$69{\\times}$ to $274{\\times}$\"\n更新: → n=500 G 值\n```\n\n---\n\n## P1: 支撑性数字更新\n\n### 11. results.tex:66 — Crossover 数字\n```\n当前: \"importance high_phase=0.032 < random=0.818, importance low_phase=7.196 > random=1.363\"\nreversal \"5.3×\"\n更新: → n=500 crossover 值\n```\n\n### 12. results.tex:71 — Qwen cross-model 段落\n```\n当前: \"Δ increases from 0.04 at s=0.15 to 2.94 at s=0.30...d_z ≥ 0.55...d_z=0.28 CI includes zero\"\n更新: → n=500 Qwen 值\n关键: 检查 s015 d_z 是否仍 marginal，onset threshold 是否仍 s≥0.20\n```\n\n### 13. appendix_moved.tex:26 — Qwen/DS 有效 n\n```\n当前: \"Four of the 50 problems...n=46 valid problems for Qwen (vs. n=49 for DeepSeek)\"\n更新: → n=500 的排除数和有效 n\n```\n\n### 14. appendix_moved.tex:59-60 — Tab cross-model Qwen Δ\n```\n当前 DS: 0.39, 1.48, 7.16, 14.59\n当前 QW: 0.04, 0.23, 1.27, 2.94\n更新: → n=500 值\n```\n\n### 15. appendix_moved.tex:88,93,99-102 — Tab permutation（DeepSeek permutation test）\n```\n当前: n=49; observed Δ̃ 0.37[0.19,0.62], 0.97[0.69,1.49], 3.34[1.66,6.64], 9.85[6.70,16.29]\ncaption \"$n{=}49$\"\n更新: → n=500 permutation test 值\n```\n\n### 16. results.tex:104 — permutation test 段落引用\n```\n当前: \"observed median differences increasing monotonically from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$\"\n更新: → 与 Tab permutation 一致\n```\n\n### 17. appendix_moved.tex:11 — crossover 详细数字\n```\n当前: \"reversal magnitude of $3.9{\\times}$ at $s{=}0.15$, $5.4{\\times}$ at $s{=}0.20$, $5.3{\\times}$ at $s{=}0.25$, and $3.6{\\times}$ at $s{=}0.30$\"\n更新: → n=500 reversal magnitudes\n```\n\n### 18. appendix_disc_analysis.tex:46-47 — permutation CI + skewness 统计\n```\n当前: \"mean/median ratio ~1.6:1 at s=0.30\"\n当前: \"permutation CIs: s015=[0.19,0.62], s020=[0.69,1.49], s025=[1.66,6.64], s030=[6.70,16.29]\"\n当前 (line 11): \"high-phase II rises to 0.105 at s=0.35\"\n更新: → n=500 值 (s035 supplementary 是否也需更新取决于是否重跑)\n```\n\n### 19. abstract.tex:10 — LLaMA cross-arch 段落\n```\n当前: \"Δ̃: 0.020→0.356; s=0.30 Wilcoxon p_Bonf=0.029\"\n注意: LLaMA 实验仍为 n=50，数字不变，但需检查措辞是否暗示与 DS/QW 同一 n\n```\n\n### 20. 图表重新生成\n```\nfig1_dose_response.pdf — G vs s 曲线（P0 依赖）\nfig3_crossover.pdf — crossover bar chart\nfig4_bootstrap.pdf — permutation forest plot\nfig5_crossmodel.pdf — cross-model Δ comparison\n所有图需用 n=500 数据重新生成\n```\n\n---\n\n## P2: 条件性更新\n\n### 21. D058: Qwen imp-vs-rand 显著性\n```\n当前状态: 论文未报告 Qwen imp-vs-rand permutation test（只报告了 DeepSeek）\n约束: n=500 前不得 claim Qwen imp-vs-rand 显著\n行动:\n  - 若 n=500 Qwen imp-vs-rand 显著 → 可添加 Qwen permutation test 表格，strengthens C1\n  - 若仍不显著 → 在 cross-model 段落加 caveat，或维持当前策略（只报 within-importance gradient）\n检查文件: results.tex:71, appendix_results.tex:10\n```\n\n### 22. D059: d_z 报告策略\n```\n约束: within-importance d_z 保留; 涉及 random 只报方向\n行动: 检查 n=500 后是否有新的 imp-vs-rand d_z 值需要报告，确保遵守\"只报方向\"规则\n影响文件: results.tex, appendix_moved.tex\n```\n\n### 23. C2 预注册: Qwen s015 onset threshold\n```\n当前: paper_framing 预注册 \"n=500 后若 QW s015 CI 仍跨零，叙事改为 'compound effect emerges above threshold sparsity (~s020)'\"\n检查: results.tex:71 \"marginal at s=0.15\" + Tab cohens-d QW s015 行\n行动:\n  - 若 n=500 QW s015 CI 不跨零 → onset = s≥0.15，更新叙事\n  - 若仍跨零 → 保持 \"emerges above ~s020\" 叙事\n```\n\n### 24. Placeholder 值填充\n以下 \\placeholder{} 标记需用实际数据填充:\n\n| 文件:行 | Placeholder | 数据来源 | n=500影响? |\n|---------|-------------|----------|-----------|\n| abstract.tex:8 | Qwen rand s030 Δ̃ | bf16_qw_rand_s030 | 是 |\n| results.tex:71 | NULL_PCT | Qwen per-phase null rate | 是 |\n| results.tex:81 | LLaMA random Wilcoxon p | c3_llama | 否(n=50) |\n| results.tex:86 | N_LLAMA | c3_llama | 否(n=50) |\n| results.tex:92-95 | 整个 LLaMA 表格 (12 cells) | c3_llama | 否(n=50) |\n| discussion.tex:10 | ORACLE_PCT, ORACLE_P, HEUR_PCT, HEUR_P | c5b_pilot | 否 |\n| discussion.tex:15 | LLaMA random Wilcoxon p | c3_llama | 否(n=50) |\n| appendix_moved.tex:30 | NULL_PCT | Qwen null rate | 是 |\n| appendix_moved.tex:35 | N_QW | Qwen valid n | 是 |\n| appendix_moved.tex:41-43 | Qwen effective n 表格 (12 cells) | Qwen per-phase data | 是 |\n| appendix_moved.tex:73 | ρ, p (per-problem concordance) | cross_model_analysis.json | 是 |\n| appendix_moved.tex:76 | Qwen rand s030 Δ̃ | bf16_qw_rand_s030 | 是 |\n| appendix_results.tex:7 | 同 appendix_moved.tex:73 (重复!) | cross_model_analysis.json | 是 |\n| appendix_results.tex:10 | 同 appendix_moved.tex:76 (重复!) | bf16_qw_rand_s030 | 是 |\n| appendix_disc_analysis.tex:14 | Qwen rand s030 Δ̃ | bf16_qw_rand_s030 | 是 |\n| appendix_disc_analysis.tex:49 | Qwen rand s030 Δ̃ | qw_rand_s030 | 是 |\n\n⚠️ appendix_results.tex 未被 main.tex \\input，内容与 appendix_moved.tex §Cross-Model 重复。建议删除或统一。\n\n---\n\n## P3: 一致性与混用风险\n\n### 25. n=50 / n=500 混用风险矩阵\n\n| 数据源 | 当前 n | 更新后 n | 混用风险 |\n|--------|--------|---------|---------|\n| DeepSeek importance/random (c2) | 50 | **500** | 主表全部替换 |\n| Qwen importance/random (c2) | 50 | **500** | 主表全部替换 |\n| LLaMA cross-arch (c3_llama) | 50 | **50 不变** | ⚠️ 高风险 |\n| Entropy/discrimination (c4) | 30 | **30 不变** | ⚠️ 中风险 |\n| c5b_pilot | ~50 | **不变** | 低风险 |\n| Permutation test | 49(DS)/46(QW) | **~490/~460** | 替换 |\n| Cross-model comparison | 50 | **500** | 替换 |\n\n### 26. 需要显式声明不同 n 的位置\n```\n- abstract.tex: \"50 MATH-500 problems\" → 改为区分 DS/QW (n=500) vs LLaMA (n=50)\n  建议: \"500 MATH-500 problems (50 for cross-architecture validation)\"\n- results.tex §5.5 (cross-arch): 已有 \"n=\\placeholder{N_LLAMA}\" → 填入 49 或 50，确保读者知道这不是 500\n- analysis.tex §6: 当前未提及 c4 的样本量 → 建议添加脚注 \"(30 problems per model)\"\n- discussion.tex §7 (pilot): 当前未提及 pilot 样本量 → 建议添加\n- methodology.tex: 需说明 \"500 problems for primary experiments; 50 for cross-architecture (LLaMA)\"\n- limitations.tex: 添加 \"LLaMA 和 mechanism 分析基于 n=50/30 子集\"\n```\n\n### 27. C8 partially_confirmed 限定语检查 ✅\n已确认以下位置使用了合格限定语:\n- abstract.tex:10 — \"mixed but directionally consistent evidence\"\n- results.tex:79 — \"partially confirming the cross-architecture hypothesis\"\n- discussion.tex:14-15 — \"partial support...substantially weaker\"\n- conclusion.tex:4 — \"partially extends cross-architecture\"\n- limitations.tex:1-2 — \"partially confirms...substantially weaker\"\n- appendix_disc_analysis.tex:33 — \"partial confirmation\"\n**状态: 合格，无需修改（除非 n=500 改变了 DS/QW 数据使 LLaMA 对比幅度比例变化）**\n\n### 28. C5b future_work 标注检查 ✅\n已确认:\n- discussion.tex:10 — pilot 结果 + \"promising direction for future work\"\n- appendix_disc_analysis.tex:57,62 — REBUTTAL comments 标注 future work\n**状态: 合格，但 discussion.tex:10 的 \\placeholder{} 值需填充**\n\n### 29. Qwen random s030 caveat 检查\n当前标注为 negligible/no meaningful modulation 的位置:\n- abstract.tex:8 — \"negligible median difference\" ✅\n- appendix_moved.tex:76 — \"negligible median difference, CI spans zero\" ✅\n- appendix_results.tex:10 — 同上 ✅\n- appendix_disc_analysis.tex:14 — \"negligible effect size\" ✅\n- appendix_disc_analysis.tex:49 — \"negligible effect size, bootstrap CI spanning zero\" ✅\n**n=500 后需重新检查: Qwen rand s030 是否仍为 borderline/negligible → 若变显著且效应量非 negligible，需修改 \"7/8 FAIL\" 叙事**\n\n---\n\n## 执行顺序建议\n\n```\nPhase 1: 数据准备\n  1.1 等 n=500 数据完成\n  1.2 运行统计分析脚本 → experiment_summary_table.json, cohens_d, permutation_test 等\n  1.3 提取所有新数值到一个汇总表\n\nPhase 2: P0 核心更新 (同步进行，确保一致)\n  2.1 更新 results.tex 三张主表 (Tab 1/2/3)\n  2.2 更新 abstract.tex 数字\n  2.3 更新 introduction.tex 数字\n  2.4 更新 conclusion.tex 数字\n  2.5 更新 discussion.tex 数字\n  2.6 更新 methodology.tex 样本量\n\nPhase 3: P1 支撑更新\n  3.1 更新 appendix_moved.tex 所有表格和数字\n  3.2 更新 appendix_disc_analysis.tex 数字\n  3.3 重新生成 4 张图 (fig1-fig5)\n\nPhase 4: P2 条件分支\n  4.1 检查 QW s015 CI → 决定 onset threshold 叙事\n  4.2 检查 QW imp-vs-rand → 决定是否添加 Qwen permutation test\n  4.3 检查 QW rand s030 → 决定 \"7/8 FAIL\" 叙事是否需调整\n  4.4 填充所有 \\placeholder{}\n\nPhase 5: P3 一致性扫描\n  5.1 全文搜索 \"n=50\" / \"50 problems\" / \"n=49\" / \"n=46\" → 确保无残留\n  5.2 添加 LLaMA n=50 / c4 n=30 的显式声明\n  5.3 清理 appendix_results.tex（重复文件）\n\nPhase 6: 验证\n  6.1 LaTeX 编译 → 确保无 red placeholder 残留\n  6.2 数字交叉检查: 每个数字在所有出现位置一致\n  6.3 paper_framing.md 同步更新\n```\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "8bf1b672-9698-4e7d-8e5a-02ac5260190e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017U78SHEgEvxuFHwY3acKmK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 775,
      "cache_read_input_tokens": 68110,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 775
      },
      "output_tokens": 59,
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

_source line 80 · 2026-05-15T01:46:14.842Z_

<details><summary>↩ Tool result · `toolu_012paCFDcowLaVpDqwq2aJMH`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/paper_update_checklist.md
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "5c3118ab-578b-46e0-ab94-160cc9c3cabc",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/paper_update_checklist.md",
    "content": "# Paper Update Checklist: n=50 → n=500\n\n> 生成时间: 2026-05-15 | 适用实验: c2_n500_deepseek + c2_qw_n500 (C7)\n> 约束: median + bootstrap CI 为主指标 (D054); d_z 分场景 (D059); Qwen imp-vs-rand 不claim显著直到n=500确认 (D058); C8=partially_confirmed (D060); C5b=future_work (D056)\n\n---\n\n## 优先级说明\n- **P0**: 核心数字，读者第一眼看到，必须同步更新\n- **P1**: 支撑性数字/表格，与 P0 有数据依赖\n- **P2**: 条件性更新（取决于 n=500 结果）\n- **P3**: 一致性检查，防止 n=50/n=500 混用\n\n---\n\n## P0: 核心数字更新\n\n### 1. methodology.tex:10 — 样本量\n```\n当前: \"We use 50 problems stratified from MATH-500\"\n更新: → 500 problems (n=500 的具体描述，包括 stratification 方式)\n```\n\n### 2. abstract.tex:6 — 样本量\n```\n当前: \"using 50 MATH-500 problems\"\n更新: → 500 MATH-500 problems\n```\n\n### 3. abstract.tex:7 — DeepSeek 主指标\n```\n当前: \"median Interaction Index difference...from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired Cohen's $d_z$ growing from $0.44$ (small) to $0.80$ (large)\"\n更新: → 用 n=500 segment-level median diff + paired d_z 替换\n注意: 0.39/14.59 是 segment-level medians；d_z 0.44/0.80 是 paired d_z。两组数据来源不同，都需更新。\n```\n\n### 4. introduction.tex:14 — DeepSeek 主指标（与 abstract 一致）\n```\n当前: \"median phase difference rises from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$ ($d_z$: $0.44 \\to 0.80$)\"\n更新: → 同 abstract\n```\n\n### 5. results.tex:8,13,19-20 — Tab aggregate-ii（DeepSeek segment-level Δ）\n```\n当前 Importance: 0.39, 1.48, 7.16, 14.59\n当前 Random: 0.01, -0.02, 0.54, 1.54\ncaption \"$n{=}50$\" → $n{=}500$ (或实际有效 n)\n更新: → 全部替换为 n=500 值\n```\n\n### 6. results.tex:34,40-50 — Tab main-results（DeepSeek 全 per-phase 分解）\n```\n当前 (importance, 4 sparsity × 3 phases + Δ + G):\n  s015: II_high=0.006, II_mid=0.081, II_low=0.398, Δ=0.39, G=69\n  s020: II_high=0.015, II_mid=0.203, II_low=1.496, Δ=1.48, G=103\n  s025: II_high=0.032, II_mid=1.118, II_low=7.196, Δ=7.16, G=222\n  s030: II_high=0.053, II_mid=2.283, II_low=14.639, Δ=14.59, G=274\n当前 (random, 4 sparsity × 3 phases + Δ + G):\n  s015: 0.093, 0.097, 0.103, 0.01, 1.1\n  s020: 0.292, 0.350, 0.276, -0.02, 0.9\n  s025: 0.818, 0.932, 1.363, 0.54, 1.7\n  s030: 2.503, 2.592, 4.041, 1.54, 1.6\ncaption \"50 problems\" → 500 problems\n更新: → 全部替换为 n=500 值\n```\n\n### 7. results.tex:106,117-120 — Tab cohens-d（DS + QW paired d_z + Δ̃[CI]）\n```\n当前 DS: d_z 0.44/0.52/0.68/0.80; Δ̃ 0.32[0.20,0.47] / 1.15[0.66,1.26] / 3.97[2.83,5.29] / 9.94[8.39,16.65]\n当前 QW: d_z 0.28/0.55/0.89/1.02; Δ̃ 0.05[-0.01,0.11] / 0.21[0.07,0.40] / 1.11[0.61,1.47] / 2.62[1.72,3.65]\n更新: → 全部替换为 n=500 值\n关键: QW s015 CI 当前包含零 → n=500 后检查是否仍包含零（影响 onset threshold 叙事）\n```\n\n### 8. conclusion.tex:4 — 核心数字复述\n```\n当前: \"severity gradient grows from $69{\\times}$ to $274{\\times}$...($d_z$: $0.44 \\to 0.80$)\"\n更新: → 与 results 一致\n```\n\n### 9. discussion.tex:5 — severity gradient + crossover 复述\n```\n当前: \"severity gradient ($69$--$274{\\times}$)\"\n当前: crossover 数字 \"0.032 vs 0.818\", \"7.196 vs 1.363\"\n更新: → 与 results 一致\n```\n\n### 10. results.tex:29 + 58 — G 值 + fig1 caption\n```\n当前: G \"from $69{\\times}$ at $s{=}0.15$ to $274{\\times}$ at $s{=}0.30$\"\n当前 fig1 caption: \"$69{\\times}$ to $274{\\times}$\"\n更新: → n=500 G 值\n```\n\n---\n\n## P1: 支撑性数字更新\n\n### 11. results.tex:66 — Crossover 数字\n```\n当前: \"importance high_phase=0.032 < random=0.818, importance low_phase=7.196 > random=1.363\"\nreversal \"5.3×\"\n更新: → n=500 crossover 值\n```\n\n### 12. results.tex:71 — Qwen cross-model 段落\n```\n当前: \"Δ increases from 0.04 at s=0.15 to 2.94 at s=0.30...d_z ≥ 0.55...d_z=0.28 CI includes zero\"\n更新: → n=500 Qwen 值\n关键: 检查 s015 d_z 是否仍 marginal，onset threshold 是否仍 s≥0.20\n```\n\n### 13. appendix_moved.tex:26 — Qwen/DS 有效 n\n```\n当前: \"Four of the 50 problems...n=46 valid problems for Qwen (vs. n=49 for DeepSeek)\"\n更新: → n=500 的排除数和有效 n\n```\n\n### 14. appendix_moved.tex:59-60 — Tab cross-model Qwen Δ\n```\n当前 DS: 0.39, 1.48, 7.16, 14.59\n当前 QW: 0.04, 0.23, 1.27, 2.94\n更新: → n=500 值\n```\n\n### 15. appendix_moved.tex:88,93,99-102 — Tab permutation（DeepSeek permutation test）\n```\n当前: n=49; observed Δ̃ 0.37[0.19,0.62], 0.97[0.69,1.49], 3.34[1.66,6.64], 9.85[6.70,16.29]\ncaption \"$n{=}49$\"\n更新: → n=500 permutation test 值\n```\n\n### 16. results.tex:104 — permutation test 段落引用\n```\n当前: \"observed median differences increasing monotonically from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$\"\n更新: → 与 Tab permutation 一致\n```\n\n### 17. appendix_moved.tex:11 — crossover 详细数字\n```\n当前: \"reversal magnitude of $3.9{\\times}$ at $s{=}0.15$, $5.4{\\times}$ at $s{=}0.20$, $5.3{\\times}$ at $s{=}0.25$, and $3.6{\\times}$ at $s{=}0.30$\"\n更新: → n=500 reversal magnitudes\n```\n\n### 18. appendix_disc_analysis.tex:46-47 — permutation CI + skewness 统计\n```\n当前: \"mean/median ratio ~1.6:1 at s=0.30\"\n当前: \"permutation CIs: s015=[0.19,0.62], s020=[0.69,1.49], s025=[1.66,6.64], s030=[6.70,16.29]\"\n当前 (line 11): \"high-phase II rises to 0.105 at s=0.35\"\n更新: → n=500 值 (s035 supplementary 是否也需更新取决于是否重跑)\n```\n\n### 19. abstract.tex:10 — LLaMA cross-arch 段落\n```\n当前: \"Δ̃: 0.020→0.356; s=0.30 Wilcoxon p_Bonf=0.029\"\n注意: LLaMA 实验仍为 n=50，数字不变，但需检查措辞是否暗示与 DS/QW 同一 n\n```\n\n### 20. 图表重新生成\n```\nfig1_dose_response.pdf — G vs s 曲线（P0 依赖）\nfig3_crossover.pdf — crossover bar chart\nfig4_bootstrap.pdf — permutation forest plot\nfig5_crossmodel.pdf — cross-model Δ comparison\n所有图需用 n=500 数据重新生成\n```\n\n---\n\n## P2: 条件性更新\n\n### 21. D058: Qwen imp-vs-rand 显著性\n```\n当前状态: 论文未报告 Qwen imp-vs-rand permutation test（只报告了 DeepSeek）\n约束: n=500 前不得 claim Qwen imp-vs-rand 显著\n行动:\n  - 若 n=500 Qwen imp-vs-rand 显著 → 可添加 Qwen permutation test 表格，strengthens C1\n  - 若仍不显著 → 在 cross-model 段落加 caveat，或维持当前策略（只报 within-importance gradient）\n检查文件: results.tex:71, appendix_results.tex:10\n```\n\n### 22. D059: d_z 报告策略\n```\n约束: within-importance d_z 保留; 涉及 random 只报方向\n行动: 检查 n=500 后是否有新的 imp-vs-rand d_z 值需要报告，确保遵守\"只报方向\"规则\n影响文件: results.tex, appendix_moved.tex\n```\n\n### 23. C2 预注册: Qwen s015 onset threshold\n```\n当前: paper_framing 预注册 \"n=500 后若 QW s015 CI 仍跨零，叙事改为 'compound effect emerges above threshold sparsity (~s020)'\"\n检查: results.tex:71 \"marginal at s=0.15\" + Tab cohens-d QW s015 行\n行动:\n  - 若 n=500 QW s015 CI 不跨零 → onset = s≥0.15，更新叙事\n  - 若仍跨零 → 保持 \"emerges above ~s020\" 叙事\n```\n\n### 24. Placeholder 值填充\n以下 \\placeholder{} 标记需用实际数据填充:\n\n| 文件:行 | Placeholder | 数据来源 | n=500影响? |\n|---------|-------------|----------|-----------|\n| abstract.tex:8 | Qwen rand s030 Δ̃ | bf16_qw_rand_s030 | 是 |\n| results.tex:71 | NULL_PCT | Qwen per-phase null rate | 是 |\n| results.tex:81 | LLaMA random Wilcoxon p | c3_llama | 否(n=50) |\n| results.tex:86 | N_LLAMA | c3_llama | 否(n=50) |\n| results.tex:92-95 | 整个 LLaMA 表格 (12 cells) | c3_llama | 否(n=50) |\n| discussion.tex:10 | ORACLE_PCT, ORACLE_P, HEUR_PCT, HEUR_P | c5b_pilot | 否 |\n| discussion.tex:15 | LLaMA random Wilcoxon p | c3_llama | 否(n=50) |\n| appendix_moved.tex:30 | NULL_PCT | Qwen null rate | 是 |\n| appendix_moved.tex:35 | N_QW | Qwen valid n | 是 |\n| appendix_moved.tex:41-43 | Qwen effective n 表格 (12 cells) | Qwen per-phase data | 是 |\n| appendix_moved.tex:73 | ρ, p (per-problem concordance) | cross_model_analysis.json | 是 |\n| appendix_moved.tex:76 | Qwen rand s030 Δ̃ | bf16_qw_rand_s030 | 是 |\n| appendix_results.tex:7 | 同 appendix_moved.tex:73 (重复!) | cross_model_analysis.json | 是 |\n| appendix_results.tex:10 | 同 appendix_moved.tex:76 (重复!) | bf16_qw_rand_s030 | 是 |\n| appendix_disc_analysis.tex:14 | Qwen rand s030 Δ̃ | bf16_qw_rand_s030 | 是 |\n| appendix_disc_analysis.tex:49 | Qwen rand s030 Δ̃ | qw_rand_s030 | 是 |\n\n⚠️ appendix_results.tex 未被 main.tex \\input，内容与 appendix_moved.tex §Cross-Model 重复。建议删除或统一。\n\n---\n\n## P3: 一致性与混用风险\n\n### 25. n=50 / n=500 混用风险矩阵\n\n| 数据源 | 当前 n | 更新后 n | 混用风险 |\n|--------|--------|---------|---------|\n| DeepSeek importance/random (c2) | 50 | **500** | 主表全部替换 |\n| Qwen importance/random (c2) | 50 | **500** | 主表全部替换 |\n| LLaMA cross-arch (c3_llama) | 50 | **50 不变** | ⚠️ 高风险 |\n| Entropy/discrimination (c4) | 30 | **30 不变** | ⚠️ 中风险 |\n| c5b_pilot | ~50 | **不变** | 低风险 |\n| Permutation test | 49(DS)/46(QW) | **~490/~460** | 替换 |\n| Cross-model comparison | 50 | **500** | 替换 |\n\n### 26. 需要显式声明不同 n 的位置\n```\n- abstract.tex: \"50 MATH-500 problems\" → 改为区分 DS/QW (n=500) vs LLaMA (n=50)\n  建议: \"500 MATH-500 problems (50 for cross-architecture validation)\"\n- results.tex §5.5 (cross-arch): 已有 \"n=\\placeholder{N_LLAMA}\" → 填入 49 或 50，确保读者知道这不是 500\n- analysis.tex §6: 当前未提及 c4 的样本量 → 建议添加脚注 \"(30 problems per model)\"\n- discussion.tex §7 (pilot): 当前未提及 pilot 样本量 → 建议添加\n- methodology.tex: 需说明 \"500 problems for primary experiments; 50 for cross-architecture (LLaMA)\"\n- limitations.tex: 添加 \"LLaMA 和 mechanism 分析基于 n=50/30 子集\"\n```\n\n### 27. C8 partially_confirmed 限定语检查 ✅\n已确认以下位置使用了合格限定语:\n- abstract.tex:10 — \"mixed but directionally consistent evidence\"\n- results.tex:79 — \"partially confirming the cross-architecture hypothesis\"\n- discussion.tex:14-15 — \"partial support...substantially weaker\"\n- conclusion.tex:4 — \"partially extends cross-architecture\"\n- limitations.tex:1-2 — \"partially confirms...substantially weaker\"\n- appendix_disc_analysis.tex:33 — \"partial confirmation\"\n**状态: 合格，无需修改（除非 n=500 改变了 DS/QW 数据使 LLaMA 对比幅度比例变化）**\n\n### 28. C5b future_work 标注检查 ✅\n已确认:\n- discussion.tex:10 — pilot 结果 + \"promising direction for future work\"\n- appendix_disc_analysis.tex:57,62 — REBUTTAL comments 标注 future work\n**状态: 合格，但 discussion.tex:10 的 \\placeholder{} 值需填充**\n\n### 29. Qwen random s030 caveat 检查\n当前标注为 negligible/no meaningful modulation 的位置:\n- abstract.tex:8 — \"negligible median difference\" ✅\n- appendix_moved.tex:76 — \"negligible median difference, CI spans zero\" ✅\n- appendix_results.tex:10 — 同上 ✅\n- appendix_disc_analysis.tex:14 — \"negligible effect size\" ✅\n- appendix_disc_analysis.tex:49 — \"negligible effect size, bootstrap CI spanning zero\" ✅\n**n=500 后需重新检查: Qwen rand s030 是否仍为 borderline/negligible → 若变显著且效应量非 negligible，需修改 \"7/8 FAIL\" 叙事**\n\n---\n\n## 执行顺序建议\n\n```\nPhase 1: 数据准备\n  1.1 等 n=500 数据完成\n  1.2 运行统计分析脚本 → experiment_summary_table.json, cohens_d, permutation_test 等\n  1.3 提取所有新数值到一个汇总表\n\nPhase 2: P0 核心更新 (同步进行，确保一致)\n  2.1 更新 results.tex 三张主表 (Tab 1/2/3)\n  2.2 更新 abstract.tex 数字\n  2.3 更新 introduction.tex 数字\n  2.4 更新 conclusion.tex 数字\n  2.5 更新 discussion.tex 数字\n  2.6 更新 methodology.tex 样本量\n\nPhase 3: P1 支撑更新\n  3.1 更新 appendix_moved.tex 所有表格和数字\n  3.2 更新 appendix_disc_analysis.tex 数字\n  3.3 重新生成 4 张图 (fig1-fig5)\n\nPhase 4: P2 条件分支\n  4.1 检查 QW s015 CI → 决定 onset threshold 叙事\n  4.2 检查 QW imp-vs-rand → 决定是否添加 Qwen permutation test\n  4.3 检查 QW rand s030 → 决定 \"7/8 FAIL\" 叙事是否需调整\n  4.4 填充所有 \\placeholder{}\n\nPhase 5: P3 一致性扫描\n  5.1 全文搜索 \"n=50\" / \"50 problems\" / \"n=49\" / \"n=46\" → 确保无残留\n  5.2 添加 LLaMA n=50 / c4 n=30 的显式声明\n  5.3 清理 appendix_results.tex（重复文件）\n\nPhase 6: 验证\n  6.1 LaTeX 编译 → 确保无 red placeholder 残留\n  6.2 数字交叉检查: 每个数字在所有出现位置一致\n  6.3 paper_framing.md 同步更新\n```\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
````

</details>

---

### Assistant

_source line 81_

清单已保存到 `artifacts/paper_update_checklist.md`。

汇总：

**P0（10项）**：abstract/intro/results/conclusion/discussion 中的核心数字——样本量 50→500、DeepSeek Δ 四个值（0.39→14.59）、d_z（0.44→0.80）、severity gradient G（69×→274×）、crossover 数字、3 张主表（aggregate-ii、main-results、cohens-d）全部需替换。

**P1（10项）**：Qwen cross-model 段落+表格、permutation test 表格+段落、crossover reversal magnitudes、appendix 所有数字、4 张图重新生成。

**P2（4项条件分支）**：QW s015 CI 是否仍跨零（决定 onset threshold 叙事）、QW imp-vs-rand 是否终于显著（D058）、QW rand s030 是否仍 negligible（影响"7/8 FAIL"叙事）、24 个 `\placeholder{}` 待填充。

**P3（5项一致性）**：LLaMA 仍 n=50、c4 机制分析仍 n=30——需在 abstract/methodology/limitations 显式声明不同 n；appendix_results.tex 是冗余文件建议清理；C8 限定语和 C5b future_work 标注已合格无需改动。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "uuid": "d22973f2-2bd0-4d2e-8a20-1a3e7eef3c5b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wcog8ZTDZixFQcyrEUsYEu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5912,
      "cache_read_input_tokens": 68885,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5912
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

_source line 82_

清单已保存到 `artifacts/paper_update_checklist.md`。

汇总：

**P0（10项）**：abstract/intro/results/conclusion/discussion 中的核心数字——样本量 50→500、DeepSeek Δ 四个值（0.39→14.59）、d_z（0.44→0.80）、severity gradient G（69×→274×）、crossover 数字、3 张主表（aggregate-ii、main-results、cohens-d）全部需替换。

**P1（10项）**：Qwen cross-model 段落+表格、permutation test 表格+段落、crossover reversal magnitudes、appendix 所有数字、4 张图重新生成。

**P2（4项条件分支）**：QW s015 CI 是否仍跨零（决定 onset threshold 叙事）、QW imp-vs-rand 是否终于显著（D058）、QW rand s030 是否仍 negligible（影响"7/8 FAIL"叙事）、24 个 `\placeholder{}` 待填充。

**P3（5项一致性）**：LLaMA 仍 n=50、c4 机制分析仍 n=30——需在 abstract/methodology/limitations 显式声明不同 n；appendix_results.tex 是冗余文件建议清理；C8 限定语和 C5b future_work 标注已合格无需改动。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 388164,
  "duration_api_ms": 389174,
  "num_turns": 30,
  "stop_reason": "end_turn",
  "session_id": "92d5a500-97ec-4718-a2d5-83296bc1ca35",
  "total_cost_usd": 1.1237709999999999,
  "usage": {
    "input_tokens": 16,
    "cache_creation_input_tokens": 63350,
    "cache_read_input_tokens": 532439,
    "output_tokens": 18409,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 63350,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 398,
        "cache_read_input_tokens": 68885,
        "cache_creation_input_tokens": 5912,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 5912
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1219,
      "outputTokens": 18,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001309,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 16,
      "outputTokens": 18409,
      "cacheReadInputTokens": 532439,
      "cacheCreationInputTokens": 63350,
      "webSearchRequests": 0,
      "costUSD": 1.1224619999999998,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "d760380b-1a88-49ca-8424-f2da1bc12fd2"
}
```

</details>

---
