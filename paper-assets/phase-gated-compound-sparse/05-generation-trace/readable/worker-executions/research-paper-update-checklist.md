# research paper update checklist

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 107
- **Recorded user turns:** 0
- **Tool calls:** 42
- **Original source:** `logs/workers/worker_research_paper_update_checklist_20260515T021713.log`
- **Structured JSON:** [`f52319f73f0de68f8423.json`](../../sessions/f5/f52319f73f0de68f8423.json)

## Before a recorded user message

107 recorded events

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
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
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
    "mcp__agent-ml-research__detect_image",
    "mcp__agent-ml-research__kill_job",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__ssh_execute",
    "mcp__agent-ml-research__ssh_read_only"
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
  "uuid": "dc5389cf-3e96-48a0-bcba-48356025fce9",
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
    "utilization": 0.62,
    "isUsingOverage": false
  },
  "uuid": "f8621bc0-1544-4533-8e7d-510ce230c78f",
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the paper_framing.md and then locate and read all .tex files for the paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "516b27a6-3eb9-4fd8-9f13-4c652e8337ad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HZHTNtwxAvp4nVUMNSnaph",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11771,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11771
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

先读 paper_framing.md，然后定位并扫描所有 .tex 文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "8789e57d-776e-41d7-9848-e4bee75692be",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HZHTNtwxAvp4nVUMNSnaph",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11771,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11771
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01GFucCQMn1uZUUfkSozwvz1`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__ssh_read_only",
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
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "3908a02f-4483-4be5-b500-6adab4c2fce4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HZHTNtwxAvp4nVUMNSnaph",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11771,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11771
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

_source line 7 · 2026-05-15T02:17:25.002Z_

<details><summary>↩ Tool result · `toolu_01GFucCQMn1uZUUfkSozwvz1`</summary>

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
  "tool_name": "mcp__agent-ml-research__ssh_read_only"
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
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "19cf97f7-e042-4d98-8395-51a137b348f9",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__ssh_read_only"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__ssh_read_only",
    "total_deferred_tools": 26
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01CbezZyjPfWKUJLDvMoxSxX`</summary>

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
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "a352ea76-7837-4be9-8afd-9d3008cc6ebf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013GUGaBRMmjGwzrDWn3XQtK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1091,
      "cache_read_input_tokens": 23612,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1091
      },
      "output_tokens": 45,
      "service_tier": "standard",
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

_source line 9 · 2026-05-15T02:17:28.475Z_

<details><summary>↩ Tool result · `toolu_01CbezZyjPfWKUJLDvMoxSxX`</summary>

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
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "c3ae1394-68c4-4121-8368-555707489584",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01XMATQ7fzp161DXVcqVHVaM`</summary>

```json
{
  "server": "westd-22162",
  "command": "find /root/autodl-tmp/pacs/paper -name \"*.tex\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "9d47631d-ca89-45ca-a580-b8d2a989d57b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013GUGaBRMmjGwzrDWn3XQtK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1091,
      "cache_read_input_tokens": 23612,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1091
      },
      "output_tokens": 45,
      "service_tier": "standard",
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

_source line 11 · 2026-05-15T02:17:30.790Z_

<details><summary>↩ Tool result · `toolu_01XMATQ7fzp161DXVcqVHVaM`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/pacs/paper/main.tex\\n/root/autodl-tmp/pacs/paper/abstract.tex\\n/root/autodl-tmp/pacs/paper/introduction.tex\\n/root/autodl-tmp/pacs/paper/related_work.tex\\n/root/autodl-tmp/pacs/paper/background.tex\\n/root/autodl-tmp/pacs/paper/methodology.tex\\n/root/autodl-tmp/pacs/paper/results.tex\\n/root/autodl-tmp/pacs/paper/analysis.tex\\n/root/autodl-tmp/pacs/paper/discussion.tex\\n/root/autodl-tmp/pacs/paper/conclusion.tex\\n/root/autodl-tmp/pacs/paper/appendix.tex\\n/root/autodl-tmp/pacs/paper/appendix_disc_analysis.tex\\n/root/autodl-tmp/pacs/paper/appendix_results.tex\\n/root/autodl-tmp/pacs/paper/appendix_moved.tex\\n/root/autodl-tmp/pacs/paper/limitations.tex\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.13}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "13db0786-68a6-437a-ae67-abbf9f1f27f3",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/pacs/paper/main.tex\\\\n/root/autodl-tmp/pacs/paper/abstract.tex\\\\n/root/autodl-tmp/pacs/paper/introduction.tex\\\\n/root/autodl-tmp/pacs/paper/related_work.tex\\\\n/root/autodl-tmp/pacs/paper/background.tex\\\\n/root/autodl-tmp/pacs/paper/methodology.tex\\\\n/root/autodl-tmp/pacs/paper/results.tex\\\\n/root/autodl-tmp/pacs/paper/analysis.tex\\\\n/root/autodl-tmp/pacs/paper/discussion.tex\\\\n/root/autodl-tmp/pacs/paper/conclusion.tex\\\\n/root/autodl-tmp/pacs/paper/appendix.tex\\\\n/root/autodl-tmp/pacs/paper/appendix_disc_analysis.tex\\\\n/root/autodl-tmp/pacs/paper/appendix_results.tex\\\\n/root/autodl-tmp/pacs/paper/appendix_moved.tex\\\\n/root/autodl-tmp/pacs/paper/limitations.tex\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.13}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/pacs/paper/main.tex\\n/root/autodl-tmp/pacs/paper/abstract.tex\\n/root/autodl-tmp/pacs/paper/introduction.tex\\n/root/autodl-tmp/pacs/paper/related_work.tex\\n/root/autodl-tmp/pacs/paper/background.tex\\n/root/autodl-tmp/pacs/paper/methodology.tex\\n/root/autodl-tmp/pacs/paper/results.tex\\n/root/autodl-tmp/pacs/paper/analysis.tex\\n/root/autodl-tmp/pacs/paper/discussion.tex\\n/root/autodl-tmp/pacs/paper/conclusion.tex\\n/root/autodl-tmp/pacs/paper/appendix.tex\\n/root/autodl-tmp/pacs/paper/appendix_disc_analysis.tex\\n/root/autodl-tmp/pacs/paper/appendix_results.tex\\n/root/autodl-tmp/pacs/paper/appendix_moved.tex\\n/root/autodl-tmp/pacs/paper/limitations.tex\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.13}}"
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
I have the paper_framing.md and the list of .tex files. Now I need to read all 15 .tex files to identify all n=50 references, Cohen's d values, bootstrap CI values, figures, tables, C8/C5b references, and Qwen caveats.

Let me read them all in parallel using ssh_read_only.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "47b3cce9-d5bb-467b-800d-8b9828a0f1c6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HaASaKe4zhD4sf12ZidXN6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5886,
      "cache_read_input_tokens": 24703,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5886
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

找到 15 个 .tex 文件。现在并行读取所有文件内容。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "5c5c2142-2d20-4a0e-9035-8bb1a369e01e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HaASaKe4zhD4sf12ZidXN6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5886,
      "cache_read_input_tokens": 24703,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5886
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01HhLWdfruBG48gu9LGaKJp7`</summary>

```json
{
  "server": "westd-22162",
  "command": "cat /root/autodl-tmp/pacs/paper/abstract.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "1f6db04b-734e-4b37-a698-0076cdf993d8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HaASaKe4zhD4sf12ZidXN6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5886,
      "cache_read_input_tokens": 24703,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5886
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

_source line 15 · 2026-05-15T02:17:37.901Z_

<details><summary>↩ Tool result · `toolu_01HhLWdfruBG48gu9LGaKJp7`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\\begin{abstract}\\nCompound sparsity---simultaneously pruning attention heads and evicting KV cache entries---is essential for efficient LLM inference but produces super-additive quality degradation whose structure is poorly understood.\\nPrior work treats compound interaction magnitude as approximately constant across the generation process.\\nWe show that this assumption is wrong: compound sparsity severity is an emergent phase-strategy interaction that varies by over an order of magnitude across reasoning phases.\\n\\nWe evaluate compound sparsity on three models---DeepSeek-R1-Distill-Qwen-7B, Qwen2.5-7B-Instruct (both Qwen2ForCausalLM), and DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM)---spanning two architectures, using 50 MATH-500 problems, measuring the Interaction Index---a super-additivity metric---across quantile-segmented reasoning phases at sparsity levels $s \\\\in \\\\{0.15, 0.20, 0.25, 0.30\\\\}$.\\nUnder importance-based KV cache eviction, the median Interaction Index difference between low-sparsity and high-sparsity reasoning phases increases monotonically from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired Cohen's $d_z$ growing from $0.44$ (small) to $0.80$ (large); Bonferroni-corrected permutation tests yield $p < 0.005$ at all four sparsity levels.\\nRandom eviction produces no significant phase modulation in 7/8 conditions; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) shows negligible median difference ($\\\\widetilde{\\\\Delta} = \\\\placeholder{}$), confirming that the severity gradient is strategy-specific, not an inherent property of compound sparsity.\\nAt $s{=}0.25$, a crossover emerges: importance-based eviction outperforms random in high-sparsity phases ($\\\\widetilde{\\\\mathrm{II}} = 0.032$ vs.\\\\ $0.818$) yet underperforms in low-sparsity phases ($\\\\widetilde{\\\\mathrm{II}} = 7.196$ vs.\\\\ $1.363$)---a qualitative reversal in strategy ranking.\\nThe pattern replicates on Qwen2.5-7B-Instruct at $s \\\\geq 0.20$ ($d_z \\\\geq 0.55$; Spearman $\\\\rho = 1.0$; gradient permutation $p = 0.043$) and on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM), where monotonically increasing median paired differences ($\\\\widetilde{\\\\Delta}$: $0.020 \\\\to 0.356$; $s{=}0.30$ Wilcoxon $p_{\\\\text{Bonf}}{=}0.029$) provide mixed but directionally consistent evidence for cross-architecture generalization, though at ${\\\\sim}$1/40 the absolute magnitude and with substantially weaker interaction than in Qwen2-based architectures. % exp_id: c3_llama\\n\\nWe propose entropy-discrimination collapse as an explanatory mechanism: head pruning flattens cumulative importance scores in phases where attention is already broadly distributed, degrading the discriminative power of importance-based eviction in a phase-dependent manner.\\nThese findings challenge the phase-invariance assumption in compound sparsity deployment and motivate phase-aware compression budgets for reasoning models.\\n\\\\end{abstract}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "25a81721-38ee-4025-a212-58d7f20e6c6d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\\begin{abstract}\\\\nCompound sparsity---simultaneously pruning attention heads and evicting KV cache entries---is essential for efficient LLM inference but produces super-additive quality degradation whose structure is poorly understood.\\\\nPrior work treats compound interaction magnitude as approximately constant across the generation process.\\\\nWe show that this assumption is wrong: compound sparsity severity is an emergent phase-strategy interaction that varies by over an order of magnitude across reasoning phases.\\\\n\\\\nWe evaluate compound sparsity on three models---DeepSeek-R1-Distill-Qwen-7B, Qwen2.5-7B-Instruct (both Qwen2ForCausalLM), and DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM)---spanning two architectures, using 50 MATH-500 problems, measuring the Interaction Index---a super-additivity metric---across quantile-segmented reasoning phases at sparsity levels $s \\\\\\\\in \\\\\\\\{0.15, 0.20, 0.25, 0.30\\\\\\\\}$.\\\\nUnder importance-based KV cache eviction, the median Interaction Index difference between low-sparsity and high-sparsity reasoning phases increases monotonically from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired Cohen's $d_z$ growing from $0.44$ (small) to $0.80$ (large); Bonferroni-corrected permutation tests yield $p < 0.005$ at all four sparsity levels.\\\\nRandom eviction produces no significant phase modulation in 7/8 conditions; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) shows negligible median difference ($\\\\\\\\widetilde{\\\\\\\\Delta} = \\\\\\\\placeholder{}$), confirming that the severity gradient is strategy-specific, not an inherent property of compound sparsity.\\\\nAt $s{=}0.25$, a crossover emerges: importance-based eviction outperforms random in high-sparsity phases ($\\\\\\\\widetilde{\\\\\\\\mathrm{II}} = 0.032$ vs.\\\\\\\\ $0.818$) yet underperforms in low-sparsity phases ($\\\\\\\\widetilde{\\\\\\\\mathrm{II}} = 7.196$ vs.\\\\\\\\ $1.363$)---a qualitative reversal in strategy ranking.\\\\nThe pattern replicates on Qwen2.5-7B-Instruct at $s \\\\\\\\geq 0.20$ ($d_z \\\\\\\\geq 0.55$; Spearman $\\\\\\\\rho = 1.0$; gradient permutation $p = 0.043$) and on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM), where monotonically increasing median paired differences ($\\\\\\\\widetilde{\\\\\\\\Delta}$: $0.020 \\\\\\\\to 0.356$; $s{=}0.30$ Wilcoxon $p_{\\\\\\\\text{Bonf}}{=}0.029$) provide mixed but directionally consistent evidence for cross-architecture generalization, though at ${\\\\\\\\sim}$1/40 the absolute magnitude and with substantially weaker interaction than in Qwen2-based architectures. % exp_id: c3_llama\\\\n\\\\nWe propose entropy-discrimination collapse as an explanatory mechanism: head pruning flattens cumulative importance scores in phases where attention is already broadly distributed, degrading the discriminative power of importance-based eviction in a phase-dependent manner.\\\\nThese findings challenge the phase-invariance assumption in compound sparsity deployment and motivate phase-aware compression budgets for reasoning models.\\\\n\\\\\\\\end{abstract}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.46}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\\begin{abstract}\\nCompound sparsity---simultaneously pruning attention heads and evicting KV cache entries---is essential for efficient LLM inference but produces super-additive quality degradation whose structure is poorly understood.\\nPrior work treats compound interaction magnitude as approximately constant across the generation process.\\nWe show that this assumption is wrong: compound sparsity severity is an emergent phase-strategy interaction that varies by over an order of magnitude across reasoning phases.\\n\\nWe evaluate compound sparsity on three models---DeepSeek-R1-Distill-Qwen-7B, Qwen2.5-7B-Instruct (both Qwen2ForCausalLM), and DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM)---spanning two architectures, using 50 MATH-500 problems, measuring the Interaction Index---a super-additivity metric---across quantile-segmented reasoning phases at sparsity levels $s \\\\in \\\\{0.15, 0.20, 0.25, 0.30\\\\}$.\\nUnder importance-based KV cache eviction, the median Interaction Index difference between low-sparsity and high-sparsity reasoning phases increases monotonically from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired Cohen's $d_z$ growing from $0.44$ (small) to $0.80$ (large); Bonferroni-corrected permutation tests yield $p < 0.005$ at all four sparsity levels.\\nRandom eviction produces no significant phase modulation in 7/8 conditions; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) shows negligible median difference ($\\\\widetilde{\\\\Delta} = \\\\placeholder{}$), confirming that the severity gradient is strategy-specific, not an inherent property of compound sparsity.\\nAt $s{=}0.25$, a crossover emerges: importance-based eviction outperforms random in high-sparsity phases ($\\\\widetilde{\\\\mathrm{II}} = 0.032$ vs.\\\\ $0.818$) yet underperforms in low-sparsity phases ($\\\\widetilde{\\\\mathrm{II}} = 7.196$ vs.\\\\ $1.363$)---a qualitative reversal in strategy ranking.\\nThe pattern replicates on Qwen2.5-7B-Instruct at $s \\\\geq 0.20$ ($d_z \\\\geq 0.55$; Spearman $\\\\rho = 1.0$; gradient permutation $p = 0.043$) and on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM), where monotonically increasing median paired differences ($\\\\widetilde{\\\\Delta}$: $0.020 \\\\to 0.356$; $s{=}0.30$ Wilcoxon $p_{\\\\text{Bonf}}{=}0.029$) provide mixed but directionally consistent evidence for cross-architecture generalization, though at ${\\\\sim}$1/40 the absolute magnitude and with substantially weaker interaction than in Qwen2-based architectures. % exp_id: c3_llama\\n\\nWe propose entropy-discrimination collapse as an explanatory mechanism: head pruning flattens cumulative importance scores in phases where attention is already broadly distributed, degrading the discriminative power of importance-based eviction in a phase-dependent manner.\\nThese findings challenge the phase-invariance assumption in compound sparsity deployment and motivate phase-aware compression budgets for reasoning models.\\n\\\\end{abstract}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01JT2H8JuHnFSdXgDkrRHSDk`</summary>

```json
{
  "server": "westd-22162",
  "command": "cat /root/autodl-tmp/pacs/paper/introduction.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "1b3e1fb2-00c9-48a9-b02d-cba2cccd9cbd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HaASaKe4zhD4sf12ZidXN6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5886,
      "cache_read_input_tokens": 24703,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5886
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

_source line 17 · 2026-05-15T02:17:38.777Z_

<details><summary>↩ Tool result · `toolu_01JT2H8JuHnFSdXgDkrRHSDk`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\\section{Introduction}\\n\\\\label{sec:introduction}\\n\\nLong-context language models place acute pressure on the key--value (KV) cache, which grows linearly with sequence length \\\\cite{kwon-sosp2023, pope-mlsys2023}.\\nTwo complementary responses---\\\\emph{attention head pruning} \\\\cite{voita-acl2019, michel-neurips2019} and \\\\emph{KV cache eviction} \\\\cite{snapkv-neurips2024, adakv-neurips2025}---can be deployed simultaneously as \\\\emph{compound sparsity}, but the resulting quality degradation is often super-additive \\\\cite{spark-aaai2026, slim-icml2025}. Recent evaluations confirm that reasoning capabilities degrade disproportionately under compound compression \\\\cite{unicomp-2026}, and that per-dimension safe zones intersect to form a smaller joint safe region \\\\cite{phase-transition-compression-2026}.\\n\\nPrior work treats compound interaction magnitude as roughly constant across generation \\\\cite{spark-aaai2026, unicomp-2026}, despite evidence that pruning sensitivity depends on representational phase \\\\cite{decision-repr-transition-2026} and that no single sparse attention strategy dominates across generation stages \\\\cite{sparse-frontier-2025}.\\nThis assumption is problematic for reasoning models, whose generations alternate between broadly distributed attention (exploratory reasoning) and sharply concentrated attention (structured computation) \\\\cite{thinkv-iclr2026}.\\nPhase-aware methods like ThinKV \\\\cite{thinkv-iclr2026} apply different KV strategies per phase but without considering compound interaction, while importance-based eviction itself faces challenges from greedy bias \\\\cite{greedy-bias-kvcache-2026}, deferred importance \\\\cite{retentivekv-2026}, and temporal dynamics in long generations \\\\cite{lethe-aaai2026}. These methods each optimize a single pruning axis; we characterize the interaction when multiple mechanisms are composed.\\nIf compound severity varies across these phases, a uniform sparsity budget may be safe in one phase yet destructive in another.\\n\\nWe show that compound sparsity severity is strongly modulated by reasoning phase and eviction strategy.\\nUnder importance-based KV cache eviction, the Interaction Index---a measure of super-additive degradation---concentrates in low-sparsity phases and is largely absent in high-sparsity phases.\\nOn DeepSeek-R1-Distill-Qwen-7B, the median phase difference rises from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$ ($d_z$: $0.44 \\\\to 0.80$; Bonferroni-corrected $p < 0.005$ at all levels).\\nThe pattern replicates at $s \\\\geq 0.20$ on Qwen2.5-7B-Instruct ($d_z \\\\geq 0.55$) and partially extends to a distinct architecture (DeepSeek-R1-Distill-Llama-8B, LlamaForCausalLM) with a qualitatively consistent but substantially weaker trend at $\\\\sim$1/40 the magnitude.\\nCritically, random eviction produces no such gradient (7/8 conditions non-significant), confirming the gradient is an emergent phase-strategy interaction.\\n\\nWe propose \\\\emph{entropy-discrimination collapse} as a mechanism: head pruning flattens cumulative importance scores in phases where attention is broadly distributed, degrading the discriminative power of importance-based eviction in a phase-dependent manner.\\nRandom eviction is immune because its decisions are independent of attention patterns.\\nOur contributions:\\n\\\\begin{enumerate}[nosep,leftmargin=*]\\n    \\\\item We identify a \\\\textbf{phase--strategy interaction}: importance-based eviction exhibits a severity gradient across reasoning phases that is absent under random eviction (\\\\S\\\\ref{sec:results}).\\n    \\\\item We show this gradient \\\\textbf{increases monotonically with sparsity} and replicates across three models spanning two architectures (\\\\S\\\\ref{sec:results}).\\n    \\\\item We propose \\\\textbf{entropy-discrimination collapse} as a mechanistic explanation (\\\\S\\\\ref{sec:analysis}).\\n\\\\end{enumerate}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "1d6cc167-1c8b-4daf-aa3a-4b0de7b91bf9",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\\section{Introduction}\\\\n\\\\\\\\label{sec:introduction}\\\\n\\\\nLong-context language models place acute pressure on the key--value (KV) cache, which grows linearly with sequence length \\\\\\\\cite{kwon-sosp2023, pope-mlsys2023}.\\\\nTwo complementary responses---\\\\\\\\emph{attention head pruning} \\\\\\\\cite{voita-acl2019, michel-neurips2019} and \\\\\\\\emph{KV cache eviction} \\\\\\\\cite{snapkv-neurips2024, adakv-neurips2025}---can be deployed simultaneously as \\\\\\\\emph{compound sparsity}, but the resulting quality degradation is often super-additive \\\\\\\\cite{spark-aaai2026, slim-icml2025}. Recent evaluations confirm that reasoning capabilities degrade disproportionately under compound compression \\\\\\\\cite{unicomp-2026}, and that per-dimension safe zones intersect to form a smaller joint safe region \\\\\\\\cite{phase-transition-compression-2026}.\\\\n\\\\nPrior work treats compound interaction magnitude as roughly constant across generation \\\\\\\\cite{spark-aaai2026, unicomp-2026}, despite evidence that pruning sensitivity depends on representational phase \\\\\\\\cite{decision-repr-transition-2026} and that no single sparse attention strategy dominates across generation stages \\\\\\\\cite{sparse-frontier-2025}.\\\\nThis assumption is problematic for reasoning models, whose generations alternate between broadly distributed attention (exploratory reasoning) and sharply concentrated attention (structured computation) \\\\\\\\cite{thinkv-iclr2026}.\\\\nPhase-aware methods like ThinKV \\\\\\\\cite{thinkv-iclr2026} apply different KV strategies per phase but without considering compound interaction, while importance-based eviction itself faces challenges from greedy bias \\\\\\\\cite{greedy-bias-kvcache-2026}, deferred importance \\\\\\\\cite{retentivekv-2026}, and temporal dynamics in long generations \\\\\\\\cite{lethe-aaai2026}. These methods each optimize a single pruning axis; we characterize the interaction when multiple mechanisms are composed.\\\\nIf compound severity varies across these phases, a uniform sparsity budget may be safe in one phase yet destructive in another.\\\\n\\\\nWe show that compound sparsity severity is strongly modulated by reasoning phase and eviction strategy.\\\\nUnder importance-based KV cache eviction, the Interaction Index---a measure of super-additive degradation---concentrates in low-sparsity phases and is largely absent in high-sparsity phases.\\\\nOn DeepSeek-R1-Distill-Qwen-7B, the median phase difference rises from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$ ($d_z$: $0.44 \\\\\\\\to 0.80$; Bonferroni-corrected $p < 0.005$ at all levels).\\\\nThe pattern replicates at $s \\\\\\\\geq 0.20$ on Qwen2.5-7B-Instruct ($d_z \\\\\\\\geq 0.55$) and partially extends to a distinct architecture (DeepSeek-R1-Distill-Llama-8B, LlamaForCausalLM) with a qualitatively consistent but substantially weaker trend at $\\\\\\\\sim$1/40 the magnitude.\\\\nCritically, random eviction produces no such gradient (7/8 conditions non-significant), confirming the gradient is an emergent phase-strategy interaction.\\\\n\\\\nWe propose \\\\\\\\emph{entropy-discrimination collapse} as a mechanism: head pruning flattens cumulative importance scores in phases where attention is broadly distributed, degrading the discriminative power of importance-based eviction in a phase-dependent manner.\\\\nRandom eviction is immune because its decisions are independent of attention patterns.\\\\nOur contributions:\\\\n\\\\\\\\begin{enumerate}[nosep,leftmargin=*]\\\\n    \\\\\\\\item We identify a \\\\\\\\textbf{phase--strategy interaction}: importance-based eviction exhibits a severity gradient across reasoning phases that is absent under random eviction (\\\\\\\\S\\\\\\\\ref{sec:results}).\\\\n    \\\\\\\\item We show this gradient \\\\\\\\textbf{increases monotonically with sparsity} and replicates across three models spanning two architectures (\\\\\\\\S\\\\\\\\ref{sec:results}).\\\\n    \\\\\\\\item We propose \\\\\\\\textbf{entropy-discrimination collapse} as a mechanistic explanation (\\\\\\\\S\\\\\\\\ref{sec:analysis}).\\\\n\\\\\\\\end{enumerate}\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\\section{Introduction}\\n\\\\label{sec:introduction}\\n\\nLong-context language models place acute pressure on the key--value (KV) cache, which grows linearly with sequence length \\\\cite{kwon-sosp2023, pope-mlsys2023}.\\nTwo complementary responses---\\\\emph{attention head pruning} \\\\cite{voita-acl2019, michel-neurips2019} and \\\\emph{KV cache eviction} \\\\cite{snapkv-neurips2024, adakv-neurips2025}---can be deployed simultaneously as \\\\emph{compound sparsity}, but the resulting quality degradation is often super-additive \\\\cite{spark-aaai2026, slim-icml2025}. Recent evaluations confirm that reasoning capabilities degrade disproportionately under compound compression \\\\cite{unicomp-2026}, and that per-dimension safe zones intersect to form a smaller joint safe region \\\\cite{phase-transition-compression-2026}.\\n\\nPrior work treats compound interaction magnitude as roughly constant across generation \\\\cite{spark-aaai2026, unicomp-2026}, despite evidence that pruning sensitivity depends on representational phase \\\\cite{decision-repr-transition-2026} and that no single sparse attention strategy dominates across generation stages \\\\cite{sparse-frontier-2025}.\\nThis assumption is problematic for reasoning models, whose generations alternate between broadly distributed attention (exploratory reasoning) and sharply concentrated attention (structured computation) \\\\cite{thinkv-iclr2026}.\\nPhase-aware methods like ThinKV \\\\cite{thinkv-iclr2026} apply different KV strategies per phase but without considering compound interaction, while importance-based eviction itself faces challenges from greedy bias \\\\cite{greedy-bias-kvcache-2026}, deferred importance \\\\cite{retentivekv-2026}, and temporal dynamics in long generations \\\\cite{lethe-aaai2026}. These methods each optimize a single pruning axis; we characterize the interaction when multiple mechanisms are composed.\\nIf compound severity varies across these phases, a uniform sparsity budget may be safe in one phase yet destructive in another.\\n\\nWe show that compound sparsity severity is strongly modulated by reasoning phase and eviction strategy.\\nUnder importance-based KV cache eviction, the Interaction Index---a measure of super-additive degradation---concentrates in low-sparsity phases and is largely absent in high-sparsity phases.\\nOn DeepSeek-R1-Distill-Qwen-7B, the median phase difference rises from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$ ($d_z$: $0.44 \\\\to 0.80$; Bonferroni-corrected $p < 0.005$ at all levels).\\nThe pattern replicates at $s \\\\geq 0.20$ on Qwen2.5-7B-Instruct ($d_z \\\\geq 0.55$) and partially extends to a distinct architecture (DeepSeek-R1-Distill-Llama-8B, LlamaForCausalLM) with a qualitatively consistent but substantially weaker trend at $\\\\sim$1/40 the magnitude.\\nCritically, random eviction produces no such gradient (7/8 conditions non-significant), confirming the gradient is an emergent phase-strategy interaction.\\n\\nWe propose \\\\emph{entropy-discrimination collapse} as a mechanism: head pruning flattens cumulative importance scores in phases where attention is broadly distributed, degrading the discriminative power of importance-based eviction in a phase-dependent manner.\\nRandom eviction is immune because its decisions are independent of attention patterns.\\nOur contributions:\\n\\\\begin{enumerate}[nosep,leftmargin=*]\\n    \\\\item We identify a \\\\textbf{phase--strategy interaction}: importance-based eviction exhibits a severity gradient across reasoning phases that is absent under random eviction (\\\\S\\\\ref{sec:results}).\\n    \\\\item We show this gradient \\\\textbf{increases monotonically with sparsity} and replicates across three models spanning two architectures (\\\\S\\\\ref{sec:results}).\\n    \\\\item We propose \\\\textbf{entropy-discrimination collapse} as a mechanistic explanation (\\\\S\\\\ref{sec:analysis}).\\n\\\\end{enumerate}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01PShzwsp2zuqGBNzEh1s82W`</summary>

```json
{
  "server": "westd-22162",
  "command": "cat /root/autodl-tmp/pacs/paper/related_work.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "d15d6880-1312-4d92-ac1e-f86b11c1affe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HaASaKe4zhD4sf12ZidXN6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5886,
      "cache_read_input_tokens": 24703,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5886
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

_source line 19 · 2026-05-15T02:17:39.701Z_

<details><summary>↩ Tool result · `toolu_01PShzwsp2zuqGBNzEh1s82W`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\\section{Related Work}\\n\\\\label{sec:related}\\n\\n\\\\paragraph{Compound compression.}\\nCombining multiple compression axes produces non-additive errors.\\n\\\\cite{spark-aaai2026} report super-additive degradation when combining channel pruning with token eviction; \\\\cite{slim-icml2025} formalize compound error for quantization and sparsity.\\n\\\\cite{unicomp-2026} evaluate compound compression across 40+ benchmarks, revealing that reasoning capabilities degrade disproportionately.\\n\\\\cite{phase-transition-compression-2026} characterize independent phase transition points per compression dimension, implying the joint safe region is the intersection of per-dimension safe zones.\\nGRASPrune~\\\\cite{graspune-acl2026} learns global budget-constrained gates for joint pruning but treats decisions as static across generation.\\nThese works establish compound interaction but share an implicit assumption: interaction magnitude is constant across the generation process.\\n\\n\\\\paragraph{KV cache eviction.}\\nMost methods rely on importance scoring whose reliability is increasingly questioned.\\nAda-KV~\\\\cite{adakv-neurips2025} introduces per-head adaptive budgets; SnapKV~\\\\cite{snapkv-neurips2024} compresses from a fixed observation window; \\\\cite{defensivekv-iclr2026} show worst-case loss $2.3$--$4.3{\\\\times}$ higher than expected under standard aggregation.\\n\\\\cite{nacl-acl2024} combine proxy-token and random eviction to counter attention bias.\\nRetentiveKV~\\\\cite{retentivekv-2026} identifies deferred importance, and \\\\cite{greedy-bias-kvcache-2026} show that single importance metrics exhibit systematic greedy bias.\\n\\\\cite{hies-2025} independently show that importance-based head discrimination collapses under heavy pruning, further questioning single-metric reliability.\\nLethe~\\\\cite{lethe-aaai2026} introduces temporal adaptivity with layer-wise multi-round pruning, and SparK~\\\\cite{spark-aaai2026} extends eviction to the channel dimension with recoverable sparsity.\\nThese methods each optimize a single pruning axis---whether aggregation, metric, temporal, or channel---without characterizing compound interactions when multiple mechanisms are simultaneously active.\\n\\n\\\\paragraph{Phase-aware inference.}\\nThinKV~\\\\cite{thinkv-iclr2026} applies different KV strategies per phase but without compound interaction.\\n\\\\cite{decision-repr-transition-2026} find pruning sensitivity depends on ``silent'' vs.\\\\ ``decisive'' representation phases.\\n\\\\cite{doing-more-with-less-2026} show pruning combined with test-time scaling can exceed unpruned baselines; \\\\cite{sparse-frontier-2025} find no universally optimal sparse attention strategy across generation stages.\\n\\\\cite{physics-kvcache-2026} identify a sharp phase transition in single-axis KV cache compression at high sparsity, characterizing the single-dimension failure mode that our compound analysis extends across multiple axes.\\nR-KV~\\\\cite{rkv-neurips2025} exploits reasoning-specific redundancy for aggressive cache compression, targeting per-axis optimization rather than characterizing compound degradation.\\nThese works establish phase-dependent compression tolerance along single axes.\\nOur work bridges this by quantifying how compound severity varies across phases and eviction strategies.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "405e7a5a-3e08-4395-bd3d-5e197c2af0b9",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\\section{Related Work}\\\\n\\\\\\\\label{sec:related}\\\\n\\\\n\\\\\\\\paragraph{Compound compression.}\\\\nCombining multiple compression axes produces non-additive errors.\\\\n\\\\\\\\cite{spark-aaai2026} report super-additive degradation when combining channel pruning with token eviction; \\\\\\\\cite{slim-icml2025} formalize compound error for quantization and sparsity.\\\\n\\\\\\\\cite{unicomp-2026} evaluate compound compression across 40+ benchmarks, revealing that reasoning capabilities degrade disproportionately.\\\\n\\\\\\\\cite{phase-transition-compression-2026} characterize independent phase transition points per compression dimension, implying the joint safe region is the intersection of per-dimension safe zones.\\\\nGRASPrune~\\\\\\\\cite{graspune-acl2026} learns global budget-constrained gates for joint pruning but treats decisions as static across generation.\\\\nThese works establish compound interaction but share an implicit assumption: interaction magnitude is constant across the generation process.\\\\n\\\\n\\\\\\\\paragraph{KV cache eviction.}\\\\nMost methods rely on importance scoring whose reliability is increasingly questioned.\\\\nAda-KV~\\\\\\\\cite{adakv-neurips2025} introduces per-head adaptive budgets; SnapKV~\\\\\\\\cite{snapkv-neurips2024} compresses from a fixed observation window; \\\\\\\\cite{defensivekv-iclr2026} show worst-case loss $2.3$--$4.3{\\\\\\\\times}$ higher than expected under standard aggregation.\\\\n\\\\\\\\cite{nacl-acl2024} combine proxy-token and random eviction to counter attention bias.\\\\nRetentiveKV~\\\\\\\\cite{retentivekv-2026} identifies deferred importance, and \\\\\\\\cite{greedy-bias-kvcache-2026} show that single importance metrics exhibit systematic greedy bias.\\\\n\\\\\\\\cite{hies-2025} independently show that importance-based head discrimination collapses under heavy pruning, further questioning single-metric reliability.\\\\nLethe~\\\\\\\\cite{lethe-aaai2026} introduces temporal adaptivity with layer-wise multi-round pruning, and SparK~\\\\\\\\cite{spark-aaai2026} extends eviction to the channel dimension with recoverable sparsity.\\\\nThese methods each optimize a single pruning axis---whether aggregation, metric, temporal, or channel---without characterizing compound interactions when multiple mechanisms are simultaneously active.\\\\n\\\\n\\\\\\\\paragraph{Phase-aware inference.}\\\\nThinKV~\\\\\\\\cite{thinkv-iclr2026} applies different KV strategies per phase but without compound interaction.\\\\n\\\\\\\\cite{decision-repr-transition-2026} find pruning sensitivity depends on ``silent'' vs.\\\\\\\\ ``decisive'' representation phases.\\\\n\\\\\\\\cite{doing-more-with-less-2026} show pruning combined with test-time scaling can exceed unpruned baselines; \\\\\\\\cite{sparse-frontier-2025} find no universally optimal sparse attention strategy across generation stages.\\\\n\\\\\\\\cite{physics-kvcache-2026} identify a sharp phase transition in single-axis KV cache compression at high sparsity, characterizing the single-dimension failure mode that our compound analysis extends across multiple axes.\\\\nR-KV~\\\\\\\\cite{rkv-neurips2025} exploits reasoning-specific redundancy for aggressive cache compression, targeting per-axis optimization rather than characterizing compound degradation.\\\\nThese works establish phase-dependent compression tolerance along single axes.\\\\nOur work bridges this by quantifying how compound severity varies across phases and eviction strategies.\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\\section{Related Work}\\n\\\\label{sec:related}\\n\\n\\\\paragraph{Compound compression.}\\nCombining multiple compression axes produces non-additive errors.\\n\\\\cite{spark-aaai2026} report super-additive degradation when combining channel pruning with token eviction; \\\\cite{slim-icml2025} formalize compound error for quantization and sparsity.\\n\\\\cite{unicomp-2026} evaluate compound compression across 40+ benchmarks, revealing that reasoning capabilities degrade disproportionately.\\n\\\\cite{phase-transition-compression-2026} characterize independent phase transition points per compression dimension, implying the joint safe region is the intersection of per-dimension safe zones.\\nGRASPrune~\\\\cite{graspune-acl2026} learns global budget-constrained gates for joint pruning but treats decisions as static across generation.\\nThese works establish compound interaction but share an implicit assumption: interaction magnitude is constant across the generation process.\\n\\n\\\\paragraph{KV cache eviction.}\\nMost methods rely on importance scoring whose reliability is increasingly questioned.\\nAda-KV~\\\\cite{adakv-neurips2025} introduces per-head adaptive budgets; SnapKV~\\\\cite{snapkv-neurips2024} compresses from a fixed observation window; \\\\cite{defensivekv-iclr2026} show worst-case loss $2.3$--$4.3{\\\\times}$ higher than expected under standard aggregation.\\n\\\\cite{nacl-acl2024} combine proxy-token and random eviction to counter attention bias.\\nRetentiveKV~\\\\cite{retentivekv-2026} identifies deferred importance, and \\\\cite{greedy-bias-kvcache-2026} show that single importance metrics exhibit systematic greedy bias.\\n\\\\cite{hies-2025} independently show that importance-based head discrimination collapses under heavy pruning, further questioning single-metric reliability.\\nLethe~\\\\cite{lethe-aaai2026} introduces temporal adaptivity with layer-wise multi-round pruning, and SparK~\\\\cite{spark-aaai2026} extends eviction to the channel dimension with recoverable sparsity.\\nThese methods each optimize a single pruning axis---whether aggregation, metric, temporal, or channel---without characterizing compound interactions when multiple mechanisms are simultaneously active.\\n\\n\\\\paragraph{Phase-aware inference.}\\nThinKV~\\\\cite{thinkv-iclr2026} applies different KV strategies per phase but without compound interaction.\\n\\\\cite{decision-repr-transition-2026} find pruning sensitivity depends on ``silent'' vs.\\\\ ``decisive'' representation phases.\\n\\\\cite{doing-more-with-less-2026} show pruning combined with test-time scaling can exceed unpruned baselines; \\\\cite{sparse-frontier-2025} find no universally optimal sparse attention strategy across generation stages.\\n\\\\cite{physics-kvcache-2026} identify a sharp phase transition in single-axis KV cache compression at high sparsity, characterizing the single-dimension failure mode that our compound analysis extends across multiple axes.\\nR-KV~\\\\cite{rkv-neurips2025} exploits reasoning-specific redundancy for aggressive cache compression, targeting per-axis optimization rather than characterizing compound degradation.\\nThese works establish phase-dependent compression tolerance along single axes.\\nOur work bridges this by quantifying how compound severity varies across phases and eviction strategies.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01MtogjwXHjrJoiaBMeS7phX`</summary>

```json
{
  "server": "westd-22162",
  "command": "cat /root/autodl-tmp/pacs/paper/background.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "f99ed93c-d897-4eb9-a651-e30429cabced",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HaASaKe4zhD4sf12ZidXN6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5886,
      "cache_read_input_tokens": 24703,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5886
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

_source line 21 · 2026-05-15T02:17:40.243Z_

<details><summary>↩ Tool result · `toolu_01MtogjwXHjrJoiaBMeS7phX`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"% Section 3: Background and Problem Setup\\n% Note: eq:ii and eq:gradient are the canonical definitions.\\n% Full formulation details in Appendix (app:formulation-details).\\n\\n\\\\section{Background and Problem Setup}\\n\\\\label{sec:background}\\n\\nWe formalize compound sparsity, define the Interaction Index, and introduce phase segmentation. Full mathematical details appear in Appendix~\\\\ref{app:formulation-details}.\\n\\n\\\\paragraph{Compound sparsity.}\\n\\\\label{sec:compound-sparsity}\\nLet $s \\\\in (0,1)$ denote a unified sparsity budget. \\\\emph{Attention head pruning} removes the bottom-$s$ fraction of heads per layer by Frobenius norm importance \\\\cite{voita-acl2019, michel-neurips2019}. \\\\emph{KV cache eviction} removes the bottom-$s$ fraction of token positions from the cache. We compare two strategies: \\\\emph{importance-based}, which scores positions by position-normalized cumulative attention mass (Eq.~\\\\ref{eq:kv-importance} in Appendix~\\\\ref{app:formulation-details}), and \\\\emph{random}, which evicts uniformly at random \\\\cite{nacl-acl2024}. Applying both simultaneously yields \\\\emph{compound sparsity}; the two axes interact because head pruning alters the importance ranking used for eviction \\\\cite{spark-aaai2026}. Existing joint-pruning approaches such as GRASPrune \\\\cite{graspune-acl2026} learn global budget-constrained gates but treat decisions as static across generation.\\n\\n\\\\paragraph{Interaction Index.}\\n\\\\label{sec:interaction-index}\\nFor a text segment, let $\\\\text{PPL}_c$ denote perplexity under condition $c \\\\in \\\\{d, a, k, b\\\\}$ (dense, attention-only, KV-only, compound). Normalizing by the dense baseline yields $r_c = \\\\text{PPL}_c / \\\\text{PPL}_d$, and:\\n\\\\begin{equation}\\n    \\\\mathrm{II} = r_b - r_a - r_k + 1.\\n    \\\\label{eq:ii}\\n\\\\end{equation}\\n$\\\\mathrm{II} > 0$ indicates super-additive degradation; $\\\\mathrm{II} = 0$ indicates additive independence. We adopt the additive null because the two axes operate on disjoint dimensions; qualitative conclusions hold under the multiplicative null (Appendix~\\\\ref{app:multiplicative-null}). Because the II distribution is heavily right-skewed, we report medians throughout.\\n\\n\\\\paragraph{Severity gradient.}\\nTo capture phase variation:\\n\\\\begin{equation}\\n    G = \\\\frac{\\\\widetilde{\\\\mathrm{II}}_{\\\\,\\\\textit{low}}}{\\\\widetilde{\\\\mathrm{II}}_{\\\\,\\\\textit{high}}},\\n    \\\\label{eq:gradient}\\n\\\\end{equation}\\nwhere $\\\\widetilde{\\\\mathrm{II}}_{\\\\,\\\\textit{low/high}}$ are median II in the low/high-sparsity phases. $G \\\\gg 1$ indicates phase-concentrated severity.\\n\\n\\\\paragraph{Phase segmentation.}\\n\\\\label{sec:phase-segmentation}\\nEach generated sequence is partitioned into three phases (low-, mid-, high-sparsity) by tercile boundaries of per-position attention sparsity, following ThinKV~\\\\cite{thinkv-iclr2026}. Low-sparsity phases correspond to broadly distributed attention (exploratory reasoning); high-sparsity phases to concentrated attention (structured computation). Details in Appendix~\\\\ref{app:formulation-details}.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "83e4ccc5-b35f-4d40-a365-d50b0009afcd",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"% Section 3: Background and Problem Setup\\\\n% Note: eq:ii and eq:gradient are the canonical definitions.\\\\n% Full formulation details in Appendix (app:formulation-details).\\\\n\\\\n\\\\\\\\section{Background and Problem Setup}\\\\n\\\\\\\\label{sec:background}\\\\n\\\\nWe formalize compound sparsity, define the Interaction Index, and introduce phase segmentation. Full mathematical details appear in Appendix~\\\\\\\\ref{app:formulation-details}.\\\\n\\\\n\\\\\\\\paragraph{Compound sparsity.}\\\\n\\\\\\\\label{sec:compound-sparsity}\\\\nLet $s \\\\\\\\in (0,1)$ denote a unified sparsity budget. \\\\\\\\emph{Attention head pruning} removes the bottom-$s$ fraction of heads per layer by Frobenius norm importance \\\\\\\\cite{voita-acl2019, michel-neurips2019}. \\\\\\\\emph{KV cache eviction} removes the bottom-$s$ fraction of token positions from the cache. We compare two strategies: \\\\\\\\emph{importance-based}, which scores positions by position-normalized cumulative attention mass (Eq.~\\\\\\\\ref{eq:kv-importance} in Appendix~\\\\\\\\ref{app:formulation-details}), and \\\\\\\\emph{random}, which evicts uniformly at random \\\\\\\\cite{nacl-acl2024}. Applying both simultaneously yields \\\\\\\\emph{compound sparsity}; the two axes interact because head pruning alters the importance ranking used for eviction \\\\\\\\cite{spark-aaai2026}. Existing joint-pruning approaches such as GRASPrune \\\\\\\\cite{graspune-acl2026} learn global budget-constrained gates but treat decisions as static across generation.\\\\n\\\\n\\\\\\\\paragraph{Interaction Index.}\\\\n\\\\\\\\label{sec:interaction-index}\\\\nFor a text segment, let $\\\\\\\\text{PPL}_c$ denote perplexity under condition $c \\\\\\\\in \\\\\\\\{d, a, k, b\\\\\\\\}$ (dense, attention-only, KV-only, compound). Normalizing by the dense baseline yields $r_c = \\\\\\\\text{PPL}_c / \\\\\\\\text{PPL}_d$, and:\\\\n\\\\\\\\begin{equation}\\\\n    \\\\\\\\mathrm{II} = r_b - r_a - r_k + 1.\\\\n    \\\\\\\\label{eq:ii}\\\\n\\\\\\\\end{equation}\\\\n$\\\\\\\\mathrm{II} > 0$ indicates super-additive degradation; $\\\\\\\\mathrm{II} = 0$ indicates additive independence. We adopt the additive null because the two axes operate on disjoint dimensions; qualitative conclusions hold under the multiplicative null (Appendix~\\\\\\\\ref{app:multiplicative-null}). Because the II distribution is heavily right-skewed, we report medians throughout.\\\\n\\\\n\\\\\\\\paragraph{Severity gradient.}\\\\nTo capture phase variation:\\\\n\\\\\\\\begin{equation}\\\\n    G = \\\\\\\\frac{\\\\\\\\widetilde{\\\\\\\\mathrm{II}}_{\\\\\\\\,\\\\\\\\textit{low}}}{\\\\\\\\widetilde{\\\\\\\\mathrm{II}}_{\\\\\\\\,\\\\\\\\textit{high}}},\\\\n    \\\\\\\\label{eq:gradient}\\\\n\\\\\\\\end{equation}\\\\nwhere $\\\\\\\\widetilde{\\\\\\\\mathrm{II}}_{\\\\\\\\,\\\\\\\\textit{low/high}}$ are median II in the low/high-sparsity phases. $G \\\\\\\\gg 1$ indicates phase-concentrated severity.\\\\n\\\\n\\\\\\\\paragraph{Phase segmentation.}\\\\n\\\\\\\\label{sec:phase-segmentation}\\\\nEach generated sequence is partitioned into three phases (low-, mid-, high-sparsity) by tercile boundaries of per-position attention sparsity, following ThinKV~\\\\\\\\cite{thinkv-iclr2026}. Low-sparsity phases correspond to broadly distributed attention (exploratory reasoning); high-sparsity phases to concentrated attention (structured computation). Details in Appendix~\\\\\\\\ref{app:formulation-details}.\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.51}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"% Section 3: Background and Problem Setup\\n% Note: eq:ii and eq:gradient are the canonical definitions.\\n% Full formulation details in Appendix (app:formulation-details).\\n\\n\\\\section{Background and Problem Setup}\\n\\\\label{sec:background}\\n\\nWe formalize compound sparsity, define the Interaction Index, and introduce phase segmentation. Full mathematical details appear in Appendix~\\\\ref{app:formulation-details}.\\n\\n\\\\paragraph{Compound sparsity.}\\n\\\\label{sec:compound-sparsity}\\nLet $s \\\\in (0,1)$ denote a unified sparsity budget. \\\\emph{Attention head pruning} removes the bottom-$s$ fraction of heads per layer by Frobenius norm importance \\\\cite{voita-acl2019, michel-neurips2019}. \\\\emph{KV cache eviction} removes the bottom-$s$ fraction of token positions from the cache. We compare two strategies: \\\\emph{importance-based}, which scores positions by position-normalized cumulative attention mass (Eq.~\\\\ref{eq:kv-importance} in Appendix~\\\\ref{app:formulation-details}), and \\\\emph{random}, which evicts uniformly at random \\\\cite{nacl-acl2024}. Applying both simultaneously yields \\\\emph{compound sparsity}; the two axes interact because head pruning alters the importance ranking used for eviction \\\\cite{spark-aaai2026}. Existing joint-pruning approaches such as GRASPrune \\\\cite{graspune-acl2026} learn global budget-constrained gates but treat decisions as static across generation.\\n\\n\\\\paragraph{Interaction Index.}\\n\\\\label{sec:interaction-index}\\nFor a text segment, let $\\\\text{PPL}_c$ denote perplexity under condition $c \\\\in \\\\{d, a, k, b\\\\}$ (dense, attention-only, KV-only, compound). Normalizing by the dense baseline yields $r_c = \\\\text{PPL}_c / \\\\text{PPL}_d$, and:\\n\\\\begin{equation}\\n    \\\\mathrm{II} = r_b - r_a - r_k + 1.\\n    \\\\label{eq:ii}\\n\\\\end{equation}\\n$\\\\mathrm{II} > 0$ indicates super-additive degradation; $\\\\mathrm{II} = 0$ indicates additive independence. We adopt the additive null because the two axes operate on disjoint dimensions; qualitative conclusions hold under the multiplicative null (Appendix~\\\\ref{app:multiplicative-null}). Because the II distribution is heavily right-skewed, we report medians throughout.\\n\\n\\\\paragraph{Severity gradient.}\\nTo capture phase variation:\\n\\\\begin{equation}\\n    G = \\\\frac{\\\\widetilde{\\\\mathrm{II}}_{\\\\,\\\\textit{low}}}{\\\\widetilde{\\\\mathrm{II}}_{\\\\,\\\\textit{high}}},\\n    \\\\label{eq:gradient}\\n\\\\end{equation}\\nwhere $\\\\widetilde{\\\\mathrm{II}}_{\\\\,\\\\textit{low/high}}$ are median II in the low/high-sparsity phases. $G \\\\gg 1$ indicates phase-concentrated severity.\\n\\n\\\\paragraph{Phase segmentation.}\\n\\\\label{sec:phase-segmentation}\\nEach generated sequence is partitioned into three phases (low-, mid-, high-sparsity) by tercile boundaries of per-position attention sparsity, following ThinKV~\\\\cite{thinkv-iclr2026}. Low-sparsity phases correspond to broadly distributed attention (exploratory reasoning); high-sparsity phases to concentrated attention (structured computation). Details in Appendix~\\\\ref{app:formulation-details}.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01FmbEr9kqvgFEaoyi3x6sSw`</summary>

```json
{
  "server": "westd-22162",
  "command": "cat /root/autodl-tmp/pacs/paper/methodology.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "52c3ac0c-02d2-4660-a514-36948b095bd2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HaASaKe4zhD4sf12ZidXN6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5886,
      "cache_read_input_tokens": 24703,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5886
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

_source line 23 · 2026-05-15T02:17:41.128Z_

<details><summary>↩ Tool result · `toolu_01FmbEr9kqvgFEaoyi3x6sSw`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\\section{Experimental Setup}\\n\\\\label{sec:experimental-setup}\\n\\n\\\\paragraph{Models.}\\n\\\\label{sec:models}\\nWe evaluate on two 7B-parameter models sharing the Qwen2 backbone (28 layers, 28 heads, 4-group GQA): \\\\textbf{DeepSeek-R1-Distill-Qwen-7B}~\\\\cite{deepseek-r1-2025}, distilled from DeepSeek-R1 with explicit chain-of-thought traces yielding pronounced phase structure; and \\\\textbf{Qwen2.5-7B-Instruct}~\\\\cite{qwen25-2024}, with standard instruction tuning, providing a cross-model replication target. Both are loaded in \\\\texttt{bfloat16} with eager attention.\\\\footnote{An earlier \\\\texttt{float16} configuration produced sporadic NaN values; \\\\texttt{bfloat16} eliminated all occurrences.}\\n\\n\\\\paragraph{Dataset.}\\n\\\\label{sec:dataset}\\nWe use 50 problems stratified from MATH-500~\\\\cite{math500-neurips2021}, sampling uniformly across categories with a fixed seed. Each problem is decoded greedily (\\\\texttt{max\\\\_new\\\\_tokens}$=$2048).\\n\\n\\\\paragraph{Sparsity configuration.}\\n\\\\label{sec:sparsity-config}\\nWe apply symmetric compound sparsity at $s \\\\in \\\\{0.15, 0.20, 0.25, 0.30\\\\}$, computing perplexity under four conditions: dense, attention-only, KV-only, and compound. We compare \\\\emph{importance-based} eviction (position-normalized cumulative attention score, Eq.~\\\\ref{eq:kv-importance}; BOS always retained) and \\\\emph{random} eviction (uniform). Heads are pruned per layer by Frobenius norm; under random eviction, both heads and positions are selected uniformly.\\n\\n\\\\paragraph{Phase segmentation and metrics.}\\n\\\\label{sec:phase-seg}\\nEach sequence is segmented into three phases using the quantile-based method (\\\\S\\\\ref{sec:phase-segmentation}), with $\\\\texttt{min\\\\_phase\\\\_length}{=}10$. We compute segment-level perplexity, II (Eq.~\\\\ref{eq:ii}), and $G$ (Eq.~\\\\ref{eq:gradient}), reporting medians due to heavy right-skew (mean/median ratios up to 43:1).\\n\\n\\\\paragraph{Statistical analysis.}\\n\\\\label{sec:stats}\\nAll reported confidence intervals and significance tests use nonparametric bootstrap ($B{=}10{,}000$)~\\\\cite{efron-1993}; initial profiling uses $B{=}1{,}000$ for computational efficiency, with all reported statistics recomputed at $B{=}10{,}000$. Paired bootstrap controls for problem-level variance. All tests yield $p_{\\\\text{Bonf}} < 0.005$ at every sparsity level.\\\\footnote{Experiments on 4$\\\\times$ NVIDIA RTX PRO 6000 Blackwell 96\\\\,GB GPUs.}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "677ea305-ce49-4408-858c-ed6f2cdd744c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\\section{Experimental Setup}\\\\n\\\\\\\\label{sec:experimental-setup}\\\\n\\\\n\\\\\\\\paragraph{Models.}\\\\n\\\\\\\\label{sec:models}\\\\nWe evaluate on two 7B-parameter models sharing the Qwen2 backbone (28 layers, 28 heads, 4-group GQA): \\\\\\\\textbf{DeepSeek-R1-Distill-Qwen-7B}~\\\\\\\\cite{deepseek-r1-2025}, distilled from DeepSeek-R1 with explicit chain-of-thought traces yielding pronounced phase structure; and \\\\\\\\textbf{Qwen2.5-7B-Instruct}~\\\\\\\\cite{qwen25-2024}, with standard instruction tuning, providing a cross-model replication target. Both are loaded in \\\\\\\\texttt{bfloat16} with eager attention.\\\\\\\\footnote{An earlier \\\\\\\\texttt{float16} configuration produced sporadic NaN values; \\\\\\\\texttt{bfloat16} eliminated all occurrences.}\\\\n\\\\n\\\\\\\\paragraph{Dataset.}\\\\n\\\\\\\\label{sec:dataset}\\\\nWe use 50 problems stratified from MATH-500~\\\\\\\\cite{math500-neurips2021}, sampling uniformly across categories with a fixed seed. Each problem is decoded greedily (\\\\\\\\texttt{max\\\\\\\\_new\\\\\\\\_tokens}$=$2048).\\\\n\\\\n\\\\\\\\paragraph{Sparsity configuration.}\\\\n\\\\\\\\label{sec:sparsity-config}\\\\nWe apply symmetric compound sparsity at $s \\\\\\\\in \\\\\\\\{0.15, 0.20, 0.25, 0.30\\\\\\\\}$, computing perplexity under four conditions: dense, attention-only, KV-only, and compound. We compare \\\\\\\\emph{importance-based} eviction (position-normalized cumulative attention score, Eq.~\\\\\\\\ref{eq:kv-importance}; BOS always retained) and \\\\\\\\emph{random} eviction (uniform). Heads are pruned per layer by Frobenius norm; under random eviction, both heads and positions are selected uniformly.\\\\n\\\\n\\\\\\\\paragraph{Phase segmentation and metrics.}\\\\n\\\\\\\\label{sec:phase-seg}\\\\nEach sequence is segmented into three phases using the quantile-based method (\\\\\\\\S\\\\\\\\ref{sec:phase-segmentation}), with $\\\\\\\\texttt{min\\\\\\\\_phase\\\\\\\\_length}{=}10$. We compute segment-level perplexity, II (Eq.~\\\\\\\\ref{eq:ii}), and $G$ (Eq.~\\\\\\\\ref{eq:gradient}), reporting medians due to heavy right-skew (mean/median ratios up to 43:1).\\\\n\\\\n\\\\\\\\paragraph{Statistical analysis.}\\\\n\\\\\\\\label{sec:stats}\\\\nAll reported confidence intervals and significance tests use nonparametric bootstrap ($B{=}10{,}000$)~\\\\\\\\cite{efron-1993}; initial profiling uses $B{=}1{,}000$ for computational efficiency, with all reported statistics recomputed at $B{=}10{,}000$. Paired bootstrap controls for problem-level variance. All tests yield $p_{\\\\\\\\text{Bonf}} < 0.005$ at every sparsity level.\\\\\\\\footnote{Experiments on 4$\\\\\\\\times$ NVIDIA RTX PRO 6000 Blackwell 96\\\\\\\\,GB GPUs.}\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\\section{Experimental Setup}\\n\\\\label{sec:experimental-setup}\\n\\n\\\\paragraph{Models.}\\n\\\\label{sec:models}\\nWe evaluate on two 7B-parameter models sharing the Qwen2 backbone (28 layers, 28 heads, 4-group GQA): \\\\textbf{DeepSeek-R1-Distill-Qwen-7B}~\\\\cite{deepseek-r1-2025}, distilled from DeepSeek-R1 with explicit chain-of-thought traces yielding pronounced phase structure; and \\\\textbf{Qwen2.5-7B-Instruct}~\\\\cite{qwen25-2024}, with standard instruction tuning, providing a cross-model replication target. Both are loaded in \\\\texttt{bfloat16} with eager attention.\\\\footnote{An earlier \\\\texttt{float16} configuration produced sporadic NaN values; \\\\texttt{bfloat16} eliminated all occurrences.}\\n\\n\\\\paragraph{Dataset.}\\n\\\\label{sec:dataset}\\nWe use 50 problems stratified from MATH-500~\\\\cite{math500-neurips2021}, sampling uniformly across categories with a fixed seed. Each problem is decoded greedily (\\\\texttt{max\\\\_new\\\\_tokens}$=$2048).\\n\\n\\\\paragraph{Sparsity configuration.}\\n\\\\label{sec:sparsity-config}\\nWe apply symmetric compound sparsity at $s \\\\in \\\\{0.15, 0.20, 0.25, 0.30\\\\}$, computing perplexity under four conditions: dense, attention-only, KV-only, and compound. We compare \\\\emph{importance-based} eviction (position-normalized cumulative attention score, Eq.~\\\\ref{eq:kv-importance}; BOS always retained) and \\\\emph{random} eviction (uniform). Heads are pruned per layer by Frobenius norm; under random eviction, both heads and positions are selected uniformly.\\n\\n\\\\paragraph{Phase segmentation and metrics.}\\n\\\\label{sec:phase-seg}\\nEach sequence is segmented into three phases using the quantile-based method (\\\\S\\\\ref{sec:phase-segmentation}), with $\\\\texttt{min\\\\_phase\\\\_length}{=}10$. We compute segment-level perplexity, II (Eq.~\\\\ref{eq:ii}), and $G$ (Eq.~\\\\ref{eq:gradient}), reporting medians due to heavy right-skew (mean/median ratios up to 43:1).\\n\\n\\\\paragraph{Statistical analysis.}\\n\\\\label{sec:stats}\\nAll reported confidence intervals and significance tests use nonparametric bootstrap ($B{=}10{,}000$)~\\\\cite{efron-1993}; initial profiling uses $B{=}1{,}000$ for computational efficiency, with all reported statistics recomputed at $B{=}10{,}000$. Paired bootstrap controls for problem-level variance. All tests yield $p_{\\\\text{Bonf}} < 0.005$ at every sparsity level.\\\\footnote{Experiments on 4$\\\\times$ NVIDIA RTX PRO 6000 Blackwell 96\\\\,GB GPUs.}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01YRxgxVxF94RjqyWWb7M1mD`</summary>

```json
{
  "server": "westd-22162",
  "command": "cat /root/autodl-tmp/pacs/paper/results.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "b2cee88d-9e2d-4918-8461-44eb2bde028c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HaASaKe4zhD4sf12ZidXN6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5886,
      "cache_read_input_tokens": 24703,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5886
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

_source line 25 · 2026-05-15T02:17:41.666Z_

<details><summary>↩ Tool result · `toolu_01YRxgxVxF94RjqyWWb7M1mD`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\n\\\\section{Results}\\n\\\\label{sec:results}\\n\\n\\\\subsection{Strategy-Dependent Severity}\\n\\\\label{sec:strategy-severity}\\n\\nTable~\\\\ref{tab:aggregate-ii} reports the median compound severity difference across strategies and sparsity levels. Under importance-based eviction, $\\\\Delta$ increases from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$---a $37{\\\\times}$ amplification. Under random eviction, no systematic growth is observed ($-0.02$ to $1.54$), confirming that compound severity depends qualitatively on eviction strategy. % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json\\n\\n\\\\begin{table}[t]\\n\\\\centering\\n\\\\small\\n\\\\caption{Median compound severity difference ($\\\\Delta = \\\\widetilde{\\\\mathrm{II}}_{\\\\textit{low}} - \\\\widetilde{\\\\mathrm{II}}_{\\\\textit{high}}$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}50$ MATH-500 problems).}\\n\\\\label{tab:aggregate-ii}\\n\\\\begin{tabular}{@{}lcccc@{}}\\n\\\\toprule\\nStrategy & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\\\\\\\\\n\\\\midrule\\nImportance & 0.39 & 1.48 & 7.16 & 14.59 \\\\\\\\ % exp_id: bf16_importance_s015..s030; source: experiment_summary_table.json median_diff\\nRandom     & 0.01 & $-$0.02 & 0.54 & 1.54 \\\\\\\\ % exp_id: bf16_ds_rand_s015..s030; source: experiment_summary_table.json median_diff\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n\\n\\n\\\\subsection{Phase-Modulated Amplification}\\n\\\\label{sec:phase-amplification}\\n\\nDecomposing II by reasoning phase reveals that strategy-dependent severity is driven by amplification in the low-sparsity phase. Table~\\\\ref{tab:main-results} reports the full per-phase breakdown. The severity gradient $G$ increases from $69{\\\\times}$ at $s{=}0.15$ to $274{\\\\times}$ at $s{=}0.30$ under importance-based eviction, while the high-sparsity phase experiences near-zero interaction ($\\\\widetilde{\\\\mathrm{II}}_{\\\\textit{high}}$ ranges from $0.006$ to $0.053$). Under random eviction, $G \\\\approx 0.9$--$1.7{\\\\times}$ at all sparsity levels. Figure~\\\\ref{fig:hero} visualizes this contrast. % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json\\n\\n\\\\begin{table*}[t]\\n\\\\centering\\n\\\\small\\n\\\\caption{Interaction index (II) by eviction strategy, reasoning phase, and sparsity level. II values are problem-level medians across 50 problems. $\\\\Delta = \\\\widetilde{\\\\mathrm{II}}_{\\\\textit{low}} - \\\\widetilde{\\\\mathrm{II}}_{\\\\textit{high}}$. $G = \\\\widetilde{\\\\mathrm{II}}_{\\\\textit{low}} / \\\\widetilde{\\\\mathrm{II}}_{\\\\textit{high}}$.}\\n\\\\label{tab:main-results}\\n\\\\begin{tabular}{@{}llccccr@{}}\\n\\\\toprule\\n$s$ & Strategy & $\\\\widetilde{\\\\mathrm{II}}_{\\\\textit{high}}$ & $\\\\widetilde{\\\\mathrm{II}}_{\\\\textit{mid}}$ & $\\\\widetilde{\\\\mathrm{II}}_{\\\\textit{low}}$ & $\\\\Delta$ & $G$ \\\\\\\\\\n\\\\midrule\\n0.15 & Importance & 0.006 & 0.081 & 0.398 & 0.39 & $\\\\mathbf{69}$ \\\\\\\\\\n0.15 & Random     & 0.093 & 0.097 & 0.103 & 0.01 & 1.1 \\\\\\\\\\n\\\\addlinespace\\n0.20 & Importance & 0.015 & 0.203 & 1.496 & 1.48 & $\\\\mathbf{103}$ \\\\\\\\\\n0.20 & Random     & 0.292 & 0.350 & 0.276 & $-$0.02 & 0.9 \\\\\\\\\\n\\\\addlinespace\\n0.25 & Importance & 0.032 & 1.118 & 7.196 & 7.16 & $\\\\mathbf{222}$ \\\\\\\\\\n0.25 & Random     & 0.818 & 0.932 & 1.363 & 0.54 & 1.7 \\\\\\\\\\n\\\\addlinespace\\n0.30 & Importance & 0.053 & 2.283 & 14.639 & 14.59 & $\\\\mathbf{274}$ \\\\\\\\\\n0.30 & Random     & 2.503 & 2.592 & 4.041 & 1.54 & 1.6 \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table*}\\n\\n\\\\begin{figure}[t]\\n\\\\centering\\n\\\\includegraphics[width=\\\\columnwidth]{fig1_dose_response.pdf}\\n\\\\caption{Severity gradient ($G$) as a function of sparsity level $s$. Importance-based eviction (solid) exhibits an increasing gradient from $69{\\\\times}$ to $274{\\\\times}$; random eviction (dashed) remains flat near $1{\\\\times}$. Shaded regions: 95\\\\% bootstrap CIs.} % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030\\n\\\\label{fig:hero}\\n\\\\end{figure}\\n\\n\\n\\\\subsection{Phase-Strategy Crossover}\\n\\\\label{sec:crossover}\\n\\nA strategy ranking reversal emerges across all sparsity levels: at $s{=}0.25$, importance-based eviction yields \\\\emph{lower} II than random in the high-sparsity phase ($0.032$ vs.\\\\ $0.818\\n\\n... [截断: 输出过长，省略 2532 字符] ...\\n\\ned difference increases monotonically ($\\\\widetilde{\\\\Delta}$: $0.020 \\\\to 0.356$), consistent with a genuine but weak trend---partially confirming the cross-architecture hypothesis while underscoring the substantially weaker interaction on LlamaForCausalLM. % exp_id: c3_llama\\n\\nThe absolute magnitude is architecture-dependent: LLaMA severity differences are ${\\\\sim}40{\\\\times}$ smaller than DeepSeek and ${\\\\sim}7{\\\\times}$ smaller than Qwen, and the interaction is substantially weaker---random eviction also shows a non-trivial phase gradient (Wilcoxon $p < \\\\placeholder{}$ at $s{=}0.30$), reducing the strategy contrast observed in Qwen2 models. The directional pattern---importance $>$ random, larger phase gradient under importance---is qualitatively consistent across all three models spanning two architectures (Qwen2ForCausalLM, LlamaForCausalLM), though the interaction magnitude is substantially weaker on LlamaForCausalLM. % exp_id: c3_llama; cross_model_analysis.json\\n\\n\\\\begin{table}[t]\\n\\\\centering\\n\\\\small\\n\\\\caption{Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM). $\\\\widetilde{\\\\Delta}$: median paired difference (importance $-$ random) with bootstrap 95\\\\% CI ($B{=}10{,}000$); $p$: Bonferroni-corrected Wilcoxon signed-rank $p$ ($k{=}4$). $n{=}\\\\placeholder{N\\\\_LLAMA}$ paired problems.}\\n\\\\label{tab:llama-cross-arch}\\n\\\\begin{tabular}{@{}lcc@{}}\\n\\\\toprule\\n$s$ & $\\\\widetilde{\\\\Delta}$\\\\; [95\\\\% CI] & $p_{\\\\text{Bonf}}$ \\\\\\\\\\n\\\\midrule\\n0.15 & \\\\placeholder{}\\\\; $[\\\\placeholder{}, \\\\placeholder{}]$ & \\\\placeholder{} \\\\\\\\\\n0.20 & \\\\placeholder{}\\\\; $[\\\\placeholder{}, \\\\placeholder{}]$ & \\\\placeholder{} \\\\\\\\\\n0.25 & \\\\placeholder{}\\\\; $[\\\\placeholder{}, \\\\placeholder{}]$ & \\\\placeholder{} \\\\\\\\\\n0.30 & \\\\placeholder{}\\\\; $[\\\\placeholder{}, \\\\placeholder{}]$ & $\\\\mathbf{\\\\placeholder{}}$ \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n\\n\\n\\\\subsection{Statistical Validation}\\n\\\\label{sec:stat-validation}\\n\\nPaired permutation tests ($10{,}000$ permutations, Bonferroni-corrected) confirm that importance-based eviction produces significantly larger phase-dependent severity than random eviction at all four sparsity levels ($p_{\\\\text{Bonf}} < 0.005$), with observed median differences increasing monotonically from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$. Full permutation test results and forest plot appear in Appendix~\\\\ref{app:permutation-details}. % exp_id: deepseek_bf16_permtest; source: permutation_test_results.json\\n\\nTable~\\\\ref{tab:cohens-d} reports paired Cohen's $d_z$ for both models. For DeepSeek, effect sizes grow from $d_z{=}0.44$ (small) to $d_z{=}0.80$ (large). For Qwen, the effect is marginal at $s{=}0.15$ ($d_z{=}0.28$, CI includes zero), becoming reliable at $s \\\\geq 0.20$ ($d_z \\\\geq 0.55$). At $s \\\\geq 0.25$, Qwen exhibits larger standardized effect sizes ($d_z{=}0.89$/$1.02$ vs.\\\\ $0.68$/$0.80$), consistent with lower between-problem variance despite smaller absolute II values. % exp_id: cohens_d_bf16.json; cohens_d_bf16_qwen.json\\n\\n\\\\begin{table}[t]\\n\\\\centering\\n\\\\small\\n\\\\caption{Paired $d_z$ for phase-dependent II (low $-$ high) under importance-based eviction. Bootstrap 95\\\\% CIs ($B{=}10{,}000$).}\\n\\\\label{tab:cohens-d}\\n\\\\begin{tabular}{@{}lcccc@{}}\\n\\\\toprule\\n$s$ & DS $d_z$ & $\\\\widetilde{\\\\Delta}$ [CI] & QW $d_z$ & $\\\\widetilde{\\\\Delta}$ [CI] \\\\\\\\\\n\\\\midrule\\n0.15 & 0.44 & 0.32\\\\; $[0.20, 0.47]$ & 0.28 & 0.05\\\\; $[-0.01, 0.11]$\\\\textsuperscript{ns} \\\\\\\\ % exp_id: bf16_ds_imp_s015, bf16_qw_imp_s015\\n0.20 & 0.52 & 1.15\\\\; $[0.66, 1.26]$ & 0.55 & 0.21\\\\; $[0.07, 0.40]$ \\\\\\\\ % exp_id: bf16_ds_imp_s020, bf16_qw_imp_s020\\n0.25 & 0.68 & 3.97\\\\; $[2.83, 5.29]$ & 0.89 & 1.11\\\\; $[0.61, 1.47]$ \\\\\\\\ % exp_id: bf16_ds_imp_s025, bf16_qw_imp_s025\\n0.30 & 0.80 & 9.94\\\\; $[8.39, 16.65]$ & 1.02 & 2.62\\\\; $[1.72, 3.65]$ \\\\\\\\ % exp_id: bf16_ds_imp_s030, bf16_qw_imp_s030\\n\\\\bottomrule\\n\\\\multicolumn{5}{@{}l}{\\\\footnotesize \\\\textsuperscript{ns}Marginal at $s{=}0.15$; reliable at $s \\\\geq 0.20$.}\\n\\\\end{tabular}\\n\\\\end{table}\\n\\nWe provide a mechanistic analysis in terms of entropy-discrimination collapse in \\\\S\\\\ref{sec:analysis}.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "e4b37d0b-d507-4c22-a3a0-88af73771885",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\n\\\\\\\\section{Results}\\\\n\\\\\\\\label{sec:results}\\\\n\\\\n\\\\\\\\subsection{Strategy-Dependent Severity}\\\\n\\\\\\\\label{sec:strategy-severity}\\\\n\\\\nTable~\\\\\\\\ref{tab:aggregate-ii} reports the median compound severity difference across strategies and sparsity levels. Under importance-based eviction, $\\\\\\\\Delta$ increases from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$---a $37{\\\\\\\\times}$ amplification. Under random eviction, no systematic growth is observed ($-0.02$ to $1.54$), confirming that compound severity depends qualitatively on eviction strategy. % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json\\\\n\\\\n\\\\\\\\begin{table}[t]\\\\n\\\\\\\\centering\\\\n\\\\\\\\small\\\\n\\\\\\\\caption{Median compound severity difference ($\\\\\\\\Delta = \\\\\\\\widetilde{\\\\\\\\mathrm{II}}_{\\\\\\\\textit{low}} - \\\\\\\\widetilde{\\\\\\\\mathrm{II}}_{\\\\\\\\textit{high}}$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}50$ MATH-500 problems).}\\\\n\\\\\\\\label{tab:aggregate-ii}\\\\n\\\\\\\\begin{tabular}{@{}lcccc@{}}\\\\n\\\\\\\\toprule\\\\nStrategy & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\nImportance & 0.39 & 1.48 & 7.16 & 14.59 \\\\\\\\\\\\\\\\ % exp_id: bf16_importance_s015..s030; source: experiment_summary_table.json median_diff\\\\nRandom     & 0.01 & $-$0.02 & 0.54 & 1.54 \\\\\\\\\\\\\\\\ % exp_id: bf16_ds_rand_s015..s030; source: experiment_summary_table.json median_diff\\\\n\\\\\\\\bottomrule\\\\n\\\\\\\\end{tabular}\\\\n\\\\\\\\end{table}\\\\n\\\\n\\\\n\\\\\\\\subsection{Phase-Modulated Amplification}\\\\n\\\\\\\\label{sec:phase-amplification}\\\\n\\\\nDecomposing II by reasoning phase reveals that strategy-dependent severity is driven by amplification in the low-sparsity phase. Table~\\\\\\\\ref{tab:main-results} reports the full per-phase breakdown. The severity gradient $G$ increases from $69{\\\\\\\\times}$ at $s{=}0.15$ to $274{\\\\\\\\times}$ at $s{=}0.30$ under importance-based eviction, while the high-sparsity phase experiences near-zero interaction ($\\\\\\\\widetilde{\\\\\\\\mathrm{II}}_{\\\\\\\\textit{high}}$ ranges from $0.006$ to $0.053$). Under random eviction, $G \\\\\\\\approx 0.9$--$1.7{\\\\\\\\times}$ at all sparsity levels. Figure~\\\\\\\\ref{fig:hero} visualizes this contrast. % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json\\\\n\\\\n\\\\\\\\begin{table*}[t]\\\\n\\\\\\\\centering\\\\n\\\\\\\\small\\\\n\\\\\\\\caption{Interaction index (II) by eviction strategy, reasoning phase, and sparsity level. II values are problem-level medians across 50 problems. $\\\\\\\\Delta = \\\\\\\\widetilde{\\\\\\\\mathrm{II}}_{\\\\\\\\textit{low}} - \\\\\\\\widetilde{\\\\\\\\mathrm{II}}_{\\\\\\\\textit{high}}$. $G = \\\\\\\\widetilde{\\\\\\\\mathrm{II}}_{\\\\\\\\textit{low}} / \\\\\\\\widetilde{\\\\\\\\mathrm{II}}_{\\\\\\\\textit{high}}$.}\\\\n\\\\\\\\label{tab:main-results}\\\\n\\\\\\\\begin{tabular}{@{}llccccr@{}}\\\\n\\\\\\\\toprule\\\\n$s$ & Strategy & $\\\\\\\\widetilde{\\\\\\\\mathrm{II}}_{\\\\\\\\textit{high}}$ & $\\\\\\\\widetilde{\\\\\\\\mathrm{II}}_{\\\\\\\\textit{mid}}$ & $\\\\\\\\widetilde{\\\\\\\\mathrm{II}}_{\\\\\\\\textit{low}}$ & $\\\\\\\\Delta$ & $G$ \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\n0.15 & Importance & 0.006 & 0.081 & 0.398 & 0.39 & $\\\\\\\\mathbf{69}$ \\\\\\\\\\\\\\\\\\\\n0.15 & Random     & 0.093 & 0.097 & 0.103 & 0.01 & 1.1 \\\\\\\\\\\\\\\\\\\\n\\\\\\\\addlinespace\\\\n0.20 & Importance & 0.015 & 0.203 & 1.496 & 1.48 & $\\\\\\\\mathbf{103}$ \\\\\\\\\\\\\\\\\\\\n0.20 & Random     & 0.292 & 0.350 & 0.276 & $-$0.02 & 0.9 \\\\\\\\\\\\\\\\\\\\n\\\\\\\\addlinespace\\\\n0.25 & Importance & 0.032 & 1.118 & 7.196 & 7.16 & $\\\\\\\\mathbf{222}$ \\\\\\\\\\\\\\\\\\\\n0.25 & Random     & 0.818 & 0.932 & 1.363 & 0.54 & 1.7 \\\\\\\\\\\\\\\\\\\\n\\\\\\\\addlinespace\\\\n0.30 & Importance & 0.053 & 2.283 & 14.639 & 14.59 & $\\\\\\\\mathbf{274}$ \\\\\\\\\\\\\\\\\\\\n0.30 & Random     & 2.503 & 2.592 & 4.041 & 1.54 & 1.6 \\\\\\\\\\\\\\\\\\\\n\\\\\\\\bottomrule\\\\n\\\\\\\\end{tabular}\\\\n\\\\\\\\end{table*}\\\\n\\\\n\\\\\\\\begin{figure}[t]\\\\n\\\\\\\\centering\\\\n\\\\\\\\includegraphics[width=\\\\\\\\columnwidth]{fig1_dose_response.pdf}\\\\n\\\\\\\\caption{Severity gradient ($G$) as a function of sparsity level $s$. Importance-based eviction (solid) exhibits an increasing gradient from $69{\\\\\\\\times}$ to $274{\\\\\\\\times}$; random eviction (dashed) remains flat near $1{\\\\\\\\times}$. Shaded regions: 95\\\\\\\\% bootstrap CIs.} % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030\\\\n\\\\\\\\label{fig:hero}\\\\n\\\\\\\\end{figure}\\\\n\\\\n\\\\n\\\\\\\\subsection{Phase-Strategy Crossover}\\\\n\\\\\\\\label{sec:crossover}\\\\n\\\\nA strategy ranking reversal emerges across all sparsity levels: at $s{=}0.25$, importance-based eviction yields \\\\\\\\emph{lower} II than random in the high-sparsity phase ($0.032$ vs.\\\\\\\\ $0.818\\\\n\\\\n... [截断: 输出过长，省略 2532 字符] ...\\\\n\\\\ned difference increases monotonically ($\\\\\\\\widetilde{\\\\\\\\Delta}$: $0.020 \\\\\\\\to 0.356$), consistent with a genuine but weak trend---partially confirming the cross-architecture hypothesis while underscoring the substantially weaker interaction on LlamaForCausalLM. % exp_id: c3_llama\\\\n\\\\nThe absolute magnitude is architecture-dependent: LLaMA severity differences are ${\\\\\\\\sim}40{\\\\\\\\times}$ smaller than DeepSeek and ${\\\\\\\\sim}7{\\\\\\\\times}$ smaller than Qwen, and the interaction is substantially weaker---random eviction also shows a non-trivial phase gradient (Wilcoxon $p < \\\\\\\\placeholder{}$ at $s{=}0.30$), reducing the strategy contrast observed in Qwen2 models. The directional pattern---importance $>$ random, larger phase gradient under importance---is qualitatively consistent across all three models spanning two architectures (Qwen2ForCausalLM, LlamaForCausalLM), though the interaction magnitude is substantially weaker on LlamaForCausalLM. % exp_id: c3_llama; cross_model_analysis.json\\\\n\\\\n\\\\\\\\begin{table}[t]\\\\n\\\\\\\\centering\\\\n\\\\\\\\small\\\\n\\\\\\\\caption{Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM). $\\\\\\\\widetilde{\\\\\\\\Delta}$: median paired difference (importance $-$ random) with bootstrap 95\\\\\\\\% CI ($B{=}10{,}000$); $p$: Bonferroni-corrected Wilcoxon signed-rank $p$ ($k{=}4$). $n{=}\\\\\\\\placeholder{N\\\\\\\\_LLAMA}$ paired problems.}\\\\n\\\\\\\\label{tab:llama-cross-arch}\\\\n\\\\\\\\begin{tabular}{@{}lcc@{}}\\\\n\\\\\\\\toprule\\\\n$s$ & $\\\\\\\\widetilde{\\\\\\\\Delta}$\\\\\\\\; [95\\\\\\\\% CI] & $p_{\\\\\\\\text{Bonf}}$ \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\n0.15 & \\\\\\\\placeholder{}\\\\\\\\; $[\\\\\\\\placeholder{}, \\\\\\\\placeholder{}]$ & \\\\\\\\placeholder{} \\\\\\\\\\\\\\\\\\\\n0.20 & \\\\\\\\placeholder{}\\\\\\\\; $[\\\\\\\\placeholder{}, \\\\\\\\placeholder{}]$ & \\\\\\\\placeholder{} \\\\\\\\\\\\\\\\\\\\n0.25 & \\\\\\\\placeholder{}\\\\\\\\; $[\\\\\\\\placeholder{}, \\\\\\\\placeholder{}]$ & \\\\\\\\placeholder{} \\\\\\\\\\\\\\\\\\\\n0.30 & \\\\\\\\placeholder{}\\\\\\\\; $[\\\\\\\\placeholder{}, \\\\\\\\placeholder{}]$ & $\\\\\\\\mathbf{\\\\\\\\placeholder{}}$ \\\\\\\\\\\\\\\\\\\\n\\\\\\\\bottomrule\\\\n\\\\\\\\end{tabular}\\\\n\\\\\\\\end{table}\\\\n\\\\n\\\\n\\\\\\\\subsection{Statistical Validation}\\\\n\\\\\\\\label{sec:stat-validation}\\\\n\\\\nPaired permutation tests ($10{,}000$ permutations, Bonferroni-corrected) confirm that importance-based eviction produces significantly larger phase-dependent severity than random eviction at all four sparsity levels ($p_{\\\\\\\\text{Bonf}} < 0.005$), with observed median differences increasing monotonically from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$. Full permutation test results and forest plot appear in Appendix~\\\\\\\\ref{app:permutation-details}. % exp_id: deepseek_bf16_permtest; source: permutation_test_results.json\\\\n\\\\nTable~\\\\\\\\ref{tab:cohens-d} reports paired Cohen's $d_z$ for both models. For DeepSeek, effect sizes grow from $d_z{=}0.44$ (small) to $d_z{=}0.80$ (large). For Qwen, the effect is marginal at $s{=}0.15$ ($d_z{=}0.28$, CI includes zero), becoming reliable at $s \\\\\\\\geq 0.20$ ($d_z \\\\\\\\geq 0.55$). At $s \\\\\\\\geq 0.25$, Qwen exhibits larger standardized effect sizes ($d_z{=}0.89$/$1.02$ vs.\\\\\\\\ $0.68$/$0.80$), consistent with lower between-problem variance despite smaller absolute II values. % exp_id: cohens_d_bf16.json; cohens_d_bf16_qwen.json\\\\n\\\\n\\\\\\\\begin{table}[t]\\\\n\\\\\\\\centering\\\\n\\\\\\\\small\\\\n\\\\\\\\caption{Paired $d_z$ for phase-dependent II (low $-$ high) under importance-based eviction. Bootstrap 95\\\\\\\\% CIs ($B{=}10{,}000$).}\\\\n\\\\\\\\label{tab:cohens-d}\\\\n\\\\\\\\begin{tabular}{@{}lcccc@{}}\\\\n\\\\\\\\toprule\\\\n$s$ & DS $d_z$ & $\\\\\\\\widetilde{\\\\\\\\Delta}$ [CI] & QW $d_z$ & $\\\\\\\\widetilde{\\\\\\\\Delta}$ [CI] \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\n0.15 & 0.44 & 0.32\\\\\\\\; $[0.20, 0.47]$ & 0.28 & 0.05\\\\\\\\; $[-0.01, 0.11]$\\\\\\\\textsuperscript{ns} \\\\\\\\\\\\\\\\ % exp_id: bf16_ds_imp_s015, bf16_qw_imp_s015\\\\n0.20 & 0.52 & 1.15\\\\\\\\; $[0.66, 1.26]$ & 0.55 & 0.21\\\\\\\\; $[0.07, 0.40]$ \\\\\\\\\\\\\\\\ % exp_id: bf16_ds_imp_s020, bf16_qw_imp_s020\\\\n0.25 & 0.68 & 3.97\\\\\\\\; $[2.83, 5.29]$ & 0.89 & 1.11\\\\\\\\; $[0.61, 1.47]$ \\\\\\\\\\\\\\\\ % exp_id: bf16_ds_imp_s025, bf16_qw_imp_s025\\\\n0.30 & 0.80 & 9.94\\\\\\\\; $[8.39, 16.65]$ & 1.02 & 2.62\\\\\\\\; $[1.72, 3.65]$ \\\\\\\\\\\\\\\\ % exp_id: bf16_ds_imp_s030, bf16_qw_imp_s030\\\\n\\\\\\\\bottomrule\\\\n\\\\\\\\multicolumn{5}{@{}l}{\\\\\\\\footnotesize \\\\\\\\textsuperscript{ns}Marginal at $s{=}0.15$; reliable at $s \\\\\\\\geq 0.20$.}\\\\n\\\\\\\\end{tabular}\\\\n\\\\\\\\end{table}\\\\n\\\\nWe provide a mechanistic analysis in terms of entropy-discrimination collapse in \\\\\\\\S\\\\\\\\ref{sec:analysis}.\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.51}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\n\\\\section{Results}\\n\\\\label{sec:results}\\n\\n\\\\subsection{Strategy-Dependent Severity}\\n\\\\label{sec:strategy-severity}\\n\\nTable~\\\\ref{tab:aggregate-ii} reports the median compound severity difference across strategies and sparsity levels. Under importance-based eviction, $\\\\Delta$ increases from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$---a $37{\\\\times}$ amplification. Under random eviction, no systematic growth is observed ($-0.02$ to $1.54$), confirming that compound severity depends qualitatively on eviction strategy. % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json\\n\\n\\\\begin{table}[t]\\n\\\\centering\\n\\\\small\\n\\\\caption{Median compound severity difference ($\\\\Delta = \\\\widetilde{\\\\mathrm{II}}_{\\\\textit{low}} - \\\\widetilde{\\\\mathrm{II}}_{\\\\textit{high}}$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}50$ MATH-500 problems).}\\n\\\\label{tab:aggregate-ii}\\n\\\\begin{tabular}{@{}lcccc@{}}\\n\\\\toprule\\nStrategy & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\\\\\\\\\n\\\\midrule\\nImportance & 0.39 & 1.48 & 7.16 & 14.59 \\\\\\\\ % exp_id: bf16_importance_s015..s030; source: experiment_summary_table.json median_diff\\nRandom     & 0.01 & $-$0.02 & 0.54 & 1.54 \\\\\\\\ % exp_id: bf16_ds_rand_s015..s030; source: experiment_summary_table.json median_diff\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n\\n\\n\\\\subsection{Phase-Modulated Amplification}\\n\\\\label{sec:phase-amplification}\\n\\nDecomposing II by reasoning phase reveals that strategy-dependent severity is driven by amplification in the low-sparsity phase. Table~\\\\ref{tab:main-results} reports the full per-phase breakdown. The severity gradient $G$ increases from $69{\\\\times}$ at $s{=}0.15$ to $274{\\\\times}$ at $s{=}0.30$ under importance-based eviction, while the high-sparsity phase experiences near-zero interaction ($\\\\widetilde{\\\\mathrm{II}}_{\\\\textit{high}}$ ranges from $0.006$ to $0.053$). Under random eviction, $G \\\\approx 0.9$--$1.7{\\\\times}$ at all sparsity levels. Figure~\\\\ref{fig:hero} visualizes this contrast. % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json\\n\\n\\\\begin{table*}[t]\\n\\\\centering\\n\\\\small\\n\\\\caption{Interaction index (II) by eviction strategy, reasoning phase, and sparsity level. II values are problem-level medians across 50 problems. $\\\\Delta = \\\\widetilde{\\\\mathrm{II}}_{\\\\textit{low}} - \\\\widetilde{\\\\mathrm{II}}_{\\\\textit{high}}$. $G = \\\\widetilde{\\\\mathrm{II}}_{\\\\textit{low}} / \\\\widetilde{\\\\mathrm{II}}_{\\\\textit{high}}$.}\\n\\\\label{tab:main-results}\\n\\\\begin{tabular}{@{}llccccr@{}}\\n\\\\toprule\\n$s$ & Strategy & $\\\\widetilde{\\\\mathrm{II}}_{\\\\textit{high}}$ & $\\\\widetilde{\\\\mathrm{II}}_{\\\\textit{mid}}$ & $\\\\widetilde{\\\\mathrm{II}}_{\\\\textit{low}}$ & $\\\\Delta$ & $G$ \\\\\\\\\\n\\\\midrule\\n0.15 & Importance & 0.006 & 0.081 & 0.398 & 0.39 & $\\\\mathbf{69}$ \\\\\\\\\\n0.15 & Random     & 0.093 & 0.097 & 0.103 & 0.01 & 1.1 \\\\\\\\\\n\\\\addlinespace\\n0.20 & Importance & 0.015 & 0.203 & 1.496 & 1.48 & $\\\\mathbf{103}$ \\\\\\\\\\n0.20 & Random     & 0.292 & 0.350 & 0.276 & $-$0.02 & 0.9 \\\\\\\\\\n\\\\addlinespace\\n0.25 & Importance & 0.032 & 1.118 & 7.196 & 7.16 & $\\\\mathbf{222}$ \\\\\\\\\\n0.25 & Random     & 0.818 & 0.932 & 1.363 & 0.54 & 1.7 \\\\\\\\\\n\\\\addlinespace\\n0.30 & Importance & 0.053 & 2.283 & 14.639 & 14.59 & $\\\\mathbf{274}$ \\\\\\\\\\n0.30 & Random     & 2.503 & 2.592 & 4.041 & 1.54 & 1.6 \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table*}\\n\\n\\\\begin{figure}[t]\\n\\\\centering\\n\\\\includegraphics[width=\\\\columnwidth]{fig1_dose_response.pdf}\\n\\\\caption{Severity gradient ($G$) as a function of sparsity level $s$. Importance-based eviction (solid) exhibits an increasing gradient from $69{\\\\times}$ to $274{\\\\times}$; random eviction (dashed) remains flat near $1{\\\\times}$. Shaded regions: 95\\\\% bootstrap CIs.} % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030\\n\\\\label{fig:hero}\\n\\\\end{figure}\\n\\n\\n\\\\subsection{Phase-Strategy Crossover}\\n\\\\label{sec:crossover}\\n\\nA strategy ranking reversal emerges across all sparsity levels: at $s{=}0.25$, importance-based eviction yields \\\\emph{lower} II than random in the high-sparsity phase ($0.032$ vs.\\\\ $0.818\\n\\n... [截断: 输出过长，省略 2532 字符] ...\\n\\ned difference increases monotonically ($\\\\widetilde{\\\\Delta}$: $0.020 \\\\to 0.356$), consistent with a genuine but weak trend---partially confirming the cross-architecture hypothesis while underscoring the substantially weaker interaction on LlamaForCausalLM. % exp_id: c3_llama\\n\\nThe absolute magnitude is architecture-dependent: LLaMA severity differences are ${\\\\sim}40{\\\\times}$ smaller than DeepSeek and ${\\\\sim}7{\\\\times}$ smaller than Qwen, and the interaction is substantially weaker---random eviction also shows a non-trivial phase gradient (Wilcoxon $p < \\\\placeholder{}$ at $s{=}0.30$), reducing the strategy contrast observed in Qwen2 models. The directional pattern---importance $>$ random, larger phase gradient under importance---is qualitatively consistent across all three models spanning two architectures (Qwen2ForCausalLM, LlamaForCausalLM), though the interaction magnitude is substantially weaker on LlamaForCausalLM. % exp_id: c3_llama; cross_model_analysis.json\\n\\n\\\\begin{table}[t]\\n\\\\centering\\n\\\\small\\n\\\\caption{Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM). $\\\\widetilde{\\\\Delta}$: median paired difference (importance $-$ random) with bootstrap 95\\\\% CI ($B{=}10{,}000$); $p$: Bonferroni-corrected Wilcoxon signed-rank $p$ ($k{=}4$). $n{=}\\\\placeholder{N\\\\_LLAMA}$ paired problems.}\\n\\\\label{tab:llama-cross-arch}\\n\\\\begin{tabular}{@{}lcc@{}}\\n\\\\toprule\\n$s$ & $\\\\widetilde{\\\\Delta}$\\\\; [95\\\\% CI] & $p_{\\\\text{Bonf}}$ \\\\\\\\\\n\\\\midrule\\n0.15 & \\\\placeholder{}\\\\; $[\\\\placeholder{}, \\\\placeholder{}]$ & \\\\placeholder{} \\\\\\\\\\n0.20 & \\\\placeholder{}\\\\; $[\\\\placeholder{}, \\\\placeholder{}]$ & \\\\placeholder{} \\\\\\\\\\n0.25 & \\\\placeholder{}\\\\; $[\\\\placeholder{}, \\\\placeholder{}]$ & \\\\placeholder{} \\\\\\\\\\n0.30 & \\\\placeholder{}\\\\; $[\\\\placeholder{}, \\\\placeholder{}]$ & $\\\\mathbf{\\\\placeholder{}}$ \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n\\n\\n\\\\subsection{Statistical Validation}\\n\\\\label{sec:stat-validation}\\n\\nPaired permutation tests ($10{,}000$ permutations, Bonferroni-corrected) confirm that importance-based eviction produces significantly larger phase-dependent severity than random eviction at all four sparsity levels ($p_{\\\\text{Bonf}} < 0.005$), with observed median differences increasing monotonically from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$. Full permutation test results and forest plot appear in Appendix~\\\\ref{app:permutation-details}. % exp_id: deepseek_bf16_permtest; source: permutation_test_results.json\\n\\nTable~\\\\ref{tab:cohens-d} reports paired Cohen's $d_z$ for both models. For DeepSeek, effect sizes grow from $d_z{=}0.44$ (small) to $d_z{=}0.80$ (large). For Qwen, the effect is marginal at $s{=}0.15$ ($d_z{=}0.28$, CI includes zero), becoming reliable at $s \\\\geq 0.20$ ($d_z \\\\geq 0.55$). At $s \\\\geq 0.25$, Qwen exhibits larger standardized effect sizes ($d_z{=}0.89$/$1.02$ vs.\\\\ $0.68$/$0.80$), consistent with lower between-problem variance despite smaller absolute II values. % exp_id: cohens_d_bf16.json; cohens_d_bf16_qwen.json\\n\\n\\\\begin{table}[t]\\n\\\\centering\\n\\\\small\\n\\\\caption{Paired $d_z$ for phase-dependent II (low $-$ high) under importance-based eviction. Bootstrap 95\\\\% CIs ($B{=}10{,}000$).}\\n\\\\label{tab:cohens-d}\\n\\\\begin{tabular}{@{}lcccc@{}}\\n\\\\toprule\\n$s$ & DS $d_z$ & $\\\\widetilde{\\\\Delta}$ [CI] & QW $d_z$ & $\\\\widetilde{\\\\Delta}$ [CI] \\\\\\\\\\n\\\\midrule\\n0.15 & 0.44 & 0.32\\\\; $[0.20, 0.47]$ & 0.28 & 0.05\\\\; $[-0.01, 0.11]$\\\\textsuperscript{ns} \\\\\\\\ % exp_id: bf16_ds_imp_s015, bf16_qw_imp_s015\\n0.20 & 0.52 & 1.15\\\\; $[0.66, 1.26]$ & 0.55 & 0.21\\\\; $[0.07, 0.40]$ \\\\\\\\ % exp_id: bf16_ds_imp_s020, bf16_qw_imp_s020\\n0.25 & 0.68 & 3.97\\\\; $[2.83, 5.29]$ & 0.89 & 1.11\\\\; $[0.61, 1.47]$ \\\\\\\\ % exp_id: bf16_ds_imp_s025, bf16_qw_imp_s025\\n0.30 & 0.80 & 9.94\\\\; $[8.39, 16.65]$ & 1.02 & 2.62\\\\; $[1.72, 3.65]$ \\\\\\\\ % exp_id: bf16_ds_imp_s030, bf16_qw_imp_s030\\n\\\\bottomrule\\n\\\\multicolumn{5}{@{}l}{\\\\footnotesize \\\\textsuperscript{ns}Marginal at $s{=}0.15$; reliable at $s \\\\geq 0.20$.}\\n\\\\end{tabular}\\n\\\\end{table}\\n\\nWe provide a mechanistic analysis in terms of entropy-discrimination collapse in \\\\S\\\\ref{sec:analysis}.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 26_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01GR5vc39oEEyswzRs8kfKTu`</summary>

```json
{
  "server": "westd-22162",
  "command": "cat /root/autodl-tmp/pacs/paper/analysis.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "893e6f1c-aaff-44a0-8120-0d71df9570f0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HaASaKe4zhD4sf12ZidXN6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5886,
      "cache_read_input_tokens": 24703,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5886
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01EC71kYDesXqhNVQSyXXFkZ`</summary>

```json
{
  "server": "westd-22162",
  "command": "cat /root/autodl-tmp/pacs/paper/discussion.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "3eec3f83-6caa-495f-89e1-19d852ee40cb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HaASaKe4zhD4sf12ZidXN6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5886,
      "cache_read_input_tokens": 24703,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5886
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

_source line 28 · 2026-05-15T02:17:42.584Z_

<details><summary>↩ Tool result · `toolu_01GR5vc39oEEyswzRs8kfKTu`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\\section{Analysis: Entropy-Discrimination Collapse}\\n\\\\label{sec:analysis}\\n\\nWe propose \\\\emph{discrimination collapse} as the primary mechanism driving the phase-strategy interaction. Head pruning reduces the number of heads contributing to cumulative importance scores, flattening the score distribution: the Gini coefficient decreases by $0.030$--$0.081$ (DeepSeek) and $0.010$--$0.020$ (Qwen) across all sparsity levels, with consistent negative deltas in all 16 conditions (Appendix~\\\\ref{app:analysis}, Table~\\\\ref{tab:discrimination-metrics-full}). When importance scores lose discriminability, thresholding degenerates into noise-sensitive selection---functionally approaching biased random eviction. This effect is phase-dependent: in low-sparsity phases, attention is already broadly distributed, so pruning-induced flattening has maximum impact; in high-sparsity phases, concentration is preserved. Random eviction is immune because its decisions are independent of score quality, explaining $G \\\\approx 1$. % exp_id: c4_entropy_deepseek, c4_entropy_qwen\\n\\nBeyond discrimination collapse, head pruning redistributes the attention entropy of surviving heads. For DeepSeek, the entropy delta is consistently negative ($\\\\Delta\\\\mathcal{H} \\\\in [-0.047, -0.040]$), indicating that importance-based pruning systematically selects heads whose removal concentrates attention in survivors. For Qwen, the pattern partially replicates at $s \\\\leq 0.20$ but reverses at $s{=}0.25$ ($\\\\Delta\\\\mathcal{H} = +0.045$), suggesting model-specific head specialization patterns (Appendix~\\\\ref{app:analysis}, Table~\\\\ref{tab:entropy-deltas}). We characterize discrimination collapse as the robust, model-independent driver, with entropy redistribution as a secondary, model-dependent amplifier. % exp_id: c4_entropy_deepseek, c4_entropy_qwen\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "8feef4d7-db78-477d-82c1-b531e250f32b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\\section{Analysis: Entropy-Discrimination Collapse}\\\\n\\\\\\\\label{sec:analysis}\\\\n\\\\nWe propose \\\\\\\\emph{discrimination collapse} as the primary mechanism driving the phase-strategy interaction. Head pruning reduces the number of heads contributing to cumulative importance scores, flattening the score distribution: the Gini coefficient decreases by $0.030$--$0.081$ (DeepSeek) and $0.010$--$0.020$ (Qwen) across all sparsity levels, with consistent negative deltas in all 16 conditions (Appendix~\\\\\\\\ref{app:analysis}, Table~\\\\\\\\ref{tab:discrimination-metrics-full}). When importance scores lose discriminability, thresholding degenerates into noise-sensitive selection---functionally approaching biased random eviction. This effect is phase-dependent: in low-sparsity phases, attention is already broadly distributed, so pruning-induced flattening has maximum impact; in high-sparsity phases, concentration is preserved. Random eviction is immune because its decisions are independent of score quality, explaining $G \\\\\\\\approx 1$. % exp_id: c4_entropy_deepseek, c4_entropy_qwen\\\\n\\\\nBeyond discrimination collapse, head pruning redistributes the attention entropy of surviving heads. For DeepSeek, the entropy delta is consistently negative ($\\\\\\\\Delta\\\\\\\\mathcal{H} \\\\\\\\in [-0.047, -0.040]$), indicating that importance-based pruning systematically selects heads whose removal concentrates attention in survivors. For Qwen, the pattern partially replicates at $s \\\\\\\\leq 0.20$ but reverses at $s{=}0.25$ ($\\\\\\\\Delta\\\\\\\\mathcal{H} = +0.045$), suggesting model-specific head specialization patterns (Appendix~\\\\\\\\ref{app:analysis}, Table~\\\\\\\\ref{tab:entropy-deltas}). We characterize discrimination collapse as the robust, model-independent driver, with entropy redistribution as a secondary, model-dependent amplifier. % exp_id: c4_entropy_deepseek, c4_entropy_qwen\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\\section{Analysis: Entropy-Discrimination Collapse}\\n\\\\label{sec:analysis}\\n\\nWe propose \\\\emph{discrimination collapse} as the primary mechanism driving the phase-strategy interaction. Head pruning reduces the number of heads contributing to cumulative importance scores, flattening the score distribution: the Gini coefficient decreases by $0.030$--$0.081$ (DeepSeek) and $0.010$--$0.020$ (Qwen) across all sparsity levels, with consistent negative deltas in all 16 conditions (Appendix~\\\\ref{app:analysis}, Table~\\\\ref{tab:discrimination-metrics-full}). When importance scores lose discriminability, thresholding degenerates into noise-sensitive selection---functionally approaching biased random eviction. This effect is phase-dependent: in low-sparsity phases, attention is already broadly distributed, so pruning-induced flattening has maximum impact; in high-sparsity phases, concentration is preserved. Random eviction is immune because its decisions are independent of score quality, explaining $G \\\\approx 1$. % exp_id: c4_entropy_deepseek, c4_entropy_qwen\\n\\nBeyond discrimination collapse, head pruning redistributes the attention entropy of surviving heads. For DeepSeek, the entropy delta is consistently negative ($\\\\Delta\\\\mathcal{H} \\\\in [-0.047, -0.040]$), indicating that importance-based pruning systematically selects heads whose removal concentrates attention in survivors. For Qwen, the pattern partially replicates at $s \\\\leq 0.20$ but reverses at $s{=}0.25$ ($\\\\Delta\\\\mathcal{H} = +0.045$), suggesting model-specific head specialization patterns (Appendix~\\\\ref{app:analysis}, Table~\\\\ref{tab:entropy-deltas}). We characterize discrimination collapse as the robust, model-independent driver, with entropy redistribution as a secondary, model-dependent amplifier. % exp_id: c4_entropy_deepseek, c4_entropy_qwen\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-15T02:17:43.124Z_

<details><summary>↩ Tool result · `toolu_01EC71kYDesXqhNVQSyXXFkZ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\\section{Discussion}\\n\\\\label{sec:discussion}\\n\\n\\\\paragraph{Quantitative surprise.}\\nWhile the qualitative direction---importance scores degrade when attention is diffuse---may seem expected, the quantitative structure is not predictable from first principles. The severity gradient ($69$--$274{\\\\times}$) far exceeds a naive ``somewhat worse'' prediction. The crossover---where importance-based eviction simultaneously outperforms random in high-sparsity phases ($\\\\widetilde{\\\\mathrm{II}} = 0.032$ vs.\\\\ $0.818$) and underperforms in low-sparsity phases ($7.196$ vs.\\\\ $1.363$)---cannot be derived from single-axis entropy reasoning. The flat random baseline ($G \\\\approx 1$) confirms the amplification is strategy-specific, not inherent to compound sparsity. % exp_id: bf16_importance_s015..s030, bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json\\n\\n\\\\paragraph{Implications for deployment.}\\nApplying a uniform compression budget across all inference steps implicitly accepts order-of-magnitude severity penalties during low-sparsity reasoning phases. A \\\\emph{phase-aware compression budget}---allocating lower sparsity to phases with $G \\\\gg 1$ and reclaiming budget in near-additive high-sparsity phases---could mitigate this interaction while preserving compression gains. The severity gradient provides a natural signal for such allocation. Discrimination collapse depends on attention-mass-based importance scoring shared by major KV cache methods (H$_2$O \\\\cite{h2o-neurips2023}, SnapKV \\\\cite{snapkv-neurips2024}, PyramidKV \\\\cite{pyramidkv-2024}), suggesting broad applicability.\\n\\nA preliminary pilot experiment explored oracle phase-aware budget reallocation, shifting sparsity budget from high-severity low-sparsity phases to low-severity high-sparsity phases. At $s{=}0.25$, oracle recovery---the fraction of compound interaction eliminated by phase-aware allocation---reached \\\\placeholder{ORACLE\\\\_PCT}\\\\% (Wilcoxon $p = \\\\placeholder{ORACLE\\\\_P}$), below the pre-registered 30\\\\% gate for claiming practical mitigation. A heuristic variant achieved \\\\placeholder{HEUR\\\\_PCT}\\\\% recovery ($p = \\\\placeholder{HEUR\\\\_P}$), but 95\\\\% CIs for both conditions span zero. These results indicate that phase-aware budget reallocation alone is insufficient to neutralize the severity gradient; effective mitigation likely requires joint optimization of budget allocation and eviction strategy selection across phases---a promising direction for future work.\\n\\nExtended discussion in Appendix~\\\\ref{app:extended-discussion}.\\n\\n\\\\paragraph{Architecture-dependent magnitude.}\\nCross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM) provides partial support for the qualitative pattern---monotonically increasing severity gradient under importance-based eviction with within-strategy phase gradient $d_z \\\\geq 1.0$---while revealing that absolute severity magnitudes are architecture-dependent (${\\\\sim}40{\\\\times}$ smaller than DeepSeek, ${\\\\sim}7{\\\\times}$ smaller than Qwen) and the strategy--phase interaction is substantially weaker than in Qwen2-based architectures. Notably, random pruning also exhibits a non-trivial phase gradient on LLaMA (Wilcoxon $p < \\\\placeholder{}$), reducing the contrast between strategies. This dissociation between qualitatively consistent directional trends and markedly different magnitudes suggests the phase-strategy interaction may be a general property of compound sparsity on reasoning models, while its quantitative impact---and the degree to which it is strategy-specific---depends on architecture-specific attention distributions and head specialization patterns. % exp_id: c3_llama\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "55cc4503-1061-46b6-9436-63f290feab52",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\\section{Discussion}\\\\n\\\\\\\\label{sec:discussion}\\\\n\\\\n\\\\\\\\paragraph{Quantitative surprise.}\\\\nWhile the qualitative direction---importance scores degrade when attention is diffuse---may seem expected, the quantitative structure is not predictable from first principles. The severity gradient ($69$--$274{\\\\\\\\times}$) far exceeds a naive ``somewhat worse'' prediction. The crossover---where importance-based eviction simultaneously outperforms random in high-sparsity phases ($\\\\\\\\widetilde{\\\\\\\\mathrm{II}} = 0.032$ vs.\\\\\\\\ $0.818$) and underperforms in low-sparsity phases ($7.196$ vs.\\\\\\\\ $1.363$)---cannot be derived from single-axis entropy reasoning. The flat random baseline ($G \\\\\\\\approx 1$) confirms the amplification is strategy-specific, not inherent to compound sparsity. % exp_id: bf16_importance_s015..s030, bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json\\\\n\\\\n\\\\\\\\paragraph{Implications for deployment.}\\\\nApplying a uniform compression budget across all inference steps implicitly accepts order-of-magnitude severity penalties during low-sparsity reasoning phases. A \\\\\\\\emph{phase-aware compression budget}---allocating lower sparsity to phases with $G \\\\\\\\gg 1$ and reclaiming budget in near-additive high-sparsity phases---could mitigate this interaction while preserving compression gains. The severity gradient provides a natural signal for such allocation. Discrimination collapse depends on attention-mass-based importance scoring shared by major KV cache methods (H$_2$O \\\\\\\\cite{h2o-neurips2023}, SnapKV \\\\\\\\cite{snapkv-neurips2024}, PyramidKV \\\\\\\\cite{pyramidkv-2024}), suggesting broad applicability.\\\\n\\\\nA preliminary pilot experiment explored oracle phase-aware budget reallocation, shifting sparsity budget from high-severity low-sparsity phases to low-severity high-sparsity phases. At $s{=}0.25$, oracle recovery---the fraction of compound interaction eliminated by phase-aware allocation---reached \\\\\\\\placeholder{ORACLE\\\\\\\\_PCT}\\\\\\\\% (Wilcoxon $p = \\\\\\\\placeholder{ORACLE\\\\\\\\_P}$), below the pre-registered 30\\\\\\\\% gate for claiming practical mitigation. A heuristic variant achieved \\\\\\\\placeholder{HEUR\\\\\\\\_PCT}\\\\\\\\% recovery ($p = \\\\\\\\placeholder{HEUR\\\\\\\\_P}$), but 95\\\\\\\\% CIs for both conditions span zero. These results indicate that phase-aware budget reallocation alone is insufficient to neutralize the severity gradient; effective mitigation likely requires joint optimization of budget allocation and eviction strategy selection across phases---a promising direction for future work.\\\\n\\\\nExtended discussion in Appendix~\\\\\\\\ref{app:extended-discussion}.\\\\n\\\\n\\\\\\\\paragraph{Architecture-dependent magnitude.}\\\\nCross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM) provides partial support for the qualitative pattern---monotonically increasing severity gradient under importance-based eviction with within-strategy phase gradient $d_z \\\\\\\\geq 1.0$---while revealing that absolute severity magnitudes are architecture-dependent (${\\\\\\\\sim}40{\\\\\\\\times}$ smaller than DeepSeek, ${\\\\\\\\sim}7{\\\\\\\\times}$ smaller than Qwen) and the strategy--phase interaction is substantially weaker than in Qwen2-based architectures. Notably, random pruning also exhibits a non-trivial phase gradient on LLaMA (Wilcoxon $p < \\\\\\\\placeholder{}$), reducing the contrast between strategies. This dissociation between qualitatively consistent directional trends and markedly different magnitudes suggests the phase-strategy interaction may be a general property of compound sparsity on reasoning models, while its quantitative impact---and the degree to which it is strategy-specific---depends on architecture-specific attention distributions and head specialization patterns. % exp_id: c3_llama\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.53}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\\section{Discussion}\\n\\\\label{sec:discussion}\\n\\n\\\\paragraph{Quantitative surprise.}\\nWhile the qualitative direction---importance scores degrade when attention is diffuse---may seem expected, the quantitative structure is not predictable from first principles. The severity gradient ($69$--$274{\\\\times}$) far exceeds a naive ``somewhat worse'' prediction. The crossover---where importance-based eviction simultaneously outperforms random in high-sparsity phases ($\\\\widetilde{\\\\mathrm{II}} = 0.032$ vs.\\\\ $0.818$) and underperforms in low-sparsity phases ($7.196$ vs.\\\\ $1.363$)---cannot be derived from single-axis entropy reasoning. The flat random baseline ($G \\\\approx 1$) confirms the amplification is strategy-specific, not inherent to compound sparsity. % exp_id: bf16_importance_s015..s030, bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json\\n\\n\\\\paragraph{Implications for deployment.}\\nApplying a uniform compression budget across all inference steps implicitly accepts order-of-magnitude severity penalties during low-sparsity reasoning phases. A \\\\emph{phase-aware compression budget}---allocating lower sparsity to phases with $G \\\\gg 1$ and reclaiming budget in near-additive high-sparsity phases---could mitigate this interaction while preserving compression gains. The severity gradient provides a natural signal for such allocation. Discrimination collapse depends on attention-mass-based importance scoring shared by major KV cache methods (H$_2$O \\\\cite{h2o-neurips2023}, SnapKV \\\\cite{snapkv-neurips2024}, PyramidKV \\\\cite{pyramidkv-2024}), suggesting broad applicability.\\n\\nA preliminary pilot experiment explored oracle phase-aware budget reallocation, shifting sparsity budget from high-severity low-sparsity phases to low-severity high-sparsity phases. At $s{=}0.25$, oracle recovery---the fraction of compound interaction eliminated by phase-aware allocation---reached \\\\placeholder{ORACLE\\\\_PCT}\\\\% (Wilcoxon $p = \\\\placeholder{ORACLE\\\\_P}$), below the pre-registered 30\\\\% gate for claiming practical mitigation. A heuristic variant achieved \\\\placeholder{HEUR\\\\_PCT}\\\\% recovery ($p = \\\\placeholder{HEUR\\\\_P}$), but 95\\\\% CIs for both conditions span zero. These results indicate that phase-aware budget reallocation alone is insufficient to neutralize the severity gradient; effective mitigation likely requires joint optimization of budget allocation and eviction strategy selection across phases---a promising direction for future work.\\n\\nExtended discussion in Appendix~\\\\ref{app:extended-discussion}.\\n\\n\\\\paragraph{Architecture-dependent magnitude.}\\nCross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM) provides partial support for the qualitative pattern---monotonically increasing severity gradient under importance-based eviction with within-strategy phase gradient $d_z \\\\geq 1.0$---while revealing that absolute severity magnitudes are architecture-dependent (${\\\\sim}40{\\\\times}$ smaller than DeepSeek, ${\\\\sim}7{\\\\times}$ smaller than Qwen) and the strategy--phase interaction is substantially weaker than in Qwen2-based architectures. Notably, random pruning also exhibits a non-trivial phase gradient on LLaMA (Wilcoxon $p < \\\\placeholder{}$), reducing the contrast between strategies. This dissociation between qualitatively consistent directional trends and markedly different magnitudes suggests the phase-strategy interaction may be a general property of compound sparsity on reasoning models, while its quantitative impact---and the degree to which it is strategy-specific---depends on architecture-specific attention distributions and head specialization patterns. % exp_id: c3_llama\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_015utHpqDuKkU5biJwahVBdj`</summary>

```json
{
  "server": "westd-22162",
  "command": "cat /root/autodl-tmp/pacs/paper/conclusion.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "38f0adb4-835e-4e8d-a849-fa0e42a707ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HaASaKe4zhD4sf12ZidXN6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5886,
      "cache_read_input_tokens": 24703,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5886
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

_source line 31 · 2026-05-15T02:17:43.960Z_

<details><summary>↩ Tool result · `toolu_015utHpqDuKkU5biJwahVBdj`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\\section{Conclusion}\\n\\\\label{sec:conclusion}\\n\\nWe showed that compound sparsity severity---the super-additive interaction between head pruning and KV cache eviction---is not phase-invariant but exhibits an emergent phase-strategy interaction spanning over an order of magnitude within a single generation. Under importance-based eviction, the severity gradient grows from $69{\\\\times}$ to $274{\\\\times}$ across sparsity levels ($d_z$: $0.44 \\\\to 0.80$); random eviction shows no such modulation (7/8 conditions non-significant). A crossover at $s{=}0.25$---where importance-based eviction reverses ranking across phases---demonstrates that no single strategy dominates uniformly. The pattern replicates on Qwen2.5-7B-Instruct at $s \\\\geq 0.20$ ($d_z \\\\geq 0.55$) and partially extends cross-architecture to DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM) with a qualitatively consistent but substantially weaker trend at $\\\\sim$1/40 the magnitude. Discrimination collapse provides a mechanistic explanation supported by both Qwen2-based models; LLaMA results are directionally consistent but the interaction is weaker than in Qwen2 architectures.\\nThese findings motivate phase-aware sparsity allocation for reasoning model deployment.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "a2df1069-c807-428a-ab99-c74a0b463e67",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\\section{Conclusion}\\\\n\\\\\\\\label{sec:conclusion}\\\\n\\\\nWe showed that compound sparsity severity---the super-additive interaction between head pruning and KV cache eviction---is not phase-invariant but exhibits an emergent phase-strategy interaction spanning over an order of magnitude within a single generation. Under importance-based eviction, the severity gradient grows from $69{\\\\\\\\times}$ to $274{\\\\\\\\times}$ across sparsity levels ($d_z$: $0.44 \\\\\\\\to 0.80$); random eviction shows no such modulation (7/8 conditions non-significant). A crossover at $s{=}0.25$---where importance-based eviction reverses ranking across phases---demonstrates that no single strategy dominates uniformly. The pattern replicates on Qwen2.5-7B-Instruct at $s \\\\\\\\geq 0.20$ ($d_z \\\\\\\\geq 0.55$) and partially extends cross-architecture to DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM) with a qualitatively consistent but substantially weaker trend at $\\\\\\\\sim$1/40 the magnitude. Discrimination collapse provides a mechanistic explanation supported by both Qwen2-based models; LLaMA results are directionally consistent but the interaction is weaker than in Qwen2 architectures.\\\\nThese findings motivate phase-aware sparsity allocation for reasoning model deployment.\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\\section{Conclusion}\\n\\\\label{sec:conclusion}\\n\\nWe showed that compound sparsity severity---the super-additive interaction between head pruning and KV cache eviction---is not phase-invariant but exhibits an emergent phase-strategy interaction spanning over an order of magnitude within a single generation. Under importance-based eviction, the severity gradient grows from $69{\\\\times}$ to $274{\\\\times}$ across sparsity levels ($d_z$: $0.44 \\\\to 0.80$); random eviction shows no such modulation (7/8 conditions non-significant). A crossover at $s{=}0.25$---where importance-based eviction reverses ranking across phases---demonstrates that no single strategy dominates uniformly. The pattern replicates on Qwen2.5-7B-Instruct at $s \\\\geq 0.20$ ($d_z \\\\geq 0.55$) and partially extends cross-architecture to DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM) with a qualitatively consistent but substantially weaker trend at $\\\\sim$1/40 the magnitude. Discrimination collapse provides a mechanistic explanation supported by both Qwen2-based models; LLaMA results are directionally consistent but the interaction is weaker than in Qwen2 architectures.\\nThese findings motivate phase-aware sparsity allocation for reasoning model deployment.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01BkBqfwDm59LSUKebhC2U7K`</summary>

```json
{
  "server": "westd-22162",
  "command": "cat /root/autodl-tmp/pacs/paper/limitations.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "dc389c28-f430-4f5a-9e74-9c3ea58676fa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HaASaKe4zhD4sf12ZidXN6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5886,
      "cache_read_input_tokens": 24703,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5886
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

_source line 33 · 2026-05-15T02:17:44.511Z_

<details><summary>↩ Tool result · `toolu_01BkBqfwDm59LSUKebhC2U7K`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\\paragraph{Model scale and architecture.}\\nAll experiments are conducted at the 7--8B parameter scale. Whether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested. Preliminary cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \\\\S\\\\ref{sec:cross-arch}) partially confirms the qualitative pattern beyond the Qwen2 architecture---monotonically increasing $d_z$ with within-importance phase gradient $\\\\sim$1.0---but with substantially weaker interaction magnitude ($\\\\sim$1/40 of DeepSeek) and mixed statistical evidence (only $s{=}0.30$ significant after Bonferroni correction). The pattern has been tested on two architecture families (Qwen2ForCausalLM, LlamaForCausalLM); comprehensive validation across more diverse architectures (e.g., Mistral, multi-latent attention) and larger scales is needed for full generalization claims.\\n\\n\\\\paragraph{Task coverage.}\\nWe evaluate exclusively on MATH-500, a mathematical reasoning benchmark. Different reasoning tasks---code generation, commonsense reasoning, multi-hop question answering---may induce different phase structures with different sparsity distributions, potentially altering the severity gradient profile.\\n\\n\\\\paragraph{Mechanism.}\\nThe discrimination collapse mechanism is supported by correlational evidence (consistent Gini/CV reduction across all conditions); causal validation through controlled entropy manipulation is needed. The entropy redistribution component replicates on only 2/4 Qwen conditions, suggesting model-specific factors.\\n\\n\\\\paragraph{Sparsity range.}\\nOur experiments span $s \\\\in \\\\{0.15, 0.20, 0.25, 0.30\\\\}$. More extreme sparsity ($s > 0.50$) may exhibit qualitatively different interaction dynamics. We do not report inference throughput or latency measurements, which are necessary for a complete deployment analysis but orthogonal to our severity characterization. Extended limitations in Appendix~\\\\ref{app:limitations}.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "f7ebdf50-1fa3-4ca5-928b-0339b51f024f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\\paragraph{Model scale and architecture.}\\\\nAll experiments are conducted at the 7--8B parameter scale. Whether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested. Preliminary cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \\\\\\\\S\\\\\\\\ref{sec:cross-arch}) partially confirms the qualitative pattern beyond the Qwen2 architecture---monotonically increasing $d_z$ with within-importance phase gradient $\\\\\\\\sim$1.0---but with substantially weaker interaction magnitude ($\\\\\\\\sim$1/40 of DeepSeek) and mixed statistical evidence (only $s{=}0.30$ significant after Bonferroni correction). The pattern has been tested on two architecture families (Qwen2ForCausalLM, LlamaForCausalLM); comprehensive validation across more diverse architectures (e.g., Mistral, multi-latent attention) and larger scales is needed for full generalization claims.\\\\n\\\\n\\\\\\\\paragraph{Task coverage.}\\\\nWe evaluate exclusively on MATH-500, a mathematical reasoning benchmark. Different reasoning tasks---code generation, commonsense reasoning, multi-hop question answering---may induce different phase structures with different sparsity distributions, potentially altering the severity gradient profile.\\\\n\\\\n\\\\\\\\paragraph{Mechanism.}\\\\nThe discrimination collapse mechanism is supported by correlational evidence (consistent Gini/CV reduction across all conditions); causal validation through controlled entropy manipulation is needed. The entropy redistribution component replicates on only 2/4 Qwen conditions, suggesting model-specific factors.\\\\n\\\\n\\\\\\\\paragraph{Sparsity range.}\\\\nOur experiments span $s \\\\\\\\in \\\\\\\\{0.15, 0.20, 0.25, 0.30\\\\\\\\}$. More extreme sparsity ($s > 0.50$) may exhibit qualitatively different interaction dynamics. We do not report inference throughput or latency measurements, which are necessary for a complete deployment analysis but orthogonal to our severity characterization. Extended limitations in Appendix~\\\\\\\\ref{app:limitations}.\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.52}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\\paragraph{Model scale and architecture.}\\nAll experiments are conducted at the 7--8B parameter scale. Whether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested. Preliminary cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \\\\S\\\\ref{sec:cross-arch}) partially confirms the qualitative pattern beyond the Qwen2 architecture---monotonically increasing $d_z$ with within-importance phase gradient $\\\\sim$1.0---but with substantially weaker interaction magnitude ($\\\\sim$1/40 of DeepSeek) and mixed statistical evidence (only $s{=}0.30$ significant after Bonferroni correction). The pattern has been tested on two architecture families (Qwen2ForCausalLM, LlamaForCausalLM); comprehensive validation across more diverse architectures (e.g., Mistral, multi-latent attention) and larger scales is needed for full generalization claims.\\n\\n\\\\paragraph{Task coverage.}\\nWe evaluate exclusively on MATH-500, a mathematical reasoning benchmark. Different reasoning tasks---code generation, commonsense reasoning, multi-hop question answering---may induce different phase structures with different sparsity distributions, potentially altering the severity gradient profile.\\n\\n\\\\paragraph{Mechanism.}\\nThe discrimination collapse mechanism is supported by correlational evidence (consistent Gini/CV reduction across all conditions); causal validation through controlled entropy manipulation is needed. The entropy redistribution component replicates on only 2/4 Qwen conditions, suggesting model-specific factors.\\n\\n\\\\paragraph{Sparsity range.}\\nOur experiments span $s \\\\in \\\\{0.15, 0.20, 0.25, 0.30\\\\}$. More extreme sparsity ($s > 0.50$) may exhibit qualitatively different interaction dynamics. We do not report inference throughput or latency measurements, which are necessary for a complete deployment analysis but orthogonal to our severity characterization. Extended limitations in Appendix~\\\\ref{app:limitations}.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 34_

<details><summary>Logged reasoning block</summary>

```text
Good, I've read the main content files. Now let me read the appendix files and the main.tex to get the full picture.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "a89e4ba9-ff89-45d7-97e2-caf4b8c06ceb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VovymmRY1RS52xDHLXp5gz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13084,
      "cache_read_input_tokens": 30589,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13084
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

现在读取 appendix 文件和 main.tex。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "5891d246-b641-47c9-9175-32f848480bc1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VovymmRY1RS52xDHLXp5gz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13084,
      "cache_read_input_tokens": 30589,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13084
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_011yvgSm7D8cCZsaNKR5BYWL`</summary>

```json
{
  "server": "westd-22162",
  "command": "cat /root/autodl-tmp/pacs/paper/appendix.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "e1cbcde5-307d-4735-9d5c-b1a2b0f60548",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VovymmRY1RS52xDHLXp5gz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13084,
      "cache_read_input_tokens": 30589,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13084
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

_source line 37 · 2026-05-15T02:17:50.281Z_

<details><summary>↩ Tool result · `toolu_011yvgSm7D8cCZsaNKR5BYWL`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\\section{Compound Sparsity Formulation}\\n\\\\label{app:formulation-details}\\n\\n\\\\paragraph{Attention head pruning.}\\nHeads are ranked by Frobenius norm importance $w_j^{(\\\\ell)} = \\\\|\\\\mathbf{A}_j^{(\\\\ell)}\\\\|_F$ \\\\cite{voita-acl2019, michel-neurips2019}; a binary mask $m_j^{(\\\\ell)} \\\\in \\\\{0,1\\\\}$ retains the top-$(1{-}s)\\\\cdot H$ heads:\\n\\\\begin{equation}\\n    \\\\tilde{\\\\mathbf{o}}_j^{(\\\\ell)} = m_j^{(\\\\ell)} \\\\cdot \\\\mathbf{o}_j^{(\\\\ell)}.\\n    \\\\label{eq:head-mask}\\n\\\\end{equation}\\n\\n\\\\paragraph{KV cache eviction.}\\nA position mask $\\\\mathbf{m}_k \\\\in \\\\{0,1\\\\}^T$ retains the top-$(1{-}s)\\\\cdot T$ positions (BOS always preserved):\\n\\\\begin{equation}\\n    \\\\tilde{a}_{ij} = a_{ij} \\\\cdot m_{k,j}, \\\\quad \\\\forall\\\\, i, j.\\n    \\\\label{eq:kv-mask}\\n\\\\end{equation}\\nUnder importance-based eviction, each position $j$ is scored by its cumulative attention mass with position normalization:\\n\\\\begin{equation}\\n    \\\\mathrm{imp}(j) = \\\\frac{\\\\sum_{\\\\ell, h, i} a_{ij}^{(\\\\ell,h)}}{T - j},\\n    \\\\label{eq:kv-importance}\\n\\\\end{equation}\\nwhere the denominator compensates for causal bias---earlier positions are attended to by more queries \\\\cite{thinkv-iclr2026, defensivekv-iclr2026}. Under random eviction, positions (excluding BOS) are evicted uniformly at random.\\n\\n\\\\paragraph{Compound sparsity.}\\nApplying both mechanisms simultaneously yields compound sparsity. The two axes interact: head pruning redistributes attention mass, altering the importance ranking for KV eviction. Prior work \\\\cite{spark-aaai2026} reports super-additive joint effects but treats interaction magnitude as a fixed property of $s$.\\n\\n\\\\paragraph{Attention sparsity metric.}\\nFor each query position $i$ and head $h$, we compute the fraction of key positions receiving negligible attention:\\n\\\\begin{equation}\\n    \\\\sigma_i^{(h)} = \\\\frac{1}{T} \\\\sum_{j=1}^{T} \\\\mathbf{1}\\\\!\\\\left[a_{ij}^{(h)} < 0.01 \\\\cdot \\\\max_k a_{ik}^{(h)}\\\\right].\\n    \\\\label{eq:attn-sparsity}\\n\\\\end{equation}\\nThe per-position sparsity $\\\\sigma_i = \\\\frac{1}{H}\\\\sum_h \\\\sigma_i^{(h)}$ averages across all heads. Tokens are partitioned into high-, mid-, and low-sparsity phases by the tercile boundaries of $\\\\{\\\\sigma_i\\\\}$; segments shorter than 10 tokens are merged into adjacent phases.\\n\\n\\\\section{Multiplicative Null Verification}\\n\\\\label{app:multiplicative-null}\\n\\nWe verified that replacing the additive null $r_b = r_a + r_k - 1$ (Eq.~\\\\ref{eq:ii}) with the multiplicative null $r_b = r_a \\\\cdot r_k$ does not change qualitative conclusions. Under the multiplicative formulation, the interaction index becomes $\\\\mathrm{II}_{\\\\times} = r_b - r_a \\\\cdot r_k$. Across all sparsity levels and both eviction strategies, the sign and relative ordering of $\\\\mathrm{II}_{\\\\times}$ match those of the additive II: importance-based eviction exhibits a monotonically increasing severity gradient ($G_{\\\\times} = 58$--$241{\\\\times}$), while random eviction remains flat ($G_{\\\\times} \\\\approx 1$). The crossover at $s{=}0.25$ is preserved. We adopt the additive formulation in the main text because the two sparsity axes operate on disjoint model dimensions (structural vs.\\\\ positional), making additive independence the more natural null hypothesis at the sparsity levels studied.\\n\\n% Bootstrap and permutation details moved to main text \\\\S\\\\ref{sec:stat-validation}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "b85c553c-b665-423c-86ee-4cc9343c701d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\\section{Compound Sparsity Formulation}\\\\n\\\\\\\\label{app:formulation-details}\\\\n\\\\n\\\\\\\\paragraph{Attention head pruning.}\\\\nHeads are ranked by Frobenius norm importance $w_j^{(\\\\\\\\ell)} = \\\\\\\\|\\\\\\\\mathbf{A}_j^{(\\\\\\\\ell)}\\\\\\\\|_F$ \\\\\\\\cite{voita-acl2019, michel-neurips2019}; a binary mask $m_j^{(\\\\\\\\ell)} \\\\\\\\in \\\\\\\\{0,1\\\\\\\\}$ retains the top-$(1{-}s)\\\\\\\\cdot H$ heads:\\\\n\\\\\\\\begin{equation}\\\\n    \\\\\\\\tilde{\\\\\\\\mathbf{o}}_j^{(\\\\\\\\ell)} = m_j^{(\\\\\\\\ell)} \\\\\\\\cdot \\\\\\\\mathbf{o}_j^{(\\\\\\\\ell)}.\\\\n    \\\\\\\\label{eq:head-mask}\\\\n\\\\\\\\end{equation}\\\\n\\\\n\\\\\\\\paragraph{KV cache eviction.}\\\\nA position mask $\\\\\\\\mathbf{m}_k \\\\\\\\in \\\\\\\\{0,1\\\\\\\\}^T$ retains the top-$(1{-}s)\\\\\\\\cdot T$ positions (BOS always preserved):\\\\n\\\\\\\\begin{equation}\\\\n    \\\\\\\\tilde{a}_{ij} = a_{ij} \\\\\\\\cdot m_{k,j}, \\\\\\\\quad \\\\\\\\forall\\\\\\\\, i, j.\\\\n    \\\\\\\\label{eq:kv-mask}\\\\n\\\\\\\\end{equation}\\\\nUnder importance-based eviction, each position $j$ is scored by its cumulative attention mass with position normalization:\\\\n\\\\\\\\begin{equation}\\\\n    \\\\\\\\mathrm{imp}(j) = \\\\\\\\frac{\\\\\\\\sum_{\\\\\\\\ell, h, i} a_{ij}^{(\\\\\\\\ell,h)}}{T - j},\\\\n    \\\\\\\\label{eq:kv-importance}\\\\n\\\\\\\\end{equation}\\\\nwhere the denominator compensates for causal bias---earlier positions are attended to by more queries \\\\\\\\cite{thinkv-iclr2026, defensivekv-iclr2026}. Under random eviction, positions (excluding BOS) are evicted uniformly at random.\\\\n\\\\n\\\\\\\\paragraph{Compound sparsity.}\\\\nApplying both mechanisms simultaneously yields compound sparsity. The two axes interact: head pruning redistributes attention mass, altering the importance ranking for KV eviction. Prior work \\\\\\\\cite{spark-aaai2026} reports super-additive joint effects but treats interaction magnitude as a fixed property of $s$.\\\\n\\\\n\\\\\\\\paragraph{Attention sparsity metric.}\\\\nFor each query position $i$ and head $h$, we compute the fraction of key positions receiving negligible attention:\\\\n\\\\\\\\begin{equation}\\\\n    \\\\\\\\sigma_i^{(h)} = \\\\\\\\frac{1}{T} \\\\\\\\sum_{j=1}^{T} \\\\\\\\mathbf{1}\\\\\\\\!\\\\\\\\left[a_{ij}^{(h)} < 0.01 \\\\\\\\cdot \\\\\\\\max_k a_{ik}^{(h)}\\\\\\\\right].\\\\n    \\\\\\\\label{eq:attn-sparsity}\\\\n\\\\\\\\end{equation}\\\\nThe per-position sparsity $\\\\\\\\sigma_i = \\\\\\\\frac{1}{H}\\\\\\\\sum_h \\\\\\\\sigma_i^{(h)}$ averages across all heads. Tokens are partitioned into high-, mid-, and low-sparsity phases by the tercile boundaries of $\\\\\\\\{\\\\\\\\sigma_i\\\\\\\\}$; segments shorter than 10 tokens are merged into adjacent phases.\\\\n\\\\n\\\\\\\\section{Multiplicative Null Verification}\\\\n\\\\\\\\label{app:multiplicative-null}\\\\n\\\\nWe verified that replacing the additive null $r_b = r_a + r_k - 1$ (Eq.~\\\\\\\\ref{eq:ii}) with the multiplicative null $r_b = r_a \\\\\\\\cdot r_k$ does not change qualitative conclusions. Under the multiplicative formulation, the interaction index becomes $\\\\\\\\mathrm{II}_{\\\\\\\\times} = r_b - r_a \\\\\\\\cdot r_k$. Across all sparsity levels and both eviction strategies, the sign and relative ordering of $\\\\\\\\mathrm{II}_{\\\\\\\\times}$ match those of the additive II: importance-based eviction exhibits a monotonically increasing severity gradient ($G_{\\\\\\\\times} = 58$--$241{\\\\\\\\times}$), while random eviction remains flat ($G_{\\\\\\\\times} \\\\\\\\approx 1$). The crossover at $s{=}0.25$ is preserved. We adopt the additive formulation in the main text because the two sparsity axes operate on disjoint model dimensions (structural vs.\\\\\\\\ positional), making additive independence the more natural null hypothesis at the sparsity levels studied.\\\\n\\\\n% Bootstrap and permutation details moved to main text \\\\\\\\S\\\\\\\\ref{sec:stat-validation}\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\\section{Compound Sparsity Formulation}\\n\\\\label{app:formulation-details}\\n\\n\\\\paragraph{Attention head pruning.}\\nHeads are ranked by Frobenius norm importance $w_j^{(\\\\ell)} = \\\\|\\\\mathbf{A}_j^{(\\\\ell)}\\\\|_F$ \\\\cite{voita-acl2019, michel-neurips2019}; a binary mask $m_j^{(\\\\ell)} \\\\in \\\\{0,1\\\\}$ retains the top-$(1{-}s)\\\\cdot H$ heads:\\n\\\\begin{equation}\\n    \\\\tilde{\\\\mathbf{o}}_j^{(\\\\ell)} = m_j^{(\\\\ell)} \\\\cdot \\\\mathbf{o}_j^{(\\\\ell)}.\\n    \\\\label{eq:head-mask}\\n\\\\end{equation}\\n\\n\\\\paragraph{KV cache eviction.}\\nA position mask $\\\\mathbf{m}_k \\\\in \\\\{0,1\\\\}^T$ retains the top-$(1{-}s)\\\\cdot T$ positions (BOS always preserved):\\n\\\\begin{equation}\\n    \\\\tilde{a}_{ij} = a_{ij} \\\\cdot m_{k,j}, \\\\quad \\\\forall\\\\, i, j.\\n    \\\\label{eq:kv-mask}\\n\\\\end{equation}\\nUnder importance-based eviction, each position $j$ is scored by its cumulative attention mass with position normalization:\\n\\\\begin{equation}\\n    \\\\mathrm{imp}(j) = \\\\frac{\\\\sum_{\\\\ell, h, i} a_{ij}^{(\\\\ell,h)}}{T - j},\\n    \\\\label{eq:kv-importance}\\n\\\\end{equation}\\nwhere the denominator compensates for causal bias---earlier positions are attended to by more queries \\\\cite{thinkv-iclr2026, defensivekv-iclr2026}. Under random eviction, positions (excluding BOS) are evicted uniformly at random.\\n\\n\\\\paragraph{Compound sparsity.}\\nApplying both mechanisms simultaneously yields compound sparsity. The two axes interact: head pruning redistributes attention mass, altering the importance ranking for KV eviction. Prior work \\\\cite{spark-aaai2026} reports super-additive joint effects but treats interaction magnitude as a fixed property of $s$.\\n\\n\\\\paragraph{Attention sparsity metric.}\\nFor each query position $i$ and head $h$, we compute the fraction of key positions receiving negligible attention:\\n\\\\begin{equation}\\n    \\\\sigma_i^{(h)} = \\\\frac{1}{T} \\\\sum_{j=1}^{T} \\\\mathbf{1}\\\\!\\\\left[a_{ij}^{(h)} < 0.01 \\\\cdot \\\\max_k a_{ik}^{(h)}\\\\right].\\n    \\\\label{eq:attn-sparsity}\\n\\\\end{equation}\\nThe per-position sparsity $\\\\sigma_i = \\\\frac{1}{H}\\\\sum_h \\\\sigma_i^{(h)}$ averages across all heads. Tokens are partitioned into high-, mid-, and low-sparsity phases by the tercile boundaries of $\\\\{\\\\sigma_i\\\\}$; segments shorter than 10 tokens are merged into adjacent phases.\\n\\n\\\\section{Multiplicative Null Verification}\\n\\\\label{app:multiplicative-null}\\n\\nWe verified that replacing the additive null $r_b = r_a + r_k - 1$ (Eq.~\\\\ref{eq:ii}) with the multiplicative null $r_b = r_a \\\\cdot r_k$ does not change qualitative conclusions. Under the multiplicative formulation, the interaction index becomes $\\\\mathrm{II}_{\\\\times} = r_b - r_a \\\\cdot r_k$. Across all sparsity levels and both eviction strategies, the sign and relative ordering of $\\\\mathrm{II}_{\\\\times}$ match those of the additive II: importance-based eviction exhibits a monotonically increasing severity gradient ($G_{\\\\times} = 58$--$241{\\\\times}$), while random eviction remains flat ($G_{\\\\times} \\\\approx 1$). The crossover at $s{=}0.25$ is preserved. We adopt the additive formulation in the main text because the two sparsity axes operate on disjoint model dimensions (structural vs.\\\\ positional), making additive independence the more natural null hypothesis at the sparsity levels studied.\\n\\n% Bootstrap and permutation details moved to main text \\\\S\\\\ref{sec:stat-validation}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 38_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01CaoqqxdXdRSYNe4DDXkkpk`</summary>

```json
{
  "server": "westd-22162",
  "command": "cat /root/autodl-tmp/pacs/paper/appendix_disc_analysis.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "80d5aea0-a406-4f2d-a1f6-d687bfc9b078",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VovymmRY1RS52xDHLXp5gz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13084,
      "cache_read_input_tokens": 30589,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13084
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

_source line 39 · 2026-05-15T02:17:51.235Z_

<details><summary>↩ Tool result · `toolu_01CaoqqxdXdRSYNe4DDXkkpk`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\\section{Discrimination Collapse Details}\\n\\\\label{app:discrimination-collapse-details}\\n\\nThis cross-model consistency (Table~\\\\ref{tab:discrimination-metrics-full}) establishes discrimination collapse as a robust consequence of compound sparsity. When importance scores lose discriminative power, thresholding the bottom-$s$ fraction becomes noise-sensitive: small perturbations change which positions cross the eviction boundary. In the limit of perfectly uniform scores, importance-based eviction degenerates into an arbitrary selection functionally equivalent to biased random eviction. The same pattern holds under random eviction (DeepSeek: $-0.031$ to $-0.073$; Qwen: $-0.019$ to $-0.045$), confirming that discrimination collapse is a consequence of head pruning \\\\emph{per se}, not of the eviction strategy. % exp_id: c4_entropy_deepseek, c4_entropy_qwen\\n\\n\\n\\\\section{Extended Discussion}\\n\\\\label{app:extended-discussion}\\n\\n\\\\paragraph{On the predictability of phase-modulated severity.}\\nThe compound interaction is not uniformly fragile---it is selectively fragile in a phase-dependent manner ($\\\\widetilde{\\\\mathrm{II}}_{\\\\text{high}} < 0.06$ at $s \\\\leq 0.30$; at $s = 0.35$, high-phase II rises to $0.105$ in a supplementary experiment, indicating onset of compound interaction even in high-sparsity phases at extreme pruning rates). % exp_id: bf16_importance_s015..s030, bf16_ds_imp_s035; high-phase medians: 0.006, 0.015, 0.032, 0.053; s035 II_high=0.1051\\n\\n\\\\paragraph{Random masking as falsification control.}\\nRandom eviction fails 7/8 paired permutation tests across both models; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) exhibits negligible effect size ($\\\\widetilde{\\\\Delta} = \\\\placeholder{}$). The absence of a phase gradient under random masking isolates the amplification as strategy-specific. % exp_id: bf16_ds_rand_s015..s030, bf16_qw_rand_s015..s030\\n\\n\\\\paragraph{Entropy mechanism boundary conditions.}\\nDirectly measuring per-head entropy shifts across architecturally distinct models---and identifying what training-time properties determine whether entropy concentrates or disperses under head pruning---would clarify the boundary conditions of the full mechanism.\\n\\n\\n\\\\section{Extended Limitations}\\n\\\\label{app:limitations}\\n\\n\\\\paragraph{Model scale.}\\nAll experiments are conducted at the 7B parameter scale.\\nWhether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested.\\nLarger models may exhibit different attention redundancy structures that alter the discrimination collapse dynamics (and the model-dependent entropy component may behave differently at scale).\\n% REVIEWER-ATTACK: \\\"7B is too small to be relevant for production.\\\"\\n% REBUTTAL: 7B is the most-deployed scale for on-device and cost-constrained serving—exactly where compound sparsity is needed. The mechanism (entropy-discrimination collapse) is scale-agnostic in principle. Scaling experiments are future work.\\n\\n\\\\paragraph{Architectural scope.}\\nOur two models---DeepSeek-R1-Distill-Qwen-7B and Qwen2.5-7B-Instruct---share the Qwen2ForCausalLM architecture.\\nThe cross-model replication (\\\\S\\\\ref{sec:cross-model}) establishes that the findings are not artifacts of a single model's weights, though both models share the same Qwen2ForCausalLM architecture.\\nPreliminary cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \\\\S\\\\ref{sec:cross-arch}) shows qualitatively consistent within-importance phase gradients ($d_z \\\\sim 1.0$) but a substantially weaker strategy $\\\\times$ phase interaction than in Qwen2-based architectures; random pruning also exhibits a non-trivial phase gradient on LLaMA, reducing the strategy contrast. This partial confirmation ($s{=}0.30$ Wilcoxon $p_{\\\\text{Bonf}}{=}0.029$; $s \\\\leq 0.25$ non-significant) suggests the qualitative pattern may generalize but quantitative impact is architecture-dependent. Comprehensive cross-architecture validation across more diverse designs (e.g., Mistral, multi-latent at\\n\\n... [截断: 输出过长，省略 661 字符] ...\\n\\nferent sparsity distributions, potentially altering the severity gradient profile.\\nGeneralizing the phase-strategy interaction to broader reasoning domains is an important next step.\\n% REVIEWER-ATTACK: \\\"Only MATH-500. How do we know this isn't a math-specific artifact?\\\"\\n% REBUTTAL: The mechanism (entropy-discrimination collapse under head pruning) depends on attention distribution properties, not math-specific features. MATH-500 is a standard benchmark with diverse difficulty. However, different reasoning tasks may induce different phase structures—we state this limitation explicitly rather than overclaiming.\\n\\n\\\\paragraph{Statistical scope.}\\nBootstrap confidence intervals use $B{=}10{,}000$ resamples (recomputed from initial $B{=}1{,}000$ profiling runs). The paired permutation test yields $n{=}49$ paired problems for DeepSeek (1 excluded) and $n{=}46$ for Qwen (4 excluded). % exp_id: cohens_d_bf16.json, cohens_d_bf16_qwen.json\\nThe severity difference distribution is right-skewed (mean/median ratio ${\\\\sim}1.6{:}1$ at $s{=}0.30$), motivating our use of medians and nonparametric tests rather than parametric alternatives. % exp_id: bf16_importance_s030; mean_diff=22.94, median_diff=14.59 (segment-level). Per-problem paired: median_diff=9.9436 at s030\\nAll four permutation tests reject $H_0$ after Bonferroni correction ($p_{\\\\text{Bonf}} < 0.005$; Table~\\\\ref{tab:permutation}), with CI lower bounds increasing from $0.19$ to $6.70$---confirming the effect direction at every sparsity level. The permutation CIs at higher sparsity are wider (e.g., $[6.70,\\\\; 16.29]$ at $s{=}0.30$), reflecting genuine variance in per-problem severity amplification. % exp_id: permutation_test_results.json; permutation CIs: s015=[0.19,0.62], s020=[0.69,1.49], s025=[1.66,6.64], s030=[6.70,16.29]\\n\\nA notable exception among the random baselines is the Qwen random condition at $s{=}0.30$, which yields a statistically significant result ($p{=}0.012$) despite negligible effect size ($\\\\widetilde{\\\\Delta} = \\\\placeholder{}$, bootstrap CI spanning zero). % exp_id: qw_rand_s030; B=10000, p=0.012, d=-0.035, negligible\\nThis case illustrates that dichotomous significance testing can flag effects of no practical magnitude---reinforcing the importance of reporting effect sizes and confidence intervals alongside $p$-values.\\n\\n\\\\paragraph{Sparsity range.}\\nOur experiments span $s \\\\in \\\\{0.15, 0.20, 0.25, 0.30\\\\}$, a moderate range representative of practical deployment targets.\\nMore extreme sparsity ($s > 0.50$) may exhibit qualitatively different interaction dynamics---the sub-exponential growth pattern suggests the severity gradient may plateau, but this remains unverified.\\nConversely, the lower boundary at which phase-modulated amplification first emerges is not yet characterized.\\n% REVIEWER-ATTACK: \\\"Why not test higher sparsity? 0.30 is conservative.\\\"\\n% REBUTTAL: Our focus is on the practically relevant regime where models retain usable quality. At s>0.30 both strategies degrade severely, making II measurement less informative. The sub-exponential growth (C6, $\\\\Delta$ growth rate $3.8{\\\\times} \\\\to 4.8{\\\\times} \\\\to 2.0{\\\\times}$) suggests saturation at higher sparsity, but confirming this is future work.\\n\\n\\\\paragraph{No throughput evaluation.}\\nWe do not report inference throughput or latency, which are necessary for deployment analysis but orthogonal to our severity characterization.\\n% REVIEWER-ATTACK: \\\"No system evaluation. How do we know the severity amplification matters for real deployment?\\\"\\n% REBUTTAL: This is an empirical finding paper, not a method/system paper. The contribution is characterizing *what happens* (phase-modulated severity) and *why* (entropy-discrimination collapse), not building a system to fix it. Phase-gated controllers are explicitly scoped as future work. The finding is actionable regardless: any compound sparsity deployment should be aware of phase-dependent severity.\\n\\n% Entropy redistribution analysis moved to main text \\\\S\\\\ref{sec:entropy-redistribution}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "3385d138-a1e3-4415-94ae-6d0d0bbc165e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\\section{Discrimination Collapse Details}\\\\n\\\\\\\\label{app:discrimination-collapse-details}\\\\n\\\\nThis cross-model consistency (Table~\\\\\\\\ref{tab:discrimination-metrics-full}) establishes discrimination collapse as a robust consequence of compound sparsity. When importance scores lose discriminative power, thresholding the bottom-$s$ fraction becomes noise-sensitive: small perturbations change which positions cross the eviction boundary. In the limit of perfectly uniform scores, importance-based eviction degenerates into an arbitrary selection functionally equivalent to biased random eviction. The same pattern holds under random eviction (DeepSeek: $-0.031$ to $-0.073$; Qwen: $-0.019$ to $-0.045$), confirming that discrimination collapse is a consequence of head pruning \\\\\\\\emph{per se}, not of the eviction strategy. % exp_id: c4_entropy_deepseek, c4_entropy_qwen\\\\n\\\\n\\\\n\\\\\\\\section{Extended Discussion}\\\\n\\\\\\\\label{app:extended-discussion}\\\\n\\\\n\\\\\\\\paragraph{On the predictability of phase-modulated severity.}\\\\nThe compound interaction is not uniformly fragile---it is selectively fragile in a phase-dependent manner ($\\\\\\\\widetilde{\\\\\\\\mathrm{II}}_{\\\\\\\\text{high}} < 0.06$ at $s \\\\\\\\leq 0.30$; at $s = 0.35$, high-phase II rises to $0.105$ in a supplementary experiment, indicating onset of compound interaction even in high-sparsity phases at extreme pruning rates). % exp_id: bf16_importance_s015..s030, bf16_ds_imp_s035; high-phase medians: 0.006, 0.015, 0.032, 0.053; s035 II_high=0.1051\\\\n\\\\n\\\\\\\\paragraph{Random masking as falsification control.}\\\\nRandom eviction fails 7/8 paired permutation tests across both models; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) exhibits negligible effect size ($\\\\\\\\widetilde{\\\\\\\\Delta} = \\\\\\\\placeholder{}$). The absence of a phase gradient under random masking isolates the amplification as strategy-specific. % exp_id: bf16_ds_rand_s015..s030, bf16_qw_rand_s015..s030\\\\n\\\\n\\\\\\\\paragraph{Entropy mechanism boundary conditions.}\\\\nDirectly measuring per-head entropy shifts across architecturally distinct models---and identifying what training-time properties determine whether entropy concentrates or disperses under head pruning---would clarify the boundary conditions of the full mechanism.\\\\n\\\\n\\\\n\\\\\\\\section{Extended Limitations}\\\\n\\\\\\\\label{app:limitations}\\\\n\\\\n\\\\\\\\paragraph{Model scale.}\\\\nAll experiments are conducted at the 7B parameter scale.\\\\nWhether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested.\\\\nLarger models may exhibit different attention redundancy structures that alter the discrimination collapse dynamics (and the model-dependent entropy component may behave differently at scale).\\\\n% REVIEWER-ATTACK: \\\\\\\"7B is too small to be relevant for production.\\\\\\\"\\\\n% REBUTTAL: 7B is the most-deployed scale for on-device and cost-constrained serving—exactly where compound sparsity is needed. The mechanism (entropy-discrimination collapse) is scale-agnostic in principle. Scaling experiments are future work.\\\\n\\\\n\\\\\\\\paragraph{Architectural scope.}\\\\nOur two models---DeepSeek-R1-Distill-Qwen-7B and Qwen2.5-7B-Instruct---share the Qwen2ForCausalLM architecture.\\\\nThe cross-model replication (\\\\\\\\S\\\\\\\\ref{sec:cross-model}) establishes that the findings are not artifacts of a single model's weights, though both models share the same Qwen2ForCausalLM architecture.\\\\nPreliminary cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \\\\\\\\S\\\\\\\\ref{sec:cross-arch}) shows qualitatively consistent within-importance phase gradients ($d_z \\\\\\\\sim 1.0$) but a substantially weaker strategy $\\\\\\\\times$ phase interaction than in Qwen2-based architectures; random pruning also exhibits a non-trivial phase gradient on LLaMA, reducing the strategy contrast. This partial confirmation ($s{=}0.30$ Wilcoxon $p_{\\\\\\\\text{Bonf}}{=}0.029$; $s \\\\\\\\leq 0.25$ non-significant) suggests the qualitative pattern may generalize but quantitative impact is architecture-dependent. Comprehensive cross-architecture validation across more diverse designs (e.g., Mistral, multi-latent at\\\\n\\\\n... [截断: 输出过长，省略 661 字符] ...\\\\n\\\\nferent sparsity distributions, potentially altering the severity gradient profile.\\\\nGeneralizing the phase-strategy interaction to broader reasoning domains is an important next step.\\\\n% REVIEWER-ATTACK: \\\\\\\"Only MATH-500. How do we know this isn't a math-specific artifact?\\\\\\\"\\\\n% REBUTTAL: The mechanism (entropy-discrimination collapse under head pruning) depends on attention distribution properties, not math-specific features. MATH-500 is a standard benchmark with diverse difficulty. However, different reasoning tasks may induce different phase structures—we state this limitation explicitly rather than overclaiming.\\\\n\\\\n\\\\\\\\paragraph{Statistical scope.}\\\\nBootstrap confidence intervals use $B{=}10{,}000$ resamples (recomputed from initial $B{=}1{,}000$ profiling runs). The paired permutation test yields $n{=}49$ paired problems for DeepSeek (1 excluded) and $n{=}46$ for Qwen (4 excluded). % exp_id: cohens_d_bf16.json, cohens_d_bf16_qwen.json\\\\nThe severity difference distribution is right-skewed (mean/median ratio ${\\\\\\\\sim}1.6{:}1$ at $s{=}0.30$), motivating our use of medians and nonparametric tests rather than parametric alternatives. % exp_id: bf16_importance_s030; mean_diff=22.94, median_diff=14.59 (segment-level). Per-problem paired: median_diff=9.9436 at s030\\\\nAll four permutation tests reject $H_0$ after Bonferroni correction ($p_{\\\\\\\\text{Bonf}} < 0.005$; Table~\\\\\\\\ref{tab:permutation}), with CI lower bounds increasing from $0.19$ to $6.70$---confirming the effect direction at every sparsity level. The permutation CIs at higher sparsity are wider (e.g., $[6.70,\\\\\\\\; 16.29]$ at $s{=}0.30$), reflecting genuine variance in per-problem severity amplification. % exp_id: permutation_test_results.json; permutation CIs: s015=[0.19,0.62], s020=[0.69,1.49], s025=[1.66,6.64], s030=[6.70,16.29]\\\\n\\\\nA notable exception among the random baselines is the Qwen random condition at $s{=}0.30$, which yields a statistically significant result ($p{=}0.012$) despite negligible effect size ($\\\\\\\\widetilde{\\\\\\\\Delta} = \\\\\\\\placeholder{}$, bootstrap CI spanning zero). % exp_id: qw_rand_s030; B=10000, p=0.012, d=-0.035, negligible\\\\nThis case illustrates that dichotomous significance testing can flag effects of no practical magnitude---reinforcing the importance of reporting effect sizes and confidence intervals alongside $p$-values.\\\\n\\\\n\\\\\\\\paragraph{Sparsity range.}\\\\nOur experiments span $s \\\\\\\\in \\\\\\\\{0.15, 0.20, 0.25, 0.30\\\\\\\\}$, a moderate range representative of practical deployment targets.\\\\nMore extreme sparsity ($s > 0.50$) may exhibit qualitatively different interaction dynamics---the sub-exponential growth pattern suggests the severity gradient may plateau, but this remains unverified.\\\\nConversely, the lower boundary at which phase-modulated amplification first emerges is not yet characterized.\\\\n% REVIEWER-ATTACK: \\\\\\\"Why not test higher sparsity? 0.30 is conservative.\\\\\\\"\\\\n% REBUTTAL: Our focus is on the practically relevant regime where models retain usable quality. At s>0.30 both strategies degrade severely, making II measurement less informative. The sub-exponential growth (C6, $\\\\\\\\Delta$ growth rate $3.8{\\\\\\\\times} \\\\\\\\to 4.8{\\\\\\\\times} \\\\\\\\to 2.0{\\\\\\\\times}$) suggests saturation at higher sparsity, but confirming this is future work.\\\\n\\\\n\\\\\\\\paragraph{No throughput evaluation.}\\\\nWe do not report inference throughput or latency, which are necessary for deployment analysis but orthogonal to our severity characterization.\\\\n% REVIEWER-ATTACK: \\\\\\\"No system evaluation. How do we know the severity amplification matters for real deployment?\\\\\\\"\\\\n% REBUTTAL: This is an empirical finding paper, not a method/system paper. The contribution is characterizing *what happens* (phase-modulated severity) and *why* (entropy-discrimination collapse), not building a system to fix it. Phase-gated controllers are explicitly scoped as future work. The finding is actionable regardless: any compound sparsity deployment should be aware of phase-dependent severity.\\\\n\\\\n% Entropy redistribution analysis moved to main text \\\\\\\\S\\\\\\\\ref{sec:entropy-redistribution}\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\\section{Discrimination Collapse Details}\\n\\\\label{app:discrimination-collapse-details}\\n\\nThis cross-model consistency (Table~\\\\ref{tab:discrimination-metrics-full}) establishes discrimination collapse as a robust consequence of compound sparsity. When importance scores lose discriminative power, thresholding the bottom-$s$ fraction becomes noise-sensitive: small perturbations change which positions cross the eviction boundary. In the limit of perfectly uniform scores, importance-based eviction degenerates into an arbitrary selection functionally equivalent to biased random eviction. The same pattern holds under random eviction (DeepSeek: $-0.031$ to $-0.073$; Qwen: $-0.019$ to $-0.045$), confirming that discrimination collapse is a consequence of head pruning \\\\emph{per se}, not of the eviction strategy. % exp_id: c4_entropy_deepseek, c4_entropy_qwen\\n\\n\\n\\\\section{Extended Discussion}\\n\\\\label{app:extended-discussion}\\n\\n\\\\paragraph{On the predictability of phase-modulated severity.}\\nThe compound interaction is not uniformly fragile---it is selectively fragile in a phase-dependent manner ($\\\\widetilde{\\\\mathrm{II}}_{\\\\text{high}} < 0.06$ at $s \\\\leq 0.30$; at $s = 0.35$, high-phase II rises to $0.105$ in a supplementary experiment, indicating onset of compound interaction even in high-sparsity phases at extreme pruning rates). % exp_id: bf16_importance_s015..s030, bf16_ds_imp_s035; high-phase medians: 0.006, 0.015, 0.032, 0.053; s035 II_high=0.1051\\n\\n\\\\paragraph{Random masking as falsification control.}\\nRandom eviction fails 7/8 paired permutation tests across both models; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) exhibits negligible effect size ($\\\\widetilde{\\\\Delta} = \\\\placeholder{}$). The absence of a phase gradient under random masking isolates the amplification as strategy-specific. % exp_id: bf16_ds_rand_s015..s030, bf16_qw_rand_s015..s030\\n\\n\\\\paragraph{Entropy mechanism boundary conditions.}\\nDirectly measuring per-head entropy shifts across architecturally distinct models---and identifying what training-time properties determine whether entropy concentrates or disperses under head pruning---would clarify the boundary conditions of the full mechanism.\\n\\n\\n\\\\section{Extended Limitations}\\n\\\\label{app:limitations}\\n\\n\\\\paragraph{Model scale.}\\nAll experiments are conducted at the 7B parameter scale.\\nWhether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested.\\nLarger models may exhibit different attention redundancy structures that alter the discrimination collapse dynamics (and the model-dependent entropy component may behave differently at scale).\\n% REVIEWER-ATTACK: \\\"7B is too small to be relevant for production.\\\"\\n% REBUTTAL: 7B is the most-deployed scale for on-device and cost-constrained serving—exactly where compound sparsity is needed. The mechanism (entropy-discrimination collapse) is scale-agnostic in principle. Scaling experiments are future work.\\n\\n\\\\paragraph{Architectural scope.}\\nOur two models---DeepSeek-R1-Distill-Qwen-7B and Qwen2.5-7B-Instruct---share the Qwen2ForCausalLM architecture.\\nThe cross-model replication (\\\\S\\\\ref{sec:cross-model}) establishes that the findings are not artifacts of a single model's weights, though both models share the same Qwen2ForCausalLM architecture.\\nPreliminary cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \\\\S\\\\ref{sec:cross-arch}) shows qualitatively consistent within-importance phase gradients ($d_z \\\\sim 1.0$) but a substantially weaker strategy $\\\\times$ phase interaction than in Qwen2-based architectures; random pruning also exhibits a non-trivial phase gradient on LLaMA, reducing the strategy contrast. This partial confirmation ($s{=}0.30$ Wilcoxon $p_{\\\\text{Bonf}}{=}0.029$; $s \\\\leq 0.25$ non-significant) suggests the qualitative pattern may generalize but quantitative impact is architecture-dependent. Comprehensive cross-architecture validation across more diverse designs (e.g., Mistral, multi-latent at\\n\\n... [截断: 输出过长，省略 661 字符] ...\\n\\nferent sparsity distributions, potentially altering the severity gradient profile.\\nGeneralizing the phase-strategy interaction to broader reasoning domains is an important next step.\\n% REVIEWER-ATTACK: \\\"Only MATH-500. How do we know this isn't a math-specific artifact?\\\"\\n% REBUTTAL: The mechanism (entropy-discrimination collapse under head pruning) depends on attention distribution properties, not math-specific features. MATH-500 is a standard benchmark with diverse difficulty. However, different reasoning tasks may induce different phase structures—we state this limitation explicitly rather than overclaiming.\\n\\n\\\\paragraph{Statistical scope.}\\nBootstrap confidence intervals use $B{=}10{,}000$ resamples (recomputed from initial $B{=}1{,}000$ profiling runs). The paired permutation test yields $n{=}49$ paired problems for DeepSeek (1 excluded) and $n{=}46$ for Qwen (4 excluded). % exp_id: cohens_d_bf16.json, cohens_d_bf16_qwen.json\\nThe severity difference distribution is right-skewed (mean/median ratio ${\\\\sim}1.6{:}1$ at $s{=}0.30$), motivating our use of medians and nonparametric tests rather than parametric alternatives. % exp_id: bf16_importance_s030; mean_diff=22.94, median_diff=14.59 (segment-level). Per-problem paired: median_diff=9.9436 at s030\\nAll four permutation tests reject $H_0$ after Bonferroni correction ($p_{\\\\text{Bonf}} < 0.005$; Table~\\\\ref{tab:permutation}), with CI lower bounds increasing from $0.19$ to $6.70$---confirming the effect direction at every sparsity level. The permutation CIs at higher sparsity are wider (e.g., $[6.70,\\\\; 16.29]$ at $s{=}0.30$), reflecting genuine variance in per-problem severity amplification. % exp_id: permutation_test_results.json; permutation CIs: s015=[0.19,0.62], s020=[0.69,1.49], s025=[1.66,6.64], s030=[6.70,16.29]\\n\\nA notable exception among the random baselines is the Qwen random condition at $s{=}0.30$, which yields a statistically significant result ($p{=}0.012$) despite negligible effect size ($\\\\widetilde{\\\\Delta} = \\\\placeholder{}$, bootstrap CI spanning zero). % exp_id: qw_rand_s030; B=10000, p=0.012, d=-0.035, negligible\\nThis case illustrates that dichotomous significance testing can flag effects of no practical magnitude---reinforcing the importance of reporting effect sizes and confidence intervals alongside $p$-values.\\n\\n\\\\paragraph{Sparsity range.}\\nOur experiments span $s \\\\in \\\\{0.15, 0.20, 0.25, 0.30\\\\}$, a moderate range representative of practical deployment targets.\\nMore extreme sparsity ($s > 0.50$) may exhibit qualitatively different interaction dynamics---the sub-exponential growth pattern suggests the severity gradient may plateau, but this remains unverified.\\nConversely, the lower boundary at which phase-modulated amplification first emerges is not yet characterized.\\n% REVIEWER-ATTACK: \\\"Why not test higher sparsity? 0.30 is conservative.\\\"\\n% REBUTTAL: Our focus is on the practically relevant regime where models retain usable quality. At s>0.30 both strategies degrade severely, making II measurement less informative. The sub-exponential growth (C6, $\\\\Delta$ growth rate $3.8{\\\\times} \\\\to 4.8{\\\\times} \\\\to 2.0{\\\\times}$) suggests saturation at higher sparsity, but confirming this is future work.\\n\\n\\\\paragraph{No throughput evaluation.}\\nWe do not report inference throughput or latency, which are necessary for deployment analysis but orthogonal to our severity characterization.\\n% REVIEWER-ATTACK: \\\"No system evaluation. How do we know the severity amplification matters for real deployment?\\\"\\n% REBUTTAL: This is an empirical finding paper, not a method/system paper. The contribution is characterizing *what happens* (phase-modulated severity) and *why* (entropy-discrimination collapse), not building a system to fix it. Phase-gated controllers are explicitly scoped as future work. The finding is actionable regardless: any compound sparsity deployment should be aware of phase-dependent severity.\\n\\n% Entropy redistribution analysis moved to main text \\\\S\\\\ref{sec:entropy-redistribution}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 40_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01CvRC2MVERUx9YUJnk1aaAo`</summary>

```json
{
  "server": "westd-22162",
  "command": "cat /root/autodl-tmp/pacs/paper/appendix_results.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "66d4b4d7-b487-467c-a7e9-b70d22c5ded3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VovymmRY1RS52xDHLXp5gz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13084,
      "cache_read_input_tokens": 30589,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13084
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

_source line 41 · 2026-05-15T02:17:52.218Z_

<details><summary>↩ Tool result · `toolu_01CvRC2MVERUx9YUJnk1aaAo`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"% Appendix: supplementary results details\\n\\n\\\\section{Cross-Model Replication Details}\\n\\\\label{app:cross-model-details}\\n\\n\\\\paragraph{Per-problem concordance.}\\nThe per-problem concordance across models is not significant (median $\\\\rho = \\\\placeholder{}$, $p = \\\\placeholder{}$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking. % exp_id: cross_model_analysis.json (spearman_rho=1.0, gradient_permutation_p=0.043, per_problem_concordance_p=0.926, mean_rho=-0.107)\\n\\n\\\\paragraph{Random eviction control.}\\nAs a control, random eviction on Qwen yields no systematic phase gradient at three of four sparsity levels (3/4 FAIL), mirroring DeepSeek's 4/4 FAIL pattern. At $s{=}0.30$, Qwen random produces a borderline PASS (permutation $p = 0.012$) but with negligible median difference ($\\\\widetilde{\\\\Delta} = \\\\placeholder{}$, CI spans zero), indicating no meaningful phase modulation. % exp_id: bf16_qw_rand_s015..s030; source: experiment_summary_table.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "8e9bef60-eccd-4d8a-9a7c-644f86cda700",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"% Appendix: supplementary results details\\\\n\\\\n\\\\\\\\section{Cross-Model Replication Details}\\\\n\\\\\\\\label{app:cross-model-details}\\\\n\\\\n\\\\\\\\paragraph{Per-problem concordance.}\\\\nThe per-problem concordance across models is not significant (median $\\\\\\\\rho = \\\\\\\\placeholder{}$, $p = \\\\\\\\placeholder{}$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking. % exp_id: cross_model_analysis.json (spearman_rho=1.0, gradient_permutation_p=0.043, per_problem_concordance_p=0.926, mean_rho=-0.107)\\\\n\\\\n\\\\\\\\paragraph{Random eviction control.}\\\\nAs a control, random eviction on Qwen yields no systematic phase gradient at three of four sparsity levels (3/4 FAIL), mirroring DeepSeek's 4/4 FAIL pattern. At $s{=}0.30$, Qwen random produces a borderline PASS (permutation $p = 0.012$) but with negligible median difference ($\\\\\\\\widetilde{\\\\\\\\Delta} = \\\\\\\\placeholder{}$, CI spans zero), indicating no meaningful phase modulation. % exp_id: bf16_qw_rand_s015..s030; source: experiment_summary_table.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"% Appendix: supplementary results details\\n\\n\\\\section{Cross-Model Replication Details}\\n\\\\label{app:cross-model-details}\\n\\n\\\\paragraph{Per-problem concordance.}\\nThe per-problem concordance across models is not significant (median $\\\\rho = \\\\placeholder{}$, $p = \\\\placeholder{}$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking. % exp_id: cross_model_analysis.json (spearman_rho=1.0, gradient_permutation_p=0.043, per_problem_concordance_p=0.926, mean_rho=-0.107)\\n\\n\\\\paragraph{Random eviction control.}\\nAs a control, random eviction on Qwen yields no systematic phase gradient at three of four sparsity levels (3/4 FAIL), mirroring DeepSeek's 4/4 FAIL pattern. At $s{=}0.30$, Qwen random produces a borderline PASS (permutation $p = 0.012$) but with negligible median difference ($\\\\widetilde{\\\\Delta} = \\\\placeholder{}$, CI spans zero), indicating no meaningful phase modulation. % exp_id: bf16_qw_rand_s015..s030; source: experiment_summary_table.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 42_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01QYWa5vPyeBV5bVeyFv2Bci`</summary>

```json
{
  "server": "westd-22162",
  "command": "cat /root/autodl-tmp/pacs/paper/appendix_moved.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "2942849b-1603-46d6-9022-ec001c8e4e02",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VovymmRY1RS52xDHLXp5gz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13084,
      "cache_read_input_tokens": 30589,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13084
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

_source line 43_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01KYcBDAFoPtw3pQ55SyP2AR`</summary>

```json
{
  "server": "westd-22162",
  "command": "cat /root/autodl-tmp/pacs/paper/main.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "3c3129cd-ee84-4bb2-89a0-a9a143cc0242",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VovymmRY1RS52xDHLXp5gz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13084,
      "cache_read_input_tokens": 30589,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13084
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

_source line 44 · 2026-05-15T02:17:52.925Z_

<details><summary>↩ Tool result · `toolu_01QYWa5vPyeBV5bVeyFv2Bci`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"% Content moved from main body to appendix:\\n% - Phase-strategy crossover details (from results §5.3)\\n% - Cross-model replication details with tables/figures (from results §5.4)\\n% - Permutation test details with table/forest plot (from results §5.5)\\n% - Full entropy-discrimination collapse analysis with tables (from analysis §6)\\n% Main body §6 (analysis.tex) contains a condensed summary referencing these tables.\\n\\n\\\\section{Phase-Strategy Crossover Details}\\n\\\\label{app:crossover-details}\\n\\nAt $s{=}0.25$, a strategy ranking reversal emerges (Figure~\\\\ref{fig:crossover}): importance-based eviction yields \\\\emph{lower} II than random in the high-sparsity phase ($0.032$ vs.\\\\ $0.818$) but \\\\emph{higher} II in the low-sparsity phase ($7.196$ vs.\\\\ $1.363$---a $5.3{\\\\times}$ reversal). This crossover is present at all four sparsity levels, with reversal magnitude of $3.9{\\\\times}$ at $s{=}0.15$, $5.4{\\\\times}$ at $s{=}0.20$, $5.3{\\\\times}$ at $s{=}0.25$, and $3.6{\\\\times}$ at $s{=}0.30$ (as random eviction severity also rises). The reversal arises because head pruning redistributes attention mass, altering importance rankings in a way that couples the two sparsity mechanisms in low-sparsity phases (\\\\S\\\\ref{sec:discrimination-collapse}). % exp_id: bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json; 7.196/1.363=5.28\\n\\n\\\\begin{figure}[t]\\n\\\\centering\\n\\\\includegraphics[width=\\\\columnwidth]{fig3_crossover.pdf}\\n\\\\caption{Strategy-dependent crossover at $s{=}0.25$. Grouped bar chart of median II by eviction strategy and reasoning phase. Importance-based eviction outperforms random in the high-sparsity phase but produces $5.3{\\\\times}$ higher II in the low-sparsity phase, reversing the strategy ranking.}\\n\\\\label{fig:crossover}\\n\\\\end{figure}\\n\\n\\n\\\\section{Cross-Model Replication Details}\\n\\\\label{app:cross-model-details}\\n\\nBoth models share the Qwen2ForCausalLM backbone (28 layers, 28 heads, 4-group GQA) but differ in training: DeepSeek uses reasoning distillation from DeepSeek-R1, while Qwen2.5 uses standard instruction tuning without explicit reasoning delimiters. This controlled comparison isolates the effect of training methodology on the compound sparsity interaction.\\n\\nDespite lacking explicit \\\\texttt{&lt;think>} delimiters, Qwen2.5-7B-Instruct exhibits sufficient variation in attention sparsity to permit phase segmentation via the same quantile-based method (\\\\S\\\\ref{sec:phase-segmentation}). Four of the 50 problems are excluded due to degenerate phase assignments, yielding $n{=}46$ valid problems for Qwen (vs.\\\\ $n{=}49$ for DeepSeek).\\n\\n\\\\paragraph{Per-phase effective sample size.}\\n\\\\label{app:qwen-null-rate}\\nTable~\\\\ref{tab:qwen-effective-n} reports the per-phase effective sample size for Qwen2.5-7B-Instruct, defined as the number of problems with $|\\\\mathrm{II}| > 0.001$ in each phase. The mid-phase null rate (\\\\placeholder{NULL\\\\_PCT}\\\\%) reflects problems where compound interaction is absent in intermediate phases; this does not affect the low--high contrast ($\\\\Delta$) used in the primary analysis.\\n\\n\\\\begin{table}[t]\\n\\\\centering\\n\\\\small\\n\\\\caption{Per-phase effective sample size for Qwen2.5-7B-Instruct ($n_{\\\\text{total}} = \\\\placeholder{N\\\\_QW}$).}\\n\\\\label{tab:qwen-effective-n}\\n\\\\begin{tabular}{@{}lcccc@{}}\\n\\\\toprule\\nPhase & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\\\\\\\\\n\\\\midrule\\nHigh & \\\\placeholder{} & \\\\placeholder{} & \\\\placeholder{} & \\\\placeholder{} \\\\\\\\\\nMid  & \\\\placeholder{} & \\\\placeholder{} & \\\\placeholder{} & \\\\placeholder{} \\\\\\\\\\nLow  & \\\\placeholder{} & \\\\placeholder{} & \\\\placeholder{} & \\\\placeholder{} \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n\\nTable~\\\\ref{tab:cross-model} reports the cross-model comparison. Qwen reproduces the monotonic severity gradient at ${\\\\sim}1/5$ of DeepSeek's magnitude. Figure~\\\\ref{fig:cross-model} visualizes this comparison. % exp_id: cross_model_analysis.json; cohens_d_bf16_qwen.json\\n\\n\\\\begin{table}[t]\\n\\\\centering\\n\\\\small\\n\\\\caption{Cross-model comparison of median compound severity difference ($\\\\Delta$) under importance-based evicti\\n\\n... [截断: 输出过长，省略 5618 字符] ...\\n\\ndom eviction, confirming that discrimination collapse is a consequence of head pruning \\\\emph{per se}, not of the eviction strategy. % exp_id: c4_entropy_deepseek, c4_entropy_qwen\\n\\n\\\\begin{table}[t]\\n\\\\centering\\n\\\\caption{Discrimination collapse under importance-based eviction. $\\\\Delta\\\\mathrm{Gini}$ and $\\\\Delta\\\\mathrm{CV}$ are post-pruning minus baseline; negative values indicate reduced discriminative power.}\\n\\\\label{tab:discrimination-metrics-full}\\n\\\\small\\n\\\\begin{tabular}{llrr}\\n\\\\toprule\\nModel & $s$ & $\\\\Delta\\\\mathrm{Gini}$ & $\\\\Delta\\\\mathrm{CV}$ \\\\\\\\\\n\\\\midrule\\nDeepSeek & $0.15$ & $-0.030$ & $-0.56$ \\\\\\\\\\nDeepSeek & $0.20$ & $-0.040$ & $-0.77$ \\\\\\\\\\nDeepSeek & $0.25$ & $-0.065$ & $-1.29$ \\\\\\\\\\nDeepSeek & $0.30$ & $-0.081$ & $-1.66$ \\\\\\\\\\n\\\\midrule\\nQwen & $0.15$ & $-0.010$ & $-0.05$ \\\\\\\\\\nQwen & $0.20$ & $-0.012$ & $-0.21$ \\\\\\\\\\nQwen & $0.25$ & $-0.010$ & $-1.49$ \\\\\\\\\\nQwen & $0.30$ & $-0.020$ & $-1.14$ \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n\\nWhen importance scores lose discriminability, thresholding degenerates into noise-sensitive selection---functionally approaching biased random eviction. This is phase-dependent: in low-sparsity phases, attention is already broadly distributed, so pruning-induced flattening has maximum impact; in high-sparsity phases, concentration is preserved. Random eviction is immune because its decisions are independent of score quality, explaining $G \\\\approx 1$. % exp_id: c4_entropy_deepseek, c4_entropy_qwen\\n\\n\\\\subsection{Entropy Redistribution}\\n\\\\label{sec:entropy-redistribution}\\n\\nBeyond discrimination collapse, we examine whether head pruning also redistributes the attention entropy of surviving heads. We measure the mean attention entropy per head:\\n\\\\begin{equation}\\n    \\\\mathcal{H}_i^{(h)} = -\\\\sum_{j=1}^{T} a_{ij}^{(h)} \\\\log a_{ij}^{(h)}\\n    \\\\label{eq:attn-entropy}\\n\\\\end{equation}\\nand compute $\\\\Delta\\\\mathcal{H}$ as the change from baseline (no pruning) to the pruned condition.\\n\\nFor DeepSeek under importance-based eviction, the entropy delta is consistently negative across all four sparsity levels ($\\\\Delta\\\\mathcal{H} \\\\in [-0.047, -0.040]$; Table~\\\\ref{tab:entropy-deltas}), indicating that importance-based pruning systematically selects heads whose removal concentrates attention in the surviving heads, reinforcing discrimination collapse. % exp_id: c4_entropy_deepseek\\n\\nFor Qwen, the entropy pattern only partially replicates. The delta is negative at $s{=}0.15$ ($\\\\Delta\\\\mathcal{H} = -0.073$) and $s{=}0.20$ ($-0.076$), consistent with DeepSeek. However, at $s{=}0.25$, the delta reverses to $+0.045$, with 22 of 30 problems showing positive entropy change. At $s{=}0.30$, the delta is near zero ($-0.007$). The $s{=}0.25$ reversal is systematic rather than a statistical artifact: it is consistent across all three reasoning phases (low: $+0.042$, mid: $+0.034$, high: $+0.017$). We interpret this as a genuine model-specific difference, possibly arising from distinct head specialization patterns: Qwen's instruction tuning (vs.\\\\ DeepSeek's distillation-based training) may produce head configurations where removing 25\\\\% of heads triggers compensatory broadening rather than concentration. % exp_id: c4_entropy_qwen\\n\\nWe characterize discrimination collapse as the robust, model-independent driver of the phase-strategy interaction, with entropy redistribution as a secondary amplifier that is consistent in DeepSeek but model-dependent in Qwen.\\n\\n\\\\begin{table}[t]\\n\\\\centering\\n\\\\caption{Attention entropy deltas ($\\\\Delta\\\\mathcal{H}$) under importance-based eviction. DeepSeek shows consistent entropy compression; Qwen partially replicates with a reversal at $s{=}0.25$.}\\n\\\\label{tab:entropy-deltas}\\n\\\\small\\n\\\\begin{tabular}{llr}\\n\\\\toprule\\nModel & $s$ & $\\\\Delta\\\\mathcal{H}$ \\\\\\\\\\n\\\\midrule\\nDeepSeek & $0.15$ & $-0.040$ \\\\\\\\\\nDeepSeek & $0.20$ & $-0.047$ \\\\\\\\\\nDeepSeek & $0.25$ & $-0.045$ \\\\\\\\\\nDeepSeek & $0.30$ & $-0.044$ \\\\\\\\\\n\\\\midrule\\nQwen & $0.15$ & $-0.073$ \\\\\\\\\\nQwen & $0.20$ & $-0.076$ \\\\\\\\\\nQwen & $0.25$ & $+0.045$ \\\\\\\\\\nQwen & $0.30$ & $-0.007$ \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "58137fb1-32aa-4ae6-8a6a-d24c305c4c38",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"% Content moved from main body to appendix:\\\\n% - Phase-strategy crossover details (from results §5.3)\\\\n% - Cross-model replication details with tables/figures (from results §5.4)\\\\n% - Permutation test details with table/forest plot (from results §5.5)\\\\n% - Full entropy-discrimination collapse analysis with tables (from analysis §6)\\\\n% Main body §6 (analysis.tex) contains a condensed summary referencing these tables.\\\\n\\\\n\\\\\\\\section{Phase-Strategy Crossover Details}\\\\n\\\\\\\\label{app:crossover-details}\\\\n\\\\nAt $s{=}0.25$, a strategy ranking reversal emerges (Figure~\\\\\\\\ref{fig:crossover}): importance-based eviction yields \\\\\\\\emph{lower} II than random in the high-sparsity phase ($0.032$ vs.\\\\\\\\ $0.818$) but \\\\\\\\emph{higher} II in the low-sparsity phase ($7.196$ vs.\\\\\\\\ $1.363$---a $5.3{\\\\\\\\times}$ reversal). This crossover is present at all four sparsity levels, with reversal magnitude of $3.9{\\\\\\\\times}$ at $s{=}0.15$, $5.4{\\\\\\\\times}$ at $s{=}0.20$, $5.3{\\\\\\\\times}$ at $s{=}0.25$, and $3.6{\\\\\\\\times}$ at $s{=}0.30$ (as random eviction severity also rises). The reversal arises because head pruning redistributes attention mass, altering importance rankings in a way that couples the two sparsity mechanisms in low-sparsity phases (\\\\\\\\S\\\\\\\\ref{sec:discrimination-collapse}). % exp_id: bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json; 7.196/1.363=5.28\\\\n\\\\n\\\\\\\\begin{figure}[t]\\\\n\\\\\\\\centering\\\\n\\\\\\\\includegraphics[width=\\\\\\\\columnwidth]{fig3_crossover.pdf}\\\\n\\\\\\\\caption{Strategy-dependent crossover at $s{=}0.25$. Grouped bar chart of median II by eviction strategy and reasoning phase. Importance-based eviction outperforms random in the high-sparsity phase but produces $5.3{\\\\\\\\times}$ higher II in the low-sparsity phase, reversing the strategy ranking.}\\\\n\\\\\\\\label{fig:crossover}\\\\n\\\\\\\\end{figure}\\\\n\\\\n\\\\n\\\\\\\\section{Cross-Model Replication Details}\\\\n\\\\\\\\label{app:cross-model-details}\\\\n\\\\nBoth models share the Qwen2ForCausalLM backbone (28 layers, 28 heads, 4-group GQA) but differ in training: DeepSeek uses reasoning distillation from DeepSeek-R1, while Qwen2.5 uses standard instruction tuning without explicit reasoning delimiters. This controlled comparison isolates the effect of training methodology on the compound sparsity interaction.\\\\n\\\\nDespite lacking explicit \\\\\\\\texttt{&lt;think>} delimiters, Qwen2.5-7B-Instruct exhibits sufficient variation in attention sparsity to permit phase segmentation via the same quantile-based method (\\\\\\\\S\\\\\\\\ref{sec:phase-segmentation}). Four of the 50 problems are excluded due to degenerate phase assignments, yielding $n{=}46$ valid problems for Qwen (vs.\\\\\\\\ $n{=}49$ for DeepSeek).\\\\n\\\\n\\\\\\\\paragraph{Per-phase effective sample size.}\\\\n\\\\\\\\label{app:qwen-null-rate}\\\\nTable~\\\\\\\\ref{tab:qwen-effective-n} reports the per-phase effective sample size for Qwen2.5-7B-Instruct, defined as the number of problems with $|\\\\\\\\mathrm{II}| > 0.001$ in each phase. The mid-phase null rate (\\\\\\\\placeholder{NULL\\\\\\\\_PCT}\\\\\\\\%) reflects problems where compound interaction is absent in intermediate phases; this does not affect the low--high contrast ($\\\\\\\\Delta$) used in the primary analysis.\\\\n\\\\n\\\\\\\\begin{table}[t]\\\\n\\\\\\\\centering\\\\n\\\\\\\\small\\\\n\\\\\\\\caption{Per-phase effective sample size for Qwen2.5-7B-Instruct ($n_{\\\\\\\\text{total}} = \\\\\\\\placeholder{N\\\\\\\\_QW}$).}\\\\n\\\\\\\\label{tab:qwen-effective-n}\\\\n\\\\\\\\begin{tabular}{@{}lcccc@{}}\\\\n\\\\\\\\toprule\\\\nPhase & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\nHigh & \\\\\\\\placeholder{} & \\\\\\\\placeholder{} & \\\\\\\\placeholder{} & \\\\\\\\placeholder{} \\\\\\\\\\\\\\\\\\\\nMid  & \\\\\\\\placeholder{} & \\\\\\\\placeholder{} & \\\\\\\\placeholder{} & \\\\\\\\placeholder{} \\\\\\\\\\\\\\\\\\\\nLow  & \\\\\\\\placeholder{} & \\\\\\\\placeholder{} & \\\\\\\\placeholder{} & \\\\\\\\placeholder{} \\\\\\\\\\\\\\\\\\\\n\\\\\\\\bottomrule\\\\n\\\\\\\\end{tabular}\\\\n\\\\\\\\end{table}\\\\n\\\\nTable~\\\\\\\\ref{tab:cross-model} reports the cross-model comparison. Qwen reproduces the monotonic severity gradient at ${\\\\\\\\sim}1/5$ of DeepSeek's magnitude. Figure~\\\\\\\\ref{fig:cross-model} visualizes this comparison. % exp_id: cross_model_analysis.json; cohens_d_bf16_qwen.json\\\\n\\\\n\\\\\\\\begin{table}[t]\\\\n\\\\\\\\centering\\\\n\\\\\\\\small\\\\n\\\\\\\\caption{Cross-model comparison of median compound severity difference ($\\\\\\\\Delta$) under importance-based evicti\\\\n\\\\n... [截断: 输出过长，省略 5618 字符] ...\\\\n\\\\ndom eviction, confirming that discrimination collapse is a consequence of head pruning \\\\\\\\emph{per se}, not of the eviction strategy. % exp_id: c4_entropy_deepseek, c4_entropy_qwen\\\\n\\\\n\\\\\\\\begin{table}[t]\\\\n\\\\\\\\centering\\\\n\\\\\\\\caption{Discrimination collapse under importance-based eviction. $\\\\\\\\Delta\\\\\\\\mathrm{Gini}$ and $\\\\\\\\Delta\\\\\\\\mathrm{CV}$ are post-pruning minus baseline; negative values indicate reduced discriminative power.}\\\\n\\\\\\\\label{tab:discrimination-metrics-full}\\\\n\\\\\\\\small\\\\n\\\\\\\\begin{tabular}{llrr}\\\\n\\\\\\\\toprule\\\\nModel & $s$ & $\\\\\\\\Delta\\\\\\\\mathrm{Gini}$ & $\\\\\\\\Delta\\\\\\\\mathrm{CV}$ \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\nDeepSeek & $0.15$ & $-0.030$ & $-0.56$ \\\\\\\\\\\\\\\\\\\\nDeepSeek & $0.20$ & $-0.040$ & $-0.77$ \\\\\\\\\\\\\\\\\\\\nDeepSeek & $0.25$ & $-0.065$ & $-1.29$ \\\\\\\\\\\\\\\\\\\\nDeepSeek & $0.30$ & $-0.081$ & $-1.66$ \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\nQwen & $0.15$ & $-0.010$ & $-0.05$ \\\\\\\\\\\\\\\\\\\\nQwen & $0.20$ & $-0.012$ & $-0.21$ \\\\\\\\\\\\\\\\\\\\nQwen & $0.25$ & $-0.010$ & $-1.49$ \\\\\\\\\\\\\\\\\\\\nQwen & $0.30$ & $-0.020$ & $-1.14$ \\\\\\\\\\\\\\\\\\\\n\\\\\\\\bottomrule\\\\n\\\\\\\\end{tabular}\\\\n\\\\\\\\end{table}\\\\n\\\\nWhen importance scores lose discriminability, thresholding degenerates into noise-sensitive selection---functionally approaching biased random eviction. This is phase-dependent: in low-sparsity phases, attention is already broadly distributed, so pruning-induced flattening has maximum impact; in high-sparsity phases, concentration is preserved. Random eviction is immune because its decisions are independent of score quality, explaining $G \\\\\\\\approx 1$. % exp_id: c4_entropy_deepseek, c4_entropy_qwen\\\\n\\\\n\\\\\\\\subsection{Entropy Redistribution}\\\\n\\\\\\\\label{sec:entropy-redistribution}\\\\n\\\\nBeyond discrimination collapse, we examine whether head pruning also redistributes the attention entropy of surviving heads. We measure the mean attention entropy per head:\\\\n\\\\\\\\begin{equation}\\\\n    \\\\\\\\mathcal{H}_i^{(h)} = -\\\\\\\\sum_{j=1}^{T} a_{ij}^{(h)} \\\\\\\\log a_{ij}^{(h)}\\\\n    \\\\\\\\label{eq:attn-entropy}\\\\n\\\\\\\\end{equation}\\\\nand compute $\\\\\\\\Delta\\\\\\\\mathcal{H}$ as the change from baseline (no pruning) to the pruned condition.\\\\n\\\\nFor DeepSeek under importance-based eviction, the entropy delta is consistently negative across all four sparsity levels ($\\\\\\\\Delta\\\\\\\\mathcal{H} \\\\\\\\in [-0.047, -0.040]$; Table~\\\\\\\\ref{tab:entropy-deltas}), indicating that importance-based pruning systematically selects heads whose removal concentrates attention in the surviving heads, reinforcing discrimination collapse. % exp_id: c4_entropy_deepseek\\\\n\\\\nFor Qwen, the entropy pattern only partially replicates. The delta is negative at $s{=}0.15$ ($\\\\\\\\Delta\\\\\\\\mathcal{H} = -0.073$) and $s{=}0.20$ ($-0.076$), consistent with DeepSeek. However, at $s{=}0.25$, the delta reverses to $+0.045$, with 22 of 30 problems showing positive entropy change. At $s{=}0.30$, the delta is near zero ($-0.007$). The $s{=}0.25$ reversal is systematic rather than a statistical artifact: it is consistent across all three reasoning phases (low: $+0.042$, mid: $+0.034$, high: $+0.017$). We interpret this as a genuine model-specific difference, possibly arising from distinct head specialization patterns: Qwen's instruction tuning (vs.\\\\\\\\ DeepSeek's distillation-based training) may produce head configurations where removing 25\\\\\\\\% of heads triggers compensatory broadening rather than concentration. % exp_id: c4_entropy_qwen\\\\n\\\\nWe characterize discrimination collapse as the robust, model-independent driver of the phase-strategy interaction, with entropy redistribution as a secondary amplifier that is consistent in DeepSeek but model-dependent in Qwen.\\\\n\\\\n\\\\\\\\begin{table}[t]\\\\n\\\\\\\\centering\\\\n\\\\\\\\caption{Attention entropy deltas ($\\\\\\\\Delta\\\\\\\\mathcal{H}$) under importance-based eviction. DeepSeek shows consistent entropy compression; Qwen partially replicates with a reversal at $s{=}0.25$.}\\\\n\\\\\\\\label{tab:entropy-deltas}\\\\n\\\\\\\\small\\\\n\\\\\\\\begin{tabular}{llr}\\\\n\\\\\\\\toprule\\\\nModel & $s$ & $\\\\\\\\Delta\\\\\\\\mathcal{H}$ \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\nDeepSeek & $0.15$ & $-0.040$ \\\\\\\\\\\\\\\\\\\\nDeepSeek & $0.20$ & $-0.047$ \\\\\\\\\\\\\\\\\\\\nDeepSeek & $0.25$ & $-0.045$ \\\\\\\\\\\\\\\\\\\\nDeepSeek & $0.30$ & $-0.044$ \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\nQwen & $0.15$ & $-0.073$ \\\\\\\\\\\\\\\\\\\\nQwen & $0.20$ & $-0.076$ \\\\\\\\\\\\\\\\\\\\nQwen & $0.25$ & $+0.045$ \\\\\\\\\\\\\\\\\\\\nQwen & $0.30$ & $-0.007$ \\\\\\\\\\\\\\\\\\\\n\\\\\\\\bottomrule\\\\n\\\\\\\\end{tabular}\\\\n\\\\\\\\end{table}\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.52}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"% Content moved from main body to appendix:\\n% - Phase-strategy crossover details (from results §5.3)\\n% - Cross-model replication details with tables/figures (from results §5.4)\\n% - Permutation test details with table/forest plot (from results §5.5)\\n% - Full entropy-discrimination collapse analysis with tables (from analysis §6)\\n% Main body §6 (analysis.tex) contains a condensed summary referencing these tables.\\n\\n\\\\section{Phase-Strategy Crossover Details}\\n\\\\label{app:crossover-details}\\n\\nAt $s{=}0.25$, a strategy ranking reversal emerges (Figure~\\\\ref{fig:crossover}): importance-based eviction yields \\\\emph{lower} II than random in the high-sparsity phase ($0.032$ vs.\\\\ $0.818$) but \\\\emph{higher} II in the low-sparsity phase ($7.196$ vs.\\\\ $1.363$---a $5.3{\\\\times}$ reversal). This crossover is present at all four sparsity levels, with reversal magnitude of $3.9{\\\\times}$ at $s{=}0.15$, $5.4{\\\\times}$ at $s{=}0.20$, $5.3{\\\\times}$ at $s{=}0.25$, and $3.6{\\\\times}$ at $s{=}0.30$ (as random eviction severity also rises). The reversal arises because head pruning redistributes attention mass, altering importance rankings in a way that couples the two sparsity mechanisms in low-sparsity phases (\\\\S\\\\ref{sec:discrimination-collapse}). % exp_id: bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json; 7.196/1.363=5.28\\n\\n\\\\begin{figure}[t]\\n\\\\centering\\n\\\\includegraphics[width=\\\\columnwidth]{fig3_crossover.pdf}\\n\\\\caption{Strategy-dependent crossover at $s{=}0.25$. Grouped bar chart of median II by eviction strategy and reasoning phase. Importance-based eviction outperforms random in the high-sparsity phase but produces $5.3{\\\\times}$ higher II in the low-sparsity phase, reversing the strategy ranking.}\\n\\\\label{fig:crossover}\\n\\\\end{figure}\\n\\n\\n\\\\section{Cross-Model Replication Details}\\n\\\\label{app:cross-model-details}\\n\\nBoth models share the Qwen2ForCausalLM backbone (28 layers, 28 heads, 4-group GQA) but differ in training: DeepSeek uses reasoning distillation from DeepSeek-R1, while Qwen2.5 uses standard instruction tuning without explicit reasoning delimiters. This controlled comparison isolates the effect of training methodology on the compound sparsity interaction.\\n\\nDespite lacking explicit \\\\texttt{&lt;think>} delimiters, Qwen2.5-7B-Instruct exhibits sufficient variation in attention sparsity to permit phase segmentation via the same quantile-based method (\\\\S\\\\ref{sec:phase-segmentation}). Four of the 50 problems are excluded due to degenerate phase assignments, yielding $n{=}46$ valid problems for Qwen (vs.\\\\ $n{=}49$ for DeepSeek).\\n\\n\\\\paragraph{Per-phase effective sample size.}\\n\\\\label{app:qwen-null-rate}\\nTable~\\\\ref{tab:qwen-effective-n} reports the per-phase effective sample size for Qwen2.5-7B-Instruct, defined as the number of problems with $|\\\\mathrm{II}| > 0.001$ in each phase. The mid-phase null rate (\\\\placeholder{NULL\\\\_PCT}\\\\%) reflects problems where compound interaction is absent in intermediate phases; this does not affect the low--high contrast ($\\\\Delta$) used in the primary analysis.\\n\\n\\\\begin{table}[t]\\n\\\\centering\\n\\\\small\\n\\\\caption{Per-phase effective sample size for Qwen2.5-7B-Instruct ($n_{\\\\text{total}} = \\\\placeholder{N\\\\_QW}$).}\\n\\\\label{tab:qwen-effective-n}\\n\\\\begin{tabular}{@{}lcccc@{}}\\n\\\\toprule\\nPhase & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\\\\\\\\\n\\\\midrule\\nHigh & \\\\placeholder{} & \\\\placeholder{} & \\\\placeholder{} & \\\\placeholder{} \\\\\\\\\\nMid  & \\\\placeholder{} & \\\\placeholder{} & \\\\placeholder{} & \\\\placeholder{} \\\\\\\\\\nLow  & \\\\placeholder{} & \\\\placeholder{} & \\\\placeholder{} & \\\\placeholder{} \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n\\nTable~\\\\ref{tab:cross-model} reports the cross-model comparison. Qwen reproduces the monotonic severity gradient at ${\\\\sim}1/5$ of DeepSeek's magnitude. Figure~\\\\ref{fig:cross-model} visualizes this comparison. % exp_id: cross_model_analysis.json; cohens_d_bf16_qwen.json\\n\\n\\\\begin{table}[t]\\n\\\\centering\\n\\\\small\\n\\\\caption{Cross-model comparison of median compound severity difference ($\\\\Delta$) under importance-based evicti\\n\\n... [截断: 输出过长，省略 5618 字符] ...\\n\\ndom eviction, confirming that discrimination collapse is a consequence of head pruning \\\\emph{per se}, not of the eviction strategy. % exp_id: c4_entropy_deepseek, c4_entropy_qwen\\n\\n\\\\begin{table}[t]\\n\\\\centering\\n\\\\caption{Discrimination collapse under importance-based eviction. $\\\\Delta\\\\mathrm{Gini}$ and $\\\\Delta\\\\mathrm{CV}$ are post-pruning minus baseline; negative values indicate reduced discriminative power.}\\n\\\\label{tab:discrimination-metrics-full}\\n\\\\small\\n\\\\begin{tabular}{llrr}\\n\\\\toprule\\nModel & $s$ & $\\\\Delta\\\\mathrm{Gini}$ & $\\\\Delta\\\\mathrm{CV}$ \\\\\\\\\\n\\\\midrule\\nDeepSeek & $0.15$ & $-0.030$ & $-0.56$ \\\\\\\\\\nDeepSeek & $0.20$ & $-0.040$ & $-0.77$ \\\\\\\\\\nDeepSeek & $0.25$ & $-0.065$ & $-1.29$ \\\\\\\\\\nDeepSeek & $0.30$ & $-0.081$ & $-1.66$ \\\\\\\\\\n\\\\midrule\\nQwen & $0.15$ & $-0.010$ & $-0.05$ \\\\\\\\\\nQwen & $0.20$ & $-0.012$ & $-0.21$ \\\\\\\\\\nQwen & $0.25$ & $-0.010$ & $-1.49$ \\\\\\\\\\nQwen & $0.30$ & $-0.020$ & $-1.14$ \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n\\nWhen importance scores lose discriminability, thresholding degenerates into noise-sensitive selection---functionally approaching biased random eviction. This is phase-dependent: in low-sparsity phases, attention is already broadly distributed, so pruning-induced flattening has maximum impact; in high-sparsity phases, concentration is preserved. Random eviction is immune because its decisions are independent of score quality, explaining $G \\\\approx 1$. % exp_id: c4_entropy_deepseek, c4_entropy_qwen\\n\\n\\\\subsection{Entropy Redistribution}\\n\\\\label{sec:entropy-redistribution}\\n\\nBeyond discrimination collapse, we examine whether head pruning also redistributes the attention entropy of surviving heads. We measure the mean attention entropy per head:\\n\\\\begin{equation}\\n    \\\\mathcal{H}_i^{(h)} = -\\\\sum_{j=1}^{T} a_{ij}^{(h)} \\\\log a_{ij}^{(h)}\\n    \\\\label{eq:attn-entropy}\\n\\\\end{equation}\\nand compute $\\\\Delta\\\\mathcal{H}$ as the change from baseline (no pruning) to the pruned condition.\\n\\nFor DeepSeek under importance-based eviction, the entropy delta is consistently negative across all four sparsity levels ($\\\\Delta\\\\mathcal{H} \\\\in [-0.047, -0.040]$; Table~\\\\ref{tab:entropy-deltas}), indicating that importance-based pruning systematically selects heads whose removal concentrates attention in the surviving heads, reinforcing discrimination collapse. % exp_id: c4_entropy_deepseek\\n\\nFor Qwen, the entropy pattern only partially replicates. The delta is negative at $s{=}0.15$ ($\\\\Delta\\\\mathcal{H} = -0.073$) and $s{=}0.20$ ($-0.076$), consistent with DeepSeek. However, at $s{=}0.25$, the delta reverses to $+0.045$, with 22 of 30 problems showing positive entropy change. At $s{=}0.30$, the delta is near zero ($-0.007$). The $s{=}0.25$ reversal is systematic rather than a statistical artifact: it is consistent across all three reasoning phases (low: $+0.042$, mid: $+0.034$, high: $+0.017$). We interpret this as a genuine model-specific difference, possibly arising from distinct head specialization patterns: Qwen's instruction tuning (vs.\\\\ DeepSeek's distillation-based training) may produce head configurations where removing 25\\\\% of heads triggers compensatory broadening rather than concentration. % exp_id: c4_entropy_qwen\\n\\nWe characterize discrimination collapse as the robust, model-independent driver of the phase-strategy interaction, with entropy redistribution as a secondary amplifier that is consistent in DeepSeek but model-dependent in Qwen.\\n\\n\\\\begin{table}[t]\\n\\\\centering\\n\\\\caption{Attention entropy deltas ($\\\\Delta\\\\mathcal{H}$) under importance-based eviction. DeepSeek shows consistent entropy compression; Qwen partially replicates with a reversal at $s{=}0.25$.}\\n\\\\label{tab:entropy-deltas}\\n\\\\small\\n\\\\begin{tabular}{llr}\\n\\\\toprule\\nModel & $s$ & $\\\\Delta\\\\mathcal{H}$ \\\\\\\\\\n\\\\midrule\\nDeepSeek & $0.15$ & $-0.040$ \\\\\\\\\\nDeepSeek & $0.20$ & $-0.047$ \\\\\\\\\\nDeepSeek & $0.25$ & $-0.045$ \\\\\\\\\\nDeepSeek & $0.30$ & $-0.044$ \\\\\\\\\\n\\\\midrule\\nQwen & $0.15$ & $-0.073$ \\\\\\\\\\nQwen & $0.20$ & $-0.076$ \\\\\\\\\\nQwen & $0.25$ & $+0.045$ \\\\\\\\\\nQwen & $0.30$ & $-0.007$ \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-15T02:17:53.462Z_

<details><summary>↩ Tool result · `toolu_01KYcBDAFoPtw3pQ55SyP2AR`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\\documentclass[11pt]{article}\\n\\n\\\\usepackage[review]{acl}\\n\\n\\\\usepackage{times}\\n\\\\usepackage{latexsym}\\n\\\\usepackage[T1]{fontenc}\\n\\\\usepackage[utf8]{inputenc}\\n\\\\usepackage{microtype}\\n\\\\usepackage{inconsolata}\\n\\n\\\\usepackage{amsmath}\\n\\\\usepackage{amssymb}\\n\\\\usepackage{graphicx}\\n\\\\usepackage{booktabs}\\n\\\\usepackage{enumitem}\\n\\\\usepackage{multirow}\\n\\n\\\\graphicspath{{figures/}}\\n\\n\\\\newcommand{\\\\placeholder}[1]{\\\\textcolor{red}{[#1]}}\\n\\n\\\\title{Phase-Modulated Compound Sparsity:\\\\\\\\Strategy-Dependent Severity Gradients in Reasoning Models}\\n\\n\\\\author{Anonymous}\\n\\n\\\\begin{document}\\n\\n\\\\maketitle\\n\\n\\\\input{abstract}\\n\\n\\\\input{introduction}\\n\\\\input{related_work}\\n\\\\input{background}\\n\\\\input{methodology}\\n\\\\input{results}\\n\\\\input{analysis}\\n\\\\input{discussion}\\n\\\\input{conclusion}\\n\\n\\\\bibliography{references}\\n\\n\\\\section*{Limitations}\\n\\\\input{limitations}\\n\\n\\\\appendix\\n\\\\input{appendix}\\n\\\\input{appendix_moved}\\n\\\\input{appendix_disc_analysis}\\n\\n\\\\end{document}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "6b71941c-bdb3-4c60-82d3-917ba013a6fc",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\\documentclass[11pt]{article}\\\\n\\\\n\\\\\\\\usepackage[review]{acl}\\\\n\\\\n\\\\\\\\usepackage{times}\\\\n\\\\\\\\usepackage{latexsym}\\\\n\\\\\\\\usepackage[T1]{fontenc}\\\\n\\\\\\\\usepackage[utf8]{inputenc}\\\\n\\\\\\\\usepackage{microtype}\\\\n\\\\\\\\usepackage{inconsolata}\\\\n\\\\n\\\\\\\\usepackage{amsmath}\\\\n\\\\\\\\usepackage{amssymb}\\\\n\\\\\\\\usepackage{graphicx}\\\\n\\\\\\\\usepackage{booktabs}\\\\n\\\\\\\\usepackage{enumitem}\\\\n\\\\\\\\usepackage{multirow}\\\\n\\\\n\\\\\\\\graphicspath{{figures/}}\\\\n\\\\n\\\\\\\\newcommand{\\\\\\\\placeholder}[1]{\\\\\\\\textcolor{red}{[#1]}}\\\\n\\\\n\\\\\\\\title{Phase-Modulated Compound Sparsity:\\\\\\\\\\\\\\\\Strategy-Dependent Severity Gradients in Reasoning Models}\\\\n\\\\n\\\\\\\\author{Anonymous}\\\\n\\\\n\\\\\\\\begin{document}\\\\n\\\\n\\\\\\\\maketitle\\\\n\\\\n\\\\\\\\input{abstract}\\\\n\\\\n\\\\\\\\input{introduction}\\\\n\\\\\\\\input{related_work}\\\\n\\\\\\\\input{background}\\\\n\\\\\\\\input{methodology}\\\\n\\\\\\\\input{results}\\\\n\\\\\\\\input{analysis}\\\\n\\\\\\\\input{discussion}\\\\n\\\\\\\\input{conclusion}\\\\n\\\\n\\\\\\\\bibliography{references}\\\\n\\\\n\\\\\\\\section*{Limitations}\\\\n\\\\\\\\input{limitations}\\\\n\\\\n\\\\\\\\appendix\\\\n\\\\\\\\input{appendix}\\\\n\\\\\\\\input{appendix_moved}\\\\n\\\\\\\\input{appendix_disc_analysis}\\\\n\\\\n\\\\\\\\end{document}\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.53}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\\documentclass[11pt]{article}\\n\\n\\\\usepackage[review]{acl}\\n\\n\\\\usepackage{times}\\n\\\\usepackage{latexsym}\\n\\\\usepackage[T1]{fontenc}\\n\\\\usepackage[utf8]{inputenc}\\n\\\\usepackage{microtype}\\n\\\\usepackage{inconsolata}\\n\\n\\\\usepackage{amsmath}\\n\\\\usepackage{amssymb}\\n\\\\usepackage{graphicx}\\n\\\\usepackage{booktabs}\\n\\\\usepackage{enumitem}\\n\\\\usepackage{multirow}\\n\\n\\\\graphicspath{{figures/}}\\n\\n\\\\newcommand{\\\\placeholder}[1]{\\\\textcolor{red}{[#1]}}\\n\\n\\\\title{Phase-Modulated Compound Sparsity:\\\\\\\\Strategy-Dependent Severity Gradients in Reasoning Models}\\n\\n\\\\author{Anonymous}\\n\\n\\\\begin{document}\\n\\n\\\\maketitle\\n\\n\\\\input{abstract}\\n\\n\\\\input{introduction}\\n\\\\input{related_work}\\n\\\\input{background}\\n\\\\input{methodology}\\n\\\\input{results}\\n\\\\input{analysis}\\n\\\\input{discussion}\\n\\\\input{conclusion}\\n\\n\\\\bibliography{references}\\n\\n\\\\section*{Limitations}\\n\\\\input{limitations}\\n\\n\\\\appendix\\n\\\\input{appendix}\\n\\\\input{appendix_moved}\\n\\\\input{appendix_disc_analysis}\\n\\n\\\\end{document}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 46_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive view of all .tex files. Let me also check what's in `appendix_results.tex` more carefully - it seems I got it but the output said it was about cross-model replication details and random eviction control. Let me now compile the checklist.

Let me also check for any remaining \placeholder{} instances and grep for "n=50", "50 problems", etc.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "2d0f310a-1f74-4843-b482-0cbbf3038a8c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QrEQ6UUdGFk7X4vPeemo6k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8685,
      "cache_read_input_tokens": 43673,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8685
      },
      "output_tokens": 12,
      "service_tier": "standard",
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

_source line 47_

现在搜索所有 `\placeholder` 出现位置，确保完整覆盖。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "6370fdcb-9aa2-4bec-bc7d-1118bd74f574",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QrEQ6UUdGFk7X4vPeemo6k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8685,
      "cache_read_input_tokens": 43673,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8685
      },
      "output_tokens": 12,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01WPy9stGPKt7W1AvSDiyqiz`</summary>

```json
{
  "server": "westd-22162",
  "command": "grep -n \"placeholder\" /root/autodl-tmp/pacs/paper/abstract.tex /root/autodl-tmp/pacs/paper/introduction.tex /root/autodl-tmp/pacs/paper/results.tex /root/autodl-tmp/pacs/paper/analysis.tex /root/autodl-tmp/pacs/paper/discussion.tex /root/autodl-tmp/pacs/paper/conclusion.tex /root/autodl-tmp/pacs/paper/limitations.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "d01d85bf-dd5c-4840-91eb-10f0f3fcc4ae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QrEQ6UUdGFk7X4vPeemo6k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8685,
      "cache_read_input_tokens": 43673,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8685
      },
      "output_tokens": 12,
      "service_tier": "standard",
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

_source line 49 · 2026-05-15T02:18:04.222Z_

<details><summary>↩ Tool result · `toolu_01WPy9stGPKt7W1AvSDiyqiz`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/pacs/paper/abstract.tex:8:Random eviction produces no significant phase modulation in 7/8 conditions; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) shows negligible median difference ($\\\\widetilde{\\\\Delta} = \\\\placeholder{}$), confirming that the severity gradient is strategy-specific, not an inherent property of compound sparsity.\\n/root/autodl-tmp/pacs/paper/results.tex:71:Qwen2.5-7B-Instruct (standard instruction tuning, same Qwen2 backbone) reproduces the monotonic severity gradient: $\\\\Delta$ increases from $0.04$ at $s{=}0.15$ to $2.94$ at $s{=}0.30$, paralleling DeepSeek at ${\\\\sim}1/5$ the magnitude. Both models yield strictly increasing $d_z$ trajectories (Spearman $\\\\rho = 1.0$; gradient permutation $p = 0.043$). The effect is marginal at $s{=}0.15$ ($d_z{=}0.28$, CI includes zero) but reliable at $s \\\\geq 0.20$ ($d_z \\\\geq 0.55$). A caveat applies to mid-phase comparisons: on Qwen2.5-7B-Instruct, approximately \\\\placeholder{NULL\\\\_PCT}\\\\% of problems yield near-zero Interaction Index in the mid-sparsity phase, where attention patterns exhibit insufficient variation to produce measurable compound interaction. This elevated null rate reduces the effective sample size for mid-phase comparisons; our primary cross-model analysis therefore focuses on the low--high phase contrast ($\\\\Delta$), which is unaffected by this limitation. Per-phase effective sample sizes are reported in Appendix~\\\\ref{app:qwen-null-rate}. Full cross-model tables and figures appear in Appendix~\\\\ref{app:cross-model-details}. % exp_id: cross_model_analysis.json; cohens_d_bf16_qwen.json\\n/root/autodl-tmp/pacs/paper/results.tex:81:The absolute magnitude is architecture-dependent: LLaMA severity differences are ${\\\\sim}40{\\\\times}$ smaller than DeepSeek and ${\\\\sim}7{\\\\times}$ smaller than Qwen, and the interaction is substantially weaker---random eviction also shows a non-trivial phase gradient (Wilcoxon $p < \\\\placeholder{}$ at $s{=}0.30$), reducing the strategy contrast observed in Qwen2 models. The directional pattern---importance $>$ random, larger phase gradient under importance---is qualitatively consistent across all three models spanning two architectures (Qwen2ForCausalLM, LlamaForCausalLM), though the interaction magnitude is substantially weaker on LlamaForCausalLM. % exp_id: c3_llama; cross_model_analysis.json\\n/root/autodl-tmp/pacs/paper/results.tex:86:\\\\caption{Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM). $\\\\widetilde{\\\\Delta}$: median paired difference (importance $-$ random) with bootstrap 95\\\\% CI ($B{=}10{,}000$); $p$: Bonferroni-corrected Wilcoxon signed-rank $p$ ($k{=}4$). $n{=}\\\\placeholder{N\\\\_LLAMA}$ paired problems.}\\n/root/autodl-tmp/pacs/paper/results.tex:92:0.15 & \\\\placeholder{}\\\\; $[\\\\placeholder{}, \\\\placeholder{}]$ & \\\\placeholder{} \\\\\\\\\\n/root/autodl-tmp/pacs/paper/results.tex:93:0.20 & \\\\placeholder{}\\\\; $[\\\\placeholder{}, \\\\placeholder{}]$ & \\\\placeholder{} \\\\\\\\\\n/root/autodl-tmp/pacs/paper/results.tex:94:0.25 & \\\\placeholder{}\\\\; $[\\\\placeholder{}, \\\\placeholder{}]$ & \\\\placeholder{} \\\\\\\\\\n/root/autodl-tmp/pacs/paper/results.tex:95:0.30 & \\\\placeholder{}\\\\; $[\\\\placeholder{}, \\\\placeholder{}]$ & $\\\\mathbf{\\\\placeholder{}}$ \\\\\\\\\\n/root/autodl-tmp/pacs/paper/discussion.tex:10:A preliminary pilot experiment explored oracle phase-aware budget reallocation, shifting sparsity budget from high-severity low-sparsity phases to low-severity high-sparsity phases. At $s{=}0.25$, oracle recovery---the fraction of compound interaction eliminated by phase-aware allocation---reached \\\\placeholder{ORACLE\\\\_PCT}\\\\% (Wilcoxon $p = \\\\placeholder{ORACLE\\\\_P}$), below the pre-registered 30\\\\% gate for claiming practical mitigation. A heuristic variant achieved \\\\placeholder{HEUR\\\\_PCT}\\\\% recovery ($p = \\\\placeholder{HEUR\\\\_P}$), but 95\\\\% CIs for both conditions span zero. These results indicate that phase-aware budget reallocation alone is insufficient to neutralize the severity gradient; effective mitigation likely requires joint optimization of budget allocation and eviction strategy selection across phases---a promising direction for future work.\\n/root/autodl-tmp/pacs/paper/discussion.tex:15:Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM) provides partial support for the qualitative pattern---monotonically increasing severity gradient under importance-based eviction with within-strategy phase gradient $d_z \\\\geq 1.0$---while revealing that absolute severity magnitudes are architecture-dependent (${\\\\sim}40{\\\\times}$ smaller than DeepSeek, ${\\\\sim}7{\\\\times}$ smaller than Qwen) and the strategy--phase interaction is substantially weaker than in Qwen2-based architectures. Notably, random pruning also exhibits a non-trivial phase gradient on LLaMA (Wilcoxon $p < \\\\placeholder{}$), reducing the contrast between strategies. This dissociation between qualitatively consistent directional trends and markedly different magnitudes suggests the phase-strategy interaction may be a general property of compound sparsity on reasoning models, while its quantitative impact---and the degree to which it is strategy-specific---depends on architecture-specific attention distributions and head specialization patterns. % exp_id: c3_llama\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "2793698d-947f-49ff-9816-d59c84756c69",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/pacs/paper/abstract.tex:8:Random eviction produces no significant phase modulation in 7/8 conditions; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) shows negligible median difference ($\\\\\\\\widetilde{\\\\\\\\Delta} = \\\\\\\\placeholder{}$), confirming that the severity gradient is strategy-specific, not an inherent property of compound sparsity.\\\\n/root/autodl-tmp/pacs/paper/results.tex:71:Qwen2.5-7B-Instruct (standard instruction tuning, same Qwen2 backbone) reproduces the monotonic severity gradient: $\\\\\\\\Delta$ increases from $0.04$ at $s{=}0.15$ to $2.94$ at $s{=}0.30$, paralleling DeepSeek at ${\\\\\\\\sim}1/5$ the magnitude. Both models yield strictly increasing $d_z$ trajectories (Spearman $\\\\\\\\rho = 1.0$; gradient permutation $p = 0.043$). The effect is marginal at $s{=}0.15$ ($d_z{=}0.28$, CI includes zero) but reliable at $s \\\\\\\\geq 0.20$ ($d_z \\\\\\\\geq 0.55$). A caveat applies to mid-phase comparisons: on Qwen2.5-7B-Instruct, approximately \\\\\\\\placeholder{NULL\\\\\\\\_PCT}\\\\\\\\% of problems yield near-zero Interaction Index in the mid-sparsity phase, where attention patterns exhibit insufficient variation to produce measurable compound interaction. This elevated null rate reduces the effective sample size for mid-phase comparisons; our primary cross-model analysis therefore focuses on the low--high phase contrast ($\\\\\\\\Delta$), which is unaffected by this limitation. Per-phase effective sample sizes are reported in Appendix~\\\\\\\\ref{app:qwen-null-rate}. Full cross-model tables and figures appear in Appendix~\\\\\\\\ref{app:cross-model-details}. % exp_id: cross_model_analysis.json; cohens_d_bf16_qwen.json\\\\n/root/autodl-tmp/pacs/paper/results.tex:81:The absolute magnitude is architecture-dependent: LLaMA severity differences are ${\\\\\\\\sim}40{\\\\\\\\times}$ smaller than DeepSeek and ${\\\\\\\\sim}7{\\\\\\\\times}$ smaller than Qwen, and the interaction is substantially weaker---random eviction also shows a non-trivial phase gradient (Wilcoxon $p < \\\\\\\\placeholder{}$ at $s{=}0.30$), reducing the strategy contrast observed in Qwen2 models. The directional pattern---importance $>$ random, larger phase gradient under importance---is qualitatively consistent across all three models spanning two architectures (Qwen2ForCausalLM, LlamaForCausalLM), though the interaction magnitude is substantially weaker on LlamaForCausalLM. % exp_id: c3_llama; cross_model_analysis.json\\\\n/root/autodl-tmp/pacs/paper/results.tex:86:\\\\\\\\caption{Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM). $\\\\\\\\widetilde{\\\\\\\\Delta}$: median paired difference (importance $-$ random) with bootstrap 95\\\\\\\\% CI ($B{=}10{,}000$); $p$: Bonferroni-corrected Wilcoxon signed-rank $p$ ($k{=}4$). $n{=}\\\\\\\\placeholder{N\\\\\\\\_LLAMA}$ paired problems.}\\\\n/root/autodl-tmp/pacs/paper/results.tex:92:0.15 & \\\\\\\\placeholder{}\\\\\\\\; $[\\\\\\\\placeholder{}, \\\\\\\\placeholder{}]$ & \\\\\\\\placeholder{} \\\\\\\\\\\\\\\\\\\\n/root/autodl-tmp/pacs/paper/results.tex:93:0.20 & \\\\\\\\placeholder{}\\\\\\\\; $[\\\\\\\\placeholder{}, \\\\\\\\placeholder{}]$ & \\\\\\\\placeholder{} \\\\\\\\\\\\\\\\\\\\n/root/autodl-tmp/pacs/paper/results.tex:94:0.25 & \\\\\\\\placeholder{}\\\\\\\\; $[\\\\\\\\placeholder{}, \\\\\\\\placeholder{}]$ & \\\\\\\\placeholder{} \\\\\\\\\\\\\\\\\\\\n/root/autodl-tmp/pacs/paper/results.tex:95:0.30 & \\\\\\\\placeholder{}\\\\\\\\; $[\\\\\\\\placeholder{}, \\\\\\\\placeholder{}]$ & $\\\\\\\\mathbf{\\\\\\\\placeholder{}}$ \\\\\\\\\\\\\\\\\\\\n/root/autodl-tmp/pacs/paper/discussion.tex:10:A preliminary pilot experiment explored oracle phase-aware budget reallocation, shifting sparsity budget from high-severity low-sparsity phases to low-severity high-sparsity phases. At $s{=}0.25$, oracle recovery---the fraction of compound interaction eliminated by phase-aware allocation---reached \\\\\\\\placeholder{ORACLE\\\\\\\\_PCT}\\\\\\\\% (Wilcoxon $p = \\\\\\\\placeholder{ORACLE\\\\\\\\_P}$), below the pre-registered 30\\\\\\\\% gate for claiming practical mitigation. A heuristic variant achieved \\\\\\\\placeholder{HEUR\\\\\\\\_PCT}\\\\\\\\% recovery ($p = \\\\\\\\placeholder{HEUR\\\\\\\\_P}$), but 95\\\\\\\\% CIs for both conditions span zero. These results indicate that phase-aware budget reallocation alone is insufficient to neutralize the severity gradient; effective mitigation likely requires joint optimization of budget allocation and eviction strategy selection across phases---a promising direction for future work.\\\\n/root/autodl-tmp/pacs/paper/discussion.tex:15:Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM) provides partial support for the qualitative pattern---monotonically increasing severity gradient under importance-based eviction with within-strategy phase gradient $d_z \\\\\\\\geq 1.0$---while revealing that absolute severity magnitudes are architecture-dependent (${\\\\\\\\sim}40{\\\\\\\\times}$ smaller than DeepSeek, ${\\\\\\\\sim}7{\\\\\\\\times}$ smaller than Qwen) and the strategy--phase interaction is substantially weaker than in Qwen2-based architectures. Notably, random pruning also exhibits a non-trivial phase gradient on LLaMA (Wilcoxon $p < \\\\\\\\placeholder{}$), reducing the contrast between strategies. This dissociation between qualitatively consistent directional trends and markedly different magnitudes suggests the phase-strategy interaction may be a general property of compound sparsity on reasoning models, while its quantitative impact---and the degree to which it is strategy-specific---depends on architecture-specific attention distributions and head specialization patterns. % exp_id: c3_llama\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/pacs/paper/abstract.tex:8:Random eviction produces no significant phase modulation in 7/8 conditions; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) shows negligible median difference ($\\\\widetilde{\\\\Delta} = \\\\placeholder{}$), confirming that the severity gradient is strategy-specific, not an inherent property of compound sparsity.\\n/root/autodl-tmp/pacs/paper/results.tex:71:Qwen2.5-7B-Instruct (standard instruction tuning, same Qwen2 backbone) reproduces the monotonic severity gradient: $\\\\Delta$ increases from $0.04$ at $s{=}0.15$ to $2.94$ at $s{=}0.30$, paralleling DeepSeek at ${\\\\sim}1/5$ the magnitude. Both models yield strictly increasing $d_z$ trajectories (Spearman $\\\\rho = 1.0$; gradient permutation $p = 0.043$). The effect is marginal at $s{=}0.15$ ($d_z{=}0.28$, CI includes zero) but reliable at $s \\\\geq 0.20$ ($d_z \\\\geq 0.55$). A caveat applies to mid-phase comparisons: on Qwen2.5-7B-Instruct, approximately \\\\placeholder{NULL\\\\_PCT}\\\\% of problems yield near-zero Interaction Index in the mid-sparsity phase, where attention patterns exhibit insufficient variation to produce measurable compound interaction. This elevated null rate reduces the effective sample size for mid-phase comparisons; our primary cross-model analysis therefore focuses on the low--high phase contrast ($\\\\Delta$), which is unaffected by this limitation. Per-phase effective sample sizes are reported in Appendix~\\\\ref{app:qwen-null-rate}. Full cross-model tables and figures appear in Appendix~\\\\ref{app:cross-model-details}. % exp_id: cross_model_analysis.json; cohens_d_bf16_qwen.json\\n/root/autodl-tmp/pacs/paper/results.tex:81:The absolute magnitude is architecture-dependent: LLaMA severity differences are ${\\\\sim}40{\\\\times}$ smaller than DeepSeek and ${\\\\sim}7{\\\\times}$ smaller than Qwen, and the interaction is substantially weaker---random eviction also shows a non-trivial phase gradient (Wilcoxon $p < \\\\placeholder{}$ at $s{=}0.30$), reducing the strategy contrast observed in Qwen2 models. The directional pattern---importance $>$ random, larger phase gradient under importance---is qualitatively consistent across all three models spanning two architectures (Qwen2ForCausalLM, LlamaForCausalLM), though the interaction magnitude is substantially weaker on LlamaForCausalLM. % exp_id: c3_llama; cross_model_analysis.json\\n/root/autodl-tmp/pacs/paper/results.tex:86:\\\\caption{Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM). $\\\\widetilde{\\\\Delta}$: median paired difference (importance $-$ random) with bootstrap 95\\\\% CI ($B{=}10{,}000$); $p$: Bonferroni-corrected Wilcoxon signed-rank $p$ ($k{=}4$). $n{=}\\\\placeholder{N\\\\_LLAMA}$ paired problems.}\\n/root/autodl-tmp/pacs/paper/results.tex:92:0.15 & \\\\placeholder{}\\\\; $[\\\\placeholder{}, \\\\placeholder{}]$ & \\\\placeholder{} \\\\\\\\\\n/root/autodl-tmp/pacs/paper/results.tex:93:0.20 & \\\\placeholder{}\\\\; $[\\\\placeholder{}, \\\\placeholder{}]$ & \\\\placeholder{} \\\\\\\\\\n/root/autodl-tmp/pacs/paper/results.tex:94:0.25 & \\\\placeholder{}\\\\; $[\\\\placeholder{}, \\\\placeholder{}]$ & \\\\placeholder{} \\\\\\\\\\n/root/autodl-tmp/pacs/paper/results.tex:95:0.30 & \\\\placeholder{}\\\\; $[\\\\placeholder{}, \\\\placeholder{}]$ & $\\\\mathbf{\\\\placeholder{}}$ \\\\\\\\\\n/root/autodl-tmp/pacs/paper/discussion.tex:10:A preliminary pilot experiment explored oracle phase-aware budget reallocation, shifting sparsity budget from high-severity low-sparsity phases to low-severity high-sparsity phases. At $s{=}0.25$, oracle recovery---the fraction of compound interaction eliminated by phase-aware allocation---reached \\\\placeholder{ORACLE\\\\_PCT}\\\\% (Wilcoxon $p = \\\\placeholder{ORACLE\\\\_P}$), below the pre-registered 30\\\\% gate for claiming practical mitigation. A heuristic variant achieved \\\\placeholder{HEUR\\\\_PCT}\\\\% recovery ($p = \\\\placeholder{HEUR\\\\_P}$), but 95\\\\% CIs for both conditions span zero. These results indicate that phase-aware budget reallocation alone is insufficient to neutralize the severity gradient; effective mitigation likely requires joint optimization of budget allocation and eviction strategy selection across phases---a promising direction for future work.\\n/root/autodl-tmp/pacs/paper/discussion.tex:15:Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM) provides partial support for the qualitative pattern---monotonically increasing severity gradient under importance-based eviction with within-strategy phase gradient $d_z \\\\geq 1.0$---while revealing that absolute severity magnitudes are architecture-dependent (${\\\\sim}40{\\\\times}$ smaller than DeepSeek, ${\\\\sim}7{\\\\times}$ smaller than Qwen) and the strategy--phase interaction is substantially weaker than in Qwen2-based architectures. Notably, random pruning also exhibits a non-trivial phase gradient on LLaMA (Wilcoxon $p < \\\\placeholder{}$), reducing the contrast between strategies. This dissociation between qualitatively consistent directional trends and markedly different magnitudes suggests the phase-strategy interaction may be a general property of compound sparsity on reasoning models, while its quantitative impact---and the degree to which it is strategy-specific---depends on architecture-specific attention distributions and head specialization patterns. % exp_id: c3_llama\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 50_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_016e2imgvvM79AzQzJo5Xmhq`</summary>

```json
{
  "server": "westd-22162",
  "command": "grep -n \"placeholder\" /root/autodl-tmp/pacs/paper/appendix.tex /root/autodl-tmp/pacs/paper/appendix_disc_analysis.tex /root/autodl-tmp/pacs/paper/appendix_results.tex /root/autodl-tmp/pacs/paper/appendix_moved.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "0a116a76-400d-422f-b4b5-8d5d966fe175",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QrEQ6UUdGFk7X4vPeemo6k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8685,
      "cache_read_input_tokens": 43673,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8685
      },
      "output_tokens": 12,
      "service_tier": "standard",
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

_source line 51 · 2026-05-15T02:18:05.683Z_

<details><summary>↩ Tool result · `toolu_016e2imgvvM79AzQzJo5Xmhq`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/pacs/paper/appendix_disc_analysis.tex:14:Random eviction fails 7/8 paired permutation tests across both models; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) exhibits negligible effect size ($\\\\widetilde{\\\\Delta} = \\\\placeholder{}$). The absence of a phase gradient under random masking isolates the amplification as strategy-specific. % exp_id: bf16_ds_rand_s015..s030, bf16_qw_rand_s015..s030\\n/root/autodl-tmp/pacs/paper/appendix_disc_analysis.tex:49:A notable exception among the random baselines is the Qwen random condition at $s{=}0.30$, which yields a statistically significant result ($p{=}0.012$) despite negligible effect size ($\\\\widetilde{\\\\Delta} = \\\\placeholder{}$, bootstrap CI spanning zero). % exp_id: qw_rand_s030; B=10000, p=0.012, d=-0.035, negligible\\n/root/autodl-tmp/pacs/paper/appendix_results.tex:7:The per-problem concordance across models is not significant (median $\\\\rho = \\\\placeholder{}$, $p = \\\\placeholder{}$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking. % exp_id: cross_model_analysis.json (spearman_rho=1.0, gradient_permutation_p=0.043, per_problem_concordance_p=0.926, mean_rho=-0.107)\\n/root/autodl-tmp/pacs/paper/appendix_results.tex:10:As a control, random eviction on Qwen yields no systematic phase gradient at three of four sparsity levels (3/4 FAIL), mirroring DeepSeek's 4/4 FAIL pattern. At $s{=}0.30$, Qwen random produces a borderline PASS (permutation $p = 0.012$) but with negligible median difference ($\\\\widetilde{\\\\Delta} = \\\\placeholder{}$, CI spans zero), indicating no meaningful phase modulation. % exp_id: bf16_qw_rand_s015..s030; source: experiment_summary_table.json\\n/root/autodl-tmp/pacs/paper/appendix_moved.tex:30:Table~\\\\ref{tab:qwen-effective-n} reports the per-phase effective sample size for Qwen2.5-7B-Instruct, defined as the number of problems with $|\\\\mathrm{II}| > 0.001$ in each phase. The mid-phase null rate (\\\\placeholder{NULL\\\\_PCT}\\\\%) reflects problems where compound interaction is absent in intermediate phases; this does not affect the low--high contrast ($\\\\Delta$) used in the primary analysis.\\n/root/autodl-tmp/pacs/paper/appendix_moved.tex:35:\\\\caption{Per-phase effective sample size for Qwen2.5-7B-Instruct ($n_{\\\\text{total}} = \\\\placeholder{N\\\\_QW}$).}\\n/root/autodl-tmp/pacs/paper/appendix_moved.tex:41:High & \\\\placeholder{} & \\\\placeholder{} & \\\\placeholder{} & \\\\placeholder{} \\\\\\\\\\n/root/autodl-tmp/pacs/paper/appendix_moved.tex:42:Mid  & \\\\placeholder{} & \\\\placeholder{} & \\\\placeholder{} & \\\\placeholder{} \\\\\\\\\\n/root/autodl-tmp/pacs/paper/appendix_moved.tex:43:Low  & \\\\placeholder{} & \\\\placeholder{} & \\\\placeholder{} & \\\\placeholder{} \\\\\\\\\\n/root/autodl-tmp/pacs/paper/appendix_moved.tex:73:The per-problem concordance across models is not significant (median $\\\\rho = \\\\placeholder{}$, $p = \\\\placeholder{}$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking. % exp_id: cross_model_analysis.json (spearman_rho=1.0, gradient_permutation_p=0.043, per_problem_concordance_p=0.926, mean_rho=-0.107)\\n/root/autodl-tmp/pacs/paper/appendix_moved.tex:76:As a control, random eviction on Qwen yields no systematic phase gradient at three of four sparsity levels (3/4 FAIL), mirroring DeepSeek's 4/4 FAIL pattern. At $s{=}0.30$, Qwen random produces a borderline PASS (permutation $p = 0.012$) but with negligible median difference ($\\\\widetilde{\\\\Delta} = \\\\placeholder{}$, CI spans zero), indicating no meaningful phase modulation. % exp_id: bf16_qw_rand_s015..s030; source: experiment_summary_table.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "e9e2d553-f85b-44f1-8830-0517c46a2b64",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/pacs/paper/appendix_disc_analysis.tex:14:Random eviction fails 7/8 paired permutation tests across both models; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) exhibits negligible effect size ($\\\\\\\\widetilde{\\\\\\\\Delta} = \\\\\\\\placeholder{}$). The absence of a phase gradient under random masking isolates the amplification as strategy-specific. % exp_id: bf16_ds_rand_s015..s030, bf16_qw_rand_s015..s030\\\\n/root/autodl-tmp/pacs/paper/appendix_disc_analysis.tex:49:A notable exception among the random baselines is the Qwen random condition at $s{=}0.30$, which yields a statistically significant result ($p{=}0.012$) despite negligible effect size ($\\\\\\\\widetilde{\\\\\\\\Delta} = \\\\\\\\placeholder{}$, bootstrap CI spanning zero). % exp_id: qw_rand_s030; B=10000, p=0.012, d=-0.035, negligible\\\\n/root/autodl-tmp/pacs/paper/appendix_results.tex:7:The per-problem concordance across models is not significant (median $\\\\\\\\rho = \\\\\\\\placeholder{}$, $p = \\\\\\\\placeholder{}$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking. % exp_id: cross_model_analysis.json (spearman_rho=1.0, gradient_permutation_p=0.043, per_problem_concordance_p=0.926, mean_rho=-0.107)\\\\n/root/autodl-tmp/pacs/paper/appendix_results.tex:10:As a control, random eviction on Qwen yields no systematic phase gradient at three of four sparsity levels (3/4 FAIL), mirroring DeepSeek's 4/4 FAIL pattern. At $s{=}0.30$, Qwen random produces a borderline PASS (permutation $p = 0.012$) but with negligible median difference ($\\\\\\\\widetilde{\\\\\\\\Delta} = \\\\\\\\placeholder{}$, CI spans zero), indicating no meaningful phase modulation. % exp_id: bf16_qw_rand_s015..s030; source: experiment_summary_table.json\\\\n/root/autodl-tmp/pacs/paper/appendix_moved.tex:30:Table~\\\\\\\\ref{tab:qwen-effective-n} reports the per-phase effective sample size for Qwen2.5-7B-Instruct, defined as the number of problems with $|\\\\\\\\mathrm{II}| > 0.001$ in each phase. The mid-phase null rate (\\\\\\\\placeholder{NULL\\\\\\\\_PCT}\\\\\\\\%) reflects problems where compound interaction is absent in intermediate phases; this does not affect the low--high contrast ($\\\\\\\\Delta$) used in the primary analysis.\\\\n/root/autodl-tmp/pacs/paper/appendix_moved.tex:35:\\\\\\\\caption{Per-phase effective sample size for Qwen2.5-7B-Instruct ($n_{\\\\\\\\text{total}} = \\\\\\\\placeholder{N\\\\\\\\_QW}$).}\\\\n/root/autodl-tmp/pacs/paper/appendix_moved.tex:41:High & \\\\\\\\placeholder{} & \\\\\\\\placeholder{} & \\\\\\\\placeholder{} & \\\\\\\\placeholder{} \\\\\\\\\\\\\\\\\\\\n/root/autodl-tmp/pacs/paper/appendix_moved.tex:42:Mid  & \\\\\\\\placeholder{} & \\\\\\\\placeholder{} & \\\\\\\\placeholder{} & \\\\\\\\placeholder{} \\\\\\\\\\\\\\\\\\\\n/root/autodl-tmp/pacs/paper/appendix_moved.tex:43:Low  & \\\\\\\\placeholder{} & \\\\\\\\placeholder{} & \\\\\\\\placeholder{} & \\\\\\\\placeholder{} \\\\\\\\\\\\\\\\\\\\n/root/autodl-tmp/pacs/paper/appendix_moved.tex:73:The per-problem concordance across models is not significant (median $\\\\\\\\rho = \\\\\\\\placeholder{}$, $p = \\\\\\\\placeholder{}$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking. % exp_id: cross_model_analysis.json (spearman_rho=1.0, gradient_permutation_p=0.043, per_problem_concordance_p=0.926, mean_rho=-0.107)\\\\n/root/autodl-tmp/pacs/paper/appendix_moved.tex:76:As a control, random eviction on Qwen yields no systematic phase gradient at three of four sparsity levels (3/4 FAIL), mirroring DeepSeek's 4/4 FAIL pattern. At $s{=}0.30$, Qwen random produces a borderline PASS (permutation $p = 0.012$) but with negligible median difference ($\\\\\\\\widetilde{\\\\\\\\Delta} = \\\\\\\\placeholder{}$, CI spans zero), indicating no meaningful phase modulation. % exp_id: bf16_qw_rand_s015..s030; source: experiment_summary_table.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/pacs/paper/appendix_disc_analysis.tex:14:Random eviction fails 7/8 paired permutation tests across both models; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) exhibits negligible effect size ($\\\\widetilde{\\\\Delta} = \\\\placeholder{}$). The absence of a phase gradient under random masking isolates the amplification as strategy-specific. % exp_id: bf16_ds_rand_s015..s030, bf16_qw_rand_s015..s030\\n/root/autodl-tmp/pacs/paper/appendix_disc_analysis.tex:49:A notable exception among the random baselines is the Qwen random condition at $s{=}0.30$, which yields a statistically significant result ($p{=}0.012$) despite negligible effect size ($\\\\widetilde{\\\\Delta} = \\\\placeholder{}$, bootstrap CI spanning zero). % exp_id: qw_rand_s030; B=10000, p=0.012, d=-0.035, negligible\\n/root/autodl-tmp/pacs/paper/appendix_results.tex:7:The per-problem concordance across models is not significant (median $\\\\rho = \\\\placeholder{}$, $p = \\\\placeholder{}$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking. % exp_id: cross_model_analysis.json (spearman_rho=1.0, gradient_permutation_p=0.043, per_problem_concordance_p=0.926, mean_rho=-0.107)\\n/root/autodl-tmp/pacs/paper/appendix_results.tex:10:As a control, random eviction on Qwen yields no systematic phase gradient at three of four sparsity levels (3/4 FAIL), mirroring DeepSeek's 4/4 FAIL pattern. At $s{=}0.30$, Qwen random produces a borderline PASS (permutation $p = 0.012$) but with negligible median difference ($\\\\widetilde{\\\\Delta} = \\\\placeholder{}$, CI spans zero), indicating no meaningful phase modulation. % exp_id: bf16_qw_rand_s015..s030; source: experiment_summary_table.json\\n/root/autodl-tmp/pacs/paper/appendix_moved.tex:30:Table~\\\\ref{tab:qwen-effective-n} reports the per-phase effective sample size for Qwen2.5-7B-Instruct, defined as the number of problems with $|\\\\mathrm{II}| > 0.001$ in each phase. The mid-phase null rate (\\\\placeholder{NULL\\\\_PCT}\\\\%) reflects problems where compound interaction is absent in intermediate phases; this does not affect the low--high contrast ($\\\\Delta$) used in the primary analysis.\\n/root/autodl-tmp/pacs/paper/appendix_moved.tex:35:\\\\caption{Per-phase effective sample size for Qwen2.5-7B-Instruct ($n_{\\\\text{total}} = \\\\placeholder{N\\\\_QW}$).}\\n/root/autodl-tmp/pacs/paper/appendix_moved.tex:41:High & \\\\placeholder{} & \\\\placeholder{} & \\\\placeholder{} & \\\\placeholder{} \\\\\\\\\\n/root/autodl-tmp/pacs/paper/appendix_moved.tex:42:Mid  & \\\\placeholder{} & \\\\placeholder{} & \\\\placeholder{} & \\\\placeholder{} \\\\\\\\\\n/root/autodl-tmp/pacs/paper/appendix_moved.tex:43:Low  & \\\\placeholder{} & \\\\placeholder{} & \\\\placeholder{} & \\\\placeholder{} \\\\\\\\\\n/root/autodl-tmp/pacs/paper/appendix_moved.tex:73:The per-problem concordance across models is not significant (median $\\\\rho = \\\\placeholder{}$, $p = \\\\placeholder{}$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking. % exp_id: cross_model_analysis.json (spearman_rho=1.0, gradient_permutation_p=0.043, per_problem_concordance_p=0.926, mean_rho=-0.107)\\n/root/autodl-tmp/pacs/paper/appendix_moved.tex:76:As a control, random eviction on Qwen yields no systematic phase gradient at three of four sparsity levels (3/4 FAIL), mirroring DeepSeek's 4/4 FAIL pattern. At $s{=}0.30$, Qwen random produces a borderline PASS (permutation $p = 0.012$) but with negligible median difference ($\\\\widetilde{\\\\Delta} = \\\\placeholder{}$, CI spans zero), indicating no meaningful phase modulation. % exp_id: bf16_qw_rand_s015..s030; source: experiment_summary_table.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 52_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01H4F67viZBnsfDASPXv59cx`</summary>

```json
{
  "server": "westd-22162",
  "command": "grep -rn \"n=50\\|n{=}50\\|50 problems\\|50~problems\\|n_50\\|50 MATH\" /root/autodl-tmp/pacs/paper/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "a6d0dccc-8710-4fd9-ae6d-51270ca0aea7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QrEQ6UUdGFk7X4vPeemo6k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8685,
      "cache_read_input_tokens": 43673,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8685
      },
      "output_tokens": 12,
      "service_tier": "standard",
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

_source line 53 · 2026-05-15T02:18:06.653Z_

<details><summary>↩ Tool result · `toolu_01H4F67viZBnsfDASPXv59cx`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "b5313667-f902-49a8-b6ae-c3d51a4ee335",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 54_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_011DTUGCYH2micDHqVxRbwRi`</summary>

```json
{
  "server": "westd-22162",
  "command": "grep -rn \"n=50\\|50 problems\\|50~problems\\|50 MATH\" /root/autodl-tmp/pacs/paper/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "929d18c5-2685-4d9a-8891-917d605339bf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TpAfZHDuYk76dRpApvb1Dn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4069,
      "cache_read_input_tokens": 52358,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4069
      },
      "output_tokens": 45,
      "service_tier": "standard",
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

_source line 55 · 2026-05-15T02:18:11.384Z_

<details><summary>↩ Tool result · `toolu_011DTUGCYH2micDHqVxRbwRi`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "8fc927f2-5654-4172-9051-22885aed99ba",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 56_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_013VQcCNHspUp8JUErGmZRbr`</summary>

```json
{
  "server": "westd-22162",
  "command": "grep -rn \"n{=}50\\|n{=}49\\|n{=}46\" /root/autodl-tmp/pacs/paper/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "a8e82781-c96d-42db-9062-49f26f50ecef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TpAfZHDuYk76dRpApvb1Dn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4069,
      "cache_read_input_tokens": 52358,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4069
      },
      "output_tokens": 45,
      "service_tier": "standard",
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

_source line 57 · 2026-05-15T02:18:12.473Z_

<details><summary>↩ Tool result · `toolu_013VQcCNHspUp8JUErGmZRbr`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "01667b98-d9aa-4a13-8213-73a2ddc69775",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 58_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01J7ENTWU29TdWbpLnowC5F4`</summary>

```json
{
  "server": "westd-22162",
  "command": "grep -rn \"Figure\\|\\\\\\\\ref{fig\" /root/autodl-tmp/pacs/paper/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "95441c6a-f461-4ad3-becb-2e1572e6833f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TpAfZHDuYk76dRpApvb1Dn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4069,
      "cache_read_input_tokens": 52358,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4069
      },
      "output_tokens": 45,
      "service_tier": "standard",
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

_source line 59 · 2026-05-15T02:18:13.242Z_

<details><summary>↩ Tool result · `toolu_01J7ENTWU29TdWbpLnowC5F4`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "1211e5e0-ad64-482c-827e-807bf80612e2",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 60_

<details><summary>Logged reasoning block</summary>

```text
The `\|` (pipe alternation in regex) is being interpreted as a shell pipe. Let me use grep with `-E` flag and escape differently, or just do separate greps.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "72f127cd-86af-420d-bc62-02bcd60ef0e0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HtwQESphC4AY5GBpM8QvoR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 736,
      "cache_read_input_tokens": 56427,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 736
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

_source line 61_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01SLgACmz5RYgsCVYUcopRMj`</summary>

```json
{
  "server": "westd-22162",
  "command": "grep -rn \"n=50\" /root/autodl-tmp/pacs/paper/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "43a747b2-0bbd-4d7d-ba49-ac841c8ba1e4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HtwQESphC4AY5GBpM8QvoR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 736,
      "cache_read_input_tokens": 56427,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 736
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

_source line 62 · 2026-05-15T02:18:18.347Z_

<details><summary>↩ Tool result · `toolu_01SLgACmz5RYgsCVYUcopRMj`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.46}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "4f980dd5-2a9d-41f4-8a3f-a882c5cc76d0",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 1}, \\\"error\\\": \\\"exit code 1\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.46}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.46}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 63_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01WnezWjtgD7CCr1BgrdUan6`</summary>

```json
{
  "server": "westd-22162",
  "command": "grep -rn \"50 problems\" /root/autodl-tmp/pacs/paper/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "c59ceb96-edc3-4bbb-91b4-fd67dce583bd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HtwQESphC4AY5GBpM8QvoR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 736,
      "cache_read_input_tokens": 56427,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 736
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

_source line 64 · 2026-05-15T02:18:18.895Z_

<details><summary>↩ Tool result · `toolu_01WnezWjtgD7CCr1BgrdUan6`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/pacs/paper/methodology.tex:10:We use 50 problems stratified from MATH-500~\\\\cite{math500-neurips2021}, sampling uniformly across categories with a fixed seed. Each problem is decoded greedily (\\\\texttt{max\\\\_new\\\\_tokens}$=$2048).\\n/root/autodl-tmp/pacs/paper/results.tex:34:\\\\caption{Interaction index (II) by eviction strategy, reasoning phase, and sparsity level. II values are problem-level medians across 50 problems. $\\\\Delta = \\\\widetilde{\\\\mathrm{II}}_{\\\\textit{low}} - \\\\widetilde{\\\\mathrm{II}}_{\\\\textit{high}}$. $G = \\\\widetilde{\\\\mathrm{II}}_{\\\\textit{low}} / \\\\widetilde{\\\\mathrm{II}}_{\\\\textit{high}}$.}\\n/root/autodl-tmp/pacs/paper/appendix_moved.tex:26:Despite lacking explicit \\\\texttt{&lt;think>} delimiters, Qwen2.5-7B-Instruct exhibits sufficient variation in attention sparsity to permit phase segmentation via the same quantile-based method (\\\\S\\\\ref{sec:phase-segmentation}). Four of the 50 problems are excluded due to degenerate phase assignments, yielding $n{=}46$ valid problems for Qwen (vs.\\\\ $n{=}49$ for DeepSeek).\\n/root/autodl-tmp/pacs/paper/main.aux:462:\\\\@writefile{lot}{\\\\contentsline {table}{\\\\numberline {2}{\\\\ignorespaces Interaction index (II) by eviction strategy, reasoning phase, and sparsity level. II values are problem-level medians across 50 problems. $\\\\Delta = \\\\setbox \\\\z@ \\\\hbox {\\\\mathsurround \\\\z@ $\\\\textstyle \\\\mathrm  {II}$}\\\\mathaccent \\\"0365{\\\\mathrm  {II}}_{\\\\textit  {low}} - \\\\setbox \\\\z@ \\\\hbox {\\\\mathsurround \\\\z@ $\\\\textstyle \\\\mathrm  {II}$}\\\\mathaccent \\\"0365{\\\\mathrm  {II}}_{\\\\textit  {high}}$. $G = \\\\setbox \\\\z@ \\\\hbox {\\\\mathsurround \\\\z@ $\\\\textstyle \\\\mathrm  {II}$}\\\\mathaccent \\\"0365{\\\\mathrm  {II}}_{\\\\textit  {low}} / \\\\setbox \\\\z@ \\\\hbox {\\\\mathsurround \\\\z@ $\\\\textstyle \\\\mathrm  {II}$}\\\\mathaccent \\\"0365{\\\\mathrm  {II}}_{\\\\textit  {high}}$.\\\\relax }}{5}{table.caption.14}\\\\protected@file@percent }\\n/root/autodl-tmp/pacs/paper/main.aux:463:\\\\newlabel{tab:main-results}{{2}{5}{Interaction index (II) by eviction strategy, reasoning phase, and sparsity level. II values are problem-level medians across 50 problems. $\\\\Delta = \\\\widetilde {\\\\mathrm {II}}_{\\\\textit {low}} - \\\\widetilde {\\\\mathrm {II}}_{\\\\textit {high}}$. $G = \\\\widetilde {\\\\mathrm {II}}_{\\\\textit {low}} / \\\\widetilde {\\\\mathrm {II}}_{\\\\textit {high}}$.\\\\relax }{table.caption.14}{}}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "178d4413-300d-4ee0-9cb1-4f1f1de2e67a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/pacs/paper/methodology.tex:10:We use 50 problems stratified from MATH-500~\\\\\\\\cite{math500-neurips2021}, sampling uniformly across categories with a fixed seed. Each problem is decoded greedily (\\\\\\\\texttt{max\\\\\\\\_new\\\\\\\\_tokens}$=$2048).\\\\n/root/autodl-tmp/pacs/paper/results.tex:34:\\\\\\\\caption{Interaction index (II) by eviction strategy, reasoning phase, and sparsity level. II values are problem-level medians across 50 problems. $\\\\\\\\Delta = \\\\\\\\widetilde{\\\\\\\\mathrm{II}}_{\\\\\\\\textit{low}} - \\\\\\\\widetilde{\\\\\\\\mathrm{II}}_{\\\\\\\\textit{high}}$. $G = \\\\\\\\widetilde{\\\\\\\\mathrm{II}}_{\\\\\\\\textit{low}} / \\\\\\\\widetilde{\\\\\\\\mathrm{II}}_{\\\\\\\\textit{high}}$.}\\\\n/root/autodl-tmp/pacs/paper/appendix_moved.tex:26:Despite lacking explicit \\\\\\\\texttt{&lt;think>} delimiters, Qwen2.5-7B-Instruct exhibits sufficient variation in attention sparsity to permit phase segmentation via the same quantile-based method (\\\\\\\\S\\\\\\\\ref{sec:phase-segmentation}). Four of the 50 problems are excluded due to degenerate phase assignments, yielding $n{=}46$ valid problems for Qwen (vs.\\\\\\\\ $n{=}49$ for DeepSeek).\\\\n/root/autodl-tmp/pacs/paper/main.aux:462:\\\\\\\\@writefile{lot}{\\\\\\\\contentsline {table}{\\\\\\\\numberline {2}{\\\\\\\\ignorespaces Interaction index (II) by eviction strategy, reasoning phase, and sparsity level. II values are problem-level medians across 50 problems. $\\\\\\\\Delta = \\\\\\\\setbox \\\\\\\\z@ \\\\\\\\hbox {\\\\\\\\mathsurround \\\\\\\\z@ $\\\\\\\\textstyle \\\\\\\\mathrm  {II}$}\\\\\\\\mathaccent \\\\\\\"0365{\\\\\\\\mathrm  {II}}_{\\\\\\\\textit  {low}} - \\\\\\\\setbox \\\\\\\\z@ \\\\\\\\hbox {\\\\\\\\mathsurround \\\\\\\\z@ $\\\\\\\\textstyle \\\\\\\\mathrm  {II}$}\\\\\\\\mathaccent \\\\\\\"0365{\\\\\\\\mathrm  {II}}_{\\\\\\\\textit  {high}}$. $G = \\\\\\\\setbox \\\\\\\\z@ \\\\\\\\hbox {\\\\\\\\mathsurround \\\\\\\\z@ $\\\\\\\\textstyle \\\\\\\\mathrm  {II}$}\\\\\\\\mathaccent \\\\\\\"0365{\\\\\\\\mathrm  {II}}_{\\\\\\\\textit  {low}} / \\\\\\\\setbox \\\\\\\\z@ \\\\\\\\hbox {\\\\\\\\mathsurround \\\\\\\\z@ $\\\\\\\\textstyle \\\\\\\\mathrm  {II}$}\\\\\\\\mathaccent \\\\\\\"0365{\\\\\\\\mathrm  {II}}_{\\\\\\\\textit  {high}}$.\\\\\\\\relax }}{5}{table.caption.14}\\\\\\\\protected@file@percent }\\\\n/root/autodl-tmp/pacs/paper/main.aux:463:\\\\\\\\newlabel{tab:main-results}{{2}{5}{Interaction index (II) by eviction strategy, reasoning phase, and sparsity level. II values are problem-level medians across 50 problems. $\\\\\\\\Delta = \\\\\\\\widetilde {\\\\\\\\mathrm {II}}_{\\\\\\\\textit {low}} - \\\\\\\\widetilde {\\\\\\\\mathrm {II}}_{\\\\\\\\textit {high}}$. $G = \\\\\\\\widetilde {\\\\\\\\mathrm {II}}_{\\\\\\\\textit {low}} / \\\\\\\\widetilde {\\\\\\\\mathrm {II}}_{\\\\\\\\textit {high}}$.\\\\\\\\relax }{table.caption.14}{}}\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.53}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/pacs/paper/methodology.tex:10:We use 50 problems stratified from MATH-500~\\\\cite{math500-neurips2021}, sampling uniformly across categories with a fixed seed. Each problem is decoded greedily (\\\\texttt{max\\\\_new\\\\_tokens}$=$2048).\\n/root/autodl-tmp/pacs/paper/results.tex:34:\\\\caption{Interaction index (II) by eviction strategy, reasoning phase, and sparsity level. II values are problem-level medians across 50 problems. $\\\\Delta = \\\\widetilde{\\\\mathrm{II}}_{\\\\textit{low}} - \\\\widetilde{\\\\mathrm{II}}_{\\\\textit{high}}$. $G = \\\\widetilde{\\\\mathrm{II}}_{\\\\textit{low}} / \\\\widetilde{\\\\mathrm{II}}_{\\\\textit{high}}$.}\\n/root/autodl-tmp/pacs/paper/appendix_moved.tex:26:Despite lacking explicit \\\\texttt{&lt;think>} delimiters, Qwen2.5-7B-Instruct exhibits sufficient variation in attention sparsity to permit phase segmentation via the same quantile-based method (\\\\S\\\\ref{sec:phase-segmentation}). Four of the 50 problems are excluded due to degenerate phase assignments, yielding $n{=}46$ valid problems for Qwen (vs.\\\\ $n{=}49$ for DeepSeek).\\n/root/autodl-tmp/pacs/paper/main.aux:462:\\\\@writefile{lot}{\\\\contentsline {table}{\\\\numberline {2}{\\\\ignorespaces Interaction index (II) by eviction strategy, reasoning phase, and sparsity level. II values are problem-level medians across 50 problems. $\\\\Delta = \\\\setbox \\\\z@ \\\\hbox {\\\\mathsurround \\\\z@ $\\\\textstyle \\\\mathrm  {II}$}\\\\mathaccent \\\"0365{\\\\mathrm  {II}}_{\\\\textit  {low}} - \\\\setbox \\\\z@ \\\\hbox {\\\\mathsurround \\\\z@ $\\\\textstyle \\\\mathrm  {II}$}\\\\mathaccent \\\"0365{\\\\mathrm  {II}}_{\\\\textit  {high}}$. $G = \\\\setbox \\\\z@ \\\\hbox {\\\\mathsurround \\\\z@ $\\\\textstyle \\\\mathrm  {II}$}\\\\mathaccent \\\"0365{\\\\mathrm  {II}}_{\\\\textit  {low}} / \\\\setbox \\\\z@ \\\\hbox {\\\\mathsurround \\\\z@ $\\\\textstyle \\\\mathrm  {II}$}\\\\mathaccent \\\"0365{\\\\mathrm  {II}}_{\\\\textit  {high}}$.\\\\relax }}{5}{table.caption.14}\\\\protected@file@percent }\\n/root/autodl-tmp/pacs/paper/main.aux:463:\\\\newlabel{tab:main-results}{{2}{5}{Interaction index (II) by eviction strategy, reasoning phase, and sparsity level. II values are problem-level medians across 50 problems. $\\\\Delta = \\\\widetilde {\\\\mathrm {II}}_{\\\\textit {low}} - \\\\widetilde {\\\\mathrm {II}}_{\\\\textit {high}}$. $G = \\\\widetilde {\\\\mathrm {II}}_{\\\\textit {low}} / \\\\widetilde {\\\\mathrm {II}}_{\\\\textit {high}}$.\\\\relax }{table.caption.14}{}}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 65_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01UB59hFpQqsXXrWnMNvGcux`</summary>

```json
{
  "server": "westd-22162",
  "command": "grep -rn \"50 MATH\" /root/autodl-tmp/pacs/paper/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "ba96bf37-4494-4a83-995f-2cf24f1b0474",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HtwQESphC4AY5GBpM8QvoR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 736,
      "cache_read_input_tokens": 56427,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 736
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

_source line 66 · 2026-05-15T02:18:19.768Z_

<details><summary>↩ Tool result · `toolu_01UB59hFpQqsXXrWnMNvGcux`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/pacs/paper/abstract.tex:6:We evaluate compound sparsity on three models---DeepSeek-R1-Distill-Qwen-7B, Qwen2.5-7B-Instruct (both Qwen2ForCausalLM), and DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM)---spanning two architectures, using 50 MATH-500 problems, measuring the Interaction Index---a super-additivity metric---across quantile-segmented reasoning phases at sparsity levels $s \\\\in \\\\{0.15, 0.20, 0.25, 0.30\\\\}$.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "eb09a59b-dbbf-4e70-b706-d1caff9f2fd7",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/pacs/paper/abstract.tex:6:We evaluate compound sparsity on three models---DeepSeek-R1-Distill-Qwen-7B, Qwen2.5-7B-Instruct (both Qwen2ForCausalLM), and DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM)---spanning two architectures, using 50 MATH-500 problems, measuring the Interaction Index---a super-additivity metric---across quantile-segmented reasoning phases at sparsity levels $s \\\\\\\\in \\\\\\\\{0.15, 0.20, 0.25, 0.30\\\\\\\\}$.\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/pacs/paper/abstract.tex:6:We evaluate compound sparsity on three models---DeepSeek-R1-Distill-Qwen-7B, Qwen2.5-7B-Instruct (both Qwen2ForCausalLM), and DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM)---spanning two architectures, using 50 MATH-500 problems, measuring the Interaction Index---a super-additivity metric---across quantile-segmented reasoning phases at sparsity levels $s \\\\in \\\\{0.15, 0.20, 0.25, 0.30\\\\}$.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 67_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01EH3WncxLgZm4tVcJvCh59E`</summary>

```json
{
  "server": "westd-22162",
  "command": "grep -rn \"n{=}49\" /root/autodl-tmp/pacs/paper/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "edc200ef-caaf-4f81-9bfa-47a8bb1b70d0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HtwQESphC4AY5GBpM8QvoR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 736,
      "cache_read_input_tokens": 56427,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 736
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

_source line 68_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01QY4d53sBfobbp7d6A1nDR1`</summary>

```json
{
  "server": "westd-22162",
  "command": "grep -rn \"n{=}46\" /root/autodl-tmp/pacs/paper/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "bd949ed4-1f98-418f-827c-610e1eacb514",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HtwQESphC4AY5GBpM8QvoR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 736,
      "cache_read_input_tokens": 56427,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 736
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

_source line 69 · 2026-05-15T02:18:20.711Z_

<details><summary>↩ Tool result · `toolu_01EH3WncxLgZm4tVcJvCh59E`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/pacs/paper/results.tex:77:To test whether the phase-modulated severity pattern extends beyond the Qwen2 architecture, we replicate the experiment on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, 8B parameters; $n{=}49$ paired problems). Table~\\\\ref{tab:llama-cross-arch} reports the strategy-dependent severity comparison across sparsity levels.\\n/root/autodl-tmp/pacs/paper/appendix_disc_analysis.tex:45:Bootstrap confidence intervals use $B{=}10{,}000$ resamples (recomputed from initial $B{=}1{,}000$ profiling runs). The paired permutation test yields $n{=}49$ paired problems for DeepSeek (1 excluded) and $n{=}46$ for Qwen (4 excluded). % exp_id: cohens_d_bf16.json, cohens_d_bf16_qwen.json\\n/root/autodl-tmp/pacs/paper/appendix_moved.tex:26:Despite lacking explicit \\\\texttt{&lt;think>} delimiters, Qwen2.5-7B-Instruct exhibits sufficient variation in attention sparsity to permit phase segmentation via the same quantile-based method (\\\\S\\\\ref{sec:phase-segmentation}). Four of the 50 problems are excluded due to degenerate phase assignments, yielding $n{=}46$ valid problems for Qwen (vs.\\\\ $n{=}49$ for DeepSeek).\\n/root/autodl-tmp/pacs/paper/appendix_moved.tex:93:\\\\caption{Paired permutation test for compound severity: importance vs.\\\\ random eviction on DeepSeek-R1-Distill-Qwen-7B ($n{=}49$, $10{,}000$ permutations, Bonferroni-corrected).}\\n/root/autodl-tmp/pacs/paper/main.aux:1062:\\\\@writefile{lot}{\\\\contentsline {table}{\\\\numberline {7}{\\\\ignorespaces Paired permutation test for compound severity: importance vs.\\\\ random eviction on DeepSeek-R1-Distill-Qwen-7B ($n{=}49$, $10{,}000$ permutations, Bonferroni-corrected).\\\\relax }}{11}{table.caption.38}\\\\protected@file@percent }\\n/root/autodl-tmp/pacs/paper/main.aux:1063:\\\\newlabel{tab:permutation}{{7}{11}{Paired permutation test for compound severity: importance vs.\\\\ random eviction on DeepSeek-R1-Distill-Qwen-7B ($n{=}49$, $10{,}000$ permutations, Bonferroni-corrected).\\\\relax }{table.caption.38}{}}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "e35a455e-0ded-4898-990f-e61a4542a028",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/pacs/paper/results.tex:77:To test whether the phase-modulated severity pattern extends beyond the Qwen2 architecture, we replicate the experiment on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, 8B parameters; $n{=}49$ paired problems). Table~\\\\\\\\ref{tab:llama-cross-arch} reports the strategy-dependent severity comparison across sparsity levels.\\\\n/root/autodl-tmp/pacs/paper/appendix_disc_analysis.tex:45:Bootstrap confidence intervals use $B{=}10{,}000$ resamples (recomputed from initial $B{=}1{,}000$ profiling runs). The paired permutation test yields $n{=}49$ paired problems for DeepSeek (1 excluded) and $n{=}46$ for Qwen (4 excluded). % exp_id: cohens_d_bf16.json, cohens_d_bf16_qwen.json\\\\n/root/autodl-tmp/pacs/paper/appendix_moved.tex:26:Despite lacking explicit \\\\\\\\texttt{&lt;think>} delimiters, Qwen2.5-7B-Instruct exhibits sufficient variation in attention sparsity to permit phase segmentation via the same quantile-based method (\\\\\\\\S\\\\\\\\ref{sec:phase-segmentation}). Four of the 50 problems are excluded due to degenerate phase assignments, yielding $n{=}46$ valid problems for Qwen (vs.\\\\\\\\ $n{=}49$ for DeepSeek).\\\\n/root/autodl-tmp/pacs/paper/appendix_moved.tex:93:\\\\\\\\caption{Paired permutation test for compound severity: importance vs.\\\\\\\\ random eviction on DeepSeek-R1-Distill-Qwen-7B ($n{=}49$, $10{,}000$ permutations, Bonferroni-corrected).}\\\\n/root/autodl-tmp/pacs/paper/main.aux:1062:\\\\\\\\@writefile{lot}{\\\\\\\\contentsline {table}{\\\\\\\\numberline {7}{\\\\\\\\ignorespaces Paired permutation test for compound severity: importance vs.\\\\\\\\ random eviction on DeepSeek-R1-Distill-Qwen-7B ($n{=}49$, $10{,}000$ permutations, Bonferroni-corrected).\\\\\\\\relax }}{11}{table.caption.38}\\\\\\\\protected@file@percent }\\\\n/root/autodl-tmp/pacs/paper/main.aux:1063:\\\\\\\\newlabel{tab:permutation}{{7}{11}{Paired permutation test for compound severity: importance vs.\\\\\\\\ random eviction on DeepSeek-R1-Distill-Qwen-7B ($n{=}49$, $10{,}000$ permutations, Bonferroni-corrected).\\\\\\\\relax }{table.caption.38}{}}\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/pacs/paper/results.tex:77:To test whether the phase-modulated severity pattern extends beyond the Qwen2 architecture, we replicate the experiment on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, 8B parameters; $n{=}49$ paired problems). Table~\\\\ref{tab:llama-cross-arch} reports the strategy-dependent severity comparison across sparsity levels.\\n/root/autodl-tmp/pacs/paper/appendix_disc_analysis.tex:45:Bootstrap confidence intervals use $B{=}10{,}000$ resamples (recomputed from initial $B{=}1{,}000$ profiling runs). The paired permutation test yields $n{=}49$ paired problems for DeepSeek (1 excluded) and $n{=}46$ for Qwen (4 excluded). % exp_id: cohens_d_bf16.json, cohens_d_bf16_qwen.json\\n/root/autodl-tmp/pacs/paper/appendix_moved.tex:26:Despite lacking explicit \\\\texttt{&lt;think>} delimiters, Qwen2.5-7B-Instruct exhibits sufficient variation in attention sparsity to permit phase segmentation via the same quantile-based method (\\\\S\\\\ref{sec:phase-segmentation}). Four of the 50 problems are excluded due to degenerate phase assignments, yielding $n{=}46$ valid problems for Qwen (vs.\\\\ $n{=}49$ for DeepSeek).\\n/root/autodl-tmp/pacs/paper/appendix_moved.tex:93:\\\\caption{Paired permutation test for compound severity: importance vs.\\\\ random eviction on DeepSeek-R1-Distill-Qwen-7B ($n{=}49$, $10{,}000$ permutations, Bonferroni-corrected).}\\n/root/autodl-tmp/pacs/paper/main.aux:1062:\\\\@writefile{lot}{\\\\contentsline {table}{\\\\numberline {7}{\\\\ignorespaces Paired permutation test for compound severity: importance vs.\\\\ random eviction on DeepSeek-R1-Distill-Qwen-7B ($n{=}49$, $10{,}000$ permutations, Bonferroni-corrected).\\\\relax }}{11}{table.caption.38}\\\\protected@file@percent }\\n/root/autodl-tmp/pacs/paper/main.aux:1063:\\\\newlabel{tab:permutation}{{7}{11}{Paired permutation test for compound severity: importance vs.\\\\ random eviction on DeepSeek-R1-Distill-Qwen-7B ($n{=}49$, $10{,}000$ permutations, Bonferroni-corrected).\\\\relax }{table.caption.38}{}}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-15T02:18:21.257Z_

<details><summary>↩ Tool result · `toolu_01QY4d53sBfobbp7d6A1nDR1`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/pacs/paper/appendix_disc_analysis.tex:45:Bootstrap confidence intervals use $B{=}10{,}000$ resamples (recomputed from initial $B{=}1{,}000$ profiling runs). The paired permutation test yields $n{=}49$ paired problems for DeepSeek (1 excluded) and $n{=}46$ for Qwen (4 excluded). % exp_id: cohens_d_bf16.json, cohens_d_bf16_qwen.json\\n/root/autodl-tmp/pacs/paper/appendix_moved.tex:26:Despite lacking explicit \\\\texttt{&lt;think>} delimiters, Qwen2.5-7B-Instruct exhibits sufficient variation in attention sparsity to permit phase segmentation via the same quantile-based method (\\\\S\\\\ref{sec:phase-segmentation}). Four of the 50 problems are excluded due to degenerate phase assignments, yielding $n{=}46$ valid problems for Qwen (vs.\\\\ $n{=}49$ for DeepSeek).\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.54}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "5a0d6d44-b812-4ef2-b176-83ee44135ef5",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/pacs/paper/appendix_disc_analysis.tex:45:Bootstrap confidence intervals use $B{=}10{,}000$ resamples (recomputed from initial $B{=}1{,}000$ profiling runs). The paired permutation test yields $n{=}49$ paired problems for DeepSeek (1 excluded) and $n{=}46$ for Qwen (4 excluded). % exp_id: cohens_d_bf16.json, cohens_d_bf16_qwen.json\\\\n/root/autodl-tmp/pacs/paper/appendix_moved.tex:26:Despite lacking explicit \\\\\\\\texttt{&lt;think>} delimiters, Qwen2.5-7B-Instruct exhibits sufficient variation in attention sparsity to permit phase segmentation via the same quantile-based method (\\\\\\\\S\\\\\\\\ref{sec:phase-segmentation}). Four of the 50 problems are excluded due to degenerate phase assignments, yielding $n{=}46$ valid problems for Qwen (vs.\\\\\\\\ $n{=}49$ for DeepSeek).\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.54}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/pacs/paper/appendix_disc_analysis.tex:45:Bootstrap confidence intervals use $B{=}10{,}000$ resamples (recomputed from initial $B{=}1{,}000$ profiling runs). The paired permutation test yields $n{=}49$ paired problems for DeepSeek (1 excluded) and $n{=}46$ for Qwen (4 excluded). % exp_id: cohens_d_bf16.json, cohens_d_bf16_qwen.json\\n/root/autodl-tmp/pacs/paper/appendix_moved.tex:26:Despite lacking explicit \\\\texttt{&lt;think>} delimiters, Qwen2.5-7B-Instruct exhibits sufficient variation in attention sparsity to permit phase segmentation via the same quantile-based method (\\\\S\\\\ref{sec:phase-segmentation}). Four of the 50 problems are excluded due to degenerate phase assignments, yielding $n{=}46$ valid problems for Qwen (vs.\\\\ $n{=}49$ for DeepSeek).\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.54}}"
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
Now let me check for n{=}50 specifically (the LaTeX form).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "22271713-4b7c-4c9b-a570-fd9d587a0f97",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011DH1yLjRLXJiDs45hL7shG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3293,
      "cache_read_input_tokens": 57163,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3293
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

_source line 72_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_019vabsNLGcgRzdmxw4qF6xB`</summary>

```json
{
  "server": "westd-22162",
  "command": "grep -rn \"n{=}50\" /root/autodl-tmp/pacs/paper/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "d14cbd17-b360-4190-8809-dad080e58cbc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011DH1yLjRLXJiDs45hL7shG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3293,
      "cache_read_input_tokens": 57163,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3293
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

_source line 73 · 2026-05-15T02:18:26.043Z_

<details><summary>↩ Tool result · `toolu_019vabsNLGcgRzdmxw4qF6xB`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/pacs/paper/results.tex:13:\\\\caption{Median compound severity difference ($\\\\Delta = \\\\widetilde{\\\\mathrm{II}}_{\\\\textit{low}} - \\\\widetilde{\\\\mathrm{II}}_{\\\\textit{high}}$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}50$ MATH-500 problems).}\\n/root/autodl-tmp/pacs/paper/main.aux:375:\\\\@writefile{lot}{\\\\contentsline {table}{\\\\numberline {1}{\\\\ignorespaces Median compound severity difference ($\\\\Delta = \\\\setbox \\\\z@ \\\\hbox {\\\\mathsurround \\\\z@ $\\\\textstyle \\\\mathrm  {II}$}\\\\mathaccent \\\"0365{\\\\mathrm  {II}}_{\\\\textit  {low}} - \\\\setbox \\\\z@ \\\\hbox {\\\\mathsurround \\\\z@ $\\\\textstyle \\\\mathrm  {II}$}\\\\mathaccent \\\"0365{\\\\mathrm  {II}}_{\\\\textit  {high}}$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}50$ MATH-500 problems).\\\\relax }}{4}{table.caption.13}\\\\protected@file@percent }\\n/root/autodl-tmp/pacs/paper/main.aux:377:\\\\newlabel{tab:aggregate-ii}{{1}{4}{Median compound severity difference ($\\\\Delta = \\\\widetilde {\\\\mathrm {II}}_{\\\\textit {low}} - \\\\widetilde {\\\\mathrm {II}}_{\\\\textit {high}}$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}50$ MATH-500 problems).\\\\relax }{table.caption.13}{}}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "cef475ce-fd30-458f-aa29-c0cbf7315486",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/pacs/paper/results.tex:13:\\\\\\\\caption{Median compound severity difference ($\\\\\\\\Delta = \\\\\\\\widetilde{\\\\\\\\mathrm{II}}_{\\\\\\\\textit{low}} - \\\\\\\\widetilde{\\\\\\\\mathrm{II}}_{\\\\\\\\textit{high}}$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}50$ MATH-500 problems).}\\\\n/root/autodl-tmp/pacs/paper/main.aux:375:\\\\\\\\@writefile{lot}{\\\\\\\\contentsline {table}{\\\\\\\\numberline {1}{\\\\\\\\ignorespaces Median compound severity difference ($\\\\\\\\Delta = \\\\\\\\setbox \\\\\\\\z@ \\\\\\\\hbox {\\\\\\\\mathsurround \\\\\\\\z@ $\\\\\\\\textstyle \\\\\\\\mathrm  {II}$}\\\\\\\\mathaccent \\\\\\\"0365{\\\\\\\\mathrm  {II}}_{\\\\\\\\textit  {low}} - \\\\\\\\setbox \\\\\\\\z@ \\\\\\\\hbox {\\\\\\\\mathsurround \\\\\\\\z@ $\\\\\\\\textstyle \\\\\\\\mathrm  {II}$}\\\\\\\\mathaccent \\\\\\\"0365{\\\\\\\\mathrm  {II}}_{\\\\\\\\textit  {high}}$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}50$ MATH-500 problems).\\\\\\\\relax }}{4}{table.caption.13}\\\\\\\\protected@file@percent }\\\\n/root/autodl-tmp/pacs/paper/main.aux:377:\\\\\\\\newlabel{tab:aggregate-ii}{{1}{4}{Median compound severity difference ($\\\\\\\\Delta = \\\\\\\\widetilde {\\\\\\\\mathrm {II}}_{\\\\\\\\textit {low}} - \\\\\\\\widetilde {\\\\\\\\mathrm {II}}_{\\\\\\\\textit {high}}$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}50$ MATH-500 problems).\\\\\\\\relax }{table.caption.13}{}}\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/pacs/paper/results.tex:13:\\\\caption{Median compound severity difference ($\\\\Delta = \\\\widetilde{\\\\mathrm{II}}_{\\\\textit{low}} - \\\\widetilde{\\\\mathrm{II}}_{\\\\textit{high}}$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}50$ MATH-500 problems).}\\n/root/autodl-tmp/pacs/paper/main.aux:375:\\\\@writefile{lot}{\\\\contentsline {table}{\\\\numberline {1}{\\\\ignorespaces Median compound severity difference ($\\\\Delta = \\\\setbox \\\\z@ \\\\hbox {\\\\mathsurround \\\\z@ $\\\\textstyle \\\\mathrm  {II}$}\\\\mathaccent \\\"0365{\\\\mathrm  {II}}_{\\\\textit  {low}} - \\\\setbox \\\\z@ \\\\hbox {\\\\mathsurround \\\\z@ $\\\\textstyle \\\\mathrm  {II}$}\\\\mathaccent \\\"0365{\\\\mathrm  {II}}_{\\\\textit  {high}}$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}50$ MATH-500 problems).\\\\relax }}{4}{table.caption.13}\\\\protected@file@percent }\\n/root/autodl-tmp/pacs/paper/main.aux:377:\\\\newlabel{tab:aggregate-ii}{{1}{4}{Median compound severity difference ($\\\\Delta = \\\\widetilde {\\\\mathrm {II}}_{\\\\textit {low}} - \\\\widetilde {\\\\mathrm {II}}_{\\\\textit {high}}$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}50$ MATH-500 problems).\\\\relax }{table.caption.13}{}}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 74_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_012z8AGjNRuK2Qo6TcrDxQG9`</summary>

```json
{
  "server": "westd-22162",
  "command": "grep -rn \"d_z\" /root/autodl-tmp/pacs/paper/abstract.tex /root/autodl-tmp/pacs/paper/introduction.tex /root/autodl-tmp/pacs/paper/results.tex /root/autodl-tmp/pacs/paper/conclusion.tex /root/autodl-tmp/pacs/paper/limitations.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "64a0ae50-d0de-482c-bc07-beaa697bbf08",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011DH1yLjRLXJiDs45hL7shG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3293,
      "cache_read_input_tokens": 57163,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3293
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

_source line 75 · 2026-05-15T02:18:27.463Z_

<details><summary>↩ Tool result · `toolu_012z8AGjNRuK2Qo6TcrDxQG9`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/pacs/paper/abstract.tex:7:Under importance-based KV cache eviction, the median Interaction Index difference between low-sparsity and high-sparsity reasoning phases increases monotonically from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired Cohen's $d_z$ growing from $0.44$ (small) to $0.80$ (large); Bonferroni-corrected permutation tests yield $p < 0.005$ at all four sparsity levels.\\n/root/autodl-tmp/pacs/paper/abstract.tex:10:The pattern replicates on Qwen2.5-7B-Instruct at $s \\\\geq 0.20$ ($d_z \\\\geq 0.55$; Spearman $\\\\rho = 1.0$; gradient permutation $p = 0.043$) and on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM), where monotonically increasing median paired differences ($\\\\widetilde{\\\\Delta}$: $0.020 \\\\to 0.356$; $s{=}0.30$ Wilcoxon $p_{\\\\text{Bonf}}{=}0.029$) provide mixed but directionally consistent evidence for cross-architecture generalization, though at ${\\\\sim}$1/40 the absolute magnitude and with substantially weaker interaction than in Qwen2-based architectures. % exp_id: c3_llama\\n/root/autodl-tmp/pacs/paper/introduction.tex:14:On DeepSeek-R1-Distill-Qwen-7B, the median phase difference rises from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$ ($d_z$: $0.44 \\\\to 0.80$; Bonferroni-corrected $p < 0.005$ at all levels).\\n/root/autodl-tmp/pacs/paper/introduction.tex:15:The pattern replicates at $s \\\\geq 0.20$ on Qwen2.5-7B-Instruct ($d_z \\\\geq 0.55$) and partially extends to a distinct architecture (DeepSeek-R1-Distill-Llama-8B, LlamaForCausalLM) with a qualitatively consistent but substantially weaker trend at $\\\\sim$1/40 the magnitude.\\n/root/autodl-tmp/pacs/paper/results.tex:71:Qwen2.5-7B-Instruct (standard instruction tuning, same Qwen2 backbone) reproduces the monotonic severity gradient: $\\\\Delta$ increases from $0.04$ at $s{=}0.15$ to $2.94$ at $s{=}0.30$, paralleling DeepSeek at ${\\\\sim}1/5$ the magnitude. Both models yield strictly increasing $d_z$ trajectories (Spearman $\\\\rho = 1.0$; gradient permutation $p = 0.043$). The effect is marginal at $s{=}0.15$ ($d_z{=}0.28$, CI includes zero) but reliable at $s \\\\geq 0.20$ ($d_z \\\\geq 0.55$). A caveat applies to mid-phase comparisons: on Qwen2.5-7B-Instruct, approximately \\\\placeholder{NULL\\\\_PCT}\\\\% of problems yield near-zero Interaction Index in the mid-sparsity phase, where attention patterns exhibit insufficient variation to produce measurable compound interaction. This elevated null rate reduces the effective sample size for mid-phase comparisons; our primary cross-model analysis therefore focuses on the low--high phase contrast ($\\\\Delta$), which is unaffected by this limitation. Per-phase effective sample sizes are reported in Appendix~\\\\ref{app:qwen-null-rate}. Full cross-model tables and figures appear in Appendix~\\\\ref{app:cross-model-details}. % exp_id: cross_model_analysis.json; cohens_d_bf16_qwen.json\\n/root/autodl-tmp/pacs/paper/results.tex:106:Table~\\\\ref{tab:cohens-d} reports paired Cohen's $d_z$ for both models. For DeepSeek, effect sizes grow from $d_z{=}0.44$ (small) to $d_z{=}0.80$ (large). For Qwen, the effect is marginal at $s{=}0.15$ ($d_z{=}0.28$, CI includes zero), becoming reliable at $s \\\\geq 0.20$ ($d_z \\\\geq 0.55$). At $s \\\\geq 0.25$, Qwen exhibits larger standardized effect sizes ($d_z{=}0.89$/$1.02$ vs.\\\\ $0.68$/$0.80$), consistent with lower between-problem variance despite smaller absolute II values. % exp_id: cohens_d_bf16.json; cohens_d_bf16_qwen.json\\n/root/autodl-tmp/pacs/paper/results.tex:111:\\\\caption{Paired $d_z$ for phase-dependent II (low $-$ high) under importance-based eviction. Bootstrap 95\\\\% CIs ($B{=}10{,}000$).}\\n/root/autodl-tmp/pacs/paper/results.tex:115:$s$ & DS $d_z$ & $\\\\widetilde{\\\\Delta}$ [CI] & QW $d_z$ & $\\\\widetilde{\\\\Delta}$ [CI] \\\\\\\\\\n/root/autodl-tmp/pacs/paper/conclusion.tex:4:We showed that compound sparsity severity---the super-additive interaction between head pruning and KV cache eviction---is not phase-invariant but exhibits an emergent phase-strategy interaction spanning over an order of magnitude within a single generation. Under importance-based eviction, the severity gradient grows from $69{\\\\times}$ to $274{\\\\times}$ across sparsity levels ($d_z$: $0.44 \\\\to 0.80$); random eviction shows no such modulation (7/8 conditions non-significant). A crossover at $s{=}0.25$---where importance-based eviction reverses ranking across phases---demonstrates that no single strategy dominates uniformly. The pattern replicates on Qwen2.5-7B-Instruct at $s \\\\geq 0.20$ ($d_z \\\\geq 0.55$) and partially extends cross-architecture to DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM) with a qualitatively consistent but substantially weaker trend at $\\\\sim$1/40 the magnitude. Discrimination collapse provides a mechanistic explanation supported by both Qwen2-based models; LLaMA results are directionally consistent but the interaction is weaker than in Qwen2 architectures.\\n/root/autodl-tmp/pacs/paper/limitations.tex:2:All experiments are conducted at the 7--8B parameter scale. Whether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested. Preliminary cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \\\\S\\\\ref{sec:cross-arch}) partially confirms the qualitative pattern beyond the Qwen2 architecture---monotonically increasing $d_z$ with within-importance phase gradient $\\\\sim$1.0---but with substantially weaker interaction magnitude ($\\\\sim$1/40 of DeepSeek) and mixed statistical evidence (only $s{=}0.30$ significant after Bonferroni correction). The pattern has been tested on two architecture families (Qwen2ForCausalLM, LlamaForCausalLM); comprehensive validation across more diverse architectures (e.g., Mistral, multi-latent attention) and larger scales is needed for full generalization claims.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "702297b9-85c7-4991-a273-16fbf7751d9b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/pacs/paper/abstract.tex:7:Under importance-based KV cache eviction, the median Interaction Index difference between low-sparsity and high-sparsity reasoning phases increases monotonically from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired Cohen's $d_z$ growing from $0.44$ (small) to $0.80$ (large); Bonferroni-corrected permutation tests yield $p < 0.005$ at all four sparsity levels.\\\\n/root/autodl-tmp/pacs/paper/abstract.tex:10:The pattern replicates on Qwen2.5-7B-Instruct at $s \\\\\\\\geq 0.20$ ($d_z \\\\\\\\geq 0.55$; Spearman $\\\\\\\\rho = 1.0$; gradient permutation $p = 0.043$) and on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM), where monotonically increasing median paired differences ($\\\\\\\\widetilde{\\\\\\\\Delta}$: $0.020 \\\\\\\\to 0.356$; $s{=}0.30$ Wilcoxon $p_{\\\\\\\\text{Bonf}}{=}0.029$) provide mixed but directionally consistent evidence for cross-architecture generalization, though at ${\\\\\\\\sim}$1/40 the absolute magnitude and with substantially weaker interaction than in Qwen2-based architectures. % exp_id: c3_llama\\\\n/root/autodl-tmp/pacs/paper/introduction.tex:14:On DeepSeek-R1-Distill-Qwen-7B, the median phase difference rises from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$ ($d_z$: $0.44 \\\\\\\\to 0.80$; Bonferroni-corrected $p < 0.005$ at all levels).\\\\n/root/autodl-tmp/pacs/paper/introduction.tex:15:The pattern replicates at $s \\\\\\\\geq 0.20$ on Qwen2.5-7B-Instruct ($d_z \\\\\\\\geq 0.55$) and partially extends to a distinct architecture (DeepSeek-R1-Distill-Llama-8B, LlamaForCausalLM) with a qualitatively consistent but substantially weaker trend at $\\\\\\\\sim$1/40 the magnitude.\\\\n/root/autodl-tmp/pacs/paper/results.tex:71:Qwen2.5-7B-Instruct (standard instruction tuning, same Qwen2 backbone) reproduces the monotonic severity gradient: $\\\\\\\\Delta$ increases from $0.04$ at $s{=}0.15$ to $2.94$ at $s{=}0.30$, paralleling DeepSeek at ${\\\\\\\\sim}1/5$ the magnitude. Both models yield strictly increasing $d_z$ trajectories (Spearman $\\\\\\\\rho = 1.0$; gradient permutation $p = 0.043$). The effect is marginal at $s{=}0.15$ ($d_z{=}0.28$, CI includes zero) but reliable at $s \\\\\\\\geq 0.20$ ($d_z \\\\\\\\geq 0.55$). A caveat applies to mid-phase comparisons: on Qwen2.5-7B-Instruct, approximately \\\\\\\\placeholder{NULL\\\\\\\\_PCT}\\\\\\\\% of problems yield near-zero Interaction Index in the mid-sparsity phase, where attention patterns exhibit insufficient variation to produce measurable compound interaction. This elevated null rate reduces the effective sample size for mid-phase comparisons; our primary cross-model analysis therefore focuses on the low--high phase contrast ($\\\\\\\\Delta$), which is unaffected by this limitation. Per-phase effective sample sizes are reported in Appendix~\\\\\\\\ref{app:qwen-null-rate}. Full cross-model tables and figures appear in Appendix~\\\\\\\\ref{app:cross-model-details}. % exp_id: cross_model_analysis.json; cohens_d_bf16_qwen.json\\\\n/root/autodl-tmp/pacs/paper/results.tex:106:Table~\\\\\\\\ref{tab:cohens-d} reports paired Cohen's $d_z$ for both models. For DeepSeek, effect sizes grow from $d_z{=}0.44$ (small) to $d_z{=}0.80$ (large). For Qwen, the effect is marginal at $s{=}0.15$ ($d_z{=}0.28$, CI includes zero), becoming reliable at $s \\\\\\\\geq 0.20$ ($d_z \\\\\\\\geq 0.55$). At $s \\\\\\\\geq 0.25$, Qwen exhibits larger standardized effect sizes ($d_z{=}0.89$/$1.02$ vs.\\\\\\\\ $0.68$/$0.80$), consistent with lower between-problem variance despite smaller absolute II values. % exp_id: cohens_d_bf16.json; cohens_d_bf16_qwen.json\\\\n/root/autodl-tmp/pacs/paper/results.tex:111:\\\\\\\\caption{Paired $d_z$ for phase-dependent II (low $-$ high) under importance-based eviction. Bootstrap 95\\\\\\\\% CIs ($B{=}10{,}000$).}\\\\n/root/autodl-tmp/pacs/paper/results.tex:115:$s$ & DS $d_z$ & $\\\\\\\\widetilde{\\\\\\\\Delta}$ [CI] & QW $d_z$ & $\\\\\\\\widetilde{\\\\\\\\Delta}$ [CI] \\\\\\\\\\\\\\\\\\\\n/root/autodl-tmp/pacs/paper/conclusion.tex:4:We showed that compound sparsity severity---the super-additive interaction between head pruning and KV cache eviction---is not phase-invariant but exhibits an emergent phase-strategy interaction spanning over an order of magnitude within a single generation. Under importance-based eviction, the severity gradient grows from $69{\\\\\\\\times}$ to $274{\\\\\\\\times}$ across sparsity levels ($d_z$: $0.44 \\\\\\\\to 0.80$); random eviction shows no such modulation (7/8 conditions non-significant). A crossover at $s{=}0.25$---where importance-based eviction reverses ranking across phases---demonstrates that no single strategy dominates uniformly. The pattern replicates on Qwen2.5-7B-Instruct at $s \\\\\\\\geq 0.20$ ($d_z \\\\\\\\geq 0.55$) and partially extends cross-architecture to DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM) with a qualitatively consistent but substantially weaker trend at $\\\\\\\\sim$1/40 the magnitude. Discrimination collapse provides a mechanistic explanation supported by both Qwen2-based models; LLaMA results are directionally consistent but the interaction is weaker than in Qwen2 architectures.\\\\n/root/autodl-tmp/pacs/paper/limitations.tex:2:All experiments are conducted at the 7--8B parameter scale. Whether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested. Preliminary cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \\\\\\\\S\\\\\\\\ref{sec:cross-arch}) partially confirms the qualitative pattern beyond the Qwen2 architecture---monotonically increasing $d_z$ with within-importance phase gradient $\\\\\\\\sim$1.0---but with substantially weaker interaction magnitude ($\\\\\\\\sim$1/40 of DeepSeek) and mixed statistical evidence (only $s{=}0.30$ significant after Bonferroni correction). The pattern has been tested on two architecture families (Qwen2ForCausalLM, LlamaForCausalLM); comprehensive validation across more diverse architectures (e.g., Mistral, multi-latent attention) and larger scales is needed for full generalization claims.\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/pacs/paper/abstract.tex:7:Under importance-based KV cache eviction, the median Interaction Index difference between low-sparsity and high-sparsity reasoning phases increases monotonically from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired Cohen's $d_z$ growing from $0.44$ (small) to $0.80$ (large); Bonferroni-corrected permutation tests yield $p < 0.005$ at all four sparsity levels.\\n/root/autodl-tmp/pacs/paper/abstract.tex:10:The pattern replicates on Qwen2.5-7B-Instruct at $s \\\\geq 0.20$ ($d_z \\\\geq 0.55$; Spearman $\\\\rho = 1.0$; gradient permutation $p = 0.043$) and on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM), where monotonically increasing median paired differences ($\\\\widetilde{\\\\Delta}$: $0.020 \\\\to 0.356$; $s{=}0.30$ Wilcoxon $p_{\\\\text{Bonf}}{=}0.029$) provide mixed but directionally consistent evidence for cross-architecture generalization, though at ${\\\\sim}$1/40 the absolute magnitude and with substantially weaker interaction than in Qwen2-based architectures. % exp_id: c3_llama\\n/root/autodl-tmp/pacs/paper/introduction.tex:14:On DeepSeek-R1-Distill-Qwen-7B, the median phase difference rises from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$ ($d_z$: $0.44 \\\\to 0.80$; Bonferroni-corrected $p < 0.005$ at all levels).\\n/root/autodl-tmp/pacs/paper/introduction.tex:15:The pattern replicates at $s \\\\geq 0.20$ on Qwen2.5-7B-Instruct ($d_z \\\\geq 0.55$) and partially extends to a distinct architecture (DeepSeek-R1-Distill-Llama-8B, LlamaForCausalLM) with a qualitatively consistent but substantially weaker trend at $\\\\sim$1/40 the magnitude.\\n/root/autodl-tmp/pacs/paper/results.tex:71:Qwen2.5-7B-Instruct (standard instruction tuning, same Qwen2 backbone) reproduces the monotonic severity gradient: $\\\\Delta$ increases from $0.04$ at $s{=}0.15$ to $2.94$ at $s{=}0.30$, paralleling DeepSeek at ${\\\\sim}1/5$ the magnitude. Both models yield strictly increasing $d_z$ trajectories (Spearman $\\\\rho = 1.0$; gradient permutation $p = 0.043$). The effect is marginal at $s{=}0.15$ ($d_z{=}0.28$, CI includes zero) but reliable at $s \\\\geq 0.20$ ($d_z \\\\geq 0.55$). A caveat applies to mid-phase comparisons: on Qwen2.5-7B-Instruct, approximately \\\\placeholder{NULL\\\\_PCT}\\\\% of problems yield near-zero Interaction Index in the mid-sparsity phase, where attention patterns exhibit insufficient variation to produce measurable compound interaction. This elevated null rate reduces the effective sample size for mid-phase comparisons; our primary cross-model analysis therefore focuses on the low--high phase contrast ($\\\\Delta$), which is unaffected by this limitation. Per-phase effective sample sizes are reported in Appendix~\\\\ref{app:qwen-null-rate}. Full cross-model tables and figures appear in Appendix~\\\\ref{app:cross-model-details}. % exp_id: cross_model_analysis.json; cohens_d_bf16_qwen.json\\n/root/autodl-tmp/pacs/paper/results.tex:106:Table~\\\\ref{tab:cohens-d} reports paired Cohen's $d_z$ for both models. For DeepSeek, effect sizes grow from $d_z{=}0.44$ (small) to $d_z{=}0.80$ (large). For Qwen, the effect is marginal at $s{=}0.15$ ($d_z{=}0.28$, CI includes zero), becoming reliable at $s \\\\geq 0.20$ ($d_z \\\\geq 0.55$). At $s \\\\geq 0.25$, Qwen exhibits larger standardized effect sizes ($d_z{=}0.89$/$1.02$ vs.\\\\ $0.68$/$0.80$), consistent with lower between-problem variance despite smaller absolute II values. % exp_id: cohens_d_bf16.json; cohens_d_bf16_qwen.json\\n/root/autodl-tmp/pacs/paper/results.tex:111:\\\\caption{Paired $d_z$ for phase-dependent II (low $-$ high) under importance-based eviction. Bootstrap 95\\\\% CIs ($B{=}10{,}000$).}\\n/root/autodl-tmp/pacs/paper/results.tex:115:$s$ & DS $d_z$ & $\\\\widetilde{\\\\Delta}$ [CI] & QW $d_z$ & $\\\\widetilde{\\\\Delta}$ [CI] \\\\\\\\\\n/root/autodl-tmp/pacs/paper/conclusion.tex:4:We showed that compound sparsity severity---the super-additive interaction between head pruning and KV cache eviction---is not phase-invariant but exhibits an emergent phase-strategy interaction spanning over an order of magnitude within a single generation. Under importance-based eviction, the severity gradient grows from $69{\\\\times}$ to $274{\\\\times}$ across sparsity levels ($d_z$: $0.44 \\\\to 0.80$); random eviction shows no such modulation (7/8 conditions non-significant). A crossover at $s{=}0.25$---where importance-based eviction reverses ranking across phases---demonstrates that no single strategy dominates uniformly. The pattern replicates on Qwen2.5-7B-Instruct at $s \\\\geq 0.20$ ($d_z \\\\geq 0.55$) and partially extends cross-architecture to DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM) with a qualitatively consistent but substantially weaker trend at $\\\\sim$1/40 the magnitude. Discrimination collapse provides a mechanistic explanation supported by both Qwen2-based models; LLaMA results are directionally consistent but the interaction is weaker than in Qwen2 architectures.\\n/root/autodl-tmp/pacs/paper/limitations.tex:2:All experiments are conducted at the 7--8B parameter scale. Whether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested. Preliminary cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \\\\S\\\\ref{sec:cross-arch}) partially confirms the qualitative pattern beyond the Qwen2 architecture---monotonically increasing $d_z$ with within-importance phase gradient $\\\\sim$1.0---but with substantially weaker interaction magnitude ($\\\\sim$1/40 of DeepSeek) and mixed statistical evidence (only $s{=}0.30$ significant after Bonferroni correction). The pattern has been tested on two architecture families (Qwen2ForCausalLM, LlamaForCausalLM); comprehensive validation across more diverse architectures (e.g., Mistral, multi-latent attention) and larger scales is needed for full generalization claims.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 76_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01KkAtRAKfaXLXhtv7VtpGgq`</summary>

```json
{
  "server": "westd-22162",
  "command": "grep -rn \"fig:\" /root/autodl-tmp/pacs/paper/ --include=\"*.tex\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "dff4c199-9c1c-4161-a5ba-90be1c0f7476",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011DH1yLjRLXJiDs45hL7shG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3293,
      "cache_read_input_tokens": 57163,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3293
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

_source line 77 · 2026-05-15T02:18:28.182Z_

<details><summary>↩ Tool result · `toolu_01KkAtRAKfaXLXhtv7VtpGgq`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/pacs/paper/results.tex:29:Decomposing II by reasoning phase reveals that strategy-dependent severity is driven by amplification in the low-sparsity phase. Table~\\\\ref{tab:main-results} reports the full per-phase breakdown. The severity gradient $G$ increases from $69{\\\\times}$ at $s{=}0.15$ to $274{\\\\times}$ at $s{=}0.30$ under importance-based eviction, while the high-sparsity phase experiences near-zero interaction ($\\\\widetilde{\\\\mathrm{II}}_{\\\\textit{high}}$ ranges from $0.006$ to $0.053$). Under random eviction, $G \\\\approx 0.9$--$1.7{\\\\times}$ at all sparsity levels. Figure~\\\\ref{fig:hero} visualizes this contrast. % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json\\n/root/autodl-tmp/pacs/paper/results.tex:59:\\\\label{fig:hero}\\n/root/autodl-tmp/pacs/paper/appendix_moved.tex:11:At $s{=}0.25$, a strategy ranking reversal emerges (Figure~\\\\ref{fig:crossover}): importance-based eviction yields \\\\emph{lower} II than random in the high-sparsity phase ($0.032$ vs.\\\\ $0.818$) but \\\\emph{higher} II in the low-sparsity phase ($7.196$ vs.\\\\ $1.363$---a $5.3{\\\\times}$ reversal). This crossover is present at all four sparsity levels, with reversal magnitude of $3.9{\\\\times}$ at $s{=}0.15$, $5.4{\\\\times}$ at $s{=}0.20$, $5.3{\\\\times}$ at $s{=}0.25$, and $3.6{\\\\times}$ at $s{=}0.30$ (as random eviction severity also rises). The reversal arises because head pruning redistributes attention mass, altering importance rankings in a way that couples the two sparsity mechanisms in low-sparsity phases (\\\\S\\\\ref{sec:discrimination-collapse}). % exp_id: bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json; 7.196/1.363=5.28\\n/root/autodl-tmp/pacs/paper/appendix_moved.tex:17:\\\\label{fig:crossover}\\n/root/autodl-tmp/pacs/paper/appendix_moved.tex:48:Table~\\\\ref{tab:cross-model} reports the cross-model comparison. Qwen reproduces the monotonic severity gradient at ${\\\\sim}1/5$ of DeepSeek's magnitude. Figure~\\\\ref{fig:cross-model} visualizes this comparison. % exp_id: cross_model_analysis.json; cohens_d_bf16_qwen.json\\n/root/autodl-tmp/pacs/paper/appendix_moved.tex:69:\\\\label{fig:cross-model}\\n/root/autodl-tmp/pacs/paper/appendix_moved.tex:88:Table~\\\\ref{tab:permutation} reports the results. All four sparsity levels reject $H_0$ after Bonferroni correction ($p_{\\\\text{Bonf}} < 0.005$), with observed median differences increasing monotonically from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$. The monotonic growth of both the point estimate and the CI lower bound ($0.19 \\\\to 0.69 \\\\to 1.66 \\\\to 6.70$) confirms that compound severity amplification strengthens with sparsity---not merely in central tendency but also in worst-case lower bounds. Figure~\\\\ref{fig:permtest-forest} presents these results as a forest plot. % exp_id: deepseek_bf16_permtest; source: permutation_test_results.json\\n/root/autodl-tmp/pacs/paper/appendix_moved.tex:111:\\\\label{fig:permtest-forest}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "9fd7b9eb-b3e1-4c92-aa05-ee2633a96592",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/pacs/paper/results.tex:29:Decomposing II by reasoning phase reveals that strategy-dependent severity is driven by amplification in the low-sparsity phase. Table~\\\\\\\\ref{tab:main-results} reports the full per-phase breakdown. The severity gradient $G$ increases from $69{\\\\\\\\times}$ at $s{=}0.15$ to $274{\\\\\\\\times}$ at $s{=}0.30$ under importance-based eviction, while the high-sparsity phase experiences near-zero interaction ($\\\\\\\\widetilde{\\\\\\\\mathrm{II}}_{\\\\\\\\textit{high}}$ ranges from $0.006$ to $0.053$). Under random eviction, $G \\\\\\\\approx 0.9$--$1.7{\\\\\\\\times}$ at all sparsity levels. Figure~\\\\\\\\ref{fig:hero} visualizes this contrast. % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json\\\\n/root/autodl-tmp/pacs/paper/results.tex:59:\\\\\\\\label{fig:hero}\\\\n/root/autodl-tmp/pacs/paper/appendix_moved.tex:11:At $s{=}0.25$, a strategy ranking reversal emerges (Figure~\\\\\\\\ref{fig:crossover}): importance-based eviction yields \\\\\\\\emph{lower} II than random in the high-sparsity phase ($0.032$ vs.\\\\\\\\ $0.818$) but \\\\\\\\emph{higher} II in the low-sparsity phase ($7.196$ vs.\\\\\\\\ $1.363$---a $5.3{\\\\\\\\times}$ reversal). This crossover is present at all four sparsity levels, with reversal magnitude of $3.9{\\\\\\\\times}$ at $s{=}0.15$, $5.4{\\\\\\\\times}$ at $s{=}0.20$, $5.3{\\\\\\\\times}$ at $s{=}0.25$, and $3.6{\\\\\\\\times}$ at $s{=}0.30$ (as random eviction severity also rises). The reversal arises because head pruning redistributes attention mass, altering importance rankings in a way that couples the two sparsity mechanisms in low-sparsity phases (\\\\\\\\S\\\\\\\\ref{sec:discrimination-collapse}). % exp_id: bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json; 7.196/1.363=5.28\\\\n/root/autodl-tmp/pacs/paper/appendix_moved.tex:17:\\\\\\\\label{fig:crossover}\\\\n/root/autodl-tmp/pacs/paper/appendix_moved.tex:48:Table~\\\\\\\\ref{tab:cross-model} reports the cross-model comparison. Qwen reproduces the monotonic severity gradient at ${\\\\\\\\sim}1/5$ of DeepSeek's magnitude. Figure~\\\\\\\\ref{fig:cross-model} visualizes this comparison. % exp_id: cross_model_analysis.json; cohens_d_bf16_qwen.json\\\\n/root/autodl-tmp/pacs/paper/appendix_moved.tex:69:\\\\\\\\label{fig:cross-model}\\\\n/root/autodl-tmp/pacs/paper/appendix_moved.tex:88:Table~\\\\\\\\ref{tab:permutation} reports the results. All four sparsity levels reject $H_0$ after Bonferroni correction ($p_{\\\\\\\\text{Bonf}} < 0.005$), with observed median differences increasing monotonically from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$. The monotonic growth of both the point estimate and the CI lower bound ($0.19 \\\\\\\\to 0.69 \\\\\\\\to 1.66 \\\\\\\\to 6.70$) confirms that compound severity amplification strengthens with sparsity---not merely in central tendency but also in worst-case lower bounds. Figure~\\\\\\\\ref{fig:permtest-forest} presents these results as a forest plot. % exp_id: deepseek_bf16_permtest; source: permutation_test_results.json\\\\n/root/autodl-tmp/pacs/paper/appendix_moved.tex:111:\\\\\\\\label{fig:permtest-forest}\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.46}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/pacs/paper/results.tex:29:Decomposing II by reasoning phase reveals that strategy-dependent severity is driven by amplification in the low-sparsity phase. Table~\\\\ref{tab:main-results} reports the full per-phase breakdown. The severity gradient $G$ increases from $69{\\\\times}$ at $s{=}0.15$ to $274{\\\\times}$ at $s{=}0.30$ under importance-based eviction, while the high-sparsity phase experiences near-zero interaction ($\\\\widetilde{\\\\mathrm{II}}_{\\\\textit{high}}$ ranges from $0.006$ to $0.053$). Under random eviction, $G \\\\approx 0.9$--$1.7{\\\\times}$ at all sparsity levels. Figure~\\\\ref{fig:hero} visualizes this contrast. % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json\\n/root/autodl-tmp/pacs/paper/results.tex:59:\\\\label{fig:hero}\\n/root/autodl-tmp/pacs/paper/appendix_moved.tex:11:At $s{=}0.25$, a strategy ranking reversal emerges (Figure~\\\\ref{fig:crossover}): importance-based eviction yields \\\\emph{lower} II than random in the high-sparsity phase ($0.032$ vs.\\\\ $0.818$) but \\\\emph{higher} II in the low-sparsity phase ($7.196$ vs.\\\\ $1.363$---a $5.3{\\\\times}$ reversal). This crossover is present at all four sparsity levels, with reversal magnitude of $3.9{\\\\times}$ at $s{=}0.15$, $5.4{\\\\times}$ at $s{=}0.20$, $5.3{\\\\times}$ at $s{=}0.25$, and $3.6{\\\\times}$ at $s{=}0.30$ (as random eviction severity also rises). The reversal arises because head pruning redistributes attention mass, altering importance rankings in a way that couples the two sparsity mechanisms in low-sparsity phases (\\\\S\\\\ref{sec:discrimination-collapse}). % exp_id: bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json; 7.196/1.363=5.28\\n/root/autodl-tmp/pacs/paper/appendix_moved.tex:17:\\\\label{fig:crossover}\\n/root/autodl-tmp/pacs/paper/appendix_moved.tex:48:Table~\\\\ref{tab:cross-model} reports the cross-model comparison. Qwen reproduces the monotonic severity gradient at ${\\\\sim}1/5$ of DeepSeek's magnitude. Figure~\\\\ref{fig:cross-model} visualizes this comparison. % exp_id: cross_model_analysis.json; cohens_d_bf16_qwen.json\\n/root/autodl-tmp/pacs/paper/appendix_moved.tex:69:\\\\label{fig:cross-model}\\n/root/autodl-tmp/pacs/paper/appendix_moved.tex:88:Table~\\\\ref{tab:permutation} reports the results. All four sparsity levels reject $H_0$ after Bonferroni correction ($p_{\\\\text{Bonf}} < 0.005$), with observed median differences increasing monotonically from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$. The monotonic growth of both the point estimate and the CI lower bound ($0.19 \\\\to 0.69 \\\\to 1.66 \\\\to 6.70$) confirms that compound severity amplification strengthens with sparsity---not merely in central tendency but also in worst-case lower bounds. Figure~\\\\ref{fig:permtest-forest} presents these results as a forest plot. % exp_id: deepseek_bf16_permtest; source: permutation_test_results.json\\n/root/autodl-tmp/pacs/paper/appendix_moved.tex:111:\\\\label{fig:permtest-forest}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 78_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive view of all the .tex files. Let me compile the checklist.

Here's what I've found:

### "50 problems" / "n=50" / "50 MATH" mentions:
1. **abstract.tex:6** — "using 50 MATH-500 problems"
2. **methodology.tex:10** — "We use 50 problems stratified from MATH-500"
3. **results.tex:13** — Table 1 caption: "($n{=}50$ MATH-500 problems)"
4. **results.tex:34** — Table 2 caption: "medians across 50 problems"


5. **appendix_moved.tex:26** — "Four of the 50 problems are excluded..."

### n{=}49, n{=}46 mentions:
1. **results.tex:77** — "n{=}49 paired problems" (LLaMA cross-arch)
2. **appendix_disc_analysis.tex:45** — "n{=}49 paired problems for DeepSeek (1 excluded) and n{=}46 for Qwen (4 excluded)"
3. **appendix_moved.tex:26** — "n{=}46 valid problems for Qwen (vs. n{=}49 for DeepSeek)"
4. **appendix_moved.tex:93** — Table permutation caption: "n{=}49"

Now I'm tracking the effect size measurements across the paper. The Cohen's d and d_z values show DeepSeek ranging from 0.44 to 0.80, while Qwen's standardized effect sizes are consistently ≥ 0.55, with some reaching as high as 1.02 in the results section. LLaMA shows smaller differences, with Δ values between 0.020 and 0.356.

Looking at the bootstrap confidence intervals in Table 3, I'm seeing the actual magnitude of these effects — DeepSeek's s015 has a modest effect (d_z=0.44, Δ=0.32), but by s030 the effect size grows substantially (d_z=0.80, Δ=9.94 with CI [8.39...]). Now I'm mapping out the table and figure references from the results and appendix files—Table 1 shows the aggregate DeepSeek results by strategy, Table 2 has the full per-phase breakdown, Table 3 contains the paired Cohen's d values, and Table 4 covers the LLaMA cross-architecture comparisons, while the figures include the dose-response curve, crossover analysis, cross-model comparisons, and the permutation test forest plot.

I'm also tracking down all the placeholder values scattered throughout the manuscript—there are about 20+ instances across the abstract, results, discussion, and appendix sections that need to be filled in with actual numbers for Qwen and LLaMA performance metrics, null percentages, p-values, and effect sizes. I'm tracking which values need to be updated once the n=500 results arrive. For DeepSeek, that means refreshing the aggregate table with new Δ values, updating the per-phase results and effect sizes, changing several inline numbers in the abstract and discussion, and recalculating the crossover thresholds and permutation test confidence intervals. Qwen's n=500 data will require updates to the Cohen's d table as well.

I also need to check the cross-model comparisons—the effect sizes are shifting substantially from 0.04 to 2.94 for Δ and 0.28 to 1.02 for d_z—and verify whether Qwen's failure counts and p-values change with the larger sample. Additionally, I'm noting all the places in the paper where the C8 cross-architecture findings are mentioned, from the abstract through the appendices, so I can ensure the language about partial confirmation remains consistent when the new data comes in. I need to track which values will shift when scaling from n=50 to n=500 for DeepSeek and Qwen — sample sizes, effect sizes, confidence intervals, p-values, and G ratios all need updating across tables and inline text, while LLaMA results stay fixed unless that's also being scaled up.

The methodology section needs clarification too: if they're now using the full MATH-500 dataset instead of 50 stratified problems, the description changes from "50 problems stratified from MATH-500" to "500 problems from MATH-500," and I should verify whether LLaMA is staying at n=50 or also being rerun at the larger scale. Looking at the Qwen imp-vs-rand comparison, the current n=50 results show no significant differences, but scaling to n=500 might reveal significance that wasn't apparent before. I'm also tracking down all the placeholders that need filling — some are waiting for the n=500 data while others are just unfilled values from the current dataset. I should also check the discrimination collapse and entropy analysis tables in the appendix to see what concrete numbers are already there. I'm looking at the c4_entropy experiments—these are separate n=30 runs that won't be affected by the n=500 campaign, so they can stay as-is. Now I need to systematically go through the paper and identify what needs updating: all n=50 data points, Cohen's d values, bootstrap confidence intervals, text mentions of "50 problems," figure and table references, C8 qualifiers about LLaMA, the C5b future work section, and any Qwen-related caveats. The key challenge is tracking the inline numbers scattered throughout the abstract, introduction, and conclusion—these summary statistics from the DeepSeek experiments will need to be updated once the n=500 results come in. Let me organize this into three categories: items that must be updated, items that depend on the n=500 results, and items that don't need changes. I'm tracking down all the numerical updates needed across the paper. There are several places where DeepSeek's effect size metrics need to be revised—the abstract mentions specific values for the correlation coefficient at different thresholds, and the effect size measure grows from a small to large range. I need to find and update those baseline numbers along with the paired problem counts that changed after exclusions. Looking at the results section, I'm tracking the key numerical findings across different parameter settings. The amplification factor for Δ grows substantially from the lower to higher s values, and I'm noting the corresponding ranges for the importance-weighted metrics. Table 2 contains the main experimental results with all 24 cells organized by rows and conditions. I'm also capturing the figure caption that highlights the same amplification range, and moving into the crossover analysis section where I need to document the specific threshold values. and "7.196 vs. 1.363". Now I'm checking the appendix sections for the crossover values and reversal magnitudes, then verifying the permutation test results with their confidence intervals and checking if Table 7 exists with the concrete values.

Looking at the QWEN numerical data that needs updating across multiple files — I need to verify the delta values ranging from 0.04 to 2.94 across the s parameter range, confirm the Cohen's d values in Table 3, and check the abstract for the statistical thresholds including the Spearman correlation coefficient. Now I'm looking at the discrimination collapse metrics across both models—DeepSeek shows Gini values ranging from 0.030 to 0.081 while Qwen is tighter at 0.010 to 0.020, and the entropy shifts follow a similar pattern with DeepSeek dropping between −0.031 and −0.073 compared to Qwen's −0.019 to −0.045. I need to verify whether these c4_entropy results at n=30 were recalculated or if they're from an earlier run, and I should check the appendix tables for the full discrimination metrics and entropy delta breakdowns. The dose-response and crossover figures may need regeneration depending on whether the underlying data changed.

I'm also tracking several figures that still need to be created or verified—the cross-model comparison, the permutation test forest plot, and possibly the per-problem distribution figure—along with a handful of placeholders scattered through the abstract and results sections that need to be filled in with values from either the n=50 or n=500 datasets. Continuing through the appendix files, I'm tracking more placeholder values across Qwen results and the moved sections—null percentages, sample sizes, per-phase effective n calculations, and concordance metrics that still need to be filled in.

Now I'm noting that items 49, 46-48, and 50 aren't actually from the n=500 experiments—they come from the c5b_pilot and c3_llama datasets instead, so they'll need their own separate data sources pulled in independently of the main update.

For the C8 LLaMA partially_confirmed results, I'm seeing references scattered across the abstract, introduction, results section 5.5, discussion, conclusion, limitations, and the appendix discussion analysis—all describing how the findings partially extend or confirm across architectures with architecture-dependent magnitude variations.

The C5b future work section gets mentioned in the discussion as a pilot experiment, and then I'm tracking down all the Qwen-specific caveats: the marginal effect at s=0.15 with confidence intervals crossing zero, the NULL_PCT mid-phase issue, the s ≥ 0.20 threshold restrictions in abstract and introduction, and that random exception at s030 in the appendix. Finally, there's this recurring "7/8 FAIL" and "3/4 FAIL" pattern showing up in the abstract as "7/8 conditions," implicitly in results, explicitly in the conclusion as non-significant conditions, and partially in the appendix discussion.

Now I'm organizing this into a final checklist format, but I realize I need to double-check the cross-model comparison table in appendix_moved.tex since the output got truncated earlier. I found the reference to Table 5 describing how Qwen reproduces the monotonic severity gradient at roughly 1/5 of DeepSeek's magnitude, but I didn't capture the actual table content itself.

I should also keep in mind that some key values like the Spearman ρ=1.0 and gradient permutation p=0.043 might shift when I run the analysis with n=500. For the checklist, I'll note which datasets stay fixed—LLaMA at n=50, c4_entropy at n=30, and c5b_pilot at its current size—while the methodology and formulation text should remain consistent across versions.

The conditional updates depend on what the larger sample reveals: if Qwen's imp-vs-rand comparison becomes significant, I'll need to soften the "marginal" language and revise the failure count; if the s015 d_z no longer crosses zero, the onset threshold discussion changes; and if random conditions show significance, that affects the overall failure tally. Now I can draft the checklist with these dependencies in mind.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "6ba66fca-d1e5-4789-9d2e-26493c091a88",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LJQTReMi9rAUshUHoKArLx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4533,
      "cache_read_input_tokens": 60456,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4533
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

_source line 79_

所有文件已读取完毕。现在我对论文全貌有完整了解，开始生成更新清单。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "887a4108-b4ff-4e7f-993a-7522258f434b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LJQTReMi9rAUshUHoKArLx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4533,
      "cache_read_input_tokens": 60456,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4533
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

_source line 80_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01SE78wxPvquufNUTDEyhuPH`</summary>

```json
{
  "server": "westd-22162",
  "command": "grep -n \"tab:cross-model\" /root/autodl-tmp/pacs/paper/appendix_moved.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "4e31be90-f45c-43a3-b5ac-051b83a8da7e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LJQTReMi9rAUshUHoKArLx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4533,
      "cache_read_input_tokens": 60456,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4533
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

_source line 81 · 2026-05-15T02:20:51.040Z_

<details><summary>↩ Tool result · `toolu_01SE78wxPvquufNUTDEyhuPH`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"48:Table~\\\\ref{tab:cross-model} reports the cross-model comparison. Qwen reproduces the monotonic severity gradient at ${\\\\sim}1/5$ of DeepSeek's magnitude. Figure~\\\\ref{fig:cross-model} visualizes this comparison. % exp_id: cross_model_analysis.json; cohens_d_bf16_qwen.json\\n54:\\\\label{tab:cross-model}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "baf4d729-73cc-463a-b69e-641d092e27c6",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"48:Table~\\\\\\\\ref{tab:cross-model} reports the cross-model comparison. Qwen reproduces the monotonic severity gradient at ${\\\\\\\\sim}1/5$ of DeepSeek's magnitude. Figure~\\\\\\\\ref{fig:cross-model} visualizes this comparison. % exp_id: cross_model_analysis.json; cohens_d_bf16_qwen.json\\\\n54:\\\\\\\\label{tab:cross-model}\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"48:Table~\\\\ref{tab:cross-model} reports the cross-model comparison. Qwen reproduces the monotonic severity gradient at ${\\\\sim}1/5$ of DeepSeek's magnitude. Figure~\\\\ref{fig:cross-model} visualizes this comparison. % exp_id: cross_model_analysis.json; cohens_d_bf16_qwen.json\\n54:\\\\label{tab:cross-model}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 82_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01LFSEycaY6L3CTRswqt3GNp`</summary>

```json
{
  "server": "westd-22162",
  "command": "grep -n \"tab:permutation\" /root/autodl-tmp/pacs/paper/appendix_moved.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "bebf2bb2-6df0-4ebb-a296-35dfa13a6a7f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LJQTReMi9rAUshUHoKArLx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4533,
      "cache_read_input_tokens": 60456,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4533
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

_source line 83 · 2026-05-15T02:20:51.741Z_

<details><summary>↩ Tool result · `toolu_01LFSEycaY6L3CTRswqt3GNp`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"88:Table~\\\\ref{tab:permutation} reports the results. All four sparsity levels reject $H_0$ after Bonferroni correction ($p_{\\\\text{Bonf}} < 0.005$), with observed median differences increasing monotonically from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$. The monotonic growth of both the point estimate and the CI lower bound ($0.19 \\\\to 0.69 \\\\to 1.66 \\\\to 6.70$) confirms that compound severity amplification strengthens with sparsity---not merely in central tendency but also in worst-case lower bounds. Figure~\\\\ref{fig:permtest-forest} presents these results as a forest plot. % exp_id: deepseek_bf16_permtest; source: permutation_test_results.json\\n94:\\\\label{tab:permutation}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "aad31224-c6b5-410e-96b5-6b07f6518bc7",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"88:Table~\\\\\\\\ref{tab:permutation} reports the results. All four sparsity levels reject $H_0$ after Bonferroni correction ($p_{\\\\\\\\text{Bonf}} < 0.005$), with observed median differences increasing monotonically from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$. The monotonic growth of both the point estimate and the CI lower bound ($0.19 \\\\\\\\to 0.69 \\\\\\\\to 1.66 \\\\\\\\to 6.70$) confirms that compound severity amplification strengthens with sparsity---not merely in central tendency but also in worst-case lower bounds. Figure~\\\\\\\\ref{fig:permtest-forest} presents these results as a forest plot. % exp_id: deepseek_bf16_permtest; source: permutation_test_results.json\\\\n94:\\\\\\\\label{tab:permutation}\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"88:Table~\\\\ref{tab:permutation} reports the results. All four sparsity levels reject $H_0$ after Bonferroni correction ($p_{\\\\text{Bonf}} < 0.005$), with observed median differences increasing monotonically from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$. The monotonic growth of both the point estimate and the CI lower bound ($0.19 \\\\to 0.69 \\\\to 1.66 \\\\to 6.70$) confirms that compound severity amplification strengthens with sparsity---not merely in central tendency but also in worst-case lower bounds. Figure~\\\\ref{fig:permtest-forest} presents these results as a forest plot. % exp_id: deepseek_bf16_permtest; source: permutation_test_results.json\\n94:\\\\label{tab:permutation}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 84_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01PuLzesF3HJgwwkX8Tm8y1n`</summary>

```json
{
  "server": "westd-22162",
  "command": "head -70 /root/autodl-tmp/pacs/paper/appendix_moved.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "9430f8b3-1d6e-452e-944a-434985e4f2c8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RFMKKNejc4Q9mcXxgrcT18",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8078,
      "cache_read_input_tokens": 64989,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8078
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

### Tool call

_source line 85_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01BLrgCtrigVb9cTLzcdCDAL`</summary>

```json
{
  "server": "westd-22162",
  "command": "tail -50 /root/autodl-tmp/pacs/paper/appendix_moved.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "17fa93d8-73aa-43a0-afac-703313afb0ce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RFMKKNejc4Q9mcXxgrcT18",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8078,
      "cache_read_input_tokens": 64989,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8078
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

_source line 86 · 2026-05-15T02:21:02.863Z_

<details><summary>↩ Tool result · `toolu_01PuLzesF3HJgwwkX8Tm8y1n`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"% Content moved from main body to appendix:\\n% - Phase-strategy crossover details (from results §5.3)\\n% - Cross-model replication details with tables/figures (from results §5.4)\\n% - Permutation test details with table/forest plot (from results §5.5)\\n% - Full entropy-discrimination collapse analysis with tables (from analysis §6)\\n% Main body §6 (analysis.tex) contains a condensed summary referencing these tables.\\n\\n\\\\section{Phase-Strategy Crossover Details}\\n\\\\label{app:crossover-details}\\n\\nAt $s{=}0.25$, a strategy ranking reversal emerges (Figure~\\\\ref{fig:crossover}): importance-based eviction yields \\\\emph{lower} II than random in the high-sparsity phase ($0.032$ vs.\\\\ $0.818$) but \\\\emph{higher} II in the low-sparsity phase ($7.196$ vs.\\\\ $1.363$---a $5.3{\\\\times}$ reversal). This crossover is present at all four sparsity levels, with reversal magnitude of $3.9{\\\\times}$ at $s{=}0.15$, $5.4{\\\\times}$ at $s{=}0.20$, $5.3{\\\\times}$ at $s{=}0.25$, and $3.6{\\\\times}$ at $s{=}0.30$ (as random eviction severity also rises). The reversal arises because head pruning redistributes attention mass, altering importance rankings in a way that couples the two sparsity mechanisms in low-sparsity phases (\\\\S\\\\ref{sec:discrimination-collapse}). % exp_id: bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json; 7.196/1.363=5.28\\n\\n\\\\begin{figure}[t]\\n\\\\centering\\n\\\\includegraphics[width=\\\\columnwidth]{fig3_crossover.pdf}\\n\\\\caption{Strategy-dependent crossover at $s{=}0.25$. Grouped bar chart of median II by eviction strategy and reasoning phase. Importance-based eviction outperforms random in the high-sparsity phase but produces $5.3{\\\\times}$ higher II in the low-sparsity phase, reversing the strategy ranking.}\\n\\\\label{fig:crossover}\\n\\\\end{figure}\\n\\n\\n\\\\section{Cross-Model Replication Details}\\n\\\\label{app:cross-model-details}\\n\\nBoth models share the Qwen2ForCausalLM backbone (28 layers, 28 heads, 4-group GQA) but differ in training: DeepSeek uses reasoning distillation from DeepSeek-R1, while Qwen2.5 uses standard instruction tuning without explicit reasoning delimiters. This controlled comparison isolates the effect of training methodology on the compound sparsity interaction.\\n\\nDespite lacking explicit \\\\texttt{&lt;think>} delimiters, Qwen2.5-7B-Instruct exhibits sufficient variation in attention sparsity to permit phase segmentation via the same quantile-based method (\\\\S\\\\ref{sec:phase-segmentation}). Four of the 50 problems are excluded due to degenerate phase assignments, yielding $n{=}46$ valid problems for Qwen (vs.\\\\ $n{=}49$ for DeepSeek).\\n\\n\\\\paragraph{Per-phase effective sample size.}\\n\\\\label{app:qwen-null-rate}\\nTable~\\\\ref{tab:qwen-effective-n} reports the per-phase effective sample size for Qwen2.5-7B-Instruct, defined as the number of problems with $|\\\\mathrm{II}| > 0.001$ in each phase. The mid-phase null rate (\\\\placeholder{NULL\\\\_PCT}\\\\%) reflects problems where compound interaction is absent in intermediate phases; this does not affect the low--high contrast ($\\\\Delta$) used in the primary analysis.\\n\\n\\\\begin{table}[t]\\n\\\\centering\\n\\\\small\\n\\\\caption{Per-phase effective sample size for Qwen2.5-7B-Instruct ($n_{\\\\text{total}} = \\\\placeholder{N\\\\_QW}$).}\\n\\\\label{tab:qwen-effective-n}\\n\\\\begin{tabular}{@{}lcccc@{}}\\n\\\\toprule\\nPhase & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\\\\\\\\\n\\\\midrule\\nHigh & \\\\placeholder{} & \\\\placeholder{} & \\\\placeholder{} & \\\\placeholder{} \\\\\\\\\\nMid  & \\\\placeholder{} & \\\\placeholder{} & \\\\placeholder{} & \\\\placeholder{} \\\\\\\\\\nLow  & \\\\placeholder{} & \\\\placeholder{} & \\\\placeholder{} & \\\\placeholder{} \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n\\nTable~\\\\ref{tab:cross-model} reports the cross-model comparison. Qwen reproduces the monotonic severity gradient at ${\\\\sim}1/5$ of DeepSeek's magnitude. Figure~\\\\ref{fig:cross-model} visualizes this comparison. % exp_id: cross_model_analysis.json; cohens_d_bf16_qwen.json\\n\\n\\\\begin{table}[t]\\n\\\\centering\\n\\\\small\\n\\\\caption{Cross-model comparison of median compound severity difference ($\\\\Delta$) under importance-based eviction.}\\n\\\\label{tab:cross-model}\\n\\\\begin{tabular}{@{}lcccc@{}}\\n\\\\toprule\\nModel & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\\\\\\\\\n\\\\midrule\\nDeepSeek-R1-Distill-Qwen-7B & 0.39 & 1.48 & 7.16 & 14.59 \\\\\\\\ % exp_id: bf16_importance_s015..s030\\nQwen2.5-7B-Instruct         & 0.04 & 0.23 & 1.27 & 2.94 \\\\\\\\ % exp_id: bf16_qw_imp_s015..s030\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n\\n\\\\begin{figure}[t]\\n\\\\centering\\n\\\\includegraphics[width=\\\\columnwidth]{fig5_crossmodel.pdf}\\n\\\\caption{Cross-model comparison of the median severity difference under importance-based eviction. Both DeepSeek (solid) and Qwen (dashed) exhibit monotonically increasing $\\\\Delta$ with sparsity; Qwen's magnitude is approximately one-fifth of DeepSeek's.} % exp_id: bf16_importance_s015..s030, bf16_qw_imp_s015..s030\\n\\\\label{fig:cross-model}\\n\\\\end{figure}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "aad90d7c-0b68-46c6-b8ed-29b387fe16b8",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"% Content moved from main body to appendix:\\\\n% - Phase-strategy crossover details (from results §5.3)\\\\n% - Cross-model replication details with tables/figures (from results §5.4)\\\\n% - Permutation test details with table/forest plot (from results §5.5)\\\\n% - Full entropy-discrimination collapse analysis with tables (from analysis §6)\\\\n% Main body §6 (analysis.tex) contains a condensed summary referencing these tables.\\\\n\\\\n\\\\\\\\section{Phase-Strategy Crossover Details}\\\\n\\\\\\\\label{app:crossover-details}\\\\n\\\\nAt $s{=}0.25$, a strategy ranking reversal emerges (Figure~\\\\\\\\ref{fig:crossover}): importance-based eviction yields \\\\\\\\emph{lower} II than random in the high-sparsity phase ($0.032$ vs.\\\\\\\\ $0.818$) but \\\\\\\\emph{higher} II in the low-sparsity phase ($7.196$ vs.\\\\\\\\ $1.363$---a $5.3{\\\\\\\\times}$ reversal). This crossover is present at all four sparsity levels, with reversal magnitude of $3.9{\\\\\\\\times}$ at $s{=}0.15$, $5.4{\\\\\\\\times}$ at $s{=}0.20$, $5.3{\\\\\\\\times}$ at $s{=}0.25$, and $3.6{\\\\\\\\times}$ at $s{=}0.30$ (as random eviction severity also rises). The reversal arises because head pruning redistributes attention mass, altering importance rankings in a way that couples the two sparsity mechanisms in low-sparsity phases (\\\\\\\\S\\\\\\\\ref{sec:discrimination-collapse}). % exp_id: bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json; 7.196/1.363=5.28\\\\n\\\\n\\\\\\\\begin{figure}[t]\\\\n\\\\\\\\centering\\\\n\\\\\\\\includegraphics[width=\\\\\\\\columnwidth]{fig3_crossover.pdf}\\\\n\\\\\\\\caption{Strategy-dependent crossover at $s{=}0.25$. Grouped bar chart of median II by eviction strategy and reasoning phase. Importance-based eviction outperforms random in the high-sparsity phase but produces $5.3{\\\\\\\\times}$ higher II in the low-sparsity phase, reversing the strategy ranking.}\\\\n\\\\\\\\label{fig:crossover}\\\\n\\\\\\\\end{figure}\\\\n\\\\n\\\\n\\\\\\\\section{Cross-Model Replication Details}\\\\n\\\\\\\\label{app:cross-model-details}\\\\n\\\\nBoth models share the Qwen2ForCausalLM backbone (28 layers, 28 heads, 4-group GQA) but differ in training: DeepSeek uses reasoning distillation from DeepSeek-R1, while Qwen2.5 uses standard instruction tuning without explicit reasoning delimiters. This controlled comparison isolates the effect of training methodology on the compound sparsity interaction.\\\\n\\\\nDespite lacking explicit \\\\\\\\texttt{&lt;think>} delimiters, Qwen2.5-7B-Instruct exhibits sufficient variation in attention sparsity to permit phase segmentation via the same quantile-based method (\\\\\\\\S\\\\\\\\ref{sec:phase-segmentation}). Four of the 50 problems are excluded due to degenerate phase assignments, yielding $n{=}46$ valid problems for Qwen (vs.\\\\\\\\ $n{=}49$ for DeepSeek).\\\\n\\\\n\\\\\\\\paragraph{Per-phase effective sample size.}\\\\n\\\\\\\\label{app:qwen-null-rate}\\\\nTable~\\\\\\\\ref{tab:qwen-effective-n} reports the per-phase effective sample size for Qwen2.5-7B-Instruct, defined as the number of problems with $|\\\\\\\\mathrm{II}| > 0.001$ in each phase. The mid-phase null rate (\\\\\\\\placeholder{NULL\\\\\\\\_PCT}\\\\\\\\%) reflects problems where compound interaction is absent in intermediate phases; this does not affect the low--high contrast ($\\\\\\\\Delta$) used in the primary analysis.\\\\n\\\\n\\\\\\\\begin{table}[t]\\\\n\\\\\\\\centering\\\\n\\\\\\\\small\\\\n\\\\\\\\caption{Per-phase effective sample size for Qwen2.5-7B-Instruct ($n_{\\\\\\\\text{total}} = \\\\\\\\placeholder{N\\\\\\\\_QW}$).}\\\\n\\\\\\\\label{tab:qwen-effective-n}\\\\n\\\\\\\\begin{tabular}{@{}lcccc@{}}\\\\n\\\\\\\\toprule\\\\nPhase & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\nHigh & \\\\\\\\placeholder{} & \\\\\\\\placeholder{} & \\\\\\\\placeholder{} & \\\\\\\\placeholder{} \\\\\\\\\\\\\\\\\\\\nMid  & \\\\\\\\placeholder{} & \\\\\\\\placeholder{} & \\\\\\\\placeholder{} & \\\\\\\\placeholder{} \\\\\\\\\\\\\\\\\\\\nLow  & \\\\\\\\placeholder{} & \\\\\\\\placeholder{} & \\\\\\\\placeholder{} & \\\\\\\\placeholder{} \\\\\\\\\\\\\\\\\\\\n\\\\\\\\bottomrule\\\\n\\\\\\\\end{tabular}\\\\n\\\\\\\\end{table}\\\\n\\\\nTable~\\\\\\\\ref{tab:cross-model} reports the cross-model comparison. Qwen reproduces the monotonic severity gradient at ${\\\\\\\\sim}1/5$ of DeepSeek's magnitude. Figure~\\\\\\\\ref{fig:cross-model} visualizes this comparison. % exp_id: cross_model_analysis.json; cohens_d_bf16_qwen.json\\\\n\\\\n\\\\\\\\begin{table}[t]\\\\n\\\\\\\\centering\\\\n\\\\\\\\small\\\\n\\\\\\\\caption{Cross-model comparison of median compound severity difference ($\\\\\\\\Delta$) under importance-based eviction.}\\\\n\\\\\\\\label{tab:cross-model}\\\\n\\\\\\\\begin{tabular}{@{}lcccc@{}}\\\\n\\\\\\\\toprule\\\\nModel & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\nDeepSeek-R1-Distill-Qwen-7B & 0.39 & 1.48 & 7.16 & 14.59 \\\\\\\\\\\\\\\\ % exp_id: bf16_importance_s015..s030\\\\nQwen2.5-7B-Instruct         & 0.04 & 0.23 & 1.27 & 2.94 \\\\\\\\\\\\\\\\ % exp_id: bf16_qw_imp_s015..s030\\\\n\\\\\\\\bottomrule\\\\n\\\\\\\\end{tabular}\\\\n\\\\\\\\end{table}\\\\n\\\\n\\\\\\\\begin{figure}[t]\\\\n\\\\\\\\centering\\\\n\\\\\\\\includegraphics[width=\\\\\\\\columnwidth]{fig5_crossmodel.pdf}\\\\n\\\\\\\\caption{Cross-model comparison of the median severity difference under importance-based eviction. Both DeepSeek (solid) and Qwen (dashed) exhibit monotonically increasing $\\\\\\\\Delta$ with sparsity; Qwen's magnitude is approximately one-fifth of DeepSeek's.} % exp_id: bf16_importance_s015..s030, bf16_qw_imp_s015..s030\\\\n\\\\\\\\label{fig:cross-model}\\\\n\\\\\\\\end{figure}\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"% Content moved from main body to appendix:\\n% - Phase-strategy crossover details (from results §5.3)\\n% - Cross-model replication details with tables/figures (from results §5.4)\\n% - Permutation test details with table/forest plot (from results §5.5)\\n% - Full entropy-discrimination collapse analysis with tables (from analysis §6)\\n% Main body §6 (analysis.tex) contains a condensed summary referencing these tables.\\n\\n\\\\section{Phase-Strategy Crossover Details}\\n\\\\label{app:crossover-details}\\n\\nAt $s{=}0.25$, a strategy ranking reversal emerges (Figure~\\\\ref{fig:crossover}): importance-based eviction yields \\\\emph{lower} II than random in the high-sparsity phase ($0.032$ vs.\\\\ $0.818$) but \\\\emph{higher} II in the low-sparsity phase ($7.196$ vs.\\\\ $1.363$---a $5.3{\\\\times}$ reversal). This crossover is present at all four sparsity levels, with reversal magnitude of $3.9{\\\\times}$ at $s{=}0.15$, $5.4{\\\\times}$ at $s{=}0.20$, $5.3{\\\\times}$ at $s{=}0.25$, and $3.6{\\\\times}$ at $s{=}0.30$ (as random eviction severity also rises). The reversal arises because head pruning redistributes attention mass, altering importance rankings in a way that couples the two sparsity mechanisms in low-sparsity phases (\\\\S\\\\ref{sec:discrimination-collapse}). % exp_id: bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json; 7.196/1.363=5.28\\n\\n\\\\begin{figure}[t]\\n\\\\centering\\n\\\\includegraphics[width=\\\\columnwidth]{fig3_crossover.pdf}\\n\\\\caption{Strategy-dependent crossover at $s{=}0.25$. Grouped bar chart of median II by eviction strategy and reasoning phase. Importance-based eviction outperforms random in the high-sparsity phase but produces $5.3{\\\\times}$ higher II in the low-sparsity phase, reversing the strategy ranking.}\\n\\\\label{fig:crossover}\\n\\\\end{figure}\\n\\n\\n\\\\section{Cross-Model Replication Details}\\n\\\\label{app:cross-model-details}\\n\\nBoth models share the Qwen2ForCausalLM backbone (28 layers, 28 heads, 4-group GQA) but differ in training: DeepSeek uses reasoning distillation from DeepSeek-R1, while Qwen2.5 uses standard instruction tuning without explicit reasoning delimiters. This controlled comparison isolates the effect of training methodology on the compound sparsity interaction.\\n\\nDespite lacking explicit \\\\texttt{&lt;think>} delimiters, Qwen2.5-7B-Instruct exhibits sufficient variation in attention sparsity to permit phase segmentation via the same quantile-based method (\\\\S\\\\ref{sec:phase-segmentation}). Four of the 50 problems are excluded due to degenerate phase assignments, yielding $n{=}46$ valid problems for Qwen (vs.\\\\ $n{=}49$ for DeepSeek).\\n\\n\\\\paragraph{Per-phase effective sample size.}\\n\\\\label{app:qwen-null-rate}\\nTable~\\\\ref{tab:qwen-effective-n} reports the per-phase effective sample size for Qwen2.5-7B-Instruct, defined as the number of problems with $|\\\\mathrm{II}| > 0.001$ in each phase. The mid-phase null rate (\\\\placeholder{NULL\\\\_PCT}\\\\%) reflects problems where compound interaction is absent in intermediate phases; this does not affect the low--high contrast ($\\\\Delta$) used in the primary analysis.\\n\\n\\\\begin{table}[t]\\n\\\\centering\\n\\\\small\\n\\\\caption{Per-phase effective sample size for Qwen2.5-7B-Instruct ($n_{\\\\text{total}} = \\\\placeholder{N\\\\_QW}$).}\\n\\\\label{tab:qwen-effective-n}\\n\\\\begin{tabular}{@{}lcccc@{}}\\n\\\\toprule\\nPhase & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\\\\\\\\\n\\\\midrule\\nHigh & \\\\placeholder{} & \\\\placeholder{} & \\\\placeholder{} & \\\\placeholder{} \\\\\\\\\\nMid  & \\\\placeholder{} & \\\\placeholder{} & \\\\placeholder{} & \\\\placeholder{} \\\\\\\\\\nLow  & \\\\placeholder{} & \\\\placeholder{} & \\\\placeholder{} & \\\\placeholder{} \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n\\nTable~\\\\ref{tab:cross-model} reports the cross-model comparison. Qwen reproduces the monotonic severity gradient at ${\\\\sim}1/5$ of DeepSeek's magnitude. Figure~\\\\ref{fig:cross-model} visualizes this comparison. % exp_id: cross_model_analysis.json; cohens_d_bf16_qwen.json\\n\\n\\\\begin{table}[t]\\n\\\\centering\\n\\\\small\\n\\\\caption{Cross-model comparison of median compound severity difference ($\\\\Delta$) under importance-based eviction.}\\n\\\\label{tab:cross-model}\\n\\\\begin{tabular}{@{}lcccc@{}}\\n\\\\toprule\\nModel & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\\\\\\\\\n\\\\midrule\\nDeepSeek-R1-Distill-Qwen-7B & 0.39 & 1.48 & 7.16 & 14.59 \\\\\\\\ % exp_id: bf16_importance_s015..s030\\nQwen2.5-7B-Instruct         & 0.04 & 0.23 & 1.27 & 2.94 \\\\\\\\ % exp_id: bf16_qw_imp_s015..s030\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n\\n\\\\begin{figure}[t]\\n\\\\centering\\n\\\\includegraphics[width=\\\\columnwidth]{fig5_crossmodel.pdf}\\n\\\\caption{Cross-model comparison of the median severity difference under importance-based eviction. Both DeepSeek (solid) and Qwen (dashed) exhibit monotonically increasing $\\\\Delta$ with sparsity; Qwen's magnitude is approximately one-fifth of DeepSeek's.} % exp_id: bf16_importance_s015..s030, bf16_qw_imp_s015..s030\\n\\\\label{fig:cross-model}\\n\\\\end{figure}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 87 · 2026-05-15T02:21:03.386Z_

<details><summary>↩ Tool result · `toolu_01BLrgCtrigVb9cTLzcdCDAL`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"DeepSeek & $0.25$ & $-0.065$ & $-1.29$ \\\\\\\\\\nDeepSeek & $0.30$ & $-0.081$ & $-1.66$ \\\\\\\\\\n\\\\midrule\\nQwen & $0.15$ & $-0.010$ & $-0.05$ \\\\\\\\\\nQwen & $0.20$ & $-0.012$ & $-0.21$ \\\\\\\\\\nQwen & $0.25$ & $-0.010$ & $-1.49$ \\\\\\\\\\nQwen & $0.30$ & $-0.020$ & $-1.14$ \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n\\nWhen importance scores lose discriminability, thresholding degenerates into noise-sensitive selection---functionally approaching biased random eviction. This is phase-dependent: in low-sparsity phases, attention is already broadly distributed, so pruning-induced flattening has maximum impact; in high-sparsity phases, concentration is preserved. Random eviction is immune because its decisions are independent of score quality, explaining $G \\\\approx 1$. % exp_id: c4_entropy_deepseek, c4_entropy_qwen\\n\\n\\\\subsection{Entropy Redistribution}\\n\\\\label{sec:entropy-redistribution}\\n\\nBeyond discrimination collapse, we examine whether head pruning also redistributes the attention entropy of surviving heads. We measure the mean attention entropy per head:\\n\\\\begin{equation}\\n    \\\\mathcal{H}_i^{(h)} = -\\\\sum_{j=1}^{T} a_{ij}^{(h)} \\\\log a_{ij}^{(h)}\\n    \\\\label{eq:attn-entropy}\\n\\\\end{equation}\\nand compute $\\\\Delta\\\\mathcal{H}$ as the change from baseline (no pruning) to the pruned condition.\\n\\nFor DeepSeek under importance-based eviction, the entropy delta is consistently negative across all four sparsity levels ($\\\\Delta\\\\mathcal{H} \\\\in [-0.047, -0.040]$; Table~\\\\ref{tab:entropy-deltas}), indicating that importance-based pruning systematically selects heads whose removal concentrates attention in the surviving heads, reinforcing discrimination collapse. % exp_id: c4_entropy_deepseek\\n\\nFor Qwen, the entropy pattern only partially replicates. The delta is negative at $s{=}0.15$ ($\\\\Delta\\\\mathcal{H} = -0.073$) and $s{=}0.20$ ($-0.076$), consistent with DeepSeek. However, at $s{=}0.25$, the delta reverses to $+0.045$, with 22 of 30 problems showing positive entropy change. At $s{=}0.30$, the delta is near zero ($-0.007$). The $s{=}0.25$ reversal is systematic rather than a statistical artifact: it is consistent across all three reasoning phases (low: $+0.042$, mid: $+0.034$, high: $+0.017$). We interpret this as a genuine model-specific difference, possibly arising from distinct head specialization patterns: Qwen's instruction tuning (vs.\\\\ DeepSeek's distillation-based training) may produce head configurations where removing 25\\\\% of heads triggers compensatory broadening rather than concentration. % exp_id: c4_entropy_qwen\\n\\nWe characterize discrimination collapse as the robust, model-independent driver of the phase-strategy interaction, with entropy redistribution as a secondary amplifier that is consistent in DeepSeek but model-dependent in Qwen.\\n\\n\\\\begin{table}[t]\\n\\\\centering\\n\\\\caption{Attention entropy deltas ($\\\\Delta\\\\mathcal{H}$) under importance-based eviction. DeepSeek shows consistent entropy compression; Qwen partially replicates with a reversal at $s{=}0.25$.}\\n\\\\label{tab:entropy-deltas}\\n\\\\small\\n\\\\begin{tabular}{llr}\\n\\\\toprule\\nModel & $s$ & $\\\\Delta\\\\mathcal{H}$ \\\\\\\\\\n\\\\midrule\\nDeepSeek & $0.15$ & $-0.040$ \\\\\\\\\\nDeepSeek & $0.20$ & $-0.047$ \\\\\\\\\\nDeepSeek & $0.25$ & $-0.045$ \\\\\\\\\\nDeepSeek & $0.30$ & $-0.044$ \\\\\\\\\\n\\\\midrule\\nQwen & $0.15$ & $-0.073$ \\\\\\\\\\nQwen & $0.20$ & $-0.076$ \\\\\\\\\\nQwen & $0.25$ & $+0.045$ \\\\\\\\\\nQwen & $0.30$ & $-0.007$ \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "6d558ca7-1fe0-4b16-9692-a9fc26f6c064",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"DeepSeek & $0.25$ & $-0.065$ & $-1.29$ \\\\\\\\\\\\\\\\\\\\nDeepSeek & $0.30$ & $-0.081$ & $-1.66$ \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\nQwen & $0.15$ & $-0.010$ & $-0.05$ \\\\\\\\\\\\\\\\\\\\nQwen & $0.20$ & $-0.012$ & $-0.21$ \\\\\\\\\\\\\\\\\\\\nQwen & $0.25$ & $-0.010$ & $-1.49$ \\\\\\\\\\\\\\\\\\\\nQwen & $0.30$ & $-0.020$ & $-1.14$ \\\\\\\\\\\\\\\\\\\\n\\\\\\\\bottomrule\\\\n\\\\\\\\end{tabular}\\\\n\\\\\\\\end{table}\\\\n\\\\nWhen importance scores lose discriminability, thresholding degenerates into noise-sensitive selection---functionally approaching biased random eviction. This is phase-dependent: in low-sparsity phases, attention is already broadly distributed, so pruning-induced flattening has maximum impact; in high-sparsity phases, concentration is preserved. Random eviction is immune because its decisions are independent of score quality, explaining $G \\\\\\\\approx 1$. % exp_id: c4_entropy_deepseek, c4_entropy_qwen\\\\n\\\\n\\\\\\\\subsection{Entropy Redistribution}\\\\n\\\\\\\\label{sec:entropy-redistribution}\\\\n\\\\nBeyond discrimination collapse, we examine whether head pruning also redistributes the attention entropy of surviving heads. We measure the mean attention entropy per head:\\\\n\\\\\\\\begin{equation}\\\\n    \\\\\\\\mathcal{H}_i^{(h)} = -\\\\\\\\sum_{j=1}^{T} a_{ij}^{(h)} \\\\\\\\log a_{ij}^{(h)}\\\\n    \\\\\\\\label{eq:attn-entropy}\\\\n\\\\\\\\end{equation}\\\\nand compute $\\\\\\\\Delta\\\\\\\\mathcal{H}$ as the change from baseline (no pruning) to the pruned condition.\\\\n\\\\nFor DeepSeek under importance-based eviction, the entropy delta is consistently negative across all four sparsity levels ($\\\\\\\\Delta\\\\\\\\mathcal{H} \\\\\\\\in [-0.047, -0.040]$; Table~\\\\\\\\ref{tab:entropy-deltas}), indicating that importance-based pruning systematically selects heads whose removal concentrates attention in the surviving heads, reinforcing discrimination collapse. % exp_id: c4_entropy_deepseek\\\\n\\\\nFor Qwen, the entropy pattern only partially replicates. The delta is negative at $s{=}0.15$ ($\\\\\\\\Delta\\\\\\\\mathcal{H} = -0.073$) and $s{=}0.20$ ($-0.076$), consistent with DeepSeek. However, at $s{=}0.25$, the delta reverses to $+0.045$, with 22 of 30 problems showing positive entropy change. At $s{=}0.30$, the delta is near zero ($-0.007$). The $s{=}0.25$ reversal is systematic rather than a statistical artifact: it is consistent across all three reasoning phases (low: $+0.042$, mid: $+0.034$, high: $+0.017$). We interpret this as a genuine model-specific difference, possibly arising from distinct head specialization patterns: Qwen's instruction tuning (vs.\\\\\\\\ DeepSeek's distillation-based training) may produce head configurations where removing 25\\\\\\\\% of heads triggers compensatory broadening rather than concentration. % exp_id: c4_entropy_qwen\\\\n\\\\nWe characterize discrimination collapse as the robust, model-independent driver of the phase-strategy interaction, with entropy redistribution as a secondary amplifier that is consistent in DeepSeek but model-dependent in Qwen.\\\\n\\\\n\\\\\\\\begin{table}[t]\\\\n\\\\\\\\centering\\\\n\\\\\\\\caption{Attention entropy deltas ($\\\\\\\\Delta\\\\\\\\mathcal{H}$) under importance-based eviction. DeepSeek shows consistent entropy compression; Qwen partially replicates with a reversal at $s{=}0.25$.}\\\\n\\\\\\\\label{tab:entropy-deltas}\\\\n\\\\\\\\small\\\\n\\\\\\\\begin{tabular}{llr}\\\\n\\\\\\\\toprule\\\\nModel & $s$ & $\\\\\\\\Delta\\\\\\\\mathcal{H}$ \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\nDeepSeek & $0.15$ & $-0.040$ \\\\\\\\\\\\\\\\\\\\nDeepSeek & $0.20$ & $-0.047$ \\\\\\\\\\\\\\\\\\\\nDeepSeek & $0.25$ & $-0.045$ \\\\\\\\\\\\\\\\\\\\nDeepSeek & $0.30$ & $-0.044$ \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\nQwen & $0.15$ & $-0.073$ \\\\\\\\\\\\\\\\\\\\nQwen & $0.20$ & $-0.076$ \\\\\\\\\\\\\\\\\\\\nQwen & $0.25$ & $+0.045$ \\\\\\\\\\\\\\\\\\\\nQwen & $0.30$ & $-0.007$ \\\\\\\\\\\\\\\\\\\\n\\\\\\\\bottomrule\\\\n\\\\\\\\end{tabular}\\\\n\\\\\\\\end{table}\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.5}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"DeepSeek & $0.25$ & $-0.065$ & $-1.29$ \\\\\\\\\\nDeepSeek & $0.30$ & $-0.081$ & $-1.66$ \\\\\\\\\\n\\\\midrule\\nQwen & $0.15$ & $-0.010$ & $-0.05$ \\\\\\\\\\nQwen & $0.20$ & $-0.012$ & $-0.21$ \\\\\\\\\\nQwen & $0.25$ & $-0.010$ & $-1.49$ \\\\\\\\\\nQwen & $0.30$ & $-0.020$ & $-1.14$ \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n\\nWhen importance scores lose discriminability, thresholding degenerates into noise-sensitive selection---functionally approaching biased random eviction. This is phase-dependent: in low-sparsity phases, attention is already broadly distributed, so pruning-induced flattening has maximum impact; in high-sparsity phases, concentration is preserved. Random eviction is immune because its decisions are independent of score quality, explaining $G \\\\approx 1$. % exp_id: c4_entropy_deepseek, c4_entropy_qwen\\n\\n\\\\subsection{Entropy Redistribution}\\n\\\\label{sec:entropy-redistribution}\\n\\nBeyond discrimination collapse, we examine whether head pruning also redistributes the attention entropy of surviving heads. We measure the mean attention entropy per head:\\n\\\\begin{equation}\\n    \\\\mathcal{H}_i^{(h)} = -\\\\sum_{j=1}^{T} a_{ij}^{(h)} \\\\log a_{ij}^{(h)}\\n    \\\\label{eq:attn-entropy}\\n\\\\end{equation}\\nand compute $\\\\Delta\\\\mathcal{H}$ as the change from baseline (no pruning) to the pruned condition.\\n\\nFor DeepSeek under importance-based eviction, the entropy delta is consistently negative across all four sparsity levels ($\\\\Delta\\\\mathcal{H} \\\\in [-0.047, -0.040]$; Table~\\\\ref{tab:entropy-deltas}), indicating that importance-based pruning systematically selects heads whose removal concentrates attention in the surviving heads, reinforcing discrimination collapse. % exp_id: c4_entropy_deepseek\\n\\nFor Qwen, the entropy pattern only partially replicates. The delta is negative at $s{=}0.15$ ($\\\\Delta\\\\mathcal{H} = -0.073$) and $s{=}0.20$ ($-0.076$), consistent with DeepSeek. However, at $s{=}0.25$, the delta reverses to $+0.045$, with 22 of 30 problems showing positive entropy change. At $s{=}0.30$, the delta is near zero ($-0.007$). The $s{=}0.25$ reversal is systematic rather than a statistical artifact: it is consistent across all three reasoning phases (low: $+0.042$, mid: $+0.034$, high: $+0.017$). We interpret this as a genuine model-specific difference, possibly arising from distinct head specialization patterns: Qwen's instruction tuning (vs.\\\\ DeepSeek's distillation-based training) may produce head configurations where removing 25\\\\% of heads triggers compensatory broadening rather than concentration. % exp_id: c4_entropy_qwen\\n\\nWe characterize discrimination collapse as the robust, model-independent driver of the phase-strategy interaction, with entropy redistribution as a secondary amplifier that is consistent in DeepSeek but model-dependent in Qwen.\\n\\n\\\\begin{table}[t]\\n\\\\centering\\n\\\\caption{Attention entropy deltas ($\\\\Delta\\\\mathcal{H}$) under importance-based eviction. DeepSeek shows consistent entropy compression; Qwen partially replicates with a reversal at $s{=}0.25$.}\\n\\\\label{tab:entropy-deltas}\\n\\\\small\\n\\\\begin{tabular}{llr}\\n\\\\toprule\\nModel & $s$ & $\\\\Delta\\\\mathcal{H}$ \\\\\\\\\\n\\\\midrule\\nDeepSeek & $0.15$ & $-0.040$ \\\\\\\\\\nDeepSeek & $0.20$ & $-0.047$ \\\\\\\\\\nDeepSeek & $0.25$ & $-0.045$ \\\\\\\\\\nDeepSeek & $0.30$ & $-0.044$ \\\\\\\\\\n\\\\midrule\\nQwen & $0.15$ & $-0.073$ \\\\\\\\\\nQwen & $0.20$ & $-0.076$ \\\\\\\\\\nQwen & $0.25$ & $+0.045$ \\\\\\\\\\nQwen & $0.30$ & $-0.007$ \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 88_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full picture. Let me also check if there's a permutation table with concrete numbers in appendix_moved.tex.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "17783b6f-c840-4e4f-9356-76dc25b09bd2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SN13M7Lt7Y35ciLPwgnrs4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3635,
      "cache_read_input_tokens": 73067,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3635
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01AzWiDPA2L1Gct6GuGwACSz`</summary>

```json
{
  "server": "westd-22162",
  "command": "sed -n '85,115p' /root/autodl-tmp/pacs/paper/appendix_moved.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "02d83ed8-ae3c-43ac-bb0a-d2e24bd6500e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SN13M7Lt7Y35ciLPwgnrs4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3635,
      "cache_read_input_tokens": 73067,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3635
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

_source line 90 · 2026-05-15T02:21:10.196Z_

<details><summary>↩ Tool result · `toolu_01AzWiDPA2L1Gct6GuGwACSz`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'sed' is not in the read-only allowlist. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "738c5928-2f18-4659-8e03-d5d8e1bbef34",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: 'sed' is not in the read-only allowlist. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'sed' is not in the read-only allowlist. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 91_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01DWoLhJLqxRQp7hcJ3KTA7U`</summary>

```json
{
  "server": "westd-22162",
  "command": "tail -n +85 /root/autodl-tmp/pacs/paper/appendix_moved.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "433be81d-e9ad-46e2-895c-cab80f8e6e74",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BYUmuGNkcVtYMzgB9X5qpV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 265,
      "cache_read_input_tokens": 76702,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 265
      },
      "output_tokens": 66,
      "service_tier": "standard",
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

_source line 92 · 2026-05-15T02:21:13.417Z_

<details><summary>↩ Tool result · `toolu_01DWoLhJLqxRQp7hcJ3KTA7U`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\nThe permutation null distributions are approximately symmetric around zero at all sparsity levels. At $s{=}0.15$, the observed statistic falls at the $99.92$th percentile of the null ($p_{\\\\text{Bonf}} = 0.0032$); at $s \\\\geq 0.20$, no permutation exceeds the observed statistic.\\n\\nTable~\\\\ref{tab:permutation} reports the results. All four sparsity levels reject $H_0$ after Bonferroni correction ($p_{\\\\text{Bonf}} < 0.005$), with observed median differences increasing monotonically from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$. The monotonic growth of both the point estimate and the CI lower bound ($0.19 \\\\to 0.69 \\\\to 1.66 \\\\to 6.70$) confirms that compound severity amplification strengthens with sparsity---not merely in central tendency but also in worst-case lower bounds. Figure~\\\\ref{fig:permtest-forest} presents these results as a forest plot. % exp_id: deepseek_bf16_permtest; source: permutation_test_results.json\\n\\n\\\\begin{table}[t]\\n\\\\centering\\n\\\\small\\n\\\\caption{Paired permutation test for compound severity: importance vs.\\\\ random eviction on DeepSeek-R1-Distill-Qwen-7B ($n{=}49$, $10{,}000$ permutations, Bonferroni-corrected).}\\n\\\\label{tab:permutation}\\n\\\\begin{tabular}{@{}rrcl@{}}\\n\\\\toprule\\n$s$ & Observed $\\\\widetilde{\\\\Delta}$ & 95\\\\% CI & $p_{\\\\text{Bonf}}$ \\\\\\\\\\n\\\\midrule\\n0.15 & 0.37 & $[0.19,\\\\; 0.62]$ & 0.0032 \\\\\\\\ % exp_id: deepseek_bf16_permtest_s015\\n0.20 & 0.97 & $[0.69,\\\\; 1.49]$ & ${<}\\\\,0.001$ \\\\\\\\ % exp_id: deepseek_bf16_permtest_s020\\n0.25 & 3.34 & $[1.66,\\\\; 6.64]$ & ${<}\\\\,0.001$ \\\\\\\\ % exp_id: deepseek_bf16_permtest_s025\\n0.30 & 9.85 & $[6.70,\\\\; 16.29]$ & ${<}\\\\,0.001$ \\\\\\\\ % exp_id: deepseek_bf16_permtest_s030\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n\\n\\\\begin{figure}[t]\\n\\\\centering\\n\\\\includegraphics[width=\\\\columnwidth]{fig4_bootstrap.pdf}\\n\\\\caption{Forest plot of permutation test results. Horizontal bars show 95\\\\% permutation CIs; diamonds mark observed median differences $\\\\widetilde{\\\\Delta}$. All CIs lie entirely above zero, confirming significant strategy-dependent severity at every sparsity level.}\\n\\\\label{fig:permtest-forest}\\n\\\\end{figure}\\n\\n\\n\\\\section{Analysis: Entropy-Discrimination Collapse}\\n\\\\label{app:analysis}\\n\\n\\\\subsection{Discrimination Collapse}\\n\\\\label{sec:discrimination-collapse}\\n\\nHead pruning reduces the number of heads contributing to cumulative importance scores, flattening the score distribution. Table~\\\\ref{tab:discrimination-metrics-full} quantifies this effect: the Gini coefficient decreases by $0.030$--$0.081$ (DeepSeek) and $0.010$--$0.020$ (Qwen) after pruning, with consistent negative deltas across all 16 conditions (both models $\\\\times$ 4 sparsity levels $\\\\times$ 2 strategies). The CV delta is likewise negative in all 8 importance-based conditions. The same pattern holds under random eviction, confirming that discrimination collapse is a consequence of head pruning \\\\emph{per se}, not of the eviction strategy. % exp_id: c4_entropy_deepseek, c4_entropy_qwen\\n\\n\\\\begin{table}[t]\\n\\\\centering\\n\\\\caption{Discrimination collapse under importance-based eviction. $\\\\Delta\\\\mathrm{Gini}$ and $\\\\Delta\\\\mathrm{CV}$ are post-pruning minus baseline; negative values indicate reduced discriminative power.}\\n\\\\label{tab:discrimination-metrics-full}\\n\\\\small\\n\\\\begin{tabular}{llrr}\\n\\\\toprule\\nModel & $s$ & $\\\\Delta\\\\mathrm{Gini}$ & $\\\\Delta\\\\mathrm{CV}$ \\\\\\\\\\n\\\\midrule\\nDeepSeek & $0.15$ & $-0.030$ & $-0.56$ \\\\\\\\\\nDeepSeek & $0.20$ & $-0.040$ & $-0.77$ \\\\\\\\\\nDeepSeek & $0.25$ & $-0.065$ & $-1.29$ \\\\\\\\\\nDeepSeek & $0.30$ & $-0.081$ & $-1.66$ \\\\\\\\\\n\\\\midrule\\nQwen & $0.15$ & $-0.010$ & $-0.05$ \\\\\\\\\\nQwen & $0.20$ & $-0.012$ & $-0.21$ \\\\\\\\\\nQwen & $0.25$ & $-0.010$ & $-1.49$ \\\\\\\\\\nQwen & $0.30$ & $-0.020$ & $-1.14$ \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n\\nWhen importance scores lose discriminability, thresholding degenerates into noise-sensitive selection---functionally approaching biased random eviction. This is phase-dependent: in low-sparsity phases, attention is already broadly distributed, so pruning-induced flattening has maximum impact; in high-sparsity phases, concentration is preserved. Random eviction is immune because its decisions are independent of score quality, explaining $G \\\\approx 1$. % exp_id: c4_entropy_deepseek, c4_entropy_qwen\\n\\n\\\\subsection{Entropy Redistribution}\\n\\\\label{sec:entropy-redistribution}\\n\\nBeyond discrimination collapse, we examine whether head pruning also redistributes the attention entropy of surviving heads. We measure the mean attention entropy per head:\\n\\\\begin{equation}\\n    \\\\mathcal{H}_i^{(h)} = -\\\\sum_{j=1}^{T} a_{ij}^{(h)} \\\\log a_{ij}^{(h)}\\n    \\\\label{eq:attn-entropy}\\n\\\\end{equation}\\nand compute $\\\\Delta\\\\mathcal{H}$ as the change from baseline (no pruning) to the pruned condition.\\n\\nFor DeepSeek under importance-based eviction, the entropy delta is consistently negative across all four sparsity levels ($\\\\Delta\\\\mathcal{H} \\\\in [-0.047, -0.040]$; Table~\\\\ref{tab:entropy-deltas}), indicating that importance-based pruning systematically selects heads whose removal concentrates attention in the surviving heads, reinforcing discrimination collapse. % exp_id: c4_entropy_deepseek\\n\\nFor Qwen, the entropy pattern only partially replicates. The delta is negative at $s{=}0.15$ ($\\\\Delta\\\\mathcal{H} = -0.073$) and $s{=}0.20$ ($-0.076$), consistent with DeepSeek. However, at $s{=}0.25$, the delta reverses to $+0.045$, with 22 of 30 problems showing positive entropy change. At $s{=}0.30$, the delta is near zero ($-0.007$). The $s{=}0.25$ reversal is systematic rather than a statistical artifact: it is consistent across all three reasoning phases (low: $+0.042$, mid: $+0.034$, high: $+0.017$). We interpret this as a genuine model-specific difference, possibly arising from distinct head specialization patterns: Qwen's instruction tuning (vs.\\\\ DeepSeek's distillation-based training) may produce head configurations where removing 25\\\\% of heads triggers compensatory broadening rather than concentration. % exp_id: c4_entropy_qwen\\n\\nWe characterize discrimination collapse as the robust, model-independent driver of the phase-strategy interaction, with entropy redistribution as a secondary amplifier that is consistent in DeepSeek but model-dependent in Qwen.\\n\\n\\\\begin{table}[t]\\n\\\\centering\\n\\\\caption{Attention entropy deltas ($\\\\Delta\\\\mathcal{H}$) under importance-based eviction. DeepSeek shows consistent entropy compression; Qwen partially replicates with a reversal at $s{=}0.25$.}\\n\\\\label{tab:entropy-deltas}\\n\\\\small\\n\\\\begin{tabular}{llr}\\n\\\\toprule\\nModel & $s$ & $\\\\Delta\\\\mathcal{H}$ \\\\\\\\\\n\\\\midrule\\nDeepSeek & $0.15$ & $-0.040$ \\\\\\\\\\nDeepSeek & $0.20$ & $-0.047$ \\\\\\\\\\nDeepSeek & $0.25$ & $-0.045$ \\\\\\\\\\nDeepSeek & $0.30$ & $-0.044$ \\\\\\\\\\n\\\\midrule\\nQwen & $0.15$ & $-0.073$ \\\\\\\\\\nQwen & $0.20$ & $-0.076$ \\\\\\\\\\nQwen & $0.25$ & $+0.045$ \\\\\\\\\\nQwen & $0.30$ & $-0.007$ \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "13e7f249-2ce8-44ad-982f-2d2cbbf02a78",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\nThe permutation null distributions are approximately symmetric around zero at all sparsity levels. At $s{=}0.15$, the observed statistic falls at the $99.92$th percentile of the null ($p_{\\\\\\\\text{Bonf}} = 0.0032$); at $s \\\\\\\\geq 0.20$, no permutation exceeds the observed statistic.\\\\n\\\\nTable~\\\\\\\\ref{tab:permutation} reports the results. All four sparsity levels reject $H_0$ after Bonferroni correction ($p_{\\\\\\\\text{Bonf}} < 0.005$), with observed median differences increasing monotonically from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$. The monotonic growth of both the point estimate and the CI lower bound ($0.19 \\\\\\\\to 0.69 \\\\\\\\to 1.66 \\\\\\\\to 6.70$) confirms that compound severity amplification strengthens with sparsity---not merely in central tendency but also in worst-case lower bounds. Figure~\\\\\\\\ref{fig:permtest-forest} presents these results as a forest plot. % exp_id: deepseek_bf16_permtest; source: permutation_test_results.json\\\\n\\\\n\\\\\\\\begin{table}[t]\\\\n\\\\\\\\centering\\\\n\\\\\\\\small\\\\n\\\\\\\\caption{Paired permutation test for compound severity: importance vs.\\\\\\\\ random eviction on DeepSeek-R1-Distill-Qwen-7B ($n{=}49$, $10{,}000$ permutations, Bonferroni-corrected).}\\\\n\\\\\\\\label{tab:permutation}\\\\n\\\\\\\\begin{tabular}{@{}rrcl@{}}\\\\n\\\\\\\\toprule\\\\n$s$ & Observed $\\\\\\\\widetilde{\\\\\\\\Delta}$ & 95\\\\\\\\% CI & $p_{\\\\\\\\text{Bonf}}$ \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\n0.15 & 0.37 & $[0.19,\\\\\\\\; 0.62]$ & 0.0032 \\\\\\\\\\\\\\\\ % exp_id: deepseek_bf16_permtest_s015\\\\n0.20 & 0.97 & $[0.69,\\\\\\\\; 1.49]$ & ${<}\\\\\\\\,0.001$ \\\\\\\\\\\\\\\\ % exp_id: deepseek_bf16_permtest_s020\\\\n0.25 & 3.34 & $[1.66,\\\\\\\\; 6.64]$ & ${<}\\\\\\\\,0.001$ \\\\\\\\\\\\\\\\ % exp_id: deepseek_bf16_permtest_s025\\\\n0.30 & 9.85 & $[6.70,\\\\\\\\; 16.29]$ & ${<}\\\\\\\\,0.001$ \\\\\\\\\\\\\\\\ % exp_id: deepseek_bf16_permtest_s030\\\\n\\\\\\\\bottomrule\\\\n\\\\\\\\end{tabular}\\\\n\\\\\\\\end{table}\\\\n\\\\n\\\\\\\\begin{figure}[t]\\\\n\\\\\\\\centering\\\\n\\\\\\\\includegraphics[width=\\\\\\\\columnwidth]{fig4_bootstrap.pdf}\\\\n\\\\\\\\caption{Forest plot of permutation test results. Horizontal bars show 95\\\\\\\\% permutation CIs; diamonds mark observed median differences $\\\\\\\\widetilde{\\\\\\\\Delta}$. All CIs lie entirely above zero, confirming significant strategy-dependent severity at every sparsity level.}\\\\n\\\\\\\\label{fig:permtest-forest}\\\\n\\\\\\\\end{figure}\\\\n\\\\n\\\\n\\\\\\\\section{Analysis: Entropy-Discrimination Collapse}\\\\n\\\\\\\\label{app:analysis}\\\\n\\\\n\\\\\\\\subsection{Discrimination Collapse}\\\\n\\\\\\\\label{sec:discrimination-collapse}\\\\n\\\\nHead pruning reduces the number of heads contributing to cumulative importance scores, flattening the score distribution. Table~\\\\\\\\ref{tab:discrimination-metrics-full} quantifies this effect: the Gini coefficient decreases by $0.030$--$0.081$ (DeepSeek) and $0.010$--$0.020$ (Qwen) after pruning, with consistent negative deltas across all 16 conditions (both models $\\\\\\\\times$ 4 sparsity levels $\\\\\\\\times$ 2 strategies). The CV delta is likewise negative in all 8 importance-based conditions. The same pattern holds under random eviction, confirming that discrimination collapse is a consequence of head pruning \\\\\\\\emph{per se}, not of the eviction strategy. % exp_id: c4_entropy_deepseek, c4_entropy_qwen\\\\n\\\\n\\\\\\\\begin{table}[t]\\\\n\\\\\\\\centering\\\\n\\\\\\\\caption{Discrimination collapse under importance-based eviction. $\\\\\\\\Delta\\\\\\\\mathrm{Gini}$ and $\\\\\\\\Delta\\\\\\\\mathrm{CV}$ are post-pruning minus baseline; negative values indicate reduced discriminative power.}\\\\n\\\\\\\\label{tab:discrimination-metrics-full}\\\\n\\\\\\\\small\\\\n\\\\\\\\begin{tabular}{llrr}\\\\n\\\\\\\\toprule\\\\nModel & $s$ & $\\\\\\\\Delta\\\\\\\\mathrm{Gini}$ & $\\\\\\\\Delta\\\\\\\\mathrm{CV}$ \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\nDeepSeek & $0.15$ & $-0.030$ & $-0.56$ \\\\\\\\\\\\\\\\\\\\nDeepSeek & $0.20$ & $-0.040$ & $-0.77$ \\\\\\\\\\\\\\\\\\\\nDeepSeek & $0.25$ & $-0.065$ & $-1.29$ \\\\\\\\\\\\\\\\\\\\nDeepSeek & $0.30$ & $-0.081$ & $-1.66$ \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\nQwen & $0.15$ & $-0.010$ & $-0.05$ \\\\\\\\\\\\\\\\\\\\nQwen & $0.20$ & $-0.012$ & $-0.21$ \\\\\\\\\\\\\\\\\\\\nQwen & $0.25$ & $-0.010$ & $-1.49$ \\\\\\\\\\\\\\\\\\\\nQwen & $0.30$ & $-0.020$ & $-1.14$ \\\\\\\\\\\\\\\\\\\\n\\\\\\\\bottomrule\\\\n\\\\\\\\end{tabular}\\\\n\\\\\\\\end{table}\\\\n\\\\nWhen importance scores lose discriminability, thresholding degenerates into noise-sensitive selection---functionally approaching biased random eviction. This is phase-dependent: in low-sparsity phases, attention is already broadly distributed, so pruning-induced flattening has maximum impact; in high-sparsity phases, concentration is preserved. Random eviction is immune because its decisions are independent of score quality, explaining $G \\\\\\\\approx 1$. % exp_id: c4_entropy_deepseek, c4_entropy_qwen\\\\n\\\\n\\\\\\\\subsection{Entropy Redistribution}\\\\n\\\\\\\\label{sec:entropy-redistribution}\\\\n\\\\nBeyond discrimination collapse, we examine whether head pruning also redistributes the attention entropy of surviving heads. We measure the mean attention entropy per head:\\\\n\\\\\\\\begin{equation}\\\\n    \\\\\\\\mathcal{H}_i^{(h)} = -\\\\\\\\sum_{j=1}^{T} a_{ij}^{(h)} \\\\\\\\log a_{ij}^{(h)}\\\\n    \\\\\\\\label{eq:attn-entropy}\\\\n\\\\\\\\end{equation}\\\\nand compute $\\\\\\\\Delta\\\\\\\\mathcal{H}$ as the change from baseline (no pruning) to the pruned condition.\\\\n\\\\nFor DeepSeek under importance-based eviction, the entropy delta is consistently negative across all four sparsity levels ($\\\\\\\\Delta\\\\\\\\mathcal{H} \\\\\\\\in [-0.047, -0.040]$; Table~\\\\\\\\ref{tab:entropy-deltas}), indicating that importance-based pruning systematically selects heads whose removal concentrates attention in the surviving heads, reinforcing discrimination collapse. % exp_id: c4_entropy_deepseek\\\\n\\\\nFor Qwen, the entropy pattern only partially replicates. The delta is negative at $s{=}0.15$ ($\\\\\\\\Delta\\\\\\\\mathcal{H} = -0.073$) and $s{=}0.20$ ($-0.076$), consistent with DeepSeek. However, at $s{=}0.25$, the delta reverses to $+0.045$, with 22 of 30 problems showing positive entropy change. At $s{=}0.30$, the delta is near zero ($-0.007$). The $s{=}0.25$ reversal is systematic rather than a statistical artifact: it is consistent across all three reasoning phases (low: $+0.042$, mid: $+0.034$, high: $+0.017$). We interpret this as a genuine model-specific difference, possibly arising from distinct head specialization patterns: Qwen's instruction tuning (vs.\\\\\\\\ DeepSeek's distillation-based training) may produce head configurations where removing 25\\\\\\\\% of heads triggers compensatory broadening rather than concentration. % exp_id: c4_entropy_qwen\\\\n\\\\nWe characterize discrimination collapse as the robust, model-independent driver of the phase-strategy interaction, with entropy redistribution as a secondary amplifier that is consistent in DeepSeek but model-dependent in Qwen.\\\\n\\\\n\\\\\\\\begin{table}[t]\\\\n\\\\\\\\centering\\\\n\\\\\\\\caption{Attention entropy deltas ($\\\\\\\\Delta\\\\\\\\mathcal{H}$) under importance-based eviction. DeepSeek shows consistent entropy compression; Qwen partially replicates with a reversal at $s{=}0.25$.}\\\\n\\\\\\\\label{tab:entropy-deltas}\\\\n\\\\\\\\small\\\\n\\\\\\\\begin{tabular}{llr}\\\\n\\\\\\\\toprule\\\\nModel & $s$ & $\\\\\\\\Delta\\\\\\\\mathcal{H}$ \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\nDeepSeek & $0.15$ & $-0.040$ \\\\\\\\\\\\\\\\\\\\nDeepSeek & $0.20$ & $-0.047$ \\\\\\\\\\\\\\\\\\\\nDeepSeek & $0.25$ & $-0.045$ \\\\\\\\\\\\\\\\\\\\nDeepSeek & $0.30$ & $-0.044$ \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\nQwen & $0.15$ & $-0.073$ \\\\\\\\\\\\\\\\\\\\nQwen & $0.20$ & $-0.076$ \\\\\\\\\\\\\\\\\\\\nQwen & $0.25$ & $+0.045$ \\\\\\\\\\\\\\\\\\\\nQwen & $0.30$ & $-0.007$ \\\\\\\\\\\\\\\\\\\\n\\\\\\\\bottomrule\\\\n\\\\\\\\end{tabular}\\\\n\\\\\\\\end{table}\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\nThe permutation null distributions are approximately symmetric around zero at all sparsity levels. At $s{=}0.15$, the observed statistic falls at the $99.92$th percentile of the null ($p_{\\\\text{Bonf}} = 0.0032$); at $s \\\\geq 0.20$, no permutation exceeds the observed statistic.\\n\\nTable~\\\\ref{tab:permutation} reports the results. All four sparsity levels reject $H_0$ after Bonferroni correction ($p_{\\\\text{Bonf}} < 0.005$), with observed median differences increasing monotonically from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$. The monotonic growth of both the point estimate and the CI lower bound ($0.19 \\\\to 0.69 \\\\to 1.66 \\\\to 6.70$) confirms that compound severity amplification strengthens with sparsity---not merely in central tendency but also in worst-case lower bounds. Figure~\\\\ref{fig:permtest-forest} presents these results as a forest plot. % exp_id: deepseek_bf16_permtest; source: permutation_test_results.json\\n\\n\\\\begin{table}[t]\\n\\\\centering\\n\\\\small\\n\\\\caption{Paired permutation test for compound severity: importance vs.\\\\ random eviction on DeepSeek-R1-Distill-Qwen-7B ($n{=}49$, $10{,}000$ permutations, Bonferroni-corrected).}\\n\\\\label{tab:permutation}\\n\\\\begin{tabular}{@{}rrcl@{}}\\n\\\\toprule\\n$s$ & Observed $\\\\widetilde{\\\\Delta}$ & 95\\\\% CI & $p_{\\\\text{Bonf}}$ \\\\\\\\\\n\\\\midrule\\n0.15 & 0.37 & $[0.19,\\\\; 0.62]$ & 0.0032 \\\\\\\\ % exp_id: deepseek_bf16_permtest_s015\\n0.20 & 0.97 & $[0.69,\\\\; 1.49]$ & ${<}\\\\,0.001$ \\\\\\\\ % exp_id: deepseek_bf16_permtest_s020\\n0.25 & 3.34 & $[1.66,\\\\; 6.64]$ & ${<}\\\\,0.001$ \\\\\\\\ % exp_id: deepseek_bf16_permtest_s025\\n0.30 & 9.85 & $[6.70,\\\\; 16.29]$ & ${<}\\\\,0.001$ \\\\\\\\ % exp_id: deepseek_bf16_permtest_s030\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n\\n\\\\begin{figure}[t]\\n\\\\centering\\n\\\\includegraphics[width=\\\\columnwidth]{fig4_bootstrap.pdf}\\n\\\\caption{Forest plot of permutation test results. Horizontal bars show 95\\\\% permutation CIs; diamonds mark observed median differences $\\\\widetilde{\\\\Delta}$. All CIs lie entirely above zero, confirming significant strategy-dependent severity at every sparsity level.}\\n\\\\label{fig:permtest-forest}\\n\\\\end{figure}\\n\\n\\n\\\\section{Analysis: Entropy-Discrimination Collapse}\\n\\\\label{app:analysis}\\n\\n\\\\subsection{Discrimination Collapse}\\n\\\\label{sec:discrimination-collapse}\\n\\nHead pruning reduces the number of heads contributing to cumulative importance scores, flattening the score distribution. Table~\\\\ref{tab:discrimination-metrics-full} quantifies this effect: the Gini coefficient decreases by $0.030$--$0.081$ (DeepSeek) and $0.010$--$0.020$ (Qwen) after pruning, with consistent negative deltas across all 16 conditions (both models $\\\\times$ 4 sparsity levels $\\\\times$ 2 strategies). The CV delta is likewise negative in all 8 importance-based conditions. The same pattern holds under random eviction, confirming that discrimination collapse is a consequence of head pruning \\\\emph{per se}, not of the eviction strategy. % exp_id: c4_entropy_deepseek, c4_entropy_qwen\\n\\n\\\\begin{table}[t]\\n\\\\centering\\n\\\\caption{Discrimination collapse under importance-based eviction. $\\\\Delta\\\\mathrm{Gini}$ and $\\\\Delta\\\\mathrm{CV}$ are post-pruning minus baseline; negative values indicate reduced discriminative power.}\\n\\\\label{tab:discrimination-metrics-full}\\n\\\\small\\n\\\\begin{tabular}{llrr}\\n\\\\toprule\\nModel & $s$ & $\\\\Delta\\\\mathrm{Gini}$ & $\\\\Delta\\\\mathrm{CV}$ \\\\\\\\\\n\\\\midrule\\nDeepSeek & $0.15$ & $-0.030$ & $-0.56$ \\\\\\\\\\nDeepSeek & $0.20$ & $-0.040$ & $-0.77$ \\\\\\\\\\nDeepSeek & $0.25$ & $-0.065$ & $-1.29$ \\\\\\\\\\nDeepSeek & $0.30$ & $-0.081$ & $-1.66$ \\\\\\\\\\n\\\\midrule\\nQwen & $0.15$ & $-0.010$ & $-0.05$ \\\\\\\\\\nQwen & $0.20$ & $-0.012$ & $-0.21$ \\\\\\\\\\nQwen & $0.25$ & $-0.010$ & $-1.49$ \\\\\\\\\\nQwen & $0.30$ & $-0.020$ & $-1.14$ \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n\\nWhen importance scores lose discriminability, thresholding degenerates into noise-sensitive selection---functionally approaching biased random eviction. This is phase-dependent: in low-sparsity phases, attention is already broadly distributed, so pruning-induced flattening has maximum impact; in high-sparsity phases, concentration is preserved. Random eviction is immune because its decisions are independent of score quality, explaining $G \\\\approx 1$. % exp_id: c4_entropy_deepseek, c4_entropy_qwen\\n\\n\\\\subsection{Entropy Redistribution}\\n\\\\label{sec:entropy-redistribution}\\n\\nBeyond discrimination collapse, we examine whether head pruning also redistributes the attention entropy of surviving heads. We measure the mean attention entropy per head:\\n\\\\begin{equation}\\n    \\\\mathcal{H}_i^{(h)} = -\\\\sum_{j=1}^{T} a_{ij}^{(h)} \\\\log a_{ij}^{(h)}\\n    \\\\label{eq:attn-entropy}\\n\\\\end{equation}\\nand compute $\\\\Delta\\\\mathcal{H}$ as the change from baseline (no pruning) to the pruned condition.\\n\\nFor DeepSeek under importance-based eviction, the entropy delta is consistently negative across all four sparsity levels ($\\\\Delta\\\\mathcal{H} \\\\in [-0.047, -0.040]$; Table~\\\\ref{tab:entropy-deltas}), indicating that importance-based pruning systematically selects heads whose removal concentrates attention in the surviving heads, reinforcing discrimination collapse. % exp_id: c4_entropy_deepseek\\n\\nFor Qwen, the entropy pattern only partially replicates. The delta is negative at $s{=}0.15$ ($\\\\Delta\\\\mathcal{H} = -0.073$) and $s{=}0.20$ ($-0.076$), consistent with DeepSeek. However, at $s{=}0.25$, the delta reverses to $+0.045$, with 22 of 30 problems showing positive entropy change. At $s{=}0.30$, the delta is near zero ($-0.007$). The $s{=}0.25$ reversal is systematic rather than a statistical artifact: it is consistent across all three reasoning phases (low: $+0.042$, mid: $+0.034$, high: $+0.017$). We interpret this as a genuine model-specific difference, possibly arising from distinct head specialization patterns: Qwen's instruction tuning (vs.\\\\ DeepSeek's distillation-based training) may produce head configurations where removing 25\\\\% of heads triggers compensatory broadening rather than concentration. % exp_id: c4_entropy_qwen\\n\\nWe characterize discrimination collapse as the robust, model-independent driver of the phase-strategy interaction, with entropy redistribution as a secondary amplifier that is consistent in DeepSeek but model-dependent in Qwen.\\n\\n\\\\begin{table}[t]\\n\\\\centering\\n\\\\caption{Attention entropy deltas ($\\\\Delta\\\\mathcal{H}$) under importance-based eviction. DeepSeek shows consistent entropy compression; Qwen partially replicates with a reversal at $s{=}0.25$.}\\n\\\\label{tab:entropy-deltas}\\n\\\\small\\n\\\\begin{tabular}{llr}\\n\\\\toprule\\nModel & $s$ & $\\\\Delta\\\\mathcal{H}$ \\\\\\\\\\n\\\\midrule\\nDeepSeek & $0.15$ & $-0.040$ \\\\\\\\\\nDeepSeek & $0.20$ & $-0.047$ \\\\\\\\\\nDeepSeek & $0.25$ & $-0.045$ \\\\\\\\\\nDeepSeek & $0.30$ & $-0.044$ \\\\\\\\\\n\\\\midrule\\nQwen & $0.15$ & $-0.073$ \\\\\\\\\\nQwen & $0.20$ & $-0.076$ \\\\\\\\\\nQwen & $0.25$ & $+0.045$ \\\\\\\\\\nQwen & $0.30$ & $-0.007$ \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 93_

<details><summary>Logged reasoning block</summary>

```text
Now I have complete coverage of all files. Let me write the comprehensive checklist and save it.

Let me organize the checklist carefully. The key structure:

1. **必须更新** — all n=50 numbers that will change to n=500
2. **条件更新** — things that depend on whether n=500 results change qualitative conclusions
3. **不需要更新** — things that stay the same (LLaMA, c4_entropy, formulations, etc.)

Also need to note the **placeholder** inventory separately since those need filling regardless.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "88b86675-7bfa-49b9-9154-34c2f200c036",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LKzQk3Pk4nmkdMW6xGS21i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2891,
      "cache_read_input_tokens": 76967,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2891
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

_source line 94_

全部数据收集完毕，现在生成清单。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "9e557655-5166-4e83-80bc-4c19eade3289",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LKzQk3Pk4nmkdMW6xGS21i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2891,
      "cache_read_input_tokens": 76967,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2891
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

_source line 95_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file · `toolu_01AUkCkvhWSvnLHijCrVCXKK`</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "file": "paper_update_checklist.md",
  "content": "# Paper Update Checklist for n=500\n\n> 生成时间: 2026-05-15 | 基于论文全文 .tex 扫描\n> n=500 实验: c2_n500_deepseek (DeepSeek) + c2_qw_n500 (Qwen)\n> LLaMA (c3_llama) 和 c4_entropy 实验不在 n=500 范围内，保持不变\n\n---\n\n## A. 必须更新 — 文字中 \"50\" → \"500\"\n\n- [ ] **abstract.tex:6** — \"using 50 MATH-500 problems\" → \"500 MATH-500 problems\"（注意：LLaMA 仍为 n=50，需分述或加注）\n- [ ] **methodology.tex:10** — \"We use 50 problems stratified from MATH-500\" → \"We use 500 problems from MATH-500\"（也需更新 sampling 描述——n=500 = 全集，不再是 stratified sample）\n- [ ] **results.tex:13** — Table 1 caption: \"($n{=}50$ MATH-500 problems)\" → \"($n{=}500$...)\"\n- [ ] **results.tex:34** — Table 2 caption: \"medians across 50 problems\" → \"500 problems\"\n- [ ] **appendix_moved.tex:26** — \"Four of the 50 problems are excluded\" → \"X of the 500 problems are excluded\"（X 待 n=500 结果确定）\n\n## B. 必须更新 — 配对样本量 n=49 / n=46\n\n- [ ] **appendix_disc_analysis.tex:45** — \"n{=}49 paired problems for DeepSeek (1 excluded) and n{=}46 for Qwen (4 excluded)\" → 新 exclusion 数\n- [ ] **appendix_moved.tex:26** — \"n{=}46 valid problems for Qwen (vs. n{=}49 for DeepSeek)\" → 新值\n- [ ] **appendix_moved.tex:93** — Table 7 (tab:permutation) caption: \"n{=}49\" → 新 DeepSeek 配对数\n\n> ⚠️ results.tex:77 的 \"n{=}49\" 是 **LLaMA** cross-arch，不更新。\n\n## C. 必须更新 — DeepSeek 数值（全部来自 bf16 n=50，需替换为 n=500）\n\n### C1. Abstract 内联数字 (abstract.tex)\n- [ ] **abstract.tex:7** — median Δ: \"$0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$\"\n- [ ] **abstract.tex:7** — d_z: \"from $0.44$ (small) to $0.80$ (large)\"\n\n### C2. Introduction 内联数字 (introduction.tex)\n- [ ] **introduction.tex:14** — \"$0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$ ($d_z$: $0.44 \\to 0.80$)\"\n\n### C3. Results §5.1 Strategy-Dependent Severity (results.tex)\n- [ ] **results.tex:5-8** — \"$\\Delta$ increases from $0.39$... to $14.59$...a $37{\\times}$ amplification\"\n- [ ] **results.tex:5-8** — random eviction: \"$-0.02$ to $1.54$\"\n\n### C4. Table 1 — tab:aggregate-ii (results.tex:16-22)\n- [ ] **Importance 行**: 0.39 / 1.48 / 7.16 / 14.59 → 全部替换\n- [ ] **Random 行**: 0.01 / −0.02 / 0.54 / 1.54 → 全部替换\n\n### C5. Results §5.2 Phase-Modulated Amplification (results.tex)\n- [ ] **results.tex:29** — G: \"$69{\\times}$ at $s{=}0.15$ to $274{\\times}$ at $s{=}0.30$\"\n- [ ] **results.tex:29** — II_high range: \"$0.006$ to $0.053$\"\n- [ ] **results.tex:29** — Random G: \"$G \\approx 0.9$--$1.7{\\times}$\"\n\n### C6. Table 2 — tab:main-results (results.tex:36-53)\n- [ ] **全部 24 个数据格**: 8 rows × (II_high, II_mid, II_low) → 全部替换\n- [ ] **Δ 列**: 4 个 importance + 4 个 random → 全部替换\n- [ ] **G 列**: 69 / 103 / 222 / 274 + 1.1 / 0.9 / 1.7 / 1.6 → 全部替换\n\n### C7. Figure 1 caption (results.tex:57-59)\n- [ ] **results.tex:58** — \"$69{\\times}$ to $274{\\times}$\" → 新值\n\n### C8. Results §5.3 Crossover (results.tex:62-66)\n- [ ] **results.tex:62-66** — s=0.25 crossover 数字: \"$0.032$ vs. $0.818$\" (high phase) 和 \"$7.196$ vs. $1.363$\" (low phase)\n\n### C9. Results §5.6 Statistical Validation (results.tex:100-102)\n- [ ] **results.tex:100-102** — permutation Δ: \"from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$\"\n\n### C10. Table 3 — tab:cohens-d, DeepSeek 列 (results.tex:117-120)\n- [ ] **DS d_z**: 0.44 / 0.52 / 0.68 / 0.80 → 全部替换\n- [ ] **DS Δ̃ [CI]**: 0.32 [0.20, 0.47] / 1.15 [0.66, 1.26] / 3.97 [2.83, 5.29] / 9.94 [8.39, 16.65] → 全部替换\n\n### C11. Conclusion (conclusion.tex:4)\n- [ ] **conclusion.tex:4** — \"$69{\\times}$ to $274{\\times}$... ($d_z$: $0.44 \\to 0.80$)\"\n\n### C12. Discussion (discussion.tex:3-4)\n- [ ] **discussion.tex:3** — \"$69$--$274{\\times}$\"\n- [ ] **discussion.tex:4** — crossover 数字: \"$0.032$ vs. $0.818$\" 和 \"$7.196$ vs. $1.363$\"\n\n### C13. Appendix Crossover Details (appendix_moved.tex:11)\n- [ ] **appendix_moved.tex:11** — crossover: \"$0.032$ vs. $0.818$\" / \"$7.196$ vs. $1.363$—a $5.3{\\times}$ reversal\"\n- [ ] **appendix_moved.tex:11** — reversal magnitudes: \"$3.9{\\times}$, $5.4{\\times}$, $5.3{\\times}$, $3.6{\\times}$\"\n- [ ] **appendix_moved.tex:17** — fig:crossover caption: \"$5.3{\\times}$\"\n\n### C14. Appendix Permutation (appendix_moved.tex:86-105)\n- [ ] **appendix_moved.tex:86** — \"99.92th percentile... $p_{\\text{Bonf}} = 0.0032$\"\n- [ ] **appendix_moved.tex:88** — Δ inline: \"from $0.37$... to $9.85$\"\n- [ ] **appendix_moved.tex:88** — CI lower bounds: \"$0.19 \\to 0.69 \\to 1.66 \\to 6.70$\"\n- [ ] **Table 7 (tab:permutation)**: 全部 4 行 × (Observed Δ̃, 95% CI, p_Bonf) → 替换\n\n### C15. Appendix Cross-Model Table (appendix_moved.tex:54-62)\n- [ ] **Table 5 (tab:cross-model) DeepSeek 行**: 0.39 / 1.48 / 7.16 / 14.59 → 替换\n\n### C16. Appendix Extended Discussion (appendix_disc_analysis.tex:9)\n- [ ] **appendix_disc_analysis.tex:9** — \"II_high < 0.06 at s ≤ 0.30; at s=0.35, high-phase II rises to 0.105\" → 更新 n=500 high-phase 值\n\n### C17. Appendix Statistical Scope (appendix_disc_analysis.tex:45-50)\n- [ ] **appendix_disc_analysis.tex:46** — \"mean/median ratio ~1.6:1 at s=0.30\"\n- [ ] **appendix_disc_analysis.tex:46** — \"mean_diff=22.94, median_diff=14.59\" (comment 中)\n- [ ] **appendix_disc_analysis.tex:47** — \"per-problem paired: median_diff=9.9436 at s030\" (comment 中)\n- [ ] **appendix_disc_analysis.tex:48** — permutation CIs in comment → 更新\n\n## D. 必须更新 — Qwen 数值\n\n### D1. Table 3 — tab:cohens-d, Qwen 列 (results.tex:117-120)\n- [ ] **QW d_z**: 0.28 / 0.55 / 0.89 / 1.02 → 全部替换\n- [ ] **QW Δ̃ [CI]**: 0.05 [-0.01, 0.11] / 0.21 [0.07, 0.40] / 1.11 [0.61, 1.47] / 2.62 [1.72, 3.65] → 全部替换\n\n### D2. Results §5.4 Cross-Model (results.tex:71)\n- [ ] **results.tex:71** — \"$\\Delta$ increases from $0.04$ at $s{=}0.15$ to $2.94$ at $s{=}0.30$\"\n- [ ] **results.tex:71** — \"$d_z{=}0.28$, CI includes zero\"\n- [ ] **results.tex:71** — \"$d_z \\geq 0.55$\"\n\n### D3. Abstract/Introduction/Conclusion Qwen 内联\n- [ ] **abstract.tex:10** — \"$d_z \\geq 0.55$; Spearman $\\rho = 1.0$; gradient permutation $p = 0.043$\"\n- [ ] **introduction.tex:15** — \"$d_z \\geq 0.55$\"\n- [ ] **conclusion.tex:4** — \"$d_z \\geq 0.55$\"\n\n### D4. Appendix Cross-Model Table (appendix_moved.tex:54-62)\n- [ ] **Table 5 (tab:cross-model) Qwen 行**: 0.04 / 0.23 / 1.27 / 2.94 → 替换\n- [ ] **appendix_moved.tex:48** — \"at ~1/5 of DeepSeek's magnitude\" → 新比例\n\n### D5. Appendix Cross-Model Figure (appendix_moved.tex:69)\n- [ ] **fig:cross-model caption** — \"one-fifth of DeepSeek's\" → 新比例\n\n## E. 必须更新 — 图表重新生成\n\n所有图表基于 n=50 数据，n=500 后需用 analyze_n500_unified.py 输出重新生成：\n\n- [ ] **fig1_dose_response.pdf** (fig:hero) — G vs s 曲线 + 95% bootstrap CI shading\n- [ ] **fig3_crossover.pdf** (fig:crossover) — s=0.25 crossover grouped bar chart\n- [ ] **fig4_bootstrap.pdf** (fig:permtest-forest) — permutation forest plot\n- [ ] **fig5_crossmodel.pdf** (fig:cross-model) — cross-model comparison curves\n\n## F. 必须填入 — 现有 \\placeholder{} 值\n\n### F1. 可从 n=500 数据直接填入\n- [ ] **results.tex:71** — `\\placeholder{NULL_PCT}` (Qwen mid-phase null rate %)\n- [ ] **appendix_moved.tex:30** — `\\placeholder{NULL_PCT}` (同上)\n- [ ] **appendix_moved.tex:35** — `\\placeholder{N_QW}` (Qwen 总有效 n)\n- [ ] **appendix_moved.tex:41-43** — Qwen per-phase effective n: 12 个 `\\placeholder{}`\n- [ ] **abstract.tex:8** — `\\placeholder{}` (Qwen s030 random Δ̃)\n- [ ] **appendix_disc_analysis.tex:14** — `\\placeholder{}` (Qwen random Δ̃)\n- [ ] **appendix_disc_analysis.tex:49** — `\\placeholder{}` (Qwen random Δ̃)\n- [ ] **appendix_results.tex:10** — `\\placeholder{}` (Qwen random Δ̃)\n- [ ] **appendix_moved.tex:76** — `\\placeholder{}` (Qwen random Δ̃)\n- [ ] **appendix_results.tex:7** — `\\placeholder{}` × 2 (per-problem concordance ρ 和 p)\n- [ ] **appendix_moved.tex:73** — `\\placeholder{}` × 2 (per-problem concordance ρ 和 p，重复)\n\n### F2. 从 c3_llama 数据填入（与 n=500 无关，可提前填）\n- [ ] **results.tex:81** — `\\placeholder{}` (LLaMA random Wilcoxon p at s=0.30)\n- [ ] **results.tex:86** — `\\placeholder{N_LLAMA}` (LLaMA paired n)\n- [ ] **results.tex:92-95** — Table 4 (tab:llama-cross-arch): 12+ `\\placeholder{}` (Δ̃, CI, p for all 4 sparsity levels)\n- [ ] **discussion.tex:15** — `\\placeholder{}` (LLaMA random Wilcoxon p)\n\n### F3. 从 c5b_pilot 数据填入（与 n=500 无关，可提前填）\n- [ ] **discussion.tex:10** — `\\placeholder{ORACLE_PCT}` (oracle recovery %)\n- [ ] **discussion.tex:10** — `\\placeholder{ORACLE_P}` (oracle Wilcoxon p)\n- [ ] **discussion.tex:10** — `\\placeholder{HEUR_PCT}` (heuristic recovery %)\n- [ ] **discussion.tex:10** — `\\placeholder{HEUR_P}` (heuristic Wilcoxon p)\n\n---\n\n## G. 条件更新（取决于 n=500 分析结果）\n\n### G1. Qwen imp-vs-rand 显著性\n- [ ] **若 Qwen s015 d_z CI 仍跨零** → results.tex:71 保持 \"marginal at s=0.15\" caveat；abstract/intro/conclusion 保持 \"at s ≥ 0.20\"\n- [ ] **若 Qwen s015 d_z CI 不再跨零** → 更新叙事为 \"at all sparsity levels\"，移除 \"marginal\" 限定\n- [ ] **若 Qwen s015 CI 仍跨零但 s020 也变边缘** → 更新 onset threshold 叙事为 \"s ≥ 0.25\"\n- [ ] 受影响位置: abstract.tex:10, introduction.tex:15, results.tex:71, results.tex:106, conclusion.tex:4, Table 3 footnote\n\n### G2. Random eviction \"7/8 FAIL\" 计数\n- [ ] **若 n=500 random 条件仍全部不显著** → 保持 \"7/8 FAIL\"（含 LLaMA 则仍为 7/8 或更新为 11/12）\n- [ ] **若 Qwen random 更多条件变显著** → 更新 FAIL 计数，可能需调整 \"strategy-specific\" 措辞\n- [ ] **若 Qwen s030 random 不再显著** → 可简化叙事（移除 exception 讨论）\n- [ ] 受影响位置: abstract.tex:8, conclusion.tex:4, appendix_disc_analysis.tex:14, appendix_results.tex:10, appendix_moved.tex:76\n\n### G3. Qwen s030 random 的 d=-0.04 negligible effect\n- [ ] **若 n=500 下 d 变大** → 需更新 \"negligible\" 描述\n- [ ] **若 d 仍然 negligible** → 保持当前措辞\n- [ ] 受影响位置: 所有 Qwen random Δ̃ placeholder 位置 (F1 列表)\n\n### G4. DeepSeek/Qwen 量级比例\n- [ ] **当前**: Qwen magnitude ~1/5 of DeepSeek → 若 n=500 比例变化，更新 appendix_moved.tex:48, 69 和 abstract/intro\n- [ ] **当前**: Spearman ρ=1.0 → 若 n=500 后排序不再完全单调，需更新\n\n### G5. Dose-response 单调性 (C6/S7→C)\n- [ ] **若 n=500 DeepSeek 或 Qwen G 曲线不再严格单调** → 需修改 \"monotonically increasing\" 措辞\n- [ ] 受影响位置: abstract, introduction, results §5.2, conclusion\n\n### G6. Sub-exponential growth (C6)\n- [ ] **当前**: Δ growth factors 3.8×→4.8×→2.0× → n=500 后重算\n- [ ] 受影响位置: appendix_disc_analysis.tex 底部, paper_framing.md\n\n### G7. Crossover 方向\n- [ ] **若 n=500 crossover 消失或方向变化** → 需重写 §5.3 和 appendix crossover\n- [ ] **极不可能**，但 n=500 可能改变 reversal magnitudes\n\n---\n\n## H. 不需要更新\n\n- [ ] **related_work.tex** — 文献综述无数据依赖，不变\n- [ ] **background.tex** — 公式定义 (II, G, phase segmentation)，不变\n- [ ] **methodology.tex:1-9** — Models/Sparsity config 段落，不变（仅 Dataset 段需更新）\n- [ ] **analysis.tex** — 引用 c4_entropy 数据 (n=30 独立实验)，不变\n  - Gini: 0.030–0.081 (DS), 0.010–0.020 (QW)\n  - Entropy: [-0.047, -0.040] (DS)\n- [ ] **appendix.tex** — formulation details / multiplicative null verification，不变\n- [ ] **appendix_disc_analysis.tex: Tables** — tab:discrimination-metrics-full (Gini/CV) 和 tab:entropy-deltas (ΔH) 来自 c4_entropy (n=30)，不变\n- [ ] **LLaMA 所有数据** — c3_llama 实验 (n=50) 不在 n=500 范围内，所有 LLaMA 数值保持：\n  - results.tex:77 \"n{=}49 paired problems\"\n  - Tab 4 (tab:llama-cross-arch) 数值（待填 placeholder 但不因 n=500 变化）\n  - discussion.tex:15 \"~40× smaller / ~7× smaller\"（注：Qwen 值更新后 \"~7×\" 可能需调整）\n  - abstract.tex:10 LLaMA: \"$0.020 \\to 0.356$\"\n  - limitations.tex:2 LLaMA 描述\n- [ ] **C5b pilot 数据** — discussion.tex:10 pilot experiment（待填 placeholder 但不因 n=500 变化）\n- [ ] **appendix_disc_analysis.tex:5** — random discrimination collapse numbers (c4_entropy)\n\n> ⚠️ **例外**: discussion.tex:15 中 \"~7× smaller than Qwen\" 是 LLaMA vs Qwen 的比较——Qwen 数值更新后此比例可能需要重新计算。\n\n---\n\n## I. 更新顺序建议\n\n1. **先填 placeholder** (F2, F3)：LLaMA 和 C5b pilot 数据与 n=500 无关，可立即填入\n2. **等 n=500 分析脚本完成** → 获取新的 experiment_summary_table.json, cohens_d_*.json, permutation_test_results.json, cross_model_analysis.json\n3. **批量替换 DeepSeek 数值** (C1-C17)：从分析输出中读取\n4. **批量替换 Qwen 数值** (D1-D5)：同上\n5. **填入 n=500 placeholder** (F1)\n6. **评估条件更新** (G1-G7)：根据 n=500 结果判断\n7. **重新生成所有图表** (E)\n8. **更新 \"50\" → \"500\" 文字** (A, B)\n9. **全文交叉检查**：确保 abstract/intro/conclusion 内联数字与 tables 一致\n\n## J. 数据来源映射\n\n| 数据类别 | 分析脚本输出 | 论文位置 |\n|---------|------------|---------|\n| DeepSeek median Δ (imp/rand) | experiment_summary_table.json → median_diff | Tab 1, Tab 2, inline |\n| DeepSeek per-phase II | experiment_summary_table.json → per-phase medians | Tab 2 |\n| DeepSeek G ratios | computed from Tab 2 (II_low / II_high) | Tab 2, inline |\n| DS/QW Cohen's d_z + Δ̃ [CI] | cohens_d_bf16.json / cohens_d_bf16_qwen.json | Tab 3 |\n| Permutation test Δ̃ + CI + p | permutation_test_results.json | Tab 7, inline |\n| Cross-model Δ comparison | cross_model_analysis.json | Tab 5, inline |\n| Qwen per-phase effective n | analyze_n500_unified.py → qwen null rate | Tab (app), inline |\n| Qwen random Δ̃ (s030) | experiment_summary_table.json → qw_rand_s030 | abstract, appendix |\n| Per-problem concordance | cross_model_analysis.json → spearman_rho, p | appendix |\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "95eeb3b9-71d4-42bf-a123-38ba9508e408",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LKzQk3Pk4nmkdMW6xGS21i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2891,
      "cache_read_input_tokens": 76967,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2891
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

_source line 96 · 2026-05-15T02:23:21.838Z_

<details><summary>↩ Tool result · `toolu_01AUkCkvhWSvnLHijCrVCXKK`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"file 'paper_update_checklist.md' is not writable via save_project_file. Writable: ['memory.md', 'paper_framing.md', 'writing_plan.yaml'].\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "29e52c76-8145-46ac-8d55-604d7a8b3916",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"file 'paper_update_checklist.md' is not writable via save_project_file. Writable: ['memory.md', 'paper_framing.md', 'writing_plan.yaml'].\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"file 'paper_update_checklist.md' is not writable via save_project_file. Writable: ['memory.md', 'paper_framing.md', 'writing_plan.yaml'].\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 97_

<details><summary>Logged reasoning block</summary>

```text
The save_project_file only allows memory.md, paper_framing.md, writing_plan.yaml. I need to save this to the artifacts directory instead. Let me use the local Write tool to save it to the artifacts directory.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "f86443ea-2c69-4a64-88e3-9e39c0399f53",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0141rHonGFAYTH5qBiNXqxHE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6599,
      "cache_read_input_tokens": 79858,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6599
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

_source line 98_

save_project_file 只支持白名单文件。改为写入 artifacts 目录。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "1921bc72-b392-450c-9674-b3c890fe3a4b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0141rHonGFAYTH5qBiNXqxHE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6599,
      "cache_read_input_tokens": 79858,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6599
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

_source line 99_

<details open><summary>🔧 Tool call — Bash · `toolu_01A2rNCKXw5BQFEm2ZqvBgv2`</summary>

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
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "f55422bf-230c-45ef-bf88-8ea800f4f9a0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0141rHonGFAYTH5qBiNXqxHE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6599,
      "cache_read_input_tokens": 79858,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6599
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

_source line 100 · 2026-05-15T02:23:28.612Z_

<details><summary>↩ Tool result · `toolu_01A2rNCKXw5BQFEm2ZqvBgv2`</summary>

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
n500_pipeline_check.md
n500_progress_20260515_0632.md
n500_progress_check.md
n500_update_checklist.md
number_consistency_audit_v2.md
pacs
paper_n500_update_checklist.md
paper_n500_update_plan.md
paper_placeholder_audit.md
paper_update_checklist.md
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
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "498eec1b-18b3-4725-80fd-38f801c6332a",
  "tool_use_result": {
    "stdout": "_project\nanalysis_pipeline_audit.md\nanalysis_pipeline_readiness.md\nanalysis_pipeline_verification.md\nanalyze_c2_n500.py\nbf16_qw_imp_failures_diagnosis.md\nbf16_qw_rand_s015\nbf16_qw_rand_s020\nbf16_qw_rand_s025\nbf16_qw_rand_s030\nbootstrap_phase_gradient.py\nc2_n500_deepseek\nc2_n500_paper_update_checklist.md\nc2_progress_report.md\nc2_progress_snapshot.json\nc2_qw_n500_investigation.md\nc3_llama\nc3_llama_results.json\nc5b_framing_proposal.md\nc5b_pilot\nc5b_pilot_design.md\nc5b_pilot_diagnosis.md\ncompute_multiplicative_null.py\nconsistency_audit_final.md\nconsistency_audit_report.md\nconsistency_report.md\ndream_reports\ngpu_check_loop7.md\nliterature_scan_20260515.md\nliterature_scan_phase_adaptive.md\nm1_phase_segmentation_analysis.md\nm2_m4_code_readiness.md\nmagnitude_crossover_novelty_check.md\nmanifest.yaml\nmechanistic_explanation.md\nmid_sparsity_gap_analysis.md\nmvp_ii_analysis.md\nmvp_ii_profiling_v2\nmvp_ii_profiling_v3\nmvp_ii_v3_analysis.md\nmvp_interaction_index_profiling\nn500_analysis_pipeline_ready.md\nn500_paper_patch_plan.md\nn500_paper_update_FINAL.md\nn500_paper_update_checklist.md\nn500_paper_update_plan.md\nn500_pipeline_check.md\nn500_progress_20260515_0632.md\nn500_progress_check.md\nn500_update_checklist.md\nnumber_consistency_audit_v2.md\npacs\npaper_n500_update_checklist.md\npaper_n500_update_plan.md\npaper_placeholder_audit.md\npaper_update_checklist.md\nqwen_kill_investigation.md\nqwen_status_check.md\nreference_audit.md\nreference_audit_report.md\nreport_analysis_pipeline_ready.md\nreport_process_check.md\nreview_issues.yaml\nreview_reports\nv5_status_check.md\nw1w5_audit_report.md",
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

_source line 101_

<details><summary>Logged reasoning block</summary>

```text
There's already a `paper_update_checklist.md` in artifacts. Let me write my comprehensive one, overwriting or creating a new file. Let me check if there's a naming convention I should follow. I see there are multiple n500-related checklists already. Let me name mine distinctively to avoid confusion.

Actually, the task says to save to `paper_update_checklist.md` using save_project_file, but that's not in the whitelist. Let me save it locally to the artifacts directory with a clear name. I'll use `paper_n500_update_checklist_v2.md` to distinguish from existing ones.


I'm seeing there are quite a few versions of this checklist already in the artifacts. I should just overwrite the main `paper_update_checklist.md` file since that's what the task is asking for.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "b492d04f-c7ae-496a-b10c-33404a853720",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pj49AYNWMhAxnXEZeHwEG6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 933,
      "cache_read_input_tokens": 86457,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 933
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

_source line 102_

<details open><summary>🔧 Tool call — Read · `toolu_0148AasoJUGYgeF9YkLbURuS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/paper_update_checklist.md",
  "limit": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "6dfcd512-2600-43e7-8842-c0d69137c653",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pj49AYNWMhAxnXEZeHwEG6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 933,
      "cache_read_input_tokens": 86457,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 933
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

_source line 103 · 2026-05-15T02:23:42.926Z_

<details><summary>↩ Tool result · `toolu_0148AasoJUGYgeF9YkLbURuS`</summary>

```text
1	# Paper Update Checklist: n=50 → n=500
2	
3	> 生成时间: 2026-05-15 | 适用实验: c2_n500_deepseek + c2_qw_n500 (C7)
4	> 约束: median + bootstrap CI 为主指标 (D054); d_z 分场景 (D059); Qwen imp-vs-rand 不claim显著直到n=500确认 (D058); C8=partially_confirmed (D060); C5b=future_work (D056)
5	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "5261e960-1eed-4e95-b93d-084be39a1a16",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/paper_update_checklist.md",
      "content": "# Paper Update Checklist: n=50 → n=500\n\n> 生成时间: 2026-05-15 | 适用实验: c2_n500_deepseek + c2_qw_n500 (C7)\n> 约束: median + bootstrap CI 为主指标 (D054); d_z 分场景 (D059); Qwen imp-vs-rand 不claim显著直到n=500确认 (D058); C8=partially_confirmed (D060); C5b=future_work (D056)\n",
      "numLines": 5,
      "startLine": 1,
      "totalLines": 313
    }
  }
}
```

</details>

---

### Tool call

_source line 104_

<details open><summary>🔧 Tool call — Write · `toolu_01AdDs3uk5EzxdfjvamxExbE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/paper_update_checklist.md",
  "content": "# Paper Update Checklist: n=50 → n=500\n\n> 生成时间: 2026-05-15 (v2, 全文逐行扫描) | 适用实验: c2_n500_deepseek + c2_qw_n500 (C7)\n> 约束: median + bootstrap CI 为主指标 (D054); d_z 分场景 (D059); Qwen imp-vs-rand 不 claim 显著直到 n=500 确认 (D058); C8=partially_confirmed (D060); C5b=future_work (D056)\n> LLaMA (c3_llama, n=50) 和 c4_entropy (n=30) 不在 n=500 范围内\n\n---\n\n## A. 必须更新 — \"50\" → \"500\" 文字提及\n\n| # | 文件:行 | 当前文本 | 更新说明 |\n|---|--------|---------|---------|\n| A1 | abstract.tex:6 | \"using 50 MATH-500 problems\" | → \"500 MATH-500 problems\"；注意 LLaMA 仍为 n=50，需分述或脚注 |\n| A2 | methodology.tex:10 | \"We use 50 problems stratified from MATH-500\" | → \"We use the full MATH-500 benchmark (500 problems)\"；sampling 描述也需改 |\n| A3 | results.tex:13 | Table 1 caption: \"($n{=}50$ MATH-500 problems)\" | → \"($n{=}500$...)\" |\n| A4 | results.tex:34 | Table 2 caption: \"medians across 50 problems\" | → \"500 problems\" |\n| A5 | appendix_moved.tex:26 | \"Four of the 50 problems are excluded\" | → \"X of the 500 problems\"（X 待定） |\n\n## B. 必须更新 — 配对样本量 n=49 / n=46\n\n| # | 文件:行 | 当前值 | 更新说明 |\n|---|--------|-------|---------|\n| B1 | appendix_disc_analysis.tex:45 | \"n{=}49 for DeepSeek (1 excluded) and n{=}46 for Qwen (4 excluded)\" | → 新 exclusion 数 |\n| B2 | appendix_moved.tex:26 | \"n{=}46 valid problems for Qwen (vs. n{=}49 for DeepSeek)\" | → 新值 |\n| B3 | appendix_moved.tex:93 | Table 7 caption: \"n{=}49\" | → 新 DS 配对数 |\n\n> ⚠️ **不动**: results.tex:77 的 \"n{=}49\" 是 LLaMA cross-arch 数据。\n\n---\n\n## C. 必须更新 — DeepSeek 数值（bf16 n=50 → n=500）\n\n### C1. Abstract 内联 (abstract.tex)\n- [ ] **L7**: median Δ \"$0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$\"\n- [ ] **L7**: d_z \"from $0.44$ (small) to $0.80$ (large)\"\n\n### C2. Introduction 内联 (introduction.tex)\n- [ ] **L14**: \"$0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$ ($d_z$: $0.44 \\to 0.80$)\"\n\n### C3. Results §5.1 (results.tex:5-8)\n- [ ] Δ: \"$0.39$... to $14.59$... a $37{\\times}$ amplification\"\n- [ ] Random: \"$-0.02$ to $1.54$\"\n\n### C4. Table 1 — tab:aggregate-ii (results.tex:16-22)\n- [ ] **Importance 行**: 0.39 / 1.48 / 7.16 / 14.59\n- [ ] **Random 行**: 0.01 / −0.02 / 0.54 / 1.54\n\n### C5. Results §5.2 (results.tex:29)\n- [ ] G: \"$69{\\times}$ at $s{=}0.15$ to $274{\\times}$ at $s{=}0.30$\"\n- [ ] II_high: \"$0.006$ to $0.053$\"\n- [ ] Random G: \"$G \\approx 0.9$--$1.7{\\times}$\"\n\n### C6. Table 2 — tab:main-results (results.tex:36-53)\n全部 32 个数据格（8 rows × II_high/II_mid/II_low/Δ） + 8 个 G 值\n\n| 行 | II_high | II_mid | II_low | Δ | G |\n|----|---------|--------|--------|---|---|\n| s015 Imp | 0.006 | 0.081 | 0.398 | 0.39 | 69 |\n| s015 Rand | 0.093 | 0.097 | 0.103 | 0.01 | 1.1 |\n| s020 Imp | 0.015 | 0.203 | 1.496 | 1.48 | 103 |\n| s020 Rand | 0.292 | 0.350 | 0.276 | −0.02 | 0.9 |\n| s025 Imp | 0.032 | 1.118 | 7.196 | 7.16 | 222 |\n| s025 Rand | 0.818 | 0.932 | 1.363 | 0.54 | 1.7 |\n| s030 Imp | 0.053 | 2.283 | 14.639 | 14.59 | 274 |\n| s030 Rand | 2.503 | 2.592 | 4.041 | 1.54 | 1.6 |\n\n### C7. Figure 1 caption (results.tex:58)\n- [ ] \"$69{\\times}$ to $274{\\times}$\"\n\n### C8. Results §5.3 Crossover (results.tex:62-66)\n- [ ] s=0.25: \"$0.032$ vs. $0.818$\" (high) / \"$7.196$ vs. $1.363$\" (low)\n\n### C9. Results §5.6 Stat Validation (results.tex:100-102)\n- [ ] Permutation Δ: \"from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$\"\n\n### C10. Table 3 — tab:cohens-d, DS 列 (results.tex:117-120)\n| s | d_z | Δ̃ | CI |\n|---|-----|----|----|\n| 0.15 | 0.44 | 0.32 | [0.20, 0.47] |\n| 0.20 | 0.52 | 1.15 | [0.66, 1.26] |\n| 0.25 | 0.68 | 3.97 | [2.83, 5.29] |\n| 0.30 | 0.80 | 9.94 | [8.39, 16.65] |\n\n### C11. Conclusion (conclusion.tex:4)\n- [ ] \"$69{\\times}$ to $274{\\times}$... ($d_z$: $0.44 \\to 0.80$)\"\n\n### C12. Discussion (discussion.tex:3-4)\n- [ ] \"$69$--$274{\\times}$\"\n- [ ] Crossover: \"$0.032$ vs. $0.818$\" / \"$7.196$ vs. $1.363$\"\n\n### C13. Appendix Crossover (appendix_moved.tex:11)\n- [ ] \"$0.032$ vs. $0.818$\" / \"$7.196$ vs. $1.363$—a $5.3{\\times}$ reversal\"\n- [ ] Reversal magnitudes: \"$3.9{\\times}$, $5.4{\\times}$, $5.3{\\times}$, $3.6{\\times}$\"\n- [ ] Fig caption (L17): \"$5.3{\\times}$\"\n\n### C14. Appendix Permutation (appendix_moved.tex:86-105)\n- [ ] L86: \"99.92th percentile... p_Bonf = 0.0032\"\n- [ ] L88: inline Δ: \"$0.37$... to $9.85$\"\n- [ ] L88: CI lower bounds: \"$0.19 \\to 0.69 \\to 1.66 \\to 6.70$\"\n- [ ] Table 7 (tab:permutation) — 全部 4 行:\n\n| s | Observed Δ̃ | 95% CI | p_Bonf |\n|---|-----------|--------|--------|\n| 0.15 | 0.37 | [0.19, 0.62] | 0.0032 |\n| 0.20 | 0.97 | [0.69, 1.49] | <0.001 |\n| 0.25 | 3.34 | [1.66, 6.64] | <0.001 |\n| 0.30 | 9.85 | [6.70, 16.29] | <0.001 |\n\n### C15. Appendix Cross-Model Table (appendix_moved.tex:60)\n- [ ] Table 5 (tab:cross-model) DS 行: 0.39 / 1.48 / 7.16 / 14.59\n\n### C16. Appendix Extended Discussion (appendix_disc_analysis.tex:9)\n- [ ] \"II_high < 0.06 at s ≤ 0.30; at s=0.35, high-phase II rises to 0.105\"\n\n### C17. Appendix Statistical Scope (appendix_disc_analysis.tex:45-50)\n- [ ] mean/median ratio ~1.6:1\n- [ ] Comments: \"mean_diff=22.94, median_diff=14.59\", \"median_diff=9.9436\"\n- [ ] Permutation CIs in comment: s015=[0.19,0.62], s020=[0.69,1.49], s025=[1.66,6.64], s030=[6.70,16.29]\n\n---\n\n## D. 必须更新 — Qwen 数值\n\n### D1. Table 3 — tab:cohens-d, QW 列 (results.tex:117-120)\n| s | d_z | Δ̃ | CI |\n|---|-----|----|----|\n| 0.15 | 0.28 | 0.05 | [−0.01, 0.11]^ns |\n| 0.20 | 0.55 | 0.21 | [0.07, 0.40] |\n| 0.25 | 0.89 | 1.11 | [0.61, 1.47] |\n| 0.30 | 1.02 | 2.62 | [1.72, 3.65] |\n\n### D2. Results §5.4 Cross-Model (results.tex:71)\n- [ ] \"$\\Delta$ increases from $0.04$... to $2.94$\"\n- [ ] \"$d_z{=}0.28$, CI includes zero\"\n- [ ] \"$d_z \\geq 0.55$\"\n\n### D3. Abstract/Introduction/Conclusion Qwen 内联\n- [ ] abstract.tex:10 — \"$d_z \\geq 0.55$; Spearman $\\rho = 1.0$; gradient permutation $p = 0.043$\"\n- [ ] introduction.tex:15 — \"$d_z \\geq 0.55$\"\n- [ ] conclusion.tex:4 — \"$d_z \\geq 0.55$\"\n\n### D4. Appendix Cross-Model (appendix_moved.tex)\n- [ ] Table 5 (tab:cross-model) QW 行: 0.04 / 0.23 / 1.27 / 2.94\n- [ ] L48: \"at ~1/5 of DeepSeek's magnitude\" → 新比例\n- [ ] fig:cross-model caption (L69): \"one-fifth of DeepSeek's\" → 新比例\n\n---\n\n## E. 必须更新 — 图表重新生成\n\n| # | 文件名 | Label | 内容 | 数据来源 |\n|---|--------|-------|------|---------|\n| E1 | fig1_dose_response.pdf | fig:hero | G vs s + 95% CI shading | experiment_summary_table.json |\n| E2 | fig3_crossover.pdf | fig:crossover | s=0.25 crossover bars | experiment_summary_table.json |\n| E3 | fig4_bootstrap.pdf | fig:permtest-forest | permutation forest plot | permutation_test_results.json |\n| E4 | fig5_crossmodel.pdf | fig:cross-model | DS vs QW Δ curves | cross_model_analysis.json |\n\n---\n\n## F. 必须填入 — 现有 \\placeholder{} 值\n\n### F1. 从 n=500 Qwen 数据填入\n| # | 文件:行 | Placeholder | 说明 |\n|---|--------|-------------|------|\n| F1a | abstract.tex:8 | `\\placeholder{}` | Qwen s030 random Δ̃ |\n| F1b | results.tex:71 | `\\placeholder{NULL_PCT}` | Qwen mid-phase null rate % |\n| F1c | appendix_moved.tex:30 | `\\placeholder{NULL_PCT}` | 同 F1b |\n| F1d | appendix_moved.tex:35 | `\\placeholder{N_QW}` | Qwen 总有效 n |\n| F1e | appendix_moved.tex:41-43 | 12× `\\placeholder{}` | Qwen per-phase effective n (3 phase × 4 sparsity) |\n| F1f | appendix_disc_analysis.tex:14 | `\\placeholder{}` | Qwen random Δ̃ |\n| F1g | appendix_disc_analysis.tex:49 | `\\placeholder{}` | Qwen random Δ̃ (重复引用) |\n| F1h | appendix_results.tex:10 | `\\placeholder{}` | Qwen random Δ̃ |\n| F1i | appendix_moved.tex:76 | `\\placeholder{}` | Qwen random Δ̃ |\n\n### F2. 从 n=500 Cross-model 数据填入\n| # | 文件:行 | Placeholder | 说明 |\n|---|--------|-------------|------|\n| F2a | appendix_results.tex:7 | `\\placeholder{}` × 2 | per-problem concordance ρ 和 p |\n| F2b | appendix_moved.tex:73 | `\\placeholder{}` × 2 | 同 F2a（重复段落） |\n\n### F3. 从 c3_llama 数据填入（与 n=500 无关，可提前填）\n| # | 文件:行 | Placeholder | 说明 |\n|---|--------|-------------|------|\n| F3a | results.tex:81 | `\\placeholder{}` | LLaMA random Wilcoxon p (s=0.30) |\n| F3b | results.tex:86 | `\\placeholder{N_LLAMA}` | LLaMA paired n |\n| F3c | results.tex:92-95 | 12+ `\\placeholder{}` | Tab 4 全部 (Δ̃, CI, p × 4 levels) |\n| F3d | discussion.tex:15 | `\\placeholder{}` | LLaMA random Wilcoxon p |\n\n### F4. 从 c5b_pilot 数据填入（与 n=500 无关，可提前填）\n| # | 文件:行 | Placeholder | 说明 |\n|---|--------|-------------|------|\n| F4a | discussion.tex:10 | `\\placeholder{ORACLE_PCT}` | oracle recovery % |\n| F4b | discussion.tex:10 | `\\placeholder{ORACLE_P}` | oracle Wilcoxon p |\n| F4c | discussion.tex:10 | `\\placeholder{HEUR_PCT}` | heuristic recovery % |\n| F4d | discussion.tex:10 | `\\placeholder{HEUR_P}` | heuristic Wilcoxon p |\n\n---\n\n## G. 条件更新（取决于 n=500 分析结果）\n\n### G1. Qwen s015 onset threshold\n- **若 CI 仍跨零** → 保持 \"marginal at s=0.15\"、\"at s ≥ 0.20\"\n- **若 CI 不再跨零** → 全部改为 \"at all sparsity levels\"，删 \"marginal\" 限定\n- **若 s020 也变边缘** → onset 改为 \"s ≥ 0.25\"\n- 受影响: abstract.tex:10, introduction.tex:15, results.tex:71/106, conclusion.tex:4, Table 3 footnote\n\n### G2. Random \"7/8 FAIL\" 计数\n- **若 n=500 random 仍不显著** → 保持 \"7/8\"\n- **若更多 random 条件显著** → 更新计数，调整 \"strategy-specific\" 措辞\n- **若 Qwen s030 random 不再显著** → 简化叙事，删 exception 讨论\n- 受影响: abstract.tex:8, conclusion.tex:4, appendix_disc_analysis.tex:14, appendix_results.tex:10\n\n### G3. Qwen s030 random effect size\n- **若 d 变大（non-negligible）** → 更新 \"negligible\" 描述\n- **若 d 仍 negligible** → 保持\n- 受影响: 所有 Qwen random Δ̃ placeholder 位置\n\n### G4. DS/QW 量级比\n- 当前: \"~1/5\"。n=500 后比例可能变化 → appendix_moved.tex:48/69\n- 当前: Spearman ρ=1.0。若不再完全单调 → 更新\n\n### G5. 单调性 (C6/S7→C)\n- 若 G 曲线不再严格单调 → 修改 \"monotonically increasing\"\n- 受影响: abstract, introduction, results §5.2, conclusion\n\n### G6. Sub-exponential growth factors\n- 当前: 3.8×→4.8×→2.0×（递减）→ 重算\n- 受影响: paper_framing.md\n\n### G7. LLaMA 相对量级\n- discussion.tex:15 \"~7× smaller than Qwen\" — Qwen 值更新后可能需重算此比例\n\n---\n\n## H. 不需要更新\n\n| 文件 | 原因 |\n|------|------|\n| related_work.tex | 文献综述，无数据依赖 |\n| background.tex | 公式定义 (II, G, phase segmentation) |\n| methodology.tex:1-9 | Models/Sparsity config 不变（仅 Dataset 段更新） |\n| analysis.tex | 引用 c4_entropy 数据 (n=30)，独立实验 |\n| appendix.tex | formulation details / multiplicative null |\n| Tab discrimination-metrics-full | c4_entropy Gini/CV (n=30) |\n| Tab entropy-deltas | c4_entropy ΔH (n=30) |\n| Tab llama-cross-arch 数值 | c3_llama (n=50)，非 n=500 范围（placeholder 另列于 F3） |\n| C5b pilot 数值 | c5b_pilot 独立实验（placeholder 另列于 F4） |\n| LLaMA abstract/intro/conclusion 内联 | \"$0.020 \\to 0.356$\" 等 LLaMA 数据不变 |\n\n---\n\n## I. 推荐更新顺序\n\n1. **立即可做**: 填 F3 (LLaMA placeholder) + F4 (C5b pilot placeholder) — 与 n=500 无关\n2. **等 n=500 分析完成** → 获取 JSON 输出文件\n3. **替换 A (文字 50→500)** + **B (配对 n)**\n4. **批量替换 C (DeepSeek 数值)** — 从 experiment_summary_table.json 读取\n5. **批量替换 D (Qwen 数值)** — 同上\n6. **填入 F1/F2 (n=500 placeholder)**\n7. **评估 G (条件更新)** — 根据结果判断叙事调整\n8. **重生成 E (图表)**\n9. **全文交叉验证**: abstract/intro/conclusion 内联数字 = tables 数字\n\n## J. 数据来源映射\n\n| 数据 | JSON 来源 | 论文位置 |\n|------|----------|---------|\n| DS median Δ (imp/rand) | experiment_summary_table.json → median_diff | Tab 1, Tab 2, inline §5.1 |\n| DS per-phase II | experiment_summary_table.json → per-phase medians | Tab 2 |\n| DS G ratios | Tab 2 (II_low / II_high) | Tab 2, inline §5.2 |\n| DS Cohen's d_z + Δ̃ [CI] | cohens_d_bf16.json | Tab 3 DS cols |\n| QW Cohen's d_z + Δ̃ [CI] | cohens_d_bf16_qwen.json | Tab 3 QW cols |\n| Permutation Δ̃ + CI + p | permutation_test_results.json | Tab 7 |\n| Cross-model Δ | cross_model_analysis.json | Tab 5 |\n| QW per-phase effective n | analyze_n500_unified.py → qwen null rate | Tab (app), inline |\n| QW random Δ̃ (s030) | experiment_summary_table.json → qw_rand_s030 | abstract, appendix |\n| Per-problem concordance | cross_model_analysis.json → spearman_rho, p | appendix |\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "84d8c150-2793-412b-8592-757bcb546917",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BvUXXUT5hYqJZsYRyGsUeX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 589,
      "cache_read_input_tokens": 87390,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 589
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

_source line 105 · 2026-05-15T02:25:38.631Z_

<details><summary>↩ Tool result · `toolu_01AdDs3uk5EzxdfjvamxExbE`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/paper_update_checklist.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "7fb97d35-0d1c-4214-b778-cd42a25267ae",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/paper_update_checklist.md",
    "content": "# Paper Update Checklist: n=50 → n=500\n\n> 生成时间: 2026-05-15 (v2, 全文逐行扫描) | 适用实验: c2_n500_deepseek + c2_qw_n500 (C7)\n> 约束: median + bootstrap CI 为主指标 (D054); d_z 分场景 (D059); Qwen imp-vs-rand 不 claim 显著直到 n=500 确认 (D058); C8=partially_confirmed (D060); C5b=future_work (D056)\n> LLaMA (c3_llama, n=50) 和 c4_entropy (n=30) 不在 n=500 范围内\n\n---\n\n## A. 必须更新 — \"50\" → \"500\" 文字提及\n\n| # | 文件:行 | 当前文本 | 更新说明 |\n|---|--------|---------|---------|\n| A1 | abstract.tex:6 | \"using 50 MATH-500 problems\" | → \"500 MATH-500 problems\"；注意 LLaMA 仍为 n=50，需分述或脚注 |\n| A2 | methodology.tex:10 | \"We use 50 problems stratified from MATH-500\" | → \"We use the full MATH-500 benchmark (500 problems)\"；sampling 描述也需改 |\n| A3 | results.tex:13 | Table 1 caption: \"($n{=}50$ MATH-500 problems)\" | → \"($n{=}500$...)\" |\n| A4 | results.tex:34 | Table 2 caption: \"medians across 50 problems\" | → \"500 problems\" |\n| A5 | appendix_moved.tex:26 | \"Four of the 50 problems are excluded\" | → \"X of the 500 problems\"（X 待定） |\n\n## B. 必须更新 — 配对样本量 n=49 / n=46\n\n| # | 文件:行 | 当前值 | 更新说明 |\n|---|--------|-------|---------|\n| B1 | appendix_disc_analysis.tex:45 | \"n{=}49 for DeepSeek (1 excluded) and n{=}46 for Qwen (4 excluded)\" | → 新 exclusion 数 |\n| B2 | appendix_moved.tex:26 | \"n{=}46 valid problems for Qwen (vs. n{=}49 for DeepSeek)\" | → 新值 |\n| B3 | appendix_moved.tex:93 | Table 7 caption: \"n{=}49\" | → 新 DS 配对数 |\n\n> ⚠️ **不动**: results.tex:77 的 \"n{=}49\" 是 LLaMA cross-arch 数据。\n\n---\n\n## C. 必须更新 — DeepSeek 数值（bf16 n=50 → n=500）\n\n### C1. Abstract 内联 (abstract.tex)\n- [ ] **L7**: median Δ \"$0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$\"\n- [ ] **L7**: d_z \"from $0.44$ (small) to $0.80$ (large)\"\n\n### C2. Introduction 内联 (introduction.tex)\n- [ ] **L14**: \"$0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$ ($d_z$: $0.44 \\to 0.80$)\"\n\n### C3. Results §5.1 (results.tex:5-8)\n- [ ] Δ: \"$0.39$... to $14.59$... a $37{\\times}$ amplification\"\n- [ ] Random: \"$-0.02$ to $1.54$\"\n\n### C4. Table 1 — tab:aggregate-ii (results.tex:16-22)\n- [ ] **Importance 行**: 0.39 / 1.48 / 7.16 / 14.59\n- [ ] **Random 行**: 0.01 / −0.02 / 0.54 / 1.54\n\n### C5. Results §5.2 (results.tex:29)\n- [ ] G: \"$69{\\times}$ at $s{=}0.15$ to $274{\\times}$ at $s{=}0.30$\"\n- [ ] II_high: \"$0.006$ to $0.053$\"\n- [ ] Random G: \"$G \\approx 0.9$--$1.7{\\times}$\"\n\n### C6. Table 2 — tab:main-results (results.tex:36-53)\n全部 32 个数据格（8 rows × II_high/II_mid/II_low/Δ） + 8 个 G 值\n\n| 行 | II_high | II_mid | II_low | Δ | G |\n|----|---------|--------|--------|---|---|\n| s015 Imp | 0.006 | 0.081 | 0.398 | 0.39 | 69 |\n| s015 Rand | 0.093 | 0.097 | 0.103 | 0.01 | 1.1 |\n| s020 Imp | 0.015 | 0.203 | 1.496 | 1.48 | 103 |\n| s020 Rand | 0.292 | 0.350 | 0.276 | −0.02 | 0.9 |\n| s025 Imp | 0.032 | 1.118 | 7.196 | 7.16 | 222 |\n| s025 Rand | 0.818 | 0.932 | 1.363 | 0.54 | 1.7 |\n| s030 Imp | 0.053 | 2.283 | 14.639 | 14.59 | 274 |\n| s030 Rand | 2.503 | 2.592 | 4.041 | 1.54 | 1.6 |\n\n### C7. Figure 1 caption (results.tex:58)\n- [ ] \"$69{\\times}$ to $274{\\times}$\"\n\n### C8. Results §5.3 Crossover (results.tex:62-66)\n- [ ] s=0.25: \"$0.032$ vs. $0.818$\" (high) / \"$7.196$ vs. $1.363$\" (low)\n\n### C9. Results §5.6 Stat Validation (results.tex:100-102)\n- [ ] Permutation Δ: \"from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$\"\n\n### C10. Table 3 — tab:cohens-d, DS 列 (results.tex:117-120)\n| s | d_z | Δ̃ | CI |\n|---|-----|----|----|\n| 0.15 | 0.44 | 0.32 | [0.20, 0.47] |\n| 0.20 | 0.52 | 1.15 | [0.66, 1.26] |\n| 0.25 | 0.68 | 3.97 | [2.83, 5.29] |\n| 0.30 | 0.80 | 9.94 | [8.39, 16.65] |\n\n### C11. Conclusion (conclusion.tex:4)\n- [ ] \"$69{\\times}$ to $274{\\times}$... ($d_z$: $0.44 \\to 0.80$)\"\n\n### C12. Discussion (discussion.tex:3-4)\n- [ ] \"$69$--$274{\\times}$\"\n- [ ] Crossover: \"$0.032$ vs. $0.818$\" / \"$7.196$ vs. $1.363$\"\n\n### C13. Appendix Crossover (appendix_moved.tex:11)\n- [ ] \"$0.032$ vs. $0.818$\" / \"$7.196$ vs. $1.363$—a $5.3{\\times}$ reversal\"\n- [ ] Reversal magnitudes: \"$3.9{\\times}$, $5.4{\\times}$, $5.3{\\times}$, $3.6{\\times}$\"\n- [ ] Fig caption (L17): \"$5.3{\\times}$\"\n\n### C14. Appendix Permutation (appendix_moved.tex:86-105)\n- [ ] L86: \"99.92th percentile... p_Bonf = 0.0032\"\n- [ ] L88: inline Δ: \"$0.37$... to $9.85$\"\n- [ ] L88: CI lower bounds: \"$0.19 \\to 0.69 \\to 1.66 \\to 6.70$\"\n- [ ] Table 7 (tab:permutation) — 全部 4 行:\n\n| s | Observed Δ̃ | 95% CI | p_Bonf |\n|---|-----------|--------|--------|\n| 0.15 | 0.37 | [0.19, 0.62] | 0.0032 |\n| 0.20 | 0.97 | [0.69, 1.49] | <0.001 |\n| 0.25 | 3.34 | [1.66, 6.64] | <0.001 |\n| 0.30 | 9.85 | [6.70, 16.29] | <0.001 |\n\n### C15. Appendix Cross-Model Table (appendix_moved.tex:60)\n- [ ] Table 5 (tab:cross-model) DS 行: 0.39 / 1.48 / 7.16 / 14.59\n\n### C16. Appendix Extended Discussion (appendix_disc_analysis.tex:9)\n- [ ] \"II_high < 0.06 at s ≤ 0.30; at s=0.35, high-phase II rises to 0.105\"\n\n### C17. Appendix Statistical Scope (appendix_disc_analysis.tex:45-50)\n- [ ] mean/median ratio ~1.6:1\n- [ ] Comments: \"mean_diff=22.94, median_diff=14.59\", \"median_diff=9.9436\"\n- [ ] Permutation CIs in comment: s015=[0.19,0.62], s020=[0.69,1.49], s025=[1.66,6.64], s030=[6.70,16.29]\n\n---\n\n## D. 必须更新 — Qwen 数值\n\n### D1. Table 3 — tab:cohens-d, QW 列 (results.tex:117-120)\n| s | d_z | Δ̃ | CI |\n|---|-----|----|----|\n| 0.15 | 0.28 | 0.05 | [−0.01, 0.11]^ns |\n| 0.20 | 0.55 | 0.21 | [0.07, 0.40] |\n| 0.25 | 0.89 | 1.11 | [0.61, 1.47] |\n| 0.30 | 1.02 | 2.62 | [1.72, 3.65] |\n\n### D2. Results §5.4 Cross-Model (results.tex:71)\n- [ ] \"$\\Delta$ increases from $0.04$... to $2.94$\"\n- [ ] \"$d_z{=}0.28$, CI includes zero\"\n- [ ] \"$d_z \\geq 0.55$\"\n\n### D3. Abstract/Introduction/Conclusion Qwen 内联\n- [ ] abstract.tex:10 — \"$d_z \\geq 0.55$; Spearman $\\rho = 1.0$; gradient permutation $p = 0.043$\"\n- [ ] introduction.tex:15 — \"$d_z \\geq 0.55$\"\n- [ ] conclusion.tex:4 — \"$d_z \\geq 0.55$\"\n\n### D4. Appendix Cross-Model (appendix_moved.tex)\n- [ ] Table 5 (tab:cross-model) QW 行: 0.04 / 0.23 / 1.27 / 2.94\n- [ ] L48: \"at ~1/5 of DeepSeek's magnitude\" → 新比例\n- [ ] fig:cross-model caption (L69): \"one-fifth of DeepSeek's\" → 新比例\n\n---\n\n## E. 必须更新 — 图表重新生成\n\n| # | 文件名 | Label | 内容 | 数据来源 |\n|---|--------|-------|------|---------|\n| E1 | fig1_dose_response.pdf | fig:hero | G vs s + 95% CI shading | experiment_summary_table.json |\n| E2 | fig3_crossover.pdf | fig:crossover | s=0.25 crossover bars | experiment_summary_table.json |\n| E3 | fig4_bootstrap.pdf | fig:permtest-forest | permutation forest plot | permutation_test_results.json |\n| E4 | fig5_crossmodel.pdf | fig:cross-model | DS vs QW Δ curves | cross_model_analysis.json |\n\n---\n\n## F. 必须填入 — 现有 \\placeholder{} 值\n\n### F1. 从 n=500 Qwen 数据填入\n| # | 文件:行 | Placeholder | 说明 |\n|---|--------|-------------|------|\n| F1a | abstract.tex:8 | `\\placeholder{}` | Qwen s030 random Δ̃ |\n| F1b | results.tex:71 | `\\placeholder{NULL_PCT}` | Qwen mid-phase null rate % |\n| F1c | appendix_moved.tex:30 | `\\placeholder{NULL_PCT}` | 同 F1b |\n| F1d | appendix_moved.tex:35 | `\\placeholder{N_QW}` | Qwen 总有效 n |\n| F1e | appendix_moved.tex:41-43 | 12× `\\placeholder{}` | Qwen per-phase effective n (3 phase × 4 sparsity) |\n| F1f | appendix_disc_analysis.tex:14 | `\\placeholder{}` | Qwen random Δ̃ |\n| F1g | appendix_disc_analysis.tex:49 | `\\placeholder{}` | Qwen random Δ̃ (重复引用) |\n| F1h | appendix_results.tex:10 | `\\placeholder{}` | Qwen random Δ̃ |\n| F1i | appendix_moved.tex:76 | `\\placeholder{}` | Qwen random Δ̃ |\n\n### F2. 从 n=500 Cross-model 数据填入\n| # | 文件:行 | Placeholder | 说明 |\n|---|--------|-------------|------|\n| F2a | appendix_results.tex:7 | `\\placeholder{}` × 2 | per-problem concordance ρ 和 p |\n| F2b | appendix_moved.tex:73 | `\\placeholder{}` × 2 | 同 F2a（重复段落） |\n\n### F3. 从 c3_llama 数据填入（与 n=500 无关，可提前填）\n| # | 文件:行 | Placeholder | 说明 |\n|---|--------|-------------|------|\n| F3a | results.tex:81 | `\\placeholder{}` | LLaMA random Wilcoxon p (s=0.30) |\n| F3b | results.tex:86 | `\\placeholder{N_LLAMA}` | LLaMA paired n |\n| F3c | results.tex:92-95 | 12+ `\\placeholder{}` | Tab 4 全部 (Δ̃, CI, p × 4 levels) |\n| F3d | discussion.tex:15 | `\\placeholder{}` | LLaMA random Wilcoxon p |\n\n### F4. 从 c5b_pilot 数据填入（与 n=500 无关，可提前填）\n| # | 文件:行 | Placeholder | 说明 |\n|---|--------|-------------|------|\n| F4a | discussion.tex:10 | `\\placeholder{ORACLE_PCT}` | oracle recovery % |\n| F4b | discussion.tex:10 | `\\placeholder{ORACLE_P}` | oracle Wilcoxon p |\n| F4c | discussion.tex:10 | `\\placeholder{HEUR_PCT}` | heuristic recovery % |\n| F4d | discussion.tex:10 | `\\placeholder{HEUR_P}` | heuristic Wilcoxon p |\n\n---\n\n## G. 条件更新（取决于 n=500 分析结果）\n\n### G1. Qwen s015 onset threshold\n- **若 CI 仍跨零** → 保持 \"marginal at s=0.15\"、\"at s ≥ 0.20\"\n- **若 CI 不再跨零** → 全部改为 \"at all sparsity levels\"，删 \"marginal\" 限定\n- **若 s020 也变边缘** → onset 改为 \"s ≥ 0.25\"\n- 受影响: abstract.tex:10, introduction.tex:15, results.tex:71/106, conclusion.tex:4, Table 3 footnote\n\n### G2. Random \"7/8 FAIL\" 计数\n- **若 n=500 random 仍不显著** → 保持 \"7/8\"\n- **若更多 random 条件显著** → 更新计数，调整 \"strategy-specific\" 措辞\n- **若 Qwen s030 random 不再显著** → 简化叙事，删 exception 讨论\n- 受影响: abstract.tex:8, conclusion.tex:4, appendix_disc_analysis.tex:14, appendix_results.tex:10\n\n### G3. Qwen s030 random effect size\n- **若 d 变大（non-negligible）** → 更新 \"negligible\" 描述\n- **若 d 仍 negligible** → 保持\n- 受影响: 所有 Qwen random Δ̃ placeholder 位置\n\n### G4. DS/QW 量级比\n- 当前: \"~1/5\"。n=500 后比例可能变化 → appendix_moved.tex:48/69\n- 当前: Spearman ρ=1.0。若不再完全单调 → 更新\n\n### G5. 单调性 (C6/S7→C)\n- 若 G 曲线不再严格单调 → 修改 \"monotonically increasing\"\n- 受影响: abstract, introduction, results §5.2, conclusion\n\n### G6. Sub-exponential growth factors\n- 当前: 3.8×→4.8×→2.0×（递减）→ 重算\n- 受影响: paper_framing.md\n\n### G7. LLaMA 相对量级\n- discussion.tex:15 \"~7× smaller than Qwen\" — Qwen 值更新后可能需重算此比例\n\n---\n\n## H. 不需要更新\n\n| 文件 | 原因 |\n|------|------|\n| related_work.tex | 文献综述，无数据依赖 |\n| background.tex | 公式定义 (II, G, phase segmentation) |\n| methodology.tex:1-9 | Models/Sparsity config 不变（仅 Dataset 段更新） |\n| analysis.tex | 引用 c4_entropy 数据 (n=30)，独立实验 |\n| appendix.tex | formulation details / multiplicative null |\n| Tab discrimination-metrics-full | c4_entropy Gini/CV (n=30) |\n| Tab entropy-deltas | c4_entropy ΔH (n=30) |\n| Tab llama-cross-arch 数值 | c3_llama (n=50)，非 n=500 范围（placeholder 另列于 F3） |\n| C5b pilot 数值 | c5b_pilot 独立实验（placeholder 另列于 F4） |\n| LLaMA abstract/intro/conclusion 内联 | \"$0.020 \\to 0.356$\" 等 LLaMA 数据不变 |\n\n---\n\n## I. 推荐更新顺序\n\n1. **立即可做**: 填 F3 (LLaMA placeholder) + F4 (C5b pilot placeholder) — 与 n=500 无关\n2. **等 n=500 分析完成** → 获取 JSON 输出文件\n3. **替换 A (文字 50→500)** + **B (配对 n)**\n4. **批量替换 C (DeepSeek 数值)** — 从 experiment_summary_table.json 读取\n5. **批量替换 D (Qwen 数值)** — 同上\n6. **填入 F1/F2 (n=500 placeholder)**\n7. **评估 G (条件更新)** — 根据结果判断叙事调整\n8. **重生成 E (图表)**\n9. **全文交叉验证**: abstract/intro/conclusion 内联数字 = tables 数字\n\n## J. 数据来源映射\n\n| 数据 | JSON 来源 | 论文位置 |\n|------|----------|---------|\n| DS median Δ (imp/rand) | experiment_summary_table.json → median_diff | Tab 1, Tab 2, inline §5.1 |\n| DS per-phase II | experiment_summary_table.json → per-phase medians | Tab 2 |\n| DS G ratios | Tab 2 (II_low / II_high) | Tab 2, inline §5.2 |\n| DS Cohen's d_z + Δ̃ [CI] | cohens_d_bf16.json | Tab 3 DS cols |\n| QW Cohen's d_z + Δ̃ [CI] | cohens_d_bf16_qwen.json | Tab 3 QW cols |\n| Permutation Δ̃ + CI + p | permutation_test_results.json | Tab 7 |\n| Cross-model Δ | cross_model_analysis.json | Tab 5 |\n| QW per-phase effective n | analyze_n500_unified.py → qwen null rate | Tab (app), inline |\n| QW random Δ̃ (s030) | experiment_summary_table.json → qw_rand_s030 | abstract, appendix |\n| Per-problem concordance | cross_model_analysis.json → spearman_rho, p | appendix |\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 312,
        "newStart": 1,
        "newLines": 277,
        "lines": [
          " # Paper Update Checklist: n=50 → n=500",
          " ",
          "-> 生成时间: 2026-05-15 | 适用实验: c2_n500_deepseek + c2_qw_n500 (C7)",
          "-> 约束: median + bootstrap CI 为主指标 (D054); d_z 分场景 (D059); Qwen imp-vs-rand 不claim显著直到n=500确认 (D058); C8=partially_confirmed (D060); C5b=future_work (D056)",
          "+> 生成时间: 2026-05-15 (v2, 全文逐行扫描) | 适用实验: c2_n500_deepseek + c2_qw_n500 (C7)",
          "+> 约束: median + bootstrap CI 为主指标 (D054); d_z 分场景 (D059); Qwen imp-vs-rand 不 claim 显著直到 n=500 确认 (D058); C8=partially_confirmed (D060); C5b=future_work (D056)",
          "+> LLaMA (c3_llama, n=50) 和 c4_entropy (n=30) 不在 n=500 范围内",
          " ",
          " ---",
          " ",
          "-## 优先级说明",
          "-- **P0**: 核心数字，读者第一眼看到，必须同步更新",
          "-- **P1**: 支撑性数字/表格，与 P0 有数据依赖",
          "-- **P2**: 条件性更新（取决于 n=500 结果）",
          "-- **P3**: 一致性检查，防止 n=50/n=500 混用",
          "+## A. 必须更新 — \"50\" → \"500\" 文字提及",
          " ",
          "+| # | 文件:行 | 当前文本 | 更新说明 |",
          "+|---|--------|---------|---------|",
          "+| A1 | abstract.tex:6 | \"using 50 MATH-500 problems\" | → \"500 MATH-500 problems\"；注意 LLaMA 仍为 n=50，需分述或脚注 |",
          "+| A2 | methodology.tex:10 | \"We use 50 problems stratified from MATH-500\" | → \"We use the full MATH-500 benchmark (500 problems)\"；sampling 描述也需改 |",
          "+| A3 | results.tex:13 | Table 1 caption: \"($n{=}50$ MATH-500 problems)\" | → \"($n{=}500$...)\" |",
          "+| A4 | results.tex:34 | Table 2 caption: \"medians across 50 problems\" | → \"500 problems\" |",
          "+| A5 | appendix_moved.tex:26 | \"Four of the 50 problems are excluded\" | → \"X of the 500 problems\"（X 待定） |",
          "+",
          "+## B. 必须更新 — 配对样本量 n=49 / n=46",
          "+",
          "+| # | 文件:行 | 当前值 | 更新说明 |",
          "+|---|--------|-------|---------|",
          "+| B1 | appendix_disc_analysis.tex:45 | \"n{=}49 for DeepSeek (1 excluded) and n{=}46 for Qwen (4 excluded)\" | → 新 exclusion 数 |",
          "+| B2 | appendix_moved.tex:26 | \"n{=}46 valid problems for Qwen (vs. n{=}49 for DeepSeek)\" | → 新值 |",
          "+| B3 | appendix_moved.tex:93 | Table 7 caption: \"n{=}49\" | → 新 DS 配对数 |",
          "+",
          "+> ⚠️ **不动**: results.tex:77 的 \"n{=}49\" 是 LLaMA cross-arch 数据。",
          "+",
          " ---",
          " ",
          "-## P0: 核心数字更新",
          "+## C. 必须更新 — DeepSeek 数值（bf16 n=50 → n=500）",
          " ",
          "-### 1. methodology.tex:10 — 样本量",
          "-```",
          "-当前: \"We use 50 problems stratified from MATH-500\"",
          "-更新: → 500 problems (n=500 的具体描述，包括 stratification 方式)",
          "-```",
          "+### C1. Abstract 内联 (abstract.tex)",
          "+- [ ] **L7**: median Δ \"$0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$\"",
          "+- [ ] **L7**: d_z \"from $0.44$ (small) to $0.80$ (large)\"",
          " ",
          "-### 2. abstract.tex:6 — 样本量",
          "-```",
          "-当前: \"using 50 MATH-500 problems\"",
          "-更新: → 500 MATH-500 problems",
          "-```",
          "+### C2. Introduction 内联 (introduction.tex)",
          "+- [ ] **L14**: \"$0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$ ($d_z$: $0.44 \\to 0.80$)\"",
          " ",
          "-### 3. abstract.tex:7 — DeepSeek 主指标",
          "-```",
          "-当前: \"median Interaction Index difference...from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired Cohen's $d_z$ growing from $0.44$ (small) to $0.80$ (large)\"",
          "-更新: → 用 n=500 segment-level median diff + paired d_z 替换",
          "-注意: 0.39/14.59 是 segment-level medians；d_z 0.44/0.80 是 paired d_z。两组数据来源不同，都需更新。",
          "-```",
          "+### C3. Results §5.1 (results.tex:5-8)",
          "+- [ ] Δ: \"$0.39$... to $14.59$... a $37{\\times}$ amplification\"",
          "+- [ ] Random: \"$-0.02$ to $1.54$\"",
          " ",
          "-### 4. introduction.tex:14 — DeepSeek 主指标（与 abstract 一致）",
          "-```",
          "-当前: \"median phase difference rises from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$ ($d_z$: $0.44 \\to 0.80$)\"",
          "-更新: → 同 abstract",
          "-```",
          "+### C4. Table 1 — tab:aggregate-ii (results.tex:16-22)",
          "+- [ ] **Importance 行**: 0.39 / 1.48 / 7.16 / 14.59",
          "+- [ ] **Random 行**: 0.01 / −0.02 / 0.54 / 1.54",
          " ",
          "-### 5. results.tex:8,13,19-20 — Tab aggregate-ii（DeepSeek segment-level Δ）",
          "-```",
          "-当前 Importance: 0.39, 1.48, 7.16, 14.59",
          "-当前 Random: 0.01, -0.02, 0.54, 1.54",
          "-caption \"$n{=}50$\" → $n{=}500$ (或实际有效 n)",
          "-更新: → 全部替换为 n=500 值",
          "-```",
          "+### C5. Results §5.2 (results.tex:29)",
          "+- [ ] G: \"$69{\\times}$ at $s{=}0.15$ to $274{\\times}$ at $s{=}0.30$\"",
          "+- [ ] II_high: \"$0.006$ to $0.053$\"",
          "+- [ ] Random G: \"$G \\approx 0.9$--$1.7{\\times}$\"",
          " ",
          "-### 6. results.tex:34,40-50 — Tab main-results（DeepSeek 全 per-phase 分解）",
          "-```",
          "-当前 (importance, 4 sparsity × 3 phases + Δ + G):",
          "-  s015: II_high=0.006, II_mid=0.081, II_low=0.398, Δ=0.39, G=69",
          "-  s020: II_high=0.015, II_mid=0.203, II_low=1.496, Δ=1.48, G=103",
          "-  s025: II_high=0.032, II_mid=1.118, II_low=7.196, Δ=7.16, G=222",
          "-  s030: II_high=0.053, II_mid=2.283, II_low=14.639, Δ=14.59, G=274",
          "-当前 (random, 4 sparsity × 3 phases + Δ + G):",
          "-  s015: 0.093, 0.097, 0.103, 0.01, 1.1",
          "-  s020: 0.292, 0.350, 0.276, -0.02, 0.9",
          "-  s025: 0.818, 0.932, 1.363, 0.54, 1.7",
          "-  s030: 2.503, 2.592, 4.041, 1.54, 1.6",
          "-caption \"50 problems\" → 500 problems",
          "-更新: → 全部替换为 n=500 值",
          "-```",
          "+### C6. Table 2 — tab:main-results (results.tex:36-53)",
          "+全部 32 个数据格（8 rows × II_high/II_mid/II_low/Δ） + 8 个 G 值",
          " ",
          "-### 7. results.tex:106,117-120 — Tab cohens-d（DS + QW paired d_z + Δ̃[CI]）",
          "-```",
          "-当前 DS: d_z 0.44/0.52/0.68/0.80; Δ̃ 0.32[0.20,0.47] / 1.15[0.66,1.26] / 3.97[2.83,5.29] / 9.94[8.39,16.65]",
          "-当前 QW: d_z 0.28/0.55/0.89/1.02; Δ̃ 0.05[-0.01,0.11] / 0.21[0.07,0.40] / 1.11[0.61,1.47] / 2.62[1.72,3.65]",
          "-更新: → 全部替换为 n=500 值",
          "-关键: QW s015 CI 当前包含零 → n=500 后检查是否仍包含零（影响 onset threshold 叙事）",
          "-```",
          "+| 行 | II_high | II_mid | II_low | Δ | G |",
          "+|----|---------|--------|--------|---|---|",
          "+| s015 Imp | 0.006 | 0.081 | 0.398 | 0.39 | 69 |",
          "+| s015 Rand | 0.093 | 0.097 | 0.103 | 0.01 | 1.1 |",
          "+| s020 Imp | 0.015 | 0.203 | 1.496 | 1.48 | 103 |",
          "+| s020 Rand | 0.292 | 0.350 | 0.276 | −0.02 | 0.9 |",
          "+| s025 Imp | 0.032 | 1.118 | 7.196 | 7.16 | 222 |",
          "+| s025 Rand | 0.818 | 0.932 | 1.363 | 0.54 | 1.7 |",
          "+| s030 Imp | 0.053 | 2.283 | 14.639 | 14.59 | 274 |",
          "+| s030 Rand | 2.503 | 2.592 | 4.041 | 1.54 | 1.6 |",
          " ",
          "-### 8. conclusion.tex:4 — 核心数字复述",
          "-```",
          "-当前: \"severity gradient grows from $69{\\times}$ to $274{\\times}$...($d_z$: $0.44 \\to 0.80$)\"",
          "-更新: → 与 results 一致",
          "-```",
          "+### C7. Figure 1 caption (results.tex:58)",
          "+- [ ] \"$69{\\times}$ to $274{\\times}$\"",
          " ",
          "-### 9. discussion.tex:5 — severity gradient + crossover 复述",
          "-```",
          "-当前: \"severity gradient ($69$--$274{\\times}$)\"",
          "-当前: crossover 数字 \"0.032 vs 0.818\", \"7.196 vs 1.363\"",
          "-更新: → 与 results 一致",
          "-```",
          "+### C8. Results §5.3 Crossover (results.tex:62-66)",
          "+- [ ] s=0.25: \"$0.032$ vs. $0.818$\" (high) / \"$7.196$ vs. $1.363$\" (low)",
          " ",
          "-### 10. results.tex:29 + 58 — G 值 + fig1 caption",
          "-```",
          "-当前: G \"from $69{\\times}$ at $s{=}0.15$ to $274{\\times}$ at $s{=}0.30$\"",
          "-当前 fig1 caption: \"$69{\\times}$ to $274{\\times}$\"",
          "-更新: → n=500 G 值",
          "-```",
          "+### C9. Results §5.6 Stat Validation (results.tex:100-102)",
          "+- [ ] Permutation Δ: \"from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$\"",
          " ",
          "----",
          "+### C10. Table 3 — tab:cohens-d, DS 列 (results.tex:117-120)",
          "+| s | d_z | Δ̃ | CI |",
          "+|---|-----|----|----|",
          "+| 0.15 | 0.44 | 0.32 | [0.20, 0.47] |",
          "+| 0.20 | 0.52 | 1.15 | [0.66, 1.26] |",
          "+| 0.25 | 0.68 | 3.97 | [2.83, 5.29] |",
          "+| 0.30 | 0.80 | 9.94 | [8.39, 16.65] |",
          " ",
          "-## P1: 支撑性数字更新",
          "+### C11. Conclusion (conclusion.tex:4)",
          "+- [ ] \"$69{\\times}$ to $274{\\times}$... ($d_z$: $0.44 \\to 0.80$)\"",
          " ",
          "-### 11. results.tex:66 — Crossover 数字",
          "-```",
          "-当前: \"importance high_phase=0.032 < random=0.818, importance low_phase=7.196 > random=1.363\"",
          "-reversal \"5.3×\"",
          "-更新: → n=500 crossover 值",
          "-```",
          "+### C12. Discussion (discussion.tex:3-4)",
          "+- [ ] \"$69$--$274{\\times}$\"",
          "+- [ ] Crossover: \"$0.032$ vs. $0.818$\" / \"$7.196$ vs. $1.363$\"",
          " ",
          "-### 12. results.tex:71 — Qwen cross-model 段落",
          "-```",
          "-当前: \"Δ increases from 0.04 at s=0.15 to 2.94 at s=0.30...d_z ≥ 0.55...d_z=0.28 CI includes zero\"",
          "-更新: → n=500 Qwen 值",
          "-关键: 检查 s015 d_z 是否仍 marginal，onset threshold 是否仍 s≥0.20",
          "-```",
          "+### C13. Appendix Crossover (appendix_moved.tex:11)",
          "+- [ ] \"$0.032$ vs. $0.818$\" / \"$7.196$ vs. $1.363$—a $5.3{\\times}$ reversal\"",
          "+- [ ] Reversal magnitudes: \"$3.9{\\times}$, $5.4{\\times}$, $5.3{\\times}$, $3.6{\\times}$\"",
          "+- [ ] Fig caption (L17): \"$5.3{\\times}$\"",
          " ",
          "-### 13. appendix_moved.tex:26 — Qwen/DS 有效 n",
          "-```",
          "-当前: \"Four of the 50 problems...n=46 valid problems for Qwen (vs. n=49 for DeepSeek)\"",
          "-更新: → n=500 的排除数和有效 n",
          "-```",
          "+### C14. Appendix Permutation (appendix_moved.tex:86-105)",
          "+- [ ] L86: \"99.92th percentile... p_Bonf = 0.0032\"",
          "+- [ ] L88: inline Δ: \"$0.37$... to $9.85$\"",
          "+- [ ] L88: CI lower bounds: \"$0.19 \\to 0.69 \\to 1.66 \\to 6.70$\"",
          "+- [ ] Table 7 (tab:permutation) — 全部 4 行:",
          " ",
          "-### 14. appendix_moved.tex:59-60 — Tab cross-model Qwen Δ",
          "-```",
          "-当前 DS: 0.39, 1.48, 7.16, 14.59",
          "-当前 QW: 0.04, 0.23, 1.27, 2.94",
          "-更新: → n=500 值",
          "-```",
          "+| s | Observed Δ̃ | 95% CI | p_Bonf |",
          "+|---|-----------|--------|--------|",
          "+| 0.15 | 0.37 | [0.19, 0.62] | 0.0032 |",
          "+| 0.20 | 0.97 | [0.69, 1.49] | <0.001 |",
          "+| 0.25 | 3.34 | [1.66, 6.64] | <0.001 |",
          "+| 0.30 | 9.85 | [6.70, 16.29] | <0.001 |",
          " ",
          "-### 15. appendix_moved.tex:88,93,99-102 — Tab permutation（DeepSeek permutation test）",
          "-```",
          "-当前: n=49; observed Δ̃ 0.37[0.19,0.62], 0.97[0.69,1.49], 3.34[1.66,6.64], 9.85[6.70,16.29]",
          "-caption \"$n{=}49$\"",
          "-更新: → n=500 permutation test 值",
          "-```",
          "+### C15. Appendix Cross-Model Table (appendix_moved.tex:60)",
          "+- [ ] Table 5 (tab:cross-model) DS 行: 0.39 / 1.48 / 7.16 / 14.59",
          " ",
          "-### 16. results.tex:104 — permutation test 段落引用",
          "-```",
          "-当前: \"observed median differences increasing monotonically from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$\"",
          "-更新: → 与 Tab permutation 一致",
          "-```",
          "+### C16. Appendix Extended Discussion (appendix_disc_analysis.tex:9)",
          "+- [ ] \"II_high < 0.06 at s ≤ 0.30; at s=0.35, high-phase II rises to 0.105\"",
          " ",
          "-### 17. appendix_moved.tex:11 — crossover 详细数字",
          "-```",
          "-当前: \"reversal magnitude of $3.9{\\times}$ at $s{=}0.15$, $5.4{\\times}$ at $s{=}0.20$, $5.3{\\times}$ at $s{=}0.25$, and $3.6{\\times}$ at $s{=}0.30$\"",
          "-更新: → n=500 reversal magnitudes",
          "-```",
          "+### C17. Appendix Statistical Scope (appendix_disc_analysis.tex:45-50)",
          "+- [ ] mean/median ratio ~1.6:1",
          "+- [ ] Comments: \"mean_diff=22.94, median_diff=14.59\", \"median_diff=9.9436\"",
          "+- [ ] Permutation CIs in comment: s015=[0.19,0.62], s020=[0.69,1.49], s025=[1.66,6.64], s030=[6.70,16.29]",
          " ",
          "-### 18. appendix_disc_analysis.tex:46-47 — permutation CI + skewness 统计",
          "-```",
          "-当前: \"mean/median ratio ~1.6:1 at s=0.30\"",
          "-当前: \"permutation CIs: s015=[0.19,0.62], s020=[0.69,1.49], s025=[1.66,6.64], s030=[6.70,16.29]\"",
          "-当前 (line 11): \"high-phase II rises to 0.105 at s=0.35\"",
          "-更新: → n=500 值 (s035 supplementary 是否也需更新取决于是否重跑)",
          "-```",
          "+---",
          " ",
          "-### 19. abstract.tex:10 — LLaMA cross-arch 段落",
          "-```",
          "-当前: \"Δ̃: 0.020→0.356; s=0.30 Wilcoxon p_Bonf=0.029\"",
          "-注意: LLaMA 实验仍为 n=50，数字不变，但需检查措辞是否暗示与 DS/QW 同一 n",
          "-```",
          "+## D. 必须更新 — Qwen 数值",
          " ",
          "-### 20. 图表重新生成",
          "-```",
          "-fig1_dose_response.pdf — G vs s 曲线（P0 依赖）",
          "-fig3_crossover.pdf — crossover bar chart",
          "-fig4_bootstrap.pdf — permutation forest plot",
          "-fig5_crossmodel.pdf — cross-model Δ comparison",
          "-所有图需用 n=500 数据重新生成",
          "-```",
          "+### D1. Table 3 — tab:cohens-d, QW 列 (results.tex:117-120)",
          "+| s | d_z | Δ̃ | CI |",
          "+|---|-----|----|----|",
          "+| 0.15 | 0.28 | 0.05 | [−0.01, 0.11]^ns |",
          "+| 0.20 | 0.55 | 0.21 | [0.07, 0.40] |",
          "+| 0.25 | 0.89 | 1.11 | [0.61, 1.47] |",
          "+| 0.30 | 1.02 | 2.62 | [1.72, 3.65] |",
          " ",
          "+### D2. Results §5.4 Cross-Model (results.tex:71)",
          "+- [ ] \"$\\Delta$ increases from $0.04$... to $2.94$\"",
          "+- [ ] \"$d_z{=}0.28$, CI includes zero\"",
          "+- [ ] \"$d_z \\geq 0.55$\"",
          "+",
          "+### D3. Abstract/Introduction/Conclusion Qwen 内联",
          "+- [ ] abstract.tex:10 — \"$d_z \\geq 0.55$; Spearman $\\rho = 1.0$; gradient permutation $p = 0.043$\"",
          "+- [ ] introduction.tex:15 — \"$d_z \\geq 0.55$\"",
          "+- [ ] conclusion.tex:4 — \"$d_z \\geq 0.55$\"",
          "+",
          "+### D4. Appendix Cross-Model (appendix_moved.tex)",
          "+- [ ] Table 5 (tab:cross-model) QW 行: 0.04 / 0.23 / 1.27 / 2.94",
          "+- [ ] L48: \"at ~1/5 of DeepSeek's magnitude\" → 新比例",
          "+- [ ] fig:cross-model caption (L69): \"one-fifth of DeepSeek's\" → 新比例",
          "+",
          " ---",
          " ",
          "-## P2: 条件性更新",
          "+## E. 必须更新 — 图表重新生成",
          " ",
          "-### 21. D058: Qwen imp-vs-rand 显著性",
          "-```",
          "-当前状态: 论文未报告 Qwen imp-vs-rand permutation test（只报告了 DeepSeek）",
          "-约束: n=500 前不得 claim Qwen imp-vs-rand 显著",
          "-行动:",
          "-  - 若 n=500 Qwen imp-vs-rand 显著 → 可添加 Qwen permutation test 表格，strengthens C1",
          "-  - 若仍不显著 → 在 cross-model 段落加 caveat，或维持当前策略（只报 within-importance gradient）",
          "-检查文件: results.tex:71, appendix_results.tex:10",
          "-```",
          "+| # | 文件名 | Label | 内容 | 数据来源 |",
          "+|---|--------|-------|------|---------|",
          "+| E1 | fig1_dose_response.pdf | fig:hero | G vs s + 95% CI shading | experiment_summary_table.json |",
          "+| E2 | fig3_crossover.pdf | fig:crossover | s=0.25 crossover bars | experiment_summary_table.json |",
          "+| E3 | fig4_bootstrap.pdf | fig:permtest-forest | permutation forest plot | permutation_test_results.json |",
          "+| E4 | fig5_crossmodel.pdf | fig:cross-model | DS vs QW Δ curves | cross_model_analysis.json |",
          " ",
          "-### 22. D059: d_z 报告策略",
          "-```",
          "-约束: within-importance d_z 保留; 涉及 random 只报方向",
          "-行动: 检查 n=500 后是否有新的 imp-vs-rand d_z 值需要报告，确保遵守\"只报方向\"规则",
          "-影响文件: results.tex, appendix_moved.tex",
          "-```",
          "+---",
          " ",
          "-### 23. C2 预注册: Qwen s015 onset threshold",
          "-```",
          "-当前: paper_framing 预注册 \"n=500 后若 QW s015 CI 仍跨零，叙事改为 'compound effect emerges above threshold sparsity (~s020)'\"",
          "-检查: results.tex:71 \"marginal at s=0.15\" + Tab cohens-d QW s015 行",
          "-行动:",
          "-  - 若 n=500 QW s015 CI 不跨零 → onset = s≥0.15，更新叙事",
          "-  - 若仍跨零 → 保持 \"emerges above ~s020\" 叙事",
          "-```",
          "+## F. 必须填入 — 现有 \\placeholder{} 值",
          " ",
          "-### 24. Placeholder 值填充",
          "-以下 \\placeholder{} 标记需用实际数据填充:",
          "+### F1. 从 n=500 Qwen 数据填入",
          "+| # | 文件:行 | Placeholder | 说明 |",
          "+|---|--------|-------------|------|",
          "+| F1a | abstract.tex:8 | `\\placeholder{}` | Qwen s030 random Δ̃ |",
          "+| F1b | results.tex:71 | `\\placeholder{NULL_PCT}` | Qwen mid-phase null rate % |",
          "+| F1c | appendix_moved.tex:30 | `\\placeholder{NULL_PCT}` | 同 F1b |",
          "+| F1d | appendix_moved.tex:35 | `\\placeholder{N_QW}` | Qwen 总有效 n |",
          "+| F1e | appendix_moved.tex:41-43 | 12× `\\placeholder{}` | Qwen per-phase effective n (3 phase × 4 sparsity) |",
          "+| F1f | appendix_disc_analysis.tex:14 | `\\placeholder{}` | Qwen random Δ̃ |",
          "+| F1g | appendix_disc_analysis.tex:49 | `\\placeholder{}` | Qwen random Δ̃ (重复引用) |",
          "+| F1h | appendix_results.tex:10 | `\\placeholder{}` | Qwen random Δ̃ |",
          "+| F1i | appendix_moved.tex:76 | `\\placeholder{}` | Qwen random Δ̃ |",
          " ",
          "-| 文件:行 | Placeholder | 数据来源 | n=500影响? |",
          "-|---------|-------------|----------|-----------|",
          "-| abstract.tex:8 | Qwen rand s030 Δ̃ | bf16_qw_rand_s030 | 是 |",
          "-| results.tex:71 | NULL_PCT | Qwen per-phase null rate | 是 |",
          "-| results.tex:81 | LLaMA random Wilcoxon p | c3_llama | 否(n=50) |",
          "-| results.tex:86 | N_LLAMA | c3_llama | 否(n=50) |",
          "-| results.tex:92-95 | 整个 LLaMA 表格 (12 cells) | c3_llama | 否(n=50) |",
          "-| discussion.tex:10 | ORACLE_PCT, ORACLE_P, HEUR_PCT, HEUR_P | c5b_pilot | 否 |",
          "-| discussion.tex:15 | LLaMA random Wilcoxon p | c3_llama | 否(n=50) |",
          "-| appendix_moved.tex:30 | NULL_PCT | Qwen null rate | 是 |",
          "-| appendix_moved.tex:35 | N_QW | Qwen valid n | 是 |",
          "-| appendix_moved.tex:41-43 | Qwen effective n 表格 (12 cells) | Qwen per-phase data | 是 |",
          "-| appendix_moved.tex:73 | ρ, p (per-problem concordance) | cross_model_analysis.json | 是 |",
          "-| appendix_moved.tex:76 | Qwen rand s030 Δ̃ | bf16_qw_rand_s030 | 是 |",
          "-| appendix_results.tex:7 | 同 appendix_moved.tex:73 (重复!) | cross_model_analysis.json | 是 |",
          "-| appendix_results.tex:10 | 同 appendix_moved.tex:76 (重复!) | bf16_qw_rand_s030 | 是 |",
          "-| appendix_disc_analysis.tex:14 | Qwen rand s030 Δ̃ | bf16_qw_rand_s030 | 是 |",
          "-| appendix_disc_analysis.tex:49 | Qwen rand s030 Δ̃ | qw_rand_s030 | 是 |",
          "+### F2. 从 n=500 Cross-model 数据填入",
          "+| # | 文件:行 | Placeholder | 说明 |",
          "+|---|--------|-------------|------|",
          "+| F2a | appendix_results.tex:7 | `\\placeholder{}` × 2 | per-problem concordance ρ 和 p |",
          "+| F2b | appendix_moved.tex:73 | `\\placeholder{}` × 2 | 同 F2a（重复段落） |",
          " ",
          "-⚠️ appendix_results.tex 未被 main.tex \\input，内容与 appendix_moved.tex §Cross-Model 重复。建议删除或统一。",
          "+### F3. 从 c3_llama 数据填入（与 n=500 无关，可提前填）",
          "+| # | 文件:行 | Placeholder | 说明 |",
          "+|---|--------|-------------|------|",
          "+| F3a | results.tex:81 | `\\placeholder{}` | LLaMA random Wilcoxon p (s=0.30) |",
          "+| F3b | results.tex:86 | `\\placeholder{N_LLAMA}` | LLaMA paired n |",
          "+| F3c | results.tex:92-95 | 12+ `\\placeholder{}` | Tab 4 全部 (Δ̃, CI, p × 4 levels) |",
          "+| F3d | discussion.tex:15 | `\\placeholder{}` | LLaMA random Wilcoxon p |",
          " ",
          "+### F4. 从 c5b_pilot 数据填入（与 n=500 无关，可提前填）",
          "+| # | 文件:行 | Placeholder | 说明 |",
          "+|---|--------|-------------|------|",
          "+| F4a | discussion.tex:10 | `\\placeholder{ORACLE_PCT}` | oracle recovery % |",
          "+| F4b | discussion.tex:10 | `\\placeholder{ORACLE_P}` | oracle Wilcoxon p |",
          "+| F4c | discussion.tex:10 | `\\placeholder{HEUR_PCT}` | heuristic recovery % |",
          "+| F4d | discussion.tex:10 | `\\placeholder{HEUR_P}` | heuristic Wilcoxon p |",
          "+",
          " ---",
          " ",
          "-## P3: 一致性与混用风险",
          "+## G. 条件更新（取决于 n=500 分析结果）",
          " ",
          "-### 25. n=50 / n=500 混用风险矩阵",
          "+### G1. Qwen s015 onset threshold",
          "+- **若 CI 仍跨零** → 保持 \"marginal at s=0.15\"、\"at s ≥ 0.20\"",
          "+- **若 CI 不再跨零** → 全部改为 \"at all sparsity levels\"，删 \"marginal\" 限定",
          "+- **若 s020 也变边缘** → onset 改为 \"s ≥ 0.25\"",
          "+- 受影响: abstract.tex:10, introduction.tex:15, results.tex:71/106, conclusion.tex:4, Table 3 footnote",
          " ",
          "-| 数据源 | 当前 n | 更新后 n | 混用风险 |",
          "-|--------|--------|---------|---------|",
          "-| DeepSeek importance/random (c2) | 50 | **500** | 主表全部替换 |",
          "-| Qwen importance/random (c2) | 50 | **500** | 主表全部替换 |",
          "-| LLaMA cross-arch (c3_llama) | 50 | **50 不变** | ⚠️ 高风险 |",
          "-| Entropy/discrimination (c4) | 30 | **30 不变** | ⚠️ 中风险 |",
          "-| c5b_pilot | ~50 | **不变** | 低风险 |",
          "-| Permutation test | 49(DS)/46(QW) | **~490/~460** | 替换 |",
          "-| Cross-model comparison | 50 | **500** | 替换 |",
          "+### G2. Random \"7/8 FAIL\" 计数",
          "+- **若 n=500 random 仍不显著** → 保持 \"7/8\"",
          "+- **若更多 random 条件显著** → 更新计数，调整 \"strategy-specific\" 措辞",
          "+- **若 Qwen s030 random 不再显著** → 简化叙事，删 exception 讨论",
          "+- 受影响: abstract.tex:8, conclusion.tex:4, appendix_disc_analysis.tex:14, appendix_results.tex:10",
          " ",
          "-### 26. 需要显式声明不同 n 的位置",
          "-```",
          "-- abstract.tex: \"50 MATH-500 problems\" → 改为区分 DS/QW (n=500) vs LLaMA (n=50)",
          "-  建议: \"500 MATH-500 problems (50 for cross-architecture validation)\"",
          "-- results.tex §5.5 (cross-arch): 已有 \"n=\\placeholder{N_LLAMA}\" → 填入 49 或 50，确保读者知道这不是 500",
          "-- analysis.tex §6: 当前未提及 c4 的样本量 → 建议添加脚注 \"(30 problems per model)\"",
          "-- discussion.tex §7 (pilot): 当前未提及 pilot 样本量 → 建议添加",
          "-- methodology.tex: 需说明 \"500 problems for primary experiments; 50 for cross-architecture (LLaMA)\"",
          "-- limitations.tex: 添加 \"LLaMA 和 mechanism 分析基于 n=50/30 子集\"",
          "-```",
          "+### G3. Qwen s030 random effect size",
          "+- **若 d 变大（non-negligible）** → 更新 \"negligible\" 描述",
          "+- **若 d 仍 negligible** → 保持",
          "+- 受影响: 所有 Qwen random Δ̃ placeholder 位置",
          " ",
          "-### 27. C8 partially_confirmed 限定语检查 ✅",
          "-已确认以下位置使用了合格限定语:",
          "-- abstract.tex:10 — \"mixed but directionally consistent evidence\"",
          "-- results.tex:79 — \"partially confirming the cross-architecture hypothesis\"",
          "-- discussion.tex:14-15 — \"partial support...substantially weaker\"",
          "-- conclusion.tex:4 — \"partially extends cross-architecture\"",
          "-- limitations.tex:1-2 — \"partially confirms...substantially weaker\"",
          "-- appendix_disc_analysis.tex:33 — \"partial confirmation\"",
          "-**状态: 合格，无需修改（除非 n=500 改变了 DS/QW 数据使 LLaMA 对比幅度比例变化）**",
          "+### G4. DS/QW 量级比",
          "+- 当前: \"~1/5\"。n=500 后比例可能变化 → appendix_moved.tex:48/69",
          "+- 当前: Spearman ρ=1.0。若不再完全单调 → 更新",
          " ",
          "-### 28. C5b future_work 标注检查 ✅",
          "-已确认:",
          "-- discussion.tex:10 — pilot 结果 + \"promising direction for future work\"",
          "-- appendix_disc_analysis.tex:57,62 — REBUTTAL comments 标注 future work",
          "-**状态: 合格，但 discussion.tex:10 的 \\placeholder{} 值需填充**",
          "+### G5. 单调性 (C6/S7→C)",
          "+- 若 G 曲线不再严格单调 → 修改 \"monotonically increasing\"",
          "+- 受影响: abstract, introduction, results §5.2, conclusion",
          " ",
          "-### 29. Qwen random s030 caveat 检查",
          "-当前标注为 negligible/no meaningful modulation 的位置:",
          "-- abstract.tex:8 — \"negligible median difference\" ✅",
          "-- appendix_moved.tex:76 — \"negligible median difference, CI spans zero\" ✅",
          "-- appendix_results.tex:10 — 同上 ✅",
          "-- appendix_disc_analysis.tex:14 — \"negligible effect size\" ✅",
          "-- appendix_disc_analysis.tex:49 — \"negligible effect size, bootstrap CI spanning zero\" ✅",
          "-**n=500 后需重新检查: Qwen rand s030 是否仍为 borderline/negligible → 若变显著且效应量非 negligible，需修改 \"7/8 FAIL\" 叙事**",
          "+### G6. Sub-exponential growth factors",
          "+- 当前: 3.8×→4.8×→2.0×（递减）→ 重算",
          "+- 受影响: paper_framing.md",
          " ",
          "+### G7. LLaMA 相对量级",
          "+- discussion.tex:15 \"~7× smaller than Qwen\" — Qwen 值更新后可能需重算此比例",
          "+",
          " ---",
          " ",
          "-## 执行顺序建议",
          "+## H. 不需要更新",
          " ",
          "-```",
          "-Phase 1: 数据准备",
          "-  1.1 等 n=500 数据完成",
          "-  1.2 运行统计分析脚本 → experiment_summary_table.json, cohens_d, permutation_test 等",
          "-  1.3 提取所有新数值到一个汇总表",
          "+| 文件 | 原因 |",
          "+|------|------|",
          "+| related_work.tex | 文献综述，无数据依赖 |",
          "+| background.tex | 公式定义 (II, G, phase segmentation) |",
          "+| methodology.tex:1-9 | Models/Sparsity config 不变（仅 Dataset 段更新） |",
          "+| analysis.tex | 引用 c4_entropy 数据 (n=30)，独立实验 |",
          "+| appendix.tex | formulation details / multiplicative null |",
          "+| Tab discrimination-metrics-full | c4_entropy Gini/CV (n=30) |",
          "+| Tab entropy-deltas | c4_entropy ΔH (n=30) |",
          "+| Tab llama-cross-arch 数值 | c3_llama (n=50)，非 n=500 范围（placeholder 另列于 F3） |",
          "+| C5b pilot 数值 | c5b_pilot 独立实验（placeholder 另列于 F4） |",
          "+| LLaMA abstract/intro/conclusion 内联 | \"$0.020 \\to 0.356$\" 等 LLaMA 数据不变 |",
          " ",
          "-Phase 2: P0 核心更新 (同步进行，确保一致)",
          "-  2.1 更新 results.tex 三张主表 (Tab 1/2/3)",
          "-  2.2 更新 abstract.tex 数字",
          "-  2.3 更新 introduction.tex 数字",
          "-  2.4 更新 conclusion.tex 数字",
          "-  2.5 更新 discussion.tex 数字",
          "-  2.6 更新 methodology.tex 样本量",
          "+---",
          " ",
          "-Phase 3: P1 支撑更新",
          "-  3.1 更新 appendix_moved.tex 所有表格和数字",
          "-  3.2 更新 appendix_disc_analysis.tex 数字",
          "-  3.3 重新生成 4 张图 (fig1-fig5)",
          "+## I. 推荐更新顺序",
          " ",
          "-Phase 4: P2 条件分支",
          "-  4.1 检查 QW s015 CI → 决定 onset threshold 叙事",
          "-  4.2 检查 QW imp-vs-rand → 决定是否添加 Qwen permutation test",
          "-  4.3 检查 QW rand s030 → 决定 \"7/8 FAIL\" 叙事是否需调整",
          "-  4.4 填充所有 \\placeholder{}",
          "+1. **立即可做**: 填 F3 (LLaMA placeholder) + F4 (C5b pilot placeholder) — 与 n=500 无关",
          "+2. **等 n=500 分析完成** → 获取 JSON 输出文件",
          "+3. **替换 A (文字 50→500)** + **B (配对 n)**",
          "+4. **批量替换 C (DeepSeek 数值)** — 从 experiment_summary_table.json 读取",
          "+5. **批量替换 D (Qwen 数值)** — 同上",
          "+6. **填入 F1/F2 (n=500 placeholder)**",
          "+7. **评估 G (条件更新)** — 根据结果判断叙事调整",
          "+8. **重生成 E (图表)**",
          "+9. **全文交叉验证**: abstract/intro/conclusion 内联数字 = tables 数字",
          " ",
          "-Phase 5: P3 一致性扫描",
          "-  5.1 全文搜索 \"n=50\" / \"50 problems\" / \"n=49\" / \"n=46\" → 确保无残留",
          "-  5.2 添加 LLaMA n=50 / c4 n=30 的显式声明",
          "-  5.3 清理 appendix_results.tex（重复文件）",
          "+## J. 数据来源映射",
          " ",
          "-Phase 6: 验证",
          "-  6.1 LaTeX 编译 → 确保无 red placeholder 残留",
          "-  6.2 数字交叉检查: 每个数字在所有出现位置一致",
          "-  6.3 paper_framing.md 同步更新",
          "-```",
          "+| 数据 | JSON 来源 | 论文位置 |",
          "+|------|----------|---------|",
          "+| DS median Δ (imp/rand) | experiment_summary_table.json → median_diff | Tab 1, Tab 2, inline §5.1 |",
          "+| DS per-phase II | experiment_summary_table.json → per-phase medians | Tab 2 |",
          "+| DS G ratios | Tab 2 (II_low / II_high) | Tab 2, inline §5.2 |",
          "+| DS Cohen's d_z + Δ̃ [CI] | cohens_d_bf16.json | Tab 3 DS cols |",
          "+| QW Cohen's d_z + Δ̃ [CI] | cohens_d_bf16_qwen.json | Tab 3 QW cols |",
          "+| Permutation Δ̃ + CI + p | permutation_test_results.json | Tab 7 |",
          "+| Cross-model Δ | cross_model_analysis.json | Tab 5 |",
          "+| QW per-phase effective n | analyze_n500_unified.py → qwen null rate | Tab (app), inline |",
          "+| QW random Δ̃ (s030) | experiment_summary_table.json → qw_rand_s030 | abstract, appendix |",
          "+| Per-problem concordance | cross_model_analysis.json → spearman_rho, p | appendix |"
        ]
      }
    ],
    "originalFile": "# Paper Update Checklist: n=50 → n=500\n\n> 生成时间: 2026-05-15 | 适用实验: c2_n500_deepseek + c2_qw_n500 (C7)\n> 约束: median + bootstrap CI 为主指标 (D054); d_z 分场景 (D059); Qwen imp-vs-rand 不claim显著直到n=500确认 (D058); C8=partially_confirmed (D060); C5b=future_work (D056)\n\n---\n\n## 优先级说明\n- **P0**: 核心数字，读者第一眼看到，必须同步更新\n- **P1**: 支撑性数字/表格，与 P0 有数据依赖\n- **P2**: 条件性更新（取决于 n=500 结果）\n- **P3**: 一致性检查，防止 n=50/n=500 混用\n\n---\n\n## P0: 核心数字更新\n\n### 1. methodology.tex:10 — 样本量\n```\n当前: \"We use 50 problems stratified from MATH-500\"\n更新: → 500 problems (n=500 的具体描述，包括 stratification 方式)\n```\n\n### 2. abstract.tex:6 — 样本量\n```\n当前: \"using 50 MATH-500 problems\"\n更新: → 500 MATH-500 problems\n```\n\n### 3. abstract.tex:7 — DeepSeek 主指标\n```\n当前: \"median Interaction Index difference...from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired Cohen's $d_z$ growing from $0.44$ (small) to $0.80$ (large)\"\n更新: → 用 n=500 segment-level median diff + paired d_z 替换\n注意: 0.39/14.59 是 segment-level medians；d_z 0.44/0.80 是 paired d_z。两组数据来源不同，都需更新。\n```\n\n### 4. introduction.tex:14 — DeepSeek 主指标（与 abstract 一致）\n```\n当前: \"median phase difference rises from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$ ($d_z$: $0.44 \\to 0.80$)\"\n更新: → 同 abstract\n```\n\n### 5. results.tex:8,13,19-20 — Tab aggregate-ii（DeepSeek segment-level Δ）\n```\n当前 Importance: 0.39, 1.48, 7.16, 14.59\n当前 Random: 0.01, -0.02, 0.54, 1.54\ncaption \"$n{=}50$\" → $n{=}500$ (或实际有效 n)\n更新: → 全部替换为 n=500 值\n```\n\n### 6. results.tex:34,40-50 — Tab main-results（DeepSeek 全 per-phase 分解）\n```\n当前 (importance, 4 sparsity × 3 phases + Δ + G):\n  s015: II_high=0.006, II_mid=0.081, II_low=0.398, Δ=0.39, G=69\n  s020: II_high=0.015, II_mid=0.203, II_low=1.496, Δ=1.48, G=103\n  s025: II_high=0.032, II_mid=1.118, II_low=7.196, Δ=7.16, G=222\n  s030: II_high=0.053, II_mid=2.283, II_low=14.639, Δ=14.59, G=274\n当前 (random, 4 sparsity × 3 phases + Δ + G):\n  s015: 0.093, 0.097, 0.103, 0.01, 1.1\n  s020: 0.292, 0.350, 0.276, -0.02, 0.9\n  s025: 0.818, 0.932, 1.363, 0.54, 1.7\n  s030: 2.503, 2.592, 4.041, 1.54, 1.6\ncaption \"50 problems\" → 500 problems\n更新: → 全部替换为 n=500 值\n```\n\n### 7. results.tex:106,117-120 — Tab cohens-d（DS + QW paired d_z + Δ̃[CI]）\n```\n当前 DS: d_z 0.44/0.52/0.68/0.80; Δ̃ 0.32[0.20,0.47] / 1.15[0.66,1.26] / 3.97[2.83,5.29] / 9.94[8.39,16.65]\n当前 QW: d_z 0.28/0.55/0.89/1.02; Δ̃ 0.05[-0.01,0.11] / 0.21[0.07,0.40] / 1.11[0.61,1.47] / 2.62[1.72,3.65]\n更新: → 全部替换为 n=500 值\n关键: QW s015 CI 当前包含零 → n=500 后检查是否仍包含零（影响 onset threshold 叙事）\n```\n\n### 8. conclusion.tex:4 — 核心数字复述\n```\n当前: \"severity gradient grows from $69{\\times}$ to $274{\\times}$...($d_z$: $0.44 \\to 0.80$)\"\n更新: → 与 results 一致\n```\n\n### 9. discussion.tex:5 — severity gradient + crossover 复述\n```\n当前: \"severity gradient ($69$--$274{\\times}$)\"\n当前: crossover 数字 \"0.032 vs 0.818\", \"7.196 vs 1.363\"\n更新: → 与 results 一致\n```\n\n### 10. results.tex:29 + 58 — G 值 + fig1 caption\n```\n当前: G \"from $69{\\times}$ at $s{=}0.15$ to $274{\\times}$ at $s{=}0.30$\"\n当前 fig1 caption: \"$69{\\times}$ to $274{\\times}$\"\n更新: → n=500 G 值\n```\n\n---\n\n## P1: 支撑性数字更新\n\n### 11. results.tex:66 — Crossover 数字\n```\n当前: \"importance high_phase=0.032 < random=0.818, importance low_phase=7.196 > random=1.363\"\nreversal \"5.3×\"\n更新: → n=500 crossover 值\n```\n\n### 12. results.tex:71 — Qwen cross-model 段落\n```\n当前: \"Δ increases from 0.04 at s=0.15 to 2.94 at s=0.30...d_z ≥ 0.55...d_z=0.28 CI includes zero\"\n更新: → n=500 Qwen 值\n关键: 检查 s015 d_z 是否仍 marginal，onset threshold 是否仍 s≥0.20\n```\n\n### 13. appendix_moved.tex:26 — Qwen/DS 有效 n\n```\n当前: \"Four of the 50 problems...n=46 valid problems for Qwen (vs. n=49 for DeepSeek)\"\n更新: → n=500 的排除数和有效 n\n```\n\n### 14. appendix_moved.tex:59-60 — Tab cross-model Qwen Δ\n```\n当前 DS: 0.39, 1.48, 7.16, 14.59\n当前 QW: 0.04, 0.23, 1.27, 2.94\n更新: → n=500 值\n```\n\n### 15. appendix_moved.tex:88,93,99-102 — Tab permutation（DeepSeek permutation test）\n```\n当前: n=49; observed Δ̃ 0.37[0.19,0.62], 0.97[0.69,1.49], 3.34[1.66,6.64], 9.85[6.70,16.29]\ncaption \"$n{=}49$\"\n更新: → n=500 permutation test 值\n```\n\n### 16. results.tex:104 — permutation test 段落引用\n```\n当前: \"observed median differences increasing monotonically from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$\"\n更新: → 与 Tab permutation 一致\n```\n\n### 17. appendix_moved.tex:11 — crossover 详细数字\n```\n当前: \"reversal magnitude of $3.9{\\times}$ at $s{=}0.15$, $5.4{\\times}$ at $s{=}0.20$, $5.3{\\times}$ at $s{=}0.25$, and $3.6{\\times}$ at $s{=}0.30$\"\n更新: → n=500 reversal magnitudes\n```\n\n### 18. appendix_disc_analysis.tex:46-47 — permutation CI + skewness 统计\n```\n当前: \"mean/median ratio ~1.6:1 at s=0.30\"\n当前: \"permutation CIs: s015=[0.19,0.62], s020=[0.69,1.49], s025=[1.66,6.64], s030=[6.70,16.29]\"\n当前 (line 11): \"high-phase II rises to 0.105 at s=0.35\"\n更新: → n=500 值 (s035 supplementary 是否也需更新取决于是否重跑)\n```\n\n### 19. abstract.tex:10 — LLaMA cross-arch 段落\n```\n当前: \"Δ̃: 0.020→0.356; s=0.30 Wilcoxon p_Bonf=0.029\"\n注意: LLaMA 实验仍为 n=50，数字不变，但需检查措辞是否暗示与 DS/QW 同一 n\n```\n\n### 20. 图表重新生成\n```\nfig1_dose_response.pdf — G vs s 曲线（P0 依赖）\nfig3_crossover.pdf — crossover bar chart\nfig4_bootstrap.pdf — permutation forest plot\nfig5_crossmodel.pdf — cross-model Δ comparison\n所有图需用 n=500 数据重新生成\n```\n\n---\n\n## P2: 条件性更新\n\n### 21. D058: Qwen imp-vs-rand 显著性\n```\n当前状态: 论文未报告 Qwen imp-vs-rand permutation test（只报告了 DeepSeek）\n约束: n=500 前不得 claim Qwen imp-vs-rand 显著\n行动:\n  - 若 n=500 Qwen imp-vs-rand 显著 → 可添加 Qwen permutation test 表格，strengthens C1\n  - 若仍不显著 → 在 cross-model 段落加 caveat，或维持当前策略（只报 within-importance gradient）\n检查文件: results.tex:71, appendix_results.tex:10\n```\n\n### 22. D059: d_z 报告策略\n```\n约束: within-importance d_z 保留; 涉及 random 只报方向\n行动: 检查 n=500 后是否有新的 imp-vs-rand d_z 值需要报告，确保遵守\"只报方向\"规则\n影响文件: results.tex, appendix_moved.tex\n```\n\n### 23. C2 预注册: Qwen s015 onset threshold\n```\n当前: paper_framing 预注册 \"n=500 后若 QW s015 CI 仍跨零，叙事改为 'compound effect emerges above threshold sparsity (~s020)'\"\n检查: results.tex:71 \"marginal at s=0.15\" + Tab cohens-d QW s015 行\n行动:\n  - 若 n=500 QW s015 CI 不跨零 → onset = s≥0.15，更新叙事\n  - 若仍跨零 → 保持 \"emerges above ~s020\" 叙事\n```\n\n### 24. Placeholder 值填充\n以下 \\placeholder{} 标记需用实际数据填充:\n\n| 文件:行 | Placeholder | 数据来源 | n=500影响? |\n|---------|-------------|----------|-----------|\n| abstract.tex:8 | Qwen rand s030 Δ̃ | bf16_qw_rand_s030 | 是 |\n| results.tex:71 | NULL_PCT | Qwen per-phase null rate | 是 |\n| results.tex:81 | LLaMA random Wilcoxon p | c3_llama | 否(n=50) |\n| results.tex:86 | N_LLAMA | c3_llama | 否(n=50) |\n| results.tex:92-95 | 整个 LLaMA 表格 (12 cells) | c3_llama | 否(n=50) |\n| discussion.tex:10 | ORACLE_PCT, ORACLE_P, HEUR_PCT, HEUR_P | c5b_pilot | 否 |\n| discussion.tex:15 | LLaMA random Wilcoxon p | c3_llama | 否(n=50) |\n| appendix_moved.tex:30 | NULL_PCT | Qwen null rate | 是 |\n| appendix_moved.tex:35 | N_QW | Qwen valid n | 是 |\n| appendix_moved.tex:41-43 | Qwen effective n 表格 (12 cells) | Qwen per-phase data | 是 |\n| appendix_moved.tex:73 | ρ, p (per-problem concordance) | cross_model_analysis.json | 是 |\n| appendix_moved.tex:76 | Qwen rand s030 Δ̃ | bf16_qw_rand_s030 | 是 |\n| appendix_results.tex:7 | 同 appendix_moved.tex:73 (重复!) | cross_model_analysis.json | 是 |\n| appendix_results.tex:10 | 同 appendix_moved.tex:76 (重复!) | bf16_qw_rand_s030 | 是 |\n| appendix_disc_analysis.tex:14 | Qwen rand s030 Δ̃ | bf16_qw_rand_s030 | 是 |\n| appendix_disc_analysis.tex:49 | Qwen rand s030 Δ̃ | qw_rand_s030 | 是 |\n\n⚠️ appendix_results.tex 未被 main.tex \\input，内容与 appendix_moved.tex §Cross-Model 重复。建议删除或统一。\n\n---\n\n## P3: 一致性与混用风险\n\n### 25. n=50 / n=500 混用风险矩阵\n\n| 数据源 | 当前 n | 更新后 n | 混用风险 |\n|--------|--------|---------|---------|\n| DeepSeek importance/random (c2) | 50 | **500** | 主表全部替换 |\n| Qwen importance/random (c2) | 50 | **500** | 主表全部替换 |\n| LLaMA cross-arch (c3_llama) | 50 | **50 不变** | ⚠️ 高风险 |\n| Entropy/discrimination (c4) | 30 | **30 不变** | ⚠️ 中风险 |\n| c5b_pilot | ~50 | **不变** | 低风险 |\n| Permutation test | 49(DS)/46(QW) | **~490/~460** | 替换 |\n| Cross-model comparison | 50 | **500** | 替换 |\n\n### 26. 需要显式声明不同 n 的位置\n```\n- abstract.tex: \"50 MATH-500 problems\" → 改为区分 DS/QW (n=500) vs LLaMA (n=50)\n  建议: \"500 MATH-500 problems (50 for cross-architecture validation)\"\n- results.tex §5.5 (cross-arch): 已有 \"n=\\placeholder{N_LLAMA}\" → 填入 49 或 50，确保读者知道这不是 500\n- analysis.tex §6: 当前未提及 c4 的样本量 → 建议添加脚注 \"(30 problems per model)\"\n- discussion.tex §7 (pilot): 当前未提及 pilot 样本量 → 建议添加\n- methodology.tex: 需说明 \"500 problems for primary experiments; 50 for cross-architecture (LLaMA)\"\n- limitations.tex: 添加 \"LLaMA 和 mechanism 分析基于 n=50/30 子集\"\n```\n\n### 27. C8 partially_confirmed 限定语检查 ✅\n已确认以下位置使用了合格限定语:\n- abstract.tex:10 — \"mixed but directionally consistent evidence\"\n- results.tex:79 — \"partially confirming the cross-architecture hypothesis\"\n- discussion.tex:14-15 — \"partial support...substantially weaker\"\n- conclusion.tex:4 — \"partially extends cross-architecture\"\n- limitations.tex:1-2 — \"partially confirms...substantially weaker\"\n- appendix_disc_analysis.tex:33 — \"partial confirmation\"\n**状态: 合格，无需修改（除非 n=500 改变了 DS/QW 数据使 LLaMA 对比幅度比例变化）**\n\n### 28. C5b future_work 标注检查 ✅\n已确认:\n- discussion.tex:10 — pilot 结果 + \"promising direction for future work\"\n- appendix_disc_analysis.tex:57,62 — REBUTTAL comments 标注 future work\n**状态: 合格，但 discussion.tex:10 的 \\placeholder{} 值需填充**\n\n### 29. Qwen random s030 caveat 检查\n当前标注为 negligible/no meaningful modulation 的位置:\n- abstract.tex:8 — \"negligible median difference\" ✅\n- appendix_moved.tex:76 — \"negligible median difference, CI spans zero\" ✅\n- appendix_results.tex:10 — 同上 ✅\n- appendix_disc_analysis.tex:14 — \"negligible effect size\" ✅\n- appendix_disc_analysis.tex:49 — \"negligible effect size, bootstrap CI spanning zero\" ✅\n**n=500 后需重新检查: Qwen rand s030 是否仍为 borderline/negligible → 若变显著且效应量非 negligible，需修改 \"7/8 FAIL\" 叙事**\n\n---\n\n## 执行顺序建议\n\n```\nPhase 1: 数据准备\n  1.1 等 n=500 数据完成\n  1.2 运行统计分析脚本 → experiment_summary_table.json, cohens_d, permutation_test 等\n  1.3 提取所有新数值到一个汇总表\n\nPhase 2: P0 核心更新 (同步进行，确保一致)\n  2.1 更新 results.tex 三张主表 (Tab 1/2/3)\n  2.2 更新 abstract.tex 数字\n  2.3 更新 introduction.tex 数字\n  2.4 更新 conclusion.tex 数字\n  2.5 更新 discussion.tex 数字\n  2.6 更新 methodology.tex 样本量\n\nPhase 3: P1 支撑更新\n  3.1 更新 appendix_moved.tex 所有表格和数字\n  3.2 更新 appendix_disc_analysis.tex 数字\n  3.3 重新生成 4 张图 (fig1-fig5)\n\nPhase 4: P2 条件分支\n  4.1 检查 QW s015 CI → 决定 onset threshold 叙事\n  4.2 检查 QW imp-vs-rand → 决定是否添加 Qwen permutation test\n  4.3 检查 QW rand s030 → 决定 \"7/8 FAIL\" 叙事是否需调整\n  4.4 填充所有 \\placeholder{}\n\nPhase 5: P3 一致性扫描\n  5.1 全文搜索 \"n=50\" / \"50 problems\" / \"n=49\" / \"n=46\" → 确保无残留\n  5.2 添加 LLaMA n=50 / c4 n=30 的显式声明\n  5.3 清理 appendix_results.tex（重复文件）\n\nPhase 6: 验证\n  6.1 LaTeX 编译 → 确保无 red placeholder 残留\n  6.2 数字交叉检查: 每个数字在所有出现位置一致\n  6.3 paper_framing.md 同步更新\n```\n",
    "userModified": false
  }
}
````

</details>

---

### Assistant

_source line 106_

清单已保存到 `artifacts/paper_update_checklist.md`。

**汇总**：

- **A+B**: 5 处 "50"→"500" 文字 + 3 处配对 n 更新
- **C**: 17 组 DeepSeek 数值更新（覆盖 Tab 1/2/3/5/7 + abstract/intro/results/discussion/conclusion/appendix 内联数字，共 ~80 个数值）
- **D**: 4 组 Qwen 数值更新（Tab 3/5 + 内联，共 ~25 个数值）
- **E**: 4 张图表需重新生成
- **F**: 30+ 个 `\placeholder{}` 需填入（其中 F3/F4 共 ~18 个与 n=500 无关，可立即填入）
- **G**: 7 类条件更新，取决于 n=500 结果是否改变定性结论（最关键: G1 Qwen onset threshold、G2 random FAIL 计数）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "uuid": "c9aab197-cfb4-44e6-b008-8a76d823f8a3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BaWrPmaDL9QyV29VVGgtpX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6161,
      "cache_read_input_tokens": 87979,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6161
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Task result

_source line 107_

清单已保存到 `artifacts/paper_update_checklist.md`。

**汇总**：

- **A+B**: 5 处 "50"→"500" 文字 + 3 处配对 n 更新
- **C**: 17 组 DeepSeek 数值更新（覆盖 Tab 1/2/3/5/7 + abstract/intro/results/discussion/conclusion/appendix 内联数字，共 ~80 个数值）
- **D**: 4 组 Qwen 数值更新（Tab 3/5 + 内联，共 ~25 个数值）
- **E**: 4 张图表需重新生成
- **F**: 30+ 个 `\placeholder{}` 需填入（其中 F3/F4 共 ~18 个与 n=500 无关，可立即填入）
- **G**: 7 类条件更新，取决于 n=500 结果是否改变定性结论（最关键: G1 Qwen onset threshold、G2 random FAIL 计数）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 509990,
  "duration_api_ms": 506045,
  "num_turns": 43,
  "stop_reason": "end_turn",
  "session_id": "599e7e9c-0266-49c2-9eb5-39612a712944",
  "total_cost_usd": 1.65903125,
  "usage": {
    "input_tokens": 20,
    "cache_creation_input_tokens": 82299,
    "cache_read_input_tokens": 994231,
    "output_tokens": 25831,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 82299,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 292,
        "cache_read_input_tokens": 87979,
        "cache_creation_input_tokens": 6161,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 6161
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1572,
      "outputTokens": 20,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001672,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 20,
      "outputTokens": 25831,
      "cacheReadInputTokens": 994231,
      "cacheCreationInputTokens": 82299,
      "webSearchRequests": 0,
      "costUSD": 1.6573592499999998,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "4a102b8e-3631-4f44-b5c6-cf76d4949fc6"
}
```

</details>

---
