# research paper update prep

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 114
- **Recorded user turns:** 1
- **Tool calls:** 36
- **Original source:** `logs/workers/worker_research_paper_update_prep_20260514T204242.log`
- **Structured JSON:** [`c753fb26e71826192344.json`](../../sessions/c7/c753fb26e71826192344.json)

## Before a recorded user message

33 recorded events

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
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
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
  "uuid": "1d28f397-5f34-4292-b498-4304dbadeca3",
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
    "status": "allowed_warning",
    "resetsAt": 1778911200,
    "rateLimitType": "seven_day",
    "utilization": 0.83,
    "isUsingOverage": false,
    "surpassedThreshold": 0.75
  },
  "uuid": "fed5a6b4-fa99-4860-91af-4c81f2734789",
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the project files mentioned in the task, then examine the paper directory for all references to n=50 data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "e98973cc-f31b-418d-ae67-e61bd2ab8a3f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TUB2uGFsQHScNYKvgaG7oc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11927,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11927
      },
      "output_tokens": 25,
      "service_tier": "standard",
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

开始准备 n=500 论文更新清单。先读取项目文件和论文内容。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "a101de7f-eda9-40b1-a0a7-0bc41f1c7a01",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TUB2uGFsQHScNYKvgaG7oc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11927,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11927
      },
      "output_tokens": 25,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Mc1RfQtEKLKVRWpifEFx8J`</summary>

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
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "d7c68ab3-c1ec-4e0d-956f-23b90489f5f6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TUB2uGFsQHScNYKvgaG7oc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11927,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11927
      },
      "output_tokens": 25,
      "service_tier": "standard",
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

_source line 7 · 2026-05-14T20:42:53.390Z_

<details><summary>↩ Tool result · `toolu_01Mc1RfQtEKLKVRWpifEFx8J`</summary>

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
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "544ae2b9-0c40-46f9-9dfa-27d7d76d0b36",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_012WeREkpYhEjfZHZemfnH75`</summary>

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
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "23b5af4f-55a6-444e-92d7-384f8b633bc5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U2D2Mof3DyEqrNdSv9s29q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 772,
      "cache_read_input_tokens": 23374,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 772
      },
      "output_tokens": 70,
      "service_tier": "standard",
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

_source line 9 · 2026-05-14T20:42:57.969Z_

<details><summary>↩ Tool result · `toolu_012WeREkpYhEjfZHZemfnH75`</summary>

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
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "588cefac-75a9-4534-a9ab-e5128262da8f",
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

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01ETXeFCXANzVmVjifudyLTx`</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "file": "writing_plan.yaml",
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
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "140a5ab1-6513-42c7-993c-77253323f0b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U2D2Mof3DyEqrNdSv9s29q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 772,
      "cache_read_input_tokens": 23374,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 772
      },
      "output_tokens": 70,
      "service_tier": "standard",
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

_source line 11 · 2026-05-14T20:42:58.293Z_

<details><summary>↩ Tool result · `toolu_01ETXeFCXANzVmVjifudyLTx`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/writing_plan.yaml\", \"content\": \"## Writing Plan — Phase-Gated Compound Sparsity\\n## 最后更新: 2026-05-14\\n\\n# ============================================================\\n# 投稿目标\\n# ============================================================\\ntarget:\\n  venue: EMNLP 2026 ARR\\n  deadline: 2026-05-25\\n  days_remaining: 11\\n  format: long paper (8 pages + references + appendix)\\n  anonymization: ARR double-blind\\n\\n# ============================================================\\n# Paper Outline\\n# ============================================================\\noutline:\\n  title_candidates:\\n    - \\\"Phase-Modulated Compound Sparsity: How Eviction Strategy and Reasoning Phase Interact in Sparse LLM Inference\\\"\\n    - \\\"Emergent Phase-Strategy Interaction in Compound Sparse LLM Inference\\\"\\n    - \\\"When Compound Sparsity Bites Back: Phase-Dependent Severity Amplification in Importance-Based Eviction\\\"\\n\\n  sections:\\n    - id: abstract\\n      title: Abstract\\n      summary: >\\n        Compound sparsity (head pruning + KV cache eviction) is assumed to degrade uniformly.\\n        We show the interaction is strategy-dependent and phase-modulated: importance-based eviction\\n        exhibits 12-75× severity amplification in low-sparsity reasoning phases, while random eviction\\n        stays flat (~1×). Bootstrap CI (B=10000) confirms significance at all 4 sparsity levels (p<0.0001).\\n        Cross-model replication on Qwen2.5-7B validates generalizability. We explain this via an\\n        entropy-discrimination collapse mechanism: head pruning distributes surviving attention,\\n        destroying importance score discriminability specifically in distributed-attention phases.\\n      length: 250 words\\n\\n    - id: introduction\\n      title: \\\"1. Introduction\\\"\\n      summary: >\\n        Motivate compound sparsity as practical deployment need. State gap: prior work (SparK, Ada-KV)\\n        treats compound interaction as uniformly super-additive. Our finding: the severity is an\\n        emergent property of the interaction between eviction strategy and reasoning phase.\\n        Preview crossover phenomenon and mechanism. State contributions.\\n      length: 1 page\\n      key_claims:\\n        - Compound sparsity severity is not uniform — it is strategy-dependent and phase-modulated\\n        - Importance-based eviction amplifies compound interaction 12-75× in low-sparsity phases\\n        - Entropy-discrimination collapse explains the phase-strategy interaction\\n\\n    - id: related_work\\n      title: \\\"2. Related Work\\\"\\n      summary: >\\n        Three threads: (1) Compound/joint compression (SparK, SLiM, UniComp, compression-ordering)\\n        — none analyzes phase × strategy interaction. (2) KV cache eviction (Ada-KV, DefensiveKV,\\n        SnapKV, NACL) — importance fragility noted but not phase-conditioned. (3) Phase-aware\\n        inference (ThinKV, PagedEviction, reasoning dynamics) — single-axis, no compound interaction.\\n      length: 0.75 page\\n      key_refs:\\n        - spark-aaai2026\\n        - thinkv-iclr2026\\n        - defensivekv-iclr2026\\n        - slim-icml2025\\n        - phase-transition-compression-2026\\n        - decision-repr-transition-2026\\n        - retentivekv-2026\\n        - greedy-bias-kvcache-2026\\n\\n    - id: background\\n      title: \\\"3. Background and Problem Setup\\\"\\n      summary: >\\n        Define compound sparsity (attention head pruning ⊗ KV cache eviction). Define Interaction\\n        Index (II) measuring super/sub-additivity. Define phase segmentation via ThinKV-style\\n        token-ratio method. Formalize the research question: is II constant across phases and strategies?\\n      length: 1 page\\n      subsections:\\n        - \\\"3.1 Compound Sparsity Formulation\\\"\\n        - \\\"3.2 Interaction Index\\\"\\n        - \\\"3.3 Phase Segmentation\\\"\\n\\n    - id: methodology\\n      title: \\\"4. Experimental Setup\\\"\\n      summary: >\\n        Models (DeepSeek-R1-Distill-Qwen-7B, Qwen2.5-7B-Instruct), dataset (MATH-500 subset, 50 problems),\\n        sparsity levels (s=0.15/0.20/0.25/0.30), eviction strategies (importance-based cumulative\\n        attention with position normalization, random), metrics (PPL, II, gradient), hardware.\\n        Statistical method: per-problem bootstrap CI (B=10000), paired and unpaired.\\n      length: 1 page\\n\\n    - id: results\\n      title: \\\"5. Results\\\"\\n      summary: >\\n        Main finding: importance gradient 11-42× (problem-level bootstrap) increasing with sparsity,\\n        random gradient ~1×. Bootstrap CI all significant (p<0.001 fp16, target p<10⁻⁴ bf16).\\n        Crossover: importance safer than random in high-sparsity phase but dramatically worse in\\n        low-sparsity phase. Sub-exponential growth pattern. Cross-model replication on Qwen.\\n      length: 2.5 pages\\n      subsections:\\n        - \\\"5.0 Experimental Overview (sec:exp-overview)\\\"\\n        - \\\"5.1 Strategy-Dependent Severity — C1 (sec:strategy-severity)\\\"\\n        - \\\"5.2 Phase-Modulated Amplification — C2 (sec:phase-amplification)\\\"\\n        - \\\"5.3 Phase-Strategy Crossover — C3 (sec:crossover)\\\"\\n        - \\\"5.4 Cross-Model Replication — C5 (sec:cross-model)\\\"\\n        - \\\"5.5 Statistical Validation (sec:stat-validation)\\\"\\n\\n    - id: analysis\\n      title: \\\"6. Analysis: Entropy-Discrimination Collapse\\\"\\n      summary: >\\n        Mechanistic explanation: head pruning → surviving heads attend more uniformly → importance\\n        score entropy increases → discrimination between important/unimportant KV entries collapses →\\n        importance-based eviction degrades to biased pseudo-random in distributed-attention phases.\\n        This is phase-dependent because reasoning phases have more distributed attention.\\n      length: 1 page\\n\\n    - id: discussion\\n      title: \\\"7. Discussion\\\"\\n      summary: >\\n        Implications for compound sparsity deployment: uniform budgets are unsafe.\\n        Phase-gated controllers as solution direction. Limitations: 7B models only,\\n        MATH-500 only, no throughput measurements yet.\\n      length: 0.5 page\\n\\n    - id: conclusion\\n      title: \\\"8. Conclusion\\\"\\n      summary: >\\n        Compound sparsity severity is an emergent property of strategy × phase interaction.\\n        This finding challenges the implicit assumption of uniform compound degradation\\n        and motivates phase-aware sparsity allocation.\\n      length: 0.25 page\\n\\n# ============================================================\\n# Figures and Tables\\n# ============================================================\\nfigures:\\n  - id: fig1_hero\\n    title: \\\"Phase-Modulated Severity Gradient (Hero Figure)\\\"\\n    type: line plot or grouped bar\\n    data_source: v5 importance + v5 random segment-level II medians\\n    message: >\\n      Importance gradient rises 12.8-74.9× across sparsity levels while random stays flat ~1×.\\n      The gap between strategies widens with sparsity — this is the core visual claim.\\n    placement: page 1 or Section 5.1\\n    priority: P0\\n\\n  - id: fig2_crossover\\n    title: \\\"Phase-Strategy Crossover Heatmap\\\"\\n    type: heatmap (strategy × phase × sparsity)\\n    data_source: v5 importance + random per-phase II values\\n    message: >\\n      At s=0.25, importance outperforms random in high-sparsity phase (0.584 vs 3.002) but\\n      underperforms dramatically in low-sparsity phase (30.903 vs 2.915). Direction reversal\\n      is phase-dependent.\\n    placement: Section 5.2\\n    priority: P0\\n\\n  - id: fig3_mechanism\\n    title: \\\"Entropy-Discrimination Collapse Illustration\\\"\\n    type: schematic diagram + attention distribution plot\\n    data_source: conceptual + optional empirical attention entropy data\\n    message: >\\n      Head pruning → attention redistribution → importance score entropy increase →\\n      discrimination collapse. Explains why importance eviction fails specifically in\\n      distributed-attention phases.\\n    placement: Section 6\\n    priority: P1\\n\\n  - id: fig4_bootstrap\\n    title: \\\"Bootstrap CI Forest Plot\\\"\\n    type: forest plot\\n    data_source: v6 per-problem bootstrap results (B=10000)\\n    message: >\\n      All 4 sparsity levels show gradient CI entirely above 1.0, p=0.0000.\\n      Visual confirmation of statistical significance.\\n    placement: Section 5.1\\n    priority: P1\\n\\n  - id: fig5_crossmodel\\n    title: \\\"Cross-Model Replication\\\"\\n    type: grouped bar or side-by-side line plot\\n    data_source: Qwen2.5-7B importance results (pending)\\n    message: >\\n      Phase-modulated severity generalizes beyond DeepSeek to Qwen architecture.\\n    placement: Section 5.3\\n    priority: P0 (blocked on Qwen experiments)\\n\\ntables:\\n  - id: tab1_main\\n    title: \\\"Main Results: II by Strategy × Phase × Sparsity\\\"\\n    data_source: v5 importance + random, median + IQR\\n    columns: [sparsity, strategy, high_phase_II, mid_phase_II, low_phase_II, gradient, gradient_CI]\\n    message: Core quantitative claim — strategy × phase interaction\\n    placement: Section 5.1\\n    priority: P0\\n\\n  - id: tab2_bootstrap\\n    title: \\\"Bootstrap Confidence Intervals (B=10000)\\\"\\n    data_source: v6 per-problem bootstrap\\n    columns: [sparsity, paired_gradient, paired_CI, unpaired_gradient, unpaired_CI, p_value]\\n    message: Statistical rigor — all gradients significant\\n    placement: Section 5.1\\n    priority: P0\\n\\n  - id: tab3_crossmodel\\n    title: \\\"Cross-Model Comparison: DeepSeek vs Qwen\\\"\\n    data_source: v6 DeepSeek + Qwen importance results (Qwen pending)\\n    message: Generalizability beyond single model family\\n    placement: Section 5.3\\n    priority: P0 (blocked on Qwen)\\n\\n# ============================================================\\n# Claims → Evidence Mapping\\n# ============================================================\\nclaims:\\n  - claim: \\\"Compound sparsity severity is strategy-dependent\\\"\\n    evidence:\\n      - \\\"v5 importance gradient 12.8-74.9× vs v5 random gradient ~1×\\\"\\n      - \\\"Bootstrap CI: importance gradient CI lower bound >> 1.0; random gradient CI spans 1.0\\\"\\n    status: confirmed\\n\\n  - claim: \\\"Severity is phase-modulated (amplified in low-sparsity reasoning phase)\\\"\\n    evidence:\\n      - \\\"v5 per-phase II: low phase >> high phase for importance at all 4 sparsity levels\\\"\\n      - \\\"Gradient monotonically increases with sparsity: 12.8→28.7→52.9→74.9\\\"\\n    status: confirmed\\n\\n  - claim: \\\"Phase-strategy crossover exists\\\"\\n    evidence:\\n      - \\\"s=0.25: importance high_phase=0.584 < random=3.002, importance low_phase=30.903 > random=2.915\\\"\\n      - \\\"Direction depends on phase, not just magnitude\\\"\\n    status: confirmed\\n\\n  - claim: \\\"Entropy-discrimination collapse explains the mechanism\\\"\\n    evidence:\\n      - \\\"Conceptual argument: head pruning → distributed attention → importance entropy up → discrimination down\\\"\\n      - \\\"Empirical: importance PPL 26-60× worse than random before metric fix (D012/D013) = metric failure\\\"\\n    status: partially_confirmed (mechanism is explanatory, not directly measured)\\n\\n  - claim: \\\"Finding generalizes across model families\\\"\\n    evidence:\\n      - \\\"Qwen2.5-7B-Instruct experiments (pending)\\\"\\n    status: pending\\n\\n  - claim: \\\"Severity gradient is sub-exponential\\\"\\n    evidence:\\n      - \\\"Growth rate: 2.24×→1.84×→1.42× (decreasing)\\\"\\n    status: confirmed\\n\\n# ============================================================\\n# Writing Priority & Schedule\\n# ============================================================\\nwriting_priority:\\n  # Phase 1: 可立即写的部分 (Day 1-3, May 14-16)\\n  - priority: 1\\n    sections: [methodology, background, related_work]\\n    reason: \\\"不依赖 Qwen 结果，数据已完备，先把 methodology infrastructure 写好\\\"\\n    deliverable: \\\"完整的 Section 3 + 4 + 2 初稿\\\"\\n\\n  - priority: 1\\n    task: \\\"fig1_hero + fig2_crossover + tab1_main + tab2_bootstrap\\\"\\n    reason: \\\"核心数据已有，图表先出可以驱动 narrative\\\"\\n    deliverable: \\\"4 个核心 figure/table 的 publication-ready 版本\\\"\\n\\n  # Phase 2: 核心结果 (Day 3-5, May 16-18)\\n  - priority: 2\\n    sections: [results_5_1, results_5_2]\\n    reason: \\\"5.1 和 5.2 数据完备，5.3 (cross-model) 需等 Qwen\\\"\\n    deliverable: \\\"Section 5.1 + 5.2 完整初稿\\\"\\n\\n  - priority: 2\\n    sections: [analysis]\\n    reason: \\\"机制解释可独立写，不依赖 Qwen\\\"\\n    deliverable: \\\"Section 6 初稿\\\"\\n\\n  # Phase 3: Cross-model + Introduction (Day 5-7, May 18-20)\\n  - priority: 3\\n    sections: [results_5_3]\\n    reason: \\\"Qwen 实验预计 Day 3-4 出结果\\\"\\n    deliverable: \\\"Section 5.3 + Table 3 + Fig 5\\\"\\n\\n  - priority: 3\\n    sections: [introduction]\\n    reason: \\\"Introduction 最后写——需要所有结果确定后才能精确表述 contributions\\\"\\n    deliverable: \\\"Section 1 完整初稿\\\"\\n\\n  # Phase 4: Abstract + Polish (Day 7-9, May 20-22)\\n  - priority: 4\\n    sections: [abstract, discussion, conclusion]\\n    reason: \\\"总结性段落最后写\\\"\\n    deliverable: \\\"完整初稿 v1\\\"\\n\\n  # Phase 5: Review & Submission (Day 9-11, May 22-25)\\n  - priority: 5\\n    task: \\\"Internal review, polish, formatting check, reference audit, submission\\\"\\n    reason: \\\"留 3 天 buffer 做 revision\\\"\\n    deliverable: \\\"Camera-ready 提交\\\"\\n\\nschedule:\\n  - days: \\\"Day 1-3 (May 14-16)\\\"\\n    tasks:\\n      - \\\"LaTeX 模板搭建 (EMNLP ARR format)\\\"\\n      - \\\"Section 3 (Background) 初稿\\\"\\n      - \\\"Section 4 (Methodology) 初稿\\\"\\n      - \\\"Section 2 (Related Work) 初稿\\\"\\n      - \\\"Fig 1 (hero), Fig 2 (crossover), Table 1, Table 2 制图\\\"\\n      - \\\"启动 Qwen cross-model 实验\\\"\\n    milestone: \\\"方法论部分完成 + 核心图表就绪\\\"\\n\\n  - days: \\\"Day 3-5 (May 16-18)\\\"\\n    tasks:\\n      - \\\"Section 5.1 (severity gradient) 初稿\\\"\\n      - \\\"Section 5.2 (crossover) 初稿\\\"\\n      - \\\"Section 6 (analysis/mechanism) 初稿\\\"\\n      - \\\"Fig 3 (mechanism diagram)\\\"\\n      - \\\"Fig 4 (bootstrap forest plot)\\\"\\n    milestone: \\\"结果+分析部分完成\\\"\\n\\n  - days: \\\"Day 5-7 (May 18-20)\\\"\\n    tasks:\\n      - \\\"Qwen 结果整合 → Section 5.3, Table 3, Fig 5\\\"\\n      - \\\"Section 1 (Introduction) 初稿\\\"\\n      - \\\"如果 Qwen 结果延迟：先写 conditional 版本，留占位\\\"\\n    milestone: \\\"主体内容完成\\\"\\n\\n  - days: \\\"Day 7-9 (May 20-22)\\\"\\n    tasks:\\n      - \\\"Abstract 撰写\\\"\\n      - \\\"Section 7 (Discussion) + Section 8 (Conclusion)\\\"\\n      - \\\"Appendix: paired bootstrap 详细结果、per-problem 分布\\\"\\n      - \\\"全文 polish pass 1: 叙事一致性、数据准确性\\\"\\n    milestone: \\\"完整初稿 v1\\\"\\n\\n  - days: \\\"Day 9-11 (May 22-25)\\\"\\n    tasks:\\n      - \\\"Reference audit (引用完整性+格式)\\\"\\n      - \\\"Polish pass 2: 语言、格式、ARR checklist\\\"\\n      - \\\"Limitations section\\\"\\n      - \\\"Ethics statement (if required)\\\"\\n      - \\\"最终提交\\\"\\n    milestone: \\\"提交完成\\\"\\n\\n# ============================================================\\n# 关键风险\\n# ============================================================\\nrisks:\\n  - risk: \\\"Qwen cross-model 实验未完成或结果 negative\\\"\\n    mitigation: >\\n      如果 Day 5 前无结果：写 conditional 版本 \\\"we additionally test on Qwen2.5-7B (results pending)\\\".\\n      如果结果 negative：调整 narrative 为 \\\"model-specific phenomenon requiring further investigation\\\",\\n      仍可作为 finding paper 提交（DeepSeek 数据已足够支撑 core claim）.\\n    impact: medium\\n\\n  - risk: \\\"11 天写不完\\\"\\n    mitigation: >\\n      优先保证 core sections (3-6)，Introduction/Discussion 可以精简。\\n      如果时间不够，砍 mechanism analysis (Section 6) 到 1 段 discussion。\\n    impact: low (schedule has 3-day buffer)\\n\\n  - risk: \\\"Reviewer 质疑 7B-only + MATH-500-only 的 generalizability\\\"\\n    mitigation: >\\n      Cross-model (Qwen) 是第一层防御。Limitations 明确声明 scale。\\n      MATH-500 是 standard benchmark，defensible。\\n    impact: medium\\n\\n# ============================================================\\n# Framing 约束 (Director D015)\\n# ============================================================\\nframing_constraints:\\n  must: \\\"emergent phase-strategy interaction\\\"\\n  must_not: \\\"importance metric limitation / importance is broken\\\"\\n  narrative_arc: >\\n    Compound sparsity is increasingly used for efficient LLM inference, but its interaction\\n    dynamics are poorly understood. We discover that the severity of compound interaction\\n    is not a fixed property — it emerges from the interplay of eviction strategy and reasoning\\n    phase. Importance-based eviction amplifies compound degradation 12-75× in low-sparsity\\n    phases, while random eviction maintains flat interaction. This phase-strategy interaction,\\n    explained by entropy-discrimination collapse, challenges the uniform-degradation assumption\\n    and motivates phase-aware sparsity allocation.\\n\", \"total_chars\": 15664, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "5774b5d4-6a80-43a5-9285-b9785871407f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/writing_plan.yaml\\\", \\\"content\\\": \\\"## Writing Plan — Phase-Gated Compound Sparsity\\\\n## 最后更新: 2026-05-14\\\\n\\\\n# ============================================================\\\\n# 投稿目标\\\\n# ============================================================\\\\ntarget:\\\\n  venue: EMNLP 2026 ARR\\\\n  deadline: 2026-05-25\\\\n  days_remaining: 11\\\\n  format: long paper (8 pages + references + appendix)\\\\n  anonymization: ARR double-blind\\\\n\\\\n# ============================================================\\\\n# Paper Outline\\\\n# ============================================================\\\\noutline:\\\\n  title_candidates:\\\\n    - \\\\\\\"Phase-Modulated Compound Sparsity: How Eviction Strategy and Reasoning Phase Interact in Sparse LLM Inference\\\\\\\"\\\\n    - \\\\\\\"Emergent Phase-Strategy Interaction in Compound Sparse LLM Inference\\\\\\\"\\\\n    - \\\\\\\"When Compound Sparsity Bites Back: Phase-Dependent Severity Amplification in Importance-Based Eviction\\\\\\\"\\\\n\\\\n  sections:\\\\n    - id: abstract\\\\n      title: Abstract\\\\n      summary: >\\\\n        Compound sparsity (head pruning + KV cache eviction) is assumed to degrade uniformly.\\\\n        We show the interaction is strategy-dependent and phase-modulated: importance-based eviction\\\\n        exhibits 12-75× severity amplification in low-sparsity reasoning phases, while random eviction\\\\n        stays flat (~1×). Bootstrap CI (B=10000) confirms significance at all 4 sparsity levels (p<0.0001).\\\\n        Cross-model replication on Qwen2.5-7B validates generalizability. We explain this via an\\\\n        entropy-discrimination collapse mechanism: head pruning distributes surviving attention,\\\\n        destroying importance score discriminability specifically in distributed-attention phases.\\\\n      length: 250 words\\\\n\\\\n    - id: introduction\\\\n      title: \\\\\\\"1. Introduction\\\\\\\"\\\\n      summary: >\\\\n        Motivate compound sparsity as practical deployment need. State gap: prior work (SparK, Ada-KV)\\\\n        treats compound interaction as uniformly super-additive. Our finding: the severity is an\\\\n        emergent property of the interaction between eviction strategy and reasoning phase.\\\\n        Preview crossover phenomenon and mechanism. State contributions.\\\\n      length: 1 page\\\\n      key_claims:\\\\n        - Compound sparsity severity is not uniform — it is strategy-dependent and phase-modulated\\\\n        - Importance-based eviction amplifies compound interaction 12-75× in low-sparsity phases\\\\n        - Entropy-discrimination collapse explains the phase-strategy interaction\\\\n\\\\n    - id: related_work\\\\n      title: \\\\\\\"2. Related Work\\\\\\\"\\\\n      summary: >\\\\n        Three threads: (1) Compound/joint compression (SparK, SLiM, UniComp, compression-ordering)\\\\n        — none analyzes phase × strategy interaction. (2) KV cache eviction (Ada-KV, DefensiveKV,\\\\n        SnapKV, NACL) — importance fragility noted but not phase-conditioned. (3) Phase-aware\\\\n        inference (ThinKV, PagedEviction, reasoning dynamics) — single-axis, no compound interaction.\\\\n      length: 0.75 page\\\\n      key_refs:\\\\n        - spark-aaai2026\\\\n        - thinkv-iclr2026\\\\n        - defensivekv-iclr2026\\\\n        - slim-icml2025\\\\n        - phase-transition-compression-2026\\\\n        - decision-repr-transition-2026\\\\n        - retentivekv-2026\\\\n        - greedy-bias-kvcache-2026\\\\n\\\\n    - id: background\\\\n      title: \\\\\\\"3. Background and Problem Setup\\\\\\\"\\\\n      summary: >\\\\n        Define compound sparsity (attention head pruning ⊗ KV cache eviction). Define Interaction\\\\n        Index (II) measuring super/sub-additivity. Define phase segmentation via ThinKV-style\\\\n        token-ratio method. Formalize the research question: is II constant across phases and strategies?\\\\n      length: 1 page\\\\n      subsections:\\\\n        - \\\\\\\"3.1 Compound Sparsity Formulation\\\\\\\"\\\\n        - \\\\\\\"3.2 Interaction Index\\\\\\\"\\\\n        - \\\\\\\"3.3 Phase Segmentation\\\\\\\"\\\\n\\\\n    - id: methodology\\\\n      title: \\\\\\\"4. Experimental Setup\\\\\\\"\\\\n      summary: >\\\\n        Models (DeepSeek-R1-Distill-Qwen-7B, Qwen2.5-7B-Instruct), dataset (MATH-500 subset, 50 problems),\\\\n        sparsity levels (s=0.15/0.20/0.25/0.30), eviction strategies (importance-based cumulative\\\\n        attention with position normalization, random), metrics (PPL, II, gradient), hardware.\\\\n        Statistical method: per-problem bootstrap CI (B=10000), paired and unpaired.\\\\n      length: 1 page\\\\n\\\\n    - id: results\\\\n      title: \\\\\\\"5. Results\\\\\\\"\\\\n      summary: >\\\\n        Main finding: importance gradient 11-42× (problem-level bootstrap) increasing with sparsity,\\\\n        random gradient ~1×. Bootstrap CI all significant (p<0.001 fp16, target p<10⁻⁴ bf16).\\\\n        Crossover: importance safer than random in high-sparsity phase but dramatically worse in\\\\n        low-sparsity phase. Sub-exponential growth pattern. Cross-model replication on Qwen.\\\\n      length: 2.5 pages\\\\n      subsections:\\\\n        - \\\\\\\"5.0 Experimental Overview (sec:exp-overview)\\\\\\\"\\\\n        - \\\\\\\"5.1 Strategy-Dependent Severity — C1 (sec:strategy-severity)\\\\\\\"\\\\n        - \\\\\\\"5.2 Phase-Modulated Amplification — C2 (sec:phase-amplification)\\\\\\\"\\\\n        - \\\\\\\"5.3 Phase-Strategy Crossover — C3 (sec:crossover)\\\\\\\"\\\\n        - \\\\\\\"5.4 Cross-Model Replication — C5 (sec:cross-model)\\\\\\\"\\\\n        - \\\\\\\"5.5 Statistical Validation (sec:stat-validation)\\\\\\\"\\\\n\\\\n    - id: analysis\\\\n      title: \\\\\\\"6. Analysis: Entropy-Discrimination Collapse\\\\\\\"\\\\n      summary: >\\\\n        Mechanistic explanation: head pruning → surviving heads attend more uniformly → importance\\\\n        score entropy increases → discrimination between important/unimportant KV entries collapses →\\\\n        importance-based eviction degrades to biased pseudo-random in distributed-attention phases.\\\\n        This is phase-dependent because reasoning phases have more distributed attention.\\\\n      length: 1 page\\\\n\\\\n    - id: discussion\\\\n      title: \\\\\\\"7. Discussion\\\\\\\"\\\\n      summary: >\\\\n        Implications for compound sparsity deployment: uniform budgets are unsafe.\\\\n        Phase-gated controllers as solution direction. Limitations: 7B models only,\\\\n        MATH-500 only, no throughput measurements yet.\\\\n      length: 0.5 page\\\\n\\\\n    - id: conclusion\\\\n      title: \\\\\\\"8. Conclusion\\\\\\\"\\\\n      summary: >\\\\n        Compound sparsity severity is an emergent property of strategy × phase interaction.\\\\n        This finding challenges the implicit assumption of uniform compound degradation\\\\n        and motivates phase-aware sparsity allocation.\\\\n      length: 0.25 page\\\\n\\\\n# ============================================================\\\\n# Figures and Tables\\\\n# ============================================================\\\\nfigures:\\\\n  - id: fig1_hero\\\\n    title: \\\\\\\"Phase-Modulated Severity Gradient (Hero Figure)\\\\\\\"\\\\n    type: line plot or grouped bar\\\\n    data_source: v5 importance + v5 random segment-level II medians\\\\n    message: >\\\\n      Importance gradient rises 12.8-74.9× across sparsity levels while random stays flat ~1×.\\\\n      The gap between strategies widens with sparsity — this is the core visual claim.\\\\n    placement: page 1 or Section 5.1\\\\n    priority: P0\\\\n\\\\n  - id: fig2_crossover\\\\n    title: \\\\\\\"Phase-Strategy Crossover Heatmap\\\\\\\"\\\\n    type: heatmap (strategy × phase × sparsity)\\\\n    data_source: v5 importance + random per-phase II values\\\\n    message: >\\\\n      At s=0.25, importance outperforms random in high-sparsity phase (0.584 vs 3.002) but\\\\n      underperforms dramatically in low-sparsity phase (30.903 vs 2.915). Direction reversal\\\\n      is phase-dependent.\\\\n    placement: Section 5.2\\\\n    priority: P0\\\\n\\\\n  - id: fig3_mechanism\\\\n    title: \\\\\\\"Entropy-Discrimination Collapse Illustration\\\\\\\"\\\\n    type: schematic diagram + attention distribution plot\\\\n    data_source: conceptual + optional empirical attention entropy data\\\\n    message: >\\\\n      Head pruning → attention redistribution → importance score entropy increase →\\\\n      discrimination collapse. Explains why importance eviction fails specifically in\\\\n      distributed-attention phases.\\\\n    placement: Section 6\\\\n    priority: P1\\\\n\\\\n  - id: fig4_bootstrap\\\\n    title: \\\\\\\"Bootstrap CI Forest Plot\\\\\\\"\\\\n    type: forest plot\\\\n    data_source: v6 per-problem bootstrap results (B=10000)\\\\n    message: >\\\\n      All 4 sparsity levels show gradient CI entirely above 1.0, p=0.0000.\\\\n      Visual confirmation of statistical significance.\\\\n    placement: Section 5.1\\\\n    priority: P1\\\\n\\\\n  - id: fig5_crossmodel\\\\n    title: \\\\\\\"Cross-Model Replication\\\\\\\"\\\\n    type: grouped bar or side-by-side line plot\\\\n    data_source: Qwen2.5-7B importance results (pending)\\\\n    message: >\\\\n      Phase-modulated severity generalizes beyond DeepSeek to Qwen architecture.\\\\n    placement: Section 5.3\\\\n    priority: P0 (blocked on Qwen experiments)\\\\n\\\\ntables:\\\\n  - id: tab1_main\\\\n    title: \\\\\\\"Main Results: II by Strategy × Phase × Sparsity\\\\\\\"\\\\n    data_source: v5 importance + random, median + IQR\\\\n    columns: [sparsity, strategy, high_phase_II, mid_phase_II, low_phase_II, gradient, gradient_CI]\\\\n    message: Core quantitative claim — strategy × phase interaction\\\\n    placement: Section 5.1\\\\n    priority: P0\\\\n\\\\n  - id: tab2_bootstrap\\\\n    title: \\\\\\\"Bootstrap Confidence Intervals (B=10000)\\\\\\\"\\\\n    data_source: v6 per-problem bootstrap\\\\n    columns: [sparsity, paired_gradient, paired_CI, unpaired_gradient, unpaired_CI, p_value]\\\\n    message: Statistical rigor — all gradients significant\\\\n    placement: Section 5.1\\\\n    priority: P0\\\\n\\\\n  - id: tab3_crossmodel\\\\n    title: \\\\\\\"Cross-Model Comparison: DeepSeek vs Qwen\\\\\\\"\\\\n    data_source: v6 DeepSeek + Qwen importance results (Qwen pending)\\\\n    message: Generalizability beyond single model family\\\\n    placement: Section 5.3\\\\n    priority: P0 (blocked on Qwen)\\\\n\\\\n# ============================================================\\\\n# Claims → Evidence Mapping\\\\n# ============================================================\\\\nclaims:\\\\n  - claim: \\\\\\\"Compound sparsity severity is strategy-dependent\\\\\\\"\\\\n    evidence:\\\\n      - \\\\\\\"v5 importance gradient 12.8-74.9× vs v5 random gradient ~1×\\\\\\\"\\\\n      - \\\\\\\"Bootstrap CI: importance gradient CI lower bound >> 1.0; random gradient CI spans 1.0\\\\\\\"\\\\n    status: confirmed\\\\n\\\\n  - claim: \\\\\\\"Severity is phase-modulated (amplified in low-sparsity reasoning phase)\\\\\\\"\\\\n    evidence:\\\\n      - \\\\\\\"v5 per-phase II: low phase >> high phase for importance at all 4 sparsity levels\\\\\\\"\\\\n      - \\\\\\\"Gradient monotonically increases with sparsity: 12.8→28.7→52.9→74.9\\\\\\\"\\\\n    status: confirmed\\\\n\\\\n  - claim: \\\\\\\"Phase-strategy crossover exists\\\\\\\"\\\\n    evidence:\\\\n      - \\\\\\\"s=0.25: importance high_phase=0.584 < random=3.002, importance low_phase=30.903 > random=2.915\\\\\\\"\\\\n      - \\\\\\\"Direction depends on phase, not just magnitude\\\\\\\"\\\\n    status: confirmed\\\\n\\\\n  - claim: \\\\\\\"Entropy-discrimination collapse explains the mechanism\\\\\\\"\\\\n    evidence:\\\\n      - \\\\\\\"Conceptual argument: head pruning → distributed attention → importance entropy up → discrimination down\\\\\\\"\\\\n      - \\\\\\\"Empirical: importance PPL 26-60× worse than random before metric fix (D012/D013) = metric failure\\\\\\\"\\\\n    status: partially_confirmed (mechanism is explanatory, not directly measured)\\\\n\\\\n  - claim: \\\\\\\"Finding generalizes across model families\\\\\\\"\\\\n    evidence:\\\\n      - \\\\\\\"Qwen2.5-7B-Instruct experiments (pending)\\\\\\\"\\\\n    status: pending\\\\n\\\\n  - claim: \\\\\\\"Severity gradient is sub-exponential\\\\\\\"\\\\n    evidence:\\\\n      - \\\\\\\"Growth rate: 2.24×→1.84×→1.42× (decreasing)\\\\\\\"\\\\n    status: confirmed\\\\n\\\\n# ============================================================\\\\n# Writing Priority & Schedule\\\\n# ============================================================\\\\nwriting_priority:\\\\n  # Phase 1: 可立即写的部分 (Day 1-3, May 14-16)\\\\n  - priority: 1\\\\n    sections: [methodology, background, related_work]\\\\n    reason: \\\\\\\"不依赖 Qwen 结果，数据已完备，先把 methodology infrastructure 写好\\\\\\\"\\\\n    deliverable: \\\\\\\"完整的 Section 3 + 4 + 2 初稿\\\\\\\"\\\\n\\\\n  - priority: 1\\\\n    task: \\\\\\\"fig1_hero + fig2_crossover + tab1_main + tab2_bootstrap\\\\\\\"\\\\n    reason: \\\\\\\"核心数据已有，图表先出可以驱动 narrative\\\\\\\"\\\\n    deliverable: \\\\\\\"4 个核心 figure/table 的 publication-ready 版本\\\\\\\"\\\\n\\\\n  # Phase 2: 核心结果 (Day 3-5, May 16-18)\\\\n  - priority: 2\\\\n    sections: [results_5_1, results_5_2]\\\\n    reason: \\\\\\\"5.1 和 5.2 数据完备，5.3 (cross-model) 需等 Qwen\\\\\\\"\\\\n    deliverable: \\\\\\\"Section 5.1 + 5.2 完整初稿\\\\\\\"\\\\n\\\\n  - priority: 2\\\\n    sections: [analysis]\\\\n    reason: \\\\\\\"机制解释可独立写，不依赖 Qwen\\\\\\\"\\\\n    deliverable: \\\\\\\"Section 6 初稿\\\\\\\"\\\\n\\\\n  # Phase 3: Cross-model + Introduction (Day 5-7, May 18-20)\\\\n  - priority: 3\\\\n    sections: [results_5_3]\\\\n    reason: \\\\\\\"Qwen 实验预计 Day 3-4 出结果\\\\\\\"\\\\n    deliverable: \\\\\\\"Section 5.3 + Table 3 + Fig 5\\\\\\\"\\\\n\\\\n  - priority: 3\\\\n    sections: [introduction]\\\\n    reason: \\\\\\\"Introduction 最后写——需要所有结果确定后才能精确表述 contributions\\\\\\\"\\\\n    deliverable: \\\\\\\"Section 1 完整初稿\\\\\\\"\\\\n\\\\n  # Phase 4: Abstract + Polish (Day 7-9, May 20-22)\\\\n  - priority: 4\\\\n    sections: [abstract, discussion, conclusion]\\\\n    reason: \\\\\\\"总结性段落最后写\\\\\\\"\\\\n    deliverable: \\\\\\\"完整初稿 v1\\\\\\\"\\\\n\\\\n  # Phase 5: Review & Submission (Day 9-11, May 22-25)\\\\n  - priority: 5\\\\n    task: \\\\\\\"Internal review, polish, formatting check, reference audit, submission\\\\\\\"\\\\n    reason: \\\\\\\"留 3 天 buffer 做 revision\\\\\\\"\\\\n    deliverable: \\\\\\\"Camera-ready 提交\\\\\\\"\\\\n\\\\nschedule:\\\\n  - days: \\\\\\\"Day 1-3 (May 14-16)\\\\\\\"\\\\n    tasks:\\\\n      - \\\\\\\"LaTeX 模板搭建 (EMNLP ARR format)\\\\\\\"\\\\n      - \\\\\\\"Section 3 (Background) 初稿\\\\\\\"\\\\n      - \\\\\\\"Section 4 (Methodology) 初稿\\\\\\\"\\\\n      - \\\\\\\"Section 2 (Related Work) 初稿\\\\\\\"\\\\n      - \\\\\\\"Fig 1 (hero), Fig 2 (crossover), Table 1, Table 2 制图\\\\\\\"\\\\n      - \\\\\\\"启动 Qwen cross-model 实验\\\\\\\"\\\\n    milestone: \\\\\\\"方法论部分完成 + 核心图表就绪\\\\\\\"\\\\n\\\\n  - days: \\\\\\\"Day 3-5 (May 16-18)\\\\\\\"\\\\n    tasks:\\\\n      - \\\\\\\"Section 5.1 (severity gradient) 初稿\\\\\\\"\\\\n      - \\\\\\\"Section 5.2 (crossover) 初稿\\\\\\\"\\\\n      - \\\\\\\"Section 6 (analysis/mechanism) 初稿\\\\\\\"\\\\n      - \\\\\\\"Fig 3 (mechanism diagram)\\\\\\\"\\\\n      - \\\\\\\"Fig 4 (bootstrap forest plot)\\\\\\\"\\\\n    milestone: \\\\\\\"结果+分析部分完成\\\\\\\"\\\\n\\\\n  - days: \\\\\\\"Day 5-7 (May 18-20)\\\\\\\"\\\\n    tasks:\\\\n      - \\\\\\\"Qwen 结果整合 → Section 5.3, Table 3, Fig 5\\\\\\\"\\\\n      - \\\\\\\"Section 1 (Introduction) 初稿\\\\\\\"\\\\n      - \\\\\\\"如果 Qwen 结果延迟：先写 conditional 版本，留占位\\\\\\\"\\\\n    milestone: \\\\\\\"主体内容完成\\\\\\\"\\\\n\\\\n  - days: \\\\\\\"Day 7-9 (May 20-22)\\\\\\\"\\\\n    tasks:\\\\n      - \\\\\\\"Abstract 撰写\\\\\\\"\\\\n      - \\\\\\\"Section 7 (Discussion) + Section 8 (Conclusion)\\\\\\\"\\\\n      - \\\\\\\"Appendix: paired bootstrap 详细结果、per-problem 分布\\\\\\\"\\\\n      - \\\\\\\"全文 polish pass 1: 叙事一致性、数据准确性\\\\\\\"\\\\n    milestone: \\\\\\\"完整初稿 v1\\\\\\\"\\\\n\\\\n  - days: \\\\\\\"Day 9-11 (May 22-25)\\\\\\\"\\\\n    tasks:\\\\n      - \\\\\\\"Reference audit (引用完整性+格式)\\\\\\\"\\\\n      - \\\\\\\"Polish pass 2: 语言、格式、ARR checklist\\\\\\\"\\\\n      - \\\\\\\"Limitations section\\\\\\\"\\\\n      - \\\\\\\"Ethics statement (if required)\\\\\\\"\\\\n      - \\\\\\\"最终提交\\\\\\\"\\\\n    milestone: \\\\\\\"提交完成\\\\\\\"\\\\n\\\\n# ============================================================\\\\n# 关键风险\\\\n# ============================================================\\\\nrisks:\\\\n  - risk: \\\\\\\"Qwen cross-model 实验未完成或结果 negative\\\\\\\"\\\\n    mitigation: >\\\\n      如果 Day 5 前无结果：写 conditional 版本 \\\\\\\"we additionally test on Qwen2.5-7B (results pending)\\\\\\\".\\\\n      如果结果 negative：调整 narrative 为 \\\\\\\"model-specific phenomenon requiring further investigation\\\\\\\",\\\\n      仍可作为 finding paper 提交（DeepSeek 数据已足够支撑 core claim）.\\\\n    impact: medium\\\\n\\\\n  - risk: \\\\\\\"11 天写不完\\\\\\\"\\\\n    mitigation: >\\\\n      优先保证 core sections (3-6)，Introduction/Discussion 可以精简。\\\\n      如果时间不够，砍 mechanism analysis (Section 6) 到 1 段 discussion。\\\\n    impact: low (schedule has 3-day buffer)\\\\n\\\\n  - risk: \\\\\\\"Reviewer 质疑 7B-only + MATH-500-only 的 generalizability\\\\\\\"\\\\n    mitigation: >\\\\n      Cross-model (Qwen) 是第一层防御。Limitations 明确声明 scale。\\\\n      MATH-500 是 standard benchmark，defensible。\\\\n    impact: medium\\\\n\\\\n# ============================================================\\\\n# Framing 约束 (Director D015)\\\\n# ============================================================\\\\nframing_constraints:\\\\n  must: \\\\\\\"emergent phase-strategy interaction\\\\\\\"\\\\n  must_not: \\\\\\\"importance metric limitation / importance is broken\\\\\\\"\\\\n  narrative_arc: >\\\\n    Compound sparsity is increasingly used for efficient LLM inference, but its interaction\\\\n    dynamics are poorly understood. We discover that the severity of compound interaction\\\\n    is not a fixed property — it emerges from the interplay of eviction strategy and reasoning\\\\n    phase. Importance-based eviction amplifies compound degradation 12-75× in low-sparsity\\\\n    phases, while random eviction maintains flat interaction. This phase-strategy interaction,\\\\n    explained by entropy-discrimination collapse, challenges the uniform-degradation assumption\\\\n    and motivates phase-aware sparsity allocation.\\\\n\\\", \\\"total_chars\\\": 15664, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/writing_plan.yaml\", \"content\": \"## Writing Plan — Phase-Gated Compound Sparsity\\n## 最后更新: 2026-05-14\\n\\n# ============================================================\\n# 投稿目标\\n# ============================================================\\ntarget:\\n  venue: EMNLP 2026 ARR\\n  deadline: 2026-05-25\\n  days_remaining: 11\\n  format: long paper (8 pages + references + appendix)\\n  anonymization: ARR double-blind\\n\\n# ============================================================\\n# Paper Outline\\n# ============================================================\\noutline:\\n  title_candidates:\\n    - \\\"Phase-Modulated Compound Sparsity: How Eviction Strategy and Reasoning Phase Interact in Sparse LLM Inference\\\"\\n    - \\\"Emergent Phase-Strategy Interaction in Compound Sparse LLM Inference\\\"\\n    - \\\"When Compound Sparsity Bites Back: Phase-Dependent Severity Amplification in Importance-Based Eviction\\\"\\n\\n  sections:\\n    - id: abstract\\n      title: Abstract\\n      summary: >\\n        Compound sparsity (head pruning + KV cache eviction) is assumed to degrade uniformly.\\n        We show the interaction is strategy-dependent and phase-modulated: importance-based eviction\\n        exhibits 12-75× severity amplification in low-sparsity reasoning phases, while random eviction\\n        stays flat (~1×). Bootstrap CI (B=10000) confirms significance at all 4 sparsity levels (p<0.0001).\\n        Cross-model replication on Qwen2.5-7B validates generalizability. We explain this via an\\n        entropy-discrimination collapse mechanism: head pruning distributes surviving attention,\\n        destroying importance score discriminability specifically in distributed-attention phases.\\n      length: 250 words\\n\\n    - id: introduction\\n      title: \\\"1. Introduction\\\"\\n      summary: >\\n        Motivate compound sparsity as practical deployment need. State gap: prior work (SparK, Ada-KV)\\n        treats compound interaction as uniformly super-additive. Our finding: the severity is an\\n        emergent property of the interaction between eviction strategy and reasoning phase.\\n        Preview crossover phenomenon and mechanism. State contributions.\\n      length: 1 page\\n      key_claims:\\n        - Compound sparsity severity is not uniform — it is strategy-dependent and phase-modulated\\n        - Importance-based eviction amplifies compound interaction 12-75× in low-sparsity phases\\n        - Entropy-discrimination collapse explains the phase-strategy interaction\\n\\n    - id: related_work\\n      title: \\\"2. Related Work\\\"\\n      summary: >\\n        Three threads: (1) Compound/joint compression (SparK, SLiM, UniComp, compression-ordering)\\n        — none analyzes phase × strategy interaction. (2) KV cache eviction (Ada-KV, DefensiveKV,\\n        SnapKV, NACL) — importance fragility noted but not phase-conditioned. (3) Phase-aware\\n        inference (ThinKV, PagedEviction, reasoning dynamics) — single-axis, no compound interaction.\\n      length: 0.75 page\\n      key_refs:\\n        - spark-aaai2026\\n        - thinkv-iclr2026\\n        - defensivekv-iclr2026\\n        - slim-icml2025\\n        - phase-transition-compression-2026\\n        - decision-repr-transition-2026\\n        - retentivekv-2026\\n        - greedy-bias-kvcache-2026\\n\\n    - id: background\\n      title: \\\"3. Background and Problem Setup\\\"\\n      summary: >\\n        Define compound sparsity (attention head pruning ⊗ KV cache eviction). Define Interaction\\n        Index (II) measuring super/sub-additivity. Define phase segmentation via ThinKV-style\\n        token-ratio method. Formalize the research question: is II constant across phases and strategies?\\n      length: 1 page\\n      subsections:\\n        - \\\"3.1 Compound Sparsity Formulation\\\"\\n        - \\\"3.2 Interaction Index\\\"\\n        - \\\"3.3 Phase Segmentation\\\"\\n\\n    - id: methodology\\n      title: \\\"4. Experimental Setup\\\"\\n      summary: >\\n        Models (DeepSeek-R1-Distill-Qwen-7B, Qwen2.5-7B-Instruct), dataset (MATH-500 subset, 50 problems),\\n        sparsity levels (s=0.15/0.20/0.25/0.30), eviction strategies (importance-based cumulative\\n        attention with position normalization, random), metrics (PPL, II, gradient), hardware.\\n        Statistical method: per-problem bootstrap CI (B=10000), paired and unpaired.\\n      length: 1 page\\n\\n    - id: results\\n      title: \\\"5. Results\\\"\\n      summary: >\\n        Main finding: importance gradient 11-42× (problem-level bootstrap) increasing with sparsity,\\n        random gradient ~1×. Bootstrap CI all significant (p<0.001 fp16, target p<10⁻⁴ bf16).\\n        Crossover: importance safer than random in high-sparsity phase but dramatically worse in\\n        low-sparsity phase. Sub-exponential growth pattern. Cross-model replication on Qwen.\\n      length: 2.5 pages\\n      subsections:\\n        - \\\"5.0 Experimental Overview (sec:exp-overview)\\\"\\n        - \\\"5.1 Strategy-Dependent Severity — C1 (sec:strategy-severity)\\\"\\n        - \\\"5.2 Phase-Modulated Amplification — C2 (sec:phase-amplification)\\\"\\n        - \\\"5.3 Phase-Strategy Crossover — C3 (sec:crossover)\\\"\\n        - \\\"5.4 Cross-Model Replication — C5 (sec:cross-model)\\\"\\n        - \\\"5.5 Statistical Validation (sec:stat-validation)\\\"\\n\\n    - id: analysis\\n      title: \\\"6. Analysis: Entropy-Discrimination Collapse\\\"\\n      summary: >\\n        Mechanistic explanation: head pruning → surviving heads attend more uniformly → importance\\n        score entropy increases → discrimination between important/unimportant KV entries collapses →\\n        importance-based eviction degrades to biased pseudo-random in distributed-attention phases.\\n        This is phase-dependent because reasoning phases have more distributed attention.\\n      length: 1 page\\n\\n    - id: discussion\\n      title: \\\"7. Discussion\\\"\\n      summary: >\\n        Implications for compound sparsity deployment: uniform budgets are unsafe.\\n        Phase-gated controllers as solution direction. Limitations: 7B models only,\\n        MATH-500 only, no throughput measurements yet.\\n      length: 0.5 page\\n\\n    - id: conclusion\\n      title: \\\"8. Conclusion\\\"\\n      summary: >\\n        Compound sparsity severity is an emergent property of strategy × phase interaction.\\n        This finding challenges the implicit assumption of uniform compound degradation\\n        and motivates phase-aware sparsity allocation.\\n      length: 0.25 page\\n\\n# ============================================================\\n# Figures and Tables\\n# ============================================================\\nfigures:\\n  - id: fig1_hero\\n    title: \\\"Phase-Modulated Severity Gradient (Hero Figure)\\\"\\n    type: line plot or grouped bar\\n    data_source: v5 importance + v5 random segment-level II medians\\n    message: >\\n      Importance gradient rises 12.8-74.9× across sparsity levels while random stays flat ~1×.\\n      The gap between strategies widens with sparsity — this is the core visual claim.\\n    placement: page 1 or Section 5.1\\n    priority: P0\\n\\n  - id: fig2_crossover\\n    title: \\\"Phase-Strategy Crossover Heatmap\\\"\\n    type: heatmap (strategy × phase × sparsity)\\n    data_source: v5 importance + random per-phase II values\\n    message: >\\n      At s=0.25, importance outperforms random in high-sparsity phase (0.584 vs 3.002) but\\n      underperforms dramatically in low-sparsity phase (30.903 vs 2.915). Direction reversal\\n      is phase-dependent.\\n    placement: Section 5.2\\n    priority: P0\\n\\n  - id: fig3_mechanism\\n    title: \\\"Entropy-Discrimination Collapse Illustration\\\"\\n    type: schematic diagram + attention distribution plot\\n    data_source: conceptual + optional empirical attention entropy data\\n    message: >\\n      Head pruning → attention redistribution → importance score entropy increase →\\n      discrimination collapse. Explains why importance eviction fails specifically in\\n      distributed-attention phases.\\n    placement: Section 6\\n    priority: P1\\n\\n  - id: fig4_bootstrap\\n    title: \\\"Bootstrap CI Forest Plot\\\"\\n    type: forest plot\\n    data_source: v6 per-problem bootstrap results (B=10000)\\n    message: >\\n      All 4 sparsity levels show gradient CI entirely above 1.0, p=0.0000.\\n      Visual confirmation of statistical significance.\\n    placement: Section 5.1\\n    priority: P1\\n\\n  - id: fig5_crossmodel\\n    title: \\\"Cross-Model Replication\\\"\\n    type: grouped bar or side-by-side line plot\\n    data_source: Qwen2.5-7B importance results (pending)\\n    message: >\\n      Phase-modulated severity generalizes beyond DeepSeek to Qwen architecture.\\n    placement: Section 5.3\\n    priority: P0 (blocked on Qwen experiments)\\n\\ntables:\\n  - id: tab1_main\\n    title: \\\"Main Results: II by Strategy × Phase × Sparsity\\\"\\n    data_source: v5 importance + random, median + IQR\\n    columns: [sparsity, strategy, high_phase_II, mid_phase_II, low_phase_II, gradient, gradient_CI]\\n    message: Core quantitative claim — strategy × phase interaction\\n    placement: Section 5.1\\n    priority: P0\\n\\n  - id: tab2_bootstrap\\n    title: \\\"Bootstrap Confidence Intervals (B=10000)\\\"\\n    data_source: v6 per-problem bootstrap\\n    columns: [sparsity, paired_gradient, paired_CI, unpaired_gradient, unpaired_CI, p_value]\\n    message: Statistical rigor — all gradients significant\\n    placement: Section 5.1\\n    priority: P0\\n\\n  - id: tab3_crossmodel\\n    title: \\\"Cross-Model Comparison: DeepSeek vs Qwen\\\"\\n    data_source: v6 DeepSeek + Qwen importance results (Qwen pending)\\n    message: Generalizability beyond single model family\\n    placement: Section 5.3\\n    priority: P0 (blocked on Qwen)\\n\\n# ============================================================\\n# Claims → Evidence Mapping\\n# ============================================================\\nclaims:\\n  - claim: \\\"Compound sparsity severity is strategy-dependent\\\"\\n    evidence:\\n      - \\\"v5 importance gradient 12.8-74.9× vs v5 random gradient ~1×\\\"\\n      - \\\"Bootstrap CI: importance gradient CI lower bound >> 1.0; random gradient CI spans 1.0\\\"\\n    status: confirmed\\n\\n  - claim: \\\"Severity is phase-modulated (amplified in low-sparsity reasoning phase)\\\"\\n    evidence:\\n      - \\\"v5 per-phase II: low phase >> high phase for importance at all 4 sparsity levels\\\"\\n      - \\\"Gradient monotonically increases with sparsity: 12.8→28.7→52.9→74.9\\\"\\n    status: confirmed\\n\\n  - claim: \\\"Phase-strategy crossover exists\\\"\\n    evidence:\\n      - \\\"s=0.25: importance high_phase=0.584 < random=3.002, importance low_phase=30.903 > random=2.915\\\"\\n      - \\\"Direction depends on phase, not just magnitude\\\"\\n    status: confirmed\\n\\n  - claim: \\\"Entropy-discrimination collapse explains the mechanism\\\"\\n    evidence:\\n      - \\\"Conceptual argument: head pruning → distributed attention → importance entropy up → discrimination down\\\"\\n      - \\\"Empirical: importance PPL 26-60× worse than random before metric fix (D012/D013) = metric failure\\\"\\n    status: partially_confirmed (mechanism is explanatory, not directly measured)\\n\\n  - claim: \\\"Finding generalizes across model families\\\"\\n    evidence:\\n      - \\\"Qwen2.5-7B-Instruct experiments (pending)\\\"\\n    status: pending\\n\\n  - claim: \\\"Severity gradient is sub-exponential\\\"\\n    evidence:\\n      - \\\"Growth rate: 2.24×→1.84×→1.42× (decreasing)\\\"\\n    status: confirmed\\n\\n# ============================================================\\n# Writing Priority & Schedule\\n# ============================================================\\nwriting_priority:\\n  # Phase 1: 可立即写的部分 (Day 1-3, May 14-16)\\n  - priority: 1\\n    sections: [methodology, background, related_work]\\n    reason: \\\"不依赖 Qwen 结果，数据已完备，先把 methodology infrastructure 写好\\\"\\n    deliverable: \\\"完整的 Section 3 + 4 + 2 初稿\\\"\\n\\n  - priority: 1\\n    task: \\\"fig1_hero + fig2_crossover + tab1_main + tab2_bootstrap\\\"\\n    reason: \\\"核心数据已有，图表先出可以驱动 narrative\\\"\\n    deliverable: \\\"4 个核心 figure/table 的 publication-ready 版本\\\"\\n\\n  # Phase 2: 核心结果 (Day 3-5, May 16-18)\\n  - priority: 2\\n    sections: [results_5_1, results_5_2]\\n    reason: \\\"5.1 和 5.2 数据完备，5.3 (cross-model) 需等 Qwen\\\"\\n    deliverable: \\\"Section 5.1 + 5.2 完整初稿\\\"\\n\\n  - priority: 2\\n    sections: [analysis]\\n    reason: \\\"机制解释可独立写，不依赖 Qwen\\\"\\n    deliverable: \\\"Section 6 初稿\\\"\\n\\n  # Phase 3: Cross-model + Introduction (Day 5-7, May 18-20)\\n  - priority: 3\\n    sections: [results_5_3]\\n    reason: \\\"Qwen 实验预计 Day 3-4 出结果\\\"\\n    deliverable: \\\"Section 5.3 + Table 3 + Fig 5\\\"\\n\\n  - priority: 3\\n    sections: [introduction]\\n    reason: \\\"Introduction 最后写——需要所有结果确定后才能精确表述 contributions\\\"\\n    deliverable: \\\"Section 1 完整初稿\\\"\\n\\n  # Phase 4: Abstract + Polish (Day 7-9, May 20-22)\\n  - priority: 4\\n    sections: [abstract, discussion, conclusion]\\n    reason: \\\"总结性段落最后写\\\"\\n    deliverable: \\\"完整初稿 v1\\\"\\n\\n  # Phase 5: Review & Submission (Day 9-11, May 22-25)\\n  - priority: 5\\n    task: \\\"Internal review, polish, formatting check, reference audit, submission\\\"\\n    reason: \\\"留 3 天 buffer 做 revision\\\"\\n    deliverable: \\\"Camera-ready 提交\\\"\\n\\nschedule:\\n  - days: \\\"Day 1-3 (May 14-16)\\\"\\n    tasks:\\n      - \\\"LaTeX 模板搭建 (EMNLP ARR format)\\\"\\n      - \\\"Section 3 (Background) 初稿\\\"\\n      - \\\"Section 4 (Methodology) 初稿\\\"\\n      - \\\"Section 2 (Related Work) 初稿\\\"\\n      - \\\"Fig 1 (hero), Fig 2 (crossover), Table 1, Table 2 制图\\\"\\n      - \\\"启动 Qwen cross-model 实验\\\"\\n    milestone: \\\"方法论部分完成 + 核心图表就绪\\\"\\n\\n  - days: \\\"Day 3-5 (May 16-18)\\\"\\n    tasks:\\n      - \\\"Section 5.1 (severity gradient) 初稿\\\"\\n      - \\\"Section 5.2 (crossover) 初稿\\\"\\n      - \\\"Section 6 (analysis/mechanism) 初稿\\\"\\n      - \\\"Fig 3 (mechanism diagram)\\\"\\n      - \\\"Fig 4 (bootstrap forest plot)\\\"\\n    milestone: \\\"结果+分析部分完成\\\"\\n\\n  - days: \\\"Day 5-7 (May 18-20)\\\"\\n    tasks:\\n      - \\\"Qwen 结果整合 → Section 5.3, Table 3, Fig 5\\\"\\n      - \\\"Section 1 (Introduction) 初稿\\\"\\n      - \\\"如果 Qwen 结果延迟：先写 conditional 版本，留占位\\\"\\n    milestone: \\\"主体内容完成\\\"\\n\\n  - days: \\\"Day 7-9 (May 20-22)\\\"\\n    tasks:\\n      - \\\"Abstract 撰写\\\"\\n      - \\\"Section 7 (Discussion) + Section 8 (Conclusion)\\\"\\n      - \\\"Appendix: paired bootstrap 详细结果、per-problem 分布\\\"\\n      - \\\"全文 polish pass 1: 叙事一致性、数据准确性\\\"\\n    milestone: \\\"完整初稿 v1\\\"\\n\\n  - days: \\\"Day 9-11 (May 22-25)\\\"\\n    tasks:\\n      - \\\"Reference audit (引用完整性+格式)\\\"\\n      - \\\"Polish pass 2: 语言、格式、ARR checklist\\\"\\n      - \\\"Limitations section\\\"\\n      - \\\"Ethics statement (if required)\\\"\\n      - \\\"最终提交\\\"\\n    milestone: \\\"提交完成\\\"\\n\\n# ============================================================\\n# 关键风险\\n# ============================================================\\nrisks:\\n  - risk: \\\"Qwen cross-model 实验未完成或结果 negative\\\"\\n    mitigation: >\\n      如果 Day 5 前无结果：写 conditional 版本 \\\"we additionally test on Qwen2.5-7B (results pending)\\\".\\n      如果结果 negative：调整 narrative 为 \\\"model-specific phenomenon requiring further investigation\\\",\\n      仍可作为 finding paper 提交（DeepSeek 数据已足够支撑 core claim）.\\n    impact: medium\\n\\n  - risk: \\\"11 天写不完\\\"\\n    mitigation: >\\n      优先保证 core sections (3-6)，Introduction/Discussion 可以精简。\\n      如果时间不够，砍 mechanism analysis (Section 6) 到 1 段 discussion。\\n    impact: low (schedule has 3-day buffer)\\n\\n  - risk: \\\"Reviewer 质疑 7B-only + MATH-500-only 的 generalizability\\\"\\n    mitigation: >\\n      Cross-model (Qwen) 是第一层防御。Limitations 明确声明 scale。\\n      MATH-500 是 standard benchmark，defensible。\\n    impact: medium\\n\\n# ============================================================\\n# Framing 约束 (Director D015)\\n# ============================================================\\nframing_constraints:\\n  must: \\\"emergent phase-strategy interaction\\\"\\n  must_not: \\\"importance metric limitation / importance is broken\\\"\\n  narrative_arc: >\\n    Compound sparsity is increasingly used for efficient LLM inference, but its interaction\\n    dynamics are poorly understood. We discover that the severity of compound interaction\\n    is not a fixed property — it emerges from the interplay of eviction strategy and reasoning\\n    phase. Importance-based eviction amplifies compound degradation 12-75× in low-sparsity\\n    phases, while random eviction maintains flat interaction. This phase-strategy interaction,\\n    explained by entropy-discrimination collapse, challenges the uniform-degradation assumption\\n    and motivates phase-aware sparsity allocation.\\n\", \"total_chars\": 15664, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01XfJ4smGWqrUy6WNX885wgb`</summary>

```json
{
  "project": "phase-gated-compound-sparse",
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
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "98c9d77b-b69f-4018-9cfb-9fd30c801710",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U2D2Mof3DyEqrNdSv9s29q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 772,
      "cache_read_input_tokens": 23374,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 772
      },
      "output_tokens": 70,
      "service_tier": "standard",
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

_source line 13 · 2026-05-14T20:42:58.657Z_

<details><summary>↩ Tool result · `toolu_01XfJ4smGWqrUy6WNX885wgb`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/literature_map.yaml\", \"content\": \"## Literature Map — Phase-Gated Compound Sparsity\\n## 增量扫描: 2026-05-14\\n\\n# ============================================================\\n# 已知文献（baseline）\\n# ============================================================\\n\\n- paper_id: spark-aaai2026\\n  title: \\\"SparK: Query-Aware Unstructured Sparsity with Recoverable KV Cache Channel Pruning\\\"\\n  venue: AAAI 2026\\n  year: 2026\\n  category: direct-competitor\\n  relevance: 首篇报告 compound sparsity 总是 super-additive（ThinK+SnapKV 退化 65%），核心对标\\n  key_finding: compound KV cache sparsity (channel + token) 产生 super-additive degradation\\n\\n- paper_id: thinkv-iclr2026\\n  title: \\\"ThinKV\\\"\\n  venue: ICLR 2026 Oral\\n  year: 2026\\n  category: method-component\\n  relevance: phase 划分思想来源，但只做单一压缩策略\\n  key_finding: KV cache 可按 phase 划分应用不同策略\\n\\n- paper_id: rac-neurips2025\\n  title: \\\"RAC\\\"\\n  venue: NeurIPS 2025\\n  year: 2025\\n  category: background\\n  relevance: reasoning model 对 sparsity 更敏感，支撑评估任务选择\\n  key_finding: reasoning model 对 sparsity 敏感度高于一般 LLM\\n\\n- paper_id: raas-acl2025\\n  title: \\\"RaaS\\\"\\n  venue: ACL 2025\\n  year: 2025\\n  category: method-component\\n  relevance: milestone tokens 先重要后衰减，支撑 phase-dependent importance\\n  key_finding: token importance 随 decoding phase 非单调变化\\n\\n- paper_id: mixeddimkv-2026\\n  title: \\\"MixedDimKV\\\"\\n  year: 2026\\n  category: method-component\\n  relevance: multi-dimension compression budget allocation，与 joint controller 思路平行\\n  key_finding: 多维度压缩 budget allocation 优于均匀分配\\n\\n# ============================================================\\n# 新增 — Compound / Joint Compression Interaction\\n# ============================================================\\n\\n- paper_id: slim-icml2025\\n  title: \\\"SLiM: One-shot Quantization and Sparsity with Low-rank Approximation for LLM Weight Compression\\\"\\n  authors: Mozaffari et al.\\n  venue: ICML 2025\\n  year: 2025\\n  category: method-component\\n  relevance: 首个正式处理 compound compression error 的框架——用 low-rank adapter 补偿 Q+S 聚合误差，证明误差非加性\\n  key_finding: quantization + sparsity 聚合误差非加性；invertible saliency function 精确计算 low-rank 补偿\\n\\n- paper_id: unicomp-2026\\n  title: \\\"UniComp: A Unified Evaluation of Large Language Model Compression via Pruning, Quantization and Distillation\\\"\\n  authors: Wang et al.\\n  venue: arXiv 2602.09130\\n  year: 2026\\n  category: evaluation\\n  relevance: 40+ benchmarks 系统评估 compound compression，发现 compression 有 consistent knowledge bias\\n  key_finding: compression 对 knowledge-intensive tasks 保留好但 reasoning/multilingual 显著退化；quantization 整体 trade-off 最佳\\n\\n- paper_id: compression-ordering-2025\\n  title: \\\"A Systematic Study of Compression Ordering for Large Language Models\\\"\\n  venue: arXiv 2511.19495\\n  year: 2025\\n  category: background\\n  relevance: 证明 compound compression ordering 显著影响结果，early quantization 造成不可逆信息损失\\n  key_finding: P→KD→Q 最优；quantization first 产生不可逆退化；interaction 依赖 ordering\\n\\n- paper_id: phase-transition-compression-2026\\n  title: \\\"Phase Transitions in Large Language Model Compression\\\"\\n  authors: Ma et al.\\n  venue: npj Artificial Intelligence (Nature), 2026\\n  year: 2026\\n  category: background\\n  relevance: 直接支撑 phase-gating 理论动机——不同压缩维度有独立 phase transition point，联合安全区可叠加\\n  key_finding: structured pruning 30-45% 崩溃，unstructured 55-65%；多维度 PTP 正交，联合安全区可实现 10% 压缩\\n\\n- paper_id: graspune-acl2026\\n  title: \\\"GRASPrune: Global Gating for Budgeted Structured Pruning of Large Language Models\\\"\\n  authors: Wang et al.\\n  venue: ACL 2026 Main\\n  year: 2026\\n  category: direct-competitor\\n  relevance: 最直接 competitor——联合 pruning FFN channels + KV head groups with learned gate scores under global budget\\n  key_finding: learned gate + projected STE 全局 budget 下联合 prune FFN+heads，高压缩比下显著优于逐层独立 pruning\\n\\n- paper_id: mustafar-neurips2025\\n  title: \\\"MUSTAFAR: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference\\\"\\n  authors: Joo et al.\\n  venue: NeurIPS 2025\\n  year: 2025\\n  category: method-component\\n  relevance: per-token magnitude pruning 70% sparsity 无损，与 token eviction 可组合——potential compound baseline\\n  key_finding: unstructured KV sparsity (per-token magnitude) 70% 无损，bitmap 格式 2.23x throughput\\n\\n# ============================================================\\n# 新增 — Non-monotonic / Sign Reversal / Phase Effects\\n# ============================================================\\n\\n- paper_id: decision-repr-transition-2026\\n  title: \\\"Understanding Performance Collapse in Layer-Pruned LLMs via Decision Representation Transitions\\\"\\n  venue: arXiv 2605.07271\\n  year: 2026\\n  category: background\\n  relevance: layer pruning 存在 Silent/Decisive Phase 二分——pruning 敏感度 phase-dependent，直接支撑 phase-gated 思想\\n  key_finding: Decision Margin 在 Transition Point 发生符号反转（负→正）；pruning Silent Phase 崩溃，Decisive Phase 可安全 prune\\n\\n- paper_id: doing-more-with-less-2026\\n  title: \\\"Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling\\\"\\n  venue: arXiv 2604.25098\\n  year: 2026\\n  category: background\\n  relevance: 符号反转直接证据——unstructured pruning + TTS 可超越未剪枝模型\\n  key_finding: unstructured pruning + test-time scaling 可超越 unpruned baseline（Qwen3-8B）；structured pruning 严重退化\\n\\n- paper_id: sparse-frontier-2025\\n  title: \\\"The Sparse Frontier: Sparse Attention Trade-offs in Transformer LLMs\\\"\\n  venue: arXiv 2504.17768\\n  year: 2025\\n  category: evaluation\\n  relevance: 最大规模 sparse attention 评估，无通用最优策略，trade-off 依赖 task 和 phase\\n  key_finding: decoding vs prefilling 可承受 sparsity 不同；大模型+高稀疏可优于小模型+密集\\n\\n# ============================================================\\n# 新增 — Adaptive / Learned Controllers\\n# ============================================================\\n\\n- paper_id: obcache-2025\\n  title: \\\"OBCache: Optimal Brain KV Cache Pruning for Efficient Long-Context LLM Inference\\\"\\n  venue: arXiv 2510.07651\\n  year: 2025\\n  category: method-component\\n  relevance: OBD 理论推导 joint K-V saliency score，可作为 importance-based masking 的理论参照\\n  key_finding: 二阶 Taylor 近似推导 joint K-V pruning score；key-pruning 比 value-pruning 影响更大\\n\\n- paper_id: pagedeviction-eacl2026\\n  title: \\\"PagedEviction: Structured Block-wise KV Cache Pruning\\\"\\n  venue: EACL 2026 Findings\\n  year: 2026\\n  category: method-component\\n  relevance: prefill/decode 两阶段不同 eviction 策略，呼应 phase-gated 思想\\n  key_finding: block-wise eviction prefill/decode 分阶段执行，优于 token-level baselines\\n\\n- paper_id: adakv-neurips2025\\n  title: \\\"Ada-KV: Adaptive Budget Allocation for KV Cache Eviction\\\"\\n  venue: NeurIPS 2025\\n  year: 2025\\n  category: method-component\\n  relevance: per-head adaptive budget 分配，与 per-phase budget allocation 正交互补\\n  key_finding: 自适应 per-head KV cache budget 优于均匀分配\\n\\n- paper_id: sol-2026\\n  title: \\\"SOL: Self-Optimizing Language Models — Compute Where it Counts\\\"\\n  venue: arXiv 2605.10875\\n  year: 2026\\n  category: method-component\\n  relevance: learned policy 按 token difficulty 分配 compute，与 learned joint controller 方法论平行\\n  key_finding: 学习 per-token compute allocation policy，easy tokens 少算 hard tokens 多算\\n\\n# ============================================================\\n# 新增 — Phase-Adaptive Dynamic Compression (2026-05-14 scan)\\n# ============================================================\\n\\n- paper_id: twilight-neurips2025\\n  title: \\\"Twilight: Adaptive Attention Sparsity with Hierarchical Top-p Pruning\\\"\\n  authors: Lin, Tang, Yang, Wang, Tang, Tian, Stoica, Han, Gao\\n  venue: NeurIPS 2025 Spotlight\\n  year: 2025\\n  category: method-component\\n  relevance: 证明 fixed budget 次优，per-step adaptive budget 更优；但单轴无 compound interaction\\n  key_finding: top-p 采样思想做 per-step adaptive attention budget，最多 prune 98% tokens\\n\\n- paper_id: lava-emnlp2025\\n  title: \\\"LAVa: Layer-wise KV Cache Eviction with Dynamic Budget Allocation\\\"\\n  authors: Shen, Yuan, Zhang, Wang, Jiang, Nguyen\\n  venue: EMNLP 2025 Findings\\n  year: 2025\\n  category: method-component\\n  relevance: layer budgets 对 generation 重要、head budgets 对 extraction 重要——支撑 task-conditional budget\\n  key_finding: 基于 Layer Attention Output Loss 的 unified eviction + dynamic budget；budget 需求 task-dependent\\n\\n- paper_id: lkv-2026\\n  title: \\\"LKV: End-to-End Learning of Head-wise Budgets and Token Selection for LLM KV Cache Eviction\\\"\\n  venue: arXiv 2605.06676\\n  year: 2026\\n  category: method-component\\n  relevance: 首个端到端可微 budget+selection 联合学习框架；可作 phase-gated controller backbone\\n  key_finding: LKV-H 学 head budget + LKV-T 学 token selection，全面超越启发式方法\\n\\n- paper_id: defensivekv-iclr2026\\n  title: \\\"DefensiveKV: Taming the Fragility of KV Cache Eviction in LLM Inference\\\"\\n  venue: ICLR 2026\\n  year: 2026\\n  category: direct-competitor\\n  relevance: 独立发现 importance-based eviction 的脆弱性——stability assumption 不成立，importance 高度非稳态\\n  key_finding: mean aggregation 在极端情况下 vulnerable；defensive aggregation 控制 worst-case risk，2.3-4.3x 质量损失降低\\n\\n- paper_id: retentivekv-2026\\n  title: \\\"RetentiveKV: State-Space Memory for Uncertainty-Aware Multimodal KV Cache Eviction\\\"\\n  venue: arXiv 2605.04075\\n  year: 2026\\n  category: background\\n  relevance: \\\"Deferred Importance\\\" 现象——token 初始 salience 低但后期变 pivotal，直接支撑 crossover 机制\\n  key_finding: 视觉 tokens 存在 deferred importance——早期不重要晚期关键；单一时刻 importance 评估不可靠\\n\\n- paper_id: pitfalls-kvcache-2025\\n  title: \\\"The Pitfalls of KV Cache Compression\\\"\\n  venue: arXiv 2510.00231\\n  year: 2025\\n  category: background\\n  relevance: multi-instruction 场景下部分指令被压缩严重忽略——condition-dependent failure\\n  key_finding: 特定 instructions 在压缩下退化极快甚至完全被忽略；compression method + order 产生 bias 交互\\n\\n- paper_id: greedy-bias-kvcache-2026\\n  title: \\\"More Than a Quick Glance: Overcoming the Greedy Bias in KV-Cache Compression\\\"\\n  venue: arXiv 2602.02199\\n  year: 2026\\n  category: background\\n  relevance: 单一 attention-score metric 是 greedy 的——miss structurally relevant tokens\\n  key_finding: 单 metric 有 greedy bias；multi-metric scoring 克服 condition-dependent metric failure\\n\\n- paper_id: thinking-tokens-mi-neurips2025\\n  title: \\\"Demystifying Reasoning Dynamics with Mutual Information: Thinking Tokens are Information Peaks\\\"\\n  venue: NeurIPS 2025\\n  year: 2025\\n  category: background\\n  relevance: reasoning 中 MI 在 thinking tokens 处突然 peak——compression 需避开 info-critical phases\\n  key_finding: thinking tokens (Hmm/Wait/Therefore) 处 MI 突增；这些 tokens 对推理性能不成比例重要\\n\\n- paper_id: lserve-mlsys2025\\n  title: \\\"LServe: Efficient Long-sequence LLM Serving with Unified Sparse Attention\\\"\\n  venue: MLSys 2025\\n  year: 2025\\n  category: background\\n  relevance: sparse attention + KV quantization 工业级联合部署但无 interaction 分析\\n  key_finding: 统一 static/dynamic sparsity + KV quant 到单 GPU kernel；prefilling 2.9x 加速\\n\\n- paper_id: squeezeattention-iclr2025\\n  title: \\\"SqueezeAttention: 2D Management of KV-Cache via Layer-wise Optimal Budget\\\"\\n  venue: ICLR 2025\\n  year: 2025\\n  category: method-component\\n  relevance: layer × sequence 二维 budget 优化；我们增加第三维——temporal phase\\n  key_finding: layer-wise cosine similarity 区分 layer 重要性，30-70% memory reduction\\n\\n- paper_id: nsa-acl2025\\n  title: \\\"NSA: Native Sparse Attention\\\"\\n  authors: DeepSeek\\n  venue: ACL 2025 Best Paper\\n  year: 2025\\n  category: background\\n  relevance: hardware-aligned trainable sparse attention；hierarchical 策略（coarse compression + fine selection）呼应 multi-phase\\n  key_finding: 端到端可训练 sparse attention，64k 解码 11.6x 加速；coarse+fine 分层策略\\n\\n- paper_id: evicpress-2025\\n  title: \\\"EVICPRESS: Joint KV-Cache Compression and Eviction for Efficient LLM Serving\\\"\\n  venue: arXiv 2512.14946\\n  year: 2025\\n  category: method-component\\n  relevance: 联合 eviction + quantization 优化 KV cache——compound 方向但仅 KV 内部\\n  key_finding: joint eviction + quantization 优于独立应用；但无 head pruning compound\\n\\n- paper_id: phase-transition-pruning-thermo-2026\\n  title: \\\"Phase Transitions in Neural Networks Pruning (Thermodynamic Analysis)\\\"\\n  venue: arXiv 2602.15224\\n  year: 2026\\n  category: background\\n  relevance: 自由能分析预测 sharp collapse；transition 前稳定 3-5%，跨越后 30%+ 骤降\\n  key_finding: free-energy phase transition 预测 pruning 崩溃点；importance 方法可能在某 phase 跨越 PTP\\n\\n- paper_id: token-budget-aware-acl2025\\n  title: \\\"Token-Budget-Aware LLM Reasoning\\\"\\n  venue: ACL 2025 Findings\\n  year: 2025\\n  category: background\\n  relevance: reasoning budget 应按 query 难度自适应分配——支撑 phase-adaptive compression\\n  key_finding: self-consistency 作为 thinking necessity proxy 动态调整 reasoning token budget\\n\\n# ============================================================\\n# 新增 — C5b Negative Result 文献联动 (2026-05-14)\\n# ============================================================\\n\\n- paper_id: physics-kvcache-2026\\n  title: \\\"Understanding the Physics of Key-Value Cache Compression for LLMs through Attention Dynamics\\\"\\n  venue: arXiv 2603.01426\\n  year: 2026\\n  category: background\\n  relevance: 直接解释 C5b negative——representational rigidity 使 budget redistribution 无法修复 routing collapse；90% 附近存在 sharp hallucination cliff (phase transition)\\n  key_finding: head-level consensus 过度导致 representational rigidity，token 存活但 routing flexibility 崩溃；compression 存在 sharp safety cliff 对应 semantic reachability phase transition\\n\\n- paper_id: rkv-neurips2025\\n  title: \\\"R-KV: Redundancy-aware KV Cache Compression for Reasoning Models\\\"\\n  authors: Cai et al.\\n  venue: NeurIPS 2025\\n  year: 2025\\n  category: method-component\\n  relevance: reasoning model 专用单轴 KV compression，10% cache 保留 ~100% 性能；但不涉及 compound interaction，与 C5b failure 机制不直接相关\\n  key_finding: importance + non-redundancy 双准则 token ranking，10% KV cache 保留全精度性能；单轴方法无 compound 讨论\\n\", \"total_chars\": 13069, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "56bf0cc7-a92a-42a1-9abd-89cb8c4a87c7",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/literature_map.yaml\\\", \\\"content\\\": \\\"## Literature Map — Phase-Gated Compound Sparsity\\\\n## 增量扫描: 2026-05-14\\\\n\\\\n# ============================================================\\\\n# 已知文献（baseline）\\\\n# ============================================================\\\\n\\\\n- paper_id: spark-aaai2026\\\\n  title: \\\\\\\"SparK: Query-Aware Unstructured Sparsity with Recoverable KV Cache Channel Pruning\\\\\\\"\\\\n  venue: AAAI 2026\\\\n  year: 2026\\\\n  category: direct-competitor\\\\n  relevance: 首篇报告 compound sparsity 总是 super-additive（ThinK+SnapKV 退化 65%），核心对标\\\\n  key_finding: compound KV cache sparsity (channel + token) 产生 super-additive degradation\\\\n\\\\n- paper_id: thinkv-iclr2026\\\\n  title: \\\\\\\"ThinKV\\\\\\\"\\\\n  venue: ICLR 2026 Oral\\\\n  year: 2026\\\\n  category: method-component\\\\n  relevance: phase 划分思想来源，但只做单一压缩策略\\\\n  key_finding: KV cache 可按 phase 划分应用不同策略\\\\n\\\\n- paper_id: rac-neurips2025\\\\n  title: \\\\\\\"RAC\\\\\\\"\\\\n  venue: NeurIPS 2025\\\\n  year: 2025\\\\n  category: background\\\\n  relevance: reasoning model 对 sparsity 更敏感，支撑评估任务选择\\\\n  key_finding: reasoning model 对 sparsity 敏感度高于一般 LLM\\\\n\\\\n- paper_id: raas-acl2025\\\\n  title: \\\\\\\"RaaS\\\\\\\"\\\\n  venue: ACL 2025\\\\n  year: 2025\\\\n  category: method-component\\\\n  relevance: milestone tokens 先重要后衰减，支撑 phase-dependent importance\\\\n  key_finding: token importance 随 decoding phase 非单调变化\\\\n\\\\n- paper_id: mixeddimkv-2026\\\\n  title: \\\\\\\"MixedDimKV\\\\\\\"\\\\n  year: 2026\\\\n  category: method-component\\\\n  relevance: multi-dimension compression budget allocation，与 joint controller 思路平行\\\\n  key_finding: 多维度压缩 budget allocation 优于均匀分配\\\\n\\\\n# ============================================================\\\\n# 新增 — Compound / Joint Compression Interaction\\\\n# ============================================================\\\\n\\\\n- paper_id: slim-icml2025\\\\n  title: \\\\\\\"SLiM: One-shot Quantization and Sparsity with Low-rank Approximation for LLM Weight Compression\\\\\\\"\\\\n  authors: Mozaffari et al.\\\\n  venue: ICML 2025\\\\n  year: 2025\\\\n  category: method-component\\\\n  relevance: 首个正式处理 compound compression error 的框架——用 low-rank adapter 补偿 Q+S 聚合误差，证明误差非加性\\\\n  key_finding: quantization + sparsity 聚合误差非加性；invertible saliency function 精确计算 low-rank 补偿\\\\n\\\\n- paper_id: unicomp-2026\\\\n  title: \\\\\\\"UniComp: A Unified Evaluation of Large Language Model Compression via Pruning, Quantization and Distillation\\\\\\\"\\\\n  authors: Wang et al.\\\\n  venue: arXiv 2602.09130\\\\n  year: 2026\\\\n  category: evaluation\\\\n  relevance: 40+ benchmarks 系统评估 compound compression，发现 compression 有 consistent knowledge bias\\\\n  key_finding: compression 对 knowledge-intensive tasks 保留好但 reasoning/multilingual 显著退化；quantization 整体 trade-off 最佳\\\\n\\\\n- paper_id: compression-ordering-2025\\\\n  title: \\\\\\\"A Systematic Study of Compression Ordering for Large Language Models\\\\\\\"\\\\n  venue: arXiv 2511.19495\\\\n  year: 2025\\\\n  category: background\\\\n  relevance: 证明 compound compression ordering 显著影响结果，early quantization 造成不可逆信息损失\\\\n  key_finding: P→KD→Q 最优；quantization first 产生不可逆退化；interaction 依赖 ordering\\\\n\\\\n- paper_id: phase-transition-compression-2026\\\\n  title: \\\\\\\"Phase Transitions in Large Language Model Compression\\\\\\\"\\\\n  authors: Ma et al.\\\\n  venue: npj Artificial Intelligence (Nature), 2026\\\\n  year: 2026\\\\n  category: background\\\\n  relevance: 直接支撑 phase-gating 理论动机——不同压缩维度有独立 phase transition point，联合安全区可叠加\\\\n  key_finding: structured pruning 30-45% 崩溃，unstructured 55-65%；多维度 PTP 正交，联合安全区可实现 10% 压缩\\\\n\\\\n- paper_id: graspune-acl2026\\\\n  title: \\\\\\\"GRASPrune: Global Gating for Budgeted Structured Pruning of Large Language Models\\\\\\\"\\\\n  authors: Wang et al.\\\\n  venue: ACL 2026 Main\\\\n  year: 2026\\\\n  category: direct-competitor\\\\n  relevance: 最直接 competitor——联合 pruning FFN channels + KV head groups with learned gate scores under global budget\\\\n  key_finding: learned gate + projected STE 全局 budget 下联合 prune FFN+heads，高压缩比下显著优于逐层独立 pruning\\\\n\\\\n- paper_id: mustafar-neurips2025\\\\n  title: \\\\\\\"MUSTAFAR: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference\\\\\\\"\\\\n  authors: Joo et al.\\\\n  venue: NeurIPS 2025\\\\n  year: 2025\\\\n  category: method-component\\\\n  relevance: per-token magnitude pruning 70% sparsity 无损，与 token eviction 可组合——potential compound baseline\\\\n  key_finding: unstructured KV sparsity (per-token magnitude) 70% 无损，bitmap 格式 2.23x throughput\\\\n\\\\n# ============================================================\\\\n# 新增 — Non-monotonic / Sign Reversal / Phase Effects\\\\n# ============================================================\\\\n\\\\n- paper_id: decision-repr-transition-2026\\\\n  title: \\\\\\\"Understanding Performance Collapse in Layer-Pruned LLMs via Decision Representation Transitions\\\\\\\"\\\\n  venue: arXiv 2605.07271\\\\n  year: 2026\\\\n  category: background\\\\n  relevance: layer pruning 存在 Silent/Decisive Phase 二分——pruning 敏感度 phase-dependent，直接支撑 phase-gated 思想\\\\n  key_finding: Decision Margin 在 Transition Point 发生符号反转（负→正）；pruning Silent Phase 崩溃，Decisive Phase 可安全 prune\\\\n\\\\n- paper_id: doing-more-with-less-2026\\\\n  title: \\\\\\\"Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling\\\\\\\"\\\\n  venue: arXiv 2604.25098\\\\n  year: 2026\\\\n  category: background\\\\n  relevance: 符号反转直接证据——unstructured pruning + TTS 可超越未剪枝模型\\\\n  key_finding: unstructured pruning + test-time scaling 可超越 unpruned baseline（Qwen3-8B）；structured pruning 严重退化\\\\n\\\\n- paper_id: sparse-frontier-2025\\\\n  title: \\\\\\\"The Sparse Frontier: Sparse Attention Trade-offs in Transformer LLMs\\\\\\\"\\\\n  venue: arXiv 2504.17768\\\\n  year: 2025\\\\n  category: evaluation\\\\n  relevance: 最大规模 sparse attention 评估，无通用最优策略，trade-off 依赖 task 和 phase\\\\n  key_finding: decoding vs prefilling 可承受 sparsity 不同；大模型+高稀疏可优于小模型+密集\\\\n\\\\n# ============================================================\\\\n# 新增 — Adaptive / Learned Controllers\\\\n# ============================================================\\\\n\\\\n- paper_id: obcache-2025\\\\n  title: \\\\\\\"OBCache: Optimal Brain KV Cache Pruning for Efficient Long-Context LLM Inference\\\\\\\"\\\\n  venue: arXiv 2510.07651\\\\n  year: 2025\\\\n  category: method-component\\\\n  relevance: OBD 理论推导 joint K-V saliency score，可作为 importance-based masking 的理论参照\\\\n  key_finding: 二阶 Taylor 近似推导 joint K-V pruning score；key-pruning 比 value-pruning 影响更大\\\\n\\\\n- paper_id: pagedeviction-eacl2026\\\\n  title: \\\\\\\"PagedEviction: Structured Block-wise KV Cache Pruning\\\\\\\"\\\\n  venue: EACL 2026 Findings\\\\n  year: 2026\\\\n  category: method-component\\\\n  relevance: prefill/decode 两阶段不同 eviction 策略，呼应 phase-gated 思想\\\\n  key_finding: block-wise eviction prefill/decode 分阶段执行，优于 token-level baselines\\\\n\\\\n- paper_id: adakv-neurips2025\\\\n  title: \\\\\\\"Ada-KV: Adaptive Budget Allocation for KV Cache Eviction\\\\\\\"\\\\n  venue: NeurIPS 2025\\\\n  year: 2025\\\\n  category: method-component\\\\n  relevance: per-head adaptive budget 分配，与 per-phase budget allocation 正交互补\\\\n  key_finding: 自适应 per-head KV cache budget 优于均匀分配\\\\n\\\\n- paper_id: sol-2026\\\\n  title: \\\\\\\"SOL: Self-Optimizing Language Models — Compute Where it Counts\\\\\\\"\\\\n  venue: arXiv 2605.10875\\\\n  year: 2026\\\\n  category: method-component\\\\n  relevance: learned policy 按 token difficulty 分配 compute，与 learned joint controller 方法论平行\\\\n  key_finding: 学习 per-token compute allocation policy，easy tokens 少算 hard tokens 多算\\\\n\\\\n# ============================================================\\\\n# 新增 — Phase-Adaptive Dynamic Compression (2026-05-14 scan)\\\\n# ============================================================\\\\n\\\\n- paper_id: twilight-neurips2025\\\\n  title: \\\\\\\"Twilight: Adaptive Attention Sparsity with Hierarchical Top-p Pruning\\\\\\\"\\\\n  authors: Lin, Tang, Yang, Wang, Tang, Tian, Stoica, Han, Gao\\\\n  venue: NeurIPS 2025 Spotlight\\\\n  year: 2025\\\\n  category: method-component\\\\n  relevance: 证明 fixed budget 次优，per-step adaptive budget 更优；但单轴无 compound interaction\\\\n  key_finding: top-p 采样思想做 per-step adaptive attention budget，最多 prune 98% tokens\\\\n\\\\n- paper_id: lava-emnlp2025\\\\n  title: \\\\\\\"LAVa: Layer-wise KV Cache Eviction with Dynamic Budget Allocation\\\\\\\"\\\\n  authors: Shen, Yuan, Zhang, Wang, Jiang, Nguyen\\\\n  venue: EMNLP 2025 Findings\\\\n  year: 2025\\\\n  category: method-component\\\\n  relevance: layer budgets 对 generation 重要、head budgets 对 extraction 重要——支撑 task-conditional budget\\\\n  key_finding: 基于 Layer Attention Output Loss 的 unified eviction + dynamic budget；budget 需求 task-dependent\\\\n\\\\n- paper_id: lkv-2026\\\\n  title: \\\\\\\"LKV: End-to-End Learning of Head-wise Budgets and Token Selection for LLM KV Cache Eviction\\\\\\\"\\\\n  venue: arXiv 2605.06676\\\\n  year: 2026\\\\n  category: method-component\\\\n  relevance: 首个端到端可微 budget+selection 联合学习框架；可作 phase-gated controller backbone\\\\n  key_finding: LKV-H 学 head budget + LKV-T 学 token selection，全面超越启发式方法\\\\n\\\\n- paper_id: defensivekv-iclr2026\\\\n  title: \\\\\\\"DefensiveKV: Taming the Fragility of KV Cache Eviction in LLM Inference\\\\\\\"\\\\n  venue: ICLR 2026\\\\n  year: 2026\\\\n  category: direct-competitor\\\\n  relevance: 独立发现 importance-based eviction 的脆弱性——stability assumption 不成立，importance 高度非稳态\\\\n  key_finding: mean aggregation 在极端情况下 vulnerable；defensive aggregation 控制 worst-case risk，2.3-4.3x 质量损失降低\\\\n\\\\n- paper_id: retentivekv-2026\\\\n  title: \\\\\\\"RetentiveKV: State-Space Memory for Uncertainty-Aware Multimodal KV Cache Eviction\\\\\\\"\\\\n  venue: arXiv 2605.04075\\\\n  year: 2026\\\\n  category: background\\\\n  relevance: \\\\\\\"Deferred Importance\\\\\\\" 现象——token 初始 salience 低但后期变 pivotal，直接支撑 crossover 机制\\\\n  key_finding: 视觉 tokens 存在 deferred importance——早期不重要晚期关键；单一时刻 importance 评估不可靠\\\\n\\\\n- paper_id: pitfalls-kvcache-2025\\\\n  title: \\\\\\\"The Pitfalls of KV Cache Compression\\\\\\\"\\\\n  venue: arXiv 2510.00231\\\\n  year: 2025\\\\n  category: background\\\\n  relevance: multi-instruction 场景下部分指令被压缩严重忽略——condition-dependent failure\\\\n  key_finding: 特定 instructions 在压缩下退化极快甚至完全被忽略；compression method + order 产生 bias 交互\\\\n\\\\n- paper_id: greedy-bias-kvcache-2026\\\\n  title: \\\\\\\"More Than a Quick Glance: Overcoming the Greedy Bias in KV-Cache Compression\\\\\\\"\\\\n  venue: arXiv 2602.02199\\\\n  year: 2026\\\\n  category: background\\\\n  relevance: 单一 attention-score metric 是 greedy 的——miss structurally relevant tokens\\\\n  key_finding: 单 metric 有 greedy bias；multi-metric scoring 克服 condition-dependent metric failure\\\\n\\\\n- paper_id: thinking-tokens-mi-neurips2025\\\\n  title: \\\\\\\"Demystifying Reasoning Dynamics with Mutual Information: Thinking Tokens are Information Peaks\\\\\\\"\\\\n  venue: NeurIPS 2025\\\\n  year: 2025\\\\n  category: background\\\\n  relevance: reasoning 中 MI 在 thinking tokens 处突然 peak——compression 需避开 info-critical phases\\\\n  key_finding: thinking tokens (Hmm/Wait/Therefore) 处 MI 突增；这些 tokens 对推理性能不成比例重要\\\\n\\\\n- paper_id: lserve-mlsys2025\\\\n  title: \\\\\\\"LServe: Efficient Long-sequence LLM Serving with Unified Sparse Attention\\\\\\\"\\\\n  venue: MLSys 2025\\\\n  year: 2025\\\\n  category: background\\\\n  relevance: sparse attention + KV quantization 工业级联合部署但无 interaction 分析\\\\n  key_finding: 统一 static/dynamic sparsity + KV quant 到单 GPU kernel；prefilling 2.9x 加速\\\\n\\\\n- paper_id: squeezeattention-iclr2025\\\\n  title: \\\\\\\"SqueezeAttention: 2D Management of KV-Cache via Layer-wise Optimal Budget\\\\\\\"\\\\n  venue: ICLR 2025\\\\n  year: 2025\\\\n  category: method-component\\\\n  relevance: layer × sequence 二维 budget 优化；我们增加第三维——temporal phase\\\\n  key_finding: layer-wise cosine similarity 区分 layer 重要性，30-70% memory reduction\\\\n\\\\n- paper_id: nsa-acl2025\\\\n  title: \\\\\\\"NSA: Native Sparse Attention\\\\\\\"\\\\n  authors: DeepSeek\\\\n  venue: ACL 2025 Best Paper\\\\n  year: 2025\\\\n  category: background\\\\n  relevance: hardware-aligned trainable sparse attention；hierarchical 策略（coarse compression + fine selection）呼应 multi-phase\\\\n  key_finding: 端到端可训练 sparse attention，64k 解码 11.6x 加速；coarse+fine 分层策略\\\\n\\\\n- paper_id: evicpress-2025\\\\n  title: \\\\\\\"EVICPRESS: Joint KV-Cache Compression and Eviction for Efficient LLM Serving\\\\\\\"\\\\n  venue: arXiv 2512.14946\\\\n  year: 2025\\\\n  category: method-component\\\\n  relevance: 联合 eviction + quantization 优化 KV cache——compound 方向但仅 KV 内部\\\\n  key_finding: joint eviction + quantization 优于独立应用；但无 head pruning compound\\\\n\\\\n- paper_id: phase-transition-pruning-thermo-2026\\\\n  title: \\\\\\\"Phase Transitions in Neural Networks Pruning (Thermodynamic Analysis)\\\\\\\"\\\\n  venue: arXiv 2602.15224\\\\n  year: 2026\\\\n  category: background\\\\n  relevance: 自由能分析预测 sharp collapse；transition 前稳定 3-5%，跨越后 30%+ 骤降\\\\n  key_finding: free-energy phase transition 预测 pruning 崩溃点；importance 方法可能在某 phase 跨越 PTP\\\\n\\\\n- paper_id: token-budget-aware-acl2025\\\\n  title: \\\\\\\"Token-Budget-Aware LLM Reasoning\\\\\\\"\\\\n  venue: ACL 2025 Findings\\\\n  year: 2025\\\\n  category: background\\\\n  relevance: reasoning budget 应按 query 难度自适应分配——支撑 phase-adaptive compression\\\\n  key_finding: self-consistency 作为 thinking necessity proxy 动态调整 reasoning token budget\\\\n\\\\n# ============================================================\\\\n# 新增 — C5b Negative Result 文献联动 (2026-05-14)\\\\n# ============================================================\\\\n\\\\n- paper_id: physics-kvcache-2026\\\\n  title: \\\\\\\"Understanding the Physics of Key-Value Cache Compression for LLMs through Attention Dynamics\\\\\\\"\\\\n  venue: arXiv 2603.01426\\\\n  year: 2026\\\\n  category: background\\\\n  relevance: 直接解释 C5b negative——representational rigidity 使 budget redistribution 无法修复 routing collapse；90% 附近存在 sharp hallucination cliff (phase transition)\\\\n  key_finding: head-level consensus 过度导致 representational rigidity，token 存活但 routing flexibility 崩溃；compression 存在 sharp safety cliff 对应 semantic reachability phase transition\\\\n\\\\n- paper_id: rkv-neurips2025\\\\n  title: \\\\\\\"R-KV: Redundancy-aware KV Cache Compression for Reasoning Models\\\\\\\"\\\\n  authors: Cai et al.\\\\n  venue: NeurIPS 2025\\\\n  year: 2025\\\\n  category: method-component\\\\n  relevance: reasoning model 专用单轴 KV compression，10% cache 保留 ~100% 性能；但不涉及 compound interaction，与 C5b failure 机制不直接相关\\\\n  key_finding: importance + non-redundancy 双准则 token ranking，10% KV cache 保留全精度性能；单轴方法无 compound 讨论\\\\n\\\", \\\"total_chars\\\": 13069, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/literature_map.yaml\", \"content\": \"## Literature Map — Phase-Gated Compound Sparsity\\n## 增量扫描: 2026-05-14\\n\\n# ============================================================\\n# 已知文献（baseline）\\n# ============================================================\\n\\n- paper_id: spark-aaai2026\\n  title: \\\"SparK: Query-Aware Unstructured Sparsity with Recoverable KV Cache Channel Pruning\\\"\\n  venue: AAAI 2026\\n  year: 2026\\n  category: direct-competitor\\n  relevance: 首篇报告 compound sparsity 总是 super-additive（ThinK+SnapKV 退化 65%），核心对标\\n  key_finding: compound KV cache sparsity (channel + token) 产生 super-additive degradation\\n\\n- paper_id: thinkv-iclr2026\\n  title: \\\"ThinKV\\\"\\n  venue: ICLR 2026 Oral\\n  year: 2026\\n  category: method-component\\n  relevance: phase 划分思想来源，但只做单一压缩策略\\n  key_finding: KV cache 可按 phase 划分应用不同策略\\n\\n- paper_id: rac-neurips2025\\n  title: \\\"RAC\\\"\\n  venue: NeurIPS 2025\\n  year: 2025\\n  category: background\\n  relevance: reasoning model 对 sparsity 更敏感，支撑评估任务选择\\n  key_finding: reasoning model 对 sparsity 敏感度高于一般 LLM\\n\\n- paper_id: raas-acl2025\\n  title: \\\"RaaS\\\"\\n  venue: ACL 2025\\n  year: 2025\\n  category: method-component\\n  relevance: milestone tokens 先重要后衰减，支撑 phase-dependent importance\\n  key_finding: token importance 随 decoding phase 非单调变化\\n\\n- paper_id: mixeddimkv-2026\\n  title: \\\"MixedDimKV\\\"\\n  year: 2026\\n  category: method-component\\n  relevance: multi-dimension compression budget allocation，与 joint controller 思路平行\\n  key_finding: 多维度压缩 budget allocation 优于均匀分配\\n\\n# ============================================================\\n# 新增 — Compound / Joint Compression Interaction\\n# ============================================================\\n\\n- paper_id: slim-icml2025\\n  title: \\\"SLiM: One-shot Quantization and Sparsity with Low-rank Approximation for LLM Weight Compression\\\"\\n  authors: Mozaffari et al.\\n  venue: ICML 2025\\n  year: 2025\\n  category: method-component\\n  relevance: 首个正式处理 compound compression error 的框架——用 low-rank adapter 补偿 Q+S 聚合误差，证明误差非加性\\n  key_finding: quantization + sparsity 聚合误差非加性；invertible saliency function 精确计算 low-rank 补偿\\n\\n- paper_id: unicomp-2026\\n  title: \\\"UniComp: A Unified Evaluation of Large Language Model Compression via Pruning, Quantization and Distillation\\\"\\n  authors: Wang et al.\\n  venue: arXiv 2602.09130\\n  year: 2026\\n  category: evaluation\\n  relevance: 40+ benchmarks 系统评估 compound compression，发现 compression 有 consistent knowledge bias\\n  key_finding: compression 对 knowledge-intensive tasks 保留好但 reasoning/multilingual 显著退化；quantization 整体 trade-off 最佳\\n\\n- paper_id: compression-ordering-2025\\n  title: \\\"A Systematic Study of Compression Ordering for Large Language Models\\\"\\n  venue: arXiv 2511.19495\\n  year: 2025\\n  category: background\\n  relevance: 证明 compound compression ordering 显著影响结果，early quantization 造成不可逆信息损失\\n  key_finding: P→KD→Q 最优；quantization first 产生不可逆退化；interaction 依赖 ordering\\n\\n- paper_id: phase-transition-compression-2026\\n  title: \\\"Phase Transitions in Large Language Model Compression\\\"\\n  authors: Ma et al.\\n  venue: npj Artificial Intelligence (Nature), 2026\\n  year: 2026\\n  category: background\\n  relevance: 直接支撑 phase-gating 理论动机——不同压缩维度有独立 phase transition point，联合安全区可叠加\\n  key_finding: structured pruning 30-45% 崩溃，unstructured 55-65%；多维度 PTP 正交，联合安全区可实现 10% 压缩\\n\\n- paper_id: graspune-acl2026\\n  title: \\\"GRASPrune: Global Gating for Budgeted Structured Pruning of Large Language Models\\\"\\n  authors: Wang et al.\\n  venue: ACL 2026 Main\\n  year: 2026\\n  category: direct-competitor\\n  relevance: 最直接 competitor——联合 pruning FFN channels + KV head groups with learned gate scores under global budget\\n  key_finding: learned gate + projected STE 全局 budget 下联合 prune FFN+heads，高压缩比下显著优于逐层独立 pruning\\n\\n- paper_id: mustafar-neurips2025\\n  title: \\\"MUSTAFAR: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference\\\"\\n  authors: Joo et al.\\n  venue: NeurIPS 2025\\n  year: 2025\\n  category: method-component\\n  relevance: per-token magnitude pruning 70% sparsity 无损，与 token eviction 可组合——potential compound baseline\\n  key_finding: unstructured KV sparsity (per-token magnitude) 70% 无损，bitmap 格式 2.23x throughput\\n\\n# ============================================================\\n# 新增 — Non-monotonic / Sign Reversal / Phase Effects\\n# ============================================================\\n\\n- paper_id: decision-repr-transition-2026\\n  title: \\\"Understanding Performance Collapse in Layer-Pruned LLMs via Decision Representation Transitions\\\"\\n  venue: arXiv 2605.07271\\n  year: 2026\\n  category: background\\n  relevance: layer pruning 存在 Silent/Decisive Phase 二分——pruning 敏感度 phase-dependent，直接支撑 phase-gated 思想\\n  key_finding: Decision Margin 在 Transition Point 发生符号反转（负→正）；pruning Silent Phase 崩溃，Decisive Phase 可安全 prune\\n\\n- paper_id: doing-more-with-less-2026\\n  title: \\\"Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling\\\"\\n  venue: arXiv 2604.25098\\n  year: 2026\\n  category: background\\n  relevance: 符号反转直接证据——unstructured pruning + TTS 可超越未剪枝模型\\n  key_finding: unstructured pruning + test-time scaling 可超越 unpruned baseline（Qwen3-8B）；structured pruning 严重退化\\n\\n- paper_id: sparse-frontier-2025\\n  title: \\\"The Sparse Frontier: Sparse Attention Trade-offs in Transformer LLMs\\\"\\n  venue: arXiv 2504.17768\\n  year: 2025\\n  category: evaluation\\n  relevance: 最大规模 sparse attention 评估，无通用最优策略，trade-off 依赖 task 和 phase\\n  key_finding: decoding vs prefilling 可承受 sparsity 不同；大模型+高稀疏可优于小模型+密集\\n\\n# ============================================================\\n# 新增 — Adaptive / Learned Controllers\\n# ============================================================\\n\\n- paper_id: obcache-2025\\n  title: \\\"OBCache: Optimal Brain KV Cache Pruning for Efficient Long-Context LLM Inference\\\"\\n  venue: arXiv 2510.07651\\n  year: 2025\\n  category: method-component\\n  relevance: OBD 理论推导 joint K-V saliency score，可作为 importance-based masking 的理论参照\\n  key_finding: 二阶 Taylor 近似推导 joint K-V pruning score；key-pruning 比 value-pruning 影响更大\\n\\n- paper_id: pagedeviction-eacl2026\\n  title: \\\"PagedEviction: Structured Block-wise KV Cache Pruning\\\"\\n  venue: EACL 2026 Findings\\n  year: 2026\\n  category: method-component\\n  relevance: prefill/decode 两阶段不同 eviction 策略，呼应 phase-gated 思想\\n  key_finding: block-wise eviction prefill/decode 分阶段执行，优于 token-level baselines\\n\\n- paper_id: adakv-neurips2025\\n  title: \\\"Ada-KV: Adaptive Budget Allocation for KV Cache Eviction\\\"\\n  venue: NeurIPS 2025\\n  year: 2025\\n  category: method-component\\n  relevance: per-head adaptive budget 分配，与 per-phase budget allocation 正交互补\\n  key_finding: 自适应 per-head KV cache budget 优于均匀分配\\n\\n- paper_id: sol-2026\\n  title: \\\"SOL: Self-Optimizing Language Models — Compute Where it Counts\\\"\\n  venue: arXiv 2605.10875\\n  year: 2026\\n  category: method-component\\n  relevance: learned policy 按 token difficulty 分配 compute，与 learned joint controller 方法论平行\\n  key_finding: 学习 per-token compute allocation policy，easy tokens 少算 hard tokens 多算\\n\\n# ============================================================\\n# 新增 — Phase-Adaptive Dynamic Compression (2026-05-14 scan)\\n# ============================================================\\n\\n- paper_id: twilight-neurips2025\\n  title: \\\"Twilight: Adaptive Attention Sparsity with Hierarchical Top-p Pruning\\\"\\n  authors: Lin, Tang, Yang, Wang, Tang, Tian, Stoica, Han, Gao\\n  venue: NeurIPS 2025 Spotlight\\n  year: 2025\\n  category: method-component\\n  relevance: 证明 fixed budget 次优，per-step adaptive budget 更优；但单轴无 compound interaction\\n  key_finding: top-p 采样思想做 per-step adaptive attention budget，最多 prune 98% tokens\\n\\n- paper_id: lava-emnlp2025\\n  title: \\\"LAVa: Layer-wise KV Cache Eviction with Dynamic Budget Allocation\\\"\\n  authors: Shen, Yuan, Zhang, Wang, Jiang, Nguyen\\n  venue: EMNLP 2025 Findings\\n  year: 2025\\n  category: method-component\\n  relevance: layer budgets 对 generation 重要、head budgets 对 extraction 重要——支撑 task-conditional budget\\n  key_finding: 基于 Layer Attention Output Loss 的 unified eviction + dynamic budget；budget 需求 task-dependent\\n\\n- paper_id: lkv-2026\\n  title: \\\"LKV: End-to-End Learning of Head-wise Budgets and Token Selection for LLM KV Cache Eviction\\\"\\n  venue: arXiv 2605.06676\\n  year: 2026\\n  category: method-component\\n  relevance: 首个端到端可微 budget+selection 联合学习框架；可作 phase-gated controller backbone\\n  key_finding: LKV-H 学 head budget + LKV-T 学 token selection，全面超越启发式方法\\n\\n- paper_id: defensivekv-iclr2026\\n  title: \\\"DefensiveKV: Taming the Fragility of KV Cache Eviction in LLM Inference\\\"\\n  venue: ICLR 2026\\n  year: 2026\\n  category: direct-competitor\\n  relevance: 独立发现 importance-based eviction 的脆弱性——stability assumption 不成立，importance 高度非稳态\\n  key_finding: mean aggregation 在极端情况下 vulnerable；defensive aggregation 控制 worst-case risk，2.3-4.3x 质量损失降低\\n\\n- paper_id: retentivekv-2026\\n  title: \\\"RetentiveKV: State-Space Memory for Uncertainty-Aware Multimodal KV Cache Eviction\\\"\\n  venue: arXiv 2605.04075\\n  year: 2026\\n  category: background\\n  relevance: \\\"Deferred Importance\\\" 现象——token 初始 salience 低但后期变 pivotal，直接支撑 crossover 机制\\n  key_finding: 视觉 tokens 存在 deferred importance——早期不重要晚期关键；单一时刻 importance 评估不可靠\\n\\n- paper_id: pitfalls-kvcache-2025\\n  title: \\\"The Pitfalls of KV Cache Compression\\\"\\n  venue: arXiv 2510.00231\\n  year: 2025\\n  category: background\\n  relevance: multi-instruction 场景下部分指令被压缩严重忽略——condition-dependent failure\\n  key_finding: 特定 instructions 在压缩下退化极快甚至完全被忽略；compression method + order 产生 bias 交互\\n\\n- paper_id: greedy-bias-kvcache-2026\\n  title: \\\"More Than a Quick Glance: Overcoming the Greedy Bias in KV-Cache Compression\\\"\\n  venue: arXiv 2602.02199\\n  year: 2026\\n  category: background\\n  relevance: 单一 attention-score metric 是 greedy 的——miss structurally relevant tokens\\n  key_finding: 单 metric 有 greedy bias；multi-metric scoring 克服 condition-dependent metric failure\\n\\n- paper_id: thinking-tokens-mi-neurips2025\\n  title: \\\"Demystifying Reasoning Dynamics with Mutual Information: Thinking Tokens are Information Peaks\\\"\\n  venue: NeurIPS 2025\\n  year: 2025\\n  category: background\\n  relevance: reasoning 中 MI 在 thinking tokens 处突然 peak——compression 需避开 info-critical phases\\n  key_finding: thinking tokens (Hmm/Wait/Therefore) 处 MI 突增；这些 tokens 对推理性能不成比例重要\\n\\n- paper_id: lserve-mlsys2025\\n  title: \\\"LServe: Efficient Long-sequence LLM Serving with Unified Sparse Attention\\\"\\n  venue: MLSys 2025\\n  year: 2025\\n  category: background\\n  relevance: sparse attention + KV quantization 工业级联合部署但无 interaction 分析\\n  key_finding: 统一 static/dynamic sparsity + KV quant 到单 GPU kernel；prefilling 2.9x 加速\\n\\n- paper_id: squeezeattention-iclr2025\\n  title: \\\"SqueezeAttention: 2D Management of KV-Cache via Layer-wise Optimal Budget\\\"\\n  venue: ICLR 2025\\n  year: 2025\\n  category: method-component\\n  relevance: layer × sequence 二维 budget 优化；我们增加第三维——temporal phase\\n  key_finding: layer-wise cosine similarity 区分 layer 重要性，30-70% memory reduction\\n\\n- paper_id: nsa-acl2025\\n  title: \\\"NSA: Native Sparse Attention\\\"\\n  authors: DeepSeek\\n  venue: ACL 2025 Best Paper\\n  year: 2025\\n  category: background\\n  relevance: hardware-aligned trainable sparse attention；hierarchical 策略（coarse compression + fine selection）呼应 multi-phase\\n  key_finding: 端到端可训练 sparse attention，64k 解码 11.6x 加速；coarse+fine 分层策略\\n\\n- paper_id: evicpress-2025\\n  title: \\\"EVICPRESS: Joint KV-Cache Compression and Eviction for Efficient LLM Serving\\\"\\n  venue: arXiv 2512.14946\\n  year: 2025\\n  category: method-component\\n  relevance: 联合 eviction + quantization 优化 KV cache——compound 方向但仅 KV 内部\\n  key_finding: joint eviction + quantization 优于独立应用；但无 head pruning compound\\n\\n- paper_id: phase-transition-pruning-thermo-2026\\n  title: \\\"Phase Transitions in Neural Networks Pruning (Thermodynamic Analysis)\\\"\\n  venue: arXiv 2602.15224\\n  year: 2026\\n  category: background\\n  relevance: 自由能分析预测 sharp collapse；transition 前稳定 3-5%，跨越后 30%+ 骤降\\n  key_finding: free-energy phase transition 预测 pruning 崩溃点；importance 方法可能在某 phase 跨越 PTP\\n\\n- paper_id: token-budget-aware-acl2025\\n  title: \\\"Token-Budget-Aware LLM Reasoning\\\"\\n  venue: ACL 2025 Findings\\n  year: 2025\\n  category: background\\n  relevance: reasoning budget 应按 query 难度自适应分配——支撑 phase-adaptive compression\\n  key_finding: self-consistency 作为 thinking necessity proxy 动态调整 reasoning token budget\\n\\n# ============================================================\\n# 新增 — C5b Negative Result 文献联动 (2026-05-14)\\n# ============================================================\\n\\n- paper_id: physics-kvcache-2026\\n  title: \\\"Understanding the Physics of Key-Value Cache Compression for LLMs through Attention Dynamics\\\"\\n  venue: arXiv 2603.01426\\n  year: 2026\\n  category: background\\n  relevance: 直接解释 C5b negative——representational rigidity 使 budget redistribution 无法修复 routing collapse；90% 附近存在 sharp hallucination cliff (phase transition)\\n  key_finding: head-level consensus 过度导致 representational rigidity，token 存活但 routing flexibility 崩溃；compression 存在 sharp safety cliff 对应 semantic reachability phase transition\\n\\n- paper_id: rkv-neurips2025\\n  title: \\\"R-KV: Redundancy-aware KV Cache Compression for Reasoning Models\\\"\\n  authors: Cai et al.\\n  venue: NeurIPS 2025\\n  year: 2025\\n  category: method-component\\n  relevance: reasoning model 专用单轴 KV compression，10% cache 保留 ~100% 性能；但不涉及 compound interaction，与 C5b failure 机制不直接相关\\n  key_finding: importance + non-redundancy 双准则 token ranking，10% KV cache 保留全精度性能；单轴方法无 compound 讨论\\n\", \"total_chars\": 13069, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
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
Good, I now have all three project files. Let me now examine the paper directory to find all .tex and .md files, and search for n=50 related references.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "440e9082-8110-4734-90d0-65267ccfca3a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GWDpezw7wrto1Zfdd3Bk2k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16779,
      "cache_read_input_tokens": 24146,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16779
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

现在检索论文目录内容并搜索所有 n=50 相关引用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "1596f009-d0b0-44ce-9cc4-4608c2b764ea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GWDpezw7wrto1Zfdd3Bk2k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16779,
      "cache_read_input_tokens": 24146,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16779
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

<details open><summary>🔧 Tool call — Glob · `toolu_017kEdkmsxKCUknfRAFoeMCJ`</summary>

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
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "aa020cde-eb0e-4249-a21f-4f272d84a3ad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GWDpezw7wrto1Zfdd3Bk2k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16779,
      "cache_read_input_tokens": 24146,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16779
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

_source line 17 · 2026-05-14T20:43:04.554Z_

<details><summary>↩ Tool result · `toolu_017kEdkmsxKCUknfRAFoeMCJ`</summary>

```text
artifacts/_project/paper/methodology.tex
artifacts/_project/paper/appendix_results.tex
artifacts/_project/paper/appendix.tex
artifacts/_project/paper/background.tex
artifacts/_project/paper/analysis.tex
artifacts/_project/paper/main.tex
artifacts/_project/paper/appendix_moved.tex
artifacts/_project/paper/abstract.tex
artifacts/_project/paper/discussion.tex
artifacts/_project/paper/results.tex
artifacts/_project/paper/conclusion.tex
artifacts/_project/paper/appendix_disc_analysis.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/limitations.tex
artifacts/_project/paper/related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "c8885a35-0aa6-4bf4-8dc8-1fd64c60053b",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/paper/methodology.tex",
      "artifacts/_project/paper/appendix_results.tex",
      "artifacts/_project/paper/appendix.tex",
      "artifacts/_project/paper/background.tex",
      "artifacts/_project/paper/analysis.tex",
      "artifacts/_project/paper/main.tex",
      "artifacts/_project/paper/appendix_moved.tex",
      "artifacts/_project/paper/abstract.tex",
      "artifacts/_project/paper/discussion.tex",
      "artifacts/_project/paper/results.tex",
      "artifacts/_project/paper/conclusion.tex",
      "artifacts/_project/paper/appendix_disc_analysis.tex",
      "artifacts/_project/paper/introduction.tex",
      "artifacts/_project/paper/limitations.tex",
      "artifacts/_project/paper/related_work.tex"
    ],
    "durationMs": 90,
    "numFiles": 15,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Glob · `toolu_01DmQP956vV1qKLVtLBQMbsu`</summary>

```json
{
  "pattern": "**/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "76591a3a-9068-4fb9-80fe-a48720a796a3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GWDpezw7wrto1Zfdd3Bk2k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16779,
      "cache_read_input_tokens": 24146,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16779
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

_source line 19 · 2026-05-14T20:43:05.699Z_

<details><summary>↩ Tool result · `toolu_01DmQP956vV1qKLVtLBQMbsu`</summary>

```text
artifacts/m2_m4_code_readiness.md
artifacts/mvp_ii_analysis.md
artifacts/mvp_interaction_index_profiling/report/mvp_ii_analysis.md
artifacts/m1_phase_segmentation_analysis.md
artifacts/mvp_ii_profiling_v2/report/mvp_ii_v2_analysis.md
artifacts/mvp_ii_profiling_v2/report/mvp_ii_v2_analysis_c4933e.md
artifacts/mvp_ii_v3_analysis.md
artifacts/mvp_ii_profiling_v3/report/mvp_ii_v3_analysis.md
artifacts/v5_status_check.md
artifacts/literature_scan_phase_adaptive.md
artifacts/magnitude_crossover_novelty_check.md
artifacts/mechanistic_explanation.md
artifacts/qwen_status_check.md
artifacts/qwen_kill_investigation.md
artifacts/_project/report/writing_readiness.md
artifacts/_project/report/multiplicative_null_comparison.md
artifacts/dream_reports/dream_20260514T054026/best/paper_framing.md
artifacts/dream_reports/dream_20260514T054026/median/paper_framing.md
artifacts/dream_reports/dream_20260514T054026/worst/paper_framing.md
artifacts/dream_reports/dream_20260514T054026/best/review_report.md
artifacts/dream_reports/dream_20260514T054026/median/review_report.md
artifacts/dream_reports/dream_20260514T054026/worst/review_report.md
artifacts/_project/report/mid_sparsity_gap_analysis.md
artifacts/mid_sparsity_gap_analysis.md
artifacts/bf16_qw_imp_failures_diagnosis.md
artifacts/_project/report/gradient_ratio_provenance.md
artifacts/consistency_report.md
artifacts/_project/paper/citation_audit_report.md
artifacts/consistency_audit_report.md
artifacts/consistency_audit_final.md
artifacts/reference_audit.md
artifacts/_project/report/number_consistency_audit_v2.md
artifacts/number_consistency_audit_v2.md
artifacts/_project/paper/numerical_audit_report.md
artifacts/_project/report/numerical_audit_report.md
artifacts/review_reports/round_3.md
artifacts/_project/report/number_audit_final.md
artifacts/c2_n500_deepseek/data/PRE_REGISTRATION_C2.md
artifacts/_project/report/final_review_report.md
artifacts/_project/report/final_review_report_610657.md
artifacts/c2_qw_n500_investigation.md
artifacts/_project/report/visual_review_report.md
artifacts/_project/report/c5b_pilot_design.md
artifacts/c5b_pilot_design.md
artifacts/dream_reports/dream_20260514T143543/best/paper_framing.md
artifacts/dream_reports/dream_20260514T143543/median/paper_framing.md
artifacts/dream_reports/dream_20260514T143543/worst/paper_framing.md
artifacts/dream_reports/dream_20260514T143543/best/review_report.md
artifacts/dream_reports/dream_20260514T143543/median/review_report.md
artifacts/dream_reports/dream_20260514T143543/worst/review_report.md
artifacts/_project/report/gpu_check_loop7.md
artifacts/gpu_check_loop7.md
artifacts/report_process_check.md
artifacts/c5b_framing_proposal.md
artifacts/c5b_pilot/report/c5b_framing_proposal.md
artifacts/c2_progress_report.md
artifacts/c5b_pilot_diagnosis.md
artifacts/_project/report/c2_n500_paper_update_checklist.md
artifacts/c2_n500_paper_update_checklist.md
artifacts/_project/report/reference_audit_report.md
artifacts/reference_audit_report.md
artifacts/_project/report/literature_scan_20260515.md
artifacts/literature_scan_20260515.md
artifacts/_project/report/analysis_pipeline_verification.md
artifacts/analysis_pipeline_verification.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "58305663-38a8-4a97-9316-2d52fda9adaa",
  "tool_use_result": {
    "filenames": [
      "artifacts/m2_m4_code_readiness.md",
      "artifacts/mvp_ii_analysis.md",
      "artifacts/mvp_interaction_index_profiling/report/mvp_ii_analysis.md",
      "artifacts/m1_phase_segmentation_analysis.md",
      "artifacts/mvp_ii_profiling_v2/report/mvp_ii_v2_analysis.md",
      "artifacts/mvp_ii_profiling_v2/report/mvp_ii_v2_analysis_c4933e.md",
      "artifacts/mvp_ii_v3_analysis.md",
      "artifacts/mvp_ii_profiling_v3/report/mvp_ii_v3_analysis.md",
      "artifacts/v5_status_check.md",
      "artifacts/literature_scan_phase_adaptive.md",
      "artifacts/magnitude_crossover_novelty_check.md",
      "artifacts/mechanistic_explanation.md",
      "artifacts/qwen_status_check.md",
      "artifacts/qwen_kill_investigation.md",
      "artifacts/_project/report/writing_readiness.md",
      "artifacts/_project/report/multiplicative_null_comparison.md",
      "artifacts/dream_reports/dream_20260514T054026/best/paper_framing.md",
      "artifacts/dream_reports/dream_20260514T054026/median/paper_framing.md",
      "artifacts/dream_reports/dream_20260514T054026/worst/paper_framing.md",
      "artifacts/dream_reports/dream_20260514T054026/best/review_report.md",
      "artifacts/dream_reports/dream_20260514T054026/median/review_report.md",
      "artifacts/dream_reports/dream_20260514T054026/worst/review_report.md",
      "artifacts/_project/report/mid_sparsity_gap_analysis.md",
      "artifacts/mid_sparsity_gap_analysis.md",
      "artifacts/bf16_qw_imp_failures_diagnosis.md",
      "artifacts/_project/report/gradient_ratio_provenance.md",
      "artifacts/consistency_report.md",
      "artifacts/_project/paper/citation_audit_report.md",
      "artifacts/consistency_audit_report.md",
      "artifacts/consistency_audit_final.md",
      "artifacts/reference_audit.md",
      "artifacts/_project/report/number_consistency_audit_v2.md",
      "artifacts/number_consistency_audit_v2.md",
      "artifacts/_project/paper/numerical_audit_report.md",
      "artifacts/_project/report/numerical_audit_report.md",
      "artifacts/review_reports/round_3.md",
      "artifacts/_project/report/number_audit_final.md",
      "artifacts/c2_n500_deepseek/data/PRE_REGISTRATION_C2.md",
      "artifacts/_project/report/final_review_report.md",
      "artifacts/_project/report/final_review_report_610657.md",
      "artifacts/c2_qw_n500_investigation.md",
      "artifacts/_project/report/visual_review_report.md",
      "artifacts/_project/report/c5b_pilot_design.md",
      "artifacts/c5b_pilot_design.md",
      "artifacts/dream_reports/dream_20260514T143543/best/paper_framing.md",
      "artifacts/dream_reports/dream_20260514T143543/median/paper_framing.md",
      "artifacts/dream_reports/dream_20260514T143543/worst/paper_framing.md",
      "artifacts/dream_reports/dream_20260514T143543/best/review_report.md",
      "artifacts/dream_reports/dream_20260514T143543/median/review_report.md",
      "artifacts/dream_reports/dream_20260514T143543/worst/review_report.md",
      "artifacts/_project/report/gpu_check_loop7.md",
      "artifacts/gpu_check_loop7.md",
      "artifacts/report_process_check.md",
      "artifacts/c5b_framing_proposal.md",
      "artifacts/c5b_pilot/report/c5b_framing_proposal.md",
      "artifacts/c2_progress_report.md",
      "artifacts/c5b_pilot_diagnosis.md",
      "artifacts/_project/report/c2_n500_paper_update_checklist.md",
      "artifacts/c2_n500_paper_update_checklist.md",
      "artifacts/_project/report/reference_audit_report.md",
      "artifacts/reference_audit_report.md",
      "artifacts/_project/report/literature_scan_20260515.md",
      "artifacts/literature_scan_20260515.md",
      "artifacts/_project/report/analysis_pipeline_verification.md",
      "artifacts/analysis_pipeline_verification.md"
    ],
    "durationMs": 37,
    "numFiles": 65,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Glob · `toolu_017XoRZ2okceM3UVsiuLReo6`</summary>

```json
{
  "pattern": "**/paper/**",
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
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "f63bf3ba-0ece-4f40-b73b-9f169ff86a89",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GWDpezw7wrto1Zfdd3Bk2k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16779,
      "cache_read_input_tokens": 24146,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16779
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

_source line 21 · 2026-05-14T20:43:06.180Z_

<details><summary>↩ Tool result · `toolu_017XoRZ2okceM3UVsiuLReo6`</summary>

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
artifacts/_project/paper/methodology.tex
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
artifacts/_project/paper/appendix_results.tex
artifacts/_project/paper/appendix.tex
artifacts/_project/paper/main_bdfc72.pdf
artifacts/_project/paper/numerical_audit_report.md
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
artifacts/_project/paper/main.tex
artifacts/_project/paper/main.fls
artifacts/_project/paper/main.fdb_latexmk
artifacts/_project/paper/appendix_moved.tex
artifacts/_project/paper/_pdf_images/main_p3.png
artifacts/_project/paper/_pdf_images/main_p1.png
artifacts/_project/paper/_pdf_images/main_p2.png
artifacts/_project/paper/_pdf_images/main_p10.png
artifacts/_project/paper/_pdf_images/main_p11.png
artifacts/_project/paper/abstract.tex
artifacts/_project/paper/discussion.tex
artifacts/_project/paper/results.tex
artifacts/_project/paper/conclusion.tex
artifacts/_project/paper/appendix_disc_analysis.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/limitations.tex
artifacts/_project/paper/references.bib
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/main.blg
artifacts/_project/paper/main.bbl
artifacts/_project/paper/main.aux
artifacts/_project/paper/main.out
artifacts/_project/paper/main.log
artifacts/_project/paper/main.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "c67528f1-4275-4b61-bb60-540a4fb8f6b0",
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
      "artifacts/_project/paper/methodology.tex",
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
      "artifacts/_project/paper/appendix_results.tex",
      "artifacts/_project/paper/appendix.tex",
      "artifacts/_project/paper/main_bdfc72.pdf",
      "artifacts/_project/paper/numerical_audit_report.md",
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
      "artifacts/_project/paper/main.tex",
      "artifacts/_project/paper/main.fls",
      "artifacts/_project/paper/main.fdb_latexmk",
      "artifacts/_project/paper/appendix_moved.tex",
      "artifacts/_project/paper/_pdf_images/main_p3.png",
      "artifacts/_project/paper/_pdf_images/main_p1.png",
      "artifacts/_project/paper/_pdf_images/main_p2.png",
      "artifacts/_project/paper/_pdf_images/main_p10.png",
      "artifacts/_project/paper/_pdf_images/main_p11.png",
      "artifacts/_project/paper/abstract.tex",
      "artifacts/_project/paper/discussion.tex",
      "artifacts/_project/paper/results.tex",
      "artifacts/_project/paper/conclusion.tex",
      "artifacts/_project/paper/appendix_disc_analysis.tex",
      "artifacts/_project/paper/introduction.tex",
      "artifacts/_project/paper/limitations.tex",
      "artifacts/_project/paper/references.bib",
      "artifacts/_project/paper/related_work.tex",
      "artifacts/_project/paper/main.blg",
      "artifacts/_project/paper/main.bbl",
      "artifacts/_project/paper/main.aux",
      "artifacts/_project/paper/main.out",
      "artifacts/_project/paper/main.log",
      "artifacts/_project/paper/main.pdf"
    ],
    "durationMs": 40,
    "numFiles": 62,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 22_

<details><summary>Logged reasoning block</summary>

```text
Now I need to search all the tex files for references to n=50 and related terms. Let me also check the existing checklist that seems to exist already.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "31535673-6bbf-48d0-9a10-d17b59e92da0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014xZ7cBKwnKLFdsDoUmQzRY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2592,
      "cache_read_input_tokens": 40925,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2592
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

_source line 23_

发现已有一个 `c2_n500_paper_update_checklist.md`。让我先看看它，再搜索论文中所有 n=50 引用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "46c16891-7a7e-4f71-a571-6b307ccb7def",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014xZ7cBKwnKLFdsDoUmQzRY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2592,
      "cache_read_input_tokens": 40925,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2592
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

<details open><summary>🔧 Tool call — Read · `toolu_011HwjiLQqLeHqJFHf9714bX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/c2_n500_paper_update_checklist.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "dc75897c-7aee-4969-94a6-f666bdbd01a6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014xZ7cBKwnKLFdsDoUmQzRY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2592,
      "cache_read_input_tokens": 40925,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2592
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

_source line 25 · 2026-05-14T20:43:11.344Z_

<details><summary>↩ Tool result · `toolu_011HwjiLQqLeHqJFHf9714bX`</summary>

````text
1	# C2 n=500 论文更新清单
2	
3	> 当 C2 n=500 实验（DeepSeek 8 conditions + Qwen 8 conditions）全部完成后，用此清单逐项替换论文中所有 n=50 数据。
4	> 数据来源均在服务器 `/root/autodl-tmp/pacs/analysis_output/` 下。
5	> **原则**：DeepSeek 和 Qwen 数值绝对值差 ~5×，不可混用；所有数值精确替换，不可近似。
6	
7	---
8	
9	## 1. 样本量文本替换（全局搜索 "50"）
10	
11	| 文件 | 行号 | 当前文本 | 替换为 | 类型 |
12	|------|------|---------|--------|------|
13	| abstract.tex | 6 | `50 MATH-500 problems` | `500 MATH-500 problems` | 文本 |
14	| methodology.tex | 10 | `50 problems stratified from MATH-500` | `500 problems from MATH-500` | 文本 |
15	| results.tex | 13 | `$n{=}50$ MATH-500 problems` (Table 1 caption) | `$n{=}500$` | 文本 |
16	| results.tex | 34 | `medians across 50 problems` (Table 2 caption) | `medians across 500 problems` | 文本 |
17	| appendix_moved.tex | 26 | `$n{=}46$ valid problems for Qwen (vs.\ $n{=}49$ for DeepSeek)` | n=500 后的有效样本量（需从数据计算） | 文本 |
18	| appendix_moved.tex | 73 | `$n{=}49$, $10{,}000$ permutations` (Table permutation caption) | 新 n 值 | 文本 |
19	| appendix_disc_analysis.tex | 45 | `$n{=}49$ paired problems for DeepSeek (1 excluded) and $n{=}46$ for Qwen (4 excluded)` | 新排除数/有效 n | 文本 |
20	
21	---
22	
23	## 2. Tables
24	
25	### Table 1: Aggregate II (tab:aggregate-ii) — results.tex L10-23
26	
27	| 行/列 | 当前值 | 数据来源 | 更新类型 |
28	|--------|--------|----------|----------|
29	| Importance s=0.15 | 0.39 | experiment_summary_table.json → DS imp s015 median_diff | 数值替换 |
30	| Importance s=0.20 | 1.48 | experiment_summary_table.json → DS imp s020 median_diff | 数值替换 |
31	| Importance s=0.25 | 7.16 | experiment_summary_table.json → DS imp s025 median_diff | 数值替换 |
32	| Importance s=0.30 | 14.59 | experiment_summary_table.json → DS imp s030 median_diff | 数值替换 |
33	| Random s=0.15 | 0.01 | experiment_summary_table.json → DS rand s015 median_diff | 数值替换 |
34	| Random s=0.20 | −0.02 | experiment_summary_table.json → DS rand s020 median_diff | 数值替换 |
35	| Random s=0.25 | 0.54 | experiment_summary_table.json → DS rand s025 median_diff | 数值替换 |
36	| Random s=0.30 | 1.54 | experiment_summary_table.json → DS rand s030 median_diff | 数值替换 |
37	| 正文 L8 | `$0.39$...$14.59$...37×` | 同上，37× = 14.59/0.39 需重算 | 数值+比率 |
38	| 正文 L8 | `$-0.02$ to $1.54$` | random range 需从新数据取 | 数值替换 |
39	
40	### Table 2: Per-phase II breakdown (tab:main-results) — results.tex L31-53
41	
42	| 行 | II_high | II_mid | II_low | Δ | G | 数据来源 |
43	|----|---------|--------|--------|---|---|----------|
44	| 0.15 Imp | 0.006 | 0.081 | 0.398 | 0.39 | 69 | DS imp s015 per-phase medians |
45	| 0.15 Rand | 0.093 | 0.097 | 0.103 | 0.01 | 1.1 | DS rand s015 per-phase medians |
46	| 0.20 Imp | 0.015 | 0.203 | 1.496 | 1.48 | 103 | DS imp s020 per-phase medians |
47	| 0.20 Rand | 0.292 | 0.350 | 0.276 | −0.02 | 0.9 | DS rand s020 per-phase medians |
48	| 0.25 Imp | 0.032 | 1.118 | 7.196 | 7.16 | 222 | DS imp s025 per-phase medians |
49	| 0.25 Rand | 0.818 | 0.932 | 1.363 | 0.54 | 1.7 | DS rand s025 per-phase medians |
50	| 0.30 Imp | 0.053 | 2.283 | 14.639 | 14.59 | 274 | DS imp s030 per-phase medians |
51	| 0.30 Rand | 2.503 | 2.592 | 4.041 | 1.54 | 1.6 | DS rand s030 per-phase medians |
52	
53	数据来源：`experiment_summary_table.json` 中各 condition 的 `median_low`, `median_mid`, `median_high`。
54	
55	### Table 3: Cohen's d (tab:cohens-d) — results.tex L81-97
56	
57	| 行 | DS d_z | DS Δ̃ [CI] | QW d_z | QW Δ̃ [CI] | 数据来源 |
58	|----|--------|-----------|--------|-----------|----------|
59	| s=0.15 | 0.44 | 0.32 [0.20, 0.47] | 0.28 | 0.05 [−0.01, 0.11]^ns | cohens_d_bf16.json / cohens_d_bf16_qwen.json |
60	| s=0.20 | 0.52 | 1.15 [0.66, 1.26] | 0.55 | 0.21 [0.07, 0.40] | 同上 |
61	| s=0.25 | 0.68 | 3.97 [2.83, 5.29] | 0.89 | 1.11 [0.61, 1.47] | 同上 |
62	| s=0.30 | 0.80 | 9.94 [8.39, 16.65] | 1.02 | 2.62 [1.72, 3.65] | 同上 |
63	
64	**注意**：n=500 后 CI 会显著收窄（~√10 倍）。QW s015 的 `ns` 标注取决于 CI 是否仍含零。
65	
66	### Table: Cross-model comparison (tab:cross-model) — appendix_moved.tex L30-43
67	
68	| 行 | 当前值 | 数据来源 |
69	|----|--------|----------|
70	| DeepSeek s015/s020/s025/s030 | 0.39 / 1.48 / 7.16 / 14.59 | experiment_summary_table.json DS imp |
71	| Qwen s015/s020/s025/s030 | 0.04 / 0.23 / 1.27 / 2.94 | experiment_summary_table.json QW imp |
72	
73	### Table: Permutation test (tab:permutation) — appendix_moved.tex L70-85
74	
75	| s | Observed Δ̃ | 95% CI | p_Bonf | 数据来源 |
76	|---|-----------|--------|--------|----------|
77	| 0.15 | 0.37 | [0.19, 0.62] | 0.0032 | permutation_test_results.json |
78	| 0.20 | 0.97 | [0.69, 1.49] | <0.001 | 同上 |
79	| 0.25 | 3.34 | [1.66, 6.64] | <0.001 | 同上 |
80	| 0.30 | 9.85 | [6.70, 16.29] | <0.001 | 同上 |
81	
82	### Table: Discrimination metrics (tab:discrimination-metrics-full) — appendix_moved.tex L103-123
83	
84	| Model | s | ΔGini | ΔCV | 数据来源 |
85	|-------|---|-------|-----|----------|
86	| DS 0.15 | −0.030 | −0.56 | c4_entropy_deepseek |
87	| DS 0.20 | −0.040 | −0.77 | 同上 |
88	| DS 0.25 | −0.065 | −1.29 | 同上 |
89	| DS 0.30 | −0.081 | −1.66 | 同上 |
90	| QW 0.15 | −0.010 | −0.05 | c4_entropy_qwen |
91	| QW 0.20 | −0.012 | −0.21 | 同上 |
92	| QW 0.25 | −0.010 | −1.49 | 同上 |
93	| QW 0.30 | −0.020 | −1.14 | 同上 |
94	
95	**注意**：C4 entropy 分析需要用 n=500 数据重跑 `analysis/entropy_analysis.py`。
96	
97	### Table: Entropy deltas (tab:entropy-deltas) — appendix_moved.tex L143-163
98	
99	| Model | s | ΔH | 数据来源 |
100	|-------|---|----|----------|
101	| DS 0.15 | −0.040 | c4_entropy_deepseek |
102	| DS 0.20 | −0.047 | 同上 |
103	| DS 0.25 | −0.045 | 同上 |
104	| DS 0.30 | −0.044 | 同上 |
105	| QW 0.15 | −0.073 | c4_entropy_qwen |
106	| QW 0.20 | −0.076 | 同上 |
107	| QW 0.25 | +0.045 | 同上 |
108	| QW 0.30 | −0.007 | 同上 |
109	
110	---
111	
112	## 3. Figures
113	
114	| Figure | 文件 | 数据来源 | 需更新内容 |
115	|--------|------|----------|-----------|
116	| Fig 1 (fig:hero) — fig1_dose_response.pdf | results.tex L55-60 | experiment_summary_table.json G values | G 曲线数据点 + caption 中 `$69{\times}$ to $274{\times}$` |
117	| Fig 2 — fig2_cohens_d (如存在) | 位置待定 | cohens_d_bf16.json, cohens_d_bf16_qwen.json | Cohen's d 森林图 |
118	| Fig 3 (fig:crossover) — fig3_crossover.pdf | appendix_moved.tex L13-18 | experiment_summary_table.json DS s025 | 柱状图数据 + caption 中 `$5.3{\times}$` |
119	| Fig 4 (fig:permtest-forest) — fig4_bootstrap.pdf | appendix_moved.tex L87-92 | permutation_test_results.json | CI 横条 + 点估计值 |
120	| Fig 5 (fig:cross-model) — fig5_crossmodel.pdf | appendix_moved.tex L46-50 | experiment_summary_table.json DS+QW imp | 双曲线数据点 + caption 中 `one-fifth` 比例 |
121	
122	**图表生成脚本**（服务器端）：
123	- `/root/autodl-tmp/pacs/analysis/generate_paper_figures.py` — fig4, fig5
124	- `/root/autodl-tmp/pacs/analysis/generate_summary_table.py` — experiment_summary_table.json
125	- `/root/autodl-tmp/pacs/analysis/cross_model_analysis.py` — cross_model_analysis.json
126	- `/root/autodl-tmp/pacs/analysis/compute_cohens_d.py` — cohens_d_bf16.json
127	
128	**更新流程**：先用 n=500 profiling 数据重跑 `generate_summary_table.py`，再重跑各分析脚本，最后重新生成所有图表 PDF。
129	
130	---
131	
132	## 4. 正文中的内联统计声明
133	
134	### abstract.tex
135	
136	| 行 | 当前文本 | 数据来源 | 类型 |
137	|----|---------|----------|------|
138	| 7 | `median Interaction Index difference...increases monotonically from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$` | experiment_summary_table.json DS imp | 数值 |
139	| 7 | `paired Cohen's $d_z$ growing from $0.44$ (small) to $0.80$ (large)` | cohens_d_bf16.json | 数值 |
140	| 7 | `$p < 0.005$ at all four sparsity levels` | permutation_test_results.json | 阈值判断 |
141	| 8 | `7/8 conditions` | 重新统计 random PASS/FAIL | 计数 |
142	| 8 | `Qwen $s{=}0.30$, $p{=}0.012$` | QW rand s030 permutation test | 数值 |
143	| 8 | `$d_z{=}{-}0.04$` | QW rand s030 Cohen's d | 数值 |
144	| 9 | `$\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$` | DS imp/rand s025 high-phase medians | 数值 |
145	| 9 | `$\widetilde{\mathrm{II}} = 7.196$ vs.\ $1.363$` | DS imp/rand s025 low-phase medians | 数值 |
146	| 10 | `$d_z \geq 0.55$` | cohens_d_bf16_qwen.json s020 | 阈值 |
147	| 10 | `Spearman $\rho = 1.0$` | cross_model_analysis.json | 数值 |
148	| 10 | `gradient permutation $p = 0.043$` | cross_model_analysis.json | 数值 |
149	
150	### introduction.tex
151	
152	| 行 | 当前文本 | 数据来源 | 类型 |
153	|----|---------|----------|------|
154	| 14 | `$0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$` | experiment_summary_table.json DS imp | 数值 |
155	| 14 | `$d_z$: $0.44 \to 0.80$` | cohens_d_bf16.json | 数值 |
156	| 14 | `Bonferroni-corrected $p < 0.005$ at all levels` | permutation_test_results.json | 阈值判断 |
157	| 15 | `$d_z \geq 0.55$` | cohens_d_bf16_qwen.json s020 | 阈值 |
158	| 16 | `7/8 conditions non-significant` | 重新统计 random PASS/FAIL | 计数 |
159	
160	### methodology.tex
161	
162	| 行 | 当前文本 | 数据来源 | 类型 |
163	|----|---------|----------|------|
164	| 18 | `mean/median ratios up to 43:1` | 从 n=500 数据重新计算 | 数值 |
165	| 22 | `$p_{\text{Bonf}} < 0.005$ at every sparsity level` | permutation_test_results.json | 阈值判断 |
166	
167	### results.tex (正文段落)
168	
169	| 行 | 当前文本 | 数据来源 | 类型 |
170	|----|---------|----------|------|
171	| 8 | `$37{\times}$ amplification` | 新 Δ_s030 / Δ_s015 需重算 | 比率 |
172	| 29 | `$69{\times}$ at $s{=}0.15$ to $274{\times}$ at $s{=}0.30$` | Table 2 G 列 | 数值 |
173	| 29 | `$0.006$ to $0.053$` | Table 2 II_high 列 min/max | 数值 |
174	| 29 | `$G \approx 0.9$--$1.7{\times}$` | Table 2 random G 列 range | 数值 |
175	| 66 | `$0.032$ vs.\ $0.818$`...`$7.196$ vs.\ $1.363$---a $5.3{\times}$` | s025 per-phase medians | 数值+比率 |
176	| 71 | `$\Delta$ increases from $0.04$...$2.94$...${\sim}1/5$` | experiment_summary_table.json QW imp | 数值+比率 |
177	| 71 | `$d_z \geq 0.55$; Spearman $\rho = 1.0$; gradient permutation $p = 0.043$` | cross_model_analysis.json | 数值 |
178	| 71 | `$d_z{=}0.28$, CI includes zero` | cohens_d_bf16_qwen.json s015 | 数值+判断 |
179	| 77 | `$0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$` | permutation_test_results.json | 数值 |
180	| 79 | `$d_z{=}0.44$ (small) to $d_z{=}0.80$ (large)` | cohens_d_bf16.json | 数值 |
181	| 79 | `$d_z{=}0.28$...CI includes zero`...`$d_z \geq 0.55$` | cohens_d_bf16_qwen.json | 数值+判断 |
182	| 79 | `$d_z{=}0.89$/$1.02$ vs.\ $0.68$/$0.80$` | cohens_d 两模型对比 | 数值 |
183	
184	### analysis.tex
185	
186	| 行 | 当前文本 | 数据来源 | 类型 |
187	|----|---------|----------|------|
188	| 4 | `$0.030$--$0.081$ (DeepSeek) and $0.010$--$0.020$ (Qwen)` | c4_entropy 分析 ΔGini ranges | 数值 |
189	| 4 | `16 conditions` | 确认是否仍为 16 | 计数 |
190	| 6 | `$\Delta\mathcal{H} \in [-0.047, -0.040]$` | c4_entropy_deepseek entropy deltas | 数值 |
191	| 6 | `$\Delta\mathcal{H} = +0.045$` | c4_entropy_qwen s025 | 数值 |
192	| 6 | `22 of 30 problems` | n=500 后需重算（可能变为 ~220 of 300） | 计数 |
193	
194	### discussion.tex
195	
196	| 行 | 当前文本 | 数据来源 | 类型 |
197	|----|---------|----------|------|
198	| 5 | `$69$--$274{\times}$` | Table 2 G range | 数值 |
199	| 5 | `$\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$` | s025 high-phase | 数值 |
200	| 5 | `$7.196$ vs.\ $1.363$` | s025 low-phase | 数值 |
201	| 5 | `$G \approx 1$` | random G（确认仍成立） | 数值 |
202	
203	### conclusion.tex
204	
205	| 行 | 当前文本 | 数据来源 | 类型 |
206	|----|---------|----------|------|
207	| 4 | `$69{\times}$ to $274{\times}$` | Table 2 G range | 数值 |
208	| 4 | `$d_z$: $0.44 \to 0.80$` | cohens_d_bf16.json | 数值 |
209	| 4 | `7/8 conditions non-significant` | random PASS/FAIL 重统计 | 计数 |
210	| 4 | `$d_z \geq 0.55$` | cohens_d_bf16_qwen.json s020 | 阈值 |
211	
212	### appendix.tex
213	
214	| 行 | 当前文本 | 数据来源 | 类型 |
215	|----|---------|----------|------|
216	| 38 | `$G_{\times} = 58$--$241{\times}$` | 乘法 null 下 G range 需重算 | 数值 |
217	
218	### appendix_moved.tex (正文段落)
219	
220	| 行 | 当前文本 | 数据来源 | 类型 |
221	|----|---------|----------|------|
222	| 11 | `$0.032$ vs.\ $0.818$`...`$7.196$ vs.\ $1.363$---a $5.3{\times}$` | s025 per-phase medians | 数值+比率 |
223	| 11 | `$3.9{\times}$...$5.4{\times}$...$5.3{\times}$...$3.6{\times}$` | 各 sparsity level crossover reversal magnitudes | 数值 |
224	| 26 | `Four of the 50 problems are excluded` | QW excluded count n=500 | 计数 |
225	| 53 | `mean $\rho = -0.11$, $p = 0.926$` | cross_model_analysis.json | 数值 |
226	| 56 | `$p = 0.012$...d_z = -0.04` | QW rand s030 | 数值 |
227	| 64 | `mean/median ratios ranging from $1.2{\times}$...$1.6{\times}$` and `$1.1{\times}$ to $1.4{\times}$ for Qwen` | 从 n=500 per-problem diffs 计算 | 数值 |
228	| 66 | `$99.92$th percentile...p_Bonf = 0.0032` | permutation_test_results.json s015 | 数值 |
229	| 68 | `$0.37$...$9.85$...CI lower bound ($0.19 \to 0.69 \to 1.66 \to 6.70$)` | permutation_test_results.json | 数值 |
230	
231	### appendix_disc_analysis.tex (正文段落)
232	
233	| 行 | 当前文本 | 数据来源 | 类型 |
234	|----|---------|----------|------|
235	| 4 | `$-0.031$ to $-0.073$; Qwen: $-0.019$ to $-0.045$` | random eviction Gini 变化 | 数值 |
236	| 11 | `$\widetilde{\mathrm{II}}_{\text{high}} < 0.06$ at $s \leq 0.30$` | Table 2 high-phase range | 数值 |
237	| 11 | `$s = 0.35$, high-phase II rises to $0.105$` | bf16_ds_imp_s035 数据 | 数值 |
238	| 14 | `7/8...Qwen $s{=}0.30$, $p{=}0.012$...$d_z{=}{-}0.04$` | QW rand s030 统计 | 数值 |
239	| 45 | `$n{=}49$...$n{=}46$` | 有效样本量 | 计数 |
240	| 46 | `mean/median ratio ${\sim}1.6{:}1$...mean_diff=22.94, median_diff=14.59` | s030 skewness stats | 数值 |
241	| 47 | CIs: `$[0.19,\; 0.62]$...$[0.69,\; 1.49]$...$[1.66,\; 6.64]$...$[6.70,\; 16.29]$` | permutation_test_results.json | 数值 |
242	| 49 | `$p{=}0.012$...$d_z{=}{-}0.04$...d=-0.035` | QW rand s030 re-bootstrap | 数值 |
243	
244	### appendix_results.tex
245	
246	| 行 | 当前文本 | 数据来源 | 类型 |
247	|----|---------|----------|------|
248	| 7 | `mean $\rho = -0.11$, $p = 0.926$` | cross_model_analysis.json | 数值 |
249	| 10 | `$p = 0.012$...d_z = -0.04` | QW rand s030 | 数值 |
250	
251	---
252	
253	## 5. Qwen s015 预注册决策点 (D037/D038)
254	
255	### 当前状态
256	Qwen s015: d_z=0.28, CI=[−0.006, 0.60] → **不显著**，论文采用 "threshold narrative"。
257	
258	### 决策矩阵
259	
260	| n=500 结果 | CI 位置 | 操作 |
261	|-----------|---------|------|
262	| CI 完全 > 0 | 例如 [0.05, 0.35] | **升级**：删除 `^ns` 标注，改叙事为 "effect reliable at all four sparsity levels for both models" |
263	| CI 仍跨零 | 例如 [−0.02, 0.15] | **维持 threshold narrative**：保持当前表述不变，仅更新数值 |
264	
265	### CI 跨零时需更新的叙事位置（仅更新数值，保留 threshold 表述）
266	
267	| 文件 | 行 | 当前叙事 | 操作 |
268	|------|------|---------|------|
269	| abstract.tex | 10 | `replicates on Qwen2.5-7B-Instruct at $s \geq 0.20$` | 更新 d_z 数值，保留 `$s \geq 0.20$` |
270	| introduction.tex | 15 | `$d_z \geq 0.55$` | 更新阈值数值 |
271	| results.tex | 71 | `marginal at $s{=}0.15$ ($d_z{=}0.28$, CI includes zero) but reliable at $s \geq 0.20$ ($d_z \geq 0.55$)` | 更新所有数值 |
272	| results.tex | 90 | `0.28` & `0.05\; $[-0.01, 0.11]$\textsuperscript{ns}` | 更新数值，保留 `^ns` |
273	| results.tex | 95 | `\textsuperscript{ns}Marginal at $s{=}0.15$; reliable at $s \geq 0.20$.` | 保留 |
274	| conclusion.tex | 4 | `$d_z \geq 0.55$` | 更新数值 |
275	
276	### CI > 0 时需更新的叙事位置（升级方案）
277	
278	| 文件 | 行 | 当前叙事 | 备选叙事 |
279	|------|------|---------|----------|
280	| abstract.tex | 10 | `at $s \geq 0.20$` | `at all four sparsity levels` |
281	| introduction.tex | 15 | `$d_z \geq 0.55$` | `$d_z \geq [新s015值]$`（改用 s015 值） |
282	| results.tex | 71 | `marginal at $s{=}0.15$...reliable at $s \geq 0.20$` | `reliable at all four sparsity levels ($d_z \geq [新值]$)` |
283	| results.tex | 90 | `\textsuperscript{ns}` | 删除 `^ns` 标注 |
284	| results.tex | 95 | 脚注 `Marginal at...reliable at...` | 删除或改为 `All levels significant.` |
285	| conclusion.tex | 4 | `$d_z \geq 0.55$` | `$d_z \geq [新s015值]$` |
286	
287	---
288	
289	## 6. 附属统计量（可能变化但方向不变）
290	
291	以下数值的 n=500 版本大概率方向不变，但绝对值会变：
292	
293	| 统计量 | 当前值 | 出现位置 | 预期变化 |
294	|--------|--------|---------|----------|
295	| mean/median ratio | up to 43:1 | methodology.tex L18 | n=500 尾部更极端，可能变大或变小 |
296	| "7/8 conditions" random non-significant | 7/8 | abstract, intro, conclusion, appendix_disc | n=500 CI 更窄，QW rand s030 borderline PASS 可能翻转为 FAIL → 变成 8/8 |
297	| DS/QW magnitude ratio | ~1/5 | results.tex L71, fig5 caption | 可能略变 |
298	| Crossover reversal magnitudes | 3.9×–5.4× | appendix_moved.tex L11 | 数据驱动，需重算 |
299	| Spearman ρ for monotonicity | 1.0 | abstract L10, results L71 | 4 点排序，大概率仍=1.0 |
300	| Gradient permutation p | 0.043 | abstract L10, results L71 | 4! = 24 种排列，最小 p=1/24≈0.042 |
301	| Per-problem concordance | ρ=−0.11, p=0.926 | appendix_moved L53, appendix_results L7 | n=500 统计功效更高，可能变显著 |
302	
303	---
304	
305	## 7. 数据管道执行顺序
306	
307	1. **等 C2 n=500 全部 16 conditions 完成**（含 DeepSeek 8 + Qwen 8）
308	2. 在服务器执行分析脚本（按依赖顺序）：
309	   ```bash
310	   cd /root/autodl-tmp/pacs
311	   # Step 1: 生成汇总表
312	   python analysis/generate_summary_table.py        # → analysis_output/experiment_summary_table.json
313	
314	   # Step 2: 统计分析（可并行）
315	   python analysis/compute_cohens_d.py               # → analysis_output/cohens_d_bf16.json, cohens_d_bf16_qwen.json
316	   python analysis/cross_model_analysis.py           # → analysis_output/cross_model_analysis.json
317	   python analysis/run_permutation_test.py           # → analysis_output/permutation_test_results.json
318	   python analysis/entropy_analysis.py               # → C4 entropy data (如需更新)
319	
320	   # Step 3: 生成图表
321	   python analysis/generate_paper_figures.py         # → paper_figures/fig1-fig5 PDFs
322	   ```
323	3. 从 JSON 文件提取所有新数值，按本清单 §1-§4 逐项替换
324	4. **关键决策点**：检查 QW s015 Cohen's d CI 是否含零 → 决定 §5 中的叙事方案
325	5. 检查 QW rand s030 是否仍 PASS → 决定 "7/8" vs "8/8"
326	6. 重新编译 LaTeX 验证 → `pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex`
327	7. 全文搜索残留的旧数值（grep "n=50"、"0.39"、"14.59" 等）
328	
329	---
330	
331	## 8. 不需更新的部分
332	
333	- **related_work.tex** — 无实验数据
334	- **background.tex** — 公式定义，无实验数据
335	- **limitations.tex** — 无具体实验数值（sparsity range $s \in \{0.15,...,0.30\}$ 不变）
336	- **methodology.tex** 公式/方法部分 — 无变化（仅 n 和统计描述需更新）
337	- 所有 `\cite{}` 引用 — 无变化
338	
339	---
340	
341	## 9. 更新总量统计
342	
343	| 类别 | 数量 |
344	|------|------|
345	| 样本量文本 "50"→"500" | 7 处 |
346	| 表格（含 8 个表） | ~80 个单元格 |
347	| 图表重新生成 | 5 个 PDF |
348	| 内联统计数值 | ~55 处 |
349	| 条件性叙事更新 (Qwen s015) | 6 处（两套方案） |
350	| 条件性叙事更新 (7/8 vs 8/8) | 4 处 |
351	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "23e0007b-8bd1-48a1-9c60-aa94dc432920",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/c2_n500_paper_update_checklist.md",
      "content": "# C2 n=500 论文更新清单\n\n> 当 C2 n=500 实验（DeepSeek 8 conditions + Qwen 8 conditions）全部完成后，用此清单逐项替换论文中所有 n=50 数据。\n> 数据来源均在服务器 `/root/autodl-tmp/pacs/analysis_output/` 下。\n> **原则**：DeepSeek 和 Qwen 数值绝对值差 ~5×，不可混用；所有数值精确替换，不可近似。\n\n---\n\n## 1. 样本量文本替换（全局搜索 \"50\"）\n\n| 文件 | 行号 | 当前文本 | 替换为 | 类型 |\n|------|------|---------|--------|------|\n| abstract.tex | 6 | `50 MATH-500 problems` | `500 MATH-500 problems` | 文本 |\n| methodology.tex | 10 | `50 problems stratified from MATH-500` | `500 problems from MATH-500` | 文本 |\n| results.tex | 13 | `$n{=}50$ MATH-500 problems` (Table 1 caption) | `$n{=}500$` | 文本 |\n| results.tex | 34 | `medians across 50 problems` (Table 2 caption) | `medians across 500 problems` | 文本 |\n| appendix_moved.tex | 26 | `$n{=}46$ valid problems for Qwen (vs.\\ $n{=}49$ for DeepSeek)` | n=500 后的有效样本量（需从数据计算） | 文本 |\n| appendix_moved.tex | 73 | `$n{=}49$, $10{,}000$ permutations` (Table permutation caption) | 新 n 值 | 文本 |\n| appendix_disc_analysis.tex | 45 | `$n{=}49$ paired problems for DeepSeek (1 excluded) and $n{=}46$ for Qwen (4 excluded)` | 新排除数/有效 n | 文本 |\n\n---\n\n## 2. Tables\n\n### Table 1: Aggregate II (tab:aggregate-ii) — results.tex L10-23\n\n| 行/列 | 当前值 | 数据来源 | 更新类型 |\n|--------|--------|----------|----------|\n| Importance s=0.15 | 0.39 | experiment_summary_table.json → DS imp s015 median_diff | 数值替换 |\n| Importance s=0.20 | 1.48 | experiment_summary_table.json → DS imp s020 median_diff | 数值替换 |\n| Importance s=0.25 | 7.16 | experiment_summary_table.json → DS imp s025 median_diff | 数值替换 |\n| Importance s=0.30 | 14.59 | experiment_summary_table.json → DS imp s030 median_diff | 数值替换 |\n| Random s=0.15 | 0.01 | experiment_summary_table.json → DS rand s015 median_diff | 数值替换 |\n| Random s=0.20 | −0.02 | experiment_summary_table.json → DS rand s020 median_diff | 数值替换 |\n| Random s=0.25 | 0.54 | experiment_summary_table.json → DS rand s025 median_diff | 数值替换 |\n| Random s=0.30 | 1.54 | experiment_summary_table.json → DS rand s030 median_diff | 数值替换 |\n| 正文 L8 | `$0.39$...$14.59$...37×` | 同上，37× = 14.59/0.39 需重算 | 数值+比率 |\n| 正文 L8 | `$-0.02$ to $1.54$` | random range 需从新数据取 | 数值替换 |\n\n### Table 2: Per-phase II breakdown (tab:main-results) — results.tex L31-53\n\n| 行 | II_high | II_mid | II_low | Δ | G | 数据来源 |\n|----|---------|--------|--------|---|---|----------|\n| 0.15 Imp | 0.006 | 0.081 | 0.398 | 0.39 | 69 | DS imp s015 per-phase medians |\n| 0.15 Rand | 0.093 | 0.097 | 0.103 | 0.01 | 1.1 | DS rand s015 per-phase medians |\n| 0.20 Imp | 0.015 | 0.203 | 1.496 | 1.48 | 103 | DS imp s020 per-phase medians |\n| 0.20 Rand | 0.292 | 0.350 | 0.276 | −0.02 | 0.9 | DS rand s020 per-phase medians |\n| 0.25 Imp | 0.032 | 1.118 | 7.196 | 7.16 | 222 | DS imp s025 per-phase medians |\n| 0.25 Rand | 0.818 | 0.932 | 1.363 | 0.54 | 1.7 | DS rand s025 per-phase medians |\n| 0.30 Imp | 0.053 | 2.283 | 14.639 | 14.59 | 274 | DS imp s030 per-phase medians |\n| 0.30 Rand | 2.503 | 2.592 | 4.041 | 1.54 | 1.6 | DS rand s030 per-phase medians |\n\n数据来源：`experiment_summary_table.json` 中各 condition 的 `median_low`, `median_mid`, `median_high`。\n\n### Table 3: Cohen's d (tab:cohens-d) — results.tex L81-97\n\n| 行 | DS d_z | DS Δ̃ [CI] | QW d_z | QW Δ̃ [CI] | 数据来源 |\n|----|--------|-----------|--------|-----------|----------|\n| s=0.15 | 0.44 | 0.32 [0.20, 0.47] | 0.28 | 0.05 [−0.01, 0.11]^ns | cohens_d_bf16.json / cohens_d_bf16_qwen.json |\n| s=0.20 | 0.52 | 1.15 [0.66, 1.26] | 0.55 | 0.21 [0.07, 0.40] | 同上 |\n| s=0.25 | 0.68 | 3.97 [2.83, 5.29] | 0.89 | 1.11 [0.61, 1.47] | 同上 |\n| s=0.30 | 0.80 | 9.94 [8.39, 16.65] | 1.02 | 2.62 [1.72, 3.65] | 同上 |\n\n**注意**：n=500 后 CI 会显著收窄（~√10 倍）。QW s015 的 `ns` 标注取决于 CI 是否仍含零。\n\n### Table: Cross-model comparison (tab:cross-model) — appendix_moved.tex L30-43\n\n| 行 | 当前值 | 数据来源 |\n|----|--------|----------|\n| DeepSeek s015/s020/s025/s030 | 0.39 / 1.48 / 7.16 / 14.59 | experiment_summary_table.json DS imp |\n| Qwen s015/s020/s025/s030 | 0.04 / 0.23 / 1.27 / 2.94 | experiment_summary_table.json QW imp |\n\n### Table: Permutation test (tab:permutation) — appendix_moved.tex L70-85\n\n| s | Observed Δ̃ | 95% CI | p_Bonf | 数据来源 |\n|---|-----------|--------|--------|----------|\n| 0.15 | 0.37 | [0.19, 0.62] | 0.0032 | permutation_test_results.json |\n| 0.20 | 0.97 | [0.69, 1.49] | <0.001 | 同上 |\n| 0.25 | 3.34 | [1.66, 6.64] | <0.001 | 同上 |\n| 0.30 | 9.85 | [6.70, 16.29] | <0.001 | 同上 |\n\n### Table: Discrimination metrics (tab:discrimination-metrics-full) — appendix_moved.tex L103-123\n\n| Model | s | ΔGini | ΔCV | 数据来源 |\n|-------|---|-------|-----|----------|\n| DS 0.15 | −0.030 | −0.56 | c4_entropy_deepseek |\n| DS 0.20 | −0.040 | −0.77 | 同上 |\n| DS 0.25 | −0.065 | −1.29 | 同上 |\n| DS 0.30 | −0.081 | −1.66 | 同上 |\n| QW 0.15 | −0.010 | −0.05 | c4_entropy_qwen |\n| QW 0.20 | −0.012 | −0.21 | 同上 |\n| QW 0.25 | −0.010 | −1.49 | 同上 |\n| QW 0.30 | −0.020 | −1.14 | 同上 |\n\n**注意**：C4 entropy 分析需要用 n=500 数据重跑 `analysis/entropy_analysis.py`。\n\n### Table: Entropy deltas (tab:entropy-deltas) — appendix_moved.tex L143-163\n\n| Model | s | ΔH | 数据来源 |\n|-------|---|----|----------|\n| DS 0.15 | −0.040 | c4_entropy_deepseek |\n| DS 0.20 | −0.047 | 同上 |\n| DS 0.25 | −0.045 | 同上 |\n| DS 0.30 | −0.044 | 同上 |\n| QW 0.15 | −0.073 | c4_entropy_qwen |\n| QW 0.20 | −0.076 | 同上 |\n| QW 0.25 | +0.045 | 同上 |\n| QW 0.30 | −0.007 | 同上 |\n\n---\n\n## 3. Figures\n\n| Figure | 文件 | 数据来源 | 需更新内容 |\n|--------|------|----------|-----------|\n| Fig 1 (fig:hero) — fig1_dose_response.pdf | results.tex L55-60 | experiment_summary_table.json G values | G 曲线数据点 + caption 中 `$69{\\times}$ to $274{\\times}$` |\n| Fig 2 — fig2_cohens_d (如存在) | 位置待定 | cohens_d_bf16.json, cohens_d_bf16_qwen.json | Cohen's d 森林图 |\n| Fig 3 (fig:crossover) — fig3_crossover.pdf | appendix_moved.tex L13-18 | experiment_summary_table.json DS s025 | 柱状图数据 + caption 中 `$5.3{\\times}$` |\n| Fig 4 (fig:permtest-forest) — fig4_bootstrap.pdf | appendix_moved.tex L87-92 | permutation_test_results.json | CI 横条 + 点估计值 |\n| Fig 5 (fig:cross-model) — fig5_crossmodel.pdf | appendix_moved.tex L46-50 | experiment_summary_table.json DS+QW imp | 双曲线数据点 + caption 中 `one-fifth` 比例 |\n\n**图表生成脚本**（服务器端）：\n- `/root/autodl-tmp/pacs/analysis/generate_paper_figures.py` — fig4, fig5\n- `/root/autodl-tmp/pacs/analysis/generate_summary_table.py` — experiment_summary_table.json\n- `/root/autodl-tmp/pacs/analysis/cross_model_analysis.py` — cross_model_analysis.json\n- `/root/autodl-tmp/pacs/analysis/compute_cohens_d.py` — cohens_d_bf16.json\n\n**更新流程**：先用 n=500 profiling 数据重跑 `generate_summary_table.py`，再重跑各分析脚本，最后重新生成所有图表 PDF。\n\n---\n\n## 4. 正文中的内联统计声明\n\n### abstract.tex\n\n| 行 | 当前文本 | 数据来源 | 类型 |\n|----|---------|----------|------|\n| 7 | `median Interaction Index difference...increases monotonically from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$` | experiment_summary_table.json DS imp | 数值 |\n| 7 | `paired Cohen's $d_z$ growing from $0.44$ (small) to $0.80$ (large)` | cohens_d_bf16.json | 数值 |\n| 7 | `$p < 0.005$ at all four sparsity levels` | permutation_test_results.json | 阈值判断 |\n| 8 | `7/8 conditions` | 重新统计 random PASS/FAIL | 计数 |\n| 8 | `Qwen $s{=}0.30$, $p{=}0.012$` | QW rand s030 permutation test | 数值 |\n| 8 | `$d_z{=}{-}0.04$` | QW rand s030 Cohen's d | 数值 |\n| 9 | `$\\widetilde{\\mathrm{II}} = 0.032$ vs.\\ $0.818$` | DS imp/rand s025 high-phase medians | 数值 |\n| 9 | `$\\widetilde{\\mathrm{II}} = 7.196$ vs.\\ $1.363$` | DS imp/rand s025 low-phase medians | 数值 |\n| 10 | `$d_z \\geq 0.55$` | cohens_d_bf16_qwen.json s020 | 阈值 |\n| 10 | `Spearman $\\rho = 1.0$` | cross_model_analysis.json | 数值 |\n| 10 | `gradient permutation $p = 0.043$` | cross_model_analysis.json | 数值 |\n\n### introduction.tex\n\n| 行 | 当前文本 | 数据来源 | 类型 |\n|----|---------|----------|------|\n| 14 | `$0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$` | experiment_summary_table.json DS imp | 数值 |\n| 14 | `$d_z$: $0.44 \\to 0.80$` | cohens_d_bf16.json | 数值 |\n| 14 | `Bonferroni-corrected $p < 0.005$ at all levels` | permutation_test_results.json | 阈值判断 |\n| 15 | `$d_z \\geq 0.55$` | cohens_d_bf16_qwen.json s020 | 阈值 |\n| 16 | `7/8 conditions non-significant` | 重新统计 random PASS/FAIL | 计数 |\n\n### methodology.tex\n\n| 行 | 当前文本 | 数据来源 | 类型 |\n|----|---------|----------|------|\n| 18 | `mean/median ratios up to 43:1` | 从 n=500 数据重新计算 | 数值 |\n| 22 | `$p_{\\text{Bonf}} < 0.005$ at every sparsity level` | permutation_test_results.json | 阈值判断 |\n\n### results.tex (正文段落)\n\n| 行 | 当前文本 | 数据来源 | 类型 |\n|----|---------|----------|------|\n| 8 | `$37{\\times}$ amplification` | 新 Δ_s030 / Δ_s015 需重算 | 比率 |\n| 29 | `$69{\\times}$ at $s{=}0.15$ to $274{\\times}$ at $s{=}0.30$` | Table 2 G 列 | 数值 |\n| 29 | `$0.006$ to $0.053$` | Table 2 II_high 列 min/max | 数值 |\n| 29 | `$G \\approx 0.9$--$1.7{\\times}$` | Table 2 random G 列 range | 数值 |\n| 66 | `$0.032$ vs.\\ $0.818$`...`$7.196$ vs.\\ $1.363$---a $5.3{\\times}$` | s025 per-phase medians | 数值+比率 |\n| 71 | `$\\Delta$ increases from $0.04$...$2.94$...${\\sim}1/5$` | experiment_summary_table.json QW imp | 数值+比率 |\n| 71 | `$d_z \\geq 0.55$; Spearman $\\rho = 1.0$; gradient permutation $p = 0.043$` | cross_model_analysis.json | 数值 |\n| 71 | `$d_z{=}0.28$, CI includes zero` | cohens_d_bf16_qwen.json s015 | 数值+判断 |\n| 77 | `$0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$` | permutation_test_results.json | 数值 |\n| 79 | `$d_z{=}0.44$ (small) to $d_z{=}0.80$ (large)` | cohens_d_bf16.json | 数值 |\n| 79 | `$d_z{=}0.28$...CI includes zero`...`$d_z \\geq 0.55$` | cohens_d_bf16_qwen.json | 数值+判断 |\n| 79 | `$d_z{=}0.89$/$1.02$ vs.\\ $0.68$/$0.80$` | cohens_d 两模型对比 | 数值 |\n\n### analysis.tex\n\n| 行 | 当前文本 | 数据来源 | 类型 |\n|----|---------|----------|------|\n| 4 | `$0.030$--$0.081$ (DeepSeek) and $0.010$--$0.020$ (Qwen)` | c4_entropy 分析 ΔGini ranges | 数值 |\n| 4 | `16 conditions` | 确认是否仍为 16 | 计数 |\n| 6 | `$\\Delta\\mathcal{H} \\in [-0.047, -0.040]$` | c4_entropy_deepseek entropy deltas | 数值 |\n| 6 | `$\\Delta\\mathcal{H} = +0.045$` | c4_entropy_qwen s025 | 数值 |\n| 6 | `22 of 30 problems` | n=500 后需重算（可能变为 ~220 of 300） | 计数 |\n\n### discussion.tex\n\n| 行 | 当前文本 | 数据来源 | 类型 |\n|----|---------|----------|------|\n| 5 | `$69$--$274{\\times}$` | Table 2 G range | 数值 |\n| 5 | `$\\widetilde{\\mathrm{II}} = 0.032$ vs.\\ $0.818$` | s025 high-phase | 数值 |\n| 5 | `$7.196$ vs.\\ $1.363$` | s025 low-phase | 数值 |\n| 5 | `$G \\approx 1$` | random G（确认仍成立） | 数值 |\n\n### conclusion.tex\n\n| 行 | 当前文本 | 数据来源 | 类型 |\n|----|---------|----------|------|\n| 4 | `$69{\\times}$ to $274{\\times}$` | Table 2 G range | 数值 |\n| 4 | `$d_z$: $0.44 \\to 0.80$` | cohens_d_bf16.json | 数值 |\n| 4 | `7/8 conditions non-significant` | random PASS/FAIL 重统计 | 计数 |\n| 4 | `$d_z \\geq 0.55$` | cohens_d_bf16_qwen.json s020 | 阈值 |\n\n### appendix.tex\n\n| 行 | 当前文本 | 数据来源 | 类型 |\n|----|---------|----------|------|\n| 38 | `$G_{\\times} = 58$--$241{\\times}$` | 乘法 null 下 G range 需重算 | 数值 |\n\n### appendix_moved.tex (正文段落)\n\n| 行 | 当前文本 | 数据来源 | 类型 |\n|----|---------|----------|------|\n| 11 | `$0.032$ vs.\\ $0.818$`...`$7.196$ vs.\\ $1.363$---a $5.3{\\times}$` | s025 per-phase medians | 数值+比率 |\n| 11 | `$3.9{\\times}$...$5.4{\\times}$...$5.3{\\times}$...$3.6{\\times}$` | 各 sparsity level crossover reversal magnitudes | 数值 |\n| 26 | `Four of the 50 problems are excluded` | QW excluded count n=500 | 计数 |\n| 53 | `mean $\\rho = -0.11$, $p = 0.926$` | cross_model_analysis.json | 数值 |\n| 56 | `$p = 0.012$...d_z = -0.04` | QW rand s030 | 数值 |\n| 64 | `mean/median ratios ranging from $1.2{\\times}$...$1.6{\\times}$` and `$1.1{\\times}$ to $1.4{\\times}$ for Qwen` | 从 n=500 per-problem diffs 计算 | 数值 |\n| 66 | `$99.92$th percentile...p_Bonf = 0.0032` | permutation_test_results.json s015 | 数值 |\n| 68 | `$0.37$...$9.85$...CI lower bound ($0.19 \\to 0.69 \\to 1.66 \\to 6.70$)` | permutation_test_results.json | 数值 |\n\n### appendix_disc_analysis.tex (正文段落)\n\n| 行 | 当前文本 | 数据来源 | 类型 |\n|----|---------|----------|------|\n| 4 | `$-0.031$ to $-0.073$; Qwen: $-0.019$ to $-0.045$` | random eviction Gini 变化 | 数值 |\n| 11 | `$\\widetilde{\\mathrm{II}}_{\\text{high}} < 0.06$ at $s \\leq 0.30$` | Table 2 high-phase range | 数值 |\n| 11 | `$s = 0.35$, high-phase II rises to $0.105$` | bf16_ds_imp_s035 数据 | 数值 |\n| 14 | `7/8...Qwen $s{=}0.30$, $p{=}0.012$...$d_z{=}{-}0.04$` | QW rand s030 统计 | 数值 |\n| 45 | `$n{=}49$...$n{=}46$` | 有效样本量 | 计数 |\n| 46 | `mean/median ratio ${\\sim}1.6{:}1$...mean_diff=22.94, median_diff=14.59` | s030 skewness stats | 数值 |\n| 47 | CIs: `$[0.19,\\; 0.62]$...$[0.69,\\; 1.49]$...$[1.66,\\; 6.64]$...$[6.70,\\; 16.29]$` | permutation_test_results.json | 数值 |\n| 49 | `$p{=}0.012$...$d_z{=}{-}0.04$...d=-0.035` | QW rand s030 re-bootstrap | 数值 |\n\n### appendix_results.tex\n\n| 行 | 当前文本 | 数据来源 | 类型 |\n|----|---------|----------|------|\n| 7 | `mean $\\rho = -0.11$, $p = 0.926$` | cross_model_analysis.json | 数值 |\n| 10 | `$p = 0.012$...d_z = -0.04` | QW rand s030 | 数值 |\n\n---\n\n## 5. Qwen s015 预注册决策点 (D037/D038)\n\n### 当前状态\nQwen s015: d_z=0.28, CI=[−0.006, 0.60] → **不显著**，论文采用 \"threshold narrative\"。\n\n### 决策矩阵\n\n| n=500 结果 | CI 位置 | 操作 |\n|-----------|---------|------|\n| CI 完全 > 0 | 例如 [0.05, 0.35] | **升级**：删除 `^ns` 标注，改叙事为 \"effect reliable at all four sparsity levels for both models\" |\n| CI 仍跨零 | 例如 [−0.02, 0.15] | **维持 threshold narrative**：保持当前表述不变，仅更新数值 |\n\n### CI 跨零时需更新的叙事位置（仅更新数值，保留 threshold 表述）\n\n| 文件 | 行 | 当前叙事 | 操作 |\n|------|------|---------|------|\n| abstract.tex | 10 | `replicates on Qwen2.5-7B-Instruct at $s \\geq 0.20$` | 更新 d_z 数值，保留 `$s \\geq 0.20$` |\n| introduction.tex | 15 | `$d_z \\geq 0.55$` | 更新阈值数值 |\n| results.tex | 71 | `marginal at $s{=}0.15$ ($d_z{=}0.28$, CI includes zero) but reliable at $s \\geq 0.20$ ($d_z \\geq 0.55$)` | 更新所有数值 |\n| results.tex | 90 | `0.28` & `0.05\\; $[-0.01, 0.11]$\\textsuperscript{ns}` | 更新数值，保留 `^ns` |\n| results.tex | 95 | `\\textsuperscript{ns}Marginal at $s{=}0.15$; reliable at $s \\geq 0.20$.` | 保留 |\n| conclusion.tex | 4 | `$d_z \\geq 0.55$` | 更新数值 |\n\n### CI > 0 时需更新的叙事位置（升级方案）\n\n| 文件 | 行 | 当前叙事 | 备选叙事 |\n|------|------|---------|----------|\n| abstract.tex | 10 | `at $s \\geq 0.20$` | `at all four sparsity levels` |\n| introduction.tex | 15 | `$d_z \\geq 0.55$` | `$d_z \\geq [新s015值]$`（改用 s015 值） |\n| results.tex | 71 | `marginal at $s{=}0.15$...reliable at $s \\geq 0.20$` | `reliable at all four sparsity levels ($d_z \\geq [新值]$)` |\n| results.tex | 90 | `\\textsuperscript{ns}` | 删除 `^ns` 标注 |\n| results.tex | 95 | 脚注 `Marginal at...reliable at...` | 删除或改为 `All levels significant.` |\n| conclusion.tex | 4 | `$d_z \\geq 0.55$` | `$d_z \\geq [新s015值]$` |\n\n---\n\n## 6. 附属统计量（可能变化但方向不变）\n\n以下数值的 n=500 版本大概率方向不变，但绝对值会变：\n\n| 统计量 | 当前值 | 出现位置 | 预期变化 |\n|--------|--------|---------|----------|\n| mean/median ratio | up to 43:1 | methodology.tex L18 | n=500 尾部更极端，可能变大或变小 |\n| \"7/8 conditions\" random non-significant | 7/8 | abstract, intro, conclusion, appendix_disc | n=500 CI 更窄，QW rand s030 borderline PASS 可能翻转为 FAIL → 变成 8/8 |\n| DS/QW magnitude ratio | ~1/5 | results.tex L71, fig5 caption | 可能略变 |\n| Crossover reversal magnitudes | 3.9×–5.4× | appendix_moved.tex L11 | 数据驱动，需重算 |\n| Spearman ρ for monotonicity | 1.0 | abstract L10, results L71 | 4 点排序，大概率仍=1.0 |\n| Gradient permutation p | 0.043 | abstract L10, results L71 | 4! = 24 种排列，最小 p=1/24≈0.042 |\n| Per-problem concordance | ρ=−0.11, p=0.926 | appendix_moved L53, appendix_results L7 | n=500 统计功效更高，可能变显著 |\n\n---\n\n## 7. 数据管道执行顺序\n\n1. **等 C2 n=500 全部 16 conditions 完成**（含 DeepSeek 8 + Qwen 8）\n2. 在服务器执行分析脚本（按依赖顺序）：\n   ```bash\n   cd /root/autodl-tmp/pacs\n   # Step 1: 生成汇总表\n   python analysis/generate_summary_table.py        # → analysis_output/experiment_summary_table.json\n\n   # Step 2: 统计分析（可并行）\n   python analysis/compute_cohens_d.py               # → analysis_output/cohens_d_bf16.json, cohens_d_bf16_qwen.json\n   python analysis/cross_model_analysis.py           # → analysis_output/cross_model_analysis.json\n   python analysis/run_permutation_test.py           # → analysis_output/permutation_test_results.json\n   python analysis/entropy_analysis.py               # → C4 entropy data (如需更新)\n\n   # Step 3: 生成图表\n   python analysis/generate_paper_figures.py         # → paper_figures/fig1-fig5 PDFs\n   ```\n3. 从 JSON 文件提取所有新数值，按本清单 §1-§4 逐项替换\n4. **关键决策点**：检查 QW s015 Cohen's d CI 是否含零 → 决定 §5 中的叙事方案\n5. 检查 QW rand s030 是否仍 PASS → 决定 \"7/8\" vs \"8/8\"\n6. 重新编译 LaTeX 验证 → `pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex`\n7. 全文搜索残留的旧数值（grep \"n=50\"、\"0.39\"、\"14.59\" 等）\n\n---\n\n## 8. 不需更新的部分\n\n- **related_work.tex** — 无实验数据\n- **background.tex** — 公式定义，无实验数据\n- **limitations.tex** — 无具体实验数值（sparsity range $s \\in \\{0.15,...,0.30\\}$ 不变）\n- **methodology.tex** 公式/方法部分 — 无变化（仅 n 和统计描述需更新）\n- 所有 `\\cite{}` 引用 — 无变化\n\n---\n\n## 9. 更新总量统计\n\n| 类别 | 数量 |\n|------|------|\n| 样本量文本 \"50\"→\"500\" | 7 处 |\n| 表格（含 8 个表） | ~80 个单元格 |\n| 图表重新生成 | 5 个 PDF |\n| 内联统计数值 | ~55 处 |\n| 条件性叙事更新 (Qwen s015) | 6 处（两套方案） |\n| 条件性叙事更新 (7/8 vs 8/8) | 4 处 |\n",
      "numLines": 351,
      "startLine": 1,
      "totalLines": 351
    }
  }
}
````

</details>

---

### Tool call

_source line 26_

<details open><summary>🔧 Tool call — Grep · `toolu_013WRNV1Y7sgiszJt3wmqDcx`</summary>

```json
{
  "pattern": "n\\s*=\\s*50[^0]|n=50[^0]|\\b50 problems\\b|\\b50 samples\\b|\\bfifty\\b|\\\\\\\\(n=50\\\\\\\\)|n\\{50\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "output_mode": "content",
  "-n": true,
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "d1be92b8-4011-462c-b352-3e02b690a57f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014xZ7cBKwnKLFdsDoUmQzRY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2592,
      "cache_read_input_tokens": 40925,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2592
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

_source line 27 · 2026-05-14T20:43:14.108Z_

<details><summary>↩ Tool result · `toolu_013WRNV1Y7sgiszJt3wmqDcx`</summary>

```text
artifacts/_project/paper/appendix_moved.tex:26:Despite lacking explicit \texttt{&lt;think>} delimiters, Qwen2.5-7B-Instruct exhibits sufficient variation in attention sparsity to permit phase segmentation via the same quantile-based method (\S\ref{sec:phase-segmentation}). Four of the 50 problems are excluded due to degenerate phase assignments, yielding $n{=}46$ valid problems for Qwen (vs.\ $n{=}49$ for DeepSeek).
artifacts/_project/paper/methodology.tex:10:We use 50 problems stratified from MATH-500~\cite{math500-neurips2021}, sampling uniformly across categories with a fixed seed. Each problem is decoded greedily (\texttt{max\_new\_tokens}$=$2048).
artifacts/_project/paper/results.tex:34:\caption{Interaction index (II) by eviction strategy, reasoning phase, and sparsity level. II values are problem-level medians across 50 problems. $\Delta = \widetilde{\mathrm{II}}_{\textit{low}} - \widetilde{\mathrm{II}}_{\textit{high}}$. $G = \widetilde{\mathrm{II}}_{\textit{low}} / \widetilde{\mathrm{II}}_{\textit{high}}$.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "7a779aef-32c0-4791-bfaf-cc052111e4af",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "artifacts/_project/paper/appendix_moved.tex:26:Despite lacking explicit \\texttt{&lt;think>} delimiters, Qwen2.5-7B-Instruct exhibits sufficient variation in attention sparsity to permit phase segmentation via the same quantile-based method (\\S\\ref{sec:phase-segmentation}). Four of the 50 problems are excluded due to degenerate phase assignments, yielding $n{=}46$ valid problems for Qwen (vs.\\ $n{=}49$ for DeepSeek).\nartifacts/_project/paper/methodology.tex:10:We use 50 problems stratified from MATH-500~\\cite{math500-neurips2021}, sampling uniformly across categories with a fixed seed. Each problem is decoded greedily (\\texttt{max\\_new\\_tokens}$=$2048).\nartifacts/_project/paper/results.tex:34:\\caption{Interaction index (II) by eviction strategy, reasoning phase, and sparsity level. II values are problem-level medians across 50 problems. $\\Delta = \\widetilde{\\mathrm{II}}_{\\textit{low}} - \\widetilde{\\mathrm{II}}_{\\textit{high}}$. $G = \\widetilde{\\mathrm{II}}_{\\textit{low}} / \\widetilde{\\mathrm{II}}_{\\textit{high}}$.}",
    "numLines": 3
  }
}
```

</details>

---

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — Grep · `toolu_01R8tVrDszQ214FVgLn8iapS`</summary>

```json
{
  "pattern": "0\\.32|1\\.15|3\\.97|9\\.94|0\\.048|0\\.208|1\\.109|2\\.619|0\\.44|0\\.80|0\\.28|1\\.02",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "output_mode": "content",
  "-n": true,
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "481f678e-405e-465a-bc7f-b352ae69e4c2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014xZ7cBKwnKLFdsDoUmQzRY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2592,
      "cache_read_input_tokens": 40925,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2592
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

_source line 29 · 2026-05-14T20:43:16.030Z_

<details><summary>↩ Tool result · `toolu_01R8tVrDszQ214FVgLn8iapS`</summary>

```text
artifacts/_project/paper/conclusion.tex:4:[Omitted long matching line]
artifacts/_project/paper/abstract.tex:7:Under importance-based KV cache eviction, the median Interaction Index difference between low-sparsity and high-sparsity reasoning phases increases monotonically from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired Cohen's $d_z$ growing from $0.44$ (small) to $0.80$ (large); Bonferroni-corrected permutation tests yield $p < 0.005$ at all four sparsity levels.
artifacts/_project/paper/appendix_disc_analysis.tex:46:The severity difference distribution is right-skewed (mean/median ratio ${\sim}1.6{:}1$ at $s{=}0.30$), motivating our use of medians and nonparametric tests rather than parametric alternatives. % exp_id: bf16_importance_s030; mean_diff=22.94, median_diff=14.59 (segment-level). Per-problem paired: median_diff=9.9436 at s030
artifacts/_project/paper/introduction.tex:14:On DeepSeek-R1-Distill-Qwen-7B, the median phase difference rises from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$ ($d_z$: $0.44 \to 0.80$; Bonferroni-corrected $p < 0.005$ at all levels).
artifacts/_project/paper/results.tex:71:[Omitted long matching line]
artifacts/_project/paper/results.tex:106:[Omitted long matching line]
artifacts/_project/paper/results.tex:117:0.15 & 0.44 & 0.32\; $[0.20, 0.47]$ & 0.28 & 0.05\; $[-0.01, 0.11]$\textsuperscript{ns} \\ % exp_id: bf16_ds_imp_s015, bf16_qw_imp_s015
artifacts/_project/paper/results.tex:118:0.20 & 0.52 & 1.15\; $[0.66, 1.26]$ & 0.55 & 0.21\; $[0.07, 0.40]$ \\ % exp_id: bf16_ds_imp_s020, bf16_qw_imp_s020
artifacts/_project/paper/results.tex:119:0.25 & 0.68 & 3.97\; $[2.83, 5.29]$ & 0.89 & 1.11\; $[0.61, 1.47]$ \\ % exp_id: bf16_ds_imp_s025, bf16_qw_imp_s025
artifacts/_project/paper/results.tex:120:0.30 & 0.80 & 9.94\; $[8.39, 16.65]$ & 1.02 & 2.62\; $[1.72, 3.65]$ \\ % exp_id: bf16_ds_imp_s030, bf16_qw_imp_s030
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "12cf00ab-8847-43b4-b777-dc9d70f00be8",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "artifacts/_project/paper/conclusion.tex:4:[Omitted long matching line]\nartifacts/_project/paper/abstract.tex:7:Under importance-based KV cache eviction, the median Interaction Index difference between low-sparsity and high-sparsity reasoning phases increases monotonically from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired Cohen's $d_z$ growing from $0.44$ (small) to $0.80$ (large); Bonferroni-corrected permutation tests yield $p < 0.005$ at all four sparsity levels.\nartifacts/_project/paper/appendix_disc_analysis.tex:46:The severity difference distribution is right-skewed (mean/median ratio ${\\sim}1.6{:}1$ at $s{=}0.30$), motivating our use of medians and nonparametric tests rather than parametric alternatives. % exp_id: bf16_importance_s030; mean_diff=22.94, median_diff=14.59 (segment-level). Per-problem paired: median_diff=9.9436 at s030\nartifacts/_project/paper/introduction.tex:14:On DeepSeek-R1-Distill-Qwen-7B, the median phase difference rises from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$ ($d_z$: $0.44 \\to 0.80$; Bonferroni-corrected $p < 0.005$ at all levels).\nartifacts/_project/paper/results.tex:71:[Omitted long matching line]\nartifacts/_project/paper/results.tex:106:[Omitted long matching line]\nartifacts/_project/paper/results.tex:117:0.15 & 0.44 & 0.32\\; $[0.20, 0.47]$ & 0.28 & 0.05\\; $[-0.01, 0.11]$\\textsuperscript{ns} \\\\ % exp_id: bf16_ds_imp_s015, bf16_qw_imp_s015\nartifacts/_project/paper/results.tex:118:0.20 & 0.52 & 1.15\\; $[0.66, 1.26]$ & 0.55 & 0.21\\; $[0.07, 0.40]$ \\\\ % exp_id: bf16_ds_imp_s020, bf16_qw_imp_s020\nartifacts/_project/paper/results.tex:119:0.25 & 0.68 & 3.97\\; $[2.83, 5.29]$ & 0.89 & 1.11\\; $[0.61, 1.47]$ \\\\ % exp_id: bf16_ds_imp_s025, bf16_qw_imp_s025\nartifacts/_project/paper/results.tex:120:0.30 & 0.80 & 9.94\\; $[8.39, 16.65]$ & 1.02 & 2.62\\; $[1.72, 3.65]$ \\\\ % exp_id: bf16_ds_imp_s030, bf16_qw_imp_s030",
    "numLines": 10
  }
}
```

</details>

---

### Assistant

_source line 30_

<details><summary>Logged reasoning block</summary>

```text
I have the existing checklist. It's already very comprehensive! Let me now read the actual tex files to verify completeness and check for any missed references. I also need to search for LLaMA/C8 related content and the n=50 specific values. Let me also check the existing checklist at the _project path to see if it differs.

Let me now also search for any additional n=50 references that might have been missed, and check for references to specific bf16 numbers in sections not yet covered. Let me read the key tex files to verify line numbers and completeness.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "22e27c7c-fb77-466c-a799-4ddc6ea36b77",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HZBWX7aVv9CJvt4SDwjLSK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11820,
      "cache_read_input_tokens": 43517,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11820
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

_source line 31_

已有一份详尽的清单。现在验证其完整性——读取关键 tex 文件确认行号准确性，并搜索可能遗漏的引用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "8a86c8c0-a9e2-4923-940d-c9695aef4f81",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HZBWX7aVv9CJvt4SDwjLSK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11820,
      "cache_read_input_tokens": 43517,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11820
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

_source line 32_

<details open><summary>🔧 Tool call — Agent · `toolu_015fDGgMfXwTBX4qwXJq1TS4`</summary>

```json
{
  "description": "Verify tex file line numbers",
  "prompt": "I need you to read specific sections of the paper tex files in this project and report the exact content at specified line numbers. The paper is at /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/\n\nRead these files completely:\n1. abstract.tex\n2. introduction.tex  \n3. methodology.tex\n4. results.tex\n5. conclusion.tex\n6. discussion.tex\n7. analysis.tex\n8. appendix_moved.tex\n9. appendix_disc_analysis.tex\n10. appendix_results.tex\n11. appendix.tex\n12. limitations.tex\n\nFor each file, report:\n- Total line count\n- ALL lines containing any of these patterns: \"50\" (as in n=50, 50 problems), \"0.32\", \"1.15\", \"3.97\", \"9.94\", \"0.048\", \"0.208\", \"1.109\", \"2.619\", \"0.44\", \"0.80\", \"0.28\", \"1.02\", \"14.59\", \"0.39\", \"7.16\", \"69\", \"274\", \"7/8\", \"qualitative\", \"n=500\", \"C5b\", \"C8\", \"LLaMA\", \"Llama\", \"future work\"\n\nReport the exact line number and content for each match. This is for verifying a paper update checklist, so precision matters.",
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
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "46832a52-2bbe-4c18-9bd2-c73b233acf5b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HZBWX7aVv9CJvt4SDwjLSK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11820,
      "cache_read_input_tokens": 43517,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11820
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

_source line 33_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a317f67854c5856c4",
  "tool_use_id": "toolu_015fDGgMfXwTBX4qwXJq1TS4",
  "description": "Verify tex file line numbers",
  "task_type": "local_agent",
  "prompt": "I need you to read specific sections of the paper tex files in this project and report the exact content at specified line numbers. The paper is at /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/\n\nRead these files completely:\n1. abstract.tex\n2. introduction.tex  \n3. methodology.tex\n4. results.tex\n5. conclusion.tex\n6. discussion.tex\n7. analysis.tex\n8. appendix_moved.tex\n9. appendix_disc_analysis.tex\n10. appendix_results.tex\n11. appendix.tex\n12. limitations.tex\n\nFor each file, report:\n- Total line count\n- ALL lines containing any of these patterns: \"50\" (as in n=50, 50 problems), \"0.32\", \"1.15\", \"3.97\", \"9.94\", \"0.048\", \"0.208\", \"1.109\", \"2.619\", \"0.44\", \"0.80\", \"0.28\", \"1.02\", \"14.59\", \"0.39\", \"7.16\", \"69\", \"274\", \"7/8\", \"qualitative\", \"n=500\", \"C5b\", \"C8\", \"LLaMA\", \"Llama\", \"future work\"\n\nReport the exact line number and content for each match. This is for verifying a paper update checklist, so precision matters.",
  "uuid": "a6f704a0-802d-47bc-b222-06ff998945f0",
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3"
}
```

---

## Round 1

81 recorded events

### User

_source line 34 · 2026-05-14T20:43:31.797Z_

I need you to read specific sections of the paper tex files in this project and report the exact content at specified line numbers. The paper is at /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/

Read these files completely:
1. abstract.tex
2. introduction.tex  
3. methodology.tex
4. results.tex
5. conclusion.tex
6. discussion.tex
7. analysis.tex
8. appendix_moved.tex
9. appendix_disc_analysis.tex
10. appendix_results.tex
11. appendix.tex
12. limitations.tex

For each file, report:
- Total line count
- ALL lines containing any of these patterns: "50" (as in n=50, 50 problems), "0.32", "1.15", "3.97", "9.94", "0.048", "0.208", "1.109", "2.619", "0.44", "0.80", "0.28", "1.02", "14.59", "0.39", "7.16", "69", "274", "7/8", "qualitative", "n=500", "C5b", "C8", "LLaMA", "Llama", "future work"

Report the exact line number and content for each match. This is for verifying a paper update checklist, so precision matters.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015fDGgMfXwTBX4qwXJq1TS4",
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "d5759384-c2ea-406b-ae78-4fb41a8bbe54"
}
```

</details>

---

### System

_source line 35_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a317f67854c5856c4",
  "tool_use_id": "toolu_015fDGgMfXwTBX4qwXJq1TS4",
  "description": "Running List paper directory contents",
  "usage": {
    "total_tokens": 14268,
    "tool_uses": 1,
    "duration_ms": 2509
  },
  "last_tool_name": "Bash",
  "uuid": "940d68b7-d5ac-452e-ad86-c2930663682f",
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3"
}
```

---

### Tool call

_source line 36_

<details open><summary>🔧 Tool call — Bash · `toolu_01URo6JG45Z1R16P89YZFjC1`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/",
  "description": "List paper directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015fDGgMfXwTBX4qwXJq1TS4",
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "2c37f4c3-a5cd-4118-8d56-5de0f7bf3cc1",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_015TzbpcXHD7Uh2xVx8xssG1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14263,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14263,
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

_source line 37 · 2026-05-14T20:43:34.488Z_

<details><summary>↩ Tool result · `toolu_01URo6JG45Z1R16P89YZFjC1`</summary>

```text
_archive
_pdf_images
abstract.tex
acl.sty
acl_natbib.bst
analysis.tex
appendix.tex
appendix_disc_analysis.tex
appendix_moved.tex
appendix_results.tex
background.tex
citation_audit_report.md
conclusion.tex
discussion.tex
figures
introduction.tex
limitations.tex
main.aux
main.bbl
main.blg
main.fdb_latexmk
main.fls
main.log
main.out
main.pdf
main.tex
main_00fdd3.pdf
main_5d82e3.pdf
main_9a05ce.pdf
main_a1a036.pdf
main_bdfc72.pdf
main_c93d3b.pdf
methodology.tex
numerical_audit_report.md
paper_compilation_note.txt
references.bib
related_work.tex
results.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015fDGgMfXwTBX4qwXJq1TS4",
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "fd40c7b3-3fc6-4469-bf9f-a55d5aaafa76"
}
```

</details>

---

### System

_source line 38_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a317f67854c5856c4",
  "tool_use_id": "toolu_015fDGgMfXwTBX4qwXJq1TS4",
  "description": "Running Get line counts for all specified files",
  "usage": {
    "total_tokens": 15530,
    "tool_uses": 2,
    "duration_ms": 5678
  },
  "last_tool_name": "Bash",
  "uuid": "8eb17942-0334-4060-8bf7-ef3c36979ce1",
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3"
}
```

---

### Tool call

_source line 39_

<details open><summary>🔧 Tool call — Bash · `toolu_01UKx8zhwXm1nJmSW5MaGeLt`</summary>

```json
{
  "command": "for f in abstract.tex introduction.tex methodology.tex results.tex conclusion.tex discussion.tex analysis.tex appendix_moved.tex appendix_disc_analysis.tex appendix_results.tex appendix.tex limitations.tex; do\n  fp=\"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/$f\"\n  if [ -f \"$fp\" ]; then\n    echo \"=== $f: $(wc -l < \"$fp\") lines ===\"\n  else\n    echo \"=== $f: NOT FOUND ===\"\n  fi\ndone",
  "description": "Get line counts for all specified files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015fDGgMfXwTBX4qwXJq1TS4",
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "eae89c72-9457-440b-8150-b9338d671110",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019xxep6KdK7KvwH2ALpGARS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1207,
      "cache_read_input_tokens": 14263,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1207,
        "ephemeral_1h_input_tokens": 0
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

_source line 40 · 2026-05-14T20:43:37.615Z_

<details><summary>↩ Tool result · `toolu_01UKx8zhwXm1nJmSW5MaGeLt`</summary>

```text
=== abstract.tex: 13 lines ===
=== introduction.tex: 25 lines ===
=== methodology.tex: 22 lines ===
=== results.tex: 126 lines ===
=== conclusion.tex: 5 lines ===
=== discussion.tex: 11 lines ===
=== analysis.tex: 6 lines ===
=== appendix_moved.tex: 163 lines ===
=== appendix_disc_analysis.tex: 64 lines ===
=== appendix_results.tex: 10 lines ===
=== appendix.tex: 40 lines ===
=== limitations.tex: 11 lines ===
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015fDGgMfXwTBX4qwXJq1TS4",
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "241d3a77-d92a-4c9c-957d-07050921bf1c"
}
```

</details>

---

### System

_source line 41_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a317f67854c5856c4",
  "tool_use_id": "toolu_015fDGgMfXwTBX4qwXJq1TS4",
  "description": "Reading artifacts/_project/paper/abstract.tex",
  "usage": {
    "total_tokens": 16002,
    "tool_uses": 3,
    "duration_ms": 8570
  },
  "last_tool_name": "Read",
  "uuid": "473fa289-cda5-460b-84cc-15c588b8bd38",
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3"
}
```

---

### Tool call

_source line 42_

<details open><summary>🔧 Tool call — Read · `toolu_01WKQMF44SLL9dWUdxbpBp1H`</summary>

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
  "parent_tool_use_id": "toolu_015fDGgMfXwTBX4qwXJq1TS4",
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "c2985ea7-7fbb-4c0a-8063-4e387a4bbe19",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019frqpueWCRySd1wmTJXHcS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 402,
      "cache_read_input_tokens": 15470,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 402,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 70,
      "service_tier": "standard",
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

_source line 43 · 2026-05-14T20:43:40.386Z_

<details><summary>↩ Tool result · `toolu_01WKQMF44SLL9dWUdxbpBp1H`</summary>

```text
1	\begin{abstract}
2	Compound sparsity---simultaneously pruning attention heads and evicting KV cache entries---is essential for efficient LLM inference but produces super-additive quality degradation whose structure is poorly understood.
3	Prior work treats compound interaction magnitude as approximately constant across the generation process.
4	We show that this assumption is wrong: compound sparsity severity is an emergent phase-strategy interaction that varies by over an order of magnitude across reasoning phases.
5	
6	We evaluate compound sparsity on three models---DeepSeek-R1-Distill-Qwen-7B, Qwen2.5-7B-Instruct (both Qwen2ForCausalLM), and DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM)---spanning two architectures, using 50 MATH-500 problems, measuring the Interaction Index---a super-additivity metric---across quantile-segmented reasoning phases at sparsity levels $s \in \{0.15, 0.20, 0.25, 0.30\}$.
7	Under importance-based KV cache eviction, the median Interaction Index difference between low-sparsity and high-sparsity reasoning phases increases monotonically from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired Cohen's $d_z$ growing from $0.44$ (small) to $0.80$ (large); Bonferroni-corrected permutation tests yield $p < 0.005$ at all four sparsity levels.
8	Random eviction produces no significant phase modulation in 7/8 conditions; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) shows negligible effect size ($d_z{=}{-}0.04$), confirming that the severity gradient is strategy-specific, not an inherent property of compound sparsity.
9	At $s{=}0.25$, a crossover emerges: importance-based eviction outperforms random in high-sparsity phases ($\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$) yet underperforms in low-sparsity phases ($\widetilde{\mathrm{II}} = 7.196$ vs.\ $1.363$)---a qualitative reversal in strategy ranking.
10	The pattern replicates on Qwen2.5-7B-Instruct at $s \geq 0.20$ ($d_z \geq 0.55$; Spearman $\rho = 1.0$; gradient permutation $p = 0.043$) and on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM), where monotonically increasing $d_z$ ($0.19 \to 0.34$; $s{=}0.30$ Wilcoxon $p_{\text{Bonf}} = 0.029$) suggests cross-architecture generalization, though at ${\sim}$1/40 the absolute magnitude and with substantially weaker interaction than in Qwen2-based architectures. % exp_id: c3_llama
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
  "parent_tool_use_id": "toolu_015fDGgMfXwTBX4qwXJq1TS4",
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "75bc02c1-b4db-42ef-896a-e287eea9bc34"
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
  "task_id": "a317f67854c5856c4",
  "tool_use_id": "toolu_015fDGgMfXwTBX4qwXJq1TS4",
  "description": "Reading artifacts/_project/paper/introduction.tex",
  "usage": {
    "total_tokens": 16072,
    "tool_uses": 4,
    "duration_ms": 8947
  },
  "last_tool_name": "Read",
  "uuid": "093ec98c-0c7a-4d70-86f6-091444c5be8e",
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3"
}
```

---

### Tool call

_source line 45_

<details open><summary>🔧 Tool call — Read · `toolu_01Hk4nf3LRSegWaVm5k4KphD`</summary>

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
  "parent_tool_use_id": "toolu_015fDGgMfXwTBX4qwXJq1TS4",
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "8a1af32c-df45-4173-8897-d9ea19fb22b3",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019frqpueWCRySd1wmTJXHcS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 402,
      "cache_read_input_tokens": 15470,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 402,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 70,
      "service_tier": "standard",
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

_source line 46 · 2026-05-14T20:43:40.765Z_

<details><summary>↩ Tool result · `toolu_01Hk4nf3LRSegWaVm5k4KphD`</summary>

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
  "parent_tool_use_id": "toolu_015fDGgMfXwTBX4qwXJq1TS4",
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "ebc69c4c-ba33-4ae9-8a39-1e2a12facc82"
}
```

</details>

---

### System

_source line 47_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a317f67854c5856c4",
  "tool_use_id": "toolu_015fDGgMfXwTBX4qwXJq1TS4",
  "description": "Reading artifacts/_project/paper/methodology.tex",
  "usage": {
    "total_tokens": 16142,
    "tool_uses": 5,
    "duration_ms": 9325
  },
  "last_tool_name": "Read",
  "uuid": "f255646f-9576-40e9-aaf7-4d30e9cc4ed9",
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3"
}
```

---

### Tool call

_source line 48_

<details open><summary>🔧 Tool call — Read · `toolu_01GqGbG1JTdYw4urinDPzSz1`</summary>

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
  "parent_tool_use_id": "toolu_015fDGgMfXwTBX4qwXJq1TS4",
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "1fc56049-5431-4cac-8a71-98c85c18e74a",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019frqpueWCRySd1wmTJXHcS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 402,
      "cache_read_input_tokens": 15470,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 402,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 70,
      "service_tier": "standard",
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

_source line 49 · 2026-05-14T20:43:41.132Z_

<details><summary>↩ Tool result · `toolu_01GqGbG1JTdYw4urinDPzSz1`</summary>

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
22	All confidence intervals and significance tests use nonparametric bootstrap ($B{=}10{,}000$)~\cite{efron-1993}. Paired bootstrap controls for problem-level variance. All tests yield $p_{\text{Bonf}} < 0.005$ at every sparsity level.\footnote{Experiments on 4$\times$ NVIDIA RTX PRO 6000 Blackwell 96\,GB GPUs.}
23	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015fDGgMfXwTBX4qwXJq1TS4",
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "3df60245-d66a-4ab6-aafb-f081f778a4fd"
}
```

</details>

---

### System

_source line 50_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a317f67854c5856c4",
  "tool_use_id": "toolu_015fDGgMfXwTBX4qwXJq1TS4",
  "description": "Reading artifacts/_project/paper/results.tex",
  "usage": {
    "total_tokens": 16212,
    "tool_uses": 6,
    "duration_ms": 9652
  },
  "last_tool_name": "Read",
  "uuid": "f47a734b-5283-44ba-ad7e-f9790d79fa16",
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3"
}
```

---

### Tool call

_source line 51_

<details open><summary>🔧 Tool call — Read · `toolu_012AV9UyuQCJ9zjK7qNyqNhm`</summary>

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
  "parent_tool_use_id": "toolu_015fDGgMfXwTBX4qwXJq1TS4",
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "55e9764b-a894-419c-a110-5e179818a54e",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019frqpueWCRySd1wmTJXHcS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 402,
      "cache_read_input_tokens": 15470,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 402,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 70,
      "service_tier": "standard",
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

_source line 52 · 2026-05-14T20:43:41.464Z_

<details><summary>↩ Tool result · `toolu_012AV9UyuQCJ9zjK7qNyqNhm`</summary>

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
71	Qwen2.5-7B-Instruct (standard instruction tuning, same Qwen2 backbone) reproduces the monotonic severity gradient: $\Delta$ increases from $0.04$ at $s{=}0.15$ to $2.94$ at $s{=}0.30$, paralleling DeepSeek at ${\sim}1/5$ the magnitude. Both models yield strictly increasing $d_z$ trajectories (Spearman $\rho = 1.0$; gradient permutation $p = 0.043$). The effect is marginal at $s{=}0.15$ ($d_z{=}0.28$, CI includes zero) but reliable at $s \geq 0.20$ ($d_z \geq 0.55$). Full cross-model tables and figures appear in Appendix~\ref{app:cross-model-details}. % exp_id: cross_model_analysis.json; cohens_d_bf16_qwen.json
72	
73	
74	\subsection{Cross-Architecture Validation}
75	\label{sec:cross-arch}
76	
77	To test whether the phase-modulated severity pattern extends beyond the Qwen2 architecture, we replicate the experiment on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, 8B parameters; $n{=}49$ paired problems). Table~\ref{tab:llama-cross-arch} reports the strategy-dependent severity comparison across sparsity levels.
78	
79	The qualitative pattern replicates: importance-based eviction produces systematically larger phase-dependent severity than random eviction, with monotonically increasing paired $d_z$ ($0.19 \to 0.26 \to 0.29 \to 0.34$). At $s{=}0.30$, the Wilcoxon test reaches significance after Bonferroni correction ($p = 0.029$, $k{=}4$). At $s{=}0.15$, the median difference CI $[0.002, 0.043]$ excludes zero despite the small absolute magnitude ($\widetilde{\Delta} = 0.020$). Under importance-based eviction, the within-strategy phase gradient $d_z$ (low $-$ high) is consistently large at all sparsity levels ($d_z \in [1.00, 1.12]$), while random eviction yields only small phase gradients ($d_z \in [0.35, 0.45]$). % exp_id: c3_llama
80	
81	The absolute magnitude is architecture-dependent: LLaMA severity differences are ${\sim}40{\times}$ smaller than DeepSeek and ${\sim}7{\times}$ smaller than Qwen, and the interaction is substantially weaker---random pruning also shows a non-trivial phase gradient on LLaMA ($d_z \in [0.35, 0.45]$), reducing the strategy contrast observed in Qwen2 models. The directional pattern---monotonically increasing $d_z$, importance $>$ random, larger phase gradient under importance---is qualitatively consistent across all three models spanning two architectures (Qwen2ForCausalLM, LlamaForCausalLM), though the interaction magnitude is substantially weaker on LlamaForCausalLM. % exp_id: c3_llama; cross_model_analysis.json
82	
83	\begin{table}[t]
84	\centering
85	\small
86	\caption{Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM). $d_z$: paired Cohen's $d$ for importance vs.\ random severity; $\widetilde{\Delta}$: median paired difference with bootstrap 95\% CI ($B{=}10{,}000$); $p$: Bonferroni-corrected Wilcoxon $p$ ($k{=}4$). $n{=}49$ paired problems.}
87	\label{tab:llama-cross-arch}
88	\begin{tabular}{@{}lccc@{}}
89	\toprule
90	$s$ & $d_z$ & $\widetilde{\Delta}$\; [95\% CI] & $p_{\text{Bonf}}$ \\
91	\midrule
92	0.15 & 0.19 & 0.020\; $[0.002, 0.043]$ & 0.219 \\
93	0.20 & 0.26 & 0.022\; $[-0.090, 0.187]$ & 0.253 \\
94	0.25 & 0.29 & 0.095\; $[-0.004, 0.303]$ & 0.083 \\
95	0.30 & 0.34 & 0.356\; $[-0.069, 0.544]$ & $\mathbf{0.029}$ \\
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
  "parent_tool_use_id": "toolu_015fDGgMfXwTBX4qwXJq1TS4",
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "ef1c25ee-3638-434e-9c0d-fc4724971f40"
}
```

</details>

---

### System

_source line 53_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a317f67854c5856c4",
  "tool_use_id": "toolu_015fDGgMfXwTBX4qwXJq1TS4",
  "description": "Reading artifacts/_project/paper/conclusion.tex",
  "usage": {
    "total_tokens": 23651,
    "tool_uses": 7,
    "duration_ms": 13124
  },
  "last_tool_name": "Read",
  "uuid": "bc3923da-39a4-45d5-b90a-b3010d419914",
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3"
}
```

---

### Tool call

_source line 54_

<details open><summary>🔧 Tool call — Read · `toolu_01M6m5p6Nqt7phVf6WDwQacq`</summary>

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
  "parent_tool_use_id": "toolu_015fDGgMfXwTBX4qwXJq1TS4",
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "84694343-fa18-48e8-9a53-d9d68f45db9e",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RFPfAhu3HQUGDZH1XbuzXx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7402,
      "cache_read_input_tokens": 15872,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7402,
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

_source line 55 · 2026-05-14T20:43:44.931Z_

<details><summary>↩ Tool result · `toolu_01M6m5p6Nqt7phVf6WDwQacq`</summary>

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
  "parent_tool_use_id": "toolu_015fDGgMfXwTBX4qwXJq1TS4",
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "edfbeab8-6b14-4377-a777-7c079aaf8637"
}
```

</details>

---

### System

_source line 56_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a317f67854c5856c4",
  "tool_use_id": "toolu_015fDGgMfXwTBX4qwXJq1TS4",
  "description": "Reading artifacts/_project/paper/discussion.tex",
  "usage": {
    "total_tokens": 23688,
    "tool_uses": 8,
    "duration_ms": 13523
  },
  "last_tool_name": "Read",
  "uuid": "c8303d74-14e9-4eb3-a69f-3a5ad7772a3e",
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3"
}
```

---

### Tool call

_source line 57_

<details open><summary>🔧 Tool call — Read · `toolu_0177TRkdLyJfHqUSMRgGQV6a`</summary>

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
  "parent_tool_use_id": "toolu_015fDGgMfXwTBX4qwXJq1TS4",
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "3b83dc11-3e66-4a96-85d1-20d0b078ce50",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RFPfAhu3HQUGDZH1XbuzXx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7402,
      "cache_read_input_tokens": 15872,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7402,
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

_source line 58 · 2026-05-14T20:43:45.334Z_

<details><summary>↩ Tool result · `toolu_0177TRkdLyJfHqUSMRgGQV6a`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Quantitative surprise.}
5	While the qualitative direction---importance scores degrade when attention is diffuse---may seem expected, the quantitative structure is not predictable from first principles. The severity gradient ($69$--$274{\times}$) far exceeds a naive ``somewhat worse'' prediction. The crossover---where importance-based eviction simultaneously outperforms random in high-sparsity phases ($\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$) and underperforms in low-sparsity phases ($7.196$ vs.\ $1.363$)---cannot be derived from single-axis entropy reasoning. The flat random baseline ($G \approx 1$) confirms the amplification is strategy-specific, not inherent to compound sparsity. % exp_id: bf16_importance_s015..s030, bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json
6	
7	\paragraph{Implications for deployment.}
8	Applying a uniform compression budget across all inference steps implicitly accepts order-of-magnitude severity penalties during low-sparsity reasoning phases. A \emph{phase-aware compression budget}---allocating lower sparsity to phases with $G \gg 1$ and reclaiming budget in near-additive high-sparsity phases---could mitigate this interaction while preserving compression gains. The severity gradient provides a natural signal for such allocation. Discrimination collapse depends on attention-mass-based importance scoring shared by major KV cache methods (H$_2$O \cite{h2o-neurips2023}, SnapKV \cite{snapkv-neurips2024}, PyramidKV \cite{pyramidkv-2024}), suggesting broad applicability. Extended discussion in Appendix~\ref{app:extended-discussion}.
9	
10	\paragraph{Architecture-dependent magnitude.}
11	Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM) provides partial support for the qualitative pattern---monotonically increasing severity gradient under importance-based eviction with within-strategy phase gradient $d_z \geq 1.0$---while revealing that absolute severity magnitudes are architecture-dependent (${\sim}40{\times}$ smaller than DeepSeek, ${\sim}7{\times}$ smaller than Qwen) and the strategy--phase interaction is substantially weaker than in Qwen2-based architectures. Notably, random pruning also exhibits a non-trivial phase gradient on LLaMA ($d_z \in [0.35, 0.45]$), reducing the contrast between strategies. This dissociation between qualitatively consistent directional trends and markedly different magnitudes suggests the phase-strategy interaction may be a general property of compound sparsity on reasoning models, while its quantitative impact---and the degree to which it is strategy-specific---depends on architecture-specific attention distributions and head specialization patterns. % exp_id: c3_llama
12	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015fDGgMfXwTBX4qwXJq1TS4",
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "01acff53-3f5d-40ea-8666-7196cd263ed7"
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
  "task_id": "a317f67854c5856c4",
  "tool_use_id": "toolu_015fDGgMfXwTBX4qwXJq1TS4",
  "description": "Reading artifacts/_project/paper/analysis.tex",
  "usage": {
    "total_tokens": 23725,
    "tool_uses": 9,
    "duration_ms": 14871
  },
  "last_tool_name": "Read",
  "uuid": "507c3a07-cb76-4d0e-b4dd-a7a9b7c13218",
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3"
}
```

---

### Tool call

_source line 60_

<details open><summary>🔧 Tool call — Read · `toolu_01CjSqdW1PRbYQdJcy6UfhuB`</summary>

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
  "parent_tool_use_id": "toolu_015fDGgMfXwTBX4qwXJq1TS4",
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "f823a73c-9347-4336-98ce-cdcf526683bd",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RFPfAhu3HQUGDZH1XbuzXx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7402,
      "cache_read_input_tokens": 15872,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7402,
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

_source line 61 · 2026-05-14T20:43:46.679Z_

<details><summary>↩ Tool result · `toolu_01CjSqdW1PRbYQdJcy6UfhuB`</summary>

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
  "parent_tool_use_id": "toolu_015fDGgMfXwTBX4qwXJq1TS4",
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "dd4c1922-e2a2-4709-949d-483793c0cf05"
}
```

</details>

---

### System

_source line 62_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a317f67854c5856c4",
  "tool_use_id": "toolu_015fDGgMfXwTBX4qwXJq1TS4",
  "description": "Reading artifacts/_project/paper/limitations.tex",
  "usage": {
    "total_tokens": 23762,
    "tool_uses": 10,
    "duration_ms": 14895
  },
  "last_tool_name": "Read",
  "uuid": "c64523e7-dba8-4283-b1db-791deab4f490",
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3"
}
```

---

### Tool call

_source line 63_

<details open><summary>🔧 Tool call — Read · `toolu_01JNDRpUhS3YA2a3Ur7Gb6Li`</summary>

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
  "parent_tool_use_id": "toolu_015fDGgMfXwTBX4qwXJq1TS4",
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "11c86278-69e1-49a2-8762-640dddef644f",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RFPfAhu3HQUGDZH1XbuzXx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7402,
      "cache_read_input_tokens": 15872,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7402,
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

_source line 64 · 2026-05-14T20:43:46.714Z_

<details><summary>↩ Tool result · `toolu_01JNDRpUhS3YA2a3Ur7Gb6Li`</summary>

```text
1	\paragraph{Model scale and architecture.}
2	All experiments are conducted at the 7B parameter scale. Whether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested. Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \S\ref{sec:cross-arch}) partially extends the findings beyond the Qwen2 architecture: the directional pattern is qualitatively consistent but the interaction magnitude is substantially weaker and random pruning also exhibits a non-trivial phase gradient on LLaMA. The qualitative pattern has been tested on only two architecture families at the 7--8B scale; further validation on larger models and more diverse architectures (e.g., Mistral, multi-latent attention) is needed.
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
  "parent_tool_use_id": "toolu_015fDGgMfXwTBX4qwXJq1TS4",
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "db431ff6-f74a-4663-ae52-2e334357dfd7"
}
```

</details>

---

### System

_source line 65_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a317f67854c5856c4",
  "tool_use_id": "toolu_015fDGgMfXwTBX4qwXJq1TS4",
  "description": "Reading artifacts/_project/paper/appendix_moved.tex",
  "usage": {
    "total_tokens": 26266,
    "tool_uses": 11,
    "duration_ms": 18166
  },
  "last_tool_name": "Read",
  "uuid": "b536d282-e2f1-4cad-98e0-c659ef489cf6",
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3"
}
```

---

### Tool call

_source line 66_

<details open><summary>🔧 Tool call — Read · `toolu_01GkMiqcxxhqRfUcxrfU8WH9`</summary>

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
  "parent_tool_use_id": "toolu_015fDGgMfXwTBX4qwXJq1TS4",
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "7afd4185-d41b-4ed6-b1aa-49777566aac5",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01U9hsLqqbKdLPFnJbf2K9HQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2467,
      "cache_read_input_tokens": 23274,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2467,
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

_source line 67 · 2026-05-14T20:43:49.972Z_

<details><summary>↩ Tool result · `toolu_01GkMiqcxxhqRfUcxrfU8WH9`</summary>

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
28	Table~\ref{tab:cross-model} reports the cross-model comparison. Qwen reproduces the monotonic severity gradient at ${\sim}1/5$ of DeepSeek's magnitude. Figure~\ref{fig:cross-model} visualizes this comparison. % exp_id: cross_model_analysis.json; cohens_d_bf16_qwen.json
29	
30	\begin{table}[t]
31	\centering
32	\small
33	\caption{Cross-model comparison of median compound severity difference ($\Delta$) under importance-based eviction.}
34	\label{tab:cross-model}
35	\begin{tabular}{@{}lcccc@{}}
36	\toprule
37	Model & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
38	\midrule
39	DeepSeek-R1-Distill-Qwen-7B & 0.39 & 1.48 & 7.16 & 14.59 \\ % exp_id: bf16_importance_s015..s030
40	Qwen2.5-7B-Instruct         & 0.04 & 0.23 & 1.27 & 2.94 \\ % exp_id: bf16_qw_imp_s015..s030
41	\bottomrule
42	\end{tabular}
43	\end{table}
44	
45	\begin{figure}[t]
46	\centering
47	\includegraphics[width=\columnwidth]{fig5_crossmodel.pdf}
48	\caption{Cross-model comparison of the median severity difference under importance-based eviction. Both DeepSeek (solid) and Qwen (dashed) exhibit monotonically increasing $\Delta$ with sparsity; Qwen's magnitude is approximately one-fifth of DeepSeek's.} % exp_id: bf16_importance_s015..s030, bf16_qw_imp_s015..s030
49	\label{fig:cross-model}
50	\end{figure}
51	
52	\paragraph{Per-problem concordance.}
53	The per-problem concordance across models is not significant (mean $\rho = -0.11$, $p = 0.926$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking. % exp_id: cross_model_analysis.json (spearman_rho=1.0, gradient_permutation_p=0.043, per_problem_concordance_p=0.926, mean_rho=-0.107)
54	
55	\paragraph{Random eviction control.}
56	As a control, random eviction on Qwen yields no systematic phase gradient at three of four sparsity levels (3/4 FAIL), mirroring DeepSeek's 4/4 FAIL pattern. At $s{=}0.30$, Qwen random produces a borderline PASS (permutation $p = 0.012$) but with negligible effect size ($d_z = -0.04$, CI spans zero), indicating no meaningful phase modulation. % exp_id: bf16_qw_rand_s015..s030; source: experiment_summary_table.json
57	
58	
59	\section{Permutation Test Details}
60	\label{app:permutation-details}
61	
62	For each problem $i$ and sparsity level $s$, we compute the compound severity difference $\Delta_i^{(\text{strat})} = \mathrm{II}_{\textit{low},i} - \mathrm{II}_{\textit{high},i}$ under each eviction strategy. The test statistic is the median of the paired difference $\widetilde{\Delta} = \text{median}_i\!\bigl(\Delta_i^{(\text{imp})} - \Delta_i^{(\text{rand})}\bigr)$, measuring whether importance-based eviction produces systematically larger phase-dependent severity than random eviction. We permute strategy labels $10{,}000$ times to construct the null distribution and apply Bonferroni correction for 4 sparsity-level comparisons.
63	
64	Per-problem distributions of the paired severity difference $\Delta_i = \mathrm{II}_{\textit{low},i} - \mathrm{II}_{\textit{high},i}$ under importance-based eviction are right-skewed at all sparsity levels, with mean/median ratios ranging from $1.2{\times}$ ($s{=}0.15$) to $1.6{\times}$ ($s{=}0.30$) for DeepSeek and $1.1{\times}$ to $1.4{\times}$ for Qwen.
65	
66	The permutation null distributions are approximately symmetric around zero at all sparsity levels. At $s{=}0.15$, the observed statistic falls at the $99.92$th percentile of the null ($p_{\text{Bonf}} = 0.0032$); at $s \geq 0.20$, no permutation exceeds the observed statistic.
67	
68	Table~\ref{tab:permutation} reports the results. All four sparsity levels reject $H_0$ after Bonferroni correction ($p_{\text{Bonf}} < 0.005$), with observed median differences increasing monotonically from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$. The monotonic growth of both the point estimate and the CI lower bound ($0.19 \to 0.69 \to 1.66 \to 6.70$) confirms that compound severity amplification strengthens with sparsity---not merely in central tendency but also in worst-case lower bounds. Figure~\ref{fig:permtest-forest} presents these results as a forest plot. % exp_id: deepseek_bf16_permtest; source: permutation_test_results.json
69	
70	\begin{table}[t]
71	\centering
72	\small
73	\caption{Paired permutation test for compound severity: importance vs.\ random eviction on DeepSeek-R1-Distill-Qwen-7B ($n{=}49$, $10{,}000$ permutations, Bonferroni-corrected).}
74	\label{tab:permutation}
75	\begin{tabular}{@{}rrcl@{}}
76	\toprule
77	$s$ & Observed $\widetilde{\Delta}$ & 95\% CI & $p_{\text{Bonf}}$ \\
78	\midrule
79	0.15 & 0.37 & $[0.19,\; 0.62]$ & 0.0032 \\ % exp_id: deepseek_bf16_permtest_s015
80	0.20 & 0.97 & $[0.69,\; 1.49]$ & ${<}\,0.001$ \\ % exp_id: deepseek_bf16_permtest_s020
81	0.25 & 3.34 & $[1.66,\; 6.64]$ & ${<}\,0.001$ \\ % exp_id: deepseek_bf16_permtest_s025
82	0.30 & 9.85 & $[6.70,\; 16.29]$ & ${<}\,0.001$ \\ % exp_id: deepseek_bf16_permtest_s030
83	\bottomrule
84	\end{tabular}
85	\end{table}
86	
87	\begin{figure}[t]
88	\centering
89	\includegraphics[width=\columnwidth]{fig4_bootstrap.pdf}
90	\caption{Forest plot of permutation test results. Horizontal bars show 95\% permutation CIs; diamonds mark observed median differences $\widetilde{\Delta}$. All CIs lie entirely above zero, confirming significant strategy-dependent severity at every sparsity level.}
91	\label{fig:permtest-forest}
92	\end{figure}
93	
94	
95	\section{Analysis: Entropy-Discrimination Collapse}
96	\label{app:analysis}
97	
98	\subsection{Discrimination Collapse}
99	\label{sec:discrimination-collapse}
100	
101	Head pruning reduces the number of heads contributing to cumulative importance scores, flattening the score distribution. Table~\ref{tab:discrimination-metrics-full} quantifies this effect: the Gini coefficient decreases by $0.030$--$0.081$ (DeepSeek) and $0.010$--$0.020$ (Qwen) after pruning, with consistent negative deltas across all 16 conditions (both models $\times$ 4 sparsity levels $\times$ 2 strategies). The CV delta is likewise negative in all 8 importance-based conditions. The same pattern holds under random eviction, confirming that discrimination collapse is a consequence of head pruning \emph{per se}, not of the eviction strategy. % exp_id: c4_entropy_deepseek, c4_entropy_qwen
102	
103	\begin{table}[t]
104	\centering
105	\caption{Discrimination collapse under importance-based eviction. $\Delta\mathrm{Gini}$ and $\Delta\mathrm{CV}$ are post-pruning minus baseline; negative values indicate reduced discriminative power.}
106	\label{tab:discrimination-metrics-full}
107	\small
108	\begin{tabular}{llrr}
109	\toprule
110	Model & $s$ & $\Delta\mathrm{Gini}$ & $\Delta\mathrm{CV}$ \\
111	\midrule
112	DeepSeek & $0.15$ & $-0.030$ & $-0.56$ \\
113	DeepSeek & $0.20$ & $-0.040$ & $-0.77$ \\
114	DeepSeek & $0.25$ & $-0.065$ & $-1.29$ \\
115	DeepSeek & $0.30$ & $-0.081$ & $-1.66$ \\
116	\midrule
117	Qwen & $0.15$ & $-0.010$ & $-0.05$ \\
118	Qwen & $0.20$ & $-0.012$ & $-0.21$ \\
119	Qwen & $0.25$ & $-0.010$ & $-1.49$ \\
120	Qwen & $0.30$ & $-0.020$ & $-1.14$ \\
121	\bottomrule
122	\end{tabular}
123	\end{table}
124	
125	When importance scores lose discriminability, thresholding degenerates into noise-sensitive selection---functionally approaching biased random eviction. This is phase-dependent: in low-sparsity phases, attention is already broadly distributed, so pruning-induced flattening has maximum impact; in high-sparsity phases, concentration is preserved. Random eviction is immune because its decisions are independent of score quality, explaining $G \approx 1$. % exp_id: c4_entropy_deepseek, c4_entropy_qwen
126	
127	\subsection{Entropy Redistribution}
128	\label{sec:entropy-redistribution}
129	
130	Beyond discrimination collapse, we examine whether head pruning also redistributes the attention entropy of surviving heads. We measure the mean attention entropy per head:
131	\begin{equation}
132	    \mathcal{H}_i^{(h)} = -\sum_{j=1}^{T} a_{ij}^{(h)} \log a_{ij}^{(h)}
133	    \label{eq:attn-entropy}
134	\end{equation}
135	and compute $\Delta\mathcal{H}$ as the change from baseline (no pruning) to the pruned condition.
136	
137	For DeepSeek under importance-based eviction, the entropy delta is consistently negative across all four sparsity levels ($\Delta\mathcal{H} \in [-0.047, -0.040]$; Table~\ref{tab:entropy-deltas}), indicating that importance-based pruning systematically selects heads whose removal concentrates attention in the surviving heads, reinforcing discrimination collapse. % exp_id: c4_entropy_deepseek
138	
139	For Qwen, the entropy pattern only partially replicates. The delta is negative at $s{=}0.15$ ($\Delta\mathcal{H} = -0.073$) and $s{=}0.20$ ($-0.076$), consistent with DeepSeek. However, at $s{=}0.25$, the delta reverses to $+0.045$, with 22 of 30 problems showing positive entropy change. At $s{=}0.30$, the delta is near zero ($-0.007$). The $s{=}0.25$ reversal is systematic rather than a statistical artifact: it is consistent across all three reasoning phases (low: $+0.042$, mid: $+0.034$, high: $+0.017$). We interpret this as a genuine model-specific difference, possibly arising from distinct head specialization patterns: Qwen's instruction tuning (vs.\ DeepSeek's distillation-based training) may produce head configurations where removing 25\% of heads triggers compensatory broadening rather than concentration. % exp_id: c4_entropy_qwen
140	
141	We characterize discrimination collapse as the robust, model-independent driver of the phase-strategy interaction, with entropy redistribution as a secondary amplifier that is consistent in DeepSeek but model-dependent in Qwen.
142	
143	\begin{table}[t]
144	\centering
145	\caption{Attention entropy deltas ($\Delta\mathcal{H}$) under importance-based eviction. DeepSeek shows consistent entropy compression; Qwen partially replicates with a reversal at $s{=}0.25$.}
146	\label{tab:entropy-deltas}
147	\small
148	\begin{tabular}{llr}
149	\toprule
150	Model & $s$ & $\Delta\mathcal{H}$ \\
151	\midrule
152	DeepSeek & $0.15$ & $-0.040$ \\
153	DeepSeek & $0.20$ & $-0.047$ \\
154	DeepSeek & $0.25$ & $-0.045$ \\
155	DeepSeek & $0.30$ & $-0.044$ \\
156	\midrule
157	Qwen & $0.15$ & $-0.073$ \\
158	Qwen & $0.20$ & $-0.076$ \\
159	Qwen & $0.25$ & $+0.045$ \\
160	Qwen & $0.30$ & $-0.007$ \\
161	\bottomrule
162	\end{tabular}
163	\end{table}
164	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015fDGgMfXwTBX4qwXJq1TS4",
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "72cbd9be-8a44-4cc2-9e80-fbe86b664175"
}
```

</details>

---

### System

_source line 68_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a317f67854c5856c4",
  "tool_use_id": "toolu_015fDGgMfXwTBX4qwXJq1TS4",
  "description": "Reading artifacts/_project/paper/appendix_disc_analysis.tex",
  "usage": {
    "total_tokens": 26303,
    "tool_uses": 12,
    "duration_ms": 18745
  },
  "last_tool_name": "Read",
  "uuid": "fd17ecab-cdf5-4f2a-8d96-8c2b00dff035",
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3"
}
```

---

### Tool call

_source line 69_

<details open><summary>🔧 Tool call — Read · `toolu_018jFcwdsaL2W7hUKeUnLLYc`</summary>

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
  "parent_tool_use_id": "toolu_015fDGgMfXwTBX4qwXJq1TS4",
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "90a02c03-46bd-4af3-a23f-8397ac0ff1cf",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01U9hsLqqbKdLPFnJbf2K9HQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2467,
      "cache_read_input_tokens": 23274,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2467,
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

_source line 70 · 2026-05-14T20:43:50.551Z_

<details><summary>↩ Tool result · `toolu_018jFcwdsaL2W7hUKeUnLLYc`</summary>

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
14	Random eviction fails 7/8 paired permutation tests across both models; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) exhibits negligible effect size ($d_z{=}{-}0.04$). The absence of a phase gradient under random masking isolates the amplification as strategy-specific. % exp_id: bf16_ds_rand_s015..s030, bf16_qw_rand_s015..s030
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
33	Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \S\ref{sec:cross-arch}) provides partial support: the directional pattern is qualitatively consistent but the interaction magnitude is substantially weaker than in Qwen2-based architectures, and random pruning also exhibits a non-trivial phase gradient on LLaMA. Further validation on more diverse architectures (e.g., Mistral, multi-latent attention architectures) is needed to establish the generality of the full interaction.
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
45	Bootstrap confidence intervals use $B{=}10{,}000$ resamples. The paired permutation test yields $n{=}49$ paired problems for DeepSeek (1 excluded) and $n{=}46$ for Qwen (4 excluded). % exp_id: cohens_d_bf16.json, cohens_d_bf16_qwen.json
46	The severity difference distribution is right-skewed (mean/median ratio ${\sim}1.6{:}1$ at $s{=}0.30$), motivating our use of medians and nonparametric tests rather than parametric alternatives. % exp_id: bf16_importance_s030; mean_diff=22.94, median_diff=14.59 (segment-level). Per-problem paired: median_diff=9.9436 at s030
47	All four permutation tests reject $H_0$ after Bonferroni correction ($p_{\text{Bonf}} < 0.005$; Table~\ref{tab:permutation}), with CI lower bounds increasing from $0.19$ to $6.70$---confirming the effect direction at every sparsity level. The permutation CIs at higher sparsity are wider (e.g., $[6.70,\; 16.29]$ at $s{=}0.30$), reflecting genuine variance in per-problem severity amplification. % exp_id: permutation_test_results.json; permutation CIs: s015=[0.19,0.62], s020=[0.69,1.49], s025=[1.66,6.64], s030=[6.70,16.29]
48	
49	A notable exception among the random baselines is the Qwen random condition at $s{=}0.30$, which yields a statistically significant result ($p{=}0.012$) despite negligible effect size ($d_z{=}{-}0.04$, bootstrap CI excluding zero). % exp_id: qw_rand_s030; B=10000, p=0.012, d=-0.035, negligible
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
  "parent_tool_use_id": "toolu_015fDGgMfXwTBX4qwXJq1TS4",
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "b38b3d92-4bda-43db-85b4-7a641e3a7c0b"
}
```

</details>

---

### System

_source line 71_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a317f67854c5856c4",
  "tool_use_id": "toolu_015fDGgMfXwTBX4qwXJq1TS4",
  "description": "Reading artifacts/_project/paper/appendix_results.tex",
  "usage": {
    "total_tokens": 33678,
    "tool_uses": 13,
    "duration_ms": 22353
  },
  "last_tool_name": "Read",
  "uuid": "93a51de2-e64e-4538-8d7e-926545710201",
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3"
}
```

---

### Tool call

_source line 72_

<details open><summary>🔧 Tool call — Read · `toolu_014Dn4vmgXmCLj1UFjLYgPx9`</summary>

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
  "parent_tool_use_id": "toolu_015fDGgMfXwTBX4qwXJq1TS4",
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "db0eb519-8658-46c6-8cd8-36e919096f06",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01CUE9mAEfKWxkX2LC2CDgQX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7338,
      "cache_read_input_tokens": 25741,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7338,
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

_source line 73 · 2026-05-14T20:43:54.192Z_

<details><summary>↩ Tool result · `toolu_014Dn4vmgXmCLj1UFjLYgPx9`</summary>

```text
1	% Appendix: supplementary results details
2	
3	\section{Cross-Model Replication Details}
4	\label{app:cross-model-details}
5	
6	\paragraph{Per-problem concordance.}
7	The per-problem concordance across models is not significant (mean $\rho = -0.11$, $p = 0.926$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking. % exp_id: cross_model_analysis.json (spearman_rho=1.0, gradient_permutation_p=0.043, per_problem_concordance_p=0.926, mean_rho=-0.107)
8	
9	\paragraph{Random eviction control.}
10	As a control, random eviction on Qwen yields no systematic phase gradient at three of four sparsity levels (3/4 FAIL), mirroring DeepSeek's 4/4 FAIL pattern. At $s{=}0.30$, Qwen random produces a borderline PASS (permutation $p = 0.012$) but with negligible effect size ($d_z = -0.04$, CI spans zero), indicating no meaningful phase modulation. % exp_id: bf16_qw_rand_s015..s030; source: experiment_summary_table.json
11	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015fDGgMfXwTBX4qwXJq1TS4",
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "3e6da463-cf18-49ba-aec4-fb68b4c7b68d"
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
  "task_id": "a317f67854c5856c4",
  "tool_use_id": "toolu_015fDGgMfXwTBX4qwXJq1TS4",
  "description": "Reading artifacts/_project/paper/appendix.tex",
  "usage": {
    "total_tokens": 33715,
    "tool_uses": 14,
    "duration_ms": 22695
  },
  "last_tool_name": "Read",
  "uuid": "e8a0128f-8f51-4c7e-9fab-9a48fc3527f3",
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3"
}
```

---

### Tool call

_source line 75_

<details open><summary>🔧 Tool call — Read · `toolu_01EUm9Lk8WwUWS6xKVE1Mx3o`</summary>

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
  "parent_tool_use_id": "toolu_015fDGgMfXwTBX4qwXJq1TS4",
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "e5d50741-750b-4d48-b470-bfbe2328be79",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01CUE9mAEfKWxkX2LC2CDgQX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7338,
      "cache_read_input_tokens": 25741,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7338,
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

_source line 76 · 2026-05-14T20:43:54.500Z_

<details><summary>↩ Tool result · `toolu_01EUm9Lk8WwUWS6xKVE1Mx3o`</summary>

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
  "parent_tool_use_id": "toolu_015fDGgMfXwTBX4qwXJq1TS4",
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "f91cb695-3394-41fd-a61a-43b41edb325f"
}
```

</details>

---

### System

_source line 77_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a317f67854c5856c4",
  "tool_use_id": "toolu_015fDGgMfXwTBX4qwXJq1TS4",
  "description": "Running Search for all specified patterns in all files",
  "usage": {
    "total_tokens": 35482,
    "tool_uses": 15,
    "duration_ms": 29401
  },
  "last_tool_name": "Bash",
  "uuid": "4a897393-9c83-446d-a5d3-674b52312010",
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3"
}
```

---

### Tool call

_source line 78_

<details open><summary>🔧 Tool call — Bash · `toolu_012guBJSsfkatmvXYo1RdNpH`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper\nfor f in abstract.tex introduction.tex methodology.tex results.tex conclusion.tex discussion.tex analysis.tex appendix_moved.tex appendix_disc_analysis.tex appendix_results.tex appendix.tex limitations.tex; do\n  echo \"=== $f ===\"\n  grep -nE '50|0\\.32|1\\.15|3\\.97|9\\.94|0\\.048|0\\.208|1\\.109|2\\.619|0\\.44|0\\.80|0\\.28|1\\.02|14\\.59|0\\.39|7\\.16|69|274|7/8|qualitative|n=500|C5b|C8|LLaMA|Llama|future work' \"$f\"\n  echo \"\"\ndone",
  "description": "Search for all specified patterns in all files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015fDGgMfXwTBX4qwXJq1TS4",
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "14e7e922-aadf-4b0b-abca-4ca1c4402ad9",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01NDGrQZkJhX8KXGz52tT99k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1765,
      "cache_read_input_tokens": 33079,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1765,
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

_source line 79 · 2026-05-14T20:44:01.333Z_

<details><summary>↩ Tool result · `toolu_012guBJSsfkatmvXYo1RdNpH`</summary>

```text
=== abstract.tex ===
6:We evaluate compound sparsity on three models---DeepSeek-R1-Distill-Qwen-7B, Qwen2.5-7B-Instruct (both Qwen2ForCausalLM), and DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM)---spanning two architectures, using 50 MATH-500 problems, measuring the Interaction Index---a super-additivity metric---across quantile-segmented reasoning phases at sparsity levels $s \in \{0.15, 0.20, 0.25, 0.30\}$.
7:Under importance-based KV cache eviction, the median Interaction Index difference between low-sparsity and high-sparsity reasoning phases increases monotonically from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired Cohen's $d_z$ growing from $0.44$ (small) to $0.80$ (large); Bonferroni-corrected permutation tests yield $p < 0.005$ at all four sparsity levels.
8:Random eviction produces no significant phase modulation in 7/8 conditions; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) shows negligible effect size ($d_z{=}{-}0.04$), confirming that the severity gradient is strategy-specific, not an inherent property of compound sparsity.
9:At $s{=}0.25$, a crossover emerges: importance-based eviction outperforms random in high-sparsity phases ($\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$) yet underperforms in low-sparsity phases ($\widetilde{\mathrm{II}} = 7.196$ vs.\ $1.363$)---a qualitative reversal in strategy ranking.
10:The pattern replicates on Qwen2.5-7B-Instruct at $s \geq 0.20$ ($d_z \geq 0.55$; Spearman $\rho = 1.0$; gradient permutation $p = 0.043$) and on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM), where monotonically increasing $d_z$ ($0.19 \to 0.34$; $s{=}0.30$ Wilcoxon $p_{\text{Bonf}} = 0.029$) suggests cross-architecture generalization, though at ${\sim}$1/40 the absolute magnitude and with substantially weaker interaction than in Qwen2-based architectures. % exp_id: c3_llama

=== introduction.tex ===
14:On DeepSeek-R1-Distill-Qwen-7B, the median phase difference rises from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$ ($d_z$: $0.44 \to 0.80$; Bonferroni-corrected $p < 0.005$ at all levels).
15:The pattern replicates at $s \geq 0.20$ on Qwen2.5-7B-Instruct ($d_z \geq 0.55$) and partially extends to a distinct architecture (DeepSeek-R1-Distill-Llama-8B, LlamaForCausalLM) with a qualitatively consistent but substantially weaker trend at $\sim$1/40 the magnitude.
16:Critically, random eviction produces no such gradient (7/8 conditions non-significant), confirming the gradient is an emergent phase-strategy interaction.

=== methodology.tex ===
10:We use 50 problems stratified from MATH-500~\cite{math500-neurips2021}, sampling uniformly across categories with a fixed seed. Each problem is decoded greedily (\texttt{max\_new\_tokens}$=$2048).

=== results.tex ===
8:Table~\ref{tab:aggregate-ii} reports the median compound severity difference across strategies and sparsity levels. Under importance-based eviction, $\Delta$ increases from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$---a $37{\times}$ amplification. Under random eviction, no systematic growth is observed ($-0.02$ to $1.54$), confirming that compound severity depends qualitatively on eviction strategy. % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json
13:\caption{Median compound severity difference ($\Delta = \widetilde{\mathrm{II}}_{\textit{low}} - \widetilde{\mathrm{II}}_{\textit{high}}$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}50$ MATH-500 problems).}
19:Importance & 0.39 & 1.48 & 7.16 & 14.59 \\ % exp_id: bf16_importance_s015..s030; source: experiment_summary_table.json median_diff
29:Decomposing II by reasoning phase reveals that strategy-dependent severity is driven by amplification in the low-sparsity phase. Table~\ref{tab:main-results} reports the full per-phase breakdown. The severity gradient $G$ increases from $69{\times}$ at $s{=}0.15$ to $274{\times}$ at $s{=}0.30$ under importance-based eviction, while the high-sparsity phase experiences near-zero interaction ($\widetilde{\mathrm{II}}_{\textit{high}}$ ranges from $0.006$ to $0.053$). Under random eviction, $G \approx 0.9$--$1.7{\times}$ at all sparsity levels. Figure~\ref{fig:hero} visualizes this contrast. % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json
34:\caption{Interaction index (II) by eviction strategy, reasoning phase, and sparsity level. II values are problem-level medians across 50 problems. $\Delta = \widetilde{\mathrm{II}}_{\textit{low}} - \widetilde{\mathrm{II}}_{\textit{high}}$. $G = \widetilde{\mathrm{II}}_{\textit{low}} / \widetilde{\mathrm{II}}_{\textit{high}}$.}
40:0.15 & Importance & 0.006 & 0.081 & 0.398 & 0.39 & $\mathbf{69}$ \\
44:0.20 & Random     & 0.292 & 0.350 & 0.276 & $-$0.02 & 0.9 \\
46:0.25 & Importance & 0.032 & 1.118 & 7.196 & 7.16 & $\mathbf{222}$ \\
49:0.30 & Importance & 0.053 & 2.283 & 14.639 & 14.59 & $\mathbf{274}$ \\
50:0.30 & Random     & 2.503 & 2.592 & 4.041 & 1.54 & 1.6 \\
58:\caption{Severity gradient ($G$) as a function of sparsity level $s$. Importance-based eviction (solid) exhibits an increasing gradient from $69{\times}$ to $274{\times}$; random eviction (dashed) remains flat near $1{\times}$. Shaded regions: 95\% bootstrap CIs.} % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030
71:Qwen2.5-7B-Instruct (standard instruction tuning, same Qwen2 backbone) reproduces the monotonic severity gradient: $\Delta$ increases from $0.04$ at $s{=}0.15$ to $2.94$ at $s{=}0.30$, paralleling DeepSeek at ${\sim}1/5$ the magnitude. Both models yield strictly increasing $d_z$ trajectories (Spearman $\rho = 1.0$; gradient permutation $p = 0.043$). The effect is marginal at $s{=}0.15$ ($d_z{=}0.28$, CI includes zero) but reliable at $s \geq 0.20$ ($d_z \geq 0.55$). Full cross-model tables and figures appear in Appendix~\ref{app:cross-model-details}. % exp_id: cross_model_analysis.json; cohens_d_bf16_qwen.json
77:To test whether the phase-modulated severity pattern extends beyond the Qwen2 architecture, we replicate the experiment on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, 8B parameters; $n{=}49$ paired problems). Table~\ref{tab:llama-cross-arch} reports the strategy-dependent severity comparison across sparsity levels.
79:The qualitative pattern replicates: importance-based eviction produces systematically larger phase-dependent severity than random eviction, with monotonically increasing paired $d_z$ ($0.19 \to 0.26 \to 0.29 \to 0.34$). At $s{=}0.30$, the Wilcoxon test reaches significance after Bonferroni correction ($p = 0.029$, $k{=}4$). At $s{=}0.15$, the median difference CI $[0.002, 0.043]$ excludes zero despite the small absolute magnitude ($\widetilde{\Delta} = 0.020$). Under importance-based eviction, the within-strategy phase gradient $d_z$ (low $-$ high) is consistently large at all sparsity levels ($d_z \in [1.00, 1.12]$), while random eviction yields only small phase gradients ($d_z \in [0.35, 0.45]$). % exp_id: c3_llama
81:The absolute magnitude is architecture-dependent: LLaMA severity differences are ${\sim}40{\times}$ smaller than DeepSeek and ${\sim}7{\times}$ smaller than Qwen, and the interaction is substantially weaker---random pruning also shows a non-trivial phase gradient on LLaMA ($d_z \in [0.35, 0.45]$), reducing the strategy contrast observed in Qwen2 models. The directional pattern---monotonically increasing $d_z$, importance $>$ random, larger phase gradient under importance---is qualitatively consistent across all three models spanning two architectures (Qwen2ForCausalLM, LlamaForCausalLM), though the interaction magnitude is substantially weaker on LlamaForCausalLM. % exp_id: c3_llama; cross_model_analysis.json
86:\caption{Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM). $d_z$: paired Cohen's $d$ for importance vs.\ random severity; $\widetilde{\Delta}$: median paired difference with bootstrap 95\% CI ($B{=}10{,}000$); $p$: Bonferroni-corrected Wilcoxon $p$ ($k{=}4$). $n{=}49$ paired problems.}
95:0.30 & 0.34 & 0.356\; $[-0.069, 0.544]$ & $\mathbf{0.029}$ \\
106:Table~\ref{tab:cohens-d} reports paired Cohen's $d_z$ for both models. For DeepSeek, effect sizes grow from $d_z{=}0.44$ (small) to $d_z{=}0.80$ (large). For Qwen, the effect is marginal at $s{=}0.15$ ($d_z{=}0.28$, CI includes zero), becoming reliable at $s \geq 0.20$ ($d_z \geq 0.55$). At $s \geq 0.25$, Qwen exhibits larger standardized effect sizes ($d_z{=}0.89$/$1.02$ vs.\ $0.68$/$0.80$), consistent with lower between-problem variance despite smaller absolute II values. % exp_id: cohens_d_bf16.json; cohens_d_bf16_qwen.json
117:0.15 & 0.44 & 0.32\; $[0.20, 0.47]$ & 0.28 & 0.05\; $[-0.01, 0.11]$\textsuperscript{ns} \\ % exp_id: bf16_ds_imp_s015, bf16_qw_imp_s015
118:0.20 & 0.52 & 1.15\; $[0.66, 1.26]$ & 0.55 & 0.21\; $[0.07, 0.40]$ \\ % exp_id: bf16_ds_imp_s020, bf16_qw_imp_s020
119:0.25 & 0.68 & 3.97\; $[2.83, 5.29]$ & 0.89 & 1.11\; $[0.61, 1.47]$ \\ % exp_id: bf16_ds_imp_s025, bf16_qw_imp_s025
120:0.30 & 0.80 & 9.94\; $[8.39, 16.65]$ & 1.02 & 2.62\; $[1.72, 3.65]$ \\ % exp_id: bf16_ds_imp_s030, bf16_qw_imp_s030

=== conclusion.tex ===
4:We showed that compound sparsity severity---the super-additive interaction between head pruning and KV cache eviction---is not phase-invariant but exhibits an emergent phase-strategy interaction spanning over an order of magnitude within a single generation. Under importance-based eviction, the severity gradient grows from $69{\times}$ to $274{\times}$ across sparsity levels ($d_z$: $0.44 \to 0.80$); random eviction shows no such modulation (7/8 conditions non-significant). A crossover at $s{=}0.25$---where importance-based eviction reverses ranking across phases---demonstrates that no single strategy dominates uniformly. The pattern replicates on Qwen2.5-7B-Instruct at $s \geq 0.20$ ($d_z \geq 0.55$) and partially extends cross-architecture to DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM) with a qualitatively consistent but substantially weaker trend at $\sim$1/40 the magnitude. Discrimination collapse provides a mechanistic explanation supported by both Qwen2-based models; LLaMA results are directionally consistent but the interaction is weaker than in Qwen2 architectures.

=== discussion.tex ===
5:While the qualitative direction---importance scores degrade when attention is diffuse---may seem expected, the quantitative structure is not predictable from first principles. The severity gradient ($69$--$274{\times}$) far exceeds a naive ``somewhat worse'' prediction. The crossover---where importance-based eviction simultaneously outperforms random in high-sparsity phases ($\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$) and underperforms in low-sparsity phases ($7.196$ vs.\ $1.363$)---cannot be derived from single-axis entropy reasoning. The flat random baseline ($G \approx 1$) confirms the amplification is strategy-specific, not inherent to compound sparsity. % exp_id: bf16_importance_s015..s030, bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json
11:Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM) provides partial support for the qualitative pattern---monotonically increasing severity gradient under importance-based eviction with within-strategy phase gradient $d_z \geq 1.0$---while revealing that absolute severity magnitudes are architecture-dependent (${\sim}40{\times}$ smaller than DeepSeek, ${\sim}7{\times}$ smaller than Qwen) and the strategy--phase interaction is substantially weaker than in Qwen2-based architectures. Notably, random pruning also exhibits a non-trivial phase gradient on LLaMA ($d_z \in [0.35, 0.45]$), reducing the contrast between strategies. This dissociation between qualitatively consistent directional trends and markedly different magnitudes suggests the phase-strategy interaction may be a general property of compound sparsity on reasoning models, while its quantitative impact---and the degree to which it is strategy-specific---depends on architecture-specific attention distributions and head specialization patterns. % exp_id: c3_llama

=== analysis.tex ===

=== appendix_moved.tex ===
26:Despite lacking explicit \texttt{&lt;think>} delimiters, Qwen2.5-7B-Instruct exhibits sufficient variation in attention sparsity to permit phase segmentation via the same quantile-based method (\S\ref{sec:phase-segmentation}). Four of the 50 problems are excluded due to degenerate phase assignments, yielding $n{=}46$ valid problems for Qwen (vs.\ $n{=}49$ for DeepSeek).
39:DeepSeek-R1-Distill-Qwen-7B & 0.39 & 1.48 & 7.16 & 14.59 \\ % exp_id: bf16_importance_s015..s030
68:Table~\ref{tab:permutation} reports the results. All four sparsity levels reject $H_0$ after Bonferroni correction ($p_{\text{Bonf}} < 0.005$), with observed median differences increasing monotonically from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$. The monotonic growth of both the point estimate and the CI lower bound ($0.19 \to 0.69 \to 1.66 \to 6.70$) confirms that compound severity amplification strengthens with sparsity---not merely in central tendency but also in worst-case lower bounds. Figure~\ref{fig:permtest-forest} presents these results as a forest plot. % exp_id: deepseek_bf16_permtest; source: permutation_test_results.json
80:0.20 & 0.97 & $[0.69,\; 1.49]$ & ${<}\,0.001$ \\ % exp_id: deepseek_bf16_permtest_s020

=== appendix_disc_analysis.tex ===
14:Random eviction fails 7/8 paired permutation tests across both models; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) exhibits negligible effect size ($d_z{=}{-}0.04$). The absence of a phase gradient under random masking isolates the amplification as strategy-specific. % exp_id: bf16_ds_rand_s015..s030, bf16_qw_rand_s015..s030
28:% REBUTTAL: 7B is the most-deployed scale for on-device and cost-constrained serving—exactly where compound sparsity is needed. The mechanism (entropy-discrimination collapse) is scale-agnostic in principle. Scaling experiments are future work.
33:Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \S\ref{sec:cross-arch}) provides partial support: the directional pattern is qualitatively consistent but the interaction magnitude is substantially weaker than in Qwen2-based architectures, and random pruning also exhibits a non-trivial phase gradient on LLaMA. Further validation on more diverse architectures (e.g., Mistral, multi-latent attention architectures) is needed to establish the generality of the full interaction.
35:% REBUTTAL: We now include cross-architecture validation on LlamaForCausalLM (\S\ref{sec:cross-arch}), which shows a qualitatively consistent but substantially weaker pattern. We use qualified language ("partially supports") rather than claiming full generalization.
38:We evaluate exclusively on MATH-500, a mathematical reasoning benchmark.
41:% REVIEWER-ATTACK: "Only MATH-500. How do we know this isn't a math-specific artifact?"
42:% REBUTTAL: The mechanism (entropy-discrimination collapse under head pruning) depends on attention distribution properties, not math-specific features. MATH-500 is a standard benchmark with diverse difficulty. However, different reasoning tasks may induce different phase structures—we state this limitation explicitly rather than overclaiming.
46:The severity difference distribution is right-skewed (mean/median ratio ${\sim}1.6{:}1$ at $s{=}0.30$), motivating our use of medians and nonparametric tests rather than parametric alternatives. % exp_id: bf16_importance_s030; mean_diff=22.94, median_diff=14.59 (segment-level). Per-problem paired: median_diff=9.9436 at s030
47:All four permutation tests reject $H_0$ after Bonferroni correction ($p_{\text{Bonf}} < 0.005$; Table~\ref{tab:permutation}), with CI lower bounds increasing from $0.19$ to $6.70$---confirming the effect direction at every sparsity level. The permutation CIs at higher sparsity are wider (e.g., $[6.70,\; 16.29]$ at $s{=}0.30$), reflecting genuine variance in per-problem severity amplification. % exp_id: permutation_test_results.json; permutation CIs: s015=[0.19,0.62], s020=[0.69,1.49], s025=[1.66,6.64], s030=[6.70,16.29]
54:More extreme sparsity ($s > 0.50$) may exhibit qualitatively different interaction dynamics---the sub-exponential growth pattern suggests the severity gradient may plateau, but this remains unverified.
57:% REBUTTAL: Our focus is on the practically relevant regime where models retain usable quality. At s>0.30 both strategies degrade severely, making II measurement less informative. The sub-exponential growth (C6, $\Delta$ growth rate $3.8{\times} \to 4.8{\times} \to 2.0{\times}$) suggests saturation at higher sparsity, but confirming this is future work.
62:% REBUTTAL: This is an empirical finding paper, not a method/system paper. The contribution is characterizing *what happens* (phase-modulated severity) and *why* (entropy-discrimination collapse), not building a system to fix it. Phase-gated controllers are explicitly scoped as future work. The finding is actionable regardless: any compound sparsity deployment should be aware of phase-dependent severity.

=== appendix_results.tex ===

=== appendix.tex ===
38:We verified that replacing the additive null $r_b = r_a + r_k - 1$ (Eq.~\ref{eq:ii}) with the multiplicative null $r_b = r_a \cdot r_k$ does not change qualitative conclusions. Under the multiplicative formulation, the interaction index becomes $\mathrm{II}_{\times} = r_b - r_a \cdot r_k$. Across all sparsity levels and both eviction strategies, the sign and relative ordering of $\mathrm{II}_{\times}$ match those of the additive II: importance-based eviction exhibits a monotonically increasing severity gradient ($G_{\times} = 58$--$241{\times}$), while random eviction remains flat ($G_{\times} \approx 1$). The crossover at $s{=}0.25$ is preserved. We adopt the additive formulation in the main text because the two sparsity axes operate on disjoint model dimensions (structural vs.\ positional), making additive independence the more natural null hypothesis at the sparsity levels studied.

=== limitations.tex ===
2:All experiments are conducted at the 7B parameter scale. Whether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested. Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \S\ref{sec:cross-arch}) partially extends the findings beyond the Qwen2 architecture: the directional pattern is qualitatively consistent but the interaction magnitude is substantially weaker and random pruning also exhibits a non-trivial phase gradient on LLaMA. The qualitative pattern has been tested on only two architecture families at the 7--8B scale; further validation on larger models and more diverse architectures (e.g., Mistral, multi-latent attention) is needed.
5:We evaluate exclusively on MATH-500, a mathematical reasoning benchmark. Different reasoning tasks---code generation, commonsense reasoning, multi-hop question answering---may induce different phase structures with different sparsity distributions, potentially altering the severity gradient profile.
11:Our experiments span $s \in \{0.15, 0.20, 0.25, 0.30\}$. More extreme sparsity ($s > 0.50$) may exhibit qualitatively different interaction dynamics. We do not report inference throughput or latency measurements, which are necessary for a complete deployment analysis but orthogonal to our severity characterization. Extended limitations in Appendix~\ref{app:limitations}.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015fDGgMfXwTBX4qwXJq1TS4",
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "76c351f7-5265-469b-9ea3-332c9ba52c63"
}
```

</details>

---

### System

_source line 80_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a317f67854c5856c4",
  "tool_use_id": "toolu_015fDGgMfXwTBX4qwXJq1TS4",
  "status": "completed",
  "output_file": "",
  "summary": "Verify tex file line numbers",
  "usage": {
    "total_tokens": 42313,
    "tool_uses": 15,
    "duration_ms": 72496
  },
  "uuid": "fadc4cf1-6080-4489-9254-052ebf90ec35",
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3"
}
```

---

### Tool result

_source line 81 · 2026-05-14T20:44:44.301Z_

<details><summary>↩ Tool result · `toolu_015fDGgMfXwTBX4qwXJq1TS4`</summary>

```text
Here is the complete report:

---

## File Summary

| File | Total Lines |
|------|-------------|
| abstract.tex | 13 |
| introduction.tex | 25 |
| methodology.tex | 22 |
| results.tex | 126 |
| conclusion.tex | 5 |
| discussion.tex | 11 |
| analysis.tex | 6 |
| appendix_moved.tex | 163 |
| appendix_disc_analysis.tex | 64 |
| appendix_results.tex | 10 |
| appendix.tex | 40 |
| limitations.tex | 11 |

---

## Pattern Matches by File

### abstract.tex (13 lines)

- **Line 6**: `50` — "using 50 MATH-500 problems"; `LlamaForCausalLM` — "DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM)"
- **Line 7**: `0.39`, `14.59`, `0.44`, `0.80` — "increases monotonically from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired Cohen's $d_z$ growing from $0.44$ (small) to $0.80$ (large)"
- **Line 8**: `7/8` — "no significant phase modulation in 7/8 conditions"
- **Line 9**: `qualitative` — "a qualitative reversal in strategy ranking"; `7.16` — "$\widetilde{\mathrm{II}} = 7.196$ vs.\ $1.363$"
- **Line 10**: `LlamaForCausalLM`, `Llama` — "DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM)"

---

### introduction.tex (25 lines)

- **Line 14**: `0.39`, `14.59`, `0.44`, `0.80` — "rises from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$ ($d_z$: $0.44 \to 0.80$"
- **Line 15**: `LlamaForCausalLM`, `Llama`, `qualitative` — "DeepSeek-R1-Distill-Llama-8B, LlamaForCausalLM) with a qualitatively consistent but substantially weaker trend"
- **Line 16**: `7/8` — "7/8 conditions non-significant"

---

### methodology.tex (22 lines)

- **Line 10**: `50` — "We use 50 problems stratified from MATH-500"

---

### results.tex (126 lines)

- **Line 8**: `0.39`, `14.59`, `qualitative` — "increases from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$"; "compound severity depends qualitatively on eviction strategy"
- **Line 13**: `50`, `n=` — caption "($n{=}50$ MATH-500 problems)"
- **Line 19**: `0.39`, `7.16`, `14.59` — table row "Importance & 0.39 & 1.48 & 7.16 & 14.59"
- **Line 29**: `69`, `274` — "severity gradient $G$ increases from $69{\times}$ at $s{=}0.15$ to $274{\times}$ at $s{=}0.30$"
- **Line 34**: `50` — caption "problem-level medians across 50 problems"
- **Line 40**: `69`, `0.39` — table row "0.15 & Importance & 0.006 & 0.081 & 0.398 & 0.39 & $\mathbf{69}$"
- **Line 46**: `7.16` — table row "0.25 & Importance & 0.032 & 1.118 & 7.196 & 7.16"
- **Line 49**: `14.59`, `274` — table row "0.30 & Importance & 0.053 & 2.283 & 14.639 & 14.59 & $\mathbf{274}$"
- **Line 50**: `50` (as part of "2.503") — table row (note: "2.503" contains "50" as substring; exact value present)
- **Line 58**: `69`, `274` — caption "increasing gradient from $69{\times}$ to $274{\times}$"
- **Line 71**: `0.28` — "marginal at $s{=}0.15$ ($d_z{=}0.28$, CI includes zero)"
- **Line 77**: `LlamaForCausalLM`, `Llama` — "DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, 8B parameters; $n{=}49$ paired problems)"
- **Line 79**: `qualitative` — "The qualitative pattern replicates"
- **Line 81**: `LLaMA`, `LlamaForCausalLM`, `qualitative` — "LLaMA severity differences are ${\sim}40{\times}$ smaller"; "qualitatively consistent across all three models"; "LlamaForCausalLM"
- **Line 86**: `LlamaForCausalLM`, `Llama` — caption "DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM)"
- **Line 106**: `0.44`, `0.80`, `0.28`, `1.02` — "grow from $d_z{=}0.44$ (small) to $d_z{=}0.80$ (large)"; "marginal at $s{=}0.15$ ($d_z{=}0.28$)"; "$d_z{=}0.89$/$1.02$"
- **Line 117**: `0.44`, `0.28`, `0.32` — table row "0.15 & 0.44 & 0.32\; $[0.20, 0.47]$ & 0.28 & 0.05"
- **Line 118**: `1.15` — table row "0.20 & 0.52 & 1.15\; $[0.66, 1.26]$"
- **Line 119**: `3.97` — table row "0.25 & 0.68 & 3.97\; $[2.83, 5.29]$"
- **Line 120**: `0.80`, `9.94`, `1.02`, `2.619` (as "2.62") — table row "0.30 & 0.80 & 9.94\; $[8.39, 16.65]$ & 1.02 & 2.62\; $[1.72, 3.65]$"

> Note on `2.619`: Line 120 contains `2.62` (which is a rounded form); `2.619` as an exact string does not appear but `2.62` is the value in the table. The exact string "2.619" does not appear verbatim anywhere.

---

### conclusion.tex (5 lines)

- **Line 4**: `69`, `274`, `0.44`, `0.80`, `7/8`, `LlamaForCausalLM`, `LLaMA`, `qualitative` — "severity gradient grows from $69{\times}$ to $274{\times}$ ($d_z$: $0.44 \to 0.80$); random eviction shows no such modulation (7/8 conditions non-significant)"; "DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM) with a qualitatively consistent"; "LLaMA results are directionally consistent"

---

### discussion.tex (11 lines)

- **Line 5**: `69`, `274`, `qualitative` — "The severity gradient ($69$--$274{\times}$)"; "qualitative direction"
- **Line 11**: `LlamaForCausalLM`, `LLaMA`, `qualitative` — "DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM)"; "qualitative pattern"; "non-trivial phase gradient on LLaMA"

---

### analysis.tex (6 lines)

**No matches** for any of the specified patterns.

---

### appendix_moved.tex (163 lines)

- **Line 26**: `50` — "Four of the 50 problems are excluded"
- **Line 39**: `0.39`, `7.16`, `14.59` — table row "DeepSeek-R1-Distill-Qwen-7B & 0.39 & 1.48 & 7.16 & 14.59"
- **Line 68**: `9.94` (as "9.85") — contains "9.85" not "9.94" (see below); also `69` not present here. Contains "0.19" — "CI lower bound ($0.19 \to 0.69 \to 1.66 \to 6.70$)"
- **Line 80**: `69` (as part of "0.69") — "$[0.69,\; 1.49]$"

> Clarifying Line 68 more precisely: "observed median differences increasing monotonically from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$" — contains `9.85` not `9.94`. The `9.94` pattern does not appear in this file.

---

### appendix_disc_analysis.tex (64 lines)

- **Line 14**: `7/8` — "Random eviction fails 7/8 paired permutation tests"
- **Line 28**: `future work` — "Scaling experiments are future work."
- **Line 33**: `LlamaForCausalLM`, `Llama`, `qualitative` — "DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM)"; "qualitatively consistent but substantially weaker"
- **Line 35**: `LlamaForCausalLM`, `qualitative` — "LlamaForCausalLM (\S\ref{sec:cross-arch}), which shows a qualitatively consistent"
- **Line 46**: `14.59` — "median_diff=14.59 (segment-level)"
- **Line 47**: `69` (as part of "$[6.70,\; 16.29]$") — contains "0.19" in "increasing from $0.19$ to $6.70$"
- **Line 54**: `qualitative` — "may exhibit qualitatively different interaction dynamics"
- **Line 57**: `future work` — "but confirming this is future work."
- **Line 62**: `future work` — "Phase-gated controllers are explicitly scoped as future work."

---

### appendix_results.tex (10 lines)

**No matches** for any of the specified patterns.

---

### appendix.tex (40 lines)

- **Line 38**: `qualitative` — "does not change qualitative conclusions"

---

### limitations.tex (11 lines)

- **Line 2**: `LlamaForCausalLM`, `Llama`, `LLaMA`, `qualitative` — "DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM)"; "non-trivial phase gradient on LLaMA"; "The qualitative pattern has been tested"
- **Line 5**: `50` (as part of "MATH-500") — "We evaluate exclusively on MATH-500"
- **Line 11**: `50` (as part of "0.50") — "More extreme sparsity ($s > 0.50$)"; `qualitative` — "may exhibit qualitatively different interaction dynamics"

---

## Patterns NOT found anywhere

The following patterns do not appear as exact strings in any of the 12 files:
- `0.048`
- `0.208`
- `1.109`
- `2.619` (only `2.62` appears, in results.tex line 120)
- `n=500`
- `C5b`
- `C8`

The pattern `9.94` appears only in **results.tex line 120** (`9.94\; $[8.39, 16.65]$`). It does NOT appear in appendix_moved.tex (which uses `9.85` for the permutation test result).

agentId: a317f67854c5856c4 (use SendMessage with to: 'a317f67854c5856c4' to continue this agent)
&lt;usage>total_tokens: 44895
tool_uses: 15
duration_ms: 72502&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "f6ce993c-0b4e-4dcf-a831-f3465b8f6cad",
  "tool_use_result": {
    "status": "completed",
    "prompt": "I need you to read specific sections of the paper tex files in this project and report the exact content at specified line numbers. The paper is at /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/\n\nRead these files completely:\n1. abstract.tex\n2. introduction.tex  \n3. methodology.tex\n4. results.tex\n5. conclusion.tex\n6. discussion.tex\n7. analysis.tex\n8. appendix_moved.tex\n9. appendix_disc_analysis.tex\n10. appendix_results.tex\n11. appendix.tex\n12. limitations.tex\n\nFor each file, report:\n- Total line count\n- ALL lines containing any of these patterns: \"50\" (as in n=50, 50 problems), \"0.32\", \"1.15\", \"3.97\", \"9.94\", \"0.048\", \"0.208\", \"1.109\", \"2.619\", \"0.44\", \"0.80\", \"0.28\", \"1.02\", \"14.59\", \"0.39\", \"7.16\", \"69\", \"274\", \"7/8\", \"qualitative\", \"n=500\", \"C5b\", \"C8\", \"LLaMA\", \"Llama\", \"future work\"\n\nReport the exact line number and content for each match. This is for verifying a paper update checklist, so precision matters.",
    "agentId": "a317f67854c5856c4",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is the complete report:\n\n---\n\n## File Summary\n\n| File | Total Lines |\n|------|-------------|\n| abstract.tex | 13 |\n| introduction.tex | 25 |\n| methodology.tex | 22 |\n| results.tex | 126 |\n| conclusion.tex | 5 |\n| discussion.tex | 11 |\n| analysis.tex | 6 |\n| appendix_moved.tex | 163 |\n| appendix_disc_analysis.tex | 64 |\n| appendix_results.tex | 10 |\n| appendix.tex | 40 |\n| limitations.tex | 11 |\n\n---\n\n## Pattern Matches by File\n\n### abstract.tex (13 lines)\n\n- **Line 6**: `50` — \"using 50 MATH-500 problems\"; `LlamaForCausalLM` — \"DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM)\"\n- **Line 7**: `0.39`, `14.59`, `0.44`, `0.80` — \"increases monotonically from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired Cohen's $d_z$ growing from $0.44$ (small) to $0.80$ (large)\"\n- **Line 8**: `7/8` — \"no significant phase modulation in 7/8 conditions\"\n- **Line 9**: `qualitative` — \"a qualitative reversal in strategy ranking\"; `7.16` — \"$\\widetilde{\\mathrm{II}} = 7.196$ vs.\\ $1.363$\"\n- **Line 10**: `LlamaForCausalLM`, `Llama` — \"DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM)\"\n\n---\n\n### introduction.tex (25 lines)\n\n- **Line 14**: `0.39`, `14.59`, `0.44`, `0.80` — \"rises from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$ ($d_z$: $0.44 \\to 0.80$\"\n- **Line 15**: `LlamaForCausalLM`, `Llama`, `qualitative` — \"DeepSeek-R1-Distill-Llama-8B, LlamaForCausalLM) with a qualitatively consistent but substantially weaker trend\"\n- **Line 16**: `7/8` — \"7/8 conditions non-significant\"\n\n---\n\n### methodology.tex (22 lines)\n\n- **Line 10**: `50` — \"We use 50 problems stratified from MATH-500\"\n\n---\n\n### results.tex (126 lines)\n\n- **Line 8**: `0.39`, `14.59`, `qualitative` — \"increases from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$\"; \"compound severity depends qualitatively on eviction strategy\"\n- **Line 13**: `50`, `n=` — caption \"($n{=}50$ MATH-500 problems)\"\n- **Line 19**: `0.39`, `7.16`, `14.59` — table row \"Importance & 0.39 & 1.48 & 7.16 & 14.59\"\n- **Line 29**: `69`, `274` — \"severity gradient $G$ increases from $69{\\times}$ at $s{=}0.15$ to $274{\\times}$ at $s{=}0.30$\"\n- **Line 34**: `50` — caption \"problem-level medians across 50 problems\"\n- **Line 40**: `69`, `0.39` — table row \"0.15 & Importance & 0.006 & 0.081 & 0.398 & 0.39 & $\\mathbf{69}$\"\n- **Line 46**: `7.16` — table row \"0.25 & Importance & 0.032 & 1.118 & 7.196 & 7.16\"\n- **Line 49**: `14.59`, `274` — table row \"0.30 & Importance & 0.053 & 2.283 & 14.639 & 14.59 & $\\mathbf{274}$\"\n- **Line 50**: `50` (as part of \"2.503\") — table row (note: \"2.503\" contains \"50\" as substring; exact value present)\n- **Line 58**: `69`, `274` — caption \"increasing gradient from $69{\\times}$ to $274{\\times}$\"\n- **Line 71**: `0.28` — \"marginal at $s{=}0.15$ ($d_z{=}0.28$, CI includes zero)\"\n- **Line 77**: `LlamaForCausalLM`, `Llama` — \"DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, 8B parameters; $n{=}49$ paired problems)\"\n- **Line 79**: `qualitative` — \"The qualitative pattern replicates\"\n- **Line 81**: `LLaMA`, `LlamaForCausalLM`, `qualitative` — \"LLaMA severity differences are ${\\sim}40{\\times}$ smaller\"; \"qualitatively consistent across all three models\"; \"LlamaForCausalLM\"\n- **Line 86**: `LlamaForCausalLM`, `Llama` — caption \"DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM)\"\n- **Line 106**: `0.44`, `0.80`, `0.28`, `1.02` — \"grow from $d_z{=}0.44$ (small) to $d_z{=}0.80$ (large)\"; \"marginal at $s{=}0.15$ ($d_z{=}0.28$)\"; \"$d_z{=}0.89$/$1.02$\"\n- **Line 117**: `0.44`, `0.28`, `0.32` — table row \"0.15 & 0.44 & 0.32\\; $[0.20, 0.47]$ & 0.28 & 0.05\"\n- **Line 118**: `1.15` — table row \"0.20 & 0.52 & 1.15\\; $[0.66, 1.26]$\"\n- **Line 119**: `3.97` — table row \"0.25 & 0.68 & 3.97\\; $[2.83, 5.29]$\"\n- **Line 120**: `0.80`, `9.94`, `1.02`, `2.619` (as \"2.62\") — table row \"0.30 & 0.80 & 9.94\\; $[8.39, 16.65]$ & 1.02 & 2.62\\; $[1.72, 3.65]$\"\n\n> Note on `2.619`: Line 120 contains `2.62` (which is a rounded form); `2.619` as an exact string does not appear but `2.62` is the value in the table. The exact string \"2.619\" does not appear verbatim anywhere.\n\n---\n\n### conclusion.tex (5 lines)\n\n- **Line 4**: `69`, `274`, `0.44`, `0.80`, `7/8`, `LlamaForCausalLM`, `LLaMA`, `qualitative` — \"severity gradient grows from $69{\\times}$ to $274{\\times}$ ($d_z$: $0.44 \\to 0.80$); random eviction shows no such modulation (7/8 conditions non-significant)\"; \"DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM) with a qualitatively consistent\"; \"LLaMA results are directionally consistent\"\n\n---\n\n### discussion.tex (11 lines)\n\n- **Line 5**: `69`, `274`, `qualitative` — \"The severity gradient ($69$--$274{\\times}$)\"; \"qualitative direction\"\n- **Line 11**: `LlamaForCausalLM`, `LLaMA`, `qualitative` — \"DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM)\"; \"qualitative pattern\"; \"non-trivial phase gradient on LLaMA\"\n\n---\n\n### analysis.tex (6 lines)\n\n**No matches** for any of the specified patterns.\n\n---\n\n### appendix_moved.tex (163 lines)\n\n- **Line 26**: `50` — \"Four of the 50 problems are excluded\"\n- **Line 39**: `0.39`, `7.16`, `14.59` — table row \"DeepSeek-R1-Distill-Qwen-7B & 0.39 & 1.48 & 7.16 & 14.59\"\n- **Line 68**: `9.94` (as \"9.85\") — contains \"9.85\" not \"9.94\" (see below); also `69` not present here. Contains \"0.19\" — \"CI lower bound ($0.19 \\to 0.69 \\to 1.66 \\to 6.70$)\"\n- **Line 80**: `69` (as part of \"0.69\") — \"$[0.69,\\; 1.49]$\"\n\n> Clarifying Line 68 more precisely: \"observed median differences increasing monotonically from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$\" — contains `9.85` not `9.94`. The `9.94` pattern does not appear in this file.\n\n---\n\n### appendix_disc_analysis.tex (64 lines)\n\n- **Line 14**: `7/8` — \"Random eviction fails 7/8 paired permutation tests\"\n- **Line 28**: `future work` — \"Scaling experiments are future work.\"\n- **Line 33**: `LlamaForCausalLM`, `Llama`, `qualitative` — \"DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM)\"; \"qualitatively consistent but substantially weaker\"\n- **Line 35**: `LlamaForCausalLM`, `qualitative` — \"LlamaForCausalLM (\\S\\ref{sec:cross-arch}), which shows a qualitatively consistent\"\n- **Line 46**: `14.59` — \"median_diff=14.59 (segment-level)\"\n- **Line 47**: `69` (as part of \"$[6.70,\\; 16.29]$\") — contains \"0.19\" in \"increasing from $0.19$ to $6.70$\"\n- **Line 54**: `qualitative` — \"may exhibit qualitatively different interaction dynamics\"\n- **Line 57**: `future work` — \"but confirming this is future work.\"\n- **Line 62**: `future work` — \"Phase-gated controllers are explicitly scoped as future work.\"\n\n---\n\n### appendix_results.tex (10 lines)\n\n**No matches** for any of the specified patterns.\n\n---\n\n### appendix.tex (40 lines)\n\n- **Line 38**: `qualitative` — \"does not change qualitative conclusions\"\n\n---\n\n### limitations.tex (11 lines)\n\n- **Line 2**: `LlamaForCausalLM`, `Llama`, `LLaMA`, `qualitative` — \"DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM)\"; \"non-trivial phase gradient on LLaMA\"; \"The qualitative pattern has been tested\"\n- **Line 5**: `50` (as part of \"MATH-500\") — \"We evaluate exclusively on MATH-500\"\n- **Line 11**: `50` (as part of \"0.50\") — \"More extreme sparsity ($s > 0.50$)\"; `qualitative` — \"may exhibit qualitatively different interaction dynamics\"\n\n---\n\n## Patterns NOT found anywhere\n\nThe following patterns do not appear as exact strings in any of the 12 files:\n- `0.048`\n- `0.208`\n- `1.109`\n- `2.619` (only `2.62` appears, in results.tex line 120)\n- `n=500`\n- `C5b`\n- `C8`\n\nThe pattern `9.94` appears only in **results.tex line 120** (`9.94\\; $[8.39, 16.65]$`). It does NOT appear in appendix_moved.tex (which uses `9.85` for the permutation test result)."
      }
    ],
    "totalDurationMs": 72502,
    "totalTokens": 44895,
    "totalToolUseCount": 15,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6830,
      "cache_read_input_tokens": 34844,
      "output_tokens": 3220,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6830
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3220,
          "cache_read_input_tokens": 34844,
          "cache_creation_input_tokens": 6830,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6830,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 12,
      "searchCount": 0,
      "bashCount": 3,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  }
}
```

</details>

---

### Assistant

_source line 82_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive picture. Let me also check for any mentions of C5b, C8, future work in the tex files, and verify the analysis.tex content more carefully since the agent reported "no matches" for the analysis patterns.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "af00e5cc-fa88-47cd-815b-00078d9362d2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XLgKMURaU1radsez7TDCrT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3920,
      "cache_read_input_tokens": 55337,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3920
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

_source line 83_

Let me verify analysis.tex content and search for a few more patterns the agent might have missed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "2c6ef254-187a-4fdc-a3b9-d0183a472207",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XLgKMURaU1radsez7TDCrT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3920,
      "cache_read_input_tokens": 55337,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3920
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

_source line 84_

<details open><summary>🔧 Tool call — Read · `toolu_01BLaWL1SoayXTBDEnZe4x26`</summary>

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
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "3bff1794-9f2a-43c6-9bde-22470423e72a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XLgKMURaU1radsez7TDCrT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3920,
      "cache_read_input_tokens": 55337,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3920
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

_source line 85 · 2026-05-14T20:44:48.295Z_

<details><summary>↩ Tool result · `toolu_01BLaWL1SoayXTBDEnZe4x26`</summary>

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
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "f773b499-8ad7-40ce-a91b-b6104238237c",
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

_source line 86_

<details open><summary>🔧 Tool call — Read · `toolu_01UxXnrB8xSvSxviCX42fv25`</summary>

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
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "ddb5e0ec-7a4b-44e0-8208-9f26928369ce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XLgKMURaU1radsez7TDCrT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3920,
      "cache_read_input_tokens": 55337,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3920
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

_source line 87 · 2026-05-14T20:44:48.812Z_

<details><summary>↩ Tool result · `toolu_01UxXnrB8xSvSxviCX42fv25`</summary>

```text
1	% Appendix: supplementary results details
2	
3	\section{Cross-Model Replication Details}
4	\label{app:cross-model-details}
5	
6	\paragraph{Per-problem concordance.}
7	The per-problem concordance across models is not significant (mean $\rho = -0.11$, $p = 0.926$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking. % exp_id: cross_model_analysis.json (spearman_rho=1.0, gradient_permutation_p=0.043, per_problem_concordance_p=0.926, mean_rho=-0.107)
8	
9	\paragraph{Random eviction control.}
10	As a control, random eviction on Qwen yields no systematic phase gradient at three of four sparsity levels (3/4 FAIL), mirroring DeepSeek's 4/4 FAIL pattern. At $s{=}0.30$, Qwen random produces a borderline PASS (permutation $p = 0.012$) but with negligible effect size ($d_z = -0.04$, CI spans zero), indicating no meaningful phase modulation. % exp_id: bf16_qw_rand_s015..s030; source: experiment_summary_table.json
11	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "38948145-352e-40d9-a42c-b9d8e0bdd726",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_results.tex",
      "content": "% Appendix: supplementary results details\n\n\\section{Cross-Model Replication Details}\n\\label{app:cross-model-details}\n\n\\paragraph{Per-problem concordance.}\nThe per-problem concordance across models is not significant (mean $\\rho = -0.11$, $p = 0.926$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking. % exp_id: cross_model_analysis.json (spearman_rho=1.0, gradient_permutation_p=0.043, per_problem_concordance_p=0.926, mean_rho=-0.107)\n\n\\paragraph{Random eviction control.}\nAs a control, random eviction on Qwen yields no systematic phase gradient at three of four sparsity levels (3/4 FAIL), mirroring DeepSeek's 4/4 FAIL pattern. At $s{=}0.30$, Qwen random produces a borderline PASS (permutation $p = 0.012$) but with negligible effect size ($d_z = -0.04$, CI spans zero), indicating no meaningful phase modulation. % exp_id: bf16_qw_rand_s015..s030; source: experiment_summary_table.json\n",
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

_source line 88_

<details open><summary>🔧 Tool call — Grep · `toolu_01DdaXaQ84ExVNBjYiihZaqN`</summary>

```json
{
  "pattern": "future.work|Future.Work|C5b|phase-gated controller|pilot|mitigation",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "output_mode": "content",
  "-n": true,
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "ab4744b8-3c48-4904-a223-d0d6e8a47a42",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XLgKMURaU1radsez7TDCrT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3920,
      "cache_read_input_tokens": 55337,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3920
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

_source line 89 · 2026-05-14T20:44:50.539Z_

<details><summary>↩ Tool result · `toolu_01DdaXaQ84ExVNBjYiihZaqN`</summary>

```text
artifacts/_project/paper/appendix_disc_analysis.tex:28:% REBUTTAL: 7B is the most-deployed scale for on-device and cost-constrained serving—exactly where compound sparsity is needed. The mechanism (entropy-discrimination collapse) is scale-agnostic in principle. Scaling experiments are future work.
artifacts/_project/paper/appendix_disc_analysis.tex:57:% REBUTTAL: Our focus is on the practically relevant regime where models retain usable quality. At s>0.30 both strategies degrade severely, making II measurement less informative. The sub-exponential growth (C6, $\Delta$ growth rate $3.8{\times} \to 4.8{\times} \to 2.0{\times}$) suggests saturation at higher sparsity, but confirming this is future work.
artifacts/_project/paper/appendix_disc_analysis.tex:62:% REBUTTAL: This is an empirical finding paper, not a method/system paper. The contribution is characterizing *what happens* (phase-modulated severity) and *why* (entropy-discrimination collapse), not building a system to fix it. Phase-gated controllers are explicitly scoped as future work. The finding is actionable regardless: any compound sparsity deployment should be aware of phase-dependent severity.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "605eceb9-616d-4b9f-93f2-1eaad88b04fb",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "artifacts/_project/paper/appendix_disc_analysis.tex:28:% REBUTTAL: 7B is the most-deployed scale for on-device and cost-constrained serving—exactly where compound sparsity is needed. The mechanism (entropy-discrimination collapse) is scale-agnostic in principle. Scaling experiments are future work.\nartifacts/_project/paper/appendix_disc_analysis.tex:57:% REBUTTAL: Our focus is on the practically relevant regime where models retain usable quality. At s>0.30 both strategies degrade severely, making II measurement less informative. The sub-exponential growth (C6, $\\Delta$ growth rate $3.8{\\times} \\to 4.8{\\times} \\to 2.0{\\times}$) suggests saturation at higher sparsity, but confirming this is future work.\nartifacts/_project/paper/appendix_disc_analysis.tex:62:% REBUTTAL: This is an empirical finding paper, not a method/system paper. The contribution is characterizing *what happens* (phase-modulated severity) and *why* (entropy-discrimination collapse), not building a system to fix it. Phase-gated controllers are explicitly scoped as future work. The finding is actionable regardless: any compound sparsity deployment should be aware of phase-dependent severity.",
    "numLines": 3
  }
}
```

</details>

---

### Assistant

_source line 90_

<details><summary>Logged reasoning block</summary>

```text
Good. Now I have a thorough picture. The existing checklist at `artifacts/c2_n500_paper_update_checklist.md` is already very comprehensive. Let me now evaluate:

1. Does it cover all n=50 references? Yes, it covers abstract L6, methodology L10, results L13/L34, appendix_moved L26/L73.
2. Does it cover all numeric values? Yes, very thorough.
3. Does it cover the C5b future work references? The checklist doesn't explicitly mention C5b, but the paper_framing says C5b is already scoped as future_work.


4. For C8 (LLaMA cross-architecture), the checklist is missing explicit coverage of the LLaMA sections scattered across results.tex, conclusion, discussion, limitations, and appendix—these will need attention if the n=500 experiments affect the LLaMA narrative.
5. I should verify the literature map is complete, and I'm realizing the existing checklist is already solid but may have gaps around the LLaMA content that needs to be flagged for potential updates.

Since the n=500 experiments only apply to DeepSeek and Qwen, the LLaMA sections shouldn't require changes unless comparative statements between models shift. The checklist covers analysis.tex and appendix_results.tex adequately, though I should add specific line references for results.tex lines 77-81 where LLaMA content appears.

The literature_map.yaml was last updated in mid-May, so I should verify there aren't recent papers in compound sparsity I'm missing, though I don't have direct web search. At this point, the existing checklist is quite comprehensive—I've read the paper framing, writing plan, literature map, and identified all n=50 references, so I should finalize and save the checklist.

Looking at what might still be missing: the abstract mentions LlamaForCausalLM which could need updating if n=500 produces new LLaMA results, the results section has that n=49 paired problems statement that stays at n=50 unless separate LLaMA experiments run, and there's a comparative claim about LLaMA severity differences that might shift with the new DS/QW data. I should also verify the appendix results section about the FAIL counts is properly captured.

Actually, scanning through more carefully, the existing checklist already covers most of the appendix sections and analysis tables. The main gap is whether the results.tex LLaMA comparative statements need recalibration based on the new data. I'm noticing the existing checklist is already quite comprehensive at 350 lines, so rather than completely rewriting it, I should identify what's genuinely missing and add those specific gaps—the literature completeness check, the C8/LLaMA implications, and any location references I haven't covered yet.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "a9d02b99-35b6-4653-b620-4ab4281371e0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DAvN2QCSsPxzUVw6mDDZZN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1645,
      "cache_read_input_tokens": 59257,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1645
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

_source line 91_

Now let me check for any references in discussion.tex and limitations.tex that the existing checklist might miss, and do the literature completeness check.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "4fc0e70d-57bf-42a1-a0a7-b4aa0a95e7d2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DAvN2QCSsPxzUVw6mDDZZN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1645,
      "cache_read_input_tokens": 59257,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1645
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

_source line 92_

<details open><summary>🔧 Tool call — Read · `toolu_01XtMiecjyfz36nhhY39WwtF`</summary>

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
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "37df67ec-92c3-41a5-bd4f-278857c4ccfb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DAvN2QCSsPxzUVw6mDDZZN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1645,
      "cache_read_input_tokens": 59257,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1645
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

_source line 93 · 2026-05-14T20:45:28.996Z_

<details><summary>↩ Tool result · `toolu_01XtMiecjyfz36nhhY39WwtF`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Quantitative surprise.}
5	While the qualitative direction---importance scores degrade when attention is diffuse---may seem expected, the quantitative structure is not predictable from first principles. The severity gradient ($69$--$274{\times}$) far exceeds a naive ``somewhat worse'' prediction. The crossover---where importance-based eviction simultaneously outperforms random in high-sparsity phases ($\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$) and underperforms in low-sparsity phases ($7.196$ vs.\ $1.363$)---cannot be derived from single-axis entropy reasoning. The flat random baseline ($G \approx 1$) confirms the amplification is strategy-specific, not inherent to compound sparsity. % exp_id: bf16_importance_s015..s030, bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json
6	
7	\paragraph{Implications for deployment.}
8	Applying a uniform compression budget across all inference steps implicitly accepts order-of-magnitude severity penalties during low-sparsity reasoning phases. A \emph{phase-aware compression budget}---allocating lower sparsity to phases with $G \gg 1$ and reclaiming budget in near-additive high-sparsity phases---could mitigate this interaction while preserving compression gains. The severity gradient provides a natural signal for such allocation. Discrimination collapse depends on attention-mass-based importance scoring shared by major KV cache methods (H$_2$O \cite{h2o-neurips2023}, SnapKV \cite{snapkv-neurips2024}, PyramidKV \cite{pyramidkv-2024}), suggesting broad applicability. Extended discussion in Appendix~\ref{app:extended-discussion}.
9	
10	\paragraph{Architecture-dependent magnitude.}
11	Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM) provides partial support for the qualitative pattern---monotonically increasing severity gradient under importance-based eviction with within-strategy phase gradient $d_z \geq 1.0$---while revealing that absolute severity magnitudes are architecture-dependent (${\sim}40{\times}$ smaller than DeepSeek, ${\sim}7{\times}$ smaller than Qwen) and the strategy--phase interaction is substantially weaker than in Qwen2-based architectures. Notably, random pruning also exhibits a non-trivial phase gradient on LLaMA ($d_z \in [0.35, 0.45]$), reducing the contrast between strategies. This dissociation between qualitatively consistent directional trends and markedly different magnitudes suggests the phase-strategy interaction may be a general property of compound sparsity on reasoning models, while its quantitative impact---and the degree to which it is strategy-specific---depends on architecture-specific attention distributions and head specialization patterns. % exp_id: c3_llama
12	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "a33075c6-9403-44ff-83f4-1a7fb58a328c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex",
      "content": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Quantitative surprise.}\nWhile the qualitative direction---importance scores degrade when attention is diffuse---may seem expected, the quantitative structure is not predictable from first principles. The severity gradient ($69$--$274{\\times}$) far exceeds a naive ``somewhat worse'' prediction. The crossover---where importance-based eviction simultaneously outperforms random in high-sparsity phases ($\\widetilde{\\mathrm{II}} = 0.032$ vs.\\ $0.818$) and underperforms in low-sparsity phases ($7.196$ vs.\\ $1.363$)---cannot be derived from single-axis entropy reasoning. The flat random baseline ($G \\approx 1$) confirms the amplification is strategy-specific, not inherent to compound sparsity. % exp_id: bf16_importance_s015..s030, bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json\n\n\\paragraph{Implications for deployment.}\nApplying a uniform compression budget across all inference steps implicitly accepts order-of-magnitude severity penalties during low-sparsity reasoning phases. A \\emph{phase-aware compression budget}---allocating lower sparsity to phases with $G \\gg 1$ and reclaiming budget in near-additive high-sparsity phases---could mitigate this interaction while preserving compression gains. The severity gradient provides a natural signal for such allocation. Discrimination collapse depends on attention-mass-based importance scoring shared by major KV cache methods (H$_2$O \\cite{h2o-neurips2023}, SnapKV \\cite{snapkv-neurips2024}, PyramidKV \\cite{pyramidkv-2024}), suggesting broad applicability. Extended discussion in Appendix~\\ref{app:extended-discussion}.\n\n\\paragraph{Architecture-dependent magnitude.}\nCross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM) provides partial support for the qualitative pattern---monotonically increasing severity gradient under importance-based eviction with within-strategy phase gradient $d_z \\geq 1.0$---while revealing that absolute severity magnitudes are architecture-dependent (${\\sim}40{\\times}$ smaller than DeepSeek, ${\\sim}7{\\times}$ smaller than Qwen) and the strategy--phase interaction is substantially weaker than in Qwen2-based architectures. Notably, random pruning also exhibits a non-trivial phase gradient on LLaMA ($d_z \\in [0.35, 0.45]$), reducing the contrast between strategies. This dissociation between qualitatively consistent directional trends and markedly different magnitudes suggests the phase-strategy interaction may be a general property of compound sparsity on reasoning models, while its quantitative impact---and the degree to which it is strategy-specific---depends on architecture-specific attention distributions and head specialization patterns. % exp_id: c3_llama\n",
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

_source line 94_

<details open><summary>🔧 Tool call — Read · `toolu_017cBjPTr1s7LdaJqNjXKkm3`</summary>

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
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "01cbebcb-8171-4f1a-94f8-8e68674efeae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DAvN2QCSsPxzUVw6mDDZZN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1645,
      "cache_read_input_tokens": 59257,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1645
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

_source line 95 · 2026-05-14T20:45:29.393Z_

<details><summary>↩ Tool result · `toolu_017cBjPTr1s7LdaJqNjXKkm3`</summary>

```text
1	\paragraph{Model scale and architecture.}
2	All experiments are conducted at the 7B parameter scale. Whether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested. Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \S\ref{sec:cross-arch}) partially extends the findings beyond the Qwen2 architecture: the directional pattern is qualitatively consistent but the interaction magnitude is substantially weaker and random pruning also exhibits a non-trivial phase gradient on LLaMA. The qualitative pattern has been tested on only two architecture families at the 7--8B scale; further validation on larger models and more diverse architectures (e.g., Mistral, multi-latent attention) is needed.
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
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "23a810f6-6518-4605-ba55-c849c8fc4741",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/limitations.tex",
      "content": "\\paragraph{Model scale and architecture.}\nAll experiments are conducted at the 7B parameter scale. Whether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested. Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \\S\\ref{sec:cross-arch}) partially extends the findings beyond the Qwen2 architecture: the directional pattern is qualitatively consistent but the interaction magnitude is substantially weaker and random pruning also exhibits a non-trivial phase gradient on LLaMA. The qualitative pattern has been tested on only two architecture families at the 7--8B scale; further validation on larger models and more diverse architectures (e.g., Mistral, multi-latent attention) is needed.\n\n\\paragraph{Task coverage.}\nWe evaluate exclusively on MATH-500, a mathematical reasoning benchmark. Different reasoning tasks---code generation, commonsense reasoning, multi-hop question answering---may induce different phase structures with different sparsity distributions, potentially altering the severity gradient profile.\n\n\\paragraph{Mechanism.}\nThe discrimination collapse mechanism is supported by correlational evidence (consistent Gini/CV reduction across all conditions); causal validation through controlled entropy manipulation is needed. The entropy redistribution component replicates on only 2/4 Qwen conditions, suggesting model-specific factors.\n\n\\paragraph{Sparsity range.}\nOur experiments span $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$. More extreme sparsity ($s > 0.50$) may exhibit qualitatively different interaction dynamics. We do not report inference throughput or latency measurements, which are necessary for a complete deployment analysis but orthogonal to our severity characterization. Extended limitations in Appendix~\\ref{app:limitations}.\n",
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

_source line 96_

<details open><summary>🔧 Tool call — Read · `toolu_01De9JDaQYzhym9XbctEExcU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex",
  "offset": 65,
  "limit": 62
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "be0a53b1-77fd-4543-94e9-27bccc800546",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DAvN2QCSsPxzUVw6mDDZZN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1645,
      "cache_read_input_tokens": 59257,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1645
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

_source line 97 · 2026-05-14T20:45:29.938Z_

<details><summary>↩ Tool result · `toolu_01De9JDaQYzhym9XbctEExcU`</summary>

```text
65	
66	A strategy ranking reversal emerges across all sparsity levels: at $s{=}0.25$, importance-based eviction yields \emph{lower} II than random in the high-sparsity phase ($0.032$ vs.\ $0.818$) but \emph{higher} II in the low-sparsity phase ($7.196$ vs.\ $1.363$---a $5.3{\times}$ reversal), demonstrating that no single strategy dominates uniformly. Full crossover analysis and visualization appear in Appendix~\ref{app:crossover-details}. % exp_id: bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json; 7.196/1.363=5.28
67	
68	\subsection{Cross-Model Replication}
69	\label{sec:cross-model}
70	
71	Qwen2.5-7B-Instruct (standard instruction tuning, same Qwen2 backbone) reproduces the monotonic severity gradient: $\Delta$ increases from $0.04$ at $s{=}0.15$ to $2.94$ at $s{=}0.30$, paralleling DeepSeek at ${\sim}1/5$ the magnitude. Both models yield strictly increasing $d_z$ trajectories (Spearman $\rho = 1.0$; gradient permutation $p = 0.043$). The effect is marginal at $s{=}0.15$ ($d_z{=}0.28$, CI includes zero) but reliable at $s \geq 0.20$ ($d_z \geq 0.55$). Full cross-model tables and figures appear in Appendix~\ref{app:cross-model-details}. % exp_id: cross_model_analysis.json; cohens_d_bf16_qwen.json
72	
73	
74	\subsection{Cross-Architecture Validation}
75	\label{sec:cross-arch}
76	
77	To test whether the phase-modulated severity pattern extends beyond the Qwen2 architecture, we replicate the experiment on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, 8B parameters; $n{=}49$ paired problems). Table~\ref{tab:llama-cross-arch} reports the strategy-dependent severity comparison across sparsity levels.
78	
79	The qualitative pattern replicates: importance-based eviction produces systematically larger phase-dependent severity than random eviction, with monotonically increasing paired $d_z$ ($0.19 \to 0.26 \to 0.29 \to 0.34$). At $s{=}0.30$, the Wilcoxon test reaches significance after Bonferroni correction ($p = 0.029$, $k{=}4$). At $s{=}0.15$, the median difference CI $[0.002, 0.043]$ excludes zero despite the small absolute magnitude ($\widetilde{\Delta} = 0.020$). Under importance-based eviction, the within-strategy phase gradient $d_z$ (low $-$ high) is consistently large at all sparsity levels ($d_z \in [1.00, 1.12]$), while random eviction yields only small phase gradients ($d_z \in [0.35, 0.45]$). % exp_id: c3_llama
80	
81	The absolute magnitude is architecture-dependent: LLaMA severity differences are ${\sim}40{\times}$ smaller than DeepSeek and ${\sim}7{\times}$ smaller than Qwen, and the interaction is substantially weaker---random pruning also shows a non-trivial phase gradient on LLaMA ($d_z \in [0.35, 0.45]$), reducing the strategy contrast observed in Qwen2 models. The directional pattern---monotonically increasing $d_z$, importance $>$ random, larger phase gradient under importance---is qualitatively consistent across all three models spanning two architectures (Qwen2ForCausalLM, LlamaForCausalLM), though the interaction magnitude is substantially weaker on LlamaForCausalLM. % exp_id: c3_llama; cross_model_analysis.json
82	
83	\begin{table}[t]
84	\centering
85	\small
86	\caption{Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM). $d_z$: paired Cohen's $d$ for importance vs.\ random severity; $\widetilde{\Delta}$: median paired difference with bootstrap 95\% CI ($B{=}10{,}000$); $p$: Bonferroni-corrected Wilcoxon $p$ ($k{=}4$). $n{=}49$ paired problems.}
87	\label{tab:llama-cross-arch}
88	\begin{tabular}{@{}lccc@{}}
89	\toprule
90	$s$ & $d_z$ & $\widetilde{\Delta}$\; [95\% CI] & $p_{\text{Bonf}}$ \\
91	\midrule
92	0.15 & 0.19 & 0.020\; $[0.002, 0.043]$ & 0.219 \\
93	0.20 & 0.26 & 0.022\; $[-0.090, 0.187]$ & 0.253 \\
94	0.25 & 0.29 & 0.095\; $[-0.004, 0.303]$ & 0.083 \\
95	0.30 & 0.34 & 0.356\; $[-0.069, 0.544]$ & $\mathbf{0.029}$ \\
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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "e2d0e3f9-8237-4794-8da4-9c086602e5e7",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex",
      "content": "\nA strategy ranking reversal emerges across all sparsity levels: at $s{=}0.25$, importance-based eviction yields \\emph{lower} II than random in the high-sparsity phase ($0.032$ vs.\\ $0.818$) but \\emph{higher} II in the low-sparsity phase ($7.196$ vs.\\ $1.363$---a $5.3{\\times}$ reversal), demonstrating that no single strategy dominates uniformly. Full crossover analysis and visualization appear in Appendix~\\ref{app:crossover-details}. % exp_id: bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json; 7.196/1.363=5.28\n\n\\subsection{Cross-Model Replication}\n\\label{sec:cross-model}\n\nQwen2.5-7B-Instruct (standard instruction tuning, same Qwen2 backbone) reproduces the monotonic severity gradient: $\\Delta$ increases from $0.04$ at $s{=}0.15$ to $2.94$ at $s{=}0.30$, paralleling DeepSeek at ${\\sim}1/5$ the magnitude. Both models yield strictly increasing $d_z$ trajectories (Spearman $\\rho = 1.0$; gradient permutation $p = 0.043$). The effect is marginal at $s{=}0.15$ ($d_z{=}0.28$, CI includes zero) but reliable at $s \\geq 0.20$ ($d_z \\geq 0.55$). Full cross-model tables and figures appear in Appendix~\\ref{app:cross-model-details}. % exp_id: cross_model_analysis.json; cohens_d_bf16_qwen.json\n\n\n\\subsection{Cross-Architecture Validation}\n\\label{sec:cross-arch}\n\nTo test whether the phase-modulated severity pattern extends beyond the Qwen2 architecture, we replicate the experiment on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, 8B parameters; $n{=}49$ paired problems). Table~\\ref{tab:llama-cross-arch} reports the strategy-dependent severity comparison across sparsity levels.\n\nThe qualitative pattern replicates: importance-based eviction produces systematically larger phase-dependent severity than random eviction, with monotonically increasing paired $d_z$ ($0.19 \\to 0.26 \\to 0.29 \\to 0.34$). At $s{=}0.30$, the Wilcoxon test reaches significance after Bonferroni correction ($p = 0.029$, $k{=}4$). At $s{=}0.15$, the median difference CI $[0.002, 0.043]$ excludes zero despite the small absolute magnitude ($\\widetilde{\\Delta} = 0.020$). Under importance-based eviction, the within-strategy phase gradient $d_z$ (low $-$ high) is consistently large at all sparsity levels ($d_z \\in [1.00, 1.12]$), while random eviction yields only small phase gradients ($d_z \\in [0.35, 0.45]$). % exp_id: c3_llama\n\nThe absolute magnitude is architecture-dependent: LLaMA severity differences are ${\\sim}40{\\times}$ smaller than DeepSeek and ${\\sim}7{\\times}$ smaller than Qwen, and the interaction is substantially weaker---random pruning also shows a non-trivial phase gradient on LLaMA ($d_z \\in [0.35, 0.45]$), reducing the strategy contrast observed in Qwen2 models. The directional pattern---monotonically increasing $d_z$, importance $>$ random, larger phase gradient under importance---is qualitatively consistent across all three models spanning two architectures (Qwen2ForCausalLM, LlamaForCausalLM), though the interaction magnitude is substantially weaker on LlamaForCausalLM. % exp_id: c3_llama; cross_model_analysis.json\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM). $d_z$: paired Cohen's $d$ for importance vs.\\ random severity; $\\widetilde{\\Delta}$: median paired difference with bootstrap 95\\% CI ($B{=}10{,}000$); $p$: Bonferroni-corrected Wilcoxon $p$ ($k{=}4$). $n{=}49$ paired problems.}\n\\label{tab:llama-cross-arch}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\n$s$ & $d_z$ & $\\widetilde{\\Delta}$\\; [95\\% CI] & $p_{\\text{Bonf}}$ \\\\\n\\midrule\n0.15 & 0.19 & 0.020\\; $[0.002, 0.043]$ & 0.219 \\\\\n0.20 & 0.26 & 0.022\\; $[-0.090, 0.187]$ & 0.253 \\\\\n0.25 & 0.29 & 0.095\\; $[-0.004, 0.303]$ & 0.083 \\\\\n0.30 & 0.34 & 0.356\\; $[-0.069, 0.544]$ & $\\mathbf{0.029}$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Statistical Validation}\n\\label{sec:stat-validation}\n\nPaired permutation tests ($10{,}000$ permutations, Bonferroni-corrected) confirm that importance-based eviction produces significantly larger phase-dependent severity than random eviction at all four sparsity levels ($p_{\\text{Bonf}} < 0.005$), with observed median differences increasing monotonically from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$. Full permutation test results and forest plot appear in Appendix~\\ref{app:permutation-details}. % exp_id: deepseek_bf16_permtest; source: permutation_test_results.json\n\nTable~\\ref{tab:cohens-d} reports paired Cohen's $d_z$ for both models. For DeepSeek, effect sizes grow from $d_z{=}0.44$ (small) to $d_z{=}0.80$ (large). For Qwen, the effect is marginal at $s{=}0.15$ ($d_z{=}0.28$, CI includes zero), becoming reliable at $s \\geq 0.20$ ($d_z \\geq 0.55$). At $s \\geq 0.25$, Qwen exhibits larger standardized effect sizes ($d_z{=}0.89$/$1.02$ vs.\\ $0.68$/$0.80$), consistent with lower between-problem variance despite smaller absolute II values. % exp_id: cohens_d_bf16.json; cohens_d_bf16_qwen.json\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Paired $d_z$ for phase-dependent II (low $-$ high) under importance-based eviction. Bootstrap 95\\% CIs ($B{=}10{,}000$).}\n\\label{tab:cohens-d}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n$s$ & DS $d_z$ & $\\widetilde{\\Delta}$ [CI] & QW $d_z$ & $\\widetilde{\\Delta}$ [CI] \\\\\n\\midrule\n0.15 & 0.44 & 0.32\\; $[0.20, 0.47]$ & 0.28 & 0.05\\; $[-0.01, 0.11]$\\textsuperscript{ns} \\\\ % exp_id: bf16_ds_imp_s015, bf16_qw_imp_s015\n0.20 & 0.52 & 1.15\\; $[0.66, 1.26]$ & 0.55 & 0.21\\; $[0.07, 0.40]$ \\\\ % exp_id: bf16_ds_imp_s020, bf16_qw_imp_s020\n0.25 & 0.68 & 3.97\\; $[2.83, 5.29]$ & 0.89 & 1.11\\; $[0.61, 1.47]$ \\\\ % exp_id: bf16_ds_imp_s025, bf16_qw_imp_s025\n0.30 & 0.80 & 9.94\\; $[8.39, 16.65]$ & 1.02 & 2.62\\; $[1.72, 3.65]$ \\\\ % exp_id: bf16_ds_imp_s030, bf16_qw_imp_s030\n\\bottomrule\n\\multicolumn{5}{@{}l}{\\footnotesize \\textsuperscript{ns}Marginal at $s{=}0.15$; reliable at $s \\geq 0.20$.}\n\\end{tabular}\n\\end{table}\n\nWe provide a mechanistic analysis in terms of entropy-discrimination collapse in \\S\\ref{sec:analysis}.",
      "numLines": 62,
      "startLine": 65,
      "totalLines": 127
    }
  }
}
```

</details>

---

### Assistant

_source line 98_

<details><summary>Logged reasoning block</summary>

```text
Now I have a complete picture. The existing checklist at `artifacts/c2_n500_paper_update_checklist.md` is already very thorough. Let me assess what's missing:

1. **LLaMA/C8 section**: The existing checklist doesn't mention results.tex L77-95 (LLaMA table), discussion.tex L11, limitations.tex L2. These LLaMA numbers (n=49 paired problems, d_z 0.19→0.34, etc.) are from c3_llama which is NOT being re-run at n=500. 

So those don't need updating, but comparative statements like "~40× smaller than DeepSeek" or "~7× smaller than Qwen" could shift if those baseline numbers change.

2. **Literature completeness**: literature_map.yaml was updated 2026-05-14 and covers direct competitors like SparK, GRASPrune, and DefensiveKV, plus phase-aware methods like ThinKV.

PagedEviction, compound compression techniques, phase transition research, and various KV cache methods. The coverage looks solid overall, though I notice HIES from arxiv 2510.13832 is referenced in paper_framing.md but missing from the literature map—that's a gap I should flag. I should also check if there are any very recent papers from May 2026 that might not be captured yet.

Looking at the C5b references, the paper already marks phase-gated controllers as future work in the appendix, so that's accounted for. Now I'm going to create an enhanced checklist that builds on the existing one and adds the literature gap I found, along with notes about LLaMA comparative statements that might need recalibration. I'll save this to the requested path with both the original content and my additions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "1974df82-9a5f-4849-bb41-9a5924b58a40",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015vc3icYm2AGLaiZ5tK44eQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5853,
      "cache_read_input_tokens": 60902,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5853
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

_source line 99_

已有一份详尽的清单。现在我需要识别遗漏项并增强它。关键发现：

1. **现有清单** (`c2_n500_paper_update_checklist.md`) 已覆盖 ~90% 内容
2. **遗漏项**：LLaMA 比较性声明可能受 DS/QW 数值变化影响（results.tex L81, discussion.tex L11），HIES 论文不在 literature_map 中
3. **需新增**：文献完整性分析、LLaMA 间接影响、C5b/C8 叙事位置追踪

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "4d3d8435-42f3-431b-9531-dc8d7f037ca9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015vc3icYm2AGLaiZ5tK44eQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5853,
      "cache_read_input_tokens": 60902,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5853
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

_source line 100_

<details open><summary>🔧 Tool call — Read · `toolu_016iwzNMrEqNNup1wheJZy5j`</summary>

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
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "c5c834fa-c9af-4986-a1d4-d65940ec46e2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015vc3icYm2AGLaiZ5tK44eQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5853,
      "cache_read_input_tokens": 60902,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5853
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

_source line 101 · 2026-05-14T20:45:55.388Z_

<details><summary>↩ Tool result · `toolu_016iwzNMrEqNNup1wheJZy5j`</summary>

```text
1	\begin{abstract}
2	Compound sparsity---simultaneously pruning attention heads and evicting KV cache entries---is essential for efficient LLM inference but produces super-additive quality degradation whose structure is poorly understood.
3	Prior work treats compound interaction magnitude as approximately constant across the generation process.
4	We show that this assumption is wrong: compound sparsity severity is an emergent phase-strategy interaction that varies by over an order of magnitude across reasoning phases.
5	
6	We evaluate compound sparsity on three models---DeepSeek-R1-Distill-Qwen-7B, Qwen2.5-7B-Instruct (both Qwen2ForCausalLM), and DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM)---spanning two architectures, using 50 MATH-500 problems, measuring the Interaction Index---a super-additivity metric---across quantile-segmented reasoning phases at sparsity levels $s \in \{0.15, 0.20, 0.25, 0.30\}$.
7	Under importance-based KV cache eviction, the median Interaction Index difference between low-sparsity and high-sparsity reasoning phases increases monotonically from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired Cohen's $d_z$ growing from $0.44$ (small) to $0.80$ (large); Bonferroni-corrected permutation tests yield $p < 0.005$ at all four sparsity levels.
8	Random eviction produces no significant phase modulation in 7/8 conditions; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) shows negligible effect size ($d_z{=}{-}0.04$), confirming that the severity gradient is strategy-specific, not an inherent property of compound sparsity.
9	At $s{=}0.25$, a crossover emerges: importance-based eviction outperforms random in high-sparsity phases ($\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$) yet underperforms in low-sparsity phases ($\widetilde{\mathrm{II}} = 7.196$ vs.\ $1.363$)---a qualitative reversal in strategy ranking.
10	The pattern replicates on Qwen2.5-7B-Instruct at $s \geq 0.20$ ($d_z \geq 0.55$; Spearman $\rho = 1.0$; gradient permutation $p = 0.043$) and on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM), where monotonically increasing $d_z$ ($0.19 \to 0.34$; $s{=}0.30$ Wilcoxon $p_{\text{Bonf}} = 0.029$) suggests cross-architecture generalization, though at ${\sim}$1/40 the absolute magnitude and with substantially weaker interaction than in Qwen2-based architectures. % exp_id: c3_llama
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
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "5c523b54-d53a-4558-b561-76d5c6244c5b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex",
      "content": "\\begin{abstract}\nCompound sparsity---simultaneously pruning attention heads and evicting KV cache entries---is essential for efficient LLM inference but produces super-additive quality degradation whose structure is poorly understood.\nPrior work treats compound interaction magnitude as approximately constant across the generation process.\nWe show that this assumption is wrong: compound sparsity severity is an emergent phase-strategy interaction that varies by over an order of magnitude across reasoning phases.\n\nWe evaluate compound sparsity on three models---DeepSeek-R1-Distill-Qwen-7B, Qwen2.5-7B-Instruct (both Qwen2ForCausalLM), and DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM)---spanning two architectures, using 50 MATH-500 problems, measuring the Interaction Index---a super-additivity metric---across quantile-segmented reasoning phases at sparsity levels $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$.\nUnder importance-based KV cache eviction, the median Interaction Index difference between low-sparsity and high-sparsity reasoning phases increases monotonically from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired Cohen's $d_z$ growing from $0.44$ (small) to $0.80$ (large); Bonferroni-corrected permutation tests yield $p < 0.005$ at all four sparsity levels.\nRandom eviction produces no significant phase modulation in 7/8 conditions; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) shows negligible effect size ($d_z{=}{-}0.04$), confirming that the severity gradient is strategy-specific, not an inherent property of compound sparsity.\nAt $s{=}0.25$, a crossover emerges: importance-based eviction outperforms random in high-sparsity phases ($\\widetilde{\\mathrm{II}} = 0.032$ vs.\\ $0.818$) yet underperforms in low-sparsity phases ($\\widetilde{\\mathrm{II}} = 7.196$ vs.\\ $1.363$)---a qualitative reversal in strategy ranking.\nThe pattern replicates on Qwen2.5-7B-Instruct at $s \\geq 0.20$ ($d_z \\geq 0.55$; Spearman $\\rho = 1.0$; gradient permutation $p = 0.043$) and on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM), where monotonically increasing $d_z$ ($0.19 \\to 0.34$; $s{=}0.30$ Wilcoxon $p_{\\text{Bonf}} = 0.029$) suggests cross-architecture generalization, though at ${\\sim}$1/40 the absolute magnitude and with substantially weaker interaction than in Qwen2-based architectures. % exp_id: c3_llama\n\nWe propose entropy-discrimination collapse as an explanatory mechanism: head pruning flattens cumulative importance scores in phases where attention is already broadly distributed, degrading the discriminative power of importance-based eviction in a phase-dependent manner.\nThese findings challenge the phase-invariance assumption in compound sparsity deployment and motivate phase-aware compression budgets for reasoning models.\n\\end{abstract}",
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

_source line 102_

<details open><summary>🔧 Tool call — Read · `toolu_011nhcokayXXT1ahw2kdtuPb`</summary>

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
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "285e9d06-5377-42d4-bbd5-672a6afe7524",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015vc3icYm2AGLaiZ5tK44eQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5853,
      "cache_read_input_tokens": 60902,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5853
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

_source line 103 · 2026-05-14T20:45:55.935Z_

<details><summary>↩ Tool result · `toolu_011nhcokayXXT1ahw2kdtuPb`</summary>

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
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "fdf1443b-cf95-40e0-843c-2ed8bca02713",
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

### Assistant

_source line 104_

<details><summary>Logged reasoning block</summary>

```text
Now I have everything I need. Let me compile the enhanced checklist. The existing one is very good, but I need to add:

1. LLaMA comparative statements that will be indirectly affected
2. Literature gap analysis (HIES missing from lit map)
3. C5b/C8 narrative position tracking
4. Some corrections to the existing checklist (e.g., appendix_results.tex has content at L7 and L10 that the existing checklist partially covers)

Let me also note: the abstract line 10 mentions "~1/40 the absolute magnitude" for LLaMA — this is compared to DeepSeek. 

I'm realizing the critical issue: if DeepSeek numbers change with n=500, all the comparative ratios throughout the paper shift too. The ~40× and ~7× comparisons in results.tex, the same ratios in discussion.tex, and the "~1/40 the magnitude" in the conclusion all hinge on DeepSeek and Qwen's baseline numbers, not LLaMA itself. The existing checklist treats LLaMA sections as static, but these dependent comparisons are actually a blind spot that needs tracking.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "504b5ca0-7965-43a0-8128-145134f70004",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jr1XKjzauxYdjGCcno2WMw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2376,
      "cache_read_input_tokens": 66755,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2376
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

_source line 105_

Now I have the complete picture. Let me save the enhanced checklist.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "1548cb05-cad4-4c11-99f3-0731c487acad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jr1XKjzauxYdjGCcno2WMw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2376,
      "cache_read_input_tokens": 66755,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2376
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

_source line 106_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01HNxhtwy25XAC8QpF5XjEVp`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file",
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
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "6bd5c4ec-4c64-4214-9041-e4eb7809d4e4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jr1XKjzauxYdjGCcno2WMw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2376,
      "cache_read_input_tokens": 66755,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2376
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

_source line 107 · 2026-05-14T20:46:07.112Z_

<details><summary>↩ Tool result · `toolu_01HNxhtwy25XAC8QpF5XjEVp`</summary>

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
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "afbf76d1-ba38-4efe-a862-44f62441e150",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 108_

<details><summary>Logged reasoning block</summary>

```text
The save_project_file tool has a whitelist: "Writable: memory.md, writing_plan.yaml, paper_framing.md". The checklist file `artifacts/n500_paper_update_checklist.md` is not in the whitelist. I'll need to use the Write tool to save it directly to the artifacts directory instead.

Let me write the enhanced checklist to the artifacts directory.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "1cf45aa1-f8f7-4a6d-936c-2c3c1a01d20a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013YUU1yDFaU3UBv2tjnnTS4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 700,
      "cache_read_input_tokens": 69131,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 700
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

### Assistant

_source line 109_

`save_project_file` 只支持白名单文件。直接写入 artifacts 目录。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "0fd44c6e-86a9-4df1-97ba-1c05eccad1d7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013YUU1yDFaU3UBv2tjnnTS4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 700,
      "cache_read_input_tokens": 69131,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 700
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

_source line 110_

<details open><summary>🔧 Tool call — Write · `toolu_01NEw2e7WEw6r3jzbtKsSsvY`</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/n500_paper_update_checklist.md",
  "content": "# n=500 论文更新清单\n\n> 当 C2 n=500 实验（DeepSeek 8 conditions + Qwen 8 conditions）全部完成后，用此清单逐项替换论文中所有 n=50 数据。\n> 数据来源均在服务器 `/root/autodl-tmp/pacs/analysis_output/` 下。\n> **原则**：DeepSeek 和 Qwen 数值绝对值差 ~5×，不可混用；所有数值精确替换，不可近似。\n> **基于**：`c2_n500_paper_update_checklist.md` 增补 LLaMA 间接影响、文献完整性、C5b/C8 叙事追踪。\n\n---\n\n## 1. 样本量文本替换（全局搜索 \"50\"）\n\n| 文件 | 行号 | 当前文本 | 替换为 | 类型 |\n|------|------|---------|--------|------|\n| abstract.tex | 6 | `50 MATH-500 problems` | `500 MATH-500 problems` | 文本 |\n| methodology.tex | 10 | `50 problems stratified from MATH-500` | `500 problems from MATH-500` | 文本 |\n| results.tex | 13 | `$n{=}50$ MATH-500 problems` (Table 1 caption) | `$n{=}500$` | 文本 |\n| results.tex | 34 | `medians across 50 problems` (Table 2 caption) | `medians across 500 problems` | 文本 |\n| appendix_moved.tex | 26 | `$n{=}46$ valid problems for Qwen (vs.\\ $n{=}49$ for DeepSeek)` | n=500 后的有效样本量（需从数据计算） | 文本 |\n| appendix_moved.tex | 26 | `Four of the 50 problems are excluded` | 新排除数/总数 | 文本 |\n| appendix_moved.tex | 73 | `$n{=}49$, $10{,}000$ permutations` (Table permutation caption) | 新 n 值 | 文本 |\n| appendix_disc_analysis.tex | 45 | `$n{=}49$ paired problems for DeepSeek (1 excluded) and $n{=}46$ for Qwen (4 excluded)` | 新排除数/有效 n | 文本 |\n\n**注意**：results.tex L77/L86 中 LLaMA 的 `$n{=}49$` **不改**（LLaMA 实验仍为 n=50）。\n\n---\n\n## 2. Tables\n\n### Table 1: Aggregate II (tab:aggregate-ii) — results.tex L10-23\n\n| 行/列 | 当前值 | 数据来源 | 更新类型 |\n|--------|--------|----------|----------|\n| Importance s=0.15 | 0.39 | experiment_summary_table.json → DS imp s015 median_diff | 数值替换 |\n| Importance s=0.20 | 1.48 | experiment_summary_table.json → DS imp s020 median_diff | 数值替换 |\n| Importance s=0.25 | 7.16 | experiment_summary_table.json → DS imp s025 median_diff | 数值替换 |\n| Importance s=0.30 | 14.59 | experiment_summary_table.json → DS imp s030 median_diff | 数值替换 |\n| Random s=0.15 | 0.01 | experiment_summary_table.json → DS rand s015 median_diff | 数值替换 |\n| Random s=0.20 | −0.02 | experiment_summary_table.json → DS rand s020 median_diff | 数值替换 |\n| Random s=0.25 | 0.54 | experiment_summary_table.json → DS rand s025 median_diff | 数值替换 |\n| Random s=0.30 | 1.54 | experiment_summary_table.json → DS rand s030 median_diff | 数值替换 |\n| 正文 L8 | `$0.39$...$14.59$...37×` | 同上，37× = 14.59/0.39 需重算 | 数值+比率 |\n| 正文 L8 | `$-0.02$ to $1.54$` | random range 需从新数据取 | 数值替换 |\n\n### Table 2: Per-phase II breakdown (tab:main-results) — results.tex L31-53\n\n| 行 | II_high | II_mid | II_low | Δ | G | 数据来源 |\n|----|---------|--------|--------|---|---|----------|\n| 0.15 Imp | 0.006 | 0.081 | 0.398 | 0.39 | 69 | DS imp s015 per-phase medians |\n| 0.15 Rand | 0.093 | 0.097 | 0.103 | 0.01 | 1.1 | DS rand s015 per-phase medians |\n| 0.20 Imp | 0.015 | 0.203 | 1.496 | 1.48 | 103 | DS imp s020 per-phase medians |\n| 0.20 Rand | 0.292 | 0.350 | 0.276 | −0.02 | 0.9 | DS rand s020 per-phase medians |\n| 0.25 Imp | 0.032 | 1.118 | 7.196 | 7.16 | 222 | DS imp s025 per-phase medians |\n| 0.25 Rand | 0.818 | 0.932 | 1.363 | 0.54 | 1.7 | DS rand s025 per-phase medians |\n| 0.30 Imp | 0.053 | 2.283 | 14.639 | 14.59 | 274 | DS imp s030 per-phase medians |\n| 0.30 Rand | 2.503 | 2.592 | 4.041 | 1.54 | 1.6 | DS rand s030 per-phase medians |\n\n数据来源：`experiment_summary_table.json` 中各 condition 的 `median_low`, `median_mid`, `median_high`。\n\n### Table 3: Cohen's d (tab:cohens-d) — results.tex L108-124\n\n| 行 | DS d_z | DS Δ̃ [CI] | QW d_z | QW Δ̃ [CI] | 数据来源 |\n|----|--------|-----------|--------|-----------|----------|\n| s=0.15 (L117) | 0.44 | 0.32 [0.20, 0.47] | 0.28 | 0.05 [−0.01, 0.11]^ns | cohens_d_bf16.json / cohens_d_bf16_qwen.json |\n| s=0.20 (L118) | 0.52 | 1.15 [0.66, 1.26] | 0.55 | 0.21 [0.07, 0.40] | 同上 |\n| s=0.25 (L119) | 0.68 | 3.97 [2.83, 5.29] | 0.89 | 1.11 [0.61, 1.47] | 同上 |\n| s=0.30 (L120) | 0.80 | 9.94 [8.39, 16.65] | 1.02 | 2.62 [1.72, 3.65] | 同上 |\n\n**注意**：n=500 后 CI 会显著收窄（~√10 倍）。QW s015 的 `^ns` 标注取决于 CI 是否仍含零。\n\n### Table: LLaMA cross-arch (tab:llama-cross-arch) — results.tex L83-98\n\n**不需直接更新**（LLaMA 实验不重跑），但见 §10 间接影响。\n\n### Table: Cross-model comparison (tab:cross-model) — appendix_moved.tex L30-43\n\n| 行 | 当前值 | 数据来源 |\n|----|--------|----------|\n| DeepSeek s015/s020/s025/s030 | 0.39 / 1.48 / 7.16 / 14.59 | experiment_summary_table.json DS imp |\n| Qwen s015/s020/s025/s030 | 0.04 / 0.23 / 1.27 / 2.94 | experiment_summary_table.json QW imp |\n\n### Table: Permutation test (tab:permutation) — appendix_moved.tex L70-85\n\n| s | Observed Δ̃ | 95% CI | p_Bonf | 数据来源 |\n|---|-----------|--------|--------|----------|\n| 0.15 | 0.37 | [0.19, 0.62] | 0.0032 | permutation_test_results.json |\n| 0.20 | 0.97 | [0.69, 1.49] | <0.001 | 同上 |\n| 0.25 | 3.34 | [1.66, 6.64] | <0.001 | 同上 |\n| 0.30 | 9.85 | [6.70, 16.29] | <0.001 | 同上 |\n\n### Table: Discrimination metrics (tab:discrimination-metrics-full) — appendix_moved.tex L103-123\n\n| Model | s | ΔGini | ΔCV | 数据来源 |\n|-------|---|-------|-----|----------|\n| DS 0.15 | −0.030 | −0.56 | c4_entropy_deepseek |\n| DS 0.20 | −0.040 | −0.77 | 同上 |\n| DS 0.25 | −0.065 | −1.29 | 同上 |\n| DS 0.30 | −0.081 | −1.66 | 同上 |\n| QW 0.15 | −0.010 | −0.05 | c4_entropy_qwen |\n| QW 0.20 | −0.012 | −0.21 | 同上 |\n| QW 0.25 | −0.010 | −1.49 | 同上 |\n| QW 0.30 | −0.020 | −1.14 | 同上 |\n\n**注意**：C4 entropy 分析需要用 n=500 数据重跑 `analysis/entropy_analysis.py`。\n\n### Table: Entropy deltas (tab:entropy-deltas) — appendix_moved.tex L143-163\n\n| Model | s | ΔH | 数据来源 |\n|-------|---|----|----------|\n| DS 0.15 | −0.040 | c4_entropy_deepseek |\n| DS 0.20 | −0.047 | 同上 |\n| DS 0.25 | −0.045 | 同上 |\n| DS 0.30 | −0.044 | 同上 |\n| QW 0.15 | −0.073 | c4_entropy_qwen |\n| QW 0.20 | −0.076 | 同上 |\n| QW 0.25 | +0.045 | 同上 |\n| QW 0.30 | −0.007 | 同上 |\n\n---\n\n## 3. Figures\n\n| Figure | 文件 | 数据来源 | 需更新内容 |\n|--------|------|----------|-----------|\n| Fig 1 (fig:hero) — fig1_dose_response.pdf | results.tex L55-60 | experiment_summary_table.json G values | G 曲线数据点 + caption 中 `$69{\\times}$ to $274{\\times}$` |\n| Fig 2 — fig2_cohens_d (如存在) | 位置待定 | cohens_d_bf16.json, cohens_d_bf16_qwen.json | Cohen's d 森林图 |\n| Fig 3 (fig:crossover) — fig3_crossover.pdf | appendix_moved.tex L13-18 | experiment_summary_table.json DS s025 | 柱状图数据 + caption 中 `$5.3{\\times}$` |\n| Fig 4 (fig:permtest-forest) — fig4_bootstrap.pdf | appendix_moved.tex L87-92 | permutation_test_results.json | CI 横条 + 点估计值 |\n| Fig 5 (fig:cross-model) — fig5_crossmodel.pdf | appendix_moved.tex L46-50 | experiment_summary_table.json DS+QW imp | 双曲线数据点 + caption 中 `one-fifth` 比例 |\n\n**图表生成脚本**（服务器端）：\n- `/root/autodl-tmp/pacs/analysis/generate_paper_figures.py` — fig4, fig5\n- `/root/autodl-tmp/pacs/analysis/generate_summary_table.py` — experiment_summary_table.json\n- `/root/autodl-tmp/pacs/analysis/cross_model_analysis.py` — cross_model_analysis.json\n- `/root/autodl-tmp/pacs/analysis/compute_cohens_d.py` — cohens_d_bf16.json\n\n**更新流程**：先用 n=500 profiling 数据重跑 `generate_summary_table.py`，再重跑各分析脚本，最后重新生成所有图表 PDF。\n\n---\n\n## 4. 正文中的内联统计声明\n\n### abstract.tex\n\n| 行 | 当前文本 | 数据来源 | 类型 |\n|----|---------|----------|------|\n| 6 | `50 MATH-500 problems` | — | 文本→500 |\n| 7 | `from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$` | experiment_summary_table.json DS imp | 数值 |\n| 7 | `$d_z$ growing from $0.44$ (small) to $0.80$ (large)` | cohens_d_bf16.json | 数值 |\n| 7 | `$p < 0.005$ at all four sparsity levels` | permutation_test_results.json | 阈值判断 |\n| 8 | `7/8 conditions` | 重新统计 random PASS/FAIL | 计数 |\n| 8 | `Qwen $s{=}0.30$, $p{=}0.012$` | QW rand s030 permutation test | 数值 |\n| 8 | `$d_z{=}{-}0.04$` | QW rand s030 Cohen's d | 数值 |\n| 9 | `$\\widetilde{\\mathrm{II}} = 0.032$ vs.\\ $0.818$` | DS imp/rand s025 high-phase medians | 数值 |\n| 9 | `$\\widetilde{\\mathrm{II}} = 7.196$ vs.\\ $1.363$` | DS imp/rand s025 low-phase medians | 数值 |\n| 10 | `$d_z \\geq 0.55$` | cohens_d_bf16_qwen.json s020 | 阈值 |\n| 10 | `Spearman $\\rho = 1.0$` | cross_model_analysis.json | 数值 |\n| 10 | `gradient permutation $p = 0.043$` | cross_model_analysis.json | 数值 |\n| 10 | `${\\sim}$1/40 the absolute magnitude` | **间接影响**：LLaMA Δ̃ 不变，DS Δ̃ 变 → 比率需重算 | 比率 |\n\n### introduction.tex\n\n| 行 | 当前文本 | 数据来源 | 类型 |\n|----|---------|----------|------|\n| 14 | `$0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$` | experiment_summary_table.json DS imp | 数值 |\n| 14 | `$d_z$: $0.44 \\to 0.80$` | cohens_d_bf16.json | 数值 |\n| 14 | `Bonferroni-corrected $p < 0.005$ at all levels` | permutation_test_results.json | 阈值判断 |\n| 15 | `$d_z \\geq 0.55$` | cohens_d_bf16_qwen.json s020 | 阈值 |\n| 16 | `7/8 conditions non-significant` | 重新统计 random PASS/FAIL | 计数 |\n\n### methodology.tex\n\n| 行 | 当前文本 | 数据来源 | 类型 |\n|----|---------|----------|------|\n| 10 | `50 problems stratified from MATH-500` | — | 文本→500 |\n| 18 | `mean/median ratios up to 43:1` | 从 n=500 数据重新计算 | 数值 |\n| 22 | `$p_{\\text{Bonf}} < 0.005$ at every sparsity level` | permutation_test_results.json | 阈值判断 |\n\n### results.tex (正文段落)\n\n| 行 | 当前文本 | 数据来源 | 类型 |\n|----|---------|----------|------|\n| 8 | `$0.39$...$14.59$...37× amplification` | 新 Δ_s030 / Δ_s015 需重算 | 数值+比率 |\n| 13 | `$n{=}50$` | — | 文本→500 |\n| 29 | `$69{\\times}$ at $s{=}0.15$ to $274{\\times}$ at $s{=}0.30$` | Table 2 G 列 | 数值 |\n| 29 | `$0.006$ to $0.053$` | Table 2 II_high 列 min/max | 数值 |\n| 29 | `$G \\approx 0.9$--$1.7{\\times}$` | Table 2 random G 列 range | 数值 |\n| 34 | `50 problems` | — | 文本→500 |\n| 58 | `$69{\\times}$ to $274{\\times}$` | Table 2 G range | 数值 |\n| 66 | `$0.032$ vs.\\ $0.818$`...`$7.196$ vs.\\ $1.363$---a $5.3{\\times}$` | s025 per-phase medians | 数值+比率 |\n| 71 | `$\\Delta$ increases from $0.04$...$2.94$...${\\sim}1/5$` | experiment_summary_table.json QW imp | 数值+比率 |\n| 71 | `$d_z \\geq 0.55$; Spearman $\\rho = 1.0$; gradient permutation $p = 0.043$` | cross_model_analysis.json | 数值 |\n| 71 | `$d_z{=}0.28$, CI includes zero` | cohens_d_bf16_qwen.json s015 | 数值+判断 |\n| 77 | `$0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$` | permutation_test_results.json | 数值 |\n| 81 | `${\\sim}40{\\times}$ smaller than DeepSeek and ${\\sim}7{\\times}$ smaller than Qwen` | **间接影响**：LLaMA Δ̃ 不变，DS/QW Δ̃ 变 → 比率需重算 | 比率 |\n| 106 | `$d_z{=}0.44$ (small) to $d_z{=}0.80$ (large)` | cohens_d_bf16.json | 数值 |\n| 106 | `$d_z{=}0.28$...CI includes zero`...`$d_z \\geq 0.55$` | cohens_d_bf16_qwen.json | 数值+判断 |\n| 106 | `$d_z{=}0.89$/$1.02$ vs.\\ $0.68$/$0.80$` | cohens_d 两模型对比 | 数值 |\n\n### analysis.tex\n\n| 行 | 当前文本 | 数据来源 | 类型 |\n|----|---------|----------|------|\n| 4 | `$0.030$--$0.081$ (DeepSeek) and $0.010$--$0.020$ (Qwen)` | c4_entropy 分析 ΔGini ranges | 数值 |\n| 4 | `16 conditions` | 确认是否仍为 16 | 计数 |\n| 6 | `$\\Delta\\mathcal{H} \\in [-0.047, -0.040]$` | c4_entropy_deepseek entropy deltas | 数值 |\n| 6 | `$\\Delta\\mathcal{H} = +0.045$` | c4_entropy_qwen s025 | 数值 |\n| 6 | `22 of 30 problems` | n=500 后需重算（可能变为 ~220 of 300 等） | 计数 |\n\n### discussion.tex\n\n| 行 | 当前文本 | 数据来源 | 类型 |\n|----|---------|----------|------|\n| 5 | `$69$--$274{\\times}$` | Table 2 G range | 数值 |\n| 5 | `$\\widetilde{\\mathrm{II}} = 0.032$ vs.\\ $0.818$` | s025 high-phase | 数值 |\n| 5 | `$7.196$ vs.\\ $1.363$` | s025 low-phase | 数值 |\n| 5 | `$G \\approx 1$` | random G（确认仍成立） | 数值 |\n| 11 | `${\\sim}40{\\times}$ smaller than DeepSeek, ${\\sim}7{\\times}$ smaller than Qwen` | **间接影响**：LLaMA Δ̃ 不变，DS/QW Δ̃ 变 → 比率需重算 | 比率 |\n\n### conclusion.tex\n\n| 行 | 当前文本 | 数据来源 | 类型 |\n|----|---------|----------|------|\n| 4 | `$69{\\times}$ to $274{\\times}$` | Table 2 G range | 数值 |\n| 4 | `$d_z$: $0.44 \\to 0.80$` | cohens_d_bf16.json | 数值 |\n| 4 | `7/8 conditions non-significant` | random PASS/FAIL 重统计 | 计数 |\n| 4 | `$d_z \\geq 0.55$` | cohens_d_bf16_qwen.json s020 | 阈值 |\n| 4 | `$\\sim$1/40 the magnitude` | **间接影响**：LLaMA Δ̃ 不变，DS Δ̃ 变 → 比率需重算 | 比率 |\n\n### appendix.tex\n\n| 行 | 当前文本 | 数据来源 | 类型 |\n|----|---------|----------|------|\n| 38 | `$G_{\\times} = 58$--$241{\\times}$` | 乘法 null 下 G range 需重算 | 数值 |\n\n### appendix_moved.tex (正文段落)\n\n| 行 | 当前文本 | 数据来源 | 类型 |\n|----|---------|----------|------|\n| 11 | `$0.032$ vs.\\ $0.818$`...`$7.196$ vs.\\ $1.363$---a $5.3{\\times}$` | s025 per-phase medians | 数值+比率 |\n| 11 | `$3.9{\\times}$...$5.4{\\times}$...$5.3{\\times}$...$3.6{\\times}$` | 各 sparsity level crossover reversal magnitudes | 数值 |\n| 26 | `Four of the 50 problems are excluded` | QW excluded count n=500 | 计数 |\n| 53 | `mean $\\rho = -0.11$, $p = 0.926$` | cross_model_analysis.json | 数值 |\n| 56 | `$p = 0.012$...d_z = -0.04` | QW rand s030 | 数值 |\n| 64 | `mean/median ratios ranging from $1.2{\\times}$...$1.6{\\times}$` and `$1.1{\\times}$ to $1.4{\\times}$ for Qwen` | 从 n=500 per-problem diffs 计算 | 数值 |\n| 66 | `$99.92$th percentile...p_Bonf = 0.0032` | permutation_test_results.json s015 | 数值 |\n| 68 | `$0.37$...$9.85$...CI lower bound ($0.19 \\to 0.69 \\to 1.66 \\to 6.70$)` | permutation_test_results.json | 数值 |\n\n### appendix_disc_analysis.tex (正文段落)\n\n| 行 | 当前文本 | 数据来源 | 类型 |\n|----|---------|----------|------|\n| 4 | `$-0.031$ to $-0.073$; Qwen: $-0.019$ to $-0.045$` | random eviction Gini 变化 | 数值 |\n| 11 | `$\\widetilde{\\mathrm{II}}_{\\text{high}} < 0.06$ at $s \\leq 0.30$` | Table 2 high-phase range | 数值 |\n| 11 | `$s = 0.35$, high-phase II rises to $0.105$` | bf16_ds_imp_s035 数据 | 数值 |\n| 14 | `7/8...Qwen $s{=}0.30$, $p{=}0.012$...$d_z{=}{-}0.04$` | QW rand s030 统计 | 数值 |\n| 45 | `$n{=}49$...$n{=}46$` | 有效样本量 | 计数 |\n| 46 | `mean/median ratio ${\\sim}1.6{:}1$...mean_diff=22.94, median_diff=14.59` | s030 skewness stats | 数值 |\n| 47 | CIs: `$[0.19,\\; 0.62]$...$[0.69,\\; 1.49]$...$[1.66,\\; 6.64]$...$[6.70,\\; 16.29]$` | permutation_test_results.json | 数值 |\n| 49 | `$p{=}0.012$...$d_z{=}{-}0.04$...d=-0.035` | QW rand s030 re-bootstrap | 数值 |\n\n### appendix_results.tex\n\n| 行 | 当前文本 | 数据来源 | 类型 |\n|----|---------|----------|------|\n| 7 | `mean $\\rho = -0.11$, $p = 0.926$` | cross_model_analysis.json | 数值 |\n| 10 | `$p = 0.012$...d_z = -0.04` | QW rand s030 | 数值 |\n| 10 | `3/4 FAIL` (Qwen random) | n=500 后重统计 | 计数 |\n\n---\n\n## 5. Qwen s015 预注册决策点 (D037/D038)\n\n### 当前状态\nQwen s015: d_z=0.28, CI=[−0.006, 0.60] → **不显著**，论文采用 \"threshold narrative\"。\n\n### 决策矩阵\n\n| n=500 结果 | CI 位置 | 操作 |\n|-----------|---------|------|\n| CI 完全 > 0 | 例如 [0.05, 0.35] | **升级**：删除 `^ns` 标注，改叙事为 \"effect reliable at all four sparsity levels for both models\" |\n| CI 仍跨零 | 例如 [−0.02, 0.15] | **维持 threshold narrative**：保持当前表述不变，仅更新数值 |\n\n### CI 跨零时需更新的叙事位置（仅更新数值，保留 threshold 表述）\n\n| 文件 | 行 | 当前叙事 | 操作 |\n|------|------|---------|------|\n| abstract.tex | 10 | `replicates on Qwen2.5-7B-Instruct at $s \\geq 0.20$` | 更新 d_z 数值，保留 `$s \\geq 0.20$` |\n| introduction.tex | 15 | `$d_z \\geq 0.55$` | 更新阈值数值 |\n| results.tex | 71 | `marginal at $s{=}0.15$ ($d_z{=}0.28$, CI includes zero) but reliable at $s \\geq 0.20$ ($d_z \\geq 0.55$)` | 更新所有数值 |\n| results.tex | 117 | `0.28` & `0.05\\; $[-0.01, 0.11]$\\textsuperscript{ns}` | 更新数值，保留 `^ns` |\n| results.tex | 122 | `\\textsuperscript{ns}Marginal at $s{=}0.15$; reliable at $s \\geq 0.20$.` | 保留 |\n| conclusion.tex | 4 | `$d_z \\geq 0.55$` | 更新数值 |\n\n### CI > 0 时需更新的叙事位置（升级方案）\n\n| 文件 | 行 | 当前叙事 | 备选叙事 |\n|------|------|---------|----------|\n| abstract.tex | 10 | `at $s \\geq 0.20$` | `at all four sparsity levels` |\n| introduction.tex | 15 | `$d_z \\geq 0.55$` | `$d_z \\geq [新s015值]$`（改用 s015 值） |\n| results.tex | 71 | `marginal at $s{=}0.15$...reliable at $s \\geq 0.20$` | `reliable at all four sparsity levels ($d_z \\geq [新值]$)` |\n| results.tex | 117 | `\\textsuperscript{ns}` | 删除 `^ns` 标注 |\n| results.tex | 122 | 脚注 `Marginal at...reliable at...` | 删除或改为 `All levels significant.` |\n| conclusion.tex | 4 | `$d_z \\geq 0.55$` | `$d_z \\geq [新s015值]$` |\n\n---\n\n## 6. 附属统计量（可能变化但方向不变）\n\n以下数值的 n=500 版本大概率方向不变，但绝对值会变：\n\n| 统计量 | 当前值 | 出现位置 | 预期变化 |\n|--------|--------|---------|----------|\n| mean/median ratio | up to 43:1 | methodology.tex L18 | n=500 尾部更极端，可能变大或变小 |\n| \"7/8 conditions\" random non-significant | 7/8 | abstract L8, intro L16, conclusion L4, appendix_disc L14 | n=500 CI 更窄，QW rand s030 borderline PASS 可能翻转为 FAIL → 变成 8/8 |\n| \"3/4 FAIL\" Qwen random | 3/4 | appendix_results.tex L10 | 同上，可能变为 4/4 |\n| DS/QW magnitude ratio | ~1/5 | results.tex L71, fig5 caption | 可能略变 |\n| Crossover reversal magnitudes | 3.9×–5.4× | appendix_moved.tex L11 | 数据驱动，需重算 |\n| Spearman ρ for monotonicity | 1.0 | abstract L10, results L71 | 4 点排序，大概率仍=1.0 |\n| Gradient permutation p | 0.043 | abstract L10, results L71 | 4! = 24 种排列，最小 p=1/24≈0.042 |\n| Per-problem concordance | ρ=−0.11, p=0.926 | appendix_moved L53, appendix_results L7 | n=500 统计功效更高，可能变显著 |\n\n---\n\n## 7. 数据管道执行顺序\n\n1. **等 C2 n=500 全部 16 conditions 完成**（含 DeepSeek 8 + Qwen 8）\n2. 在服务器执行分析脚本（按依赖顺序）：\n   ```bash\n   cd /root/autodl-tmp/pacs\n   # Step 1: 生成汇总表\n   python analysis/generate_summary_table.py        # → analysis_output/experiment_summary_table.json\n\n   # Step 2: 统计分析（可并行）\n   python analysis/compute_cohens_d.py               # → analysis_output/cohens_d_bf16.json, cohens_d_bf16_qwen.json\n   python analysis/cross_model_analysis.py           # → analysis_output/cross_model_analysis.json\n   python analysis/run_permutation_test.py           # → analysis_output/permutation_test_results.json\n   python analysis/entropy_analysis.py               # → C4 entropy data (如需更新)\n\n   # Step 3: 生成图表\n   python analysis/generate_paper_figures.py         # → paper_figures/fig1-fig5 PDFs\n   ```\n3. 从 JSON 文件提取所有新数值，按本清单 §1-§4 逐项替换\n4. **关键决策点**：检查 QW s015 Cohen's d CI 是否含零 → 决定 §5 中的叙事方案\n5. 检查 QW rand s030 是否仍 PASS → 决定 \"7/8\" vs \"8/8\"（及 \"3/4\" vs \"4/4\"）\n6. 重新编译 LaTeX 验证 → `pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex`\n7. 全文搜索残留的旧数值（grep \"n=50[^0]\"、\"0.39\"、\"14.59\" 等）\n\n---\n\n## 8. 不需更新的部分\n\n- **related_work.tex** — 无实验数据\n- **background.tex** — 公式定义，无实验数据\n- **limitations.tex** — 无具体实验数值（sparsity range $s \\in \\{0.15,...,0.30\\}$ 不变；LLaMA 描述性文字无需改）\n- **methodology.tex** 公式/方法部分 — 无变化（仅 n 和统计描述需更新）\n- **results.tex L83-98** (LLaMA table) — LLaMA 实验不重跑，表内数值不变\n- **results.tex L79** (LLaMA d_z 0.19→0.34) — 不变\n- 所有 `\\cite{}` 引用 — 无变化\n\n---\n\n## 9. 更新总量统计\n\n| 类别 | 数量 |\n|------|------|\n| 样本量文本 \"50\"→\"500\" | 8 处 |\n| 表格（含 8 个表） | ~80 个单元格 |\n| 图表重新生成 | 5 个 PDF |\n| 内联统计数值 | ~60 处 |\n| 条件性叙事更新 (Qwen s015) | 6 处（两套方案） |\n| 条件性叙事更新 (7/8 vs 8/8) | 5 处 |\n| LLaMA 间接比率更新 | 4 处（§10） |\n\n---\n\n## 10. LLaMA 比较性声明间接影响（新增）\n\nLLaMA c3_llama 实验不重跑（n=50 不变），但 LLaMA 与 DS/QW 的**比率声明**会因 DS/QW 数值变化而需要重算：\n\n| 文件 | 行 | 当前声明 | 需重算内容 |\n|------|------|---------|-----------|\n| abstract.tex | 10 | `${\\sim}$1/40 the absolute magnitude` | LLaMA s030 Δ̃=0.356 不变；DS s030 Δ̃ 从 n=500 获取 → 重算比率 |\n| results.tex | 81 | `${\\sim}40{\\times}$ smaller than DeepSeek and ${\\sim}7{\\times}$ smaller than Qwen` | DS/QW 新 Δ̃ → 重算两个比率 |\n| discussion.tex | 11 | `${\\sim}40{\\times}$ smaller than DeepSeek, ${\\sim}7{\\times}$ smaller than Qwen` | 同上 |\n| conclusion.tex | 4 | `$\\sim$1/40 the magnitude` | 同 abstract L10 |\n\n**计算方法**：LLaMA s030 median Δ̃ = 0.356（不变）。新比率 = 新 DS s030 Δ̃ / 0.356 和 新 QW s030 Δ̃ / 0.356。\n\n---\n\n## 11. C5b → Future Work 叙事位置追踪（新增）\n\nC5b (phase-aware mitigation pilot) 状态 = future_work (D056)。论文中已正确定位为 future work。n=500 不影响 C5b 叙事，但确认以下位置一致性：\n\n| 文件 | 行 | 内容 | 状态 |\n|------|------|------|------|\n| discussion.tex | 8 | `phase-aware compression budget` 作为 future direction | ✓ 无需改 |\n| appendix_disc_analysis.tex | 28 | `Scaling experiments are future work.` (REBUTTAL comment) | ✓ 无需改 |\n| appendix_disc_analysis.tex | 57 | `confirming this is future work` (REBUTTAL comment) | ✓ 无需改 |\n| appendix_disc_analysis.tex | 62 | `Phase-gated controllers are explicitly scoped as future work` (REBUTTAL comment) | ✓ 无需改 |\n\n**如果 n=500 中 mid-phase 数据给 C5b 提供新 evidence**：可在 discussion.tex L8 后插入一句 pilot 结果简述。但这取决于 n=500 分析后的判断，不在机械替换范围内。\n\n---\n\n## 12. C8 (LLaMA cross-architecture) 限定语检查（新增）\n\nC8 状态 = partially_confirmed (D060)。论文中已使用恰当限定语。n=500 不影响 LLaMA 数据，但确认限定语位置：\n\n| 文件 | 行 | 限定语 | 状态 |\n|------|------|--------|------|\n| abstract.tex | 10 | `suggests cross-architecture generalization, though at ~1/40 magnitude and with substantially weaker interaction` | ✓ 恰当 |\n| results.tex | 79 | `The qualitative pattern replicates` | ✓ 恰当 |\n| results.tex | 81 | `qualitatively consistent...though the interaction magnitude is substantially weaker` | ✓ 恰当 |\n| discussion.tex | 11 | `provides partial support for the qualitative pattern` | ✓ 恰当 |\n| conclusion.tex | 4 | `qualitatively consistent but substantially weaker trend` | ✓ 恰当 |\n| limitations.tex | 2 | `directional pattern is qualitatively consistent but the interaction magnitude is substantially weaker` | ✓ 恰当 |\n\n**无需修改**，除非 n=500 DS/QW 结果导致比率声明变化（见 §10）。\n\n---\n\n## 13. 文献完整性检查（新增）\n\n### literature_map.yaml 缺口\n\n| 缺失论文 | arXiv | 类别 | 为何需要 |\n|----------|-------|------|---------|\n| **HIES** | 2510.13832 (Oct 2025) | method-component / supporting evidence | paper_framing.md RC5/RC6 中引用了 HIES 的 importance score collapse 作为 discrimination collapse 的独立佐证。但 HIES 未收录在 literature_map.yaml 中。**需补录。** |\n\n### 已有文献完整性确认\n\n- **direct-competitor** (3): SparK ✓, GRASPrune ✓, DefensiveKV ✓ — 完整\n- **phase-aware 单轴** (4): ThinKV ✓, PagedEviction ✓, R-KV ✓, Twilight ✓ — 完整\n- **compound compression** (4): SLiM ✓, UniComp ✓, compression-ordering ✓, EVICPRESS ✓ — 完整\n- **phase transition / mechanism** (3): Physics of KV Cache ✓, phase-transition-pruning-thermo ✓, decision-repr-transition ✓ — 完整\n- **importance fragility** (3): DefensiveKV ✓, greedy-bias ✓, RetentiveKV ✓ — 完整，**但缺 HIES**\n- **adaptive controllers** (4): Ada-KV ✓, SOL ✓, LKV ✓, LAVa ✓ — 完整\n- **reasoning dynamics** (2): thinking-tokens-MI ✓, token-budget-aware ✓ — 完整\n\n### 近 2 周新论文扫描建议\n\nliterature_map.yaml 最后扫描日期 2026-05-14。距投稿 2026-05-25 还有 11 天。建议在 Day 9 (2026-05-23) 做最终扫描，重点关注：\n- arXiv cs.CL + cs.LG 中 \"compound sparsity\" / \"KV cache pruning\" / \"attention head pruning\" 相关\n- 特别注意 2026-05 新出的 ICML 2026 camera-ready 版本是否有新 compound compression 工作\n\n---\n\n## 14. 残留旧值清扫 grep 命令（更新后执行）\n\n```bash\ncd /path/to/paper/\n# 以下命令在所有 .tex 文件完成替换后执行\ngrep -n \"n=50[^0]\" *.tex           # 应只剩 LLaMA 的 n=49\ngrep -n \"\\\\b0\\\\.39\\\\b\" *.tex        # 应为 0\ngrep -n \"14\\\\.59\" *.tex             # 应为 0\ngrep -n \"\\\\b69\\\\b\" *.tex            # 应为 0（注意排除年份如 2069）\ngrep -n \"\\\\b274\\\\b\" *.tex           # 应为 0\ngrep -n \"\\\\b0\\\\.44\\\\b\" *.tex        # 应为 0（DS d_z）\ngrep -n \"\\\\b0\\\\.80\\\\b\" *.tex        # 应为 0（DS d_z）\ngrep -n \"7/8\" *.tex                 # 应为 0（除非仍为 7/8）\n```\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "5c470b48-c08a-4b83-aafc-47fbdd920992",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013YUU1yDFaU3UBv2tjnnTS4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 700,
      "cache_read_input_tokens": 69131,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 700
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

_source line 111 · 2026-05-14T20:49:28.195Z_

<details><summary>↩ Tool result · `toolu_01NEw2e7WEw6r3jzbtKsSsvY`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/n500_paper_update_checklist.md
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "4b32bebf-67ec-4767-b5e3-a3153099bc51",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/n500_paper_update_checklist.md",
    "content": "# n=500 论文更新清单\n\n> 当 C2 n=500 实验（DeepSeek 8 conditions + Qwen 8 conditions）全部完成后，用此清单逐项替换论文中所有 n=50 数据。\n> 数据来源均在服务器 `/root/autodl-tmp/pacs/analysis_output/` 下。\n> **原则**：DeepSeek 和 Qwen 数值绝对值差 ~5×，不可混用；所有数值精确替换，不可近似。\n> **基于**：`c2_n500_paper_update_checklist.md` 增补 LLaMA 间接影响、文献完整性、C5b/C8 叙事追踪。\n\n---\n\n## 1. 样本量文本替换（全局搜索 \"50\"）\n\n| 文件 | 行号 | 当前文本 | 替换为 | 类型 |\n|------|------|---------|--------|------|\n| abstract.tex | 6 | `50 MATH-500 problems` | `500 MATH-500 problems` | 文本 |\n| methodology.tex | 10 | `50 problems stratified from MATH-500` | `500 problems from MATH-500` | 文本 |\n| results.tex | 13 | `$n{=}50$ MATH-500 problems` (Table 1 caption) | `$n{=}500$` | 文本 |\n| results.tex | 34 | `medians across 50 problems` (Table 2 caption) | `medians across 500 problems` | 文本 |\n| appendix_moved.tex | 26 | `$n{=}46$ valid problems for Qwen (vs.\\ $n{=}49$ for DeepSeek)` | n=500 后的有效样本量（需从数据计算） | 文本 |\n| appendix_moved.tex | 26 | `Four of the 50 problems are excluded` | 新排除数/总数 | 文本 |\n| appendix_moved.tex | 73 | `$n{=}49$, $10{,}000$ permutations` (Table permutation caption) | 新 n 值 | 文本 |\n| appendix_disc_analysis.tex | 45 | `$n{=}49$ paired problems for DeepSeek (1 excluded) and $n{=}46$ for Qwen (4 excluded)` | 新排除数/有效 n | 文本 |\n\n**注意**：results.tex L77/L86 中 LLaMA 的 `$n{=}49$` **不改**（LLaMA 实验仍为 n=50）。\n\n---\n\n## 2. Tables\n\n### Table 1: Aggregate II (tab:aggregate-ii) — results.tex L10-23\n\n| 行/列 | 当前值 | 数据来源 | 更新类型 |\n|--------|--------|----------|----------|\n| Importance s=0.15 | 0.39 | experiment_summary_table.json → DS imp s015 median_diff | 数值替换 |\n| Importance s=0.20 | 1.48 | experiment_summary_table.json → DS imp s020 median_diff | 数值替换 |\n| Importance s=0.25 | 7.16 | experiment_summary_table.json → DS imp s025 median_diff | 数值替换 |\n| Importance s=0.30 | 14.59 | experiment_summary_table.json → DS imp s030 median_diff | 数值替换 |\n| Random s=0.15 | 0.01 | experiment_summary_table.json → DS rand s015 median_diff | 数值替换 |\n| Random s=0.20 | −0.02 | experiment_summary_table.json → DS rand s020 median_diff | 数值替换 |\n| Random s=0.25 | 0.54 | experiment_summary_table.json → DS rand s025 median_diff | 数值替换 |\n| Random s=0.30 | 1.54 | experiment_summary_table.json → DS rand s030 median_diff | 数值替换 |\n| 正文 L8 | `$0.39$...$14.59$...37×` | 同上，37× = 14.59/0.39 需重算 | 数值+比率 |\n| 正文 L8 | `$-0.02$ to $1.54$` | random range 需从新数据取 | 数值替换 |\n\n### Table 2: Per-phase II breakdown (tab:main-results) — results.tex L31-53\n\n| 行 | II_high | II_mid | II_low | Δ | G | 数据来源 |\n|----|---------|--------|--------|---|---|----------|\n| 0.15 Imp | 0.006 | 0.081 | 0.398 | 0.39 | 69 | DS imp s015 per-phase medians |\n| 0.15 Rand | 0.093 | 0.097 | 0.103 | 0.01 | 1.1 | DS rand s015 per-phase medians |\n| 0.20 Imp | 0.015 | 0.203 | 1.496 | 1.48 | 103 | DS imp s020 per-phase medians |\n| 0.20 Rand | 0.292 | 0.350 | 0.276 | −0.02 | 0.9 | DS rand s020 per-phase medians |\n| 0.25 Imp | 0.032 | 1.118 | 7.196 | 7.16 | 222 | DS imp s025 per-phase medians |\n| 0.25 Rand | 0.818 | 0.932 | 1.363 | 0.54 | 1.7 | DS rand s025 per-phase medians |\n| 0.30 Imp | 0.053 | 2.283 | 14.639 | 14.59 | 274 | DS imp s030 per-phase medians |\n| 0.30 Rand | 2.503 | 2.592 | 4.041 | 1.54 | 1.6 | DS rand s030 per-phase medians |\n\n数据来源：`experiment_summary_table.json` 中各 condition 的 `median_low`, `median_mid`, `median_high`。\n\n### Table 3: Cohen's d (tab:cohens-d) — results.tex L108-124\n\n| 行 | DS d_z | DS Δ̃ [CI] | QW d_z | QW Δ̃ [CI] | 数据来源 |\n|----|--------|-----------|--------|-----------|----------|\n| s=0.15 (L117) | 0.44 | 0.32 [0.20, 0.47] | 0.28 | 0.05 [−0.01, 0.11]^ns | cohens_d_bf16.json / cohens_d_bf16_qwen.json |\n| s=0.20 (L118) | 0.52 | 1.15 [0.66, 1.26] | 0.55 | 0.21 [0.07, 0.40] | 同上 |\n| s=0.25 (L119) | 0.68 | 3.97 [2.83, 5.29] | 0.89 | 1.11 [0.61, 1.47] | 同上 |\n| s=0.30 (L120) | 0.80 | 9.94 [8.39, 16.65] | 1.02 | 2.62 [1.72, 3.65] | 同上 |\n\n**注意**：n=500 后 CI 会显著收窄（~√10 倍）。QW s015 的 `^ns` 标注取决于 CI 是否仍含零。\n\n### Table: LLaMA cross-arch (tab:llama-cross-arch) — results.tex L83-98\n\n**不需直接更新**（LLaMA 实验不重跑），但见 §10 间接影响。\n\n### Table: Cross-model comparison (tab:cross-model) — appendix_moved.tex L30-43\n\n| 行 | 当前值 | 数据来源 |\n|----|--------|----------|\n| DeepSeek s015/s020/s025/s030 | 0.39 / 1.48 / 7.16 / 14.59 | experiment_summary_table.json DS imp |\n| Qwen s015/s020/s025/s030 | 0.04 / 0.23 / 1.27 / 2.94 | experiment_summary_table.json QW imp |\n\n### Table: Permutation test (tab:permutation) — appendix_moved.tex L70-85\n\n| s | Observed Δ̃ | 95% CI | p_Bonf | 数据来源 |\n|---|-----------|--------|--------|----------|\n| 0.15 | 0.37 | [0.19, 0.62] | 0.0032 | permutation_test_results.json |\n| 0.20 | 0.97 | [0.69, 1.49] | <0.001 | 同上 |\n| 0.25 | 3.34 | [1.66, 6.64] | <0.001 | 同上 |\n| 0.30 | 9.85 | [6.70, 16.29] | <0.001 | 同上 |\n\n### Table: Discrimination metrics (tab:discrimination-metrics-full) — appendix_moved.tex L103-123\n\n| Model | s | ΔGini | ΔCV | 数据来源 |\n|-------|---|-------|-----|----------|\n| DS 0.15 | −0.030 | −0.56 | c4_entropy_deepseek |\n| DS 0.20 | −0.040 | −0.77 | 同上 |\n| DS 0.25 | −0.065 | −1.29 | 同上 |\n| DS 0.30 | −0.081 | −1.66 | 同上 |\n| QW 0.15 | −0.010 | −0.05 | c4_entropy_qwen |\n| QW 0.20 | −0.012 | −0.21 | 同上 |\n| QW 0.25 | −0.010 | −1.49 | 同上 |\n| QW 0.30 | −0.020 | −1.14 | 同上 |\n\n**注意**：C4 entropy 分析需要用 n=500 数据重跑 `analysis/entropy_analysis.py`。\n\n### Table: Entropy deltas (tab:entropy-deltas) — appendix_moved.tex L143-163\n\n| Model | s | ΔH | 数据来源 |\n|-------|---|----|----------|\n| DS 0.15 | −0.040 | c4_entropy_deepseek |\n| DS 0.20 | −0.047 | 同上 |\n| DS 0.25 | −0.045 | 同上 |\n| DS 0.30 | −0.044 | 同上 |\n| QW 0.15 | −0.073 | c4_entropy_qwen |\n| QW 0.20 | −0.076 | 同上 |\n| QW 0.25 | +0.045 | 同上 |\n| QW 0.30 | −0.007 | 同上 |\n\n---\n\n## 3. Figures\n\n| Figure | 文件 | 数据来源 | 需更新内容 |\n|--------|------|----------|-----------|\n| Fig 1 (fig:hero) — fig1_dose_response.pdf | results.tex L55-60 | experiment_summary_table.json G values | G 曲线数据点 + caption 中 `$69{\\times}$ to $274{\\times}$` |\n| Fig 2 — fig2_cohens_d (如存在) | 位置待定 | cohens_d_bf16.json, cohens_d_bf16_qwen.json | Cohen's d 森林图 |\n| Fig 3 (fig:crossover) — fig3_crossover.pdf | appendix_moved.tex L13-18 | experiment_summary_table.json DS s025 | 柱状图数据 + caption 中 `$5.3{\\times}$` |\n| Fig 4 (fig:permtest-forest) — fig4_bootstrap.pdf | appendix_moved.tex L87-92 | permutation_test_results.json | CI 横条 + 点估计值 |\n| Fig 5 (fig:cross-model) — fig5_crossmodel.pdf | appendix_moved.tex L46-50 | experiment_summary_table.json DS+QW imp | 双曲线数据点 + caption 中 `one-fifth` 比例 |\n\n**图表生成脚本**（服务器端）：\n- `/root/autodl-tmp/pacs/analysis/generate_paper_figures.py` — fig4, fig5\n- `/root/autodl-tmp/pacs/analysis/generate_summary_table.py` — experiment_summary_table.json\n- `/root/autodl-tmp/pacs/analysis/cross_model_analysis.py` — cross_model_analysis.json\n- `/root/autodl-tmp/pacs/analysis/compute_cohens_d.py` — cohens_d_bf16.json\n\n**更新流程**：先用 n=500 profiling 数据重跑 `generate_summary_table.py`，再重跑各分析脚本，最后重新生成所有图表 PDF。\n\n---\n\n## 4. 正文中的内联统计声明\n\n### abstract.tex\n\n| 行 | 当前文本 | 数据来源 | 类型 |\n|----|---------|----------|------|\n| 6 | `50 MATH-500 problems` | — | 文本→500 |\n| 7 | `from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$` | experiment_summary_table.json DS imp | 数值 |\n| 7 | `$d_z$ growing from $0.44$ (small) to $0.80$ (large)` | cohens_d_bf16.json | 数值 |\n| 7 | `$p < 0.005$ at all four sparsity levels` | permutation_test_results.json | 阈值判断 |\n| 8 | `7/8 conditions` | 重新统计 random PASS/FAIL | 计数 |\n| 8 | `Qwen $s{=}0.30$, $p{=}0.012$` | QW rand s030 permutation test | 数值 |\n| 8 | `$d_z{=}{-}0.04$` | QW rand s030 Cohen's d | 数值 |\n| 9 | `$\\widetilde{\\mathrm{II}} = 0.032$ vs.\\ $0.818$` | DS imp/rand s025 high-phase medians | 数值 |\n| 9 | `$\\widetilde{\\mathrm{II}} = 7.196$ vs.\\ $1.363$` | DS imp/rand s025 low-phase medians | 数值 |\n| 10 | `$d_z \\geq 0.55$` | cohens_d_bf16_qwen.json s020 | 阈值 |\n| 10 | `Spearman $\\rho = 1.0$` | cross_model_analysis.json | 数值 |\n| 10 | `gradient permutation $p = 0.043$` | cross_model_analysis.json | 数值 |\n| 10 | `${\\sim}$1/40 the absolute magnitude` | **间接影响**：LLaMA Δ̃ 不变，DS Δ̃ 变 → 比率需重算 | 比率 |\n\n### introduction.tex\n\n| 行 | 当前文本 | 数据来源 | 类型 |\n|----|---------|----------|------|\n| 14 | `$0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$` | experiment_summary_table.json DS imp | 数值 |\n| 14 | `$d_z$: $0.44 \\to 0.80$` | cohens_d_bf16.json | 数值 |\n| 14 | `Bonferroni-corrected $p < 0.005$ at all levels` | permutation_test_results.json | 阈值判断 |\n| 15 | `$d_z \\geq 0.55$` | cohens_d_bf16_qwen.json s020 | 阈值 |\n| 16 | `7/8 conditions non-significant` | 重新统计 random PASS/FAIL | 计数 |\n\n### methodology.tex\n\n| 行 | 当前文本 | 数据来源 | 类型 |\n|----|---------|----------|------|\n| 10 | `50 problems stratified from MATH-500` | — | 文本→500 |\n| 18 | `mean/median ratios up to 43:1` | 从 n=500 数据重新计算 | 数值 |\n| 22 | `$p_{\\text{Bonf}} < 0.005$ at every sparsity level` | permutation_test_results.json | 阈值判断 |\n\n### results.tex (正文段落)\n\n| 行 | 当前文本 | 数据来源 | 类型 |\n|----|---------|----------|------|\n| 8 | `$0.39$...$14.59$...37× amplification` | 新 Δ_s030 / Δ_s015 需重算 | 数值+比率 |\n| 13 | `$n{=}50$` | — | 文本→500 |\n| 29 | `$69{\\times}$ at $s{=}0.15$ to $274{\\times}$ at $s{=}0.30$` | Table 2 G 列 | 数值 |\n| 29 | `$0.006$ to $0.053$` | Table 2 II_high 列 min/max | 数值 |\n| 29 | `$G \\approx 0.9$--$1.7{\\times}$` | Table 2 random G 列 range | 数值 |\n| 34 | `50 problems` | — | 文本→500 |\n| 58 | `$69{\\times}$ to $274{\\times}$` | Table 2 G range | 数值 |\n| 66 | `$0.032$ vs.\\ $0.818$`...`$7.196$ vs.\\ $1.363$---a $5.3{\\times}$` | s025 per-phase medians | 数值+比率 |\n| 71 | `$\\Delta$ increases from $0.04$...$2.94$...${\\sim}1/5$` | experiment_summary_table.json QW imp | 数值+比率 |\n| 71 | `$d_z \\geq 0.55$; Spearman $\\rho = 1.0$; gradient permutation $p = 0.043$` | cross_model_analysis.json | 数值 |\n| 71 | `$d_z{=}0.28$, CI includes zero` | cohens_d_bf16_qwen.json s015 | 数值+判断 |\n| 77 | `$0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$` | permutation_test_results.json | 数值 |\n| 81 | `${\\sim}40{\\times}$ smaller than DeepSeek and ${\\sim}7{\\times}$ smaller than Qwen` | **间接影响**：LLaMA Δ̃ 不变，DS/QW Δ̃ 变 → 比率需重算 | 比率 |\n| 106 | `$d_z{=}0.44$ (small) to $d_z{=}0.80$ (large)` | cohens_d_bf16.json | 数值 |\n| 106 | `$d_z{=}0.28$...CI includes zero`...`$d_z \\geq 0.55$` | cohens_d_bf16_qwen.json | 数值+判断 |\n| 106 | `$d_z{=}0.89$/$1.02$ vs.\\ $0.68$/$0.80$` | cohens_d 两模型对比 | 数值 |\n\n### analysis.tex\n\n| 行 | 当前文本 | 数据来源 | 类型 |\n|----|---------|----------|------|\n| 4 | `$0.030$--$0.081$ (DeepSeek) and $0.010$--$0.020$ (Qwen)` | c4_entropy 分析 ΔGini ranges | 数值 |\n| 4 | `16 conditions` | 确认是否仍为 16 | 计数 |\n| 6 | `$\\Delta\\mathcal{H} \\in [-0.047, -0.040]$` | c4_entropy_deepseek entropy deltas | 数值 |\n| 6 | `$\\Delta\\mathcal{H} = +0.045$` | c4_entropy_qwen s025 | 数值 |\n| 6 | `22 of 30 problems` | n=500 后需重算（可能变为 ~220 of 300 等） | 计数 |\n\n### discussion.tex\n\n| 行 | 当前文本 | 数据来源 | 类型 |\n|----|---------|----------|------|\n| 5 | `$69$--$274{\\times}$` | Table 2 G range | 数值 |\n| 5 | `$\\widetilde{\\mathrm{II}} = 0.032$ vs.\\ $0.818$` | s025 high-phase | 数值 |\n| 5 | `$7.196$ vs.\\ $1.363$` | s025 low-phase | 数值 |\n| 5 | `$G \\approx 1$` | random G（确认仍成立） | 数值 |\n| 11 | `${\\sim}40{\\times}$ smaller than DeepSeek, ${\\sim}7{\\times}$ smaller than Qwen` | **间接影响**：LLaMA Δ̃ 不变，DS/QW Δ̃ 变 → 比率需重算 | 比率 |\n\n### conclusion.tex\n\n| 行 | 当前文本 | 数据来源 | 类型 |\n|----|---------|----------|------|\n| 4 | `$69{\\times}$ to $274{\\times}$` | Table 2 G range | 数值 |\n| 4 | `$d_z$: $0.44 \\to 0.80$` | cohens_d_bf16.json | 数值 |\n| 4 | `7/8 conditions non-significant` | random PASS/FAIL 重统计 | 计数 |\n| 4 | `$d_z \\geq 0.55$` | cohens_d_bf16_qwen.json s020 | 阈值 |\n| 4 | `$\\sim$1/40 the magnitude` | **间接影响**：LLaMA Δ̃ 不变，DS Δ̃ 变 → 比率需重算 | 比率 |\n\n### appendix.tex\n\n| 行 | 当前文本 | 数据来源 | 类型 |\n|----|---------|----------|------|\n| 38 | `$G_{\\times} = 58$--$241{\\times}$` | 乘法 null 下 G range 需重算 | 数值 |\n\n### appendix_moved.tex (正文段落)\n\n| 行 | 当前文本 | 数据来源 | 类型 |\n|----|---------|----------|------|\n| 11 | `$0.032$ vs.\\ $0.818$`...`$7.196$ vs.\\ $1.363$---a $5.3{\\times}$` | s025 per-phase medians | 数值+比率 |\n| 11 | `$3.9{\\times}$...$5.4{\\times}$...$5.3{\\times}$...$3.6{\\times}$` | 各 sparsity level crossover reversal magnitudes | 数值 |\n| 26 | `Four of the 50 problems are excluded` | QW excluded count n=500 | 计数 |\n| 53 | `mean $\\rho = -0.11$, $p = 0.926$` | cross_model_analysis.json | 数值 |\n| 56 | `$p = 0.012$...d_z = -0.04` | QW rand s030 | 数值 |\n| 64 | `mean/median ratios ranging from $1.2{\\times}$...$1.6{\\times}$` and `$1.1{\\times}$ to $1.4{\\times}$ for Qwen` | 从 n=500 per-problem diffs 计算 | 数值 |\n| 66 | `$99.92$th percentile...p_Bonf = 0.0032` | permutation_test_results.json s015 | 数值 |\n| 68 | `$0.37$...$9.85$...CI lower bound ($0.19 \\to 0.69 \\to 1.66 \\to 6.70$)` | permutation_test_results.json | 数值 |\n\n### appendix_disc_analysis.tex (正文段落)\n\n| 行 | 当前文本 | 数据来源 | 类型 |\n|----|---------|----------|------|\n| 4 | `$-0.031$ to $-0.073$; Qwen: $-0.019$ to $-0.045$` | random eviction Gini 变化 | 数值 |\n| 11 | `$\\widetilde{\\mathrm{II}}_{\\text{high}} < 0.06$ at $s \\leq 0.30$` | Table 2 high-phase range | 数值 |\n| 11 | `$s = 0.35$, high-phase II rises to $0.105$` | bf16_ds_imp_s035 数据 | 数值 |\n| 14 | `7/8...Qwen $s{=}0.30$, $p{=}0.012$...$d_z{=}{-}0.04$` | QW rand s030 统计 | 数值 |\n| 45 | `$n{=}49$...$n{=}46$` | 有效样本量 | 计数 |\n| 46 | `mean/median ratio ${\\sim}1.6{:}1$...mean_diff=22.94, median_diff=14.59` | s030 skewness stats | 数值 |\n| 47 | CIs: `$[0.19,\\; 0.62]$...$[0.69,\\; 1.49]$...$[1.66,\\; 6.64]$...$[6.70,\\; 16.29]$` | permutation_test_results.json | 数值 |\n| 49 | `$p{=}0.012$...$d_z{=}{-}0.04$...d=-0.035` | QW rand s030 re-bootstrap | 数值 |\n\n### appendix_results.tex\n\n| 行 | 当前文本 | 数据来源 | 类型 |\n|----|---------|----------|------|\n| 7 | `mean $\\rho = -0.11$, $p = 0.926$` | cross_model_analysis.json | 数值 |\n| 10 | `$p = 0.012$...d_z = -0.04` | QW rand s030 | 数值 |\n| 10 | `3/4 FAIL` (Qwen random) | n=500 后重统计 | 计数 |\n\n---\n\n## 5. Qwen s015 预注册决策点 (D037/D038)\n\n### 当前状态\nQwen s015: d_z=0.28, CI=[−0.006, 0.60] → **不显著**，论文采用 \"threshold narrative\"。\n\n### 决策矩阵\n\n| n=500 结果 | CI 位置 | 操作 |\n|-----------|---------|------|\n| CI 完全 > 0 | 例如 [0.05, 0.35] | **升级**：删除 `^ns` 标注，改叙事为 \"effect reliable at all four sparsity levels for both models\" |\n| CI 仍跨零 | 例如 [−0.02, 0.15] | **维持 threshold narrative**：保持当前表述不变，仅更新数值 |\n\n### CI 跨零时需更新的叙事位置（仅更新数值，保留 threshold 表述）\n\n| 文件 | 行 | 当前叙事 | 操作 |\n|------|------|---------|------|\n| abstract.tex | 10 | `replicates on Qwen2.5-7B-Instruct at $s \\geq 0.20$` | 更新 d_z 数值，保留 `$s \\geq 0.20$` |\n| introduction.tex | 15 | `$d_z \\geq 0.55$` | 更新阈值数值 |\n| results.tex | 71 | `marginal at $s{=}0.15$ ($d_z{=}0.28$, CI includes zero) but reliable at $s \\geq 0.20$ ($d_z \\geq 0.55$)` | 更新所有数值 |\n| results.tex | 117 | `0.28` & `0.05\\; $[-0.01, 0.11]$\\textsuperscript{ns}` | 更新数值，保留 `^ns` |\n| results.tex | 122 | `\\textsuperscript{ns}Marginal at $s{=}0.15$; reliable at $s \\geq 0.20$.` | 保留 |\n| conclusion.tex | 4 | `$d_z \\geq 0.55$` | 更新数值 |\n\n### CI > 0 时需更新的叙事位置（升级方案）\n\n| 文件 | 行 | 当前叙事 | 备选叙事 |\n|------|------|---------|----------|\n| abstract.tex | 10 | `at $s \\geq 0.20$` | `at all four sparsity levels` |\n| introduction.tex | 15 | `$d_z \\geq 0.55$` | `$d_z \\geq [新s015值]$`（改用 s015 值） |\n| results.tex | 71 | `marginal at $s{=}0.15$...reliable at $s \\geq 0.20$` | `reliable at all four sparsity levels ($d_z \\geq [新值]$)` |\n| results.tex | 117 | `\\textsuperscript{ns}` | 删除 `^ns` 标注 |\n| results.tex | 122 | 脚注 `Marginal at...reliable at...` | 删除或改为 `All levels significant.` |\n| conclusion.tex | 4 | `$d_z \\geq 0.55$` | `$d_z \\geq [新s015值]$` |\n\n---\n\n## 6. 附属统计量（可能变化但方向不变）\n\n以下数值的 n=500 版本大概率方向不变，但绝对值会变：\n\n| 统计量 | 当前值 | 出现位置 | 预期变化 |\n|--------|--------|---------|----------|\n| mean/median ratio | up to 43:1 | methodology.tex L18 | n=500 尾部更极端，可能变大或变小 |\n| \"7/8 conditions\" random non-significant | 7/8 | abstract L8, intro L16, conclusion L4, appendix_disc L14 | n=500 CI 更窄，QW rand s030 borderline PASS 可能翻转为 FAIL → 变成 8/8 |\n| \"3/4 FAIL\" Qwen random | 3/4 | appendix_results.tex L10 | 同上，可能变为 4/4 |\n| DS/QW magnitude ratio | ~1/5 | results.tex L71, fig5 caption | 可能略变 |\n| Crossover reversal magnitudes | 3.9×–5.4× | appendix_moved.tex L11 | 数据驱动，需重算 |\n| Spearman ρ for monotonicity | 1.0 | abstract L10, results L71 | 4 点排序，大概率仍=1.0 |\n| Gradient permutation p | 0.043 | abstract L10, results L71 | 4! = 24 种排列，最小 p=1/24≈0.042 |\n| Per-problem concordance | ρ=−0.11, p=0.926 | appendix_moved L53, appendix_results L7 | n=500 统计功效更高，可能变显著 |\n\n---\n\n## 7. 数据管道执行顺序\n\n1. **等 C2 n=500 全部 16 conditions 完成**（含 DeepSeek 8 + Qwen 8）\n2. 在服务器执行分析脚本（按依赖顺序）：\n   ```bash\n   cd /root/autodl-tmp/pacs\n   # Step 1: 生成汇总表\n   python analysis/generate_summary_table.py        # → analysis_output/experiment_summary_table.json\n\n   # Step 2: 统计分析（可并行）\n   python analysis/compute_cohens_d.py               # → analysis_output/cohens_d_bf16.json, cohens_d_bf16_qwen.json\n   python analysis/cross_model_analysis.py           # → analysis_output/cross_model_analysis.json\n   python analysis/run_permutation_test.py           # → analysis_output/permutation_test_results.json\n   python analysis/entropy_analysis.py               # → C4 entropy data (如需更新)\n\n   # Step 3: 生成图表\n   python analysis/generate_paper_figures.py         # → paper_figures/fig1-fig5 PDFs\n   ```\n3. 从 JSON 文件提取所有新数值，按本清单 §1-§4 逐项替换\n4. **关键决策点**：检查 QW s015 Cohen's d CI 是否含零 → 决定 §5 中的叙事方案\n5. 检查 QW rand s030 是否仍 PASS → 决定 \"7/8\" vs \"8/8\"（及 \"3/4\" vs \"4/4\"）\n6. 重新编译 LaTeX 验证 → `pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex`\n7. 全文搜索残留的旧数值（grep \"n=50[^0]\"、\"0.39\"、\"14.59\" 等）\n\n---\n\n## 8. 不需更新的部分\n\n- **related_work.tex** — 无实验数据\n- **background.tex** — 公式定义，无实验数据\n- **limitations.tex** — 无具体实验数值（sparsity range $s \\in \\{0.15,...,0.30\\}$ 不变；LLaMA 描述性文字无需改）\n- **methodology.tex** 公式/方法部分 — 无变化（仅 n 和统计描述需更新）\n- **results.tex L83-98** (LLaMA table) — LLaMA 实验不重跑，表内数值不变\n- **results.tex L79** (LLaMA d_z 0.19→0.34) — 不变\n- 所有 `\\cite{}` 引用 — 无变化\n\n---\n\n## 9. 更新总量统计\n\n| 类别 | 数量 |\n|------|------|\n| 样本量文本 \"50\"→\"500\" | 8 处 |\n| 表格（含 8 个表） | ~80 个单元格 |\n| 图表重新生成 | 5 个 PDF |\n| 内联统计数值 | ~60 处 |\n| 条件性叙事更新 (Qwen s015) | 6 处（两套方案） |\n| 条件性叙事更新 (7/8 vs 8/8) | 5 处 |\n| LLaMA 间接比率更新 | 4 处（§10） |\n\n---\n\n## 10. LLaMA 比较性声明间接影响（新增）\n\nLLaMA c3_llama 实验不重跑（n=50 不变），但 LLaMA 与 DS/QW 的**比率声明**会因 DS/QW 数值变化而需要重算：\n\n| 文件 | 行 | 当前声明 | 需重算内容 |\n|------|------|---------|-----------|\n| abstract.tex | 10 | `${\\sim}$1/40 the absolute magnitude` | LLaMA s030 Δ̃=0.356 不变；DS s030 Δ̃ 从 n=500 获取 → 重算比率 |\n| results.tex | 81 | `${\\sim}40{\\times}$ smaller than DeepSeek and ${\\sim}7{\\times}$ smaller than Qwen` | DS/QW 新 Δ̃ → 重算两个比率 |\n| discussion.tex | 11 | `${\\sim}40{\\times}$ smaller than DeepSeek, ${\\sim}7{\\times}$ smaller than Qwen` | 同上 |\n| conclusion.tex | 4 | `$\\sim$1/40 the magnitude` | 同 abstract L10 |\n\n**计算方法**：LLaMA s030 median Δ̃ = 0.356（不变）。新比率 = 新 DS s030 Δ̃ / 0.356 和 新 QW s030 Δ̃ / 0.356。\n\n---\n\n## 11. C5b → Future Work 叙事位置追踪（新增）\n\nC5b (phase-aware mitigation pilot) 状态 = future_work (D056)。论文中已正确定位为 future work。n=500 不影响 C5b 叙事，但确认以下位置一致性：\n\n| 文件 | 行 | 内容 | 状态 |\n|------|------|------|------|\n| discussion.tex | 8 | `phase-aware compression budget` 作为 future direction | ✓ 无需改 |\n| appendix_disc_analysis.tex | 28 | `Scaling experiments are future work.` (REBUTTAL comment) | ✓ 无需改 |\n| appendix_disc_analysis.tex | 57 | `confirming this is future work` (REBUTTAL comment) | ✓ 无需改 |\n| appendix_disc_analysis.tex | 62 | `Phase-gated controllers are explicitly scoped as future work` (REBUTTAL comment) | ✓ 无需改 |\n\n**如果 n=500 中 mid-phase 数据给 C5b 提供新 evidence**：可在 discussion.tex L8 后插入一句 pilot 结果简述。但这取决于 n=500 分析后的判断，不在机械替换范围内。\n\n---\n\n## 12. C8 (LLaMA cross-architecture) 限定语检查（新增）\n\nC8 状态 = partially_confirmed (D060)。论文中已使用恰当限定语。n=500 不影响 LLaMA 数据，但确认限定语位置：\n\n| 文件 | 行 | 限定语 | 状态 |\n|------|------|--------|------|\n| abstract.tex | 10 | `suggests cross-architecture generalization, though at ~1/40 magnitude and with substantially weaker interaction` | ✓ 恰当 |\n| results.tex | 79 | `The qualitative pattern replicates` | ✓ 恰当 |\n| results.tex | 81 | `qualitatively consistent...though the interaction magnitude is substantially weaker` | ✓ 恰当 |\n| discussion.tex | 11 | `provides partial support for the qualitative pattern` | ✓ 恰当 |\n| conclusion.tex | 4 | `qualitatively consistent but substantially weaker trend` | ✓ 恰当 |\n| limitations.tex | 2 | `directional pattern is qualitatively consistent but the interaction magnitude is substantially weaker` | ✓ 恰当 |\n\n**无需修改**，除非 n=500 DS/QW 结果导致比率声明变化（见 §10）。\n\n---\n\n## 13. 文献完整性检查（新增）\n\n### literature_map.yaml 缺口\n\n| 缺失论文 | arXiv | 类别 | 为何需要 |\n|----------|-------|------|---------|\n| **HIES** | 2510.13832 (Oct 2025) | method-component / supporting evidence | paper_framing.md RC5/RC6 中引用了 HIES 的 importance score collapse 作为 discrimination collapse 的独立佐证。但 HIES 未收录在 literature_map.yaml 中。**需补录。** |\n\n### 已有文献完整性确认\n\n- **direct-competitor** (3): SparK ✓, GRASPrune ✓, DefensiveKV ✓ — 完整\n- **phase-aware 单轴** (4): ThinKV ✓, PagedEviction ✓, R-KV ✓, Twilight ✓ — 完整\n- **compound compression** (4): SLiM ✓, UniComp ✓, compression-ordering ✓, EVICPRESS ✓ — 完整\n- **phase transition / mechanism** (3): Physics of KV Cache ✓, phase-transition-pruning-thermo ✓, decision-repr-transition ✓ — 完整\n- **importance fragility** (3): DefensiveKV ✓, greedy-bias ✓, RetentiveKV ✓ — 完整，**但缺 HIES**\n- **adaptive controllers** (4): Ada-KV ✓, SOL ✓, LKV ✓, LAVa ✓ — 完整\n- **reasoning dynamics** (2): thinking-tokens-MI ✓, token-budget-aware ✓ — 完整\n\n### 近 2 周新论文扫描建议\n\nliterature_map.yaml 最后扫描日期 2026-05-14。距投稿 2026-05-25 还有 11 天。建议在 Day 9 (2026-05-23) 做最终扫描，重点关注：\n- arXiv cs.CL + cs.LG 中 \"compound sparsity\" / \"KV cache pruning\" / \"attention head pruning\" 相关\n- 特别注意 2026-05 新出的 ICML 2026 camera-ready 版本是否有新 compound compression 工作\n\n---\n\n## 14. 残留旧值清扫 grep 命令（更新后执行）\n\n```bash\ncd /path/to/paper/\n# 以下命令在所有 .tex 文件完成替换后执行\ngrep -n \"n=50[^0]\" *.tex           # 应只剩 LLaMA 的 n=49\ngrep -n \"\\\\b0\\\\.39\\\\b\" *.tex        # 应为 0\ngrep -n \"14\\\\.59\" *.tex             # 应为 0\ngrep -n \"\\\\b69\\\\b\" *.tex            # 应为 0（注意排除年份如 2069）\ngrep -n \"\\\\b274\\\\b\" *.tex           # 应为 0\ngrep -n \"\\\\b0\\\\.44\\\\b\" *.tex        # 应为 0（DS d_z）\ngrep -n \"\\\\b0\\\\.80\\\\b\" *.tex        # 应为 0（DS d_z）\ngrep -n \"7/8\" *.tex                 # 应为 0（除非仍为 7/8）\n```\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
````

</details>

---

### Assistant

_source line 112_

清单已保存到 `artifacts/n500_paper_update_checklist.md`。

**摘要**：

- **~60 处内联数值** + **~80 个表格单元格** + **5 个图表 PDF** 需更新
- **8 处** "50"→"500" 文本替换
- **2 个条件分支**：QW s015 CI 是否含零（6 处叙事方案）、7/8 vs 8/8（5 处）
- **4 处 LLaMA 比率声明**（§10 新增）：LLaMA 数据不变但 DS/QW 基数变化导致 "~40×"/"~7×"/"~1/40" 需重算
- **文献缺口**：HIES (arXiv 2510.13832) 已在 paper_framing RC5/RC6 中引用但未收录到 literature_map.yaml，需补录
- **C5b/C8 叙事位置**已确认无需修改（除 §10 比率外）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "uuid": "1acfd37a-e630-450b-9b64-3627d637fd34",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019QhWpvEkMEWVhNUa97U2FX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12392,
      "cache_read_input_tokens": 69831,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12392
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

_source line 113_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed_warning",
    "resetsAt": 1778911200,
    "rateLimitType": "seven_day",
    "utilization": 0.84,
    "isUsingOverage": false,
    "surpassedThreshold": 0.75
  },
  "uuid": "88d3c6d9-ad1d-4ee5-aca3-fb3aaf6dad77",
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3"
}
```

---

### Task result

_source line 114_

清单已保存到 `artifacts/n500_paper_update_checklist.md`。

**摘要**：

- **~60 处内联数值** + **~80 个表格单元格** + **5 个图表 PDF** 需更新
- **8 处** "50"→"500" 文本替换
- **2 个条件分支**：QW s015 CI 是否含零（6 处叙事方案）、7/8 vs 8/8（5 处）
- **4 处 LLaMA 比率声明**（§10 新增）：LLaMA 数据不变但 DS/QW 基数变化导致 "~40×"/"~7×"/"~1/40" 需重算
- **文献缺口**：HIES (arXiv 2510.13832) 已在 paper_framing RC5/RC6 中引用但未收录到 literature_map.yaml，需补录
- **C5b/C8 叙事位置**已确认无需修改（除 §10 比率外）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 409675,
  "duration_api_ms": 410081,
  "num_turns": 22,
  "stop_reason": "end_turn",
  "session_id": "2dafa52e-5734-485a-99e3-d769217d09b3",
  "total_cost_usd": 1.4471934000000002,
  "usage": {
    "input_tokens": 17,
    "cache_creation_input_tokens": 70776,
    "cache_read_input_tokens": 524622,
    "output_tokens": 18520,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 70776,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 295,
        "cache_read_input_tokens": 69831,
        "cache_creation_input_tokens": 12392,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 12392
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1372,
      "outputTokens": 18,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001462,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 17,
      "outputTokens": 18520,
      "cacheReadInputTokens": 524622,
      "cacheCreationInputTokens": 70776,
      "webSearchRequests": 0,
      "costUSD": 1.1677460000000002,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    },
    "claude-sonnet-4-6": {
      "inputTokens": 10,
      "outputTokens": 4861,
      "cacheReadInputTokens": 162543,
      "cacheCreationInputTokens": 41674,
      "webSearchRequests": 0,
      "costUSD": 0.2779854,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "a570f85c-bbfb-40b8-9ef4-31071f210cda"
}
```

</details>

---
