# paper post llama consistency check

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 40
- **Recorded user turns:** 0
- **Tool calls:** 13
- **Original source:** `logs/workers/worker_paper_post_llama_consistency_check_20260516T224223.log`
- **Structured JSON:** [`6b85ae1cc0025b928ad7.json`](../../sessions/6b/6b85ae1cc0025b928ad7.json)

## Before a recorded user message

40 recorded events

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
  "session_id": "e127786f-a191-4d01-b58d-071eb9fc50fc",
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
  "uuid": "e8ac44d5-3738-47b0-94e5-db229b07e226",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/memory/"
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
    "resetsAt": 1778988000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "bb8354e9-1ea8-4f5c-881d-2c0f745de227",
  "session_id": "e127786f-a191-4d01-b58d-071eb9fc50fc"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the paper_framing.md and then the tex files to check consistency.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e127786f-a191-4d01-b58d-071eb9fc50fc",
  "uuid": "c7c336c4-32a0-4bfe-adfb-565773ccea99",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V1tfCk3Yr7WtsZtuf2X4sd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12582,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12582
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

### Assistant

_source line 5_

I'll read the paper framing document and all relevant tex files to check consistency.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e127786f-a191-4d01-b58d-071eb9fc50fc",
  "uuid": "d4bbb511-9c8c-4bf0-8614-87544ff564c7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V1tfCk3Yr7WtsZtuf2X4sd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12582,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12582
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

_source line 6_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_014PuoEYZbMc6cXdxormBhfN`</summary>

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
  "session_id": "e127786f-a191-4d01-b58d-071eb9fc50fc",
  "uuid": "a83943d4-eeb2-4d52-ae9c-2d11a4a5b697",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V1tfCk3Yr7WtsZtuf2X4sd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12582,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12582
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

_source line 7 · 2026-05-16T22:42:37.775Z_

<details><summary>↩ Tool result · `toolu_014PuoEYZbMc6cXdxormBhfN`</summary>

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
  "session_id": "e127786f-a191-4d01-b58d-071eb9fc50fc",
  "uuid": "3d707b3d-129b-4100-b70e-c1e0666556f6",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file",
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
Let me read the paper_framing.md first, then read the tex files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e127786f-a191-4d01-b58d-071eb9fc50fc",
  "uuid": "4f9a29ef-62dc-47f6-8910-ec5a04d152f0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JqxDm9gBcGGnHx6CvdxFWY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 489,
      "cache_read_input_tokens": 24423,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 489
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

_source line 9_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01TghsDugeczZoRV2hSEheBA`</summary>

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
  "session_id": "e127786f-a191-4d01-b58d-071eb9fc50fc",
  "uuid": "84a531e1-cf16-44b6-bf41-eae4c9daa072",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JqxDm9gBcGGnHx6CvdxFWY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 489,
      "cache_read_input_tokens": 24423,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 489
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

_source line 10 · 2026-05-16T22:42:41.363Z_

<details><summary>↩ Tool result · `toolu_01TghsDugeczZoRV2hSEheBA`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper_framing.md\", \"content\": \"# Paper Framing — Phase-Gated Compound Sparsity\\n\\n> 最后更新: 2026-05-16 (数值对齐 n=500 registry: DS median_diff 0.39/1.21/3.99/8.48; QW 0.07/0.31/1.07/3.16; Cohen's d registry 0.61→1.13/0.37→1.44; C7+C10 status→confirmed; imp/rand 2.7-15×) | 维护者: Director\\n\\n## Core Insight\\n\\nCompound sparsity（attention head pruning + KV cache eviction）的 severity 不是固定常数——它是 eviction strategy 和 reasoning phase 交互的涌现属性。Importance-based eviction 的 compound interaction severity（paired median difference: median(II_low_i − II_high_i)）随 sparsity 单调递增（DeepSeek: 0.39→1.21→3.99→8.48; Qwen: 0.07→0.31→1.07→3.16），而 random masking 在 s015/s020 NS，在 s025 跨模型显著但效应量远小于 importance（DS: 0.257 vs 3.986; QW: 0.393 vs 1.074, 2.7-15×差异），存在 sparsity threshold ~s020-s025（D063; s030 待定）。Cohen's d（per-problem paired, B=10000）从 medium 到 large（DeepSeek: 0.61→1.13; Qwen: 0.37→1.44，registry cohens_d s015→s030）。LLaMA 跨架构验证（D060）qualitative direction consistent（within-importance d_z~1.0），但 strategy×phase 交互弱于 Qwen2 架构（imp_vs_rand d_z 0.19→0.34, 仅 s030 显著），且 random 在 LLaMA 上也显示显著 phase gradient（d_z 0.35→0.44），与 DeepSeek/Qwen random 低 sparsity NS 模式定性不同。GSM8K 跨 benchmark 验证（D075）：importance masking 的 phase gradient 在 GSM8K 上同样单调递增（QW: 0.039→0.158→1.100→2.092; DS: 0.241→0.740→1.992→4.682），但 strategy specificity（importance/random gradient ratio）从 MATH-500 的 15-36× 衰减至 GSM8K 的 2.3-3.8×。注意：\\\"反转\\\"仅在原始 II_low 值上（random > importance），phase gradient 层面 importance ≥ random。Strategy specificity 的 task-dependence 机制是开放问题（见 §6 Discussion）。这一发现挑战了 compound degradation 均匀分布的隐含假设。\\n\\n**数字基准**：所有数字基于 bf16 per-problem paired 统计量（B=10000 bootstrap）。median_diff 定义为 median(II_low_i − II_high_i)（逐 problem 配对差的中位数）。fp16 旧数据已弃用。\\n\\n## Narrative Arc\\n\\nCompound sparsity 是高效 LLM 推理的实用部署需求，但 prior work（SparK, Ada-KV, SLiM）将 compound interaction 视为均匀超可加。我们发现 severity 是 strategy × phase 交互的涌现属性：importance eviction 的 compound interaction 在 low-sparsity phase 远大于 high-sparsity phase（paired median difference 单调递增 0.39→8.48），而 random eviction 在低 sparsity (s015/s020) NS，在 s025+ 跨模型显著但效应量远小于 importance (2.7-15×)——存在 sparsity threshold (~s020-s025)，低于阈值 compound effect importance-specific，高于阈值两者均触发但 importance 主导。Cross-model replication 方向一致（Qwen magnitude ~1/4 of DeepSeek，onset threshold s≥0.20）。LLaMA 跨架构验证已完成（c3_llama, D060）：qualitative direction consistent（importance phase gradient d_z≈1.0），但 imp_vs_rand 交互弱（d_z 0.19→0.34, 仅 s030 显著），且 random 也显示非平凡 phase gradient（d_z 0.35→0.44），strategy-dependence 强度 architecture-dependent。我们通过 discrimination collapse 机制解释这一现象：head pruning → importance score 的判别力崩塌（Gini/CV 下降跨模型一致）→ importance eviction 退化为有偏伪随机。Attention entropy redistribution 作为 model-dependent secondary effect 在 DeepSeek 上观察到，但在 Qwen 上不稳健（D044）。\\n\\n**Framing 硬约束（D015）**：\\n- MUST: \\\\\\\\\\\\\\\"emergent phase-strategy interaction\\\\\\\\\\\\\\\"\\n- MUST NOT: \\\\\\\\\\\\\\\"importance metric limitation / importance is broken\\\\\\\\\\\\\\\"\\n- MUST NOT: claim \\\\\\\\\\\\\\\"importance masking produces super-additive interaction\\\\\\\\\\\\\\\" without qualifier — random masking also produces positive II, and at s025+ random is statistically significant (D063). The distinguishing signal is **magnitude gradient** (importance 2.7-15× larger) and **onset threshold** (random NS below ~s020, importance significant from s015+), not the existence of super-additivity itself (D023)\\n\\n## Core Claims\\n\\n| ID | Claim | Status | Key Evidence |\\n|----|-------|--------|-------------|\\n| C1 | Compound sparsity severity is strategy- and task-modulated | confirmed | MATH-500: importance gradient 15-36× random; GSM8K: ratio 衰减至 2.3-3.8× (D075)。Phase gradient 层面 importance ≥ random 跨 benchmark 成立，但 magnitude ratio task-dependent。Threshold ~s020-s025 (D063) |\\n| C2 | Severity is phase-modulated (amplified in low-sparsity phase) | confirmed | bf16 paired median difference 单调递增: 0.39→1.21→3.99→8.48; Bonferroni p<0.005 全 4 水平 (D032)。预注册：n=500 后若 QW s015 CI 仍跨零，叙事改为 'compound effect emerges above threshold sparsity (~s020)' |\\n| C3 | Phase-strategy crossover exists | confirmed | s=0.25: importance high_phase=0.032 < random=0.818, importance low_phase=7.196 > random=1.363 (bf16) |\\n| C4 | Discrimination collapse as primary mechanism; entropy redistribution model-dependent | partially_confirmed | D044: Gini/CV 下降跨模型一致; entropy collapse DeepSeek 一致但 Qwen s025 反转(+0.045) s030≈0。30/30 problems completed. |\\n| C5 | Phase-modulated compound severity generalizes across models | confirmed | DeepSeek + Qwen cross-model replication: 方向一致, Cohen's d ρ=1.0, gradient permutation p=0.043. Qwen magnitude ~1/4 of DeepSeek, onset threshold s≥0.20 (S3→C). |\\n| C5b | Phase-aware mitigation recovers compound degradation | future_work | D056: pilot 完成 gate_failed。Oracle recovery 18% < 30% gate (Wilcoxon p=0.002)，heuristic 32% 但 CI 跨零。方向正确但效应量不足，需更精细 phase boundary estimation → future work |\\n| C6 | Severity gradient is sub-exponential | confirmed | Growth rate decreasing: Δ增长因子 3.8×→4.8×→2.0×（递减） |\\n| C7 | Statistical power at n=500 confirms dose-response | confirmed | c2_n500_deepseek (success) + c2_qw_n500_r3 (success): 两模型 n=500 全 4 sparsity Bonferroni p<0.005, Spearman ρ=1.0 |\\n| C8 | Cross-architecture validation (LLaMA) | partially_confirmed | D060: within-importance phase gradient 强(d_z~1.0) ✓，但 imp_vs_rand 交互弱(d_z 0.19→0.34, 仅 s030 Bonferroni p=0.029 显著)。**关键**：random 在 LLaMA 上也显示显著 phase gradient(d_z 0.35→0.44, CI 排除零)，与 DeepSeek/Qwen random 低 sparsity NS 模式定性不同。Qualitative direction consistent, quantitative strategy×phase interaction weaker + architecture-dependent。论文禁用 \\\"confirms\\\"，改用 \\\"suggests\\\"/\\\"provides partial support\\\"。 |\\n| C9 | Differentiation from Lethe/SparK prior work | planned | Related Work §2 引用区分 + SparK gap analysis |\\n| S3→C | Onset threshold is model-dependent (DeepSeek s≥0.15, Qwen s≥0.20) | confirmed | D037/D038: Qwen s015 d_z=0.37 CI含0, s020+ 显著 |\\n| C10 | Phase gradient cross-benchmark robust; strategy specificity task-modulated | confirmed | GSM8K DS gradient 0.241→4.682 单调递增; QW gradient 0.039→2.092; imp/rand ratio 衰减至 2.3-3.8× (D075)。QW random s025+s030 均 success |\\n| S7→C | Dose-response monotonicity (Spearman ρ=1.0) | confirmed | D047: 6-point dose-response, 单调递增 |\\n\\n## Anticipated Reviewer Concerns\\n\\n### RC1: Generalizability — 7B models only, benchmark scope\\n- **预期质疑**: \\\\\\\"Results on two 7B models and MATH-500 only. How do we know this generalizes to larger models or other reasoning tasks?\\\\\\\"\\n- **应对**: 四层泛化证据：(1) Cross-model: DeepSeek-R1-Distill-Qwen-7B + Qwen2.5-7B-Instruct（同架构不同训练，ρ=1.0）(2) Cross-architecture: c3_llama (DeepSeek-R1-Distill-Llama-8B, LlamaForCausalLM)，qualitative direction consistent，但需加限定——LLaMA 上 random 也显示 phase gradient，strategy × phase 交互弱于 Qwen2 架构（D060）(3) **Cross-benchmark (D075)**: GSM8K（两模型）phase gradient 单调递增复现（DS: 0.241→4.682; QW: 0.039→2.092），但 strategy specificity ratio 从 MATH-500 15-36× 衰减至 2.3-3.8×，表明 phase modulation 跨 benchmark 稳健而 magnitude modulation task-dependent。Limitations 诚实声明：(a) 7B scale only；(b) strategy specificity 强度 task-dependent（GSM8K 衰减，可能因推理链更短）；(c) LLaMA 跨架构验证 n=50 限制功效；(d) random phase gradient 行为 architecture-dependent。\\n- **实验支撑**: C5 (cross-model) + C8 (c3_llama cross-architecture) + C10 (cross-benchmark GSM8K, D075)\\n\\n### RC2: Mechanism — entropy-discrimination collapse 缺乏直接测量\\n- **预期质疑**: \\\\\\\"The mechanism is conceptual. Where is the empirical evidence for entropy increase and discrimination collapse?\\\\\\\"\\n- **应对**: c4_entropy 实验已完成（DeepSeek 30/30 + Qwen 30/30）。D044 结论：Gini/CV 下降跨模型一致（discrimination collapse confirmed）；entropy redistribution 在 DeepSeek 上一致但在 Qwen 上 s025 方向反转、s030 近零（model-dependent）。论文以 discrimination collapse 为主线，entropy 作 DeepSeek 特有的强化因素。\\n- **实验支撑**: c4_entropy (DeepSeek DONE) + qwen_c4_entropy (DONE, negative for entropy universality)\\n\\n### RC3: Practical impact — 没有 throughput 数据\\n- **预期质疑**: \\\\\\\"No wall-clock or throughput measurements. Is the severity amplification reflected in actual inference speed?\\\\\\\"\\n- **应对**: 本文定位是 empirical finding paper（发现 + 机制解释），不是 method paper。Throughput 不是 claim 的一部分。Discussion 中明确 phase-gated controller 作为 future direction。\\n  - C5b pilot 已完成（D056）：oracle recovery 18%（Wilcoxon p=0.002），heuristic recovery 32%（p=0.024），但两者 95% CI 均跨零。方向正确（Wilcoxon 显著）但效应量不足（未达 30% gate），需更精细的 phase boundary estimation。论文 §6 Discussion 诚实报告 pilot 结果 + future work。\\n  - Heuristic > oracle 悖论值得提及：token position ratio 粗粒度划分可能恰好更适合 mitigation 场景，暗示 phase boundary 的最优粒度是开放问题。\\n- **实验支撑**: c5b_pilot (gate_failed, D056)\\n\\n### RC4: Statistical rigor — bootstrap 是否足够\\n- **预期质疑**: \\\\\\\"Per-problem bootstrap with 50 problems — sufficient sample size?\\\\\\\"\\n- **应对**: bf16 使用 B=10000 per-problem paired bootstrap，有效配对数 n=49 (DeepSeek) / n=46 (Qwen)；n=500 实验进一步验证 (C7 running)。Permutation test 使用 paired median difference 作为 robust statistic（D032），Bonferroni 校正后全 4 水平 p<0.005。Dose-response 主用 Wilcoxon signed-rank p + median_diff（robust to outliers），Cohen's d 作为辅助效应量（DeepSeek 0.61→1.13, Qwen 0.37→1.44, registry cohens_d s015→s030），注释高 sparsity 下 d 受 outlier-driven variance 影响（DS s020→s025: median 3.3× jump 但 d 非单调，因极端 II 值影响分母，D064）。可在 appendix 补充 per-problem 分布图（已生成 fig4_per_problem_dist.pdf）。\\n- **实验支撑**: bf16 permutation test (D032) + Cohen's d per-problem paired (rebootstrap B=10000) + n=500 Wilcoxon (C7 running)\\n\\n### RC5: Novelty — prior work 是否已覆盖 phase-dependent sparsity\\n- **预期质疑**: \\\"ThinKV and phase-aware methods already consider phase. What's new?\\\"\\n- **应对**: Prior work 在单轴上分析 phase（ThinKV: phase-aware eviction）或 compound（SparK: joint compression）。没有工作同时分析 compound × phase × strategy 的三维交互。Crossover 现象（同一 strategy 在不同 phase 方向反转）是全新发现。Related Work 加 Lethe 引用区分 + SparK 对比。具体区分：\\n  - **ThinKV** (arxiv 2510.01290, Oct 2025): 在 KV cache 单轴上做 phase-aware 压缩（按 CoT 阶段差异化 eviction），但不涉及 pruning × eviction 的 compound interaction。我们研究的是双轴（head pruning × KV eviction）compound interaction 如何随 phase 变化，ThinKV 的单轴 phase-aware 策略是我们分析维度的子集。\\n  - **Physics of KV Cache Compression** (arxiv 2603.01426, Mar 2026): 揭示了单轴 KV 压缩的 phase transition 和 representational rigidity，是机制层面最接近的工作。关键区分：他们刻画的是单一压缩轴上压缩率的 critical threshold（phase transition），我们刻画的是两种压缩方法的 compound interaction severity 如何被 reasoning phase 调制（phase-dependent gradient）——维度正交。\\n  - **HIES** (arxiv 2510.13832, Oct 2025): 发现 importance score collapse 并提出 entropy 补偿，为我们的 discrimination collapse 机制提供独立 supporting evidence——他们在单轴上观察到的 score collapse 正是我们在 compound setting 中发现的 Gini/CV 下降的单轴对应。\\n  - **R-KV** (arxiv 2505.24133, May 2025): 针对 reasoning task 做 KV compression 优化，属于 task-specific method。我们不是提出新方法，而是 mechanistic 分析 compound interaction 的 phase-dependent 行为，二者目标不同（optimization vs understanding）。\\n- **实验支撑**: C3 (crossover), Related Work §2 的 gap 分析\\n\\n### RC6: Novelty vs Lethe/SparK\\n- **预期质疑**: \\\"How does this differ from Lethe (AAAI 2026) which also does layer-time-adaptive KV pruning, or SparK which studies compound compression?\\\"\\n- **应对**: Lethe 和 SparK 都没有分析 phase × strategy 的交互效应。Lethe 是 method paper（提出 adaptive eviction 方法），我们是 empirical finding paper（发现 phase-dependent severity gradient）。SparK 研究 compound compression 但将 interaction 视为均匀超可加，我们发现 interaction severity 随 phase 和 strategy 变化。新近工作进一步确认我们的独特定位：\\n  - **Physics of KV Cache Compression** (arxiv 2603.01426, Mar 2026) 是最近的相关工作，研究单轴压缩的 phase transition 阈值行为。与我们的核心区别：他们的 phase transition 是压缩率维度上的 critical point，我们的 phase-dependent gradient 是 reasoning phase 维度上 compound interaction 的连续调制——两者刻画的 \\\"phase\\\" 语义不同（compression-rate phase vs reasoning phase）。\\n  - **ThinKV** (arxiv 2510.01290, Oct 2025) 和 **R-KV** (arxiv 2505.24133, May 2025) 都在 KV compression 单轴上引入 phase/reasoning awareness，但均未涉及 compound interaction。我们的贡献在于揭示 pruning × eviction 双轴交互如何被 reasoning phase 调制，这是单轴方法无法观察到的涌现现象。\\n  - **HIES** (arxiv 2510.13832, Oct 2025) 的 importance score collapse 发现为我们的 discrimination collapse 机制提供了独立佐证，但 HIES 聚焦于单轴补偿方法，未研究 collapse 在 compound setting 中的放大效应。\\n  - Related Work §2 明确区分三者定位：Lethe/SparK = method/compound method, ThinKV/R-KV = single-axis phase-aware, Physics of KV = single-axis phase transition, HIES = single-axis collapse。我们 = compound × phase × strategy 三维交互分析。\\n- **实验支撑**: 不需要额外实验，仅需 §2 引用区分\\n\\n## Paper Positioning\\n\\n**类型**: Empirical finding paper（非 method paper）\\n**核心贡献**:\\n1. 发现 compound sparsity severity 的 strategy × phase 交互\\n2. 量化 severity gradient（bf16 paired median difference 0.39→8.48, Cohen's d 0.61→1.13）和 crossover 现象\\n3. 提出 discrimination collapse 机制解释（Gini/CV 跨模型一致；entropy redistribution model-dependent）\\n4. Cross-model + cross-architecture (LLaMA) replication 验证泛化性（三模型两架构；LLaMA partially_confirmed，strategy×phase 交互强度 architecture-dependent, D060）\\n\\n**投稿目标**: EMNLP 2026 ARR, deadline 2026-05-25\\n**Rebuttal 准备**: Day 9 (2026-05-23) 预留 rebuttal letter 写作时间\\n**关键时间线**：\\n- Day 9 (2026-05-23): 预留写 rebuttal letter\\n- Day 11 (2026-05-25): EMNLP 2026 ARR 截稿\\n\", \"total_chars\": 12640, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e127786f-a191-4d01-b58d-071eb9fc50fc",
  "uuid": "0c86e47f-1402-4305-a20e-534252e18b49",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing — Phase-Gated Compound Sparsity\\\\n\\\\n> 最后更新: 2026-05-16 (数值对齐 n=500 registry: DS median_diff 0.39/1.21/3.99/8.48; QW 0.07/0.31/1.07/3.16; Cohen's d registry 0.61→1.13/0.37→1.44; C7+C10 status→confirmed; imp/rand 2.7-15×) | 维护者: Director\\\\n\\\\n## Core Insight\\\\n\\\\nCompound sparsity（attention head pruning + KV cache eviction）的 severity 不是固定常数——它是 eviction strategy 和 reasoning phase 交互的涌现属性。Importance-based eviction 的 compound interaction severity（paired median difference: median(II_low_i − II_high_i)）随 sparsity 单调递增（DeepSeek: 0.39→1.21→3.99→8.48; Qwen: 0.07→0.31→1.07→3.16），而 random masking 在 s015/s020 NS，在 s025 跨模型显著但效应量远小于 importance（DS: 0.257 vs 3.986; QW: 0.393 vs 1.074, 2.7-15×差异），存在 sparsity threshold ~s020-s025（D063; s030 待定）。Cohen's d（per-problem paired, B=10000）从 medium 到 large（DeepSeek: 0.61→1.13; Qwen: 0.37→1.44，registry cohens_d s015→s030）。LLaMA 跨架构验证（D060）qualitative direction consistent（within-importance d_z~1.0），但 strategy×phase 交互弱于 Qwen2 架构（imp_vs_rand d_z 0.19→0.34, 仅 s030 显著），且 random 在 LLaMA 上也显示显著 phase gradient（d_z 0.35→0.44），与 DeepSeek/Qwen random 低 sparsity NS 模式定性不同。GSM8K 跨 benchmark 验证（D075）：importance masking 的 phase gradient 在 GSM8K 上同样单调递增（QW: 0.039→0.158→1.100→2.092; DS: 0.241→0.740→1.992→4.682），但 strategy specificity（importance/random gradient ratio）从 MATH-500 的 15-36× 衰减至 GSM8K 的 2.3-3.8×。注意：\\\\\\\"反转\\\\\\\"仅在原始 II_low 值上（random > importance），phase gradient 层面 importance ≥ random。Strategy specificity 的 task-dependence 机制是开放问题（见 §6 Discussion）。这一发现挑战了 compound degradation 均匀分布的隐含假设。\\\\n\\\\n**数字基准**：所有数字基于 bf16 per-problem paired 统计量（B=10000 bootstrap）。median_diff 定义为 median(II_low_i − II_high_i)（逐 problem 配对差的中位数）。fp16 旧数据已弃用。\\\\n\\\\n## Narrative Arc\\\\n\\\\nCompound sparsity 是高效 LLM 推理的实用部署需求，但 prior work（SparK, Ada-KV, SLiM）将 compound interaction 视为均匀超可加。我们发现 severity 是 strategy × phase 交互的涌现属性：importance eviction 的 compound interaction 在 low-sparsity phase 远大于 high-sparsity phase（paired median difference 单调递增 0.39→8.48），而 random eviction 在低 sparsity (s015/s020) NS，在 s025+ 跨模型显著但效应量远小于 importance (2.7-15×)——存在 sparsity threshold (~s020-s025)，低于阈值 compound effect importance-specific，高于阈值两者均触发但 importance 主导。Cross-model replication 方向一致（Qwen magnitude ~1/4 of DeepSeek，onset threshold s≥0.20）。LLaMA 跨架构验证已完成（c3_llama, D060）：qualitative direction consistent（importance phase gradient d_z≈1.0），但 imp_vs_rand 交互弱（d_z 0.19→0.34, 仅 s030 显著），且 random 也显示非平凡 phase gradient（d_z 0.35→0.44），strategy-dependence 强度 architecture-dependent。我们通过 discrimination collapse 机制解释这一现象：head pruning → importance score 的判别力崩塌（Gini/CV 下降跨模型一致）→ importance eviction 退化为有偏伪随机。Attention entropy redistribution 作为 model-dependent secondary effect 在 DeepSeek 上观察到，但在 Qwen 上不稳健（D044）。\\\\n\\\\n**Framing 硬约束（D015）**：\\\\n- MUST: \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"emergent phase-strategy interaction\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"\\\\n- MUST NOT: \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"importance metric limitation / importance is broken\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"\\\\n- MUST NOT: claim \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"importance masking produces super-additive interaction\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\" without qualifier — random masking also produces positive II, and at s025+ random is statistically significant (D063). The distinguishing signal is **magnitude gradient** (importance 2.7-15× larger) and **onset threshold** (random NS below ~s020, importance significant from s015+), not the existence of super-additivity itself (D023)\\\\n\\\\n## Core Claims\\\\n\\\\n| ID | Claim | Status | Key Evidence |\\\\n|----|-------|--------|-------------|\\\\n| C1 | Compound sparsity severity is strategy- and task-modulated | confirmed | MATH-500: importance gradient 15-36× random; GSM8K: ratio 衰减至 2.3-3.8× (D075)。Phase gradient 层面 importance ≥ random 跨 benchmark 成立，但 magnitude ratio task-dependent。Threshold ~s020-s025 (D063) |\\\\n| C2 | Severity is phase-modulated (amplified in low-sparsity phase) | confirmed | bf16 paired median difference 单调递增: 0.39→1.21→3.99→8.48; Bonferroni p<0.005 全 4 水平 (D032)。预注册：n=500 后若 QW s015 CI 仍跨零，叙事改为 'compound effect emerges above threshold sparsity (~s020)' |\\\\n| C3 | Phase-strategy crossover exists | confirmed | s=0.25: importance high_phase=0.032 < random=0.818, importance low_phase=7.196 > random=1.363 (bf16) |\\\\n| C4 | Discrimination collapse as primary mechanism; entropy redistribution model-dependent | partially_confirmed | D044: Gini/CV 下降跨模型一致; entropy collapse DeepSeek 一致但 Qwen s025 反转(+0.045) s030≈0。30/30 problems completed. |\\\\n| C5 | Phase-modulated compound severity generalizes across models | confirmed | DeepSeek + Qwen cross-model replication: 方向一致, Cohen's d ρ=1.0, gradient permutation p=0.043. Qwen magnitude ~1/4 of DeepSeek, onset threshold s≥0.20 (S3→C). |\\\\n| C5b | Phase-aware mitigation recovers compound degradation | future_work | D056: pilot 完成 gate_failed。Oracle recovery 18% < 30% gate (Wilcoxon p=0.002)，heuristic 32% 但 CI 跨零。方向正确但效应量不足，需更精细 phase boundary estimation → future work |\\\\n| C6 | Severity gradient is sub-exponential | confirmed | Growth rate decreasing: Δ增长因子 3.8×→4.8×→2.0×（递减） |\\\\n| C7 | Statistical power at n=500 confirms dose-response | confirmed | c2_n500_deepseek (success) + c2_qw_n500_r3 (success): 两模型 n=500 全 4 sparsity Bonferroni p<0.005, Spearman ρ=1.0 |\\\\n| C8 | Cross-architecture validation (LLaMA) | partially_confirmed | D060: within-importance phase gradient 强(d_z~1.0) ✓，但 imp_vs_rand 交互弱(d_z 0.19→0.34, 仅 s030 Bonferroni p=0.029 显著)。**关键**：random 在 LLaMA 上也显示显著 phase gradient(d_z 0.35→0.44, CI 排除零)，与 DeepSeek/Qwen random 低 sparsity NS 模式定性不同。Qualitative direction consistent, quantitative strategy×phase interaction weaker + architecture-dependent。论文禁用 \\\\\\\"confirms\\\\\\\"，改用 \\\\\\\"suggests\\\\\\\"/\\\\\\\"provides partial support\\\\\\\"。 |\\\\n| C9 | Differentiation from Lethe/SparK prior work | planned | Related Work §2 引用区分 + SparK gap analysis |\\\\n| S3→C | Onset threshold is model-dependent (DeepSeek s≥0.15, Qwen s≥0.20) | confirmed | D037/D038: Qwen s015 d_z=0.37 CI含0, s020+ 显著 |\\\\n| C10 | Phase gradient cross-benchmark robust; strategy specificity task-modulated | confirmed | GSM8K DS gradient 0.241→4.682 单调递增; QW gradient 0.039→2.092; imp/rand ratio 衰减至 2.3-3.8× (D075)。QW random s025+s030 均 success |\\\\n| S7→C | Dose-response monotonicity (Spearman ρ=1.0) | confirmed | D047: 6-point dose-response, 单调递增 |\\\\n\\\\n## Anticipated Reviewer Concerns\\\\n\\\\n### RC1: Generalizability — 7B models only, benchmark scope\\\\n- **预期质疑**: \\\\\\\\\\\\\\\"Results on two 7B models and MATH-500 only. How do we know this generalizes to larger models or other reasoning tasks?\\\\\\\\\\\\\\\"\\\\n- **应对**: 四层泛化证据：(1) Cross-model: DeepSeek-R1-Distill-Qwen-7B + Qwen2.5-7B-Instruct（同架构不同训练，ρ=1.0）(2) Cross-architecture: c3_llama (DeepSeek-R1-Distill-Llama-8B, LlamaForCausalLM)，qualitative direction consistent，但需加限定——LLaMA 上 random 也显示 phase gradient，strategy × phase 交互弱于 Qwen2 架构（D060）(3) **Cross-benchmark (D075)**: GSM8K（两模型）phase gradient 单调递增复现（DS: 0.241→4.682; QW: 0.039→2.092），但 strategy specificity ratio 从 MATH-500 15-36× 衰减至 2.3-3.8×，表明 phase modulation 跨 benchmark 稳健而 magnitude modulation task-dependent。Limitations 诚实声明：(a) 7B scale only；(b) strategy specificity 强度 task-dependent（GSM8K 衰减，可能因推理链更短）；(c) LLaMA 跨架构验证 n=50 限制功效；(d) random phase gradient 行为 architecture-dependent。\\\\n- **实验支撑**: C5 (cross-model) + C8 (c3_llama cross-architecture) + C10 (cross-benchmark GSM8K, D075)\\\\n\\\\n### RC2: Mechanism — entropy-discrimination collapse 缺乏直接测量\\\\n- **预期质疑**: \\\\\\\\\\\\\\\"The mechanism is conceptual. Where is the empirical evidence for entropy increase and discrimination collapse?\\\\\\\\\\\\\\\"\\\\n- **应对**: c4_entropy 实验已完成（DeepSeek 30/30 + Qwen 30/30）。D044 结论：Gini/CV 下降跨模型一致（discrimination collapse confirmed）；entropy redistribution 在 DeepSeek 上一致但在 Qwen 上 s025 方向反转、s030 近零（model-dependent）。论文以 discrimination collapse 为主线，entropy 作 DeepSeek 特有的强化因素。\\\\n- **实验支撑**: c4_entropy (DeepSeek DONE) + qwen_c4_entropy (DONE, negative for entropy universality)\\\\n\\\\n### RC3: Practical impact — 没有 throughput 数据\\\\n- **预期质疑**: \\\\\\\\\\\\\\\"No wall-clock or throughput measurements. Is the severity amplification reflected in actual inference speed?\\\\\\\\\\\\\\\"\\\\n- **应对**: 本文定位是 empirical finding paper（发现 + 机制解释），不是 method paper。Throughput 不是 claim 的一部分。Discussion 中明确 phase-gated controller 作为 future direction。\\\\n  - C5b pilot 已完成（D056）：oracle recovery 18%（Wilcoxon p=0.002），heuristic recovery 32%（p=0.024），但两者 95% CI 均跨零。方向正确（Wilcoxon 显著）但效应量不足（未达 30% gate），需更精细的 phase boundary estimation。论文 §6 Discussion 诚实报告 pilot 结果 + future work。\\\\n  - Heuristic > oracle 悖论值得提及：token position ratio 粗粒度划分可能恰好更适合 mitigation 场景，暗示 phase boundary 的最优粒度是开放问题。\\\\n- **实验支撑**: c5b_pilot (gate_failed, D056)\\\\n\\\\n### RC4: Statistical rigor — bootstrap 是否足够\\\\n- **预期质疑**: \\\\\\\\\\\\\\\"Per-problem bootstrap with 50 problems — sufficient sample size?\\\\\\\\\\\\\\\"\\\\n- **应对**: bf16 使用 B=10000 per-problem paired bootstrap，有效配对数 n=49 (DeepSeek) / n=46 (Qwen)；n=500 实验进一步验证 (C7 running)。Permutation test 使用 paired median difference 作为 robust statistic（D032），Bonferroni 校正后全 4 水平 p<0.005。Dose-response 主用 Wilcoxon signed-rank p + median_diff（robust to outliers），Cohen's d 作为辅助效应量（DeepSeek 0.61→1.13, Qwen 0.37→1.44, registry cohens_d s015→s030），注释高 sparsity 下 d 受 outlier-driven variance 影响（DS s020→s025: median 3.3× jump 但 d 非单调，因极端 II 值影响分母，D064）。可在 appendix 补充 per-problem 分布图（已生成 fig4_per_problem_dist.pdf）。\\\\n- **实验支撑**: bf16 permutation test (D032) + Cohen's d per-problem paired (rebootstrap B=10000) + n=500 Wilcoxon (C7 running)\\\\n\\\\n### RC5: Novelty — prior work 是否已覆盖 phase-dependent sparsity\\\\n- **预期质疑**: \\\\\\\"ThinKV and phase-aware methods already consider phase. What's new?\\\\\\\"\\\\n- **应对**: Prior work 在单轴上分析 phase（ThinKV: phase-aware eviction）或 compound（SparK: joint compression）。没有工作同时分析 compound × phase × strategy 的三维交互。Crossover 现象（同一 strategy 在不同 phase 方向反转）是全新发现。Related Work 加 Lethe 引用区分 + SparK 对比。具体区分：\\\\n  - **ThinKV** (arxiv 2510.01290, Oct 2025): 在 KV cache 单轴上做 phase-aware 压缩（按 CoT 阶段差异化 eviction），但不涉及 pruning × eviction 的 compound interaction。我们研究的是双轴（head pruning × KV eviction）compound interaction 如何随 phase 变化，ThinKV 的单轴 phase-aware 策略是我们分析维度的子集。\\\\n  - **Physics of KV Cache Compression** (arxiv 2603.01426, Mar 2026): 揭示了单轴 KV 压缩的 phase transition 和 representational rigidity，是机制层面最接近的工作。关键区分：他们刻画的是单一压缩轴上压缩率的 critical threshold（phase transition），我们刻画的是两种压缩方法的 compound interaction severity 如何被 reasoning phase 调制（phase-dependent gradient）——维度正交。\\\\n  - **HIES** (arxiv 2510.13832, Oct 2025): 发现 importance score collapse 并提出 entropy 补偿，为我们的 discrimination collapse 机制提供独立 supporting evidence——他们在单轴上观察到的 score collapse 正是我们在 compound setting 中发现的 Gini/CV 下降的单轴对应。\\\\n  - **R-KV** (arxiv 2505.24133, May 2025): 针对 reasoning task 做 KV compression 优化，属于 task-specific method。我们不是提出新方法，而是 mechanistic 分析 compound interaction 的 phase-dependent 行为，二者目标不同（optimization vs understanding）。\\\\n- **实验支撑**: C3 (crossover), Related Work §2 的 gap 分析\\\\n\\\\n### RC6: Novelty vs Lethe/SparK\\\\n- **预期质疑**: \\\\\\\"How does this differ from Lethe (AAAI 2026) which also does layer-time-adaptive KV pruning, or SparK which studies compound compression?\\\\\\\"\\\\n- **应对**: Lethe 和 SparK 都没有分析 phase × strategy 的交互效应。Lethe 是 method paper（提出 adaptive eviction 方法），我们是 empirical finding paper（发现 phase-dependent severity gradient）。SparK 研究 compound compression 但将 interaction 视为均匀超可加，我们发现 interaction severity 随 phase 和 strategy 变化。新近工作进一步确认我们的独特定位：\\\\n  - **Physics of KV Cache Compression** (arxiv 2603.01426, Mar 2026) 是最近的相关工作，研究单轴压缩的 phase transition 阈值行为。与我们的核心区别：他们的 phase transition 是压缩率维度上的 critical point，我们的 phase-dependent gradient 是 reasoning phase 维度上 compound interaction 的连续调制——两者刻画的 \\\\\\\"phase\\\\\\\" 语义不同（compression-rate phase vs reasoning phase）。\\\\n  - **ThinKV** (arxiv 2510.01290, Oct 2025) 和 **R-KV** (arxiv 2505.24133, May 2025) 都在 KV compression 单轴上引入 phase/reasoning awareness，但均未涉及 compound interaction。我们的贡献在于揭示 pruning × eviction 双轴交互如何被 reasoning phase 调制，这是单轴方法无法观察到的涌现现象。\\\\n  - **HIES** (arxiv 2510.13832, Oct 2025) 的 importance score collapse 发现为我们的 discrimination collapse 机制提供了独立佐证，但 HIES 聚焦于单轴补偿方法，未研究 collapse 在 compound setting 中的放大效应。\\\\n  - Related Work §2 明确区分三者定位：Lethe/SparK = method/compound method, ThinKV/R-KV = single-axis phase-aware, Physics of KV = single-axis phase transition, HIES = single-axis collapse。我们 = compound × phase × strategy 三维交互分析。\\\\n- **实验支撑**: 不需要额外实验，仅需 §2 引用区分\\\\n\\\\n## Paper Positioning\\\\n\\\\n**类型**: Empirical finding paper（非 method paper）\\\\n**核心贡献**:\\\\n1. 发现 compound sparsity severity 的 strategy × phase 交互\\\\n2. 量化 severity gradient（bf16 paired median difference 0.39→8.48, Cohen's d 0.61→1.13）和 crossover 现象\\\\n3. 提出 discrimination collapse 机制解释（Gini/CV 跨模型一致；entropy redistribution model-dependent）\\\\n4. Cross-model + cross-architecture (LLaMA) replication 验证泛化性（三模型两架构；LLaMA partially_confirmed，strategy×phase 交互强度 architecture-dependent, D060）\\\\n\\\\n**投稿目标**: EMNLP 2026 ARR, deadline 2026-05-25\\\\n**Rebuttal 准备**: Day 9 (2026-05-23) 预留 rebuttal letter 写作时间\\\\n**关键时间线**：\\\\n- Day 9 (2026-05-23): 预留写 rebuttal letter\\\\n- Day 11 (2026-05-25): EMNLP 2026 ARR 截稿\\\\n\\\", \\\"total_chars\\\": 12640, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper_framing.md\", \"content\": \"# Paper Framing — Phase-Gated Compound Sparsity\\n\\n> 最后更新: 2026-05-16 (数值对齐 n=500 registry: DS median_diff 0.39/1.21/3.99/8.48; QW 0.07/0.31/1.07/3.16; Cohen's d registry 0.61→1.13/0.37→1.44; C7+C10 status→confirmed; imp/rand 2.7-15×) | 维护者: Director\\n\\n## Core Insight\\n\\nCompound sparsity（attention head pruning + KV cache eviction）的 severity 不是固定常数——它是 eviction strategy 和 reasoning phase 交互的涌现属性。Importance-based eviction 的 compound interaction severity（paired median difference: median(II_low_i − II_high_i)）随 sparsity 单调递增（DeepSeek: 0.39→1.21→3.99→8.48; Qwen: 0.07→0.31→1.07→3.16），而 random masking 在 s015/s020 NS，在 s025 跨模型显著但效应量远小于 importance（DS: 0.257 vs 3.986; QW: 0.393 vs 1.074, 2.7-15×差异），存在 sparsity threshold ~s020-s025（D063; s030 待定）。Cohen's d（per-problem paired, B=10000）从 medium 到 large（DeepSeek: 0.61→1.13; Qwen: 0.37→1.44，registry cohens_d s015→s030）。LLaMA 跨架构验证（D060）qualitative direction consistent（within-importance d_z~1.0），但 strategy×phase 交互弱于 Qwen2 架构（imp_vs_rand d_z 0.19→0.34, 仅 s030 显著），且 random 在 LLaMA 上也显示显著 phase gradient（d_z 0.35→0.44），与 DeepSeek/Qwen random 低 sparsity NS 模式定性不同。GSM8K 跨 benchmark 验证（D075）：importance masking 的 phase gradient 在 GSM8K 上同样单调递增（QW: 0.039→0.158→1.100→2.092; DS: 0.241→0.740→1.992→4.682），但 strategy specificity（importance/random gradient ratio）从 MATH-500 的 15-36× 衰减至 GSM8K 的 2.3-3.8×。注意：\\\"反转\\\"仅在原始 II_low 值上（random > importance），phase gradient 层面 importance ≥ random。Strategy specificity 的 task-dependence 机制是开放问题（见 §6 Discussion）。这一发现挑战了 compound degradation 均匀分布的隐含假设。\\n\\n**数字基准**：所有数字基于 bf16 per-problem paired 统计量（B=10000 bootstrap）。median_diff 定义为 median(II_low_i − II_high_i)（逐 problem 配对差的中位数）。fp16 旧数据已弃用。\\n\\n## Narrative Arc\\n\\nCompound sparsity 是高效 LLM 推理的实用部署需求，但 prior work（SparK, Ada-KV, SLiM）将 compound interaction 视为均匀超可加。我们发现 severity 是 strategy × phase 交互的涌现属性：importance eviction 的 compound interaction 在 low-sparsity phase 远大于 high-sparsity phase（paired median difference 单调递增 0.39→8.48），而 random eviction 在低 sparsity (s015/s020) NS，在 s025+ 跨模型显著但效应量远小于 importance (2.7-15×)——存在 sparsity threshold (~s020-s025)，低于阈值 compound effect importance-specific，高于阈值两者均触发但 importance 主导。Cross-model replication 方向一致（Qwen magnitude ~1/4 of DeepSeek，onset threshold s≥0.20）。LLaMA 跨架构验证已完成（c3_llama, D060）：qualitative direction consistent（importance phase gradient d_z≈1.0），但 imp_vs_rand 交互弱（d_z 0.19→0.34, 仅 s030 显著），且 random 也显示非平凡 phase gradient（d_z 0.35→0.44），strategy-dependence 强度 architecture-dependent。我们通过 discrimination collapse 机制解释这一现象：head pruning → importance score 的判别力崩塌（Gini/CV 下降跨模型一致）→ importance eviction 退化为有偏伪随机。Attention entropy redistribution 作为 model-dependent secondary effect 在 DeepSeek 上观察到，但在 Qwen 上不稳健（D044）。\\n\\n**Framing 硬约束（D015）**：\\n- MUST: \\\\\\\\\\\\\\\"emergent phase-strategy interaction\\\\\\\\\\\\\\\"\\n- MUST NOT: \\\\\\\\\\\\\\\"importance metric limitation / importance is broken\\\\\\\\\\\\\\\"\\n- MUST NOT: claim \\\\\\\\\\\\\\\"importance masking produces super-additive interaction\\\\\\\\\\\\\\\" without qualifier — random masking also produces positive II, and at s025+ random is statistically significant (D063). The distinguishing signal is **magnitude gradient** (importance 2.7-15× larger) and **onset threshold** (random NS below ~s020, importance significant from s015+), not the existence of super-additivity itself (D023)\\n\\n## Core Claims\\n\\n| ID | Claim | Status | Key Evidence |\\n|----|-------|--------|-------------|\\n| C1 | Compound sparsity severity is strategy- and task-modulated | confirmed | MATH-500: importance gradient 15-36× random; GSM8K: ratio 衰减至 2.3-3.8× (D075)。Phase gradient 层面 importance ≥ random 跨 benchmark 成立，但 magnitude ratio task-dependent。Threshold ~s020-s025 (D063) |\\n| C2 | Severity is phase-modulated (amplified in low-sparsity phase) | confirmed | bf16 paired median difference 单调递增: 0.39→1.21→3.99→8.48; Bonferroni p<0.005 全 4 水平 (D032)。预注册：n=500 后若 QW s015 CI 仍跨零，叙事改为 'compound effect emerges above threshold sparsity (~s020)' |\\n| C3 | Phase-strategy crossover exists | confirmed | s=0.25: importance high_phase=0.032 < random=0.818, importance low_phase=7.196 > random=1.363 (bf16) |\\n| C4 | Discrimination collapse as primary mechanism; entropy redistribution model-dependent | partially_confirmed | D044: Gini/CV 下降跨模型一致; entropy collapse DeepSeek 一致但 Qwen s025 反转(+0.045) s030≈0。30/30 problems completed. |\\n| C5 | Phase-modulated compound severity generalizes across models | confirmed | DeepSeek + Qwen cross-model replication: 方向一致, Cohen's d ρ=1.0, gradient permutation p=0.043. Qwen magnitude ~1/4 of DeepSeek, onset threshold s≥0.20 (S3→C). |\\n| C5b | Phase-aware mitigation recovers compound degradation | future_work | D056: pilot 完成 gate_failed。Oracle recovery 18% < 30% gate (Wilcoxon p=0.002)，heuristic 32% 但 CI 跨零。方向正确但效应量不足，需更精细 phase boundary estimation → future work |\\n| C6 | Severity gradient is sub-exponential | confirmed | Growth rate decreasing: Δ增长因子 3.8×→4.8×→2.0×（递减） |\\n| C7 | Statistical power at n=500 confirms dose-response | confirmed | c2_n500_deepseek (success) + c2_qw_n500_r3 (success): 两模型 n=500 全 4 sparsity Bonferroni p<0.005, Spearman ρ=1.0 |\\n| C8 | Cross-architecture validation (LLaMA) | partially_confirmed | D060: within-importance phase gradient 强(d_z~1.0) ✓，但 imp_vs_rand 交互弱(d_z 0.19→0.34, 仅 s030 Bonferroni p=0.029 显著)。**关键**：random 在 LLaMA 上也显示显著 phase gradient(d_z 0.35→0.44, CI 排除零)，与 DeepSeek/Qwen random 低 sparsity NS 模式定性不同。Qualitative direction consistent, quantitative strategy×phase interaction weaker + architecture-dependent。论文禁用 \\\"confirms\\\"，改用 \\\"suggests\\\"/\\\"provides partial support\\\"。 |\\n| C9 | Differentiation from Lethe/SparK prior work | planned | Related Work §2 引用区分 + SparK gap analysis |\\n| S3→C | Onset threshold is model-dependent (DeepSeek s≥0.15, Qwen s≥0.20) | confirmed | D037/D038: Qwen s015 d_z=0.37 CI含0, s020+ 显著 |\\n| C10 | Phase gradient cross-benchmark robust; strategy specificity task-modulated | confirmed | GSM8K DS gradient 0.241→4.682 单调递增; QW gradient 0.039→2.092; imp/rand ratio 衰减至 2.3-3.8× (D075)。QW random s025+s030 均 success |\\n| S7→C | Dose-response monotonicity (Spearman ρ=1.0) | confirmed | D047: 6-point dose-response, 单调递增 |\\n\\n## Anticipated Reviewer Concerns\\n\\n### RC1: Generalizability — 7B models only, benchmark scope\\n- **预期质疑**: \\\\\\\"Results on two 7B models and MATH-500 only. How do we know this generalizes to larger models or other reasoning tasks?\\\\\\\"\\n- **应对**: 四层泛化证据：(1) Cross-model: DeepSeek-R1-Distill-Qwen-7B + Qwen2.5-7B-Instruct（同架构不同训练，ρ=1.0）(2) Cross-architecture: c3_llama (DeepSeek-R1-Distill-Llama-8B, LlamaForCausalLM)，qualitative direction consistent，但需加限定——LLaMA 上 random 也显示 phase gradient，strategy × phase 交互弱于 Qwen2 架构（D060）(3) **Cross-benchmark (D075)**: GSM8K（两模型）phase gradient 单调递增复现（DS: 0.241→4.682; QW: 0.039→2.092），但 strategy specificity ratio 从 MATH-500 15-36× 衰减至 2.3-3.8×，表明 phase modulation 跨 benchmark 稳健而 magnitude modulation task-dependent。Limitations 诚实声明：(a) 7B scale only；(b) strategy specificity 强度 task-dependent（GSM8K 衰减，可能因推理链更短）；(c) LLaMA 跨架构验证 n=50 限制功效；(d) random phase gradient 行为 architecture-dependent。\\n- **实验支撑**: C5 (cross-model) + C8 (c3_llama cross-architecture) + C10 (cross-benchmark GSM8K, D075)\\n\\n### RC2: Mechanism — entropy-discrimination collapse 缺乏直接测量\\n- **预期质疑**: \\\\\\\"The mechanism is conceptual. Where is the empirical evidence for entropy increase and discrimination collapse?\\\\\\\"\\n- **应对**: c4_entropy 实验已完成（DeepSeek 30/30 + Qwen 30/30）。D044 结论：Gini/CV 下降跨模型一致（discrimination collapse confirmed）；entropy redistribution 在 DeepSeek 上一致但在 Qwen 上 s025 方向反转、s030 近零（model-dependent）。论文以 discrimination collapse 为主线，entropy 作 DeepSeek 特有的强化因素。\\n- **实验支撑**: c4_entropy (DeepSeek DONE) + qwen_c4_entropy (DONE, negative for entropy universality)\\n\\n### RC3: Practical impact — 没有 throughput 数据\\n- **预期质疑**: \\\\\\\"No wall-clock or throughput measurements. Is the severity amplification reflected in actual inference speed?\\\\\\\"\\n- **应对**: 本文定位是 empirical finding paper（发现 + 机制解释），不是 method paper。Throughput 不是 claim 的一部分。Discussion 中明确 phase-gated controller 作为 future direction。\\n  - C5b pilot 已完成（D056）：oracle recovery 18%（Wilcoxon p=0.002），heuristic recovery 32%（p=0.024），但两者 95% CI 均跨零。方向正确（Wilcoxon 显著）但效应量不足（未达 30% gate），需更精细的 phase boundary estimation。论文 §6 Discussion 诚实报告 pilot 结果 + future work。\\n  - Heuristic > oracle 悖论值得提及：token position ratio 粗粒度划分可能恰好更适合 mitigation 场景，暗示 phase boundary 的最优粒度是开放问题。\\n- **实验支撑**: c5b_pilot (gate_failed, D056)\\n\\n### RC4: Statistical rigor — bootstrap 是否足够\\n- **预期质疑**: \\\\\\\"Per-problem bootstrap with 50 problems — sufficient sample size?\\\\\\\"\\n- **应对**: bf16 使用 B=10000 per-problem paired bootstrap，有效配对数 n=49 (DeepSeek) / n=46 (Qwen)；n=500 实验进一步验证 (C7 running)。Permutation test 使用 paired median difference 作为 robust statistic（D032），Bonferroni 校正后全 4 水平 p<0.005。Dose-response 主用 Wilcoxon signed-rank p + median_diff（robust to outliers），Cohen's d 作为辅助效应量（DeepSeek 0.61→1.13, Qwen 0.37→1.44, registry cohens_d s015→s030），注释高 sparsity 下 d 受 outlier-driven variance 影响（DS s020→s025: median 3.3× jump 但 d 非单调，因极端 II 值影响分母，D064）。可在 appendix 补充 per-problem 分布图（已生成 fig4_per_problem_dist.pdf）。\\n- **实验支撑**: bf16 permutation test (D032) + Cohen's d per-problem paired (rebootstrap B=10000) + n=500 Wilcoxon (C7 running)\\n\\n### RC5: Novelty — prior work 是否已覆盖 phase-dependent sparsity\\n- **预期质疑**: \\\"ThinKV and phase-aware methods already consider phase. What's new?\\\"\\n- **应对**: Prior work 在单轴上分析 phase（ThinKV: phase-aware eviction）或 compound（SparK: joint compression）。没有工作同时分析 compound × phase × strategy 的三维交互。Crossover 现象（同一 strategy 在不同 phase 方向反转）是全新发现。Related Work 加 Lethe 引用区分 + SparK 对比。具体区分：\\n  - **ThinKV** (arxiv 2510.01290, Oct 2025): 在 KV cache 单轴上做 phase-aware 压缩（按 CoT 阶段差异化 eviction），但不涉及 pruning × eviction 的 compound interaction。我们研究的是双轴（head pruning × KV eviction）compound interaction 如何随 phase 变化，ThinKV 的单轴 phase-aware 策略是我们分析维度的子集。\\n  - **Physics of KV Cache Compression** (arxiv 2603.01426, Mar 2026): 揭示了单轴 KV 压缩的 phase transition 和 representational rigidity，是机制层面最接近的工作。关键区分：他们刻画的是单一压缩轴上压缩率的 critical threshold（phase transition），我们刻画的是两种压缩方法的 compound interaction severity 如何被 reasoning phase 调制（phase-dependent gradient）——维度正交。\\n  - **HIES** (arxiv 2510.13832, Oct 2025): 发现 importance score collapse 并提出 entropy 补偿，为我们的 discrimination collapse 机制提供独立 supporting evidence——他们在单轴上观察到的 score collapse 正是我们在 compound setting 中发现的 Gini/CV 下降的单轴对应。\\n  - **R-KV** (arxiv 2505.24133, May 2025): 针对 reasoning task 做 KV compression 优化，属于 task-specific method。我们不是提出新方法，而是 mechanistic 分析 compound interaction 的 phase-dependent 行为，二者目标不同（optimization vs understanding）。\\n- **实验支撑**: C3 (crossover), Related Work §2 的 gap 分析\\n\\n### RC6: Novelty vs Lethe/SparK\\n- **预期质疑**: \\\"How does this differ from Lethe (AAAI 2026) which also does layer-time-adaptive KV pruning, or SparK which studies compound compression?\\\"\\n- **应对**: Lethe 和 SparK 都没有分析 phase × strategy 的交互效应。Lethe 是 method paper（提出 adaptive eviction 方法），我们是 empirical finding paper（发现 phase-dependent severity gradient）。SparK 研究 compound compression 但将 interaction 视为均匀超可加，我们发现 interaction severity 随 phase 和 strategy 变化。新近工作进一步确认我们的独特定位：\\n  - **Physics of KV Cache Compression** (arxiv 2603.01426, Mar 2026) 是最近的相关工作，研究单轴压缩的 phase transition 阈值行为。与我们的核心区别：他们的 phase transition 是压缩率维度上的 critical point，我们的 phase-dependent gradient 是 reasoning phase 维度上 compound interaction 的连续调制——两者刻画的 \\\"phase\\\" 语义不同（compression-rate phase vs reasoning phase）。\\n  - **ThinKV** (arxiv 2510.01290, Oct 2025) 和 **R-KV** (arxiv 2505.24133, May 2025) 都在 KV compression 单轴上引入 phase/reasoning awareness，但均未涉及 compound interaction。我们的贡献在于揭示 pruning × eviction 双轴交互如何被 reasoning phase 调制，这是单轴方法无法观察到的涌现现象。\\n  - **HIES** (arxiv 2510.13832, Oct 2025) 的 importance score collapse 发现为我们的 discrimination collapse 机制提供了独立佐证，但 HIES 聚焦于单轴补偿方法，未研究 collapse 在 compound setting 中的放大效应。\\n  - Related Work §2 明确区分三者定位：Lethe/SparK = method/compound method, ThinKV/R-KV = single-axis phase-aware, Physics of KV = single-axis phase transition, HIES = single-axis collapse。我们 = compound × phase × strategy 三维交互分析。\\n- **实验支撑**: 不需要额外实验，仅需 §2 引用区分\\n\\n## Paper Positioning\\n\\n**类型**: Empirical finding paper（非 method paper）\\n**核心贡献**:\\n1. 发现 compound sparsity severity 的 strategy × phase 交互\\n2. 量化 severity gradient（bf16 paired median difference 0.39→8.48, Cohen's d 0.61→1.13）和 crossover 现象\\n3. 提出 discrimination collapse 机制解释（Gini/CV 跨模型一致；entropy redistribution model-dependent）\\n4. Cross-model + cross-architecture (LLaMA) replication 验证泛化性（三模型两架构；LLaMA partially_confirmed，strategy×phase 交互强度 architecture-dependent, D060）\\n\\n**投稿目标**: EMNLP 2026 ARR, deadline 2026-05-25\\n**Rebuttal 准备**: Day 9 (2026-05-23) 预留 rebuttal letter 写作时间\\n**关键时间线**：\\n- Day 9 (2026-05-23): 预留写 rebuttal letter\\n- Day 11 (2026-05-25): EMNLP 2026 ARR 截稿\\n\", \"total_chars\": 12640, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Glob · `toolu_01QvZ2YaBRGaWWq93bmiKYQs`</summary>

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
  "session_id": "e127786f-a191-4d01-b58d-071eb9fc50fc",
  "uuid": "53d4f921-350e-429d-a117-76eee98ba83a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JqxDm9gBcGGnHx6CvdxFWY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 489,
      "cache_read_input_tokens": 24423,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 489
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

_source line 12 · 2026-05-16T22:42:42.017Z_

<details><summary>↩ Tool result · `toolu_01QvZ2YaBRGaWWq93bmiKYQs`</summary>

```text
artifacts/_project/paper/main.tex
artifacts/_project/paper/appendix.tex
artifacts/_project/paper/appendix_robustness.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/analysis.tex
artifacts/_project/paper/discussion.tex
artifacts/_project/paper/methodology.tex
artifacts/_project/paper/background.tex
artifacts/_project/paper/results.tex
artifacts/_project/paper/appendix_moved.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/limitations.tex
artifacts/_project/paper/abstract.tex
artifacts/_project/paper/appendix_disc_analysis.tex
artifacts/_project/paper/conclusion.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e127786f-a191-4d01-b58d-071eb9fc50fc",
  "uuid": "ab8c1e4e-ab23-4b05-aa83-e5d26f88d27f",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/paper/main.tex",
      "artifacts/_project/paper/appendix.tex",
      "artifacts/_project/paper/appendix_robustness.tex",
      "artifacts/_project/paper/related_work.tex",
      "artifacts/_project/paper/analysis.tex",
      "artifacts/_project/paper/discussion.tex",
      "artifacts/_project/paper/methodology.tex",
      "artifacts/_project/paper/background.tex",
      "artifacts/_project/paper/results.tex",
      "artifacts/_project/paper/appendix_moved.tex",
      "artifacts/_project/paper/introduction.tex",
      "artifacts/_project/paper/limitations.tex",
      "artifacts/_project/paper/abstract.tex",
      "artifacts/_project/paper/appendix_disc_analysis.tex",
      "artifacts/_project/paper/conclusion.tex"
    ],
    "durationMs": 18,
    "numFiles": 15,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 13_

Now let me read the tex files that were updated.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e127786f-a191-4d01-b58d-071eb9fc50fc",
  "uuid": "cf6226bd-da9a-4182-8be6-b9ae340b4a11",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JubK9ZyZRrZ8aanNzhm9LW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6477,
      "cache_read_input_tokens": 24912,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6477
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

_source line 14_

<details open><summary>🔧 Tool call — Read · `toolu_01UWwg4vVuA3qQFZhPiF8dkb`</summary>

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
  "session_id": "e127786f-a191-4d01-b58d-071eb9fc50fc",
  "uuid": "2959ec87-461f-4db2-9f43-ee7c1d26dff5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JubK9ZyZRrZ8aanNzhm9LW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6477,
      "cache_read_input_tokens": 24912,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6477
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

_source line 15 · 2026-05-16T22:42:47.359Z_

<details><summary>↩ Tool result · `toolu_01UWwg4vVuA3qQFZhPiF8dkb`</summary>

```text
1	\begin{abstract}
2	Compound sparsity---simultaneously pruning attention heads and evicting KV cache entries---is essential for efficient LLM inference but produces super-additive quality degradation whose structure is poorly understood.
3	We find that compound sparsity severity is not a fixed constant but an emergent property of the interaction among eviction strategy, reasoning phase, and sparsity level.
4	On DeepSeek-R1-Distill-Qwen-7B (MATH-500), importance-based eviction exhibits a monotonically increasing phase--severity gradient: the paired median difference $\Delta$ rises from $0.39$ at sparsity $s{=}0.15$ to $8.48$ at $s{=}0.30$ (Spearman $\rho{=}1.0$; all Bonferroni-corrected $p < 0.005$).
5	Random eviction develops a detectable gradient only above $s \approx 0.20$, at $2.7$--$17{\times}$ smaller magnitude.
6	The pattern replicates on Qwen2.5-7B-Instruct ($\Delta$: $0.07 \to 3.16$; $\rho{=}1.0$), shows consistent phase gradient direction on GSM8K for both models, and generalizes to LlamaForCausalLM ($n{=}250$; importance phase gradient $d_z{=}0.81$--$1.15$, all $p < 10^{-29}$; strategy specificity architecture-dependent).
7	Per-phase Gini analysis identifies \emph{importance discrimination collapse}---the degeneration of head importance scores toward uniformity under compound stress---as a correlational diagnostic of this severity divergence.
8	Prior work characterizes compound degradation as phase-agnostic; we show that phase modulates severity by $15$--$17{\times}$ on DeepSeek and $2.7$--$3.5{\times}$ on Qwen. These findings establish phase-gated analysis---decomposing compound severity by reasoning phase and eviction strategy---as a principled diagnostic framework, with direct implications for phase-aware budget allocation in inference systems.
9	\end{abstract}
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e127786f-a191-4d01-b58d-071eb9fc50fc",
  "uuid": "142b189e-d61b-4030-92cc-b1b55e0768ba",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex",
      "content": "\\begin{abstract}\nCompound sparsity---simultaneously pruning attention heads and evicting KV cache entries---is essential for efficient LLM inference but produces super-additive quality degradation whose structure is poorly understood.\nWe find that compound sparsity severity is not a fixed constant but an emergent property of the interaction among eviction strategy, reasoning phase, and sparsity level.\nOn DeepSeek-R1-Distill-Qwen-7B (MATH-500), importance-based eviction exhibits a monotonically increasing phase--severity gradient: the paired median difference $\\Delta$ rises from $0.39$ at sparsity $s{=}0.15$ to $8.48$ at $s{=}0.30$ (Spearman $\\rho{=}1.0$; all Bonferroni-corrected $p < 0.005$).\nRandom eviction develops a detectable gradient only above $s \\approx 0.20$, at $2.7$--$17{\\times}$ smaller magnitude.\nThe pattern replicates on Qwen2.5-7B-Instruct ($\\Delta$: $0.07 \\to 3.16$; $\\rho{=}1.0$), shows consistent phase gradient direction on GSM8K for both models, and generalizes to LlamaForCausalLM ($n{=}250$; importance phase gradient $d_z{=}0.81$--$1.15$, all $p < 10^{-29}$; strategy specificity architecture-dependent).\nPer-phase Gini analysis identifies \\emph{importance discrimination collapse}---the degeneration of head importance scores toward uniformity under compound stress---as a correlational diagnostic of this severity divergence.\nPrior work characterizes compound degradation as phase-agnostic; we show that phase modulates severity by $15$--$17{\\times}$ on DeepSeek and $2.7$--$3.5{\\times}$ on Qwen. These findings establish phase-gated analysis---decomposing compound severity by reasoning phase and eviction strategy---as a principled diagnostic framework, with direct implications for phase-aware budget allocation in inference systems.\n\\end{abstract}\n",
      "numLines": 10,
      "startLine": 1,
      "totalLines": 10
    }
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Read · `toolu_01F2jsQMAtUwu2TMQy9LdeYQ`</summary>

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
  "session_id": "e127786f-a191-4d01-b58d-071eb9fc50fc",
  "uuid": "4d86a590-f511-4b8c-aebc-ff4d07809c5c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JubK9ZyZRrZ8aanNzhm9LW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6477,
      "cache_read_input_tokens": 24912,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6477
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

_source line 17 · 2026-05-16T22:42:47.793Z_

<details><summary>↩ Tool result · `toolu_01F2jsQMAtUwu2TMQy9LdeYQ`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Long-context language models place acute pressure on the key--value (KV) cache, which grows linearly with sequence length \cite{kwon-sosp2023, pope-mlsys2023}.
5	Two complementary responses---\emph{attention head pruning} \cite{voita-acl2019, michel-neurips2019} and \emph{KV cache eviction} \cite{snapkv-neurips2024, adakv-neurips2025}---are increasingly deployed simultaneously as \emph{compound sparsity}, but the resulting quality degradation is often super-additive \cite{spark-aaai2026, slim-icml2025}. Recent evaluations show that reasoning capabilities degrade disproportionately under compound compression \cite{unicomp-2026}, and that per-dimension safe zones intersect to form a smaller joint safe region \cite{phase-transition-compression-2026}.
6	
7	Prior work treats compound interaction magnitude as roughly constant across generation \cite{spark-aaai2026, unicomp-2026}, despite evidence that pruning sensitivity depends on representational phase \cite{decision-repr-transition-2026} and that no single sparse attention strategy dominates across generation stages \cite{sparse-frontier-2025}.
8	This assumption is problematic for reasoning models, whose chain-of-thought generations \cite{wei-neurips2022-cot} alternate between broadly distributed attention (exploratory reasoning) and sharply concentrated attention (structured computation) \cite{thinkv-iclr2026}.
9	Phase-aware methods like ThinKV \cite{thinkv-iclr2026} apply different KV strategies per phase but without considering compound interaction, while importance-based eviction itself faces challenges from score collapse \cite{hies-2025}, greedy bias \cite{greedy-bias-kvcache-2026}, and temporal dynamics \cite{lethe-aaai2026}. These methods each optimize a single pruning axis; we characterize the interaction when multiple axes are composed.
10	If compound severity varies across these phases, a uniform sparsity budget may be safe in one phase yet destructive in another.
11	
12	We find that compound sparsity severity is an emergent property of the three-way interaction among eviction strategy, reasoning phase, and sparsity level.
13	Under importance-based KV cache eviction, the Interaction Index---a measure of super-additive degradation---concentrates in low-sparsity reasoning phases and is largely absent in high-sparsity phases.
14	On DeepSeek-R1-Distill-Qwen-7B (MATH-500), the paired median difference rises from $0.39$ at $s{=}0.15$ to $8.48$ at $s{=}0.30$ (Spearman $\rho{=}1.0$; all Bonferroni-corrected $p < 0.005$).
15	The pattern replicates on Qwen2.5-7B-Instruct ($\Delta$: $0.07 \to 3.16$; all $p < 0.005$), with cross-architecture support from DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, $n{=}250$), where the importance phase gradient replicates with large effect sizes ($d_z{=}0.81$--$1.15$; all $p < 10^{-29}$) despite reduced strategy specificity ($2.0$--$2.6{\times}$ vs.\ $15$--$17{\times}$ on Qwen2-family models).
16	Random eviction develops a detectable phase gradient only above $s \approx 0.20$, at $2.7$--$17{\times}$ smaller magnitude than importance-based (where both strategies reach significance at $s \geq 0.25$), supporting that the dominant gradient is strategy-specific.
17	Cross-benchmark validation on GSM8K reveals consistent phase gradient direction: DeepSeek replicates the monotonic dose-response ($\Delta$: $0.24 \to 4.68$; all $p \leq 0.0003$), while Qwen shows directional consistency at $s \geq 0.25$ but is inconclusive due to generation truncation (\S\ref{sec:cross-benchmark}). Strategy specificity attenuates on GSM8K relative to MATH-500, indicating that phase modulation generalizes but its magnitude is task-dependent.
18	
19	Per-phase Gini analysis identifies \emph{importance discrimination collapse}---the degeneration of head importance scores toward uniformity under compound stress---as a correlational diagnostic of this phase--strategy divergence. Both strategies exhibit consistent Gini drops across all tested conditions, yet severity diverges by $2.7$--$17{\times}$, implicating the structural specificity of importance-based pruning as the key differentiator.
20	
21	Beyond individual findings, we contribute a \emph{phase-gated analysis framework} that decomposes compound severity by reasoning phase and eviction strategy, transforming a scalar interaction metric into a structured diagnostic. This framework---combining the Interaction Index with attention-sparsity-based phase segmentation---reveals structure in compound degradation that aggregate metrics miss, and provides practitioners with a principled basis for phase-aware sparsity allocation.
22	
23	Our contributions:
24	\begin{enumerate}[nosep,leftmargin=*]
25	    \item We characterize a \textbf{phase-modulated compound severity gradient}: importance-based eviction exhibits a monotonic dose-response ($\rho{=}1.0$; $\Delta$: $0.39 \to 8.48$) with a phase gradient $2.7$--$17{\times}$ larger than random eviction where both strategies are significant ($s \geq 0.25$) on MATH-500; the gradient direction is consistent on GSM8K, while strategy specificity attenuates (\S\ref{sec:cross-benchmark}).
26	    \item We replicate the pattern \textbf{across training paradigms and architectures}: within-architecture replication on Qwen2.5-7B-Instruct (same Qwen2 backbone, instruction-tuned; $\Delta$: $0.07 \to 3.16$; $\rho{=}1.0$) and cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM; $n{=}250$; importance phase gradient $d_z{=}0.81$--$1.15$, all $p < 10^{-29}$; strategy specificity reduced to $2.0$--$2.6{\times}$, architecture-dependent; \S\ref{sec:cross-arch}).
27	    \item We identify \textbf{importance discrimination collapse} via per-phase Gini analysis as a correlational diagnostic: consistent collapse across models and strategies, with the structural specificity of importance-based pruning corresponding to the severity divergence (\S\ref{sec:analysis}).
28	    \item We validate the phase gradient on \textbf{GSM8K} for both models, finding that phase modulation is benchmark-robust while strategy specificity is task-dependent (\S\ref{sec:cross-benchmark}).
29	\end{enumerate}
30	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e127786f-a191-4d01-b58d-071eb9fc50fc",
  "uuid": "b54fa4ac-e741-4660-a71b-3445c0cfacea",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nLong-context language models place acute pressure on the key--value (KV) cache, which grows linearly with sequence length \\cite{kwon-sosp2023, pope-mlsys2023}.\nTwo complementary responses---\\emph{attention head pruning} \\cite{voita-acl2019, michel-neurips2019} and \\emph{KV cache eviction} \\cite{snapkv-neurips2024, adakv-neurips2025}---are increasingly deployed simultaneously as \\emph{compound sparsity}, but the resulting quality degradation is often super-additive \\cite{spark-aaai2026, slim-icml2025}. Recent evaluations show that reasoning capabilities degrade disproportionately under compound compression \\cite{unicomp-2026}, and that per-dimension safe zones intersect to form a smaller joint safe region \\cite{phase-transition-compression-2026}.\n\nPrior work treats compound interaction magnitude as roughly constant across generation \\cite{spark-aaai2026, unicomp-2026}, despite evidence that pruning sensitivity depends on representational phase \\cite{decision-repr-transition-2026} and that no single sparse attention strategy dominates across generation stages \\cite{sparse-frontier-2025}.\nThis assumption is problematic for reasoning models, whose chain-of-thought generations \\cite{wei-neurips2022-cot} alternate between broadly distributed attention (exploratory reasoning) and sharply concentrated attention (structured computation) \\cite{thinkv-iclr2026}.\nPhase-aware methods like ThinKV \\cite{thinkv-iclr2026} apply different KV strategies per phase but without considering compound interaction, while importance-based eviction itself faces challenges from score collapse \\cite{hies-2025}, greedy bias \\cite{greedy-bias-kvcache-2026}, and temporal dynamics \\cite{lethe-aaai2026}. These methods each optimize a single pruning axis; we characterize the interaction when multiple axes are composed.\nIf compound severity varies across these phases, a uniform sparsity budget may be safe in one phase yet destructive in another.\n\nWe find that compound sparsity severity is an emergent property of the three-way interaction among eviction strategy, reasoning phase, and sparsity level.\nUnder importance-based KV cache eviction, the Interaction Index---a measure of super-additive degradation---concentrates in low-sparsity reasoning phases and is largely absent in high-sparsity phases.\nOn DeepSeek-R1-Distill-Qwen-7B (MATH-500), the paired median difference rises from $0.39$ at $s{=}0.15$ to $8.48$ at $s{=}0.30$ (Spearman $\\rho{=}1.0$; all Bonferroni-corrected $p < 0.005$).\nThe pattern replicates on Qwen2.5-7B-Instruct ($\\Delta$: $0.07 \\to 3.16$; all $p < 0.005$), with cross-architecture support from DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, $n{=}250$), where the importance phase gradient replicates with large effect sizes ($d_z{=}0.81$--$1.15$; all $p < 10^{-29}$) despite reduced strategy specificity ($2.0$--$2.6{\\times}$ vs.\\ $15$--$17{\\times}$ on Qwen2-family models).\nRandom eviction develops a detectable phase gradient only above $s \\approx 0.20$, at $2.7$--$17{\\times}$ smaller magnitude than importance-based (where both strategies reach significance at $s \\geq 0.25$), supporting that the dominant gradient is strategy-specific.\nCross-benchmark validation on GSM8K reveals consistent phase gradient direction: DeepSeek replicates the monotonic dose-response ($\\Delta$: $0.24 \\to 4.68$; all $p \\leq 0.0003$), while Qwen shows directional consistency at $s \\geq 0.25$ but is inconclusive due to generation truncation (\\S\\ref{sec:cross-benchmark}). Strategy specificity attenuates on GSM8K relative to MATH-500, indicating that phase modulation generalizes but its magnitude is task-dependent.\n\nPer-phase Gini analysis identifies \\emph{importance discrimination collapse}---the degeneration of head importance scores toward uniformity under compound stress---as a correlational diagnostic of this phase--strategy divergence. Both strategies exhibit consistent Gini drops across all tested conditions, yet severity diverges by $2.7$--$17{\\times}$, implicating the structural specificity of importance-based pruning as the key differentiator.\n\nBeyond individual findings, we contribute a \\emph{phase-gated analysis framework} that decomposes compound severity by reasoning phase and eviction strategy, transforming a scalar interaction metric into a structured diagnostic. This framework---combining the Interaction Index with attention-sparsity-based phase segmentation---reveals structure in compound degradation that aggregate metrics miss, and provides practitioners with a principled basis for phase-aware sparsity allocation.\n\nOur contributions:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item We characterize a \\textbf{phase-modulated compound severity gradient}: importance-based eviction exhibits a monotonic dose-response ($\\rho{=}1.0$; $\\Delta$: $0.39 \\to 8.48$) with a phase gradient $2.7$--$17{\\times}$ larger than random eviction where both strategies are significant ($s \\geq 0.25$) on MATH-500; the gradient direction is consistent on GSM8K, while strategy specificity attenuates (\\S\\ref{sec:cross-benchmark}).\n    \\item We replicate the pattern \\textbf{across training paradigms and architectures}: within-architecture replication on Qwen2.5-7B-Instruct (same Qwen2 backbone, instruction-tuned; $\\Delta$: $0.07 \\to 3.16$; $\\rho{=}1.0$) and cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM; $n{=}250$; importance phase gradient $d_z{=}0.81$--$1.15$, all $p < 10^{-29}$; strategy specificity reduced to $2.0$--$2.6{\\times}$, architecture-dependent; \\S\\ref{sec:cross-arch}).\n    \\item We identify \\textbf{importance discrimination collapse} via per-phase Gini analysis as a correlational diagnostic: consistent collapse across models and strategies, with the structural specificity of importance-based pruning corresponding to the severity divergence (\\S\\ref{sec:analysis}).\n    \\item We validate the phase gradient on \\textbf{GSM8K} for both models, finding that phase modulation is benchmark-robust while strategy specificity is task-dependent (\\S\\ref{sec:cross-benchmark}).\n\\end{enumerate}\n",
      "numLines": 30,
      "startLine": 1,
      "totalLines": 30
    }
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Read · `toolu_01HCFhijhf7HpmLuw6XP7iyc`</summary>

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
  "session_id": "e127786f-a191-4d01-b58d-071eb9fc50fc",
  "uuid": "49e3c46f-426c-4191-9062-f4d6479dc35f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JubK9ZyZRrZ8aanNzhm9LW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6477,
      "cache_read_input_tokens": 24912,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6477
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

_source line 19 · 2026-05-16T22:42:48.137Z_

<details><summary>↩ Tool result · `toolu_01HCFhijhf7HpmLuw6XP7iyc`</summary>

```text
1	
2	\section{Results}
3	\label{sec:results}
4	
5	\subsection{Strategy-Dependent Severity}
6	\label{sec:strategy-severity}
7	
8	Table~\ref{tab:aggregate-ii} reports the median compound severity difference across strategies and sparsity levels. Under importance-based eviction, $\Delta$ increases from $0.39$ at $s{=}0.15$ to $8.48$ at $s{=}0.30$---a $22{\times}$ amplification (all Bonferroni-corrected $p \ll 10^{-10}$). Random eviction develops a detectable but weak phase gradient above $s \approx 0.20$: at $s \leq 0.20$, $\Delta$ is non-significant ($0.01$--$0.03$; CIs span zero); at $s \geq 0.25$, $\Delta$ becomes significant ($0.26$--$0.51$; $p_{\text{Bonf}} < 0.006$) but $15$--$17{\times}$ smaller than under importance-based eviction. Both strategies exhibit monotonic dose-response (Jonckheere-Terpstra $z{=}6.2$--$33.7$, all $p < 10^{-9}$), but importance masking effect sizes are an order of magnitude larger.
9	
10	\begin{table}[t]
11	\centering
12	\small
13	\caption{Median of per-problem paired severity differences ($\Delta$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}496$, MATH-500).}
14	\label{tab:aggregate-ii}
15	\begin{tabular}{@{}lcccc@{}}
16	\toprule
17	Strategy & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
18	\midrule
19	Importance & 0.39 & 1.21 & 3.99 & 8.48 \\
20	Random     & 0.01 & 0.03 & 0.26 & 0.51 \\
21	\bottomrule
22	\end{tabular}
23	\end{table}
24	
25	
26	\subsection{Phase-Modulated Amplification}
27	\label{sec:phase-amplification}
28	
29	Decomposing II by reasoning phase reveals that strategy-dependent severity is driven by amplification in the low-sparsity phase. Table~\ref{tab:main-results} reports the per-phase breakdown. Under importance-based eviction, the median II in the low-sparsity phase rises from $0.357$ ($s{=}0.15$) to $8.456$ ($s{=}0.30$), while the high-sparsity phase remains near zero ($0.003$--$0.038$), yielding paired median differences $\Delta$ from $0.39$ to $8.48$ (all $p \ll 10^{-10}$). Random eviction shows a detectable but much weaker phase gradient at $s \geq 0.25$ ($\Delta{=}0.26$--$0.51$; $p_{\text{Bonf}} < 0.006$), $15$--$17{\times}$ smaller than importance-based at matched sparsity. Figure~\ref{fig:hero} visualizes the dose-response relationship for both models. The per-problem amplification ratio $G$ (Eq.~\ref{eq:gradient}) provides an auxiliary illustrative perspective and is reported in Appendix~\ref{app:g-metric}.
30	Under the multiplicative null ($r_b = r_a \cdot r_k$; Appendix~\ref{app:multiplicative-null}), the phase-severity gradient is preserved ($G_{\times}{=}21$--$64{\times}$); we report additive-null values throughout as the more conservative estimates.
31	
32	\begin{table*}[t]
33	\centering
34	\small
35	\caption{Per-phase interaction index (II) at $n{=}496$/$475$. $\Delta{=}\widetilde{\mathrm{II}^{(i)}_{\textit{low}} - \mathrm{II}^{(i)}_{\textit{high}}}$: median of per-problem paired differences (not the difference of column medians) with bootstrap 95\% CI ($B{=}10{,}000$). $G$ values reported in Appendix~\ref{app:g-metric}. Profiling-subset values ($n{=}50$) in Table~\ref{tab:profiling-subset}.}
36	\label{tab:main-results}
37	\begin{tabular}{@{}llcccc@{}}
38	\toprule
39	$s$ & Strategy & $\widetilde{\mathrm{II}}_{\textit{high}}$ & $\widetilde{\mathrm{II}}_{\textit{low}}$ & $\Delta$\; [95\% CI] & $p_{\text{Bonf}}$ \\
40	\midrule
41	\multicolumn{6}{@{}l}{\textit{DeepSeek-R1-Distill-Qwen-7B ($n{=}496$)}} \\
42	0.15 & Importance & 0.003 & 0.357 & 0.39\; $[0.35,\; 0.44]$ & $< 10^{-10}$ \\
43	0.15 & Random     & 0.083 & 0.090 & 0.01\; $[-0.02,\; 0.04]$ & ns \\
44	\addlinespace
45	0.20 & Importance & 0.008 & 1.211 & 1.21\; $[1.11,\; 1.34]$ & $< 10^{-10}$ \\
46	0.20 & Random     & 0.270 & 0.357 & 0.03\; $[-0.01,\; 0.08]$ & ns \\
47	\addlinespace
48	0.25 & Importance & 0.021 & 3.971 & 3.99\; $[3.53,\; 4.36]$ & $< 10^{-10}$ \\
49	0.25 & Random     & 1.113 & 1.514 & 0.26\; $[0.13,\; 0.35]$ & $< 0.006$ \\
50	\addlinespace
51	0.30 & Importance & 0.038 & 8.456 & 8.48\; $[7.75,\; 9.69]$ & $< 10^{-10}$ \\
52	0.30 & Random     & 3.112 & 3.848 & 0.51\; $[0.26,\; 0.89]$ & $< 0.006$ \\
53	\midrule
54	\multicolumn{6}{@{}l}{\textit{Qwen2.5-7B-Instruct ($n{=}475$)}} \\
55	0.15 & Importance & $-$0.000$^{\ddagger}$ & 0.044 & 0.07\; $[0.05,\; 0.09]$ & $< 10^{-14}$ \\
56	0.15 & Random     & 0.094 & 0.097 & $-$0.01\; $[-0.04,\; 0.01]$ & ns \\
57	\addlinespace
58	0.20 & Importance & 0.000 & 0.275 & 0.31\; $[0.26,\; 0.36]$ & $< 10^{-14}$ \\
59	0.20 & Random     & 0.291 & 0.356 & 0.02\; $[-0.01,\; 0.07]$ & ns \\
60	\addlinespace
61	0.25 & Importance & 0.004 & 1.053 & 1.07\; $[0.98,\; 1.18]$ & $< 10^{-14}$ \\
62	0.25 & Random     & 1.108 & 1.769 & 0.39\; $[0.24,\; 0.55]$ & $< 10^{-10}$ \\
63	\addlinespace
64	0.30 & Importance & 0.014 & 3.208 & 3.16\; $[2.78,\; 3.56]$ & $< 10^{-14}$ \\
65	0.30 & Random     & 2.819 & 4.253 & 0.91\; $[0.61,\; 1.26]$ & $< 10^{-13}$ \\
66	\bottomrule
67	\multicolumn{6}{@{}p{0.92\textwidth}}{\footnotesize $^{\ddagger}$ Negative II at this sparsity reflects \texttt{bfloat16} numerical noise when the interaction effect approaches zero ($|\mathrm{II}| < 10^{-4}$). $\Delta{=}0.07$, $p{=}8.7 \times 10^{-15}$ supports $\mathrm{II}_{\textit{low}} > \mathrm{II}_{\textit{high}}$.}
68	\end{tabular}
69	\end{table*}
70	
71	\begin{figure*}[t]
72	\centering
73	\includegraphics[width=\textwidth]{fig1_ii_scatter.pdf}
74	\caption{Paired median difference $\Delta$ (primary metric) as a function of sparsity level $s$ for DeepSeek-R1-Distill-Qwen-7B ($n{=}496$, left) and Qwen2.5-7B-Instruct ($n{=}475$, right). Importance-based eviction (red) exhibits monotonically increasing $\Delta$ ($0.39$--$8.48$ for DeepSeek, $0.07$--$3.16$ for Qwen); random eviction (blue) remains near zero at low sparsity (ns) and shows weak effects at $s \geq 0.25$. Error bars show asymmetric bootstrap 95\% CIs. DeepSeek importance effects are ${\sim}2.7{\times}$ larger than Qwen, consistent with the training-paradigm contrast (\S\ref{sec:cross-model}). Significance: {*}{*}{*}\,$p_{\text{Bonf}} < 0.001$; {*}{*}\,$p_{\text{Bonf}} < 0.01$; ns\,$p_{\text{Bonf}} > 0.05$.}
75	\label{fig:hero}
76	\end{figure*}
77	
78	
79	\subsection{Phase-Strategy Crossover}
80	\label{sec:crossover}
81	
82	The phase-strategy crossover is model-dependent. For DeepSeek ($n{=}496$), a strategy ranking reversal emerges at all four sparsity levels: at $s{=}0.25$, importance-based eviction yields \emph{lower} II than random in the high-sparsity phase ($0.021$ vs.\ $1.113$) but \emph{higher} II in the low-sparsity phase ($3.971$ vs.\ $1.514$---a $2.6{\times}$ reversal; both $p < 10^{-4}$), with reversal magnitude ranging from $2.2{\times}$ to $4.0{\times}$ across $s \in \{0.15, 0.20, 0.25, 0.30\}$. Qwen does \emph{not} exhibit this crossover: importance-based eviction produces lower II than random in both phases (e.g., at $s{=}0.25$: high $0.004$ vs.\ $1.108$; low $1.053$ vs.\ $1.769$). This divergence suggests the crossover arises from model-specific attention head specialization patterns rather than a universal compound-sparsity property. Full crossover analysis appears in Appendix~\ref{app:crossover-details}.
83	
84	\subsection{Replication Across Training Paradigms}
85	\label{sec:cross-model}
86	
87	DeepSeek-R1-Distill-Qwen-7B (distillation-trained) and Qwen2.5-7B-Instruct (instruction-tuned) share the Qwen2 backbone but differ in training objective, providing a within-architecture-family comparison across training paradigms.
88	Qwen2.5-7B-Instruct ($n_{\text{eff}}{=}475$) reproduces the monotonic severity gradient: $\Delta$ increases from $0.07$ at $s{=}0.15$ to $3.16$ at $s{=}0.30$ (all Bonferroni-corrected $p < 10^{-14}$), paralleling DeepSeek at approximately one-quarter to one-sixth the magnitude. Both models yield strictly increasing median $\Delta$ trajectories (Jonckheere-Terpstra $z \geq 6.2$, $p < 10^{-9}$; see \S\ref{par:stats}). Random eviction on Qwen mirrors DeepSeek: non-significant at $s \leq 0.20$, becoming significant at $s \geq 0.25$ ($\Delta{=}0.39$--$0.91$; $p_{\text{Bonf}} < 10^{-10}$) but $2.7$--$20{\times}$ weaker than importance-based. A caveat: 45.2\% of Qwen problems yield null mid-phase segments due to low temporal autocorrelation ($r{=}0.718$ vs.\ $0.894$); this does not affect $\Delta$ (Appendix~\ref{app:qwen-null-rate}). Full tables in Appendix~\ref{app:cross-model-details}.
89	
90	\subsection{Cross-Architecture Validation}
91	\label{sec:cross-arch}
92	
93	Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, $n{=}250$, MATH-500) supports the generality of phase-modulated compound interaction beyond the Qwen2 architecture family. Under importance-based eviction, the paired median difference $\Delta$ rises monotonically from $0.050$ ($s{=}0.15$) to $0.695$ ($s{=}0.30$), with large effect sizes throughout ($d_z{=}0.81$--$1.15$; all $p < 10^{-29}$; Table~\ref{tab:llama-cross-arch}).
94	
95	A key architectural difference emerges in strategy specificity. On LLaMA, random eviction also exhibits significant phase gradients ($\Delta{=}0.025$--$0.271$; $d_z{=}0.41$--$0.46$; all $p < 10^{-12}$), unlike DeepSeek and Qwen where random is non-significant at $s \leq 0.20$. The importance/random $\Delta$ ratio is $2.0$--$2.6{\times}$ on LLaMA, substantially weaker than the $15$--$17{\times}$ observed on DeepSeek. Dose-response monotonicity holds for both strategies (all conditions monotonic). This indicates that the phase gradient itself is architecture-general, while the degree of strategy specificity is architecture-dependent, likely reflecting differences between GQA (LLaMA, 32 heads with 8 KV groups) and MHA (Qwen2, 28 heads) in how head pruning differentially disrupts importance scoring.
96	
97	Absolute interaction magnitudes are approximately $7$--$12{\times}$ smaller than Qwen2-family models at matched sparsity, consistent with architecture-specific attention head specialization patterns. Full per-condition breakdowns appear in Appendix~\ref{app:cross-arch}.
98	
99	\subsection{Scale Analysis: Qwen2.5-14B}
100	\label{sec:scale-14b}
101	
102	To assess whether phase-modulated severity persists at larger model scale within the same architecture family, we evaluate Qwen2.5-14B-Instruct on MATH-500 ($n{=}500$) at $s \in \{0.15, 0.20, 0.25, 0.30\}$.
103	
104	\begin{table}[t]
105	\centering
106	\small
107	\caption{Median of per-problem paired severity differences ($\Delta$) under importance-based eviction on Qwen2.5-14B-Instruct (MATH-500). \textit{Results pending.}}
108	\label{tab:scale-14b}
109	\begin{tabular}{@{}lcccc@{}}
110	\toprule
111	Strategy & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
112	\midrule
113	Importance & --- & --- & --- & --- \\
114	Random     & --- & --- & --- & --- \\
115	\bottomrule
116	\end{tabular}
117	\end{table}
118	
119	%% PLACEHOLDER: Fill Table~\ref{tab:scale-14b} when c12 experiment completes.
120	%% Expected analysis: (1) whether 14B amplifies or attenuates severity relative to 7B,
121	%% (2) whether strategy specificity ratio is scale-invariant,
122	%% (3) comparison of phase segmentation thresholds at larger scale.
123	
124	\subsection{Cross-Benchmark Validation: GSM8K}
125	\label{sec:cross-benchmark}
126	
127	To assess task generalization, we evaluate both models on GSM8K ($n{=}50$) at $s \in \{0.15, 0.20, 0.25, 0.30\}$. On DeepSeek (clean data, no output truncation), importance-based eviction replicates the MATH-500 phase gradient across all four sparsity levels with a strict dose-response: $\Delta{=}0.24$ at $s{=}0.15$ rising to $4.68$ at $s{=}0.30$ (all $p \leq 0.0003$, Wilcoxon). Strategy specificity on GSM8K manifests as a \emph{qualitative} gap: importance-based eviction produces significant phase gradients while random eviction is non-significant across all conditions (CIs spanning zero).
128	
129	We interpret this attenuation as \emph{reasoning depth scaling}: strategy specificity scales with reasoning chain depth. MATH-500 (complex multi-step reasoning, strategy ratio $15$--$17{\times}$) produces stronger phase contrast than GSM8K (simpler arithmetic, ratio ${\sim}3{\times}$). Within MATH-500, longer traces exhibit higher strategy specificity (Spearman $\rho > 0$, $p < 0.02$), providing continuous correlational support. This scaling relationship is predictive: tasks with deeper reasoning chains should exhibit stronger strategy${\times}$phase interactions, because longer low-sparsity phases provide more opportunity for importance discrimination collapse to accumulate. Qwen GSM8K results are inconclusive due to generation truncation (\texttt{max\_new\_tokens}${=}$2047): while directional consistency holds at $s \geq 0.25$ ($\Delta{=}1.14$--$4.62$; $p < 10^{-4}$), absolute values and phase assignments are unreliable because all outputs hit the token limit. Full tables in Appendix~\ref{app:gsm8k}.
130	
131	\paragraph{GSM8K accuracy under compound sparsity.}
132	A power analysis on GSM8K ($n{=}50$) reveals a strategy-dependent asymmetry in downstream accuracy. Under random head removal, all 8 conditions (2 models $\times$ 4 sparsity levels) are non-significant (max $|d|{=}0.164$). Post-hoc power analysis indicates $n{=}50$ can detect effects of $d \geq 0.40$ ($\alpha{=}0.05$, power${=}0.80$); all random conditions showed $|d| \leq 0.164$, meaning the null results may reflect insufficient power rather than true absence of effect. Under importance-based pruning, Qwen exhibits a medium-sized accuracy degradation at $s \geq 0.25$ ($d \approx 0.63$, power ${>}\,0.99$), consistent with the PPL-based severity gradient observed on MATH-500. DeepSeek importance conditions exhibit a qualitative downward trend in accuracy but are excluded from parametric inference due to heavy-tailed distributions that violate test assumptions.
133	
134	\subsection{Cross-Benchmark Validation: GPQA Diamond}
135	\label{sec:cross-benchmark-gpqa}
136	
137	To assess generalization beyond mathematical reasoning, we evaluate both models on GPQA Diamond~\cite{rein-gpqa-2024} ($n{=}198$), a graduate-level science QA benchmark requiring multi-step reasoning across physics, chemistry, and biology.
138	
139	\begin{table}[t]
140	\centering
141	\small
142	\caption{Median of per-problem paired severity differences ($\Delta$) under importance-based eviction on GPQA Diamond. \textit{Results pending.}}
143	\label{tab:gpqa-results}
144	\begin{tabular}{@{}lcccc@{}}
145	\toprule
146	Model & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
147	\midrule
148	DeepSeek-R1-Distill-Qwen-7B & --- & --- & --- & --- \\
149	Qwen2.5-7B-Instruct         & --- & --- & --- & --- \\
150	\bottomrule
151	\end{tabular}
152	\end{table}
153	
154	%% PLACEHOLDER: Fill Table~\ref{tab:gpqa-results} when c11 experiment completes.
155	%% Expected analysis: (1) phase gradient direction consistency with MATH-500/GSM8K,
156	%% (2) strategy specificity comparison across task types (math vs. science reasoning),
157	%% (3) whether cognitive load modulation hypothesis extends to non-mathematical domains.
158	
159	\subsection{Statistical Validation}
160	\label{sec:stat-validation}
161	
162	Table~\ref{tab:cohens-d} reports the paired median difference $\Delta$ under importance-based eviction for both models at $n{=}496$/$475$. All eight conditions yield CIs excluding zero; within-importance dose-response $d_z$ (s015 vs.\ s030) is $0.94$ (DeepSeek) and $0.92$ (Qwen), both large effects. Importance-based eviction produces significantly larger phase gradients than random at all four sparsity levels ($p_{\text{Bonf}} \ll 10^{-10}$, Wilcoxon; permutation tests in Appendix~\ref{app:permutation-details}).
163	
164	\begin{table}[t]
165	\centering
166	\small
167	\caption{Median of paired differences ($\Delta_i = \mathrm{II}^{(i)}_{\textit{low}} - \mathrm{II}^{(i)}_{\textit{high}}$) under importance-based eviction with bootstrap 95\% CIs ($B{=}10{,}000$).}
168	\label{tab:cohens-d}
169	\begin{tabular}{@{}lcc@{}}
170	\toprule
171	$s$ & DS ($n{=}496$): $\widetilde{\Delta}$\; [95\% CI] & QW ($n{=}475$): $\widetilde{\Delta}$\; [95\% CI] \\
172	\midrule
173	0.15 & $0.39$\; $[0.35,\; 0.44]$ & $0.07$\; $[0.05,\; 0.09]$ \\
174	0.20 & $1.21$\; $[1.11,\; 1.34]$ & $0.31$\; $[0.26,\; 0.36]$ \\
175	0.25 & $3.99$\; $[3.53,\; 4.36]$ & $1.07$\; $[0.98,\; 1.18]$ \\
176	0.30 & $8.48$\; $[7.75,\; 9.69]$ & $3.16$\; $[2.78,\; 3.56]$ \\
177	\bottomrule
178	\multicolumn{3}{@{}l}{\footnotesize All $p_{\text{Bonf}} < 10^{-13}$. Within-importance $d_z$ (s015 vs.\ s030): DS $0.94$, QW $0.92$.}
179	\end{tabular}
180	\end{table}
181	
182	\subsection{Answer-Region Analysis}
183	\label{sec:answer-region}
184	
185	Across both models, 93.2\% of answer tokens (\verb|\boxed{}| markers) fall within the high-sparsity phase, where compound interaction is minimal. This non-uniformity identifies \emph{where} severity concentrates: reasoning-trace tokens show $5.7$--$43.5{\times}$ PPL degradation vs.\ $1.3$--$5.3{\times}$ for answer tokens (Wilcoxon $p < 0.001$). However, reasoning-trace degradation may produce \emph{silent reasoning errors}---correct formatting with corrupted intermediate logic \cite{lanham-2023-faithfulness, turpin-2023-biased-cot}---a failure mode that PPL detects but answer-level accuracy may miss.
186	
187	\subsection{Downstream Accuracy Validation}
188	\label{sec:accuracy-validation}
189	
190	To validate that the PPL-based severity gradient translates to downstream task performance, we evaluate MATH-500 accuracy under compound sparsity (importance-based eviction, \texttt{max\_new\_tokens}${=}$8192; Table~\ref{tab:accuracy}). Qwen's minimal truncation ($\leq 4\%$) provides a clean PPL-accuracy bridge.
191	Qwen ($n{=}100$; truncation $\leq 4\%$) shows gradual decline from $46\%$ (dense) through $s{=}0.25$ ($\delta{=}-4$ to $-13$\,pp) with a sharp cliff at $s{=}0.30$ ($19\%$, $\delta{=}-27$\,pp). DeepSeek ($n{=}50$) degrades more steeply ($74\% \to 4\%$) with a dual-regime structure: at $s \leq 0.20$, degradation is primarily truncation-driven (non-truncated accuracy remains $68$--$71\%$ at $s{=}0.15$--$0.20$ vs.\ $88\%$ dense); at $s \geq 0.25$, both truncation and reasoning quality collapse simultaneously (Appendix~\ref{app:accuracy-details}).
192	The two models exhibit distinct failure modes reflecting training-paradigm dependence: DeepSeek failures are \emph{truncation-dominated} (truncation $16\% \to 76\%$), while Qwen failures are \emph{wrong-answer-dominated} (truncation $\leq 4\%$, reasoning quality degrades directly). Given minimal truncation, Qwen accuracy data provide a reliable PPL-accuracy bridge; DeepSeek accuracy results, confounded by truncation rates of $16\%$--$76\%$, should be interpreted as qualitative observations only.
193	
194	We provide a correlational mechanistic analysis in terms of importance discrimination collapse in \S\ref{sec:analysis}.
195	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e127786f-a191-4d01-b58d-071eb9fc50fc",
  "uuid": "5d0171bc-cdd9-423d-9cd2-b25796d4f46c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex",
      "content": "\n\\section{Results}\n\\label{sec:results}\n\n\\subsection{Strategy-Dependent Severity}\n\\label{sec:strategy-severity}\n\nTable~\\ref{tab:aggregate-ii} reports the median compound severity difference across strategies and sparsity levels. Under importance-based eviction, $\\Delta$ increases from $0.39$ at $s{=}0.15$ to $8.48$ at $s{=}0.30$---a $22{\\times}$ amplification (all Bonferroni-corrected $p \\ll 10^{-10}$). Random eviction develops a detectable but weak phase gradient above $s \\approx 0.20$: at $s \\leq 0.20$, $\\Delta$ is non-significant ($0.01$--$0.03$; CIs span zero); at $s \\geq 0.25$, $\\Delta$ becomes significant ($0.26$--$0.51$; $p_{\\text{Bonf}} < 0.006$) but $15$--$17{\\times}$ smaller than under importance-based eviction. Both strategies exhibit monotonic dose-response (Jonckheere-Terpstra $z{=}6.2$--$33.7$, all $p < 10^{-9}$), but importance masking effect sizes are an order of magnitude larger.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Median of per-problem paired severity differences ($\\Delta$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}496$, MATH-500).}\n\\label{tab:aggregate-ii}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nStrategy & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\\\\n\\midrule\nImportance & 0.39 & 1.21 & 3.99 & 8.48 \\\\\nRandom     & 0.01 & 0.03 & 0.26 & 0.51 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Phase-Modulated Amplification}\n\\label{sec:phase-amplification}\n\nDecomposing II by reasoning phase reveals that strategy-dependent severity is driven by amplification in the low-sparsity phase. Table~\\ref{tab:main-results} reports the per-phase breakdown. Under importance-based eviction, the median II in the low-sparsity phase rises from $0.357$ ($s{=}0.15$) to $8.456$ ($s{=}0.30$), while the high-sparsity phase remains near zero ($0.003$--$0.038$), yielding paired median differences $\\Delta$ from $0.39$ to $8.48$ (all $p \\ll 10^{-10}$). Random eviction shows a detectable but much weaker phase gradient at $s \\geq 0.25$ ($\\Delta{=}0.26$--$0.51$; $p_{\\text{Bonf}} < 0.006$), $15$--$17{\\times}$ smaller than importance-based at matched sparsity. Figure~\\ref{fig:hero} visualizes the dose-response relationship for both models. The per-problem amplification ratio $G$ (Eq.~\\ref{eq:gradient}) provides an auxiliary illustrative perspective and is reported in Appendix~\\ref{app:g-metric}.\nUnder the multiplicative null ($r_b = r_a \\cdot r_k$; Appendix~\\ref{app:multiplicative-null}), the phase-severity gradient is preserved ($G_{\\times}{=}21$--$64{\\times}$); we report additive-null values throughout as the more conservative estimates.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Per-phase interaction index (II) at $n{=}496$/$475$. $\\Delta{=}\\widetilde{\\mathrm{II}^{(i)}_{\\textit{low}} - \\mathrm{II}^{(i)}_{\\textit{high}}}$: median of per-problem paired differences (not the difference of column medians) with bootstrap 95\\% CI ($B{=}10{,}000$). $G$ values reported in Appendix~\\ref{app:g-metric}. Profiling-subset values ($n{=}50$) in Table~\\ref{tab:profiling-subset}.}\n\\label{tab:main-results}\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\n$s$ & Strategy & $\\widetilde{\\mathrm{II}}_{\\textit{high}}$ & $\\widetilde{\\mathrm{II}}_{\\textit{low}}$ & $\\Delta$\\; [95\\% CI] & $p_{\\text{Bonf}}$ \\\\\n\\midrule\n\\multicolumn{6}{@{}l}{\\textit{DeepSeek-R1-Distill-Qwen-7B ($n{=}496$)}} \\\\\n0.15 & Importance & 0.003 & 0.357 & 0.39\\; $[0.35,\\; 0.44]$ & $< 10^{-10}$ \\\\\n0.15 & Random     & 0.083 & 0.090 & 0.01\\; $[-0.02,\\; 0.04]$ & ns \\\\\n\\addlinespace\n0.20 & Importance & 0.008 & 1.211 & 1.21\\; $[1.11,\\; 1.34]$ & $< 10^{-10}$ \\\\\n0.20 & Random     & 0.270 & 0.357 & 0.03\\; $[-0.01,\\; 0.08]$ & ns \\\\\n\\addlinespace\n0.25 & Importance & 0.021 & 3.971 & 3.99\\; $[3.53,\\; 4.36]$ & $< 10^{-10}$ \\\\\n0.25 & Random     & 1.113 & 1.514 & 0.26\\; $[0.13,\\; 0.35]$ & $< 0.006$ \\\\\n\\addlinespace\n0.30 & Importance & 0.038 & 8.456 & 8.48\\; $[7.75,\\; 9.69]$ & $< 10^{-10}$ \\\\\n0.30 & Random     & 3.112 & 3.848 & 0.51\\; $[0.26,\\; 0.89]$ & $< 0.006$ \\\\\n\\midrule\n\\multicolumn{6}{@{}l}{\\textit{Qwen2.5-7B-Instruct ($n{=}475$)}} \\\\\n0.15 & Importance & $-$0.000$^{\\ddagger}$ & 0.044 & 0.07\\; $[0.05,\\; 0.09]$ & $< 10^{-14}$ \\\\\n0.15 & Random     & 0.094 & 0.097 & $-$0.01\\; $[-0.04,\\; 0.01]$ & ns \\\\\n\\addlinespace\n0.20 & Importance & 0.000 & 0.275 & 0.31\\; $[0.26,\\; 0.36]$ & $< 10^{-14}$ \\\\\n0.20 & Random     & 0.291 & 0.356 & 0.02\\; $[-0.01,\\; 0.07]$ & ns \\\\\n\\addlinespace\n0.25 & Importance & 0.004 & 1.053 & 1.07\\; $[0.98,\\; 1.18]$ & $< 10^{-14}$ \\\\\n0.25 & Random     & 1.108 & 1.769 & 0.39\\; $[0.24,\\; 0.55]$ & $< 10^{-10}$ \\\\\n\\addlinespace\n0.30 & Importance & 0.014 & 3.208 & 3.16\\; $[2.78,\\; 3.56]$ & $< 10^{-14}$ \\\\\n0.30 & Random     & 2.819 & 4.253 & 0.91\\; $[0.61,\\; 1.26]$ & $< 10^{-13}$ \\\\\n\\bottomrule\n\\multicolumn{6}{@{}p{0.92\\textwidth}}{\\footnotesize $^{\\ddagger}$ Negative II at this sparsity reflects \\texttt{bfloat16} numerical noise when the interaction effect approaches zero ($|\\mathrm{II}| < 10^{-4}$). $\\Delta{=}0.07$, $p{=}8.7 \\times 10^{-15}$ supports $\\mathrm{II}_{\\textit{low}} > \\mathrm{II}_{\\textit{high}}$.}\n\\end{tabular}\n\\end{table*}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig1_ii_scatter.pdf}\n\\caption{Paired median difference $\\Delta$ (primary metric) as a function of sparsity level $s$ for DeepSeek-R1-Distill-Qwen-7B ($n{=}496$, left) and Qwen2.5-7B-Instruct ($n{=}475$, right). Importance-based eviction (red) exhibits monotonically increasing $\\Delta$ ($0.39$--$8.48$ for DeepSeek, $0.07$--$3.16$ for Qwen); random eviction (blue) remains near zero at low sparsity (ns) and shows weak effects at $s \\geq 0.25$. Error bars show asymmetric bootstrap 95\\% CIs. DeepSeek importance effects are ${\\sim}2.7{\\times}$ larger than Qwen, consistent with the training-paradigm contrast (\\S\\ref{sec:cross-model}). Significance: {*}{*}{*}\\,$p_{\\text{Bonf}} < 0.001$; {*}{*}\\,$p_{\\text{Bonf}} < 0.01$; ns\\,$p_{\\text{Bonf}} > 0.05$.}\n\\label{fig:hero}\n\\end{figure*}\n\n\n\\subsection{Phase-Strategy Crossover}\n\\label{sec:crossover}\n\nThe phase-strategy crossover is model-dependent. For DeepSeek ($n{=}496$), a strategy ranking reversal emerges at all four sparsity levels: at $s{=}0.25$, importance-based eviction yields \\emph{lower} II than random in the high-sparsity phase ($0.021$ vs.\\ $1.113$) but \\emph{higher} II in the low-sparsity phase ($3.971$ vs.\\ $1.514$---a $2.6{\\times}$ reversal; both $p < 10^{-4}$), with reversal magnitude ranging from $2.2{\\times}$ to $4.0{\\times}$ across $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$. Qwen does \\emph{not} exhibit this crossover: importance-based eviction produces lower II than random in both phases (e.g., at $s{=}0.25$: high $0.004$ vs.\\ $1.108$; low $1.053$ vs.\\ $1.769$). This divergence suggests the crossover arises from model-specific attention head specialization patterns rather than a universal compound-sparsity property. Full crossover analysis appears in Appendix~\\ref{app:crossover-details}.\n\n\\subsection{Replication Across Training Paradigms}\n\\label{sec:cross-model}\n\nDeepSeek-R1-Distill-Qwen-7B (distillation-trained) and Qwen2.5-7B-Instruct (instruction-tuned) share the Qwen2 backbone but differ in training objective, providing a within-architecture-family comparison across training paradigms.\nQwen2.5-7B-Instruct ($n_{\\text{eff}}{=}475$) reproduces the monotonic severity gradient: $\\Delta$ increases from $0.07$ at $s{=}0.15$ to $3.16$ at $s{=}0.30$ (all Bonferroni-corrected $p < 10^{-14}$), paralleling DeepSeek at approximately one-quarter to one-sixth the magnitude. Both models yield strictly increasing median $\\Delta$ trajectories (Jonckheere-Terpstra $z \\geq 6.2$, $p < 10^{-9}$; see \\S\\ref{par:stats}). Random eviction on Qwen mirrors DeepSeek: non-significant at $s \\leq 0.20$, becoming significant at $s \\geq 0.25$ ($\\Delta{=}0.39$--$0.91$; $p_{\\text{Bonf}} < 10^{-10}$) but $2.7$--$20{\\times}$ weaker than importance-based. A caveat: 45.2\\% of Qwen problems yield null mid-phase segments due to low temporal autocorrelation ($r{=}0.718$ vs.\\ $0.894$); this does not affect $\\Delta$ (Appendix~\\ref{app:qwen-null-rate}). Full tables in Appendix~\\ref{app:cross-model-details}.\n\n\\subsection{Cross-Architecture Validation}\n\\label{sec:cross-arch}\n\nCross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, $n{=}250$, MATH-500) supports the generality of phase-modulated compound interaction beyond the Qwen2 architecture family. Under importance-based eviction, the paired median difference $\\Delta$ rises monotonically from $0.050$ ($s{=}0.15$) to $0.695$ ($s{=}0.30$), with large effect sizes throughout ($d_z{=}0.81$--$1.15$; all $p < 10^{-29}$; Table~\\ref{tab:llama-cross-arch}).\n\nA key architectural difference emerges in strategy specificity. On LLaMA, random eviction also exhibits significant phase gradients ($\\Delta{=}0.025$--$0.271$; $d_z{=}0.41$--$0.46$; all $p < 10^{-12}$), unlike DeepSeek and Qwen where random is non-significant at $s \\leq 0.20$. The importance/random $\\Delta$ ratio is $2.0$--$2.6{\\times}$ on LLaMA, substantially weaker than the $15$--$17{\\times}$ observed on DeepSeek. Dose-response monotonicity holds for both strategies (all conditions monotonic). This indicates that the phase gradient itself is architecture-general, while the degree of strategy specificity is architecture-dependent, likely reflecting differences between GQA (LLaMA, 32 heads with 8 KV groups) and MHA (Qwen2, 28 heads) in how head pruning differentially disrupts importance scoring.\n\nAbsolute interaction magnitudes are approximately $7$--$12{\\times}$ smaller than Qwen2-family models at matched sparsity, consistent with architecture-specific attention head specialization patterns. Full per-condition breakdowns appear in Appendix~\\ref{app:cross-arch}.\n\n\\subsection{Scale Analysis: Qwen2.5-14B}\n\\label{sec:scale-14b}\n\nTo assess whether phase-modulated severity persists at larger model scale within the same architecture family, we evaluate Qwen2.5-14B-Instruct on MATH-500 ($n{=}500$) at $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Median of per-problem paired severity differences ($\\Delta$) under importance-based eviction on Qwen2.5-14B-Instruct (MATH-500). \\textit{Results pending.}}\n\\label{tab:scale-14b}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nStrategy & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\\\\n\\midrule\nImportance & --- & --- & --- & --- \\\\\nRandom     & --- & --- & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%% PLACEHOLDER: Fill Table~\\ref{tab:scale-14b} when c12 experiment completes.\n%% Expected analysis: (1) whether 14B amplifies or attenuates severity relative to 7B,\n%% (2) whether strategy specificity ratio is scale-invariant,\n%% (3) comparison of phase segmentation thresholds at larger scale.\n\n\\subsection{Cross-Benchmark Validation: GSM8K}\n\\label{sec:cross-benchmark}\n\nTo assess task generalization, we evaluate both models on GSM8K ($n{=}50$) at $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$. On DeepSeek (clean data, no output truncation), importance-based eviction replicates the MATH-500 phase gradient across all four sparsity levels with a strict dose-response: $\\Delta{=}0.24$ at $s{=}0.15$ rising to $4.68$ at $s{=}0.30$ (all $p \\leq 0.0003$, Wilcoxon). Strategy specificity on GSM8K manifests as a \\emph{qualitative} gap: importance-based eviction produces significant phase gradients while random eviction is non-significant across all conditions (CIs spanning zero).\n\nWe interpret this attenuation as \\emph{reasoning depth scaling}: strategy specificity scales with reasoning chain depth. MATH-500 (complex multi-step reasoning, strategy ratio $15$--$17{\\times}$) produces stronger phase contrast than GSM8K (simpler arithmetic, ratio ${\\sim}3{\\times}$). Within MATH-500, longer traces exhibit higher strategy specificity (Spearman $\\rho > 0$, $p < 0.02$), providing continuous correlational support. This scaling relationship is predictive: tasks with deeper reasoning chains should exhibit stronger strategy${\\times}$phase interactions, because longer low-sparsity phases provide more opportunity for importance discrimination collapse to accumulate. Qwen GSM8K results are inconclusive due to generation truncation (\\texttt{max\\_new\\_tokens}${=}$2047): while directional consistency holds at $s \\geq 0.25$ ($\\Delta{=}1.14$--$4.62$; $p < 10^{-4}$), absolute values and phase assignments are unreliable because all outputs hit the token limit. Full tables in Appendix~\\ref{app:gsm8k}.\n\n\\paragraph{GSM8K accuracy under compound sparsity.}\nA power analysis on GSM8K ($n{=}50$) reveals a strategy-dependent asymmetry in downstream accuracy. Under random head removal, all 8 conditions (2 models $\\times$ 4 sparsity levels) are non-significant (max $|d|{=}0.164$). Post-hoc power analysis indicates $n{=}50$ can detect effects of $d \\geq 0.40$ ($\\alpha{=}0.05$, power${=}0.80$); all random conditions showed $|d| \\leq 0.164$, meaning the null results may reflect insufficient power rather than true absence of effect. Under importance-based pruning, Qwen exhibits a medium-sized accuracy degradation at $s \\geq 0.25$ ($d \\approx 0.63$, power ${>}\\,0.99$), consistent with the PPL-based severity gradient observed on MATH-500. DeepSeek importance conditions exhibit a qualitative downward trend in accuracy but are excluded from parametric inference due to heavy-tailed distributions that violate test assumptions.\n\n\\subsection{Cross-Benchmark Validation: GPQA Diamond}\n\\label{sec:cross-benchmark-gpqa}\n\nTo assess generalization beyond mathematical reasoning, we evaluate both models on GPQA Diamond~\\cite{rein-gpqa-2024} ($n{=}198$), a graduate-level science QA benchmark requiring multi-step reasoning across physics, chemistry, and biology.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Median of per-problem paired severity differences ($\\Delta$) under importance-based eviction on GPQA Diamond. \\textit{Results pending.}}\n\\label{tab:gpqa-results}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nModel & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\\\\n\\midrule\nDeepSeek-R1-Distill-Qwen-7B & --- & --- & --- & --- \\\\\nQwen2.5-7B-Instruct         & --- & --- & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%% PLACEHOLDER: Fill Table~\\ref{tab:gpqa-results} when c11 experiment completes.\n%% Expected analysis: (1) phase gradient direction consistency with MATH-500/GSM8K,\n%% (2) strategy specificity comparison across task types (math vs. science reasoning),\n%% (3) whether cognitive load modulation hypothesis extends to non-mathematical domains.\n\n\\subsection{Statistical Validation}\n\\label{sec:stat-validation}\n\nTable~\\ref{tab:cohens-d} reports the paired median difference $\\Delta$ under importance-based eviction for both models at $n{=}496$/$475$. All eight conditions yield CIs excluding zero; within-importance dose-response $d_z$ (s015 vs.\\ s030) is $0.94$ (DeepSeek) and $0.92$ (Qwen), both large effects. Importance-based eviction produces significantly larger phase gradients than random at all four sparsity levels ($p_{\\text{Bonf}} \\ll 10^{-10}$, Wilcoxon; permutation tests in Appendix~\\ref{app:permutation-details}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Median of paired differences ($\\Delta_i = \\mathrm{II}^{(i)}_{\\textit{low}} - \\mathrm{II}^{(i)}_{\\textit{high}}$) under importance-based eviction with bootstrap 95\\% CIs ($B{=}10{,}000$).}\n\\label{tab:cohens-d}\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n$s$ & DS ($n{=}496$): $\\widetilde{\\Delta}$\\; [95\\% CI] & QW ($n{=}475$): $\\widetilde{\\Delta}$\\; [95\\% CI] \\\\\n\\midrule\n0.15 & $0.39$\\; $[0.35,\\; 0.44]$ & $0.07$\\; $[0.05,\\; 0.09]$ \\\\\n0.20 & $1.21$\\; $[1.11,\\; 1.34]$ & $0.31$\\; $[0.26,\\; 0.36]$ \\\\\n0.25 & $3.99$\\; $[3.53,\\; 4.36]$ & $1.07$\\; $[0.98,\\; 1.18]$ \\\\\n0.30 & $8.48$\\; $[7.75,\\; 9.69]$ & $3.16$\\; $[2.78,\\; 3.56]$ \\\\\n\\bottomrule\n\\multicolumn{3}{@{}l}{\\footnotesize All $p_{\\text{Bonf}} < 10^{-13}$. Within-importance $d_z$ (s015 vs.\\ s030): DS $0.94$, QW $0.92$.}\n\\end{tabular}\n\\end{table}\n\n\\subsection{Answer-Region Analysis}\n\\label{sec:answer-region}\n\nAcross both models, 93.2\\% of answer tokens (\\verb|\\boxed{}| markers) fall within the high-sparsity phase, where compound interaction is minimal. This non-uniformity identifies \\emph{where} severity concentrates: reasoning-trace tokens show $5.7$--$43.5{\\times}$ PPL degradation vs.\\ $1.3$--$5.3{\\times}$ for answer tokens (Wilcoxon $p < 0.001$). However, reasoning-trace degradation may produce \\emph{silent reasoning errors}---correct formatting with corrupted intermediate logic \\cite{lanham-2023-faithfulness, turpin-2023-biased-cot}---a failure mode that PPL detects but answer-level accuracy may miss.\n\n\\subsection{Downstream Accuracy Validation}\n\\label{sec:accuracy-validation}\n\nTo validate that the PPL-based severity gradient translates to downstream task performance, we evaluate MATH-500 accuracy under compound sparsity (importance-based eviction, \\texttt{max\\_new\\_tokens}${=}$8192; Table~\\ref{tab:accuracy}). Qwen's minimal truncation ($\\leq 4\\%$) provides a clean PPL-accuracy bridge.\nQwen ($n{=}100$; truncation $\\leq 4\\%$) shows gradual decline from $46\\%$ (dense) through $s{=}0.25$ ($\\delta{=}-4$ to $-13$\\,pp) with a sharp cliff at $s{=}0.30$ ($19\\%$, $\\delta{=}-27$\\,pp). DeepSeek ($n{=}50$) degrades more steeply ($74\\% \\to 4\\%$) with a dual-regime structure: at $s \\leq 0.20$, degradation is primarily truncation-driven (non-truncated accuracy remains $68$--$71\\%$ at $s{=}0.15$--$0.20$ vs.\\ $88\\%$ dense); at $s \\geq 0.25$, both truncation and reasoning quality collapse simultaneously (Appendix~\\ref{app:accuracy-details}).\nThe two models exhibit distinct failure modes reflecting training-paradigm dependence: DeepSeek failures are \\emph{truncation-dominated} (truncation $16\\% \\to 76\\%$), while Qwen failures are \\emph{wrong-answer-dominated} (truncation $\\leq 4\\%$, reasoning quality degrades directly). Given minimal truncation, Qwen accuracy data provide a reliable PPL-accuracy bridge; DeepSeek accuracy results, confounded by truncation rates of $16\\%$--$76\\%$, should be interpreted as qualitative observations only.\n\nWe provide a correlational mechanistic analysis in terms of importance discrimination collapse in \\S\\ref{sec:analysis}.\n",
      "numLines": 195,
      "startLine": 1,
      "totalLines": 195
    }
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Read · `toolu_01H7DzcUuTWq7c7nZVwDJEs1`</summary>

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
  "session_id": "e127786f-a191-4d01-b58d-071eb9fc50fc",
  "uuid": "17ea82c1-dcdf-4ea9-8984-1f753cbc35ff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qs6Zv4TTFooKBHUBayTD8F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10011,
      "cache_read_input_tokens": 31389,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10011
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

_source line 21 · 2026-05-16T22:42:52.655Z_

<details><summary>↩ Tool result · `toolu_01H7DzcUuTWq7c7nZVwDJEs1`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We showed that compound sparsity severity is not phase-invariant but exhibits an emergent phase-strategy interaction. Under importance-based eviction, the paired median difference $\Delta$ increases from $0.39$ to $8.48$ (DeepSeek, $n{=}500$; Spearman $\rho{=}1.0$) and $0.07$ to $3.16$ (Qwen, $n{=}475$), all $p < 10^{-13}$. Random eviction is $2.7$--$17{\times}$ weaker where both strategies are significant ($s \geq 0.25$; DeepSeek $15$--$17{\times}$, Qwen $2.7$--$3.5{\times}$). The importance phase gradient replicates on LlamaForCausalLM ($d_z{=}0.81$--$1.15$, $n{=}250$, all $p < 10^{-29}$), supporting architecture-generality of phase modulation, while strategy specificity is architecture-dependent ($2.0$--$2.6{\times}$ on LLaMA vs.\ $15$--$17{\times}$ on DeepSeek). A model-dependent crossover on DeepSeek demonstrates that no single strategy dominates uniformly. Per-phase Gini analysis reveals importance discrimination collapse as a correlational diagnostic: despite near-identical aggregate Gini drops, severity diverges by $2.7$--$17{\times}$, implicating the structural specificity of importance-based pruning.
5	Beyond the empirical findings, the phase-gated analysis framework itself---decomposing compound severity by reasoning phase and eviction strategy---transforms a scalar interaction metric into a structured diagnostic that reveals where compound sparsity fails and why. This framework provides practitioners with a principled basis for phase-aware sparsity allocation: applying aggressive compression during high-sparsity (structured computation) phases while preserving budget during low-sparsity (exploratory reasoning) phases. Future work could explore generalization to other reasoning domains, causal validation of importance discrimination collapse, and systematic characterization of asymmetric compound interactions.
6	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e127786f-a191-4d01-b58d-071eb9fc50fc",
  "uuid": "74d2ea18-daaa-41e3-b0b7-3882a32aaa9e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex",
      "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe showed that compound sparsity severity is not phase-invariant but exhibits an emergent phase-strategy interaction. Under importance-based eviction, the paired median difference $\\Delta$ increases from $0.39$ to $8.48$ (DeepSeek, $n{=}500$; Spearman $\\rho{=}1.0$) and $0.07$ to $3.16$ (Qwen, $n{=}475$), all $p < 10^{-13}$. Random eviction is $2.7$--$17{\\times}$ weaker where both strategies are significant ($s \\geq 0.25$; DeepSeek $15$--$17{\\times}$, Qwen $2.7$--$3.5{\\times}$). The importance phase gradient replicates on LlamaForCausalLM ($d_z{=}0.81$--$1.15$, $n{=}250$, all $p < 10^{-29}$), supporting architecture-generality of phase modulation, while strategy specificity is architecture-dependent ($2.0$--$2.6{\\times}$ on LLaMA vs.\\ $15$--$17{\\times}$ on DeepSeek). A model-dependent crossover on DeepSeek demonstrates that no single strategy dominates uniformly. Per-phase Gini analysis reveals importance discrimination collapse as a correlational diagnostic: despite near-identical aggregate Gini drops, severity diverges by $2.7$--$17{\\times}$, implicating the structural specificity of importance-based pruning.\nBeyond the empirical findings, the phase-gated analysis framework itself---decomposing compound severity by reasoning phase and eviction strategy---transforms a scalar interaction metric into a structured diagnostic that reveals where compound sparsity fails and why. This framework provides practitioners with a principled basis for phase-aware sparsity allocation: applying aggressive compression during high-sparsity (structured computation) phases while preserving budget during low-sparsity (exploratory reasoning) phases. Future work could explore generalization to other reasoning domains, causal validation of importance discrimination collapse, and systematic characterization of asymmetric compound interactions.\n",
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

_source line 22_

<details open><summary>🔧 Tool call — Read · `toolu_01Pykfjj5AdzTcSDMGTQ1ygC`</summary>

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
  "session_id": "e127786f-a191-4d01-b58d-071eb9fc50fc",
  "uuid": "999b9a4b-980d-4238-bd1c-533d9e949250",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qs6Zv4TTFooKBHUBayTD8F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10011,
      "cache_read_input_tokens": 31389,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10011
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

_source line 23 · 2026-05-16T22:42:53.689Z_

<details><summary>↩ Tool result · `toolu_01Pykfjj5AdzTcSDMGTQ1ygC`</summary>

```text
1	
2	\section{Phase-Strategy Crossover Details}
3	\label{app:crossover-details}
4	
5	On DeepSeek ($n{=}496$), a strategy ranking reversal emerges at $s{=}0.25$ (Figure~\ref{fig:crossover}): importance-based eviction yields \emph{lower} II than random in the high-sparsity phase ($0.021$ vs.\ $1.113$) but \emph{higher} II in the low-sparsity phase ($3.971$ vs.\ $1.514$---a $2.6{\times}$ reversal; both $p < 10^{-4}$). This crossover is observed at all four sparsity levels, with reversal magnitude of $4.0{\times}$ at $s{=}0.15$, $3.4{\times}$ at $s{=}0.20$, $2.6{\times}$ at $s{=}0.25$, and $2.2{\times}$ at $s{=}0.30$ (decreasing as random eviction severity rises). The reversal arises because head pruning redistributes attention mass, altering importance rankings in a way that couples the two sparsity mechanisms in low-sparsity phases (\S\ref{sec:discrimination-collapse-main}). Qwen does not exhibit a crossover: importance-based eviction produces lower II than random in both phases across all sparsity levels (e.g., at $s{=}0.25$: high $0.004$ vs.\ $1.108$; low $1.053$ vs.\ $1.769$).
6	
7	\begin{figure}[t]
8	\centering
9	\includegraphics[width=\columnwidth]{fig3_crossover.pdf}
10	\caption{Strategy-dependent crossover at $s{=}0.25$ on DeepSeek ($n{=}496$). Grouped bar chart of median II by eviction strategy and reasoning phase. Importance-based eviction outperforms random in the high-sparsity phase but produces $2.6{\times}$ higher II in the low-sparsity phase, reversing the strategy ranking.}
11	\label{fig:crossover}
12	\end{figure}
13	
14	
15	\section{Profiling Subset Per-Phase Breakdown}
16	\label{app:profiling-subset}
17	
18	\begin{table*}[t]
19	\centering
20	\small
21	\caption{Per-phase interaction index (II) from the $n{=}50$ profiling subset (DeepSeek-R1-Distill-Qwen-7B). This preliminary table does not include per-condition bootstrap CIs; full-scale values with bootstrap 95\% CIs ($B{=}10{,}000$) at $n{=}496$ appear in Table~\ref{tab:main-results}, and strategy-contrast CIs for this subset appear in the permutation test (Table~\ref{tab:permutation}). $G$ values use the ratio-of-medians definition ($\widetilde{\mathrm{II}}_{\textit{low}} / \widetilde{\mathrm{II}}_{\textit{high}}$) and serve as an auxiliary illustration of phase concentration; the primary evidence is $\Delta$ (see Appendix~\ref{app:g-metric}). At low sparsity ($s{=}0.15$), the ratio-of-medians and per-problem definitions diverge ($7.5{\times}$ vs.\ $69{\times}$) because per-problem ratios are sensitive to near-zero $\mathrm{II}_{\textit{high}}$ values.}
22	\label{tab:profiling-subset}
23	\begin{tabular}{@{}llccccr@{}}
24	\toprule
25	$s$ & Strategy & $\widetilde{\mathrm{II}}_{\textit{high}}$ & $\widetilde{\mathrm{II}}_{\textit{mid}}$ & $\widetilde{\mathrm{II}}_{\textit{low}}$ & $\Delta$ & $G$ \\
26	\midrule
27	0.15 & Importance & 0.006 & 0.081 & 0.398 & 0.39 & $\mathbf{69}$ \\
28	0.15 & Random     & 0.093 & 0.097 & 0.103 & 0.01 & 1.1 \\
29	\addlinespace
30	0.20 & Importance & 0.015 & 0.203 & 1.496 & 1.48 & $\mathbf{103}$ \\
31	0.20 & Random     & 0.292 & 0.350 & 0.276 & $-$0.02 & 0.9 \\
32	\addlinespace
33	0.25 & Importance & 0.032 & 1.118 & 7.196 & 7.16 & $\mathbf{222}$ \\
34	0.25 & Random     & 0.818 & 0.932 & 1.363 & 0.54 & 1.7 \\
35	\addlinespace
36	0.30 & Importance & 0.053 & 2.283 & 14.639 & 14.59 & $\mathbf{274}$ \\
37	0.30 & Random     & 2.503 & 2.592 & 4.041 & 1.54 & 1.6 \\
38	\bottomrule
39	\end{tabular}
40	\end{table*}
41	
42	The $n{=}50$ profiling subset served as a preliminary calibration; all importance-based $\Delta$ values were subsequently replicated at $n{=}496$ with bootstrap 95\% CIs excluding zero (Table~\ref{tab:main-results}: $\Delta{=}0.39$\;$[0.35,\;0.44]$ to $8.48$\;$[7.75,\;9.69]$). The paired permutation test on this subset ($n{=}49$; Table~\ref{tab:permutation}) provides bootstrap 95\% CIs for the strategy contrast ($\widetilde{\Delta}_{\text{imp}} - \widetilde{\Delta}_{\text{rand}}$), all excluding zero after Bonferroni correction.
43	
44	
45	\section{Cross-Training-Paradigm Replication Details}
46	\label{app:cross-model-details}
47	
48	Both models share the Qwen2ForCausalLM backbone (28 layers, 28 heads, 4-group GQA) but differ in training: DeepSeek uses reasoning distillation from DeepSeek-R1, while Qwen2.5 uses standard instruction tuning without explicit reasoning delimiters. This within-architecture-family comparison enables assessment of training methodology effects on the compound sparsity interaction, though causal attribution is limited by the observational design.
49	
50	Despite lacking explicit \texttt{&lt;think>} delimiters, Qwen2.5-7B-Instruct exhibits sufficient variation in attention sparsity to permit phase segmentation via the same quantile-based method (\S\ref{par:phase-segmentation}). Twenty-five of the 500 problems are excluded due to degenerate phase assignments, yielding $n{=}475$ valid problems for Qwen (vs.\ $n{=}496$ for DeepSeek).
51	
52	\paragraph{Per-phase effective sample size.}
53	\label{app:qwen-null-rate}
54	Table~\ref{tab:qwen-effective-n} reports the per-phase effective sample size for Qwen2.5-7B-Instruct, defined as the number of problems with non-null phase segments (segment length $\geq$ \texttt{min\_phase\_length}). The mid-phase null rate (45.2\%) reflects problems where mid-sparsity tokens do not form contiguous runs above the merging threshold; this does not affect the low--high contrast ($\Delta$) used in the primary analysis.
55	
56	\begin{table}[t]
57	\centering
58	\small
59	\caption{Per-phase effective sample size for Qwen2.5-7B-Instruct ($n_{\text{eff}} = 475$). Phase segmentation is performed once on dense-model attention patterns and is independent of sparsity level.}
60	\label{tab:qwen-effective-n}
61	\begin{tabular}{@{}lcccc@{}}
62	\toprule
63	Phase & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
64	\midrule
65	High & 475 & 475 & 475 & 475 \\
66	Mid  & 274 & 274 & 274 & 274 \\
67	Low  & 475 & 475 & 475 & 475 \\
68	\bottomrule
69	\end{tabular}
70	\end{table}
71	
72	Table~\ref{tab:cross-model} reports the cross-training-paradigm comparison. Qwen reproduces the monotonic severity gradient at ${\sim}1/5$ of DeepSeek's magnitude. Figure~\ref{fig:cross-model} visualizes this comparison.
73	
74	\begin{table}[t]
75	\centering
76	\small
77	\caption{Cross-training-paradigm comparison of median compound severity difference ($\Delta$) under importance-based eviction.}
78	\label{tab:cross-model}
79	\begin{tabular}{@{}lcccc@{}}
80	\toprule
81	Model & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
82	\midrule
83	DeepSeek-R1-Distill-Qwen-7B ($n{=}496$) & 0.39 & 1.21 & 3.99 & 8.48 \\
84	Qwen2.5-7B-Instruct ($n{=}475$)         & 0.07 & 0.31 & 1.07 & 3.16 \\
85	\bottomrule
86	\end{tabular}
87	\end{table}
88	
89	\begin{figure}[t]
90	\centering
91	\includegraphics[width=\columnwidth]{fig5_crossmodel.pdf}
92	\caption{Cross-training-paradigm comparison of the median severity difference under importance-based eviction ($n{=}496$/$475$). Both DeepSeek (solid) and Qwen (dashed) exhibit monotonically increasing $\Delta$ with sparsity; Qwen's magnitude is approximately one-quarter to one-sixth of DeepSeek's.}
93	\label{fig:cross-model}
94	\end{figure}
95	
96	\paragraph{Per-problem concordance.}
97	The per-problem concordance across models is not significant (mean $\rho = -0.107$, $p = 0.926$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking.
98	
99	\paragraph{Random eviction control.}
100	As a control, random eviction on Qwen mirrors DeepSeek: non-significant at $s \leq 0.20$ ($\Delta$: $-0.01$, $0.02$; CIs span zero) but significant at $s \geq 0.25$ ($\Delta{=}0.39$, $p_{\text{Bonf}} < 10^{-10}$; $\Delta{=}0.91$, $p_{\text{Bonf}} < 10^{-13}$). Where significant, the random phase gradient is $2.7$--$3.5{\times}$ weaker than importance-based ($0.39$ vs.\ $1.07$ at $s{=}0.25$; $0.91$ vs.\ $3.16$ at $s{=}0.30$), supporting strategy-specific amplification.
101	
102	
103	\section{Permutation Test Details}
104	\label{app:permutation-details}
105	
106	For each problem $i$ and sparsity level $s$, we compute the compound severity difference $\Delta_i^{(\text{strat})} = \mathrm{II}_{\textit{low},i} - \mathrm{II}_{\textit{high},i}$ under each eviction strategy. The test statistic is the median of the paired difference $\widetilde{\Delta} = \text{median}_i\!\bigl(\Delta_i^{(\text{imp})} - \Delta_i^{(\text{rand})}\bigr)$, measuring whether importance-based eviction produces systematically larger phase-dependent severity than random eviction. We permute strategy labels $10{,}000$ times to construct the null distribution and apply Bonferroni correction for 4 sparsity-level comparisons.
107	
108	Per-problem distributions of the paired severity difference $\Delta_i = \mathrm{II}_{\textit{low},i} - \mathrm{II}_{\textit{high},i}$ under importance-based eviction are right-skewed at all sparsity levels, with mean/median ratios ranging from $1.2{\times}$ ($s{=}0.15$) to $1.6{\times}$ ($s{=}0.30$) for DeepSeek and $1.1{\times}$ to $1.4{\times}$ for Qwen.
109	
110	The permutation null distributions are approximately symmetric around zero at all sparsity levels. At $s{=}0.15$, the observed statistic falls at the $99.92$th percentile of the null ($p_{\text{Bonf}} = 0.0032$); at $s \geq 0.20$, no permutation exceeds the observed statistic.
111	
112	Table~\ref{tab:permutation} reports the results. All four sparsity levels reject $H_0$ after Bonferroni correction ($p_{\text{Bonf}} < 0.005$), with observed median differences increasing monotonically from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$. The monotonic growth of both the point estimate and the CI lower bound ($0.19 \to 0.69 \to 1.66 \to 6.70$) supports that compound severity amplification strengthens with sparsity---not merely in central tendency but also in worst-case lower bounds. Figure~\ref{fig:permtest-forest} presents these results as a forest plot.
113	
114	\begin{table}[t]
115	\centering
116	\small
117	\caption{Paired permutation test for compound severity: importance vs.\ random eviction on DeepSeek-R1-Distill-Qwen-7B ($n{=}49$ profiling subset, $10{,}000$ permutations, Bonferroni-corrected). The monotonic $\Delta$ pattern is supported at $n{=}496$ (Table~\ref{tab:aggregate-ii}).}
118	\label{tab:permutation}
119	\begin{tabular}{@{}rrcl@{}}
120	\toprule
121	$s$ & Observed $\widetilde{\Delta}$ & 95\% CI & $p_{\text{Bonf}}$ \\
122	\midrule
123	0.15 & 0.37 & $[0.19,\; 0.62]$ & 0.0032 \\
124	0.20 & 0.97 & $[0.69,\; 1.49]$ & ${<}\,0.001$ \\
125	0.25 & 3.34 & $[1.66,\; 6.64]$ & ${<}\,0.001$ \\
126	0.30 & 9.85 & $[6.70,\; 16.29]$ & ${<}\,0.001$ \\
127	\bottomrule
128	\end{tabular}
129	\end{table}
130	
131	\begin{figure}[t]
132	\centering
133	\includegraphics[width=\columnwidth]{fig4_bootstrap.pdf}
134	\caption{Forest plot of permutation test results. Horizontal bars show 95\% permutation CIs; diamonds mark observed median differences $\widetilde{\Delta}$. All CIs lie entirely above zero, supporting significant strategy-dependent severity at every sparsity level.}
135	\label{fig:permtest-forest}
136	\end{figure}
137	
138	
139	\section{Cross-Architecture Analysis}
140	\label{app:cross-arch}
141	
142	To test whether the phase-modulated severity pattern extends beyond the Qwen2 architecture, we replicate the full experiment on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, 8B parameters; $n{=}250$, MATH-500) under both importance-based and random eviction at $s \in \{0.15, 0.20, 0.25, 0.30\}$. Table~\ref{tab:llama-cross-arch} reports paired median differences and effect sizes for all 8 conditions.
143	
144	The within-importance phase gradient replicates with large effect sizes: $\Delta$ rises monotonically from $0.050$ ($s{=}0.15$, $d_z{=}0.81$) to $0.695$ ($s{=}0.30$, $d_z{=}1.15$), all $p < 10^{-29}$. An architecture-specific difference emerges in strategy specificity: random eviction on LLaMA also exhibits statistically significant phase gradients at all four sparsity levels ($\Delta{=}0.025$--$0.271$; $d_z{=}0.41$--$0.46$; all $p < 10^{-12}$), unlike DeepSeek and Qwen where random eviction is non-significant at $s \leq 0.20$. The importance/random $\Delta$ ratio on LLaMA is $2.0$--$2.6{\times}$, substantially weaker than the $15$--$17{\times}$ observed on DeepSeek.
145	
146	Dose-response monotonicity holds for both strategies across all sparsity levels, supporting the phase gradient as an architecture-general phenomenon. The reduced strategy specificity on LLaMA suggests that GQA's grouped key-value structure partially preserves importance score quality under head pruning, attenuating the discrimination collapse that drives strategy divergence on MHA architectures.
147	
148	\begin{table}[t]
149	\centering
150	\small
151	\caption{Cross-architecture validation: paired median difference ($\Delta$) and effect size ($d_z$) on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, $n{=}250$, MATH-500). All conditions are monotonic.}
152	\label{tab:llama-cross-arch}
153	\begin{tabular}{@{}llccc@{}}
154	\toprule
155	$s$ & Strategy & $\Delta$ & $d_z$ & $p$ \\
156	\midrule
157	0.15 & Importance & $0.050$ & $0.814$ & $1.4 \times 10^{-29}$ \\
158	0.15 & Random     & $0.025$ & $0.436$ & $9.3 \times 10^{-13}$ \\
159	\addlinespace
160	0.20 & Importance & $0.159$ & $1.010$ & $8.9 \times 10^{-35}$ \\
161	0.20 & Random     & $0.065$ & $0.459$ & $3.6 \times 10^{-15}$ \\
162	\addlinespace
163	0.25 & Importance & $0.376$ & $1.115$ & $4.3 \times 10^{-39}$ \\
164	0.25 & Random     & $0.184$ & $0.424$ & $3.8 \times 10^{-13}$ \\
165	\addlinespace
166	0.30 & Importance & $0.695$ & $1.150$ & $1.5 \times 10^{-40}$ \\
167	0.30 & Random     & $0.271$ & $0.410$ & $6.0 \times 10^{-12}$ \\
168	\bottomrule
169	\multicolumn{5}{@{}l}{\footnotesize Imp/Rand $\Delta$ ratio: $2.0$--$2.6{\times}$ (cf.\ $15$--$17{\times}$ on DeepSeek).}
170	\end{tabular}
171	\end{table}
172	
173	\paragraph{Magnitude comparison.}
174	LLaMA interaction magnitudes are approximately $7$--$12{\times}$ smaller than Qwen2-architecture models at matched sparsity. This gap likely reflects differences in attention head specialization between MHA (Qwen2, 28 heads) and GQA (LLaMA, 32 heads with 8 KV groups). The phase gradient direction and dose-response monotonicity replicate, supporting the architecture-generality of phase-modulated compound interaction. Strategy specificity, however, is weaker ($2.0$--$2.6{\times}$ on LLaMA vs.\ $15$--$17{\times}$ on DeepSeek), indicating that the magnitude of strategy${\times}$phase interaction depends on architectural factors governing importance score stability under pruning.
175	
176	
177	\section{Analysis: Importance Discrimination Collapse}
178	\label{app:analysis}
179	
180	\subsection{Importance Discrimination Collapse}
181	\label{sec:discrimination-collapse}
182	
183	Head pruning reduces the number of heads contributing to cumulative importance scores, collapsing the score distribution. Table~\ref{tab:discrimination-metrics-full} quantifies this effect: the Gini coefficient decreases by $0.030$--$0.081$ (DeepSeek) and $0.010$--$0.020$ (Qwen) after pruning, with consistent negative deltas across all 16 conditions (both models $\times$ 4 sparsity levels $\times$ 2 strategies). The CV delta is likewise negative in all 8 importance-based conditions. The same pattern holds under random eviction, indicating that importance discrimination collapse is a consequence of head pruning \emph{per se}, not of the eviction strategy.
184	
185	\begin{table}[t]
186	\centering
187	\caption{Importance discrimination collapse under importance-based eviction. $\Delta\mathrm{Gini}$ and $\Delta\mathrm{CV}$ are post-pruning minus baseline; negative values indicate reduced discriminative power.}
188	\label{tab:discrimination-metrics-full}
189	\small
190	\begin{tabular}{llrr}
191	\toprule
192	Model & $s$ & $\Delta\mathrm{Gini}$ & $\Delta\mathrm{CV}$ \\
193	\midrule
194	DeepSeek & $0.15$ & $-0.030$ & $-0.56$ \\
195	DeepSeek & $0.20$ & $-0.040$ & $-0.77$ \\
196	DeepSeek & $0.25$ & $-0.065$ & $-1.29$ \\
197	DeepSeek & $0.30$ & $-0.081$ & $-1.66$ \\
198	\midrule
199	Qwen & $0.15$ & $-0.010$ & $-0.05$ \\
200	Qwen & $0.20$ & $-0.012$ & $-0.21$ \\
201	Qwen & $0.25$ & $-0.010$ & $-1.49$ \\
202	Qwen & $0.30$ & $-0.020$ & $-1.14$ \\
203	\bottomrule
204	\end{tabular}
205	\end{table}
206	
207	When importance scores lose discriminability, thresholding degenerates into noise-sensitive selection---functionally approaching biased random eviction. This is phase-dependent: in low-sparsity phases, attention is already broadly distributed, so pruning-induced collapse has maximum impact; in high-sparsity phases, concentration is preserved. Random eviction is immune because its decisions are independent of score quality, consistent with $G \approx 1$.
208	
209	\subsection{Entropy Redistribution}
210	\label{sec:entropy-redistribution}
211	
212	Beyond importance discrimination collapse, we examine whether head pruning also redistributes the attention entropy of surviving heads. We measure the mean attention entropy per head:
213	\begin{equation}
214	    \mathcal{H}_i^{(h)} = -\sum_{j=1}^{T} a_{ij}^{(h)} \log a_{ij}^{(h)}
215	    \label{eq:attn-entropy}
216	\end{equation}
217	and compute $\Delta\mathcal{H}$ as the change from baseline (no pruning) to the pruned condition.
218	
219	For DeepSeek under importance-based eviction, the entropy delta is consistently negative across all four sparsity levels ($\Delta\mathcal{H} \in [-0.047, -0.040]$; Table~\ref{tab:entropy-deltas}), indicating that importance-based pruning systematically selects heads whose removal concentrates attention in the surviving heads, reinforcing importance discrimination collapse.
220	
221	For Qwen, the entropy pattern only partially replicates. The delta is negative at $s{=}0.15$ ($\Delta\mathcal{H} = -0.073$) and $s{=}0.20$ ($-0.076$), consistent with DeepSeek. However, at $s{=}0.25$, the delta reverses to $+0.045$, with 22 of 30 problems showing positive entropy change. At $s{=}0.30$, the delta is near zero ($-0.007$). The $s{=}0.25$ reversal is systematic rather than a statistical artifact: it is consistent across all three reasoning phases (low: $+0.042$, mid: $+0.034$, high: $+0.017$). We interpret this as a genuine model-specific difference, possibly arising from distinct head specialization patterns: Qwen's instruction tuning (vs.\ DeepSeek's distillation-based training) may produce head configurations where removing 25\% of heads triggers compensatory broadening rather than concentration.
222	
223	We characterize importance discrimination collapse as the robust, model-independent driver of the phase-strategy interaction, with entropy redistribution as a secondary amplifier that is consistent in DeepSeek but model-dependent in Qwen.
224	
225	\begin{table}[t]
226	\centering
227	\caption{Attention entropy deltas ($\Delta\mathcal{H}$) under importance-based eviction. DeepSeek shows consistent entropy compression; Qwen partially replicates with a reversal at $s{=}0.25$.}
228	\label{tab:entropy-deltas}
229	\small
230	\begin{tabular}{llr}
231	\toprule
232	Model & $s$ & $\Delta\mathcal{H}$ \\
233	\midrule
234	DeepSeek & $0.15$ & $-0.040$ \\
235	DeepSeek & $0.20$ & $-0.047$ \\
236	DeepSeek & $0.25$ & $-0.045$ \\
237	DeepSeek & $0.30$ & $-0.044$ \\
238	\midrule
239	Qwen & $0.15$ & $-0.073$ \\
240	Qwen & $0.20$ & $-0.076$ \\
241	Qwen & $0.25$ & $+0.045$ \\
242	Qwen & $0.30$ & $-0.007$ \\
243	\bottomrule
244	\end{tabular}
245	\end{table}
246	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e127786f-a191-4d01-b58d-071eb9fc50fc",
  "uuid": "df5f331c-2bb9-4723-8b72-16d3aab712f4",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex",
      "content": "\n\\section{Phase-Strategy Crossover Details}\n\\label{app:crossover-details}\n\nOn DeepSeek ($n{=}496$), a strategy ranking reversal emerges at $s{=}0.25$ (Figure~\\ref{fig:crossover}): importance-based eviction yields \\emph{lower} II than random in the high-sparsity phase ($0.021$ vs.\\ $1.113$) but \\emph{higher} II in the low-sparsity phase ($3.971$ vs.\\ $1.514$---a $2.6{\\times}$ reversal; both $p < 10^{-4}$). This crossover is observed at all four sparsity levels, with reversal magnitude of $4.0{\\times}$ at $s{=}0.15$, $3.4{\\times}$ at $s{=}0.20$, $2.6{\\times}$ at $s{=}0.25$, and $2.2{\\times}$ at $s{=}0.30$ (decreasing as random eviction severity rises). The reversal arises because head pruning redistributes attention mass, altering importance rankings in a way that couples the two sparsity mechanisms in low-sparsity phases (\\S\\ref{sec:discrimination-collapse-main}). Qwen does not exhibit a crossover: importance-based eviction produces lower II than random in both phases across all sparsity levels (e.g., at $s{=}0.25$: high $0.004$ vs.\\ $1.108$; low $1.053$ vs.\\ $1.769$).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig3_crossover.pdf}\n\\caption{Strategy-dependent crossover at $s{=}0.25$ on DeepSeek ($n{=}496$). Grouped bar chart of median II by eviction strategy and reasoning phase. Importance-based eviction outperforms random in the high-sparsity phase but produces $2.6{\\times}$ higher II in the low-sparsity phase, reversing the strategy ranking.}\n\\label{fig:crossover}\n\\end{figure}\n\n\n\\section{Profiling Subset Per-Phase Breakdown}\n\\label{app:profiling-subset}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Per-phase interaction index (II) from the $n{=}50$ profiling subset (DeepSeek-R1-Distill-Qwen-7B). This preliminary table does not include per-condition bootstrap CIs; full-scale values with bootstrap 95\\% CIs ($B{=}10{,}000$) at $n{=}496$ appear in Table~\\ref{tab:main-results}, and strategy-contrast CIs for this subset appear in the permutation test (Table~\\ref{tab:permutation}). $G$ values use the ratio-of-medians definition ($\\widetilde{\\mathrm{II}}_{\\textit{low}} / \\widetilde{\\mathrm{II}}_{\\textit{high}}$) and serve as an auxiliary illustration of phase concentration; the primary evidence is $\\Delta$ (see Appendix~\\ref{app:g-metric}). At low sparsity ($s{=}0.15$), the ratio-of-medians and per-problem definitions diverge ($7.5{\\times}$ vs.\\ $69{\\times}$) because per-problem ratios are sensitive to near-zero $\\mathrm{II}_{\\textit{high}}$ values.}\n\\label{tab:profiling-subset}\n\\begin{tabular}{@{}llccccr@{}}\n\\toprule\n$s$ & Strategy & $\\widetilde{\\mathrm{II}}_{\\textit{high}}$ & $\\widetilde{\\mathrm{II}}_{\\textit{mid}}$ & $\\widetilde{\\mathrm{II}}_{\\textit{low}}$ & $\\Delta$ & $G$ \\\\\n\\midrule\n0.15 & Importance & 0.006 & 0.081 & 0.398 & 0.39 & $\\mathbf{69}$ \\\\\n0.15 & Random     & 0.093 & 0.097 & 0.103 & 0.01 & 1.1 \\\\\n\\addlinespace\n0.20 & Importance & 0.015 & 0.203 & 1.496 & 1.48 & $\\mathbf{103}$ \\\\\n0.20 & Random     & 0.292 & 0.350 & 0.276 & $-$0.02 & 0.9 \\\\\n\\addlinespace\n0.25 & Importance & 0.032 & 1.118 & 7.196 & 7.16 & $\\mathbf{222}$ \\\\\n0.25 & Random     & 0.818 & 0.932 & 1.363 & 0.54 & 1.7 \\\\\n\\addlinespace\n0.30 & Importance & 0.053 & 2.283 & 14.639 & 14.59 & $\\mathbf{274}$ \\\\\n0.30 & Random     & 2.503 & 2.592 & 4.041 & 1.54 & 1.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nThe $n{=}50$ profiling subset served as a preliminary calibration; all importance-based $\\Delta$ values were subsequently replicated at $n{=}496$ with bootstrap 95\\% CIs excluding zero (Table~\\ref{tab:main-results}: $\\Delta{=}0.39$\\;$[0.35,\\;0.44]$ to $8.48$\\;$[7.75,\\;9.69]$). The paired permutation test on this subset ($n{=}49$; Table~\\ref{tab:permutation}) provides bootstrap 95\\% CIs for the strategy contrast ($\\widetilde{\\Delta}_{\\text{imp}} - \\widetilde{\\Delta}_{\\text{rand}}$), all excluding zero after Bonferroni correction.\n\n\n\\section{Cross-Training-Paradigm Replication Details}\n\\label{app:cross-model-details}\n\nBoth models share the Qwen2ForCausalLM backbone (28 layers, 28 heads, 4-group GQA) but differ in training: DeepSeek uses reasoning distillation from DeepSeek-R1, while Qwen2.5 uses standard instruction tuning without explicit reasoning delimiters. This within-architecture-family comparison enables assessment of training methodology effects on the compound sparsity interaction, though causal attribution is limited by the observational design.\n\nDespite lacking explicit \\texttt{&lt;think>} delimiters, Qwen2.5-7B-Instruct exhibits sufficient variation in attention sparsity to permit phase segmentation via the same quantile-based method (\\S\\ref{par:phase-segmentation}). Twenty-five of the 500 problems are excluded due to degenerate phase assignments, yielding $n{=}475$ valid problems for Qwen (vs.\\ $n{=}496$ for DeepSeek).\n\n\\paragraph{Per-phase effective sample size.}\n\\label{app:qwen-null-rate}\nTable~\\ref{tab:qwen-effective-n} reports the per-phase effective sample size for Qwen2.5-7B-Instruct, defined as the number of problems with non-null phase segments (segment length $\\geq$ \\texttt{min\\_phase\\_length}). The mid-phase null rate (45.2\\%) reflects problems where mid-sparsity tokens do not form contiguous runs above the merging threshold; this does not affect the low--high contrast ($\\Delta$) used in the primary analysis.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Per-phase effective sample size for Qwen2.5-7B-Instruct ($n_{\\text{eff}} = 475$). Phase segmentation is performed once on dense-model attention patterns and is independent of sparsity level.}\n\\label{tab:qwen-effective-n}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nPhase & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\\\\n\\midrule\nHigh & 475 & 475 & 475 & 475 \\\\\nMid  & 274 & 274 & 274 & 274 \\\\\nLow  & 475 & 475 & 475 & 475 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:cross-model} reports the cross-training-paradigm comparison. Qwen reproduces the monotonic severity gradient at ${\\sim}1/5$ of DeepSeek's magnitude. Figure~\\ref{fig:cross-model} visualizes this comparison.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-training-paradigm comparison of median compound severity difference ($\\Delta$) under importance-based eviction.}\n\\label{tab:cross-model}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nModel & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\\\\n\\midrule\nDeepSeek-R1-Distill-Qwen-7B ($n{=}496$) & 0.39 & 1.21 & 3.99 & 8.48 \\\\\nQwen2.5-7B-Instruct ($n{=}475$)         & 0.07 & 0.31 & 1.07 & 3.16 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig5_crossmodel.pdf}\n\\caption{Cross-training-paradigm comparison of the median severity difference under importance-based eviction ($n{=}496$/$475$). Both DeepSeek (solid) and Qwen (dashed) exhibit monotonically increasing $\\Delta$ with sparsity; Qwen's magnitude is approximately one-quarter to one-sixth of DeepSeek's.}\n\\label{fig:cross-model}\n\\end{figure}\n\n\\paragraph{Per-problem concordance.}\nThe per-problem concordance across models is not significant (mean $\\rho = -0.107$, $p = 0.926$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking.\n\n\\paragraph{Random eviction control.}\nAs a control, random eviction on Qwen mirrors DeepSeek: non-significant at $s \\leq 0.20$ ($\\Delta$: $-0.01$, $0.02$; CIs span zero) but significant at $s \\geq 0.25$ ($\\Delta{=}0.39$, $p_{\\text{Bonf}} < 10^{-10}$; $\\Delta{=}0.91$, $p_{\\text{Bonf}} < 10^{-13}$). Where significant, the random phase gradient is $2.7$--$3.5{\\times}$ weaker than importance-based ($0.39$ vs.\\ $1.07$ at $s{=}0.25$; $0.91$ vs.\\ $3.16$ at $s{=}0.30$), supporting strategy-specific amplification.\n\n\n\\section{Permutation Test Details}\n\\label{app:permutation-details}\n\nFor each problem $i$ and sparsity level $s$, we compute the compound severity difference $\\Delta_i^{(\\text{strat})} = \\mathrm{II}_{\\textit{low},i} - \\mathrm{II}_{\\textit{high},i}$ under each eviction strategy. The test statistic is the median of the paired difference $\\widetilde{\\Delta} = \\text{median}_i\\!\\bigl(\\Delta_i^{(\\text{imp})} - \\Delta_i^{(\\text{rand})}\\bigr)$, measuring whether importance-based eviction produces systematically larger phase-dependent severity than random eviction. We permute strategy labels $10{,}000$ times to construct the null distribution and apply Bonferroni correction for 4 sparsity-level comparisons.\n\nPer-problem distributions of the paired severity difference $\\Delta_i = \\mathrm{II}_{\\textit{low},i} - \\mathrm{II}_{\\textit{high},i}$ under importance-based eviction are right-skewed at all sparsity levels, with mean/median ratios ranging from $1.2{\\times}$ ($s{=}0.15$) to $1.6{\\times}$ ($s{=}0.30$) for DeepSeek and $1.1{\\times}$ to $1.4{\\times}$ for Qwen.\n\nThe permutation null distributions are approximately symmetric around zero at all sparsity levels. At $s{=}0.15$, the observed statistic falls at the $99.92$th percentile of the null ($p_{\\text{Bonf}} = 0.0032$); at $s \\geq 0.20$, no permutation exceeds the observed statistic.\n\nTable~\\ref{tab:permutation} reports the results. All four sparsity levels reject $H_0$ after Bonferroni correction ($p_{\\text{Bonf}} < 0.005$), with observed median differences increasing monotonically from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$. The monotonic growth of both the point estimate and the CI lower bound ($0.19 \\to 0.69 \\to 1.66 \\to 6.70$) supports that compound severity amplification strengthens with sparsity---not merely in central tendency but also in worst-case lower bounds. Figure~\\ref{fig:permtest-forest} presents these results as a forest plot.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Paired permutation test for compound severity: importance vs.\\ random eviction on DeepSeek-R1-Distill-Qwen-7B ($n{=}49$ profiling subset, $10{,}000$ permutations, Bonferroni-corrected). The monotonic $\\Delta$ pattern is supported at $n{=}496$ (Table~\\ref{tab:aggregate-ii}).}\n\\label{tab:permutation}\n\\begin{tabular}{@{}rrcl@{}}\n\\toprule\n$s$ & Observed $\\widetilde{\\Delta}$ & 95\\% CI & $p_{\\text{Bonf}}$ \\\\\n\\midrule\n0.15 & 0.37 & $[0.19,\\; 0.62]$ & 0.0032 \\\\\n0.20 & 0.97 & $[0.69,\\; 1.49]$ & ${<}\\,0.001$ \\\\\n0.25 & 3.34 & $[1.66,\\; 6.64]$ & ${<}\\,0.001$ \\\\\n0.30 & 9.85 & $[6.70,\\; 16.29]$ & ${<}\\,0.001$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig4_bootstrap.pdf}\n\\caption{Forest plot of permutation test results. Horizontal bars show 95\\% permutation CIs; diamonds mark observed median differences $\\widetilde{\\Delta}$. All CIs lie entirely above zero, supporting significant strategy-dependent severity at every sparsity level.}\n\\label{fig:permtest-forest}\n\\end{figure}\n\n\n\\section{Cross-Architecture Analysis}\n\\label{app:cross-arch}\n\nTo test whether the phase-modulated severity pattern extends beyond the Qwen2 architecture, we replicate the full experiment on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, 8B parameters; $n{=}250$, MATH-500) under both importance-based and random eviction at $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$. Table~\\ref{tab:llama-cross-arch} reports paired median differences and effect sizes for all 8 conditions.\n\nThe within-importance phase gradient replicates with large effect sizes: $\\Delta$ rises monotonically from $0.050$ ($s{=}0.15$, $d_z{=}0.81$) to $0.695$ ($s{=}0.30$, $d_z{=}1.15$), all $p < 10^{-29}$. An architecture-specific difference emerges in strategy specificity: random eviction on LLaMA also exhibits statistically significant phase gradients at all four sparsity levels ($\\Delta{=}0.025$--$0.271$; $d_z{=}0.41$--$0.46$; all $p < 10^{-12}$), unlike DeepSeek and Qwen where random eviction is non-significant at $s \\leq 0.20$. The importance/random $\\Delta$ ratio on LLaMA is $2.0$--$2.6{\\times}$, substantially weaker than the $15$--$17{\\times}$ observed on DeepSeek.\n\nDose-response monotonicity holds for both strategies across all sparsity levels, supporting the phase gradient as an architecture-general phenomenon. The reduced strategy specificity on LLaMA suggests that GQA's grouped key-value structure partially preserves importance score quality under head pruning, attenuating the discrimination collapse that drives strategy divergence on MHA architectures.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-architecture validation: paired median difference ($\\Delta$) and effect size ($d_z$) on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, $n{=}250$, MATH-500). All conditions are monotonic.}\n\\label{tab:llama-cross-arch}\n\\begin{tabular}{@{}llccc@{}}\n\\toprule\n$s$ & Strategy & $\\Delta$ & $d_z$ & $p$ \\\\\n\\midrule\n0.15 & Importance & $0.050$ & $0.814$ & $1.4 \\times 10^{-29}$ \\\\\n0.15 & Random     & $0.025$ & $0.436$ & $9.3 \\times 10^{-13}$ \\\\\n\\addlinespace\n0.20 & Importance & $0.159$ & $1.010$ & $8.9 \\times 10^{-35}$ \\\\\n0.20 & Random     & $0.065$ & $0.459$ & $3.6 \\times 10^{-15}$ \\\\\n\\addlinespace\n0.25 & Importance & $0.376$ & $1.115$ & $4.3 \\times 10^{-39}$ \\\\\n0.25 & Random     & $0.184$ & $0.424$ & $3.8 \\times 10^{-13}$ \\\\\n\\addlinespace\n0.30 & Importance & $0.695$ & $1.150$ & $1.5 \\times 10^{-40}$ \\\\\n0.30 & Random     & $0.271$ & $0.410$ & $6.0 \\times 10^{-12}$ \\\\\n\\bottomrule\n\\multicolumn{5}{@{}l}{\\footnotesize Imp/Rand $\\Delta$ ratio: $2.0$--$2.6{\\times}$ (cf.\\ $15$--$17{\\times}$ on DeepSeek).}\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Magnitude comparison.}\nLLaMA interaction magnitudes are approximately $7$--$12{\\times}$ smaller than Qwen2-architecture models at matched sparsity. This gap likely reflects differences in attention head specialization between MHA (Qwen2, 28 heads) and GQA (LLaMA, 32 heads with 8 KV groups). The phase gradient direction and dose-response monotonicity replicate, supporting the architecture-generality of phase-modulated compound interaction. Strategy specificity, however, is weaker ($2.0$--$2.6{\\times}$ on LLaMA vs.\\ $15$--$17{\\times}$ on DeepSeek), indicating that the magnitude of strategy${\\times}$phase interaction depends on architectural factors governing importance score stability under pruning.\n\n\n\\section{Analysis: Importance Discrimination Collapse}\n\\label{app:analysis}\n\n\\subsection{Importance Discrimination Collapse}\n\\label{sec:discrimination-collapse}\n\nHead pruning reduces the number of heads contributing to cumulative importance scores, collapsing the score distribution. Table~\\ref{tab:discrimination-metrics-full} quantifies this effect: the Gini coefficient decreases by $0.030$--$0.081$ (DeepSeek) and $0.010$--$0.020$ (Qwen) after pruning, with consistent negative deltas across all 16 conditions (both models $\\times$ 4 sparsity levels $\\times$ 2 strategies). The CV delta is likewise negative in all 8 importance-based conditions. The same pattern holds under random eviction, indicating that importance discrimination collapse is a consequence of head pruning \\emph{per se}, not of the eviction strategy.\n\n\\begin{table}[t]\n\\centering\n\\caption{Importance discrimination collapse under importance-based eviction. $\\Delta\\mathrm{Gini}$ and $\\Delta\\mathrm{CV}$ are post-pruning minus baseline; negative values indicate reduced discriminative power.}\n\\label{tab:discrimination-metrics-full}\n\\small\n\\begin{tabular}{llrr}\n\\toprule\nModel & $s$ & $\\Delta\\mathrm{Gini}$ & $\\Delta\\mathrm{CV}$ \\\\\n\\midrule\nDeepSeek & $0.15$ & $-0.030$ & $-0.56$ \\\\\nDeepSeek & $0.20$ & $-0.040$ & $-0.77$ \\\\\nDeepSeek & $0.25$ & $-0.065$ & $-1.29$ \\\\\nDeepSeek & $0.30$ & $-0.081$ & $-1.66$ \\\\\n\\midrule\nQwen & $0.15$ & $-0.010$ & $-0.05$ \\\\\nQwen & $0.20$ & $-0.012$ & $-0.21$ \\\\\nQwen & $0.25$ & $-0.010$ & $-1.49$ \\\\\nQwen & $0.30$ & $-0.020$ & $-1.14$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWhen importance scores lose discriminability, thresholding degenerates into noise-sensitive selection---functionally approaching biased random eviction. This is phase-dependent: in low-sparsity phases, attention is already broadly distributed, so pruning-induced collapse has maximum impact; in high-sparsity phases, concentration is preserved. Random eviction is immune because its decisions are independent of score quality, consistent with $G \\approx 1$.\n\n\\subsection{Entropy Redistribution}\n\\label{sec:entropy-redistribution}\n\nBeyond importance discrimination collapse, we examine whether head pruning also redistributes the attention entropy of surviving heads. We measure the mean attention entropy per head:\n\\begin{equation}\n    \\mathcal{H}_i^{(h)} = -\\sum_{j=1}^{T} a_{ij}^{(h)} \\log a_{ij}^{(h)}\n    \\label{eq:attn-entropy}\n\\end{equation}\nand compute $\\Delta\\mathcal{H}$ as the change from baseline (no pruning) to the pruned condition.\n\nFor DeepSeek under importance-based eviction, the entropy delta is consistently negative across all four sparsity levels ($\\Delta\\mathcal{H} \\in [-0.047, -0.040]$; Table~\\ref{tab:entropy-deltas}), indicating that importance-based pruning systematically selects heads whose removal concentrates attention in the surviving heads, reinforcing importance discrimination collapse.\n\nFor Qwen, the entropy pattern only partially replicates. The delta is negative at $s{=}0.15$ ($\\Delta\\mathcal{H} = -0.073$) and $s{=}0.20$ ($-0.076$), consistent with DeepSeek. However, at $s{=}0.25$, the delta reverses to $+0.045$, with 22 of 30 problems showing positive entropy change. At $s{=}0.30$, the delta is near zero ($-0.007$). The $s{=}0.25$ reversal is systematic rather than a statistical artifact: it is consistent across all three reasoning phases (low: $+0.042$, mid: $+0.034$, high: $+0.017$). We interpret this as a genuine model-specific difference, possibly arising from distinct head specialization patterns: Qwen's instruction tuning (vs.\\ DeepSeek's distillation-based training) may produce head configurations where removing 25\\% of heads triggers compensatory broadening rather than concentration.\n\nWe characterize importance discrimination collapse as the robust, model-independent driver of the phase-strategy interaction, with entropy redistribution as a secondary amplifier that is consistent in DeepSeek but model-dependent in Qwen.\n\n\\begin{table}[t]\n\\centering\n\\caption{Attention entropy deltas ($\\Delta\\mathcal{H}$) under importance-based eviction. DeepSeek shows consistent entropy compression; Qwen partially replicates with a reversal at $s{=}0.25$.}\n\\label{tab:entropy-deltas}\n\\small\n\\begin{tabular}{llr}\n\\toprule\nModel & $s$ & $\\Delta\\mathcal{H}$ \\\\\n\\midrule\nDeepSeek & $0.15$ & $-0.040$ \\\\\nDeepSeek & $0.20$ & $-0.047$ \\\\\nDeepSeek & $0.25$ & $-0.045$ \\\\\nDeepSeek & $0.30$ & $-0.044$ \\\\\n\\midrule\nQwen & $0.15$ & $-0.073$ \\\\\nQwen & $0.20$ & $-0.076$ \\\\\nQwen & $0.25$ & $+0.045$ \\\\\nQwen & $0.30$ & $-0.007$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
      "numLines": 246,
      "startLine": 1,
      "totalLines": 246
    }
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Read · `toolu_01HxxUAc7jEHqLuVkajcg3dy`</summary>

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
  "session_id": "e127786f-a191-4d01-b58d-071eb9fc50fc",
  "uuid": "0f7809fc-1c01-4f4c-8f16-21d26a4e174d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qs6Zv4TTFooKBHUBayTD8F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10011,
      "cache_read_input_tokens": 31389,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10011
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

_source line 25 · 2026-05-16T22:42:54.044Z_

<details><summary>↩ Tool result · `toolu_01HxxUAc7jEHqLuVkajcg3dy`</summary>

```text
1	\section{Importance Discrimination Collapse Details}
2	\label{app:discrimination-collapse-details}
3	
4	This cross-model consistency (Table~\ref{tab:discrimination-metrics-full}) supports importance discrimination collapse as a robust consequence of compound sparsity. When importance scores lose discriminative power, thresholding the bottom-$s$ fraction becomes noise-sensitive: small perturbations change which positions cross the eviction boundary. In the limit of perfectly uniform scores, importance-based eviction degenerates into an arbitrary selection functionally equivalent to biased random eviction. The same pattern holds under random eviction (DeepSeek: $-0.031$ to $-0.071$; Qwen: $-0.019$ to $-0.046$), indicating that importance discrimination collapse is a consequence of head pruning \emph{per se}, not of the eviction strategy.
5	
6	
7	\section{Extended Discussion}
8	\label{app:extended-discussion}
9	
10	\paragraph{On the predictability of phase-modulated severity.}
11	The compound interaction is not uniformly fragile---it is selectively fragile in a phase-dependent manner ($\widetilde{\mathrm{II}}_{\text{high}} < 0.06$ at $s \leq 0.30$).
12	
13	\paragraph{Random masking as falsification control.}
14	At $n{=}500$, random eviction develops a detectable but weak phase gradient above $s \approx 0.20$: non-significant at $s \leq 0.20$ for both models, but significant at $s \geq 0.25$ (DS: $\Delta{=}0.26$--$0.51$, $p_{\text{Bonf}} < 0.006$; QW: $\Delta{=}0.39$--$0.91$, $p_{\text{Bonf}} < 10^{-10}$). Where significant, the random phase gradient is $2.7$--$17{\times}$ weaker than importance-based (restricted to conditions where both strategies are significant, $s \geq 0.25$), supporting that the dominant amplification is strategy-specific.
15	
16	\paragraph{Entropy mechanism boundary conditions.}
17	Directly measuring per-head entropy shifts across architecturally distinct models---and identifying what training-time properties determine whether entropy concentrates or disperses under head pruning---would clarify the boundary conditions of the full mechanism.
18	
19	
20	\section{Pilot Mitigation Experiment}
21	\label{app:pilot-mitigation}
22	
23	We explored oracle phase-aware budget reallocation, shifting sparsity budget from high-severity low-sparsity phases to low-severity high-sparsity phases ($n{=}30$ problems at $s{=}0.25$). Oracle recovery---the fraction of compound interaction eliminated by phase-aware allocation---reached 18\% (95\% CI: $[-39\%, 45.8\%]$; Wilcoxon $p = 0.002$), below the pre-registered 30\% gate for claiming practical mitigation. A heuristic variant achieved 32\% recovery (95\% CI: $[-22.8\%, 66\%]$; $p = 0.024$). \textbf{Critically, 95\% bootstrap CIs for both conditions span zero}, meaning neither recovery estimate is statistically distinguishable from no improvement. \textbf{Gate status: FAIL}---neither oracle nor heuristic recovery meets the pre-registered threshold, and neither is statistically distinguishable from zero improvement. These results indicate that phase-aware budget reallocation alone is insufficient to neutralize the severity gradient; effective mitigation likely requires joint optimization of budget allocation and eviction strategy selection across phases.
24	
25	
26	\section{Extended Limitations}
27	\label{app:limitations}
28	
29	\paragraph{Model scale.}
30	All experiments are conducted at the 7B parameter scale.
31	Whether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested.
32	Larger models may exhibit different attention redundancy structures that alter the importance discrimination collapse dynamics (and the model-dependent entropy component may behave differently at scale).
33	
34	
35	\paragraph{Architectural scope.}
36	Our two models---DeepSeek-R1-Distill-Qwen-7B and Qwen2.5-7B-Instruct---share the Qwen2ForCausalLM architecture.
37	The cross-training-paradigm replication (\S\ref{sec:cross-model}) suggests that the findings are not artifacts of a single model's weights, though both models share the same Qwen2ForCausalLM architecture.
38	Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, $n{=}250$, \S\ref{sec:cross-arch}, Appendix~\ref{app:cross-arch}) confirms qualitatively consistent within-importance phase gradients ($d_z{=}0.81$--$1.15$; all $p < 10^{-29}$) but a substantially weaker strategy${\times}$phase interaction than in Qwen2-based architectures: random eviction also exhibits significant phase gradients on LLaMA ($d_z{=}0.41$--$0.46$; all $p < 10^{-12}$), reducing the importance/random ratio to $2.0$--$2.6{\times}$ (vs.\ $15$--$17{\times}$ on DeepSeek). The phase gradient direction and dose-response monotonicity are architecture-general; quantitative strategy specificity is architecture-dependent. Comprehensive cross-architecture validation across more diverse designs (e.g., Mistral, multi-latent attention architectures) and scales remains an important next step.
39	
40	
41	\paragraph{Task coverage.}
42	We evaluate exclusively on MATH-500, a mathematical reasoning benchmark.
43	Different reasoning tasks---code generation, commonsense reasoning, multi-hop question answering---may induce different phase structures with different sparsity distributions, potentially altering the severity gradient profile.
44	Generalizing the phase-strategy interaction to broader reasoning domains is an important next step.
45	
46	
47	\paragraph{Statistical scope.}
48	Bootstrap confidence intervals use $B{=}10{,}000$ resamples (seed$=$42). The primary analysis uses $n{=}496$ paired problems for DeepSeek (4 excluded) and $n{=}475$ for Qwen (25 excluded); the permutation test (Table~\ref{tab:permutation}) uses $n{=}49$ from an initial profiling subset.
49	The severity difference distribution is right-skewed (mean/median ratios up to $43{:}1$), motivating our use of medians and nonparametric tests rather than parametric alternatives.
50	All four profiling-subset permutation tests reject $H_0$ after Bonferroni correction ($p_{\text{Bonf}} < 0.005$; Table~\ref{tab:permutation}), with CI lower bounds increasing from $0.19$ to $6.70$---supporting the effect direction at every sparsity level. At $n{=}496$, Wilcoxon signed-rank tests support all conditions with $p_{\text{Bonf}} < 10^{-13}$ (Table~\ref{tab:cohens-d}). The permutation CIs at higher sparsity are wider (e.g., $[6.70,\; 16.29]$ at $s{=}0.30$), reflecting genuine variance in per-problem severity amplification.
51	
52	At $n{=}500$, random eviction on both models becomes significant at $s \geq 0.25$ (Qwen: $\Delta{=}0.39$, $p_{\text{Bonf}} < 10^{-10}$ at $s{=}0.25$; $\Delta{=}0.91$, $p_{\text{Bonf}} < 10^{-13}$ at $s{=}0.30$; bootstrap CIs exclude zero).
53	These effects are genuine but $2.7$--$20{\times}$ weaker than importance-based eviction at the same sparsity levels, consistent with a weak phase gradient that is detectable at sufficient sample size but not the primary driver of compound severity.
54	
55	\paragraph{Sparsity range.}
56	Our primary analysis spans $s \in \{0.15, 0.20, 0.25, 0.30\}$; pilot data at $s{=}0.10$ and $s{=}0.35$ exist (6 total sparsity levels) but are not included in the main analysis due to limited sample size at these boundary conditions. Monotonicity is established at the tested sparsity levels (JT test $p \ll 10^{-10}$); the functional form of $G(s)$ between and beyond these levels is not characterized.
57	More extreme sparsity ($s > 0.50$) may exhibit qualitatively different interaction dynamics---the sub-exponential growth pattern suggests the severity gradient may plateau, but this remains unverified.
58	
59	
60	\paragraph{No throughput evaluation.}
61	We do not report inference throughput or latency, which are necessary for deployment analysis but orthogonal to our severity characterization.
62	
63	
64	
65	\section{Cross-Benchmark Validation: GSM8K}
66	\label{app:gsm8k}
67	
68	Tables~\ref{tab:gsm8k-ds} and \ref{tab:gsm8k-qw} report the per-phase II breakdown on GSM8K ($n{=}50$) for DeepSeek and Qwen, respectively. All statistics use medians, Wilcoxon signed-rank tests, and bootstrap median CIs ($B{=}10{,}000$), matching the MATH-500 methodology. DeepSeek importance-based eviction replicates the MATH-500 phase gradient across all four sparsity levels (all $p \leq 0.0003$) with a strict dose-response ($\Delta$: $0.24 \to 4.68$). Qwen importance-based eviction is significant at $s \geq 0.25$ ($p < 10^{-4}$). Random eviction is non-significant across all conditions for both models; Qwen random $s{=}0.30$ is excluded due to data quality concerns (output truncation producing extreme II values).
69	
70	\paragraph{Power analysis for random conditions.}
71	Post-hoc power analysis indicates that at $n{=}50$, the minimum detectable effect size is $d \geq 0.40$ ($\alpha{=}0.05$, power${=}0.80$). All 8 random conditions (2 models $\times$ 4 sparsity levels) show $|d| \leq 0.164$, well below the detectability threshold; their non-significance should therefore be interpreted as absence of evidence rather than evidence of absence. By contrast, Qwen importance-based eviction at $s \geq 0.25$ is adequately powered ($d \approx 0.63$, power ${>}\,0.99$), indicating that the observed significance reflects a genuine effect.
72	
73	\begin{table*}[t]
74	\centering
75	\small
76	\caption{Per-phase interaction index on GSM8K: DeepSeek-R1-Distill-Qwen-7B ($n{=}50$). $\Delta$: paired median difference ($\widetilde{\mathrm{II}}_{\textit{low}} - \widetilde{\mathrm{II}}_{\textit{high}}$) with bootstrap 95\% CI ($B{=}10{,}000$, median statistic). $p$: Wilcoxon signed-rank, Bonferroni-corrected ($k{=}4$).}
77	\label{tab:gsm8k-ds}
78	\begin{tabular}{@{}llcccc@{}}
79	\toprule
80	$s$ & Strategy & $\widetilde{\mathrm{II}}_{\textit{high}}$ & $\widetilde{\mathrm{II}}_{\textit{low}}$ & $\Delta$\; [95\% CI] & $p_{\text{Bonf}}$ \\
81	\midrule
82	0.15 & Importance & $-$0.001 & 0.241 & 0.24\; $[0.08,\; 0.48]$ & 0.0003 \\
83	0.15 & Random     & 0.036 & 0.105 & $-$0.04\textsuperscript{ns} & 0.90 \\
84	\addlinespace
85	0.20 & Importance & $-$0.002 & 0.740 & 0.74\; $[0.31,\; 1.12]$ & ${<}\,10^{-4}$ \\
86	0.20 & Random     & 0.143 & 0.423 & 0.28\textsuperscript{ns} & 0.96 \\
87	\addlinespace
88	0.25 & Importance & 0.009 & 1.992 & 1.99\; $[0.93,\; 2.82]$ & ${<}\,10^{-4}$ \\
89	0.25 & Random     & 0.619 & 1.603 & 0.98\textsuperscript{ns} & 0.83 \\
90	\addlinespace
91	0.30 & Importance & 0.024 & 4.682 & 4.68\; $[2.12,\; 10.56]$ & ${<}\,10^{-4}$ \\
92	0.30 & Random     & 1.837 & 4.683 & 2.85\textsuperscript{ns} & 0.54 \\
93	\bottomrule
94	\end{tabular}
95	\end{table*}
96	
97	\begin{table*}[t]
98	\centering
99	\small
100	\caption{Per-phase interaction index on GSM8K: Qwen2.5-7B-Instruct ($n{=}50$). Outputs truncated at \texttt{max\_new\_tokens}${=}$2047; absolute values should be interpreted with this limitation. $^{\ddagger}$Excluded: extreme II values from truncation artifacts render this condition invalid.}
101	\label{tab:gsm8k-qw}
102	\begin{tabular}{@{}llcccc@{}}
103	\toprule
104	$s$ & Strategy & $\widetilde{\mathrm{II}}_{\textit{high}}$ & $\widetilde{\mathrm{II}}_{\textit{low}}$ & $\Delta$\; [95\% CI] & $p_{\text{Bonf}}$ \\
105	\midrule
106	0.15 & Importance & 0.000 & 0.029 & 0.03\textsuperscript{ns} & 0.39 \\
107	0.15 & Random     & 0.089 & 0.033 & $-$1.58\textsuperscript{ns} & 0.69 \\
108	\addlinespace
109	0.20 & Importance & 0.004 & 0.180 & 0.09\textsuperscript{ns} & 0.62 \\
110	0.20 & Random     & 0.201 & 0.356 & 4.88\textsuperscript{ns} & 0.57 \\
111	\addlinespace
112	0.25 & Importance & 0.009 & 1.064 & 1.14\; $[0.62,\; 1.66]$ & ${<}\,10^{-4}$ \\
113	0.25 & Random     & 0.802 & 1.213 & 11.1\textsuperscript{ns} & 0.39 \\
114	\addlinespace
115	0.30 & Importance & 0.023 & 2.140 & 4.62\; $[2.88,\; 6.92]$ & ${<}\,10^{-4}$ \\
116	0.30 & Random$^{\ddagger}$     & \multicolumn{4}{c}{\textit{excluded (data quality)}} \\
117	\bottomrule
118	\end{tabular}
119	\end{table*}
120	
121	
122	\section{Downstream Accuracy Validation Details}
123	\label{app:accuracy-details}
124	
125	Table~\ref{tab:accuracy} reports MATH-500 accuracy under compound sparsity (importance-based eviction) at $s \in \{0.15, 0.20, 0.25, 0.30\}$ with \texttt{max\_new\_tokens}${=}$8192, complementing the PPL-based analysis in \S\ref{sec:accuracy-validation}. Qwen ($n{=}100$; truncation $\leq 4\%$ across all conditions) provides the cleanest dose-response evidence: accuracy declines gradually from $46\%$ (dense) through $s{=}0.25$ ($\delta{=}-4$ to $-13$\,pp) before a sharp cliff at $s{=}0.30$ ($19\%$, $\delta{=}-27$\,pp). DeepSeek ($n{=}50$) shows steeper overall degradation ($74\% \to 4\%$), confounded by rising truncation ($16\% \to 76\%$); non-truncated analysis (\S\ref{app:accuracy-nt}) reveals a dual-regime structure.
126	
127	\begin{table}[h]
128	\centering
129	\small
130	\caption{MATH-500 accuracy under compound sparsity (importance-based eviction, \texttt{max\_new\_tokens}${=}$8192). $\delta$: accuracy change vs.\ dense. Trunc: truncation rate under sparse condition. DS: $n{=}50$ (dense truncation $16\%$); QW: $n{=}100$ (truncation $\leq 4\%$ all conditions).}
131	\label{tab:accuracy}
132	\begin{tabular}{@{}lccccc@{}}
133	\toprule
134	Model & $s$ & Dense & Sparse & $\delta$ & Trunc \\
135	\midrule
136	DS & 0.15 & 74\% & 48\% & $-$26\,pp & 32\% \\
137	DS & 0.20 & 74\% & 30\% & $-$44\,pp & 56\% \\
138	DS & 0.25 & 74\% & 8\% & $-$66\,pp & 76\% \\
139	DS & 0.30 & 74\% & 4\% & $-$70\,pp & 76\% \\
140	\addlinespace
141	QW & 0.15 & 46\% & 42\% & $-$4\,pp & $\leq$4\% \\
142	QW & 0.20 & 46\% & 36\% & $-$10\,pp & $\leq$4\% \\
143	QW & 0.25 & 46\% & 33\% & $-$13\,pp & $\leq$4\% \\
144	QW & 0.30 & 46\% & 19\% & $-$27\,pp & $\leq$4\% \\
145	\bottomrule
146	\end{tabular}
147	\end{table}
148	
149	\paragraph{Failure mode divergence.}
150	DeepSeek and Qwen exhibit qualitatively distinct failure modes under compound sparsity. DeepSeek failures are \emph{truncation-dominated}: compound sparsity is associated with verbose, repetitive chain-of-thought that exceeds the token limit (truncation rises from $16\%$ at dense to $32\%$ at $s{=}0.15$ and $76\%$ at $s{=}0.30$, even with \texttt{max\_new\_tokens}${=}$8192). Qwen failures are \emph{wrong-answer-dominated}: outputs complete within the token limit (truncation $\leq 4\%$) but produce incorrect answers, indicating that compound sparsity disrupts reasoning quality directly. This divergence likely reflects training-paradigm differences: DeepSeek's distillation from DeepSeek-R1 produces extended CoT traces susceptible to truncation under degraded conditions.
151	
152	\paragraph{Language switching under high sparsity.}
153	DeepSeek problems exhibit language switching to Chinese mid-generation at the following observed rates: 0\% at dense, 4\% at $s{=}0.15$, and 40\% at $s{=}0.30$ (intermediate sparsity levels not yet measured).\footnote{Language switching rates were detected from \texttt{gen\_snippet} fields in 2048-token evaluations, not from the independent 8192-token generations used in Table~\ref{tab:accuracy}. Rates under the 8192-token budget were not re-measured.} This qualitative pathology---absent in Qwen---is a \emph{symptom} of compound-sparsity-induced degradation rather than a cause of accuracy loss: at $s{=}0.30$, Chinese-language and English-language outputs achieve comparable accuracy ($\sim$10\%), indicating that the accuracy decline reflects pruning-induced reasoning corruption regardless of output language. The switching pattern is consistent with the model's Chinese-language pretraining corpus surfacing under degraded attention in distillation-trained models.
154	
155	
156	\section{Non-Truncated Sensitivity Analysis}
157	\label{app:accuracy-nt}
158	
159	With \texttt{max\_new\_tokens}${=}$8192, Qwen truncation remains $\leq 4\%$ across all sparsity levels, so the full-sample accuracy decline ($\delta{=}-4$ to $-27$\,pp; Table~\ref{tab:accuracy}) reflects pure reasoning quality degradation without truncation confound.
160	
161	DeepSeek exhibits substantial truncation ($16\%$ at dense to $76\%$ at $s{=}0.25$--$0.30$). Restricting to non-truncated outputs reveals a \emph{dual-regime} structure. At $s \leq 0.20$, non-truncated accuracy remains $68$--$71\%$ (vs.\ $88\%$ dense; $n_{\text{NT}}{=}34$ at $s{=}0.15$, $n_{\text{NT}}{=}22$ at $s{=}0.20$), while full-sample accuracy drops to $30$--$48\%$---indicating that degradation at low sparsity is primarily truncation-driven rather than reflecting reasoning quality loss. At $s \geq 0.25$, non-truncated accuracy itself collapses: $33\%$ at $s{=}0.25$ and $17\%$ at $s{=}0.30$ ($n_{\text{NT}}{=}12$ for both; reported as reference values given small samples), showing that high-dose compound sparsity degrades both generation length \emph{and} reasoning quality simultaneously. The NT accuracy cliff from $68\%$ ($s{=}0.20$) to $33\%$ ($s{=}0.25$) localizes the transition between truncation-driven and dual-collapse regimes.
162	
163	This dual-regime structure complements the importance discrimination collapse analysis (\S\ref{sec:analysis}): at low sparsity, compound interaction primarily manifests as increased verbosity (degraded attention produces repetitive CoT); at high sparsity, the interaction additionally corrupts reasoning-critical computations.
164	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e127786f-a191-4d01-b58d-071eb9fc50fc",
  "uuid": "3b91cf35-182b-4216-bfb8-5b752a983144",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex",
      "content": "\\section{Importance Discrimination Collapse Details}\n\\label{app:discrimination-collapse-details}\n\nThis cross-model consistency (Table~\\ref{tab:discrimination-metrics-full}) supports importance discrimination collapse as a robust consequence of compound sparsity. When importance scores lose discriminative power, thresholding the bottom-$s$ fraction becomes noise-sensitive: small perturbations change which positions cross the eviction boundary. In the limit of perfectly uniform scores, importance-based eviction degenerates into an arbitrary selection functionally equivalent to biased random eviction. The same pattern holds under random eviction (DeepSeek: $-0.031$ to $-0.071$; Qwen: $-0.019$ to $-0.046$), indicating that importance discrimination collapse is a consequence of head pruning \\emph{per se}, not of the eviction strategy.\n\n\n\\section{Extended Discussion}\n\\label{app:extended-discussion}\n\n\\paragraph{On the predictability of phase-modulated severity.}\nThe compound interaction is not uniformly fragile---it is selectively fragile in a phase-dependent manner ($\\widetilde{\\mathrm{II}}_{\\text{high}} < 0.06$ at $s \\leq 0.30$).\n\n\\paragraph{Random masking as falsification control.}\nAt $n{=}500$, random eviction develops a detectable but weak phase gradient above $s \\approx 0.20$: non-significant at $s \\leq 0.20$ for both models, but significant at $s \\geq 0.25$ (DS: $\\Delta{=}0.26$--$0.51$, $p_{\\text{Bonf}} < 0.006$; QW: $\\Delta{=}0.39$--$0.91$, $p_{\\text{Bonf}} < 10^{-10}$). Where significant, the random phase gradient is $2.7$--$17{\\times}$ weaker than importance-based (restricted to conditions where both strategies are significant, $s \\geq 0.25$), supporting that the dominant amplification is strategy-specific.\n\n\\paragraph{Entropy mechanism boundary conditions.}\nDirectly measuring per-head entropy shifts across architecturally distinct models---and identifying what training-time properties determine whether entropy concentrates or disperses under head pruning---would clarify the boundary conditions of the full mechanism.\n\n\n\\section{Pilot Mitigation Experiment}\n\\label{app:pilot-mitigation}\n\nWe explored oracle phase-aware budget reallocation, shifting sparsity budget from high-severity low-sparsity phases to low-severity high-sparsity phases ($n{=}30$ problems at $s{=}0.25$). Oracle recovery---the fraction of compound interaction eliminated by phase-aware allocation---reached 18\\% (95\\% CI: $[-39\\%, 45.8\\%]$; Wilcoxon $p = 0.002$), below the pre-registered 30\\% gate for claiming practical mitigation. A heuristic variant achieved 32\\% recovery (95\\% CI: $[-22.8\\%, 66\\%]$; $p = 0.024$). \\textbf{Critically, 95\\% bootstrap CIs for both conditions span zero}, meaning neither recovery estimate is statistically distinguishable from no improvement. \\textbf{Gate status: FAIL}---neither oracle nor heuristic recovery meets the pre-registered threshold, and neither is statistically distinguishable from zero improvement. These results indicate that phase-aware budget reallocation alone is insufficient to neutralize the severity gradient; effective mitigation likely requires joint optimization of budget allocation and eviction strategy selection across phases.\n\n\n\\section{Extended Limitations}\n\\label{app:limitations}\n\n\\paragraph{Model scale.}\nAll experiments are conducted at the 7B parameter scale.\nWhether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested.\nLarger models may exhibit different attention redundancy structures that alter the importance discrimination collapse dynamics (and the model-dependent entropy component may behave differently at scale).\n\n\n\\paragraph{Architectural scope.}\nOur two models---DeepSeek-R1-Distill-Qwen-7B and Qwen2.5-7B-Instruct---share the Qwen2ForCausalLM architecture.\nThe cross-training-paradigm replication (\\S\\ref{sec:cross-model}) suggests that the findings are not artifacts of a single model's weights, though both models share the same Qwen2ForCausalLM architecture.\nCross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, $n{=}250$, \\S\\ref{sec:cross-arch}, Appendix~\\ref{app:cross-arch}) confirms qualitatively consistent within-importance phase gradients ($d_z{=}0.81$--$1.15$; all $p < 10^{-29}$) but a substantially weaker strategy${\\times}$phase interaction than in Qwen2-based architectures: random eviction also exhibits significant phase gradients on LLaMA ($d_z{=}0.41$--$0.46$; all $p < 10^{-12}$), reducing the importance/random ratio to $2.0$--$2.6{\\times}$ (vs.\\ $15$--$17{\\times}$ on DeepSeek). The phase gradient direction and dose-response monotonicity are architecture-general; quantitative strategy specificity is architecture-dependent. Comprehensive cross-architecture validation across more diverse designs (e.g., Mistral, multi-latent attention architectures) and scales remains an important next step.\n\n\n\\paragraph{Task coverage.}\nWe evaluate exclusively on MATH-500, a mathematical reasoning benchmark.\nDifferent reasoning tasks---code generation, commonsense reasoning, multi-hop question answering---may induce different phase structures with different sparsity distributions, potentially altering the severity gradient profile.\nGeneralizing the phase-strategy interaction to broader reasoning domains is an important next step.\n\n\n\\paragraph{Statistical scope.}\nBootstrap confidence intervals use $B{=}10{,}000$ resamples (seed$=$42). The primary analysis uses $n{=}496$ paired problems for DeepSeek (4 excluded) and $n{=}475$ for Qwen (25 excluded); the permutation test (Table~\\ref{tab:permutation}) uses $n{=}49$ from an initial profiling subset.\nThe severity difference distribution is right-skewed (mean/median ratios up to $43{:}1$), motivating our use of medians and nonparametric tests rather than parametric alternatives.\nAll four profiling-subset permutation tests reject $H_0$ after Bonferroni correction ($p_{\\text{Bonf}} < 0.005$; Table~\\ref{tab:permutation}), with CI lower bounds increasing from $0.19$ to $6.70$---supporting the effect direction at every sparsity level. At $n{=}496$, Wilcoxon signed-rank tests support all conditions with $p_{\\text{Bonf}} < 10^{-13}$ (Table~\\ref{tab:cohens-d}). The permutation CIs at higher sparsity are wider (e.g., $[6.70,\\; 16.29]$ at $s{=}0.30$), reflecting genuine variance in per-problem severity amplification.\n\nAt $n{=}500$, random eviction on both models becomes significant at $s \\geq 0.25$ (Qwen: $\\Delta{=}0.39$, $p_{\\text{Bonf}} < 10^{-10}$ at $s{=}0.25$; $\\Delta{=}0.91$, $p_{\\text{Bonf}} < 10^{-13}$ at $s{=}0.30$; bootstrap CIs exclude zero).\nThese effects are genuine but $2.7$--$20{\\times}$ weaker than importance-based eviction at the same sparsity levels, consistent with a weak phase gradient that is detectable at sufficient sample size but not the primary driver of compound severity.\n\n\\paragraph{Sparsity range.}\nOur primary analysis spans $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$; pilot data at $s{=}0.10$ and $s{=}0.35$ exist (6 total sparsity levels) but are not included in the main analysis due to limited sample size at these boundary conditions. Monotonicity is established at the tested sparsity levels (JT test $p \\ll 10^{-10}$); the functional form of $G(s)$ between and beyond these levels is not characterized.\nMore extreme sparsity ($s > 0.50$) may exhibit qualitatively different interaction dynamics---the sub-exponential growth pattern suggests the severity gradient may plateau, but this remains unverified.\n\n\n\\paragraph{No throughput evaluation.}\nWe do not report inference throughput or latency, which are necessary for deployment analysis but orthogonal to our severity characterization.\n\n\n\n\\section{Cross-Benchmark Validation: GSM8K}\n\\label{app:gsm8k}\n\nTables~\\ref{tab:gsm8k-ds} and \\ref{tab:gsm8k-qw} report the per-phase II breakdown on GSM8K ($n{=}50$) for DeepSeek and Qwen, respectively. All statistics use medians, Wilcoxon signed-rank tests, and bootstrap median CIs ($B{=}10{,}000$), matching the MATH-500 methodology. DeepSeek importance-based eviction replicates the MATH-500 phase gradient across all four sparsity levels (all $p \\leq 0.0003$) with a strict dose-response ($\\Delta$: $0.24 \\to 4.68$). Qwen importance-based eviction is significant at $s \\geq 0.25$ ($p < 10^{-4}$). Random eviction is non-significant across all conditions for both models; Qwen random $s{=}0.30$ is excluded due to data quality concerns (output truncation producing extreme II values).\n\n\\paragraph{Power analysis for random conditions.}\nPost-hoc power analysis indicates that at $n{=}50$, the minimum detectable effect size is $d \\geq 0.40$ ($\\alpha{=}0.05$, power${=}0.80$). All 8 random conditions (2 models $\\times$ 4 sparsity levels) show $|d| \\leq 0.164$, well below the detectability threshold; their non-significance should therefore be interpreted as absence of evidence rather than evidence of absence. By contrast, Qwen importance-based eviction at $s \\geq 0.25$ is adequately powered ($d \\approx 0.63$, power ${>}\\,0.99$), indicating that the observed significance reflects a genuine effect.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Per-phase interaction index on GSM8K: DeepSeek-R1-Distill-Qwen-7B ($n{=}50$). $\\Delta$: paired median difference ($\\widetilde{\\mathrm{II}}_{\\textit{low}} - \\widetilde{\\mathrm{II}}_{\\textit{high}}$) with bootstrap 95\\% CI ($B{=}10{,}000$, median statistic). $p$: Wilcoxon signed-rank, Bonferroni-corrected ($k{=}4$).}\n\\label{tab:gsm8k-ds}\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\n$s$ & Strategy & $\\widetilde{\\mathrm{II}}_{\\textit{high}}$ & $\\widetilde{\\mathrm{II}}_{\\textit{low}}$ & $\\Delta$\\; [95\\% CI] & $p_{\\text{Bonf}}$ \\\\\n\\midrule\n0.15 & Importance & $-$0.001 & 0.241 & 0.24\\; $[0.08,\\; 0.48]$ & 0.0003 \\\\\n0.15 & Random     & 0.036 & 0.105 & $-$0.04\\textsuperscript{ns} & 0.90 \\\\\n\\addlinespace\n0.20 & Importance & $-$0.002 & 0.740 & 0.74\\; $[0.31,\\; 1.12]$ & ${<}\\,10^{-4}$ \\\\\n0.20 & Random     & 0.143 & 0.423 & 0.28\\textsuperscript{ns} & 0.96 \\\\\n\\addlinespace\n0.25 & Importance & 0.009 & 1.992 & 1.99\\; $[0.93,\\; 2.82]$ & ${<}\\,10^{-4}$ \\\\\n0.25 & Random     & 0.619 & 1.603 & 0.98\\textsuperscript{ns} & 0.83 \\\\\n\\addlinespace\n0.30 & Importance & 0.024 & 4.682 & 4.68\\; $[2.12,\\; 10.56]$ & ${<}\\,10^{-4}$ \\\\\n0.30 & Random     & 1.837 & 4.683 & 2.85\\textsuperscript{ns} & 0.54 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Per-phase interaction index on GSM8K: Qwen2.5-7B-Instruct ($n{=}50$). Outputs truncated at \\texttt{max\\_new\\_tokens}${=}$2047; absolute values should be interpreted with this limitation. $^{\\ddagger}$Excluded: extreme II values from truncation artifacts render this condition invalid.}\n\\label{tab:gsm8k-qw}\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\n$s$ & Strategy & $\\widetilde{\\mathrm{II}}_{\\textit{high}}$ & $\\widetilde{\\mathrm{II}}_{\\textit{low}}$ & $\\Delta$\\; [95\\% CI] & $p_{\\text{Bonf}}$ \\\\\n\\midrule\n0.15 & Importance & 0.000 & 0.029 & 0.03\\textsuperscript{ns} & 0.39 \\\\\n0.15 & Random     & 0.089 & 0.033 & $-$1.58\\textsuperscript{ns} & 0.69 \\\\\n\\addlinespace\n0.20 & Importance & 0.004 & 0.180 & 0.09\\textsuperscript{ns} & 0.62 \\\\\n0.20 & Random     & 0.201 & 0.356 & 4.88\\textsuperscript{ns} & 0.57 \\\\\n\\addlinespace\n0.25 & Importance & 0.009 & 1.064 & 1.14\\; $[0.62,\\; 1.66]$ & ${<}\\,10^{-4}$ \\\\\n0.25 & Random     & 0.802 & 1.213 & 11.1\\textsuperscript{ns} & 0.39 \\\\\n\\addlinespace\n0.30 & Importance & 0.023 & 2.140 & 4.62\\; $[2.88,\\; 6.92]$ & ${<}\\,10^{-4}$ \\\\\n0.30 & Random$^{\\ddagger}$     & \\multicolumn{4}{c}{\\textit{excluded (data quality)}} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\n\\section{Downstream Accuracy Validation Details}\n\\label{app:accuracy-details}\n\nTable~\\ref{tab:accuracy} reports MATH-500 accuracy under compound sparsity (importance-based eviction) at $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$ with \\texttt{max\\_new\\_tokens}${=}$8192, complementing the PPL-based analysis in \\S\\ref{sec:accuracy-validation}. Qwen ($n{=}100$; truncation $\\leq 4\\%$ across all conditions) provides the cleanest dose-response evidence: accuracy declines gradually from $46\\%$ (dense) through $s{=}0.25$ ($\\delta{=}-4$ to $-13$\\,pp) before a sharp cliff at $s{=}0.30$ ($19\\%$, $\\delta{=}-27$\\,pp). DeepSeek ($n{=}50$) shows steeper overall degradation ($74\\% \\to 4\\%$), confounded by rising truncation ($16\\% \\to 76\\%$); non-truncated analysis (\\S\\ref{app:accuracy-nt}) reveals a dual-regime structure.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{MATH-500 accuracy under compound sparsity (importance-based eviction, \\texttt{max\\_new\\_tokens}${=}$8192). $\\delta$: accuracy change vs.\\ dense. Trunc: truncation rate under sparse condition. DS: $n{=}50$ (dense truncation $16\\%$); QW: $n{=}100$ (truncation $\\leq 4\\%$ all conditions).}\n\\label{tab:accuracy}\n\\begin{tabular}{@{}lccccc@{}}\n\\toprule\nModel & $s$ & Dense & Sparse & $\\delta$ & Trunc \\\\\n\\midrule\nDS & 0.15 & 74\\% & 48\\% & $-$26\\,pp & 32\\% \\\\\nDS & 0.20 & 74\\% & 30\\% & $-$44\\,pp & 56\\% \\\\\nDS & 0.25 & 74\\% & 8\\% & $-$66\\,pp & 76\\% \\\\\nDS & 0.30 & 74\\% & 4\\% & $-$70\\,pp & 76\\% \\\\\n\\addlinespace\nQW & 0.15 & 46\\% & 42\\% & $-$4\\,pp & $\\leq$4\\% \\\\\nQW & 0.20 & 46\\% & 36\\% & $-$10\\,pp & $\\leq$4\\% \\\\\nQW & 0.25 & 46\\% & 33\\% & $-$13\\,pp & $\\leq$4\\% \\\\\nQW & 0.30 & 46\\% & 19\\% & $-$27\\,pp & $\\leq$4\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Failure mode divergence.}\nDeepSeek and Qwen exhibit qualitatively distinct failure modes under compound sparsity. DeepSeek failures are \\emph{truncation-dominated}: compound sparsity is associated with verbose, repetitive chain-of-thought that exceeds the token limit (truncation rises from $16\\%$ at dense to $32\\%$ at $s{=}0.15$ and $76\\%$ at $s{=}0.30$, even with \\texttt{max\\_new\\_tokens}${=}$8192). Qwen failures are \\emph{wrong-answer-dominated}: outputs complete within the token limit (truncation $\\leq 4\\%$) but produce incorrect answers, indicating that compound sparsity disrupts reasoning quality directly. This divergence likely reflects training-paradigm differences: DeepSeek's distillation from DeepSeek-R1 produces extended CoT traces susceptible to truncation under degraded conditions.\n\n\\paragraph{Language switching under high sparsity.}\nDeepSeek problems exhibit language switching to Chinese mid-generation at the following observed rates: 0\\% at dense, 4\\% at $s{=}0.15$, and 40\\% at $s{=}0.30$ (intermediate sparsity levels not yet measured).\\footnote{Language switching rates were detected from \\texttt{gen\\_snippet} fields in 2048-token evaluations, not from the independent 8192-token generations used in Table~\\ref{tab:accuracy}. Rates under the 8192-token budget were not re-measured.} This qualitative pathology---absent in Qwen---is a \\emph{symptom} of compound-sparsity-induced degradation rather than a cause of accuracy loss: at $s{=}0.30$, Chinese-language and English-language outputs achieve comparable accuracy ($\\sim$10\\%), indicating that the accuracy decline reflects pruning-induced reasoning corruption regardless of output language. The switching pattern is consistent with the model's Chinese-language pretraining corpus surfacing under degraded attention in distillation-trained models.\n\n\n\\section{Non-Truncated Sensitivity Analysis}\n\\label{app:accuracy-nt}\n\nWith \\texttt{max\\_new\\_tokens}${=}$8192, Qwen truncation remains $\\leq 4\\%$ across all sparsity levels, so the full-sample accuracy decline ($\\delta{=}-4$ to $-27$\\,pp; Table~\\ref{tab:accuracy}) reflects pure reasoning quality degradation without truncation confound.\n\nDeepSeek exhibits substantial truncation ($16\\%$ at dense to $76\\%$ at $s{=}0.25$--$0.30$). Restricting to non-truncated outputs reveals a \\emph{dual-regime} structure. At $s \\leq 0.20$, non-truncated accuracy remains $68$--$71\\%$ (vs.\\ $88\\%$ dense; $n_{\\text{NT}}{=}34$ at $s{=}0.15$, $n_{\\text{NT}}{=}22$ at $s{=}0.20$), while full-sample accuracy drops to $30$--$48\\%$---indicating that degradation at low sparsity is primarily truncation-driven rather than reflecting reasoning quality loss. At $s \\geq 0.25$, non-truncated accuracy itself collapses: $33\\%$ at $s{=}0.25$ and $17\\%$ at $s{=}0.30$ ($n_{\\text{NT}}{=}12$ for both; reported as reference values given small samples), showing that high-dose compound sparsity degrades both generation length \\emph{and} reasoning quality simultaneously. The NT accuracy cliff from $68\\%$ ($s{=}0.20$) to $33\\%$ ($s{=}0.25$) localizes the transition between truncation-driven and dual-collapse regimes.\n\nThis dual-regime structure complements the importance discrimination collapse analysis (\\S\\ref{sec:analysis}): at low sparsity, compound interaction primarily manifests as increased verbosity (degraded attention produces repetitive CoT); at high sparsity, the interaction additionally corrupts reasoning-critical computations.\n",
      "numLines": 164,
      "startLine": 1,
      "totalLines": 164
    }
  }
}
```

</details>

---

### Assistant

_source line 26_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the discussion.tex and the analysis.tex files to check for consistency as well.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e127786f-a191-4d01-b58d-071eb9fc50fc",
  "uuid": "56542203-082c-4577-a630-35ad33bede82",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014uESCXxE7yDP7dMksL6NCg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14395,
      "cache_read_input_tokens": 41400,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14395
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

Let me also read the discussion and analysis sections.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e127786f-a191-4d01-b58d-071eb9fc50fc",
  "uuid": "1dfef8ec-92b3-43b0-9d4a-0fda45989c96",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014uESCXxE7yDP7dMksL6NCg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14395,
      "cache_read_input_tokens": 41400,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14395
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

<details open><summary>🔧 Tool call — Read · `toolu_01CKjwF1BFu33GVcJL7Vcmc8`</summary>

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
  "session_id": "e127786f-a191-4d01-b58d-071eb9fc50fc",
  "uuid": "7f73b347-e1e7-4ea7-be71-d3ed931e4f9e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014uESCXxE7yDP7dMksL6NCg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14395,
      "cache_read_input_tokens": 41400,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14395
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

_source line 29 · 2026-05-16T22:42:59.949Z_

<details><summary>↩ Tool result · `toolu_01CKjwF1BFu33GVcJL7Vcmc8`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Implications for deployment.}
5	A uniform compression budget implicitly accepts order-of-magnitude severity penalties during low-sparsity reasoning phases. Pilot evaluation ($n{=}30$, $s{=}0.25$; Appendix~\ref{app:pilot-mitigation}) achieved 18\% oracle recovery (95\% CI: $[-39\%, 45.8\%]$), falling below the pre-registered 30\% gate; the CI spans zero, indicating no statistically distinguishable improvement. Effective phase-aware allocation likely requires finer phase boundary estimation than current proxies provide. Additional mechanisms (e.g., strategy switching, adaptive thresholding) warrant investigation. We hypothesize that phase-modulated severity may extend to alternative attention-mass-based scoring methods (H$_2$O \cite{h2o-neurips2023}, SnapKV \cite{snapkv-neurips2024}, PyramidKV \cite{pyramidkv-colm2025}), which remains an open question for future work. Extended discussion in Appendix~\ref{app:extended-discussion}.
6	
7	\paragraph{Reasoning depth scaling.}
8	Strategy specificity is not a fixed property but scales with reasoning chain depth: MATH-500 ($15$--$17{\times}$) $>$ GSM8K (${\sim}3{\times}$), with within-MATH-500 correlational support (Spearman $\rho > 0$, $p < 0.02$ between trace length and specificity). This scaling is consistent with the discrimination collapse mechanism: longer low-sparsity phases provide more tokens over which pruning-degraded importance scores accumulate errors, amplifying the gap between importance-based and random eviction. The implication is practical: as models generate longer reasoning chains (a trend driven by test-time compute scaling~\cite{snell-2024-scaling-test-time}), the penalty for naive compound compression grows superlinearly.
9	
10	\paragraph{Diagnostic framework value.}
11	While we do not propose a new compression method, the phase-gated analysis framework has direct engineering utility: (1)~the Interaction Index can serve as a per-phase evaluation metric for assessing the phase robustness of any new compound compression scheme; (2)~the dose-response curves (Figure~\ref{fig:hero}) provide target operating points for phase-aware controllers---e.g., maintaining $s \leq 0.20$ during low-sparsity phases to keep $\Delta < 1.5$; (3)~the strategy specificity finding carries a concrete engineering implication: importance-based eviction under compound sparsity requires phase-aware protection that random eviction does not, because the interaction is structurally coupled to the scoring mechanism rather than to compression magnitude alone.
12	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e127786f-a191-4d01-b58d-071eb9fc50fc",
  "uuid": "1e225e17-4f21-42f7-9144-5f04d3ba3702",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex",
      "content": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Implications for deployment.}\nA uniform compression budget implicitly accepts order-of-magnitude severity penalties during low-sparsity reasoning phases. Pilot evaluation ($n{=}30$, $s{=}0.25$; Appendix~\\ref{app:pilot-mitigation}) achieved 18\\% oracle recovery (95\\% CI: $[-39\\%, 45.8\\%]$), falling below the pre-registered 30\\% gate; the CI spans zero, indicating no statistically distinguishable improvement. Effective phase-aware allocation likely requires finer phase boundary estimation than current proxies provide. Additional mechanisms (e.g., strategy switching, adaptive thresholding) warrant investigation. We hypothesize that phase-modulated severity may extend to alternative attention-mass-based scoring methods (H$_2$O \\cite{h2o-neurips2023}, SnapKV \\cite{snapkv-neurips2024}, PyramidKV \\cite{pyramidkv-colm2025}), which remains an open question for future work. Extended discussion in Appendix~\\ref{app:extended-discussion}.\n\n\\paragraph{Reasoning depth scaling.}\nStrategy specificity is not a fixed property but scales with reasoning chain depth: MATH-500 ($15$--$17{\\times}$) $>$ GSM8K (${\\sim}3{\\times}$), with within-MATH-500 correlational support (Spearman $\\rho > 0$, $p < 0.02$ between trace length and specificity). This scaling is consistent with the discrimination collapse mechanism: longer low-sparsity phases provide more tokens over which pruning-degraded importance scores accumulate errors, amplifying the gap between importance-based and random eviction. The implication is practical: as models generate longer reasoning chains (a trend driven by test-time compute scaling~\\cite{snell-2024-scaling-test-time}), the penalty for naive compound compression grows superlinearly.\n\n\\paragraph{Diagnostic framework value.}\nWhile we do not propose a new compression method, the phase-gated analysis framework has direct engineering utility: (1)~the Interaction Index can serve as a per-phase evaluation metric for assessing the phase robustness of any new compound compression scheme; (2)~the dose-response curves (Figure~\\ref{fig:hero}) provide target operating points for phase-aware controllers---e.g., maintaining $s \\leq 0.20$ during low-sparsity phases to keep $\\Delta < 1.5$; (3)~the strategy specificity finding carries a concrete engineering implication: importance-based eviction under compound sparsity requires phase-aware protection that random eviction does not, because the interaction is structurally coupled to the scoring mechanism rather than to compression magnitude alone.\n",
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

_source line 30_

<details open><summary>🔧 Tool call — Read · `toolu_01FQo1CDzSC3d6VHxMUdu1xS`</summary>

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
  "session_id": "e127786f-a191-4d01-b58d-071eb9fc50fc",
  "uuid": "4aa5a6b8-87e5-42dd-8e19-9c01312be44a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014uESCXxE7yDP7dMksL6NCg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14395,
      "cache_read_input_tokens": 41400,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14395
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

_source line 31 · 2026-05-16T22:43:00.036Z_

<details><summary>↩ Tool result · `toolu_01FQo1CDzSC3d6VHxMUdu1xS`</summary>

```text
1	\section{Importance Discrimination Collapse under Compound Sparsity}
2	\label{sec:analysis}
3	
4	The mechanisms discussed here are \emph{correlational diagnostics} that illuminate but do not fully explain the $15$--$17{\times}$ severity divergence between strategies. Both strategies exhibit near-identical Gini drops ($<10\%$ difference), yet severity diverges by $15$--$17{\times}$---an order-of-magnitude mismatch indicating that aggregate concentration collapse alone is insufficient. The critical differentiator is \emph{structural specificity} of importance-based pruning, which systematically removes high-attention-score heads (\S\ref{sec:discrimination-collapse-main}).
5	
6	\subsection{Importance Discrimination Collapse}
7	\label{sec:discrimination-collapse-main}
8	
9	Head pruning systematically reduces the discriminative power of cumulative importance scores, providing a correlational diagnostic for the phase-strategy interaction (causal attribution requires future intervention experiments). The Gini coefficient decreases by $0.030$--$0.081$ (DeepSeek, $6$--$17\%$ relative to dense baseline) and $0.010$--$0.020$ (Qwen, $2$--$4\%$) after pruning, with consistent negative deltas in all 16 conditions (Appendix~\ref{app:analysis}, Table~\ref{tab:discrimination-metrics-full}). Random eviction shows near-identical Gini drops (e.g., DeepSeek $s{=}0.25$: $-0.065$ vs.\ $-0.060$), indicating that collapse is a consequence of head pruning \emph{per se}. Yet importance-based severity is $15$--$17{\times}$ larger---the amplification arises because importance-based eviction \emph{depends on} the very scores that pruning degrades.
10	
11	This pattern---\emph{importance discrimination collapse}---reflects eviction degenerating into noise-sensitive selection as score distributions approach uniformity. The effect is phase-dependent: per-phase Gini analysis shows that the low-sparsity phase exhibits the largest Gini delta at every sparsity level on both models, with monotonically increasing magnitude (DeepSeek: $-0.016$ at $s{=}0.15$, $-0.021$ at $s{=}0.20$, $-0.031$ at $s{=}0.25$, $-0.037$ at $s{=}0.30$; Qwen: $-0.017$, $-0.020$, $-0.029$, $-0.035$). Low-sparsity phases have broadly distributed attention where collapse has maximum impact; high-sparsity phases preserve concentration. \cite{hies-2025} report this collapse under single-axis pruning; we extend it to the compound setting.
12	
13	To provide quantitative evidence for structural specificity, we analyzed the attention Gini coefficients of importance-pruned versus retained heads. Importance pruning (Frobenius norm criterion) systematically removes heads with lower Gini coefficients---i.e., heads with more dispersed attention patterns (Mann-Whitney $U$, $p < 10^{-28}$; rank-biserial $r = 0.62$--$0.76$ across all 8 conditions). Random pruning, by contrast, samples heads with Gini indistinguishable from the population mean (200-trial verification). The Frobenius norm and Gini share sensitivity to attention magnitude; the large effect size ($r > 0.6$) nonetheless indicates strong structural separation.
14	
15	We note that this evidence is correlational; causal validation through controlled manipulation of importance-score entropy is an important direction for future work.
16	
17	\subsection{Entropy Redistribution: A Model-Dependent Secondary Effect}
18	\label{sec:entropy-redistribution-main}
19	
20	As a supplementary observation, head pruning also redistributes the attention entropy of surviving heads on DeepSeek ($\Delta\mathcal{H} \in [-0.047, -0.040]$; Appendix~\ref{app:analysis}, Table~\ref{tab:entropy-deltas}). However, entropy redistribution shows model-dependent behavior---the direction reverses on Qwen at $s{=}0.25$ ($\Delta\mathcal{H} = +0.045$)---replicating in only 2/4 Qwen conditions and thus only partially consistent. Importance discrimination collapse remains the more robust, model-independent correlate, though it partially accounts for rather than fully explains the severity divergence.
21	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e127786f-a191-4d01-b58d-071eb9fc50fc",
  "uuid": "0368296c-d4b0-4968-8f6f-9b1c55e0d433",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex",
      "content": "\\section{Importance Discrimination Collapse under Compound Sparsity}\n\\label{sec:analysis}\n\nThe mechanisms discussed here are \\emph{correlational diagnostics} that illuminate but do not fully explain the $15$--$17{\\times}$ severity divergence between strategies. Both strategies exhibit near-identical Gini drops ($<10\\%$ difference), yet severity diverges by $15$--$17{\\times}$---an order-of-magnitude mismatch indicating that aggregate concentration collapse alone is insufficient. The critical differentiator is \\emph{structural specificity} of importance-based pruning, which systematically removes high-attention-score heads (\\S\\ref{sec:discrimination-collapse-main}).\n\n\\subsection{Importance Discrimination Collapse}\n\\label{sec:discrimination-collapse-main}\n\nHead pruning systematically reduces the discriminative power of cumulative importance scores, providing a correlational diagnostic for the phase-strategy interaction (causal attribution requires future intervention experiments). The Gini coefficient decreases by $0.030$--$0.081$ (DeepSeek, $6$--$17\\%$ relative to dense baseline) and $0.010$--$0.020$ (Qwen, $2$--$4\\%$) after pruning, with consistent negative deltas in all 16 conditions (Appendix~\\ref{app:analysis}, Table~\\ref{tab:discrimination-metrics-full}). Random eviction shows near-identical Gini drops (e.g., DeepSeek $s{=}0.25$: $-0.065$ vs.\\ $-0.060$), indicating that collapse is a consequence of head pruning \\emph{per se}. Yet importance-based severity is $15$--$17{\\times}$ larger---the amplification arises because importance-based eviction \\emph{depends on} the very scores that pruning degrades.\n\nThis pattern---\\emph{importance discrimination collapse}---reflects eviction degenerating into noise-sensitive selection as score distributions approach uniformity. The effect is phase-dependent: per-phase Gini analysis shows that the low-sparsity phase exhibits the largest Gini delta at every sparsity level on both models, with monotonically increasing magnitude (DeepSeek: $-0.016$ at $s{=}0.15$, $-0.021$ at $s{=}0.20$, $-0.031$ at $s{=}0.25$, $-0.037$ at $s{=}0.30$; Qwen: $-0.017$, $-0.020$, $-0.029$, $-0.035$). Low-sparsity phases have broadly distributed attention where collapse has maximum impact; high-sparsity phases preserve concentration. \\cite{hies-2025} report this collapse under single-axis pruning; we extend it to the compound setting.\n\nTo provide quantitative evidence for structural specificity, we analyzed the attention Gini coefficients of importance-pruned versus retained heads. Importance pruning (Frobenius norm criterion) systematically removes heads with lower Gini coefficients---i.e., heads with more dispersed attention patterns (Mann-Whitney $U$, $p < 10^{-28}$; rank-biserial $r = 0.62$--$0.76$ across all 8 conditions). Random pruning, by contrast, samples heads with Gini indistinguishable from the population mean (200-trial verification). The Frobenius norm and Gini share sensitivity to attention magnitude; the large effect size ($r > 0.6$) nonetheless indicates strong structural separation.\n\nWe note that this evidence is correlational; causal validation through controlled manipulation of importance-score entropy is an important direction for future work.\n\n\\subsection{Entropy Redistribution: A Model-Dependent Secondary Effect}\n\\label{sec:entropy-redistribution-main}\n\nAs a supplementary observation, head pruning also redistributes the attention entropy of surviving heads on DeepSeek ($\\Delta\\mathcal{H} \\in [-0.047, -0.040]$; Appendix~\\ref{app:analysis}, Table~\\ref{tab:entropy-deltas}). However, entropy redistribution shows model-dependent behavior---the direction reverses on Qwen at $s{=}0.25$ ($\\Delta\\mathcal{H} = +0.045$)---replicating in only 2/4 Qwen conditions and thus only partially consistent. Importance discrimination collapse remains the more robust, model-independent correlate, though it partially accounts for rather than fully explains the severity divergence.\n",
      "numLines": 21,
      "startLine": 1,
      "totalLines": 21
    }
  }
}
```

</details>

---

### Assistant

_source line 32_

<details><summary>Logged reasoning block</summary>

```text
Now let me check the key issues:

1. **paper_framing.md vs tex files on "architecture-dependent" claim:**
   - paper_framing.md says: "strategy-dependence 强度 architecture-dependent" and in C8: "Qualitative direction consistent, quantitative strategy×phase interaction weaker + architecture-dependent"
   - abstract.tex (line 6): "strategy specificity architecture-dependent" ✓
   - introduction.tex (line 15): "despite reduced strategy specificity ($2.0$--$2.6{\times}$ vs.\ $15$--$17{\times}$ on Qwen2-family models)" ✓
   - introduction.tex (line 26): "strategy specificity reduced to $2.0$--$2.6{\times}$, architecture-dependent" ✓
   - results.tex (line 95): "the degree of strategy specificity is architecture-dependent" ✓
   - conclusion.tex (line 4): "while strategy specificity is architecture-dependent" ✓
   - appendix_moved.tex (line 38): "quantitative strategy specificity is architecture-dependent" ✓

2. **Numbers consistency check:** Now I'm verifying the LLaMA improvement-to-random ratios across the documents to ensure the $2.0$--$2.6{\times}$ figures are consistent with what's reported in paper_framing.md. I'm seeing the same d_z values repeated across the introduction, results, and appendix sections, which checks out. But there's a mismatch with the sample size—the paper_framing document mentions n=50 for the LLaMA cross-architecture validation, yet all the tex files are reporting n=250, which suggests they're using the c8_llama_n250 version instead.

Now I'm verifying the DS median differences across the documents. The values 0.39, 1.21, 3.99, and 8.48 appear consistently in the results table and are cited correctly in the abstract, introduction, and conclusion sections. I'm checking the QW median differences next to see if those align as well. /1.07/3.16" for QW
     - results.tex table: 0.07, 0.31, 1.07, 3.16 ✓
     - abstract.tex: "$0.07 \to 3.16$" ✓
     - introduction.tex: "$0.07 \to 3.16$" ✓
     - conclusion.tex: "$0.07$ to $3.16$" ✓

   - imp/rand ratio: paper_framing.md says "2.7-15×"
     - abstract.tex: "$2.7$--$17{\times}$" (line 5) — DISCREPANCY with paper_framing.md "2.7-15×" but let me look more carefully
     - paper_framing.md core insight: "而 random masking 在 s015/s020 NS，在 s025 跨模型显著但效应量远小于 importance（DS: 0.257 vs 3.986; QW: 0.393 vs 1.074, 2.7-15×差异）"

Now I'm checking the actual ratios across the datasets. For DS at s025, the importance improvement is 3.99 while random is 0.26, giving about 15.3×. At s030, it's even larger at 16.6×. For QW at s025, the ratio is 2.74×, which aligns with the lower bound. The tex files show "$2.7$--$17{\times}$" but the paper_framing.md specifies "2.7-15×", so there's a discrepancy in the upper bound that needs reconciling. I'm noticing inconsistencies across the documents—the narrative arc and core text reference different ranges depending on context, and I need to track what "15-33×" actually refers to. Looking at the paper files, I see GSM8K comparisons showing 15-36× for importance versus random gradients, while other sections mention the ratio decaying to 2.3-3.8×, and the discussion section starts citing 15-17× for MATH-500. I'm trying to reconcile where the 36× figure comes from in the paper_framing.md notes—the tex files consistently show 15-17× for DeepSeek across MATH-500, which matches the direct calculations, so the broader 15-36× range might be pulling from older data or comparisons with other models like Qwen that I need to track down. The 36× might come from a different comparison. Looking at the appendix data with n=50, I'm getting ratios around 13.3× and 9.5×, which differ from the n=500 results showing 15-17× for DeepSeek. The "36×" appears to be outdated. The tex files are consistent internally at "15-17×" for DeepSeek and "2.7-3.5×" for Qwen, but paper_framing.md has "15-36×" which contradicts this and needs fixing.

I'm also noticing several stale references in paper_framing.md: the LLaMA section still mentions n=50 when the current data is n=250, and the range descriptions use "2.7-15×" or "2.7-15×差异" when they should reflect the full "2.7-17×" span across all models. The paper_framing.md file reports LLaMA random phase gradients as d_z 0.35→0.44, but the actual tex data shows 0.41-0.46, so that range needs updating. I'm also noticing the document still references the old n=50 pilot data for LLaMA cross-architecture validation, which should be replaced with the new n=250 results showing much stronger effects.

Now checking the consistency of "architecture-dependent" phrasing across all sections — it's being used uniformly in the abstract, introduction, results, conclusion, and appendix, plus the framing document, so that terminology is solid throughout.

There's a minor discrepancy with the sample size reporting: the conclusion states n=500 while the results table shows n=496 (since 4 problems were excluded from the original 500). Technically both are defensible — one refers to the experiment's initial size and the other to the effective sample — but a reviewer might flag this inconsistency, so the conclusion should probably align with what the results section reports.

The MATH-500 and GSM8K performance comparisons in the discussion match the underlying data, so those are fine.

Now I'm noticing something odd about the GSM8K ratio claim. The discussion says "~3×" but the results section explicitly states that random performance is non-significant across all conditions on GSM8K, which makes it unclear how that ratio was computed. The framing document mentions an imp/rand ratio of 2.3-3.8× and the introduction notes that strategy specificity attenuates on GSM8K relative to MATH-500, but I need to trace through where exactly this "~3×" figure comes from. results section says for GSM8K: "Strategy specificity on GSM8K manifests as a qualitative gap: importance-based eviction produces significant phase gradients while random eviction is non-significant across all conditions"
    - So on GSM8K, the "ratio" can't be computed in the same way since random is NS. The "2.3-3.8×" and "~3×" seems to be from looking at raw Δ values even though random is NS.
    - Wait, paper_framing.md Core Insight says: "GSM8K 跨 benchmark 验证（D075）：importance masking 的 phase gradient 在 GSM8K 上同样单调递增（QW: 0.039→0.158→1.100→2.092; DS: 0.241→0.740→1.992→4.682），但 strategy specificity（importance/random gradient ratio）从 MATH-500 的 15-36× 衰减至 GSM8K 的 2.3-3.8×"

Now I'm looking at the actual GSM8K data from the appendix tables, and the random eviction deltas are all non-significant. The 2.3-3.8× ratio appears to come from comparing raw delta magnitudes even when random doesn't reach significance—for instance, with DeepSeek, the importance deltas are 0.24, 0.74, 1.99, 4.68 while random shows -0.04, 0.28, 0.98, 2.85, which would give ratios like 2.6× and 2.0× when dividing the larger values by the smaller ones. The "~3×" comparison in the discussion might be calculated differently—possibly from the QW data where importance shows significant deltas compared to Qwen's random baseline on MATH-500, though this feels like a loose approximation. The results.tex file clarifies that on GSM8K, importance-based strategies create meaningful phase gradients while random eviction remains non-significant across all conditions.

There's a tension here: the results section carefully describes this as a qualitative gap, but the discussion quantifies it as "~3×," which is a minor inconsistency worth flagging.

I'm also noticing that paper_framing.md claims d_z~1.0 for the within-importance phase gradient, and the actual tex values of 0.81-1.15 do support that approximation. However, the framing document still references the older n=50 terminology in several places rather than the updated n=250 LLaMA data, so there's some outdated language to clean up.

Now I'm seeing several critical mismatches between paper_framing.md and the actual tex files. The Core Insight section is citing old n=50 c3_llama results showing imp_vs_rand d_z of 0.19→0.34 with only s030 significant, but the new n=250 data shows a much stronger imp/rand Δ ratio of 2.0-2.6× with random d_z=0.41-0.46 and all conditions reaching significance. Similarly, RC1 still frames the LLaMA cross-architecture validation as limited by n=50, which is no longer the constraint. And there's a discrepancy in the MATH-500 strategy ratio—paper_framing.md claims "15-36×" while the tex files consistently show either "15-17×" for DeepSeek or "2.7-17×" across different conditions.

The header claim of "imp/rand 2.7-15×" also needs updating to "2.7-17×" to match the tex data, and the Core Insight's description of random showing d_z=0.35→0.44 on LLaMA should be corrected to d_z=0.41-0.46. In the tex files themselves, there's a minor inconsistency where conclusion.tex reports n=500 while results.tex uses n=496 (the difference being 4 excluded problems), and discussion.tex references "~3×" for GSM8K strategy specificity, though results.tex describes the GSM8K random condition as non-significant, suggesting the "~3×" might be derived from raw deltas rather than a proper effect size comparison.

I've verified that the LLaMA numbers, core DS/QW improvements, and architecture-dependent terminology are all consistent across the tex files, and there's no stale pilot data lingering in the main sections. Now I need to draft the corrections for paper_framing.md.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e127786f-a191-4d01-b58d-071eb9fc50fc",
  "uuid": "2e978923-f81e-4e30-af63-ea87fa3866fb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T7SgjG7o71tQEkuJu69F1N",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2080,
      "cache_read_input_tokens": 55795,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2080
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

_source line 33_

Here's my consistency check. Let me also verify one detail about the GSM8K ratio numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e127786f-a191-4d01-b58d-071eb9fc50fc",
  "uuid": "b203d4eb-a8dd-4509-9b43-5f6fbca5f1cf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T7SgjG7o71tQEkuJu69F1N",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2080,
      "cache_read_input_tokens": 55795,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2080
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

_source line 34_

<details open><summary>🔧 Tool call — Grep · `toolu_01WRfvVq8gAsusJXPo9rgTJy`</summary>

```json
{
  "pattern": "15.*36|36.*15|33",
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
  "session_id": "e127786f-a191-4d01-b58d-071eb9fc50fc",
  "uuid": "2a941611-10e4-4dfe-b7e1-127c786c9967",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T7SgjG7o71tQEkuJu69F1N",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2080,
      "cache_read_input_tokens": 55795,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2080
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

_source line 35 · 2026-05-16T22:44:44.184Z_

<details><summary>↩ Tool result · `toolu_01WRfvVq8gAsusJXPo9rgTJy`</summary>

```text
artifacts/_project/paper/main.bbl:16:\newblock \href {https://arxiv.org/abs/2505.24133} {{R-KV}: Redundancy-aware
artifacts/_project/paper/main.bbl:48:\newblock \emph{Nature}, 645:633--638.
artifacts/_project/paper/main.bbl:77:\newblock \href {https://arxiv.org/abs/2510.13334} {{DefensiveKV}: Taming the
artifacts/_project/paper/main.bbl:270:\newblock \href {https://arxiv.org/abs/2408.03314} {Scaling {LLM} test-time
artifacts/_project/paper/main.bbl:272:\newblock \emph{arXiv preprint arXiv:2408.03314}.
artifacts/_project/paper/acl.sty:211: \def\newblock{\hskip .11em plus .33em minus -.07em}
artifacts/_project/paper/acl.sty:228: \def\newblock{\hskip .11em plus .33em minus -.07em}
artifacts/_project/paper/numerical_audit_report.md:90:| II_high range | 0.006–0.053 | 0.005752, 0.014513, 0.032363, 0.053399 | ✅ |
artifacts/_project/paper/numerical_audit_report.md:120:| 0.15 | 0.37 | [0.19, 0.62] | 0.0032 | obs=0.3678, CI=[0.1872, 0.6232], p_Bonf=0.0032 | ✅ |
artifacts/_project/paper/numerical_audit_report.md:122:| 0.25 | 3.34 | [1.66, 6.64] | <0.001 | obs=3.3362, CI=[1.6616, 6.6362], p_Bonf=0.0008 | ✅ |
artifacts/_project/paper/main.log:146:Package: pdftexcmds 2020-06-27 v0.33 Utility functions of pdfTeX for LuaTeX (HO
artifacts/_project/paper/main.log:344:LaTeX Info: Redefining \frac on input line 233.
artifacts/_project/paper/main.log:422:Package: booktabs 2020/01/12 v1.61803398 Publication quality tables
artifacts/_project/paper/main.log:438:\@lastruleclass=\count330
artifacts/_project/paper/main.log:447:\enit@count@id=\count331
artifacts/_project/paper/main.log:448:\enitdp@description=\count332
artifacts/_project/paper/main.log:453:\multirow@cntb=\count333
artifacts/_project/paper/main.log:459:\l__color_backend_stack_int=\count334
artifacts/_project/paper/main.log:484:\scratchcounter=\count335
artifacts/_project/paper/main.log:487:\nofMPsegments=\count336
artifacts/_project/paper/main.log:488:\nofMParguments=\count337
artifacts/_project/paper/main.log:489:\everyMPshowfont=\toks33
artifacts/_project/paper/main.log:490:\MPscratchCnt=\count338
artifacts/_project/paper/main.log:492:\MPnumerator=\count339
artifacts/_project/paper/main.log:618:.95 (+20) --$\OT1/cmr/m/n/10.95 33[]$ \T1/ptm/m/n/10.95 (+20) repli-cates, $[]\
artifacts/_project/paper/main.log:712:Underfull \hbox (badness 4036) in paragraph at lines 14--15
artifacts/_project/paper/main.log:907:Package pdftex.def Info: figures/fig4_bootstrap.pdf  used on input line 133.
artifacts/_project/paper/main.log:1116:Underfull \hbox (badness 2359) in paragraph at lines 132--133
artifacts/_project/paper/main.log:1122:Underfull \hbox (badness 2334) in paragraph at lines 135--136
artifacts/_project/paper/main.out:33:\BOOKMARK [1][-]{appendix.J}{\376\377\000E\000x\000t\000e\000n\000d\000e\000d\000\040\000D\000i\000s\000c\000u\000s\000s\000i\000o\000n}{}% 33
artifacts/_project/paper/main.blg:28:duplicate$ -- 2433
artifacts/_project/paper/main.blg:30:format.name$ -- 1133
artifacts/_project/paper/appendix.tex:38:[Omitted long matching line]
artifacts/_project/paper/appendix_disc_analysis.tex:83:0.15 & Random     & 0.036 & 0.105 & $-$0.04\textsuperscript{ns} & 0.90 \\
artifacts/_project/paper/appendix_disc_analysis.tex:107:0.15 & Random     & 0.089 & 0.033 & $-$1.58\textsuperscript{ns} & 0.69 \\
artifacts/_project/paper/appendix_disc_analysis.tex:143:QW & 0.25 & 46\% & 33\% & $-$13\,pp & $\leq$4\% \\
artifacts/_project/paper/appendix_disc_analysis.tex:161:[Omitted long matching line]
artifacts/_project/paper/references.bib:39:    pages   = {633--638},
artifacts/_project/paper/references.bib:49:    url       = {https://arxiv.org/abs/2510.13334},
artifacts/_project/paper/references.bib:202:    url       = {https://arxiv.org/abs/2505.24133},
artifacts/_project/paper/references.bib:386:    journal = {arXiv preprint arXiv:2408.03314},
artifacts/_project/paper/references.bib:388:    url     = {https://arxiv.org/abs/2408.03314},
artifacts/_project/paper/results.tex:8:[Omitted long matching line]
artifacts/_project/paper/main.aux:55:\@LN{33}{0}
artifacts/_project/paper/main.aux:166:\@LN{133}{1}
artifacts/_project/paper/main.aux:305:\@LN{233}{2}
artifacts/_project/paper/main.aux:418:\@LN{330}{3}
artifacts/_project/paper/main.aux:419:\@LN{331}{3}
artifacts/_project/paper/main.aux:420:\@LN{332}{3}
artifacts/_project/paper/main.aux:421:\@LN{333}{3}
artifacts/_project/paper/main.aux:422:\@LN{334}{3}
artifacts/_project/paper/main.aux:423:\@LN{335}{3}
artifacts/_project/paper/main.aux:426:\@LN{336}{3}
artifacts/_project/paper/main.aux:427:\@LN{337}{3}
artifacts/_project/paper/main.aux:429:\@LN{338}{3}
artifacts/_project/paper/main.aux:430:\@LN{339}{3}
artifacts/_project/paper/main.aux:537:\@LN{433}{4}
artifacts/_project/paper/main.aux:654:\@LN{533}{5}
artifacts/_project/paper/main.aux:773:\@LN{633}{7}
artifacts/_project/paper/main.aux:892:\@LN{733}{8}
artifacts/_project/paper/main.aux:1007:\@LN{833}{9}
artifacts/_project/paper/main.aux:1131:\@LN{933}{10}
artifacts/_project/paper/main.aux:1165:\bibcite{sanh-neurips2020}{{33}{2020}{{Sanh et~al.}}{{Sanh, Wolf, and Rush}}}
artifacts/_project/paper/main.aux:1256:\@LN{1033}{11}
artifacts/_project/paper/main.aux:1369:\@LN{1133}{12}
artifacts/_project/paper/main.aux:1431:\@writefile{toc}{\contentsline {paragraph}{Phase segmentation validation.}{14}{section*.33}\protected@file@percent }
artifacts/_project/paper/main.aux:1480:\@LN{1233}{13}
artifacts/_project/paper/main.aux:1595:\@LN{1330}{14}
artifacts/_project/paper/main.aux:1596:\@LN{1331}{14}
artifacts/_project/paper/main.aux:1597:\@LN{1332}{14}
artifacts/_project/paper/main.aux:1598:\@LN{1333}{14}
artifacts/_project/paper/main.aux:1601:\@LN{1334}{14}
artifacts/_project/paper/main.aux:1602:\@LN{1335}{14}
artifacts/_project/paper/main.aux:1603:\@LN{1336}{14}
artifacts/_project/paper/main.aux:1604:\@LN{1337}{14}
artifacts/_project/paper/main.aux:1605:\@LN{1338}{14}
artifacts/_project/paper/main.aux:1606:\@LN{1339}{14}
artifacts/_project/paper/main.aux:1608:[Omitted long matching line]
artifacts/_project/paper/main.aux:1632:\@LN{1360}{15}
artifacts/_project/paper/main.aux:1633:\@LN{1361}{15}
artifacts/_project/paper/main.aux:1636:\@LN{1362}{15}
artifacts/_project/paper/main.aux:1637:\@LN{1363}{15}
artifacts/_project/paper/main.aux:1638:\@LN{1364}{15}
artifacts/_project/paper/main.aux:1639:\@LN{1365}{15}
artifacts/_project/paper/main.aux:1640:\@LN{1366}{15}
artifacts/_project/paper/main.aux:1641:\@LN{1367}{15}
artifacts/_project/paper/main.aux:1642:\@LN{1368}{15}
artifacts/_project/paper/main.aux:1643:\@LN{1369}{15}
artifacts/_project/paper/main.aux:1726:\@LN{1433}{16}
artifacts/_project/paper/main.aux:1845:\@LN{1533}{18}
artifacts/_project/paper/main.aux:1848:\@LN{1536}{18}
artifacts/_project/paper/main.aux:1960:\@LN{1633}{19}
artifacts/_project/paper/main.aux:2070:\@LN{1733}{20}
artifacts/_project/paper/main.aux:2191:\@LN{1833}{22}
artifacts/_project/paper/main.aux:2310:\@LN{1933}{23}
artifacts/_project/paper/acl_natbib.bst:36: % \ProvidesFile{merlin.mbs}[2011/11/18 4.33 (PWD, AO, DPC)]
artifacts/_project/paper/appendix_robustness.tex:42:DS & Imp & 0.15 & 0.391 & 0.391 & 0.393 & 496 & 433 \\
artifacts/_project/paper/appendix_robustness.tex:43:DS & Imp & 0.20 & 1.215 & 1.215 & 1.235 & 496 & 433 \\
artifacts/_project/paper/appendix_robustness.tex:44:DS & Imp & 0.25 & 3.986 & 3.986 & 4.017 & 496 & 433 \\
artifacts/_project/paper/appendix_robustness.tex:45:DS & Imp & 0.30 & 8.481 & 8.481 & 8.420 & 496 & 433 \\
artifacts/_project/paper/appendix_robustness.tex:47:DS & Rand & 0.15 & 0.014 & 0.014\textsuperscript{ns} & 0.012\textsuperscript{ns} & 496 & 433 \\
artifacts/_project/paper/appendix_robustness.tex:48:DS & Rand & 0.20 & 0.031\textsuperscript{ns} & 0.031\textsuperscript{ns} & 0.023\textsuperscript{ns} & 496 & 433 \\
artifacts/_project/paper/appendix_robustness.tex:49:DS & Rand & 0.25 & 0.257 & 0.257 & 0.190 & 496 & 433 \\
artifacts/_project/paper/appendix_robustness.tex:50:DS & Rand & 0.30 & 0.510 & 0.510 & 0.410 & 496 & 433 \\
artifacts/_project/paper/appendix_robustness.tex:65:The main effect of increasing mpl is reduced $n_{\text{eff}}$: at mpl$=$20, DeepSeek retains 433/500 problems and Qwen retains 289/500 (mid-null rate rises to 71.2\% and 84.6\%, respectively). Despite this sample reduction, all significance conclusions hold.
artifacts/_project/paper/appendix_robustness.tex:82:\multirow{4}{*}{DeepSeek} & 0.15 & 0.391 & 0.491\; $[0.44,\; 0.70]$ & 0.505\; $[0.33,\; 0.71]$ \\
artifacts/_project/paper/appendix_moved.tex:158:0.15 & Random     & $0.025$ & $0.436$ & $9.3 \times 10^{-13}$ \\
artifacts/_project/paper/methodology.tex:21:[Omitted long matching line]
artifacts/_project/paper/response_letter.md:21:- **W1**: Spearman rho=1.0 downgraded to footnote; Jonckheere-Terpstra test promoted to primary dose-response statistic (z=6.2--33.7)
artifacts/_project/paper/main.fdb_latexmk:8:  "/usr/share/texlive/texmf-dist/fonts/tfm/adobe/helvetic/phvb8r.tfm" 1136768653 4484 b828043cbd581d289d955903c1339981 ""
artifacts/_project/paper/main.fdb_latexmk:9:  "/usr/share/texlive/texmf-dist/fonts/tfm/adobe/times/ptmb8r.tfm" 1136768653 4524 6bce29db5bc272ba5f332261583fee9c ""
artifacts/_project/paper/main.fdb_latexmk:10:  "/usr/share/texlive/texmf-dist/fonts/tfm/adobe/times/ptmb8t.tfm" 1136768653 6880 f19b8995b61c334d78fc734065f6b4d4 ""
artifacts/_project/paper/main.fdb_latexmk:13:  "/usr/share/texlive/texmf-dist/fonts/tfm/adobe/times/ptmri8r.tfm" 1136768653 4640 532ca3305aad10cc01d769f3f91f1029 ""
artifacts/_project/paper/main.fdb_latexmk:25:  "/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmmi10.tfm" 1136768653 1528 abec98dbc43e172678c11b3b9031252a ""
artifacts/_project/paper/main.fdb_latexmk:26:  "/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmmi12.tfm" 1136768653 1524 4414a8315f39513458b80dfc63bff03a ""
artifacts/_project/paper/main.fdb_latexmk:27:  "/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmmi6.tfm" 1136768653 1512 f21f83efb36853c0b70002322c1ab3ad ""
artifacts/_project/paper/main.fdb_latexmk:28:  "/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmmi8.tfm" 1136768653 1520 eccf95517727cb11801f4f1aee3a21b4 ""
artifacts/_project/paper/main.fdb_latexmk:29:  "/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmmi9.tfm" 1136768653 1524 d89e2d087a9828407a196f428428ef4a ""
artifacts/_project/paper/main.fdb_latexmk:32:  "/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmr6.tfm" 1136768653 1300 b62933e007d01cfd073f79b963c01526 ""
artifacts/_project/paper/main.fdb_latexmk:36:  "/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmsy6.tfm" 1136768653 1116 933a60c408fc0a863a92debe84b2d294 ""
artifacts/_project/paper/main.fdb_latexmk:46:  "/usr/share/texlive/texmf-dist/fonts/vf/adobe/helvetic/phvb.vf" 1136768653 1516 a73c15525916e6e96ff30639f5ddb11b ""
artifacts/_project/paper/main.fdb_latexmk:51:  "/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty" 1576625341 40635 c40361e206be584d448876bba8a64a3b ""
artifacts/_project/paper/main.fdb_latexmk:52:  "/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty" 1576016050 33961 6b5c75130e435b2bfdb9f480a09a39f9 ""
artifacts/_project/paper/main.fdb_latexmk:55:  "/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty" 1572645307 1057 525c2192b5febbd8c1f662c9468335bb ""
artifacts/_project/paper/main.fdb_latexmk:56:  "/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty" 1575499628 8356 7bbb2c2373aa810be568c29e333da8ed ""
artifacts/_project/paper/main.fdb_latexmk:58:  "/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty" 1576878844 5412 d5a2436094cd7be85769db90f29250a6 ""
artifacts/_project/paper/main.fdb_latexmk:61:  "/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty" 1593379760 20089 80423eac55aa175305d35b49e04fe23b ""
artifacts/_project/paper/main.fdb_latexmk:64:  "/usr/share/texlive/texmf-dist/tex/generic/xkeyval/xkeyval.tex" 1762376337 19299 c7c03646b32f5a7caaa137673b7e76d2 ""
artifacts/_project/paper/main.fdb_latexmk:65:  "/usr/share/texlive/texmf-dist/tex/generic/xkeyval/xkvutils.tex" 1762376337 7787 7dfc2f158253fc82fd655393220e6620 ""
artifacts/_project/paper/main.fdb_latexmk:79:  "/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo" 1748806692 8464 f339f4d5391fbe0425b2d94c90e6819e ""
artifacts/_project/paper/main.fdb_latexmk:81:  "/usr/share/texlive/texmf-dist/tex/latex/base/ulasy.fd" 1738182759 2233 b5d3114ec3e0616e658a8e7b74e810f1 ""
artifacts/_project/paper/main.fdb_latexmk:83:  "/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty" 1696191071 56128 c2ccf1a29d78c33bc553880402e4fb9a ""
artifacts/_project/paper/main.fdb_latexmk:86:  "/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty" 1579991033 13886 d1306dcf79a944f6988e688c1785f9ce ""
artifacts/_project/paper/main.fdb_latexmk:91:  "/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def" 1759176675 19626 23e2822b9b2b5005f4c549ca98b9334d ""
artifacts/_project/paper/main.fdb_latexmk:94:  "/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty" 1748806692 8118 43b99e52946c33a23f5f43b52d5cc5ec ""
artifacts/_project/paper/main.fdb_latexmk:96:  "/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx" 1667332637 2885 9c645d672ae17285bba324998918efd8 ""
artifacts/_project/paper/main.fdb_latexmk:97:  "/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty" 1748806692 4023 e66acf578d6b564c4670fb57ff336a7a ""
artifacts/_project/paper/main.fdb_latexmk:101:  "/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty" 1750533789 11027 0fe7ce2c6b5291fd809c2de7bbdca37e ""
artifacts/_project/paper/main.fdb_latexmk:105:  "/usr/share/texlive/texmf-dist/tex/latex/inconsolata/t1zi4.fd" 1516054831 1021 03341d1cf7f388bbac1915f944d5d128 ""
artifacts/_project/paper/main.fdb_latexmk:123:  "/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty" 1750533675 9684 a33a14b82ce60d6e77cb9be689d79ee6 ""
artifacts/_project/paper/main.fdb_latexmk:124:  "/usr/share/texlive/texmf-dist/tex/latex/upquote/upquote.sty" 1334873510 1048 517e01cde97c1c0baf72e69d43aa5a2e ""
artifacts/_project/paper/main.fdb_latexmk:127:  "/usr/share/texlive/texmf-dist/tex/latex/xkeyval/xkeyval.sty" 1762376337 5006 d7e899bb5d9717c7f214e9bc0284de7b ""
artifacts/_project/paper/main.fdb_latexmk:134:  "background.tex" 1778903870.43558 4501 6fa94f1901655336cda45eb6be308b0e ""
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e127786f-a191-4d01-b58d-071eb9fc50fc",
  "uuid": "46723972-6ea9-421c-b3bc-2cc0bbb7ec55",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "artifacts/_project/paper/main.bbl:16:\\newblock \\href {https://arxiv.org/abs/2505.24133} {{R-KV}: Redundancy-aware\nartifacts/_project/paper/main.bbl:48:\\newblock \\emph{Nature}, 645:633--638.\nartifacts/_project/paper/main.bbl:77:\\newblock \\href {https://arxiv.org/abs/2510.13334} {{DefensiveKV}: Taming the\nartifacts/_project/paper/main.bbl:270:\\newblock \\href {https://arxiv.org/abs/2408.03314} {Scaling {LLM} test-time\nartifacts/_project/paper/main.bbl:272:\\newblock \\emph{arXiv preprint arXiv:2408.03314}.\nartifacts/_project/paper/acl.sty:211: \\def\\newblock{\\hskip .11em plus .33em minus -.07em}\nartifacts/_project/paper/acl.sty:228: \\def\\newblock{\\hskip .11em plus .33em minus -.07em}\nartifacts/_project/paper/numerical_audit_report.md:90:| II_high range | 0.006–0.053 | 0.005752, 0.014513, 0.032363, 0.053399 | ✅ |\nartifacts/_project/paper/numerical_audit_report.md:120:| 0.15 | 0.37 | [0.19, 0.62] | 0.0032 | obs=0.3678, CI=[0.1872, 0.6232], p_Bonf=0.0032 | ✅ |\nartifacts/_project/paper/numerical_audit_report.md:122:| 0.25 | 3.34 | [1.66, 6.64] | <0.001 | obs=3.3362, CI=[1.6616, 6.6362], p_Bonf=0.0008 | ✅ |\nartifacts/_project/paper/main.log:146:Package: pdftexcmds 2020-06-27 v0.33 Utility functions of pdfTeX for LuaTeX (HO\nartifacts/_project/paper/main.log:344:LaTeX Info: Redefining \\frac on input line 233.\nartifacts/_project/paper/main.log:422:Package: booktabs 2020/01/12 v1.61803398 Publication quality tables\nartifacts/_project/paper/main.log:438:\\@lastruleclass=\\count330\nartifacts/_project/paper/main.log:447:\\enit@count@id=\\count331\nartifacts/_project/paper/main.log:448:\\enitdp@description=\\count332\nartifacts/_project/paper/main.log:453:\\multirow@cntb=\\count333\nartifacts/_project/paper/main.log:459:\\l__color_backend_stack_int=\\count334\nartifacts/_project/paper/main.log:484:\\scratchcounter=\\count335\nartifacts/_project/paper/main.log:487:\\nofMPsegments=\\count336\nartifacts/_project/paper/main.log:488:\\nofMParguments=\\count337\nartifacts/_project/paper/main.log:489:\\everyMPshowfont=\\toks33\nartifacts/_project/paper/main.log:490:\\MPscratchCnt=\\count338\nartifacts/_project/paper/main.log:492:\\MPnumerator=\\count339\nartifacts/_project/paper/main.log:618:.95 (+20) --$\\OT1/cmr/m/n/10.95 33[]$ \\T1/ptm/m/n/10.95 (+20) repli-cates, $[]\\\nartifacts/_project/paper/main.log:712:Underfull \\hbox (badness 4036) in paragraph at lines 14--15\nartifacts/_project/paper/main.log:907:Package pdftex.def Info: figures/fig4_bootstrap.pdf  used on input line 133.\nartifacts/_project/paper/main.log:1116:Underfull \\hbox (badness 2359) in paragraph at lines 132--133\nartifacts/_project/paper/main.log:1122:Underfull \\hbox (badness 2334) in paragraph at lines 135--136\nartifacts/_project/paper/main.out:33:\\BOOKMARK [1][-]{appendix.J}{\\376\\377\\000E\\000x\\000t\\000e\\000n\\000d\\000e\\000d\\000\\040\\000D\\000i\\000s\\000c\\000u\\000s\\000s\\000i\\000o\\000n}{}% 33\nartifacts/_project/paper/main.blg:28:duplicate$ -- 2433\nartifacts/_project/paper/main.blg:30:format.name$ -- 1133\nartifacts/_project/paper/appendix.tex:38:[Omitted long matching line]\nartifacts/_project/paper/appendix_disc_analysis.tex:83:0.15 & Random     & 0.036 & 0.105 & $-$0.04\\textsuperscript{ns} & 0.90 \\\\\nartifacts/_project/paper/appendix_disc_analysis.tex:107:0.15 & Random     & 0.089 & 0.033 & $-$1.58\\textsuperscript{ns} & 0.69 \\\\\nartifacts/_project/paper/appendix_disc_analysis.tex:143:QW & 0.25 & 46\\% & 33\\% & $-$13\\,pp & $\\leq$4\\% \\\\\nartifacts/_project/paper/appendix_disc_analysis.tex:161:[Omitted long matching line]\nartifacts/_project/paper/references.bib:39:    pages   = {633--638},\nartifacts/_project/paper/references.bib:49:    url       = {https://arxiv.org/abs/2510.13334},\nartifacts/_project/paper/references.bib:202:    url       = {https://arxiv.org/abs/2505.24133},\nartifacts/_project/paper/references.bib:386:    journal = {arXiv preprint arXiv:2408.03314},\nartifacts/_project/paper/references.bib:388:    url     = {https://arxiv.org/abs/2408.03314},\nartifacts/_project/paper/results.tex:8:[Omitted long matching line]\nartifacts/_project/paper/main.aux:55:\\@LN{33}{0}\nartifacts/_project/paper/main.aux:166:\\@LN{133}{1}\nartifacts/_project/paper/main.aux:305:\\@LN{233}{2}\nartifacts/_project/paper/main.aux:418:\\@LN{330}{3}\nartifacts/_project/paper/main.aux:419:\\@LN{331}{3}\nartifacts/_project/paper/main.aux:420:\\@LN{332}{3}\nartifacts/_project/paper/main.aux:421:\\@LN{333}{3}\nartifacts/_project/paper/main.aux:422:\\@LN{334}{3}\nartifacts/_project/paper/main.aux:423:\\@LN{335}{3}\nartifacts/_project/paper/main.aux:426:\\@LN{336}{3}\nartifacts/_project/paper/main.aux:427:\\@LN{337}{3}\nartifacts/_project/paper/main.aux:429:\\@LN{338}{3}\nartifacts/_project/paper/main.aux:430:\\@LN{339}{3}\nartifacts/_project/paper/main.aux:537:\\@LN{433}{4}\nartifacts/_project/paper/main.aux:654:\\@LN{533}{5}\nartifacts/_project/paper/main.aux:773:\\@LN{633}{7}\nartifacts/_project/paper/main.aux:892:\\@LN{733}{8}\nartifacts/_project/paper/main.aux:1007:\\@LN{833}{9}\nartifacts/_project/paper/main.aux:1131:\\@LN{933}{10}\nartifacts/_project/paper/main.aux:1165:\\bibcite{sanh-neurips2020}{{33}{2020}{{Sanh et~al.}}{{Sanh, Wolf, and Rush}}}\nartifacts/_project/paper/main.aux:1256:\\@LN{1033}{11}\nartifacts/_project/paper/main.aux:1369:\\@LN{1133}{12}\nartifacts/_project/paper/main.aux:1431:\\@writefile{toc}{\\contentsline {paragraph}{Phase segmentation validation.}{14}{section*.33}\\protected@file@percent }\nartifacts/_project/paper/main.aux:1480:\\@LN{1233}{13}\nartifacts/_project/paper/main.aux:1595:\\@LN{1330}{14}\nartifacts/_project/paper/main.aux:1596:\\@LN{1331}{14}\nartifacts/_project/paper/main.aux:1597:\\@LN{1332}{14}\nartifacts/_project/paper/main.aux:1598:\\@LN{1333}{14}\nartifacts/_project/paper/main.aux:1601:\\@LN{1334}{14}\nartifacts/_project/paper/main.aux:1602:\\@LN{1335}{14}\nartifacts/_project/paper/main.aux:1603:\\@LN{1336}{14}\nartifacts/_project/paper/main.aux:1604:\\@LN{1337}{14}\nartifacts/_project/paper/main.aux:1605:\\@LN{1338}{14}\nartifacts/_project/paper/main.aux:1606:\\@LN{1339}{14}\nartifacts/_project/paper/main.aux:1608:[Omitted long matching line]\nartifacts/_project/paper/main.aux:1632:\\@LN{1360}{15}\nartifacts/_project/paper/main.aux:1633:\\@LN{1361}{15}\nartifacts/_project/paper/main.aux:1636:\\@LN{1362}{15}\nartifacts/_project/paper/main.aux:1637:\\@LN{1363}{15}\nartifacts/_project/paper/main.aux:1638:\\@LN{1364}{15}\nartifacts/_project/paper/main.aux:1639:\\@LN{1365}{15}\nartifacts/_project/paper/main.aux:1640:\\@LN{1366}{15}\nartifacts/_project/paper/main.aux:1641:\\@LN{1367}{15}\nartifacts/_project/paper/main.aux:1642:\\@LN{1368}{15}\nartifacts/_project/paper/main.aux:1643:\\@LN{1369}{15}\nartifacts/_project/paper/main.aux:1726:\\@LN{1433}{16}\nartifacts/_project/paper/main.aux:1845:\\@LN{1533}{18}\nartifacts/_project/paper/main.aux:1848:\\@LN{1536}{18}\nartifacts/_project/paper/main.aux:1960:\\@LN{1633}{19}\nartifacts/_project/paper/main.aux:2070:\\@LN{1733}{20}\nartifacts/_project/paper/main.aux:2191:\\@LN{1833}{22}\nartifacts/_project/paper/main.aux:2310:\\@LN{1933}{23}\nartifacts/_project/paper/acl_natbib.bst:36: % \\ProvidesFile{merlin.mbs}[2011/11/18 4.33 (PWD, AO, DPC)]\nartifacts/_project/paper/appendix_robustness.tex:42:DS & Imp & 0.15 & 0.391 & 0.391 & 0.393 & 496 & 433 \\\\\nartifacts/_project/paper/appendix_robustness.tex:43:DS & Imp & 0.20 & 1.215 & 1.215 & 1.235 & 496 & 433 \\\\\nartifacts/_project/paper/appendix_robustness.tex:44:DS & Imp & 0.25 & 3.986 & 3.986 & 4.017 & 496 & 433 \\\\\nartifacts/_project/paper/appendix_robustness.tex:45:DS & Imp & 0.30 & 8.481 & 8.481 & 8.420 & 496 & 433 \\\\\nartifacts/_project/paper/appendix_robustness.tex:47:DS & Rand & 0.15 & 0.014 & 0.014\\textsuperscript{ns} & 0.012\\textsuperscript{ns} & 496 & 433 \\\\\nartifacts/_project/paper/appendix_robustness.tex:48:DS & Rand & 0.20 & 0.031\\textsuperscript{ns} & 0.031\\textsuperscript{ns} & 0.023\\textsuperscript{ns} & 496 & 433 \\\\\nartifacts/_project/paper/appendix_robustness.tex:49:DS & Rand & 0.25 & 0.257 & 0.257 & 0.190 & 496 & 433 \\\\\nartifacts/_project/paper/appendix_robustness.tex:50:DS & Rand & 0.30 & 0.510 & 0.510 & 0.410 & 496 & 433 \\\\\nartifacts/_project/paper/appendix_robustness.tex:65:The main effect of increasing mpl is reduced $n_{\\text{eff}}$: at mpl$=$20, DeepSeek retains 433/500 problems and Qwen retains 289/500 (mid-null rate rises to 71.2\\% and 84.6\\%, respectively). Despite this sample reduction, all significance conclusions hold.\nartifacts/_project/paper/appendix_robustness.tex:82:\\multirow{4}{*}{DeepSeek} & 0.15 & 0.391 & 0.491\\; $[0.44,\\; 0.70]$ & 0.505\\; $[0.33,\\; 0.71]$ \\\\\nartifacts/_project/paper/appendix_moved.tex:158:0.15 & Random     & $0.025$ & $0.436$ & $9.3 \\times 10^{-13}$ \\\\\nartifacts/_project/paper/methodology.tex:21:[Omitted long matching line]\nartifacts/_project/paper/response_letter.md:21:- **W1**: Spearman rho=1.0 downgraded to footnote; Jonckheere-Terpstra test promoted to primary dose-response statistic (z=6.2--33.7)\nartifacts/_project/paper/main.fdb_latexmk:8:  \"/usr/share/texlive/texmf-dist/fonts/tfm/adobe/helvetic/phvb8r.tfm\" 1136768653 4484 b828043cbd581d289d955903c1339981 \"\"\nartifacts/_project/paper/main.fdb_latexmk:9:  \"/usr/share/texlive/texmf-dist/fonts/tfm/adobe/times/ptmb8r.tfm\" 1136768653 4524 6bce29db5bc272ba5f332261583fee9c \"\"\nartifacts/_project/paper/main.fdb_latexmk:10:  \"/usr/share/texlive/texmf-dist/fonts/tfm/adobe/times/ptmb8t.tfm\" 1136768653 6880 f19b8995b61c334d78fc734065f6b4d4 \"\"\nartifacts/_project/paper/main.fdb_latexmk:13:  \"/usr/share/texlive/texmf-dist/fonts/tfm/adobe/times/ptmri8r.tfm\" 1136768653 4640 532ca3305aad10cc01d769f3f91f1029 \"\"\nartifacts/_project/paper/main.fdb_latexmk:25:  \"/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmmi10.tfm\" 1136768653 1528 abec98dbc43e172678c11b3b9031252a \"\"\nartifacts/_project/paper/main.fdb_latexmk:26:  \"/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmmi12.tfm\" 1136768653 1524 4414a8315f39513458b80dfc63bff03a \"\"\nartifacts/_project/paper/main.fdb_latexmk:27:  \"/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmmi6.tfm\" 1136768653 1512 f21f83efb36853c0b70002322c1ab3ad \"\"\nartifacts/_project/paper/main.fdb_latexmk:28:  \"/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmmi8.tfm\" 1136768653 1520 eccf95517727cb11801f4f1aee3a21b4 \"\"\nartifacts/_project/paper/main.fdb_latexmk:29:  \"/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmmi9.tfm\" 1136768653 1524 d89e2d087a9828407a196f428428ef4a \"\"\nartifacts/_project/paper/main.fdb_latexmk:32:  \"/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmr6.tfm\" 1136768653 1300 b62933e007d01cfd073f79b963c01526 \"\"\nartifacts/_project/paper/main.fdb_latexmk:36:  \"/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmsy6.tfm\" 1136768653 1116 933a60c408fc0a863a92debe84b2d294 \"\"\nartifacts/_project/paper/main.fdb_latexmk:46:  \"/usr/share/texlive/texmf-dist/fonts/vf/adobe/helvetic/phvb.vf\" 1136768653 1516 a73c15525916e6e96ff30639f5ddb11b \"\"\nartifacts/_project/paper/main.fdb_latexmk:51:  \"/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty\" 1576625341 40635 c40361e206be584d448876bba8a64a3b \"\"\nartifacts/_project/paper/main.fdb_latexmk:52:  \"/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\" 1576016050 33961 6b5c75130e435b2bfdb9f480a09a39f9 \"\"\nartifacts/_project/paper/main.fdb_latexmk:55:  \"/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\" 1572645307 1057 525c2192b5febbd8c1f662c9468335bb \"\"\nartifacts/_project/paper/main.fdb_latexmk:56:  \"/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty\" 1575499628 8356 7bbb2c2373aa810be568c29e333da8ed \"\"\nartifacts/_project/paper/main.fdb_latexmk:58:  \"/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty\" 1576878844 5412 d5a2436094cd7be85769db90f29250a6 \"\"\nartifacts/_project/paper/main.fdb_latexmk:61:  \"/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\" 1593379760 20089 80423eac55aa175305d35b49e04fe23b \"\"\nartifacts/_project/paper/main.fdb_latexmk:64:  \"/usr/share/texlive/texmf-dist/tex/generic/xkeyval/xkeyval.tex\" 1762376337 19299 c7c03646b32f5a7caaa137673b7e76d2 \"\"\nartifacts/_project/paper/main.fdb_latexmk:65:  \"/usr/share/texlive/texmf-dist/tex/generic/xkeyval/xkvutils.tex\" 1762376337 7787 7dfc2f158253fc82fd655393220e6620 \"\"\nartifacts/_project/paper/main.fdb_latexmk:79:  \"/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo\" 1748806692 8464 f339f4d5391fbe0425b2d94c90e6819e \"\"\nartifacts/_project/paper/main.fdb_latexmk:81:  \"/usr/share/texlive/texmf-dist/tex/latex/base/ulasy.fd\" 1738182759 2233 b5d3114ec3e0616e658a8e7b74e810f1 \"\"\nartifacts/_project/paper/main.fdb_latexmk:83:  \"/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\" 1696191071 56128 c2ccf1a29d78c33bc553880402e4fb9a \"\"\nartifacts/_project/paper/main.fdb_latexmk:86:  \"/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\" 1579991033 13886 d1306dcf79a944f6988e688c1785f9ce \"\"\nartifacts/_project/paper/main.fdb_latexmk:91:  \"/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def\" 1759176675 19626 23e2822b9b2b5005f4c549ca98b9334d \"\"\nartifacts/_project/paper/main.fdb_latexmk:94:  \"/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\" 1748806692 8118 43b99e52946c33a23f5f43b52d5cc5ec \"\"\nartifacts/_project/paper/main.fdb_latexmk:96:  \"/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx\" 1667332637 2885 9c645d672ae17285bba324998918efd8 \"\"\nartifacts/_project/paper/main.fdb_latexmk:97:  \"/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty\" 1748806692 4023 e66acf578d6b564c4670fb57ff336a7a \"\"\nartifacts/_project/paper/main.fdb_latexmk:101:  \"/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\" 1750533789 11027 0fe7ce2c6b5291fd809c2de7bbdca37e \"\"\nartifacts/_project/paper/main.fdb_latexmk:105:  \"/usr/share/texlive/texmf-dist/tex/latex/inconsolata/t1zi4.fd\" 1516054831 1021 03341d1cf7f388bbac1915f944d5d128 \"\"\nartifacts/_project/paper/main.fdb_latexmk:123:  \"/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\" 1750533675 9684 a33a14b82ce60d6e77cb9be689d79ee6 \"\"\nartifacts/_project/paper/main.fdb_latexmk:124:  \"/usr/share/texlive/texmf-dist/tex/latex/upquote/upquote.sty\" 1334873510 1048 517e01cde97c1c0baf72e69d43aa5a2e \"\"\nartifacts/_project/paper/main.fdb_latexmk:127:  \"/usr/share/texlive/texmf-dist/tex/latex/xkeyval/xkeyval.sty\" 1762376337 5006 d7e899bb5d9717c7f214e9bc0284de7b \"\"\nartifacts/_project/paper/main.fdb_latexmk:134:  \"background.tex\" 1778903870.43558 4501 6fa94f1901655336cda45eb6be308b0e \"\"",
    "numLines": 143
  }
}
```

</details>

---

### Tool call

_source line 36_

<details open><summary>🔧 Tool call — Grep · `toolu_01JtKNizSo2RtWy48yhAYcTN`</summary>

```json
{
  "pattern": "n.*=.*500|n=500",
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
  "session_id": "e127786f-a191-4d01-b58d-071eb9fc50fc",
  "uuid": "e5183b02-a898-4824-a755-25430a5c002c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T7SgjG7o71tQEkuJu69F1N",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2080,
      "cache_read_input_tokens": 55795,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2080
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

_source line 37 · 2026-05-16T22:44:45.006Z_

<details><summary>↩ Tool result · `toolu_01JtKNizSo2RtWy48yhAYcTN`</summary>

```text
artifacts/_project/paper/conclusion.tex:4:[Omitted long matching line]
artifacts/_project/paper/appendix_robustness.tex:65:The main effect of increasing mpl is reduced $n_{\text{eff}}$: at mpl$=$20, DeepSeek retains 433/500 problems and Qwen retains 289/500 (mid-null rate rises to 71.2\% and 84.6\%, respectively). Despite this sample reduction, all significance conclusions hold.
artifacts/_project/paper/appendix_robustness.tex:147:[Omitted long matching line]
artifacts/_project/paper/appendix_robustness.tex:150:The direct $\kappa$ validation ($\kappa{=}0.88$, $n{=}48$) is limited to DeepSeek-R1-Distill-Qwen-7B on GSM8K; MATH-500 has only indirect (temporal ordering) validation. Qwen2.5-7B-Instruct does not produce explicit reasoning delimiters, precluding direct $\kappa$ validation on either benchmark. Phase segmentation is computed on the dense model's attention patterns and is independent of sparsity level, so the agreement statistics are reported once rather than per-$s$.
artifacts/_project/paper/appendix_moved.tex:142:To test whether the phase-modulated severity pattern extends beyond the Qwen2 architecture, we replicate the full experiment on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, 8B parameters; $n{=}250$, MATH-500) under both importance-based and random eviction at $s \in \{0.15, 0.20, 0.25, 0.30\}$. Table~\ref{tab:llama-cross-arch} reports paired median differences and effect sizes for all 8 conditions.
artifacts/_project/paper/appendix_moved.tex:151:\caption{Cross-architecture validation: paired median difference ($\Delta$) and effect size ($d_z$) on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, $n{=}250$, MATH-500). All conditions are monotonic.}
artifacts/_project/paper/methodology.tex:21:[Omitted long matching line]
artifacts/_project/paper/response_letter.md:3:We thank the reviewers for their thorough and constructive feedback. We apologize for the delayed incorporation of n=500 crossover verification and the ThinKV attribution correction. Both analyses were completed but not reflected in the previous revision due to a process oversight. This revision fully integrates all outstanding changes.
artifacts/_project/paper/response_letter.md:5:Below we address each comment point-by-point. All data changes reference the n=500 dataset (n_eff=496 DeepSeek, n_eff=475 Qwen) unless otherwise noted.
artifacts/_project/paper/response_letter.md:12:- **N1**: Table 2 replaced with n=500 data for both DeepSeek (n=496) and Qwen (n=475); G redefined as per-problem median ratio with bootstrap CIs; QW s015 G marked "n.d." (II_high~0, CI spans zero)
artifacts/_project/paper/appendix.tex:38:[Omitted long matching line]
artifacts/_project/paper/results.tex:13:\caption{Median of per-problem paired severity differences ($\Delta$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}496$, MATH-500).}
artifacts/_project/paper/results.tex:93:Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, $n{=}250$, MATH-500) supports the generality of phase-modulated compound interaction beyond the Qwen2 architecture family. Under importance-based eviction, the paired median difference $\Delta$ rises monotonically from $0.050$ ($s{=}0.15$) to $0.695$ ($s{=}0.30$), with large effect sizes throughout ($d_z{=}0.81$--$1.15$; all $p < 10^{-29}$; Table~\ref{tab:llama-cross-arch}).
artifacts/_project/paper/results.tex:102:To assess whether phase-modulated severity persists at larger model scale within the same architecture family, we evaluate Qwen2.5-14B-Instruct on MATH-500 ($n{=}500$) at $s \in \{0.15, 0.20, 0.25, 0.30\}$.
artifacts/_project/paper/results.tex:127:[Omitted long matching line]
artifacts/_project/paper/results.tex:132:[Omitted long matching line]
artifacts/_project/paper/appendix_disc_analysis.tex:14:[Omitted long matching line]
artifacts/_project/paper/appendix_disc_analysis.tex:52:At $n{=}500$, random eviction on both models becomes significant at $s \geq 0.25$ (Qwen: $\Delta{=}0.39$, $p_{\text{Bonf}} < 10^{-10}$ at $s{=}0.25$; $\Delta{=}0.91$, $p_{\text{Bonf}} < 10^{-13}$ at $s{=}0.30$; bootstrap CIs exclude zero).
artifacts/_project/paper/appendix_disc_analysis.tex:68:[Omitted long matching line]
artifacts/_project/paper/introduction.tex:25:    \item We characterize a \textbf{phase-modulated compound severity gradient}: importance-based eviction exhibits a monotonic dose-response ($\rho{=}1.0$; $\Delta$: $0.39 \to 8.48$) with a phase gradient $2.7$--$17{\times}$ larger than random eviction where both strategies are significant ($s \geq 0.25$) on MATH-500; the gradient direction is consistent on GSM8K, while strategy specificity attenuates (\S\ref{sec:cross-benchmark}).
artifacts/_project/paper/main.aux:586:\@writefile{lot}{\contentsline {table}{\numberline {1}{\ignorespaces Median of per-problem paired severity differences ($\Delta $) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}496$, MATH-500).}}{6}{table.caption.17}\protected@file@percent }
artifacts/_project/paper/main.aux:588:\newlabel{tab:aggregate-ii}{{1}{6}{Median of per-problem paired severity differences ($\Delta $) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}496$, MATH-500)}{table.caption.17}{}}
artifacts/_project/paper/main.aux:1735:\@writefile{lot}{\contentsline {table}{\numberline {10}{\ignorespaces Cross-architecture validation: per-phase II on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, $n{=}250$, MATH-500). Low/High: ratio of low-phase to high-phase median II.}}{18}{table.caption.52}\protected@file@percent }
artifacts/_project/paper/main.aux:1736:\newlabel{tab:llama-cross-arch}{{10}{18}{Cross-architecture validation: per-phase II on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, $n{=}250$, MATH-500). Low/High: ratio of low-phase to high-phase median II}{table.caption.52}{}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e127786f-a191-4d01-b58d-071eb9fc50fc",
  "uuid": "44e89ca6-3337-4d3e-9062-7c7b61f21c7a",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "artifacts/_project/paper/conclusion.tex:4:[Omitted long matching line]\nartifacts/_project/paper/appendix_robustness.tex:65:The main effect of increasing mpl is reduced $n_{\\text{eff}}$: at mpl$=$20, DeepSeek retains 433/500 problems and Qwen retains 289/500 (mid-null rate rises to 71.2\\% and 84.6\\%, respectively). Despite this sample reduction, all significance conclusions hold.\nartifacts/_project/paper/appendix_robustness.tex:147:[Omitted long matching line]\nartifacts/_project/paper/appendix_robustness.tex:150:The direct $\\kappa$ validation ($\\kappa{=}0.88$, $n{=}48$) is limited to DeepSeek-R1-Distill-Qwen-7B on GSM8K; MATH-500 has only indirect (temporal ordering) validation. Qwen2.5-7B-Instruct does not produce explicit reasoning delimiters, precluding direct $\\kappa$ validation on either benchmark. Phase segmentation is computed on the dense model's attention patterns and is independent of sparsity level, so the agreement statistics are reported once rather than per-$s$.\nartifacts/_project/paper/appendix_moved.tex:142:To test whether the phase-modulated severity pattern extends beyond the Qwen2 architecture, we replicate the full experiment on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, 8B parameters; $n{=}250$, MATH-500) under both importance-based and random eviction at $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$. Table~\\ref{tab:llama-cross-arch} reports paired median differences and effect sizes for all 8 conditions.\nartifacts/_project/paper/appendix_moved.tex:151:\\caption{Cross-architecture validation: paired median difference ($\\Delta$) and effect size ($d_z$) on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, $n{=}250$, MATH-500). All conditions are monotonic.}\nartifacts/_project/paper/methodology.tex:21:[Omitted long matching line]\nartifacts/_project/paper/response_letter.md:3:We thank the reviewers for their thorough and constructive feedback. We apologize for the delayed incorporation of n=500 crossover verification and the ThinKV attribution correction. Both analyses were completed but not reflected in the previous revision due to a process oversight. This revision fully integrates all outstanding changes.\nartifacts/_project/paper/response_letter.md:5:Below we address each comment point-by-point. All data changes reference the n=500 dataset (n_eff=496 DeepSeek, n_eff=475 Qwen) unless otherwise noted.\nartifacts/_project/paper/response_letter.md:12:- **N1**: Table 2 replaced with n=500 data for both DeepSeek (n=496) and Qwen (n=475); G redefined as per-problem median ratio with bootstrap CIs; QW s015 G marked \"n.d.\" (II_high~0, CI spans zero)\nartifacts/_project/paper/appendix.tex:38:[Omitted long matching line]\nartifacts/_project/paper/results.tex:13:\\caption{Median of per-problem paired severity differences ($\\Delta$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}496$, MATH-500).}\nartifacts/_project/paper/results.tex:93:Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, $n{=}250$, MATH-500) supports the generality of phase-modulated compound interaction beyond the Qwen2 architecture family. Under importance-based eviction, the paired median difference $\\Delta$ rises monotonically from $0.050$ ($s{=}0.15$) to $0.695$ ($s{=}0.30$), with large effect sizes throughout ($d_z{=}0.81$--$1.15$; all $p < 10^{-29}$; Table~\\ref{tab:llama-cross-arch}).\nartifacts/_project/paper/results.tex:102:To assess whether phase-modulated severity persists at larger model scale within the same architecture family, we evaluate Qwen2.5-14B-Instruct on MATH-500 ($n{=}500$) at $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$.\nartifacts/_project/paper/results.tex:127:[Omitted long matching line]\nartifacts/_project/paper/results.tex:132:[Omitted long matching line]\nartifacts/_project/paper/appendix_disc_analysis.tex:14:[Omitted long matching line]\nartifacts/_project/paper/appendix_disc_analysis.tex:52:At $n{=}500$, random eviction on both models becomes significant at $s \\geq 0.25$ (Qwen: $\\Delta{=}0.39$, $p_{\\text{Bonf}} < 10^{-10}$ at $s{=}0.25$; $\\Delta{=}0.91$, $p_{\\text{Bonf}} < 10^{-13}$ at $s{=}0.30$; bootstrap CIs exclude zero).\nartifacts/_project/paper/appendix_disc_analysis.tex:68:[Omitted long matching line]\nartifacts/_project/paper/introduction.tex:25:    \\item We characterize a \\textbf{phase-modulated compound severity gradient}: importance-based eviction exhibits a monotonic dose-response ($\\rho{=}1.0$; $\\Delta$: $0.39 \\to 8.48$) with a phase gradient $2.7$--$17{\\times}$ larger than random eviction where both strategies are significant ($s \\geq 0.25$) on MATH-500; the gradient direction is consistent on GSM8K, while strategy specificity attenuates (\\S\\ref{sec:cross-benchmark}).\nartifacts/_project/paper/main.aux:586:\\@writefile{lot}{\\contentsline {table}{\\numberline {1}{\\ignorespaces Median of per-problem paired severity differences ($\\Delta $) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}496$, MATH-500).}}{6}{table.caption.17}\\protected@file@percent }\nartifacts/_project/paper/main.aux:588:\\newlabel{tab:aggregate-ii}{{1}{6}{Median of per-problem paired severity differences ($\\Delta $) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}496$, MATH-500)}{table.caption.17}{}}\nartifacts/_project/paper/main.aux:1735:\\@writefile{lot}{\\contentsline {table}{\\numberline {10}{\\ignorespaces Cross-architecture validation: per-phase II on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, $n{=}250$, MATH-500). Low/High: ratio of low-phase to high-phase median II.}}{18}{table.caption.52}\\protected@file@percent }\nartifacts/_project/paper/main.aux:1736:\\newlabel{tab:llama-cross-arch}{{10}{18}{Cross-architecture validation: per-phase II on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, $n{=}250$, MATH-500). Low/High: ratio of low-phase to high-phase median II}{table.caption.52}{}}",
    "numLines": 24
  }
}
```

</details>

---

### Assistant

_source line 38_

<details><summary>Logged reasoning block</summary>

```text
Now I have a complete picture. Let me compile the findings:

Key findings:
1. conclusion.tex says "n=500" but the table reference is n=496. This is explained by 4 problems being excluded.
2. paper_framing.md has several stale numbers from the old c3_llama (n=50) data that need updating to match the new n=250 data.
3. The "15-36×" in paper_framing.md is inconsistent with the "15-17×" in the tex files.


4. Several other stale values need correction: the "2.7-15×" range should be "2.7-17×", the improvement metric "0.19→0.34" is from outdated n=50 data, and there's still a reference to "n=50 限制功效" for LLaMA in RC1.
5. I'm checking for the "15-33×" the user mentioned, but I'm not finding it in the tex or paper_framing files.
6. Looking at the Jonckheere-Terpstra statistics across files—results.tex has "z=6.2--33.7" while introduction.tex consistently shows "z ≥ 6.2, p < 10^{-9}", which align properly.
7. Now verifying the abstract's Qwen ratio claim of "2.7--3.5×" against the actual data points.
8. Checking DeepSeek's "15-17×" range against the computed ratios from the data.
9. Confirming the cross-model full range spans from 2.7× to 17×, matching the stated "2.7-17×".
10. Noting a potential discrepancy with "2.7-20×" mentioned in appendix_moved.tex that needs investigation.

Now I'm looking at line 88 of that file more carefully. The text says the effect becomes significant at s ≥ 0.25 with a ratio of "2.7–20×" weaker than importance-based, but when I calculate the actual ratios from the Qwen data (2.74× and 3.47×), that doesn't match the upper bound of 20×. I'm wondering if the "20×" is referring to something else or if there's an error in the text. I'm checking the actual numbers from the paper—at s≥0.25, Qwen shows importance-based deltas of 1.07-3.16 versus random deltas of 0.39-0.91, giving ratios of 2.7-3.5×, so the "2.7-20×" range must be pulling in DeepSeek's results as well. The ratios I'm calculating for Qwen are 2.7× at s025 and 3.5× at s030, which gives a range of 2.7-3.5×, not 2.7-20×. The text explicitly compares Qwen random to Qwen importance-based, so the "20×" figure doesn't align with the actual data—this looks like an error in the source document. I'm trying different interpretations of where the 2.7-20× range comes from—comparing importance deltas across different sparsity levels to the random baseline, but the math doesn't quite line up with any single calculation. It's possible this is outdated data from an earlier version of the paper when the numbers were different. matches what the results section says, so that's the correct figure. The appendix line 88 with "2.7--20×" appears to be outdated or erroneous compared to the verified calculations in the main text. I'm spotting another inconsistency—line 88 reports the random phase gradient as 2.7–20× weaker than importance-based for Qwen, but line 100 gives 2.7–3.5× for the same comparison. The wider range likely reflects cross-model variation, but within the Qwen-specific context of line 88, the tighter 2.7–3.5× range from line 100 is the accurate figure. I should flag this discrepancy in my findings.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e127786f-a191-4d01-b58d-071eb9fc50fc",
  "uuid": "ce0f437e-97ad-4c53-af59-3f48cadecd78",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M49pwfVG6EQMk6uMWDe4Dg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14206,
      "cache_read_input_tokens": 57875,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14206
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

_source line 39_

## 一致性检查结果

### Tex 文件内部一致性

**总体：tex 文件之间高度一致。** LLaMA 数据（n=250, d_z=0.81-1.15, imp/rand ratio 2.0-2.6×）和"architecture-dependent"表述在 abstract/introduction/results/conclusion/appendix 中完全统一。

发现以下问题：

#### 问题 1: appendix_moved.tex 内部矛盾（"2.7-20×"）
- **Line 88**: "but $2.7$--$20{\times}$ weaker than importance-based"
- **Line 100** (同文件): "the random phase gradient is $2.7$--$3.5{\times}$ weaker"（带具体数字验证：0.39 vs 1.07, 0.91 vs 3.16）
- Line 100 正确。Line 88 的"20×"无法从数据验证（Qwen s025=2.7×, s030=3.5×）。

#### 问题 2: conclusion.tex "n=500" vs results.tex "n=496"
- conclusion.tex line 4: "DeepSeek, $n{=}500$"
- results.tex table 1 caption: "$n{=}496$"
- 实验入组 500，排除 4 得到 n_eff=496。Conclusion 用 500 指实验规模是可接受的，但与 results 不一致，审稿人可能注意到。

#### 问题 3: discussion.tex GSM8K "~3×" 的来源
- discussion.tex line 8: "MATH-500 ($15$--$17{\times}$) $>$ GSM8K (${\sim}3{\times}$)"
- 但 results.tex GSM8K 部分说 random 在 GSM8K 上全部 NS（CIs spanning zero）
- 若 random NS 则无法计算有意义的 imp/rand ratio。"~3×"来源不明确（可能从原始 Δ 值计算但统计无效）。

---

### paper_framing.md 与 tex 文件的不一致（需更新）

#### 问题 4（主要）: LLaMA 数据仍为旧 c3_llama n=50

paper_framing.md Core Insight:
> "imp_vs_rand d_z 0.19→0.34, 仅 s030 显著"

Tex 文件（n=250 data）:
- Random d_z = 0.41-0.46, ALL conditions p < 10^{-12}
- Imp/rand Δ ratio = 2.0-2.6×

paper_framing.md 的 "d_z 0.19→0.34, 仅 s030 显著" 是旧 n=50 数据，完全过时。

#### 问题 5: paper_framing.md "random d_z 0.35→0.44" vs tex d_z 0.41-0.46
- paper_framing.md: "random 在 LLaMA 上也显示显著 phase gradient（d_z 0.35→0.44）"
- Tex table: d_z = 0.436, 0.459, 0.424, 0.410 → range 0.41-0.46
- "0.35→0.44"不准确。

#### 问题 6: paper_framing.md "15-36×" vs tex "15-17×"
- paper_framing.md C1: "MATH-500: importance gradient 15-36× random"
- paper_framing.md RC1: "strategy ratio $15$--$36{\times}$"
- Tex 文件一致使用: "$15$--$17{\times}$"（DeepSeek），"$2.7$--$17{\times}$"（跨模型）
- 计算验证: DS s025=15.3×, DS s030=16.6× → 15-17× ✓
- **"36×"无来源**，可能是旧版计算残留。

#### 问题 7: paper_framing.md header "imp/rand 2.7-15×"
- 更新记录写 "imp/rand 2.7-15×"
- 实际: DeepSeek s030 = 16.6× ≈ 17×
- 应为 "2.7-17×"

#### 问题 8: paper_framing.md RC1 "n=50 限制功效"
- RC1: "(c) LLaMA 跨架构验证 n=50 限制功效"
- 已完成 n=250 验证（c8_llama_n250_fixed），此限制大幅缓解。

---

### 无问题确认

- "architecture-dependent" 在所有 6 个更新文件中一致使用 ✓
- DS median_diff (0.39/1.21/3.99/8.48) 全文一致 ✓
- QW median_diff (0.07/0.31/1.07/3.16) 全文一致 ✓
- LLaMA d_z=0.81-1.15 在 abstract/intro/results/conclusion/appendix 一致 ✓
- LLaMA imp/rand 2.0-2.6× 在所有位置一致 ✓
- 无遗留的旧 "pilot n=50" 数据出现在主文 tex 文件中（profiling subset n=50 有正确标注） ✓
- Cohen's d 数字 (DS 0.94, QW 0.92) 一致 ✓

---

### paper_framing.md 草拟更新

需要更新的部分：

**Core Insight 段落中的 LLaMA 部分，替换为：**

> LLaMA 跨架构验证（D060, c8_llama_n250_fixed）qualitative direction consistent（within-importance d_z=0.81-1.15, all p<10^-29），且 random 在 LLaMA 上所有条件均显著（d_z=0.41-0.46, all p<10^-12），imp/rand Δ ratio 仅 2.0-2.6×（vs DeepSeek 15-17×），strategy×phase 交互强度 architecture-dependent。

**C1 claim，"15-36×" 改为 "15-17×"：**

> MATH-500: importance gradient 15-17× random（DeepSeek s025-s030）

**Header 更新记录，"imp/rand 2.7-15×" 改为 "2.7-17×"**

**RC1 更新：**
- "(c) LLaMA 跨架构验证 n=50 限制功效" → "(c) LLaMA n=250 验证 strategy specificity 弱于 Qwen2 架构（2.0-2.6× vs 15-17×）"

**C8 部分，替换旧 n=50 数据描述：**

> D060 + c8_llama_n250_fixed: within-importance phase gradient 强(d_z=0.81-1.15, all p<10^-29) ✓。Random 所有条件显著(d_z=0.41-0.46, all p<10^-12)，与 DeepSeek/Qwen random 低 sparsity NS 模式定性不同。Imp/rand Δ ratio 2.0-2.6×（远低于 DS 15-17×）。n=250 功效充分。

---

### 建议修复优先级

1. **High**: paper_framing.md 的 LLaMA 数据全面更新（问题 4-8）
2. **Medium**: appendix_moved.tex line 88 的 "2.7-20×" → "2.7-3.5×"
3. **Low**: conclusion.tex "n=500" → "n=496"（或保持不变，加脚注说明）
4. **Low**: discussion.tex "~3×" GSM8K ratio 加限定语（raw magnitude comparison, random NS）

需要我执行这些修复吗？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e127786f-a191-4d01-b58d-071eb9fc50fc",
  "uuid": "3bb9e41f-bf94-4f0e-a0cb-d783d93ee1f1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M49pwfVG6EQMk6uMWDe4Dg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14206,
      "cache_read_input_tokens": 57875,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14206
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

### Task result

_source line 40_

## 一致性检查结果

### Tex 文件内部一致性

**总体：tex 文件之间高度一致。** LLaMA 数据（n=250, d_z=0.81-1.15, imp/rand ratio 2.0-2.6×）和"architecture-dependent"表述在 abstract/introduction/results/conclusion/appendix 中完全统一。

发现以下问题：

#### 问题 1: appendix_moved.tex 内部矛盾（"2.7-20×"）
- **Line 88**: "but $2.7$--$20{\times}$ weaker than importance-based"
- **Line 100** (同文件): "the random phase gradient is $2.7$--$3.5{\times}$ weaker"（带具体数字验证：0.39 vs 1.07, 0.91 vs 3.16）
- Line 100 正确。Line 88 的"20×"无法从数据验证（Qwen s025=2.7×, s030=3.5×）。

#### 问题 2: conclusion.tex "n=500" vs results.tex "n=496"
- conclusion.tex line 4: "DeepSeek, $n{=}500$"
- results.tex table 1 caption: "$n{=}496$"
- 实验入组 500，排除 4 得到 n_eff=496。Conclusion 用 500 指实验规模是可接受的，但与 results 不一致，审稿人可能注意到。

#### 问题 3: discussion.tex GSM8K "~3×" 的来源
- discussion.tex line 8: "MATH-500 ($15$--$17{\times}$) $>$ GSM8K (${\sim}3{\times}$)"
- 但 results.tex GSM8K 部分说 random 在 GSM8K 上全部 NS（CIs spanning zero）
- 若 random NS 则无法计算有意义的 imp/rand ratio。"~3×"来源不明确（可能从原始 Δ 值计算但统计无效）。

---

### paper_framing.md 与 tex 文件的不一致（需更新）

#### 问题 4（主要）: LLaMA 数据仍为旧 c3_llama n=50

paper_framing.md Core Insight:
> "imp_vs_rand d_z 0.19→0.34, 仅 s030 显著"

Tex 文件（n=250 data）:
- Random d_z = 0.41-0.46, ALL conditions p < 10^{-12}
- Imp/rand Δ ratio = 2.0-2.6×

paper_framing.md 的 "d_z 0.19→0.34, 仅 s030 显著" 是旧 n=50 数据，完全过时。

#### 问题 5: paper_framing.md "random d_z 0.35→0.44" vs tex d_z 0.41-0.46
- paper_framing.md: "random 在 LLaMA 上也显示显著 phase gradient（d_z 0.35→0.44）"
- Tex table: d_z = 0.436, 0.459, 0.424, 0.410 → range 0.41-0.46
- "0.35→0.44"不准确。

#### 问题 6: paper_framing.md "15-36×" vs tex "15-17×"
- paper_framing.md C1: "MATH-500: importance gradient 15-36× random"
- paper_framing.md RC1: "strategy ratio $15$--$36{\times}$"
- Tex 文件一致使用: "$15$--$17{\times}$"（DeepSeek），"$2.7$--$17{\times}$"（跨模型）
- 计算验证: DS s025=15.3×, DS s030=16.6× → 15-17× ✓
- **"36×"无来源**，可能是旧版计算残留。

#### 问题 7: paper_framing.md header "imp/rand 2.7-15×"
- 更新记录写 "imp/rand 2.7-15×"
- 实际: DeepSeek s030 = 16.6× ≈ 17×
- 应为 "2.7-17×"

#### 问题 8: paper_framing.md RC1 "n=50 限制功效"
- RC1: "(c) LLaMA 跨架构验证 n=50 限制功效"
- 已完成 n=250 验证（c8_llama_n250_fixed），此限制大幅缓解。

---

### 无问题确认

- "architecture-dependent" 在所有 6 个更新文件中一致使用 ✓
- DS median_diff (0.39/1.21/3.99/8.48) 全文一致 ✓
- QW median_diff (0.07/0.31/1.07/3.16) 全文一致 ✓
- LLaMA d_z=0.81-1.15 在 abstract/intro/results/conclusion/appendix 一致 ✓
- LLaMA imp/rand 2.0-2.6× 在所有位置一致 ✓
- 无遗留的旧 "pilot n=50" 数据出现在主文 tex 文件中（profiling subset n=50 有正确标注） ✓
- Cohen's d 数字 (DS 0.94, QW 0.92) 一致 ✓

---

### paper_framing.md 草拟更新

需要更新的部分：

**Core Insight 段落中的 LLaMA 部分，替换为：**

> LLaMA 跨架构验证（D060, c8_llama_n250_fixed）qualitative direction consistent（within-importance d_z=0.81-1.15, all p<10^-29），且 random 在 LLaMA 上所有条件均显著（d_z=0.41-0.46, all p<10^-12），imp/rand Δ ratio 仅 2.0-2.6×（vs DeepSeek 15-17×），strategy×phase 交互强度 architecture-dependent。

**C1 claim，"15-36×" 改为 "15-17×"：**

> MATH-500: importance gradient 15-17× random（DeepSeek s025-s030）

**Header 更新记录，"imp/rand 2.7-15×" 改为 "2.7-17×"**

**RC1 更新：**
- "(c) LLaMA 跨架构验证 n=50 限制功效" → "(c) LLaMA n=250 验证 strategy specificity 弱于 Qwen2 架构（2.0-2.6× vs 15-17×）"

**C8 部分，替换旧 n=50 数据描述：**

> D060 + c8_llama_n250_fixed: within-importance phase gradient 强(d_z=0.81-1.15, all p<10^-29) ✓。Random 所有条件显著(d_z=0.41-0.46, all p<10^-12)，与 DeepSeek/Qwen random 低 sparsity NS 模式定性不同。Imp/rand Δ ratio 2.0-2.6×（远低于 DS 15-17×）。n=250 功效充分。

---

### 建议修复优先级

1. **High**: paper_framing.md 的 LLaMA 数据全面更新（问题 4-8）
2. **Medium**: appendix_moved.tex line 88 的 "2.7-20×" → "2.7-3.5×"
3. **Low**: conclusion.tex "n=500" → "n=496"（或保持不变，加脚注说明）
4. **Low**: discussion.tex "~3×" GSM8K ratio 加限定语（raw magnitude comparison, random NS）

需要我执行这些修复吗？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 232399,
  "duration_api_ms": 233282,
  "num_turns": 14,
  "stop_reason": "end_turn",
  "session_id": "e127786f-a191-4d01-b58d-071eb9fc50fc",
  "total_cost_usd": 0.8045885,
  "usage": {
    "input_tokens": 11,
    "cache_creation_input_tokens": 60240,
    "cache_read_input_tokens": 247635,
    "output_tokens": 12118,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 60240,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 5238,
        "cache_read_input_tokens": 57875,
        "cache_creation_input_tokens": 14206,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 14206
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1181,
      "outputTokens": 17,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001266,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 11,
      "outputTokens": 12118,
      "cacheReadInputTokens": 247635,
      "cacheCreationInputTokens": 60240,
      "webSearchRequests": 0,
      "costUSD": 0.8033224999999999,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "fdcacff1-dbcc-4a13-b51e-8761ab7138cb"
}
```

</details>

---
