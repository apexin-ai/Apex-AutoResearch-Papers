# paper related work

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/workers/worker_paper_related_work_20260515T233455.log`
- **Structured JSON:** [`7147316c2e0b14726aca.json`](../../sessions/71/7147316c2e0b14726aca.json)

## Before a recorded user message

35 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "session_id": "6b846b79-5ede-4f4c-b716-29d3245fa231",
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
  "uuid": "eeb33b26-865a-448b-82fa-6b99a13e3c6d",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/memory/"
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
    "resetsAt": 1778905200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "28701da5-6008-499f-9bf0-2f5858b9fcdc",
  "session_id": "6b846b79-5ede-4f4c-b716-29d3245fa231"
}
```

---

### Assistant

_source line 4_

I'll start by reading the existing project files to understand the paper's framing and method details before writing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6b846b79-5ede-4f4c-b716-29d3245fa231",
  "uuid": "5e312aec-5e91-4412-8d79-3552a295e827",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014mvcEDZgpR4jTQYTaZXDc2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12375,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12375
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_016wee5fimztrUzwU8T2HJZ5`</summary>

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
  "session_id": "6b846b79-5ede-4f4c-b716-29d3245fa231",
  "uuid": "a34926dc-8efc-4078-9f21-492879e13750",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014mvcEDZgpR4jTQYTaZXDc2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12375,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12375
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

_source line 6 · 2026-05-15T23:35:05.654Z_

<details><summary>↩ Tool result · `toolu_016wee5fimztrUzwU8T2HJZ5`</summary>

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
  "session_id": "6b846b79-5ede-4f4c-b716-29d3245fa231",
  "uuid": "a5e2cc8f-c2d6-4da6-b9dd-dbd833840eda",
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

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Let me read the paper framing, literature map, and writing plan to understand the context before writing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6b846b79-5ede-4f4c-b716-29d3245fa231",
  "uuid": "571092fa-5b69-403c-950b-90ab95eb64f7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016YPGxu9Tvojy4syAp7yVrq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 722,
      "cache_read_input_tokens": 23822,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 722
      },
      "output_tokens": 36,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01GVRviTzCno6RST15oxfp8f`</summary>

```json
{
  "project": "provenance_weight_training",
  "file": "paper_framing.md",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6b846b79-5ede-4f4c-b716-29d3245fa231",
  "uuid": "dd57697d-06ae-4796-92cd-9449735e232f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016YPGxu9Tvojy4syAp7yVrq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 722,
      "cache_read_input_tokens": 23822,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 722
      },
      "output_tokens": 36,
      "service_tier": "standard",
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

_source line 9 · 2026-05-15T23:35:10.931Z_

<details><summary>↩ Tool result · `toolu_01GVRviTzCno6RST15oxfp8f`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper_framing.md\", \"content\": \"# Paper Framing — provenance_weight_training\\n\\n> 状态: STABLE (D023 dual-constraint + D029 ESS-only resolved + D035 τ sweep complete)\\n> 最后更新: 2026-05-15 21:30 UTC\\n> 投稿目标: EMNLP 2026 ARR May 25\\n\\n## Core Insight\\n\\nWeb 语料预训练面临合成数据污染问题（20-60%，来源未知），Drayson et al. (EMNLP 2025) 提出 w=(1-q)^b detect-and-reweight 框架，但 b 需要 per-model validation-based grid search（GPT-2/SmolLM ≤360M 用 b=10，SmolLM 1.7B 用 b=1）。\\n\\n我们提出 **dual-constrained adaptive b***：per-batch 从 q-score 分布推导最优 b*，同时满足两个约束：\\n- **α_eff(b) ≥ τ** — 质量下界：确保加权后有效真实率达到收敛理论要求的阈值（\\\"至少做够清洁\\\"）\\n- **ESS(b) ≥ n_min** — 稳定上界：确保有效样本量不低于 Kish 阈值（\\\"不要清洁过头\\\"）\\n\\nb* = inf{b ≥ 0 : α_eff(b) ≥ τ} subject to ESS(b) ≥ n_min — **最小干预准则**：在保证质量的前提下，使用最少的 downweighting。\\n\\n**关键洞察**：α_eff(b) 单调递增、ESS(b) 单调递减。α_eff 给出 b 的下界 b_τ（需至少这么多清洁），ESS 给出 b 的上界 b_ESS（最多这么多清洁）。当 b_τ < b_ESS（~40% reweighted batches），α_eff 是 binding constraint，b* 远小于 ESS 上界（mean 1.67 vs 4.15）——方法选择保守干预而非最大干预。\\n\\n实现路径：**直接 loss reweighting**（gradient 层面连续加权），vs Drayson 的 SIR resampling（离散重采样）。\\n\\n### α_eff(b) 的角色（D023 修正定论）\\n\\n**D021 证明 α_eff(b) 严格单调递增**（dα_eff/db = Cov_w(x, ln x) ≥ 0）——这是正确的。\\n\\n**D021 的错误推论**：\\\"因此 α_eff 优化等价于 ESS 阈值化\\\"——这假设优化目标是 max α_eff(b) s.t. ESS ≥ n_min。但实际优化是 **inf{b : α_eff(b) ≥ τ}**——最小满足质量阈值的 b。单调性恰恰保证了 b_τ 的**存在性和唯一性**。\\n\\n**Q1 实证（Reviewer 独立核实）**：\\n- 51,913 micro-batches 中，49.9% clean (b*=0), 20.2% α_eff binding, 30.0% ESS binding\\n- 在需 reweighting 的 batch 中：40.1% α_eff binding, 59.9% ESS binding\\n- α_eff binding 时 b*=1.67，ESS-only 方法会选 b*=4.15（2.5× 更激进）\\n- α_eff binding 时 ESS=2.60（vs n_min=2.0，有 30% 余量）\\n\\n**论文呈现**：α_eff 是方法的核心组件（非仅 motivation），提供质量阈值约束。Figure: 双轴图展示 α_eff(b) 和 ESS(b) 曲线 + b_τ 和 b_ESS 标注。\\n\\n**τ 的定位（D025 定论 + D035 τ sweep 完整数据更新）**：收敛理论 (arXiv 2602.16065) 中 α = m₁/(m₁+m₂) 是已知设计参数，推导依赖已知比例。τ **不能声称有 proportion-free 的理论推导**。正确定位：empirical hyperparameter with theoretical motivation——收敛理论解释了\\\"为什么需要质量阈值\\\"（α 越高收敛越快），但 τ 的特定值由经验确定。\\n\\n**τ sweep 完整结果（6 点，seed42，ρ=0.4）**：\\n\\n| τ | PPL | Δ vs uniform (17.694) | b* mean | conclusion |\\n|---|-----|----------------------|---------|------------|\\n| 0.50 | 17.688 | −0.006 | 0.39 | success |\\n| 0.60 | 17.681 | −0.013 | 0.59 | success |\\n| 0.70 | 17.679 | −0.015 | 0.89 | success |\\n| **0.80** | **17.653** | **−0.041** | **1.40** | **best** |\\n| 0.90 | 17.712 | +0.018 | 2.36 | negative |\\n| 0.95 | 17.723 | +0.029 | 3.08 | negative |\\n\\n**关键洞察**：(1) [0.5, 0.8] 全部 beat uniform，safe range 内 PPL 差异仅 0.035；(2) τ=0.8 是最优默认值；(3) τ>0.8 因 b* 膨胀导致过度 downweighting 而退化（asymmetric sensitivity）；(4) b* 与 τ 严格单调递增，机制清晰——τ 越高要求越严，solver 被迫推高 b*。不能说\\\"τ 不敏感\\\"，正确表述：\\\"wide safe range [0.5, 0.8] with principled default τ=0.8\\\"。\\n\\n**ESS-only baseline 已验证 (D029)**：ESS-only PPL=17.728（+0.034 vs uniform，+0.076 vs adaptive_fix）——max-intervention 退化确认，min-intervention (dual) 明确优于 max-intervention (ESS-only)。ess_only_seed123/456 跨 seed 验证进行中。\\n\\n## Positioning vs Prior Work\\n\\n### Drayson et al. (EMNLP 2025) — 最近相关工作\\n\\n**共同点**：同一加权公式 w=(1-q)^b，detect-and-reweight 范式。\\n\\n**关键区分**：\\n\\n| 维度 | Drayson et al. | Ours |\\n|------|---------------|------|\\n| **b 选择** | 验证集 empirical 选取，训练中固定 | α_eff + ESS 双重约束自适应推导，per-batch 动态 |\\n| **干预原则** | 无原则（b 是超参数） | 最小干预（inf{b : α_eff ≥ τ}，只做必要的清洁） |\\n| **实现路径** | SIR resampling（离散重采样） | Loss reweighting（连续梯度加权） |\\n| **污染设置** | 不假设已知比例，但 b 依赖 validation set | 仅需 detector scores，无 validation set |\\n| **检测器** | ModernBERT 150M (AUC=0.986) | TF-IDF + LR (AUC=0.939)，轻量即可 |\\n| **训练场景** | 递归训练 model collapse prevention | Web corpus 一次性预训练 |\\n| **数据规模** | WikiText-2 (~2M tokens) | FineWeb subset (132M+ tokens) |\\n| **validation 成本** | 需 per-model validation run | 零额外 validation cost |\\n\\n**定位原则：complementary approaches for different settings。**\\n\\n### Golden Ratio Weighting (arXiv 2502.18049, 2025)\\n理论最优 w*=1/φ，但假设已知 real/synthetic 比例 k。作为 oracle baseline。\\n\\n### 其他相关工作\\n- **Strong Model Collapse (ICLR 2025)** — 理论动机：微量合成数据即致 collapse\\n- **Dynamic Loss-Based Reweighting (ICLR 2025)** — 按 loss 加权（不使用 detector score），互补\\n- **SoftDedup (ACL 2024)** — 基于重复度的 soft reweighting\\n- **DoReMi / DSIR (NeurIPS 2023)** — 域级优化 vs 我们的实例级\\n- **Beyond Model Collapse / Verification (NeurIPS 2025)** — verifier-based prevention\\n- **PSIS (Pareto Smoothed IS)** — 重要性采样诊断，Kish's ESS 理论来源\\n- **arXiv 2602.16065** — α_eff 质量阈值 τ 的收敛理论来源\\n\\n## Core Claims\\n\\n### Claim 1 (Primary): Dual-Constrained Adaptive b* — Minimum Intervention Principle\\n\\nα_eff + ESS 双重约束的 adaptive b*，提供 contamination-aware reweighting 中权重指数的 **principled 推导**，替代 Drayson et al. 的 per-model empirical grid search。\\n\\n- **方法核心**：b* = inf{b ≥ 0 : α_eff(b) ≥ τ} s.t. ESS(b) ≥ n_min。两个约束分别提供 b 的下界（质量）和上界（稳定），b* 是最小满足质量阈值的可行解\\n- **最小干预原则**：不 downweight 更多于必要——在 ~40% reweighted batch 中，b* 仅为 ESS-only 上界的 45%，保留显著更多有效样本\\n- **差异化**：Drayson 的 b 是超参数（需 validation + grid search）；我们的 b* 是双约束下的自适应推导\\n- **证据需求**：(a) α_eff binding 比例统计 (✓ Q1); (b) ESS-only baseline head-to-head 对比（证明 min > max intervention）; (c) b* 轨迹分析\\n- **理论 motivation**：α_eff(b) 单调性保证 b_τ 唯一存在；收敛理论为 τ 选择提供指导\\n\\n### Claim 2 (Primary): Adaptive b* 免调参即匹配 Grid-best\\n\\nAdaptive b* 在零超参调优下达到 grid-search 最优同等水平（within seed variance），消除 grid search 的计算开销（6N → 1 runs）。\\n\\n- **MVP 证据**: adaptive_fix ×3 seeds vs grid-b ×3 seeds（40% 污染, Qwen3-0.6B, 200M tokens）\\n- **状态**: ✅ MVP Path B PASS (D019: aggregate 88.6%, 三支柱论证)\\n\\n**叙事弹性**：\\n- 核心表述：**\\\"adaptive matches grid-best within seed variance\\\"**\\n- 补充表述：**\\\"eliminates grid search cost (6N → 1 runs)\\\"** + **\\\"consistent improvement across all seeds\\\"**\\n\\n**MVP 数据**：\\n\\n| Metric | seed42 | seed123 | seed456 |\\n|--------|--------|---------|---------|\\n| Uniform PPL | 17.690 | 17.690 | 17.700 |\\n| Grid-best PPL (b=0.5) | 17.651 | 17.638 | 17.650 |\\n| Adaptive_fix PPL | 17.650 | 17.643 | 17.660 |\\n| Ratio | 102.6% | 90.4% | 80.0% |\\n\\nAggregate ratio: 88.6% (D019). Path B PASS.\\n\\n### Claim 3 (Setting): Unknown Contamination Proportion\\n\\n方法仅需 detector scores，无需已知污染比例、无需 clean validation set。\\n\\n- **差异化**：Golden Ratio 需已知比例 k；Drayson 的 b 依赖 validation set；我们仅需 per-sample q-scores\\n- **实际意义**：web-scale pretraining 中污染比例本质不可知\\n- **D021 代码修复**: ✅ τ = 0.8 固定 CLI 参数，不依赖 contamination_ratio\\n- **D025 理论审计**: arXiv 2602.16065 的 α 是已知比例，τ 不能声称有 proportion-free 理论推导。τ 定位为 empirical hyperparameter with theoretical motivation\\n- **D035 τ sweep 完整数据 (6 点)**：[0.5, 0.8] 为 safe range（all beat uniform，PPL 差异 <0.035），τ=0.8 为最优默认值；τ>0.8 因 b* 膨胀退化。正确表述：\\\"wide safe range with principled default\\\"，不说\\\"insensitive\\\"\\n- **Claim 3 核心仍成立**：b* 推导不需要已知比例（ESS 和 α_eff 从 batch 统计量计算），方法运行时不访问 contamination_ratio。τ 在 [0.5, 0.8] 范围内是 robust empirical default，类似于 learning rate warmup steps——有理论 motivation 但具体值凭经验，且有明确的有效范围上界\\n\\n## Ancillary Finding: Lightweight Detector Sufficiency\\n\\nTF-IDF + LR (AUC=0.939) 即可支撑有效的 adaptive reweighting，不需要 ModernBERT 级别的强检测器（Drayson 用 AUC=0.986）。q-score 的连续性（calibration）比分类精度（AUC）更重要。\\n\\n可升级为 co-primary contribution 如果 detector quality ablation 显示明确的 \\\"sufficiency threshold\\\"。\\n\\n## n_min Robustness Framing\\n\\nESS 约束的 n_min 是 adaptive b* 的超参数之一（另一个是 τ）。\\n\\n- n_min=3 at batch_size=4 → ESS 约束过紧，b* 被钳制在低值，seed42 零改善\\n- n_min=2 at batch_size=4 → 稳定工作，3/3 seeds positive\\n- **论文呈现**：n_min sensitivity curve (n_min=1,2,3,4,5) + batch_size 消融 (4,8,16) 证明 knife-edge 是 batch_size=4 的 artifact\\n\\n## Narrative Structure\\n\\n**起点**: Web 语料 20-60% 为合成文本，比例未知——Strong Model Collapse (ICLR 2025) 证明微量污染即破坏 scaling law。\\n\\n**现有方法不足**：Drayson 的 b 依赖 per-model validation（不同模型需不同 b），Golden Ratio 假设已知混合比例。\\n\\n**我们的方案**: Dual-constrained adaptive b*——α_eff 确保 \\\"至少做够清洁\\\"，ESS 确保 \\\"不要清洁过头\\\"，b* 是满足质量阈值的最小干预。\\n\\n**方法直觉**：想象一个旋钮 b 控制去污力度。α_eff 告诉你\\\"至少拧到这里才够干净\\\"（质量下界），ESS 告诉你\\\"再拧就会丢太多有效数据\\\"（稳定上界）。方法选择旋钮的最小有效位置——刚好够干净，不多不少。\\n\\n**α_eff 的贡献**：不是\\\"α_eff vs ESS 哪个更重要\\\"，而是双约束共同构成最小干预准则。在 ~40% reweighted batch 中，α_eff 是 binding constraint（b* 远低于 ESS 上界）——如果没有 α_eff，方法会过度 downweight，浪费有效样本。\\n\\n**实验验证**：(a) adaptive vs grid-best within seed variance; (b) adaptive vs ESS-only baseline（证明 min-intervention > max-intervention）; (c) τ/n_min sensitivity; (d) batch_size 消融。\\n\\n## Contribution Structure (D023 reframed)\\n\\n1. **Primary — Method**: Dual-constrained adaptive b*（α_eff 质量下界 + ESS 稳定上界 → 最小干预准则），零 validation cost 的 per-batch 自适应 b 推导，替代 per-model grid search。\\n2. **Primary — Empirical Finding**: (a) Adaptive b* 免调参匹配 grid-best within seed variance; (b) 轻量检测器 (TF-IDF+LR, AUC=0.939) 即可支撑有效重加权; (c) min-intervention 优于 max-intervention（需 ESS-only baseline 验证）。\\n3. **Setting — Unknown Proportion**: 仅需 detector scores，无需已知比例或 validation set（τ 修复后）。\\n\\n**α_eff 是方法的核心组件**，提供质量约束和最小干预语义。收敛理论作为 τ 选择的 motivation。\\n\\n## Anticipated Reviewer Concerns\\n\\n| Concern | Response Strategy | 实验支撑 |\\n|---------|------------------|----------|\\n| \\\"Incremental over Drayson\\\" | 差异化: adaptive b* (zero validation) vs per-model empirical b; min-intervention principle; loss reweighting vs SIR | Claim 1 + Claim 3 + ESS-only baseline |\\n| \\\"α_eff monotone → just ESS thresholding?\\\" | inf{b} vs max{b} 区分: 最小干预 vs 最大干预。Q1 实证: 40% α_eff binding, b* = 1.67 vs ESS-only 4.15。ESS-only baseline 对比训练结果 | ESS-only baseline + Q1 figure |\\n| \\\"Small effect size (~0.3% PPL)\\\" | claim 聚焦免调参+方法正确性; 60% 污染+3B 模型放大; zero-cost advantage | p0_contamination_60 + p0_llama3b |\\n| \\\"Two hyperparameters (τ, n_min) vs one (b)\\\" | 关键区别：τ 在 [0.5,0.8] 有效（sweep 6 点验证），n_min=2 跨 3 seed 稳定。两个 HP 都有明确 safe range + principled default，设一次即可跨数据集；Drayson 的 b 需 per-model per-dataset validation。2 个 robust defaults 替代 1 个 sensitive HP | p0_nmin_* + p0_tau_sweep ✅ + p0_batchsize_* |\\n| \\\"Only 0.6B model\\\" | Limitations 诚实说明；batch_size 消融间接展示方法在不同 ESS 范围下的稳健性（bs=4→16 相当于模拟不同 scale 的 batch 统计行为）；Llama-3B 列为 P1 如有 GPU 余量补做 | p0_batchsize_* + p1_llama3b_adaptive |\\n| \\\"Detector quality sensitivity\\\" | TF-IDF+LR 即可; calibration > AUC | p1_detector_ablation |\\n| \\\"Controlled injection ≠ real web\\\" | domain-skewed + semi-realistic | p2_domain_skewed |\\n| \\\"τ comes from contamination_ratio?\\\" | τ 代码已独立 (D021 fix); 收敛理论 α 确实依赖已知比例 (D025)，诚实说明 τ 是 empirical default with theoretical motivation; τ sweep 6 点完整数据证明 [0.5,0.8] safe range + principled default τ=0.8 | p0_tau_fix ✅ + p0_tau_sweep ✅ |\\n\\n## Key Risks\\n\\n1. **~~ESS-only baseline 可能同样好~~** ✅ **RESOLVED (D029)**: ESS-only PPL=17.728（比 uniform 差 +0.034，比 adaptive 差 +0.076）——max-intervention 明确退化。结果落在\\\"dual > ESS-only\\\"理想区间：min-intervention principle 有可量化的性能优势。跨 seed 验证 (ess_only_seed123/456) 进行中\\n2. **Novelty risk (D013)**: 基础公式来自 Drayson，双约束框架新颖性需充分论证。**应对**: 差异化锚定在 min-intervention principle + zero validation cost\\n3. **~~τ 修复后性能变化~~** ✅ **RESOLVED (D035)**: τ sweep 6 点完成。[0.5, 0.8] safe range 全部 beat uniform；τ=0.8 最优；τ>0.8 退化但机制清晰（b* 膨胀）。方法 robust in practical range\\n4. **~~τ 理论来源依赖已知比例~~** ✅ **RESOLVED (D025+D035)**: τ 定位为 empirical HP with theoretical motivation。τ sweep 提供完整 empirical justification，Claim 3 核心不受影响\\n5. **效应量小**: **应对**: 60% 污染 + 3B 模型放大; zero-cost advantage framing\\n6. **Venue fit**: 核心偏 ML，EMNLP reviewer 可能低估。**应对**: NLP-specific analysis\\n\\n## MVP → Full Paper 扩展路径\\n\\n| 维度 | MVP | Full Paper |\\n|------|-----|-----------|\\n| 污染比例 | 40% | 20%, 40%, 60% |\\n| 模型 | Qwen3-0.6B | + Llama-3.2-3B |\\n| 生成器 | Qwen3-0.6B (self) | + Llama-3.2-1B, Mistral, Gemma |\\n| 检测器 | TF-IDF + LR | + ModernBERT variants (quality ablation) |\\n| Baseline | uniform, grid-b, adaptive | + ESS-only adaptive, Golden Ratio, detect-and-remove, random reweight |\\n| 评估 | eval_ppl | + MMLU, HellaSwag, Self-BLEU, distinct-n |\\n| 注入方式 | uniform random | + domain-skewed, semi-realistic |\\n| n_min 分析 | n_min=2 vs n_min=3 | + n_min=1,4,5 + batch_size=4,8,16 |\\n| τ 分析 | 无 | ✅ τ sweep (6 点) + ESS-only vs dual-constraint 对比 |\\n\", \"total_chars\": 11323, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6b846b79-5ede-4f4c-b716-29d3245fa231",
  "uuid": "c80c9f34-e71a-4f7f-a80a-5b0099dfa14c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing — provenance_weight_training\\\\n\\\\n> 状态: STABLE (D023 dual-constraint + D029 ESS-only resolved + D035 τ sweep complete)\\\\n> 最后更新: 2026-05-15 21:30 UTC\\\\n> 投稿目标: EMNLP 2026 ARR May 25\\\\n\\\\n## Core Insight\\\\n\\\\nWeb 语料预训练面临合成数据污染问题（20-60%，来源未知），Drayson et al. (EMNLP 2025) 提出 w=(1-q)^b detect-and-reweight 框架，但 b 需要 per-model validation-based grid search（GPT-2/SmolLM ≤360M 用 b=10，SmolLM 1.7B 用 b=1）。\\\\n\\\\n我们提出 **dual-constrained adaptive b***：per-batch 从 q-score 分布推导最优 b*，同时满足两个约束：\\\\n- **α_eff(b) ≥ τ** — 质量下界：确保加权后有效真实率达到收敛理论要求的阈值（\\\\\\\"至少做够清洁\\\\\\\"）\\\\n- **ESS(b) ≥ n_min** — 稳定上界：确保有效样本量不低于 Kish 阈值（\\\\\\\"不要清洁过头\\\\\\\"）\\\\n\\\\nb* = inf{b ≥ 0 : α_eff(b) ≥ τ} subject to ESS(b) ≥ n_min — **最小干预准则**：在保证质量的前提下，使用最少的 downweighting。\\\\n\\\\n**关键洞察**：α_eff(b) 单调递增、ESS(b) 单调递减。α_eff 给出 b 的下界 b_τ（需至少这么多清洁），ESS 给出 b 的上界 b_ESS（最多这么多清洁）。当 b_τ < b_ESS（~40% reweighted batches），α_eff 是 binding constraint，b* 远小于 ESS 上界（mean 1.67 vs 4.15）——方法选择保守干预而非最大干预。\\\\n\\\\n实现路径：**直接 loss reweighting**（gradient 层面连续加权），vs Drayson 的 SIR resampling（离散重采样）。\\\\n\\\\n### α_eff(b) 的角色（D023 修正定论）\\\\n\\\\n**D021 证明 α_eff(b) 严格单调递增**（dα_eff/db = Cov_w(x, ln x) ≥ 0）——这是正确的。\\\\n\\\\n**D021 的错误推论**：\\\\\\\"因此 α_eff 优化等价于 ESS 阈值化\\\\\\\"——这假设优化目标是 max α_eff(b) s.t. ESS ≥ n_min。但实际优化是 **inf{b : α_eff(b) ≥ τ}**——最小满足质量阈值的 b。单调性恰恰保证了 b_τ 的**存在性和唯一性**。\\\\n\\\\n**Q1 实证（Reviewer 独立核实）**：\\\\n- 51,913 micro-batches 中，49.9% clean (b*=0), 20.2% α_eff binding, 30.0% ESS binding\\\\n- 在需 reweighting 的 batch 中：40.1% α_eff binding, 59.9% ESS binding\\\\n- α_eff binding 时 b*=1.67，ESS-only 方法会选 b*=4.15（2.5× 更激进）\\\\n- α_eff binding 时 ESS=2.60（vs n_min=2.0，有 30% 余量）\\\\n\\\\n**论文呈现**：α_eff 是方法的核心组件（非仅 motivation），提供质量阈值约束。Figure: 双轴图展示 α_eff(b) 和 ESS(b) 曲线 + b_τ 和 b_ESS 标注。\\\\n\\\\n**τ 的定位（D025 定论 + D035 τ sweep 完整数据更新）**：收敛理论 (arXiv 2602.16065) 中 α = m₁/(m₁+m₂) 是已知设计参数，推导依赖已知比例。τ **不能声称有 proportion-free 的理论推导**。正确定位：empirical hyperparameter with theoretical motivation——收敛理论解释了\\\\\\\"为什么需要质量阈值\\\\\\\"（α 越高收敛越快），但 τ 的特定值由经验确定。\\\\n\\\\n**τ sweep 完整结果（6 点，seed42，ρ=0.4）**：\\\\n\\\\n| τ | PPL | Δ vs uniform (17.694) | b* mean | conclusion |\\\\n|---|-----|----------------------|---------|------------|\\\\n| 0.50 | 17.688 | −0.006 | 0.39 | success |\\\\n| 0.60 | 17.681 | −0.013 | 0.59 | success |\\\\n| 0.70 | 17.679 | −0.015 | 0.89 | success |\\\\n| **0.80** | **17.653** | **−0.041** | **1.40** | **best** |\\\\n| 0.90 | 17.712 | +0.018 | 2.36 | negative |\\\\n| 0.95 | 17.723 | +0.029 | 3.08 | negative |\\\\n\\\\n**关键洞察**：(1) [0.5, 0.8] 全部 beat uniform，safe range 内 PPL 差异仅 0.035；(2) τ=0.8 是最优默认值；(3) τ>0.8 因 b* 膨胀导致过度 downweighting 而退化（asymmetric sensitivity）；(4) b* 与 τ 严格单调递增，机制清晰——τ 越高要求越严，solver 被迫推高 b*。不能说\\\\\\\"τ 不敏感\\\\\\\"，正确表述：\\\\\\\"wide safe range [0.5, 0.8] with principled default τ=0.8\\\\\\\"。\\\\n\\\\n**ESS-only baseline 已验证 (D029)**：ESS-only PPL=17.728（+0.034 vs uniform，+0.076 vs adaptive_fix）——max-intervention 退化确认，min-intervention (dual) 明确优于 max-intervention (ESS-only)。ess_only_seed123/456 跨 seed 验证进行中。\\\\n\\\\n## Positioning vs Prior Work\\\\n\\\\n### Drayson et al. (EMNLP 2025) — 最近相关工作\\\\n\\\\n**共同点**：同一加权公式 w=(1-q)^b，detect-and-reweight 范式。\\\\n\\\\n**关键区分**：\\\\n\\\\n| 维度 | Drayson et al. | Ours |\\\\n|------|---------------|------|\\\\n| **b 选择** | 验证集 empirical 选取，训练中固定 | α_eff + ESS 双重约束自适应推导，per-batch 动态 |\\\\n| **干预原则** | 无原则（b 是超参数） | 最小干预（inf{b : α_eff ≥ τ}，只做必要的清洁） |\\\\n| **实现路径** | SIR resampling（离散重采样） | Loss reweighting（连续梯度加权） |\\\\n| **污染设置** | 不假设已知比例，但 b 依赖 validation set | 仅需 detector scores，无 validation set |\\\\n| **检测器** | ModernBERT 150M (AUC=0.986) | TF-IDF + LR (AUC=0.939)，轻量即可 |\\\\n| **训练场景** | 递归训练 model collapse prevention | Web corpus 一次性预训练 |\\\\n| **数据规模** | WikiText-2 (~2M tokens) | FineWeb subset (132M+ tokens) |\\\\n| **validation 成本** | 需 per-model validation run | 零额外 validation cost |\\\\n\\\\n**定位原则：complementary approaches for different settings。**\\\\n\\\\n### Golden Ratio Weighting (arXiv 2502.18049, 2025)\\\\n理论最优 w*=1/φ，但假设已知 real/synthetic 比例 k。作为 oracle baseline。\\\\n\\\\n### 其他相关工作\\\\n- **Strong Model Collapse (ICLR 2025)** — 理论动机：微量合成数据即致 collapse\\\\n- **Dynamic Loss-Based Reweighting (ICLR 2025)** — 按 loss 加权（不使用 detector score），互补\\\\n- **SoftDedup (ACL 2024)** — 基于重复度的 soft reweighting\\\\n- **DoReMi / DSIR (NeurIPS 2023)** — 域级优化 vs 我们的实例级\\\\n- **Beyond Model Collapse / Verification (NeurIPS 2025)** — verifier-based prevention\\\\n- **PSIS (Pareto Smoothed IS)** — 重要性采样诊断，Kish's ESS 理论来源\\\\n- **arXiv 2602.16065** — α_eff 质量阈值 τ 的收敛理论来源\\\\n\\\\n## Core Claims\\\\n\\\\n### Claim 1 (Primary): Dual-Constrained Adaptive b* — Minimum Intervention Principle\\\\n\\\\nα_eff + ESS 双重约束的 adaptive b*，提供 contamination-aware reweighting 中权重指数的 **principled 推导**，替代 Drayson et al. 的 per-model empirical grid search。\\\\n\\\\n- **方法核心**：b* = inf{b ≥ 0 : α_eff(b) ≥ τ} s.t. ESS(b) ≥ n_min。两个约束分别提供 b 的下界（质量）和上界（稳定），b* 是最小满足质量阈值的可行解\\\\n- **最小干预原则**：不 downweight 更多于必要——在 ~40% reweighted batch 中，b* 仅为 ESS-only 上界的 45%，保留显著更多有效样本\\\\n- **差异化**：Drayson 的 b 是超参数（需 validation + grid search）；我们的 b* 是双约束下的自适应推导\\\\n- **证据需求**：(a) α_eff binding 比例统计 (✓ Q1); (b) ESS-only baseline head-to-head 对比（证明 min > max intervention）; (c) b* 轨迹分析\\\\n- **理论 motivation**：α_eff(b) 单调性保证 b_τ 唯一存在；收敛理论为 τ 选择提供指导\\\\n\\\\n### Claim 2 (Primary): Adaptive b* 免调参即匹配 Grid-best\\\\n\\\\nAdaptive b* 在零超参调优下达到 grid-search 最优同等水平（within seed variance），消除 grid search 的计算开销（6N → 1 runs）。\\\\n\\\\n- **MVP 证据**: adaptive_fix ×3 seeds vs grid-b ×3 seeds（40% 污染, Qwen3-0.6B, 200M tokens）\\\\n- **状态**: ✅ MVP Path B PASS (D019: aggregate 88.6%, 三支柱论证)\\\\n\\\\n**叙事弹性**：\\\\n- 核心表述：**\\\\\\\"adaptive matches grid-best within seed variance\\\\\\\"**\\\\n- 补充表述：**\\\\\\\"eliminates grid search cost (6N → 1 runs)\\\\\\\"** + **\\\\\\\"consistent improvement across all seeds\\\\\\\"**\\\\n\\\\n**MVP 数据**：\\\\n\\\\n| Metric | seed42 | seed123 | seed456 |\\\\n|--------|--------|---------|---------|\\\\n| Uniform PPL | 17.690 | 17.690 | 17.700 |\\\\n| Grid-best PPL (b=0.5) | 17.651 | 17.638 | 17.650 |\\\\n| Adaptive_fix PPL | 17.650 | 17.643 | 17.660 |\\\\n| Ratio | 102.6% | 90.4% | 80.0% |\\\\n\\\\nAggregate ratio: 88.6% (D019). Path B PASS.\\\\n\\\\n### Claim 3 (Setting): Unknown Contamination Proportion\\\\n\\\\n方法仅需 detector scores，无需已知污染比例、无需 clean validation set。\\\\n\\\\n- **差异化**：Golden Ratio 需已知比例 k；Drayson 的 b 依赖 validation set；我们仅需 per-sample q-scores\\\\n- **实际意义**：web-scale pretraining 中污染比例本质不可知\\\\n- **D021 代码修复**: ✅ τ = 0.8 固定 CLI 参数，不依赖 contamination_ratio\\\\n- **D025 理论审计**: arXiv 2602.16065 的 α 是已知比例，τ 不能声称有 proportion-free 理论推导。τ 定位为 empirical hyperparameter with theoretical motivation\\\\n- **D035 τ sweep 完整数据 (6 点)**：[0.5, 0.8] 为 safe range（all beat uniform，PPL 差异 <0.035），τ=0.8 为最优默认值；τ>0.8 因 b* 膨胀退化。正确表述：\\\\\\\"wide safe range with principled default\\\\\\\"，不说\\\\\\\"insensitive\\\\\\\"\\\\n- **Claim 3 核心仍成立**：b* 推导不需要已知比例（ESS 和 α_eff 从 batch 统计量计算），方法运行时不访问 contamination_ratio。τ 在 [0.5, 0.8] 范围内是 robust empirical default，类似于 learning rate warmup steps——有理论 motivation 但具体值凭经验，且有明确的有效范围上界\\\\n\\\\n## Ancillary Finding: Lightweight Detector Sufficiency\\\\n\\\\nTF-IDF + LR (AUC=0.939) 即可支撑有效的 adaptive reweighting，不需要 ModernBERT 级别的强检测器（Drayson 用 AUC=0.986）。q-score 的连续性（calibration）比分类精度（AUC）更重要。\\\\n\\\\n可升级为 co-primary contribution 如果 detector quality ablation 显示明确的 \\\\\\\"sufficiency threshold\\\\\\\"。\\\\n\\\\n## n_min Robustness Framing\\\\n\\\\nESS 约束的 n_min 是 adaptive b* 的超参数之一（另一个是 τ）。\\\\n\\\\n- n_min=3 at batch_size=4 → ESS 约束过紧，b* 被钳制在低值，seed42 零改善\\\\n- n_min=2 at batch_size=4 → 稳定工作，3/3 seeds positive\\\\n- **论文呈现**：n_min sensitivity curve (n_min=1,2,3,4,5) + batch_size 消融 (4,8,16) 证明 knife-edge 是 batch_size=4 的 artifact\\\\n\\\\n## Narrative Structure\\\\n\\\\n**起点**: Web 语料 20-60% 为合成文本，比例未知——Strong Model Collapse (ICLR 2025) 证明微量污染即破坏 scaling law。\\\\n\\\\n**现有方法不足**：Drayson 的 b 依赖 per-model validation（不同模型需不同 b），Golden Ratio 假设已知混合比例。\\\\n\\\\n**我们的方案**: Dual-constrained adaptive b*——α_eff 确保 \\\\\\\"至少做够清洁\\\\\\\"，ESS 确保 \\\\\\\"不要清洁过头\\\\\\\"，b* 是满足质量阈值的最小干预。\\\\n\\\\n**方法直觉**：想象一个旋钮 b 控制去污力度。α_eff 告诉你\\\\\\\"至少拧到这里才够干净\\\\\\\"（质量下界），ESS 告诉你\\\\\\\"再拧就会丢太多有效数据\\\\\\\"（稳定上界）。方法选择旋钮的最小有效位置——刚好够干净，不多不少。\\\\n\\\\n**α_eff 的贡献**：不是\\\\\\\"α_eff vs ESS 哪个更重要\\\\\\\"，而是双约束共同构成最小干预准则。在 ~40% reweighted batch 中，α_eff 是 binding constraint（b* 远低于 ESS 上界）——如果没有 α_eff，方法会过度 downweight，浪费有效样本。\\\\n\\\\n**实验验证**：(a) adaptive vs grid-best within seed variance; (b) adaptive vs ESS-only baseline（证明 min-intervention > max-intervention）; (c) τ/n_min sensitivity; (d) batch_size 消融。\\\\n\\\\n## Contribution Structure (D023 reframed)\\\\n\\\\n1. **Primary — Method**: Dual-constrained adaptive b*（α_eff 质量下界 + ESS 稳定上界 → 最小干预准则），零 validation cost 的 per-batch 自适应 b 推导，替代 per-model grid search。\\\\n2. **Primary — Empirical Finding**: (a) Adaptive b* 免调参匹配 grid-best within seed variance; (b) 轻量检测器 (TF-IDF+LR, AUC=0.939) 即可支撑有效重加权; (c) min-intervention 优于 max-intervention（需 ESS-only baseline 验证）。\\\\n3. **Setting — Unknown Proportion**: 仅需 detector scores，无需已知比例或 validation set（τ 修复后）。\\\\n\\\\n**α_eff 是方法的核心组件**，提供质量约束和最小干预语义。收敛理论作为 τ 选择的 motivation。\\\\n\\\\n## Anticipated Reviewer Concerns\\\\n\\\\n| Concern | Response Strategy | 实验支撑 |\\\\n|---------|------------------|----------|\\\\n| \\\\\\\"Incremental over Drayson\\\\\\\" | 差异化: adaptive b* (zero validation) vs per-model empirical b; min-intervention principle; loss reweighting vs SIR | Claim 1 + Claim 3 + ESS-only baseline |\\\\n| \\\\\\\"α_eff monotone → just ESS thresholding?\\\\\\\" | inf{b} vs max{b} 区分: 最小干预 vs 最大干预。Q1 实证: 40% α_eff binding, b* = 1.67 vs ESS-only 4.15。ESS-only baseline 对比训练结果 | ESS-only baseline + Q1 figure |\\\\n| \\\\\\\"Small effect size (~0.3% PPL)\\\\\\\" | claim 聚焦免调参+方法正确性; 60% 污染+3B 模型放大; zero-cost advantage | p0_contamination_60 + p0_llama3b |\\\\n| \\\\\\\"Two hyperparameters (τ, n_min) vs one (b)\\\\\\\" | 关键区别：τ 在 [0.5,0.8] 有效（sweep 6 点验证），n_min=2 跨 3 seed 稳定。两个 HP 都有明确 safe range + principled default，设一次即可跨数据集；Drayson 的 b 需 per-model per-dataset validation。2 个 robust defaults 替代 1 个 sensitive HP | p0_nmin_* + p0_tau_sweep ✅ + p0_batchsize_* |\\\\n| \\\\\\\"Only 0.6B model\\\\\\\" | Limitations 诚实说明；batch_size 消融间接展示方法在不同 ESS 范围下的稳健性（bs=4→16 相当于模拟不同 scale 的 batch 统计行为）；Llama-3B 列为 P1 如有 GPU 余量补做 | p0_batchsize_* + p1_llama3b_adaptive |\\\\n| \\\\\\\"Detector quality sensitivity\\\\\\\" | TF-IDF+LR 即可; calibration > AUC | p1_detector_ablation |\\\\n| \\\\\\\"Controlled injection ≠ real web\\\\\\\" | domain-skewed + semi-realistic | p2_domain_skewed |\\\\n| \\\\\\\"τ comes from contamination_ratio?\\\\\\\" | τ 代码已独立 (D021 fix); 收敛理论 α 确实依赖已知比例 (D025)，诚实说明 τ 是 empirical default with theoretical motivation; τ sweep 6 点完整数据证明 [0.5,0.8] safe range + principled default τ=0.8 | p0_tau_fix ✅ + p0_tau_sweep ✅ |\\\\n\\\\n## Key Risks\\\\n\\\\n1. **~~ESS-only baseline 可能同样好~~** ✅ **RESOLVED (D029)**: ESS-only PPL=17.728（比 uniform 差 +0.034，比 adaptive 差 +0.076）——max-intervention 明确退化。结果落在\\\\\\\"dual > ESS-only\\\\\\\"理想区间：min-intervention principle 有可量化的性能优势。跨 seed 验证 (ess_only_seed123/456) 进行中\\\\n2. **Novelty risk (D013)**: 基础公式来自 Drayson，双约束框架新颖性需充分论证。**应对**: 差异化锚定在 min-intervention principle + zero validation cost\\\\n3. **~~τ 修复后性能变化~~** ✅ **RESOLVED (D035)**: τ sweep 6 点完成。[0.5, 0.8] safe range 全部 beat uniform；τ=0.8 最优；τ>0.8 退化但机制清晰（b* 膨胀）。方法 robust in practical range\\\\n4. **~~τ 理论来源依赖已知比例~~** ✅ **RESOLVED (D025+D035)**: τ 定位为 empirical HP with theoretical motivation。τ sweep 提供完整 empirical justification，Claim 3 核心不受影响\\\\n5. **效应量小**: **应对**: 60% 污染 + 3B 模型放大; zero-cost advantage framing\\\\n6. **Venue fit**: 核心偏 ML，EMNLP reviewer 可能低估。**应对**: NLP-specific analysis\\\\n\\\\n## MVP → Full Paper 扩展路径\\\\n\\\\n| 维度 | MVP | Full Paper |\\\\n|------|-----|-----------|\\\\n| 污染比例 | 40% | 20%, 40%, 60% |\\\\n| 模型 | Qwen3-0.6B | + Llama-3.2-3B |\\\\n| 生成器 | Qwen3-0.6B (self) | + Llama-3.2-1B, Mistral, Gemma |\\\\n| 检测器 | TF-IDF + LR | + ModernBERT variants (quality ablation) |\\\\n| Baseline | uniform, grid-b, adaptive | + ESS-only adaptive, Golden Ratio, detect-and-remove, random reweight |\\\\n| 评估 | eval_ppl | + MMLU, HellaSwag, Self-BLEU, distinct-n |\\\\n| 注入方式 | uniform random | + domain-skewed, semi-realistic |\\\\n| n_min 分析 | n_min=2 vs n_min=3 | + n_min=1,4,5 + batch_size=4,8,16 |\\\\n| τ 分析 | 无 | ✅ τ sweep (6 点) + ESS-only vs dual-constraint 对比 |\\\\n\\\", \\\"total_chars\\\": 11323, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper_framing.md\", \"content\": \"# Paper Framing — provenance_weight_training\\n\\n> 状态: STABLE (D023 dual-constraint + D029 ESS-only resolved + D035 τ sweep complete)\\n> 最后更新: 2026-05-15 21:30 UTC\\n> 投稿目标: EMNLP 2026 ARR May 25\\n\\n## Core Insight\\n\\nWeb 语料预训练面临合成数据污染问题（20-60%，来源未知），Drayson et al. (EMNLP 2025) 提出 w=(1-q)^b detect-and-reweight 框架，但 b 需要 per-model validation-based grid search（GPT-2/SmolLM ≤360M 用 b=10，SmolLM 1.7B 用 b=1）。\\n\\n我们提出 **dual-constrained adaptive b***：per-batch 从 q-score 分布推导最优 b*，同时满足两个约束：\\n- **α_eff(b) ≥ τ** — 质量下界：确保加权后有效真实率达到收敛理论要求的阈值（\\\"至少做够清洁\\\"）\\n- **ESS(b) ≥ n_min** — 稳定上界：确保有效样本量不低于 Kish 阈值（\\\"不要清洁过头\\\"）\\n\\nb* = inf{b ≥ 0 : α_eff(b) ≥ τ} subject to ESS(b) ≥ n_min — **最小干预准则**：在保证质量的前提下，使用最少的 downweighting。\\n\\n**关键洞察**：α_eff(b) 单调递增、ESS(b) 单调递减。α_eff 给出 b 的下界 b_τ（需至少这么多清洁），ESS 给出 b 的上界 b_ESS（最多这么多清洁）。当 b_τ < b_ESS（~40% reweighted batches），α_eff 是 binding constraint，b* 远小于 ESS 上界（mean 1.67 vs 4.15）——方法选择保守干预而非最大干预。\\n\\n实现路径：**直接 loss reweighting**（gradient 层面连续加权），vs Drayson 的 SIR resampling（离散重采样）。\\n\\n### α_eff(b) 的角色（D023 修正定论）\\n\\n**D021 证明 α_eff(b) 严格单调递增**（dα_eff/db = Cov_w(x, ln x) ≥ 0）——这是正确的。\\n\\n**D021 的错误推论**：\\\"因此 α_eff 优化等价于 ESS 阈值化\\\"——这假设优化目标是 max α_eff(b) s.t. ESS ≥ n_min。但实际优化是 **inf{b : α_eff(b) ≥ τ}**——最小满足质量阈值的 b。单调性恰恰保证了 b_τ 的**存在性和唯一性**。\\n\\n**Q1 实证（Reviewer 独立核实）**：\\n- 51,913 micro-batches 中，49.9% clean (b*=0), 20.2% α_eff binding, 30.0% ESS binding\\n- 在需 reweighting 的 batch 中：40.1% α_eff binding, 59.9% ESS binding\\n- α_eff binding 时 b*=1.67，ESS-only 方法会选 b*=4.15（2.5× 更激进）\\n- α_eff binding 时 ESS=2.60（vs n_min=2.0，有 30% 余量）\\n\\n**论文呈现**：α_eff 是方法的核心组件（非仅 motivation），提供质量阈值约束。Figure: 双轴图展示 α_eff(b) 和 ESS(b) 曲线 + b_τ 和 b_ESS 标注。\\n\\n**τ 的定位（D025 定论 + D035 τ sweep 完整数据更新）**：收敛理论 (arXiv 2602.16065) 中 α = m₁/(m₁+m₂) 是已知设计参数，推导依赖已知比例。τ **不能声称有 proportion-free 的理论推导**。正确定位：empirical hyperparameter with theoretical motivation——收敛理论解释了\\\"为什么需要质量阈值\\\"（α 越高收敛越快），但 τ 的特定值由经验确定。\\n\\n**τ sweep 完整结果（6 点，seed42，ρ=0.4）**：\\n\\n| τ | PPL | Δ vs uniform (17.694) | b* mean | conclusion |\\n|---|-----|----------------------|---------|------------|\\n| 0.50 | 17.688 | −0.006 | 0.39 | success |\\n| 0.60 | 17.681 | −0.013 | 0.59 | success |\\n| 0.70 | 17.679 | −0.015 | 0.89 | success |\\n| **0.80** | **17.653** | **−0.041** | **1.40** | **best** |\\n| 0.90 | 17.712 | +0.018 | 2.36 | negative |\\n| 0.95 | 17.723 | +0.029 | 3.08 | negative |\\n\\n**关键洞察**：(1) [0.5, 0.8] 全部 beat uniform，safe range 内 PPL 差异仅 0.035；(2) τ=0.8 是最优默认值；(3) τ>0.8 因 b* 膨胀导致过度 downweighting 而退化（asymmetric sensitivity）；(4) b* 与 τ 严格单调递增，机制清晰——τ 越高要求越严，solver 被迫推高 b*。不能说\\\"τ 不敏感\\\"，正确表述：\\\"wide safe range [0.5, 0.8] with principled default τ=0.8\\\"。\\n\\n**ESS-only baseline 已验证 (D029)**：ESS-only PPL=17.728（+0.034 vs uniform，+0.076 vs adaptive_fix）——max-intervention 退化确认，min-intervention (dual) 明确优于 max-intervention (ESS-only)。ess_only_seed123/456 跨 seed 验证进行中。\\n\\n## Positioning vs Prior Work\\n\\n### Drayson et al. (EMNLP 2025) — 最近相关工作\\n\\n**共同点**：同一加权公式 w=(1-q)^b，detect-and-reweight 范式。\\n\\n**关键区分**：\\n\\n| 维度 | Drayson et al. | Ours |\\n|------|---------------|------|\\n| **b 选择** | 验证集 empirical 选取，训练中固定 | α_eff + ESS 双重约束自适应推导，per-batch 动态 |\\n| **干预原则** | 无原则（b 是超参数） | 最小干预（inf{b : α_eff ≥ τ}，只做必要的清洁） |\\n| **实现路径** | SIR resampling（离散重采样） | Loss reweighting（连续梯度加权） |\\n| **污染设置** | 不假设已知比例，但 b 依赖 validation set | 仅需 detector scores，无 validation set |\\n| **检测器** | ModernBERT 150M (AUC=0.986) | TF-IDF + LR (AUC=0.939)，轻量即可 |\\n| **训练场景** | 递归训练 model collapse prevention | Web corpus 一次性预训练 |\\n| **数据规模** | WikiText-2 (~2M tokens) | FineWeb subset (132M+ tokens) |\\n| **validation 成本** | 需 per-model validation run | 零额外 validation cost |\\n\\n**定位原则：complementary approaches for different settings。**\\n\\n### Golden Ratio Weighting (arXiv 2502.18049, 2025)\\n理论最优 w*=1/φ，但假设已知 real/synthetic 比例 k。作为 oracle baseline。\\n\\n### 其他相关工作\\n- **Strong Model Collapse (ICLR 2025)** — 理论动机：微量合成数据即致 collapse\\n- **Dynamic Loss-Based Reweighting (ICLR 2025)** — 按 loss 加权（不使用 detector score），互补\\n- **SoftDedup (ACL 2024)** — 基于重复度的 soft reweighting\\n- **DoReMi / DSIR (NeurIPS 2023)** — 域级优化 vs 我们的实例级\\n- **Beyond Model Collapse / Verification (NeurIPS 2025)** — verifier-based prevention\\n- **PSIS (Pareto Smoothed IS)** — 重要性采样诊断，Kish's ESS 理论来源\\n- **arXiv 2602.16065** — α_eff 质量阈值 τ 的收敛理论来源\\n\\n## Core Claims\\n\\n### Claim 1 (Primary): Dual-Constrained Adaptive b* — Minimum Intervention Principle\\n\\nα_eff + ESS 双重约束的 adaptive b*，提供 contamination-aware reweighting 中权重指数的 **principled 推导**，替代 Drayson et al. 的 per-model empirical grid search。\\n\\n- **方法核心**：b* = inf{b ≥ 0 : α_eff(b) ≥ τ} s.t. ESS(b) ≥ n_min。两个约束分别提供 b 的下界（质量）和上界（稳定），b* 是最小满足质量阈值的可行解\\n- **最小干预原则**：不 downweight 更多于必要——在 ~40% reweighted batch 中，b* 仅为 ESS-only 上界的 45%，保留显著更多有效样本\\n- **差异化**：Drayson 的 b 是超参数（需 validation + grid search）；我们的 b* 是双约束下的自适应推导\\n- **证据需求**：(a) α_eff binding 比例统计 (✓ Q1); (b) ESS-only baseline head-to-head 对比（证明 min > max intervention）; (c) b* 轨迹分析\\n- **理论 motivation**：α_eff(b) 单调性保证 b_τ 唯一存在；收敛理论为 τ 选择提供指导\\n\\n### Claim 2 (Primary): Adaptive b* 免调参即匹配 Grid-best\\n\\nAdaptive b* 在零超参调优下达到 grid-search 最优同等水平（within seed variance），消除 grid search 的计算开销（6N → 1 runs）。\\n\\n- **MVP 证据**: adaptive_fix ×3 seeds vs grid-b ×3 seeds（40% 污染, Qwen3-0.6B, 200M tokens）\\n- **状态**: ✅ MVP Path B PASS (D019: aggregate 88.6%, 三支柱论证)\\n\\n**叙事弹性**：\\n- 核心表述：**\\\"adaptive matches grid-best within seed variance\\\"**\\n- 补充表述：**\\\"eliminates grid search cost (6N → 1 runs)\\\"** + **\\\"consistent improvement across all seeds\\\"**\\n\\n**MVP 数据**：\\n\\n| Metric | seed42 | seed123 | seed456 |\\n|--------|--------|---------|---------|\\n| Uniform PPL | 17.690 | 17.690 | 17.700 |\\n| Grid-best PPL (b=0.5) | 17.651 | 17.638 | 17.650 |\\n| Adaptive_fix PPL | 17.650 | 17.643 | 17.660 |\\n| Ratio | 102.6% | 90.4% | 80.0% |\\n\\nAggregate ratio: 88.6% (D019). Path B PASS.\\n\\n### Claim 3 (Setting): Unknown Contamination Proportion\\n\\n方法仅需 detector scores，无需已知污染比例、无需 clean validation set。\\n\\n- **差异化**：Golden Ratio 需已知比例 k；Drayson 的 b 依赖 validation set；我们仅需 per-sample q-scores\\n- **实际意义**：web-scale pretraining 中污染比例本质不可知\\n- **D021 代码修复**: ✅ τ = 0.8 固定 CLI 参数，不依赖 contamination_ratio\\n- **D025 理论审计**: arXiv 2602.16065 的 α 是已知比例，τ 不能声称有 proportion-free 理论推导。τ 定位为 empirical hyperparameter with theoretical motivation\\n- **D035 τ sweep 完整数据 (6 点)**：[0.5, 0.8] 为 safe range（all beat uniform，PPL 差异 <0.035），τ=0.8 为最优默认值；τ>0.8 因 b* 膨胀退化。正确表述：\\\"wide safe range with principled default\\\"，不说\\\"insensitive\\\"\\n- **Claim 3 核心仍成立**：b* 推导不需要已知比例（ESS 和 α_eff 从 batch 统计量计算），方法运行时不访问 contamination_ratio。τ 在 [0.5, 0.8] 范围内是 robust empirical default，类似于 learning rate warmup steps——有理论 motivation 但具体值凭经验，且有明确的有效范围上界\\n\\n## Ancillary Finding: Lightweight Detector Sufficiency\\n\\nTF-IDF + LR (AUC=0.939) 即可支撑有效的 adaptive reweighting，不需要 ModernBERT 级别的强检测器（Drayson 用 AUC=0.986）。q-score 的连续性（calibration）比分类精度（AUC）更重要。\\n\\n可升级为 co-primary contribution 如果 detector quality ablation 显示明确的 \\\"sufficiency threshold\\\"。\\n\\n## n_min Robustness Framing\\n\\nESS 约束的 n_min 是 adaptive b* 的超参数之一（另一个是 τ）。\\n\\n- n_min=3 at batch_size=4 → ESS 约束过紧，b* 被钳制在低值，seed42 零改善\\n- n_min=2 at batch_size=4 → 稳定工作，3/3 seeds positive\\n- **论文呈现**：n_min sensitivity curve (n_min=1,2,3,4,5) + batch_size 消融 (4,8,16) 证明 knife-edge 是 batch_size=4 的 artifact\\n\\n## Narrative Structure\\n\\n**起点**: Web 语料 20-60% 为合成文本，比例未知——Strong Model Collapse (ICLR 2025) 证明微量污染即破坏 scaling law。\\n\\n**现有方法不足**：Drayson 的 b 依赖 per-model validation（不同模型需不同 b），Golden Ratio 假设已知混合比例。\\n\\n**我们的方案**: Dual-constrained adaptive b*——α_eff 确保 \\\"至少做够清洁\\\"，ESS 确保 \\\"不要清洁过头\\\"，b* 是满足质量阈值的最小干预。\\n\\n**方法直觉**：想象一个旋钮 b 控制去污力度。α_eff 告诉你\\\"至少拧到这里才够干净\\\"（质量下界），ESS 告诉你\\\"再拧就会丢太多有效数据\\\"（稳定上界）。方法选择旋钮的最小有效位置——刚好够干净，不多不少。\\n\\n**α_eff 的贡献**：不是\\\"α_eff vs ESS 哪个更重要\\\"，而是双约束共同构成最小干预准则。在 ~40% reweighted batch 中，α_eff 是 binding constraint（b* 远低于 ESS 上界）——如果没有 α_eff，方法会过度 downweight，浪费有效样本。\\n\\n**实验验证**：(a) adaptive vs grid-best within seed variance; (b) adaptive vs ESS-only baseline（证明 min-intervention > max-intervention）; (c) τ/n_min sensitivity; (d) batch_size 消融。\\n\\n## Contribution Structure (D023 reframed)\\n\\n1. **Primary — Method**: Dual-constrained adaptive b*（α_eff 质量下界 + ESS 稳定上界 → 最小干预准则），零 validation cost 的 per-batch 自适应 b 推导，替代 per-model grid search。\\n2. **Primary — Empirical Finding**: (a) Adaptive b* 免调参匹配 grid-best within seed variance; (b) 轻量检测器 (TF-IDF+LR, AUC=0.939) 即可支撑有效重加权; (c) min-intervention 优于 max-intervention（需 ESS-only baseline 验证）。\\n3. **Setting — Unknown Proportion**: 仅需 detector scores，无需已知比例或 validation set（τ 修复后）。\\n\\n**α_eff 是方法的核心组件**，提供质量约束和最小干预语义。收敛理论作为 τ 选择的 motivation。\\n\\n## Anticipated Reviewer Concerns\\n\\n| Concern | Response Strategy | 实验支撑 |\\n|---------|------------------|----------|\\n| \\\"Incremental over Drayson\\\" | 差异化: adaptive b* (zero validation) vs per-model empirical b; min-intervention principle; loss reweighting vs SIR | Claim 1 + Claim 3 + ESS-only baseline |\\n| \\\"α_eff monotone → just ESS thresholding?\\\" | inf{b} vs max{b} 区分: 最小干预 vs 最大干预。Q1 实证: 40% α_eff binding, b* = 1.67 vs ESS-only 4.15。ESS-only baseline 对比训练结果 | ESS-only baseline + Q1 figure |\\n| \\\"Small effect size (~0.3% PPL)\\\" | claim 聚焦免调参+方法正确性; 60% 污染+3B 模型放大; zero-cost advantage | p0_contamination_60 + p0_llama3b |\\n| \\\"Two hyperparameters (τ, n_min) vs one (b)\\\" | 关键区别：τ 在 [0.5,0.8] 有效（sweep 6 点验证），n_min=2 跨 3 seed 稳定。两个 HP 都有明确 safe range + principled default，设一次即可跨数据集；Drayson 的 b 需 per-model per-dataset validation。2 个 robust defaults 替代 1 个 sensitive HP | p0_nmin_* + p0_tau_sweep ✅ + p0_batchsize_* |\\n| \\\"Only 0.6B model\\\" | Limitations 诚实说明；batch_size 消融间接展示方法在不同 ESS 范围下的稳健性（bs=4→16 相当于模拟不同 scale 的 batch 统计行为）；Llama-3B 列为 P1 如有 GPU 余量补做 | p0_batchsize_* + p1_llama3b_adaptive |\\n| \\\"Detector quality sensitivity\\\" | TF-IDF+LR 即可; calibration > AUC | p1_detector_ablation |\\n| \\\"Controlled injection ≠ real web\\\" | domain-skewed + semi-realistic | p2_domain_skewed |\\n| \\\"τ comes from contamination_ratio?\\\" | τ 代码已独立 (D021 fix); 收敛理论 α 确实依赖已知比例 (D025)，诚实说明 τ 是 empirical default with theoretical motivation; τ sweep 6 点完整数据证明 [0.5,0.8] safe range + principled default τ=0.8 | p0_tau_fix ✅ + p0_tau_sweep ✅ |\\n\\n## Key Risks\\n\\n1. **~~ESS-only baseline 可能同样好~~** ✅ **RESOLVED (D029)**: ESS-only PPL=17.728（比 uniform 差 +0.034，比 adaptive 差 +0.076）——max-intervention 明确退化。结果落在\\\"dual > ESS-only\\\"理想区间：min-intervention principle 有可量化的性能优势。跨 seed 验证 (ess_only_seed123/456) 进行中\\n2. **Novelty risk (D013)**: 基础公式来自 Drayson，双约束框架新颖性需充分论证。**应对**: 差异化锚定在 min-intervention principle + zero validation cost\\n3. **~~τ 修复后性能变化~~** ✅ **RESOLVED (D035)**: τ sweep 6 点完成。[0.5, 0.8] safe range 全部 beat uniform；τ=0.8 最优；τ>0.8 退化但机制清晰（b* 膨胀）。方法 robust in practical range\\n4. **~~τ 理论来源依赖已知比例~~** ✅ **RESOLVED (D025+D035)**: τ 定位为 empirical HP with theoretical motivation。τ sweep 提供完整 empirical justification，Claim 3 核心不受影响\\n5. **效应量小**: **应对**: 60% 污染 + 3B 模型放大; zero-cost advantage framing\\n6. **Venue fit**: 核心偏 ML，EMNLP reviewer 可能低估。**应对**: NLP-specific analysis\\n\\n## MVP → Full Paper 扩展路径\\n\\n| 维度 | MVP | Full Paper |\\n|------|-----|-----------|\\n| 污染比例 | 40% | 20%, 40%, 60% |\\n| 模型 | Qwen3-0.6B | + Llama-3.2-3B |\\n| 生成器 | Qwen3-0.6B (self) | + Llama-3.2-1B, Mistral, Gemma |\\n| 检测器 | TF-IDF + LR | + ModernBERT variants (quality ablation) |\\n| Baseline | uniform, grid-b, adaptive | + ESS-only adaptive, Golden Ratio, detect-and-remove, random reweight |\\n| 评估 | eval_ppl | + MMLU, HellaSwag, Self-BLEU, distinct-n |\\n| 注入方式 | uniform random | + domain-skewed, semi-realistic |\\n| n_min 分析 | n_min=2 vs n_min=3 | + n_min=1,4,5 + batch_size=4,8,16 |\\n| τ 分析 | 无 | ✅ τ sweep (6 点) + ESS-only vs dual-constraint 对比 |\\n\", \"total_chars\": 11323, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01JmAP19HNqKWmGDS6SEzspt`</summary>

```json
{
  "project": "provenance_weight_training",
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
  "session_id": "6b846b79-5ede-4f4c-b716-29d3245fa231",
  "uuid": "089cd00a-570a-428d-a94c-faa79780392a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016YPGxu9Tvojy4syAp7yVrq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 722,
      "cache_read_input_tokens": 23822,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 722
      },
      "output_tokens": 36,
      "service_tier": "standard",
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

_source line 11 · 2026-05-15T23:35:10.983Z_

<details><summary>↩ Tool result · `toolu_01JmAP19HNqKWmGDS6SEzspt`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/literature_map.yaml\", \"content\": \"# Literature Map for provenance_weight_training\\n# 研究方向：基于收敛理论的自适应污染重加权\\n# 核心公式：w=(1-q)^b，q 为检测器合成概率，b* 为理论最优权重指数\\n# 更新日期：2026-05-15（文献扫描：补充 Wang et al. + 4 方向新文献 + 修正 2 处错误）\\n\\n# ============================================================\\n# Category: direct-competitor\\n# 同主题/同方法的论文\\n# ============================================================\\n\\n- id: drayson_2025_detection_collapse\\n  title: \\\"Machine-Generated Text Detection Prevents Language Model Collapse\\\"\\n  authors: \\\"George Drayson, Emine Yilmaz, Vasileios Lampos\\\"\\n  venue: \\\"EMNLP 2025\\\"\\n  year: 2025\\n  arxiv_id: \\\"2502.15654\\\"\\n  url: \\\"https://arxiv.org/abs/2502.15654\\\"\\n  github: \\\"https://github.com/GeorgeDrayson/model_collapse\\\"\\n  category: direct-competitor\\n  role: \\\"使用同一公式 w=(1-q)^b 进行重加权，但 b 为验证集 empirical 选取，训练中固定\\\"\\n  method_summary: >\\n    Detect-and-reweight 防止递归训练 model collapse。检测器为 ModernBERT 150M\\n    (MAGE fine-tune, in-domain AUC=0.986, OOD AUC=0.943)。权重公式 wⱼ=(1-q(xⱼ))^b / Σₗ(1-q(xₗ))^b，\\n    通过 SIR 按权重重采样训练数据。b 通过 WikiText-2 验证集上 1 代递归训练后评估选取\\n    (GPT-2/SmolLM 135M/360M 用 b=10, SmolLM 1.7B 用 b=1)，训练全程固定。\\n    实验覆盖 4 个模型 (GPT-2 124M, SmolLM 135M/360M/1.7B)、10 代递归训练、6 种解码策略。\\n    结果 PPL 降低 0.85%–25.65%，diversity 提升 3.44%–14.62%。\\n  key_findings: \\\"验证 detect-and-reweight 有效防止 model collapse 且优于纯人类数据训练；b 值对模型规模敏感（小模型 b=10，大模型 b=1）\\\"\\n  differentiation:\\n    b_selection: \\\"Drayson: 验证集 empirical grid search, per-model 固定 | 我们: α_eff(b) + ESS 约束, per-batch 自适应\\\"\\n    contamination_setting: \\\"Drayson: 不假设已知比例（原文明确声明），但实验为控制设置 | 我们: 未知比例（batch 统计量在线估计）\\\"\\n    detector: \\\"Drayson: ModernBERT 150M (AUC=0.986) | 我们: TF-IDF+LR (AUC=0.939)，证明轻量检测器即可\\\"\\n    theory: \\\"Drayson: 无 b 选取理论（SIR 启发式） | 我们: 收敛理论 motivated α_eff(b) 推导\\\"\\n    training_scenario: \\\"Drayson: 递归训练 model collapse prevention | 我们: Web corpus 一次性预训练中的未知污染\\\"\\n    scale: \\\"Drayson: WikiText-2 (~2M tokens) | 我们: FineWeb subset (132M+ tokens)\\\"\\n    dynamics: \\\"Drayson: b 固定（训练全程不变） | 我们: b* per-batch 自适应\\\"\\n  our_advantages:\\n    - \\\"From heuristic to principled: 理论推导 b* 替代 empirical grid search，零额外 validation cost\\\"\\n    - \\\"Zero validation cost: 无需 validation set 做 b 选择，适用大规模 web pretraining（Drayson 也不假设已知比例，但其 b 选择依赖 validation set）\\\"\\n    - \\\"Lightweight detector sufficiency: TF-IDF+LR 即可，检测器计算开销降低数量级\\\"\\n    - \\\"Unified continuous spectrum: b=0 uniform → b→∞ hard filter 的统一框架\\\"\\n  relevance_to_us: \\\"最直接的竞争者。共享 w=(1-q)^b 公式，但 b 选取方法根本不同——我们的核心贡献正是理论推导 adaptive b*\\\"\\n\\n- id: he_2025_golden_ratio\\n  title: \\\"Golden Ratio Weighting Prevents Model Collapse\\\"\\n  authors: \\\"Hengzhi He, Shirong Xu, Guang Cheng\\\"\\n  venue: \\\"Under review at JRSSB, 2025\\\"\\n  year: 2025\\n  arxiv_id: \\\"2502.18049\\\"\\n  url: \\\"https://arxiv.org/abs/2502.18049\\\"\\n  category: direct-competitor\\n  role: \\\"从理论推导合成/真实数据混合的最优权重，发现最优权重为黄金比例的倒数(~0.62)\\\"\\n  key_findings: \\\"在高斯估计、GLM、非参数估计等场景下，当合成数据与真实数据等量时，真实数据的最优权重约为 0.62（黄金比例倒数）。公式 w*=(√(k²+4k)−k)/2, k=真实/合成样本比\\\"\\n  differentiation:\\n    scope: \\\"纯理论工作，假设已知污染比例，未涉及检测器或 LLM 实验，不处理 unknown/online 设置\\\"\\n  relevance_to_us: \\\"同样是理论推导最优权重，但针对 real/synthetic 固定混合比例，未考虑检测器置信度的连续估计\\\"\\n\\n- id: feng_2025_beyond_collapse\\n  title: \\\"Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification\\\"\\n  authors: \\\"Yunzhen Feng, Elvis Dohmatob, Pu Yang, François Charton, Julia Kempe\\\"\\n  venue: \\\"ICLR 2025\\\"\\n  year: 2025\\n  url: \\\"https://arxiv.org/abs/2406.07515\\\"\\n  category: direct-competitor\\n  role: \\\"使用 verifier 过滤合成数据防止 model collapse，理论证明即使不完美的 verifier 也有效\\\"\\n  key_findings: \\\"用高斯混合模型和线性分类器推导条件，证明 verifier 引导的合成数据筛选可避免 model collapse；即使 verifier 不完美也能受益\\\"\\n  relevance_to_us: \\\"与我们的方法最相似——都用检测器置信度来处理合成数据。区别在于他们做 hard filtering，我们做 soft reweighting\\\"\\n\\n# ============================================================\\n# Category: theoretical-foundation\\n# 理论动机来源\\n# ============================================================\\n\\n- id: wang_2026_survive_contamination\\n  title: \\\"Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training\\\"\\n  authors: \\\"Kevin Wang, Hongqian Niu, Didong Li\\\"\\n  venue: \\\"arXiv preprint\\\"\\n  year: 2026\\n  arxiv_id: \\\"2602.16065\\\"\\n  url: \\\"https://arxiv.org/abs/2602.16065\\\"\\n  category: theoretical-foundation\\n  role: \\\"τ（α_eff 质量下界阈值）的理论动机来源；在通用框架下证明污染递归训练仍然收敛\\\"\\n  method_summary: >\\n    在最小假设（不限数据分布、允许通用逼近器生成模型）下研究递归训练。\\n    证明收敛率 = min(基线模型收敛率, α)，其中 α = m₁/(m₁+m₂) 是每轮真实数据比例。\\n    首个不依赖分布假设的递归训练正面理论结果。进一步扩展到采样偏差场景。\\n  key_findings: \\\"收敛率由真实数据比例 α 下界控制；α 越大收敛越快；即使有污染，只要 α > 0 训练仍收敛\\\"\\n  tension_with_our_work: >\\n    论文中 α = m₁/(m₁+m₂) 是**已知设计参数**（依赖已知的真实/合成数据比例），\\n    而我们的 τ 是 empirical hyperparameter（通过检测器统计量在线估计）。\\n    与 Claim 3（proportion-free）存在张力：Wang 的理论要求知道 α，\\n    我们的方法不假设已知比例，而是通过 α_eff(b) 间接逼近。\\n    需在论文中明确讨论：我们的 τ 是 α 的 principled proxy，而非精确值。\\n  relevance_to_us: \\\"为 α_eff 阈值提供理论合理性——收敛保证依赖真实数据有效比例，我们的 b* 选取正是为了保证 α_eff(b) ≥ τ\\\"\\n\\n# ============================================================\\n# Category: method-component\\n# 我们用到的技术组件\\n# ============================================================\\n\\n- id: kimura_2024_iw_survey\\n  title: \\\"A Short Survey on Importance Weighting for Machine Learning\\\"\\n  authors: \\\"Masanari Kimura, Hideitsu Hino\\\"\\n  venue: \\\"TMLR 2024\\\"\\n  year: 2024\\n  url: \\\"https://arxiv.org/abs/2403.10175\\\"\\n  category: method-component\\n  role: \\\"importance weighting 在机器学习中的全面综述，覆盖分布偏移、密度比估计等核心理论\\\"\\n  key_findings: \\\"系统整理了 importance weighting 在监督学习分布偏移下的理论保证和应用，包括 covariate shift、domain adaptation 等场景\\\"\\n  relevance_to_us: \\\"为我们的 importance weighting 框架提供理论基础和方法论参考\\\"\\n\\n- id: vehtari_2024_psis\\n  title: \\\"Pareto Smoothed Importance Sampling\\\"\\n  authors: \\\"Aki Vehtari, Daniel Simpson, Andrew Gelman, Yuling Yao, Jonah Gabry\\\"\\n  venue: \\\"JMLR 2024\\\"\\n  year: 2024\\n  url: \\\"https://arxiv.org/abs/1507.02646\\\"\\n  category: method-component\\n  role: \\\"提供稳定的 effective sample size 估计和收敛诊断方法\\\"\\n  key_findings: \\\"用广义 Pareto 分布拟合 importance ratio 上尾实现平滑；提出 Pareto k 有限样本收敛率诊断指标；k<min(1-1/log10(S),0.7) 时估计可靠\\\"\\n  relevance_to_us: \\\"我们的 α_eff(b) 估计直接依赖 effective sample size 理论，PSIS 的收敛诊断可用于验证我们的权重方案\\\"\\n\\n- id: sow_2025_dynamic_reweighting\\n  title: \\\"Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining\\\"\\n  authors: \\\"Daouda Sow, Herbert Woisetschläger, Saikiran Bulusu, Shiqiang Wang, Hans-Arno Jacobsen, Yingbin Liang\\\"\\n  venue: \\\"ICLR 2025\\\"\\n  year: 2025\\n  url: \\\"https://arxiv.org/abs/2502.06733\\\"\\n  github: \\\"https://github.com/sowmaster/Sample-Level-Loss-Reweighting-ICLR-2025\\\"\\n  category: method-component\\n  role: \\\"首次提出 loss-based reweighting 对梯度优化收敛性影响的理论框架\\\"\\n  key_findings: \\\"基于 loss 值动态调整每个样本权重；建立了 loss-based reweighting 对收敛界影响的形式化刻画；在 7B 和 1.4B 模型上验证更快收敛和更优性能\\\"\\n  relevance_to_us: \\\"其收敛性理论框架可作为我们推导 b* 最优性的参考；loss-based 与 provenance-based reweighting 互补（不使用检测器，纯 loss signal 驱动）\\\"\\n\\n- id: ye_2025_data_mixing_laws\\n  title: \\\"Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance\\\"\\n  authors: \\\"Jiasheng Ye, Peiju Liu, Tianxiang Sun, Yunhua Zhou, Jun Zhan, Xipeng Qiu\\\"\\n  venue: \\\"ICLR 2025\\\"\\n  year: 2025\\n  url: \\\"https://arxiv.org/abs/2403.16952\\\"\\n  category: method-component\\n  role: \\\"发现数据混合比例与模型性能之间的定量可预测性\\\"\\n  key_findings: \\\"模型性能关于混合比例具有函数形式的可预测性；可用小规模训练预测大模型在不同混合下的性能；适用于 continual training 的遗忘预测\\\"\\n  relevance_to_us: \\\"data mixing laws 可作为验证我们 b* 最优性的理论框架——检验不同 b 下的 mixing 效果是否符合预测\\\"\\n\\n- id: he_2024_softdedup\\n  title: \\\"SoftDedup: an Efficient Data Reweighting Method for Speeding Up Language Model Pre-training\\\"\\n  authors: \\\"Nan He, Weichen Xiong, Hanwen Liu, Yi Liao, Lei Ding, Kai Zhang, Guohua Tang, Xiao Han, Yang Wei\\\"\\n  venue: \\\"ACL 2024\\\"\\n  year: 2024\\n  url: \\\"https://arxiv.org/abs/2407.06654\\\"\\n  category: method-component\\n  role: \\\"用 data commonness 指标进行软去重加权，而非硬删除\\\"\\n  key_findings: \\\"用 n-gram 模型量化样本的 commonness，高频样本降权低频样本升权；相比硬去重保留信息完整性；等效训练时间提升 26% 效率和 1.77% 下游准确率\\\"\\n  relevance_to_us: \\\"软加权优于硬过滤的思路与我们一致——w=(1-q)^b 是连续加权而非二元过滤\\\"\\n\\n- id: xie_2023_doremi\\n  title: \\\"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining\\\"\\n  authors: \\\"Sang Michael Xie, Hieu Pham, Xuanyi Dong, Nan Du, Hanxiao Liu, Yifeng Lu, Percy Liang, Quoc V. Le, Tengyu Ma, Adams Wei Yu\\\"\\n  venue: \\\"NeurIPS 2023\\\"\\n  year: 2023\\n  url: \\\"https://arxiv.org/abs/2305.10429\\\"\\n  category: method-component\\n  role: \\\"域级别权重优化（Group DRO + 小模型代理），不处理 instance-level 污染\\\"\\n  key_findings: \\\"用小代理模型通过 Group DRO 优化域级别数据混合权重；在 The Pile 和 GLaM 数据集上无需目标分布知识即可改善下游性能\\\"\\n  relevance_to_us: \\\"域级别 reweighting baseline；我们的方法在 instance-level 操作，粒度更细且基于检测器置信度而非 loss-based DRO\\\"\\n\\n- id: xie_2023_dsir\\n  title: \\\"Data Selection for Language Models via Importance Resampling\\\"\\n  authors: \\\"Sang Michael Xie, Shibani Santurkar, Tengyu Ma, Percy Liang\\\"\\n  venue: \\\"NeurIPS 2023\\\"\\n  year: 2023\\n  url: \\\"https://arxiv.org/abs/2302.03169\\\"\\n  category: method-component\\n  role: \\\"N-gram 特征重要性采样选择数据子集匹配目标分布\\\"\\n  key_findings: \\\"用 n-gram 特征估计 importance weights 并重采样数据匹配目标分布；比 heuristic filtering 更 principled；在 GLUE 和下游任务上优于随机选择和启发式方法\\\"\\n  relevance_to_us: \\\"同样用 importance resampling，但目标是分布匹配而非污染处理；与 Drayson 的 SIR 方法有方法论联系\\\"\\n\\n- id: chen_2025_aioli\\n  title: \\\"Aioli: A Unified Optimization Framework for Language Model Data Mixing\\\"\\n  authors: \\\"Mayee F. Chen, Michael Y. Hu, Nicholas Lourie, Kyunghyun Cho, Christopher Ré\\\"\\n  venue: \\\"ICLR 2025\\\"\\n  year: 2025\\n  arxiv_id: \\\"2411.05735\\\"\\n  url: \\\"https://arxiv.org/abs/2411.05735\\\"\\n  github: \\\"https://github.com/HazyResearch/aioli\\\"\\n  category: method-component\\n  role: \\\"在线自适应数据混合优化框架，统一现有 domain-level mixing 方法\\\"\\n  key_findings: \\\"统一 DoReMi/Data Mixing Laws 等为标准优化问题（最小化平均 loss + mixing law 约束）；提出 AIOLI 在训练中动态估计 mixing law 参数并调整比例；6/6 数据集上超越分层采样\\\"\\n  relevance_to_us: \\\"最直接的 non-grid-search adaptive weighting 对比：AIOLI 是 domain-level 在线优化，我们是 instance-level α_eff-based 在线优化。AIOLI 不处理污染，纯 loss-driven\\\"\\n\\n- id: yang_2026_data_mixing_agent\\n  title: \\\"Data Mixing Agent: Learning to Re-weight Domains for Continual Pre-training\\\"\\n  authors: \\\"Kailai Yang, Xiao Liu, Lei Ji, Hao Li, Xiao Liang, Zhiwei Liu, Yeyun Gong, Peng Cheng, Mao Yang\\\"\\n  venue: \\\"ACL 2026\\\"\\n  year: 2026\\n  arxiv_id: \\\"2507.15640\\\"\\n  url: \\\"https://arxiv.org/abs/2507.15640\\\"\\n  category: method-component\\n  role: \\\"用 RL 学习 domain 级别数据混合权重，解决 continual pretraining 中的灾难性遗忘\\\"\\n  key_findings: \\\"首个 model-based end-to-end 域权重学习框架；RL agent 在大量 mixing trajectory 上学习泛化启发式；跨 source field、target model、domain space 泛化\\\"\\n  relevance_to_us: \\\"另一条 non-grid-search 路线（RL-based），但在 domain-level 操作且不处理污染检测；我们的 b* 推导更轻量（无需 RL 训练）\\\"\\n\\n# ============================================================\\n# Category: background\\n# 数据污染/合成数据在 LLM 训练中的问题\\n# ============================================================\\n\\n- id: shumailov_2024_model_collapse\\n  title: \\\"AI Models Collapse When Trained on Recursively Generated Data\\\"\\n  authors: \\\"Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Nicolas Papernot, Ross Anderson, Yarin Gal\\\"\\n  venue: \\\"Nature 2024\\\"\\n  year: 2024\\n  url: \\\"https://www.nature.com/articles/s41586-024-07566-y\\\"\\n  category: background\\n  role: \\\"奠基性工作——证明在递归生成数据上训练导致 model collapse\\\"\\n  key_findings: \\\"在 LLM、VAE、GMM 上证明不加区分地用模型生成内容训练会导致不可逆退化；原始分布的尾部逐渐消失；反复训练的语言模型出现重复短语\\\"\\n  relevance_to_us: \\\"model collapse 是我们工作的核心动机——加权方案的目标就是防止污染数据导致的性能退化\\\"\\n\\n- id: alemohammad_2024_mad\\n  title: \\\"Self-Consuming Generative Models Go MAD\\\"\\n  authors: \\\"Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, Richard G. Baraniuk\\\"\\n  venue: \\\"ICLR 2024\\\"\\n  year: 2024\\n  url: \\\"https://arxiv.org/abs/2307.01850\\\"\\n  category: background\\n  role: \\\"提出 Model Autophagy Disorder (MAD) 概念——自消费式生成模型的退化\\\"\\n  key_findings: \\\"分析三种自消费循环（fully synthetic、synthetic augmentation、fresh data）；无新鲜真实数据时质量或多样性不可避免下降；即使保留原始训练数据也可能退化\\\"\\n  relevance_to_us: \\\"MAD 的数学框架帮助理解不同污染程度下的退化动力学，为我们的收敛理论提供上下文\\\"\\n\\n- id: dohmatob_2025_strong_collapse\\n  title: \\\"Strong Model Collapse\\\"\\n  authors: \\\"Elvis Dohmatob, Yunzhen Feng, Arjun Subramonian, Julia Kempe\\\"\\n  venue: \\\"ICLR 2025 (Spotlight)\\\"\\n  year: 2025\\n  arxiv_id: \\\"2410.04840\\\"\\n  url: \\\"https://arxiv.org/abs/2410.04840\\\"\\n  category: background\\n  role: \\\"证明即使极少量合成数据（1/1000）也能导致 model collapse\\\"\\n  key_findings: \\\"在 scaling laws 框架下建立 strong model collapse；用算子值自由概率论获得测试误差的 bias-variance 分解；更大模型可放大 collapse 效应\\\"\\n  relevance_to_us: \\\"强化了我们工作的必要性——即使少量合成污染也需要处理，仅靠增加数据量无法解决\\\"\\n\\n- id: nait_saada_2025_quality_illusion\\n  title: \\\"The Data-Quality Illusion: Rethinking Classifier-Based Quality Filtering for LLM Pretraining\\\"\\n  authors: \\\"Thiziri Nait Saada, Louis Bethune, Michal Klein, David Grangier, Marco Cuturi, Pierre Ablin\\\"\\n  venue: \\\"arXiv preprint\\\"\\n  year: 2025\\n  url: \\\"https://arxiv.org/abs/2510.00866\\\"\\n  category: background\\n  role: \\\"质疑基于分类器的数据质量评分是否真正捕获了有意义的质量概念\\\"\\n  key_findings: \\\"CQF 改善下游任务但不一定改善语言建模；质量分类器隐式偏向其监督目标的数据分布；质量桶与特定 benchmark 对齐\\\"\\n  relevance_to_us: \\\"提醒我们检测器置信度 q 不等于真实质量——需要理论保证 b* 在检测器有偏时仍然有效\\\"\\n\\n- id: guo_2025_escaping_collapse\\n  title: \\\"Escaping Model Collapse via Synthetic Data Verification\\\"\\n  venue: \\\"arXiv preprint\\\"\\n  year: 2025\\n  arxiv_id: \\\"2510.16657\\\"\\n  url: \\\"https://arxiv.org/abs/2510.16657\\\"\\n  category: background\\n  role: \\\"提出验证机制筛选合成数据质量，与 detection-based 方法互补\\\"\\n  key_findings: \\\"通过验证机制在合成数据生成后筛选质量，与基于检测器的事后加权方法互补\\\"\\n  relevance_to_us: \\\"verification-based 方法是另一条技术路线——他们做生成时验证，我们做训练时加权\\\"\\n\\n- id: cheng_2025_contamination_survey\\n  title: \\\"A Survey on Data Contamination for Large Language Models\\\"\\n  authors: \\\"Yuxing Cheng, Yi Chang, Yuan Wu\\\"\\n  venue: \\\"arXiv preprint\\\"\\n  year: 2025\\n  arxiv_id: \\\"2502.14425\\\"\\n  url: \\\"https://arxiv.org/abs/2502.14425\\\"\\n  category: background\\n  role: \\\"数据污染问题的全面综述，覆盖检测方法和 contamination-free 评估策略\\\"\\n  key_findings: \\\"系统整理训练/测试数据重叠的检测方法（MIA-based、reference-based、data updating/rewriting）；分析 contamination 对 benchmark 可靠性的影响；提出三类 contamination-free 评估策略\\\"\\n  relevance_to_us: \\\"为我们的 problem statement 提供全面综述支撑——pretraining data contamination 是 LLM 社区公认的系统性问题\\\"\\n\\n- id: wei_2024_data_watermarks\\n  title: \\\"Proving Membership in LLM Pretraining Data via Data Watermarks\\\"\\n  authors: \\\"Johnny Tian-Zheng Wei, Ryan Yixiang Wang, Robin Jia\\\"\\n  venue: \\\"arXiv preprint\\\"\\n  year: 2024\\n  arxiv_id: \\\"2402.10892\\\"\\n  url: \\\"https://arxiv.org/abs/2402.10892\\\"\\n  category: background\\n  role: \\\"用数据水印证明数据集是否在 LLM 预训练中被使用，数据溯源的主动方案\\\"\\n  key_findings: \\\"在公开发布前嵌入随机水印，检测建模为假设检验（控制误检率）；两种水印：随机序列插入和 Unicode lookalike 替换；水印强度随数据集增大而减弱但随模型增大而保持\\\"\\n  relevance_to_us: \\\"主动 provenance 方案（事前水印）vs 我们的被动方案（事后检测+加权）；互补但不冲突\\\"\\n\\n# ============================================================\\n# Category: evaluation\\n# 评估方法相关\\n# ============================================================\\n\\n- id: mitchell_2023_detectgpt\\n  title: \\\"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\\\"\\n  authors: \\\"Eric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher D. Manning, Chelsea Finn\\\"\\n  venue: \\\"ICML 2023\\\"\\n  year: 2023\\n  url: \\\"https://arxiv.org/abs/2301.11305\\\"\\n  category: evaluation\\n  role: \\\"零样本机器生成文本检测方法——我们的检测器 q 的基线方法之一\\\"\\n  key_findings: \\\"LLM 生成的文本倾向于占据模型对数概率函数的负曲率区域；无需训练分类器、收集数据集或水印；在 GPT-NeoX 假新闻检测上从 0.81 AUROC 提升到 0.95\\\"\\n  relevance_to_us: \\\"可作为计算合成概率 q 的检测器之一；其概率曲率方法可能与我们的权重公式有理论联系\\\"\\n\\n- id: shi_2024_minkprob\\n  title: \\\"Detecting Pretraining Data from Large Language Models\\\"\\n  authors: \\\"Weijia Shi, Anirudh Ajith, Mengzhou Xia, Yangsibo Huang, Daogao Liu, Terra Blevins, Danqi Chen, Luke Zettlemoyer\\\"\\n  venue: \\\"ICLR 2024\\\"\\n  year: 2024\\n  url: \\\"https://arxiv.org/abs/2310.16789\\\"\\n  category: evaluation\\n  role: \\\"Min-K% Prob 方法——检测数据是否在预训练集中的无参考方法\\\"\\n  key_findings: \\\"已训练数据包含更少低概率异常 token；取最低 K% token 概率的平均值判断；在 WikiMIA 上比最佳基线高 7.4 AUC；无需参考模型\\\"\\n  relevance_to_us: \\\"Min-K% Prob 可作为估计合成概率 q 的候选方法；其 membership inference 思路可扩展为连续置信度估计\\\"\\n\\n- id: kuo_2024_data_weighting\\n  title: \\\"Not All LLM-Generated Data Are Equal: Rethinking Data Weighting in Text Classification\\\"\\n  authors: \\\"Hsun-Yu Kuo et al.\\\"\\n  venue: \\\"arXiv preprint\\\"\\n  year: 2024\\n  url: \\\"https://arxiv.org/abs/2410.21526\\\"\\n  category: evaluation\\n  role: \\\"评估合成数据加权策略在文本分类中的效果\\\"\\n  key_findings: \\\"提出加权损失方法用少量真实数据对齐合成数据分布；在 BERT 级模型上稳定优于标准交叉熵和其他加权方法\\\"\\n  relevance_to_us: \\\"验证了合成数据需要差异化加权的思路；其评估框架可参考用于我们的下游任务评估\\\"\\n\", \"total_chars\": 15632, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6b846b79-5ede-4f4c-b716-29d3245fa231",
  "uuid": "ba244e88-42e4-4977-a7f3-e60f503ab9a8",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/literature_map.yaml\\\", \\\"content\\\": \\\"# Literature Map for provenance_weight_training\\\\n# 研究方向：基于收敛理论的自适应污染重加权\\\\n# 核心公式：w=(1-q)^b，q 为检测器合成概率，b* 为理论最优权重指数\\\\n# 更新日期：2026-05-15（文献扫描：补充 Wang et al. + 4 方向新文献 + 修正 2 处错误）\\\\n\\\\n# ============================================================\\\\n# Category: direct-competitor\\\\n# 同主题/同方法的论文\\\\n# ============================================================\\\\n\\\\n- id: drayson_2025_detection_collapse\\\\n  title: \\\\\\\"Machine-Generated Text Detection Prevents Language Model Collapse\\\\\\\"\\\\n  authors: \\\\\\\"George Drayson, Emine Yilmaz, Vasileios Lampos\\\\\\\"\\\\n  venue: \\\\\\\"EMNLP 2025\\\\\\\"\\\\n  year: 2025\\\\n  arxiv_id: \\\\\\\"2502.15654\\\\\\\"\\\\n  url: \\\\\\\"https://arxiv.org/abs/2502.15654\\\\\\\"\\\\n  github: \\\\\\\"https://github.com/GeorgeDrayson/model_collapse\\\\\\\"\\\\n  category: direct-competitor\\\\n  role: \\\\\\\"使用同一公式 w=(1-q)^b 进行重加权，但 b 为验证集 empirical 选取，训练中固定\\\\\\\"\\\\n  method_summary: >\\\\n    Detect-and-reweight 防止递归训练 model collapse。检测器为 ModernBERT 150M\\\\n    (MAGE fine-tune, in-domain AUC=0.986, OOD AUC=0.943)。权重公式 wⱼ=(1-q(xⱼ))^b / Σₗ(1-q(xₗ))^b，\\\\n    通过 SIR 按权重重采样训练数据。b 通过 WikiText-2 验证集上 1 代递归训练后评估选取\\\\n    (GPT-2/SmolLM 135M/360M 用 b=10, SmolLM 1.7B 用 b=1)，训练全程固定。\\\\n    实验覆盖 4 个模型 (GPT-2 124M, SmolLM 135M/360M/1.7B)、10 代递归训练、6 种解码策略。\\\\n    结果 PPL 降低 0.85%–25.65%，diversity 提升 3.44%–14.62%。\\\\n  key_findings: \\\\\\\"验证 detect-and-reweight 有效防止 model collapse 且优于纯人类数据训练；b 值对模型规模敏感（小模型 b=10，大模型 b=1）\\\\\\\"\\\\n  differentiation:\\\\n    b_selection: \\\\\\\"Drayson: 验证集 empirical grid search, per-model 固定 | 我们: α_eff(b) + ESS 约束, per-batch 自适应\\\\\\\"\\\\n    contamination_setting: \\\\\\\"Drayson: 不假设已知比例（原文明确声明），但实验为控制设置 | 我们: 未知比例（batch 统计量在线估计）\\\\\\\"\\\\n    detector: \\\\\\\"Drayson: ModernBERT 150M (AUC=0.986) | 我们: TF-IDF+LR (AUC=0.939)，证明轻量检测器即可\\\\\\\"\\\\n    theory: \\\\\\\"Drayson: 无 b 选取理论（SIR 启发式） | 我们: 收敛理论 motivated α_eff(b) 推导\\\\\\\"\\\\n    training_scenario: \\\\\\\"Drayson: 递归训练 model collapse prevention | 我们: Web corpus 一次性预训练中的未知污染\\\\\\\"\\\\n    scale: \\\\\\\"Drayson: WikiText-2 (~2M tokens) | 我们: FineWeb subset (132M+ tokens)\\\\\\\"\\\\n    dynamics: \\\\\\\"Drayson: b 固定（训练全程不变） | 我们: b* per-batch 自适应\\\\\\\"\\\\n  our_advantages:\\\\n    - \\\\\\\"From heuristic to principled: 理论推导 b* 替代 empirical grid search，零额外 validation cost\\\\\\\"\\\\n    - \\\\\\\"Zero validation cost: 无需 validation set 做 b 选择，适用大规模 web pretraining（Drayson 也不假设已知比例，但其 b 选择依赖 validation set）\\\\\\\"\\\\n    - \\\\\\\"Lightweight detector sufficiency: TF-IDF+LR 即可，检测器计算开销降低数量级\\\\\\\"\\\\n    - \\\\\\\"Unified continuous spectrum: b=0 uniform → b→∞ hard filter 的统一框架\\\\\\\"\\\\n  relevance_to_us: \\\\\\\"最直接的竞争者。共享 w=(1-q)^b 公式，但 b 选取方法根本不同——我们的核心贡献正是理论推导 adaptive b*\\\\\\\"\\\\n\\\\n- id: he_2025_golden_ratio\\\\n  title: \\\\\\\"Golden Ratio Weighting Prevents Model Collapse\\\\\\\"\\\\n  authors: \\\\\\\"Hengzhi He, Shirong Xu, Guang Cheng\\\\\\\"\\\\n  venue: \\\\\\\"Under review at JRSSB, 2025\\\\\\\"\\\\n  year: 2025\\\\n  arxiv_id: \\\\\\\"2502.18049\\\\\\\"\\\\n  url: \\\\\\\"https://arxiv.org/abs/2502.18049\\\\\\\"\\\\n  category: direct-competitor\\\\n  role: \\\\\\\"从理论推导合成/真实数据混合的最优权重，发现最优权重为黄金比例的倒数(~0.62)\\\\\\\"\\\\n  key_findings: \\\\\\\"在高斯估计、GLM、非参数估计等场景下，当合成数据与真实数据等量时，真实数据的最优权重约为 0.62（黄金比例倒数）。公式 w*=(√(k²+4k)−k)/2, k=真实/合成样本比\\\\\\\"\\\\n  differentiation:\\\\n    scope: \\\\\\\"纯理论工作，假设已知污染比例，未涉及检测器或 LLM 实验，不处理 unknown/online 设置\\\\\\\"\\\\n  relevance_to_us: \\\\\\\"同样是理论推导最优权重，但针对 real/synthetic 固定混合比例，未考虑检测器置信度的连续估计\\\\\\\"\\\\n\\\\n- id: feng_2025_beyond_collapse\\\\n  title: \\\\\\\"Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification\\\\\\\"\\\\n  authors: \\\\\\\"Yunzhen Feng, Elvis Dohmatob, Pu Yang, François Charton, Julia Kempe\\\\\\\"\\\\n  venue: \\\\\\\"ICLR 2025\\\\\\\"\\\\n  year: 2025\\\\n  url: \\\\\\\"https://arxiv.org/abs/2406.07515\\\\\\\"\\\\n  category: direct-competitor\\\\n  role: \\\\\\\"使用 verifier 过滤合成数据防止 model collapse，理论证明即使不完美的 verifier 也有效\\\\\\\"\\\\n  key_findings: \\\\\\\"用高斯混合模型和线性分类器推导条件，证明 verifier 引导的合成数据筛选可避免 model collapse；即使 verifier 不完美也能受益\\\\\\\"\\\\n  relevance_to_us: \\\\\\\"与我们的方法最相似——都用检测器置信度来处理合成数据。区别在于他们做 hard filtering，我们做 soft reweighting\\\\\\\"\\\\n\\\\n# ============================================================\\\\n# Category: theoretical-foundation\\\\n# 理论动机来源\\\\n# ============================================================\\\\n\\\\n- id: wang_2026_survive_contamination\\\\n  title: \\\\\\\"Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training\\\\\\\"\\\\n  authors: \\\\\\\"Kevin Wang, Hongqian Niu, Didong Li\\\\\\\"\\\\n  venue: \\\\\\\"arXiv preprint\\\\\\\"\\\\n  year: 2026\\\\n  arxiv_id: \\\\\\\"2602.16065\\\\\\\"\\\\n  url: \\\\\\\"https://arxiv.org/abs/2602.16065\\\\\\\"\\\\n  category: theoretical-foundation\\\\n  role: \\\\\\\"τ（α_eff 质量下界阈值）的理论动机来源；在通用框架下证明污染递归训练仍然收敛\\\\\\\"\\\\n  method_summary: >\\\\n    在最小假设（不限数据分布、允许通用逼近器生成模型）下研究递归训练。\\\\n    证明收敛率 = min(基线模型收敛率, α)，其中 α = m₁/(m₁+m₂) 是每轮真实数据比例。\\\\n    首个不依赖分布假设的递归训练正面理论结果。进一步扩展到采样偏差场景。\\\\n  key_findings: \\\\\\\"收敛率由真实数据比例 α 下界控制；α 越大收敛越快；即使有污染，只要 α > 0 训练仍收敛\\\\\\\"\\\\n  tension_with_our_work: >\\\\n    论文中 α = m₁/(m₁+m₂) 是**已知设计参数**（依赖已知的真实/合成数据比例），\\\\n    而我们的 τ 是 empirical hyperparameter（通过检测器统计量在线估计）。\\\\n    与 Claim 3（proportion-free）存在张力：Wang 的理论要求知道 α，\\\\n    我们的方法不假设已知比例，而是通过 α_eff(b) 间接逼近。\\\\n    需在论文中明确讨论：我们的 τ 是 α 的 principled proxy，而非精确值。\\\\n  relevance_to_us: \\\\\\\"为 α_eff 阈值提供理论合理性——收敛保证依赖真实数据有效比例，我们的 b* 选取正是为了保证 α_eff(b) ≥ τ\\\\\\\"\\\\n\\\\n# ============================================================\\\\n# Category: method-component\\\\n# 我们用到的技术组件\\\\n# ============================================================\\\\n\\\\n- id: kimura_2024_iw_survey\\\\n  title: \\\\\\\"A Short Survey on Importance Weighting for Machine Learning\\\\\\\"\\\\n  authors: \\\\\\\"Masanari Kimura, Hideitsu Hino\\\\\\\"\\\\n  venue: \\\\\\\"TMLR 2024\\\\\\\"\\\\n  year: 2024\\\\n  url: \\\\\\\"https://arxiv.org/abs/2403.10175\\\\\\\"\\\\n  category: method-component\\\\n  role: \\\\\\\"importance weighting 在机器学习中的全面综述，覆盖分布偏移、密度比估计等核心理论\\\\\\\"\\\\n  key_findings: \\\\\\\"系统整理了 importance weighting 在监督学习分布偏移下的理论保证和应用，包括 covariate shift、domain adaptation 等场景\\\\\\\"\\\\n  relevance_to_us: \\\\\\\"为我们的 importance weighting 框架提供理论基础和方法论参考\\\\\\\"\\\\n\\\\n- id: vehtari_2024_psis\\\\n  title: \\\\\\\"Pareto Smoothed Importance Sampling\\\\\\\"\\\\n  authors: \\\\\\\"Aki Vehtari, Daniel Simpson, Andrew Gelman, Yuling Yao, Jonah Gabry\\\\\\\"\\\\n  venue: \\\\\\\"JMLR 2024\\\\\\\"\\\\n  year: 2024\\\\n  url: \\\\\\\"https://arxiv.org/abs/1507.02646\\\\\\\"\\\\n  category: method-component\\\\n  role: \\\\\\\"提供稳定的 effective sample size 估计和收敛诊断方法\\\\\\\"\\\\n  key_findings: \\\\\\\"用广义 Pareto 分布拟合 importance ratio 上尾实现平滑；提出 Pareto k 有限样本收敛率诊断指标；k&lt;min(1-1/log10(S),0.7) 时估计可靠\\\\\\\"\\\\n  relevance_to_us: \\\\\\\"我们的 α_eff(b) 估计直接依赖 effective sample size 理论，PSIS 的收敛诊断可用于验证我们的权重方案\\\\\\\"\\\\n\\\\n- id: sow_2025_dynamic_reweighting\\\\n  title: \\\\\\\"Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining\\\\\\\"\\\\n  authors: \\\\\\\"Daouda Sow, Herbert Woisetschläger, Saikiran Bulusu, Shiqiang Wang, Hans-Arno Jacobsen, Yingbin Liang\\\\\\\"\\\\n  venue: \\\\\\\"ICLR 2025\\\\\\\"\\\\n  year: 2025\\\\n  url: \\\\\\\"https://arxiv.org/abs/2502.06733\\\\\\\"\\\\n  github: \\\\\\\"https://github.com/sowmaster/Sample-Level-Loss-Reweighting-ICLR-2025\\\\\\\"\\\\n  category: method-component\\\\n  role: \\\\\\\"首次提出 loss-based reweighting 对梯度优化收敛性影响的理论框架\\\\\\\"\\\\n  key_findings: \\\\\\\"基于 loss 值动态调整每个样本权重；建立了 loss-based reweighting 对收敛界影响的形式化刻画；在 7B 和 1.4B 模型上验证更快收敛和更优性能\\\\\\\"\\\\n  relevance_to_us: \\\\\\\"其收敛性理论框架可作为我们推导 b* 最优性的参考；loss-based 与 provenance-based reweighting 互补（不使用检测器，纯 loss signal 驱动）\\\\\\\"\\\\n\\\\n- id: ye_2025_data_mixing_laws\\\\n  title: \\\\\\\"Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance\\\\\\\"\\\\n  authors: \\\\\\\"Jiasheng Ye, Peiju Liu, Tianxiang Sun, Yunhua Zhou, Jun Zhan, Xipeng Qiu\\\\\\\"\\\\n  venue: \\\\\\\"ICLR 2025\\\\\\\"\\\\n  year: 2025\\\\n  url: \\\\\\\"https://arxiv.org/abs/2403.16952\\\\\\\"\\\\n  category: method-component\\\\n  role: \\\\\\\"发现数据混合比例与模型性能之间的定量可预测性\\\\\\\"\\\\n  key_findings: \\\\\\\"模型性能关于混合比例具有函数形式的可预测性；可用小规模训练预测大模型在不同混合下的性能；适用于 continual training 的遗忘预测\\\\\\\"\\\\n  relevance_to_us: \\\\\\\"data mixing laws 可作为验证我们 b* 最优性的理论框架——检验不同 b 下的 mixing 效果是否符合预测\\\\\\\"\\\\n\\\\n- id: he_2024_softdedup\\\\n  title: \\\\\\\"SoftDedup: an Efficient Data Reweighting Method for Speeding Up Language Model Pre-training\\\\\\\"\\\\n  authors: \\\\\\\"Nan He, Weichen Xiong, Hanwen Liu, Yi Liao, Lei Ding, Kai Zhang, Guohua Tang, Xiao Han, Yang Wei\\\\\\\"\\\\n  venue: \\\\\\\"ACL 2024\\\\\\\"\\\\n  year: 2024\\\\n  url: \\\\\\\"https://arxiv.org/abs/2407.06654\\\\\\\"\\\\n  category: method-component\\\\n  role: \\\\\\\"用 data commonness 指标进行软去重加权，而非硬删除\\\\\\\"\\\\n  key_findings: \\\\\\\"用 n-gram 模型量化样本的 commonness，高频样本降权低频样本升权；相比硬去重保留信息完整性；等效训练时间提升 26% 效率和 1.77% 下游准确率\\\\\\\"\\\\n  relevance_to_us: \\\\\\\"软加权优于硬过滤的思路与我们一致——w=(1-q)^b 是连续加权而非二元过滤\\\\\\\"\\\\n\\\\n- id: xie_2023_doremi\\\\n  title: \\\\\\\"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining\\\\\\\"\\\\n  authors: \\\\\\\"Sang Michael Xie, Hieu Pham, Xuanyi Dong, Nan Du, Hanxiao Liu, Yifeng Lu, Percy Liang, Quoc V. Le, Tengyu Ma, Adams Wei Yu\\\\\\\"\\\\n  venue: \\\\\\\"NeurIPS 2023\\\\\\\"\\\\n  year: 2023\\\\n  url: \\\\\\\"https://arxiv.org/abs/2305.10429\\\\\\\"\\\\n  category: method-component\\\\n  role: \\\\\\\"域级别权重优化（Group DRO + 小模型代理），不处理 instance-level 污染\\\\\\\"\\\\n  key_findings: \\\\\\\"用小代理模型通过 Group DRO 优化域级别数据混合权重；在 The Pile 和 GLaM 数据集上无需目标分布知识即可改善下游性能\\\\\\\"\\\\n  relevance_to_us: \\\\\\\"域级别 reweighting baseline；我们的方法在 instance-level 操作，粒度更细且基于检测器置信度而非 loss-based DRO\\\\\\\"\\\\n\\\\n- id: xie_2023_dsir\\\\n  title: \\\\\\\"Data Selection for Language Models via Importance Resampling\\\\\\\"\\\\n  authors: \\\\\\\"Sang Michael Xie, Shibani Santurkar, Tengyu Ma, Percy Liang\\\\\\\"\\\\n  venue: \\\\\\\"NeurIPS 2023\\\\\\\"\\\\n  year: 2023\\\\n  url: \\\\\\\"https://arxiv.org/abs/2302.03169\\\\\\\"\\\\n  category: method-component\\\\n  role: \\\\\\\"N-gram 特征重要性采样选择数据子集匹配目标分布\\\\\\\"\\\\n  key_findings: \\\\\\\"用 n-gram 特征估计 importance weights 并重采样数据匹配目标分布；比 heuristic filtering 更 principled；在 GLUE 和下游任务上优于随机选择和启发式方法\\\\\\\"\\\\n  relevance_to_us: \\\\\\\"同样用 importance resampling，但目标是分布匹配而非污染处理；与 Drayson 的 SIR 方法有方法论联系\\\\\\\"\\\\n\\\\n- id: chen_2025_aioli\\\\n  title: \\\\\\\"Aioli: A Unified Optimization Framework for Language Model Data Mixing\\\\\\\"\\\\n  authors: \\\\\\\"Mayee F. Chen, Michael Y. Hu, Nicholas Lourie, Kyunghyun Cho, Christopher Ré\\\\\\\"\\\\n  venue: \\\\\\\"ICLR 2025\\\\\\\"\\\\n  year: 2025\\\\n  arxiv_id: \\\\\\\"2411.05735\\\\\\\"\\\\n  url: \\\\\\\"https://arxiv.org/abs/2411.05735\\\\\\\"\\\\n  github: \\\\\\\"https://github.com/HazyResearch/aioli\\\\\\\"\\\\n  category: method-component\\\\n  role: \\\\\\\"在线自适应数据混合优化框架，统一现有 domain-level mixing 方法\\\\\\\"\\\\n  key_findings: \\\\\\\"统一 DoReMi/Data Mixing Laws 等为标准优化问题（最小化平均 loss + mixing law 约束）；提出 AIOLI 在训练中动态估计 mixing law 参数并调整比例；6/6 数据集上超越分层采样\\\\\\\"\\\\n  relevance_to_us: \\\\\\\"最直接的 non-grid-search adaptive weighting 对比：AIOLI 是 domain-level 在线优化，我们是 instance-level α_eff-based 在线优化。AIOLI 不处理污染，纯 loss-driven\\\\\\\"\\\\n\\\\n- id: yang_2026_data_mixing_agent\\\\n  title: \\\\\\\"Data Mixing Agent: Learning to Re-weight Domains for Continual Pre-training\\\\\\\"\\\\n  authors: \\\\\\\"Kailai Yang, Xiao Liu, Lei Ji, Hao Li, Xiao Liang, Zhiwei Liu, Yeyun Gong, Peng Cheng, Mao Yang\\\\\\\"\\\\n  venue: \\\\\\\"ACL 2026\\\\\\\"\\\\n  year: 2026\\\\n  arxiv_id: \\\\\\\"2507.15640\\\\\\\"\\\\n  url: \\\\\\\"https://arxiv.org/abs/2507.15640\\\\\\\"\\\\n  category: method-component\\\\n  role: \\\\\\\"用 RL 学习 domain 级别数据混合权重，解决 continual pretraining 中的灾难性遗忘\\\\\\\"\\\\n  key_findings: \\\\\\\"首个 model-based end-to-end 域权重学习框架；RL agent 在大量 mixing trajectory 上学习泛化启发式；跨 source field、target model、domain space 泛化\\\\\\\"\\\\n  relevance_to_us: \\\\\\\"另一条 non-grid-search 路线（RL-based），但在 domain-level 操作且不处理污染检测；我们的 b* 推导更轻量（无需 RL 训练）\\\\\\\"\\\\n\\\\n# ============================================================\\\\n# Category: background\\\\n# 数据污染/合成数据在 LLM 训练中的问题\\\\n# ============================================================\\\\n\\\\n- id: shumailov_2024_model_collapse\\\\n  title: \\\\\\\"AI Models Collapse When Trained on Recursively Generated Data\\\\\\\"\\\\n  authors: \\\\\\\"Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Nicolas Papernot, Ross Anderson, Yarin Gal\\\\\\\"\\\\n  venue: \\\\\\\"Nature 2024\\\\\\\"\\\\n  year: 2024\\\\n  url: \\\\\\\"https://www.nature.com/articles/s41586-024-07566-y\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"奠基性工作——证明在递归生成数据上训练导致 model collapse\\\\\\\"\\\\n  key_findings: \\\\\\\"在 LLM、VAE、GMM 上证明不加区分地用模型生成内容训练会导致不可逆退化；原始分布的尾部逐渐消失；反复训练的语言模型出现重复短语\\\\\\\"\\\\n  relevance_to_us: \\\\\\\"model collapse 是我们工作的核心动机——加权方案的目标就是防止污染数据导致的性能退化\\\\\\\"\\\\n\\\\n- id: alemohammad_2024_mad\\\\n  title: \\\\\\\"Self-Consuming Generative Models Go MAD\\\\\\\"\\\\n  authors: \\\\\\\"Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, Richard G. Baraniuk\\\\\\\"\\\\n  venue: \\\\\\\"ICLR 2024\\\\\\\"\\\\n  year: 2024\\\\n  url: \\\\\\\"https://arxiv.org/abs/2307.01850\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"提出 Model Autophagy Disorder (MAD) 概念——自消费式生成模型的退化\\\\\\\"\\\\n  key_findings: \\\\\\\"分析三种自消费循环（fully synthetic、synthetic augmentation、fresh data）；无新鲜真实数据时质量或多样性不可避免下降；即使保留原始训练数据也可能退化\\\\\\\"\\\\n  relevance_to_us: \\\\\\\"MAD 的数学框架帮助理解不同污染程度下的退化动力学，为我们的收敛理论提供上下文\\\\\\\"\\\\n\\\\n- id: dohmatob_2025_strong_collapse\\\\n  title: \\\\\\\"Strong Model Collapse\\\\\\\"\\\\n  authors: \\\\\\\"Elvis Dohmatob, Yunzhen Feng, Arjun Subramonian, Julia Kempe\\\\\\\"\\\\n  venue: \\\\\\\"ICLR 2025 (Spotlight)\\\\\\\"\\\\n  year: 2025\\\\n  arxiv_id: \\\\\\\"2410.04840\\\\\\\"\\\\n  url: \\\\\\\"https://arxiv.org/abs/2410.04840\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"证明即使极少量合成数据（1/1000）也能导致 model collapse\\\\\\\"\\\\n  key_findings: \\\\\\\"在 scaling laws 框架下建立 strong model collapse；用算子值自由概率论获得测试误差的 bias-variance 分解；更大模型可放大 collapse 效应\\\\\\\"\\\\n  relevance_to_us: \\\\\\\"强化了我们工作的必要性——即使少量合成污染也需要处理，仅靠增加数据量无法解决\\\\\\\"\\\\n\\\\n- id: nait_saada_2025_quality_illusion\\\\n  title: \\\\\\\"The Data-Quality Illusion: Rethinking Classifier-Based Quality Filtering for LLM Pretraining\\\\\\\"\\\\n  authors: \\\\\\\"Thiziri Nait Saada, Louis Bethune, Michal Klein, David Grangier, Marco Cuturi, Pierre Ablin\\\\\\\"\\\\n  venue: \\\\\\\"arXiv preprint\\\\\\\"\\\\n  year: 2025\\\\n  url: \\\\\\\"https://arxiv.org/abs/2510.00866\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"质疑基于分类器的数据质量评分是否真正捕获了有意义的质量概念\\\\\\\"\\\\n  key_findings: \\\\\\\"CQF 改善下游任务但不一定改善语言建模；质量分类器隐式偏向其监督目标的数据分布；质量桶与特定 benchmark 对齐\\\\\\\"\\\\n  relevance_to_us: \\\\\\\"提醒我们检测器置信度 q 不等于真实质量——需要理论保证 b* 在检测器有偏时仍然有效\\\\\\\"\\\\n\\\\n- id: guo_2025_escaping_collapse\\\\n  title: \\\\\\\"Escaping Model Collapse via Synthetic Data Verification\\\\\\\"\\\\n  venue: \\\\\\\"arXiv preprint\\\\\\\"\\\\n  year: 2025\\\\n  arxiv_id: \\\\\\\"2510.16657\\\\\\\"\\\\n  url: \\\\\\\"https://arxiv.org/abs/2510.16657\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"提出验证机制筛选合成数据质量，与 detection-based 方法互补\\\\\\\"\\\\n  key_findings: \\\\\\\"通过验证机制在合成数据生成后筛选质量，与基于检测器的事后加权方法互补\\\\\\\"\\\\n  relevance_to_us: \\\\\\\"verification-based 方法是另一条技术路线——他们做生成时验证，我们做训练时加权\\\\\\\"\\\\n\\\\n- id: cheng_2025_contamination_survey\\\\n  title: \\\\\\\"A Survey on Data Contamination for Large Language Models\\\\\\\"\\\\n  authors: \\\\\\\"Yuxing Cheng, Yi Chang, Yuan Wu\\\\\\\"\\\\n  venue: \\\\\\\"arXiv preprint\\\\\\\"\\\\n  year: 2025\\\\n  arxiv_id: \\\\\\\"2502.14425\\\\\\\"\\\\n  url: \\\\\\\"https://arxiv.org/abs/2502.14425\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"数据污染问题的全面综述，覆盖检测方法和 contamination-free 评估策略\\\\\\\"\\\\n  key_findings: \\\\\\\"系统整理训练/测试数据重叠的检测方法（MIA-based、reference-based、data updating/rewriting）；分析 contamination 对 benchmark 可靠性的影响；提出三类 contamination-free 评估策略\\\\\\\"\\\\n  relevance_to_us: \\\\\\\"为我们的 problem statement 提供全面综述支撑——pretraining data contamination 是 LLM 社区公认的系统性问题\\\\\\\"\\\\n\\\\n- id: wei_2024_data_watermarks\\\\n  title: \\\\\\\"Proving Membership in LLM Pretraining Data via Data Watermarks\\\\\\\"\\\\n  authors: \\\\\\\"Johnny Tian-Zheng Wei, Ryan Yixiang Wang, Robin Jia\\\\\\\"\\\\n  venue: \\\\\\\"arXiv preprint\\\\\\\"\\\\n  year: 2024\\\\n  arxiv_id: \\\\\\\"2402.10892\\\\\\\"\\\\n  url: \\\\\\\"https://arxiv.org/abs/2402.10892\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"用数据水印证明数据集是否在 LLM 预训练中被使用，数据溯源的主动方案\\\\\\\"\\\\n  key_findings: \\\\\\\"在公开发布前嵌入随机水印，检测建模为假设检验（控制误检率）；两种水印：随机序列插入和 Unicode lookalike 替换；水印强度随数据集增大而减弱但随模型增大而保持\\\\\\\"\\\\n  relevance_to_us: \\\\\\\"主动 provenance 方案（事前水印）vs 我们的被动方案（事后检测+加权）；互补但不冲突\\\\\\\"\\\\n\\\\n# ============================================================\\\\n# Category: evaluation\\\\n# 评估方法相关\\\\n# ============================================================\\\\n\\\\n- id: mitchell_2023_detectgpt\\\\n  title: \\\\\\\"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\\\\\\\"\\\\n  authors: \\\\\\\"Eric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher D. Manning, Chelsea Finn\\\\\\\"\\\\n  venue: \\\\\\\"ICML 2023\\\\\\\"\\\\n  year: 2023\\\\n  url: \\\\\\\"https://arxiv.org/abs/2301.11305\\\\\\\"\\\\n  category: evaluation\\\\n  role: \\\\\\\"零样本机器生成文本检测方法——我们的检测器 q 的基线方法之一\\\\\\\"\\\\n  key_findings: \\\\\\\"LLM 生成的文本倾向于占据模型对数概率函数的负曲率区域；无需训练分类器、收集数据集或水印；在 GPT-NeoX 假新闻检测上从 0.81 AUROC 提升到 0.95\\\\\\\"\\\\n  relevance_to_us: \\\\\\\"可作为计算合成概率 q 的检测器之一；其概率曲率方法可能与我们的权重公式有理论联系\\\\\\\"\\\\n\\\\n- id: shi_2024_minkprob\\\\n  title: \\\\\\\"Detecting Pretraining Data from Large Language Models\\\\\\\"\\\\n  authors: \\\\\\\"Weijia Shi, Anirudh Ajith, Mengzhou Xia, Yangsibo Huang, Daogao Liu, Terra Blevins, Danqi Chen, Luke Zettlemoyer\\\\\\\"\\\\n  venue: \\\\\\\"ICLR 2024\\\\\\\"\\\\n  year: 2024\\\\n  url: \\\\\\\"https://arxiv.org/abs/2310.16789\\\\\\\"\\\\n  category: evaluation\\\\n  role: \\\\\\\"Min-K% Prob 方法——检测数据是否在预训练集中的无参考方法\\\\\\\"\\\\n  key_findings: \\\\\\\"已训练数据包含更少低概率异常 token；取最低 K% token 概率的平均值判断；在 WikiMIA 上比最佳基线高 7.4 AUC；无需参考模型\\\\\\\"\\\\n  relevance_to_us: \\\\\\\"Min-K% Prob 可作为估计合成概率 q 的候选方法；其 membership inference 思路可扩展为连续置信度估计\\\\\\\"\\\\n\\\\n- id: kuo_2024_data_weighting\\\\n  title: \\\\\\\"Not All LLM-Generated Data Are Equal: Rethinking Data Weighting in Text Classification\\\\\\\"\\\\n  authors: \\\\\\\"Hsun-Yu Kuo et al.\\\\\\\"\\\\n  venue: \\\\\\\"arXiv preprint\\\\\\\"\\\\n  year: 2024\\\\n  url: \\\\\\\"https://arxiv.org/abs/2410.21526\\\\\\\"\\\\n  category: evaluation\\\\n  role: \\\\\\\"评估合成数据加权策略在文本分类中的效果\\\\\\\"\\\\n  key_findings: \\\\\\\"提出加权损失方法用少量真实数据对齐合成数据分布；在 BERT 级模型上稳定优于标准交叉熵和其他加权方法\\\\\\\"\\\\n  relevance_to_us: \\\\\\\"验证了合成数据需要差异化加权的思路；其评估框架可参考用于我们的下游任务评估\\\\\\\"\\\\n\\\", \\\"total_chars\\\": 15632, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/literature_map.yaml\", \"content\": \"# Literature Map for provenance_weight_training\\n# 研究方向：基于收敛理论的自适应污染重加权\\n# 核心公式：w=(1-q)^b，q 为检测器合成概率，b* 为理论最优权重指数\\n# 更新日期：2026-05-15（文献扫描：补充 Wang et al. + 4 方向新文献 + 修正 2 处错误）\\n\\n# ============================================================\\n# Category: direct-competitor\\n# 同主题/同方法的论文\\n# ============================================================\\n\\n- id: drayson_2025_detection_collapse\\n  title: \\\"Machine-Generated Text Detection Prevents Language Model Collapse\\\"\\n  authors: \\\"George Drayson, Emine Yilmaz, Vasileios Lampos\\\"\\n  venue: \\\"EMNLP 2025\\\"\\n  year: 2025\\n  arxiv_id: \\\"2502.15654\\\"\\n  url: \\\"https://arxiv.org/abs/2502.15654\\\"\\n  github: \\\"https://github.com/GeorgeDrayson/model_collapse\\\"\\n  category: direct-competitor\\n  role: \\\"使用同一公式 w=(1-q)^b 进行重加权，但 b 为验证集 empirical 选取，训练中固定\\\"\\n  method_summary: >\\n    Detect-and-reweight 防止递归训练 model collapse。检测器为 ModernBERT 150M\\n    (MAGE fine-tune, in-domain AUC=0.986, OOD AUC=0.943)。权重公式 wⱼ=(1-q(xⱼ))^b / Σₗ(1-q(xₗ))^b，\\n    通过 SIR 按权重重采样训练数据。b 通过 WikiText-2 验证集上 1 代递归训练后评估选取\\n    (GPT-2/SmolLM 135M/360M 用 b=10, SmolLM 1.7B 用 b=1)，训练全程固定。\\n    实验覆盖 4 个模型 (GPT-2 124M, SmolLM 135M/360M/1.7B)、10 代递归训练、6 种解码策略。\\n    结果 PPL 降低 0.85%–25.65%，diversity 提升 3.44%–14.62%。\\n  key_findings: \\\"验证 detect-and-reweight 有效防止 model collapse 且优于纯人类数据训练；b 值对模型规模敏感（小模型 b=10，大模型 b=1）\\\"\\n  differentiation:\\n    b_selection: \\\"Drayson: 验证集 empirical grid search, per-model 固定 | 我们: α_eff(b) + ESS 约束, per-batch 自适应\\\"\\n    contamination_setting: \\\"Drayson: 不假设已知比例（原文明确声明），但实验为控制设置 | 我们: 未知比例（batch 统计量在线估计）\\\"\\n    detector: \\\"Drayson: ModernBERT 150M (AUC=0.986) | 我们: TF-IDF+LR (AUC=0.939)，证明轻量检测器即可\\\"\\n    theory: \\\"Drayson: 无 b 选取理论（SIR 启发式） | 我们: 收敛理论 motivated α_eff(b) 推导\\\"\\n    training_scenario: \\\"Drayson: 递归训练 model collapse prevention | 我们: Web corpus 一次性预训练中的未知污染\\\"\\n    scale: \\\"Drayson: WikiText-2 (~2M tokens) | 我们: FineWeb subset (132M+ tokens)\\\"\\n    dynamics: \\\"Drayson: b 固定（训练全程不变） | 我们: b* per-batch 自适应\\\"\\n  our_advantages:\\n    - \\\"From heuristic to principled: 理论推导 b* 替代 empirical grid search，零额外 validation cost\\\"\\n    - \\\"Zero validation cost: 无需 validation set 做 b 选择，适用大规模 web pretraining（Drayson 也不假设已知比例，但其 b 选择依赖 validation set）\\\"\\n    - \\\"Lightweight detector sufficiency: TF-IDF+LR 即可，检测器计算开销降低数量级\\\"\\n    - \\\"Unified continuous spectrum: b=0 uniform → b→∞ hard filter 的统一框架\\\"\\n  relevance_to_us: \\\"最直接的竞争者。共享 w=(1-q)^b 公式，但 b 选取方法根本不同——我们的核心贡献正是理论推导 adaptive b*\\\"\\n\\n- id: he_2025_golden_ratio\\n  title: \\\"Golden Ratio Weighting Prevents Model Collapse\\\"\\n  authors: \\\"Hengzhi He, Shirong Xu, Guang Cheng\\\"\\n  venue: \\\"Under review at JRSSB, 2025\\\"\\n  year: 2025\\n  arxiv_id: \\\"2502.18049\\\"\\n  url: \\\"https://arxiv.org/abs/2502.18049\\\"\\n  category: direct-competitor\\n  role: \\\"从理论推导合成/真实数据混合的最优权重，发现最优权重为黄金比例的倒数(~0.62)\\\"\\n  key_findings: \\\"在高斯估计、GLM、非参数估计等场景下，当合成数据与真实数据等量时，真实数据的最优权重约为 0.62（黄金比例倒数）。公式 w*=(√(k²+4k)−k)/2, k=真实/合成样本比\\\"\\n  differentiation:\\n    scope: \\\"纯理论工作，假设已知污染比例，未涉及检测器或 LLM 实验，不处理 unknown/online 设置\\\"\\n  relevance_to_us: \\\"同样是理论推导最优权重，但针对 real/synthetic 固定混合比例，未考虑检测器置信度的连续估计\\\"\\n\\n- id: feng_2025_beyond_collapse\\n  title: \\\"Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification\\\"\\n  authors: \\\"Yunzhen Feng, Elvis Dohmatob, Pu Yang, François Charton, Julia Kempe\\\"\\n  venue: \\\"ICLR 2025\\\"\\n  year: 2025\\n  url: \\\"https://arxiv.org/abs/2406.07515\\\"\\n  category: direct-competitor\\n  role: \\\"使用 verifier 过滤合成数据防止 model collapse，理论证明即使不完美的 verifier 也有效\\\"\\n  key_findings: \\\"用高斯混合模型和线性分类器推导条件，证明 verifier 引导的合成数据筛选可避免 model collapse；即使 verifier 不完美也能受益\\\"\\n  relevance_to_us: \\\"与我们的方法最相似——都用检测器置信度来处理合成数据。区别在于他们做 hard filtering，我们做 soft reweighting\\\"\\n\\n# ============================================================\\n# Category: theoretical-foundation\\n# 理论动机来源\\n# ============================================================\\n\\n- id: wang_2026_survive_contamination\\n  title: \\\"Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training\\\"\\n  authors: \\\"Kevin Wang, Hongqian Niu, Didong Li\\\"\\n  venue: \\\"arXiv preprint\\\"\\n  year: 2026\\n  arxiv_id: \\\"2602.16065\\\"\\n  url: \\\"https://arxiv.org/abs/2602.16065\\\"\\n  category: theoretical-foundation\\n  role: \\\"τ（α_eff 质量下界阈值）的理论动机来源；在通用框架下证明污染递归训练仍然收敛\\\"\\n  method_summary: >\\n    在最小假设（不限数据分布、允许通用逼近器生成模型）下研究递归训练。\\n    证明收敛率 = min(基线模型收敛率, α)，其中 α = m₁/(m₁+m₂) 是每轮真实数据比例。\\n    首个不依赖分布假设的递归训练正面理论结果。进一步扩展到采样偏差场景。\\n  key_findings: \\\"收敛率由真实数据比例 α 下界控制；α 越大收敛越快；即使有污染，只要 α > 0 训练仍收敛\\\"\\n  tension_with_our_work: >\\n    论文中 α = m₁/(m₁+m₂) 是**已知设计参数**（依赖已知的真实/合成数据比例），\\n    而我们的 τ 是 empirical hyperparameter（通过检测器统计量在线估计）。\\n    与 Claim 3（proportion-free）存在张力：Wang 的理论要求知道 α，\\n    我们的方法不假设已知比例，而是通过 α_eff(b) 间接逼近。\\n    需在论文中明确讨论：我们的 τ 是 α 的 principled proxy，而非精确值。\\n  relevance_to_us: \\\"为 α_eff 阈值提供理论合理性——收敛保证依赖真实数据有效比例，我们的 b* 选取正是为了保证 α_eff(b) ≥ τ\\\"\\n\\n# ============================================================\\n# Category: method-component\\n# 我们用到的技术组件\\n# ============================================================\\n\\n- id: kimura_2024_iw_survey\\n  title: \\\"A Short Survey on Importance Weighting for Machine Learning\\\"\\n  authors: \\\"Masanari Kimura, Hideitsu Hino\\\"\\n  venue: \\\"TMLR 2024\\\"\\n  year: 2024\\n  url: \\\"https://arxiv.org/abs/2403.10175\\\"\\n  category: method-component\\n  role: \\\"importance weighting 在机器学习中的全面综述，覆盖分布偏移、密度比估计等核心理论\\\"\\n  key_findings: \\\"系统整理了 importance weighting 在监督学习分布偏移下的理论保证和应用，包括 covariate shift、domain adaptation 等场景\\\"\\n  relevance_to_us: \\\"为我们的 importance weighting 框架提供理论基础和方法论参考\\\"\\n\\n- id: vehtari_2024_psis\\n  title: \\\"Pareto Smoothed Importance Sampling\\\"\\n  authors: \\\"Aki Vehtari, Daniel Simpson, Andrew Gelman, Yuling Yao, Jonah Gabry\\\"\\n  venue: \\\"JMLR 2024\\\"\\n  year: 2024\\n  url: \\\"https://arxiv.org/abs/1507.02646\\\"\\n  category: method-component\\n  role: \\\"提供稳定的 effective sample size 估计和收敛诊断方法\\\"\\n  key_findings: \\\"用广义 Pareto 分布拟合 importance ratio 上尾实现平滑；提出 Pareto k 有限样本收敛率诊断指标；k<min(1-1/log10(S),0.7) 时估计可靠\\\"\\n  relevance_to_us: \\\"我们的 α_eff(b) 估计直接依赖 effective sample size 理论，PSIS 的收敛诊断可用于验证我们的权重方案\\\"\\n\\n- id: sow_2025_dynamic_reweighting\\n  title: \\\"Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining\\\"\\n  authors: \\\"Daouda Sow, Herbert Woisetschläger, Saikiran Bulusu, Shiqiang Wang, Hans-Arno Jacobsen, Yingbin Liang\\\"\\n  venue: \\\"ICLR 2025\\\"\\n  year: 2025\\n  url: \\\"https://arxiv.org/abs/2502.06733\\\"\\n  github: \\\"https://github.com/sowmaster/Sample-Level-Loss-Reweighting-ICLR-2025\\\"\\n  category: method-component\\n  role: \\\"首次提出 loss-based reweighting 对梯度优化收敛性影响的理论框架\\\"\\n  key_findings: \\\"基于 loss 值动态调整每个样本权重；建立了 loss-based reweighting 对收敛界影响的形式化刻画；在 7B 和 1.4B 模型上验证更快收敛和更优性能\\\"\\n  relevance_to_us: \\\"其收敛性理论框架可作为我们推导 b* 最优性的参考；loss-based 与 provenance-based reweighting 互补（不使用检测器，纯 loss signal 驱动）\\\"\\n\\n- id: ye_2025_data_mixing_laws\\n  title: \\\"Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance\\\"\\n  authors: \\\"Jiasheng Ye, Peiju Liu, Tianxiang Sun, Yunhua Zhou, Jun Zhan, Xipeng Qiu\\\"\\n  venue: \\\"ICLR 2025\\\"\\n  year: 2025\\n  url: \\\"https://arxiv.org/abs/2403.16952\\\"\\n  category: method-component\\n  role: \\\"发现数据混合比例与模型性能之间的定量可预测性\\\"\\n  key_findings: \\\"模型性能关于混合比例具有函数形式的可预测性；可用小规模训练预测大模型在不同混合下的性能；适用于 continual training 的遗忘预测\\\"\\n  relevance_to_us: \\\"data mixing laws 可作为验证我们 b* 最优性的理论框架——检验不同 b 下的 mixing 效果是否符合预测\\\"\\n\\n- id: he_2024_softdedup\\n  title: \\\"SoftDedup: an Efficient Data Reweighting Method for Speeding Up Language Model Pre-training\\\"\\n  authors: \\\"Nan He, Weichen Xiong, Hanwen Liu, Yi Liao, Lei Ding, Kai Zhang, Guohua Tang, Xiao Han, Yang Wei\\\"\\n  venue: \\\"ACL 2024\\\"\\n  year: 2024\\n  url: \\\"https://arxiv.org/abs/2407.06654\\\"\\n  category: method-component\\n  role: \\\"用 data commonness 指标进行软去重加权，而非硬删除\\\"\\n  key_findings: \\\"用 n-gram 模型量化样本的 commonness，高频样本降权低频样本升权；相比硬去重保留信息完整性；等效训练时间提升 26% 效率和 1.77% 下游准确率\\\"\\n  relevance_to_us: \\\"软加权优于硬过滤的思路与我们一致——w=(1-q)^b 是连续加权而非二元过滤\\\"\\n\\n- id: xie_2023_doremi\\n  title: \\\"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining\\\"\\n  authors: \\\"Sang Michael Xie, Hieu Pham, Xuanyi Dong, Nan Du, Hanxiao Liu, Yifeng Lu, Percy Liang, Quoc V. Le, Tengyu Ma, Adams Wei Yu\\\"\\n  venue: \\\"NeurIPS 2023\\\"\\n  year: 2023\\n  url: \\\"https://arxiv.org/abs/2305.10429\\\"\\n  category: method-component\\n  role: \\\"域级别权重优化（Group DRO + 小模型代理），不处理 instance-level 污染\\\"\\n  key_findings: \\\"用小代理模型通过 Group DRO 优化域级别数据混合权重；在 The Pile 和 GLaM 数据集上无需目标分布知识即可改善下游性能\\\"\\n  relevance_to_us: \\\"域级别 reweighting baseline；我们的方法在 instance-level 操作，粒度更细且基于检测器置信度而非 loss-based DRO\\\"\\n\\n- id: xie_2023_dsir\\n  title: \\\"Data Selection for Language Models via Importance Resampling\\\"\\n  authors: \\\"Sang Michael Xie, Shibani Santurkar, Tengyu Ma, Percy Liang\\\"\\n  venue: \\\"NeurIPS 2023\\\"\\n  year: 2023\\n  url: \\\"https://arxiv.org/abs/2302.03169\\\"\\n  category: method-component\\n  role: \\\"N-gram 特征重要性采样选择数据子集匹配目标分布\\\"\\n  key_findings: \\\"用 n-gram 特征估计 importance weights 并重采样数据匹配目标分布；比 heuristic filtering 更 principled；在 GLUE 和下游任务上优于随机选择和启发式方法\\\"\\n  relevance_to_us: \\\"同样用 importance resampling，但目标是分布匹配而非污染处理；与 Drayson 的 SIR 方法有方法论联系\\\"\\n\\n- id: chen_2025_aioli\\n  title: \\\"Aioli: A Unified Optimization Framework for Language Model Data Mixing\\\"\\n  authors: \\\"Mayee F. Chen, Michael Y. Hu, Nicholas Lourie, Kyunghyun Cho, Christopher Ré\\\"\\n  venue: \\\"ICLR 2025\\\"\\n  year: 2025\\n  arxiv_id: \\\"2411.05735\\\"\\n  url: \\\"https://arxiv.org/abs/2411.05735\\\"\\n  github: \\\"https://github.com/HazyResearch/aioli\\\"\\n  category: method-component\\n  role: \\\"在线自适应数据混合优化框架，统一现有 domain-level mixing 方法\\\"\\n  key_findings: \\\"统一 DoReMi/Data Mixing Laws 等为标准优化问题（最小化平均 loss + mixing law 约束）；提出 AIOLI 在训练中动态估计 mixing law 参数并调整比例；6/6 数据集上超越分层采样\\\"\\n  relevance_to_us: \\\"最直接的 non-grid-search adaptive weighting 对比：AIOLI 是 domain-level 在线优化，我们是 instance-level α_eff-based 在线优化。AIOLI 不处理污染，纯 loss-driven\\\"\\n\\n- id: yang_2026_data_mixing_agent\\n  title: \\\"Data Mixing Agent: Learning to Re-weight Domains for Continual Pre-training\\\"\\n  authors: \\\"Kailai Yang, Xiao Liu, Lei Ji, Hao Li, Xiao Liang, Zhiwei Liu, Yeyun Gong, Peng Cheng, Mao Yang\\\"\\n  venue: \\\"ACL 2026\\\"\\n  year: 2026\\n  arxiv_id: \\\"2507.15640\\\"\\n  url: \\\"https://arxiv.org/abs/2507.15640\\\"\\n  category: method-component\\n  role: \\\"用 RL 学习 domain 级别数据混合权重，解决 continual pretraining 中的灾难性遗忘\\\"\\n  key_findings: \\\"首个 model-based end-to-end 域权重学习框架；RL agent 在大量 mixing trajectory 上学习泛化启发式；跨 source field、target model、domain space 泛化\\\"\\n  relevance_to_us: \\\"另一条 non-grid-search 路线（RL-based），但在 domain-level 操作且不处理污染检测；我们的 b* 推导更轻量（无需 RL 训练）\\\"\\n\\n# ============================================================\\n# Category: background\\n# 数据污染/合成数据在 LLM 训练中的问题\\n# ============================================================\\n\\n- id: shumailov_2024_model_collapse\\n  title: \\\"AI Models Collapse When Trained on Recursively Generated Data\\\"\\n  authors: \\\"Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Nicolas Papernot, Ross Anderson, Yarin Gal\\\"\\n  venue: \\\"Nature 2024\\\"\\n  year: 2024\\n  url: \\\"https://www.nature.com/articles/s41586-024-07566-y\\\"\\n  category: background\\n  role: \\\"奠基性工作——证明在递归生成数据上训练导致 model collapse\\\"\\n  key_findings: \\\"在 LLM、VAE、GMM 上证明不加区分地用模型生成内容训练会导致不可逆退化；原始分布的尾部逐渐消失；反复训练的语言模型出现重复短语\\\"\\n  relevance_to_us: \\\"model collapse 是我们工作的核心动机——加权方案的目标就是防止污染数据导致的性能退化\\\"\\n\\n- id: alemohammad_2024_mad\\n  title: \\\"Self-Consuming Generative Models Go MAD\\\"\\n  authors: \\\"Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, Richard G. Baraniuk\\\"\\n  venue: \\\"ICLR 2024\\\"\\n  year: 2024\\n  url: \\\"https://arxiv.org/abs/2307.01850\\\"\\n  category: background\\n  role: \\\"提出 Model Autophagy Disorder (MAD) 概念——自消费式生成模型的退化\\\"\\n  key_findings: \\\"分析三种自消费循环（fully synthetic、synthetic augmentation、fresh data）；无新鲜真实数据时质量或多样性不可避免下降；即使保留原始训练数据也可能退化\\\"\\n  relevance_to_us: \\\"MAD 的数学框架帮助理解不同污染程度下的退化动力学，为我们的收敛理论提供上下文\\\"\\n\\n- id: dohmatob_2025_strong_collapse\\n  title: \\\"Strong Model Collapse\\\"\\n  authors: \\\"Elvis Dohmatob, Yunzhen Feng, Arjun Subramonian, Julia Kempe\\\"\\n  venue: \\\"ICLR 2025 (Spotlight)\\\"\\n  year: 2025\\n  arxiv_id: \\\"2410.04840\\\"\\n  url: \\\"https://arxiv.org/abs/2410.04840\\\"\\n  category: background\\n  role: \\\"证明即使极少量合成数据（1/1000）也能导致 model collapse\\\"\\n  key_findings: \\\"在 scaling laws 框架下建立 strong model collapse；用算子值自由概率论获得测试误差的 bias-variance 分解；更大模型可放大 collapse 效应\\\"\\n  relevance_to_us: \\\"强化了我们工作的必要性——即使少量合成污染也需要处理，仅靠增加数据量无法解决\\\"\\n\\n- id: nait_saada_2025_quality_illusion\\n  title: \\\"The Data-Quality Illusion: Rethinking Classifier-Based Quality Filtering for LLM Pretraining\\\"\\n  authors: \\\"Thiziri Nait Saada, Louis Bethune, Michal Klein, David Grangier, Marco Cuturi, Pierre Ablin\\\"\\n  venue: \\\"arXiv preprint\\\"\\n  year: 2025\\n  url: \\\"https://arxiv.org/abs/2510.00866\\\"\\n  category: background\\n  role: \\\"质疑基于分类器的数据质量评分是否真正捕获了有意义的质量概念\\\"\\n  key_findings: \\\"CQF 改善下游任务但不一定改善语言建模；质量分类器隐式偏向其监督目标的数据分布；质量桶与特定 benchmark 对齐\\\"\\n  relevance_to_us: \\\"提醒我们检测器置信度 q 不等于真实质量——需要理论保证 b* 在检测器有偏时仍然有效\\\"\\n\\n- id: guo_2025_escaping_collapse\\n  title: \\\"Escaping Model Collapse via Synthetic Data Verification\\\"\\n  venue: \\\"arXiv preprint\\\"\\n  year: 2025\\n  arxiv_id: \\\"2510.16657\\\"\\n  url: \\\"https://arxiv.org/abs/2510.16657\\\"\\n  category: background\\n  role: \\\"提出验证机制筛选合成数据质量，与 detection-based 方法互补\\\"\\n  key_findings: \\\"通过验证机制在合成数据生成后筛选质量，与基于检测器的事后加权方法互补\\\"\\n  relevance_to_us: \\\"verification-based 方法是另一条技术路线——他们做生成时验证，我们做训练时加权\\\"\\n\\n- id: cheng_2025_contamination_survey\\n  title: \\\"A Survey on Data Contamination for Large Language Models\\\"\\n  authors: \\\"Yuxing Cheng, Yi Chang, Yuan Wu\\\"\\n  venue: \\\"arXiv preprint\\\"\\n  year: 2025\\n  arxiv_id: \\\"2502.14425\\\"\\n  url: \\\"https://arxiv.org/abs/2502.14425\\\"\\n  category: background\\n  role: \\\"数据污染问题的全面综述，覆盖检测方法和 contamination-free 评估策略\\\"\\n  key_findings: \\\"系统整理训练/测试数据重叠的检测方法（MIA-based、reference-based、data updating/rewriting）；分析 contamination 对 benchmark 可靠性的影响；提出三类 contamination-free 评估策略\\\"\\n  relevance_to_us: \\\"为我们的 problem statement 提供全面综述支撑——pretraining data contamination 是 LLM 社区公认的系统性问题\\\"\\n\\n- id: wei_2024_data_watermarks\\n  title: \\\"Proving Membership in LLM Pretraining Data via Data Watermarks\\\"\\n  authors: \\\"Johnny Tian-Zheng Wei, Ryan Yixiang Wang, Robin Jia\\\"\\n  venue: \\\"arXiv preprint\\\"\\n  year: 2024\\n  arxiv_id: \\\"2402.10892\\\"\\n  url: \\\"https://arxiv.org/abs/2402.10892\\\"\\n  category: background\\n  role: \\\"用数据水印证明数据集是否在 LLM 预训练中被使用，数据溯源的主动方案\\\"\\n  key_findings: \\\"在公开发布前嵌入随机水印，检测建模为假设检验（控制误检率）；两种水印：随机序列插入和 Unicode lookalike 替换；水印强度随数据集增大而减弱但随模型增大而保持\\\"\\n  relevance_to_us: \\\"主动 provenance 方案（事前水印）vs 我们的被动方案（事后检测+加权）；互补但不冲突\\\"\\n\\n# ============================================================\\n# Category: evaluation\\n# 评估方法相关\\n# ============================================================\\n\\n- id: mitchell_2023_detectgpt\\n  title: \\\"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\\\"\\n  authors: \\\"Eric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher D. Manning, Chelsea Finn\\\"\\n  venue: \\\"ICML 2023\\\"\\n  year: 2023\\n  url: \\\"https://arxiv.org/abs/2301.11305\\\"\\n  category: evaluation\\n  role: \\\"零样本机器生成文本检测方法——我们的检测器 q 的基线方法之一\\\"\\n  key_findings: \\\"LLM 生成的文本倾向于占据模型对数概率函数的负曲率区域；无需训练分类器、收集数据集或水印；在 GPT-NeoX 假新闻检测上从 0.81 AUROC 提升到 0.95\\\"\\n  relevance_to_us: \\\"可作为计算合成概率 q 的检测器之一；其概率曲率方法可能与我们的权重公式有理论联系\\\"\\n\\n- id: shi_2024_minkprob\\n  title: \\\"Detecting Pretraining Data from Large Language Models\\\"\\n  authors: \\\"Weijia Shi, Anirudh Ajith, Mengzhou Xia, Yangsibo Huang, Daogao Liu, Terra Blevins, Danqi Chen, Luke Zettlemoyer\\\"\\n  venue: \\\"ICLR 2024\\\"\\n  year: 2024\\n  url: \\\"https://arxiv.org/abs/2310.16789\\\"\\n  category: evaluation\\n  role: \\\"Min-K% Prob 方法——检测数据是否在预训练集中的无参考方法\\\"\\n  key_findings: \\\"已训练数据包含更少低概率异常 token；取最低 K% token 概率的平均值判断；在 WikiMIA 上比最佳基线高 7.4 AUC；无需参考模型\\\"\\n  relevance_to_us: \\\"Min-K% Prob 可作为估计合成概率 q 的候选方法；其 membership inference 思路可扩展为连续置信度估计\\\"\\n\\n- id: kuo_2024_data_weighting\\n  title: \\\"Not All LLM-Generated Data Are Equal: Rethinking Data Weighting in Text Classification\\\"\\n  authors: \\\"Hsun-Yu Kuo et al.\\\"\\n  venue: \\\"arXiv preprint\\\"\\n  year: 2024\\n  url: \\\"https://arxiv.org/abs/2410.21526\\\"\\n  category: evaluation\\n  role: \\\"评估合成数据加权策略在文本分类中的效果\\\"\\n  key_findings: \\\"提出加权损失方法用少量真实数据对齐合成数据分布；在 BERT 级模型上稳定优于标准交叉熵和其他加权方法\\\"\\n  relevance_to_us: \\\"验证了合成数据需要差异化加权的思路；其评估框架可参考用于我们的下游任务评估\\\"\\n\", \"total_chars\": 15632, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0153tBb24cXpgNKZQcs3k2PA`</summary>

```json
{
  "project": "provenance_weight_training",
  "file": "writing_plan.yaml",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6b846b79-5ede-4f4c-b716-29d3245fa231",
  "uuid": "b222ddea-2f47-4327-884c-4234f1e2af42",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016YPGxu9Tvojy4syAp7yVrq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 722,
      "cache_read_input_tokens": 23822,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 722
      },
      "output_tokens": 36,
      "service_tier": "standard",
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

_source line 13 · 2026-05-15T23:35:11.042Z_

<details><summary>↩ Tool result · `toolu_0153tBb24cXpgNKZQcs3k2PA`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/writing_plan.yaml\", \"content\": \"# Writing Plan — provenance_weight_training\\n# Generated: 2026-05-15\\n# Contract for downstream writing Workers\\n\\nvenue: EMNLP 2026 ARR May 25\\ndeadline: 2026-05-25\\npage_limit: 8 (+ unlimited appendix)\\n\\ntitle: \\\"Minimum Intervention Reweighting: Adaptive Exponent Selection for Contamination-Aware Pretraining\\\"\\n# 备选:\\n# - \\\"Dual-Constrained Adaptive Reweighting for Pretraining on Contaminated Web Corpora\\\"\\n# - \\\"How Much to Downweight? Principled Exponent Selection for Contamination-Aware Pretraining\\\"\\n\\nabstract_outline:\\n  - sentence_1: \\\"Web pretraining corpora contain 20–60% machine-generated text of unknown provenance, and naive training on such mixtures degrades model quality (model collapse).\\\"\\n  - sentence_2: \\\"Existing detect-and-reweight methods (Drayson et al., 2025) require per-model validation-based grid search over the weighting exponent b, which is expensive and fragile.\\\"\\n  - sentence_3: \\\"We propose a dual-constrained adaptive b* that jointly enforces a quality lower bound (α_eff ≥ τ) and a stability upper bound (ESS ≥ n_min), yielding the minimum intervention—the smallest b that achieves sufficient cleaning per batch, with zero validation cost.\\\"\\n  - sentence_4: \\\"On FineWeb with Qwen3-0.6B, adaptive b* matches grid-search-optimal performance within seed variance while eliminating 6× search cost, and outperforms both uniform training and the max-intervention (ESS-only) baseline.\\\"\\n\\n# ============================================================\\n# SECTIONS\\n# ============================================================\\n\\nsections:\\n\\n  introduction:\\n    target_pages: 1.0\\n    key_points:\\n      - \\\"Web corpora contamination is pervasive (20–60%) and growing; strong model collapse occurs even at low contamination (Dohmatob et al., 2025)\\\"\\n      - \\\"Detect-and-reweight via w=(1-q)^b is effective (Drayson et al., 2025), but b selection requires per-model validation grid search\\\"\\n      - \\\"Problem statement: given per-sample detector scores q, how to choose b without validation?\\\"\\n      - \\\"Our answer: dual-constrained adaptive b* — α_eff(b) ≥ τ (quality floor) + ESS(b) ≥ n_min (stability ceiling) → minimum intervention principle\\\"\\n      - \\\"Key insight: α_eff monotonically increasing, ESS monotonically decreasing → b has a lower bound b_τ and upper bound b_ESS; b* = b_τ when feasible\\\"\\n    contributions:\\n      - \\\"Dual-constrained framework for adaptive b* selection with minimum intervention semantics (Section 3)\\\"\\n      - \\\"Empirical demonstration that adaptive b* matches grid-best within seed variance at zero validation cost (Section 5)\\\"\\n      - \\\"Evidence that minimum intervention (dual-constraint) outperforms maximum intervention (ESS-only), and that a lightweight TF-IDF+LR detector suffices (Section 5)\\\"\\n    evidence:\\n      - adaptive_fix_seed42\\n      - adaptive_fix_seed123\\n      - adaptive_fix_seed456\\n      - ess_only_seed42\\n\\n  related_work:\\n    target_pages: 1.0\\n    groups:\\n      synthetic_contamination_and_collapse:\\n        narrative: \\\"Model collapse under recursive/contaminated training\\\"\\n        papers:\\n          - shumailov_2024_model_collapse\\n          - alemohammad_2024_mad\\n          - dohmatob_2025_strong_collapse\\n          - cheng_2025_contamination_survey\\n      detect_and_reweight:\\n        narrative: \\\"Detection-based reweighting and filtering for contaminated data\\\"\\n        papers:\\n          - drayson_2025_detection_collapse    # direct competitor, most detailed comparison\\n          - feng_2025_beyond_collapse          # hard filtering via verifier\\n          - guo_2025_escaping_collapse         # verification-based\\n          - mitchell_2023_detectgpt            # detector method\\n          - shi_2024_minkprob                  # detector method\\n      data_mixing_and_reweighting:\\n        narrative: \\\"Domain- and instance-level data weighting for LLM pretraining\\\"\\n        papers:\\n          - xie_2023_doremi\\n          - xie_2023_dsir\\n          - he_2024_softdedup\\n          - sow_2025_dynamic_reweighting\\n          - chen_2025_aioli\\n          - ye_2025_data_mixing_laws\\n          - yang_2026_data_mixing_agent\\n          - kuo_2024_data_weighting\\n      theoretical_foundations:\\n        narrative: \\\"Optimal weighting theory and importance sampling diagnostics\\\"\\n        papers:\\n          - he_2025_golden_ratio\\n          - wang_2026_survive_contamination\\n          - vehtari_2024_psis\\n          - kimura_2024_iw_survey\\n    key_points:\\n      - \\\"Position Drayson as closest prior work: same w=(1-q)^b formula, but b is a per-model hyperparameter chosen via validation grid search\\\"\\n      - \\\"Distinguish from Golden Ratio (requires known proportion) and DoReMi/DSIR (domain-level, not instance-level contamination)\\\"\\n      - \\\"Highlight gap: no existing method provides principled per-batch b selection without validation\\\"\\n\\n  method:\\n    target_pages: 2.5\\n    subsections:\\n      problem_setup:\\n        key_points:\\n          - \\\"Training corpus D = D_real ∪ D_synth, proportion unknown\\\"\\n          - \\\"Detector provides per-sample q(x) ∈ [0,1] (synthetic probability)\\\"\\n          - \\\"Weighting formula w(x) = (1-q(x))^b, shared with Drayson et al.\\\"\\n          - \\\"Goal: choose b per-batch to maximize training quality without validation\\\"\\n        evidence: []\\n      dual_constraint_framework:\\n        key_points:\\n          - \\\"Define α_eff(b) = Σ_i w_i · 1[real_i] / Σ_i w_i — effective real proportion after reweighting\\\"\\n          - \\\"Define ESS(b) = (Σ w_i)² / Σ w_i² — Kish's effective sample size\\\"\\n          - \\\"Monotonicity: α_eff(b) strictly increasing (Proposition 1, proof via Cov_w(x, ln x) ≥ 0); ESS(b) strictly decreasing\\\"\\n          - \\\"Quality constraint: α_eff(b) ≥ τ → lower bound b_τ (at least this much cleaning)\\\"\\n          - \\\"Stability constraint: ESS(b) ≥ n_min → upper bound b_ESS (at most this much cleaning)\\\"\\n          - \\\"b* = inf{b ≥ 0 : α_eff(b) ≥ τ} subject to ESS(b) ≥ n_min\\\"\\n          - \\\"Minimum intervention principle: use the smallest b that achieves the quality floor\\\"\\n        evidence: []\\n      algorithm:\\n        key_points:\\n          - \\\"Algorithm 1: Per-batch b* solver (bisection on α_eff, check ESS feasibility)\\\"\\n          - \\\"Three regimes per batch: (1) already clean → b*=0; (2) α_eff binding → b*=b_τ; (3) ESS binding → b*=b_ESS\\\"\\n          - \\\"Implementation: loss reweighting (continuous gradient weighting) vs Drayson's SIR (discrete resampling)\\\"\\n          - \\\"Complexity: O(B log(1/ε)) per batch, negligible vs forward/backward pass\\\"\\n        evidence: []\\n      hyperparameters:\\n        key_points:\\n          - \\\"τ (quality threshold): theoretically motivated by convergence rate ∝ α (Wang et al., 2026); empirically, wide safe range [0.5, 0.8] with default τ=0.8\\\"\\n          - \\\"n_min (ESS floor): default n_min=2; robust across {2,3}; n_min=1 removes stability constraint (degrades); n_min ≥ batch_size trivially forces b*=0\\\"\\n          - \\\"Both have principled defaults set once, no per-model tuning needed\\\"\\n        evidence:\\n          - tau_05_seed42\\n          - tau_06_seed42\\n          - tau_07_seed42\\n          - adaptive_fix_seed42  # tau=0.8\\n          - tau_09_seed42\\n          - tau_095_seed42\\n          - nmin1_seed42\\n\\n  experiments:\\n    target_pages: 1.0\\n    key_points:\\n      - \\\"Base model: Qwen3-0.6B pretrained from scratch on FineWeb subset\\\"\\n      - \\\"Data: 132M+ tokens, 40% synthetic injection (Qwen3-0.6B self-generated), uniform random mixing\\\"\\n      - \\\"Detector: TF-IDF + Logistic Regression (AUC=0.939, calibrated ECE=0.048)\\\"\\n      - \\\"Training: 6103 steps, batch_size=4, AdamW, cosine schedule\\\"\\n      - \\\"Evaluation: held-out eval_ppl on balanced real/synthetic held-out set\\\"\\n      - \\\"All comparisons use 3 random seeds (42, 123, 456) for statistical reliability\\\"\\n    subsections:\\n      baselines:\\n        items:\\n          - \\\"Uniform: w=1 for all samples (no contamination handling)\\\"\\n          - \\\"Grid-b: fixed b ∈ {0.5, 1.0, 1.5, 2.0, 3.0, 5.0}, best selected post-hoc\\\"\\n          - \\\"ESS-only: b* = max{b : ESS(b) ≥ n_min} (maximum intervention, no α_eff constraint)\\\"\\n          - \\\"Golden Ratio: w*=1/φ ≈ 0.618 for synthetic samples (oracle, requires known proportion)\\\"\\n      experiment_groups:\\n        main_comparison:\\n          description: \\\"Adaptive b* vs grid-best vs uniform vs ESS-only vs golden ratio\\\"\\n          exp_ids:\\n            - adaptive_fix_seed42\\n            - adaptive_fix_seed123\\n            - adaptive_fix_seed456\\n            - uniform_seed42\\n            - uniform_seed123\\n            - uniform_seed456\\n            - grid_b_seed42   # b=0.5 best\\n            - grid_b_seed123\\n            - grid_b_seed456\\n            - ess_only_seed42\\n            - ess_only_seed123   # running\\n            - ess_only_seed456   # running\\n            - golden_ratio_seed42\\n        tau_sweep:\\n          description: \\\"τ ∈ {0.5, 0.6, 0.7, 0.8, 0.9, 0.95} sensitivity analysis\\\"\\n          exp_ids:\\n            - tau_05_seed42\\n            - tau_06_seed42\\n            - tau_07_seed42\\n            - adaptive_fix_seed42   # τ=0.8\\n            - tau_09_seed42\\n            - tau_095_seed42\\n        nmin_sensitivity:\\n          description: \\\"n_min ∈ {1, 2, 3, 4} sensitivity analysis\\\"\\n          exp_ids:\\n            - nmin1_seed42\\n            - adaptive_fix_seed42   # n_min=2\\n            - adaptive_seed42       # n_min=3\\n            - nmin4_seed42          # running\\n        batch_size:\\n          description: \\\"batch_size ∈ {4, 8} generalization (n_min=2 fixed)\\\"\\n          exp_ids:\\n            - adaptive_fix_seed42      # bs=4\\n            - bs8_nmin2_seed42_r2      # bs=8, running\\n    evidence:\\n      - all exp_ids listed above\\n\\n  results:\\n    target_pages: 1.5\\n    key_points:\\n      - \\\"Main result: adaptive b* PPL within seed variance of grid-best (aggregate ratio 88.6%), both beating uniform by ~0.04 PPL\\\"\\n      - \\\"ESS-only (max intervention) PPL=17.73 — worse than uniform (17.69), confirming minimum > maximum intervention\\\"\\n      - \\\"Golden ratio PPL=17.654 ≈ adaptive — oracle baseline matched without known proportion\\\"\\n      - \\\"τ sweep: [0.5, 0.8] all beat uniform; τ=0.8 optimal (PPL=17.653); τ>0.8 degrades due to b* inflation\\\"\\n      - \\\"n_min: n_min=2 stable across 3 seeds; n_min=1 degrades (no stability constraint); n_min=3 also works; n_min=4 expected to force b*≈0\\\"\\n      - \\\"Binding constraint analysis: 49.9% clean (b*=0), 20.2% α_eff-binding, 30.0% ESS-binding; when α_eff binds, b*=1.67 vs ESS-only's 4.15\\\"\\n      - \\\"Detector: lightweight TF-IDF+LR (AUC=0.939) sufficient; calibration (ECE=0.048) more important than raw AUC\\\"\\n    evidence:\\n      - adaptive_fix_seed42\\n      - adaptive_fix_seed123\\n      - adaptive_fix_seed456\\n      - uniform_seed42\\n      - uniform_seed123\\n      - uniform_seed456\\n      - ess_only_seed42\\n      - golden_ratio_seed42\\n      - tau_05_seed42\\n      - tau_06_seed42\\n      - tau_07_seed42\\n      - tau_09_seed42\\n      - tau_095_seed42\\n      - nmin1_seed42\\n      - detector_tfidf_lr\\n\\n  discussion:\\n    target_pages: 0.5\\n    key_points:\\n      - \\\"Minimum intervention principle: why doing less is better — over-downweighting discards useful gradient signal from borderline samples\\\"\\n      - \\\"τ as practical dial: controls the quality-efficiency tradeoff; [0.5, 0.8] safe range gives practitioners a clear operating region\\\"\\n      - \\\"Connection to convergence theory: Wang et al. (2026) show convergence rate ∝ α; our τ serves as a proxy for α without requiring known proportions\\\"\\n    limitations:\\n      - \\\"Single model scale (0.6B) — batch-level statistics may behave differently at 3B+ where batch sizes are larger\\\"\\n      - \\\"Controlled injection (uniform random) — real web contamination has domain-skewed distribution\\\"\\n      - \\\"Single detector family (TF-IDF+LR) — detector quality ablation not yet complete\\\"\\n      - \\\"τ is an empirical hyperparameter; the convergence theory (Wang et al.) requires known α, which we do not assume\\\"\\n      - \\\"Effect size ~0.3% PPL at 0.6B/40% contamination — expected to amplify at higher contamination and larger scale\\\"\\n    evidence: []\\n\\n  conclusion:\\n    target_pages: 0.3\\n    key_points:\\n      - \\\"Dual-constrained adaptive b* provides principled, validation-free \\n\\n... [截断: 省略 9042 字符，传 max_chars=0 获取完整内容]\", \"total_chars\": 21042, \"truncated\": true}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6b846b79-5ede-4f4c-b716-29d3245fa231",
  "uuid": "c7e894ee-65c6-42e4-9fab-3d8a64de4258",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/writing_plan.yaml\\\", \\\"content\\\": \\\"# Writing Plan — provenance_weight_training\\\\n# Generated: 2026-05-15\\\\n# Contract for downstream writing Workers\\\\n\\\\nvenue: EMNLP 2026 ARR May 25\\\\ndeadline: 2026-05-25\\\\npage_limit: 8 (+ unlimited appendix)\\\\n\\\\ntitle: \\\\\\\"Minimum Intervention Reweighting: Adaptive Exponent Selection for Contamination-Aware Pretraining\\\\\\\"\\\\n# 备选:\\\\n# - \\\\\\\"Dual-Constrained Adaptive Reweighting for Pretraining on Contaminated Web Corpora\\\\\\\"\\\\n# - \\\\\\\"How Much to Downweight? Principled Exponent Selection for Contamination-Aware Pretraining\\\\\\\"\\\\n\\\\nabstract_outline:\\\\n  - sentence_1: \\\\\\\"Web pretraining corpora contain 20–60% machine-generated text of unknown provenance, and naive training on such mixtures degrades model quality (model collapse).\\\\\\\"\\\\n  - sentence_2: \\\\\\\"Existing detect-and-reweight methods (Drayson et al., 2025) require per-model validation-based grid search over the weighting exponent b, which is expensive and fragile.\\\\\\\"\\\\n  - sentence_3: \\\\\\\"We propose a dual-constrained adaptive b* that jointly enforces a quality lower bound (α_eff ≥ τ) and a stability upper bound (ESS ≥ n_min), yielding the minimum intervention—the smallest b that achieves sufficient cleaning per batch, with zero validation cost.\\\\\\\"\\\\n  - sentence_4: \\\\\\\"On FineWeb with Qwen3-0.6B, adaptive b* matches grid-search-optimal performance within seed variance while eliminating 6× search cost, and outperforms both uniform training and the max-intervention (ESS-only) baseline.\\\\\\\"\\\\n\\\\n# ============================================================\\\\n# SECTIONS\\\\n# ============================================================\\\\n\\\\nsections:\\\\n\\\\n  introduction:\\\\n    target_pages: 1.0\\\\n    key_points:\\\\n      - \\\\\\\"Web corpora contamination is pervasive (20–60%) and growing; strong model collapse occurs even at low contamination (Dohmatob et al., 2025)\\\\\\\"\\\\n      - \\\\\\\"Detect-and-reweight via w=(1-q)^b is effective (Drayson et al., 2025), but b selection requires per-model validation grid search\\\\\\\"\\\\n      - \\\\\\\"Problem statement: given per-sample detector scores q, how to choose b without validation?\\\\\\\"\\\\n      - \\\\\\\"Our answer: dual-constrained adaptive b* — α_eff(b) ≥ τ (quality floor) + ESS(b) ≥ n_min (stability ceiling) → minimum intervention principle\\\\\\\"\\\\n      - \\\\\\\"Key insight: α_eff monotonically increasing, ESS monotonically decreasing → b has a lower bound b_τ and upper bound b_ESS; b* = b_τ when feasible\\\\\\\"\\\\n    contributions:\\\\n      - \\\\\\\"Dual-constrained framework for adaptive b* selection with minimum intervention semantics (Section 3)\\\\\\\"\\\\n      - \\\\\\\"Empirical demonstration that adaptive b* matches grid-best within seed variance at zero validation cost (Section 5)\\\\\\\"\\\\n      - \\\\\\\"Evidence that minimum intervention (dual-constraint) outperforms maximum intervention (ESS-only), and that a lightweight TF-IDF+LR detector suffices (Section 5)\\\\\\\"\\\\n    evidence:\\\\n      - adaptive_fix_seed42\\\\n      - adaptive_fix_seed123\\\\n      - adaptive_fix_seed456\\\\n      - ess_only_seed42\\\\n\\\\n  related_work:\\\\n    target_pages: 1.0\\\\n    groups:\\\\n      synthetic_contamination_and_collapse:\\\\n        narrative: \\\\\\\"Model collapse under recursive/contaminated training\\\\\\\"\\\\n        papers:\\\\n          - shumailov_2024_model_collapse\\\\n          - alemohammad_2024_mad\\\\n          - dohmatob_2025_strong_collapse\\\\n          - cheng_2025_contamination_survey\\\\n      detect_and_reweight:\\\\n        narrative: \\\\\\\"Detection-based reweighting and filtering for contaminated data\\\\\\\"\\\\n        papers:\\\\n          - drayson_2025_detection_collapse    # direct competitor, most detailed comparison\\\\n          - feng_2025_beyond_collapse          # hard filtering via verifier\\\\n          - guo_2025_escaping_collapse         # verification-based\\\\n          - mitchell_2023_detectgpt            # detector method\\\\n          - shi_2024_minkprob                  # detector method\\\\n      data_mixing_and_reweighting:\\\\n        narrative: \\\\\\\"Domain- and instance-level data weighting for LLM pretraining\\\\\\\"\\\\n        papers:\\\\n          - xie_2023_doremi\\\\n          - xie_2023_dsir\\\\n          - he_2024_softdedup\\\\n          - sow_2025_dynamic_reweighting\\\\n          - chen_2025_aioli\\\\n          - ye_2025_data_mixing_laws\\\\n          - yang_2026_data_mixing_agent\\\\n          - kuo_2024_data_weighting\\\\n      theoretical_foundations:\\\\n        narrative: \\\\\\\"Optimal weighting theory and importance sampling diagnostics\\\\\\\"\\\\n        papers:\\\\n          - he_2025_golden_ratio\\\\n          - wang_2026_survive_contamination\\\\n          - vehtari_2024_psis\\\\n          - kimura_2024_iw_survey\\\\n    key_points:\\\\n      - \\\\\\\"Position Drayson as closest prior work: same w=(1-q)^b formula, but b is a per-model hyperparameter chosen via validation grid search\\\\\\\"\\\\n      - \\\\\\\"Distinguish from Golden Ratio (requires known proportion) and DoReMi/DSIR (domain-level, not instance-level contamination)\\\\\\\"\\\\n      - \\\\\\\"Highlight gap: no existing method provides principled per-batch b selection without validation\\\\\\\"\\\\n\\\\n  method:\\\\n    target_pages: 2.5\\\\n    subsections:\\\\n      problem_setup:\\\\n        key_points:\\\\n          - \\\\\\\"Training corpus D = D_real ∪ D_synth, proportion unknown\\\\\\\"\\\\n          - \\\\\\\"Detector provides per-sample q(x) ∈ [0,1] (synthetic probability)\\\\\\\"\\\\n          - \\\\\\\"Weighting formula w(x) = (1-q(x))^b, shared with Drayson et al.\\\\\\\"\\\\n          - \\\\\\\"Goal: choose b per-batch to maximize training quality without validation\\\\\\\"\\\\n        evidence: []\\\\n      dual_constraint_framework:\\\\n        key_points:\\\\n          - \\\\\\\"Define α_eff(b) = Σ_i w_i · 1[real_i] / Σ_i w_i — effective real proportion after reweighting\\\\\\\"\\\\n          - \\\\\\\"Define ESS(b) = (Σ w_i)² / Σ w_i² — Kish's effective sample size\\\\\\\"\\\\n          - \\\\\\\"Monotonicity: α_eff(b) strictly increasing (Proposition 1, proof via Cov_w(x, ln x) ≥ 0); ESS(b) strictly decreasing\\\\\\\"\\\\n          - \\\\\\\"Quality constraint: α_eff(b) ≥ τ → lower bound b_τ (at least this much cleaning)\\\\\\\"\\\\n          - \\\\\\\"Stability constraint: ESS(b) ≥ n_min → upper bound b_ESS (at most this much cleaning)\\\\\\\"\\\\n          - \\\\\\\"b* = inf{b ≥ 0 : α_eff(b) ≥ τ} subject to ESS(b) ≥ n_min\\\\\\\"\\\\n          - \\\\\\\"Minimum intervention principle: use the smallest b that achieves the quality floor\\\\\\\"\\\\n        evidence: []\\\\n      algorithm:\\\\n        key_points:\\\\n          - \\\\\\\"Algorithm 1: Per-batch b* solver (bisection on α_eff, check ESS feasibility)\\\\\\\"\\\\n          - \\\\\\\"Three regimes per batch: (1) already clean → b*=0; (2) α_eff binding → b*=b_τ; (3) ESS binding → b*=b_ESS\\\\\\\"\\\\n          - \\\\\\\"Implementation: loss reweighting (continuous gradient weighting) vs Drayson's SIR (discrete resampling)\\\\\\\"\\\\n          - \\\\\\\"Complexity: O(B log(1/ε)) per batch, negligible vs forward/backward pass\\\\\\\"\\\\n        evidence: []\\\\n      hyperparameters:\\\\n        key_points:\\\\n          - \\\\\\\"τ (quality threshold): theoretically motivated by convergence rate ∝ α (Wang et al., 2026); empirically, wide safe range [0.5, 0.8] with default τ=0.8\\\\\\\"\\\\n          - \\\\\\\"n_min (ESS floor): default n_min=2; robust across {2,3}; n_min=1 removes stability constraint (degrades); n_min ≥ batch_size trivially forces b*=0\\\\\\\"\\\\n          - \\\\\\\"Both have principled defaults set once, no per-model tuning needed\\\\\\\"\\\\n        evidence:\\\\n          - tau_05_seed42\\\\n          - tau_06_seed42\\\\n          - tau_07_seed42\\\\n          - adaptive_fix_seed42  # tau=0.8\\\\n          - tau_09_seed42\\\\n          - tau_095_seed42\\\\n          - nmin1_seed42\\\\n\\\\n  experiments:\\\\n    target_pages: 1.0\\\\n    key_points:\\\\n      - \\\\\\\"Base model: Qwen3-0.6B pretrained from scratch on FineWeb subset\\\\\\\"\\\\n      - \\\\\\\"Data: 132M+ tokens, 40% synthetic injection (Qwen3-0.6B self-generated), uniform random mixing\\\\\\\"\\\\n      - \\\\\\\"Detector: TF-IDF + Logistic Regression (AUC=0.939, calibrated ECE=0.048)\\\\\\\"\\\\n      - \\\\\\\"Training: 6103 steps, batch_size=4, AdamW, cosine schedule\\\\\\\"\\\\n      - \\\\\\\"Evaluation: held-out eval_ppl on balanced real/synthetic held-out set\\\\\\\"\\\\n      - \\\\\\\"All comparisons use 3 random seeds (42, 123, 456) for statistical reliability\\\\\\\"\\\\n    subsections:\\\\n      baselines:\\\\n        items:\\\\n          - \\\\\\\"Uniform: w=1 for all samples (no contamination handling)\\\\\\\"\\\\n          - \\\\\\\"Grid-b: fixed b ∈ {0.5, 1.0, 1.5, 2.0, 3.0, 5.0}, best selected post-hoc\\\\\\\"\\\\n          - \\\\\\\"ESS-only: b* = max{b : ESS(b) ≥ n_min} (maximum intervention, no α_eff constraint)\\\\\\\"\\\\n          - \\\\\\\"Golden Ratio: w*=1/φ ≈ 0.618 for synthetic samples (oracle, requires known proportion)\\\\\\\"\\\\n      experiment_groups:\\\\n        main_comparison:\\\\n          description: \\\\\\\"Adaptive b* vs grid-best vs uniform vs ESS-only vs golden ratio\\\\\\\"\\\\n          exp_ids:\\\\n            - adaptive_fix_seed42\\\\n            - adaptive_fix_seed123\\\\n            - adaptive_fix_seed456\\\\n            - uniform_seed42\\\\n            - uniform_seed123\\\\n            - uniform_seed456\\\\n            - grid_b_seed42   # b=0.5 best\\\\n            - grid_b_seed123\\\\n            - grid_b_seed456\\\\n            - ess_only_seed42\\\\n            - ess_only_seed123   # running\\\\n            - ess_only_seed456   # running\\\\n            - golden_ratio_seed42\\\\n        tau_sweep:\\\\n          description: \\\\\\\"τ ∈ {0.5, 0.6, 0.7, 0.8, 0.9, 0.95} sensitivity analysis\\\\\\\"\\\\n          exp_ids:\\\\n            - tau_05_seed42\\\\n            - tau_06_seed42\\\\n            - tau_07_seed42\\\\n            - adaptive_fix_seed42   # τ=0.8\\\\n            - tau_09_seed42\\\\n            - tau_095_seed42\\\\n        nmin_sensitivity:\\\\n          description: \\\\\\\"n_min ∈ {1, 2, 3, 4} sensitivity analysis\\\\\\\"\\\\n          exp_ids:\\\\n            - nmin1_seed42\\\\n            - adaptive_fix_seed42   # n_min=2\\\\n            - adaptive_seed42       # n_min=3\\\\n            - nmin4_seed42          # running\\\\n        batch_size:\\\\n          description: \\\\\\\"batch_size ∈ {4, 8} generalization (n_min=2 fixed)\\\\\\\"\\\\n          exp_ids:\\\\n            - adaptive_fix_seed42      # bs=4\\\\n            - bs8_nmin2_seed42_r2      # bs=8, running\\\\n    evidence:\\\\n      - all exp_ids listed above\\\\n\\\\n  results:\\\\n    target_pages: 1.5\\\\n    key_points:\\\\n      - \\\\\\\"Main result: adaptive b* PPL within seed variance of grid-best (aggregate ratio 88.6%), both beating uniform by ~0.04 PPL\\\\\\\"\\\\n      - \\\\\\\"ESS-only (max intervention) PPL=17.73 — worse than uniform (17.69), confirming minimum > maximum intervention\\\\\\\"\\\\n      - \\\\\\\"Golden ratio PPL=17.654 ≈ adaptive — oracle baseline matched without known proportion\\\\\\\"\\\\n      - \\\\\\\"τ sweep: [0.5, 0.8] all beat uniform; τ=0.8 optimal (PPL=17.653); τ>0.8 degrades due to b* inflation\\\\\\\"\\\\n      - \\\\\\\"n_min: n_min=2 stable across 3 seeds; n_min=1 degrades (no stability constraint); n_min=3 also works; n_min=4 expected to force b*≈0\\\\\\\"\\\\n      - \\\\\\\"Binding constraint analysis: 49.9% clean (b*=0), 20.2% α_eff-binding, 30.0% ESS-binding; when α_eff binds, b*=1.67 vs ESS-only's 4.15\\\\\\\"\\\\n      - \\\\\\\"Detector: lightweight TF-IDF+LR (AUC=0.939) sufficient; calibration (ECE=0.048) more important than raw AUC\\\\\\\"\\\\n    evidence:\\\\n      - adaptive_fix_seed42\\\\n      - adaptive_fix_seed123\\\\n      - adaptive_fix_seed456\\\\n      - uniform_seed42\\\\n      - uniform_seed123\\\\n      - uniform_seed456\\\\n      - ess_only_seed42\\\\n      - golden_ratio_seed42\\\\n      - tau_05_seed42\\\\n      - tau_06_seed42\\\\n      - tau_07_seed42\\\\n      - tau_09_seed42\\\\n      - tau_095_seed42\\\\n      - nmin1_seed42\\\\n      - detector_tfidf_lr\\\\n\\\\n  discussion:\\\\n    target_pages: 0.5\\\\n    key_points:\\\\n      - \\\\\\\"Minimum intervention principle: why doing less is better — over-downweighting discards useful gradient signal from borderline samples\\\\\\\"\\\\n      - \\\\\\\"τ as practical dial: controls the quality-efficiency tradeoff; [0.5, 0.8] safe range gives practitioners a clear operating region\\\\\\\"\\\\n      - \\\\\\\"Connection to convergence theory: Wang et al. (2026) show convergence rate ∝ α; our τ serves as a proxy for α without requiring known proportions\\\\\\\"\\\\n    limitations:\\\\n      - \\\\\\\"Single model scale (0.6B) — batch-level statistics may behave differently at 3B+ where batch sizes are larger\\\\\\\"\\\\n      - \\\\\\\"Controlled injection (uniform random) — real web contamination has domain-skewed distribution\\\\\\\"\\\\n      - \\\\\\\"Single detector family (TF-IDF+LR) — detector quality ablation not yet complete\\\\\\\"\\\\n      - \\\\\\\"τ is an empirical hyperparameter; the convergence theory (Wang et al.) requires known α, which we do not assume\\\\\\\"\\\\n      - \\\\\\\"Effect size ~0.3% PPL at 0.6B/40% contamination — expected to amplify at higher contamination and larger scale\\\\\\\"\\\\n    evidence: []\\\\n\\\\n  conclusion:\\\\n    target_pages: 0.3\\\\n    key_points:\\\\n      - \\\\\\\"Dual-constrained adaptive b* provides principled, validation-free \\\\n\\\\n... [截断: 省略 9042 字符，传 max_chars=0 获取完整内容]\\\", \\\"total_chars\\\": 21042, \\\"truncated\\\": true}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/writing_plan.yaml\", \"content\": \"# Writing Plan — provenance_weight_training\\n# Generated: 2026-05-15\\n# Contract for downstream writing Workers\\n\\nvenue: EMNLP 2026 ARR May 25\\ndeadline: 2026-05-25\\npage_limit: 8 (+ unlimited appendix)\\n\\ntitle: \\\"Minimum Intervention Reweighting: Adaptive Exponent Selection for Contamination-Aware Pretraining\\\"\\n# 备选:\\n# - \\\"Dual-Constrained Adaptive Reweighting for Pretraining on Contaminated Web Corpora\\\"\\n# - \\\"How Much to Downweight? Principled Exponent Selection for Contamination-Aware Pretraining\\\"\\n\\nabstract_outline:\\n  - sentence_1: \\\"Web pretraining corpora contain 20–60% machine-generated text of unknown provenance, and naive training on such mixtures degrades model quality (model collapse).\\\"\\n  - sentence_2: \\\"Existing detect-and-reweight methods (Drayson et al., 2025) require per-model validation-based grid search over the weighting exponent b, which is expensive and fragile.\\\"\\n  - sentence_3: \\\"We propose a dual-constrained adaptive b* that jointly enforces a quality lower bound (α_eff ≥ τ) and a stability upper bound (ESS ≥ n_min), yielding the minimum intervention—the smallest b that achieves sufficient cleaning per batch, with zero validation cost.\\\"\\n  - sentence_4: \\\"On FineWeb with Qwen3-0.6B, adaptive b* matches grid-search-optimal performance within seed variance while eliminating 6× search cost, and outperforms both uniform training and the max-intervention (ESS-only) baseline.\\\"\\n\\n# ============================================================\\n# SECTIONS\\n# ============================================================\\n\\nsections:\\n\\n  introduction:\\n    target_pages: 1.0\\n    key_points:\\n      - \\\"Web corpora contamination is pervasive (20–60%) and growing; strong model collapse occurs even at low contamination (Dohmatob et al., 2025)\\\"\\n      - \\\"Detect-and-reweight via w=(1-q)^b is effective (Drayson et al., 2025), but b selection requires per-model validation grid search\\\"\\n      - \\\"Problem statement: given per-sample detector scores q, how to choose b without validation?\\\"\\n      - \\\"Our answer: dual-constrained adaptive b* — α_eff(b) ≥ τ (quality floor) + ESS(b) ≥ n_min (stability ceiling) → minimum intervention principle\\\"\\n      - \\\"Key insight: α_eff monotonically increasing, ESS monotonically decreasing → b has a lower bound b_τ and upper bound b_ESS; b* = b_τ when feasible\\\"\\n    contributions:\\n      - \\\"Dual-constrained framework for adaptive b* selection with minimum intervention semantics (Section 3)\\\"\\n      - \\\"Empirical demonstration that adaptive b* matches grid-best within seed variance at zero validation cost (Section 5)\\\"\\n      - \\\"Evidence that minimum intervention (dual-constraint) outperforms maximum intervention (ESS-only), and that a lightweight TF-IDF+LR detector suffices (Section 5)\\\"\\n    evidence:\\n      - adaptive_fix_seed42\\n      - adaptive_fix_seed123\\n      - adaptive_fix_seed456\\n      - ess_only_seed42\\n\\n  related_work:\\n    target_pages: 1.0\\n    groups:\\n      synthetic_contamination_and_collapse:\\n        narrative: \\\"Model collapse under recursive/contaminated training\\\"\\n        papers:\\n          - shumailov_2024_model_collapse\\n          - alemohammad_2024_mad\\n          - dohmatob_2025_strong_collapse\\n          - cheng_2025_contamination_survey\\n      detect_and_reweight:\\n        narrative: \\\"Detection-based reweighting and filtering for contaminated data\\\"\\n        papers:\\n          - drayson_2025_detection_collapse    # direct competitor, most detailed comparison\\n          - feng_2025_beyond_collapse          # hard filtering via verifier\\n          - guo_2025_escaping_collapse         # verification-based\\n          - mitchell_2023_detectgpt            # detector method\\n          - shi_2024_minkprob                  # detector method\\n      data_mixing_and_reweighting:\\n        narrative: \\\"Domain- and instance-level data weighting for LLM pretraining\\\"\\n        papers:\\n          - xie_2023_doremi\\n          - xie_2023_dsir\\n          - he_2024_softdedup\\n          - sow_2025_dynamic_reweighting\\n          - chen_2025_aioli\\n          - ye_2025_data_mixing_laws\\n          - yang_2026_data_mixing_agent\\n          - kuo_2024_data_weighting\\n      theoretical_foundations:\\n        narrative: \\\"Optimal weighting theory and importance sampling diagnostics\\\"\\n        papers:\\n          - he_2025_golden_ratio\\n          - wang_2026_survive_contamination\\n          - vehtari_2024_psis\\n          - kimura_2024_iw_survey\\n    key_points:\\n      - \\\"Position Drayson as closest prior work: same w=(1-q)^b formula, but b is a per-model hyperparameter chosen via validation grid search\\\"\\n      - \\\"Distinguish from Golden Ratio (requires known proportion) and DoReMi/DSIR (domain-level, not instance-level contamination)\\\"\\n      - \\\"Highlight gap: no existing method provides principled per-batch b selection without validation\\\"\\n\\n  method:\\n    target_pages: 2.5\\n    subsections:\\n      problem_setup:\\n        key_points:\\n          - \\\"Training corpus D = D_real ∪ D_synth, proportion unknown\\\"\\n          - \\\"Detector provides per-sample q(x) ∈ [0,1] (synthetic probability)\\\"\\n          - \\\"Weighting formula w(x) = (1-q(x))^b, shared with Drayson et al.\\\"\\n          - \\\"Goal: choose b per-batch to maximize training quality without validation\\\"\\n        evidence: []\\n      dual_constraint_framework:\\n        key_points:\\n          - \\\"Define α_eff(b) = Σ_i w_i · 1[real_i] / Σ_i w_i — effective real proportion after reweighting\\\"\\n          - \\\"Define ESS(b) = (Σ w_i)² / Σ w_i² — Kish's effective sample size\\\"\\n          - \\\"Monotonicity: α_eff(b) strictly increasing (Proposition 1, proof via Cov_w(x, ln x) ≥ 0); ESS(b) strictly decreasing\\\"\\n          - \\\"Quality constraint: α_eff(b) ≥ τ → lower bound b_τ (at least this much cleaning)\\\"\\n          - \\\"Stability constraint: ESS(b) ≥ n_min → upper bound b_ESS (at most this much cleaning)\\\"\\n          - \\\"b* = inf{b ≥ 0 : α_eff(b) ≥ τ} subject to ESS(b) ≥ n_min\\\"\\n          - \\\"Minimum intervention principle: use the smallest b that achieves the quality floor\\\"\\n        evidence: []\\n      algorithm:\\n        key_points:\\n          - \\\"Algorithm 1: Per-batch b* solver (bisection on α_eff, check ESS feasibility)\\\"\\n          - \\\"Three regimes per batch: (1) already clean → b*=0; (2) α_eff binding → b*=b_τ; (3) ESS binding → b*=b_ESS\\\"\\n          - \\\"Implementation: loss reweighting (continuous gradient weighting) vs Drayson's SIR (discrete resampling)\\\"\\n          - \\\"Complexity: O(B log(1/ε)) per batch, negligible vs forward/backward pass\\\"\\n        evidence: []\\n      hyperparameters:\\n        key_points:\\n          - \\\"τ (quality threshold): theoretically motivated by convergence rate ∝ α (Wang et al., 2026); empirically, wide safe range [0.5, 0.8] with default τ=0.8\\\"\\n          - \\\"n_min (ESS floor): default n_min=2; robust across {2,3}; n_min=1 removes stability constraint (degrades); n_min ≥ batch_size trivially forces b*=0\\\"\\n          - \\\"Both have principled defaults set once, no per-model tuning needed\\\"\\n        evidence:\\n          - tau_05_seed42\\n          - tau_06_seed42\\n          - tau_07_seed42\\n          - adaptive_fix_seed42  # tau=0.8\\n          - tau_09_seed42\\n          - tau_095_seed42\\n          - nmin1_seed42\\n\\n  experiments:\\n    target_pages: 1.0\\n    key_points:\\n      - \\\"Base model: Qwen3-0.6B pretrained from scratch on FineWeb subset\\\"\\n      - \\\"Data: 132M+ tokens, 40% synthetic injection (Qwen3-0.6B self-generated), uniform random mixing\\\"\\n      - \\\"Detector: TF-IDF + Logistic Regression (AUC=0.939, calibrated ECE=0.048)\\\"\\n      - \\\"Training: 6103 steps, batch_size=4, AdamW, cosine schedule\\\"\\n      - \\\"Evaluation: held-out eval_ppl on balanced real/synthetic held-out set\\\"\\n      - \\\"All comparisons use 3 random seeds (42, 123, 456) for statistical reliability\\\"\\n    subsections:\\n      baselines:\\n        items:\\n          - \\\"Uniform: w=1 for all samples (no contamination handling)\\\"\\n          - \\\"Grid-b: fixed b ∈ {0.5, 1.0, 1.5, 2.0, 3.0, 5.0}, best selected post-hoc\\\"\\n          - \\\"ESS-only: b* = max{b : ESS(b) ≥ n_min} (maximum intervention, no α_eff constraint)\\\"\\n          - \\\"Golden Ratio: w*=1/φ ≈ 0.618 for synthetic samples (oracle, requires known proportion)\\\"\\n      experiment_groups:\\n        main_comparison:\\n          description: \\\"Adaptive b* vs grid-best vs uniform vs ESS-only vs golden ratio\\\"\\n          exp_ids:\\n            - adaptive_fix_seed42\\n            - adaptive_fix_seed123\\n            - adaptive_fix_seed456\\n            - uniform_seed42\\n            - uniform_seed123\\n            - uniform_seed456\\n            - grid_b_seed42   # b=0.5 best\\n            - grid_b_seed123\\n            - grid_b_seed456\\n            - ess_only_seed42\\n            - ess_only_seed123   # running\\n            - ess_only_seed456   # running\\n            - golden_ratio_seed42\\n        tau_sweep:\\n          description: \\\"τ ∈ {0.5, 0.6, 0.7, 0.8, 0.9, 0.95} sensitivity analysis\\\"\\n          exp_ids:\\n            - tau_05_seed42\\n            - tau_06_seed42\\n            - tau_07_seed42\\n            - adaptive_fix_seed42   # τ=0.8\\n            - tau_09_seed42\\n            - tau_095_seed42\\n        nmin_sensitivity:\\n          description: \\\"n_min ∈ {1, 2, 3, 4} sensitivity analysis\\\"\\n          exp_ids:\\n            - nmin1_seed42\\n            - adaptive_fix_seed42   # n_min=2\\n            - adaptive_seed42       # n_min=3\\n            - nmin4_seed42          # running\\n        batch_size:\\n          description: \\\"batch_size ∈ {4, 8} generalization (n_min=2 fixed)\\\"\\n          exp_ids:\\n            - adaptive_fix_seed42      # bs=4\\n            - bs8_nmin2_seed42_r2      # bs=8, running\\n    evidence:\\n      - all exp_ids listed above\\n\\n  results:\\n    target_pages: 1.5\\n    key_points:\\n      - \\\"Main result: adaptive b* PPL within seed variance of grid-best (aggregate ratio 88.6%), both beating uniform by ~0.04 PPL\\\"\\n      - \\\"ESS-only (max intervention) PPL=17.73 — worse than uniform (17.69), confirming minimum > maximum intervention\\\"\\n      - \\\"Golden ratio PPL=17.654 ≈ adaptive — oracle baseline matched without known proportion\\\"\\n      - \\\"τ sweep: [0.5, 0.8] all beat uniform; τ=0.8 optimal (PPL=17.653); τ>0.8 degrades due to b* inflation\\\"\\n      - \\\"n_min: n_min=2 stable across 3 seeds; n_min=1 degrades (no stability constraint); n_min=3 also works; n_min=4 expected to force b*≈0\\\"\\n      - \\\"Binding constraint analysis: 49.9% clean (b*=0), 20.2% α_eff-binding, 30.0% ESS-binding; when α_eff binds, b*=1.67 vs ESS-only's 4.15\\\"\\n      - \\\"Detector: lightweight TF-IDF+LR (AUC=0.939) sufficient; calibration (ECE=0.048) more important than raw AUC\\\"\\n    evidence:\\n      - adaptive_fix_seed42\\n      - adaptive_fix_seed123\\n      - adaptive_fix_seed456\\n      - uniform_seed42\\n      - uniform_seed123\\n      - uniform_seed456\\n      - ess_only_seed42\\n      - golden_ratio_seed42\\n      - tau_05_seed42\\n      - tau_06_seed42\\n      - tau_07_seed42\\n      - tau_09_seed42\\n      - tau_095_seed42\\n      - nmin1_seed42\\n      - detector_tfidf_lr\\n\\n  discussion:\\n    target_pages: 0.5\\n    key_points:\\n      - \\\"Minimum intervention principle: why doing less is better — over-downweighting discards useful gradient signal from borderline samples\\\"\\n      - \\\"τ as practical dial: controls the quality-efficiency tradeoff; [0.5, 0.8] safe range gives practitioners a clear operating region\\\"\\n      - \\\"Connection to convergence theory: Wang et al. (2026) show convergence rate ∝ α; our τ serves as a proxy for α without requiring known proportions\\\"\\n    limitations:\\n      - \\\"Single model scale (0.6B) — batch-level statistics may behave differently at 3B+ where batch sizes are larger\\\"\\n      - \\\"Controlled injection (uniform random) — real web contamination has domain-skewed distribution\\\"\\n      - \\\"Single detector family (TF-IDF+LR) — detector quality ablation not yet complete\\\"\\n      - \\\"τ is an empirical hyperparameter; the convergence theory (Wang et al.) requires known α, which we do not assume\\\"\\n      - \\\"Effect size ~0.3% PPL at 0.6B/40% contamination — expected to amplify at higher contamination and larger scale\\\"\\n    evidence: []\\n\\n  conclusion:\\n    target_pages: 0.3\\n    key_points:\\n      - \\\"Dual-constrained adaptive b* provides principled, validation-free \\n\\n... [截断: 省略 9042 字符，传 max_chars=0 获取完整内容]\", \"total_chars\": 21042, \"truncated\": true}, \"error\": null, \"metadata\": {}}"
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
I have comprehensive context now. Let me write the Related Work section. I need to:

1. Follow the 4-group structure specified in the task
2. Use proper \citet{} and \citep{} formatting
3. Keep to ~600-700 words
4. Position Drayson carefully as closest competitor
5. End with the gap statement

Let me also check the artifacts directory exists.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6b846b79-5ede-4f4c-b716-29d3245fa231",
  "uuid": "1069ed2b-c874-4187-b106-e83b19c108fb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018iKWQeLuLUTuCtSpRL2ep4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20706,
      "cache_read_input_tokens": 24544,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20706
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

Now I have the full context. Let me check the output directory and write the draft.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6b846b79-5ede-4f4c-b716-29d3245fa231",
  "uuid": "f5dceba7-7038-4478-b299-bc5790008228",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018iKWQeLuLUTuCtSpRL2ep4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20706,
      "cache_read_input_tokens": 24544,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20706
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

<details open><summary>🔧 Tool call — Bash · `toolu_01MB68iHL2818j76XvKpruVK`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
  "description": "Check if paper directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6b846b79-5ede-4f4c-b716-29d3245fa231",
  "uuid": "42614911-935f-4fe6-a360-6069b4e412ad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018iKWQeLuLUTuCtSpRL2ep4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20706,
      "cache_read_input_tokens": 24544,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20706
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

_source line 17 · 2026-05-15T23:35:18.864Z_

<details><summary>↩ Tool result · `toolu_01MB68iHL2818j76XvKpruVK`</summary>

```text
conclusion.tex
conclusion_386ecc.tex
experiment_setup_draft.md
experiments.tex
experiments_1613c9.tex
introduction.tex
introduction_a663ee.tex
method.tex
method_76a694.tex
method_section_draft.md
related_work.tex
related_work_963aec.tex
results.tex
results_819b43.tex
writing_plan_v1_info.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6b846b79-5ede-4f4c-b716-29d3245fa231",
  "uuid": "34fb3fea-676a-4172-add4-f16b47f851ec",
  "tool_use_result": {
    "stdout": "conclusion.tex\nconclusion_386ecc.tex\nexperiment_setup_draft.md\nexperiments.tex\nexperiments_1613c9.tex\nintroduction.tex\nintroduction_a663ee.tex\nmethod.tex\nmethod_76a694.tex\nmethod_section_draft.md\nrelated_work.tex\nrelated_work_963aec.tex\nresults.tex\nresults_819b43.tex\nwriting_plan_v1_info.txt",
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

_source line 18_

<details><summary>Logged reasoning block</summary>

```text
Let me also check existing related_work.tex to see what's already been written.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6b846b79-5ede-4f4c-b716-29d3245fa231",
  "uuid": "53cc7f52-75de-4e00-8c65-c9684edf7dc7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017RLDNmNkLv48xP4GBZuD3j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 363,
      "cache_read_input_tokens": 45250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 363
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

Let me check the existing related_work.tex to avoid redundancy.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6b846b79-5ede-4f4c-b716-29d3245fa231",
  "uuid": "22942f8c-ef16-4cb0-987b-495c4cdab9f1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017RLDNmNkLv48xP4GBZuD3j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 363,
      "cache_read_input_tokens": 45250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 363
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

<details open><summary>🔧 Tool call — Read · `toolu_01Dq7UYqRyA2bZi1x6ZehvNe`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6b846b79-5ede-4f4c-b716-29d3245fa231",
  "uuid": "481ba3f1-e9d6-47b3-aa56-fd66492c90af",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017RLDNmNkLv48xP4GBZuD3j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 363,
      "cache_read_input_tokens": 45250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 363
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

_source line 21 · 2026-05-15T23:35:22.161Z_

<details><summary>↩ Tool result · `toolu_01Dq7UYqRyA2bZi1x6ZehvNe`</summary>

```text
1	\section{Related Work}
2	
3	\paragraph{Synthetic Contamination and Model Collapse.}
4	Training on recursively generated data leads to irreversible quality degradation---\emph{model collapse}~\citep{shumailov_2024_model_collapse}.
5	\citet{alemohammad_2024_mad} formalize this as Model Autophagy Disorder, showing that quality or diversity inevitably degrades without fresh real data, even when original training data is retained.
6	More critically, \citet{dohmatob_2025_strong_collapse} prove under scaling-law regimes that even a vanishingly small synthetic fraction (e.g., $1/1000$) suffices to trigger collapse, ruling out data scaling as a remedy.
7	\citet{cheng_2025_contamination_survey} survey the broader contamination landscape, confirming that synthetic content now constitutes an estimated 20--60\% of web corpora.
8	These results motivate \emph{contamination-aware} training strategies that explicitly account for synthetic provenance rather than treating all tokens equally.
9	
10	\paragraph{Detection and Filtering of Machine-Generated Text.}
11	Given the severity of contamination, a natural response is to detect and remove synthetic content.
12	DetectGPT~\citep{mitchell_2023_detectgpt} performs zero-shot detection via probability curvature, while Min-$k$\% Prob~\citep{shi_2024_minkprob} uses the average log-probability of the lowest-$k$\% tokens as a reference-free signal.
13	Both produce continuous confidence scores suitable as input to downstream weighting---including ours.
14	On the mitigation side, \citet{feng_2025_beyond_collapse} prove that even an imperfect verifier prevents collapse, but apply hard binary filtering that discards borderline samples.
15	\citet{guo_2025_escaping_collapse} similarly rely on verification-based selection.
16	Hard filtering requires a precision--recall threshold; soft reweighting avoids this trade-off by assigning continuous weights.
17	
18	Most directly related to our work, \citet{drayson_2025_detection_collapse} propose $w_j = (1{-}q_j)^b$ for collapse prevention via detect-and-reweight, where $q_j$ is the detector's synthetic probability.
19	We adopt the same weighting formula but differ in several fundamental ways.
20	\textbf{(i)}~Drayson et al.\ select $b$ via validation-set grid search and fix it throughout training; different model scales require different values ($b{=}10$ for ${\leq}360$M, $b{=}1$ for 1.7B), making the choice \emph{per-model} and expensive.
21	Our $b^*$ is derived per-batch from dual constraints ($\alpha_{\mathrm{eff}} \geq \tau$, $\mathrm{ESS} \geq n_{\min}$) at zero validation cost.
22	\textbf{(ii)}~Their SIR resampling discretizes the weight distribution; we apply direct loss reweighting with continuous gradients.
23	\textbf{(iii)}~They employ a ModernBERT-150M detector (AUC\,=\,0.986) on WikiText-2 (${\sim}$2M tokens); we show that a lightweight TF-IDF+LR detector (AUC\,=\,0.939) suffices on FineWeb-scale data (132M+ tokens), suggesting that score calibration matters more than raw detection accuracy.
24	
25	\paragraph{Data Mixing and Instance-Level Reweighting.}
26	A parallel line of work optimizes data composition without targeting synthetic contamination.
27	At the \emph{domain} level, DoReMi~\citep{xie_2023_doremi} learns mixture weights via Group DRO with a proxy model, DSIR~\citep{xie_2023_dsir} performs importance resampling with $n$-gram features, and \citet{ye_2025_data_mixing_laws} discover predictable functional forms relating mixing ratios to performance.
28	AIOLI~\citep{chen_2025_aioli} unifies these into an online adaptive framework, while \citet{yang_2026_data_mixing_agent} train an RL agent for domain-weight selection.
29	These methods do not address instance-level contamination within a domain.
30	At the \emph{instance} level, SoftDedup~\citep{he_2024_softdedup} downweights high-frequency samples via $n$-gram commonness, \citet{sow_2025_dynamic_reweighting} derive sample weights from per-sample loss with convergence guarantees, and \citet{kuo_2024_data_weighting} show that differentiated weighting of LLM-generated data improves downstream classification.
31	Our reweighting differs from all of these in being driven by \emph{provenance}---detector scores estimating human vs.\ synthetic origin---rather than loss, frequency, or domain membership.
32	
33	\paragraph{Theoretical Foundations.}
34	\citet{he_2025_golden_ratio} derive the optimal real-data weight under known mixture proportions, finding the golden-ratio reciprocal (${\approx}0.62$) optimal when both sources are equally sized.
35	Their result requires the contamination ratio $k$, unavailable in web-scale settings; we use it as an oracle baseline.
36	\citet{wang_2026_survive_contamination} prove that contaminated recursive training converges at a rate governed by the effective real-data fraction $\alpha$, providing the theoretical motivation for our quality threshold: ensuring $\alpha_{\mathrm{eff}}(b) \geq \tau$ guarantees a convergence-rate lower bound.
37	We operationalize this without the known-proportion assumption, estimating $\alpha_{\mathrm{eff}}$ from batch-level statistics online.
38	For the stability constraint, we build on Kish's effective sample size and the Pareto-smoothed importance sampling framework of \citet{vehtari_2024_psis}.
39	\citet{kimura_2024_iw_survey} provide a broader treatment of importance weighting under distribution shift, within which our provenance-based reweighting can be viewed as a special case of covariate-shift correction where the covariate is synthetic origin probability.
40	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6b846b79-5ede-4f4c-b716-29d3245fa231",
  "uuid": "e2fa60e7-bf00-4283-8faf-7ceafb760d1e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/related_work.tex",
      "content": "\\section{Related Work}\n\n\\paragraph{Synthetic Contamination and Model Collapse.}\nTraining on recursively generated data leads to irreversible quality degradation---\\emph{model collapse}~\\citep{shumailov_2024_model_collapse}.\n\\citet{alemohammad_2024_mad} formalize this as Model Autophagy Disorder, showing that quality or diversity inevitably degrades without fresh real data, even when original training data is retained.\nMore critically, \\citet{dohmatob_2025_strong_collapse} prove under scaling-law regimes that even a vanishingly small synthetic fraction (e.g., $1/1000$) suffices to trigger collapse, ruling out data scaling as a remedy.\n\\citet{cheng_2025_contamination_survey} survey the broader contamination landscape, confirming that synthetic content now constitutes an estimated 20--60\\% of web corpora.\nThese results motivate \\emph{contamination-aware} training strategies that explicitly account for synthetic provenance rather than treating all tokens equally.\n\n\\paragraph{Detection and Filtering of Machine-Generated Text.}\nGiven the severity of contamination, a natural response is to detect and remove synthetic content.\nDetectGPT~\\citep{mitchell_2023_detectgpt} performs zero-shot detection via probability curvature, while Min-$k$\\% Prob~\\citep{shi_2024_minkprob} uses the average log-probability of the lowest-$k$\\% tokens as a reference-free signal.\nBoth produce continuous confidence scores suitable as input to downstream weighting---including ours.\nOn the mitigation side, \\citet{feng_2025_beyond_collapse} prove that even an imperfect verifier prevents collapse, but apply hard binary filtering that discards borderline samples.\n\\citet{guo_2025_escaping_collapse} similarly rely on verification-based selection.\nHard filtering requires a precision--recall threshold; soft reweighting avoids this trade-off by assigning continuous weights.\n\nMost directly related to our work, \\citet{drayson_2025_detection_collapse} propose $w_j = (1{-}q_j)^b$ for collapse prevention via detect-and-reweight, where $q_j$ is the detector's synthetic probability.\nWe adopt the same weighting formula but differ in several fundamental ways.\n\\textbf{(i)}~Drayson et al.\\ select $b$ via validation-set grid search and fix it throughout training; different model scales require different values ($b{=}10$ for ${\\leq}360$M, $b{=}1$ for 1.7B), making the choice \\emph{per-model} and expensive.\nOur $b^*$ is derived per-batch from dual constraints ($\\alpha_{\\mathrm{eff}} \\geq \\tau$, $\\mathrm{ESS} \\geq n_{\\min}$) at zero validation cost.\n\\textbf{(ii)}~Their SIR resampling discretizes the weight distribution; we apply direct loss reweighting with continuous gradients.\n\\textbf{(iii)}~They employ a ModernBERT-150M detector (AUC\\,=\\,0.986) on WikiText-2 (${\\sim}$2M tokens); we show that a lightweight TF-IDF+LR detector (AUC\\,=\\,0.939) suffices on FineWeb-scale data (132M+ tokens), suggesting that score calibration matters more than raw detection accuracy.\n\n\\paragraph{Data Mixing and Instance-Level Reweighting.}\nA parallel line of work optimizes data composition without targeting synthetic contamination.\nAt the \\emph{domain} level, DoReMi~\\citep{xie_2023_doremi} learns mixture weights via Group DRO with a proxy model, DSIR~\\citep{xie_2023_dsir} performs importance resampling with $n$-gram features, and \\citet{ye_2025_data_mixing_laws} discover predictable functional forms relating mixing ratios to performance.\nAIOLI~\\citep{chen_2025_aioli} unifies these into an online adaptive framework, while \\citet{yang_2026_data_mixing_agent} train an RL agent for domain-weight selection.\nThese methods do not address instance-level contamination within a domain.\nAt the \\emph{instance} level, SoftDedup~\\citep{he_2024_softdedup} downweights high-frequency samples via $n$-gram commonness, \\citet{sow_2025_dynamic_reweighting} derive sample weights from per-sample loss with convergence guarantees, and \\citet{kuo_2024_data_weighting} show that differentiated weighting of LLM-generated data improves downstream classification.\nOur reweighting differs from all of these in being driven by \\emph{provenance}---detector scores estimating human vs.\\ synthetic origin---rather than loss, frequency, or domain membership.\n\n\\paragraph{Theoretical Foundations.}\n\\citet{he_2025_golden_ratio} derive the optimal real-data weight under known mixture proportions, finding the golden-ratio reciprocal (${\\approx}0.62$) optimal when both sources are equally sized.\nTheir result requires the contamination ratio $k$, unavailable in web-scale settings; we use it as an oracle baseline.\n\\citet{wang_2026_survive_contamination} prove that contaminated recursive training converges at a rate governed by the effective real-data fraction $\\alpha$, providing the theoretical motivation for our quality threshold: ensuring $\\alpha_{\\mathrm{eff}}(b) \\geq \\tau$ guarantees a convergence-rate lower bound.\nWe operationalize this without the known-proportion assumption, estimating $\\alpha_{\\mathrm{eff}}$ from batch-level statistics online.\nFor the stability constraint, we build on Kish's effective sample size and the Pareto-smoothed importance sampling framework of \\citet{vehtari_2024_psis}.\n\\citet{kimura_2024_iw_survey} provide a broader treatment of importance weighting under distribution shift, within which our provenance-based reweighting can be viewed as a special case of covariate-shift correction where the covariate is synthetic origin probability.\n",
      "numLines": 40,
      "startLine": 1,
      "totalLines": 40
    }
  }
}
```

</details>

---

### Assistant

_source line 22_

<details><summary>Logged reasoning block</summary>

```text
There's already a complete related_work.tex. The task asks me to write a related_work_draft.md. Let me look at the existing .tex - it's actually quite good and aligns well with the task specifications. But the task explicitly asks for a markdown draft at the specified path.

Let me compare what's requested vs. what exists:

The existing .tex has 4 paragraphs matching the 4 groups, uses \citet{} and \citep{}, and covers all the requested papers. It's well-written and around the right length.

But the task asks for a markdown draft. Let me write this as a clean markdown version that matches the task specifications closely. Actually, the existing .tex already covers everything requested. 

I need to create the markdown draft at the specified path. The existing .tex is solid at around 650 words, which fits the target range, but I should refine it to match the task's specific structure and emphasis requirements, particularly around the Drayson comparison point mentioned in the instructions. I'm refining the markdown draft to closely follow the LaTeX structure while strengthening the closing statement—specifically adding a clear gap about the lack of principled per-batch b selection methods that don't require validation data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6b846b79-5ede-4f4c-b716-29d3245fa231",
  "uuid": "8f369792-efbe-4443-a647-3803ebfc698d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018ea6awNvqUzDZrFji84kN3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1735,
      "cache_read_input_tokens": 45613,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1735
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

Existing `related_work.tex` is already strong (~650 words, 4 paragraphs, correct citations). I'll write the markdown draft with targeted refinements: sharpen the Drayson comparison, add the closing gap statement, and tighten a few transitions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6b846b79-5ede-4f4c-b716-29d3245fa231",
  "uuid": "1555c0ee-3126-4e8c-ae8d-624f614c3252",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018ea6awNvqUzDZrFji84kN3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1735,
      "cache_read_input_tokens": 45613,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1735
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

<details open><summary>🔧 Tool call — Write · `toolu_01Psir4cH1X41UcuVjX8dQfJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/related_work_draft.md",
  "content": "# Related Work — Draft\n\n## \\section{Related Work}\n\n\\paragraph{Synthetic Contamination and Model Collapse.}\nTraining on recursively generated data leads to irreversible quality degradation---\\emph{model collapse}~\\citep{shumailov_2024_model_collapse}.\n\\citet{alemohammad_2024_mad} formalize this as Model Autophagy Disorder, showing that quality or diversity inevitably degrades without fresh real data, even when original training data is retained.\nMore critically, \\citet{dohmatob_2025_strong_collapse} prove under scaling-law regimes that even a vanishingly small synthetic fraction (e.g., $1/1000$) suffices to trigger collapse, and that larger models can \\emph{amplify} rather than mitigate the effect---ruling out data scaling as a remedy.\n\\citet{cheng_2025_contamination_survey} survey the broader contamination landscape, confirming that synthetic content now constitutes an estimated 20--60\\% of web corpora.\nThese results motivate \\emph{contamination-aware} training strategies that explicitly account for synthetic provenance rather than treating all tokens equally.\n\n\\paragraph{Detection-Based Reweighting and Filtering.}\nGiven the severity of contamination, a natural response is to detect and remove synthetic content.\nDetectGPT~\\citep{mitchell_2023_detectgpt} performs zero-shot detection via probability curvature, while Min-$k$\\% Prob~\\citep{shi_2024_minkprob} uses the average log-probability of the lowest-$k$\\% tokens as a reference-free membership signal.\nBoth produce continuous confidence scores suitable as input to downstream weighting schemes, including ours.\nOn the mitigation side, \\citet{feng_2025_beyond_collapse} prove that even an imperfect verifier prevents collapse, but apply hard binary filtering that discards potentially useful borderline samples.\n\\citet{guo_2025_escaping_collapse} similarly rely on verification-based selection.\nHard filtering requires a precision--recall threshold and loses information; soft reweighting avoids this trade-off by assigning continuous weights.\n\nMost directly related to our work, \\citet{drayson_2025_detection_collapse} propose the detect-and-reweight formula $w_j = (1{-}q_j)^b$ for collapse prevention, where $q_j$ is the detector's synthetic probability.\nWe adopt the same weighting formula but differ in several fundamental ways.\n\\textbf{(i)}~Drayson et al.\\ select $b$ via validation-set grid search and fix it throughout training; different model scales require different values ($b{=}10$ for ${\\leq}360$M parameters, $b{=}1$ for 1.7B), making the choice \\emph{per-model} and expensive.\nOur $b^*$ is derived per-batch from dual constraints ($\\alpha_{\\mathrm{eff}} \\geq \\tau$, $\\mathrm{ESS} \\geq n_{\\min}$) at zero validation cost.\n\\textbf{(ii)}~Their SIR resampling discretizes the weight distribution into a resampled subset; we apply direct loss reweighting with continuous gradients, preserving the full batch.\n\\textbf{(iii)}~They employ a ModernBERT-150M detector (AUC\\,=\\,0.986) on WikiText-2 (${\\sim}$2M tokens); we show that a lightweight TF-IDF+LR detector (AUC\\,=\\,0.939) suffices at FineWeb scale (132M+ tokens), suggesting that score calibration matters more than raw detection accuracy.\n\n\\paragraph{Data Mixing and Instance-Level Reweighting.}\nA parallel line of work optimizes data composition without targeting synthetic contamination.\nAt the \\emph{domain} level, DoReMi~\\citep{xie_2023_doremi} learns mixture weights via Group DRO with a proxy model, DSIR~\\citep{xie_2023_dsir} performs importance resampling with $n$-gram features, and \\citet{ye_2025_data_mixing_laws} discover predictable functional forms relating mixing ratios to performance.\nAIOLI~\\citep{chen_2025_aioli} unifies these into an online adaptive framework.\nThese methods operate at the domain level and do not address instance-level contamination within a domain.\nAt the \\emph{instance} level, SoftDedup~\\citep{he_2024_softdedup} downweights high-frequency samples via $n$-gram commonness, and \\citet{sow_2025_dynamic_reweighting} derive sample weights from per-sample loss with convergence guarantees.\nOur reweighting differs from all of these in being driven by \\emph{provenance}---detector scores estimating human vs.\\ synthetic origin---rather than loss, frequency, or domain membership.\n\n\\paragraph{Theoretical Foundations.}\n\\citet{he_2025_golden_ratio} derive the optimal real-data weight under known mixture proportions, finding the golden-ratio reciprocal ($w^* \\approx 0.62$) optimal when both sources are equally sized.\nTheir result requires the contamination ratio $k$, which is unavailable in web-scale settings; we use it as an oracle baseline.\n\\citet{wang_2026_survive_contamination} prove that contaminated recursive training converges at a rate governed by the effective real-data fraction $\\alpha$, providing the theoretical motivation for our quality threshold: ensuring $\\alpha_{\\mathrm{eff}}(b) \\geq \\tau$ guarantees a convergence-rate lower bound.\nWe operationalize this insight without the known-proportion assumption by estimating $\\alpha_{\\mathrm{eff}}$ from batch-level detector statistics online.\nFor the stability constraint, we build on Kish's effective sample size and the Pareto-smoothed importance sampling diagnostics of \\citet{vehtari_2024_psis}.\n\\citet{kimura_2024_iw_survey} provide a broader treatment of importance weighting under distribution shift, within which our provenance-based reweighting can be viewed as covariate-shift correction where the covariate is synthetic-origin probability.\nTo our knowledge, no existing method provides principled, per-batch exponent selection for contamination-aware reweighting without relying on a held-out validation set or known contamination proportions.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6b846b79-5ede-4f4c-b716-29d3245fa231",
  "uuid": "adfba704-48b8-43bd-ac1d-a09d0c2ef920",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018ea6awNvqUzDZrFji84kN3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1735,
      "cache_read_input_tokens": 45613,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1735
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

_source line 25 · 2026-05-15T23:35:54.660Z_

<details><summary>↩ Tool result · `toolu_01Psir4cH1X41UcuVjX8dQfJ`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/related_work_draft.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6b846b79-5ede-4f4c-b716-29d3245fa231",
  "uuid": "fe08807d-95d7-4ee5-af61-c9224e84e57d",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/related_work_draft.md",
    "content": "# Related Work — Draft\n\n## \\section{Related Work}\n\n\\paragraph{Synthetic Contamination and Model Collapse.}\nTraining on recursively generated data leads to irreversible quality degradation---\\emph{model collapse}~\\citep{shumailov_2024_model_collapse}.\n\\citet{alemohammad_2024_mad} formalize this as Model Autophagy Disorder, showing that quality or diversity inevitably degrades without fresh real data, even when original training data is retained.\nMore critically, \\citet{dohmatob_2025_strong_collapse} prove under scaling-law regimes that even a vanishingly small synthetic fraction (e.g., $1/1000$) suffices to trigger collapse, and that larger models can \\emph{amplify} rather than mitigate the effect---ruling out data scaling as a remedy.\n\\citet{cheng_2025_contamination_survey} survey the broader contamination landscape, confirming that synthetic content now constitutes an estimated 20--60\\% of web corpora.\nThese results motivate \\emph{contamination-aware} training strategies that explicitly account for synthetic provenance rather than treating all tokens equally.\n\n\\paragraph{Detection-Based Reweighting and Filtering.}\nGiven the severity of contamination, a natural response is to detect and remove synthetic content.\nDetectGPT~\\citep{mitchell_2023_detectgpt} performs zero-shot detection via probability curvature, while Min-$k$\\% Prob~\\citep{shi_2024_minkprob} uses the average log-probability of the lowest-$k$\\% tokens as a reference-free membership signal.\nBoth produce continuous confidence scores suitable as input to downstream weighting schemes, including ours.\nOn the mitigation side, \\citet{feng_2025_beyond_collapse} prove that even an imperfect verifier prevents collapse, but apply hard binary filtering that discards potentially useful borderline samples.\n\\citet{guo_2025_escaping_collapse} similarly rely on verification-based selection.\nHard filtering requires a precision--recall threshold and loses information; soft reweighting avoids this trade-off by assigning continuous weights.\n\nMost directly related to our work, \\citet{drayson_2025_detection_collapse} propose the detect-and-reweight formula $w_j = (1{-}q_j)^b$ for collapse prevention, where $q_j$ is the detector's synthetic probability.\nWe adopt the same weighting formula but differ in several fundamental ways.\n\\textbf{(i)}~Drayson et al.\\ select $b$ via validation-set grid search and fix it throughout training; different model scales require different values ($b{=}10$ for ${\\leq}360$M parameters, $b{=}1$ for 1.7B), making the choice \\emph{per-model} and expensive.\nOur $b^*$ is derived per-batch from dual constraints ($\\alpha_{\\mathrm{eff}} \\geq \\tau$, $\\mathrm{ESS} \\geq n_{\\min}$) at zero validation cost.\n\\textbf{(ii)}~Their SIR resampling discretizes the weight distribution into a resampled subset; we apply direct loss reweighting with continuous gradients, preserving the full batch.\n\\textbf{(iii)}~They employ a ModernBERT-150M detector (AUC\\,=\\,0.986) on WikiText-2 (${\\sim}$2M tokens); we show that a lightweight TF-IDF+LR detector (AUC\\,=\\,0.939) suffices at FineWeb scale (132M+ tokens), suggesting that score calibration matters more than raw detection accuracy.\n\n\\paragraph{Data Mixing and Instance-Level Reweighting.}\nA parallel line of work optimizes data composition without targeting synthetic contamination.\nAt the \\emph{domain} level, DoReMi~\\citep{xie_2023_doremi} learns mixture weights via Group DRO with a proxy model, DSIR~\\citep{xie_2023_dsir} performs importance resampling with $n$-gram features, and \\citet{ye_2025_data_mixing_laws} discover predictable functional forms relating mixing ratios to performance.\nAIOLI~\\citep{chen_2025_aioli} unifies these into an online adaptive framework.\nThese methods operate at the domain level and do not address instance-level contamination within a domain.\nAt the \\emph{instance} level, SoftDedup~\\citep{he_2024_softdedup} downweights high-frequency samples via $n$-gram commonness, and \\citet{sow_2025_dynamic_reweighting} derive sample weights from per-sample loss with convergence guarantees.\nOur reweighting differs from all of these in being driven by \\emph{provenance}---detector scores estimating human vs.\\ synthetic origin---rather than loss, frequency, or domain membership.\n\n\\paragraph{Theoretical Foundations.}\n\\citet{he_2025_golden_ratio} derive the optimal real-data weight under known mixture proportions, finding the golden-ratio reciprocal ($w^* \\approx 0.62$) optimal when both sources are equally sized.\nTheir result requires the contamination ratio $k$, which is unavailable in web-scale settings; we use it as an oracle baseline.\n\\citet{wang_2026_survive_contamination} prove that contaminated recursive training converges at a rate governed by the effective real-data fraction $\\alpha$, providing the theoretical motivation for our quality threshold: ensuring $\\alpha_{\\mathrm{eff}}(b) \\geq \\tau$ guarantees a convergence-rate lower bound.\nWe operationalize this insight without the known-proportion assumption by estimating $\\alpha_{\\mathrm{eff}}$ from batch-level detector statistics online.\nFor the stability constraint, we build on Kish's effective sample size and the Pareto-smoothed importance sampling diagnostics of \\citet{vehtari_2024_psis}.\n\\citet{kimura_2024_iw_survey} provide a broader treatment of importance weighting under distribution shift, within which our provenance-based reweighting can be viewed as covariate-shift correction where the covariate is synthetic-origin probability.\nTo our knowledge, no existing method provides principled, per-batch exponent selection for contamination-aware reweighting without relying on a held-out validation set or known contamination proportions.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 26_

Now register the artifact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6b846b79-5ede-4f4c-b716-29d3245fa231",
  "uuid": "99259049-50b0-4f6c-aa1a-b71d1c526c0f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MKcz5NTA3SgauJ6Wx2tXBt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2433,
      "cache_read_input_tokens": 47348,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2433
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

_source line 27_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01E1HPXpiRBZpmD87UyEUfsF`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__append_idea",
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
  "session_id": "6b846b79-5ede-4f4c-b716-29d3245fa231",
  "uuid": "b79a2de5-daa4-42d7-9267-b50541a47960",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MKcz5NTA3SgauJ6Wx2tXBt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2433,
      "cache_read_input_tokens": 47348,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2433
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

_source line 28 · 2026-05-15T23:35:58.037Z_

<details><summary>↩ Tool result · `toolu_01E1HPXpiRBZpmD87UyEUfsF`</summary>

````text
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
  "session_id": "6b846b79-5ede-4f4c-b716-29d3245fa231",
  "uuid": "297f8e69-eb79-4922-ae79-9ad3e1ade137",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__append_idea"
    ],
    "query": "select:mcp__agent-ml-research__append_idea",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 29_

<details><summary>Logged reasoning block</summary>

```text
I need to find the register_artifact tool. Let me search for it.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6b846b79-5ede-4f4c-b716-29d3245fa231",
  "uuid": "2761cb81-a116-41ea-95e7-87e96a8fb0bb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0165smLUBA3YExdJm6BRoCxD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 299,
      "cache_read_input_tokens": 49781,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 299
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_012DGKj4w9fZRpSbMFpVHULP`</summary>

```json
{
  "query": "register_artifact",
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
  "session_id": "6b846b79-5ede-4f4c-b716-29d3245fa231",
  "uuid": "30fda631-f30a-4e9c-a1ff-4c524b482eac",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0165smLUBA3YExdJm6BRoCxD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 299,
      "cache_read_input_tokens": 49781,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 299
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

_source line 31 · 2026-05-15T23:36:00.827Z_

<details><summary>↩ Tool result · `toolu_012DGKj4w9fZRpSbMFpVHULP`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6b846b79-5ede-4f4c-b716-29d3245fa231",
  "uuid": "6f166814-648b-4af4-b3fb-09bb10905771",
  "tool_use_result": {
    "matches": [],
    "query": "register_artifact",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01BWrq67ZNZ1T1geY8SUZRbU`</summary>

```json
{
  "query": "artifact",
  "max_results": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6b846b79-5ede-4f4c-b716-29d3245fa231",
  "uuid": "18412d5d-c12e-40ac-87c9-5f48ba283fb0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DFYumZWV58UrqkjBzvW8N8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 125,
      "cache_read_input_tokens": 50080,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 125
      },
      "output_tokens": 56,
      "service_tier": "standard",
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

_source line 33 · 2026-05-15T23:36:03.397Z_

<details><summary>↩ Tool result · `toolu_01BWrq67ZNZ1T1geY8SUZRbU`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6b846b79-5ede-4f4c-b716-29d3245fa231",
  "uuid": "78cf8435-c56d-407e-b452-08ce1a542e6a",
  "tool_use_result": {
    "matches": [],
    "query": "artifact",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 34_

`register_artifact` tool not available in current tool set. Draft written to:

`artifacts/_project/paper/related_work_draft.md`

**Changes vs existing `related_work.tex`:**
- Added "larger models can *amplify* rather than mitigate" detail from Dohmatob (stronger motivation)
- Tightened Drayson (ii): clarified SIR "discretizes into a resampled subset" vs our "preserving the full batch"
- Removed `yang_2026_data_mixing_agent` and `kuo_2024_data_weighting` from data mixing paragraph (not in task spec, streamlines word count)
- Added closing gap statement: *"no existing method provides principled, per-batch exponent selection… without validation set or known contamination proportions"*
- ~670 words, 4 paragraphs, all citations use `\citet{}`/`\citep{}` format

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6b846b79-5ede-4f4c-b716-29d3245fa231",
  "uuid": "04ed3a8e-dca9-4c65-abe1-660ae1b856df",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0162UfUoxVFJWkp4MBcjXnES",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 90,
      "cache_read_input_tokens": 50205,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 90
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

_source line 35_

`register_artifact` tool not available in current tool set. Draft written to:

`artifacts/_project/paper/related_work_draft.md`

**Changes vs existing `related_work.tex`:**
- Added "larger models can *amplify* rather than mitigate" detail from Dohmatob (stronger motivation)
- Tightened Drayson (ii): clarified SIR "discretizes into a resampled subset" vs our "preserving the full batch"
- Removed `yang_2026_data_mixing_agent` and `kuo_2024_data_weighting` from data mixing paragraph (not in task spec, streamlines word count)
- Added closing gap statement: *"no existing method provides principled, per-batch exponent selection… without validation set or known contamination proportions"*
- ~670 words, 4 paragraphs, all citations use `\citet{}`/`\citep{}` format

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 68008,
  "duration_api_ms": 68849,
  "num_turns": 11,
  "stop_reason": "end_turn",
  "session_id": "6b846b79-5ede-4f4c-b716-29d3245fa231",
  "total_cost_usd": 0.509124,
  "usage": {
    "input_tokens": 15,
    "cache_creation_input_tokens": 38848,
    "cache_read_input_tokens": 348090,
    "output_tokens": 3611,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 38848,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 223,
        "cache_read_input_tokens": 50205,
        "cache_creation_input_tokens": 90,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 90
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1834,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001929,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 15,
      "outputTokens": 3611,
      "cacheReadInputTokens": 348090,
      "cacheCreationInputTokens": 38848,
      "webSearchRequests": 0,
      "costUSD": 0.507195,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "1af5a1df-49cf-473c-913f-e8ba40e19861"
}
```

</details>

---
