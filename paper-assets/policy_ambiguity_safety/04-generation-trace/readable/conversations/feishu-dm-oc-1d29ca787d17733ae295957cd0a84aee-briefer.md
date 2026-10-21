# feishu dm oc 1d29ca787d17733ae295957cd0a84aee briefer

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 12
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/feishu_dm_oc_1d29ca787d17733ae295957cd0a84aee_briefer.jsonl`
- **Structured JSON:** [`65895a36d836f3923bdf.json`](../../sessions/65/65895a36d836f3923bdf.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

12 recorded events

### User

_source line 1 · 2026-05-22T05:56:39.458756+00:00_

[飞书用户 曹晓玉 (ou_4d6ae15bdfe9c1c9ecc77b04af20b154)]: 你帮我看看这个项目的核心claim是什么，实验做得怎么样

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:dm:oc_1d29ca787d17733ae295957cd0a84aee:briefer",
  "source": "feishu:oc_1d29ca787d17733ae295957cd0a84aee"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-22T05:56:46.772361+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_roadmap",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:dm:oc_1d29ca787d17733ae295957cd0a84aee:briefer",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_roadmap",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-22T05:56:47.464402+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:dm:oc_1d29ca787d17733ae295957cd0a84aee:briefer",
  "tool": "ToolSearch",
  "elapsed_ms": 692
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-22T05:56:49.424941+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "file": "memory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:dm:oc_1d29ca787d17733ae295957cd0a84aee:briefer",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "file": "memory.md"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-22T05:56:50.070298+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/memory.md\", \"content\": \"# Memory — policy_ambiguity_safety\\n\\n## 竞品实验参考\\n（见 literature_map.yaml）\\n\\n## 经验教训\\n\\n### 5-Model Error Analysis 发现 (2026-05-21)\\n- **Layer mechanism 不是 clean dichotomy**：2-model 分析说 spec-layer = guess-and-act, linguistic-layer = misparse-and-apply。但 5-model 数据显示 conditional_precedence (spec-layer) 的 dominant FM 是 scope_misapplication（5/5 unanimous），与 linguistic-layer 一致。Failure mode 是 **type-specific** 而非 layer-specific。\\n- **Disambiguation awareness 有 model family 差异**：Claude 11.0%, GPT-4.1 10.7%（有一定 awareness），Qwen3 0%, DeepSeek 0%（完全 blind）。Overall 4.6%。\\n- **Claude conservative profile**：scope_misapplication dominant (50.5%), conservative_refusal highest (8.8%)，与低 violation rate (30.3%) 一致。\\n- **Inter-coder kappa 下降**：5-model κ=0.517 vs 2-model κ=0.594。新 3 模型的 traces 可能更难分类。\\n\\n### 已验证的模型 ID (OpenRouter proxy)\\n- `gpt-5.4` — 直接用，无 provider prefix\\n- `gpt-4.1` — 直接用\\n- `anthropic/claude-sonnet-4-6` — 需要 provider prefix\\n- `qwen/qwen3-235b-a22b` — 需要 provider prefix\\n- `deepseek/deepseek-chat-v3-0324` — 需要 provider prefix\\n- Base URL: `http://47.94.22.126/v1`\\n\\n### 运行脚本注意事项\\n- 必须用 `.venv/bin/python3` 而非系统 `python3`，因为 `core.crypto` 依赖 `cryptography` 包只在 venv 中\\n- 必须设置 `PYTHONUNBUFFERED=1` 否则 nohup 输出为空（Python stdout buffering）\\n- `core.crypto` 模块在 `/home/ubuntu/agent-ml-research/core/crypto.py`，脚本通过 `sys.path.insert(0, \\\"/home/ubuntu/agent-ml-research\\\")` 加载\\n\", \"total_chars\": 1360, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:dm:oc_1d29ca787d17733ae295957cd0a84aee:briefer",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 645
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-22T05:56:50.070722+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "file": "report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:dm:oc_1d29ca787d17733ae295957cd0a84aee:briefer",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "file": "report.md"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-22T05:56:50.472426+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/report.md\", \"content\": \"# Handover — 2026-05-22\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **plan_009** (success): Cross-judge LLM agreement (gpt-5.4 vs gpt-4.1) achieves substantial agreement (weighted κ ≥ 0.60) on violation level classification. LLM-human agreement should be comparable, validating the cross-judge evaluation design.\\n  [plan_009_annotation_guidelines](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/report/annotation_guidelines.md) | [plan_009_annotation_sheet](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/data/annotation_sheet.jsonl) | [plan_009_llm_agreement](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/report/llm_agreement.json) | [plan_009_annotation_sheet_clean](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/data/annotation_sheet_clean.jsonl)\\n- **plan_014** (success): Expanding perturbation control from n=120 to n=300 will maintain non-significant Δ_perturb (CI containing zero) while narrowing CI upper bound from 13.3pp to ~8pp, strengthening SESOI justification for C1 causal inference ← 基于 plan_010\\n  [plan_014_extended_perturbation_results](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_014/data/results.json) | [plan_014_perturbation_clauses_extended](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_014/data/clauses_perturbation_extended.json) | [plan_014_run_script](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_014/intermediate/run_plan014.py)\\n- **plan_015** (success): Authorization scope violations are predominantly unauthorized escalation (granting excess permissions) rather than restriction, consistent across all 5 models, revealing systematic permissiveness bias under boundar
…[truncated 222 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:dm:oc_1d29ca787d17733ae295957cd0a84aee:briefer",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 401
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-22T05:56:50.472798+00:00_

called mcp__agent-ml-research__read_roadmap

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_roadmap</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:dm:oc_1d29ca787d17733ae295957cd0a84aee:briefer",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-22T05:56:51.111295+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/ROADMAP.md\", \"content\": \"# policy_ambiguity_safety — Research Dashboard\\n\\n> 最后更新: 2026-05-22 00:59 UTC | 更新原因: 修正 orphan bib 假阳性（tamkin/yin 为有效引用）、清理已完成任务、添加 plan_009 bookkeeping\\n\\n> 详见 paper_framing.md\\n\\n## 核心方向\\nPolicy ambiguity causes universal safety violations (+34.0pp, OR=15.1, 7 models × 6 providers), with incompleteness as consistent upper-bound risk type (46-62% across all models). Disambiguation Deficit: <11% awareness. 详见 paper_framing.md\\n\\n## 当前阶段: **Round 11 审稿待审批**\\n\\nRound 9 (fresh): 3.5 → Round 10 (fresh): 3.5。审稿人明确指出 \\\"有 4.0 Conference 潜力\\\"，核心阻碍是 claims-evidence calibration gap。Round 10 已执行全部升分条件：\\n- MF1: auth scope 52pp 标为 upper bound + C4 sans auth scope 分析（p=0.97，interaction 完全由 auth scope 驱动）\\n- MF2: two-tier hierarchy 弱化为 \\\"incompleteness as consistent upper-bound risk type\\\"\\n- 4 项新 robustness 分析集成到 Appendix（C4 decomposition、per-type token delta、within-judge C2、sans-incompleteness C1）\\n- Method 事实修正（judge assignment）\\n- DN credit 归属修正（Willis et al. 2008）\\n- Disambiguation Deficit 定义明确 \\\"default behavioral pattern, not inherent inability\\\"\\n\\nRound 11 审稿已提交（continue 模式），待用户审批。\\n\\n## Claim 覆盖率 (5+2 models)\\n\\n| Claim | 状态 | 关键数据 |\\n|-------|------|---------|\\n| C1 Binary Effect | ✅ confirmed (7/7 models) | +34.0pp, OR=15.1; sans-incompleteness Δ=31.0pp |\\n| C2 Type Hierarchy | ✅ confirmed (upper bound + margin-dependent tiers) | V=0.137; incompleteness ≥46% all 7 models |\\n| C3 Layer Effect | ⚠️ inconclusive | Δ=6.08pp, p=0.017, Holm-Bonferroni fails |\\n| C4 Model×Type | ✅ exploratory (hedged) | F(20)=1.97, p=0.006; sans auth scope p=0.97 |\\n| C5 Error Analysis | ✅ coded | 614 traces; Disambiguation Deficit <11% |\\n\\n## 实验完成状态\\n\\n12 成功 / 3 阴性，无 GPU 需求（全 API 实验）。阴性实验影响评估：\\n- mvp_001: 初始 MVP 迭代，已被后续实验替代\\n- plan_002: 早期方法探索，不影响当前 story\\n- diag_001: C3 layer 
…[truncated 1974 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:dm:oc_1d29ca787d17733ae295957cd0a84aee:briefer",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 638
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-22T05:56:51.111649+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:dm:oc_1d29ca787d17733ae295957cd0a84aee:briefer",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-22T05:56:51.741892+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"plan_009\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T16:28:11.387Z\", \"updated_at\": \"2026-05-22T01:02:20.222Z\", \"hypothesis\": \"Cross-judge LLM agreement (gpt-5.4 vs gpt-4.1) achieves substantial agreement (weighted κ ≥ 0.60) on violation level classification. LLM-human agreement should be comparable, validating the cross-judge evaluation design.\", \"conclusion\": \"success\", \"metrics\": {\"cross_judge_kappa_weighted\": 0.685, \"cross_judge_exact_agreement\": 0.76, \"cross_judge_binary_kappa\": 0.74, \"human_llm_pooled_kappa_weighted\": 0.807, \"human_inter_annotator_kappa_weighted\": 0.762, \"n_episodes\": 100}}, \"plan_014\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T10:57:21.805Z\", \"updated_at\": \"2026-05-21T11:10:40.914Z\", \"hypothesis\": \"Expanding perturbation control from n=120 to n=300 will maintain non-significant Δ_perturb (CI containing zero) while narrowing CI upper bound from 13.3pp to ~8pp, strengthening SESOI justification for C1 causal inference\", \"parent\": \"plan_010\", \"conclusion\": \"success\", \"metrics\": {\"n_episodes\": 300, \"delta_perturb_pp\": -0.67, \"ci_95_bootstrap\": [-8, 6.67], \"ci_upper_bound\": 6.67, \"ci_width\": 14.67, \"mcnemar_p\": 1, \"verdict\": \"PASS\", \"plan_010_ci_upper\": 13.33, \"ci_upper_reduction\": 6.66}}, \"plan_015\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T10:57:22.179Z\", \"updated_at\": \"2026-05-21T11:00:42.716Z\", \"hypothesis\": \"Authorization scope violations are predominantly unauthorized escalation (granting excess permissions) rather than restriction, consistent across all 5 models, revealing systematic permissiveness bias under boundary ambiguity\", \"conclusion\": \"success\", \"metrics\": {\"pooled_escalation_rate\": 0.692, \"pooled_restriction_rate\": 0, \"binomial_p\": 5.5e-05, \"models_majority_escalation\": \"4/5\", \"n_total\": 104, \"n_escalation\": 72}}, \"plan_013\": {\"status\": \
…[truncated 8149 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:dm:oc_1d29ca787d17733ae295957cd0a84aee:briefer",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 630
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-22T05:57:12.858842+00:00_

## 核心 Claim

这个项目研究的是 **策略文档中的语言歧义如何导致 LLM Agent 的安全违规**。投稿目标是 EMNLP 2026 ARR。

论文有 5 个 claim：

| Claim | 内容 | 状态 |
|-------|------|------|
| **C1** Binary Effect | 策略歧义导致违规率大幅上升 +34.0pp（OR=15.1），**7个模型全部复现** | ✅ 已确认 |
| **C2** Type Hierarchy | 6种歧义类型中 incompleteness 是一致的上界风险类型（所有模型 ≥46%） | ✅ 已确认 |
| **C3** Layer Effect | specification-layer 比 linguistic-layer 更危险（Δ=6.08pp），但统计校正后不显著 | ⚠️ inconclusive |
| **C4** Model×Type Interaction | 不同模型对不同歧义类型的脆弱性不同，但交互效应完全由 auth_scope 驱动 | ✅ 探索性（已 hedge） |
| **C5** Error Analysis | 614条违规trace的failure mode分析；模型几乎不会主动识别歧义（awareness <11%） | ✅ 已完成 |

**一句话核心 claim**：策略文档中的歧义是 LLM Agent 安全违规的系统性原因，效应跨模型架构普遍存在（7模型 × 6 provider），且模型几乎没有自主消歧能力。

## 实验状态

共 **16 个实验**，成功 13 / 阴性 3 / 失败 0。全部完成，无在跑实验。全是 API 实验，不需要 GPU。

关键实验链：
- **plan_002 → plan_003a/3b/002c → plan_004**：从 2 模型扩展到 5 模型（GPT-4.1, GPT-5.4, Claude Sonnet 4.6, Qwen3-235B, DeepSeek V3），确认 C1-C4
- **plan_013**：再加 Gemini 2.5 Flash 和 LLaMA 4 Scout，7/7 模型 C1 复现
- **plan_006**：可复现性验证（ICC ≥ 0.75）
- **plan_009**：cross-judge 标注一致性（κ_w=0.685，human-LLM κ_w=0.807）
- **plan_010/005**：failure mode 错误分析（614 traces）
- **plan_011**：消歧指令缓解实验（整体降 6.6pp，auth_scope 降 18pp，但效果有限）
- **plan_014**：扩展扰动控制（n=300），CI 上界从 13.3pp 收窄到 6.67pp

## 当前进度

论文已写完（8页主文合规），Round 10 审稿得分 3.5（Borderline Conference），审稿人明确说"有 4.0 潜力"。Round 11 审稿已提交，等待用户审批和结果返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:dm:oc_1d29ca787d17733ae295957cd0a84aee:briefer"
}
```

</details>

---
